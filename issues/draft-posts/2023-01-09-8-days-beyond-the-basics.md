---
this_file: issues/draft-posts/2023-01-09-8-days-beyond-the-basics.md
title: "Eight days of FontLab — beyond the basics"
slug: 8-days-beyond-the-basics
authors: [fontlab]
date:
  created: 2023-01-09
tags: [tutorials, drawing]
draft: true
---
One font is a typeface.
A family of weights and widths is a tool.
And once you know how to build one, an OpenType file stops looking like a container for
letters and starts looking like a container for almost any vector artwork — logos,
icons, even photographs.
Days 6 through 8 cover variation, fonts that aren’t really text, and colour.

<!-- more -->

## Day 6: from one weight to a family

Most fonts have relatives — Bold, Italic, Condensed, ExtraLight.
Each style is a *master*: a set of contours with the same point count arranged
differently. FontLab interpolates between masters to produce everything in between, and
beyond.

To prototype a condensed variant, open your Regular, choose *Font > Add Variations*,
type `Condensed`, click OK. You now have a Width axis and two identical masters.
Select some glyphs, open *Tools > Actions*, and apply *Change width* to the Condensed
master only. Run *Match Masters* across all glyphs.
You have variation.

That gets you two outputs:

- **Static families** — predetermined points along each axis.
  Light, Regular, Bold.
  Every app supports this.
- **Variable fonts** — a single file that lets users slide continuously between any
  positions on each axis.
  A typesetter picks exactly the weight that fills the column rather than rounding to
  the nearest static style.
  Export with *Variable TT*.

Make a Regular and a Bold.
FontLab interpolates Medium and Semibold, extrapolates outward to Light and Black.
Ship them as static instances, fold the whole family into one variable file, or both.
A complete family adapts to headlines, body text, captions, tight layouts, loose ones —
without anyone in production having to fight it.

Working in a team helps too.
FontLab puts communication inside the font: **flags** colour-code glyph cells (blue for
designer A, red for needs review); **tags** group glyphs logically and apply to guides
and zones; **notes** are free-text per font or per glyph; **stickers** are visual
annotations inside the Glyph window — circles, arrows, text callouts added with the
Guides tool. None of it ships with the exported font.
It’s for your team, not your users.

## Day 7: fonts that aren’t text

Every logo ends up as a folder: PDF, EPS, SVG, PNG, light background, dark background,
monochrome, CMYK — plus the brand guidelines explaining when to use which.
That’s an archive before a single piece of collateral ships.

A font is simpler. One `.otf` stores high-resolution vectors, works across applications
and platforms, and serves as a web font without conversion.

To pack a monochrome logo as a font:

1. Create a new font. *File > Font Info > Names* — name it, click *Build Names*. Under
   Font Dimensions, turn off *Round coordinates*.
2. Pick a glyph cell. The digit `1` (`one`) is a sensible target.
3. Open the EPS, PDF, or SVG in Illustrator or Affinity Designer, copy, paste into the
   cell. When prompted, choose *monochrome contours* and *Descender to Caps Height*.
4. If paths that should be black appear white, *Contour > Join* fixes them.
5. Adjust sidebearings with the Metrics tool.
6. *Font > Export Font As* → OpenType PS. Install, type `1`, set the font.

Multi-colour logos use one glyph per colour layer with overlapping sidebearings, plus an
OpenType ligature that swaps a trigger string for the combined form.
Users type a phrase, the colours typeset separately, the logo appears.

For icons, the same idea scales.
Three principles:

- **Simplicity.** Strip to minimum recognisable elements — visual haikus.
- **Consistency.** Set *Units Per eM* to 180 or 1800 for a sane artboard; turn on *Round
  coordinates*; apply consistent stroke thickness.
- **Reuse.** Element references let you draw a shape once.
  *Element > Image > Make SVG Editable* on a folder of imports, then *Font > Detect
  Composites*, and FontLab links identical elements across icons.
  Change one, change every icon that uses it.

Test in the Preview panel at multiple sizes.
An icon clear at 48px can fall apart at 16px. Export the font, or extract individual
SVG, PDF, or PNG files via *Font > Export > Artwork Collection*.

## Day 8: colour fonts

For most of typography’s history, type was monochrome and apps coloured the ink.
Emoji broke that. The OpenType spec was extended to carry colour data inside the font
itself, and four formats coexist:

- **OpenType+COLR** — vector layers with flat colours (v0) or gradients and compositing
  (v1)
- **OpenType+SVG** — full SVG per glyph
- **OpenType+sbix** — PNG bitmaps, Apple’s original emoji format
- **OpenType+CBDT** — PNG bitmaps, Google’s format

FontLab 8 exports all four.
None works everywhere, so you typically ship two or three as a bundle and let each
application pick what it can render.

The simplest path is **layered fonts**. Design two monochrome fonts — a body and a drop
shadow, say — overlay them in FontLab, assign a colour to each layer in the Colors
panel, export as OpenType+COLR. Users type, text arrives pre-coloured.

FontLab is also a complete colour vector environment.
Paste artwork with gradients from Illustrator or Affinity, or draw fresh and fill with
linear, radial, or conical gradients edited directly in the Glyph window.
Bitmaps work too — photograph anything, paste into glyph cells, kern them.
A font of seaweed, rocks, candy, or crumpled paper is strange but entirely legitimate.

**FontAudit** keeps the result honest.
About two dozen tests run continuously and flag unwanted loops, unnecessary points,
near-flat curves that should be straight, open contours, uneven stems, and short
segments. Click a marker, read the explanation, fix it — or batch-fix all instances of
one problem across the whole glyph set, which is a genuine relief after autotracing a
hundred glyphs. Not every flag is an error.
If your design intentionally uses slightly tapered curves, turn that test off.
Each flag is a judgment call; FontAudit makes the catches so you can exercise the
judgment.

* * *

From a first sketch to a polished colour family, the distance is manageable.
The tools meet you wherever you start.

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/){ .fl-help-cta }
