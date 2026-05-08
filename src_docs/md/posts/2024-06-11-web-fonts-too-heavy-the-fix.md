---
this_file: src_docs/md/posts/2024-06-11-web-fonts-too-heavy-the-fix.md
title: "Your web fonts are probably too heavy — here is the fix"
authors: [fontlab]
tags: [web-fonts, woff2, performance, transtype, subsetting]
date:
  created: 2024-06-11
slug: web-fonts-too-heavy-the-fix
review:
  cta_status: ok
  cta_target: "https://help.fontlab.com/fontlab/8/manual/"
  title_case: ok
  title_suggested: ""
  voice_quality: adequate
  facts_to_verify:
    - "WOFF2 compresses better than anything else — verify vs Brotli/gzip alternatives; WOFF2 uses Brotli internally"
    - "Full Latin-Extended cut 90 KB, subset 12 KB — verify these are representative figures"
    - "TransType 4 released in 2013 — verify this is accurate for the web font context claim"
    - "Font Squirrel and Transfonter handle quick jobs — verify both tools are still actively maintained"
  image_status: present
  image_needs: ""
  weakness_verdict: keep
  consolidate_with: ""
  notes: "CTA at end is correctly formatted with .fl-help-cta class — the only post in this slice with a properly formatted CTA. The TransType historical tangent (2013) feels forced in a 2024 web performance post; tighten or cut it."
---
![](../media/illu/web-fonts-too-heavy-the-fix-1.png){.illu-thumb .illu-index}

You inherit a folder of old PostScript Type 1 fonts.
Or a client sends a family with broken names, duplicate glyphs, and kerning that only
works in one app. You need web fonts that load fast and look right everywhere.

<!-- more -->

![Variable font components in FontLab 8](../media/fl8-head-07-varcomponent.png)

The modern answer is brutally simple: WOFF2, subsetted, one file per family where
possible. WOFF2 compresses better than anything else and every current browser
understands it. Guides from DebugBear and Wholegrain Digital repeat the same checklist:
convert once, subset to the characters you actually use, serve with the right
`@font-face` syntax, and test the waterfall.

Subsetting is where most of the weight goes.
A full Latin-Extended pan-European cut might be 90 KB. A subset that covers only the
characters your homepage actually contains can be 12 KB. The browser does not need every
Vietnamese tone mark on a marketing page that does not contain Vietnamese.

Variable fonts compound the win.
Where a static family meant five separate files for five weights, one variable font
handles the whole range — sometimes for less total bytes than two of the static cuts
combined. The trade-off is that very small variable fonts can be larger than a single
static weight; the fewer weights you use, the closer the break-even point.

In 2013 TransType 4 made the conversion side of that checklist practical.
It reorganised messy families, fixed naming conflicts, generated proper web packages,
and even handled early colour layers.
The same problems still exist today; the tools have just multiplied.
Font Squirrel’s webfont generator and Transfonter handle quick jobs well.
For production families with complex features or legacy sources, a dedicated converter
that preserves OpenType tables and repairs metrics remains the professional choice.

The result is measurable: fewer requests, smaller kilobytes, faster first paint.
Your readers notice only that the page feels crisp and the type never janks.

## References

- [The ultimate guide to font performance — DebugBear](https://www.debugbear.com/blog/website-font-performance)
- [The performance cost of custom web fonts — Wholegrain Digital](https://www.wholegraindigital.com/blog/performant-web-fonts/)
- [TransType — FontLab](https://www.fontlab.com/font-converter/transtype/)
- [Variable fonts on the web — web.dev](https://web.dev/articles/variable-fonts)

[Read more →](https://help.fontlab.com/fontlab/8/manual/){ .fl-help-cta }
