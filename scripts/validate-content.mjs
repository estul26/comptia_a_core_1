import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(scriptDir, '..');

const failures = [];
const successes = [];

function pass(message) {
  successes.push(message);
  console.log(`✓ ${message}`);
}

function fail(message) {
  failures.push(message);
  console.error(`✗ ${message}`);
}

function read(relativePath) {
  const absolutePath = path.join(root, relativePath);
  if (!fs.existsSync(absolutePath)) {
    fail(`Missing required file: ${relativePath}`);
    return null;
  }
  return fs.readFileSync(absolutePath, 'utf8');
}

function parseJson(relativePath) {
  const text = read(relativePath);
  if (text === null) return null;
  try {
    const value = JSON.parse(text);
    pass(`${relativePath} is valid JSON`);
    return value;
  } catch (error) {
    fail(`${relativePath} is invalid JSON: ${error.message}`);
    return null;
  }
}

function uniqueDuplicates(values) {
  const seen = new Set();
  const duplicates = new Set();
  for (const value of values) {
    if (seen.has(value)) duplicates.add(value);
    seen.add(value);
  }
  return [...duplicates];
}

function normalizeLocalAsset(assetPath) {
  if (assetPath === '/') return 'index.html';
  return assetPath.replace(/^\//, '').split(/[?#]/, 1)[0];
}

function fileExistsForWebPath(assetPath) {
  if (!assetPath || /^(?:https?:)?\/\//i.test(assetPath) || assetPath.startsWith('data:')) {
    return true;
  }
  const relativePath = normalizeLocalAsset(assetPath);
  return Boolean(relativePath) && fs.existsSync(path.join(root, relativePath));
}

const html = read('index.html');
const sw = read('sw.js');
const manifest = parseJson('manifest.webmanifest');
const pkg = parseJson('package.json');

if (pkg) {
  if (typeof pkg.version === 'string' && /^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$/.test(pkg.version)) {
    pass(`package version is valid semver-like text (${pkg.version})`);
  } else {
    fail('package.json must contain a valid version');
  }

  const wrangler = pkg.devDependencies?.wrangler;
  if (typeof wrangler === 'string' && /^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$/.test(wrangler)) {
    pass(`Wrangler is pinned exactly (${wrangler})`);
  } else {
    fail('Wrangler must be pinned to an exact version in devDependencies');
  }
}

if (html) {
  const lessonMatch = html.match(/const\s+LESSONS\s*=\s*(\[[\s\S]*?\])\s*;\s*const\s+domainLabels\s*=/);
  if (!lessonMatch) {
    fail('Could not locate the LESSONS data array in index.html');
  } else {
    try {
      const lessonScript = new vm.Script(`(${lessonMatch[1]})`, { filename: 'LESSONS-data.js' });
      const lessons = lessonScript.runInNewContext(Object.create(null), { timeout: 1000 });
      const expectedIds = [
        'intro',
        '1.1', '1.2', '1.3',
        '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8',
        '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8',
        '4.1', '4.2',
        '5.1', '5.2', '5.3', '5.4', '5.5', '5.6'
      ];

      if (lessons.length === expectedIds.length) {
        pass(`LESSONS contains ${lessons.length} entries (Introduction + 27 objectives)`);
      } else {
        fail(`LESSONS should contain ${expectedIds.length} entries but contains ${lessons.length}`);
      }

      const ids = lessons.map(lesson => lesson?.id);
      const duplicateLessonIds = uniqueDuplicates(ids);
      if (duplicateLessonIds.length === 0) {
        pass('Lesson/objective IDs are unique');
      } else {
        fail(`Duplicate lesson/objective IDs: ${duplicateLessonIds.join(', ')}`);
      }

      if (JSON.stringify(ids) === JSON.stringify(expectedIds)) {
        pass('All expected objective IDs exist in the expected order');
      } else {
        const missing = expectedIds.filter(id => !ids.includes(id));
        const unexpected = ids.filter(id => !expectedIds.includes(id));
        if (missing.length) fail(`Missing objective IDs: ${missing.join(', ')}`);
        if (unexpected.length) fail(`Unexpected objective IDs: ${unexpected.join(', ')}`);
        if (!missing.length && !unexpected.length) fail('Objective IDs are present but not in the expected order');
      }

      const emptyEnglish = lessons.filter(lesson => typeof lesson?.english !== 'string' || !lesson.english.trim()).map(lesson => lesson?.id ?? '(unknown)');
      const emptyUyghur = lessons.filter(lesson => typeof lesson?.uyghur !== 'string' || !lesson.uyghur.trim()).map(lesson => lesson?.id ?? '(unknown)');
      const missingEnglishTitles = lessons.filter(lesson => typeof lesson?.domain_en !== 'string' || !lesson.domain_en.trim()).map(lesson => lesson?.id ?? '(unknown)');
      const missingUyghurTitles = lessons.filter(lesson => typeof lesson?.domain_ug !== 'string' || !lesson.domain_ug.trim()).map(lesson => lesson?.id ?? '(unknown)');

      if (!emptyEnglish.length) pass('Every lesson has English content');
      else fail(`Lessons with empty English content: ${emptyEnglish.join(', ')}`);

      if (!emptyUyghur.length) pass('Every lesson has Uyghur content');
      else fail(`Lessons with empty Uyghur content: ${emptyUyghur.join(', ')}`);

      if (!missingEnglishTitles.length) pass('Every lesson has an English domain/title label');
      else fail(`Lessons missing English labels: ${missingEnglishTitles.join(', ')}`);

      if (!missingUyghurTitles.length) pass('Every lesson has a Uyghur domain/title label');
      else fail(`Lessons missing Uyghur labels: ${missingUyghurTitles.join(', ')}`);
    } catch (error) {
      fail(`LESSONS data could not be parsed safely: ${error.message}`);
    }
  }

  const htmlWithoutExecutableBlocks = html
    .replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, '')
    .replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi, '');

  const staticIds = [...htmlWithoutExecutableBlocks.matchAll(/\bid\s*=\s*["']([^"']+)["']/gi)].map(match => match[1]);
  const duplicateStaticIds = uniqueDuplicates(staticIds);
  if (!duplicateStaticIds.length) pass(`Static HTML IDs are unique (${staticIds.length} IDs)`);
  else fail(`Duplicate static HTML IDs: ${duplicateStaticIds.join(', ')}`);

  const inlineScripts = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .filter(match => !/\bsrc\s*=/.test(match[1]))
    .map(match => match[2]);

  if (!inlineScripts.length) {
    fail('No inline application script found in index.html');
  } else {
    inlineScripts.forEach((code, index) => {
      try {
        new vm.Script(code, { filename: `index.html:inline-script-${index + 1}.js` });
        pass(`Inline JavaScript block ${index + 1} parses successfully`);
      } catch (error) {
        fail(`Inline JavaScript block ${index + 1} has a syntax error: ${error.message}`);
      }
    });

    const combinedScript = inlineScripts.join('\n');
    const domRefs = [...combinedScript.matchAll(/\$\(\s*["']([^"']+)["']\s*\)/g)].map(match => match[1]);
    const missingDomRefs = [...new Set(domRefs)].filter(id => !staticIds.includes(id));
    if (!missingDomRefs.length) pass(`All ${new Set(domRefs).size} literal $() DOM references point to existing static IDs`);
    else fail(`JavaScript references missing HTML IDs: ${missingDomRefs.join(', ')}`);
  }

  const localHeadAssets = [];
  for (const match of htmlWithoutExecutableBlocks.matchAll(/<(?:link|script)\b[^>]*(?:href|src)\s*=\s*["']([^"']+)["'][^>]*>/gi)) {
    const asset = match[1];
    if (asset.startsWith('/')) localHeadAssets.push(asset);
  }
  const missingHeadAssets = [...new Set(localHeadAssets)].filter(asset => !fileExistsForWebPath(asset));
  if (!missingHeadAssets.length) pass('Local linked head assets exist');
  else fail(`Missing local linked assets: ${missingHeadAssets.join(', ')}`);
}

