---
date:
  created: 2013-11-07
title: "Color font concepts: layers, palettes, scaling, and finiteness"
authors: [adam]
draft: false
---

With four competing color font proposals on the table in 2013, we need to step back and examine their foundational concepts. Their individual advantages and blind spots reveal the broader challenge of adding color to OpenType. This post covers palettes as a third typographic user control mechanism, the analogy between color font formats and display color history, co-existence with existing OpenType glyph sources, and the underappreciated virtue of a format that clearly defines its own limits.

<!-- more -->

*Note: This article is highly technical. The views presented are personal.*

## The proposals

Each approach has distinct advantages and drawbacks.

* **APP (Apple `sbix`)**: Already implemented in Apple OSes and FreeType. It uses PNGs for complex fills but fails in high-resolution scenarios. The interaction between `sbix` and `glyf` tables lacks a fallback scenario. Its scope is vaguely defined, allowing anything from PNGs to movie clips. This open-ended nature can be daunting for developers.
* **MIC (Microsoft `COLR`/`CPAL`)**: Focuses on multilayer outline glyphs with solid fills. It scales perfectly and allows precise hinting. While limited to flat colors, it defines its scope cleanly.
* **GOO (Google `CBDT`/`CBLC`)**: Also uses PNGs for complex fills and is supported by FreeType. It plugs directly into the existing embedded bitmap infrastructure. It is a self-limiting format that does one thing very well. However, its insistence on excluding the `glyf` table is an unnecessary limitation.
* **SVG (Mozilla/Adobe SVG in `SFNT`)**: Delivers rich color and complex vector graphics. It requires a smart rasterizer and does not offer hinting. Firefox already implements this approach. It is a stable proposal because it delegates the heavy lifting to the existing SVG standard.

In principle, the MIC and GOO approaches could marry well. MIC handles scalable solid fills, while GOO manages refined bitmaps with clear fallback scenarios.

## Color palettes

Adding color palettes to font formats acts as the **third element of typographic user control**.

1. **Character mapping (`cmap`)**: The user enters Unicode characters and picks a size. The font does the rest.
2. **OpenType Layout (`GSUB`/`GPOS`)**: The user specifies layout features to apply to the text.
3. **Color palettes (`CPAL`)**: The user selects multiple colors from the font's predefined palette.

## Relation to existing solutions

The evolution of color font formats mirrors the history of computer displays.

* **Black-and-white monitors**: Analogous to current monochrome font formats.
* **16 to 256 colors (GIF)**: Flat color implementation, exactly like the MIC proposal.
* **16 million colors (JPG/PNG)**: Rich color applications, analogous to the SVG proposal.

Before color fonts, OpenType peacefully hosted three separate glyph sources. Embedded bitmaps handled monochrome or grayscale pixels. TrueType outlines offered precise hinting control. PostScript outlines provided complex structural features.

We expect a similar peaceful co-existence for color proposals. Each has merits. None is sufficient on its own. GOO extends embedded bitmaps. MIC extends TrueType outlines. SVG acts as a cousin to PostScript outlines. In fact, GOO serves as an ideal fallback for SVG. Complex SVG graphics can be pre-rendered into `CBDT`/`CBLC` tables to support older environments.

## Finiteness

A format's "finiteness" matters. Developers need to know if a format's limits are clearly defined. An infinitely extensible structure poses risks. Developers want to implement a standard and move on.

* **GOO** is the best example of a self-limiting format. It extends existing bitmap formats with a few new subformats and stops there.
* **APP** limits itself vaguely. The `sbix` table can host PNG, TIFF, JPEG, SVG, PDF, or even MOV clips. This open-ended nature makes full implementation difficult.
* **MIC** cleanly defines its current scope with `CPAL` and `COLR`.
* **SVG** is ambitious graphically but clearly limited structurally. It defines a container and delegates everything else to the SVG standard.

## Support in FontLab apps

FontLab fully supports this evolution.

* **FontLab Pad**: A free app for Mac and Windows that lets users type with color fonts. It currently supports APP and MIC formats.
* **TransType 4**: Creates MIC-compatible fonts by overlaying existing layered fonts and assigning colors. It also outputs APP-compatible fonts.
* **BitFonter 3**: Works with TransType 4 to produce sophisticated full-bitmap color fonts in the APP format.

Our upcoming font editors will support multicolor fonts natively. You will be able to create fonts in all color formats, including SVG, with layers and complex fills.

Read more on help.fontlab.com →{ .fl-help-cta }