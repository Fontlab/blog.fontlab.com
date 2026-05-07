Fonts aren't just for letters. An OpenType file can hold a company logo, a set of UI icons, or an entire pictogram library — one file that works in every application that renders text. Day 7 covers two practical workflows: packaging a logo as a font, and building a consistent icon set in FontLab.

## Your logo as a font

Every logo ends up as a folder of files: PDF, EPS, SVG, PNG, light-background, dark-background, monochrome, CMYK — plus the brand guidelines explaining when to use which. That's a small archive before you've produced a single piece of collateral.

There's a simpler way: a font. An OpenType `.otf` file stores high-resolution vector graphics, works across applications and operating systems, and can be served as a web font. One file.

To turn a monochrome vector logo into a font:

1. Create a new font in FontLab. Go to *File > Font Info > Names*, enter a name like "MyLogoFont", click Build Names. Under Font Dimensions, turn off Round coordinates.
1. In the Font window, pick a glyph cell for your logo — "one" works, so the logo appears when you type the digit 1.
1. Open your EPS, PDF, or SVG in Illustrator or Affinity Designer, copy it, paste into the FontLab glyph cell. If prompted, choose "monochrome contours" and "Descender to Caps Height".
1. If any paths that should be black appear white, use *Contour > Join* to fix them.
1. Adjust sidebearings with the Metrics tool so the advance width matches the logo's intended space.
1. Export as OpenType PS from *Font > Export Font As*. Install the font, type "1", set the font to MyLogoFont in any application — your logo appears.

For a multi-color logo, use separate glyphs for each color layer, set sidebearings so they overlap correctly when typed in sequence, and add an OpenType ligature that replaces the sequence with the combined form. Users type the trigger text, choose the font, and see the full logo with colors typeset separately.

## Icon fonts: three principles

Icons reduce complex ideas to simple, universal symbols. Good ones are visual haikus: precise and stripped down. A custom icon set gives a product a cohesive look that stock libraries can't match.

Three principles for building one in FontLab:

**Simplicity.** Determine the subject matter, style, and count. Sketch with basic shapes — lines, curves, circles, squares, triangles. Strip to the minimum recognizable elements.

**Consistency.** Each icon lives in its own glyph slot. Draw vector skeletons with FontLab's built-in tools — Bézier curves, ellipses, polygons, stars — then apply consistent stroke thickness. The eM grid (set *Font Info > Family Dimensions > Units Per eM* to 180 or 1800) gives you a consistent artboard. Turn on Round coordinates and points snap to integer positions.

**Reuse.** FontLab's element references let you draw a basic shape once and reuse it across icons. If you're extending an existing set, drop all SVG files into a new FontLab font, select all glyphs, and run *Element > Image > Make SVG Editable*, then *Font > Detect Composites*. FontLab finds identical elements across icons and links them as references — change the shared element and every icon that uses it updates.

Test in the Preview panel at multiple sizes. An icon clear at 48px can fall apart at 16px. Adjust stroke weights and simplify shapes until they read at small sizes as well as large.

Export as an OpenType font with *Font > Export Font As*, or as individual SVG, PDF, or PNG files with *Font > Export > Artwork Collection*.

______________________________________________________________________

## More in this series

1. [Day 1: Start making fonts](https://blog.fontlab.com/2022/08/15/8-days-start/index.md)
1. [Day 2: A-B-C](https://blog.fontlab.com/2022/09/12/8-days-abc/index.md)
1. [Day 3: Beyond A-B-C](https://blog.fontlab.com/2022/10/10/8-days-beyond-abc/index.md)
1. [Day 4: Clever fonts](https://blog.fontlab.com/2022/11/07/8-days-clever/index.md)
1. [Day 5: Letter crowd](https://blog.fontlab.com/2022/12/05/8-days-letter-crowd/index.md)
1. [Day 6: Bigger, bolder, better](https://blog.fontlab.com/2023/01/09/8-days-bigger-bolder/index.md)
1. **Day 7: beyond text** (this post)
1. [Day 8: Color is the new black](https://blog.fontlab.com/2023/03/13/8-days-color/index.md)
