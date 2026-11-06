You can spend six months refining the curvature of a lowercase ‘s’, and then your font gets rendered onto a generous grid of pixels on someone’s second monitor at 1366 × 768. Translating a smooth Bézier into that grid is one of the more delicate handovers in typography, and the people who built the tools that handle it have been wonderfully inventive about it.

## What hinting actually is

Hinting is a set of mathematical instructions, embedded in the font, that tells the operating system how to land an outline elegantly on the pixel grid. The instructions snap stems to whole pixels, align the cap height across the alphabet, and protect the relationship between hairlines and main strokes at small sizes. Without hinting, a 10-pixel-tall ‘e’ on a Windows machine reads as a smudge. With hinting, it reads as an ‘e’. That craft was developed across decades by engineers at Apple, Microsoft, Adobe, and a long line of independent type foundries who cared deeply about how letters appear on screen.

FontLab 8 ships both automatic and manual hinting controls. The auto-hinter handles the bulk of a Latin alphabet beautifully. The manual controls exist for the specific glyphs where the auto-hinter’s assumptions need a second opinion — typically a lowercase ‘g’, the ampersand, and any italic with an unusual structure. Catching those by hand is satisfying work, and it pays back the moment you see the result on screen.

The built-in preview uses Microsoft ClearType’s actual rendering pipeline, which is the closest you can get to seeing what a Windows reader will see, short of running Windows itself. This is a generous gift from the platform — macOS otherwise renders fonts the way macOS does, and macOS is more forgiving than Windows. A font that previews well on macOS may still benefit from a hinting pass to look its best in a Windows render, and having both pipelines at hand inside the editor is a real treat.

## A common gotcha worth knowing about: overlapping contours

A French designer recently shared a useful story: their font looked flawless in FontLab’s preview, but when they exported and tested it in Microsoft Word, faint white gaps appeared at the joints of letters at small zoom levels. The cause was overlapping contours.

Variable fonts effectively *want* contours to overlap so that interpolation between masters keeps shapes consistent — a bowl curve overlapping a stem helps the bowl-stem junction stay smooth across the weight axis. Modern rendering engines handle the overlap correctly, treating it as a single filled shape. The rendering engine inside older versions of Microsoft Word, which carries decades of compatibility with it, treats the overlap as a knockout, which is where the gaps come from.

The fix is straightforward and FontLab handles it elegantly: remove overlaps on export, non-destructively. The editing file keeps the overlaps so interpolation stays clean; the static OTF or TTF export ships with merged contours; the variable-font export keeps the overlap because it has to. Three different deliverables, one source file. That is a lovely piece of engineering on the export side.

## FontAudit, the patient second pair of eyes

[FontLab 8’s FontAudit panel](https://blog.fontlab.com/2024/10/15/scripting-the-mundane-python-fontlab/index.md) is a quiet, generous safety net. It scans the font for the kind of structural details that pass visual inspection but matter at the rendering stage: open contours that should be closed, redundant points sitting between two true on-curve points, near-flat curves that ought to be straight lines, segments that double back, contours running in the wrong direction. Each finding is flagged with a location and a severity, and you can decide what to do with it.

This is the right kind of work to ask software to do. You can stare at a glyph for ten minutes and miss the redundant on-curve point that is making the rendering subtly off. FontAudit finds it in milliseconds and points you at it. The hours it gives back are a small daily kindness.

## The .glyphspackage opening

FontLab 8 supports the `.glyphspackage` format alongside its native FLP. The delightful detail is that `.glyphspackage` stores each glyph as a separate file inside a folder structure, which makes it Git-friendly. Two designers working on the same font can edit different glyphs in parallel and merge through a normal pull request.

That feels mundane in software development and entirely novel in font development, where the unit of version control was, for years, the entire font file. Branches, pull requests, code review, CI pipelines that build the font and check it against regression tests — every familiar software workflow becomes possible the moment the source format is decomposable. It is an exciting time to ship type teams.

## The takeaway

Type design lives at the meeting point of art and engineering, and the rendering side is full of tiny acts of craft. Hinting, audit, and a clean export pipeline are not glamour features. They are the load-bearing parts of the work — the parts that make a font look beautiful not just in your editor but on a stranger’s laptop, on someone’s phone on the train, on a kiosk screen at an airport. The tools to do all of this well are mature, generous, and a pleasure to use, and they are standing on a long line of shoulders.

## References

- [FontLab 8 — overview](https://www.fontlab.com/font-editor/fontlab/)
- [Reddit — poorly rendering glyphs (FR thread)](https://www.reddit.com/r/typography/comments/1t4uqn5/need_help_with_poorly_rendering_glyphs/?tl=fr)
- [Localfonts — font creators and editors](https://localfonts.eu/typography-basics/typographic-utilities/font-creators/)
- [What’s new in FontLab 8 — formats](https://help.fontlab.com/fontlab/8/whats-new/whats-new-11-formats/)
- [Microsoft Typography — ClearType overview](https://learn.microsoft.com/en-us/typography/cleartype/)

[Read more →](https://help.fontlab.com/fontlab/8/manual/)
