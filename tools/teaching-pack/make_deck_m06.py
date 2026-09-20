"""M06 spoiler-safe student deck and gated instructor reveal."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

OUT = os.path.join(ROOT, "build", "M06")


def add_notes(prs, notes):
    if len(prs.slides) != len(notes):
        raise ValueError(f"notes ({len(notes)}) != slides ({len(prs.slides)})")
    for slide, note in zip(prs.slides, notes):
        slide.notes_slide.notes_text_frame.text = note.strip()


# ======================================================= STUDENT DECK =======
prs = deck()
title_slide(prs, "Meeting 06  ·  Unit 1: Hired", "Real—or an outlier?",
            "Audit FOREMAN's reversal, close Unit 1, hand the file to Wes",
            "Thursday, February 18, 2027  ·  SEIS 201")

s, y = content(prs, "FOREMAN has reversed itself", "Tuesday: close it. Thursday: delete it.")
speaker_card(s, .72, y + .2, 11.87, 2.15, "FOREMAN v4.2 — FINAL DISPOSITION", [
    "“Daily peak strain is normally distributed. The 286.1 µε value is more than five "
    "standard deviations from normal operation. Discard it as a sensor fault.”"
], machine=True, body_size=21)
speaker_card(s, .72, y + 2.75, 11.87, 1.5, "DIANE HALVORSEN, PE", [
    "“It cannot be an emergency Tuesday and bad data Thursday just because both answers are decisive.”"
], body_size=16)

s, y = content(prs, "The hunt", "Audit the claim, the data path, and the independent record")
card(s, .72, y + .2, 3.75, 3.6, "1  DISTRIBUTION", [
    "What is the unit of analysis?", "What shape do the daily peaks have?",
    "Is a normal model justified?"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 4.79, y + .2, 3.75, 3.6, "2  PIPELINE", [
    "Did correction, averaging, or duplication create the 03:00 value?"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)
card(s, 8.86, y + .2, 3.75, 3.6, "3  EVENT RECORD", [
    "What independent record can test whether something crossed at the same time?"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

section(prs, "1", "Describe the distribution first",
        "The model is a claim about shape, not a default setting")

s, y = content(prs, "A distribution connects values to frequency",
               "Choose the observational unit before making the histogram")
bullet_list(s, .95, y + .2, 11.4, 3.55, [
    ("Gauge row  ", "one sensor at one timestamp."),
    ("Timestamp maximum  ", "the largest corrected reading across eight gauges."),
    ("Daily peak  ", "one selected maximum per day—the population FOREMAN says it modeled."),
    ("Consequence  ", "changing the unit changes the shape, sample size, and meaning."),
], size=19, dot=GIRDER_LT)
card(s, .72, y + 3.75, 11.87, 1.3, "AUDIT QUESTION", [
    "Which population supports the claim FOREMAN actually made?"
], tint=CREAM, edge=GOLD, body_size=13)

s, y = content(prs, "Normal and skewed are shapes—not verdicts")
card(s, .72, y + .2, 5.85, 3.8, "NORMAL", [
    "Symmetric around a centre", "Mean and median align", "Two tails of similar form",
    "A model to justify—not assume"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.8, "RIGHT-SKEWED", [
    "Most values cluster lower", "A long tail reaches higher values",
    "Heavy crossings can create rare high strain", "Mean is pulled toward the tail"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

statement(prs, "An outlier is unusual in a distribution.\nIt is not automatically an error.",
          "Statistical description ≠ physical diagnosis", dark=True, size=43)

s, y = content(prs, "Pipeline artifact is a causal claim",
               "Show the operation that created or corrupted the value")
bullet_list(s, .95, y + .2, 11.4, 3.8, [
    ("Source row  ", "Does 286.1 µε exist in the corrected feed?"),
    ("Transformation  ", "Did baseline correction or the 10-minute window create it?"),
    ("Duplication  ", "Does the known repeated block touch this timestamp or change the daily maximum?"),
    ("Cross-sensor pattern  ", "Do neighbouring gauges move at the same time?"),
    ("Independent record  ", "Does another system record an event at that timestamp?"),
], size=18, dot=STICKER)

section(prs, "2", "Audit the whole reasoning chain",
        "Unusual → error → delete contains two unsupported arrows until evidence earns them")

activity(prs, "Build the daily-peak histogram", 12, [
    "Open M06-gauge-audit-and-handoff.xlsx and use the Daily peaks sheet.",
    "Plot daily_peak_corrected_microstrain as a histogram.",
    "Describe centre, spread, shape, and any unusual values without deleting a row.",
    "Write whether the histogram supports FOREMAN's normal-distribution assumption.",
], note="Do not diagnose the cause from the histogram.")

activity(prs, "Trace the 03:00 value through the pipeline", 10, [
    "Use the 03-00 event sheet and the M05 feed, run log, and threshold configuration.",
    "Check whether all gauges, only G6, or no neighbours move at 03:00.",
    "Locate the duplicated timestamp block from HW3. Does it touch this event?",
    "Mark each claim: supported, unsupported, or unresolved.",
], note="A known data problem is not evidence that every unusual value is bad.")

activity(prs, "Open the independent record", 8, [
    "Open traffic_counts.csv and filter to the alarm window.",
    "Align its timestamp with the gauge spreadsheet. Record the matching row, if any.",
    "State what temporal alignment supports—and what it still cannot prove.",
    "Choose retain, quarantine, or remove. Give the evidence and next check.",
], note="The decision and its limits go in H6-03 before any reveal.")

closer(prs, [
    ("HAND IN", "H6-02 audit and H6-03 decision log / Unit 1 debrief."),
    ("COMPLETE", "The Wes handoff sheet inside the workbook and H6-04 cover record."),
    ("HAND OFF", "Give the gauge spreadsheet to Wes with checked and unchecked items visible."),
    ("REMEMBER", "Diane's reaction is not your grade. Your evidence trail is."),
], title="Close Unit 1")

student_notes = [
    "SAY: “Today we decide whether the alarm evidence was real, an outlier, or a pipeline artifact. At the end, this file leaves your desk.” Keep the reveal deck closed.",
    "SAY: “FOREMAN changed from emergency to deletion. Confidence did not make either chain complete.” Hand out H6-01.",
    "SAY: “Three hunts, three kinds of evidence. Do not let an unusual value become a sensor fault by vocabulary alone.”",
    "SAY: “Before computing anything, name the distribution FOREMAN says it used.”",
    "SAY: “A histogram answers a question about the unit you counted. Rows, timestamp maxima, and daily peaks are different populations.”",
    "SAY: “Normality is not the spreadsheet default. Describe visible shape before choosing a model.”",
    "SAY: “Outlier names a relationship to the rest of a set. It does not tell us truck, fault, or danger.”",
    "SAY: “To call this a pipeline artifact, point to the transformation that produced it.”",
    "SAY: “FOREMAN's chain contains arrows. Our job is to test every arrow, not just the first number.”",
    "SAY: “Keep every row while plotting. Describe first; decide later.” Circulate without confirming the shape.",
    "SAY: “The duplicate block is real. Test whether it is relevant to this timestamp instead of using it as a general reason to distrust the feed.”",
    "SAY: “The independent file is now available. Match timestamps, then state the boundary of what a match proves.” Do not announce the matching row.",
    "SAY: “Write first. Then complete the cover record and physically hand the workbook to Wes.” Collect decisions before opening the reveal.",
]
add_notes(prs, student_notes)
save(prs, os.path.join(OUT, "M06-student.pptx"))


# ======================================================== REVEAL DECK =======
rev = deck()
title_slide(rev, "Meeting 06  ·  Instructor reveal", "What the records support.",
            "Open only after students submit the audit decision",
            "M06 · Unit 1 close")

s, y = content(rev, "The selected daily peaks are strongly right-tailed",
               "15 days · median 110.7 µε · range 104.0–286.1 µε")
card(s, .72, y + .2, 5.85, 3.4, "WHAT THE HISTOGRAM SHOWS", [
    "Most daily peaks cluster near 104–121 µε.", "One extreme event extends the right tail.",
    "The small set of selected maxima does not justify FOREMAN's normal model."
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.4, "WHAT IT DOES NOT SHOW", [
    "The physical cause", "Whether the bridge was unsafe", "Whether the sensor failed"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)

s, y = content(rev, "The duplicate block is real—and irrelevant to 03:00",
               "February 12, 14:00–15:00 ≠ February 16, 03:00")
speaker_card(s, .72, y + .2, 11.87, 1.7, "PIPELINE AUDIT", [
    "The duplicate payload changes row counts. It does not create, repeat, or alter the alarm event or its daily peak."
], body_size=18)
card(s, .72, y + 2.15, 11.87, 1.65, "LESSON", [
    "Finding one pipeline defect does not license deleting a different unusual value."
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=19)

s, y = content(rev, "The independent record aligns at 03:00",
               "Kinnick County bridge traffic counter")
table_slide_rows = [
    ["Timestamp", "Direction", "Class", "Axles", "Estimated gross weight"],
    ["2027-02-16 03:00", "EB", "5-axle heavy vehicle", "5", "79,400 lb"],
]
gt = s.shapes.add_table(2, 5, Inches(.72), Inches(y + .35), Inches(11.87), Inches(1.35)).table
widths = [2.25, 1.25, 3.65, 1.0, 3.72]
for ci, width in enumerate(widths):
    gt.columns[ci].width = Inches(width)
for ri, row in enumerate(table_slide_rows):
    for ci, value in enumerate(row):
        c = gt.cell(ri, ci); c.fill.solid()
        c.fill.fore_color.rgb = GIRDER if ri == 0 else CREAM
        p = c.text_frame.paragraphs[0]; r = p.add_run(); r.text = value
        r.font.name = DISPLAY if ri == 0 else BODY; r.font.size = Pt(14)
        r.font.bold = ri == 0; r.font.color.rgb = WHITE if ri == 0 else REBAR
card(s, .72, y + 2.15, 11.87, 1.65, "BOUNDARY", [
    "Timestamp alignment and the cross-gauge response support retaining the event. They do not alone establish safety or prove a load-response mechanism."
], tint=PAPER, edge=CONCRETE, body_size=16)

statement(rev, "Tuesday overreacted.\nThursday overcorrected.",
          "A real event still needs a bounded engineering disposition.", dark=True, size=48)

s, y = content(rev, "A defensible record keeps the event and its limits")
speaker_card(s, .72, y + .2, 11.87, 3.15, "MODEL DECISION — NOT THE ONLY FULL-CREDIT WORDING", [
    "“I retained and annotated the 03:00 reading because it appears in the corrected feed, "
    "all gauges rise at the same timestamp, and the traffic counter records a heavy vehicle "
    "then. The duplicate block occurs on a different day. This supports a real event, not by "
    "itself a safety disposition; next I would verify the vehicle estimate and bridge response.”"
], body_size=17)

s, y = content(rev, "Unit 1 · mask off", "Compare verification choices, not character approval")
bullet_list(s, .95, y + .2, 11.4, 3.7, [
    ("M01  ", "A traceable rule and a learned pattern answer different questions."),
    ("M02  ", "Averages can hide measurement problems."),
    ("M03  ", "Fluent citations still require the source."),
    ("M04  ", "A mean can hide the spread."),
    ("M05–M06  ", "Audit every agent handoff; unusual is not the same as wrong."),
], size=18, dot=GIRDER_LT)

closer(rev, [
    ("LOG", "Collect the decision and what remained unchecked."),
    ("COVER", "Students complete H6-04 and the workbook Wes handoff sheet."),
    ("HAND OFF", "Each student gives the February gauge workbook to Wes."),
    ("INSTRUCTOR", "Preserve the submitted file unchanged. Do not announce its later return."),
], title="The file leaves their desk")

reveal_notes = [
    "SAY: “Now we compare what the evidence supports. This is the reveal, not a reward for choosing Diane's preference.”",
    "SAY: “The shape is right-tailed, and there are only 15 selected maxima. FOREMAN's normal assumption is not earned.”",
    "SAY: “The duplicated timestamps matter for later analyses, but they occur on another day. A real defect is not a universal explanation.”",
    "SAY: “The traffic counter aligns with the gauge event. That is independent corroboration, not a complete safety analysis.”",
    "SAY: “Tuesday, FOREMAN jumped from warning to closure. Thursday, it jumped from unusual to fault. Both skipped evidence.”",
    "SAY: “Full credit follows the trace and limits. Retain or quarantine can be defensible; unsupported deletion cannot.”",
    "SAY: “Mask off. Which check changed your wording? Which did you not buy with your project hours?”",
    "SAY: “Complete the handoff now. The receiving engineer needs the unchecked items as much as the chart.” Preserve student files; do not mention M25.",
]
add_notes(rev, reveal_notes)
save(rev, os.path.join(OUT, "M06-instructor-reveal.pptx"))
