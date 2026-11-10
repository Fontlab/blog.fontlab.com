A new FontLab VI Public Preview for Mac is out, adding context menus, a Gallery panel for named shapes, faster glyph access, and italic-angle drawing.

This build lands a month after the last preview, with new features and a long list of fixes. The highlights:

**Interface**

- **Context menus** (right-click or Ctrl+click) now work in the Glyph and Font windows.
- A **High contrast mode** in **Preferences › Editing** boosts the visual contrast of UI elements in the Glyph window.

**Shapes**

- The new **Gallery** panel lists every named shape in the font and lets you drop it into the active layer via the **Place** button or drag-and-drop, in either the Glyph or Font window. Name a shape in the Shapes panel and it joins the Gallery for reuse elsewhere.

**Glyph access**

Keyboard navigation in the Font and Glyph windows is faster:

- `/` jumps to a glyph by name; `#` jumps by Unicode.
- **Cmd+F** (*Edit › Find Glyphs…*) inserts or selects glyphs by various criteria.
- **Shift+Cmd+F** jumps to the Search box to filter the Font window or insert results in the Glyph window.
- **Cmd+L** (*Edit › List Related Glyphs…*) goes to glyphs related to the current selection.

The Font window’s **All Glyphs** toggle controls filtering: on (default) shows filtered cells in a “yellow area” at the top with the rest following, FontLab Studio 5 style; off hides everything but the matches.

**Glyph design**

- *View › Apply Italic Angle* (the `\` key) cycles through three states for italic fonts: slanted sidebearings, slanted sidebearings plus a slanted grid (so Shift-constrained moves follow the italic axis), and straightened.
- **Arrow keys** move points by 1 unit; with Ctrl 0.1 unit, with Shift 10 units, with Cmd 100 units. The base and Shift distances are configurable in *Preferences › Distances*.
- With the Guides tool, Ctrl+click adds a glyph anchor and Alt+click adds a shape pin.
- Glyphs made with Generate Glyphs now respect matching named anchors such as `top`/`_top`.

**Import, export, technology**

- A confirmation dialog now shows where exported fonts were written.
- *Curve Conversion › Create short curves* now applies only to explicit, user-initiated conversion. A new *Open Fonts › Break long TrueType curves to short segments* setting governs the same behavior when fonts are opened.
- The built-in **ttfautohint** and **HarfBuzz** are updated to their April 2016 versions.

Beyond these, the build clears a long list of fixes across the Font and Glyph windows, the Sketchboard, the Layers and Shapes panels, and various crashes, plus assorted refresh and redraw problems.

A Windows version is also in progress.

Current builds run on OS X 10.7 and later. They do not run on 10.6.8 or earlier.

[Read more →](https://help.fontlab.com/fontlab-vi/Release-Notes/)
