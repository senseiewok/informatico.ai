#!/usr/bin/env python3
"""Build the Informatico.ai Cross-Scale Featured Essays (/essays/ and /es-mx/essays/) + deterministic PNG plates.

Keeps the 48 Pillar Folios (E.01–M.12), 6 Bounties, 6 Toolboxes, and 13 Time & Gravity pages (T.00–T.12) untouched as
their own core tracks while publishing standalone long-form synthesis essays under /essays/<slug>/ (with static Spanish
twins under /es-mx/essays/<slug>/, live interactive SVG observatories, SKILL.md companions, and Python verifiers).
"""
from __future__ import annotations

import hashlib
import html
import json
import math
import struct
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_longform_folios as B  # noqa: E402
from folios.seo_copy import BRAND, PILLAR_SEO  # noqa: E402

RESEARCH = ROOT / "src"
PLATES_DIR = RESEARCH / "plates"

BOUNDARY_BANNER_EN = (
    "Research and physics education, not clinical advice. Cross-scale examples compare mathematical and physical laws "
    "across vacuum traps, clocks, civil materials, and biomolecules; nothing here is a treatment claim or clinical guidance."
)
BOUNDARY_BANNER_ES = (
    "Investigación y divulgación física, no orientación clínica. Los ejemplos entre escalas comparan leyes matemáticas y "
    "físicas entre trampas de vacío, relojes, materiales civiles y biomoléculas; nada aquí constituye consejo ni promesa clínica."
)


def a(s: str) -> str:
    return html.escape(str(s), quote=True)


def t(s: str) -> str:
    return html.escape(str(s), quote=False)


