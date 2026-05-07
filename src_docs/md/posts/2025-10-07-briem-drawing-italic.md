---
this_file: src_docs/md/posts/2025-10-07-briem-drawing-italic.md
title: "Briem: how to draw an italic (and why the slanted-roman trap is real)"
authors: [fontlab]
tags: [italic, slant, cursive, drawing]
date:
  created: 2025-10-07
slug: briem-drawing-italic
---
Italic is not roman tilted to the right.
Slant your upright `a` and what you get is a tilted `a`, not an italic `a` — the
structure is wrong, the rhythm is wrong, the connection points are wrong.
Briem’s italic tutorial, lightly modernized, walks through what an italic actually is.

<!-- more -->

## What an italic is

Italics descend from cursive handwriting — letters drawn quickly with a broad-edged pen,
joined where joining was natural, simplified where simplification saved time.
The four hallmarks:

1. **Single-storey `a` and `g`.** The two-storey forms in roman are a printer’s
   invention. Cursive `a` is a single bowl; cursive `g` is a single bowl with a tail.
2. **Compressed lowercase.** Italic letters are narrower than their roman counterparts —
   most easily seen on `n`, `o`, `e`.
3. **Cursive entry and exit strokes.** `i`, `n`, `m`, `u` start from the baseline with a
   small upstroke, end with a small upstroke into the next letter.
   These are the connection points cursive writing demands.
4. **Slant.** The slant follows from holding the pen at a steeper angle while writing
   quickly. It is the most visible feature and the least important — most of italic’s
   character comes from the structural changes above.

## What slanted roman is

Take a roman `a`, apply a 12° transform, ship as Italic.
The result has:

- Two-storey `a` (wrong).
- Roman widths (too wide).
- No entry/exit strokes (no cursive rhythm).
- Curves that have been geometrically slanted, which produces lopsided ovals — the
  inside of every round letter looks heavier on one side than the other.

It is faster. It is also wrong, and any reader who reads italic regularly will feel the
wrongness without being able to name it.

## How to draw an italic that works

Start from the broad-pen logic.
Hold the pen at a steeper angle (40–50° from baseline rather than 30°). The contrast
axis tips with it, which is what produces the characteristic italic stress.

Draw the lowercase first, narrower than your roman lowercase by 5–10% at the same point
size. Use single-storey `a` and `g`. Add the entry and exit strokes — small but
consistent.

Slant comes last, often as a transformation applied late in the process to a
near-finished design.
Many italics ship with slants between 6° and 14°; some excellent italics ship with no
slant at all (true upright italics) and rely entirely on cursive structure.

## Practical exercise

Draw `i n o a` four times: once at 0° slant with cursive structure, once at 12° slant
with roman structure, once at 12° slant with cursive structure, once at 0° slant with
roman structure. Three of those four are wrong as italics.
Identify which one is right and what makes the other three feel off.

[Read more on help.fontlab.com →](https://help.fontlab.com/fontlab/8/tutorials/briem/4-3-italic/briem-4-31-italic/){
.fl-help-cta }
