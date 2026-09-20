"""M06 student handouts, instructor key, and generated file index."""
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M06")


def lines(doc, count=3):
    for _ in range(count):
        p = para(doc, "", after=10, before=2)
        bottom_rule(p, "C9CFD6", 6)


# ============================================================ H6-01 =========
d = foreman_doc("Alarm Disposition Review — Final",
                generated="2027-02-18 07:42 CST")
callout(d, "FINAL DISPOSITION",
        "Discard the 03:00 G6 reading as a sensor fault. No bridge action is required.",
        fill="FFF1E8", edge="F26B1D")
h2(d, "Automated analysis", color=REBAR)
bullets(d, [
    "Daily peak corrected strain is normally distributed.",
    "The 286.1 µε reading is more than five standard deviations from normal operation.",
    "Values this unlikely are outliers and should be removed before reporting.",
    "The overnight alarm was therefore false and the closure draft may be closed.",
])
h2(d, "Method record", color=REBAR)
table(d, [
    ["Step", "FOREMAN record"],
    ["Population", "Daily maximum corrected strain, February 2–16"],
    ["Model", "Normal distribution"],
    ["Outlier rule", "Remove values more than five standard deviations from normal"],
    ["Independent event record", "Not queried"],
    ["Pipeline audit", "Duplicate-timestamp block removed before daily maxima"],
], widths=[2.0, 4.9], head_fill="2B2F36")
mono_block(d, [
    "fm-run-27114-0218  |  confidence 99%  |  status FINAL",
    "AUTOMATED OUTPUT  |  DISTRIBUTION ASSUMPTION NOT REVIEWED",
])
save(d, os.path.join(OUT, "H6-01-FOREMAN-alarm-disposition.docx"))


# ============================================================ H6-02 =========
d = course_doc("M06", "Real, Outlier, or Pipeline Artifact?", kind="AUDIT WORKSHEET")
para(d, "FOREMAN has reversed itself: Tuesday it recommended closure; Thursday it says delete "
        "the reading. Audit the reasoning before accepting either disposition.", after=8)
callout(d, "Keep three claims separate",
        "A row can be unusual and still be real. “Outlier” describes its relationship to other "
        "values; it does not identify a cause. A pipeline artifact must be demonstrated in the "
        "data path.", fill="EEF3F8", edge="6F8FAF")
h2(d, "A — Reproduce the evidence")
table(d, [
    ["Question", "File / field / result"],
    ["What is the unit of analysis: every gauge row, each timestamp, or each day's peak?", ""],
    ["How many daily peaks are in the spreadsheet?", ""],
    ["What shape does the histogram suggest? Cite visible features.", ""],
    ["Does the duplicate block alter the 03:00 event or its daily peak?", ""],
    ["What happened in the independent traffic record at 03:00?", ""],
], widths=[4.45, 2.45], size=8.7, zebra=None)
h2(d, "B — Audit FOREMAN's chain")
table(d, [
    ["FOREMAN step", "Supported?", "Evidence and correction"],
    ["Choose daily peaks", "", ""],
    ["Assume a normal distribution", "", ""],
    ["Call 286.1 µε an outlier", "", ""],
    ["Translate outlier → sensor fault", "", ""],
    ["Discard the row", "", ""],
    ["Close the physical-event question", "", ""],
], widths=[2.5, 1.05, 3.35], size=8.5, zebra=None)
h2(d, "C — Decision")
para(d, "Write a bounded disposition: keep / remove / quarantine the reading; what the files "
        "support; what they do not prove; and the next engineering check.", size=9.5)
lines(d, 5)
save(d, os.path.join(OUT, "H6-02-distribution-and-chain-audit.docx"))


# ============================================================ H6-03 =========
d = course_doc("M06", "Decision Log + Unit 1 Debrief", kind="HAND-IN")
para(d, "Log the decision you can defend today. Project hours shape what you checked; they are "
        "not grade points. The instructor grades the reasoning and record, not the outcome.",
     after=8)
