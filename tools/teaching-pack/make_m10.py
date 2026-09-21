"""M10 evidence, worksheets, HW5 callback, instructor key, and file index."""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M10")


def ruled_lines(doc, count=3):
    for _ in range(count):
        p = para(doc, "", after=10, before=2)
        bottom_rule(p, "C9CFD6", 6)


with open(os.path.join(OUT, "M10-interval-summary.csv"), newline="") as f:
    summaries = list(csv.DictReader(f))
coupon = summaries[0]
paired95 = summaries[1]
paired99 = summaries[2]


# ======================================================== FOREMAN OUTPUT ====
d = foreman_doc("Deck Load-Test Comparison — Final",
                generated="2027-03-04 07:31 CST")
callout(
    d, "FINAL FINDING",
    "Mean strain under the reference test truck increased 6 percent from 2019 to 2027. "
    "The change is statistically significant (p = 0.04), so there is a 96 percent chance "
    "the deck has deteriorated. Deterioration is confirmed.",
    fill="FFF1E8", edge="F26B1D",
)
d.add_picture(os.path.join(OUT, "M10-paired-location-means.png"), width=Inches(6.75))
h2(d, "Reported basis", color=REBAR)
table(d, [
    ["Comparison", "2019 mean", "2027 mean", "Change", "Disposition"],
    ["8 paired locations", "100.0 µε", "106.0 µε", "+6.0%", "Confirmed deterioration"],
], widths=[1.6, 1.15, 1.15, .9, 2.1], size=8.4)
h2(d, "Recommendation", color=REBAR)
bullets(d, [
    "Enter “deterioration confirmed” in the interim report.",
    "Treat p = 0.04 as 96% confidence that the deterioration claim is true.",
    "Do not distinguish statistical significance from engineering magnitude.",
])
callout(
    d, "MODEL LIMIT",
    "FOREMAN gives no interval, does not show the confidence-level sensitivity, and does not "
    "separate repeatability noise, process controls, and the estimated between-year change.",
    fill="F4F6F8", edge="6F8FAF",
)
save(d, os.path.join(OUT, "FOREMAN-M10-deterioration-claim.docx"))


# ========================================================= H10-01 ==========
d = course_doc("M10", "Coupon Confidence-Interval Warm-Up", kind="GUIDED HANDOUT")
callout(
    d, "Warm-up",
    "Use six steel coupons to build a 95% confidence interval on mean yield strength. "
    "This teaches the interval mechanics before the paired deck comparison.",
    fill="EEF3F8", edge="6F8FAF",
)
table(d, [
    ["Coupon", "Yield strength (ksi)"],
    ["CP-01", "47.8"], ["CP-02", "49.1"], ["CP-03", "50.4"],
    ["CP-04", "48.7"], ["CP-05", "51.2"], ["CP-06", "49.8"],
], widths=[2.8, 2.8], size=9.0)
h2(d, "Build the interval")
table(d, [
    ["Quantity", "Student value"],
    ["n", ""], ["sample mean", ""], ["sample standard deviation", ""],
    ["standard error = s / √n", ""], ["t* for 95%, df = 5", ""],
    ["margin = t* × SE", ""], ["95% confidence interval", ""],
], widths=[3.6, 3.3], size=8.4, zebra=None)
callout(
    d, "Interpretation stem",
    "A 95% confidence interval is a range produced by a method that captures the true "
    "population mean in about 95% of repeated samples—not a 95% probability assigned to this "
    "fixed interval after it is calculated.",
    fill="FFF6E5", edge="F2C230",
)
save(d, os.path.join(OUT, "H10-01-coupon-interval-warmup.docx"))


