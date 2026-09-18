# CompTIA A+ Core 1 — English ↔ Uyghur Study Reader

A bilingual CompTIA A+ Core 1 study app with English and Uyghur side by side.

## Features

- 27 CompTIA A+ Core 1 exam objectives
- English ↔ Uyghur bilingual reading
- Improved Uyghur Arabic-script typography and RTL handling
- Search, bookmarks, progress and personal notes
- Active recall: hide English or hide Uyghur
- Offline/PWA support
- Shareable objective links
- Installable on supported browsers/devices
- Cloudflare Workers Static Assets deployment
- Verified V5.2 runtime fixes and safer saved-state handling

## Cloudflare deployment

This repository is configured for **Cloudflare Workers Static Assets**.

Cloudflare deploy command:

```bash
npx wrangler deploy
```

The permanent configuration is stored in `wrangler.jsonc`:

- Worker: `comptia-a-core-1`
- Static assets directory: repository root (`.`)
- Production branch: `main`

`package.json` pins the Wrangler version used by the project so future deployments are more predictable.

## Static asset controls

`.assetsignore` prevents repository-only files such as `README.md`, `source/`,
Wrangler configuration and local development files from being published as website assets.

Keep these deployment files in the root because Wrangler reads them while deploying:

- `_headers`
- `_redirects`

## Offline Uyghur font behavior

The preferred online font remains **Noto Naskh Arabic**. The service worker now caches
Google Fonts resources after the first successful online visit, so later offline visits can
continue using the preferred Uyghur typography when those resources have already been loaded.

The app still has local fallback fonts when the preferred web font is unavailable.

## Local preview

Basic preview:

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

For Cloudflare-local behavior:

```bash
npm install
npm run dev
```

## User data

Study progress, bookmarks, reading position, font settings and notes are stored locally in the browser.

## V5.2 verification

V5.2 fixes the study-card alignment boundary bug, improves reading-position resume, validates saved browser settings safely, and preserves the chosen language layout. The original transcript remains in `source/`; obvious speech-to-text term corrections used by the study display are documented in `TRANSCRIPT_CORRECTIONS.md`.


## V5.30 UI refresh

- Cleaner two-level study toolbar
- Improved visual hierarchy and reading width
- Refined English/Uyghur language panes
- More readable objective navigation and progress
- Mobile objective selector
- Sticky mobile previous/next navigation
- Preserves the verified V5.2 study engine and storage behavior


## Translation review status

All 27 exam objectives have completed technical/source-fidelity review. **V6.8 introduced the broad Uyghur language-polish pass; V6.9 is the learner-quality audit of the published reader.** V6.9 began with line-by-line review of **3.2, 3.3, and 3.5**, then extended the same standard across the remaining objectives after the audit found older English-heavy study scaffolding in Domains 1, 2, storage/RAID, virtualization/cloud, power/printer content, and troubleshooting summaries.

The published Uyghur reader now favors natural Uyghur for explanations, headings, comparison tables, troubleshooting actions and exam-memory cues while keeping canonical exam-recognition terms visible where useful, including acronyms, protocol names, connector/standard identifiers, formulas, official English expansions and explicitly quoted source wording.

The archived Uyghur source remains intentionally fuller than the published lesson text and is **not** replaced wholesale by the shorter reader version. It keeps the prior deterministic cleanup for malformed wording and formatting artifacts, while V6.9 regression tests now scan **all 27 objectives** plus the archive for known learner-quality regressions.

## V6 study workspace redesign

The V6 interface keeps the reviewed V5.30 bilingual lesson content and study engine while making the app substantially calmer and easier to scan. Course navigation, objective controls, and the bilingual reader now have distinct visual levels; secondary toolbar actions are grouped under **More**; English and Uyghur reading panes use improved typography and spacing; and mobile navigation has been refined for phone-sized study sessions.

Existing browser-saved progress, bookmarks, notes, font choice, reading position, language layout, and recall settings remain compatible.


## V6.9 learner-quality release

V6.9.0 completes a full learner-language audit of all 27 objectives. It keeps exam-standard technical identifiers in English where useful, while translating ordinary explanatory scaffolding into clearer Uyghur. The release also adds a regression guard for recurring editorial and mixed-language grammar artifacts.

See [V6_9_LEARNER_QUALITY_AUDIT.md](V6_9_LEARNER_QUALITY_AUDIT.md) for scope and release criteria.
