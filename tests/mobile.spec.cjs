const { test, expect } = require("@playwright/test");
const fs = require("fs");
const path = require("path");

async function selectObjective(page, needle) {
  const value = await page.locator("#mobileLessonSelect option").evaluateAll(
    (options, text) => options.find(option => option.textContent.includes(text))?.value || "",
    needle
  );
  expect(value, `Missing objective option containing: ${needle}`).not.toBe("");
  await page.locator("#mobileLessonSelect").selectOption(value);
  await page.waitForTimeout(80);
  return value;
}

async function documentRatio(page) {
  return page.evaluate(() => {
    const max = Math.max(0, document.documentElement.scrollHeight - innerHeight);
    return max > 0 ? scrollY / max : 0;
  });
}

test.beforeEach(async ({ page }) => {
  await page.addInitScript(() => localStorage.clear());
  await page.goto("/", { waitUntil: "domcontentloaded" });
  await expect(page.locator("#mobileLessonSelect")).toBeVisible();
});

test("mobile layout uses one scroll surface and touch-sized controls", async ({ page }) => {
  const metrics = await page.evaluate(() => {
    const pane = document.querySelector(".pane");
    const bottom = document.querySelector(".bottom");
    const summary = document.querySelector(".more-menu > summary");
    const language = document.querySelector("#languageMode");
    const next = document.querySelector("#nextBtn");
    const rect = element => {
      const r = element.getBoundingClientRect();
      return { width: r.width, height: r.height, top: r.top, bottom: r.bottom };
    };
    return {
      coarse: matchMedia("(pointer:coarse)").matches,
      horizontalOverflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
      paneOverflowY: getComputedStyle(pane).overflowY,
      paneScrollDelta: pane.scrollHeight - pane.clientHeight,
      syncDisplay: getComputedStyle(document.querySelector("#syncBtn")).display,
      bottomPosition: getComputedStyle(bottom).position,
      summary: rect(summary),
      language: rect(language),
      next: rect(next)
    };
  });

  expect(metrics.coarse).toBe(true);
  expect(metrics.horizontalOverflow).toBeLessThanOrEqual(1);
  expect(metrics.paneOverflowY).toBe("visible");
  expect(Math.abs(metrics.paneScrollDelta)).toBeLessThanOrEqual(2);
  expect(metrics.syncDisplay).toBe("none");
  expect(metrics.bottomPosition).toBe("fixed");
  expect(metrics.summary.height).toBeGreaterThanOrEqual(44);
  expect(metrics.language.height).toBeGreaterThanOrEqual(44);
  expect(metrics.next.height).toBeGreaterThanOrEqual(44);
  await expect(page.locator("#mobileProgress")).toHaveText("0 / 27 complete · 0%");
});

test("language modes and objective navigation remain usable", async ({ page }) => {
  const language = page.locator("#languageMode");

  await language.selectOption("en");
  await expect(page.locator("#enPane")).toBeVisible();
  await expect(page.locator("#ugPane")).toBeHidden();

  await language.selectOption("ug");
  await expect(page.locator("#enPane")).toBeHidden();
  await expect(page.locator("#ugPane")).toBeVisible();

  await language.selectOption("both");
  await expect(page.locator("#enPane")).toBeVisible();
  await expect(page.locator("#ugPane")).toBeVisible();

  const first = await selectObjective(page, "Objective 1.1");
  expect(page.locator("#mobileLessonSelect")).toHaveValue(first);

  await page.locator("#nextBtn").click();
  await expect(page.locator("#mobileLessonSelect")).toHaveValue(String(Number(first) + 1));

  await page.locator("#prevBtn").click();
  await expect(page.locator("#mobileLessonSelect")).toHaveValue(first);
});

test("More menu closes on outside tap and Escape returns focus", async ({ page }) => {
  const details = page.locator("details.more-menu");
  const summary = details.locator("summary");

  await summary.click();
  await expect(details).toHaveAttribute("open", "");
  const popover = await page.locator(".more-popover").boundingBox();
  const viewport = page.viewportSize();
  expect(popover).not.toBeNull();
  expect(viewport).not.toBeNull();
  await page.mouse.click(Math.max(4, popover.x - 12), Math.min(viewport.height - 80, popover.y + 80));
  await expect(details).not.toHaveAttribute("open", "");

  await summary.click();
  await expect(details).toHaveAttribute("open", "");
  await page.keyboard.press("Escape");
  await expect(details).not.toHaveAttribute("open", "");
  await expect(summary).toBeFocused();
});

