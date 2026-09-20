"""Charts and diagrams for the M01-M04 decks.

Chart palette is brand-derived and validated with the dataviz validator:
  node scripts/validate_palette.js "3A7DBF,E8631F" --mode light  -> all PASS
Status red is used only for a FAIL state and always carries a direct text label,
so identity is never colour-alone.
"""
import os, sys, json, csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import numpy as np

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "build", "charts")
os.makedirs(OUT, exist_ok=True)
FACTS = json.load(open(os.path.join(ROOT, "build", "facts.json")))

FONTDIR = os.path.join(ROOT, "fonts")
if not os.path.exists(os.path.join(FONTDIR, "barlow-latin-400-normal.ttf")):
    FONTDIR = os.path.join(FONTDIR, "ttf")
for f in os.listdir(FONTDIR):
    if f.endswith(".ttf"):
        fm.fontManager.addfont(os.path.join(FONTDIR, f))

SER1 = "#3A7DBF"      # validated categorical slot 1 (Girder Blue, chart step)
SER2 = "#E8631F"      # validated categorical slot 2 (Sticker Orange, chart step)
CRIT = "#C0263C"      # status: critical. Always with a text label.
INK = "#2B2F36"
INK2 = "#5A6470"
GRID = "#DCE0E5"
SURF = "#FFFFFF"

plt.rcParams.update({
    "font.family": ["Barlow", "DejaVu Sans"],
    "font.size": 12,
    "axes.edgecolor": GRID,
    "axes.labelcolor": INK2,
    "text.color": INK,
    "xtick.color": INK2,
    "ytick.color": INK2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.facecolor": SURF,
    "axes.facecolor": SURF,
    "savefig.facecolor": SURF,
})


def finish(fig, name, pad=0.18):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=200, bbox_inches="tight", pad_inches=pad)
    plt.close(fig)
    print("  chart", name)


# --------------------------------------------------- gauge baseline (full) --
rows = list(csv.DictReader(open(os.path.join(ROOT, "build", "data", "gauges_install.csv"))))
G = [f"G{i}" for i in range(1, 9)]
vals = {g: [float(r[g]) for r in rows] for g in G}
means = [np.mean(vals[g]) for g in G]


def gauge_chart(name, zoom):
    fig, ax = plt.subplots(figsize=(10.2, 4.3))
    lim = 30 if zoom else 210
    ax.axhspan(-25, 25, color=SER1, alpha=0.09, zorder=0)
    ax.axhline(25, color=SER1, lw=1.4, ls=(0, (5, 3)), zorder=1)
    ax.axhline(-25, color=SER1, lw=1.4, ls=(0, (5, 3)), zorder=1)
    ax.axhline(0, color=GRID, lw=1.2, zorder=1)
    for i, g in enumerate(G):
        fail = abs(means[i]) > 25
        c = CRIT if fail else SER1
        v = vals[g]
        if not zoom or abs(means[i]) <= lim:
            ax.plot([i, i], [min(v), max(v)], color=c, lw=2.4, alpha=0.32,
                    solid_capstyle="round", zorder=2)
            ax.plot([i] * len(v), v, "o", ms=5, color=c, alpha=0.5,
                    markeredgecolor=SURF, markeredgewidth=1.2, zorder=3)
            ax.plot([i], [means[i]], "o", ms=11, color=c,
                    markeredgecolor=SURF, markeredgewidth=2, zorder=4)
    ax.set_xticks(range(8))
    ax.set_xticklabels(G)
    ax.set_ylabel("No-load reading (µε)")
    ax.set_xlim(-0.6, 7.6)
    ax.grid(axis="y", color=GRID, lw=0.8)
    ax.set_axisbelow(True)

    if zoom:
        ax.set_ylim(-30, 30)
        ax.set_title("The other seven gauges, up close", fontsize=15,
                     fontfamily="Barlow Condensed", fontweight="bold",
                     color=INK, loc="left", pad=14)
        ax.annotate("G6 is off this chart at 187.5 µε",
                    xy=(5, 27.5), ha="center", va="bottom", fontsize=11,
                    color=CRIT, fontweight="bold")
        ax.annotate("", xy=(5, 30), xytext=(5, 22),
                    arrowprops=dict(arrowstyle="-|>", color=CRIT, lw=2))
        ax.annotate("Specification limit ±25 µε", xy=(7.5, 25), xytext=(7.5, 20.5),
                    ha="right", fontsize=10.5, color=SER1)
    else:
        ax.set_ylim(-20, 205)
        ax.set_title("Strain gauge baseline — every gauge, read one at a time",
                     fontsize=15, fontfamily="Barlow Condensed", fontweight="bold",
                     color=INK, loc="left", pad=14)
        ax.annotate(f"G6  —  FAIL\n{means[5]:.1f} µε, 7.5× the limit",
                    xy=(5, means[5]), xytext=(4.25, 155),
                    fontsize=12, color=CRIT, fontweight="bold", ha="right",
                    arrowprops=dict(arrowstyle="-|>", color=CRIT, lw=2,
                                    connectionstyle="arc3,rad=-0.2"))
        ax.annotate("Specification limit ±25 µε", xy=(0.1, 27), fontsize=10.5, color=SER1)
        ax.annotate("Seven gauges sit here,\nwithin about 1 µε of zero",
                    xy=(1.6, 2), xytext=(1.0, 62), fontsize=11, color=INK2,
                    arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1.6,
                                    connectionstyle="arc3,rad=0.25"))
        ax.annotate(f"FOREMAN's number: {FACTS['m02']['array_mean']:.2f} µε\n"
                    f"(all 8 averaged together)",
                    xy=(7.4, FACTS["m02"]["array_mean"]), xytext=(6.2, 108),
                    fontsize=11, color=INK, ha="center",
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.6,
                                    connectionstyle="arc3,rad=-0.25"))
        ax.plot([-0.6, 7.6], [FACTS["m02"]["array_mean"]] * 2, color=INK,
                lw=1.6, ls=(0, (2, 2)), zorder=5)
    finish(fig, name)


