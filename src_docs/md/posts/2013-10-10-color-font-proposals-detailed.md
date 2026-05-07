---
date:
  created: 2013-10-10
title: "The four color-font proposals: APP, COLR/CPAL, CBDT/CBLC, and SVG"
authors: [adam]
draft: false
---
Apple, Google, Microsoft, and Adobe/Mozilla each approached the color font problem
differently in 2013. This post examines the four proposals in technical detail — their
table structures, co-existence characteristics, fallback behavior, and open questions —
based on what was known at the time of the first implementations.

<!-- more -->

*This article is very technical.
No completeness or correctness of the information presented below, and all views are
personal.*

## Detailed discussion of approaches

### <span class="caps">GOO</span>: Google `CBDT`/`CBLC` tables

Bitmap-based (<span class="caps">PNG</span>) glyphs, either as per-PPM bitmap strike
definition, without any scaling, or as scalable bitmap glyphs with multiple “master
<span class="caps">PPM</span> sizes” — this is unclear (see below for details).

Announced in May <span class="numbers">2013</span> on the Google blog
\[<span class="caps">GOO<span class="numbers">1</span></span>\], this is an approach
which specifies two tables (`CBDT`/`CBLC`,
\[<span class="caps">GOO<span class="numbers">2</span></span>\]), which in turn extend
the existing OpenType `EBDT`/`EBLC` tables
\[<span class="caps">GOO<span class="numbers">3</span></span>\],
\[<span class="caps">GOO<span class="numbers">4</span></span>\] by adding the ability to
include uncompressed color images or <span class="caps">PNG</span> images.
Those, in turn, are extended version of Apple’s original `bdat`/`bloc` tables which have
a long history.

Google hosts a “Color Emoji” project dedicated to this
\[<span class="caps">GOO<span class="numbers">5</span></span>\], have created a Python
tool which embeds PNGs into that table
\[<span class="caps">GOO<span class="numbers">6</span></span>\] and have provided sample
fonts. FreeType <span class="numbers">2</span>.<span class="numbers">5</span> now also
includes support for this
\[<span class="caps">GOO<span class="numbers">7</span></span>\], added on May
<span class="numbers">29</span><sup>th</sup>.

*Co-existence:* The <span class="caps">GOO</span> proposal states: “It is recommended
that such fonts include no `glyf` table, and as such be bitmap-only fonts.
In the presence of color and non-color strikes in the same font, it is currently
unspecified which bitmap a conformant client will choose for rendering.”. While this
does not directly invalidate co-existence, it raises a valid question (for co-existence
in general, and for precedence in particular).
However, in Microsoft’s and Apple’s traditional implementations of the TrueType
rasterizer (before ClearType), the bdat/bloc and `EBDT`/`EBLC` tables worked so that if
a bitmap strike was available for a given <span class="caps">PPM</span>, it was used,
otherwise the outline glyph was rendered from the `glyf` table (even for the same glyph
but different <span class="caps">PPM</span>). I definitely think that all consuming
platforms which support the <span class="caps">GOO</span> approach should adopt the
aforementioned principle.
This is especially crucial when it comes to co-existence between the
<span class="caps">GOO</span> proposal and the <span class="caps">MIC</span> proposal.
If the <span class="caps">GOO</span> approach behaves as I described, then chances are
that one font could include the `CBDT`, `CBLC`, `COLR`, `CPAL` and glyf tables, and the
consuming platform could easily choose whether to use the <span class="caps">GOO</span>
approach first, and then (for different <span class="caps">PPM</span> sizes or glyphs
which are not supported by the <span class="caps">GOO</span> tables) use the
<span class="caps">MIC</span> approach (or just the plain `glyf` table).
*External modification:* While some people have generally voiced their desire to be able
to manipulate colors that are embedded inside of a font file externally, I think in case
of PNG-based glyphs, this should be, if at all, a post-processing step (after the glyph
images have been retrieved from the scaler).
*Fallback/degradation:* the <span class="caps">GOO</span> spec includes provisions as to
how the color bitmap data should be transformed into grayscale bitmap data.
*Unclear:* The OpenType spec also includes the `EBSC` table
\[<span class="caps">GOO<span class="numbers">8</span></span>\] which defines which
per-PPM strikes should be used for which <span class="caps">PPM</span> ranges when they
need to be scaled. Without `EBSC`, it is assumed that the `EBDT`/`EBLC` strikes are only
rendered for the specified <span class="caps">PPM</span>. The
<span class="caps">GOO</span> proposal makes no mention of how scaling should be
implemented, or whether a scaler should rely on the presence of the `EBSC` table.
I **strongly** think that, should the <span class="caps">GOO</span> proposal aim at
wider adoption, it should strictly follow the principle laid out in the OpenType spec:
if no `EBSC` table is present, strikes should be rendered only at given PPMs.
For scaling, it should refer to the `EBSC` table.
It’s also unclear to me what FreeType
<span class="numbers">2</span>.<span class="numbers">5</span> is doing at this point,
and whether support for `EBSC` is planned.

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

