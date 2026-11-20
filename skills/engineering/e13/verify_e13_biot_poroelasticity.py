#!/usr/bin/env python3
"""Deterministic verifier for Folio E.13: Biot 3D Poroelasticity, Skempton B & Mohr-Coulomb Fault Slip Margin.

Sign convention (compression-positive geomechanics):
  - Biot-Willis intact-matrix effective stress coefficient: alpha = 1 - K_d / K_s
  - Rice-Cleary (1976) Skempton undrained coefficient:
        B = (1/K_d - 1/K_s) / [1/K_d - 1/K_s + phi * (1/K_f - 1/K_s)]
    with undrained pore-pressure increment delta_p_u = +B * delta_sigma_mean.
  - Lateral poroelastic stress-path factor (passive readout; total sigma_h = k_0 * sigma_v is uncoupled):
        eta_poro = alpha * (1 - 2*nu) / (1 - nu)
  - Cohesionless Mohr-Coulomb fault plane (dipping 90 - beta from horizontal; fault-plane angle beta from sigma_v, i.e. normal beta from sigma_h):
        sigma_n = 0.5*(sigma_v + sigma_h) - 0.5*(sigma_v - sigma_h)*cos(2*beta)
        |tau|   = |0.5*(sigma_v - sigma_h)*sin(2*beta)|
        sigma'_n = sigma_n - alpha_fault * (p_0 + delta_p_inj)
        slip_tendency = |tau| / sigma'_n  (when sigma'_n > 0)
        tensile_margin = min(sigma_v, sigma_h) - (p_0 + delta_p_inj)
        critical_delta_p = ((sigma_n - |tau| / mu_f) / alpha_fault) - p_0

Planted-defect mode (`--planted-defect`):
  Substitutes the intact sandstone Biot coefficient `biot_alpha` (0.667) instead of `alpha_fault` (1.0)
  inside the fault-plane effective normal stress and critical overpressure calculations, illustrating
  how confusing matrix alpha with open-fault Terzaghi alpha_fault overestimates fault stability.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from typing import Any


def evaluate_biot_poroelastic_fault_slip(
    drained_bulk_kd_gpa: float = 12.0,
    solid_grain_ks_gpa: float = 36.0,
    porosity_phi: float = 0.20,
    fluid_bulk_kf_gpa: float = 2.2,
    drained_poisson_nu: float = 0.25,
    sigma_v_mpa: float = 50.0,
    stress_ratio_k0: float = 0.72,
    hydrostatic_p0_mpa: float = 20.0,
    delta_p_inj_mpa: float = 4.5,
    fault_angle_beta_deg: float = 30.0,
    friction_mu_f: float = 0.60,
    alpha_fault: float = 1.0,
    planted_defect: bool = False,
) -> dict[str, Any]:
    """Compute Biot 3D poroelastic constants, Skempton B, and Mohr-Coulomb fault slip margins."""
    numeric_inputs = (
        drained_bulk_kd_gpa,
        solid_grain_ks_gpa,
        fluid_bulk_kf_gpa,
        porosity_phi,
        drained_poisson_nu,
        sigma_v_mpa,
        stress_ratio_k0,
        hydrostatic_p0_mpa,
        delta_p_inj_mpa,
        fault_angle_beta_deg,
        friction_mu_f,
        alpha_fault,
    )
    if not all(math.isfinite(v) for v in numeric_inputs):
        raise ValueError("All poroelastic and stress parameters must be finite numbers")
    if drained_bulk_kd_gpa <= 0.0 or solid_grain_ks_gpa <= 0.0 or drained_bulk_kd_gpa >= solid_grain_ks_gpa:
        raise ValueError("Require 0 < K_d < K_s (GPa) for physical Biot-Willis alpha in (0, 1)")
    if fluid_bulk_kf_gpa <= 0.0 or fluid_bulk_kf_gpa > solid_grain_ks_gpa:
        raise ValueError("Require 0 < K_f <= K_s (GPa) for physical Skempton B in (0, 1]")
    if not (0.0 < porosity_phi < 1.0):
        raise ValueError("Porosity phi must lie in (0, 1)")
    if not (-1.0 < drained_poisson_nu < 0.5):
        raise ValueError("Drained Poisson ratio nu must lie in (-1.0, 0.5)")
    if sigma_v_mpa <= 0.0 or stress_ratio_k0 <= 0.0 or hydrostatic_p0_mpa < 0.0 or delta_p_inj_mpa < 0.0:
        raise ValueError("Overburden, stress ratio, and pore pressures must be valid")
    if friction_mu_f <= 0.0 or alpha_fault <= 0.0 or alpha_fault > 1.0:
        raise ValueError("Friction mu_f must be positive and alpha_fault in (0, 1]")

    biot_alpha = 1.0 - (drained_bulk_kd_gpa / solid_grain_ks_gpa)
    c_drain = (1.0 / drained_bulk_kd_gpa) - (1.0 / solid_grain_ks_gpa)
    c_fluid = porosity_phi * ((1.0 / fluid_bulk_kf_gpa) - (1.0 / solid_grain_ks_gpa))
    skempton_b = c_drain / (c_drain + c_fluid)
    eta_poro = biot_alpha * (1.0 - 2.0 * drained_poisson_nu) / (1.0 - drained_poisson_nu)

    sigma_h_mpa = stress_ratio_k0 * sigma_v_mpa
    sigma_3_mpa = min(sigma_v_mpa, sigma_h_mpa)
    beta_rad = math.radians(fault_angle_beta_deg)
    sigma_mean_2d = 0.5 * (sigma_v_mpa + sigma_h_mpa)
    sigma_diff_half = 0.5 * (sigma_v_mpa - sigma_h_mpa)

    sigma_n_mpa = sigma_mean_2d - sigma_diff_half * math.cos(2.0 * beta_rad)
    shear_tau_mpa = abs(sigma_diff_half * math.sin(2.0 * beta_rad))

    effective_fault_alpha = biot_alpha if planted_defect else alpha_fault
    total_p_mpa = hydrostatic_p0_mpa + delta_p_inj_mpa
    sigma_n_eff_mpa = sigma_n_mpa - effective_fault_alpha * total_p_mpa
    tensile_margin_mpa = sigma_3_mpa - total_p_mpa
    tensile_safe = sigma_n_eff_mpa > 0.0 and tensile_margin_mpa > 0.0

    critical_delta_p_mpa = ((sigma_n_mpa - (shear_tau_mpa / friction_mu_f)) / effective_fault_alpha) - hydrostatic_p0_mpa
    slip_margin_mpa = critical_delta_p_mpa - delta_p_inj_mpa

    if sigma_n_eff_mpa <= 0.0:
        slip_tendency: float | None = None
        slip_safe = False
    else:
        slip_tendency = shear_tau_mpa / sigma_n_eff_mpa
        slip_safe = slip_tendency < friction_mu_f

    return {
        "folio": "E.13",
        "biot_alpha": round(biot_alpha, 3),
        "skempton_b": round(skempton_b, 3),
        "poroelastic_stress_path_eta": round(eta_poro, 3),
        "sigma_h_mpa": round(sigma_h_mpa, 2),
        "fault_normal_stress_mpa": round(sigma_n_mpa, 2),
        "fault_shear_stress_mpa": round(shear_tau_mpa, 3),
        "fault_effective_normal_stress_mpa": round(sigma_n_eff_mpa, 2),
        "slip_tendency": None if slip_tendency is None else round(slip_tendency, 3),
        "critical_delta_p_mpa": round(critical_delta_p_mpa, 2),
        "slip_margin_mpa": round(slip_margin_mpa, 2),
        "tensile_margin_mpa": round(tensile_margin_mpa, 2),
        "tensile_safe": tensile_safe,
        "slip_safe": slip_safe,
        "poroelastic_fault_pass": tensile_safe and slip_safe,
    }


def _check_bounds_rejections() -> bool:
    invalid_cases = (
        dict(drained_bulk_kd_gpa=40.0, solid_grain_ks_gpa=36.0),
        dict(fluid_bulk_kf_gpa=72.0),
        dict(porosity_phi=1.0),
        dict(drained_poisson_nu=0.5),
        dict(alpha_fault=0.0),
        dict(delta_p_inj_mpa=float("nan")),
    )
    for kw in invalid_cases:
        try:
            evaluate_biot_poroelastic_fault_slip(**kw)
            return False
        except ValueError:
            pass
    return True


def run_verification(planted_defect: bool = False) -> dict[str, Any]:
    nominal = evaluate_biot_poroelastic_fault_slip(planted_defect=planted_defect)
    co2_fluid = evaluate_biot_poroelastic_fault_slip(fluid_bulk_kf_gpa=0.20, planted_defect=planted_defect)
    basement = evaluate_biot_poroelastic_fault_slip(stress_ratio_k0=0.60, delta_p_inj_mpa=4.5, planted_defect=planted_defect)
    pre_inj = evaluate_biot_poroelastic_fault_slip(stress_ratio_k0=0.56, delta_p_inj_mpa=0.0, planted_defect=planted_defect)
    overpressure = evaluate_biot_poroelastic_fault_slip(delta_p_inj_mpa=11.0, planted_defect=planted_defect)
    tensile = evaluate_biot_poroelastic_fault_slip(delta_p_inj_mpa=22.0, planted_defect=planted_defect)
    reverse = evaluate_biot_poroelastic_fault_slip(stress_ratio_k0=1.20, fault_angle_beta_deg=5.0, delta_p_inj_mpa=32.0, planted_defect=planted_defect)
    terzaghi = evaluate_biot_poroelastic_fault_slip(drained_bulk_kd_gpa=1e-4, fluid_bulk_kf_gpa=36.0, planted_defect=planted_defect)

    checks = {
        "nominal_biot_alpha_0_667": nominal["biot_alpha"] == 0.667,
        "nominal_skempton_b_0_394": nominal["skempton_b"] == 0.394,
        "nominal_eta_poro_0_444": nominal["poroelastic_stress_path_eta"] == 0.444,
        "nominal_slip_tendency_0_404": nominal["slip_tendency"] == 0.404,
        "nominal_critical_dp_9_40": nominal["critical_delta_p_mpa"] == 9.40,
        "nominal_margins_pass": nominal["slip_margin_mpa"] == 4.90 and nominal["tensile_margin_mpa"] == 11.50 and nominal["poroelastic_fault_pass"],
        "co2_skempton_b_0_053": co2_fluid["skempton_b"] == 0.053,
        "basement_k0_0_60_slips": (not basement["slip_safe"]) and basement["critical_delta_p_mpa"] == 0.57 and basement["slip_tendency"] == 0.825,
        "pre_injection_k0_0_56_unstable": (not pre_inj["slip_safe"]) and pre_inj["critical_delta_p_mpa"] < 0.0,
        "overpressure_11mpa_slips": (not overpressure["slip_safe"]) and overpressure["slip_margin_mpa"] < 0.0,
        "tensile_22mpa_hydraulic_breach": (not tensile["tensile_safe"]) and tensile["slip_tendency"] is None,
        "reverse_fault_overburden_tensile_breach": (not reverse["tensile_safe"]) and reverse["tensile_margin_mpa"] < 0.0,
        "terzaghi_incompressible_limit": terzaghi["biot_alpha"] > 0.999 and terzaghi["skempton_b"] == 1.0,
        "invalid_bounds_raise_value_error": _check_bounds_rejections(),
    }
    ok = all(checks.values())
    return {
        "status": "PASS" if ok else "FAIL",
        "folio_id": "E.13",
        "planted_defect": planted_defect,
        "nominal": nominal,
        "co2_skempton_b": co2_fluid["skempton_b"],
        "basement_k0_0_60": {
            "slip_tendency": basement["slip_tendency"],
            "critical_delta_p_mpa": basement["critical_delta_p_mpa"],
            "slip_safe": basement["slip_safe"],
        },
        "checks": checks,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify Folio E.13 Biot 3D Poroelasticity & Fault Slip Margin.")
    parser.add_argument("--planted-defect", action="store_true", help="Substitute matrix alpha for alpha_fault on fault plane (must fail)")
    parser.add_argument("--json", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)

    report = run_verification(planted_defect=args.planted_defect)
    print(json.dumps(report, indent=2 if args.json else None))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
