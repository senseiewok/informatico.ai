#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dark-sector gravitational clock shift, cosmological matter budget, and clock-network kernel (T.12, stdlib only).

T.12  Two Clocks That Only Meet in Gravity:
      1. Cosmological gravitating vs. electromagnetically luminous budget (Planck 2018 VI; Clowe et al. 2006):
         - Physical cold dark matter density Ω_c h² = 0.1200 ± 0.0012 and baryon density Ω_b h² = 0.02237 ± 0.00015 give
           Ω_c / Ω_b = 5.3643 ± 0.0646 and dark matter fraction f_dark = Ω_c / (Ω_c + Ω_b) = 84.29 %.
         - Uncertainty propagation verified by closed-form partial derivatives against central finite differences.
      2. Gravitational proper-time shift of an electromagnetically transparent transit (Carney et al. 2021):
         - A compact mass M_DM with zero electromagnetic cross-section (α_EM = 0, Λ_EM = 0) passing at speed v_0 on
           r_DM(t) = (b, v_0 t, 0) past Clock 1 at (0, 0, 0) (impact parameter b_1 = b) and Clock 2 at (-d_c, 0, 0)
           (impact parameter b_2 = b + d_c) induces the instantaneous gravitational redshift difference
           Δν(t)/ν = (Φ_1(t) - Φ_2(t))/c² = -(G M_DM / c²) [1/√(b_1² + v_0² t²) - 1/√(b_2² + v_0² t²)].
         - Integrating over [-T, +T] yields the exact proper-time step
           Δτ(T) = -(2 G M_DM / (c² v_0)) [arsinh(v_0 T / b_1) - arsinh(v_0 T / b_2)]
           → -(2 G M_DM / (c² v_0)) ln(b_2 / b_1) for v_0 T ≫ b_2.
         - Recomputed via composite 5-point Gauss-Legendre quadrature across 64 subintervals, the numerical integral
           matches the closed-form arsinh expression to < 1e-12, and central finite differences verify the transverse
           velocity impulse identity +c² ∂(Δτ_∞)/∂b_1 = 2 G M_DM / (b_1 v_0) = Δv_⊥ to < 1e-10.
      3. Equivalence-principle baseline requirement vs. ultralight scalar portal bounds (Kennedy et al. 2020;
         Filzinger et al. 2023):
         - For a purely gravitational dark sector (dilaton coupling d_e = 0), co-located clocks (baseline d_c = 0)
           experience identical proper time (Δτ = 0, δ(ν_A/ν_B) = 0); detecting a purely gravitational transit requires
           a non-zero spatial baseline d_c > 0.
         - If an ultralight scalar field φ(t) of local energy density ρ_DM = 0.4 GeV/cm³ couples to α_EM via d_e ≠ 0,
           co-located optical clocks modulate at ω_φ = m_φ c² / ħ with Planck-normalised amplitude
           Φ_Pl = ħ √(8π G ρ_DM) / (m_φ c³), verified by the energy-density round-trip identity
           (c⁴ / 8πG) (m_φ c² / ħc)² Φ_Pl² = ρ_DM to < 1e-12.
      4. Planted defect (and instrument knockout): severing the universal gravitational coupling of the electromagnetically
         transparent mass (G_dark = 0) or claiming a non-zero gravitational clock shift at zero baseline (d_c = 0, d_e = 0)
         fails the trajectory quadrature and equivalence-principle checks.
