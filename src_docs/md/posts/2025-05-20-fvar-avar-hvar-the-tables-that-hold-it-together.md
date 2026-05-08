---
this_file: src_docs/md/posts/2025-05-20-fvar-avar-hvar-the-tables-that-hold-it-together.md
title: "fvar, avar, HVAR — the tables that hold a variable font together"
authors: [fontlab]
tags: [variable-fonts, opentype, fontlab-8]
date:
  created: 2025-05-20
slug: fvar-avar-hvar-the-tables-that-hold-it-together
---
![](../media/illu/fvar-avar-hvar-the-tables-that-hold-it-together-1.png){.illu-thumb
.illu-index}

A variable font isn’t a new file format.
It’s an OpenType file with a few extra tables nailed on, and once you know what each one
does, the whole thing stops being magic.

<!-- more -->

The core stack:

**`fvar`** declares the axes the font supports — their names, ranges, and defaults —
plus any named instances ("Bold", “Condensed Italic”) the designer wanted to bake in.
Without `fvar`, the renderer doesn’t know the font varies at all.

**`gvar`** (for TrueType outlines) or **`CFF2`** (for PostScript outlines) holds the
deltas: the per-axis offsets that move each point as you slide a value.
This is where the actual interpolation data lives.

**`avar`** handles non-linear axis remapping.
A slider midpoint doesn’t have to be a visual midpoint.
If the weight axis looks thin for the bottom half of its range and fat for the top,
`avar` lets the designer remap the curve so the slider feels even.

**`HVAR`** stores per-instance advance-width deltas so layout engines don’t have to
interpolate metrics from scratch.
Without it, spacing can drift between instances in ways that look like bugs and are.

**`MVAR`** covers font-wide metric variations — cap height, x-height, line gap — that
need to shift as axes change.

**`STAT`** is the table that makes named instances findable.
It’s what lets an app understand that “Bold Condensed” in a variable font is the same
concept as “Bold Condensed” in a static family.

All of this was announced at ATypI Warsaw in September 2016 — Adobe, Apple, Google, and
Microsoft on the same stage.
John Hudson’s Medium essay from that month remains the most readable single account of
what the format is and why it was built the way it was.

The practical reason to know this is dull and useful.
When something renders correctly in Chrome but breaks in Safari, the answer is almost
always one of these tables disagreeing with another — `avar` misread, `HVAR` missing,
`STAT` entries that contradict `fvar` ranges.
Knowing what each table is for shortens the debug from a day to twenty minutes.

## References

- [OpenType variations overview — Microsoft](https://learn.microsoft.com/en-us/typography/opentype/spec/otvaroverview)
- [Introducing OpenType variable fonts — John Hudson, Medium](https://medium.com/variable-fonts/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369)
- [Variable fonts — Typolexikon (German)](https://www.typolexikon.de/variable-fonts/)
- [Variable fonts guide — Google Fonts](https://googlefonts.github.io/gf-guide/variable.html)

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-7-variable/){ .fl-help-cta }
