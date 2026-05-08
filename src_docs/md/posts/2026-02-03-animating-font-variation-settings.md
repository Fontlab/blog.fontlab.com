---
this_file: src_docs/md/posts/2026-02-03-animating-font-variation-settings.md
title: "Animating font-variation-settings: keeping motion buttery at scale"
authors: [fontlab]
tags: [variable-fonts, css, animation, web, performance]
date:
  created: 2026-02-03
slug: animating-font-variation-settings
---
![](../media/illu/animating-font-variation-settings-1.png){.illu-thumb .illu-index}

Browsers have shipped robust `font-variation-settings` support since 2018, and animating
those axes works the way the rest of CSS animation works.
That is a small miracle, and the people who built it deserve a round of applause.

<!-- more -->

`font-variation-settings` is the low-level handle on a variable font’s design space.
You name an axis tag — `"wght"`, `"wdth"`, an `"opsz"` for optical size, or any custom
axis the type designer defined — and you give it a value.
The renderer interpolates between masters in real time, so a single keyframe block can
take a headline from 200 to 800 weight without a flicker:

```css
@keyframes breathe {
  from { font-variation-settings: "wght" 200; }
  to   { font-variation-settings: "wght" 800; }
}
h1 { animation: breathe 4s ease-in-out infinite; }
```

The first time this works on a real page, it feels a little magical.
The browser is re-interpolating glyph outlines and re-rasterising them every frame, and
it does so fluidly because graphics teams at Apple, Google, Mozilla, and Microsoft put
years into making it fluid.

## A generous tip from the community

When you start animating *many* headings on the same page — section titles, pull-quotes,
a sticky nav, ten card heroes in a long scroll — every one of those animations keeps
running even when its element is off-screen.
That is normal CSS-animation behaviour, but it is also a great place to be a good
neighbour to your reader’s CPU.

Mandy Michael published a clean pattern for this back when variable fonts first hit the
web, and it still works beautifully today: pause animations on elements that are
scrolled out of view using `IntersectionObserver`.

```js
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    e.target.style.animationPlayState =
      e.isIntersecting ? "running" : "paused";
  });
});
document.querySelectorAll(".animated-heading")
  .forEach(el => observer.observe(el));
```

A handful of lines, and the whole page stays smooth.
It is a lovely bit of craft from a community that has been generous with its lessons
since variable fonts were brand new.

## Two playgrounds worth bookmarking

Two more places that opened the door before variable fonts were officially mainstream:

- **Axis-Praxis**, by Laurence Penney, launched in late 2016 — before the variable font
  specification was even finalised.
  It was the first public playground for exploring what the axes could do, and it is
  still one of the most enjoyable.
- **v-fonts.com**, by Nick Sherman, launched at Robothon in March 2018. It remains the
  best gallery for fonts worth animating today.

Both predate the moment “variable fonts” became a mainstream phrase, and both are still
the right place to start when you want inspiration.
Stand on those shoulders — they were put there for you.

## References

- [Variable fonts on the web — web.dev](https://web.dev/articles/variable-fonts)
- [Getting started with variable fonts — variablefonts.dev](https://variablefonts.dev/getting-started)
- [Using variable fonts on the web — Dinamo](https://abcdinamo.com/news/using-variable-fonts-on-the-web)
- [v-fonts.com — variable font gallery](https://v-fonts.com)
- [Axis-Praxis — variable font playground](https://www.axis-praxis.org)

[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/8-days/day-7-variable/){ .fl-help-cta }
