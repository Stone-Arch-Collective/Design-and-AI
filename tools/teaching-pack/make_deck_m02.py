"""M02 decks — spoiler-safe student projection and instructor reveal."""
import os, sys, json
from io import BytesIO
from pptx import Presentation
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidelib import *

FACTS = json.load(open(os.path.join(ROOT, "build", "facts.json")))
G = FACTS["m02"]
P = FACTS["m02_pin"]
GA = G["gauges"]
prs = deck()

title_slide(prs, "Meeting 02  ·  Unit 1: Hired",
            "Measure one thing,\nfive times",
            "Why measurement is uncertain, and what averaging can and cannot fix",
            "Thursday, February 4, 2027  ·  SEIS 201")

# 2 -------------------------------------------------------------------------
s, y = content(prs, "FOREMAN cleared the gauge array at 06:02 this morning")
speaker_card(s, 0.72, y + 0.15, 11.87, 2.05, "FOREMAN v4.2 — BASELINE ACCEPTANCE CHECK",
             [f"“PASS. Array baseline offset {G['array_mean']:.6f} µε against a "
              f"specification limit of ±25 µε. The array is within tolerance and cleared for "
              f"service. Confidence 97%.”"], machine=True, body_size=19)
text(s, 0.72, y + 2.45, 11.9, 1.3,
     [[("Northline invoices us the moment we accept the array, and the February load response "
        "study runs off these eight gauges. ", {}),
       ("Diane will not accept it until somebody has looked.", {"bold": True, "color": GIRDER})]],
     size=19, color=REBAR, line=1.25)
card(s, 0.72, y + 3.55, 11.87, 1.45, "THE QUESTION ON THE TABLE",
     ["Do we accept the array?"], tint=CREAM, edge=GOLD, body_size=22, label_color=REBAR)

# 3 -------------------------------------------------------------------------
statement(prs, "We are not going to open\nthat file for forty minutes.",
          "You cannot judge somebody else's measurements until you have watched your own "
          "disagree with each other.")

# 4 -------------------------------------------------------------------------
section(prs, "1", "What a measurement is",
        "Nobody measures anything once")

# 5 -------------------------------------------------------------------------
s, y = content(prs, "Measure the same thing five times and you get five answers",
               "This is not carelessness. It is what measurement is.")
bullet_list(s, 0.95, y + 0.3, 11.4, 3.4, [
    ("The reading  ", "one number off the instrument. On its own it tells you almost nothing."),
    ("The spread  ", "how far apart your repeated readings are. This is the honest width of "
                     "what you know."),
    ("The resolution  ", "the smallest division the instrument can actually show. You cannot "
                         "know anything finer than this, no matter how many readings you take."),
    ("The true value  ", "what you are trying to find. You never see it. You only ever see "
                         "readings."),
], size=19, dot=GIRDER_LT)
card(s, 0.72, y + 3.55, 11.87, 1.65, "WRITE THIS DOWN",
     ["A measurement is a range, not a number. Reporting it as a single number is a decision "
      "you made, and you should be able to say what you threw away."],
     tint=CREAM, edge=GOLD, body_size=17, label_color=REBAR)

# 6 -------------------------------------------------------------------------
s = image_slide(prs, "Two ways to be wrong", "m02-accuracy-precision.png",
                kicker="The crosshair is the true value. Each dot is one reading.",
                caption="Precise means your readings agree with each other. Accurate means they "
                        "agree with the truth. They are independent, and only one of them is "
                        "visible from inside your own data.", box_h=3.5)

# 7 -------------------------------------------------------------------------
s, y = content(prs, "This is the distinction that matters today")
speaker_card(s, 0.72, y + 0.2, 5.9, 3.5, "RANDOM ERROR",
             ["Pushes you up as often as down.",
              "Shows up as scatter in your own readings.",
              "More readings shrink it.",
              "",
              "Averaging works."], body_size=18)
