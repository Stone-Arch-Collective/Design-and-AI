"""Student brand kit: brand guide, Word memo template, PowerPoint template,
Excel calculation sheet, logo files, fonts, README."""
import os, sys, shutil, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doclib import *
from docx.enum.text import WD_ALIGN_PARAGRAPH

KIT = os.path.join(BUILD, "brand-kit")
os.makedirs(KIT, exist_ok=True)

# ---------------------------------------------------------- brand guide ----
d = acme_doc(subtitle="Brand Guide for Project Staff",
             footer="ACMEJOB.Ai brand guide  ·  v1.0  ·  Otter Bend project team")
h1(d, "ACMEJOB.Ai — Brand Guide")
para(d, "Everything you hand to the county has the firm's name on it. This page is how to make "
        "it look like the firm meant it. Two pages, and then you never have to think about it "
        "again.", size=10, after=10)

h2(d, "The name", before=4)
para(d, "The firm is ACMEJOB.Ai. Not AcmeJob, not ACMEJob, not Acme Job. The “.Ai” is "
        "capital A, lowercase i, and it is part of the name whether or not anyone here is happy "
        "about that.", after=8)
callout(d, "Est. 1967", "The firm is sixty years old and the AI is two. The logo says both "
                        "things on purpose: a bridge that was drawn with a straightedge, and a "
                        "sticker somebody slapped on it in 2025.")

h2(d, "Colour")
table(d, [
    ["Name", "Hex", "Where it goes"],
    ["Girder Blue", "#1F3A5F", "Headings, the logo, anything structural"],
    ["Sticker Orange", "#F26B1D", "The .Ai sticker, FOREMAN, and nothing else"],
    ["Rebar Charcoal", "#2B2F36", "Body text"],
    ["Cured Concrete", "#E6E8EA", "Rules, borders, table lines"],
    ["Kinnick River", "#6F8FAF", "Secondary text, captions"],
    ["Diane's Highlighter", "#F2C230", "Callout boxes. Sparingly."],
    ["Deferred Maintenance Rust", "#9C4A2F", "County documents only. Not ours."],
], widths=[2.1, 1.2, 3.6])
callout(d, "The one rule that matters",
        "Orange means the machine said it. Blue means a person said it. Keep that straight in "
        "everything you produce and your reader never has to ask.",
        fill="FFF1E8", edge="F26B1D")

h2(d, "Type")
table(d, [
    ["Use", "Font", "If it is not installed"],
    ["Headings", "Barlow Condensed SemiBold", "Arial Narrow Bold"],
    ["Body", "Barlow Regular", "Arial"],
    ["Numbers, code, data", "IBM Plex Mono", "Courier New"],
    ["Diane's handwriting", "Caveat", "Do not substitute — leave it as type"],
], widths=[1.9, 2.5, 2.5])
para(d, "All three fonts are in the fonts folder of this kit under the SIL Open Font License, "
        "which permits you to install and use them. Install them before you start.",
     size=9, italic=True, color=GREY, after=8)

h2(d, "Voice")
bullets(d, [
    ("Say the thing first. ", "Open a document by saying what it is, not by describing how "
     "important the reader's situation is."),
    ("Numbers carry units and uncertainty. ", "“23.06 µε” is a number. "
     "“23.062500 µε” is a performance."),
    ("Never write what you cannot support. ", "If you would not want to be asked where it came "
     "from, do not put it on letterhead."),
    ("Words we do not use: ", "leverage, transform, unlock, seamless, cutting-edge, "
     "revolutionary, at the end of the day."),
])

d.add_page_break()
h1(d, "Using the templates")
h2(d, "What is in this kit", before=4)
table(d, [
    ["File", "What it is for"],
    ["ACMEJOB-memo-template.docx", "Any memo, note or short report on firm letterhead"],
    ["ACMEJOB-deck-template.pptx", "Presentations, including the county board briefing in May"],
    ["ACMEJOB-calculation-sheet.xlsx", "Any calculation you want somebody else to be able to check"],
    ["logo/", "Logo files. SVG for anything that scales, PNG for documents"],
    ["fonts/", "The three fonts, with their licence"],
], widths=[2.9, 4.0])

h2(d, "Which logo file")
table(d, [
    ["File", "Use it when"],
    ["acmejob-logo-primary.svg", "Covers, title slides, anything large"],
    ["acmejob-logo-horizontal.svg", "Document headers. This is the one you will use most"],
    ["acmejob-logo-stacked.svg", "Square or narrow spaces"],
    ["acmejob-mark.svg", "The bridge alone, where the name is already on the page"],
    ["*-dark.svg", "Any of the above on a dark background"],
    ["foreman-mark.svg", "Labelling FOREMAN output as FOREMAN output. Always label it"],
], widths=[2.9, 4.0])

