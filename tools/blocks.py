"""Isometric block clusters from the brand cover generator, written as standalone SVGs."""
import math, os

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = 64
C, Sn = math.cos(math.radians(30)) * S, math.sin(math.radians(30)) * S
INK = "#161514"
ORANGE = {"top": "#F47B3D", "l": "#EE6B2D", "r": "#E25E22"}
CREAM = {"top": "#F3F1E6", "l": "#E4E1D2", "r": "#D9D5C3"}

def proj(ox, oy, i, j, z):
    return (ox + (i - j) * C, oy + (i + j) * Sn - z * S)

def poly(pts, fill):
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polygon points="{d}" fill="{fill}"/>'

def hatch(a, b, d, n):
    out = []
    for k in range(1, n):
        t = k / n
        x1, y1 = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
        x2, y2 = d[0] + (b[0] - a[0]) * t, d[1] + (b[1] - a[1]) * t
        out.append(f"M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}")
    return f'<path class="h" d="{"".join(out)}"/>'

def box(ox, oy, i, j, h, pal):
    P = lambda a, b, z: proj(ox, oy, a, b, z)
    i2, j2 = i + 1, j + 1
    top = [P(i, j, h), P(i2, j, h), P(i2, j2, h), P(i, j2, h)]
    right = [P(i2, j, 0), P(i2, j2, 0), P(i2, j2, h), P(i2, j, h)]
    left = [P(i, j2, 0), P(i2, j2, 0), P(i2, j2, h), P(i, j2, h)]
    nl = lambda length: max(3, int(length * S / 11))
    g = [poly(right, pal["r"]), hatch(right[0], right[1], right[3], nl(1)),
         poly(left, pal["l"]), hatch(left[0], left[1], left[3], nl(1)),
         poly(top, pal["top"]), hatch(top[0], top[3], top[1], nl(1))]
    return "".join(g)

def svg(name, heights, cream):
    cells = sorted(heights.items(), key=lambda c: (c[0][0] + c[0][1], c[0][0]))
    ox, oy = 0, 0
    body = "".join(box(ox, oy, i, j, h, CREAM if (i, j) in cream else ORANGE) for (i, j), h in cells)
    pts = [proj(ox, oy, i + a, j + b, z) for (i, j), h in heights.items()
           for a in (0, 1) for b in (0, 1) for z in (0, h)]
    pad = 6
    x0, y0 = min(p[0] for p in pts) - pad, min(p[1] for p in pts) - pad
    w, hgt = max(p[0] for p in pts) - x0 + pad, max(p[1] for p in pts) - y0 + pad
    out = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} {w:.0f} {hgt:.0f}">'
           f'<style>polygon{{stroke:{INK};stroke-width:4.5;stroke-linejoin:round}}'
           f'.h{{stroke:{INK};stroke-width:1.7;stroke-opacity:.55;stroke-linecap:round;fill:none}}</style>'
           f"{body}</svg>")
    open(f"{SITE}/img/{name}.svg", "w", encoding="utf-8").write(out)

svg("blocks-right", {
    (0, 0): 4.2, (1, 0): 3.0, (2, 0): 5.6, (3, 0): 2.2,
    (0, 1): 2.6, (1, 1): 1.6, (2, 1): 3.4, (3, 1): 1.0,
    (0, 2): 1.4, (1, 2): 0.8, (2, 2): 2.0,
    (0, 3): 0.6, (1, 3): 0.35,
    (4, 0): 3.8, (4, 1): 2.4, (3, 2): 1.2, (2, 3): 0.6,
    (5, 0): 1.8, (5, 1): 1.0,
}, {(1, 1), (3, 0), (0, 3), (4, 1), (2, 3)})
svg("blocks-left", {(0, 0): 1.6, (1, 0): 2.6, (0, 1): 0.9, (2, 0): 1.1, (1, 1): 0.5, (0, 2): 0.3},
    {(0, 1), (2, 0)})
print("blocks ok")
