# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state (2026-07-05)

Live and building. ProperDocs 1.6.7 + MaterialX 10.1.4 site at `mkdocs/mkdocs.yml`, blog moved to site root (`blog_dir: .`, posts at `/yyyy/mm/dd/slug/`). 134 published posts in `src_docs/md/posts/`, 11 offline drafts under `issues/draft-posts/`. RSS + JSON Feed, `llms.txt` / `llms-full.txt` generated. Build via `./build.sh build` (Flowmark format → ProperDocs build); preview via `./build.sh serve`.

Source: `IDEA.md` (master spec, read first), `spec/00-toc.md` + `spec/01.md`–`spec/15.md` (chapters incl. editorial roadmap and content series), `TODO.md` (open work), `CHANGELOG.md` (history). Latest release tag: `v1.0.92`.

Open work right now (see `TODO.md`): 41 newer posts still need the editorial `review:` overlay, and 19 reviewed posts still carry a placeholder hero image. `tests/test_content_state.py` verifies the live counts and the invariants that hold today.

## Build & deploy (load-bearing — read before touching publishing)

The hosting has three parts that are easy to confuse. Keep them straight:

| Piece | Truth |
|---|---|
| **GitHub Pages source** | The **`gh-pages`** branch (a repo *setting*, not in the tree), served at `blog.fontlab.com`. **Not** `main/docs`. |
| **`.github/workflows/ci.yml`** (`deploy`) | Runs `./build.sh build`, then deploys `docs/` → `gh-pages` via `peaceiris/actions-gh-pages@v4` (orphan branch, writes `CNAME`). |
| **`docs/`** | Build output. Tracked on `main` but **vestigial** — it only seeds `docs/CNAME`, which `build.sh` *preserves* (does not regenerate) and CI's sanity-check requires. Never hand-edit; the live HTML comes from `gh-pages`. |

**`ci.yml` triggers:** push to `main`, `v*.*.*` tag push, and manual dispatch.
So a single Markdown push to `main` is enough to publish — `build.sh` runs in
CI and redeploys `gh-pages`. `./build.sh build` does Flowmark-format
`src_docs/md/` → clean `docs/` (preserving `CNAME`) → ProperDocs build.
`./publish.sh` is the heavier path: build + sanity-check + `uvx gitnextver`
(commit, tag, push) — the tag also triggers deploy.

Do **not** "fix" the `docs/` churn by untracking it: a fresh CI checkout needs
`docs/CNAME` to exist before `build.sh` runs, or the sanity-check fails.

Force a redeploy: `gh workflow run deploy --repo Fontlab/blog.fontlab.com --ref main`.

> **History / gotcha (2026-06-07):** Pages previously served `main/docs`
> directly and `ci.yml` ran only on tags. The api.fontlab.com web admin
> publishes posts by committing only the source Markdown to `main` (it never
> rebuilds `docs/`), so posts landed in `src_docs/` but never went live.
> Fixed by switching Pages to `gh-pages` + adding the `main` push trigger.

### How posts get written

A post is `src_docs/md/posts/YYYY-MM-DD-slug.md` with frontmatter `title:`,
`authors: [<key>]` (a key from `src_docs/md/authors.yml` — this is the category
axis; there is **no `tags:` taxonomy**), nested `date: created:`, and `slug:`.
The excerpt is the text above a `<!-- more -->` separator. Most posts are
authored through the FontLab WWW Admin
(`api.fontlab.com/dist/public/www-admin/`, "Blog post" tab), which writes
exactly this schema and pushes to `main`.

## Goal (from IDEA.md)

Modern (May 2026) **ProperDocs**-based blog at `blog.fontlab.com`, GitHub Pages from the `gh-pages` branch (built by CI from `docs/` — see [Build & deploy](#build--deploy-load-bearing--read-before-touching-publishing)). Source Markdown in `src_docs/md/`. `uv`-driven CLI wraps build + publish; the deploy Action runs on push to `main`, on `v*.*.*` tags, and on manual dispatch.

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
