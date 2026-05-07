---
date:
  created: 2013-09-19
title: "Color fonts: overview of proposals for color extensions of OpenType"
authors: [adam]
draft: false
---
In 2013, Apple, Google, Microsoft, and Adobe with Mozilla each proposed a different way to add color to OpenType fonts. None of them agreed. The proposals range from simple PNG bitmaps to layered solid-color outlines to full SVG with potential animation. This post summarizes the conceptual landscape and the four approaches.

<!-- more -->

*Note: This article gets technical. The views are personal, and the information might not be perfectly complete.*

<img src="https://i.ytimg.com/vi/Yit1ZpClwAk/maxresdefault.jpg" class="epyt-facade-poster skip-lazy" decoding="async" data-spai-excluded="true" loading="lazy" alt="Color fonts. The next big thing? FontLab tutorial with Adam Twardoch" />

![](data:image/svg+xml;base64,PHN2ZyBkYXRhLW5vLWxhenk9IjEiIGhlaWdodD0iMTAwJSIgdmVyc2lvbj0iMS4xIiB2aWV3Ym94PSIwIDAgNjggNDgiIHdpZHRoPSIxMDAlIj48cGF0aCBjbGFzcz0icGFyYSIgZD0iTTY2LjUyLDcuNzRjLTAuNzgtMi45My0yLjQ5LTUuNDEtNS40Mi02LjE5QzU1Ljc5LC4xMywzNCwwLDM0LDBTMTIuMjEsLjEzLDYuOSwxLjU1IEMzLjk3LDIuMzMsMi4yNyw0LjgxLDEuNDgsNy43NEMwLjA2LDEzLjA1LDAsMjQsMCwyNHMwLjA2LDEwLjk1LDEuNDgsMTYuMjZjMC43OCwyLjkzLDIuNDksNS40MSw1LjQyLDYuMTkgQzEyLjIxLDQ3Ljg3LDM0LDQ4LDM0LDQ4czIxLjc5LTAuMTMsMjcuMS0xLjU1YzIuOTMtMC43OCw0LjY0LTMuMjYsNS40Mi02LjE5QzY3Ljk0LDM0Ljk1LDY4LDI0LDY4LDI0UzY3Ljk0LDEzLjA1LDY2LjUyLDcuNzR6IiBmaWxsPSIjZjAwIiAvPjxwYXRoIGQ9Ik0gNDUsMjQgMjcsMTQgMjcsMzQiIGZpbGw9IiNmZmYiIGNsYXNzPSJwYXJhIiAvPjwvc3ZnPg==)

<span itemprop="video" itemscope="" itemtype="http://schema.org/VideoObject"></span>

Adam Twardoch's video tutorial accompanies this article. It offers a practical take on color font creation.

## Concepts

You can approach color fonts in several ways. Here they are, from simple to complex:

*   **Per-PPM bitmap strikes**, without any scaling.
*   **Scalable bitmap glyphs** with multiple master PPM sizes.
*   **One scalable bitmap glyph** definition across all PPMs.
*   **Layered outline glyphs**, with one solid fill per layer.
*   **Static outline glyphs** with complex fills and optional bitmap content.
*   **Animated variants** of static outline glyphs.

## Approaches

The major vendors offer four distinct approaches. They scale in complexity:

*   **Google (`CBDT`/`CBLC`)**: Uses per-PPM or scalable bitmaps.
*   **Apple (`sbix`)**: Uses scalable bitmap glyphs.
*   **Microsoft (`COLR`/`CPAL`)**: Uses layered outline glyphs.
*   **Adobe and Mozilla (`SVG`)**: Uses static outline glyphs, possibly expandable to animation.

## Considerations

Each implementation must address several core issues:

*   **Co-existence**: Can multiple approaches live in the same `SFNT` font file? We need to know what happens if a platform supports multiple formats. We also need to know if formats can share structures like PNG image data or color palettes. Co-existence with the existing `glyf` or `CFF` table is critical.
*   **External modification**: Can the consuming platform change the colors specified in the font file? This matters for outline approaches. It includes controlling animation in SVG formats or interacting with the document DOM in a web browser.
*   **Fallback and degradation**: How should color data appear in grayscale or monochrome environments? Adobe's Leonard Rosenthol raised fundamental issues about this during the SVG discussion. The "Glyph bbox concerns" threads offer good background reading: [Thread 1](http://lists.w3.org/Archives/Public/public-svgopentype/2012Jun/thread.html) and [Thread 2](http://lists.w3.org/Archives/Public/public-svgopentype/2012Aug/thread.html).

## More on color fonts

*   [The four color-font proposals: APP, COLR/CPAL, CBDT/CBLC, and SVG](2013-10-10-color-font-proposals-detailed.md)
*   [Color font concepts: layers, palettes, scaling, and finiteness](2013-11-07-color-font-concepts.md)

Read more on help.fontlab.com →{ .fl-help-cta }