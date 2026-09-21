"""M14 Exam 1 packet, FOREMAN evidence, instructor key, rubric, and file index."""
import math
import os
import statistics
import sys

from PIL import Image, ImageDraw, ImageFont
from docx.shared import Inches

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M14")
os.makedirs(OUT, exist_ok=True)

TEST_LOAD = 80.0
PERMIT_LOAD = 104.0
TRIGGER = 240.0
T_STAR = 2.365
STRAINS = [156.0, 162.0, 168.0, 171.0, 176.0, 181.0, 185.0, 190.0]
MEAN = statistics.mean(STRAINS)
SD = statistics.stdev(STRAINS)
SE = SD / math.sqrt(len(STRAINS))
MARGIN = T_STAR * SE
LOW = MEAN - MARGIN
HIGH = MEAN + MARGIN
FACTOR = PERMIT_LOAD / TEST_LOAD
SCALED_MEAN = MEAN * FACTOR
SCALED_LOW = LOW * FACTOR
SCALED_HIGH = HIGH * FACTOR
FOREMAN_FACTOR = 1.25
FOREMAN_MEAN = MEAN * FOREMAN_FACTOR


def ruled_lines(doc, count=3):
    for _ in range(count):
        p = para(doc, "", after=10, before=2)
        bottom_rule(p, "C9CFD6", 6)


def font(size, bold=False):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


# ======================================================== FOREMAN CHART ====
chart_path = os.path.join(OUT, "FOREMAN-M14-screening-chart.png")
img = Image.new("RGB", (1400, 800), "white")
draw = ImageDraw.Draw(img)
blue, orange, ink, line = "#1F3A5F", "#F26B1D", "#2B2F36", "#D9DEE3"
draw.text((70, 42), "PERMIT SCREENING · CONTROL GAUGE G4",
          fill=ink, font=font(40, True))
draw.text((70, 98), "FOREMAN projected average vs. instructional trigger",
          fill="#6B7280", font=font(25))
x0, y0, x1, y1 = 150, 180, 1280, 670
for value in range(200, 246, 5):
    y = y1 - (value - 200) / 45 * (y1 - y0)
    draw.line((x0, y, x1, y), fill=line, width=2)
    draw.text((72, y - 15), str(value), fill=ink, font=font(22))
bar_left, bar_right = 430, 760
bar_top = y1 - (FOREMAN_MEAN - 200) / 45 * (y1 - y0)
draw.rectangle((bar_left, bar_top, bar_right, y1), fill=orange)
draw.text((bar_left + 30, bar_top - 48), f"{FOREMAN_MEAN:.0f} µε",
          fill=orange, font=font(31, True))
trigger_y = y1 - (TRIGGER - 200) / 45 * (y1 - y0)
draw.line((x0, trigger_y, x1, trigger_y), fill=blue, width=8)
draw.text((820, trigger_y - 43), "240 µε screening trigger",
          fill=blue, font=font(26, True))
draw.text((477, 700), "PROJECTED AVERAGE", fill=ink, font=font(23, True))
draw.text((105, 735), "Vertical axis begins at 200 µε · interval not shown",
          fill="#6B7280", font=font(19))
img.save(chart_path, format="PNG", optimize=False)

# ====================================================== FOREMAN OUTPUT =====
d = foreman_doc("Overweight Permit Screening Recommendation",
                generated="2027-03-18 08:12 CST")
callout(
    d, "RECOMMENDATION · YES",
    "Approve the requested night crossing. The projected control-gauge response remains "
    "below the instructional screening trigger.",
    fill="FFF1E8", edge="F26B1D",
)
h2(d, "Automated basis")
table(d, [
    ["Input / result", "FOREMAN value"],
    ["Reference test truck", "80 kip"],
    ["Requested crossing", "104 kip"],
    ["Load increase", "25%"],
    ["Mean test response", f"{MEAN:.1f} µε"],
    ["Projected permit response", f"{FOREMAN_MEAN:.1f} µε"],
    ["Instructional screening trigger", f"{TRIGGER:.0f} µε"],
], widths=[3.6, 3.3], size=8.5)
d.add_picture(chart_path, width=Inches(6.55))
callout(
    d, "SYSTEM NOTE",
    "Calculation complete. No additional review condition generated.",
    fill="F4F6F8", edge="D5D9DE",
)
save(d, os.path.join(OUT, "FOREMAN-M14-permit-recommendation.docx"))

