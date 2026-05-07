# Changelog

## [Unreleased] — 2026-05-07

### Added
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
- **Blog moved to site root.** `blog_dir: .` (was `blog`). Post URLs are now `/yyyy/mm/dd/slug/`; categories at `/category/<slug>/`; archive at `/archive/<yyyy>/`. Site index IS the blog index — no redundant landing page. Spec chapters 6 and 7 still describe the previous layout.
- `.nojekyll` is now written by the build pipeline (CLI `build` step) instead of being a static file. GitHub Pages requires it because MaterialX ships some `_`-prefixed asset directories.

### Verified
- `uv sync` — 56 packages, all from local `reference/` checkouts.
- `./build.sh build` — clean build, 0 errors. Outputs `docs/CNAME` and `docs/.nojekyll`.
- `uvx ruff check src/` — clean.
- Browser smoke test (Chrome DevTools): `/`, post pages render with menu, footer, author, date, categories, excerpt; no console errors.
