---
this_file: src_docs/md/posts/2025-02-04-a-width-axis-is-not-a-squeeze-command.md
title: "A width axis is not a squeeze command"
authors: [fontlab]
tags: [variable-fonts, width-axis, type-design, fontlab-8, condensed]
date:
  created: 2025-02-04
slug: a-width-axis-is-not-a-squeeze-command
---
Read enough writing on variable fonts in German, French, Spanish, Italian, Portuguese,
Polish, Russian, Chinese, Japanese, and Korean and the cliché falls apart.
Variable fonts are not a flashy weight slider.

<!-- more -->

<!-- image TBD -->

Across all those languages, serious sources keep returning to the same point: variable
fonts package multiple styles or axes into one OpenType file, help with responsive
typography, and — more importantly — give designers finer control over width, slant,
optical size, and motion.
The details differ. The pattern is strikingly consistent.

A justfont article from Taipei makes the case better than half the English-language hype
ever did. The image is three lines of the same word at the same width target.
The top line is the original.
The lower-left is brute-force horizontal squeezing.
The lower-right is the designer’s condensed version.
Same characters, same width, very different result.
The violent compression disturbs stroke logic and texture; the designed version keeps
the character’s voice.
That is the article.
That is the whole article.

This is what a width axis is for.
It is not a CSS transform that distorts strokes.
It is a separate, designed cut — narrow enough to fit, drawn carefully enough that the
rhythm survives the trip.
FontLab 8 makes this concrete: you draw the Light Condensed and the Light Wide as
masters, the engine interpolates the in-between widths, and you check the intermediate
decisions live.

Underware’s writing on variable fonts is still the useful antidote to timid thinking.
Their argument is that the format gets interesting when you stop treating old categories
as sacred — time can be an axis, motion can be an axis, contrast can be an axis.
Korean design-system writing around Roboto Flex makes a similar point: fine-grained
parameters are valuable because they let a designer build a better hierarchy, not
because they make a software demo look busy.

A width axis matters because somebody drew and checked the intermediate decisions.
Anything else is a transform.

## References

- [Tearfont and variable fonts — justfont](https://blog.justfont.com/2024/07/tearfont_variable-fonts/)
- [Very-able fonts — Underware](https://www.underware.nl/blog/2018/06/very-able-fonts-com/)
- [Thinking beyond the static — Type Network](https://typenetwork.com/articles/thinking-beyond-the-static)
- [Variable fonts — web.dev](https://web.dev/articles/variable-fonts)

[Read more on help.fontlab.com →](https://help.fontlab.com/fontlab/8/manual/Variations/){ .fl-help-cta }
