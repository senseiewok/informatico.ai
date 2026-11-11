#!/usr/bin/env python3
"""Draw the Time & Gravity editorial plates as PNG files with the standard library only (no fonts, no text).

  src/plates/t00.png  the hub: a worldline across a clock-rate gradient, with a marker for the imagined 'now'
  src/plates/t01.png  T.01: the falling worldline the kernel integrates, over the same gradient

The curve in t01.png comes from tools/timegravity_kernel.integrate, so the plate is drawn from the page's own number.
Deterministic; drawn on a 1280x720 RGB canvas, then cropped and box-filtered to 1200x630 (the Open Graph image size
the site's SEO audit expects for PNG plates); zlib-compressed PNG written by hand (struct + zlib).
"""
from __future__ import annotations

import struct
import sys
import zlib
from array import array
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from timegravity_kernel import integrate  # noqa: E402

W, H = 1280, 720          # drawing canvas
OUT_W, OUT_H = 1200, 630  # written plate (Open Graph size); 16 canvas pixels -> 15 plate pixels on both axes
PLATES = ROOT / "src" / "plates"

VELLUM = (247, 248, 249)
STONE = (223, 227, 231)
PRUSSIAN = (21, 53, 86)
MINIUM = (176, 48, 30)
INK = (17, 22, 28)
VERDIGRIS = (24, 92, 75)


