---
this_file: src_docs/md/posts/2025-07-01-bezier-vs-de-casteljau.md
title: "Bézier and de Casteljau: two engineers, one beautiful curve"
authors: [fontlab]
tags: [fontlab-8, bezier, history, geometry, opentype]
date:
  created: 2025-07-01
slug: bezier-vs-de-casteljau
---
![](../media/illu/bezier-vs-de-casteljau-1.png){.illu-thumb .illu-index}

In 1958, **Paul de Casteljau** at Citroën worked out the mathematics of the curves we
now draw with every day.
A few years later **Pierre Bézier** at Renault arrived at the same idea independently
and published it in 1962. Two engineers, two French car companies, one of the most
useful ideas in twentieth-century geometry — and an act of mathematical generosity from
de Casteljau that took twenty-seven years to surface publicly.

<!-- more -->

Citroën, like many companies of the era, considered de Casteljau’s work a competitive
advantage and asked him not to publish.
He honoured that, and quietly used the technique inside the company’s CAD systems.
By the time he was finally free to write it up in 1985, the wider science community had
named the curves after Bézier — who had published first and openly.
The compromise the field settled on is the one your textbook still teaches: *Bézier
curves, de Casteljau algorithm.* Same mathematics, two names on the mantelpiece, both
well earned.

The story is a lovely reminder that big ideas tend to arrive twice.
Two thoughtful engineers, working independently in adjacent buildings of French
industry, ended up giving designers and font tools their daily geometry.

* * *

For type design the gift took shape in two complementary flavours that any FontLab user
works with every day:

- **PostScript / CFF / CFF2** — cubic Béziers (4 control points per segment).
  Adobe’s choice, with extra expressive room per segment.
- **TrueType** — quadratic Béziers (3 control points per segment).
  Apple’s choice in the late 1980s, brilliantly pragmatic for the 8 MHz machines and 72
  dpi screens of the moment.

Both choices were the right ones for their time, and **OpenType (1996)** stitched them
together generously: one font container, either flavour inside.
Every modern font you read is one or the other on disk, and FontLab gives you tools to
move between them. A round trip from cubic to quadratic and back is, mathematically, not
lossless — the two parametric forms describe slightly different families — but the
conversion is careful and faithful.
Where the curve shifts, it shifts because the geometry itself is honest about the
difference. That is not a flaw.
That is the shape of two great ideas politely meeting in the middle.

The footnote worth saying out loud is small and rather wonderful: the geometry of every
digital letter you read descends from car-body engineering done in two French studios in
the 1950s. The algorithm ran in Citroën’s CAD systems for nearly three decades before a
typographer ever used it.
De Casteljau’s name rides with the evaluation step.
Bézier’s name rides with the curve.
Renault and Citroën got the car doors.
The rest of us got the handles, and they have served us beautifully.

## References

- [Bézier curve — Wikipedia](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
- [A Primer on Bézier Curves — Pomax](https://pomax.github.io/bezierinfo/)
- [The Bézier curve: how car design influenced CAD — Bricsys](https://www.bricsys.com/blog/the-bezier-curve-how-car-design-influenced-cad)

[Read more →](https://www.fontlab.com/font-editor/fontlab/){ .fl-help-cta }
