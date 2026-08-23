# V5.3 Verification Report

Audit date: 2026-08-23

## Result

The V5.3 repository passed the final application regression suite after fixing issues found during the audit.

### Interaction regression: 33 / 33 passed

Verified:

- Current-lesson search and highlighting
- Course-wide search results
- Sidebar/course filtering
- English-only mode
- Uyghur-only mode
- Uyghur font selector
- Font-size controls
- Dark mode
- Synchronized/free scrolling toggle
- Distraction-free focus mode
- Focus-line mode
- Paired study-card mode
- Hide/reveal Uyghur and English active-recall behavior
- Bookmark saving and bookmarks-only filtering
- Mark-complete course progress
- Per-objective notes autosave and restore
- Notes export download
- Paragraph copy
- Share-objective link fallback
- Print action
- Online/offline status indicator
- Install prompt flow
- Keyboard shortcuts C, E, L, /
- Mobile horizontal-overflow check
- Mobile study cards stack vertically
- No JavaScript runtime exceptions during the interaction suite

### Additional regression checks

- 28 lessons render: Introduction + 27 exam objectives
- All 27 objective IDs are present and in order
- No empty English or Uyghur lesson content
- 41/41 JavaScript-controlled HTML IDs exist; no duplicate IDs
- JavaScript syntax passes `node --check`
- `sw.js` syntax passes `node --check`
- `manifest.webmanifest` and `package.json` parse as valid JSON
- PWA icons are valid 192×192 and 512×512 PNG files
- All service-worker core cache paths exist
- No `_redirects` file is present
- Original English and Uyghur source text files remain in `source/`

## Problems found and fixed

1. **Study-card alignment boundary crash**
   - The alignment search could start at array index `-1` on the first paragraph.
   - Fixed by clamping the lower search bound to `0`.

2. **Reading-position reset risk**
   - Changing lessons could overwrite a previously saved reading position while panes were being reset to the top.
   - Fixed with normalized reading-position storage and reset suppression.
   - Reading position is now saved from either the English or Uyghur pane.

3. **Saved-settings robustness**
   - Malformed JSON in browser localStorage could crash the app at startup.
   - Invalid font/language/recall values are now safely recovered to defaults.

4. **Technical-term chip false positives**
   - Very short terms such as `IP` could match inside unrelated words.
   - Technical-term detection now uses token boundaries.

5. **Transcript study-display corrections**
   - Obvious speech-to-text errors such as DBR/TBR for DDR were corrected in the embedded study display.
   - Original source transcripts remain unchanged.
   - See `TRANSCRIPT_CORRECTIONS.md`.

6. **Share fallback**
   - If the browser exposes Web Share but the share call fails, the app now attempts to copy the objective URL before reporting failure.

7. **Language layout persistence**
   - English/Uyghur layout selection is now saved and restored.

## Cloudflare notes

- Deployment model: Cloudflare Workers Static Assets.
- `wrangler.jsonc` points static assets at the repository root.
- `.assetsignore` prevents repository-only files from being published as static assets.
- `_headers` remains in the asset directory for Cloudflare to parse.
- There is intentionally no `_redirects` file because objective navigation uses URL hash fragments.

## Environment limitation

The audit environment blocks browser navigation to localhost/file URLs, so a true end-to-end service-worker registration over a local HTTP origin could not be executed. The service worker was syntax-checked, its referenced cache files were verified, and the PWA/static-asset configuration was structurally validated. A final Cloudflare deployment is still the definitive end-to-end test of the hosting environment.


## V5.3 UI regression note

The V5.3 release changes presentation and adds a mobile objective selector. The previously verified study engine is retained. Static dependency and syntax checks were rerun after the UI changes; no missing element references or duplicate IDs were found.
