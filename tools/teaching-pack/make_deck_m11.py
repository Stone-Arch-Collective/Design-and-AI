"""M11 spoiler-safe student deck and gated instructor reveal with Cloud-passed SAY."""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

OUT = os.path.join(ROOT, "build", "M11")
with open(os.path.join(OUT, "M11-dashboard-tile-register.csv"), newline="") as f:
    tiles = list(csv.DictReader(f))


def add_canon_notes(prs, notes):
    if len(prs.slides) != len(notes):
        raise ValueError(f"notes ({len(notes)}) != slides ({len(prs.slides)})")
    for slide, note in zip(prs.slides, notes):
        slide.notes_slide.notes_text_frame.text = (
            "OLI CANON SAY — Cloud hard-review PASS.\n\n" + note.strip()
        )


# ======================================================= STUDENT DECK =======
prs = deck()
title_slide(prs, "Meeting 11  ·  Unit 2: Doubt", "Permission to publish.",
            "Agentic dashboards and the human review checkpoint",
            "Tuesday, March 9, 2027  ·  SEIS 201")

s, y = content(prs, "The overnight publish request", "Five tiles · county-facing · approval requested")
speaker_card(s, .72, y + .1, 11.87, 2.25, "FOREMAN · 06:12 CST", [
    "County-facing Otter Bend health dashboard assembled overnight. Five tiles.",
    "Requesting approval to publish to the public portal. No human review requested. Confidence high.",
], machine=True, body_size=17)
speaker_card(s, .72, y + 2.65, 5.75, 1.75, "DIANE HALVORSEN, PE", [
    "“The county will see this. I am not rubber-stamping a pretty board.”"
], body_size=17)
speaker_card(s, 6.67, y + 2.65, 5.92, 1.75, "WES TANAKA, EIT", [
    "“I barely slept. I’m not walking the tiles with you — use the form.”"
], body_size=17)

image_slide(prs, "The five-tile publish candidate", os.path.join(OUT, "M11-five-tile-dashboard.png"),
            "Orange text means FOREMAN said it. Review before release.",
            caption="Do not vote by appearance. Use H11-01 and inspect every tile.", box_h=4.7)

