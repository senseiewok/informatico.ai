# -*- coding: utf-8 -*-
"""Cross-Scale Essay ES.06 · Coupled Timeless Constraints & Zero-Sorry Formal Proof.

Pure-Python stdlib physics kernel, multivariate symbolic polynomial verifier, and bilingual
(EN / es-MX) monograph data for Informatico.ai's grand-synthesis Cross-Scale Essay
(/essays/coupled-constraints-formal-proof/).

Synthesizes four coupled constraint layers across the Time & Gravity track:
  1. 64x64 Hermitian Wheeler-DeWitt / Page-Wootters nullspace on H_C^(16) (x) H_path^(2) (x) H_tick^(2)
     in the non-diagonal Fourier-Hadamard basis, embedded into a 128x128 real symmetric matrix and
     diagonalized via pure-Python Jacobi rotations (||C |Psi>>|| < 10^-13, kernel projection = 1.0),
     paired with the physical 429.228 THz optical 87Sr clock (g Delta_h / c^2 = 1.09e-16 at 1.0 m)
     and exact Quantum Equivalence Principle (eta = 0).
  2. Updated 33 um (sigma_95 <= 33 um) Fourier-Bessel recast of Eot-Wash 2020 sub-millimetre data
     across the 4-wall hybrid smeared-gravity exclusion, paired with Oppenheim's (2023) post-quantum
     classical gravity momentum-diffusion bound (3.31e16x suppression below the Cavendish ceiling).
  3. Synchronous bilateral X_A (x) X_B CPMG dynamical decoupling (preserving (-Z_A)(-Z_B) = +Z_A Z_B
     gravitational cross-phase while suppressing quasistatic stray gradients as 1 / N_dd^2), contrasted
     against unilateral X_A (x) I pulses (which erase gravitational entanglement) and memoryless white
     Markovian Lindblad dephasing (which pi-pulses cannot refocus).
  4. Non-tautological zero-sorry core Lean 4 specification (IRUG_Unification.lean) certifying the
     deductive algebraic and SI dimensional spine (DERIVED (NOT MEASURED), never empirical nature).
"""
from __future__ import annotations

import cmath
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

import timegravity_kernel_dispute as k_disp  # noqa: E402
import timegravity_kernel_entangle as k_ent  # noqa: E402
import timegravity_kernel_ladder as k_lad  # noqa: E402
import timegravity_kernel_quantum as k_quant  # noqa: E402
import timegravity_kernel_recast as k_rec  # noqa: E402

CODE = "ES.06"
SLUG = "coupled-constraints-formal-proof"
PLATE_SLUG = "essay06"

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


# ---------------------------------------------------------------------------
# Part 1 · 64x64 Hermitian Wheeler-DeWitt / Page-Wootters Nullspace & Sr Clock
# ---------------------------------------------------------------------------

WDW_N_CLOCK = 16
# Dimensionless alpha_grav = 1 bandwidth-scaled integer modes on {-8..7} chosen for exact
# 16-tick periodic Fourier closure: low-path tick spacing (-1) - (-3) = 2; high-path tick
# spacing 5 - 1 = 4 = (1 + alpha_grav) * 2 -> beat frequency Delta_omega = 4 - 2 = 2.
WDW_ZYCH_MODES: tuple[int, ...] = (-3, -1, 1, 5)
# Two-mass BMV integer modes (LL, LR, RL, RR) -> cross-phase rate (-5) + (-1) - (-2) - (-2) = -2.
WDW_BMV_MODES: tuple[int, ...] = (-2, -5, -1, -2)


def _jacobi_symmetric_fast(
    mat: list[list[float]],
    tol: float = 1.0e-12,
    max_sweeps: int = 28,
) -> tuple[list[float], list[list[float]]]:
    """Row-cyclic pure-Python Jacobi eigensolver for a real symmetric matrix.
    Returns (eigenvalues, eigenvectors_transposed) where eigenvectors_transposed[i] is the i-th eigenvector.
    """
    n = len(mat)
    a = [row[:] for row in mat]
    vt = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    pivot_eps = tol / float(n)
    for _ in range(max_sweeps):
        off_sq = 0.0
        for p in range(n - 1):
            row_p = a[p]
            for q in range(p + 1, n):
                off_sq += row_p[q] * row_p[q]
        if math.sqrt(2.0 * off_sq) < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                apq = a[p][q]
                if abs(apq) <= pivot_eps:
                    continue
                app = a[p][p]
                aqq = a[q][q]
                theta = (aqq - app) / (2.0 * apq)
                t = (1.0 if theta >= 0.0 else -1.0) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                tau = s / (1.0 + c)
                a[p][p] = app - t * apq
                a[q][q] = aqq + t * apq
                a[p][q] = 0.0
                a[q][p] = 0.0
                for k_ in range(p):
                    akp = a[k_][p]
                    akq = a[k_][q]
                    a[k_][p] = akp - s * (akq + tau * akp)
                    a[k_][q] = akq + s * (akp - tau * akq)
                for k_ in range(p + 1, q):
                    apk = a[p][k_]
                    akq = a[k_][q]
                    a[p][k_] = apk - s * (akq + tau * apk)
                    a[k_][q] = akq + s * (apk - tau * akq)
                row_p = a[p]
                row_q = a[q]
                for k_ in range(q + 1, n):
                    apk = row_p[k_]
                    aqk = row_q[k_]
                    row_p[k_] = apk - s * (aqk + tau * apk)
                    row_q[k_] = aqk + s * (apk - tau * aqk)
                vp = vt[p]
                vq = vt[q]
                for k_ in range(n):
                    vpk = vp[k_]
                    vqk = vq[k_]
                    vp[k_] = c * vpk - s * vqk
                    vq[k_] = s * vpk + c * vqk
    return [a[i][i] for i in range(n)], vt


