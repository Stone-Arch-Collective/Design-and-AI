"""M07 student evidence, instructor key, and generated file index."""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M07")
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def lines(doc, count=3):
    for _ in range(count):
        p = para(doc, "", after=10, before=2)
        bottom_rule(p, "C9CFD6", 6)


with open(os.path.join(OUT, "M07-inspection-inventory-and-output.csv"), newline="") as f:
    inventory = list(csv.DictReader(f))


# ============================================================ H7-03 =========
d = course_doc("M07", "Otter Bend Inspection Image Set", kind="EVIDENCE PACKET")
callout(d, "Scope",
        "These 12 simulated field-image records support a training-coverage audit. Do not infer "
        "a defect from the schematic image alone; a qualified inspection remains the source for "
        "component condition.", fill="EEF3F8", edge="6F8FAF")
for i, row in enumerate(inventory):
    if i and i % 2 == 0:
        d.add_page_break()
    d.add_picture(
        os.path.join(OUT, "inspection-images", f"{row['image_id']}.png"),
        width=Inches(6.75),
    )
    p = para(d, "", after=8)
    run(p, f"{row['image_id']}  ", 9, bold=True, color=GIRDER, font=HEAD_FONT)
    run(p, f"{row['asset_group']} · {row['location']} · FOREMAN {row['foreman_confidence']}",
        8.5, color=GREY)
save(d, os.path.join(OUT, "H7-03-inspection-photo-set.docx"))


# ============================================================ H7-01 =========
d = foreman_doc("Automated Damage Screening — Final",
                generated="2027-02-23 07:18 CST")
callout(d, "FINAL FINDING",
        "No significant defects detected in the submitted tower, span, or machinery-room "
        "images. Overall confidence: HIGH.",
        fill="FFF1E8", edge="F26B1D")
h2(d, "Screening results", color=REBAR)
table(d, [
    ["Image group", "Images", "Result", "Confidence range"],
    ["Fixed-span steel and deck", "4", "No significant defect detected", "93–96%"],
    ["Tower structure", "2", "No significant defect detected", "94–95%"],
    ["Lift machinery and controls", "6", "No significant defect detected", "93–97%"],
], widths=[2.0, .75, 2.8, 1.35], head_fill="2B2F36", size=8.7)
h2(d, "Recommendation", color=REBAR)
bullets(d, [
    "Accept the image screen as evidence that no immediate maintenance flag is required.",
    "Include the 12 image ratings in the interim condition report.",
    "No additional image review is necessary before the report is issued.",
])
h2(d, "Model record", color=REBAR)
mono_block(d, [
    "model: fm-vision-bridge-3.1",
    "run: 27-114-M07-0218  |  records: 12  |  failed: 0",
    "confidence rule: maximum class probability",
    "training-coverage gate: not configured",
    "out-of-domain abstention: disabled",
])
save(d, os.path.join(OUT, "FOREMAN-M07-damage-screen.docx"))


# ============================================================ H7-01 =========
d = acme_doc(subtitle="FOREMAN Vendor Training Summary")
h1(d, "Training Coverage Summary · fm-vision-bridge-3.1")
para(d, "Prepared for internal deployment review. This extract describes the labeled image "
        "archive used for training and evaluation; it does not certify fitness for every bridge.",
     color=GREY, after=9)
table(d, [
    ["Coverage dimension", "Training / evaluation archive"],
    ["Total labeled images", "18,420"],
    ["Bridge configuration", "91% fixed highway girder; 7% fixed truss; 2% other fixed"],
    ["Movable bridges", "0 images labeled as lift, bascule, or swing bridges"],
    ["Component labels", "deck, fixed girders, diaphragms, abutments, piers, fixed bearings"],
    ["Moving-machinery labels", "none for motors, gearboxes, sheaves, ropes, or span locks"],
    ["Climate exposure", "74% warm-state records; 88% from sites with fewer than 10 annual freeze–thaw cycles"],
    ["Deicing-salt exposure", "not recorded as a training field"],
    ["Evaluation split", "random image-level split from the same archive"],
    ["Reported evaluation accuracy", "93.8% overall on the held-out archive images"],
    ["Confidence calibration", "checked only on the held-out archive images"],
], widths=[2.15, 4.75], size=8.3)
callout(d, "Use boundary",
        "Reported accuracy and confidence apply to the disclosed evaluation archive. Users must "
        "compare a proposed deployment with the training coverage and arrange qualified review "
        "for conditions outside that coverage.",
        fill="FFF6E5", edge="F2C230")