if (sw) {
  try {
    new vm.Script(sw, { filename: 'sw.js' });
    pass('sw.js parses successfully');
  } catch (error) {
    fail(`sw.js has a syntax error: ${error.message}`);
  }

  const coreMatch = sw.match(/const\s+CORE\s*=\s*(\[[\s\S]*?\])\s*;/);
  if (!coreMatch) {
    fail('Could not locate CORE asset list in sw.js');
  } else {
    try {
      const coreAssets = JSON.parse(coreMatch[1]);
      const missingCoreAssets = coreAssets.filter(asset => !fileExistsForWebPath(asset));
      if (!missingCoreAssets.length) pass(`All ${coreAssets.length} service-worker core assets exist`);
      else fail(`Service-worker CORE paths are missing: ${missingCoreAssets.join(', ')}`);
    } catch (error) {
      fail(`Service-worker CORE list is invalid: ${error.message}`);
    }
  }
}

if (manifest) {
  if (manifest.start_url === '/') pass('PWA start_url is /');
  else fail(`Unexpected PWA start_url: ${String(manifest.start_url)}`);

  if (manifest.scope === '/') pass('PWA scope is /');
  else fail(`Unexpected PWA scope: ${String(manifest.scope)}`);

  const icons = Array.isArray(manifest.icons) ? manifest.icons : [];
  if (icons.length) {
    const missingIcons = icons.filter(icon => !fileExistsForWebPath(icon?.src)).map(icon => icon?.src ?? '(missing src)');
    if (!missingIcons.length) pass(`All ${icons.length} manifest icon entries resolve to existing files`);
    else fail(`Manifest icons are missing: ${missingIcons.join(', ')}`);
  } else {
    fail('manifest.webmanifest contains no icons');
  }
}

console.log(`\nValidation summary: ${successes.length} passed, ${failures.length} failed.`);
if (failures.length) process.exit(1);
