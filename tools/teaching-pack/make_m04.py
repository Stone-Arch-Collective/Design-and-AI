"""M04 handouts: One number, and what it leaves out."""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M04")
C = FACTS["m04"]
os.makedirs(OUT, exist_ok=True)
shutil.copy(os.path.join(BUILD, "data", "cores_2027.csv"),
            os.path.join(OUT, "cores_2027.csv"))
print("  wrote M04/cores_2027.csv")

# ============================================================ H4-01 ==========
d = acme_doc(subtitle="Internal Memorandum")
memo_block(d, to="You", frm="Diane Halvorsen, PE",
           date="Thursday, February 11, 2027",
           re_="One number for the deck cores")
para(d, "The laboratory returned the 24 concrete core results. The county briefing has room "
        "for one number, not a spreadsheet. Give me the number that best describes the deck.",
     after=8)
para(d, "FOREMAN says the concrete is adequate. I need a short answer I can repeat, and I need "
        "to know what that short answer leaves out.", after=10)
h2(d, "What I need before noon")
numbers(d, [
    "One number that describes the center of the 24 reported strengths.",
    "One number that describes how far the strengths spread around that center.",
    "A count of results below the 4,500 psi project comparison value.",
    "Three sentences: the one-number answer, the qualification, and what these 24 cores cannot "
    "establish about the whole deck.",
])
h2(d, "Your six project hours")
table(d, [
    ["Option", "Hours", "What it buys"],
    ["Accept FOREMAN's adequacy sentence", "0", "A fast answer; no independent check"],
    ["Recompute the mean", "1", "Center checked"],
    ["Compute sample SD and CV", "2", "Spread on an absolute and relative scale"],
    ["Count and identify results below 4,500 psi", "1", "The low tail stays visible"],
    ["Plot all 24 values", "1", "A shape Diane can see"],
    ["Review drill locations and sampling limits", "1", "What the sample can represent"],
], widths=[3.0, 0.75, 3.15], align=["l", "c", "l"], size=8.8)
callout(d, "A boundary",
        "The 4,500 psi value is a project comparison for this exercise, not a complete code "
        "acceptance rule. Describe the data. Do not turn one classroom threshold into an "
        "engineering disposition.", fill="FFF6E5", edge="F2C230")
handwriting(d, "One number is the brief. The spread is the part I cannot afford to lose. — D.H.")
save(d, os.path.join(OUT, "H4-01-diane-one-number-ask.docx"))

# ============================================================ H4-02 ==========
d = course_doc("M04", "Spreadsheet Hunt — Center, Spread, and Scale",
               kind="IN-CLASS WORKSHEET")
para(d, "Open cores_2027.csv. Work from the 24 strength_psi values. Do not begin with "
        "FOREMAN's conclusion; begin with the data.", after=8)
callout(d, "The hunt",
        "You are looking for two summaries that can both be mathematically correct while "
        "supporting very different stories. Do not decide which story matters until every pair "
        "has center, spread, and the low-result count.", fill="EEF3F8", edge="6F8FAF")
h2(d, "Part A — Name the data")
table(d, [
    ["Question", "Your answer"],
    ["What is one row (the observational unit)?", ""],
    ["Which column is the quantitative variable?", ""],
    ["Which columns describe where the sample came from?", ""],
    ["Are these 24 rows a sample or the full deck population?", ""],
], widths=[4.6, 2.3], zebra=None)
h2(d, "Part B — Compute")
table(d, [
    ["Statistic", "Spreadsheet expression", "Your result"],
    ["Count, n", "=COUNT(range)", ""],
    ["Mean", "=AVERAGE(range)", ""],
    ["Sample variance", "=VAR.S(range)", ""],
    ["Sample standard deviation", "=STDEV.S(range)", ""],
    ["Coefficient of variation", "=STDEV.S(range)/AVERAGE(range)", ""],
    ["Minimum and maximum", "=MIN(range), =MAX(range)", ""],
    ["Count below 4,500 psi", '=COUNTIF(range,"<4500")', ""],
], widths=[2.15, 2.85, 1.9], size=8.8, zebra=None)
para(d, "Format CV as a percentage. Keep enough working digits to reproduce your result; round "
        "the reported mean and SD to sensible precision.", size=9, italic=True, color=GREY)
