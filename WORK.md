# Work — blog.fontlab.com

## In progress

- (none — session deliverables shipped)

## Shipped (2026-05-08 sprint)

### Flowmark build formatting
- Added Flowmark 0.6.5 to the locked project dependencies.
- Added `blog-fontlab format` / `./build.sh format` for in-place formatting of `src_docs/md/`.
- `blog-fontlab build` now runs Flowmark before cleaning `docs/` and running ProperDocs.
- Flowmark runs with semantic line breaks, safe cleanups, smart quotes, and ellipses.
- Added a post-Flowmark repair step that restores ASCII quote delimiters inside raw HTML tags so legacy WordPress HTML attributes stay valid.

### Content and task reconciliation
- Reconciled `TASKS.md` and `TODO.md` against the current root-layout site.
- Current source tree: 113 Markdown posts in `src_docs/md/posts/`.
- Issue 203 draft expansion: 32 of 35 post files exist and build. Remaining open slugs: `nabla-colrv1-and-color-fonts`, `when-type-becomes-texture`, `distortion-as-defense-2026`.
- Completed post-list/CTA styling, Made with FontLab series, browser-check, llms, and stale configuration items were removed from the open checklist and recorded in `CHANGELOG.md`.

### Fixes
- Removed stale `categories:` front matter and unknown `editorial` authors from new posts.
- Replaced premature internal links to unshipped draft posts with plain text where needed.
- Fixed narrow-post overflow in `mkdocs/mk-fontlab/main.html`.
- Moved the Vexy Lines engraving post image to `src_docs/md/media/vexy-lines-and-the-useful-lie-of-engraving/` and updated the post link so the asset builds.

### Verified
- `uv run blog-fontlab format` — complete; no `.bak` or `.orig` files created.
- `./build.sh build` — complete, no warnings.
- `uv sync --frozen` — complete.
- `uvx ruff check src/` — clean.
- Source/generated HTML quote check — no smart-quote attribute delimiters in `src_docs/md` or `docs`.
- Output sanity: `docs/index.html`, `docs/about/index.html`, `docs/CNAME`, `docs/.nojekyll`, `docs/llms.txt`, `docs/llms-full.txt` exist.
- Counts: 113 source posts, 113 generated public post pages.
- Browser checks: Playwright screenshots saved for home, post, archive, and about; Chrome DevTools found no horizontal overflow and no console errors on checked pages.

## Shipped (2026-05-07 session)

### Foundation
- `CLAUDE.md`, `README.md`, `CHANGELOG.md`, `WORK.md`, `TODO.md` (72-item flat checklist).
- `uv` project: `pyproject.toml` (hatchling + hatch-vcs), `src/blog_fontlab/{__init__,cli}.py` (Fire CLI: `build` / `serve` / `clean`), `build.sh`. 56 packages resolve from local `reference/` checkouts.
- `mkdocs/mkdocs.yml` — ProperDocs + MaterialX, full pymdownx extension set, search + tags + blog plugins.
- `mkdocs/mk-fontlab/main.html` — template loading the shared FontLab Web Component menu/footer from `https://i.fontlab.com/menu/`.
- CSS: `src_docs/md/css/{fontlab-chrome,extra}.css`.
- Theme update: partner-site typography fonts loaded in the template, MaterialX font autoloading disabled, and `src_docs/md/css/extra.css` added for heading and CTA styling.
- Footer CTA band: three FontLab-wide actions (`Buy FontLab`, `Explore FontLab`, `Questions first?`) linking to `fontlab.com/buy`, `fontlab.com`, and `fontlab.com/contact`.
- `.github/workflows/ci.yml` — tag-triggered (`v*.*.*`) deploy to `gh-pages` via `peaceiris/actions-gh-pages@v4`.
- `src_docs/md/{CNAME,.nojekyll}` handling so both survive the build.

### Spec
- 13-file spec at `spec/00-toc.md` + `spec/01.md`…`spec/12.md`.

### Content (12 posts spanning 2013–2024)
- 1 ported blog post: 2013 color-fonts overview.
- 7 ported release announcements (DTL OTMaster 7.9, FontLab VI 12-in-12, FLS5/Fog5/TT3 on Catalina, Introducing FontLab 7, Hello FontLab 7.2, FL 7.2.0.7644 + Monterey, Hello FontLab 8.2).
- 4 written from inventory of fldoc/FontLabVI-help release notes: FontLab VI launch (2017-12-07), FontLab 7 year-in-review (2020-12-30), Hello FontLab 8 (2022-06-26), FontLab 8.3/8.4 roundup (2024-06-05).
- Most-recent post pinned (`pin: true`).
- 1 promo post intentionally dropped ("Save $40").
- About page: ~750-word company history.
- Author registry: `adam` (Adam Twardoch) + `thomas` (Thomas Phinney), both with stable GitHub avatar URLs.

### Media
- 7 images downloaded from `wp-content/uploads/` to `src_docs/md/media/` (1.7 MB total).
- Image references in posts rewritten to `/media/<file>`.

### Layout decisions
- Blog at site root (`blog_dir: .`). Post URL: `/yyyy/mm/dd/slug/`. Categories at `/category/<slug>/`. Archive at `/archive/<yyyy>/`.
- WordPress "About the Author" footer blocks (Gravatar + bio paragraph) stripped from every ported post; the blog plugin renders authors via `.authors.yml` instead.

### Verified
- `./build.sh build` — clean, 0 errors, 0 warnings.
- `uvx ruff check src/` — clean.
- Chrome DevTools: desktop CTA columns align; 390px mobile CTA stacks without horizontal overflow; single-post heading and body render coherently; no console errors.
- Curl: site root, page 2 (pagination), all 8 archive years, both category pages, About page, every post URL, sitemap (26 entries), `/media/` images — all HTTP 200.
- Avatars: GitHub URLs only (no Gravatar fallbacks). Thomas Phinney correctly attributed on the DTL post.

## Open follow-ups (next sessions)

- Reconcile `spec/06.md` and `spec/07.md` with the at-root blog layout.
- The 2013 color-fonts post initially ported as teaser-only; pandoc conversion later ported the full body. Verify that the body matches the Wayback / archive original.
- Drop `tool.uv.sources` overrides in `pyproject.toml` once `properdocs` and `mkdocs-materialx` are reliably resolvable from PyPI.
- Ship `vexy-mkdocs-tools` per IDEA.md so the blog can eventually call `uvx vexy-mkdocs-tools build` instead of `properdocs build` directly.
- Modernize `vexy-mkdocs-markdown-in-template` (currently missing from `reference/`) and relax `vexy-marktripy`'s Python 3.12-only pin.
- Verify Thomas Phinney's GitHub avatar URL (currently a guessed user ID — `3043872` may not match).
- Stripped excerpt content sometimes ends with a stub paragraph from the WP export; quick polish pass would catch any leftover scaffolding.
- An unprompted commit (`0a7adc5`) was made by a background agent; subsequent porting/relocation/cleanup edits are uncommitted.
