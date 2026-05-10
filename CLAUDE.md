# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state (2026-05-08)

Live and building. ProperDocs 1.6.7 + MaterialX 10.1.4 site at `mkdocs/mkdocs.yml`, blog moved to site root (`blog_dir: .`, posts at `/yyyy/mm/dd/slug/`). 78 published posts in `src_docs/md/posts/`, 11 offline drafts under `issues/draft-posts/`. RSS + JSON Feed, `llms.txt` / `llms-full.txt` generated. Build via `./build.sh build` (Flowmark format → ProperDocs build); preview via `./build.sh serve`. CI deploys on git tag `v*.*.*` via `peaceiris/actions-gh-pages@v4`.

Source: `IDEA.md` (master spec, read first), `spec/00-toc.md` + `spec/01.md`–`spec/15.md` (chapters incl. editorial roadmap and content series), `TODO.md` (open work), `CHANGELOG.md` (history). Latest release tag: `v1.0.58`.

Open work right now (see `TODO.md`): 13 generic-placeholder image follow-ups. Everything else from the recent rewrite/title-case/CTA/consolidation/missing-image sprints has shipped.

## Goal (from IDEA.md)

Modern (May 2026) **ProperDocs**-based blog at `blog.fontlab.com`, GitHub Pages from `docs/`. Source Markdown in `src_docs/md/`. `uv`-driven CLI wraps build + publish; GitHub Action runs on tag.

Content is ported (selectively, blog-only, no promos) from:
- `reference/fontlab-com-oldpub/2013…2023/` — keep blog-style posts mostly verbatim, preserve original dates
- `reference/fldoc/` and `reference/FontLabVI-help/` — only short "news"-style summaries

The blog must be compatible with the MaterialX `blog` plugin (`jaywhj.github.io/mkdocs-materialx/plugins/blog.html`).

## The `reference/` tree

The `reference/` directory contains gitignored sibling repos and assets cloned in for context. Four main categories — respect them:

| Category | Examples | Rule |
|---|---|---|
| **Static Assets** | `i.fontlab.com/docs/`, `i.vexy.art/docs/`, `vexy-lines.static/`, `flum-unified-database.static/` | Hosted CDNs and static help sites. Used for shared components (e.g. `i.fontlab.com/menu/`). |
| **Writable references** | `fontlab-partners/`, `fldoc/`, `twardown-{docs,js,org,py}/` | `fontlab-partners` is in good shape — only fix obvious bugs. `fldoc` needs modernization to ProperDocs/MaterialX. `twardown-*` to be prepped for PyPI/NPM publish with `hatch-vcs` + GitHub Actions. |
| **Read-only references** | `FontLabVI-help/`, `fontlab-com-oldpub/` | Don't edit. Used as source material to port blog posts and news summaries to the new site. |
| **Writable Python tools** | `vexy-mkdocs-*`, `vexy-marktripy/`, `vexy-python-markdown-steroids/` | Own repos, target PyPI. Rename packages to `vexy-…` prefix where noted. Use `uv publish`, `uvx hatch test`, `uvx hatch build`. `hatch-vcs` + git semver tags; `__version__.py` gitignored. Each gets `build.sh` + `publish.sh` + GH Actions. Modernize for ProperDocs / Python-Markdown 3.10.2 / Python 3.12+. |
| **Read-only Python tools** | `properdocs/`, `mkdocs-materialx/`, `pymdown-extensions/`, plus the `mkdocs-*` plugins | Don't edit. If a non-published `mkdocs-*` plugin is needed, fork it to `./reference/github.vexyart/` with a `vexy-` prefix, add scaffolding, publish it, and add to `vexy-mkdocs-tools` requirements. |

`vexy-mkdocs-tools` is the central Fire-based CLI that owns dependencies and exposes commands like `uvx vexy-mkdocs-tools build`. New work that isn't a plugin or Markdown extension goes there.

## Migration constraints (load-bearing)

- **MkDocs → ProperDocs.** MkDocs is EOL; v2 will break. All new and modernized code targets ProperDocs.
- **MkDocs Material → MaterialX.** Same story for the theme. Surgically extend, don't fork. Familiarize yourself with MaterialX plugins for ProperDocs: `optimize`, `tags`, and absolutely crucially `blog`.
- **Python-Markdown 3.10.2** and **Python 3.12+** are the floor for the Markdown-side tools.
- No backwards-compatibility constraint for the new code we own.

## Conventions inherited from this workspace

From the parent workspace (`../CLAUDE.md`):

- Every source file carries a `this_file:` header (comment in code, YAML frontmatter in markdown) recording its path relative to project root. Update on move.
- Maintain `WORK.md`, `TODO.md`, `PLAN.md`, `CHANGELOG.md` per subproject — they are load-bearing; read `WORK.md` / `TODO.md` before resuming.
- The shared FontLab menu/footer is loaded as a Web Component from `https://i.fontlab.com/menu/` — the blog will consume it the same way `partners.fontlab.com` does. Don't reimplement.

## Spec deliverables (per IDEA.md → "Tasks")

1. `spec/00-toc.md` with ToC + TL;DR per chapter, then `spec/01.md` … `spec/12.md` — a 12-chapter spec of the new site.
2. `TODO.md` derived from the spec, items prefixed `- [ ]`.
3. As implementation progresses, tick items in `TODO.md` and append to `CHANGELOG.md`.

## Writing style for blog/spec content

From IDEA.md: lead strong, plain language, concise, show-don't-tell, edit ruthlessly. Light Norm-Macdonald-meets-Stephen-Fry humor allowed, clarity wins. No corpo jargon, no "revolutionary"-class hype words. Stephen King's rules apply.
