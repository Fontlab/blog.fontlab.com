<!-- this_file: README.md -->

# blog.fontlab.com

Build orchestrator for the FontLab blog, published to
[blog.fontlab.com](https://blog.fontlab.com/) via GitHub Pages. Posts are
authored as Markdown in `src_docs/md/posts/`, built with
[ProperDocs](https://github.com/fontlab/properdocs) (an MkDocs-based pipeline
with the MaterialX theme), and the generated HTML is deployed to the
**`gh-pages`** branch by GitHub Actions.

## Quick start

```bash
uv sync          # install dependencies into .venv/
./build.sh build # Flowmark-format src_docs/md, then build docs/
./build.sh serve # live-reload preview at http://localhost:8000
./publish.sh     # build docs/, create next v*.*.* tag, push to trigger deploy
```

You do **not** have to run `publish.sh` to ship a post. Any push to `main`
(including a single new Markdown file) triggers the deploy workflow — see
[Publishing & deploy](#publishing--deploy). `publish.sh` is the heavier path
that also stamps a version tag.

## Writing a post

1. Open [**src_docs/md/posts/**](https://github.com/Fontlab/blog.fontlab.com/tree/main/src_docs/md/posts).
2. **Create a post:** choose **Add file → Create new file**, name it
   `YYYY-MM-DD-your-slug.md`, and paste a [post example](#post-examples).
   Set `this_file`, `title`, `authors`, `date.created` and `slug` for your post.
   Choose an author key from [authors.yml](src_docs/md/authors.yml).
3. **Edit a post:** click the existing file, then **Edit this file** (pencil).
   Keep its `date.created` and `slug` to preserve its URL.
4. Write the summary above `<!-- more -->` and the article below it.
   Check the text, links and images using **Preview**.
5. Click **Commit changes**, select **Commit directly to the main branch**,
   and confirm. GitHub Actions rebuilds and republishes the blog automatically.
6. Check [GitHub Actions](https://github.com/Fontlab/blog.fontlab.com/actions/workflows/ci.yml)
   for a successful deploy, then check your post on [blog.fontlab.com](https://blog.fontlab.com/).

## Post examples

Copy an example and replace its metadata, text and images with your post's content.

### Example 1: product announcement with a clear next step

Adapted from [FontLab Pad 2](src_docs/md/posts/2026-09-17-fontlab-pad-2.md).
Use this structure when the reader needs a problem, an outcome and a download
link. Sample filename: `2026-09-17-try-fonts-in-pad.md`.

```markdown
---
this_file: src_docs/md/posts/2026-09-17-try-fonts-in-pad.md
title: "FontLab Pad 2: try a font, then take your text with you"
authors: [fontlab-pad]
date:
  created: 2026-09-17
slug: try-fonts-in-pad
---

Your layout app may not show every style or glyph in a font.
[FontLab Pad 2](https://www.fontlab.com/fontlab-pad/) lets you try the font
without installing it, shape your text, and copy the result into your work.

<!-- more -->

## Open the font without installing it

Open the font file in Pad and type your text. Your system font menus stay
unchanged while you try the design.

## Take the result into your layout

Choose the style and glyph variants you need, then copy the result as PDF,
SVG or Bitmap and paste it into your design or presentation app.

[Get FontLab Pad →](https://www.fontlab.com/fontlab-pad/){ .fl-help-cta }
```

### Example 2: release notes grouped by the work they improve

Adapted from [Vexy Lines 2](src_docs/md/posts/2026-06-07-vexy-lines-2.md).
Group changes under useful headings instead of writing one long feature list.
Sample filename: `2026-06-07-vexy-lines-update-highlights.md`.

```markdown
---
this_file: src_docs/md/posts/2026-06-07-vexy-lines-update-highlights.md
title: "Vexy Lines 2: clearer signals, sharper masks"
authors: [vexy-lines]
date:
  created: 2026-06-07
slug: vexy-lines-update-highlights
---

Vexy Lines 2 adds image filters and sharp masks, with improvements throughout
the drawing workflow. Here are two places to start with the update.

<!-- more -->

## Shape the source before generating the lines

Add image filters in the Properties panel to change how a fill interprets
its source image:

- Adjust brightness and contrast to change the balance of light and dark.
- Sharpen the source to bring out detail.
- Reorder filters to try a different result.

## Keep strokes inside the mask

A **Sharp mask** cuts the rendered strokes at the mask boundary. Use it
when the stroke edges need to stay within the selected region.

## Get the update

If you already use Vexy Lines, choose **Check for Updates** in the app.

[Explore Vexy Lines →](https://vexy.art/lines/){ .fl-help-cta }
```

### Example 3: a tutorial with steps and a screenshot

Adapted from the instance-conversion workflow in
[TransType 5](src_docs/md/posts/2026-09-02-transtype-5.md).
Sample filename: `2026-09-02-export-variable-font-instances.md`.
Replace the screenshot with your own when documenting a different workflow.

```markdown
---
this_file: src_docs/md/posts/2026-09-02-export-variable-font-instances.md
title: "Turn a variable font instance into a font your app can use"
authors: [transtype]
date:
  created: 2026-09-02
slug: export-variable-font-instances
---

Your variable font contains the style you want, but your app does not offer
it. Export that instance as a static font in TransType 5.

<!-- more -->

## Convert the instance

1. Drop your variable font into TransType 5.
2. Choose **File > Add Instance**, or click **+ Instance** in the family bar.
3. Add the in-between style you want to use.
4. Choose a static output format and destination, then click **Convert**.

![TransType's Add Instance workflow](https://cdn.prod.website-files.com/59f8b0f378cc2d0001fd32e5/6a982b9439dc6a86ba2b85be_tr5-screen-13-add-instance-light.png)

## Check the result in your app

Install the exported font, or turn on **Install Fonts** in TransType's
Destination dropdown before conversion. You may need to restart your
layout app before the new style appears in its font menu.

[Explore TransType →](https://www.fontlab.com/font-converter/transtype/){ .fl-help-cta }
```

### Example 4: a short teaser with an index thumbnail

Adapted from [Play with lines](src_docs/md/posts/2026-06-30-vexy-playlines-play-with-lines.md).
Use this when the main experience is on another page. A live widget is
optional; a clear link is enough. Sample filename: `2026-06-30-try-playlines.md`.

```markdown
---
this_file: src_docs/md/posts/2026-06-30-try-playlines.md
title: "One photo, a different set of lines"
authors: [vexy-lines]
date:
  created: 2026-06-30
slug: try-playlines
---

![Halftone portraits made with Playlines](../media/2026-06-30-thumb-sq.jpg){ .illu-thumb .illu-front .illu-photo }

Drop a photo into [Vexy Playlines](https://playlines.vexy.art/), choose a
fill, and watch it become vector artwork in your browser.

<!-- more -->

Move the controls to change the pattern and compare it with your source
image. The same photo can become a field of lines, dots or triangles.

Download the result as SVG and take it into your design app. Start with
your own photo: seeing the pattern change is the useful part.

[Try Playlines →](https://playlines.vexy.art/){ .fl-help-cta }
```

### Example 5: a designer story with a specific takeaway

Adapted from [Made with FontLab: Fábio Duarte Martins](src_docs/md/posts/2026-04-08-made-with-fontlab-fabio-duarte-martins.md).
Use this structure for a person's work and methods. Link to the original
work, credit images, and quote only statements you have checked.
Sample filename: `2026-04-08-scannerlicker-workflow.md`.

```markdown
---
this_file: src_docs/md/posts/2026-04-08-scannerlicker-workflow.md
title: "Made with FontLab: a look at Scannerlicker's workflow"
authors: [adam]
date:
  created: 2026-04-08
slug: scannerlicker-workflow
---

Fábio Duarte Martins runs Scannerlicker. His account of working in FontLab
names the tools he uses, giving other designers a practical place to start.

<!-- more -->

## The tools behind the work

His testimonial highlights drawing tools, FontAudit, masks and layers for
multiple masters, and expressions and tags for organizing production work.

## A useful place to start

Choose one repetitive task in your own project. Look at how expressions or
tags could make that task easier before trying to automate the whole font.

## See the finished typefaces

The foundry's catalogue puts the workflow in context: the tools serve the
letters, and the letters are what readers will see.

[Browse Scannerlicker →](https://fonts.scannerlicker.net/){ .fl-help-cta }
```

### Example 6: a recording with a linked preview image

Adapted from the [Matthew Carter webinar](src_docs/md/posts/2014-02-15-matthew-carter-webinar.md).
A thumbnail linking to the recording is simpler than an iframe and works
without loading a video player on the blog page.
Sample filename: `2014-02-15-watch-matthew-carter.md`.

```markdown
---
this_file: src_docs/md/posts/2014-02-15-watch-matthew-carter.md
title: "Watch the Matthew Carter webinar"
authors: [adam]
date:
  created: 2014-02-15
slug: watch-matthew-carter
---

FontLab's February 2014 webinar with Matthew Carter looks at how technical
constraints shape type design, from metal type to digital fonts.

<!-- more -->

[![Matthew Carter webinar recording](../media/matthew-carter-webinar.jpg)](https://www.youtube.com/watch?v=ibJhxbsbqJ4)

## What to listen for

- How a production constraint becomes a design decision.
- How Carter's working methods changed with the technology.
- What the transition to digital production made possible.

[Watch the recording →](https://www.youtube.com/watch?v=ibJhxbsbqJ4){ .fl-help-cta }
```

### Images, links and reusable body patterns

Upload local images to [`src_docs/md/media/`](src_docs/md/media/) before
publishing a post that refers to them. From a file in `posts/`, use
`../media/filename.png`, not `media/filename.png` or a path into generated
`docs/`. Existing posts also use full HTTPS image URLs, as in Example 3.
Give images descriptive alt text and include any required credit or source link.

```markdown
![Matthew Carter webinar thumbnail](../media/matthew-carter-webinar.jpg)

[Read the FontLab Pad 2 announcement](2026-09-17-fontlab-pad-2.md)

[Explore FontLab →](https://www.fontlab.com/font-editor/fontlab/){ .fl-help-cta }
```

Use `{ .illu-thumb .illu-front .illu-photo }` before `<!-- more -->` for an
index thumbnail. Add a separate image below the separator for the article.
Use `{ .off-glb }` to opt an image out of click-to-zoom. Add
`{ .fl-help-cta }` to a standalone next-step link.

For a compact comparison inside a tutorial or release post, use a table:

```markdown
| Task | Where to start |
|---|---|
| Try a font without installing it | FontLab Pad |
| Convert a variable instance into a static font | TransType |
| Draw and edit your own font | FontLab |
```

For a short sourced note, use a footnote. For interface labels, use bold; for
filenames and literal values, use backticks:

```markdown
Choose **File > Add Instance** to add a style, then export a static `.otf`
or `.ttf` font. This workflow is described in the TransType announcement.[^source]

[^source]: [TransType 5 announcement](2026-09-02-transtype-5.md).
```

### Before committing a post

- Replace every copied title, date, slug, path and product-specific detail.
- Check that the author key exists and YAML indentation uses spaces.
- Keep the summary above exactly one `<!-- more -->` separator.
- Upload new images and check their paths, alt text and credits.
- Check facts, links and any quoted statements; keep the next step clear.
- Preserve an existing post's creation date and slug when editing its wording.
- After publishing, check the Actions result, the index excerpt, the topic
  page and the full article on [blog.fontlab.com](https://blog.fontlab.com/).

Most posts can also be written through the web admin described below.

## Publishing & deploy

The hosting is deliberately simple but has three moving parts — know which is
which:

| Piece | What it is |
|---|---|
| **GitHub Pages source** | The `gh-pages` branch, served at `blog.fontlab.com` (a repo *setting*, not a file in the tree). |
| **`.github/workflows/ci.yml`** (`deploy`) | Runs `./build.sh build`, then publishes `docs/` → `gh-pages` via `peaceiris/actions-gh-pages` (orphan branch, writes the `CNAME`). |
| **`docs/`** | Build output. Still tracked on `main` but **vestigial** — it only seeds `docs/CNAME`, which `build.sh` preserves and CI's sanity-check requires. The *live* HTML comes from `gh-pages`, rebuilt by CI. |

**The deploy workflow runs on:**

- a push to **`main`** (the everyday path — including new posts written by the
  web admin, which commit a Markdown file to `main`),
- a `v*.*.*` **tag** push (what `publish.sh` / `gitnextver` create), and
- **manual dispatch**.

So the normal flow is: edit/add Markdown in `src_docs/md/` → push to `main` →
GitHub Actions builds and deploys to `gh-pages` → the live site updates after
the workflow and Pages deployment finish successfully.

> **History / gotcha:** Pages used to serve `main`'s `docs/` folder *directly*,
> and `ci.yml` only ran on tags. Because the web admin pushes only source
> Markdown (it never rebuilds `docs/`), posts landed in `src_docs/` but never
> appeared live. Switching Pages to `gh-pages` and adding the `main` trigger
> fixed it: a source push is now sufficient to publish.

### Force a redeploy

```bash
gh workflow run deploy --repo Fontlab/blog.fontlab.com --ref main
```

### Publishing through the web admin

Editors can write posts without a local checkout at
[api.fontlab.com/www-admin/?tab=blog](https://api.fontlab.com/www-admin/?tab=blog).
That form clones/pulls this repo on the server, writes the Markdown file to
`src_docs/md/posts/`, and commits + pushes it to `main` — which then triggers
the deploy workflow described above. The author dropdown is populated from this
repo's `src_docs/md/authors.yml`. See `api.fontlab.com`'s README for the admin
side.

## CLI subcommands

| Command | Description |
|---|---|
| `./build.sh build` | Flowmark-format `src_docs/md/`, clean `docs/` (preserving `CNAME`), then run ProperDocs build |
| `./build.sh format` | Run Flowmark on `src_docs/md/` with semantic breaks, smart quotes, ellipses, and safe cleanups |
| `./build.sh serve` | Run ProperDocs serve (live reload) at `:8000` |
| `./build.sh clean` | Remove `docs/` contents, preserve `CNAME` |
| `./publish.sh` | Build, sanity-check `docs/`, then run `uvx gitnextver` to commit, tag, and push; the tag triggers the deploy workflow |

The build/preview logic itself lives in the `blog-fontlab` package
(`src/blog_fontlab/cli.py`); `build.sh` is a thin `uv run blog-fontlab` wrapper.

## Layout

```
blog.fontlab.com/
├── build.sh               # CLI wrapper (delegates to uv run blog-fontlab)
├── publish.sh             # build + sanity-check + gitnextver tag/push
├── .github/workflows/
│   └── ci.yml             # "deploy": build → publish docs/ to gh-pages
├── docs/                  # build output → deployed to gh-pages (do not hand-edit)
│   └── CNAME              # blog.fontlab.com (seed preserved by build.sh)
├── mkdocs/
│   └── mkdocs.yml         # ProperDocs/MaterialX config and theme overrides
├── src_docs/
│   └── md/
│       ├── posts/         # one Markdown file per post (YYYY-MM-DD-slug.md)
│       └── authors.yml    # author/category definitions
├── src/
│   └── blog_fontlab/
│       ├── __init__.py
│       └── cli.py         # fire CLI: build / serve / clean / format
└── pyproject.toml
```

## The `reference/` directory

The `./reference/` directory is **gitignored** and contains various cloned
repositories and assets used as context, tooling, and source material.

- **Assets & Static Sites:**
  - `i.fontlab.com/docs/` — CDN with images/assets for FontLab apps.
  - `i.vexy.art/docs/` — CDN with images/assets for Vexy Lines.
  - `vexy-lines.static/` — Help site and images for Vexy Lines.
  - `flum-unified-database.static/` — Articles about FontLab.
- **Source Material (Read-only):**
  - `fontlab-com-oldpub/` — Old WordPress blog exports (2013-2023). Blog-style posts will be ported to the new site.
  - `FontLabVI-help/` — Ancient site for FontLab VI and 7.
- **Reference Sites (Writable):**
  - `fontlab-partners/` — Partners site (MkDocs + MaterialX, Tailwind CSS).
  - `fldoc/` — FontLab 8 help site (Older MkDocs). Needs modernization.
- **Python Tools (Writable, to be published):**
  - `twardown-*` — Various twardown packages to be published to PyPI/NPM.
  - `vexy-mkdocs-*`, `vexy-marktripy/`, `vexy-python-markdown-steroids/` — Plugins and tools being modernized for ProperDocs / Python 3.12+.
- **Python Tools (Read-only):**
  - `properdocs/` — Maintained fork of MkDocs.
  - `mkdocs-materialx/` — Maintained fork of MkDocs Material.
  - `pymdown-extensions/`, and various `mkdocs-*` plugins.

## License

MIT — Copyright 2026 Fontlab Ltd.

<!-- shared-theme-integration:start -->
## Shared FontLab theme integration

This repository is part of the FontLab theme 2026 rollout: fontlab blog.
[THEME.md](THEME.md) documents its source/output boundaries, configuration,
publication route, control ownership, shared visual changes and verification.
Use the [public setup guide](https://i.fontlab.com/fltheme26/) and
[MaterialX starter](https://i.fontlab.com/fltheme26/starter.zip) for new sites.
<!-- shared-theme-integration:end -->
