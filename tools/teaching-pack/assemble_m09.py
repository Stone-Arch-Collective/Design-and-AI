"""Assemble generated M09 artifacts into the committed teaching pack."""
import os
import re
import shutil
import tempfile
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, "..", ".."))
BUILD = os.path.join(ROOT, "build")
SOURCE = os.path.join(BUILD, "M09")
TARGET = os.path.join(REPO, "teaching-pack", "13-M09-false-precision")

expected = [
    "FOREMAN-M09-fatigue-life-output.docx",
    "H9-01-fatigue-evidence-guide.docx",
    "H9-02-precision-audit.docx",
    "H9-03-concepts-and-reporting.docx",
    "H9-04-random-sampling-lab.docx",
    "H9-05-core-sampling-frame-audit.docx",
    "H9-06-note-v2-and-decision-log.docx",
    "KEY-M09-answer-key.docx",
    "M09-instructor-reveal.pptx",
    "M09-student.pptx",
    "fatigue_tests.csv",
    "M09-fatigue-summary.csv",
    "core_population_200_simulated.csv",
    "M09-random-samples-n8.csv",
    "cores_2027.csv",
]

missing = [name for name in expected if not os.path.exists(os.path.join(SOURCE, name))]
if missing:
    raise FileNotFoundError(f"Generate M09 first; missing: {', '.join(missing)}")


def normalize_ooxml(path):
    """Remove package clock time so repeated builds produce byte-identical files."""
    fixed = (2027, 3, 2, 12, 0, 0)
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
                        r"\g<1>2027-03-02T12:00:00Z\g<2>",
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

index_source = os.path.join(BUILD, "M09-INSTRUCTOR", "FILE-INDEX.docx")
index_target = os.path.join(REPO, "teaching-pack", "00-INSTRUCTOR", "FILE-INDEX.docx")
normalize_ooxml(index_source)
shutil.copy2(index_source, index_target)
print(f"assembled {len(expected)} M09 files and instructor index")
