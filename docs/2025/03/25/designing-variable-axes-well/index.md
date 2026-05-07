Variable font axis design is the process of deciding which dimensions of a typeface should be controllable, then drawing the masters that make those dimensions behave.

Five axes are registered and supported everywhere variable fonts work: weight (`wght`, 1–1000), width (`wdth`, percentage of normal), slant (`slnt`, in degrees), optical size (`opsz`, in points), and italic (`ital`, 0 or 1). Custom axes — your own four-character tag, your own range — let you expose anything else: contrast, x-height, grade, the roundness of a corner.

Most typefaces only need one to three axes. Weight plus width is the classic starting pair. Add slant or optical size only when they genuinely improve the design. File size grows with every axis and every master, and so does the number of compatibility checks you have to keep in your head.

Draw the extremes first. Lightest and heaviest. Narrowest and widest. Keep every glyph’s point count, direction, and order identical across masters; FontLab calls this “compatible” or “isomorphic” outlines, and the variation engine cannot blend masters that disagree on the basics. Add intermediate masters only where linear interpolation breaks — counters filling at heavy weights, serifs collapsing in the condensed cut, joins thickening past the point of legibility.

In FontLab 8, the workflow is direct. Open Font Info, define each axis with tag, name, and range. Draw or import the masters. Run Match Moves to verify compatibility. Use the Variation panel to slide axes live and watch the in-between glyphs behave. Add conditional substitutions through the `rvrn` feature for glyphs that need a different shape past a certain axis position — a single-storey `g` past 850 weight, for instance.

Test at the edges. Very light weights vanish on screen. Very heavy weights close counters. Extreme widths usually need optical adjustments to stay legible. The variation engine does the maths; the designer is responsible for the taste.

A well-designed axis turns a typeface into a system. Done right, one file replaces an entire family while giving CSS — and human readers — precise control.

## References

- [variablefonts.io — interactive axis explorer](https://variablefonts.io)
- [Axis Praxis — live VF testing](https://axis-praxis.org)
- [OpenType Font Variations overview — Microsoft](https://learn.microsoft.com/en-us/typography/opentype/spec/otvaroverview)
- [Families and variation in FontLab 8](https://blog.fontlab.com/2025/03/25/designing-variable-axes-well/fontlab/8/manual/Variations/fontlab/8/whats-new/whats-new-07-families-variation/index.md)

[Read more on help.fontlab.com →](https://blog.fontlab.com/2025/03/25/designing-variable-axes-well/fontlab/8/manual/Variations/index.md){ .fl-help-cta }