card(s, 6.72, y + 0.2, 5.87, 3.5, "SYSTEMATIC ERROR",
     ["Pushes the same way every time.",
      "Invisible inside your own readings — they agree beautifully.",
      "More readings do nothing.",
      "",
      "Averaging hides it."],
     tint=RGBColor(0xFA, 0xEA, 0xEC), edge=CRIT, label_color=CRIT, body_size=18)
text(s, 0.72, y + 3.95, 11.9, 0.6,
     [[("Hold on to that last line. ", {"bold": True, "color": CRIT}),
       ("In forty minutes it is going to cost somebody an invoice.", {})]],
     size=18, color=REBAR)

# 8 -------------------------------------------------------------------------
activity(prs, "The measurement lab — handout H2-01", 25, [
    "Part A. Measure the pin five times. Put the instrument down between readings. Record "
    "every value, including the one you think is wrong.",
    "Part B. Swap pins with the pair next to you and measure theirs. Compare their mean with "
    "yours, and compare that gap with your own spread.",
    "Part C. Turn your diameter into a cross-sectional area, and carry the uncertainty with it.",
], note="No calipers on your table? A ruler works, and works better for Part A. No instrument at "
        "all? Use pin_measurements_backup.csv — 24 readings, two people.")

# 9 -------------------------------------------------------------------------
s, y = content(prs, "Part C — uncertainty does not stay where you left it")
rect(s, 0.72, y + 0.2, 11.87, 1.3, fill=PAPER, line=CONCRETE, radius=0.06)
text(s, 0.72, y + 0.5, 11.87, 0.8, "A  =  π d² / 4", size=40, color=GIRDER,
     font="Courier New", bold=True, align=PP_ALIGN.CENTER)
text(s, 0.95, y + 1.8, 11.4, 1.5,
     [[("Because the diameter is squared, a 1% error in ", {}), ("d", {"bold": True}),
       (" becomes a 2% error in ", {}), ("A", {"bold": True}),
       (". Nobody cares about the diameter. They care about the area of steel, because that is "
        "what carries the load — and that is the number your uncertainty has to survive into.",
        {})]], size=19, color=REBAR, line=1.3)
card(s, 0.72, y + 3.15, 11.87, 1.65, "WITH THE BACKUP DATA",
     [f"Mean diameter {P['mean']:.3f} mm, spread {P['sd']:.4f} mm — about "
      f"{100*P['sd']/P['mean']:.3f}% of d. Area comes out {P['area_mm2']:.0f} mm², "
      f"± {P['area_rel_pct']:.3f}% — twice the percentage you started with."],
     tint=PAPER, edge=CONCRETE, body_size=17, label_color=GIRDER)

# 10 ------------------------------------------------------------------------
s = image_slide(prs, "What the backup data shows", "m02-pin-readers.png",
                kicker="Two people, the same pin, twelve readings each",
                caption="Reader B is about 33 micrometres high on every single reading. Their own "
                        "twelve readings agree with each other beautifully. Nothing inside B's "
                        "data can reveal this — it only shows up when you compare with A.",
                box_h=3.4)

# 11 ------------------------------------------------------------------------
statement(prs, "Now open the gauge file.", "gauges_install.csv — eight gauges, twelve readings "
                                           "each, taken on install day with the roadway closed.")

# 12 ------------------------------------------------------------------------
section(prs, "2", "Eight gauges",
        "FOREMAN read all 96 numbers in 0.4 seconds. We are going to read them one gauge at a "
        "time.")

# 13 ------------------------------------------------------------------------
rows = [["Gauge", "Mean (µε)", "Spread", "Within ±25 µε?"]]
for g in [f"G{i}" for i in range(1, 9)]:
    st = GA[g]
    rows.append([g, f"{st['mean']:.2f}", str(st["range"]), "yes" if st["pass"] else "NO"])
s, yend = table_slide(prs, "One gauge at a time", rows,
                      widths=[1.7, 2.6, 2.0, 3.0], size=15,
                      col_align=["c", "r", "c", "c"],
                      row_colors={6: CRIT},
                      kicker="Specification KC-MB-12 §4.3: each gauge shall read within "
                             "±25 µε of zero under no load")

