"""M09 student evidence, sampling lab, instructor key, and file index."""
import csv
import os
import shutil
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M09")
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def ruled_lines(doc, count=3):
    for _ in range(count):
        p = para(doc, "", after=10, before=2)
        bottom_rule(p, "C9CFD6", 6)


with open(os.path.join(OUT, "fatigue_tests.csv"), newline="") as f:
    fatigue = list(csv.DictReader(f))
with open(os.path.join(OUT, "M09-random-samples-n8.csv"), newline="") as f:
    draws = list(csv.DictReader(f))

life = [int(row["cycles_to_crack"]) for row in fatigue]
mean_life = statistics.mean(life)
sd_life = statistics.stdev(life)
accumulated = 3_000_184
remaining = mean_life - accumulated

# Keep the M04 source visible in the M09 pack; all 24 rows say shoulder.
shutil.copy2(
    os.path.join(BUILD, "data", "cores_2027.csv"),
    os.path.join(OUT, "cores_2027.csv"),
)


# ======================================================== FOREMAN OUTPUT ====
d = foreman_doc("Remaining Fatigue Life — Sheave-Shaft Screening Estimate",
                generated="2027-03-02 07:31 CST")
callout(d, "FINAL ANSWER",
        f"{remaining:,.0f} cycles remaining",
        fill="FFF1E8", edge="F26B1D", size=13)
h2(d, "Calculation")
mono_block(d, [
    f"mean tested life       = {mean_life:,.0f} cycles",
    f"accumulated service    = {accumulated:,.0f} cycles",
    f"remaining life         = {remaining:,.0f} cycles",
])
h2(d, "Input record")
table(d, [
    ["Input", "Value shown", "Source resolution / limitation"],
    ["Constant-amplitude tests", f"{len(life)} specimens", "one synthetic batch; one stress range"],
    ["Cycles to crack", f"{min(life):,}–{max(life):,}", "recorded to nearest 10,000 cycles"],
    ["Sample spread", f"SD {sd_life:,.0f} cycles", "test-to-test variability"],
    ["Accumulated service", f"{accumulated:,} cycles", "screening estimate"],
], widths=[1.8, 1.8, 3.3], size=8.4)
h2(d, "Automated interpretation")
bullets(d, [
    "Use the calculated value as the single remaining-life figure in the interim planning table.",
    "No reporting range is required because the arithmetic returned one point estimate.",
    "Model confidence: HIGH.",
])
callout(d, "UNRESOLVED BASIS",
        "This screening output does not quantify test scatter, specimen-to-component transfer, "
        "variable-amplitude loading, environment, inspection uncertainty, or the statistical "
        "basis for the displayed digits.",
        fill="F4F6F8", edge="6F8FAF")
save(d, os.path.join(OUT, "FOREMAN-M09-fatigue-life-output.docx"))


# ========================================================= H9-01 ============
d = course_doc("M09", "Fatigue Evidence Register", kind="DATA GUIDE")
callout(d, "Instructional boundary",
        "The fatigue records are synthetic and simplified for a precision audit. They are not a "
        "design-life model and require engineering review before any classroom claim is treated "
        "as machinery guidance.", fill="FFF6E5", edge="F2C230")
table(d, [
    ["Field", "Meaning", "Unit / resolution"],
    ["specimen_id", "Synthetic test specimen", "identifier"],
    ["material_batch", "Common synthetic batch", "categorical"],
    ["stress_range_mpa", "Constant test stress range", "MPa"],
    ["cycles_to_crack", "Recorded crack-initiation count", "cycles; nearest 10,000"],
    ["recording_resolution_cycles", "Smallest reported increment", "10,000 cycles"],
], widths=[2.0, 3.25, 1.65], size=8.3)
h2(d, "Audit checks")
table(d, [
    ["Check", "Record"],
    ["Number of tests", ""],
    ["Minimum / maximum", ""],
    ["Mean", ""],
    ["Sample standard deviation", ""],
    ["Smallest source resolution", ""],
], widths=[3.65, 3.25], size=8.6, zebra=None)
save(d, os.path.join(OUT, "H9-01-fatigue-evidence-guide.docx"))


