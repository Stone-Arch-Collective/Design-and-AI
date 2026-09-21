"""M11 dashboard asset, review form, handouts, key, and generated file index."""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M11")
with open(os.path.join(OUT, "M11-dashboard-tile-register.csv"), newline="") as f:
    tiles = list(csv.DictReader(f))


def lines(doc, count=3):
    for _ in range(count):
        p = para(doc, "", after=9, before=2)
        bottom_rule(p, "C9CFD6", 6)


# ======================================================== DASHBOARD ASSET ===
d = foreman_doc("Otter Bend Public Health Dashboard — Publish Candidate",
                generated="2027-03-09 06:12 CST")
callout(d, "PUBLISH REQUEST",
        "County-facing Otter Bend health dashboard assembled overnight. Five tiles. "
        "Requesting approval to publish to the public portal. No human review requested. "
        "Confidence high.",
        fill="FFF1E8", edge="F26B1D")
d.add_picture(os.path.join(OUT, "M11-five-tile-dashboard.png"), width=Inches(6.75))
callout(d, "AUTOMATION STATUS",
        "Draft assembled by FOREMAN. Public release remains pending until an authorized human "
        "selects PUBLISH.",
        fill="F4F6F8", edge="6F8FAF")
save(d, os.path.join(OUT, "FOREMAN-M11-dashboard-stub.docx"))


# ========================================================= H11-01 ===========
d = course_doc("M11", "Five-Tile Publish Review", kind="REVIEW FORM")
callout(d, "Human review checkpoint",
        "For every tile, choose APPROVE, FIX, or PULL. Give one sentence tied to its "
        "definition, units, source, timestamp, or evidence.",
        fill="FFF6E5", edge="F2C230")
table(d, [
    ["Tile", "Decision", "One-sentence reason / required change"],
    ["1 · Structural health score", "□ APPROVE  □ FIX  □ PULL", ""],
    ["2 · Midspan strain trend", "□ APPROVE  □ FIX  □ PULL", ""],
    ["3 · Weather join coverage", "□ APPROVE  □ FIX  □ PULL", ""],
    ["4 · Source quality flags", "□ APPROVE  □ FIX  □ PULL", ""],
    ["5 · Reporting window", "□ APPROVE  □ FIX  □ PULL", ""],
], widths=[1.65, 2.0, 3.25], size=8.0, zebra=None)
h2(d, "Publish decision")
table(d, [
    ["Decision", "Record"],
    ["□ ALLOW PUBLISH  □ HOLD PUBLISH", ""],
    ["Conditions before release", ""],
    ["Reviewer / date", ""],
], widths=[2.8, 4.1], size=8.4, zebra=None)
save(d, os.path.join(OUT, "H11-01-dashboard-review-form.docx"))


# ========================================================= H11-02 ===========
d = course_doc("M11", "Dashboard Metric Checkpoint", kind="FIELD GUIDE")
table(d, [
    ["Check", "Question to ask", "Evidence to record"],
    ["Definition", "What exactly is measured or calculated?", "Formula, inputs, inclusion rules"],
    ["Units", "What scale or unit gives the value meaning?", "Unit, denominator, or category"],
    ["Source", "Where did the value come from?", "File, system, owner, or method"],
    ["Timestamp", "What period does it represent?", "Observation and refresh time"],
    ["Claim", "What does color, arrow, label, or score imply?", "Support and known limits"],
], widths=[1.0, 2.75, 3.15], size=8.0)
callout(d, "Decision vocabulary",
        "APPROVE = publish as shown. FIX = retain the tile after a named correction. "
        "PULL = do not publish the tile because a correction cannot be made safely now.",
        fill="EEF3F8", edge="6F8FAF")
save(d, os.path.join(OUT, "H11-02-metric-checkpoint-guide.docx"))


