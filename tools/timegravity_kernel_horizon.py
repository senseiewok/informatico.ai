#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Horizon-thermodynamics kernel for the Time & Gravity track (T.08, standard library only).

T.08  A Horizon Has a Temperature:
      1. A clock with uniform proper acceleration a follows the hyperbolic Rindler worldline
         x(τ) = (c²/a) cosh(aτ/c), t(τ) = (c/a) sinh(aτ/c), seeing a causal horizon at x = ±ct.
      2. Restricting a Minkowski vacuum mode of frequency ω across the Left and Right Rindler wedges yields the
         two-mode squeezed state |Ψ(ξ)⟩ = Z_d(ξ)^{-1/2} Σ_{n=0}^{d-1} exp(-n ξ / 2) |n_L⟩ ⊗ |n_R⟩ with dimensionless
         Boltzmann exponent ξ = 2π ω c / a = ħ ω / (k_B T_U), where T_U = ħ a / (2π k_B c) is the Unruh temperature
         (SI dimensional check: [ħ a / c] = (J·s)(m/s²)/(m/s) = J; dividing by k_B gives K).
      3. Tracing out the hidden Left wedge gives ρ_R = Tr_L(|Ψ⟩⟨Ψ|). Embedded in a dense rotated basis and
         diagonalised with the track's pure-Python Jacobi solver, the eigenvalues of ρ_R match the truncated Gibbs
         weights exp(-n ξ)/Z_d(ξ) to < 1e-12 for every ξ > 0, and at ξ >= 2.0 (where Fock truncation leakage
         exp(-d ξ) <= exp(-32) = 1.27e-14 for d = 16) match the infinite-dimensional Planck distribution
         p_n = (1 - exp(-ξ)) exp(-n ξ), Bose-Einstein occupation n̄ = 1/(exp(ξ) - 1), and thermal von Neumann
         entropy S = ξ/(exp(ξ) - 1) - ln(1 - exp(-ξ)) to < 1e-12.
      4. Substituting Schwarzschild surface gravity κ = c⁴/(4GM) gives Hawking's temperature T_H = ħ c³/(8π G M k_B)
         (61.7 nK at M = M_sun) and, integrated through the Bardeen-Carter-Hawking first law dE = c² dM = T_H dS =
         (κ c² / 8π G) dA ( checked by Gauss-Legendre quadrature and central differences), fixes the Bekenstein-Hawking
         entropy coefficient at S_BH = k_B A / (4 ℓ_P²) with ℓ_P² = ħ G / c³.
      5. Planted defect (and instrument knockout): severing the entanglement across the horizon (product state
         |0_L⟩ ⊗ |0_R⟩) collapses the reduced state's entropy to zero and fails the Planck-spectrum check.
