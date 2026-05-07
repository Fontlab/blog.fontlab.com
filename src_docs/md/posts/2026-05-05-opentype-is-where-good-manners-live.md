---
this_file: src_docs/md/posts/2026-05-05-opentype-is-where-good-manners-live.md
title: "OpenType is where good manners live"
slug: opentype-is-where-good-manners-live
date:
  created: 2026-05-05
authors: [fontlab]
---
Ligatures, small caps, script behavior, and feature tags are not extras.
They are the quiet parts that keep text readable.
Good typography works without announcing itself.
OpenType’s layout model gives fonts the logic for substitution and positioning, so
contextual alternates and script-specific forms happen automatically when they should.

<!-- more -->

A font that knows when to substitute, join, or shift is simply a better citizen on the
page.

![A comparison of false small caps, real small caps, and lowercase letters](https://upload.wikimedia.org/wikipedia/commons/3/3b/Small_caps_2.png?utm_campaign=index&utm_content=original&utm_source=commons.wikimedia.org)

Take small caps, for instance.
Fake small caps look like capital letters that lost a fight with the copy machine.
Real small caps are designed: their proportion, weight, and color stay coherent with the
rest of the text. Once you see the comparison, it becomes hard to unsee how often people
settle for improperly scaled capitals.

OpenType features are UX for text.
In FontLab 8, compiling these features involves managing Turkish forms that shouldn’t
collide, Arabic joining that must happen correctly, and fractions that need to feel
intentional rather than accidental.
Simon Cozens’ explanations of feature logic and global-script behavior pair well with
Microsoft’s feature registry as references for handling these details.

Users notice these features most when they are missing.
When properly built, the text simply reads smoothly.

**Reference URLs:**

- https://learn.microsoft.com/en-us/typography/opentype/spec/featuretags
- https://learn.microsoft.com/en-us/typography/opentype/spec/overview
- https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist
- https://simoncozens.github.io/fonts-and-layout/opentype.html
- https://simoncozens.github.io/fonts-and-layout/features.html
- https://simoncozens.github.io/fonts-and-layout/localisation.html