class Canvas:
    def __init__(self) -> None:
        self.px = array("B", bytes(W * H * 3))

    def blend(self, x: int, y: int, rgb: tuple[int, int, int], a: float) -> None:
        if a <= 0 or x < 0 or y < 0 or x >= W or y >= H:
            return
        i = (y * W + x) * 3
        for k in range(3):
            self.px[i + k] = int(self.px[i + k] * (1 - a) + rgb[k] * a + 0.5)

    def fill_gradient(self) -> None:
        for y in range(H):
            f = y / (H - 1)
            r = int(VELLUM[0] + (STONE[0] - VELLUM[0]) * f)
            g = int(VELLUM[1] + (STONE[1] - VELLUM[1]) * f)
            b = int(VELLUM[2] + (STONE[2] - VELLUM[2]) * f)
            row = array("B", bytes((r, g, b)) * W)
            self.px[y * W * 3:(y + 1) * W * 3] = row

    def rate_column(self, x0: int, x1: int, y0: int, y1: int) -> None:
        """Darker lower: slower clocks. Alpha grows quadratically with depth, plus faint tick bands."""
        for y in range(y0, y1):
            f = (y - y0) / max(1, (y1 - y0 - 1))
            a = 0.06 + 0.78 * f * f
            band = 0.05 if (y - y0) % 48 < 2 else 0.0
            for x in range(x0, x1):
                edge = min(x - x0, x1 - 1 - x)
                aa = a * (min(1.0, edge / 6.0))
                self.blend(x, y, PRUSSIAN, min(0.92, aa + band))

    def stroke(self, pts: list[tuple[float, float]], rgb: tuple[int, int, int], radius: float, dash: tuple[int, int] | None = None) -> None:
        """Anti-aliased polyline by stamping discs along the path at sub-pixel spacing."""
        r = radius
        n = 0
        for (ax, ay), (bx, by) in zip(pts, pts[1:]):
            seg = max(1, int(((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5 * 2))
            for s in range(seg):
                n += 1
                if dash and (n // (dash[0] * 2)) % 2 == 1:
                    continue
                px = ax + (bx - ax) * s / seg
                py = ay + (by - ay) * s / seg
                for dy in range(int(-r) - 1, int(r) + 2):
                    for dx in range(int(-r) - 1, int(r) + 2):
                        d = ((px - int(px) - dx) ** 2 + (py - int(py) - dy) ** 2) ** 0.5
                        a = max(0.0, min(1.0, r + 0.5 - d))
                        if a > 0:
                            self.blend(int(px) + dx, int(py) + dy, rgb, a * 0.55)

    def disc(self, cx: float, cy: float, radius: float, rgb: tuple[int, int, int], ring: tuple[int, int, int] | None = None) -> None:
        r = radius + 3
        for dy in range(int(-r) - 1, int(r) + 2):
            for dx in range(int(-r) - 1, int(r) + 2):
                d = (dx * dx + dy * dy) ** 0.5
                if ring and radius - 3 <= d <= radius + 1.5:
                    self.blend(int(cx) + dx, int(cy) + dy, ring, max(0.0, min(1.0, 1.5 - abs(d - radius + 0.75))))
                a = max(0.0, min(1.0, radius - 2.5 - d + 0.5)) if ring else max(0.0, min(1.0, radius - d + 0.5))
                if a > 0:
                    self.blend(int(cx) + dx, int(cy) + dy, rgb, a)

    def downscaled(self) -> array:
        """Crop 24 rows top and bottom (1280x672) and box-filter by 15/16 on both axes to OUT_W x OUT_H (1200x630).

        16 source pixels map onto 15 output pixels exactly, so each output pixel is an area average of two or three
        source pixels with weights in fifteenths; separable, integer, deterministic."""
        crop_top = (H - OUT_H * 16 // 15) // 2  # 24
        taps = []
        for o in range(max(OUT_W, OUT_H)):
            lo, hi = o * 16, o * 16 + 16  # span in fifteenths of a source pixel
            s = lo // 15
            pairs = []
            while s * 15 < hi:
                w = min(hi, s * 15 + 15) - max(lo, s * 15)
                pairs.append((s, w))
                s += 1
            taps.append(pairs)
        # horizontal pass: H_crop rows x OUT_W columns, values x16
        h_rows = OUT_H * 16 // 15  # 672
        mid = array("I", [0]) * (h_rows * OUT_W * 3)
        px = self.px
        for y in range(h_rows):
            src = (y + crop_top) * W * 3
            dst = y * OUT_W * 3
            for x in range(OUT_W):
                r = g = b = 0
                for s, w in taps[x]:
                    i = src + s * 3
                    r += px[i] * w
                    g += px[i + 1] * w
                    b += px[i + 2] * w
                j = dst + x * 3
                mid[j], mid[j + 1], mid[j + 2] = r, g, b
        # vertical pass: OUT_H rows, values x256 -> divide
        out = array("B", bytes(OUT_W * OUT_H * 3))
        for y in range(OUT_H):
            dst = y * OUT_W * 3
            for x in range(OUT_W):
                r = g = b = 0
                for s, w in taps[y]:
                    i = s * OUT_W * 3 + x * 3
                    r += mid[i] * w
                    g += mid[i + 1] * w
                    b += mid[i + 2] * w
                j = dst + x * 3
                out[j] = (r + 128) >> 8
                out[j + 1] = (g + 128) >> 8
                out[j + 2] = (b + 128) >> 8
        return out

    def png(self) -> bytes:
        px = self.downscaled()
        raw = bytearray()
        stride = OUT_W * 3
        for y in range(OUT_H):
            raw.append(0)
            raw += px[y * stride:(y + 1) * stride].tobytes()

        def chunk(tag: bytes, data: bytes) -> bytes:
            return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

        ihdr = struct.pack(">IIBBBBB", OUT_W, OUT_H, 8, 2, 0, 0, 0)
        return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b"")


def to_plate_y(z: float) -> float:
    return 72 + (648 - 72) * ((1.0 - z) / (1.0 - (-10.5)))


def frame(c: Canvas) -> None:
    c.fill_gradient()
    c.rate_column(96, 236, 72, 648)
    # axes of the (t, z) diagram
    c.stroke([(320, 72), (320, 648)], INK, 1.2)
    c.stroke([(320, 648), (1200, 648)], INK, 1.2)
    # clocks beside the column at the same heights (0, -3.5, -7.0, -10.0 m) as the SVG stage
    for i, z in enumerate((0.0, -3.5, -7.0, -10.0)):
        cy = to_plate_y(z)
        c.disc(66, cy, 16, VELLUM, ring=INK)
        ang = -1.2 + 0.55 * i
        import math
        c.stroke([(66, cy), (66 + 11 * math.cos(ang), cy + 11 * math.sin(ang))], INK, 1.3)


def plate_t01() -> bytes:
    c = Canvas()
    frame(c)
    res = integrate(True, +1.0, sample_every=250)
    pts = []
    for _tau, t, z in res["samples"]:
        x = 320 + 880 * min(1.0, max(0.0, t / 1.0))
        y = to_plate_y(max(-10.5, min(1.0, z)))
        pts.append((x, min(646.0, y)))
    y_rel = to_plate_y(0.0)
    c.stroke([(320, y_rel), (1200, y_rel)], INK, 1.0, dash=(6, 6))  # release height
    c.stroke(pts, MINIUM, 4.0)
    c.disc(pts[-1][0], pts[-1][1], 11, INK)
    return c.png()


def plate_t00() -> bytes:
    c = Canvas()
    frame(c)
    pts = [(320 + 880 * s, 150 + 300 * s * s * 0.55 + 40 * s) for s in [i / 60 for i in range(61)]]
    c.stroke(pts, MINIUM, 4.0)
    mx, my = pts[33]
    c.disc(mx, my, 13, MINIUM, ring=VELLUM)
    c.disc(mx, my, 5, VELLUM)
    # a faint second worldline with no marker: the physics has the line, not the point
    pts2 = [(320 + 880 * s, 420 + 120 * s * s) for s in [i / 60 for i in range(61)]]
    c.stroke(pts2, VERDIGRIS, 2.5)
    return c.png()


def ring(c: Canvas, cx: float, cy: float, r: float, rgb: tuple[int, int, int], width: float) -> None:
    import math
    pts = [(cx + r * math.cos(a), cy + r * math.sin(a)) for a in [i * 2 * math.pi / 180 for i in range(181)]]
    c.stroke(pts, rgb, width)


def plate_t02() -> bytes:
    """Earth, an orbit, a satellite, and the three clock-budget bars (lengths from the kernel)."""
    from timegravity_kernel import gps_terms
    c = Canvas()
    c.fill_gradient()
    c.rate_column(96, 236, 72, 648)
    c.disc(520, 360, 70, PRUSSIAN, ring=INK)
    ring(c, 520, 360, 230, INK, 1.4)
    c.disc(750, 360, 13, MINIUM, ring=VELLUM)
    terms = gps_terms()
    scale = 7.0
    y = 120
    for val, col in ((terms["grav_us"], VERDIGRIS), (abs(terms["vel_us"]), (156, 69, 20)), (terms["net_us"], PRUSSIAN)):
        c.stroke([(820, y), (820 + val * scale, y)], col, 9.0)
        y += 44
    return c.png()


def plate_t03() -> bytes:
    """Concentric rings around a mass from the Poisson grid solution, and two bodies on one vertical line."""
    from timegravity_kernel import GM_EARTH, G_NEWTON, R_EARTH, poisson_radial
    c = Canvas()
    c.fill_gradient()
    sol = poisson_radial(GM_EARTH / G_NEWTON, R_EARTH, 4.0 * R_EARTH, 400)
    cx, cy, R = 420.0, 360.0, 70.0
    for k in range(1, 8):
        rr = 1.0 + 0.4 * k
        i = min(400, int(round(rr / 4.0 * 400)))
        depth = abs(sol["phi"][i]) / abs(sol["phi"][100])
        ring(c, cx, cy, R * rr, PRUSSIAN, 2.0 + 8.0 * depth)
    c.disc(cx, cy, R, INK)
    c.stroke([(1000, 120), (1000, 600)], INK, 1.0, dash=(6, 6))
    c.disc(1000, 300, 12, MINIUM, ring=VELLUM)
    c.disc(1000, 300, 5, VELLUM)
    c.disc(1000, 300, 19, (0, 0, 0), ring=INK) if False else None
    c.disc(1000, 420, 18, INK, ring=VELLUM)
    return c.png()


def plate_t04() -> bytes:
    """Two arms at different heights with a clock on each, and the visibility curve falling with height difference."""
    from timegravity_kernel_quantum import OMEGA_SR, zych_visibility
    c = Canvas()
    c.fill_gradient()
    c.rate_column(96, 236, 72, 648)
    for y in (220, 500):
        c.stroke([(330, y), (600, y)], INK, 3.0)
        c.disc(465, y, 34, VELLUM, ring=INK)
        c.stroke([(465, y), (465, y - 26)], INK, 2.5)
    c.stroke([(300, 360), (330, 220)], INK, 1.2, dash=(5, 5))
    c.stroke([(300, 360), (330, 500)], INK, 1.2, dash=(5, 5))
    pts = [(700 + 480 * s, 620 - 480 * zych_visibility(10.0 * s, 1.0, OMEGA_SR)) for s in [i / 160 for i in range(161)]]
    c.stroke([(700, 140), (700, 620)], INK, 1.2)
    c.stroke([(700, 620), (1180, 620)], INK, 1.2)
    c.stroke(pts, MINIUM, 4.0)
    c.disc(pts[16][0], pts[16][1], 11, INK)
    return c.png()


def plate_t07() -> bytes:
    """A grid of tiles for the stationary history state and the cos² curve of the conditional probabilities."""
    from timegravity_kernel_quantum import pw_history_state
    import math
    c = Canvas()
    c.fill_gradient()
    st = pw_history_state()
    d = st["d"]
    for cnd in st["conditional"]:
        n = cnd["n"]
        for col, p in ((0, cnd["p_plus_x"]), (1, 1.0 - cnd["p_plus_x"])):
            x0 = 140 + col * 120
            y0 = 90 + n * 34
            for y in range(y0, y0 + 30):
                for x in range(x0, x0 + 110):
                    c.blend(x, y, PRUSSIAN, 0.08 + 0.85 * p)
    pts = [(500 + 640 * s, 600 - 440 * math.cos(st["eps"] * (s * (d - 1)) / 2.0) ** 2) for s in [i / 200 for i in range(201)]]
    c.stroke([(500, 140), (500, 600)], INK, 1.2)
    c.stroke([(500, 600), (1140, 600)], INK, 1.2)
    c.stroke(pts, PRUSSIAN, 3.0)
    for cnd in st["conditional"]:
        x = 500 + 640 * cnd["n"] / (d - 1)
        c.disc(x, 600 - 440 * cnd["p_plus_x"], 8, MINIUM)
    return c.png()


def plate_t06() -> bytes:
    """The model's collapse time falling with mass, and the R0 exclusion bar with two bounds and the parameter-free dot."""
    import math
    from timegravity_kernel_bounds import GS_R0_BOUND_M, GS_R0_PARAMFREE_M, XENONNT_R0_90, dp_collapse_time
    c = Canvas()
    c.fill_gradient()
    pts = []
    for i in range(81):
        lm = -20.0 + 8.0 * i / 80
        lt = max(-6.0, min(12.0, math.log10(dp_collapse_time(10.0 ** lm, 1e-6, 2e-6))))
        pts.append((100 + 460 * i / 80, 620 - 480 * (lt + 6.0) / 18.0))
    c.stroke([(100, 140), (100, 620)], INK, 1.2)
    c.stroke([(100, 620), (560, 620)], INK, 1.2)
    c.stroke(pts, PRUSSIAN, 4.0)
    bx0, bx1, by = 680, 1200, 380
    to_bx = lambda r0: bx0 + (bx1 - bx0) * (math.log10(r0) + 12.0) / 3.0  # noqa: E731
    gs, xe, pf = to_bx(GS_R0_BOUND_M), to_bx(XENONNT_R0_90), to_bx(GS_R0_PARAMFREE_M)
    for y in range(by - 30, by + 30):
        for x in range(bx0, int(gs)):
            c.blend(x, y, MINIUM, 0.18)
        for x in range(int(gs), bx1):
            c.blend(x, y, VERDIGRIS, 0.18)
    c.stroke([(bx0, by), (bx1, by)], INK, 1.5)
    c.stroke([(gs, by - 60), (gs, by + 60)], INK, 4.0)
    c.stroke([(xe, by - 60), (xe, by + 60)], PRUSSIAN, 4.0, dash=(6, 6))
    c.disc(pf, by, 12, MINIUM, ring=VELLUM)
    return c.png()


def plate_t05() -> bytes:
    """Two masses each in two places with the four branch lines, and entanglement against hold time for the three channels:
    the quantum curve, the LOCC flat line and the disputed band between them."""
    import math
    from timegravity_kernel_entangle import BMV_D_M, BMV_DX_M, BMV_M_KG, branch_phases, concurrence_closed, entanglement_phase
    c = Canvas()
    c.fill_gradient()
    # Left: positions along x; A at -dx/2, +dx/2; B at d - dx/2, d + dx/2 (scaled into 110..560).
    span = BMV_D_M + BMV_DX_M
    sx = lambda pos: 110 + 450 * (pos + BMV_DX_M / 2) / span  # noqa: E731
    ya, yb = 240, 480
    ax = (sx(-BMV_DX_M / 2), sx(BMV_DX_M / 2))
    bx = (sx(BMV_D_M - BMV_DX_M / 2), sx(BMV_D_M + BMV_DX_M / 2))
    for i, xa in enumerate(ax):
        for j, xb_ in enumerate(bx):
            c.stroke([(xa, ya), (xb_, yb)], STONE if i == j else PRUSSIAN, 2.4)
    for xa in ax:
        c.disc(xa, ya, 16, PRUSSIAN, ring=VELLUM)
    for xb_ in bx:
        c.disc(xb_, yb, 16, MINIUM, ring=VELLUM)
    # Right: entanglement against hold time 0..30 s.
    x0, x1, y0, y1 = 700, 1200, 120, 600
    tx = lambda t: x0 + (x1 - x0) * t / 30.0  # noqa: E731
    ey = lambda e: y1 - (y1 - y0) * e  # noqa: E731
    pts = []
    for i in range(121):
        t = 30.0 * i / 120
        e = concurrence_closed(entanglement_phase(branch_phases(BMV_M_KG, BMV_D_M, BMV_DX_M, t, "quantum")))
        pts.append((tx(t), ey(e)))
    # Disputed band: hatch between the flat line and the curve.
    for k in range(len(pts) - 1):
        xa, ya_ = pts[k]
        for yy in range(int(ya_), y1):
            if ((int(xa) + yy) // 7) % 2 == 0:
                c.blend(int(xa), yy, PRUSSIAN, 0.10)
    c.stroke([(x0, y0), (x0, y1)], INK, 1.2)
    c.stroke([(x0, y1), (x1, y1)], INK, 1.2)
    c.stroke(pts, PRUSSIAN, 4.0)
    c.stroke([(x0, y1 - 2), (x1, y1 - 2)], VERDIGRIS, 4.0, dash=(8, 8))
    t25 = tx(2.5)
    c.disc(t25, ey(concurrence_closed(entanglement_phase(branch_phases(BMV_M_KG, BMV_D_M, BMV_DX_M, 2.5, "quantum")))), 12, MINIUM, ring=VELLUM)
    return c.png()


def plate_t07_page() -> bytes:
    """Hawking's straight line and Page's hill, with the ten-qubit toy's dots."""
    import math
    from timegravity_kernel_bounds import page_average_entropy, page_curve_toy
    c = Canvas()
    c.fill_gradient()
    toy = page_curve_toy()
    N = toy["n_qubits"]
    ymax = 12.0 * math.log(2.0)
    to_x = lambda a: 140 + 1000 * a / N  # noqa: E731
    to_y = lambda s: 640 - 500 * min(ymax, s) / ymax  # noqa: E731
    c.stroke([(140, 100), (140, 640)], INK, 1.2)
    c.stroke([(140, 640), (1140, 640)], INK, 1.2)
    c.stroke([(to_x(0), to_y(0)), (to_x(N), to_y(N * math.log(2.0)))], (156, 69, 20), 3.0, dash=(8, 8))
    pts = [(to_x(a), to_y(page_average_entropy(2 ** a, 2 ** (N - a)) if 0 < a < N else 0.0)) for a in range(N + 1)]
    smooth = []
    for i in range(len(pts) - 1):
        for s in [k / 10 for k in range(10)]:
            smooth.append((pts[i][0] + (pts[i + 1][0] - pts[i][0]) * s, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * s))
    smooth.append(pts[-1])
    c.stroke(smooth, PRUSSIAN, 4.0)
    for cnd in toy["curve"]:
        c.disc(to_x(cnd["a"]), to_y(cnd["toy_mean_nats"]), 9, MINIUM, ring=VELLUM)
    return c.png()


def plate_t08() -> bytes:
    """Left: Rindler null horizons X = ±cT and accelerated hyperbola. Right: Planck Fock occupation bars and curve."""
    import math
    from timegravity_kernel_horizon import XI_DEFAULT, two_mode_squeezed_wedge
    c = Canvas()
    c.fill_gradient()
    # Left: Rindler wedge diagram centered at (320, 380)
    cx, cy, span = 260.0, 380.0, 220.0
    c.stroke([(cx, cy - span), (cx + span, cy), (cx, cy + span)], INK, 1.5, dash=(6, 6))
    c.stroke([(cx, cy), (cx + span, cy - span)], MINIUM, 3.0)
    c.stroke([(cx, cy), (cx + span, cy + span)], MINIUM, 3.0)
    hyp = []
    for i in range(81):
        eta = -1.1 + 2.2 * i / 80.0
        x = cx + 95.0 * math.cosh(eta)
        y = cy - 95.0 * math.sinh(eta)
        hyp.append((x, y))
    c.stroke(hyp, PRUSSIAN, 4.0)
    c.disc(cx + 95.0, cy, 10, PRUSSIAN, ring=VELLUM)
    c.disc(cx - 55.0, cy, 10, STONE, ring=INK)
    # Right: Fock occupation probabilities p_n from the Jacobi partial-trace kernel
    wedge = two_mode_squeezed_wedge(XI_DEFAULT, 8)
    x0, x1, y0, y1 = 640, 1180, 140, 620
    c.stroke([(x0, y0), (x0, y1)], INK, 1.2)
    c.stroke([(x0, y1), (x1, y1)], INK, 1.2)
    bw = 44
    for n, p in enumerate(wedge["eigenvalues"][:8]):
        bx = x0 + 24 + n * 64
        bh = int(round((y1 - y0 - 20) * p))
        for yy in range(y1 - bh, y1):
            for xx in range(bx, bx + bw):
                c.blend(xx, yy, PRUSSIAN, 0.72)
        c.disc(bx + bw // 2, y1 - bh, 7, MINIUM, ring=VELLUM)
    return c.png()


def plate_t09() -> bytes:
    """Left: Kerr damped ringdown waveform h(t) for (2,2,0) and (2,2,1). Right: (f, tau) spin trajectory."""
    import math
    from timegravity_kernel_kerr import FIDUCIAL_MASS_SOLAR, KERR_SPINS, physical_ringdown, solve_kerr_qnm_branch
    c = Canvas()
    c.fill_gradient()
    b0 = {r["chi"]: r for r in solve_kerr_qnm_branch(KERR_SPINS, overtone_n=0)}
    b1 = {r["chi"]: r for r in solve_kerr_qnm_branch(KERR_SPINS, overtone_n=1)}
    r220 = b0[0.68]
    r221 = b1[0.68]
    # Left: damped sinusoid over t / M in [0, 60]
    lx0, lx1, lyc = 110, 610, 380
    c.stroke([(lx0, lyc), (lx1, lyc)], INK, 1.0, dash=(5, 5))
    wave0, wave1 = [], []
    for i in range(181):
        tm = 60.0 * i / 180.0
        x = lx0 + (lx1 - lx0) * (i / 180.0)
        y0_ = lyc - 180.0 * math.exp(r220["mw_im"] * tm) * math.cos(r220["mw_re"] * tm)
        y1_ = lyc - 140.0 * math.exp(r221["mw_im"] * tm) * math.cos(r221["mw_re"] * tm)
        wave0.append((x, y0_))
        wave1.append((x, y1_))
    c.stroke(wave1, VERDIGRIS, 2.5)
    c.stroke(wave0, PRUSSIAN, 4.0)
    # Right: (f_Hz, tau_ms) trajectory across chi in KERR_SPINS for 62 M_sun
    rx0, rx1, ry0, ry1 = 700, 1180, 140, 620
    c.stroke([(rx0, ry0), (rx0, ry1)], INK, 1.2)
    c.stroke([(rx0, ry1), (rx1, ry1)], INK, 1.2)
    fx = lambda f: rx0 + (rx1 - rx0) * (f - 180.0) / 220.0  # noqa: E731
    ty = lambda tau: ry1 - (ry1 - ry0) * (tau - 0.8) / 4.5  # noqa: E731
    pts0, pts1 = [], []
    for chi in KERR_SPINS:
        p0 = physical_ringdown(FIDUCIAL_MASS_SOLAR, b0[chi]["mw_re"], b0[chi]["mw_im"])
        p1 = physical_ringdown(FIDUCIAL_MASS_SOLAR, b1[chi]["mw_re"], b1[chi]["mw_im"])
        pts0.append((fx(p0["f_hz"]), ty(p0["tau_ms"])))
        pts1.append((fx(p1["f_hz"]), ty(p1["tau_ms"])))
    c.stroke(pts0, PRUSSIAN, 3.5)
    c.stroke(pts1, VERDIGRIS, 2.5, dash=(6, 6))
    for i, (px, py) in enumerate(pts0):
        c.disc(px, py, 10 if KERR_SPINS[i] == 0.68 else 6, MINIUM if KERR_SPINS[i] == 0.68 else PRUSSIAN, ring=VELLUM)
    return c.png()


def plate_t11() -> bytes:
    """Left: pointer state radial photon broadcast to N=6 modes. Right: Quantum Darwinism I(S:E_k) plateau vs coherence decay."""
    import math
    from timegravity_kernel_einselection import N_ENV_DEFAULT, THETA_DEFAULT, statevector_quantum_darwinism
    c = Canvas()
    c.fill_gradient()
    qd = statevector_quantum_darwinism(THETA_DEFAULT, N_ENV_DEFAULT, planted_defect=False)
    # Left: central pointer qubit S broadcasting radial wave-fronts to 6 environment observer nodes
    cx, cy, r_ring = 310.0, 380.0, 175.0
    for rad in (55, 95, 135, 175):
        ring_pts = [(cx + rad * math.cos(2 * math.pi * j / 72), cy + rad * math.sin(2 * math.pi * j / 72)) for j in range(73)]
        c.stroke(ring_pts, STONE, 1.5)
    for m in range(N_ENV_DEFAULT):
        ang = -math.pi / 2 + 2.0 * math.pi * m / N_ENV_DEFAULT
        ox, oy = cx + r_ring * math.cos(ang), cy + r_ring * math.sin(ang)
        c.stroke([(cx, cy), (ox, oy)], PRUSSIAN if m < 2 else VERDIGRIS, 2.8 if m < 2 else 1.8, dash=None if m < 2 else (6, 6))
        c.disc(ox, oy, 11 if m < 2 else 8, MINIUM if m < 2 else PRUSSIAN, ring=VELLUM)
    c.disc(cx, cy, 16, PRUSSIAN, ring=VELLUM)
    # Right: mutual information I(S:E_k) in bits (0 to 2 bits) and off-diagonal coherence gamma^k
    rx0, rx1, ry0, ry1 = 620, 1170, 130, 620
    c.stroke([(rx0, ry0), (rx0, ry1)], INK, 1.2)
    c.stroke([(rx0, ry1), (rx1, ry1)], INK, 1.2)
    # Classical 1-bit plateau line
    y_one_bit = ry1 - (ry1 - ry0) * 0.5
    c.stroke([(rx0, y_one_bit), (rx1, y_one_bit)], INK, 1.2, dash=(6, 6))
    tx = lambda k: rx0 + (rx1 - rx0) * (k / N_ENV_DEFAULT)  # noqa: E731
    ty_mi = lambda bits: ry1 - (ry1 - ry0) * min(2.0, max(0.0, bits)) / 2.0  # noqa: E731
    ty_coh = lambda coh: ry1 - (ry1 - ry0) * min(1.0, max(0.0, coh)) * 0.5  # noqa: E731
    mi_pts = [(tx(row["k"]), ty_mi(row["i_s_ek_jacobi_bits"])) for row in qd["fragments"]]
    coh_pts = [(tx(k), ty_coh(qd["gamma"] ** k)) for k in range(N_ENV_DEFAULT + 1)]
    c.stroke(coh_pts, MINIUM, 3.0, dash=(7, 7))
    c.stroke(mi_pts, PRUSSIAN, 4.2)
    for x, y in mi_pts:
        c.disc(x, y, 9, PRUSSIAN, ring=VELLUM)
    return c.png()


def plate_t12() -> bytes:
    """Left: EM-transparent mass flyby past two clocks across baseline d_c. Right: differential redshift pulse and arsinh step."""
    import math
    from timegravity_kernel_dark_clock import dark_transit_clock_shift
    c = Canvas()
    c.fill_gradient()
    tr = dark_transit_clock_shift()
    # Left: two clocks separated by baseline d_c and gravitational potential contours of passing dark mass
    c1x, c1y = 260.0, 270.0
    c2x, c2y = 260.0, 510.0
    dmx, dmy = 420.0, 270.0
    c.stroke([(c1x, c1y), (c2x, c2y)], INK, 2.0, dash=(6, 6))
    c.stroke([(dmx, 120.0), (dmx, 620.0)], MINIUM, 3.2)
    for rad in (48, 92, 145, 210):
        ring_pts = [(dmx + rad * math.cos(2 * math.pi * j / 72), dmy + rad * math.sin(2 * math.pi * j / 72)) for j in range(73)]
        c.stroke(ring_pts, PRUSSIAN, 1.4, dash=(5, 5))
    c.disc(c1x, c1y, 13, PRUSSIAN, ring=VELLUM)
    c.disc(c2x, c2y, 13, VERDIGRIS, ring=VELLUM)
    c.disc(dmx, dmy, 15, MINIUM, ring=VELLUM)
    # Right: instantaneous differential redshift pulse and integrated proper-time step arsinh curve
    rx0, rx1, ry0, ry1 = 620, 1170, 130, 620
    ry_mid = 0.5 * (ry0 + ry1)
    c.stroke([(rx0, ry0), (rx0, ry1)], INK, 1.2)
    c.stroke([(rx0, ry_mid), (rx1, ry_mid)], INK, 1.1, dash=(6, 6))
    prof = tr["profile"]
    min_df = min(p["delta_nu_over_nu"] for p in prof) or -1.0
    pulse_pts = []
    step_pts = []
    max_asinh = math.asinh(5.0)
    for p in prof:
        u = p["vt_over_b1"]
        x = rx0 + (rx1 - rx0) * ((u + 5.0) / 10.0)
        y_pulse = ry_mid + 200.0 * (p["delta_nu_over_nu"] / abs(min_df))
        y_step = ry_mid + 180.0 * (math.asinh(u) / max_asinh)
        pulse_pts.append((x, y_pulse))
        step_pts.append((x, y_step))
    c.stroke(pulse_pts, PRUSSIAN, 4.0)
    c.stroke(step_pts, MINIUM, 3.2)
    for x, y in pulse_pts[::4]:
        c.disc(x, y, 7, PRUSSIAN, ring=VELLUM)
    return c.png()


def main() -> int:
    PLATES.mkdir(parents=True, exist_ok=True)
    for name, fn in (("t00", plate_t00), ("t01", plate_t01), ("t02", plate_t02), ("t03", plate_t03), ("t04", plate_t04), ("t05", plate_t05), ("t06", plate_t06), ("t07", plate_t07), ("t08", plate_t08), ("t09", plate_t09), ("t10", plate_t07_page), ("t11", plate_t11), ("t12", plate_t12)):
        data = fn()
        (PLATES / f"{name}.png").write_bytes(data)
        print(f"PASS: wrote plates/{name}.png ({len(data):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
