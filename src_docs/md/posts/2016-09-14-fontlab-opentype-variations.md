---
this_file: src_docs/md/posts/2016-09-14-fontlab-opentype-variations.md
title: "FontLab's plans for OpenType 1.8 variable fonts"
authors: [fontlab]
date:
  created: 2016-09-14
slug: fontlab-opentype-variations
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab-vi/Release-Notes/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "OpenType 1.8 with variable fonts unveiled at ATypI Warsaw, September 2016, jointly by Google, Microsoft, Apple, and Adobe — verify date and parties"
    - "Variable fonts are an evolution of Apple's 1990s GX Variations and a superset of Adobe Multiple Master — verify framing"
    - "FontLab VI Public Preview builds already shipped a Variations panel (build 6101) — verify build number"
  image_status: missing
  image_needs: "Screenshot of the early FontLab VI Variations panel (the prototype from build 6101 referenced in the original post)"
  weakness_verdict: keep
  consolidate_with: ""
  notes: "Vision/tech post tied to the OpenType 1.8 announcement. Stripped event-week urgency (the Comm Arts article and WebVisions talk plug) but kept the technical substance: multiple-master heritage, masters anywhere in the design space, multiple axes. Original by Thomas Phinney."
---
At the ATypI conference in Warsaw, Google, Microsoft, Apple, and Adobe jointly unveiled version 1.8 of the OpenType specification — and with it, variable fonts.

<!-- more -->

Variable fonts, also called OpenType Variations, extend and update the GX Variations technology Apple invented in the 1990s. They are a functional superset of Adobe’s Multiple Master fonts: a single file can carry several axes of variation — weight, width, optical size, or anything a designer chooses to define.

The appeal is twofold. Users get more freedom — a continuous range of styles rather than a handful of fixed weights — and font families ship as smaller files, because the variation data is shared instead of duplicated across every instance. Crucially, the interpolation is done with real typographic finesse. This is not artificial stretching or algorithmic distortion; the designer controls how each axis behaves.

FontLab had already begun integrating variable-font support into FontLab VI before the announcement. Sharp-eyed users of the recent Public Preview builds will have spotted a Variations panel, which exposes some of the flexibility variable fonts allow but Multiple Master did not — masters placed at any point in the design space, and the option of many more design axes. FontLab VI will ship with OpenType Variations support, and the work will continue afterward across FontLab products.

There is a long thread here. FontLab was the first font editor to give designers a full visual environment for Multiple Master, and the idea of folding GX-style variations into OpenType has been kicked around at FontLab for years. Seeing the four major platform owners agree on a shared specification is the part that makes it real.

[Read more →](https://help.fontlab.com/fontlab-vi/Release-Notes/){ .fl-help-cta }
