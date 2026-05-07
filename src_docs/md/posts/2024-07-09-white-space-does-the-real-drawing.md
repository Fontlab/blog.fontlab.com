---
this_file: src_docs/md/posts/2024-07-09-white-space-does-the-real-drawing.md
title: "White space does the real drawing"
authors: [adam]
tags: [spacing, counters, type-design, fontlab-8, frutiger]
date:
  created: 2024-07-09
slug: white-space-does-the-real-drawing
---
Letterforms are made of black shapes, but type is judged by the white around and inside
them.

<!-- more -->

<!-- image TBD -->

Adrian Frutiger’s old line — that the empty spaces are the crucial part of a typeface —
remains the cleanest correction to beginner enthusiasm.
People fall in love with terminals, serifs, and flamboyant tails.
The page falls apart because the counters and sidebearings were treated as
afterthoughts.

Walter Tracy’s spacing logic is useful precisely because it is unfancy.
Start with a few key letters.
Think in groups. Build rhythm before you chase exceptions.
Do not confuse kerning with structural spacing.
Research on spacing methods makes the same point in more formal language: fitting is not
cosmetic repair after drawing.
It is part of the drawing.

That is a perfect FontLab 8 theme because it turns the software away from “how to kern
fast” and toward the harder truth: if the default rhythm is wrong, you are decorating a
problem.
FontLab’s metrics keys let you set the sidebearing of `n` once and link the left
sidebearings of `b`, `h`, `i`, `k`, and `r` to it; tighten the `n` later and everything
linked tightens with it.
Class-based kerning extends the same logic to pairs.
You group all left-leaning diagonals — `V`, `W`, `Y` and their diacritical variants —
into one class, all right-leaning diagonals into another, and kern the class once.

Optical sizes push the same idea further: text and display cuts are not vanity
variations, but different answers to different spatial problems.
The smaller the type, the more air the letters need.
The larger the type, the tighter the rhythm can sit without falling apart.

The drawing is the part students notice.
The spacing is the part professionals get paid for.

## References

- [The empty spaces — Frutiger via Typography.guru](https://typography.guru/quote/the-empty-spaces/)
- [Spacing a font, part 1 — Society of Fonts](https://www.societyoffonts.com/2018/09/19/spacing-a-font-part-1/)
- [Inside the fonts: optical sizes — Type Network](https://typenetwork.com/articles/inside-the-fonts-optical-sizes)
- [opsz axis — Microsoft](https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_opsz)

[Read more on help.fontlab.com →](https://help.fontlab.com/fontlab/8/manual/Spacing/){
.fl-help-cta }
