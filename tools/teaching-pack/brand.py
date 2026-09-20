"""ACMEJOB.Ai brand constants and SVG helpers. Everything is original artwork."""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(ROOT, "fonts")
if not os.path.exists(os.path.join(FONTS, "barlow-latin-400-normal.ttf")):
    FONTS = os.path.join(ROOT, "fonts", "ttf")   # dev tree layout

# Palette (names are part of the joke; hex values are the contract)
GIRDER = "#1F3A5F"    # Girder Blue, primary
STICKER = "#F26B1D"   # Sticker Orange, the ".Ai"
REBAR = "#2B2F36"     # Rebar Charcoal, text
CONCRETE = "#E6E8EA"  # Cured Concrete, light neutral
RUST = "#9C4A2F"      # Deferred Maintenance Rust, secondary
HILITE = "#F2C230"    # Diane's Highlighter
WHITE = "#FFFFFF"
RIVER = "#6F8FAF"     # Kinnick River, tint of primary

_font_cache = {}


def font(name):
    if name not in _font_cache:
        _font_cache[name] = TTFont(os.path.join(FONTS, name + ".ttf"))
    return _font_cache[name]


BC700 = "barlow-condensed-latin-700-normal"
BC600 = "barlow-condensed-latin-600-normal"
BC500 = "barlow-condensed-latin-500-normal"
B400 = "barlow-latin-400-normal"
B600 = "barlow-latin-600-normal"
CAV700 = "caveat-latin-700-normal"
MONO500 = "ibm-plex-mono-latin-500-normal"
MONO700 = "ibm-plex-mono-latin-700-normal"


def text_width(fname, text, size, tracking=0.0):
    f = font(fname)
    upm = f["head"].unitsPerEm
    cmap = f.getBestCmap()
    hmtx = f["hmtx"]
    w = 0.0
    for ch in text:
        g = cmap.get(ord(ch))
        if g is None:
            g = ".notdef"
        w += hmtx[g][0] * size / upm + tracking
    return w - tracking if text else 0.0


def text_path(fname, text, size, x, y, fill, tracking=0.0, anchor="start", extra=""):
    """Return an SVG <path> with the text converted to outlines (no font needed to view)."""
    f = font(fname)
    upm = f["head"].unitsPerEm
    cmap = f.getBestCmap()
    gs = f.getGlyphSet()
    hmtx = f["hmtx"]
    s = size / upm
    total = text_width(fname, text, size, tracking)
    if anchor == "middle":
        x -= total / 2
    elif anchor == "end":
        x -= total
    d = []
    cx = x
    for ch in text:
        g = cmap.get(ord(ch)) or ".notdef"
        pen = SVGPathPen(gs)
        tp = TransformPen(pen, (s, 0, 0, -s, cx, y))
        gs[g].draw(tp)
        cmds = pen.getCommands()
        if cmds:
            d.append(cmds)
        cx += hmtx[g][0] * s + tracking
    return f'<path d="{" ".join(d)}" fill="{fill}" {extra}/>'


def bridge_mark(x=0, y=0, scale=1.0, stroke=GIRDER, accent=STICKER, water=None, sparkle=True):
    """Vertical lift bridge, span raised. Drawn on a 120 x 120 grid."""
    water = water or stroke
    sw = 5
    p = []
    p.append(f'<g transform="translate({x},{y}) scale({scale})" fill="none" stroke="{stroke}" '
             f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">')
    # towers
    for tx in (16, 86):
        p.append(f'<rect x="{tx}" y="18" width="18" height="80"/>')
        # bracing
        for yy in (18, 45, 72):
            h = 27 if yy < 72 else 26
            p.append(f'<path d="M{tx} {yy} L{tx+18} {yy+h} M{tx+18} {yy} L{tx} {yy+h}" stroke-width="3"/>')
        # sheave housing
        p.append(f'<rect x="{tx-4}" y="8" width="26" height="10" fill="{stroke}"/>')
    # approach roadway
    p.append('<path d="M2 84 L16 84 M104 84 L118 84"/>')
    # lifted span (truss)
    p.append('<path d="M34 58 L86 58 M38 44 L82 44 M34 58 L38 44 M86 58 L82 44"/>')
    p.append('<path d="M38 44 L47 58 L56 44 L65 58 L73 44 L82 58" stroke-width="3"/>')
    # hoist ropes
    p.append('<path d="M38 18 L38 44 M82 18 L82 44" stroke-width="2.5"/>')
    # water
    p.append(f'<path d="M6 108 q7 -6 14 0 t14 0 t14 0 t14 0 t14 0 t14 0 t14 0 t14 0" stroke="{water}" stroke-width="3.5"/>')
    if sparkle:
        # the obligatory AI sparkle, bolted on above the span
        cx, cy, r, q = 60, 27, 11, 2.6
        p.append(f'<path d="M{cx} {cy-r} Q{cx+q} {cy-q} {cx+r} {cy} Q{cx+q} {cy+q} {cx} {cy+r} '
                 f'Q{cx-q} {cy+q} {cx-r} {cy} Q{cx-q} {cy-q} {cx} {cy-r} Z" fill="{accent}" stroke="none"/>')
    p.append('</g>')
    return "\n".join(p)


def ai_sticker(x, y, h, fill=STICKER, ink=WHITE, edge=WHITE, shadow="#00000033", rot=-7):
    """The '.Ai' that was added two years ago. Deliberately a sticker. x,y = top-left before rotation."""
    size = h * 0.92
    tw = text_width(CAV700, ".Ai", size)
    w = tw + h * 0.62
    cx, cy = x + w / 2, y + h / 2
    out = [f'<g transform="rotate({rot} {cx:.1f} {cy:.1f})">']
    out.append(f'<rect x="{x+2:.1f}" y="{y+3:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{h*0.2:.1f}" fill="{shadow}"/>')
    out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{h*0.2:.1f}" fill="{fill}" stroke="{edge}" stroke-width="{h*0.07:.1f}"/>')
    out.append(text_path(CAV700, ".Ai", size, x + h * 0.26, y + h * 0.76, ink))
    out.append('</g>')
    return "\n".join(out), w


def svg(w, h, body, bg=None):
    r = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'{r}{body}</svg>')
