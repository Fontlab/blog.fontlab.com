Here are five draft blog posts in the requested style, each with YAML metadata, image references, and a reference URL list.

***

<!-- Post 1: variable fonts in ten languages (FontLab 8) -->

```markdown
---
this_file: src_docs/md/posts/2026-05-07-variable-fonts-in-many-languages.md
title: "variable fonts in many languages"
authors: [adam]
categories: [blog]
date:
  created: 2026-05-07
slug: variable-fonts-in-many-languages
---

Designers in Warsaw, Seoul, Barcelona and Tokyo are all asking the same quiet question: why am I still shipping twenty font files when one variable font would do?

![Variable font masters and instances in FontLab 8](../media/fl8-head-07-varcomponent.png)

## variable fonts are now the default question

In the last few years, tutorials and essays about variable fonts have appeared in Polish, Spanish, Chinese, Japanese and Korean, and they all converge on the same idea: one file, many styles, faster pages, better typography.[web:18][web:20][web:47][web:52][web:59][web:60]

Chinese and Japanese guides explain variation axes as levers for weight, width, slant and optical size, and emphasise that axes can be either continuous ranges or simple on–off switches.[web:52][web:58][web:59]

Polish and Spanish articles speak the language of practice: fewer HTTP requests, smoother responsive type scales, and the comfort of adjusting weight in fine steps instead of jumping between “Regular” and “Bold”.[web:17][web:18][web:29][web:30]

Korean authors go further, treating variable fonts as part of design systems, using Roboto Flex and other families to tune stroke width, counter size and contrast for specific screen densities and hierarchy levels.[web:48][web:51][web:57][web:60]

## what the multi‑lingual chorus is really saying

Across these languages, the benefits repeat: smaller payloads, continuous control, and better accessibility.[web:48][web:51][web:54][web:56]

Guides from MDN and Google’s codelabs spell out how a single `@font-face` declaration can expose the full variation range, with CSS properties like `font-weight`, `font-stretch` and `font-variation-settings` driving the axes.[web:15][web:52][web:58][web:59][web:61]

A Spanish variable-font primer on Runebook is blunt: if your OS and browser are even vaguely current, your bottleneck is no longer technology, it’s whether your typeface is ready.[web:18][web:24][web:27]

A Japanese overview notes that the real conceptual shift is treating weight, width and other traits as a continuous space instead of a handful of static instances, which matches how type designers already think about their design space.[web:50][web:56][web:59]

## where FontLab 8 fits in

FontLab 8 arrived in 2022, just as browser and OS support for variable fonts stopped being experimental and became the boring default.[web:59][web:61][web:43]

External reviews highlight its strength as a complete variable-font production environment on both macOS and Windows, filling the long‑standing gap for Windows‑based type designers who needed robust interpolation, OpenType features and export in one app.[web:37][web:40][web:43]

In practice, that means you can draw a Light and a Black, interpolate the in‑between masters, define `wght`, `wdth` and custom axes, and export one font file that speaks fluently to CSS on a Korean news site, a Japanese app UI and a Polish cultural portal.[web:34][web:40][web:56]

Typoteka’s history of variable fonts and screen typography reminds us that typographic innovation now happens on screens first, with families like Lato reaching readers worldwide through web embedding; FontLab 8 is one of the tools where those multi‑script, screen‑native families are actually built.[web:20][web:26][web:43]

## building for many scripts, exporting once

Multi‑script families from Polish foundries and international studios increasingly ship as variable fonts that support Latin, Cyrillic, Greek and often Arabic or Hebrew in a single file.[web:20][web:21][web:60]

Microsoft’s DirectWrite documentation treats OpenType variable fonts as a standard part of modern text rendering pipelines, not a special effect, which is exactly how these families are used in interface work.[web:24][web:52]

FontLab 8’s master‑matching and variation tools map neatly onto this reality: you can keep Latin and Cyrillic masters aligned, use variation axes consistently across scripts, and then export a single VF for a Figma component library in Tokyo, a React app in São Paulo and a WordPress theme in Berlin.[web:34][web:46][web:51]

For designers, the payoff is simple: all those multi‑lingual tutorials about variable typography stop being aspirational. They describe what you can ship today—if your drawing, spacing and interpolation live in a tool that understands variable fonts as well as the people writing about them do.[web:18][web:52][web:56]

## references

- https://runebook.dev/es/docs/css/css_fonts/variable_fonts_guide
- https://developer.mozilla.org/zh-CN/docs/Web/CSS/Guides/Fonts/Variable_fonts
- https://developer.mozilla.org/ja/docs/Web/CSS/Guides/Fonts/Variable_fonts
- https://grafmag.pl/artykuly/darmowe-zmienne-fonty-z-polskimi-znakami-czesc-61-edycja-variable-fonts
- https://typoteka.pl/en/period/variable-fonts-and-screen-typography
- https://yozm.wishket.com/magazine/detail/1239/
- https://codelabs.developers.google.com/migrating-variable-fonts
- https://theendearingdesigner.com/fontlab-8-review/
- https://learn.microsoft.com/es-mx/windows/win32/directwrite/opentype-variable-fonts
```