h2(d, "Rules for the logo")
bullets(d, [
    "Leave clear space around it, at least the height of the bridge mark.",
    "Do not recolour it, stretch it, rotate it, or put it on a busy photograph.",
    "Do not remove the .Ai sticker. Several people here have tried.",
    "Minimum size: the horizontal logo should never be smaller than 1.2 inches wide, or the "
    "sticker becomes an orange smudge.",
])

h2(d, "The calculation sheet")
para(d, "Every calculation you hand to somebody else goes on the calculation sheet, with the "
        "inputs in the blue cells and the formulas showing. The sheet exists so that a reviewer "
        "can change an input and watch the answer move. A number typed into a cell where a "
        "formula belongs is the single most common way a calculation becomes uncheckable.",
     after=8)
callout(d, "This is the brand",
        "Not the colours. A document from this firm is one somebody else can check. Everything "
        "on these two pages is in service of that.")

save(d, os.path.join(KIT, "ACMEJOB-brand-guide.docx"))

# ------------------------------------------------------- memo template -----
d = acme_doc(subtitle="Internal Memorandum")
memo_block(d, to="[Name, role]", frm="[Your name, role]",
           date="[Day, Month D, YYYY]", re_="[What this memo is about, in one line]")
para(d, "[Open by saying what this is. One or two sentences. Do not warm up.]", after=8)
h2(d, "[Section heading]", before=8)
para(d, "[Body text. Barlow Regular, 10 point. Keep paragraphs to three or four sentences.]",
     after=8)
h2(d, "[A table, if you have one]")
table(d, [["Column", "Column", "Column"],
          ["", "", ""],
          ["", "", ""]], widths=[2.3, 2.3, 2.3])
para(d, "", after=6)
callout(d, "Callout", "[For the one thing the reader must not miss. Use at most one of these "
                      "per page.]")
h2(d, "How I know this is right")
para(d, "[Your note. In February this is one sentence: the claim, and what you checked it "
        "against. It gets longer as the semester goes on.]", after=8)
p = para(d, "", after=10, before=4)
bottom_rule(p, "C9CFD6", 6)
para(d, "Delete these instructions before you send anything. Replace the footer text in "
        "View → Header and Footer with your own project reference.",
     size=8.5, italic=True, color=GREY)
save(d, os.path.join(KIT, "ACMEJOB-memo-template.docx"))

# ---------------------------------------------------- calculation sheet ----
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Calculation"
thin = Side(style="thin", color="C9CFD6")
box_b = Border(left=thin, right=thin, top=thin, bottom=thin)
HEAD = PatternFill("solid", fgColor="1F3A5F")
INPUT = PatternFill("solid", fgColor="EEF3F8")
NOTE = PatternFill("solid", fgColor="FFF6E5")
BLUE = Font(name="Arial", size=10, color="0000FF")
BLK = Font(name="Arial", size=10)
WH = Font(name="Arial", size=11, bold=True, color="FFFFFF")

widths = [3, 34, 15, 10, 30]
for i, w in enumerate(widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

ws["B2"] = "ACMEJOB.Ai — CALCULATION SHEET"
ws["B2"].font = Font(name="Arial", size=14, bold=True, color="1F3A5F")
meta = [("Project", "Otter Bend Lift Bridge — Kinnick County 27-114"),
        ("Calculation", "[what this computes]"),
        ("Prepared by", "[your name]"),
        ("Date", "[date]"),
        ("Checked by", "[leave blank until somebody actually checks it]")]
r = 4
for k, v in meta:
    ws.cell(r, 2, k).font = Font(name="Arial", size=10, bold=True)
    c = ws.cell(r, 3, v); c.font = BLUE; c.fill = INPUT; c.border = box_b
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=5)
    r += 1

r += 1
ws.cell(r, 2, "INPUTS").font = Font(name="Arial", size=11, bold=True, color="1F3A5F")
r += 1
for h, col in zip(["Quantity", "Value", "Units", "Source — where this number came from"],
                  [2, 3, 4, 5]):
    c = ws.cell(r, col, h); c.font = WH; c.fill = HEAD; c.border = box_b
    c.alignment = Alignment(horizontal="center")
