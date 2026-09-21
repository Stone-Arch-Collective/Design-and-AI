"""M14 exam launch and post-collection reveal with SAY placeholders only."""
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


def add_placeholder_notes(prs, hooks):
    if len(prs.slides) != len(hooks):
        raise ValueError(f"notes ({len(hooks)}) != slides ({len(prs.slides)})")
    for slide, hook in zip(prs.slides, hooks):
        slide.notes_slide.notes_text_frame.text = (
            "M14 SAY HOLD — PLACEHOLDER ONLY — NOT CLOUD-PASS.\n"
            "Do not deliver this text as canon. Replace only from the attached "
            "Cloud-PASS file in a follow-up.\n\n"
            f"RUN-OF-DAY HOOK: {hook}"
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

add_placeholder_notes(prs, [
    "[OPENING / identity check placeholder. State the common-file and 75-minute conditions without adding story detail.]",
    "[MATERIALS / integrity placeholder. Confirm allowed files and how students submit work.]",
    "[SCENARIO boundary placeholder. Name Diane Halvorsen, PE as unreachable only if the Cloud-PASS file does so.]",
    "[TIME checks placeholder. Insert locally approved time announcements; do not coach task content.]",
    "[COLLECTION placeholder. State stop-work, file naming, and collection procedure.]",
])
save(prs, os.path.join(OUT, "M14-exam-launch.pptx"))


# =========================================================== REVEAL ========
rev = deck()
title_slide(
    rev, "Meeting 14  ·  Instructor reveal", "The record changes the call",
    "Open only after every exam is collected",
    "M14 · Exam 1 · Unit 2 close",
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
    ("SAY HOLD", "Speaker language remains empty until a Cloud-PASS file is attached."),
], title="Unit 2 closes on a documented judgment")

add_placeholder_notes(rev, [
    "[POST-COLLECTION opening placeholder. Confirm all exam materials are secured before reveal.]",
    "[REVEAL thesis placeholder. Distinguish a completed machine calculation from an engineering record.]",
    "[SOURCE-check walkthrough placeholder. Invite multiple valid source checks before showing the 1.30 ratio.]",
    "[DESCRIPTIVE-statistics placeholder. Preserve supported rounding and units.]",
    "[INTERVAL walkthrough placeholder. State direct scaling as an exam simplification, not a real rating method.]",
    "[CHART critique placeholder. Accept other consequential critiques grounded in the supplied visual.]",
    "[DECISION comparison placeholder. Keep YES WITH CONDITIONS and NO / HOLD both gradeable.]",
    "[UNIT 2 close placeholder. No later-semester spoilers. Restate that Diane is not the grading key.]",
])
save(rev, os.path.join(OUT, "M14-instructor-reveal.pptx"))
