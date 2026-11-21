#!/usr/bin/env python3
"""Independent offline verifier for Folio A.14 (Candela Hypar Ruled Shells & Pucher Membrane Shear).

Standard library only. Recomputes the doubly-ruled hyperbolic paraboloid saddle geometry,
Pucher flat-projection membrane shear resultant N_xy, 45-degree principal membrane stresses
sigma_1 and sigma_2, allowable compressive margin lambda_comp, material volume savings
relative to a 200 mm flat concrete slab, and 4-quadrant umbrella stormwater catchment rate.

Usage:
  python skills/architecture/a14/verify_a14_candela_hypar.py
  python skills/architecture/a14/verify_a14_candela_hypar.py --planted-defect
  python skills/architecture/a14/verify_a14_candela_hypar.py --planted-defect=omit-half

Note: Model calculations for an idealized flat-projection interior membrane with supported
boundaries; omits slope-factor self-weight amplification, cantilevered free-edge bending,
valley/spine rib stress concentration, and thin-shell creep or buckling. Not a building code check.
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PAGES = (
    ROOT / "src" / "architecture" / "a14" / "index.html",
    ROOT / "src" / "es-mx" / "architecture" / "a14" / "index.html",
)

_DEFECT_ARG = next((a for a in sys.argv[1:] if a.startswith("--planted-defect")), "")
DEFECT = (_DEFECT_ARG.split("=", 1)[1] if "=" in _DEFECT_ARG else "omit-half") if _DEFECT_ARG else ""
VALID_DEFECTS = {"", "omit-half", "invert-sign"}


def evaluate_candela_hypar(
    semi_span_a_m: float = 12.0,
    semi_span_b_m: float = 12.0,
    corner_rise_h_m: float = 4.0,
    thickness_mm: float = 40.0,
    concrete_density_kg_m3: float = 2400.0,
    superimposed_load_kn_m2: float = 0.80,
    characteristic_fck_mpa: float = 35.0,
    rainfall_intensity_mm_h: float = 50.0,
    planted_defect: str = "",
) -> dict[str, object]:
    if (
        semi_span_a_m <= 0.0
        or semi_span_b_m <= 0.0
        or corner_rise_h_m <= 0.0
        or thickness_mm <= 0.0
        or characteristic_fck_mpa <= 0.0
    ):
        raise ValueError("All geometric and strength inputs must be strictly positive")

    t_m = thickness_mm / 1000.0
    q_sw_kn_m2 = (concrete_density_kg_m3 * 9.80665 * t_m) / 1000.0
    q_total_kn_m2 = q_sw_kn_m2 + superimposed_load_kn_m2

    twist_c_m = (semi_span_a_m * semi_span_b_m) / corner_rise_h_m
    divisor = 1.0 if planted_defect == "omit-half" else 2.0
    n_xy_kn_m = (q_total_kn_m2 * twist_c_m) / divisor

    sigma_1_mpa = (n_xy_kn_m / t_m) / 1000.0
    sigma_2_mpa = sigma_1_mpa if planted_defect == "invert-sign" else -sigma_1_mpa

    allowable_comp_mpa = 0.45 * characteristic_fck_mpa
    lambda_comp = allowable_comp_mpa / abs(sigma_2_mpa) if abs(sigma_2_mpa) > 1e-12 else 999.0
    volume_savings_pct = (1.0 - t_m / 0.20) * 100.0

    roof_area_m2 = 4.0 * semi_span_a_m * semi_span_b_m
    q_storm_m3_h = roof_area_m2 * (rainfall_intensity_mm_h / 1000.0)
    q_storm_l_s = (q_storm_m3_h / 3600.0) * 1000.0

    return {
        "semi_span_a_m": round(semi_span_a_m, 2),
        "semi_span_b_m": round(semi_span_b_m, 2),
        "corner_rise_h_m": round(corner_rise_h_m, 2),
        "thickness_mm": round(thickness_mm, 1),
        "q_sw_kn_m2": round(q_sw_kn_m2, 3),
        "q_total_kn_m2": round(q_total_kn_m2, 3),
        "twist_c_m": round(twist_c_m, 2),
        "membrane_shear_kn_m": round(n_xy_kn_m, 2),
        "sigma_1_mpa": round(sigma_1_mpa, 3),
        "sigma_2_mpa": round(sigma_2_mpa, 3),
        "lambda_comp": round(lambda_comp, 1),
        "volume_savings_pct": round(volume_savings_pct, 1),
        "roof_area_m2": round(roof_area_m2, 1),
        "stormwater_l_s": round(q_storm_l_s, 1),
        "stormwater_m3_h": round(q_storm_m3_h, 1),
        "comp_safe": lambda_comp >= 3.0,
        "savings_safe": volume_savings_pct >= 75.0,
    }


def check_html_readouts(ref: dict[str, object]) -> list[str]:
    errs: list[str] = []
    expected_tokens = (
        f"{ref['membrane_shear_kn_m']:.2f} kN/m",
        f"{ref['sigma_2_mpa']:.3f} MPa",
        f"λ_comp = {ref['lambda_comp']:.1f}",
        f"{ref['volume_savings_pct']:.1f}%",
        f"{ref['stormwater_l_s']:.1f} L/s",
        f"{ref['stormwater_m3_h']:.1f} m³/h",
        f"{int(round(float(ref['roof_area_m2'])))} m²",
    )
    for page in PAGES:
        if not page.is_file():
            errs.append(f"Missing built HTML page: {page.relative_to(ROOT).as_posix()}")
            continue
        txt = page.read_text(encoding="utf-8")
        strip = re.search(r'<div class="tp-readout-strip".*?</div>\s*</div>', txt, re.S)
        scope = strip.group(0) if strip else txt
        for tok in expected_tokens:
            if tok not in scope:
                errs.append(f"{page.relative_to(ROOT).as_posix()} missing readout token {tok!r}")
    return errs


def main() -> int:
    if DEFECT not in VALID_DEFECTS:
        print(json.dumps({"status": "FAIL", "error": f"Unknown planted defect {DEFECT!r}; expected one of {sorted(VALID_DEFECTS - {''})}"}))
        return 1
    ref = evaluate_candela_hypar(planted_defect=DEFECT)
    shallow_neg = evaluate_candela_hypar(corner_rise_h_m=0.10, planted_defect=DEFECT)
    half_rise = evaluate_candela_hypar(corner_rise_h_m=2.0, planted_defect=DEFECT)
    half_span = evaluate_candela_hypar(semi_span_a_m=6.0, semi_span_b_m=6.0, planted_defect=DEFECT)

    failures: list[str] = []

    if ref["q_total_kn_m2"] != 1.741:
        failures.append(f"Expected q_total=1.741 kN/m^2, got {ref['q_total_kn_m2']}")
    if ref["membrane_shear_kn_m"] != 31.35:
        failures.append(f"Expected N_xy=31.35 kN/m, got {ref['membrane_shear_kn_m']}")
    if ref["sigma_1_mpa"] != 0.784:
        failures.append(f"Expected sigma_1=+0.784 MPa, got {ref['sigma_1_mpa']}")
    if ref["sigma_2_mpa"] != -0.784:
        failures.append(f"Expected sigma_2=-0.784 MPa, got {ref['sigma_2_mpa']}")
    if ref["lambda_comp"] != 20.1:
        failures.append(f"Expected lambda_comp=20.1, got {ref['lambda_comp']}")
    if ref["volume_savings_pct"] != 80.0:
        failures.append(f"Expected volume_savings_pct=80.0, got {ref['volume_savings_pct']}")
    if ref["stormwater_l_s"] != 8.0 or ref["stormwater_m3_h"] != 28.8:
        failures.append(f"Expected Q_storm=8.0 L/s (28.8 m^3/h), got {ref['stormwater_l_s']} L/s")

    # Inverse-rise scaling invariant: halving rise h from 4.0 m to 2.0 m must double N_xy.
    rise_ratio = float(half_rise["membrane_shear_kn_m"]) / max(float(ref["membrane_shear_kn_m"]), 1e-9)
    if abs(rise_ratio - 2.0) > 0.01:
        failures.append(f"Inverse-rise scaling violated: h=2m/h=4m ratio={rise_ratio:.4f} != 2.0")

    # Quadratic square-span scaling invariant: doubling a=b from 6.0 m to 12.0 m must quadruple N_xy.
    span_ratio = float(ref["membrane_shear_kn_m"]) / max(float(half_span["membrane_shear_kn_m"]), 1e-9)
    if abs(span_ratio - 4.0) > 0.01:
        failures.append(f"Quadratic span scaling violated: 12m/6m ratio={span_ratio:.4f} != 4.0")

    # Negative control: shallow rise h = 0.10 m must fail lambda_comp >= 3.0.
    if bool(shallow_neg["comp_safe"]) or float(shallow_neg["lambda_comp"]) >= 3.0:
        failures.append(f"Negative control h=0.10 m unexpectedly passed: lambda_comp={shallow_neg['lambda_comp']}")

    # Sign consistency: principal compression sigma_2 must be negative.
    if float(ref["sigma_2_mpa"]) >= 0.0:
        failures.append(f"Principal compressive stress sign error: sigma_2={ref['sigma_2_mpa']} >= 0")

    failures.extend(check_html_readouts(ref))

    payload = {
        "status": "FAIL" if failures else "PASS",
        "folio_id": "A.14",
        "planted_defect": DEFECT or None,
        "reference_umbrella": ref,
        "negative_control_shallow_rise": shallow_neg,
        "inverse_rise_ratio": round(rise_ratio, 4),
        "quadratic_span_ratio": round(span_ratio, 4),
        "failures": failures,
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
