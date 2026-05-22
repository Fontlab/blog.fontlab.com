---
this_file: src_docs/md/posts/2019-04-04-fontlab-studio-typetool-fontographer-mac-updates.md
title: "Mac updates for FontLab Studio, TypeTool and Fontographer"
authors: [fontlab]
date:
  created: 2019-04-04
slug: fontlab-studio-typetool-fontographer-mac-updates
review:
  cta_status: todo
  cta_target: "https://www.fontlab.com/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "Versions: FontLab Studio 5.1.6, TypeTool 3.1.3, Fontographer 5.2.4 — verify"
    - "A 25-year-old byte-reordering bug surfaced when Apple changed a system function in macOS 10.14.4 — verify"
    - "Copy/paste relied on an API Apple removed in macOS 10.13 — verify"
  image_status: missing
  image_needs: "App icons for FontLab Studio 5, Fontographer 5 and TypeTool 3 (the original had a three-up icon gallery)."
  weakness_verdict: keep
  consolidate_with: ""
  notes: "Classic-app maintenance release covering macOS compatibility fixes. CTA left as todo with a generic fontlab.com target — the original linked to three separate product/download pages, none of which is a clean single 'read more' destination."
---
We have released Mac updates for FontLab Studio 5 (5.1.6), TypeTool (3.1.3) and Fontographer (5.2.4), fixing font open/export and copy-paste problems on recent macOS releases.

<!-- more -->

These updates address two macOS compatibility issues: a font open/export failure that appeared with macOS 10.14.4, and copy-paste problems on macOS 10.13 and 10.14 (High Sierra and Mojave).

### Opening and exporting OpenType fonts

The old FontLab core relied on a system byte-reordering function for 25 years. There was a latent bug in our code, but it stayed hidden — Mac OS 9 and early OS X handled it fine. When Apple adjusted that system function in macOS 10.14.4 (a change well within spec), it exposed our bug, and FontLab Studio, Fontographer and TypeTool could no longer open or export OTFs and TTFs correctly. That is now fixed for users on macOS 10.14.4 and newer; older macOS versions were never affected.

### OS/2 average width

The same change also appears to fix a problem with the `averageWidth` entry in the OS/2 table, which earlier versions saved incorrectly. This one helps users on every macOS version.

### Copy and paste

Our copy-paste code leaned partly on a system API that Apple removed in macOS 10.13. We rewrote it to use only the newer API, so copy-paste works again in the Font and Glyph windows — including copying contours to and from Adobe Illustrator. This helps users on macOS 10.13 and 10.14.

### Faster progress, on every version

FontLab Studio and TypeTool spent a surprising amount of effort drawing and updating the progress bar shown while opening and exporting fonts. Trimming that work makes those operations up to 10 times faster on all macOS versions.

### Pasting in panels

We improved pasting non-ASCII text into the OpenType panel and the Edit Macro panel. Those fields were never Unicode-capable and will not be, but pasting Unicode text in 5.1.5 produced odd results. Now FontLab keeps the full macOS Roman (Western European) range and drops the rest. This applies to FontLab Studio on all macOS versions.

[Read more →](https://www.fontlab.com/){ .fl-help-cta }
