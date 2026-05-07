---
this_file: src_docs/md/posts/2024-12-10-opentype-features-as-ux.md
title: "OpenType features as invisible UX"
authors: [fontlab]
tags: [opentype, kerning, ligatures, contextual-alternates, ux]
date:
  created: 2024-12-10
slug: opentype-features-as-ux
---
Most readers never notice when typography is right.
They only notice when reading feels like work.
The features that decide which side of that line a font lands on are mostly the
unglamorous ones — kerning, standard ligatures, contextual alternates — the parts that
handle the friction the user never sees.

<!-- more -->

![OpenType feature panel in FontLab 8](/media/opentype-features-as-ux/fl8-8days-opentype.png)

## the features users never see

OpenType features get sold on the showy ones: swashes, discretionary ligatures,
alternate numerals, fancy stylistic sets.
Those are the ones that show up in marketing copy and design-blog round-ups.
The serious typographic work happens in the boring features.

`kern` for kerning. `liga` for the default ligatures that fix collisions like `fi` and
`fl`. `calt` for the contextual substitutions that keep cursive scripts from looking
like they were typed by a machine.
`mark` and `mkmk` for the diacritic positioning that keeps an ‘é’ vertically aligned
across every base it sits on.
None of those features are flashy.
All of them are the difference between text that reads as text and text that reads as a
series of characters.

Type Network frames it well: standard ligatures are a “font superpower” precisely
because they turn a raw glyph set into a text system that behaves intelligently.
The user never thinks about the `fi` ligature.
They think about how the paragraph reads.

## kerning, the load-bearing feature

Of all the OpenType features, kerning carries the most weight in user perception.
A poorly kerned font reads as cheap, because the eye notices the gaps before it notices
the letters. A well-kerned font reads as professional, because the eye doesn’t notice
anything at all.

Modern kerning is class-based.
Rather than kerning every individual pair (the V/A cuts, the T/o tucks, the L/Y
collisions), you group letters into classes — left-side diagonals, right-side diagonals,
round shoulders, narrow stems — and kern at the class level.
The result is a smaller table, faster lookups in the rendering engine, and consistency
across accented variants you might otherwise forget to kern.

FontLab 8’s kerning panel handles the class structure natively.
You tag a glyph as belonging to a class, define the class once, kern the class once, and
every member of the class — including the eight Eastern European accented variants of
the base glyph — gets the kerning applied.
This matters most for languages with heavy accent coverage, where kerning every pair
manually is the opposite of feasible.

## contextual alternates, the engine behind connected scripts

`calt` is the OpenType feature that decides which version of a glyph to substitute based
on the surrounding context.
Its native habitat is connected scripts — Arabic, Devanagari, cursive Latin, blackletter
— where the entry stroke of one letter has to match the exit stroke of the previous one
or the script falls apart visually.

Arabic is the demanding case.
A single letter changes shape depending on whether it sits at the beginning, middle, or
end of a word, or stands alone.
The OpenType layout engine handles the positional substitution automatically through the
`init`, `medi`, `fina`, and `isol` features.
A handwriting font in any script may use thousands of contextual rules to vary glyph
shapes so that the same letter never appears identically in a row, mimicking the natural
variation of a human hand.

FontLab 8 generates the substitution syntax automatically when glyphs are named with the
right conventions. A small-cap glyph named `a.sc` ends up in the `smcp` feature without
anybody writing the feature code by hand.
A swash glyph named `A.swsh` ends up in the `swsh` feature.
The naming conventions are the schema; the feature code is the compiled output.

## the messy reality

In practice, OpenType features do not always work as cleanly as the spec suggests.
Discussion threads among type designers note that the OpenType specification
*recommends* certain default behaviours but does not require them, and applications are
free to ignore the recommendations.
Firefox’s early OpenType support, in particular, made discretionary-ligature decisions
that broke German words and Turkish dotted/dotless `i` distinctions because the engine
ignored language-specific rules baked into the fonts.

This is why font engineers obsess over language system tags, feature ordering, and test
strings. The user shouldn’t have to know that German wants `Auflauf` to behave
differently from English `office`, only that both read correctly.
The engineering work happens at the feature level so the user’s reading experience stays
unbroken.

## CSS, the application side

For web designers engaging these features, the CSS surface is straightforward in theory
and messy in practice.
High-level properties like `font-variant-ligatures` and `font-kerning` cover the common
cases. The low-level escape hatch is `font-feature-settings`, which takes raw OpenType
feature tags and lets you force a browser to obey your typographic will:

```css
.body-text {
  font-feature-settings: "kern" 1, "liga" 1, "calt" 1, "onum" 1;
  font-variant-ligatures: contextual common-ligatures;
}
```

The trick is that some browsers respect the high-level properties and some require the
low-level tags; in production code, you write both, in that order.
Browsers favour the more specific declaration, which means the `font-feature-settings`
line wins where it matters.

## the moral

OpenType features are user experience for text.
They are how a font behaves under pressure — long paragraphs, mixed scripts, accented
characters, contextual letter combinations, language-specific rules.
The features that decide whether the user has a good time are mostly the ones the user
will never consciously notice.
That is the point. Good UX, in any medium, is invisible until somebody removes it.

## References

- [Caring about OpenType features — Typekit Practice](https://practice.typekit.com/lesson/caring-about-opentype-features/)
- [OpenType at work: standard ligatures — Type Network](https://typenetwork.com/articles/opentype-at-work-standard-ligatures)
- [OpenType fonts — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/OpenType_fonts)
- [Kerning and OpenType features in Firefox 3 — Ralf Herrmann](https://opentype.info/blog/2008/06/14/kerning-and-opentype-features-in-firefox-3.html)
- [Practical guide to alternate characters and OpenType features — Pangram Pangram](https://pangrampangram.com/blogs/journal/opentype-features)

[Read more on help.fontlab.com →](https://help.fontlab.com/fontlab/8/manual/OpenType-Features/fontlab/8/manual/){
.fl-help-cta }
