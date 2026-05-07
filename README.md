# blog.fontlab.com

Build orchestrator for the FontLab blog, deployed to [blog.fontlab.com](https://blog.fontlab.com/) via GitHub Pages. Content is authored as Markdown, built with [ProperDocs](https://github.com/fontlab/properdocs) (an MkDocs-based pipeline with the MaterialX theme), and published from `docs/`.

## Quick start

```bash
uv sync          # install dependencies into .venv/
./build.sh build # build docs/ from mkdocs/mkdocs.yml
./build.sh serve # live-reload preview at http://localhost:8000
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
| `./build.sh build` | Clean docs/ then run properdocs build |
| `./build.sh serve` | Run properdocs serve (live reload) |
| `./build.sh clean` | Remove docs/ contents, preserve CNAME |

## License

MIT — Copyright 2026 Fontlab Ltd.
