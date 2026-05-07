---
date:
  created: 2013-09-19
title: "Color fonts: Overview of proposals for color extensions of OpenType"
categories:
  - blog
author: adam
draft: false
---

# Color fonts. Overview of the proposals for color extensions of the OpenType font format.

By [Adam
Twardoch](https://www.fontlab.com/author/adamtwr39258/ "Adam Twardoch")
on 2013-09-19 in
<a href="https://www.fontlab.com/news/" rel="category tag">News</a>

Although Fontlab Ltd. debuted the Photofont technology some
<span class="numbers">8</span> years ago, the typographic community did
not show much interest for multi-color fonts or typography. In
<span class="numbers">2013</span>, it changed. Actually, this started
a few years ago with Apple introducing the color emoji font into iOS,
and then Mac <span class="caps">OS</span>
X <span class="numbers">10</span>.<span class="numbers">7</span>. Now,
all major industry players (Apple, Adobe, Mozilla, Google and Microsoft)
have proposed their formats, which aim to extend the OpenType font
format by the ability of including color glyph information. The
proposals differ in many aspects. Below is a discussion of the proposals
along with some personal comments.

<span id="more-40"></span>

*This article is very technical. No completeness or correctness of the
information presented below, and all views are personal.*

<img src="https://i.ytimg.com/vi/Yit1ZpClwAk/maxresdefault.jpg"
class="epyt-facade-poster skip-lazy" decoding="async"
data-spai-excluded="true" loading="lazy"
alt="Color Fonts. The next big thing? FontLab tutorial with Adam Twardoch" />

![](data:image/svg+xml;base64,PHN2ZyBkYXRhLW5vLWxhenk9IjEiIGhlaWdodD0iMTAwJSIgdmVyc2lvbj0iMS4xIiB2aWV3Ym94PSIwIDAgNjggNDgiIHdpZHRoPSIxMDAlIj48cGF0aCBjbGFzcz0icGFyYSIgZD0iTTY2LjUyLDcuNzRjLTAuNzgtMi45My0yLjQ5LTUuNDEtNS40Mi02LjE5QzU1Ljc5LC4xMywzNCwwLDM0LDBTMTIuMjEsLjEzLDYuOSwxLjU1IEMzLjk3LDIuMzMsMi4yNyw0LjgxLDEuNDgsNy43NEMwLjA2LDEzLjA1LDAsMjQsMCwyNHMwLjA2LDEwLjk1LDEuNDgsMTYuMjZjMC43OCwyLjkzLDIuNDksNS40MSw1LjQyLDYuMTkgQzEyLjIxLDQ3Ljg3LDM0LDQ4LDM0LDQ4czIxLjc5LTAuMTMsMjcuMS0xLjU1YzIuOTMtMC43OCw0LjY0LTMuMjYsNS40Mi02LjE5QzY3Ljk0LDM0Ljk1LDY4LDI0LDY4LDI0UzY3Ljk0LDEzLjA1LDY2LjUyLDcuNzR6IiBmaWxsPSIjZjAwIiAvPjxwYXRoIGQ9Ik0gNDUsMjQgMjcsMTQgMjcsMzQiIGZpbGw9IiNmZmYiIGNsYXNzPSJwYXJhIiAvPjwvc3ZnPg==)

<span itemprop="video" itemscope=""
itemtype="http://schema.org/VideoObject"></span>

The video tutorial by Adam Twardoch accompanies this article by
providing a more practical take on color font creation issues.

## Concepts

There are several conceptual approaches for “color fonts” that can be
considered, in increasing order of complexity:

- a\] per-PPM bitmap strike definition, without any scaling
- b\] scalable bitmap glyphs with multiple “master
  <span class="caps">PPM</span> sizes”
- c\] one scalable bitmap glyph definition across all PPMs
- d\] layered outline glyphs, one solid fill per layer
- e\] static outline glyphs with complex fills and optional bitmap
  content
- f\] animated variant of e\]

## Approaches

We have now four distinct approaches from the major vendors, in
increasing order of complexity:

- <span class="caps">GOO</span>: Google `CBDT`/`CBLC` tables — a\] or
  b\], unclear
- <span class="caps">APP</span>: Apple `sbix` table — b\] concept
- <span class="caps">MIC</span>: Microsoft `COLR`/`CPAL` tables — d\]
  concept
- <span class="caps">SVG</span>: Joint Adobe and Mozilla `SVG`
   table — e\] concept, possibly expandable to f\]

## Considerations

There are also several considerations, or aspects, which each
implementation needs to address.

- **Co-existence**: regardless of the possible size inflation, whether
  several approach can co-exist within the same `SFNT` font file. This
  includes questions such as precedence (what should happen if
  a consuming platform “understands” multiple approaches) or structure
  sharing (whether the same structure, e.g. the
  <span class="caps">PNG</span> image data or a color palette, can be
  shared by multiple approaches). In particular, the question of
  co-existence of the new structures with old ones (`glyf` or `CFF`
   table) is important.
- **External modification**: especially with the outline approaches,
  whether the colors specified within the `SFNT` font file can somehow
  be manipulated/modified externally by the consuming platforms. This
  also includes more specific questions such as, in case of the
  SVG-based approaches, controlling animation or, if the consuming
  platform is a web browser, interaction with the document’s
  <span class="caps">DOM</span>.
