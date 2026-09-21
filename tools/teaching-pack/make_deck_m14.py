"""M14 exam launch and later-review reveal with Cloud-PASS canon SAY."""
import math
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

OUT = os.path.join(ROOT, "build", "M14")
STRAINS = [156.0, 162.0, 168.0, 171.0, 176.0, 181.0, 185.0, 190.0]
MEAN = statistics.mean(STRAINS)
SD = statistics.stdev(STRAINS)
SE = SD / math.sqrt(len(STRAINS))
MARGIN = 2.365 * SE
FACTOR = 104.0 / 80.0
LOW, HIGH = (MEAN - MARGIN) * FACTOR, (MEAN + MARGIN) * FACTOR


def add_canon_notes(prs, notes):
    if len(prs.slides) != len(notes):
        raise ValueError(f"notes ({len(notes)}) != slides ({len(prs.slides)})")
    for slide, note in zip(prs.slides, notes):
        slide.notes_slide.notes_text_frame.text = (
            "M14 CANON SAY — Cloud PASS.\n"
            "Clock resolution: setup before the timed block; 75 silent-writing minutes; "
            "collect after time. This follows the course and simulation plan and gives "
            "5 more silent minutes than the PASS file's soft 'Exam block 70' label.\n\n"
            + note.strip()
        )


# ========================================================= EXAM LAUNCH =====
prs = deck()
title_slide(
    prs, "Meeting 14  ·  Exam 1", "The permit call",
    "One clean file · one documented recommendation · 75 minutes",
    "Thursday, March 18, 2027  ·  SEIS 201",
)