***

<!-- Post 2: OpenType features as invisible UX (FontLab 8 + TransType) -->

```markdown
---
this_file: src_docs/md/posts/2026-05-07-opentype-features-as-ux.md
title: "opentype features as invisible ux"
authors: [adam]
categories: [blog]
date:
  created: 2026-05-07
slug: opentype-features-as-ux
---

Most users never notice when your typography is wrong. They only notice when reading feels like work.

![OpenType features and metrics in FontLab 8](../media/fl8-head-06-metrics.png)

## features that quietly carry the text

OpenType features are often sold as tricks: swashes, discretionary ligatures, alternate numerals.[web:9][web:12]

The serious work happens elsewhere—kerning, standard ligatures, contextual alternates—features that Typekit’s practice guides call “font superpowers” because they turn a raw glyph set into a text system that behaves intelligently.[web:12][web:15]

Type Network’s deep‑dive on standard ligatures breaks them into categories: problem‑solvers that fix collisions like `fi`, aesthetic flourishes, and historical forms, all encoded in separate features (`liga`, `dlig`, `hlig`, `clig`, `rlig`) so applications can decide what belongs in body text.[web:9][web:12]

MDN’s overview from the browser side lines up with that view: kerning and default ligatures should be on by default, with other features exposed using CSS properties like `font-kerning`, `font-variant-ligatures` and low‑level `font-feature-settings` switches.[web:15][web:6]

## language, context, and the messy real world

In practice, things are not that tidy.

Ralf Herrmann’s notes on Firefox 3’s early OpenType support documented how turning on discretionary ligatures globally led to broken German words and Turkish confusion around dotted and dotless `i`, because the engine ignored language‑specific rules baked into the fonts.[web:6][web:3]

Discussion threads among type designers point out that the OpenType spec only *recommends* default behaviours; applications are free to ignore them, which they sometimes do.[web:3][web:6]

This is why font engineers obsess over language system tags, feature ordering, and test strings; the user shouldn’t have to know why “Auflauf” needs different ligature behaviour than “office”, only that it reads correctly.[web:3][web:9][web:12]

## how FontLab 8 helps you wire the UX

External reviewers often praise FontLab 8 for its robust OpenType support as much as for its drawing tools.[web:40][web:43]

You can write feature code for ligatures, alternates and mark positioning, test it live in multi‑script sample strings, and audit the results visually—crucial when scripts like Arabic or Devanagari rely heavily on contextual substitutions that must work across masters and variable axes.[web:43][web:34]

Its kerning and metrics editors let you treat spacing as part of the design, not an afterthought, matching what OpenType practice guides insist on: built‑in kerning should be your starting point, manual adjustments only a refinement.[web:12][web:15][web:40]

Right‑to‑left kerning enhancements and better auditing tools mean that when you export a variable font for use on the web, you’re not just shipping outlines and axes, you’re shipping a layout engine’s worth of typographic decisions in one file.[web:34][web:43]

## keeping features alive when you convert fonts

The messy reality of 2026 is that many studios still rely on older PostScript Type 1 fonts with hand‑tuned kerning and layout behaviour.[web:44][web:41]

Adobe’s retirement of Type 1 support in their apps forced teams to choose between abandoning those libraries or converting them cleanly to OpenType.[web:44]

Independent articles on CreativePro and elsewhere singled out TransType 4—first released in 2013 and still maintained—as a practical conversion tool that preserves families, style links and as much internal structure as possible while generating modern OpenType fonts.[web:44][web:41][web:32]

That combination matters: you draw and refine OpenType features in FontLab 8 for new work, but when a legacy font needs rescuing, TransType 4 converts it into an OpenType file that keeps kerning, naming and layout intact enough to live in the same projects without embarrassing seams.[web:32][web:38][web:44]

In both cases, what the reader sees is simple: text that looks like it belongs there. The secret is that most of the user experience lives inside four‑letter feature tags and kerning tables you edit on a Tuesday afternoon.

## references

- https://practice.typekit.com/lesson/caring-about-opentype-features/
- https://typenetwork.com/articles/opentype-at-work-standard-ligatures
- https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/OpenType_fonts
- https://opentype.info/blog/2008/06/14/kerning-and-opentype-features-in-firefox-3.html
- https://typedrawers.com/discussion/1182/opentype-registered-features
- https://creativepro.com/how-to-convert-postscript-fonts-to-opentype-with-transtype/
- https://www.youtube.com/watch?v=j06_QuBwy7Y
- https://www.fontlab.com/font-converter/transtype/
- https://theendearingdesigner.com/fontlab-8-review/
- https://www.toolfarm.com/buy/fontlab/
```

