---
this_file: src_docs/md/posts/2026-02-17-the-four-stack-of-screen-rendering.md
title: "The four-stack of screen rendering"
authors: [fontlab]
tags: [fontlab-8, rendering, hinting, screens, history]
date:
  created: 2026-02-17
slug: the-four-stack-of-screen-rendering
---
Most type designers know their fonts will be rendered differently on macOS and Windows.
Fewer know the names of the four pieces of plumbing responsible.
The names are worth knowing, because the plumbing shapes everything.

<!-- more -->

**ClearType.** Bill Gates announced it at COMDEX/Fall on 15 November 1998: *“a major
obstacle to ubiquitous on-screen reading… overcome.”* The technique exploited the
physical structure of LCD panels — each pixel is three coloured stripes, and by treating
each stripe as an independent sample, ClearType tripled horizontal rendering resolution
at the cost of slight colour fringing.
It was, for low-resolution screens, a genuine improvement.

Apple deprecated subpixel anti-aliasing in macOS Mojave in 2018. The reasoning was that
display resolutions had increased to the point where the fringing cost outweighed the
clarity gain. At 220 ppi, you don’t need the trick.
The core ClearType patents expired worldwide by August 2019.

**TextKit 2.** Introduced at WWDC 2021 by Donna Tom and Chris Willmore ("Meet TextKit
2"). It replaced TextKit 1, which had been part of OpenStep since the early 1990s —
meaning Apple’s text layout engine had been running on architecture from the NeXT era
through five major macOS versions.
TextKit 2 moves from a glyph-run model to a paragraph-graph model, which handles
bidirectional text and CJK layout substantially better.
It had already been powering TextEdit and AppKit text fields since macOS Big Sur in
2020; WWDC 2021 made it official.

Apple’s renderer has ignored TrueType hints since OS X. This is not a bug.
At high resolutions, the mathematical distortions that hinting imposes on outlines —
snapping stems to pixel boundaries, aligning cap heights — are more visible than the
pixel-grid problems they were designed to solve.

**DirectWrite + DWriteCore.** DirectWrite is the Windows text stack.
Colour font support arrived in stages: `COLR` in Windows 8.1, SVG/CBDT/sbix in the
Windows 10 Anniversary Update in 2016, full COLRv1 paint-tree support later.
DWriteCore — part of the Windows App SDK — extends DirectWrite cross-platform, making it
possible to ship a text application that renders identically on Windows and on other
systems that bundle it.

On Windows, hints are read and applied.
The same font that renders unhinted on macOS renders with its full TrueType instruction
set on Windows DirectWrite.

**ttfautohint.** Werner Lemberg’s open-source hinter.
Google Fonts adopted it in 2012 as the standard autohinting pipeline for fonts added to
the library.
It supports 22 scripts and, deliberately, only adds hints along the y-axis —
the vertical stems that most affect legibility at small sizes on Windows screens.
Lemberg’s scope choice is a design decision: y-axis hinting solves most of the problem
without the complexity and fragility of full TrueType hinting.

The practical consequence for a type designer is this: a face that hints itself
elegantly on Windows DirectWrite renders unhinted on macOS TextKit 2. Two different
stacks, two different assumptions, one font file.
Designing for both means trusting neither fully — which means testing on both, not
previewing on one and hoping.

## References

- [Microsoft announces ClearType — Microsoft News (1998)](https://news.microsoft.com/source/1998/11/15/microsoft-research-announces-screen-display-breakthrough-at-comdexfall-98/)
- [Meet TextKit 2 — WWDC 2021](https://developer.apple.com/videos/play/wwdc2021/10061/)
- [Apple text layout architecture evolution — atadistance.net](https://atadistance.net/2021/07/13/apple-text-layout-architecture-evolution-textkit-reboot/)
- [ttfautohint — freetype.org](https://freetype.org/ttfautohint/)
- [ClearType overview — Microsoft Typography](https://learn.microsoft.com/en-us/typography/cleartype/)

[Read more →](https://www.fontlab.com/font-editor/fontlab/){ .fl-help-cta }
