---
date:
  created: 2023-10-11
title: "FontLab 8.2: glyphs, font formats, scripting, and color"
categories:
  - release
authors: [adam]
draft: false
---

FontLab 8.2 rounds out the release with improvements across the Font window, format interop, Python scripting, and color fonts. Highlights include COLRv1 support, temporary font installation on export, improved Glyphs file format support, Python 3.11.3 for 10–60% faster scripting, and case conversion in the Font window.

<!-- more -->

## Test and adjust.

FontLab helps you iterate toward the ideal and test in real-world environments. Find and fix problems automatically, optimize contours, tweak tension and curvature, merge paths, and apply non-destructive tweaks like rounded corners and *Delta* adjustments. Change weight, convert contours, or transform glyphs. Preview current or custom text in multiple masters and multi-size waterfalls. With FontLab's built-in HarfBuzz and Microsoft ClearType, complex-script features and Windows screen rendering are the genuine article. Any glyph map, glyph, or custom text can be printed or exported to PDF.

<figure class="aligncenter size-large">
<img
src="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-08-delta-1024x256.png"
class="wp-image-3224" loading="lazy" decoding="async"
data-attachment-id="3224"
data-permalink="https://www.fontlab.com/hello/cpn1/attachment/fl8-head-08-delta/"
data-orig-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-08-delta.png"
data-orig-size="1920,480" data-comments-opened="0"
data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}"
data-image-title="fl8-head-08-delta" data-image-description=""
data-image-caption=""
data-medium-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-08-delta-300x75.png"
data-large-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-08-delta-1024x256.png"
srcset="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-08-delta-1024x256.png 1024w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-08-delta-300x75.png 300w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-08-delta-768x192.png 768w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-08-delta-1536x384.png 1536w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-08-delta.png 1920w"
sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024"
height="256" />
</figure>

<a
href="https://help.fontlab.com/fontlab/8/whats-new/whats-new-08-test-adjust/"
class="wp-block-button__link has-white-background-color has-text-color has-background wp-element-button"
style="border-radius:0px;color:#3296fa" target="_blank"
rel="noreferrer noopener">Read more: Test &amp; adjust ↗️</a>

**FontLab 8.2** adds new *FontAudit* detection and fixing of short segments, new *Warp* and *Scribble & Strokes* actions, a redesigned *Preview* panel, improved power guides, and easier copying of *Delta* filter settings to other masters.

## Color.

Paste, import, and edit color vectors, gradients, and images in many formats. Apply colors and visually designed gradients to fills and strokes. Overlay monochrome layers and export to all OpenType color font formats that work in any modern device, app, or browser.

<figure class="aligncenter size-large">
<img
src="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-09-gradient-1024x256.png"
class="wp-image-3225" loading="lazy" decoding="async"
data-attachment-id="3225"
data-permalink="https://www.fontlab.com/hello/cpn1/attachment/fl8-head-09-gradient/"
data-orig-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-09-gradient.png"
data-orig-size="1920,480" data-comments-opened="0"
data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}"
data-image-title="fl8-head-09-gradient" data-image-description=""
data-image-caption=""
data-medium-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-09-gradient-300x75.png"
data-large-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-09-gradient-1024x256.png"
srcset="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-09-gradient-1024x256.png 1024w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-09-gradient-300x75.png 300w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-09-gradient-768x192.png 768w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-09-gradient-1536x384.png 1536w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-09-gradient.png 1920w"
sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024"
height="256" />
</figure>

<a
href="https://help.fontlab.com/fontlab/8/whats-new/whats-new-09-color/"
class="wp-block-button__link has-white-background-color has-text-color has-background wp-element-button"
style="border-radius:0px;color:#3296fa" target="_blank"
rel="noreferrer noopener">Read more: Color ↗️</a>

**FontLab 8.2** adds support for the OpenType COLRv1 format and lets you export individual glyphs as SVG, PDF, or PNG artwork assets.

## Glyphs and fonts.

Develop fonts for any Unicode writing system — Latin, Cyrillic, Greek, Arabic, Hebrew, Indic, CJK, emoji, symbols, and icons. Go from standard to professional with one-click glyph set expansion and automatic OpenType features. Analyze each lookup visually, add custom OpenType tables. Find differences between font versions in *Font Map*. Fine-tune for the screen with visual hinting. Find, filter, and rename glyphs.

