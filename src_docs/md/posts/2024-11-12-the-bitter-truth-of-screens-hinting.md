---
this_file: src_docs/md/posts/2024-11-12-the-bitter-truth-of-screens-hinting.md
title: "The bitter truth of screens: testing and hinting"
authors: [fontlab]
tags: [hinting, fontaudit, rendering, opentype, fontlab-8]
date:
  created: 2024-11-12
slug: the-bitter-truth-of-screens-hinting
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab/8/manual/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "FL8 auto-hinter known-bad cases: 'lowercase g, ampersand, and italics' — verify this claim"
    - "Built-in preview uses Microsoft ClearType's actual rendering pipeline — verify technical accuracy"
    - ".glyphspackage stores each glyph as a separate file — confirm format spec"
    - "French designer white-gaps anecdote — flagged as illustrative; check it isn't fabricated"
  image_status: missing
  image_needs: "hinting panel or FontAudit panel screenshot from reference/fldoc/"
  weakness_verdict: keep
  consolidate_with: ""
  notes: "Covers hinting, FontAudit, overlapping contours, and .glyphspackage — arguably four posts squeezed into one; CTA should deep-link to hinting section."
---
You can spend six months agonising over the curvature of a lowercase ‘s’, and then your
font is rendered by a ruthless grid of pixels on somebody’s second monitor at 1366×768.
Translating smooth Bézier curves onto a low-resolution raster is a violent process.
The curves win the design argument.
The pixels win the rendering argument.

<!-- more -->

## What hinting actually is

Hinting is a set of mathematical instructions embedded in the font that tells the
operating system how to distort the outline so it lands properly on the pixel grid.
The instructions snap stems to whole pixels, align the cap height across the alphabet,
and keep the relationship between hairlines and main strokes legible at small sizes.
Without hinting, a 10-pixel-tall ‘e’ on a Windows machine in 2024 reads as a smudge.
With hinting, it reads as an ‘e’.

FontLab 8 ships both automatic and manual hinting controls.
The auto-hinter handles the bulk of a Latin alphabet acceptably; the manual controls
exist for the specific glyphs where the auto-hinter’s assumptions are wrong, which is
usually the lowercase ‘g’, the ampersand, and any italic that has structure the
auto-hinter is not expecting.

The built-in preview uses Microsoft ClearType’s actual rendering pipeline, which is the
closest you can get to seeing what a Windows user will see, short of running Windows.
This matters because the FontLab editor on macOS otherwise renders fonts the way macOS
renders them, and macOS is much more forgiving than Windows.
A font that previews well on macOS may still need hinting work to survive a Windows
render.

## The trap of overlapping contours

A French designer recently posted a typical horror story: their font looked flawless in
FontLab’s preview, but when they exported and tested it in Microsoft Word, white gaps
appeared at the joints of the letters at small zoom levels.
The culprit was overlapping contours.

This is the rendering-engine equivalent of the law of unintended consequences.
Variable fonts effectively *require* contours to overlap so that interpolation between
masters produces consistent shapes — the curves of the bowl have to overlap the stem to
keep the bowl-stem junction smooth across the weight axis.
Modern rendering engines handle the overlap correctly, treating it as a single filled
shape. The rendering engine buried inside Microsoft Word, which is several generations
old, does not. It interprets the overlap as a knockout — a transparent hole — and
produces white gaps at the junctions.

The fix is to remove overlaps on export.
FontLab does this non-destructively: the editing file keeps the overlaps so
interpolation works; the export produces a flattened static OTF or TTF whose contours
have been merged. The variable-font export keeps the overlap because it has to.

## FontAudit, the pedantic accountant

[FontLab 8’s FontAudit panel](/2024/10/15/scripting-the-mundane-python-fontlab/) is the
safety net most users do not know they have.
It scans the font for the kind of structural issues that pass visual inspection but fail
at the rendering stage: open contours that should be closed, unnecessary points sitting
between two true on-curve points, near-flat curves that ought to be straight lines,
segments that double back on themselves, contours running in the wrong direction.
Each finding gets flagged with a location and a severity.

The auditing role is the right one for software.
Visually, you can stare at a glyph for ten minutes and miss the redundant on-curve point
that is making the rendering subtly off.
FontAudit finds it in milliseconds and tells you exactly where it is.

## The .glyphspackage opening

FontLab 8 supports the `.glyphspackage` format alongside its native FLP. The interesting
thing about `.glyphspackage` is that it stores each glyph as a separate file inside a
folder structure, which makes it Git-friendly.
Two designers working on the same font can edit different glyphs in parallel and merge
the changes through a normal pull request.
This is mundane in software development; it is novel in font development, where for
years the unit of version control was the entire font file.

The implication is that font production starts to look like software production.
Branches, pull requests, code review, CI pipelines that build the font and check it
against regression tests — all of it becomes possible because the source format is
finally decomposable.

## The moral

Type design is an exercise in engineering as much as in art.
The drawing is the first half of the job.
Surviving the brutal reality of the screen is the second half.
Hinting, audit, and a clean export pipeline are not glamour features.
They are the difference between a font that looks beautiful in your editor and a font
that looks beautiful on a stranger’s laptop in 2024.

## References

- [FontLab 8 — overview](https://www.fontlab.com/font-editor/fontlab/)
- [Reddit — poorly rendering glyphs (FR thread)](https://www.reddit.com/r/typography/comments/1t4uqn5/need_help_with_poorly_rendering_glyphs/?tl=fr)
- [Localfonts — font creators and editors](https://localfonts.eu/typography-basics/typographic-utilities/font-creators/)
- [What’s new in FontLab 8 — formats](https://help.fontlab.com/fontlab/8/whats-new/whats-new-11-formats/)
- [Microsoft Typography — ClearType overview](https://learn.microsoft.com/en-us/typography/cleartype/)

[Read more →](https://help.fontlab.com/fontlab/8/manual/){ .fl-help-cta }
