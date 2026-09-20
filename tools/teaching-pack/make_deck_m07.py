"""M07 spoiler-safe student deck and gated instructor reveal."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

OUT = os.path.join(ROOT, "build", "M07")


def add_notes(prs, notes):
    if len(prs.slides) != len(notes):
        raise ValueError(f"notes ({len(notes)}) != slides ({len(prs.slides)})")
    for slide, note in zip(prs.slides, notes):
        slide.notes_slide.notes_text_frame.text = (
            "OLI CANON SAY — Cloud hard-review pass.\n\n"
            + note.strip()
        )


# ======================================================= STUDENT DECK =======
prs = deck()
title_slide(prs, "Meeting 07  ·  Unit 2: Doubt", "Does the confidence travel?",
            "Audit training coverage before using FOREMAN's image screen",
            "Tuesday, February 23, 2027  ·  SEIS 201")

s, y = content(prs, "The interim report moved up", "FOREMAN screened 12 images in under a minute")
speaker_card(s, .72, y + .15, 11.87, 1.75, "FOREMAN v4.2 — FINAL", [
    "“No significant defects detected in the submitted tower, span, or machinery-room images. Overall confidence: HIGH.”"
], machine=True, body_size=19)
speaker_card(s, .72, y + 2.1, 11.87, 1.45, "DIANE HALVORSEN, PE", [
    "“It looked at 12 images in under a minute. Give me a specific reason not to use it.”"
], body_size=18)
card(s, .72, y + 3.85, 11.87, 1.35, "TODAY'S DECISION", [
    "Which ratings, if any, can enter the interim report—and under what boundary?"
], tint=CREAM, edge=GOLD, body_size=16)

s, y = content(prs, "The hunt", "Do not diagnose a hidden defect; audit applicability")
card(s, .72, y + .2, 3.75, 3.65, "1  PROFILE", [
    "What was represented in training and evaluation?", "Which categories were absent?"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 4.79, y + .2, 3.75, 3.65, "2  COMPARE", [
    "How does Otter Bend differ by bridge type, climate, and component?"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)
card(s, 8.86, y + .2, 3.75, 3.65, "3  BOUND", [
    "Where can a rating remain provisional? Where must FOREMAN abstain?"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

section(prs, "1", "Bias begins before the answer",
        "A model inherits what its examples include, omit, label, and measure")

s, y = content(prs, "AI bias is patterned error—not machine intent")
bullet_list(s, .95, y + .2, 11.4, 3.75, [
    ("Training-data bias  ", "examples systematically overrepresent some conditions and underrepresent others."),
    ("Label bias  ", "the available categories make some conditions visible and others impossible to name."),
    ("Evaluation bias  ", "a test set resembles training but not the intended deployment."),
    ("Deployment bias  ", "people use a model for a population or task its evidence does not support."),
], size=18, dot=GIRDER_LT)
card(s, .72, y + 4.1, 11.87, 1.35, "AUDIT MOVE", [
    "Ask which population the performance number describes."
], tint=CREAM, edge=GOLD, body_size=15)

s, y = content(prs, "Representative of what?", "A large sample can still miss the intended use")
card(s, .72, y + .2, 5.85, 3.75, "REPRESENTATIVE SAMPLE", [
    "Resembles the population and task where the claim will be used",
    "Covers relevant subgroups and operating conditions",
    "Makes omissions visible"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.75, "NOT ENOUGH BY ITSELF", [
    "A large image count", "A random split from one archive", "High average accuracy",
    "A confident score on a new category"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

statement(prs, "Accuracy answers:\n“How did it perform there?”",
          "It does not answer: “Does there resemble here?”", dark=True, size=46)

s, y = content(prs, "Distribution shift changes the data relationship",
               "The deployment distribution differs from training")
bullet_list(s, .95, y + .2, 11.4, 3.75, [
    ("Inputs shift  ", "bridge configuration, image setting, climate, corrosion exposure."),
    ("Labels shift  ", "deployment asks about components the training taxonomy did not name."),
    ("Frequencies shift  ", "rare training conditions become common in deployment."),
    ("Consequence  ", "held-out performance and confidence may not transfer."),
], size=18, dot=STICKER)
card(s, .72, y + 4.1, 11.87, 1.35, "IMPORTANT", [
    "Shift is a reason to investigate performance—not proof that every rating is wrong."
], tint=PAPER, edge=CONCRETE, body_size=15)

s, y = content(prs, "Out of domain means the evidence boundary was crossed")
card(s, .72, y + .2, 5.85, 3.8, "COVERAGE GAP", [
    "A relevant category or condition is absent or too sparse to support the use",
    "The correct response may be abstention, new validation, or qualified review"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.8, "HIGH CONFIDENCE", [
    "Usually a model score among known labels", "Not a detector of missing knowledge",
    "Can remain high on unfamiliar inputs"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

section(prs, "2", "Compare before you conclude",
        "Bridge type · climate · component labels · evaluation design")

activity(prs, "Profile the training archive", 10, [
    "Open H7-01 and underline the population behind 93.8% accuracy.",
    "Record bridge configurations, climate exposure, component labels, and evaluation split.",
    "Circle every category that is absent or not recorded.",
    "Complete the training column in H7-05 without opening the key.",
], note="A random split can be valid and still answer the wrong deployment question.")

activity(prs, "Map Otter Bend against that coverage", 13, [
    "Open H7-02, H7-03, and the CSV. Group all 12 records by fixed span, tower, and moving machinery.",
    "Compare each group with the disclosed training taxonomy.",
    "Mark each dimension match, shift, or gap; cite the exact line in H7-01.",
    "Do not guess whether a hidden defect exists. Judge whether the rating is supportable.",
], note="The audit target is model applicability, not visual defect diagnosis.")

activity(prs, "Challenge the confidence", 10, [
    "Open H7-04 and identify what FOREMAN means by confidence.",
    "Decide which image groups can remain provisional and which require abstention or review.",
    "State what 93.8% supports—and what it cannot support at Otter Bend.",
    "Write a bounded recommendation before the reveal.",
], note="Blanket trust and blanket rejection both skip the coverage evidence.")

s, y = content(prs, "Write Unit 2 note v2", "Three lines; claim, check, result")
card(s, .72, y + .2, 3.75, 3.65, "CLAIM", [
    "State exactly what FOREMAN says and which records it covers."
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)
card(s, 4.79, y + .2, 3.75, 3.65, "CHECK", [
    "Name the training-coverage evidence and dimensions you compared."
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 8.86, y + .2, 3.75, 3.65, "RESULT", [
    "Say what can be used, withheld, or routed to qualified review."
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

closer(prs, [
    ("HAND IN", "H7-05 coverage audit and H7-06 Note version 2."),
    ("RECORD", "Your proposed project-hour choice and what remains unverified."),
    ("PRESERVE", "Wes's memo with the evidence packet; polished prose is not validation."),
    ("NEXT", "M08 begins the next investigation as seasonal conditions change."),
], title="Before the reveal")

student_notes = [
    "INBOX — SAY: “The report is in. No defects found. High confidence. Let's move.” Establish that the report covers Otter Bend towers and machinery as well as familiar fixed-span components.",
    "INBOX — Diane Halvorsen, PE: “It looked at 400 photos in a minute. Give me a reason not to use it.” Wes Tanaka, EIT: “I'm drafting the memo to accept the machinery rating based on the vendor summary.” STUDENT: “Wait, I need to check the training data source first.”",
    "HUNT — SAY: “Read the training summary closely. Compare the 12 photos with the population the model actually saw. Your answer must name the gap, not merely distrust the tool.”",
    "TEACH TRANSITION — SAY: “Bias begins before the answer: in what the examples include, omit, label, and measure.”",
    "TEACH — SAY: “Bias here is patterned limitation in examples, labels, evaluation, or deployment. It does not require intent.”",
    "TEACH — SAY: “A representative sample is representative of a particular population and task. Ask: representative of what?”",
    "TEACH — SAY: “The held-out score may honestly describe performance on the archive. It does not show that the archive resembles Otter Bend.”",
    "TEACH — SAY: “Distribution shift means the deployment differs from training in relevant ways. Shift is a reason to test applicability, not proof that every output is wrong.”",
    "TEACH — SAY: “Out of domain marks a coverage boundary. A high class score does not tell you the system lacks the right experience or label.”",
    "LAB TRANSITION — INSTRUCTOR: “Read the vendor summary. Where were these photos taken?” EXPECT: “Warm states, highway girders only.” Then ask: “What does Otter Bend have that this data never saw?” EXPECT: “Lift machinery, freeze and thaw, road salt.”",
    "LAB — TASK: Compare the 12 photos against the training-summary distribution. Complete the archive profile in H7-05. Do not reveal the final applicability classification.",
    "LAB — ACTION: Mark photos where Otter Bend's bridge type, machinery, freeze–thaw exposure, or road-salt context differs from training. Require an H7-01 citation.",
    "LAB — OBSERVATION: Confidence remains high across the domain shift. Ask: “Why might the model fail to express uncertainty on an out-of-domain input?” Do not give the answer before students write.",
    "NOTE — Students write Note version 2 only: claim, check, result. SAY: “Professional judgment sets the evidence boundary when the model record does not.”",
    "CLOSE — Collect Note version 2 only. Light hook: “The conditions around a bridge do not stay fixed through the year.” Do not explain the M08 mechanism.",
]
add_notes(prs, student_notes)
save(prs, os.path.join(OUT, "M07-student.pptx"))


# ======================================================== REVEAL DECK =======
rev = deck()
title_slide(rev, "Meeting 07  ·  Instructor reveal", "The confidence does not travel.",
            "Open only after students submit the coverage audit",
            "M07 · Unit 2: Doubt")

s, y = content(rev, "The archive and the job differ on every major dimension")
table_slide_rows = [
    ["Dimension", "Training / evaluation", "Otter Bend"],
    ["Bridge", "91% fixed highway girder", "Vertical-lift bridge"],
    ["Climate", "Mostly warm / low freeze–thaw", "Minnesota exposure"],
    ["Labels", "Fixed structural components", "Towers + moving machinery"],
    ["Machinery", "No relevant labels", "6 of 12 records"],
]
gt = s.shapes.add_table(5, 3, Inches(.72), Inches(y + .15), Inches(11.87), Inches(3.4)).table
for ci, width in enumerate([2.2, 4.5, 5.17]):
    gt.columns[ci].width = Inches(width)
for ri, row in enumerate(table_slide_rows):
    gt.rows[ri].height = Inches(.68)
    for ci, value in enumerate(row):
        c = gt.cell(ri, ci); c.fill.solid()
        c.fill.fore_color.rgb = GIRDER if ri == 0 else (WHITE if ri % 2 else PAPER)
        p = c.text_frame.paragraphs[0]; r = p.add_run(); r.text = value
        r.font.name = DISPLAY if ri == 0 else BODY; r.font.size = Pt(15)
        r.font.bold = ri == 0; r.font.color.rgb = WHITE if ri == 0 else REBAR

s, y = content(rev, "A same-archive test cannot validate a new domain",
               "93.8% answers a narrower question")
card(s, .72, y + .2, 5.85, 3.7, "VALID CLAIM", [
    "The model scored 93.8% on held-out images sampled from its disclosed archive."
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=19)
card(s, 6.72, y + .2, 5.87, 3.7, "UNSUPPORTED LEAP", [
    "Therefore all 12 Minnesota lift-bridge ratings are reliable at 93–97%."
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=19)

s, y = content(rev, "The machinery ratings cross a hard coverage gap")
card(s, .72, y + .2, 5.85, 3.75, "PROVISIONAL TRIAGE", [
    "001–004 use familiar fixed-girder or deck categories",
    "Climate and whole-asset shift still require an explicit limit"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.75, "WITHHOLD + REVIEW", [
    "005–006 tower structure is outside the listed taxonomy",
    "007–012 machinery categories are absent from training labels"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

statement(rev, "High confidence can describe\nan unsupported choice among known labels.",
          "The score does not measure what the model never learned.", dark=True, size=42)

s, y = content(rev, "A bounded action preserves use without pretending")
speaker_card(s, .72, y + .2, 11.87, 2.75, "MODEL DECISION — NOT THE ONLY FULL-CREDIT WORDING", [
    "“Withhold the all-clear. The disclosed archive contains no movable bridges or moving-machinery labels and little comparable climate exposure. Route images 005–012 to qualified review; retain 001–004 only as provisional triage with the coverage limits visible.”"
], body_size=18)
card(s, .72, y + 3.3, 11.87, 1.35, "DO NOT CLAIM", [
    "This audit proves a defect exists. It proves the all-clear is not supported by this model record."
], tint=CREAM, edge=GOLD, body_size=15)

s, y = content(rev, "Wes's memo passed—and remains wrong")
speaker_card(s, .72, y + .2, 5.85, 3.5, "WES TANAKA, EIT", [
    "Polished summary", "Exact confidence range", "No coverage comparison",
    "Recommendation outruns evidence"
], body_size=17)
speaker_card(s, 6.72, y + .2, 5.87, 3.5, "DIANE HALVORSEN, PE", [
    "Believer mode", "Schedule pressure", "Approval is an organizational event",
    "Approval is not validation"
], body_size=17)

closer(rev, [
    ("NOTE v2", "Claim, check, result—the evidence boundary belongs in the record."),
    ("HOURS", "Choose the next check; project hours shape priority and are not points."),
    ("RETAIN", "Keep Wes's accepted memo as one seed inside the existing M13 messy handoff."),
    ("M08", "Lightly hook seasonal change; keep the temperature-as-damage mechanism hidden."),
], title="Close M07")

reveal_notes = [
    "REVEAL — SAY: “FOREMAN rated the machinery-room photos clean and high confidence even though its disclosed training contains no movable bridges or machinery labels.”",
    "REVEAL — SAY: “The training distribution is almost entirely highway girder bridges from warm states. Otter Bend adds a vertical-lift configuration, Minnesota freeze–thaw, and road-salt exposure.”",
    "REVEAL — SAY: “The 93.8 percent score answers performance on a same-archive holdout. It does not establish performance on Otter Bend.”",
    "REVEAL — SAY: “The familiar fixed-span records may remain provisional triage. Tower and machinery records cross the disclosed coverage boundary and require qualified review.”",
    "REVEAL — INSTRUCTOR: “The AI rates the machinery room with the same confidence as the girder photos. It has no sign of uncertainty because it was never trained on them.” Clarify that confidence is not an ignorance detector.",
    "REVEAL — SAY: “Withhold the all-clear. This audit does not prove a defect; it proves that this model record cannot support the all-clear for the out-of-domain images.”",
    "SIDE BEAT — Wes polishes the accept-memo; Diane skims and passes it in BELIEVER mode. Preserve it only as liability color seeded inside M13's existing messy unit-mismatch handoff. Do not rewrite M13 as the memo's return.",
    "CLOSE — Collect Note version 2 only. Professional judgment overrides unsupported automated confidence. Lightly hook changing seasonal conditions without naming temperature-as-damage.",
]
add_notes(rev, reveal_notes)
save(rev, os.path.join(OUT, "M07-instructor-reveal.pptx"))
