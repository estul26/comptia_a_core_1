# V6.5 — RTL Content Polish

Focused follow-up to V6.4 based on live production screenshots.

## Changes

- Pure-English paragraphs and headings inside the Uyghur reader render as isolated LTR blocks while staying anchored to the right side of the reading column.
- Pure-English bullet and numbered lists render as compact LTR list islands with natural English marker placement.
- Short technical headings that are mostly Latin but contain a small Uyghur connector (for example `T568A ۋە T568B Pinout`) preserve the technical identifier order.
- `Transcript correction:` and `Source-scope note:` lines render as direction-aware editorial callouts instead of visually competing with lesson prose.
- Uyghur-only desktop mode increases the article width to `62rem`; bilingual mode remains unchanged.
- Package version is synchronized to `6.5.0`.
- Service-worker cache is bumped to V6.5.

No lesson translation text was edited by this patch.