# 14 ------------------------------------------------------------------------
s = image_slide(prs, "G6", "m02-gauges-full.png",
                caption="Seven gauges sit within about one microstrain of zero. G6 reads "
                        f"{GA['G6']['mean']:.1f} — seven times the limit. Its own twelve readings "
                        "are as tight as everybody else's, so nothing inside G6 looks wrong.",
                box_h=4.3)

# 15 ------------------------------------------------------------------------
s, y = content(prs, "So how did it pass?", "FOREMAN's arithmetic is correct. Every digit of it.")
rect(s, 0.72, y + 0.25, 11.87, 1.72, fill=PAPER, line=CONCRETE, radius=0.06)
text(s, 0.72, y + 0.38, 11.87, 0.42,
     f"G6 187.50   +   the other seven (−3.00)   =   184.50 µε",
     size=22, color=GIRDER, font="Courier New", bold=True, align=PP_ALIGN.CENTER)
text(s, 0.72, y + 0.82, 11.87, 0.42,
     f"184.50  ÷  8 gauges  =  {G['array_mean']:.2f} µε",
     size=26, color=GIRDER, font="Courier New", bold=True, align=PP_ALIGN.CENTER)
text(s, 0.72, y + 1.3, 11.87, 0.42,
     f"{G['array_mean']:.2f}  <  25       PASS",
     size=22, color=RGBColor(0x2E, 0x7D, 0x4F), font="Courier New", bold=True,
     align=PP_ALIGN.CENTER)
text(s, 0.95, y + 2.2, 11.4, 1.3,
     [[("Averaging eight gauges divided one gauge's error by eight, and slid a "
        "failure of 162 µε under a limit it fails outright. ", {}),
       ("The error is not in how FOREMAN computed. It is in what it chose to compute.",
        {"bold": True, "color": CRIT})]], size=19, color=REBAR, line=1.3)
card(s, 0.72, y + 3.5, 11.87, 1.68, "AND THE SECOND ONE",
     [f"It reported {G['array_mean']:.6f} µε — six decimal places, from an instrument whose "
      f"installation record says it resolves 1 µε."],
     tint=CREAM, edge=GOLD, body_size=17, label_color=REBAR)

# 16 ------------------------------------------------------------------------
s, y = content(prs, "Somebody already knew",
               "Page 2 of the installation record, in the margin, in pen")
rect(s, 1.6, y + 0.4, 10.1, 1.5, fill=CREAM, line=GOLD, radius=0.04)
text(s, 2.0, y + 0.72, 9.3, 0.9,
     "“Northline guy was in a hurry. I watched him re-glue G6 and didn't see him "
     "re-zero it. Said it was fine.”",
     size=21, color=GIRDER, font="Caveat", line=1.15)
text(s, 2.0, y + 1.5, 9.3, 0.3, "— W. Tanaka, EIT", size=14, color=GREY, italic=True)
bullet_list(s, 0.95, y + 2.3, 11.4, 2.2, [
    ("One hour ", "spent reading the installation record would have handed you the answer."),
    ("Two hours ", "spent recomputing the eight means would have found it the hard way, and "
                   "taught you more."),
    ("Zero hours ", "carries G6 into the February study, into HW3, and into April."),
], size=18, dot=GIRDER_LT)

# 17 ------------------------------------------------------------------------
statement(prs, "This one comes back.",
          "In April a four-step workflow produces a number nobody can explain, and one of its "
          "inputs came from a February file with your name on it. Nobody will tell you which.",
          accent=STICKER)

# 18 ------------------------------------------------------------------------
s, y = content(prs, "HW1, and your ten hours",
               "Handout H2-04. Due Tuesday, one page.")
s2, yend = None, None
rows = [["What you could do", "Hours", "What it buys"],
        ["Recompute all eight gauge means yourself", "2", "You know the numbers are real"],
        ["Spot-check one gauge", "1", "Your method works — not that the rest is right"],
        ["Read the installation record and field notes", "1", "Context FOREMAN did not have"],
        ["Call Northline about the install", "1", "An answer next meeting, not today"],
        ["Re-derive FOREMAN's array figure", "2", "You learn what it actually did"],
        ["Accept FOREMAN's result as delivered", "0", "Four hours saved, a number you cannot defend"]]