h2(d, "Part C — Put the spread back into the sentence")
numbers(d, [
    "Write a sentence using only the mean. What would a reader reasonably conclude?",
    "Write a second sentence that adds SD or CV and the below-comparison count.",
    "What changed when the individual results returned to the story?",
    "What can 24 shoulder cores say about the sampled locations? What can they not establish "
    "about every part of the deck?",
])
save(d, os.path.join(OUT, "H4-02-spreadsheet-hunt.docx"))

# ============================================================ H4-03 ==========
d = foreman_doc("Deck Core Strength — Executive Summary",
                generated="2027-02-11 07:18 CST")
para(d, "Automated descriptive summary of 28-day compressive strength results for 24 cores "
        "from the Otter Bend bridge deck. Source: cores_2027.csv.", size=9.5, after=8)
p = para(d, "", after=10)
box(p, fill="FFF1E8", color="F26B1D", size=8, space=8)
run(p, "RESULT   ", 9.5, bold=True, font=HEAD_FONT, color=STICKER, caps=True, space=0.8)
run(p, f"ADEQUATE. Mean core strength is {C['mean_psi']:,.0f} psi, exceeding the "
       f"{C['comparison_psi']:,} psi project value by "
       f"{C['mean_psi'] - C['comparison_psi']:,.0f} psi. No further statistical review is "
       "required. Confidence 94%.", 10, bold=True)
h2(d, "Executive metric", color=REBAR)
table(d, [
    ["Statistic", "Value"],
    ["Core results", str(C["n"])],
    ["Mean compressive strength", f"{C['mean_psi']:,.0f} psi"],
    ["Project comparison value", f"{C['comparison_psi']:,} psi"],
    ["Mean margin", f"+{C['mean_psi'] - C['comparison_psi']:,.0f} psi"],
    ["Status", "ADEQUATE"],
], widths=[3.6, 3.3], align=["l", "r"], head_fill="2B2F36")
h2(d, "Recommendation", color=REBAR)
para(d, "Use the mean strength as the single representative value in the county briefing. "
        "Individual results have been retained in the source CSV but are not material to the "
        "executive conclusion.", size=10, after=10)
mono_block(d, [
    "fm-analytics-4.2  |  24 values  |  0.3 s  |  no human review requested",
])
save(d, os.path.join(OUT, "H4-03-foreman-core-summary.docx"))

# ============================================================ H4-04 ==========
d = course_doc("M04", "Three-Sentence Brief to Diane", kind="HAND-IN")
para(d, "Diane asked for one number. Give it to her without making it carry a claim it cannot "
        "support. Use values you computed from cores_2027.csv.", after=8)
table(d, [
    ["Sentence", "Required job"],
    ["1 — Center", "Give the requested one-number summary, with units."],
    ["2 — Spread", "Give SD or CV and the count below 4,500 psi; explain why it changes the story."],
    ["3 — Scope", "State what this sample can and cannot establish about the whole deck."],
], widths=[1.35, 5.55], size=9.2)
for label in ("Sentence 1", "Sentence 2", "Sentence 3"):
    h2(d, label, before=10)
    for _ in range(2):
        p = para(d, "", after=10, before=2)
        bottom_rule(p, "C9CFD6", 6)
h2(d, "How I know this is right — note v1")
para(d, "In one sentence, name the check you actually performed. Do not name a check you "
        "intended to perform.", size=9.5, after=6)
for _ in range(2):
    p = para(d, "", after=10, before=2)
    bottom_rule(p, "C9CFD6", 6)
callout(d, "Grading",
        "The record and reasoning are graded, not whether Diane likes the sentence. Hours are "
        "not points.", fill="EEF3F8", edge="6F8FAF")
save(d, os.path.join(OUT, "H4-04-three-sentence-brief.docx"))

