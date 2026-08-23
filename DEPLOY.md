# Deploy to Cloudflare Workers Static Assets

This repository is ready for Cloudflare Workers Static Assets.

## Cloudflare build/deploy settings

- Production branch: `main`
- Deploy command: `npx wrangler deploy`
- Static asset directory: `.` (defined in `wrangler.jsonc`)

No `_redirects` file is used. The app navigates with hash URLs such as `#objective=2.5`, so an SPA fallback redirect is unnecessary and would cause a Cloudflare infinite-loop validation error.

## First deployment

Cloudflare should install dependencies from `package.json`, then run Wrangler.

You can also test locally:

```bash
npm install
npm run dev
```

Deploy manually:

```bash
npm run deploy
```

## Important

There is intentionally **no `_redirects` file** in this repository. Hash-based objective navigation does not require one.
