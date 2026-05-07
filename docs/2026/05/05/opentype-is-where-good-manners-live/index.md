A font with manners reads like a person who knows when not to interrupt. You don’t notice it. You notice the one without.

Look at that picture. Three lines. The middle one is real small caps — a separate set of glyphs, drawn at the right weight and width to sit next to lowercase without shouting. The top one is what your word processor does when you tick the “small caps” box without an OpenType-aware font: it scales the capitals down. The colour goes weak, the weight goes spindly, the proportions go wrong. Once you see it, every menu and business card in the world becomes a small personal injury.

That difference lives in OpenType. The `smcp` feature is one tag among hundreds, and each one is a tiny social contract the font keeps with the layout engine. `liga` for fi and fl. `kern` for the gap between Y and o. `locl` for language-specific local forms when the same script needs different glyphs. `smcp` and `c2sc` for real small caps instead of shrunken capitals. `init`, `medi`, `fina`, `isol` so Arabic joins itself together without your help. `frac` so ½ stops looking like a typo.

Compiling these correctly is the actual job of FontLab’s Features panel. Turkish locals must not collide with the default. Arabic substitutions must fire in the right order or the word disconnects mid-air. Fractions need to look intentional, not like two numbers shoved together by gravity. The editor handles the bookkeeping; the designer decides what good behaviour looks like.

For the underlying logic, [Simon Cozens’ *Fonts and Layout*](https://simoncozens.github.io/fonts-and-layout/opentype.html) is the clearest plain-English account, with companion chapters on [features](https://simoncozens.github.io/fonts-and-layout/features.html) and [localisation](https://simoncozens.github.io/fonts-and-layout/localisation.html). Microsoft’s [feature tag registry](https://learn.microsoft.com/en-us/typography/opentype/spec/featuretags), [small-caps feature notes](https://learn.microsoft.com/en-us/typography/opentype/spec/features_pt#tag-smcp), and [spec overview](https://learn.microsoft.com/en-us/typography/opentype/spec/overview) are the receipts. FontLab’s own [FontLab 8 OpenType features tutorial](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-4-clever/#opentype-features-empowering-your-font-in-fontlab-8) shows where those rules get written, tested, compiled, and exported.

Good manners are invisible. Bad manners ruin dinner.

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-4-clever/#opentype-features-empowering-your-font-in-fontlab-8)
