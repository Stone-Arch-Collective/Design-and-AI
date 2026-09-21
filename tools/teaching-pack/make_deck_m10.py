"""M10 spoiler-safe student deck and gated reveal with Oli SAY placeholders."""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

OUT = os.path.join(ROOT, "build", "M10")
with open(os.path.join(OUT, "M10-interval-summary.csv"), newline="") as f:
    summaries = list(csv.DictReader(f))
coupon, paired95, paired99 = summaries


def add_placeholder_notes(prs, labels):
    if len(prs.slides) != len(labels):
        raise ValueError(f"notes ({len(labels)}) != slides ({len(prs.slides)})")
    for slide, label in zip(prs.slides, labels):
        slide.notes_slide.notes_text_frame.text = (
            "OLI SAY PLACEHOLDER — CLOUD PASS PENDING.\n\n"
            f"Beat: {label}\n"
            "Do not improvise or treat this scaffold as approved canon. "
            "Replace only from the Cloud-PASS M10 SAY file on follow-up."
        )


# ======================================================= STUDENT DECK =======
prs = deck()
title_slide(
    prs, "Meeting 10  ·  Unit 2: Doubt", "Did the deck get worse?",
    "Separate a small paired signal from measurement and process noise",
    "Thursday, March 4, 2027  ·  SEIS 201",
)

s, y = content(prs, "The yes-or-no request", "FOREMAN has already made the answer sound final")
speaker_card(s, .72, y + .15, 11.87, 1.9, "FOREMAN · FINAL OUTPUT", [
    "Mean test-truck strain is up 6%. Deterioration confirmed.",
    "p = 0.04, so there is a 96% chance the deck has deteriorated.",
], machine=True, body_size=18)
speaker_card(s, .72, y + 2.35, 11.87, 1.35, "DIANE HALVORSEN, PE", [
    "Did the deck get worse since 2019—yes or no?"
], body_size=18)

