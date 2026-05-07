---
this_file: src_docs/md/posts/2025-06-03-the-mathematics-of-variable-fonts.md
title: "The mathematics of variable fonts"
authors: [fontlab]
tags: [variable-fonts, interpolation, opentype, mathematics, fontlab-8]
date:
  created: 2025-06-03
slug: the-mathematics-of-variable-fonts
---
For five hundred years, making a letter bolder meant casting a new chunk of lead.
Digital typography clung to this habit for decades.
You wanted a bold italic, you bought a separate file.

<!-- more -->

<!-- image TBD -->

Then came 2016.
Apple, Adobe, Google, and Microsoft agreed on OpenType Font Variations.
Suddenly, a whole type family could live inside a single file.

A variable font stores a default master design.
It also packs a dense set of mathematical instructions for stretching and squishing that design along continuous axes.
Think of it as a multi-dimensional space.
Give a font a weight axis and a width axis, and you define four corners: Light Condensed, Light Wide, Black Condensed, and Black Wide.
The renderer does the math to generate any point inside that square instantly.

The math gets intense.
Researchers recently built a differentiable framework using PyTorch to approximate target glyphs with unrelated variable fonts.
You don't need to understand the calculus to appreciate the result.

For UI design, the payoff is obvious.
Web pages used to choke on four separate font files just to display a few weights.
Now, one network request delivers a semibold for a tablet, a heavy condensed cut for a phone, and a delicate wide cut for a desktop monitor.

Building these files requires capable software.
FontLab 8 handles variable production natively.
Merge a static Regular with a static Bold, and FontLab sets up the axis automatically.
But linear math has limits.
Letters don't get bolder at a constant rate.
If you interpolate straight from a hairline to an ultra-black, the middle weights usually look anemic or muddy.

The solution is intermediate masters.
Drop a corrected drawing at the 700 weight position.
FontLab then warps the interpolation path to hit that exact anchor.
Sometimes a glyph needs to change shape entirely, like switching to a single-storey `g` past weight 850.
FontLab handles this by writing the OpenType code through the `rvrn` feature.

Look at Roboto Flex or IBM Plex Sans Variable.
A single file acts as a complete typography system.
UX teams get granular control without needing to license a new font weight every time a client changes their mind.

## References

- [Variable font, Wikipedia](https://en.wikipedia.org/wiki/Variable_font)
- [OpenType Font Variations, Microsoft](https://learn.microsoft.com/en-us/typography/opentype/spec/otvaroverview)
- [Differentiable variable fonts, arXiv](https://arxiv.org/html/2510.07638v2)
- [Families and variation, FontLab 8](fontlab/8/whats-new/whats-new-07-families-variation/)

Read more on help.fontlab.com →{
.fl-help-cta }
