# Loading.plus

A static Nuxt 4 motion gallery at https://loading.plus, with five prerendered pages.

```bash
pnpm dev
pnpm generate
```

Deploy `.output/public` to a static host. Production needs no Python or GIF service.
If an environment-injected pnpm dependency check attempts to reinstall the already installed modules, use `pnpm --config.verify-deps-before-run=false run generate` (or `run dev`).

## Original GIF assets

Twelve GIFs and twelve PNG covers are checked into `public/gifs/`. Regenerate offline with Python 3 and Pillow, supplying a local font:

```bash
python3 scripts/generate-gifs.py --font /path/to/font.ttf
python3 scripts/verify-static.py
```

The generator writes dimensions and byte sizes to `app/data/gifs.json`. No fonts or image-processing libraries are shipped to production. The checked-in assets use Arial; use the same font for matching output.

`verify-static.py` runs after generation and checks HTML, links, metadata, sitemap, and decodes every GIF frame. This repository has no separate lint or TypeScript-check script/dependency.

See [Phase 2 report](PHASE2-REPORT.md) for the page metadata, asset inventory, and verification results.

## Cloudflare deployment

Production: https://loading.plus

The site uses Workers Static Assets with `wrangler.jsonc`. The configuration binds the apex domain, serves `.output/public`, removes trailing slashes to match canonical URLs, and returns the generated 404 page for missing routes. No Nuxt SSR server or production image-processing runtime is required.

```bash
pnpm deploy:check  # Generate and validate the Cloudflare upload without publishing
pnpm deploy        # Generate and deploy to loading.plus
```

Wrangler is pinned as a development dependency. Sign in with `pnpm exec wrangler login` on a new machine. For CI, provide `CLOUDFLARE_API_TOKEN` through the CI secret store; never commit credentials. `.wrangler/` local state is ignored.

Deployment follows Cloudflare's [SSG guidance](https://developers.cloudflare.com/workers/static-assets/routing/static-site-generation/) and [custom domain configuration](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/).
