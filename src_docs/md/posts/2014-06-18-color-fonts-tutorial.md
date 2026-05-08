---
this_file: src_docs/md/posts/2014-06-18-color-fonts-tutorial.md
title: "Color fonts: the next big thing? A FontLab tutorial"
authors: [fontlab]
date:
  created: 2014-06-18
slug: color-fonts-tutorial
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-8-color/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "Tutorial runtime is 103 minutes — verify against YouTube"
    - "Four color font formats listed: sbix, COLR/CPAL, SVG-in-OpenType, OpenType-SVG — verify distinctions were accurate in 2014"
    - "COLRv1 eventually won format war — verify this framing is accurate"
  image_status: present
  image_needs: "Thumbnail present (fontlabtv-Yit1ZpClwAk.jpg) — adequate for a tutorial embed"
  weakness_verdict: keep
  consolidate_with: "2013-09-19 and 2013-10-10 and 2013-11-07 color font series if those exist in this blog"
  notes: "Strong opener and good historical framing. The 'watching it now' retrospective angle is the post's best hook — lean into it harder. Image thumbnail present and relevant."
---
![](../media/illu/color-fonts-tutorial-3.png){.illu-thumb}

Back in 2014, color fonts were a brand new frontier.
This 103-minute tutorial with Adam Twardoch was one of the first deep dives into how to
actually make them.
It covers technical standards, font editor workflows, and the promise
of full-color type right when emoji and display typography were pushing the format into
the mainstream.

<!-- more -->

Traditional fonts render in a single color chosen by the app.
Color fonts break that rule.
They embed layered outlines, bitmaps, or SVG artwork directly in the font file.
This lets a single glyph display multiple colors, gradients, or photographic detail.

[![Color fonts: the next big thing?](../media/fontlabtv-Yit1ZpClwAk.jpg)](https://www.youtube.com/watch?v=Yit1ZpClwAk)

This tutorial walks through the color font formats available at the time:

* **Apple’s `sbix`**
* **Microsoft’s `COLR`/`CPAL`**
* **Google and Mozilla’s SVG-in-OpenType**
* **Adobe and Mozilla’s OpenType-SVG**

It explains how browsers and operating systems supported them.
You’ll also see a demonstration of building color glyphs inside FontLab Studio.
Adam covers fallback outlines for older environments, file size trade-offs, and the
tooling landscape of the era.

Watching it now serves as a great historical document.
Many of the format conflicts described here eventually resolved in favor of
`COLR`/`CPAL` and later COLRv1. Tooling has matured a lot since then.
But the design thinking behind color glyph construction remains directly relevant today.

Watch the full video on [FontLab TV](https://www.youtube.com/watch?v=Yit1ZpClwAk).

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-8-color/){ .fl-help-cta }