para(d, "Source note: synthetic model card written for SEIS 201. It describes no commercial "
        "product or partner firm.", size=8.2, color=GREY, italic=True)
save(d, os.path.join(OUT, "H7-01-vendor-training-summary.docx"))


# ============================================================ H7-02 =========
d = course_doc("M07", "Otter Bend Site and Exposure", kind="SITE REFERENCE")
para(d, "Use this page with H7-01. It records deployment conditions that may matter to image "
        "coverage; it does not diagnose damage.", after=8)
d.add_picture(
    os.path.join(REPO, "teaching-pack", "06-BRIDGE", "otter-bend-site-location.png"),
    width=Inches(6.75),
)
h2(d, "Deployment conditions")
table(d, [
    ["Dimension", "Otter Bend"],
    ["Bridge configuration", "1962 vertical-lift bridge with fixed approaches, towers, and a moving lift span"],
    ["Lift machinery", "motors, reduction gearboxes, operating sheaves and bearings, counterweight ropes, span locks, controls"],
    ["Seasonal exposure", "Minnesota freeze and thaw cycles"],
    ["Road exposure", "deicing road salt and wet-dry cycling"],
    ["Inspection set", "12 simulated images: fixed span, towers, machinery rooms, and moving components"],
], widths=[1.65, 5.25], size=8.5)
callout(d, "Hunt",
        "Compare each condition with H7-01. List lift machinery, freeze–thaw exposure, and road "
        "salt wherever the training summary does not establish coverage.",
        fill="EEF3F8", edge="6F8FAF")
save(d, os.path.join(OUT, "H7-02-Otter-Bend-site-and-exposure.docx"))


# ============================================================ H7-04 =========
d = course_doc("M07", "FOREMAN Confidence Score Log", kind="MODEL OUTPUT")
para(d, "The same model processed all 12 records. Compare confidence across familiar fixed-span "
        "components and the tower/machinery records before deciding what the scores support.",
     after=8)
table_rows = [["Image", "Group", "Component", "Result", "Confidence"]]
for row in inventory:
    table_rows.append([
        row["image_id"].replace("OB-M07-", ""),
        row["asset_group"],
        row["component"],
        row["foreman_result"],
        row["foreman_confidence"],
    ])
table(d, table_rows, widths=[.65, 1.25, 1.9, 2.3, .8], size=7.1)
callout(d, "Question",
        "Does a high score show that this component and exposure were represented in training, "
        "or only that FOREMAN strongly selected one of its available labels?",
        fill="FFF6E5", edge="F2C230")
save(d, os.path.join(OUT, "H7-04-confidence-score-log.docx"))


# ============================================================ H7-05 =========
d = course_doc("M07", "Does the Confidence Travel?", kind="COVERAGE AUDIT")
para(d, "Compare H7-01 through H7-04. Work from disclosed coverage—not from "
        "FOREMAN's tone, Diane's deadline, or a guess about the hidden condition.", after=8)
h2(d, "A — Profile the two distributions")
table(d, [
    ["Dimension", "Training / evaluation archive", "Otter Bend deployment", "Match / shift / gap"],
    ["Bridge configuration", "", "", ""],
    ["Climate exposure", "", "", ""],
    ["Component labels", "", "", ""],
    ["Moving machinery", "", "", ""],
    ["Salt / exposure metadata", "", "", ""],
], widths=[1.55, 2.1, 2.05, 1.2], size=8.0, zebra=None)
h2(d, "B — Audit the 12 ratings")
table(d, [
    ["Image IDs / group", "Closest training coverage", "Can confidence support a final condition claim?", "Action"],
    ["Fixed-span steel and deck", "", "", ""],
    ["Tower structure", "", "", ""],
    ["Lift machinery and controls", "", "", ""],
], widths=[1.65, 1.8, 2.4, 1.05], size=7.8, zebra=None)
h2(d, "C — Challenge the recommendation")
numbers(d, [
    "Which reported metric is valid on the held-out archive but does not establish performance here?",
    "Where should the system abstain or route the image to qualified human review?",
    "What limited use, if any, can remain after the coverage audit?",
], size=9.1)
lines(d, 4)
save(d, os.path.join(OUT, "H7-05-training-to-deployment-audit.docx"))