s, y = content(prs, "The hunt", "Estimate · audit noise · change confidence · bound the claim")
card(s, .72, y + .2, 2.75, 3.7, "1  PAIR", [
    "Same eight locations", "2027 minus 2019"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 3.68, y + .2, 2.75, 3.7, "2  QUANTIFY", [
    "Mean change", "Standard error"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)
card(s, 6.64, y + .2, 2.75, 3.7, "3  AUDIT", [
    "Repeatability", "Matched process controls"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 9.60, y + .2, 2.99, 3.7, "4  BOUND", [
    "95% versus 99%", "Signal without overclaim"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

section(prs, "1", "Build an interval",
        "Start with six coupons; then move to eight paired changes")

s, y = content(prs, "Standard error is uncertainty in the sample mean")
card(s, .72, y + .2, 5.85, 3.75, "SPREAD OF VALUES", [
    "Standard deviation describes variation among observations",
    "The paired changes differ by location"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.75, "SPREAD OF AN ESTIMATE", [
    "Standard error = s / √n", "It estimates sample-to-sample variation of the mean"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

s, y = content(prs, "Small samples use a t multiplier")
card(s, .72, y + .2, 5.85, 3.75, "t*", [
    "Depends on confidence level", "Depends on degrees of freedom",
    "Larger confidence demand → larger multiplier"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.75, "MARGIN", [
    "margin = t* × standard error", "interval = estimate ± margin"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=18)

s, y = content(prs, "Confidence describes a method—not a vote on a claim")
card(s, .72, y + .2, 5.85, 3.75, "95% CONFIDENCE", [
    "In repeated sampling, about 95% of intervals built this way capture the true mean"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.75, "NOT THIS", [
    "A 95% chance this calculated interval moves", "A 95% chance FOREMAN's story is true"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

activity(prs, "Warm up with six coupons", 10, [
    "Open coupons.csv and H10-01.",
    "Calculate the mean, sample SD, and SE.",
    "Read t* for 95% confidence and df = 5 from the supplied table.",
    "Build and interpret the interval on mean yield strength.",
], note="The warm-up teaches mechanics; it does not answer the deck question.")

section(prs, "2", "Separate signal from noise",
        "Pair locations and inspect what the test process controlled")

s, y = content(prs, "Pairing asks each location to serve as its own baseline")
card(s, .72, y + .2, 5.85, 3.75, "UNPAIRED QUESTION", [
    "How do all 2019 values compare with all 2027 values?",
    "Location differences remain mixed into the spread"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)
card(s, 6.72, y + .2, 5.87, 3.75, "PAIRED QUESTION", [
    "For each same location, what is 2027 − 2019?",
    "Analyze the eight location changes"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)

s, y = content(prs, "Noise has more than one address")
card(s, .72, y + .2, 3.75, 3.75, "MEASUREMENT", [
    "Instrument resolution", "Pass-to-pass repeatability", "Calibration"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 4.79, y + .2, 3.75, 3.75, "PROCESS", [
    "Truck load", "Lane position", "Speed", "Temperature handling"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)
card(s, 8.86, y + .2, 3.75, 3.75, "SAMPLING", [
    "Only eight locations", "Change varies by location", "SE and interval"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

activity(prs, "Audit the test before the p-value", 8, [
    "Open H10-02 and M10-test-control-check.csv.",
    "Verify load, lane position, speed, passes, and temperature handling across years.",
    "Compare within-test repeatability SD with each paired change.",
    "List one source reduced by design and one uncertainty that remains.",
], note="Matched controls reduce alternative explanations; they do not diagnose a mechanism.")

activity(prs, "Build the paired 95% interval", 12, [
    "Use M10-paired-location-summary.csv and H10-03.",
    "Check each 2027 − 2019 change before summarizing.",
    "Calculate mean, SD, SE, t* for df = 7, and the 95% interval.",
    "Decide whether zero mean change remains plausible at this confidence level.",
], note="Commit the interval and a one-sentence claim before the reveal.")

s, y = content(prs, "Significance is not size, certainty, or diagnosis")
card(s, .72, y + .2, 5.85, 3.75, "p-VALUE", [
    "Assumes a null model", "Asks how unusual this result would be under that model",
    "Does not assign probability to FOREMAN's claim"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 6.72, y + .2, 5.87, 3.75, "ENGINEERING CLAIM", [
    "Needs magnitude", "Needs uncertainty", "Needs test controls",
    "May still need a physical mechanism"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

activity(prs, "Raise the confidence level", 5, [
    "Keep the same mean, SD, SE, and df.",
    "Replace the 95% t multiplier with the 99% multiplier.",
    "Rebuild the interval and check whether zero enters.",
    "Explain why the two intervals are not contradictory.",
], note="Higher confidence requires a wider interval.")

s, y = content(prs, "Write Unit 2 Note v2", "Claim · check · result · now with an interval")
card(s, .72, y + .2, 3.75, 3.65, "CLAIM", [
    "State FOREMAN's 6% and p-value interpretation."
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)
card(s, 4.79, y + .2, 3.75, 3.65, "CHECK", [
    "Give paired estimate, interval, and noise/control audit."
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 8.86, y + .2, 3.75, 3.65, "RESULT", [
    "Say how sure—and what the data still cannot prove."
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

closer(prs, [
    ("HAND IN", "H10-03 and H10-06 after committing the paired claim."),
    ("ASSIGNED", "HW5: audit duplicate timestamps before building the peak-strain interval."),
    ("RECORD", "Project-hour choice and anything accepted unverified."),
    ("BOUNDARY", "No Exam 1 load, scaling, chart, or permit details enter M10."),
], title="Before the gated reveal")

add_placeholder_notes(prs, [
    "title and meeting frame", "inbox: Diane, FOREMAN, and schedule pressure",
    "student hunt", "teach transition", "standard error", "t multiplier",
    "confidence level", "coupon warm-up", "signal/noise transition", "paired design",
    "measurement/process/sampling noise", "test-control audit", "paired 95% interval",
    "p-value and significance language", "99% sensitivity check", "Note v2",
    "HW5 callback and close",
])
save(prs, os.path.join(OUT, "M10-student.pptx"))


# ======================================================== REVEAL DECK =======
rev = deck()
title_slide(
    rev, "Meeting 10  ·  Instructor reveal", "Probably a small real change.",
    "Open only after students commit the paired interval",
    "M10 · Unit 2: Doubt",
)

s, y = content(rev, "The coupon interval establishes the method")
card(s, .72, y + .25, 11.87, 2.9, "SIX COUPONS · 95% CONFIDENCE", [
    f"Mean = {float(coupon['mean']):.2f} ksi",
    f"SE = {float(coupon['standard_error']):.2f} ksi · t* = {coupon['t_multiplier']}",
    f"95% CI = [{float(coupon['lower']):.2f}, {float(coupon['upper']):.2f}] ksi",
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=19)

s, y = content(rev, "Same-location changes reveal a small positive mean")
picture(s, os.path.join(OUT, "M10-paired-changes.png"), .85, y + .15, w=7.25)
card(s, 8.4, y + .4, 4.2, 2.9, "PAIRED ESTIMATE", [
    "n = 8 locations", "Mean = 6.00 µε",
    f"SD = {float(paired95['sd']):.2f} µε",
    f"SE = {float(paired95['standard_error']):.2f} µε",
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)

s, y = content(rev, "At 95%, zero sits just outside the interval")
card(s, .72, y + .4, 5.85, 3.35, "95% INTERVAL", [
    f"t* = {paired95['t_multiplier']}",
    f"[{float(paired95['lower']):.2f}, {float(paired95['upper']):.2f}] µε",
    "Zero excluded—barely"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=20)
card(s, 6.72, y + .4, 5.87, 3.35, "SUPPORTED", [
    "Evidence of a positive mean change", "Magnitude remains small and uncertain",
    "Not a complete damage diagnosis"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

s, y = content(rev, "At 99%, the wider interval includes zero")
card(s, .72, y + .4, 5.85, 3.35, "99% INTERVAL", [
    f"t* = {paired99['t_multiplier']}",
    f"[{float(paired99['lower']):.2f}, {float(paired99['upper']):.2f}] µε",
    "Zero remains plausible"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=20)
card(s, 6.72, y + .4, 5.87, 3.35, "WHY", [
    "Same estimate and data", "Higher confidence demand", "Wider uncertainty band"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)

statement(
    rev, "The signal survives a 95% interval.\nThe certainty does not survive 99%.",
    "Probably a small real change is stronger than either “noise” or “confirmed.”",
    dark=True, size=40,
)

s, y = content(rev, "FOREMAN turned significance into certainty")
card(s, .72, y + .2, 5.85, 3.7, "VALID", [
    "The paired estimate is +6.0 µε", "The 95% interval excludes zero",
    "Matched controls reduce some process noise"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.7, "INVALID LEAP", [
    "p = 0.04 means 96% probability", "Significant means confirmed",
    "Positive strain change proves deck deterioration"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

s, y = content(rev, "A bounded answer keeps the uncertainty visible")
speaker_card(s, .72, y + .2, 11.87, 2.65, "MODEL RESPONSE · NOT REQUIRED WORDING", [
    "The eight matched locations show a mean increase of 6.0 microstrain.",
    f"The 95% interval is [{float(paired95['lower']):.2f}, {float(paired95['upper']):.2f}] "
    f"microstrain; the 99% interval is [{float(paired99['lower']):.2f}, "
    f"{float(paired99['upper']):.2f}]. This is probably a small real change, not confirmed deterioration.",
], body_size=17)

closer(rev, [
    ("HW5", "Audit duplicate timestamps before calculating the peak-strain interval."),
    ("NOTE v2", "Include the estimate and interval in claim/check/result."),
    ("DIANE", "Her demand for yes/no is schedule pressure—not the grading key."),
    ("SPOILER GUARD", "Keep all Exam 1 permit details out of this meeting."),
], title="Close M10")

add_placeholder_notes(rev, [
    "reveal title", "coupon result", "paired estimate", "95% interval",
    "99% interval", "confidence-level synthesis", "FOREMAN designed error",
    "bounded response", "HW5 and close",
])
save(rev, os.path.join(OUT, "M10-instructor-reveal.pptx"))