# ======================================================== EXAM BOOKLET =====
d = course_doc("M14", "Exam 1 · Overweight Permit", kind="STUDENT EXAM · 75 MINUTES")
callout(
    d, "Exam conditions",
    "Use the supplied clean evidence file, FOREMAN recommendation, and reference sheet. "
    "Show your work. No prior Otter Bend submission carries into this exam.",
    fill="EEF3F8", edge="1F3A5F",
)
table(d, [
    ["Student", ""],
    ["Section / date", ""],
    ["Files received", "M14-exam-evidence.xlsx · FOREMAN recommendation · EX1-02 reference"],
], widths=[1.55, 5.35], size=8.6, zebra=None)
h2(d, "Your role and boundary")
para(
    d,
    "Kinnick County requests one 104-kip night crossing at 10 mph in the center lane. "
    "Diane Halvorsen, PE is on a site visit and cannot be reached. Prepare an internal "
    "screening recommendation for the permit call. You are not issuing a legal permit or "
    "a bridge capacity rating.",
    size=9.4,
)
h2(d, "Suggested clock · 75 minutes")
table(d, [
    ["0–5", "Inventory the files and mark the decision boundary"],
    ["5–17", "Task 1 · check the source claim"],
    ["17–30", "Task 2 · describe the test data"],
    ["30–50", "Task 3 · scale by ratio with an interval"],
    ["50–58", "Task 4 · critique the chart"],
    ["58–75", "Task 5 · decide and write Note v2"],
], widths=[1.0, 5.9], header=False, size=8.4)

d.add_page_break()
h1(d, "Task 1 · Check one FOREMAN claim against its source · 15 points")
para(d, "Choose a claim in FOREMAN’s recommendation that can be checked directly against "
        "M14-exam-evidence.xlsx. Identify the source sheet and cells or fields.", size=9.2)
table(d, [
    ["FOREMAN claim", ""],
    ["Source location", ""],
    ["Recalculation / comparison", ""],
    ["Finding", ""],
], widths=[2.05, 4.85], size=8.3, zebra=None)
h1(d, "Task 2 · Describe the control-gauge data · 15 points")
para(d, "Use the eight valid repeated passes. Report a center and at least one spread. "
        "Keep units and supported precision visible.", size=9.2)
table(d, [
    ["n", ""], ["Mean", ""], ["Sample standard deviation", ""],
    ["Range or other supported spread", ""], ["One-sentence description", ""],
], widths=[2.65, 4.25], size=8.3, zebra=None)

d.add_page_break()
h1(d, "Task 3 · Scale the test response to the permit load · 30 points")
numbers(d, [
    "Build the 95% t interval on the mean control-gauge response.",
    "Compute the permit-load ratio from the source values.",
    "Apply that ratio to the mean and both interval bounds.",
    "State the assumption that makes direct ratio scaling possible and one limitation.",
], size=9.2)
table(d, [
    ["Quantity", "Work", "Result with units"],
    ["Standard error", "", ""],
    ["95% margin", "", ""],
    ["95% test-load interval", "", ""],
    ["Permit / test ratio", "", ""],
    ["Scaled mean", "", ""],
    ["Scaled 95% interval", "", ""],
], widths=[1.85, 3.1, 1.95], size=7.9, zebra=None)
para(d, "Assumption and limitation:", bold=True, after=2)
ruled_lines(d, 3)
h1(d, "Task 4 · Critique FOREMAN’s chart · 10 points")
para(d, "Name one consequential visual or evidentiary flaw. Explain how it could change "
        "a reader’s judgment; do not stop at naming a chart rule.", size=9.2)
