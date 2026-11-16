#!/usr/bin/env python3
"""Verify CC.02 · Stereotomy & Mechanics Lab (La Sagrada Família): hyperboloids, catenaries, twisted columns, PT stone.

Standard library only. Reads MODEL inputs from cc02_mechanics.py, independently re-derives every surface, integral,
cross-section, and stress metric, and verifies every table cell printed on both the EN and ES-MX pages.

  python skills/classics/cc02/verify_cc02_sagrada.py                                -> exit 0 and PASS
  python skills/classics/cc02/verify_cc02_sagrada.py --planted-defect               -> exit 1 (non-tangent ruling)
  python skills/classics/cc02/verify_cc02_sagrada.py --planted-defect=parabola-catenary | twist-pinch | unprestressed-wind
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from folios.classics import cc02_mechanics as M  # noqa: E402  (inputs only; formulas are re-derived here)

PINNED_SHA256 = "e40e2077ad9a52c0d77f4029a93a2d51c7b99bf8cdef48d055f9572d0df7674c"
PAGES = (
    ROOT / "src" / "classics" / "sagrada-familia" / "index.html",
    ROOT / "src" / "es-mx" / "classics" / "sagrada-familia" / "index.html",
)

FLAG_ARG = next((arg for arg in sys.argv[1:] if arg.startswith("--planted-defect")), "")
DEFECT = (FLAG_ARG.split("=", 1)[1] if "=" in FLAG_ARG else "non-tangent-ruling") if FLAG_ARG else ""


def canonical_inputs() -> bytes:
    payload = {
        "hyperboloid": M.HYPERBOLOID_MODEL,
        "funicular": M.FUNICULAR_MODEL,
        "column": M.COLUMN_MODEL,
        "tiers": [list(r) for r in M.COLUMN_TIERS],
        "towers": [list(r) for r in M.TOWERS_LEDGER],
        "panel": M.TOWER_PANEL_MODEL,
    }
    return json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")


# ------------------------------------------------------------------------------------------- 1. Hyperboloid rulings ---
def ruling_point(u: float, v: float, family: int, hm: dict, planted: str = DEFECT) -> tuple[float, float, float]:
    s = 1.0 if family >= 0 else -1.0
    if planted == "non-tangent-ruling":
        # Defect: fail to shift orthogonally in tangent plane (wrong radial factor breaks quadric identity)
        x = hm["a_m"] * (math.cos(u) + 0.35 * s * v * math.cos(u))
        y = hm["b_m"] * (math.sin(u) - 0.35 * s * v * math.sin(u))
    else:
        x = hm["a_m"] * (math.cos(u) - s * v * math.sin(u))
        y = hm["b_m"] * (math.sin(u) + s * v * math.cos(u))
    z = hm["c_m"] * v
    return x, y, z


def check_hyperboloid(hm: dict) -> tuple[dict, list[str]]:
    errs: list[str] = []
    v_lim = hm["v_max"]
    max_res = 0.0
    max_collinear = 0.0
    for fam in (1, -1):
        for k in range(12):
            u = (k / 12.0) * 2.0 * math.pi
            p_neg = ruling_point(u, -v_lim, fam, hm)
            p_zero = ruling_point(u, 0.0, fam, hm)
            p_pos = ruling_point(u, v_lim, fam, hm)
            collinear = math.sqrt(sum((p_neg[j] + p_pos[j] - 2.0 * p_zero[j]) ** 2 for j in range(3)))
            max_collinear = max(max_collinear, collinear)
            for p in (p_neg, p_zero, p_pos):
                res = abs((p[0] / hm["a_m"]) ** 2 + (p[1] / hm["b_m"]) ** 2 - (p[2] / hm["c_m"]) ** 2 - 1.0)
                max_res = max(max_res, res)
    if max_res > 1e-12:
        errs.append(f"hyperboloid quadric residual {max_res:.3e} exceeds 1e-12 along ruling")
    if max_collinear > 1e-12:
        errs.append(f"hyperboloid ruling non-collinear error {max_collinear:.3e} m")

    area_throat = math.pi * hm["a_m"] * hm["b_m"]
    scale = math.sqrt(1.0 + v_lim * v_lim)
    area_top = math.pi * (hm["a_m"] * scale) * (hm["b_m"] * scale)
    pitch_deg = math.degrees(math.atan2(hm["c_m"], hm["a_m"]))
    return {
        "area_throat": area_throat,
        "area_top": area_top,
        "ratio": area_top / area_throat,
        "pitch_deg": pitch_deg,
        "max_residual": max_res,
    }, errs


# ----------------------------------------------------------------------------------- 2. Funicular Simpson quadrature ---
def arch_profile(x_m: float, lantern_kn: float, fm: dict, planted: str = DEFECT) -> tuple[float, float]:
    """Return (elevation y(x), slope dy/dx) using self-weight catenary or defective parabola substitute."""
    span = fm["span_m"]
    a = fm["catenary_a_m"]
    w = fm["w_kn_per_m"]
    h_kn = w * a
    alpha0 = math.asinh(lantern_kn / (2.0 * h_kn)) if lantern_kn > 0.0 else 0.0
    rise = a * (math.cosh(span / (2.0 * a) + alpha0) - math.cosh(alpha0))
    if planted == "parabola-catenary":
        y = rise * (1.0 - (2.0 * x_m / span) ** 2)
        dydx = -rise * (8.0 * abs(x_m)) / (span * span)
        return y, dydx
    y = a * (math.cosh(span / (2.0 * a) + alpha0) - math.cosh(abs(x_m) / a + alpha0))
    dydx = -math.sinh(abs(x_m) / a + alpha0)
    return y, dydx


def simpson_half_arc(lantern_kn: float, fm: dict, n_steps: int = 400, planted: str = DEFECT) -> float:
    half_span = fm["span_m"] * 0.5
    h_step = half_span / n_steps
    total = 0.0
    for i in range(n_steps + 1):
        x = i * h_step
        _y, dydx = arch_profile(x, lantern_kn, fm, planted)
        ds = math.sqrt(1.0 + dydx * dydx)
        coeff = 1.0 if (i == 0 or i == n_steps) else (4.0 if i % 2 == 1 else 2.0)
        total += coeff * ds
    return (h_step / 3.0) * total


def check_funicular(fm: dict) -> tuple[dict[int, dict], float, list[str]]:
    errs: list[str] = []
    span = fm["span_m"]
    a = fm["catenary_a_m"]
    w = fm["w_kn_per_m"]
    h_kn = w * a

    rows: dict[int, dict] = {}
    for w_top in (0.0, fm["lantern_load_kn"], fm["lantern_max_kn"]):
        half_arc = simpson_half_arc(w_top, fm)
        _y0, dydx_spring = arch_profile(span * 0.5, w_top, fm)
        v_reaction = -h_kn * dydx_spring
        v_weight = w * half_arc + 0.5 * w_top
        if abs(v_reaction - v_weight) > 1e-2:
            errs.append(f"vertical equilibrium broken at W_top={w_top}: H*|y'|={v_reaction:.3f} vs w*s+W/2={v_weight:.3f}")
        rise, dydx_crown = arch_profile(1e-9, w_top, fm)
        tilt_deg = math.degrees(math.atan2(h_kn, v_reaction))
        kink_deg = 2.0 * math.degrees(math.atan2(-dydx_crown, 1.0)) if w_top > 0.0 else 0.0
        rows[int(w_top)] = {
            "h_kn": h_kn,
            "v_kn": v_reaction,
            "rise_m": rise,
            "tilt_deg": tilt_deg,
            "kink_deg": kink_deg,
        }

    # Unloaded equal-span, equal-rise parabola vs catenary max vertical gap (mm)
    rise0 = a * (math.cosh(span / (2.0 * a)) - 1.0)
    gap_mm = 0.0
    for i in range(401):
        x = (span * 0.5) * (i / 400.0)
        yc, _ = arch_profile(x, 0.0, fm)
        yp = rise0 * (1.0 - (2.0 * x / span) ** 2)
        gap_mm = max(gap_mm, abs(yc - yp) * 1000.0)
    if gap_mm < 50.0:
        errs.append(f"unloaded catenary-parabola gap collapsed to {gap_mm:.2f} mm")
    return rows, gap_mm, errs


# ------------------------------------------------------------------------------------ 3. Star columns & Montjuïc ---
def star_r(psi: float, n: int, r_in: float, ratio: float) -> float:
    r_out = r_in * ratio
    sector = 2.0 * math.pi / n
    half = math.pi / n
    phi = abs(((psi + half) % sector) - half)
    return (r_out * r_in * math.sin(half)) / (r_in * math.sin(half) * math.cos(phi) + (r_out - r_in * math.cos(half)) * math.sin(phi))


def column_metrics(n: int, d_in: float, load_kn: float, z_frac: float, cm: dict, planted: str = DEFECT) -> dict:
    r_in = d_in * 0.5
    twist = (math.pi / (2.0 * n)) * z_frac
    sign_b = 1.0 if planted == "twist-pinch" else -1.0  # co-rotating twist defect eliminates intersection narrowing
    steps = 1440
    dphi = (2.0 * math.pi) / steps
    area_gross = 0.0
    for i in range(steps):
        phi = (i + 0.5) * dphi
        ra = star_r(phi - twist, n, r_in, cm["star_tip_ratio"])
        rb = star_r(phi - sign_b * twist, n, r_in, cm["star_tip_ratio"])
        rc = min(ra, rb)
        area_gross += 0.5 * rc * rc * dphi
    r_void = r_in * cm["duct_radius_frac"]
    area_net = area_gross - math.pi * r_void * r_void
    stress_mpa = (load_kn / area_net) / 1000.0
    return {
        "h_total": 2.0 * n,
        "h_shaft": 10.0 * d_in,
        "area_net": area_net,
        "stress_mpa": stress_mpa,
    }


def check_columns_and_skyline(cm: dict) -> tuple[dict[int, tuple[dict, dict]], list[str]]:
    errs: list[str] = []
    out: dict[int, tuple[dict, dict]] = {}
    for n, _se, _ss, _pe, _ps, d_in, load_kn in M.COLUMN_TIERS:
        s0 = column_metrics(n, d_in, load_kn, 0.0, cm)
        s1 = column_metrics(n, d_in, load_kn, 1.0, cm)
        if not (0.0 < s1["area_net"] < s0["area_net"] - 1e-4):
            errs.append(f"{n}-pt column twist failed strict section narrowing: A(1)={s1['area_net']:.4f} vs A(0)={s0['area_net']:.4f}")
        out[n] = (s0, s1)

    heights = {row[0]: row[2] for row in M.TOWERS_LEDGER}
    if abs((heights["Montjuïc Hill (datum)"] - heights["Jesus Christ (2026)"]) - 5.2) > 1e-6:
        errs.append("Montjuïc headroom datum mismatch against 172.5 m Tower of Jesus Christ")
    if not (heights["Ulm Minster (reference)"] < heights["Jesus Christ (2026)"] < heights["Montjuïc Hill (datum)"]):
        errs.append("tower skyline ordering violated")
    return out, errs


# ------------------------------------------------------------------------------------ 4. Post-tensioned stone panel ---
def panel_stress(f_pt_kn: float, q_wind_kpa: float, tp: dict, planted: str = DEFECT) -> dict:
    effective_fpt = 0.0 if (planted == "unprestressed-wind" and f_pt_kn > 0.0) else f_pt_kn
    b, t, h = tp["width_m"], tp["thickness_m"], tp["height_m"]
    a_net = b * t - tp["n_ducts"] * math.pi * (tp["duct_radius_m"] ** 2)
    i_net = (b * (t ** 3)) / 12.0 - tp["n_ducts"] * (math.pi * (tp["duct_radius_m"] ** 4) / 4.0)
    z_net = i_net / (t * 0.5)
    m_wind = 0.5 * q_wind_kpa * b * (h ** 2)
    s_ax = ((effective_fpt + tp["dead_load_kn"]) / a_net) / 1000.0
    s_bend = (m_wind / z_net) / 1000.0
    return {
        "m_wind_knm": m_wind,
        "sigma_min": s_ax - s_bend,
        "sigma_max": s_ax + s_bend,
    }


def check_panel(tp: dict) -> tuple[dict[int, dict], list[str]]:
    errs: list[str] = []
    q_wind = tp["wind_kpa"]
    r_zero = panel_stress(0.0, q_wind, tp)
    r_pt = panel_stress(tp["prestress_kn"], q_wind, tp)
    if r_zero["sigma_min"] >= 0.0:
        errs.append(f"unprestressed joint expected to decompress below 0 MPa, got {r_zero['sigma_min']:.3f}")
    if r_pt["sigma_min"] < 0.0:
        errs.append(f"post-tensioned joint failed compression requirement: sigma_min = {r_pt['sigma_min']:.3f} MPa")
    return {0: r_zero, int(tp["prestress_kn"]): r_pt}, errs


# ------------------------------------------------------------------------------------ Page DOM value cross-checks ----
def check_pages(hyp: dict, fun_rows: dict[int, dict], gap_mm: float,
                cols: dict[int, tuple[dict, dict]], pt: dict[int, dict]) -> list[str]:
    errs: list[str] = []
    for page in PAGES:
        if not page.is_file():
            errs.append(f"missing HTML page {page.relative_to(ROOT).as_posix()}")
            continue
        html = page.read_text(encoding="utf-8")
        rel = page.relative_to(ROOT).as_posix()

        # Hyperboloid scalars
        m_th = re.search(r'data-hyp-throat>([\d.]+) m²<', html)
        m_tp = re.search(r'data-hyp-top>([\d.]+) m²<', html)
        m_rt = re.search(r'data-hyp-ratio>([\d.]+)×<', html)
        m_pt = re.search(r'data-hyp-pitch>([\d.]+)°<', html)
        if not (m_th and m_tp and m_rt and m_pt):
            errs.append(f"{rel}: missing hyperboloid readout attributes")
        else:
            if (abs(float(m_th.group(1)) - round(hyp["area_throat"], 2)) > 0.02
                    or abs(float(m_tp.group(1)) - round(hyp["area_top"], 2)) > 0.02
                    or abs(float(m_rt.group(1)) - round(hyp["ratio"], 4)) > 1e-3
                    or abs(float(m_pt.group(1)) - round(hyp["pitch_deg"], 2)) > 0.02):
                errs.append(f"{rel}: hyperboloid metrics mismatch against recomputation")

        # Funicular table rows
        for w_key, fr in fun_rows.items():
            mrow = re.search(rf'<tr data-lantern-kn="{w_key}">(.*?)</tr>', html, re.S)
            if not mrow:
                errs.append(f"{rel}: missing funicular row W_top={w_key}")
                continue
            nums = [float(x) for x in re.findall(r'<td[^>]*>([-+\d.]+)\s*(?:kN|m|°)<', mrow.group(1))]
            want = [fr["h_kn"], fr["v_kn"], fr["rise_m"], fr["tilt_deg"], fr["kink_deg"]]
            if len(nums) != 5 or any(abs(a - b) > 0.02 for a, b in zip(nums, want)):
                errs.append(f"{rel}: funicular row {w_key} shows {nums}, recomputed {[round(x, 2) for x in want]}")

        mgap = re.search(r'class="sf-cat-gap-mm">([\d.]+) mm<', html)
        if not mgap or abs(float(mgap.group(1)) - gap_mm) > 0.25:
            errs.append(f"{rel}: catenary-parabola gap mismatch vs {gap_mm:.1f} mm")

        # Star column rows
        for n_key, (s0, s1) in cols.items():
            crow = re.search(rf'<tr data-col-n="{n_key}">(.*?)</tr>', html, re.S)
            if not crow:
                errs.append(f"{rel}: missing star column row n={n_key}")
                continue
            nums = [float(x) for x in re.findall(r'>([-+\d.]+)\s*(?:m|m²|MPa)<', crow.group(1))]
            want = [s0["h_total"], s0["h_shaft"], s0["area_net"], s1["area_net"], s0["stress_mpa"], s1["stress_mpa"]]
            if len(nums) != 6 or any(abs(a - b) > 0.02 for a, b in zip(nums, want)):
                errs.append(f"{rel}: star column n={n_key} shows {nums}, recomputed {[round(x, 4) for x in want]}")

        # PT panel rows
        for f_key, pr in pt.items():
            prow = re.search(rf'<tr data-pt-kn="{f_key}">(.*?)</tr>', html, re.S)
            if not prow:
                errs.append(f"{rel}: missing PT panel row F_pt={f_key}")
                continue
            nums = [float(x) for x in re.findall(r'>([-+\d.]+)\s*(?:kN·m|MPa)<', prow.group(1))]
            want = [pr["m_wind_knm"], pr["sigma_min"], pr["sigma_max"]]
            if len(nums) != 3 or any(abs(a - b) > 0.01 for a, b in zip(nums, want)):
                errs.append(f"{rel}: PT row F_pt={f_key} shows {nums}, recomputed {[round(x, 3) for x in want]}")

    return errs


def main() -> int:
    fails: list[str] = []
    digest = hashlib.sha256(canonical_inputs()).hexdigest()
    if digest != PINNED_SHA256:
        fails.append(f"data pin mismatch: {digest} != {PINNED_SHA256}")

    hyp, h_errs = check_hyperboloid(M.HYPERBOLOID_MODEL)
    fun_rows, gap_mm, f_errs = check_funicular(M.FUNICULAR_MODEL)
    cols, c_errs = check_columns_and_skyline(M.COLUMN_MODEL)
    pt_rows, p_errs = check_panel(M.TOWER_PANEL_MODEL)
    page_errs = check_pages(hyp, fun_rows, gap_mm, cols, pt_rows)

    fails.extend(h_errs + f_errs + c_errs + p_errs + page_errs)
    status = "FAIL" if fails else "PASS"
    print(json.dumps({
        "verifier": "cc02-sagrada-stereotomy",
        "status": status,
        "defect": DEFECT or None,
        "failures": fails,
        "hyp_max_residual": hyp["max_residual"],
        "tilt_160kn_deg": round(fun_rows[160]["tilt_deg"], 2),
        "catenary_gap_mm": round(gap_mm, 1),
        "porphyry_sigma_top_mpa": round(cols[12][1]["stress_mpa"], 2),
        "pt_sigma_min_mpa": round(pt_rows[1200]["sigma_min"], 3),
    }, ensure_ascii=False))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
