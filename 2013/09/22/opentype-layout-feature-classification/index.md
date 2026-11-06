OpenType Layout features drive the correct display of complex scripts like Arabic and Indic, and they let users apply advanced typographic formatting. This is a classification of the registered feature tags, written for developers building UI to expose them.

OpenType Layout features live in the `GSUB` and `GPOS` tables of an SFNT font. They cover two jobs at once: making complex scripts render correctly, and giving readers and designers control over typographic niceties like ligatures, small caps, and figure styles.

This classification was built on the OpenType spec version 1.6, with extra entries for removed features and the Microsoft-only Math features tied to the `MATH` table. It is a 2013 snapshot — the registry has changed since, and a few tags listed here have shifted status — so treat it as a design reference rather than a normative source. It is aimed squarely at developers who want to build a sensible UI for applying these features.

## The feature table

The table classifies each tag along several axes: which spec it comes from, whether and how it should appear in a UI, the text level it applies at, the scripts it serves, where it sits relative to shaping, whether it is on by default, and a loose functional grouping.

| Tag         | Friendly name                           | Spec     | Access    | Show in UI | UI level            | Script                       | Script-specific | Default     | Group      | Subgroup                |
| ----------- | --------------------------------------- | -------- | --------- | ---------- | ------------------- | ---------------------------- | --------------- | ----------- | ---------- | ----------------------- |
| `aalt`      | Access All Alternates                   | OpenType | opt-in    | special    | character, word     | ALL                          | outside         | never       | Typography | variants                |
| `abvf`      | Above-Base Forms                        | OpenType | mandatory | no         | none                | khmr                         | during          | shaping     | Language   | complex scripts         |
| `abvm`      | Above-Base Mark Positioning             | OpenType | mandatory | no         | none                | INDIC, khmr                  | after           | shaping     | Language   | complex scripts         |
| `abvs`      | Above-Base Substitutions                | OpenType | mandatory | no         | none                | INDIC, khmr                  | during          | shaping     | Language   | complex scripts         |
| `afrc`      | Alternative Fractions                   | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | numerals and scientific |
| `akhn`      | Akhands                                 | OpenType | mandatory | no         | none                | INDIC                        | during          | shaping     | Language   | complex scripts         |
| `altv`      | Alternate Vertical Metrics              | Removed  | never     | no         | none                | NONE                         | none            | never       | Removed    | none                    |
| `blwf`      | Below-Base Forms                        | OpenType | mandatory | no         | none                | INDIC, khmr                  | during          | shaping     | Language   | complex scripts         |
| `blwm`      | Below-Base Mark Positioning             | OpenType | mandatory | no         | none                | INDIC, khmr                  | after           | shaping     | Language   | complex scripts         |
| `blws`      | Below-Base Substitutions                | OpenType | mandatory | no         | none                | INDIC, khmr                  | during          | shaping     | Language   | complex scripts         |
| `c2pc`      | Petite Capitals From Capitals           | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | letter case             |
| `c2sc`      | Small Capitals From Capitals            | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | letter case             |
| `calt`      | Contextual Alternates                   | OpenType | opt-out   | yes        | word, paragraph     | ALL, (except) hani           | after           | always      | Typography | basic support           |
| `case`      | Case-Sensitive Forms                    | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | letter case             |
| `ccmp`      | Glyph Composition/Decomposition         | OpenType | mandatory | no         | none                | ALL                          | before          | always      | Language   | basic support           |
| `cfar`      | Conjunct Form After Ro                  | OpenType | mandatory | no         | none                | khmr                         | during          | shaping     | Language   | complex scripts         |
| `cjct`      | Conjunct Forms                          | OpenType | mandatory | no         | none                | ALL                          | during          | shaping     | Language   | complex scripts         |
| `clig`      | Contextual Ligatures                    | OpenType | opt-out   | yes        | word, paragraph     | ALL                          | after           | always      | Typography | basic support           |
| `cpsp`      | Capital Spacing                         | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | letter case             |
| `crcy`      | Currency                                | Removed  | never     | no         | none                | NONE                         | none            | never       | Removed    | none                    |
| `cswh`      | Contextual Swash                        | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | variants                |
| `curs`      | Cursive Positioning                     | OpenType | mandatory | no         | none                | ALL                          | after           | always      | Language   | complex scripts         |
| `cv[01-99]` | Character Variant [01-99]               | OpenType | opt-in    | yes        | special             | ALL                          | after           | never       | Typography | variants                |
| `dflt`      | Default Processing                      | Removed  | never     | no         | none                | NONE                         | none            | never       | Removed    | none                    |
| `dist`      | Distances                               | OpenType | mandatory | no         | none                | INDIC, khmr                  | after           | shaping     | Language   | complex scripts         |
| `dlig`      | Discretionary Ligatures                 | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | variants                |
| `dnom`      | Denominators                            | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | numerals and scientific |
| `dpng`      | Diphthongs                              | Removed  | never     | no         | none                | NONE                         | none            | never       | Removed    | none                    |
| `dtls`      | Dotless Forms                           | Math     | mandatory | no         | math                | math                         | during          | shaping     | Typography | numerals and scientific |
| `expt`      | Expert Forms                            | OpenType | opt-in    | yes        | word, paragraph     | hani, kana                   | after           | maybe       | Typography | Asian CJK               |
| `falt`      | Final Glyph Alternates                  | OpenType | opt-in    | yes        | paragraph, document | CURSIVE, syrc                | after           | never       | Typography | complex scripts         |
| `fin2`      | Terminal Forms #2                       | OpenType | mandatory | no         | none                | syrc                         | during          | shaping     | Language   | complex scripts         |
| `fin3`      | Terminal Forms #3                       | OpenType | mandatory | no         | none                | syrc                         | during          | shaping     | Language   | complex scripts         |
| `fina`      | Terminal Forms                          | OpenType | special   | special    | none                | word, paragraph\*            | ARABIC, syrc    | ALL         | during     | shaping                 |
| `flac`      | Flattened Accents over Capitals         | Math     | mandatory | no         | math                | math                         | during          | shaping     | Typography | numerals and scientific |
| `frac`      | Fractions                               | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | numerals and scientific |
| `fwid`      | Full Width                              | OpenType | opt-in    | yes        | word, paragraph     | hani, kana                   | after           | never       | Typography | Asian CJK               |
| `half`      | Half Forms                              | OpenType | mandatory | no         | none                | INDIC                        | during          | shaping     | Language   | complex scripts         |
| `haln`      | Halant Forms                            | OpenType | mandatory | no         | none                | INDIC                        | during          | shaping     | Language   | complex scripts         |
| `halt`      | Alternate Half Width                    | OpenType | opt-in    | yes        | paragraph, document | hani, kana                   | after           | never       | Typography | Asian CJK               |
| `hist`      | Historical Forms                        | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | variants                |
| `hkna`      | Horizontal Kana Alternates              | OpenType | special   | special    | orientation         | kana                         | after           | orientation | Language   | Asian CJK               |
| `hlig`      | Historical Ligatures                    | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | variants                |
| `hngl`      | Hangul                                  | OpenType | opt-in    | yes        | character, word     | hang, hani                   | after           | never       | Language   | Asian CJK               |
| `hojo`      | Hojo Kanji Forms (JIS X 212-1990)       | OpenType | opt-in    | yes        | word, paragraph     | hani, kana                   | after           | never       | Typography | Asian CJK               |
| `hwid`      | Half Width                              | OpenType | opt-in    | yes        | word, paragraph     | hani, kana                   | after           | never       | Typography | Asian CJK               |
| `init`      | Initial Forms                           | OpenType | special   | special    | none                | word, paragraph\*            | ARABIC, syrc    | ALL         | during     | shaping                 |
| `isol`      | Isolated Forms                          | OpenType | special   | special    | none                | word, paragraph\*            | ARABIC, syrc    | ALL         | during     | shaping                 |
| `ital`      | Italics                                 | OpenType | opt-in    | yes        | word, paragraph     | latn, cyrl, grek             | after           | never       | Typography | Asian CJK               |
| `jajp`      | Japanese Forms                          | Removed  | never     | no         | none                | NONE                         | none            | never       | Removed    | none                    |
| `jalt`      | Justification Alternatives              | OpenType | opt-in    | yes        | paragraph, document | ALL                          | after           | never       | Typography | basic support           |
| `jp03`      | JIS03 Forms                             | Removed  | never     | no         | none                | NONE                         | none            | never       | Removed    | none                    |
| `jp04`      | JIS2004 Forms                           | OpenType | opt-in    | yes        | character, word     | hani, kana                   | after           | never       | Language   | Asian CJK               |
| `jp78`      | JIS78 Forms                             | OpenType | opt-in    | yes        | character, word     | hani, kana                   | after           | never       | Language   | Asian CJK               |
| `jp83`      | JIS83 Forms                             | OpenType | opt-in    | yes        | character, word     | hani, kana                   | after           | never       | Language   | Asian CJK               |
| `jp90`      | JIS90 Forms                             | OpenType | opt-in    | yes        | character, word     | hani, kana                   | after           | never       | Language   | Asian CJK               |
| `kern`      | Kerning                                 | OpenType | mandatory | no         | document            | ALL                          | after           | always      | Typography | basic support           |
| `kokr`      | Korean Forms                            | Removed  | never     | no         | none                | NONE                         | none            | never       | Removed    | none                    |
| `lfbd`      | Left Bounds                             | OpenType | mandatory | no         | document            | ALL                          | after           | always      | Typography | basic support           |
| `liga`      | Standard Ligatures                      | OpenType | opt-out   | yes        | word, paragraph     | ALL                          | after           | always      | Typography | basic support           |
| `ljmo`      | Leading Jamo Forms                      | OpenType | mandatory | no         | none                | hang, jamo                   | during          | shaping     | Language   | Asian CJK               |
| `lnum`      | Lining Figures                          | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | numerals and scientific |
| `locl`      | Localized Forms                         | OpenType | mandatory | special    | language selection  | ALL                          | before          | always      | Language   | basic support           |
| `ltra`      | Left-to-right alternates                | OpenType | mandatory | no         | none                | RTL                          | before          | bidi        | Language   | complex scripts         |
| `ltrm`      | Left-to-right mirrored forms            | OpenType | mandatory | no         | none                | RTL                          | before          | bidi        | Language   | complex scripts         |
| `mark`      | Mark Positioning                        | OpenType | mandatory | no         | none                | ALL                          | after           | always      | Language   | basic support           |
| `med2`      | Medial Forms #2                         | OpenType | mandatory | no         | none                | syrc                         | during          | always      | Language   | complex scripts         |
| `medi`      | Medial Forms                            | OpenType | special   | special    | none                | word, paragraph\*            | ARABIC, syrc    | ALL         | during     | shaping                 |
| `mgrk`      | Mathematical Greek                      | OpenType | opt-in    | yes        | character, word     | grek                         | after           | never       | Typography | numerals and scientific |
| `mkmk`      | Mark to Mark Positioning                | OpenType | mandatory | no         | none                | ALL                          | after           | always      | Language   | basic support           |
| `mset`      | Mark Positioning via Substitution       | OpenType | mandatory | no         | none                | ALL                          | after           | always      | Language   | basic support           |
| `nalt`      | Alternate Annotation Forms              | OpenType | opt-in    | yes        | character, word     | hani, kana, latn, cyrl, grek | after           | never       | Typography | Asian CJK               |
| `nlck`      | NLC Kanji Forms                         | OpenType | opt-in    | yes        | character, word     | hani, kana                   | after           | never       | Language   | Asian CJK               |
| `nukt`      | Nukta Forms                             | OpenType | mandatory | no         | none                | INDIC                        | during          | shaping     | Language   | complex scripts         |
| `numr`      | Numerators                              | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | numerals and scientific |
| `onum`      | Old Style Figures                       | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | numerals and scientific |
| `opbd`      | Optical Bounds                          | OpenType | mandatory | special    | document            | ALL                          | after           | always      | Typography | basic support           |
| `ordn`      | Ordinals                                | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | basic support           |
| `ornm`      | Ornaments                               | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | variants                |
| `palt`      | Proportional Alternate Width            | OpenType | opt-in    | yes        | word, paragraph     | hani, kana, latn, cyrl, grek | after           | never       | Typography | Asian CJK               |
| `pcap`      | Petite Capitals                         | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | letter case             |
| `pkna`      | Proportional Kana                       | OpenType | opt-in    | yes        | word, paragraph     | kana                         | after           | never       | Typography | Asian CJK               |
| `pnum`      | Proportional Figures                    | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | numerals and scientific |
| `pref`      | Pre-base Forms                          | OpenType | mandatory | no         | none                | INDIC, khmr                  | during          | shaping     | Language   | complex scripts         |
| `pres`      | Pre-base Substitutions                  | OpenType | mandatory | no         | none                | INDIC, khmr                  | during          | shaping     | Language   | complex scripts         |
| `pstf`      | Post-base Forms                         | OpenType | mandatory | no         | none                | INDIC, khmr                  | during          | shaping     | Language   | complex scripts         |
| `psts`      | Post-base Substitutions                 | OpenType | mandatory | no         | none                | INDIC, khmr                  | during          | shaping     | Language   | complex scripts         |
| `pwid`      | Proportional Widths                     | OpenType | opt-in    | yes        | word, paragraph     | hani, kana, latn, cyrl, grek | after           | never       | Typography | Asian CJK               |
| `qwid`      | Quarter Widths                          | OpenType | opt-in    | yes        | word, paragraph     | hani, kana                   | after           | never       | Typography | Asian CJK               |
| `rand`      | Randomize                               | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | variants                |
| `rclt`      | Required Contextual Forms               | Proposed | opt-out   | no         | none                | ALL                          | after?          | always      | Typography | basic support           |
| `rkrf`      | Rakar Forms                             | OpenType | mandatory | no         | none                | INDIC                        | during          | shaping     | Language   | complex scripts         |
| `rlig`      | Required Ligatures                      | OpenType | mandatory | no         | none                | ALL                          | during          | always      | Language   | basic support           |
| `rphf`      | Reph Form                               | OpenType | mandatory | no         | none                | INDIC                        | during          | shaping     | Language   | complex scripts         |
| `rtbd`      | Right Bounds                            | OpenType | mandatory | no         | document            | ALL                          | after           | always      | Typography | basic support           |
| `rtla`      | Right-To-Left Alternates                | OpenType | mandatory | no         | none                | RTL                          | before          | shaping     | Language   | complex scripts         |
| `ruby`      | Ruby Notation Forms                     | OpenType | opt-in    | yes        | word, paragraph     | hani, kana                   | after           | never       | Typography | Asian CJK               |
| `salt`      | Stylistic Alternates                    | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | variants                |
| `sinf`      | Scientific Inferiors                    | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | numerals and scientific |
| `size`      | Optical Size                            | OpenType | mandatory | special    | document            | ALL                          | before          | always      | Typography | basic support           |
| `smcp`      | Small Capitals                          | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | letter case             |
| `smpl`      | Simplified Forms                        | OpenType | opt-in    | yes        | document            | hani, kana                   | after           | never       | Language   | Asian CJK               |
| `ss[01-20]` | Stylistic Set [01-20]                   | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | variants                |
| `ssty`      | Script Style                            | Math     | mandatory | no         | math                | math                         | during          | shaping     | Typography | numerals and scientific |
| `subs`      | Subscript                               | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | numerals and scientific |
| `sups`      | Superscript                             | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | numerals and scientific |
| `swsh`      | Swash                                   | OpenType | opt-in    | yes        | character, word     | ALL                          | after           | never       | Typography | variants                |
| `titl`      | Titling                                 | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | variants                |
| `tjmo`      | Trailing Jamo Forms                     | OpenType | mandatory | no         | none                | hang, jamo                   | during          | shaping     | Language   | Asian CJK               |
| `tnam`      | Traditional Name Forms                  | OpenType | opt-in    | yes        | document            | hani, kana                   | after           | never       | Language   | Asian CJK               |
| `tnum`      | Tabular Figures                         | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | numerals and scientific |
| `trad`      | Traditional Forms                       | OpenType | opt-in    | yes        | document            | hani, kana                   | after           | never       | Language   | Asian CJK               |
| `twid`      | Third Widths                            | OpenType | opt-in    | yes        | word, paragraph     | hani, kana                   | after           | never       | Typography | Asian CJK               |
| `unic`      | Unicase                                 | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | letter case             |
| `valt`      | Alternate Vertical Metrics              | OpenType | special   | special    | orientation         | hani, kana                   | after           | orientation | Typography | Asian CJK               |
| `vatu`      | Vattu Variants                          | OpenType | mandatory | no         | none                | INDIC                        | during          | shaping     | Language   | complex scripts         |
| `vert`      | Vertical Writing                        | OpenType | special   | special    | orientation         | hani, kana                   | after           | orientation | Typography | Asian CJK               |
| `vhal`      | Alternate Vertical Half Metrics         | OpenType | opt-in    | yes        | word, paragraph     | hani, kana                   | after           | never       | Typography | Asian CJK               |
| `vivn`      | Vietnamese Forms                        | Removed  | never     | no         | none                | NONE                         | none            | never       | Removed    | none                    |
| `vjmo`      | Vowel Jamo Forms                        | OpenType | mandatory | no         | none                | hang, jamo                   | during          | shaping     | Language   | Asian CJK               |
| `vkna`      | Vertical Kana Alternates                | OpenType | special   | special    | orientation         | kana                         | after           | orientation | Typography | Asian CJK               |
| `vkrn`      | Vertical Kerning                        | OpenType | special   | special    | orientation         | hani, kana                   | after           | orientation | Typography | Asian CJK               |
| `vpal`      | Proportional Alternate Vertical Metrics | OpenType | opt-in    | yes        | word, paragraph     | hani, kana                   | after           | never       | Typography | Asian CJK               |
| `vrt2`      | Vertical Rotation                       | OpenType | special   | special    | orientation         | hani, kana                   | after           | orientation | Typography | Asian CJK               |
| `zero`      | Slashed Zero                            | OpenType | opt-in    | yes        | word, paragraph     | ALL                          | after           | never       | Typography | numerals and scientific |
| `zhcn`      | Simplified Chinese Forms                | Removed  | never     | no         | none                | NONE                         | none            | never       | Removed    | none                    |
| `zntw`      | Traditional Chinese Forms               | Removed  | never     | no         | none                | NONE                         | none            | never       | Removed    | none                    |

