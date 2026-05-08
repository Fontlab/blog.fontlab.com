---
this_file: src_docs/md/posts/2014-12-15-otmaster-5-vfb2ufo-fontlab-pad-11.md
title: DTL OTMaster 5.0, vfb2ufo, and FontLab Pad 1.1
authors: [fontlab-pad]
date:
  created: 2014-12-15
slug: otmaster-5-vfb2ufo-fontlab-pad-11
review:
  cta_status: ok
  cta_target: "https://www.fontlab.com/font-utility/dtl-otmaster/"
  title_case: ok
  title_suggested: ""
  voice_quality: adequate
  facts_to_verify:
    - "OTMaster 5.0 described as 'massive upgrade from 4.x' — verify what 4.x lacked"
    - "vfb2ufo described as two-way conversion — verify it converted both VFB→UFO and UFO→VFB"
    - "FontLab Pad 1.1 ran on Mac OS X and Windows — verify platform support"
  image_status: present
  image_needs: "Replaced generic FontLab 8 placeholder with an existing OTMaster hero screenshot."
  weakness_verdict: keep
  consolidate_with: "2018-11-22-dtl-otmaster-7-9-available.md"
  notes: "Three unrelated tools crammed into one post — a common 'December release dump' pattern. Worth splitting or consolidating each tool thread across its own posts. The vfb2ufo bullet is genuinely useful context for UFO-workflow readers."
---
![](../media/illu/otmaster-5-vfb2ufo-fontlab-pad-11-3.png){.illu-thumb}

December 2014 brought a major update to DTL OTMaster, plus two new free tools.
We released a command-line UFO converter and an updated color font typesetter.

<!-- more -->

![DTL OTMaster interface](../media/otm-hero6-e1629877211343-1024x576.png)

Here is what shipped in this release:

* **DTL OTMaster 5.0**: A technical OpenType font editor from the Dutch Type Library.
  It gives you low-level access to the binary structure of OpenType fonts.
  You can edit tables, records, and individual fields directly.
  This skips the visual design interface entirely.
  Version 5.0 marked a massive upgrade from the 4.x series.
* **vfb2ufo**: A free command-line tool for two-way conversion.
  It translates between VFB (FontLab Studio’s native binary format) and UFO (Unified
  Font Object, the open XML-based interchange format).
  This gives FontLab Studio users a direct path to UFO-based workflows.
  You don’t need to open the GUI to convert files.
* **FontLab Pad 1.1**: A free app for Mac OS X and Windows.
  It lets you set text in color fonts.
  You can use bitmap color, SVG color, and layered color OpenType formats.
  The app renders the results correctly, something most operating systems and apps
  couldn’t do back then.
  Version 1.1 brought updates to both Mac and Windows builds.

[Read more →](https://www.fontlab.com/font-utility/dtl-otmaster/){ .fl-help-cta }
