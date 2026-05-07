---
date:
  created: 2023-09-20
title: "FontLab 8.2: OpenType features, kerning, and variable fonts"
categories:
  - release
authors: [adam]
draft: false
---

FontLab 8.2 advances OpenType feature handling and kerning: right-to-left kerning for Arabic and Hebrew, the new Kern to Distance autokerning, better exception auditing, and improved kerning class management. Variable font support gains easier intermediate masters and extended conditional glyph substitution. Component and auto-layer workflows are also refined.

<!-- more -->

## Build and assemble.

Add accented glyphs with a double-click. Build glyphs from components or always-editable element references. Automate complex glyphs with *Auto layers*. Join design parts with *Skin* and *Glue*. Convert drawing parts to components in one click. Use *Fill* to sculpt whitespace off filled areas. Add ligatures, small caps, and old-style numerals with automatically generated OpenType features.

<figure class="aligncenter size-large">
<img
src="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-05-cornercomp-1024x256.png"
class="wp-image-3221" loading="lazy" decoding="async"
data-attachment-id="3221"
data-permalink="https://www.fontlab.com/hello/cpn1/attachment/fl8-head-05-cornercomp/"
data-orig-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-05-cornercomp.png"
data-orig-size="1920,480" data-comments-opened="0"
data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}"
data-image-title="fl8-head-05-cornercomp" data-image-description=""
data-image-caption=""
data-medium-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-05-cornercomp-300x75.png"
data-large-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-05-cornercomp-1024x256.png"
srcset="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-05-cornercomp-1024x256.png 1024w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-05-cornercomp-300x75.png 300w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-05-cornercomp-768x192.png 768w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-05-cornercomp-1536x384.png 1536w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-05-cornercomp.png 1920w"
sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024"
height="256" />
</figure>

<a
href="https://help.fontlab.com/fontlab/8/whats-new/whats-new-05-build-assemble/"
class="wp-block-button__link has-white-background-color has-text-color has-background wp-element-button"
style="border-radius:0px;color:#3296fa" target="_blank"
rel="noreferrer noopener">Read more: Build &amp; assemble ↗️</a>

**FontLab 8.2** adds one-click copying of auto layer recipes to other masters, improves the *Skin* filter, element switching, and automatic conversion of simple contours to composites.

## Space and kern.

Adjust metrics and kerning in a text-like editor, by planned phrases and pair lists. Apply tracking, modify widths, sidebearings, and kerning globally or for selected glyphs. Build kerning classes automatically or manually, and link metrics between glyphs using expressions. Auto-calculate metrics and kerning, and audit kerning exceptions to find combinations that create visual conflicts.

<figure class="aligncenter size-large">
<img
src="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-06-metrics-1024x256.png"
class="wp-image-3222" loading="lazy" decoding="async"
data-attachment-id="3222"
data-permalink="https://www.fontlab.com/hello/cpn1/attachment/fl8-head-06-metrics/"
data-orig-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-06-metrics.png"
data-orig-size="1920,480" data-comments-opened="0"
data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}"
data-image-title="fl8-head-06-metrics" data-image-description=""
data-image-caption=""
data-medium-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-06-metrics-300x75.png"
data-large-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-06-metrics-1024x256.png"
srcset="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-06-metrics-1024x256.png 1024w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-06-metrics-300x75.png 300w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-06-metrics-768x192.png 768w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-06-metrics-1536x384.png 1536w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-06-metrics.png 1920w"
sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024"
height="256" />
</figure>

<a
href="https://help.fontlab.com/fontlab/8/whats-new/whats-new-06-metrics-kerning/"
class="wp-block-button__link has-white-background-color has-text-color has-background wp-element-button"
style="border-radius:0px;color:#3296fa" target="_blank"
rel="noreferrer noopener">Read more: Metrics &amp; kerning ↗️</a>

**FontLab 8.2** brings major kerning improvements: right-to-left kerning for Arabic and Hebrew, new *Kern to Distance* autokerning, better exception handling and auditing, and improved kerning class management. The Metrics line-spacing workflow is improved, with new support for optical bounds for better text line edge alignment.

## Families and variation.

Build large font families and variable OpenType fonts. Interpolate and extrapolate fonts. Create intermediate weights and styles. Add conditional glyph substitutions. Work on multiple masters at once, and run automatic masters matching for point-compatible outlines. Preview interpolation live with sliders, a variation map, and play/pause buttons — inside FontLab, without external tools.

<figure class="aligncenter size-large">
<img
src="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-07-varcomponent-1024x256.png"
class="wp-image-3223" loading="lazy" decoding="async"
data-attachment-id="3223"
data-permalink="https://www.fontlab.com/hello/cpn1/attachment/fl8-head-07-varcomponent/"
data-orig-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-07-varcomponent.png"
data-orig-size="1920,480" data-comments-opened="0"
data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}"
data-image-title="fl8-head-07-varcomponent" data-image-description=""
data-image-caption=""
data-medium-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-07-varcomponent-300x75.png"
data-large-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-07-varcomponent-1024x256.png"
srcset="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-07-varcomponent-1024x256.png 1024w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-07-varcomponent-300x75.png 300w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-07-varcomponent-768x192.png 768w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-07-varcomponent-1536x384.png 1536w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-07-varcomponent.png 1920w"
sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024"
height="256" />
</figure>

<a
href="https://help.fontlab.com/fontlab/8/whats-new/whats-new-07-families-variation/"
class="wp-block-button__link has-white-background-color has-text-color has-background wp-element-button"
style="border-radius:0px;color:#3296fa" target="_blank"
rel="noreferrer noopener">Read more: Families &amp; variation ↗️</a>

**FontLab 8.2** makes adding simple variation easier and extends support for conditional glyph substitution to features other than `rvrn`.

## More on FontLab 8.2

- [Hello, FontLab 8.2!](2023-08-09-fontlab-8.md)
- [Drawing, stroke, and contour tools](2023-08-30-fontlab-82-drawing-tools.md)
- [Glyphs, font formats, scripting, and color](2023-10-11-fontlab-82-glyphs-formats-scripting-color.md)