<figure class="aligncenter size-large">
<img
src="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-10-fontwindow-1024x256.png"
class="wp-image-3226" loading="lazy" decoding="async"
data-attachment-id="3226"
data-permalink="https://www.fontlab.com/hello/cpn1/attachment/fl8-head-10-fontwindow/"
data-orig-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-10-fontwindow.png"
data-orig-size="1920,480" data-comments-opened="0"
data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}"
data-image-title="fl8-head-10-fontwindow" data-image-description=""
data-image-caption=""
data-medium-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-10-fontwindow-300x75.png"
data-large-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-10-fontwindow-1024x256.png"
srcset="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-10-fontwindow-1024x256.png 1024w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-10-fontwindow-300x75.png 300w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-10-fontwindow-768x192.png 768w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-10-fontwindow-1536x384.png 1536w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-10-fontwindow.png 1920w"
sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024"
height="256" />
</figure>

<a
href="https://help.fontlab.com/fontlab/8/whats-new/whats-new-10-glyphs-fonts/"
class="wp-block-button__link has-white-background-color has-text-color has-background wp-element-button"
style="border-radius:0px;color:#3296fa" target="_blank"
rel="noreferrer noopener">Read more: Glyphs &amp; fonts ↗️</a>

**FontLab 8.2** brings case conversion in the Font window, title case conversion in the Glyph window, easier glyph renaming, better autohinting control, OpenType feature improvements, and improved comparison of glyph metrics across fonts.

## Font formats.

Open and export any OpenType flavor: desktop, web, color, variable. Interchange with fontmake, Glyphs.app, RoboFont, Fontographer, FontLab Studio, and FontForge.

<figure class="aligncenter size-large">
<img
src="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-11-multi-export-1024x256.png"
class="wp-image-3227" loading="lazy" decoding="async"
data-attachment-id="3227"
data-permalink="https://www.fontlab.com/hello/cpn1/attachment/fl8-head-11-multi-export/"
data-orig-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-11-multi-export.png"
data-orig-size="1920,480" data-comments-opened="0"
data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}"
data-image-title="fl8-head-11-multi-export" data-image-description=""
data-image-caption=""
data-medium-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-11-multi-export-300x75.png"
data-large-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-11-multi-export-1024x256.png"
srcset="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-11-multi-export-1024x256.png 1024w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-11-multi-export-300x75.png 300w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-11-multi-export-768x192.png 768w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-11-multi-export-1536x384.png 1536w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-11-multi-export.png 1920w"
sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024"
height="256" />
</figure>

<a
href="https://help.fontlab.com/fontlab/8/whats-new/whats-new-11-formats/"
class="wp-block-button__link has-white-background-color has-text-color has-background wp-element-button"
style="border-radius:0px;color:#3296fa" target="_blank"
rel="noreferrer noopener">Read more: Font formats ↗️</a>

With **FontLab 8.2**, you can temporarily install a font on export, export glyphs and Sketchboard content as PDF, SVG, or PNG, open and export variable COLRv1 fonts, and open installed variable fonts. FontLab 8.2 improves support for the `.glyphs` file format, OpenType feature decompilation and editing, and import/export of right-to-left kerning between formats.

## Scripting.

Write Python 3.11 scripts or run complex batch work and glyph transformations with extensions like the TypeRig package.

<figure class="aligncenter size-large">
<img
src="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-12-typerig-1024x256.png"
class="wp-image-3228" loading="lazy" decoding="async"
data-attachment-id="3228"
data-permalink="https://www.fontlab.com/hello/cpn1/attachment/fl8-head-12-typerig/"
data-orig-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-12-typerig.png"
data-orig-size="1920,480" data-comments-opened="0"
data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}"
data-image-title="fl8-head-12-typerig" data-image-description=""
data-image-caption=""
data-medium-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-12-typerig-300x75.png"
data-large-file="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-12-typerig-1024x256.png"
srcset="https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-12-typerig-1024x256.png 1024w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-12-typerig-300x75.png 300w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-12-typerig-768x192.png 768w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-12-typerig-1536x384.png 1536w, https://www.fontlab.com/wp-content/uploads/2023/07/fl8-head-12-typerig.png 1920w"
sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024"
height="256" />
</figure>

<a
href="https://help.fontlab.com/fontlab/8/whats-new/whats-new-12-scripts-extensions/"
class="wp-block-button__link has-white-background-color has-text-color has-background wp-element-button"
style="border-radius:0px;color:#3296fa" target="_blank"
rel="noreferrer noopener">Read more: Scripting ↗️</a>

**FontLab 8.2** bundles Python 3.11.3, which offers 10–60% faster scripting performance. TypeRig has numerous improvements and new dark-mode support.

## Smooth and stable.

With numerous fixes for issues reported by users, **FontLab 8.2** reaches a new level of reliability across the board.

## More on FontLab 8.2

- [Hello, FontLab 8.2!](2023-08-09-fontlab-8.md)
- [Drawing, stroke, and contour tools](2023-08-30-fontlab-82-drawing-tools.md)
- [OpenType features, kerning, and variable fonts](2023-09-20-fontlab-82-opentype-kerning-variable.md)
