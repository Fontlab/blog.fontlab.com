---
this_file: issues/draft-posts/2025-12-09-vexy-lines-signal-and-halftone.md
title: "Vexy Lines: signal processing meets the joy of halftone"
authors: [vexy-lines]
tags: [vexy-lines, signal-processing, halftone, vector, screen-printing]
date:
  created: 2025-12-09
slug: vexy-lines-signal-and-halftone
draft: true
---
The boundary between a letterform and an illustration is a human invention.
To a computer, both are coordinates plotted on a grid.
Vexy Lines, released in December 2025, leans hard into that observation.

<!-- more -->

![Vexy Lines hero](/media/vexy-hello-hero.png)

## The pipeline is a signal chain

Vexy Lines is, fundamentally, a signal-processing engine for images.
Feed it a raster — a high-contrast photograph, a pencil sketch, an AI-generated noise
field — and it analyses the luminance, then draws mathematically precise lines, dots, or
strokes to recreate the picture in pure vector.

The path is direct. Source image becomes a luminance heatmap.
The heatmap drives stroke weight, dot size, or text weight.
Darker regions command thicker geometry; lighter regions get fine, restrained marks.
The output is print-ready SVG that scales infinitely, recolours cleanly, and exports to
PDF without losing fidelity.

It is the same mental model a sound engineer uses on a recording.
Treat the input as a signal.
Shape it. Filter it.
Reduce it until the essential thing comes through.

## Why halftone earns its own mode

If you grew up staring at old maps, comics, or 1980s movie posters, halftone is already
wired into your visual cortex.
Vector tutorials have explained halftone tricks for years.
Illustrator guides build dot patterns through the Blend tool, expand to vectors, then
mask. Plug-ins like Astute Graphics’ Phantasm add live controls.
The results can be beautiful, but each variant — lines, dots, waves — tends to demand
its own manual recipe, and iterating means digging back through layers of destructive
steps.

Vexy Lines treats halftone as a first-class fill.
Drop in a photo, add a Layer, choose Halftone.
Tone controls dot or stroke size and density.
Placement can be grid-based or randomised.
Dot shapes are configurable, including custom SVG imports.
Pattern size, angle, contrast, and dot morphing between shapes are all live.
Because the output is vector, you can scale to a billboard, recolour, or export to SVG
and PDF for screenprint and risograph workflows without watching the file crumble.

If you are chasing the very specific “screen-printed band poster found under a
refrigerator magnet” look, you can stack multiple halftone fills at different angles and
dot sizes — only this time with live controls instead of blind trial and error.

## The fill catalogue, briefly

A dozen distinct fill styles ship in the first release.
Linear produces parallel lines that swell and taper based on the luminance map.
Wave does the same with a sinusoidal twist.
Trace abandons the grid to follow the natural edge contrast of the source image,
producing something close to nineteenth-century steel engraving.
Stipple clusters dots based on density, automating the painstaking newspaper-hedcut
style that illustrators used to spend days crafting by hand.
Halftone separates the image into configurable dots that mimic offset printing.

For printmakers, the multicolour halftone mode separates the source into colour channels
and renders each as a separate, angled halftone layer.
The output is layered SVG, one layer per colour, ready to be burned onto silk screens.
The maths is simple.
The discipline is choosing what to keep and what to throw away.

## The typographic crossover

Mapping a variable-font specimen into Vexy Lines translates weight and contrast into
stroke thickness and density, turning a static type sample into something closer to a
print pulled from a mid-century engraving shop.
Both tools think in continuous spaces: FontLab 8 lets you design interpolation across
weight and width axes; Vexy Lines lets you interpolate stroke thickness and density
based on tone.

The Text fill mode goes further, using a variable font’s weight axis to encode
brightness. That deserves its own post.

## References

- [Vexy Lines — official site](https://vexy.art/lines/)
- [Vexy Lines knowledge base](https://help.vexy.art/)
- [Halftone shading — Astute Graphics](https://astutegraphics.com/learn/10minskills/halftone-shading-a-quick-how-to)
- [Vexy Lines on AlternativeTo](https://alternativeto.net/software/vexy-lines/about/)

[Read more →](https://vexy.art/lines/){ .fl-help-cta }
