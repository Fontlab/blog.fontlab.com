# FontLab 8, seen from six languages

*What type designers say when they're not speaking English.*

---

The English-language conversation around font editors is well mapped. But FontLab has users in Tokyo, Seoul, Moscow, Berlin, São Paulo, and Warsaw — and what they say, in their own languages, draws a different picture than the one you get from Anglophone typography blogs.

## Japanese: a minority worth listening to

A Japanese designer writing under the name "hide" has published a multi-part FontLab 8 tutorial series on note.com. He opens with characteristic self-deprecation: this is software, he writes, that concerns only "twisted maniacs and professionals." In Japan, where Glyphs dominates professional type design, FontLab users are scarce. Japanese-language information is "almost nonexistent."

And yet he writes anyway, covering dark mode setup, variable font editing, and a complete walkthrough for making a handwriting-style font. The tutorials are detailed, opinionated, and funny in a way that professional software documentation rarely permits itself. His variable font tutorial walks through building a LINE Seed variable font — a real project, not a toy example.

The existence of these tutorials says something. Japanese type designers working on Latin and CJK projects are finding FontLab 8 worth documenting in a market where almost nobody else does.

## German: the toolbox vs. the wizard

On typografie.info, the leading German-language typography forum, a nuanced debate unfolded in early 2023. "FontLab is not obsolete," one contributor wrote. "It's a traditional program that grew over many years. The young developers behind Glyphs and RoboFont took new paths and made many things easier or different."

Another added: "FontLab 7/8 now has so much of what we wished Glyphs had in FontLab, and in my opinion much more besides. Yuri Yarmola really thought about how font design and technical production could be pleasant."

The verdict was not winner-take-all. "If I wanted to quickly realize a great font idea, I'd look at Glyphs. If I wanted to learn font production completely and potentially use all the possibilities, I'd go for FontLab."

## Chinese: "the ultra-bold font editor"

Chinese software review sites describe FontLab 8 with undisguised enthusiasm. CSDN, one of China's largest developer communities, published a review calling the interface "intuitive and easy to learn" and praising its stability "even when handling large font files." Bilibili hosts video introductions showing the software's capabilities for OpenType, variable, color, and web fonts.

On helloworld.net, a reviewer summarized: "Overall, FontLab 8 is a very practical font design software with an intuitive interface, rich font design tools, multi-format support, efficient font repair and optimization, and multilingual support."

## Russian: precision as craft

Yuri Gordon, a Russian type designer with a long-running LiveJournal, wrote about moving from Illustrator to FontLab. "FontLab is adapted for mouse work, and often for arrow keys on the keyboard. A letter isn't so much drawn as constructed and refined by adjusting points and handles." He describes FontLab's value proposition precisely: "The important quality of FontLab is the ability to optimize a curve with one command (Cmd+E) and place points at extrema. No less useful, though often criticized, is FontAudit."

On VK, a Russian social network, a user thanked someone for "the first Russian-language course on font development in FontLab — a big and detailed (if boring) course is always better than a short interface overview with memes."

## Korean: a book arrives

In April 2025, a Korean-language guide titled *FontLab Type Design* (폰트랩 타입 디자인) was published by Kwon Gun-oh. It teaches Hangul font creation using FontLab — a significant milestone for software that, like most font editors, evolved around Latin typography. The book covers FontLab's features alongside practical methods for making Korean fonts. That a publisher invested in this project suggests a growing user base in Korea, or at least enough curiosity to justify the risk.

## French and English: "the ultimate tool"

A French agency, EasyWeb, published a bilingual assessment that captures the consensus among professionals: "FontLab is not for the casual designer. The learning curve is steep, and its cost represents an investment. You really need specific and advanced typography needs to fully justify adopting it." But: "Clearly, among users, FontLab is seen as the ultimate tool for type design. Professionals in the field praise its unrivalled precision on Bézier curves and its advanced management of OpenType functionalities."

---

None of this settles the question of which font editor is "best." But the pattern across six languages is consistent: FontLab 8 is understood as the deep-end tool — harder to learn, more powerful once mastered, the choice of people who need to do things the easier tools can't.

---

## references

