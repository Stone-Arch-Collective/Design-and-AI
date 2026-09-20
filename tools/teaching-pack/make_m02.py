"""M02 handouts: Measure something with your own hands."""
import os, sys, csv, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M02")
G = FACTS["m02"]
P = FACTS["m02_pin"]
GA = G["gauges"]
os.makedirs(OUT, exist_ok=True)
for f in ("gauges_install.csv", "pin_measurements_backup.csv"):
    shutil.copy(os.path.join(BUILD, "data", f), os.path.join(OUT, f))
    print("  wrote", f"M02/{f}")

# ============================================================ H2-01 ==========
d = course_doc("M02", "Measurement Lab — Measure One Thing, Five Times", kind="LAB SHEET")
para(d, "You are measuring a sheave pin. On the real bridge it carries the counterweight ropes "
        "over the tower, and its diameter sets how much steel is holding a 90-ton counterweight "
        "in the air. Today it is a pin, a dowel or a bolt on your table. The physics of measuring "
        "it is identical.", after=8)

callout(d, "Why before sensors",
        "On Tuesday you will be handed eight strain gauges' worth of data and asked whether to "
        "trust it. You cannot judge somebody else's measurements until you have watched your own "
        "disagree with each other.", fill="EEF3F8", edge="6F8FAF")

h2(d, "Part A — Five readings, one person")
numbers(d, [
    "Measure the diameter of the pin five times. Set the instrument down and pick it up again "
    "between readings. Do not look at your previous number before you take the next one.",
    "Record every reading, including the one you think is wrong. Especially that one.",
    "Write the smallest division your instrument can actually show. Not what you wish it showed.",
])
rows = [["Reading", "1", "2", "3", "4", "5"], ["Your value", "", "", "", "", ""]]
table(d, rows, widths=[1.3, 1.12, 1.12, 1.12, 1.12, 1.12], align=["l", "c", "c", "c", "c", "c"],
      zebra=None)
para(d, "", after=6)
rows = [
    ["Quantity", "Your answer", "How you got it"],
    ["Instrument smallest division", "", "Read it off the tool"],
    ["Largest reading − smallest reading (the range)", "", ""],
    ["Middle of your readings (the mean)", "", "Add them, divide by 5"],
]
table(d, rows, widths=[3.0, 1.6, 2.3], zebra=None)

h2(d, "Part B — The same pin, a different person")
para(d, "Swap with the pair next to you and measure their pin. Then compare your five readings of "
        "the same pin with theirs.", after=6)
rows = [
    ["Question", "Answer"],
    ["Is their mean higher or lower than yours?", ""],
    ["By how much?", ""],
    ["Is that difference bigger or smaller than the spread within your own five readings?", ""],
]
table(d, rows, widths=[4.4, 2.5], zebra=None)
callout(d, "The distinction",
        "Scatter within your own readings is random: it pushes you up as often as down, and more "
        "readings average it away. A difference between two people is systematic: it pushes one "
        "way every time, and a thousand readings will not remove it. Averaging fixes the first "
        "and hides the second. Hold on to that sentence — on Tuesday it is the whole lesson.")

h2(d, "Part C — Carry the uncertainty into an answer nobody measured")
para(d, "Nobody cares about the diameter. They care about the cross-sectional area of steel, "
        "because that is what carries the load.", after=6)
p = para(d, "", after=6)
box(p, fill="F4F6F8", color="C9CFD6", size=6, space=8)
run(p, "A = π d² / 4        so a 1% error in d becomes a 2% error in A", 12.5,
    bold=True, font=MONO_FONT, color=GIRDER)
rows = [
    ["Step", "Your answer"],
    ["Area from your mean diameter, A = π d² / 4", ""],
    ["Your spread in d, as a percentage of d", ""],
    ["Double it — that is your spread in A, as a percentage", ""],
    ["Your spread in A, in square units", ""],
]
table(d, rows, widths=[4.4, 2.5], zebra=None)
callout(d, "The question to take home",
        "You just turned a measurement you made into a number you did not. How much of the "
        "uncertainty survived the trip? Uncertainty does not stay where you left it.")

h2(d, "If there is no instrument on your table")
bullets(d, [
    ("Ruler instead of calipers: ", "the lab works unchanged, and works better in one way — a "
     "coarse instrument makes the resolution question obvious instead of subtle."),
    ("Nothing to measure: ", "use pin_measurements_backup.csv. It holds 24 readings of one pin "
     "by two people. Parts A and B run off the file; Part C is unchanged."),
])
save(d, os.path.join(OUT, "H2-01-measurement-lab.docx"))

