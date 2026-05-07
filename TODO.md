<!-- this_file: TODO.md -->
# TODO — blog.fontlab.com

Flat checklist derived from `spec/01.md`–`15.md`. Completed items are recorded in `CHANGELOG.md`. Only open items remain here.

## Foundation

- [ ] Drop `tool.uv.sources` local overrides in `pyproject.toml` once `properdocs` and `mkdocs-materialx` are on PyPI.
- [ ] Commit `uv.lock` and verify `uv sync --frozen` works in a clean environment.
- [ ] Add `src/blog_fontlab/__version__.py` to `.gitignore`.
- [ ] Verify `hatch-vcs` writes `__version__.py` correctly from a `v*.*.*` git tag.

## Site config

- [ ] Add `awesome-nav` plugin to `mkdocs.yml`.
- [ ] Add `vexy-output-as-input` plugin to `mkdocs.yml`.
- [ ] Add `vexy-strip-number-prefix` plugin to `mkdocs.yml`.
- [ ] Add `vexy-tags` plugin to `mkdocs.yml`.
- [ ] Verify `vexy_python_markdown_steroids.all` shorthand exists in the current package; fall back to explicit extension list if not.

## Theme & chrome

- [ ] Move chrome CSS from `src_docs/md/css/` to `src_docs/md/assets/css/` to match spec; update `extra_css`.
- [ ] Confirm exact colour token values against FontLab brand guide before v0.1.0 ships.
- [ ] Verify dark mode: page background matches `<fontlab-menu mode="dark">` background with no colour join at the seam.

## Typography sweep (issues/202.md)

- [ ] In every post under `src_docs/md/posts/`, replace ASCII `'` with proper Unicode apostrophes (U+2019) and `"` with English curly quotes (U+201C / U+201D), respecting code blocks and inline code (which must stay as-is).
- [ ] Surround every em dash (—) with normal spaces ` — ` (do not use thin spaces or no-break spaces); leave en dashes used in numeric ranges alone.
- [ ] Add a CI check (or `vexy-mkdocs-tools` lint subcommand) that flags straight quotes and unspaced em dashes in `posts/*.md`.

## Existing post fixes (issues/202.md)

- [ ] `2023/09/04/briem-decisions/`: pull figure images from `reference/fldoc/src/fontlab/8/md/tutorials/briem/3-0-decisions/` (and parent `briem/img/`) into `src_docs/md/media/briem/`; add captions.
- [ ] `2024-11-19-designers-on-fontlab.md`: convert from listicle to series anchor. Each subsequent series entry profiles ONE designer + their fonts (see `spec/13.md` schedule).

## Content — porting backlog

- [ ] Source the full body of the 2013 colour-fonts article (Wayback Machine or backup); replace any remaining placeholder.
- [ ] Run `pandoc -f html -t markdown_strict` on each surviving oldpub post as a conversion starting point (already done for the 8 ported; document the recipe in `spec/11.md`).
- [ ] Rewrite internal links: `fontlab.com/blog/...` → relative `/...` if target is ported; drop if target is retired.
- [ ] Verify all `help.fontlab.com` external links in ported posts still resolve.
- [ ] Annotate dead external links inline rather than silently removing them.
- [ ] Store all post images in `src_docs/md/media/` (current convention); ensure descriptive kebab-case filenames.
- [ ] Compress all ported images to ≤500KB; enforce 1200px max width.
- [ ] Add alt text to every image in every post.

## Editorial roadmap (spec/13.md, spec/14.md)

- [ ] Write the 12 planned 2026 posts (Jan–May 2026) per `spec/13.md`.
- [ ] Write the 24 planned 2025 posts (2/month) per `spec/13.md`.
- [ ] Write the 24 planned 2024 posts (2/month) per `spec/13.md`, deduping with already-shipped slugs.
- [ ] Build the "FontLab TV" companion series (one post per Kapusta chapter, 25 chapters) per `spec/14.md`. Pack 2024–2026 with these.
- [ ] Build the "Tutorials" series modernizing `briem/4-2-bold` … `briem/7-0-glossary` and selected `calfonts/` chapters per `spec/14.md`.
- [ ] For every planned post that is currently `TBD: select topic from <source>` in `spec/13.md`, lock the topic before drafting.

## Build & deploy

- [ ] Configure GitHub repository: Settings → Pages → Source: `gh-pages` branch, `/ (root)`.
- [ ] Add DNS `CNAME` record: `blog.fontlab.com → fontlab.github.io`.
- [ ] Enable branch protection on `main`: require PR review + `build` status check before merge.
- [ ] Push `v0.1.0` tag to trigger first deploy.
- [ ] Wait for TLS certificate provisioning and verify `https://blog.fontlab.com/` loads over HTTPS.
- [ ] Add `pull_request_template.md` at `.github/pull_request_template.md` with authoring checklist from `spec/11.md`.

## Quality

- [ ] Install `lychee` and run `lychee --offline docs/` against the local build output.
- [ ] Add `.lycheeignore` suppressing `fonts.googleapis.com` and `fonts.gstatic.com`.
- [ ] Add scheduled (weekly) external link check job to `ci.yml` using `lychee docs/ --exclude-all-private`.
- [ ] Verify Web Component local nav items (Blog, Archive, About) are visible in the rendered menu.
- [ ] Verify RSS feed after deploy; confirm content and post ordering.
- [ ] DECIDE: RSS feed URL — accept plugin default or alias as `/feed.xml`?
- [ ] Maintain `pin: true` on the most-recent series anchor post once the editorial roadmap rolls forward.

## Issue 203 — Draft expansion

Thirty-two of the 35 issue-203 posts from `spec/15.md` now exist in `src_docs/md/posts/` and build as public pages. The remaining three are still open.

- [ ] 2025-07-01 — `nabla-colrv1-and-color-fonts` (source: `403-grok:section-4`)
- [ ] 2026-02-17 — `when-type-becomes-texture` (source: `401-grok:section-4`)
- [ ] 2026-03-31 — `distortion-as-defense-2026` (source: `406-gemi:distortion`)

### Follow-ups

- [ ] Add provenance `_sources.txt` for `the-long-awkward-adolescence-of-color-fonts`.
- [ ] Re-read issue-203 posts after they ship and add cross-links between related posts.
- [ ] Reconcile any issue-203 date collisions with `spec/13.md` and update that chapter's date table.
