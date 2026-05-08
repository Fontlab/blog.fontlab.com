---
this_file: src_docs/md/posts/2025-06-24-fontlab-tv-design-space.md
title: "FontLab TV: design space basics"
authors: [fontlab]
tags: [design-space, masters, axes, variable-fonts, tutorial]
date:
  created: 2025-06-24
slug: fontlab-tv-design-space
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab/8/manual/"
  title_case: ok
  title_suggested: ""
  voice_quality: adequate
  facts_to_verify:
    - "FontLab TV design space episode URL — confirm actual episode at fontlab.tv"
    - "rclt and rvrn features for conditional substitution — verify both tags are correct"
    - "STAT table setup for OS/app font menu naming — verify this is covered in the episode"
    - "Custom axis examples XHGT, YOPQ — verify these are real registered axis tags"
  image_status: present
  image_needs: ""
  weakness_verdict: keep
  consolidate_with: ""
  notes: "Canonical conceptual intro to design space; absorbed the unique parts of 2025-03-25-designing-variable-axes-well.md."
---
![](../media/illu/fontlab-tv-design-space-1.png){.illu-thumb}

Design space is the part of variable font work that decides whether your font feels good
or merely works. The FontLab TV design space episode is the conceptual foundation for
everything you do with masters, axes, and instances.

<!-- more -->

![FontLab TV](../media/fontlab-tv1.png)

![FontLab TV: design space tutorial](../media/fontlab-tv2.png)

> 📺 Watch:
> [Design space axes & multiple masters on FontLab TV](https://www.youtube.com/watch?v=AijDkf3DBk8)

## What it covers

**The space, not the masters.** A design space is a coordinate system.
Masters are points in it.
Instances — what users see when they pick “Bold” or set a slider — are coordinates in
that same space. Once you think this way, axis design starts to feel like a normal
modeling problem.

**Choosing axes.** The five registered axes (Weight, Width, Italic, Slant, Optical Size)
cover most cases, but custom axes solve things the registered ones cannot — `XHGT` for
x-height, `YOPQ` for stroke contrast, the kind of thing the variable-font spec was
designed to make extensible.

**Master placement.** Masters at the corners of the space define the linear
interpolation. The episode shows when corners are enough and when you need an interior
master to control a specific instance — for instance to keep the Bold from being
mathematically the average of Light and Black.

**Instance design.** Named instances (`Light`, `Regular`, `Bold`, `Black`) are
coordinates plus a name table entry.
The video shows how to set up the STAT table so that operating systems and apps name
your instances correctly in font menus.

**Axis ranges and conditional substitution.** A late-episode topic worth knowing about:
the `rclt` and `rvrn` features let you substitute one glyph for another when the design
space crosses a threshold.
Useful for letterforms that need to change shape at certain weights.

## Why it matters

Most variable font problems are design space problems.
This episode is the framing that lets you debug VF behaviour by drawing diagrams instead
of guessing.

[Read more →](https://help.fontlab.com/fontlab/8/manual/){ .fl-help-cta }
