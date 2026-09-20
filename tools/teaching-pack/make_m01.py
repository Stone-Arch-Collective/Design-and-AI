"""M01 handouts: First day. Rules versus learned patterns."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "M01")
F = FACTS["m01"]

# ============================================================ H1-01 ==========
d = acme_doc(subtitle="Internal Memorandum")
memo_block(d,
           to="New engineering staff, Otter Bend project",
           frm="Diane Halvorsen, PE — Principal Engineer",
           date="Monday, February 2, 2027",
           re_="What this job is, and the one thing I ask")

para(d, "Welcome. You start today on the biggest job this office has, and I would rather you "
        "hear how I work from me than figure it out by getting something wrong.", after=8)

h2(d, "The job", before=8)
para(d, "The Otter Bend Lift Bridge carries County Road 9 over the Kinnick River. It was built in "
        "1962, it is a vertical lift span, and it is carrying loads nobody designed it for. Kinnick "
        "County has put strain, temperature and vibration sensors on it, and they want an answer by "
        "May: rehabilitate it, or replace it. That answer will be a number with my stamp on it.", after=8)

h2(d, "The part you were sold")
para(d, "Two years ago this firm added two letters to its name and told the county we could assess "
        "this bridge faster and cheaper than anyone else, because we have FOREMAN. You will use "
        "FOREMAN. I am not going to tell you not to. It is quick, it reads more than I can read, and "
        "it does not get tired at four in the afternoon.", after=8)
para(d, "It is also wrong sometimes, and it is never less confident when it is wrong. That is the "
        "part nobody put in the proposal.", after=8)

h2(d, "The one thing I ask")
p = para(d, "", after=8)
box(p, fill="FFF6E5", color="F2C230", size=10, space=8)
run(p, "Every number you hand me comes with one sentence: how do you know that is right?", 12,
    bold=True, color=REBAR, font=HEAD_FONT)
para(d, "One sentence. Not a report. I am not asking you to prove the number from first principles "
        "every time — you would never finish. I am asking you to know which check you did, so that "
        "when the county asks me, I have an answer that is not \u201cthe computer said so.\u201d", after=8)
para(d, "I have been asked that question my whole career, often by people who did not ask it of the "
        "man sitting next to me. I learned to always have the answer ready. You will too.", after=10)

h2(d, "Today")
numbers(d, [
    "Read the load rating sheet. Work the rating factor for Girder G-4 by hand. It is arithmetic; "
    "you do not need to have taken structures yet.",
    "Read FOREMAN's deck condition assessment and my 2019 inspection notes on the same panels.",
    "Sort the task cards: which of these is a rule, which is a learned pattern, and which is both.",
    "Hand me your note. One sentence.",
])

para(d, "", after=2)
handwriting(d, "— Welcome aboard. Coffee is terrible. Machine is in the north hall. — D.H.")

save(d, os.path.join(OUT, "H1-01-orientation-memo-halvorsen.docx"))

# ============================================================ H1-02 ==========
d = acme_doc(subtitle="Calculation Sheet  ·  Load Rating")
h1(d, "Simplified Load Rating — Approach Span Girders")
para(d, "ACMEJOB.Ai standard sheet LR-1. Use for interior girders of the Otter Bend north and south "
        "approach spans only. This is a teaching simplification of the operating rating procedure; "
        "it is not a substitute for the governing rating manual.", size=9, italic=True,
     color=GREY, after=10)

h2(d, "The rule", before=4)
p = para(d, "", after=6)
box(p, fill="F4F6F8", color="C9CFD6", size=6, space=8)
run(p, "RF  =  ( C − D ) ÷ ( L × IM )", 15, bold=True, font=MONO_FONT, color=GIRDER)
p2 = para(d, "", after=10)
box(p2, fill="F4F6F8", color="C9CFD6", size=6, space=8)
run(p2, "Rating (tons)  =  RF × 36", 15, bold=True, font=MONO_FONT, color=GIRDER)

table(d, [
    ["Symbol", "Means", "Where it comes from"],
    ["C", "Girder moment capacity, kip-ft", "Section properties + material tests"],
    ["D", "Dead load moment, kip-ft", "Weight of the structure itself"],
    ["L", "Live load moment, kip-ft", "The rating truck, here an HS-20 at 36 tons"],
    ["IM", "Impact factor (dimensionless)", "Allowance for a moving load bouncing. 1.33 here."],
    ["RF", "Rating factor", "Above 1.00 the girder carries the rating truck."],
], widths=[0.75, 2.05, 4.05], align=["c", "l", "l"])

h2(d, "Worked example — Girder G-3, south approach")
table(d, [
    ["Step", "Substitution", "Result"],
    ["1. Capacity minus dead load", "3,920 − 1,455", "2,465 kip-ft"],
    ["2. Live load with impact", "1,080 × 1.33", "1,436.4 kip-ft"],
    ["3. Rating factor", "2,465 ÷ 1,436.4", "1.716"],
    ["4. Rating in tons", "1.716 × 36", "61.8 tons"],
], widths=[2.15, 2.35, 2.35], align=["l", "l", "r"])
callout(d, "Reading it", "RF is 1.716, which is above 1.00, so G-3 carries the rating truck with "
                         "room to spare. Every step above can be checked by someone who was not in "
                         "the room. That is the whole point of a rule.")

h2(d, "Your turn — Girder G-4, south approach")
para(d, "G-4 sits under the wheel line and its bottom flange has section loss from 60 years of "
        "runoff, so its capacity is lower. Dead and live load are unchanged.", after=6)
table(d, [
    ["Input", "Value"],
    ["C, capacity (reduced for section loss)", f"{F['capacity_kipft']:,.0f} kip-ft"],
    ["D, dead load moment", f"{F['dead_kipft']:,.0f} kip-ft"],
    ["L, live load moment", f"{F['live_kipft']:,.0f} kip-ft"],
    ["IM, impact factor", f"{F['impact']}"],
], widths=[4.4, 2.5], align=["l", "r"])

para(d, "", after=4)
rows = [["Step", "Show your substitution", "Result"]]
for s in ["1. C − D", "2. L × IM", "3. RF = step 1 ÷ step 2", "4. Rating = RF × 36"]:
    rows.append([s, "", ""])
table(d, rows, widths=[2.15, 2.85, 1.9], align=["l", "l", "r"], zebra=None)

para(d, "", after=6)
callout(d, "Before you move on",
        "Is your RF above or below 1.00? Say in one sentence what that means for a 36-ton truck "
        "crossing the south approach, and what you would want to know before saying it out loud "
        "to the county.",
        fill="EEF3F8", edge="6F8FAF")

save(d, os.path.join(OUT, "H1-02-load-rating-sheet.docx"))

# ============================================================ H1-03 ==========
d = foreman_doc("Deck Condition Assessment — Otter Bend Lift Bridge",
                generated="2027-02-02 07:41 CST")
para(d, "Automated condition rating of 6 deck panels from inspection photography captured "
        "2027-01-28. Ratings follow the standard 9-point condition scale (9 = excellent, "
        "1 = failed).", size=9.5, after=8)

p = para(d, "", after=10)
box(p, fill="FFF1E8", color="F26B1D", size=8, space=8)
run(p, "SUMMARY   ", 9.5, bold=True, font=HEAD_FONT, color=STICKER, caps=True, space=0.8)
run(p, "Deck is in fair to good condition overall. Mean panel rating 6.8. No panel rated below 6. "
       "No immediate action required. Model confidence is high across all panels "
       "(mean 92.0%).", 10, bold=True)

rows = [["Panel", "Condition rating", "Model confidence", "Assessment"]]
labels = {8: "Good", 7: "Good", 6: "Satisfactory", 5: "Fair"}
for pid, rating, conf, _d19, _note in FACTS["m01_panels"]:
    rows.append([pid, str(rating), f"{conf*100:.0f}%", labels[rating]])
table(d, rows, widths=[1.2, 1.8, 1.8, 2.1], align=["c", "c", "c", "l"],
      head_fill="2B2F36")

h2(d, "Method", color=REBAR)
para(d, "Each panel image was evaluated by the fm-vision condition model, trained on 41,800 "
        "labelled bridge deck images. Ratings are produced directly from image features. "
        "Confidence is the model's own estimate of its accuracy on each image.", size=9.5, after=8)

h2(d, "Recommendation", color=REBAR)
para(d, "Proceed to load rating and machinery assessment. Deck condition does not appear to be "
        "a controlling factor in the rehabilitate-versus-replace decision. Recommend deferring "
        "further deck investigation to reduce project hours.", size=10, after=10)

mono_block(d, [
    "fm-vision-4.2  |  6 images  |  1.9 s  |  no human review requested",
    "sources: IMG_2841..IMG_2846 (2027-01-28, handheld, deck level)",
])

save(d, os.path.join(OUT, "H1-03-foreman-deck-assessment.docx"))

# ============================================================ H1-04 ==========
d = acme_doc(subtitle="Field File  ·  Otter Bend Deck Panels")
h1(d, "Deck Panel History — D. Halvorsen field notes")
para(d, "Transcribed from the 2019 biennial inspection field book. Same six panels FOREMAN "
        "assessed. Ratings on the same 9-point scale.", size=9, italic=True, color=GREY, after=10)

rows = [["Panel", "2019 rating", "What I saw", "Note"]]
for pid, _f, _c, d19, note in FACTS["m01_panels"]:
    rows.append([pid, str(d19), note, ""])
table(d, rows, widths=[0.8, 1.0, 3.7, 1.4], align=["c", "c", "l", "l"])

para(d, "", after=6)
handwriting(d, "D-15 was overlaid in 2018. You cannot see the deck. Do not let anyone tell you "
               "it improved. — D.H.")

h2(d, "Why this file exists")
para(d, "A condition rating is a judgement about a thing you often cannot see. The 2019 ratings "
        "were made by a person who could tap the deck with a hammer, drag a chain across it and "
        "listen, and who remembered what was done to each panel and when. A photograph carries "
        "none of that.", after=8)
callout(d, "Compare", "Put FOREMAN's 2027 ratings next to the 2019 ratings, panel by panel. Five "
                      "panels are close. One is not. Before you decide who is right, ask what "
                      "each source could possibly have known.")

save(d, os.path.join(OUT, "H1-04-deck-panel-history-2019.docx"))

# ============================================================ H1-05 ==========
d = course_doc("M01", "Task Sort — Rule, Learned Pattern, or Both", kind="IN-CLASS ACTIVITY")
para(d, "Nine things ACMEJOB.Ai does on the Otter Bend job. Cut the cards apart, or just number "
        "your answers. For each one decide how you would build it, and write the one piece of "
        "evidence that would convince you it works.", after=8)

table(d, [
    ["If you would build it with", "Then it is", "And you check it by"],
    ["A formula, a lookup, a threshold — steps someone can write down",
     "A rule", "Working the steps yourself"],
    ["Showing a machine thousands of examples until it picks up the pattern",
     "A learned pattern", "Testing it on examples it has never seen"],
], widths=[3.2, 1.6, 2.1])

para(d, "", after=8)
tasks = [
    "Compute the rating factor for a girder from its section properties.",
    "Decide which of 400 inspection photographs show spalling.",
    "Check that the lift span counterweight balances the span within 2%.",
    "Draft the cover letter that goes to the county with the report.",
    "Flag any strain reading above 250 microstrain within one minute of it arriving.",
    "Predict which deck panels will need repair within five years.",
    "Convert a span length of 42 ft 7 in to metres.",
    "Decide whether a crack pattern in a pier is fatigue or shrinkage.",
    "Look up the minimum inspection interval for lift machinery in the county specification.",
]
rows = [["#", "Task", "Rule / Learned / Both", "What would convince you"]]
for i, t in enumerate(tasks, 1):
    rows.append([str(i), t, "", ""])
table(d, rows, widths=[0.35, 3.0, 1.55, 2.0], align=["c", "l", "c", "l"])

para(d, "", after=6)
callout(d, "The argument", "Two of these nine are genuinely arguable, and the argument is the "
                           "lesson. Be ready to say which two, and why.",
        fill="EEF3F8", edge="6F8FAF")
save(d, os.path.join(OUT, "H1-05-task-sort-activity.docx"))

# ============================================================ H1-06 ==========
d = course_doc("M01", "The Note — Version 1", kind="TEMPLATE + RUBRIC")
para(d, "Every piece of work you hand in at ACMEJOB.Ai carries a note. In February the note is one "
        "sentence. It gets longer as the semester goes on, and it gets longer because you will have "
        "more ways to check things, not because anyone wants more writing.", after=10)

h2(d, "The form", before=2)
p = para(d, "", after=10)
box(p, fill="FFF6E5", color="F2C230", size=10, space=10)
run(p, "I believe ", 12, font=HEAD_FONT)
run(p, "[the number or claim]", 12, bold=True, color=STICKER, font=HEAD_FONT)
run(p, " is right because I checked it against ", 12, font=HEAD_FONT)
run(p, "[the thing you checked it against]", 12, bold=True, color=STICKER, font=HEAD_FONT)
run(p, ".", 12, font=HEAD_FONT)

h2(d, "Three examples")
table(d, [
    ["Note", "Verdict"],
    ["\"I believe the rating factor of 1.69 is right because I worked the arithmetic twice and "
     "the second pass matched.\"", "Strong. Names the claim and a real check."],
    ["\"I believe the deck is in fair condition because FOREMAN rated it 6.8 with 92% "
     "confidence.\"", "Weak. Confidence is not a check. Nothing was compared to anything."],
    ["\"I checked it.\"", "No. Checked what, against what?"],
], widths=[4.6, 2.3])

h2(d, "How it is graded")
table(d, [
    ["", "3 — Meets the bar", "2 — Partial", "1 — Not yet"],
    ["Names the claim", "States the specific number or conclusion",
     "Vague about which claim", "No claim named"],
    ["Names a real check", "A check someone else could repeat",
     "A check that leans on the tool that produced the answer",
     "Restates confidence, or asserts correctness"],
    ["Honest about limits", "Says what was not checked when it matters",
     "Silent on limits", "Claims more certainty than the check supports"],
], widths=[1.3, 2.0, 1.8, 1.8], size=8.5)

para(d, "", after=8)
callout(d, "Two things that are not true",
        "A note is not graded on whether the number turned out to be right. It is graded on "
        "whether the check was real and the claim was honest. And Diane's reaction is not your "
        "grade — she is a character, she skims, and some weeks she is in a hurry.",
        fill="EEF3F8", edge="6F8FAF")

para(d, "", after=10)
h2(d, "Your note for today")
for _ in range(3):
    p = para(d, "", after=14, before=6)
    bottom_rule(p, "C9CFD6", 6)
save(d, os.path.join(OUT, "H1-06-note-v1-template-rubric.docx"))

# ============================================================ KEY ============
d = course_doc("M01", "Answer Key and Teaching Notes", kind="INSTRUCTOR ONLY")
h2(d, "H1-02 Load rating, Girder G-4", before=2)
table(d, [
    ["Step", "Substitution", "Result"],
    ["1. C − D", f"{F['capacity_kipft']:,.0f} − {F['dead_kipft']:,.0f}", f"{F['numerator']:,.0f} kip-ft"],
    ["2. L × IM", f"{F['live_kipft']:,.0f} × {F['impact']}", f"{F['live_times_impact']:,.1f} kip-ft"],
    ["3. RF", f"{F['numerator']:,.0f} ÷ {F['live_times_impact']:,.1f}", f"{F['RF']}"],
    ["4. Rating", f"{F['RF']} × 36", f"{F['rating_tons']} tons"],
], widths=[1.6, 2.6, 2.7], align=["l", "l", "r"])
bullets(d, [
    ("Expected answer: ", f"RF = {F['RF']}, rating {F['rating_tons']} tons. Accept 1.69–1.70 and 60.8–61.0."),
    ("The point: ", "every step is checkable by a stranger. Contrast with H1-03, where no step is."),
    ("Common error: ", "applying impact to the dead load as well. Ask why impact belongs only on the moving load."),
    ("If someone finishes early: ", "ask what happens to RF if the section loss is worse than "
     "assumed and C drops to 3,500. (RF = 1.448, rating 52.1 tons — still above 1.00.)"),
])

h2(d, "H1-03 vs H1-04 — the comparison")
table(d, [
    ["Panel", "FOREMAN 2027", "Halvorsen 2019", "What is going on"],
    ["D-12", "7 (94%)", "7", "Agrees."],
    ["D-13", "7 (91%)", "6", "One point better after 8 years. Arguable, not alarming."],
    ["D-14", "6 (88%)", "6", "Agrees."],
    ["D-15", "8 (96%)", "5", "The one that matters. Overlaid in 2018 — the model is rating the "
                              "overlay, not the deck, and is most confident here."],
    ["D-16", "6 (90%)", "6", "Agrees."],
    ["D-17", "7 (93%)", "7", "Agrees."],
], widths=[0.7, 1.35, 1.35, 3.5], size=8.5)
callout(d, "The move to make",
        "Ask the class which panel FOREMAN was most confident about. It is D-15, at 96% — the one "
        "it got most wrong. Confidence went up because the overlay is smooth and photographs "
        "cleanly. Let that sit before explaining it. Do not use the word 'hallucination' today; "
        "that arrives at M03.")
bullets(d, [
    "Nobody is wrong here. The photo model answered the question it was asked. The question was "
    "the wrong one.",
    "A deck rating is a claim about material you cannot see. That is a limit of the input, not a "
    "flaw in the algorithm — and no amount of training data fixes it.",
])

h2(d, "H1-05 Task sort")
table(d, [
    ["#", "Task", "Answer", "Why"],
    ["1", "Rating factor", "Rule", "Arithmetic on measured inputs."],
    ["2", "Spalling in 400 photos", "Learned", "Nobody can write the rule for what spalling looks like."],
    ["3", "Counterweight balance", "Rule", "Statics. Sum of moments."],
    ["4", "Cover letter", "Learned", "Language. Note that 'it reads well' is not 'it is correct'."],
    ["5", "Threshold flag at 250 µε", "Rule", "A comparison. Returns at M05 inside an agent."],
    ["6", "Predict 5-year repairs", "Learned", "Pattern over history. Ask what data you would need."],
    ["7", "42 ft 7 in to metres", "Rule", "Unit conversion. 12.98 m."],
    ["8", "Fatigue or shrinkage crack", "Both — argue it", "A model can sort images; the call "
                                                           "needs load history and context. Human decides."],
    ["9", "Look up an interval in the spec", "Both — argue it", "Retrieval looks like a rule, but "
                                                                "an LLM generates rather than looks up. This is the M03 setup."],
], widths=[0.3, 1.9, 1.35, 3.35], size=8.5)
callout(d, "Land #9 deliberately",
        "Most students call #9 a rule. It is a rule if you open the document. It is not a rule if "
        "you ask a language model, because the model produces text that looks like the document "
        "rather than reading it. Say you will come back to this on Tuesday, and do not explain "
        "further. M03 is the payoff.", fill="EEF3F8", edge="6F8FAF")

h2(d, "Closing 10 minutes")
numbers(d, [
    "Collect the notes. Read two aloud, anonymously — one strong, one weak. Do not identify anyone.",
    "State plainly, once: Diane is a character. Her approval is never the grade. The rubric is.",
    "Assign HW1 (handed out at M02) and tell them Thursday is hands-on — they will measure "
    "something physical before they touch any sensor data.",
])
save(d, os.path.join(OUT, "KEY-M01-answer-key.docx"))
print("M01 done")
