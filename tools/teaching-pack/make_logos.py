"""Generate the ACMEJOB.Ai logo family as SVG. All artwork is original."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

OUT = os.path.join(ROOT, "kit", "logo")
os.makedirs(OUT, exist_ok=True)


def wordmark(ink=GIRDER, accent=STICKER, sticker_ink=WHITE, sticker_edge=WHITE,
             tagline=True, tag_ink=None, x=0, y=0):
    """ACMEJOB + .Ai sticker. Baseline of ACMEJOB sits at y. Returns (svg, width)."""
    size = 76
    tr = 1.2
    word = "ACMEJOB"
    wm_w = text_width(BC700, word, size, tr)
    parts = [text_path(BC700, word, size, x, y, ink, tracking=tr)]
    st, st_w = ai_sticker(x + wm_w + 8, y - size * 0.70, size * 0.62,
                          fill=accent, ink=sticker_ink, edge=sticker_edge)
    parts.append(st)
    total = wm_w + 8 + st_w + 6
    if tagline:
        tag = "ENGINEERING  ·  EST. 1967"
        parts.append(text_path(BC500, tag, 17.5, x + 2, y + 24, tag_ink or ink, tracking=2.2))
    return "\n".join(parts), total


def primary(dark=False):
    ink = WHITE if dark else GIRDER
    bg = REBAR if dark else None
    mark = bridge_mark(8, 10, 0.86, stroke=ink, accent=STICKER,
                       water=RIVER if not dark else RIVER)
    wm, wmw = wordmark(ink=ink, tag_ink=RIVER if dark else "#5A6B80",
                       sticker_edge=REBAR if dark else WHITE, x=132, y=86)
    w = 132 + wmw + 16
    return svg(round(w), 128, mark + wm, bg=bg)


def horizontal_small():
    """Compact lockup for document headers: mark + ACMEJOB.Ai, no tagline."""
    ink = GIRDER
    mark = bridge_mark(0, 2, 0.42, stroke=ink, accent=STICKER, water=RIVER)
    size = 34
    wm_w = text_width(BC700, "ACMEJOB", size, 0.6)
    parts = [mark, text_path(BC700, "ACMEJOB", size, 58, 40, ink, tracking=0.6)]
    st, st_w = ai_sticker(58 + wm_w + 4, 40 - size * 0.70, size * 0.62)
    parts.append(st)
    return svg(round(58 + wm_w + 4 + st_w + 4), 56, "\n".join(parts))


def mark_only(dark=False):
    ink = WHITE if dark else GIRDER
    return svg(120, 120, bridge_mark(0, 0, 1.0, stroke=ink, accent=STICKER, water=RIVER),
               bg=REBAR if dark else None)


def stacked():
    wm, wmw = wordmark(x=0, y=150)
    W = max(wmw + 24, 230)
    mark_w = 120 * 0.78
    mark = bridge_mark((W - mark_w) / 2, 4, 0.78, stroke=GIRDER, accent=STICKER, water=RIVER)
    body = f'<g>{mark}</g><g transform="translate({(W-wmw)/2:.1f},0)">{wm}</g>'
    return svg(round(W), 190, body)


def foreman_mark(dark=False):
    """FOREMAN's own logo: the sparkle inside a hard hat. Deliberately over-designed."""
    ink = WHITE if dark else REBAR
    g = []
    # hard hat: wide brim, low dome, two ridges
    g.append(f'<path d="M26 60 a22 22 0 0 1 44 0 Z" fill="{STICKER}"/>')
    g.append(f'<path d="M10 60 h76 a4 4 0 0 1 0 8 H10 a4 4 0 0 1 0 -8 Z" fill="{STICKER}"/>')
    g.append(f'<path d="M40 41 v19 M56 41 v19" stroke="{WHITE if not dark else REBAR}" '
             f'stroke-width="2.5" stroke-linecap="round" opacity="0.45"/>')
    # sparkle sitting on the hat, because of course it does
    cx, cy, r, q = 48, 26, 12, 2.9
    g.append(f'<path d="M{cx} {cy-r} Q{cx+q} {cy-q} {cx+r} {cy} Q{cx+q} {cy+q} {cx} {cy+r} '
             f'Q{cx-q} {cy+q} {cx-r} {cy} Q{cx-q} {cy-q} {cx} {cy-r} Z" fill="{STICKER}"/>')
    g.append(text_path(BC700, "FOREMAN", 26, 48, 94, ink, tracking=2.6, anchor="middle"))
    g.append(text_path(MONO500, "v4.2", 12, 48, 110, RIVER, tracking=0.6, anchor="middle"))
    return svg(96, 120, "\n".join(g), bg=REBAR if dark else None)


