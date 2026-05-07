---
this_file: src_docs/md/posts/2024-05-07-rescuing-type1-with-transtype.md
title: "Rescuing endangered fonts with TransType 4"
authors: [transtype]
tags: [transtype, type-1, opentype, conversion, fontlab-8]
date:
  created: 2024-05-07
slug: rescuing-type1-with-transtype
---
A surprising amount of contemporary design still depends on fonts that think the year is
1998\.

<!-- more -->

<!-- image TBD -->

When Adobe announced that PostScript Type 1 would no longer work in Creative Cloud,
studios discovered that their “legacy” fonts were not museum pieces.
They were inside active identities, ongoing book series, and live UI mockups.
The technical question is simple: how do you get from Type 1 to OpenType without
breaking names, style links, and carefully tuned kerning?

Independent reviews keep pointing to TransType 4. The flow is brutally direct — drag
Type 1 files in, organise families, map styles into sensible slots, export fresh
OpenType with updated internals and consistent naming.
Drag and drop, a live glyph map, family and style names that stay stable so existing
layouts do not suddenly reflow.
TransType preserves as much of the original font data as possible while upgrading it to
modern OpenType, optimising outlines and fixing common structural issues along the way.

TransType is not a font editor.
It is a bridge. The long-term health of a typeface depends on editing and maintaining it
in a modern environment — precisely the niche that FontLab 8 fills.
A typical workflow looks like this: TransType 4 converts a mission-critical Type 1
family into clean OpenType, then FontLab 8 picks it up if you need to extend the
character set, add OpenType features, or build a variable version.
The combination lets studios rescue 1990s typefaces without abandoning the years of
design and engineering locked in their outlines and kerning tables.

If you squint a bit, it is one continuum: Pyrus and early FontLab on one end, variable
fonts and screen typography on the other, and a small conversion utility in the middle
making sure the bridge does not collapse.

## References

- [How to convert PostScript fonts with TransType — CreativePro](https://creativepro.com/how-to-convert-postscript-fonts-to-opentype-with-transtype/)
- [TransType 4 — FontLab](https://www.fontlab.com/font-converter/transtype/)
- [FontLab 8 review — The Endearing Designer](https://theendearingdesigner.com/fontlab-8-review/)
- [Variable fonts and screen typography — Typoteka](https://typoteka.pl/en/period/variable-fonts-and-screen-typography)

Read more on help.fontlab.com →{ .fl-help-cta }
