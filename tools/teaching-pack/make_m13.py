"""M13 inbox, pipeline hunt, Note v2, debrief, instructor key, and file index."""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M13")


def ruled_lines(doc, count=3):
    for _ in range(count):
        p = para(doc, "", after=10, before=2)
        bottom_rule(p, "C9CFD6", 6)


with open(os.path.join(OUT, "M13-pipeline-output.csv"), newline="") as f:
    pipeline = list(csv.DictReader(f))
with open(os.path.join(OUT, "FOREMAN-M13-pipeline-log.csv"), newline="") as f:
    log_rows = list(csv.reader(f))

mm_row = next(row for row in pipeline if row["source_lateral_offset"].endswith("mm"))
wrong_value = float(mm_row["model_input_microstrain"])
source_mm = float(mm_row["source_lateral_offset"].split()[0])
correct_ft = source_mm / 304.8
correct_alignment = 8.0 * correct_ft
correct_value = (
    float(mm_row["raw_strain_microstrain"])
    - float(mm_row["thermal_adjustment_microstrain"])
    + correct_alignment
)

# ============================================================= INBOX =======
d = acme_doc("INTERNAL HANDOFF · RECEIVED 2027-03-16")
memo_block(
    d,
    to="Project team",
    frm="Wes Tanaka, EIT",
    date="March 16, 2027",
    re_="Otter Bend pipeline handoff — partial",
)
callout(
    d, "WES · HANDOFF",
    "Handoff is late. Two of four sheets. I’ll finish assumptions later — Diane needs "
    "the pipeline tonight.",
    fill="EEF3F8", edge="6F8FAF",
)
h2(d, "Delivered")
table(d, [
    ["Workbook sheet", "Status"],
    ["SENSOR_READINGS", "Included"],
    ["WEATHER_STATION", "Included"],
    ["ASSUMPTIONS", "Not included"],
    ["QA_CHECKS", "Not included"],
], widths=[3.4, 3.5], size=8.6)
h2(d, "Direction")
callout(
    d, "DIANE HALVORSEN, PE · BELIEVER",
    "Run it. Otter Bend cannot wait on a perfect notebook.",
    fill="EEF3F8", edge="1F3A5F",
)
h2(d, "Side file on Diane's desk")
para(
    d,
    "The mechanical inspector reports bearing wear that FOREMAN rated fine at M07. "
    "Wes’s earlier accept-memo is attached to that inspector note. This is liability "
    "context for the handoff, not a second analysis assignment.",
    size=9.2,
)
save(d, os.path.join(OUT, "WES-M13-partial-handoff-note.docx"))

# ======================================================= FOREMAN LOG =======
d = foreman_doc("Pipeline Run Log — Accepted", generated="2027-03-16 20:01 CST")
callout(
    d, "RUN STATUS",
    "COMPLETE · 10 records delivered to the existing temperature-correction consumer.",
    fill="FFF1E8", edge="F26B1D",
)
table(d, log_rows, widths=[.45, 1.25, 2.15, .8, .8, .8, 1.65], size=6.8)
h2(d, "Automated disposition", color=REBAR)
bullets(d, [
    "Input schemas accepted.",
    "Join and adjustment stages completed without a stop condition.",
    "Output written to M13-pipeline-output.csv.",
    "No operator question generated.",
], size=9.0)
save(d, os.path.join(OUT, "FOREMAN-M13-pipeline-log.docx"))

# ========================================================= H13-01 =========
d = course_doc("M13", "Trace One Value End to End", kind="PIPELINE HUNT")
callout(
    d, "Hunt",
    "Pick one record. Trace it from the workbook through FOREMAN’s log to the model-output "
    "CSV. At every step ask whether units, missingness, and format stayed visible—or whether "
    "the path kept going quietly.",
    fill="EEF3F8", edge="6F8FAF",
)
h2(d, "Files")
table(d, [
    ["File", "Role"],
    ["wes_handoff.xlsx", "Two delivered source sheets"],
    ["FOREMAN-M13-pipeline-log.docx / .csv", "Step counts, schema choices, and run status"],
    ["M13-pipeline-output.csv", "Fields sent to the existing downstream consumer"],
], widths=[2.85, 4.05], size=8.3)
h2(d, "One-record trace")
table(d, [
    ["Checkpoint", "Observed value / count", "Unit or format", "Flag / question"],
    ["Source workbook", "", "", ""],
    ["Parse / ingestion", "", "", ""],
    ["Join / cleaning", "", "", ""],
    ["Adjustment fields", "", "", ""],
    ["Model input", "", "", ""],
], widths=[1.45, 1.85, 1.55, 2.05], size=7.7, zebra=None)
h2(d, "Stop-or-continue decision")
para(d, "Where should a careful engineer have stopped to ask?", bold=True, after=2)
ruled_lines(d, 3)
callout(
    d, "Time box",
    "You will not finish every column. Choose one path now; record the unchecked columns "
    "on H13-03 instead of implying they were reviewed.",
    fill="FFF6E5", edge="F2C230",
)
save(d, os.path.join(OUT, "H13-01-pipeline-trace-hunt.docx"))

