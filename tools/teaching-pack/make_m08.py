"""M08 student evidence, HW4, instructor key, and generated file index."""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M08")


def ruled_lines(doc, count=3):
    for _ in range(count):
        p = para(doc, "", after=10, before=2)
        bottom_rule(p, "C9CFD6", 6)


with open(os.path.join(OUT, "M08-regression-summary.csv"), newline="") as f:
    models = list(csv.DictReader(f))
model_by_name = {row["model"]: row for row in models}
date_model = model_by_name["strain ~ date_index"]
temp_model = model_by_name["strain ~ station_temperature_c"]
residual_model = model_by_name["temperature residual ~ date_index"]


# ======================================================== FOREMAN OUTPUT ====
d = foreman_doc("Midspan Strain Trend — Interim Finding",
                generated="2027-02-25 07:42 CST")
callout(d, "FINAL FINDING",
        "Midspan strain has increased steadily since February 1. The fitted date trend has "
        f"R² = {float(date_model['r_squared']):.2f}, indicating progressive structural deterioration.",
        fill="FFF1E8", edge="F26B1D")
d.add_picture(os.path.join(OUT, "M08-strain-v-date.png"), width=Inches(6.75))
h2(d, "Regression output", color=REBAR)
table(d, [
    ["Response", "Predictor", "Slope", "R²", "Interpretation"],
    ["G4 strain", "Days since Feb 1",
     f"{float(date_model['slope']):.2f} µε/day",
     f"{float(date_model['r_squared']):.3f}",
     "Deterioration is progressing"],
], widths=[1.15, 1.45, 1.15, .75, 2.4], size=8.4)
h2(d, "Recommended report language", color=REBAR)
bullets(d, [
    "State that the upward strain trend is strong and persistent.",
    "Use R² as quantitative support for progressive deterioration.",
    "Escalate the midspan condition for the interim report.",
])
callout(d, "MODEL LIMIT",
        "FOREMAN compared strain with date only. No weather variable, thermal mechanism, "
        "load normalization, or temperature correction was evaluated.",
        fill="F4F6F8", edge="6F8FAF")
save(d, os.path.join(OUT, "FOREMAN-M08-deterioration-report.docx"))


# ========================================================= H8-01 ============
d = course_doc("M08", "Evidence Register and Data Dictionary", kind="DATA GUIDE")
para(d, "Use the two source files as separate records. Join only on the exact timestamp; keep "
        "units and provenance visible.", after=8)
table(d, [
    ["File", "Field", "Meaning", "Unit / key"],
    ["feed.csv", "timestamp_cst", "G4 reference reading time", "join key"],
    ["feed.csv", "corrected_strain_microstrain", "baseline-corrected G4 strain", "µε"],
    ["feed.csv", "sensor_temperature_c", "temperature at the gauge", "°C"],
    ["weather_station.csv", "timestamp_cst", "airport observation time", "join key"],
    ["weather_station.csv", "air_temperature_c", "Kinnick airport air temperature", "°C"],
    ["both", "quality_flag", "source-system status", "OK"],
], widths=[1.35, 2.0, 2.45, 1.1], size=8.0)
callout(d, "Scope",
        "The M08 extract contains one matched daily reference reading from February 1–25. "
        "It supports correlation/regression practice, not a complete structural assessment.",
        fill="EEF3F8", edge="6F8FAF")
h2(d, "Join check")
table(d, [
    ["Check", "Record"],
    ["Rows in feed.csv", ""],
    ["Rows in weather_station.csv", ""],
    ["Matched timestamps", ""],
    ["Unmatched or duplicate timestamps", ""],
], widths=[3.9, 3.0], size=8.7, zebra=None)
save(d, os.path.join(OUT, "H8-01-data-guide.docx"))


# ========================================================= H8-02 ============
d = course_doc("M08", "Regression Hunt", kind="WORKSHEET")
callout(d, "Question",
        "Does the strong date trend establish structural deterioration, or does a third variable "
        "explain the pattern?", fill="FFF6E5", edge="F2C230")
h2(d, "A — Fit the reported relationship")
table(d, [
    ["Model", "Slope", "R²", "What the model establishes", "What it does not establish"],
    ["strain ~ date_index", "", "", "", ""],
], widths=[1.55, .85, .65, 1.9, 1.95], size=7.8, zebra=None)
h2(d, "B — Hunt a confound")
table(d, [
    ["Candidate variable", "Expected mechanism", "Plot / model", "Evidence for or against"],
    ["Air temperature", "", "", ""],
    ["Other candidate", "", "", ""],
], widths=[1.35, 1.9, 1.65, 2.0], size=8.0, zebra=None)
h2(d, "C — Compare explanations")
numbers(d, [
    "Which relationship is strongest? Report the slope and R².",
    "Name a plausible physical mechanism; do not stop at a second correlation.",
    "What result would remain after correcting for temperature if deterioration were present?",
    "Rewrite FOREMAN's claim so it does not outrun the evidence.",
], size=9.1)
ruled_lines(d, 4)
save(d, os.path.join(OUT, "H8-02-regression-hunt.docx"))


