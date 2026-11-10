FontLab VI 6.1 adds three things type designers had been asking for: real, standards-compliant components, a Font window sidebar that filters glyphs by script and category, and metrics expressions that link spacing across glyphs, layers and masters.

## Components

FontLab VI 6.1 (re-)introduces **Components** as a standards-compliant way to build glyphs from other glyphs. They work like components in FontLab Studio 5, UFO, or TrueType-flavored OpenType fonts: a component points to a **source glyph** and carries a transformation — usually a shift, optionally scale, rotation or slant. That is the whole idea. If you have used components in any other font editor, you are already at home.

This sits alongside the **Element References** that earlier versions of VI offered. Element References are great for reusing a design piece — a stem, a serif, a fragment — across glyphs in the same layer, keeping every instance linked. But all references are equal: there is no source glyph they point to, they simply link to each other, and they know nothing about metrics or anchors. They behave rather like subroutines in CFF OpenType fonts.

Earlier VI versions *simulated* components by locking some references and guessing the best source glyph. It was never quite satisfying, so we added real components instead. The rule of thumb: use **Element References** to link pieces of glyphs, use **Components** to build composite glyphs from whole glyphs. VI 6.1 has both.

You can build composites from components in one master or all of them — via Generate Glyphs, Add Component, Copy-Paste or Auto Layers. You can mix components and plain contours in one layer, and you can nest them: build `dieresiscomb` from two `dotaccentcomb` components, then build `Adieresis` from `A` and `dieresiscomb`. On export, FontLab keeps your component structure in formats that support it (TTF, VFB, UFO) and decomposes only where a format cannot represent something — rotated components, say, or components mixed with contours.

### Choosing components or references

In **Preferences > Open Fonts > Composite glyphs**, pick **Use components** (FontLab prefers components) or **Convert components to element references** (FontLab prefers references). When you open a `.vfc` or `.vfj`, FontLab keeps your references as references and your components as components either way; the exception is Auto Layers, which are built dynamically and follow this setting.

When you open a format that supports components (`.ttf`, `.vfb`, `.ufo`, `.fog`, `.glyphs` and derivatives like `.woff`), FontLab either imports the components as-is or converts them to references, depending on the same preference. For formats that *don’t* carry components (`.otf`, Type 1), turn on **Detect composites** and FontLab finds repeating contours and links them — then converts those to components if **Use components** is on.

### Converting references to components

Select glyphs in the Font window and choose **Element > Element Reference > References to Components**; repeat per master. FontLab picks the source glyph by finding where the referenced element appears on its own and is “least transformed” — closest to (0, 0) with no other transformations. If several candidates exist it chooses the least-transformed one; if none works, it leaves the references alone. So “helper glyphs” holding serifs or stems become natural component sources.

### Adding components automatically and by hand

With **Use components** on, FontLab uses components when you run **Font > Generate Glyphs**, turn on **Glyph > Auto Layer**, double-click an empty cell (with the “fill created glyphs” preference on), or run **Font > Detect Composites**.

To add one by hand, choose **Glyph > Add Component…**. Start typing the component’s **glyph name** and pick from the results — with **Find glyph name synonyms** on, typing `uni0414` also finds `Decyr`. Placement is flexible:

- Leave **X** and **Y** empty and FontLab uses matching anchors (`top` and `_top`), or centers horizontally and shifts a mark up by the cap-height-minus-x-height difference on uppercase letters.
- Enter a number in either field to fix that coordinate while the other follows the automatic rule.
- Enter an anchor name in a field to position by anchor, and mix the two — `0` in X, `top` in Y.

Use **Flip horizontally/vertically** to mirror, choose whether the glyph keeps its metrics or adopts the component’s width, and use **Apply to all masters** to insert everywhere at once.

You can also paste: copy one glyph cell, select targets, and **Edit > Paste Components** inserts it as a component in all of them across all masters. Copy several cells and the components are matched one-to-one with the selected targets.

### Working with components

Components are special “glyph filter” elements, so you can move them with the Element tool (or the Contour tool) and use most of the **Element** menu and the **Elements** panel. Press `<` and `>` to step between components; double-click (or **Ctrl+E**) to open a component’s source glyph for editing alongside the current one. **Send to Back** makes a component “first”; **Group** keeps several components moving together.

