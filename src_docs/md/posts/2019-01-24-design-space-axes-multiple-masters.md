---
this_file: src_docs/md/posts/2019-01-24-design-space-axes-multiple-masters.md
title: "Design space axes and multiple masters in FontLab VI"
authors: [fontlab]
date:
  created: 2019-01-24
slug: design-space-axes-multiple-masters
---
Variable fonts require thinking in multiple dimensions at once — and this four-minute
video from FontLab VI shows exactly how to set up a design space with axes and masters.
It is a concise, visual introduction to the core concept behind variable font
production.

<!-- more -->

[![Design Space Axes and Multiple Masters](../media/fontlabtv-AijDkf3DBk8.jpg)](https://www.youtube.com/watch?v=AijDkf3DBk8)

A variable font is not a single design but a continuous space of designs.
You define the extremes — light and bold, condensed and wide, upright and italic — as
separate masters, and the font interpolates smoothly between them at runtime.
The design space is the conceptual model that holds all of this together.

FontLab VI’s design space panel lets you define axes (Weight, Width, Optical Size, or
custom axes of your own), place masters at coordinates within that space, and
immediately preview interpolated instances without exporting.
This video walks through setting up a two-axis design space, adding masters, and
checking that interpolation is compatible across glyphs.

What makes this video useful beyond the mechanics is the way it makes the abstract
concrete. Seeing the masters laid out on a grid, with a draggable instance point moving
through the space, turns a concept that can feel mathematical into something visual and
tactile. Variable font design in FontLab starts here.

Watch on [FontLab TV](https://www.youtube.com/watch?v=AijDkf3DBk8).