# ============================================================ H2-02 ==========
d = acme_doc(subtitle="Field Record  ·  Instrumentation")
h1(d, "Sensor Installation Record — Strain Gauge Array")
rows = [
    ["Field", "Entry"],
    ["Structure", "Otter Bend Lift Bridge, County Road 9 over Kinnick River"],
    ["Installed", "January 14, 2027"],
    ["Installed by", "Northline Instrumentation, subcontract 27-114-S2"],
    ["Array", "8 bonded foil strain gauges, G1 through G8, midspan and quarter points"],
    ["Instrument resolution", "1 microstrain (µε)"],
    ["Witnessed by", "W. Tanaka, EIT"],
]
table(d, rows, widths=[1.7, 5.2])

h2(d, "Acceptance check")
para(d, "Specification KC-MB-12 §4.3 requires that under no load, each gauge read within "
        "±25 µε of zero. Twelve readings were taken at each gauge with the span down and the "
        "roadway closed. Raw readings are in gauges_install.csv.", after=8)

rows = [["Gauge", "Location", "Installed", "Notes from the field"]]
locs = ["S approach, midspan", "S approach, quarter pt", "S tower base", "Lift span, quarter pt",
        "Lift span, midspan", "Lift span, midspan (redundant)", "N tower base", "N approach, midspan"]
for i, (g, loc) in enumerate(zip([f"G{i}" for i in range(1, 9)], locs), 1):
    note = "Re-bonded after first attempt lifted" if g == "G6" else ""
    rows.append([g, loc, "2027-01-14", note])
table(d, rows, widths=[0.75, 2.35, 1.1, 2.7], size=9)

para(d, "", after=6)
callout(d, "Signed off",
        "Array installed and accepted. Northline's technician reported the array within "
        "specification and left the site at 14:20. No individual gauge values were recorded on "
        "this form.", fill="F4F6F8", edge="C9CFD6")
para(d, "", after=4)
handwriting(d, "Northline guy was in a hurry. I watched him re-glue G6 and didn't see him "
               "re-zero it. Said it was fine. — W.T.")
para(d, "Handwritten in the margin of the original. Nobody followed up.", size=8.5,
     italic=True, color=GREY, after=4)
save(d, os.path.join(OUT, "H2-02-sensor-installation-record.docx"))

# ============================================================ H2-03 ==========
d = foreman_doc("Strain Gauge Array — Baseline Acceptance Check",
                generated="2027-02-04 06:02 CST")
para(d, "Automated verification of the Otter Bend strain gauge array against installation "
        "specification KC-MB-12 §4.3 (no-load baseline within ±25 µε). Source: "
        "gauges_install.csv, 8 gauges × 12 readings.", size=9.5, after=8)

p = para(d, "", after=10)
box(p, fill="E8F5EC", color="2E7D4F", size=8, space=8)
run(p, "RESULT   ", 9.5, bold=True, font=HEAD_FONT, color=RGBColor(0x2E, 0x7D, 0x4F),
    caps=True, space=0.8)
run(p, f"PASS. Array baseline offset {G['array_mean']:.6f} µε against a specification limit of "
       f"±25 µε. The array is within tolerance and cleared for service. "
       f"Confidence 97%.", 10, bold=True)

h2(d, "Computation", color=REBAR)
mono_block(d, [
    "readings      = 96   (8 gauges x 12)",
    "array_mean    = mean(all readings)",
    f"array_mean    = {G['array_mean']:.6f} ue",
    f"spec_limit    = 25.000000 ue",
    f"|array_mean| <= spec_limit   ->   PASS",
])
para(d, "", after=8)

h2(d, "Array summary", color=REBAR)
table(d, [
    ["Statistic", "Value"],
    ["Gauges reporting", "8 of 8"],
    ["Readings ingested", "96"],
    ["Array baseline offset", f"{G['array_mean']:.6f} µε"],
    ["Specification limit", "±25.000000 µε"],
    ["Margin to limit", f"{25 - G['array_mean']:.6f} µε"],
    ["Status", "WITHIN SPECIFICATION"],
], widths=[3.3, 3.6], align=["l", "r"], head_fill="2B2F36")

h2(d, "Recommendation", color=REBAR)
para(d, "No re-zeroing required. Array may be used for the February load response study. "
        "Per-gauge review was not performed as the array-level check passed.", size=10, after=10)
mono_block(d, [
    "fm-analytics-4.2  |  96 values  |  0.4 s  |  no human review requested",
])
save(d, os.path.join(OUT, "H2-03-foreman-baseline-check.docx"))