To **replace** a component, type a new source glyph name into the property bar’s underlined **C:** field (or the **Glyph name** field in the Elements panel) and press Enter. To **decompose**, click the **Decompose** button or choose **Glyph > Decompose** — Shift-click components first to decompose only those. **Expand Filters**, **Flatten Glyph** and **Separate Contours to Elements** all decompose as part of their work. Finally, **Element > Element Reference > Component to Reference** converts a component back to a reference, handy when you want to apply a filter or change the fill colour. Delete a source glyph and FontLab converts the affected components to references automatically.

## Font filters and the Font window sidebar

**Font filters** find glyphs in the Font window and sort matches ahead of (or instead of) the rest. (Don’t confuse them with the *glyph* filters in the Glyph window, which do effects like Power Brush.) The Font window shows every glyph in your font, sorted by the property bar’s **Sort** dropdown — but a font filter lets you focus on a subset, or surface empty cells for glyphs you might want to add.

Filters match in three ways:

- **Exact** filters match only when a name, codepoint or property matches outright.
- **Fuzzy** filters also match variants and alternates, using name suffixes and ligature naming.
- **Prospective** filters add empty placeholder cells for glyphs you could create — they are exact, since the full set of matches is known up front.

### Hiding unfiltered glyphs

When a filter is active, cells split into **filtered** (matching) and **unfiltered** (not). The new **Hide unfiltered glyphs** toggle in the property bar (formerly **All glyphs** at the bottom of the sidebar) controls the view. Off (the default), matches sit at the top highlighted in yellow — colour adjustable in **Preferences > Font Window > Highlight** — with everything else below. On, only the matches show.

### The filter dropdown and search box

The **Filter** dropdown produces prospective filters for Encodings, Unicode ranges, Codepages, Unicode Categories and Unicode Scripts — choose a type, then the filter. The Encoding filters in the OpenType group no longer pad each encoding with empty cells.

The **Search box** (top-right of the Font and Glyph windows) produces the same prospective filters plus exact or fuzzy ones, and 6.1 improves it. You can now search by:

- **Synonyms** — searching a glyph name also matches other names with the same Unicode from `standard.nam`, plus `XXXX`/`uXXXX`/`uniXXXX` algorithmic names. For `uni042F` (Cyrillic Ya), synonyms include `IA`, `42f` and `afii10049`.
- **Layers** — enter a complete layer name to find glyphs that include it.
- **Tags** — enter a complete tag to find glyphs that carry it, including the extended built-in virtual tags.

### The sidebar

Open the sidebar with the 2nd button in the Font window’s property bar. Its filter area is now a hierarchical list in three sections.

**Basics** is for beginners — three prospective encodings in a sensible drawing order:

- **New font** — 157 glyphs in an order you might draw them (basic Latin, digits, some punctuation).
- **Latin Simple** — 231 glyphs for a simple Western Latin font.
- **Latin Pro** — 374 glyphs for a wider pan-European Latin font.

**Categories** holds pre-defined filters by Unicode category and OpenType class. Prospective subcategories show a **totals label** — grey shows current matches versus the complete possible set, and clicking it offers **Generate Missing Glyphs**; green means complete. **All**, **Letter** and **Number** are visible by default; **Punctuation**, **Symbol**, **Mark**, **Separator** and **Small caps** appear as your glyph set grows. The **Properties** subcategory lists glyphs by **virtual tags** FontLab assigns automatically — `composite`, `compound`, `references`, `auto`, `colored` — and by OpenType Glyph Definition Class (`otsimp`, `otliga`, `otmark`, `otcomp`, `otnone`). The **Layers & Masters** subcategory lists every layer name present in any glyph, a quick way to find stray layers you forgot about.

**Scripts** lists every Unicode writing system your glyphs cover. Latin, Cyrillic and Greek always appear with prospective subsections (Basic, Historic, Extended); other scripts show once you have at least one glyph for them.

### Custom filters

For a quick **exact** filter, select glyphs, copy, click the Search box, paste, and choose **Text** — it shows just those glyphs and lands in Search History, from where you can drag it to Bookmarks. For a reusable **prospective** filter, write a custom Encoding file and drop it into the `Encoding` subfolder of your User data folder (now settable in **Preferences > General > User data folder**).

## Nonspacing components and elements

