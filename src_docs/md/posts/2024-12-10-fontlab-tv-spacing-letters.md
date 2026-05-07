---
this_file: src_docs/md/posts/2024-12-10-fontlab-tv-spacing-letters.md
title: "FontLab TV: spacing letters from scratch"
authors: [fontlab]
tags: [spacing, sidebearings, metrics, tutorial]
date:
  created: 2024-12-10
slug: fontlab-tv-spacing-letters
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab/8/tutorials/calfonts/3.%20Fitting%20and%20Spacing/3a-0%20Intro%20to%20Spacing/"
  title_case: ok
  title_suggested: ""
  voice_quality: adequate
  facts_to_verify:
    - "Spacing manual CTA URL is live"
    - "FontLab TV spacing episode URL — confirm actual episode URL at fontlab.tv"
    - "Spacing string 'nnHnoHonn' — verify this is the string Dave Lawrence recommends"
  image_status: missing
  image_needs: "FontLab TV spacing episode thumbnail or metrics window screenshot"
  weakness_verdict: keep
  consolidate_with: "2024-07-09-white-space-does-the-real-drawing.md"
  notes: "Useful companion to the white-space editorial post but thin on its own. CTA URL is now fixed."
---
Spacing is what separates a font that exists from a font that reads.
The FontLab TV spacing episode is the one to watch first — before kerning, before
OpenType, before anything else that can mask bad sidebearings.

<!-- more -->

> 📺 Watch: [Spacing letters on FontLab TV](https://fontlab.tv/)

## What it covers

**The spacing string.** Start with a controlled context — `nnHnoHonn`, `HHOHO`, `nono` —
not a sentence. The episode shows why “Hamburgevons” is not enough and what to look for
in a real spacing string.

**Sidebearings, not pairs.** Every spacing problem you can solve with sidebearings, you
should. Kerning is for the pairs that nothing else can fix.
The video walks through setting `n`, `o`, `H`, `O` first, then deriving the rest of the
lowercase and uppercase from those four anchors.

**Round, flat, diagonal, open.** Most letters fall into a small number of side-shape
categories. Once you know what `o` does, you know roughly what every round letter does.
Once `H` is set, every flat-sided letter follows.
The episode shows the bucketing in practice.

**Metric classes.** FontLab lets you link sidebearings across glyphs so that one
adjustment to `n` propagates to `m`, `h`, `u`, and so on.
The video shows how to set these up and when to break them deliberately.

## Why it matters

Bad spacing is the single most common reason a technically competent font feels off.
This episode is the cheapest hour you will spend improving every font you make from now
on.

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/calfonts/3.%20Fitting%20and%20Spacing/3a-0%20Intro%20to%20Spacing/){ .fl-help-cta }
