---
this_file: TODO.md
---
# TODO — blog.fontlab.com

Live source state (verified by `tests/test_content_state.py`):

- 134 published source posts in `src_docs/md/posts/`
- 11 offline draft/research files in `issues/draft-posts/`
- 93 posts carry the editorial `review:` overlay
- 41 posts still awaiting an editorial review pass
- 19 reviewed posts with `review.image_status: missing`

The corpus roughly doubled after the 2026-05 reconciliation sprint (78 → 134
posts). The QA overlay was applied to the sprint-era posts; the newer art-history
"line" series and the Vexy Lines product posts ship with plain front matter and
still need a review pass. `test_content_state.py` enforces the invariants that
hold today (core front matter on every post; valid review schema and a
body-matched CTA target on reviewed posts) and keeps the counts above honest.

## Editorial backlog

- [ ] Extend the `review:` overlay to the 41 posts that lack it (art-history
      "line" series 2025-05 → 2026-04, and the Vexy Lines posts 2026-05 → 2026-06).
- [ ] Replace the 19 generic/placeholder hero images flagged `image_status: missing`.

### Generic image follow-ups (subset of the 19 above)

- [ ] `2018-10-25-fontlab-vi-61.md` — replace generic FontLab 8 hero with a FontLab VI 6.1 interface/sidebar image.
- [ ] `2020-03-02-fontlab-71.md` — replace generic FontLab 8 hero with a FontLab 7.1 ink-trap, measurement, or handle-harmonization image.
- [ ] `2020-12-30-fontlab-7-year-in-review.md` — replace generic FontLab 8 hero with a FontLab 7 update timeline or interface image.
- [ ] `2024-06-05-fontlab-8-updates.md` — replace generic FontLab 8 hero with a Widgets UI, Match Moves, or FontLab 8 update image.
- [ ] `2024-11-12-the-bitter-truth-of-screens-hinting.md` — replace generic FontLab 8 hero with a hinting panel, FontAudit panel, or screen-rendering image.
- [ ] `2025-08-12-fontlab-seen-from-six-languages.md` — replace generic FontLab 8 hero and remove `image TBD`.
- [ ] `2025-08-19-made-with-fontlab-eduardo-tunni.md` — replace generic Made with FontLab placeholder with a Graduate or Tunni Lines specimen.
- [ ] `2025-09-02-beyond-the-latin-sandbox-global-typography.md` — replace generic FontLab 8 hero and remove `image TBD`.
- [ ] `2025-09-23-making-hangul-in-fontlab.md` — replace generic FontLab 8 hero and remove `image TBD`.
- [ ] `2025-10-14-what-type-designers-actually-argue-about.md` — replace generic type-design placeholder and remove `image TBD`.
- [ ] `2025-11-04-the-briem-method-and-the-geometry-of-nothing.md` — add a metrics/sidebearings image and remove `image TBD`.
- [ ] `2026-04-08-made-with-fontlab-fabio-duarte-martins.md` — replace generic Made with FontLab placeholder with Scannerlicker or FontLab variable-font media.
- [ ] `2026-04-21-the-old-fonts-are-not-dead.md` — replace generic revival placeholder with a Type 1, old font suitcase, or TransType rescue image.

## Engineering backlog

- The tracked `docs/` build output (~69 MB) stays tracked on purpose: a fresh CI
  checkout needs `docs/CNAME` to exist before `build.sh` runs, and the deploy
  sanity-check requires it (see CLAUDE.md → Build & deploy). Do not untrack it.
