---
this_file: src_docs/md/posts/2025-08-26-calfonts-honing-letters.md
title: "Calfonts: honing letters from rough sketches to clean curves"
authors: [fontlab]
tags: [drawing, contours, beziers, refinement, fontlab-8]
date:
  created: 2025-08-26
slug: calfonts-honing-letters
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab/8/manual/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "50% handle = 'circle' tension claim — verify against Calfonts source"
    - "55–65% handle range as standard — verify against Calfonts material"
    - "Overshoot 1–2% of UPM — verify standard range"
  image_status: missing
  image_needs: "Screenshot of FontLab contour optimization tools or before/after honing example"
  weakness_verdict: keep
  consolidate_with: ""
  notes: "Practical and grounded; the three-sizes heuristic is the kind of advice that earns a bookmark. CTA URL is too generic — needs deep link to contour/honing chapter."
---
Honing is the part of font design between “I have a sketch” and “I have a glyph that
ships.” The Calfonts honing tutorial — adapted here — covers the boring, decisive 80% of
drawing: fixing paths automatically where you can, fixing them by hand where you must.

<!-- more -->

## Step 1: automatic path fixing

FontLab’s automatic tools resolve a surprising amount of contour mess:

- **Optimize contours** removes superfluous points without changing the shape.
- **Convert to TrueType / PostScript** rewrites curves in the target curve type cleanly.
- **Reverse path direction** fixes paths whose winding is wrong (outer counterclockwise,
  inner clockwise — or the reverse, depending on PostScript vs TrueType).
- **Heal openings and overlaps** fixes contours that have been broken by editing.

Run these first. They are fast, conservative, and remove the kind of contour debris that
makes hand-fixing harder than it needs to be.

## Step 2: fixing paths by hand

What automation can’t fix:

- **Visual proportions.** A counter that is too small.
  A bowl that is asymmetric in a way the design does not justify.
  The shoulder of `n` that meets the stem at a wrong angle.
- **Curve quality.** Inflection points where there shouldn’t be any.
  Bézier handles that don’t align with the curve direction at on-curve points (which
  produces a small but visible kink).
- **Spurious points.** Two on-curve points where one would do.
  Three points where two would do.
  The rule: if removing a point doesn’t change the shape, remove it.

The Calfonts heuristic is to look at every glyph at three sizes: the size you are
designing at (large), the intended use size (small), and a deliberately-too-large size
(200pt+). Different problems show at different sizes.

## Step 3: curve types and tension

The Calfonts material spends real time on curve tension — the question of how full or
how empty a curve looks at a given handle length.
A 50% handle (the so-called “circle” tension) makes a curve that looks like part of a
circle. Shorter handles produce flatter, more rectangular curves.
Longer handles produce ballooning curves that often look wrong.

Most letterforms want handles in the 55–65% range.
Going outside that range is a deliberate design choice; getting there by accident is a
bug.

## Step 4: optical adjustment

Curved letters need to overshoot straight ones — `o` extends slightly above and below
`n`. Diagonals (`v`, `w`, `y`) usually overshoot more than rounds.
These adjustments are tiny in number (1–2% of UPM) and enormous in effect.
The Calfonts tutorial recommends setting overshoot zones in FontLab so that the values
apply consistently across glyphs rather than being eyeballed per glyph.

## When honing is done

You stop honing when you cannot identify a specific change that would make the glyph
better. That is not “when you are tired of it” or “when the deadline arrives” — though
both happen. The Calfonts standard is the higher one.

[Read more →](https://help.fontlab.com/fontlab/8/manual/){ .fl-help-cta }
