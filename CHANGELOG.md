# Changelog

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
