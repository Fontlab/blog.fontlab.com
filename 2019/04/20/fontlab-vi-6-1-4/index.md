FontLab VI 6.1.4 adds high-precision segment editing, a snapping Knife, smarter glyph deletion — and, the headline, the ability to open and export `.glyphs` files on both Mac and Windows.

### Major improvements

- Edit segments directly with **high-precision dragging**.
- Add nodes, break or slice contours with an improved **snapping Knife**.
- **Kern** more efficiently with improved keyboard shortcuts.
- See at a glance which Font window **cells** hold composites or auto layers.
- **Delete** glyphs and decide what happens to their composites and auto layers.
- Export OpenType PS (`.otf`) fonts with better **hinting**.
- Export OpenType Variations (`.ttf`) with fewer limitations.

### Collaborate via .glyphs files

FontLab VI already moves between tools easily: it opens and exports `.vfb` (FontLab Studio 5, Fontographer), `.designspace` and `.ufo` (Superpolator, RoboFont, FontForge). The gap was Glyphs.app — VI could read `.glyphs` files but not write them.

That changes here. FontLab VI 6.1.4 exports `.glyphs` files and opens them far more faithfully, on Mac and Windows alike. The conversion has limits, but you will walk a long way before you hit them.

Export is **beta**, so the Glyphs profile is hidden by default. Turn it on under *File > Profiles* (tick the blue checkbox next to *Glyphs*, click OK), then choose the *Glyphs* profile in *File > Export Font As*.

### Other improvements

- Reach common contour operations from the **Node** panel.
- **Snap** guides to other objects, and turn them into hints and zones.
- Measure thickness quickly with `G` and drag.
- Tap `\` to make up/down moves **italic** or upright, for reliable italic metrics linking.
- Show **anchor** clouds only for selected anchors.
- Tap `Esc` for a **clean view** in Metrics and Kerning modes.
- Optically separate imported **artwork** more flexibly.
- **Zoom** in and out more easily in Glyph and Font windows.
- **Remove Overlap** while leaving unaffected nodes untouched.
- No more vanishing kerning, plus other bug fixes.

### Demo mode

When the FontLab VI trial expired, you used to be stuck at the Activation screen. Now the app switches to **demo mode** instead. In demo mode you can open any font and explore freely — you just cannot save, export, print, or copy contours to other apps.

That makes VI a capable font viewer. Open and proof fonts made elsewhere — TrueType variable fonts, color fonts of every flavour, development formats like `.vfc`, `.vfj`, `.vfb`, `.fog`, `.ufo` or `.glyphs`. Check curve quality and curvature, test interpolation, inspect kerning and OpenType Layout features, run contours under FontAudit, and see how automatic master matching behaves. On the Mac, you can even check hinting in the genuine Windows ClearType rasterizer via the TrueType Hinting tool.

When you do need to save and export, the *buy* button is one click away.

[Read more →](https://help.fontlab.com/fontlab-vi/Release-Notes/)
