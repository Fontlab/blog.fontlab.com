---
this_file: src_docs/md/posts/2025-11-04-the-briem-method-and-the-geometry-of-nothing.md
title: "The Briem method and the geometry of nothing"
authors: [fontlab]
tags: [briem, spacing, kerning, metrics, fontlab-8]
date:
  created: 2025-11-04
slug: the-briem-method-and-the-geometry-of-nothing
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab/8/tutorials/briem/5-0-spacing/briem-5-01-spacing/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "Briem taught at Royal Academy of Fine Arts, Copenhagen, 1996 — verify institution and date"
    - "Tschichold condemned tight spacing in 1952 — verify source/year"
    - "Zapf popularised tight spacing with Palatino — verify historical claim"
    - "Control characters n, o, H, O for spacing — verify this matches Briem's actual method"
  image_status: present
  image_needs: ""
  weakness_verdict: keep
  consolidate_with: "2025-10-07-briem-drawing-italic.md, 2025-12-16-fontlab-tv-briem-on-brushes.md"
  notes: "Strong title and opening; Tschichold/Zapf historical framing is the best paragraph. Briem series needs cross-links; standalone it buries the spacing workflow under too much preamble."
---
![](../media/illu/the-briem-method-and-the-geometry-of-nothing-1.png){.illu-thumb
.illu-index}

The most difficult part of drawing a typeface is not the black ink.
It is the white space.

<!-- more -->

Letters are social creatures, and how much personal space they afford one another
decides whether a paragraph is a joy to read or a chore.
Gunnlaugur SE Briem, who taught type design at the Royal Academy of Fine Arts in
Copenhagen in 1996, distilled this into a relentlessly practical methodology that
eschews inspiration in favour of systematic testing.

Briem’s foundational advice is grounded in optical illusions.
If you rely purely on mathematics, the result will look terrible.
Human vision requires compensation.
Briem advocated for a modular approach to rough out a design quickly — assembling
letters from a basic rectangle, a curve, and a diagonal — before spending the majority
of the time on optical correction.
You literally chop away the parts that look wrong until it looks right.

Spacing, Briem argued, is not about finding a universal mathematical truth.
It is about establishing rhythm.
In FontLab 8, this is managed through sidebearings and metrics keys.
You do not space all twenty-six letters independently.
You establish control characters — typically the lowercase `n` and `o`, the uppercase
`H` and `O`. You adjust the space around the `n` until a string of `nnnnn` feels
comfortable. Then you link the left sidebearing of `b`, `h`, `i`, `k`, and `r` to the
left sidebearing of `n`.

FontLab handles the linkage through mathematical expressions.
If you later decide your typeface needs to be tighter, you narrow the spacing on the
`n`, and every linked glyph updates.
It brings programmatic efficiency to an aesthetic judgement.

When sidebearing logic fails, you resort to kerning.
The `V` next to the `A` will always need a per-pair adjustment.
To avoid kerning ten thousand individual pairs, FontLab uses class-based kerning.
Group all left-leaning diagonals into one class, all right-leaning diagonals into
another, kern the class once, and the adjustment propagates.

Spacing evolves with technology and taste.
Tschichold condemned tight spacing in 1952; Zapf popularised it with Palatino soon
after. The fundamentals do not change.
Letters must relate to one another logically, and the white between them is where the
relationship lives.

## References

- [Briem method tutorial — FontLab](https://help.fontlab.com/fontlab/8/tutorials/briem/1-0-intro/briem-1-00-intro/)
- [How to space a typeface — MyFonts](https://www.myfonts.com/a/font/content/how-to-space-a-typeface)
- [Spacing a font, part 1 — Society of Fonts](https://www.societyoffonts.com/2018/09/19/spacing-a-font-part-1/)
- [White-space compensation — TypeDrawers](https://typedrawers.com/discussion/3317/white-space-compensation-or-other-reasons-in-n-m-w-etc)

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/briem/5-0-spacing/briem-5-01-spacing/){ .fl-help-cta }