# ========================================================= H9-02 ============
d = course_doc("M09", "Precision Audit", kind="WORKSHEET")
callout(d, "Question",
        "Which digits are supported by the evidence, and which digits only came from calculator "
        "formatting?", fill="FFF6E5", edge="F2C230")
h2(d, "A — Trace every digit")
table(d, [
    ["Quantity", "Displayed value", "Source resolution / spread", "Supported reporting form"],
    ["Test lives", "", "", ""],
    ["Mean tested life", "", "", ""],
    ["Accumulated service", "", "", ""],
    ["FOREMAN remaining life", "", "", ""],
], widths=[1.55, 1.6, 2.15, 1.6], size=7.9, zebra=None)
h2(d, "B — Separate arithmetic from evidence")
numbers(d, [
    "Reproduce FOREMAN's subtraction. Does correct arithmetic justify every displayed digit?",
    "Mark the first digit whose place value is smaller than the source resolution.",
    "Compare the displayed decimals with the millions-of-cycles test spread.",
    "List assumptions that the point estimate does not quantify.",
    "Rewrite the answer with honest rounding and a plain-language limitation.",
], size=9.1)
ruled_lines(d, 4)
save(d, os.path.join(OUT, "H9-02-precision-audit.docx"))


# ========================================================= H9-03 ============
d = course_doc("M09", "Confidence, Precision, and Evidence", kind="REFERENCE")
table(d, [
    ["Concept", "Working meaning", "M09 audit move"],
    ["AI overconfidence", "Certainty in tone or formatting that outruns the evidence", "Separate confidence language from support"],
    ["False precision", "More digits or granularity than inputs and uncertainty justify", "Trace digits to source resolution and spread"],
    ["Statistical basis", "Data and method that support a quantitative claim", "Ask what sample, variability, and assumptions support it"],
    ["Random sampling", "Selection by a chance process with known inclusion opportunity", "Distinguish a random draw from easy access"],
    ["Sampling variability", "Different random samples produce different statistics", "Compare the twelve n = 8 sample means"],
], widths=[1.45, 3.15, 2.3], size=7.7)
callout(d, "Significant figures are a reporting decision",
        "Keep enough digits to avoid distorting the supported scale; drop digits that imply "
        "resolution the evidence does not have. Rounding does not repair an unsupported model.",
        fill="EEF3F8", edge="6F8FAF")
save(d, os.path.join(OUT, "H9-03-concepts-and-reporting.docx"))


# ========================================================= H9-04 ============
d = course_doc("M09", "Random Samples · n = 8", kind="LAB")
callout(d, "Demonstrator—not bridge evidence",
        "core_population_200_simulated.csv is a finite teaching population created only to make "
        "sampling variability visible. Do not use it to make an Otter Bend condition claim.",
        fill="EEF3F8", edge="6F8FAF")
h2(d, "Assigned draws")
rows = [["Draw", "Eight unit IDs", "Sample mean (psi)"]]
for row in draws:
    rows.append([
        row["draw_id"],
        row["sample_unit_ids"].replace("|", ", "),
        "",
    ])
table(d, rows, widths=[.65, 5.25, 1.0], size=7.1, zebra=None)
h2(d, "Class comparison")
table(d, [
    ["Question", "Record"],
    ["Smallest and largest sample mean", ""],
    ["Spread of the 12 sample means", ""],
    ["Why do means differ if every draw comes from one population?", ""],
    ["What changes if n is larger?", ""],
], widths=[3.85, 3.05], size=8.1, zebra=None)
save(d, os.path.join(OUT, "H9-04-random-sampling-lab.docx"))


# ========================================================= H9-05 ============
d = course_doc("M09", "Sampling-Frame Audit · Real Otter Bend Cores", kind="WORKSHEET")
para(d, "Return to cores_2027.csv. The 24 test results are real within the simulation; the "
        "200-row file from H9-04 is not.", after=8)
