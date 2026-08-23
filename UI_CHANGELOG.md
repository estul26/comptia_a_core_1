# V6 UI — Study Workspace Redesign

This release keeps the reviewed V5.30 bilingual lesson data and the existing study engine, but substantially redesigns the interface around the way a learner actually uses the app.

## Major improvements

- Rebuilt the visual hierarchy around **course navigation → objective controls → bilingual reader**
- New compact A+ course identity and a clearer progress card with live percentage
- Cleaner objective navigation with stronger active states, sticky domain labels, better completion markers, and improved search
- Consolidated the top toolbar so search and everyday reading controls stay visible while secondary actions live in a **More** menu
- Split objective identity into clear objective/domain/position metadata instead of one crowded title line
- Separated English and Uyghur objective titles for cleaner bilingual scanning
- Redesigned the English and Uyghur panes as independent reading cards with more comfortable line length, spacing, headings, and sticky language headers
- Improved technical-term chips, note editor, completion state, bookmark state, recall controls, resume reading, and previous/next navigation
- Refined Cards mode to match the new visual system
- Improved dark mode contrast and component consistency
- Added stronger keyboard focus states and an `aria-live` toast status
- Added reduced-motion support
- Reworked tablet/mobile layouts with a sticky search toolbar, mobile objective selector, stacked reader cards, and sticky previous/next controls
- Preserves progress, notes, bookmarks, search, synced scrolling, language layout, Uyghur font choice, reading position, Cards/recall mode, sharing, printing, installation, and offline/PWA behavior

## Compatibility / data safety

- No lesson text was removed or rewritten by the UI redesign
- Existing localStorage keys were preserved, so saved browser progress and notes remain compatible
- Existing element IDs required by the JavaScript study engine were preserved
- Service-worker cache name was bumped so the refreshed interface is picked up cleanly after deployment

## Validation

- 47 unique DOM IDs, no duplicates
- All JavaScript `$()` element references resolve to an existing ID
- Embedded JavaScript passes `node --check`
- Service worker passes `node --check`
- `manifest.webmanifest`, `package.json`, and `wrangler.jsonc` parse as valid JSON/JSONC-compatible project files
- 28 lessons remain present: introduction + 27 objectives


## V6.1 — Reading Space Update
- Removed the large objective title/action header from the reading canvas.
- Moved Complete, Bookmark, Notes, Resume, and Recall tools into the **More** menu.
- Expanded the bilingual reader to use the freed vertical space.
- Kept a compact objective selector on mobile.
- Bumped the service-worker cache so the new layout appears after deployment.


## V6.2 — Desktop Polish
- Reduced the full-desktop sidebar to 280px; compact desktop hides the sidebar so the bilingual reader stays wide.
- Simplified the main toolbar to Search, Language, Sync, Cards, and More.
- Moved font size, theme, and reading-focus controls into More.
- Added a tiny current-objective context strip instead of restoring the large lesson header.
- Capped the desktop reading workspace at 1940px for ultrawide monitors.
- Limited English line length to 74ch and Uyghur content to 48rem for easier reading.
- Tightened English and Uyghur line spacing and paragraph spacing to show more lesson content.
- Reduced sticky language-header height.
- Improved secondary-label contrast and minimum label sizing.
- Added a 901–1180px compact-desktop mode with a slim objective selector and side-by-side bilingual panes.
- Moved the stacked/mobile layout breakpoint to 900px to avoid cramped narrow-desktop layouts.
- Preserved all existing study-engine IDs, localStorage keys, notes, bookmarks, progress, recall, cards, PWA, and offline behavior.
- Bumped the service-worker cache to V6.2.