- **Fallback/degradation**: related to co-existence, how the color data
  should be represented in environments that only support grayscale or
  even monochrome data. Adobe’s Leonard Rosenthol has raised a number of
  fundamental issues on this in context of the
  <span class="caps">SVG</span> discussion. The discussion makes,
  I hope, an interesting read: the “Glyph bbox concerns” thread,
  \[<span class="numbers">1</span>\] and
  \[<span class="numbers">2</span>\].
- \[<span class="numbers">1</span>\]  <a
  href="http://lists.w3.org/Archives/Public/public-svgopentype/2012Jun/thread.html"
  rel="nofollow">http://​lists​.w<span
  class="numbers">3</span>​.org/​A​r​c​h​i​v​e​s​/​P​u​b​l​i​c​/​p​u​b​l​i​c​-​s​v​g​o​p​e​n​t​y​p​e​/​<span
  class="numbers">2</span>​<span class="numbers">0</span>​<span
  class="numbers">1</span>​<span
  class="numbers">2</span>​J​u​n​/​t​h​r​e​a​d​.​h​tml</a>
- \[<span class="numbers">2</span>\]  <a
  href="http://lists.w3.org/Archives/Public/public-svgopentype/2012Aug/thread.html"
  rel="nofollow">http://​lists​.w<span
  class="numbers">3</span>​.org/​A​r​c​h​i​v​e​s​/​P​u​b​l​i​c​/​p​u​b​l​i​c​-​s​v​g​o​p​e​n​t​y​p​e​/​<span
  class="numbers">2</span>​<span class="numbers">0</span>​<span
  class="numbers">1</span>​<span
  class="numbers">2</span>​A​u​g​/​t​h​r​e​a​d​.​h​tml</a>

## Detailed discussion of approaches

### <span class="caps">GOO</span>: Google `CBDT`/`CBLC` tables

Bitmap-based (<span class="caps">PNG</span>) glyphs, either as per-PPM
bitmap strike definition, without any scaling, or as scalable bitmap
glyphs with multiple “master <span class="caps">PPM</span> sizes” — this
is unclear (see below for details).

Announced in May <span class="numbers">2013</span> on the Google blog
\[<span class="caps">GOO<span class="numbers">1</span></span>\], this is
an approach which specifies two tables (`CBDT`/`CBLC`,
\[<span class="caps">GOO<span class="numbers">2</span></span>\]), which
in turn extend the existing OpenType `EBDT`/`EBLC` tables
\[<span class="caps">GOO<span class="numbers">3</span></span>\],
\[<span class="caps">GOO<span class="numbers">4</span></span>\] by
adding the ability to include uncompressed color images or
<span class="caps">PNG</span> images. Those, in turn, are extended
version of Apple’s original `bdat`/`bloc` tables which have a long
history.

Google hosts a “Color Emoji” project dedicated to this
\[<span class="caps">GOO<span class="numbers">5</span></span>\], have
created a Python tool which embeds PNGs into that table
\[<span class="caps">GOO<span class="numbers">6</span></span>\] and have
provided sample fonts. FreeType
<span class="numbers">2</span>.<span class="numbers">5</span> now also
includes support for this
\[<span class="caps">GOO<span class="numbers">7</span></span>\], added
on May <span class="numbers">29</span><sup>th</sup>.

*Co-existence:* The <span class="caps">GOO</span> proposal states: “It
is recommended that such fonts include no `glyf` table, and as such be
bitmap-only fonts. In the presence of color and non-color strikes in the
same font, it is currently unspecified which bitmap a conformant client
will choose for rendering.”. While this does not directly invalidate
co-existence, it raises a valid question (for co-existence in general,
and for precedence in particular). However, in Microsoft’s and Apple’s
traditional implementations of the TrueType rasterizer (before
ClearType), the bdat/bloc and `EBDT`/`EBLC` tables worked so that if
a bitmap strike was available for a given <span class="caps">PPM</span>,
it was used, otherwise the outline glyph was rendered from the `glyf`
table (even for the same glyph but different
<span class="caps">PPM</span>). I definitely think that all consuming
platforms which support the <span class="caps">GOO</span> approach
should adopt the aforementioned principle. This is especially crucial
when it comes to co-existence between the <span class="caps">GOO</span>
proposal and the <span class="caps">MIC</span> proposal. If the
<span class="caps">GOO</span> approach behaves as I described, then
chances are that one font could include the `CBDT`, `CBLC`, `COLR`,
`CPAL` and glyf tables, and the consuming platform could easily choose
whether to use the <span class="caps">GOO</span> approach first, and
then (for different <span class="caps">PPM</span> sizes or glyphs which
are not supported by the <span class="caps">GOO</span> tables) use the
<span class="caps">MIC</span> approach (or just the plain `glyf` table).
*External modification:* While some people have generally voiced their
desire to be able to manipulate colors that are embedded inside of
a font file externally, I think in case of PNG-based glyphs, this should
be, if at all, a post-processing step (after the glyph images have been
retrieved from the scaler). *Fallback/degradation:* the
<span class="caps">GOO</span> spec includes provisions as to how the
color bitmap data should be transformed into grayscale bitmap data.
*Unclear:* The OpenType spec also includes the `EBSC` table
\[<span class="caps">GOO<span class="numbers">8</span></span>\] which
defines which per-PPM strikes should be used for which
<span class="caps">PPM</span> ranges when they need to be scaled.
Without `EBSC`, it is assumed that the `EBDT`/`EBLC` strikes are only
rendered for the specified <span class="caps">PPM</span>. The
<span class="caps">GOO</span> proposal makes no mention of how scaling
should be implemented, or whether a scaler should rely on the presence
of the `EBSC` table. I **strongly** think that, should the
<span class="caps">GOO</span> proposal aim at wider adoption, it should
strictly follow the principle laid out in the OpenType spec: if no
`EBSC` table is present, strikes should be rendered only at given PPMs.
For scaling, it should refer to the `EBSC` table. It’s also unclear to
me what FreeType
<span class="numbers">2</span>.<span class="numbers">5</span> is doing
at this point, and whether support for `EBSC` is planned.