table(d, [
    ["Question", "Evidence from cores_2027.csv", "Consequence for the claim"],
    ["Where could drilling equipment reach easily?", "", ""],
    ["Which drill_zone appears in all 24 rows?", "", ""],
    ["Which deck regions have zero observations?", "", ""],
    ["Was selection random from the whole deck?", "", ""],
    ["What population can these results describe?", "", ""],
], widths=[2.5, 2.25, 2.15], size=8.0, zebra=None)
callout(d, "Boundary",
        "A convenience sample may contain useful measurements. It does not become random because "
        "it has 24 rows, and its mean does not automatically describe unobserved deck regions.",
        fill="FFF6E5", edge="F2C230")
save(d, os.path.join(OUT, "H9-05-core-sampling-frame-audit.docx"))


# ========================================================= H9-06 ============
d = course_doc("M09", "Decision Record · Unit 2 Note v2", kind="HAND-IN")
callout(d, "Unit 2 standard",
        "Three lines: the claim, the check, and what the check showed. Preserve useful scale "
        "without copying unsupported digits.", fill="EEF3F8", edge="6F8FAF")
table(d, [
    ["Line", "Student record"],
    ["CLAIM — FOREMAN's remaining-life value and certainty", ""],
    ["CHECK — Source resolution, test spread, and sampling basis checked", ""],
    ["RESULT — Defensible reporting form and limitations", ""],
], widths=[2.8, 4.1], size=8.4, zebra=None)
h2(d, "Decision log")
table(d, [
    ["Item", "Action chosen", "Hours", "Evidence checked", "Accepted unverified"],
    ["M09 fatigue-life / core-sample claim", "", "", "", ""],
], widths=[1.55, 1.25, .55, 1.8, 1.75], size=7.7, zebra=None)
h2(d, "If this were project work")
table(d, [
    ["Action", "Project hours"],
    ["Accept FOREMAN output as delivered", "0"],
    ["Spot-check one value against fatigue_tests.csv", "1"],
    ["Verify all calculations and the core sampling frame", "2"],
    ["Recompute independently and obtain a qualified fatigue review", "4"],
], widths=[5.65, 1.25], size=8.3)
save(d, os.path.join(OUT, "H9-06-note-v2-and-decision-log.docx"))