s, y = content(prs, "You are the human review checkpoint", "One decision and one reason for every tile")
card(s, .72, y + .2, 3.75, 3.55, "APPROVE", [
    "Publish as shown", "Evidence and wording support the displayed claim"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 4.79, y + .2, 3.75, 3.55, "FIX", [
    "Retain after a named correction", "State exactly what must change"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)
card(s, 8.86, y + .2, 3.75, 3.55, "PULL", [
    "Do not publish now", "The claim cannot be corrected safely before release"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)

section(prs, "1", "A dashboard is a set of claims",
        "Compact presentation does not make a metric self-explanatory")

s, y = content(prs, "A metric needs a definition")
card(s, .72, y + .2, 5.85, 3.7, "DEFINED", [
    "What is measured", "How it is calculated", "What is included or excluded"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.7, "VISIBLE", [
    "Units or scale", "Source", "Observation and refresh time"
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=18)

s, y = content(prs, "Time series still need honest interpretation")
card(s, .72, y + .2, 5.85, 3.7, "DATA", [
    "Measurements ordered across time", "Window, units, source, and processing"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=18)
card(s, 6.72, y + .2, 5.87, 3.7, "CLAIM", [
    "Arrow, color, label, or score", "A visual cue is an interpretation—not a fact"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=18)

s, y = content(prs, "An agent-built report separates capability from authority")
card(s, .72, y + .2, 5.85, 3.75, "FOREMAN CAN", [
    "Gather fields", "Assemble tiles", "Format a board", "Request an action"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)
card(s, 6.72, y + .2, 5.87, 3.75, "A HUMAN MUST", [
    "Check the evidence", "Set the release boundary", "Record and own the publish decision"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)

statement(prs, "Autonomy can assemble the board.\nIt does not grant authority to publish.",
          "The human checkpoint is a control, not a ceremonial click.", dark=True, size=42)

section(prs, "2", "Walk every tile",
        "Definition · units · source · timestamp · claim")

activity(prs, "Review tiles 1 and 2", 12, [
    "Read the displayed value, label, color, and visual direction.",
    "Find a definition, units or scale, source, and timestamp for each.",
    "Ask whether you have seen either claim or chart story before.",
    "Mark approve, fix, or pull and write one evidence-based sentence.",
], note="Do not compare votes yet. Commit your own review.")

activity(prs, "Review tiles 3 through 5", 10, [
    "Apply the same checks; do not assume every tile fails.",
    "Distinguish a source-system status from an engineering condition claim.",
    "Check numerator, denominator, reporting window, and source time.",
    "Mark approve, fix, or pull and write one evidence-based sentence.",
], note="A clean-looking tile still needs a definition and provenance.")

activity(prs, "Make the publish decision", 8, [
    "Confirm all five rows on H11-01 have a decision and reason.",
    "Choose ALLOW PUBLISH or HOLD PUBLISH for the board as a whole.",
    "List conditions required before release.",
    "Sign the review as the human checkpoint.",
], note="The board does not go live by default.")

s, y = content(prs, "Write Unit 2 Note v2", "Claim · check · result")
card(s, .72, y + .2, 3.75, 3.65, "CLAIM", [
    "State what FOREMAN asks permission to publish."
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)
card(s, 4.79, y + .2, 3.75, 3.65, "CHECK", [
    "Name the evidence checks used across the five tiles."
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)
card(s, 8.86, y + .2, 3.75, 3.65, "RESULT", [
    "Record what may ship, what must change, and why."
], tint=CREAM, edge=GOLD, label_color=REBAR, body_size=17)

closer(prs, [
    ("HAND IN", "Completed H11-01: all five tile decisions and the board-level call."),
    ("ATTACH", "H11-04 Note version 2 and decision-log entry."),
    ("REMEMBER", "A defined source status is not automatically a condition conclusion."),
    ("BOUNDARY", "Publish is a human decision."),
], title="Before the gated reveal")

student_notes = [
    "TITLE — M11: Permission to publish. The dashboard is county-facing, so Diane Halvorsen, PE is SKEPTIC again.",
    "INBOX 10 — FOREMAN says: “County-facing Otter Bend health dashboard assembled overnight. Five tiles. Requesting approval to publish to the public portal. No human review requested. Confidence high.” Diane Halvorsen, PE: “The county will see this. I am not rubber-stamping a pretty board.” Wes Tanaka, EIT: “I barely slept. I’m not walking the tiles with you — use the form.”",
    "INBOX — Show the five-tile stub. Orange text means FOREMAN said it. Students receive the dashboard and review form. Do not identify which tiles fail.",
    "HUNT — Students are literally the human review checkpoint. For each tile: approve, fix, or pull, with a reason.",
    "TEACH TRANSITION — The dashboard is a set of claims. Compact presentation does not make any metric self-explanatory.",
    "TEACH 25 — Dashboard and metrics: a tile is only as good as its definition, units, source, and timestamp.",
    "TEACH — Time series on a dashboard still need the same honesty as a lab plot. A red arrow is a claim, not a fact.",
    "TEACH — Agent-built report and agent autonomy: FOREMAN can assemble overnight; that does not license publish.",
    "TEACH — Human review is the safety layer. Keep the two designed errors gated until students finish the hunt.",
    "LAB 30 — Open the five-tile dashboard and H11-01. Check definitions, units, sources, timestamps, and whether a time-series claim matches prior class evidence.",
    "LAB — Students review the first two tiles without being told which survive. Wes does not co-solve or tip the hunt.",
    "LAB — Students review the remaining three tiles. Some tiles can be approve-worthy; this is not a wipeout.",
    "LAB — Students complete all five decisions and make the board-level publish call before discussion.",
    "NOTE 10 — Hand in the completed review form and Note version 2: a short audit trail of what was approved, fixed, or pulled and why Diane should or should not allow publish.",
    "CLOSE — Publish is a human decision. FOREMAN can draft the board overnight; Otter Bend’s county page only goes live if a person owns the review. Leave open that chart craft still matters without naming later chart tricks.",
]
add_canon_notes(prs, student_notes)
save(prs, os.path.join(OUT, "M11-student.pptx"))


# ======================================================== REVEAL DECK =======
rev = deck()
title_slide(rev, "Meeting 11  ·  Instructor reveal", "Two tiles do not ship.",
            "Open only after all five review decisions are committed",
            "M11 · Unit 2: Doubt")

s, y = content(rev, "Designed error 1 · an undefined aggregate score")
card(s, .72, y + .2, 4.0, 3.6, "DISPLAYED", [
    "Structural health score", "87 / 100"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=24)
card(s, 4.95, y + .2, 7.64, 3.6, "MISSING", [
    "Definition or formula", "Inputs and weighting", "Source and timestamp",
    "Meaning of 87, 100, or any threshold"
], tint=PAPER, edge=CONCRETE, label_color=GIRDER, body_size=17)

s, y = content(rev, "Designed error 2 · the M08 claim was recycled")
picture(s, os.path.join(OUT, "M11-five-tile-dashboard.png"), .82, y + .2, w=7.35)
card(s, 8.45, y + .3, 4.12, 3.5, "WHY IT FAILS", [
    "Raw strain-versus-date trend", "Red “worsening” arrow",
    "Temperature-driven M08 story reused as damage evidence"
], tint=PEACH, edge=STICKER, label_color=STICKER, body_size=16)

s, y = content(rev, "Three tiles have visible definitions and provenance")
for i, tile_row in enumerate(tiles[2:]):
    card(s, .72 + i * 4.08, y + .3, 3.76, 3.65, tile_row["title"].upper(), [
        tile_row["display_value"], tile_row["definition"], tile_row["source"]
    ], tint=PAPER if i != 1 else CREAM,
       edge=CONCRETE if i != 1 else GOLD,
       label_color=GIRDER, body_size=13)

table_slide(rev, "Model checkpoint decisions", [
    ["Tile", "Model call", "Release boundary"],
    ["1 · Health score", "PULL / FIX", "No undefined aggregate score"],
    ["2 · Strain trend", "PULL / FIX", "No recycled damage inference"],
    ["3 · Join coverage", "APPROVE", "Defined exact-match metric"],
    ["4 · Quality flags", "APPROVE", "Status only; not condition"],
    ["5 · Window", "APPROVE", "Dates, count, source visible"],
], [2.2, 1.55, 6.9], size=14, y0=1.75)

statement(rev, "The board is not ready because\nits strongest-looking claims are weakest.",
          "Polish and automation do not substitute for definition and evidence.", dark=True, size=42)

s, y = content(rev, "A defensible review record")
speaker_card(s, .72, y + .2, 11.87, 2.6, "MODEL NOTE v2 · NOT REQUIRED WORDING", [
    "CLAIM — FOREMAN asks to publish five county-facing tiles without human review.",
    "CHECK — I checked definitions, units, sources, timestamps, and prior evidence.",
    "RESULT — Hold publish until the undefined score and recycled trend are removed or corrected."
], body_size=16)
card(s, .72, y + 3.15, 11.87, 1.4, "OWNERSHIP", [
    "The reviewer records what can ship, what cannot, and why."
], tint=CREAM, edge=GOLD, body_size=16)

closer(rev, [
    ("HAND IN", "Completed five-tile review form plus Note version 2."),
    ("ALLOW", "Reasoned variation when the required correction is specific."),
    ("DO NOT SHIP", "Undefined aggregate scores or recycled bad trends."),
    ("CLOSE", "Publish is a human decision."),
], title="Close M11")

reveal_notes = [
    "REVEAL — Open only after students commit all five approve/fix/pull decisions and the board-level publish call.",
    "REVEAL — Designed error one: 87 out of 100 has no definition, formula, inputs, source, or meaningful scale. An aggregate score without a definition is a red flag.",
    "REVEAL — Designed error two: FOREMAN recycled the raw midspan strain trend from M08 with a red “worsening” arrow. Students already established that the M08 story was temperature, not progressive damage.",
    "REVEAL — The other tiles can be approve-worthy because they expose definitions, units or denominators, sources, and timestamps. Source quality flags are not a bridge condition rating.",
    "REVEAL — Compare decisions. Accept FIX or PULL on the two designed errors when the reason and release boundary are specific.",
    "REVEAL — The strongest-looking claims are the weakest because polish and automation do not substitute for definition and evidence.",
    "NOTE — Diane Halvorsen, PE’s skepticism is justified: the county would have seen an undefined score and a recycled false trend. Grade the record, not agreement with Diane.",
    "CLOSE — Hand in the completed review form and Note version 2. Undefined aggregate scores and recycled bad trends do not ship to the county. Publish is a human decision.",
]
add_canon_notes(rev, reveal_notes)
save(rev, os.path.join(OUT, "M11-instructor-reveal.pptx"))