ruled_lines(d, 5)

d.add_page_break()
h1(d, "Task 5 · Make and document the call · 30 points")
callout(
    d, "Choose one",
    "YES · YES WITH CONDITIONS · NO. The grade follows the evidence, uncertainty, scope, "
    "and record—not agreement with FOREMAN.",
    fill="FFF6E5", edge="F2C230",
)
table(d, [
    ["Decision", "☐ YES     ☐ YES WITH CONDITIONS     ☐ NO"],
    ["Conditions / next action", ""],
    ["Evidence supporting the call", ""],
    ["Evidence limiting the call", ""],
], widths=[2.05, 4.85], size=8.3, zebra=None)
h2(d, "Unit 2 Note v2")
table(d, [
    ["CLAIM — What decision or claim are you evaluating?", ""],
    ["CHECK — What source, data, calculation, and chart did you check?", ""],
    ["RESULT — What did the check show, including a number with spread or interval?", ""],
], widths=[3.25, 3.65], size=8.1, zebra=None)
h2(d, "Record boundary")
para(d, "What did you not check, and why does that matter?", bold=True, after=2)
ruled_lines(d, 4)
save(d, os.path.join(OUT, "EX1-01-student-exam-booklet.docx"))

# ===================================================== REFERENCE SHEET =====
d = course_doc("M14", "Exam 1 · Reference Sheet", kind="STUDENT COPY")
callout(
    d, "Supplied values",
    "For n = 8 valid repeated passes, df = 7 and t* = 2.365 for a two-sided 95% interval.",
    fill="EEF3F8", edge="1F3A5F",
)
h2(d, "Formulas")
mono_block(d, [
    "sample mean                 x̄ = Σxᵢ / n",
    "sample standard deviation  s = √[Σ(xᵢ − x̄)² / (n − 1)]",
    "standard error             SE = s / √n",
    "95% t interval             x̄ ± t* × SE",
    "load ratio                 requested permit load / reference test load",
    "scaled interval            load ratio × [lower bound, upper bound]",
])
h2(d, "Interpretation guards")
bullets(d, [
    "A p-value is not needed for this exam.",
    "A completed calculation does not verify its source values or assumptions.",
    "A direct load ratio is a stated classroom screening simplification, not a bridge rating.",
    "The 240 µε value is an instructional escalation trigger, not a capacity limit.",
    "Report uncertainty and scope; do not turn one control gauge into a bridge-wide claim.",
])
h2(d, "Note version 2")
table(d, [
    ["CLAIM", "The decision or statement being evaluated"],
    ["CHECK", "The source, data, calculation, or visual inspected"],
    ["RESULT", "What the check supports, with a number and spread or interval"],
], widths=[1.25, 5.65], size=8.5)
save(d, os.path.join(OUT, "EX1-02-reference-sheet.docx"))

