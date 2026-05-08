---
this_file: src_docs/md/posts/2025-11-18-the-fontlab-book-in-korean.md
title: "The FontLab book in Korean"
authors: [fontlab]
tags: [fontlab-8, hangul, books, korean, typography]
date:
  created: 2025-11-18
slug: the-fontlab-book-in-korean
---
![](../media/illu/the-fontlab-book-in-korean-1.png){.illu-thumb .illu-index}

Most font editors grew up thinking about Latin. In April 2025, a Korean designer published the book that translates FontLab into Hangul terms.

<!-- more -->

Kwon Gun-oh (권건오) published **《폰트랩 타입 디자인》 (FontLab Type Design)** — the first Korean-language guide to designing fonts, and specifically Hangul fonts, in FontLab. The book covers the toolset on FontLab’s own terms: glyph window, masters, mastering, components, OpenType features. Then it pairs each chapter with the practical methods Korean designers actually use.

That second half is where it earns its place. Korean has 11,172 modern Hangul syllables. Each syllable block is assembled from up to three components — initial consonant (초성), vowel (중성), and optional final consonant (종성) — that tile, stack, and resize depending on which slot they fill. The same ㄱ that takes up half a block as an initial takes a quarter as a final. Drawing 11,172 variations one by one is a career, not a project. The answer is component-based design, and the book explains how to do it in FontLab specifically.

I wrote about the component workflow last year in [Making Hangul in FontLab](2025-09-23-making-hangul-in-fontlab.md) — the variable components, the smart components, the substitution logic. Kwon’s book covers that ground in Korean, with the practical judgment calls that don’t make it into documentation: which jamo (자모) shapes to draw first, how to handle the contextual sizing, where the edge cases hide.

A font editor that makes components awkward is unusable for Hangul. A guide in the wrong language doubles the cost of learning. A book by a Korean designer for Korean designers, published in Korean, quietly enlarges what FontLab is — not by changing the software, but by making it legible to the people who need it.

The character set is large. The work is not impossible. Now there is a book that says so, in Korean.

## References

- [폰트랩 타입 디자인 — Kyobo Books](https://product.kyobobook.co.kr/) *(search 폰트랩 타입 디자인)*
- [Hangul — Wikipedia](https://en.wikipedia.org/wiki/Hangul)
- [Making Hangul in FontLab](2025-09-23-making-hangul-in-fontlab.md)
- [Variable components in FontLab 8](https://help.fontlab.com/fontlab/8/whats-new/whats-new-07-families-variation/)

[Read more →](https://help.fontlab.com/fontlab/8/manual/){ .fl-help-cta }
