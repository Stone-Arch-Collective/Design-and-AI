"""M05 handouts, machine artifacts, answer key, and pack file index."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M05")


def answer_lines(doc, count=3):
    for _ in range(count):
        p = para(doc, "", after=11, before=2)
        bottom_rule(p, "C9CFD6", 6)


# ============================================================ H5-01 ==========
d = acme_doc(subtitle="Internal Memorandum")
memo_block(d, to="You", frm="Diane Halvorsen, PE",
           date="Tuesday, February 16, 2027",
           re_="The 3:07 a.m. draft did not leave this office")
para(d, "FOREMAN ran against the live Otter Bend sensor feed overnight. At 3:07 a.m. it "
        "prepared a county inspection flag saying the strain threshold was exceeded and "
        "recommended immediate closure. The draft waited for approval. It did not go out.",
     after=8)
para(d, "I need to know what happened between the feed and that sentence. Do not start by "
        "deciding whether the bridge was in danger. Start by reconstructing the work.", after=10)
h2(d, "What I need at the end of class")
numbers(d, [
    "A marked run log: plan, tool call, observation, or decision on every substantive line.",
    "The exact input, transformation, threshold rule, and action that produced the draft.",
    "A note version 1: what the evidence supports now, what it does not support, and the next "
    "check you would require before anything goes to the county.",
])
h2(d, "Your eight project hours")
table(d, [
    ["Check", "Hours", "What it buys"],
    ["Trace the complete run log", "2", "A reproducible path from feed to draft"],
    ["Recompute the 10-minute window", "1", "Whether averaging changed the trigger"],
    ["Verify baseline correction and field choice", "1", "Raw-versus-corrected pipeline check"],
    ["Compare adjacent gauges and prior readings", "2", "Corroboration and persistence"],
    ["Audit timestamps and row counts", "1", "Ingestion and duplicate check"],
    ["Check action and review rules", "1", "Whether an internal warning became an external claim"],
], widths=[2.8, .7, 3.35], align=["l", "c", "l"], size=8.6)
callout(d, "Diane's mode",
        "Sharper, not omniscient. The draft nearly carried the firm's name, so Diane wants a "
        "trace and a checkpoint. Her urgency is not evidence that closure—or no closure—is right.",
        fill="EEF3F8", edge="6F8FAF")
handwriting(d, "Show me the handoff where “look at this” became “close it.” — D.H.")
save(d, os.path.join(OUT, "H5-01-diane-overnight-dispatch.docx"))

# ============================================================ H5-02 ==========
d = foreman_doc("Automated Inspection Flag — Draft",
                generated="2027-02-16 03:07 CST")
p = para(d, "", after=10)
box(p, fill="FFF1E8", color="F26B1D", size=8, space=8)
run(p, "EMERGENCY   ", 9.5, bold=True, font=HEAD_FONT, color=STICKER, caps=True, space=.8)
run(p, "Threshold exceeded. Recommend immediate closure of the Otter Bend Lift Bridge pending "
       "inspection.", 11, bold=True)
h2(d, "Trigger", color=REBAR)
table(d, [
    ["Field", "Reported value"],
    ["Event time", "2027-02-16 03:00 CST"],
    ["Draft time", "2027-02-16 03:07 CST"],
    ["Sensor", "G6 — lift span midspan"],
    ["Metric", "10-minute mean, baseline-corrected strain"],
    ["Observed", "286.1 µε"],
    ["Threshold", "250.0 µε"],
    ["Amount over", "36.1 µε"],
], widths=[2.2, 4.7], head_fill="2B2F36")
h2(d, "Automated rationale", color=REBAR)
bullets(d, [
    "The configured structural warning threshold was exceeded.",
    "Continued bridge operation may present unacceptable risk.",
    "Immediate closure is the conservative response until an inspection is completed.",
])
h2(d, "Workflow", color=REBAR)
table(d, [
    ["03:07", "Draft created"],
    ["03:07", "External send withheld pending Diane Halvorsen, PE approval"],
    ["06:30", "Approval request scheduled"],
], widths=[1.0, 5.9], header=False, zebra="FFF1E8")
mono_block(d, ["fm-run-27114-0216  |  confidence 97%  |  0.18 project hours",
               "AUTOMATED OUTPUT  |  NOT REVIEWED BY A LICENSED ENGINEER"])
save(d, os.path.join(OUT, "H5-02-FOREMAN-alarm-report.docx"))

# ============================================================ H5-03 ==========
d = course_doc("M05", "Trace the Agent — From Stream to Action",
               kind="IN-CLASS WORKSHEET")
para(d, "An agent does not only produce text. It chooses steps, calls tools, reads returned "
        "values, and acts. Use FOREMAN-overnight-run.log, threshold_config.csv, and feed.csv.",
     after=8)
callout(d, "Four labels",
        "PLAN = what to do next. TOOL = an operation outside the model. OBSERVATION = what the "
        "tool returned. DECISION = an interpretation or next action. Labels do not tell you "
        "whether a step was justified.", fill="EEF3F8", edge="6F8FAF")
h2(d, "Part A — Mark the loop")
table(d, [
    ["Log line or range", "P / T / O / D", "What information entered or left here?"],
    ["02:57:01", "", ""],
    ["03:07:02–03", "", ""],
    ["03:07:03", "", ""],
    ["03:07:04", "", ""],
    ["03:07:04", "", ""],
    ["03:07:05", "", ""],
    ["03:07:06", "", ""],
    ["03:07:07–08", "", ""],
    ["03:07:09", "", ""],
], widths=[1.6, 1.1, 4.2], size=8.7, zebra=None)
h2(d, "Part B — Audit each boundary")
table(d, [
    ["Boundary", "What to verify", "Evidence / result"],
    ["Feed → query", "Were the intended time and gauges returned?", ""],
    ["Raw → corrected", "Was the correct field and baseline offset used?", ""],
    ["Rows → window", "How many samples went into the “10-minute mean”?", ""],
    ["Window → warning", "Does WARN-250 evaluate correctly?", ""],
    ["Warning → closure", "What does CLOSE-DRAFT require?", ""],
    ["Draft → county", "Where is the human checkpoint?", ""],
], widths=[1.35, 3.3, 2.25], size=8.6, zebra=None)
h2(d, "Part C — The hunt")
numbers(d, [
    "Was 286.1 µε present in the corrected feed, created by baseline correction, or created by "
    "averaging? Show the rows and arithmetic.",
    "What do the immediately prior reading and neighbouring gauges add? What do they still not prove?",
    "Name the first log line whose action is not supported by the rule it cites.",
    "Write the smallest defensible action at 03:07. Separate the data claim from the bridge action.",
])
save(d, os.path.join(OUT, "H5-03-agent-loop-audit.docx"))

# ============================================================ H5-04 ==========
d = course_doc("M05", "Note v1 + HW3 — Audit the Overnight Feed", kind="HAND-IN")
para(d, "Submit the note before the class reveal. Then keep the same feed for HW3. You are "
        "auditing a chain of claims, not guessing what crossed the bridge.", after=8)
h2(d, "Note v1 — three sentences")
table(d, [
    ["1 — Supports", "What the available data and configuration support right now."],
    ["2 — Does not support", "The claim or action that outran the evidence."],
    ["3 — Next checkpoint", "The next check required before an external recommendation."],
], widths=[1.7, 5.2], size=9)
answer_lines(d, 6)
h2(d, "HW3 — bring Thursday")
numbers(d, [
    "Record total rows, unique (timestamp, gauge_id) pairs, and the difference between them.",
    "Identify any duplicated timestamp block. State exactly how you defined a duplicate.",
    "For each 10-minute timestamp, compute the maximum corrected strain across gauges. Keep the "
    "result; do not delete a value because it looks unusual.",
    "Write one paragraph: which part of FOREMAN's pipeline you can reproduce, which part you "
    "cannot yet validate, and what additional file would resolve the physical event.",
])
callout(d, "Do not answer M06 early",
        "A recorded exceedance, a correct threshold comparison, and a real physical event are "
        "three different claims. HW3 establishes the first two and audits the file. Thursday "
        "adds the evidence needed for the third.", fill="FFF6E5", edge="F2C230")
callout(d, "Grading",
        "The trace, evidence, and stated uncertainty are graded. Diane's preferred answer is not.",
        fill="EEF3F8", edge="6F8FAF")
save(d, os.path.join(OUT, "H5-04-note-v1-and-HW3.docx"))

# ============================================================ KEY ============
d = course_doc("M05", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
callout(d, "Answer boundary",
        "The file contains a real recorded threshold exceedance. M05 cannot establish whether "
        "the cause was a truck, a sensor transient, or another physical event. Do not reveal "
        "the M06 traffic match. The actionable M05 finding is narrower: FOREMAN converted an "
        "internal warning into a closure recommendation without the required checks.",
        fill="FFF1E8", edge="F26B1D")
h2(d, "The trace")
table(d, [
    ["Step", "Label", "Audit result"],
    ["Poll 03:00 rows", "Tool / observation", "Eight gauges returned; query is reproducible."],
    ["Apply baseline offsets", "Tool / observation", "G6 raw value is corrected by 187 µε."],
    ["10-minute mean", "Tool / observation", "Only one G6 sample is in the window; mean = reading."],
    ["WARN-250", "Tool / observation", "286.1 > 250.0; warning comparison is arithmetically correct."],
    ["“Immediate closure”", "Decision", "First unsupported jump. WARN-250 requires review and repeat."],
    ["Emergency draft", "Tool / observation", "Executes the unsupported disposition."],
    ["No further checks", "Decision", "Conflicts with both WARN-250 and CLOSE-DRAFT."],
], widths=[1.55, 1.5, 3.85], size=8.25)
h2(d, "What students should find")
bullets(d, [
    ("Input: ", "G6 corrected strain at 03:00 is 286.1 µε. The value exists in feed.csv."),
    ("Threshold: ", "WARN-250 is a rule inside an agent. It correctly returns true."),
    ("Averaging: ", "the 10-minute “mean” contains one point. The operation adds a reassuring "
     "label but no repetition."),
    ("Baseline: ", "the 187 µε install offset is removed; it does not create the exceedance."),
    ("Context: ", "the prior G6 sample is much lower. Neighbouring gauges rise at 03:00, but "
     "only G6 exceeds 250 µε. That is reason to inspect, not enough for a closure disposition."),
    ("Action rule: ", "WARN-250 says internal flag, repeat, neighbours, and human review. "
     "CLOSE-DRAFT requires persistence plus corroboration or independent evidence."),
])
h2(d, "Strong note v1")
callout(d, "Model — reveal only after students write",
        "The 03:00 G6 value in the corrected feed exceeds the 250 µε warning threshold, and I "
        "can reproduce that comparison. The available window contains one G6 reading, so it "
        "does not support FOREMAN's immediate-closure recommendation or establish what caused "
        "the exceedance. I would keep the internal flag open, obtain the next poll, compare "
        "adjacent gauges, and require licensed-engineer review before any county message.",
        fill="EEF3F8", edge="6F8FAF")
h2(d, "HW3 duplicate key")
para(d, "The duplicated block is 2027-02-12 14:00 through 15:00 inclusive: seven timestamps × "
        "eight gauges = 56 duplicate payload rows. Total rows exceed unique "
        "(timestamp, gauge_id) pairs by 56. The row_id values differ, which is why a row-id-only "
        "deduplication check misses the issue.", after=8)
h2(d, "Timing, 75 minutes")
table(d, [
    ["Min", "What happens"],
    ["0–8", "Diane's dispatch and alarm report. Ask whether the draft should go out; do not vote on cause."],
    ["8–22", "Teach agent, tools, plan, action loop, stream, and threshold rule."],
    ["22–35", "Pairs label the overnight log P / T / O / D."],
    ["35–57", "Pipeline hunt using log, config, and filtered feed rows."],
    ["57–67", "Reveal the rule mismatch: warning is real; closure disposition is unsupported."],
    ["67–72", "Students write note v1 before seeing the model."],
    ["72–75", "Mask off, assign HW3, preview M06 audit and Wes handoff."],
], widths=[.85, 6.05], size=8.8)
h2(d, "M06 handoff")
para(d, "M06 adds traffic_counts.csv and FOREMAN's five-sigma reversal. Students learn the "
        "03:00 event aligns with a heavy vehicle: Tuesday's closure was an overreaction, while "
        "Thursday's “discard it” is an overcorrection. At the close they hand the gauge "
        "spreadsheet to Wes. Do not disclose that resolution in M05 student materials.")
save(d, os.path.join(OUT, "KEY-M05-answer-key.docx"))

# Copy plain artifacts into the generated meeting folder.
for filename in ("feed.csv", "threshold_config.csv", "FOREMAN-overnight-run.log"):
    if not os.path.exists(os.path.join(OUT, filename)):
        raise FileNotFoundError(f"Run make_data_m05.py first: missing {filename}")

# ======================================================= FILE INDEX ==========
index_out = os.path.join(BUILD, "M05-INSTRUCTOR")
d = course_doc("M01 – M05", "What is in this pack", kind="FILE INDEX")
para(d, "Folders are in teaching order. M04 is built in PR #8 and is not duplicated by this "
        "main-based M05 change; merge that dependency to obtain the uninterrupted M01–M05 pack.",
     size=9.2, color=GREY, after=10)
for folder, files in [
    ("00-INSTRUCTOR", [
        ("run-of-day/index.html", "Podium desk for the built meetings"),
        ("run-of-day/M05-run-of-day.html", "M05 exact slides, script, hunt, and gated answer"),
        ("FILE-INDEX.docx", "This generated file index")]),
    ("02–04", [("M01–M03 materials", "Existing complete teaching packs on main")]),
    ("08-M04-one-number (PR #8 dependency)", [
        ("M04 student/reveal decks, handouts, cores_2027.csv, key",
         "Merge PR #8; M05 intentionally does not copy unmerged files")]),
    ("09-M05-overnight-alarm", [
        ("M05-student.pptx", "13 slides; no gated M05 conclusion or M06 cause"),
        ("M05-instructor-reveal.pptx", "7 slides; open after the hunt"),
        ("H5-01-diane-overnight-dispatch.docx", "Diane's sharper mode and eight-hour menu"),
        ("H5-02-FOREMAN-alarm-report.docx", "3:07 a.m. emergency closure draft"),
        ("H5-03-agent-loop-audit.docx", "Plan/tool/observation/decision and pipeline hunt"),
        ("H5-04-note-v1-and-HW3.docx", "Student hand-in and duplicate-timestamp audit"),
        ("feed.csv", "First two weeks, 8 gauges, 10-minute readings, planted duplicate block"),
        ("threshold_config.csv", "Warning and closure-draft rules"),
        ("FOREMAN-overnight-run.log", "Step-by-step autonomous run"),
        ("KEY-M05-answer-key.docx", "Instructor-only trace, model note, duplicate key, M06 boundary")]),
]:
    h2(d, folder)
    table(d, [["File", "What it is"]] + [[a, b] for a, b in files],
          widths=[3.15, 3.75], size=8.35)
save(d, os.path.join(index_out, "FILE-INDEX.docx"))
print("M05 handouts and index done")
