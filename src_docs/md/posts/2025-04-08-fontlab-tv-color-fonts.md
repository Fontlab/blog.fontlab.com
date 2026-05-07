---
this_file: src_docs/md/posts/2025-04-08-fontlab-tv-color-fonts.md
title: "FontLab TV: color fonts without tears"
authors: [fontlab]
tags: [color-fonts, opentype, cpal, colr, svg, tutorial]
date:
  created: 2025-04-08
slug: fontlab-tv-color-fonts
---
Color fonts have stopped being a novelty and started being a deliverable — emoji,
branded display faces, multi-layered display work.
The FontLab TV color font episode covers the four formats you actually have to think
about and which to ship for which target.

<!-- more -->

> 📺 Watch: [Color fonts on FontLab TV](https://fontlab.tv/)

## What it covers

**The four formats.**

- **COLR/CPAL v0** — layered solid-color glyphs.
  Tiny file size, broad support.
  The default for branded display work.
- **COLR v1** — gradients, transforms, paint graphs.
  The new hotness. Increasing browser and OS support.
- **SVG-in-OpenType** — full SVG glyphs.
  Maximum flexibility, larger files.
- **CBDT/sbix** — bitmap glyph tables.
  Used by Apple emoji and similar.

**The episode walks through which to use when.** Layered (COLR v0) is the safe default.
SVG when you need raster effects or photographic content.
COLR v1 when you can require modern renderers.

**Drawing layered glyphs.** FontLab handles the layered approach via element-based glyph
composition: each color in the final glyph is a separate element with its own fill.
The video shows the workflow for building, previewing, and exporting.

**CPAL palettes.** A single font can carry multiple palettes, and renderers can switch
between them.
Useful for dark/light mode display fonts and for shipping brand variants in
one binary.

**Export.** FontLab exports to all four formats from the same source.
The episode shows the export dialog flags and how to verify the output in a browser and
in modern OS rendering.

## Why it matters

Color fonts are now production-grade for display, branding, and app-icon contexts — not
just emoji. This episode is the fastest way from “I have a layered illustration” to “I
have a working color OTF that ships.”

[Read more on help.fontlab.com →](https://help.fontlab.com/fontlab/8/manual/){
.fl-help-cta }
