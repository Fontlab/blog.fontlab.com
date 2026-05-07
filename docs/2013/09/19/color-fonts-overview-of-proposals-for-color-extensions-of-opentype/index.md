In 2013, all four major players — Apple, Google, Microsoft, and Adobe with Mozilla — each proposed a different way to add color to OpenType fonts, and none of them agreed. The proposals range from simple PNG bitmaps (Apple's `sbix`, Google's `CBDT`/`CBLC`) to layered solid-color outlines (Microsoft's `COLR`/`CPAL`) to full SVG with potential animation (Adobe/Mozilla's `SVG` table). This post summarises the conceptual landscape and the four approaches at a high level.

*This article is very technical. No completeness or correctness of the information presented below is guaranteed, and all views are personal.*

The video tutorial by Adam Twardoch accompanies this article with a more practical take on color font creation.

## Concepts

Several conceptual approaches for "color fonts" are possible, in increasing order of complexity:

- a\] per-PPM bitmap strike definition, without any scaling
- b\] scalable bitmap glyphs with multiple "master PPM sizes"
- c\] one scalable bitmap glyph definition across all PPMs
- d\] layered outline glyphs, one solid fill per layer
- e\] static outline glyphs with complex fills and optional bitmap content
- f\] animated variant of e\]

## Approaches

Four distinct approaches from the major vendors, in increasing order of complexity:

- GOO: Google `CBDT`/`CBLC` tables — a\] or b\], unclear
- APP: Apple `sbix` table — b\] concept
- MIC: Microsoft `COLR`/`CPAL` tables — d\] concept
- SVG: Joint Adobe and Mozilla `SVG` table — e\] concept, possibly expandable to f\]

## Considerations

Each implementation needs to address several aspects:

- **Co-existence**: whether several approaches can co-exist within the same `SFNT` font file, including questions of precedence (what happens if a consuming platform supports multiple approaches) and structure sharing (whether the same structure, e.g. the PNG image data or a color palette, can be shared by multiple approaches). Co-existence with the existing `glyf` or `CFF` table is especially important.
- **External modification**: especially with the outline approaches, whether the colors specified within the font file can be manipulated externally by the consuming platform. This includes controlling animation in SVG-based approaches or, if the consuming platform is a web browser, interaction with the document's DOM.
- **Fallback/degradation**: related to co-existence, how the color data should be represented in environments that only support grayscale or monochrome. Adobe's Leonard Rosenthol raised a number of fundamental issues on this in the context of the SVG discussion. The "Glyph bbox concerns" thread makes an interesting read: [1] and [2].
- [1] [http://​lists​.w3​.org/​A​r​c​h​i​v​e​s​/​P​u​b​l​i​c​/​p​u​b​l​i​c​-​s​v​g​o​p​e​n​t​y​p​e​/​2​0​1​2​J​u​n​/​t​h​r​e​a​d​.​h​tml](http://lists.w3.org/Archives/Public/public-svgopentype/2012Jun/thread.html)
- [2] [http://​lists​.w3​.org/​A​r​c​h​i​v​e​s​/​P​u​b​l​i​c​/​p​u​b​l​i​c​-​s​v​g​o​p​e​n​t​y​p​e​/​2​0​1​2​A​u​g​/​t​h​r​e​a​d​.​h​tml](http://lists.w3.org/Archives/Public/public-svgopentype/2012Aug/thread.html)

## More on color fonts

- [The four color-font proposals: APP, COLR/CPAL, CBDT/CBLC, and SVG](https://blog.fontlab.com/2013/10/10/the-four-color-font-proposals-app-colrcpal-cbdtcblc-and-svg/index.md)
- [Color font concepts: layers, palettes, scaling, and finiteness](https://blog.fontlab.com/2013/11/07/color-font-concepts-layers-palettes-scaling-and-finiteness/index.md)
