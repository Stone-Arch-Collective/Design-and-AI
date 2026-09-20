"""Deterministic M07 inspection inventory and FOREMAN output."""
import csv
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "build", "M07")
os.makedirs(OUT, exist_ok=True)

rows = [
    ("OB-M07-001", "south approach", "fixed steel girder web", "fixed span", "surface condition", 0.96),
    ("OB-M07-002", "north approach", "fixed steel girder web", "fixed span", "surface condition", 0.95),
    ("OB-M07-003", "south approach", "concrete deck soffit", "fixed span", "surface condition", 0.94),
    ("OB-M07-004", "north approach", "concrete deck soffit", "fixed span", "surface condition", 0.93),
    ("OB-M07-005", "east tower", "tower lattice connection", "lift structure", "connection condition", 0.95),
    ("OB-M07-006", "west tower", "tower lattice connection", "lift structure", "connection condition", 0.94),
    ("OB-M07-007", "east machinery room", "lift motor housing", "moving machinery", "housing condition", 0.97),
    ("OB-M07-008", "east machinery room", "reduction gearbox", "moving machinery", "housing and seal condition", 0.96),
    ("OB-M07-009", "west tower head", "operating sheave bearing", "moving machinery", "bearing condition", 0.95),
    ("OB-M07-010", "west tower", "counterweight rope termination", "moving machinery", "rope and termination condition", 0.94),
    ("OB-M07-011", "lift span end", "span lock assembly", "moving machinery", "lock contact condition", 0.96),
    ("OB-M07-012", "west machinery room", "motor control cabinet", "moving machinery", "cabinet exterior condition", 0.93),
]

fields = [
    "image_id", "location", "component", "asset_group", "requested_review",
    "foreman_result", "foreman_confidence", "human_review_status",
]
with open(os.path.join(OUT, "M07-inspection-inventory-and-output.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for image_id, location, component, asset_group, requested_review, confidence in rows:
        writer.writerow({
            "image_id": image_id,
            "location": location,
            "component": component,
            "asset_group": asset_group,
            "requested_review": requested_review,
            "foreman_result": "No significant defect detected",
            "foreman_confidence": f"{confidence:.0%}",
            "human_review_status": "Not yet reviewed",
        })

image_dir = os.path.join(OUT, "inspection-images")
os.makedirs(image_dir, exist_ok=True)
try:
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
    body_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 20)
except OSError:
    title_font = body_font = small_font = ImageFont.load_default()

for index, (image_id, location, component, asset_group, requested_review, _) in enumerate(rows):
    image = Image.new("RGB", (1200, 720), "#D9DEE3")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 1200, 88), fill="#1F3A5F")
    draw.text((34, 22), f"{image_id}  ·  SIMULATED FIELD IMAGE", fill="white", font=title_font)
    draw.rectangle((74, 138, 1126, 562), fill="#88939D", outline="#2B2F36", width=5)
    # Deliberately schematic: the lesson is training coverage, not visual diagnosis.
    cx, cy = 600, 350
    if asset_group == "fixed span":
        draw.rectangle((250, 285, 950, 410), fill="#515B65")
        for x in range(300, 951, 130):
            draw.line((x, 285, x + 80, 410), fill="#C8D0D6", width=13)
    elif asset_group == "lift structure":
        draw.line((330, 500, 470, 185), fill="#414A54", width=28)
        draw.line((870, 500, 730, 185), fill="#414A54", width=28)
        draw.line((470, 185, 730, 185), fill="#414A54", width=22)
        draw.line((390, 365, 810, 365), fill="#D3DAE0", width=18)
    else:
        draw.ellipse((410, 200, 790, 500), fill="#4B555F", outline="#D3DAE0", width=12)
        draw.ellipse((520, 280, 680, 440), fill="#88939D", outline="#F26B1D", width=12)
        for angle_x, angle_y in [(600, 170), (805, 350), (600, 530), (395, 350)]:
            draw.ellipse((angle_x - 18, angle_y - 18, angle_x + 18, angle_y + 18), fill="#D3DAE0")
    draw.text((92, 595), component.upper(), fill="#1F3A5F", font=title_font)
    draw.text((94, 652), f"{location}  ·  requested: {requested_review}", fill="#2B2F36", font=body_font)
    draw.text((995, 665), f"{index + 1:02d}/12", fill="#2B2F36", font=small_font)
    image.save(os.path.join(image_dir, f"{image_id}.png"))

print(f"  wrote M07/M07-inspection-inventory-and-output.csv ({len(rows)} records)")
print(f"  wrote M07/inspection-images/ ({len(rows)} simulated records)")