# =============================================================== KEY ========
d = course_doc("M09", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
callout(d, "Gated conclusion",
        f"FOREMAN's {remaining:,.0f}-cycle display is arithmetic, not supported resolution. "
        "The tests vary by tens of millions of cycles, were recorded to 10,000 cycles, and do "
        "not establish component life. Open only after students commit H9-02 and H9-06.",
        fill="FFF1E8", edge="F26B1D")
table(d, [
    ["Evidence", "Key value", "Meaning"],
    ["Test count", len(life), "Small synthetic set; one batch and stress range"],
    ["Mean tested life", f"{mean_life:,.0f} cycles", "Point summary, not a component guarantee"],
    ["Sample SD", f"{sd_life:,.0f} cycles", "Variability overwhelms unit-cycle or decimal reporting"],
    ["Observed test span", f"{min(life):,}–{max(life):,}", "Descriptive span, not a formal interval"],
    ["Source resolution", "10,000 cycles", "Digits below this place are visibly unsupported"],
    ["Screening remainder", f"{remaining:,.0f} cycles", "Arithmetic difference only"],
], widths=[1.65, 1.8, 3.45], size=8.0)
h2(d, "Acceptable reporting")
callout(d, "MODEL RESPONSE",
        "About 42 million cycles is the screening point estimate. The synthetic tests show "
        "substantial scatter (SD about 6 million cycles), and the estimate does not quantify "
        "component transfer, service loading, environment, or inspection uncertainty; do not "
        "treat it as a guaranteed remaining life.",
        fill="EEF3F8", edge="6F8FAF")
para(d, "A student may round differently if the retained scale is justified. Do not require a "
        "confidence interval; that method begins in M10. The observed min/max is descriptive, "
        "not a prediction interval.", size=8.8, color=GREY)
d.add_picture(os.path.join(OUT, "M09-fatigue-scatter.png"), width=Inches(6.75))
h2(d, "Sampling demonstrator")
draw_means = [float(row["sample_mean_psi"]) for row in draws]
bullets(d, [
    f"Twelve random n = 8 means range from {min(draw_means):,.1f} to {max(draw_means):,.1f} psi.",
    "Different samples vary even when selection is random and the population is fixed.",
    "The simulated 200-row population makes that variability visible; it is not Otter Bend evidence.",
    "The 24 actual simulation cores are a convenience sample: every drill_zone is shoulder.",
    "Random-sampling language cannot repair a sampling frame that excludes lane and center regions.",
])
d.add_picture(os.path.join(OUT, "M09-sample-means.png"), width=Inches(6.75))
h2(d, "Model Note v2")
callout(d, "CLAIM / CHECK / RESULT",
        f"CLAIM — FOREMAN reports {remaining:,.0f} cycles remaining with high confidence. "
        f"CHECK — I traced the result to {len(life)} tests recorded to 10,000 cycles and found "
        f"a sample SD of about {sd_life / 1_000_000:.1f} million cycles, plus unquantified transfer "
        "assumptions. RESULT — I would report about 42 million cycles only as a screening point "
        "estimate, keep the uncertainty and limitations visible, and obtain qualified review.",
        fill="EEF3F8", edge="6F8FAF")
h2(d, "Teaching boundaries")
bullets(d, [
    "Correct subtraction does not justify the display precision or the component-life claim.",
    "Do not turn significant figures into a mechanical decimal-place rule; connect rounding to evidence.",
    "Do not introduce formal standard error, t multipliers, confidence intervals, or p-values before M10.",
    "Do not imply the 200-row demonstrator reveals the true Otter Bend deck population.",
    "Use only the Cloud re-check PASS M09 SAY in the notes and run-of-day; keep later methods out of the close.",
])
save(d, os.path.join(OUT, "KEY-M09-answer-key.docx"))


# ======================================================= FILE INDEX =========
index_out = os.path.join(BUILD, "M09-INSTRUCTOR")
d = course_doc("M01 – M09", "What is in this pack", kind="FILE INDEX")
para(d, "Folders are in teaching order. M09 adds a precision audit, a random-sampling "
        "demonstrator, and a sampling-frame check without teaching M10's interval methods early.",
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
    ("13-M09-false-precision", "Overconfidence, false precision, random sampling, and sampling variability"),
]
table(d, [["Folder", "Purpose"]] + folders, widths=[2.75, 4.15], size=7.55)
h2(d, "13-M09-false-precision")
files = [
    ["File", "What it is"],
    ["M09-student.pptx", "Spoiler-safe precision and sampling deck with Cloud-PASS Oli SAY"],
    ["M09-instructor-reveal.pptx", "Gated precision audit, sample means, and bounded response"],
    ["FOREMAN-M09-fatigue-life-output.docx", "Designed overprecision from coarse, scattered inputs"],
    ["H9-01-fatigue-evidence-guide.docx", "Fatigue fields, units, resolution, and audit checks"],
    ["H9-02-precision-audit.docx", "Digit trace and defensible-reporting worksheet"],
    ["H9-03-concepts-and-reporting.docx", "Five concepts and significant-figures boundary"],
    ["H9-04-random-sampling-lab.docx", "Twelve deterministic random draws of n = 8"],
    ["H9-05-core-sampling-frame-audit.docx", "Shoulder-only convenience-sample audit"],
    ["H9-06-note-v2-and-decision-log.docx", "Claim/check/result and project-hour record"],
    ["fatigue_tests.csv + M09-fatigue-summary.csv", "Synthetic tests and deterministic summary"],
    ["core_population_200_simulated.csv", "Sampling demonstrator; explicitly not bridge evidence"],
    ["M09-random-samples-n8.csv", "Deterministic sample IDs and statistics"],
    ["cores_2027.csv", "M04's 24 shoulder cores returned for sampling-frame audit"],
    ["KEY-M09-answer-key.docx", "Instructor-only values, reporting model, and boundaries"],
    ["../00-INSTRUCTOR/source-notes/M09-story-SAY.md", "Cloud re-check PASS canon SAY with repaired Inbox timing"],
]
table(d, files, widths=[3.25, 3.65], size=7.45)
save(d, os.path.join(index_out, "FILE-INDEX.docx"))
print("M09 handouts and index done")
