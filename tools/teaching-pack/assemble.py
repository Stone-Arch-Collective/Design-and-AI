import os, shutil, glob
ROOT = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(ROOT, "build")
OUT = os.path.abspath(os.path.join(ROOT, "..", "..", "teaching-pack"))
if os.path.exists(OUT): shutil.rmtree(OUT)
plan = {
 "00-INSTRUCTOR": [("build/00-INSTRUCTOR/*.docx", None)],
 # The brand kit ships as the zip students receive; no unzipped copy in the repo.
 "01-BRAND-KIT":  [("build/ACMEJOB-brand-kit.zip", None)],
 "02-M01-first-day": [("build/M01/*.docx", None), ("build/M01/*.pptx", None)],
 "03-M02-measurement": [("build/M02/*.docx", None), ("build/M02/*.pptx", None), ("build/M02/*.csv", None)],
 "04-M03-hallucination": [("build/M03/*.docx", None), ("build/M03/*.pptx", None)],
 "05-CHARTS": [("build/charts/*.png", None)],
}
n=0
for folder, items in plan.items():
    dst = os.path.join(OUT, folder); os.makedirs(dst, exist_ok=True)
    for pat, sub in items:
        src = os.path.join(ROOT, pat)
        if sub:
            shutil.copytree(src, os.path.join(dst, sub)); n += sum(len(f) for _,_,f in os.walk(src))
        else:
            for f in sorted(glob.glob(src)):
                shutil.copy(f, dst); n += 1
print(f"{n} files")
for r, dirs, files in sorted(os.walk(OUT)):
    rel = os.path.relpath(r, OUT)
    if rel.startswith("01-BRAND-KIT/unzipped") and rel != "01-BRAND-KIT/unzipped": continue
    if rel != ".": print(f"\n{rel}/")
    for f in sorted(files): print(f"   {f}")
