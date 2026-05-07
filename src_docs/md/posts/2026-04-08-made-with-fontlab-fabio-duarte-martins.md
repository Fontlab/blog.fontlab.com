---
this_file: src_docs/md/posts/2026-04-08-made-with-fontlab-fabio-duarte-martins.md
title: "Made with FontLab: Fábio Duarte Martins"
authors: [adam]
tags: [made-with-fontlab, scannerlicker, variable-fonts]
date:
  created: 2026-04-08
slug: made-with-fontlab-fabio-duarte-martins
---
[Scannerlicker](https://fonts.scannerlicker.net/) is Fábio Duarte Martins’s foundry, and
his testimonial is one of the few that actually names the FontLab features doing the
work. It is, accidentally, a short manual on what to learn first.

<!-- more -->

Most testimonials are vibes.
Martins’s reads like a release-notes annotation, which is what makes it useful.
He runs Scannerlicker out of Portugal, builds variable fonts, and writes about the
editor the way somebody writes about a daily driver they have actually opened.

His full statement on FontLab 8:

> This baby is a rock-solid font development software, from design to engineering.
> Drawing is a joy: FontLab has the best drawing tools I’ve ever seen, and they just got
> better! FontAudit keeps you in check, with new information and smarter corrections; the
> new views for masks and layers are a super-handy for designing multiple masters; and
> the nudging workflow is spot-on.
>
> Expressions and tags became my bread and butter: generate tags to keep you organized
> in one click, edit them to automate your kerning classes and OT features, copy your
> expressions to all of your masters with one click!
>
> Did I mention that the new FontLab is a serious variable font production tool, with
> conditional glyph substitutions, table editing and all?
> To be honest, I wish I recorded my face when I saw the new axis graph!
>
> FontLab 8 is the juiciest release of FontLab.
> And hey, it’s running flawlessly on my Linux machine too!

— Fábio Duarte Martins, [Scannerlicker](https://fonts.scannerlicker.net/)

The phrase “from design to engineering” is the one to keep.
Modern variable font work is not just drawing — it’s also a non-trivial engineering job,
with conditional substitutions, design-space configuration, OpenType feature
compilation, and binary table editing.
The traditional split between “designer who draws” and “engineer who packages” is
exactly what the modern editor has to collapse.

Martins’s bread-and-butter pair is **expressions and tags.** Tags let you label glyphs
("punctuation", “uppercase”, “Cyrillic”, whatever), then drive kerning classes and
OpenType feature generation off the tags rather than off hand-edited lists.
Expressions let you parametrise glyph metrics — set this sidebearing equal to that one
minus three units — and propagate the relationship across all masters with one click.
Together, they turn the tedious bookkeeping of a large family into something approaching
automation.

The Linux remark is not throwaway.
FontLab ships native binaries for macOS, Windows, and — yes — Linux.
Most of the working type-design world is on the first two; the people who are on Linux
either run a one-person foundry or work inside a larger pipeline where Linux is the only
choice. Either way, “running flawlessly on my Linux machine” is an unusually quiet piece
of cross-platform engineering for an industry that mostly assumes Mac.

The Scannerlicker catalogue at
[fonts.scannerlicker.net](https://fonts.scannerlicker.net/) is the proof.
Variable fonts shipped, conditional substitutions configured, design space defined, all
out of one editor and one studio.

## More from Fábio Duarte Martins

- [Scannerlicker catalogue](https://fonts.scannerlicker.net/) — variable fonts and
  retail families

[Browse Scannerlicker →](https://fonts.scannerlicker.net/){ .fl-help-cta }