In the current implementation: bitmap-based (<span class="caps">PNG</span>) glyphs, as
scalable bitmap glyphs with multiple “master strikes” per <span class="caps">PPM</span>.
The `sbix` spec has provisions to hold other types of glyph definitions, such as
<span class="caps">TIFF</span>, <span class="caps">SVG</span>,
<span class="caps">PDF</span> or even movie clips, but this is not very clearly
specified nor implemented.

Apple’s is the first implementation that has been officially deployed.
It was introduced to iOS <span class="numbers">4</span> and also runs in CoreText
applications Mac <span class="caps">OS</span> X
<span class="numbers">10</span>.<span class="numbers">7</span> and newer.
It does not run on <span class="caps">ATSUI</span> applications such as Pages
<span class="numbers">09</span> or Keynote <span class="numbers">09</span>, but does
work in CoreText applications such as TextEdit or Safari.
Support for `sbix` table with <span class="caps">PNG</span> glyph has also been added to
FreeType.

The spec of the table has not been officially published by Apple, but has been shared
with interested developers.
The implementation hosts <span class="caps">PNG</span> data inside the `sbix` table,
with multiple <span class="caps">PPM</span> “master bitmaps” possible per glyph.
The scaler is responsible for choosing the most appropriate
<span class="caps">PPM</span> size and scale it to other <span class="caps">PPM</span>
sizes as needed.

It seems that per “master strike”, both the <span class="caps">PPM</span> and
<span class="caps">DPI</span> information can be provided.
For the metrics, the implementation relies on the bounding boxes stored in the `glyf`
table. It seems that, very unfortunately, the Apple implementation renders the contents
of a `glyf` table glyph, and the on top it renders its associated bitmap — so if bitmaps
are available in the `sbix` table for a particular glyph <span class="caps">ID</span>,
the corresponding `glyf` glyph <span class="caps">ID</span> slot has to be empty.

Mac <span class="caps">OS</span> X
<span class="numbers">10</span>.<span class="numbers">8</span> includes one font with
the `sbix` table: Apple Color Emoji, while iOS <span class="numbers">6</span> includes
the former along with Apple Color Emoji@<span class="numbers">2</span> (the latter
hosting the glyphs in double <span class="caps">DPI</span> resolution, it appears).

A reverse-engineered incomplete and faulty spec has been published
\[<span class="caps">APP<span class="numbers">1</span></span>\] and
\[<span class="caps">APP<span class="numbers">2</span></span>\], and a patch for
fontTools/<span class="caps">TTX</span> has been published
\[<span class="caps">APP<span class="numbers">3</span></span>\]. Those do not seem to
work correctly, though.
However, Fontlab Ltd.
has implemented its own `sbix` reading and writing, which seems to work correctly.
Fontlab Ltd.
also has its own `sbix` renderer, and I have successfully built Latin-script
color fonts with the `sbix` table and OpenType Layout features such as `calt`, and that
font works as expected in Mac <span class="caps">OS</span> X
<span class="numbers">10</span>.<span class="numbers">7</span> and
<span class="numbers">10</span>.<span class="numbers">8</span> (hooray!).

