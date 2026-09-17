# Deploy to Cloudflare Workers Static Assets

This repository is ready for Cloudflare Workers Static Assets.

## Cloudflare build/deploy settings

- Production branch: `main`
- Deploy command: `npx wrangler deploy`
- Static asset directory: `.` (defined in `wrangler.jsonc`)

## Automatic deployment with GitHub Actions

The workflow in `.github/workflows/deploy.yml` runs `wrangler deploy` after every
push to `main`. It can also be started manually from the **Actions** tab in GitHub.

Before the first automated deployment, add these repository secrets in
**GitHub → Settings → Secrets and variables → Actions**:

- `CLOUDFLARE_ACCOUNT_ID`: the Cloudflare account ID that owns the Worker.
- `CLOUDFLARE_API_TOKEN`: an API token created from Cloudflare's **Edit
  Cloudflare Workers** template and restricted to the deployment account.

Never commit either value to this repository. After adding the secrets, push a
commit to `main` or run **Deploy to Cloudflare** from the GitHub Actions page.

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
