#!/usr/bin/env python3
"""Deterministic verifier for Folio E.16: Bridge Pier Local Scour, Shields Sediment Threshold & Flood-Duration Time-Scale Lag.

Governing relations (Shields 1936 via Buffington 1999, DOI 10.1061/(ASCE)0733-9429(1999)125:4(376);
Melville 1997, DOI 10.1061/(ASCE)0733-9429(1997)123:2(125);
Melville & Chiew 1999, DOI 10.1061/(ASCE)0733-9429(1999)125:1(59);
Sheppard, Melville & Demir 2014, DOI 10.1061/(ASCE)HY.1943-7900.0000800):
  1. Shields incipient motion & logarithmic depth-averaged threshold velocity V_c (m/s):
        u_*c = sqrt(theta_c * (s - 1) * g * d_50)               [m/s]
        V_c  = 5.75 * u_*c * log10(5.53 * y_1 / d_50)           [m/s, for 5.53 * y_1 / d_50 > 1]
  2. Sheppard-Melville (S/M) clear-water equilibrium local scour (0.4014 <= V_1 / V_c <= 1.0):
        f_1 = tanh((y_1 / a*)^0.4)
        f_2 = max(0.0, 1.0 - 1.2 * (ln(V_1 / V_c))^2)
        f_3 = (a* / d_50) / (0.4 * (a* / d_50)^1.2 + 10.6 * (a* / d_50)^(-0.13))
        y_s,SM = 2.5 * a* * f_1 * f_2 * f_3                     [m]
  3. HEC-18 CSU equilibrium pier-scour reference envelope:
        Fr_1 = V_1 / sqrt(g * y_1)
        y_s,CSU = min(cap_ratio * a*, 2.0 * K_1 * K_2 * K_3 * y_1 * (a* / y_1)^0.65 * Fr_1^0.43) [m]
        where cap_ratio = 2.4 for Fr_1 <= 0.8 else 3.0.
  4. Melville & Chiew (1999) clear-water equilibrium time scale t_e (days) and temporal factor K_t:
        Dimensionless time scale t* = V_1 * t_e_sec / a*:
          t_e (days) = 30.89 * (a* / V_1) * (V_1 / V_c - 0.4) * (y_1 / a*)^0.25   for y_1 / a* <= 6.0
          t_e (days) = 48.26 * (a* / V_1) * (V_1 / V_c - 0.4)                     for y_1 / a* > 6.0
          (empirical unit factors 30.89 = 2.669e6 / 86400 days*s^-1 and 48.26 = 4.170e6 / 86400 days*s^-1,
           with a* in m and V_1 in m/s).
        K_t(t_d) = 1.0                                                            for t_d / 24 >= t_e
        K_t(t_d) = exp(-0.03 * |(V_c / V_1) * ln((t_d / 24) / t_e)|^1.6)          for 0 < t_d / 24 < t_e
        y_s(t_d) = K_t(t_d) * y_s,SM                                              [m]

Model scope & caveats:
  - Illustrative closed-form hydraulic screening model for a single unskewed circular pier in uniform
    cohesionless sand/gravel under clear-water flow (0.45 <= V_1 / V_c <= 1.00); not a bridge foundation
    design calculation.
  - Does not cover live-bed sediment transport (V_1 / V_c > 1.0), graded armor-layer breach ("armor-break"
    scour, Kabiri-Samani et al. 2026), multi-peak flood deposition/erosion memory (Link et al. 2020),
    cohesive clays, debris rafts, or complex pier/pile-cap geometries.

Planted-defect mode (`--planted-defect`):
  Drops both sediment-coarseness attenuation (setting f_3 = 1.0) and flood-duration time-scale lag
  (setting K_t = 1.0), inflating modeled short-flood clear-water scour depth by >2x at t_d = 2 h
  and erasing temporal sensitivity across flash vs. multi-day floods.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from typing import Any


def evaluate_pier_scour(
    flow_intensity_ratio: float = 0.85,
    flood_duration_hours: float = 24.0,
    pier_diameter_m: float = 2.00,
    approach_depth_m: float = 3.00,
    median_grain_d50_mm: float = 2.00,
    specific_gravity_s: float = 2.65,
    critical_shields_theta_c: float = 0.045,
    gravity_m_s2: float = 9.81,
    csu_k1: float = 1.0,
    csu_k2: float = 1.0,
    csu_k3: float = 1.1,
    planted_defect: bool = False,
) -> dict[str, Any]:
    """Evaluate Shields threshold, Sheppard-Melville & HEC-18 CSU equilibrium scour, and Melville-Chiew lag."""
    params = (
        flow_intensity_ratio,
        flood_duration_hours,
        pier_diameter_m,
        approach_depth_m,
        median_grain_d50_mm,
        specific_gravity_s,
        critical_shields_theta_c,
        gravity_m_s2,
        csu_k1,
        csu_k2,
        csu_k3,
    )
    if any(isinstance(v, bool) or not math.isfinite(v) for v in params):
        raise ValueError("All hydraulic scour parameters must be finite non-boolean numbers")
    if any(
        v <= 0.0
        for v in (
            flood_duration_hours,
            pier_diameter_m,
            approach_depth_m,
            median_grain_d50_mm,
            critical_shields_theta_c,
            gravity_m_s2,
            csu_k1,
            csu_k2,
            csu_k3,
        )
    ):
        raise ValueError("Geometric, sediment, gravity, and duration parameters must be strictly positive")
    if specific_gravity_s <= 1.0:
        raise ValueError("Sediment specific gravity s = rho_s / rho must exceed 1.0")
    # f_2 crosses zero at exp(-1/sqrt(1.2)) = 0.40137; clear-water regime requires (0.4014, 1.00]
    if not (0.405 <= flow_intensity_ratio <= 1.0):
        raise ValueError("Clear-water flow intensity ratio V_1 / V_c must lie in [0.405, 1.00]")

    d50_m = median_grain_d50_mm * 1.0e-3
    roughness_arg = 5.53 * approach_depth_m / d50_m
    if roughness_arg <= 1.0:
        raise ValueError("Relative depth 5.53 * y_1 / d_50 must exceed 1.0 for logarithmic velocity profile")

    u_star_c = math.sqrt(critical_shields_theta_c * (specific_gravity_s - 1.0) * gravity_m_s2 * d50_m)
    critical_velocity_m_s = 5.75 * u_star_c * math.log10(roughness_arg)
    approach_velocity_m_s = flow_intensity_ratio * critical_velocity_m_s
    froude_1 = approach_velocity_m_s / math.sqrt(gravity_m_s2 * approach_depth_m)

    shallowness_y_over_a = approach_depth_m / pier_diameter_m
    coarseness_a_over_d50 = pier_diameter_m / d50_m

    f1 = math.tanh(shallowness_y_over_a ** 0.4)
    f2 = max(0.0, 1.0 - 1.2 * (math.log(flow_intensity_ratio) ** 2))
    raw_f3 = coarseness_a_over_d50 / (
        0.4 * (coarseness_a_over_d50 ** 1.2) + 10.6 * (coarseness_a_over_d50 ** -0.13)
    )
    f3 = 1.0 if planted_defect else raw_f3

    ys_sm_eq_m = 2.5 * pier_diameter_m * f1 * f2 * f3

    csu_cap = 2.4 if froude_1 <= 0.8 else 3.0
    ys_csu_raw_m = (
        2.0
        * csu_k1
        * csu_k2
        * csu_k3
        * approach_depth_m
        * ((pier_diameter_m / approach_depth_m) ** 0.65)
        * (froude_1 ** 0.43)
    )
    ys_csu_eq_m = min(csu_cap * pier_diameter_m, ys_csu_raw_m)

    # Melville & Chiew (1999) clear-water equilibrium time scale t_e (days), a* in m, V_1 in m/s
    if shallowness_y_over_a <= 6.0:
        te_days = (
            30.89
            * (pier_diameter_m / approach_velocity_m_s)
            * (flow_intensity_ratio - 0.4)
            * (shallowness_y_over_a ** 0.25)
        )
    else:
        te_days = 48.26 * (pier_diameter_m / approach_velocity_m_s) * (flow_intensity_ratio - 0.4)

    flood_days = flood_duration_hours / 24.0
    if planted_defect or flood_days >= te_days:
        kt_factor = 1.0
    else:
        kt_arg = abs((1.0 / flow_intensity_ratio) * math.log(flood_days / te_days))
        kt_factor = math.exp(-0.03 * (kt_arg ** 1.6))

    ys_transient_m = kt_factor * ys_sm_eq_m
    csu_to_transient_ratio = ys_csu_eq_m / ys_transient_m if ys_transient_m > 0.0 else float("inf")

    if kt_factor < 0.65:
        regime = "RAPID INITIAL EXCAVATION (K_t < 0.65, model)"
    elif kt_factor < 0.90:
        regime = "TRANSIENT HYDROGRAPH LAG (0.65 <= K_t < 0.90, model)"
    else:
        regime = "NEAR-EQUILIBRIUM MATURITY (K_t >= 0.90, model)"

    return {
        "folio": "E.16",
        "flow_intensity_ratio": round(flow_intensity_ratio, 3),
        "flood_duration_hours": round(flood_duration_hours, 1),
        "u_star_c_m_s": round(u_star_c, 5),
        "critical_velocity_vc_m_s": round(critical_velocity_m_s, 4),
        "approach_velocity_v1_m_s": round(approach_velocity_m_s, 4),
        "froude_1": round(froude_1, 4),
        "f1_shallowness": round(f1, 4),
        "f2_intensity": round(f2, 4),
        "f3_coarseness": round(f3, 4),
        "equilibrium_time_te_days": round(te_days, 2),
        "equilibrium_time_te_hours": round(te_days * 24.0, 1),
        "time_factor_kt": round(kt_factor, 4),
        "ys_sm_eq_m": round(ys_sm_eq_m, 3),
        "ys_csu_eq_m": round(ys_csu_eq_m, 3),
        "ys_transient_m": round(ys_transient_m, 3),
        "csu_to_transient_ratio": round(csu_to_transient_ratio, 3),
        "regime": regime,
        "exact_ys_sm_eq_m": ys_sm_eq_m,
        "exact_ys_csu_eq_m": ys_csu_eq_m,
        "exact_ys_transient_m": ys_transient_m,
        "exact_kt_factor": kt_factor,
        "exact_te_days": te_days,
    }


def run_checks(planted_defect: bool = False) -> dict[str, Any]:
    default_24h = evaluate_pier_scour(
        flow_intensity_ratio=0.85,
        flood_duration_hours=24.0,
        planted_defect=planted_defect,
    )
    flash_2h = evaluate_pier_scour(
        flow_intensity_ratio=0.85,
        flood_duration_hours=2.0,
        planted_defect=planted_defect,
    )
    multiday_120h = evaluate_pier_scour(
        flow_intensity_ratio=0.85,
        flood_duration_hours=120.0,
        planted_defect=planted_defect,
    )
    threshold_peak_24h = evaluate_pier_scour(
        flow_intensity_ratio=1.00,
        flood_duration_hours=24.0,
        planted_defect=planted_defect,
    )
    post_eq_low_intensity = evaluate_pier_scour(
        flow_intensity_ratio=0.45,
        flood_duration_hours=240.0,
        planted_defect=planted_defect,
    )
    deep_flow_case = evaluate_pier_scour(
        flow_intensity_ratio=0.85,
        flood_duration_hours=24.0,
        pier_diameter_m=0.50,
        approach_depth_m=4.00,  # y_1 / a* = 8.0 > 6.0 exercises the 48.26 deep-flow branch
        planted_defect=planted_defect,
    )
    high_froude_csu_case = evaluate_pier_scour(
        flow_intensity_ratio=1.00,
        flood_duration_hours=24.0,
        pier_diameter_m=0.40,
        approach_depth_m=0.45,
        median_grain_d50_mm=45.0,
        critical_shields_theta_c=0.055,  # Fr_1 > 0.8 exercises the 3.0 * a* CSU cap
        csu_k1=1.1,
        csu_k2=1.4,
        csu_k3=1.1,
        planted_defect=planted_defect,
    )

    # Verify algebraic identity between the two published HEC-18 forms of f_3
    r_val = 2.00 / 0.002
    f3_form_a = r_val / (0.4 * (r_val ** 1.2) + 10.6 * (r_val ** -0.13))
    f3_form_b = (r_val ** 1.13) / (0.4 * (r_val ** 1.33) + 10.6)

    failures: list[str] = []
    if abs(f3_form_a - f3_form_b) > 1e-12:
        failures.append("Sheppard-Melville f_3 algebraic forms diverged")
    expected_deep_te = 48.26 * (0.50 / deep_flow_case["approach_velocity_v1_m_s"]) * (0.85 - 0.4)
    if abs(deep_flow_case["exact_te_days"] - expected_deep_te) > 0.02:
        failures.append(f"Deep-flow y_1/a* > 6.0 branch failed 48.26 time-scale check: {deep_flow_case['exact_te_days']}")
    if high_froude_csu_case["froude_1"] <= 0.8 or abs(high_froude_csu_case["exact_ys_csu_eq_m"] - 3.0 * 0.40) > 1e-9:
        failures.append(
            f"High-Froude CSU 3.0*a* cap check failed: Fr_1={high_froude_csu_case['froude_1']}, y_s,CSU={high_froude_csu_case['ys_csu_eq_m']}"
        )
    if not (flash_2h["exact_ys_transient_m"] < default_24h["exact_ys_transient_m"] < multiday_120h["exact_ys_transient_m"]):
        failures.append("Transient scour depth y_s(t_d) must strictly grow from 2 h to 24 h to 120 h under sub-equilibrium flow")
    if default_24h["exact_kt_factor"] >= 0.90 or flash_2h["exact_kt_factor"] >= 0.60:
        failures.append(
            f"Time-scale lag factor K_t failed flash-flood attenuation bounds (2h={flash_2h['time_factor_kt']}, 24h={default_24h['time_factor_kt']})"
        )
    if default_24h["f3_coarseness"] >= 0.75:
        failures.append(
            f"Grain-coarseness factor f_3={default_24h['f3_coarseness']} failed to attenuate sand-scale pier ratio a*/d_50=1000"
        )
    if not (default_24h["exact_ys_transient_m"] < default_24h["exact_ys_csu_eq_m"] < default_24h["exact_ys_sm_eq_m"]):
        failures.append("Expected 24h ordering y_s(24h) < y_s,CSU,eq < y_s,SM,eq violated at V_1/V_c=0.85")
    if not (post_eq_low_intensity["exact_ys_sm_eq_m"] < post_eq_low_intensity["exact_ys_csu_eq_m"]):
        failures.append("Near-threshold V_1/V_c=0.45 must keep threshold-aware y_s,SM,eq below Froude-only y_s,CSU,eq")
    if threshold_peak_24h["exact_ys_sm_eq_m"] <= default_24h["exact_ys_sm_eq_m"]:
        failures.append("Equilibrium clear-water scour y_s,SM must peak at incipient live-bed threshold V_1/V_c = 1.00")
    if abs(post_eq_low_intensity["exact_kt_factor"] - 1.0) > 1e-9:
        failures.append("Post-equilibrium clamp failed when t_d = 240 h exceeds t_e = 212.0 h at V_1/V_c = 0.45")

    # Domain rejection checks
    for bad_label, bad_kwargs in (
        ("sub-threshold V_1/V_c = 0.35", {"flow_intensity_ratio": 0.35}),
        ("live-bed V_1/V_c = 1.15", {"flow_intensity_ratio": 1.15}),
        ("zero flood duration", {"flood_duration_hours": 0.0}),
        ("non-submerged density s = 0.95", {"specific_gravity_s": 0.95}),
        ("roughness 5.53*y_1/d_50 <= 1", {"approach_depth_m": 0.01, "median_grain_d50_mm": 60.0}),
        ("boolean intensity", {"flow_intensity_ratio": True}),
        ("NaN intensity", {"flow_intensity_ratio": float("nan")}),
    ):
        try:
            evaluate_pier_scour(**bad_kwargs)
            failures.append(f"Domain guard failed to reject {bad_label}")
        except ValueError:
            pass

    status = "FAIL" if failures else "PASS"
    return {
        "status": status,
        "folio": "E.16",
        "planted_defect": planted_defect,
        "default_24h_flood": default_24h,
        "flash_2h_flood": flash_2h,
        "multiday_120h_flood": multiday_120h,
        "threshold_peak_24h": threshold_peak_24h,
        "post_eq_low_intensity_240h": post_eq_low_intensity,
        "failures": failures,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify Folio E.16 Bridge Pier Scour & Flood Time-Scale Lag model.")
    parser.add_argument("--planted-defect", action="store_true", help="Set f_3=1 and K_t=1 (must fail).")
    args = parser.parse_args(argv)
    result = run_checks(planted_defect=args.planted_defect)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