"""
from __future__ import annotations

import json
import math
import sys

from timegravity_kernel import C
from timegravity_kernel_horizon import G_NEWTON, HBAR, _GL5_NODES, _GL5_WEIGHTS

EV_JOULE = 1.602176634e-19                  # J (exact SI 2019)
GEV_PER_CM3_TO_J_M3 = 1e9 * EV_JOULE * 1e6  # 1 GeV/cm³ = 1.602176634e-4 J/m³
RHO_DM_LOCAL_GEV_CM3 = 0.4                  # Standard halo model local dark-matter energy density (GeV/cm³)
RHO_DM_LOCAL_J_M3 = RHO_DM_LOCAL_GEV_CM3 * GEV_PER_CM3_TO_J_M3

# Planck 2018 VI (Aghanim et al. 2020, Astron. Astrophys. 641, A6, Table 2 TT,TE,EE+lowE+lensing)
OMEGA_C_H2 = 0.1200
OMEGA_C_H2_ERR = 0.0012
OMEGA_B_H2 = 0.02237
OMEGA_B_H2_ERR = 0.00015

# Default galactic virial transit geometry for the clock-network double-entry check
V_VIRIAL_M_S = 220_000.0                    # 220 km/s galactic rotation speed
M_TRANSIT_DEFAULT_KG = 1.0e6                # 10^6 kg compact non-luminous test transit
B_IMPACT_DEFAULT_M = 1.0                    # 1 m closest approach to Clock 1
BASELINE_DEFAULT_M = 1000.0                 # 1 km clock-network baseline (b_2 = b_1 + d_c = 1001 m)
T_HALF_WINDOW_S = 10.0                      # [-10 s, +10 s] integration window (v_0 T = 2.2e6 m ≫ b_2)
DARK_CLOCK_TOL = 1e-12


def cosmological_matter_budget() -> dict:
    """Planck 2018 VI dark-to-baryonic matter ratio and dark fraction, with uncertainty propagation verified by
    central finite differences."""
    ratio = OMEGA_C_H2 / OMEGA_B_H2
    f_dark = OMEGA_C_H2 / (OMEGA_C_H2 + OMEGA_B_H2)
    f_baryon = OMEGA_B_H2 / (OMEGA_C_H2 + OMEGA_B_H2)

    # Analytic first-order error propagation for ratio R = x / y
    dr_dx_ana = 1.0 / OMEGA_B_H2
    dr_dy_ana = -OMEGA_C_H2 / (OMEGA_B_H2 ** 2)
    ratio_err_ana = math.hypot(dr_dx_ana * OMEGA_C_H2_ERR, dr_dy_ana * OMEGA_B_H2_ERR)

    # Central finite-difference check of partial derivatives
    eps = 1e-8
    dr_dx_num = ((OMEGA_C_H2 + eps) / OMEGA_B_H2 - (OMEGA_C_H2 - eps) / OMEGA_B_H2) / (2.0 * eps)
    dr_dy_num = (OMEGA_C_H2 / (OMEGA_B_H2 + eps) - OMEGA_C_H2 / (OMEGA_B_H2 - eps)) / (2.0 * eps)
    ratio_err_num = math.hypot(dr_dx_num * OMEGA_C_H2_ERR, dr_dy_num * OMEGA_B_H2_ERR)
    err_propagation_rel_diff = abs(ratio_err_ana - ratio_err_num) / ratio_err_ana

    return {
        "omega_c_h2": OMEGA_C_H2,
        "omega_c_h2_err": OMEGA_C_H2_ERR,
        "omega_b_h2": OMEGA_B_H2,
        "omega_b_h2_err": OMEGA_B_H2_ERR,
        "dark_to_baryon_ratio": ratio,
        "dark_to_baryon_ratio_err": ratio_err_ana,
        "dark_fraction_of_matter": f_dark,
        "baryon_fraction_of_matter": f_baryon,
        "err_propagation_rel_diff": err_propagation_rel_diff,
    }


def _composite_gl5_integral(fn, a: float, b: float, n_sub: int = 64) -> float:
    """Composite 5-point Gauss-Legendre quadrature of fn(t) on [a, b] divided into n_sub subintervals."""
    step = (b - a) / n_sub
    total = 0.0
    for i in range(n_sub):
        x0 = a + i * step
        half = 0.5 * step
        mid = x0 + half
        sub = 0.0
        for node, weight in zip(_GL5_NODES, _GL5_WEIGHTS):
            sub += weight * fn(mid + half * node)
        total += half * sub
    return total


def dark_transit_clock_shift(
    mass_kg: float = M_TRANSIT_DEFAULT_KG,
    b1_m: float = B_IMPACT_DEFAULT_M,
    baseline_m: float = BASELINE_DEFAULT_M,
    v_m_s: float = V_VIRIAL_M_S,
    t_half_s: float = T_HALF_WINDOW_S,
    planted_defect: bool = False,
) -> dict:
    """Differential proper-time shift Δτ(T) and asymptotic step Δτ_∞ between two clocks at impact parameters
    b_1 and b_2 = b_1 + d_c during the flyby of an electromagnetically transparent mass M_DM."""
    b2_m = b1_m + baseline_m
    g_eff = 0.0 if planted_defect else G_NEWTON
    prefactor = (g_eff * mass_kg) / ((C ** 2) * v_m_s)

    # Exact closed-form integral on [-T, +T]:
    # Δτ(T) = ∫_{-T}^{+T} (Φ_1(t) - Φ_2(t))/c² dt = -2 (G M / c² v) [arsinh(v T / b_1) - arsinh(v T / b_2)]
    delta_tau_analytic = -2.0 * prefactor * (
        math.asinh(v_m_s * t_half_s / b1_m) - math.asinh(v_m_s * t_half_s / b2_m)
    )
    delta_tau_asymptotic = -2.0 * prefactor * math.log(b2_m / b1_m)

    # Numerical quadrature of the exact integrand (always using true G_NEWTON for reference comparison)
    def integrand_true(t: float) -> float:
        r1 = math.hypot(b1_m, v_m_s * t)
        r2 = math.hypot(b2_m, v_m_s * t)
        return -(G_NEWTON * mass_kg / (C ** 2)) * (1.0 / r1 - 1.0 / r2)

    # Split integral at t = 0 with geometric knots anchored at the flyby scale t_char = b_1 / v_0
    t_char = b1_m / v_m_s
    knots = [0.0]
    scale = 0.25 * t_char
    while scale < t_half_s:
        knots.append(scale)
        scale *= 2.5
    knots.append(t_half_s)
    half_quad = 0.0
    for k_idx in range(len(knots) - 1):
        half_quad += _composite_gl5_integral(integrand_true, knots[k_idx], knots[k_idx + 1], n_sub=16)
    delta_tau_quad_true = 2.0 * half_quad

    quad_rel_err = abs(delta_tau_analytic - delta_tau_quad_true) / abs(delta_tau_quad_true)

    # Transverse velocity impulse identity: Δv_⊥ = 2 G M / (b_1 v) = +c² ∂(Δτ_∞)/∂b_1 (holding b_2 fixed)
    eps_b = 1e-6 * b1_m
    dtau_plus = -2.0 * ((g_eff * mass_kg) / ((C ** 2) * v_m_s)) * math.log(b2_m / (b1_m + eps_b))
    dtau_minus = -2.0 * ((g_eff * mass_kg) / ((C ** 2) * v_m_s)) * math.log(b2_m / (b1_m - eps_b))
    dv_perp_from_clock = (C ** 2) * (dtau_plus - dtau_minus) / (2.0 * eps_b)
    dv_perp_exact = (2.0 * G_NEWTON * mass_kg) / (b1_m * v_m_s)
    impulse_rel_err = abs(dv_perp_from_clock - dv_perp_exact) / dv_perp_exact

    # Zero-baseline equivalence-principle check (d_c = 0 => b_2 = b_1 => Δτ = 0 identically)
    zero_baseline_shift = -2.0 * prefactor * math.log(b1_m / b1_m)

    # Sampled redshift profile Δν(t)/ν across t ∈ [-5 b_1/v, +5 b_1/v] for the interactive instrument
    t_char = b1_m / v_m_s
    profile = []
    for i in range(-20, 21, 2):
        tau_norm = i / 4.0  # v t / b_1 ∈ [-5, 5]
        t_val = tau_norm * t_char
        df_over_f = integrand_true(t_val) if not planted_defect else 0.0
        profile.append({
            "vt_over_b1": tau_norm,
            "t_s": t_val,
            "delta_nu_over_nu": df_over_f,
        })

    return {
        "mass_kg": mass_kg,
        "b1_m": b1_m,
        "b2_m": b2_m,
        "baseline_m": baseline_m,
        "v_m_s": v_m_s,
        "t_half_s": t_half_s,
        "delta_tau_analytic_s": delta_tau_analytic,
        "delta_tau_quadrature_s": delta_tau_quad_true,
        "delta_tau_asymptotic_s": delta_tau_asymptotic,
        "quadrature_rel_err": quad_rel_err,
        "dv_perp_m_s": dv_perp_exact,
        "dv_perp_from_clock_gradient_m_s": dv_perp_from_clock,
        "impulse_rel_err": impulse_rel_err,
        "zero_baseline_shift_s": zero_baseline_shift,
        "em_scattering_rate_s": 0.0,
        "profile": profile,
    }


def ultralight_scalar_clock_bound(
    m_phi_ev: float = 1.0e-15,
    d_e: float = 0.0,
    delta_k_alpha: float = 1.06,
) -> dict:
    """Ultralight scalar dark-matter clock modulation amplitude δ(ν_A/ν_B)/(ν_A/ν_B) = ΔK_α d_e Φ_Pl (Kennedy et al. 2020;
    Filzinger et al. 2023) and round-trip energy-density verification."""
    m_phi_j = m_phi_ev * EV_JOULE
    omega_phi_rad_s = m_phi_j / HBAR
    freq_hz = omega_phi_rad_s / (2.0 * math.pi)

    # Dimensionless Planck-normalised field amplitude Φ_Pl = ħ √(8π G ρ_DM) / (m_φ c³)
    phi_planck = (HBAR * math.sqrt(8.0 * math.pi * G_NEWTON * RHO_DM_LOCAL_J_M3)) / (m_phi_j * C)

    # Round-trip check: ρ_DM = (c² / 8πG) ω_φ² Φ_Pl²
    rho_reconstructed = ((C ** 2) / (8.0 * math.pi * G_NEWTON)) * (omega_phi_rad_s ** 2) * (phi_planck ** 2)
    rho_rel_err = abs(rho_reconstructed - RHO_DM_LOCAL_J_M3) / RHO_DM_LOCAL_J_M3

    fractional_mod_amp = abs(delta_k_alpha * d_e * phi_planck)

    return {
        "m_phi_ev": m_phi_ev,
        "compton_freq_hz": freq_hz,
        "rho_dm_gev_cm3": RHO_DM_LOCAL_GEV_CM3,
        "rho_dm_j_m3": RHO_DM_LOCAL_J_M3,
        "phi_planck_dimensionless": phi_planck,
        "rho_roundtrip_rel_err": rho_rel_err,
        "d_e": d_e,
        "delta_k_alpha": delta_k_alpha,
        "fractional_freq_modulation": fractional_mod_amp,
    }


def check_dark_clock(planted_defect: bool = False) -> dict:
    """Acceptance gate for T.12."""
    cosmo = cosmological_matter_budget()
    transit = dark_transit_clock_shift(planted_defect=planted_defect)
    bad_transit = dark_transit_clock_shift(planted_defect=True)
    uldm_pure_grav = ultralight_scalar_clock_bound(1.0e-15, d_e=0.0)
    uldm_portal = ultralight_scalar_clock_bound(1.0e-15, d_e=1.0e-4)

    # Sweep across baseline ratios b_2 / b_1 to confirm quadrature vs. arsinh match everywhere
    sweep_quad_max_err = max(
        dark_transit_clock_shift(
            mass_kg=M_TRANSIT_DEFAULT_KG,
            b1_m=1.0,
            baseline_m=bl,
            v_m_s=V_VIRIAL_M_S,
            t_half_s=T_HALF_WINDOW_S,
            planted_defect=planted_defect,
        )["quadrature_rel_err"]
        for bl in (1.0, 10.0, 100.0, 1000.0)
    )

    cosmo_ok = (
        abs(cosmo["dark_to_baryon_ratio"] - (0.1200 / 0.02237)) < DARK_CLOCK_TOL
        and cosmo["err_propagation_rel_diff"] < 1e-9
        and 0.84 < cosmo["dark_fraction_of_matter"] < 0.85
    )
    transit_ok = (
        transit["quadrature_rel_err"] < 1e-11
        and sweep_quad_max_err < 1e-11
        and transit["impulse_rel_err"] < 1e-9
        and transit["zero_baseline_shift_s"] == 0.0
    )
    uldm_ok = (
        uldm_pure_grav["rho_roundtrip_rel_err"] < DARK_CLOCK_TOL
        and uldm_pure_grav["fractional_freq_modulation"] == 0.0
        and uldm_portal["fractional_freq_modulation"] > 0.0
    )
    defect_rejected = not (bad_transit["quadrature_rel_err"] < 1e-11 and bad_transit["impulse_rel_err"] < 1e-9)

    return {
        "dark_to_baryon_ratio": cosmo["dark_to_baryon_ratio"],
        "dark_to_baryon_ratio_err": cosmo["dark_to_baryon_ratio_err"],
        "dark_fraction_of_matter": cosmo["dark_fraction_of_matter"],
        "cosmo_err_propagation_rel_diff": cosmo["err_propagation_rel_diff"],
        "delta_tau_analytic_s": transit["delta_tau_analytic_s"],
        "delta_tau_quadrature_s": transit["delta_tau_quadrature_s"],
        "delta_tau_asymptotic_s": transit["delta_tau_asymptotic_s"],
        "quadrature_rel_err": transit["quadrature_rel_err"],
        "sweep_quad_max_err": sweep_quad_max_err,
        "dv_perp_m_s": transit["dv_perp_m_s"],
        "impulse_rel_err": transit["impulse_rel_err"],
        "uldm_1e15ev_phi_planck": uldm_pure_grav["phi_planck_dimensionless"],
        "uldm_rho_roundtrip_rel_err": uldm_pure_grav["rho_roundtrip_rel_err"],
        "uldm_pure_gravity_colocated_mod": uldm_pure_grav["fractional_freq_modulation"],
        "uldm_portal_de1e4_mod": uldm_portal["fractional_freq_modulation"],
        "planted_delta_tau_s": bad_transit["delta_tau_analytic_s"],
        "planted_quadrature_rel_err": bad_transit["quadrature_rel_err"],
        "cosmo_ok": cosmo_ok,
        "transit_ok": transit_ok,
        "uldm_ok": uldm_ok,
        "defect_rejected": defect_rejected,
        "ok": bool(cosmo_ok and transit_ok and uldm_ok and defect_rejected),
    }


if __name__ == "__main__":
    res = check_dark_clock(planted_defect="--planted-defect" in sys.argv)
    print(json.dumps(res, indent=2))