# ========================================================= H11-03 ===========
d = course_doc("M11", "Agentic Dashboards and Human Review", kind="REFERENCE")
table(d, [
    ["Concept", "Working meaning", "M11 application"],
    ["Dashboard and metrics", "A compact display of defined measures for a decision", "A tile needs meaning, not just polish"],
    ["Time series data", "Measurements ordered across time", "An arrow is an interpretation of a trend"],
    ["Agent-built report", "An automated system assembles evidence and presentation", "Assembly speed does not validate claims"],
    ["Agent autonomy", "A system acts across steps with limited intervention", "Drafting is different from authority to publish"],
    ["Human review checkpoint", "A person evaluates output before a consequential action", "Approve, fix, or pull every tile"],
], widths=[1.45, 2.75, 2.7], size=7.8)
h2(d, "Checkpoint rule")
callout(d, "PUBLISH IS AN ACTION",
        "FOREMAN may assemble and request. A person must review the evidence, record the "
        "decision, and own whether the county-facing page goes live.",
        fill="FFF1E8", edge="F26B1D")
save(d, os.path.join(OUT, "H11-03-concepts-and-publish-check.docx"))


# ========================================================= H11-04 ===========
d = course_doc("M11", "Decision Record · Unit 2 Note v2", kind="HAND-IN")
callout(d, "Submit both records",
        "Attach the completed five-tile review form. Then write the three-line Note v2 audit trail.",
        fill="EEF3F8", edge="6F8FAF")
table(d, [
    ["Line", "Student record"],
    ["CLAIM — What FOREMAN asks permission to publish", ""],
    ["CHECK — What you checked across the five tiles", ""],
    ["RESULT — What may publish, what must change, and why", ""],
], widths=[2.65, 4.25], size=8.4, zebra=None)
h2(d, "Decision log")
table(d, [
    ["Item", "Action chosen", "Hours", "Evidence checked", "Accepted unverified"],
    ["M11 dashboard publish checkpoint", "", "", "", ""],
], widths=[1.65, 1.2, .55, 1.75, 1.75], size=7.6, zebra=None)
save(d, os.path.join(OUT, "H11-04-note-v2-and-decision-log.docx"))