h2(d, "Decision log")
table(d, [
    ["Item", "Action chosen", "Hours", "Evidence checked", "Accepted unverified"],
    ["M06 alarm disposition", "", "", "", ""],
], widths=[1.35, 1.45, .55, 1.85, 1.7], size=8.2, zebra=None)
h2(d, "Note v1 — one sentence")
para(d, "State what you checked the alarm disposition against. Name the files, not FOREMAN's "
        "confidence.", size=9.3)
lines(d, 2)
h2(d, "Unit 1 mask-off")
numbers(d, [
    "Which verification choice changed your conclusion or narrowed your language?",
    "What did you leave unchecked because of the hour budget?",
    "Where did FOREMAN calculate correctly but reason beyond its evidence?",
    "What will the next engineer need so they do not have to reconstruct your work?",
], size=9.5)
callout(d, "Assessment boundary",
        "Diane is a character, not the grader. A defensible keep, quarantine, or remove decision "
        "can earn full credit when its evidence and limits are explicit.",
        fill="FFF6E5", edge="F2C230")
save(d, os.path.join(OUT, "H6-03-decision-log-and-unit-debrief.docx"))


# ============================================================ H6-04 =========
d = acme_doc(subtitle="Internal Data Handoff")
memo_block(d, to="Wes Tanaka, EIT", frm="Student file owner",
           date="Thursday, February 18, 2027",
           re_="Otter Bend gauge audit spreadsheet")
para(d, "I am handing off M06-gauge-audit-and-handoff.xlsx for the next project stage. "
        "This cover sheet travels with the file; a clean-looking spreadsheet without its "
        "limits is not a complete handoff.", after=8)
h2(d, "Required before release")
table(d, [
    ["Record", "Student entry"],
    ["Exact filename and version", ""],
    ["Source files used", ""],
    ["Transformations performed", ""],
    ["Checks completed", ""],
    ["Known issue: duplicate timestamps", ""],
    ["Rows retained, removed, or quarantined—and why", ""],
    ["Items not checked", ""],
    ["Decision-log row included", ""],
], widths=[3.0, 3.9], size=8.7, zebra=None)
h2(d, "Wes handoff")
para(d, "I am handing over the spreadsheet with the evidence and limits recorded above. I have "
        "not represented an unusual reading as a sensor fault without an independent basis.",
     size=9.5)
table(d, [
    ["Released by", "Date / time", "Received by"],
    ["", "", "Wes Tanaka, EIT"],
], widths=[2.7, 1.5, 2.7], size=8.6, zebra=None)
callout(d, "Retain with the project record",
        "Do not overwrite the February file. Copy it forward with its decision log and known "
        "limitations intact.", fill="EEF3F8", edge="6F8FAF")
save(d, os.path.join(OUT, "H6-04-Wes-gauge-file-handoff.docx"))


