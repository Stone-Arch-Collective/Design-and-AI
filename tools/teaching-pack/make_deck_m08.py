"""M08 spoiler-safe student deck and gated instructor reveal.

Oli story/SAY is intentionally not present. Every notes pane carries an explicit
paste hook so the approved text can be folded without rebuilding slide content.
"""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

OUT = os.path.join(ROOT, "build", "M08")
with open(os.path.join(OUT, "M08-regression-summary.csv"), newline="") as f:
    models = {row["model"]: row for row in csv.DictReader(f)}


def add_pending_notes(prs, hooks):
    if len(prs.slides) != len(hooks):
        raise ValueError(f"notes ({len(hooks)}) != slides ({len(prs.slides)})")
    for slide, hook in zip(prs.slides, hooks):
        slide.notes_slide.notes_text_frame.text = (
            "OLI STORY/SAY STATUS: PENDING CLOUD PASS — DO NOT TREAT THIS HOOK AS CANON SAY.\n\n"
            "PASTE APPROVED SAY HERE, preserving the instructional action below.\n\n"
            + hook.strip()
        )


# ======================================================= STUDENT DECK =======
prs = deck()
title_slide(prs, "Meeting 08  ·  Unit 2: Doubt", "A strong fit can still mislead.",
            "Correlation, regression, mechanism, and a temperature confound",
            "Thursday, February 25, 2027  ·  SEIS 201")

s, y = content(prs, "The interim finding", "FOREMAN modeled G4 strain against date")
speaker_card(s, .72, y + .15, 11.87, 1.85, "FOREMAN · FINAL OUTPUT", [
    f"Midspan strain rises with date. R² = {float(models['strain ~ date_index']['r_squared']):.2f}.",
    "Conclusion entered in the draft: progressive structural deterioration."
], machine=True, body_size=18)
card(s, .72, y + 2.3, 11.87, 1.45, "DECISION", [
    "Does this relationship support a damage claim—or is date standing in for something else?"
], tint=CREAM, edge=GOLD, body_size=17)

