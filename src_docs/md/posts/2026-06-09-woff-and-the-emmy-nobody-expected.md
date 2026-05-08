---
this_file: src_docs/md/posts/2026-06-09-woff-and-the-emmy-nobody-expected.md
title: "WOFF, WOFF2, and the Emmy nobody expected"
authors: [fontlab]
tags: [woff, woff2, web-fonts, history]
date:
  created: 2026-06-09
slug: woff-and-the-emmy-nobody-expected
---
In 2021 the Television Academy gave the W3C a Technology & Engineering Emmy for font
standardisation.
One of the recipients was the CEO of FontLab Ltd — one of the few times a font tool
company has won a piece of broadcast hardware named after a 1940s televised play.

<!-- more -->

The Web Open Font Format started in 2009 with three names on the draft: **Jonathan Kew**
(Mozilla), **Tal Leming**, and **Erik van Blokland**.
Submitted to the W3C in April 2010, recommendation status by December 2012.
The mechanism was modest: a thin wrapper around an OpenType file, with metadata and zlib
compression.
The politics were not modest.
Type foundries had refused to license desktop fonts for raw `.otf` web embedding for
years.
WOFF was the format they would license.
That was the actual invention — not the wrapper, but the agreement.

WOFF2 followed in April 2012.
The compression switched to **Brotli**, developed by Jyrki Alakuijala and Zoltán
Szabadka at Google.
The wrong-footing detail: Brotli was built for fonts *first*, before it became the
general-purpose web compression algorithm you now encounter everywhere.
RFC 7932 in July 2016 standardised it for everything else.
WOFF2 became a W3C Recommendation in March 2018.

The size numbers are not subtle.
WOFF2 vs WOFF: roughly 30% smaller on average across the Google Fonts corpus.
For CJK fonts: over 50% smaller.
Full Noto Emoji as CBDT bitmap tables: 9 MB.
The same set as COLRv1 plus WOFF2: 1.85 MB.

The lesson is not that WOFF was technically hard.
It isn't.
The lesson is that the parties who had to agree — Mozilla, Adobe, Microsoft, Apple,
Google, every type foundry that mattered, and the W3C — had no obvious reason to agree
on anything, and somehow did.
The format works because the people behind it had spent twenty years arguing about
everything else, and eventually ran out of objections.

Some arguments do end.
Slowly, expensively, with an Emmy at the finish line.

## References

- [WOFF2 specification — W3C](https://w3c.github.io/woff/woff2/)
- [WOFF2 on GitHub — Google](https://github.com/google/woff2)
- [W3C Technology & Engineering Emmy — W3C blog](https://www.w3.org/blog/2021/w3c-technology-engineering-emmy/)

[Read more →](https://www.fontlab.com/font-editor/fontlab/){ .fl-help-cta }