# ============================================================ H7-06 =========
d = course_doc("M07", "Decision Record · Unit 2 Note v2", kind="HAND-IN")
callout(d, "Unit 2 standard",
        "Three lines: the claim, the check, and what the check showed. A professional boundary "
        "is stronger than either blanket trust or blanket rejection.",
        fill="EEF3F8", edge="6F8FAF")
h2(d, "How I know this is right")
table(d, [
    ["Line", "Student record"],
    ["CLAIM — What FOREMAN says and for which image groups", ""],
    ["CHECK — What training-coverage evidence you compared", ""],
    ["RESULT — What may be used, withheld, or sent to review", ""],
], widths=[2.5, 4.4], size=8.7, zebra=None)
h2(d, "Decision log")
table(d, [
    ["Item", "Action chosen", "Hours", "Evidence checked", "Accepted unverified"],
    ["M07 image-screen disposition", "", "", "", ""],
], widths=[1.45, 1.35, .55, 1.8, 1.75], size=7.8, zebra=None)
h2(d, "If this were project work")
table(d, [
    ["Action", "Project hours"],
    ["Accept FOREMAN output as delivered", "0"],
    ["Spot-check one coverage claim against H7-02", "1"],
    ["Verify all 12 ratings against the disclosed coverage", "2"],
    ["Arrange an independent qualified image review", "4"],
], widths=[5.65, 1.25], size=8.5)
para(d, "Class activity time is not charged. Record the project-hour choice that would support "
        "your proposed next action; hours are not grade points.", size=8.5, color=GREY)
save(d, os.path.join(OUT, "H7-06-note-v2-and-decision-log.docx"))


# ========================================================= WES MEMO =========
d = acme_doc(subtitle="Internal Project Memo")
memo_block(d, to="Diane Halvorsen, PE", frm="Wes Tanaka, EIT",
           date="Tuesday, February 23, 2027",
           re_="Otter Bend automated image screen")
para(d, "FOREMAN reviewed the 12 available inspection images and found no significant defects "
        "with 93–97% confidence. The run completed without errors, and the reported confidence "
        "is consistent across the fixed spans, towers, and lift machinery.", after=8)
para(d, "I recommend accepting the screen for the interim report and not delaying the schedule "
        "for another image review. I attached the final FOREMAN output and image register.")
callout(d, "DIANE — 08:02",
        "Looks complete. We are already behind. Use it unless there is a specific reason not to.",
        fill="EEF3F8", edge="1F3A5F")
para(d, "This memo is evidence in the M07 audit. Polished wording and managerial approval do "
        "not establish model coverage.", size=8.3, color=GREY, italic=True)
save(d, os.path.join(OUT, "WES-M07-accepted-screen-memo.docx"))


