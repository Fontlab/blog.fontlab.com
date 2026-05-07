---
this_file: src_docs/md/posts/2023-01-09-8-days-bigger-bolder.md
title: "Eight days of FontLab — Day 6: bigger, bolder, better"
authors: [fontlab]
date:
  created: 2023-01-09
slug: 8-days-bigger-bolder
---
One font is a typeface.
A family of weights and widths is a tool.
Day 6 covers two things: how FontLab helps teams stay organized across a shared project,
and how to build font families — static and variable — using masters, interpolation, and
variation axes.

<!-- more -->

## Collaboration without chaos: flags, tags, notes, stickers

Type design doesn’t have to be a solo project.
But group work is hard when collaborators are in different time zones, all touching the
same file.

FontLab’s answer is to put communication inside the font.
Four tools:

**Flags** are color codes on glyph cells in the Font window.
Assign blue to one designer’s glyphs, green to another’s, red to glyphs needing review.
Everyone sees the project’s status at a glance.

**Tags** are labels that group glyphs logically — “linFig” for lining figures,
“smallcap” for small capitals.
Filter by tag in the Classes panel to work on a subset.
Tags also apply to font guides and zones, letting FontLab show guides only in glyphs
where they’re relevant.

**Notes** are free-text fields.
Per-font notes go in File › Font Info › Note.
Per-glyph notes appear under the glyph cell or via right-click > Edit Note.
A small yellow icon marks glyphs with notes so teammates spot them without opening every
glyph.

**Stickers** are visual annotations inside the Glyph window — circles, arrows, text
callouts pointing to specific areas of the drawing.
Activate the Guides tool to add them.
Useful for “perhaps too bold here” or “descender should reach −30”.

None of this data goes into the exported OpenType font.
It’s for your team, not your users.

## From single weight to type family

Most fonts have family members: Bold, Italic, Condensed, ExtraLight.
Each style is a *master* — a set of contours with the same point count arranged
differently. FontLab interpolates between masters to produce everything in between.

To prototype a condensed variant, open your Regular in FontLab.
Choose *Add Variations* from the Font menu, type “Condensed”, click OK. You now have a
Width axis and two identical masters.
Select some glyphs, open *Tools > Actions*, find *Change width* in the Adjust section,
apply it to the Condensed master only.
Select all glyphs, run *Match Masters*. You have variation.

Variation enables two kinds of output:

**Static font families** — predetermined points along each axis.
Users get Light, Regular, Bold, and choose among them.
Every app supports this.

**Variable fonts** — a single file that lets users slide continuously between any
positions on each axis.
A typesetter can pick exactly the weight that fills a column, without accepting the
nearest static style.
Export with *Variable TT* to produce this format.
Variable fonts work in Adobe InDesign CC 2020 and later, among many other apps.

The math is simpler than it sounds.
Make a Regular and a Bold (or a Regular and a Condensed).
FontLab interpolates anything in between — Medium, Semibold — and extrapolates outward
to Light or Black. Produce all of those as static instances, or fold the whole family
into one variable file.
Assign names to each instance in Font Info › Instances.

A complete family handles every situation.
Headlines, body text, captions, tight layouts, loose ones — a well-built family adapts.

* * *

## More in this series

1. [Day 1: Start making fonts](2022-08-15-8-days-start.md)
2. [Day 2: A-B-C](2022-09-12-8-days-abc.md)
3. [Day 3: Beyond A-B-C](2022-10-10-8-days-beyond-abc.md)
4. [Day 4: Clever fonts](2022-11-07-8-days-clever.md)
5. [Day 5: Letter crowd](2022-12-05-8-days-letter-crowd.md)
6. **Day 6: bigger, bolder, better** (this post)
7. [Day 7: Beyond text](2023-02-13-8-days-beyond-text.md)
8. [Day 8: Color is the new black](2023-03-13-8-days-color.md)