# ========================================================= H10-02 ==========
d = course_doc("M10", "Paired Load-Test Evidence Guide", kind="DATA GUIDE")
para(
    d, "The comparison uses the same eight instrumented locations and three matched truck passes "
    "per location in each year. Analyze location means as eight paired observations.", after=8,
)
table(d, [
    ["File / field", "Meaning", "Unit / role"],
    ["loadtest_2019_2027.csv", "48 pass-level records: 8 locations × 2 years × 3 passes", "source"],
    ["analysis_strain_microstrain", "temperature-corrected response under the reference truck", "µε"],
    ["reference_load_kips", "matched reference test load", "80.0 kips"],
    ["lane_offset_ft / speed_mph", "matched process controls", "0.0 ft / 5.0 mph"],
    ["M10-paired-location-summary.csv", "year means, paired change, and repeatability SD", "analysis"],
], widths=[2.2, 3.65, 1.05], size=7.8)
h2(d, "Noise audit")
table(d, [
    ["Source", "How M10 checks or limits it", "What remains"],
    ["Measurement repeatability", "Three passes; within-test SD reported", ""],
    ["Location-to-location variation", "Same-location pairing", ""],
    ["Truck load / lane / speed", "Matched controls in both years", ""],
    ["Temperature response", "Correction already applied and recorded", ""],
    ["Sampling uncertainty", "Standard error and t interval on 8 changes", ""],
], widths=[1.7, 3.4, 1.8], size=7.7, zebra=None)
callout(
    d, "Boundary",
    "These controls make a small between-year signal more credible. They do not identify a "
    "damage mechanism or prove the whole deck deteriorated uniformly.",
    fill="FFF6E5", edge="F2C230",
)
save(d, os.path.join(OUT, "H10-02-paired-load-test-guide.docx"))


# ========================================================= H10-03 ==========
d = course_doc("M10", "Signal or Noise?", kind="PAIRED-INTERVAL WORKSHEET")
callout(
    d, "Decision question",
    "Did mean strain at the eight matched locations increase beyond the noise visible in this "
    "test—or is zero change still plausible at the stated confidence level?",
    fill="FFF6E5", edge="F2C230",
)
h2(d, "A — Pair before you summarize")
table(d, [
    ["Location", "2019 mean", "2027 mean", "Change (2027 − 2019)"],
    ["G1", "", "", ""], ["G2", "", "", ""], ["G3", "", "", ""],
    ["G4", "", "", ""], ["G5", "", "", ""], ["G6", "", "", ""],
    ["G7", "", "", ""], ["G8", "", "", ""],
], widths=[1.2, 1.65, 1.65, 2.4], size=7.8, zebra=None)
h2(d, "B — Interval on the eight changes")
table(d, [
    ["Quantity", "95% calculation", "99% calculation"],
    ["mean change", "", ""], ["standard deviation", "", ""],
    ["standard error", "", ""], ["t multiplier (df = 7)", "", ""],
    ["margin", "", ""], ["interval", "", ""], ["Does zero remain plausible?", "", ""],
], widths=[2.25, 2.3, 2.3], size=7.8, zebra=None)
h2(d, "C — Defend the claim")
numbers(d, [
    "Compare the size of the mean change with repeatability noise and location-to-location spread.",
    "Explain why the 95% and 99% intervals support different levels of caution.",
    "Write one sentence that preserves both the signal and its uncertainty.",
], size=9.0)
ruled_lines(d, 3)
save(d, os.path.join(OUT, "H10-03-signal-v-noise-worksheet.docx"))


# ========================================================= H10-04 ==========
d = course_doc("M10", "Intervals, Confidence, and Significance", kind="REFERENCE")
table(d, [
    ["Concept", "Working meaning", "M10 use"],
    ["Standard error", "Estimated sample-to-sample variation of a mean", "SE = s / √n for 8 paired changes"],
    ["t multiplier", "Critical value reflecting confidence level and degrees of freedom", "Larger at 99% than 95%"],
    ["Confidence interval", "estimate ± t* × SE", "Plausible values for mean paired change"],
    ["Confidence level", "Long-run capture rate of the interval method", "Changing it changes interval width"],
    ["Significance / p-value", "Compatibility of the data with a stated null model", "Not the probability the claim is true"],
], widths=[1.35, 3.15, 2.4], size=7.7)
h2(d, "Language audit")
table(d, [
    ["Avoid", "Use instead"],
    ["“p = 0.04 means a 96% chance deterioration is real.”",
     "“If the mean change were zero under the model, a result this extreme would be uncommon.”"],
    ["“Significant means important or confirmed.”",
     "“The 95% interval excludes zero, but the estimated change is small and uncertain.”"],
    ["“The 99% result contradicts the 95% result.”",
     "“The higher confidence level demands a wider interval and supports more caution.”"],
], widths=[3.4, 3.5], size=8.0)
save(d, os.path.join(OUT, "H10-04-concepts-and-language.docx"))


