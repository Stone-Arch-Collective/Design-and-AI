"""M08 spoiler-safe student deck and gated instructor reveal with canon Oli SAY."""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

OUT = os.path.join(ROOT, "build", "M08")
with open(os.path.join(OUT, "M08-regression-summary.csv"), newline="") as f:
    models = {row["model"]: row for row in csv.DictReader(f)}


def add_canon_notes(prs, notes):
    if len(prs.slides) != len(notes):
        raise ValueError(f"notes ({len(notes)}) != slides ({len(prs.slides)})")
    for slide, note in zip(prs.slides, notes):
        slide.notes_slide.notes_text_frame.text = (
            "OLI CANON SAY — Cloud hard-review PASS.\n\n"
            + note.strip()
        )


# ======================================================= STUDENT DECK =======
prs = deck()
title_slide(prs, "Meeting 08  ·  Unit 2: Doubt", "A strong fit can still mislead.",
            "Correlation, regression, mechanism, and a hidden driver",
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

student_notes = [
    "TITLE — M08: “It is spring.” Students investigate whether a strong fitted relationship supports FOREMAN’s damage claim.",
    "INBOX — FOREMAN reports that midspan strain has risen steadily since February 1, R-squared 0.87 against date, indicating progressive structural deterioration. Diane Halvorsen, PE: “0.87 sounds high. Put it in the report.” Wes Tanaka, EIT is drafting and distracted under schedule pressure; he is not the discoverer.",
    "HUNT — Students are the hunters. They reproduce the date plot, compare it with the weather record, identify the mechanism driving strain, and prepare HW4. Do not disclose the result before they work.",
    "TEACH TRANSITION — Concepts: scatter plot, correlation coefficient, linear regression, R-squared, correlation versus causation, and spurious correlation.",
    "TEACH — Explain how a scatter plot displays the strain-versus-date pairs before a line is fitted.",
    "TEACH — Explain correlation coefficient as linear association. Keep correlation separate from causation.",
    "TEACH — Demonstrate fitting a line in a spreadsheet. Connect the slope to its units.",
    "TEACH — Explain R-squared as model fit. A high R-squared is not proof of cause.",
    "TEACH — Keep the question open: a fitted pattern is not yet a mechanism.",
    "TEACH — Explain spurious correlation as an association that misleads about the damage claim.",
    "LAB TRANSITION — Students receive feed.csv and weather_station.csv. Do not solve the trend for them.",
    "LAB — Student task: plot strain versus date using feed.csv and fit the line in a spreadsheet.",
    "LAB — Student task: plot strain versus air temperature using weather_station.csv and fit the line. Students perform the join and comparison.",
    "LAB — Student task: identify the mechanism driving the strain, not just the pattern. Students find that temperature drives the calendar trend and strain; steel expands when it warms.",
    "LAB — Students set up the temperature correction and prepare the two-line reply. Preserve the boundary: this trend does not support progressive damage; the correction does not prove no damage.",
    "NOTE — Students write Note version 2: claim, check, result. Continue the form handed off at M07.",
    "CLOSE — Assign HW4: temperature-corrected strain trend plus a two-line reply to FOREMAN’s claim. Diane still wants the impressive R-squared in the county-facing report; students leave with the corrected note. Lightly hold rising measurement pressure without naming later concepts.",
]
add_canon_notes(prs, student_notes)
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

reveal_notes = [
    "REVEAL — Open only after students complete the hunt and commit H8-02 and Note version 2.",
    "REVEAL — Confirm the date-model result. FOREMAN’s fitted line is reproducible; the progressive-deterioration interpretation is not supported.",
    "REVEAL — Confirm that strain has a strong relationship with air temperature. Students, not Diane or Wes, identify the thermal-expansion mechanism.",
    "REVEAL — Temperature drives the calendar trend and the measured strain: date → warming → steel expansion → measured strain.",
    "REVEAL — Confirm the temperature-corrected result. Use “no meaningful date trend in this extract,” not “proof of no damage.”",
    "REVEAL — FOREMAN’s designed error is reading the seasonal temperature effect as structural damage and offering high R-squared as proof of cause.",
    "REVEAL — Compare student replies. The supported conclusion is that this uncorrected trend does not establish progressive structural deterioration.",
    "CLOSE — HW4 stays at M08: temperature-corrected strain trend plus a two-line reply. Continue Note version 2 from M07. Diane remains in believer mode and students retain the corrected record.",
]
add_canon_notes(rev, reveal_notes)
save(rev, os.path.join(OUT, "M08-instructor-reveal.pptx"))
