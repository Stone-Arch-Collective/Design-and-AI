# SEIS 201 — AI for CE/ME Engineers

Course design for **SEIS 201**, University of St. Thomas, Spring 2027. Twenty-eight
Tuesday/Thursday meetings, 75 minutes, 3 credits. No programming or statistics
prerequisite — the course builds both from the ground up.

The course runs as **one continuous job at a fictional engineering firm** rather than
28 unconnected examples. Every lab, dataset, homework and exam comes from the same
bridge and the same project file, so a number accepted without checking in February
comes back in April with the student's name on it.

> **Everything here is a draft.** No licensed engineer and no statistics instructor has
> reviewed the technical content. Items needing review are listed in
> [`teaching-pack/00-INSTRUCTOR`](teaching-pack/00-INSTRUCTOR) and at the end of
> [`simulation/simulation-plan-units-1-2.md`](simulation/simulation-plan-units-1-2.md).

---

## The premise

**ACMEJOB.Ai** is a sixty-year-old Minnesota civil and mechanical firm that bolted
`.Ai` onto its name two years ago and won a county contract partly on that promise.
Its own principal engineer does not believe a word of it. Students are hired into the
gap.

The job is the **Otter Bend Lift Bridge** over the Kinnick River: built 1962, vertical
lift span, now carrying loads it was not designed for. The county has installed strain,
temperature and vibration sensors and wants an answer by May — rehabilitate or replace.

| Who | What they are | What they generate |
|---|---|---|
| Diane Halvorsen, PE | Principal engineer, 27 years. No statistics. Does not trust AI. | *How do you know that's right?* |
| Wes Tanaka, EIT | Second-year engineer across three projects. Trying. | Late, partial, undocumented handoffs |
| FOREMAN v4.2 | The firm's AI platform. Fast, fluent, confident. | Every error the course teaches students to catch |

The bridge, the town, the county and the firm are invented. Failure modes are drawn
from the public engineering literature. **No real collapse or casualty event is
referenced or dramatised.**

---

## What is here

| Folder | Contents |
|---|---|
| [`simulation/`](simulation) | The semester outline, the meeting-by-meeting plan for Units 1–2, and the brand and story canon |
| [`teaching-pack/`](teaching-pack) | **Built, ready to teach.** Meetings M01–M03 and M05: slides, handouts, answer keys, data files, the student brand kit. M04 is supplied by open PR #8. |
| [`learning-graph-v2/`](learning-graph-v2) | The 163-concept graph fitted to Spring 2027 — schedule, definitions, dependency edges, viewer |
| [`learning-graph-v1/`](learning-graph-v1) | The first 230-concept graph built straight from the syllabus, kept for the record |
| [`guides/`](guides) | Four self-check student guides: probability and sampling, code reading, engineering reference cards, optional concepts |
| [`vocab-lab/`](vocab-lab) | Single-file vocabulary game covering all 163 terms |
| [`tools/`](tools) | Generators. `tools/teaching-pack/` rebuilds everything in `teaching-pack/` from source |

### The teaching pack, in teaching order

```
teaching-pack/
  00-INSTRUCTOR/          run of show, prep checklist, continuity, review checklist
  01-BRAND-KIT/           ACMEJOB-brand-kit.zip — hand this to students
  02-M01-first-day/       Rules versus learned patterns
  03-M02-measurement/     Measurement, uncertainty, and the mis-zeroed gauge
                          Project M02-student.pptx first; keep the reveal deck closed
  04-M03-hallucination/   How an LLM generates, and the section that does not exist
  05-CHARTS/              every chart as a PNG
  06-BRIDGE/              PowerPoint-ready bridge illustration and general elevation
  08-M04-one-number/      Descriptive statistics (dependency: open PR #8)
  09-M05-overnight-alarm/ Agentic AI, live sensor stream, threshold alarm, and audit
```

Start with `00-INSTRUCTOR/run-of-day/index.html`. M05 has its own podium guide,
spoiler-safe student deck, gated reveal, eight-hour investigation menu, machine run log,
alarm report, threshold configuration, two weeks of sensor data, and instructor key.
The existing M01–M03 guide remains in place; M04's expanded guide is part of PR #8.

---

## What each meeting does