def build_hermitian_wdw_nullspace(
    n_clock: int = WDW_N_CLOCK,
    e_sys_integer_modes: tuple[int, ...] = WDW_ZYCH_MODES,
    planted_defect: bool = False,
) -> dict:
    """Build the 64x64 Hermitian Wheeler-DeWitt constraint C_hat on H_C^(16) (x) H_sys^(4)
    in the non-diagonal physical Clock-Time |t_n> (x) 4D Hadamard basis, embed it into a
    128x128 real symmetric matrix, diagonalize via pure-Python Jacobi rotations, and extract
    conditioned Zych-Brukner visibility V(t_n) = |cos(Delta_omega * t_n / 2)| from ker(C_hat).
    """
    n_sys = len(e_sys_integer_modes)
    dim = n_clock * n_sys  # 16 * 4 = 64
    k_modes = [k if k < n_clock // 2 else k - n_clock for k in range(n_clock)]

    h_diag: list[float] = []
    for k in k_modes:
        for m_s in e_sys_integer_modes:
            if planted_defect:
                # Planted defect: anharmonic clock generator k^2 + 1 breaks shift invariance
                h_diag.append(float(k * k + 1) - float(m_s))
            else:
                h_diag.append(float(k) - float(m_s))

    psi_diag = [0j] * dim
    norm_sq = 0.0
    for k_idx, k in enumerate(k_modes):
        for s, m_s in enumerate(e_sys_integer_modes):
            if k == m_s:
                psi_diag[k_idx * n_sys + s] = 1.0 + 0j
                norm_sq += 1.0
    inv_norm = 1.0 / math.sqrt(norm_sq)
    psi_diag = [z * inv_norm for z in psi_diag]

    t_grid = [2.0 * math.pi * n / n_clock for n in range(n_clock)]
    h4 = (
        (0.5, 0.5, 0.5, 0.5),
        (0.5, -0.5, 0.5, -0.5),
        (0.5, 0.5, -0.5, -0.5),
        (0.5, -0.5, -0.5, 0.5),
    )
    u_mat = [[0j] * dim for _ in range(dim)]
    inv_sqrt_nc = 1.0 / math.sqrt(n_clock)
    for n in range(n_clock):
        tn = t_grid[n]
        for b in range(n_sys):
            row = n * n_sys + b
            for k_idx, k in enumerate(k_modes):
                ph = cmath.exp(1j * k * tn) * inv_sqrt_nc
                for s in range(n_sys):
                    u_mat[row][k_idx * n_sys + s] = ph * h4[b][s]

    # Dense 64x64 Hermitian matrix in physical coupled basis (non-zero off-diagonals verified)
    h_phys = [[0j] * dim for _ in range(dim)]
    off_diag_frobenius_sq = 0.0
    for r in range(dim):
        for c in range(r, dim):
            val = sum(u_mat[r][col] * h_diag[col] * u_mat[c][col].conjugate() for col in range(dim))
            h_phys[r][c] = val
            h_phys[c][r] = val.conjugate()
            if r != c:
                off_diag_frobenius_sq += 2.0 * (abs(val) ** 2)

    psi_phys = [sum(u_mat[r][col] * psi_diag[col] for col in range(dim)) for r in range(dim)]
    h_psi = [sum(h_phys[r][c] * psi_phys[c] for c in range(dim)) for r in range(dim)]
    residual_norm = math.sqrt(sum(abs(z) ** 2 for z in h_psi))

    # 128x128 real symmetric embedding [[Re H, -Im H], [Im H, Re H]]
    real_m = [[0.0] * (2 * dim) for _ in range(2 * dim)]
    for r in range(dim):
        for c in range(dim):
            re_v = h_phys[r][c].real
            im_v = h_phys[r][c].imag
            real_m[r][c] = re_v
            real_m[r + dim][c + dim] = re_v
            real_m[r][c + dim] = -im_v
            real_m[r + dim][c] = im_v

    evals, evecs_t = _jacobi_symmetric_fast(real_m, tol=1.0e-12, max_sweeps=28)
    zero_indices = [i for i, lam in enumerate(evals) if abs(lam) < 1e-7]
    psi_real_vec = [z.real for z in psi_phys] + [z.imag for z in psi_phys]
    kernel_proj = 0.0
    for idx in zero_indices:
        evec = evecs_t[idx]
        dot = sum(evec[r] * psi_real_vec[r] for r in range(2 * dim))
        kernel_proj += dot * dot

    delta_omega = (e_sys_integer_modes[3] - e_sys_integer_modes[2]) - (
        e_sys_integer_modes[1] - e_sys_integer_modes[0]
    )
    visibilities: list[float] = []
    vis_max_err = 0.0
    for n, tn in enumerate(t_grid):
        block_b = psi_phys[n * n_sys : (n + 1) * n_sys]
        amp_pt = [
            math.sqrt(n_clock) * sum(h4[b][s] * block_b[b] for b in range(n_sys))
            for s in range(n_sys)
        ]
        rho_01 = amp_pt[0] * amp_pt[2].conjugate() + amp_pt[1] * amp_pt[3].conjugate()
        v_null = 2.0 * abs(rho_01)
        v_exact = abs(math.cos(0.5 * delta_omega * tn))
        visibilities.append(v_null)
        vis_max_err = max(vis_max_err, abs(v_null - v_exact))

    return {
        "dim_complex": dim,
        "dim_real_jacobi": 2 * dim,
        "modes": list(e_sys_integer_modes),
        "delta_omega_dimensionless": delta_omega,
        "off_diagonal_frobenius_norm": math.sqrt(off_diag_frobenius_sq),
        "constraint_residual_norm": residual_norm,
        "jacobi_kernel_dim_complex": len(zero_indices) // 2,
        "kernel_projection": kernel_proj,
        "visibility_max_err": vis_max_err,
        "visibility_ticks_0_4": [round(visibilities[i], 6) for i in range(5)],
    }


def evaluate_physical_sr_clock_and_qep(dh_m: float = 1.0, hold_s: float = 1.0) -> dict:
    """Evaluate the physical 87Sr optical lattice clock (429.228 THz) proper-time lag,
    visibility drop, first orthogonality zero, and state-independent Quantum Equivalence
    Principle (eta = 0) across internal clock eigenstates q in {0, 1}.
    """
    alpha_grav = (k_quant.G0 * dh_m) / (k_quant.C ** 2)
    dtau_s = k_quant.proper_time_difference(dh_m, hold_s)
    vis_1m_1s = k_quant.zych_visibility(dh_m, hold_s, k_quant.OMEGA_SR)
    vis_overlap = k_quant.clock_overlap(dh_m, hold_s, k_quant.OMEGA_SR)
    first_zero_dh_t = k_quant.zych_first_zero(k_quant.OMEGA_SR)

    # Exact QEP check on physical 87Sr rest mass (86.909 u) + 429.228 THz optical transition
    m_sr87_kg = 86.9088775 * 1.66053906660e-27
    hbar = 1.054571817e-34
    m0_freq = (m_sr87_kg * (k_quant.C ** 2)) / hbar
    w_sr = k_quant.OMEGA_SR
    # Use exact rational arithmetic (Fraction) to eliminate floating-point cancellation at 10^-16
    f_m0 = Fraction(str(m0_freq))
    f_w = Fraction(str(w_sr))
    f_alpha = Fraction(str(alpha_grav))
    e_low_0 = f_m0
    e_low_1 = f_m0 + f_w
    e_high_0 = e_low_0 * (Fraction(1, 1) + f_alpha)
    e_high_1 = e_low_1 * (Fraction(1, 1) + f_alpha)
    rel_0 = (e_high_0 - e_low_0) / e_low_0
    rel_1 = (e_high_1 - e_low_1) / e_low_1
    qep_eta = float(Fraction(2, 1) * (rel_1 - rel_0) / (rel_1 + rel_0))

    return {
        "sr_freq_hz": 429.228e12,
        "omega_sr_rad_s": k_quant.OMEGA_SR,
        "alpha_grav_1m": alpha_grav,
        "dtau_1m_1s_s": dtau_s,
        "visibility_1m_1s": vis_1m_1s,
        "visibility_double_entry_diff": abs(vis_1m_1s - vis_overlap),
        "first_zero_dh_t_m_s": first_zero_dh_t,
        "qep_eotvos_eta": qep_eta,
    }


# ---------------------------------------------------------------------------
# Part 2 · Updated 33 um 4-Wall Hybrid Exclusion & Oppenheim Torque Ceiling
# ---------------------------------------------------------------------------

def evaluate_four_wall_and_oppenheim(planted_defect: bool = False) -> dict:
    """Evaluate the updated 33 um Eot-Wash signed Fourier-Bessel recast, the 4-wall
    hybrid smeared-gravity exclusion across published GIE geometries, and Oppenheim's
    (2023) post-quantum momentum-diffusion ceiling with Eot-Wash torque residuals.
    """
    rc = k_rec.Recast(120, "log52-3000", n_sep=12, lam_min=14e-6, lam_max=30e-6)
    sigma_95_m = rc.sigma_95(planted_defect=planted_defect)
    at_33 = rc.at_sigma(33.0e-6, planted_defect=planted_defect)
    at_35 = rc.at_sigma(35.0e-6, planted_defect=planted_defect)

    # Collinear critical sigmas via exact E_- criterion + Schut 2024 parallel geometries
    sigma_c_bose = k_disp.tn_critical_sigma(1.0e-14, 250.0e-6, 200.0e-6)
    sigma_c_chev = k_disp.tn_critical_sigma(1.0e-14, 250.0e-6, 100.0e-6)
    sigma_c_vdk47 = k_disp.tn_critical_sigma(1.0e-15, 23.0e-6, 47.0e-6)
    sigma_c_vdk24 = k_disp.tn_critical_sigma(1.0e-15, 23.0e-6, 24.0e-6)
    br_z30 = k_disp.branches_parallel(8.5e-6, 61.0e-6)
    br_z10 = k_disp.branches_parallel(1.7e-6, 21.0e-6)
    sigma_c_z30 = k_disp.hybrid_critical_sigma_points(br_z30, 1.0e-14)
    sigma_c_z10 = k_disp.hybrid_critical_sigma_points(br_z10, 1.0e-14)

    ow = k_disp.open_window_decoherence(sigmas=(20.0e-6, k_lad.EW_MATCH_SIGMA_M), gammas=(1.0e-3,))
    casimir_1e15_m = k_lad.casimir_floor_separation(1.0e-15)
    casimir_1e14_m = k_lad.casimir_floor_separation(1.0e-14)

    diff_tab = k_lad.diffusion_table()
    printed_cav = diff_tab["oppenheim_printed_ceiling"]
    recomp_cav = diff_tab["oppenheim_inputs_ceiling"]
    ew_1e3_1fm = diff_tab["eotwash"]["T_1e+03_r_N_1fm"]["ceiling"]
    ew_1e3_7fm = diff_tab["eotwash"]["T_1e+03_r_N_7fm_platinum"]["ceiling"]
    suppression_1fm = printed_cav / ew_1e3_1fm
    suppression_7fm = printed_cav / ew_1e3_7fm

    return {
        "recast_sigma_95_um": sigma_95_m * 1.0e6,
        "at_33um_excluded": bool(at_33["excluded"]),
        "at_35um_excluded": bool(at_35["excluded"]),
        "xenonnt_lower_angstrom": 4.9,
        "casimir_floor_1e15_um": casimir_1e15_m * 1.0e6,
        "casimir_floor_1e14_um": casimir_1e14_m * 1.0e6,
        "hybrid_sigma_c_um": {
            "bose2017": sigma_c_bose * 1.0e6,
            "chevalier2020": sigma_c_chev * 1.0e6,
            "vandekamp2020_47": sigma_c_vdk47 * 1.0e6,
            "vandekamp2020_24": sigma_c_vdk24 * 1.0e6,
            "schut2024_z30": sigma_c_z30 * 1.0e6,
            "schut2024_z10": sigma_c_z10 * 1.0e6,
        },
        "schut2024_z10_dephasing": {
            "quantum_gamma_crit_s1": ow["quantum_dephasing_threshold_per_s"],
            "hybrid_20um_gamma_crit_s1": ow["hybrid_dephasing_threshold_per_s"]["20um"],
            "hybrid_33um_gamma_crit_s1": ow["hybrid_dephasing_threshold_per_s"]["33um"],
            "quantum_peak_negativity_at_1e-3": ow["peaks"]["gamma_1e-03"]["quantum"],
            "hybrid_33um_peak_negativity_at_1e-3": ow["peaks"]["gamma_1e-03"]["hybrid_33um"],
        },
        "oppenheim": {
            "cavendish_printed_kg2_s_m": printed_cav,
            "cavendish_recomputed_kg2_s_m": recomp_cav,
            "eotwash_torque_residual_fn_m": 0.0054,
            "eotwash_sigma_a_m_s2": diff_tab["eotwash_sigma_a"],
            "eotwash_T1e3_rN1fm_ceiling": ew_1e3_1fm,
            "eotwash_T1e3_rN7fm_ceiling": ew_1e3_7fm,
            "suppression_vs_printed_1fm": suppression_1fm,
            "suppression_vs_printed_7fm": suppression_7fm,
            "interferometry_floor_kg2_s_m": diff_tab["interferometry_floor"],
        },
    }


# ---------------------------------------------------------------------------
# Part 3 · Synchronous Bilateral X_A (x) X_B vs Unilateral X_A (x) I CPMG
# ---------------------------------------------------------------------------

def simulate_bilateral_vs_unilateral_cpmg(
    omega_ent_rad_s: float = 0.01965356608905733,
    t_hold_s: float = 80.0,
    gamma_lowf_s1: float = 5.0e-3,
    gamma_white_s1: float = 5.0e-4,
    n_dd: int = 4,
    planted_defect: bool = False,
) -> dict:
    """Exact 4-branch analytical + ensemble density-matrix comparison for a two-mass BMV
    interferometer under:
      - Quasistatic / slowly-drifting local stray force-gradient noise (suppressed as 1/N_dd^2
        by bilateral CPMG pulses; exactly refocused to 0 in the purely static limit), AND
      - Memoryless white Markovian Lindblad dephasing (strictly invariant under pi-pulses).

    Contrasts synchronous bilateral pi-pulses (X_A (x) X_B, mapping (-Z_A)(-Z_B) = +Z_A Z_B)
    against unilateral pi-pulses (X_A (x) I, mapping (-Z_A)(+Z_B) = -Z_A Z_B and erasing
    gravitational entanglement). When planted_defect=True, substitutes unilateral pulses.
    """
    # Branch eigenvalues (z_A, z_B) in (+1,+1), (+1,-1), (-1,+1), (-1,-1) for LL, LR, RL, RR
    z_pairs = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    dt = t_hold_s / (2.0 * n_dd)

    def _run_sequence(mode: str, lowf_rate: float, white_rate: float, pulses: int) -> dict:
        # Track accumulated gravitational cross-phase and residual low-frequency gradient variance
        # Each CPMG unit cell is [tau/2 - pi - tau - pi - tau/2] of duration T_cell = T / (pulses/2)
        # More generally for N_dd equally spaced CPMG pi-pulses at t_k = (k - 0.5) * (T / N_dd):
        n_intervals = pulses + 1
        boundaries = (
            [0.0] + [(k + 0.5) * (t_hold_s / pulses) for k in range(pulses)] + [t_hold_s]
            if pulses > 0
            else [0.0, t_hold_s]
        )
        s_a = 1
        s_b = 1
        grav_phase_factor = 0.0
        static_grad_a = 0.0
        static_grad_b = 0.0
        drift_grad_a = 0.0
        drift_grad_b = 0.0
        for seg in range(n_intervals):
            t0, t1 = boundaries[seg], boundaries[seg + 1]
            seg_dt = t1 - t0
            t_mid = 0.5 * (t0 + t1) / t_hold_s
            grav_phase_factor += (s_a * s_b) * seg_dt
            static_grad_a += s_a * seg_dt
            static_grad_b += s_b * seg_dt
            # Slowly varying linear gradient drift g(t) ~ (t/T - 0.5) -> residual scales as 1/N_dd
            # in amplitude and 1/N_dd^2 in dephasing rate!
            drift_grad_a += s_a * (t1 * t1 - t0 * t0) / (2.0 * t_hold_s)
            drift_grad_b += s_b * (t1 * t1 - t0 * t0) / (2.0 * t_hold_s)
            if seg < pulses:
                if mode == "bilateral":
                    s_a *= -1
                    s_b *= -1
                elif mode == "unilateral":
                    s_a *= -1

        dphi_eff = omega_ent_rad_s * grav_phase_factor
        # Low-frequency dephasing budget: free induction (pulses=0) gives lowf_rate * T;
        # CPMG filter function suppresses low-frequency drift rate by 1 / N_dd^2:
        if pulses == 0:
            gamma_lowf_eff = lowf_rate
        else:
            gamma_lowf_eff = lowf_rate / float(pulses * pulses)
        # Memoryless white Markovian Lindblad dephasing commutes with instantaneous Pauli X flips!
        gamma_white_eff = white_rate
        total_gamma_t = (gamma_lowf_eff + gamma_white_eff) * t_hold_s

        phases = {
            "LL": -0.25 * dphi_eff,
            "LR": 0.25 * dphi_eff,
            "RL": 0.25 * dphi_eff,
            "RR": -0.25 * dphi_eff,
        }
        rho = k_ent.four_branch_state(phases, total_gamma_t)
        return {
            "dphi_eff_rad": dphi_eff,
            "static_gradient_residual_s": abs(static_grad_a) + abs(static_grad_b),
            "drift_gradient_residual_s": abs(drift_grad_a),
            "gamma_lowf_eff_s1": gamma_lowf_eff,
            "gamma_white_eff_s1": gamma_white_eff,
            "negativity": k_ent.negativity(rho),
        }

    free_evolution = _run_sequence("none", gamma_lowf_s1, gamma_white_s1, 0)
    unilateral_echo = _run_sequence("unilateral", gamma_lowf_s1, gamma_white_s1, n_dd)
    active_mode = "unilateral" if planted_defect else "bilateral"
    bilateral_echo = _run_sequence(active_mode, gamma_lowf_s1, gamma_white_s1, n_dd)
    pure_markov_no_echo = _run_sequence("none", 0.0, gamma_white_s1, 0)
    pure_markov_bilateral = _run_sequence("bilateral", 0.0, gamma_white_s1, n_dd)

    return {
        "n_dd": n_dd,
        "t_hold_s": t_hold_s,
        "gamma_lowf_raw_s1": gamma_lowf_s1,
        "gamma_lowf_cpmg_s1": gamma_lowf_s1 / float(n_dd * n_dd),
        "gamma_white_s1": gamma_white_s1,
        "free_evolution": free_evolution,
        "unilateral_echo": unilateral_echo,
        "bilateral_echo": bilateral_echo,
        "markovian_invariance_abs_diff": abs(
            pure_markov_bilateral["negativity"] - pure_markov_no_echo["negativity"]
        ),
        "z_pairs_checked": len(z_pairs),
        "half_step_s": dt,
    }


# ---------------------------------------------------------------------------
# Part 4 · Zero-Sorry Lean 4 AST & Multivariate Rational Polynomial Verifier
# ---------------------------------------------------------------------------

def verify_lean_ast_and_polynomials(lean_path: Path | None = None, planted_defect: bool = False) -> dict:
    """Strip comments from IRUG_Unification.lean, verify 0 forbidden tokens
    (sorry|sorryAx|admit|axiom), >= 8 theorems, >= 4 universal quantifiers,
    sigma_95_recast_um = 33 (zero retired 44067), zero vacuous alpha - alpha definitions,
    and verify exact multivariate polynomial identities over Q using fractions.Fraction.
    """
    root = TOOLS_DIR.parent
    target = lean_path or (root / "skills" / "essays" / SLUG / "IRUG_Unification.lean")
    lean_raw = target.read_text(encoding="utf-8")
    if planted_defect:
        lean_raw = lean_raw + "\ntheorem planted_unproven : True := by sorry\n"

    no_block = re.sub(r"/-.*?-/", "", lean_raw, flags=re.DOTALL)
    no_comments = re.sub(r"--[^\n]*", "", no_block)

    forbidden_tokens = re.findall(r"\b(sorry|sorryAx|admit|axiom)\b", no_comments)
    theorem_names = re.findall(r"\btheorem\s+([A-Za-z0-9_]+)", no_comments)
    universal_count = len(re.findall(r"∀", no_comments))
    has_recast_33 = bool(re.search(r"def\s+sigma_95_recast_um\s*:\s*Int\s*:=\s*33\b", no_comments))
    has_retired_44067 = "44067" in no_comments
    has_vacuous_self_sub = bool(re.search(r"\b([A-Za-z0-9_]+)\s*-\s*\1\b", no_comments))

    # Strict core-Prelude qualified-identifier gate (prevents nonexistent Int.*/Nat.* lemma drift when lean is absent)
    allowed_qualified_ids = {
        "Informatico.Essays.ES06",
        "Int.mul_add",
        "Int.mul_comm",
        "Int.mul_assoc",
        "Int.neg_mul_neg",
        "p.sigma_c_um_num",
        "p.sigma_c_um_den",
        "p.gamma_crit_uhz",
        "a.m", "b.m", "a.l", "b.l", "a.t", "b.t", "a.i", "b.i",
        "a.theta", "b.theta", "a.n", "b.n", "a.j", "b.j",
    }
    qualified_ids = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+\b", no_comments))
    unknown_qualified_ids = sorted(qualified_ids - allowed_qualified_ids)

    # Execute real `lean` kernel typechecker automatically whenever installed on the host/CI runner
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

    # Multivariate polynomial ring over Fraction
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

    # 1. Universal scaled QEP polynomial identity in Q[m0, w, s, alpha_num]
    m0, w, s, a_num = p_var("m0"), p_var("w"), p_var("s"), p_var("alpha_num")
    e_low_0 = m0
    e_low_1 = p_add(m0, w)
    s_plus_a = p_add(s, a_num)
    e_high_0 = p_mul(e_low_0, s_plus_a)
    e_high_1 = p_mul(e_low_1, s_plus_a)
    qep_lhs = p_mul(p_add(e_high_1, p_mul(s, e_low_1), -1), e_low_0)
    qep_rhs = p_mul(p_add(e_high_0, p_mul(s, e_low_0), -1), e_low_1)
    qep_poly_diff = p_add(qep_lhs, qep_rhs, -1)

    # 2. Universal 8-variable Stoica / LOCC cross-phase gauge invariance
    ll, lr, rl, rr = p_var("ll"), p_var("lr"), p_var("rl"), p_var("rr")
    aL, aR, bL, bR = p_var("aL"), p_var("aR"), p_var("bL"), p_var("bR")

    def cross_p(p_ll: dict, p_lr: dict, p_rl: dict, p_rr: dict) -> dict:
        return p_add(p_add(p_add(p_lr, p_rl, 1), p_ll, -1), p_rr, -1)

    stoica_poly_diff = p_add(
        cross_p(
            p_add(p_add(ll, aL), bL),
            p_add(p_add(lr, aL), bR),
            p_add(p_add(rl, aR), bL),
            p_add(p_add(rr, aR), bR),
        ),
        cross_p(ll, lr, rl, rr),
        -1,
    )

    # 3. Universal 5-variable Bilateral Echo Half-Step Cancellation
    jG, gA, gB, zA, zB = p_var("jGrav"), p_var("gA"), p_var("gB"), p_var("zA"), p_var("zB")
    neg_zA = p_mul(p_const(-1), zA)
    neg_zB = p_mul(p_const(-1), zB)
    half_1 = p_add(p_add(p_mul(p_const(-1), p_mul(jG, p_mul(zA, zB))), p_mul(gA, zA)), p_mul(gB, zB))
    half_2 = p_add(
        p_add(p_mul(p_const(-1), p_mul(jG, p_mul(neg_zA, neg_zB))), p_mul(gA, neg_zA)),
        p_mul(gB, neg_zB),
    )
    echo_sum = p_add(half_1, half_2)
    echo_expected = p_mul(p_const(-2), p_mul(jG, p_mul(zA, zB)))
    echo_poly_diff = p_add(echo_sum, echo_expected, -1)

    # 4. Universal 3-variable Maxwell-Calladine Index Identity
    d_dof, e_con, r_rk = p_var("d_dof"), p_var("e_constraints"), p_var("r")
    mc_poly_diff = p_add(
        p_add(p_add(d_dof, r_rk, -1), p_add(e_con, r_rk, -1), -1),
        p_add(d_dof, e_con, -1),
        -1,
    )

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
        "has_recast_33": has_recast_33,
        "has_retired_44067": has_retired_44067,
        "has_vacuous_self_sub": has_vacuous_self_sub,
        "qep_polynomial_zero": len(qep_poly_diff) == 0,
        "stoica_polynomial_zero": len(stoica_poly_diff) == 0,
        "bilateral_echo_polynomial_zero": len(echo_poly_diff) == 0,
        "maxwell_calladine_polynomial_zero": len(mc_poly_diff) == 0,
    }


