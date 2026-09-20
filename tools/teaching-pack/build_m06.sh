#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

M05="${M05_FEED:-../../teaching-pack/09-M05-overnight-alarm/feed.csv}"
if [[ ! -f "$M05" ]]; then
  echo "M06 requires the preceding M05 feed at $M05." >&2
  echo "Run ./build_m05.sh, then rerun this build." >&2
  exit 1
fi

python3 make_data.py
python3 make_logos.py
python3 - <<'PY'
import cairosvg
import glob
for source in sorted(glob.glob("kit/logo/*.svg")):
    cairosvg.svg2png(url=source, write_to=source[:-4] + ".png", scale=4.0)
PY
python3 make_data_m06.py
python3 make_m06.py
python3 make_deck_m06.py
python3 assemble_m06.py
