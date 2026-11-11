# -*- coding: utf-8 -*-
"""Cross-Scale Essay ES.07 · The Parallel Horizon & The Loophole-Free Quantum Island.

Pure-Python stdlib physics kernel, multivariate rational polynomial verifier, and bilingual
(EN / es-MX) monograph data for Informatico.ai's Movement III capstone Cross-Scale Essay
(/essays/loophole-free-parallel-horizon/).

Synthesizes five coupled analytical and epistemic results:
  1. Exact reflection-parity block diagonalization of the 4x4 partial-transpose matrix for the
     2-D and 3-D skewed parallel Diósi-Penrose hybrid master equation under local environmental
     dephasing, yielding an overflow-free closed form for N_hyb(t) on all t in [0, inf) and the
     exact critical dephasing threshold gamma_crit^hyb = (G m^2 / hbar) max(0, sqrt(2) b - a).
  2. Exact asymptotic expansion of the parallel hybrid entanglement horizon from
     D_{c,0} = 1.547134 sigma (sigma_c / D = 0.646356) at small splits to the universal ceiling
     D_{c,inf} = 2.210928 sigma (sigma_c / D = 0.452299) as Delta_x / sigma -> inf. Combined with
     the 33.08 um Eöt-Wash 2020 signed Yukawa recast, any parallel experiment with D >= 73.14 um
     has N_hyb(t) = 0 identically for all splits and hold times, opening a loophole-free corridor
     above the 28.29 um centre-to-centre Casimir screen wall at 10^-14 kg (benchmark D = 75 um,
     Delta_x = 250 um, t = 2.5 s -> N_hyb = 0.0 vs N_Q = 0.4302..0.4902) that pinches shut at
     10^-12 kg where Casimir + sphere diameter reaches 73.30 um > 73.14 um.
  3. Four cryogenic vacuum ensemble regimes (isobaric P = const with analytical T* = 2.04 K / 2.50 K
     valley, sealed isochoric n = const, Knudsen thermal transpiration, and cryo-pumped vapour) plus
     the hardware-free 3-D skew-angle null control at theta = 90 deg (midpoint-centred '+' cross:
     r_same = r_diff = 191.87 um, cancelling gravitational cross-phase to all multipole orders,
     contrasted with the uncentred corner-aligned +(3/4) Delta_x^4 / D^5 residue).
  4. Explicit four-part epistemic boundary explaining why a tabletop entanglement corridor is NOT
     a Theory of Everything (low-energy IR regime vs UV graviton completion, model-conditional
     scope vs Aziz & Howl 2025 higher-order matter vertices, published-table recast vs raw 95-run
     profile likelihood refit, and DERIVED (NOT MEASURED) vs unbuilt macroscopic superpositions).
  5. Nine zero-sorry core Lean 4 Prelude theorems (ParallelHorizon.lean) certifying SI dimensional
     homogeneity, partial-transpose discriminant positivity, 3-D skewed midpoint cancellation,
     orthogonal all-multipole nullity, T^9 blackbody steepness, and the 10^-15..10^-12 kg mass pinch.
"""
from __future__ import annotations

from decimal import Decimal, InvalidOperation
from fractions import Fraction
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

TOOLS_DIR = Path(__file__).resolve().parents[2]
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import timegravity_kernel as k_base  # noqa: E402
import timegravity_kernel_dispute as k_disp  # noqa: E402
import timegravity_kernel_entangle as k_ent  # noqa: E402
import timegravity_kernel_recast as k_rec  # noqa: E402

CODE = "ES.07"
SLUG = "loophole-free-parallel-horizon"
PLATE_SLUG = "essay07"

G_NEWTON = k_base.G_NEWTON
HBAR = k_ent.HBAR
C_LIGHT = 299_792_458.0
K_BOLTZMANN = 1.380649e-23
DIAMOND_DENSITY_KG_M3 = 3500.0
DIAMOND_EPSILON_R = 5.7
HELIUM4_MASS_KG = 4.002602 * 1.66053906660e-27
PLATE_THICKNESS_M = 1.0e-6
CASIMIR_ETA = 0.10  # max Casimir-to-Newtonian force fraction (Van De Kamp et al. 2020 Eq. 14)

# Cited Van De Kamp et al. (2020) Eq. 20 gas prefactor vs pure hard-sphere kinetic flux:
# At m = 10^-14 kg (R = 0.8803 um), P = 2.7e-16 Pa, T = 1.0 K, kinetic geometric flux pi R^2 P / sqrt(...)
# gives 3.46e-3 s^-1 while the cited macroscopic scattering formula (16 pi / 3) n v_th R^2 (with thermal
# wavelength & polarizability enhancement in Van De Kamp / Romero-Isart conventions) is ~8.38x higher.
VDK_CITED_GAS_FACTOR = 16.0 / (3.0 * math.sqrt(2.0 * math.pi / 8.0))  # 32 / (3 * sqrt(pi)) * sqrt(...) -> exact ratio below

_SUB_SUP_DIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻₀₁₂₃₄₅₆₇₈₉", "0123456789-0123456789")
_NUM_RE = re.compile(r"(?<![A-Za-z])[-−]?\d+(?:,\d{3})*(?:\.\d+)?(?:[eE][-−+]?\d+)?")


def extract_number_tokens(text: str) -> list[str]:
    """Extract normalized numeric tokens from prose or table cells for bilingual parity checks."""
    norm = text.translate(_SUB_SUP_DIGITS).replace("−", "-")
    tokens: list[str] = []
    for match in _NUM_RE.finditer(norm):
        raw = match.group(0).replace(",", "")
        try:
            tokens.append(format(Decimal(raw).normalize(), "f"))
        except InvalidOperation:
            tokens.append(raw)
    return sorted(tokens)


def diamond_radius_m(mass_kg: float) -> float:
    return (3.0 * mass_kg / (4.0 * math.pi * DIAMOND_DENSITY_KG_M3)) ** (1.0 / 3.0)


def casimir_screen_min_cc_m(mass_kg: float, plate_m: float = PLATE_THICKNESS_M) -> dict[str, float]:
    """Van De Kamp et al. (2020) Eq. 14 minimum sphere-to-screen surface separation d_min, plus finite
    sphere radius R on each side of the conducting screen of thickness W:
      D_min,surf = 2 * d_min + W,    D_min,cc = 2 * (d_min + R) + W.
    """
    from timegravity_kernel_ladder import casimir_floor_separation
    r_m = diamond_radius_m(mass_kg)
    d_surf = casimir_floor_separation(mass_kg)
    d_cc = d_surf + 2.0 * r_m
    return {
        "mass_kg": mass_kg,
        "radius_m": r_m,
        "surface_floor_m": d_surf,
        "center_to_center_floor_m": d_cc,
    }


def gas_decoherence_rates_per_s(mass_kg: float, pressure_pa: float, temp_k: float) -> dict[str, float]:
    """Short-wavelength (Delta_x >> lambda_th) helium gas collisional localization rate:
      - kinetic_flux: geometric hard-sphere impingement rate n <v> pi R^2 = P * sqrt(8 pi R^4 / (m_gas k_B T)) / ...
        Specifically n = P / (k_B T), <v> = sqrt(8 k_B T / (pi m_gas)) => Gamma_kin = P * R^2 * sqrt(8 pi / (m_gas k_B T)).
      - vdk_cited: Van De Kamp et al. (2020) Eq. 20 / Schut et al. (2024) conservative prefactor (16 pi / sqrt(3)) * P * R^2 / sqrt(2 pi m_gas k_B T)
        matching T.05's cited gas decoherence convention (~8.38x kinetic flux).
    """
    r_m = diamond_radius_m(mass_kg)
    gamma_kin = pressure_pa * (r_m * r_m) * math.sqrt(8.0 * math.pi / (HELIUM4_MASS_KG * K_BOLTZMANN * temp_k))
    # Van De Kamp Eq. 20: Gamma_gas = (16 pi / sqrt(3)) * P R^2 / sqrt(2 pi m_gas k_B T) * ... -> T.05 kernel ratio:
    # Use exact analytical ratio (32 * sqrt(pi / 3) / sqrt(8 pi)) -> let's cross-check directly with Van De Kamp Eq. 20:
    # Eq. 20: Gamma_air = (16 pi * sqrt(2 pi / 3)) * P * R^2 / sqrt(m_air k_B T) -> ratio to sqrt(8 pi) is 16 pi / sqrt(12) = 8 pi / sqrt(3) = 14.51,
    # whereas Joos-Zeh / Hornberger short-wavelength s-wave + diffraction shadow (2 pi R^2 vs pi R^2 * ...) gives 8.3835x:
    # Specifically (16 * math.sqrt(math.pi / 3.0)) / math.sqrt(8.0 * math.pi) ... wait:
    # Let's use the exact Romero-Isart (2011) / Van De Kamp (2020) short-wavelength dipolar-diffraction factor 8 * sqrt(2 * pi) / 3 * P R^2 / sqrt(m_gas k_B T) * pi = (8 pi sqrt(2 pi) / 3) = 20.9439 / 2.5066 = 8.3554x!
    import timegravity_kernel_decoherence as k_deco
    r_m = diamond_radius_m(mass_kg)
    return {
        "kinetic_per_s": k_deco.gas_rate(250.0e-6, pressure_pa, temp_k, r_m, form="kinetic"),
        "cited_per_s": k_deco.gas_rate(250.0e-6, pressure_pa, temp_k, r_m, form="cited"),
    }


def blackbody_photon_rate_per_s(mass_kg: float, split_m: float, temp_k: float) -> float:
    """Thermal blackbody photon Rayleigh scattering + emission/absorption localization rate (Romero-Isart 2011;
    Van De Kamp et al. 2020 Eqs. 21-23) for an isotropic dielectric sphere (epsilon_r = 5.7, Im chi ~ 0 at 1-4 K):
      Gamma_BB,sc = (8! * 8 * zeta(9) / 9 pi) * c * R^6 * ((epsilon_r - 1)/(epsilon_r + 2))^2 * (k_B T / (hbar c))^9 * Delta_x^2.
    """
    import timegravity_kernel_decoherence as k_deco
    r_m = diamond_radius_m(mass_kg)
    return k_deco.photon_rate(split_m, r_m, temp_k, temp_k)["total"]


def quantum_parallel_negativity(
    split_m: float, gap_m: float, mass_kg: float, t_s: float, gamma_per_s: float = 0.0, theta_rad: float = 0.0
) -> dict[str, float]:
    """Exact Peres negativity of the unitary Newtonian parallel / 3-D skewed channel under local dephasing gamma."""
    ct = math.cos(theta_rad)
    r_same = math.sqrt(gap_m * gap_m + 0.5 * split_m * split_m * (1.0 - ct))
    r_diff = math.sqrt(gap_m * gap_m + 0.5 * split_m * split_m * (1.0 + ct))
    omega_ent = (G_NEWTON * mass_kg * mass_kg / HBAR) * abs(1.0 / r_same - 1.0 / r_diff) * 2.0
    dphi = omega_ent * t_s
    t_full = (math.pi / omega_ent) if omega_ent > 0.0 else float("inf")
    # Under local dephasing eta = exp(-gamma t) on both qubits (same dephase_points convention as T.05):
    br = k_disp.branches_parallel_skewed(split_m, gap_m, theta_rad)
    n_val = k_ent.negativity(k_disp.dephase_points(k_disp.quantum_state_points(br, mass_kg, t_s), gamma_per_s, t_s))
    return {
        "r_same_m": r_same,
        "r_diff_m": r_diff,
        "omega_ent_rad_s": omega_ent,
        "entanglement_phase_rad": dphi,
        "t_full_s": t_full,
        "negativity": n_val,
    }


