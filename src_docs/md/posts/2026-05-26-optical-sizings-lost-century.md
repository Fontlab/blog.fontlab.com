---
this_file: src_docs/md/posts/2026-05-26-optical-sizings-lost-century.md
title: "Optical sizing's lost century"
authors: [fontlab]
tags: [variable-fonts, optical-sizing, history, fontlab-8]
date:
  created: 2026-05-26
slug: optical-sizings-lost-century
---
William Caslon knew something in 1720 that digital type spent a century forgetting:
a six-point letter is not a twelve-point letter made smaller.

<!-- more -->

[![Caslon 1720 specimen showing every size cut as a separate punch](https://upload.wikimedia.org/wikipedia/commons/9/93/Caslon-schriftmusterblatt.jpeg)](https://en.wikipedia.org/wiki/Optical_sizing)

Open Caslon's 1720 specimen and you see it immediately.
Every size of every face is a different drawing.
The six-point is thicker, wider, more open — cut from a different punch by a punchcutter
who understood that ink squashes and eyes strain at small sizes.
The sixty-point is crisper, more refined, its spacing tighter because it can afford to be.

Phototype killed this.
One master, photographed up and down.
A 72-point headline and a 9-point caption came from the same piece of film, scaled.
Nobody at the photo house was cutting a different punch for each size.
It was efficient and it looked mediocre and it became the norm.

Digital didn't fix it.
PostScript took the same shortcut.
So did TrueType, and most OpenType fonts right up to the variable era.

The `opsz` axis finally brings it back.
Set the axis value to the intended size in points, and the font swaps in shapes drawn for
that size — heavier strokes and looser spacing at 6pt, finer strokes and tighter spacing
at 60pt.
Amstelvar (2017, ranging from 8 to 144pt) and Roboto Flex pioneered the continuous
version.
Adobe's Source Serif 4 took a different position in January 2021: five discrete `opsz`
styles rather than infinite interpolation.
Frank Grießhammer's argument was that five carefully drawn sizes beat an infinite
number of mediocre ones.
Both approaches are defensible.

There is still an unresolved argument over what `opsz` units actually mean.
Physical points? CSS pixels?
GitHub issue roboto-flex#104 has been open for years, with Adam Twardoch, Laurence
Penney, John Hudson, and Dave Crossland trading positions.
It matters more than it sounds: `font-optical-sizing: auto` is the default in most
browsers, and "auto" is doing slightly different things on each platform.

Caslon would have an opinion.
He would probably be terse about it.

## References

- [Optical sizing — Wikipedia](https://en.wikipedia.org/wiki/Optical_sizing)
- [roboto-flex issue #104 — opsz units](https://github.com/googlefonts/roboto-flex/issues/104)
- [Introducing Source Serif 4 — Adobe blog](https://blog.adobe.com/en/publish/2021/01/12/introducing-source-serif-4)

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-7-variable/){ .fl-help-cta }
