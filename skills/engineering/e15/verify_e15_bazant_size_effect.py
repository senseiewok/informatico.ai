#!/usr/bin/env python3
"""Deterministic verifier for Folio E.15: Bažant Size Effect Law, Hillerborg Fictitious Crack Model & Concrete Brittleness Scaling.

Governing relations (Bažant 1984, DOI 10.1061/(ASCE)0733-9399(1984)110:4(518);
Bažant & Kazemi 1990, DOI 10.1007/BF00047063; Hillerborg, Modéer & Petersson 1976,
DOI 10.1016/0008-8846(76)90007-7):
  - Geometrically similar notched Type II concrete members (notch ratio alpha_0 = a_0 / D > 0,
    dimensionless LEFM energy release g(alpha_0) > 0, g'(alpha_0) > 0):
        beta_B = D / D_0                                        (dimensionless brittleness number)
        sigma_N(D) = B * f'_t / sqrt(1 + beta_B)                [MPa]
        s(D) = d ln(sigma_N) / d ln(D) = -beta_B / (2*(1 + beta_B))
  - Initial Mode I fracture energy and effective fracture process zone (FPZ) length:
        G_f = (B * f'_t)^2 * D_0 * g(alpha_0) / E'              [N/m, with MPa^2 * mm / GPa = N/m]
        c_f = D_0 * g(alpha_0) / g'(alpha_0)                    [mm]
        l_ch = E' * G_f / (f'_t)^2                              [mm, with GPa * (N/m) / MPa^2 = mm]

Model scope & caveats:
  - Applies strictly to geometrically similar Type II notched structures (alpha_0 > 0) where
    macrocrack localization from a pre-existing notch or stress concentrator governs failure.
  - Varying transitional size D_0 while holding B*f'_t, E', f'_t, g(alpha_0), and g'(alpha_0) fixed
    scales G_f, c_f, and l_ch linearly with D_0 (comparing tougher vs. more brittle concrete mixes
    at constant small-scale plastic strength B*f'_t).
  - Does not cover unnotched Type I modulus-of-rupture beams (which follow Type I Weibull-energetic
    scaling with a finite large-size asymptotic strength), heavily stirrup-confined shear members,
    or ultra-high-strength fiber-reinforced composites.

Planted-defect mode (`--planted-defect`):
  Drops the size-effect denominator (1 + D / D_0), extrapolating the scale-invariant small-specimen
  plastic strength sigma_N = B * f'_t = 4.20 MPa across a full-scale D = 2000 mm girder (where
  the Bažant Type II model gives 1.322 MPa, a 3.177x unsafe overprediction).
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from typing import Any


def evaluate_size_effect(
    structural_depth_d_mm: float = 400.0,
    transitional_size_d0_mm: float = 220.0,
    small_scale_strength_bft_mpa: float = 4.20,
    effective_modulus_ep_gpa: float = 34.0,
    tensile_strength_ft_mpa: float = 3.20,
    lefm_g_alpha0: float = 1.12,
    lefm_gp_alpha0: float = 3.80,
    planted_defect: bool = False,
) -> dict[str, Any]:
    """Evaluate Bažant Type II Size Effect Law and Hillerborg fracture parameters."""
    params = (
        structural_depth_d_mm,
        transitional_size_d0_mm,
        small_scale_strength_bft_mpa,
        effective_modulus_ep_gpa,
        tensile_strength_ft_mpa,
        lefm_g_alpha0,
        lefm_gp_alpha0,
    )
    if not all(math.isfinite(v) for v in params):
        raise ValueError("All fracture scaling parameters must be finite numbers")
    if any(v <= 0.0 for v in params):
        raise ValueError("D, D_0, B*f'_t, E', f'_t, g(alpha_0), and g'(alpha_0) must be strictly positive")

    brittleness_beta_b = structural_depth_d_mm / transitional_size_d0_mm
    effective_beta = 0.0 if planted_defect else brittleness_beta_b

    retention_ratio = 1.0 / math.sqrt(1.0 + effective_beta)
    nominal_strength_mpa = small_scale_strength_bft_mpa * retention_ratio
    log_log_slope = -effective_beta / (2.0 * (1.0 + effective_beta))

    # Unit identity: (MPa^2 * mm) / GPa = ((1e6 N/m^2)^2 * 1e-3 m) / (1e9 N/m^2) = 1 N/m
    fracture_energy_gf_n_per_m = (
        (small_scale_strength_bft_mpa ** 2) * transitional_size_d0_mm * lefm_g_alpha0
    ) / effective_modulus_ep_gpa
    fpz_length_cf_mm = transitional_size_d0_mm * lefm_g_alpha0 / lefm_gp_alpha0
    # Unit identity: (GPa * N/m) / MPa^2 = 1e-3 m = 1 mm
    hillerborg_lch_mm = (effective_modulus_ep_gpa * fracture_energy_gf_n_per_m) / (
        tensile_strength_ft_mpa ** 2
    )

    if effective_beta <= 0.15:
        regime = "QUASI-PLASTIC LIMIT (β_B <= 0.15, model)"
    elif effective_beta <= 10.0:
        regime = "QUASI-BRITTLE TRANSITION (0.15 < β_B <= 10, model)"
    else:
        regime = "LEFM BRITTLE ASYMPTOTE (β_B > 10, model)"

    return {
        "folio": "E.15",
        "structural_depth_d_mm": round(structural_depth_d_mm, 1),
        "transitional_size_d0_mm": round(transitional_size_d0_mm, 1),
        "brittleness_beta_b": round(effective_beta, 3),
        "nominal_strength_mpa": round(nominal_strength_mpa, 3),
        "retention_pct": round(retention_ratio * 100.0, 1),
        "log_log_slope": round(log_log_slope, 3),
        "fracture_energy_gf_n_per_m": round(fracture_energy_gf_n_per_m, 2),
        "fpz_length_cf_mm": round(fpz_length_cf_mm, 2),
        "hillerborg_lch_mm": round(hillerborg_lch_mm, 1),
        "regime": regime,
        "exact_nominal_strength_mpa": nominal_strength_mpa,
        "exact_log_log_slope": log_log_slope,
    }


def linear_regression_bazant_kazemi(
    depths_mm: list[float],
    strengths_mpa: list[float],
) -> tuple[float, float]:
    """Recover B*f'_t and D_0 via Y = 1/sigma_N^2 = C*D + A (Bažant & Kazemi 1990)."""
    n = len(depths_mm)
    if n < 2 or n != len(strengths_mpa):
        raise ValueError("Need >= 2 paired (D, sigma_N) measurements")
    if not all(math.isfinite(d) and d > 0.0 for d in depths_mm):
        raise ValueError("All structural depths D must be finite and strictly positive")
    if not all(math.isfinite(s) and s > 0.0 for s in strengths_mpa):
        raise ValueError("All nominal strengths sigma_N must be finite and strictly positive")
    xs = depths_mm
    ys = [1.0 / (s * s) for s in strengths_mpa]
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    sxx = sum((x - mean_x) ** 2 for x in xs)
    if not math.isfinite(sxx) or sxx <= 0.0:
        raise ValueError("Need >= 2 distinct structural depths D for regression")
    sxy = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    slope_c = sxy / sxx
    intercept_a = mean_y - slope_c * mean_x
    if not (math.isfinite(slope_c) and math.isfinite(intercept_a)) or slope_c <= 0.0 or intercept_a <= 0.0:
        raise ValueError("Regression slope C and intercept A must be finite and strictly positive")
    bft_recovered = 1.0 / math.sqrt(intercept_a)
    d0_recovered = intercept_a / slope_c
    return bft_recovered, d0_recovered