***

<!-- Post 3: halftone lines and Vexy Lines -->

```markdown
---
this_file: src_docs/md/posts/2026-05-07-vexy-lines-halftone-joy.md
title: "vexy lines and the joy of halftone"
authors: [adam]
categories: [blog]
date:
  created: 2026-05-07
slug: vexy-lines-halftone-joy
---

If you grew up staring at old maps, comics or 1980s movie posters, halftone is probably wired into your visual cortex already.

![Portrait rendered with halftone lines in Vexy Lines](../media/vexy-lines2-portrait.jpeg)

## how designers fake halftone the hard way

Vector tutorials have been explaining halftone tricks for years.

Illustrator guides show how to use the Blend tool to interpolate shapes or lines into smooth gradients, then expand everything into dense, editable vectors.[web:4][web:10]

Plug‑ins like Astute Graphics’ Phantasm add live halftone controls—dot size, angle, density—so you can preview shading changes instantly while still ending up with pure vector art at the end.[web:7][web:39]

YouTube is full of walkthroughs on building perfect halftone circles or horizontal line patterns in Illustrator and Photoshop, often involving multiple trips through filters, expansion, alignment and masking.[web:13][web:16]

The results can be beautiful, but each variant (lines, dots, waves) tends to require a different manual recipe, and iterating on a design means digging back through layers of destructive steps.

## vexy lines: one signal, many strokes

Vexy Lines, released in December 2025, takes a different approach: treat the bitmap image as a “signal” and let a stroke algorithm decide how to translate tone into vector geometry.[web:36][web:42]

You drop in a photo, drawing or AI image, add a Layer, and choose one or more Fills: straight or wavy lines, halftone dots, text fills, and other stroke‑based patterns.[web:36][web:33]

Its halftone fill engine uses tone to control dot or stroke size and density, with options for grid‑based or randomised placement, multiple dot shapes (including custom SVG imports), and live tweaking of pattern size, angle, contrast and even dot morphing between shapes.[web:33]

Because the output is vector, you can scale to poster size, recolour, or export to SVG and PDF for screenprint and risograph workflows without watching your file crumble.[web:42][web:33]

## when type designers start playing with halftone

For type designers, halftone tools are not just for posters.

Mapping a variable font specimen into Vexy Lines translates weight and contrast into stroke thickness and density, turning a static type sample into something closer to a print from a mid‑century engraving shop.[web:2][web:11][web:33]

You can feed in multi‑script text layouts exported from FontLab 8—Latin, Cyrillic, Greek, maybe even a sprinkle of Arabic—and have Vexy Lines render them in wave or halftone fills that stay vector‑sharp for large‑format prints or exhibition panels.[web:43][web:36]

The trick is that both tools think in continuous spaces: FontLab 8 lets you design interpolation across weight and width axes; Vexy Lines lets you interpolate stroke thickness and density based on tone. Together they make that 1980s “laser grid meets serif” poster in your head much easier to build.

## the practical bits

Vexy Lines runs on macOS and Windows, with a freemium model and a one‑time license for the full version, making it more of a studio tool than a subscription line item.[web:42]

Because it exports clean vector files, you can round‑trip artwork from Vexy Lines into FontLab Pad or other layout tools, overlaying halftone imagery with type set in your own fonts.[web:36][web:43]

And yes, if you’re chasing that very specific “screen‑printed band poster found under a refrigerator magnet” look, you can stack multiple halftone fills at different angles and dot sizes, just as the old tutorials recommend—only this time with live controls instead of blind trial and error.[web:4][web:7][web:33]

Vexy Lines doesn’t replace the satisfaction of drawing everything by hand. It just takes your pixels, turns them into strokes, and gives you back the feeling that halftone can be fun again.

## references

- https://www.vexy.art/lines/
- https://help.vexy.art/docs/halftone-fills
- https://alternativeto.net/software/vexy-lines/about/
- https://design.tutsplus.com/tutorials/using-the-blend-tool-to-create-a-halftone-effect-portrait-in-adobe-illustrator--vector-910
- https://astutegraphics.com/learn/10minskills/halftone-shading-a-quick-how-to
- https://www.trainingmagnetwork.com/lessons/list?lesson_type_id=26&no_header=true&page=1491&sort_by=title%2F1000
- https://www.reddit.com/r/graphic_design/comments/63g01w/how_do_you_replicate_this_halftone_lines_effect/
- https://www.youtube.com/watch?v=MWF2M2cOwKs
- https://www.youtube.com/watch?v=c4vfFxejvAM
```

