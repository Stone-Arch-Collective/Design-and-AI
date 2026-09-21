"""M09 spoiler-safe student deck and gated instructor reveal.

Oli story/SAY is intentionally absent. Notes panes carry explicit paste hooks
until the attached draft receives a Cloud pass.
"""
import csv
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

OUT = os.path.join(ROOT, "build", "M09")
with open(os.path.join(OUT, "fatigue_tests.csv"), newline="") as f:
    fatigue = list(csv.DictReader(f))
with open(os.path.join(OUT, "M09-random-samples-n8.csv"), newline="") as f:
    draws = list(csv.DictReader(f))

life = [int(row["cycles_to_crack"]) for row in fatigue]
mean_life = statistics.mean(life)
sd_life = statistics.stdev(life)
remaining = mean_life - 3_000_184
draw_means = [float(row["sample_mean_psi"]) for row in draws]


def add_pending_notes(prs, hooks):
    if len(prs.slides) != len(hooks):
        raise ValueError(f"notes ({len(hooks)}) != slides ({len(prs.slides)})")
    for slide, hook in zip(prs.slides, hooks):
        slide.notes_slide.notes_text_frame.text = (
            "M09 SAY STATUS: HOLD — CLOUD RE-CHECK PASS REQUIRED.\n\n"
            "PLACEHOLDER ONLY. Do not treat as canon dialogue.\n\n"
            + hook.strip()
        )


# ======================================================= STUDENT DECK =======
prs = deck()
title_slide(prs, "Meeting 09  ·  Unit 2: Doubt", "To the single cycle.",
            "Overconfidence, false precision, random sampling, and sampling variability",
            "Tuesday, March 2, 2027  ·  SEIS 201")

s, y = content(prs, "One planning number arrived", "FOREMAN turned scattered tests into a single-cycle answer")
speaker_card(s, .72, y + .15, 11.87, 1.9, "FOREMAN · FINAL ANSWER", [
    f"{remaining:,.0f} cycles remaining",
    "Model confidence: HIGH"
], machine=True, body_size=21)
card(s, .72, y + 2.35, 11.87, 1.45, "DECISION REQUEST", [
    "A concise planning value was requested. Which digits—and which claim—can the evidence support?"
], tint=CREAM, edge=GOLD, body_size=17)

