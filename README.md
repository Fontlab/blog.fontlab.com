# blog.fontlab.com

Build orchestrator for the FontLab blog, deployed to [blog.fontlab.com](https://blog.fontlab.com/) via GitHub Pages. Content is authored as Markdown, built with [ProperDocs](https://github.com/fontlab/properdocs) (an MkDocs-based pipeline with the MaterialX theme), and published from `docs/`.

## Quick start

```bash
uv sync          # install dependencies into .venv/
./build.sh build # Flowmark-format src_docs/md, then build docs/
./build.sh serve # live-reload preview at http://localhost:8000
./publish.sh    # build docs/, create next v*.*.* tag, push to trigger deploy
```

## Layout

```
blog.fontlab.com/
├── build.sh           # CLI wrapper (delegates to uv run blog-fontlab)
├── docs/              # build output (GitHub Pages root) — do not hand-edit
│   └── CNAME          # blog.fontlab.com
├── mkdocs/            # MkDocs config and theme overrides (created separately)
│   └── mkdocs.yml
├── src_docs/          # Markdown source (created separately)
├── src/
│   └── blog_fontlab/
│       ├── __init__.py
│       └── cli.py     # fire CLI: build / serve / clean
└── pyproject.toml
```

## CLI subcommands

| Command | Description |
|---|---|
| `./build.sh build` | Flowmark-format `src_docs/md/`, clean `docs/`, then run ProperDocs build |
| `./build.sh format` | Run Flowmark on `src_docs/md/` with semantic breaks, smart quotes, ellipses, and safe cleanups |
| `./build.sh serve` | Run properdocs serve (live reload) |
| `./build.sh clean` | Remove docs/ contents, preserve CNAME |
| `./publish.sh` | Build, sanity-check `docs/`, then run `uvx gitnextver` to commit, tag, and push; GitHub Actions deploys the tag |

## The `reference/` directory

The `./reference/` directory is **gitignored** and contains various cloned repositories and assets used as context, tooling, and source material.

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
