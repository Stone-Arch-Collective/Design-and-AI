"""M13 spoiler-safe student deck and gated silent-ingestion reveal."""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

OUT = os.path.join(ROOT, "build", "M13")
with open(os.path.join(OUT, "M13-pipeline-output.csv"), newline="") as f:
    pipeline = list(csv.DictReader(f))
mm_row = next(row for row in pipeline if row["source_lateral_offset"].endswith("mm"))
source_mm = float(mm_row["source_lateral_offset"].split()[0])
correct_ft = source_mm / 304.8
correct_alignment = 8.0 * correct_ft
correct_model = (
    float(mm_row["raw_strain_microstrain"])
    - float(mm_row["thermal_adjustment_microstrain"])
    + correct_alignment
)


def add_canon_notes(prs, notes):
    if len(prs.slides) != len(notes):
        raise ValueError(f"notes ({len(notes)}) != slides ({len(prs.slides)})")
    for slide, note in zip(prs.slides, notes):
        slide.notes_slide.notes_text_frame.text = (
            "M13 CANON SAY — Cloud hard-review PASS.\n\n" + note.strip()
        )


# ======================================================= STUDENT DECK =======
prs = deck()
title_slide(
    prs, "Meeting 13  ·  Unit 2: Doubt", "Wes’s handoff",
    "Trace what a late, undocumented pipeline does quietly",
    "Tuesday, March 16, 2027  ·  SEIS 201",
)

s, y = content(prs, "Inbox  ·  two days late", "Two of four sheets · assumptions to follow")
speaker_card(s, .72, y + .1, 5.85, 3.75, "WES TANAKA, EIT", [
    "Handoff is late. Two of four sheets.",
    "I’ll finish assumptions later—Diane needs the pipeline tonight.",
], body_size=17)
speaker_card(s, 6.72, y + .1, 5.87, 3.75, "DIANE HALVORSEN, PE · BELIEVER", [
    "Run it.",
    "Otter Bend cannot wait on a perfect notebook.",
], body_size=18)