gauge_chart("m02-gauges-full.png", zoom=False)
gauge_chart("m02-gauges-zoom.png", zoom=True)

# ------------------------------------------------------------- pin readers --
pr = list(csv.DictReader(open(os.path.join(ROOT, "build", "data", "pin_measurements_backup.csv"))))
A = [float(r["diameter_mm"]) for r in pr if r["reader"] == "A"]
B = [float(r["diameter_mm"]) for r in pr if r["reader"] == "B"]
fig, ax = plt.subplots(figsize=(10.2, 3.5))
for vals_, y, c, lab in ((A, 1, SER1, "Reader A"), (B, 0, SER2, "Reader B")):
    jit = np.linspace(-0.13, 0.13, len(vals_))
    ax.plot(vals_, [y] * len(vals_) + jit, "o", ms=9, color=c, alpha=0.55,
            markeredgecolor=SURF, markeredgewidth=1.4, label=lab)
    m = np.mean(vals_)
    ax.plot([m, m], [y - 0.28, y + 0.28], color=c, lw=3, solid_capstyle="round")
    ax.annotate(f"{lab} mean {m:.3f} mm", xy=(m, y + 0.34), ha="center",
                fontsize=11.5, color=c, fontweight="bold")
ax.set_yticks([])
ax.set_ylim(-0.7, 1.75)
ax.set_xlabel("Measured diameter (mm)")
ax.grid(axis="x", color=GRID, lw=0.8)
ax.set_axisbelow(True)
ax.set_title("Twelve readings each, same pin, two people",
             fontsize=15, fontfamily="Barlow Condensed", fontweight="bold",
             color=INK, loc="left", pad=14)
d = np.mean(B) - np.mean(A)
ax.annotate(f"Every one of B's readings runs high.\nAveraging will never remove this.",
            xy=(np.mean(B), -0.45), ha="center", fontsize=11, color=INK2)
finish(fig, "m02-pin-readers.png")

# --------------------------------------------------------- next-token bars --
fig, ax = plt.subplots(figsize=(7.4, 3.9))
words = ["deck", "gauge", "bridge"]
probs = [0.6, 0.2, 0.2]
bars = ax.barh(range(3), probs, height=0.55, color=[SER2, SER1, SER1])
for i, (w, p) in enumerate(zip(words, probs)):
    ax.annotate(f"{p*100:.0f}%", xy=(p + 0.015, i), va="center", fontsize=13,
                color=INK, fontweight="bold")