def bi(tag: str, en: str, es: str, cls: str = "", extra: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    x = f" {extra}" if extra else ""
    return f'<{tag}{c}{x} data-en="{a(en)}" data-es="{a(es)}">{t(en)}</{tag}>'


# ---------------------------------------------------------------------------
# Pure-stdlib deterministic 1200x630 PNG plate renderer (zero baked-in text)
# ---------------------------------------------------------------------------

def _make_canvas(w: int, h: int, bg: tuple[int, int, int]) -> bytearray:
    row = bytes(bg) * w
    return bytearray(row * h)


def _blend(buf: bytearray, w: int, h: int, x: int, y: int, col: tuple[int, int, int], alpha: float) -> None:
    if x < 0 or x >= w or y < 0 or y >= h or alpha <= 0.0:
        return
    if alpha >= 1.0:
        idx = (y * w + x) * 3
        buf[idx] = col[0]
        buf[idx + 1] = col[1]
        buf[idx + 2] = col[2]
        return
    idx = (y * w + x) * 3
    inv = 1.0 - alpha
    buf[idx] = int(buf[idx] * inv + col[0] * alpha)
    buf[idx + 1] = int(buf[idx + 1] * inv + col[1] * alpha)
    buf[idx + 2] = int(buf[idx + 2] * inv + col[2] * alpha)


def _fill_rect(buf: bytearray, w: int, h: int, x0: int, y0: int, x1: int, y1: int, col: tuple[int, int, int], alpha: float = 1.0) -> None:
    xa, xb = max(0, x0), min(w, x1)
    ya, yb = max(0, y0), min(h, y1)
    for y in range(ya, yb):
        for x in range(xa, xb):
            _blend(buf, w, h, x, y, col, alpha)


def _draw_disc(buf: bytearray, w: int, h: int, cx: float, cy: float, r: float, col: tuple[int, int, int], alpha: float = 1.0) -> None:
    x0, x1 = max(0, int(cx - r - 2)), min(w, int(cx + r + 3))
    y0, y1 = max(0, int(cy - r - 2)), min(h, int(cy + r + 3))
    for y in range(y0, y1):
        for x in range(x0, x1):
            d = math.hypot(x - cx, y - cy)
            if d <= r - 0.6:
                _blend(buf, w, h, x, y, col, alpha)
            elif d <= r + 0.6:
                _blend(buf, w, h, x, y, col, alpha * (r + 0.6 - d) / 1.2)


def _draw_ring(buf: bytearray, w: int, h: int, cx: float, cy: float, r: float, stroke: float, col: tuple[int, int, int], alpha: float = 1.0) -> None:
    half = stroke * 0.5
    x0, x1 = max(0, int(cx - r - half - 2)), min(w, int(cx + r + half + 3))
    y0, y1 = max(0, int(cy - r - half - 2)), min(h, int(cy + r + half + 3))
    for y in range(y0, y1):
        for x in range(x0, x1):
            d = abs(math.hypot(x - cx, y - cy) - r)
            if d <= half - 0.5:
                _blend(buf, w, h, x, y, col, alpha)
            elif d <= half + 0.7:
                _blend(buf, w, h, x, y, col, alpha * (half + 0.7 - d) / 1.2)


def _draw_line(buf: bytearray, w: int, h: int, x0: float, y0: float, x1: float, y1: float, stroke: float, col: tuple[int, int, int], alpha: float = 1.0) -> None:
    steps = max(2, int(math.hypot(x1 - x0, y1 - y0) * 1.5))
    r = max(0.6, stroke * 0.5)
    for i in range(steps + 1):
        u = i / steps
        _draw_disc(buf, w, h, x0 + (x1 - x0) * u, y0 + (y1 - y0) * u, r, col, alpha)


def _encode_png(w: int, h: int, buf: bytearray) -> bytes:
    raw = bytearray()
    stride = w * 3
    for y in range(h):
        raw.append(0)
        raw.extend(buf[y * stride:(y + 1) * stride])

    def chunk(tag: bytes, data: bytes) -> bytes:
        crc = zlib.crc32(tag + data) & 0xFFFFFFFF
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", crc)

    ihdr = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
    idat = zlib.compress(bytes(raw), level=9)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", idat) + chunk(b"IEND", b"")


def generate_essay_plates() -> dict[str, str]:
    PLATES_DIR.mkdir(parents=True, exist_ok=True)
    w, h = 1200, 630
    stone = (244, 241, 234)
    vellum = (251, 249, 245)
    ink = (26, 31, 38)
    prussian = (22, 58, 95)
    minium = (158, 43, 37)
    sienna = (146, 84, 39)
    verdigris = (31, 106, 94)
    rule = (210, 204, 192)
    hashes: dict[str, str] = {}

    # Plate 1: essay01.png (Mesoscopic Floor: Vacuum diamond interferometry vs 310K polymer hydrogel mesh)
    b1 = _make_canvas(w, h, stone)
    _fill_rect(b1, w, h, 36, 36, 582, 594, vellum)
    _fill_rect(b1, w, h, 618, 36, 1164, 594, vellum)
    for gx in range(80, 560, 60):
        _draw_line(b1, w, h, gx, 60, gx, 570, 1.0, rule, 0.55)
    # Left: coherent two-path diamond interferometer + R^6 T^9 wave rings
    _draw_ring(b1, w, h, 309, 315, 195, 2.2, prussian, 0.25)
    _draw_ring(b1, w, h, 309, 315, 135, 2.2, prussian, 0.35)
    for i in range(90):
        u = i / 90
        y = 110 + u * 410
        dx = math.sin(u * math.pi) * 115
        _draw_disc(b1, w, h, 309 - dx, y, 3.2, prussian, 0.95)
        _draw_disc(b1, w, h, 309 + dx, y, 3.2, minium, 0.95)
    _draw_disc(b1, w, h, 309, 110, 9.0, ink)
    _draw_disc(b1, w, h, 309, 520, 9.0, ink)
    _draw_disc(b1, w, h, 194, 315, 11.0, prussian)
    _draw_disc(b1, w, h, 424, 315, 11.0, minium)
    # Right: polymer hydrogel mesh + hindered Brownian walk
    for mx in range(660, 1130, 52):
        _draw_line(b1, w, h, mx, 72, mx + 18, 558, 2.4, verdigris, 0.28)
    for my in range(90, 555, 48):
        _draw_line(b1, w, h, 648, my, 1136, my - 14, 2.4, verdigris, 0.28)
    px, py = 740.0, 175.0
    for step in range(44):
        ang = 1.9 * math.sin(step * 0.73) + 0.65 * math.cos(step * 1.41)
        nx = max(680.0, min(1100.0, px + 24.0 * math.cos(ang)))
        ny = max(110.0, min(525.0, py + 21.0 * math.sin(ang) + 5.5))
        _draw_line(b1, w, h, px, py, nx, ny, 3.4, sienna, 0.9)
        px, py = nx, ny
    _draw_disc(b1, w, h, 740, 175, 10.0, prussian)
    _draw_disc(b1, w, h, px, py, 13.0, minium)
    _draw_line(b1, w, h, 600, 54, 600, 576, 3.0, ink, 0.85)
    p1_bytes = _encode_png(w, h, b1)
    (PLATES_DIR / "essay01.png").write_bytes(p1_bytes)
    hashes["essay01"] = hashlib.sha256(p1_bytes).hexdigest()[:8]

    # Plate 2: essay02.png (Derived, Not Measured: 6-tier epistemic lattice + torsion ring + structural gap)
    b2 = _make_canvas(w, h, stone)
    _fill_rect(b2, w, h, 36, 36, 1164, 594, vellum)
    # Left: Eot-Wash 12-wedge torsion disc
    cx_l, cy_l = 270.0, 315.0
    _draw_ring(b2, w, h, cx_l, cy_l, 155, 3.0, prussian, 0.9)
    _draw_ring(b2, w, h, cx_l, cy_l, 92, 2.5, prussian, 0.7)
    for k in range(12):
        ang = k * (math.pi / 6.0)
        _draw_line(b2, w, h, cx_l + 92 * math.cos(ang), cy_l + 92 * math.sin(ang),
                   cx_l + 155 * math.cos(ang), cy_l + 155 * math.sin(ang), 2.4, prussian, 0.8)
    _draw_disc(b2, w, h, cx_l, cy_l, 12.0, ink)
    # Center: 6-node Epistemic Hasse Lattice
    nodes = [
        (600, 105, verdigris),
        (500, 215, prussian),
        (700, 215, sienna),
        (600, 325, prussian),
        (500, 435, minium),
        (700, 435, ink),
    ]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (3, 5)]
    for i, j in edges:
        _draw_line(b2, w, h, nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1], 3.0, rule, 0.95)
    for nx, ny, ncol in nodes:
        _draw_disc(b2, w, h, nx, ny, 22.0, vellum)
        _draw_ring(b2, w, h, nx, ny, 22.0, 4.0, ncol)
        _draw_disc(b2, w, h, nx, ny, 8.0, ncol)
    # Right: Resolved architectural truss with explicit unmodeled dashed gap
    cx_r, cy_r = 935.0, 315.0
    pts = [(855, 165), (915, 225), (865, 295), (945, 355), (885, 435), (965, 490)]
    for idx in range(len(pts) - 1):
        if idx == 2:
            # Explicit unresolved gap: dotted beads only, never solid interpolated rod
            for d_i in range(1, 6):
                u = d_i / 6.0
                gx = pts[idx][0] + (pts[idx + 1][0] - pts[idx][0]) * u
                gy = pts[idx][1] + (pts[idx + 1][1] - pts[idx][1]) * u
                _draw_disc(b2, w, h, gx, gy, 3.0, minium, 0.85)
        else:
            _draw_line(b2, w, h, pts[idx][0], pts[idx][1], pts[idx + 1][0], pts[idx + 1][1], 4.2, ink, 0.9)
    for px2, py2 in pts:
        _draw_disc(b2, w, h, px2, py2, 9.5, prussian)
    _draw_ring(b2, w, h, cx_r - 25, cy_r + 10, 48.0, 2.4, minium, 0.75)
    p2_bytes = _encode_png(w, h, b2)
    (PLATES_DIR / "essay02.png").write_bytes(p2_bytes)
    hashes["essay02"] = hashlib.sha256(p2_bytes).hexdigest()[:8]

    # Plate 3: essay03.png (Barriers, Pores, and Clocks: Markov clock ring + Q_TUR >= 2 hyperbola + Kramers double-well)
    b3 = _make_canvas(w, h, stone)
    _fill_rect(b3, w, h, 36, 36, 1164, 594, vellum)
    # Left: 6-state biased Markov clock ring
    rcx, rcy, rr = 235.0, 315.0, 130.0
    _draw_ring(b3, w, h, rcx, rcy, rr, 3.0, prussian, 0.45)
    for k in range(6):
        ang = -0.5 * math.pi + k * (math.pi / 3.0)
        sx, sy = rcx + rr * math.cos(ang), rcy + rr * math.sin(ang)
        _draw_disc(b3, w, h, sx, sy, 16.0, vellum)
        _draw_ring(b3, w, h, sx, sy, 16.0, 3.8, prussian if k % 2 == 0 else verdigris)
    _draw_line(b3, w, h, rcx, rcy, rcx + 76, rcy - 44, 4.0, minium)
    _draw_disc(b3, w, h, rcx, rcy, 8.0, ink)
    # Center: TUR hyperbolic bound curve (Var * Sigma >= 2 k_B)
    _draw_line(b3, w, h, 455, 515, 765, 515, 2.5, ink)
    _draw_line(b3, w, h, 455, 515, 455, 115, 2.5, ink)
    prev = None
    for i in range(90):
        u = 0.12 + (i / 89.0) * 0.88
        x = 465 + u * 290
        y = 505 - min(370.0, 72.0 / u)
        if prev is not None:
            _draw_line(b3, w, h, prev[0], prev[1], x, y, 4.0, minium)
        prev = (x, y)
    # Right: Kramers double-well free-energy barrier (high solid vs rescued dashed/lowered)
    prev_hi, prev_lo = None, None
    for i in range(110):
        q = -1.35 + (i / 109.0) * 2.7
        x = 825 + ((q + 1.35) / 2.7) * 300
        v_hi = 0.9 * (q * q - 1.0) ** 2 + 0.12 * q
        v_lo = 0.48 * (q * q - 1.0) ** 2 + 0.12 * q
        y_hi = 485 - v_hi * 240
        y_lo = 485 - v_lo * 240
        if prev_hi is not None:
            _draw_line(b3, w, h, prev_hi[0], prev_hi[1], x, y_hi, 3.6, prussian)
            _draw_line(b3, w, h, prev_lo[0], prev_lo[1], x, y_lo, 3.2, verdigris)
        prev_hi, prev_lo = (x, y_hi), (x, y_lo)
    p3_bytes = _encode_png(w, h, b3)
    (PLATES_DIR / "essay03.png").write_bytes(p3_bytes)
    hashes["essay03"] = hashlib.sha256(p3_bytes).hexdigest()[:8]

    # Plate 4: essay04.png (Tensegrity, Microcausality & Zero Modes: braced cubic truss + rank matrix + spacelike arms)
    b4 = _make_canvas(w, h, stone)
    _fill_rect(b4, w, h, 36, 36, 582, 594, vellum)
    _fill_rect(b4, w, h, 618, 36, 1164, 594, vellum)
    # Left: 3D isometric cubic truss with 6 verdigris diagonal shear braces
    cube_pts = [
        (160, 210), (360, 210), (360, 410), (160, 410),
        (245, 145), (445, 145), (445, 345), (245, 345),
    ]
    cube_edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
    ]
    cube_diags = [(0, 2), (4, 6), (0, 5), (3, 6), (1, 6), (0, 7)]
    for i, j in cube_diags:
        _draw_line(b4, w, h, cube_pts[i][0], cube_pts[i][1], cube_pts[j][0], cube_pts[j][1], 2.8, verdigris, 0.8)
    for i, j in cube_edges:
        _draw_line(b4, w, h, cube_pts[i][0], cube_pts[i][1], cube_pts[j][0], cube_pts[j][1], 3.8, prussian, 0.92)
    for cx_p, cy_p in cube_pts:
        _draw_disc(b4, w, h, cx_p, cy_p, 8.5, ink)
    # Right: su(4) 6+9 Cartan decomposition lattice & spacelike lightcone arms [A_A, A_B] = 0
    _draw_line(b4, w, h, 890, 110, 890, 520, 2.0, rule, 0.9)
    _draw_line(b4, w, h, 720, 145, 1060, 485, 2.2, minium, 0.45)
    _draw_line(b4, w, h, 1060, 145, 720, 485, 2.2, minium, 0.45)
    _draw_ring(b4, w, h, 755, 315, 58.0, 3.6, prussian, 0.9)
    _draw_ring(b4, w, h, 1025, 315, 58.0, 3.6, verdigris, 0.9)
    for k in range(3):
        ang = k * (2.0 * math.pi / 3.0)
        _draw_disc(b4, w, h, 755 + 58 * math.cos(ang), 315 + 58 * math.sin(ang), 7.5, prussian)
        _draw_disc(b4, w, h, 1025 + 58 * math.cos(ang), 315 + 58 * math.sin(ang), 7.5, verdigris)
    for r_i in range(3):
        for c_i in range(3):
            gx, gy = 855 + c_i * 35, 280 + r_i * 35
            _draw_disc(b4, w, h, gx, gy, 5.5, sienna, 0.85)
    _draw_line(b4, w, h, 600, 54, 600, 576, 3.0, ink, 0.85)
    p4_bytes = _encode_png(w, h, b4)
    (PLATES_DIR / "essay04.png").write_bytes(p4_bytes)
    hashes["essay04"] = hashlib.sha256(p4_bytes).hexdigest()[:8]

    # Plate 5: essay05.png (Islands, Blinders & Conditional Survival: QES Page tent vs Hawking rise + Doob barrier chain)
    b5 = _make_canvas(w, h, stone)
    _fill_rect(b5, w, h, 36, 36, 1164, 594, vellum)
    # Left-Center: Page curve axes + Hawking rising line + QES unitary tent crossing at midpoint
    ax_x0, ax_y0, ax_w, ax_h = 95, 505, 520, 360
    _draw_line(b5, w, h, ax_x0, ax_y0, ax_x0 + ax_w, ax_y0, 2.8, ink)
    _draw_line(b5, w, h, ax_x0, ax_y0, ax_x0, ax_y0 - ax_h, 2.8, ink)
    # Hawking coarse-grained / blinder line (minium)
    _draw_line(b5, w, h, ax_x0, ax_y0, ax_x0 + ax_w, ax_y0 - ax_h + 20, 3.6, minium, 0.82)
    # Island saddle descending line (verdigris faint)
    _draw_line(b5, w, h, ax_x0, ax_y0 - ax_h + 20, ax_x0 + ax_w, ax_y0, 2.4, verdigris, 0.45)
    # QES unitary tent (prussian bold)
    mid_x, mid_y = ax_x0 + ax_w * 0.5, ax_y0 - (ax_h - 20) * 0.5
    _draw_line(b5, w, h, ax_x0, ax_y0, mid_x, mid_y, 5.0, prussian)
    _draw_line(b5, w, h, mid_x, mid_y, ax_x0 + ax_w, ax_y0, 5.0, prussian)
    _draw_disc(b5, w, h, mid_x, mid_y, 11.0, sienna)
    _draw_disc(b5, w, h, ax_x0 + ax_w, ax_y0, 10.0, verdigris)
    # Right: 6-step absorbing barrier chain + Doob h-conditioned surviving trajectory
    for b_idx in range(6):
        bx = 700 + b_idx * 72
        _draw_line(b5, w, h, bx, 150, bx, 480, 2.6, rule, 0.95)
        # Absorbing sink node below
        _draw_disc(b5, w, h, bx, 495, 7.5, minium, 0.8)
        if b_idx < 5:
            y_cur = 340 - b_idx * 28
            y_nxt = 340 - (b_idx + 1) * 28
            _draw_line(b5, w, h, bx, y_cur, bx + 72, y_nxt, 4.4, verdigris)
            _draw_line(b5, w, h, bx, y_cur, bx + 26, 495, 2.0, minium, 0.55)
        _draw_disc(b5, w, h, bx, 340 - b_idx * 28, 9.0, prussian)
    p5_bytes = _encode_png(w, h, b5)
    (PLATES_DIR / "essay05.png").write_bytes(p5_bytes)
    hashes["essay05"] = hashlib.sha256(p5_bytes).hexdigest()[:8]

    # Plate 6: essay06.png (One Timeless Operator, Four Regimes & Zero-Sorry Proof: 16-tick WdW clock + bilateral echo + turnstile)
    b6 = _make_canvas(w, h, stone)
    _fill_rect(b6, w, h, 36, 36, 1164, 594, vellum)
    # Left: 16-state Page-Wootters timeless clock ring coupled to central 4-state system diamond
    wcx, wcy, wr = 265.0, 315.0, 155.0
    _draw_ring(b6, w, h, wcx, wcy, wr, 3.2, prussian, 0.85)
    _draw_ring(b6, w, h, wcx, wcy, 68.0, 2.4, verdigris, 0.75)
    for k in range(16):
        ang = -0.5 * math.pi + k * (math.pi / 8.0)
        tx, ty = wcx + wr * math.cos(ang), wcy + wr * math.sin(ang)
        _draw_disc(b6, w, h, tx, ty, 7.5 if k % 4 else 10.5, prussian if k % 2 == 0 else sienna)
        if k % 4 == 0:
            ix, iy = wcx + 68.0 * math.cos(ang), wcy + 68.0 * math.sin(ang)
            _draw_line(b6, w, h, ix, iy, tx, ty, 2.4, verdigris, 0.75)
            _draw_disc(b6, w, h, ix, iy, 8.5, ink)
    # Center: Bilateral X_A (x) X_B spin-echo pulse rails
    for ry in (235, 395):
        _draw_line(b6, w, h, 495, ry, 795, ry, 3.2, prussian)
    for px_i in (555, 625, 695, 765):
        _draw_line(b6, w, h, px_i, 195, px_i, 435, 3.8, sienna, 0.9)
        _draw_disc(b6, w, h, px_i, 235, 8.5, verdigris)
        _draw_disc(b6, w, h, px_i, 395, 8.5, verdigris)
    # Right: 4-Wall exclusion frame + formal turnstile geometry (⊢)
    _fill_rect(b6, w, h, 865, 135, 1115, 495, stone, 0.85)
    _draw_line(b6, w, h, 865, 135, 1115, 135, 3.0, minium)
    _draw_line(b6, w, h, 865, 495, 1115, 495, 3.0, minium)
    _draw_line(b6, w, h, 865, 135, 865, 495, 3.0, minium)
    _draw_line(b6, w, h, 1115, 135, 1115, 495, 3.0, minium)
    # Crisp turnstile symbol (geometric vertical + horizontal bar, not letters) + unitary survival disc
    _draw_line(b6, w, h, 945, 235, 945, 395, 6.0, ink)
    _draw_line(b6, w, h, 945, 315, 1035, 315, 6.0, ink)
    _draw_disc(b6, w, h, 1055, 315, 16.0, verdigris)
    _draw_ring(b6, w, h, 1055, 315, 26.0, 3.0, prussian)
    p6_bytes = _encode_png(w, h, b6)
    (PLATES_DIR / "essay06.png").write_bytes(p6_bytes)
    hashes["essay06"] = hashlib.sha256(p6_bytes).hexdigest()[:8]

    # Plate 7: essay07.png (Parallel Horizon & Quantum Island: 1.547σ -> 2.211σ ceiling + D=75µm island + 2.04K valley + 90° '+' null)
    b7 = _make_canvas(w, h, stone)
    _fill_rect(b7, w, h, 36, 36, 1164, 594, vellum)
    # Left panel: Parallel horizon expansion curve from 51.2 µm to 73.14 µm ceiling + green D = 75 µm island above 28.3 µm Casimir wall
    lx0, ly0, lw, lh = 95, 515, 455, 390
    # Quantum island corridor above 73.14 µm ceiling (y = 200..125)
    _fill_rect(b7, w, h, lx0, 125, lx0 + lw, 205, (215, 236, 224), 0.72)
    _draw_line(b7, w, h, lx0, ly0, lx0 + lw, ly0, 2.8, ink)
    _draw_line(b7, w, h, lx0, ly0, lx0, 125, 2.8, ink)
    # Casimir + 2R floor line (y = 415)
    _draw_line(b7, w, h, lx0, 415, lx0 + lw, 415, 3.0, sienna, 0.9)
    # 73.14 µm asymptotic parallel ceiling line (y = 205)
    _draw_line(b7, w, h, lx0, 205, lx0 + lw, 205, 3.2, minium, 0.92)
    # Monotone parallel horizon curve rising from 51.18 µm (y = 300) toward 73.14 µm (y = 205)
    prev_hx, prev_hy = float(lx0), 300.0
    for step_i in range(1, 33):
        u = step_i / 32.0
        hx = lx0 + u * lw
        frac = (u * u) / (0.14 + u * u)
        hy = 300.0 - 92.0 * frac
        _draw_line(b7, w, h, prev_hx, prev_hy, hx, hy, 4.6, minium)
        prev_hx, prev_hy = hx, hy
    # D = 60 µm naive trap point (minium warning ring) vs D = 75 µm quantum island benchmark disc (verdigris + prussian)
    _draw_disc(b7, w, h, lx0 + 0.62 * lw, 262.0, 9.0, minium)
    _draw_disc(b7, w, h, lx0 + 0.72 * lw, 168.0, 13.5, verdigris)
    _draw_ring(b7, w, h, lx0 + 0.72 * lw, 168.0, 22.0, 3.0, prussian)
    # Center divider
    _draw_line(b7, w, h, 600, 54, 600, 576, 3.0, ink, 0.85)
    # Right-top: 2.04 K isobaric cryogenic valley curve (T^-1/2 gas + T^6 photon)
    rx0, ry0, rw = 665, 295, 435
    _draw_line(b7, w, h, rx0, ry0, rx0 + rw, ry0, 2.4, rule)
    pv_x, pv_y = float(rx0), 175.0
    for k_i in range(1, 33):
        u = k_i / 32.0
        tk = 0.7 + 2.5 * u
        val = 0.55 * (tk ** -0.5) + 0.012 * (tk ** 3.8)
        vx = rx0 + u * rw
        vy = ry0 - min(165.0, max(22.0, val * 155.0))
        _draw_line(b7, w, h, pv_x, pv_y, vx, vy, 4.0, prussian)
        pv_x, pv_y = vx, vy
    # Valley minimum marker around T* = 2.04 K (u ~ 0.54)
    _draw_disc(b7, w, h, rx0 + 0.54 * rw, 228.0, 10.5, sienna)
    # Right-bottom: Midpoint-centred '+' 90° orthogonal null cross geometry
    ncx, ncy, arm = 882.0, 435.0, 82.0
    _draw_ring(b7, w, h, ncx, ncy, arm, 2.4, rule, 0.9)
    _draw_line(b7, w, h, ncx - arm, ncy, ncx + arm, ncy, 4.8, prussian)
    _draw_line(b7, w, h, ncx, ncy - arm, ncx, ncy + arm, 4.8, verdigris)
    for dx_p, dy_p, col_p in ((-arm, 0.0, prussian), (arm, 0.0, prussian), (0.0, -arm, verdigris), (0.0, arm, verdigris)):
        _draw_disc(b7, w, h, ncx + dx_p, ncy + dy_p, 8.5, col_p)
    _draw_disc(b7, w, h, ncx, ncy, 7.5, sienna)
    p7_bytes = _encode_png(w, h, b7)
    (PLATES_DIR / "essay07.png").write_bytes(p7_bytes)
    hashes["essay07"] = hashlib.sha256(p7_bytes).hexdigest()[:8]
    return hashes


