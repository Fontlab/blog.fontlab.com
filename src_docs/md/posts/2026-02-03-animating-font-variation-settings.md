---
this_file: src_docs/md/posts/2026-02-03-animating-font-variation-settings.md
title: "Animating font-variation-settings: the performance problem nobody mentions"
authors: [fontlab]
tags: [variable-fonts, css, animation, web, performance]
date:
  created: 2026-02-03
slug: animating-font-variation-settings
---
![](../media/illu/animating-font-variation-settings-2.png){.illu-thumb}

Browser support for `font-variation-settings` has been broad since September 2018.
Animating the value works the way other CSS animation works.

What the tutorials skip is what happens to the GPU when you do it at scale.

<!-- more -->

The `font-variation-settings` CSS property is the low-level mechanism for controlling
the axes of variable fonts.
Its syntax lets you set the values of registered axes—like `"wght"` for weight, `"wdth"`
for width, or custom axes defined by the font—by specifying axis tags and numeric
values. By changing these settings, you can fine-tune the appearance of type, smoothly
morphing its shape and weight along the font’s design space, often beyond what
traditional static fonts allow.

To animate a variable font with CSS keyframes, you can use:

```css
@keyframes breathe {
  from { font-variation-settings: "wght" 200; }
  to   { font-variation-settings: "wght" 800; }
}
h1 { animation: breathe 4s ease-in-out infinite; }
```

That works. The problem is what “works” costs.
Every frame, the renderer has to interpolate glyph outlines between masters and
re-rasterise the result.
A single animated headline is fine.
Twenty animated headings on a long page — section titles, pull-quotes, a sticky nav —
and the laptop fan will tell you what you’ve done.

Mandy Michael’s recommendation, which has held up since she made it: wrap animated text
in an `IntersectionObserver` and pause the animation when the element scrolls off
screen.

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

This is the difference between a page that renders well and one that performs a
side-show no one asked for.

Two reference points worth keeping in mind.
Laurence Penney launched **Axis-Praxis** in late 2016, before the variable font
specification was even finished — the first public playground for exploring what the
axes could do.
Nick Sherman launched **v-fonts.com** at Robothon in March 2018, still the
best gallery for fonts worth animating.
Both predate the “variable fonts are mainstream” moment by years; both are still the
right places to start.

## References

- [Variable fonts on the web — web.dev](https://web.dev/articles/variable-fonts)
- [Getting started with variable fonts — variablefonts.dev](https://variablefonts.dev/getting-started)
- [Using variable fonts on the web — Dinamo](https://abcdinamo.com/news/using-variable-fonts-on-the-web)
- [v-fonts.com — variable font gallery](https://v-fonts.com)
- [Axis-Praxis — variable font playground](https://www.axis-praxis.org)

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-7-variable/){ .fl-help-cta }
