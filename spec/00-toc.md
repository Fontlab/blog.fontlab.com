---
this_file: spec/00-toc.md
---

# blog.fontlab.com — Site Specification

## Table of Contents

| # | Chapter | TL;DR |
|---|---------|-------|
| [01](01.md) | Goals & Non-Goals | The blog exists to publish evergreen technical writing for type designers and FontLab users — not to announce sales, not to mirror the docs, not to compete with the help site. This chapter defines the audience, the editorial mission, and the hard limits of scope. |
| [02](02.md) | Architecture | ProperDocs 1.6.7 (a maintained MkDocs fork) + MaterialX 10.1.4 + a thin Fire-based CLI. The `sys.meta_path` shim that makes `import mkdocs.*` resolve to `properdocs.*` is the key trick that lets every existing MkDocs plugin work without modification. This chapter explains why each layer was chosen and how they fit together. |
| [03](03.md) | Repository Layout | Every directory, every key file, and what owns what — shown as an annotated tree. The layout mirrors `fontlab-partners` for familiarity: `src_docs/md/` is source, `docs/` is build output, `mkdocs/` holds config, `src/` holds the CLI. |
| [04](04.md) | Build Pipeline | `./build.sh` is a thin shell wrapper around `uv run blog-fontlab`. The Fire CLI (`src/blog_fontlab/cli.py`) exposes `build`, `serve`, and `clean`. This chapter covers the `uv` lockfile policy, `hatch-vcs` versioning from git tags, and local development ergonomics. |
| [05](05.md) | Deploy Pipeline | Tag-triggered GitHub Actions workflow: `uv sync` → `build` → sanity-check `docs/index.html` and `docs/CNAME` → deploy to `gh-pages` branch via `peaceiris/actions-gh-pages@v4`. This chapter covers CNAME wiring, rollback procedure, and branch protection decisions. |
| [06](06.md) | Site Structure & Navigation | The blog is the primary content surface. Supporting pages are `/about/` and a thin home redirect. The MaterialX blog plugin auto-generates `/blog/archive/{yyyy}/`, `/blog/category/{slug}/`, and `/blog/author/{slug}/` — no manual nav entries needed for those. |
| [07](07.md) | MaterialX Blog Plugin Configuration | Front-matter contract, `.authors.yml` schema, post URL format, pagination settings, draft handling, archive and category generation. Everything the plugin touches is pinned here so authors know exactly what fields matter. |
| [08](08.md) | Theme & Chrome | The MaterialX header is hidden; the FontLab Web Component (`fontlab.js`) provides menu and footer. This chapter covers the `<fontlab-menu>` wiring, the `localMenu` config object, vanilla CSS custom properties, and the explicit no-build-step rule for CSS. |
| [09](09.md) | Plugin & Extension Stack | The exact plugin list with version pins and one-line rationale for each. Covers the interaction order, known conflicts, and which plugins touch the same pipeline stage. |
| [10](10.md) | Content & Porting Strategy | ~12 posts survive from `oldpub`. All promo/sale posts and point-release notes are retired. The 2013 colour-fonts technical piece is the crown jewel — port it with original date preserved. This chapter explains what to keep, what to cut, and how to do the HTML→Markdown conversion without mangling the content. |
| [11](11.md) | Authoring Workflow | Front-matter template, slug rules, image handling, draft flag lifecycle, local preview command, and link-checking discipline. Everything a new author needs from first draft to merged post. |
| [12](12.md) | Quality, Testing & Roadmap | Local smoke tests (link check, browser render via Chrome DevTools MCP), CI sanity checks, the evergreen-only content rule, and the open questions that need a decision before v1.0 ships. |

---

Status: Draft v0.1, 2026-05-07.
