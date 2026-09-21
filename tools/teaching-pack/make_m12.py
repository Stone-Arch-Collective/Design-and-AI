"""M12 FOREMAN pack, H12 handouts, instructor key, and pack file index."""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M12")


def ruled_lines(doc, count=3):
    for _ in range(count):
        p = para(doc, "", after=10, before=2)
        bottom_rule(p, "C9CFD6", 6)


with open(os.path.join(OUT, "M12-daily-peak-strain.csv"), newline="") as f:
    strain = list(csv.DictReader(f))
with open(os.path.join(OUT, "M12-hourly-traffic.csv"), newline="") as f:
    traffic = list(csv.DictReader(f))


# ======================================================== FOREMAN PACK =====
d = foreman_doc("Otter Bend Interim Report · Chart Pack",
                generated="2027-03-11 07:42 CST")
callout(
    d, "PUBLISH STATUS",
    "Chart pack assembled for county review. Ready for county. No human review requested.",
    fill="FFF1E8", edge="F26B1D",
)
para(d, "Review the three chart tiles as delivered. The student copy intentionally does not "
        "identify which tiles should be approved, fixed, or pulled.", italic=True, color=GREY)
for letter, caption in [
    ("A", "Daily peak strain"),
    ("B", "Hourly traffic"),
    ("C", "Vehicle-class comparison"),
]:
    h2(d, f"TILE {letter} · {caption}", color=STICKER)
    d.add_picture(os.path.join(OUT, f"M12-tile-{letter}.png"), width=Inches(6.75))
save(d, os.path.join(OUT, "FOREMAN-M12-interim-chart-pack.docx"))


# ========================================================= H12-01 ==========
d = course_doc("M12", "County Chart Review", kind="HUNT WORKSHEET")
callout(
    d, "Do not ask Wes for the answers",
    "For each tile, decide APPROVE, FIX, or PULL. Name the question the chart should answer, "
    "check chart type and y-axis/baseline, and give one evidence-based reason.",
    fill="EEF3F8", edge="6F8FAF",
)
table(d, [
    ["Tile", "Question the chart answers", "Approve / fix / pull", "One-line reason"],
    ["A", "", "", ""], ["B", "", "", ""], ["C", "", "", ""],
], widths=[.55, 2.25, 1.55, 2.55], size=8.2, zebra=None)
h2(d, "Reader test")
bullets(d, [
    "Would the picture make ordinary variation look like failure?",
    "Would the picture hide a real change?",
    "Does the chart type preserve order when order is the question?",
    "Where does the quantitative axis begin, and what comparison does that baseline invite?",
])
h2(d, "Commit before reveal")
para(d, "I refuse tile(s) ______ as delivered because ______________________________________.")
ruled_lines(d, 2)
save(d, os.path.join(OUT, "H12-01-chart-hunt.docx"))


# ========================================================= H12-02 ==========
d = course_doc("M12", "Chart Type, Scale, and Baseline", kind="REFERENCE")
table(d, [
    ["Question", "Useful chart", "Audit move"],
    ["How does a value change over ordered time?", "Line or ordered bars", "Keep time order; label units"],
    ["How do categories compare?", "Bars or dots", "Use a common baseline; bars normally begin at zero"],
    ["How is one whole divided?", "Pie only for a small true part-to-whole set", "Confirm slices share one meaningful whole"],
    ["How large is variation in context?", "Line, dots, interval, or distribution", "Inspect axis limits and comparison range"],
], widths=[2.25, 2.15, 2.5], size=7.8)
callout(
    d, "Truncation",
    "A nonzero baseline is not automatically dishonest, but it magnifies vertical differences. "
    "If the visual claim is about magnitude, show enough context and state the scale plainly.",
    fill="FFF6E5", edge="F2C230",
)
callout(
    d, "AI chart review",
    "Finished styling is not evidence of a correct question, chart type, scale, or claim. "
    "Review the encoded comparison before reviewing polish.",
    fill="EEF3F8", edge="6F8FAF",
)
save(d, os.path.join(OUT, "H12-02-chart-choice-and-axis-guide.docx"))


