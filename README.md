<!-- this_file: README.md -->

# blog.fontlab.com

Build orchestrator for the FontLab blog, published to
[blog.fontlab.com](https://blog.fontlab.com/) via GitHub Pages. Posts are
authored as Markdown in `src_docs/md/posts/`, built with
[ProperDocs](https://github.com/fontlab/properdocs) (an MkDocs-based pipeline
with the MaterialX theme), and the generated HTML is deployed to the
**`gh-pages`** branch by GitHub Actions.

## Quick start

```bash
uv sync          # install dependencies into .venv/
./build.sh build # Flowmark-format src_docs/md, then build docs/
./build.sh serve # live-reload preview at http://localhost:8000
./publish.sh     # build docs/, create next v*.*.* tag, push to trigger deploy
```

You do **not** have to run `publish.sh` to ship a post. Any push to `main`
(including a single new Markdown file) triggers the deploy workflow — see
[Publishing & deploy](#publishing--deploy). `publish.sh` is the heavier path
that also stamps a version tag.

## Writing a post

A post is one Markdown file at `src_docs/md/posts/YYYY-MM-DD-slug.md` with this
frontmatter (matched by every existing post — there is **no `tags:`
taxonomy**; the `authors:` field is the blog's category axis):

```markdown
---
title: "Vexy Lines 2 is here!"
authors: [vexy-lines]
date:
  created: 2026-06-07
slug: vexy-lines-2
---

Lead paragraph that shows on the index and in feeds.

<!-- more -->

Full body of the post…
```

- **`authors:`** must reference a key defined in `src_docs/md/authors.yml`
  (e.g. `fontlab`, `vexy-lines`, `adam`, `transtype`, `typetool`,
  `fontographer`, `fontlab-pad`). An unknown author makes the post unresolvable.
- **`<!-- more -->`** is the mkdocs-material excerpt separator — text above it
  becomes the summary on the index page and in the RSS/JSON feeds.
- The published URL is `/YYYY/MM/DD/slug/`, derived from the date + slug.

Most posts are written through the web admin (see below) rather than by hand.

## Publishing & deploy

The hosting is deliberately simple but has three moving parts — know which is
which:

| Piece | What it is |
|---|---|
| **GitHub Pages source** | The `gh-pages` branch, served at `blog.fontlab.com` (a repo *setting*, not a file in the tree). |
| **`.github/workflows/ci.yml`** (`deploy`) | Runs `./build.sh build`, then publishes `docs/` → `gh-pages` via `peaceiris/actions-gh-pages` (orphan branch, writes the `CNAME`). |
| **`docs/`** | Build output. Still tracked on `main` but **vestigial** — it only seeds `docs/CNAME`, which `build.sh` preserves and CI's sanity-check requires. The *live* HTML comes from `gh-pages`, rebuilt by CI. |

**The deploy workflow runs on:**

- a push to **`main`** (the everyday path — including new posts written by the
  web admin, which commit a Markdown file to `main`),
- a `v*.*.*` **tag** push (what `publish.sh` / `gitnextver` create), and
- **manual dispatch**.

So the normal flow is: edit/add Markdown in `src_docs/md/` → push to `main` →
GitHub Actions builds and deploys to `gh-pages` → the live site updates within
a minute or two.

> **History / gotcha:** Pages used to serve `main`'s `docs/` folder *directly*,
> and `ci.yml` only ran on tags. Because the web admin pushes only source
> Markdown (it never rebuilds `docs/`), posts landed in `src_docs/` but never
> appeared live. Switching Pages to `gh-pages` and adding the `main` trigger
> fixed it: a source push is now sufficient to publish.

### Force a redeploy

```bash
gh workflow run deploy --repo Fontlab/blog.fontlab.com --ref main
```

### Publishing through the web admin

Editors can write posts without a local checkout at
[api.fontlab.com/www-admin/?tab=blog](https://api.fontlab.com/www-admin/?tab=blog).
That form clones/pulls this repo on the server, writes the Markdown file to
`src_docs/md/posts/`, and commits + pushes it to `main` — which then triggers
the deploy workflow described above. The author dropdown is populated from this
repo's `src_docs/md/authors.yml`. See `api.fontlab.com`'s README for the admin
side.

## CLI subcommands

| Command | Description |
|---|---|
| `./build.sh build` | Flowmark-format `src_docs/md/`, clean `docs/` (preserving `CNAME`), then run ProperDocs build |
| `./build.sh format` | Run Flowmark on `src_docs/md/` with semantic breaks, smart quotes, ellipses, and safe cleanups |
| `./build.sh serve` | Run ProperDocs serve (live reload) at `:8000` |
| `./build.sh clean` | Remove `docs/` contents, preserve `CNAME` |
| `./publish.sh` | Build, sanity-check `docs/`, then run `uvx gitnextver` to commit, tag, and push; the tag triggers the deploy workflow |

The build/preview logic itself lives in the `blog-fontlab` package
(`src/blog_fontlab/cli.py`); `build.sh` is a thin `uv run blog-fontlab` wrapper.

## Layout

```
blog.fontlab.com/
├── build.sh               # CLI wrapper (delegates to uv run blog-fontlab)
├── publish.sh             # build + sanity-check + gitnextver tag/push
├── .github/workflows/
│   └── ci.yml             # "deploy": build → publish docs/ to gh-pages
├── docs/                  # build output → deployed to gh-pages (do not hand-edit)
│   └── CNAME              # blog.fontlab.com (seed preserved by build.sh)
├── mkdocs/
│   └── mkdocs.yml         # ProperDocs/MaterialX config and theme overrides
├── src_docs/
│   └── md/
│       ├── posts/         # one Markdown file per post (YYYY-MM-DD-slug.md)
│       └── authors.yml    # author/category definitions
├── src/
│   └── blog_fontlab/
│       ├── __init__.py
│       └── cli.py         # fire CLI: build / serve / clean / format
└── pyproject.toml
```

## The `reference/` directory

The `./reference/` directory is **gitignored** and contains various cloned
repositories and assets used as context, tooling, and source material.

- **Assets & Static Sites:**
  - `i.fontlab.com/docs/` — CDN with images/assets for FontLab apps.
  - `i.vexy.art/docs/` — CDN with images/assets for Vexy Lines.
  - `vexy-lines.static/` — Help site and images for Vexy Lines.
  - `flum-unified-database.static/` — Articles about FontLab.
- **Source Material (Read-only):**
  - `fontlab-com-oldpub/` — Old WordPress blog exports (2013-2023). Blog-style posts will be ported to the new site.
  - `FontLabVI-help/` — Ancient site for FontLab VI and 7.
- **Reference Sites (Writable):**
  - `fontlab-partners/` — Partners site (MkDocs + MaterialX, Tailwind CSS).
  - `fldoc/` — FontLab 8 help site (Older MkDocs). Needs modernization.
- **Python Tools (Writable, to be published):**
  - `twardown-*` — Various twardown packages to be published to PyPI/NPM.
  - `vexy-mkdocs-*`, `vexy-marktripy/`, `vexy-python-markdown-steroids/` — Plugins and tools being modernized for ProperDocs / Python 3.12+.
- **Python Tools (Read-only):**
  - `properdocs/` — Maintained fork of MkDocs.
  - `mkdocs-materialx/` — Maintained fork of MkDocs Material.
  - `pymdown-extensions/`, and various `mkdocs-*` plugins.

## License

MIT — Copyright 2026 Fontlab Ltd.
