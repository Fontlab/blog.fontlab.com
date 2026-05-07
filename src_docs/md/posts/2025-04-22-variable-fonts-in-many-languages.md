---
this_file: src_docs/md/posts/2025-04-22-variable-fonts-in-many-languages.md
title: "Variable fonts in many languages"
authors: [adam]
tags: [variable-fonts, multilingual, web, fontlab-8, design-systems]
date:
  created: 2025-04-22
slug: variable-fonts-in-many-languages
---
Designers in Warsaw, Seoul, Barcelona, and Tokyo are all asking the same quiet question:
why am I still shipping twenty font files when one variable font would do?

<!-- more -->

![Variable component in FontLab 8](/media/fl8-head-07-varcomponent.png)

Tutorials and essays about variable fonts have appeared in Polish, Spanish, Chinese,
Japanese, and Korean over the past few years, and they all converge on the same idea:
one file, many styles, faster pages, better typography.
Chinese and Japanese guides explain variation axes as levers for weight, width, slant,
and optical size, and emphasise that axes can be either continuous ranges or simple
on–off switches. Polish and Spanish articles speak the language of practice: fewer HTTP
requests, smoother responsive type scales, and the comfort of adjusting weight in fine
steps instead of jumping between Regular and Bold.
Korean writing goes further, treating variable fonts as part of design systems — using
Roboto Flex and other families to tune stroke width, counter size, and contrast for
specific screen densities and hierarchy levels.

Across languages, the benefits repeat.
Smaller payloads. Continuous control.
Better accessibility.
MDN and Google’s codelabs spell out how a single `@font-face` declaration can expose the
full variation range, with `font-weight`, `font-stretch`, and `font-variation-settings`
driving the axes. A Spanish primer on Runebook puts it bluntly: if your OS and browser
are even vaguely current, your bottleneck is no longer technology, it is whether your
typeface is ready.

FontLab 8 arrived in 2022, just as browser and OS support for variable fonts stopped
being experimental and became the boring default.
External reviewers highlight its strength as a complete variable-font production
environment on macOS and Windows — the long-standing gap for Windows-based designers who
needed robust interpolation, OpenType features, and export in one app.

In practice, that means you can draw a Light and a Black, interpolate the in-between
masters, define `wght`, `wdth` and custom axes, and export one file that speaks fluently
to a Korean news site, a Japanese app UI, and a Polish cultural portal.
All those multilingual tutorials stop being aspirational.
They describe what you can ship today.

## References

- [Variable fonts (zh-CN) — MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Guides/Fonts/Variable_fonts)
- [Variable fonts (ja) — MDN](https://developer.mozilla.org/ja/docs/Web/CSS/Guides/Fonts/Variable_fonts)
- [Variable fonts and screen typography — Typoteka](https://typoteka.pl/en/period/variable-fonts-and-screen-typography)
- [Migrating to variable fonts — Google Codelabs](https://codelabs.developers.google.com/migrating-variable-fonts)

[Read more on help.fontlab.com →](https://help.fontlab.com/fontlab/8/manual/Variations/){ .fl-help-cta }
