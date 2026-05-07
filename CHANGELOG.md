# Changelog

## [Unreleased] — 2026-05-08 (continued)

### Added
- Added Flowmark 0.6.5 as a locked build dependency.
- Added `./build.sh format` / `blog-fontlab format` to format `src_docs/md/` in place with semantic line breaks, safe cleanups, smart quotes, and ellipses.
- Generated root-level `docs/llms.txt` and `docs/llms-full.txt` through the `llmstxt` plugin.
- Added 32 issue-203 expansion posts from `spec/15.md`; only `nabla-colrv1-and-color-fonts`, `when-type-becomes-texture`, and `distortion-as-defense-2026` remain open.
- Added 2024–2026 roadmap posts for the Made with FontLab, FontLab TV, Briem, Calfonts, and Vexy Lines series, bringing the source tree to 113 Markdown posts.
- Added a local Vexy Lines interface image for `vexy-lines-and-the-useful-lie-of-engraving`, replacing a broken `doc360/Images` reference.

### Changed
- `./build.sh build` now runs Flowmark against `src_docs/md/` before cleaning `docs/` and running ProperDocs.
- Build-time Flowmark formatting restores ASCII quote delimiters inside raw HTML tags after smart quote conversion, so legacy WordPress HTML attributes remain valid.
- Enabled `include-markdown`, `llmstxt`, and `copy-to-llm` in `mkdocs/mkdocs.yml`.
- Expanded GitHub Actions output checks for the at-root layout: `docs/index.html`, `docs/about/index.html`, `docs/CNAME`, `docs/.nojekyll`, `docs/llms.txt`, and `docs/llms-full.txt`.
- Reconciled `TASKS.md` and `TODO.md` so completed configuration, post-list styling, FontLab 8.2 split, excerpt, llms, browser-check, Made with FontLab, and shipped issue-203 post-file tasks are removed from the open checklist.
- Tightened the template content container so narrow post pages no longer overflow horizontally.

### Verified
- `uv sync --frozen` completed with Flowmark in the lock file.
- `uv run blog-fontlab format` completed against 118 Markdown files with no `.bak` or `.orig` files.
- `./build.sh build` completed after running Flowmark first.
- `uvx ruff check src/` passed.
- Local checks found no smart-quote HTML attribute delimiters in `src_docs/md` or generated `docs`.
- `uv sync --frozen` completed.
- `./build.sh build` completed and generated root `llms.txt` and `llms-full.txt`.
- `uvx ruff check src/` passed.
- Local checks confirmed all current posts include `<!-- more -->`, no post uses `authors: [editorial]` or `categories:`, CI sanity-check target files exist, and `src_docs/md/posts/` currently contains 113 Markdown posts.
- Local build output contains 113 generated public post pages, `docs/llms.txt` (14,252 bytes), and `docs/llms-full.txt` (359,412 bytes).
- Playwright screenshots were captured for home, single post, archive, and about at desktop and narrow mobile widths.
- Chrome DevTools checks found no horizontal overflow and no console errors on home, `opentype-features-as-ux`, archive 2025, and about.

## [Unreleased] — 2026-05-07 (cont)

### Planned
- Editorial roadmap: 12 posts in 2026 (Jan–May), 24 posts in 2025, 24 posts in 2024 — see `spec/13.md`.
- Three new content series — "Made with FontLab" (designer profiles), "FontLab TV" (Kapusta-chapter companions), "Tutorials" (briem + calfonts modernizations) — see `spec/14.md`.

### Changed (planning)
- `spec/06.md` rewritten for the at-root blog layout (`blog_dir: .`); removed every `/blog/` URL prefix and documented category-free blog behavior.
- `spec/07.md` updated: `blog_dir: .`, `post_dir: posts`, `authors_file: authors.yml`, `categories: false`, and post-URL examples no longer prefixed with `/blog/`.
- `spec/00-toc.md` extended to include chapters 13 and 14.
- `TODO.md` rewritten: completed items moved into `CHANGELOG.md` `## Shipped` (below); only open items remain. New sections added for the typography sweep, post-list restyling, existing-post fixes, and editorial-roadmap drafting.

