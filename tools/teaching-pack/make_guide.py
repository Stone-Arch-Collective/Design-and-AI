"""Instructor guide for M01-M03."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *

OUT = os.path.join(BUILD, "00-INSTRUCTOR")
F, G, P = FACTS["m01"], FACTS["m02"], FACTS["m02_pin"]

d = course_doc("M01 – M03", "Instructor Guide", kind="INSTRUCTOR ONLY")
para(d, "Everything needed to run the first three meetings of SEIS 201, Spring 2027. Draft. No "
        "engineer or statistics instructor has reviewed the technical content; the items needing "
        "review are listed on the last page.", size=9.5, italic=True, color=GREY, after=10)

# ---------------------------------------------------------------------------
h2(d, "The shape of the three meetings", before=2)
table(d, [
    ["", "M01 — Tue Feb 2", "M02 — Thu Feb 4", "M03 — Tue Feb 9"],
    ["Teaches", "Rules vs learned patterns (6 concepts)",
     "Measurement and uncertainty (6)", "LLMs and probability (7)"],
    ["Hands-on", "Task sort, 12 min", "Measurement lab, 25 min", "Dice activity, 10 min + "
                                                                 "worksheet, 20 min"],
    ["FOREMAN's error", "None. It is right, and cannot say why",
     "Averages a failing gauge away; six decimal places",
     "Fabricates §4.7; turns a shall into a should"],
    ["Students hand in", "Note v1", "Note v1, then HW1 assigned", "Note v1, then HW2 assigned"],
], widths=[1.15, 1.95, 1.95, 1.85], size=8.5)

callout(d, "The one instruction that matters",
        "In all three meetings, the answer arrives after the students look, not before. Every "
        "planted error in this pack is findable from material they hold. If you name the error "
        "first, the meeting becomes a lecture about a thing that already happened.")

# ---------------------------------------------------------------------------
h2(d, "Prep — do this once, before M01")
rows = [["#", "Task", "When"]]
for i, (t, w) in enumerate([
    ("Install the four brand fonts from the kit on the machine you will present from. Without "
     "them the decks fall back to Arial — readable, but the titles reflow.", "Once"),
    ("Decide the measurement instrument for M02. Calipers are best; rulers work and make the "
     "resolution point sharper. If neither, the backup CSV runs the whole lab.", "Before M02"),
    ("Confirm which AI assistant students may use live in class. M03 has a two-minute live "
     "prompt demo that can be cut if the answer is none.", "Before M03"),
    ("Decide whether to hand out the brand kit at M01 or M02. Recommendation: M01, so the note "
     "and HW1 come back on letterhead.", "Before M01"),
    ("Print the handouts listed below. Everything else can be projected.", "Each meeting"),
    ("Read the three answer keys. They carry the teaching moves, not just the answers.", "Once"),
], 1):
    rows.append([str(i), t, w])
table(d, rows, widths=[0.3, 5.1, 1.5], size=9)

h2(d, "What to print")
table(d, [
    ["Meeting", "Print one per student", "Print one per pair", "Project only"],
    ["M01", "H1-02 load rating sheet, H1-06 note template",
     "H1-03 FOREMAN assessment, H1-04 2019 history, H1-05 task sort",
     "H1-01 orientation memo"],
    ["M02", "H2-01 lab sheet, H2-05 decision log", "H2-02 install record, H2-03 FOREMAN check",
     "H2-04 HW1 (or print)"],
    ["M03", "H3-01 county spec, H3-04 worksheet", "H3-02 FOREMAN summary, H3-03 dice activity",
     "H3-05 HW2 (or print)"],
], widths=[0.8, 2.3, 2.2, 1.6], size=8.5)
para(d, "H3-01, the county specification, is the one thing that must be on paper. The whole "
        "exercise is students physically turning to Section 4 and finding it ends at 4.5.",
     size=9, italic=True, color=GREY, after=8)

d.add_page_break()

# ---------------------------------------------------------------------------
h1(d, "M01 — Tuesday, February 2. First day")
para(d, "Concepts 13–18: artificial intelligence, rule-based systems, machine learning, training "
        "data, learned patterns, rules versus learned patterns.", size=9, color=GREY, after=8)

table(d, [
    ["Min", "What happens", "Slides"],
    ["0–10", "Open in world. Students are new hires. Put FOREMAN's deck assessment on screen, "
             "then Diane's memo. Do not resolve the contradiction.", "1–6"],
    ["10–25", "Rules. Walk the load rating formula. Work G-3 together on the board, slowly, "
              "with a pencil. The point is not the arithmetic — it is that a stranger could "
              "redo it.", "7–9"],
    ["25–35", "Activity: students work G-4 on H1-02. Circulate. Answer: RF = "
              f"{F['RF']}, rating {F['rating_tons']} tons.", "10–11"],
    ["35–50", "Learned patterns. How the photo model works. Then put FOREMAN's six ratings next "
              "to Diane's 2019 ratings and let the class find D-15.", "12–14"],
    ["50–57", "The reveal: ask which panel FOREMAN was most confident about. Wait. It is D-15, "
              "at 96%. Sit in the silence before explaining the overlay.", "15–17"],
    ["57–69", "Activity: task sort, H1-05, in pairs. Debrief items 8 and 9 only.", "18–20"],
    ["69–75", "The note. Collect it. Mask off, two minutes. Assign nothing but reading.", "21–24"],
], widths=[0.75, 4.55, 0.85], size=9)

h2(d, "Three moves")
bullets(d, [
    ("Do not say “hallucination” today. ", "FOREMAN is not wrong at M01. It answers "
     "the question it was asked, correctly, and cannot say why. That distinction dies if "
     "students learn on day one that the AI is simply unreliable."),
    ("Let D-15 land before explaining it. ", "The instinct is to narrate. Ask the confidence "
     "question, take answers, and only then say the panel was overlaid in 2018."),
    ("Land task 9 and refuse to resolve it. ", "Most students call “look it up in the "
     "spec” a rule. It is — if you open the document. Say you will come back to it on "
     "Tuesday, and stop. M03 is the payoff and it is much better if they have been wondering."),
])

h2(d, "Expect to hear")
table(d, [
    ["A student says", "Useful reply"],
    ["“So the AI was wrong.”", "It was not. It rated the surface in the photograph. "
                                         "The surface was not the deck. Which of those is the "
                                         "model's fault?"],
    ["“Why not just use a better model?”", "What would a better model see in a "
                                                     "photograph of an overlay? This is a limit "
                                                     "of the input, not the algorithm."],
    ["“Is Diane just anti-AI?”", "She uses it. She signs her name to the output. "
                                           "Those are different positions."],
], widths=[2.4, 4.5], size=9)

d.add_page_break()

# ---------------------------------------------------------------------------
h1(d, "M02 — Thursday, February 4. Measure one thing, five times")
para(d, "Concepts 19–24: measurement and why it matters, repeated measurements, range of "
        "readings, systematic error and accuracy, uncertainty propagation, instrument "
        "resolution.", size=9, color=GREY, after=8)

table(d, [
    ["Min", "What happens", "Slides"],
    ["0–10", "FOREMAN's PASS on screen. Ask: do we accept the array? Take a show of hands. "
             "Then say you are not opening the file for forty minutes.", "1–3"],
    ["10–22", "Teach measurement: reading, spread, resolution, true value. Then accuracy vs "
              "precision on the target diagram, and random vs systematic error.", "4–7"],
    ["22–47", "The lab, H2-01. Parts A, B and C. Part B is the one that matters — make sure "
              "pairs actually swap pins.", "8–10"],
    ["47–55", "Debrief the lab. Get the sentence out of the room: averaging fixes random error "
              "and hides systematic error.", "10"],
    ["55–68", "Open gauges_install.csv together. Per gauge, not in aggregate. Let G6 emerge. "
              "Then show how FOREMAN's number was built.", "11–15"],
    ["68–73", "Wes's margin note on the install record. Then the hours.", "16–18"],
    ["73–75", "Mask off. Assign HW1 and the decision log.", "19–20"],
], widths=[0.75, 4.55, 0.85], size=9)

h2(d, "The numbers you will need at the board")
table(d, [
    ["Quantity", "Value"],
    ["G6 mean", f"{G['gauges']['G6']['mean']:.2f} µε"],
    ["Specification limit", "±25 µε (KC-MB-12 §4.3)"],
    ["G6 exceeds the limit by", "162.5 µε — seven and a half times the limit"],
    ["The other seven gauge means", "all within about 1 µε of zero; they sum to −3.00 µε"],
    ["Sum of all eight means", "184.50 µε"],
    ["FOREMAN's array figure", f"184.50 ÷ 8 = {G['array_mean']:.4f} µε, which passes ±25"],
    ["Backup pin data, reader A vs B", f"{P['mean_A']:.3f} vs {P['mean_B']:.3f} mm — "
                                       f"{1000*(P['mean_B']-P['mean_A']):.0f} µm systematic"],
    ["Area propagation", f"{P['area_rel_pct']:.3f}% in area from "
                         f"{100*P['sd']/P['mean']:.3f}% in diameter — double, because d is squared"],
], widths=[2.6, 4.3], size=9)

callout(d, "Do not write G6 on the board early",
        "The whole meeting is built so that a student says “the average passed but a gauge "
        "failed” out loud. If nobody has by minute 62, ask: which gauge is the average "
        "hiding? Do not name it.")

h2(d, "Two things students get wrong here")
bullets(d, [
    ("They look for a software bug. ", "There is not one. FOREMAN's arithmetic is correct to "
     "every digit. The error is in what it chose to compute, not how. Say this explicitly — "
     "students arrive expecting AI mistakes to look like typos."),
    ("They think catching G6 was the assignment. ", "It was not. The assignment is choosing what "
     "to check with ten hours. A student who checked the wrong thing carefully and said so has "
     "done the job. Make that unambiguous at the mask-off."),
])

d.add_page_break()

# ---------------------------------------------------------------------------
h1(d, "M03 — Tuesday, February 9. The section that does not exist")
para(d, "Concepts 25–31: large language models and tokens, probability basics, next-token "
        "prediction, sampling and temperature, prompts, hallucination, checking output against "
        "source.", size=9, color=GREY, after=8)

table(d, [
    ["Min", "What happens", "Slides"],
    ["0–8", "FOREMAN's spec summary on screen. Read the §4.7 row aloud, in passing, with no "
            "emphasis. Move on. Nobody will object.", "1–3"],
    ["8–20", "Probability in fifteen minutes: probability, fair die, weighted die, likely is "
             "not certain. Keep it concrete.", "4–6"],
    ["20–30", "The dice activity, H3-03. Both rounds plus the comparison.", "7–9"],
    ["30–45", "Tokens, next-token prediction, temperature, prompts — each tied back to a column "
              "of the table they just used.", "10"],
    ["45–65", "Worksheet H3-04 in pairs, with the specification on paper. Circulate. Do not "
              "confirm §4.7 either way until a pair states it.", "11–12"],
    ["65–72", "Land it: §4.7 does not exist, and §3.2 changed one word. Then name hallucination.",
     "13–18"],
    ["72–75", "How you catch it. Mask off. Assign HW2.", "19–21"],
], widths=[0.75, 4.55, 0.85], size=9)

h2(d, "The two planted errors")
table(d, [
    ["Where", "What FOREMAN did", "Why this one"],
    ["§4.7", "Cites a section that does not exist, and uses it to license automated assessment "
             "above 90% confidence — which is exactly what its own M01 deck assessment claimed.",
     "The fabrication is self-serving. Ask the class who benefits from §4.7 being real."],
    ["§3.2", "“Shall review and seal” became “should be reviewed.” The seal "
             "and the responsible-charge sentence vanish entirely.",
     "One word moves work from mandatory to optional. This returns at M26, licensure."],
], widths=[0.9, 3.4, 2.6], size=8.5)
para(d, "Eight of the ten claims are accurate. That is deliberate — a summary wrong throughout "
        "would be easy to catch and would teach the wrong lesson. Students must read all ten.",
     size=9.5, after=8)

h2(d, "The third catch, if the class is moving fast")
para(d, "FOREMAN omits §2.4 entirely — special inspection within 30 days after an impact, flood, "
        "overload or machinery failure. Nothing it wrote about §2.4 is false; §2.4 simply is not "
        "there. Ask whether an omission can mislead. It can, because the summary claims to cover "
        "what the specification requires. This matters at M14, where the overweight permit is "
        "precisely the trigger §2.4 describes.", after=8)

h2(d, "Say the word last")
para(d, "Students will call §4.7 “made up”, “invented”, or say “it "
        "lied.” Take all three, then give them the term. Correct “lied” gently: "
        "lying requires knowing the truth and choosing otherwise, and nothing in the dice table "
        "knows anything. That is why the dice come before the worksheet, and why naming "
        "hallucination before they have caught one wastes the only chance to do it in the right "
        "order.", after=10)

d.add_page_break()

# ---------------------------------------------------------------------------
h1(d, "Continuity — what comes back")
para(d, "Nothing in these three meetings is self-contained. Note who does what, because the "
        "callbacks are the reason the simulation exists.", after=8)
table(d, [
    ["Planted here", "Returns at", "As"],
    ["G6's offset, accepted or caught in HW1 (M02)", "M19, M25",
     "An input to a four-step workflow that produces an unexplainable number, traceable to a "
     "February file with the student's name on it"],
    ["The gauge spreadsheet handed to Wes (M06)", "M25",
     "Part of the package the student must independently verify"],
    ["Task 9, unresolved (M01)", "M03", "Resolved — and it is the whole meeting"],
    ["§3.2, shall vs should (M03)", "M26", "Licensure, the PE stamp, responsible charge"],
    ["§2.4, the omitted clause (M03)", "M14", "The overweight permit is a §2.4 trigger"],
    ["D-15's overlay (M01)", "M07", "Out-of-domain use — the model was trained on girder bridges"],
], widths=[2.3, 1.1, 3.5], size=8.5)

h2(d, "Grading these three meetings")
bullets(d, [
    ("The note is graded on the check, never the outcome. ", "A student whose number was wrong "
     "but whose check was real and honestly described meets the bar. The rubric is on H1-06."),
    ("Hours are never points. ", "The decision log is evidence of judgement. It is not scored."),
    ("Diane is not the grader. ", "Say this at every mask-off. If her approval reads as the "
     "right answer, students optimise for pleasing her and the simulation collapses."),
])

h2(d, "What still needs review before this runs")
for t in [
    "The simplified load rating formula and the G-3 / G-4 numbers — a licensed engineer should "
    "confirm these are a fair teaching simplification and not misleading.",
    "Working values in the data: strain magnitudes, the ±25 µε acceptance limit, a 1 µε gauge "
    "resolution, and whether a 187 µε install offset is plausible.",
    "KC-MB-12 is invented. If the department can license a real standard, the two planted errors "
    "port to any document with numbered sections and a “shall.”",
    "The 9-point condition rating scale is used in an NBI-like way. Confirm the usage is fair.",
    "Whether a redundant midspan gauge (G5 / G6) is a realistic array design.",
]:
    p = doc_p = para(d, "", after=5)
    run(p, "☐   ", 11, color=GIRDER)
    run(p, t, 9.5)

para(d, "", after=8)
callout(d, "Source note",
        "ACMEJOB.Ai, FOREMAN, Diane Halvorsen, Wes Tanaka, the Otter Bend Lift Bridge and "
        "Kinnick County are invented for this course. Failure modes are drawn from the public "
        "engineering literature. No real collapse or casualty event is referenced or dramatised.",
        fill="F4F6F8", edge="C9CFD6")

save(d, os.path.join(OUT, "INSTRUCTOR-GUIDE-M01-M03.docx"))

# ------------------------------------------------------------- file index --
d = course_doc("M01 – M03", "What is in this pack", kind="FILE INDEX")
para(d, "Twenty-eight files. Folders are in teaching order.", size=9.5, color=GREY, after=10)
for folder, rows in [
    ("00-INSTRUCTOR", [
        ("INSTRUCTOR-GUIDE-M01-M03.docx", "Run of show, prep, continuity, review checklist"),
        ("FILE-INDEX.docx", "This page")]),
    ("01-BRAND-KIT", [
        ("ACMEJOB-brand-kit.zip", "Hand this to students. Fonts, logos, templates, brand guide"),
        ("(unzipped copy)", "Same contents, for you to look through")]),
    ("02-M01-first-day", [
        ("M01-slides-first-day.pptx", "24 slides"),
        ("H1-01-orientation-memo-halvorsen.docx", "Diane's memo — project or read aloud"),
        ("H1-02-load-rating-sheet.docx", "The rule. Worked G-3, blank G-4"),
        ("H1-03-foreman-deck-assessment.docx", "FOREMAN's six panel ratings"),
        ("H1-04-deck-panel-history-2019.docx", "Diane's 2019 field ratings, same panels"),
        ("H1-05-task-sort-activity.docx", "Nine tasks to sort"),
        ("H1-06-note-v1-template-rubric.docx", "The note, and how it is graded"),
        ("KEY-M01-answer-key.docx", "Answers and teaching notes")]),
    ("03-M02-measurement", [
        ("M02-slides-measurement.pptx", "20 slides"),
        ("H2-01-measurement-lab.docx", "The lab, with ruler and no-instrument fallbacks"),
        ("H2-02-sensor-installation-record.docx", "The install record, with Wes's margin note"),
        ("H2-03-foreman-baseline-check.docx", "FOREMAN's PASS"),
        ("H2-04-HW1-gauge-baseline.docx", "HW1 and the ten-hour budget"),
        ("H2-05-hours-and-decision-log.docx", "One page, kept all semester"),
        ("gauges_install.csv", "8 gauges × 12 readings. The keystone data file"),
        ("pin_measurements_backup.csv", "24 pin readings, two people — lab fallback"),
        ("KEY-M02-answer-key.docx", "Gauge statistics, the planted errors, timing")]),
    ("04-M03-hallucination", [
        ("M03-slides-hallucination.pptx", "21 slides"),
        ("H3-01-KC-MB-12-county-spec.docx", "The invented county spec. Print this one"),
        ("H3-02-foreman-spec-summary.docx", "Ten claims, two of them wrong"),
        ("H3-03-next-word-dice-activity.docx", "The dice table"),
        ("H3-04-source-check-worksheet.docx", "Check the ten claims"),
        ("H3-05-HW2-spec-summary-check.docx", "HW2"),
        ("KEY-M03-answer-key.docx", "Claim-by-claim verdicts, teaching notes")]),
    ("05-CHARTS", [("*.png", "Every chart used in the decks, if you want them elsewhere")]),
]:
    h2(d, folder)
    table(d, [["File", "What it is"]] + [[a, b] for a, b in rows],
          widths=[3.2, 3.7], size=8.5)
save(d, os.path.join(OUT, "FILE-INDEX.docx"))
