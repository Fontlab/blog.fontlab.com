Italics are the part of a font family that most often gets shipped wrong — slanted romans, no cursive structure, lopsided ovals. The Calfonts italic tutorial walks through what it actually takes to draw an italic that earns its place next to the roman.

## What the italic is for

Italics do four jobs in real text:

1. **Emphasis.** Marking a word or phrase as important within roman text.
1. **Titles.** Book titles, ship names, foreign words.
1. **Voice change.** Inner monologue, quotation, stage direction.
1. **Hierarchy.** Distinguishing one level of a document outline from another.

All four require that the italic look distinctly different from the roman at the same size. A 12° slant is not enough to do that. The italic has to be structurally different.

## The structural changes that make an italic

**Single-storey `a` and `g`.** This is the single most-recognizable italic feature. The two-storey `a` and `g` are roman conventions; cursive `a` is a single bowl, cursive `g` has a single bowl with a tail.

**Narrower lowercase.** Italic letters are 5–10% narrower than their roman counterparts at the same size. Same x-height, same cap-height, less width. The texture of italic text is denser, which is part of how it reads as different from roman.

**Cursive entry and exit strokes.** `i`, `n`, `m`, `r`, `u` start with a small upstroke from the baseline. `e`, `i`, `n`, `m` end with a small upstroke into the next letter. These are vestiges of pen-on-paper writing, and they are what gives italic text its rhythm.

**Tipped contrast axis.** A broad-edged pen held at 40–50° (vs the roman 30°) produces a different stress on round letters. The thicks and thins move. Designing italic without thinking about the contrast axis produces ovals that are heavier on the wrong side.

## Drawing the italic

The Calfonts approach: draw the italic lowercase at 0° slant first. Get the structure right — single-storey letters, cursive strokes, narrower widths, correct contrast axis. Then apply slant as a transformation, usually 8–14°.

Doing it in the other order (slanting first, then trying to fix structure) almost always produces a worse result. The slant disguises structural problems just enough to make them hard to find.

## The capital question

Italic capitals have less leeway. They are usually slanted versions of the roman caps with mild structural touches — narrower proportions, sometimes a different `Q` tail or `J` foot. Full cursive capitals (swash caps) are a separate design layer, usually accessed through `swsh` or `salt` features.

## Verification

Set the italic next to the roman at text size — 9 to 11 point — and read a paragraph. The italic should look like a sibling of the roman, not a tilted twin. If the slant feels like a transformation rather than a design, something in the structure is still wrong.

Read more on help.fontlab.com →{ .fl-help-cta }
