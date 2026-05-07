FontLab 8 launched in June 2022 with over 1,400 improvements over FontLab VI. For FL VI users considering the upgrade, here is a practical summary of what changed across every stage of the font-making workflow.

FontLab VI was released in 2017. It introduced a lot — elements, variable font support, a new drawing engine — but it arrived before those ideas were fully settled. FontLab 7 (2019) consolidated the rough edges. FontLab 8 (2022) followed with what the team calls the “best and boldest upgrade ever,” with FontLab 8.2, 8.3, and 8.4 extending it further through 2023–2024.

## Interface and environment

The most visible change is the optional **dark theme** — a common request from designers who spend long hours at a screen. Beyond aesthetics, the interface has been substantially reorganized. **Widgets** give quick access to properties for glyphs, components, and selections. Panels can be grouped into scrollable **panel docks**. Numeric values accept **slider** input and simple **calculations** (type “300+50” and get 350). Hold **F1** over any interface element to get a **Quick Help** popup explaining what it does.

## Drawing

FontLab VI had the Power Brush. FontLab 8 adds the **Power Stroke** — a different approach to skeleton-based drawing that allows thickness to vary asymmetrically on either side of the skeleton, with more cap options. The **Thickness** tool lets you visually modulate stroke weight along a path. The Pen and Rapid tools now have **toolbox sub-tools** accessible without switching tools.

The **Rectangle** tool draws polygons and stars as well as rectangles. The **Pencil** produces smoother freehand curves. Autotrace has been improved for better glyph-optimized results.

## Editing

**Power Nudge** now has a toolbox toggle so you can switch between nudge modes without a menu trip. The **Lever** is new: hold Cmd (Mac) or Ctrl (Windows) while dragging a node to move it with high precision without zooming in. Curves can be tension-adjusted numerically. Points can be **aligned** and **collapsed**. Contours can be **sorted**. **Paste to replace selection** is a new operation. Ink traps and smart corners can be fine-tuned individually.

## Consistency and precision

**Auto-meter** shows stem widths, segment lengths, curve tensions, and corner angles — live analytics as you draw. **Quick measurement** displays thickness between opposing segments. Snapping now includes **continuation lines**, **perpendicular** lines, and **centerlines**. The **Suggest Stems** feature highlights common widths in your font as you draw new paths, making it easy to keep stems consistent across glyphs.

## Composites and assembly

**Variable components** — composites that use interpolated instances of other glyphs — are new. Adjust them visually with sliders. A **Fusion** filter applies live Boolean pathfinding between elements. **Text shapes** let you re-use scaled words from your font as elements inside other glyphs. **Clipping groups** mask out areas. The Glue and Skin filters handle decorations attached to nodes and segments.

## Metrics and kerning

Auto-spacing and auto-kerning are now a single keypress (semicolon). **Right-to-left kerning** is supported. Lever dragging extends to sidebearing and kerning adjustment. **Audit Kerning** finds class kerning conflicts and converts them to exceptions. The **Pairs & Phrases** panel manages the most commonly kerned combinations.

## Families and variation

Static fonts can be merged into a variable font with **Fonts > Merge Fonts to Masters**. **Per-glyph variation axes** allow individual glyphs to vary along custom axes independent of the main font axes. **Smart variable components** use interpolated instances of other glyphs as building blocks. Conditional glyph substitutions using tilde glyph tags (e.g. `~wt>850`) allow `rvrn` rules in exported variable fonts.

## Color

The **Colors** panel is redesigned with palettes and gradient support — linear, radial, and conical. A **visual gradient editor** works directly in the Glyph window. **OpenType COLRv1** export is supported, including variable color fonts. Dark-mode palette export is automatic.

## Scripting

FontLab 8 uses **Python 3.11** (up from Python 2.7 in FontLab VI), which is 10–60% faster. The **TypeRig** library by Vassil Kateliev is bundled, providing extensive glyph transformation and batch-processing capabilities. Interchange with RoboFont, Glyphs, FontForge, and other editors is improved throughout.

______________________________________________________________________

The full list of changes across all FontLab 8 releases is at [help.fontlab.com/fontlab/8/whats-new/](https://help.fontlab.com/fontlab/8/whats-new/).