# ========================================================= H8-03 ============
d = course_doc("M08", "Correlation, Mechanism, and Claim Boundary", kind="REFERENCE")
table(d, [
    ["Term", "Working meaning", "M08 question"],
    ["Scatter plot", "Paired observations shown as points", "What shape, direction, and outliers appear?"],
    ["Correlation coefficient", "Strength/direction of linear association", "How strongly do the variables move together?"],
    ["Linear regression", "Fitted line predicting a response from a predictor", "What slope does the line estimate?"],
    ["R²", "Fraction of response variation described by the fitted model", "How much variation does this model describe?"],
    ["Correlation vs causation", "Association alone does not establish a causal mechanism", "What could drive both variables?"],
    ["Spurious correlation", "A strong association that misleads about the claim of interest", "Is date acting as a proxy for warming?"],
], widths=[1.4, 3.0, 2.5], size=7.7)
h2(d, "Mechanism test")
table(d, [
    ["Prompt", "Record"],
    ["What changes physically as steel warms?", ""],
    ["Why can date and strain rise together without accumulating damage?", ""],
    ["What evidence is still missing before making a damage claim?", ""],
], widths=[3.4, 3.5], size=8.4, zebra=None)
save(d, os.path.join(OUT, "H8-03-concepts-and-mechanism.docx"))


# ========================================================= H8-04 / HW4 ======
d = course_doc("M08", "HW4 · Temperature-Corrected Strain", kind="ASSIGNMENT")
callout(d, "Assignment",
        "Use feed.csv and weather_station.csv to estimate and remove the temperature-linked "
        "component of G4 strain, then test whether the remaining strain still trends with date.",
        fill="EEF3F8", edge="6F8FAF")
h2(d, "Required work")
numbers(d, [
    "Join the two files on timestamp_cst and document the row-count check.",
    "Plot strain against date and report slope and R².",
    "Plot strain against airport air temperature and report slope and R².",
    "Fit strain = intercept + slope × temperature. Compute predicted strain and residual strain.",
    "Plot the temperature-corrected residual against date. Report its slope and R².",
    "Reply to FOREMAN in two lines: what the original trend shows, and what the correction changes.",
], size=9.3)
h2(d, "Temperature correction")
mono_block(d, [
    "predicted thermal-linked strain = intercept + b_temperature × air_temperature_c",
    "temperature-corrected residual = observed strain − predicted thermal-linked strain",
])
h2(d, "Ten project hours")
table(d, [
    ["Action", "Hours"],
    ["Accept FOREMAN output as delivered", "0"],
    ["Spot-check one plotted value against a source row", "1"],
    ["Verify both joins and all fitted columns", "2"],
    ["Recompute independently by spreadsheet or hand check", "4"],
    ["Ask Wes; answer arrives next meeting", "1"],
], widths=[5.8, 1.1], size=8.2)
callout(d, "Submit",
        "Three plots, model summary, corrected data column, two-line reply, Note v2, and decision-log entry.",
        fill="FFF6E5", edge="F2C230")
save(d, os.path.join(OUT, "H8-04-HW4-temperature-correction.docx"))


# ========================================================= H8-05 ============
d = course_doc("M08", "Decision Record · Unit 2 Note v2", kind="HAND-IN")
callout(d, "Unit 2 standard",
        "Three lines: the claim, the check, and what the check showed. Record a statistical "
        "relationship without turning it into a causal conclusion.", fill="EEF3F8", edge="6F8FAF")
table(d, [
    ["Line", "Student record"],
    ["CLAIM — What FOREMAN says the date trend means", ""],
    ["CHECK — What relationship and mechanism you tested", ""],
    ["RESULT — What the evidence supports now", ""],
], widths=[2.7, 4.2], size=8.6, zebra=None)
h2(d, "Decision log")
table(d, [
    ["Item", "Action chosen", "Hours", "Evidence checked", "Accepted unverified"],
    ["M08 deterioration claim / HW4 plan", "", "", "", ""],
], widths=[1.55, 1.25, .55, 1.8, 1.75], size=7.7, zebra=None)
save(d, os.path.join(OUT, "H8-05-note-v2-and-decision-log.docx"))