def plate_hash(plate_slug: str) -> str:
    p = PLATES_DIR / f"{plate_slug}.png"
    return hashlib.sha256(p.read_bytes()).hexdigest()[:8] if p.is_file() else "00000000"


# ---------------------------------------------------------------------------
# Interactive SVG Instruments for ES.01, ES.02, ES.03
# ---------------------------------------------------------------------------

def render_predict_box(essay: dict, is_es: bool = False) -> str:
    pred = essay["predict"]
    btns = []
    for ch in pred["choices"]:
        btns.append(
            f'          <button type="button" class="tp-cta" data-choice="{a(ch["id"])}" aria-pressed="false" '
            f'data-en="{a(ch["en"])}" data-es="{a(ch["es"])}">{t(ch["en"])}</button>'
        )
    btns_html = "\n".join(btns)
    aria_pred = "Predice antes de revelar" if is_es else "Predict before reveal"
    return f"""    <section class="tp-essay-predict" data-cs-predict data-answer="{a(pred['answer'])}" data-explain-en="{a(pred['explain_en'])}" data-explain-es="{a(pred['explain_es'])}" aria-label="{aria_pred}">
      <p class="tp-kicker" data-en="Predict Before You Reveal · Active Intuition Check" data-es="Predice Antes de Revelar · Prueba de Intuición">Predict Before You Reveal · Active Intuition Check</p>
      {bi("p", pred["question_en"], pred["question_es"], "tp-essay-predict-q")}
      <div class="tp-essay-predict-btns">
{btns_html}
      </div>
      <p class="tp-essay-predict-verdict" data-cs-verdict hidden role="status"></p>
    </section>"""