# =============================================================== KEY ========
d = course_doc("M11", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
callout(d, "Gated reveal",
        "Two tiles are designed to fail careful review: the undefined 87/100 structural health "
        "score and the recycled raw M08 trend with a red worsening arrow. Do not identify them "
        "before students complete all five decisions.",
        fill="FFF1E8", edge="F26B1D")
table(d, [
    ["Tile", "Model decision", "Why"],
    ["1 · Structural health score", "PULL or FIX", "87/100 has no formula, inputs, source, or defensible meaning"],
    ["2 · Midspan strain trend", "PULL or FIX", "Raw M08 date trend recycles a temperature-driven damage story"],
    ["3 · Weather join coverage", "APPROVE", "Defined numerator/denominator, sources, and exact-match rule"],
    ["4 · Source quality flags", "APPROVE", "Defined and sourced; explicitly not a condition rating"],
    ["5 · Reporting window", "APPROVE", "Dates, count, source, and source timestamp are visible"],
], widths=[1.55, 1.05, 4.3], size=7.7)
h2(d, "Acceptable variation")
bullets(d, [
    "A student may choose FIX for either failing tile if the required correction is specific and removes the unsupported public claim.",
    "A student may choose FIX for a cleaner tile when the requested improvement is evidence-based; the form is not graded by matching five labels.",
    "The key assesses the reason and release boundary, not agreement with Diane Halvorsen, PE.",
])
h2(d, "Model Note v2")
callout(d, "CLAIM / CHECK / RESULT",
        "CLAIM — FOREMAN asks to publish a five-tile county dashboard without human review. "
        "CHECK — I checked each tile for a definition, units, source, timestamp, and whether its "
        "claim matches prior evidence. RESULT — hold publish until the undefined score and "
        "recycled worsening trend are removed or corrected; the three defined source-status "
        "tiles may remain.",
        fill="EEF3F8", edge="6F8FAF")
h2(d, "Spoiler boundary")
bullets(d, [
    "Diane Halvorsen, PE is skeptical. Wes Tanaka, EIT is tired and does not co-solve.",
    "Do not preview later chart tricks, pipeline defects, or Exam 1 details.",
    "Use only Diane Halvorsen, PE; Wes Tanaka, EIT; Otter Bend; and FOREMAN.",
])
save(d, os.path.join(OUT, "KEY-M11-answer-key.docx"))


# ======================================================= FILE INDEX =========
index_out = os.path.join(BUILD, "M11-INSTRUCTOR")
d = course_doc("M01 – M11", "What is in this pack", kind="FILE INDEX")
para(d, "Folders are numbered in teaching order. M11 is folder 15 so it follows the M09 and "
        "M10 packs without renumbering.",
        size=9.2, color=GREY, after=10)
folders = [
    ("00-INSTRUCTOR", "Run-of-day desk, faculty brief, source SAY notes, and this index"),
    ("01-BRAND-KIT", "ACMEJOB logos, fonts, templates, and brand guide"),
    ("02-M01-first-day", "Rules versus learned patterns"),
    ("03-M02-measurement", "Measurement, resolution, uncertainty, and G6"),
    ("04-M03-hallucination", "Next-token generation and source checking"),
    ("05-CHARTS", "Reusable meeting-deck charts"),
    ("06-BRIDGE", "Reusable bridge illustrations and schematics"),
    ("07-HW-CASE-B-LIFT-STATION", "M02 transfer homework and instructor key"),
    ("08-M04-one-number", "Center, spread, CV, low count, and sample scope"),
    ("09-M05-overnight-alarm", "Agent loop, threshold alarm, and unresolved event"),
    ("10-M06-alarm-audit", "Distribution audit, traffic corroboration, and Unit 1 handoff"),
    ("11-M07-training-mismatch", "Training bias, distribution shift, and Unit 2 note v2"),
    ("12-M08-spurious-correlation", "Correlation, regression, thermal confound, and HW4"),
    ("13-M09-false-precision", "False precision, fatigue-test scatter, and random sample means"),
    ("14-M10-deterioration-v-noise", "Confidence intervals and paired signal-versus-noise audit"),
    ("15-M11-dashboard-publish", "Agentic dashboards and the human publish checkpoint"),
]
table(d, [["Folder", "Purpose"]] + folders, widths=[2.7, 4.2], size=7.5)
h2(d, "15-M11-dashboard-publish")
files = [
    ["File", "What it is"],
    ["M11-student.pptx", "Spoiler-safe concepts and five-tile hunt with Cloud-passed SAY"],
    ["M11-instructor-reveal.pptx", "Gated tile decisions and publish boundary"],
    ["FOREMAN-M11-dashboard-stub.docx", "Five-tile county-facing publish candidate"],
    ["H11-01-dashboard-review-form.docx", "Approve / fix / pull plus reason for all five tiles"],
    ["H11-02-metric-checkpoint-guide.docx", "Definition, units, source, timestamp, and claim checks"],
    ["H11-03-concepts-and-publish-check.docx", "Five concepts and the authority boundary"],
    ["H11-04-note-v2-and-decision-log.docx", "Claim / check / result hand-in"],
    ["M11-dashboard-tile-register.csv", "Deterministic definitions and provenance for all tiles"],
    ["M11-five-tile-dashboard.png", "Rendered dashboard stub used in the pack"],
    ["KEY-M11-answer-key.docx", "Instructor-only designed errors and acceptable decisions"],
    ["../00-INSTRUCTOR/source-notes/M11-story-SAY.md", "Cloud-passed canon story and SAY source"],
]
table(d, files, widths=[3.15, 3.75], size=7.6)
save(d, os.path.join(index_out, "FILE-INDEX.docx"))
print("M11 dashboard asset, handouts, key, and index done")