# ========================================================= H13-02 =========
d = course_doc("M13", "Agentic Data Pipelines", kind="CONCEPT GUIDE")
table(d, [
    ["Concept", "Working meaning", "Question to ask"],
    ["Data pipeline", "A sequence that moves and transforms data", "What enters, changes, and exits?"],
    ["Data ingestion", "The point where a system reads source data", "What schema or defaults were assumed?"],
    ["Unit / format mismatch", "Values share a field but not one representation", "Were units parsed or merely presumed?"],
    ["Data cleaning", "Rules that retain, change, or remove records", "Was each decision logged?"],
    ["Missing / bad data", "Unavailable, invalid, or suspect values", "Stop, flag, impute, or exclude—and why?"],
    ["Errors through a pipeline", "An early mistake changes later fields and claims", "How does the difference grow downstream?"],
], widths=[1.45, 3.0, 2.45], size=7.6)
h2(d, "A pipeline decision record")
table(d, [
    ["Stage", "Minimum visible record"],
    ["Ingest", "source, row count, schema, units, parse failures"],
    ["Clean / join", "rule, affected records, before/after counts"],
    ["Transform", "formula or mapping, input units, output units"],
    ["Deliver", "consumer, version, exceptions, review checkpoint"],
], widths=[1.4, 5.5], size=8.3)
callout(
    d, "Boundary",
    "The downstream temperature-correction model is already familiar from M08. M13 audits "
    "what reaches it; it does not re-teach the regression.",
    fill="FFF6E5", edge="F2C230",
)
save(d, os.path.join(OUT, "H13-02-pipeline-concepts.docx"))

# ========================================================= H13-03 =========
d = course_doc("M13", "Decision Record · Unit 2 Note v2", kind="HAND-IN")
callout(
    d, "Unit 2 standard",
    "Record what you traced, what broke in your own words, and what you did not have time "
    "to check. A narrow, honest review is stronger than an undocumented claim of completeness.",
    fill="EEF3F8", edge="6F8FAF",
)
table(d, [
    ["Line", "Student record"],
    ["CLAIM — What FOREMAN’s completed run implies", ""],
    ["CHECK — Record traced and checkpoints inspected", ""],
    ["RESULT — What the trace supports and where the path should pause", ""],
], widths=[2.8, 4.1], size=8.4, zebra=None)
h2(d, "Unchecked-column log")
table(d, [
    ["Column / field left unchecked", "Why it was not checked", "Risk if wrong", "Next action"],
    ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
], widths=[2.0, 1.7, 1.55, 1.65], size=7.4, zebra=None)
h2(d, "Decision log")
table(d, [
    ["Item", "Action chosen", "Hours", "Evidence checked", "Accepted unverified"],
    ["M13 late handoff / pipeline run", "", "", "", ""],
], widths=[1.55, 1.25, .55, 1.8, 1.75], size=7.5, zebra=None)
save(d, os.path.join(OUT, "H13-03-note-v2-unchecked-log.docx"))

# ========================================================= H13-04 =========
d = course_doc("M13", "Unit 2 Debrief · Mask Off", kind="DISCUSSION")
callout(
    d, "This is not role-play",
    "Compare verification choices in plain language. Diane is a character, not the grader. "
    "The course grades the evidence and the record—not whether pressure made a choice feel easy.",
    fill="FFF6E5", edge="F2C230",
)
table(d, [
    ["Unit 2 theme", "What changed in your review behavior?"],
    ["Agent and model claims", ""],
    ["Human review checkpoints", ""],
    ["Charts and public-facing evidence", ""],
    ["Pipelines, units, and missing records", ""],
], widths=[2.55, 4.35], size=8.3, zebra=None)
h2(d, "Discuss")
numbers(d, [
    "What did you choose to verify, and what did you knowingly leave unchecked?",
    "Where did a confident output hide a choice about evidence?",
    "What should a human checkpoint make visible before work continues?",
], size=9.2)
save(d, os.path.join(OUT, "H13-04-unit-2-debrief.docx"))

