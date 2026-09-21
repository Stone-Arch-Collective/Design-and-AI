"""Deterministic M10 coupon and paired load-test data with noise diagnostics."""
import csv
import math
import os
import statistics

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "build", "M10")
os.makedirs(OUT, exist_ok=True)

T95_DF5 = 2.571
T95_DF7 = 2.365
T99_DF7 = 3.499


def summary(values, t_value):
    mean = statistics.mean(values)
    sd = statistics.stdev(values)
    se = sd / math.sqrt(len(values))
    return mean, sd, se, mean - t_value * se, mean + t_value * se


coupons = [
    ("CP-01", 47.8), ("CP-02", 49.1), ("CP-03", 50.4),
    ("CP-04", 48.7), ("CP-05", 51.2), ("CP-06", 49.8),
]
with open(os.path.join(OUT, "coupons.csv"), "w", newline="") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(["coupon_id", "yield_strength_ksi"])
    writer.writerows(coupons)

locations = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"]
baseline = [92.0, 96.0, 99.0, 101.0, 103.0, 104.0, 102.0, 103.0]
changes = [-5.0, 0.0, 2.0, 6.0, 7.0, 10.0, 12.0, 16.0]
repeat_offsets = {
    "G1": (-1.2, 0.3, 0.9), "G2": (-0.8, -0.1, 0.9),
    "G3": (-0.7, 0.2, 0.5), "G4": (-1.0, 0.4, 0.6),
    "G5": (-0.9, 0.1, 0.8), "G6": (-1.1, 0.2, 0.9),
    "G7": (-0.6, -0.2, 0.8), "G8": (-1.3, 0.5, 0.8),
}

raw_rows = []
paired_rows = []
for location, old_mean, change in zip(locations, baseline, changes):
    new_mean = old_mean + change
    offsets = repeat_offsets[location]
    for year, center in ((2019, old_mean), (2027, new_mean)):
        for run, offset in enumerate(offsets, 1):
            raw_rows.append({
                "location_id": location,
                "test_year": year,
                "truck_pass": run,
                "analysis_strain_microstrain": f"{center + offset:.1f}",
                "reference_load_kips": "80.0",
                "lane_offset_ft": "0.0",
                "speed_mph": "5.0",
                "temperature_corrected": "YES",
                "quality_flag": "OK",
            })
    within_sd = statistics.stdev(offsets)
    paired_rows.append({
        "location_id": location,
        "mean_2019_microstrain": f"{old_mean:.1f}",
        "mean_2027_microstrain": f"{new_mean:.1f}",
        "paired_change_microstrain": f"{change:.1f}",
        "within_test_sd_microstrain": f"{within_sd:.2f}",
    })

with open(os.path.join(OUT, "loadtest_2019_2027.csv"), "w", newline="") as f:
    fields = list(raw_rows[0])
    writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(raw_rows)

with open(os.path.join(OUT, "M10-paired-location-summary.csv"), "w", newline="") as f:
    fields = list(paired_rows[0])
    writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(paired_rows)

coupon_stats = summary([value for _, value in coupons], T95_DF5)
change_stats_95 = summary(changes, T95_DF7)
change_stats_99 = summary(changes, T99_DF7)
old_mean = statistics.mean(baseline)
new_mean = statistics.mean([old + change for old, change in zip(baseline, changes)])

summary_rows = [
    ["analysis", "n", "mean", "sd", "standard_error", "confidence_level",
     "t_multiplier", "lower", "upper"],
    ["coupon yield strength (ksi)", 6, f"{coupon_stats[0]:.3f}",
     f"{coupon_stats[1]:.3f}", f"{coupon_stats[2]:.3f}", "95%",
     f"{T95_DF5:.3f}", f"{coupon_stats[3]:.3f}", f"{coupon_stats[4]:.3f}"],
    ["paired strain change (microstrain)", 8, f"{change_stats_95[0]:.3f}",
     f"{change_stats_95[1]:.3f}", f"{change_stats_95[2]:.3f}", "95%",
     f"{T95_DF7:.3f}", f"{change_stats_95[3]:.3f}", f"{change_stats_95[4]:.3f}"],
    ["paired strain change (microstrain)", 8, f"{change_stats_99[0]:.3f}",
     f"{change_stats_99[1]:.3f}", f"{change_stats_99[2]:.3f}", "99%",
     f"{T99_DF7:.3f}", f"{change_stats_99[3]:.3f}", f"{change_stats_99[4]:.3f}"],
]
with open(os.path.join(OUT, "M10-interval-summary.csv"), "w", newline="") as f:
    csv.writer(f, lineterminator="\n").writerows(summary_rows)

with open(os.path.join(OUT, "M10-test-control-check.csv"), "w", newline="") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(["control", "2019", "2027", "comparison"])
    writer.writerow(["reference truck load", "80.0 kips", "80.0 kips", "matched"])
    writer.writerow(["lane offset", "0.0 ft", "0.0 ft", "matched"])
    writer.writerow(["target speed", "5.0 mph", "5.0 mph", "matched"])
    writer.writerow(["temperature correction", "applied", "applied", "matched"])
    writer.writerow(["passes per location", "3", "3", "matched"])
    writer.writerow(["instrument resolution", "1 microstrain", "1 microstrain", "matched"])

fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=160)
x = list(range(len(locations)))
ax.plot(x, baseline, "o-", color="#6F8FAF", linewidth=2, label="2019 mean")
ax.plot(x, [old + change for old, change in zip(baseline, changes)],
        "o-", color="#F26B1D", linewidth=2, label="2027 mean")
ax.set_xticks(x, locations)
ax.set_ylabel("Analysis strain (microstrain)")
ax.set_title("Same locations, matched test protocol", loc="left",
             color="#1F3A5F", weight="bold", fontsize=14)
ax.grid(axis="y", color="#E6E8EA")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "M10-paired-location-means.png"), facecolor="white")
plt.close(fig)

fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=160)
ax.scatter(x, changes, s=60, color="#1F3A5F", zorder=3)
ax.axhline(0, color="#2B2F36", linewidth=1)
ax.axhline(change_stats_95[0], color="#F26B1D", linewidth=2,
           label=f"Mean change = {change_stats_95[0]:.1f} µε")
ax.set_xticks(x, locations)
ax.set_ylabel("2027 − 2019 (microstrain)")
ax.set_title("Paired change by location", loc="left",
             color="#1F3A5F", weight="bold", fontsize=14)
ax.grid(axis="y", color="#E6E8EA")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "M10-paired-changes.png"), facecolor="white")
plt.close(fig)

print(f"  wrote M10 coupon and load-test data ({len(raw_rows)} test rows)")
print(
    f"  old mean={old_mean:.1f}; new mean={new_mean:.1f}; change={change_stats_95[0]:.1f} "
    f"({100 * change_stats_95[0] / old_mean:.1f}%)"
)
print(
    f"  95% CI [{change_stats_95[3]:.3f}, {change_stats_95[4]:.3f}]; "
    f"99% CI [{change_stats_99[3]:.3f}, {change_stats_99[4]:.3f}]"
)
