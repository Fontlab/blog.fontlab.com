---
this_file: issues/draft-posts/2022-08-15-8-days-the-essentials.md
title: "Eight days of FontLab — the essentials"
slug: 8-days-the-essentials
authors: [fontlab]
date:
  created: 2022-08-15
tags: [tutorials, drawing]
draft: true
---
A font is harder to make than letters are to draw.
The gap between a sketch that looks good on paper and a working OpenType file is wide,
and most of it is tedium: spacing that read fine in pencil now reads like a ransom note,
curves drift by a unit and break a whole alphabet.
FontLab 8 exists to close that gap.
This first half of *Eight days of FontLab* covers the craft — drawing letters, expanding
to a real glyph set, teaching them to behave as text, and getting them to sit
comfortably side by side.

<!-- more -->

![FontLab 8 in dark theme with a font open across multiple panels](../media/fl8days-1-start-fl8-shot-theme-dark.png)

## Day 1: from sketch to font

You can come at FontLab three ways, and most designers use all three at different
stages: import vector artwork from Illustrator or Affinity, scan physical drawings as
bitmaps, or draw directly in the app.

The shortest route from paper to working font runs through **Autotrace**. Drag a scanned
alphabet onto the **Sketchboard**, or drop individual glyph images onto Font window
cells. The autotracer is tuned for letterforms — its sliders control smoothness and
corner detection with a live preview.
Use **Optically Separate** to split the sheet into elements, then **Place As Glyphs** to
drop each one into its slot.
Built-in OCR usually names them correctly.
Adjust sidebearings with the Metrics tool and you have a font.
First time through, this can take under a minute.

That is the tunnel. Manual tracing is the mountain.
Choose accordingly.

For consistency while drawing, the **Power Brush** lets you sketch a vector skeleton and
apply a live calligraphic stroke that you can re-tune at any time — change one weight,
change them all.
FontLab suggests common stem widths as you draw, flags unusual ones, and
lets you draw a shape once as an *element* and reference it across dozens of glyphs.

**FontAudit** runs in the background, flagging kinks, near-flat curves, open contours,
and a couple of dozen other problems that are invisible to a casual eye but ruin a font
later.

## Day 2: even a tiny font is a font

You don’t need a full character set.
A twelve-glyph font is still a font, and the format earns its keep the moment you ship
it.

![A small font built in FontLab for the Joker movie titles](../media/fl8days-2-abc-joker.png)

An OpenType `.otf` is the one universal vector container that works without negotiation
— print, design apps, office, browsers, every operating system.
One file replaces a folder of PDF, EPS, SVG, PNG variants.
A logo can be a single character.
Your signage needs twelve letters?
Make a twelve-letter font.

For drawing letters specifically, FontLab gives you tools general vector editors don’t.
The **Rapid** tool is built for the curves letters are actually made of.
**Power Nudge**, **Servant** nodes, and **Power Guides** let you stretch and squeeze
without breaking stroke thickness.

The most useful idea on day 2 is **stroke-based design**. Closed contours are fine for
geometric sans, miserable for scripts.
Instead, draw a skeleton and let FontLab expand it — uniform, tapered, or
pressure-modulated from a tablet.
End-cap shapes give you the serif you want.
Convert to contours later if you need to.
Curvy fonts stop being intimidating once the tool behaves like a pen.

## Day 3: from fifty glyphs to five hundred

English makes do with the basic Latin alphabet.
Most other Latin-script languages don’t. Add Greek or Cyrillic and the count climbs
fast. Drawing each accented variant from scratch would be miserable.

![Composite assembly: base letters plus diacritical marks](../media/fl8days-3-beyond-abc-expandyourfonts-02.png)

Draw a diaeresis once, combine it with `a`, get `ä`. With one click, FontLab generates
the composite glyphs needed to cover most European languages.
Change the base later and every composite updates.

For precision, use **anchors**. Add a `top` anchor on `a`, a matching `_top` (underscore
prefix) on `acutecomb`, turn on *Glyph > Auto Layer* in `aacute`, and the accent snaps
where the two meet. Move either anchor and every variant that uses them follows.

For symbols with no Unicode codepoint, use the Private Use Area (`U+E000`–`U+F8FF`) or
build a dedicated symbol font where typing `A` produces your first symbol.

## Day 4: when letters do the work for you

A font is a coordinated system, not a folder of drawings.
OpenType Layout gives a font two kinds of intelligence: continuous variation along
design axes, and substitution rules that respond to context.
Day 4 is about the second.

A **ligature** is a single glyph that replaces a common letter pair — `fi`, `fl`, `st`.
Naming does the work.
Create the combined drawing, name it `f_i` (underscore between components), and choose
**Add Auto Features** from the Features panel menu.
FontLab writes the `liga` code:

- `f_i` or `f_i.liga` → Standard Ligatures, on by default
- `s_t.dlig` → Discretionary Ligatures, user-enabled

The same trick handles swashes (`A.swsh`), small caps (`A.sc`), and stylistic sets
(`A.ss01`). Walter Tracy: a great typeface is not a collection of beautiful letters, but
a beautiful collection of letters.
Naming, then **Add Auto Features**, gets you most of the way there.

Contextual substitutions — Arabic letter shaping, varying `e`s in a script font, swash
caps only at word starts — need hand-written `calt` code, but the logic is learnable.

## Day 5: spacing and kerning

Letters are social. How much room they give each other decides whether the font reads or
shouts. Harry Carter put it best: success or failure of a type is largely a question of
getting a good balance of white inside and outside the letters.

![Frutiger’s Meridien presentation, showing the rhythm of whites](../media/fl8days-5-fig1-meridien.png)

In FontLab, the white at left and right of each glyph is its **sidebearings**. Doing
each glyph by hand is endless and inconsistent.
Instead, use **metrics keys**. Start with control characters — `n` and `o` for
lowercase, `H` and `O` for uppercase.
Tune `nnonoo` and `HHOHOO` until they feel even.
Then link the rest: `n` controls the flat-left side of `b h i j k l m p r`, `o` controls
the round-left side of `c d e q`. Change `n` later, and every dependent glyph updates.

**Kerning** is the per-pair override for combinations that stay awkward no matter how
you space the individual glyphs — the classic `VA`. Don’t start kerning until spacing is
finalised. Use **kerning classes** so one adjustment for the V-family against the
A-family handles every accented variant.
Kern the big problems first; trust your eye on whole paragraphs, not isolated pairs.
The goal is comfortable texture, not mathematical equality.

* * *

That’s the foundation: drawing, expansion, behaviour, spacing.
The next four days cover families, variation, fonts that aren’t text, and colour.

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/){ .fl-help-cta }