s, y = content(prs, "Exam conditions", "Same evidence and same clock for every student")
card(s, .72, y + .2, 3.75, 3.75, "USE", [
    "Clean evidence workbook", "FOREMAN recommendation",
    "Exam booklet + reference sheet",
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 4.79, y + .2, 3.75, 3.75, "SHOW", [
    "Source locations", "Calculations + units", "Interval + assumption",
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)
card(s, 8.86, y + .2, 3.75, 3.75, "DECIDE", [
    "Yes", "Yes with conditions", "No",
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

s, y = content(prs, "The decision boundary", "Internal screening—not a legal permit or capacity rating")
speaker_card(s, .72, y + .1, 5.85, 3.75, "KINNICK COUNTY REQUEST", [
    "One 104-kip night crossing", "10 mph", "Center lane"
], body_size=18)
speaker_card(s, 6.72, y + .1, 5.87, 3.75, "FOREMAN", [
    "Recommendation: YES", "Your job: inspect the evidence and record"
], machine=True, body_size=18)

s, y = content(prs, "Suggested clock · 75 minutes", "The clock guides; the five tasks are the exam")
card(s, .72, y + .2, 2.15, 3.6, "0–17", ["Inventory", "Source check"],
     tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=15)
card(s, 2.98, y + .2, 2.15, 3.6, "17–30", ["Center", "Spread"],
     tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=15)
card(s, 5.24, y + .2, 2.15, 3.6, "30–50", ["95% interval", "Load ratio"],
     tint=CREAM, edge=GOLD, label_color=REBAR, body_size=15)
card(s, 7.50, y + .2, 2.15, 3.6, "50–58", ["Chart", "Consequence"],
     tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=15)
card(s, 9.76, y + .2, 2.83, 3.6, "58–75", ["Decision", "Note v2", "Boundary"],
     tint=PEACH, edge=STICKER, label_color=STICKER, body_size=15)

closer(prs, [
    ("HAND IN", "Completed EX1-01 booklet and any attached calculation pages."),
    ("KEEP VISIBLE", "Source, units, spread or interval, assumption, and decision scope."),
    ("GRADING", "Reasoning and record—not agreement with FOREMAN or a character."),
    ("BEGIN", "Open START_HERE in M14-exam-evidence.xlsx."),
], title="Begin Exam 1")

add_canon_notes(prs, [
    "SETUP — SAY: “Exam 1 — overweight permit. Same file for everyone. Diane Halvorsen, PE is unreachable. FOREMAN’s rec is in the packet (orange). Phones away. 75 minutes.” Complete the access check before starting the timed block.",
    "SETUP — Confirm the exam file, FOREMAN recommendation and chart, booklet, and reference sheet. Clarify logistics only—not content. No Wes co-solve and no live Diane.",
    "EXAM CALL — SAY: “Kinnick County Public Works needs a decision today on an overweight permit for a night crossing at the Otter Bend Lift Bridge. FOREMAN recommends approval and says the crossing is fine. You are the human review checkpoint.”",
    "SILENT WORK — 75 timed minutes. Make time calls at about 35 minutes remaining and 10 minutes remaining. Clarify logistics only; do not identify a failed claim, chart flaw, or preferred decision branch.",
    "CLOSE — SAY: “Pens down.” Collect exam-file responses and Note version 2. Do not run a right-answer debrief or open the reveal on exam day.",
])
save(prs, os.path.join(OUT, "M14-exam-launch.pptx"))


# =========================================================== REVEAL ========
rev = deck()
title_slide(
    rev, "Exam 1  ·  Later review only", "The record changes the call",
    "Never open on exam day · use only after release is approved",
    "M14 · Instructor review · Unit 2",
)

statement(
    rev, "FOREMAN checked a number.\nYou checked the basis.",
    "Source · spread · interval · visual · scope",
    dark=True, size=44,
)

s, y = content(rev, "Source check · the ratio is 1.30", "FOREMAN states 25% and calculates with 1.25")
card(s, .72, y + .35, 5.85, 3.25, "SOURCE VALUES", [
    "Requested load = 104 kip", "Test load = 80 kip"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=20)
card(s, 6.72, y + .35, 5.87, 3.25, "CHECK", [
    "104 / 80 = 1.30", "Requested load is 30% above the test load"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=19)

s, y = content(rev, "Test data · center needs spread")
card(s, .72, y + .2, 3.75, 3.75, "CENTER", [
    f"Mean = {MEAN:.1f} µε"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=20)
card(s, 4.79, y + .2, 3.75, 3.75, "SPREAD", [
    f"Sample SD = {SD:.1f} µε", "Range = 34.0 µε"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=18)
card(s, 8.86, y + .2, 3.75, 3.75, "SCOPE", [
    "8 repeated passes", "One control gauge", "One test condition"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

s, y = content(rev, "Scaled interval · close to the trigger")
card(s, .72, y + .2, 5.85, 3.7, "TEST-LOAD 95% INTERVAL", [
    "163.9 to 183.3 µε", f"Mean = {MEAN:.1f} µε"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=20)
card(s, 6.72, y + .2, 5.87, 3.7, "PERMIT-LOAD SCREEN", [
    f"Ratio = {FACTOR:.2f}", f"Scaled interval = {LOW:.1f} to {HIGH:.1f} µε",
    "Instructional trigger = 240 µε",
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=18)

s, y = content(rev, "The chart hides what the decision needs")
card(s, .72, y + .2, 5.85, 3.7, "VISUAL FRAMING", [
    "Axis starts at 200 µε", "Small margin looks decisive"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.7, "MISSING EVIDENCE", [
    "Only the average appears", "No interval", "No one-gauge scope"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)

s, y = content(rev, "More than one call can be defensible")
card(s, .72, y + .2, 5.85, 3.7, "YES WITH CONDITIONS", [
    "Upper bound remains just below the classroom trigger",
    "Retain speed, lane, one-crossing, review / monitoring conditions",
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.7, "NO / HOLD", [
    "Linear scaling is assumed", "Margin is narrow",
    "One gauge does not establish bridge-wide capacity",
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

closer(rev, [
    ("GRADE", "Reasoning, traceability, uncertainty, assumptions, and scope."),
    ("DO NOT GRADE", "Agreement with FOREMAN, Diane, or one preferred final outcome."),
    ("BOUNDARY", "No later-unit methods, callbacks, or Otter Bend outcomes in this reveal."),
    ("CANON", "Cloud-PASS SAY is folded; this deck is reserved for a separate later review."),
], title="Unit 2 closes on a documented judgment")

add_canon_notes(rev, [
    "LATER REVIEW ONLY — Do not open on exam day. Use only in a separately scheduled review after exam materials are secured and release is approved.",
    "REVIEW — SAY: “FOREMAN checked a number. Your exam record checked the source, spread, interval, visual, and scope.” Do not frame this as one correct decision reveal.",
    "SOURCE CHECK — Invite valid source checks before showing the ratio. The permit request gives 104 kip and the test record gives 80 kip; 104 / 80 = 1.30.",
    "SPREAD — Preserve supported rounding and units. Mean alone is not enough; the record needs spread and the one-gauge / one-condition scope.",
    "INTERVAL — Walk the supplied t interval and ratio. State that direct load scaling is an exam simplification, not a real bridge rating method.",
    "CHART — Accept any consequential flaw grounded in the supplied chart. Do not require one phrase when the student explains why the flaw matters to a county reader.",
    "DECISION — Do not crown one branch. YES WITH CONDITIONS and NO / HOLD are both defensible when the record is honest; unconditioned YES is usually weak.",
    "CLOSE — Score the reasoning and record. No M13 answers as free points, no Unit 3 content, and no later Otter Bend outcomes.",
])
save(rev, os.path.join(OUT, "M14-instructor-later-review.pptx"))
