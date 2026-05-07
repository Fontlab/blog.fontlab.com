---
date:
  created: 2013-09-19
title: "Color fonts: overview of proposals for color extensions of OpenType"
authors: [adam]
draft: false
---
In 2013, all four major players — Apple, Google, Microsoft, and Adobe with Mozilla —
each proposed a different way to add color to OpenType fonts, and none of them agreed.
The proposals range from simple PNG bitmaps (Apple’s `sbix`, Google’s `CBDT`/`CBLC`) to
layered solid-color outlines (Microsoft’s `COLR`/`CPAL`) to full SVG with potential
animation (Adobe/Mozilla’s `SVG` table).
This post summarises the conceptual landscape and the four approaches at a high level.

<!-- more -->

*This article is very technical.
No completeness or correctness of the information presented below is guaranteed, and all
views are personal.*

<img src="https://i.ytimg.com/vi/Yit1ZpClwAk/maxresdefault.jpg"
class="epyt-facade-poster skip-lazy" decoding="async" data-spai-excluded="true"
loading="lazy" alt="Color fonts.
The next big thing? FontLab tutorial with Adam Twardoch" />

![](data:image/svg+xml;base64,PHN2ZyBkYXRhLW5vLWxhenk9IjEiIGhlaWdodD0iMTAwJSIgdmVyc2lvbj0iMS4xIiB2aWV3Ym94PSIwIDAgNjggNDgiIHdpZHRoPSIxMDAlIj48cGF0aCBjbGFzcz0icGFyYSIgZD0iTTY2LjUyLDcuNzRjLTAuNzgtMi45My0yLjQ5LTUuNDEtNS40Mi02LjE5QzU1Ljc5LC4xMywzNCwwLDM0LDBTMTIuMjEsLjEzLDYuOSwxLjU1IEMzLjk3LDIuMzMsMi4yNyw0LjgxLDEuNDgsNy43NEMwLjA2LDEzLjA1LDAsMjQsMCwyNHMwLjA2LDEwLjk1LDEuNDgsMTYuMjZjMC43OCwyLjkzLDIuNDksNS40MSw1LjQyLDYuMTkgQzEyLjIxLDQ3Ljg3LDM0LDQ4LDM0LDQ4czIxLjc5LTAuMTMsMjcuMS0xLjU1YzIuOTMtMC43OCw0LjY0LTMuMjYsNS40Mi02LjE5QzY3Ljk0LDM0Ljk1LDY4LDI0LDY4LDI0UzY3Ljk0LDEzLjA1LDY2LjUyLDcuNzR6IiBmaWxsPSIjZjAwIiAvPjxwYXRoIGQ9Ik0gNDUsMjQgMjcsMTQgMjcsMzQiIGZpbGw9IiNmZmYiIGNsYXNzPSJwYXJhIiAvPjwvc3ZnPg==)

<span itemprop="video" itemscope="" itemtype="http://schema.org/VideoObject"></span>

The video tutorial by Adam Twardoch accompanies this article with a more practical take
on color font creation.

## Concepts

Several conceptual approaches for “color fonts” are possible, in increasing order of
complexity:

- a\] per-PPM bitmap strike definition, without any scaling
- b\] scalable bitmap glyphs with multiple “master <span class="caps">PPM</span> sizes”
- c\] one scalable bitmap glyph definition across all PPMs
- d\] layered outline glyphs, one solid fill per layer
- e\] static outline glyphs with complex fills and optional bitmap content
- f\] animated variant of e\]

## Approaches

Four distinct approaches from the major vendors, in increasing order of complexity:

- <span class="caps">GOO</span>: Google `CBDT`/`CBLC` tables — a\] or b\], unclear
- <span class="caps">APP</span>: Apple `sbix` table — b\] concept
- <span class="caps">MIC</span>: Microsoft `COLR`/`CPAL` tables — d\] concept
- <span class="caps">SVG</span>: Joint Adobe and Mozilla `SVG` table — e\] concept,
  possibly expandable to f\]

## Considerations

Each implementation needs to address several aspects:

- **Co-existence**: whether several approaches can co-exist within the same `SFNT` font
  file, including questions of precedence (what happens if a consuming platform supports
  multiple approaches) and structure sharing (whether the same structure, e.g. the
  <span class="caps">PNG</span> image data or a color palette, can be shared by multiple
  approaches). Co-existence with the existing `glyf` or `CFF` table is especially
  important.
- **External modification**: especially with the outline approaches, whether the colors
  specified within the font file can be manipulated externally by the consuming
  platform. This includes controlling animation in SVG-based approaches or, if the
  consuming platform is a web browser, interaction with the document’s
  <span class="caps">DOM</span>.
- **Fallback/degradation**: related to co-existence, how the color data should be
  represented in environments that only support grayscale or monochrome.
  Adobe’s Leonard Rosenthol raised a number of fundamental issues on this in the context
  of the <span class="caps">SVG</span> discussion.
  The “Glyph bbox concerns” thread makes an interesting read:
  \[<span class="numbers">1</span>\] and \[<span class="numbers">2</span>\].
- \[<span class="numbers">1</span>\]
  <a href="http://lists.w3.org/Archives/Public/public-svgopentype/2012Jun/thread.html" rel="nofollow">http://​lists​.w<span class="numbers">3</span>​.org/​A​r​c​h​i​v​e​s​/​P​u​b​l​i​c​/​p​u​b​l​i​c​-​s​v​g​o​p​e​n​t​y​p​e​/​<span class="numbers">2</span>​<span class="numbers">0</span>​<span class="numbers">1</span>​<span class="numbers">2</span>​J​u​n​/​t​h​r​e​a​d​.​h​tml</a>
- \[<span class="numbers">2</span>\]
  <a href="http://lists.w3.org/Archives/Public/public-svgopentype/2012Aug/thread.html" rel="nofollow">http://​lists​.w<span class="numbers">3</span>​.org/​A​r​c​h​i​v​e​s​/​P​u​b​l​i​c​/​p​u​b​l​i​c​-​s​v​g​o​p​e​n​t​y​p​e​/​<span class="numbers">2</span>​<span class="numbers">0</span>​<span class="numbers">1</span>​<span class="numbers">2</span>​A​u​g​/​t​h​r​e​a​d​.​h​tml</a>

## More on color fonts

- [The four color-font proposals: APP, COLR/CPAL, CBDT/CBLC, and SVG](2013-10-10-color-font-proposals-detailed.md)
- [Color font concepts: layers, palettes, scaling, and finiteness](2013-11-07-color-font-concepts.md)
