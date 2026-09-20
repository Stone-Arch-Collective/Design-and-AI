"""Generate the Otter Bend site-location schematic.

The bridge geometry is deliberately explicit here: County Road 9 crosses the
Kinnick River, and the lift-bridge symbol is centered on that crossing.
"""

from pathlib import Path
import sys

import cairosvg

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from brand import (  # noqa: E402
    B400,
    B600,
    BC500,
    BC600,
    BC700,
    CAV700,
    GIRDER,
    MONO700,
    RIVER,
    STICKER,
    text_path,
)

W, H = 1936, 1248
CREAM = "#F8F7F3"
WATER = "#A8C9E0"
WATER_EDGE = "#78A7C9"
ROAD = "#F2C230"
ROAD_EDGE = "#C99B18"
SECONDARY = "#D9D6CE"
TOWN = "#E4E1D8"
MUTED = "#6F7885"
INK = "#2B2F36"


def label(font, text, size, x, y, color=GIRDER, **kwargs):
    return text_path(font, text, size, x, y, color, **kwargs)


parts = [f'<rect width="{W}" height="{H}" rx="24" fill="{CREAM}"/>']

# Kinnick River: the map's dominant geographic feature.
river_path = (
    "M -80 354 "
    "C 250 350 425 430 615 615 "
    "C 830 825 1080 862 1335 824 "
    "C 1580 788 1715 665 2015 705"
)
parts += [
    f'<path d="{river_path}" fill="none" stroke="{WATER_EDGE}" '
    'stroke-width="148" stroke-linecap="round"/>',
    f'<path d="{river_path}" fill="none" stroke="{WATER}" '
    'stroke-width="136" stroke-linecap="round"/>',
    label(CAV700, "Kinnick River", 45, 228, 420, RIVER, extra='transform="rotate(18 228 420)"'),
]

# Otter Bend street grid.
parts += [
    '<rect x="190" y="755" width="548" height="410" fill="#ECEAE3"/>',
    '<g fill="#DCD9D0">',
]
for row in range(3):
    for col in range(4):
        x = 220 + col * 125
        y = 790 + row * 108
        parts.append(f'<rect x="{x}" y="{y}" width="78" height="65"/>')
parts += [
    "</g>",
    f'<path d="M 485 742 V 1182" stroke="{SECONDARY}" stroke-width="15"/>',
    f'<path d="M 485 900 H 980" stroke="{SECONDARY}" stroke-width="15"/>',
    label(BC700, "OTTER BEND", 37, 240, 730, MUTED, tracking=3),
    label(BC500, "pop. 3,140", 22, 245, 765, MUTED),
]

# Quiet secondary road and Kinnickville.
parts += [
    f'<path d="M 1345 190 V 520 L 1600 600" fill="none" stroke="{SECONDARY}" '
    'stroke-width="15" stroke-linejoin="round"/>',
    f'<circle cx="1485" cy="395" r="12" fill="{MUTED}"/>',
    label(B600, "Kinnickville (county seat, 11 mi)", 20, 1515, 403, MUTED),
]

# County Road 9. Its diagonal segment visibly crosses both river banks.
road_path = "M 92 532 H 620 L 866 824 L 980 900 H 1844"
parts += [
    f'<path d="{road_path}" fill="none" stroke="{ROAD_EDGE}" stroke-width="24" '
    'stroke-linecap="round" stroke-linejoin="round"/>',
    f'<path d="{road_path}" fill="none" stroke="{ROAD}" stroke-width="16" '
    'stroke-linecap="round" stroke-linejoin="round"/>',
]

# CR 9 shield.
parts += [
    f'<rect x="1118" y="642" width="86" height="70" rx="10" fill="{CREAM}" '
    f'stroke="{MUTED}" stroke-width="4"/>',
    label(BC600, "CR", 19, 1161, 671, MUTED, anchor="middle"),
    label(MONO700, "9", 29, 1161, 701, GIRDER, anchor="middle"),
]

