FontLab VI Public Preview is now available for Windows, alongside an updated Mac build. It is free until the final app ships.

FontLab VI is our cross-platform professional font editor, a substantial step up from FontLab Studio 5. It runs on both macOS and Windows with the same performance, interface, and toolset.

### What’s in FontLab VI

FontLab Studio 5 users will recognize a lot here, rebuilt and refined. The new **Font window** adds visual sorting, smart search and filtering, and a table view exposing numerical glyph data. The **Glyph window** and **Metrics window** are unified, so the Metrics and Kerning tools are reachable from the main toolbar. The old Class panel is now the **Groups panel**, still the home for kerning and OpenType groups.

In place of the old limited Components, FontLab VI introduces **Cloned Shapes** with bidirectional live links between contours that appear in different glyphs. The View, Transform, OpenType Features, and Python Scripting panels are all still here, each redesigned.

New functionality includes automatic **Create Overlaps** and **TrueType Hinting** commands attachable to PostScript outlines. An internal **fractional coordinate** system lets you scale or slant contours losslessly. There are new drawing tools: the **Rapid** tool, **Tunni Lines** and **Genius points** for curvature control, the **Fill** tool that ignores path direction, the **Power Brush** for calligraphic strokes, and **Power Nudge** for typographically correct condensing and expanding.

The app supports all of **Unicode 9** (including color emoji) and **OpenType 1.8** (including Arabic and Indic shaping, and color and variable fonts). This build can open variable fonts but cannot yet generate them; you can set up unlimited font-wide or per-glyph **Masters** in a MutatorMath- and OpenType Variations-compatible design space that stays backwards-compatible with FontLab Studio 5’s Multiple Master model.

FontLab VI also brings unlimited glyphs and layers, multi-line multi-glyph editing, full color support, tag-based guides and zones, anchor-based mark attachment, and metrics linking via expressions. It converts between `.ttf`, `.otf`, `.vfb`, `.ufo`, `.glyphs`, and color OpenType formats such as OpenType+SVG.

### The Windows build

Because FontLab VI is built on a cross-platform framework, the Windows feature set is practically identical to the Mac version. We expect only a few platform-specific bugs, mostly interface-related.

The Windows version is a 32-bit app that runs on both 32- and 64-bit Windows, from Windows XP through Windows 10. We tested it specifically on Windows XP, 7, and 10.

One caveat: some menu shortcuts are marked with a “Meta” modifier and are not yet accessible. The Mac has three modifier keys available to developers (Ctrl, Alt, Cmd) while Windows has two (Ctrl, Alt). Sensible Windows shortcuts are still being worked out.

[Read more →](https://help.fontlab.com/fontlab-vi/Release-Notes/)
