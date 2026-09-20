#!/usr/bin/env bash
# Rebuild the M01-M03 teaching pack from source.
#
#   cd tools/teaching-pack && ./build.sh
#
# Output lands in ./build/ and is assembled into ../../teaching-pack/.
# Everything is deterministic: same inputs, same files, every run.
set -euo pipefail
cd "$(dirname "$0")"

echo "1/7  data          — gauge readings, pin measurements, the load-rating numbers"
python3 make_data.py
echo "2/7  logos         — ACMEJOB, FOREMAN, Kinnick County marks (SVG then PNG)"
python3 make_logos.py > /dev/null
python3 - <<'PY'
import cairosvg, glob, os
for f in sorted(glob.glob("kit/logo/*.svg")):
    cairosvg.svg2png(url=f, write_to=f[:-4] + ".png", scale=4.0)
print("      rendered", len(glob.glob("kit/logo/*.png")), "PNGs")
PY
echo "3/7  charts"
python3 make_charts.py
echo "4/7  handouts"
python3 make_m01.py; python3 make_m02.py; python3 make_m03.py
echo "5/7  slides"
python3 make_deck_m01.py; python3 make_deck_m02.py; python3 make_deck_m03.py
echo "6/7  brand kit + instructor guide"
python3 make_kit.py; python3 make_guide.py
echo "7/7  assemble"
python3 assemble.py
echo
echo "Done. Slide builds print layout warnings if any text overflows its box;"
echo "a clean run prints 'no layout warnings' for each deck."