test("Reading Focus follows the visible paragraph while scrolling", async ({ page }) => {
  await selectObjective(page, "Objective 1.1");

  const details = page.locator("details.more-menu");
  await details.locator("summary").click();
  await page.locator("#focusLineBtn").click();
  await page.keyboard.press("Escape");

  const focused = page.locator(".article .focus-line");
  await expect(focused).toHaveCount(1);
  const before = (await focused.textContent() || "").trim();

  await page.evaluate(() => {
    const max = Math.max(0, document.documentElement.scrollHeight - innerHeight);
    scrollTo(0, max * 0.55);
  });
  await page.waitForTimeout(200);

  await expect(focused).toHaveCount(1);
  const after = (await focused.textContent() || "").trim();
  expect(after).not.toBe(before);

  const visibility = await focused.evaluate(element => {
    const r = element.getBoundingClientRect();
    const top = document.querySelector(".top")?.getBoundingClientRect().bottom || 0;
    const bottom = document.querySelector(".bottom")?.getBoundingClientRect().top || innerHeight;
    return { elementTop: r.top, elementBottom: r.bottom, visibleTop: top, visibleBottom: bottom };
  });
  expect(visibility.elementBottom).toBeGreaterThan(visibility.visibleTop);
  expect(visibility.elementTop).toBeLessThan(visibility.visibleBottom);
});

test("Resume reading restores the saved mobile document position", async ({ page }) => {
  await selectObjective(page, "Objective 1.1");

  await page.evaluate(() => {
    const max = Math.max(0, document.documentElement.scrollHeight - innerHeight);
    scrollTo(0, max * 0.4);
  });
  await page.waitForTimeout(220);

  const stored = await page.evaluate(() => Number(localStorage.getItem("a1-scroll-ratio-1.1") || 0));
  expect(stored).toBeGreaterThan(0.2);

  await selectObjective(page, "Objective 1.2");
  await selectObjective(page, "Objective 1.1");
  expect(await documentRatio(page)).toBeLessThan(0.08);

  const details = page.locator("details.more-menu");
  await details.locator("summary").click();
  await expect(page.locator("#resumePill")).toBeVisible();
  await page.locator("#resumePill").click();
  await page.waitForTimeout(120);

  const restored = await documentRatio(page);
  expect(restored).toBeGreaterThan(0.2);
  expect(Math.abs(restored - stored)).toBeLessThan(0.15);
});

test("Cards and Columns preserve approximate mobile reading position", async ({ page }) => {
  await selectObjective(page, "Objective 1.1");

  await page.evaluate(() => {
    const max = Math.max(0, document.documentElement.scrollHeight - innerHeight);
    scrollTo(0, max * 0.35);
  });
  await page.waitForTimeout(120);
  const columnsRatio = await documentRatio(page);

  await expect(page.locator("#pairBtn")).toBeVisible();
  await page.locator("#pairBtn").evaluate(button => button.click());
  await expect(page.locator("body")).toHaveClass(/pairs/);
  await page.waitForTimeout(180);
  const cardsRatio = await documentRatio(page);
  expect(Math.abs(cardsRatio - columnsRatio)).toBeLessThan(0.16);

  await page.locator("#pairBtn").evaluate(button => button.click());
  await expect(page.locator("body")).not.toHaveClass(/pairs/);
  await page.waitForTimeout(180);
  const columnsAgain = await documentRatio(page);
  expect(Math.abs(columnsAgain - cardsRatio)).toBeLessThan(0.16);
});


test("mobile search opens course results and navigates to a hit", async ({ page }) => {
  const search = page.locator("#lessonSearch");
  await search.fill("DHCP");
  const results = page.locator("#globalResults");
  await expect(results).toHaveClass(/open/);
  const first = results.locator(".search-hit").first();
  await expect(first).toBeVisible();
  const targetIndex = await first.getAttribute("data-i");
  expect(targetIndex).not.toBeNull();

  await first.click();
  await expect(page.locator("#mobileLessonSelect")).toHaveValue(targetIndex);
  await expect(results).not.toHaveClass(/open/);
});