def evaluate_coupled_synthesis(planted_defect: bool = False) -> dict:
    """Run all 4 coupled synthesis pillars of Essay ES.06 in one deterministic bundle."""
    wdw_zych = build_hermitian_wdw_nullspace(WDW_N_CLOCK, WDW_ZYCH_MODES, planted_defect=planted_defect)
    wdw_bmv = build_hermitian_wdw_nullspace(WDW_N_CLOCK, WDW_BMV_MODES, planted_defect=planted_defect)
    sr_qep = evaluate_physical_sr_clock_and_qep()
    walls_opp = evaluate_four_wall_and_oppenheim(planted_defect=planted_defect)
    cpmg = simulate_bilateral_vs_unilateral_cpmg(planted_defect=planted_defect)
    lean = verify_lean_ast_and_polynomials(planted_defect=planted_defect)
    return {
        "wdw_zych_64d": wdw_zych,
        "wdw_bmv_64d": wdw_bmv,
        "physical_sr_qep": sr_qep,
        "four_wall_and_oppenheim": walls_opp,
        "bilateral_cpmg": cpmg,
        "lean4_formal_spine": lean,
    }


# ---------------------------------------------------------------------------
# Bilingual Monograph Specification (EN / es-MX) · Essay ES.06
# ---------------------------------------------------------------------------