def evaluate_parallel_horizon_curve(planted_defect: bool = False) -> dict:
    """Cross-verify closed-form 2-D and 3-D skewed parallel hybrid negativity against 4x4 diagonalization
    and map the monotone parallel horizon expansion D_c(Delta_x / sigma) / sigma from 1.547134 to 2.210928."""
    max_matrix_diff = 0.0
    for theta in (0.0, math.pi / 6.0, math.pi / 4.0, math.pi / 2.0, math.pi):
        br = k_disp.branches_parallel_skewed(40e-6, 45e-6, theta)
        for gamma in (0.0, 2.0e-4):
            for t_s in (2.5, 600.0):
                n_mat = k_ent.negativity(
                    k_disp.dephase_points(k_disp.hybrid_state_points(br, 1.0e-14, 50e-6, t_s), gamma, t_s)
                )
                n_closed = k_disp.parallel_hybrid_negativity_closed(
                    40e-6, 45e-6, 1.0e-14, 50e-6, t_s, gamma_env=gamma, theta_rad=theta, planted_defect=planted_defect
                )
                max_matrix_diff = max(max_matrix_diff, abs(n_mat - n_closed))

    # Overflow-free check across extreme hold times up to 10^8 s
    t1e8_val = k_disp.parallel_hybrid_negativity_closed(
        250e-6, 75e-6, 1.0e-14, 33.1e-6, 1.0e8, planted_defect=planted_defect
    )

    curve_rows = []
    for ratio in (0.01, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 20.0):
        dc_over_s = (
            k_disp.PARALLEL_DC0_OVER_SIGMA
            if planted_defect
            else k_disp.parallel_hybrid_critical_gap_over_sigma(ratio, 0.0)
        )
        col_dc = k_disp.tn_critical_separation_from_e_minus(1.0, ratio)
        curve_rows.append(
            {
                "split_over_sigma": ratio,
                "parallel_dc_over_sigma": dc_over_s,
                "parallel_sigma_c_over_gap": (1.0 / dc_over_s) if dc_over_s > 0.0 else float("inf"),
                "collinear_dc_over_sigma": col_dc if col_dc is not None else 0.0,
            }
        )

    return {
        "dc0_over_sigma": k_disp.PARALLEL_DC0_OVER_SIGMA,
        "dc_inf_over_sigma": k_disp.PARALLEL_DC_INF_OVER_SIGMA,
        "sigma_c_over_gap_small_split": 1.0 / k_disp.PARALLEL_DC0_OVER_SIGMA,
        "sigma_c_over_gap_large_split": 1.0 / k_disp.PARALLEL_DC_INF_OVER_SIGMA,
        "max_4x4_vs_closed_diff": max_matrix_diff,
        "negativity_75um_at_1e8s": t1e8_val,
        "horizon_curve": curve_rows,
    }


def evaluate_loophole_free_island(planted_defect: bool = False) -> dict:
    """Compute the Eöt-Wash 33.08 um parallel horizon bounds, the Casimir + 2R mass-pinch table,
    the falsified D = 60 um naive small-split point, and the loophole-free D = 75 um benchmark."""
    recast = k_rec.Recast(120, "log52-3000", n_sep=12, lam_min=10e-6, lam_max=100e-6)
    sigma_95_m = recast.sigma_95()
    dc0_m = k_disp.PARALLEL_DC0_OVER_SIGMA * sigma_95_m
    dc_inf_m = (k_disp.PARALLEL_DC0_OVER_SIGMA if planted_defect else k_disp.PARALLEL_DC_INF_OVER_SIGMA) * sigma_95_m

    mass_corridor = []
    for m_kg in (1.0e-15, 1.0e-14, 1.0e-13, 1.0e-12):
        cas = casimir_screen_min_cc_m(m_kg)
        cc_m = cas["center_to_center_floor_m"]
        mass_corridor.append(
            {
                "mass_kg": m_kg,
                "radius_um": cas["radius_m"] * 1.0e6,
                "casimir_surface_um": cas["surface_floor_m"] * 1.0e6,
                "casimir_cc_um": cc_m * 1.0e6,
                "parallel_ceiling_um": dc_inf_m * 1.0e6,
                "corridor_open_above_ceiling": cc_m < dc_inf_m,
            }
        )

    # Naive small-split trap: D = 60 um, Delta_x = 250 um sits above 51.18 um, yet sigma_c = 31.65 um < 33.08 um!
    sigma_c_60_m = k_disp.parallel_hybrid_critical_sigma_exact(250e-6, 60e-6, 0.0)
    peak_60_at_33 = max(
        k_disp.parallel_hybrid_negativity_closed(250e-6, 60e-6, 1.0e-14, 33.0e-6, 10.0 ** (-2.0 + k / 20.0))
        for k in range(0, 60)
    )

    # Loophole-free benchmark: D = 75 um, Delta_x = 250 um, m = 10^-14 kg, t = 2.5 s, T = 1.0 K, P = 2.7e-16 Pa
    d_bench = 75.0e-6
    dx_bench = 250.0e-6
    m_bench = 1.0e-14
    t_bench = 2.5
    p_base = 2.7e-16
    temp_bench = 1.0

    sigma_c_75_m = k_disp.parallel_hybrid_critical_sigma_exact(dx_bench, d_bench, 0.0)
    sigma_c_75_inf_m = d_bench / k_disp.PARALLEL_DC_INF_OVER_SIGMA
    hyb_max_75 = max(
        k_disp.parallel_hybrid_negativity_closed(
            dx_bench, d_bench, m_bench, sigma_95_m, 10.0 ** (k / 4.0), planted_defect=planted_defect
        )
        for k in range(-8, 36)
    )

    gas = gas_decoherence_rates_per_s(m_bench, p_base, temp_bench)
    phot = blackbody_photon_rate_per_s(m_bench, dx_bench, temp_bench)
    q_unit = quantum_parallel_negativity(dx_bench, d_bench, m_bench, t_bench, 0.0)
    q_kin = quantum_parallel_negativity(dx_bench, d_bench, m_bench, t_bench, gas["kinetic_per_s"] + phot)
    q_cit = quantum_parallel_negativity(dx_bench, d_bench, m_bench, t_bench, gas["cited_per_s"] + phot)

    return {
        "sigma_95_um": sigma_95_m * 1.0e6,
        "parallel_dc0_um": dc0_m * 1.0e6,
        "parallel_dc_inf_um": dc_inf_m * 1.0e6,
        "mass_corridor": mass_corridor,
        "naive_60um_trap": {
            "sigma_c_um": sigma_c_60_m * 1.0e6,
            "hybrid_peak_at_33um": peak_60_at_33,
        },
        "benchmark_75um": {
            "gap_um": 75.0,
            "split_um": 250.0,
            "mass_kg": m_bench,
            "radius_um": diamond_radius_m(m_bench) * 1.0e6,
            "sigma_c_um": sigma_c_75_m * 1.0e6,
            "sigma_c_inf_split_um": sigma_c_75_inf_m * 1.0e6,
            "hybrid_max_negativity_all_t": hyb_max_75,
            "entanglement_phase_rad": q_unit["entanglement_phase_rad"],
            "t_full_s": q_unit["t_full_s"],
            "gamma_gas_kinetic_per_s": gas["kinetic_per_s"],
            "gamma_gas_cited_per_s": gas["cited_per_s"],
            "gamma_photon_1k_per_s": phot,
            "quantum_negativity_unitary": q_unit["negativity"],
            "quantum_negativity_kinetic": q_kin["negativity"],
            "quantum_negativity_cited": q_cit["negativity"],
        },
    }


def isobaric_optimal_temp_k(mass_kg: float, split_m: float, pressure_pa: float, mode: str = "cited") -> dict[str, float]:
    """Cryogenic valley minimizer T* of gamma_tot(T) = gamma_gas(T) + gamma_phot(T) under isobaric P = const:
    At Im(eps) = 10^-4 (Rijavec et al. 2021), thermal emission + absorption B_em T^6 dominates T^9 Rayleigh
    scattering across 1-3 K, giving analytical balance d/dT [A_gas T^(-1/2) + B_em T^6] = 0 ==> T* = (A_gas / 12 B_em)^(2/13)
    (2.044 K at 2.7e-16 Pa; exact Romero-Isart saturating minimum 2.042 K).
    """
    rates_1k = gas_decoherence_rates_per_s(mass_kg, pressure_pa, 1.0)
    a_gas = rates_1k["cited_per_s"] if mode == "cited" else rates_1k["kinetic_per_s"]
    b_phot = blackbody_photon_rate_per_s(mass_kg, split_m, 1.0)
    lo, hi = 0.5, 6.0
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    def tot(tk: float) -> float:
        rg = gas_decoherence_rates_per_s(mass_kg, pressure_pa, tk)
        gv = rg["cited_per_s"] if mode == "cited" else rg["kinetic_per_s"]
        return gv + blackbody_photon_rate_per_s(mass_kg, split_m, tk)
    for _ in range(50):
        m1 = hi - gr * (hi - lo)
        m2 = lo + gr * (hi - lo)
        if tot(m1) < tot(m2):
            hi = m2
        else:
            lo = m1
    t_star = 0.5 * (lo + hi)
    g_min = tot(t_star)
    return {"t_star_k": t_star, "gamma_min_per_s": g_min, "a_gas_1k": a_gas, "b_phot_1k": b_phot}


def evaluate_cryogenic_ensembles_and_skew_null(planted_defect: bool = False) -> dict:
    """Compare the four cryogenic vacuum ensembles and verify the 3-D skew-angle rotation signature
    theta in [0, 90 deg], contrasting midpoint-centred '+' nullity with uncentred corner-aligned L-branches."""
    m_bench = 1.0e-14
    dx_bench = 250.0e-6
    d_bench = 75.0e-6

    opt_2p7e16 = isobaric_optimal_temp_k(m_bench, dx_bench, 2.7e-16, mode="cited")
    opt_1e15 = isobaric_optimal_temp_k(m_bench, dx_bench, 1.0e-15, mode="cited")

    # Sealed isochoric (n = const anchored at 1 K): gamma_isochoric(T) = A_1K * sqrt(T) + B_1K * T^9 (strictly increasing)
    a1 = opt_2p7e16["a_gas_1k"]
    b1 = opt_2p7e16["b_phot_1k"]
    isochoric_1k = a1 * math.sqrt(1.0) + b1 * (1.0 ** 9)
    isochoric_2k = a1 * math.sqrt(2.0) + b1 * (2.0 ** 9)

    # 3-D skew rotation curve
    skew_rows = []
    for deg in (0.0, 30.0, 45.0, 60.0, 90.0):
        th = math.radians(deg)
        q_row = quantum_parallel_negativity(dx_bench, d_bench, m_bench, 2.5, opt_2p7e16["gamma_min_per_s"], theta_rad=th)
        hyb_60 = k_disp.parallel_hybrid_negativity_closed(dx_bench, d_bench, m_bench, 60.0e-6, 600.0, theta_rad=th)
        skew_rows.append(
            {
                "angle_deg": deg,
                "r_same_um": q_row["r_same_m"] * 1.0e6,
                "r_diff_um": q_row["r_diff_m"] * 1.0e6,
                "entanglement_phase_rad": q_row["entanglement_phase_rad"],
                "quantum_negativity_cited": q_row["negativity"],
                "hybrid_negativity_sigma60um": hyb_60,
            }
        )

    # Uncentred corner-aligned orthogonal L-branches: A in {(0,0,0), (0,dx,0)}, B in {(D,0,0), (D,0,dx)}
    r_ll = d_bench
    r_lr = math.hypot(d_bench, dx_bench)
    r_rl = r_lr
    r_rr = math.sqrt(d_bench * d_bench + 2.0 * dx_bench * dx_bench)
    dphi_corner = (G_NEWTON * m_bench * m_bench * 2.5 / HBAR) * abs(1.0 / r_lr + 1.0 / r_rl - 1.0 / r_ll - 1.0 / r_rr)
    # If planted_defect is set, pretend uncentred corner branches give the exact null test:
    orth_phase_reported = dphi_corner if planted_defect else skew_rows[-1]["entanglement_phase_rad"]

    return {
        "isobaric_2p7e16_pa": opt_2p7e16,
        "isobaric_1e15_pa": opt_1e15,
        "isochoric_monotone_increase": isochoric_2k > isochoric_1k,
        "skew_rotation_rows": skew_rows,
        "orthogonal_midpoint_phase_rad": orth_phase_reported,
        "uncentred_corner_phase_rad": dphi_corner,
    }


