---
this_file: src_docs/md/posts/2025-07-01-bezier-vs-de-casteljau.md
title: "Bézier vs de Casteljau — the Citroën curve nobody named"
authors: [fontlab]
tags: [fontlab-8, bezier, history, geometry, opentype]
date:
  created: 2025-07-01
slug: bezier-vs-de-casteljau
---
![](../media/illu/bezier-vs-de-casteljau-1.png){.illu-thumb}

Paul de Casteljau invented the Bézier curve in 1958. His employer made him keep quiet
about it for 27 years.

<!-- more -->

**Pierre Bézier** worked at Renault.
He published his parametric curve method in 1962. **Paul de Casteljau** worked at
Citroën. He had the same mathematics in 1958–59.

Citroën, deciding the technique was a competitive advantage, **forbade publication**.
Twenty-seven years passed.
By the time de Casteljau was finally allowed to publish in 1985, the science community
had long since named the curves after Bézier.
The compromise was to name the *evaluation algorithm* after de Casteljau — which is why
every renderer textbook says *Bézier curve, de Casteljau algorithm*.

They mean the same thing.
The names mark which company let its engineer publish.

* * *

For type design the consequence of this automotive argument is the cubic/quadratic split
that any FontLab user lives with every day:

- **PostScript / CFF / CFF2** — cubic Béziers (4 control points per segment).
  Adobe’s choice.
- **TrueType** — quadratic Béziers (3 control points per segment).
  Apple’s choice, made in the late 1980s for one reason: the arithmetic was cheaper to
  render on an 8 MHz machine at 72 dpi.

On faster hardware, at higher resolution, Adobe’s reasoning looked better.
But both choices were already locked in by the time it mattered.

**OpenType (1996)** solved the standoff by wrapping both: one font container, either
flavour inside. Every modern font is still one or the other on disk.
Conversion between them is not lossless — a round trip from cubic to quadratic and back
will, in general, change the curve.
FontLab’s conversion tools do the best they can, which is quite good, but the geometry
does not survive perfectly.
That is not a bug. It is the shape of the original disagreement.

The historical footnote worth keeping is small but worth saying out loud: the geometry
of every digital letter you read descends from a French car company that almost
classified it.
The algorithm ran in Citroën’s CAD systems for nearly three decades before
a typographer ever used it.
De Casteljau got his name on the evaluation step.
Bézier got his name on the curve.
Renault got the credit, Citroën got the car doors, and the rest of us got the handles.

## References

- [Bézier curve — Wikipedia](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
- [A Primer on Bézier Curves — Pomax](https://pomax.github.io/bezierinfo/)
- [The Bézier curve: how car design influenced CAD — Bricsys](https://www.bricsys.com/blog/the-bezier-curve-how-car-design-influenced-cad)

[Read more →](https://www.fontlab.com/font-editor/fontlab/){ .fl-help-cta }