# =============================================================== KEY ========
d = course_doc("M13", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
callout(
    d, "Designed error · reveal after the hunt",
    "Silent ingestion. FOREMAN never stops to ask.",
    fill="FFF1E8", edge="F26B1D",
)
h2(d, "What tracing should expose")
bullets(d, [
    "The source workbook has 12 sensor records but only 10 weather records. The exact-time "
    "inner join emits 10 model rows without a warning or exception record.",
    "One lateral_offset column contains feet and millimetres. FOREMAN extracts each numeric "
    "token and applies its default-foot schema to all records.",
    "The early assumptions flow into adjustment fields and then into the existing "
    "temperature-correction consumer. A COMPLETE status does not make the path honest.",
])
h2(d, f"Worked trace · {mm_row['record_id']}")
table(d, [
    ["Checkpoint", "FOREMAN path", "Unit-aware path"],
    ["Source offset", mm_row["source_lateral_offset"], mm_row["source_lateral_offset"]],
    ["Offset interpreted in feet", f"{float(mm_row['parsed_offset']):.3f} ft", f"{correct_ft:.4f} ft"],
    ["Alignment adjustment", f"{float(mm_row['alignment_adjustment_microstrain']):.2f} µε", f"{correct_alignment:.2f} µε"],
    ["Model input", f"{wrong_value:.2f} µε", f"{correct_value:.2f} µε"],
], widths=[2.1, 2.4, 2.4], size=8.1)
h2(d, "Model Note v2")
callout(
    d, "CLAIM / CHECK / RESULT",
    f"CLAIM — FOREMAN marks the run complete and emits 10 model records. CHECK — I traced "
    f"{mm_row['record_id']} from the workbook through parsing, join, adjustments, and output; "
    "I also reconciled row counts at each stage. RESULT — the path should stop at ingestion: "
    "source records disappear without an exception record, and a mixed-unit value is processed "
    "under one default unit. I did not review every field; those fields are listed separately.",
    fill="EEF3F8", edge="6F8FAF",
)
h2(d, "Story and spoiler boundaries")
bullets(d, [
    "Diane Halvorsen, PE remains BELIEVER: the pipeline has to run tonight.",
    "Wes Tanaka, EIT owns the late, partial, undocumented handoff and does not co-solve.",
    "The M07 bearing-wear / accept-memo item is inbox liability color only—not the hunt.",
    "Do not name the missing-temperature drop or millimetres-as-feet result before Reveal.",
    "Do not introduce any M14 overweight-permit scenario details.",
    "Run the Unit 2 debrief as its own 15-minute beat after Lab and Note.",
])
save(d, os.path.join(OUT, "KEY-M13-answer-key.docx"))

# ======================================================= FILE INDEX =========
index_out = os.path.join(BUILD, "M13-INSTRUCTOR")
d = course_doc("M01 – M13", "What is in this pack", kind="FILE INDEX")
para(
    d, "M13 is folder 17 in teaching order, following the built M11 dashboard and M12 chart "
    "packs in folders 15 and 16.",
    size=9.2, color=GREY, after=10,
)
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
    ("13-M09-false-precision", "Overconfidence, false precision, sampling, and sample scope"),
    ("14-M10-deterioration-v-noise", "Paired intervals, signal/noise audit, and HW5 callback"),
    ("15-M11-dashboard-publish", "Agent dashboard and human publish checkpoint"),
    ("16-M12-misleading-charts", "Chart selection, axes, and misleading visual claims"),
    ("17-M13-wes-handoff", "Pipeline ingestion, mixed formats, missing data, and Unit 2 debrief"),
]
table(d, [["Folder", "Purpose"]] + folders, widths=[2.75, 4.15], size=6.8)
h2(d, "17-M13-wes-handoff")
table(d, [
    ["File", "What it is"],
    ["M13-student.pptx", "Spoiler-safe inbox, concepts, trace hunt, Note v2, and debrief"],
    ["M13-instructor-reveal.pptx", "Gated silent-ingestion reveal and one worked trace"],
    ["wes_handoff.xlsx", "Two delivered source sheets from Wes’s four-sheet handoff"],
    ["WES-M13-partial-handoff-note.docx", "Late handoff, Diane direction, and M07 liability color"],
    ["FOREMAN-M13-pipeline-log.docx / .csv", "Orange machine run record"],
    ["M13-pipeline-output.csv", "Ten rows emitted to the existing consumer"],
    ["H13-01-pipeline-trace-hunt.docx", "One-value end-to-end trace worksheet"],
    ["H13-02-pipeline-concepts.docx", "Six concepts and minimum visible records"],
    ["H13-03-note-v2-unchecked-log.docx", "Claim/check/result plus unchecked-column log"],
    ["H13-04-unit-2-debrief.docx", "Mask-off Unit 2 debrief"],
    ["KEY-M13-answer-key.docx", "Instructor-only reveal, worked trace, and boundaries"],
    ["../00-INSTRUCTOR/source-notes/M13-story-SAY.md", "Cloud-PASS M13 canon story and SAY source"],
], widths=[3.2, 3.7], size=7.0)
save(d, os.path.join(index_out, "FILE-INDEX.docx"))
print("M13 handouts and index done")
