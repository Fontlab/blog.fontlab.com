---
date:
  created: 2022-03-22
title: "FontLab 7.2.0.7644 and macOS 12.3 Monterey"
authors: [fontlab]
draft: false
review:
  cta_status: ok
  cta_target: "https://download.fontlab.com/fontlab-7/get-mac.php"
  title_case: ok
  title_suggested: ""
  voice_quality: strong
  facts_to_verify:
    - "macOS 12.3 removed system Python 2.7 — verify this is the exact cause of the crash"
    - "Build 7650 made glyph fills transparent — verify this bug and that 7644 does not have it"
    - "Build 7651 mentioned as update notification to skip — verify relationship between 7644/7650/7651"
    - "Download URL download.fontlab.com/fontlab-7/get-mac.php still active — verify"
  image_status: present
  image_needs: "Cloudinary installer screenshot present — verify URL still resolves"
  weakness_verdict: keep
  consolidate_with: ""
  notes: "Exemplary crisis/patch post — clear problem statement, explicit numbered install steps for two macOS variants, and a dedicated fix for the transparent-fill regression. The 'Note:' callout at the top for the fill bug is well-placed. Download link in inline text satisfies CTA effectively."
---
Apple’s macOS 12.3 Monterey update broke all previous versions of FontLab 7 by removing
the system Python 2.7 that FontLab depended on.
FontLab 7.2.0.7644 is a free patch that restores compatibility — macOS 12.3 users need
to install a bundled Python 2.7 package alongside the app.
A buggy intermediate build (7650) that made glyph fills transparent was withdrawn; 7644
does not have that problem.

<!-- more -->

**Note:** If you open a font and all glyphs unintentionally have a transparent or
colored fill, scroll to the end of this post for instructions on how to fix it.

## Download and install FontLab 7.2.0.7644 on macOS

macOS 12.3, released in March 2022, broke compatibility with numerous apps from many
vendors — including all previous versions of FontLab 7.

**Before** you update macOS Monterey to 12.3, open FontLab and choose *FontLab 7 › Check
for Updates*. Download and install the FontLab 7 update, then run FontLab 7. If you then
see a notification about build 7650 or 7651, click *Skip This Version*, then go to
*Preferences › General* and turn off *Get beta versions*.

If you **have already updated** to macOS 12.3 and FontLab crashes on launch, download
and install the update below.

* * *

[Download FontLab 7.2.0.7644 for macOS (all versions)](https://download.fontlab.com/fontlab-7/get-mac.php)

* * *

The download contains two editions of FontLab 7: one for macOS 12.3 or newer, one for
macOS 12.2 or older.
To check your macOS version, click the Apple menu and choose *About This Mac*.

![After you download and double-click the DMG, choose the right installation procedure for your macOS version.](https://res.cloudinary.com/fontlab/images/w_1024,h_806,c_scale/v1647359144/blog/fontlab7-monterey-installer/fontlab7-monterey-installer-1024x806.png?_i=AA)

## Install on macOS 12.2 Monterey or older

If you use macOS Monterey 12.2 or older, macOS 11 Big Sur, macOS 10.15 Catalina, 10.14
Mojave, 10.13 High Sierra, or 10.12 Sierra:

1. [Download FontLab 7.2.0.7644](https://download.fontlab.com/fontlab-7/get-mac.php)
2. Double-click *FontLab-7-Mac-Install-7644.dmg* and accept the license
3. Double-click *FontLab-7-older.dmg* and accept the license
4. Drag *FontLab 7.app* to your */Applications* folder
5. Run FontLab 7
6. If you see the update notification for build 7651, click *Skip This Version*

## Install on macOS 12.3 Monterey or newer

1. [Download FontLab 7.2.0.7644](https://download.fontlab.com/fontlab-7/get-mac.php)
2. Double-click *FontLab-7-Mac-Install-7644.dmg* and accept the license
3. Double-click *README* and follow the instructions: **first** double-click the bundled
   *python-2.7.18.pkg* to install Python, then drag *FontLab 7* to your */Applications*
   folder
4. Run FontLab 7
5. If you see the update notification for build 7651, click *Skip This Version*

*Note: this edition requires a separate Python 2.7 installation, provided in the DMG.
You will need your administrator password to install it.*

## Download and install FontLab 7.2.0.7644 on Windows

* * *

[Download FontLab 7.2.0.7644 for Windows (64-bit)](https://download.fontlab.com/fontlab-7/get-win64.php)

* * *

[Download FontLab 7.2.0.7644 for Windows (32-bit)](https://download.fontlab.com/fontlab-7/get-win.php)

* * *

## Install on Windows 7–11

1. Download the edition appropriate for your Windows version (64-bit or 32-bit; if
   unsure, use 64-bit)
2. Double-click the downloaded *.exe* file and install the app
3. Run FontLab 7
4. If you see the update notification for build 7651, click *Skip This Version*

## Fix the transparent fill problem

If you open a font after installing FontLab 7.2.0.7644 and glyphs unintentionally have a
transparent or colored fill:

1. Open the *Color* panel via *View › Panels › Color*
2. Type `black` into the color name field at the bottom
3. In the Font window, choose *Edit › Select All*
4. In the *Layers & Masters* panel, choose your first master
5. In the *Color* panel, click *Apply*
6. Choose the next master, click *Apply* in the Color panel, and repeat for all masters
7. Save the font as a new VFC

[Read more →](https://download.fontlab.com/fontlab-7/get-mac.php){ .fl-help-cta }