***

<!-- Post 4: rescuing endangered fonts with TransType 4 -->

```markdown
---
this_file: src_docs/md/posts/2026-05-07-rescuing-type1-with-transtype.md
title: "rescuing endangered fonts with transtype 4"
authors: [adam]
categories: [blog]
date:
  created: 2026-05-07
slug: rescuing-type1-with-transtype
---

A surprising amount of contemporary design still depends on fonts that think the year is 1998.

![TransType 4 font family organization](../media/transtype-hero.png)

## when the software moves on and your fonts don’t

When Adobe announced that PostScript Type 1 fonts would no longer work in Creative Cloud apps, a lot of studios discovered that their “legacy” fonts were not museum pieces—they were inside active identities, book series and UI mockups.[web:44][web:41]

Articles aimed at production designers described the situation bluntly: unless you convert those Type 1 files to modern OpenType, you will either be re‑setting long documents or freezing your toolchain on old software.[web:44]

The legal questions are real (licenses vary), but the technical question is simple: how do you get from Type 1 to OpenType without breaking names, style links and carefully tuned kerning?[web:44][web:41]

## why TransType 4 keeps showing up in these conversations

Independent reviews and how‑to pieces tend to single out TransType 4, originally released in 2013, as a practical conversion tool for designers who are not font engineers.[web:44][web:35][web:38]

CreativePro’s walkthrough shows the basic flow: drag Type 1 fonts into TransType, organise families, map styles into sensible slots, tweak tracking or slant if needed, then export fresh OpenType PS or TT fonts with updated internals and consistent naming.[web:44]

Video intros emphasise the same points: drag‑and‑drop simplicity, a live glyph map, effects such as slant or smoothing if you need them, and the ability to keep family and style names stable so existing layouts don’t suddenly reflow.[web:38][web:41]

TransType’s own documentation stresses that it preserves as much of the original font data as possible while upgrading it to modern OpenType, optimising outlines and fixing common structural issues along the way.[web:32]

## how this pairs with FontLab 8

TransType is not a font editor; it’s a bridge.

The long‑term health of a typeface still depends on editing and maintaining it in a modern environment—precisely the niche that FontLab 8, released in 2022, is reviewed as filling for professional designers on both macOS and Windows.[web:40][web:43]

A typical workflow looks like this: use TransType 4 to convert a mission‑critical Type 1 family into clean OpenType, then bring those fonts into FontLab 8 if you need to extend character sets, add OpenType features or build variable versions.[web:32][web:34][web:40]

That combination lets studios rescue 1990s typefaces from obsolescence without abandoning the years of design and engineering locked in their outlines and kerning tables.

## type history is infrastructure

Typography histories like Typoteka’s overview of Polish screen type remind us that some of the most widely read fonts on the web started life long before anyone said “variable font” out loud.[web:20]

Tools like TransType 4 are not glamorous, but they quietly keep that history usable, turning endangered file formats into modern fonts that can live alongside new variable families drawn and exported from FontLab 8.[web:20][web:32][web:44]

If you squint a bit, it’s all one continuum: Pyrus and early FontLab on one end, variable fonts and screen typography on the other, and a little conversion utility in the middle making sure the bridge doesn’t collapse.

## references

- https://creativepro.com/how-to-convert-postscript-fonts-to-opentype-with-transtype/
- https://www.youtube.com/watch?v=j06_QuBwy7Y
- https://www.youtube.com/watch?v=_jwHfaUcEvE
- https://www.fontlab.com/font-converter/transtype/
- http://23.20.233.182/transtype-4-review
- https://typoteka.pl/en/period/variable-fonts-and-screen-typography
- https://theendearingdesigner.com/fontlab-8-review/
- https://www.toolfarm.com/buy/fontlab/
```

***

<!-- Post 5: variable fonts as motion and interface (FontLab 8 + Vexy Lines) -->