test("touch Copy writes the selected paragraph to the clipboard", async ({ page, context }) => {
  await context.grantPermissions(["clipboard-read", "clipboard-write"], {
    origin: "http://127.0.0.1:8080"
  });
  await selectObjective(page, "Objective 1.1");

  const paragraph = page.locator("#enArticle p").first();
  await paragraph.tap();
  const copy = paragraph.locator(".copybtn");
  await expect(copy).toHaveCSS("pointer-events", "auto");
  await copy.click();
  await expect(page.locator("#toast")).toContainText("Copied");

  const copied = await page.evaluate(() => navigator.clipboard.readText());
  expect(copied.trim().length).toBeGreaterThan(10);
});

test("PWA app shell reloads while offline after service worker installation", async ({ page, context }) => {
  await page.evaluate(async () => {
    if (!("serviceWorker" in navigator)) throw new Error("Service workers unavailable");
    await navigator.serviceWorker.ready;
  });

  // Reload online once so the page is definitely controlled by the installed worker.
  await page.reload({ waitUntil: "domcontentloaded" });
  await expect(page.locator("#mobileLessonSelect")).toBeVisible();
  await expect.poll(() => page.evaluate(() => Boolean(navigator.serviceWorker.controller))).toBe(true);

  await context.setOffline(true);
  try {
    await page.reload({ waitUntil: "domcontentloaded" });
    await expect(page.locator("#mobileLessonSelect")).toBeVisible();
    await expect(page.locator("#netStatus")).toHaveText("Offline");
  } finally {
    await context.setOffline(false);
  }
});

test("visible interactive controls have accessible names and IDs stay unique", async ({ page }) => {
  const audit = await page.evaluate(() => {
    const ids = [...document.querySelectorAll("[id]")].map(element => element.id);
    const duplicates = [...new Set(ids.filter((id, index) => ids.indexOf(id) !== index))];

    const visible = element => {
      const style = getComputedStyle(element);
      const rect = element.getBoundingClientRect();
      return style.display !== "none" && style.visibility !== "hidden" && rect.width > 0 && rect.height > 0;
    };
    const labelledBy = element => (element.getAttribute("aria-labelledby") || "")
      .split(/\s+/)
      .filter(Boolean)
      .map(id => document.getElementById(id)?.textContent || "")
      .join(" ");
    const accessibleName = element => [
      element.getAttribute("aria-label"),
      labelledBy(element),
      element.labels ? [...element.labels].map(label => label.textContent).join(" ") : "",
      element.getAttribute("title"),
      element.getAttribute("placeholder"),
      element.textContent
    ].filter(Boolean).join(" ").trim();

    const unnamed = [...document.querySelectorAll("button,summary,select,input,textarea")]
      .filter(visible)
      .filter(element => !accessibleName(element))
      .map(element => element.id || element.outerHTML.slice(0, 120));

    return { duplicates, unnamed };
  });

  expect(audit.duplicates).toEqual([]);
  expect(audit.unnamed).toEqual([]);
});

test("capture mobile reader, menu, and focus screenshots", async ({ page }, testInfo) => {
  await selectObjective(page, "Objective 1.1");

  const dir = path.join(process.cwd(), "artifacts", "mobile-screenshots");
  fs.mkdirSync(dir, { recursive: true });
  const prefix = testInfo.project.name;

  await page.screenshot({ path: path.join(dir, `${prefix}-reader.png`) });

  const details = page.locator("details.more-menu");
  await details.locator("summary").click();
  await page.screenshot({ path: path.join(dir, `${prefix}-more-menu.png`) });
  await page.keyboard.press("Escape");

  await details.locator("summary").click();
  await page.locator("#focusLineBtn").click();
  await page.keyboard.press("Escape");
  await page.evaluate(() => {
    const max = Math.max(0, document.documentElement.scrollHeight - innerHeight);
    scrollTo(0, max * 0.35);
  });
  await page.waitForTimeout(160);
  await page.screenshot({ path: path.join(dir, `${prefix}-reading-focus.png`) });
});

