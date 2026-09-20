"""Build the branded HW1B student handout from Oli's Markdown source."""

from __future__ import annotations

import os
import re
import runpy
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if not (SCRIPT_DIR / "build" / "facts.json").exists():
    runpy.run_path(str(SCRIPT_DIR / "make_data.py"), run_name="__main__")

sys.path.insert(0, str(SCRIPT_DIR))
from doclib import (  # noqa: E402
    BODY_FONT,
    GIRDER,
    GREY,
    HEAD_FONT,
    STICKER,
    box,
    course_doc,
    h2,
    page_field,
    para,
    run,
    save,
    table,
)


ROOT = Path(__file__).resolve().parents[2]
STUDENT_DIR = ROOT / "teaching-pack" / "07-HW-CASE-B-LIFT-STATION" / "student"
SOURCE = STUDENT_DIR / "HW1B-student-ask.md"
OUTPUT = STUDENT_DIR / "HW1B-student-ask.docx"


def section(source: str, heading: str, next_heading: str | None = None) -> str:
    start = source.index(f"## {heading}") + len(f"## {heading}")
    end = source.index(f"## {next_heading}", start) if next_heading else len(source)
    return source[start:end].strip()


def markdown_text(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    return text.strip()


def replace_footer(doc) -> None:
    footer = doc.sections[0].footer
    p = footer.paragraphs[0]
    p.clear()
    run(
        p,
        "Fictional instructional data  ·  Not verified by a licensed engineer",
        8,
        color=GREY,
        font=BODY_FONT,
    )
    p.add_run("\t")
    page_field(p)


def build() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    for required in (
        "ACMEJOB.Ai",
        "Diane PE",
        "Wes EIT",
        "FOREMAN",
        "sensors_startup.csv",
        "install_startup_note.md",
        "FOREMAN_PASS_report.md",
        "10-hour verification budget",
    ):
        if required not in source:
            raise ValueError(f"HW1B Markdown source is missing: {required}")
    for spoiler in ("PT-107", "46.810", "+4.80", "G6"):
        if spoiler in source:
            raise ValueError(f"Student handout contains spoiler: {spoiler}")

    situation = markdown_text(section(source, "Situation", "Materials"))
    materials = [
        markdown_text(line[2:])
        for line in section(source, "Materials", "Your Job").splitlines()
        if line.startswith("- ")
    ]
    job_source = section(source, "Your Job", "Deliverable")
    job_intro, *job_lines = job_source.splitlines()
    jobs = []
    for line in job_lines:
        match = re.match(r"\d+\.\s+\*\*(.+?)\*\*:\s*(.+)", line)
        if match:
            jobs.append((match.group(1), match.group(2)))
    deliverable = markdown_text(section(source, "Deliverable", "Decision Log"))
    grading_and_after = section(source, "Grading")
    grading = grading_and_after.split("**Important Notes**", 1)[0].strip()
    notes_and_constraints = grading_and_after.split("**Important Notes**", 1)[1]
    notes_source, constraints_source = notes_and_constraints.split("**Constraints**", 1)
    notes = [
        markdown_text(line[2:])
        for line in notes_source.splitlines()
        if line.startswith("* ")
    ]
    constraint_lines = [
        markdown_text(line[2:])
        for line in constraints_source.splitlines()
        if line.startswith("* ")
    ]

    doc = course_doc(
        "HW1B",
        "Second client: Lift station startup",
        kind="TRANSFER HOMEWORK",
    )
    replace_footer(doc)

    p = para(doc, "", before=0, after=5, line=1.0)
    box(p, fill="EEF3F8", color="6F8FAF", size=7, space=5)
    run(p, "HUMAN REVIEW  ", 8.5, bold=True, color=GIRDER, font=HEAD_FONT, caps=True)
    run(p, "Diane PE · Wes EIT", 9, bold=True, color=GIRDER)
    run(p, "     ")
    run(p, "MACHINE OUTPUT  ", 8.5, bold=True, color=STICKER, font=HEAD_FONT, caps=True)
    run(p, "FOREMAN", 9, bold=True, color=STICKER)

    h2(doc, "Situation", before=5)
    para(doc, situation, size=9, after=4, line=1.05)

    h2(doc, "Materials", before=5)
    rows = [["File", "What it contains"]]
    for item in materials:
        filename, description = item.split(":", 1)
        rows.append([filename, description.strip()])
    table(doc, rows, widths=[2.25, 4.65], size=8.5, zebra=None)

    h2(doc, "Your job", before=6)
    para(doc, markdown_text(job_intro), size=9, after=3, line=1.05)
    for index, (label, detail) in enumerate(jobs, 1):
        p = para(doc, "", after=2, line=1.03)
        run(p, f"{index}. {label}: ", 8.8, bold=True, color=STICKER if "FOREMAN" in label else GIRDER)
        run(p, detail, 8.8)

    h2(doc, "Deliverable", before=5)
    para(doc, deliverable, size=9, bold=True, color=GIRDER, after=4, line=1.05)

    h2(doc, "Decision log", before=5)
    table(
        doc,
        [
            ["Check", "Hours", "Done (Y/N)", "Why kept or skipped"],
            ["", "", "", ""],
            ["", "", "", ""],
        ],
        widths=[2.25, 0.7, 1.0, 2.95],
        size=8,
        zebra=None,
    )

    h2(doc, "Grading", before=5)
    para(doc, markdown_text(grading), size=8.7, after=3, line=1.03)

    rows = [["Important notes", "Constraints"]]
    max_rows = max(len(notes), len(constraint_lines))
    for index in range(max_rows):
        rows.append(
            [
                notes[index] if index < len(notes) else "",
                constraint_lines[index] if index < len(constraint_lines) else "",
            ]
        )
    table(doc, rows, widths=[4.25, 2.65], size=7.8, zebra=None)

    final_instruction = next(
        (
            markdown_text(line)
            for line in constraints_source.splitlines()
            if line.startswith("*If ")
        ),
        "",
    )
    p = para(doc, "", before=4, after=0, line=1.0)
    box(p, fill="FFF6E5", color="F2C230", size=7, space=5)
    run(p, final_instruction, 8.2, bold=True, color=GIRDER)

    save(doc, str(OUTPUT))


if __name__ == "__main__":
    build()