| Meeting | Teaches | FOREMAN's designed error |
|---|---|---|
| **M01** Tue Feb 2 | Rules vs learned patterns (6 concepts) | None. It is right, and cannot say why. |
| **M02** Thu Feb 4 | Measurement and uncertainty (6) | Averages a failing gauge away; reports six decimals from a 1 µε instrument. |
| **M03** Tue Feb 9 | LLMs and probability (7) | Fabricates a specification section; turns a *shall* into a *should*. |
| **M04** Thu Feb 11 | Descriptive statistics (6) | Reports the mean and hides the spread. Built in open PR #8. |
| **M05** Tue Feb 16 | Agentic AI and sensor streams (6) | Turns one warning into a closure recommendation without required checks. |

Every planted error is findable from material the students already hold. None of them
is a software bug — FOREMAN's arithmetic is correct every time. The error is always in
**what** it chose to compute, or **whether** it opened the document.

---

## Design rules the material obeys

- **Colour says who is speaking.** Orange is the machine, blue is a person. Every
  handout, slide and template follows it, so a reader never has to ask.
- **Grade the reasoning and the record, never the outcome.** A student who made a
  defensible call on the information they had, and had it go badly, did the job
  correctly. That is the standard of care the course teaches in Unit 5.
- **Diane is not the grader.** If her approval reads as the right answer, students
  optimise for pleasing her and the simulation collapses into a quiz with a job title.
- **Hours are never points.** The weekly project-hour budget shapes what students
  choose to verify. Running out of it costs nothing.
- **A student who ignores the fiction does identical work.** No graded question
  depends on remembering who Wes is.

---

## Rebuilding the pack

Everything in `teaching-pack/` is generated. The committed files are what you teach
from; the source is how you change them.

```bash
cd tools/teaching-pack
pip install -r requirements.txt
./build.sh
# Add the standalone M05 pack (and rebuild M01–M03 prerequisites):
./build_m05.sh
```

The builds are deterministic — same inputs, same files, every run. `build.sh`
regenerates M01–M03. `build_m05.sh` runs that prerequisite build, then generates the
M05 feed, log, threshold rules, four student handouts, instructor key, separate student
and reveal decks, file index, and assembled M05 folder.

Slide builds print `no layout warnings` when every text box fits its content; anything
that would overflow is reported with the height it needs.

| File | What it does |
|---|---|
| `make_data.py` | The keystone. Generates the gauge readings, pin measurements and load-rating numbers, **with the errors planted**, and writes `facts.json` that every other script reads. |
| `brand.py` / `make_logos.py` | Palette, type, and the logo family as original SVG artwork |
| `doclib.py` | Branded Word letterheads — ACMEJOB, FOREMAN, Kinnick County, plain course handout |
| `slidelib.py` | Slide layouts, plus the text-height estimator that catches overflow before rendering |
| `make_charts.py` | Charts, on a brand-derived palette validated for colour-vision separation |
| `make_m0*.py` | Handouts and answer keys per meeting |
| `make_deck_m0*.py` | The four slide files; M02 builds separate student and instructor reveal decks |
| `make_data_m05.py` | Two-week live feed, duplicate-timestamp callback, threshold config, and overnight run log |
| `build_m05.sh` | Standalone M05 build and assembly; does not copy the unmerged M04 dependency |
| `make_kit.py` | The student brand kit and its templates |
| `make_guide.py` | Instructor guide and file index |

Change a number in `make_data.py` and every handout, slide, chart and answer key that
quotes it updates on the next build. Nothing is typed twice.

---

## Fonts

Barlow, Barlow Condensed, Caveat and IBM Plex Mono, all under the
[SIL Open Font License 1.1](tools/teaching-pack/fonts). They are committed so the build
is reproducible and so students can install them from the brand kit.

Slide **body** text is Arial on purpose: it is metric-predictable everywhere, so a
podium machine without the brand fonts still lays out correctly. Only display titles
use Barlow Condensed.

---

## Open decisions

- Exam 2 moving into the finals slot needs registrar approval.
- Which AI assistant students may use live in class.
- Whether the library can license a real standard for M03. `KC-MB-12` is invented so
  students can read all of it and check every claim; the two planted errors port to any
  document with numbered sections and a *shall*.
- Classroom measurement equipment for M02. The lab is written for calipers, works with
  rulers, and falls back to a pre-recorded dataset.
- ENGR 100 content has not been checked against the assumed-on-entry list.

---

*ACMEJOB.Ai, FOREMAN, Diane Halvorsen, Wes Tanaka, the Otter Bend Lift Bridge and
Kinnick County are fictional, invented for this course. Any resemblance to a real firm,
product or structure is coincidental.*