- \[<span class="caps">GOO<span class="numbers">1</span></span>\] 
  [http://​google​-opensource​.blogspot​.de/​<span class="numbers">2</span>​<span class="numbers">0</span>​<span class="numbers">1</span>​<span class="numbers">3</span>​/​<span class="numbers">0</span>​<span class="numbers">5</span>​/​o​p​e​n​-​s​t​a​n​d​a​r​d​-​c​o​l​o​r​-​f​o​n​t​-​f​u​n​-​f​o​r​.​h​tml](http://google-opensource.blogspot.de/2013/05/open-standard-color-font-fun-for.html)
- \[<span class="caps">GOO<span class="numbers">2</span></span>\] 
  [https://​color​-emoji​.googlecode​.com/​g​i​t​/​s​p​e​c​i​f​i​c​a​t​i​o​n​/​v​<span class="numbers">1</span>​.​h​tml](https://color-emoji.googlecode.com/git/specification/v1.html)
- \[<span class="caps">GOO<span class="numbers">3</span></span>\] 
  [http://​www​.microsoft​.com/​t​y​p​o​g​r​a​p​h​y​/​o​t​s​p​e​c​/​e​b​d​t​.​htm](http://www.microsoft.com/typography/otspec/ebdt.htm)
- \[<span class="caps">GOO<span class="numbers">4</span></span>\] 
  [http://​www​.microsoft​.com/​t​y​p​o​g​r​a​p​h​y​/​o​t​s​p​e​c​/​e​b​l​c​.​htm](http://www.microsoft.com/typography/otspec/eblc.htm)
- \[<span class="caps">GOO<span class="numbers">5</span></span>\] 
  [https://​code​.google​.com/​p​/​c​o​l​o​r​-​e​m​o​ji/](https://code.google.com/p/color-emoji/)
- \[<span class="caps">GOO<span class="numbers">6</span></span>\] 
  [https://​code​.google​.com/​p​/​c​o​l​o​r​-​e​m​o​j​i​/​s​o​u​r​c​e​/​b​r​o​w​se/](https://code.google.com/p/color-emoji/source/browse/)
- \[<span class="caps">GOO<span class="numbers">7</span></span>\] 
  [http://​git​.savannah​.gnu​.org/​c​g​i​t​/​f​r​e​e​t​y​p​e​/​f​r​e​e​t​y​p​e​<span class="numbers">2</span>​.​g​it/](http://git.savannah.gnu.org/cgit/freetype/freetype2.git/)
- \[<span class="caps">GOO<span class="numbers">8</span></span>\] 
  [https://​www​.microsoft​.com/​t​y​p​o​g​r​a​p​h​y​/​o​t​s​p​e​c​/​e​b​s​c​.​htm](https://www.microsoft.com/typography/otspec/ebsc.htm)

### <span class="caps">APP</span>: Apple `sbix` table

In the current implementation: bitmap-based
(<span class="caps">PNG</span>) glyphs, as scalable bitmap glyphs with
multiple “master strikes” per <span class="caps">PPM</span>. The `sbix`
spec has provisions to hold other types of glyph definitions, such as
<span class="caps">TIFF</span>, <span class="caps">SVG</span>,
<span class="caps">PDF</span> or even movie clips, but this is not very
clearly specified nor implemented.

Apple’s is the first implementation that has been officially deployed.
It was introduced to iOS <span class="numbers">4</span> and also runs in
CoreText applications Mac <span class="caps">OS</span>
X <span class="numbers">10</span>.<span class="numbers">7</span> and
newer. It does not run on <span class="caps">ATSUI</span> applications
such as Pages <span class="numbers">09</span> or Keynote
<span class="numbers">09</span>, but does work in CoreText applications
such as TextEdit or Safari. Support for `sbix` table with
<span class="caps">PNG</span> glyph has also been added to FreeType.

The spec of the table has not been officially published by Apple, but
has been shared with interested developers. The implementation hosts
<span class="caps">PNG</span> data inside the `sbix` table, with
multiple <span class="caps">PPM</span> “master bitmaps” possible per
glyph. The scaler is responsible for choosing the most appropriate
<span class="caps">PPM</span> size and scale it to other
<span class="caps">PPM</span> sizes as needed.

It seems that per “master strike”, both the
<span class="caps">PPM</span> and <span class="caps">DPI</span>
information can be provided. For the metrics, the implementation relies
on the bounding boxes stored in the `glyf` table. It seems that, very
unfortunately, the Apple implementation renders the contents of a `glyf`
table glyph, and the on top it renders its associated bitmap — so if
bitmaps are available in the `sbix` table for a particular glyph
<span class="caps">ID</span>, the corresponding `glyf` glyph
<span class="caps">ID</span> slot has to be empty.

Mac <span class="caps">OS</span>
X <span class="numbers">10</span>.<span class="numbers">8</span>
includes one font with the `sbix` table: Apple Color Emoji, while iOS
<span class="numbers">6</span> includes the former along with Apple
Color Emoji@<span class="numbers">2</span> (the latter hosting the
glyphs in double <span class="caps">DPI</span> resolution, it appears).

A reverse-engineered incomplete and faulty spec has been published
\[<span class="caps">APP<span class="numbers">1</span></span>\] and
\[<span class="caps">APP<span class="numbers">2</span></span>\], and
a patch for fontTools/<span class="caps">TTX</span> has been published
\[<span class="caps">APP<span class="numbers">3</span></span>\]. Those
do not seem to work correctly, though. However, Fontlab Ltd. has
implemented its own `sbix` reading and writing, which seems to work
correctly. Fontlab Ltd. also has its own `sbix` renderer, and I have
successfully built Latin-script color fonts with the `sbix` table and
OpenType Layout features such as `calt`, and that font works as expected
in Mac <span class="caps">OS</span>
X <span class="numbers">10</span>.<span class="numbers">7</span> and
<span class="numbers">10</span>.<span class="numbers">8</span>
(hooray!).

*Co-existence:* The fact that the `sbix` implementation in Apple OSes
seems to require that the `glyf` glyphs are blank raises a big
co-existence concern. In particular, it seems that this approach could
not co-exist with the <span class="caps">MIC</span> approach, which is
a pity. I see that as a weakness of the <span class="caps">APP</span>
approach. As for the co-existence of the <span class="caps">APP</span>
and <span class="caps">GOO</span> approaches, it seems somewhat unclear
to me. The <span class="caps">APP</span> approach requires both `sbix`
and `glyf` to be present, while currently, the
<span class="caps">GOO</span> approach discourages the presence of
`glyf`. I see it as a weakness of both approaches (more strongly of the
<span class="caps">GOO</span> approach). Also, there is the question of
data duplication. Theoretically, I imagine that a smart mechanism (akin
to `TTC`) could allow for some data sharing, wherein both the `sbix`
table and the `CBLC` table referred to the same
<span class="caps">PNG</span> chunks. But I’m not sure if offsets that
go beyond defined table boundaries are permitted in the
<span class="caps">OT</span> spec (I don’t think they are). *External
modification:* While some people have generally voiced their desire to
be able to manipulate colors that are embedded inside of a font file
externally, I think in case of PNG-based glyphs, this should be, if at
all, a post-processing step (after the glyph images have been retrieved
from the scaler). *Fallback/degradation:* the
<span class="caps">APP</span> implementation does not have any clear
provisions for fallback/degradation. A renderer could fall back to
grayscale or monochrome (dithered) versions of the `sbix`
<span class="caps">PNG</span> glyphs, but it would be desirable if it
could also fall back to “proper” `glyf` outline glyphs. However, the
fact that the <span class="caps">APP</span> implementation relies on
**empty** `glyf` glyphs invalidates that. *Unclear:* It’s not currently
clear how the
<span class="caps">PPM</span>+<span class="caps">DPI</span> “master
strikes” should be chosen and scaled, but my assumption is that the
<span class="caps">APP</span> approach explicitly assumes that the
`sbix` glyphs are scalable, without the need for an additional `EBSC`
table. This may be disputable. Also, it’s not entirely clear to me how
a renderer should make use of the <span class="caps">PPM</span> and
<span class="caps">DPI</span> information, though by itself it seems
rather straightforward.

- \[<span class="caps">APP<span class="numbers">1</span></span>\] 
  [http://​typophile​.com/​n​o​d​e​/​<span class="numbers">9</span>​<span class="numbers">6</span>​<span class="numbers">6</span>​<span class="numbers">7</span>​<span class="numbers">1</span>​#​c​o​m​m​e​n​t​-​<span class="numbers">5</span>​<span class="numbers">2</span>​<span class="numbers">4</span>​<span class="numbers">375</span>](http://typophile.com/node/96671#comment-524375)
- \[<span class="caps">APP<span class="numbers">2</span></span>\] 
  [http://​kanji​-database​.sourceforge​.net/​f​o​n​t​s​/​o​p​e​n​t​y​p​e​.​h​tml](http://kanji-database.sourceforge.net/fonts/opentype.html)
- \[<span class="caps">APP<span class="numbers">3</span></span>\] 
  [https://​gist​.github​.com/​j​j​g​o​d​/​<span class="numbers">5</span>​<span class="numbers">4</span>​<span class="numbers">7</span>​<span class="numbers">8</span>​<span class="numbers">229</span>](https://gist.github.com/jjgod/5478229)

### <span class="caps">MIC</span>: Microsoft `COLR`/`CPAL` tables

The newest member in the family of solutions, announced by Microsoft’s
Michelle Perham and Si Daniels on June
<span class="numbers">26</span><sup>th</sup>
\[<span class="caps">MIC<span class="numbers">1</span></span>\], the
Microsoft proposal looks quite simple and clever to me, judging from the
announcement. It adds a relatively lightweight baggage of `COLR` and
`CPAL` tables which results in layered outline glyphs with one solid
fill per layer.

The <span class="caps">MIC</span> approach is implemented in Windows
<span class="numbers">8</span>.<span class="numbers">1</span>, with
a new Segoe <span class="caps">UI</span> Emoji font being included in
the <span class="caps">OS</span>. A video from Microsoft’s Dan McLachlan
talk where he presents the approach is available
\[<span class="caps">MIC<span class="numbers">2</span></span>\] (about
<span class="numbers">9</span> minutes into the talk). Also, Michelle
Perham made a presentation at TypeCon <span class="numbers">2013</span>
dedicated to the topic.

The approach uses a base glyph (`glyf` or, presumably, also `CFF` )
which is used for non-color situations. The `COLR` table refers from
this glyph into other outline glyphs (which exist within the same
table), which serve as layers. Each “layer glyph” has its own z‑order
and a single color references. The color references are handled has
palette indices, with a separate table, `CPAL` in OpenType that resolves
the <span class="caps">RGBA</span> colors actually used for the glyph.
Therefore, both the `COLR` and the `CPAL` tables should be quite small
in size, all the heavy-lifting being done by the traditional rendering
methods. It was announced that Microsoft plans to publish the specs for
the tables within the next few weeks.

*Co-existence:* If the <span class="caps">GOO</span> approach clarifies
its behavior when the `glyf` table is present, then the
<span class="caps">MIC</span> approach could co-exist easily with the
<span class="caps">GOO</span> approach. Actually, these two approaches
could cleverly echo the former co-existence of `glyf` with
`bdat`/`bloc` (or `EBDT`/`EBLC`/`EBSC`). A consuming platform could go
straight for the monochrome `glyf` glyphs, or could prioritize the
<span class="caps">MIC</span> approach with a fallback to `glyf`, or
could prioritize the <span class="caps">GOO</span> approach with
a fallback to `glyf`, or could prioritize the
<span class="caps">GOO</span> approach, then fall back to the
<span class="caps">MIC</span> approach, and then finally fall back to
`glyf`. I don’t see any principal conflict there. *External
modification:* As Michelle wrote on the OpenType list, “Fonts can have
multiple palettes, but right now the colors are defined by the font
developer and the user is not able to make changes to the palettes.
That’s definitely something we’d like to consider in the future and
might be something that applications could expose.” At TypeCon, Greg
Hitchcock clarified the envisioned roles of the palettes: first palette
is used by default for “dark on light” color situations while second
palette is intended for use in “light on dark” situations. Additional
palettes should be selectable by the user. *Fallback/degradation:* This
approach seems to be degrading nicely, and fallback implications have
been discussed above.

- \[<span class="caps">MIC<span class="numbers">1</span></span>\] 
  [http://​typophile​.com/​n​o​d​e​/​<span class="numbers">1</span>​<span class="numbers">0</span>​<span class="numbers">4</span>​<span class="numbers">174</span>](http://typophile.com/node/104174)
- \[<span class="caps">MIC<span class="numbers">2</span></span>\] 
  [http://​channel<span class="numbers">9</span>​.msdn​.com/​E​v​e​n​t​s​/​B​u​i​l​d​/​<span class="numbers">2</span>​<span class="numbers">0</span>​<span class="numbers">1</span>​<span class="numbers">3</span>/<span class="numbers">3</span> – <span class="numbers">191</span>](http://channel9.msdn.com/Events/Build/2013/3-191)

### <span class="caps">SVG</span>: Joint Adobe and Mozilla `SVG`  table

The “full Monty” outline+bitmap (<span class="caps">SVG</span>) glyphs
with possible animation.

This is a proposal formulated by Mozilla’s Edwin Flores and Cameron
McCormack, with input from Robert O’Callahan and Adobe’s Sairus Patel,
which has been submitted as <s>an unofficial editor’s draft</s> a Final
Community Group Specification to the
<span class="caps">W<span class="numbers">3</span>C</span>
\[<span class="caps">SVG<span class="numbers">1</span></span>\]. There
is a reasonably well-working <span class="caps">SVG</span> OpenType
community for this
\[<span class="caps">SVG<span class="numbers">3</span></span>\] and
a public mailing list
\[<span class="caps">SVG<span class="numbers">2</span></span>\]. As
indicated on Robert O’Callahan’s blog
\[<span class="caps">SVG<span class="numbers">4</span></span>\], this
proposal has been implemented in Firefox — it’s off by default but can
be enabled by toggling `gfx.font_rendering.opentype_svg.enabled` in
about:config. Also, a tool, written in Python, is available to create
such fonts
\[<span class="caps">SVG<span class="numbers">5</span></span>\].

This is the by-far most complex proposal, as it puts the bar quite high
for implementers (it requires a full <span class="caps">SVG</span>
renderer, and has provisions for animated glyphs). On the other hand,
its great advantage is that, once an app has access to the
<span class="caps">SVG</span> renderer, it can delegate the rendering of
the glyphs completely to the <span class="caps">SVG</span> library. So
the app only needs to call an OpenType Layout library to perform the
layout, and then call the <span class="caps">SVG</span> renderer for
each glyph, and position the rendered bitmaps. So in fact in an
SVG-compatible environment using the <span class="caps">SVG</span> table
would be trivial.

The <span class="caps">SVG</span> proposal allows for designs that
cannot be achieved by the other solutions: it implements “rich color”
(with gradients etc.), allows for drawing various strokes and, of
course, intermixing vectors and bitmaps. So it’s potentially very very
powerful.

Sairus Patel explained to me at TypeCon that he considers the current
proposed spec as “good to go”, and that’s the spec that is implemented
in Firefox.

This approach really is an entirely different animal than all of the
above. I can easily imagine that the <span class="caps">APP</span>,
<span class="caps">GOO</span> and <span class="caps">MIC</span>
approaches are all some kind of “color fonts
<span class="numbers">1</span>.<span class="numbers">0</span>”, while
the <span class="caps">SVG</span> proposal is “color fonts
<span class="numbers">2</span>.<span class="numbers">0</span>”. There’s
is an ongoing debate on the public mailing list of the
<span class="caps">W<span class="numbers">3</span>C</span> community, so
I won’t get into a detailed discussion here (also because I don’t quite
understand some of the complexities involved). I definitely think,
though, that this approach can co-exist with all the previous ones. One
potential co-existence benefit could be if the `SVG`  table co-exists
with the <span class="caps">MIC</span> `CPAL` table. The
<span class="caps">SVG</span> glyphs could potentially make references
to the color palettes specified within `CPAL`, and if — in future — some
means to externally manipulate the `CPAL` palettes were implemented in
consuming platforms, both the <span class="caps">MIC</span> approach and
the <span class="caps">SVG</span> approach could benefit from that
development. In the light of the <span class="caps">MIC</span> proposal,
Sairus Patel mentioned to me that he might consider proposing some
extensions to the Microsoft `CPAL` table, and then would consider
dropping the color palette format proposed in the
<span class="caps">SVG</span> spec — so that ultimately both the
<span class="caps">MIC</span> and the <span class="caps">SVG</span>
formats could use the `CPAL` table.

- \[<span class="caps">SVG<span class="numbers">1</span></span>\]  [http://​www​.w<span class="numbers">3</span>​.org/​<span class="numbers">2</span>​<span class="numbers">0</span>​<span class="numbers">1</span>​<span class="numbers">3</span>​/​<span class="numbers">1</span>​<span class="numbers">0</span>​/​S​V​G​\_​i​n​\_​O​p​e​n​T​y​pe/](http://www.w3.org/2013/10/SVG_in_OpenType/)
- \[<span class="caps">SVG<span class="numbers">2</span></span>\] 
  [http://​www​.w<span class="numbers">3</span>​.org/​c​o​m​m​u​n​i​t​y​/​s​v​g​o​p​e​n​t​y​pe/](http://www.w3.org/community/svgopentype/)
- \[<span class="caps">SVG<span class="numbers">3</span></span>\] 
  [http://​lists​.w<span class="numbers">3</span>​.org/​A​r​c​h​i​v​e​s​/​P​u​b​l​i​c​/​p​u​b​l​i​c​-​s​v​g​o​p​e​n​t​y​pe/](http://lists.w3.org/Archives/Public/public-svgopentype/)
- \[<span class="caps">SVG<span class="numbers">4</span></span>\] 
  [http://​robert​.ocallahan​.org/​<span class="numbers">2</span>​<span class="numbers">0</span>​<span class="numbers">1</span>​<span class="numbers">3</span>​/​<span class="numbers">0</span>​<span class="numbers">2</span>​/​s​v​g​-​i​n​-​o​p​e​n​t​y​p​e​-​n​e​w​-​a​p​p​r​o​a​c​h​-​t​o​-​s​v​g​.​h​tml](http://robert.ocallahan.org/2013/02/svg-in-opentype-new-approach-to-svg.html)
- \[<span class="caps">SVG<span class="numbers">5</span></span>\] 
  [https://​github​.com/​e​d​f​<span class="numbers">8</span>​<span class="numbers">2</span>​<span class="numbers">5</span>​/​S​V​G​-​O​p​e​n​T​y​p​e​-​U​t​ils](https://github.com/edf825/SVG-OpenType-Utils)

## Personal conclusion

In my view, each of the presented approaches has its advantages and
disadvantages.

### The Proposals

The <span class="caps">APP</span> proposal is great in so far that it’s
actually already implemented. However, the interaction of the `sbix` and
`glyf` tables as implemented in Apple OSes has its serious drawbacks (no
fallback scenario). Also, it’s unknown whether the `sbix` table would
ever make its way into the official <span class="caps">ISO</span>
<span class="caps">OFF</span> or OpenType specs.

The <span class="caps">MIC</span> proposal only “goes color” in
a limited scope — it provides a way to render multilayer glyphs with
solid fills. But they’re outline glyphs, so they should scale nicely.

The <span class="caps">GOO</span> and <span class="caps">APP</span>
proposals use <span class="caps">PNG</span> as their vehicle, so they
can have complex fills but would fail in high-resolution scenarios.
FreeType already implements the <span class="caps">APP</span> proposal
with <span class="caps">PNG</span> glyph definitions, and the
<span class="caps">GOO</span> proposal — so it looks like adding support
for them was quite easy.

The <span class="caps">GOO</span> approach has advantages in so far that
it ties into an existing infrastructure of tables, but my fear is that
these existing table concepts may be abused (no reference to how scaling
should happen). Also, <span class="caps">GOO</span>’s insistence over
non-presence of the `glyf` table is very limiting, and not
understandable: they say they want their extensions to go into the
official `EBDT`/`EBLC` tables, but those tables make no such
requirement.

In principle, the <span class="caps">MIC</span> and
<span class="caps">GOO</span> approaches could be easily “married
together”: the <span class="caps">MIC</span> proposal would be useful
for multilayer glyphs with solid fills, the
<span class="caps">GOO</span> approach for glyphs which require more
refined bitmap treatment, and fallback scenarios could be defined rather
well.

The <span class="caps">SVG</span> approach is very welcome, and, as
I said, a kind of
“<span class="numbers">2</span>.<span class="numbers">0</span>” thing.
I believe the discussion on them should continue, even if
implementations of those could be confined to only the web browser
context. Also, Firefox actually already implements the
<span class="caps">SVG</span> approach, which is very good news.

### Color Palettes

As for **color palettes**, I consider its addition to font formats
(whether through a unified and further developed `CPAL` table or through
several separate mechanisms) as **third element of typographic user
control**.

Historically, the first user control mechanism was just the `cmap`
table: the user’s control over a font was limited to just entering
a string of Unicodes, and picking the font size — and the rest would be
done by the font.

The second mechanism was the addition of the `GSUB`/`GPOS` tables:
user’s control was extended by the ability to specify OpenType Layout
features that should be applied to the text.

And now, we’re extending the user’s control by adding ability to specify
multiple colors through the font’s color palette.

### Relation to Existing Solutions

When comparing the **outline color font format** proposals, I would use
the following analogy:

- First personal computers had **black-and-white** monitors so they only
  could display one color. That’s like the current monochrome font
  formats.
- Then, computers could display **<span class="numbers">16</span>
  colors** at the time, and later even <span class="numbers">256</span>
  colors. The <span class="caps">GIF</span> graphics format dominated
  the early days of the web, and it supported up to
  <span class="numbers">256</span> colors. So that was the “**flat
  color**” implementation, and that’s exactly what the
  <span class="caps">MIC</span> proposal is.
- Finally, computers gained the possibility to display
  over **<span class="numbers">16</span> million colors**, and graphic
  formats such as <span class="caps">JPG</span> and
  <span class="caps">PNG</span> were developed to support this. That
  allowed for “**rich color**” applications, and this is analogous to
  the <span class="caps">SVG</span> proposal.

Before color fonts, **OpenType** had three separate possible glyph
sources:

- **embedded bitmaps**, which could be monochrome or grayscale, in the
  `bdat`/`bloc`/`EBDT`/`EBLC`/`EBSC` tables
- **TrueType outlines** in the `glyf` table, which was a very
  straightforward structure that allowed little design flexibility but
  through its sophisticated hinting mechanism gave the designer a lot of
  control over the rasterizer
- **PostScript outlines** in the `CFF`  table, which did not give that
  precise control over the rasterizer through hinting, but was
  a relatively complex structure that came “supercharged” with some
  features that were not fully explored to date: fractional point
  coordinates, the FontMatrix mechanism which allowed on-the-fly
  skewing, scaling or rotation, and even Multiple Master, which was
  dropped from the spec.

All three solutions “co-existed peacefully” in the monochrome
font world.

The <span class="caps">GOO</span> proposal plugs directly into the
embedded bitmaps mechanism, but extends it with color.

The <span class="caps">MIC</span> proposal extends the `glyf` table and
provides a simple solution for “flat colors”, but is quite limited
beyond that. Yet it allows precise hinting.

The <span class="caps">SVG</span> proposal is a cousin of the `CFF`
 table: it’s technically the most complex, and requires a very smart,
“active” rasterizer. It does not offer hinting but allows more complex
design solutions than the other proposals.

I hope that a similar “peaceful co-existence” can emerge for the color
proposals that had existed for the monochrome solutions. Each of them
has its merits and none of them is sufficient by its own.

### Finiteness

There is one more consideration that I should mention: “finiteness” of
the proposals. By that I mean whether the limitations of what a given
formats aims to achieve in the end is now clearly defined. This is
closely related to stability of implementations, meaning: if, as
a developer, I invest the time to implement a given format now, will
I have to revisit it in the future?

Superficially, an “extensible” structure is appealing. “Oh, this
structure is infinitely extensible, we can add so many cool stuff to it
later”. But in many cases, an infinitely extensible structure also poses
risks. Software developers have limited time windows to devote to fonts
and text technology. They often want to implement something and be done
with it for the next years. So somewhat paradoxically, a proposal that
clearly and consciously states its limits is actually attractive because
it doesn’t leave open questions.

The <span class="caps">GOO</span> proposal seems to be the best example
of such self-limiting format. It extends the existing embedded bitmap
formats by adding just two or so new subformats, and that’s it. There
may be one or two open questions now (the scalability issue
I discussed), but once those are answered, and developers add support
for it, it’s a done deal. The <span class="caps">GOO</span> proposal
does not leave many loose ends.

In other words, the <span class="caps">GOO</span> proposal doesn’t try
to cook many dishes at the same time or doesn’t try to be a “catch all
solution”. Instead, it aims to do just one thing, and to do it very
well. Which is, I believe, where its real beauty lies. Also — just like
the older embedded bitmap formats — it can be used to host bitmap-only
glyph data, without any outline fallback. This actually is quite
desirable for some scenarios such as fixed-size devices — simple
electronic displays (brick phones, scrolling electronic banners, diplays
in car radios or other portable electronics).

In constrast, the <span class="caps">APP</span> proposal limits itself
very vaguely. The `sbix` table spec says that it can host a huge variety
of possible glyph formats, from <span class="caps">PNG</span> through
<span class="caps">TIFF</span> and <span class="caps">JPEG</span>,
<span class="caps">SVG</span> and <span class="caps">PDF</span> to even
movie clips. Attractive in principle, it also may be a bit “scary”. The
current <span class="caps">APP</span> implementation isn’t actually
`sbix`. It’s “`sbix` with <span class="caps">PNG</span> glyph data”. But
there could be “`sbix` with <span class="caps">SVG</span> data” or
“`sbix` with <span class="caps">MOV</span> clips”. This means that
develpers who choose to implement “sbix as a whole” may end up
struggling to support various glyph data sources, and they may never be
sure whether something new wouldn’t pop up in future.

The <span class="caps">MIC</span> proposal quite cleanly defines its
current scope, though Greg Hitchcock has suggested during the TypeCon
meeting that Microsoft may in future extend their format to support
“more things”, like gradients. However, knowing Microsoft’s practice,
they would most likely extend it in a transparent, backwards-compatible
way (so, for example, a gradient would fall back to a solid color). At
the current stage of the proposal, `CPAL` and `COLR` are nicely defined.
`CPAL` may undergo some revisions, especially if (hopefully) both the
`COLR` and the `SVG`  tables make use it, i.e. if Adobe, Microsoft and
Mozilla come to common terms regarding some minor `CPAL` extensions.

Interestingly, the <span class="caps">SVG</span> in `SFNT` proposal,
although very ambitious in terms of graphic effects you can achieve, is
actually fairly clearly limited. Again, some wrinkles need to be ironed
out, and animation is a big open question, but if we limit ourselves to
static SVGs, the principle is very simple: the
<span class="caps">SVG</span> in `SFNT` format only defines a container
format for the data, and clearly **delegates** everything else to the
<span class="caps">SVG</span> standard proper.

This is actually a fairly stable proposal. It means that, as a developer
who implements it, you’ll need to keep up with the evolution of
<span class="caps">SVG</span> proper, but — if you do have an
<span class="caps">SVG</span> renderer implementation — you’ll want to
do it anyway. But the <span class="caps">SVG</span> in `SFNT` makes
(more less) a promise that they won’t bother you greatly with doing big
changes in future that will be font-specific. So as long as you’ve
implemented the <span class="caps">SFNT</span> `SVG`  table once
(hopefully the revised one which shouls reuse `CPAL`), you’ll be done at
the font end. Then, you’ll just need to keep up with your general
<span class="caps">SVG</span> renderer as you normally would.

So with <span class="caps">SVG</span>, if your application does not have
an <span class="caps">SVG</span> renderer, it’s a “big step” that you’d
need to do, but you’d only need to do it once. (And perhaps it would be
a good idea to do it anyway, since <span class="caps">SVG</span> is
a graphics format that may be useful is supporting regardless of fonts).
But once you’ve done it, all future steps you’ll have to do will likely
be very small and will “just happen”.

In fact, I think the <span class="caps">GOO</span> mechanism would serve
as an ideal fallback to <span class="caps">SVG</span>. Since
<span class="caps">SVG</span> can contain scalable graphics which
intermix vectors and bitmaps, the results can be very complex. But they
could be pre-rendered and put into the `CBDT`/`CBLC` tables as well. It
could be similar to how pre-rendered <span class="caps">PNG</span>
bitmaps are (or used to be) often served by websites to older browsers
which don’t support <span class="caps">SVG</span>. You’d lose the smooth
scalability, but you would at least get the intended glyphs appearance.

## Support by FontLab apps

Fontlab Ltd. will soon be releasing a free app for Mac and Windows
called **FontLab Pad** which will allow users on both OSes to use fonts
that implement any of the above proposals (currently the
<span class="caps">APP</span> and <span class="caps">MIC</span> formats
are implemented but more support is being added as we speak). Also,
FontLab’s **TransType <span class="numbers">4</span>** allows simple
creation of MIC-compatible fonts through overlaying existing “layered
fonts” and assigning each layer a color. TransType can also output
APP-compatible fonts with the same contents. In combination with
FontLab’s **BitFonter <span class="numbers">3</span>**, TransType
<span class="numbers">4</span> can be used to produce sophisticated
full-bitmap color fonts in the APP-compatible format.

At FontLab, we are very happy with this development and support it
fully. Our upcoming font editors will support multicolor fonts natively,
with layers and potentially also complex fills, so fonts in all color
formats (including <span class="caps">SVG</span>) can be created.

<img
src="https://secure.gravatar.com/avatar/a19bf747f8460e6f957b712ff0d7ac8b?s=96&amp;d=blank&amp;r=g"
class="uk-comment-avatar avatar-96 photo"
srcset="https://secure.gravatar.com/avatar/a19bf747f8460e6f957b712ff0d7ac8b?s=192&amp;d=blank&amp;r=g 2x"
decoding="async" width="96" height="96" />

## Adam Twardoch

Adam Twardoch is Director of Products at FontLab, and a font consultant
specializing in font technology, multilingual typography, CSS webfonts,
Unicode and OpenType. Co-designer of Lato, the world’s most-popular
independently made font family (by Łukasz Dziedzic), and of Milka (by
Botio Nikoltchev). Co-creator of OpenType Font Variations and CSS Fonts
specs. In 2000–2014, technical and linguistic consultant at MyFonts, the
world’s largest online font distributor, and board member of Association
Typographique Internationale (ATypI). Adam regularly teaches workshops
in font creation. He lives and works in Warsaw and Berlin.
