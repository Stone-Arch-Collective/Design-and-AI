"""Assemble generated M13 artifacts into the committed teaching pack."""
import os
import re
import shutil
import tempfile
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, "..", ".."))
BUILD = os.path.join(ROOT, "build")
SOURCE = os.path.join(BUILD, "M13")
TARGET = os.path.join(REPO, "teaching-pack", "17-M13-wes-handoff")

expected = [
    "WES-M13-partial-handoff-note.docx",
    "FOREMAN-M13-pipeline-log.docx",
    "FOREMAN-M13-pipeline-log.csv",
    "H13-01-pipeline-trace-hunt.docx",
    "H13-02-pipeline-concepts.docx",
    "H13-03-note-v2-unchecked-log.docx",
    "H13-04-unit-2-debrief.docx",
    "KEY-M13-answer-key.docx",
    "M13-instructor-reveal.pptx",
    "M13-student.pptx",
    "wes_handoff.xlsx",
    "M13-pipeline-output.csv",
]

missing = [name for name in expected if not os.path.exists(os.path.join(SOURCE, name))]
if missing:
    raise FileNotFoundError(f"Generate M13 first; missing: {', '.join(missing)}")


def normalize_ooxml(path):
    """Remove package clock time so repeated builds produce byte-identical files."""
    fixed = (2027, 3, 16, 12, 0, 0)
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(path)[1]) as tmp:
        temp_path = tmp.name
    try:
        with zipfile.ZipFile(path, "r") as source, zipfile.ZipFile(
            temp_path, "w", compression=zipfile.ZIP_DEFLATED
        ) as target:
            for item in source.infolist():
                data = source.read(item.filename)
                if item.filename == "docProps/core.xml":
                    text = data.decode("utf-8")
                    text = re.sub(
                        r"(<dcterms:(?:created|modified)[^>]*>).*?(</dcterms:(?:created|modified)>)",
                        r"\g<1>2027-03-16T12:00:00Z\g<2>",
                        text,
                    )
                    data = text.encode("utf-8")
                info = zipfile.ZipInfo(item.filename, fixed)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = item.external_attr
                info.create_system = item.create_system
                target.writestr(info, data)
        os.replace(temp_path, path)
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)


os.makedirs(TARGET, exist_ok=True)
for name in expected:
    source_path = os.path.join(SOURCE, name)
    if os.path.splitext(name)[1] in {".docx", ".pptx", ".xlsx"}:
        normalize_ooxml(source_path)
    shutil.copy2(source_path, os.path.join(TARGET, name))

index_source = os.path.join(BUILD, "M13-INSTRUCTOR", "FILE-INDEX.docx")
index_target = os.path.join(REPO, "teaching-pack", "00-INSTRUCTOR", "FILE-INDEX.docx")
normalize_ooxml(index_source)
shutil.copy2(index_source, index_target)
print(f"assembled {len(expected)} M13 files and instructor index")
