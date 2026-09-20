"""Copy generated M05 deliverables into the committed teaching pack."""
import os
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(ROOT, "build")
PACK = os.path.abspath(os.path.join(ROOT, "..", "..", "teaching-pack"))
SOURCE = os.path.join(BUILD, "M05")
TARGET = os.path.join(PACK, "09-M05-overnight-alarm")

if os.path.exists(TARGET):
    shutil.rmtree(TARGET)
shutil.copytree(SOURCE, TARGET)

index_source = os.path.join(BUILD, "M05-INSTRUCTOR", "FILE-INDEX.docx")
index_target = os.path.join(PACK, "00-INSTRUCTOR", "FILE-INDEX.docx")
shutil.copy2(index_source, index_target)

print(f"assembled {len(os.listdir(SOURCE))} M05 files into teaching-pack/09-M05-overnight-alarm")
print("updated teaching-pack/00-INSTRUCTOR/FILE-INDEX.docx")