# ============================================================ KEY ============
d = course_doc("M04", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
callout(d, "The reveal",
        "FOREMAN's mean is correct. Its conclusion is not supported by the mean alone. Wait for "
        "students to identify the summary that makes the low results disappear before showing "
        "the table below.", fill="FFF1E8", edge="F26B1D")
h2(d, "Descriptive statistics")
table(d, [
    ["Statistic", "Instructor value"],
    ["n", str(C["n"])],
    ["Mean", f"{C['mean_psi']:,.2f} psi"],
    ["Sample variance", f"{C['variance_psi2']:,.2f} psi²"],
    ["Sample standard deviation", f"{C['sample_sd_psi']:,.2f} psi"],
    ["Sample CV", f"{C['sample_cv_pct']:.2f}%"],
    ["Population SD (contrast only)", f"{C['population_sd_psi']:,.2f} psi"],
    ["Population CV (contrast only)", f"{C['population_cv_pct']:.2f}%"],
    ["Range", f"{C['minimum_psi']:,}–{C['maximum_psi']:,} psi "
              f"({C['range_psi']:,} psi wide)"],
    [f"Below {C['comparison_psi']:,} psi", f"{C['below_comparison']} of {C['n']}"],
], widths=[3.6, 3.3], align=["l", "r"], size=9)
h2(d, "The five low results")
para(d, "C-01 3,820 psi; C-02 4,050 psi; C-03 4,200 psi; C-04 4,380 psi; "
        "C-05 4,470 psi.", font=MONO_FONT, size=9.5)
bullets(d, [
    ("Mean story: ", "5,003.75 psi is 503.75 psi above the project comparison. That arithmetic "
     "is correct."),
    ("Spread story: ", "sample SD is 554.67 psi and CV is 11.09%; five of 24 values sit below "
     "4,500 psi. Center does not erase tails."),
    ("Scope story: ", "all 24 cores came from accessible shoulder locations. They describe "
     "those tested cores; they are not the full deck population or a representative sample of "
     "every deck region."),
    ("Engineering boundary: ", "do not teach that any individual value below 4,500 psi proves "
     "failure, or that the mean proves adequacy. The exercise teaches descriptive statistics, "
     "not a complete concrete acceptance standard."),
])
h2(d, "A strong three-sentence response")
callout(d, "Model — do not project before the hunt",
        f"The 24 tested cores average {C['mean_psi']:,.0f} psi. Their sample standard deviation "
        f"is {C['sample_sd_psi']:,.0f} psi (CV {C['sample_cv_pct']:.1f}%), and "
        f"{C['below_comparison']} of {C['n']} results fall below the 4,500 psi project "
        "comparison, so the mean alone hides consequential spread. Because every core was "
        "drilled from an accessible shoulder location, these results describe the sampled "
        "locations but do not establish the condition of the entire deck.",
        fill="EEF3F8", edge="6F8FAF")
h2(d, "Sample versus population")
para(d, "Use STDEV.S and VAR.S because the 24 cores are a sample from a larger physical deck. "
        "STDEV.P is useful only as a contrast: it treats the file as the entire population of "
        "interest and produces the smaller value shown above. The formula choice encodes the "
        "claim being made.", after=8)
h2(d, "Timing, 75 minutes")
table(d, [
    ["Min", "What happens"],
    ["0–8", "Diane's one-number ask and FOREMAN's 94%-confident adequacy sentence. Take a vote."],
    ["8–23", "Data sets, variables, mean, variance, SD, and why units change at variance."],
    ["23–33", "CV and sample versus population. Set up formulas; give no computed answers."],
    ["33–55", "Spreadsheet hunt in pairs. Center, spread, low count, and sampling scope."],
    ["55–67", "Reveal the strip plot and statistics. Compare the mean-only and spread-aware stories."],
    ["67–73", "Students write the three-sentence brief and note v1."],
    ["73–75", "Mask off: Diane is wrong to ask for only one number and right to need brevity."],
], widths=[0.85, 6.05], size=9)
save(d, os.path.join(OUT, "KEY-M04-answer-key.docx"))
print("M04 done")
