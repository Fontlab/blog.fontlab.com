---
date:
  created: 2013-11-07
title: "Color font concepts: layers, palettes, scaling, and finiteness"
authors: [adam]
draft: false
---
With four competing color font proposals on the table in 2013, it is worth stepping back
to examine the foundational concepts each one builds on — and what their individual
advantages and blind spots reveal about the broader challenge of adding color to
OpenType. This post covers palettes as a third typographic user-control mechanism, the
analogy between color font formats and display-color history, co-existence with existing
OpenType glyph sources, and the underappreciated virtue of a format that clearly defines
its own limits.

<!-- more -->

*This article is very technical.
No completeness or correctness of the information presented below, and all views are
personal.*

## Personal conclusion

In my view, each of the presented approaches has its advantages and disadvantages.

### The Proposals

The <span class="caps">APP</span> proposal is great in so far that it’s actually already
implemented. However, the interaction of the `sbix` and `glyf` tables as implemented in
Apple OSes has its serious drawbacks (no fallback scenario).
Also, it’s unknown whether the `sbix` table would ever make its way into the official
<span class="caps">ISO</span> <span class="caps">OFF</span> or OpenType specs.

The <span class="caps">MIC</span> proposal only “goes color” in a limited scope — it
provides a way to render multilayer glyphs with solid fills.
But they’re outline glyphs, so they should scale nicely.

The <span class="caps">GOO</span> and <span class="caps">APP</span> proposals use
<span class="caps">PNG</span> as their vehicle, so they can have complex fills but would
fail in high-resolution scenarios.
FreeType already implements the <span class="caps">APP</span> proposal with
<span class="caps">PNG</span> glyph definitions, and the <span class="caps">GOO</span>
proposal — so it looks like adding support for them was quite easy.

The <span class="caps">GOO</span> approach has advantages in so far that it ties into an
existing infrastructure of tables, but my fear is that these existing table concepts may
be abused (no reference to how scaling should happen).
Also, <span class="caps">GOO</span>'s insistence over non-presence of the `glyf` table
is very limiting, and not understandable: they say they want their extensions to go into
the official `EBDT`/`EBLC` tables, but those tables make no such requirement.

In principle, the <span class="caps">MIC</span> and <span class="caps">GOO</span>
approaches could be easily “married together”: the <span class="caps">MIC</span>
proposal would be useful for multilayer glyphs with solid fills, the
<span class="caps">GOO</span> approach for glyphs which require more refined bitmap
treatment, and fallback scenarios could be defined rather well.

The <span class="caps">SVG</span> approach is very welcome, and, as I said, a kind of
“<span class="numbers">2</span>.<span class="numbers">0</span>” thing.
I believe the discussion on them should continue, even if implementations of those could
be confined to only the web browser context.
Also, Firefox actually already implements the <span class="caps">SVG</span> approach,
which is very good news.

### Color Palettes

As for **color palettes**, I consider its addition to font formats (whether through a
unified and further developed `CPAL` table or through several separate mechanisms) as
**third element of typographic user control**.

Historically, the first user control mechanism was just the `cmap` table: the user’s
control over a font was limited to just entering a string of Unicodes, and picking the
font size — and the rest would be done by the font.

The second mechanism was the addition of the `GSUB`/`GPOS` tables: user’s control was
extended by the ability to specify OpenType Layout features that should be applied to
the text.

And now, we’re extending the user’s control by adding ability to specify multiple colors
through the font’s color palette.

### Relation to Existing Solutions

When comparing the **outline color font format** proposals, I would use the following
analogy:

- First personal computers had **black-and-white** monitors so they only could display
  one color. That’s like the current monochrome font formats.
- Then, computers could display **<span class="numbers">16</span> colors** at the time,
  and later even <span class="numbers">256</span> colors.
  The <span class="caps">GIF</span> graphics format dominated the early days of the web,
  and it supported up to <span class="numbers">256</span> colors.
  So that was the “**flat color**” implementation, and that’s exactly what the
  <span class="caps">MIC</span> proposal is.
