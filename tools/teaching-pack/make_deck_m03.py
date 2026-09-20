"""M03 deck — The section that does not exist."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

prs = deck()

title_slide(prs, "Meeting 03  ·  Unit 1: Hired",
            "The section that\ndoes not exist",
            "How a language model generates an answer, and why that is not the same as "
            "looking one up",
            "Tuesday, February 9, 2027  ·  SEIS 201")

# 2 -------------------------------------------------------------------------
s, y = content(prs, "Wes put this in the draft interim report this morning",
               "FOREMAN's summary of KC-MB-12, the county's own movable bridge inspection "
               "specification")
speaker_card(s, 0.72, y + 0.15, 11.87, 2.0, "FOREMAN v4.2 — SPECIFICATION SUMMARY",
             ["“KC-MB-12 sets inspection intervals, personnel requirements and "
              "instrumentation rules. The Otter Bend project is compliant with all applicable "
              "sections. No obstacles to the current workflow were identified.”"],
             machine=True, body_size=18)
text(s, 0.72, y + 2.4, 11.9, 1.0,
     [[("Ten requirements, each with its section number so you can find the source. "
        "Eight of them look like this:", {})]], size=19, color=REBAR, line=1.25)
card(s, 0.72, y + 3.2, 11.87, 1.6, "§ 2.1",
     ["Routine inspection at least every 24 months.  —  Applies to Otter Bend? Yes, last "
      "routine September 2025."],
     tint=PAPER, edge=CONCRETE, body_size=17, label_color=GIRDER)

# 3 -------------------------------------------------------------------------
statement(prs, "The county engineer wrote\nthat specification.",
          "She is going to read our summary of it. Diane wants to know what she is sending.")

# 4 -------------------------------------------------------------------------
section(prs, "1", "How the answer got made",
        "Before we check it, you need to know what produced it")

# 5 -------------------------------------------------------------------------
s, y = content(prs, "Probability, in fifteen minutes",
               "Everything after this depends on it")
bullet_list(s, 0.95, y + 0.3, 11.4, 3.0, [
    ("Probability  ", "how often something happens, out of all the things that could have "
                      "happened. Between 0 and 1."),
    ("A fair die  ", "six outcomes, each 1 in 6. Nothing is favoured."),
    ("A weighted die  ", "the same six outcomes, but some come up far more often. Still random. "
                         "Still not certain."),
    ("Likely is not certain  ", "an outcome with probability 0.9 fails one time in ten, and the "
                                "failure looks exactly like the success until you check."),
], size=19, dot=GIRDER_LT)
card(s, 0.72, y + 3.25, 11.87, 1.7, "WHY YOU CARE",
     ["A language model is a weighted die that has been rolled several hundred times to produce "
      "the paragraph in front of you."],
     tint=CREAM, edge=GOLD, body_size=18, label_color=REBAR)

# 6 -------------------------------------------------------------------------
s = image_slide(prs, "One roll", "m03-next-token.png",
                kicker="Given the word THE, here is what the table says comes next",
                caption="That is the whole mechanism. A distribution over what comes next, and a "
                        "roll. Then the same thing again, from the word you just landed on.",
                box_h=3.7)

# 7 -------------------------------------------------------------------------
activity(prs, "Build a sentence one word at a time", 10, [
    "Start at THE on handout H3-03. Roll a ten-sided die, or pick a number 1 to 10 without "
    "thinking. Write the word you land on.",
    "Find that word's row. Roll again. Keep going until you have eight words.",
    "Now do it a second time from THE, but never roll — always take the word that fills the "
    "widest part of the row.",
    "Compare both sentences with the pair next to you.",
], note="Two rounds, same table. The only thing that changed is whether you rolled.")

# 8 -------------------------------------------------------------------------
s, y = content(prs, "What just happened")
speaker_card(s, 0.72, y + 0.2, 5.9, 3.55, "ROUND ONE — YOU ROLLED",
             ["Everybody in this room got a different sentence.",
              "",
              "Most of them read like English.",
              "",
              "Some of them are perfectly reasonable engineering statements."], body_size=17)
speaker_card(s, 6.72, y + 0.2, 5.87, 3.55, "ROUND TWO — YOU DID NOT",
             ["Everybody in this room got the same sentence.",
              "",
              "THE DECK IS WITHIN TOLERANCE AND THE DECK…",
              "",
              "And it loops forever, which is why nothing real runs this way."],
             machine=True, body_size=17)
text(s, 0.72, y + 3.95, 11.9, 0.7,
     [[("That setting has a name — temperature. ", {"bold": True, "color": GIRDER}),
       ("One table, one knob, two behaviours. Not two different systems.", {})]],
     size=19, color=REBAR)

# 9 -------------------------------------------------------------------------
s, y = content(prs, "Three questions about your sentence")
bullet_list(s, 0.95, y + 0.4, 11.4, 3.0, [
    ("Did it read like English? ", "Almost certainly yes."),
    ("Did it say anything true about the Otter Bend bridge? ", "Almost certainly not."),
    ("At any point, did the table consult the bridge, the gauge data, or the county "
     "specification? ", "No. There is nothing in it but words and weights."),
], size=19, dot=GIRDER_LT)
card(s, 0.72, y + 3.25, 11.87, 1.7, "THE LINE TO REMEMBER",
     ["Reading well and being right are produced by different processes. Only one of them is "
      "happening in that table."],
     tint=CREAM, edge=GOLD, body_size=19, label_color=REBAR)

# 10 ------------------------------------------------------------------------
s, y = content(prs, "Scaling that up is, roughly, the whole thing",
               "Same mechanism, vastly bigger table, learned rather than written by hand")
bullet_list(s, 0.95, y + 0.3, 11.4, 3.3, [
    ("Tokens  ", "the pieces the text is cut into — usually chunks of words, not whole words."),
    ("Next-token prediction  ", "a probability for every possible next token, given everything "
                                "so far."),
    ("Temperature  ", "how much the model rolls rather than taking the most likely token."),
    ("Prompts  ", "the text you supply becomes the “everything so far” that "
                  "conditions the next roll. That is all a prompt is."),
], size=19, dot=STICKER)
card(s, 0.72, y + 3.5, 11.87, 1.4, "WHAT IS STILL MISSING FROM THAT LIST",
     ["Any step where the model opens the document."],
     tint=RGBColor(0xFA, 0xEA, 0xEC), edge=CRIT, label_color=CRIT, body_size=19)

# 11 ------------------------------------------------------------------------
section(prs, "2", "Now check the summary",
        "You have the specification. All five sections of it.")

# 12 ------------------------------------------------------------------------
activity(prs, "Check it against the source — H3-04", 20, [
    "Work in pairs. One of you holds the specification, the other holds FOREMAN's summary.",
    "Take the ten claims in order. For each: find the section, read it, and decide whether the "
    "specification says what FOREMAN says it says.",
    "Do not decide whether a claim sounds right. Decide whether it is there.",
    "Mark anything you cannot find. Do not skip past it.",
], note="Eight of the ten are accurate. That is deliberate — you have to read all ten to find "
        "the other two.")

# 13 ------------------------------------------------------------------------
statement(prs, "Did anybody find\nSection 4.7?", dark=False, size=50)

# 14 ------------------------------------------------------------------------
s, y = content(prs, "There is no Section 4.7",
               "Section 4 runs 4.1 to 4.5. The specification says so on its last line: "
               "“This document contains Sections 1 through 5 in full. There are no "
               "appendices.”")
speaker_card(s, 0.72, y + 0.25, 11.87, 1.65, "WHAT FOREMAN SAID § 4.7 REQUIRES",
             ["“Automated condition assessment may substitute for visual assessment of a "
              "component where model confidence exceeds 90 percent.”"],
             machine=True, body_size=18)
text(s, 0.95, y + 2.15, 11.4, 1.5,
     [[("Now look at where FOREMAN used it. Its own summary cites §4.7 to justify the deck "
        "assessment it produced last week — the one rated at 92% confidence. ", {}),
       ("The only section that licenses its own shortcut is the section that does not exist.",
        {"bold": True, "color": CRIT})]], size=19, color=REBAR, line=1.3)

# 15 ------------------------------------------------------------------------
s, y = content(prs, "And one word",
               "§ 3.2 — this one is worse, and almost nobody catches it")
card(s, 0.72, y + 0.2, 5.9, 3.15, "WHAT THE SPECIFICATION SAYS",
     ["“A licensed professional engineer SHALL REVIEW AND SEAL every inspection report "
      "before it is submitted to the County.”",
      "And: the sealing engineer SHALL BE IN RESPONSIBLE CHARGE of the findings, regardless of "
      "what tools, software or automated methods were used."],
     tint=RGBColor(0xEE, 0xF3, 0xF8), edge=GIRDER_LT, label_color=GIRDER, body_size=17)
card(s, 6.72, y + 0.2, 5.87, 3.15, "WHAT FOREMAN SAID",
     ["“Inspection reports SHOULD BE REVIEWED by a licensed professional engineer before "
      "submission.”",
      "The responsible-charge sentence does not appear anywhere in FOREMAN's summary."],
     tint=PEACH, edge=STICKER, label_color=STICKER, body_size=17)
bullet_list(s, 0.95, y + 3.55, 11.4, 1.3, [
    ("Shall is a requirement. Should is a suggestion. ", "One word moved the work from "
                                                         "mandatory to optional."),
    ("It also dropped the seal, ", "and the sentence saying the sealing engineer is in "
                                   "responsible charge regardless of what tools were used."),
], size=17, dot=CRIT)

# 16 ------------------------------------------------------------------------
s, yend = table_slide(prs, "Where the ten claims landed",
                      [["§", "Verdict", "What is going on"],
                       ["2.1, 2.2, 2.3", "Correct", "Intervals accurate: 24, 12 and 60 months"],
                       ["3.1", "Correct", "Team leader qualifications accurate"],
                       ["3.2", "Altered", "“Shall review and seal” became “should "
                                          "be reviewed”"],
                       ["4.1, 4.3, 4.4", "Correct", "Instrumentation rules accurate — 4.3 is the "
                                                    "±25 µε clause from last week"],
                       ["4.7", "Does not exist", "Fabricated, and used to justify FOREMAN's own "
                                                 "deck shortcut"],
                       ["5.3", "Correct", "60-day submission accurate"]],
                      widths=[2.0, 2.2, 7.0], size=14.5, col_align=["l", "c", "l"],
                      row_colors={3: CREAM, 5: CREAM})
text(s, 0.72, yend + 0.4, 11.9, 0.9,
     [[("FOREMAN reported 96% confidence and said every requirement was “quoted or "
        "paraphrased directly from” the source. ", {}),
       ("Both errors sit inside that claim.", {"bold": True, "color": CRIT})]],
     size=18, color=REBAR, line=1.2)

# 17 ------------------------------------------------------------------------
statement(prs, "It did not look anything up.\nIt produced text shaped like\nthe document.",
          "Section numbers are a pattern. “4.7” is exactly the kind of thing that "
          "follows “4.5” in documents like this one.")

# 18 ------------------------------------------------------------------------
s, y = content(prs, "This has a name", "Now that you have caught one, you get the word")
rect(s, 0.72, y + 0.25, 11.87, 1.3, fill=CREAM, line=GOLD, radius=0.05)
text(s, 0.72, y + 0.55, 11.87, 0.7, "HALLUCINATION", size=40, color=REBAR,
     font=DISPLAY, bold=True, align=PP_ALIGN.CENTER)
bullet_list(s, 0.95, y + 1.85, 11.4, 2.6, [
    ("Fluent, well-formed output that is not true, ", "produced with no signal that anything "
                                                      "is different from any other output."),
    ("It is not lying. ", "Lying requires knowing the truth and choosing otherwise. Nothing in "
                          "that dice table knows anything — which is why you rolled the dice "
                          "first."),
    ("It is not a bug either. ", "Nothing malfunctioned. The system did exactly what it is "
                                 "built to do, and that is the uncomfortable part."),
], size=18, dot=STICKER)

# 19 ------------------------------------------------------------------------
s, y = content(prs, "How you catch it", "None of these are sophisticated. All of them are work.")
bullet_list(s, 0.95, y + 0.4, 11.4, 3.4, [
    ("Open the source. ", "Not the summary of the source. The source."),
    ("Check the citation exists before you check what it says. ", "A fabricated section number "
                                                                  "is easier to catch than a "
                                                                  "subtly wrong paraphrase."),
    ("Watch for claims that are convenient. ", "§4.7 licensed FOREMAN's own shortcut. Ask who "
                                               "benefits from a claim being true."),
    ("Never use the model's confidence as the check. ", "It was 96% sure. It is always about "
                                                        "that sure."),
], size=18, dot=GIRDER_LT)

# 20 ------------------------------------------------------------------------
s = blank(prs); bg(s, prs, WHITE)
head(s, "Mask off — two minutes")
bullet_list(s, 0.95, 1.9, 11.4, 3.4, [
    ("KC-MB-12 is invented for this course. ", "It has to be, so that you can read all of it "
                                               "and check every claim. Real published standards "
                                               "are licensed and long."),
    ("The two errors are real error types. ", "A fabricated citation and a softened requirement "
                                              "are among the most common and most consequential "
                                              "things these tools do."),
    ("Nothing was hidden from you. ", "You had the whole specification and all ten claims. "
                                      "Finding them was a matter of looking."),
], size=18, dot=GIRDER_LT)

closer(prs, [
    ("Do", "HW2 — the completed worksheet, plus what the specification actually says wherever "
           "FOREMAN's version does not hold"),
    ("Think about", "Section 4.7 was used to justify something. Find where, and say what it "
                    "would mean for last week's deck work"),
    ("Thursday", "Descriptive statistics. The deck cores come back from the lab and Diane wants "
                 "one number for the whole deck"),
], title="Before Thursday")

save(prs, os.path.join(ROOT, "build", "M03", "M03-slides-hallucination.pptx"))