"""
from __future__ import annotations

import json
import math
import sys

from timegravity_kernel import C, G0
from timegravity_kernel_quantum import jacobi_eigen

HBAR = 1.054571817e-34              # J·s (exact SI 2019)
K_B = 1.380649e-23                  # J/K (exact SI 2019)
G_NEWTON = 6.67430e-11              # m³ kg⁻¹ s⁻² (CODATA)
M_SUN = 1.98847e30                  # kg (nominal solar mass)
T_CMB_K = 2.72548                   # K (Fixsen 2009 / COBE FIRAS blackbody temperature)
L_PLANCK_SQ = HBAR * G_NEWTON / (C ** 3)
L_PLANCK = math.sqrt(L_PLANCK_SQ)

FOCK_D = 16                         # Fock levels per wedge; 16x16 bipartition = 256 states
XI_DEFAULT = 2.5                    # βħω = 2π ω c / κ; at d=16, exp(-16 * 2.5) = 4.25e-18 << 1e-12
HORIZON_TOL = 1e-12


def unruh_temperature(accel_m_s2: float) -> float:
    """T_U = ħ a / (2π k_B c) in Kelvin for proper acceleration or surface gravity a (m/s²)."""
    return HBAR * accel_m_s2 / (2.0 * math.pi * K_B * C)


def rindler_worldline(accel_m_s2: float = G0, tau_max: float = 1.0, n_steps: int = 80) -> dict:
    """Hyperbolic Rindler trajectory in dimensionless variables u = a t / c, v = a x / c² across u_tau = a τ / c."""
    samples = []
    max_invariant_err = 0.0
    max_four_vel_err = 0.0
    for i in range(n_steps + 1):
        eta = -1.2 + 2.4 * (i / n_steps)     # dimensionless rapidity η = a τ / c
        v_x = math.cosh(eta)                 # x / (c²/a)
        u_t = math.sinh(eta)                 # c t / (c²/a)
        inv_err = abs((v_x * v_x - u_t * u_t) - 1.0)
        # dx/dτ = c sinh(η), c dt/dτ = c cosh(η) => (c dt/dτ)² - (dx/dτ)² = c²
        vel_err = abs((math.cosh(eta) ** 2 - math.sinh(eta) ** 2) - 1.0)
        max_invariant_err = max(max_invariant_err, inv_err)
        max_four_vel_err = max(max_four_vel_err, vel_err)
        samples.append({"rapidity": eta, "ct_over_x0": u_t, "x_over_x0": v_x})
    return {
        "accel_m_s2": accel_m_s2,
        "horizon_distance_x0_m": (C * C) / accel_m_s2,
        "unruh_temp_k": unruh_temperature(accel_m_s2),
        "max_hyperbola_invariant_err": max_invariant_err,
        "max_four_velocity_norm_err": max_four_vel_err,
        "samples": samples,
    }


def planck_exact(xi: float) -> dict:
    """Exact infinite-dimensional single-mode Planck/Gibbs statistics at ξ = βħω > 0."""
    ex = math.exp(-xi)
    one_minus = -math.expm1(-xi)             # 1 - exp(-ξ)
    n_bar = ex / one_minus                   # 1 / (exp(ξ) - 1)
    entropy = (xi * ex / one_minus) - math.log(one_minus)
    return {
        "xi": xi,
        "n_bar": n_bar,
        "entropy_nats": entropy,
        "p0": one_minus,
    }


def _orthogonal_dct_matrix(d: int) -> list[list[float]]:
    """Exact Type-II orthogonal discrete cosine transform matrix on R^d (U U^T = I) to embed ρ_R as a dense matrix
    before diagonalising with the pure-Python Jacobi solver (so Jacobi cannot cheat on an already-diagonal input)."""
    u = [[0.0] * d for _ in range(d)]
    for r in range(d):
        scale = math.sqrt(1.0 / d) if r == 0 else math.sqrt(2.0 / d)
        for c in range(d):
            u[r][c] = scale * math.cos(math.pi * r * (2 * c + 1) / (2.0 * d))
    return u


def two_mode_squeezed_wedge(xi: float = XI_DEFAULT, d: int = FOCK_D, planted_defect: bool = False) -> dict:
    """Build the two-mode squeezed state |Ψ(ξ)⟩ on H_L ⊗ H_R (dim d²), take the partial trace ρ_R = Tr_L(|Ψ⟩⟨Ψ|),
    rotate ρ_R into a dense symmetric matrix via DCT-II, diagonalise with Jacobi, and compare against both the
    truncated Gibbs distribution and (for ξ >= 2.0) the infinite-dimensional Planck formula."""
    if planted_defect:
        # Planted defect / knockout: sever entanglement across the horizon (product state |0_L⟩ ⊗ |0_R⟩)
        amps = [1.0 if n == 0 else 0.0 for n in range(d)]
    else:
        raw = [math.exp(-0.5 * n * xi) for n in range(d)]
        norm = math.sqrt(sum(a * a for a in raw))
        amps = [a / norm for a in raw]

    # Full bipartite state vector ψ_{m,n} on d × d Fock space (index m * d + n)
    psi = [0.0] * (d * d)
    for n in range(d):
        psi[n * d + n] = amps[n]

    # Partial trace over Left wedge: (ρ_R)_{n, n'} = Σ_m ψ_{m, n} ψ_{m, n'}
    rho_r = [[0.0] * d for _ in range(d)]
    for n in range(d):
        for np_ in range(d):
            rho_r[n][np_] = sum(psi[m * d + n] * psi[m * d + np_] for m in range(d))

    # Rotate into a dense real symmetric matrix M = U ρ_R U^T and diagonalise with Jacobi
    u = _orthogonal_dct_matrix(d)
    tmp = [[sum(rho_r[i][k] * u[j][k] for k in range(d)) for j in range(d)] for i in range(d)]
    dense = [[sum(u[i][k] * tmp[k][j] for k in range(d)) for j in range(d)] for i in range(d)]
    eigvals, _ = jacobi_eigen(dense, tol=1e-14, max_sweeps=80)
    eigvals_sorted = sorted((max(0.0, val) for val in eigvals), reverse=True)

    # Exact truncated Gibbs probabilities
    z_d = sum(math.exp(-n * xi) for n in range(d))
    gibbs_trunc = [math.exp(-n * xi) / z_d for n in range(d)]
    # Exact infinite-dimensional Planck probabilities
    one_minus = -math.expm1(-xi)
    planck_inf = [one_minus * math.exp(-n * xi) for n in range(d)]

    s_jacobi = -sum(p * math.log(p) for p in eigvals_sorted if p > 1e-300)
    n_bar_jacobi = sum(n * p for n, p in enumerate(eigvals_sorted))
    exact_inf = planck_exact(xi)

    max_dev_trunc = max(abs(eigvals_sorted[n] - gibbs_trunc[n]) for n in range(d))
    max_dev_planck = max(abs(eigvals_sorted[n] - planck_inf[n]) for n in range(d))
    entropy_dev_planck = abs(s_jacobi - exact_inf["entropy_nats"])
    n_bar_dev_planck = abs(n_bar_jacobi - exact_inf["n_bar"])
    trace_rho_sq = sum(p * p for p in eigvals_sorted)

    return {
        "xi": xi,
        "d": d,
        "truncation_tail": math.exp(-d * xi),
        "eigenvalues": eigvals_sorted,
        "planck_probabilities": planck_inf,
        "gibbs_truncated": gibbs_trunc,
        "entropy_jacobi_nats": s_jacobi,
        "entropy_planck_nats": exact_inf["entropy_nats"],
        "n_bar_jacobi": n_bar_jacobi,
        "n_bar_planck": exact_inf["n_bar"],
        "purity_tr_rho2": trace_rho_sq,
        "max_dev_from_truncated_gibbs": max_dev_trunc,
        "max_dev_from_planck": max_dev_planck,
        "entropy_dev_from_planck": entropy_dev_planck,
        "n_bar_dev_from_planck": n_bar_dev_planck,
    }


def schwarzschild_thermodynamics(mass_kg: float = M_SUN) -> dict:
    """Schwarzschild radius r_s, horizon area A, surface gravity κ, Hawking temperature T_H, and Bekenstein-Hawking
    entropy S_BH / k_B = A / (4 ℓ_P²) in SI units."""
    r_s = 2.0 * G_NEWTON * mass_kg / (C ** 2)
    area = 4.0 * math.pi * r_s * r_s
    kappa = (C ** 4) / (4.0 * G_NEWTON * mass_kg)
    t_hawking = unruh_temperature(kappa)
    t_hawking_closed = (HBAR * (C ** 3)) / (8.0 * math.pi * G_NEWTON * mass_kg * K_B)
    s_bh_over_kb = area / (4.0 * L_PLANCK_SQ)
    return {
        "mass_kg": mass_kg,
        "mass_solar": mass_kg / M_SUN,
        "r_s_m": r_s,
        "area_m2": area,
        "kappa_m_s2": kappa,
        "t_hawking_k": t_hawking,
        "t_hawking_closed_k": t_hawking_closed,
        "t_hawking_rel_diff": abs(t_hawking - t_hawking_closed) / t_hawking_closed,
        "s_bh_over_kb": s_bh_over_kb,
        "s_bh_joule_per_k": s_bh_over_kb * K_B,
        "t_cmb_over_t_hawking": T_CMB_K / t_hawking,
    }


# 5-point Gauss-Legendre nodes and weights on [-1, 1] (exact for polynomials up to degree 9)
_GL5_NODES = (
    -0.9061798459386640,
    -0.5384693101056831,
    0.0,
    0.5384693101056831,
    0.9061798459386640,
)
_GL5_WEIGHTS = (
    0.2369268850561891,
    0.4786286704993665,
    0.5688888888888889,
    0.4786286704993665,
    0.2369268850561891,
)


def first_law_area_check(mass_kg: float = M_SUN) -> dict:
    """Double-entry check of the Bekenstein-Hawking 1/4 coefficient:
    1. Integrate d(S/k_B) = c² dM / (k_B T_H(M)) from m = 0 to M using Gauss-Legendre quadrature and compare with
       A(M) / (4 ℓ_P²).
    2. Check the Bardeen-Carter-Hawking differential first law (κ c² / 8π G) (dA/dM) = c² by central finite
       differences."""
    # Quadrature of d(S/k_B)/dM = c² / (k_B T_H(m)) over [0, mass_kg]
    half = 0.5 * mass_kg
    s_quad_over_kb = 0.0
    for node, weight in zip(_GL5_NODES, _GL5_WEIGHTS):
        m_i = half * (node + 1.0)
        t_h_i = (HBAR * (C ** 3)) / (8.0 * math.pi * G_NEWTON * m_i * K_B)
        integrand = (C ** 2) / (K_B * t_h_i)
        s_quad_over_kb += half * weight * integrand

    bh = schwarzschild_thermodynamics(mass_kg)
    s_area_over_kb = bh["s_bh_over_kb"]
    quad_rel_err = abs(s_quad_over_kb - s_area_over_kb) / s_area_over_kb

    # Central finite difference for dA/dM at M
    dm = 1e-5 * mass_kg
    a_plus = schwarzschild_thermodynamics(mass_kg + dm)["area_m2"]
    a_minus = schwarzschild_thermodynamics(mass_kg - dm)["area_m2"]
    da_dm_num = (a_plus - a_minus) / (2.0 * dm)
    lhs_first_law = (bh["kappa_m_s2"] * (C ** 2) / (8.0 * math.pi * G_NEWTON)) * da_dm_num
    first_law_rel_err = abs(lhs_first_law - (C ** 2)) / (C ** 2)

    return {
        "s_quadrature_over_kb": s_quad_over_kb,
        "s_area_over_kb": s_area_over_kb,
        "quadrature_vs_area_quarter_rel_err": quad_rel_err,
        "bch_first_law_rel_err": first_law_rel_err,
    }


def check_horizon(planted_defect: bool = False) -> dict:
    """Acceptance gate for T.08."""
    rw = rindler_worldline(1.0e20)
    wedge = two_mode_squeezed_wedge(XI_DEFAULT, FOCK_D, planted_defect=planted_defect)
    bad_wedge = two_mode_squeezed_wedge(XI_DEFAULT, FOCK_D, planted_defect=True)
    bh_solar = schwarzschild_thermodynamics(M_SUN)
    fl = first_law_area_check(M_SUN)

    # Sweep across ξ to confirm truncated Gibbs agreement at all temperatures
    sweep_trunc_max_dev = max(
        two_mode_squeezed_wedge(xi, FOCK_D, planted_defect=planted_defect)["max_dev_from_truncated_gibbs"]
        for xi in (0.5, 1.0, 1.5, 2.0, 2.5, 4.0)
    )

    worldline_ok = rw["max_hyperbola_invariant_err"] < HORIZON_TOL and rw["max_four_velocity_norm_err"] < HORIZON_TOL
    planck_ok = (
        wedge["max_dev_from_planck"] < HORIZON_TOL
        and wedge["entropy_dev_from_planck"] < HORIZON_TOL
        and wedge["n_bar_dev_from_planck"] < HORIZON_TOL
        and sweep_trunc_max_dev < HORIZON_TOL
        and wedge["entropy_jacobi_nats"] > 0.1
    )
    first_law_ok = (
        fl["quadrature_vs_area_quarter_rel_err"] < HORIZON_TOL
        and fl["bch_first_law_rel_err"] < 1e-10
        and bh_solar["t_hawking_rel_diff"] < HORIZON_TOL
    )
    defect_rejected = not (
        bad_wedge["max_dev_from_planck"] < HORIZON_TOL and bad_wedge["entropy_dev_from_planck"] < HORIZON_TOL
    )

    return {
        "xi_default": XI_DEFAULT,
        "fock_d": FOCK_D,
        "max_dev_from_planck": wedge["max_dev_from_planck"],
        "entropy_dev_from_planck": wedge["entropy_dev_from_planck"],
        "n_bar_dev_from_planck": wedge["n_bar_dev_from_planck"],
        "sweep_truncated_gibbs_max_dev": sweep_trunc_max_dev,
        "entropy_jacobi_nats": wedge["entropy_jacobi_nats"],
        "n_bar_jacobi": wedge["n_bar_jacobi"],
        "unruh_temp_at_1e20_m_s2_k": rw["unruh_temp_k"],
        "solar_hawking_temp_k": bh_solar["t_hawking_k"],
        "solar_s_bh_over_kb": bh_solar["s_bh_over_kb"],
        "quadrature_vs_area_quarter_rel_err": fl["quadrature_vs_area_quarter_rel_err"],
        "bch_first_law_rel_err": fl["bch_first_law_rel_err"],
        "max_hyperbola_invariant_err": rw["max_hyperbola_invariant_err"],
        "planted_entropy_nats": bad_wedge["entropy_jacobi_nats"],
        "planted_max_dev_from_planck": bad_wedge["max_dev_from_planck"],
        "worldline_ok": worldline_ok,
        "planck_ok": planck_ok,
        "first_law_ok": first_law_ok,
        "defect_rejected": defect_rejected,
        "ok": bool(worldline_ok and planck_ok and first_law_ok and defect_rejected),
    }


if __name__ == "__main__":
    res = check_horizon(planted_defect="--planted-defect" in sys.argv)
    print(json.dumps(res, indent=2))
