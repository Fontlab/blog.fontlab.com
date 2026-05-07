---
this_file: src_docs/md/posts/2024-10-08-fontlab-tv-variable-fonts-crash-course.md
title: "FontLab TV: variable fonts crash course"
authors: [fontlab]
tags: [variable-fonts, masters, axes, tutorial]
date:
  created: 2024-10-08
slug: fontlab-tv-variable-fonts-crash-course
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab/8/manual/"
  title_case: ok
  title_suggested: ""
  voice_quality: adequate
  facts_to_verify:
    - "FontLab TV crash course URL — confirm actual episode URL at fontlab.tv"
    - "'Under an hour of focused video' — verify actual runtime"
  image_status: present
  image_needs: "Added existing FontLab TV variable-fonts thumbnail from src_docs/md/media/fontlabtv-AijDkf3DBk8.jpg."
  weakness_verdict: keep
  consolidate_with: "2025-06-24-fontlab-tv-design-space.md"
  notes: "Solid intro post. CTA now uses an absolute FontLab 8 manual URL; FontLab TV link still goes only to the homepage and needs the real episode URL."
---
If “variable font” still sounds like one of those things you’ll learn properly later —
this is the playlist that fixes that.
The FontLab TV crash course gets you from a single static master to a working VF in
under an hour of focused video.

<!-- more -->

![FontLab TV variable-fonts crash course thumbnail](../media/fontlabtv-AijDkf3DBk8.jpg)

> 📺 Watch: [Variable fonts crash course on FontLab TV](https://fontlab.tv/)

## What it covers

**Masters and axes.** A variable font is a system of masters along one or more axes —
Weight, Width, Optical Size, Slant, plus any custom axis you define.
The episode shows how to set up two-master and three-master designs and how to think
about the design space before you start drawing.

**Compatibility.** Master interpolation only works if the masters share contour
structure: same point count, same start points, same path direction, compatible
component setups. The video walks through FontLab’s compatibility checker and the most
common things that break it.

**Intermediate masters.** When linear interpolation between two extremes does not give
you the curve you want, you add a master in the middle of an axis to “pin” a specific
instance. The episode shows when to reach for this and when to fix the extremes instead.

**Export and inspection.** Final step: export to a single VF binary, inspect it in a
browser or in FontLab’s built-in tester, verify named instances and STAT table
behaviour.

## Why it matters

Variable fonts are not exotic anymore — they are the default delivery format for most
new releases. The crash course is the fastest way from “I have static masters” to “I am
shipping a VF that browsers handle correctly.”

[Read more →](https://help.fontlab.com/fontlab/8/manual/){ .fl-help-cta }