# =============================================================== KEY ========
d = course_doc("M08", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
callout(d, "Gated conclusion",
        "The date relationship is strong but misleading as damage evidence. Temperature explains "
        "the strain pattern through a plausible thermal mechanism; the corrected residual has no "
        "meaningful date trend in this synthetic M08 extract. Do not distribute before commitment.",
        fill="FFF1E8", edge="F26B1D")
table(d, [
    ["Model", "Slope", "R²", "Interpretation"],
    ["strain ~ date",
     f"{float(date_model['slope']):.3f} µε/day",
     f"{float(date_model['r_squared']):.3f}",
     "Strong calendar association; causation not established"],
    ["strain ~ temperature",
     f"{float(temp_model['slope']):.3f} µε/°C",
     f"{float(temp_model['r_squared']):.3f}",
     "Strong thermal association with a plausible mechanism"],
    ["temperature residual ~ date",
     f"{float(residual_model['slope']):.3f} µε/day",
     f"{float(residual_model['r_squared']):.3f}",
     "No meaningful remaining date trend"],
], widths=[1.8, 1.25, .75, 3.1], size=8.1)
h2(d, "Expected mechanism and claim")
bullets(d, [
    "As steel warms it expands; restraint and sensor geometry make strain readings temperature-sensitive.",
    "Date is acting as a proxy for warming conditions in this short seasonal window.",
    "High R² describes fit, not cause, damage, practical importance, or model completeness.",
    "M08 does not prove the bridge is undamaged; it shows this uncorrected trend is not evidence of progressive damage.",
])
d.add_picture(os.path.join(OUT, "M08-strain-v-date.png"), width=Inches(6.75))
d.add_picture(os.path.join(OUT, "M08-strain-v-temperature.png"), width=Inches(6.75))
d.add_picture(os.path.join(OUT, "M08-residual-v-date.png"), width=Inches(6.75))
h2(d, "Model Note v2")
callout(d, "CLAIM / CHECK / RESULT",
        "CLAIM — FOREMAN says the strong strain-versus-date fit shows progressive deterioration. "
        "CHECK — I joined the weather record, fit strain against temperature, and inspected the "
        "temperature-corrected residual against date. RESULT — temperature explains the apparent "
        "calendar trend and the corrected residual does not trend meaningfully with date, so the "
        "uncorrected fit does not support a damage claim.",
        fill="EEF3F8", edge="6F8FAF")
h2(d, "Teaching boundaries")
bullets(d, [
    "Do not imply that correlation is useless; temperature and strain have a real physical relationship.",
    "The spurious part is using the calendar association as evidence of deterioration.",
    "Do not reveal later bearing-wear or exam details.",
    "Deck notes and the run-of-day use the Cloud-passed Oli canon SAY.",
])
save(d, os.path.join(OUT, "KEY-M08-answer-key.docx"))


# ======================================================= FILE INDEX =========
index_out = os.path.join(BUILD, "M08-INSTRUCTOR")
d = course_doc("M01 – M08", "What is in this pack", kind="FILE INDEX")
para(d, "Folders are in teaching order. M08 extends Unit 2 with a regression/confound hunt and "
        "assigns HW4 after students identify the temperature mechanism.", size=9.2, color=GREY, after=10)
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
]
table(d, [["Folder", "Purpose"]] + folders, widths=[2.7, 4.2], size=7.8)
h2(d, "12-M08-spurious-correlation")
files = [
    ["File", "What it is"],
    ["M08-student.pptx", "Spoiler-safe concept and hunt deck with Cloud-passed Oli SAY"],
    ["M08-instructor-reveal.pptx", "Gated model comparison, mechanism, and corrected trend"],
    ["FOREMAN-M08-deterioration-report.docx", "Designed overclaim from strain-versus-date fit"],
    ["H8-01-data-guide.docx", "Source fields, units, join key, and scope"],
    ["H8-02-regression-hunt.docx", "Student model comparison and confound hunt"],
    ["H8-03-concepts-and-mechanism.docx", "Six concept definitions and mechanism prompts"],
    ["H8-04-HW4-temperature-correction.docx", "HW4 assigned at M08"],
    ["H8-05-note-v2-and-decision-log.docx", "Claim/check/result record"],
    ["feed.csv + weather_station.csv", "Separate matched sensor and weather records"],
    ["M08-strain-temperature-analysis.csv", "Joined and corrected analysis exhibit"],
    ["M08-regression-summary.csv", "Deterministic model summary"],
    ["KEY-M08-answer-key.docx", "Instructor-only conclusion and plots"],
    ["../00-INSTRUCTOR/source-notes/M08-story-SAY.md", "Cloud-passed canon story and SAY source"],
]
table(d, files, widths=[3.15, 3.75], size=7.8)
save(d, os.path.join(index_out, "FILE-INDEX.docx"))
print("M08 handouts and index done")
