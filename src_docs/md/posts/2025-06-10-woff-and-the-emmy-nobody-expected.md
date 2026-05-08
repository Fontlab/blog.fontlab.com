---
this_file: src_docs/md/posts/2025-06-10-woff-and-the-emmy-nobody-expected.md
title: "WOFF, WOFF2, and the Emmy that crowned web type"
authors: [fontlab]
tags: [woff, woff2, web-fonts, history]
date:
  created: 2025-06-10
slug: woff-and-the-emmy-nobody-expected
---
![](../media/illu/woff-and-the-emmy-nobody-expected-1.png){.illu-thumb}

In 2021 the Television Academy gave the W3C a Technology & Engineering Emmy for font
standardisation on the web.
Among the recipients was the CEO of FontLab Ltd — a small, deeply satisfying
acknowledgement that the work to make type travel cleanly across browsers, operating
systems, and broadcast pipelines mattered enough to be celebrated alongside
cinematography and sound design.

<!-- more -->

The Web Open Font Format started in 2009 with three names on the draft: **Jonathan Kew**
(Mozilla), **Tal Leming**, and **Erik van Blokland**. They submitted it to the W3C in
April 2010 and saw it reach Recommendation status by December 2012. The mechanism itself
was elegant in its modesty — a thin wrapper around an OpenType file, a little metadata,
zlib compression. The brilliant part was the agreement underneath: type foundries, who
had reasonably refused to license desktop fonts for raw `.otf` web embedding, were
willing to license WOFF. That trust was the real invention.

WOFF2 followed in April 2012. The team switched the compression to **Brotli**, developed
by Jyrki Alakuijala and Zoltán Szabadka at Google.
A delightful detail worth keeping: Brotli was designed for fonts *first*, and only later
became the general-purpose web compression algorithm we use everywhere — RFC 7932
standardised it in July 2016. WOFF2 itself reached W3C Recommendation in March 2018.

The size numbers reward that work generously.
Across the Google Fonts corpus, WOFF2 runs about 30% smaller than WOFF on average, and
over 50% smaller for CJK fonts.
A full Noto Emoji set as CBDT bitmap tables weighs in at 9 MB; the same set as COLRv1
plus WOFF2 lands at 1.85 MB. Every byte of that saving is delivered to readers on
metered data plans, on slow networks, on devices that fit in a pocket.

What strikes you reading the story now is how much patient collaboration sits behind a
single file extension.
Mozilla, Adobe, Microsoft, Apple, Google, every type foundry that mattered, and the W3C
had no obvious reason to converge on anything, and yet they did — through twenty years
of conversation, draft after draft, edit after edit, and a long friendship between
people who clearly care about letters.

Some agreements take a long time to land, and when they finally do, the result reads
like a small miracle.
WOFF and WOFF2 are exactly that.
The Emmy was a lovely way to say thank you to everyone who carried the project across
the line.

## References

- [WOFF2 specification — W3C](https://w3c.github.io/woff/woff2/)
- [WOFF2 on GitHub — Google](https://github.com/google/woff2)
- [W3C Technology & Engineering Emmy — W3C blog](https://www.w3.org/blog/2021/w3c-technology-engineering-emmy/)

[Read more →](https://www.fontlab.com/font-editor/fontlab/){ .fl-help-cta }
