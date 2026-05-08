Browser support for `font-variation-settings` has been broad since September 2018. Animating the value works the way other CSS animation works. What the tutorials skip is what happens to the GPU when you do it at scale.

The syntax is straightforward:

```css
@keyframes breathe {
  from { font-variation-settings: "wght" 200; }
  to   { font-variation-settings: "wght" 800; }
}
h1 { animation: breathe 4s ease-in-out infinite; }
```

That works. The problem is what “works” costs. Every frame, the renderer has to interpolate glyph outlines between masters and re-rasterise the result. A single animated headline is fine. Twenty animated headings on a long page — section titles, pull-quotes, a sticky nav — and the laptop fan will tell you what you’ve done.

Mandy Michael’s recommendation, which has held up since she made it: wrap animated text in an `IntersectionObserver` and pause the animation when the element scrolls off screen.

```js
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    e.target.style.animationPlayState =
      e.isIntersecting ? 'running' : 'paused';
  });
});
document.querySelectorAll('.animated-heading')
  .forEach(el => observer.observe(el));
```

This is not clever. It is the difference between a page that renders well and one that performs a side-show no one asked for.

Two reference points worth keeping in mind. Laurence Penney launched **Axis-Praxis** in late 2016, before the variable font specification was even finished — the first public playground for exploring what the axes could do. Nick Sherman launched **v-fonts.com** at Robothon in March 2018, still the best gallery for fonts worth animating. Both predate the “variable fonts are mainstream” moment by years; both are still the right places to start.

The mistake people make is treating the weight slider as the thing to demonstrate. It is not. The interesting animation is the one you do not notice: `opsz` drifting as the viewport narrows, `wght` tightening at small sizes, `GRAD` nudging on dark mode. These are invisible by design. They make text more readable without announcing they are doing so.

Animation that reveals the system is worth doing. Animation that performs the system is a screensaver.

## References

- [Variable fonts on the web — web.dev](https://web.dev/articles/variable-fonts)
- [Getting started with variable fonts — variablefonts.dev](https://variablefonts.dev/getting-started)
- [Using variable fonts on the web — Dinamo](https://abcdinamo.com/news/using-variable-fonts-on-the-web)
- [v-fonts.com — variable font gallery](https://v-fonts.com)
- [Axis-Praxis — variable font playground](https://www.axis-praxis.org)

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-7-variable/)