test("all objective Uyghur content avoids known learner-quality artifacts", async ({ page }) => {
  const priority = ["Objective 1.1", "Objective 1.2", "Objective 1.3", "Objective 2.1", "Objective 2.2", "Objective 2.3", "Objective 2.4", "Objective 2.5", "Objective 2.6", "Objective 2.7", "Objective 2.8", "Objective 3.1", "Objective 3.2", "Objective 3.3", "Objective 3.4", "Objective 3.5", "Objective 3.6", "Objective 3.7", "Objective 3.8", "Objective 4.1", "Objective 4.2", "Objective 5.1", "Objective 5.2", "Objective 5.3", "Objective 5.4", "Objective 5.5", "Objective 5.6"];
  const forbidden = [
    "Exam memory:",
    "Source-scope note:",
    "Source-framing note:",
    "Source-safety note:",
    "Source-accuracy note:",
    "Source-model caution:",
    "Source-boundary note:",
    "Source-attribution caution:",
    "Transcript correction:",
    "Reviewed Uyghur",
    "reviewed lesson",
    "Repair ياكى component replacement",
    "reviewed flow:",
    "Exam Objective ",
    "Source-Stated Possible Causes",
    "Source-stated benefits:",
    "Source teaching model:",
    "Source components:",
    "Source process:",
    "Source example:",
    "Source examples:",
    "learner-facing",
    "Original transcript",
    "قوزغىتىدۇ قىلىدۇ",
    "يۈكلەنمەيدۇ بولمايدۇ",
    "قايتا قۇرۇلىدۇ قىلىنىدۇ",
    "باشقۇرىدۇ قىلىدۇ",
    "سايلايدۇ قىلىدۇ",
    "چۈشىنىلىدۇ قىلىنىدۇ",
    "زىيارەت نى",
    "ئۆزگەرتىش دىن",
    "زىيارىتى قا",
    "ساقلاش سىغىمى غا",
    "بېشى نىڭ",
    "دەرس نىڭ"
  ];

  for (const objective of priority) {
    await selectObjective(page, objective);
    const uyghur = await page.locator("#ugArticle").innerText();
    for (const needle of forbidden) {
      expect(uyghur, objective + " still contains: " + needle).not.toContain(needle);
    }
  }

  const archived = fs.readFileSync(
    path.join(process.cwd(), "source", "comptia_a_core_1_Uyghur.txt"),
    "utf8"
  );
  expect(archived).not.toContain("مەنبەدەئىرىسى");
  expect(archived).not.toContain("ئالامەت / ئالامەت");
  expect(archived).not.toMatch(/[\u0600-\u06FF]s\b/);
  expect(archived).not.toContain("قوزغىتىدۇ قىلىدۇ");
  expect(archived).not.toContain("يۈكلەنمەيدۇ بولمايدۇ");
  expect(archived).not.toContain("قايتا قۇرۇلىدۇ قىلىنىدۇ");
  expect(archived).not.toContain("باشقۇرىدۇ قىلىدۇ");
  expect(archived).not.toContain("زىيارەت نى");
  expect(archived).not.toContain("ئۆزگەرتىش دىن");
  expect(archived).not.toContain("زىيارىتى قا");
  expect(archived.split(/\r?\n/).some(line => line.trim() === ".")).toBe(false);
});



test('learner-quality regression guard', async () => {
  const fs = require('node:fs');
  const path = require('node:path');
  const assert = require('node:assert/strict');

  const source = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
  const match = source.match(/const LESSONS = (\[.*?\]);\n/s);
  assert.ok(match, 'LESSONS data should remain parseable');

  const lessons = JSON.parse(match[1]);
  assert.equal(lessons.filter((lesson) => lesson.number !== 'Intro').length, 27);

  const bannedEditorial = [
    /Exam Objective/i,
    /\blearner-facing\b/i,
    /\bSource-stated\b/i,
    /Original transcript/i,
    /Reviewed Uyghur/i,
    /Source-scope note:/i,
    /Source-framing note:/i,
    /Transcript correction:/i,
    /§[A-Z]\d+§/,
  ];
  const malformedUyghur = [
    /قوزغىتىدۇ\s+قىلىدۇ/,
    /يۈكلىنىدۇ\s+قىلىدۇ/,
    /باشقۇرىدۇ\s+قىلىدۇ/,
    /ئۆتكۈزۈۋالىدۇ\s+قىلىش/,
    /ئەسلىگە كەلتۈرۈشى\s+قىلىشى/,
    /زىيارەت\s+نى/,
    /ئۆزگەرتىش\s+دىن/,
    /ئۇلىنىش\s+نى/,
    /تەڭشەك\s+نى/,
    /كابېل\s+نى/,
    /پورت\s+نى/,
    /ئۈسكۈنە\s+نى/,
  ];

  for (const lesson of lessons) {
    assert.match(lesson.uyghur, /[\u0600-\u06FF]/, `${lesson.number} should contain Uyghur text`);
    for (const pattern of [...bannedEditorial, ...malformedUyghur]) {
      assert.equal(pattern.test(lesson.uyghur), false, `${lesson.number} contains learner-quality artifact: ${pattern}`);
    }
  }
});
