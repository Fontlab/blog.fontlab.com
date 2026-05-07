---
this_file: src_docs/md/posts/2025-05-13-variable-fonts-were-never-about-file-size.md
title: "Variable fonts were never about file size"
authors: [fontlab]
tags: [variable-fonts, design, fontlab-8, opentype, hierarchy]
date:
  created: 2025-05-13
slug: variable-fonts-were-never-about-file-size
---
The marketing for variable fonts has spent a decade promising smaller downloads.
The smaller downloads are real.
They are also the least interesting thing about the format.

<!-- more -->

<!-- image TBD -->

A variable font compresses an entire family into one file by storing a default master
and a set of mathematical instructions for deforming it along continuous axes.
Yes, that is fewer HTTP requests.
Yes, the page weight drops.
The Google Fonts and web.dev articles have repeated this for years and they are correct.

The interesting part is what continuous control does to design itself.
A static family forces the typesetter to choose between Regular and Bold, with nothing
in between. A variable family lets the typesetter pick 525 — between Medium and Semibold
— because that is the weight the column actually wants.
UI teams use this for hierarchy.
Editorial teams use it for colour balance on a tight page.
Motion designers use it because the same axis that controls weight in CSS controls the
keyframe in After Effects.

Underware’s argument from 2018 still holds: variable fonts get interesting when you stop
treating old categories as sacred.
Time can be an axis.
Motion can be an axis.
The interface can become part of the typeface experience.
A weight slider is the start, not the destination.

FontLab 8 sits behind a lot of this work because it treats the variation space as a
primary unit. Open a Light and a Black as masters; the engine establishes the axis
automatically. Add an intermediate master at 700 if linear interpolation muddies the
middle. Tag a single-storey `g` to swap in past 850 weight via the `rvrn` feature.
Export, ship one file, give the typesetter the whole continuum.

The savings on bandwidth are nice.
The control is the point.

## References

- [Very-able fonts — Underware](https://www.underware.nl/blog/2018/06/very-able-fonts-com/)
- [Thinking beyond the static — Type Network](https://typenetwork.com/articles/thinking-beyond-the-static)
- [Variable fonts on the web — web.dev](https://web.dev/articles/variable-fonts)
- [Families and variation in FontLab 8](https://help.fontlab.com/fontlab/8/manual/Variations/fontlab/8/whats-new/whats-new-07-families-variation/)

[Read more on help.fontlab.com →](https://help.fontlab.com/fontlab/8/manual/Variations/){ .fl-help-cta }
