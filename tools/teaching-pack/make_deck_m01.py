"""M01 deck — First day. Rules versus learned patterns."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

FACTS = json.load(open(os.path.join(ROOT, "build", "facts.json")))
F = FACTS["m01"]
P = FACTS["m01_panels"]
prs = deck()

# 1 -------------------------------------------------------------------------
title_slide(prs, "Meeting 01  ·  Unit 1: Hired",
            "Your first day at\nACMEJOB.Ai",
            "What is AI, and what is the difference between a rule and a learned pattern",
            "Tuesday, February 2, 2027  ·  SEIS 201")

# 2 -------------------------------------------------------------------------
s, y = content(prs, "You were hired this morning",
               "ACMEJOB.Ai — a 60-year-old Minnesota civil and mechanical firm that added two "
               "letters to its name two years ago")
speaker_card(s, 0.72, y + 0.1, 3.75, 3.5, "DIANE HALVORSEN, PE",
             ["Principal engineer, 27 years.",
              "Knows every inspector and contractor in the county.",
              "Does not trust FOREMAN.",
              "Asks one question, every time."])
speaker_card(s, 4.78, y + 0.1, 3.75, 3.5, "WES TANAKA, EIT",
             ["Second year out of school.",
              "Split across three projects.",
              "Genuinely trying.",
              "His handoffs arrive late and incomplete."])
speaker_card(s, 8.84, y + 0.1, 3.75, 3.5, "FOREMAN v4.2",
             ["The firm's AI platform.",
              "Fast, fluent, confident.",
              "Reads more than any of you can.",
              "Wrong about one time in five, at full confidence."],
             machine=True)
text(s, 0.72, y + 3.85, 11.9, 0.6,
     [[("The colour code holds all semester: ", {"bold": True}),
       ("orange is the machine, blue is a person. When you cannot remember who said "
        "something, look at the colour.", {})]],
     size=16, color=GREY, line=1.2)

# 3 -------------------------------------------------------------------------
s, y = content(prs, "The job", "Kinnick County wants an answer by May")
card(s, 0.72, y + 0.1, 5.9, 3.9, "THE OTTER BEND LIFT BRIDGE",
     ["County Road 9 over the Kinnick River.",
      "Built 1962. Vertical lift span.",
      "Carrying loads nobody designed it for.",
      "Strain, temperature and vibration sensors were installed last month.",
      "",
      "The question: rehabilitate, or replace?"],
     tint=PAPER, edge=CONCRETE, body_size=17)
card(s, 6.92, y + 0.1, 5.67, 3.9, "WHAT THAT MEANS FOR YOU",
     ["Every lab, every dataset and both exams this semester come from this one bridge.",
      "",
      "Work you do in February comes back in April with your name on it.",
      "",
      "In May, somebody stamps a recommendation. That is what all of this is for."],
     tint=RGBColor(0xEE, 0xF3, 0xF8), edge=GIRDER_LT, body_size=17,
     label_color=GIRDER)

# 4 -------------------------------------------------------------------------
statement(prs, "Two things happened before\nnine o'clock this morning.",
          "And they do not agree with each other.")

# 5 -------------------------------------------------------------------------
s, y = content(prs, "Exhibit A — FOREMAN's demo, 07:41")
speaker_card(s, 0.72, y + 0.15, 11.87, 2.35, "FOREMAN v4.2 — DECK CONDITION ASSESSMENT",
             ["“Deck is in fair to good condition overall. Mean panel rating 6.8. No panel "
              "rated below 6. No immediate action required. Model confidence is high across all "
              "panels (mean 92.0%).”",
              "Six panels rated from photographs. Elapsed time: 1.9 seconds."],
             machine=True, body_size=18)
text(s, 0.72, y + 2.8, 11.9, 0.9,
     [[("It read six photographs and produced six numbers, faster than you can open the file. "
        "Ask yourself now, before we go further: ", {}),
       ("what would it take to check this?", {"bold": True, "color": GIRDER})]],
     size=19, color=REBAR, line=1.2)

# 6 -------------------------------------------------------------------------
s, y = content(prs, "Exhibit B — Diane's orientation memo, 08:30")
speaker_card(s, 0.72, y + 0.15, 11.87, 1.95, "DIANE HALVORSEN, PE",
             ["“Every number you hand me comes with one sentence: how do you know that "
              "is right?”"], body_size=22)
text(s, 0.72, y + 2.35, 11.9, 1.4,
     [[("She is not asking you to prove the number from first principles. She is asking you to "
        "know ", {}), ("which check you did", {"bold": True}),
       (" — so that when the county asks her, the answer is not “the computer said so.”",
        {})]],
     size=19, color=REBAR, line=1.25)
card(s, 0.72, y + 3.5, 11.87, 1.75,
     "TODAY'S ARGUMENT, IN ONE LINE",
     ["FOREMAN produced an answer nobody can check. Diane's method produces an answer anybody "
      "can check. Both are legitimate engineering. Knowing which one you are holding is the job."],
     tint=CREAM, edge=GOLD, body_size=17, label_color=REBAR)

# 7 -------------------------------------------------------------------------
section(prs, "1", "Rules", "Steps somebody wrote down, that anybody can repeat")

# 8 -------------------------------------------------------------------------
s, y = content(prs, "A rule: the load rating check",
               "Diane's standard sheet LR-1. This is arithmetic — you do not need to have taken "
               "structures.")
rect(s, 0.72, y + 0.15, 11.87, 1.25, fill=PAPER, line=CONCRETE, radius=0.06)
text(s, 0.72, y + 0.42, 11.87, 0.8, "RF  =  ( C − D )  ÷  ( L × IM )", size=40,
     color=GIRDER, font="Courier New", bold=True, align=PP_ALIGN.CENTER)
items = [
    ("C  ", "girder moment capacity — what the steel can carry"),
    ("D  ", "dead load moment — the weight of the structure itself"),
    ("L  ", "live load moment — the rating truck, an HS-20 at 36 tons"),
    ("IM  ", "impact factor — allowance for a moving load bouncing. 1.33."),
]
bullet_list(s, 0.95, y + 1.75, 11.4, 2.0, items, size=18, dot=GIRDER_LT)
text(s, 0.95, y + 3.7, 11.4, 0.5,
     [[("Above RF = 1.00 the girder carries the truck. Below it, you post or restrict the bridge.",
        {"bold": True})]], size=18, color=REBAR)

# 9 -------------------------------------------------------------------------
s, yend = table_slide(prs, "Worked: Girder G-3, south approach",
                      [["Step", "Substitution", "Result"],
                       ["1.  Capacity minus dead load", "3,920 − 1,455", "2,465 kip-ft"],
                       ["2.  Live load with impact", "1,080 × 1.33", "1,436.4 kip-ft"],
                       ["3.  Rating factor", "2,465 ÷ 1,436.4", "1.716"],
                       ["4.  Rating in tons", "1.716 × 36", "61.8 tons"]],
                      widths=[4.3, 3.6, 3.4], size=17, col_align=["l", "l", "r"],
                      kicker="Follow it with a pencil. Every line is checkable by somebody who "
                             "was not in the room.")
text(s, 0.72, yend + 0.5, 11.9, 0.9,
     [[("That is the entire point of a rule. ", {"bold": True, "color": GIRDER}),
       ("Nobody has to trust Diane. They can redo it.", {})]], size=20, color=REBAR)

# 10 ------------------------------------------------------------------------
activity(prs, "Work the rating factor for Girder G-4", 10, [
    "G-4 sits under the wheel line. Its bottom flange has 60 years of section loss, so its "
    "capacity is lower: C = 3,850 kip-ft. D and L are unchanged.",
    "Work the four steps on handout H1-02. Show every substitution.",
    "Is your RF above or below 1.00? Say what that means for a 36-ton truck.",
    "Write one sentence: how do you know your answer is right?",
], note="If you finish early: what happens to the rating if the section loss is worse than "
        "assumed and C drops to 3,500?")

# 11 ------------------------------------------------------------------------
s = image_slide(prs, "The answer", "m01-rating-factor.png",
                kicker=f"RF = {F['RF']}, which is a rating of {F['rating_tons']} tons",
                caption="G-4 carries the rating truck, with less margin than G-3. Both girders "
                        "pass. Nothing here required judgement — and that is exactly what makes "
                        "it a rule.")

# 12 ------------------------------------------------------------------------
section(prs, "2", "Learned patterns",
        "Nobody wrote the steps down. A machine was shown examples until it picked up the pattern.")

# 13 ------------------------------------------------------------------------
s, y = content(prs, "How FOREMAN rated the deck",
               "There is no formula in here anywhere")
steps = [("Training  ", "41,800 photographs of bridge decks, each labelled by an inspector"),
         ("Learning  ", "the model adjusts itself until its ratings match the labels"),
         ("Use  ", "show it a new photograph, it returns the rating that best matches the "
                    "pattern it picked up"),
         ("Confidence  ", "the model's own estimate of how well it did, produced by the model itself")]
bullet_list(s, 0.95, y + 0.25, 11.4, 2.6, steps, size=18, dot=STICKER)
card(s, 0.72, y + 2.95, 11.87, 2.05, "WHY THIS IS NOT A BAD THING",
     ["Nobody can write the rule for what spalling looks like in a photograph. If you want that "
      "job done at all, it has to be learned. The question is never whether to use it — it is "
      "what you would accept as evidence that it worked."],
     tint=PAPER, edge=CONCRETE, body_size=17, label_color=GIRDER)

# 14 ------------------------------------------------------------------------
image_slide(prs, "Same six panels. Two sources.", "m01-deck-ratings.png",
            kicker="FOREMAN's 2027 photo ratings against Diane's 2019 field ratings",
            caption="Five panels agree within a point. One is three points apart.")

# 15 ------------------------------------------------------------------------
statement(prs, "Which panel was FOREMAN\nmost confident about?", dark=False, size=48)

# 16 ------------------------------------------------------------------------
image_slide(prs, "D-15. At 96 percent.", "m01-confidence-vs-error.png",
            caption="The panel was overlaid with new surfacing in 2018. The photograph shows a "
                    "smooth, clean overlay — so the model was surer, not less sure. Confidence "
                    "went up precisely because the evidence got worse.")

# 17 ------------------------------------------------------------------------
s, y = content(prs, "Nobody here is wrong",
               "This is the distinction the whole semester rests on")
speaker_card(s, 0.72, y + 0.2, 5.9, 3.78, "WHAT FOREMAN DID",
             ["Answered the question it was asked: what condition does this surface appear to "
              "be in?",
              "",
              "Its answer was reasonable for that question.",
              "",
              "It had no way to know the surface was not the deck."], machine=True, body_size=17)
speaker_card(s, 6.72, y + 0.2, 5.87, 3.78, "WHAT DIANE HAD",
             ["She could tap the deck with a hammer and listen.",
              "",
              "She remembered the 2018 overlay because she was there.",
              "",
              "None of that is in a photograph, and no amount of training data puts it there."],
             body_size=17)
text(s, 0.72, y + 4.18, 11.9, 0.7,
     [[("The failure was in the question, not the algorithm. ", {"bold": True, "color": GIRDER}),
       ("Remember that when somebody tells you a better model would have caught it.", {})]],
     size=18, color=REBAR, line=1.2)

# 18 ------------------------------------------------------------------------
s, yend = table_slide(prs, "Rules and learned patterns, side by side",
                      [["", "A rule", "A learned pattern"],
                       ["Built from", "Steps somebody wrote down", "Examples somebody labelled"],
                       ["Shows its work", "Every line", "No line"],
                       ["You check it by", "Redoing the steps", "Testing it on cases it never saw"],
                       ["Fails by", "Being wrong the same way every time",
                        "Being wrong on things unlike its training"],
                       ["Tells you it failed", "It does not, but you can see where",
                        "It does not, and it sounds the same either way"]],
                      widths=[2.5, 4.4, 5.0], size=15, col_align=["l", "l", "l"])
text(s, 0.72, yend + 0.45, 11.9, 0.7,
     "Most real work is a mix. The skill is knowing which part you are holding at any moment.",
     size=19, color=REBAR)

# 19 ------------------------------------------------------------------------
activity(prs, "Task sort — rule, learned, or both?", 12, [
    "Handout H1-05 lists nine things this firm does on the Otter Bend job.",
    "For each: how would you build it — a rule, a learned pattern, or either?",
    "Then the harder column: what single piece of evidence would convince you it works?",
    "Two of the nine are genuinely arguable. Be ready to say which two.",
], note="Work in pairs. Disagreement is the point — if your pair agrees on all nine, you are "
        "not arguing hard enough about number 9.")

# 20 ------------------------------------------------------------------------
s, yend = table_slide(prs, "Where that lands",
                      [["#", "Task", "Answer"],
                       ["1", "Rating factor for a girder", "Rule"],
                       ["2", "Find spalling in 400 photographs", "Learned"],
                       ["3", "Counterweight balance check", "Rule"],
                       ["4", "Draft the county cover letter", "Learned"],
                       ["5", "Flag any strain reading above 250 µε", "Rule"],
                       ["6", "Predict which panels need repair in 5 years", "Learned"],
                       ["7", "Convert 42 ft 7 in to metres", "Rule"],
                       ["8", "Fatigue crack or shrinkage crack?", "Both — argue it"],
                       ["9", "Look up an interval in the county spec", "Both — argue it"]],
                      widths=[0.7, 7.4, 3.3], size=14.5, col_align=["c", "l", "l"],
                      row_colors={8: CREAM, 9: CREAM})

# 21 ------------------------------------------------------------------------
statement(prs, "Number 9 is a rule —\nif you open the document.",
          "Next Tuesday we find out what happens when you ask a language model instead. "
          "Do not look it up before then.")

# 22 ------------------------------------------------------------------------
s, y = content(prs, "The note", "One sentence. It is due before you leave.")
rect(s, 0.72, y + 0.2, 11.87, 1.3, fill=CREAM, line=GOLD, radius=0.05)
text(s, 1.1, y + 0.52, 11.1, 0.8,
     [[("I believe ", {}), ("[the number or claim]", {"bold": True, "color": STICKER}),
       (" is right because I checked it against ", {}),
       ("[the thing you checked it against]", {"bold": True, "color": STICKER}), (".", {})]],
     size=26, color=REBAR, font=DISPLAY)
card(s, 0.72, y + 1.75, 5.9, 2.55, "STRONG",
     ["“I believe the rating factor of 1.69 is right because I worked the arithmetic twice "
      "and the second pass matched.”",
      "Names the claim. Names a check somebody else could repeat."],
     tint=RGBColor(0xE9, 0xF4, 0xEC), edge=RGBColor(0x2E, 0x7D, 0x4F),
     label_color=RGBColor(0x2E, 0x7D, 0x4F), body_size=16)
card(s, 6.72, y + 1.75, 5.87, 2.55, "NOT YET",
     ["“I believe the deck is in fair condition because FOREMAN rated it 6.8 with 92% "
      "confidence.”",
      "Confidence is not a check. Nothing was compared to anything."],
     tint=RGBColor(0xFA, 0xEA, 0xEC), edge=CRIT, label_color=CRIT, body_size=16)

# 23 ------------------------------------------------------------------------
s = blank(prs); bg(s, prs, WHITE)
head(s, "Mask off — two minutes", "The part where I stop being the firm and go back to being "
                                  "your instructor")
bullet_list(s, 0.95, 2.1, 11.4, 3.2, [
    ("Diane is a character. ", "She is not the grader and her reaction is never your grade. "
                               "Some weeks she will be in a hurry and wave through work that "
                               "deserved better."),
    ("The rubric is the grade. ", "It scores the claim you named and the check you did — never "
                                  "whether the number turned out right."),
    ("You are allowed to disagree with her. ", "Doing it with evidence is the assignment."),
], size=18, dot=GIRDER_LT)

# 24 ------------------------------------------------------------------------
closer(prs, [
    ("Read", "The orientation memo and the deck panel history, if you have not already"),
    ("Thursday", "Bring a ruler or calipers if you own them. We measure something physical "
                 "before anyone touches sensor data"),
    ("Coming", "HW1 is handed out Thursday. It is about eight strain gauges and whether you "
               "believe them"),
], title="Before Thursday")

save(prs, os.path.join(ROOT, "build", "M01", "M01-slides-first-day.pptx"))
