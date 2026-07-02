---
this_file: src_docs/md/posts/2026-06-23-vexy-lines-type-that-reads-the-picture.md
title: "Type that reads the picture underneath it"
authors: [vexy-lines]
date:
  created: 2026-06-23
slug: vexy-lines-type-that-reads-the-picture
---
![A flame rendered entirely from variable-font text, each glyph at its own instance](https://i.vexy.art/vl/case-text/vexy3d-7-after.png){ .illu-thumb .illu-front }

With Vexy Lines, you can make the most of your variable fonts. Create expressive typographic arrangements, impactful headlines and font specimens. Check out the [Vexy Lines Text fill](https://vexy.art/lines/case-typography/)! It typesets your text along the baselines created by the app’s procedural patterns. Each text glyph picks its font size or variable font instance from the brightness of the image beneath it. Sampled per glyph. Mapped to Weight, Width, Optical Size, or any other axis. Exported to SVG & PDF. For foundries who want to show their design spaces flow along pixels.

<!-- more -->

<div class="w-1/2 float-left"><script type="module" src="https://i.vexy.art/dist/lines-nano/vexy-before-after.js"></script><vexy-before-after before="https://i.vexy.art/vl/case-text/vexy3d-7-before.jpg" after="https://i.vexy.art/vl/case-text/vexy3d-7-after.png" before-label="Source image" after-label="Text fill" position="50" direction="horizontal" aspect="1/1" rounded="6px" style="display: block; width: 100%; max-width: 1024px; margin: 0 auto"></vexy-before-after></div>

What do Vexy Lines and FontLab have in common? Same developers, and same passion for high-quality typography. Of course we added a unique typographic gem into our new parametric vector graphics creation app: Text fill!

Drop in a source image, Put a base fill over it, and hide it — Linear, Wave, Circular, Spiral, Handmade, or even Halftone!

Apply Filters like Contrast or Blur to the base fill to tweak the impact of the source image.

Add a Text fill based on the first fill. The pattern paths of the base fill decide where and how the baselines in the Text fill will flow. Enter your text, pick a variable font, nominate a variation axis.

[![](../media/vartypo-futura1.svg){ .ml-[-1em] }](https://vexy.art/lines/case-typography/){ .w-1/1 }

As the text flows along the pattern paths, Vexy Lines samples the image brightness under each glyph, and makes two-fold use of it.

The image brightness modulates the stroke thickness within the thickness range in the hidden base fill. This, in turn, modulates the font size in the Text fill. Lighter pixels — thinner stroke — smaller glyphs. Make the min and max thickness the same for a constant font size.

[![](https://i.vexy.art/vl/case-text/flamesq-141-text.png)](https://vexy.art/lines/case-typography/){ .w-1/2 .float-right .ml-6 .mb-4" }

Additionally, the image brightness directly drives the variable instance selection along the nominated axis, one interpolated instance per glyph. This works even if the min and max stroke thickness are the same. If you choose Weight, light pixels will give you light letters, dark pixels give you bold glyphs.

That makes it a specimen tool, not a gimmick. Instead of nine static cuts you get the full axis rendered continuously across a single word, and the axis can be anything your designspace defines — Weight, Width, Optical Size, a custom grade; the flame poem drives Weight, Width, Italic and Optical Size at once. It works with the real families you already license — Playfair by Claus Eggers Sørensen, Futura, whatever variable font you feed it — and it exports to SVG and PDF, so the finished piece drops straight into the specimen sheet or the deck you were already building.

[![A single line set in a variable font where each glyph takes a different instance sampled from the image beneath it](../media/2026-06-23-typography-specimen.png)](https://vexy.art/lines/case-typography/)

[Discover variable typography in Vexy Lines →](https://vexy.art/lines/case-typography/){ .md-button .md-button--primary }