*Co-existence:* The fact that the `sbix` implementation in Apple OSes seems to require
that the `glyf` glyphs are blank raises a big co-existence concern.
In particular, it seems that this approach could not co-exist with the
<span class="caps">MIC</span> approach, which is a pity.
I see that as a weakness of the <span class="caps">APP</span> approach.
As for the co-existence of the <span class="caps">APP</span> and
<span class="caps">GOO</span> approaches, it seems somewhat unclear to me.
The <span class="caps">APP</span> approach requires both `sbix` and `glyf` to be
present, while currently, the <span class="caps">GOO</span> approach discourages the
presence of `glyf`. I see it as a weakness of both approaches (more strongly of the
<span class="caps">GOO</span> approach).
Also, there is the question of data duplication.
Theoretically, I imagine that a smart mechanism (akin to `TTC`) could allow for some
data sharing, wherein both the `sbix` table and the `CBLC` table referred to the same
<span class="caps">PNG</span> chunks.
But I’m not sure if offsets that go beyond defined table boundaries are permitted in the
<span class="caps">OT</span> spec (I don’t think they are).
*External modification:* While some people have generally voiced their desire to be able
to manipulate colors that are embedded inside of a font file externally, I think in case
of PNG-based glyphs, this should be, if at all, a post-processing step (after the glyph
images have been retrieved from the scaler).
*Fallback/degradation:* the <span class="caps">APP</span> implementation does not have
any clear provisions for fallback/degradation.
A renderer could fall back to grayscale or monochrome (dithered) versions of the `sbix`
<span class="caps">PNG</span> glyphs, but it would be desirable if it could also fall
back to “proper” `glyf` outline glyphs.
However, the fact that the <span class="caps">APP</span> implementation relies on
**empty** `glyf` glyphs invalidates that.
*Unclear:* It’s not currently clear how the
<span class="caps">PPM</span>+<span class="caps">DPI</span> “master strikes” should be
chosen and scaled, but my assumption is that the <span class="caps">APP</span> approach
explicitly assumes that the `sbix` glyphs are scalable, without the need for an
additional `EBSC` table.
This may be disputable.
Also, it’s not entirely clear to me how a renderer should make use of the
<span class="caps">PPM</span> and <span class="caps">DPI</span> information, though by
itself it seems rather straightforward.