ax.set_yticks(range(3))
ax.set_yticklabels(words, fontsize=14)
ax.invert_yaxis()
ax.set_xlim(0, 0.75)
ax.set_xticks([])
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_color(GRID)
ax.set_title("After the word THE, what comes next?",
             fontsize=15, fontfamily="Barlow Condensed", fontweight="bold",
             color=INK, loc="left", pad=14)
finish(fig, "m03-next-token.png")

# ------------------------------------------------- accuracy / precision -----
fig, axs = plt.subplots(1, 4, figsize=(12.4, 3.6))
rng = np.random.default_rng(4)
cases = [
    ("Precise\nand accurate", 0.00, 0.10, SER1),
    ("Precise,\nnot accurate", 0.52, 0.10, CRIT),
    ("Accurate,\nnot precise", 0.00, 0.50, SER1),
    ("Neither", 0.52, 0.42, INK2),
]
for ax, (lab, bias, spread, col) in zip(axs, cases):
    for r, a in ((1.0, 0.10), (0.66, 0.16), (0.33, 0.22)):
        ax.add_patch(plt.Circle((0, 0), r, color=INK2, alpha=a, zorder=0))
    ang = rng.uniform(0, 2 * np.pi, 9)
    rad = abs(rng.normal(0, spread, 9))
    x = bias + rad * np.cos(ang)
    y = rad * np.sin(ang)
    ax.plot(x, y, "o", ms=9, color=col, markeredgecolor=SURF, markeredgewidth=1.6, zorder=3)
    ax.plot([0], [0], "+", ms=17, color=INK, markeredgewidth=2.4, zorder=5)
    ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.15, 1.15)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(lab, fontsize=13.5, fontfamily="Barlow Condensed",
                 fontweight="bold", color=INK, pad=8)
axs[1].annotate("G6", xy=(0.52, -0.62), ha="center", fontsize=13,
                color=CRIT, fontweight="bold")
finish(fig, "m02-accuracy-precision.png")

# ------------------------------------------------------- RF number line -----
F = FACTS["m01"]
fig, ax = plt.subplots(figsize=(10.2, 2.5))
ax.axhline(0, color=GRID, lw=2)
ax.axvspan(0.6, 1.0, color=CRIT, alpha=0.10)
ax.axvspan(1.0, 2.0, color=SER1, alpha=0.08)
ax.axvline(1.0, color=INK, lw=2)
ax.annotate("RF = 1.00\nthe girder exactly carries the truck", xy=(1.0, -0.34),
            ha="center", va="top", fontsize=11, color=INK)
ax.annotate("below 1.00\npost or restrict it", xy=(0.79, 0.30), ha="center",
            fontsize=11, color=CRIT, fontweight="bold")
for x, lab, c, ty, ha in ((F["RF"], f"G-4  RF {F['RF']}", SER2, 0.30, "right"),
                          (1.716, f"G-3  RF 1.716", SER1, 0.55, "left")):
    ax.plot([x], [0], "o", ms=15, color=c, markeredgecolor=SURF, markeredgewidth=2.5, zorder=5)
    ax.annotate(lab, xy=(x, 0), xytext=(x + (-0.11 if ha == "right" else 0.11), ty),
                ha=ha, fontsize=13, color=c, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=c, lw=1.4))
ax.set_xlim(0.6, 2.0); ax.set_ylim(-0.85, 0.75)
ax.set_yticks([])
ax.set_xticks([0.75, 1.0, 1.25, 1.5, 1.75, 2.0])
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.set_title("Rating factor — both approach girders carry the truck",
             fontsize=15, fontfamily="Barlow Condensed", fontweight="bold",
             color=INK, loc="left", pad=12)
finish(fig, "m01-rating-factor.png")

# ------------------------------------------- deck ratings, FOREMAN vs 2019 --
panels = FACTS["m01_panels"]
fig, ax = plt.subplots(figsize=(10.2, 4.0))
x = np.arange(len(panels))
f27 = [p[1] for p in panels]
d19 = [p[3] for p in panels]
w = 0.36
ax.bar(x - w / 2 - 0.01, d19, w, color=SER1, label="Halvorsen, 2019 (by hand)")
ax.bar(x + w / 2 + 0.01, f27, w, color=SER2, label="FOREMAN, 2027 (from photos)")
for i, (a, b) in enumerate(zip(d19, f27)):
    ax.annotate(str(a), xy=(i - w / 2 - 0.01, a + 0.12), ha="center", fontsize=11, color=INK)
    ax.annotate(str(b), xy=(i + w / 2 + 0.01, b + 0.12), ha="center", fontsize=11, color=INK)
