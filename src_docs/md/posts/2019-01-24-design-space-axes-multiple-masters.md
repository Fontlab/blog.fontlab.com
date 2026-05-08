---
this_file: src_docs/md/posts/2019-01-24-design-space-axes-multiple-masters.md
title: "Design space axes and multiple masters in FontLab VI"
authors: [fontlab]
date:
  created: 2019-01-24
slug: design-space-axes-multiple-masters
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab/7/manual/Variable-Fonts/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "Video runtime four minutes — verify against YouTube"
    - "FontLab VI design space panel described — verify UI still matches FontLab 7/8"
  image_status: present
  image_needs: "Thumbnail present (fontlabtv-AijDkf3DBk8.jpg) — adequate"
  weakness_verdict: keep
  consolidate_with: "2021-05-27-make-variable-fonts-better-fontlab-7.md"
  notes: "Concise and well-paced; the 'abstract made concrete' paragraph earns its place. The post covers FontLab VI but the feature carries forward — a one-line note pointing to current docs would extend its shelf life. Good cross-link candidate with the ATypI variable fonts quality talk."
---
![](../media/illu/design-space-axes-multiple-masters-1.png){.illu-thumb .illu-index}

Variable fonts force you to think in multiple dimensions at once. This four-minute video shows exactly how to set up a design space with axes and masters in FontLab VI. It gives you a concise, visual introduction to the core concepts behind variable font production.

<!-- more -->

[![Design Space Axes and Multiple Masters](../media/fontlabtv-AijDkf3DBk8.jpg)](https://www.youtube.com/watch?v=AijDkf3DBk8)

A variable font isn’t a single design. It is a continuous space of designs. You define the extremes as separate masters, and the font interpolates smoothly between them at runtime. The design space is the conceptual model that holds all of this together.

Common extremes include:
* **Weight:** Light and bold.
* **Width:** Condensed and wide.
* **Slant:** Upright and italic.

FontLab VI’s design space panel lets you define axes, place masters at coordinates within that space, and immediately preview interpolated instances without exporting. You can use standard axes like Weight, Width, and Optical Size, or create custom axes of your own. This video walks through setting up a design space with two axes, adding masters, and checking that interpolation is compatible across glyphs.

What makes this video useful beyond the mechanics is how it makes the abstract concrete. Seeing the masters laid out on a grid turns a mathematical concept into something visual and tactile. A draggable instance point moves through the space to show you exactly what happens between your masters. Variable font design in FontLab starts here.

Watch on [FontLab TV](https://www.youtube.com/watch?v=AijDkf3DBk8).

[Read more →](https://help.fontlab.com/fontlab/7/manual/Variable-Fonts/){ .fl-help-cta }
