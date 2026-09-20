"""Deterministic M08 strain/weather data and regression exhibits."""
import csv
import math
import os
import random
from datetime import datetime, timedelta

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "build", "M08")
os.makedirs(OUT, exist_ok=True)

START = datetime(2027, 2, 1, 14, 0)
N = 25
rng = random.Random(2711408)


def fit(xs, ys):
    xbar = sum(xs) / len(xs)
    ybar = sum(ys) / len(ys)
    sxx = sum((x - xbar) ** 2 for x in xs)
    sxy = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    slope = sxy / sxx
    intercept = ybar - slope * xbar
    predictions = [intercept + slope * x for x in xs]
    sse = sum((y - p) ** 2 for y, p in zip(ys, predictions))
    sst = sum((y - ybar) ** 2 for y in ys)
    return intercept, slope, 1 - sse / sst, predictions


records = []
for day in range(N):
    ts = START + timedelta(days=day)
    # A warming seasonal path with ordinary weather variation.
    temperature = -12.0 + 0.72 * day + 2.35 * math.sin(day * 0.71) + rng.uniform(-1.05, 1.05)
    airport = temperature + rng.uniform(-0.65, 0.65)
    # Stable structural response plus thermal strain; there is no planted damage trend.
    # Noise is tuned so the date-only fit rounds to the simulation-plan value, R² = 0.87.
    strain = 176.0 + 11.8 * temperature + rng.gauss(0, 14.0)
    records.append({
        "timestamp_cst": ts.strftime("%Y-%m-%d %H:%M"),
        "date_index": day,
        "gauge_id": "G4",
        "corrected_strain_microstrain": round(strain, 1),
        "sensor_temperature_c": round(temperature, 1),
        "station_temperature_c": round(airport, 1),
        "quality_flag": "OK",
    })

date_x = [r["date_index"] for r in records]
strain_y = [r["corrected_strain_microstrain"] for r in records]
temp_x = [r["station_temperature_c"] for r in records]
date_fit = fit(date_x, strain_y)
temp_fit = fit(temp_x, strain_y)
residuals = [y - p for y, p in zip(strain_y, temp_fit[3])]
residual_fit = fit(date_x, residuals)

with open(os.path.join(OUT, "feed.csv"), "w", newline="") as f:
    fields = [
        "timestamp_cst", "gauge_id", "corrected_strain_microstrain",
        "sensor_temperature_c", "quality_flag",
    ]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for r in records:
        writer.writerow({field: r[field] for field in fields})

with open(os.path.join(OUT, "weather_station.csv"), "w", newline="") as f:
    fields = ["timestamp_cst", "station_id", "air_temperature_c", "quality_flag"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for r in records:
        writer.writerow({
            "timestamp_cst": r["timestamp_cst"],
            "station_id": "KINNICK-AP",
            "air_temperature_c": r["station_temperature_c"],
            "quality_flag": "OK",
        })

with open(os.path.join(OUT, "M08-strain-temperature-analysis.csv"), "w", newline="") as f:
    fields = [
        "timestamp_cst", "date_index", "gauge_id", "corrected_strain_microstrain",
        "station_temperature_c", "temperature_model_prediction_microstrain",
        "temperature_corrected_residual_microstrain",
    ]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for r, prediction, residual in zip(records, temp_fit[3], residuals):
        writer.writerow({
            "timestamp_cst": r["timestamp_cst"],
            "date_index": r["date_index"],
            "gauge_id": r["gauge_id"],
            "corrected_strain_microstrain": f"{r['corrected_strain_microstrain']:.1f}",
            "station_temperature_c": f"{r['station_temperature_c']:.1f}",
            "temperature_model_prediction_microstrain": f"{prediction:.1f}",
            "temperature_corrected_residual_microstrain": f"{residual:.1f}",
        })

with open(os.path.join(OUT, "M08-regression-summary.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["model", "intercept", "slope", "slope_units", "r_squared"])
    writer.writerow(["strain ~ date_index", f"{date_fit[0]:.3f}", f"{date_fit[1]:.3f}",
                     "microstrain/day", f"{date_fit[2]:.3f}"])
    writer.writerow(["strain ~ station_temperature_c", f"{temp_fit[0]:.3f}", f"{temp_fit[1]:.3f}",
                     "microstrain/degree C", f"{temp_fit[2]:.3f}"])
    writer.writerow(["temperature residual ~ date_index", f"{residual_fit[0]:.3f}",
                     f"{residual_fit[1]:.3f}", "microstrain/day", f"{residual_fit[2]:.3f}"])


def scatter(path, xs, ys, xlabel, ylabel, title, fit_values, color):
    fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=160)
    ax.scatter(xs, ys, s=45, color="#1F3A5F", edgecolor="white", linewidth=.7, zorder=3)
    ordered = sorted(zip(xs, fit_values))
    ax.plot([x for x, _ in ordered], [y for _, y in ordered], color=color, linewidth=2.5)
    ax.set_title(title, loc="left", color="#1F3A5F", weight="bold", fontsize=14)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(color="#E6E8EA", linewidth=.8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, path), transparent=False, facecolor="white")
    plt.close(fig)


scatter("M08-strain-v-date.png", date_x, strain_y, "Days since February 1",
        "G4 strain (microstrain)", f"Strain vs date · R² = {date_fit[2]:.3f}",
        date_fit[3], "#F26B1D")
scatter("M08-strain-v-temperature.png", temp_x, strain_y, "Airport air temperature (°C)",
        "G4 strain (microstrain)", f"Strain vs temperature · R² = {temp_fit[2]:.3f}",
        temp_fit[3], "#F26B1D")
scatter("M08-residual-v-date.png", date_x, residuals, "Days since February 1",
        "Temperature-corrected residual (microstrain)",
        f"Temperature-corrected residual vs date · R² = {residual_fit[2]:.3f}",
        residual_fit[3], "#6F8FAF")

print(f"  wrote M08/feed.csv and weather_station.csv ({N} matched records each)")
print(f"  date R²={date_fit[2]:.3f}; temperature R²={temp_fit[2]:.3f}; "
      f"residual date slope={residual_fit[1]:.3f} microstrain/day")