# ========================================================= H10-05 / HW5 =====
d = course_doc("M10", "HW5 · Peak-Strain Interval Audit", kind="ASSIGNMENT")
callout(
    d, "HW3 CALLBACK IN HW5",
    "Build an interval on mean daily peak strain from the previously issued feed file. First "
    "audit timestamp uniqueness. A duplicated block makes the sample look larger than it is and "
    "can make the interval too narrow.",
    fill="EEF3F8", edge="6F8FAF",
)
h2(d, "Required work")
numbers(d, [
    "Preserve the original row count and count unique timestamps.",
    "Identify exact duplicated timestamps; document the rule used to retain one record.",
    "Calculate mean, standard deviation, n, standard error, and a 95% t interval before cleaning.",
    "Repeat after removing exact duplicate records.",
    "Compare interval widths and explain why duplicate rows are not independent new evidence.",
    "Submit Note v2 with a number and interval: claim, check, result.",
], size=9.1)
h2(d, "Ten project hours")
table(d, [
    ["Action", "Hours"],
    ["Accept the feed as delivered", "0"],
    ["Spot-check timestamp uniqueness", "1"],
    ["Verify the full feed against the source / data rules", "2"],
    ["Recompute independently after a documented cleaning step", "4"],
    ["Ask Wes; answer arrives next meeting", "1"],
], widths=[5.8, 1.1], size=8.2)
callout(
    d, "Fairness",
    "The callback asks for a correction, not a retroactive penalty. If your earlier file was "
    "already clean, use the supplied callback copy and document the comparison.",
    fill="FFF6E5", edge="F2C230",
)
save(d, os.path.join(OUT, "H10-05-HW5-peak-strain-interval.docx"))


# ========================================================= H10-06 ==========
d = course_doc("M10", "Decision Record · Unit 2 Note v2", kind="HAND-IN")
callout(
    d, "Unit 2 standard",
    "Three lines: claim, check, result. From M10 onward, include a number with its spread or "
    "interval. Diane's yes-or-no request does not erase uncertainty.",
    fill="EEF3F8", edge="6F8FAF",
)
table(d, [
    ["Line", "Student record"],
    ["CLAIM — What FOREMAN says the 6% increase proves", ""],
    ["CHECK — Paired estimate, confidence interval, and noise/control audit", ""],
    ["RESULT — Supported conclusion with magnitude and confidence boundary", ""],
], widths=[2.8, 4.1], size=8.5, zebra=None)
h2(d, "Decision log")
table(d, [
    ["Item", "Action chosen", "Hours", "Evidence checked", "Accepted unverified"],
    ["M10 deck-change claim / HW5 plan", "", "", "", ""],
], widths=[1.55, 1.25, .55, 1.8, 1.75], size=7.7, zebra=None)
save(d, os.path.join(OUT, "H10-06-note-v2-and-decision-log.docx"))


