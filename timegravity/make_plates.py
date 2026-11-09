#!/usr/bin/env python3
"""Draw the Time & Gravity editorial plates as PNG files with the standard library only (no fonts, no text).

  src/research/plates/t00.png  the hub: a worldline across a clock-rate gradient, with a marker for the imagined 'now'
  src/research/plates/t01.png  T.01: the falling worldline the kernel integrates, over the same gradient

The curve in t01.png comes from tools/timegravity_kernel.integrate, so the plate is drawn from the page's own number.
Deterministic; 1280x720 RGB; zlib-compressed PNG written by hand (struct + zlib).
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

W, H = 1280, 720
PLATES = ROOT / "src" / "research" / "plates"

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

    def png(self) -> bytes:
        raw = bytearray()
        stride = W * 3
        for y in range(H):
            raw.append(0)
            raw += self.px[y * stride:(y + 1) * stride].tobytes()

        def chunk(tag: bytes, data: bytes) -> bytes:
            return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

        ihdr = struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0)
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


def main() -> int:
    PLATES.mkdir(parents=True, exist_ok=True)
    for name, fn in (("t00", plate_t00), ("t01", plate_t01), ("t02", plate_t02), ("t03", plate_t03), ("t04", plate_t04), ("t06", plate_t06), ("t07", plate_t07), ("t10", plate_t07_page)):
        data = fn()
        (PLATES / f"{name}.png").write_bytes(data)
        print(f"PASS: wrote plates/{name}.png ({len(data):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
