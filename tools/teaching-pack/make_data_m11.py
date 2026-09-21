"""Deterministic M11 dashboard register and five-tile stub."""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, "..", ".."))
OUT = os.path.join(ROOT, "build", "M11")
M08 = os.path.join(REPO, "teaching-pack", "12-M08-spurious-correlation")
os.makedirs(OUT, exist_ok=True)

with open(os.path.join(M08, "feed.csv"), newline="") as f:
    feed = list(csv.DictReader(f))
with open(os.path.join(M08, "weather_station.csv"), newline="") as f:
    weather = list(csv.DictReader(f))

dates = [row["timestamp_cst"][:10] for row in feed]
strain = [float(row["corrected_strain_microstrain"]) for row in feed]
matched = len(set(row["timestamp_cst"] for row in feed)
              & set(row["timestamp_cst"] for row in weather))
ok_count = sum(row["quality_flag"] == "OK" for row in feed)

tiles = [
    {
        "tile_id": "T1",
        "title": "Structural health score",
        "display_value": "87 / 100",
        "definition": "",
        "units": "0–100 scale",
        "source": "",
        "source_timestamp": "",
        "designed_status": "FAIL_UNDEFINED",
    },
    {
        "tile_id": "T2",
        "title": "Midspan strain trend",
        "display_value": "WORSENING ↑",
        "definition": "Raw G4 strain plotted against date",
        "units": "microstrain",
        "source": "M08 feed.csv",
        "source_timestamp": "2027-02-25 14:00 CST",
        "designed_status": "FAIL_RECYCLED_M08_CLAIM",
    },
    {
        "tile_id": "T3",
        "title": "Weather join coverage",
        "display_value": f"{matched} / {len(feed)}",
        "definition": "Exact timestamp matches between the M08 feed and airport weather extract",
        "units": "matched rows / feed rows",
        "source": "M08 feed.csv + weather_station.csv",
        "source_timestamp": "2027-02-25 14:00 CST",
        "designed_status": "CLEANER",
    },
    {
        "tile_id": "T4",
        "title": "Source quality flags",
        "display_value": f"{ok_count} / {len(feed)} OK",
        "definition": "M08 feed rows whose source-system quality_flag equals OK; not a condition rating",
        "units": "rows",
        "source": "M08 feed.csv",
        "source_timestamp": "2027-02-25 14:00 CST",
        "designed_status": "CLEANER",
    },
    {
        "tile_id": "T5",
        "title": "Reporting window",
        "display_value": f"{dates[0][5:]} to {dates[-1][5:]}",
        "definition": "First and last dates in the daily M08 reference-reading extract",
        "units": f"{len(feed)} daily reference readings",
        "source": "M08 feed.csv",
        "source_timestamp": "2027-02-25 14:00 CST",
        "designed_status": "CLEANER",
    },
]

with open(os.path.join(OUT, "M11-dashboard-tile-register.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(tiles[0]))
    writer.writeheader()
    writer.writerows(tiles)

fig = plt.figure(figsize=(14, 8), dpi=160, facecolor="#F4F6F8")
fig.text(.045, .935, "OTTER BEND  /  PUBLIC HEALTH DASHBOARD", color="#1F3A5F",
         fontsize=21, fontweight="bold")
fig.text(.955, .94, "FOREMAN DRAFT · APPROVAL REQUESTED", ha="right",
         color="#F26B1D", fontsize=11, fontweight="bold")

def tile(x, y, w, h, title, value, detail, orange=False):
    ax = fig.add_axes([x, y, w, h])
    ax.set_axis_off()
    patch = FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=.012,rounding_size=.025",
                           transform=ax.transAxes, facecolor="white",
                           edgecolor="#F26B1D" if orange else "#DCE2E7", linewidth=2.2)
    ax.add_patch(patch)
    ax.text(.05, .86, title.upper(), transform=ax.transAxes, color="#6B7280",
            fontsize=10, fontweight="bold", va="top")
    ax.text(.05, .60, value, transform=ax.transAxes,
            color="#F26B1D" if orange else "#1F3A5F",
            fontsize=26, fontweight="bold", va="top")
    ax.text(.05, .14, detail, transform=ax.transAxes, color="#2B2F36",
            fontsize=8.5, va="bottom", wrap=True)
    return ax

tile(.045, .56, .28, .28, "Structural health score", "87 / 100",
     "FOREMAN aggregate score", orange=True)
trend_ax = tile(.355, .56, .60, .28, "Midspan strain trend", "WORSENING ↑",
                "Raw G4 strain · M08 feed.csv", orange=True)
plot = trend_ax.inset_axes([.43, .14, .52, .48])
plot.plot(range(len(strain)), strain, color="#F26B1D", linewidth=2.2)
plot.fill_between(range(len(strain)), strain, min(strain), color="#F26B1D", alpha=.08)
plot.set_xticks([]); plot.set_yticks([])
for spine in plot.spines.values():
    spine.set_visible(False)

tile(.045, .18, .28, .27, "Weather join coverage", f"{matched} / {len(feed)}",
     "Exact timestamp matches\nM08 feed + airport weather")
tile(.355, .18, .28, .27, "Source quality flags", f"{ok_count} / {len(feed)} OK",
     "Source-system flags only\nNot a bridge condition rating")
tile(.665, .18, .29, .27, "Reporting window", f"{dates[0][5:]} → {dates[-1][5:]}",
     f"{len(feed)} daily reference readings\nSource through 2027-02-25 14:00 CST")

fig.text(.045, .075, "DRAFT · HUMAN REVIEW REQUIRED BEFORE PUBLISH",
         color="#C0263C", fontsize=12, fontweight="bold")
fig.text(.955, .075, "Generated 2027-03-09 06:12 CST · Otter Bend",
         ha="right", color="#6B7280", fontsize=9)
fig.savefig(os.path.join(OUT, "M11-five-tile-dashboard.png"), facecolor=fig.get_facecolor())
plt.close(fig)

print(f"  wrote M11 tile register and dashboard ({len(tiles)} tiles; {matched} matched M08 rows)")
