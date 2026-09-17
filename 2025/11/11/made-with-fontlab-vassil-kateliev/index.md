[Science Gothic](https://github.com/tphinney/science-gothic) is a four-axis variable font drawn by Thomas Phinney, Brandon Buerkle, and Vassil Kateliev. The fact that it exists at all — full Latin coverage, four axes, a real production pipeline — is partly because Kateliev wrote the toolkit that did the heavy lifting.

Kateliev runs [Karandash type foundry](http://karandash.eu/) and [The FontMaker](http://thefontmaker.com/), and he’s the developer behind [TypeRig](https://kateliev.github.io/TypeRig/) — the Python library and toolkit that lets type designers script FontLab to do things the GUI doesn’t expose, or doesn’t expose fast enough. TypeRig is a quiet load-bearing piece of the modern FontLab ecosystem; Robert Strauch and Alexander Haberer separately credit “the integration of Vassil Kateliev’s fabulous TypeRig libraries” as the thing that lets them write studio tools for batch-processing and diagnostics.

Kateliev’s testimonial is long and worth reading whole. The relevant part:

> The definitive FontLab version to have: blazingly fast, cutting-edge technology, and with superbly rich functionality that touches almost every possible aspect of type design. (…) A keen tool worthy of a master!
>
> What’s not to love? The best vector engine for drawing and manipulation I have seen in ages. Rock-steady interpolation engine that is also compliant with variable OpenType fonts. Start with an excellent multi-paradigm approach to type design — old-school outlines, element references, components, auto-generated glyphs, or all of them combined. Sprinkle on top a handful of nifty tricks to speed up your work like auto layers or auto OpenType feature generation. Combine that with a super powerful Python-based API (that I actually use a lot). Let’s not forget multi-platform: a fact that I consider very important.
>
> The new FontLab is an endless ocean of opportunities — you get an app for every taste and workflow.

— Vassil Kateliev, [Karandash type foundry](http://karandash.eu/), [The FontMaker](http://thefontmaker.com/), developer of [TypeRig](https://kateliev.github.io/TypeRig/)

The phrase that matters here is “Python-based API (that I actually use a lot).” Kateliev does not say it’s a nice-to-have. He says he uses it a lot, and the proof is TypeRig — a library of his own that turns FontLab into the back end of a custom workflow he and his clients depend on. That’s the point of an extensible editor. The vendor ships the application; serious users ship plugins on top of it that the vendor never had to write.

Science Gothic is the visible artefact. Behind it sits the less-visible argument: that the editor’s interpolation engine has to be rock-steady, that the variable-OpenType compliance has to be handled correctly without manual TTX surgery, and that the multi-paradigm approach (outlines, references, components, generated glyphs) has to coexist without forcing the designer into one religion. Four axes across thousands of glyphs is the test that breaks lesser pipelines. This one shipped.

The “endless ocean of opportunities” line is salesman language only if you don’t know Kateliev. Coming from someone who has written a parallel toolkit on top of the editor’s API, it is closer to a status report.

## More from Vassil Kateliev

- [Science Gothic](https://github.com/tphinney/science-gothic) — with Thomas Phinney and Brandon Buerkle

[Browse Karandash →](http://karandash.eu/)
