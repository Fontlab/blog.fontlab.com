---
this_file: src_docs/md/posts/2024-06-05-fontlab-8-updates.md
date:
  created: 2024-06-05
title: "FontLab 8.3 and 8.4: what's new"
authors: [fontlab]
draft: false
slug: fontlab-8-updates-2024
---
Since the FontLab 8.2 release in August 2023, two major free updates have shipped: 8.3
in December 2023 and 8.4 in June 2024. Together they add over 200 new features and
improvements. Here is the short version.

<!-- more -->

Both updates are free for all FontLab 8 users.
FontLab 8.4 also marks a milestone: over 900 improvements relative to FontLab 7, and
over 500 relative to the original 8.0 release.

## FontLab 8.3 (December 2023)

- **Widgets** — a new UI layer in the Glyph window that puts sidebearings, advance
  width, and kerning class assignment directly on the canvas.
  Click the number next to the glyph and type — no panel hunting.
- **Match Moves** — adjust a node or handle in one master and the change propagates to
  all visible masters simultaneously.
  Essential for keeping a variable font family consistent without switching masters back
  and forth.
- **Glance on hover** — move the pointer over any glyph cell, component reference, or
  element in the Font window and see a live contour preview without opening the glyph.
- **Export post-processing** — run a custom Python script automatically after every
  export. Useful for renaming files, running a QA check, committing to Git, or copying to
  a test directory.
- **Glyph Package format** — read and write `.glyphspackage`, the Git-friendly Glyphs
  format where each glyph is a separate file.
  Easier diffs, easier collaboration.
- **Apple Silicon native build** — FontLab 8.3 runs natively on Apple Silicon Macs, up
  to 2× faster than the Rosetta 2 version on the same hardware.
  macOS Catalina (10.15) or later required.
- **Variable mark attachment** — preview anchor-based mark positioning across all
  masters at once, so you can verify mark placement holds up across the interpolation
  range.

## FontLab 8.4 (June 2024)

- **Variable components** — drag handles in the Glyph window to change a component’s
  variation axis values in real time, without typing numbers into a panel.
- **Detach serifs from stems** — extract serif elements from a glyph and convert them to
  reusable Smart Corner components, so editing the serif shape once propagates across
  the whole typeface.
- **UVS sequences** — edit Unicode Variation Sequences for CJK ideograph variants and
  emoji, required for fonts targeting Japanese, Chinese, and Korean publishing
  workflows.
- **Tool-specific context menus** — right-click with any tool (Text, Eraser, Brush,
  Pencil, Knife, Scissors, Thickness, and more) to get a menu relevant to that tool’s
  context.
- **Node and handle rendering** — customize the size, shape, and color of nodes and
  handles. Useful on high-DPI displays where default node sizes can feel cramped.
- **Kerning preview** — a visual overlay in the Glyph window showing the applied kerning
  value as a colored band between glyphs, making it easy to spot missing or anomalous
  pairs.
- **Better Help panel** — context-sensitive articles that update as you switch tools,
  keeping relevant documentation one glance away.
- **Auto features on export** — if a font has no OpenType feature definitions, FontLab
  generates a sensible default feature set at export time.

FontLab 8.4 and all prior 8.x updates are free for FontLab 8 license holders.
Download the latest build and browse the full release notes at
[fontlab.com/font-editor/fontlab/](https://www.fontlab.com/font-editor/fontlab/). Full
documentation is at [help.fontlab.com](https://help.fontlab.com/).
