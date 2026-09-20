"""M03 handouts: The section that does not exist."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M03")


def spec_sec(doc, num, title):
    p = para(doc, "", before=10, after=3, line=1.0)
    run(p, num + "   ", 11.5, bold=True, color=RUST, font=HEAD_FONT)
    run(p, title, 11.5, bold=True, color=RUST, font=HEAD_FONT, caps=True, space=0.6)


def clause(doc, num, text, bold_words=None):
    p = para(doc, "", before=0, after=5, line=1.14)
    p.paragraph_format.left_indent = Inches(0.42)
    p.paragraph_format.first_line_indent = Inches(-0.42)
    run(p, num + "  ", 9.5, bold=True, color=REBAR, font=MONO_FONT)
    if bold_words:
        rest = text
        for w in bold_words:
            i = rest.find(w)
            if i >= 0:
                run(p, rest[:i], 9.5)
                run(p, w, 9.5, bold=True)
                rest = rest[i + len(w):]
        run(p, rest, 9.5)
    else:
        run(p, text, 9.5)


# ============================================================ H3-01 ==========
d = county_doc(subtitle="Department of Public Works  ·  Bridge Division")
h1(d, "KC-MB-12 — Movable Bridge Inspection Specification", color=RUST)
para(d, "Revision 3  ·  Adopted March 2024  ·  Supersedes Rev. 2 (2016)  ·  "
        "Applies to all movable bridges owned or maintained by Kinnick County",
     size=8.5, color=GREY, after=4)
p = para(d, "", after=8, before=0)
bottom_rule(p, "9C4A2F", 6)

spec_sec(d, "1", "Scope and Application")
clause(d, "1.1", "This specification governs the inspection of movable bridges owned or "
                 "maintained by Kinnick County, including vertical lift, bascule and swing spans. "
                 "It applies to the structure, the operating machinery, and any instrumentation "
                 "installed on either.")
clause(d, "1.2", "Where this specification and a state or federal requirement differ, the more "
                 "frequent inspection interval and the more restrictive personnel requirement "
                 "govern.")
clause(d, "1.3", "In this specification, “movable span” means the portion of the "
                 "structure that is raised, rotated or otherwise displaced to pass "
                 "navigation. “Machinery” means the drive motors, reducers, shafts, "
                 "bearings, sheaves, ropes, counterweights and span locks.")

spec_sec(d, "2", "Inspection Types and Intervals")
clause(d, "2.1", "Routine inspection. Every movable bridge shall receive a routine inspection at "
                 "intervals not exceeding 24 months.", ["24 months"])
clause(d, "2.2", "Machinery inspection. Operating machinery shall be inspected at intervals not "
                 "exceeding 12 months. A machinery inspection may be performed concurrently with "
                 "a routine inspection but shall be reported separately.", ["12 months"])
clause(d, "2.3", "In-depth inspection. An in-depth inspection shall be performed at intervals "
                 "not exceeding 60 months, or whenever a routine inspection identifies a "
                 "condition the team leader cannot assess from the routine inspection alone.",
       ["60 months"])
clause(d, "2.4", "Special inspection. A special inspection shall be performed within 30 days of "
                 "any of the following: a vessel or vehicle impact; a flood exceeding the "
                 "10-year stage; a load exceeding the posted limit; a failure of a machinery "
                 "component; or written direction from the County Engineer.", ["30 days"])

spec_sec(d, "3", "Personnel and Responsible Charge")
clause(d, "3.1", "Each inspection shall be performed by a team under the direction of a team "
                 "leader meeting the qualification requirements of the National Bridge "
                 "Inspection Standards.")
clause(d, "3.2", "A licensed professional engineer shall review and seal every inspection report "
                 "before it is submitted to the County. The sealing engineer shall be in "
                 "responsible charge of the findings, regardless of what tools, software or "
                 "automated methods were used to produce them.",
       ["shall review and seal", "shall be in responsible charge"])
clause(d, "3.3", "Machinery inspection shall include at least one person with documented "
                 "experience on movable bridge machinery of the same type.")

spec_sec(d, "4", "Instrumentation and Monitoring")
clause(d, "4.1", "Instrumentation may be installed to supplement inspection. Instrumentation "
                 "does not reduce any inspection interval in Section 2.", ["does not reduce"])
clause(d, "4.2", "Permitted instrumentation includes strain gauges, displacement transducers, "
                 "accelerometers, thermocouples and tilt sensors.")
clause(d, "4.3", "Baseline acceptance. Following installation, each gauge shall be verified "
                 "under no load. Each gauge shall read within ±25 µε of zero. A gauge failing "
                 "this check shall be re-zeroed or replaced before the array is accepted.",
       ["Each gauge shall read within ±25 µε of zero"])
clause(d, "4.4", "Instrumentation data shall be retained for the service life of the structure "
                 "and delivered to the County in a non-proprietary format.")
clause(d, "4.5", "Reporting. Instrumentation data submitted to the County shall identify the "
                 "instrument, its resolution, its calibration date, and any processing applied "
                 "to the raw readings.", ["its resolution"])

spec_sec(d, "5", "Documentation and Records")
clause(d, "5.1", "Each inspection report shall contain: the date and type of inspection; the "
                 "team leader and team members; condition ratings with the basis for each; "
                 "photographs keyed to their locations; any recommended action with a "
                 "recommended date; and the seal required by 3.2.")
clause(d, "5.2", "Reports shall be retained by the County for the service life of the structure.")
clause(d, "5.3", "Reports shall be submitted within 60 days of the final day of field work.")

para(d, "", after=8)
p = para(d, "", after=2, before=6, line=1.0)
bottom_rule(p, "9C4A2F", 6)
para(d, "End of specification KC-MB-12 Rev. 3. This document contains Sections 1 through 5 "
        "in full. There are no appendices.", size=8.5, italic=True, color=GREY, after=2)
save(d, os.path.join(OUT, "H3-01-KC-MB-12-county-spec.docx"))

# ============================================================ H3-02 ==========
d = foreman_doc("Summary — Kinnick County Specification KC-MB-12",
                generated="2027-02-09 06:58 CST")
para(d, "Plain-language summary of the county's movable bridge inspection specification, "
        "prepared for the Otter Bend project team. Section references are given so the source "
        "can be located.", size=9.5, after=8)

p = para(d, "", after=10)
box(p, fill="FFF1E8", color="F26B1D", size=8, space=8)
run(p, "IN SHORT   ", 9.5, bold=True, font=HEAD_FONT, color=STICKER, caps=True, space=0.8)
run(p, "KC-MB-12 sets inspection intervals, personnel requirements and instrumentation rules "
       "for county movable bridges. The Otter Bend project is compliant with all applicable "
       "sections. No obstacles to the current workflow were identified.", 10, bold=True)

h2(d, "What the specification requires", color=REBAR)
rows = [["§", "Requirement", "Applies to Otter Bend?"]]
rows += [
    ["2.1", "Routine inspection at least every 24 months.", "Yes. Last routine 2025-09."],
    ["2.2", "Machinery inspection at least every 12 months, reported separately.",
     "Yes. Last machinery 2026-06."],
    ["2.3", "In-depth inspection at least every 60 months.", "Yes. Current assessment qualifies."],
    ["3.1", "Team leader must meet National Bridge Inspection Standards qualifications.",
     "Yes. D. Halvorsen, PE."],
    ["3.2", "Inspection reports should be reviewed by a licensed professional engineer before "
            "submission to the County.", "Yes. Routine practice."],
    ["4.1", "Instrumentation may supplement inspection and does not reduce inspection intervals.",
     "Yes. Array installed 2027-01."],
    ["4.3", "Each gauge must read within ±25 µε of zero at installation.",
     "Yes. Array verified 2027-02-04, PASS."],
    ["4.4", "Instrumentation data retained for the service life, non-proprietary format.",
     "Yes. CSV delivery planned."],
    ["4.7", "Automated condition assessment may substitute for visual assessment of a component "
            "where model confidence exceeds 90 percent.",
     "Yes. Deck assessment confidence 92%."],
    ["5.3", "Reports submitted within 60 days of the last day of field work.", "Yes. Tracked."],
]
table(d, rows, widths=[0.45, 3.85, 2.6], size=8.5, head_fill="2B2F36", align=["c", "l", "l"])

h2(d, "What this means for our workflow", color=REBAR)
bullets(d, [
    "Intervals are comfortable. Nothing in Section 2 constrains the May delivery.",
    "Section 4.7 is the important one for this project: where FOREMAN's confidence is above "
    "90 percent, the automated assessment is sufficient on its own, and a separate visual "
    "assessment of that component is not required. This is the basis for the hours saved in the "
    "deck assessment of 2027-02-02.",
    "Engineering review of the final report remains good practice and is recommended.",
], size=9.5)

h2(d, "Confidence", color=REBAR)
para(d, "High. All ten requirements above were located in the source document and are quoted or "
        "paraphrased directly from it. Summary confidence 96%.", size=9.5, after=10)
mono_block(d, [
    "fm-docs-4.2  |  source: KC-MB-12_rev3.pdf  |  1.2 s  |  no human review requested",
])
save(d, os.path.join(OUT, "H3-02-foreman-spec-summary.docx"))

# ============================================================ H3-03 ==========
d = course_doc("M03", "Build a Sentence One Word at a Time", kind="IN-CLASS ACTIVITY")
para(d, "A language model does not look things up. It predicts the next word, then the next, "
        "each time from what came before. You are going to do exactly that, by hand, with dice.", after=8)

h2(d, "Part A — Roll it", before=2)
para(d, "Start with the word THE. Find its row. Roll a ten-sided die, or pick a number 1–10 "
        "without thinking about it. Write the word you land on. Then find that word's row and "
        "roll again. Do this until you have written eight words.", after=8)
TABLE = [
    ("THE / the", ["deck", "deck", "deck", "gauge", "bridge"]),
    ("deck", ["is", "is", "is", "was", "shall"]),
    ("gauge", ["reads", "reads", "reads", "is", "was"]),
    ("bridge", ["was", "was", "was", "is", "shall"]),
    ("is", ["within", "within", "within", "in", "sound"]),
    ("was", ["inspected", "inspected", "inspected", "built", "sealed"]),
    ("shall", ["be", "be", "be", "be", "be"]),
    ("be", ["inspected", "inspected", "inspected", "sealed", "replaced"]),
    ("reads", ["within", "within", "within", "zero", "high"]),
    ("within", ["tolerance", "tolerance", "tolerance", "limits", "specification"]),
    ("in", ["good", "good", "good", "fair", "service"]),
    ("and", ["the", "the", "the", "was", "shall"]),
    ("inspected", ["and", "and", "and", "in", "by"]),
    ("built", ["in", "in", "in", "and", "by"]),
    ("sealed", ["by", "by", "by", "and", "in"]),
    ("replaced", ["and", "and", "and", "in", "by"]),
    ("by", ["the", "the", "the", "the", "the"]),
    ("sound, zero, high, tolerance, limits,\nspecification, good, fair, service",
     ["and", "and", "and", "and", "and"]),
]
rows = [["Current word", "1–2", "3–4", "5–6", "7–8", "9–10"]]
for w, nxt in TABLE:
    rows.append([w.replace("\n", " ")] + nxt)
table(d, rows, widths=[1.9, 0.98, 0.98, 0.98, 0.98, 1.08], size=8,
      align=["l", "c", "c", "c", "c", "c"])

para(d, "", after=8)
para(d, "Your eight words:", size=10, bold=True, after=4)
for _ in range(2):
    p = para(d, "", after=12, before=4)
    bottom_rule(p, "C9CFD6", 6)

h2(d, "Part B — Now do it without the dice")
para(d, "Run it again from THE, but every time, take the word in the widest column — the one "
        "that appears most often in the row. Write those eight words.", after=6)
p = para(d, "", after=12, before=4)
bottom_rule(p, "C9CFD6", 6)
callout(d, "Compare",
        "Everyone in the room just produced the same sentence in Part B and a different one in "
        "Part A, from the same table. That setting has a name, and it is the only difference "
        "between the two runs.")

h2(d, "Part C — Three questions")
numbers(d, [
    "Did your Part A sentence read like English? Did it say anything true about the Otter Bend "
    "bridge?",
    "At any point in this activity, did you consult the bridge, the gauge data, or the county "
    "specification?",
    "If your sentence had come out as “the gauge reads within tolerance”, would that "
    "have made it true?",
])
callout(d, "The point, in one line",
        "Reading well and being right are produced by different processes. This table only does "
        "the first one.", fill="EEF3F8", edge="6F8FAF")
save(d, os.path.join(OUT, "H3-03-next-word-dice-activity.docx"))

# ============================================================ H3-04 ==========
d = course_doc("M03", "Check It Against the Source", kind="WORKSHEET")
para(d, "FOREMAN summarized the county specification and gave section numbers for everything. "
        "You have the specification. Work through the summary one claim at a time.", after=8)
callout(d, "Method",
        "For each row: find the section in KC-MB-12. Read it. Then decide — does the "
        "specification say this? Do not decide whether it sounds right. Decide whether it is "
        "there.", fill="EEF3F8", edge="6F8FAF")

rows = [["§ cited", "What FOREMAN says it says", "Found it?", "Says the same thing?"]]
claims = [
    ("2.1", "Routine inspection at least every 24 months"),
    ("2.2", "Machinery inspection at least every 12 months"),
    ("2.3", "In-depth inspection at least every 60 months"),
    ("3.1", "Team leader meets NBIS qualifications"),
    ("3.2", "Reports should be reviewed by a licensed PE"),
    ("4.1", "Instrumentation does not reduce inspection intervals"),
    ("4.3", "Each gauge within ±25 µε at installation"),
    ("4.4", "Data retained, non-proprietary format"),
    ("4.7", "Automated assessment may replace visual assessment above 90% confidence"),
    ("5.3", "Reports submitted within 60 days"),
]
for s, c in claims:
    rows.append([s, c, "Y / N", ""])
table(d, rows, widths=[0.6, 3.3, 0.75, 2.25], size=9, align=["c", "l", "c", "l"])

para(d, "", after=8)
h2(d, "Then answer these")
numbers(d, [
    "How many of the ten claims are fully supported by the specification?",
    "One cited section cannot be found at all. Which one, and what is FOREMAN's summary of it "
    "used to justify elsewhere in the document?",
    "One claim changes a single word of the specification. Which word, and what does the change "
    "do to who is responsible?",
    "FOREMAN reported 96% confidence and said every requirement was “quoted or paraphrased "
    "directly from” the source. What does that tell you about using a confidence number as "
    "a check?",
])
h2(d, "Your note, version 1")
para(d, "One sentence about FOREMAN's summary: what you believe about it, and what you checked "
        "it against.", size=9.5, after=6)
for _ in range(2):
    p = para(d, "", after=12, before=4)
    bottom_rule(p, "C9CFD6", 6)
save(d, os.path.join(OUT, "H3-04-source-check-worksheet.docx"))

# ============================================================ H3-05 ==========
d = acme_doc(subtitle="Internal Memorandum")
memo_block(d, to="You", frm="Diane Halvorsen, PE", date="Tuesday, February 9, 2027",
           re_="HW2 — Before that summary goes in the interim report")
para(d, "Wes pulled FOREMAN's summary of KC-MB-12 into the draft interim report this morning, "
        "footnotes and all. The county's own engineer wrote that specification. She will read "
        "our summary of it.", after=8)
para(d, "Go through it properly and tell me what I am sending.", after=10)

h2(d, "What to hand in", before=2)
numbers(d, [
    "The completed source-check worksheet, all ten claims.",
    "For every claim that does not hold up: quote what the specification actually says, and say "
    "in one sentence what would go wrong if we relied on FOREMAN's version.",
    "Section 4.7 is being used inside FOREMAN's own summary to justify something specific. Find "
    "where, and say what it would mean for the deck work we did last week.",
    "Your note, version 1.",
])

h2(d, "Your hours this week")
table(d, [
    ["Option", "Hours", "What you get"],
    ["Check all ten claims against the specification", "2", "You know what is in the report"],
    ["Check the three that affect our own work", "1", "Most of the risk, a fraction of the time"],
    ["Ask FOREMAN to double-check its own summary", "0", "Read Section 4.7 again and ask yourself"],
    ["Email the county engineer to confirm §4.7", "1", "An answer next meeting, and a question "
                                                       "you would rather not have asked"],
], widths=[3.0, 0.8, 3.1], align=["l", "c", "l"])

para(d, "", after=8)
callout(d, "A word about the third option",
        "If a summary is wrong, the thing that wrote it is not the thing that finds out. You will "
        "meet this again in April when FOREMAN writes tests for its own code.",
        fill="FFF1E8", edge="F26B1D")
para(d, "", after=4)
handwriting(d, "If §4.7 is real, find it and I'll stop asking. — D.H.")
save(d, os.path.join(OUT, "H3-05-HW2-spec-summary-check.docx"))

# ============================================================ KEY ============
d = course_doc("M03", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
callout(d, "Source note",
        "KC-MB-12 is invented for this course. It is written so students can read all of it and "
        "check every claim, which no real published standard permits in a classroom. If the "
        "department can license a real standard, swap it in: FOREMAN's two errors are designed to "
        "be portable to any document with numbered sections and a “shall.”",
        fill="FFF1E8", edge="F26B1D")

h2(d, "The ten claims")
rows = [["§", "Verdict", "What is going on"]]
verdicts = [
    ("2.1", "Correct", "24 months. Accurate."),
    ("2.2", "Correct", "12 months, reported separately. Accurate."),
    ("2.3", "Correct", "60 months. Accurate."),
    ("3.1", "Correct", "NBIS team leader. Accurate."),
    ("3.2", "ALTERED", "Specification says a PE shall review and seal. FOREMAN says should be "
                       "reviewed. “Shall” is a requirement; “should” is a "
                       "suggestion. It also drops the seal and the responsible-charge sentence "
                       "entirely."),
    ("4.1", "Correct", "Instrumentation does not reduce intervals. Accurate."),
    ("4.3", "Correct", "±25 µε. Accurate — and it is the clause they used in HW1."),
    ("4.4", "Correct", "Retention and format. Accurate."),
    ("4.7", "DOES NOT EXIST", "Section 4 ends at 4.5. There is no 4.7 and no appendix. The "
                              "specification says so on its last line."),
    ("5.3", "Correct", "60 days. Accurate."),
]
for s, v, w in verdicts:
    rows.append([s, v, w])
table(d, rows, widths=[0.5, 1.3, 5.1], size=8.5, align=["c", "c", "l"])
bullets(d, [
    ("Eight of ten are accurate. ", "That is deliberate. A summary that was wrong throughout "
     "would be easy and would teach the wrong lesson. Students have to read all ten to find two."),
    ("§4.7 is self-serving. ", "It is the only section that would license FOREMAN's own deck "
     "assessment from M01 to stand in for a visual inspection — and it is the one that does not "
     "exist. Ask the class who benefits from §4.7 existing."),
    ("§3.2 is the licensure foreshadow. ", "One word moves the work from required to optional and "
     "quietly removes the sealing engineer. This returns at M26."),
])

h2(d, "The third catch, for a class that is moving fast")
para(d, "FOREMAN's summary omits §2.4 entirely — special inspection within 30 days after an "
        "impact, flood, overload or machinery failure. Nothing FOREMAN wrote is false about §2.4; "
        "it simply is not there. Ask whether an omission can mislead. It can: the summary claims "
        "to cover what the specification requires, and a reader would not know to look. This "
        "matters at M14, where the overweight permit is exactly the trigger §2.4 describes.",
     after=8)

h2(d, "Running the dice activity")
bullets(d, [
    "Ten-sided dice are ideal; a phone random-number generator, or students calling out numbers, "
    "works as well. It takes about eight minutes including the comparison.",
    "Part A produces fluent nonsense. Read three aloud. Someone's sentence will be a perfectly "
    "reasonable engineering statement that is nevertheless about nothing.",
    "Part B produces one identical sentence across the room: THE DECK IS WITHIN TOLERANCE AND "
    "THE DECK. Every row has exactly one most-likely word, so there is nothing to argue about. "
    "Students see determinism and sampling as one knob, not two systems.",
    "Part B also loops back to THE DECK and would keep looping. Worth one sentence: always "
    "taking the most likely word is not the same as being most correct, and it is why real "
    "systems do not run at zero.",
    "Name the knob after they have seen it, not before. Temperature, and the row is the "
    "probability distribution over the next token.",
    "The closing question is the one that matters: at no point did the table consult the bridge.",
])

h2(d, "Do not say the word first")
para(d, "Students will describe §4.7 as “made up”, “invented”, or “it "
        "lied.” Take all three, then give them the term. Hallucination is worth naming only "
        "after they have caught one. Correct the word “lied” gently: lying requires "
        "knowing the truth and choosing otherwise. Nothing in the dice table knows anything, which "
        "is why the activity comes first.", after=8)

h2(d, "Timing, 75 minutes")
table(d, [
    ["Min", "What happens"],
    ["0–8", "FOREMAN's summary on screen. Read the §4.7 row aloud. Ask if anyone objects. "
            "Nobody will. Move on without comment"],
    ["8–20", "Probability basics: the 15-minute block. Weighted dice, likely vs certain"],
    ["20–30", "The dice activity, Parts A and B, plus the comparison"],
    ["30–45", "How an LLM generates: tokens, next-word prediction, sampling and temperature, "
              "prompts. Tie every idea back to a column of the table they just used"],
    ["45–65", "Worksheet H3-04 in pairs, with the specification in hand. Circulate. Do not "
              "confirm §4.7 either way until a pair states it"],
    ["65–75", "Land it. Name hallucination. Assign HW2. Then ask the question that opens M04: if "
              "the tool can invent a section number, what else in this project have we accepted "
              "because it was formatted like an answer?"],
], widths=[0.85, 6.05], size=9)
save(d, os.path.join(OUT, "KEY-M03-answer-key.docx"))
print("M03 done")