def render_instrument(essay: dict, is_es: bool = False) -> str:
    kind = essay["instrument_kind"]
    if kind == "mesoscopic":
        svg_aria = (
            "Comparación logarítmica de tasa colisional de helio en onda corta, tasa dipolar de fotones térmicos y fracción de difusión de Ogston en hidrogel"
            if is_es
            else "Logarithmic bar comparison of short-wavelength helium collision rate, dipole black-body photon localization rate, and Ogston hydrogel diffusion fraction"
        )
        return f"""    <section id="instrument" class="tp-essay-observatory" data-cs-instrument="mesoscopic" aria-labelledby="inst-heading">
      <div class="tp-essay-obs-head">
        <p class="tp-kicker" data-en="Interactive Cross-Scale Observatory · ES.01" data-es="Observatorio Interactivo entre Escalas · ES.01">Interactive Cross-Scale Observatory · ES.01</p>
        <h2 id="inst-heading" class="tp-h2" data-en="Vacuum Decoherence (0.5–20 K) vs. Hydrogel Hindered Diffusion (310 K)" data-es="Decoherencia en Vacío (0.5–20 K) frente a Difusión Impedida en Hidrogel (310 K)">Vacuum Decoherence (0.5–20 K) vs. Hydrogel Hindered Diffusion (310 K)</h2>
      </div>
      <div class="tp-essay-obs-grid">
        <svg class="tp-essay-svg" viewBox="0 0 560 250" role="img" aria-label="{svg_aria}">
          <rect x="8" y="8" width="544" height="234" rx="10" fill="var(--tp-stone)" stroke="var(--tp-rule)"/>
          <text x="24" y="40" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="1 · He Collisional Rate Γ_gas (short-λ saturated, 10⁻¹²–10¹⁰ s⁻¹)" data-es="1 · Tasa Colisional de He Γ_gas (onda corta saturada, 10⁻¹²–10¹⁰ s⁻¹)">1 · He Collisional Rate Γ_gas (short-λ saturated, 10⁻¹²–10¹⁰ s⁻¹)</text>
          <rect x="24" y="50" width="240" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="gas" x="24" y="50" width="107.0" height="18" rx="4" fill="var(--tp-prussian)"/>
          <text data-cs-read="gammagas" x="278" y="64" fill="var(--tp-ink)" font-family="monospace" font-size="13">6.40e-3 s⁻¹</text>

          <text x="24" y="114" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="2 · Scattered Photon Rate Γ_ph (long-λ R⁶T⁹Δx², 10⁻¹²–10¹⁰ s⁻¹)" data-es="2 · Fotones Térmicos Γ_ph (onda larga R⁶T⁹Δx², 10⁻¹²–10¹⁰ s⁻¹)">2 · Scattered Photon Rate Γ_ph (long-λ R⁶T⁹Δx², 10⁻¹²–10¹⁰ s⁻¹)</text>
          <rect x="24" y="124" width="240" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="phot" x="24" y="124" width="97.7" height="18" rx="4" fill="var(--tp-minium)"/>
          <text data-cs-read="gammaphot" x="278" y="138" fill="var(--tp-ink)" font-family="monospace" font-size="13">8.94e-4 s⁻¹</text>

          <text x="24" y="186" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="3 · 310 K Nanoparticle Mobility D_eff / D₀ (100 nm sphere in mesh ξ)" data-es="3 · Movilidad de Nanopartícula a 310 K D_eff / D₀ (esfera de 100 nm en malla ξ)">3 · 310 K Nanoparticle Mobility D_eff / D₀ (100 nm sphere in mesh ξ)</text>
          <rect x="24" y="196" width="240" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="gel" x="24" y="196" width="137.5" height="18" rx="4" fill="var(--tp-verdigris)"/>
          <text data-cs-read="deff" x="278" y="210" fill="var(--tp-ink)" font-family="monospace" font-size="13" data-en="3.77 µm²/s (57.3% of D₀)" data-es="3.77 µm²/s (57.3% de D₀)">3.77 µm²/s (57.3% of D₀)</text>
        </svg>
        <div class="tp-essay-controls">
          <label class="tp-essay-ctrl">
            <span data-en="Vacuum gas pressure log₁₀(P / Pa)" data-es="Presión de gas en vacío log₁₀(P / Pa)">Vacuum gas pressure log₁₀(P / Pa)</span>
            <strong data-cs-read="logp">10^-15.0 Pa</strong>
            <input type="range" min="-17" max="-11" step="0.5" value="-15" data-cs-input="logp">
          </label>
          <label class="tp-essay-ctrl">
            <span data-en="Ambient vacuum bath temperature T (K)" data-es="Temperatura del baño en vacío T (K)">Ambient vacuum bath temperature T (K)</span>
            <strong data-cs-read="temp">4.0 K</strong>
            <input type="range" min="0.5" max="20" step="0.5" value="4.0" data-cs-input="temp">
          </label>
          <label class="tp-essay-ctrl">
            <span data-en="Diamond superposition split Δx (µm)" data-es="Separación de superposición Δx (µm)">Diamond superposition split Δx (µm)</span>
            <strong data-cs-read="split">100 µm</strong>
            <input type="range" min="10" max="250" step="10" value="100" data-cs-input="split">
          </label>
          <label class="tp-essay-ctrl">
            <span data-en="310 K polymer/mucin mesh spacing ξ (nm)" data-es="Espaciamiento de malla polimérica a 310 K ξ (nm)">310 K polymer/mucin mesh spacing ξ (nm)</span>
            <strong data-cs-read="mesh">120 nm</strong>
            <input type="range" min="60" max="350" step="10" value="120" data-cs-input="mesh">
          </label>
          <button type="button" class="tp-cta" data-cs-knockout aria-pressed="false" data-en="Toggle Planted Regime Defect" data-es="Alternar Defecto de Régimen Plantado">Toggle Planted Regime Defect</button>
        </div>
      </div>
      <p class="tp-essay-status" data-cs-status role="status"></p>
    </section>"""

    if kind == "epistemic":
        svg_aria = (
            "Comparación de cuatro niveles epistémicos: MEDIDO, DERIVADO (NO MEDIDO), PROPUESTO y ABIERTO / COORDENADAS NO RESUELTAS"
            if is_es
            else "Four-tier epistemic provenance comparison: MEASURED, DERIVED (NOT MEASURED), PROPOSED, and OPEN / UNRESOLVED COORDINATES"
        )
        grp_aria = "Seleccionar caso científico" if is_es else "Select scientific claim case"
        return f"""    <section id="instrument" class="tp-essay-observatory" data-cs-instrument="epistemic" aria-labelledby="inst-heading">
      <div class="tp-essay-obs-head">
        <p class="tp-kicker" data-en="Interactive Epistemic Lattice &amp; Mutation Inspector · ES.02" data-es="Inspector Interactivo de Celosía Epistémica y Mutaciones · ES.02">Interactive Epistemic Lattice &amp; Mutation Inspector · ES.02</p>
        <h2 id="inst-heading" class="tp-h2" data-en="Why Calculation Precision Never Substitutes for a Missing Measurement" data-es="Por Qué la Precisión de Cálculo Nunca Sustituye una Medición Ausente">Why Calculation Precision Never Substitutes for a Missing Measurement</h2>
      </div>
      <div class="tp-essay-obs-grid">
        <svg class="tp-essay-svg" viewBox="0 0 560 300" role="img" aria-label="{svg_aria}">
          <rect x="8" y="8" width="544" height="284" rx="10" fill="var(--tp-stone)" stroke="var(--tp-rule)"/>
          <rect data-ep-highlight x="20" y="108" width="520" height="44" rx="8" fill="var(--tp-prussian-soft)" stroke="var(--tp-prussian)" stroke-width="2"/>
          <text x="36" y="68" fill="var(--tp-ink)" font-size="13" font-weight="700" data-en="MEASURED · ≥ 2 independent collaborations, peer-reviewed, &gt; 24 months" data-es="MEDIDO · ≥ 2 colaboraciones independientes, revisado por pares, &gt; 24 meses">MEASURED · ≥ 2 independent collaborations, peer-reviewed, &gt; 24 months</text>
          <text x="36" y="134" fill="var(--tp-prussian)" font-size="13" font-weight="700" data-en="DERIVED (NOT MEASURED) · Exact math from a named MEASURED parent row" data-es="DERIVADO (NO MEDIDO) · Álgebra exacta desde una fila madre MEDIDA">DERIVED (NOT MEASURED) · Exact math from a named MEASURED parent row</text>
          <text x="36" y="198" fill="var(--tp-sienna)" font-size="13" font-weight="700" data-en="PROPOSED · Unbuilt apparatus or preprint ceiling (never promoted by algebra)" data-es="PROPUESTO · Aparato no construido o preimpresión (nunca promovido por álgebra)">PROPOSED · Unbuilt apparatus or preprint ceiling (never promoted by algebra)</text>
          <text x="36" y="262" fill="var(--tp-minium)" font-size="13" font-weight="700" data-en="OPEN / UNRESOLVED · Active dispute or disordered cryo-EM density left blank" data-es="ABIERTO / NO RESUELTO · Disputa activa o densidad crio-EM desordenada en blanco">OPEN / UNRESOLVED · Active dispute or disordered cryo-EM density left blank</text>
        </svg>
        <div class="tp-essay-controls">
          <div class="tp-essay-btn-stack" role="group" aria-label="{grp_aria}">
            <button type="button" class="tp-cta" data-ep-case="derived_recast" aria-pressed="true" data-en="T.05 Fourier–Bessel σ ≤ 33 µm Recast" data-es="Recast T.05 Fourier–Bessel σ ≤ 33 µm">T.05 Fourier–Bessel σ ≤ 33 µm Recast</button>
            <button type="button" class="tp-cta" data-ep-case="cryo_rdomain" aria-pressed="false" data-en="Cryo-EM 5UAK/6MSM Unmodeled R-Domain" data-es="Dominio R No Resuelto en Crio-EM 5UAK/6MSM">Cryo-EM 5UAK/6MSM Unmodeled R-Domain</button>
            <button type="button" class="tp-cta" data-ep-case="bmv_witness" aria-pressed="false" data-en="2017 BMV 10⁻¹⁴ kg Entanglement Witness" data-es="Testigo BMV 2017 de 10⁻¹⁴ kg">2017 BMV 10⁻¹⁴ kg Entanglement Witness</button>
            <button type="button" class="tp-cta" data-ep-case="eotwash_law" aria-pressed="false" data-en="52 µm Sub-Millimetre Inverse-Square Law" data-es="Ley del Inverso del Cuadrado a 52 µm">52 µm Sub-Millimetre Inverse-Square Law</button>
          </div>
          <div class="tp-essay-readout-box">
            <div><span data-en="Assigned Badge:" data-es="Etiqueta Asignada:">Assigned Badge:</span> <strong data-cs-read="badge" data-en="DERIVED (NOT MEASURED)" data-es="DERIVADO (NO MEDIDO)">DERIVED (NOT MEASURED)</strong></div>
            <div><strong data-cs-read="parent" data-en="Parent: T05-LEE2020 (52 µm Eöt-Wash inverse-square data)" data-es="Fila madre: T05-LEE2020 (datos Eöt-Wash a 52 µm)">Parent: T05-LEE2020 (52 µm Eöt-Wash inverse-square data)</strong></div>
            <div><span data-en="Mutation Gate:" data-es="Compuerta de Mutación:">Mutation Gate:</span> <strong data-cs-read="mutants" data-en="8/8 mutants killed (PASS)" data-es="8/8 mutantes eliminados (PASA)">8/8 mutants killed (PASS)</strong></div>
          </div>
          <button type="button" class="tp-cta" data-cs-knockout aria-pressed="false" data-en="Toggle Lax Prose Mode (Disable Parent Gate)" data-es="Alternar Modo Laxo (Apagar Compuerta Madre)">Toggle Lax Prose Mode (Disable Parent Gate)</button>
        </div>
      </div>
      <p class="tp-essay-status" data-cs-status role="status"></p>
    </section>"""

    if kind == "kinematic":
        svg_aria = (
            "Comparación rango-nulidad de modos blandos en celosía cúbica, modos no locales en su(4) y deriva de negatividad BMV"
            if is_es
            else "Rank-nullity comparison of cubic space-frame floppy modes, su(4) non-local zero-modes, and BMV entanglement negativity drift"
        )
        return f"""    <section id="instrument" class="tp-essay-observatory" data-cs-instrument="kinematic" aria-labelledby="inst-heading">
      <div class="tp-essay-obs-head">
        <p class="tp-kicker" data-en="Interactive Rank–Nullity &amp; Microcausality Observatory · ES.04" data-es="Observatorio Interactivo de Rango-Nulidad y Microcausalidad · ES.04">Interactive Rank–Nullity &amp; Microcausality Observatory · ES.04</p>
        <h2 id="inst-heading" class="tp-h2" data-en="Cubic Space-Frame Bracing (3V − 6 − E) vs. su(4) Microcausality Locking" data-es="Arriostramiento de Celosía Cúbica (3V − 6 − E) frente al Bloqueo de Microcausalidad en su(4)">Cubic Space-Frame Bracing (3V − 6 − E) vs. su(4) Microcausality Locking</h2>
      </div>
      <div class="tp-essay-obs-grid">
        <svg class="tp-essay-svg" viewBox="0 0 560 250" role="img" aria-label="{svg_aria}">
          <rect x="8" y="8" width="544" height="234" rx="10" fill="var(--tp-stone)" stroke="var(--tp-rule)"/>
          <text x="24" y="40" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="1 · 3D Cubic Truss Shear Zero-Modes (V = 8, E = 12 + braces)" data-es="1 · Modos Blandos de Corte en Celosía Cúbica 3D (V = 8, E = 12 + diagonales)">1 · 3D Cubic Truss Shear Zero-Modes (V = 8, E = 12 + braces)</text>
          <rect x="24" y="50" width="230" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="truss" x="24" y="50" width="8.0" height="18" rx="4" fill="var(--tp-prussian)"/>
          <text data-cs-read="trussmodes" x="268" y="64" fill="var(--tp-ink)" font-family="monospace" font-size="13" data-en="0 floppy · 0 self-stress" data-es="0 blandos · 0 autotensión">0 floppy · 0 self-stress</text>

          <text x="24" y="114" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="2 · su(4) Unpinned Cartan–Weyl σ_i ⊗ σ_j Modes (dim 15 = 6 local + 9 non-local)" data-es="2 · Modos Cartan–Weyl σ_i ⊗ σ_j Libres en su(4) (dim 15 = 6 locales + 9 no locales)">2 · su(4) Unpinned Cartan–Weyl σ_i ⊗ σ_j Modes (dim 15 = 6 local + 9 non-local)</text>
          <rect x="24" y="124" width="230" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="su4" x="24" y="124" width="8.0" height="18" rx="4" fill="var(--tp-verdigris)"/>
          <text data-cs-read="su4modes" x="268" y="138" fill="var(--tp-ink)" font-family="monospace" font-size="13" data-en="0 free non-local (local kernel = 6)" data-es="0 no locales libres (núcleo local = 6)">0 free non-local (local kernel = 6)</text>

          <text x="24" y="186" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="3 · Two-Mass BMV Negativity Gauge Drift ΔN under Allowed Algebra" data-es="3 · Deriva de Calibre de Negatividad BMV ΔN bajo el Álgebra Permitida">3 · Two-Mass BMV Negativity Gauge Drift ΔN under Allowed Algebra</text>
          <rect x="24" y="196" width="230" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="drift" x="24" y="196" width="8.0" height="18" rx="4" fill="var(--tp-minium)"/>
          <text data-cs-read="bmvdrift" x="268" y="210" fill="var(--tp-ink)" font-family="monospace" font-size="13" data-en="ΔN = 0.000 (N = 0.078 invariant)" data-es="ΔN = 0.000 (N = 0.078 invariante)">ΔN = 0.000 (N = 0.078 invariant)</text>
        </svg>
        <div class="tp-essay-controls">
          <label class="tp-essay-ctrl">
            <span data-en="Diagonal shear braces on cubic frame" data-es="Diagonales de corte en celosía cúbica">Diagonal shear braces on cubic frame</span>
            <strong data-cs-read="braces">6 / 6</strong>
            <input type="range" min="0" max="7" step="1" value="6" data-cs-input="braces">
          </label>
          <label class="tp-essay-ctrl">
            <span data-en="Pinned spatial microcausality commutators [A_A, A_B] = 0" data-es="Conmutadores espaciales fijados [A_A, A_B] = 0">Pinned spatial microcausality commutators [A_A, A_B] = 0</span>
            <strong data-cs-read="pinrank">9 / 9</strong>
            <input type="range" min="0" max="9" step="1" value="9" data-cs-input="pinrank">
          </label>
          <button type="button" class="tp-cta" data-cs-knockout aria-pressed="false" data-en="Toggle Non-Local su(4) Refactorization Defect" data-es="Alternar Defecto de Refactorización No Local en su(4)">Toggle Non-Local su(4) Refactorization Defect</button>
        </div>
      </div>
      <p class="tp-essay-status" data-cs-status role="status"></p>
    </section>"""

    if kind == "island_page":
        svg_aria = (
            "Comparación en nats entre la curva unitaria QES de Page, la línea de grano grueso sin vestido gravitatorio y el costo KL de Doob"
            if is_es
            else "Comparison in nats of the unitary QES Page tent, the undressed subalgebra coarse-graining line, and the Doob KL post-selection cost"
        )
        grp_aria = "Seleccionar régimen de horizonte o barrera" if is_es else "Select horizon or barrier regime"
        return f"""    <section id="instrument" class="tp-essay-observatory" data-cs-instrument="island_page" aria-labelledby="inst-heading">
      <div class="tp-essay-obs-head">
        <p class="tp-kicker" data-en="Interactive Page-Curve &amp; Doob Survival Observatory · ES.05" data-es="Observatorio Interactivo de Curva de Page y Supervivencia de Doob · ES.05">Interactive Page-Curve &amp; Doob Survival Observatory · ES.05</p>
        <h2 id="inst-heading" class="tp-h2" data-en="Unitary QES Saddle Switch vs. Subalgebra Blinders vs. Doob Post-Selection Cost" data-es="Cambio de Silla QES Unitario frente a Subálgebra Restringida y Costo de Doob">Unitary QES Saddle Switch vs. Subalgebra Blinders vs. Doob Post-Selection Cost</h2>
      </div>
      <div class="tp-essay-obs-grid">
        <svg class="tp-essay-svg" viewBox="0 0 560 260" role="img" aria-label="{svg_aria}">
          <rect x="8" y="8" width="544" height="244" rx="10" fill="var(--tp-stone)" stroke="var(--tp-rule)"/>
          <line x1="64" y1="224" x2="496" y2="224" stroke="var(--tp-ink)" stroke-width="1.5"/>
          <line x1="64" y1="44" x2="64" y2="224" stroke="var(--tp-ink)" stroke-width="1.5"/>
          <line x1="64" y1="224" x2="496" y2="44" stroke="var(--tp-minium)" stroke-width="2.2" stroke-dasharray="6 4"/>
          <polyline points="64,224 280,134 496,224" fill="none" stroke="var(--tp-prussian)" stroke-width="3.4"/>
          <circle data-ip-point cx="280.0" cy="134.0" r="8.5" fill="var(--tp-verdigris)" stroke="var(--tp-vellum)" stroke-width="2.5"/>
          <text x="76" y="34" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="Entropy S(k) in nats · Solid: QES min(k, 6−k) ln 2 · Dashed: Undressed k ln 2" data-es="Entropía S(k) en nats · Sólida: QES mín(k, 6−k) ln 2 · Guiones: Sin vestido k ln 2">Entropy S(k) in nats · Solid: QES min(k, 6−k) ln 2 · Dashed: Undressed k ln 2</text>
          <text x="64" y="242" fill="var(--tp-ink)" font-size="11">k = 0</text>
          <text x="266" y="242" fill="var(--tp-ink)" font-size="11">k = 3</text>
          <text x="476" y="242" fill="var(--tp-ink)" font-size="11">k = 6</text>
        </svg>
        <div class="tp-essay-controls">
          <div class="tp-essay-btn-stack" role="group" aria-label="{grp_aria}">
            <button type="button" class="tp-cta" data-ip-mode="qes_unitary" aria-pressed="true" data-en="1 · Unitary QES Saddle Switch (DERIVED)" data-es="1 · Cambio de Silla QES Unitario (DERIVADO)">1 · Unitary QES Saddle Switch (DERIVED)</button>
            <button type="button" class="tp-cta" data-ip-mode="blinder_cptp" aria-pressed="false" data-en="2 · Subalgebra Blinders (PROPOSED CPTP)" data-es="2 · Subálgebra sin Vestido (CPTP PROPUESTO)">2 · Subalgebra Blinders (PROPOSED CPTP)</button>
            <button type="button" class="tp-cta" data-ip-mode="doob_postselect" aria-pressed="false" data-en="3 · Doob Conditional Survival (Post-Selected)" data-es="3 · Supervivencia Condicional de Doob (Postselección)">3 · Doob Conditional Survival (Post-Selected)</button>
          </div>
          <label class="tp-essay-ctrl">
            <span data-en="Evaporation / barrier step k (N = 6)" data-es="Paso de evaporación / barrera k (N = 6)">Evaporation / barrier step k (N = 6)</span>
            <strong data-cs-read="stepk">k = 3 / 6</strong>
            <input type="range" min="0" max="6" step="1" value="3" data-cs-input="stepk">
          </label>
          <label class="tp-essay-ctrl">
            <span data-en="Per-step absorbing hazard γ (Doob benchmark)" data-es="Riesgo absorbente por paso γ (referencia Doob)">Per-step absorbing hazard γ (Doob benchmark)</span>
            <strong data-cs-read="hazard">γ = 0.25</strong>
            <input type="range" min="0.05" max="0.50" step="0.05" value="0.25" data-cs-input="hazard">
          </label>
          <div class="tp-essay-readout-box">
            <div><span data-en="Radiation Entropy S(k):" data-es="Entropía de Radiación S(k):">Radiation Entropy S(k):</span> <strong data-cs-read="snats">2.079 nats</strong></div>
            <div><span data-en="Doob KL Sampling Cost V_Doob:" data-es="Costo KL de Muestreo V_Doob:">Doob KL Sampling Cost V_Doob:</span> <strong data-cs-read="vdoob">0.000 nats</strong></div>
            <div><span data-en="Trajectory Selection:" data-es="Selección de Trayectorias:">Trajectory Selection:</span> <strong data-cs-read="discard" data-en="0.0% discarded" data-es="0.0 % descartado">0.0% discarded</strong></div>
          </div>
          <button type="button" class="tp-cta" data-cs-knockout aria-pressed="false" data-en="Toggle Ensemble-Conflation Defect" data-es="Alternar Defecto de Confusión de Ensambles">Toggle Ensemble-Conflation Defect</button>
        </div>
      </div>
      <p class="tp-essay-status" data-cs-status role="status"></p>
    </section>"""

    if kind == "wdw_clock":
        svg_aria = (
            "Visibilidad condicionada de Page-Wootters en el núcleo 64x64, negatividad cuántica bajo eco bilateral CPMG y exclusión híbrida a 33 micrómetros"
            if is_es
            else "Conditioned Page-Wootters visibility from the 64x64 nullspace, quantum negativity under bilateral CPMG echo, and 33-micrometre hybrid exclusion"
        )
        grp_aria = "Seleccionar protocolo de eco de espín" if is_es else "Select spin-echo protocol"
        return f"""    <section id="instrument" class="tp-essay-observatory" data-cs-instrument="wdw_clock" aria-labelledby="inst-heading">
      <div class="tp-essay-obs-head">
        <p class="tp-kicker" data-en="Interactive 64×64 Timeless Nullspace &amp; Bilateral Echo Observatory · ES.06" data-es="Observatorio Interactivo de Núcleo Atemporal 64×64 y Eco Bilateral · ES.06">Interactive 64×64 Timeless Nullspace &amp; Bilateral Echo Observatory · ES.06</p>
        <h2 id="inst-heading" class="tp-h2" data-en="Conditioned Clock Visibility, Synchronous X_A ⊗ X_B Echo &amp; 33 µm Hybrid Exclusion" data-es="Visibilidad de Reloj Condicionada, Eco Síncrono X_A ⊗ X_B y Exclusión Híbrida a 33 µm">Conditioned Clock Visibility, Synchronous X_A ⊗ X_B Echo &amp; 33 µm Hybrid Exclusion</h2>
      </div>
      <div class="tp-essay-obs-grid">
        <svg class="tp-essay-svg" viewBox="0 0 560 250" role="img" aria-label="{svg_aria}">
          <rect x="8" y="8" width="544" height="234" rx="10" fill="var(--tp-stone)" stroke="var(--tp-rule)"/>
          <text x="24" y="40" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="1 · Conditioned Zych–Brukner Visibility ⟨t_n|Ψ⟩⟩ from ker(C) (dim 64)" data-es="1 · Visibilidad Condicionada ⟨t_n|Ψ⟩⟩ desde ker(C) (dim 64)">1 · Conditioned Zych–Brukner Visibility ⟨t_n|Ψ⟩⟩ from ker(C) (dim 64)</text>
          <rect x="24" y="50" width="230" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="vis" x="24" y="50" width="8.0" height="18" rx="4" fill="var(--tp-prussian)"/>
          <text data-cs-read="vis" x="268" y="64" fill="var(--tp-ink)" font-family="monospace" font-size="13">V(t_n) = 0.000 · η = 0</text>

          <text x="24" y="114" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="2 · Unitary Quantum BMV Negativity under Quasistatic Gradient Echo" data-es="2 · Negatividad BMV Cuántica Unitaria bajo Eco de Gradiente Cuasiestático">2 · Unitary Quantum BMV Negativity under Quasistatic Gradient Echo</text>
          <rect x="24" y="124" width="230" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="negq" x="24" y="124" width="195.4" height="18" rx="4" fill="var(--tp-verdigris)"/>
          <text data-cs-read="negq" x="268" y="138" fill="var(--tp-ink)" font-family="monospace" font-size="13">N_Q = 0.357</text>

          <text x="24" y="186" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="3 · Classical-Hybrid Smeared Gravity Channel (T.05/T.06 4-Wall Gate)" data-es="3 · Canal Híbrido Clásico de Gravedad Suavizada (Compuerta de 4 Muros)">3 · Classical-Hybrid Smeared Gravity Channel (T.05/T.06 4-Wall Gate)</text>
          <rect x="24" y="196" width="230" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="negh" x="24" y="196" width="8.0" height="18" rx="4" fill="var(--tp-minium)"/>
          <text data-cs-read="negh" x="268" y="210" fill="var(--tp-ink)" font-family="monospace" font-size="13" data-en="N_hyb = 0.000 (σ ≤ 33 µm excluded)" data-es="N_hyb = 0.000 (σ ≤ 33 µm excluido)">N_hyb = 0.000 (σ ≤ 33 µm excluded)</text>
        </svg>
        <div class="tp-essay-controls">
          <div class="tp-essay-btn-stack" role="group" aria-label="{grp_aria}">
            <button type="button" class="tp-cta" data-wdw-echo="bilateral" aria-pressed="true" data-en="Bilateral X_A ⊗ X_B Echo (Preserves Z_A Z_B)" data-es="Eco Bilateral X_A ⊗ X_B (Preserva Z_A Z_B)">Bilateral X_A ⊗ X_B Echo (Preserves Z_A Z_B)</button>
            <button type="button" class="tp-cta" data-wdw-echo="unilateral" aria-pressed="false" data-en="Unilateral X_A ⊗ I Echo (Cancels Z_A Z_B!)" data-es="Eco Unilateral X_A ⊗ I (¡Cancela Z_A Z_B!)">Unilateral X_A ⊗ I Echo (Cancels Z_A Z_B!)</button>
          </div>
          <label class="tp-essay-ctrl">
            <span data-en="Conditioned clock reading n ∈ {{0..15}}" data-es="Lectura condicionada del reloj n ∈ {{0..15}}">Conditioned clock reading n ∈ {{0..15}}</span>
            <strong data-cs-read="tickn">n = 4 (t_n = 0.50π)</strong>
            <input type="range" min="0" max="15" step="1" value="4" data-cs-input="tickn">
          </label>
          <label class="tp-essay-ctrl">
            <span data-en="CPMG π-pulses N_dd against 1/f gradient noise" data-es="Pulsos π CPMG N_dd frente a ruido de gradiente 1/f">CPMG π-pulses N_dd against 1/f gradient noise</span>
            <strong data-cs-read="ndd">N_dd = 4 (γ_eff = 7.50e-4 s⁻¹)</strong>
            <input type="range" min="1" max="8" step="1" value="4" data-cs-input="ndd">
          </label>
          <button type="button" class="tp-cta" data-cs-knockout aria-pressed="false" data-en="Toggle Retired 44 µm / White-Noise Defect" data-es="Alternar Defecto de 44 µm Retirado / Ruido Blanco">Toggle Retired 44 µm / White-Noise Defect</button>
        </div>
      </div>
      <p class="tp-essay-status" data-cs-status role="status"></p>
    </section>"""

    if kind == "parallel_horizon":
        svg_aria = (
            "Ancho crítico híbrido paralelo exacto frente al recast de 33.08 micrómetros, negatividad cuántica criogénica y control nulo ortogonal a 90 grados"
            if is_es
            else "Exact parallel hybrid critical width against the 33.08-micrometre recast, cryogenic quantum negativity, and 90-degree orthogonal null control"
        )
        grp_theta_aria = "Seleccionar ángulo relativo 3-D de Stern-Gerlach" if is_es else "Select 3-D Stern-Gerlach skew angle"
        grp_ens_aria = "Seleccionar ensamble termodinámico de vacío criogénico" if is_es else "Select cryogenic vacuum ensemble"
        return f"""    <section id="instrument" class="tp-essay-observatory" data-cs-instrument="parallel_horizon" aria-labelledby="inst-heading">
      <div class="tp-essay-obs-head">
        <p class="tp-kicker" data-en="Interactive 3-D Parallel Horizon, Cryogenic Valley &amp; 90° Null Observatory · ES.07" data-es="Observatorio Interactivo de Horizonte Paralelo 3-D, Valle Criogénico y Nulo a 90° · ES.07">Interactive 3-D Parallel Horizon, Cryogenic Valley &amp; 90° Null Observatory · ES.07</p>
        <h2 id="inst-heading" class="tp-h2" data-en="Exact Closed-Form Horizon (1.547σ → 2.211σ), D = 75 µm Quantum Island &amp; '+' Null Cross" data-es="Horizonte Cerrado Exacto (1.547σ → 2.211σ), Isla Cuántica en D = 75 µm y Cruz Nula '+'">Exact Closed-Form Horizon (1.547σ → 2.211σ), D = 75 µm Quantum Island &amp; '+' Null Cross</h2>
      </div>
      <div class="tp-essay-obs-grid">
        <svg class="tp-essay-svg" viewBox="0 0 560 260" role="img" aria-label="{svg_aria}">
          <rect x="8" y="8" width="544" height="244" rx="10" fill="var(--tp-stone)" stroke="var(--tp-rule)"/>
          <text x="24" y="40" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="1 · Exact Parallel Hybrid Critical Width σ_c(D, Δx, θ) vs 33.08 µm Recast" data-es="1 · Ancho Crítico Híbrido Paralelo Exacto σ_c(D, Δx, θ) frente a 33.08 µm">1 · Exact Parallel Hybrid Critical Width σ_c(D, Δx, θ) vs 33.08 µm Recast</text>
          <rect x="24" y="50" width="230" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="sigmac" x="24" y="50" width="157.6" height="18" rx="4" fill="var(--tp-prussian)"/>
          <line x1="150.8" y1="45" x2="150.8" y2="73" stroke="var(--tp-minium)" stroke-width="2.2" stroke-dasharray="3 2"/>
          <text data-cs-read="sigmac" x="268" y="64" fill="var(--tp-ink)" font-family="monospace" font-size="12.5">σ_c = 41.12 µm &gt; 33.08 µm</text>

          <text x="24" y="116" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="2 · Unitary Quantum BMV Negativity N_Q(t = 2.5 s) under Cryogenic Bath" data-es="2 · Negatividad BMV Cuántica Unitaria N_Q(t = 2.5 s) en Baño Criogénico">2 · Unitary Quantum BMV Negativity N_Q(t = 2.5 s) under Cryogenic Bath</text>
          <rect x="24" y="126" width="230" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="negq" x="24" y="126" width="205.3" height="18" rx="4" fill="var(--tp-verdigris)"/>
          <text data-cs-read="negq" x="268" y="140" fill="var(--tp-ink)" font-family="monospace" font-size="12.5">N_Q = 0.446 · Δφ = 3.01 rad</text>

          <text x="24" y="192" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="3 · Classical-Hybrid Smeared Channel max_t N_hyb(t) at σ_95 = 33.08 µm" data-es="3 · Canal Híbrido Clásico Difuminado máx_t N_hyb(t) en σ_95 = 33.08 µm">3 · Classical-Hybrid Smeared Channel max_t N_hyb(t) at σ_95 = 33.08 µm</text>
          <rect x="24" y="202" width="230" height="18" rx="4" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect data-cs-bar="negh" x="24" y="202" width="8.0" height="18" rx="4" fill="var(--tp-minium)"/>
          <text data-cs-read="negh" x="268" y="216" fill="var(--tp-ink)" font-family="monospace" font-size="12.5" data-en="N_hyb = 0.0000 (Classically Dark)" data-es="N_hyb = 0.0000 (Clásicamente Oscuro)">N_hyb = 0.0000 (Classically Dark)</text>
        </svg>
        <div class="tp-essay-controls">
          <div class="tp-essay-btn-stack" role="group" aria-label="{grp_theta_aria}">
            <button type="button" class="tp-cta" data-ph-theta="0" aria-pressed="true" data-en="θ = 0° Parallel Arms" data-es="θ = 0° Brazos Paralelos">θ = 0° Parallel Arms</button>
            <button type="button" class="tp-cta" data-ph-theta="45" aria-pressed="false" data-en="θ = 45° Skew Signature" data-es="θ = 45° Firma Sesgada">θ = 45° Skew Signature</button>
            <button type="button" class="tp-cta" data-ph-theta="90" aria-pressed="false" data-en="θ = 90° Midpoint '+' Null Cross" data-es="θ = 90° Cruz Nula '+' Centrada">θ = 90° Midpoint '+' Null Cross</button>
          </div>
          <div class="tp-essay-btn-stack" role="group" aria-label="{grp_ens_aria}">
            <button type="button" class="tp-cta" data-ph-ens="isobaric" aria-pressed="true" data-en="Isobaric P = 2.7×10⁻¹⁶ Pa (2.04 K Valley)" data-es="Isobárico P = 2.7×10⁻¹⁶ Pa (Valle 2.04 K)">Isobaric P = 2.7×10⁻¹⁶ Pa (2.04 K Valley)</button>
            <button type="button" class="tp-cta" data-ph-ens="isochoric" aria-pressed="false" data-en="Sealed Isochoric Cell (n = const)" data-es="Celda Isocórica Sellada (n = const)">Sealed Isochoric Cell (n = const)</button>
          </div>
          <label class="tp-essay-ctrl">
            <span data-en="Parallel centre-to-centre gap D (µm, Casimir floor 28.3 µm)" data-es="Separación paralela centro a centro D (µm, piso Casimir 28.3 µm)">Parallel centre-to-centre gap D (µm, Casimir floor 28.3 µm)</span>
            <strong data-cs-read="gap">D = 75 µm (Island ≥ 73.14 µm)</strong>
            <input type="range" min="35" max="110" step="1" value="75" data-cs-input="gap">
          </label>
          <label class="tp-essay-ctrl">
            <span data-en="Superposition split Δx (µm)" data-es="División de superposición Δx (µm)">Superposition split Δx (µm)</span>
            <strong data-cs-read="split">Δx = 250 µm</strong>
            <input type="range" min="15" max="300" step="5" value="250" data-cs-input="split">
          </label>
          <label class="tp-essay-ctrl">
            <span data-en="Cryogenic bath temperature T (K, m = 10⁻¹⁴ kg)" data-es="Temperatura del baño criogénico T (K, m = 10⁻¹⁴ kg)">Cryogenic bath temperature T (K, m = 10⁻¹⁴ kg)</span>
            <strong data-cs-read="temp">T = 2.0 K (γ = 2.20e-2 s⁻¹)</strong>
            <input type="range" min="0.6" max="3.6" step="0.1" value="2.0" data-cs-input="temp">
          </label>
          <button type="button" class="tp-cta" data-cs-knockout aria-pressed="false" data-en="Toggle Naive 51.2 µm / Uncentred-90° Defect" data-es="Alternar Defecto de 51.2 µm / Esquina 90°">Toggle Naive 51.2 µm / Uncentred-90° Defect</button>
        </div>
      </div>
      <p class="tp-essay-status" data-cs-status role="status"></p>
    </section>"""

    svg_aria = (
        "Cota de la Relación de Incertidumbre Termodinámica en Q_TUR = 2 con punto operativo en vivo"
        if is_es
        else "Thermodynamic Uncertainty Relation bound line at Q_TUR = 2 with live operating point"
    )
    return f"""    <section id="instrument" class="tp-essay-observatory" data-cs-instrument="tur_pores" aria-labelledby="inst-heading">
      <div class="tp-essay-obs-head">
        <p class="tp-kicker" data-en="Interactive Thermodynamic Clock &amp; Barrier Explorer · ES.03" data-es="Explorador Termodinámico de Relojes y Barreras · ES.03">Interactive Thermodynamic Clock &amp; Barrier Explorer · ES.03</p>
        <h2 id="inst-heading" class="tp-h2" data-en="Markovian Clock Precision Bound (Q_TUR ≥ 2) &amp; Kramers Barrier Rescue" data-es="Cota de Precisión en Relojes Markovianos (Q_TUR ≥ 2) y Rescate de Kramers">Markovian Clock Precision Bound (Q_TUR ≥ 2) &amp; Kramers Barrier Rescue</h2>
      </div>
      <div class="tp-essay-obs-grid">
        <svg class="tp-essay-svg" viewBox="0 0 560 260" role="img" aria-label="{svg_aria}">
          <rect x="8" y="8" width="544" height="244" rx="10" fill="var(--tp-stone)" stroke="var(--tp-rule)"/>
          <rect x="60" y="212" width="370" height="30" fill="var(--tp-minium-soft)"/>
          <line x1="60" y1="212" x2="430" y2="212" stroke="var(--tp-minium)" stroke-width="2.5" stroke-dasharray="6 4"/>
          <text x="440" y="216" fill="var(--tp-minium)" font-size="12" font-weight="700">Q_TUR = 2</text>
          <text x="70" y="232" fill="var(--tp-minium)" font-size="11" data-en="Forbidden classical Markovian region (Q_TUR &lt; 2)" data-es="Región markoviana clásica prohibida (Q_TUR &lt; 2)">Forbidden classical Markovian region (Q_TUR &lt; 2)</text>
          <line x1="60" y1="40" x2="60" y2="242" stroke="var(--tp-ink)" stroke-width="1.5"/>
          <circle data-tur-point cx="240.0" cy="160.9" r="9" fill="var(--tp-prussian)" stroke="var(--tp-vellum)" stroke-width="2.5"/>
          <text x="72" y="58" fill="var(--tp-ink)" font-size="12" font-weight="700" data-en="Operating point above universal 2 k_B dissipation floor" data-es="Punto operativo sobre el piso universal de disipación 2 k_B">Operating point above universal 2 k_B dissipation floor</text>
        </svg>
        <div class="tp-essay-controls">
          <label class="tp-essay-ctrl">
            <span data-en="Cycle thermodynamic affinity A (k_B T, e.g. ATP ≈ 20)" data-es="Afinidad termodinámica por ciclo A (k_B T, ej. ATP ≈ 20)">Cycle thermodynamic affinity A (k_B T, e.g. ATP ≈ 20)</span>
            <strong data-cs-read="affinity">20.0 k_B T</strong>
            <input type="range" min="1" max="40" step="1" value="20" data-cs-input="affinity">
          </label>
          <label class="tp-essay-ctrl">
            <span data-en="Markov ring states per tick N_states" data-es="Estados del anillo markoviano por pulso N_states">Markov ring states per tick N_states</span>
            <strong data-cs-read="states">4</strong>
            <input type="range" min="2" max="12" step="1" value="4" data-cs-input="states">
          </label>
          <label class="tp-essay-ctrl">
            <span data-en="Allosteric / thermal barrier reduction ΔΔG‡ (k_B T)" data-es="Reducción de barrera de activación ΔΔG‡ (k_B T)">Allosteric / thermal barrier reduction ΔΔG‡ (k_B T)</span>
            <strong data-cs-read="ddg">3.0 k_B T</strong>
            <input type="range" min="0" max="6" step="0.5" value="3.0" data-cs-input="ddg">
          </label>
          <div class="tp-essay-readout-box">
            <div><span>Q_TUR:</span> <strong data-cs-read="qtur" data-en="5.068 ≥ 2 (PASS)" data-es="5.068 ≥ 2 (PASA)">5.068 ≥ 2 (PASS)</strong></div>
            <div><span data-en="Cycle Fano factor Var(N)/⟨N⟩:" data-es="Factor de Fano cíclico Var(N)/⟨N⟩:">Cycle Fano factor Var(N)/⟨N⟩:</span> <strong data-cs-read="relvar">0.253</strong></div>
            <div><span data-en="Kramers flux multiplier:" data-es="Multiplicador de flujo Kramers:">Kramers flux multiplier:</span> <strong data-cs-read="boost">20.1×</strong></div>
          </div>
          <button type="button" class="tp-cta" data-cs-knockout aria-pressed="false" data-en="Toggle Perpetuum-Mobile Defect" data-es="Alternar Defecto de Móvil Perpetuo">Toggle Perpetuum-Mobile Defect</button>
        </div>
      </div>
      <p class="tp-essay-status" data-cs-status role="status"></p>
    </section>"""


