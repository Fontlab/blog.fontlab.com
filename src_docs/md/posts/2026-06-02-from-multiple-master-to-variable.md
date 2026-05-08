---
this_file: src_docs/md/posts/2026-06-02-from-multiple-master-to-variable.md
title: "From Multiple Master to OpenType variable fonts"
authors: [fontlab]
tags: [variable-fonts, multiple-master, history, fontlab-8]
date:
  created: 2026-06-02
slug: from-multiple-master-to-variable
---
Variable fonts are not new.
They are the third attempt at the same idea, by mostly the same engineers, after
twenty-five years of finding out what didn't work.

<!-- more -->

Adobe announced **Multiple Master** in 1991.
Myriad MM had four masters — light/black × condensed/extended — and let you interpolate
any instance in between.
Minion MM added an optical-size axis, Caption to Display.
It was, technically, beautiful.

Commercially it died slowly.
Tamye Riggs's *Adobe Originals Silver Anniversary* essay puts it best: users had to
generate a separate instance for every variation they wanted to use, resulting in hard
drives full of files named things like `MinioMM_578 BD 465 CN 11 OP`.
The last MM release was 1999.

Apple shipped its own answer the same year, inside QuickDraw GX: **TrueType GX
Variations**.
Same idea, different table layout.
It worked.
It also lost, mostly because GX as a whole lost.
When an operating system dies, it takes its font format with it.

Then nothing, for sixteen years.

Then ATypI Warsaw, September 2016: Adobe, Apple, Google, and Microsoft stood on the same
stage and announced OpenType 1.8 with variations support.
The mechanism is essentially TrueType GX with the lessons of Multiple Master applied —
continuous interpolation, standard axis tags, named instances that don't require
generating static files.

FontLab Ltd was inside the working group pushing for it, and shipped support in
FontLab VI when the spec landed.
David Lemon was at Adobe through both eras.
The continuity is unusual.
Most format wars don't have the same people on both ends.

The reason Multiple Master failed wasn't the technology.
It was the workflow: too many files, too many names, too much manual work to get from
"this font varies" to "I can use this font."
OpenType variables solved that.
The variation is in the file.
The instance names are in `fvar`.
Nothing lives on the hard drive that didn't need to be generated.

FontLab 8 inherits a direct line from that Warsaw announcement.
The axes you define, the masters you draw, the designspace you set up — it's the same
idea Myriad MM was, made fit to use.

## References

- [The Adobe Originals Silver Anniversary — Typekit blog](https://blog.typekit.com/2014/07/30/the-adobe-originals-silver-anniversary-story-how-the-originals-endured-in-an-ever-changing-industry/)
- [Multiple master fonts — Wikipedia](https://en.wikipedia.org/wiki/Multiple_master_fonts)
- [TrueType GX — Wikipedia](https://en.wikipedia.org/wiki/TrueType_GX)

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-7-variable/){ .fl-help-cta }
