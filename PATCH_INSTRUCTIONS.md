# V5.1 Patch — Upload to GitHub

Upload all files in this folder to the ROOT of:

estul26/comptia_a_core_1

When GitHub asks about existing files:
- replace `sw.js`
- replace `README.md`
- add the other new files

Files:
- `wrangler.jsonc` — permanent Cloudflare configuration
- `.assetsignore` — keeps repo-only files out of public assets
- `.gitignore` — ignores local Wrangler/Node files
- `package.json` — pins Wrangler 4.125.0
- `sw.js` — improved offline cache + Google Fonts caching
- `README.md` — updated Workers deployment documentation

After committing to `main`, your Cloudflare Git integration should trigger a new deployment automatically.
