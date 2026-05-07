---
this_file: src_docs/md/posts/2025-09-23-making-hangul-in-fontlab.md
title: "Making Hangul in FontLab"
authors: [fontlab]
tags: [hangul, korean, fontlab-8, components, scripts]
date:
  created: 2025-09-23
slug: making-hangul-in-fontlab
---
Hangul looks deceptively simple to a Latin-trained eye.
Twenty-four basic letters, written in tidy syllabic blocks.
The reality is that those letters combine into more than eleven thousand pre-composed
syllables, and getting them all to behave inside a single font is one of the harder jobs
in modern type design.

<!-- more -->

<!-- image TBD -->

Each syllable block is built from up to three components: an initial consonant, a vowel,
and an optional final consonant.
The components do not sit side by side.
They tile, stack, and resize depending on which slot they fill.
The same `ㅁ` that takes up half a block as an initial takes up a quarter as a final.
Designers who try to draw eleven thousand syllables one by one are still drawing them
five years later.

The way out is component-based design.
You draw the components — initial, medial, final — in the positions and sizes they need,
then assemble them into syllables programmatically.
Korean designers have done this in various tools for years; FontLab 8’s variable
components and smart components make it considerably less painful.

The Korean web and design-system community has interesting things to say about this.
`wdnote` and `pixso.net` write about Hangul fonts as design-system tokens, treating
weight, width, and contrast as parameters that the brand controls.
Roboto Flex is invoked constantly as a model.
The argument is that a Hangul family ought to expose the same axis design as a serious
Latin family — not because Hangul mimics Latin, but because typography systems are
typography systems.

FontLab 8 supports the workflow end to end.
Component-based assembly.
Variable components for syllable-level interpolation.
OpenType feature code for the substitution rules that actually compose Hangul on screen.
Proper export to OpenType variable fonts that the browser, the iOS keyboard, and the
Korean news site all understand.

The character set is large.
The work is not impossible.
The tools have caught up.

## References

- [Hangul typography on wdnote](https://wdnote.tistory.com/197)
- [Pixso — HTML and Korean fonts](https://pixso.net/kr/articles/html-pixso-fonts-design/)
- [Variable components in FontLab 8](https://help.fontlab.com/fontlab/8/whats-new/whats-new-07-families-variation/)
- [The Type — typography podcast](https://www.thetype.com/typechat/feed/)

[Read more on help.fontlab.com →](https://help.fontlab.com/){ .fl-help-cta }