# ============================================================ H2-04 ==========
d = acme_doc(subtitle="Internal Memorandum")
memo_block(d, to="You", frm="Diane Halvorsen, PE", date="Thursday, February 4, 2027",
           re_="HW1 — The gauge baseline, before I sign anything")
para(d, "FOREMAN cleared the strain gauge array this morning. Northline will invoice us for the "
        "install as soon as we accept it, and the February load response study runs off these "
        "gauges. So I would like a second pair of eyes before I accept anything.", after=8)
para(d, "I do not want an essay. I want to know whether the array is good.", after=10)

h2(d, "What to hand in", before=2)
numbers(d, [
    "Open gauges_install.csv. For each of the eight gauges, report the mean of its twelve "
    "readings and the spread (largest minus smallest).",
    "Check each gauge against the ±25 µε limit in KC-MB-12 §4.3, one gauge at a time. State "
    "which gauges pass and which do not.",
    "FOREMAN reported an array baseline offset of "
    f"{G['array_mean']:.6f} µε and called it a pass. Say in two or three sentences whether you "
    "agree, and why.",
    "Your note, version 1. One sentence.",
])

h2(d, "Your hours this week")
para(d, "You have ten project hours. You will not be able to do everything below, which is the "
        "point — choose, and write down what you chose not to do.", after=6)
table(d, [
    ["Option", "Hours", "What you get"],
    ["Recompute all 8 gauge means yourself", "2", "You know the numbers are real"],
    ["Recompute one gauge as a spot check", "1", "You know your method works, not that the rest is right"],
    ["Read the installation record and field notes", "1", "Context FOREMAN did not have"],
    ["Call Northline about the install", "1", "An answer arrives next meeting, not today"],
    ["Re-derive FOREMAN's array figure to see how it got there", "2", "You learn what it actually did"],
    ["Accept FOREMAN's result as delivered", "0", "Four hours saved, and a number you cannot defend"],
], widths=[3.0, 0.8, 3.1], align=["l", "c", "l"])

para(d, "", after=6)
callout(d, "One warning",
        "Whatever you hand me this week gets passed to Wes and used for the February study. If "
        "something is wrong in it, it will not stay in this week.", fill="FFF1E8", edge="F26B1D")
para(d, "", after=4)
handwriting(d, "Due Tuesday. One page. I mean one page. — D.H.")
save(d, os.path.join(OUT, "H2-04-HW1-gauge-baseline.docx"))

# ============================================================ H2-05 ==========
d = course_doc("M02", "Project Hours and Decision Log", kind="KEEP THIS ALL SEMESTER")
para(d, "One page, one line per week. It takes two minutes and it is the only record of what you "
        "chose. In May you will be asked to verify a package that contains your own February work, "
        "and this page is how you will find what is in it.", after=8)
callout(d, "Hours are not points",
        "Running out of hours never costs you a grade. Spending them on the wrong thing never "
        "costs you a grade either. The log is evidence of judgement, not a performance measure.",
        fill="EEF3F8", edge="6F8FAF")

rows = [["Wk", "What I was handed", "What I checked", "Hrs", "What I accepted without checking"]]
for i in range(12):
    rows.append([str(i + 1) if i else "1", "", "", "", ""])
table(d, rows, widths=[0.35, 1.75, 1.75, 0.4, 2.65], size=8.5, zebra=None)
para(d, "", after=8)
h2(d, "Standard hour costs")
table(d, [
    ["Action", "Hours"],
    ["Accept an AI output as delivered", "0"],
    ["Spot-check one value against its source", "1"],
    ["Verify a full output against the source or the data", "2"],
    ["Recompute independently, by hand or in a spreadsheet", "4"],
    ["Ask Wes, or call a vendor or lab", "1, answer arrives next meeting"],
    ["Redo a submission that came back to you", "2"],
], widths=[4.4, 2.5], align=["l", "r"])
save(d, os.path.join(OUT, "H2-05-hours-and-decision-log.docx"))

