---
date:
  created: 2013-10-10
title: "The four color-font proposals: APP, COLR/CPAL, CBDT/CBLC, and SVG"
authors: [adam]
draft: false
---
Apple, Google, Microsoft, and Adobe/Mozilla each approached the color font problem differently in 2013. This post examines the four proposals in technical detail. We look at their table structures, co-existence characteristics, fallback behavior, and open questions based on early implementations.

<!-- more -->

*Note: This article is highly technical. The views presented are personal.*

## Detailed discussion of approaches

### GOO: Google `CBDT`/`CBLC` tables

Google uses bitmap-based (PNG) glyphs. Announced in May 2013, this approach specifies two tables (`CBDT` and `CBLC`) that extend the existing OpenType `EBDT` and `EBLC` tables to include uncompressed color images or PNGs. FreeType 2.5 includes support for this format.

* **Co-existence:** Google recommends omitting the `glyf` table, making these bitmap-only fonts. This raises questions about co-existence. In traditional TrueType rasterizers, if a bitmap strike was available for a given PPM, it was used. Otherwise, the outline glyph rendered from the `glyf` table. Platforms supporting the Google approach should adopt this principle. This would allow a single font to include `CBDT`, `CBLC`, `COLR`, `CPAL`, and `glyf` tables.
* **External modification:** Manipulating embedded colors for PNG-based glyphs should be a post-processing step.
* **Fallback:** The specification includes provisions for transforming color bitmap data into grayscale.
* **Unclear:** The proposal makes no mention of how scaling should be implemented or whether a scaler should rely on the `EBSC` table. If this proposal aims for wider adoption, it should strictly follow the OpenType specification.

### APP: Apple `sbix` table

Apple also uses bitmap-based (PNG) glyphs, implemented as scalable bitmap glyphs with multiple master strikes per PPM. This was the first implementation officially deployed, appearing in iOS 4 and Mac OS X 10.7.

The implementation hosts PNG data inside the `sbix` table. The scaler chooses the most appropriate PPM size and scales it as needed. For metrics, it relies on bounding boxes stored in the `glyf` table. Unfortunately, Apple's implementation renders the contents of a `glyf` table glyph and then renders its associated bitmap on top. This means if bitmaps are available in the `sbix` table, the corresponding `glyf` slot must be empty.

* **Co-existence:** The requirement for empty `glyf` glyphs prevents co-existence with the Microsoft approach.
* **External modification:** Like the Google approach, color manipulation should be a post-processing step.
* **Fallback:** There are no clear provisions for fallback or degradation. A renderer could fall back to grayscale, but falling back to proper outline glyphs is impossible due to the empty `glyf` requirement.
* **Unclear:** It is not entirely clear how a renderer should make use of the PPM and DPI information.

### MIC: Microsoft `COLR`/`CPAL` tables

Microsoft introduced a simple and clever approach in Windows 8.1. It adds lightweight `COLR` and `CPAL` tables, resulting in layered outline glyphs with one solid fill per layer.

This approach uses a base glyph (`glyf` or `CFF`) for non-color situations. The `COLR` table refers from this base glyph to other outline glyphs that serve as layers. Each layer has its own z-order and a single color reference. The `CPAL` table resolves the RGBA colors.

* **Co-existence:** This approach can easily co-exist with the Google approach. A platform could prioritize the Microsoft approach with a fallback to `glyf`, or prioritize the Google approach with a fallback to Microsoft, and finally to `glyf`.
* **External modification:** Fonts can have multiple palettes. Currently, colors are defined by the font developer. Future updates might allow applications to expose palette selection to users.
* **Fallback:** This approach degrades nicely to the base outline glyph.

### SVG: Joint Adobe and Mozilla `SVG` table

This proposal offers full outline and bitmap (SVG) glyphs with possible animation. Submitted to the W3C, it is implemented in Firefox behind a configuration flag.

This is the most complex proposal. It requires a full SVG renderer. However, once an application has access to the SVG renderer, it can delegate glyph rendering completely. The application only needs to call an OpenType Layout library for positioning.

The SVG proposal allows for designs unachievable by other solutions. It supports rich colors, gradients, various strokes, and intermixing vectors with bitmaps.

* **Co-existence:** This approach can co-exist with all previous ones. A potential benefit is co-existence with the Microsoft `CPAL` table. SVG glyphs could reference color palettes specified within `CPAL`. If consuming platforms implement external palette manipulation, both the Microsoft and SVG approaches would benefit. Sairus Patel mentioned he might propose extensions to the Microsoft CPAL table and drop the color palette format proposed in the SVG spec. Ultimately, both formats could use the CPAL table.

Read more on help.fontlab.com →{ .fl-help-cta }