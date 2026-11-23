---
this_file: THEME.md
---

# Theme: blog.fontlab.com

## FontLab blog

The site uses the installable **fly-january** theme (ProperDocs theme extending MaterialX)
and its `fly` plugin. The MaterialX blog plugin remains responsible for post routing,
archives, topic pages, pagination, feeds and search.

| Configuration | Role | Destination |
|---|---|---|
| `mkdocs/mkdocs.yml` | active publication configuration | https://blog.fontlab.com/ |

## What lives where

- `theme.name: fly-january`, `plugins: [..., fly]`, `extra.fly` in `mkdocs/mkdocs.yml`:
  `chrome: fontlab` renders `<fontlab-menu>` (site-label "Blog", search-from "blog",
  MaterialX drawer and search) and `<fontlab-footer>`; `fonts` loads Outfit and sets the
  type roles (Outfit headings, system sans text, `sans` role for links, italic `em`). No hue: H1 stays ink.
- `mkdocs/mk-fontlab/` (custom_dir) holds only what the theme lacks. Never add a
  `main.html` there: it would replace the theme's own and drop its CSS and JS.
  - `blog.html`: MaterialX blog index template plus the homepage hero.
  - `partials/post.html`: excerpt layout (avatar, inline date and read time).
  - `partials/footer.html`: the FontLab CTA band (the blog shows no MaterialX footer).
- `mkdocs/hooks/site_head.py`: Google Tag Manager and JSON Feed links (no template slot).
- `mkdocs/hooks/glightbox_small_images.py`: keeps small images out of the lightbox.
- `src_docs/md/css/extra.css`: blog content styling. rem values are against the theme's
  14.4px root. Component links are styled as `.md-typeset .class` (no `!important`).
- Plugins use bare names (`search`, `blog`, `tags`).
- `mkdocs/hooks/plain_links.py`: adds `data-fly-plain` to `.fl-help-cta` links so the
  theme's article-link rule leaves the CTA component alone.
- Tailwind Play CDN + `js/tailwind-config.js` serve the unprefixed utility classes used
  in posts (`extra.fly.utilities` stays off: posts do not use `tw:` classes).

## Build

`./build.sh build` (or `uv run properdocs build -f mkdocs/mkdocs.yml`). Python 3.13 via
uv; engine pins in `pyproject.toml`: properdocs 1.6.7, mkdocs 1.6.1, mkdocs-materialx
10.1.8, pymdown-extensions 11.0.1. fly-january is an editable path source until it is
published on PyPI; until then CI cannot build this configuration.

## Verification

Check desktop and mobile, light and dark: index, `/page/2/`, an archive and a topic
page, posts with images, code and tables; menu search, mobile drawer, lightbox, footer.
