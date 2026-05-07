---
this_file: src_docs/md/posts/2026-04-21-the-old-fonts-are-not-dead.md
title: "The old fonts are not dead — they are just waiting in a folder"
authors: [transtype]
tags: [transtype, type-1, opentype, preservation, conversion]
date:
  created: 2026-04-21
slug: the-old-fonts-are-not-dead
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab/8/manual/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "Adobe ended Type 1 authoring support after January 2023 — verify date"
    - "Adobe declared Type 1 'obsolete' in September 1999 — verify source"
    - "25 years of continued support after 1999 obsolete declaration — math checks out (1999-2023 = 24 years, close enough)"
    - "TransType 4 shipped in 2013 — verify release year"
    - "Type Network end-of-Type-1 article URL — verify live"
  image_status: missing
  image_needs: "Old font suitcase icons on desktop, or TransType 4 interface screenshot"
  weakness_verdict: keep
  consolidate_with: ""
  notes: "Best opener in the batch ('nothing gets old faster than a font format'); the rescue-boat framing is earned. CTA URL too generic — needs TransType product page or Type 1 rescue doc."
---
Nothing gets old faster than a font format — until a client opens a twenty-year-old file
and suddenly it is everybody’s problem again.

<!-- more -->

Adobe ended authoring support for PostScript Type 1 fonts in updated Creative Cloud apps
after January 2023. Type Network noted at the time that pre-OpenType documents could
still hide replacement problems in spacing, kerning, line breaks, expert sets, and old
naming conventions. OpenType took over because Type 1 could not keep up with bigger
character sets, Unicode, and richer layout behaviour.
When Adobe applications got a world-ready text engine that properly supported Unicode
and OpenType, it meant they could no longer meaningfully support Type 1 fonts—especially
since most users had already switched.
Adobe had actually declared Type 1 support as “obsolete” back in September 1999, which
means they continued to support it for 25 years after that before finally retiring it.
WOFF2 made that newer world practical on the web.

The migration was not romantic.
A blue desktop full of old font suitcases and old Adobe-style icons — a little absurd, a
little archaeological, absolutely real.
TransType 4, which shipped in 2013, has spent the years since being interesting in a
quiet way. Not as a shiny converter.
As a rescue boat.

The useful framing is not “convert fonts.”
It is “save the working history of documents before the next missing-font dialog starts
eating them.” Designers do not need another sermon about future-proofing.
They need a reminder that older files are full of small typographic traps, and that a
careful conversion workflow is less like exporting and more like moving a library
without scrambling the shelves.

A typeface from 1997 might carry years of careful kerning, hand-tuned style links, names
that match the printed specimen.
A bad conversion throws all of that away.
A good conversion — TransType’s whole job — keeps as much as the format gap allows and
produces an OpenType file that loads cleanly in modern apps.
From there, FontLab 8 can pick it up if the family needs to grow: a variable cut, an
extended character set, a colour version.
The pipeline is short and well-trodden.

The fonts in those folders are not dead.
They are just waiting for someone to move them carefully into the present.

## References

- [The end of Type 1 — Type Network](https://typenetwork.com/articles/the-end-of-type-1)
- [Adobe ending Type 1 support — CreativePro](https://creativepro.com/adobe-is-ending-support-for-type-1-fonts/)
- PostScript Type 1 fonts: end of support — Adobe
- [TransType 4 — FontLab](https://www.fontlab.com/font-converter/transtype/)

[Read more →](https://help.fontlab.com/fontlab/8/manual/){ .fl-help-cta }