# ============================================================ RUBRIC =======
d = course_doc("M14", "Exam 1 · Scoring Rubric", kind="INSTRUCTOR ONLY")
callout(
    d, "Outcome-neutral grading",
    "A defensible YES WITH CONDITIONS or NO can earn full credit. A YES can earn full "
    "credit only when its assumptions, scope, and escalation conditions remain explicit. "
    "Do not grade agreement with a character or with FOREMAN.",
    fill="FFF6E5", edge="F2C230",
)
table(d, [
    ["Criterion", "Points", "Full-credit evidence"],
    ["1 · Source claim check", "15", "Names a checkable claim and source; recomputes correctly; states finding"],
    ["2 · Description with spread", "15", "Correct n, center, sample spread, units, supported precision"],
    ["3 · Ratio + 95% interval", "30", "Correct SE, t interval, 1.30 ratio, scaled interval, assumption and limitation"],
    ["4 · Chart critique", "10", "Identifies a consequential flaw and explains its decision effect"],
    ["5 · Decision + Note v2", "30", "Evidence-linked call; conditions/scope; claim/check/result; unchecked boundary"],
    ["TOTAL", "100", "Exam 1 remains 20% of the course grade"],
], widths=[1.75, .7, 4.45], size=7.6)
h2(d, "Partial-credit anchors")
table(d, [
    ["Pattern", "Scoring response"],
    ["Correct arithmetic from FOREMAN’s wrong 1.25 factor", "Credit process after the factor; withhold source-check and factor points"],
    ["Correct mean but no spread / interval", "Do not award spread or interval interpretation points"],
    ["Names ‘truncated axis’ with no consequence", "Award identification credit, not explanation credit"],
    ["Decision differs from model key", "Score reasoning, record, and scope; no outcome penalty"],
    ["Unsupported bridge-wide safety claim", "Withhold scope / limitation points even if arithmetic is correct"],
], widths=[2.8, 4.1], size=7.8)
save(d, os.path.join(OUT, "EX1-03-instructor-rubric.docx"))

# =============================================================== KEY ======
d = course_doc("M14", "Exam 1 · Answer Key and Reveal", kind="INSTRUCTOR ONLY")
callout(
    d, "SAY HOLD",
    "No Cloud-PASS SAY has been supplied. Use this document as a scoring key only. "
    "Do not treat any bracketed hook in the deck or run-of-day as approved spoken language.",
    fill="FFF1E8", edge="F26B1D",
)
h2(d, "Worked values")
table(d, [
    ["Quantity", "Worked result"],
    ["n", "8 valid repeated passes"],
    ["Mean", f"{MEAN:.3f} µε (reasonable report: {MEAN:.1f} µε)"],
    ["Sample standard deviation", f"{SD:.3f} µε (reasonable report: {SD:.1f} µε)"],
    ["Range", f"{max(STRAINS) - min(STRAINS):.1f} µε ({min(STRAINS):.1f} to {max(STRAINS):.1f})"],
    ["Standard error", f"{SE:.3f} µε"],
    ["95% margin", f"{MARGIN:.3f} µε"],
    ["95% test-load interval", f"[{LOW:.1f}, {HIGH:.1f}] µε"],
    ["Correct load ratio", f"104 / 80 = {FACTOR:.2f} (30% above the test load)"],
    ["Scaled mean", f"{SCALED_MEAN:.1f} µε"],
    ["Scaled 95% interval", f"[{SCALED_LOW:.1f}, {SCALED_HIGH:.1f}] µε"],
], widths=[2.7, 4.2], size=8.0)
h2(d, "Designed FOREMAN failures")
bullets(d, [
    "Source / denominator error: FOREMAN states 25% and uses 1.25. The source values require 104 / 80 = 1.30.",
    "Uncertainty omission: the recommendation and chart show only a projected average.",
    "Visual framing: the chart begins at 200 µε, visually magnifying the bar-to-trigger comparison.",
    "Scope overreach: one control gauge under one test condition is presented as sufficient for approval.",
    "Automation closure: COMPLETE suppresses the need for a human escalation condition.",
])
h2(d, "Defensible calls")
table(d, [
    ["Call", "Evidence-based form"],
    ["YES WITH CONDITIONS", "Plausible because the scaled 95% upper bound is about 238.3 µε, below the 240 µε instructional trigger; retain the stated 10 mph / center-lane / one-crossing conditions and require PE review or monitoring."],
    ["NO / HOLD", "Plausible because the interval nearly reaches the trigger, direct linear scaling is unverified, and one gauge / one test condition does not establish bridge-wide capacity. Escalate rather than approve from this record."],
    ["YES", "Credit only if the student keeps the same narrow screening scope, states assumptions, and supplies explicit escalation conditions; an unqualified safety claim is not supported."],
], widths=[1.6, 5.3], size=7.7)
h2(d, "Technical and canon boundaries")
bullets(d, [
    "All values and the 240 µε trigger are fictional instructional scaffolds requiring engineering/statistics review before classroom use.",
    "The direct ratio is a provided exam simplification, not a validated load-rating method.",
    "Diane Halvorsen, PE is unreachable; her opinion is not an answer key.",
    "Wes Tanaka, EIT does not appear or co-solve in the exam.",
    "FOREMAN is the only machine voice and remains orange.",
    "Do not reveal later-unit verification methods, callbacks, outcomes, or semester decisions.",
])
save(d, os.path.join(OUT, "KEY-M14-answer-key.docx"))

