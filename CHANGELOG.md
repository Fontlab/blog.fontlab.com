# Changelog

## [Unreleased] — 2026-09-02 — Image lightbox

### Added
- Click-to-zoom lightbox on post images, via `mkdocs-glightbox` (a MaterialX
  `recommended` plugin). Images open in an overlay gallery with keyboard and
  touch navigation; the assets ship from the site itself, no CDN.
- `mkdocs/hooks/glightbox_small_images.py` — build hook that stamps the
  plugin's own `off-glb` opt-out class onto any image whose intrinsic size is
  under 480px on both axes, so icons, avatars and small crops stay unzoomable.
  The decision is per image and reads the real file, so no Markdown changes are
  needed; `{ .off-glb }` in Markdown still works as a manual escape hatch.
- `tests/test_lightbox.py` covering the plugin wiring, the size threshold, the
  `src` resolution and the class stamping.

### Changed
- `.illu-thumb` hero/index illustrations are excluded from the lightbox
  (`skip_classes`): on the blog index they are the click-target for the post
  link (`js/illu-link.js`), which a lightbox anchor would hijack.
- Images that already sit inside a link (YouTube, Wikimedia sources) keep their
  link — the plugin skips them.
- TODO.md corpus counts refreshed to the live 135 posts / 42 unreviewed.

## [Unreleased] — 2026-07-05 — Repo modernization + honest content-state tests

### Added
- `[project.urls]` (Homepage, Source, Issues) and a minimal `[tool.mypy]`
  block in `pyproject.toml`.
- `docs/assets/icon.png` — a Steinberg-style single-line concept icon
  ("Markdown pushed, blog goes live"), palette-quantized to 1024×1024 / ~270 KB.
- New content invariants split into two honest tiers: core front matter
  (`title`/`date`/`authors`) required on every post, and review-schema checks
  (known `image_status`, body-matched `cta_target`) only for posts that carry
  the editorial `review:` overlay.

### Changed
- `tests/test_content_state.py` rewritten. The old tests asserted a
  "finished editorial sprint" state (every post reviewed, zero missing
  images) that the corpus outgrew when it doubled to 134 posts; they had
  rotted because CI runs `./build.sh build`, not pytest. The new tests
  encode invariants that are true today and keep the TODO.md summary honest.
- `TODO.md` now reports the true live counts (134 posts, 93 reviewed,
  41 awaiting review, 19 with a missing hero image) and records the real
  editorial backlog.
- Fixed a CTA drift in `2026-04-08-made-with-fontlab-fabio-duarte-martins.md`:
  the review `cta_target` pointed at a MyFonts collection while the published
  body links to the designer's own live catalogue; aligned the annotation to
  the shipped link.

### Removed
- Untracked accidental artifacts and added them to `.gitignore`: a broken
  `tmp_plugin_download` gitlink (submodule pointer with no `.gitmodules`),
  the `ruvector.db` AI vector cache (~1.5 MB), and the generated
  `src_docs-llms.txt` snapshot (~316 KB).

## [Unreleased] — 2026-07-02 — Frontpage AIDA leads + index-only thumbnails

### Added
- New `.illu-front` thumbnail mode in `extra.css`: the image shows as the
  200px card thumbnail on the blog index but is hidden on the post page.
  Completes the trio — `.illu-thumb` (post only), `.illu-thumb .illu-index`
  (both), `.illu-thumb .illu-front` (index only).
- New `.illu-photo` modifier: exempts photographic/color thumbnails from
  the dark-mode line-art invert filter; cover-fit with rounded corners.
- Six square 600×600 thumbnails in `src_docs/md/media/` (`*-thumb-sq.*`),
  cropped/resized via sips from i.vexy.art case art and landing heroes.

### Changed
- Rewrote the lead paragraph (excerpt above `<!-- more -->`) of all six
  Vexy Lines/Playlines posts as dense, self-standing AIDA leads for the
  blog index, and attached the index-only square thumbnail to each.

## [Unreleased] — 2026-07-02 — Vexy Lines teaser AIDA rewrite (issues/211.md)