s, y = content(prs, "The hunt", "Trace · compare · sample · report")
card(s, .72, y + .2, 2.75, 3.7, "1  TRACE", [
    "Reproduce the arithmetic", "Find every input's resolution"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 3.68, y + .2, 2.75, 3.7, "2  COMPARE", [
    "Measure test spread", "Mark unsupported digits"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)
card(s, 6.64, y + .2, 2.75, 3.7, "3  SAMPLE", [
    "Draw n = 8 at random", "Compare sample means"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 9.60, y + .2, 2.99, 3.7, "4  REPORT", [
    "Round to supported scale", "Keep limitations visible"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

section(prs, "1", "Precision is a claim",
        "Every retained digit says the evidence can resolve that place")

s, y = content(prs, "AI overconfidence can live in the format")
card(s, .72, y + .2, 5.85, 3.75, "WHAT YOU SEE", [
    "One exact-looking answer", "Many decimal places", "Confident label", "No range"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.75, "WHAT YOU MUST ASK", [
    "What sample?", "What spread?", "What input resolution?", "What transfer assumptions?"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)

s, y = content(prs, "False precision is unsupported granularity")
card(s, .72, y + .2, 5.85, 3.75, "ARITHMETIC PRECISION", [
    "Software can carry and print many digits", "The subtraction can be reproducible"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.75, "EVIDENCE PRECISION", [
    "Inputs have finite resolution", "Tests vary", "A model has assumptions and limits"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=18)

s, y = content(prs, "Significant figures preserve supported scale",
               "They are not a ritual of counting decimals")
bullet_list(s, .95, y + .2, 11.35, 3.7, [
    ("Trace  ", "the least-resolved input and the observed variability."),
    ("Retain  ", "digits needed to communicate the supported magnitude."),
    ("Drop  ", "digits that imply distinctions the evidence cannot make."),
    ("State  ", "uncertainty and model limitations; rounding cannot repair a weak basis."),
], size=18, dot=GIRDER_LT)
card(s, .72, y + 4.1, 11.87, 1.3, "TEST", [
    "Could a different plausible sample move the reported digit?"
], tint=CREAM, edge=GOLD, body_size=15)

s, y = content(prs, "A quantitative claim needs a statistical basis")
card(s, .72, y + .2, 3.75, 3.65, "DATA", [
    "Who or what was measured?", "How many?", "How selected?"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 4.79, y + .2, 3.75, 3.65, "VARIABILITY", [
    "How much do results differ?", "What resolution and spread are visible?"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)
card(s, 8.86, y + .2, 3.75, 3.65, "METHOD", [
    "How was the estimate formed?", "What assumptions connect test to claim?"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

statement(prs, "A calculator can return eight significant figures.\nThe evidence may support two or three.",
          "Correct arithmetic and defensible reporting are different checks.", dark=True, size=40)

section(prs, "2", "Samples move",
        "Random selection reduces selection bias; it does not make variability disappear")

s, y = content(prs, "Random sampling describes the selection process")
card(s, .72, y + .2, 5.85, 3.75, "RANDOM SAMPLE", [
    "Chance selects units from a defined frame",
    "Each eligible unit has a known opportunity to enter"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.75, "NOT RANDOM", [
    "Take the easiest locations", "Choose only available records",
    "Call a convenience sample random after collection"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

s, y = content(prs, "Sampling variability is expected")
card(s, .72, y + .2, 5.85, 3.75, "ONE POPULATION", [
    "The 200-row demonstrator stays fixed", "Its population mean does not change"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.75, "MANY RANDOM SAMPLES", [
    "Each n = 8 draw contains different units", "Sample means differ by chance"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=18)

activity(prs, "Audit FOREMAN's digits", 10, [
    "Open fatigue_tests.csv, FOREMAN-M09, H9-01, and H9-02.",
    "Reproduce the mean and subtraction; record the source resolution.",
    "Compute the test minimum, maximum, and sample standard deviation.",
    "Mark the first place where displayed precision outruns the evidence.",
], note="Do not replace one unsupported exact number with a method the class has not learned yet.")

activity(prs, "Draw and compare random samples", 12, [
    "Open core_population_200_simulated.csv and your assigned H9-04 draw.",
    "Retrieve the eight listed IDs and calculate the sample mean.",
    "Post the mean; compare all 12 class draws.",
    "Explain why random selection and identical n do not produce identical means.",
], note="The 200 rows are an instructional population, not hidden Otter Bend truth.")

activity(prs, "Audit the real core sampling frame", 8, [
    "Open cores_2027.csv and H9-05.",
    "Inspect drill_zone for all 24 rows; identify observed and unobserved deck regions.",
    "Decide whether the selection was random from the whole deck.",
    "Write the narrowest population the core results can describe.",
], note="Convenient measurements can be useful; the claim must stay inside the sampling frame.")

s, y = content(prs, "Write Unit 2 Note v2", "Claim · check · result")
card(s, .72, y + .2, 3.75, 3.65, "CLAIM", [
    "State FOREMAN's value, precision, and confidence language."
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)
card(s, 4.79, y + .2, 3.75, 3.65, "CHECK", [
    "Name source resolution, spread, and sampling basis."
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 8.86, y + .2, 3.75, 3.65, "RESULT", [
    "Give a supported reporting form and explicit limitations."
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

closer(prs, [
    ("HAND IN", "H9-02 precision audit, H9-05 frame audit, and H9-06 Note v2."),
    ("RECORD", "Project-hour choice and anything accepted unverified."),
    ("REPORT", "Preserve useful scale; remove digits the evidence cannot defend."),
    ("BOUNDARY", "Use only today's precision, spread, and sampling evidence."),
], title="Before the gated reveal")

student_hooks = [
    "TITLE HOOK — Introduce M09 and the false-precision investigation. Do not preview any later statistical method.",
    "INBOX HOOK — Paste only Cloud re-check PASS dialogue here. Preserve the locked beat: Diane Halvorsen, PE wants one number; FOREMAN reports 41,872,316 cycles; Diane is in BELIEVER mode. Verify the revised Wes Tanaka, EIT line before folding.",
    "HUNT HOOK — Frame trace, compare, sample, and report without revealing the supported reporting form. Diane remains BELIEVER throughout the hunt.",
    "TEACH TRANSITION HOOK — Move from the exact-looking output to the statistical basis for a quantitative claim.",
    "TEACH HOOK — Define AI overconfidence through formatting, tone, and omitted uncertainty.",
    "TEACH HOOK — Separate reproducible arithmetic from evidence-supported precision.",
    "TEACH HOOK — Treat significant figures as evidence-based reporting, not a decimal-counting ritual.",
    "TEACH HOOK — Ask for the data, variability, and method behind a quantitative claim.",
    "TEACH HOOK — Contrast calculator output with defensible reporting scale without adding character dialogue.",
    "SAMPLING TRANSITION HOOK — Move from one estimate to what changes across repeated samples.",
    "TEACH HOOK — Define random sampling by selection process and sampling frame.",
    "TEACH HOOK — Define sampling variability before students see the class means.",
    "LAB A HOOK — Students reproduce the point estimate, inspect resolution and spread, and mark unsupported digits.",
    "LAB B HOOK — Release the 200-row demonstrator and assigned random draws. Repeat that it is not bridge evidence.",
    "LAB C HOOK — Return to the actual shoulder-only cores and audit the convenience sampling frame. Diane stays BELIEVER.",
    "NOTE HOOK — Students commit claim/check/result before reveal; assign no new homework number.",
    "CLOSE HOOK — Insert only the Cloud re-check PASS close. Do not preview or name the next meeting's statistical methods.",
]
add_pending_notes(prs, student_hooks)
save(prs, os.path.join(OUT, "M09-student.pptx"))


# ======================================================== REVEAL DECK =======
rev = deck()
title_slide(rev, "Meeting 09  ·  Instructor reveal", "The decimals came from formatting.",
            "Open only after students commit the precision and sampling audits",
            "M09 · Unit 2: Doubt")

s, y = content(rev, "The arithmetic is reproducible")
card(s, .72, y + .2, 5.85, 3.75, "CALCULATION", [
    f"Mean tested life: {mean_life:,.0f} cycles",
    "Accumulated estimate: 3,000,184 cycles",
    f"Difference: {remaining:,.0f} cycles"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.75, "DISPLAY", [
    f"{remaining:,.0f} cycles",
    "Eight significant figures imply single-cycle resolution the evidence does not have."
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

s, y = content(rev, "The tests do not support single-cycle resolution")
picture(s, os.path.join(OUT, "M09-fatigue-scatter.png"), .85, y + .15, w=7.25)
card(s, 8.4, y + .35, 4.2, 3.2, "EVIDENCE SCALE", [
    f"n = {len(life)}", f"SD ≈ {sd_life / 1_000_000:.1f} million cycles",
    f"Range: {min(life) / 1_000_000:.2f}–{max(life) / 1_000_000:.2f} million",
    "Recorded to 10,000 cycles"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=15)

s, y = content(rev, "A supported report is rounded—and bounded")
speaker_card(s, .72, y + .2, 11.87, 2.7, "MODEL RESPONSE · NOT REQUIRED WORDING", [
    "About 42 million cycles is the screening point estimate.",
    "The tests show substantial scatter, and the estimate does not quantify component transfer, service loading, environment, or inspection uncertainty."
], body_size=17)
card(s, .72, y + 3.25, 11.87, 1.35, "NOT A FORMAL INTERVAL", [
    "M09 describes visible spread and reporting scale; the observed test span is descriptive only."
], tint=CREAM, edge=GOLD, body_size=15)

s, y = content(rev, "Random samples produce different means")
picture(s, os.path.join(OUT, "M09-sample-means.png"), .85, y + .15, w=7.25)
card(s, 8.4, y + .35, 4.2, 3.2, "TWELVE n = 8 DRAWS", [
    f"Smallest mean: {min(draw_means):,.1f} psi",
    f"Largest mean: {max(draw_means):,.1f} psi",
    "One fixed population", "Different chance-selected units"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)

s, y = content(rev, "The real cores were not random from the whole deck")
card(s, .72, y + .2, 5.85, 3.75, "WHAT WAS OBSERVED", [
    "24 tested cores", "West and east sides", "Accessible shoulder locations only"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.75, "CLAIM BOUNDARY", [
    "No lane or center cores", "Selection followed access", "Whole-deck representation is not established"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

statement(rev, "Randomness is a property of selection.\nPrecision is a property of evidence.",
          "Neither can be added after the data are collected.", dark=True, size=42)

s, y = content(rev, "Use a bounded Note v2")
speaker_card(s, .72, y + .2, 11.87, 3.05, "CLAIM · CHECK · RESULT", [
    f"CLAIM — FOREMAN reports {remaining:,.0f} cycles remaining with high confidence.",
    f"CHECK — The {len(life)} tests were recorded to 10,000 cycles and have an SD near {sd_life / 1_000_000:.1f} million cycles; transfer assumptions are unquantified.",
    "RESULT — Report about 42 million cycles only as a screening point estimate, state the limitations, and obtain qualified review."
], body_size=16)

closer(rev, [
    ("NOTE v2", "Claim, check, result—rounding and limitations belong in the record."),
    ("SAMPLE", "Keep the simulated demonstrator separate from actual Otter Bend evidence."),
    ("HOURS", "Record what was checked and what remains unverified."),
    ("SCOPE", "Close without teaching M10's interval or significance methods early."),
], title="Close M09")

reveal_hooks = [
    "REVEAL TITLE HOOK — Open only after students commit the precision audit, sampling-frame audit, and Note version 2.",
    "REVEAL HOOK — Confirm 41,872,316 cycles and the unsupported single-cycle precision. Add no character dialogue.",
    "REVEAL HOOK — Show source resolution and fatigue spread; keep the observed span descriptive.",
    "MODEL RESPONSE HOOK — Accept justified rounding alternatives and keep the estimate explicitly screening-level.",
    "REVEAL HOOK — Compare the twelve sample means and name sampling variability.",
    "REVEAL HOOK — Confirm that every actual core is from a shoulder convenience frame; the simulated population is not bridge truth.",
    "REVEAL HOOK — Tie random sampling to selection and precision to evidence.",
    "NOTE HOOK — Compare bounded Note v2 responses; assign no new homework number.",
    "CLOSE HOOK — Paste only Cloud re-check PASS SAY. Diane remains BELIEVER; do not preview or name later methods.",
]
add_pending_notes(rev, reveal_hooks)
save(rev, os.path.join(OUT, "M09-instructor-reveal.pptx"))
