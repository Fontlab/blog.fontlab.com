---
this_file: src_docs/md/posts/2016-12-28-deprecated-vs-discontinued.md
title: "Deprecated vs. discontinued"
authors: [fontlab]
date:
  created: 2016-12-28
slug: deprecated-vs-discontinued
review:
  cta_status: todo
  cta_target: "https://www.fontlab.com/"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "Discontinued examples cited: FOGlamp, FontFlasher — verify these were discontinued, not deprecated"
    - "Deprecated examples cited: ScanFont, BitFonter — verify status at time of writing"
    - "BitFonter and ScanFont Mac versions were shipped in a WINE wrapper running the Windows build — verify"
  image_status: missing
  image_needs: ""
  weakness_verdict: keep
  consolidate_with: ""
  notes: "Opinion/explainer that still reads well — a clear distinction between two product end-of-life states. cta_target set to fontlab.com generically; cta_status todo because the product pages it referenced may no longer exist. Original by Thomas Phinney."
---
“Discontinued” and “deprecated” sound like the same thing. At FontLab they mean two different fates for an old product, and the difference matters if you depend on one of them.

<!-- more -->

Every so often a tool we offer gets old and we have no intention of updating it — usually because demand has dried up, or because a newer product does the same job better. What happens next depends on whether anyone is left who genuinely needs it.

**Discontinued** products we drop entirely. No web page, no store listing, no promotion. FOGlamp is a good example: it converted Fontographer’s native files straight to FontLab Studio, and it became unnecessary once newer FontLab Studio versions could simply open those old FOG files. If you ever desperately need a discontinued tool, contact sales — they may be able to help.

**Deprecated** products are a special case. Sometimes a tool ticks two awkward boxes at once:

1. It does not sell enough to justify a new version.
2. Some people who need it have no real alternative — competing products lack the features, do not run on the right operating system, or simply do not exist.

So we keep the page live and continue to sell it, and we label it deprecated. That label means two things:

- We have no current plans to make a new version. Some of its functionality may eventually be folded into another product.
- Support has limits. We still try to help, but a known bug may never get a fix, and our ability to support the tool will gradually decline.

There are also Mac-specific catches for deprecated apps. In some cases — BitFonter and ScanFont among them — the Mac version no longer runs on recent macOS, so we ship the Windows build inside a WINE wrapper. That makes for a larger app running the Windows version under emulation on a Mac.

These older Mac apps also tend not to be Retina-aware. On a double-resolution Retina display they still work, but parts of the interface render at half resolution and look blurry. You can soften this by running the Mac at a higher non-Retina resolution — a trade-off between blur and small interface elements — and utilities such as QuickRes or DisplayMenu give you more resolution choices. (For what it is worth, a few of our current, non-deprecated apps are not Retina-savvy either.)

[Read more →](https://www.fontlab.com/){ .fl-help-cta }