VI 6.1 lets you mark a component or element as **nonspacing**. A nonspacing component still exports and still draws — it does not change the glyph’s advance width — but **inside FontLab** it is invisible to the metrics engine. FontLab ignores it when showing width and sidebearing values, when copying metrics with Paste Special, and when computing linked metrics.

This mirrors how typesetting treats nonspacing characters: positioned relative to the spacing glyphs before them, but with their own metrics ignored. With the Measurement Line off, sidebearings are read from the bounding box of the whole layer; nonspacing elements let you exclude parts of that box from the calculation. The exported font, of course, still carries the correct absolute metrics.

*Example:* in `imacron` ("ī"), mark the `macron` component nonspacing, then set LSB and RSB to `=dotlessi`. The macron drops out of the sidebearing calculation, so linking `imacron` to `dotlessi` just works.

To set it, click a component or element and use the **Nonspacing** toggle in the property bar, or the Nonspacing column in the Elements panel. Turn on **Preferences > Open Fonts > Automatically assign nonspacing property to accent components** and FontLab marks components whose source is named `circumflex`/`caron`, falls in the relevant Unicode ranges (U+02B9–02BD, U+02C6–02CF, U+02EC), sits in the “Nonspacing Mark” or “Modifier Symbol” category, or has the OT Mark class. **Element > Nonspacing > Detect Nonspacing** applies the same rule on demand; **Tools > Actions > Metrics > Nonspacing** has Detect and Clear for all masters. If you would rather not use the feature at all, clear nonspacing across the whole font and turn the preference off.

## Metrics expressions (linked metrics)

VI 6.1 sharpens the expressions you write into metrics fields to link spacing across glyphs, layers and masters. Updating is much faster, expressions consistently beat static numbers, you can link across masters, and there are new functions.

**Faster updates.** Because updating is now quick, **Preferences > Spacing > Automatically update linked metrics** is on by default. With thousands of linked glyphs you may prefer to turn it off and run **Font > Update Metrics** manually.

**Expressions take precedence.** The interaction between expressions and plain numbers in the three fields — LSB, RSB, advance width — is now consistent: expressions win over numbers, and the most recent expression wins over an earlier one. One expression makes the other fields adjust; two expressions fix the third; three expressions (a bad idea) let the last one win and adjust one of the others by a constant.

**Specifying glyphs and layers.** Use a glyph name (`aogonek`) to refer to the current layer of that glyph — this works in functions, simple expressions and as a constant. You can also write `ą` (a single character), `:Thin` (a layer of the current glyph) or `ą:Bold` (a glyph and layer), though those three don’t work as constants in extended expressions.

FontLab-specific functions:

| Function             | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| `l()`                | LSB of the current glyph and layer                           |
| `r()`                | RSB of the current glyph and layer                           |
| `b()`                | **new:** bounding-box width of the current glyph and layer   |
| `w()`                | advance width of the current glyph and layer (`l()+b()+r()`) |
| `lsb("glyphspec")`   | LSB of the specified glyph and/or layer                      |
| `rsb("glyphspec")`   | RSB of the specified glyph and/or layer                      |
| `width("glyphspec")` | advance width of the specified glyph and/or layer            |
| `g("guidename")`     | x position of a vertical guideline named `guidename`         |

You can now wrap a `glyphspec` or `guidename` in single quotes as well as double. Enter `=width(':Regular') + 10` into the Bold layer’s width field for `space` and it sits 10 units wider than the Regular layer.

On top of that you get the full [muParser](http://beltoforion.de/article.php?a=muparser) function set, including **conditionals** — `=(d>0) ? d : o` sets the LSB of “q” to that of “d” unless “d” has no contours, in which case it borrows “o” — and **statistics** like `=max(i, w, m)` or `=avg(width(':Thin'), width(':Bold'))`.

**Other fixes.** Expression results are now always rounded to integers (`H` width 100, `I` set to `= H / 3` gives 33, `K` set to `= I * 2` gives 66; fractions are kept internally, so `= H / 3 + 0.18` gives 34). And when you manually nudge a glyph that uses an expression, the adjustment now *modifies the expression* — drag the RSB of “j” (set to `i`) ten units right and the field becomes `i+10`, rather than collapsing to a plain number as before.

[Read more →](https://help.fontlab.com/fontlab-vi/Release-Notes/)
