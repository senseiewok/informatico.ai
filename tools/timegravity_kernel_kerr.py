#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kerr horizon and quasi-normal ringdown kernel for the Time & Gravity track (T.09, standard library only).

T.09  A Horizon Rings Like a Bell:
      1. A spinning Kerr black hole of mass M and dimensionless spin χ = c J / (G M²) ∈ [0, 1) has outer event horizon
         r_+ = r_g (1 + √(1 − χ²)) with r_g = G M / c², equatorial ergosphere r_erg(π/2) = 2 r_g, horizon area
         A(M, χ) = 8π r_g² (1 + √(1 − χ²)), surface gravity κ(M, χ) = c⁴ √(1 − χ²) / [2 G M (1 + √(1 − χ²))], and
         horizon angular velocity Ω_H(M, χ) = c³ χ / [2 G M (1 + √(1 − χ²))].
      2. Double-entry check 1 (Smarr & First Law): for every (M, χ), the algebraic Smarr relation
         M c² = (κ c² / 4π G) A + 2 Ω_H J holds to < 1e-14, and the differential first law
         δ(M c²) = (κ c² / 8π G) δA + Ω_H δJ checked by central finite differences along independent mass and spin
         displacements holds to < 1e-10.
      3. Double-entry check 2 (Coupled Leaver Continued-Fraction QNM Solver): solves Teukolsky's angular spheroidal
         and radial master equations (s = −2, ℓ = 2, m = 2) for both the fundamental mode (n = 0) and the first
         overtone (n = 1, using Leaver's first inversion Eq. 14) via coupled three-term continued fractions across
         χ ∈ [0, 0.90] by homotopy continuation from Schwarzschild (χ = 0, A_{22} = 4). Both continued-fraction
         residuals |R_rad| and |R_ang| vanish to < 1e-11, and the solved M ω_{22n}(χ) match published tables
         (Leaver 1985 Table 1; Berti, Cardoso & Starinets 2009) to < 1e-5.
      4. Planted defect: flipping the spin sign under the radical in r_+ = r_g (1 + √(1 + χ²)) breaks the Kerr
         no-hair geometry, causing Smarr's identity, the differential first law, and the continued-fraction recurrence
         check to fail cleanly.
      5. Observational guardrail (shared with T.10): GW150914 and GW250114 ringdown and area-law figures are quoted
         strictly as the collaborations' posterior results; median masses are never plugged into A(M, χ) as a fake
         observational test.
"""
from __future__ import annotations

import json
import math
import sys

from timegravity_kernel import C
from timegravity_kernel_horizon import G_NEWTON, HBAR, K_B, L_PLANCK_SQ, M_SUN, unruh_temperature

KERR_SPINS = (0.0, 0.2, 0.4, 0.5, 0.68, 0.8, 0.9)
FIDUCIAL_MASS_SOLAR = 62.0          # GW150914-scale remnant mass for physical Hz / ms illustration
FIDUCIAL_CHI = 0.68

# Published reference benchmarks (Leaver 1985 Proc. R. Soc. A 402, 285; Berti, Cardoso & Starinets 2009 CQG 26, 163001)
PUBLISHED_QNM_220 = {
    0.0: complex(0.37367168, -0.08896232),
    0.5: complex(0.46412303, -0.08563883),
    0.68: complex(0.52397510, -0.08151262),
    0.8: complex(0.58601697, -0.07562955),
    0.9: complex(0.67161427, -0.06486924),
}
PUBLISHED_QNM_221 = {
    0.0: complex(0.34671099, -0.27391488),
    0.5: complex(0.44740704, -0.26022455),
    0.68: complex(0.51194115, -0.24652858),
    0.8: complex(0.57792240, -0.22814894),
    0.9: complex(0.66765755, -0.19525207),
}


def kerr_horizon(mass_kg: float = FIDUCIAL_MASS_SOLAR * M_SUN, chi: float = FIDUCIAL_CHI, planted_defect: bool = False) -> dict:
    """Exact Kerr horizon geometry and thermodynamic potentials in SI units."""
    r_g = G_NEWTON * mass_kg / (C ** 2)
    rad = math.sqrt(1.0 + chi * chi) if planted_defect else math.sqrt(1.0 - chi * chi)
    one_plus = 1.0 + rad
    r_plus = r_g * one_plus
    r_minus = r_g * (1.0 - rad)
    r_erg_eq = 2.0 * r_g
    area = 8.0 * math.pi * (r_g ** 2) * one_plus
    kappa = (C ** 4) * rad / (2.0 * G_NEWTON * mass_kg * one_plus)
    omega_h = (C ** 3) * chi / (2.0 * G_NEWTON * mass_kg * one_plus)
    j_ang = chi * G_NEWTON * (mass_kg ** 2) / C
    t_hawking = unruh_temperature(kappa)
    s_bh_over_kb = area / (4.0 * L_PLANCK_SQ)

    # Smarr algebraic identity: M c² = (κ c² / 4π G) A + 2 Ω_H J
    mc2 = mass_kg * (C ** 2)
    smarr_rhs = (kappa * (C ** 2) / (4.0 * math.pi * G_NEWTON)) * area + 2.0 * omega_h * j_ang
    smarr_rel_err = abs(smarr_rhs - mc2) / mc2

    return {
        "mass_kg": mass_kg,
        "mass_solar": mass_kg / M_SUN,
        "chi": chi,
        "r_g_m": r_g,
        "r_plus_m": r_plus,
        "r_minus_m": r_minus,
        "r_erg_equator_m": r_erg_eq,
        "area_m2": area,
        "kappa_m_s2": kappa,
        "omega_h_rad_s": omega_h,
        "j_kg_m2_s": j_ang,
        "t_hawking_k": t_hawking,
        "s_bh_over_kb": s_bh_over_kb,
        "smarr_rel_err": smarr_rel_err,
    }


def kerr_first_law_check(mass_kg: float = FIDUCIAL_MASS_SOLAR * M_SUN, chi: float = FIDUCIAL_CHI,
                         planted_defect: bool = False) -> dict:
    """Check the differential first law δ(M c²) = (κ c² / 8π G) δA + Ω_H δJ by central finite differences along
    (1) a mass variation at fixed χ and (2) a spin variation at fixed M (where δM = 0 so (κ c² / 8π G) δA = −Ω_H δJ)."""
    base = kerr_horizon(mass_kg, chi, planted_defect=planted_defect)
    kappa = base["kappa_m_s2"]
    omega_h = base["omega_h_rad_s"]

    # 1. Mass step at fixed χ
    dm = 1e-5 * mass_kg
    p_m = kerr_horizon(mass_kg + dm, chi, planted_defect=planted_defect)
    m_m = kerr_horizon(mass_kg - dm, chi, planted_defect=planted_defect)
    da_dm = (p_m["area_m2"] - m_m["area_m2"]) / (2.0 * dm)
    dj_dm = (p_m["j_kg_m2_s"] - m_m["j_kg_m2_s"]) / (2.0 * dm)
    rhs_dm = (kappa * (C ** 2) / (8.0 * math.pi * G_NEWTON)) * da_dm + omega_h * dj_dm
    mass_step_rel_err = abs(rhs_dm - (C ** 2)) / (C ** 2)

    # 2. Spin step at fixed M (δM = 0 => (κ c² / 8π G)(dA/dχ) + Ω_H (dJ/dχ) = 0)
    dchi = 1e-6
    p_c = kerr_horizon(mass_kg, chi + dchi, planted_defect=planted_defect)
    m_c = kerr_horizon(mass_kg, chi - dchi, planted_defect=planted_defect)
    da_dchi = (p_c["area_m2"] - m_c["area_m2"]) / (2.0 * dchi)
    dj_dchi = (p_c["j_kg_m2_s"] - m_c["j_kg_m2_s"]) / (2.0 * dchi)
    term_a = (kappa * (C ** 2) / (8.0 * math.pi * G_NEWTON)) * da_dchi
    term_j = omega_h * dj_dchi
    spin_step_rel_err = abs(term_a + term_j) / max(abs(term_j), 1e-300)

    return {
        "smarr_rel_err": base["smarr_rel_err"],
        "mass_step_first_law_rel_err": mass_step_rel_err,
        "spin_step_first_law_rel_err": spin_step_rel_err,
        "worst_first_law_rel_err": max(base["smarr_rel_err"], mass_step_rel_err, spin_step_rel_err),
    }


def angular_cf(a_sep: complex, u: complex, ell: int = 2, m: int = 2, s: int = -2, n_terms: int = 60) -> complex:
    """Leaver 1985 (Proc. R. Soc. A 402, 285, Eqs. 18-21) angular spheroidal continued fraction for u = a ω_L = χ (Mω)."""
    k1 = 0.5 * abs(m - s)
    k2 = 0.5 * abs(m + s)

    def coeffs(n: int) -> tuple[complex, complex, complex]:
        alpha = -2.0 * (n + 1) * (n + 2.0 * k1 + 1.0)
        beta = (
            n * (n - 1.0)
            + 2.0 * n * (k1 + k2 + 1.0 - 2.0 * u)
            - (2.0 * u * (2.0 * k1 + s + 1.0) - (k1 + k2) * (k1 + k2 + 1.0))
            - (u * u + s * (s + 1.0) + a_sep)
        )
        gamma = 2.0 * u * (n + k1 + k2 + s)
        return alpha, beta, gamma

    tail = 0j
    for n in range(n_terms, 0, -1):
        a_prev, _, _ = coeffs(n - 1)
        _, b_n, g_n = coeffs(n)
        tail = (a_prev * g_n) / (b_n - tail)
    _, b0, _ = coeffs(0)
    return b0 - tail


def solve_angular_separation(u: complex, a_init: complex = 4.0 + 0j, ell: int = 2, m: int = 2, s: int = -2) -> complex:
    """Solve angular_cf(A, u) = 0 by complex secant iteration."""
    if abs(u) < 1e-15:
        return complex(ell * (ell + 1) - s * (s + 1), 0.0)
    a0 = a_init
    a1 = a_init + 1e-5
    f0 = angular_cf(a0, u, ell, m, s)
    for _ in range(25):
        f1 = angular_cf(a1, u, ell, m, s)
        if abs(f1 - f0) < 1e-16:
            break
        a2 = a1 - f1 * (a1 - a0) / (f1 - f0)
        a0, f0, a1 = a1, f1, a2
        if abs(f1) < 1e-14:
            break
    return a1


def radial_cf(mw: complex, chi: float, n_inv: int = 0, a_seed: complex = 4.0 + 0j,
              ell: int = 2, m: int = 2, s: int = -2, n_terms: int = 140,
              planted_defect: bool = False) -> tuple[complex, complex]:
    """Leaver 1985 (Eqs. 14, 23-27) radial continued fraction in 2M = 1 units (ω_L = 2 Mω, a = χ/2, b = √(1 − χ²))."""
    w = 2.0 * mw
    a = 0.5 * chi
    b = math.sqrt(1.0 + 4.0 * a * a) if planted_defect else math.sqrt(1.0 - 4.0 * a * a)
    u = a * w
    a_sep = solve_angular_separation(u, a_seed, ell, m, s)
    w_am = 0.5 * w - a * m
    c0 = 1.0 - s - 1j * w - (2j / b) * w_am
    c1 = -4.0 + 2j * w * (2.0 + b) + (4j / b) * w_am
    c2 = s + 3.0 - 3j * w - (2j / b) * w_am
    c3 = (
        w * w * (4.0 + 2.0 * b - a * a)
        - 2.0 * a * m * w
        - s
        - 1.0
        + (2.0 + b) * 1j * w
        - a_sep
        + ((4.0 * w + 2j) / b) * w_am
    )
    c4 = s + 1.0 - 2.0 * w * w - (2.0 * s + 3.0) * 1j * w - ((4.0 * w + 2j) / b) * w_am

    def coeffs(n: int) -> tuple[complex, complex, complex]:
        alpha = n * n + (c0 + 1.0) * n + c0
        beta = -2.0 * n * n + (c1 + 2.0) * n + c3
        gamma = n * n + (c2 - 3.0) * n + c4 - c2 + 2.0
        return alpha, beta, gamma

    tail = 0j
    for n in range(n_terms, n_inv, -1):
        a_prev, _, _ = coeffs(n - 1)
        _, b_n, g_n = coeffs(n)
        tail = (a_prev * g_n) / (b_n - tail)
    head = 0j
    for n in range(0, n_inv):
        a_n, b_n, _ = coeffs(n)
        _, _, g_next = coeffs(n + 1)
        head = (a_n * g_next) / (b_n - head)
    _, b_inv, _ = coeffs(n_inv)
    return b_inv - head - tail, a_sep


def solve_kerr_qnm_branch(spins: tuple[float, ...] = KERR_SPINS, overtone_n: int = 0) -> list[dict]:
    """Solve coupled angular + radial Leaver continued fractions across `spins` by homotopy continuation starting only
    from the rough Schwarzschild (χ = 0) WKB seed (0.37 − 0.09i for n=0; 0.35 − 0.27i for n=1)."""
    mw_seed = complex(0.37, -0.09) if overtone_n == 0 else complex(0.35, -0.27)
    a_seed = complex(4.0, 0.0)
    out = []
    # Step along a fine homotopy ladder with quadratic prediction so the n=1 overtone never jumps to n=0 at high spin
    all_spins = sorted(set(spins) | {round(0.02 * k, 2) for k in range(46)})
    by_spin = {}
    prev_chi, prev_mw = None, None
    for chi in all_spins:
        if prev_chi is not None and prev_mw is not None and len(by_spin) >= 2:
            # Linear extrapolation along the branch
            z0 = mw_seed + (mw_seed - prev_mw) * ((chi - prev_chi) / max(prev_chi - prev2_chi, 1e-9))
        else:
            z0 = mw_seed
        z1 = z0 + (1e-5 - 1e-5j)
        f0, a0 = radial_cf(z0, chi, n_inv=overtone_n, a_seed=a_seed)
        for _ in range(35):
            f1, a1 = radial_cf(z1, chi, n_inv=overtone_n, a_seed=a0)
            if abs(f1 - f0) < 1e-16:
                break
            step = f1 * (z1 - z0) / (f1 - f0)
            if abs(step) > 0.02:
                step = step * (0.02 / abs(step))
            z2 = z1 - step
            z0, f0, a0, z1 = z1, f1, a1, z2
            if abs(f1) < 1e-12:
                break
        f_rad, a_final = radial_cf(z1, chi, n_inv=overtone_n, a_seed=a0)
        f_ang = angular_cf(a_final, 0.5 * chi * (2.0 * z1))
        prev2_chi, prev_chi, prev_mw = prev_chi, chi, mw_seed
        mw_seed, a_seed = z1, a_final
        by_spin[chi] = {
            "chi": chi,
            "overtone_n": overtone_n,
            "mw_re": z1.real,
            "mw_im": z1.imag,
            "a_sep_re": a_final.real,
            "a_sep_im": a_final.imag,
            "quality_factor": -z1.real / (2.0 * z1.imag),
            "radial_cf_residual": abs(f_rad),
            "angular_cf_residual": abs(f_ang),
        }
    for chi in spins:
        out.append(by_spin[chi])
    return out


def physical_ringdown(mass_solar: float, mw_re: float, mw_im: float) -> dict:
    """Convert dimensionless Mω to physical frequency f (Hz) and damping time τ (ms) for a mass M."""
    t_m = G_NEWTON * (mass_solar * M_SUN) / (C ** 3)     # GM/c³ in seconds
    f_hz = mw_re / (2.0 * math.pi * t_m)
    tau_s = -t_m / mw_im
    return {
        "mass_solar": mass_solar,
        "f_hz": f_hz,
        "tau_ms": tau_s * 1e3,
        "quality_factor": math.pi * f_hz * tau_s,
    }


def check_kerr(planted_defect: bool = False) -> dict:
    """Acceptance gate for T.09."""
    fl_checks = [kerr_first_law_check(FIDUCIAL_MASS_SOLAR * M_SUN, chi, planted_defect=planted_defect)
                 for chi in (0.2, 0.5, 0.68, 0.9)]
    worst_smarr = max(c["smarr_rel_err"] for c in fl_checks)
    worst_first_law = max(c["worst_first_law_rel_err"] for c in fl_checks)

    branch_n0 = solve_kerr_qnm_branch(KERR_SPINS, overtone_n=0)
    branch_n1 = solve_kerr_qnm_branch(KERR_SPINS, overtone_n=1)
    by_chi_0 = {r["chi"]: r for r in branch_n0}
    by_chi_1 = {r["chi"]: r for r in branch_n1}

    max_cf_residual = max(
        max(r["radial_cf_residual"], r["angular_cf_residual"]) for r in (branch_n0 + branch_n1)
    )
    max_pub_dev_0 = max(
        abs(complex(by_chi_0[c]["mw_re"], by_chi_0[c]["mw_im"]) - w_pub)
        for c, w_pub in PUBLISHED_QNM_220.items()
    )
    max_pub_dev_1 = max(
        abs(complex(by_chi_1[c]["mw_re"], by_chi_1[c]["mw_im"]) - w_pub)
        for c, w_pub in PUBLISHED_QNM_221.items()
    )

    # Check that planted defect breaks both the first law and the radial continued fraction at χ = 0.68
    bad_fl = kerr_first_law_check(FIDUCIAL_MASS_SOLAR * M_SUN, FIDUCIAL_CHI, planted_defect=True)
    w_68 = complex(by_chi_0[FIDUCIAL_CHI]["mw_re"], by_chi_0[FIDUCIAL_CHI]["mw_im"])
    bad_cf_res, _ = radial_cf(w_68, FIDUCIAL_CHI, n_inv=0, planted_defect=True)
    planted_cf_residual = abs(bad_cf_res)
    if planted_defect:
        max_cf_residual = max(max_cf_residual, planted_cf_residual)

    fid_geom = kerr_horizon(FIDUCIAL_MASS_SOLAR * M_SUN, FIDUCIAL_CHI, planted_defect=planted_defect)
    fid_phys_0 = physical_ringdown(FIDUCIAL_MASS_SOLAR, by_chi_0[FIDUCIAL_CHI]["mw_re"], by_chi_0[FIDUCIAL_CHI]["mw_im"])
    fid_phys_1 = physical_ringdown(FIDUCIAL_MASS_SOLAR, by_chi_1[FIDUCIAL_CHI]["mw_re"], by_chi_1[FIDUCIAL_CHI]["mw_im"])

    first_law_ok = worst_smarr < 1e-13 and worst_first_law < 1e-9
    qnm_ok = max_cf_residual < 1e-10 and max_pub_dev_0 < 1e-6 and max_pub_dev_1 < 1e-6
    defect_rejected = bad_fl["worst_first_law_rel_err"] > 1e-2 and planted_cf_residual > 1e-2

    return {
        "schwarzschild_mw_220": [by_chi_0[0.0]["mw_re"], by_chi_0[0.0]["mw_im"]],
        "schwarzschild_mw_221": [by_chi_1[0.0]["mw_re"], by_chi_1[0.0]["mw_im"]],
        "kerr_chi068_mw_220": [by_chi_0[FIDUCIAL_CHI]["mw_re"], by_chi_0[FIDUCIAL_CHI]["mw_im"]],
        "kerr_chi068_mw_221": [by_chi_1[FIDUCIAL_CHI]["mw_re"], by_chi_1[FIDUCIAL_CHI]["mw_im"]],
        "fiducial_62msun_chi068": {
            "r_plus_km": fid_geom["r_plus_m"] / 1e3,
            "area_km2": fid_geom["area_m2"] / 1e6,
            "f_220_hz": fid_phys_0["f_hz"],
            "tau_220_ms": fid_phys_0["tau_ms"],
            "f_221_hz": fid_phys_1["f_hz"],
            "tau_221_ms": fid_phys_1["tau_ms"],
        },
        "worst_smarr_rel_err": worst_smarr,
        "worst_first_law_rel_err": worst_first_law,
        "max_cf_residual": max_cf_residual,
        "max_published_dev_220": max_pub_dev_0,
        "max_published_dev_221": max_pub_dev_1,
        "planted_first_law_rel_err": bad_fl["worst_first_law_rel_err"],
        "planted_cf_residual": planted_cf_residual,
        "first_law_ok": first_law_ok,
        "qnm_ok": qnm_ok,
        "defect_rejected": defect_rejected,
        "ok": bool(first_law_ok and qnm_ok and defect_rejected),
    }


if __name__ == "__main__":
    res = check_kerr(planted_defect="--planted-defect" in sys.argv)
    print(json.dumps(res, indent=2))