### Changed
- Rewrote all six Vexy Lines / Playlines teaser posts (2026-06-22 …
  2026-06-30) as four-paragraph AIDA stories, each voiced for the target
  audience named in issues/211.md (type designers, brand/vector designers,
  poster designers, general graphic designers).
- Added judicious media per post: `https://i.vexy.art/vl/…` lead images,
  local `media/` screenshots, and one interactive element where it earns
  its place — Vexy Before-After sliders (typography, portraits, lettering)
  and one draggable Vexy Lines Nano (Playlines).
- Fixed component pitfalls: aligned before/after pairs only (swapped
  typography UI screenshots for the flamesq artwork pair; replaced the
  retro scan-vs-vector slider, whose framings don't align, with a static
  restored-scan image), and collapsed multi-line custom-element markup to
  a single line so Markdown emits real tags instead of escaped source.

### Verified
- `./build.sh build` clean; all six pages 200 on 127.0.0.1:8080; every
  local and remote image/script URL resolves (200); no escaped `&lt;vexy-…`
  markup in built HTML; excerpts render on the blog index.

## 2026-07-02 (earlier) — Vexy Lines teaser condensation

### Changed
- Condensed the six Vexy Lines / Playlines posts from 2026-06-22 through
  2026-06-30 into three-paragraph teasers.
- Replaced full case-study narration, image grids, embeds, headings, and
  references with short audience-specific copy that points readers to the actual
  Vexy Lines case pages or Playlines app.

### Verified
- Paragraph-count check confirms each edited source post has exactly 3 body
  paragraphs.
- `./build.sh build` completes successfully and regenerates all six public post
  pages.

## [Unreleased] — 2026-07-02 — Playlines embed export UI

### Fixed
- Removed the `copy` plugin from the Playlines blog embed so the embedded
  `<vexy-lines-nano>` widget shows a single SVG/PNG/PDF download dropdown
  instead of two adjacent format dropdowns.

### Verified
- `./build.sh build` completes.
- `node --check` passes for the relevant `i.vexy.art/docs/dist/lines-nano`
  plugin modules.
- Python Playwright on the localhost Playlines post confirms one dropdown exists
  and opening it shows `SVG`, `PNG`, `PDF`.

## [Unreleased] — 2026-07-01 — Vexy Lines series revision (issue 211, Tasks 1 & 2)