- Finally, computers gained the possibility to display over
  **<span class="numbers">16</span> million colors**, and graphic formats such as
  <span class="caps">JPG</span> and <span class="caps">PNG</span> were developed to
  support this. That allowed for “**rich color**” applications, and this is analogous to
  the <span class="caps">SVG</span> proposal.

Before color fonts, **OpenType** had three separate possible glyph sources:

- **embedded bitmaps**, which could be monochrome or grayscale, in the
  `bdat`/`bloc`/`EBDT`/`EBLC`/`EBSC` tables
- **TrueType outlines** in the `glyf` table, which was a very straightforward structure
  that allowed little design flexibility but through its sophisticated hinting mechanism
  gave the designer a lot of control over the rasterizer
- **PostScript outlines** in the `CFF` table, which did not give that precise control
  over the rasterizer through hinting, but was a relatively complex structure that came
  “supercharged” with some features that were not fully explored to date: fractional
  point coordinates, the FontMatrix mechanism which allowed on-the-fly skewing, scaling
  or rotation, and even Multiple Master, which was dropped from the spec.

All three solutions “co-existed peacefully” in the monochrome font world.

The <span class="caps">GOO</span> proposal plugs directly into the embedded bitmaps
mechanism, but extends it with color.

The <span class="caps">MIC</span> proposal extends the `glyf` table and provides a
simple solution for “flat colors”, but is quite limited beyond that.
Yet it allows precise hinting.

The <span class="caps">SVG</span> proposal is a cousin of the `CFF` table: it’s
technically the most complex, and requires a very smart, “active” rasterizer.
It does not offer hinting but allows more complex design solutions than the other
proposals.

I hope that a similar “peaceful co-existence” can emerge for the color proposals that
had existed for the monochrome solutions.
Each of them has its merits and none of them is sufficient by its own.

### Finiteness

There is one more consideration that I should mention: “finiteness” of the proposals.
By that I mean whether the limitations of what a given formats aims to achieve in the
end is now clearly defined.
This is closely related to stability of implementations, meaning: if, as a developer, I
invest the time to implement a given format now, will I have to revisit it in the
future?

Superficially, an “extensible” structure is appealing.
“Oh, this structure is infinitely extensible, we can add so many cool stuff to it
later”. But in many cases, an infinitely extensible structure also poses risks.
Software developers have limited time windows to devote to fonts and text technology.
They often want to implement something and be done with it for the next years.
So somewhat paradoxically, a proposal that clearly and consciously states its limits is
actually attractive because it doesn’t leave open questions.

The <span class="caps">GOO</span> proposal seems to be the best example of such
self-limiting format.
It extends the existing embedded bitmap formats by adding just two or so new subformats,
and that’s it. There may be one or two open questions now (the scalability issue I
discussed), but once those are answered, and developers add support for it, it’s a done
deal. The <span class="caps">GOO</span> proposal does not leave many loose ends.

In other words, the <span class="caps">GOO</span> proposal doesn’t try to cook many
dishes at the same time or doesn’t try to be a “catch all solution”.
Instead, it aims to do just one thing, and to do it very well.
Which is, I believe, where its real beauty lies.
Also — just like the older embedded bitmap formats — it can be used to host bitmap-only
glyph data, without any outline fallback.
This actually is quite desirable for some scenarios such as fixed-size devices — simple
electronic displays (brick phones, scrolling electronic banners, diplays in car radios
or other portable electronics).

In constrast, the <span class="caps">APP</span> proposal limits itself very vaguely.
The `sbix` table spec says that it can host a huge variety of possible glyph formats,
from <span class="caps">PNG</span> through <span class="caps">TIFF</span> and
<span class="caps">JPEG</span>, <span class="caps">SVG</span> and
<span class="caps">PDF</span> to even movie clips.
Attractive in principle, it also may be a bit “scary”.
The current <span class="caps">APP</span> implementation isn’t actually `sbix`. It’s
“`sbix` with <span class="caps">PNG</span> glyph data”.
But there could be “`sbix` with <span class="caps">SVG</span> data” or “`sbix` with
<span class="caps">MOV</span> clips”.
This means that develpers who choose to implement “sbix as a whole” may end up
struggling to support various glyph data sources, and they may never be sure whether
something new wouldn’t pop up in future.