# ---------------------------------------------------------------------------
# Block, Sidenote, Source, Skill, Pager & Hub Renderers
# ---------------------------------------------------------------------------

def render_block(blk: dict) -> str:
    btype = blk["type"]
    if btype == "p":
        return f"        {bi('p', blk['en'], blk['es'])}"
    if btype in ("bridge", "analogy"):
        cls = "tp-plain-bridge-box" if btype == "bridge" else "tp-analogy-box"
        ps = "\n".join(f"          {bi('p', pe, ps_)}" for pe, ps_ in blk["paras"])
        h3 = f"\n          {bi('h3', blk['title_en'], blk['title_es'])}" if blk.get("title_en") else ""
        return f"""        <aside class="{cls}">
          {bi("span", blk["kicker_en"], blk["kicker_es"], "tp-plain-bridge-kicker")}{h3}
{ps}
        </aside>"""
    if btype == "equation":
        return f"""        <div class="tp-essay-eq" role="math" aria-label="{a(blk['label_en'])}">
          {bi("span", blk["label_en"], blk["label_es"], "tp-essay-eq-label")}
          <code class="tp-essay-eq-code">{t(blk["formula"])}</code>
          {bi("p", blk["note_en"], blk["note_es"], "tp-essay-eq-note")}
        </div>"""
    if btype == "table":
        ths = "".join(f'<th scope="col" data-en="{a(he)}" data-es="{a(hs)}">{t(he)}</th>'
                      for he, hs in zip(blk["headers_en"], blk["headers_es"]))
        trs = []
        for row in blk["rows"]:
            tds = []
            for idx, cell in enumerate(row):
                ce, cs = cell if isinstance(cell, (tuple, list)) else (str(cell), str(cell))
                tag = 'th scope="row"' if idx == 0 else "td"
                close = "th" if idx == 0 else "td"
                tds.append(f'<{tag} data-en="{a(ce)}" data-es="{a(cs)}">{t(ce)}</{close}>')
            trs.append("              <tr>" + "".join(tds) + "</tr>")
        trs_html = "\n".join(trs)
        return f"""        <div class="tp-essay-table-wrap">
          <table class="tp-telemetry-benchmark-table">
            <caption data-en="{a(blk['caption_en'])}" data-es="{a(blk['caption_es'])}">{t(blk['caption_en'])}</caption>
            <thead><tr>{ths}</tr></thead>
            <tbody>
{trs_html}
            </tbody>
          </table>
        </div>"""
    raise ValueError(f"Unknown essay block type: {btype!r}")


