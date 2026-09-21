#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

python3 make_data.py
python3 make_logos.py
python3 - <<'PY'
import cairosvg
import glob
for source in sorted(glob.glob("kit/logo/*.svg")):
    cairosvg.svg2png(url=source, write_to=source[:-4] + ".png", scale=4.0)
PY
python3 make_data_m14.py
python3 make_m14.py
python3 make_deck_m14.py
python3 assemble_m14.py
