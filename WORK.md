# Work — blog.fontlab.com

## In progress

- (none — session deliverables shipped)

## Done (2026-05-07 session)

- Repo init: `CLAUDE.md`, `CHANGELOG.md`, `WORK.md`, `README.md`.
- uv project scaffold: `pyproject.toml` (hatchling + hatch-vcs), `src/blog_fontlab/{__init__,cli}.py`, `build.sh`. `uv sync` ✓ (56 packages from local `reference/` sources). `blog-fontlab build|serve|clean --help` all responding.
- ProperDocs config: `mkdocs/mkdocs.yml` with materialx theme, blog plugin (archive/categories/authors/pagination), full pymdownx extension set.
- Template: `mkdocs/mk-fontlab/main.html` loading `<fontlab-menu>` + `<fontlab-footer>` from `https://i.fontlab.com/menu/fontlab.js`, MaterialX chrome hidden via `src_docs/md/css/fontlab-chrome.css`.
- Content skeleton: `index.md`, `about.md` (full ~750-word company history), `blog/index.md`, `blog/.authors.yml`, `blog/posts/2013-09-19-color-fonts.md`.
- CNAME moved to `src_docs/md/CNAME` so the build pipeline preserves it.
- GitHub Actions: `.github/workflows/ci.yml` — tag-triggered deploy to `gh-pages` with `peaceiris/actions-gh-pages@v4`.
- Local build: `./build.sh build` runs clean.
- Browser smoke test (chrome-devtools MCP): `/`, `/blog/`, single-post route all render correctly. Web Component menu/footer load from `i.fontlab.com`. Author + date + categories + excerpt + "Continue reading" all wired. 0 console errors.

## Restructure (later in session)

- Blog moved to site root: `blog_dir: .` in mkdocs.yml; src_docs/md/blog/* contents flattened into src_docs/md/. Post URLs are now `/yyyy/mm/dd/slug/`. Re-verified in browser. Spec chapters 6/7 reference the old layout — to be reconciled later.

## Open follow-ups (next sessions)

- Reconcile spec/06.md and spec/07.md with the at-root blog layout.
- The 2013 color-fonts post in the WordPress export is teaser-only (~80 words). Source the full article body from a backup, the Wayback Machine, or rewrite from outline. The `<!-- TODO -->` marker is in the post.
- Drop `tool.uv.sources` overrides in `pyproject.toml` once `properdocs` and `mkdocs-materialx` are reliably resolvable from PyPI in CI.
- Ship `vexy-mkdocs-tools`: per IDEA.md, the blog should eventually call `vexy-mkdocs-tools build` instead of `properdocs build` directly. The wrapper should bundle the standard plugin/extension stack.
- Modernize `vexy-mkdocs-markdown-in-template` (currently missing from `reference/`) and `vexy-marktripy` (Python 3.12-only pin).
- Author avatar: pick a canonical URL once one exists; currently the `avatar:` field is omitted.
- Consider porting more "news"-style summaries from `reference/fldoc/` and `reference/FontLabVI-help/` per IDEA.md content rules.

## WordPress Article Porting (2026-05-07, continued session)

- Completed WordPress inventory via background agent: `.omc/notes/oldpub-inventory.md`
  - Result: 9 articles identified across 2013–2023
  - 8 articles to port (1 blog + 7 releases)
  - 1 promo article (dropped per spec)
  
- Ported all 8 articles to Markdown:
  - HTML → Markdown conversion via pandoc
  - Front-matter: date.created, title, categories, author, draft: false
  - Saved as `YYYY-MM-DD-slug.md` in `src_docs/md/posts/`
  
- Image handling:
  - Downloaded 7 images from wp-content/uploads/ (total 1.7 MB, all <500KB)
  - Stored in `src_docs/md/posts/img/`
  - Updated Markdown image references to local paths
  
- Build & testing:
  - Blog builds successfully with all 8 posts
  - 9 HTML post pages generated at `/YYYY/MM/DD/slug/` paths
  - Dev server tested: all pages render correctly
  - Added `pin: true` to most recent post (2023-08-09)
  - Removed duplicate stub post
  
Next: visual testing, link verification, alt text audit, optional additional content sourcing

