"""Assemble generated M06 artifacts into the committed teaching pack."""
import os
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, "..", ".."))
BUILD = os.path.join(ROOT, "build")
SOURCE = os.path.join(BUILD, "M06")
TARGET = os.path.join(REPO, "teaching-pack", "10-M06-alarm-audit")

expected = [
    "H6-01-FOREMAN-alarm-disposition.docx",
    "H6-02-distribution-and-chain-audit.docx",
    "H6-03-decision-log-and-unit-debrief.docx",
    "H6-04-Wes-gauge-file-handoff.docx",
    "KEY-M06-answer-key.docx",
    "M06-gauge-audit-and-handoff.xlsx",
    "M06-instructor-reveal.pptx",
    "M06-student.pptx",
    "traffic_counts.csv",
]

missing = [name for name in expected if not os.path.exists(os.path.join(SOURCE, name))]
if missing:
    raise FileNotFoundError(f"Generate M06 first; missing: {', '.join(missing)}")

os.makedirs(TARGET, exist_ok=True)
for name in expected:
    shutil.copy2(os.path.join(SOURCE, name), os.path.join(TARGET, name))

index_source = os.path.join(BUILD, "M06-INSTRUCTOR", "FILE-INDEX.docx")
index_target = os.path.join(REPO, "teaching-pack", "00-INSTRUCTOR", "FILE-INDEX.docx")
shutil.copy2(index_source, index_target)
print(f"assembled {len(expected)} M06 files and instructor index")