- \[<span class="caps">APP<span class="numbers">1</span></span>\]
  [http://​typophile​.com/​n​o​d​e​/​<span class="numbers">9</span>​<span class="numbers">6</span>​<span class="numbers">6</span>​<span class="numbers">7</span>​<span class="numbers">1</span>​#​c​o​m​m​e​n​t​-​<span class="numbers">5</span>​<span class="numbers">2</span>​<span class="numbers">4</span>​<span class="numbers">375</span>](http://typophile.com/node/96671#comment-524375)
- \[<span class="caps">APP<span class="numbers">2</span></span>\]
  [http://​kanji​-database​.sourceforge​.net/​f​o​n​t​s​/​o​p​e​n​t​y​p​e​.​h​tml](http://kanji-database.sourceforge.net/fonts/opentype.html)
- \[<span class="caps">APP<span class="numbers">3</span></span>\]
  [https://​gist​.github​.com/​j​j​g​o​d/​<span class="numbers">5</span>​<span class="numbers">4</span>​<span class="numbers">7</span>​<span class="numbers">8</span>​<span class="numbers">229</span>](https://gist.github.com/jjgod/5478229)

### <span class="caps">MIC</span>: Microsoft `COLR`/`CPAL` tables

The newest member in the family of solutions, announced by Microsoft’s Michelle Perham
and Si Daniels on June <span class="numbers">26</span><sup>th</sup>
\[<span class="caps">MIC<span class="numbers">1</span></span>\], the Microsoft proposal
looks quite simple and clever to me, judging from the announcement.
It adds a relatively lightweight baggage of `COLR` and `CPAL` tables which results in
layered outline glyphs with one solid fill per layer.

The <span class="caps">MIC</span> approach is implemented in Windows
<span class="numbers">8</span>.<span class="numbers">1</span>, with a new Segoe
<span class="caps">UI</span> Emoji font being included in the
<span class="caps">OS</span>. A video from Microsoft’s Dan McLachlan talk where he
presents the approach is available
\[<span class="caps">MIC<span class="numbers">2</span></span>\] (about
<span class="numbers">9</span> minutes into the talk).
Also, Michelle Perham made a presentation at TypeCon <span class="numbers">2013</span>
dedicated to the topic.

The approach uses a base glyph (`glyf` or, presumably, also `CFF` ) which is used for
non-color situations.
The `COLR` table refers from this glyph into other outline glyphs (which exist within
the same table), which serve as layers.
Each “layer glyph” has its own z‑order and a single color references.
The color references are handled has palette indices, with a separate table, `CPAL` in
OpenType that resolves the <span class="caps">RGBA</span> colors actually used for the
glyph. Therefore, both the `COLR` and the `CPAL` tables should be quite small in size,
all the heavy-lifting being done by the traditional rendering methods.
It was announced that Microsoft plans to publish the specs for the tables within the
next few weeks.

*Co-existence:* If the <span class="caps">GOO</span> approach clarifies its behavior
when the `glyf` table is present, then the <span class="caps">MIC</span> approach could
co-exist easily with the <span class="caps">GOO</span> approach.
Actually, these two approaches could cleverly echo the former co-existence of `glyf`
with `bdat`/`bloc` (or `EBDT`/`EBLC`/`EBSC`). A consuming platform could go straight for
the monochrome `glyf` glyphs, or could prioritize the <span class="caps">MIC</span>
approach with a fallback to `glyf`, or could prioritize the
<span class="caps">GOO</span> approach with a fallback to `glyf`, or could prioritize
the <span class="caps">GOO</span> approach, then fall back to the
<span class="caps">MIC</span> approach, and then finally fall back to `glyf`. I don’t
see any principal conflict there.
*External modification:* As Michelle wrote on the OpenType list, “Fonts can have
multiple palettes, but right now the colors are defined by the font developer and the
user is not able to make changes to the palettes.
That’s definitely something we’d like to consider in the future and might be something
that applications could expose.”
At TypeCon, Greg Hitchcock clarified the envisioned roles of the palettes: first palette
is used by default for “dark on light” color situations while second palette is intended
for use in “light on dark” situations.
Additional palettes should be selectable by the user.
*Fallback/degradation:* This approach seems to be degrading nicely, and fallback
implications have been discussed above.

- \[<span class="caps">MIC<span class="numbers">1</span></span>\]
  [http://​typophile​.com/​n​o​d​e​/​<span class="numbers">1</span>​<span class="numbers">0</span>​<span class="numbers">4</span>​<span class="numbers">174</span>](http://typophile.com/node/104174)
- \[<span class="caps">MIC<span class="numbers">2</span></span>\]
  [http://​channel<span class="numbers">9</span>​.msdn​.com/​E​v​e​n​t​s​/​B​u​i​l​d​/​<span class="numbers">2</span>​<span class="numbers">0</span>​<span class="numbers">1</span>​<span class="numbers">3</span>/<span class="numbers">3</span> – <span class="numbers">191</span>](http://channel9.msdn.com/Events/Build/2013/3-191)

### <span class="caps">SVG</span>: Joint Adobe and Mozilla `SVG` table

The “full Monty” outline+bitmap (<span class="caps">SVG</span>) glyphs with possible
animation.

This is a proposal formulated by Mozilla’s Edwin Flores and Cameron McCormack, with
input from Robert O’Callahan and Adobe’s Sairus Patel, which has been submitted as <s>an
unofficial editor’s draft</s> a Final Community Group Specification to the
<span class="caps">W<span class="numbers">3</span>C</span>
\[<span class="caps">SVG<span class="numbers">1</span></span>\]. There is a reasonably
well-working <span class="caps">SVG</span> OpenType community for this
\[<span class="caps">SVG<span class="numbers">3</span></span>\] and a public mailing
list \[<span class="caps">SVG<span class="numbers">2</span></span>\]. As indicated on
Robert O’Callahan’s blog
\[<span class="caps">SVG<span class="numbers">4</span></span>\], this proposal has been
implemented in Firefox — it’s off by default but can be enabled by toggling
`gfx.font_rendering.opentype_svg.enabled` in about:config.
Also, a tool, written in Python, is available to create such fonts
\[<span class="caps">SVG<span class="numbers">5</span></span>\].

This is the by-far most complex proposal, as it puts the bar quite high for implementers
(it requires a full <span class="caps">SVG</span> renderer, and has provisions for
animated glyphs). On the other hand, its great advantage is that, once an app has access
to the <span class="caps">SVG</span> renderer, it can delegate the rendering of the
glyphs completely to the <span class="caps">SVG</span> library.
So the app only needs to call an OpenType Layout library to perform the layout, and then
call the <span class="caps">SVG</span> renderer for each glyph, and position the
rendered bitmaps. So in fact in an SVG-compatible environment using the
<span class="caps">SVG</span> table would be trivial.

The <span class="caps">SVG</span> proposal allows for designs that cannot be achieved by
the other solutions: it implements “rich color” (with gradients etc.), allows for
drawing various strokes and, of course, intermixing vectors and bitmaps.
So it’s potentially very very powerful.

Sairus Patel explained to me at TypeCon that he considers the current proposed spec as
“good to go”, and that’s the spec that is implemented in Firefox.

This approach really is an entirely different animal than all of the above.
I can easily imagine that the <span class="caps">APP</span>,
<span class="caps">GOO</span> and <span class="caps">MIC</span> approaches are all some
kind of “color fonts <span class="numbers">1</span>.<span class="numbers">0</span>”,
while the <span class="caps">SVG</span> proposal is “color fonts
<span class="numbers">2</span>.<span class="numbers">0</span>”. There’s is an ongoing
debate on the public mailing list of the
<span class="caps">W<span class="numbers">3</span>C</span> community, so I won’t get
into a detailed discussion here (also because I don’t quite understand some of the
complexities involved).
I definitely think, though, that this approach can co-exist with all the previous ones.
One potential co-existence benefit could be if the `SVG` table co-exists with the
<span class="caps">MIC</span> `CPAL` table.
The <span class="caps">SVG</span> glyphs could potentially make references to the color
palettes specified within `CPAL`, and if — in future — some means to externally
manipulate the `CPAL` palettes were implemented in consuming platforms, both the
<span class="caps">MIC</span> approach and the <span class="caps">SVG</span> approach
could benefit from that development.
In the light of the <span class="caps">MIC</span> proposal, Sairus Patel mentioned to me
that he might consider proposing some extensions to the Microsoft `CPAL` table, and then
would consider dropping the color palette format proposed in the
<span class="caps">SVG</span> spec — so that ultimately both the
<span class="caps">MIC</span> and the <span class="caps">SVG</span> formats could use
the `CPAL` table.

- \[<span class="caps">SVG<span class="numbers">1</span></span>\]
  [http://​www​.w<span class="numbers">3</span>​.org/​<span class="numbers">2</span>​<span class="numbers">0</span>​<span class="numbers">1</span>​<span class="numbers">3</span>​/​<span class="numbers">1</span>​<span class="numbers">0</span>​/​S​V​G​\_​i​n​\_​O​p​e​n​T​y​pe/](http://www.w3.org/2013/10/SVG_in_OpenType/)
- \[<span class="caps">SVG<span class="numbers">2</span></span>\]
  [http://​www​.w<span class="numbers">3</span>​.org/​c​o​m​m​u​n​i​t​y​/​s​v​g​o​p​e​n​t​y​pe/](http://www.w3.org/community/svgopentype/)
- \[<span class="caps">SVG<span class="numbers">3</span></span>\]
  [http://​lists​.w<span class="numbers">3</span>​.org/​A​r​c​h​i​v​e​s​/​P​u​b​l​i​c​/​p​u​b​l​i​c​-​s​v​g​o​p​e​n​t​y​pe/](http://lists.w3.org/Archives/Public/public-svgopentype/)
- \[<span class="caps">SVG<span class="numbers">4</span></span>\]
  [http://​robert​.ocallahan​.org/​<span class="numbers">2</span>​<span class="numbers">0</span>​<span class="numbers">1</span>​<span class="numbers">3</span>​/​<span class="numbers">0</span>​<span class="numbers">2</span>​/​s​v​g​-​i​n​-​o​p​e​n​t​y​p​e​-​n​e​w​-​a​p​p​r​o​a​c​h​-​t​o​-​s​v​g​.​h​tml](http://robert.ocallahan.org/2013/02/svg-in-opentype-new-approach-to-svg.html)
- \[<span class="caps">SVG<span class="numbers">5</span></span>\]
  [https://​github​.com/​e​d​f​<span class="numbers">8</span>​<span class="numbers">2</span>​<span class="numbers">5</span>​/​S​V​G​-​O​p​e​n​T​y​p​e​-​U​t​ils](https://github.com/edf825/SVG-OpenType-Utils)

## More on color fonts

- [Color fonts: the moment has arrived](2013-09-19-color-font-format-proposals.md)
- [Color font concepts: layers, palettes, scaling, and finiteness](2013-11-07-color-font-concepts.md)
