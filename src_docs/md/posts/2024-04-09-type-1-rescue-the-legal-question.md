---
this_file: src_docs/md/posts/2024-04-09-type-1-rescue-the-legal-question.md
title: "Type 1 rescue, the legal question"
authors: [transtype]
tags: [type-1, transtype, licensing, opentype, legal]
date:
  created: 2024-04-09
slug: type-1-rescue-the-legal-question
---
Converting a font you bought in 1998 to a format you can use in 2024 sounds like a
technical problem. Often it is a licence problem first.

<!-- more -->

<!-- image TBD -->

Most Type 1 licences from the 1990s and early 2000s did not anticipate format
conversion. They predate OpenType.
Some explicitly forbid modifying the file.
Some say nothing. A handful permit conversion for personal use only.
The result, in 2024, is that a designer with a perfectly legal old library and a
brand-new copy of InDesign can find themselves in a small grey area that nobody at the
original foundry is around to clarify.

The honest answer is to read the EULA. Many foundries — Adobe, Linotype, Monotype,
Bitstream’s successors — have published modern statements about format migration.
Some offer free or discounted upgrades to OpenType for licensed users.
Others ask you to repurchase.
A few have quietly accepted that the alternative is the file disappearing from active
studios entirely, which is good for nobody.

Where the legal answer is “yes, you may convert”, TransType 4 is the practical tool.
It moves the outlines into OpenType, preserves the kerning, fixes the names, and
produces a file that modern apps will load.
It does not strip embedding bits or alter the licence metadata.
The new file is, technically and legally, a wrapper around the same design you paid for.

Where the answer is “no”, the right move is to license a current OpenType cut from the
foundry. The conversion route was never about saving money.
It was about not abandoning a typeface that had been doing real work in real documents
for two decades.

The format changed. The work the font was doing did not.
A careful conversion respects both.

## References

- [TransType 4 — FontLab](https://www.fontlab.com/font-converter/transtype/)
- Adobe Type 1 end-of-support FAQ
- [How to convert PostScript fonts to OpenType — CreativePro](https://creativepro.com/how-to-convert-postscript-fonts-to-opentype-with-transtype/)
- [The end of Type 1 — Type Network](https://typenetwork.com/articles/the-end-of-type-1)

Read more on help.fontlab.com →{ .fl-help-cta }