# ============================================================ KEY ============
d = course_doc("M02", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
h2(d, "The gauge numbers", before=2)
rows = [["Gauge", "Mean (µε)", "SD", "Range", "±25 µε check"]]
for g in [f"G{i}" for i in range(1, 9)]:
    s = GA[g]
    rows.append([g, f"{s['mean']:.2f}", f"{s['sd']:.2f}", str(s["range"]),
                 "PASS" if s["pass"] else "FAIL"])
table(d, rows, widths=[0.9, 1.5, 1.0, 1.0, 2.5], align=["c", "r", "r", "c", "c"])
bullets(d, [
    (f"G6 reads {GA['G6']['mean']:.2f} µε. ", "It exceeds the ±25 limit by 162.5 µε — seven and a half times the limit. Every "
     "other gauge sits within about 1 µε of zero."),
    (f"FOREMAN's array figure of {G['array_mean']:.4f} µε is arithmetically correct. ",
     "The eight gauge means sum to 184.50 µε — G6 contributes 187.50 and the other seven sum "
     "to −3.00 — and 184.50 ÷ 8 = 23.0625. Averaging divided one gauge's error by eight and "
     "slid a 162.5 µε failure under a limit it fails outright."),
    (f"Mean of the other seven gauges is {G['seven_gauge_mean']:.2f} µε. ",
     "That is what a healthy array looks like, and it is the comparison that makes G6 obvious."),
    ("G6 is redundant with G5 at lift span midspan. ",
     "That is what makes it catchable — and what makes accepting it tempting, since G5 covers it."),
])
callout(d, "The sentence to get out of a student, not to say yourself",
        "“The average passed but a gauge failed.” Wait for it. If nobody gets there by "
        "the 20-minute mark, ask: which gauge is the average hiding?")

h2(d, "The two planted errors in H2-03")
table(d, [
    ["#", "What FOREMAN did", "Concept", "How students catch it"],
    ["1", f"Averaged 8 gauges into one number, so a gauge that exceeds the limit by "
          f"162.5 µε lands at {G['array_mean']:.2f} and passes",
     "Systematic error and accuracy", "Check the gauges one at a time"],
    ["2", "Reported the result to six decimal places from an instrument that resolves 1 µε",
     "Instrument resolution", "Read the resolution on the installation record"],
], widths=[0.3, 2.7, 1.7, 2.2], size=8.5)
para(d, "Both are correct arithmetic. Neither is a software bug. The error is in what was "
        "computed, not how. Make that explicit — students arrive expecting AI mistakes to look "
        "like typos.", after=8)

h2(d, "Where the evidence is hidden")
bullets(d, [
    "H2-02 carries Wes's margin note: he watched G6 re-glued and did not see it re-zeroed. "
    "A student who spends one hour on the installation record gets the answer handed to them.",
    "A student who spends two hours recomputing the means finds it the hard way, and learns more.",
    "A student who accepts FOREMAN's result spends zero hours and carries G6 into HW3 and "
    "beyond. This is the M19 and M25 callback. Note who does this — do not tell them.",
])

h2(d, "Lab numbers, if you use the backup file")
table(d, [
    ["Quantity", "Value"],
    ["Mean diameter, all 24 readings", f"{P['mean']:.3f} mm"],
    ["Standard deviation", f"{P['sd']:.4f} mm"],
    ["Range", f"{P['min']:.2f} to {P['max']:.2f} mm"],
    ["Reader A mean", f"{P['mean_A']:.4f} mm"],
    ["Reader B mean", f"{P['mean_B']:.4f} mm"],
    ["Difference between readers", f"{P['mean_B'] - P['mean_A']:.4f} mm (systematic)"],
    ["Area from the mean diameter", f"{P['area_mm2']:.2f} mm²"],
    ["Relative spread in area", f"{P['area_rel_pct']:.3f}%  (double the 0.067% in d)"],
], widths=[3.4, 3.5], align=["l", "r"])
bullets(d, [
    ("The designed feature: ", f"reader B reads about {1000*(P['mean_B']-P['mean_A']):.0f} µm high "
     "on every reading. Averaging B's twelve readings does not remove it."),
    ("The bridge to Tuesday: ", "reader B is G6. Same error, different instrument."),
])

h2(d, "Timing, 75 minutes")
table(d, [
    ["Min", "What happens"],
    ["0–10", "The install record and FOREMAN's pass are on the screen. Ask: do we accept the array?"],
    ["10–25", "Teach measurement, repeated readings, range, resolution, accuracy vs precision"],
    ["25–50", "Lab: Parts A, B, C. Circulate. Part B matters most — make sure pairs actually swap"],
    ["50–65", "Open gauges_install.csv together. Per gauge, not in aggregate. Let G6 emerge"],
    ["65–75", "Hand out HW1 and the decision log. Explain the ten hours. Take no questions on "
              "what is 'worth' checking — that is the assignment"],
], widths=[0.85, 6.05], size=9)
save(d, os.path.join(OUT, "KEY-M02-answer-key.docx"))
print("M02 done")
