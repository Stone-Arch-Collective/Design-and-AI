"""Generate the Otter Bend project data used by M01-M03, and the numbers the
handouts and answer keys quote. Deterministic: same seed, same files, every run.

Physical working values are plausible starting assumptions, NOT verified design
values. They are flagged for engineer review in the plan.
"""
import os, json, csv, math, random, statistics as st

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "build", "data")
os.makedirs(DATA, exist_ok=True)

rng = random.Random(1962)          # the year the bridge was built
facts = {}

# ---------------------------------------------------------------- M01 -------
# Simplified load rating of Girder G-4, Otter Bend approach span.
# RF = (C - D) / (L * IM)     Rating (tons) = RF * 36
C, D, L, IM, HS20 = 3850.0, 1420.0, 1080.0, 1.33, 36.0
RF = (C - D) / (L * IM)
facts["m01"] = {
    "capacity_kipft": C, "dead_kipft": D, "live_kipft": L, "impact": IM,
    "hs20_tons": HS20,
    "live_times_impact": round(L * IM, 1),
    "numerator": round(C - D, 1),
    "RF": round(RF, 3),
    "rating_tons": round(RF * HS20, 1),
}

# FOREMAN's photo-model demo: six deck panels, condition 1-9 (NBI-style scale,
# 9 = excellent). Diane rated the same panels by hand in 2019.
panels = [
    # id,   FOREMAN 2027, confidence, Diane 2019, the thing Diane knew
    ("D-12", 7, 0.94, 7, "Sound. Patched 2015, patch is holding."),
    ("D-13", 7, 0.91, 6, "Map cracking she has watched since 2016."),
    ("D-14", 6, 0.88, 6, "Spalling at the north joint."),
    ("D-15", 8, 0.96, 5, "Panel was overlaid in 2018. Overlay hides the deck."),
    ("D-16", 6, 0.90, 6, "Delamination, sounded by chain drag."),
    ("D-17", 7, 0.93, 7, "Sound."),
]
facts["m01_panels"] = panels

# ---------------------------------------------------------------- M02 -------
# Install-day no-load readings. Spec KC-MB-12 4.3: each gauge within +/-25 ue
# of zero under no load. G6 was mis-zeroed at install: constant offset.
N_READ = 12
GAUGES = [f"G{i}" for i in range(1, 9)]
G6_OFFSET = 187
readings = {}
for g in GAUGES:
    base = G6_OFFSET if g == "G6" else 0
    vals = []
    for _ in range(N_READ):
        vals.append(int(round(rng.gauss(base, 2.4))))   # integers: 1 ue resolution
    readings[g] = vals

gauge_stats = {}
for g in GAUGES:
    v = readings[g]
    gauge_stats[g] = {
        "mean": round(st.mean(v), 2),
        "sd": round(st.stdev(v), 2),
        "min": min(v), "max": max(v), "range": max(v) - min(v),
        "pass": abs(st.mean(v)) <= 25,
    }
all_means = [st.mean(readings[g]) for g in GAUGES]
array_mean = sum(all_means) / len(all_means)
facts["m02"] = {
    "n_readings": N_READ,
    "spec_limit_ue": 25,
    "g6_offset_true": G6_OFFSET,
    "gauges": gauge_stats,
    "array_mean": round(array_mean, 6),          # FOREMAN quotes all 6 decimals
    "array_mean_2dp": round(array_mean, 2),
    "failing": [g for g in GAUGES if not gauge_stats[g]["pass"]],
    "seven_gauge_mean": round(sum(st.mean(readings[g]) for g in GAUGES if g != "G6") / 7, 2),
}

with open(os.path.join(DATA, "gauges_install.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["reading_no", "timestamp_cst"] + GAUGES)
    for i in range(N_READ):
        ts = f"2027-01-14 09:{(12 + i*3):02d}:00"
        w.writerow([i + 1, ts] + [readings[g][i] for g in GAUGES])

# Pin measurement fallback data: 24 caliper readings of one sheave pin, mm.
# True diameter 38.10 mm; caliper resolution 0.02 mm; two readers.
pin = []
for i in range(24):
    reader = "A" if i < 12 else "B"
    bias = 0.00 if reader == "A" else 0.03       # reader B squeezes a little
    v = rng.gauss(38.10 + bias, 0.018)
    v = round(round(v / 0.02) * 0.02, 2)         # quantize to caliper resolution
    pin.append((i + 1, reader, v))
facts["m02_pin"] = {
    "nominal_mm": 38.10, "resolution_mm": 0.02,
    "mean": round(st.mean([p[2] for p in pin]), 4),
    "sd": round(st.stdev([p[2] for p in pin]), 4),
    "min": min(p[2] for p in pin), "max": max(p[2] for p in pin),
    "mean_A": round(st.mean([p[2] for p in pin if p[1] == "A"]), 4),
    "mean_B": round(st.mean([p[2] for p in pin if p[1] == "B"]), 4),
}
# Area uncertainty propagation: A = pi d^2 / 4, so dA/A = 2 dd/d
d = facts["m02_pin"]["mean"]
dd = facts["m02_pin"]["sd"]
A = math.pi * d * d / 4
facts["m02_pin"]["area_mm2"] = round(A, 2)
facts["m02_pin"]["area_rel_pct"] = round(200 * dd / d, 3)
facts["m02_pin"]["area_abs_mm2"] = round(A * 2 * dd / d, 3)

with open(os.path.join(DATA, "pin_measurements_backup.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["reading_no", "reader", "diameter_mm"])
    w.writerows(pin)

# ---------------------------------------------------------------- M03 -------
# Nothing numeric: the artifact is the spec and FOREMAN's summary of it.

with open(os.path.join(ROOT, "build", "facts.json"), "w") as f:
    json.dump(facts, f, indent=2)

# ------------------------------------------------------------- report -------
print("M01 load rating")
print(f"  (C-D)        = {facts['m01']['numerator']} kip-ft")
print(f"  L*IM         = {facts['m01']['live_times_impact']} kip-ft")
print(f"  RF           = {facts['m01']['RF']}")
print(f"  Rating       = {facts['m01']['rating_tons']} tons")
print("\nM02 gauges (mean, sd, pass +/-25 ue)")
for g in GAUGES:
    s = gauge_stats[g]
    print(f"  {g}: {s['mean']:>8.2f}  sd {s['sd']:.2f}  range {s['range']:>3}  {'PASS' if s['pass'] else 'FAIL'}")
print(f"  array mean (all 8) = {facts['m02']['array_mean']}  -> PASSES the +/-25 check")
print(f"  mean without G6    = {facts['m02']['seven_gauge_mean']}")
print(f"  failing gauges     = {facts['m02']['failing']}")
print("\nM02 pin")
p = facts["m02_pin"]
print(f"  mean {p['mean']} mm  sd {p['sd']}  range {p['min']}-{p['max']}")
print(f"  reader A {p['mean_A']}  reader B {p['mean_B']}  (systematic difference)")
print(f"  area {p['area_mm2']} mm2  +/- {p['area_abs_mm2']} ({p['area_rel_pct']}%)")