s, y = content(prs, "The hunt", "Reproduce · compare · explain · correct")
card(s, .72, y + .2, 2.75, 3.7, "1  REPRODUCE", [
    "Plot strain against date", "Fit the reported line"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 3.68, y + .2, 2.75, 3.7, "2  COMPARE", [
    "Join weather", "Plot strain against temperature"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)
card(s, 6.64, y + .2, 2.75, 3.7, "3  EXPLAIN", [
    "Name a physical mechanism", "Set the causal boundary"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 9.60, y + .2, 2.99, 3.7, "4  CORRECT", [
    "Remove temperature-linked strain", "Retest the date trend"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

section(prs, "1", "See the relationship",
        "A scatter plot comes before a coefficient")

s, y = content(prs, "A scatter plot shows paired observations")
bullet_list(s, .95, y + .2, 11.35, 3.7, [
    ("Direction  ", "positive, negative, or no clear linear pattern."),
    ("Form  ", "linear, curved, clustered, or changing spread."),
    ("Strength  ", "how tightly points follow the pattern."),
    ("Exceptions  ", "outliers, gaps, or groups that need explanation."),
], size=18, dot=GIRDER_LT)
card(s, .72, y + 4.1, 11.87, 1.3, "FIRST MOVE", [
    "Plot before interpreting a fitted statistic."
], tint=CREAM, edge=GOLD, body_size=15)

s, y = content(prs, "Correlation measures linear association",
               "It does not identify the mechanism")
card(s, .72, y + .2, 5.85, 3.75, "CORRELATION COEFFICIENT r", [
    "Ranges from −1 to +1", "Sign gives direction", "Magnitude gives linear strength"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.75, "NOT INCLUDED", [
    "Proof of cause", "Protection from a hidden variable", "Engineering significance"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

s, y = content(prs, "Linear regression fits a prediction line")
card(s, .72, y + .2, 5.85, 3.7, "MODEL", [
    "response = intercept + slope × predictor",
    "Slope: expected response change per predictor unit"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.7, "CHECK", [
    "Units", "Range represented", "Residual pattern", "Variables omitted"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

s, y = content(prs, "R² describes fit—not cause")
card(s, .72, y + .2, 5.85, 3.75, "R² CAN SAY", [
    "How much response variation is described by this fitted model in this sample"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=19)
card(s, 6.72, y + .2, 5.87, 3.75, "R² CANNOT SAY", [
    "The predictor caused the response", "The model is complete", "Damage is progressing"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

statement(prs, "A model can fit the observed points\nand still tell the wrong story.",
          "The causal claim needs a mechanism and competing explanations.", dark=True, size=43)

s, y = content(prs, "Spurious does not mean imaginary")
card(s, .72, y + .2, 5.85, 3.75, "REAL ASSOCIATION", [
    "Date and strain can move together", "The fitted line can be computed correctly"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.75, "MISLEADING CLAIM", [
    "Date may proxy another variable", "The association does not establish deterioration"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=18)

section(prs, "2", "Hunt the confound",
        "Use the weather record, then name the mechanism")

activity(prs, "Reproduce FOREMAN's model", 8, [
    "Open feed.csv and plot corrected strain against date_index.",
    "Fit a linear trendline; record slope and R² in H8-02.",
    "Write one sentence the model supports without using a causal verb.",
], note="A reproduced statistic can still support an overclaimed interpretation.")

activity(prs, "Join the weather record", 10, [
    "Use timestamp_cst to join feed.csv and weather_station.csv.",
    "Check row counts, unmatched timestamps, duplicates, and °C units.",
    "Plot strain against air_temperature_c; fit the second line.",
    "Compare direction, slope units, and R² with the date model.",
], note="A clean join is part of the evidence, not clerical overhead.")

activity(prs, "Name the mechanism; set the boundary", 8, [
    "Explain what warming does to steel and a restrained sensor location.",
    "Draw date → temperature → measured strain on H8-03.",
    "State why the date fit alone cannot distinguish thermal response from damage.",
    "List evidence still needed before claiming structural deterioration.",
], note="A second correlation becomes useful when it has a plausible physical mechanism.")

activity(prs, "Set up the correction", 4, [
    "Use the temperature model to calculate predicted strain.",
    "Residual = observed strain − predicted temperature-linked strain.",
    "Plot the residual against date and identify the claim that test can support.",
], note="Complete the full calculation in HW4; do not claim that one correction proves no damage.")

s, y = content(prs, "Write Unit 2 Note v2", "Claim · check · result")
card(s, .72, y + .2, 3.75, 3.65, "CLAIM", [
    "State FOREMAN's exact deterioration inference."
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)
card(s, 4.79, y + .2, 3.75, 3.65, "CHECK", [
    "Name the weather join, model comparison, and mechanism."
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 8.86, y + .2, 3.75, 3.65, "RESULT", [
    "Bound what the uncorrected trend can support."
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

closer(prs, [
    ("HAND IN", "H8-02 regression hunt and H8-05 Note version 2."),
    ("ASSIGNED", "HW4: temperature-corrected strain trend."),
    ("RECORD", "Project-hour choice and anything accepted unverified."),
    ("BOUNDARY", "This meeting tests the trend claim; it does not settle bridge condition."),
], title="Before the gated reveal")

student_hooks = [
    "TITLE HOOK — Introduce M08 and Unit 2's next designed error. Preserve the distinction between a strong relationship and damage evidence.",
    "INBOX HOOK — Deliver the approved FOREMAN/Diane/Wes story beat here. Preserve: date-model R², deterioration overclaim, Diane in believer mode. Do not add later bearing-wear or exam details.",
    "HUNT HOOK — Frame the four student actions without disclosing temperature as the answer before the hunt begins.",
    "TEACH TRANSITION HOOK — Move from story evidence into scatter plots.",
    "TEACH HOOK — Ask students what they inspect before calculating a coefficient.",
    "TEACH HOOK — Define correlation coefficient and explicitly separate association from mechanism.",
    "TEACH HOOK — Connect slope units to an engineering interpretation.",
    "TEACH HOOK — State that R² is fit in a sample, not a causation score.",
    "TEACH HOOK — Invite an example of a fitted line that could still tell the wrong story.",
    "TEACH HOOK — Define spurious correlation as a misleading inference, not fabricated data.",
    "LAB TRANSITION HOOK — Open the investigation without naming the temperature mechanism.",
    "LAB A HOOK — Students reproduce FOREMAN's date model and write a noncausal description.",
    "LAB B HOOK — Release weather_station.csv. Require timestamp and unit checks before modeling.",
    "LAB C HOOK — After students see the temperature relationship, elicit the thermal expansion mechanism.",
    "LAB D HOOK — Set up residual correction as HW4's method; preserve the distinction between 'not evidence of damage' and 'proof of no damage.'",
    "NOTE HOOK — Students commit claim/check/result before the reveal.",
    "CLOSE HOOK — Assign HW4 here. Insert approved story close when available; do not preview later Unit 2 revelations.",
]
add_pending_notes(prs, student_hooks)
save(prs, os.path.join(OUT, "M08-student.pptx"))


# ======================================================== REVEAL DECK =======
rev = deck()
title_slide(rev, "Meeting 08  ·  Instructor reveal", "Date was carrying temperature.",
            "Open only after students commit the regression hunt",
            "M08 · Unit 2: Doubt")

s, y = content(rev, "FOREMAN reproduced the date fit—and overclaimed it")
picture(s, os.path.join(OUT, "M08-strain-v-date.png"), .85, y + .15, w=7.25)
card(s, 8.4, y + .4, 4.2, 2.9, "DATE MODEL", [
    f"Slope: {float(models['strain ~ date_index']['slope']):.2f} µε/day",
    f"R²: {float(models['strain ~ date_index']['r_squared']):.3f}",
    "Strong association", "Cause unresolved"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

s, y = content(rev, "Temperature explains the observed pattern")
picture(s, os.path.join(OUT, "M08-strain-v-temperature.png"), .85, y + .15, w=7.25)
card(s, 8.4, y + .4, 4.2, 2.9, "TEMPERATURE MODEL", [
    f"Slope: {float(models['strain ~ station_temperature_c']['slope']):.2f} µε/°C",
    f"R²: {float(models['strain ~ station_temperature_c']['r_squared']):.3f}",
    "Physical mechanism: thermal expansion"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)

s, y = content(rev, "The confound is a causal structure")
card(s, .72, y + .5, 3.3, 2.6, "DATE", [
    "Tracks seasonal progress"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
text(s, 4.15, y + 1.25, .7, .5, "→", size=36, color=STICKER, bold=True)
card(s, 4.8, y + .5, 3.3, 2.6, "AIR TEMPERATURE", [
    "Warms over the observed window"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=18)
text(s, 8.25, y + 1.25, .7, .5, "→", size=36, color=STICKER, bold=True)
card(s, 8.9, y + .5, 3.7, 2.6, "MEASURED STRAIN", [
    "Changes with thermal expansion and restraint"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)

s, y = content(rev, "After correction, the date trend disappears")
picture(s, os.path.join(OUT, "M08-residual-v-date.png"), .85, y + .15, w=7.25)
card(s, 8.4, y + .4, 4.2, 2.9, "RESIDUAL MODEL", [
    f"Slope: {float(models['temperature residual ~ date_index']['slope']):.2f} µε/day",
    f"R²: {float(models['temperature residual ~ date_index']['r_squared']):.3f}",
    "No meaningful date trend in this extract"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)

statement(rev, "The date trend is real.\nThe damage inference is not supported.",
          "Temperature correction changes the engineering claim.", dark=True, size=43)

s, y = content(rev, "Use a bounded correction")
speaker_card(s, .72, y + .2, 11.87, 2.65, "MODEL RESPONSE · NOT REQUIRED WORDING", [
    "The uncorrected G4 strain increases with date, but date tracks warming in this observation window.",
    "After modeling the temperature-linked response, the residual does not show a meaningful date trend; this evidence does not support progressive deterioration."
], body_size=17)
card(s, .72, y + 3.2, 11.87, 1.35, "DO NOT CLAIM", [
    "Temperature correction proves the bridge has no damage."
], tint=CREAM, edge=GOLD, body_size=15)

closer(rev, [
    ("HW4", "Complete the temperature correction and submit the corrected trend."),
    ("NOTE v2", "Claim, check, result—the mechanism belongs in the record."),
    ("HOURS", "Record what you checked and what remains unverified."),
    ("SCOPE", "No later bearing-wear or Exam details enter M08."),
], title="Close M08")

reveal_hooks = [
    "REVEAL TITLE HOOK — Open only after students commit H8-02 and Note v2.",
    "REVEAL HOOK — Confirm the date-model values. Separate reproducible calculation from unsupported causal interpretation.",
    "REVEAL HOOK — Confirm the temperature-model values and elicit the physical mechanism.",
    "REVEAL HOOK — Walk date → temperature → measured strain. Clarify that date is a proxy in this observed window.",
    "REVEAL HOOK — Show residual model. Use 'no meaningful trend in this extract,' not 'proof of no damage.'",
    "REVEAL HOOK — State the designed error: FOREMAN treated fit as proof of deterioration.",
    "MODEL RESPONSE HOOK — Compare student boundaries; accept equivalent evidence-based wording.",
    "CLOSE HOOK — Assign HW4 and collect Note v2. Approved Oli story close may be pasted here later.",
]
add_pending_notes(rev, reveal_hooks)
save(rev, os.path.join(OUT, "M08-instructor-reveal.pptx"))