def run_checks(planted_defect: bool = False) -> dict[str, Any]:
    default_beam = evaluate_size_effect(
        structural_depth_d_mm=400.0,
        transitional_size_d0_mm=220.0,
        planted_defect=planted_defect,
    )
    small_lab_beam = evaluate_size_effect(
        structural_depth_d_mm=100.0,
        transitional_size_d0_mm=220.0,
        planted_defect=planted_defect,
    )
    full_scale_girder = evaluate_size_effect(
        structural_depth_d_mm=2000.0,
        transitional_size_d0_mm=220.0,
        planted_defect=planted_defect,
    )
    tough_beam = evaluate_size_effect(
        structural_depth_d_mm=400.0,
        transitional_size_d0_mm=440.0,
        planted_defect=planted_defect,
    )

    sample_depths = [100.0, 200.0, 400.0, 800.0, 1600.0]
    sample_strengths = [
        evaluate_size_effect(
            structural_depth_d_mm=d,
            transitional_size_d0_mm=220.0,
            planted_defect=planted_defect,
        )["exact_nominal_strength_mpa"]
        for d in sample_depths
    ]

    failures: list[str] = []
    if not (small_lab_beam["exact_nominal_strength_mpa"] > default_beam["exact_nominal_strength_mpa"] > full_scale_girder["exact_nominal_strength_mpa"]):
        failures.append("Nominal strength must strictly decrease as structural depth D grows from 100 mm to 2000 mm")
    if full_scale_girder["exact_nominal_strength_mpa"] >= 1.50:
        failures.append(
            f"Full-scale D=2000 mm girder strength {full_scale_girder['nominal_strength_mpa']} MPa exceeds Type II size-effect bound (<1.50 MPa)"
        )
    if full_scale_girder["exact_log_log_slope"] > -0.40:
        failures.append(
            f"Full-scale D=2000 mm log-log slope {full_scale_girder['log_log_slope']} failed to approach LEFM -0.5 asymptote"
        )
    if abs(default_beam["fracture_energy_gf_n_per_m"] - 127.84) > 0.05:
        failures.append(f"Unexpected G_f at D_0=220 mm: {default_beam['fracture_energy_gf_n_per_m']}")
    if abs(default_beam["fpz_length_cf_mm"] - 64.84) > 0.05:
        failures.append(f"Unexpected c_f at D_0=220 mm: {default_beam['fpz_length_cf_mm']}")
    if abs(default_beam["hillerborg_lch_mm"] - 424.5) > 0.5:
        failures.append(f"Unexpected l_ch at D_0=220 mm: {default_beam['hillerborg_lch_mm']}")
    if tough_beam["exact_nominal_strength_mpa"] <= default_beam["exact_nominal_strength_mpa"]:
        failures.append("Doubling D_0 (tougher aggregate/FPZ) must raise nominal strength at fixed D = 400 mm")

    try:
        bft_rec, d0_rec = linear_regression_bazant_kazemi(sample_depths, sample_strengths)
        if abs(bft_rec - 4.20) > 1e-6 or abs(d0_rec - 220.0) > 1e-6:
            failures.append(f"Bažant-Kazemi regression mismatch: B*f'_t={bft_rec}, D_0={d0_rec}")
    except ValueError as exc:
        failures.append(f"Bažant-Kazemi regression failed: {exc}")

    # Negative domain checks: non-positive depth, duplicate depths, and non-positive/NaN strength must raise ValueError
    rejected_invalid = False
    try:
        evaluate_size_effect(structural_depth_d_mm=0.0)
    except ValueError:
        rejected_invalid = True
    if not rejected_invalid:
        failures.append("Domain check failed to reject D = 0 mm")

    for bad_label, bad_args in (
        ("duplicate D", ([400.0, 400.0], [2.5, 2.5])),
        ("zero strength", ([100.0, 400.0], [0.0, 2.5])),
        ("negative strength", ([100.0, 400.0], [-3.4, 2.5])),
        ("NaN strength", ([100.0, 400.0], [float("nan"), 2.5])),
    ):
        try:
            linear_regression_bazant_kazemi(*bad_args)
            failures.append(f"Regression failed to reject {bad_label}")
        except ValueError:
            pass

    status = "FAIL" if failures else "PASS"
    return {
        "status": status,
        "folio": "E.15",
        "planted_defect": planted_defect,
        "default_beam_400mm": default_beam,
        "small_lab_beam_100mm": small_lab_beam,
        "full_scale_girder_2000mm": full_scale_girder,
        "tough_beam_d0_440mm": tough_beam,
        "overprediction_ratio_at_2000mm": round(4.20 / full_scale_girder["exact_nominal_strength_mpa"], 3),
        "failures": failures,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify Folio E.15 Bažant Size Effect Law & Hillerborg FPZ model.")
    parser.add_argument("--planted-defect", action="store_true", help="Drop (1 + D/D_0) size scaling (must fail).")
    args = parser.parse_args(argv)
    result = run_checks(planted_defect=args.planted_defect)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