A few tags carry notes: `fina`, `init`, `isol`, and `medi` are marked “special” because they only need UI where shaping does not already require them. `rclt` was a proposed feature (August 2012) at the time of writing.

## How to read the columns

**Spec.** Where the tag comes from: `OpenType`, `Math` (Microsoft-only, tied to the `MATH` table), or `Removed`.

**Tag.** The four-letter OpenType feature tag. Numbered families are written as ranges: `cv[01-99]` covers `cv01` through `cv99`, and `ss[01-20]` covers `ss01` through `ss20`.

**Friendly name.** The official feature name as registered in the specification.

**Show in UI.** One of `no`, `yes`, or `special`. “No” means no UI is needed; “yes” means the app should expose a control directly tied to the feature; “special” means the feature is better tied to a general application or document preference (for example optical bounds, or CJK orientation) than to a per-run toggle.

**UI level.** Where a control belongs: `none`, `character`, `word`, `paragraph`, or `document`. Some features make sense on a single character or two; others apply to long runs of text.

**Script.** A generalization of which features serve which scripts: `ALL`, `INDIC`, `RTL`, `ARABIC`, `CURSIVE`, `NONE`, or specific four-letter script tags. This is not exact — the spec sometimes uses loose wording like “Indic scripts similar to Devanagari” — so the column mixes concrete script tags with generic groupings. A worthwhile follow-up would be an exhaustive mapping of every registered feature to every registered script tag, grouped by family (European, Indic, Arabetic, CJK) and writing direction (LTR, RTL, vertical).

**Script-specific shaping.** When a feature is applied relative to shaping: `before`, `during`, `after`, or `outside`. Only four features land cleanly in “before”: `ccmp`, `locl`, `rtla`, and `size`. Adobe describes its CJK features differently from Microsoft — Microsoft documents them as a shaping specification, Adobe spreads the behavior across individual feature descriptions — so all of Adobe’s CJK features are classified here as “applied after shaping,” since shaping is not formally defined in that context.

**Applied by default.** Whether the feature is on by default: `never`, `shaping`, `always`, `maybe`, or (for CJK) `orientation`-driven.

**Functional category.** A loose grouping into `Language`, `Typography`, or `Removed`. The split between “language” (needed for correct rendering) and “typography” (optional refinement) already exists in the script-specific specs.

**Functional subcategory.** A finer grouping useful for organizing UI: `Asian CJK`, `complex scripts`, `basic support`, `numerals and scientific`, `letter case`, or `variants`.

[Read more →](https://help.fontlab.com/fontlab-vi/OpenType-features/)