### Fixed / investigated (Task 1 — "new posts don't show on localhost")
- Diagnosed as **non-reproducing**: a clean `./build.sh build` regenerates all six
  post dirs and `live-server docs` serves each (HTTP 200) and lists all six on `/`.
  The build/serve pipeline is correct — the original symptom was a stale
  browser/live-server tab (reload socket doesn't fire on tabs opened before the
  server) or a view during "Cleaning site directory". Remedy: hard-refresh or
  restart live-server. No config change needed. (`draft_on_serve: true` only
  affects `properdocs serve`, not the static server, and these posts aren't drafts.)

### Changed (Task 2 — friendlier rewrite + better media)
- Rewrote all six posts in a warmer, more conversational register, each with its own
  twist: host/welcome (new-home), peer-to-peer + precise (typography), practical +
  space-crew humor (portraits), the print-shop-email running gag (lettering),
  hype/steal-the-look (retro), and playful "drag this" (Playlines).
- Replaced the weak placeholder images with **real case-study art** pulled from
  `www.vexy.art/dev_wf/lines/case-*` (web-ready stages, the Elara before→process→
  engraving, the balltext specimen, the teal/orange crew) and **live-site
  screenshots** captured via headless Chrome over CDP (cookie-consent modal
  dismissed by coordinate click; `shoot.py`).
- Portraits post now shows Elara's before/after + process (per brief) and drops the
  mismatched source-headshots collage.
- Fixed two swapped `this_file:` headers (06-23 typography, 06-29 retro).
- Removed 13 orphaned/superseded media files.

### Added (infra)
- **Tailwind CSS (Play CDN)** in `mkdocs/mk-fontlab/main.html` `extrahead`, with
  `corePlugins.preflight:false` and `important:'.md-typeset'` so utility classes work
  in post Markdown without the base reset clobbering the MaterialX theme. Posts use
  responsive `<img>` grids (`grid grid-cols-… gap-… my-…`) — authored as raw HTML with
  root-absolute `/media/…` paths so Flowmark's `--width 0` line-collapsing and
  `md_in_html`'s `<p>`-wrapping can't break the grid.
- A **live `<vexy-lines-nano>` embed** in the Playlines post (loads
  `i.vexy.art/dist/lines-nano/…`; image served with `ACAO: *` so the canvas isn't
  tainted), giving readers an interactive before/after they can drag.

### Verified
- `./build.sh build` completes (exit 0); Tailwind CDN present in built `<head>`.
- Browser render (headless, localhost:8080) confirms: 2- and 3-column grids lay out
  as columns; standalone images and screenshots load via `/media/`; the nano embed
  renders a live before/after split; MaterialX theme unaffected by Tailwind.
- All `../media/` and `/media/` references resolve to existing files; no missing images.

## [Unreleased] — 2026-06-30 — Vexy Lines week series (issue 211)

### Added
- Six `vexy-lines` blog posts, one per scheduled date:
  - `2026-06-22-vexy-lines-new-home.md` — the relaunched vexy.art/lines site + the Strokes Maker → Vexy origin story; opens the week-long series.
  - `2026-06-23-vexy-lines-retro-poster-revival.md` — Albert Kapr's 1977 poster revived as three variants; for poster/graphic designers (hype + humor).
  - `2026-06-24-vexy-lines-one-team-one-look.md` — unifying mismatched team headshots; for website/UI designers (problem-solving + the space-crew demo).
  - `2026-06-25-vexy-lines-lettering-that-survives-the-cutter.md` — flat vector patterns for vinyl/large-format; for vector/brand designers.
  - `2026-06-29-vexy-lines-type-that-reads-the-picture.md` — per-glyph variable-font instance selection; for type designers (precise).
  - `2026-06-30-vexy-playlines-paint-with-algorithms.md` — the free browser app; viral/emotional finale.
- 29 curated, date-prefixed images copied into `src_docs/md/media/` and referenced by the posts.
- Six social files in `src_docs/social/` (primary tweet + alternates + a 3-tweet thread + a LinkedIn variant each).
- Two researched SEO/virality recommendation docs: `www.vexy.art/dev_wf/ideas-260630.md` (vexy.art site) and `www.vexy.art/dev_wf/playlines/ideas-260630.md` (Vexy Playlines), each ~2,300 words with a NOW/NEXT/LATER roadmap and cited sources.

### Verified
- `./build.sh build` completes (exit 0); ProperDocs builds in ~5 s with only the pre-existing `topic/index.md` nav notice.
- All six posts render at `docs/2026/06/<dd>/<slug>/index.html`; 29 new media files copied into `docs/media/`.
- Every `../media/...` reference in the six posts resolves to an existing file.
- Frontmatter on all six posts matches the house schema after Flowmark (`this_file`, quoted title, `authors: [vexy-lines]`, nested `date.created`, `slug`; no `tags:` field).

## [Unreleased] — 2026-05-22 — Publish helper

### Added
- Added `./publish.sh`, which runs `./build.sh build`, verifies required `docs/` outputs, then runs `uvx gitnextver --directory <repo>` to commit/tag/push and trigger the existing tag-based GitHub Pages deploy workflow.
- Documented `./publish.sh` in `README.md`.

### Verified
- `bash -n publish.sh` passes.
- `./publish.sh` was not executed because it would create a git commit/tag and push.

## [Unreleased] — 2026-05-22 — Topic CTA spacing

### Changed
- Made in-content `.fl-help-cta` links more modest: plain text-link treatment, lighter weight, tighter top gap, and larger bottom gap before generated post lists.

### Verified
- `./build.sh build` completes successfully.
- Confirmed `/topic/vexy-lines/` renders the updated CTA style.

## [Unreleased] — 2026-05-22 — Topic overview page

### Added
- Added `src_docs/md/topic/index.md`, a hand-authored `/topic/` overview page listing all topic/profile pages.
- Added a regression test that requires every `authors.yml` topic slug to be linked from the topic overview page.

### Verified
- `./build.sh build` completes successfully and generates `docs/topic/index.html`.

## [Unreleased] — 2026-05-22 — Author profile topic pages

### Added
- Enabled MaterialX author profile generation for `/topic/{slug}/` pages and labelled the generated navigation section `Topics`, matching the site's use of `authors` as product/topic categories.
- Added source profile pages under `src_docs/md/topic/` for FontLab, Vexy Lines, TransType, TypeTool, Fontographer, FontLab Pad, and Adam Twardoch. Each page provides a short topic bio and external product/person link; MaterialX appends the matching post list.
- Added a content-state regression test that requires every author/topic entry to resolve to a local profile page instead of an external `url:`.

### Changed
- Updated `src_docs/md/authors.yml` descriptions and replaced external `url:` fields with explicit `slug:` fields so single-post author links now point to local profile pages.

### Verified
- `./build.sh build` completes successfully.
- Focused author-profile regression test passes.
- The hedcut post now links its Vexy Lines author entry to `/topic/vexy-lines/`.
- `/topic/vexy-lines/` renders the Vexy Lines bio followed by generated post excerpts, including "The hedcut at 45".

## [Unreleased] — 2026-05-22 — RSS date metadata fix

### Fixed
- `mkdocs/mkdocs.yml` RSS plugin: changed `date_from_meta.as_creation` from `date` to `date.created` and `as_update` from `git` to `date.updated`. The plugin was reading the whole `date` mapping (`{created, updated}`) and failing to parse it, which logged "Creation date … has not been recognized" for **every** post (126 INFO lines). With the dotted keys it reads the scalar creation date directly (falling back to git for posts without `date.updated`). A clean `./build.sh build` now emits **zero** date-retrieval messages.
- The separate "Dates could not be retrieved for page" messages on the 19 newly ported posts were resolved when those files were committed (they had been untracked, so the git date lookup found no history).

### Verified
- `./build.sh build` completes in ~4s with no ERROR/WARNING and no RSS date INFO messages.
- `docs/feed_rss_created.xml` / `feed_json_created.json` carry correct historical post dates (e.g. 2026-05-07, 2026-05-03 …) rather than build-date fallbacks; channel `pubDate` is the build date, as expected.

## [Unreleased] — 2026-05-22 — Old-blog migration gap audit

### Audit summary
- Scanned the WordPress static export in `private/blog/` against `src_docs/md/posts/` to find articles that were never migrated and are **not** sale/discount/pricing announcements.
- The export's canonical posts were identified by mapping each `/{yyyy}/{mm}/{dd}/` daily-archive page to its post permalink (the deepest non-category, non-feed, non-author, non-paginated link). 92 daily archives were found.
- **Snapshot is incomplete:** of the ~92 referenced posts, only **35 unique post pages have captured HTML** (48 files counting category-path duplicates). The rest — most `varia/*`, `learn/webinars/*`, `type-design/*`, and deep `fontlab/fontlab-studio-5/*` posts (e.g. "Sumner Stone superfamilies", "How to make stroke-only fonts", "Remembering Hermann Zapf", the webinar announcements) — exist only as links; **their content was never downloaded into this snapshot and cannot be ported from here.**
- Of the 35 captured unique posts: **10 already exist** in the new blog (color-font proposals → consolidated into `2026-05-03-color-fonts-in-2026`; create-multi-color-fonts → `2014-06-18-color-fonts-tutorial`; vfb2ufo → `2014-12-15-otmaster-5-vfb2ufo-fontlab-pad-11`; plus fontlab-vi-6-1, dtl-otmaster-7-9, 12-releases-in-12-months, fls5-fog5-tt3-catalina, introducing-fontlab-7, fontlab-72-dec-2020, and fontlab-vi-for-mac-and-windows → `2017-12-07-fontlab-vi-released`).
- **6 are sale/pricing/discount announcements — intentionally skipped** per the migration rule: cyber-monday-typetool-sale, 33-off-sale-605-update, fontlab-vi-1-3-off-to-august-31, fontlab-vi-2018-cyber-monday-sale, new-fontlab-vi-price-usd-459, fontlab-education-discounts-free-posters.

### Added
- Ported the **19 remaining non-sale posts** that were missing from the new blog, rewritten in the house editorial voice (strong lead, `<!-- more -->` excerpt, `.fl-help-cta` link, full `review:` front-matter block, `authors: [fontlab]`, original WordPress dates and slugs preserved, external image URLs dropped with `image_status: missing`):
  - `2013-09-18-fractional-coordinates.md` — technical explainer on fractional/floating-point outline coordinates.
  - `2013-09-22-opentype-layout-feature-classification.md` — reference article with the full OpenType Layout feature classification table.
  - `2013-10-30-fontlab-products-ok-mavericks-osx.md` — macOS 10.9 Mavericks compatibility note.
  - `2016-01-03-fontlab-vi-public-preview-2.md`, `2016-04-29-fontlab-vi-pp4-mac.md`, `2016-11-10-free-fontlab-vi-preview-windows.md` — FontLab VI public-preview milestones.
  - `2016-09-14-fontlab-opentype-variations.md` — FontLab's plans for OpenType 1.8 variable fonts (substantive vision/tech post).
  - `2016-12-19-fontlab-vi-ship-update.md` — VI development/ship status update.
  - `2016-12-28-deprecated-vs-discontinued.md` — explainer on how FontLab labels deprecated vs. discontinued products.
  - `2017-06-17-fontlab-vi-on-mac-os-10-9.md` — VI on macOS 10.9 support note.
  - `2017-09-19-update-2017-09.md` — "What's up with VI @ FontLab?" development status update.
  - `2017-09-26-fontlab-macos-high-sierra.md` — FontLab Studio / TypeTool / old TransType issues on macOS 10.13 High Sierra advisory.
  - `2018-08-13-fontlab-vi-6-0-9-update.md` — VI 6.0.9 release.
  - `2018-08-17-free-fontlab-vi-workshops-at-atypi-antwerp.md` — ATypI Antwerp 2018 workshops, rewritten as a past-tense historical record.
  - `2018-10-25-font-filters-components-and-metrics-in-fontlab-vi-6-1.md` — large 6.1 feature deep-dive (companion to the existing `2018-10-25-fontlab-vi-61` release post).
  - `2018-12-21-fontlab-vi-6-1-2.md`, `2019-03-26-fontlab-vi-6-1-3.md`, `2019-04-20-fontlab-vi-6-1-4.md` — VI 6.1.x point releases (each `review.consolidate_with` references the `2018-12-21-fontlab-vi-12-releases-in-12-months` roundup).
  - `2019-04-04-fontlab-studio-typetool-fontographer-mac-updates.md` — classic-app (Studio 5 / TypeTool / Fontographer) macOS compatibility updates.

### Verified
- `./build.sh build` completed in ~5s with no errors or warnings beyond the pre-existing RSS-plugin "creation date not recognized" informational notices; total published posts now 127.
- All 19 new files validated for required structure (single `<!-- more -->`, `.fl-help-cta` link, `this_file:`, `slug:`).
- Confirmed generated pages exist at their date-based URLs (e.g. `docs/2013/09/18/fractional-coordinates/`, `docs/2019/04/20/fontlab-vi-6-1-4/`).
- Several posts carry `cta_status: todo` (deprecated-vs-discontinued, high-sierra, atypi-workshops, mac-updates) where no clean live "read more" target was available; flagged in front matter for follow-up.

## [Unreleased] — 2026-05-08 (continued)

### Added
- Added `mkdocs-rss-plugin` (>=1.17, installed 1.19) and configured RSS 2.0 + JSON Feed 1.1 generation for `posts/*` with materialx blog integration (`use_material_blog: true`); produces `feed_rss_created.xml`, `feed_rss_updated.xml`, `feed_json_created.json`, `feed_json_updated.json` at the site root, with `<link rel="alternate">` autodiscovery wired into `mk-fontlab/main.html` `extrahead`.
- Added 40 localized external-image assets under `src_docs/md/media/external/`.
- Added `src_docs/md/media/external/_sources.txt` with source/fetch URL provenance for the localized image set.
- Added content-state regression tests for CTA targets, image review markers, and TODO summary counts.
- Added Flowmark 0.6.5 as a locked build dependency.
- Added `./build.sh format` / `blog-fontlab format` to format `src_docs/md/` in place with semantic line breaks, safe cleanups, smart quotes, and ellipses.
- Added focused CLI tests for build ordering and Flowmark smart-quote HTML tag repair.
- Added a regression test for both Flowmark-split `.fl-help-cta` Markdown attribute-list shapes.
- Generated root-level `docs/llms.txt` and `docs/llms-full.txt` through the `llmstxt` plugin.
- Added 32 issue-203 expansion posts from `spec/15.md`; only `nabla-colrv1-and-color-fonts`, `when-type-becomes-texture`, and `distortion-as-defense-2026` remain open.
- Added 2024–2026 roadmap posts for the Made with FontLab, FontLab TV, Briem, Calfonts, and Vexy Lines series.
- Added a local Vexy Lines interface image for `vexy-lines-and-the-useful-lie-of-engraving`, replacing a broken `doc360/Images` reference.
- Added `src_docs/md/posts/2026-05-03-color-fonts-in-2026.md`, a current consolidated color-font article covering COLR v1, variation, browser support, app/rendering support, and FontLab 8 support.
- Added local media references for FontLab Studio 5, Matthew Carter, Brush Romans, and FontLab TV posts that still had missing-image review markers.
- Added the verified FontLab YouTube recording link for the 2014 Matthew Carter webinar.

### Changed
- Rewrote 19 post files so embedded image references use `../media/external/...` instead of external `i.ytimg.com`, `i.fontlab.com`, Cloudinary, or Wikimedia image URLs.
- Resolved stale Wikimedia image paths through current Commons file URLs before localization.
- `./build.sh build` now runs Flowmark against `src_docs/md/` before cleaning `docs/` and running ProperDocs.
- Rewrote `2025-09-23-making-hangul-in-fontlab.md` to focus on Kwon Gun-oh's Korean *FontLab Type Design* book and its 2,780-glyph Hangul workflow instead of the older generic component-design angle.
- Build-time Flowmark formatting restores ASCII quote delimiters inside raw HTML tags and rejoins `.fl-help-cta` Markdown attribute lists after smart quote/line-wrap conversion, so legacy WordPress HTML attributes and CTA styling remain valid.
- Consolidated the three 2013 color-font proposal posts into the new 2026-05-03 article and updated the archive link in `2025-07-22-the-long-awkward-adolescence-of-color-fonts.md`.
- Replaced dead `calfonts.com` links in Dave Lawrence / California Type Foundry posts with the current MyFonts collection URL.
- Moved four duplicate consolidation candidate posts to `issues/draft-posts/` and left them marked as drafts so they stay out of the public blog until reviewed.
- Fixed the missing image reference in the 2025 color-font history post by pointing it at an existing FontLab gradient asset.
- Normalized current source-post CTA links from each post's `review.cta_target`, using live official FontLab help URLs where the older TODO target was stale.
- Updated verified CTA targets for TransType 4, FontLab VI release notes, FontLab 7 artwork import, the FontLab 8 intro tutorial, variable-font variations, and Scannerlicker.
- Updated the 2026 OpenType post's FontLab source reference from the older FontLab 7 manual page to the current FontLab 8 OpenType tutorial.
- Updated the variable-font file-size post CTA to the current FontLab 8 Families & variation chapter.
- Rewrote `opentype-is-where-good-manners-live` with a stronger small-caps example, formatted references, and a live OpenType help CTA.
- Enabled `include-markdown`, `llmstxt`, and `copy-to-llm` in `mkdocs/mkdocs.yml`.
- Expanded GitHub Actions output checks for the at-root layout: `docs/index.html`, `docs/about/index.html`, `docs/CNAME`, `docs/.nojekyll`, `docs/llms.txt`, and `docs/llms-full.txt`.
- Reconciled `TASKS.md` and `TODO.md` so completed configuration, post-list styling, FontLab 8.2 split, excerpt, llms, browser-check, Made with FontLab, and shipped issue-203 post-file tasks are removed from the open checklist.
- Tightened the template content container so narrow post pages no longer overflow horizontally.
- Kept the Brush Romans webinar CTA on the FontLab TV fallback after current web/video research found no stable recording URL.
- Retired the duplicate 2025-12-09 Vexy Lines signal/halftone draft after confirming the live Vexy Lines intro and engraving posts already cover the material.
- Rewrote `2018-12-21-fontlab-vi-12-releases-in-12-months.md` from the FontLab VI release-note archive instead of leaving it as a thin announcement.
- Replaced generic FontLab 8 placeholder images in the OTMaster, TransType Type 1 rescue, and Vexy Lines pipeline posts with product-specific local media.
- Added a `TODO.md` follow-up section for the 13 remaining generic placeholder image candidates that are not marked missing/weak in front matter.

### Verified
- Checked all `src_docs/md/posts/*.md` files for embedded external image URLs; none remain.
- Verified all 40 localized external-image files with `file` and `magick identify`.
- Built and visually inspected contact sheets for YouTube, FontLab/Briem, and Cloudinary/Wikimedia localized images.
- `uv run properdocs build -f mkdocs/mkdocs.yml -d /tmp/blog-fontlab-external-image-build` completed with only existing absolute-link and missing-post warnings.
- `uv run properdocs build -f mkdocs/mkdocs.yml` regenerated `docs/` and copied all 40 localized external images to `docs/media/external/`.
- `uv run --with pytest python -m pytest -q` remains blocked by the existing published-post `review:` metadata failures.
- `uv run --with pytest python -m pytest -q` now covers the content-state guardrails.
- `uv sync --frozen` completed with Flowmark in the lock file.
- `uv run blog-fontlab format` completed against the current 78 published Markdown source files with no `.bak` or `.orig` files.
- `uv run --with pytest python -m pytest -q` passed.
- `uvx ruff check src tests` passed.
- `./build.sh build` completed after running Flowmark first.
- `uvx ruff check src/` passed.
- Local checks found no smart-quote HTML attribute delimiters in `src_docs/md` or generated `docs`.
- Local CTA audit found no split `.fl-help-cta` attributes and no mismatch between source `review.cta_target` values and Markdown CTA links.
- HTTP checks returned 200 for the updated TransType 4, FontLab VI release notes, FontLab 7 importing artwork, FontLab 8 intro tutorial, FontLab 8 families & variation, and Scannerlicker catalogue CTA targets.
- Local checks confirmed the four named offline draft consolidation candidates remain under `issues/draft-posts/` with `draft: true`.
- Playwright browser smoke check at `http://127.0.0.1:8808/` covered home, Matthew Carter webinar, Brush Romans webinar, About, 2026 archive, and a retired color-font URL at desktop and mobile widths with no horizontal overflow, no relevant console errors, correct edited CTA hrefs, and HTTP 404 for the retired URL.
- `uv sync --frozen` completed.
- `./build.sh build` completed and generated root `llms.txt` and `llms-full.txt`.
- `uvx ruff check src/` passed.
- Local checks confirmed all current published posts include `<!-- more -->`, no post uses `authors: [editorial]` or `categories:`, CI sanity-check target files exist, `src_docs/md/posts/` currently contains 78 published Markdown posts, and 11 offline draft/research files live under `issues/draft-posts/`.
- Local build output contains 78 generated public post pages, `docs/llms.txt`, and `docs/llms-full.txt`.
- Local checks confirmed the three retired 2013 color-font pages are absent from generated `docs/`, the new 2026 color-font page exists, and no source or generated page links to the old color-font URLs.
- Current web research found the Matthew Carter recording at `https://www.youtube.com/watch?v=ibJhxbsbqJ4`; searches found the Brush Romans event listing/preview but no stable recording URL.
- Playwright checks found no horizontal overflow and no relevant console errors on home, the Matthew Carter webinar post, the Brush Romans webinar post, About, the 2026 archive, and a retired color-font URL at desktop and mobile widths.
- Verified the rewritten Hangul post against Aladin and Yes24 book metadata, and confirmed the post CTA target matches its `.fl-help-cta` body link.
- `uv run properdocs build -f mkdocs/mkdocs.yml -d /tmp/blog-fontlab-hangul-build` completed with only existing absolute-link informational notices.
- `uvx ruff check src tests` passed.

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
- First post: `blog/posts/2013-09-19-color-fonts.md` (color-fonts overview, ported from WordPress export; later replaced by the 2026 consolidated color-font guide).
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
