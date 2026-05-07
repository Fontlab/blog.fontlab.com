# Work — blog.fontlab.com

## In progress

- (none — session deliverables shipped)

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