# =============================================================== KEY ========
d = course_doc("M06", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
callout(d, "Gated conclusion",
        "The 03:00 reading aligns with a heavy vehicle in the independent traffic counter. It "
        "is an unusual but recorded physical event, not the M05 duplicate block. Do not put this "
        "conclusion in the student deck or distribute this key before the hunt.",
        fill="FFF1E8", edge="F26B1D")
h2(d, "Evidence chain")
table(d, [
    ["Question", "Key"],
    ["Daily peaks", "15 values; median 110.7 µε; range 104.0–286.1 µε."],
    ["Shape", "Strong right tail. One extreme event; a normal model is not justified by this small, selected set."],
    ["Duplicate block", "Feb 12, 14:00–15:00. It does not create or alter the Feb 16 03:00 event."],
    ["Traffic match", "03:00 CST: 5-axle heavy vehicle, estimated 79,400 lb, quality flag OK."],
    ["Gauge pattern", "All eight corrected gauges rise at 03:00; G6 is highest at 286.1 µε."],
    ["Physical conclusion", "The records align in time. They support retaining the event; they do not alone prove structural safety or causation."],
], widths=[1.45, 5.45], size=8.25)
h2(d, "Audit of FOREMAN")
bullets(d, [
    ("Reasonable: ", "use daily peaks to ask whether the event is unusual; remove the known duplicate payload before counting."),
    ("Unsupported: ", "assume normality from 15 selected maxima, then use rarity as proof of sensor fault."),
    ("Category error: ", "“outlier” is a statistical description, not a physical diagnosis."),
    ("Missed tool call: ", "the independent traffic record was available and not queried."),
    ("Disposition: ", "retain and annotate the event; do not delete it. Escalation still requires engineering review."),
])
h2(d, "Model bounded decision")
callout(d, "Reveal only after collection",
        "I retained and annotated the 03:00 reading because it appears in the corrected feed, "
        "all gauges rise at the same timestamp, and the traffic counter records a heavy vehicle "
        "then; the duplicate block occurs on a different day. The evidence supports a real "
        "crossing-related event, but not by itself a safety disposition, so the next step is "
        "engineering review of the vehicle estimate and bridge response.",
        fill="EEF3F8", edge="6F8FAF")
h2(d, "Unit close and callback")
para(d, "Collect H6-03, then have every student complete H6-04 and hand the spreadsheet to "
        "Wes explicitly. Say only that the file is leaving their desk. Instructor continuity: "
        "preserve the February workbook unchanged; it returns at M25. Do not announce that "
        "callback to students.")
save(d, os.path.join(OUT, "KEY-M06-answer-key.docx"))


# ======================================================= FILE INDEX ==========
index_out = os.path.join(BUILD, "M06-INSTRUCTOR")
d = course_doc("M01 – M06", "What is in this pack", kind="FILE INDEX")
para(d, "M06 is based on main and depends on M05 PR #9 for feed.csv, the overnight run, "
        "threshold rules, and the unresolved alarm. M04 PR #8 supplies the preceding descriptive "
        "statistics meeting but is not a direct file dependency.", size=9.2, color=GREY, after=10)
for folder, files in [
    ("00-INSTRUCTOR", [
        ("run-of-day/index.html", "Podium desk for Unit 1"),
        ("run-of-day/M06-run-of-day.html", "M06 script, reveal boundary, debrief, and Wes handoff"),
        ("FILE-INDEX.docx", "This generated index"),
    ]),
    ("09-M05-overnight-alarm (PR #9 dependency)", [
        ("feed.csv + run log + threshold_config.csv", "The chain and unresolved event audited in M06"),
    ]),
    ("10-M06-alarm-audit", [
        ("M06-student.pptx", "Spoiler-safe 13-slide hunt deck"),
        ("M06-instructor-reveal.pptx", "Gated 7-slide conclusion and Unit 1 close"),
        ("H6-01-FOREMAN-alarm-disposition.docx", "FOREMAN's normality / sensor-fault reversal"),
        ("H6-02-distribution-and-chain-audit.docx", "Histogram, pipeline, and reasoning audit"),
        ("H6-03-decision-log-and-unit-debrief.docx", "Hand-in and mask-off prompts"),
        ("H6-04-Wes-gauge-file-handoff.docx", "Explicit student-to-Wes cover record"),
        ("M06-gauge-audit-and-handoff.xlsx", "Student workbook handed to Wes; retain for M25"),
        ("traffic_counts.csv", "Independent 03:00 event record"),
        ("KEY-M06-answer-key.docx", "Instructor-only physical-event resolution"),
    ]),
]:
    h2(d, folder)
    table(d, [["File", "What it is"]] + [[a, b] for a, b in files],
          widths=[3.15, 3.75], size=8.25)
save(d, os.path.join(index_out, "FILE-INDEX.docx"))
print("M06 handouts and index done")
