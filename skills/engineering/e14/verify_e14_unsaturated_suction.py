#!/usr/bin/env python3
"""Deterministic verifier for Folio E.14: Unsaturated Soil Suction Stress, van Genuchten-Mualem Retention & Infinite-Slope Stability.

Sign convention (compression-positive geomechanics, matching E.05 and E.13):
  - Matric suction (gauge pore-air pressure u_a = 0): psi = u_a - u_w >= 0 (kPa).
  - Effective saturation (van Genuchten 1980, DOI 10.2136/sssaj1980.03615995004400050002x):
        S_e(psi) = [1 + (alpha_vg * psi)^n]^(-m),   m = 1 - 1/n,   n > 1.
  - Relative hydraulic conductivity (Mualem 1976, DOI 10.1029/WR012i003p00513):
        K_r(S_e) = S_e^(1/2) * [1 - (1 - S_e^(1/m))^m]^2.
  - Closed-form suction stress (Lu, Godt & Wu 2010, DOI 10.1029/2009WR008646):
        sigma_s(psi) = -S_e(psi) * psi <= 0 (tensile interparticle capillary/adsorptive attraction).
    Effective normal stress on slip plane: sigma'_n = (sigma_n - u_a) - sigma_s = (sigma_n - u_a) + S_e * psi.
  - Infinite-slope Factor of Safety at slip-plane depth z (Lu & Godt 2008, DOI 10.1029/2008WR006976):
        FS = tan(phi') / tan(beta) + (c' - sigma_s * tan(phi')) / (gamma * z * sin(beta) * cos(beta)).

Model scope & caveats:
  - Prescribes steady uniform matric suction psi >= 0 at depth z rather than solving coupled transient
    Richards infiltration psi(z, t) or moisture-dependent unit weight gamma(theta).
  - alpha_vg is in kPa^-1 (1 kPa ~ 10.194 cm H2O).
  - Below the water table (u_w > u_a, psi < 0), this unsaturated domain transitions to saturated Terzaghi
    effective stress (S_e = 1, K_r = 1, sigma_s = -psi = u_w - u_a > 0).

Planted-defect mode (`--planted-defect`):
  Sets Bishop weighting chi = 1.0 (extrapolating saturated Terzaghi linearly as sigma_s = -psi instead of
  -S_e * psi) across unsaturated soil, falsely predicting slope stability (FS > 1) in clean sand at
  psi = 40.0 kPa where actual desaturation leaves S_e = 0.052 and FS < 1.0.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from typing import Any


def evaluate_unsaturated_slope(
    matric_suction_psi_kpa: float = 24.0,
    slope_beta_deg: float = 34.0,
    alpha_vg_inv_kpa: float = 0.02,
    van_genuchten_n: float = 1.60,
    unit_weight_gamma_kn_m3: float = 19.0,
    cohesion_c_eff_kpa: float = 2.0,
    friction_phi_eff_deg: float = 28.0,
    slip_depth_z_m: float = 2.0,
    planted_defect: bool = False,
) -> dict[str, Any]:
    """Compute van Genuchten S_e, Mualem K_r, Lu-Godt-Wu suction stress sigma_s, and infinite-slope FS."""
    numeric_inputs = (
        matric_suction_psi_kpa,
        slope_beta_deg,
        alpha_vg_inv_kpa,
        van_genuchten_n,
        unit_weight_gamma_kn_m3,
        cohesion_c_eff_kpa,
        friction_phi_eff_deg,
        slip_depth_z_m,
    )
    if not all(math.isfinite(v) for v in numeric_inputs):
        raise ValueError("All unsaturated soil and slope parameters must be finite numbers")
    if matric_suction_psi_kpa < 0.0:
        raise ValueError("Matric suction psi = u_a - u_w must be >= 0 kPa in the unsaturated zone")
    if alpha_vg_inv_kpa <= 0.0:
        raise ValueError("van Genuchten alpha_vg (kPa^-1) must be strictly positive")
    if van_genuchten_n <= 1.0:
        raise ValueError("van Genuchten exponent n must be > 1.0 so m = 1 - 1/n lies in (0, 1)")
    if not (0.0 < slope_beta_deg < 90.0):
        raise ValueError("Slope inclination beta (deg) must lie in (0, 90)")
    if not (0.0 < friction_phi_eff_deg < 90.0):
        raise ValueError("Drained friction angle phi' (deg) must lie in (0, 90)")
    if unit_weight_gamma_kn_m3 <= 0.0 or slip_depth_z_m <= 0.0:
        raise ValueError("Unit weight gamma and slip-plane depth z must be strictly positive")
    if cohesion_c_eff_kpa < 0.0:
        raise ValueError("Effective cohesion c' must be non-negative")

    m = 1.0 - (1.0 / van_genuchten_n)
    if matric_suction_psi_kpa == 0.0:
        effective_sat = 1.0
        rel_perm_kr = 1.0
        suction_stress_kpa = 0.0
    else:
        scaled = alpha_vg_inv_kpa * matric_suction_psi_kpa
        effective_sat = (1.0 + scaled ** van_genuchten_n) ** (-m)
        u = min(1.0, max(0.0, effective_sat ** (1.0 / m)))
        if u >= 1.0:
            inner = 1.0
        elif u <= 0.0:
            inner = 0.0
        else:
            inner = -math.expm1(m * math.log1p(-u))
        rel_perm_kr = math.sqrt(effective_sat) * (inner * inner)
        chi_eff = 1.0 if planted_defect else effective_sat
        suction_stress_kpa = -chi_eff * matric_suction_psi_kpa

    beta_rad = math.radians(slope_beta_deg)
    phi_rad = math.radians(friction_phi_eff_deg)
    tan_beta = math.tan(beta_rad)
    tan_phi = math.tan(phi_rad)
    denom_shear = unit_weight_gamma_kn_m3 * slip_depth_z_m * math.sin(beta_rad) * math.cos(beta_rad)
    sigma_n_net_kpa = unit_weight_gamma_kn_m3 * slip_depth_z_m * (math.cos(beta_rad) ** 2)
    sigma_n_eff_kpa = sigma_n_net_kpa - suction_stress_kpa
    shear_tau_kpa = denom_shear

    factor_of_safety = (tan_phi / tan_beta) + (
        (cohesion_c_eff_kpa - suction_stress_kpa * tan_phi) / denom_shear
    )

    if factor_of_safety < 1.0:
        regime = "BELOW LIMIT EQUILIBRIUM (FS < 1.0, model)"
    elif factor_of_safety < 1.2:
        regime = "MARGINAL EQUILIBRIUM (1.0 <= FS < 1.2, model)"
    else:
        regime = "ABOVE LIMIT EQUILIBRIUM (FS >= 1.2, model)"

    return {
        "folio": "E.14",
        "effective_saturation_se": round(effective_sat, 3),
        "relative_conductivity_kr": round(rel_perm_kr, 4),
        "suction_stress_kpa": round(suction_stress_kpa, 2),
        "effective_normal_stress_kpa": round(sigma_n_eff_kpa, 2),
        "shear_demand_kpa": round(shear_tau_kpa, 2),
        "factor_of_safety": round(factor_of_safety, 3),
        "slope_pass": factor_of_safety >= 1.0,
        "regime": regime,
    }


def _check_bounds_rejections() -> bool:
    invalid_cases = (
        dict(matric_suction_psi_kpa=-1.0),
        dict(van_genuchten_n=1.0),
        dict(van_genuchten_n=0.8),
        dict(alpha_vg_inv_kpa=0.0),
        dict(slope_beta_deg=0.0),
        dict(slope_beta_deg=90.0),
        dict(friction_phi_eff_deg=0.0),
        dict(unit_weight_gamma_kn_m3=0.0),
        dict(slip_depth_z_m=-0.5),
        dict(cohesion_c_eff_kpa=-1.0),
        dict(matric_suction_psi_kpa=float("nan")),
    )
    for kw in invalid_cases:
        try:
            evaluate_unsaturated_slope(**kw)
            return False
        except ValueError:
            pass
    return True


def run_verification(planted_defect: bool = False) -> dict[str, Any]:
    nominal = evaluate_unsaturated_slope(planted_defect=planted_defect)
    saturated = evaluate_unsaturated_slope(matric_suction_psi_kpa=0.0, planted_defect=planted_defect)
    near_onset = evaluate_unsaturated_slope(matric_suction_psi_kpa=2.0, planted_defect=planted_defect)
    dry_loam = evaluate_unsaturated_slope(matric_suction_psi_kpa=120.0, planted_defect=planted_defect)
    clean_sand_peak = evaluate_unsaturated_slope(
        matric_suction_psi_kpa=7.964,
        slope_beta_deg=36.0,
        alpha_vg_inv_kpa=0.145,
        van_genuchten_n=2.68,
        unit_weight_gamma_kn_m3=18.0,
        cohesion_c_eff_kpa=0.0,
        friction_phi_eff_deg=32.0,
        slip_depth_z_m=2.0,
        planted_defect=planted_defect,
    )
    clean_sand_dry = evaluate_unsaturated_slope(
        matric_suction_psi_kpa=40.0,
        slope_beta_deg=36.0,
        alpha_vg_inv_kpa=0.145,
        van_genuchten_n=2.68,
        unit_weight_gamma_kn_m3=18.0,
        cohesion_c_eff_kpa=0.0,
        friction_phi_eff_deg=32.0,
        slip_depth_z_m=2.0,
        planted_defect=planted_defect,
    )

    checks = {
        "nominal_se_0_904": nominal["effective_saturation_se"] == 0.904,
        "nominal_kr_0_1662": nominal["relative_conductivity_kr"] == 0.1662,
        "nominal_suction_stress_neg_21_69": nominal["suction_stress_kpa"] == -21.69,
        "nominal_fs_1_557": nominal["factor_of_safety"] == 1.557 and nominal["slope_pass"],
        "saturated_psi_0_kr_1_and_unstable": (
            saturated["effective_saturation_se"] == 1.0
            and saturated["relative_conductivity_kr"] == 1.0
            and saturated["suction_stress_kpa"] == 0.0
            and saturated["factor_of_safety"] == 0.902
            and (not saturated["slope_pass"])
        ),
        "unsaturated_wetting_collapse_at_psi_2": (
            near_onset["suction_stress_kpa"] == -2.0
            and near_onset["factor_of_safety"] == 0.962
            and (not near_onset["slope_pass"])
        ),
        "silty_loam_monotonic_suction_n_1_60": abs(dry_loam["suction_stress_kpa"]) > abs(nominal["suction_stress_kpa"]),
        "clean_sand_non_monotonic_peak_7_96kpa": (
            abs(clean_sand_peak["suction_stress_kpa"]) > abs(clean_sand_dry["suction_stress_kpa"])
        ),
        "clean_sand_dry_40kpa_desaturated_unstable": (
            clean_sand_dry["effective_saturation_se"] == 0.052
            and clean_sand_dry["suction_stress_kpa"] == -2.08
            and clean_sand_dry["factor_of_safety"] == 0.936
            and (not clean_sand_dry["slope_pass"])
        ),
        "invalid_bounds_raise_value_error": _check_bounds_rejections(),
    }
    ok = all(checks.values())
    return {
        "status": "PASS" if ok else "FAIL",
        "folio_id": "E.14",
        "planted_defect": planted_defect,
        "nominal": nominal,
        "saturated": saturated,
        "near_onset_psi_2": near_onset,
        "clean_sand_peak": clean_sand_peak,
        "clean_sand_dry_40kpa": clean_sand_dry,
        "checks": checks,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify Folio E.14 Unsaturated Soil Suction Stress & Slope Stability.")
    parser.add_argument(
        "--planted-defect",
        action="store_true",
        help="Force Bishop chi = 1.0 (linear Terzaghi suction extrapolation) instead of chi = S_e (must fail)",
    )
    parser.add_argument("--json", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)

    report = run_verification(planted_defect=args.planted_defect)
    print(json.dumps(report, indent=2 if args.json else None))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
