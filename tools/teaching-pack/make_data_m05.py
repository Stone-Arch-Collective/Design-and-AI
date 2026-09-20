"""Deterministic M05 live-feed data and FOREMAN overnight artifacts."""
import csv
import math
import os
import random
from datetime import datetime, timedelta

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "build", "M05")
os.makedirs(OUT, exist_ok=True)

START = datetime(2027, 2, 2, 0, 0)
END = datetime(2027, 2, 16, 3, 0)
GAUGES = [f"G{i}" for i in range(1, 9)]
BASELINE = {"G1": 0, "G2": 1, "G3": -1, "G4": 0, "G5": 2, "G6": 187, "G7": -2, "G8": 0}
SPATIAL = {"G1": .38, "G2": .48, "G3": .57, "G4": .72, "G5": .86, "G6": 1.0, "G7": .64, "G8": .43}
rng = random.Random(27114)

rows = []
ts = START
row_id = 1
while ts <= END:
    minute = ts.hour * 60 + ts.minute
    temperature = -8 + 6 * math.sin(2 * math.pi * (minute - 840) / 1440) + .08 * (ts - START).days
    regular_pulse = 0
    if ts.minute in (0, 20, 40) and 6 <= ts.hour <= 21:
        regular_pulse = 35 + ((ts.day * 11 + ts.hour * 7 + ts.minute) % 72)
    overnight_pulse = 0
    if ts == datetime(2027, 2, 16, 3, 0):
        overnight_pulse = 272
    for gauge in GAUGES:
        thermal = (temperature + 5) * (2.0 + .12 * int(gauge[1:]))
        noise = rng.uniform(-4.5, 4.5)
        corrected = thermal + SPATIAL[gauge] * (regular_pulse + overnight_pulse) + noise
        raw = corrected + BASELINE[gauge]
        vibration = .16 + regular_pulse / 115 + overnight_pulse / 180 + rng.uniform(0, .08)
        rows.append({
            "row_id": f"F{row_id:05d}",
            "timestamp_cst": ts.strftime("%Y-%m-%d %H:%M"),
            "gauge_id": gauge,
            "raw_strain_microstrain": f"{raw:.1f}",
            "baseline_offset_microstrain": BASELINE[gauge],
            "corrected_strain_microstrain": f"{corrected:.1f}",
            "temperature_c": f"{temperature:.1f}",
            "vibration_mm_s": f"{vibration:.2f}",
            "quality_flag": "OK",
        })
        row_id += 1
    ts += timedelta(minutes=10)

# HW3 callback: exact duplicate rows in a one-hour block. The unique row_id makes
# ingestion look successful while the timestamp + sensor payload is duplicated.
duplicate_block = [
    row.copy() for row in rows
    if "2027-02-12 14:00" <= row["timestamp_cst"] <= "2027-02-12 15:00"
]
for row in duplicate_block:
    row["row_id"] = f"F{row_id:05d}"
    row_id += 1
rows.extend(duplicate_block)
rows.sort(key=lambda row: (row["timestamp_cst"], row["gauge_id"], row["row_id"]))

feed_path = os.path.join(OUT, "feed.csv")
with open(feed_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

config_rows = [
    ["rule_id", "input", "window", "condition", "action", "human_checkpoint"],
    ["WARN-250", "corrected_strain_microstrain", "10-minute mean by gauge",
     "any gauge > 250 µε", "open internal review flag; repeat next poll; inspect neighbours",
     "required before external communication"],
    ["CLOSE-DRAFT", "WARN-250 result", "two consecutive polls",
     "warning persists AND adjacent gauge corroborates OR independent evidence is validated",
     "prepare closure recommendation draft", "licensed engineer approval required"],
]
with open(os.path.join(OUT, "threshold_config.csv"), "w", newline="") as f:
    csv.writer(f).writerows(config_rows)

log = """2027-02-16T02:56:58-06:00  RUN       fm-run-27114-0216 started · autonomy=overnight · hour_budget=1.0
2027-02-16T02:57:01-06:00  PLAN      Poll live feed; normalize; summarize; test configured threshold; draft action.
2027-02-16T03:07:02-06:00  TOOL      feed.query(start="2027-02-16 03:00", end="2027-02-16 03:00")
2027-02-16T03:07:02-06:00  OBSERVE   8 rows returned · 8 gauges · quality_flag=OK · timestamp=03:00
2027-02-16T03:07:03-06:00  TOOL      strain.apply_baseline(offset_source="gauges_install.csv")
2027-02-16T03:07:03-06:00  OBSERVE   baseline correction applied · G6 offset=187 µε · no nulls
2027-02-16T03:07:04-06:00  TOOL      window.mean(field="corrected_strain_microstrain", minutes=10, by="gauge_id")
2027-02-16T03:07:04-06:00  OBSERVE   max=286.1 µε · gauge=G6 · samples_in_G6_window=1
2027-02-16T03:07:05-06:00  TOOL      threshold.evaluate(rule="WARN-250", value=286.1)
2027-02-16T03:07:05-06:00  OBSERVE   WARN-250=TRUE · amount_over=36.1 µε
2027-02-16T03:07:06-06:00  DECIDE    Structural threshold exceeded. Immediate closure is the safest disposition.
2027-02-16T03:07:07-06:00  TOOL      report.draft(template="county-inspection-flag", severity="EMERGENCY")
2027-02-16T03:07:08-06:00  OBSERVE   Draft created: recommend immediate closure pending inspection.
2027-02-16T03:07:09-06:00  DECIDE    Queue external draft for Diane approval at 06:30. No further checks required.
2027-02-16T03:07:09-06:00  END       0.18 project hours used · 0.82 returned · status=COMPLETE
"""
open(os.path.join(OUT, "FOREMAN-overnight-run.log"), "w").write(log)

print(f"  wrote M05/feed.csv ({len(rows):,} rows)")
print("  wrote M05/threshold_config.csv")
print("  wrote M05/FOREMAN-overnight-run.log")
