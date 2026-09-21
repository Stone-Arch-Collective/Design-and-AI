# SEIS 201 M13 — Wes's handoff

**SEIS 201 M13 — Wes's handoff**

## Story Spine (6-8 beats)

1. Wes Tanaka, EIT’s handoff lands two days late: only two of four sheets, mixed units in one column, no assumptions written down.
2. Students open `wes_handoff.xlsx` and FOREMAN’s pipeline log. The downstream consumer is the simple temperature-correction model from M08 — do not re-teach M08.
3. Diane Halvorsen, PE is BELIEVER: the Otter Bend pipeline has to run tonight.
4. Side color (not the main hunt): the mechanical inspector found bearing wear FOREMAN rated fine at M07; Wes’s earlier accept-memo liability color is back on Diane’s desk. Burn on Wes, not on students. Do not turn class into “the M07 memo returns.”
5. Teach: pipelines, ingestion, unit/format mismatch, cleaning, missing data, how errors grow step to step.
6. Lab hunt: trace **one** value from ingestion to output. Find silent drops and unit misreads without being told which. FOREMAN’s designed error is silent ingestion — it never stops to ask.
7. Hand in note version 2: not enough time for all four columns — choose what you checked and log what you left unchecked.
8. Last ~15 minutes: Unit 2 debrief, mask off (own beat after Lab/Note).

## Student Hunt

Open `wes_handoff.xlsx` and the FOREMAN pipeline log. Pick **one** value and trace it from ingestion through cleaning to the model output. At each step ask: Did the path stay honest — flags, units, formats — or did it keep going quietly? Would a careful engineer have stopped to ask? Diane Halvorsen, PE wants the pipeline to run tonight — your job is still to see what the silent path does to the numbers. Wes Tanaka, EIT does not co-solve. Log which columns you did not have time to check.

## Instructor Reveal (after hunt)

FOREMAN’s designed error: **silent ingestion**. It never stops to ask.

After the hunt, name what students should have caught by tracing:

1. Rows with **missing temperatures** were **dropped without a word**.
2. **Millimetres were read as feet** in a mixed-unit column — the error grows at each downstream step into the temperature-correction consumer.

Wes Tanaka, EIT’s thin handoff (late, incomplete sheets, no assumptions) is the human side of the same failure mode. The M07 bearing-wear / accept-memo color on Diane Halvorsen, PE’s desk is liability flavor for Wes — not a second student hunt.

## SAY Beats

### Inbox 10

- Wes Tanaka, EIT (thin/defensive): “Handoff is late. Two of four sheets. I’ll finish assumptions later — Diane needs the pipeline tonight.”
- Attachments: `wes_handoff.xlsx`, FOREMAN pipeline log (orange).
- Diane Halvorsen, PE (BELIEVER): “Run it. Otter Bend cannot wait on a perfect notebook.”
- Side color (inbox only, not the hunt): mechanical inspector note — bearing wear FOREMAN called fine at M07; Wes’s earlier accept-memo is back on Diane’s desk.

### Teach 25

- Data pipeline and ingestion: what enters, what is assumed, what is logged.
- Unit and format mismatch: mixed feet/mm (or similar) in one column is a classic silent killer.
- Data cleaning and missing/bad data: dropping rows without a flag is still a decision.
- Errors through a pipeline: a small misread early becomes a wrong model input later (M08-style consumer — do not re-teach M08).
- Canon: Diane Halvorsen, PE; Wes Tanaka, EIT; Otter Bend; FOREMAN (orange = machine).
- Save silent-drop and mm-as-feet for Reveal — do not print them as hunt answers on the student deck.

### Lab 30

- Materials: `wes_handoff.xlsx`, FOREMAN pipeline log.
- Trace **one** value end to end. Mark where the path goes quiet (no ask, no flag).
- Show how the error grows at each step into the downstream model input.
- Time box: you will not finish all four columns — choose, then start the unchecked log for Note.

### Note 10

- Hand in **note version 2**: what you traced, what broke (in your own words), and a short log of **columns left unchecked**.
- One-liner: silent ingestion is still a choice — FOREMAN just never asks.

### Unit 2 debrief 15

- Own beat **after** Lab/Note — not inside Lab.
- Mask off: Unit 2 themes in plain language (agent claims, human review, charts, pipelines). No M14 overweight-permit spoilers.

### Closing 5

The pipeline can run tonight and still be wrong if nobody stops it at ingestion. Wes Tanaka, EIT owns the messy handoff; Diane Halvorsen, PE owns the pressure to ship; students own the record of what they checked and what they did not.

## Spoiler Guard

Student decks and Hunt: do not name “mm as feet” or “silent drop of missing temps” as the answer — students discover by tracing. Diane stays BELIEVER. Wes does not co-solve. M07 memo/bearing wear stays side liability color — do not rewrite M13 as memo-return. No M14 overweight-permit spoilers (night crossing, Diane unreachable, FOREMAN says fine, etc.). Designed errors live in Reveal (and light Inbox orange), not as Hunt spoilers.

## Pack notes (for CB)

- Fold this SAY into Design-and-AI **after Cloud PASS only**.
- Assets: `wes_handoff.xlsx` (two of four sheets usable; mixed feet/mm column; missing temps); FOREMAN pipeline log showing silent drops and unit misread into the M08-style consumer.
- Hand-in: note version 2 with unchecked-column log.
- Clock: Teach 25 → Lab 30 → Note 10 → Unit 2 debrief 15 (own beat) → Closing 5.
- Diane = believer. Do not start M14 exam pack from this fold until Shannon directs.
