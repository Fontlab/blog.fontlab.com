---
this_file: src_docs/md/posts/2026-03-03-gsub-gpos-and-harfbuzz.md
title: "GSUB, GPOS, and HarfBuzz: the machinery under OpenType"
authors: [fontlab]
tags: [fontlab-8, opentype, harfbuzz, gsub, gpos, shaping]
date:
  created: 2026-03-03
slug: gsub-gpos-and-harfbuzz
---
![](../media/illu/gsub-gpos-and-harfbuzz-2.png){.illu-thumb }

Every OpenType feature — ligatures, kerning, small caps, Arabic joining forms — runs through two tables and one engine. Most type designers know the features exist. Fewer know what the tables look like from the inside.

<!-- more -->

**GSUB** substitutes glyphs. `f` followed by `i` becomes `fi`. `1/2` becomes ½. An Arabic isolated form becomes a medial form depending on its neighbours. **GPOS** positions them — kerning between pairs, mark attachment so combining accents land correctly, cursive connection so joined scripts flow. Both tables share the same architectural layout:

ScriptList → FeatureList → LookupList

The ScriptList identifies the writing system — Latin, Arabic, Devanagari. The FeatureList names the behaviours an application can ask for: `liga` for standard ligatures, `kern` for kerning, `mark` for mark-to-base positioning. The LookupList contains the actual rules — the substitution tables, the value records, the coverage arrays that say which glyphs the rule applies to.

This three-tier structure is not incidental. It means the same font can behave differently for different scripts, different languages, and different feature selections — all from one set of tables. The `locl` feature fires language-specific substitutions: the same Unicode codepoint for dotless-i renders differently under a Turkish locale tag. The rules fire in Lookup order, and that order is the font designer’s responsibility to get right.

**HarfBuzz** — Persian حرف‌باز, literally “open type” — is the shaping engine that walks those tables and produces the run of positioned glyphs an application then draws. It is what Chrome, Firefox, Android, GNOME, LibreOffice, Flutter, and Unreal Engine all use. Behdad Esfahbod began rewriting it in C++ in 2005 from an earlier C codebase; the harfbuzz-ng rewrite stabilised around 2012 with Mozilla’s Jonathan Kew contributing core work. Esfahbod received the 2013 O’Reilly Open Source Award. Most of the world’s user-facing text in 2026 passes through this library; most of the people whose text passes through it have never heard of it.

For variable fonts there is one mechanism worth knowing specifically: **FeatureVariations**. It lets a font apply a different GSUB lookup at different points in the design space. A light-weight instance and a black-weight instance can substitute different glyphs — a higher-contrast shape at the heavy end, a more open form at the light end — and the substitution happens as part of shaping, not as a separate styling step. It is the correct way to encode design decisions that differ across the weight axis, and it is under-used.

The pragmatic point: GSUB and GPOS errors live at the rendering boundary. A feature that looks correct in FontLab’s preview may shape wrong in HarfBuzz, because the preview and HarfBuzz may not execute the same lookup chain. The honest test is to render through the same shaper Chrome will use.

The tool for that is `hb-shape`, a command-line utility that ships with HarfBuzz:

```bash
hb-shape --font-file=myfont.ttf --features=liga,kern "fi 1/2"
```

It outputs the glyph IDs, advance widths, and offsets HarfBuzz produces for that input string. When a ligature isn’t forming, or a kern pair is the wrong value, or an Arabic word is breaking in the wrong place, `hb-shape` tells you what the shaper actually received and what it actually returned. It solves an enormous category of bugs in a single step.

## References

- [OpenType GSUB table — Microsoft](https://learn.microsoft.com/en-us/typography/opentype/spec/gsub)
- [OpenType GPOS table — Microsoft](https://learn.microsoft.com/en-us/typography/opentype/spec/gpos)
- [Why do I need a shaping engine? — HarfBuzz](https://harfbuzz.github.io/why-do-i-need-a-shaping-engine.html)
- [Fonts and Layout for Global Scripts — Simon Cozens](https://simoncozens.github.io/fonts-and-layout/features.html)
- [OpenType feature tags registry — Microsoft](https://learn.microsoft.com/en-us/typography/opentype/spec/featuretags)

[Read more →](https://www.fontlab.com/font-editor/fontlab/){ .fl-help-cta }