def verify_lean_parallel_horizon(lean_path: Path | None = None, planted_defect: bool = False) -> dict:
    """Audit ParallelHorizon.lean: comment-stripped forbidden-token scan, strict core-Prelude qualified-ID
    allowlist, optional live `lean` kernel execution, and exact multivariate Fraction polynomial checks."""
    target = (
        lean_path
        if lean_path is not None
        else TOOLS_DIR.parent / "skills" / "essays" / "loophole-free-parallel-horizon" / "ParallelHorizon.lean"
    )
    lean_raw = target.read_text(encoding="utf-8")
    if planted_defect:
        lean_raw = lean_raw + "\ntheorem planted_unproven_parallel_claim : 1 = 2 := by sorry\n"

    no_block = re.sub(r"/--?.*?-/", "", lean_raw, flags=re.S)
    no_comments = re.sub(r"--.*?$", "", no_block, flags=re.M)

    forbidden_tokens = re.findall(r"\b(?:sorry|sorryAx|admit|axiom)\b", no_comments)
    theorem_names = re.findall(r"\btheorem\s+([A-Za-z0-9_]+)", no_comments)
    universal_count = len(re.findall(r"∀|\bforall\b", no_comments))

    allowed_qualified_ids = {
        "Informatico.Essays.ES07",
        "Int.mul_add",
        "Int.neg_mul_neg",
        "Int.ofNat",
        "Nat.add_mul",
        "Nat.mul_add",
        "r.casimir_cc_nm",
        "r.sigma_c_75_nm",
        "a.m", "b.m", "a.l", "b.l", "a.t", "b.t", "a.i", "b.i",
        "a.theta", "b.theta", "a.n", "b.n", "a.j", "b.j",
    }
    qualified_ids = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+\b", no_comments))
    unknown_qualified_ids = sorted(qualified_ids - allowed_qualified_ids)

    lean_bin = shutil.which("lean")
    if not lean_bin:
        elan_candidate = Path.home() / ".elan" / "bin" / ("lean.exe" if os.name == "nt" else "lean")
        if elan_candidate.is_file():
            lean_bin = str(elan_candidate)
    lean_compiler_checked = False
    lean_compiler_ok = True
    lean_compiler_stderr = ""
    if lean_bin:
        lean_compiler_checked = True
        if planted_defect:
            with tempfile.NamedTemporaryFile("w", suffix=".lean", encoding="utf-8", delete=False) as tf:
                tf.write(lean_raw)
                tmp_path = Path(tf.name)
            try:
                proc = subprocess.run([lean_bin, str(tmp_path)], capture_output=True, text=True, timeout=60, check=False)
            finally:
                tmp_path.unlink(missing_ok=True)
        else:
            proc = subprocess.run([lean_bin, str(target)], capture_output=True, text=True, timeout=60, check=False)
        lean_compiler_ok = proc.returncode == 0 and "warning: declaration uses 'sorry'" not in (proc.stdout + proc.stderr)
        lean_compiler_stderr = (proc.stdout + proc.stderr).strip()[:400]

    # Exact multivariate polynomial ring over Fraction
    def p_var(name: str) -> dict:
        return {((name, 1),): Fraction(1, 1)}

    def p_const(val: int) -> dict:
        return {(): Fraction(val, 1)} if val != 0 else {}

    def p_add(p: dict, q: dict, sign: int = 1) -> dict:
        out = dict(p)
        for mon, coeff in q.items():
            out[mon] = out.get(mon, Fraction(0, 1)) + sign * coeff
            if out[mon] == 0:
                del out[mon]
        return out

    def p_mul(p: dict, q: dict) -> dict:
        out: dict = {}
        for m1, c1 in p.items():
            for m2, c2 in q.items():
                merged: dict[str, int] = {}
                for v, e in m1:
                    merged[v] = merged.get(v, 0) + e
                for v, e in m2:
                    merged[v] = merged.get(v, 0) + e
                mon = tuple(sorted((v, e) for v, e in merged.items() if e != 0))
                out[mon] = out.get(mon, Fraction(0, 1)) + c1 * c2
                if out[mon] == 0:
                    del out[mon]
        return out

    # 1. 4-variable skewed parallel midpoint difference polynomial in Q[dSq, hSq, scale, cosScaled]
    dSq, hSq, sc, cSc = p_var("dSq"), p_var("hSq"), p_var("scale"), p_var("cosScaled")
    r_same_p = p_add(p_mul(p_const(2), p_mul(sc, dSq)), p_mul(p_const(2), p_mul(hSq, p_add(sc, cSc, -1))))
    r_diff_p = p_add(p_mul(p_const(2), p_mul(sc, dSq)), p_mul(p_const(2), p_mul(hSq, p_add(sc, cSc, 1))))
    skew_diff_poly = p_add(p_add(r_diff_p, r_same_p, -1), p_mul(p_const(4), p_mul(hSq, cSc)), -1)

    # 2. 3-variable orthogonal cross identity at cosScaled = 0
    r_same_0 = p_add(p_mul(p_const(2), p_mul(sc, dSq)), p_mul(p_const(2), p_mul(hSq, sc)))
    r_diff_0 = p_add(p_mul(p_const(2), p_mul(sc, dSq)), p_mul(p_const(2), p_mul(hSq, sc)))
    orth_null_poly = p_add(r_diff_0, r_same_0, -1)

    # 3. 3-variable uncentred corner fourth-order Taylor numerator in Q[d4, d2dx2, dx4]
    d4, d2dx2, dx4 = p_var("d4"), p_var("d2dx2"), p_var("dx4")
    ll_p = p_mul(p_const(8), d4)
    rr_p = p_add(p_add(p_mul(p_const(8), d4), p_mul(p_const(8), d2dx2), -1), p_mul(p_const(12), dx4))
    lr_p = p_add(p_add(p_mul(p_const(8), d4), p_mul(p_const(4), d2dx2), -1), p_mul(p_const(3), dx4))
    corner_num = p_add(p_add(ll_p, rr_p), p_mul(p_const(2), lr_p), -1)
    corner_poly_diff = p_add(corner_num, p_mul(p_const(6), dx4), -1)

    return {
        "lean_file": target.name,
        "forbidden_tokens": forbidden_tokens,
        "unknown_qualified_ids": unknown_qualified_ids,
        "lean_compiler_checked": lean_compiler_checked,
        "lean_compiler_ok": lean_compiler_ok,
        "lean_compiler_stderr": lean_compiler_stderr,
        "theorem_names": theorem_names,
        "theorem_count": len(theorem_names),
        "universal_quantifier_count": universal_count,
        "skew_midpoint_poly_zero": len(skew_diff_poly) == 0,
        "orthogonal_null_poly_zero": len(orth_null_poly) == 0,
        "corner_taylor4_poly_zero": len(corner_poly_diff) == 0,
    }


def evaluate_parallel_synthesis(planted_defect: bool = False) -> dict:
    """Run all coupled verification layers of Essay ES.07."""
    return {
        "parallel_curve": evaluate_parallel_horizon_curve(planted_defect=planted_defect),
        "loophole_free_island": evaluate_loophole_free_island(planted_defect=planted_defect),
        "cryogenic_and_skew": evaluate_cryogenic_ensembles_and_skew_null(planted_defect=planted_defect),
        "lean4_parallel_spine": verify_lean_parallel_horizon(planted_defect=planted_defect),
    }


# ---------------------------------------------------------------------------
# Bilingual Monograph Specification (EN / es-MX) · Essay ES.07
# ---------------------------------------------------------------------------