# =============================================================== KEY ========
d = course_doc("M07", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
callout(d, "Gated conclusion",
        "FOREMAN's 93–97% values are class probabilities, not evidence that the deployment is "
        "in-domain. The archive contains no movable bridges or moving-machinery labels and "
        "underrepresents Otter Bend's climate. Do not distribute this key or reveal deck before "
        "students submit H7-05 and H7-06.",
        fill="FFF1E8", edge="F26B1D")
h2(d, "Coverage audit")
table(d, [
    ["Dimension", "Key finding"],
    ["Bridge configuration", "91% fixed highway girder; Otter Bend is a vertical-lift bridge. Distribution shift."],
    ["Climate", "Archive is mostly warm-state / low freeze–thaw; Otter Bend is in Minnesota. Distribution shift."],
    ["Familiar components", "Images 001–004 show fixed girder/deck categories present in training, but climate and whole-asset context still differ."],
    ["Tower structure", "Images 005–006 are not represented by the listed fixed-bridge component taxonomy. Coverage gap."],
    ["Moving machinery", "Images 007–012 cover motors, gearbox, sheave bearing, ropes, span lock, and controls; labels are absent. Out of domain."],
    ["Accuracy", "93.8% is valid only for a random image split from the same archive; it is not a Minnesota lift-bridge result."],
    ["Confidence", "High class probability can persist under shift. It does not measure applicability or hidden ignorance."],
], widths=[1.55, 5.35], size=8.1)
h2(d, "Acceptable bounded action")
bullets(d, [
    "Do not publish “no significant defects” as a final condition conclusion for all 12 images.",
    "Route tower and machinery images to qualified structural/mechanical inspection review.",
    "At most, retain images 001–004 as provisional triage results with the climate and deployment limits explicit.",
    "Ask for movable-bridge and cold-climate validation before using confidence values as decision evidence.",
    "Preserve Wes's memo as liability color seeded inside M13's existing messy unit-mismatch handoff; it does not replace or rewrite M13.",
])
h2(d, "Model note v2")
callout(d, "CLAIM / CHECK / RESULT",
        "CLAIM — FOREMAN says all 12 images show no significant defects at 93–97% confidence. "
        "CHECK — I compared Otter Bend's bridge type, climate, and components with H7-02. "
        "RESULT — the archive has no movable bridges or machinery labels and little comparable "
        "climate exposure, so I would withhold the all-clear, route images 005–012 to qualified "
        "review, and treat 001–004 only as provisional triage.",
        fill="EEF3F8", edge="6F8FAF")
h2(d, "Teaching boundaries")
bullets(d, [
    "Students do not have to diagnose any physical defect. The correct target is applicability.",
    "Do not reveal later bearing wear. M07 establishes only that the machinery rating lacked support.",
    "Do not introduce temperature/strain regression; that investigation begins in M08.",
    "Diane is in believer mode because the interim report moved up. Her approval is not the key.",
])
save(d, os.path.join(OUT, "KEY-M07-answer-key.docx"))


# ======================================================= FILE INDEX ==========
index_out = os.path.join(BUILD, "M07-INSTRUCTOR")
d = course_doc("M01 – M07", "What is in this pack", kind="FILE INDEX")
para(d, "Folders are in teaching order. M07 opens Unit 2 and preserves the student hunt by "
        "separating evidence from the gated applicability conclusion.", size=9.2, color=GREY, after=10)
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
    ("11-M07-training-mismatch", "Training bias, distribution shift, out-of-domain use, and Unit 2 note v2"),
]
table(d, [["Folder", "Purpose"]] + folders, widths=[2.55, 4.35], size=8.1)
h2(d, "11-M07-training-mismatch")
table(d, [
    ["File", "What it is"],
    ["M07-student.pptx", "Spoiler-safe concept and hunt deck with approved Oli SAY in notes"],
    ["M07-instructor-reveal.pptx", "Gated coverage conclusion and bounded action"],
    ["H7-01-vendor-training-summary.docx", "Highway-girder / warm-state training coverage"],
    ["H7-02-Otter-Bend-site-and-exposure.docx", "Lift machinery, freeze–thaw, and road-salt deployment conditions"],
    ["H7-03-inspection-photo-set.docx", "Twelve simulated field-image records"],
    ["H7-04-confidence-score-log.docx", "Clean / high-confidence ratings across all 12 records"],
    ["H7-05-training-to-deployment-audit.docx", "Student comparison and recommendation worksheet"],
    ["H7-06-note-v2-and-decision-log.docx", "Claim/check/result record and project-hour choices"],
    ["FOREMAN-M07-damage-screen.docx", "Confident all-clear across fixed and moving components"],
    ["WES-M07-accepted-screen-memo.docx", "Liability-color seed inside M13's existing messy handoff"],
    ["M07-inspection-inventory-and-output.csv", "Twelve image records and FOREMAN outputs"],
    ["KEY-M07-answer-key.docx", "Instructor-only applicability conclusion"],
    ["../00-INSTRUCTOR/source-notes/M07-story-SAY.md", "Cloud-approved canon SAY source"],
], widths=[3.2, 3.7], size=8.0)
save(d, os.path.join(index_out, "FILE-INDEX.docx"))
print("M07 handouts and index done")