def render_sections(essay: dict) -> str:
    out = []
    for sec in essay["sections"]:
        blocks = "\n".join(render_block(b) for b in sec["blocks"])
        out.append(
            f"""        <section id="{a(sec['id'])}" class="tp-essay-sec">
          <h2 class="tp-h2" data-en="{a(sec['h2_en'])}" data-es="{a(sec['h2_es'])}">{t(sec['h2_en'])}</h2>
{blocks}
        </section>"""
        )
    return "\n".join(out)


def render_sources(essay: dict) -> str:
    rows = []
    for s in essay["sources"]:
        doi = s["doi"]
        url = f"https://doi.org/{doi}"
        rows.append(
            f"""              <tr>
                <th scope="row"><code>{t(s['id'])}</code></th>
                <td>{t(s['citation'])} ({t(str(s['year']))})</td>
                <td><a href="{a(url)}" target="_blank" rel="noopener noreferrer"><code>{t(doi)}</code></a></td>
                <td data-en="{a(s['role_en'])}" data-es="{a(s['role_es'])}">{t(s['role_en'])}</td>
              </tr>"""
        )
    rows_html = "\n".join(rows)
    return f"""        <section id="sources" class="tp-essay-sec">
          <h2 class="tp-h2" data-en="Primary Sources &amp; Offline DOI Ledger" data-es="Fuentes Primarias y Registro DOI sin Conexión">Primary Sources &amp; Offline DOI Ledger</h2>
          <div class="tp-essay-table-wrap">
            <table class="tp-telemetry-benchmark-table">
              <thead>
                <tr>
                  <th scope="col">ID</th>
                  <th scope="col" data-en="Reference" data-es="Referencia">Reference</th>
                  <th scope="col">DOI</th>
                  <th scope="col" data-en="Role in this Essay" data-es="Papel en este Ensayo">Role in this Essay</th>
                </tr>
              </thead>
              <tbody>
{rows_html}
              </tbody>
            </table>
          </div>
        </section>"""


