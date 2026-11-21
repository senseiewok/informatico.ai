#!/usr/bin/env python3
"""Independent offline verifier for Folio A.13 (Isler-Inspired Thin Spherical Cap Buckling Model).

Standard library only. Recomputes the idealized spherical-cap geometry, uniform-projection
membrane stress, Zoelly (1915) classical elastic buckling pressure, and an illustrative
empirical-style imperfection knockdown curve inspired by NASA SP-8007 and Dulacska.

Usage:
  python skills/architecture/a13/verify_a13_isler_buckling.py
  python skills/architecture/a13/verify_a13_isler_buckling.py --planted-defect
  python skills/architecture/a13/verify_a13_isler_buckling.py --planted-defect=no-knockdown

Note: These are model calculations for an idealized spherical cap, not a structural code check
or engineering sign-off for any physical building.
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PAGES = (
    ROOT / "src" / "architecture" / "a13" / "index.html",
    ROOT / "src" / "es-mx" / "architecture" / "a13" / "index.html",
)

_DEFECT_ARG = next((a for a in sys.argv[1:] if a.startswith("--planted-defect")), "")
DEFECT = (_DEFECT_ARG.split("=", 1)[1] if "=" in _DEFECT_ARG else "linear-scaling") if _DEFECT_ARG else ""


def spherical_cap_radius_m(span_m: float, rise_m: float) -> float:
    return (span_m ** 2 + 4.0 * (rise_m ** 2)) / (8.0 * rise_m)


def zoelly_classical_pressure_kn_m2(
    elastic_modulus_gpa: float,
    poisson_ratio: float,
    thickness_m: float,
    radius_m: float,
) -> float:
    c_factor = 1.0 / math.sqrt(3.0 * (1.0 - poisson_ratio ** 2))
    e_kpa = elastic_modulus_gpa * 1e6
    ratio = thickness_m / radius_m
    exponent = 1 if DEFECT == "linear-scaling" else 2
    return 2.0 * c_factor * e_kpa * (ratio ** exponent)


def illustrative_knockdown_gamma(radius_m: float, thickness_m: float) -> float:
    if DEFECT == "no-knockdown":
        return 1.0
    r_over_t = radius_m / thickness_m
    return 0.14 + 0.32 * math.exp(-0.1 * math.sqrt(r_over_t))


def evaluate_isler_spherical_cap(
    span_m: float = 31.6,
    rise_m: float = 4.2,
    thickness_mm: float = 90.0,
    elastic_modulus_gpa: float = 30.0,
    poisson_ratio: float = 0.20,
    concrete_density_kg_m3: float = 2400.0,
    superimposed_load_kn_m2: float = 1.20,
) -> dict[str, object]:
    t_m = thickness_mm / 1000.0
    radius_m = spherical_cap_radius_m(span_m, rise_m)
    phi0_rad = math.asin((span_m / 2.0) / radius_m)
    rim_secant = 1.0 / math.cos(phi0_rad)

    q_sw_kn_m2 = (concrete_density_kg_m3 * 9.80665 * t_m) / 1000.0
    q_total_kn_m2 = q_sw_kn_m2 + superimposed_load_kn_m2
    sigma_mem_mpa = ((q_total_kn_m2 * radius_m) / (2.0 * t_m)) / 1000.0

    p_cl_kn_m2 = zoelly_classical_pressure_kn_m2(
        elastic_modulus_gpa, poisson_ratio, t_m, radius_m
    )
    gamma_kd = illustrative_knockdown_gamma(radius_m, t_m)
    p_act_kn_m2 = gamma_kd * p_cl_kn_m2
    lambda_b = p_act_kn_m2 / q_total_kn_m2

    return {
        "span_m": round(span_m, 2),
        "rise_m": round(rise_m, 2),
        "thickness_mm": round(thickness_mm, 1),
        "radius_m": round(radius_m, 2),
        "edge_half_angle_deg": round(math.degrees(phi0_rad), 1),
        "rim_secant": round(rim_secant, 3),
        "q_sw_kn_m2": round(q_sw_kn_m2, 3),
        "q_total_kn_m2": round(q_total_kn_m2, 3),
        "membrane_stress_mpa": round(sigma_mem_mpa, 3),
        "classical_buckling_kpa": round(p_cl_kn_m2, 1),
        "knockdown_gamma": round(gamma_kd, 3),
        "actual_buckling_kpa": round(p_act_kn_m2, 1),
        "buckling_ratio_lambda": round(lambda_b, 1),
        "thickness_ratio_vs_450mm_pct": round((1.0 - t_m / 0.45) * 100.0, 1),
    }


def check_html_readouts(ref: dict[str, object]) -> list[str]:
    errs: list[str] = []
    expected_tokens = (
        f"{ref['membrane_stress_mpa']:.3f} MPa",
        f"{ref['classical_buckling_kpa']:.1f} kN/m²",
        f"{ref['knockdown_gamma']:.3f}",
        f"{ref['actual_buckling_kpa']:.1f} kN/m²",
        f"{ref['buckling_ratio_lambda']:.1f}",
    )
    for page in PAGES:
        if not page.is_file():
            continue
        txt = page.read_text(encoding="utf-8")
        strip = re.search(r'<div class="tp-readout-strip".*?</div>\s*</div>', txt, re.S)
        scope = strip.group(0) if strip else txt
        for tok in expected_tokens:
            if tok not in scope:
                errs.append(f"{page.relative_to(ROOT).as_posix()} missing readout token {tok!r}")
    return errs


def main() -> int:
    ref = evaluate_isler_spherical_cap()
    thin_neg = evaluate_isler_spherical_cap(thickness_mm=15.0)
    t60 = evaluate_isler_spherical_cap(thickness_mm=60.0)
    t120 = evaluate_isler_spherical_cap(thickness_mm=120.0)

    failures: list[str] = []

    if ref["radius_m"] != 31.82:
        failures.append(f"Expected R=31.82 m, got {ref['radius_m']}")
    if ref["membrane_stress_mpa"] != 0.587:
        failures.append(f"Expected sigma_mem=0.587 MPa, got {ref['membrane_stress_mpa']}")
    if ref["classical_buckling_kpa"] != 282.9:
        failures.append(f"Expected p_cl=282.9 kN/m^2, got {ref['classical_buckling_kpa']}")
    if ref["knockdown_gamma"] != 0.189:
        failures.append(f"Expected gamma_kd=0.189, got {ref['knockdown_gamma']}")
    if ref["actual_buckling_kpa"] != 53.4:
        failures.append(f"Expected p_act=53.4 kN/m^2, got {ref['actual_buckling_kpa']}")
    if ref["buckling_ratio_lambda"] != 16.1:
        failures.append(f"Expected lambda_b=16.1, got {ref['buckling_ratio_lambda']}")

    # Quadratic (t/R)^2 scaling invariant: doubling thickness from 60 mm to 120 mm must quadruple p_cl.
    scale_ratio = float(t120["classical_buckling_kpa"]) / max(float(t60["classical_buckling_kpa"]), 1e-9)
    if abs(scale_ratio - 4.0) > 0.05:
        failures.append(f"Zoelly quadratic thickness scaling violated: 120mm/60mm ratio={scale_ratio:.3f} != 4.0")

    # Monotonicity: thinner shells (higher R/t) must have strictly lower knockdown factor gamma_kd.
    if not (float(thin_neg["knockdown_gamma"]) < float(t60["knockdown_gamma"]) < float(ref["knockdown_gamma"])):
        failures.append("Knockdown monotonicity violated: thinner shells did not receive lower gamma_kd")

    # Negative control: 15 mm shell at R=31.82 m must drop below lambda_b = 3.0.
    if float(thin_neg["buckling_ratio_lambda"]) >= 3.0:
        failures.append(
            f"Negative control failed: 15 mm shell stayed at lambda_b={thin_neg['buckling_ratio_lambda']} >= 3.0"
        )

    failures.extend(check_html_readouts(ref))

    ok = len(failures) == 0
    payload = {
        "status": "PASS" if ok else "FAIL",
        "folio_id": "A.13",
        "planted_defect": DEFECT or None,
        "reference_90mm": ref,
        "negative_control_15mm": thin_neg,
        "zoelly_doubling_ratio": round(scale_ratio, 3),
        "failures": failures,
    }
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