r += 1
first_input = r
for q, v, u, srcv in [
    ("Girder moment capacity, C", 3850, "kip-ft", "Section properties + coupon tests"),
    ("Dead load moment, D", 1420, "kip-ft", "Structure self-weight"),
    ("Live load moment, L", 1080, "kip-ft", "HS-20 rating truck"),
    ("Impact factor, IM", 1.33, "—", "Standard allowance"),
    ("Rating truck weight", 36, "tons", "HS-20"),
]:
    ws.cell(r, 2, q).font = BLK
    c = ws.cell(r, 3, v); c.font = BLUE; c.fill = INPUT
    ws.cell(r, 4, u).font = BLK
    ws.cell(r, 5, srcv).font = BLK
    for col in range(2, 6):
        ws.cell(r, col).border = box_b
    r += 1

r += 1
ws.cell(r, 2, "CALCULATION").font = Font(name="Arial", size=11, bold=True, color="1F3A5F")
r += 1
for h, col in zip(["Step", "Result", "Units", "Formula as written"], [2, 3, 4, 5]):
    c = ws.cell(r, col, h); c.font = WH; c.fill = HEAD; c.border = box_b
    c.alignment = Alignment(horizontal="center")
r += 1
C, D, L, IM, TW = [f"C{first_input + i}" for i in range(5)]
steps = [("Capacity minus dead load", f"={C}-{D}", "kip-ft", "C − D"),
         ("Live load with impact", f"={L}*{IM}", "kip-ft", "L × IM"),
         ("Rating factor", None, "—", "(C − D) ÷ (L × IM)"),
         ("Rating", None, "tons", "RF × rating truck weight")]
srow = r
for i, (name, formula, u, shown) in enumerate(steps):
    ws.cell(r, 2, name).font = BLK
    if formula is None:
        formula = f"=C{srow}/C{srow+1}" if i == 2 else f"=C{srow+2}*{TW}"
    c = ws.cell(r, 3, formula); c.font = BLK
    c.number_format = "0.000" if i >= 2 else "#,##0.0"
    ws.cell(r, 4, u).font = BLK
    ws.cell(r, 5, shown).font = BLK
    for col in range(2, 6):
        ws.cell(r, col).border = box_b
    r += 1

r += 1
ws.cell(r, 2, "HOW I KNOW THIS IS RIGHT").font = Font(name="Arial", size=11, bold=True,
                                                      color="1F3A5F")
r += 1
c = ws.cell(r, 2, "[The claim, and what you checked it against. One sentence in February.]")
c.font = BLUE; c.fill = NOTE; c.alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells(start_row=r, start_column=2, end_row=r + 2, end_column=5)
for rr in range(r, r + 3):
    for col in range(2, 6):
        ws.cell(rr, col).border = box_b
r += 4

ws.cell(r, 2, "LEGEND").font = Font(name="Arial", size=10, bold=True)
r += 1
for t in ["Blue text on a pale blue fill = an input. These are the only cells you type into.",
          "Black text = a formula. Never replace a formula with a typed number.",
          "Every input names its source. An input with no source is a guess wearing a number.",
          "Change an input and watch the answer move. If it does not move, something is typed in "
          "that should not be."]:
    ws.cell(r, 2, t).font = Font(name="Arial", size=9, color="6B7280")
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
    r += 1

ws.sheet_view.showGridLines = False
wb.save(os.path.join(KIT, "ACMEJOB-calculation-sheet.xlsx"))
print("  wrote ACMEJOB-calculation-sheet.xlsx")

# ---------------------------------------------------------- deck template --
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import slidelib as S

prs = S.deck()
S.title_slide(prs, "Otter Bend Lift Bridge  ·  Kinnick County 27-114",
              "[Your title here]", "[One line saying what this is]",
              "[Your name]  ·  [date]")
s, y = S.content(prs, "[Section title]", "[Optional one-line kicker]")
S.bullet_list(s, 0.95, y + 0.3, 11.4, 3.0, [
    ("A point  ", "with the lead in bold and the rest in plain text."),
    ("Another  ", "keep these to one or two lines each."),
    ("A third  ", "four bullets is usually the limit before a slide stops being read."),
], size=19, dot=S.GIRDER_LT)
S.card(s, 0.72, y + 3.3, 11.87, 1.4, "CALLOUT",
       ["[The one thing on this slide that must survive.]"],
       tint=S.CREAM, edge=S.GOLD, body_size=18, label_color=S.REBAR)

s, y = S.content(prs, "[Two things side by side]")
S.speaker_card(s, 0.72, y + 0.2, 5.9, 3.4, "A PERSON SAID THIS",
               ["Blue card. Use it for anything a human produced — a colleague, the county, "
                "your own analysis."], body_size=17)
