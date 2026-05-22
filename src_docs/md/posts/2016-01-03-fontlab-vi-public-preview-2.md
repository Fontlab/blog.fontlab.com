---
this_file: src_docs/md/posts/2016-01-03-fontlab-vi-public-preview-2.md
title: "FontLab VI Public Preview 2 for Mac"
authors: [fontlab]
date:
  created: 2016-01-03
slug: fontlab-vi-public-preview-2
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab-vi/Release-Notes/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "Public Preview 2 build number 5844 — verify"
    - "Public Preview 1 expired 31 December 2015 — verify date"
    - "Does not run on OS X 10.6.8 or earlier — verify minimum OS"
  image_status: missing
  image_needs: "FontLab VI app icon or a Public Preview screenshot"
  weakness_verdict: keep
  consolidate_with: ""
  notes: "Mac-only preview update. Stripped expiry urgency, sign-up/download CTAs, and 'why not bugs first' hand-wringing; kept the architecture-change facts (OpenGL drawing, VFC format, tabbed windows, crash reporting)."
---
FontLab VI Public Preview 2 (build 5844) is out for Mac, following the expiry of the first preview. We are still not calling it a beta.

<!-- more -->

This release focuses less on visible features and more on architecture changes that needed doing before the app could stabilize. A few bugs are fixed, but the bulk of the work happened under the hood.

Here is what changed:

* **OpenGL drawing:** Anti-aliased on-screen drawing can now use OpenGL, offloading work to the graphics processor for a large speed boost on complex shapes. It is off by default in this build (enable it in **Preferences › General**) because it was not yet stable on Windows. Machines without a dedicated graphics card see little change.
* **Native VFC file format:** FontLab VI’s own VFC format is in place, though not yet well tested. You can also set the app to auto-save in UFO, VFB, or XFO.
* **Windows or tabs:** In **Preferences › General** you can turn off **Open new windows as tabs**. With it off, the Font, Glyphs, and Metrics windows each open separately after a restart, closer to the FontLab Studio 5 experience.
* **Crash reporting:** An early crash-reporting system is going in. Opt-out and screenshot options are still to come.
* **Internal messaging:** The messaging layer the app uses to communicate between its parts is being rewritten.

A Windows version is also in progress.

Public Preview 2 does not run on OS X 10.6.8 or earlier.

[Read more →](https://help.fontlab.com/fontlab-vi/Release-Notes/){ .fl-help-cta }
