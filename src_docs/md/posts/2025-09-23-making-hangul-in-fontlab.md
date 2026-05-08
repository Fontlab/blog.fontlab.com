---
this_file: src_docs/md/posts/2025-09-23-making-hangul-in-fontlab.md
title: "Making Hangul in FontLab: a book, a script, a quiet milestone"
authors: [fontlab]
tags: [hangul, korean, fontlab-8, components, scripts, books]
date:
  created: 2025-09-23
slug: making-hangul-in-fontlab
review:
  cta_status: ok
  cta_target: "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=362506917"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "Aladin/Yes24 book metadata: 권군오, 컴원미디어, 2025-04-30, 468 pages, ISBN 9791190444354."
    - "Yes24 excerpt says the book explains reference-based drawing for 2,780 Hangul glyphs and delta filters."
    - "YouTube Seedream/FontLab 8 Hangul 2780 workflow remains live."
  image_status: present
  image_needs: ""
  weakness_verdict: keep
  consolidate_with: ""
  notes: "Rewritten 2026-05-08 to focus on Kwon Gun-oh's Korean FontLab Type Design book from issues/draft-posts/404-deepseek.md."
---
![](../media/illu/making-hangul-in-fontlab-1.png){.illu-thumb}

In April 2025, a Korean book appeared with a modest title and a very specific promise:
*폰트랩 타입 디자인* — *FontLab Type Design*. Its subtitle is even better: “FontLab and Hangul
2780, an enjoyable story.”
That is not just a manual.
It is a map through one of the hardest jobs in type design.

<!-- more -->

Kwon Gun-oh (권군오) wrote the book for people who want to make Hangul fonts in FontLab.
That sounds narrow until you remember what Hangul asks from a font editor.
Latin teaches you to think in hundreds of glyphs.
Korean starts at a different scale.
A practical Hangul font may need 2,780 syllables for common production coverage, and
full modern Hangul coverage reaches 11,172 syllables before you have drawn a digit, a
Latin letter, or a punctuation mark.

This is why the book matters.
It does not treat Hangul as a Latin workflow with a larger shopping list.
It starts from the actual Korean problem: syllable blocks built from reusable jamo (자모)
parts. Each block can contain an initial consonant, a vowel, and an optional final
consonant. Those pieces do not merely sit in a row.
They change position, proportion, and sometimes shape depending on the slot they fill.
The same component that behaves one way as an initial may need another shape as a final.

FontLab’s component, reference, and element workflows are the way through that maze.
Draw the reusable parts.
Connect them. Assemble the syllables.
Then change the source part and let the dependent glyphs update instead of redrawing
hundreds of near-identical forms by hand.
The book’s own sample text says it explains how to draw 2,780 Hangul glyphs using
references, and how to keep those connections editable with delta filters.
That is the difference between a weekend fantasy and a working production method.

The other quiet fact is language.
FontLab documentation exists in English, and the software itself grew out of a
Latin-heavy professional culture.
Korean type designers have always had to translate more than words: they have had to
translate assumptions.
What counts as a “base glyph”?
What counts as a component?
How much shape variation is structural, and how much is design taste?
Where do the edge cases hide?

A Korean guidebook answers those questions in the place where they are actually being
asked. It makes FontLab legible to designers who think in Hangul first, not after the
Latin section is finished.
That is a small publishing event and a large workflow event.

There are already signs that Korean FontLab practice is mixing traditional font
production with newer tools.
One Korean video shows a designer using Seedream-generated material and FontLab 8 to
work through a 2,780-glyph Hangul project.
The interesting part is not the AI garnish.
The interesting part is that the unit of ambition is no longer “try a few letters.”
It is “build the system.”

Hangul is not impossible in FontLab.
It is just not a Latin problem.
Kwon’s book says that clearly, in Korean, with the workflow attached.

## References

- [폰트랩 타입 디자인 — Aladin](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=362506917)
- [폰트랩 타입 디자인 — Yes24](https://www.yes24.com/product/goods/145331896)
- [Seedream으로 생성한 폰트랩 8로 한글 2780자 디자인 — YouTube](https://www.youtube.com/watch?v=XyCx4KnQ8UA)
- [GetGo Fonts for FontLab](https://fontlabcom.github.io/getgo-fonts/)

[See the book →](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=362506917){ .fl-help-cta }
