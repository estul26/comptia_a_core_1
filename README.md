# CompTIA A+ Core 1 — English ↔ Uyghur Study Reader

A bilingual CompTIA A+ Core 1 study website with English and Uyghur side by side.

## Features

- English ↔ Uyghur bilingual reading
- 27 exam objectives
- Search, bookmarks, progress, notes
- Active recall: hide English or Uyghur
- Better Uyghur typography and RTL handling
- Offline/PWA support
- Shareable objective links
- Installable on supported browsers/devices
- Cloudflare Pages ready

## Cloudflare Pages deployment

Connect this GitHub repository to Cloudflare Pages.

Recommended settings:

- Framework preset: None
- Production branch: `main`
- Build command: leave blank
- Root directory: repository root
- Build output directory: repository root (`.`) if Cloudflare asks for one

The repository root contains `index.html`, `_headers`, `_redirects`, the web manifest, and service worker.

## Local preview

You can open `index.html` directly for basic use.

For service-worker/offline testing, serve the folder over HTTP instead, for example:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

## Notes

Study progress, bookmarks, font settings, and notes are stored in the browser's localStorage.