def render_skill_box(essay: dict, is_es: bool = False) -> str:
    gh_skill = f"https://github.com/senseiewok/informatico.ai/blob/main/{essay['skill_path']}"
    gh_ver = f"https://github.com/senseiewok/informatico.ai/blob/main/{essay['verifier_path']}"
    aria_skill = "SKILL.md portable y verificador en Python" if is_es else "Portable SKILL.md and Python verifier"
    return f"""        <aside class="tp-plain-bridge-box tp-essay-skill-box" aria-label="{aria_skill}">
          {bi("span", "Portable AI SKILL.md & Deterministic Python Verifier", "Compañero SKILL.md Portable y Verificador en Python", "tp-plain-bridge-kicker")}
          {bi("p",
              f"Run `python {essay['verifier_path']}` locally (standard library only, zero network calls) to recompute every equation on this page, and `--planted-defect` to confirm the verifier fails closed when a regime or epistemic rule is broken.",
              f"Ejecuta `python {essay['verifier_path']}` localmente (solo biblioteca estándar, cero red) para recalcular cada ecuación de esta página, y `--planted-defect` para confirmar que el verificador falla en cerrado ante un defecto plantado.")}
          <p class="tp-series-rack-ctas">
            <a class="tp-cta" href="{a(gh_skill)}" target="_blank" rel="noopener noreferrer"><code>{t(essay['skill_path'])}</code> →</a>
            <a class="tp-cta" href="{a(gh_ver)}" target="_blank" rel="noopener noreferrer"><code>{t(essay['verifier_path'])}</code> →</a>
          </p>
        </aside>"""


def render_sidenotes(essay: dict) -> str:
    notes = []
    for sn in essay["sidenotes"]:
        notes.append(
            f"""        <div class="tp-sidenote">
          {bi("strong", sn["label_en"], sn["label_es"], "tp-sidenote-label")}
          {bi("p", sn["en"], sn["es"])}
        </div>"""
        )
    return "\n".join(notes)


def render_essay_cards(essays: list[dict], rel_res: str, is_es: bool = False) -> str:
    cards = []
    for es_doc in essays:
        slug = es_doc["slug"]
        pslug = es_doc["plate_slug"]
        v = plate_hash(pslug)
        href = B._href(rel_res, f"essays/{slug}/")
        img_src = B._href(rel_res, f"plates/{pslug}.png?v={v}")
        alt_txt = es_doc["title_es"] if is_es else es_doc["title_en"]
        cards.append(
            f"""        <a class="tp-rack-card tp-essay-card" href="{a(href)}">
          <span class="tp-rack-thumb-wrap"><img class="tp-essay-thumb" src="{a(img_src)}" alt="{a(alt_txt)}" width="1200" height="630" loading="lazy" decoding="async"></span>
          <span class="tp-rack-top"><span class="tp-rack-id" data-en="{a(es_doc['code'])} · Cross-Scale" data-es="{a(es_doc['code'])} · Entre Escalas">{t(es_doc['code'])} · Cross-Scale</span><span class="tp-rack-badge" data-en="{a(es_doc['reading_time_en'])}" data-es="{a(es_doc['reading_time_es'])}">{t(es_doc['reading_time_en'])}</span></span>
          <strong class="tp-rack-title" data-en="{a(es_doc['title_en'])}" data-es="{a(es_doc['title_es'])}">{t(es_doc['title_en'])}</strong>
          <span class="tp-rack-dek" data-en="{a(es_doc['card_dek_en'])}" data-es="{a(es_doc['card_dek_es'])}">{t(es_doc['card_dek_en'])}</span>
        </a>"""
        )
    return "\n".join(cards)


def render_essay_page(essay: dict, essays: list[dict], catalog: dict, lang: str = "en") -> str:
    is_es = lang == "es"
    slug = essay["slug"]
    path = f"essays/{slug}/"
    rel_root = "../.."
    rel_res = "../.."
    t_en, d_en, t_es, d_es = essay["seo"]
    seo_t = t_es if is_es else t_en
    seo_d = d_es if is_es else d_en
    full_title = seo_t if seo_t.endswith(BRAND) else f"{seo_t} | {BRAND}"
    canon = B.page_url(path, lang)
    pslug = essay["plate_slug"]
    v = plate_hash(pslug)
    image = f"https://informatico.ai/plates/{pslug}.png"
    crumbs = [
        ("Informatico.ai", B.page_url("", lang)),
        ("Ensayos entre Escalas" if is_es else "Cross-Scale Essays", B.page_url("essays/", lang)),
        (essay["code"], canon),
    ]
    ld = B._ld(
        "ScholarlyArticle",
        seo_t,
        seo_d,
        canon,
        lang,
        image=image,
        date_published=essay["date"],
        date_modified=essay["date"],
        crumbs=crumbs,
    )
    head = B.render_head(full_title, seo_d, path, "article", image, rel_root, rel_res, ld, lang)

    jumps = [("#instrument", "Interactive Observatory", "Observatorio Interactivo")]
    for sec in essay["sections"]:
        jumps.append((f"#{sec['id']}", sec["short_en"], sec["short_es"]))
    jumps.append(("#sources", "Sources", "Fuentes"))
    jump_html = "\n".join(
        f'      <a class="tp-essay-jump-pill" href="{a(jh)}" data-en="{a(je)}" data-es="{a(js)}">{t(je)}</a>'
        for jh, je, js in jumps
    )

    idx = next(i for i, e in enumerate(essays) if e["slug"] == slug)
    prev_e = essays[(idx - 1) % len(essays)]
    next_e = essays[(idx + 1) % len(essays)]
    aria_crumb = "Ruta de navegación" if is_es else "Breadcrumb"
    aria_jump = "Secciones del ensayo" if is_es else "Sections of this essay"
    aria_bound = "Límite de investigación no clínica" if is_es else "Non-clinical research boundary"
    aria_essay = "Ensayo" if is_es else "Essay"
    aria_rail = f"Notas al margen de {essay['code']}" if is_es else f"{essay['code']} margin notes"
    aria_pager = "Navegación de ensayos entre escalas" if is_es else "Cross-Scale Essay navigation"
    plate_alt = f"Lámina esquemática de {essay['title_es']}" if is_es else f"{essay['title_en']} schematic diagram"

    return f"""{head}
<body class="tp-body tp-page-folio tp-page-cross-essay">
{B.render_masthead(rel_res, "physics", lang)}
{B.render_contents_dialog(rel_res, catalog, slug)}
  <main id="main" class="tp-shell" tabindex="-1">
    <nav class="tp-breadcrumb-bar" aria-label="{aria_crumb}">
      <ol class="tp-breadcrumb-list">
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="../../">Informatico.ai</a></li>
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="../" data-en="Cross-Scale Essays" data-es="Ensayos entre Escalas">Cross-Scale Essays</a></li>
        <li class="tp-crumb-item" aria-current="page"><span>{t(essay['code'])}</span></li>
      </ol>
    </nav>
    <div id="tp-folio-mount" data-folio-id="{a(essay['code'])}" data-folio-slug="{a(slug)}">
      <section class="tp-hero">
        <p class="tp-kicker">{bi("span", essay["kicker_en"], essay["kicker_es"])} · {bi("span", essay["reading_time_en"], essay["reading_time_es"])}</p>
        <h1 class="tp-h1" data-en="{a(essay['title_en'])}" data-es="{a(essay['title_es'])}">{t(essay['title_en'])}</h1>
        {bi("p", essay["standfirst_en"], essay["standfirst_es"], "tp-standfirst")}
        <div class="tz-dignity-stamp" role="note" aria-label="{aria_bound}">
          <strong data-en="NON-CLINICAL RESEARCH &amp; PHYSICS BOUNDARY" data-es="LÍMITE DE INVESTIGACIÓN FÍSICA NO CLÍNICA">NON-CLINICAL RESEARCH &amp; PHYSICS BOUNDARY</strong>
          {bi("span", BOUNDARY_BANNER_EN, BOUNDARY_BANNER_ES)}
        </div>
      </section>
      <figure class="tp-essay-lead-plate">
        <img src="{rel_res}/plates/{pslug}.png?v={v}" width="1200" height="630" loading="eager" decoding="async" alt="{a(plate_alt)}">
      </figure>
      <nav class="tp-essay-jump-bar" aria-label="{aria_jump}">
{jump_html}
      </nav>
{render_predict_box(essay, is_es=is_es)}
{render_instrument(essay, is_es=is_es)}
      <section class="tp-folio-layout" aria-label="{aria_essay}">
        <div class="tp-prose">
{render_sections(essay)}
          {bi("p", essay["ai_line_en"], essay["ai_line_es"], "tg-ai-line")}
{render_skill_box(essay, is_es=is_es)}
{render_sources(essay)}
        </div>
        <aside class="tp-rail" aria-label="{a(aria_rail)}">
{render_sidenotes(essay)}
        </aside>
      </section>
    </div>
    <nav class="tp-pager" aria-label="{aria_pager}">
      <a class="tp-pager-link tp-pager-prev" href="../{a(prev_e['slug'])}/">
        <span class="tp-pager-dir" data-en="← Companion Essay · {a(prev_e['code'])}" data-es="← Ensayo Compañero · {a(prev_e['code'])}">← Companion Essay · {t(prev_e['code'])}</span>
        <strong class="tp-pager-title" data-en="{a(prev_e['title_en'])}" data-es="{a(prev_e['title_es'])}">{t(prev_e['title_en'])}</strong>
      </a>
      <a class="tp-pager-link tp-pager-next" href="../{a(next_e['slug'])}/">
        <span class="tp-pager-dir" data-en="Next Essay · {a(next_e['code'])} →" data-es="Siguiente Ensayo · {a(next_e['code'])} →">Next Essay · {t(next_e['code'])} →</span>
        <strong class="tp-pager-title" data-en="{a(next_e['title_en'])}" data-es="{a(next_e['title_es'])}">{t(next_e['title_en'])}</strong>
      </a>
    </nav>
    <p class="tp-pager-all">
      <a href="../" data-en="All {len(essays)} Cross-Scale Essays →" data-es="Los {len(essays)} Ensayos entre Escalas →">All {len(essays)} Cross-Scale Essays →</a> ·
      <a href="../../timegravity/" data-en="Time &amp; Gravity (T.00–T.12) →" data-es="Tiempo y Gravedad (T.00–T.12) →">Time &amp; Gravity (T.00–T.12) →</a>
    </p>
{B.render_site_footer(rel_res)}
  </main>
  <script type="module" src="{rel_res}/modules/main.mjs"></script>
  <script type="module" src="{rel_res}/modules/cross-scale-essays.mjs"></script>
</body>
</html>
"""


