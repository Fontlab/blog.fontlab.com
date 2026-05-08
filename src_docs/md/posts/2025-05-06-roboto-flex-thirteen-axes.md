---
this_file: src_docs/md/posts/2025-05-06-roboto-flex-thirteen-axes.md
title: "Roboto Flex and the thirteen axes"
authors: [fontlab]
tags: [variable-fonts, fontlab-8, opentype, roboto]
date:
  created: 2025-05-06
slug: roboto-flex-thirteen-axes
---
![](../media/illu/roboto-flex-thirteen-axes-2.png){.illu-thumb .illu-index}

Christian Robertson drew Roboto in 2011 for Android. Ten years later, David Berlow’s team turned it into something with thirteen knobs.

<!-- more -->

Roboto Flex shipped in September 2021. The team — Santiago Orozco, Irene Vlachou, Ilya Ruderman, Yury Ostromentsky, Mikhail Strukov — inherited the architecture from Amstelvar, Berlow’s 2017 experiment that first tried the parametric idea at scale.

The axis count breaks down like this. Five are standard: `wght`, `wdth`, `opsz`, `GRAD`, `slnt`. Eight are parametric: `XTRA`, `XOPQ`, `YOPQ`, `YTLC`, `YTUC`, `YTAS`, `YTDE`, `YTFI`. The parametric set reaches into the geometry of the letters themselves — x-height separately from cap height, ascenders separately from descenders, contrast separately from overall weight. Things that used to require a new drawing now require a slider.

Eight parametric axes is a lot to hand to a working designer. Type Network built `typeroof` and `videoproof` to demonstrate that the thirteen- dimensional space is actually coherent — that the eye accepts what it sees at every position, not just at the corners. It holds up.

The lesson for anyone working in FontLab 8 isn’t “ship thirteen axes.” Most fonts don’t need three. The lesson is that the toolchain has caught up. Designspace, mastering, delta interpolation, axis validation — the infrastructure that makes something this large work in browsers shipped today is stable. Variable fonts stopped being an experiment somewhere around the time Roboto Flex landed.

Version 3.200 shipped in 2023. The source is on GitHub. It is, as Robertson might say, a complete family.

## References

- [Type Network: Finesse and Express](https://typenetwork.com/articles/finesse-and-express)
- [Roboto Flex on GitHub](https://github.com/googlefonts/roboto-flex)
- [ATypI: Amstelvar and Roboto Flex](https://atypi.org/presentation/amstelvar-and-roboto-flex-unprecedented-flexibility-in-text-typography/)
- [Roboto Flex on Google Fonts](https://fonts.google.com/specimen/Roboto+Flex)

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-7-variable/){ .fl-help-cta }
