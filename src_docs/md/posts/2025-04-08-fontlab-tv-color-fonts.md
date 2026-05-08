---
this_file: src_docs/md/posts/2025-04-08-fontlab-tv-color-fonts.md
title: "FontLab TV: color fonts without tears"
authors: [fontlab]
tags: [color-fonts, opentype, cpal, colr, svg, tutorial]
date:
  created: 2025-04-08
slug: fontlab-tv-color-fonts
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab/8/manual/"
  title_case: ok
  title_suggested: ""
  voice_quality: adequate
  facts_to_verify:
    - "FontLab TV color fonts episode URL — confirm actual episode at fontlab.tv"
    - "COLR v1 support status — verify browser/OS support as of 2026"
    - "CBDT/sbix — verify Apple still uses sbix for emoji (not COLR)"
    - "CTA should deep-link to color fonts section"
  image_status: present
  image_needs: ""
  weakness_verdict: keep
  consolidate_with: "2025-07-22-the-long-awkward-adolescence-of-color-fonts.md"
  notes: "Good four-format overview but thin; pairs with the color history post; FontLab TV link goes to homepage not episode."
---
![](../media/illu/fontlab-tv-color-fonts-2.png){.illu-thumb }

Color fonts have stopped being a novelty and started being a deliverable — emoji, branded display faces, multi-layered display work. The FontLab TV color font episode covers the four formats you actually have to think about and which to ship for which target.

<!-- more -->

> 📺 Watch: [Color fonts: the next big thing? on FontLab TV](https://www.youtube.com/watch?v=Yit1ZpClwAk)

## What it covers

**The four formats.**

- **OpenType+COLR v0** — layered solid-color glyphs. Tiny file size, broad support. The default for branded display work. (What’s not covered is **COLR v1**: gradients, transforms, paint graphs. The new hotness. Increasing browser and OS support.)
- **OpenType+SVG** — full SVG glyphs. Maximum flexibility, larger files.
- **OpenType+sbix** and **OpenType+CBDT** — bitmap glyph tables. Used by Apple emoji and similar.

**The episode walks through which to use when.** Layered (COLR v0) is the safe default. COLR v1 and SVG when you need gradients (COLR v1 works in Chrome-based browsers, SVG works in Safari, Firefox, in macOS and in Adobe apps).

**Drawing layered glyphs.** FontLab handles the layered approach via element-based glyph composition: each color in the final glyph is a separate element with its own fill. The video shows the workflow for building, previewing, and exporting.

**CPAL palettes.** A single font can carry multiple palettes, and renderers can switch between them. Useful for dark/light mode display fonts and for shipping brand variants in one binary.

**Export.** FontLab exports to all four formats from the same source. The episode shows the export dialog flags and how to verify the output in a browser and in modern OS rendering.

## Why it matters

Color fonts are now production-grade for display, branding, and app-icon contexts — not just emoji. This episode is the fastest way from “I have a layered illustration” to “I have a working color OpenType that ships.”

[Read more →](https://help.fontlab.com/fontlab/8/manual/){ .fl-help-cta }
