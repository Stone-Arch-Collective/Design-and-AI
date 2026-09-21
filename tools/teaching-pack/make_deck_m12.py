"""M12 spoiler-safe student deck and gated chart reveal."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

OUT = os.path.join(ROOT, "build", "M12")


def add_canon_notes(prs, notes):
    if len(prs.slides) != len(notes):
        raise ValueError(f"notes ({len(notes)}) != slides ({len(prs.slides)})")
    for slide, note in zip(prs.slides, notes):
        slide.notes_slide.notes_text_frame.text = (
            "CLOUD-PASS CANON SAY · revised M12.\n\n" + note.strip()
        )


# ======================================================= STUDENT DECK =======
prs = deck()
title_slide(
    prs, "Meeting 12  ·  Unit 2: Doubt", "The county reads charts, not appendices.",
    "Critique FOREMAN's chart pack before it ships",
    "Thursday, March 11, 2027  ·  SEIS 201",
)

s, y = content(prs, "Publish-ready is not review-ready")
speaker_card(s, .72, y + .12, 11.87, 1.8, "FOREMAN · CHART PACK", [
    "Interim report chart pack assembled for Otter Bend.",
    "Ready for county. No human review requested.",
], machine=True, body_size=18)
speaker_card(s, .72, y + 2.05, 11.87, 1.45, "DIANE HALVORSEN, PE · SKEPTIC", [
    "The county reads charts, not appendices. If the picture lies, the memo does not save you."
], body_size=18)

s, y = content(prs, "Today's sequence", "The review block starts after Lab—not inside it")
card(s, .72, y + .18, 2.75, 3.5, "TEACH · 20", [
    "Chart question", "Type", "Scale + baseline"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 3.68, y + .18, 2.75, 3.5, "LAB · 30", [
    "Hunt first", "Approve / fix / pull", "Redraw refusals"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)
card(s, 6.64, y + .18, 2.75, 3.5, "REVIEW · 25", [
    "Units 1–2 only", "Separate block", "No new scenario"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 9.60, y + .18, 2.99, 3.5, "NOTE · 5", [
    "HW6", "Two redraws", "Primer assigned"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

section(prs, "1", "Match the chart to the question",
        "Trend over time · category comparison · parts of a whole")

s, y = content(prs, "Chart type is a claim about what should be compared")
card(s, .72, y + .2, 3.75, 3.65, "ORDERED TIME", [
    "Line or ordered bars", "Keep sequence visible"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 4.79, y + .2, 3.75, 3.65, "CATEGORIES", [
    "Bars or dots", "Use a common scale"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)
card(s, 8.86, y + .2, 3.75, 3.65, "PARTS OF ONE WHOLE", [
    "Pie only when the whole matters", "Few slices"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)

s, y = content(prs, "Axes decide what differences feel large")
card(s, .72, y + .2, 5.85, 3.7, "READ THE SCALE", [
    "Where does the quantitative axis begin?", "What range is visible?",
    "Are units and intervals explicit?"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.7, "READ THE CLAIM", [
    "Does the title describe—or diagnose?", "Would a different baseline change the feeling?",
    "Is context hidden outside the frame?"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

s, y = content(prs, "A nonzero baseline is a demand for explanation")
card(s, .72, y + .4, 11.87, 2.95, "BASELINE TEST", [
    "A cropped range can help readers see small changes.",
    "It can also make ordinary movement look like failure.",
    "The chart must preserve scale context and avoid a conclusion the numbers do not support.",
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=18)

section(prs, "2", "Open the chart pack",
        "Do not assume every tile fails · do not assume polish means approval")

s, y = content(prs, "FOREMAN tile A", "Record approve / fix / pull before discussion")
picture(s, os.path.join(OUT, "M12-tile-A.png"), 1.35, y + .05, w=10.6)

s, y = content(prs, "FOREMAN tile B", "Record approve / fix / pull before discussion")
picture(s, os.path.join(OUT, "M12-tile-B.png"), 1.35, y + .05, w=10.6)

s, y = content(prs, "FOREMAN tile C", "Record approve / fix / pull before discussion")
picture(s, os.path.join(OUT, "M12-tile-C.png"), 1.35, y + .05, w=10.6)

activity(prs, "Hunt first · then redraw", 30, [
    "Complete H12-01 for all three tiles: approve, fix, or pull with one reason.",
    "Use H12-02 to test question, chart type, scale, baseline, units, and title.",
    "Open the source CSVs only after your first visual review.",
    "Redraw every tile you refuse as delivered using H12-03.",
    "Commit both redraws before the instructor reveal.",
], note="Wes Tanaka, EIT delivered the folder. He is not a source of answers.")

statement(
    prs, "Lab ends here.",
    "The 25-minute Exam 1 review is a separate block after the chart hunt and redraws.",
    dark=True, size=48,
)

section(prs, "3", "Exam 1 review · 25 minutes",
        "Units 1–2 only · spread · intervals · spurious trends · human review")

s, y = content(prs, "Four review moves", "No new scenario · no new designed errors")
card(s, .72, y + .2, 2.75, 3.7, "SPREAD", [
    "Mean + SD / range", "Distribution shape"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 3.68, y + .2, 2.75, 3.7, "INTERVAL", [
    "Estimate + uncertainty", "Confidence ≠ certainty"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=16)
card(s, 6.64, y + .2, 2.75, 3.7, "TREND", [
    "Association ≠ cause", "Name a mechanism"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)
card(s, 9.60, y + .2, 2.99, 3.7, "REVIEW", [
    "Source", "Assumptions", "Human disposition"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

activity(prs, "Review in four-minute rounds", 25, [
    "Use H12-05. Write one claim with a number and spread or interval.",
    "Bound one causal claim as an association and name a competing mechanism.",
    "Name one check that does not depend on an agent's confident wording.",
    "Explain why a polished report still needs a human review checkpoint.",
    "Compare answers and mark one move to use under time pressure.",
], note="This review does not reveal or rehearse any Exam 1 scenario.")

closer(prs, [
    ("HAND IN", "HW6: two clearly labeled redraws plus Note v2."),
    ("ASSIGNED", "Async code-reading primer; due before M15."),
    ("BOUNDARY", "Exam review was its own block after Lab."),
    ("CLOSE", "The county reads charts, not appendices."),
], title="Note · 5 minutes")

add_canon_notes(prs, [
    "TITLE — SAY: “The county reads charts, not appendices. Today you are the human review checkpoint before Otter Bend visuals leave the firm.”",
    "INBOX — FOREMAN (orange): “Interim report chart pack assembled for Otter Bend. Ready for county. No human review requested.” Diane Halvorsen, PE (skeptic): “The county reads charts, not appendices. If the picture lies, the memo does not save you.” Wes Tanaka, EIT: “Pack is in the shared folder. I’m not redrawing these with you.”",
    "CLOCK — SAY: “Teach is 20, Lab is 30, Exam review is a separate 25-minute block after Lab, and Note is 5. The passed durations total 80 minutes; the instructor key flags the five-minute conflict with the 75-minute course slot.”",
    "TEACH TRANSITION — SAY: “Before opening FOREMAN’s tiles, name the question each visual form can honestly answer.”",
    "TEACH — SAY: “Start with the reader’s question. Trend over time, category comparison, and parts of a whole require different visual encodings.”",
    "TEACH — SAY: “Where the axis begins changes the story readers feel. Read the scale before you read the shape.”",
    "TEACH — SAY: “A nonzero baseline is not automatically dishonest. It does require enough context that a small movement does not masquerade as failure.”",
    "LAB TRANSITION — SAY: “Now open the chart pack. Every tile gets a disposition, and the student deck does not tell you which ones fail.”",
    "LAB TRANSITION — SAY: “FOREMAN looks finished. Finished is not reviewed. Open H12-01 and commit a disposition for every tile before we discuss any.”",
    "LAB — SAY: “Tile A. Do not ask which kind of error you are looking for. Name the question, scale, baseline, and implication.”",
    "LAB — SAY: “Tile B. Preserve time order if time is the question. Commit approve, fix, or pull.”",
    "LAB — SAY: “Tile C. The pack is not a wipeout. Approval is a valid disposition when the visual earns it.”",
    "LAB — SAY: “Hunt first. Then open the three CSVs, redraw every chart you refuse, and explain how your encoding changes what an honest reader sees. Wes Tanaka, EIT does not co-solve.”",
    "TRANSITION — SAY: “Stop the Lab. The redraw work is complete. Exam review begins now as its own block.”",
    "REVIEW — SAY: “Units 1–2 only: spreads, confidence intervals, spurious trends, and human review of agent claims. No new scenario and no new designed error.”",
    "REVIEW — SAY: “Use H12-05 in four-minute rounds. Give a number with spread or interval; bound a causal claim; name an independent check; locate the human review checkpoint.”",
    "NOTE — SAY: “Hand in HW6: the two redrawn charts, clearly labeled, plus Note v2. Assign the async code-reading primer, due before M15. The county reads charts, not appendices.”",
])
save(prs, os.path.join(OUT, "M12-student.pptx"))


# ======================================================== REVEAL DECK =======
rev = deck()
title_slide(
    rev, "Meeting 12  ·  Instructor reveal", "Pretty does not mean honest.",
    "Open only after students commit dispositions and redraws",
    "M12 · Unit 2: Doubt",
)

s, y = content(rev, "Tile A · truncated y-axis")
picture(s, os.path.join(OUT, "M12-tile-A.png"), .75, y + .15, w=7.35)
card(s, 8.35, y + .35, 4.25, 3.0, "WHY IT FAILS", [
    "99.5–104.5 µε scale", "Ordinary movement fills the frame",
    "Failure-sounding title outruns the data"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

s, y = content(rev, "Repair A · restore magnitude context")
picture(s, os.path.join(OUT, "M12-fix-A-honest-scale.png"), 1.15, y + .05, w=11.05)

s, y = content(rev, "Tile B · wrong chart type for ordered time")
picture(s, os.path.join(OUT, "M12-tile-B.png"), .75, y + .12, w=7.35)
card(s, 8.35, y + .35, 4.25, 3.0, "WHY IT FAILS", [
    "Pie treats hours as unordered shares", "Sequence is hard to compare",
    "Question is hourly pattern, not composition"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

s, y = content(rev, "Repair B · put hour back on the x-axis")
picture(s, os.path.join(OUT, "M12-fix-B-hourly-bars.png"), 1.15, y + .05, w=11.05)

s, y = content(rev, "Tile C · approve")
picture(s, os.path.join(OUT, "M12-tile-C.png"), .75, y + .12, w=7.35)
card(s, 8.35, y + .35, 4.25, 3.0, "WHY IT WORKS", [
    "Bars match category comparison", "Common zero baseline",
    "Counts and observation window are labeled"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=16)

statement(
    rev, "The chart can lie while every number is true.",
    "Human review tests the question, encoding, scale, and claim—not only arithmetic.",
    dark=True, size=43,
)

closer(rev, [
    ("HW6", "Two corrected charts, clearly labeled, with Note v2."),
    ("PRIMER", "Async code reading due before M15."),
    ("WES", "Delivered the pack; did not co-solve."),
    ("SPOILER GUARD", "No M13 or Exam 1 scenario details."),
], title="Close M12")

add_canon_notes(rev, [
    "REVEAL — SAY: “Name the designed errors only now. Tile A uses a truncated y-axis that makes ordinary variation look like failure.”",
    "REVEAL — SAY: “The repair restores magnitude context and removes the diagnostic title. A narrower scale could be used only with an explicit reason and honest context.”",
    "REVEAL — SAY: “Tile B uses a pie for hourly traffic. A pie destroys the time order the reader needs.”",
    "REVEAL — SAY: “The repair uses ordered bars. A line would also preserve the hourly sequence.”",
    "REVEAL — SAY: “Tile C is the cleaner chart. Its bars answer a category-comparison question from a common zero baseline. The hunt was never supposed to be a wipeout.”",
    "REVEAL — SAY: “FOREMAN did not invent numbers. The misleading story came from chart type, scale, and title. Critiquing that finished output is the engineering skill.”",
    "CLOSE — SAY: “If an Otter Bend chart would scare the county about ordinary variation—or use a chart type that cannot show the question—it does not ship. Diane Halvorsen, PE owns what the county sees.”",
    "CLOSE — SAY: “Collect HW6, assign the code-reading primer due before M15, and preserve the spoiler guard: no M13 details and no Exam 1 scenario details.”",
])
save(rev, os.path.join(OUT, "M12-instructor-reveal.pptx"))