### Added (planning)
- `spec/13.md` — Editorial Roadmap 2024–2026 with 60 planned posts (date, slug, title, summary, source).
- `spec/14.md` — Content Series specifying "Made with FontLab", "FontLab TV", "Tutorials".

## Shipped

The following items were marked `[x]` in `TODO.md` during the 2026-05-07 session and have moved here so the open list stays focused. Verification evidence is preserved in the `### Verified` block of the original `[Unreleased] — 2026-05-07` section below.

### Foundation
- Created `pyproject.toml` with hatchling + hatch-vcs, `requires-python = ">=3.12"`, all plugin dependencies pinned.
- Created `src/blog_fontlab/__init__.py` (empty).
- Created `src/blog_fontlab/cli.py` with Fire CLI exposing `build`, `serve`, `clean`.
- Registered `blog-fontlab` entry point in `pyproject.toml` `[project.scripts]`.
- Created `build.sh` as thin `uv run blog-fontlab "$@"` wrapper with `set -euo pipefail`.
- Ran `uv sync` and verified all 56+ packages resolve (including local `reference/` sources).

### Site config
- Created `mkdocs/mkdocs.yml` with `theme: materialx`, `palette: scheme: slate`, `docs_dir: ../src_docs/md`, `site_dir: ../docs`.
- Added `materialx/blog` plugin block (archive, categories, authors, pagination, draft, slugify, readtime).
- Added `materialx/tags` plugin.
- Added full `markdown_extensions` block (pymdownx suite + admonition + footnotes + toc + vexy_python_markdown_steroids).

### Theme & chrome
- Created `mkdocs/mk-fontlab/main.html` extending `base.html`, injecting the FontLab Web Component menu/footer, with `DOMContentLoaded` config assignment.
- Wired `localMenu` config object with Blog, Archive, About items in `main.html`.

### Content
- Created `src_docs/md/index.md` landing page (Option B brief intro under 300 words).
- Created `src_docs/md/about.md` condensed from the oldpub about page.
- Created the initial blog index file (later removed when the blog moved to site root).
- Created `.authors.yml` with `adam` entry.
- Created the 2013-09-19 colour-fonts post with correct front-matter.

### Build & deploy
- Moved `CNAME` to `src_docs/md/CNAME` so the build pipeline copies it to `docs/CNAME`.
- Verified `docs/CNAME` contains `blog.fontlab.com` after `./build.sh build`.
- Confirmed `.nojekyll` is present in build output.
- Created `.github/workflows/ci.yml` with tag-triggered deploy via `peaceiris/actions-gh-pages@v4`, `fetch-depth: 0`, `uv sync --frozen`.

## [Unreleased] — 2026-05-07

### Added
- Footer CTA band, adapted from `reference/fontlab-partners`, with three FontLab-wide actions: buy, learn more, and contact.
- Loaded partner-site heading fonts (`Outfit`, `Bricolage Grotesque`, `Crimson Pro`) through the MaterialX template override.
- `src_docs/md/css/extra.css`, the stylesheet already referenced by `mkdocs/mkdocs.yml`, for blog typography and CTA styling.
- Initial scaffold: uv-managed Python project with `blog-fontlab` Fire CLI (`build`, `serve`, `clean`).
- ProperDocs 1.6.7 + mkdocs-materialx 10.1.4 site config at `mkdocs/mkdocs.yml`.
- MaterialX blog plugin enabled with archive, categories, authors, pagination.
- Template override at `mkdocs/mk-fontlab/main.html` loading the shared FontLab Web Component menu/footer from `i.fontlab.com/menu/`.
- Skeleton pages: `index.md`, `about.md` (full company history, ~750 words), `blog/index.md`.
- Author registry at `blog/.authors.yml` (Adam Twardoch).
- First post: `blog/posts/2013-09-19-color-fonts.md` (color-fonts overview, ported from WordPress export — body was teaser-only in the source archive; full piece needs sourcing).
- `src_docs/md/CNAME` so `blog.fontlab.com` survives the build clean.
- `.github/workflows/ci.yml`: tag-triggered (`v*.*.*`) deploy to `gh-pages` branch via `peaceiris/actions-gh-pages@v4`.
- `CLAUDE.md` capturing repo layout, reference policy, and migration constraints.
- `spec/` directory: 12-chapter site specification (in progress).