ax.set_xticks(x)
ax.set_xticklabels([p[0] for p in panels], fontsize=12.5)
ax.set_ylabel("Condition rating  (9 = excellent)")
ax.set_ylim(0, 11.6)
ax.grid(axis="y", color=GRID, lw=0.8)
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, 1.13), ncol=2, fontsize=11.5)
ax.annotate("D-15: three points apart. Overlaid in 2018 —\nthe photograph shows the overlay, not the deck.",
            xy=(3.19, 8.25), xytext=(0.55, 10.2), fontsize=12, color=CRIT,
            fontweight="bold", ha="left", va="center",
            arrowprops=dict(arrowstyle="-|>", color=CRIT, lw=2,
                            connectionstyle="arc3,rad=-0.18"))
finish(fig, "m01-deck-ratings.png")

# ------------------------------------------------- confidence vs error ------
fig, ax = plt.subplots(figsize=(8.6, 4.0))
err = [abs(p[1] - p[3]) for p in panels]
conf = [p[2] * 100 for p in panels]
for i, p in enumerate(panels):
    c = CRIT if err[i] >= 3 else SER1
    ax.plot([conf[i]], [err[i]], "o", ms=14, color=c,
            markeredgecolor=SURF, markeredgewidth=2)
    ax.annotate(p[0], xy=(conf[i], err[i] + 0.16), ha="center", fontsize=11.5, color=c)
ax.set_xlabel("FOREMAN's stated confidence (%)")
ax.set_ylabel("Points away from the 2019 rating")
ax.set_ylim(-0.4, 3.9)
ax.set_xlim(86, 98)
ax.grid(color=GRID, lw=0.8)
ax.set_axisbelow(True)
ax.set_title("The panel it was surest about is the one it got most wrong",
             fontsize=15, fontfamily="Barlow Condensed", fontweight="bold",
             color=INK, loc="left", pad=14)
finish(fig, "m01-confidence-vs-error.png")

# ------------------------------------------------------ M04 deck cores -----
core_rows = list(csv.DictReader(open(os.path.join(
    ROOT, "build", "data", "cores_2027.csv"
))))
core_vals = np.array([float(r["strength_psi"]) for r in core_rows])
core_ids = [r["core_id"] for r in core_rows]
c4 = FACTS["m04"]
fig, ax = plt.subplots(figsize=(10.4, 4.1))
y = np.linspace(-0.13, 0.13, len(core_vals))
colors = [CRIT if v < c4["comparison_psi"] else SER1 for v in core_vals]
ax.scatter(core_vals, y, s=88, c=colors, edgecolors=SURF, linewidths=1.5, zorder=3)
ax.axvline(c4["comparison_psi"], color=CRIT, lw=2, ls=(0, (5, 3)), zorder=1)
ax.axvline(c4["mean_psi"], color=SER2, lw=3, zorder=2)
ax.annotate(f"Mean  {c4['mean_psi']:,.0f} psi", xy=(c4["mean_psi"], 0.19),
            ha="center", fontsize=12, color=SER2, fontweight="bold")
ax.annotate(f"Project comparison  {c4['comparison_psi']:,} psi",
            xy=(c4["comparison_psi"], -0.24), ha="center",
            fontsize=11, color=CRIT, fontweight="bold")
for i, (ident, value, yy) in enumerate(zip(core_ids, core_vals, y)):
    if value < c4["comparison_psi"]:
        ax.annotate(ident, xy=(value, yy), xytext=(0, 8 + 12 * (i % 2)),
                    textcoords="offset points", ha="center",
                    fontsize=8.5, color=CRIT)
ax.set_yticks([])
ax.set_ylim(-0.34, 0.34)
ax.set_xlim(3600, 6200)
ax.set_xlabel("28-day compressive strength (psi)")
ax.grid(axis="x", color=GRID, lw=0.8)
ax.set_axisbelow(True)
ax.set_title("Twenty-four cores do not become one core when you average them",
             fontsize=15, fontfamily="Barlow Condensed", fontweight="bold",
             color=INK, loc="left", pad=14)
finish(fig, "m04-core-spread.png")
print("charts done")
