A font is not a static collection of drawings. It is a highly coordinated piece of software.

Beneath the vector outlines of any professional OpenType font is a layer of programmable logic that decides how characters behave when they meet one another. These are OpenType features: a series of named execution slots that substitute or reposition glyphs based on context.

The most common feature is the standard ligature, tagged `liga`. Certain letters do not get along — the hood of a lowercase `f` routinely crashes into the tittle of an `i`. The `liga` feature acts as a bouncer, detecting the collision and replacing the two glyphs with a single, harmonious `fi`.

OpenType is capable of much deeper logic. Calligraphic and handwriting fonts lean heavily on contextual alternates, tagged `calt`. Human handwriting is endlessly varied; the entry stroke of a cursive letter depends entirely on the exit stroke of the letter that came before it. A `calt` feature scans the surrounding glyphs and swaps in alternates so a digital script does not look like it was typed by a robot. In Arabic, the same machinery is not decorative but mandatory — a letter changes shape depending on whether it sits at the beginning, middle, or end of a word.

Writing this syntax by hand is miserable. FontLab 8 mostly bypasses the coding through naming conventions. Name an alternate `A.swsh` and the Swash feature is compiled automatically. Name a glyph `a.sc` and the Small Caps feature appears. The software writes the code so the designer can focus on the drawing.

For web developers, engaging features at the lowest level still means `font-feature-settings: "smcp" 1, "onum" 1;` in CSS. It is the mechanism by which digital text is forced to behave with the discipline of traditional typesetting. Users notice OpenType features most when they are missing.

## References

- [OpenType features in CSS — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/OpenType_fonts)
- [How to use OpenType features — Fontfabric](https://www.fontfabric.com/blog/how-to-use-opentype-features/)
- [A practical guide to OpenType features — Pangram Pangram](https://pangrampangram.com/blogs/journal/opentype-features)
- [OpenType feature tags — Microsoft](https://learn.microsoft.com/en-us/typography/opentype/spec/featuretags)

[Read more on help.fontlab.com →](https://help.fontlab.com/fontlab/8/manual/OpenType-Features/){ .fl-help-cta }