S.speaker_card(s, 6.72, y + 0.2, 5.87, 3.4, "FOREMAN SAID THIS",
               ["Orange card. Use it for anything an AI produced, always labelled as such. "
                "Never mix the two colours up."], machine=True, body_size=17)

S.table_slide(prs, "[A table]",
              [["Column", "Column", "Column"], ["", "", ""], ["", "", ""], ["", "", ""]],
              widths=[4.0, 4.0, 4.0], size=15)
S.statement(prs, "[One line that deserves\na slide of its own.]", "[Optional attribution]")
S.section(prs, "1", "[Section break]", "[What this section is for]")
S.closer(prs, [("Item", "[what you want them to do]"),
               ("Item", "[when]"),
               ("Item", "[what is next]")], title="[Closing slide]")
S.save(prs, os.path.join(KIT, "ACMEJOB-deck-template.pptx"))

# -------------------------------------------------------------- assets -----
for sub in ("logo", "fonts"):
    os.makedirs(os.path.join(KIT, sub), exist_ok=True)
for f in glob.glob(os.path.join(ROOT, "kit", "logo", "*")):
    shutil.copy(f, os.path.join(KIT, "logo", os.path.basename(f)))
FONTDIR = os.path.join(ROOT, "fonts")
if not glob.glob(os.path.join(FONTDIR, "*.ttf")):
    FONTDIR = os.path.join(FONTDIR, "ttf")
for f in glob.glob(os.path.join(FONTDIR, "*.ttf")):
    shutil.copy(f, os.path.join(KIT, "fonts", os.path.basename(f)))
for src in glob.glob(os.path.join(ROOT, "fonts", "LICENSE-*.txt")):
    shutil.copy(src, os.path.join(KIT, "fonts", os.path.basename(src)))
for pkg, name in (("barlow", "Barlow"), ("barlow-condensed", "Barlow-Condensed"),
                  ("caveat", "Caveat"), ("ibm-plex-mono", "IBM-Plex-Mono")):
    src = os.path.join(ROOT, "fonts", f"x_fontsource-{pkg}-5.3.0", "package", "LICENSE")
    if os.path.exists(src):
        shutil.copy(src, os.path.join(KIT, "fonts", f"LICENSE-{name}.txt"))

open(os.path.join(KIT, "README.txt"), "w").write("""ACMEJOB.Ai BRAND KIT
====================
SEIS 201: AI for CE/ME Engineers — University of St. Thomas

Everything you hand in this semester goes on ACMEJOB.Ai letterhead. This kit is
how. Start here.

FIRST, INSTALL THE FONTS
  Open fonts/ and install all sixteen .ttf files (select all, right-click,
  Install — or drag them into Font Book on a Mac). Do this before you open the
  templates, or your documents will silently substitute Arial and the spacing
  will shift.

THEN READ
  ACMEJOB-brand-guide.docx      Two pages. Colour, type, voice, logo rules.

THE TEMPLATES
  ACMEJOB-memo-template.docx    Memos, notes, short reports.
  ACMEJOB-deck-template.pptx    Presentations, including the May county briefing.
  ACMEJOB-calculation-sheet.xlsx  Any calculation somebody else has to check.

  Save a copy before you edit. Do not work in the original.

LOGO FILES  (logo/)
  Use .svg wherever it will scale. Use .png in Word and PowerPoint.
  acmejob-logo-horizontal    Document headers. The one you will use most.
  acmejob-logo-primary       Covers and title slides.
  acmejob-logo-stacked       Square or narrow spaces.
  acmejob-mark               The bridge alone.
  foreman-mark               Label FOREMAN output as FOREMAN output. Always.
  kinnick-county-seal        County documents only. Never on our letterhead.
  Anything ending -dark is for dark backgrounds.

THE ONE RULE
  Orange means a machine said it. Blue means a person said it.
  Keep that straight and your reader never has to ask.

FONT LICENCES
  Barlow, Barlow Condensed, Caveat and IBM Plex Mono are all licensed under the
  SIL Open Font License 1.1. The licence text is in fonts/. You may install and
  use them freely, including in work you hand in and work you publish.

ACMEJOB.Ai, FOREMAN, the Otter Bend Lift Bridge and Kinnick County are fictional,
invented for this course. Any resemblance to a real firm, product or structure is
coincidental.
""")
print("  wrote README.txt")

# zip it
z = os.path.join(BUILD, "ACMEJOB-brand-kit")
if os.path.exists(z + ".zip"):
    os.remove(z + ".zip")
shutil.make_archive(z, "zip", KIT)
print("  wrote ACMEJOB-brand-kit.zip",
      f"({os.path.getsize(z + '.zip') // 1024} KB)")
