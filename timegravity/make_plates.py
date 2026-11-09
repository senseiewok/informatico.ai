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


def frame(c: Canvas) -> None:
    c.fill_gradient()
    c.rate_column(96, 236, 72, 648)
    # axes of the (t, z) diagram
    c.stroke([(320, 72), (320, 648)], INK, 1.2)
    c.stroke([(320, 648), (1200, 648)], INK, 1.2)
    # clocks beside the column: hands at the same angle would be "same rate"; we draw the slow ones lagging
    for i, cy in enumerate((120, 260, 400, 540)):
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
        x = 320 + 880 * (t / 1.0)
        y = 120 + (648 - 120) * (max(0.0, -z) / 5.6)
        pts.append((x, min(646.0, y)))
    c.stroke([(320, 120), (1200, 120)], INK, 1.0, dash=(6, 6))  # release height
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


def main() -> int:
    PLATES.mkdir(parents=True, exist_ok=True)
    for name, fn in (("t00", plate_t00), ("t01", plate_t01)):
        data = fn()
        (PLATES / f"{name}.png").write_bytes(data)
        print(f"PASS: wrote plates/{name}.png ({len(data):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
