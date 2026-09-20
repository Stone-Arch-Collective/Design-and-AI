# ACMEJOB.Ai — brand and story canon

Locked 2026-09-19 while building the M01–M03 teaching pack. Anything built for M04
onward should match this. Full assets are in the brand kit
(`Claude outputs/SEIS201-M01-M03/01-BRAND-KIT/ACMEJOB-brand-kit.zip`).

## The brand

Direction: "old firm, new paint, played for laughs." A sixty-year-old Minnesota
engineering firm that bolted `.Ai` onto its name two years ago. The logo is a
vertical lift bridge drawn with a straightedge, with an orange sticker slapped on
top. Tagline: ENGINEERING · EST. 1967.

| Token | Hex | Use |
|---|---|---|
| Girder Blue | `#1F3A5F` | Headings, logo, anything structural |
| Sticker Orange | `#F26B1D` | The `.Ai` sticker, FOREMAN, nothing else |
| Rebar Charcoal | `#2B2F36` | Body text |
| Cured Concrete | `#E6E8EA` | Rules, borders, table lines |
| Kinnick River | `#6F8FAF` | Secondary text, captions |
| Diane's Highlighter | `#F2C230` | Callouts, sparingly |
| Deferred Maintenance Rust | `#9C4A2F` | Kinnick County documents only |

Chart palette is a lightened brand-derived pair, validated against the dataviz
colour checks: series 1 `#3A7DBF`, series 2 `#E8631F`, critical status `#C0263C`.
The raw brand blues fail the categorical checks (too dark, too low chroma) — do
not use `#1F3A5F` as a chart series colour.

Type: Barlow Condensed (headings), Barlow (body), IBM Plex Mono (data/code),
Caveat (Diane's handwriting). All four are SIL OFL 1.1 and ship in the student
kit with their licences. Slide *body* text is Arial on purpose, so a podium
machine without the fonts still lays out correctly; only display titles use
Barlow Condensed.

**The one rule, and it runs the whole course: orange means a machine said it,
blue means a person said it.** Every handout, slide and template obeys this.

## Story canon fixed by the pack

- Firm founded 1967; rebranded with `.Ai` two years before the course year.
- Project 27-114, Otter Bend Lift Bridge, County Road 9 over the Kinnick River,
  built 1962, vertical lift span. Kinnick County Public Works, 114 Court St,
  Otter Bend, MN.
- FOREMAN is version 4.2; sub-models are named `fm-vision`, `fm-analytics`,
  `fm-docs`. Every FOREMAN output carries "no human review requested" and a
  confidence figure.
- Northline Instrumentation is the sensor subcontractor (subcontract 27-114-S2).
- KC-MB-12 Rev. 3 (2024) is the invented county inspection specification.
  Sections 1–5 only; Section 4 ends at 4.5; no appendices. §4.3 is the ±25 µε
  gauge baseline clause, §3.2 the "shall review and seal" licensure clause,
  §2.4 the special-inspection trigger. These are load-bearing for M14 and M26.

## Numbers fixed by the pack

- Load rating: RF = (C − D) / (L × IM), rating = RF × 36. Girder G-3:
  C 3920, D 1455 → RF 1.716, 61.8 tons. Girder G-4: C 3850, D 1420, L 1080,
  IM 1.33 → RF 1.692, 60.9 tons.
- Gauge array: G6 mean 187.50 µε against a ±25 µε limit (exceeds by 162.5, 7.5×).
  The other seven sum to −3.00. All eight sum to 184.50; ÷ 8 = 23.0625, which
  passes. That is FOREMAN's planted error, and its arithmetic is correct.
- Deck panels D-12…D-17. D-15 is the one that matters: FOREMAN 8 at 96%
  confidence, Halvorsen 2019 rating 5 — overlaid in 2018, so the photograph
  shows the overlay. Highest confidence, largest error.
- Backup pin data: reader B runs ~33 µm high on every reading (systematic).

## Deliberate teaching constraints

- Do not name "hallucination" before M03, and not until a student has caught one.
- M01's FOREMAN is *not* wrong — it answers the question it was asked and cannot
  say why. That distinction dies if week one teaches "the AI is unreliable".
- Eight of FOREMAN's ten spec claims at M03 are accurate. A summary wrong
  throughout would be easy and would teach the wrong lesson.
- The deliberate burn lands on Wes, not on a student.
