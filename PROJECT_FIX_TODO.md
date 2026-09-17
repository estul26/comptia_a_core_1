# Full Project Cleanup TODO

This checklist tracks the safe, incremental cleanup of the CompTIA A+ Core 1 English ↔ Uyghur study app.

## Rules for this cleanup

- Keep the current working app behavior intact.
- Do not change lesson meaning or Uyghur translations during code refactoring unless a separate content fix is documented.
- Make small commits.
- Validate after every structural change.
- Keep `main` stable; work on `fix/full-project-cleanup` first.
- Only move to the next phase after the current phase passes validation.

## Phase 0 — Safety baseline

- [x] Create dedicated cleanup branch: `fix/full-project-cleanup`
- [ ] Record current app version and baseline commit
- [ ] Capture baseline structural checks
- [ ] Confirm current app loads without JavaScript syntax errors
- [ ] Confirm current PWA manifest and service worker files are valid

## Phase 1 — Automated validation

- [ ] Add `scripts/validate-content.mjs`
- [ ] Validate all expected objective IDs exist
- [ ] Validate objective IDs are unique
- [ ] Validate English content is not empty
- [ ] Validate Uyghur content is not empty
- [ ] Detect duplicate HTML IDs
- [ ] Validate `manifest.webmanifest`
- [ ] Validate service-worker core asset paths
- [ ] Validate important internal references
- [ ] Add `npm run validate`
- [ ] Add `npm run check`

## Phase 2 — Reproducible development setup

- [ ] Commit `package-lock.json`
- [ ] Keep Wrangler pinned to an exact version
- [ ] Verify `npm ci` works from a clean checkout
- [ ] Document local development and validation commands

## Phase 3 — Continuous integration

- [ ] Add GitHub Actions validation workflow
- [ ] Run validation on pushes and pull requests
- [ ] Run JavaScript syntax checks in CI
- [ ] Verify CI passes on the cleanup branch

## Phase 4 — Deployment boundary cleanup

- [ ] Create dedicated production asset directory (`public/` or equivalent)
- [ ] Move only deployable assets into that directory
- [ ] Keep audits, source transcripts, review reports, and development docs outside production assets
- [ ] Update `wrangler.jsonc` to deploy only the production asset directory
- [ ] Recheck `_headers`
- [ ] Verify manifest, icons, service worker, and start URL after the move

## Phase 5 — Documentation organization

- [ ] Create `docs/audits/`
- [ ] Create `docs/objective-reviews/`
- [ ] Create `docs/translation/`
- [ ] Create `docs/releases/`
- [ ] Move historical audit/review documents without losing history
- [ ] Update README links after file moves

## Phase 6 — Service worker / PWA hardening

- [ ] Restrict cache cleanup to this app's cache prefix
- [ ] Make background cache refresh lifecycle-safe
- [ ] Make navigation cache writes lifecycle-safe
- [ ] Remove manual cache-version drift
- [ ] Verify offline fallback behavior
- [ ] Verify old caches are removed safely
- [ ] Verify PWA install still works

## Phase 7 — Split the giant `index.html`

- [ ] Extract CSS to a dedicated stylesheet
- [ ] Extract application JavaScript without behavior changes
- [ ] Separate storage/localStorage logic
- [ ] Separate search logic
- [ ] Separate progress/bookmark logic
- [ ] Separate notes logic
- [ ] Separate study-card/recall logic
- [ ] Separate UI/layout logic
- [ ] Keep objective/content data independent from UI code
- [ ] Re-run validation after every extraction

## Phase 8 — Browser regression tests

- [ ] Add browser test framework
- [ ] Test initial application load
- [ ] Test objective navigation
- [ ] Test English-only mode
- [ ] Test Uyghur-only mode
- [ ] Test bilingual mode
- [ ] Test search and search-result navigation
- [ ] Test bookmarks
- [ ] Test progress/completion persistence
- [ ] Test objective notes persistence
- [ ] Test dark mode
- [ ] Test focus/reading modes
- [ ] Test active-recall cards
- [ ] Test mobile layout/no horizontal overflow
- [ ] Test keyboard shortcuts
- [ ] Test offline behavior where practical

## Phase 9 — Code quality and security review

- [ ] Find duplicated functions and dead code
- [ ] Review `innerHTML`/DOM insertion paths
- [ ] Review URL/hash handling
- [ ] Review localStorage parsing and recovery paths
- [ ] Review event-listener cleanup/duplication
- [ ] Review accessibility labels and keyboard focus
- [ ] Review third-party/CDN dependencies
- [ ] Review security headers/CSP compatibility
- [ ] Fix confirmed issues one at a time with regression coverage

## Phase 10 — Performance cleanup

- [ ] Measure initial page size and parse cost
- [ ] Reduce unnecessary startup work
- [ ] Avoid repeated full-document queries where possible
- [ ] Lazy-load or defer nonessential work where useful
- [ ] Recheck mobile performance
- [ ] Compare before/after page weight and behavior

## Phase 11 — Release/version consistency

- [ ] Use one source of truth for app version
- [ ] Synchronize service-worker cache version automatically
- [ ] Generate or update release verification data from current build
- [ ] Replace stale V5.3-only verification status with current release validation
- [ ] Record commit SHA/date in release verification output

## Phase 12 — Final verification

- [ ] Run all static validation
- [ ] Run all browser regression tests
- [ ] Verify all objectives still render
- [ ] Verify English/Uyghur content integrity
- [ ] Verify progress/bookmarks/notes still persist
- [ ] Verify RTL/Uyghur presentation
- [ ] Verify mobile layout
- [ ] Verify PWA install/offline behavior
- [ ] Verify Cloudflare deployment configuration
- [ ] Review final diff before merging
- [ ] Merge only after all critical checks pass

## Deferred / optional improvements

- [ ] Add explicit project license and content-rights note
- [ ] Add contributor/development guide
- [ ] Add automated release notes
- [ ] Add accessibility audit tooling
- [ ] Add performance budget