# =============================================================== KEY ========
d = course_doc("M10", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
callout(
    d, "Gated conclusion",
    "The matched-location data support a small positive mean change at 95% confidence, but the "
    "99% interval includes zero. The defensible claim is “probably a small real change,” not "
    "confirmed deterioration or a 96% probability that deterioration occurred.",
    fill="FFF1E8", edge="F26B1D",
)
h2(d, "Coupon warm-up")
table(d, [
    ["n", "Mean", "SD", "SE", "t* (95%, df 5)", "95% CI"],
    [coupon["n"], f"{float(coupon['mean']):.2f} ksi",
     f"{float(coupon['sd']):.2f}", f"{float(coupon['standard_error']):.2f}",
     coupon["t_multiplier"],
     f"[{float(coupon['lower']):.2f}, {float(coupon['upper']):.2f}] ksi"],
], widths=[.55, 1.05, .85, .85, 1.5, 2.1], size=8.0)
h2(d, "Paired deck comparison")
table(d, [
    ["Level", "Mean change", "SD", "SE", "t*", "Interval", "Zero?"],
    ["95%", "6.00 µε", f"{float(paired95['sd']):.2f}",
     f"{float(paired95['standard_error']):.2f}", paired95["t_multiplier"],
     f"[{float(paired95['lower']):.2f}, {float(paired95['upper']):.2f}] µε", "No"],
    ["99%", "6.00 µε", f"{float(paired99['sd']):.2f}",
     f"{float(paired99['standard_error']):.2f}", paired99["t_multiplier"],
     f"[{float(paired99['lower']):.2f}, {float(paired99['upper']):.2f}] µε", "Yes"],
], widths=[.6, 1.0, .65, .65, .6, 2.2, .7], size=7.8)
d.add_picture(os.path.join(OUT, "M10-paired-changes.png"), width=Inches(6.75))
h2(d, "Signal versus noise")
bullets(d, [
    "Same-location pairing removes much of the stable location-to-location baseline variation.",
    "Three passes show repeatability noise near one microstrain—smaller than the six-microstrain mean change.",
    "Matched truck load, lane, speed, and recorded temperature correction reduce process explanations.",
    "The eight paired changes still vary widely; standard error and the interval carry that uncertainty.",
    "A positive average strain change is evidence of changed response, not by itself a diagnosed damage mechanism.",
])
h2(d, "Model Note v2")
callout(
    d, "CLAIM / CHECK / RESULT",
    "CLAIM — FOREMAN says a 6% increase and p = 0.04 confirm deck deterioration. "
    "CHECK — I calculated the interval on eight same-location changes and compared the change "
    "with repeatability and matched process controls. RESULT — mean strain increased 6.0 µε; "
    f"the 95% CI is [{float(paired95['lower']):.2f}, {float(paired95['upper']):.2f}] µε, "
    f"while the 99% CI is [{float(paired99['lower']):.2f}, {float(paired99['upper']):.2f}] µε. "
    "The evidence supports probably a small real change, not confirmed deterioration.",
    fill="EEF3F8", edge="6F8FAF",
)
h2(d, "Teaching boundaries")
bullets(d, [
    "Keep the reveal closed until students commit H10-03.",
    "Do not convert a p-value into the probability that the claim is true.",
    "Do not equate statistical significance with engineering importance or a damage diagnosis.",
    "Do not introduce any Exam 1 scenario details.",
    "Deck notes and the run-of-day use the revised M10 Cloud-PASS canon SAY.",
])
save(d, os.path.join(OUT, "KEY-M10-answer-key.docx"))


# ======================================================= FILE INDEX =========
index_out = os.path.join(BUILD, "M10-INSTRUCTOR")
d = course_doc("M01 – M10", "What is in this pack", kind="FILE INDEX")
para(
    d, "Folders are in teaching order. M10 is folder 14 after the M09 pack and separates a "
    "small paired deterioration signal from measurement, process, and sampling noise.",
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
]
table(d, [["Folder", "Purpose"]] + folders, widths=[2.75, 4.15], size=7.4)
h2(d, "14-M10-deterioration-v-noise")
table(d, [
    ["File", "What it is"],
    ["M10-student.pptx", "Spoiler-safe concepts and interval hunt with Cloud-PASS canon SAY"],
    ["M10-instructor-reveal.pptx", "Gated 95%/99% comparison and bounded claim"],
    ["FOREMAN-M10-deterioration-claim.docx", "Designed p-value and significance overclaim"],
    ["H10-01-coupon-interval-warmup.docx", "Six-coupon guided t interval"],
    ["H10-02-paired-load-test-guide.docx", "Data dictionary and measurement/process-noise audit"],
    ["H10-03-signal-v-noise-worksheet.docx", "Paired-change interval worksheet"],
    ["H10-04-concepts-and-language.docx", "Five concept definitions and safe language"],
    ["H10-05-HW5-peak-strain-interval.docx", "Duplicate-timestamp callback assignment"],
    ["H10-06-note-v2-and-decision-log.docx", "Claim/check/result with interval"],
    ["coupons.csv + loadtest_2019_2027.csv", "Warm-up and pass-level source data"],
    ["M10-paired-location-summary.csv", "Eight paired location means and repeatability SD"],
    ["M10-interval-summary.csv", "Deterministic 95% and 99% calculations"],
    ["M10-test-control-check.csv", "Matched process-control record"],
    ["KEY-M10-answer-key.docx", "Instructor-only calculations and boundaries"],
    ["../00-INSTRUCTOR/source-notes/M10-story-SAY.md", "Revised M10 Cloud-PASS canon story and SAY source"],
], widths=[3.2, 3.7], size=7.3)
save(d, os.path.join(index_out, "FILE-INDEX.docx"))
print("M10 handouts and index done")
