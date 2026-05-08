---
this_file: src_docs/md/posts/2026-01-27-cpal-and-css-font-palette.md
title: "A colour font is a black-and-white machine"
authors: [fontlab]
tags: [color-fonts, cpal, css, font-palette, web]
date:
  created: 2026-01-27
slug: cpal-and-css-font-palette
---
A colour font with one palette is a coloured drawing.
A colour font with thirty palettes is a theme system.
The difference is `CPAL`, and most people walk right past it.

<!-- more -->

`CPAL` — the Color Palette table — is the OpenType table that holds the colours a `COLR`
font uses. The architecture is straightforward: each palette is a list of sRGB colour
records, indexed from zero.
Palette 0 is the default.
Version 1 of `CPAL` can label palettes and mark them as appropriate for light or dark
backgrounds, so a renderer can pick the right one automatically.

One index is reserved: `0xFFFF` means “the foreground colour” — whatever `color` the CSS
or application context has set.
That single convention is quietly load-bearing.
Any glyph layer assigned `0xFFFF` will follow the text colour into dark mode, into a
coloured heading, into a print stylesheet with black-on-white.
The parts that should look like text *do* look like text, without extra CSS.

On the web side, CSS caught up properly with `@font-palette-values`. The rule lets a
page override palette entries or compose an entirely new palette for a family, without
touching the font file:

```css
@font-palette-values --night {
  font-family: "Bradley Initials";
  base-palette: 2;
  override-colors: 0 #f0c, 1 #14213d;
}
.heading { font-palette: --night; }
```

WebKit’s “Customizing Color Fonts on the Web” demo, built on DJR’s Bradley Initials,
remains the cleanest live example of what this makes possible: a single font file, half
a dozen radically different looks, no export step.

Underware’s Plakato Color Grade pushes the concept as far as it currently goes: the font
ships **1,360 palette entries** in `CPAL`. Not thirty palettes — 1,360 individual colour
records across a large palette library.
Swap a palette and the entire feel of the font changes.
The outlines never move.

The mental shift worth making is this: a colour font is not a coloured drawing.
It is a black-and-white machine that gets coloured in by CSS. The outlines are the
machine. The palettes are the paint.
Once you see it that way, the design problem becomes “what palettes ship by default” —
the same problem every stylesheet has always had, just with a font table attached.

Safari can select and override `CPAL` palettes via CSS `font-palette` and
`@font-palette-values` even while it does not yet render `COLRv1` glyph colour.
Those are different layers of the stack.
The CSS theming surface is broadly supported; the glyph rendering varies by browser.
Test both, separately.

## References

- [Customizing color fonts on the web — WebKit blog](https://webkit.org/blog/12662/customizing-color-fonts-on-the-web/)
- [OpenType CPAL table — Microsoft](https://learn.microsoft.com/en-us/typography/opentype/spec/cpal)
- [Bradley Initials colour demo — DJR](https://tools.djr.com/misc/bradley-initials/)
- [Plakato Color Grade — Underware](https://underware.nl/fonts/plakato/features/color/)
- [CSS font-palette — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/font-palette)

[Read more →](https://www.fontlab.com/font-editor/fontlab/){ .fl-help-cta }