- [FontLab 8 解説その1 — note.com (Japanese)](https://note.com/up_hide/n/na220e87812b9)
- [FontLab 8：手書き風フォントの作り方 — note.com (Japanese)](https://note.com/up_hide/n/ne5c7438111a3)
- [FontLab 8 解説・LINE Seed Variable — note.com (Japanese)](https://note.com/up_hide/n/n0b3d2b3a10c0)
- [Beliebt: FontLab Diskussion — typografie.info (German)](https://www.typografie.info/3/leaderboard/)
- [FontLab 8 for Mac v8.4.1.8920 — blog.csdn.net (Chinese)](https://blog.csdn.net/m0_63787483/article/details/141424299)
- [FontLab 8，字体编辑设计制作工具 — helloworld.net (Chinese)](https://www.helloworld.net/p/4476282983)
- [FontLab字体设计软件V8.4.1版 — bilibili.com (Chinese)](https://www.bilibili.com/read/cv37147516/)
- [Ваком и шрифт — yurigordon.livejournal.com (Russian)](https://yurigordon.livejournal.com/109626.html)
- [За курс о разработке шрифта в Фонтлабе — vk.com (Russian)](https://vk.com/wall-122615_16173)
- [폰트랩 타입 디자인 — 교보문고 (Korean)](https://product.kyobobook.co.kr/detail/S000215038244)
- [Faut-il utiliser FontLab en 2025? — easyweb-agency.fr (French/English)](https://www.easyweb-agency.fr/en/should-fontlab-be-used-in-2025/)
- [FontLab — We See Giants (English)](https://weseegiants.com/resource/fontlab/)


# The converter that outlived the format

*Adobe killed Type 1 in 2023. TransType 4, released in 2013, turns out to have been the escape hatch.*

---

PostScript Type 1 fonts were born in 1985 and buried in January 2023, when Adobe yanked support from every Creative Cloud application. Microsoft followed in 2024, announcing deprecation in a future Windows update. The format had a 38-year run — longer than most marriages — and at its peak, every professional designer owned hundreds of Type 1 fonts. Some still do.

When Adobe pulled the plug, those designers had three choices: abandon the fonts, find OpenType replacements (expensive, often impossible), or convert them. Conversion fell to a tool that had been sitting quietly in FontLab's product line for a decade.

TransType 4 shipped in December 2013. It was a complete rewrite of a font converter that had existed since 1999. The timing was odd: by 2013, converting between Mac and Windows formats — the original problem TransType solved — was no longer a problem. What *was* a problem, and what the rewrite addressed, was the growing mess of formats proliferating around OpenType: web fonts, color fonts, variable fonts. And, buried in the feature list, the ability to convert "virtually any font format into other font formats."

That line turned out to matter more than anyone expected.

## What the professionals said

Mike Rankin at CreativePro wrote the definitive recommendation in 2021: "My favorite option is TransType by FontLab Ltd, Inc. The process of converting a Type 1 font with TransType could hardly be simpler. In fact, the main hurdle to updating your font library isn't technological, it's legal."

The legal hurdle he mentions is real. Many font licenses prohibit modification, and conversion technically counts. TransType displays any embedded license information and reminds users to check before converting — a small touch that reflects the company's deep familiarity with foundry concerns.

German typography site typografie.info reviewed TransType 4 when it shipped, noting its then-novel web font and color font support: "Neu hinzugekommen ist die Unterstützung für farbige Desktopschriften" — newly added support for colored desktop fonts, at a moment when Apple, Google, Microsoft, and Adobe each had incompatible color font proposals and TransType 4 was among the first tools to bridge them.

On TypeDrawers, Thomas Phinney — a font technologist who has worked at Adobe, FontLab, and Google — noted during beta testing: "I've been using TransType 4 in beta, and have been impressed so far. It is the first app coming from FontLab's new code base, code name 'Victoria.'"

## Eleven years in the field

Software released in 2013 is, by normal standards, ancient. TransType 4 still sells for $97 and still gets the job done. The interface hasn't been redesigned. The feature set hasn't expanded dramatically. But Type 1 fonts from 1988 still need converting, and TransType 4 still does it.

The German typografie.info review noted something else: TransType 4 handled *Stilverlinkung* — font family style linking — automatically. Drag fonts into a family, reorganize them, and the software fixes internal naming so they work across operating systems and applications. This kind of quiet, invisible correctness is harder to build than flashy features, and it ages better.

FontLab could have let TransType die quietly once the cross-platform format wars ended. That they rewrote it in 2013 instead, on a new codebase, suggests either prescience or stubbornness. Given what happened to Type 1, the distinction is academic.

For anyone still sitting on a folder of old PostScript fonts: the 7-day trial converts fonts in demo mode. The clock is not on your fonts. It's on the operating systems that still know what to do with them.

---

## references

- [How to Convert PostScript Fonts to OpenType with TransType — CreativePro](https://creativepro.com/how-to-convert-postscript-fonts-to-opentype/)
- [Font-Konverter TransType 4 erschienen — typografie.info (German)](https://www.typografie.info/3/artikel.htm/n/t/fontlab-transtype4)
- [FL TransType 4 discussion — TypeDrawers](https://typedrawers.com/discussion/459/fl-transtype-4)
- [PostScript Type 1 fonts end of support — Adobe](https://helpx.adobe.com/fonts/kb/postscript-type-1-fonts-end-of-support.html)
- [Microsoft will deprecate PostScript Type1 — windowsreport.com](https://windowsreport.com/microsoft-deprecate-postscript-type1-font/)
- [TransType 4 loses kerning when converting — FontLab Support](https://support.fontlab.com/hc/en-us/articles/115004333825)
- [Konvertierung Type 1 -> OpenType, die Zweite — typografie.info (German)](https://www.typografie.info/3/threads/konvertierung-type-1-opentype-die-zweite.24837/)


# Variable fonts were never about file size

*Nine years after OpenType 1.8, the most interesting variable fonts do things the specification never imagined.*

---

When variable fonts landed in 2016, the pitch was simple: merge an entire type family into one file. Smaller downloads, faster websites, better compression. The promise was practical — and almost entirely beside the point.

"Nine years after the introduction of variable fonts," designer Bernd Volmer told the 39C3 conference in Hamburg, "their most exciting uses have little to do with what variable fonts originally were intended for." That talk, *Variable Fonts — It Was Never About File Size*, traced a history of creative misuse that has become the format's real legacy.

## The conference identity that moved

In 2017, the TypoLabs conference commissioned a visual identity using a custom variable font. The font, later named Denman, animated between extremes of weight and width — making it, according to its designers, the first variable font used as the core of a visual identity. The project won a Red Dot Design Award and was never commercially released.

TypoLabs set the template. Variable fonts could be performances, not just files.

By 2025, the 39C3 (Chaos Communication Congress) identity used a custom variable font called Kario — duplexed so weight changes never reflow text, with optical-size adjustments and what the designer called "typographic Easter eggs." A conference identity that breathes.

## Pattern fonts: letters that tile

Marjoree, released in 2024, is a variable font family that includes pattern fonts — Marjoree Hex and Marjoree Penta — based on hexagonal and pentagonal tilings. The family was inspired by Marjorie Rice, an amateur mathematician who discovered new pentagonal tilings in the 1970s. A variable font axis lets you transition seamlessly between positive and inverted letterforms without changing text flow.

This is not what OpenType 1.8 was designed for. A variable axis controlling tessellation polarity? The specification authors did not anticipate this. But the format is flexible enough to absorb it.

## Font Spectrum: animation as a design principle

An Amsterdam-based foundry called Font Spectrum, run by Daniël Maarleveld and Edgar Walthert, treats animation not as a post-production effect but as a structural property of the typeface. Their typeface Silver Coil "can be looped into an infinite rotation." Purple Haze has "a readable regular weight and decorative extremes" that reveal themselves as the axis shifts. Electric Blue was "inspired by the neon glow of the 80s."

These are fonts built to be seen in motion. The variable font format is the animation engine; the font file is the animation.

## The wrong way, on purpose

"Early head-tracking experiments once tried to adjust a variable font's optical size based on reader position," Volmer's talk noted, "producing total chaos as text reshaped itself while being read." That chaos — connecting a font axis to live data, mouse movement, sound, network input — is where things get interesting.

The CCC talk included links to experiments at bronco.varfont.com, denman.varfont.com, and seraphs.varfont.com — variable fonts doing things their creators never intended. A font that responds to weather data. A font that animates with cursor position. A font that becomes unpredictable.

FontLab 8 supports variable font creation from start to finish: masters, intermediate instances, avar axis mapping, conditional glyph substitution. But the tool only provides the mechanism. What designers do with it — the misbehavior Volmer celebrates — is the point. The file size was never the story.

---

## references

- [Variable Fonts — It Was Never About File Size (39C3) — media.ccc.de](https://media.ccc.de/v/39c3-variable-fonts-it-was-never-about-file-size)
- [Font Spectrum is making futuristic typefaces that shift — It's Nice That](https://www.itsnicethat.com/articles/font-spectrum-graphic-design-discover-270325)
- [Font Spectrum создаёт футуристические шрифты — skillbox.ru (Russian)](https://skillbox.ru/media/design/font-spectrum-sozdayet-futuristicheskie-shrifty-kotorye-menyayut-formu/)
- [Purple Haze — Future Fonts](https://www.futurefonts.com/font-spectrum/purple-haze)
- [Silver Coil — Future Fonts](https://www.futurefonts.com/font-spectrum/silver-coil)
- [Show Me Fonts – TypoLabs](https://showmefonts.com/typolabs/)
- [Show Me Fonts – 39C3 Congress Design](https://showmefonts.com/39c3-congress-design/)
- [Marjoree — TDC](https://tdc.org/typeface/marjoree)
- [Marjoree: Klasse Schrift und tolle Muster — PAGE (German)](https://page-online.de/typografie/marjoree-font/)
- [Variable Color Fonts, how do they work? — Typearture](https://www.typearture.com/how-variable-color-fonts-work/)
- [CSS小技巧使用 font-variation 让文字起飞 — bbs.songma.com (Chinese)](https://bbs.songma.com/thread-112043-1-1.html)


# Nabla, COLRv1, and what happened to color fonts

*For a decade, color fonts were a format war. Then a strange isometric typeface from two Dutch designers showed everyone what the fuss was about.*

---

In 2013, four competing proposals — from Apple, Google, Microsoft, and Adobe/Mozilla — each tried to add color to OpenType in incompatible ways. FontLab covered all four, released FontLab Pad so people could actually *use* color fonts, and waited.

The format war sorted itself out. COLRv1 won: a vector format supporting gradients, compositing operations, and — crucially — variable color, where gradient stops can move along a variation axis. But a format needs a poster child, and in 2022, COLRv1 got one.

Nabla is an isometric color font designed by Arthur Reinders Folmer (Typearture) and Just van Rossum. It looks like something from a late-1990s video game rendered in vector: dimensional letterforms with highlights, shadows, and gradients that shift as you adjust two variation axes — Depth and Highlight. It shipped on Google Fonts under the SIL Open Font License, meaning anyone can use it, modify it, and build on it.

## What Nabla proved

Before Nabla, color fonts were emoji. The format existed to make smiley faces render in multiple colors on mobile phones. Nabla demonstrated that COLRv1 could carry expressive display typography — that a color font could be a design object in its own right, not just a container for pictograms.

The font includes multiple color palettes — what Google's documentation calls "skins" — selectable via CSS. On Chinese design platforms, Nabla was introduced as "a color variable font inspired by retro computer games, using the COLRv1 color font format that allows smooth gradients, sharp highlights, and blended shadows in font files." A Russian blog at skillbox.ru covered Nabla alongside Font Spectrum's animated variable fonts.

Just van Rossum reported on the state of COLRv1 in late 2025: "Nabla is currently supported in all browsers aside from Safari and any iOS browser. Nabla is also supported in Adobe Illustrator and Photoshop." The holdouts are shrinking.

## Color fonts in FontLab 8

FontLab 8 exports all four color OpenType formats: COLRv0, COLRv1, SVG, and sbix/CBDT. The Colors panel handles solid fills, linear gradients, radial gradients, and conical gradients with a visual editor that previews directly on the glyph canvas. Gradient stops, direction, and opacity are all adjustable by dragging — no numeric entry required unless you want it.

A dark-mode palette can be auto-generated for COLRv1 fonts, mapping light-background colors to dark-background equivalents. The mechanism is the same one that lets emoji adapt to system light/dark mode.

Color fonts are not a separate mode or plugin. They're part of the same workflow that produces monochrome OpenType: draw, color, export. The format is no longer the bottleneck. The bottleneck is designers realizing what the format can do.

## What's next

Nabla showed that COLRv1 can carry a sophisticated chromatic typographic design. Font Spectrum's animated variable fonts show that motion and color can combine. The technical infrastructure — format specification, browser support, font editor — is in place. What's missing, for now, is volume: enough designers making enough color fonts that the format becomes unremarkable.

That will probably take another five years. Type moves slowly. But the direction is clear.

---

## references

- [Nabla — Google Fonts](https://fonts.google.com/specimen/Nabla)
- [Typearture's Nabla: an Isometric COLRv1 font — Google Design](https://design.google/library/nabla-color-font/)
- [Nabla 彩色可变字体 — iconfont.cn (Chinese)](https://www.iconfont.cn/collections/detail?cid=51118)
- [Isometrischer Color-Font im COLRv1-Format — designerinaction.de (German)](https://www.designerinaction.de/typografie/isometrischer-color-font-im-colrv1-format-zum-downloaden/)
- [Variable Color Fonts, how do they work? — Typearture](https://www.typearture.com/how-variable-color-fonts-work/)
- [The state of COLRv1 — Just van Rossum on typo.social](https://typo.social/@justvanrossum/115700574164161538)
- [A font with built-in TeX syntax highlighting — planet.kde.org](https://planet.kde.org/steven-2025-12-27-a-font-with-built-in-tex-syntax-highlighting/)
- [Innovative OpenType Font Brings Built-In Syntax Highlighting — news.lavx.hu](https://news.lavx.hu/2025/12/27/innovative-opentype-font-brings-built-in-syntax-highlighting-to-tex-documents/)


# What type designers actually argue about

*A debate about non-destructive transformations reveals the fault lines in how type designers think about precision.*

---

Ray Larabie has designed more typefaces than most people have fonts installed. So when he posted on TypeDrawers in January 2025 about non-destructive transformations and floating-point coordinates, people paid attention.

He was not diplomatic: "I find them more frustrating than helpful. I constantly need to 'apply rounding' to eliminate floating-point coordinates. Every so often I'll struggle to align points vertically, only to realize there's an unapplied skew transformation."

The "elements" system in FontLab 8 — reusable, non-destructive glyph components — drew particular fire: "There has never been a case where I would intentionally use non-destructive transformation. And, for example, in FontLab 8, I can't just flatten the layer, or I'll lose something I require, like smart-corners."

The post exposed a tension that runs through type design tools. Do you want a system that preserves editability, letting you tweak transformations and update components globally? Or do you want absolute, direct control over every point and handle? These two goals pull in opposite directions.

## The response: trade-offs, not absolutes

Other designers pushed back — partly. "I use smart corners early in the process," one wrote, "and maybe by the time I'm done, I'll have decomposed some or all of them. It's not even because of floating point rounding, I just find it's not always ideal for the design." Another noted: "I will absolutely scale components like a bar imprecisely, and not care about it."

The consensus, if there was one, was that non-destructive features are useful scaffolding — the thing you build with, not the thing you ship. Smart corners for early-stage serif design, decomposed into plain outlines before export. Elements for roughing out a family, flattened once the design settles. The feature is a means, not an end.

## A separate fight: UI density

In a parallel thread that same month — titled "FontLab wants to know how is your workspace" — Nick Shinn posted a side-by-side comparison of FontLab Studio 5 and FontLab 8. "I much prefer v.5," he wrote. "Please make the present UI more 'Classic.'"

Ray Larabie agreed: "I recently did some experiments on video with FontLab 5 and 8. Aside from some jagginess from running FLS 5 for Windows on my Mac at non-retina, the FLS 5 interface still showed up much better on video."

Another designer blamed historical trends rather than FontLab specifically: "Ever since Windows Vista, UIs have started wasting white space. Dialog boxes are over twice as big, UI fonts are larger, none of it is user-configurable." The "inescapable hypermodernism" complaint.

## What these arguments tell you

Type designers argue about tools the way musicians argue about instruments. The arguments sound petty to outsiders — a few pixels of padding, the behavior of a single node when dragged — but they reflect real differences in how people work.

What's notable about the TypeDrawers threads is that nobody is arguing about whether FontLab 8 *works*. The complaints are about *how* it works — the choices it makes about workflow, interface, and precision. That's a mature-tool argument. You don't have nuanced debates about floating-point rounding in software that can't draw a proper Bézier curve.

FontLab 8 is not trying to be the simplest font editor. It's trying to be the one that gives you the most control. The arguments about non-destructive transformations and UI density are arguments about where control should live. Those arguments are a sign of health.

---

## references

- [Who likes non-destructive transformations, and floating-point coordinates? — TypeDrawers](https://typedrawers.com/discussion/6212/who-likes-non-destructive-transformations-and-floating-point-coordinates)
- [FontLab wants to know how is your workspace — TypeDrawers](https://typedrawers.com/discussion/6189/fontlab-wants-to-know-how-is-your-workspace)
- [FontLab Studio 5 screenshot comparison — TypeDrawers](https://typedrawers.com/discussion/comment/67622/#Comment_67622)


# Making Hangul in FontLab: a book, a script, a quiet milestone

*Most font editors evolved around the Latin alphabet. Korean designers have been adapting anyway. Now they have a guidebook.*

---

In April 2025, a book appeared on Korean bookstore shelves. Its title was plain: *폰트랩 타입 디자인* — FontLab Type Design. Its author, Kwon Gun-oh, had written a guide to making Hangul fonts using FontLab 8. The book covers FontLab's feature set alongside practical methods for Korean font creation. It is the first of its kind.

Hangul is not Latin. Where Latin fonts typically contain a few hundred glyphs, a working Hangul font needs 2,780 syllables — the KS X 1001 standard — assembled from 24 basic letters (jamo) combined into syllabic blocks. The combinatorial math is unforgiving, and font editors built for Latin often struggle with the structural requirements.

FontLab's component and element system helps. A Hangul syllable like 한 (han) is built from ᄒ (h), ᅡ (a), and ᄂ (n) — components that repeat across hundreds of syllables. Change the jamo design and every syllable updates. The same mechanism that builds accented Latin characters (a + acute → á) scales to the much larger problem of Korean syllabic assembly. But the workflow differs enough from Latin that dedicated documentation matters.

## What Korean designers say

The book's reception has been positive but realistic. One reviewer wrote: "I'm not planning to become a font maker. But I was surprised at how profound the world of fonts is. I want to buy a copy." Another noted FontLab's Latin-centric history: "FontLab is a program optimized for English. For Hangul, there may be problems."

That tension — powerful tool, Latin bias — is familiar to anyone designing non-Latin type in software born in the Latin alphabet world. But FontLab 8's support for Unicode, its glyph naming flexibility (including custom name lists for non-Latin scripts), and its Python scripting layer make it adaptable. A Korean YouTube channel shows a designer using FontLab 8 with the AI image generator Seedream to design 2,780 Hangul glyphs — a workflow that blends traditional type design with generative tools.

## Why this matters

Font editors live or die by their documentation ecosystems. A tool with excellent tutorials in your language is accessible. A tool without them is a locked door. The Korean book matters not because it reveals anything new about FontLab, but because it *unlocks* the tool for an entire community of designers who were previously dependent on English-language resources.

The broader pattern holds across scripts. FontLab 8 ships with template fonts (GetGo Fonts) covering Latin, Cyrillic, Greek, and Arabic. Ukrainian type designers at Lviv Polytechnic have published academic papers on using FontLab for Cyrillic font development. Vietnamese designers have written tutorials on variable master workflows in FontLab. Each script community builds its own bridge.

A book is a small thing. But a book in Korean about a font editor is evidence that Korean type designers are using the tool seriously enough to justify one. That's not nothing.

---

## references

- [폰트랩 타입 디자인 — 교보문고 (Korean)](https://product.kyobobook.co.kr/detail/S000215038244)
- [폰트랩 타입 디자인 — 알라딘 (Korean)](https://www.aladin.co.kr/shop/wproduct.aspx?ItemID=358159027)
- [Seedream으로 생성한 폰트랩 8로 한글 2780자 디자인 — YouTube (Korean)](https://www.youtube.com/watch?v=XyCx4KnQ8UA)
- [폰트제작 일지 E04 — greenegg.co.kr (Korean)](https://greenegg.co.kr/221836295407)
- [Systematic to Parametric: Extracting Variable Design Principles from Ukrainian Type Heritage — ATypI](https://atypi.org/program-2025/systematic-to-parametric-extracting-variable-design-principles-from-ukrainian-type-heritage-to-contemporary-fonts/)
- [Розроблення каліграфічного шрифту для української абетки — science.lpnu.ua (Ukrainian)](https://science.lpnu.ua/sites/default/files/attachments/2024/34808/importantdoc/zbirnyktez-1-94-1-6.pdf)
- [Biến thể Font chữ trong FontLab — nya.vn (Vietnamese)](https://nya.vn/bien-font-chu-trong-fontlab/)
- [GetGo Fonts for FontLab](https://fontlabcom.github.io/getgo-fonts/)


# Vexy Lines: signal processing in an artist's coat

*A desktop app that turns brightness into stroke weight, and photographs into engravings.*

---

Vexy Lines appeared in December 2025. It does one thing: converts raster images into vector art by varying line thickness according to pixel brightness. The mechanism is signal processing. The output looks like engraving, or halftone, or pen-and-ink. The interface hides the math.

You drop in a photo. The software measures luminance across every pixel and maps it to stroke weight — darker areas get thicker lines, lighter areas get thinner ones. Then it draws those lines as SVG vectors. The result is scalable to any size without pixelation, because the output is not a filtered image. It's a new drawing.

## The fill types

Six fill modes define the character of the output:

- **Linear** draws parallel lines whose weight tracks the source image's tonal values. Angle, spacing, and thickness range are all adjustable.
- **Wave** adds undulation to the parallel-line approach, producing a hand-engraved feel.
- **Halftone** deploys dots rather than lines, with configurable dot size, angle, and frequency. Classic printing technique, now in vector.
- **Stipple** places dots in a pattern that mimics the hedcut illustrations familiar from the *Wall Street Journal* — portraits built from thousands of individually placed dots.
- **Trace** follows edges in the source image rather than a fixed grid, producing contour-following strokes.
- **Text** fills areas with letterforms, using variable font weight to encode brightness. Darker regions get bolder letters; lighter regions get thinner ones.

Each fill type is a layer. You can stack multiple fills — a halftone base layer with a stipple detail layer on top, or a trace fill combined with linear shading — and control opacity, blending, and color sampling independently.

## Where the images come from

The software ships as a free browser version and paid macOS/Windows desktop applications. A Python package on PyPI, `vexy-lines-run`, provides a GUI wrapper around the Vexy Lines API, supporting batch image processing, video frame-by-frame style transfer, and `.lines` file interchange. The Python package runs on macOS, Windows, and Linux.

Output formats span SVG, PDF, EPS for vectors; PNG and JPG for raster at configurable resolutions. The vector exports make Vexy Lines suitable for large-format printing — murals, vinyl cutting, screen printing — where raster graphics would show their pixels.

## What connects this to FontLab

Vexy Lines is made by the same company. The connection is not superficial. Both tools convert one kind of visual information into another: FontLab converts drawings into font glyphs; Vexy Lines converts photographs into vector artwork. Both output formats that can be used in professional design workflows. Both automate the tedious part so humans can do the interesting part.

A Vexy Lines SVG can be pasted directly into a FontLab glyph cell. A photograph of calligraphy becomes vector line art, which becomes a font character. An image of a leaf becomes a halftone pattern, which becomes a decorative glyph. The tools are separate but the pipeline is real.

## What to use it for

Typical applications: poster art, album covers, tattoo design, hedcut portraits, textile patterns, screenprint separations, SVG animation source material, large-format prints, vinyl-cutting files. The text fill mode, using variable fonts to encode image brightness as typographic weight, is genuinely novel — a typographic halftone built from letterforms rather than dots.

The free browser version lets you evaluate the software. The desktop versions unlock full-resolution export and batch processing. More at [vexy.art](https://vexy.art/).

---

## references

- [Vexy Lines — vexy.art](https://vexy.art/)
- [Welcome to Vexy Lines Knowledge Base — help.vexy.art](https://help.vexy.art/)
- [Fills — help.vexy.art](https://help.vexy.art/fills/)
- [vexy-lines-run — PyPI](https://pypi.org/project/vexy-lines-run/)
- [Linear fill — help.vexy.art](https://help.vexy.art/fills/linear/)
- [Halftone fill — help.vexy.art](https://help.vexy.art/fills/halftone/)

![Vexy Lines application showing fill styles](../media/vexy-hello-hero.png)

![Vexy Lines — halftone effect](../media/vexy-lines2-halftone.jpg)

![Vexy Lines — linear engraving of a portrait](../media/vexy-lines2-hero.jpg)# FontLab 8, seen from six languages *What type designers say when they're not
speaking English.* \--- The English-language conversation around font editors
is well mapped. But FontLab has users in Tokyo, Seoul, Moscow, Berlin, São
Paulo, and Warsaw — and what they say, in their own languages, draws a
different picture than the one you get from Anglophone typography blogs. ##
Japanese: a minority worth listening to A Japanese designer writing under the
name "hide" has published a multi-part FontLab 8 tutorial series on note.com.
He opens with characteristic self-deprecation: this is software, he writes,
that concerns only "twisted maniacs and professionals." In Japan, where Glyphs
dominates professional type design, FontLab users are scarce. Japanese-
language information is "almost nonexistent." And yet he writes anyway,
covering dark mode setup, variable font editing, and a complete walkthrough
for making a handwriting-style font. The tutorials are detailed, opinionated,
and funny in a way that professional software documentation rarely permits
itself. His variable font tutorial walks through building a LINE Seed variable
font — a real project, not a toy example. The existence of these tutorials
says something. Japanese type designers working on Latin and CJK projects are
finding FontLab 8 worth documenting in a market where almost nobody else does.
## German: the toolbox vs. the wizard On typografie.info, the leading German-
language typography forum, a nuanced debate unfolded in early 2023. "FontLab
is not obsolete," one contributor wrote. "It's a traditional program that grew
over many years. The young developers behind Glyphs and RoboFont took new
paths and made many things easier or different." Another added: "FontLab 7/8
now has so much of what we wished Glyphs had in FontLab, and in my opinion
much more besides. Yuri Yarmola really thought about how font design and
technical production could be pleasant." The verdict was not winner-take-all.
"If I wanted to quickly realize a great font idea, I'd look at Glyphs. If I
wanted to learn font production completely and potentially use all the
possibilities, I'd go for FontLab." ## Chinese: "the ultra-bold font editor"
Chinese software review sites describe FontLab 8 with undisguised enthusiasm.
CSDN, one of China's largest developer communities, published a review calling
the interface "intuitive and easy to learn" and praising its stability "even
when handling large font files." Bilibili hosts video introductions showing
the software's capabilities for OpenType, variable, color, and web fonts. On
helloworld.net, a reviewer summarized: "Overall, FontLab 8 is a very practical
font design software with an intuitive interface, rich font design tools,
multi-format support, efficient font repair and optimization, and multilingual
support." ## Russian: precision as craft Yuri Gordon, a Russian type designer
with a long-running LiveJournal, wrote about moving from Illustrator to
FontLab. "FontLab is adapted for mouse work, and often for arrow keys on the
keyboard. A letter isn't so much drawn as constructed and refined by adjusting
points and handles." He describes FontLab's value proposition precisely: "The
important quality of FontLab is the ability to optimize a curve with one
command (Cmd+E) and place points at extrema. No less useful, though often
criticized, is FontAudit." On VK, a Russian social network, a user thanked
someone for "the first Russian-language course on font development in FontLab
— a big and detailed (if boring) course is always better than a short
interface overview with memes." ## Korean: a book arrives In April 2025, a
Korean-language guide titled *FontLab Type Design* (폰트랩 타입 디자인) was published
by Kwon Gun-oh. It teaches Hangul font creation using FontLab — a significant
milestone for software that, like most font editors, evolved around Latin
typography. The book covers FontLab's features alongside practical methods for
making Korean fonts. That a publisher invested in this project suggests a
growing user base in Korea, or at least enough curiosity to justify the risk.
## French and English: "the ultimate tool" A French agency, EasyWeb, published
a bilingual assessment that captures the consensus among professionals:
"FontLab is not for the casual designer. The learning curve is steep, and its
cost represents an investment. You really need specific and advanced
typography needs to fully justify adopting it." But: "Clearly, among users,
FontLab is seen as the ultimate tool for type design. Professionals in the
field praise its unrivalled precision on Bézier curves and its advanced
management of OpenType functionalities." \--- None of this settles the
question of which font editor is "best." But the pattern across six languages
is consistent: FontLab 8 is understood as the deep-end tool — harder to learn,
more powerful once mastered, the choice of people who need to do things the
easier tools can't. \--- ## references \- [FontLab 8 解説その1 — note.com
(Japanese)](https://note.com/up_hide/n/na220e87812b9) \- [FontLab
8：手書き風フォントの作り方 — note.com
(Japanese)](https://note.com/up_hide/n/ne5c7438111a3) \- [FontLab 8 解説・LINE
Seed Variable — note.com (Japanese)](https://note.com/up_hide/n/n0b3d2b3a10c0)
\- [Beliebt: FontLab Diskussion — typografie.info
(German)](https://www.typografie.info/3/leaderboard/) \- [FontLab 8 for Mac
v8.4.1.8920 — blog.csdn.net
(Chinese)](https://blog.csdn.net/m0_63787483/article/details/141424299) \-
[FontLab 8，字体编辑设计制作工具 — helloworld.net
(Chinese)](https://www.helloworld.net/p/4476282983) \- [FontLab字体设计软件V8.4.1版 —
bilibili.com (Chinese)](https://www.bilibili.com/read/cv37147516/) \- [Ваком и
шрифт — yurigordon.livejournal.com
(Russian)](https://yurigordon.livejournal.com/109626.html) \- [За курс о
разработке шрифта в Фонтлабе — vk.com
(Russian)](https://vk.com/wall-122615_16173) \- [폰트랩 타입 디자인 — 교보문고
(Korean)](https://product.kyobobook.co.kr/detail/S000215038244) \- [Faut-il
utiliser FontLab en 2025? — easyweb-agency.fr
(French/English)](https://www.easyweb-agency.fr/en/should-fontlab-be-used-
in-2025/) \- [FontLab — We See Giants
(English)](https://weseegiants.com/resource/fontlab/) # The converter that
outlived the format *Adobe killed Type 1 in 2023. TransType 4, released in
2013, turns out to have been the escape hatch.* \--- PostScript Type 1 fonts
were born in 1985 and buried in January 2023, when Adobe yanked support from
every Creative Cloud application. Microsoft followed in 2024, announcing
deprecation in a future Windows update. The format had a 38-year run — longer
than most marriages — and at its peak, every professional designer owned
hundreds of Type 1 fonts. Some still do. When Adobe pulled the plug, those
designers had three choices: abandon the fonts, find OpenType replacements
(expensive, often impossible), or convert them. Conversion fell to a tool that
had been sitting quietly in FontLab's product line for a decade. TransType 4
shipped in December 2013. It was a complete rewrite of a font converter that
had existed since 1999. The timing was odd: by 2013, converting between Mac
and Windows formats — the original problem TransType solved — was no longer a
problem. What *was* a problem, and what the rewrite addressed, was the growing
mess of formats proliferating around OpenType: web fonts, color fonts,
variable fonts. And, buried in the feature list, the ability to convert
"virtually any font format into other font formats." That line turned out to
matter more than anyone expected. ## What the professionals said Mike Rankin
at CreativePro wrote the definitive recommendation in 2021: "My favorite
option is TransType by FontLab Ltd, Inc. The process of converting a Type 1
font with TransType could hardly be simpler. In fact, the main hurdle to
updating your font library isn't technological, it's legal." The legal hurdle
he mentions is real. Many font licenses prohibit modification, and conversion
technically counts. TransType displays any embedded license information and
reminds users to check before converting — a small touch that reflects the
company's deep familiarity with foundry concerns. German typography site
typografie.info reviewed TransType 4 when it shipped, noting its then-novel
web font and color font support: "Neu hinzugekommen ist die Unterstützung für
farbige Desktopschriften" — newly added support for colored desktop fonts, at
a moment when Apple, Google, Microsoft, and Adobe each had incompatible color
font proposals and TransType 4 was among the first tools to bridge them. On
TypeDrawers, Thomas Phinney — a font technologist who has worked at Adobe,
FontLab, and Google — noted during beta testing: "I've been using TransType 4
in beta, and have been impressed so far. It is the first app coming from
FontLab's new code base, code name 'Victoria.'" ## Eleven years in the field
Software released in 2013 is, by normal standards, ancient. TransType 4 still
sells for $97 and still gets the job done. The interface hasn't been
redesigned. The feature set hasn't expanded dramatically. But Type 1 fonts
from 1988 still need converting, and TransType 4 still does it. The German
typografie.info review noted something else: TransType 4 handled
*Stilverlinkung* — font family style linking — automatically. Drag fonts into
a family, reorganize them, and the software fixes internal naming so they work
across operating systems and applications. This kind of quiet, invisible
correctness is harder to build than flashy features, and it ages better.
FontLab could have let TransType die quietly once the cross-platform format
wars ended. That they rewrote it in 2013 instead, on a new codebase, suggests
either prescience or stubbornness. Given what happened to Type 1, the
distinction is academic. For anyone still sitting on a folder of old
PostScript fonts: the 7-day trial converts fonts in demo mode. The clock is
not on your fonts. It's on the operating systems that still know what to do
with them. \--- ## references \- [How to Convert PostScript Fonts to OpenType
with TransType — CreativePro](https://creativepro.com/how-to-convert-
postscript-fonts-to-opentype/) \- [Font-Konverter TransType 4 erschienen —
typografie.info
(German)](https://www.typografie.info/3/artikel.htm/n/t/fontlab-transtype4) \-
[FL TransType 4 discussion —
TypeDrawers](https://typedrawers.com/discussion/459/fl-transtype-4) \-
[PostScript Type 1 fonts end of support —
Adobe](https://helpx.adobe.com/fonts/kb/postscript-type-1-fonts-end-of-
support.html) \- [Microsoft will deprecate PostScript Type1 —
windowsreport.com](https://windowsreport.com/microsoft-deprecate-postscript-
type1-font/) \- [TransType 4 loses kerning when converting — FontLab
Support](https://support.fontlab.com/hc/en-us/articles/115004333825) \-
[Konvertierung Type 1 -> OpenType, die Zweite — typografie.info
(German)](https://www.typografie.info/3/threads/konvertierung-type-1-opentype-
die-zweite.24837/) # Variable fonts were never about file size *Nine years
after OpenType 1.8, the most interesting variable fonts do things the
specification never imagined.* \--- When variable fonts landed in 2016, the
pitch was simple: merge an entire type family into one file. Smaller
downloads, faster websites, better compression. The promise was practical —
and almost entirely beside the point. "Nine years after the introduction of
variable fonts," designer Bernd Volmer told the 39C3 conference in Hamburg,
"their most exciting uses have little to do with what variable fonts
originally were intended for." That talk, *Variable Fonts — It Was Never About
File Size*, traced a history of creative misuse that has become the format's
real legacy. ## The conference identity that moved In 2017, the TypoLabs
conference commissioned a visual identity using a custom variable font. The
font, later named Denman, animated between extremes of weight and width —
making it, according to its designers, the first variable font used as the
core of a visual identity. The project won a Red Dot Design Award and was
never commercially released. TypoLabs set the template. Variable fonts could
be performances, not just files. By 2025, the 39C3 (Chaos Communication
Congress) identity used a custom variable font called Kario — duplexed so
weight changes never reflow text, with optical-size adjustments and what the
designer called "typographic Easter eggs." A conference identity that
breathes. ## Pattern fonts: letters that tile Marjoree, released in 2024, is a
variable font family that includes pattern fonts — Marjoree Hex and Marjoree
Penta — based on hexagonal and pentagonal tilings. The family was inspired by
Marjorie Rice, an amateur mathematician who discovered new pentagonal tilings
in the 1970s. A variable font axis lets you transition seamlessly between
positive and inverted letterforms without changing text flow. This is not what
OpenType 1.8 was designed for. A variable axis controlling tessellation
polarity? The specification authors did not anticipate this. But the format is
flexible enough to absorb it. ## Font Spectrum: animation as a design
principle An Amsterdam-based foundry called Font Spectrum, run by Daniël
Maarleveld and Edgar Walthert, treats animation not as a post-production
effect but as a structural property of the typeface. Their typeface Silver
Coil "can be looped into an infinite rotation." Purple Haze has "a readable
regular weight and decorative extremes" that reveal themselves as the axis
shifts. Electric Blue was "inspired by the neon glow of the 80s." These are
fonts built to be seen in motion. The variable font format is the animation
engine; the font file is the animation. ## The wrong way, on purpose "Early
head-tracking experiments once tried to adjust a variable font's optical size
based on reader position," Volmer's talk noted, "producing total chaos as text
reshaped itself while being read." That chaos — connecting a font axis to live
data, mouse movement, sound, network input — is where things get interesting.
The CCC talk included links to experiments at bronco.varfont.com,
denman.varfont.com, and seraphs.varfont.com — variable fonts doing things
their creators never intended. A font that responds to weather data. A font
that animates with cursor position. A font that becomes unpredictable. FontLab
8 supports variable font creation from start to finish: masters, intermediate
instances, avar axis mapping, conditional glyph substitution. But the tool
only provides the mechanism. What designers do with it — the misbehavior
Volmer celebrates — is the point. The file size was never the story. \--- ##
references \- [Variable Fonts — It Was Never About File Size (39C3) —
media.ccc.de](https://media.ccc.de/v/39c3-variable-fonts-it-was-never-about-
file-size) \- [Font Spectrum is making futuristic typefaces that shift — It's
Nice That](https://www.itsnicethat.com/articles/font-spectrum-graphic-design-
discover-270325) \- [Font Spectrum создаёт футуристические шрифты —
skillbox.ru (Russian)](https://skillbox.ru/media/design/font-spectrum-
sozdayet-futuristicheskie-shrifty-kotorye-menyayut-formu/) \- [Purple Haze —
Future Fonts](https://www.futurefonts.com/font-spectrum/purple-haze) \-
[Silver Coil — Future Fonts](https://www.futurefonts.com/font-spectrum/silver-
coil) \- [Show Me Fonts – TypoLabs](https://showmefonts.com/typolabs/) \-
[Show Me Fonts – 39C3 Congress Design](https://showmefonts.com/39c3-congress-
design/) \- [Marjoree — TDC](https://tdc.org/typeface/marjoree) \- [Marjoree:
Klasse Schrift und tolle Muster — PAGE (German)](https://page-
online.de/typografie/marjoree-font/) \- [Variable Color Fonts, how do they
work? — Typearture](https://www.typearture.com/how-variable-color-fonts-work/)
\- [CSS小技巧使用 font-variation 让文字起飞 — bbs.songma.com
(Chinese)](https://bbs.songma.com/thread-112043-1-1.html) # Nabla, COLRv1, and
what happened to color fonts *For a decade, color fonts were a format war.
Then a strange isometric typeface from two Dutch designers showed everyone
what the fuss was about.* \--- In 2013, four competing proposals — from Apple,
Google, Microsoft, and Adobe/Mozilla — each tried to add color to OpenType in
incompatible ways. FontLab covered all four, released FontLab Pad so people
could actually *use* color fonts, and waited. The format war sorted itself
out. COLRv1 won: a vector format supporting gradients, compositing operations,
and — crucially — variable color, where gradient stops can move along a
variation axis. But a format needs a poster child, and in 2022, COLRv1 got
one. Nabla is an isometric color font designed by Arthur Reinders Folmer
(Typearture) and Just van Rossum. It looks like something from a late-1990s
video game rendered in vector: dimensional letterforms with highlights,
shadows, and gradients that shift as you adjust two variation axes — Depth and
Highlight. It shipped on Google Fonts under the SIL Open Font License, meaning
anyone can use it, modify it, and build on it. ## What Nabla proved Before
Nabla, color fonts were emoji. The format existed to make smiley faces render
in multiple colors on mobile phones. Nabla demonstrated that COLRv1 could
carry expressive display typography — that a color font could be a design
object in its own right, not just a container for pictograms. The font
includes multiple color palettes — what Google's documentation calls "skins" —
selectable via CSS. On Chinese design platforms, Nabla was introduced as "a
color variable font inspired by retro computer games, using the COLRv1 color
font format that allows smooth gradients, sharp highlights, and blended
shadows in font files." A Russian blog at skillbox.ru covered Nabla alongside
Font Spectrum's animated variable fonts. Just van Rossum reported on the state
of COLRv1 in late 2025: "Nabla is currently supported in all browsers aside
from Safari and any iOS browser. Nabla is also supported in Adobe Illustrator
and Photoshop." The holdouts are shrinking. ## Color fonts in FontLab 8
FontLab 8 exports all four color OpenType formats: COLRv0, COLRv1, SVG, and
sbix/CBDT. The Colors panel handles solid fills, linear gradients, radial
gradients, and conical gradients with a visual editor that previews directly
on the glyph canvas. Gradient stops, direction, and opacity are all adjustable
by dragging — no numeric entry required unless you want it. A dark-mode
palette can be auto-generated for COLRv1 fonts, mapping light-background
colors to dark-background equivalents. The mechanism is the same one that lets
emoji adapt to system light/dark mode. Color fonts are not a separate mode or
plugin. They're part of the same workflow that produces monochrome OpenType:
draw, color, export. The format is no longer the bottleneck. The bottleneck is
designers realizing what the format can do. ## What's next Nabla showed that
COLRv1 can carry a sophisticated chromatic typographic design. Font Spectrum's
animated variable fonts show that motion and color can combine. The technical
infrastructure — format specification, browser support, font editor — is in
place. What's missing, for now, is volume: enough designers making enough
color fonts that the format becomes unremarkable. That will probably take
another five years. Type moves slowly. But the direction is clear. \--- ##
references \- [Nabla — Google Fonts](https://fonts.google.com/specimen/Nabla)
\- [Typearture's Nabla: an Isometric COLRv1 font — Google
Design](https://design.google/library/nabla-color-font/) \- [Nabla 彩色可变字体 —
iconfont.cn (Chinese)](https://www.iconfont.cn/collections/detail?cid=51118)
\- [Isometrischer Color-Font im COLRv1-Format — designerinaction.de
(German)](https://www.designerinaction.de/typografie/isometrischer-color-font-
im-colrv1-format-zum-downloaden/) \- [Variable Color Fonts, how do they work?
— Typearture](https://www.typearture.com/how-variable-color-fonts-work/) \-
[The state of COLRv1 — Just van Rossum on
typo.social](https://typo.social/@justvanrossum/115700574164161538) \- [A font
with built-in TeX syntax highlighting —
planet.kde.org](https://planet.kde.org/steven-2025-12-27-a-font-with-built-in-
tex-syntax-highlighting/) \- [Innovative OpenType Font Brings Built-In Syntax
Highlighting — news.lavx.hu](https://news.lavx.hu/2025/12/27/innovative-
opentype-font-brings-built-in-syntax-highlighting-to-tex-documents/) # What
type designers actually argue about *A debate about non-destructive
transformations reveals the fault lines in how type designers think about
precision.* \--- Ray Larabie has designed more typefaces than most people have
fonts installed. So when he posted on TypeDrawers in January 2025 about non-
destructive transformations and floating-point coordinates, people paid
attention. He was not diplomatic: "I find them more frustrating than helpful.
I constantly need to 'apply rounding' to eliminate floating-point coordinates.
Every so often I'll struggle to align points vertically, only to realize
there's an unapplied skew transformation." The "elements" system in FontLab 8
— reusable, non-destructive glyph components — drew particular fire: "There
has never been a case where I would intentionally use non-destructive
transformation. And, for example, in FontLab 8, I can't just flatten the
layer, or I'll lose something I require, like smart-corners." The post exposed
a tension that runs through type design tools. Do you want a system that
preserves editability, letting you tweak transformations and update components
globally? Or do you want absolute, direct control over every point and handle?
These two goals pull in opposite directions. ## The response: trade-offs, not
absolutes Other designers pushed back — partly. "I use smart corners early in
the process," one wrote, "and maybe by the time I'm done, I'll have decomposed
some or all of them. It's not even because of floating point rounding, I just
find it's not always ideal for the design." Another noted: "I will absolutely
scale components like a bar imprecisely, and not care about it." The
consensus, if there was one, was that non-destructive features are useful
scaffolding — the thing you build with, not the thing you ship. Smart corners
for early-stage serif design, decomposed into plain outlines before export.
Elements for roughing out a family, flattened once the design settles. The
feature is a means, not an end. ## A separate fight: UI density In a parallel
thread that same month — titled "FontLab wants to know how is your workspace"
— Nick Shinn posted a side-by-side comparison of FontLab Studio 5 and FontLab
8. "I much prefer v.5," he wrote. "Please make the present UI more 'Classic.'"
Ray Larabie agreed: "I recently did some experiments on video with FontLab 5
and 8. Aside from some jagginess from running FLS 5 for Windows on my Mac at
non-retina, the FLS 5 interface still showed up much better on video." Another
designer blamed historical trends rather than FontLab specifically: "Ever
since Windows Vista, UIs have started wasting white space. Dialog boxes are
over twice as big, UI fonts are larger, none of it is user-configurable." The
"inescapable hypermodernism" complaint. ## What these arguments tell you Type
designers argue about tools the way musicians argue about instruments. The
arguments sound petty to outsiders — a few pixels of padding, the behavior of
a single node when dragged — but they reflect real differences in how people
work. What's notable about the TypeDrawers threads is that nobody is arguing
about whether FontLab 8 *works*. The complaints are about *how* it works — the
choices it makes about workflow, interface, and precision. That's a mature-
tool argument. You don't have nuanced debates about floating-point rounding in
software that can't draw a proper Bézier curve. FontLab 8 is not trying to be
the simplest font editor. It's trying to be the one that gives you the most
control. The arguments about non-destructive transformations and UI density
are arguments about where control should live. Those arguments are a sign of
health. \--- ## references \- [Who likes non-destructive transformations, and
floating-point coordinates? —
TypeDrawers](https://typedrawers.com/discussion/6212/who-likes-non-
destructive-transformations-and-floating-point-coordinates) \- [FontLab wants
to know how is your workspace —
TypeDrawers](https://typedrawers.com/discussion/6189/fontlab-wants-to-know-
how-is-your-workspace) \- [FontLab Studio 5 screenshot comparison —
TypeDrawers](https://typedrawers.com/discussion/comment/67622/#Comment_67622)
# Making Hangul in FontLab: a book, a script, a quiet milestone *Most font
editors evolved around the Latin alphabet. Korean designers have been adapting
anyway. Now they have a guidebook.* \--- In April 2025, a book appeared on
Korean bookstore shelves. Its title was plain: *폰트랩 타입 디자인* — FontLab Type
Design. Its author, Kwon Gun-oh, had written a guide to making Hangul fonts
using FontLab 8. The book covers FontLab's feature set alongside practical
methods for Korean font creation. It is the first of its kind. Hangul is not
Latin. Where Latin fonts typically contain a few hundred glyphs, a working
Hangul font needs 2,780 syllables — the KS X 1001 standard — assembled from 24
basic letters (jamo) combined into syllabic blocks. The combinatorial math is
unforgiving, and font editors built for Latin often struggle with the
structural requirements. FontLab's component and element system helps. A
Hangul syllable like 한 (han) is built from ᄒ (h), ᅡ (a), and ᄂ (n) —
components that repeat across hundreds of syllables. Change the jamo design
and every syllable updates. The same mechanism that builds accented Latin
characters (a + acute → á) scales to the much larger problem of Korean
syllabic assembly. But the workflow differs enough from Latin that dedicated
documentation matters. ## What Korean designers say The book's reception has
been positive but realistic. One reviewer wrote: "I'm not planning to become a
font maker. But I was surprised at how profound the world of fonts is. I want
to buy a copy." Another noted FontLab's Latin-centric history: "FontLab is a
program optimized for English. For Hangul, there may be problems." That
tension — powerful tool, Latin bias — is familiar to anyone designing non-
Latin type in software born in the Latin alphabet world. But FontLab 8's
support for Unicode, its glyph naming flexibility (including custom name lists
for non-Latin scripts), and its Python scripting layer make it adaptable. A
Korean YouTube channel shows a designer using FontLab 8 with the AI image
generator Seedream to design 2,780 Hangul glyphs — a workflow that blends
traditional type design with generative tools. ## Why this matters Font
editors live or die by their documentation ecosystems. A tool with excellent
tutorials in your language is accessible. A tool without them is a locked
door. The Korean book matters not because it reveals anything new about
FontLab, but because it *unlocks* the tool for an entire community of
designers who were previously dependent on English-language resources. The
broader pattern holds across scripts. FontLab 8 ships with template fonts
(GetGo Fonts) covering Latin, Cyrillic, Greek, and Arabic. Ukrainian type
designers at Lviv Polytechnic have published academic papers on using FontLab
for Cyrillic font development. Vietnamese designers have written tutorials on
variable master workflows in FontLab. Each script community builds its own
bridge. A book is a small thing. But a book in Korean about a font editor is
evidence that Korean type designers are using the tool seriously enough to
justify one. That's not nothing. \--- ## references \- [폰트랩 타입 디자인 — 교보문고
(Korean)](https://product.kyobobook.co.kr/detail/S000215038244) \- [폰트랩 타입 디자인
— 알라딘 (Korean)](https://www.aladin.co.kr/shop/wproduct.aspx?ItemID=358159027)
\- [Seedream으로 생성한 폰트랩 8로 한글 2780자 디자인 — YouTube
(Korean)](https://www.youtube.com/watch?v=XyCx4KnQ8UA) \- [폰트제작 일지 E04 —
greenegg.co.kr (Korean)](https://greenegg.co.kr/221836295407) \- [Systematic
to Parametric: Extracting Variable Design Principles from Ukrainian Type
Heritage — ATypI](https://atypi.org/program-2025/systematic-to-parametric-
extracting-variable-design-principles-from-ukrainian-type-heritage-to-
contemporary-fonts/) \- [Розроблення каліграфічного шрифту для української
абетки — science.lpnu.ua
(Ukrainian)](https://science.lpnu.ua/sites/default/files/attachments/2024/34808/importantdoc/zbirnyktez-1-94-1-6.pdf)
\- [Biến thể Font chữ trong FontLab — nya.vn
(Vietnamese)](https://nya.vn/bien-font-chu-trong-fontlab/) \- [GetGo Fonts for
FontLab](https://fontlabcom.github.io/getgo-fonts/) # Vexy Lines: signal
processing in an artist's coat *A desktop app that turns brightness into
stroke weight, and photographs into engravings.* \--- Vexy Lines appeared in
December 2025. It does one thing: converts raster images into vector art by
varying line thickness according to pixel brightness. The mechanism is signal
processing. The output looks like engraving, or halftone, or pen-and-ink. The
interface hides the math. You drop in a photo. The software measures luminance
across every pixel and maps it to stroke weight — darker areas get thicker
lines, lighter areas get thinner ones. Then it draws those lines as SVG
vectors. The result is scalable to any size without pixelation, because the
output is not a filtered image. It's a new drawing. ## The fill types Six fill
modes define the character of the output: \- **Linear** draws parallel lines
whose weight tracks the source image's tonal values. Angle, spacing, and
thickness range are all adjustable. \- **Wave** adds undulation to the
parallel-line approach, producing a hand-engraved feel. \- **Halftone**
deploys dots rather than lines, with configurable dot size, angle, and
frequency. Classic printing technique, now in vector. \- **Stipple** places
dots in a pattern that mimics the hedcut illustrations familiar from the *Wall
Street Journal* — portraits built from thousands of individually placed dots.
\- **Trace** follows edges in the source image rather than a fixed grid,
producing contour-following strokes. \- **Text** fills areas with letterforms,
using variable font weight to encode brightness. Darker regions get bolder
letters; lighter regions get thinner ones. Each fill type is a layer. You can
stack multiple fills — a halftone base layer with a stipple detail layer on
top, or a trace fill combined with linear shading — and control opacity,
blending, and color sampling independently. ## Where the images come from The
software ships as a free browser version and paid macOS/Windows desktop
applications. A Python package on PyPI, `vexy-lines-run`, provides a GUI
wrapper around the Vexy Lines API, supporting batch image processing, video
frame-by-frame style transfer, and `.lines` file interchange. The Python
package runs on macOS, Windows, and Linux. Output formats span SVG, PDF, EPS
for vectors; PNG and JPG for raster at configurable resolutions. The vector
exports make Vexy Lines suitable for large-format printing — murals, vinyl
cutting, screen printing — where raster graphics would show their pixels. ##
What connects this to FontLab Vexy Lines is made by the same company. The
connection is not superficial. Both tools convert one kind of visual
information into another: FontLab converts drawings into font glyphs; Vexy
Lines converts photographs into vector artwork. Both output formats that can
be used in professional design workflows. Both automate the tedious part so
humans can do the interesting part. A Vexy Lines SVG can be pasted directly
into a FontLab glyph cell. A photograph of calligraphy becomes vector line
art, which becomes a font character. An image of a leaf becomes a halftone
pattern, which becomes a decorative glyph. The tools are separate but the
pipeline is real. ## What to use it for Typical applications: poster art,
album covers, tattoo design, hedcut portraits, textile patterns, screenprint
separations, SVG animation source material, large-format prints, vinyl-cutting
files. The text fill mode, using variable fonts to encode image brightness as
typographic weight, is genuinely novel — a typographic halftone built from
letterforms rather than dots. The free browser version lets you evaluate the
software. The desktop versions unlock full-resolution export and batch
processing. More at [vexy.art](https://vexy.art/). \--- ## references \- [Vexy
Lines — vexy.art](https://vexy.art/) \- [Welcome to Vexy Lines Knowledge Base
— help.vexy.art](https://help.vexy.art/) \- [Fills —
help.vexy.art](https://help.vexy.art/fills/) \- [vexy-lines-run —
PyPI](https://pypi.org/project/vexy-lines-run/) \- [Linear fill —
help.vexy.art](https://help.vexy.art/fills/linear/) \- [Halftone fill —
help.vexy.art](https://help.vexy.art/fills/halftone/) ![Vexy Lines application
showing fill styles](../media/vexy-hello-hero.png) ![Vexy Lines — halftone
effect](../media/vexy-lines2-halftone.jpg) ![Vexy Lines — linear engraving of
a portrait](../media/vexy-lines2-hero.jpg)
