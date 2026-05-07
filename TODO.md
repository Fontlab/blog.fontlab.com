<!-- this_file: TODO.md -->
# TODO — blog.fontlab.com

Flat task checklist derived from spec/01.md–12.md. Items marked `[x]` shipped in the 2026-05-07 session.

> **Note (2026-05-07):** the blog now lives at the site root (`blog_dir: .`), not under `/blog/`. Post URLs are `/yyyy/mm/dd/slug/`; categories at `/category/<slug>/`; archive at `/archive/<yyyy>/`. Spec chapters 6 and 7 still describe the old layout — reconcile when convenient.

## Foundation

- [x] Create `pyproject.toml` with hatchling + hatch-vcs, `requires-python = ">=3.12"`, all plugin dependencies pinned.
- [x] Create `src/blog_fontlab/__init__.py` (empty).
- [x] Create `src/blog_fontlab/cli.py` with Fire CLI exposing `build`, `serve`, `clean`.
- [x] Register `blog-fontlab` entry point in `pyproject.toml` `[project.scripts]`.
- [x] Create `build.sh` as thin `uv run blog-fontlab "$@"` wrapper with `set -euo pipefail`.
- [x] Run `uv sync` and verify all 56+ packages resolve (including local `reference/` sources).
- [ ] Drop `tool.uv.sources` local overrides in `pyproject.toml` once `properdocs` and `mkdocs-materialx` are on PyPI.
- [ ] Commit `uv.lock` and verify `uv sync --frozen` works in a clean environment.
- [ ] Add `src/blog_fontlab/__version__.py` to `.gitignore`.
- [ ] Verify `hatch-vcs` writes `__version__.py` correctly from a `v*.*.*` git tag.

## Site config

- [x] Create `mkdocs/mkdocs.yml` with `theme: materialx`, `palette: scheme: slate`, `docs_dir: ../src_docs/md`, `site_dir: ../docs`.
- [x] Add `materialx/blog` plugin block with full config from spec/07.md (archive, categories, authors, pagination, draft, slugify, readtime).
- [x] Add `materialx/tags` plugin.
- [ ] Add `awesome-nav` plugin to `mkdocs.yml`.
- [ ] Add `include-markdown` plugin with `opening_tag: "{!"` and `closing_tag: "!}"`.
- [ ] Add `llmstxt` plugin (`enabled: true`) to `mkdocs.yml`.
- [ ] Add `copy-to-llm` plugin (`enabled: true`) to `mkdocs.yml`.
- [ ] Add `vexy-output-as-input` plugin to `mkdocs.yml`.
- [ ] Add `vexy-strip-number-prefix` plugin to `mkdocs.yml`.
- [ ] Add `vexy-tags` plugin to `mkdocs.yml`.
- [x] Add full `markdown_extensions` block (pymdownx suite + admonition + footnotes + toc + vexy_python_markdown_steroids).
- [ ] Verify `vexy_python_markdown_steroids.all` shorthand exists in the current package; fall back to explicit extension list if not.
- [ ] Set `nav:` in `mkdocs.yml` to include only `index.md` and `about.md`; exclude blog posts (plugin owns those).
- [ ] Add `extra_css` entries for `assets/css/fontlab-chrome.css` and `assets/css/extra.css`.
- [ ] Add `custom_dir: mk-fontlab` to `theme:` block in `mkdocs.yml`.

## Theme & chrome

- [x] Create `mkdocs/mk-fontlab/main.html` extending `base.html`, injecting `<script defer src="https://i.fontlab.com/menu/fontlab.js">`, `<fontlab-menu>`, `<fontlab-footer>`, and `DOMContentLoaded` config assignment.
- [x] Wire `localMenu` config object with Blog, Archive, About items in `main.html`.
- [ ] Create `src_docs/md/assets/css/fontlab-chrome.css` with `.md-header { display: none !important; }` and `.md-main { padding-top: 0; }`.
- [ ] Create `src_docs/md/assets/css/extra.css` with CSS custom property tokens (`--fl-bg`, `--fl-fg`, `--fl-accent`, `--fl-code-bg`, `--fl-border`).
- [ ] Confirm exact colour token values against FontLab brand guide before v0.1.0 ships.
- [ ] Verify dark mode: page background matches `<fontlab-menu mode="dark">` background with no colour join at the seam.
- [ ] Disable MaterialX light/dark toggle by omitting `toggle` block from `palette:` in `mkdocs.yml`.

## Content

