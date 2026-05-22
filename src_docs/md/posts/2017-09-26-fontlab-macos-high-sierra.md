---
this_file: src_docs/md/posts/2017-09-26-fontlab-macos-high-sierra.md
title: "FontLab Studio, TypeTool & old TransType on macOS 10.13 High Sierra"
authors: [fontlab]
date:
  created: 2017-09-26
slug: fontlab-macos-high-sierra
review:
  cta_status: todo
  cta_target: "https://help.fontlab.com/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "FontLab Studio 5.1.4 and earlier, plus TransType Pro 3, cannot install or launch on macOS 10.13+ — verify version cutoff"
    - "FontLab Studio 5.1.5 (free update for 5.0/5.1.x) and TransType 4 resolve the install/launch issue — verify"
    - "Multiple-master glyph copy/paste and Paste Special in FLS5 stay broken on High Sierra with no workaround — verify"
  image_status: missing
  image_needs: "A simple advisory/compatibility graphic, e.g. macOS High Sierra plus the FontLab Studio 5 icon, or a screenshot of the license-error dialog."
  weakness_verdict: keep
  notes: "Historical compatibility advisory for legacy apps. A later post addressed these issues with updated builds; this is kept as a historical record. cta_target set to the help center generically; flagged todo since the original points to a since-superseded announcement."
---
A compatibility note for owners of the older apps: FontLab Studio 5, TypeTool 3, and TransType Pro 3 had real problems on macOS 10.13 “High Sierra” and 10.14 “Mojave.” Here is what broke and what to do about it.

<!-- more -->

This is a historical record. The issues below were later addressed with updated builds; check the help center for the current state before acting on any of it.

Fontographer 5, TransType 4, and FontLab VI had no High Sierra or Mojave issues. FontLab VI was built on an all-new platform and ran fine. Anyone using FontLab Studio 5 for axis-based (Multiple Master) design, or relying on Paste Special, was better off moving to FontLab VI before upgrading macOS.

## Install and launch problems

FontLab Studio 5.1.4 and earlier, and TransType Pro 3, could not be installed on High Sierra or later. If already installed, they would not launch. Symptoms were a license-file write error, or an “Error initializing license system. Bad or missing or expired RLM license (-130)” message.

The fix: install **FontLab Studio 5.1.5** — a free update for 5.0 and 5.1.x — or upgrade from TransType 3 to TransType 4. FontLab Studio users should still read the operating problems below.

## Operating problems

FontLab Studio 5.1.5 and TypeTool 3.1.2 were both affected on High Sierra and later:

* **Copy and paste in the Font window** did not work normally. The “paste” and “append glyph” commands were grayed out even after a copy, and the keyboard shortcuts were dead too. There is a workaround below.
* **Contour copy/paste for multiple-master fonts** in the Glyph window copied only one master. Single-master fonts were fine. No workaround.
* **Paste Special** in FontLab Studio 5 did not work. No workaround.

## Workaround for Font window copy/paste

There is no fix for MM editing in FontLab Studio 5, but the Font window copy problem has a decent workaround in both apps:

1. Select the cell or cells.
2. Click and drag them to their destination, but do not release the mouse button.
3. Press and hold the Command key, then release the mouse button.

This works within one Font window or between two. Drop into an empty slot, or into an occupied slot and answer “no” when asked to replace, which appends the glyphs instead.

[Read more →](https://help.fontlab.com/){ .fl-help-cta }
