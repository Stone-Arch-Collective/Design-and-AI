"""Assemble generated M11 artifacts into the committed teaching pack."""
import os
import re
import shutil
import tempfile
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, "..", ".."))
BUILD = os.path.join(ROOT, "build")
SOURCE = os.path.join(BUILD, "M11")
TARGET = os.path.join(REPO, "teaching-pack", "15-M11-dashboard-publish")

expected = [
    "FOREMAN-M11-dashboard-stub.docx",
    "H11-01-dashboard-review-form.docx",
    "H11-02-metric-checkpoint-guide.docx",
    "H11-03-concepts-and-publish-check.docx",
    "H11-04-note-v2-and-decision-log.docx",
    "KEY-M11-answer-key.docx",
    "M11-instructor-reveal.pptx",
    "M11-student.pptx",
    "M11-dashboard-tile-register.csv",
    "M11-five-tile-dashboard.png",
]

missing = [name for name in expected if not os.path.exists(os.path.join(SOURCE, name))]
if missing:
    raise FileNotFoundError(f"Generate M11 first; missing: {', '.join(missing)}")


def normalize_ooxml(path):
    """Remove package clock time so repeated builds produce byte-identical files."""
    fixed = (2027, 3, 9, 12, 0, 0)
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
                        r"\g<1>2027-03-09T12:00:00Z\g<2>",
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

index_source = os.path.join(BUILD, "M11-INSTRUCTOR", "FILE-INDEX.docx")
index_target = os.path.join(REPO, "teaching-pack", "00-INSTRUCTOR", "FILE-INDEX.docx")
normalize_ooxml(index_source)
shutil.copy2(index_source, index_target)
print(f"assembled {len(expected)} M11 files and instructor index")