gt_y = y + 0.15
tw = [5.0, 1.1, 5.4]
x = (W - sum(tw)) / 2
tbl = s.shapes.add_table(len(rows), 3, Inches(x), Inches(gt_y), Inches(sum(tw)),
                         Inches(0.42 * len(rows))).table
for ci, cw in enumerate(tw):
    tbl.columns[ci].width = Inches(cw)
for ri, row in enumerate(rows):
    tbl.rows[ri].height = Inches(0.42)
    for ci, val in enumerate(row):
        c = tbl.cell(ri, ci)
        c.margin_left = Inches(0.13); c.margin_right = Inches(0.1)
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = c.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER if ci == 1 else PP_ALIGN.LEFT
        r = p.add_run(); r.text = str(val)
        r.font.size = Pt(15); r.font.name = DISPLAY if ri == 0 else BODY
        r.font.bold = ri == 0
        r.font.color.rgb = WHITE if ri == 0 else REBAR
        c.fill.solid()
        c.fill.fore_color.rgb = GIRDER if ri == 0 else (WHITE if ri % 2 else PAPER)
text(s, 0.72, gt_y + 0.42 * len(rows) + 0.35, 11.9, 0.8,
     [[("You have ten. You cannot do all of it — that is the assignment. ", {"bold": True}),
       ("Write down what you chose not to check, on the decision log. You will want it in May.",
        {})]], size=18, color=REBAR, line=1.2)

# 19 ------------------------------------------------------------------------
s = blank(prs); bg(s, prs, WHITE)
head(s, "Mask off — two minutes")
bullet_list(s, 0.95, 1.9, 11.4, 3.4, [
    ("Hours are never points. ", "Running out of them costs you nothing. Spending them on the "
                                 "wrong thing costs you nothing."),
    ("There was no trick. ", "The data was in the file, the warning was in the margin, and the "
                             "arithmetic was correct. Nothing was hidden from you."),
    ("Nobody is expected to catch everything. ", "You are expected to know what you did not "
                                                 "check, and to say so."),
], size=18, dot=GIRDER_LT)

closer(prs, [
    ("Do", "HW1, one page, due Tuesday. Start your decision log — week 1 line"),
    ("Keep", "The decision log lives in your folder all semester. Two minutes a week"),
    ("Tuesday", "FOREMAN summarizes the county specification, and we find out what happens when "
                "a language model looks something up"),
], title="Before Tuesday")

def slides_from(source, slide_numbers):
    """Return a copy containing only the requested 1-based source slides."""
    requested = list(slide_numbers)
    if len(source.slides) != 20:
        raise ValueError(f"M02 source deck must have 20 slides, found {len(source.slides)}")
    if len(requested) != len(set(requested)):
        raise ValueError("M02 split contains duplicate slide numbers")
    if any(number < 1 or number > len(source.slides) for number in requested):
        raise ValueError("M02 split contains an out-of-range slide number")

    buffer = BytesIO()
    source.save(buffer)
    buffer.seek(0)
    result = Presentation(buffer)
    keep = set(requested)
    for index in reversed(range(len(result.slides))):
        if index + 1 not in keep:
            slide_id = result.slides._sldIdLst[index]
            result.part.drop_rel(slide_id.rId)
            del result.slides._sldIdLst[index]
    return result


student_slides = list(range(1, 10)) + [11, 12]
reveal_slides = [10] + list(range(13, 21))
if set(student_slides) & set(reveal_slides) or set(student_slides + reveal_slides) != set(range(1, 21)):
    raise ValueError("M02 student and reveal decks must partition all 20 source slides")

save(slides_from(prs, student_slides),
     os.path.join(ROOT, "build", "M02", "M02-student.pptx"))
save(slides_from(prs, reveal_slides),
     os.path.join(ROOT, "build", "M02", "M02-instructor-reveal.pptx"))
