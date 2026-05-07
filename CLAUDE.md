# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

Greenfield. The only authored content is `IDEA.md` (the master spec — read it first), a `docs/CNAME` pinned to `blog.fontlab.com`, and a large `reference/` tree that is **gitignored** and treated as read-only or selectively-writable input material. There is no build system, no source code, no tests yet. Do not invent commands that aren't grounded in `IDEA.md`.

## Goal (from IDEA.md)

Build a modern (May 2026) **ProperDocs**-based blog at `blog.fontlab.com`, deployed to GitHub Pages from `docs/`. Source Markdown lives in `src_docs/md/`. A small `uv`-driven CLI in this repo wraps `vexy-mkdocs-tools` to build and publish, and a GitHub Action runs on git tags.

Content is ported (selectively, blog-only, no promos) from:
- `reference/fontlab-com-oldpub/2013…2023/` — keep blog-style posts mostly verbatim, preserve original dates
- `reference/fldoc/` and `reference/FontLabVI-help/` — only short "news"-style summaries

The blog must be compatible with the MaterialX `blog` plugin (`jaywhj.github.io/mkdocs-materialx/plugins/blog.html`).

## The `reference/` tree

Gitignored sibling repos cloned in for context. Three categories — respect them:

| Category | Examples | Rule |
|---|---|---|
| **Writable references** (have own remotes; OK to push fixes) | `fontlab-partners/`, `fldoc/`, `twardown-{docs,js,org,py}/` | `fontlab-partners` is in good shape — only fix obvious bugs. `fldoc` needs modernization. `twardown-*` to be prepped for PyPI/NPM publish with `hatch-vcs` + GitHub Actions. |
| **Writable Python tools** (own repos, target PyPI) | `vexy-mkdocs-output-as-input/`, `vexy-mkdocs-strip-number-prefix/`, `vexy-mkdocs-text-export/`, `vexy-mkdocs-markdown-in-template/`, `vexy-mkdocs-tags/`, `vexy-mkdocs-tools/`, `vexy-marktripy/`, `vexy-python-markdown-steroids/` | Rename packages to `vexy-…` prefix where noted. Use `uv publish`, `uvx hatch test`, `uvx hatch build`. `hatch-vcs` + git semver tags; `__version__.py` gitignored. Each gets `build.sh` + `publish.sh` + GH Actions. Modernize for ProperDocs / Python-Markdown 3.10.2 / Python 3.12+. |
| **Read-only references** | `properdocs/`, `mkdocs-materialx/`, `FontLabVI-help/`, `fontlab-com-oldpub/`, `pymdown-extensions/`, plus the `mkdocs-*` plugin clones | Don't edit. For non-published `mkdocs-*` plugins worth using, fork to `vexyart` org with `vexy-` prefix instead of editing in place. |

`vexy-mkdocs-tools` is the central Fire-based CLI that owns dependencies and exposes commands like `uvx vexy-mkdocs-tools build`. New work that isn't a plugin or Markdown extension goes there.

## Migration constraints (load-bearing)

- **MkDocs → ProperDocs.** MkDocs is EOL; v2 will break. All new and modernized code targets ProperDocs.
- **MkDocs Material → MaterialX.** Same story for the theme. Surgically extend, don't fork.
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
