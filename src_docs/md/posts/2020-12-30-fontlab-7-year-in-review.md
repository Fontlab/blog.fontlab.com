---
this_file: src_docs/md/posts/2020-12-30-fontlab-7-year-in-review.md
date:
  created: 2020-12-30
title: "FontLab 7: a year in updates"
authors: [fontlab]
draft: false
slug: fontlab-7-year-in-review
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "Six named releases from 7.0 to 7.2: 7.0.1, 7.1, 7.1.1, 7.1.2, 7.1.3, 7.1.4 — verify list is complete"
    - "30× faster interpolation described as arriving in 7.2.0 beta builds during late 2020 — verify"
    - "Glyphs.app interchange improved — verify specific version of Glyphs supported"
  image_status: present
  image_needs: ""
  weakness_verdict: keep
  consolidate_with: "2020-03-02-fontlab-71.md"
  notes: "Good thematic grouping of 2020 updates — drawing, metrics, variation, files. The cross-link to the 7.2 post is well-placed. Could be stronger with one concrete 'before/after' example per theme rather than a list of feature names. Inline help.fontlab.com link satisfies CTA."
---
![](../media/illu/fontlab-7-year-in-review-1.png){.illu-thumb}

FontLab 7 launched in December 2019 with over 250 new features.
Twelve months later, it has rather more than that.
Here is what the 2020 update cycle actually delivered — not counting FontLab 7.2, which
has [its own post](2020-11-30-fontlab-72-dec-2020.md).

<!-- more -->

The journey from 7.0 to 7.2 ran through six named releases (7.0.1, 7.1, 7.1.1, 7.1.2,
7.1.3, 7.1.4), all free for existing users.
The highlights, grouped by theme:

**Drawing and editing**

- **Ink traps and looped corners** — the Scissors tool gained the ability to add simple
  ink traps in one click; a new looped corner component type lets you design decorative
  corner terminals as reusable Smart Corners.
- **Harmonize Handles** — a new node type that produces G3-continuous (ultra-smooth)
  curves, useful wherever two curve segments must blend without a visible inflection.
- **Knife improvements** — duplicate a node by clicking with the Knife, or view the cut
  angle before committing.
- **High-precision dragging** — hold Cmd/Ctrl to nudge nodes and handles in tiny
  increments without zooming in; applies to non-node segment editing as well.

**Metrics and measurement**

- **Quick measurement** — the live stem-thickness tool (showing distance between
  opposing paths as a rainbow gradient) became smarter: it picks the closest distance
  automatically as you move the pointer, and respects italic angle with Shift+Ctrl.
- **Diagonal handle length display** — see the length of any handle or line segment as
  you draw or adjust it.
- **Link sidebearing to opposite** — one click to make left and right sidebearings
  mirror each other, updating live.

**Variation and masters**

- **Add variation easily** — 7.1.4 introduced a workflow for adding a master or axis to
  an existing single-master font without restructuring the file by hand.
- **Multi-master preview** — the Preview panel can display several masters
  simultaneously as overlaid wireframes, making interpolation problems visible without
  switching masters.
- **30× faster interpolation** (arriving in 7.2.0 beta builds during late 2020) — large
  variable font projects that previously took seconds to preview became near-instant.

**Files and interoperability**

- **Glyphs.app interchange** — improved `.glyphs` import and a new dedicated export
  path, making it easier to move work between FontLab and Glyphs.
- **UFO and VFM** — expanded metrics and kerning import from VFM, plus fixes to UFO
  export for folders with unusual characters in their paths.
- **Microsoft VOLT** — 7.1.4 added export of OpenType features directly to VOLT format
  for complex-script font engineering.

All of these shipped as free updates.
If you have FontLab 7 and have not updated recently, grab the latest build from the
[FontLab product page](https://www.fontlab.com/font-editor/fontlab/). Full documentation
starts at the [FontLab Help Center](https://help.fontlab.com/).

[Read more →](https://help.fontlab.com/){ .fl-help-cta }
