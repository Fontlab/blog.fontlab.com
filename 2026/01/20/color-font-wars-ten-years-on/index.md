In 2013, four companies each decided the same thing: OpenType needed color. They each decided it differently.

Apple shipped `sbix` — PNG bitmaps locked to a pixel size, the format behind the original iPhone emoji. Google shipped `CBDT/CBLC` — also bitmaps, also PNG, but with size-table machinery borrowed from the old monochrome strike system. Microsoft and Adobe went vector, in opposite directions: Microsoft proposed `COLR`, a palette of layered outlines; Adobe and Mozilla proposed `SVG-in-OpenType`, full SVG documents embedded inside the font.

That last pairing felt like it had the momentum. Photoshop CC 2017 shipped the first commercial OT-SVG release, Trajan Color Concept. Type With Pride’s Gilbert typeface, the rainbow tribute to Gilbert Baker, launched in April 2017 and put OT-SVG on the front page of every design magazine. SVG was richer, more expressive, more obviously “the right answer.” For a while in the late 2010s, `COLR`’s spare palette-and-layers architecture looked like the budget option.

Then the numbers arrived.

COLRv1 — the joint Google and Microsoft revision, shipping in OpenType 1.9 in 2021 — added the pieces that had made `COLR` feel limited: gradients, blend modes, transforms, a full paint-tree model. Chrome 98 shipped it in February 2022, driven by Dominik Röttsches. Edge followed via Chromium. Firefox 107 in November 2022. And the file size argument was decisive: the full Noto Emoji set as `CBDT` weighs 9 MB. The same set as COLRv1 with WOFF2 compression weighs 1.85 MB. That is roughly a fivefold reduction — the kind of number that ends arguments.

Roel Nieskens, who had been among OT-SVG’s advocates, put it plainly:

> “I used to say the OpenType-SVG format was the best… until I realized this is just too complex for a low-level job like text rendering. … So I switched sides to COLR.”

The thing the “COLRv1 won” headline got wrong is that OT-SVG didn’t lose. It just lost *that fight*. Safari still renders it. Adobe Photoshop, Illustrator, and InDesign still author with it. The split as of late 2026 is COLRv1 across Chromium and Firefox, OT-SVG across Safari and Adobe’s apps. One-format-fits-all remains aspirational.

For anyone designing a color font today, the practical conclusion is unglamorous: know your target. A web display face bound for Chromium browsers should start with COLRv1 and a monochrome fallback. If the same face needs to work in Adobe apps or on Safari, the SVG table still earns its place. The four-format argument from 2013 did not resolve into a winner. It resolved into a division of labour.

## References

- [Chrome COLRv1 blog post — developer.chrome.com](https://developer.chrome.com/blog/colrv1-fonts)
- [COLRv1 and CSS font-palette — CSS-Tricks](https://css-tricks.com/colrv1-and-css-font-palette-web-typography/)
- [SVG OpenType genesis — Typekit blog (2013)](https://blog.typekit.com/2013/10/08/svg-opentype-genesis/)
- [OpenType COLR table — Microsoft](https://learn.microsoft.com/en-us/typography/opentype/spec/colr)
- [Type With Pride — Gilbert Color font](https://www.typewithpride.com/)

[Read more →](https://www.fontlab.com/font-editor/fontlab/)