ESSAY: dict = {
    "code": CODE,
    "slug": SLUG,
    "plate_slug": PLATE_SLUG,
    "date": "2026-11-10",
    "seo": (
        "Parallel Gravity Horizons and the Quantum Island",
        "Exact closed-form parallel smeared-gravity horizons, torsion-balance limits, cryogenic valleys, and orthogonal null controls for tabletop entanglement.",
        "Horizontes Paralelos y la Isla Cuántica de Mesa",
        "Horizontes exactos en gravedad difuminada paralela, límites de torsión, valles criogénicos y controles nulos ortogonales en entrelazamiento de mesa.",
    ),
    "kicker_en": "Cross-Scale Essay · ES.07 · Parallel Smeared-Gravity Horizons, Cryogenic Valleys & Epistemic Boundaries",
    "kicker_es": "Ensayo Transescalar · ES.07 · Horizontes Paralelos de Gravedad Difuminada, Valles Criogénicos y Fronteras Epistémicas",
    "reading_time_en": "16 min read",
    "reading_time_es": "16 min de lectura",
    "title_en": "The Parallel Horizon & The Loophole-Free Quantum Island: Exact Bounds, Cryogenic Valleys, and Why This Is Not a Theory of Everything",
    "title_es": "El Horizonte Paralelo y la Isla Cuántica sin Resquicios: Cotas Exactas, Valles Criogénicos y por Qué Esto No Es una Teoría del Todo",
    "standfirst_en": (
        "When two spatial superpositions sit side by side rather than in line, how far can Diósi–Penrose smeared "
        "classical gravity reach before its own self-decoherence extinguishes entanglement identically? Block-diagonalizing "
        "the 4 × 4 partial-transpose matrix in closed form reveals that the parallel hybrid horizon expands from "
        "1.5471 σ at small splits to a universal ceiling of 2.2109 σ as Δx / σ → ∞. Combined with the 33.08 µm "
        "Eöt-Wash torsion recast, every parallel gap above 73.14 µm is classically dark at all splits and times—opening "
        "a clean quantum island around D = 75 µm with a hardware-free 90° null test, while leaving four sharp "
        "epistemic boundaries between tabletop entanglement and a Theory of Everything."
    ),
    "standfirst_es": (
        "Cuando dos superposiciones espaciales se colocan en paralelo en vez de en línea, ¿hasta dónde alcanza la "
        "gravedad clásica difuminada de Diósi–Penrose antes de que su propia autodecoherencia anule el entrelazamiento? "
        "Diagonalizar por bloques la transpuesta parcial de 4 × 4 en forma cerrada revela que el horizonte híbrido "
        "paralelo crece de 1.5471 σ a divisiones pequeñas hasta un techo universal de 2.2109 σ cuando Δx / σ → ∞. Junto "
        "al recast de torsión de Eöt-Wash de 33.08 µm, toda separación paralela sobre 73.14 µm queda clásicamente a "
        "oscuras, abriendo una isla cuántica en D = 75 µm con control nulo a 90° y cuatro fronteras epistémicas."
    ),
    "card_dek_en": (
        "Closed-form parallel Diósi–Penrose block diagonalization (1.5471 σ to 2.2109 σ), the 73.14 µm universal "
        "ceiling, the D = 75 µm quantum island, 2.04 K cryogenic valleys, 90° null controls, and 9 Lean 4 theorems."
    ),
    "card_dek_es": (
        "Diagonalización cerrada de Diósi–Penrose paralelo (1.5471 σ a 2.2109 σ), el techo universal de 73.14 µm, "
        "la isla cuántica en D = 75 µm, valles criogénicos a 2.04 K, control nulo a 90° y 9 teoremas en Lean 4."
    ),
    "instrument_kind": "parallel_horizon",
    "predict": {
        "question_en": (
            "Under the 33.08 µm Eöt-Wash recast, the parallel Diósi–Penrose hybrid horizon sits at 51.18 µm for small "
            "splits (1.5471 σ). If an experimenter increases the superposition split to Δx = 250 µm at gap D = 60 µm—"
            "or steps out to D = 75 µm and rotates one interferometer arm by θ = 90° about its midpoint—what happens?"
        ),
        "question_es": (
            "Bajo el recast de Eöt-Wash de 33.08 µm, el horizonte híbrido paralelo de Diósi–Penrose vale 51.18 µm para "
            "divisiones pequeñas (1.5471 σ). Si aumentas la división a Δx = 250 µm en D = 60 µm —o pasas a D = 75 µm "
            "y giras un brazo θ = 90° respecto a su punto medio—, ¿qué ocurre?"
        ),
        "choices": [
            {
                "id": "a",
                "en": "The 51.18 µm parallel horizon holds for all splits, so D = 60 µm already eliminates hybrid entanglement, while a 90° rotation keeps half the Newtonian phase.",
                "es": "El horizonte paralelo de 51.18 µm vale para toda división, de modo que D = 60 µm ya elimina el entrelazamiento híbrido y girar 90° conserva la mitad de la fase newtoniana.",
            },
            {
                "id": "b",
                "en": "Large splits widen the parallel horizon up to 2.2109 σ = 73.14 µm, so D = 60 µm still leaks hybrid entanglement (σ_c = 31.65 µm), whereas D = 75 µm (σ_c = 41.12 µm) forces N_hyb = 0 at all times and midpoint θ = 90° nulls all multipoles to 0.",
                "es": "Las divisiones grandes amplían el horizonte paralelo hasta 2.2109 σ = 73.14 µm, por lo que D = 60 µm aún filtra entrelazamiento híbrido (σ_c = 31.65 µm), mientras D = 75 µm (σ_c = 41.12 µm) fuerza N_hyb = 0 siempre y θ = 90° anula todos los multipolos a 0.",
            },
        ],
        "answer": "b",
        "explain_en": (
            "In parallel geometry, increasing Δx suppresses intra-particle cross-coherence f(Δx) faster than inter-particle "
            "phase asymmetry, expanding D_c / σ from 1.5471 to 2.2109 (73.14 µm at σ_95 = 33.08 µm). Thus D = 60 µm at "
            "Δx = 250 µm requires only σ_c = 31.65 µm and still entangles classically; stepping to D = 75 µm pushes σ_c to "
            "41.12 µm > 33.08 µm so N_hyb(t) = 0 for all t ≥ 0, and rotating by θ = 90° about the midpoint sets "
            "r_same = r_diff = 192.03 µm, cancelling gravitational cross-phase to every multipole order."
        ),
        "explain_es": (
            "En geometría paralela, aumentar Δx reduce f(Δx) y amplía D_c / σ de 1.5471 a 2.2109 (73.14 µm para "
            "σ_95 = 33.08 µm). Por ello D = 60 µm con Δx = 250 µm solo exige σ_c = 31.65 µm y aún entrelaza clásicamente; "
            "pasar a D = 75 µm eleva σ_c a 41.12 µm > 33.08 µm fijando N_hyb(t) = 0 para todo t ≥ 0, y girar θ = 90° "
            "sobre el punto medio iguala r_same = r_diff = 192.03 µm, anulando la fase gravitatoria en todo orden multipolar."
        ),
    },
    "sections": [
        {
            "id": "closed-form-parallel",
            "h2_en": "I · Exact Closed-Form Block Diagonalization of the Parallel Smeared-Gravity Master Equation",
            "h2_es": "I · Diagonalización Exacta por Bloques de la Ecuación Maestra Paralela de Gravedad Difuminada",
            "short_en": "I · Closed-Form Master Equation",
            "short_es": "I · Forma Cerrada",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "In Step T.05 of the Time & Gravity series and Essay ES.06, the parallel Diósi–Penrose hybrid "
                        "channel of Trillo and Navascués (2025) was evaluated numerically on a logarithmic time grid across "
                        "4 × 4 density matrices for splits up to Δx / D = 2. Numerical grids answer what happens at one "
                        "chosen geometry, yet they hide the analytical boundary where hybrid classical entanglement dies "
                        "identically. Because two side-by-side interferometers centred on their midpoints possess exact "
                        "simultaneous reflection symmetry (sa, sb) ↦ (−sa, −sb), the entire 4 × 4 partial-transpose matrix "
                        "ρ^{T_B}(t) decomposes analytically into two decoupled 2 × 2 blocks—not only for parallel arms "
                        "(θ = 0°), but for any 3-D relative skew angle θ ∈ [0°, 180°]."
                    ),
                    "es": (
                        "En el Paso T.05 de Tiempo y Gravedad y en el Ensayo ES.06, el canal híbrido paralelo de "
                        "Diósi–Penrose formulado por Trillo y Navascués (2025) se evaluó numéricamente sobre una malla "
                        "logarítmica de tiempo en matrices de 4 × 4 hasta Δx / D = 2. Las mallas numéricas resuelven puntos "
                        "aislados, pero ocultan la frontera analítica donde el entrelazamiento clásico híbrido se extingue. "
                        "Como dos interferómetros centrados en su punto medio poseen simetría exacta de reflexión "
                        "(sa, sb) ↦ (−sa, −sb), toda la matriz transpuesta parcial ρ^{T_B}(t) de 4 × 4 se descompone "
                        "analíticamente en dos bloques de 2 × 2—no solo con brazos paralelos (θ = 0°), sino para cualquier ángulo 3-D θ ∈ [0°, 180°]."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Place mass A at (0, ∓Δx / 2, 0) and mass B at (D, ∓(Δx / 2) cos θ, ∓(Δx / 2) sin θ), each of mass m "
                        "with Gaussian mass-density smearing σ and local single-body environmental dephasing rate γ_env "
                        "(Lindblad, 1976; Diósi, 1987). Only two inter-particle distances exist across all four branches: "
                        "r_same(θ) = √(D² + 0.5 Δx²(1 − cos θ)) and r_diff(θ) = √(D² + 0.5 Δx²(1 + cos θ)). With the "
                        "smeared pair kernel f(r; σ) = erf(r / 2σ) / r and f(0; σ) = 1 / (σ √π), define the self-decoherence "
                        "rate parameter a = f(0; σ) − f(Δx; σ), the noise-dressed rate ã = a + ħ γ_env / (G m²), and the "
                        "cross-coupling rate b(θ) = |f(r_same(θ); σ) − f(r_diff(θ); σ)|. Writing f(r; σ) as the Gaussian "
                        "integral (1 / σ √π) ∫₀¹ exp(−(r / 2σ)² u²) du proves the non-strict ordering 0 ≤ b(θ) ≤ a ≤ ã "
                        "for every geometry: the exponential decay factor p − q = 4(ã − b)τ with τ = G m² t / (2ħ) is "
                        "non-negative at all times t ≥ 0, eliminating floating-point hyperbolic overflow even at t = 10⁸ s."
                    ),
                    "es": (
                        "Situemos la masa A en (0, ∓Δx / 2, 0) y la masa B en (D, ∓(Δx / 2) cos θ, ∓(Δx / 2) sin θ), ambas "
                        "de masa m con suavizado gaussiano σ y tasa local de desfase ambiental γ_env (Lindblad, 1976; "
                        "Diósi, 1987). Solo aparecen dos distancias entre partículas en las cuatro ramas: "
                        "r_same(θ) = √(D² + 0.5 Δx²(1 − cos θ)) y r_diff(θ) = √(D² + 0.5 Δx²(1 + cos θ)). Con el núcleo "
                        "f(r; σ) = erf(r / 2σ) / r y f(0; σ) = 1 / (σ √π), definimos la autodecoherencia a = f(0; σ) − f(Δx; σ), "
                        "la tasa vestida ã = a + ħ γ_env / (G m²) y el acoplamiento b(θ) = |f(r_same(θ); σ) − f(r_diff(θ); σ)|. "
                        "Escribir f(r; σ) como (1 / σ √π) ∫₀¹ exp(−(r / 2σ)² u²) du demuestra 0 ≤ b(θ) ≤ a ≤ ã en toda geometría: el exponente "
                        "p − q = 4(ã − b)τ con τ = G m² t / (2ħ) es no negativo para todo t ≥ 0, evitando desbordamientos incluso en t = 10⁸ s."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Exact Overflow-Free Parallel Hybrid Negativity & Critical Dephasing Rate",
                    "label_es": "Negatividad Híbrida Paralela Exacta sin Desbordamiento y Tasa Crítica de Desfase",
                    "formula": "N_hyb(t) = max(0, ¼[u_+ + √(u_−² + 4 e^{−4ãτ} sin²(2bτ)) − 1]) ,    γ_crit^hyb = (G m² / ħ) max(0, √2 b − a)",
                    "note_en": (
                        "Here u_± = ½(e^{−4(ã−b)τ} ± e^{−4(ã+b)τ}) with τ = G m² t / (2ħ) (Peres, 1996). Matches 4 × 4 "
                        "numerical diagonalization to < 10⁻¹³ across 0° ≤ θ ≤ 180° and reproduces T.05's z = 10 µm threshold "
                        "γ_crit^hyb(33.1 µm) = 7.87 × 10⁻⁵ s⁻¹ analytically."
                    ),
                    "note_es": (
                        "Aquí u_± = ½(e^{−4(ã−b)τ} ± e^{−4(ã+b)τ}) con τ = G m² t / (2ħ) (Peres, 1996). Coincide con la "
                        "diagonalización 4 × 4 a < 10⁻¹³ entre 0° ≤ θ ≤ 180° y reproduce analíticamente el umbral "
                        "γ_crit^hyb(33.1 µm) = 7.87 × 10⁻⁵ s⁻¹ en z = 10 µm de T.05."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Expanding the partial-transpose determinant at short times τ → 0⁺ immediately yields the exact "
                        "analytical entanglement condition without a single time-grid search. The reflection-odd 2 × 2 block "
                        "has strictly positive eigenvalues for all τ > 0; negativity arises solely from the reflection-even "
                        "block whenever 8(2 b² − ã²) τ² > 0, that is, if and only if √2 b(θ) > ã. Setting γ_env = 0 defines "
                        "the exact geometric horizon √2 b(θ) = a, while solving √2 b(θ) = a + ħ γ_env / (G m²) gives the "
                        "closed-form environmental noise ceiling γ_crit^hyb = (G m² / ħ) max(0, √2 b − a)—reproducing the "
                        "log-bisection thresholds on Schut et al. (2024) z = 10 µm (2.17 × 10⁻⁴ s⁻¹ at 20 µm, 1.00 × 10⁻⁴ s⁻¹ "
                        "at 30 µm, and 7.87 × 10⁻⁵ s⁻¹ at 33.1 µm) directly from two error-function evaluations."
                    ),
                    "es": (
                        "Desarrollar el determinante de la transpuesta parcial para tiempos cortos τ → 0⁺ entrega la "
                        "condición exacta de entrelazamiento sin explorar mallas temporales. El bloque impar de 2 × 2 posee "
                        "autovalores estrictamente positivos para todo τ > 0; la negatividad nace únicamente del bloque par "
                        "cuando 8(2 b² − ã²) τ² > 0, es decir, si y solo si √2 b(θ) > ã. Fijar γ_env = 0 define el horizonte "
                        "geométrico exacto √2 b(θ) = a, y despejar √2 b(θ) = a + ħ γ_env / (G m²) entrega el techo cerrado "
                        "γ_crit^hyb = (G m² / ħ) max(0, √2 b − a), reproduciendo los umbrales de Schut et al. (2024) en "
                        "z = 10 µm (2.17 × 10⁻⁴ s⁻¹ a 20 µm, 1.00 × 10⁻⁴ s⁻¹ a 30 µm y 7.87 × 10⁻⁵ s⁻¹ a 33.1 µm)."
                    ),
                },
            ],
        },
        {
            "id": "loophole-free-island",
            "h2_en": "II · Why the Parallel Horizon Expands to 2.2109 σ — And Where the Loophole-Free Island Opens",
            "h2_es": "II · Por Qué el Horizonte Paralelo Crece hasta 2.2109 σ y Dónde se Abre la Isla sin Resquicios",
            "short_en": "II · 73.14 µm Ceiling & Island",
            "short_es": "II · Techo de 73.14 µm e Isla",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Tracing the exact root √2 b(0°) = a across all split-to-smearing ratios Δx / σ uncovers a striking "
                        "geometric reversal between collinear and parallel interferometers. In the collinear layout of Bose "
                        "et al. (2017) and Marletto and Vedral (2017), enlarging the superposition split L pushes the outer "
                        "branches apart while keeping self-decoherence high, so the critical nearest separation d_c(L) / σ "
                        "shrinks monotonically from 0.8509 at L / σ → 0 down to 0 above L / σ ≈ 0.878. In the parallel "
                        "layout, the opposite happens: as Δx / σ grows from 0 to ∞, the like-branch distance stays pinned "
                        "at D while both f(Δx; σ) and f(√(D² + Δx²); σ) vanish as 1 / Δx, causing D_c(Δx) / σ to expand "
                        "monotonically from s₀ = 1.5471 (σ_c / D = 0.6464) up to the universal asymptote s_∞ = 2.2109 "
                        "(σ_c / D = 0.4523), governed by (√π / s_∞) erf(s_∞ / 2) = 1 / √2."
                    ),
                    "es": (
                        "Seguir la raíz exacta √2 b(0°) = a en todo cociente Δx / σ descubre una inversión geométrica "
                        "notable entre interferómetros colineales y paralelos. En la disposición colineal de Bose et al. "
                        "(2017) y Marletto y Vedral (2017), agrandar la división L aleja las ramas externas y encoge la "
                        "separación crítica d_c(L) / σ desde 0.8509 cuando L / σ → 0 hasta 0 sobre L / σ ≈ 0.878. En la "
                        "disposición paralela ocurre lo contrario: al crecer Δx / σ de 0 a ∞, la distancia entre ramas "
                        "iguales permanece fija en D mientras f(Δx; σ) y f(√(D² + Δx²); σ) caen como 1 / Δx, ampliando "
                        "D_c(Δx) / σ de s₀ = 1.5471 (σ_c / D = 0.6464) hasta la asíntota universal s_∞ = 2.2109 "
                        "(σ_c / D = 0.4523), fijada por (√π / s_∞) erf(s_∞ / 2) = 1 / √2."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Universal Parallel Hybrid Horizon Asymptotes & Eöt-Wash 33.08 µm Ceiling",
                    "label_es": "Asíntotas Universales del Horizonte Híbrido Paralelo y Techo Eöt-Wash de 33.08 µm",
                    "formula": "1.547134 σ ≤ D_c(Δx, σ) < 2.210928 σ   ⟹   D_c,∞(33.08 µm) = 73.14 µm   (N_hyb ≡ 0 ∀ D ≥ 73.14 µm)",
                    "note_en": (
                        "DERIVED (NOT MEASURED) from Trillo & Navascués (2025) and the signed Fourier–Bessel recast of "
                        "Lee et al. (2020) (σ_95 = 33.08 µm; 73.18 µm at rounded 33.1 µm). Naive extrapolation of the "
                        "small-split 51.18 µm horizon fails at D = 60 µm, Δx = 250 µm where σ_c = 31.65 µm < 33.08 µm."
                    ),
                    "note_es": (
                        "DERIVADO (NO MEDIDO) a partir de Trillo y Navascués (2025) y el recast con signo de Fourier–Bessel "
                        "de Lee et al. (2020) (σ_95 = 33.08 µm; 73.18 µm al redondear a 33.1 µm). Extrapolar el umbral corto "
                        "de 51.18 µm falla en D = 60 µm, Δx = 250 µm donde σ_c = 31.65 µm < 33.08 µm."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "This 43% horizon expansion exposes a critical design trap and simultaneously maps out a clean "
                        "quantum corridor. Under the signed 95% Fourier–Bessel Yukawa recast of Lee et al. (2020) "
                        "(σ_95 = 33.08 µm), the small-split parallel horizon sits at 51.18 µm, whereas the infinite-split "
                        "ceiling sits at 73.14 µm (73.18 µm at rounded 33.1 µm). Suppose an experimenter builds a large-split "
                        "parallel interferometer at D = 60 µm and Δx = 250 µm assuming 51.18 µm suffices: the exact formula "
                        "gives σ_c(60 µm, 250 µm) = 31.65 µm < 33.08 µm, so Diósi–Penrose classical gravity at σ = 33.0 µm "
                        "still generates peak negativity 0.0014! Stepping across the universal ceiling to D = 75 µm at "
                        "Δx = 250 µm raises σ_c to 41.12 µm (and even as Δx → ∞, σ_c ≥ 33.92 µm > 33.08 µm), forcing "
                        "N_hyb(t) = 0.0000 at every hold time t ≥ 0 without relying on environmental noise to kill the hybrid signal."
                    ),
                    "es": (
                        "Esta expansión del 43% revela una trampa crítica de diseño y delimita a la vez un corredor cuántico "
                        "limpio. Con el recast con signo al 95% de Lee et al. (2020) (σ_95 = 33.08 µm), el horizonte paralelo "
                        "de división corta está en 51.18 µm, pero el techo de división infinita llega a 73.14 µm (73.18 µm "
                        "usando 33.1 µm). Si alguien construye un interferómetro paralelo en D = 60 µm y Δx = 250 µm creyendo "
                        "que bastan 51.18 µm, la fórmula exacta arroja σ_c(60 µm, 250 µm) = 31.65 µm < 33.08 µm, por lo que "
                        "la gravedad híbrida en σ = 33.0 µm aún alcanza negatividad 0.0014. Al cruzar el techo hacia D = 75 µm "
                        "con Δx = 250 µm, σ_c sube a 41.12 µm (y aun cuando Δx → ∞, σ_c ≥ 33.92 µm > 33.08 µm), forzando "
                        "N_hyb(t) = 0.0000 en todo t ≥ 0 sin depender del ruido ambiental."
                    ),
                },
                {
                    "type": "table",
                    "caption_en": "Table ES.07-A · Centre-to-Centre Casimir Screen Floor vs. Universal 73.14 µm Parallel Hybrid Ceiling",
                    "caption_es": "Tabla ES.07-A · Piso Casimir Centro a Centro frente al Techo Híbrido Paralelo Universal de 73.14 µm",
                    "headers_en": ["Diamond Mass m", "Sphere Radius R", "Casimir + 2R Floor D_min,cc", "Parallel Ceiling D_c,∞", "D = 75 µm Status"],
                    "headers_es": ["Masa Diamante m", "Radio Esfera R", "Piso Casimir + 2R D_min,cc", "Techo Paralelo D_c,∞", "Estado en D = 75 µm"],
                    "rows": [
                        [
                            ("10⁻¹⁵ kg", "10⁻¹⁵ kg"),
                            ("0.409 µm", "0.409 µm"),
                            ("17.92 µm", "17.92 µm"),
                            ("73.14 µm", "73.14 µm"),
                            ("Open (t_full = 261.2 s)", "Abierto (t_full = 261.2 s)"),
                        ],
                        [
                            ("10⁻¹⁴ kg", "10⁻¹⁴ kg"),
                            ("0.880 µm", "0.880 µm"),
                            ("28.29 µm", "28.29 µm"),
                            ("73.14 µm", "73.14 µm"),
                            ("Open Sweet Spot (t_full = 2.61 s)", "Óptimo Abierto (t_full = 2.61 s)"),
                        ],
                        [
                            ("10⁻¹³ kg", "10⁻¹³ kg"),
                            ("1.896 µm", "1.896 µm"),
                            ("45.25 µm", "45.25 µm"),
                            ("73.14 µm", "73.14 µm"),
                            ("Open (t_full = 0.026 s)", "Abierto (t_full = 0.026 s)"),
                        ],
                        [
                            ("10⁻¹² kg", "10⁻¹² kg"),
                            ("4.086 µm", "4.086 µm"),
                            ("73.30 µm", "73.30 µm"),
                            ("73.14 µm", "73.14 µm"),
                            ("Pinched below 73.30 µm", "Cerrado bajo 73.30 µm"),
                        ],
                    ],
                },
                {
                    "type": "p",
                    "en": (
                        "Does the unitary quantum channel still produce macroscopic, observable entanglement beyond 73.14 µm "
                        "without touching a Casimir screen? Including both the 1 µm conducting screen of Van De Kamp et al. "
                        "(2020) and the finite diamond radius R on each side sets the centre-to-centre Casimir floor at "
                        "D_min,cc = 28.29 µm for m = 10⁻¹⁴ kg (R = 0.880 µm), leaving a 45 µm margin up to 73.14 µm before "
                        "pinching shut at 10⁻¹² kg where D_min,cc = 73.30 µm overtakes 73.14 µm. At the benchmark point "
                        "D = 75 µm, Δx = 250 µm, m = 10⁻¹⁴ kg, and t = 2.5 s, the Newtonian cross-phase reaches "
                        "Δφ_N = 3.007 rad (t_full = 2.612 s). Under the extreme cryogenic Penning-trap vacuum demonstrated by "
                        "Sellner et al. (2017) (P_He = 2.7 × 10⁻¹⁶ Pa at T = 1.0 K, where blackbody photon scattering is only "
                        "γ_phot = 2.32 × 10⁻⁵ s⁻¹), the unitary channel delivers negativity N_Q = 0.4902 under hard-sphere "
                        "kinetic gas flux (γ_kin = 3.46 × 10⁻³ s⁻¹) and N_Q = 0.4302 under the conservative cited prefactor "
                        "(γ_cited = 2.90 × 10⁻² s⁻¹), against N_hyb = 0.0000."
                    ),
                    "es": (
                        "¿Produce aún el canal cuántico unitario un entrelazamiento observable más allá de 73.14 µm sin "
                        "chocar con la pantalla de Casimir? Sumar la placa conductora de 1 µm de Van De Kamp et al. (2020) "
                        "y el radio finito R del diamante a cada lado fija el piso centro a centro en D_min,cc = 28.29 µm "
                        "para m = 10⁻¹⁴ kg (R = 0.880 µm), dejando 45 µm de margen hasta 73.14 µm antes del cierre en 10⁻¹² kg donde "
                        "D_min,cc = 73.30 µm rebasa 73.14 µm. En el punto de referencia D = 75 µm, Δx = 250 µm, m = 10⁻¹⁴ kg "
                        "y t = 2.5 s, la fase newtoniana alcanza Δφ_N = 3.007 rad (t_full = 2.612 s). Bajo el vacío criogénico "
                        "demostrado por Sellner et al. (2017) (P_He = 2.7 × 10⁻¹⁶ Pa a T = 1.0 K, con dispersión fotónica "
                        "γ_phot = 2.32 × 10⁻⁵ s⁻¹), el canal cuántico entrega N_Q = 0.4902 con flujo cinético "
                        "(γ_kin = 3.46 × 10⁻³ s⁻¹) y N_Q = 0.4302 con el prefactor conservador (γ_cited = 2.90 × 10⁻² s⁻¹), "
                        "frente a N_hyb = 0.0000."
                    ),
                },
            ],
        },
        {
            "id": "cryogenic-and-skew-null",
            "h2_en": "III · Four Cryogenic Vacuum Ensembles and the Hardware-Free 90° Orthogonal Null Control",
            "h2_es": "III · Cuatro Colectividades de Vacío Criogénico y el Control Nulo Ortogonal a 90° sin Hardware Extra",
            "short_en": "III · Cryo Valleys & 90° Null",
            "short_es": "III · Valles Crio y Nulo a 90°",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Cooling a levitated dielectric microsphere does not automatically reduce decoherence unless one "
                        "specifies which thermodynamic variable the vacuum chamber holds fixed. Assuming bulk internal "
                        "thermalization T_int = T_env = T during free fall with Im(ε) = 10⁻⁴, blackbody dielectric emission "
                        "and absorption rise as B_em T⁶ (joined at higher T by B_sc T⁹ Rayleigh scattering), whereas "
                        "collisional gas scattering scales as n(T) √T. In an isobaric gauge-regulated chamber "
                        "(P = const, so n = P / k_B T ∝ T⁻¹), gas decoherence rises at lower temperatures as A_gas T⁻¹/², "
                        "creating a sharp analytical valley at T* = (A_gas / 12 B_em)^(2/13): at Δx = 250 µm and "
                        "P = 2.7 × 10⁻¹⁶ Pa, T* = 2.04 K (γ_min = 2.20 × 10⁻² s⁻¹); at P = 10⁻¹⁵ Pa, T* = 2.50 K "
                        "(γ_min = 7.37 × 10⁻² s⁻¹). By contrast, in a hermetically pinched-off cryogenic cell above "
                        "condensation (n = const, γ_gas ∝ T⁺¹/²), in a Knudsen thermal-transpiration tube connecting warm "
                        "and cold stages (P / √T = const, γ_gas = const), or in a cryo-pumped helium cell governed by "
                        "Clausius–Clapeyron vapour pressure P_vap(T), cooling monotonically lowers or flattens total noise."
                    ),
                    "es": (
                        "Enfriar una microesfera dieléctrica levitada no reduce automáticamente la decoherencia salvo que se "
                        "especifique qué variable termodinámica mantiene fija la cámara de vacío. Asumiendo equilibrio térmico "
                        "T_int = T_env = T en caída libre con Im(ε) = 10⁻⁴, la emisión y absorción dieléctrica de cuerpo negro "
                        "crecen como B_em T⁶ (sumadas a mayor T a la dispersión Rayleigh B_sc T⁹), mientras el gas escala como "
                        "n(T) √T. En régimen isobárico (P = const, n = P / k_B T ∝ T⁻¹), el gas crece al enfriar como "
                        "A_gas T⁻¹/², formando un valle analítico en T* = (A_gas / 12 B_em)^(2/13): con Δx = 250 µm y "
                        "P = 2.7 × 10⁻¹⁶ Pa resulta T* = 2.04 K (γ_min = 2.20 × 10⁻² s⁻¹), y con P = 10⁻¹⁵ Pa resulta "
                        "T* = 2.50 K (γ_min = 7.37 × 10⁻² s⁻¹). En cambio, en una celda hermética (n = const, γ_gas ∝ T⁺¹/²), "
                        "bajo transpiración térmica de Knudsen (P / √T = const) o con criobombeo P_vap(T), enfriar reduce o "
                        "aplana monótonamente el ruido total."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Even inside a loophole-free geometric and cryogenic corridor, an experimenter must prove that an "
                        "observed entanglement witness came from 1 / r gravity rather than stray electrostatic patch charges, "
                        "magnetic Stern–Gerlach cross-talk, or common-mode vibrational noise. Rotating one interferometer's "
                        "Stern–Gerlach gradient axis by angle θ about its midpoint while keeping D = 75 µm, Δx = 250 µm, "
                        "masses, laser pulses, and screening plate identical provides an exact, hardware-free zero-parameter "
                        "null control. As θ sweeps through 0°, 30°, 45°, 60°, and 90°, the Newtonian phase follows "
                        "r_same(θ) and r_diff(θ) smoothly (3.007, 1.943, 1.300, 0.790, and 0.000 rad at t = 2.5 s). At the "
                        "midpoint-centred '+' cross θ = 90°, r_same(90°) = r_diff(90°) = √(D² + 0.5 Δx²) = 192.03 µm: every "
                        "central pair potential V(r)—Newtonian, Yukawa, or erf-smeared—cancels identically across all four "
                        "branches to every multipole order! Crucially, midpoint centring is mandatory: an uncentred "
                        "corner-aligned L-layout leaves a spurious +(3 / 4) Δx⁴ / D⁵ Taylor residue (Δφ = 1.335 rad at D = 75 µm, "
                        "Δx = 250 µm) that would masquerade as false signal."
                    ),
                    "es": (
                        "Incluso dentro de un corredor geométrico y criogénico libre de resquicios, un experimento debe "
                        "demostrar que el testigo medido proviene de la gravedad 1 / r y no de cargas parásitas, diafonía "
                        "magnética de Stern–Gerlach o vibraciones comunes. Girar un eje de Stern–Gerlach un ángulo θ sobre "
                        "su punto medio manteniendo idénticos D = 75 µm, Δx = 250 µm, masas, pulsos y pantalla ofrece un "
                        "control nulo exacto sin cambiar piezas. Al recorrer θ = 0°, 30°, 45°, 60° y 90°, la fase newtoniana "
                        "traza 3.007, 1.943, 1.300, 0.790 y 0.000 rad en t = 2.5 s. En la cruz centrada '+' a θ = 90°, "
                        "r_same(90°) = r_diff(90°) = √(D² + 0.5 Δx²) = 192.03 µm: todo potencial central V(r) se cancela "
                        "exactamente en todo orden multipolar. El centrado es indispensable: una esquina en 'L' descentrada "
                        "deja un residuo espurio +(3 / 4) Δx⁴ / D⁵ (Δφ = 1.335 rad en D = 75 µm, Δx = 250 µm)."
                    ),
                },
                {
                    "type": "table",
                    "caption_en": "Table ES.07-B · 3-D Midpoint Skew-Angle Signature at D = 75 µm, Δx = 250 µm, m = 10⁻¹⁴ kg, t = 2.5 s",
                    "caption_es": "Tabla ES.07-B · Firma Angular 3-D Centrada en D = 75 µm, Δx = 250 µm, m = 10⁻¹⁴ kg, t = 2.5 s",
                    "headers_en": ["Skew Angle θ", "r_same(θ)", "r_diff(θ)", "Newtonian Phase Δφ_N", "Quantum N_Q (2.04 K Cited)", "Hybrid N_hyb (σ ≤ 33.08 µm)"],
                    "headers_es": ["Ángulo θ", "r_same(θ)", "r_diff(θ)", "Fase Newtoniana Δφ_N", "N_Q Cuántica (2.04 K Citado)", "N_hyb Híbrida (σ ≤ 33.08 µm)"],
                    "rows": [
                        [("0°", "0°"), ("75.00 µm", "75.00 µm"), ("261.01 µm", "261.01 µm"), ("3.007 rad", "3.007 rad"), ("0.4462", "0.4462"), ("0.0000", "0.0000")],
                        [("30°", "30°"), ("99.05 µm", "99.05 µm"), ("252.86 µm", "252.86 µm"), ("1.943 rad", "1.943 rad"), ("0.3648", "0.3648"), ("0.0000", "0.0000")],
                        [("45°", "45°"), ("121.56 µm", "121.56 µm"), ("242.84 µm", "242.84 µm"), ("1.300 rad", "1.300 rad"), ("0.2604", "0.2604"), ("0.0000", "0.0000")],
                        [("60°", "60°"), ("145.77 µm", "145.77 µm"), ("229.13 µm", "229.13 µm"), ("0.790 rad", "0.790 rad"), ("0.1560", "0.1560"), ("0.0000", "0.0000")],
                        [("90° (+ Cross)", "90° (Cruz +)"), ("192.03 µm", "192.03 µm"), ("192.03 µm", "192.03 µm"), ("0.000 rad", "0.000 rad"), ("0.0000", "0.0000"), ("0.0000", "0.0000")],
                    ],
                },
                {
                    "type": "bridge",
                    "kicker_en": "Cross-Scale Structural Bridge · Clocks, Vaults & Living Pores",
                    "kicker_es": "Puente Estructural entre Escalas · Relojes, Bóvedas y Poros Vivos",
                    "title_en": "Competing Power-Law Walls Define Every Feasible Mesoscopic Corridor",
                    "title_es": "Muros de Ley de Potencias Opuestos Definen Todo Corredor Mesoscópico Viable",
                    "paras": [
                        (
                            "Across all three pillars of Informatico.ai, feasible physical designs live inside narrow islands "
                            "carved by opposing power-law walls rather than unconstrained optima. Here a T⁻¹/² gas floor and "
                            "a T⁶ / T⁹ photon wall carve a 2.04 K valley while a D_min,cc Casimir wall and a 2.2109 σ torsion-recast "
                            "ceiling bound the 28.29 µm to 73.14 µm corridor; in masonry vaults (Folio A.01), thrust lines must "
                            "stay inside the middle-third Heyman kernel; and in airway mucus hydrogels studied around CFTR "
                            "anion transport in cystic fibrosis biophysics, nanoparticles face steric mesh-exclusion walls "
                            "at large radii and mucoadhesive electrostatic trapping at high surface charge.",
                            "En los tres pilares de Informatico.ai, los diseños físicamente viables habitan islas estrechas "
                            "esculpidas por muros opuestos de ley de potencias. Aquí un piso gaseoso T⁻¹/² y un muro fotónico "
                            "T⁶ / T⁹ fijan un valle a 2.04 K mientras el piso de Casimir D_min,cc y el techo de torsión 2.2109 σ "
                            "acotan el corredor de 28.29 µm a 73.14 µm; en bóvedas de piedra (Folio A.01), el empuje debe "
                            "permanecer en el núcleo central de Heyman; y en hidrogeles de moco estudiados junto al canal CFTR "
                            "en biofísica de fibrosis quística, las nanopartículas enfrentan exclusión estérica por tamaño y "
                            "atrapamiento electrostático por carga superficial.",
                        ),
                    ],
                },
            ],
        },
        {
            "id": "epistemic-boundaries",
            "h2_en": "IV · Why This Is Not a Theory of Everything: Four Sharp Epistemic Boundaries",
            "h2_es": "IV · Por Qué Esto No Es una Teoría del Todo: Cuatro Fronteras Epistémicas Nítidas",
            "short_en": "IV · Four Boundaries",
            "short_es": "IV · Cuatro Fronteras",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Deriving a parameter-free classical-hybrid horizon at 73.14 µm and pairing it with Wheeler–DeWitt "
                        "clock constraints (Essay ES.06) and Eöt-Wash sub-millimetre data is genuinely clarifying: it turns "
                        "qualitative arguments about 'testing quantum gravity on a tabletop' into falsifiable inequalities "
                        "where every assumption has a street address. Precisely for that reason, scientific honesty requires "
                        "stating four strict boundaries that separate this result from a Theory of Everything."
                    ),
                    "es": (
                        "Derivar un horizonte híbrido clásico libre de parámetros ajustables en 73.14 µm y acoplarlo con "
                        "restricciones de reloj de Wheeler–DeWitt (Ensayo ES.06) y datos submilimétricos de Eöt-Wash aporta "
                        "claridad real: convierte debates cualitativos sobre 'probar la gravedad cuántica en una mesa' en "
                        "desigualdades falsables. Precisamente por ello, la honestidad científica exige declarar cuatro "
                        "fronteras estrictas que separan este resultado de una Teoría del Todo."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "First, low-energy infrared scope versus ultraviolet completion: every equation on this page operates "
                        "in the non-relativistic, weak-field Newtonian sector Φ / c² ~ 10⁻⁴¹. Observing N_Q > 0 at D = 75 µm "
                        "would witness coherent quantum superposition of the Newtonian gravitational potential sourced by "
                        "delocalized mass—a historic milestone matching low-energy effective field theory—yet it does not "
                        "resolve Planck-scale renormalization at 1.62 × 10⁻³⁵ m, select between string theory, loop quantum "
                        "gravity, or asymptotic safety, determine black-hole interior unitarity, or couple the Standard Model "
                        "gauge group SU(3) × SU(2) × U(1) to spacetime curvature. Second, model-conditional elimination: "
                        "crossing D ≥ 73.14 µm rules out local-operations-and-classical-communication (LOCC) gravity channels "
                        "and the Diósi–Penrose σ-smeared hybrid master equation of Trillo and Navascués (2025) under the "
                        "33.08 µm recast, while Oppenheim et al. (2023) independently squeeze Markovian diffusive classical "
                        "gravity by 3.31 × 10¹⁶×; however, non-Markovian or higher-order quantum-field matter-vertex couplings "
                        "to classical metrics—such as Aziz and Howl (2025), whose predicted amplitude sits 25 to 34 orders of "
                        "magnitude below the Newtonian phase at 10⁻¹⁴ kg—must be discriminated by M⁶ t² scaling rather than "
                        "by the σ-smearing bound alone."
                    ),
                    "es": (
                        "Primero, alcance infrarrojo de baja energía frente a completitud ultravioleta: toda ecuación de "
                        "esta página opera en el régimen newtoniano débil Φ / c² ~ 10⁻⁴¹. Observar N_Q > 0 en D = 75 µm "
                        "atestiguaría la superposición cuántica coherente del potencial gravitatorio newtoniano —un hito "
                        "histórico—, pero no resuelve la renormalización a escala de Planck en 1.62 × 10⁻³⁵ m, no decide "
                        "entre cuerdas, lazos o seguridad asintótica, no fija el interior de agujeros negros ni acopla el "
                        "grupo gauge SU(3) × SU(2) × U(1) a la curvatura. Segundo, eliminación condicional al modelo: cruzar "
                        "D ≥ 73.14 µm descarta canales LOCC y la ecuación maestra híbrida difuminada en σ de Trillo y "
                        "Navascués (2025) bajo el recast de 33.08 µm, mientras Oppenheim et al. (2023) comprimen la difusión "
                        "clásica markoviana por 3.31 × 10¹⁶×; sin embargo, acoplamientos de orden superior como Aziz y Howl "
                        "(2025) —cuya amplitud cae entre 25 y 34 órdenes de magnitud bajo la fase newtoniana en 10⁻¹⁴ kg— "
                        "requieren distinguirse por su escalamiento M⁶ t²."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Third, published-table recast versus raw-data refit: the σ_95 = 33.08 µm bound projects the exact "
                        "120-fold Fourier–Bessel erf deficit onto the 66 signed Yukawa rows of Lee et al. (2020) over "
                        "52 µm to 3000 µm, where the erf shape matches a λ ≈ 0.55 σ Yukawa template to within 2% to 4%. "
                        "Because we do not possess the unpublished separation-by-separation covariance weights or systematic "
                        "nuisance parameters across the collaboration's 95 torsion runs, confirming whether the exact profile-"
                        "likelihood limit sits at 31 µm, 33 µm, or 36 µm awaits a direct refit by the Eöt-Wash group. Fourth, "
                        "DERIVED (NOT MEASURED) status: spatial superpositions of 10⁻¹⁴ kg nanocrystals across Δx = 250 µm "
                        "sit roughly nine orders of magnitude in mass above today's largest macromolecular interferometers. "
                        "Mathematics maps the exact island before the ship is built; only an experiment in vacuum can sail it."
                    ),
                    "es": (
                        "Tercero, proyección sobre tablas publicadas frente a reajuste de datos crudos: la cota "
                        "σ_95 = 33.08 µm proyecta el déficit exacto de Fourier–Bessel de 120 cuñas sobre las 66 filas con "
                        "signo de Yukawa de Lee et al. (2020) entre 52 µm y 3000 µm, donde el perfil erf imita una forma de "
                        "Yukawa λ ≈ 0.55 σ dentro del 2% al 4%. Sin las ponderaciones internas de covarianza de las 95 "
                        "corridas experimentales, confirmar si el límite exacto cae en 31 µm, 33 µm o 36 µm aguarda un "
                        "reajuste directo sobre los datos originales. Cuarto, estatuto DERIVADO (NO MEDIDO): superponer "
                        "nanocristales de 10⁻¹⁴ kg a Δx = 250 µm supera por unos nueve órdenes de magnitud en masa los mayores "
                        "interferómetros macromoleculares actuales. La matemática traza la isla; solo el laboratorio navega."
                    ),
                },
            ],
        },
        {
            "id": "lean4-parallel-spine",
            "h2_en": "V · Zero-Sorry Core Lean 4 Certification of the Parallel Horizon Spine",
            "h2_es": "V · Certificación sin Sorry en Lean 4 Base de la Columna Formal del Horizonte Paralelo",
            "short_en": "V · Lean 4 Proof Spine",
            "short_es": "V · Prueba en Lean 4",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Following the formal-methods standard of Tooby-Smith (2025) and Essay ES.06, the companion file "
                        "ParallelHorizon.lean encodes 9 non-tautological theorems in pure core Lean 4 Prelude with 0 external "
                        "imports and 0 occurrences of sorry, admit, or axiom. Theorem 1 (parallel_horizon_si_homogeneity) "
                        "verifies by kernel reduction that all 6 governing equations—the smeared pair rate, dimensionless "
                        "master-equation exponent, closed-form γ_crit^hyb, squared kinetic gas scattering rate, T⁹ thermal "
                        "blackbody photon rate, and R³ ħ c / d⁴ Casimir energy—carry exact SI integer dimension vectors. "
                        "Theorem 2 (even_block_radicand_strict_pos) proves strict positivity of the partial-transpose "
                        "discriminant radicand whenever coherent cross-phase is non-zero."
                    ),
                    "es": (
                        "Siguiendo el estándar formal de Tooby-Smith (2025) y del Ensayo ES.06, el archivo compañero "
                        "ParallelHorizon.lean codifica 9 teoremas no tautológicos en Lean 4 Prelude puro con 0 importaciones "
                        "externas y 0 usos de sorry, admit o axiom. El Teorema 1 (parallel_horizon_si_homogeneity) verifica "
                        "por reducción del núcleo que las 6 ecuaciones rectoras —tasa par difuminada, exponente adimensional, "
                        "umbral cerrado γ_crit^hyb, tasa cinética de gas al cuadrado, tasa fotónica térmica T⁹ y energía de "
                        "Casimir R³ ħ c / d⁴— portan vectores exactos de dimensión SI. El Teorema 2 "
                        "(even_block_radicand_strict_pos) demuestra la positividad estricta del discriminante par."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Theorems 3, 4, and 5 certify the 3-D skew geometry over universal integer polynomials: "
                        "skew_parallel_midpoint_difference proves r_diff² − r_same² = Δx² cos θ with exact cancellation of D² "
                        "(the identity that eliminated 12-digit floating-point loss down to 1.4 × 10⁻¹⁴ in our Python kernel); "
                        "orthogonal_cross_exact_null proves all-multipole cancellation at θ = 90°; and "
                        "uncentred_corner_nonzero_residue proves that an uncentred L-geometry leaves an exact +6 Δx⁴ fourth-"
                        "order numerator residue. Theorems 6 through 9 prove 3(k + 2)⁴ < (k + 2)⁸ for all k ∈ ℕ, environmental "
                        "dephasing monotonicity, the 28,147 nm < 51,178 nm < 73,136 nm < 75,000 nm horizon chain, and the "
                        "exact mass-pinch transition from open (10⁻¹⁵, 10⁻¹⁴, and 10⁻¹³ kg) to closed at 10⁻¹² kg (73,297 nm > "
                        "73,136 nm), mirrored by exact multivariate Fraction polynomial checks in verify_essay_parallel_horizon.py."
                    ),
                    "es": (
                        "Los Teoremas 3, 4 y 5 certifican la geometría 3-D sesgada sobre polinomios enteros universales: "
                        "skew_parallel_midpoint_difference prueba r_diff² − r_same² = Δx² cos θ con cancelación exacta de D² "
                        "(la identidad que eliminó la pérdida de 12 dígitos de precisión hasta 1.4 × 10⁻¹⁴ en nuestro núcleo Python); "
                        "orthogonal_cross_exact_null prueba la anulación multipolar en θ = 90°; y "
                        "uncentred_corner_nonzero_residue demuestra el residuo de cuarto orden +6 Δx⁴ en geometrías 'L' "
                        "descentradas. Los Teoremas 6 al 9 prueban 3(k + 2)⁴ < (k + 2)⁸ para todo k ∈ ℕ, la monotonía frente "
                        "al ruido, la cadena 28,147 nm < 51,178 nm < 73,136 nm < 75,000 nm y el cierre por masa entre "
                        "10⁻¹⁵, 10⁻¹⁴ y 10⁻¹³ kg (abiertos) y 10⁻¹² kg (73,297 nm > 73,136 nm, cerrado)."
                    ),
                },
            ],
        },
    ],
    "sidenotes": [
        {
            "label_en": "Sidenote 1 · Cancellation-Free Quadrature on [0, 1]",
            "label_es": "Nota al Margen 1 · Cuadratura sin Cancelación en [0, 1]",
            "en": (
                "Subtracting erf(r_diff / 2σ) / r_diff from erf(r_same / 2σ) / r_same loses 12 float64 digits at Δx / D = 10⁻⁶. "
                "Using r_diff² − r_same² = Δx² cos θ inside a 24-node Gauss–Legendre integral of −expm1(−Δα u²) keeps "
                "accuracy within 1.4 × 10⁻¹⁴ across all scales."
            ),
            "es": (
                "Restar erf(r_diff / 2σ) / r_diff de erf(r_same / 2σ) / r_same pierde 12 dígitos float64 en Δx / D = 10⁻⁶. "
                "Usar r_diff² − r_same² = Δx² cos θ en una integral de Gauss–Legendre de 24 nodos con −expm1(−Δα u²) "
                "conserva precisión de 1.4 × 10⁻¹⁴ en todas las escalas."
            ),
        },
        {
            "label_en": "Sidenote 2 · Centre-to-Centre vs. Surface Casimir Floors",
            "label_es": "Nota al Margen 2 · Piso Casimir Centro a Centro frente a Superficie",
            "en": (
                "At m = 10⁻¹⁴ kg (R = 0.88 µm), adding 2R shifts the 26.53 µm surface floor modestly to 28.29 µm. At "
                "m = 10⁻¹² kg (R = 4.09 µm), 2R = 8.17 µm lifts the 65.13 µm surface floor to 73.30 µm—pushing it past "
                "the 73.14 µm parallel hybrid ceiling."
            ),
            "es": (
                "Para m = 10⁻¹⁴ kg (R = 0.88 µm), sumar 2R eleva el piso superficial de 26.53 µm a 28.29 µm. Para "
                "m = 10⁻¹² kg (R = 4.09 µm), 2R = 8.17 µm lleva el piso de 65.13 µm hasta 73.30 µm, superando el "
                "techo híbrido paralelo de 73.14 µm."
            ),
        },
        {
            "label_en": "Sidenote 3 · Kinetic Flux vs. Cited Dipolar Scattering",
            "label_es": "Nota al Margen 3 · Flujo Cinético frente a Dispersión Dipolar Citada",
            "en": (
                "Short-wavelength gas decoherence differs by an 8.38× numerical prefactor between pure geometric "
                "hard-sphere impingement (3.46 × 10⁻³ s⁻¹ at 2.7 × 10⁻¹⁶ Pa, 1 K) and the diffraction-enhanced formula "
                "cited in QGEM proposals (2.90 × 10⁻² s⁻¹). Both preserve strong quantum negativity (0.4902 and 0.4302)."
            ),
            "es": (
                "La decoherencia por gas difiere por un prefactor de 8.38× entre el impacto geométrico de esfera dura "
                "(3.46 × 10⁻³ s⁻¹ a 2.7 × 10⁻¹⁶ Pa, 1 K) y la fórmula con difracción citada en propuestas QGEM "
                "(2.90 × 10⁻² s⁻¹). Ambas preservan alta negatividad cuántica (0.4902 y 0.4302)."
            ),
        },
        {
            "label_en": "Sidenote 4 · Midpoint '+' Cross vs. Corner 'L' Alignment",
            "label_es": "Nota al Margen 4 · Cruz Centrada '+' frente a Esquina Descentrada 'L'",
            "en": (
                "Rotating arm B by 90° about one endpoint rather than its midpoint leaves r_LL = D and "
                "r_RR = √(D² + 2 Δx²), creating a +(3 / 4) Δx⁴ / D⁵ residue (1.335 rad at D = 75 µm, Δx = 250 µm). "
                "Midpoint symmetry equates r_same and r_diff identically."
            ),
            "es": (
                "Girar el brazo B 90° sobre un extremo en vez de su punto medio deja r_LL = D y r_RR = √(D² + 2 Δx²), "
                "creando un residuo +(3 / 4) Δx⁴ / D⁵ (1.335 rad en D = 75 µm, Δx = 250 µm). El centrado iguala "
                "r_same y r_diff de forma exacta."
            ),
        },
    ],
    "sources": [
        {
            "id": "ES07-LINDBLAD1976",
            "citation": "Lindblad, G. — On the generators of quantum dynamical semigroups, Communications in Mathematical Physics 48(2), 119–130",
            "doi": "10.1007/bf01608499",
            "year": 1976,
            "role_en": "Defines the completely positive Markovian generator governing single-body environmental dephasing γ_env.",
            "role_es": "Define el generador markoviano completamente positivo que rige el desfase ambiental local γ_env.",
        },
        {
            "id": "ES07-DIOSI1987",
            "citation": "Diósi, L. — A universal master equation for the gravitational violation of quantum mechanics, Physics Letters A 120(8), 377–381",
            "doi": "10.1016/0375-9601(87)90681-5",
            "year": 1987,
            "role_en": "Introduces the Gaussian σ-smeared gravitational self-decoherence master equation.",
            "role_es": "Introduce la ecuación maestra de autodecoherencia gravitatoria con suavizado gaussiano σ.",
        },
        {
            "id": "ES07-PERES1996",
            "citation": "Peres, A. — Separability criterion for density matrices, Physical Review Letters 77(8), 1413–1415",
            "doi": "10.1103/physrevlett.77.1413",
            "year": 1996,
            "role_en": "Provides the partial-transpose negativity criterion block-diagonalized analytically in Section I.",
            "role_es": "Aporta el criterio de negatividad por transpuesta parcial diagonalizado analíticamente en la Sección I.",
        },
        {
            "id": "ES07-SELLNER2017",
            "citation": "Sellner, S., Besirli, M., Bohman, M., Borchert, M. J., Harrington, J., Higuchi, T., Mooser, A., Nagahama, H., Schneider, G., Smorra, C., Tanaka, T., Blaum, K., Matsuda, Y., Ospelkaus, C., Quint, W., Walz, J., Yamazaki, Y., & Ulmer, S. — Improved limit on the directly measured antiproton lifetime, New Journal of Physics 19(8), 083023",
            "doi": "10.1088/1367-2630/aa7e73",
            "year": 2017,
            "role_en": "Demonstrates extreme cryogenic Penning-trap vacuum below 2.7 × 10⁻¹⁶ Pa anchoring the D = 75 µm benchmark.",
            "role_es": "Demuestra vacío criogénico extremo bajo 2.7 × 10⁻¹⁶ Pa usado en el punto de referencia D = 75 µm.",
        },
        {
            "id": "ES07-BOSE2017",
            "citation": "Bose, S., Mazumdar, A., Morley, G. W., Ulbricht, H., Toroš, M., Paternostro, M., Geraci, A. A., Barker, P. F., Kim, M. S., & Milburn, G. — Spin entanglement witness for quantum gravity, Physical Review Letters 119(24), 240401",
            "doi": "10.1103/physrevlett.119.240401",
            "year": 2017,
            "role_en": "Establishes the four-branch Stern–Gerlach matter-wave gravitational entanglement protocol.",
            "role_es": "Establece el protocolo de entrelazamiento gravitatorio de cuatro ramas mediante gradientes Stern–Gerlach.",
        },
        {
            "id": "ES07-MARLETTO2017",
            "citation": "Marletto, C., & Vedral, V. — Gravitationally induced entanglement between two massive particles is sufficient evidence of quantum effects in gravity, Physical Review Letters 119(24), 240402",
            "doi": "10.1103/physrevlett.119.240402",
            "year": 2017,
            "role_en": "Proves that LOCC classical mediators cannot generate entanglement from product states.",
            "role_es": "Demuestra que mediadores clásicos LOCC no pueden generar entrelazamiento desde estados producto.",
        },
        {
            "id": "ES07-LEE2020",
            "citation": "Lee, J. G., Adelberger, E. G., Cook, T. S., Fleischer, S. M., & Heckel, B. R. — New test of the gravitational 1/r² law at separations down to 52 µm, Physical Review Letters 124(10), 101101",
            "doi": "10.1103/physrevlett.124.101101",
            "year": 2020,
            "role_en": "Supplies the sub-millimetre 120-fold wedge limits down to 52 µm recasted to σ_95 = 33.08 µm.",
            "role_es": "Aporta los límites de 120 cuñas a 52 µm proyectados al umbral con signo σ_95 = 33.08 µm.",
        },
        {
            "id": "ES07-VANDEKAMP2020",
            "citation": "Van De Kamp, T. W., Marshman, R. J., Bose, S., & Mazumdar, A. — Quantum gravity witness via entanglement of masses: Casimir screening, Physical Review A 102(6), 062807",
            "doi": "10.1103/physreva.102.062807",
            "year": 2020,
            "role_en": "Defines the conducting Casimir screen minimum distance and gas/blackbody decoherence scaling laws.",
            "role_es": "Define la separación mínima con pantalla de Casimir y las tasas de decoherencia por gas y cuerpo negro.",
        },
        {
            "id": "ES07-OPPENHEIM2023",
            "citation": "Oppenheim, J., Sparaciari, C., Šoda, B., & Weller-Davies, Z. — Gravitationally induced decoherence vs space-time diffusion: testing the quantum nature of gravity, Nature Communications 14, 7910",
            "doi": "10.1038/s41467-023-43348-2",
            "year": 2023,
            "role_en": "Bounds consistent Markovian post-quantum classical gravity via stochastic momentum diffusion.",
            "role_es": "Acota toda gravedad clásica markoviana consistente mediante difusión estocástica de momento.",
        },
        {
            "id": "ES07-SCHUT2024",
            "citation": "Schut, M., Geraci, A., Bose, S., & Mazumdar, A. — Micrometer-size spatial superpositions for the QGEM protocol via screening and trapping, Physical Review Research 6(1), 013199",
            "doi": "10.1103/physrevresearch.6.013199",
            "year": 2024,
            "role_en": "Introduces the parallel screened QGEM configuration generalized analytically to all splits here.",
            "role_es": "Introduce la configuración QGEM paralela apantallada generalizada aquí analíticamente a toda división.",
        },
        {
            "id": "ES07-TRILLO2025",
            "citation": "Trillo, D., & Navascués, M. — Diósi–Penrose model of classical gravity predicts gravitationally induced entanglement, Physical Review D 111(12), L121101",
            "doi": "10.1103/physrevd.111.l121101",
            "year": 2025,
            "role_en": "Formulates the σ-smeared hybrid classical-gravity master equation solved in closed form in Section I.",
            "role_es": "Formula la ecuación maestra híbrida con suavizado σ resuelta en forma cerrada en la Sección I.",
        },
        {
            "id": "ES07-AZIZ2025",
            "citation": "Aziz, J., & Howl, R. — Classical theories of gravity produce entanglement, Nature 646, 813–817",
            "doi": "10.1038/s41586-025-09595-7",
            "year": 2025,
            "role_en": "Illustrates higher-order matter-vertex classical-metric couplings discussed in Epistemic Boundary 2.",
            "role_es": "Ilustra acoplamientos de orden superior entre vértices de materia y métrica clásica en la Frontera 2.",
        },
        {
            "id": "ES07-TOOBYSMITH2025",
            "citation": "Tooby-Smith, J. — HepLean: Digitalising high energy physics, Computer Physics Communications 308, 109457",
            "doi": "10.1016/j.cpc.2024.109457",
            "year": 2025,
            "role_en": "Establishes the Lean 4 dimensional and algebraic verification methodology used in ParallelHorizon.lean.",
            "role_es": "Establece la metodología de verificación dimensional y algebraica en Lean 4 usada en ParallelHorizon.lean.",
        },
    ],
    "skill_path": "skills/essays/loophole-free-parallel-horizon/SKILL.md",
    "verifier_path": "skills/essays/loophole-free-parallel-horizon/verify_essay_parallel_horizon.py",
    "ai_line_en": (
        "AI contribution to cited primary literature: none. Essay prose, bilingual es-MX twin, closed-form 3-D "
        "skewed parallel Diósi–Penrose solver, cryogenic valley & 90° null observatory, core Lean 4 specification, "
        "and Python verifier were drafted with AI assistance and checked deterministically against cached primary DOIs."
    ),
    "ai_line_es": (
        "Contribución de IA a la literatura primaria citada: ninguna. El ensayo, su gemelo es-MX, el solucionador "
        "cerrado 3-D de Diósi–Penrose paralelo, el observatorio criogénico y nulo a 90°, la especificación en Lean 4 "
        "y el verificador en Python se redactaron con apoyo de IA y se verificaron contra DOIs primarios en caché."
    ),
}
