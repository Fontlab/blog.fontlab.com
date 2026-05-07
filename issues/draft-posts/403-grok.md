**Variable font axis design** is the process of defining the controllable dimensions of a typeface so a single file can smoothly interpolate between styles.

A **variation axis** expresses one aspect of the design (weight, width, slant, etc.). The font contains **masters** (extreme drawings) and the renderer blends them in real time.

### Standard (registered) axes

These five are supported everywhere variable fonts work:

- **wght** — Weight (1–1000)
  Thin (100) → Regular (400) → Bold (700) → Black (900)

- **wdth** — Width (50–200, as percentage of normal)
  Condensed (75) → Normal (100) → Expanded (125)

- **slnt** — Slant (−90° to +90°)
  Upright (0) → Italic-style slant (usually −10° to −20°)

- **opsz** — Optical size (typically 8–144 pt)
  Smaller values for text, larger for display (adjusts contrast, spacing, details)

- **ital** — Italic (0 = roman, 1 = italic)
  Often combined with slnt for true italics

You can also create **custom axes** (e.g., `CNTR` for contrast, `XOPQ` for x-height, or anything you invent) with your own four-character tag.

### How to design axes well

1. **Decide what actually needs to vary**
   Most typefaces only need 1–3 axes. Weight + width is the classic starting pair. Add slant or optical size only if they genuinely improve the design.

2. **Create masters at the extremes first**
   Draw the lightest + heaviest, narrowest + widest, etc.
   Keep every glyph’s **point count, direction, and order identical** across masters (this is called “compatible” or “isomorphic” outlines).

3. **Add intermediate masters only when needed**
   Linear interpolation works for most weight/width changes.
   Add a middle master if curves collapse, counters fill in, or serifs break at certain values.

4. **Map design space to user space**
   Internally the font uses “design coordinates” (your drawing numbers).
   You expose clean “user coordinates” (the numbers designers actually type: 100–900 for weight, 50–200 for width).




**Example diagram** (from FontLab documentation):
The blue line shows how user weight values (100–900) map to actual design-space positions. Notice the non-linear spacing — this prevents the “too light / too heavy” extremes from looking broken.

5. **Test interpolation constantly**
   Use a variation preview panel.
   Watch for:
   - Nodes crossing or disappearing
   - Counters filling at heavy weights
   - Diacritics drifting off anchors
   - Hinting or spacing problems that only appear at certain axis positions

6. **Respect readability at the edges**
   Very light weights (<300) can disappear on screen.
   Very heavy weights close counters — useful for display, dangerous for body text.
   Extreme widths often need optical adjustments (tighter spacing in condensed, looser in expanded).

### Practical workflow in FontLab 8

- Open **Font Info > Axes** and define each axis (tag, name, min/max/default).
- Draw or import your masters.
- Run **Match Masters** (or the new “Match Moves” in recent builds) to verify compatibility.
- Use the **Variation** panel or **Preview** window to slide axes live.
- Add **conditional glyph substitution** (rvrn feature) for glyphs that need different shapes at certain axis positions.
- Export as **Variable OpenType** (TT or CFF2). FontLab automatically builds the `fvar`, `gvar` (or `CFF2`), `STAT`, and `HVAR`/`MVAR` tables.

### Real-world tips from designers

- Start with weight + width. Most users only need these two.
- Use optical size (`opsz`) for text vs. display cuts — it automatically adjusts stroke contrast and spacing.
- For custom axes, keep the range small and meaningful (e.g., 0–100 for “grunge” or “contrast”).
- File size grows with every axis and every master. Two axes with three masters each is usually plenty.
- Test on actual devices and browsers — interpolation can look different on Windows ClearType vs. macOS vs. web.

Variable fonts turn a typeface into a **design system**. Done right, one file replaces an entire family while giving users (and CSS) precise control.

**Further reading & tools**

- [variablefonts.io](https://variablefonts.io) – interactive axis explorer
- [Axis Praxis](https://axis-praxis.org) – live testing of real variable fonts
- FontLab 8 “Families & Variation” chapter in the built-in help
- web.dev article on variable fonts (excellent CSS examples)

If you’re working on a specific typeface or axis idea (e.g., adding a contrast axis or designing for a particular script), share more details and I can give targeted advice on master placement, compatibility checks, or export settings.