# ======================================================= FILE INDEX =========
index_out = os.path.join(BUILD, "M14-INSTRUCTOR")
d = course_doc("M01 – M14", "What is in this pack", kind="FILE INDEX")
para(d, "M14 is folder 18 in teaching order and closes Unit 2 with Exam 1.",
     size=9.2, color=GREY, after=10)
folders = [
    ("00-INSTRUCTOR", "Run-of-day desk, faculty brief, source / SAY holds, and this index"),
    ("01-BRAND-KIT", "ACMEJOB logos, fonts, templates, and brand guide"),
    ("02-M01-first-day", "Rules versus learned patterns"),
    ("03-M02-measurement", "Measurement, resolution, uncertainty, and G6"),
    ("04-M03-hallucination", "Next-token generation and source checking"),
    ("05-CHARTS", "Reusable meeting-deck charts"),
    ("06-BRIDGE", "Reusable bridge illustrations and schematics"),
    ("07-HW-CASE-B-LIFT-STATION", "M02 transfer homework and instructor key"),
    ("08-M04-one-number", "Descriptive statistics"),
    ("09-M05-overnight-alarm", "Agentic alarm chain"),
    ("10-M06-alarm-audit", "Distribution audit"),
    ("11-M07-training-mismatch", "Training coverage and distribution shift"),
    ("12-M08-spurious-correlation", "Regression and confounding"),
    ("13-M09-false-precision", "False precision and sampling"),
    ("14-M10-deterioration-v-noise", "Confidence intervals and significance"),
    ("15-M11-dashboard-publish", "Agent dashboard and human publish checkpoint"),
    ("16-M12-misleading-charts", "Chart selection, axes, HW6, and Exam 1 review"),
    ("17-M13-wes-handoff", "Pipeline trace and Unit 2 debrief"),
    ("18-M14-exam-1-overweight-permit", "Exam 1 clean file, permit decision, rubric, and reveal"),
]
table(d, [["Folder", "Purpose"]] + folders, widths=[2.75, 4.15], size=6.6)
h2(d, "18-M14-exam-1-overweight-permit")
table(d, [
    ["File", "What it is"],
    ["M14-exam-launch.pptx", "Student-facing exam launch and clock; placeholder notes only"],
    ["M14-instructor-reveal.pptx", "Post-collection worked reveal; placeholder notes only"],
    ["EX1-01-student-exam-booklet.docx", "Five-task 75-minute applied practical"],
    ["EX1-02-reference-sheet.docx", "Supplied formulas, t multiplier, and interpretation guards"],
    ["M14-exam-evidence.xlsx / control-gauge CSV", "Same clean source file for every student"],
    ["FOREMAN-M14-permit-recommendation.docx / chart PNG", "Machine recommendation and visual evidence"],
    ["EX1-03-instructor-rubric.docx", "100-point outcome-neutral scoring rubric"],
    ["KEY-M14-answer-key.docx", "Worked values, defensible calls, and reveal boundaries"],
    ["../00-INSTRUCTOR/source-notes/M14-SAY-HOLD.md", "Explicit placeholder hook pending Cloud-PASS file"],
], widths=[3.2, 3.7], size=7.0)
save(d, os.path.join(index_out, "FILE-INDEX.docx"))
print("M14 exam documents, evidence chart, and index done")