def favicon():
    body = f'<rect width="120" height="120" rx="20" fill="{GIRDER}"/>'
    body += bridge_mark(0, 4, 1.0, stroke=WHITE, accent=STICKER, water=RIVER)
    return svg(120, 120, body)


def county_seal():
    """Kinnick County seal, for county-side documents. Plain, municipal, no AI anything."""
    g = [f'<circle cx="60" cy="60" r="57" fill="none" stroke="{RUST}" stroke-width="2.5"/>',
         f'<circle cx="60" cy="60" r="51" fill="none" stroke="{RUST}" stroke-width="1"/>']
    # lift bridge: two towers, raised span between them, river below
    g.append(f'<g fill="none" stroke="{RUST}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">')
    g.append('<path d="M38 74 V46 M50 74 V46 M38 46 h12 M38 60 h12"/>')     # left tower
    g.append('<path d="M70 74 V46 M82 74 V46 M70 46 h12 M70 60 h12"/>')     # right tower
    g.append('<path d="M50 56 h20 M52 50 h16 M50 56 L52 50 M70 56 L68 50"/>')  # raised span
    g.append('<path d="M28 74 h10 M82 74 h10"/>')                            # approaches
    g.append(f'<path d="M26 84 q6 -4 12 0 t12 0 t12 0 t12 0 t12 0 t12 0" stroke-width="2"/>')
    g.append('</g>')
    g.append(text_path(BC600, "KINNICK COUNTY", 11, 60, 33, RUST, tracking=1.2, anchor="middle"))
    g.append(text_path(BC500, "MINNESOTA", 8.5, 60, 100, RUST, tracking=2.2, anchor="middle"))
    return svg(120, 120, "\n".join(g))


def foreman_wide():
    """Horizontal FOREMAN lockup for document headers."""
    g = []
    g.append(f'<path d="M14 30 a16 16 0 0 1 32 0 Z" fill="{STICKER}"/>')
    g.append(f'<path d="M2 30 h56 a3 3 0 0 1 0 6 H2 a3 3 0 0 1 0 -6 Z" fill="{STICKER}"/>')
    cx, cy, r, q = 30, 9, 8, 1.9
    g.append(f'<path d="M{cx} {cy-r} Q{cx+q} {cy-q} {cx+r} {cy} Q{cx+q} {cy+q} {cx} {cy+r} '
             f'Q{cx-q} {cy+q} {cx-r} {cy} Q{cx-q} {cy-q} {cx} {cy-r} Z" fill="{STICKER}"/>')
    fw = text_width(BC700, "FOREMAN", 30, 2.0)
    g.append(text_path(BC700, "FOREMAN", 30, 72, 32, REBAR, tracking=2.0))
    vx = 72 + fw + 10
    g.append(text_path(MONO500, "v4.2", 12, vx, 32, RIVER))
    w = vx + text_width(MONO500, "v4.2", 12) + 8
    return svg(round(w), 44, "\n".join(g))


files = {
    "foreman-mark-wide.svg": foreman_wide(),
    "acmejob-logo-primary.svg": primary(False),
    "acmejob-logo-primary-dark.svg": primary(True),
    "acmejob-logo-horizontal.svg": horizontal_small(),
    "acmejob-logo-stacked.svg": stacked(),
    "acmejob-mark.svg": mark_only(False),
    "acmejob-mark-dark.svg": mark_only(True),
    "acmejob-favicon.svg": favicon(),
    "foreman-mark.svg": foreman_mark(False),
    "foreman-mark-dark.svg": foreman_mark(True),
    "kinnick-county-seal.svg": county_seal(),
}
for name, data in files.items():
    open(os.path.join(OUT, name), "w").write(data)
    print(name, len(data))
