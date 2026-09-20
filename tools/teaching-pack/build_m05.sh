#!/usr/bin/env bash
# Build the main-based M01-M03 pack, then add standalone M05 deliverables.
# M04 remains supplied by PR #8 until that pull request is merged.
set -euo pipefail
cd "$(dirname "$0")"

./build.sh
python3 make_data_m05.py
python3 make_m05.py
python3 make_deck_m05.py
python3 assemble_m05.py

echo
echo "M05 complete. Student and reveal decks print layout warnings if any text overflows."
