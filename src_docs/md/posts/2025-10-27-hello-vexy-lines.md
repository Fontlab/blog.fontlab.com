---
this_file: src_docs/md/posts/2025-10-27-hello-vexy-lines.md
title: "Hello, Vexy Lines"
authors: [vexy-lines]
date:
  created: 2025-10-27
slug: hello-vexy-lines
---
Vexy Lines converts raster images into scalable vector artwork.
Drop in a photo, screenshot, or AI-generated graphic; choose a fill style; export as SVG
or PDF. The underlying mechanism is signal processing: image brightness drives stroke
thickness, so darker areas get heavier lines and lighter areas get finer ones.

<!-- more -->

![Vexy Lines application showing fill styles](../media/vexy-hello-hero.png)

Fill styles available at launch:

- **Linear** — parallel lines whose weight tracks the source image’s luminance
- **Wave** — undulating lines, same brightness-to-weight mapping
- **Halftone** — classic dot-based halftone pattern
- **Trace** — follows edges in the source image rather than a fixed grid
- **Text** — fills areas with letterforms, using variable font weight to encode
  brightness
- **Handmade** — a looser, sketch-like stroke character

![Vexy Lines fill style examples](../media/vexy-hello-fills.png)

Output is organized with layers, groups, and masks, giving you control over which parts
of the source image get which treatment.
Strokes can sample colors from the source image, producing a chromatic result that
echoes the original photograph’s palette.
A mesh-wrapping option handles pattern continuity, and hidden-line removal conceals
strokes on the far side of a shape.

![Vexy Lines stroke sampling from source image colors](../media/vexy-hello-strokes.jpeg)

The text fill mode deserves a note.
Font weight is driven by the same signal-processing pipeline that controls line weight
in the linear mode — the typographic texture encodes the image’s tonal structure.
It works with variable fonts that have a weight axis, and the effect can be combined
with linear or wave fills in layers.

Vexy Lines is available as a free browser version and as paid desktop applications for
macOS and Windows. The browser version has limited export options; the desktop versions
export full-resolution SVG and PDF.

More at [vexy.art](https://vexy.art/).