The <span class="caps">MIC</span> proposal quite cleanly defines its current scope,
though Greg Hitchcock has suggested during the TypeCon meeting that Microsoft may in
future extend their format to support “more things”, like gradients.
However, knowing Microsoft’s practice, they would most likely extend it in a
transparent, backwards-compatible way (so, for example, a gradient would fall back to a
solid color).
At the current stage of the proposal, `CPAL` and `COLR` are nicely defined.
`CPAL` may undergo some revisions, especially if (hopefully) both the `COLR` and the
`SVG` tables make use it, i.e. if Adobe, Microsoft and Mozilla come to common terms
regarding some minor `CPAL` extensions.

Interestingly, the <span class="caps">SVG</span> in `SFNT` proposal, although very
ambitious in terms of graphic effects you can achieve, is actually fairly clearly
limited. Again, some wrinkles need to be ironed out, and animation is a big open
question, but if we limit ourselves to static SVGs, the principle is very simple: the
<span class="caps">SVG</span> in `SFNT` format only defines a container format for the
data, and clearly **delegates** everything else to the <span class="caps">SVG</span>
standard proper.

This is actually a fairly stable proposal.
It means that, as a developer who implements it, you’ll need to keep up with the
evolution of <span class="caps">SVG</span> proper, but — if you do have an
<span class="caps">SVG</span> renderer implementation — you’ll want to do it anyway.
But the <span class="caps">SVG</span> in `SFNT` makes (more less) a promise that they
won’t bother you greatly with doing big changes in future that will be font-specific.
So as long as you’ve implemented the <span class="caps">SFNT</span> `SVG` table once
(hopefully the revised one which shouls reuse `CPAL`), you’ll be done at the font end.
Then, you’ll just need to keep up with your general <span class="caps">SVG</span>
renderer as you normally would.

So with <span class="caps">SVG</span>, if your application does not have an
<span class="caps">SVG</span> renderer, it’s a “big step” that you’d need to do, but
you’d only need to do it once.
(And perhaps it would be a good idea to do it anyway, since
<span class="caps">SVG</span> is a graphics format that may be useful is supporting
regardless of fonts).
But once you’ve done it, all future steps you’ll have to do will likely be very small
and will “just happen”.

In fact, I think the <span class="caps">GOO</span> mechanism would serve as an ideal
fallback to <span class="caps">SVG</span>. Since <span class="caps">SVG</span> can
contain scalable graphics which intermix vectors and bitmaps, the results can be very
complex. But they could be pre-rendered and put into the `CBDT`/`CBLC` tables as well.
It could be similar to how pre-rendered <span class="caps">PNG</span> bitmaps are (or
used to be) often served by websites to older browsers which don’t support
<span class="caps">SVG</span>. You’d lose the smooth scalability, but you would at least
get the intended glyphs appearance.

## Support by FontLab apps

Fontlab Ltd.
will soon be releasing a free app for Mac and Windows called **FontLab Pad**
which will allow users on both OSes to use fonts that implement any of the above
proposals (currently the <span class="caps">APP</span> and <span class="caps">MIC</span>
formats are implemented but more support is being added as we speak).
Also, FontLab’s **TransType <span class="numbers">4</span>** allows simple creation of
MIC-compatible fonts through overlaying existing “layered fonts” and assigning each
layer a color. TransType can also output APP-compatible fonts with the same contents.
In combination with FontLab’s **BitFonter <span class="numbers">3</span>**, TransType
<span class="numbers">4</span> can be used to produce sophisticated full-bitmap color
fonts in the APP-compatible format.

At FontLab, we are very happy with this development and support it fully.
Our upcoming font editors will support multicolor fonts natively, with layers and
potentially also complex fills, so fonts in all color formats (including
<span class="caps">SVG</span>) can be created.

## More on color fonts

- [Color fonts: the moment has arrived](2013-09-19-color-font-format-proposals.md)
- [The four color-font proposals: APP, COLR/CPAL, CBDT/CBLC, and SVG](2013-10-10-color-font-proposals-detailed.md)