s, y = content(prs, "The side file is not today’s hunt", "Liability context stays in the inbox")
card(s, .72, y + .25, 11.87, 3.45, "ON DIANE’S DESK", [
    "Mechanical inspector note: bearing wear that FOREMAN rated fine at M07.",
    "Wes’s earlier accept-memo is attached.",
    "Do not analyze that memo today. Trace the handoff in front of you.",
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=18)

s, y = content(prs, "Today’s clock", "A deliberate extended Unit 2 close")
card(s, .72, y + .2, 2.15, 3.6, "INBOX · 10", ["Late handoff", "Ship pressure"],
     tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=15)
card(s, 2.98, y + .2, 2.15, 3.6, "TEACH · 25", ["Pipeline", "Ingestion"],
     tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=15)
card(s, 5.24, y + .2, 2.15, 3.6, "LAB · 30", ["Trace one", "Commit"],
     tint=CREAM, edge=GOLD, label_color=REBAR, body_size=15)
card(s, 7.50, y + .2, 2.15, 3.6, "NOTE · 10", ["Note v2", "Unchecked log"],
     tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=15)
card(s, 9.76, y + .2, 2.83, 3.6, "DEBRIEF 15 · CLOSE 5", ["Mask off", "Then close"],
     tint=PEACH, edge=STICKER, label_color=STICKER, body_size=14)

section(prs, "1", "What enters a pipeline?",
        "A completed run can still hide undocumented decisions")

s, y = content(prs, "A pipeline is a chain of decisions")
card(s, .72, y + .2, 2.75, 3.7, "INGEST", ["Read files", "Apply schema"],
     tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 3.68, y + .2, 2.75, 3.7, "CLEAN / JOIN", ["Retain", "Change", "Remove"],
     tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)
card(s, 6.64, y + .2, 2.75, 3.7, "TRANSFORM", ["Calculate", "Map units"],
     tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 9.60, y + .2, 2.99, 3.7, "DELIVER", ["Model input", "Decision output"],
     tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

s, y = content(prs, "Ingestion is where assumptions become behavior")
card(s, .72, y + .2, 5.85, 3.75, "VISIBLE INGESTION", [
    "Source and row count", "Schema and units", "Parse failures and exceptions"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.75, "QUIET INGESTION", [
    "Defaults substitute for questions", "Rows change count without a reason",
    "A completed status hides the decision"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

s, y = content(prs, "Cleaning is not neutral")
card(s, .72, y + .2, 3.75, 3.75, "KEEP", [
    "What qualifies?", "What remains uncertain?"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 4.79, y + .2, 3.75, 3.75, "CHANGE", [
    "What formula?", "What input and output units?"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)
card(s, 8.86, y + .2, 3.75, 3.75, "REMOVE", [
    "Which records?", "Where is the exception record?"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

s, y = content(prs, "An early error compounds")
card(s, .72, y + .2, 5.85, 3.75, "EARLY STAGE", [
    "A field is parsed", "A default is applied", "A row enters or leaves"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.75, "DOWNSTREAM", [
    "The transformed field looks official", "The consumer receives no original context",
    "The final claim inherits the first decision"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)

section(prs, "2", "Trace one value",
        "Do not audit everything badly; audit one path honestly")

activity(prs, "Open the handoff", 5, [
    "Open wes_handoff.xlsx and count the delivered sheets.",
    "Inventory fields, units, formats, row counts, and missing timestamps.",
    "Open FOREMAN’s pipeline log and output CSV.",
    "Do not begin with the final number—choose one source record.",
], note="Wes Tanaka, EIT does not co-solve. Use the files.")

activity(prs, "Trace one record end to end", 20, [
    "Copy its source value and timestamp into H13-01.",
    "Follow parse, join, adjustment, and model-input fields.",
    "Reconcile record counts at every stage.",
    "Mark each point where the system asks, flags, defaults, or stays quiet.",
], note="Keep the reveal closed. The files—not this slide—contain the hunt.")

activity(prs, "Show how the difference grows", 5, [
    "Recompute your chosen path using the source representation.",
    "Compare that path with the emitted model input.",
    "Name the earliest stage where a human checkpoint belongs.",
    "Commit your trace before discussion.",
], note="The downstream consumer is familiar from M08; do not re-teach it.")

s, y = content(prs, "Write Unit 2 Note v2", "Claim · check · result · unchecked log")
card(s, .72, y + .2, 2.75, 3.7, "CLAIM", [
    "What does FOREMAN’s completed run imply?"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)
card(s, 3.68, y + .2, 2.75, 3.7, "CHECK", [
    "Which record and stages did you trace?"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.64, y + .2, 2.75, 3.7, "RESULT", [
    "What broke, in your own words?"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)
card(s, 9.60, y + .2, 2.99, 3.7, "UNCHECKED", [
    "List columns you did not review."
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)

section(prs, "3", "Unit 2 debrief",
        "Mask off · compare choices, not character approval")

s, y = content(prs, "What changed across Unit 2?")
card(s, .72, y + .2, 2.75, 3.7, "CLAIMS", [
    "What evidence sits behind confidence?"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 3.68, y + .2, 2.75, 3.7, "REVIEW", [
    "Where must a human checkpoint stop the path?"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)
card(s, 6.64, y + .2, 2.75, 3.7, "CHARTS", [
    "What does a public display make look certain?"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 9.60, y + .2, 2.99, 3.7, "PIPELINES", [
    "What became invisible between source and output?"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

closer(prs, [
    ("HAND IN", "H13-01 trace and H13-03 Note v2 with unchecked-column log."),
    ("RECORD", "What you checked, what you did not, and where the path should stop."),
    ("OWNERSHIP", "Wes owns the handoff; Diane owns ship pressure; you own your review record."),
    ("CLOSE", "A pipeline can run tonight and still be wrong at ingestion."),
], title="The run status is not the engineering answer")

add_canon_notes(prs, [
    "TITLE — SAY: “Wes’s handoff is late and incomplete. Today you will trace what happens when a pipeline keeps moving without asking.”",
    "INBOX 10 — Wes Tanaka, EIT: “Handoff is late. Two of four sheets. I’ll finish assumptions later—Diane needs the pipeline tonight.” Diane Halvorsen, PE, BELIEVER: “Run it. Otter Bend cannot wait on a perfect notebook.” Attach wes_handoff.xlsx and the orange FOREMAN pipeline log.",
    "INBOX COLOR — SAY: “A mechanical inspector note is on Diane’s desk: bearing wear FOREMAN rated fine at M07, with Wes’s earlier accept-memo attached. That is liability context for Wes—not today’s hunt. Do not turn this into a memo-return exercise.”",
    "CLOCK — SAY: “Pack clock: Inbox 10, Teach 25, Lab 30, Note 10, Unit 2 debrief 15, Closing 5. Keep the debrief as its own beat after Lab and Note.”",
    "TEACH TRANSITION — SAY: “The downstream consumer is the simple temperature-correction model you already know. We are not re-teaching M08. We are checking what reaches it.”",
    "TEACH — SAY: “A pipeline is a sequence of decisions: ingest, clean or join, transform, and deliver. Each stage needs a visible record of what changed.”",
    "TEACH — SAY: “Ingestion is where a file becomes a schema. Defaults are decisions. A successful parse is not proof that the source meant what the schema assumed.”",
    "TEACH — SAY: “Cleaning includes keeping, changing, and removing data. Removing a record without a flag is still a decision.”",
    "TEACH — SAY: “An early mismatch can become a clean-looking downstream field. The consumer sees the transformed number, not the missing context.”",
    "LAB TRANSITION — SAY: “Do not audit everything badly. Choose one source record and audit its path honestly.”",
    "LAB 30 — SAY: “Open the workbook, FOREMAN log, and pipeline output. Pick one value. Trace it from source through ingestion, cleaning, adjustment, and output.”",
    "LAB — SAY: “At each step ask: did the path stay honest about flags, units, and formats, or did it keep going quietly? Would a careful engineer have stopped to ask?”",
    "LAB — SAY: “Recompute your chosen path from the source representation. Show where the difference first appears and how it changes downstream. Commit before Reveal.”",
    "NOTE 10 — SAY: “Write Note version 2: what you traced, what broke in your own words, and a short log of columns left unchecked. Silent ingestion is still a choice—the machine just never asks.”",
    "DEBRIEF 15 — MASK OFF. SAY: “Compare what you chose to verify and why. Unit 2 has moved from model claims to human review, charts, and pipelines. Diane is not the grading key.” Do not preview M14.",
    "DEBRIEF — ASK: “Where did a confident output hide a choice about evidence? What should a human checkpoint make visible before work continues?”",
    "CLOSING 5 — SAY: “The pipeline can run tonight and still be wrong if nobody stops it at ingestion. Wes Tanaka, EIT owns the messy handoff; Diane Halvorsen, PE owns the pressure to ship; you own the record of what you checked and what you did not.”",
])
save(prs, os.path.join(OUT, "M13-student.pptx"))


# ======================================================== REVEAL DECK =======
rev = deck()
title_slide(
    rev, "Meeting 13  ·  Instructor reveal", "Silent ingestion",
    "Open only after students commit one end-to-end trace",
    "M13 · Unit 2: Doubt",
)

statement(
    rev, "FOREMAN never stopped to ask.",
    "A COMPLETE run can preserve every hidden assumption.",
    dark=True, size=46,
)

s, y = content(rev, "The row count changes without an exception record")
card(s, .72, y + .35, 5.85, 3.25, "SOURCE", [
    "12 sensor records", "10 weather records"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=21)
card(s, 6.72, y + .35, 5.87, 3.25, "EMITTED", [
    "10 joined model records", "Status: COMPLETE", "No operator question"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=19)

s, y = content(rev, "One field carries more than one unit")
card(s, .72, y + .35, 5.85, 3.25, "SOURCE COLUMN", [
    "lateral_offset includes feet and millimetres",
    f"Worked record: {mm_row['record_id']} = {mm_row['source_lateral_offset']}",
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
card(s, 6.72, y + .35, 5.87, 3.25, "INGESTION DEFAULT", [
    "Numeric token extracted", "Every value assigned schema_unit = ft",
    "No unit exception generated"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=18)

s, y = content(rev, f"Worked trace · {mm_row['record_id']}")
card(s, .72, y + .2, 5.85, 3.7, "FOREMAN PATH", [
    f"Offset = {float(mm_row['parsed_offset']):.3f} ft",
    f"Alignment adjustment = {float(mm_row['alignment_adjustment_microstrain']):.2f} µε",
    f"Model input = {float(mm_row['model_input_microstrain']):.2f} µε",
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.7, "UNIT-AWARE PATH", [
    f"Offset = {correct_ft:.4f} ft",
    f"Alignment adjustment = {correct_alignment:.2f} µε",
    f"Model input = {correct_model:.2f} µε",
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)

s, y = content(rev, "The human and machine failures rhyme")
card(s, .72, y + .2, 5.85, 3.7, "WES’S HANDOFF", [
    "Late", "Two promised sheets absent", "Assumptions undocumented"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.7, "FOREMAN’S INGESTION", [
    "Defaults replace questions", "Rows disappear quietly", "Run status says COMPLETE"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=18)

s, y = content(rev, "A bounded review record is the deliverable")
speaker_card(s, .72, y + .15, 11.87, 3.2, "MODEL NOTE v2 · NOT REQUIRED WORDING", [
    f"I traced {mm_row['record_id']} through source, parse, join, adjustments, and output.",
    "The path should stop at ingestion because source records disappear without an exception "
    "record and a mixed-unit value is processed under one default unit.",
    "I did not review every field; the unchecked fields are logged separately.",
], body_size=17)

closer(rev, [
    ("REVEAL", "Silent ingestion: FOREMAN never stops to ask."),
    ("DEBRIEF", "Run the full 15-minute mask-off beat after Note."),
    ("STORY", "M07 liability color stays in the inbox; Wes does not co-solve."),
    ("SPOILER GUARD", "Do not introduce any M14 overweight-permit details."),
], title="Close Unit 2 without erasing the record")

add_canon_notes(rev, [
    "REVEAL — Open only after students commit H13-01. SAY: “FOREMAN’s designed error is silent ingestion. It never stops to ask.”",
    "REVEAL — SAY: “A complete run is not an honest run. The status only says that the configured steps executed.”",
    "REVEAL — SAY: “Twelve sensor records entered, ten weather records existed, and ten model records emerged. The inner join removed unmatched source records without an exception record.”",
    "REVEAL — SAY: “The source field mixes feet and millimetres. FOREMAN extracts the numeric token and applies a default-foot schema to every row.”",
    f"REVEAL — SAY: “For {mm_row['record_id']}, FOREMAN treats {mm_row['source_lateral_offset']} as {float(mm_row['parsed_offset']):.3f} feet. The unit-aware path converts it to {correct_ft:.4f} feet. The difference grows in the adjustment and reaches the downstream model input.”",
    "REVEAL — SAY: “Wes’s thin handoff and FOREMAN’s silent ingestion share one failure mode: undocumented assumptions continue downstream. Keep the M07 memo/bearing-wear item as liability color only.”",
    "NOTE — SAY: “A complete audit is not required. An honest trace plus an unchecked-column log is required. Grade the record, not agreement with Diane’s schedule pressure.”",
    "CLOSE — SAY: “After this reveal, run the separate Unit 2 debrief. Do not preview the M14 exam scenario. Close on ownership: handoff, ship pressure, and review record.”",
])
save(rev, os.path.join(OUT, "M13-instructor-reveal.pptx"))
