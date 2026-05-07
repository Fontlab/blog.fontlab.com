---
this_file: src_docs/md/posts/2024-02-13-transtype-the-converter-that-outlived-the-format.md
title: "TransType, the converter that outlived the format"
authors: [transtype]
tags: [transtype, type-1, opentype, conversion, legacy]
date:
  created: 2024-02-13
slug: transtype-the-converter-that-outlived-the-format
---
TransType 4 shipped in 2013 to solve a problem nobody wanted to keep having.
A decade later it is still solving it, because PostScript Type 1 refused to leave the
building on schedule.

<!-- more -->

<!-- image TBD -->

When Adobe finally pulled Type 1 support from Creative Cloud in early 2023, a lot of
studios discovered that their “legacy” libraries were not in a museum.
They were inside live identities, half-finished books, and active brand guidelines.
The fonts that had worked since the Clinton administration suddenly refused to load in
InDesign, and the deadline was Tuesday.

TransType’s job is not glamorous.
You drag in a folder of dusty Type 1 files.
The tool merges 256-glyph fragments — the standard set, the expert set, the small caps
that lived in their own file — into one coherent OpenType.
It rewrites the names so the family hangs together again.
It keeps as much of the kerning and metric information as it can carry across the format
gap. Then it spits out an OTF or TTF that modern apps will actually open.

The clever part is what it does not do.
It does not “improve” the outlines.
It does not redraw anything.
It moves a typeface from one container to another with the smallest amount of damage.
That restraint is the whole product.

It is worth remembering that the same engine had a side career in early colour fonts.
Before COLRv1 was a settled standard, designers used TransType’s overlay feature to
stack monochrome fonts into rough chromatic typefaces — a duct-tape solution that
worked.

A converter is supposed to be a footnote.
TransType 4 keeps showing up in working studios because the format it converts away from
keeps refusing to die.

## References

- [TransType 4 — overview](https://www.fontlab.com/font-converter/transtype/)
- [How to convert PostScript fonts to OpenType — CreativePro](https://creativepro.com/how-to-convert-postscript-fonts-to-opentype-with-transtype/)
- Adobe ends Type 1 support — Adobe
- [The end of Type 1 — Type Network](https://typenetwork.com/articles/the-end-of-type-1)

Read more on help.fontlab.com →{ .fl-help-cta }