# ========================================================= H12-03 ==========
d = course_doc("M12", "Redraw the Charts You Refuse", kind="LAB WORKSHEET")
callout(
    d, "Lab deliverable",
    "Redraw every chart you mark FIX or PULL. Preserve the source numbers. Change the visual "
    "encoding so an honest reader can answer the intended question.",
    fill="EEF3F8", edge="6F8FAF",
)
h2(d, "Source A · temperature-corrected daily peak strain")
table(d, [["Date", "µε"]] + [[r["date"][5:], r["temperature_corrected_peak_strain_microstrain"]]
      for r in strain], widths=[2.4, 2.0], size=7.1)
para(d, "Redraw A here or attach a spreadsheet chart. State the y-axis minimum and why:", bold=True)
ruled_lines(d, 3)
d.add_page_break()
h1(d, "Source B · hourly traffic")
table(d, [["Hour", "Total vehicles"]] + [[r["hour"], r["total_vehicles"]] for r in traffic],
      widths=[2.4, 2.0], size=7.4)
para(d, "Redraw B here or attach a spreadsheet chart. State why the chart type matches time order:",
     bold=True)
ruled_lines(d, 4)
h2(d, "Proof check")
table(d, [
    ["Check", "A", "B"],
    ["Source values preserved", "☐", "☐"],
    ["Axes / categories labeled with units", "☐", "☐"],
    ["Scale and baseline do not overstate the pattern", "☐", "☐"],
    ["Chart type matches the question", "☐", "☐"],
], widths=[4.7, 1.0, 1.0], size=8.0, zebra=None)
save(d, os.path.join(OUT, "H12-03-redraw-lab.docx"))


# ========================================================= H12-04 ==========
d = course_doc("M12", "HW6 · Two Honest Redraws", kind="HAND-IN")
callout(
    d, "Submit",
    "Turn in two clearly labeled charts: the corrected daily peak-strain chart and the corrected "
    "hourly-traffic chart. Use the supplied data; do not alter values to improve the story.",
    fill="EEF3F8", edge="6F8FAF",
)
h2(d, "Required with each redraw")
numbers(d, [
    "State the question the chart answers.",
    "Name the chart type and the quantitative-axis baseline or range.",
    "Give one sentence explaining what the corrected chart shows without overclaiming.",
])
h2(d, "Unit 2 Note v2")
table(d, [
    ["Line", "Student record"],
    ["CLAIM — What the original visual implied", ""],
    ["CHECK — Chart type, scale/baseline, and source-data comparison", ""],
    ["RESULT — What the corrected visuals support", ""],
], widths=[2.7, 4.2], size=8.3, zebra=None)
callout(
    d, "Hand-in boundary",
    "HW6 is the two redraws. Exam review is a separate in-class block and is not part of this lab.",
    fill="FFF6E5", edge="F2C230",
)
save(d, os.path.join(OUT, "H12-04-HW6-two-redraws.docx"))


# ========================================================= H12-05 ==========
d = course_doc("M12", "Exam 1 Review · Units 1–2", kind="SEPARATE 25-MINUTE BLOCK")
callout(
    d, "Boundary",
    "This review begins only after the 30-minute chart lab ends. It contains no exam scenario "
    "details and introduces no new designed errors.",
    fill="FFF6E5", edge="F2C230",
)
table(d, [
    ["Review move", "Prompt", "Evidence to name"],
    ["Spread", "Why can a mean alone mislead?", "SD, range, distribution, or count"],
    ["Confidence interval", "What does an interval preserve that a point estimate erases?", "Magnitude and uncertainty"],
    ["Spurious trend", "What second variable or mechanism could explain a trend?", "Comparison plot plus physical reasoning"],
    ["Human review", "Where must an agent-built claim stop for a person?", "Source, assumptions, data, and disposition"],
], widths=[1.25, 3.15, 2.5], size=7.8)
h2(d, "Four-minute rounds")
numbers(d, [
    "Write one sentence using a number with spread or interval.",
    "Rewrite one causal claim as a bounded association.",
    "Name one check independent of an agent's confident wording.",
    "Explain why a polished chart still requires human review.",
])
h2(d, "Last five minutes")
para(d, "Compare answers. Mark one Unit 1–2 move you will use under time pressure: ____________.")
save(d, os.path.join(OUT, "H12-05-exam-1-review.docx"))


