---
this_file: src_docs/md/posts/2026-11-03-the-open-tool-ecosystem.md
title: "The open tool ecosystem"
authors: [fontlab]
tags: [fontlab-8, tools, open-source, harfbuzz]
date:
  created: 2026-11-03
slug: the-open-tool-ecosystem
---

Most of the world's text passes through a library most people have never heard of.

<!-- more -->

**HarfBuzz** — Persian حرف‌باز, meaning "open type" with a secondary sense of "insincerely talkative" — is the shaping engine behind Chrome, Firefox, Android, GNOME, LibreOffice, Flutter, and Unreal Engine.
**Behdad Esfahbod** began rewriting it in C++ in 2005.
Mozilla's Jonathan Kew helped stabilise harfbuzz-ng around 2012.
Esfahbod won the O'Reilly Open Source Award in 2013.
The library is everywhere type renders. The people who rely on it, almost to a person, have no idea it exists.

---

**FontTools / TTX** was started by Just van Rossum in 1999.
It is the Python library that lets you open any font file, inspect every table, change one byte, and write it back out.
Esfahbod revived the project around 2013 inside Google.
At TypeCon 2014 he said:

> "I'll make a bet — no matter what you use to create a font, if you round trip it through TTX, it will be functionally the same."

That bet has held well enough to be a practical standard.

**FontGoggles** (Just van Rossum, funded by Google Fonts) is a macOS preview tool.
Drop any `.ufo`, `.designspace`, or `.ttf` on it and the preview reloads as you save.
Stephen Nixon, on first use: *"WOW. Font Goggles is just so good. It allows me to open a preview of the full Recursive designspace in maybe 4 or 5 seconds."*
For variable font work it shortens the edit-and-check loop to something that doesn't interrupt thought.

**Wakamai Fondue** (Roel Nieskens, wakamaifondue.com) tells you what's inside any font dropped into a browser tab — features, axes, glyph counts, languages supported.
A major release in **April 2026** at Fontstand Berlin swapped the old Fontkit backend for **LibFont**.

**fontdrop.info** (Viktor Nübel) is the same diagnostic idea with a stricter scope and a smaller payload: under 1.5 MB, all client-side.
It started in 2016 from a German publishing-house consulting job.
The scope discipline is visible: it does one thing well and does not grow.

---

The right way to use these five together is unromantic.
HarfBuzz and FontTools are infrastructure — the water and drains of a modern font workflow.
FontGoggles is the fast inner loop for day-to-day iteration.
Wakamai Fondue and fontdrop are diagnostics for when something breaks.

A font workflow that doesn't lean on at least three of them is doing more manual work than it needs to.
None of them requires a subscription.
All of them existed before they were fashionable.

## References

- [Why is it called HarfBuzz? — HarfBuzz documentation](https://harfbuzz.github.io/why-is-it-called-harfbuzz.html)
- [FontGoggles](https://fontgoggles.org/)
- [Wakamai Fondue](https://wakamaifondue.com/)
- [fontdrop.info](https://fontdrop.info/)
- [FontTools — GitHub](https://github.com/fonttools/fonttools)

[Read more →](https://www.fontlab.com/font-editor/fontlab/){ .fl-help-cta }
