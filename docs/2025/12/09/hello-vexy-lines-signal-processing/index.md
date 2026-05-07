The boundary between a letterform and an illustration is a human invention. To a computer, both are coordinates plotted on a grid.

Vexy Lines, released in December 2025, leans into that observation. It is, fundamentally, a signal-processing engine for images. You give it a raster — a high-contrast photograph, a pencil sketch, an AI-generated noise field — and it analyses the luminance, then draws mathematically precise lines, dots, or strokes to recreate the picture in pure vector.

The pipeline is direct. Source image becomes a luminance heatmap. The heatmap drives stroke weight, dot size, or text weight. Darker regions command thicker geometry; lighter regions get fine, restrained marks. The output is print-ready SVG that scales infinitely, recolours cleanly, and exports to PDF without losing fidelity.

A dozen distinct fill styles ship in the first release. Linear produces parallel lines that swell and taper based on the luminance map. Wave does the same with a sinusoidal twist. Trace abandons the grid to follow the natural edge contrast of the source image, producing something close to nineteenth-century steel engraving. Halftone separates the image into configurable dots that mimic offset printing. Stipple clusters dots based on density, automating the painstaking newspaper-hedcut style that illustrators used to spend days crafting by hand.

For printmakers, a multicolour halftone mode separates the source into colour channels and renders each as a separate, angled halftone layer. The output is layered SVG, ready to be burned onto silk screens. The maths is simple; the discipline is choosing what to keep and what to throw away.

The connection back to FontLab and the typography world is the Text fill mode, where a variable font’s weight axis encodes brightness. That deserves its own post. For now, it is enough to say that Vexy Lines treats an image the way a sound engineer treats a recording — as a signal you can shape, filter, and reduce until the essential thing comes through.

## References

- [Vexy Lines — official site](https://vexy.art/lines/)
- [Vexy Lines knowledge base](https://help.vexy.art/)
- [Vexy Lines on AlternativeTo](https://alternativeto.net/software/vexy-lines/about/)
- [Vexy Lines on MacUpdate](https://vexy-lines.macupdate.com/)

[Read more on help.fontlab.com →](https://help.fontlab.com/fontlab/8/manual/)