# ========================================================= H12-06 ==========
d = course_doc("M12", "Async Code-Reading Primer", kind="ASSIGNMENT · DUE BEFORE M15")
callout(
    d, "Assigned today",
    "Complete guides/code-reading-primer.html before M15. The goal is reading generated Python, "
    "not writing a program from a blank file.",
    fill="EEF3F8", edge="6F8FAF",
)
numbers(d, [
    "Open the primer and complete its input → process → output trace.",
    "Identify variables, function calls, conditionals, and loops in the worked examples.",
    "Mark one line where units, a boundary condition, or an assumption could change the answer.",
    "Bring the completed self-check to M15.",
])
callout(
    d, "Why now",
    "You cannot check what you cannot read. This assignment prepares the verification work after "
    "Exam 1 without previewing any exam content.",
    fill="FFF6E5", edge="F2C230",
)
save(d, os.path.join(OUT, "H12-06-async-code-reading-primer.docx"))


# =============================================================== KEY ========
d = course_doc("M12", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
callout(
    d, "Gated reveal",
    "Do not identify the designed errors before students commit H12-01. Tiles A and B require "
    "redraws. Tile C is an acceptable comparison chart and prevents the hunt from being a wipeout.",
    fill="FFF1E8", edge="F26B1D",
)
callout(
    d, "Gated materials",
    "Distribute H12-01 and H12-02 first. Keep H12-03, the source CSVs, H12-04, this key, and the "
    "reveal deck closed until every student has committed all three initial dispositions.",
    fill="FFF6E5", edge="F2C230",
)
table(d, [
    ["Tile", "Disposition", "Reason", "Model repair"],
    ["A", "FIX / PULL", "99.5–104.5 µε y-axis magnifies ordinary variation and supports a failure-sounding title",
     "Show a zero or meaningfully broad contextual range; use a neutral title"],
    ["B", "FIX / PULL", "Pie slices discard time order; readers cannot see the hourly pattern cleanly",
     "Ordered bars or a line with hour on x and vehicles per hour on y"],
    ["C", "APPROVE", "Category comparison uses bars, labeled counts, and a zero baseline",
     "No required repair; accessibility or labeling refinements are acceptable"],
], widths=[.45, .85, 3.25, 2.35], size=7.2)
h2(d, "Model redraws")
d.add_picture(os.path.join(OUT, "M12-fix-A-honest-scale.png"), width=Inches(6.65))
d.add_picture(os.path.join(OUT, "M12-fix-B-hourly-bars.png"), width=Inches(6.65))
h2(d, "Timing guard")
bullets(d, [
    "Cloud-PASS durations total 80 minutes: Teach 20, Lab 30, Exam review 25, Note 5.",
    "The SEIS 201 course plan names a 75-minute meeting. Do not hide this five-minute mismatch.",
    "Exam review remains a separate block after Lab; never take its first five minutes from Lab.",
    "Before teaching, choose an approved accommodation such as a five-minute pre-class start or revised clock.",
])
h2(d, "Canon and spoiler guard")
bullets(d, [
    "Diane Halvorsen, PE is SKEPTIC; the county reads charts, not appendices.",
    "Wes Tanaka, EIT delivers the shared-folder pack and does not co-solve.",
    "FOREMAN is orange and looks publish-ready; human review is the skill.",
    "Do not introduce M13 handoff details or any Exam 1 overweight-permit details.",
])
save(d, os.path.join(OUT, "KEY-M12-answer-key.docx"))


# ======================================================= FILE INDEX =========
index_out = os.path.join(BUILD, "M12-INSTRUCTOR")
os.makedirs(index_out, exist_ok=True)
d = course_doc("M01 – M12", "What is in this pack", kind="FILE INDEX")
para(
    d, "Folders are in teaching order. M11 uses folder 15 and M12 uses folder 16, keeping "
    "meeting and pack numbering stable.", size=9.2, color=GREY,
)
folders = [
    ("00-INSTRUCTOR", "Run-of-day desk, faculty brief, source SAY notes, TOC, and this index"),
    ("01-BRAND-KIT", "ACMEJOB logos, fonts, templates, and brand guide"),
    ("02-M01-first-day", "Rules versus learned patterns"),
    ("03-M02-measurement", "Measurement, uncertainty, and G6"),
    ("04-M03-hallucination", "Next-token generation and source checking"),
    ("05-CHARTS", "Reusable meeting-deck charts"),
    ("06-BRIDGE", "Reusable bridge illustrations and schematics"),
    ("07-HW-CASE-B-LIFT-STATION", "M02 transfer homework and instructor key"),
    ("08-M04-one-number", "Center, spread, CV, low count, and sample scope"),
    ("09-M05-overnight-alarm", "Agent loop and threshold alarm"),
    ("10-M06-alarm-audit", "Distribution audit and Unit 1 handoff"),
    ("11-M07-training-mismatch", "Training coverage and distribution shift"),
    ("12-M08-spurious-correlation", "Regression and the thermal confound"),
    ("13-M09-false-precision", "False precision and sampling variability"),
    ("14-M10-deterioration-v-noise", "Paired intervals and signal/noise audit"),
    ("15-M11-dashboard-publish", "Agentic dashboard review and human publish checkpoint"),
    ("16-M12-misleading-charts", "Chart-type and truncated-axis hunt, HW6, and separate review"),
]
table(d, [["Folder", "Purpose"]] + folders, widths=[2.75, 4.15], size=7.1)
h2(d, "16-M12-misleading-charts")
files = [
    ["File", "What it is"],
    ["M12-student.pptx", "Spoiler-safe Teach, chart hunt, Lab, and separate review transition"],
    ["M12-instructor-reveal.pptx", "Gated designed-error names and corrected charts"],
    ["FOREMAN-M12-interim-chart-pack.docx", "Three-tile county chart pack; errors unlabeled"],
    ["H12-01-chart-hunt.docx", "Approve / fix / pull review checkpoint"],
    ["H12-02-chart-choice-and-axis-guide.docx", "Chart type, baseline, and AI-chart reference"],
    ["H12-03-redraw-lab.docx", "Source values and two redraw work areas"],
    ["H12-04-HW6-two-redraws.docx", "HW6 hand-in and Unit 2 Note v2"],
    ["H12-05-exam-1-review.docx", "Separate spoiler-safe 25-minute Units 1–2 review"],
    ["H12-06-async-code-reading-primer.docx", "Primer assignment due before M15"],
    ["M12-*.csv", "Deterministic strain, hourly traffic, and vehicle-class source data"],
    ["M12-tile-*.png", "Three student hunt charts"],
    ["M12-fix-*.png", "Instructor-only model redraws"],
    ["KEY-M12-answer-key.docx", "Dispositions, model repairs, timing conflict, and boundaries"],
    ["../00-INSTRUCTOR/source-notes/M12-story-SAY.md", "Cloud-PASS revised M12 canon SAY"],
]
table(d, files, widths=[3.2, 3.7], size=7.2)
save(d, os.path.join(index_out, "FILE-INDEX.docx"))
print("M12 handouts and instructor file index done")