- [x] Create `src_docs/md/index.md` landing page (Option B: brief intro + "Read the blog" link, under 300 words, good for search indexing).
- [x] Create `src_docs/md/about.md` condensed from `reference/fontlab-com-oldpub/about/index.html`, under 300 words.
- [x] Create `src_docs/md/blog/index.md` (minimal; plugin overrides this page).
- [x] Create `src_docs/md/blog/.authors.yml` with `adam` entry (name, description, avatar URL, external URL).
- [ ] Upload author avatar to `https://i.fontlab.com/assets/authors/adam.jpg` and update `avatar:` field in `.authors.yml`.
- [x] Create `src_docs/md/blog/posts/2013-09-19-color-fonts.md` with correct front-matter (`date.created: 2013-09-23`, `draft: false`).
- [ ] Source the full body of the 2013 colour fonts article (Wayback Machine or backup); replace the `<!-- TODO -->` placeholder in the post.
- [ ] Verify `<!-- more -->` separator is present and excerpt reads as a standalone paragraph.
- [ ] Run `pandoc -f html -t markdown_strict` on each surviving oldpub post as a conversion starting point.
- [ ] Review all oldpub posts in `reference/fontlab-com-oldpub/`; identify 3–5 survivors beyond the 2013 piece.
- [ ] Port each surviving oldpub post: add front-matter, fix code blocks, strip WordPress metadata markup, verify prose.
- [ ] Preserve original `date.created` from HTML metadata for every ported post; never use today's date for historical content.
- [ ] Rewrite internal links: `fontlab.com/blog/...` → relative `/blog/...` if target is ported; drop if target is retired.
- [ ] Verify all `help.fontlab.com` external links in ported posts still resolve.
- [ ] Annotate dead external links in ported posts with an inline note rather than silently removing them.
- [ ] Store all post images in `src_docs/md/blog/posts/img/`; ensure descriptive kebab-case filenames.
- [ ] Compress all ported images to ≤500KB; enforce 1200px max width.
- [ ] Add alt text to every image in every post.
- [ ] Review `reference/fldoc/` for news-style summaries worth porting; port candidates only.
- [ ] DECIDE: home page — keep Option B landing or switch to Option A redirect template?

## Build & deploy

- [x] Move `CNAME` to `src_docs/md/CNAME` so the build pipeline copies it to `docs/CNAME`.
- [x] Verify `docs/CNAME` contains `blog.fontlab.com` after `./build.sh build`.
- [x] Confirm `.nojekyll` is present in build output (prevents GitHub Pages Jekyll processing).
- [x] Create `.github/workflows/ci.yml` with tag-triggered deploy via `peaceiris/actions-gh-pages@v4`, `fetch-depth: 0`, `uv sync --frozen`.
- [ ] Expand CI sanity checks to assert `docs/blog/index.html`, `docs/about/index.html`, and `docs/llms.txt` exist after build.
- [ ] Configure GitHub repository: Settings → Pages → Source: `gh-pages` branch, `/ (root)`.
- [ ] Add DNS `CNAME` record: `blog.fontlab.com → fontlab.github.io`.
- [ ] Enable branch protection on `main`: require PR review + `build` status check before merge.
- [ ] Push `v0.1.0` tag to trigger first deploy.
- [ ] Wait for TLS certificate provisioning and verify `https://blog.fontlab.com/` loads over HTTPS.
- [ ] Add `pull_request_template.md` at `.github/pull_request_template.md` with authoring checklist from spec/11.md.

## Quality

- [ ] Install `lychee` and run `lychee --offline docs/` against the local build output.
- [ ] Add `.lycheeignore` suppressing `fonts.googleapis.com` and `fonts.gstatic.com`.
- [ ] Add scheduled (weekly) external link check job to `ci.yml` using `lychee docs/ --exclude-all-private`.
- [ ] Browser render check at 1280px and 375px: home, blog index, single post, archive, about — confirm no layout breaks.
- [ ] Verify Web Component local nav items (Blog, Archive, About) are visible in the rendered menu.
- [ ] Verify RSS feed at `/blog/feed.xml` after deploy; confirm content and post ordering.
- [ ] Verify `llms.txt` and `llms-full.txt` are generated at site root and contain meaningful content.
- [ ] DECIDE: RSS feed URL — accept plugin default `/blog/feed.xml` or add a `/feed.xml` alias?
- [ ] Add `pin: true` to the front-matter of the most recent post once the post backlog is ported.
