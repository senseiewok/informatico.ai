#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rational SI dimensional homogeneity (AH-14), parameter provenance (AH-9), ±25% sensitivity envelopes (AH-11),
and complex-step derivative parity across the Time & Gravity (T.01–T.12) and Cross-Scale (ES.01–ES.06) kernels.

Pure-Python standard library only (`fractions.Fraction`, `cmath`, `math`).
Zero domain-external symbols: 100% physics & mathematics kernel.
"""
from __future__ import annotations

import cmath
from fractions import Fraction
import json
import math
from pathlib import Path
import sys

_TOOLS_DIR = str(Path(__file__).resolve().parent)
if _TOOLS_DIR not in sys.path:
    sys.path.insert(0, _TOOLS_DIR)

import timegravity_kernel_decoherence as k_dec
import timegravity_kernel_entangle as k_ent
import timegravity_kernel_isl as k_isl
import timegravity_kernel_ladder as k_lad

# Exact 7-component SI base dimension vector: (M, L, T, I, Theta, N, J)
SIDim = tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, Fraction]


def dim_vec(m: int = 0, l: int = 0, t: int = 0, i: int = 0, th: int = 0, n: int = 0, j: int = 0) -> SIDim:
    return (Fraction(m), Fraction(l), Fraction(t), Fraction(i), Fraction(th), Fraction(n), Fraction(j))


def dim_mul(a: SIDim, b: SIDim) -> SIDim:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def dim_div(a: SIDim, b: SIDim) -> SIDim:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def dim_pow(a: SIDim, p: int | Fraction) -> SIDim:
    pf = Fraction(p)
    return tuple(x * pf for x in a)  # type: ignore[return-value]


DIMLESS = dim_vec(0, 0, 0, 0, 0, 0, 0)
MASS = dim_vec(m=1)
LENGTH = dim_vec(l=1)
TIME = dim_vec(t=1)
TEMP = dim_vec(th=1)
VELOCITY = dim_div(LENGTH, TIME)
ACCEL = dim_div(LENGTH, dim_pow(TIME, 2))
FORCE = dim_mul(MASS, ACCEL)
ENERGY = dim_mul(FORCE, LENGTH)
ACTION = dim_mul(ENERGY, TIME)
FREQ = dim_pow(TIME, -1)
PRESSURE = dim_div(FORCE, dim_pow(LENGTH, 2))
VISCOSITY = dim_mul(PRESSURE, TIME)
DENSITY = dim_div(MASS, dim_pow(LENGTH, 3))
POTENTIAL = dim_pow(VELOCITY, 2)
BOLTZMANN_K = dim_div(ENERGY, TEMP)
GRAV_G = dim_vec(m=-1, l=3, t=-2)
MOMENTUM_DIFFUSION = dim_div(dim_pow(dim_mul(MASS, VELOCITY), 2), TIME)


# Explicit Parameter Provenance Ledger (Rule AH-9): every apparatus/recast constant tagged by class & primary source
PARAMETER_PROVENANCE_LEDGER: tuple[dict[str, object], ...] = (
    {
        "symbol": "G_NEWTON",
        "value_si": 6.67430e-11,
        "unit": "m^3 kg^-1 s^-2",
        "provenance_class": "empirical",
        "ledger_id": "T05-WESTPHAL2021",
        "source_locator": "CODATA 2018 / Westphal et al. 2021 Nature 591, 225",
    },
    {
        "symbol": "EW_S_MIN_M",
        "value_si": 52.0e-6,
        "unit": "m",
        "provenance_class": "empirical",
        "ledger_id": "T05-LEE2020",
        "source_locator": "Lee et al. 2020 PRL 124, 101101, Sec. II (minimum face separation 52 um)",
    },
    {
        "symbol": "EW_YUKAWA_EDGE_LAMBDA_M",
        "value_si": 38.6e-6,
        "unit": "m",
        "provenance_class": "empirical",
        "ledger_id": "T05-LEE2020",
        "source_locator": "Lee et al. 2020 PRL 124, 101101, Abstract (|alpha|=1 Yukawa 95% exclusion lambda < 38.6 um)",
    },
    {
        "symbol": "RECAST_SMEARED_SIGMA_95_M",
        "value_si": k_lad.EW_MATCH_SIGMA_M,
        "unit": "m",
        "provenance_class": "derived",
        "ledger_id": "T05-LEE2020",
        "source_locator": "tools/timegravity_kernel_recast.py projection onto J. G. Lee 2020 Table 11.4 signed -alpha95 (33.08 um -> 33.1 um)",
    },
    {
        "symbol": "XENONNT_R0_90_M",
        "value_si": 4.9e-10,
        "unit": "m",
        "provenance_class": "empirical",
        "ledger_id": "T06-XENON2026",
        "source_locator": "Aprile et al. 2026 PRL (XENONnT spontaneous radiation 90% CL R0 > 4.9e-10 m)",
    },
    {
        "symbol": "GS_R0_BOUND_M",
        "value_si": 0.54e-10,
        "unit": "m",
        "provenance_class": "empirical",
        "ledger_id": "T06-DONADI2021",
        "source_locator": "Donadi et al. 2021 Nat. Phys. 17, 74, Eq. 5 (Gran Sasso Ge 95% CL R0 > 0.54e-10 m)",
    },
    {
        "symbol": "BMV_M_KG",
        "value_si": 1.0e-14,
        "unit": "kg",
        "provenance_class": "phenomenological_heuristic",
        "ledger_id": "T05-BOSE2017",
        "source_locator": "Bose et al. 2017 PRL 119, 240401 benchmark nanocrystal proposal mass (unbuilt)",
    },
    {
        "symbol": "SCHUT_GAMMA_CRIT_S1",
        "value_si": 9.83e-3,
        "unit": "s^-1",
        "provenance_class": "derived",
        "ledger_id": "T05-SCHUT2024",
        "source_locator": "tools/timegravity_kernel_dispute_latest.py critical dephasing rate on Schut et al. 2024 PRR 6, 013199",
    },
)


def verify_si_dimensional_homogeneity(planted_defect: bool = False) -> dict[str, object]:
    """Verify exact rational SI dimensional balance across 16 governing equations of T.01–T.12 & ES.01–ES.06."""
    g_dim = dim_vec(m=-1, l=2, t=-2) if planted_defect else GRAV_G
    planck_len_sq = dim_div(dim_mul(ACTION, g_dim), dim_pow(VELOCITY, 3))

    equations: list[tuple[str, SIDim, SIDim]] = [
        # 1. T.01 Gravitational redshift Delta_f / f = g * dh / c^2
        ("T01_redshift_ratio", dim_div(dim_mul(ACCEL, LENGTH), dim_pow(VELOCITY, 2)), DIMLESS),
        # 2. T.01 Geodesic acceleration a = c^2 * d(Phi/c^2)/dz
        ("T01_geodesic_accel", dim_div(POTENTIAL, LENGTH), ACCEL),
        # 3. T.02 Relativistic proper-time invariant c^2 dtau^2 = c^2 dt^2 - dx^2
        ("T02_minkowski_interval", dim_mul(dim_pow(VELOCITY, 2), dim_pow(TIME, 2)), dim_pow(LENGTH, 2)),
        # 4. T.03 Weak-field Poisson equation nabla^2 Phi = 4 pi G rho
        ("T03_poisson_weak_field", dim_div(POTENTIAL, dim_pow(LENGTH, 2)), dim_mul(g_dim, DENSITY)),
        # 5. T.04 Zych-Brukner proper-time interferometric phase omega * g * dh * T / (2 c^2)
        ("T04_zych_brukner_phase", dim_div(dim_mul(dim_mul(FREQ, ACCEL), dim_mul(LENGTH, TIME)), dim_pow(VELOCITY, 2)), DIMLESS),
        # 6. T.05 BMV Newtonian entanglement cross-phase G m^2 T / (hbar d)
        ("T05_bmv_cross_phase", dim_div(dim_mul(dim_mul(g_dim, dim_pow(MASS, 2)), TIME), dim_mul(ACTION, LENGTH)), DIMLESS),
        # 7. T.05/ES.01 Dipole scattered thermal-photon rate Lambda_sc * dx^2 ~ c R^6 (k_B T / (hbar c))^9 dx^2
        (
            "T05_ES01_photon_scattering_rate",
            dim_mul(
                dim_mul(VELOCITY, dim_pow(LENGTH, 6)),
                dim_mul(dim_pow(dim_div(dim_mul(BOLTZMANN_K, TEMP), dim_mul(ACTION, VELOCITY)), 9), dim_pow(LENGTH, 2)),
            ),
            FREQ,
        ),
        # 8. T.05/ES.01 Epstein free-molecular damping rate gamma_m ~ P R^2 sqrt(m_gas / (k_B T)) / M
        (
            "T05_ES01_epstein_damping_rate",
            dim_div(
                dim_mul(
                    dim_mul(PRESSURE, dim_pow(LENGTH, 2)),
                    dim_pow(dim_div(MASS, dim_mul(BOLTZMANN_K, TEMP)), Fraction(1, 2)),
                ),
                MASS,
            ),
            FREQ,
        ),
        # 9. ES.01 Fluctuation-Dissipation identity D_p = gamma_m * M * k_B * T
        ("ES01_fluctuation_dissipation", dim_mul(dim_mul(FREQ, MASS), dim_mul(BOLTZMANN_K, TEMP)), MOMENTUM_DIFFUSION),
        # 10. ES.01 Stokes-Einstein diffusivity D_0 = k_B T / (6 pi eta R)
        (
            "ES01_stokes_einstein_diffusivity",
            dim_div(dim_mul(BOLTZMANN_K, TEMP), dim_mul(VISCOSITY, LENGTH)),
            dim_div(dim_pow(LENGTH, 2), TIME),
        ),
        # 11. T.06 Diosi-Penrose collapse rate 1/tau_DP = G m^2 / (hbar R)
        ("T06_diosi_penrose_rate", dim_div(dim_mul(g_dim, dim_pow(MASS, 2)), dim_mul(ACTION, LENGTH)), FREQ),
        # 12. T.06/ES.06 Oppenheim post-quantum classical gravity inequality l_P^2 * D_2 ~ T * sigma_a^2 * r_N^3 / G^2
        #     (Oppenheim et al. 2023 Eq. F16: l_P^2 D_2 in kg^2 m^-1 s = [2, -1, 1], so D_2 has units kg^2 m^-3 s = [2, -3, 1])
        (
            "T06_ES06_oppenheim_tradeoff",
            dim_mul(planck_len_sq, dim_vec(m=2, l=-3, t=1)),
            dim_div(dim_mul(TIME, dim_mul(dim_pow(ACCEL, 2), dim_pow(LENGTH, 3))), dim_pow(g_dim, 2)),
        ),
        # 13. T.08/T.10/ES.05 Bekenstein-Hawking / QES area term S_BH / k_B = A c^3 / (4 G hbar)
        (
            "T08_T10_ES05_qes_area_entropy",
            dim_div(dim_mul(dim_pow(LENGTH, 2), dim_pow(VELOCITY, 3)), dim_mul(g_dim, ACTION)),
            DIMLESS,
        ),
        # 14. T.09 Gravitational-wave strain amplitude h ~ G M / (c^2 r)
        ("T09_gw_strain", dim_div(dim_mul(g_dim, MASS), dim_mul(dim_pow(VELOCITY, 2), LENGTH)), DIMLESS),
        # 15. ES.03 Brinkman Darcy permeability kappa = mu * v / |nabla P| -> [L^2]
        (
            "ES03_brinkman_permeability",
            dim_div(dim_mul(VISCOSITY, VELOCITY), dim_div(PRESSURE, LENGTH)),
            dim_pow(LENGTH, 2),
        ),
        # 16. ES.03 Barato-Seifert Thermodynamic Uncertainty product Q_TUR = (Var(tau)/<tau>^2) * <tau> * Sigma_dot / k_B
        #     where Var(tau)/<tau>^2 is [T^2 / T^2], <tau> is [T], and Sigma_dot = dS_env/dt is [Energy / (Temp * T)]
        (
            "ES03_barato_seifert_tur",
            dim_div(
                dim_mul(
                    dim_div(dim_pow(TIME, 2), dim_pow(TIME, 2)),
                    dim_mul(TIME, dim_div(dim_div(ENERGY, TEMP), TIME)),
                ),
                BOLTZMANN_K,
            ),
            DIMLESS,
        ),
    ]

    mismatches = [name for name, lhs, rhs in equations if lhs != rhs]
    return {
        "checked_equations": len(equations),
        "mismatches": mismatches,
        "ok": len(mismatches) == 0,
    }


def verify_sensitivity_and_complex_step(planted_defect: bool = False) -> dict[str, object]:
    """Verify ±25% perturbation sensitivity envelopes (AH-11) and complex-step derivative parity (h = 1e-30)."""
    # 1. BMV entanglement negativity across ±25% mass & separation perturbations
    m0 = k_ent.BMV_M_KG
    d0 = k_ent.BMV_D_M
    dx0 = k_ent.BMV_DX_M
    t0 = k_ent.BMV_T_S
    neg_m_lo = k_ent.negativity(k_ent.four_branch_state(k_ent.branch_phases(0.75 * m0, d0, dx0, t0, "quantum")))
    neg_m_0 = k_ent.negativity(k_ent.four_branch_state(k_ent.branch_phases(1.00 * m0, d0, dx0, t0, "quantum")))
    neg_m_hi = k_ent.negativity(k_ent.four_branch_state(k_ent.branch_phases(1.25 * m0, d0, dx0, t0, "quantum")))

    # 2. Smeared-gravity plate mode ratio R(q, s; sigma) across ±25% around sigma_95 = EW_MATCH_SIGMA_M (33.1 um) at s = 52 um
    q_ew = 120.0 / k_isl.EW_R_OUT_M
    s_ew = k_isl.EW_S_MIN_M
    sig_95 = k_lad.EW_MATCH_SIGMA_M
    def_sig_lo = 1.0 - k_isl.plate_mode_ratio(q_ew, s_ew, 0.75 * sig_95)
    def_sig_0 = 1.0 - k_isl.plate_mode_ratio(q_ew, s_ew, 1.00 * sig_95)
    def_sig_hi = 1.0 - k_isl.plate_mode_ratio(q_ew, s_ew, 1.25 * sig_95)

    # 3. Cryogenic diamond scattered black-body photon rate across ±25% bath temperature around 4.0 K and ±20% Re(eps)
    r_qgem = k_dec.sphere_radius(1.0e-14, k_dec.DIAMOND_DENSITY)
    dx_qgem = 250.0e-6
    ph_t_lo = k_dec.photon_rate(dx_qgem, r_qgem, 0.75 * 4.0, 0.75 * 4.0)["scattering"]
    ph_t_0 = k_dec.photon_rate(dx_qgem, r_qgem, 1.00 * 4.0, 1.00 * 4.0)["scattering"]
    ph_t_hi = k_dec.photon_rate(dx_qgem, r_qgem, 1.25 * 4.0, 1.25 * 4.0)["scattering"]
    ph_eps_lo = k_dec.photon_rate(dx_qgem, r_qgem, 4.0, 4.0, eps=complex(0.80 * 5.7, 1.0e-4))["scattering"]
    ph_eps_hi = k_dec.photon_rate(dx_qgem, r_qgem, 4.0, 4.0, eps=complex(1.20 * 5.7, 1.0e-4))["scattering"]

    # 4. Oppenheim Eot-Wash diffusion ceiling suppression ratio
    opp = k_lad.diffusion_table()
    opp_suppression = opp["oppenheim_printed_ceiling"] / opp["eotwash"]["T_1e+03_r_N_1fm"]["ceiling"]

    # 5. Complex-step derivative parity Im(f(x + i*h))/h at h = 1e-30 (zero subtractive cancellation!)
    h_cs = 1.0e-30
    # Cross-phase Delta_phi(d) = G m^2 T / hbar * (1/(d - dx) + 1/(d + dx) - 2/d)
    pref = 6.67430e-11 * (m0 ** 2) * t0 / 1.054571817e-34
    dc = complex(d0, h_cs)
    f_complex = pref * (1.0 / (dc - dx0) + 1.0 / (dc + dx0) - 2.0 / dc)
    dphi_dd_cs = f_complex.imag / h_cs
    dphi_dd_exact = pref * (-1.0 / ((d0 - dx0) ** 2) - 1.0 / ((d0 + dx0) ** 2) + 2.0 / (d0 ** 2))
    if planted_defect:
        dphi_dd_cs = -dphi_dd_cs
    cs_rel_err = abs(dphi_dd_cs - dphi_dd_exact) / abs(dphi_dd_exact)

    provenance_classes = {str(r["provenance_class"]) for r in PARAMETER_PROVENANCE_LEDGER}
    provenance_ok = provenance_classes == {"empirical", "derived", "phenomenological_heuristic"}

    ok = (
        provenance_ok
        and (0.0 < neg_m_lo < neg_m_0 < neg_m_hi < 0.5)
        and (0.0 < def_sig_lo < def_sig_0 < def_sig_hi < 1.0)
        and (0.0 < ph_t_lo < ph_t_0 < ph_t_hi)
        and (0.0 < ph_eps_lo < ph_t_0 < ph_eps_hi)
        and opp_suppression > 1.0e15
        and cs_rel_err < 1.0e-13
    )
    return {
        "parameter_provenance_entries": len(PARAMETER_PROVENANCE_LEDGER),
        "provenance_classes": sorted(provenance_classes),
        "bmv_negativity_envelope_m_pm25": [round(neg_m_lo, 6), round(neg_m_0, 6), round(neg_m_hi, 6)],
        "eotwash_120fold_deficit_sigma33_pm25": [round(def_sig_lo, 6), round(def_sig_0, 6), round(def_sig_hi, 6)],
        "photon_decoherence_4K_pm25_s1": [ph_t_lo, ph_t_0, ph_t_hi],
        "photon_decoherence_eps_pm20_s1": [ph_eps_lo, ph_t_0, ph_eps_hi],
        "oppenheim_eotwash_suppression_factor": opp_suppression,
        "complex_step_rel_error": cs_rel_err,
        "ok": ok,
    }


def run_all_checks(planted_defect: bool = False) -> dict[str, object]:
    dim_res = verify_si_dimensional_homogeneity(planted_defect=planted_defect)
    sens_res = verify_sensitivity_and_complex_step(planted_defect=planted_defect)
    ok = bool(dim_res["ok"]) and bool(sens_res["ok"])
    return {
        "status": "PASS" if ok else "FAIL",
        "folio": "T.06-DIM-SENS",
        "si_homogeneity": dim_res,
        "provenance_and_sensitivity": sens_res,
    }


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    res = run_all_checks(planted_defect=planted)
    stream = sys.stdout if res["status"] == "PASS" else sys.stderr
    print(json.dumps(res, indent=2), file=stream)
    return 0 if res["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
