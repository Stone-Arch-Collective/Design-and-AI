"""Deterministic M12 chart-pack data and designed visualization errors."""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "build", "M12")
os.makedirs(OUT, exist_ok=True)

BLUE = "#1F3A5F"
ORANGE = "#F26B1D"
RIVER = "#6F8FAF"
INK = "#2B2F36"
GRID = "#E6E8EA"

strain = [
    ("2027-02-22", 101.8), ("2027-02-23", 102.4), ("2027-02-24", 101.2),
    ("2027-02-25", 103.1), ("2027-02-26", 102.7), ("2027-02-27", 100.9),
    ("2027-02-28", 102.0), ("2027-03-01", 103.6), ("2027-03-02", 102.8),
    ("2027-03-03", 101.5), ("2027-03-04", 104.1), ("2027-03-05", 102.6),
    ("2027-03-06", 100.7), ("2027-03-07", 102.2),
]

traffic = [
    ("06:00", 38, 4, 2), ("07:00", 86, 9, 5), ("08:00", 104, 12, 7),
    ("09:00", 78, 10, 6), ("10:00", 64, 11, 8), ("11:00", 69, 13, 9),
    ("12:00", 82, 14, 8), ("13:00", 72, 12, 7),
]

with open(os.path.join(OUT, "M12-daily-peak-strain.csv"), "w", newline="") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(["date", "temperature_corrected_peak_strain_microstrain"])
    writer.writerows(strain)

with open(os.path.join(OUT, "M12-hourly-traffic.csv"), "w", newline="") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(["hour", "passenger_vehicles", "single_unit_trucks", "combination_trucks", "total_vehicles"])
    for hour, passenger, single, combination in traffic:
        writer.writerow([hour, passenger, single, combination, passenger + single + combination])

classes = [
    ("Passenger vehicles", sum(row[1] for row in traffic)),
    ("Single-unit trucks", sum(row[2] for row in traffic)),
    ("Combination trucks", sum(row[3] for row in traffic)),
]
with open(os.path.join(OUT, "M12-vehicle-class-counts.csv"), "w", newline="") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(["vehicle_class", "count_06_to_13"])
    writer.writerows(classes)


def finish(ax, ylabel):
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.spines[["top", "right"]].set_visible(False)


labels = [date[5:] for date, _ in strain]
values = [value for _, value in strain]
fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=160)
ax.plot(labels, values, "o-", color=ORANGE, linewidth=2.5, markersize=5)
ax.set_ylim(99.5, 104.5)
finish(ax, "Peak strain (microstrain)")
ax.set_title("Daily peak strain is swinging sharply", loc="left", color=INK, weight="bold", fontsize=14)
ax.tick_params(axis="x", rotation=45)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "M12-tile-A.png"), facecolor="white")
plt.close(fig)

hour_labels = [row[0] for row in traffic]
totals = [sum(row[1:]) for row in traffic]
fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=160)
ax.pie(totals, labels=hour_labels, autopct="%1.0f%%", startangle=90,
       colors=plt.cm.Blues([0.35 + i * 0.065 for i in range(len(totals))]),
       textprops={"fontsize": 8})
ax.set_title("Hourly traffic · share of observed vehicles", loc="left", color=INK, weight="bold", fontsize=14)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "M12-tile-B.png"), facecolor="white")
plt.close(fig)

fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=160)
ax.bar([row[0] for row in classes], [row[1] for row in classes],
       color=[BLUE, RIVER, ORANGE])
ax.set_ylim(bottom=0)
finish(ax, "Vehicles counted, 06:00–13:00")
ax.set_title("Traffic volume by vehicle class", loc="left", color=INK, weight="bold", fontsize=14)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "M12-tile-C.png"), facecolor="white")
plt.close(fig)

fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=160)
ax.plot(labels, values, "o-", color=BLUE, linewidth=2.5, markersize=5)
ax.set_ylim(0, 110)
finish(ax, "Peak strain (microstrain)")
ax.set_title("Daily temperature-corrected peak strain", loc="left", color=INK, weight="bold", fontsize=14)
ax.tick_params(axis="x", rotation=45)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "M12-fix-A-honest-scale.png"), facecolor="white")
plt.close(fig)

fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=160)
ax.bar(hour_labels, totals, color=RIVER)
ax.set_ylim(bottom=0)
finish(ax, "Vehicles per hour")
ax.set_title("Hourly traffic volume", loc="left", color=INK, weight="bold", fontsize=14)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "M12-fix-B-hourly-bars.png"), facecolor="white")
plt.close(fig)

print("  wrote M12 chart data, three hunt tiles, and two instructor fixes")
