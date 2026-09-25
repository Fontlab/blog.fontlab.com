OpenType features are the part of font design where text becomes typography. The FontLab TV OpenType episode walks through the feature tags you will actually use, what they do at runtime, and how to write them without breaking anything else.

> 📺 Watch: [Auto OpenType features in FontLab 7 on FontLab TV](https://www.youtube.com/watch?v=ehkuzMvmjbY)

## What it covers

**The features that matter most.**

- `kern` — pair kerning. Always on.
- `liga` — standard ligatures (`fi`, `fl`). Almost always on.
- `dlig` — discretionary ligatures (`st`, `ct`). User-toggled.
- `smcp` / `c2sc` — small caps from lowercase / from uppercase.
- `onum` / `lnum` / `tnum` / `pnum` — old-style / lining / tabular / proportional figures.
- `ss01`–`ss20` — stylistic sets. Twenty buckets for alternates.
- `salt` / `calt` — stylistic alternates / contextual alternates.
- `locl` — language-specific forms (Polish kreska, Catalan punt volat, Dutch IJ).

**FEA syntax, the practical bits.** The episode covers substitution rules (`sub a by a.alt;`), classes (`@uppercase = [A B C ...];`), context-sensitive rules (`sub a' b by a.alt;`), and lookup ordering. Most feature bugs come from the wrong feature firing first; FontLab’s compiler error messages and trace tools help.

**Compiling and testing.** FontLab has both a built-in compiler and round-trips with Adobe’s `makeotf`. The video shows the compile-test loop and the small set of system fonts (Adobe Fonts test pages, browser dev tools, OS font palettes) that surface feature bugs fastest.

**The mark and mkmk features briefly.** These are auto-generated from anchors, but you should still understand what they emit — they are often the source of “why is my accent in the wrong place” bugs.

## Why it matters

Almost every modern type design ships with at least a dozen OpenType features. Getting them right is what separates a “font” from a typography product.

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-4-clever/#opentype-features-empowering-your-font-in-fontlab-8)