### Changed
- Blog heading typography now follows the partner site direction: Outfit-based content headings, Bricolage display treatment for blog index titles, Crimson Pro quotes, and tighter MaterialX overrides.
- MaterialX default font autoloading is disabled so the partner typography is the active font system.
- **Blog moved to site root.** `blog_dir: .` (was `blog`). Post URLs are now `/yyyy/mm/dd/slug/`; categories at `/category/<slug>/`; archive at `/archive/<yyyy>/`. Site index IS the blog index — no redundant landing page. Spec chapters 6 and 7 still describe the previous layout.
- `.nojekyll` is now written by the build pipeline (CLI `build` step) instead of being a static file. GitHub Pages requires it because MaterialX ships some `_`-prefixed asset directories.

### Content
- Re-inventory of `reference/fontlab-com-oldpub/`: 9 unique articles confirmed (1 blog + 7 release announcements + 1 promo). Notes at `.omc/notes/oldpub-inventory.md`.
- Inventory of FontLab 8 release notes: 534-line roadmap at `.omc/notes/fl8-releases.md`.
- Inventory of FontLab VI/7 release notes: 39 releases catalogued at `.omc/notes/flvi7-releases.md`.
- Ported 8 WordPress posts (HTML→Markdown via pandoc) into `src_docs/md/posts/` covering 2013–2023. Promo "Save $40" post dropped per spec.
- Wrote 4 new release-summary posts to fill gaps: FontLab VI launch (2017-12-07), FontLab 7 year-in-review (2020-12-30), FontLab 8 launch (2022-06-26), FontLab 8.3/8.4 roundup (2024-06-05).
- Total: 12 posts spanning 2013–2024.
- Pinned the most-recent oldpub post (`2023-08-09`) so it appears at the top of the index.
- Stripped the WordPress "About the Author" footer block from every ported post (Gravatar `<img>` + `## Adam Twardoch` heading + bio) — the blog plugin renders authors via `.authors.yml` instead.
- Author registry now has two entries: `adam` (GitHub avatar `519108`), `thomas` (Thomas Phinney, used by the DTL OTMaster post; GitHub avatar `3043872`).
- All post-asset images downloaded from `wp-content/uploads/` to `src_docs/md/media/` (7 PNGs, 1.7 MB total). Markdown references rewritten to `/media/<file>`.
- Set `extra_css` to load both `css/fontlab-chrome.css` (header suppression) and `css/extra.css` (typography tokens).

### Verified
- `./build.sh build` after CTA/typography changes — complete; existing absolute `/media/...` link notices remain informational.
- `uvx ruff check src/` after CTA/typography changes — clean.
- Chrome DevTools visual check: CTA renders as three aligned desktop columns and stacked mobile panels at a 390px emulated viewport; post heading scale remains readable; no console errors.
- `uv sync` — 56 packages, all from local `reference/` checkouts.
- `./build.sh build` — clean build, 0 errors, 0 warnings. Outputs `docs/CNAME` and `docs/.nojekyll`.
- `uvx ruff check src/` — clean.
- Curl verification: site root + page 2 (pagination), all 8 archive years (2013/2017–2020/2022–2024), both category pages (`release`, `blog`), `/about/`, every individual post URL, sitemap (26 entries), `/media/` images. All return HTTP 200.
- All post pages render the correct GitHub avatar (no Gravatar fallbacks remain). Thomas Phinney correctly attributed on the DTL post.

### Known
- A background agent created an unprompted git commit `0a7adc5` ("Port 8 oldpub WordPress articles..."). The user did not request it. Subsequent edits (release-summary posts, image relocation, gravatar stripping, avatar fix) are uncommitted and ready for the user to review.
