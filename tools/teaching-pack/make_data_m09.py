"""Deterministic M09 fatigue and sampling-variability evidence."""
import csv
import os
import random
import statistics

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "build", "M09")
os.makedirs(OUT, exist_ok=True)

# Synthetic constant-amplitude tests. Results are recorded only to the nearest
# 10,000 cycles; the intentionally absurd FOREMAN display precision is created
# later from these coarse and highly scattered inputs.
FATIGUE_LIVES = [
    35_780_000, 37_420_000, 38_960_000, 40_610_000,
    42_050_000, 43_870_000, 45_230_000, 46_980_000,
    48_740_000, 50_190_000, 52_640_000, 56_000_000,
]
ACCUMULATED_CYCLES = 3_000_184

with open(os.path.join(OUT, "fatigue_tests.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "specimen_id", "material_batch", "stress_range_mpa",
        "cycles_to_crack", "recording_resolution_cycles",
    ])
    for index, life in enumerate(FATIGUE_LIVES, 1):
        writer.writerow([f"FT-{index:02d}", "SYN-27A", 165, life, 10_000])

mean_life = statistics.mean(FATIGUE_LIVES)
sd_life = statistics.stdev(FATIGUE_LIVES)
remaining = mean_life - ACCUMULATED_CYCLES

summary = {
    "test_count": len(FATIGUE_LIVES),
    "mean_cycles_to_crack": mean_life,
    "sample_sd_cycles": sd_life,
    "coefficient_of_variation": sd_life / mean_life,
    "minimum_cycles_to_crack": min(FATIGUE_LIVES),
    "maximum_cycles_to_crack": max(FATIGUE_LIVES),
    "estimated_accumulated_cycles": ACCUMULATED_CYCLES,
    "foreman_remaining_cycles": remaining,
}
with open(os.path.join(OUT, "M09-fatigue-summary.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["metric", "value", "unit_or_note"])
    writer.writerow(["test_count", summary["test_count"], "specimens"])
    writer.writerow(["mean_cycles_to_crack", f"{mean_life:.0f}", "cycles"])
    writer.writerow(["sample_sd_cycles", f"{sd_life:.1f}", "cycles"])
    writer.writerow(["coefficient_of_variation", f"{sd_life / mean_life:.4f}", "ratio"])
    writer.writerow(["minimum_cycles_to_crack", min(FATIGUE_LIVES), "cycles"])
    writer.writerow(["maximum_cycles_to_crack", max(FATIGUE_LIVES), "cycles"])
    writer.writerow(["estimated_accumulated_cycles", ACCUMULATED_CYCLES, "cycles"])
    writer.writerow([
        "foreman_remaining_cycles",
        f"{remaining:.0f}",
        "point estimate displayed with unjustified precision",
    ])

# A finite synthetic population for seeing sampling variability by hand. This
# is a teaching demonstrator, not hidden knowledge about the actual bridge.
rng = random.Random(2010909)
zones = ["west shoulder", "east shoulder", "west lane", "east lane", "centerline"]
population = []
for index in range(1, 201):
    zone = zones[(index - 1) % len(zones)]
    zone_shift = {
        "west shoulder": -90,
        "east shoulder": 70,
        "west lane": -20,
        "east lane": 35,
        "centerline": 10,
    }[zone]
    strength = round((4_850 + zone_shift + rng.gauss(0, 520)) / 10) * 10
    strength = max(3_300, min(6_350, strength))
    population.append({
        "unit_id": f"SIM-{index:03d}",
        "zone": zone,
        "strength_psi": strength,
        "instructional_status": "SIMULATED POPULATION — NOT OTTER BEND EVIDENCE",
    })

with open(os.path.join(OUT, "core_population_200_simulated.csv"), "w", newline="") as f:
    fields = ["unit_id", "zone", "strength_psi", "instructional_status"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(population)

draw_rng = random.Random(209008)
draws = []
for draw in range(1, 13):
    sample = draw_rng.sample(population, 8)
    values = [row["strength_psi"] for row in sample]
    draws.append({
        "draw_id": f"D{draw:02d}",
        "sample_size": 8,
        "sample_unit_ids": "|".join(row["unit_id"] for row in sample),
        "sample_mean_psi": statistics.mean(values),
        "sample_sd_psi": statistics.stdev(values),
    })

with open(os.path.join(OUT, "M09-random-samples-n8.csv"), "w", newline="") as f:
    fields = [
        "draw_id", "sample_size", "sample_unit_ids",
        "sample_mean_psi", "sample_sd_psi",
    ]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for row in draws:
        writer.writerow({
            **row,
            "sample_mean_psi": f"{row['sample_mean_psi']:.1f}",
            "sample_sd_psi": f"{row['sample_sd_psi']:.1f}",
        })


def finish_axes(ax):
    ax.grid(axis="y", color="#E6E8EA", linewidth=.8)
    ax.spines[["top", "right"]].set_visible(False)


fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=160)
xs = list(range(1, len(FATIGUE_LIVES) + 1))
ax.scatter(xs, [v / 1_000_000 for v in FATIGUE_LIVES], s=58,
           color="#1F3A5F", edgecolor="white", linewidth=.7, zorder=3)
ax.axhline(mean_life / 1_000_000, color="#F26B1D", linewidth=2.5,
           label=f"mean = {mean_life / 1_000_000:.2f} million")
ax.set_title("Same test condition, visibly different fatigue lives", loc="left",
             color="#1F3A5F", weight="bold", fontsize=14)
ax.set_xlabel("Synthetic specimen")
ax.set_ylabel("Cycles to crack (millions)")
ax.legend(frameon=False)
finish_axes(ax)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "M09-fatigue-scatter.png"), facecolor="white")
plt.close(fig)

fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=160)
sample_means = [row["sample_mean_psi"] for row in draws]
ax.plot(range(1, 13), sample_means, marker="o", color="#1F3A5F", linewidth=1.8)
ax.axhline(statistics.mean([row["strength_psi"] for row in population]),
           color="#F26B1D", linewidth=2.5, label="population mean")
ax.set_title("Twelve random samples of 8 do not give one identical mean", loc="left",
             color="#1F3A5F", weight="bold", fontsize=14)
ax.set_xlabel("Random draw")
ax.set_ylabel("Sample mean strength (psi)")
ax.set_xticks(range(1, 13))
ax.legend(frameon=False)
finish_axes(ax)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "M09-sample-means.png"), facecolor="white")
plt.close(fig)

print(f"  fatigue mean={mean_life:,.0f}; SD={sd_life:,.0f}; "
      f"FOREMAN={remaining:.0f} cycles")
print(f"  wrote 200-unit sampling demonstrator and {len(draws)} random draws")
