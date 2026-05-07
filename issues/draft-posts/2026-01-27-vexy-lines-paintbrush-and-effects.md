---
this_file: issues/draft-posts/2026-01-27-vexy-lines-paintbrush-and-effects.md
title: "The algorithmic paintbrush: Vexy Lines effects and exports"
authors: [vexy-lines]
tags: [vexy-lines, algorithms, vector, effects, export, variable-fonts]
date:
  created: 2026-01-27
slug: vexy-lines-paintbrush-and-effects
draft: true
---
Algorithms make better paintbrushes than people give them credit for, when they are
aimed at the right problem.
Vexy Lines aims them at one specific job: turning a raster image into pure vector marks
that survive any pipeline downstream.

<!-- more -->

![Vexy Lines — linear engraving of a portrait](../media/vexy-lines2-hero.jpg)

## One pipeline, many fills

Every fill mode in Vexy Lines shares the same engine.
The tool reads source-image luminance, builds a heatmap, and decides where strokes go
thick and where they go thin.
What changes between modes is the geometry the engine paints with.

**Linear** draws parallel lines that swell and taper with the luminance map.
**Wave** does the same with a sinusoidal modulation.
**Trace** abandons the fixed grid and follows the natural edge contrast of the image,
producing something close to nineteenth-century steel engraving.
**Flowlines** follow the contour structure of the source — lines curve around the shape
of a face or object instead of marching in ranks.
**Halftone** mimics offset printing with configurable dot size, angle, and frequency.
**Dithering** is a coarser, grittier variant of the same idea.
**Stipple** clusters dots by density, automating the hedcut look familiar from newspaper
portraits.

For printmakers, **multicolour halftone** separates the source into colour channels and
renders each as a separate halftone layer at a different screen angle.
The output is layered SVG with one layer per colour — drop straight into a screenprint
workflow, or open in Illustrator for further editing.

![Vexy Lines — halftone effect](../media/vexy-lines2-halftone.jpg)

## Variable-font text fills

The most interesting fill, for type designers, is Text.
Rather than scaling static letters to fill a region, Vexy Lines uses the weight axis of
a variable font to encode the image’s brightness.
A region of deep shadow renders in Ultra Black; a bright highlight renders in Extra
Light. The result is a typographic texture where the letters themselves modulate to form
a photograph. It is a literal answer to the question “what if your image were the
variation slider”.

Text fills can combine linear and wave patterns with variable-font weight encoding.
A gradient source drives the variable-font axis, producing typographic textures where
letterform weight transitions across the image.
The practical payoff: SVG text fills that animate cleanly in browsers using CSS
transitions, with no JavaScript.

![Vexy Lines — stipple hedcut portrait](../media/vexy-lines2-portrait.jpeg)

## Export formats that match real workflows

Vector work is only useful if it lands cleanly in the next tool.
Vexy Lines exports SVG, PDF, and EPS for scalable output, and PNG and JPG for raster
output at configurable resolutions.
EPS keeps the door open for older print pipelines that still expect it.
The raster formats make Vexy Lines usable without an SVG-capable application downstream
— paste a halftone PNG straight into a layout, ship a JPG to a client preview, no
further tooling required.

## Where this fits in a working studio

Typical uses cover most of the territory where vector marks meet imagery: social-media
graphics, vintage poster design, tattoo artwork, hedcut portraits, textile patterns,
screenprint preparation, retro gradient effects, SVG animation source material,
large-format prints, murals, vinyl-cutting files.

Platform: macOS and Windows, with a free browser version for evaluation.
The processing happens locally in the desktop app — your source images do not leave the
machine. The browser version is the lightweight on-ramp; the desktop builds are where
production work belongs.

The tool takes the analog grit of photography and translates it into the cold, scalable
mathematics of SVG, while staying close enough to the printmaker’s hand that the output
still looks made, not generated.

## References

- [Vexy Lines — official](https://vexy.art/lines/)
- [Vexy Lines knowledge base](https://help.vexy.art/)
- [Vexy Lines on AlternativeTo](https://alternativeto.net/software/vexy-lines/about/)
- [Vexy Lines on MacUpdate](https://vexy-lines.macupdate.com/)

[Read more →](https://vexy.art/lines/){ .fl-help-cta }