# Lift bridge centered on the road/river crossing. The long bridge deck spans
# the full water band, while the orange circle and callout identify the site.
bridge_x, bridge_y = 782, 724
parts += [
    f'<g transform="rotate(50 {bridge_x} {bridge_y})">',
    f'<rect x="{bridge_x - 104}" y="{bridge_y - 27}" width="208" height="54" '
    f'fill="{CREAM}" stroke="{GIRDER}" stroke-width="6"/>',
    f'<path d="M {bridge_x - 104} {bridge_y - 9} H {bridge_x + 104} '
    f'M {bridge_x - 104} {bridge_y + 9} H {bridge_x + 104}" '
    f'stroke="{GIRDER}" stroke-width="5"/>',
    f'<path d="M {bridge_x - 72} {bridge_y - 27} L {bridge_x - 38} {bridge_y + 27} '
    f'M {bridge_x - 38} {bridge_y - 27} L {bridge_x - 4} {bridge_y + 27} '
    f'M {bridge_x - 4} {bridge_y - 27} L {bridge_x + 30} {bridge_y + 27} '
    f'M {bridge_x + 30} {bridge_y - 27} L {bridge_x + 64} {bridge_y + 27}" '
    f'stroke="{GIRDER}" stroke-width="4"/>',
    "</g>",
    f'<circle cx="{bridge_x}" cy="{bridge_y}" r="56" fill="none" '
    f'stroke="{STICKER}" stroke-width="6"/>',
    f'<path d="M 824 685 L 995 505" fill="none" stroke="{STICKER}" '
    'stroke-width="4" stroke-linecap="round"/>',
    label(BC700, "OTTER BEND LIFT BRIDGE", 31, 1010, 493, GIRDER, tracking=1),
    label(BC500, "Built 1962  ·  Vertical lift  ·  320 ft", 22, 1010, 528, MUTED),
]

# Title and fictional-place disclaimer.
parts += [
    label(BC700, "SITE LOCATION", 38, 405, 124, GIRDER, tracking=2),
    label(BC600, "Kinnick County Project 27-114", 22, 405, 160, MUTED),
    label(
        B400,
        "Otter Bend, Kinnick County and the Kinnick River are invented for this course.",
        17,
        405,
        191,
        MUTED,
    ),
]

# Minnesota locator inset.
parts += [
    '<rect x="68" y="64" width="294" height="334" fill="#FFFFFF" '
    'stroke="#C7CCD1" stroke-width="3"/>',
    '<path d="M 132 105 L 280 105 L 280 158 L 299 184 L 297 303 '
    'L 254 340 L 215 340 L 207 314 L 152 314 L 132 282 Z" '
    'fill="#E1E5E9" stroke="#AAB2BC" stroke-width="3"/>',
    f'<circle cx="229" cy="250" r="11" fill="{STICKER}"/>',
    f'<circle cx="244" cy="264" r="4" fill="{MUTED}"/>',
    label(B400, "St. Paul", 14, 264, 271, MUTED),
    label(BC600, "MINNESOTA", 18, 215, 380, MUTED, tracking=3, anchor="middle"),
]

# North arrow.
parts += [
    f'<path d="M 1765 92 L 1744 179 L 1765 164 Z" fill="{MUTED}"/>',
    f'<path d="M 1765 92 L 1786 179 L 1765 164 Z" fill="{INK}"/>',
    label(BC700, "N", 23, 1765, 207, INK, anchor="middle"),
]

# Two-mile scale.
scale_x, scale_y = 1498, 1140
parts += [
    label(B400, "0", 15, scale_x, scale_y - 13, INK, anchor="middle"),
    label(B400, "1", 15, scale_x + 145, scale_y - 13, INK, anchor="middle"),
    label(B400, "2", 15, scale_x + 290, scale_y - 13, INK, anchor="middle"),
    f'<rect x="{scale_x}" y="{scale_y}" width="72.5" height="16" fill="{INK}"/>',
    f'<rect x="{scale_x + 72.5}" y="{scale_y}" width="72.5" height="16" '
    f'fill="{CREAM}" stroke="{INK}" stroke-width="2"/>',
    f'<rect x="{scale_x + 145}" y="{scale_y}" width="72.5" height="16" fill="{INK}"/>',
    f'<rect x="{scale_x + 217.5}" y="{scale_y}" width="72.5" height="16" '
    f'fill="{CREAM}" stroke="{INK}" stroke-width="2"/>',
    label(BC600, "MILES", 17, scale_x + 302, scale_y + 15, MUTED),
]

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
    f'viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
)

source_png = HERE / "bridge" / "otter-bend-site-location.png"
published_png = HERE.parent.parent / "teaching-pack" / "06-BRIDGE" / source_png.name
for output in (source_png, published_png):
    output.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(output), output_width=W, output_height=H)
    print(output.relative_to(HERE.parent.parent))