def render_essays_hub(essays: list[dict], catalog: dict, lang: str = "en") -> str:
    is_es = lang == "es"
    path = "essays/"
    rel_root = ".."
    rel_res = ".."
    t_en, d_en, t_es, d_es = PILLAR_SEO["essays"]
    seo_t = t_es if is_es else t_en
    seo_d = d_es if is_es else d_en
    canon = B.page_url(path, lang)
    image = "https://informatico.ai/plates/essay01.png"
    crumbs = [
        ("Informatico.ai", B.page_url("", lang)),
        ("Ensayos entre Escalas" if is_es else "Cross-Scale Essays", canon),
    ]
    ld = B._ld("CollectionPage", seo_t.replace(f" | {BRAND}", ""), seo_d, canon, lang, image=image, crumbs=crumbs)
    head = B.render_head(seo_t, seo_d, path, "website", image, rel_root, rel_res, ld, lang)
    cards_m1 = render_essay_cards(essays[:3], rel_res, is_es=is_es)
    cards_m2 = render_essay_cards(essays[3:6], rel_res, is_es=is_es)
    cards_m3 = render_essay_cards(essays[6:], rel_res, is_es=is_es)
    aria_crumb = "Ruta de navegación" if is_es else "Breadcrumb"
    aria_rack1 = "Movimiento I: Pisos, Registros y Relojes" if is_es else "Movement I: Floors, Ledgers & Clocks"
    aria_rack2 = "Movimiento II: Celosías, Horizontes y Operadores Atemporales" if is_es else "Movement II: Frames, Horizons & Timeless Operators"
    aria_rack3 = "Movimiento III: Horizontes Paralelos, Islas Cuánticas y Fronteras Epistémicas" if is_es else "Movement III: Parallel Horizons, Quantum Islands & Epistemic Boundaries"

    m2_section = ""
    if essays[3:6]:
        m2_section = f"""
    <section class="tp-issue-rack" aria-label="{aria_rack2}">
      <div class="tp-section-head">
        <p class="tp-kicker" data-en="Movement II · ES.04–ES.06 · Rigidity, Horizons &amp; Coupled Formal Proof" data-es="Movimiento II · ES.04–ES.06 · Rigidez, Horizontes y Prueba Formal Acoplada">Movement II · ES.04–ES.06 · Rigidity, Horizons &amp; Coupled Formal Proof</p>
        <h2 class="tp-h2" data-en="Frames, Horizons, and One Timeless Operator" data-es="Celosías, Horizontes y un Operador Atemporal">Frames, Horizons, and One Timeless Operator</h2>
      </div>
      <div class="tp-rack-grid">
{cards_m2}
      </div>
    </section>"""

    m3_section = ""
    if essays[6:]:
        m3_section = f"""
    <section class="tp-issue-rack" aria-label="{aria_rack3}">
      <div class="tp-section-head">
        <p class="tp-kicker" data-en="Movement III · ES.07 · Parallel Smeared-Gravity Horizons, Cryogenic Valleys &amp; Epistemic Scope" data-es="Movimiento III · ES.07 · Horizontes Paralelos de Gravedad Difuminada, Valles Criogénicos y Alcance Epistémico">Movement III · ES.07 · Parallel Smeared-Gravity Horizons, Cryogenic Valleys &amp; Epistemic Scope</p>
        <h2 class="tp-h2" data-en="The Parallel Horizon, the 75 µm Quantum Island, and Why This Is Not a Theory of Everything" data-es="El Horizonte Paralelo, la Isla Cuántica de 75 µm y por Qué Esto No Es una Teoría del Todo">The Parallel Horizon, the 75 µm Quantum Island, and Why This Is Not a Theory of Everything</h2>
      </div>
      <div class="tp-rack-grid">
{cards_m3}
      </div>
    </section>"""

    return f"""{head}
<body class="tp-body tp-page-hub">
{B.render_masthead(rel_res, "physics", lang)}
{B.render_contents_dialog(rel_res, catalog)}
  <main id="main" class="tp-shell" tabindex="-1">
    <nav class="tp-breadcrumb-bar" aria-label="{aria_crumb}">
      <ol class="tp-breadcrumb-list">
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="../">Informatico.ai</a></li>
        <li class="tp-crumb-item" aria-current="page"><span data-en="Cross-Scale Essays" data-es="Ensayos entre Escalas">Cross-Scale Essays</span></li>
      </ol>
    </nav>
    <section class="tp-hero">
      <p class="tp-kicker" data-en="Featured Synthesis · 7 Standalone Essays · Three Movements &amp; Zero-Sorry Verification" data-es="Síntesis Destacada · 7 Ensayos Independientes · Tres Movimientos y Verificación Formal">Featured Synthesis · 7 Standalone Essays · Three Movements &amp; Zero-Sorry Verification</p>
      <h1 class="tp-h1" data-en="Cross-Scale Essays: Clocks, Stone, and Living Matter" data-es="Ensayos entre Escalas: Relojes, Piedra y Materia Viva">Cross-Scale Essays: Clocks, Stone, and Living Matter</h1>
      <p class="tp-standfirst" data-en="Seven standalone essays in three movements exploring why the exact same mathematical equations and formal verification rules—fluctuation-dissipation, epistemic parent-row provenance, thermodynamic uncertainty, rank–nullity microcausality, Doob conditional survival, coupled timeless constraints, and closed-form parallel horizons—govern 10⁻¹⁴ kg quantum-gravity diamonds, space-frame trusses, black-hole horizons, and nanoscale biological channels." data-es="Siete ensayos independientes en tres movimientos sobre por qué las mismas ecuaciones matemáticas y reglas de verificación formal —fluctuación-disipación, procedencia epistémica, incertidumbre termodinámica, rango-nulidad y microcausalidad, supervivencia condicional de Doob, ligaduras atemporales acopladas y horizontes paralelos cerrados— gobiernan diamantes de gravedad cuántica de 10⁻¹⁴ kg, celosías estructurales, horizontes de agujeros negros y canales biológicos a nanoescala.">Seven standalone essays in three movements exploring why the exact same mathematical equations and formal verification rules—fluctuation-dissipation, epistemic parent-row provenance, thermodynamic uncertainty, rank–nullity microcausality, Doob conditional survival, coupled timeless constraints, and closed-form parallel horizons—govern 10⁻¹⁴ kg quantum-gravity diamonds, space-frame trusses, black-hole horizons, and nanoscale biological channels.</p>
      <div class="tp-series-rack-ctas">
        <a class="tp-cta tp-cta-primary" href="mesoscopic-floor/" data-en="Start Movement I · ES.01 The Mesoscopic Floor →" data-es="Iniciar Movimiento I · ES.01 El Piso Mesoscópico →">Start Movement I · ES.01 The Mesoscopic Floor →</a>
        <a class="tp-cta" href="loophole-free-parallel-horizon/" data-en="Read Capstone · ES.07 The Parallel Horizon &amp; 75 µm Island →" data-es="Leer Cierre · ES.07 El Horizonte Paralelo e Isla de 75 µm →">Read Capstone · ES.07 The Parallel Horizon &amp; 75 µm Island →</a>
        <a class="tp-cta" href="../timegravity/" data-en="Time &amp; Gravity Core Series (T.00–T.12) →" data-es="Serie Principal Tiempo y Gravedad (T.00–T.12) →">Time &amp; Gravity Core Series (T.00–T.12) →</a>
      </div>
    </section>
    <section class="tp-issue-rack" aria-label="{aria_rack1}">
      <div class="tp-section-head">
        <p class="tp-kicker" data-en="Movement I · ES.01–ES.03 · Thermal Baths, Epistemic Ledgers &amp; Markov Clocks" data-es="Movimiento I · ES.01–ES.03 · Baños Térmicos, Registros Epistémicos y Relojes Markovianos">Movement I · ES.01–ES.03 · Thermal Baths, Epistemic Ledgers &amp; Markov Clocks</p>
        <h2 class="tp-h2" data-en="Floors, Ledgers, and Dissipative Clocks" data-es="Pisos, Registros y Relojes Disipativos">Floors, Ledgers, and Dissipative Clocks</h2>
      </div>
      <div class="tp-rack-grid">
{cards_m1}
      </div>
    </section>{m2_section}{m3_section}
{B.render_site_footer(rel_res)}
  </main>
  <script type="module" src="{rel_res}/modules/main.mjs"></script>
</body>
</html>
"""


def load_essays() -> list[dict]:
    from folios.essays import ESSAYS  # noqa: E402
    return list(ESSAYS)


def write_essay_pages(catalog: dict | None = None) -> list[Path]:
    generate_essay_plates()
    essays = load_essays()
    catalog = catalog or B.update_catalogs()
    written: list[Path] = []

    en_hub = RESEARCH / "essays"
    es_hub = RESEARCH / B.ES_PREFIX.strip("/") / "essays"
    en_hub.mkdir(parents=True, exist_ok=True)
    es_hub.mkdir(parents=True, exist_ok=True)
    (en_hub / "index.html").write_text(render_essays_hub(essays, catalog, "en"), encoding="utf-8")
    (es_hub / "index.html").write_text(B.to_spanish_static(render_essays_hub(essays, catalog, "es")), encoding="utf-8")
    written += [en_hub / "index.html", es_hub / "index.html"]

    for es_doc in essays:
        slug = es_doc["slug"]
        en_dir = en_hub / slug
        es_dir = es_hub / slug
        en_dir.mkdir(parents=True, exist_ok=True)
        es_dir.mkdir(parents=True, exist_ok=True)
        (en_dir / "index.html").write_text(render_essay_page(es_doc, essays, catalog, "en"), encoding="utf-8")
        (es_dir / "index.html").write_text(B.to_spanish_static(render_essay_page(es_doc, essays, catalog, "es")), encoding="utf-8")
        written += [en_dir / "index.html", es_dir / "index.html"]
    return written


def main() -> int:
    catalog = B.update_catalogs()
    written = write_essay_pages(catalog)
    (RESEARCH / "index.html").write_text(B.render_hub_index(catalog), encoding="utf-8")
    (RESEARCH / B.ES_PREFIX.strip("/") / "index.html").write_text(B.to_spanish_static(B.render_hub_index(catalog, "es")), encoding="utf-8")
    (RESEARCH / "sitemap.xml").write_text(B.render_research_sitemap(catalog), encoding="utf-8")
    (RESEARCH / "llms.txt").write_text(B.render_llms_txt(catalog), encoding="utf-8")
    print(f"PASS: Built {len(written)} Cross-Scale Essay pages (hub + {len(load_essays())} essays × EN/ES-MX) + {len(load_essays())} PNG plates + cover, sitemap.xml and llms.txt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
