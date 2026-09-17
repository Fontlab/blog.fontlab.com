Round a number too early and the error never leaves. That is the whole case for working in fractional coordinates while you design, and rounding to a grid only when you ship.

OpenType PS (`.otf`, CFF outlines) permits fractional coordinates in principle. There are technical caveats, and the final font you ship is effectively expected to sit on an integer grid. But there is a real difference between the grid you ship on and the grid you work on.

## Why precision during editing matters

Say you draw your glyphs on an integer grid, then start adjusting. You make a glyph slightly narrower, then a touch wider. You slant it a few degrees, then slant it back. You nudge a small rotation, or scale the shape down and then up again.

On an integer grid, each of those operations rounds its result to whole units. The errors do not cancel out — they accumulate. After a handful of transforms, your control points, angles, and stem thicknesses have all drifted from the original design, and there is no way to recover the values you started with.

On a fractional grid, none of that happens. The positions of the control points, the angles, the stem thicknesses — everything stays exactly as designed, no matter how many times you transform the shape and transform it back.

## The practical takeaway

A hardwired integer grid, like the one in FontLab Studio, puts a quiet limit on the designer: every edit costs a little precision. A fractional grid, like the one in Fontographer, lets you avoid that loss entirely during the design process.

The rounding still has to happen — just at the right moment. When you generate or ship the font, you align the points to an integer grid (or the software does it for you). The difference is that you round once, from clean source values, instead of accumulating rounding error across every edit along the way.

[Read more →](https://help.fontlab.com/fontlab-vi/Drawing/)