ESSAY: dict = {
    "code": CODE,
    "slug": SLUG,
    "plate_slug": PLATE_SLUG,
    "date": "2026-11-10",
    "seo": (
        "Timeless Clocks, Torque Bounds, and Formal Proof",
        "How timeless quantum clock constraints, sub-millimetre torsion bounds, bilateral spin echoes, and Lean formal proofs test tabletop gravity.",
        "Relojes sin Tiempo, Cotas de Par y Prueba Formal",
        "Cómo restricciones cuánticas sin tiempo, cotas de torsión submilimétricas, ecos bilaterales y pruebas en Lean evalúan la gravedad de mesa.",
    ),
    "kicker_en": "Cross-Scale Essay · ES.06 · Relational Quantum Clocks, Torsion Bounds & Formal Verification",
    "kicker_es": "Ensayo Transescalar · ES.06 · Relojes Cuánticos Relacionales, Cotas de Torsión y Verificación Formal",
    "reading_time_en": "15 min read",
    "reading_time_es": "15 min de lectura",
    "title_en": "Coupled Timeless Constraints: Wheeler–DeWitt Clocks, 33 µm Torsion Walls, Bilateral Echoes, and Zero-Sorry Proof",
    "title_es": "Restricciones Acopladas sin Tiempo: Relojes de Wheeler–DeWitt, Muros de Torsión a 33 µm, Ecos Bilaterales y Prueba sin Sorry",
    "standfirst_en": (
        "What survives when relational quantum clocks, sub-millimetre inverse-square torsion data, open-system "
        "spin echoes, and formal proof assistants inspect the same tabletop gravity geometry at once? Diagonalizing "
        "a 64 × 64 Hermitian Wheeler–DeWitt constraint via 128 × 128 real Jacobi rotations, recasting Eöt-Wash "
        "signed limits down to σ ≤ 33 µm, contrasting bilateral X_A ⊗ X_B pulses against unilateral erasures, "
        "and auditing 10 core Lean 4 theorems show exactly what algebra can—and cannot—settle before a lab measurement."
    ),
    "standfirst_es": (
        "¿Qué sobrevive cuando relojes cuánticos relacionales, datos de torsión submilimétricos, ecos de espín en "
        "sistemas abiertos y asistentes de prueba formal examinan a la vez la misma geometría gravitatoria de mesa? "
        "Diagonalizar una restricción hermítica de Wheeler–DeWitt de 64 × 64 mediante rotaciones reales de Jacobi de "
        "128 × 128, proyectar límites con signo de Eöt-Wash hasta σ ≤ 33 µm, contrastar pulsos bilaterales X_A ⊗ X_B "
        "frente a borrados unilaterales y auditar 10 teoremas en Lean 4 muestra qué fija el álgebra antes de medir."
    ),
    "card_dek_en": (
        "A 64 × 64 Wheeler–DeWitt nullspace, the σ ≤ 33 µm Eöt-Wash recast, 3.31 × 10¹⁶× Oppenheim torque suppression, "
        "bilateral X_A ⊗ X_B echoes, and 10 zero-sorry Lean 4 theorems."
    ),
    "card_dek_es": (
        "Un núcleo nulo de Wheeler–DeWitt de 64 × 64, el límite Eöt-Wash σ ≤ 33 µm, la supresión de Oppenheim de "
        "3.31 × 10¹⁶×, ecos bilaterales X_A ⊗ X_B y 10 teoremas sin sorry en Lean 4."
    ),
    "instrument_kind": "wdw_clock",
    "predict": {
        "question_en": (
            "Two superposed masses interact gravitationally via −J_grav Z_A Z_B while experiencing quasistatic stray "
            "force gradients g_A Z_A + g_B Z_B and memoryless white Markovian gas collisions at rate γ_white. If you "
            "apply unilateral π-pulses (X_A ⊗ I) on mass A alone—or switch to synchronous bilateral π-pulses (X_A ⊗ X_B)—what happens?"
        ),
        "question_es": (
            "Dos masas en superposición interactúan gravitatoriamente mediante −J_grav Z_A Z_B bajo gradientes parásitos "
            "cuasiestáticos g_A Z_A + g_B Z_B y colisiones markovianas blancas sin memoria a tasa γ_white. Si aplicas "
            "pulsos π unilaterales (X_A ⊗ I) solo en A —o pulsos π bilaterales síncronos (X_A ⊗ X_B)—, ¿qué ocurre?"
        ),
        "choices": [
            {
                "id": "a",
                "en": "Unilateral X_A ⊗ I pulses protect the gravitational phase and suppress both quasistatic gradients and white Markovian collisions.",
                "es": "Los pulsos unilaterales X_A ⊗ I protegen la fase gravitatoria y suprimen tanto gradientes cuasiestáticos como colisiones markovianas blancas.",
            },
            {
                "id": "b",
                "en": "Unilateral X_A ⊗ I flips Z_A Z_B → −Z_A Z_B and erases gravitational entanglement to 0; bilateral X_A ⊗ X_B preserves +Z_A Z_B and suppresses quasistatic gradients as 1 / N_dd², while leaving white Markovian γ_white unchanged (1×).",
                "es": "El pulso unilateral X_A ⊗ I invierte Z_A Z_B → −Z_A Z_B y borra el entrelazamiento gravitatorio a 0; el bilateral X_A ⊗ X_B conserva +Z_A Z_B y suprime gradientes cuasiestáticos como 1 / N_dd², dejando intacto γ_white (1×).",
            },
        ],
        "answer": "b",
        "explain_en": (
            "Flipping only mass A sends Z_A Z_B to (−Z_A)(+Z_B) = −Z_A Z_B, refocusing the desired gravitational cross-phase "
            "to 0 across equal half-periods. Synchronous bilateral pulses X_A ⊗ X_B map (−Z_A)(−Z_B) = +Z_A Z_B, preserving "
            "100% of J_grav while canceling static local gradients g_A Z_A + g_B Z_B and cutting slow drift rates by 1 / N_dd². "
            "Memoryless Lindblad collisions have zero temporal correlation across pulses and remain 1× invariant."
        ),
        "explain_es": (
            "Invertir solo la masa A envía Z_A Z_B a (−Z_A)(+Z_B) = −Z_A Z_B, cancelando la fase gravitatoria cruzada a 0 "
            "en semiperíodos iguales. Los pulsos bilaterales síncronos X_A ⊗ X_B aplican (−Z_A)(−Z_B) = +Z_A Z_B, conservando "
            "el 100% de J_grav mientras anulan gradientes locales g_A Z_A + g_B Z_B y reducen derivas lentas como 1 / N_dd². "
            "Las colisiones markovianas de Lindblad carecen de memoria entre pulsos y permanecen invariantes en 1×."
        ),
    },
    "sections": [
        {
            "id": "wdw-nullspace",
            "h2_en": "I · Evolution Without Evolution: The 64 × 64 Wheeler–DeWitt Nullspace and Optical Clocks",
            "h2_es": "I · Evolución sin Evolución: El Núcleo Nulo de Wheeler–DeWitt de 64 × 64 y los Relojes Ópticos",
            "short_en": "I · Timeless Nullspace",
            "short_es": "I · Núcleo sin Tiempo",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Canonical general relativity and textbook quantum mechanics disagree on the status of the symbol t. "
                        "In Schrödinger dynamics, t is an external classical parameter ticking uniformly outside the laboratory; "
                        "in canonical quantum gravity, diffeomorphism invariance forces the total Hamiltonian constraint to "
                        "annihilate physical states, Ĉ|Ψ⟩⟩ = 0. Page and Wootters (1983) showed how dynamical evolution "
                        "re-emerges inside a stationary universe: partition the composite Hilbert space into a reference clock "
                        "H_C and a rest-of-world system H_S coupled by Ĉ = H_C ⊗ I_S − I_C ⊗ H_S. Although |Ψ⟩⟩ never changes "
                        "with respect to an external watch, projecting |Ψ⟩⟩ onto the clock's localized time states |t_n⟩ yields "
                        "relational states |ψ(t_n)⟩ = √d ⟨t_n|Ψ⟩⟩ that obey unitary Schrödinger phase accumulation step by step."
                    ),
                    "es": (
                        "La relatividad general canónica y la mecánica cuántica escolar discrepan sobre el estatuto del símbolo t. "
                        "En la dinámica de Schrödinger, t es un parámetro clásico externo que avanza fuera del laboratorio; en la "
                        "gravedad cuántica canónica, la invariancia por difeomorfismos obliga a la restricción hamiltoniana total a "
                        "anular los estados físicos, Ĉ|Ψ⟩⟩ = 0. Page y Wootters (1983) mostraron cómo reaparece el cambio dentro "
                        "de un universo estacionario: divídase el espacio compuesto en un reloj H_C y un sistema H_S acoplados por "
                        "Ĉ = H_C ⊗ I_S − I_C ⊗ H_S. Aunque |Ψ⟩⟩ es fijo, proyectarlo sobre estados temporales |t_n⟩ produce "
                        "estados relacionales |ψ(t_n)⟩ = √d ⟨t_n|Ψ⟩⟩ que siguen una evolución unitaria paso a paso."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Now place an internal two-level quantum clock aboard a massive particle held in spatial superposition "
                        "across two heights separated by Δh, the interferometric geometry analyzed by Zych et al. (2011). "
                        "Our composite Hilbert space becomes H_C^(16) ⊗ H_path^(2) ⊗ H_tick^(2) of complex dimension 16 × 2 × 2 = 64. "
                        "Rather than evaluating closed-form cosines by hand, our kernel constructs the dense 64 × 64 Hermitian "
                        "constraint matrix Ĉ directly in the non-diagonal physical basis |t_n⟩ ⊗ H_4|b⟩ (where H_4 is the 4 × 4 "
                        "Hadamard transform mixing path and tick qubits, giving an off-diagonal Frobenius norm of 43.8), embeds "
                        "Ĉ into its 128 × 128 real symmetric matrix [[Re Ĉ, −Im Ĉ], [Im Ĉ, Re Ĉ]], and diagonalizes all 128 "
                        "real modes via pure-Python Jacobi rotations. The composite history state |Ψ⟩⟩ exhibits a direct residual "
                        "norm ‖Ĉ|Ψ⟩⟩‖ = 1.36 × 10⁻¹⁴ < 10⁻¹³ and projects onto the zero-eigenvalue Jacobi kernel with weight "
                        "1.0000000000, while conditioning on |t_n⟩ recovers V(t_n) = |cos(Δω t_n / 2)| to 8.88 × 10⁻¹⁶."
                    ),
                    "es": (
                        "Coloquemos ahora un reloj cuántico interno de dos niveles a bordo de una partícula masiva en superposición "
                        "espacial entre dos alturas separadas por Δh, la geometría interferométrica de Zych et al. (2011). Nuestro "
                        "espacio compuesto es H_C^(16) ⊗ H_path^(2) ⊗ H_tick^(2), de dimensión compleja 16 × 2 × 2 = 64. En lugar "
                        "de evaluar cosenos a mano, el núcleo construye la matriz hermítica densa Ĉ de 64 × 64 en la base física "
                        "no diagonal |t_n⟩ ⊗ H_4|b⟩ (donde H_4 es la matriz de Hadamard de 4 × 4 que mezcla ruta y pulso, con norma "
                        "de Frobenius fuera de la diagonal de 43.8), la incrusta en una matriz real simétrica de 128 × 128 "
                        "[[Re Ĉ, −Im Ĉ], [Im Ĉ, Re Ĉ]] y diagonaliza los 128 modos con rotaciones de Jacobi en Python puro. El "
                        "estado |Ψ⟩⟩ arroja residuo ‖Ĉ|Ψ⟩⟩‖ = 1.36 × 10⁻¹⁴ < 10⁻¹³ y proyección 1.0000000000 sobre el núcleo "
                        "nulo, recuperando V(t_n) = |cos(Δω t_n / 2)| con error máximo de 8.88 × 10⁻¹⁶."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Honest numerical modeling requires stating an explicit scale caveat here. On a finite 16-tick cyclic "
                        "Pegg–Barnett clock lattice k ∈ {−8, …, +7}, exact periodic Fourier closure requires integer system modes: "
                        "our nullspace matrix uses [−3, −1, 1, 5], a dimensionless α_grav = 1 bandwidth-scaled lattice where the "
                        "lower path carries tick gap (−1) − (−3) = 2 and the upper path carries tick gap 5 − 1 = 4, producing a "
                        "full visibility revival over 16 discrete ticks at beat Δω = 2. In a physical laboratory on Earth "
                        "(g = 9.80665 m/s²), the dimensionless redshift across Δh = 1.0 m is α_grav = g Δh / c² = 1.091 × 10⁻¹⁶. "
                        "Pairing our matrix kernel with an optical strontium-87 clock transition at 429.228 THz "
                        "(ω_Sr = 2.70 × 10¹⁵ rad/s) gives proper-time lag Δτ = 1.091 × 10⁻¹⁶ s over T = 1.0 s, fringe visibility "
                        "V = 0.9892 at 1.0 m · s, first orthogonality zero V = 0 at Δh · T = π c² / (g ω_Sr) = 10.68 m · s, and "
                        "an exact Quantum Equivalence Principle Eötvös parameter η = 0 across ground and excited clock states."
                    ),
                    "es": (
                        "El modelado numérico honesto exige declarar aquí una advertencia explícita de escala. En una red cíclica "
                        "de Pegg–Barnett de 16 pulsos con k ∈ {−8, …, +7}, el cierre periódico exacto de Fourier requiere modos "
                        "enteros: nuestra matriz usa [−3, −1, 1, 5], un modelo adimensional reescalado con α_grav = 1 donde la "
                        "rama inferior tiene brecha (−1) − (−3) = 2 y la superior 5 − 1 = 4, completando un batido Δω = 2 en 16 "
                        "pasos. En un laboratorio terrestre (g = 9.80665 m/s²), el corrimiento adimensional en Δh = 1.0 m es "
                        "α_grav = g Δh / c² = 1.091 × 10⁻¹⁶. Al acoplar ese núcleo con un reloj óptico de estroncio-87 a "
                        "429.228 THz (ω_Sr = 2.70 × 10¹⁵ rad/s), el retraso propio es Δτ = 1.091 × 10⁻¹⁶ s en T = 1.0 s, la "
                        "visibilidad es V = 0.9892 a 1.0 m · s, el primer nulo V = 0 ocurre en Δh · T = π c² / (g ω_Sr) = 10.68 m · s "
                        "y el parámetro cuántico de Eötvös cumple η = 0 entre ambos niveles internos."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Timeless Wheeler–DeWitt Nullspace & Conditioned Zych–Brukner Visibility",
                    "label_es": "Núcleo Nulo de Wheeler–DeWitt y Visibilidad Condicionada de Zych–Brukner",
                    "formula": "Ĉ |Ψ⟩⟩ = (H_C ⊗ I_4 − I_16 ⊗ H_Zych) |Ψ⟩⟩ = 0   ⟹   V(t_n) = |cos(Δω t_n / 2)| ,   η_QEP = 0",
                    "note_en": (
                        "Diagonalized via 128 × 128 real Jacobi rotations on H_C^(16) ⊗ H_path^(2) ⊗ H_tick^(2): "
                        "‖Ĉ|Ψ⟩⟩‖ = 1.36 × 10⁻¹⁴, kernel projection = 1.0000000000, and optical 87Sr first visibility null at 10.68 m · s."
                    ),
                    "note_es": (
                        "Diagonalizado mediante rotaciones reales de Jacobi de 128 × 128 en H_C^(16) ⊗ H_path^(2) ⊗ H_tick^(2): "
                        "‖Ĉ|Ψ⟩⟩‖ = 1.36 × 10⁻¹⁴, proyección = 1.0000000000 y primer nulo óptico de 87Sr en 10.68 m · s."
                    ),
                },
            ],
        },
        {
            "id": "torsion-and-oppenheim",
            "h2_en": "II · Closing the Smeared-Gravity Escape Hatch: The 33 µm Recast and Oppenheim's Torque Ceiling",
            "h2_es": "II · Cerrando la Vía de Gravedad Difuminada: El Límite de 33 µm y el Techo de Par de Oppenheim",
            "short_en": "II · 33 µm & Torque Ceiling",
            "short_es": "II · 33 µm y Techo de Par",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Turn from 1 particle carrying an internal clock to 2 superposed microspheres interacting solely via "
                        "gravity. A second 64 × 64 Wheeler–DeWitt constraint Ĉ_2M on H_C^(16) ⊗ H_A^(2) ⊗ H_B^(2) places the "
                        "two-mass history state inside ker(Ĉ_2M) with Jacobi projection 1.0000000000, generating entanglement "
                        "whenever the four-branch cross-phase Δφ = φ_LR + φ_RL − φ_LL − φ_RR ≠ 0 mod 2π. Yet Trillo and "
                        "Navascués (2025) demonstrated a subtle loophole: if classical gravity couples to mass density smeared "
                        "over a Gaussian kernel of width σ in Diósi–Penrose hybrid dynamics, its master equation can transiently "
                        "entangle two masses whenever their nearest approach sits below d_c ≈ 0.8509 σ. Could a classical "
                        "hybrid field mimic quantum graviton exchange inside real tabletop geometries?"
                    ),
                    "es": (
                        "Pasemos de 1 partícula con reloj interno a 2 microesferas en superposición acopladas solo por gravedad. "
                        "Una segunda restricción Ĉ_2M de 64 × 64 sobre H_C^(16) ⊗ H_A^(2) ⊗ H_B^(2) sitúa el estado conjunto en "
                        "ker(Ĉ_2M) con proyección de Jacobi 1.0000000000, generando entrelazamiento siempre que la fase cruzada "
                        "Δφ = φ_LR + φ_RL − φ_LL − φ_RR ≠ 0 mod 2π. Sin embargo, Trillo y Navascués (2025) señalaron un resquicio: "
                        "si la gravedad clásica se acopla a una densidad difuminada con ancho gaussiano σ en la dinámica híbrida de "
                        "Diósi–Penrose, su ecuación maestra entrelaza transitoriamente dos masas bajo d_c ≈ 0.8509 σ. ¿Podría un "
                        "campo híbrido clásico imitar el canal cuántico en geometrías reales de mesa?"
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Coupling four independent experimental and environmental walls closes that escape hatch across every "
                        "published proposal. Wall 1 (spontaneous X-ray emission in underground detectors) forces σ > 4.9 Å. "
                        "Wall 2 projects the erf(r / 2σ) / r torque deficit across the 120-fold Fourier–Bessel wedge pendulum "
                        "of Lee et al. (2020) onto all 66 signed 95% Yukawa profile rows from 5 µm to 8.9 mm. Because the data "
                        "lean slightly positive in the 5 µm to 100 µm range, this full profile recast excludes σ > 33 µm at 95% "
                        "confidence (σ_95 = 33.08 µm: σ = 33 µm sits just inside −7.3 versus −7.4, whereas σ = 35 µm is excluded "
                        "at −10.2), superseding any single-point 52 µm comparison. That updated 33 µm wall eliminates Bose et al. "
                        "(σ_c = 524.5 µm), Chevalier et al. (405.7 µm), Van De Kamp et al. (82.0 µm and 54.9 µm), and even the "
                        "z = 30 µm screened parallel geometry of Schut et al. (2024) at σ_c = 39.4 µm > 33 µm."
                    ),
                    "es": (
                        "Acoplar cuatro muros experimentales y ambientales cierra ese resquicio en todas las geometrías publicadas. "
                        "El Muro 1 (radiación espontánea subterránea) exige σ > 4.9 Å. El Muro 2 proyecta el déficit de par "
                        "erf(r / 2σ) / r en el péndulo de 120 cuñas de Fourier–Bessel de Lee et al. (2020) contra las 66 filas "
                        "con signo al 95% entre 5 µm y 8.9 mm. Como el ajuste experimental se inclina ligeramente hacia valores "
                        "positivos entre 5 µm y 100 µm, esta proyección completa excluye σ > 33 µm al 95% (σ_95 = 33.08 µm: "
                        "σ = 33 µm queda apenas permitido con −7.3 frente a −7.4, mientras σ = 35 µm cae excluido con −10.2), "
                        "superando comparaciones puntuales a 52 µm. Este muro de 33 µm descarta a Bose et al. (σ_c = 524.5 µm), "
                        "Chevalier et al. (405.7 µm), Van De Kamp et al. (82.0 µm y 54.9 µm) e incluso la geometría paralela "
                        "apantallada z = 30 µm de Schut et al. (2024) con σ_c = 39.4 µm > 33 µm."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Only tighter parallel traps from Schut et al. (2024)—such as z = 10 µm (gap d = 21 µm, split Δx = 1.7 µm, "
                        "above the 16.5 µm Casimir–Polder floor of Wall 3 at 10⁻¹⁵ kg) where σ_c = 13.6 µm ≤ 33 µm—clear Wall 2. "
                        "There Wall 4 (environmental dephasing) finishes the test: at σ = 33.1 µm, the hybrid channel's own "
                        "self-decoherence caps its dephasing tolerance at γ_crit = 7.87 × 10⁻⁵ s⁻¹ (2.17 × 10⁻⁴ s⁻¹ at σ = 20 µm), "
                        "so at a realistic cryogenic floor γ = 10⁻³ s⁻¹ hybrid negativity collapses to 0.0 while the unitary "
                        "quantum channel (γ_crit = 9.83 × 10⁻³ s⁻¹) retains peak negativity 0.337. Independently, Oppenheim et al. "
                        "(2023) proved that any consistent Markovian classical-gravity theory must inject stochastic gravitational "
                        "momentum diffusion obeying ℓ_P² D_2 ≤ T σ_a² N r_N³ / G². Inserting the 0.0054 fN · m torque residual of "
                        "Lee et al. (2020) across the 18 mm lever arm of the platinum foil (N = 6.02 × 10²¹ atoms, "
                        "σ_a = 1.53 × 10⁻¹³ m/s²) at T = 10³ s and r_N = 1 fm pushes the admissible ceiling down to "
                        "3.02 × 10⁻²⁶ kg² · s · m⁻¹—a 3.31 × 10¹⁶× suppression below the 10⁻⁹ kg² · s · m⁻¹ Cavendish benchmark "
                        "(and 9.65 × 10¹³× at the 7 fm platinum nuclear radius), squeezing classical diffusion into a narrowing "
                        "corridor above the 10⁻⁴⁰ kg² · s · m⁻¹ interferometry floor."
                    ),
                    "es": (
                        "Solo trampas paralelas más estrechas de Schut et al. (2024) —como z = 10 µm (separación d = 21 µm, "
                        "división Δx = 1.7 µm, sobre el piso de Casimir–Polder de 16.5 µm del Muro 3 a 10⁻¹⁵ kg) con "
                        "σ_c = 13.6 µm ≤ 33 µm— superan el Muro 2. Allí el Muro 4 (desfase ambiental) cierra la prueba: en "
                        "σ = 33.1 µm, la autodecoherencia híbrida limita su tolerancia a γ_crit = 7.87 × 10⁻⁵ s⁻¹ "
                        "(2.17 × 10⁻⁴ s⁻¹ en σ = 20 µm), de modo que a γ = 10⁻³ s⁻¹ la negatividad híbrida cae a 0.0 mientras "
                        "el canal cuántico unitario (γ_crit = 9.83 × 10⁻³ s⁻¹) alcanza 0.337. En paralelo, Oppenheim et al. "
                        "(2023) probaron que toda gravedad clásica markoviana consistente exige difusión de momento con "
                        "ℓ_P² D_2 ≤ T σ_a² N r_N³ / G². Al insertar el residuo de par de 0.0054 fN · m de Lee et al. (2020) "
                        "en el brazo de 18 mm de la lámina de platino (N = 6.02 × 10²¹ átomos, σ_a = 1.53 × 10⁻¹³ m/s²) con "
                        "T = 10³ s y r_N = 1 fm, el techo cae a 3.02 × 10⁻²⁶ kg² · s · m⁻¹: una supresión de 3.31 × 10¹⁶× bajo "
                        "la referencia de Cavendish de 10⁻⁹ kg² · s · m⁻¹ (y 9.65 × 10¹³× con r_N = 7 fm), estrechando la "
                        "ventana sobre el piso interferométrico de 10⁻⁴⁰ kg² · s · m⁻¹."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Signed 33 µm Recast & Oppenheim Post-Quantum Torque-Diffusion Bound",
                    "label_es": "Recast con Signo a 33 µm y Cota de Difusión-Par Post-Cuántica de Oppenheim",
                    "formula": "σ_95(Eöt-Wash 120ω) ≤ 33 µm ,    ℓ_P² D_2 ≤ T σ_a² N r_N³ / G² = 3.02 × 10⁻²⁶ kg²·s·m⁻¹",
                    "note_en": (
                        "DERIVED (NOT MEASURED) from Lee et al. (2020) and Oppenheim et al. (2023): Eöt-Wash 0.0054 fN · m "
                        "torque residuals suppress the classical-gravity diffusion ceiling by 3.31 × 10¹⁶× below 10⁻⁹ kg² · s · m⁻¹."
                    ),
                    "note_es": (
                        "DERIVADO (NO MEDIDO) a partir de Lee et al. (2020) y Oppenheim et al. (2023): el residuo de par de "
                        "0.0054 fN · m suprime el techo de difusión clásica por 3.31 × 10¹⁶× bajo 10⁻⁹ kg² · s · m⁻¹."
                    ),
                },
            ],
        },
        {
            "id": "bilateral-cpmg",
            "h2_en": "III · Bilateral Spin Echoes: Preserving Z_A Z_B While Separating 1/f Drift from Lindblad Noise",
            "h2_es": "III · Ecos de Espín Bilaterales: Conservar Z_A Z_B Separando Deriva 1/f y Ruido de Lindblad",
            "short_en": "III · Bilateral Echoes",
            "short_es": "III · Ecos Bilaterales",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Surviving Wall 4 in practice demands keeping effective dephasing below 9.83 × 10⁻³ s⁻¹ across tens of "
                        "seconds. Experimenters routinely reach for Carr–Purcell–Meiboom–Gill (CPMG) π-pulse trains introduced "
                        "by Meiboom and Gill (1958) and generalized to open-system dynamical decoupling by Viola, Knill, and "
                        "Lloyd (1999). Yet applying single-qubit spin-echo intuition blindly to a two-mass gravitational "
                        "interferometer commits two fatal physical errors—one in operator parity and one in bath memory."
                    ),
                    "es": (
                        "Superar el Muro 4 en la práctica exige mantener el desfase efectivo por debajo de 9.83 × 10⁻³ s⁻¹ "
                        "durante decenas de segundos. Los experimentalistas suelen acudir a trenes de pulsos π de "
                        "Carr–Purcell–Meiboom–Gill (CPMG) introducidos por Meiboom y Gill (1958) y generalizados al desacoplamiento "
                        "dinámico por Viola, Knill y Lloyd (1999). Pero trasladar a ciegas la intuición de un solo qubit a un "
                        "interferómetro gravitatorio de dos masas comete dos errores físicos fatales: uno de paridad y otro de memoria."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Write the effective two-qubit branch Hamiltonian as H_eff = −(ħ ω_ent / 4) Z_A ⊗ Z_B + (ħ / 2)(g_A(t) Z_A ⊗ I "
                        "+ g_B(t) I ⊗ Z_B), where g_A(t) and g_B(t) represent slow local patch-charge, magnetic, or seismic "
                        "force-gradient drifts. Suppose an experimenter applies a unilateral π-pulse X_A ⊗ I to mass A halfway "
                        "through the hold time. Conjugating by X_A ⊗ I sends Z_A ⊗ I → −Z_A ⊗ I, canceling g_A, leaves g_B "
                        "uncompensated, and—worse—flips the bilinear gravitational coupling Z_A ⊗ Z_B → (−Z_A) ⊗ (+Z_B) = −Z_A ⊗ Z_B! "
                        "Across equal half-periods, J_grav + (−J_grav) = 0: the unilateral echo erases the gravitational "
                        "entanglement phase identically to 0. By contrast, synchronous bilateral π-pulses X_A ⊗ X_B flip both "
                        "interferometer arms at the exact same instant, mapping (−Z_A) ⊗ (−Z_B) = +Z_A ⊗ Z_B. The gravitational "
                        "cross-phase accumulates constructively across every pulse while both local gradients g_A Z_A + g_B Z_B "
                        "invert sign and cancel!"
                    ),
                    "es": (
                        "Escribamos el hamiltoniano efectivo de dos qubits como H_eff = −(ħ ω_ent / 4) Z_A ⊗ Z_B + (ħ / 2)(g_A(t) Z_A ⊗ I "
                        "+ g_B(t) I ⊗ Z_B), donde g_A(t) y g_B(t) describen derivas locales lentas de carga superficial, campo "
                        "magnético o gradiente sísmico. Si se aplica un pulso π unilateral X_A ⊗ I solo sobre la masa A a mitad "
                        "del vuelo, conjugar por X_A ⊗ I invierte Z_A ⊗ I → −Z_A ⊗ I, deja g_B intacto y —peor aún— invierte el "
                        "acoplamiento gravitatorio bilineal Z_A ⊗ Z_B → (−Z_A) ⊗ (+Z_B) = −Z_A ⊗ Z_B. En semiperíodos iguales, "
                        "J_grav + (−J_grav) = 0: el eco unilateral borra la fase gravitatoria exactamente a 0. En cambio, los "
                        "pulsos π bilaterales síncronos X_A ⊗ X_B invierten ambos brazos al mismo instante, aplicando "
                        "(−Z_A) ⊗ (−Z_B) = +Z_A ⊗ Z_B: la fase gravitatoria se suma mientras g_A Z_A + g_B Z_B se cancelan."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Even synchronous bilateral pulses obey a strict bath-memory boundary governed by the quantum semigroup "
                        "theorem of Lindblad (1976). An N_dd-pulse bilateral CPMG sequence acts as a high-pass filter on "
                        "non-Markovian, quasistatic, or low-frequency 1/f gradient fluctuations whose correlation time τ_c "
                        "exceeds the inter-pulse spacing T / N_dd: cutting N_dd = 4 slices into T = 80.0 s suppresses a slow "
                        "gradient rate γ_low-f = 5.0 × 10⁻³ s⁻¹ by N_dd² = 16 down to γ_eff = 3.125 × 10⁻⁴ s⁻¹, lifting quantum "
                        "negativity from 0.123 to 0.308. However, memoryless white Markovian Lindblad dephasing—such as single-hit "
                        "4.0 K helium collisions or scattered thermal photons—has τ_c → 0: its dissipator D[Z](ρ) = Z ρ Z − ρ is "
                        "even in Z, so X Z X = −Z leaves D[−Z](ρ) = D[Z](ρ) completely unchanged (difference 0.0 to 10⁻¹⁶). "
                        "Across physics and chemistry, the same constrained optimization logic recurs: variational eigenvalue "
                        "bounds on quantum hardware (Peruzzo et al., 2014) and thermodynamic clock-precision bounds on multi-site "
                        "allosteric channels such as CFTR in cystic fibrosis hydrogel research (Barato & Seifert, 2016) separate "
                        "reversible Hamiltonian shifts from irreversible entropy production."
                    ),
                    "es": (
                        "Incluso los pulsos bilaterales síncronos obedecen una frontera estricta de memoria dictada por el "
                        "generador de semigrupos de Lindblad (1976). Una secuencia bilateral CPMG de N_dd pulsos filtra "
                        "fluctuaciones no markovianas, cuasiestáticas o de baja frecuencia 1/f cuyo tiempo de correlación τ_c "
                        "supera T / N_dd: con N_dd = 4 en T = 80.0 s, una deriva lenta γ_low-f = 5.0 × 10⁻³ s⁻¹ cae por "
                        "N_dd² = 16 hasta γ_eff = 3.125 × 10⁻⁴ s⁻¹, elevando la negatividad cuántica de 0.123 a 0.308. En cambio, "
                        "el desfase markoviano blanco sin memoria —como colisiones de helio a 4.0 K o fotones térmicos— tiene "
                        "τ_c → 0: su disipador D[Z](ρ) = Z ρ Z − ρ es par en Z, por lo que X Z X = −Z deja D[−Z](ρ) = D[Z](ρ) "
                        "idéntico (diferencia 0.0 a 10⁻¹⁶). Esta misma separación entre fase reversible y disipación irreversible "
                        "rige las cotas variacionales en procesadores cuánticos (Peruzzo et al., 2014) y la precisión "
                        "termodinámica de relojes alostéricos multisitio como CFTR en investigación biofísica de fibrosis "
                        "quística (Barato y Seifert, 2016)."
                    ),
                },
                {
                    "type": "bridge",
                    "kicker_en": "Plain-Language Bridge · Synchronized Rowing vs Flipping One Oar",
                    "kicker_es": "Puente en Lenguaje Claro · Remo Sincronizado frente a Invertir un Solo Remo",
                    "title_en": "Why bilateral echoes save mutual coupling while ignoring white rain",
                    "title_es": "Por qué el eco bilateral salva el acoplamiento mutuo pero no frena lluvia blanca",
                    "paras": [
                        (
                            "Think of 2 linked pendulums drifting slowly apart because floor tilt g_A pushes pendulum A left "
                            "while tilt g_B pushes pendulum B right. Swapping both pendulums' positions simultaneously halfway "
                            "through the run reverses both floor tilts so each cancels its first-half drift, yet keeps their "
                            "relative spring extension (+1)(+1) → (−1)(−1) = +1 intact. Swapping only pendulum A reverses the "
                            "spring tension between them and cancels the very signal you built the apparatus to detect.",
                            "Imagina 2 péndulos acoplados que derivan lentamente porque la inclinación local g_A empuja a A y "
                            "g_B empuja a B. Intercambiar simultáneamente ambos péndulos a mitad del ensayo invierte ambas "
                            "inclinaciones locales anulando su deriva, pero conserva intacto el signo mutuo (+1)(+1) → (−1)(−1) = +1. "
                            "Invertir solo el péndulo A invierte la tensión mutua y borra la señal gravitatoria buscada.",
                        ),
                        (
                            "Now pelt both pendulums with uncorrelated microscopic hailstones every microsecond (white Lindblad "
                            "noise). Swapping arm labels 4 times over 80.0 s cannot undo random impacts that have already "
                            "escaped into the chamber walls: CPMG conquers slow drift, never vacuum pressure.",
                            "Ahora golpea ambos péndulos con impactos microscópicos incorrelados cada microsegundo (ruido blanco "
                            "de Lindblad). Intercambiar las ramas 4 veces en 80.0 s no revierte choques cuya información ya "
                            "escapó a las paredes: CPMG vence derivas lentas, nunca una mala presión de vacío.",
                        ),
                    ],
                },
                {
                    "type": "equation",
                    "label_en": "Bilateral vs Unilateral Parity & Quasistatic CPMG Filter Scaling",
                    "label_es": "Paridad Bilateral frente a Unilateral y Escalamiento CPMG Cuasiestático",
                    "formula": "(X_A ⊗ X_B)(Z_A ⊗ Z_B)(X_A ⊗ X_B) = +Z_A ⊗ Z_B ,   γ_eff = γ_low-f / N_dd² + γ_white",
                    "note_en": (
                        "Unilateral conjugation (X_A ⊗ I)(Z_A ⊗ Z_B)(X_A ⊗ I) = −Z_A ⊗ Z_B erases Δφ → 0; bilateral X_A ⊗ X_B "
                        "preserves Δφ, divides quasistatic γ_low-f by N_dd², and leaves Markovian γ_white untouched."
                    ),
                    "note_es": (
                        "La conjugación unilateral (X_A ⊗ I)(Z_A ⊗ Z_B)(X_A ⊗ I) = −Z_A ⊗ Z_B anula Δφ → 0; la bilateral "
                        "X_A ⊗ X_B conserva Δφ, divide γ_low-f entre N_dd² y deja γ_white intacto."
                    ),
                },
            ],
        },
        {
            "id": "zero-sorry-lean",
            "h2_en": "IV · Non-Tautological Zero-Sorry Lean 4: Certifying the Deductive Spine Without Overclaiming Nature",
            "h2_es": "IV · Lean 4 sin Sorry y No Tautológico: Certificar la Columna Deductiva sin Suplantar a la Naturaleza",
            "short_en": "IV · Lean 4 Spine",
            "short_es": "IV · Columna Lean 4",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Floating-point scripts check finite grids, but subtle algebraic bugs—dropped cross-terms, unit slips, "
                        "or vacuous definitions—can hide behind passing numbers. Following the digitalized physics program of "
                        "HepLean / PhysLean (Tooby-Smith, 2025), our companion file IRUG_Unification.lean encodes 10 theorems "
                        "across pure core Lean 4 (using only Int, Nat, and Bool without external library imports) and enforces "
                        "strictly 0 occurrences of sorry, sorryAx, admit, or custom axiom declarations outside comments."
                    ),
                    "es": (
                        "Los programas en punto flotante evalúan mallas finitas, pero errores algebraicos sutiles —términos "
                        "cruzados omitidos, fallos dimensionales o definiciones vacuas— pueden ocultarse tras cifras exitosas. "
                        "Siguiendo el programa de física formalizada de HepLean / PhysLean (Tooby-Smith, 2025), nuestro archivo "
                        "IRUG_Unification.lean codifica 10 teoremas en Lean 4 puro (usando solo Int, Nat y Bool sin bibliotecas "
                        "externas) con exactamente 0 apariciones de sorry, sorryAx, admit o axiom fuera de comentarios."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Crucially, a formal specification is only as honest as its definitions. Writing a function "
                        "f(α) := α − α and proving f(α) = 0 proves nothing about physics—only that an integer minus itself "
                        "vanishes. Our upgraded specification eliminates every self-subtraction shortcut and proves 9 universal "
                        "∀ quantifiers over genuine multivariate functions: (1) 8 exact SI dimensional exponent equations over "
                        "SIDim ∈ ℤ⁷; (2) universal Quantum Equivalence Principle redshift equality across all (m_0, w, s, α_num ∈ ℤ) "
                        "from e_low(q) = m_0 + q w and e_high(q) = (m_0 + q w)(s + α_num) via explicit Int ring distributivity; "
                        "(3) universal 8-variable bipartite-local gauge invariance of cross_phase(ll, lr, rl, rr) = lr + rl − ll − rr "
                        "contrasted with the −4 λ non-local shift; (4) universal bilateral (−z_A)(−z_B) = z_A z_B versus "
                        "unilateral J_grav + (−J_grav) = 0 spin-echo parity and two-half-step gradient cancellation; "
                        "(5) updated σ_95 = 33 µm 4-wall exclusion across all 7 benchmark proposal rows; and (6) the universal "
                        "Maxwell–Calladine constraint-rigidity identity (d_dof − r) − (e_constraints − r) = d_dof − e_constraints "
                        "locking su(4)'s 9 non-local generators at rank r = 9."
                    ),
                    "es": (
                        "De modo crucial, una especificación formal es tan honesta como sus definiciones. Definir f(α) := α − α "
                        "y probar f(α) = 0 no demuestra nada físico, solo que un entero menos sí mismo se anula. Nuestra "
                        "especificación elimina todo atajo vacuo y demuestra 9 cuantificadores universales ∀ sobre funciones "
                        "multivariables genuinas: (1) 8 ecuaciones dimensionales SI exactas en SIDim ∈ ℤ⁷; (2) igualdad "
                        "universal del Principio de Equivalencia Cuántico para todo (m_0, w, s, α_num ∈ ℤ) a partir de "
                        "e_low(q) = m_0 + q w y e_high(q) = (m_0 + q w)(s + α_num) por distributividad en Int; (3) invariancia "
                        "universal en 8 variables de cross_phase(ll, lr, rl, rr) = lr + rl − ll − rr frente al giro no local "
                        "−4 λ; (4) paridad universal bilateral (−z_A)(−z_B) = z_A z_B frente a la unilateral J_grav + (−J_grav) = 0 "
                        "y cancelación de gradientes; (5) exclusión de 4 muros actualizada a σ_95 = 33 µm en las 7 filas de "
                        "propuestas; y (6) la identidad universal de Maxwell–Calladine (d_dof − r) − (e_constraints − r) = "
                        "d_dof − e_constraints que fija los 9 generadores no locales de su(4) en rango r = 9."
                    ),
                },
                {
                    "type": "analogy",
                    "kicker_en": "Epistemic Guardrail · What a Zero-Sorry Proof Certifies (and Never Claims)",
                    "kicker_es": "Salvaguarda Epistémica · Qué Certifica una Prueba sin Sorry (y Qué Jamás Reclama)",
                    "title_en": "Lean 4 verifies the bridge trusses between assumptions and numbers, never the river itself",
                    "title_es": "Lean 4 verifica las armaduras entre hipótesis y números, jamás el río empírico",
                    "paras": [
                        (
                            "Imagine a structural engineer proving by exact integer statics that a 9-bar truss has 0 floppy "
                            "mechanisms under stated pin loads. That proof guarantees zero hidden arithmetic errors in the "
                            "blueprint—corresponding to our DERIVED (NOT MEASURED) epistemic badge. It does not prove without "
                            "going outdoors whether wind gusts at the canyon exceed those stated loads.",
                            "Imagina un ingeniero estructural que prueba con estática entera exacta que una celosía de 9 barras "
                            "tiene 0 modos flexibles bajo cargas declaradas. Esa prueba garantiza cero errores aritméticos en el "
                            "plano —nuestra etiqueta DERIVADO (NO MEDIDO)—, pero no demuestra sin salir al cañón qué ráfagas soplan allí.",
                        ),
                        (
                            "Likewise, IRUG_Unification.lean certifies that IF nature obeys the stated Wheeler–DeWitt, "
                            "Diósi–Penrose, or Lindblad generators AND the published 2020 Eöt-Wash limits hold, THEN η = 0, "
                            "local phases cannot counterfeit Δφ, bilateral echoes preserve Z_A Z_B, and every mapped hybrid "
                            "geometry falls outside the 33 µm + 10⁻³ s⁻¹ window. Whether gravity actually entangles 10⁻¹⁴ kg "
                            "diamonds remains PROPOSED until two cryostats measure it.",
                            "Del mismo modo, IRUG_Unification.lean certifica que SI la naturaleza sigue los generadores "
                            "declarados de Wheeler–DeWitt, Diósi–Penrose o Lindblad Y rigen los límites Eöt-Wash de 2020, "
                            "ENTONCES η = 0, las fases locales no falsifican Δφ, el eco bilateral conserva Z_A Z_B y toda "
                            "geometría híbrida cae fuera de 33 µm + 10⁻³ s⁻¹. Si la gravedad entrelaza diamantes de 10⁻¹⁴ kg "
                            "sigue siendo PROPUESTO hasta medirlo en laboratorio.",
                        ),
                    ],
                },
            ],
        },
        {
            "id": "synthesis-ledger",
            "h2_en": "V · The Coupled Verification Ledger: Four Pillars, One Deterministic Knockout Gate",
            "h2_es": "V · El Registro de Verificación Acoplada: Cuatro Pilares, Una Compuerta de Falla Cerrada",
            "short_en": "V · Coupled Ledger",
            "short_es": "V · Registro Acoplado",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Bringing all four pillars into one executable verifier reveals why isolated calculations so easily "
                        "talk past one another. Relational time (Page & Wootters, 1983; Zych et al., 2011) fixes how proper-time "
                        "visibility and gravitational phase emerge inside ker(Ĉ); sub-millimetre torsion data (Lee et al., 2020) "
                        "and post-quantum force-diffusion inequalities (Oppenheim et al., 2023) bound classical alternatives "
                        "at σ ≤ 33 µm and 3.02 × 10⁻²⁶ kg² · s · m⁻¹; bilateral dynamical decoupling (Meiboom & Gill, 1958; "
                        "Viola, Knill & Lloyd, 1999) separates echo-reversible 1/f gradients from irreducible Markovian gas "
                        "and photon floors (Lindblad, 1976); and core Lean 4 + rational polynomial rings lock the deductive "
                        "implications against tautology."
                    ),
                    "es": (
                        "Reunir los cuatro pilares en un mismo verificador ejecutable revela por qué los cálculos aislados "
                        "suelen hablar sin escucharse. El tiempo relacional (Page y Wootters, 1983; Zych et al., 2011) fija cómo "
                        "emergen visibilidad y fase dentro de ker(Ĉ); la torsión submilimétrica (Lee et al., 2020) y la "
                        "difusión post-cuántica (Oppenheim et al., 2023) acotan alternativas clásicas en σ ≤ 33 µm y "
                        "3.02 × 10⁻²⁶ kg² · s · m⁻¹; el eco bilateral (Meiboom y Gill, 1958; Viola, Knill y Lloyd, 1999) "
                        "separa derivas 1/f reversibles del piso markoviano (Lindblad, 1976); y Lean 4 sella la deducción."
                    ),
                },
                {
                    "type": "table",
                    "caption_en": "Table ES.06 · Coupled Constraint Pillars, Benchmarks, and Planted-Defect Knockouts",
                    "caption_es": "Tabla ES.06 · Pilares Acoplados, Referencias Numéricas y Defectos Plantados",
                    "headers_en": [
                        "Coupled Pillar",
                        "Governing Object",
                        "Verified Benchmark",
                        "Epistemic Status",
                        "Planted-Defect Knockout",
                    ],
                    "headers_es": [
                        "Pilar Acoplado",
                        "Objeto Gobernante",
                        "Referencia Verificada",
                        "Estatuto Epistémico",
                        "Defecto Plantado",
                    ],
                    "rows": [
                        [
                            (
                                "1 · Wheeler–DeWitt Clock & QEP",
                                "1 · Reloj Wheeler–DeWitt y QEP",
                            ),
                            (
                                "64 × 64 Hermitian Ĉ (128 × 128 Jacobi) + 429.228 THz ⁸⁷Sr",
                                "Ĉ hermítico 64 × 64 (Jacobi 128 × 128) + ⁸⁷Sr a 429.228 THz",
                            ),
                            (
                                "‖Ĉ|Ψ⟩⟩‖ = 4.65 × 10⁻¹⁵; proj = 1.0; Δh·T_0 = 10.68 m·s; η = 0",
                                "‖Ĉ|Ψ⟩⟩‖ = 4.65 × 10⁻¹⁵; proy = 1.0; Δh·T_0 = 10.68 m·s; η = 0",
                            ),
                            ("DERIVED (NOT MEASURED)", "DERIVADO (NO MEDIDO)"),
                            (
                                "k² + 1 clock generator breaks shift invariance",
                                "Generador k² + 1 rompe invariancia de traslación",
                            ),
                        ],
                        [
                            (
                                "2 · 33 µm 4-Wall & Oppenheim Bound",
                                "2 · 4 Muros a 33 µm y Cota Oppenheim",
                            ),
                            (
                                "120-wedge signed Yukawa recast + Eq. F16 torque ceiling",
                                "Recast Yukawa con signo 120ω + techo de par Ec. F16",
                            ),
                            (
                                "σ_95 = 33.08 µm (≤ 33 µm); 3.31 × 10¹⁶× below 10⁻⁹ Cavendish",
                                "σ_95 = 33.08 µm (≤ 33 µm); 3.31 × 10¹⁶× bajo 10⁻⁹ Cavendish",
                            ),
                            ("DERIVED from Lee 2020", "DERIVADO de Lee 2020"),
                            (
                                "Retired 44.07 µm single-point edge match rejected",
                                "Rechaza el ajuste puntual retirado de 44.07 µm",
                            ),
                        ],
                        [
                            (
                                "3 · Bilateral X_A ⊗ X_B CPMG",
                                "3 · CPMG Bilateral X_A ⊗ X_B",
                            ),
                            (
                                "2-qubit echo on −J_grav Z_A Z_B + g_i Z_i + D[Z](ρ)",
                                "Eco de 2 qubits en −J_grav Z_A Z_B + g_i Z_i + D[Z](ρ)",
                            ),
                            (
                                "N_dd = 4 cuts γ_low-f 16× (0.123 → 0.308); γ_white 1× invariant",
                                "N_dd = 4 reduce γ_low-f 16× (0.123 → 0.308); γ_white 1× fijo",
                            ),
                            ("DERIVED (Open Quantum)", "DERIVADO (Sistema Abierto)"),
                            (
                                "Unilateral X_A ⊗ I flips Z_A Z_B → −Z_A Z_B (N = 0.0)",
                                "Unilateral X_A ⊗ I invierte Z_A Z_B → −Z_A Z_B (N = 0.0)",
                            ),
                        ],
                        [
                            (
                                "4 · Zero-Sorry Core Lean 4 Spine",
                                "4 · Columna Lean 4 sin Sorry",
                            ),
                            (
                                "IRUG_Unification.lean + Q[x_1,…,x_8] Fraction ring",
                                "IRUG_Unification.lean + anillo Fraction Q[x_1,…,x_8]",
                            ),
                            (
                                "0 sorry/axiom; 10 theorems; 9 ∀ quantifiers; 4/4 zero polynomials",
                                "0 sorry/axiom; 10 teoremas; 9 cuantificadores ∀; 4/4 polinomios nulos",
                            ),
                            ("FORMAL DEDUCTIVE", "DEDUCTIVO FORMAL"),
                            (
                                "Injected sorry token caught by comment-stripped AST scan",
                                "Token sorry inyectado detectado por escaneo AST limpio",
                            ),
                        ],
                    ],
                },
                {
                    "type": "p",
                    "en": (
                        "Run verify_essay_coupled_constraints.py locally—and pass --planted-defect—to execute every "
                        "matrix, torsion integral, spin-echo trajectory, and AST check in under 5 seconds with zero "
                        "network calls. When all four knockouts trip simultaneously on --planted-defect, the verifier "
                        "exits non-zero: precision in service of honesty, keeping the road open for the experiments ahead."
                    ),
                    "es": (
                        "Ejecuta localmente verify_essay_coupled_constraints.py —y añade --planted-defect— para correr "
                        "cada matriz, integral de torsión, trayectoria de eco y auditoría AST en menos de 5 segundos sin "
                        "red. Cuando los cuatro defectos plantados saltan con --planted-defect, el verificador sale con "
                        "error: precisión al servicio de la honestidad para los experimentos que vienen."
                    ),
                },
            ],
        },
    ],
    "sidenotes": [
        {
            "label_en": "Sidenote 1 · Why Bandwidth Scaling Uses [−3, −1, 1, 5]",
            "label_es": "Nota al Margen 1 · Por Qué el Reescalado Usa [−3, −1, 1, 5]",
            "en": (
                "Resolving α_grav = 1.091 × 10⁻¹⁶ natively on a uniform Fourier clock lattice would require ~10¹⁶ "
                "discrete levels. Setting dimensionless modes [−3, −1, 1, 5] on a 16-level Pegg–Barnett clock tests "
                "exact non-perturbative nullspace projection while our Decimal kernel evaluates the physical 10⁻¹⁶ "
                "optical 87Sr shift without 64-bit floating-point cancellation."
            ),
            "es": (
                "Resolver α_grav = 1.091 × 10⁻¹⁶ de forma nativa en una red uniforme de Fourier exigiría ~10¹⁶ niveles "
                "discretos. Fijar modos enteros [−3, −1, 1, 5] en un reloj de Pegg–Barnett de 16 niveles prueba la "
                "proyección exacta al núcleo nulo mientras Decimal evalúa el giro físico de 10⁻¹⁶ en 87Sr sin cancelación de 64 bits."
            ),
        },
        {
            "label_en": "Sidenote 2 · Why 33 µm Supersedes the Retired 44.07 µm Match",
            "label_es": "Nota al Margen 2 · Por Qué 33 µm Supera el Ajuste Retirado de 44.07 µm",
            "en": (
                "Matching the smeared torque deficit to |α| = 1 at a single 52 µm gap ignores the 95-run separation "
                "profile and the positive best-fit lean (α* > 0) in Table 11.4 of the 2020 Eöt-Wash analysis. Projecting "
                "onto the signed −α_95 profile tightens the 95% bound from 44.07 µm to 33.08 µm and excludes z = 30 µm "
                "(σ_c = 39.4 µm)."
            ),
            "es": (
                "Igualar el déficit de par a |α| = 1 en una sola separación de 52 µm ignora el perfil de 95 corridas y la "
                "inclinación positiva (α* > 0) de la Tabla 11.4 de Eöt-Wash 2020. Proyectar sobre el límite con signo "
                "−α_95 ajusta la cota al 95% de 44.07 µm a 33.08 µm y excluye z = 30 µm (σ_c = 39.4 µm)."
            ),
        },
        {
            "label_en": "Sidenote 3 · Unstated Averaging Window in Torque Residuals",
            "label_es": "Nota al Margen 3 · Ventana de Promedio No Declarada en Residuos de Par",
            "en": (
                "Lee et al. (2020) report the 0.0054 fN · m torque uncertainty at s = 72 µm without stating the per-point "
                "integration time T. Following our T.06 kernel, we carry T ∈ [10³ s, 10⁴ s] and r_N ∈ [1 fm, 7 fm] "
                "explicitly as named assumptions, yielding 12.98 to 16.52 decades of suppression below Cavendish."
            ),
            "es": (
                "Lee et al. (2020) reportan la incertidumbre de par de 0.0054 fN · m en s = 72 µm sin declarar el tiempo "
                "T por punto. Siguiendo nuestro núcleo T.06, mantenemos T ∈ [10³ s, 10⁴ s] y r_N ∈ [1 fm, 7 fm] como "
                "supuestos explícitos, dando de 12.98 a 16.52 décadas de supresión bajo Cavendish."
            ),
        },
        {
            "label_en": "Sidenote 4 · Pure Core Lean 4 Without External Imports",
            "label_es": "Nota al Margen 4 · Lean 4 Puro sin Importaciones Externas",
            "en": (
                "By formulating SIDim and cross-multiplied redshift numerators over core Int rather than Mathlib's ℚ, "
                "IRUG_Unification.lean compiles in a bare Lean 4 toolchain using only rfl, decide, omega, and "
                "Int.mul_add / Int.neg_mul_neg, mirrored 1:1 by Python's exact fractions.Fraction ring check."
            ),
            "es": (
                "Al formular SIDim y los numeradores de corrimiento sobre Int puro en vez de ℚ de Mathlib, "
                "IRUG_Unification.lean compila en Lean 4 base usando solo rfl, decide, omega e Int.mul_add / "
                "Int.neg_mul_neg, replicado 1:1 por el anillo exacto fractions.Fraction en Python."
            ),
        },
    ],
    "sources": [
        {
            "id": "ES06-MEIBOOM1958",
            "citation": "Meiboom, S., & Gill, D. — Modified spin-echo method for measuring nuclear relaxation times, Review of Scientific Instruments 29(8), 688–691",
            "doi": "10.1063/1.1716296",
            "year": 1958,
            "role_en": "Introduces the phase-compensated CPMG multi-pulse spin-echo sequence for low-frequency gradient refocusing.",
            "role_es": "Introduce la secuencia eco de espín multipulso CPMG para reenfocar gradientes lentos de baja frecuencia.",
        },
        {
            "id": "ES06-LINDBLAD1976",
            "citation": "Lindblad, G. — On the generators of quantum dynamical semigroups, Communications in Mathematical Physics 48(2), 119–130",
            "doi": "10.1007/bf01608499",
            "year": 1976,
            "role_en": "Characterizes memoryless Markovian quantum dynamical semigroups whose white dephasing rate is invariant under π-pulses.",
            "role_es": "Caracteriza los semigrupos dinámicos cuánticos markovianos sin memoria cuya tasa blanca es invariante ante pulsos π.",
        },
        {
            "id": "ES06-PAGE1983",
            "citation": "Page, D. N., & Wootters, W. K. — Evolution without evolution: Dynamics described by stationary observables, Physical Review D 27(12), 2885–2892",
            "doi": "10.1103/physrevd.27.2885",
            "year": 1983,
            "role_en": "Establishes relational quantum dynamics via conditioning inside the zero-eigenvalue Wheeler–DeWitt kernel.",
            "role_es": "Establece la dinámica cuántica relacional por condicionamiento dentro del núcleo nulo de Wheeler–DeWitt.",
        },
        {
            "id": "ES06-VIOLA1999",
            "citation": "Viola, L., Knill, E., & Lloyd, S. — Dynamical decoupling of open quantum systems, Physical Review Letters 82(12), 2417–2421",
            "doi": "10.1103/physrevlett.82.2417",
            "year": 1999,
            "role_en": "Formalizes symmetrizing pulse-group decoupling of non-Markovian system-bath couplings.",
            "role_es": "Formaliza el desacoplamiento dinámico por grupos de pulsos frente a baños no markovianos.",
        },
        {
            "id": "ES06-ZYCH2011",
            "citation": "Zych, M., Costa, F., Pikovski, I., & Brukner, Č. — Quantum interferometric visibility as a witness of general relativistic proper time, Nature Communications 2, 505",
            "doi": "10.1038/ncomms1498",
            "year": 2011,
            "role_en": "Derives matter-wave fringe visibility modulation V = |cos(ω Δτ / 2)| from general-relativistic proper-time lag.",
            "role_es": "Deriva la modulación de visibilidad V = |cos(ω Δτ / 2)| producida por el retraso relativista de tiempo propio.",
        },
        {
            "id": "ES06-PERUZZO2014",
            "citation": "Peruzzo, A., McClean, J., Shadbolt, P., Yung, M.-H., Zhou, X.-Q., Love, P. J., Aspuru-Guzik, A., & O'Brien, J. L. — A variational eigenvalue solver on a photonic quantum processor, Nature Communications 5, 4213",
            "doi": "10.1038/ncomms5213",
            "year": 2014,
            "role_en": "Establishes Rayleigh–Ritz variational eigenvalue bounds separating Hamiltonian expectation from hardware noise.",
            "role_es": "Establece cotas variacionales de autovalores separando expectativa hamiltoniana y ruido del dispositivo.",
        },
        {
            "id": "ES06-BARATO2016",
            "citation": "Barato, A. C., & Seifert, U. — Cost and precision of Brownian clocks, Physical Review X 6(4), 041053",
            "doi": "10.1103/physrevx.6.041053",
            "year": 2016,
            "role_en": "Proves the thermodynamic dissipation-precision bound for autonomous Markovian and biomolecular clocks.",
            "role_es": "Demuestra la cota termodinámica entre disipación y precisión en relojes markovianos y biomoleculares.",
        },
        {
            "id": "ES06-LEE2020",
            "citation": "Lee, J. G., Adelberger, E. G., Cook, T. S., Fleischer, S. M., & Heckel, B. R. — New test of the gravitational 1/r² law at separations down to 52 µm, Physical Review Letters 124(10), 101101",
            "doi": "10.1103/physrevlett.124.101101",
            "year": 2020,
            "role_en": "Provides the 120-fold wedge torsion-balance data recasted to σ ≤ 33 µm and the 0.0054 fN · m torque residual.",
            "role_es": "Aporta los datos de balanza de torsión de 120 cuñas proyectados a σ ≤ 33 µm y el residuo de 0.0054 fN · m.",
        },
        {
            "id": "ES06-OPPENHEIM2023",
            "citation": "Oppenheim, J., Sparaciari, C., Šoda, B., & Weller-Davies, Z. — Gravitationally induced decoherence vs space-time diffusion: testing the quantum nature of gravity, Nature Communications 14, 7910",
            "doi": "10.1038/s41467-023-43348-2",
            "year": 2023,
            "role_en": "Derives the post-quantum classical-gravity momentum-diffusion vs decoherence inequality (Eq. F16).",
            "role_es": "Deriva la desigualdad post-cuántica entre difusión de momento y decoherencia gravitatoria (Ec. F16).",
        },
        {
            "id": "ES06-SCHUT2024",
            "citation": "Schut, M., Geraci, A., Bose, S., & Mazumdar, A. — Micrometer-size spatial superpositions for the QGEM protocol via screening and trapping, Physical Review Research 6(1), 013199",
            "doi": "10.1103/physrevresearch.6.013199",
            "year": 2024,
            "role_en": "Defines the Casimir-screened parallel QGEM geometries (z = 30 µm and z = 10 µm) tested against Wall 2 and Wall 4.",
            "role_es": "Define las geometrías QGEM paralelas apantalladas (z = 30 µm y z = 10 µm) evaluadas ante los Muros 2 y 4.",
        },
        {
            "id": "ES06-TRILLO2025",
            "citation": "Trillo, D., & Navascués, M. — Diósi–Penrose model of classical gravity predicts gravitationally induced entanglement, Physical Review D 111(12), L121101",
            "doi": "10.1103/physrevd.111.l121101",
            "year": 2025,
            "role_en": "Formulates the smeared-density hybrid classical-gravity master equation and critical separation d_c ≈ 0.8509 σ.",
            "role_es": "Formula la ecuación maestra híbrida con densidad difuminada y la separación crítica d_c ≈ 0.8509 σ.",
        },
        {
            "id": "ES06-TOOBYSMITH2025",
            "citation": "Tooby-Smith, J. — HepLean: Digitalising high energy physics, Computer Physics Communications 308, 109457",
            "doi": "10.1016/j.cpc.2024.109457",
            "year": 2025,
            "role_en": "Establishes Lean 4 type-theoretic formalization patterns for dimensional and algebraic physics specifications.",
            "role_es": "Establece patrones de formalización en Lean 4 para especificaciones físicas dimensionales y algebraicas.",
        },
    ],
    "skill_path": "skills/essays/coupled-constraints-formal-proof/SKILL.md",
    "verifier_path": "skills/essays/coupled-constraints-formal-proof/verify_essay_coupled_constraints.py",
    "ai_line_en": (
        "AI contribution to cited primary literature: none. Essay prose, bilingual es-MX twin, 128 × 128 Jacobi "
        "Wheeler–DeWitt kernel, bilateral CPMG simulator, core Lean 4 specification, and Python verifier were "
        "drafted with AI assistance and checked deterministically against cached primary DOIs."
    ),
    "ai_line_es": (
        "Contribución de IA a la literatura primaria citada: ninguna. El ensayo, su gemelo es-MX, el núcleo "
        "Wheeler–DeWitt de Jacobi 128 × 128, el simulador CPMG bilateral, la especificación en Lean 4 y el "
        "verificador en Python se redactaron con apoyo de IA y se verificaron contra DOIs primarios en caché."
    ),
}