```markdown
---
this_file: src_docs/md/posts/2026-05-07-variable-fonts-motion-and-ui.md
title: "variable fonts in motion and interface"
authors: [adam]
categories: [blog]
date:
  created: 2026-05-07
slug: variable-fonts-motion-and-ui
---

Typography on screen used to mean “pick a weight and hope for the best.” Now the weight can follow the user.

![Variable font interpolation and export in FontLab 8](../media/fl8-head-11-multi-export.png)

## from static weights to animated axes

Web and motion tutorials increasingly treat variable fonts as a standard tool, not a novelty.

Webflow University, Dinamo’s guides and other educational resources walk through using CSS to animate weight and width on hover, scroll and viewport size changes, showing how a single VF file can replace multiple static fonts in interactive layouts.[web:2][web:5][web:11][web:52]

YouTube tutorials demonstrate animating variable fonts in After Effects, using text animators to drive axes like weight, width, slant or even custom bounce parameters, creating kinetic type where the motion lives inside the font itself.[web:8][web:14]

Google’s codelabs and MDN’s variable font guides fill in the engineering details: map axes to `font-weight` where possible for better browser support, fall back to `font-variation-settings` for custom axes, and keep your `@font-face` blocks honest about the ranges they expose.[web:15][web:52][web:58][web:61]

## designing for this in FontLab 8

All of that assumes you have a variable font worth animating.

FontLab 8’s multi‑master and variation tools are designed for exactly this: you open static fonts as masters, map them to axes, and preview interpolation with sliders or variation maps directly in the editor before you ever export a VF.[web:34][web:46]

Reviews point out that this is particularly important for UI and motion work where intermediate weights and widths are not theoretical—you will see them when a button animates or when responsive text reflows.[web:40][web:43]

You can define standard axes (`wght`, `wdth`, `slnt`) and custom ones, then export a single font that motion designers can wire up in After Effects and developers can control in CSS, without separate “Condensed”, “Bold” or “Wide” files scattered through a project.[web:34][web:52]

## “weird” axes and UI nuance

Articles in Japanese, Korean and Chinese make a point that some of the most interesting variable axes are not weight or width but things like contrast, corner roundness or serif size—parameters that directly affect legibility and brand voice.[web:50][web:56][web:60]

Korean design‑system writers describe using variable fonts to fine‑tune label weight and tracking for different screen densities, improving clarity without needing distinct font families.[web:51][web:57][web:54]

FontLab 8’s support for custom per‑glyph variation axes and variable components fits that direction: you can, for instance, create an axis that softens corners for small UI sizes and sharpens them for headlines, all exposed through one exported VF.[web:34][web:46][web:56]

## when type meets image‑based motion

On the image side, motion designers are increasingly mixing variable text with generative vector textures—exactly the territory where Vexy Lines lives.[web:36][web:42]

A typical workflow: set your titles in a variable font exported from FontLab 8, animate the axes in After Effects or CSS, and use Vexy Lines to turn background imagery into moving fields of lines or dots that share the same directionality and rhythm as the type.[web:8][web:11][web:33]

Because both type and image elements can stay vector until the final render, you preserve sharpness at any resolution and avoid the “crunchy at 4K” problem that haunted early kinetic typography experiments.[web:11][web:33][web:42]

The future that multi‑language tutorials describe—responsive typography, animated axes, fine‑tuned UI—is already here. Tools like FontLab 8 and Vexy Lines just make it a little less heroic to get there.

## references

- https://university.webflow.com/videos/variable-fonts
- https://www.vermeulen-design.com/blog/variable-fonts-tutorial
- https://abcdinamo.com/news/using-variable-fonts-on-the-web
- https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts
- https://developer.mozilla.org/zh-CN/docs/Web/CSS/Guides/Fonts/Variable_fonts
- https://www.youtube.com/watch?v=0fVymQ7SZw0
- https://www.youtube.com/watch?v=aWZUS59HVsQ
- https://codelabs.developers.google.com/migrating-variable-fonts
- https://syp.vn/jp/article/variable-font-basics
- https://figmapedia.com/entry/238fdea8-0034-80c0-b425-e507a666c3c8
- https://wdnote.tistory.com/197
- https://pixso.net/kr/articles/html-pixso-fonts-design/
- https://yozm.wishket.com/magazine/detail/1239/
- https://help.fontlab.com/fontlab/8/whats-new/whats-new-07-families-variation/
- https://help.fontlab.com/fontlab/8/whats-new/whats-new-since-fontlab-vi/
- https://www.vexy.art/lines/
- https://alternativeto.net/software/vexy-lines/about/
```

If you’d like, I can add a couple more posts focusing specifically on typeface design case studies (e.g. multi‑script families or experimental variable axes) and how they fit into FontLab / TransType / Vexy Lines workflows.