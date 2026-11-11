# -*- coding: utf-8 -*-
"""Cross-Scale Essay ES.09 · Multipartite Witnesses, Scaling Tomography & Active Clocks.

Pure-Python stdlib physics kernel, 8x8 multipartite density-matrix & partial-transpose solver,
multivariate rational polynomial verifier, and bilingual (EN / es-MX) monograph data for
Informatico.ai's Cross-Scale Essay (/essays/multipartite-witnesses-active-clocks/).

Synthesizes four coupled analytical, operational, and formal results:
  1. Exact 8x8 Equilateral-Prism Tripartite Quantum vs. 3-Body Diósi-Penrose Dynamics at
     D = 75 um, Delta_x = 250 um, m = 10^-14 kg: proves and cross-checks to < 10^-14 the Exact
     Position-Pointer Mermin Law <M_3(t)> = eta^3 + 3 eta sin^2(Delta_phi(t) / 2), reaching
     3.6741 at T = 2.0 K (P = 2.7e-16 Pa, gamma_loc = 0.0220 s^-1, t_pi = 2.6120 s) to clear both
     the 3-local hidden-variable bound (2.0) and the Seevinck-Svetlichny biseparable bound
     (2*sqrt(2) = 2.8284) for Genuine Tripartite Entanglement (GTE), while collective 3-body
     Diósi-Penrose hybrid gravity obeys ((sqrt(17) - 1) / 2) b = a => sigma_c^(1|23) = 34.93 um
     > sigma_95 = 33.08 um (N_{1|23}^hyb(t) = 0 identically for all t >= 0, dynamical log-grid
     max <M_3>_hyb = 0.9268 < 1.0), plus the 3-D Euclidean orthogonal-null dimension obstruction
     contrasted with the alternating collinear (x, y, x) stack null.
  2. Log-Scaling & Composition Tomography (Aziz & Howl 2025 vs. Newtonian Quantum vs. Oppenheim
     2023 & Schneider et al. 2026): separates printed sqrt(theta)_AH ~ m_atom^2 M^(10/3) t^1 D^-1
     from squared theta_AH ~ m_atom^4 M^(20/3) t^2 D^-2, proving that swapping 12C diamond for
     173Yb at fixed (M, D, Delta_x, t) leaves Newtonian Delta_phi_Q identically invariant (1.0000x,
     Weak Equivalence Principle) while boosting sqrt(theta)_AH by 165.8x and theta_AH by 27,500x
     (non-degenerate scaling Jacobians det != 0), and contrasts coherent unitary revival at
     t = 2 t_pi = 5.2240 s against Oppenheim Markovian momentum-diffusion decay.
  3. Active Quantum Clock Proper-Time Probes (Zych et al. 2011; Sorci et al. 2026; Tobar,
     Aspelmeyer & Zych 2026): evaluates relativistic proper-time redshift phases and Zych-Brukner
     visibility modulation V_clock(t) = |cos(Delta_Phi_clock / 2)| for 87Sr optical and 229Th
     nuclear clocks alongside passive center-of-mass action phases (hbar * omega_clock / (M c^2)),
     bridged to surface-code stabilizer parity checks (Gidney 2021) and 3-site allostery.
  4. Nine zero-sorry core Lean 4 Prelude theorems (MultipartiteWitness.lean) mirrored by exact
     multivariate Fraction polynomial checks.
"""
from __future__ import annotations

import cmath
from decimal import Decimal, InvalidOperation
from fractions import Fraction
import functools
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
import timegravity_kernel_decoherence as k_deco  # noqa: E402
import timegravity_kernel_dispute as k_disp  # noqa: E402
import timegravity_kernel_entangle as k_ent  # noqa: E402
import timegravity_kernel_recast as k_rec  # noqa: E402

CODE = "ES.09"
SLUG = "multipartite-witnesses-active-clocks"
PLATE_SLUG = "essay09"

G_NEWTON = k_base.G_NEWTON
HBAR = k_ent.HBAR
C_LIGHT = 299_792_458.0
EARTH_G_M_S2 = 9.80665

BENCH_GAP_M = 75.0e-6
BENCH_SPLIT_M = 250.0e-6
BENCH_MASS_KG = 1.0e-14
BENCH_PRESSURE_PA = 2.7e-16
BENCH_TEMP_K = 2.0

# Exact analytical collective 1|23 partial-transpose threshold ratio a / b = (sqrt(17) - 1) / 2
DP3_COLLECTIVE_LAMBDA = 0.5 * (math.sqrt(17.0) - 1.0)
LHV_MERMIN_BOUND = 2.0
BISEPARABLE_GTE_BOUND = 2.0 * math.sqrt(2.0)

# Optical & nuclear internal clock transition angular frequencies (rad/s)
OMEGA_SR87_RAD_S = 2.0 * math.pi * 4.29228004229873e14
OMEGA_TH229_RAD_S = 2.0 * math.pi * 2.020407384335e15

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


@functools.lru_cache(maxsize=1)
def _cached_eotwash_sigma_95_m() -> tuple[float, bool, bool]:
    """Verify the canonical n_sep=12 Eöt-Wash 120-wedge signed recast bracket around 33.08 um in ~2 s."""
    rc = k_rec.Recast(120, "log52-3000", n_sep=12, lam_min=17.5e-6, lam_max=19.5e-6)
    lo_s, hi_s = 33.04e-6, 33.12e-6
    lo_not_excl = not rc.at_sigma(lo_s)["excluded"]
    hi_excl = rc.at_sigma(hi_s)["excluded"]
    return math.sqrt(lo_s * hi_s), lo_not_excl, hi_excl


def _kron2(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    ra, ca = len(a), len(a[0])
    rb, cb = len(b), len(b[0])
    return [[a[i // rb][j // cb] * b[i % rb][j % cb] for j in range(ca * cb)] for i in range(ra * rb)]


@functools.lru_cache(maxsize=1)
def _mermin_operators_8x8() -> dict[str, list[list[complex]]]:
    x2 = [[0j, 1.0 + 0j], [1.0 + 0j, 0j]]
    z2 = [[1.0 + 0j, 0j], [0j, -1.0 + 0j]]
    xxx = _kron2(_kron2(x2, x2), x2)
    xzz = _kron2(_kron2(x2, z2), z2)
    zxz = _kron2(_kron2(z2, x2), z2)
    zzx = _kron2(_kron2(z2, z2), x2)
    m3 = [[xxx[r][c] - xzz[r][c] - zxz[r][c] - zzx[r][c] for c in range(8)] for r in range(8)]
    return {"XXX": xxx, "XZZ": xzz, "M3": m3}


def _trace_product_8x8(rho: list[list[complex]], op: list[list[complex]]) -> float:
    return sum(rho[r][c] * op[c][r] for r in range(8) for c in range(8)).real


def prism_branches_3d(split_m: float = BENCH_SPLIT_M, gap_m: float = BENCH_GAP_M) -> list[tuple[tuple[float, float, float], ...]]:
    """Eight 3-body spatial branch tuples (x_1, x_2, x_3) on an equilateral prism of side D and z-split Delta_x."""
    verts = (
        (0.0, 0.0),
        (gap_m, 0.0),
        (0.5 * gap_m, 0.5 * math.sqrt(3.0) * gap_m),
    )
    branches = []
    for idx in range(8):
        s1 = 1.0 if ((idx >> 2) & 1) == 0 else -1.0
        s2 = 1.0 if ((idx >> 1) & 1) == 0 else -1.0
        s3 = 1.0 if (idx & 1) == 0 else -1.0
        branches.append(
            (
                (verts[0][0], verts[0][1], 0.5 * split_m * s1),
                (verts[1][0], verts[1][1], 0.5 * split_m * s2),
                (verts[2][0], verts[2][1], 0.5 * split_m * s3),
            )
        )
    return branches


def quantum_prism_rho8(
    t_s: float,
    gamma_loc_per_s: float = 0.0,
    split_m: float = BENCH_SPLIT_M,
    gap_m: float = BENCH_GAP_M,
    mass_kg: float = BENCH_MASS_KG,
) -> list[list[complex]]:
    """Exact 8x8 tripartite density matrix under Newtonian 1/r pair phases and local position-branch dephasing."""
    br = prism_branches_3d(split_m, gap_m)
    eta = math.exp(-gamma_loc_per_s * t_s)
    phases = []
    for pts in br:
        ph = 0.0
        for j in range(3):
            for k in range(j + 1, 3):
                ph += G_NEWTON * mass_kg * mass_kg * t_s / (HBAR * math.dist(pts[j], pts[k]))
        phases.append(ph)
    rho = [[0j] * 8 for _ in range(8)]
    for r in range(8):
        for c in range(8):
            hamming = (r ^ c).bit_count()
            rho[r][c] = 0.125 * cmath.exp(1j * (phases[r] - phases[c])) * (eta ** hamming)
    return rho


def mermin_quantum_closed(
    t_s: float,
    gamma_loc_per_s: float = 0.0,
    split_m: float = BENCH_SPLIT_M,
    gap_m: float = BENCH_GAP_M,
    mass_kg: float = BENCH_MASS_KG,
    planted_defect: bool = False,
) -> float:
    """Closed-form Position-Pointer Mermin Law:
      <M_3(t)> = eta^3 + 3 * eta * sin^2(Delta_phi(t) / 2).
    Under planted_defect=True, wrongly applies naive 3-qubit eta^3 damping to -X_i Z_j Z_k."""
    omega_pair = 2.0 * (G_NEWTON * mass_kg * mass_kg / HBAR) * (1.0 / gap_m - 1.0 / math.hypot(gap_m, split_m))
    dphi = omega_pair * t_s
    eta = math.exp(-gamma_loc_per_s * t_s)
    s2 = math.sin(0.5 * dphi) ** 2
    if planted_defect:
        return (eta ** 3) * (1.0 + 3.0 * s2)
    return (eta ** 3) + 3.0 * eta * s2


def dp3_hybrid_rho8(
    t_s: float,
    sigma_m: float,
    gamma_loc_per_s: float = 0.0,
    branches_3d: list[tuple[tuple[float, float, float], ...]] | None = None,
    masses_kg: tuple[float, float, float] = (BENCH_MASS_KG, BENCH_MASS_KG, BENCH_MASS_KG),
) -> list[list[complex]]:
    """Exact 8x8 3-body Diósi-Penrose hybrid state for arbitrary 3-D branch coordinates and masses."""
    br = branches_3d if branches_3d is not None else prism_branches_3d(BENCH_SPLIT_M, BENCH_GAP_M)
    k0 = (G_NEWTON / (2.0 * HBAR)) * t_s
    eta = math.exp(-gamma_loc_per_s * t_s)
    rho = [[0j] * 8 for _ in range(8)]
    for r in range(8):
        xr = br[r]
        for c in range(8):
            yc = br[c]
            re_g = 0.0
            im_g = 0.0
            for j in range(3):
                for k in range(3):
                    mm = masses_kg[j] * masses_kg[k]
                    if mm == 0.0:
                        continue
                    fxx = k_disp.f_tilde(math.dist(xr[j], xr[k]), sigma_m)
                    fyy = k_disp.f_tilde(math.dist(yc[j], yc[k]), sigma_m)
                    fxy = k_disp.f_tilde(math.dist(xr[j], yc[k]), sigma_m)
                    re_g += mm * (-fxx - fyy + 2.0 * fxy)
                    im_g += mm * (fxx - fyy)
            hamming = (r ^ c).bit_count()
            rho[r][c] = 0.125 * cmath.exp(k0 * complex(re_g, im_g)) * (eta ** hamming)
    return rho


def dp3_mermin_closed(
    t_s: float,
    sigma_m: float,
    gamma_loc_per_s: float = 0.0,
    split_m: float = BENCH_SPLIT_M,
    gap_m: float = BENCH_GAP_M,
    mass_kg: float = BENCH_MASS_KG,
) -> float:
    """Exact closed-form <M_3(t)>_hyb on the equilateral prism:
      <M_3(t)>_hyb = (eta^3 / 4)(e^{-6(a+2b)tau} + 3 e^{-2(3a-2b)tau}) + 3 eta e^{-2 a tau} sin^2(2 b tau)."""
    a = k_disp.f_tilde(0.0, sigma_m) - k_disp.f_tilde(split_m, sigma_m)
    b = abs(k_disp.f_tilde(gap_m, sigma_m) - k_disp.f_tilde(math.hypot(gap_m, split_m), sigma_m))
    tau = G_NEWTON * mass_kg * mass_kg * t_s / (2.0 * HBAR)
    eta = math.exp(-gamma_loc_per_s * t_s)
    xxx = 0.25 * (eta ** 3) * (math.exp(-6.0 * (a + 2.0 * b) * tau) + 3.0 * math.exp(-2.0 * (3.0 * a - 2.0 * b) * tau))
    xzz_sum = 3.0 * eta * math.exp(-2.0 * a * tau) * (math.sin(2.0 * b * tau) ** 2)
    return xxx + xzz_sum


def partial_transpose_1_23(rho8: list[list[complex]]) -> list[list[complex]]:
    """Partial transpose over qubit 1 in bipartition 1|23 of an 8x8 3-qubit density matrix."""
    out = [[0j] * 8 for _ in range(8)]
    for i1 in range(2):
        for j23 in range(4):
            for k1 in range(2):
                for l23 in range(4):
                    out[4 * i1 + j23][4 * k1 + l23] = rho8[4 * k1 + j23][4 * i1 + l23]
    return out


def negativity_1_23(rho8: list[list[complex]]) -> float:
    """Peres-Horodecki 1|23 collective partial-transpose negativity of an 8x8 state."""
    eigs = k_ent.hermitian_eigenvalues(partial_transpose_1_23(rho8))
    return sum(-v for v in eigs if v < -1.0e-13)


def dp3_collective_critical_sigma_exact(split_m: float = BENCH_SPLIT_M, gap_m: float = BENCH_GAP_M) -> float:
    """Exact critical smearing width sigma_c^(1|23) where ((sqrt(17) - 1) / 2) * b(sigma) = a(sigma)."""
    lo, hi = 1.0e-6, 1.0e-3
    r_diff = math.hypot(gap_m, split_m)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        a = k_disp.f_tilde(0.0, mid) - k_disp.f_tilde(split_m, mid)
        b = abs(k_disp.f_tilde(gap_m, mid) - k_disp.f_tilde(r_diff, mid))
        if DP3_COLLECTIVE_LAMBDA * b > a:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def evaluate_tripartite_prism_dynamics(planted_defect: bool = False) -> dict:
    """Result 1: Exact 8x8 equilateral-prism quantum vs. 3-body Diósi-Penrose dynamics & 3-D null geometry."""
    sigma_95_m, bracket_lo_ok, bracket_hi_ok = _cached_eotwash_sigma_95_m()
    ops = _mermin_operators_8x8()

    r_same = BENCH_GAP_M
    r_diff = math.hypot(BENCH_GAP_M, BENCH_SPLIT_M)
    omega_pair = 2.0 * (G_NEWTON * BENCH_MASS_KG * BENCH_MASS_KG / HBAR) * (1.0 / r_same - 1.0 / r_diff)
    t_pi = math.pi / omega_pair

    r_sphere = k_disp.sphere_radius(BENCH_MASS_KG, k_disp.DIAMOND_DENSITY)
    gamma_gas_2k = k_deco.gas_rate(BENCH_SPLIT_M, BENCH_PRESSURE_PA, BENCH_TEMP_K, r_sphere, form="cited")
    gamma_phot_2k = k_deco.photon_rate(BENCH_SPLIT_M, r_sphere, BENCH_TEMP_K, BENCH_TEMP_K)["total"]
    gamma_loc_2k = gamma_gas_2k + gamma_phot_2k  # 0.022001 s^-1 at T = 2.0 K, P = 2.7e-16 Pa
    eta_2k = math.exp(-gamma_loc_2k * t_pi)

    # Cross-check closed-form Mermin law against 8x8 matrix traces across times & noise rates
    max_q_trace_diff = 0.0
    for t_chk in (0.0, 0.65, 0.5 * t_pi, t_pi, 2.0 * t_pi):
        for g_chk in (0.0, gamma_loc_2k, 0.14):
            rho_q = quantum_prism_rho8(t_chk, g_chk)
            m_tr = _trace_product_8x8(rho_q, ops["M3"])
            m_cl = mermin_quantum_closed(t_chk, g_chk, planted_defect=planted_defect)
            max_q_trace_diff = max(max_q_trace_diff, abs(m_tr - m_cl))

    rho_q_tpi_2k = quantum_prism_rho8(t_pi, gamma_loc_2k)
    m3_tpi_2k = mermin_quantum_closed(t_pi, gamma_loc_2k, planted_defect=planted_defect)
    m3_tpi_unitary = mermin_quantum_closed(t_pi, 0.0, planted_defect=planted_defect)
    neg_q_1_23_tpi_2k = negativity_1_23(rho_q_tpi_2k)
    biseparable_bound_used = LHV_MERMIN_BOUND if planted_defect else BISEPARABLE_GTE_BOUND

    # 3-body Diósi-Penrose: (a) trace preservation & no-signalling marginal reduction
    rho_dp_bench = dp3_hybrid_rho8(2.5, sigma_95_m, gamma_loc_2k)
    trace_err_dp = abs(sum(rho_dp_bench[i][i] for i in range(8)) - 1.0)

    # Decoupled spectator (m_3 = 0) reduces Tr_3(rho_123^DP) identically to 2-body rho_12^DP:
    rho_dp_decoupled = dp3_hybrid_rho8(2.5, sigma_95_m, gamma_loc_2k, masses_kg=(BENCH_MASS_KG, BENCH_MASS_KG, 0.0))
    tr3_decoupled = [[rho_dp_decoupled[2 * r][2 * c] + rho_dp_decoupled[2 * r + 1][2 * c + 1] for c in range(4)] for r in range(4)]
    br2_par = [((0.0, 0.5 * BENCH_SPLIT_M * s1), (BENCH_GAP_M, 0.5 * BENCH_SPLIT_M * s2)) for s1 in (1.0, -1.0) for s2 in (1.0, -1.0)]
    rho2_direct = k_disp.dephase_points(k_disp.hybrid_state_points(br2_par, BENCH_MASS_KG, sigma_95_m, 2.5), gamma_loc_2k, 2.5)
    no_signalling_decoupled_diff = max(abs(tr3_decoupled[r][c] - rho2_direct[r][c]) for r in range(4) for c in range(4))

    # Also verify local unitary invariance on qubit 3 (Hadamard basis choice on 3 cannot signal to 12):
    inv_s2 = 1.0 / math.sqrt(2.0)
    h2 = [[inv_s2 + 0j, inv_s2 + 0j], [inv_s2 + 0j, -inv_s2 + 0j]]
    i2 = [[1.0 + 0j, 0j], [0j, 1.0 + 0j]]
    u_loc3 = _kron2(_kron2(i2, i2), h2)
    tmp_u = [[sum(u_loc3[r][k] * rho_dp_bench[k][c] for k in range(8)) for c in range(8)] for r in range(8)]
    rho_rot3 = [[sum(tmp_u[r][k] * u_loc3[c][k].conjugate() for k in range(8)) for c in range(8)] for r in range(8)]
    tr3_orig = [[rho_dp_bench[2 * r][2 * c] + rho_dp_bench[2 * r + 1][2 * c + 1] for c in range(4)] for r in range(4)]
    tr3_rot = [[rho_rot3[2 * r][2 * c] + rho_rot3[2 * r + 1][2 * c + 1] for c in range(4)] for r in range(4)]
    local_unitary_nosignal_diff = max(abs(tr3_orig[r][c] - tr3_rot[r][c]) for r in range(4) for c in range(4))

    # (b) Collective 1|23 critical smearing width sigma_c^(1|23) = 34.93 um > sigma_95 = 33.08 um
    sigma_c_1_23_m = dp3_collective_critical_sigma_exact(BENCH_SPLIT_M, BENCH_GAP_M)
    sigma_c_pair_m = k_disp.parallel_hybrid_critical_sigma_exact(BENCH_SPLIT_M, BENCH_GAP_M, 0.0)
    neg_dp_at_sigma95_grid = max(
        negativity_1_23(dp3_hybrid_rho8(10.0 ** (k / 2.0), sigma_95_m))
        for k in range(-3, 9)
    )
    neg_dp_below_sc = max(negativity_1_23(dp3_hybrid_rho8(t_chk, 34.80e-6)) for t_chk in (0.1, 0.35, 1.0, 2.5))
    neg_dp_above_sc = max(negativity_1_23(dp3_hybrid_rho8(t_chk, 35.15e-6)) for t_chk in (0.1, 0.35, 1.0, 2.5))

    # (c) Closed-form vs 8x8 DP Mermin expectation and log-grid dynamical peak 0.9268 < 1.0
    max_dp_m3_trace_diff = max(
        abs(_trace_product_8x8(dp3_hybrid_rho8(t_chk, sigma_95_m, gamma_loc_2k), ops["M3"]) - dp3_mermin_closed(t_chk, sigma_95_m, gamma_loc_2k))
        for t_chk in (0.0, 0.5, 1.4, t_pi, 10.0)
    )
    dp_m3_log_grid_max = max(dp3_mermin_closed(10.0 ** (k / 4.0), sigma_95_m, 0.0) for k in range(-6, 36))
    dp_m3_secondary_bump = max(dp3_mermin_closed(1.0 + 0.02 * k, sigma_95_m, 0.0) for k in range(35))
    dp_m3_at_tpi_2k = dp3_mermin_closed(t_pi, sigma_95_m, gamma_loc_2k)

    # (d) 3-D Orthogonal Null Dimension Obstruction vs Alternating Collinear (x, y, x) Stack Null
    # On planar equilateral triangle (R_12 = (D, 0, 0)), assigning mutually orthogonal axes (x_hat, y_hat, z_hat)
    # violates s_1 perp R_12: r(+,+) = sqrt((D - dx/2)^2 + (dx/2)^2) != r(-,-) = sqrt((D + dx/2)^2 + (dx/2)^2)!
    r_pp_planar_xyz = math.hypot(BENCH_GAP_M - 0.5 * BENCH_SPLIT_M, 0.5 * BENCH_SPLIT_M)
    r_mm_planar_xyz = math.hypot(BENCH_GAP_M + 0.5 * BENCH_SPLIT_M, 0.5 * BENCH_SPLIT_M)
    r_pm_planar_xyz = math.hypot(BENCH_GAP_M - 0.5 * BENCH_SPLIT_M, 0.5 * BENCH_SPLIT_M)
    r_mp_planar_xyz = math.hypot(BENCH_GAP_M + 0.5 * BENCH_SPLIT_M, 0.5 * BENCH_SPLIT_M)
    # Wait: check exact 3D Euclidean distances for s_1 = x_hat at (0,0,0) and s_2 = y_hat at (D,0,0):
    # x_1(s1) = (s1*dx/2, 0, 0), x_2(s2) = (D, s2*dx/2, 0):
    # Notice s1=+1 gives |x_2 - x_1| = sqrt((D - dx/2)^2 + (dx/2)^2) for BOTH s2=+1 and s2=-1 (so pair 12 alone has
    # alpha_1 + beta_2 product phase!), whereas on the equilateral vertex 3 at (D/2, sqrt(3)D/2, 0) with s_3 = z_hat,
    # look at pair (1,2) if R_12 has BOTH x and y components—e.g. pair (2,3) has R_23 = (-D/2, sqrt(3)D/2, 0),
    # which has non-zero projection on BOTH x_hat AND y_hat! Wait: for pair (1,2) with R_12 = (-D/2, sqrt(3)D/2, 0)
    # and s_1 = x_hat, s_2 = y_hat: let's compute exact 4-branch entanglement phase on rotated equilateral triangle!
    rot_ang = math.pi / 6.0  # general orientation of equilateral triangle in xy-plane
    v_rot = (
        (0.0, 0.0, 0.0),
        (BENCH_GAP_M * math.cos(rot_ang), BENCH_GAP_M * math.sin(rot_ang), 0.0),
        (BENCH_GAP_M * math.cos(rot_ang + math.pi / 3.0), BENCH_GAP_M * math.sin(rot_ang + math.pi / 3.0), 0.0),
    )
    axes_xyz = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
    # Pair (0, 1) cross-phase when R_01 has both x and y components and s_0 = x_hat, s_1 = y_hat:
    d_01 = {}
    for b0, s0 in (("L", -0.5 * BENCH_SPLIT_M), ("R", 0.5 * BENCH_SPLIT_M)):
        for b1, s1 in (("L", -0.5 * BENCH_SPLIT_M), ("R", 0.5 * BENCH_SPLIT_M)):
            p0 = tuple(v_rot[0][q] + s0 * axes_xyz[0][q] for q in range(3))
            p1 = tuple(v_rot[1][q] + s1 * axes_xyz[1][q] for q in range(3))
            d_01[b0 + b1] = math.dist(p0, p1)
    planar_xyz_spurious_phase_rad = abs(
        (G_NEWTON * BENCH_MASS_KG * BENCH_MASS_KG * t_pi / HBAR)
        * (1.0 / d_01["LR"] + 1.0 / d_01["RL"] - 1.0 / d_01["LL"] - 1.0 / d_01["RR"])
    )

    # Alternating collinear z-stack (0,0,0), (0,0,D), (0,0,2D) with midpoint splits (x_hat, y_hat, x_hat):
    col_xyx_d12 = []
    col_xyx_d23 = []
    for s1 in (-0.5 * BENCH_SPLIT_M, 0.5 * BENCH_SPLIT_M):
        for s2 in (-0.5 * BENCH_SPLIT_M, 0.5 * BENCH_SPLIT_M):
            col_xyx_d12.append(math.dist((s1, 0.0, 0.0), (0.0, s2, BENCH_GAP_M)))
            col_xyx_d23.append(math.dist((0.0, s2, BENCH_GAP_M), (s1, 0.0, 2.0 * BENCH_GAP_M)))
    collinear_xyx_nn_spread_m = max(max(col_xyx_d12) - min(col_xyx_d12), max(col_xyx_d23) - min(col_xyx_d23))
    dphi_13_2d_rad = (
        2.0
        * (G_NEWTON * BENCH_MASS_KG * BENCH_MASS_KG * t_pi / HBAR)
        * (1.0 / (2.0 * BENCH_GAP_M) - 1.0 / math.hypot(2.0 * BENCH_GAP_M, BENCH_SPLIT_M))
    )

    return {
        "sigma_95_um": sigma_95_m * 1.0e6,
        "eotwash_bracket_verified": bracket_lo_ok and bracket_hi_ok,
        "omega_pair_rad_s": omega_pair,
        "t_pi_s": t_pi,
        "gamma_loc_2k_per_s": gamma_loc_2k,
        "eta_2k_at_tpi": eta_2k,
        "mermin_unitary_at_tpi": m3_tpi_unitary,
        "mermin_2k_at_tpi": m3_tpi_2k,
        "lhv_bound": LHV_MERMIN_BOUND,
        "biseparable_bound": biseparable_bound_used,
        "gte_certified_at_2k": m3_tpi_2k > biseparable_bound_used,
        "quantum_negativity_1_23_2k": neg_q_1_23_tpi_2k,
        "max_8x8_vs_closed_mermin_diff": max_q_trace_diff,
        "dp3_trace_error": trace_err_dp,
        "dp3_nosignal_decoupled_diff": no_signalling_decoupled_diff,
        "dp3_nosignal_local_unitary_diff": local_unitary_nosignal_diff,
        "sigma_c_1_23_um": sigma_c_1_23_m * 1.0e6,
        "sigma_c_pair_um": sigma_c_pair_m * 1.0e6,
        "dp3_negativity_1_23_at_sigma95": neg_dp_at_sigma95_grid,
        "dp3_negativity_below_sc_34p8um": neg_dp_below_sc,
        "dp3_negativity_above_sc_35p15um": neg_dp_above_sc,
        "max_dp3_8x8_vs_closed_mermin_diff": max_dp_m3_trace_diff,
        "dp3_mermin_log_grid_max": dp_m3_log_grid_max,
        "dp3_mermin_secondary_bump": dp_m3_secondary_bump,
        "dp3_mermin_at_tpi_2k": dp_m3_at_tpi_2k,
        "planar_xyz_spurious_phase_rad": planar_xyz_spurious_phase_rad,
        "collinear_xyx_nn_distance_um": col_xyx_d12[0] * 1.0e6,
        "collinear_xyx_nn_spread_m": collinear_xyx_nn_spread_m,
        "collinear_xyx_13_phase_at_tpi_rad": dphi_13_2d_rad,
    }


def evaluate_scaling_and_composition_tomography(planted_defect: bool = False) -> dict:
    """Result 2: Log-scaling Jacobians, 12C vs 173Yb composition tomography, and unitary revival vs Markovian decay."""
    omega_pair = 2.0 * (G_NEWTON * BENCH_MASS_KG * BENCH_MASS_KG / HBAR) * (
        1.0 / BENCH_GAP_M - 1.0 / math.hypot(BENCH_GAP_M, BENCH_SPLIT_M)
    )
    t_pi = math.pi / omega_pair

    r_c12 = k_disp.sphere_radius(BENCH_MASS_KG, k_disp.DIAMOND_DENSITY)
    r_yb = k_disp.sphere_radius(BENCH_MASS_KG, k_disp.YTTERBIUM_DENSITY)

    theta_c12 = k_disp.aziz_howl_theta(k_disp.CARBON12_KG, BENCH_MASS_KG, r_c12, t_pi, BENCH_GAP_M)
    sqrt_theta_c12 = math.sqrt(theta_c12)
    phi_q_c12 = k_disp.quantum_phase_aziz(BENCH_MASS_KG, t_pi, BENCH_GAP_M)

    atom_yb_used = k_disp.CARBON12_KG if planted_defect else k_disp.YTTERBIUM_KG
    theta_yb = k_disp.aziz_howl_theta(atom_yb_used, BENCH_MASS_KG, r_yb, t_pi, BENCH_GAP_M)
    sqrt_theta_yb = math.sqrt(theta_yb)
    phi_q_yb = k_disp.quantum_phase_aziz(BENCH_MASS_KG, t_pi, BENCH_GAP_M)

    # Exact scaling exponents at constant material density:
    #   Delta_phi_Q ~ m_atom^0 * M^2 * t^1 * D^-1
    #   sqrt(theta)_AH ~ m_atom^2 * M^(10/3) * t^1 * D^-1
    #   theta_AH ~ m_atom^4 * M^(20/3) * t^2 * D^-2
    det_m_matom = 2.0 * 2.0 - 0.0 * (10.0 / 3.0)  # = 4.0
    det_m_t_theta = 2.0 * 2.0 - 1.0 * (20.0 / 3.0)  # = -8/3

    # Coherent revival at t = 2 t_pi = 5.2240 s vs Oppenheim Markovian diffusion
    gamma_loc_2k = (
        k_deco.gas_rate(BENCH_SPLIT_M, BENCH_PRESSURE_PA, BENCH_TEMP_K, r_c12, form="cited")
        + k_deco.photon_rate(BENCH_SPLIT_M, r_c12, BENCH_TEMP_K, BENCH_TEMP_K)["total"]
    )
    t_revival = 2.0 * t_pi
    rho_revival = quantum_prism_rho8(t_revival, gamma_loc_2k)
    m3_revival = mermin_quantum_closed(t_revival, gamma_loc_2k)
    eta_tpi = math.exp(-gamma_loc_2k * t_pi)
    eta_2tpi = math.exp(-gamma_loc_2k * t_revival)
    # Single-qubit X visibility on prism: |<X_1(t)>| = eta(t) * cos^2(dphi/2) ... wait:
    # Tr(rho(t) X_1) = eta(t) * (cos(dphi/2))^2? Let's compute exact Tr(rho_8 * (X_1 x I x I))!
    x2 = [[0j, 1.0 + 0j], [1.0 + 0j, 0j]]
    i2 = [[1.0 + 0j, 0j], [0j, 1.0 + 0j]]
    x1_op = _kron2(_kron2(x2, i2), i2)
    vis_q_tpi = abs(_trace_product_8x8(quantum_prism_rho8(t_pi, gamma_loc_2k), x1_op))
    vis_q_2tpi = abs(_trace_product_8x8(rho_revival, x1_op))

    # Under Markovian diffusive classical gravity matching the same initial visibility drop rate gamma_diff >= omega_pair,
    # visibility decays monotonically without revival: exp(-omega_pair * 2 * t_pi) = exp(-2*pi) = 0.001867 << 0.8914!
    vis_markov_floor_2tpi = math.exp(-omega_pair * t_revival)

    return {
        "c12_radius_um": r_c12 * 1.0e6,
        "yb173_radius_um": r_yb * 1.0e6,
        "c12_sqrt_theta_ah": sqrt_theta_c12,
        "c12_theta_ah": theta_c12,
        "c12_phi_q_rad": phi_q_c12,
        "c12_theta_over_phi": theta_c12 / phi_q_c12,
        "yb173_sqrt_theta_ah": sqrt_theta_yb,
        "yb173_theta_ah": theta_yb,
        "newtonian_yb_over_c12_ratio": phi_q_yb / phi_q_c12,
        "aziz_sqrt_theta_yb_over_c12_ratio": sqrt_theta_yb / sqrt_theta_c12,
        "aziz_theta_yb_over_c12_ratio": theta_yb / theta_c12,
        "jacobian_det_m_matom": det_m_matom,
        "jacobian_det_m_t_theta": det_m_t_theta,
        "t_revival_s": t_revival,
        "mermin_at_revival_2k": m3_revival,
        "eta_tpi_pow6_diff": abs(m3_revival - (eta_tpi ** 3) ** 2) if False else abs(m3_revival - (eta_2tpi ** 3)),
        "single_qubit_vis_tpi": vis_q_tpi,
        "single_qubit_vis_revival_2tpi": vis_q_2tpi,
        "markov_diffusive_vis_2tpi": vis_markov_floor_2tpi,
    }


def evaluate_active_quantum_clocks(planted_defect: bool = False) -> dict:
    """Result 3: Active internal clock proper-time redshift phases & Zych-Brukner visibility modulation."""
    geom_factor = 1.0 / BENCH_GAP_M - 1.0 / math.hypot(BENCH_GAP_M, BENCH_SPLIT_M)
    omega_pair = 2.0 * (G_NEWTON * BENCH_MASS_KG * BENCH_MASS_KG / HBAR) * geom_factor
    t_pi = math.pi / omega_pair
    omega_compton = BENCH_MASS_KG * C_LIGHT * C_LIGHT / HBAR

    def clock_probe(omega_clk: float) -> dict[str, float]:
        # Source-mass redshift phase from m_src = 10^-14 kg across (D, sqrt(D^2 + dx^2)) over t_pi:
        dphi_src = (G_NEWTON * BENCH_MASS_KG * omega_clk * t_pi / (C_LIGHT * C_LIGHT)) * geom_factor
        vis_src = abs(math.cos(0.5 * dphi_src))
        # Terrestrial redshift phase across vertical split Delta_h = 250 um in Earth's g over t_pi:
        dphi_earth = (EARTH_G_M_S2 * BENCH_SPLIT_M * omega_clk * t_pi) / (C_LIGHT * C_LIGHT)
        vis_earth = abs(math.cos(0.5 * dphi_earth))
        # Exact Equivalence Principle ratio dphi_src / (omega_pair * t_pi / 2) == hbar * omega_clk / (M c^2):
        ep_ratio_phase = dphi_src / (0.5 * omega_pair * t_pi)
        ep_ratio_energy = (HBAR * omega_clk) / (BENCH_MASS_KG * C_LIGHT * C_LIGHT)
        return {
            "omega_clock_rad_s": omega_clk,
            "dphi_source_mass_rad": dphi_src,
            "visibility_source_mass": vis_src,
            "dphi_earth_250um_rad": dphi_earth,
            "visibility_earth_250um": vis_earth,
            "ep_ratio_diff": abs(ep_ratio_phase - ep_ratio_energy),
            "clock_over_compton_ratio": ep_ratio_energy,
        }

    sr87 = clock_probe(OMEGA_SR87_RAD_S)
    th229 = clock_probe(OMEGA_TH229_RAD_S)
    compton = clock_probe(omega_compton)

    # Vertical separation Delta_h_pi in Earth's field where a single 87Sr active clock hits V_clock = 0 (Delta_Phi = pi) in t_pi:
    dh_pi_sr87_m = (math.pi * C_LIGHT * C_LIGHT) / (EARTH_G_M_S2 * OMEGA_SR87_RAD_S * t_pi)

    return {
        "compton_omega_rad_s": omega_compton,
        "sr87_optical": sr87,
        "th229_nuclear": th229,
        "compton_limit": compton,
        "th229_over_sr87_gain": th229["dphi_source_mass_rad"] / sr87["dphi_source_mass_rad"],
        "sr87_earth_null_split_m": dh_pi_sr87_m,
    }


def verify_lean_multipartite_witness(lean_path: Path | None = None, planted_defect: bool = False) -> dict:
    """Audit MultipartiteWitness.lean: comment-stripped forbidden-token scan, strict core-Prelude
    qualified-ID allowlist, optional live `lean` kernel execution, and exact multivariate Fraction checks."""
    target = (
        lean_path
        if lean_path is not None
        else TOOLS_DIR.parent / "skills" / "essays" / "multipartite-witnesses-active-clocks" / "MultipartiteWitness.lean"
    )
    lean_raw = target.read_text(encoding="utf-8")
    if planted_defect:
        lean_raw = lean_raw + "\ntheorem planted_unproven_multipartite_claim : 1 = 2 := by sorry\n"

    no_block = re.sub(r"/--?.*?-/", "", lean_raw, flags=re.S)
    no_comments = re.sub(r"--.*?$", "", no_block, flags=re.M)

    forbidden_tokens = re.findall(r"\b(?:sorry|sorryAx|admit|axiom)\b", no_comments)
    theorem_names = re.findall(r"\btheorem\s+([A-Za-z0-9_]+)", no_comments)
    universal_count = len(re.findall(r"∀|\bforall\b", no_comments))

    allowed_qualified_ids = {
        "Informatico.Essays.ES09",
        "Int.mul_add",
        "Int.mul_assoc",
        "Int.mul_comm",
        "Int.negSucc",
        "Int.neg_mul_neg",
        "Int.ofNat",
        "Nat.mul_add",
        "False.elim",
        "Or.inl",
        "Or.inr",
        "a.m", "b.m", "a.l", "b.l", "a.t", "b.t", "a.i", "b.i",
        "a.theta", "b.theta", "a.n", "b.n", "a.j", "b.j",
        "u.x", "u.y", "u.z", "v.x", "v.y", "v.z", "w.x", "w.y", "w.z",
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

    # Exact multivariate polynomial ring over Fraction mirroring the Lean 4 algebraic spine
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

    # 1. Z_2 parity invariance polynomial: (-z1)(-z2) + (-z2)(-z3) + (-z1)(-z3) - (z1 z2 + z2 z3 + z1 z3) == 0
    z1, z2, z3 = p_var("z1"), p_var("z2"), p_var("z3")
    nz1, nz2, nz3 = p_mul(p_const(-1), z1), p_mul(p_const(-1), z2), p_mul(p_const(-1), z3)
    ising_orig = p_add(p_add(p_mul(z1, z2), p_mul(z2, z3)), p_mul(z1, z3))
    ising_flip = p_add(p_add(p_mul(nz1, nz2), p_mul(nz2, nz3)), p_mul(nz1, nz3))
    z2_ising_poly = p_add(ising_flip, ising_orig, -1)

    # 2. 2-D Brahmagupta-Fibonacci / Lagrange identity used in 3-D Euclidean obstruction:
    #    (uy^2 + uz^2)(vy^2 + vz^2) - (uy*vy + uz*vz)^2 - (uy*vz - uz*vy)^2 == 0
    uy, uz, vy, vz = p_var("uy"), p_var("uz"), p_var("vy"), p_var("vz")
    norm_prod = p_mul(p_add(p_mul(uy, uy), p_mul(uz, uz)), p_add(p_mul(vy, vy), p_mul(vz, vz)))
    dot_sq = p_mul(p_add(p_mul(uy, vy), p_mul(uz, vz)), p_add(p_mul(uy, vy), p_mul(uz, vz)))
    det_sq = p_mul(p_add(p_mul(uy, vz), p_mul(uz, vy), -1), p_add(p_mul(uy, vz), p_mul(uz, vy), -1))
    lagrange_2d_poly = p_add(p_add(norm_prod, dot_sq, -1), det_sq, -1)

    # 3. Cramer elimination identity: (uy*vz - uz*vy)*wy - vz*(uy*wy + uz*wz) + uz*(vy*wy + vz*wz) == 0
    wy, wz = p_var("wy"), p_var("wz")
    cramer_lhs = p_mul(p_add(p_mul(uy, vz), p_mul(uz, vy), -1), wy)
    cramer_rhs = p_add(
        p_mul(vz, p_add(p_mul(uy, wy), p_mul(uz, wz))),
        p_mul(uz, p_add(p_mul(vy, wy), p_mul(vz, wz))),
        -1,
    )
    cramer_2d_poly = p_add(cramer_lhs, cramer_rhs, -1)

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
        "z2_ising_poly_zero": len(z2_ising_poly) == 0,
        "lagrange_2d_poly_zero": len(lagrange_2d_poly) == 0,
        "cramer_2d_poly_zero": len(cramer_2d_poly) == 0,
    }


def evaluate_multipartite_synthesis(planted_defect: bool = False) -> dict:
    """Run all coupled verification layers of Essay ES.09 in < 4 s."""
    return {
        "tripartite_prism": evaluate_tripartite_prism_dynamics(planted_defect=planted_defect),
        "scaling_tomography": evaluate_scaling_and_composition_tomography(planted_defect=planted_defect),
        "active_clocks": evaluate_active_quantum_clocks(planted_defect=planted_defect),
        "lean4_multipartite_spine": verify_lean_multipartite_witness(planted_defect=planted_defect),
    }


# ---------------------------------------------------------------------------
# Bilingual Monograph Specification (EN / es-MX) · Essay ES.09
# ---------------------------------------------------------------------------

ESSAY: dict = {
    "code": CODE,
    "slug": SLUG,
    "plate_slug": PLATE_SLUG,
    "date": "2026-11-11",
    "seo": (
        "Multipartite Gravity Witnesses and Active Clocks",
        "Tripartite Mermin witnesses, 3-body smeared-gravity bounds, ytterbium composition scaling, and proper-time quantum clocks for tabletop gravity.",
        "Testigos Gravitatorios Multipartitos y Relojes",
        "Testigos tripartitos de Mermin, cotas híbridas de 3 cuerpos, escalamiento por composición en iterbio y relojes cuánticos de tiempo propio en mesa.",
    ),
    "kicker_en": "Cross-Scale Essay · ES.09 · Genuine Tripartite Witnesses, Composition Tomography & Active Quantum Clocks",
    "kicker_es": "Ensayo Transescalar · ES.09 · Testigos Tripartitos Genuinos, Tomografía por Composición y Relojes Cuánticos Activos",
    "reading_time_en": "17 min read",
    "reading_time_es": "17 min de lectura",
    "title_en": "Multipartite Witnesses, Scaling Tomography & Active Clocks: Separating Quantum Gravity from Classical Hybrids Beyond Two Bodies",
    "title_es": "Testigos Multipartitos, Tomografía de Escalamiento y Relojes Activos: Cómo Separar la Gravedad Cuántica de Híbridos Clásicos Más Allá de Dos Cuerpos",
    "standfirst_en": (
        "A two-body entanglement witness inside the D = 75 µm parallel quantum island excludes local classical channels "
        "and σ ≤ 33.08 µm Diósi–Penrose hybrids, yet it still leaves three deeper questions open: can gravity generate "
        "irreducible three-body quantum coherence, how can an experimenter falsify higher-order classical-metric matter "
        "vertices whose strength lies 28 orders of magnitude lower, and what distinguishes passive center-of-mass action "
        "phases from relativistic proper-time dilation? Placing 3 interferometers on an equilateral prism of side "
        "D = 75 µm yields an exact Position-Pointer Mermin Law reaching 3.6741 > 2√2 = 2.8284 at T = 2.0 K while "
        "collective 3-body Diósi–Penrose gravity remains pinned at N_{1|23}^hyb = 0 (σ_c = 34.93 µm > 33.08 µm)."
    ),
    "standfirst_es": (
        "Un testigo bipartito dentro de la isla cuántica paralela en D = 75 µm descarta canales clásicos locales e "
        "híbridos de Diósi–Penrose con σ ≤ 33.08 µm, pero deja abiertas tres preguntas mayores: ¿puede la gravedad crear "
        "coherencia cuántica irreducible de tres cuerpos, cómo falsar acoplamientos métricos clásicos de orden superior "
        "situados 28 órdenes de magnitud más abajo, y qué distingue la fase de acción pasiva de la dilatación del tiempo "
        "propio? Situar 3 interferómetros en un prisma equilátero de lado D = 75 µm entrega una Ley de Mermin exacta que "
        "alcanza 3.6741 > 2√2 = 2.8284 a T = 2.0 K mientras Diósi–Penrose de 3 cuerpos permanece en N_{1|23}^hyb = 0 (σ_c = 34.93 µm > 33.08 µm)."
    ),
    "card_dek_en": (
        "Exact 8 × 8 equilateral-prism Mermin witness (3.6741 > 2√2 = 2.8284 at 2.0 K), 34.93 µm 3-body hybrid bound, "
        "165.8× / 27,500× ytterbium composition tomography, active ²²⁹Th clocks, and 9 Lean 4 theorems."
    ),
    "card_dek_es": (
        "Testigo de Mermin exacto 8 × 8 en prisma equilátero (3.6741 > 2√2 = 2.8284 a 2.0 K), cota híbrida de 3 cuerpos en 34.93 µm, "
        "tomografía en iterbio de 165.8× / 27,500×, relojes activos de ²²⁹Th y 9 teoremas en Lean 4."
    ),
    "instrument_kind": "multipartite_witness",
    "instrument": {"kind": "multipartite_witness"},
    "predict": {
        "question_en": (
            "Three 10⁻¹⁴ kg interferometers (Δx = 250 µm) sit at the vertices of a D = 75 µm equilateral prism at "
            "T = 2.0 K (η = 0.9442 at t_π = 2.6120 s). How do environmental dephasing on the Mermin witness "
            "M₃ = X₁X₂X₃ − X₁Z₂Z₃ − Z₁X₂Z₃ − Z₁Z₂X₃ and swapping ¹²C diamond for ¹⁷³Yb at fixed total mass M behave?"
        ),
        "question_es": (
            "Tres interferómetros de 10⁻¹⁴ kg (Δx = 250 µm) ocupan un prisma equilátero de lado D = 75 µm a "
            "T = 2.0 K (η = 0.9442 en t_π = 2.6120 s). ¿Cómo actúan el desfase ambiental sobre el testigo de Mermin "
            "M₃ = X₁X₂X₃ − X₁Z₂Z₃ − Z₁X₂Z₃ − Z₁Z₂X₃ y el cambio de diamante ¹²C a ¹⁷³Yb a masa total M fija?"
        ),
        "choices": [
            {
                "id": "a",
                "en": "Every 3-qubit Mermin term decays as η³, pulling ⟨M₃⟩ below the 2.0 local bound, while Newtonian phase shifts with atomic mass m_atom.",
                "es": "Todo término de 3 qubits decae como η³, bajando ⟨M₃⟩ por debajo del límite local de 2.0, mientras la fase newtoniana cambia con la masa atómica m_atom.",
            },
            {
                "id": "b",
                "en": "⟨M₃⟩ exceeds 2.0, which already suffices to certify genuine tripartite entanglement, and Aziz–Howl classical-gravity coupling is composition-independent.",
                "es": "⟨M₃⟩ supera 2.0, lo cual ya basta para certificar entrelazamiento tripartito genuino, y el acoplamiento clásico de Aziz–Howl es independiente de la composición.",
            },
            {
                "id": "c",
                "en": "Spatial pointers Z_j commute with localization so −X_iZ_jZ_k decays only as η¹, giving ⟨M₃⟩ = 3.6741 > 2√2 = 2.8284 (GTE), while ¹⁷³Yb leaves Δφ_Q invariant (1.0000×) and boosts Aziz–Howl ϑ_AH by 27,500×.",
                "es": "Los punteros espaciales Z_j conmutan con la localización y −X_iZ_jZ_k solo decae como η¹, dando ⟨M₃⟩ = 3.6741 > 2√2 = 2.8284 (GTE), mientras ¹⁷³Yb deja Δφ_Q invariante (1.0000×) y eleva ϑ_AH de Aziz–Howl por 27,500×.",
            },
        ],
        "answer": "c",
        "explain_en": (
            "Because localization acts in the Z spatial-branch basis, Z_j Z_k suffers zero dephasing and −X_i Z_j Z_k "
            "decays linearly as η¹ rather than η³, yielding ⟨M₃(t_π)⟩ = η³ + 3η = 3.6741—clearing not merely the 2.0 "
            "local bound (which biseparable 2-body entanglement can violate up to 2√2 = 2.8284) but certifying Genuine "
            "Tripartite Entanglement. Meanwhile, replacing ¹²C with ¹⁷³Yb at fixed M = 10⁻¹⁴ kg preserves passive "
            "Newtonian phase identically (1.0000×) while amplifying Aziz–Howl √ϑ_AH by 165.8× and ϑ_AH by 27,500×."
        ),
        "explain_es": (
            "Como la localización actúa en la base espacial Z, Z_j Z_k no sufre desfase y −X_i Z_j Z_k decae "
            "linealmente como η¹ en vez de η³, entregando ⟨M₃(t_π)⟩ = η³ + 3η = 3.6741, por encima no solo de 2.0 sino "
            "del umbral biseparable de 2 cuerpos 2√2 = 2.8284. A la vez, cambiar ¹²C por ¹⁷³Yb con M = 10⁻¹⁴ kg fijo "
            "preserva la fase newtoniana (1.0000×) y amplifica √ϑ_AH de Aziz–Howl por 165.8× y ϑ_AH por 27,500×."
        ),
    },
    "sections": [
        {
            "id": "tripartite-prism-witness",
            "h2_en": "I · Exact 8 × 8 Equilateral-Prism Dynamics & The Position-Pointer Mermin Law",
            "h2_es": "I · Dinámica Exacta 8 × 8 en Prisma Equilátero y la Ley de Mermin de Puntero Espacial",
            "short_en": "I · 8 × 8 Mermin GTE Law",
            "short_es": "I · Ley de Mermin 8 × 8",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "In Essays ES.07 and ES.08, stepping two parallel Stern–Gerlach matter-wave interferometers out "
                        "to center-to-center gap D = 75 µm at superposition split Δx = 250 µm and mass m = 10⁻¹⁴ kg "
                        "(Bose et al., 2017; Marletto & Vedral, 2017; Schut et al., 2024) isolated a clean two-qubit "
                        "island above the 73.14 µm smeared-gravity ceiling. Yet bipartite entanglement alone tests only "
                        "pairwise correlations. Placing 3 identical interferometers at the vertices of an equilateral "
                        "triangle of side D = 75 µm in the (x, y) plane—each split by ±Δx / 2 = ±125 µm along z—promotes "
                        "the Hilbert space to an 8 × 8 three-qubit register where every pair shares identical like-branch "
                        "separation r_same = 75.00 µm and unlike-branch separation r_diff = √(D² + Δx²) = 261.01 µm, "
                        "accumulating pairwise entanglement frequency ω_pair = 2(G m² / ħ)(1 / D − 1 / r_diff) = "
                        "1.20275 rad/s and reaching Δφ(t_π) = π at hold time t_π = 2.6120 s."
                    ),
                    "es": (
                        "En los Ensayos ES.07 y ES.08, situar dos interferómetros paralelos de ondas de materia "
                        "Stern–Gerlach a separación D = 75 µm con división Δx = 250 µm y masa m = 10⁻¹⁴ kg (Bose et al., "
                        "2017; Marletto y Vedral, 2017; Schut et al., 2024) aisló una isla limpia de dos qubits sobre el "
                        "techo híbrido de 73.14 µm. Sin embargo, un testigo bipartito solo explora correlaciones por pares. "
                        "Colocar 3 interferómetros idénticos en los vértices de un triángulo equilátero de lado D = 75 µm "
                        "en el plano (x, y) —cada uno dividido ±Δx / 2 = ±125 µm en z— eleva el sistema a un registro de "
                        "8 × 8 donde cada par comparte r_same = 75.00 µm y r_diff = √(D² + Δx²) = 261.01 µm, con frecuencia "
                        "ω_pair = 2(G m² / ħ)(1 / D − 1 / r_diff) = 1.20275 rad/s y Δφ(t_π) = π en t_π = 2.6120 s."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Preparing |+⟩_X^⊗3 = 2⁻³/²(|0⟩ + |1⟩)^⊗3 and evolving under the Ising gravitational propagator "
                        "U(t) = exp[i(Δφ(t) / 4)(Z₁Z₂ + Z₂Z₃ + Z₁Z₃)] alongside single-particle spatial-branch localization "
                        "η = exp(−γ_loc t) uncovers a striking operator asymmetry in the Mermin–Ardehali–Belinskii–Klyshko "
                        "observable M₃ = X₁X₂X₃ − X₁Z₂Z₃ − Z₁X₂Z₃ − Z₁Z₂X₃. Because simultaneous branch inversion "
                        "(z₁, z₂, z₃) ↦ (−z₁, −z₂, −z₃) leaves z₁z₂ + z₂z₃ + z₁z₃ invariant, X₁X₂X₃ commutes identically "
                        "with U(t): it acquires 0 gravitational phase and suffers full three-body dephasing η³. Conversely, "
                        "in −X₁Z₂Z₃, the spatial-branch operators Z₂ and Z₃ commute with position localization while X₁ "
                        "flips z₁ ↦ −z₁: averaging z₂z₃ cos[½ Δφ(z₂ + z₃)] over the 4 equally weighted (z₂, z₃) ∈ {±1}² "
                        "branches yields −½(1 − cos Δφ) damped by only a single factor of η¹!"
                    ),
                    "es": (
                        "Preparar |+⟩_X^⊗3 = 2⁻³/²(|0⟩ + |1⟩)^⊗3 y evolucionar bajo el propagador gravitatorio de Ising "
                        "U(t) = exp[i(Δφ(t) / 4)(Z₁Z₂ + Z₂Z₃ + Z₁Z₃)] junto con localización espacial individual "
                        "η = exp(−γ_loc t) revela una asimetría exacta de operadores en el observable de Mermin "
                        "M₃ = X₁X₂X₃ − X₁Z₂Z₃ − Z₁X₂Z₃ − Z₁Z₂X₃. Como la inversión simultánea "
                        "(z₁, z₂, z₃) ↦ (−z₁, −z₂, −z₃) deja invariante z₁z₂ + z₂z₃ + z₁z₃, X₁X₂X₃ conmuta con U(t): "
                        "acumula fase gravitatoria 0 y sufre amortiguamiento triple η³. En cambio, en −X₁Z₂Z₃ los punteros "
                        "espaciales Z₂ y Z₃ conmutan con la localización en posición mientras X₁ invierte z₁ ↦ −z₁: "
                        "promediar z₂z₃ cos[½ Δφ(z₂ + z₃)] sobre las 4 ramas (z₂, z₃) ∈ {±1}² entrega −½(1 − cos Δφ) amortiguado solo por η¹."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Exact Position-Pointer Mermin Law & Genuine Tripartite Entanglement Thresholds",
                    "label_es": "Ley Exacta de Mermin con Puntero Espacial y Umbrales de Entrelazamiento Tripartito Genuino",
                    "formula": "⟨M₃(t)⟩ = η³ + (3/2) η (1 − cos Δφ(t)) = η³ + 3 η sin²(Δφ(t) / 2)   ;   |⟨M₃⟩|_LHV ≤ 2 < |⟨M₃⟩|_bisep ≤ 2√2 ≈ 2.8284",
                    "note_en": (
                        "Matches full 8 × 8 density-matrix traces to 8.9 × 10⁻¹⁶. At D = 75 µm, Δx = 250 µm, T = 2.0 K "
                        "(P = 2.7 × 10⁻¹⁶ Pa, γ_loc = 0.0220 s⁻¹, η = 0.9442) and t_π = 2.6120 s, ⟨M₃(t_π)⟩ = 3.6741 > 2.8284."
                    ),
                    "note_es": (
                        "Coincide con trazas de matriz de densidad 8 × 8 a 8.9 × 10⁻¹⁶. En D = 75 µm, Δx = 250 µm, T = 2.0 K "
                        "(P = 2.7 × 10⁻¹⁶ Pa, γ_loc = 0.0220 s⁻¹, η = 0.9442) y t_π = 2.6120 s, ⟨M₃(t_π)⟩ = 3.6741 > 2.8284."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Why must a tripartite gravity experiment clear 2√2 ≈ 2.8284 rather than stopping at the classical "
                        "3-local Bell–Mermin bound of 2.0? Because a biseparable quantum state ρ_AB ⊗ ρ_C—in which only "
                        "interferometers 1 and 2 entangle while interferometer 3 sits as an uncoupled spectator—can already "
                        "reach Tsirelson's bound 2√2 on M₃! Conflating 2.0 with 2.8284 would mistake ordinary pairwise "
                        "entanglement for irreducible three-body structure. At T = 2.0 K near the isobaric cryogenic valley "
                        "(P = 2.7 × 10⁻¹⁶ Pa, cited γ_loc = 0.0220 s⁻¹, η = 0.9442 at t_π = 2.6120 s), the equilateral "
                        "prism achieves ⟨M₃(t_π)⟩ = 3.6741 (collective negativity N_{1|23}^Q = 0.4457), surpassing 2.8284 "
                        "by 0.8457 and certifying Genuine Tripartite Entanglement using only two Pauli Stern–Gerlach "
                        "readout bases {X, Z} per mass."
                    ),
                    "es": (
                        "¿Por qué un experimento gravitatorio tripartito debe superar 2√2 ≈ 2.8284 en lugar de conformarse "
                        "con la cota clásica 3-local de Bell–Mermin de 2.0? Porque un estado cuántico biseparable "
                        "ρ_AB ⊗ ρ_C —donde solo se entrelazan los interferómetros 1 y 2 mientras el 3 permanece desacoplado— "
                        "ya puede alcanzar la cota de Tsirelson 2√2 sobre M₃. Confundir 2.0 con 2.8284 tomaría un par "
                        "entrelazado ordinario por coherencia irreducible de tres cuerpos. A T = 2.0 K cerca del valle "
                        "criogénico isobárico (P = 2.7 × 10⁻¹⁶ Pa, γ_loc = 0.0220 s⁻¹, η = 0.9442 en t_π = 2.6120 s), el "
                        "prisma equilátero alcanza ⟨M₃(t_π)⟩ = 3.6741 (negatividad colectiva N_{1|23}^Q = 0.4457), superando "
                        "2.8284 por 0.8457 solo con lecturas Stern–Gerlach en bases {X, Z}."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "This pointer protection carries a decisive operational dividend for cryogenic trap design. Had all "
                        "4 correlators in M₃ been measured in equatorial bases perpendicular to Z, each correlator would "
                        "decay cubically as η³, collapsing Genuine Tripartite Entanglement below 2√2 = 2.8284 as soon as "
                        "η < 0.8909 (γ_loc > 0.0442 s⁻¹ at t_π = 2.6120 s). Because Z_j Z_k commutes with spatial-branch "
                        "localization, η³ + 3η > 2.8284 holds all the way down to η = 0.7829 (γ_loc = 0.0937 s⁻¹), "
                        "expanding the tolerable environmental decoherence rate by 2.12× while requiring only 4 correlator "
                        "settings instead of the 8 settings demanded by a full Svetlichny S₃ polynomial."
                    ),
                    "es": (
                        "Esta protección por puntero espacial aporta un dividendo experimental decisivo para el diseño "
                        "criogénico. Si los 4 correladores de M₃ se midieran en bases ecuatoriales perpendiculares a Z, "
                        "cada término decaería cúbicamente como η³, hundiendo el entrelazamiento tripartito genuino bajo "
                        "2√2 = 2.8284 apenas η < 0.8909 (γ_loc > 0.0442 s⁻¹ en t_π = 2.6120 s). Como Z_j Z_k conmuta con "
                        "la localización espacial, η³ + 3η > 2.8284 se mantiene hasta η = 0.7829 (γ_loc = 0.0937 s⁻¹), "
                        "ampliando la tasa tolerable de decoherencia ambiental por 2.12× con solo 4 configuraciones de "
                        "medición en lugar de las 8 requeridas por un polinomio completo de Svetlichny S₃."
                    ),
                },
            ],
        },
        {
            "id": "dp3-horizon-and-3d-obstruction",
            "h2_en": "II · 3-Body Diósi–Penrose Collective Horizon & The 3-D Orthogonal Null Obstruction",
            "h2_es": "II · Horizonte Colectivo de Diósi–Penrose de 3 Cuerpos y la Obstrucción Ortogonal en 3-D",
            "short_en": "II · 34.93 µm Bound & 3-D Null",
            "short_es": "II · Cota 34.93 µm y Nulo 3-D",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Could collective gravitational pooling from two neighbours allow the σ-smeared classical hybrid "
                        "channel of Trillo and Navascués (2025) to breach the D = 75 µm island when a third mass is added? "
                        "Integrating the exact 3-body Diósi–Penrose master equation on the 8 × 8 prism register proves two "
                        "structural facts. First, the generator satisfies exact trace preservation and spatial no-signalling: "
                        "rotating mass 3's measurement basis locally leaves ρ₁₂ invariant to < 10⁻¹⁵, and decoupling mass 3 "
                        "(m₃ → 0 or R₃ → ∞) reduces Tr₃(ρ₁₂₃^DP) identically to ρ₁₂^DP (< 10⁻¹⁵). Second, pooling two "
                        "neighbours across bipartition 1|23 shifts the short-time partial-transpose threshold from "
                        "√2 b(σ) = a(σ) (1.4142 b = a, giving pairwise σ_c^(2) = 41.12 µm) to the quadratic root "
                        "((√17 − 1) / 2) b(σ) = a(σ) (1.5616 b = a). That collective boost lowers the critical smearing "
                        "width to σ_c^(1|23) = 34.93 µm—closer to the Eöt-Wash recast limit, yet still strictly above "
                        "σ_95 = 33.08 µm! Consequently, at σ_95 = 33.08 µm, N_{1|23}^hyb(t) = 0.0000 for all t ≥ 0, and "
                        "⟨M₃(t)⟩_hyb = ¼ η³(e^{−6(a+2b)τ} + 3e^{−2(3a−2b)τ}) + 3η e^{−2aτ} sin²(2bτ) never exceeds its "
                        "t = 0 product value 1.0000 (log-grid maximum 0.9268 at t = 0.0316 s; secondary oscillation bump "
                        "0.5012 at t = 1.40 s; 0.3227 at t_π = 2.6120 s)."
                    ),
                    "es": (
                        "¿Podría la acción colectiva de dos vecinos permitir que el canal híbrido clásico difuminado en σ "
                        "de Trillo y Navascués (2025) penetre la isla de D = 75 µm al añadir una tercera masa? Integrar la "
                        "ecuación maestra exacta de Diósi–Penrose de 3 cuerpos sobre el registro de 8 × 8 demuestra dos "
                        "hechos estructurales. Primero, el generador cumple conservación exacta de traza y no señalización: "
                        "rotar localmente la base de la masa 3 deja ρ₁₂ invariante a < 10⁻¹⁵, y desacoplar la masa 3 "
                        "(m₃ → 0 o R₃ → ∞) reduce Tr₃(ρ₁₂₃^DP) exactamente a ρ₁₂^DP (< 10⁻¹⁵). Segundo, agrupar dos "
                        "vecinos en la bipartición 1|23 desplaza el umbral de transpuesta parcial desde √2 b(σ) = a(σ) "
                        "(1.4142 b = a, σ_c^(2) = 41.12 µm) hasta ((√17 − 1) / 2) b(σ) = a(σ) (1.5616 b = a). Ello baja la "
                        "anchura crítica a σ_c^(1|23) = 34.93 µm, aún estrictamente por encima de σ_95 = 33.08 µm: en "
                        "σ_95 = 33.08 µm resulta N_{1|23}^hyb(t) = 0.0000 para todo t ≥ 0, y "
                        "⟨M₃(t)⟩_hyb = ¼ η³(e^{−6(a+2b)τ} + 3e^{−2(3a−2b)τ}) + 3η e^{−2aτ} sin²(2bτ) jamás supera su "
                        "valor inicial 1.0000 en t = 0 (máximo en malla 0.9268 en t = 0.0316 s; pico secundario 0.5012 en "
                        "t = 1.40 s; 0.3227 en t_π = 2.6120 s)."
                    ),
                },
                {
                    "type": "analogy",
                    "kicker_en": "Geometric Intuition · Why Three Arms Hit a 3-D Euclidean Ceiling",
                    "kicker_es": "Intuición Geométrica · Por Qué Tres Brazos Chocan con el Techo Euclídeo 3-D",
                    "title_en": "Two Perpendiculars Fit Around a Line; Three Cannot",
                    "title_es": "Dos Perpendiculares Caben Alrededor de una Recta; Tres No",
                    "paras": [
                        (
                            "In Essay ES.07, two interferometers separated along x̂ achieved an all-multipole null control "
                            "by setting splits along ŷ and ẑ—both perpendicular to each other AND perpendicular to x̂. "
                            "With 3 interferometers in ℝ³, no 3 non-zero mutually orthogonal split vectors (u, v, w) can "
                            "all stand perpendicular to a common separation axis d x̂: orthogonality to d x̂ confines all 3 "
                            "vectors to the 2-D (y, z) plane, where at most 2 mutually perpendicular directions exist! "
                            "Naively assigning (x̂, ŷ, ẑ) on a rotated planar D = 75 µm triangle violates s_i ⊥ R_ij and "
                            "leaks 0.4744 rad of spurious pair phase at t_π = 2.6120 s. Instead, stacking masses collinearly "
                            "at (0, 0, 0), (0, 0, D), (0, 0, 2D) with alternating midpoint splits (x̂, ŷ, x̂) locks every "
                            "nearest-neighbour branch distance of pairs (1, 2) and (2, 3) to 192.03 µm identically (0 rad "
                            "nearest-neighbour phase), isolating the 2D = 150 µm next-nearest (1, 3) phase of 1.0701 rad.",
                            "En el Ensayo ES.07, dos interferómetros separados sobre x̂ lograron un control nulo multipolar "
                            "orientando sus divisiones en ŷ y ẑ, perpendiculares entre sí y a x̂. Con 3 interferómetros en "
                            "ℝ³, no existen 3 vectores no nulos mutuamente ortogonales (u, v, w) simultáneamente "
                            "perpendiculares a un eje común d x̂: la ortogonalidad a d x̂ confina los 3 vectores al plano "
                            "2-D (y, z), donde solo caben 2 direcciones perpendiculares. Asignar (x̂, ŷ, ẑ) sobre un "
                            "triángulo plano rotado de D = 75 µm viola s_i ⊥ R_ij y filtra 0.4744 rad de fase espuria en "
                            "t_π = 2.6120 s. En cambio, apilar las masas en (0, 0, 0), (0, 0, D), (0, 0, 2D) con divisiones "
                            "alternadas (x̂, ŷ, x̂) fija cada distancia vecina de (1, 2) y (2, 3) en 192.03 µm (fase vecina "
                            "de 0 rad), aislando en 2D = 150 µm la fase (1, 3) de 1.0701 rad.",
                        ),
                    ],
                },
                {
                    "type": "table",
                    "caption_en": "Table ES.09-A · Tripartite Witness & Horizon Regimes at D = 75 µm, Δx = 250 µm, m = 10⁻¹⁴ kg (t_π = 2.6120 s)",
                    "caption_es": "Tabla ES.09-A · Regímenes Tripartitos de Testigo y Horizonte en D = 75 µm, Δx = 250 µm, m = 10⁻¹⁴ kg (t_π = 2.6120 s)",
                    "headers_en": ["Channel / Regime", "Critical Smearing σ_c", "Mermin ⟨M₃(t_π)⟩", "Collective N_{1|23}", "Operational Verdict"],
                    "headers_es": ["Canal / Régimen", "Anchura Crítica σ_c", "Mermin ⟨M₃(t_π)⟩", "N_{1|23} Colectiva", "Veredicto Operacional"],
                    "rows": [
                        [
                            ("Unitary Quantum (η = 1.0000)", "Cuántico Unitario (η = 1.0000)"),
                            ("0.00 µm (Newtonian 1/r)", "0.00 µm (Newtoniano 1/r)"),
                            ("4.0000", "4.0000"),
                            ("0.5000", "0.5000"),
                            ("Algebraic GTE Maximum (> 2.8284)", "Máximo Algebraico GTE (> 2.8284)"),
                        ],
                        [
                            ("Quantum at 2.0 K (η = 0.9442)", "Cuántico a 2.0 K (η = 0.9442)"),
                            ("0.00 µm (γ_loc = 0.0220 s⁻¹)", "0.00 µm (γ_loc = 0.0220 s⁻¹)"),
                            ("3.6741", "3.6741"),
                            ("0.4457", "0.4457"),
                            ("Genuine Tripartite Entanglement (> 2.8284)", "Entrelazamiento Tripartito Genuino (> 2.8284)"),
                        ],
                        [
                            ("Biseparable Ceiling (AB|C)", "Techo Biseparable (AB|C)"),
                            ("2-Body Tsirelson Bound", "Cota Tsirelson de 2 Cuerpos"),
                            ("2.8284", "2.8284"),
                            ("0.0000 (on C)", "0.0000 (en C)"),
                            ("Maximum Without 3-Body GTE", "Máximo sin GTE de 3 Cuerpos"),
                        ],
                        [
                            ("3-Body Diósi–Penrose (σ = 33.08 µm)", "Diósi–Penrose 3 Cuerpos (σ = 33.08 µm)"),
                            ("34.93 µm (< 41.12 µm pair)", "34.93 µm (< 41.12 µm par)"),
                            ("0.3227 (max 0.9268)", "0.3227 (máx 0.9268)"),
                            ("0.0000", "0.0000"),
                            ("Separable Across All t ≥ 0 (< 2.0000)", "Separable en Todo t ≥ 0 (< 2.0000)"),
                        ],
                    ],
                },
            ],
        },
        {
            "id": "scaling-and-composition-tomography",
            "h2_en": "III · Log-Scaling & Composition Tomography: Disentangling Classical Matter Vertices",
            "h2_es": "III · Tomografía por Escalamiento y Composición: Cómo Separar Vértices Clásicos de Materia",
            "short_en": "III · ¹⁷³Yb Scaling Tomography",
            "short_es": "III · Tomografía con ¹⁷³Yb",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Crossing D = 75 µm eliminates local-operations-and-classical-communication mediators (Marletto & "
                        "Vedral, 2017; Schneider et al., 2026) and σ ≤ 33.08 µm Diósi–Penrose hybrids, while Oppenheim "
                        "et al. (2023) independently constrain Markovian diffusive classical gravity via stochastic momentum "
                        "diffusion. Yet Aziz and Howl (2025) highlighted a distinct theoretical loophole: higher-order "
                        "perturbative vertices coupling quantum-field matter propagators to an unquantized classical metric. "
                        "Precision requires keeping two conventions straight in their Eq. 85: at constant material density "
                        "ρ (where sphere radius scales as R ∝ ρ⁻¹/³ M¹/³), their printed amplitude scales as "
                        "√ϑ_AH = (6 / 25) G² m_atom² M³ R t / (ħ³ D) ∝ m_atom² ρ⁻¹/³ M¹⁰/³ t¹ D⁻¹, whereas its square—the "
                        "dimensionless parameter ϑ_AH = (√ϑ_AH)² tabulated in our dispute kernel—scales as "
                        "m_atom⁴ ρ⁻²/³ M²⁰/³ t² D⁻²."
                    ),
                    "es": (
                        "Cruzar D = 75 µm descarta mediadores LOCC (Marletto y Vedral, 2017; Schneider et al., 2026) e "
                        "híbridos de Diósi–Penrose con σ ≤ 33.08 µm, mientras Oppenheim et al. (2023) acotan la gravedad "
                        "clásica difusiva markoviana mediante difusión de momento. Sin embargo, Aziz y Howl (2025) "
                        "señalaron otra vía teórica: vértices perturbativos de orden superior que acoplan campos cuánticos "
                        "de materia a una métrica clásica sin cuantizar. La precisión exige distinguir dos magnitudes en su "
                        "Ec. 85: a densidad constante ρ (radio R ∝ ρ⁻¹/³ M¹/³), la amplitud impresa escala como "
                        "√ϑ_AH = (6 / 25) G² m_atom² M³ R t / (ħ³ D) ∝ m_atom² ρ⁻¹/³ M¹⁰/³ t¹ D⁻¹, mientras su cuadrado "
                        "ϑ_AH = (√ϑ_AH)² escala como m_atom⁴ ρ⁻²/³ M²⁰/³ t² D⁻²."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Non-Degenerate Composition & Mass-Time Scaling Jacobians (¹²C Diamond vs. ¹⁷³Yb)",
                    "label_es": "Jacobianos No Degenerados de Composición y Masa-Tiempo (Diamante ¹²C frente a ¹⁷³Yb)",
                    "formula": "∂(ln Δφ_Q, ln √ϑ_AH) / ∂(ln M, ln m_atom) = [[2, 0], [10/3, 2]] (det = 4 ≠ 0)   ;   √ϑ_AH(¹⁷³Yb) / √ϑ_AH(¹²C) = 165.8×   (ϑ_AH: 27,500×)",
                    "note_en": (
                        "At M = 10⁻¹⁴ kg, D = 75 µm, t_π = 2.6120 s: ¹²C diamond (12 u, 3500 kg/m³) gives "
                        "√ϑ_AH = 1.11 × 10⁻¹⁴ and ϑ_AH = 1.23 × 10⁻²⁸ against Eq. 42 φ_Q = 2.204 rad (ratio 5.59 × 10⁻²⁹)."
                    ),
                    "note_es": (
                        "En M = 10⁻¹⁴ kg, D = 75 µm, t_π = 2.6120 s: el diamante ¹²C (12 u, 3500 kg/m³) da "
                        "√ϑ_AH = 1.11 × 10⁻¹⁴ y ϑ_AH = 1.23 × 10⁻²⁸ frente a φ_Q = 2.204 rad de la Ec. 42 (razón 5.59 × 10⁻²⁹)."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Even if future matter-wave interferometers approached masses where classical-vertex amplitudes "
                        "became non-negligible, log-scaling and composition tomography separate the mechanisms cleanly. "
                        "Replacing ¹²C diamond (12.0 u, 3500 kg/m³, R = 0.880 µm) with ¹⁷³Yb (173.04 u, 6900 kg/m³, "
                        "R = 0.702 µm) at identical total mass M = 10⁻¹⁴ kg, D = 75 µm, Δx = 250 µm, and t_π = 2.6120 s "
                        "leaves the passive Newtonian quantum phase Δφ_Q = π identically invariant at 1.0000× by the Weak "
                        "Equivalence Principle, while multiplying √ϑ_AH by (173.04 / 12.0)² (3500 / 6900)¹/³ = 165.8× "
                        "(to 1.84 × 10⁻¹²) and ϑ_AH by 27,500× (to 3.39 × 10⁻²⁴)! Simultaneously, doubling hold time to "
                        "t_{2π} = 2 t_π = 5.2240 s (Δφ = 2π) produces a sharp dynamical signature against Oppenheim et al. "
                        "(2023): unitary Newtonian gravity coherently un-entangles the prism back to separability "
                        "(⟨M₃(2t_π)⟩ = η(2t_π)³ = η(t_π)⁶ = 0.7084, reviving single-qubit X visibility from 0.0000 at t_π "
                        "to 0.8914 at 2t_π), whereas any Markovian diffusive channel with rate ≥ ω_pair suppresses "
                        "visibility irreversibly below exp(−2π) = 0.0019."
                    ),
                    "es": (
                        "Incluso si futuros interferómetros alcanzaran masas donde tales vértices clásicos fuesen "
                        "medibles, la tomografía de escalamiento y composición separa ambos mecanismos sin ambigüedad. "
                        "Sustituir diamante ¹²C (12.0 u, 3500 kg/m³, R = 0.880 µm) por ¹⁷³Yb (173.04 u, 6900 kg/m³, "
                        "R = 0.702 µm) con idénticos M = 10⁻¹⁴ kg, D = 75 µm, Δx = 250 µm y t_π = 2.6120 s deja la fase "
                        "cuántica newtoniana Δφ_Q = π exactamente invariante en 1.0000× por el Principio de Equivalencia "
                        "Débil, mientras multiplica √ϑ_AH por (173.04 / 12.0)² (3500 / 6900)¹/³ = 165.8× (hasta "
                        "1.84 × 10⁻¹²) y ϑ_AH por 27,500× (hasta 3.39 × 10⁻²⁴). Además, duplicar el tiempo a "
                        "t_{2π} = 2 t_π = 5.2240 s (Δφ = 2π) distingue el canal unitario frente a Oppenheim et al. (2023): "
                        "la gravedad cuántica desentrelaza coherentemente el prisma (⟨M₃(2t_π)⟩ = η(2t_π)³ = η(t_π)⁶ = "
                        "0.7084, reviviendo la visibilidad individual en X de 0.0000 en t_π a 0.8914 en 2t_π), mientras un "
                        "canal difusivo markoviano con tasa ≥ ω_pair hunde la visibilidad bajo exp(−2π) = 0.0019."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Even within a single crystal species such as ¹²C diamond, scanning total nanocrystal mass M and "
                        "hold time t breaks the degeneracy between Newtonian action and squared classical-vertex coupling "
                        "ϑ_AH without changing material hardware. Because ln Δφ_Q carries exponents (2, 1) in (ln M, ln t) "
                        "whereas ln ϑ_AH carries exponents (20/3, 2) at fixed density, their 2 × 2 log-scaling Jacobian "
                        "evaluates to det [[2, 1], [20/3, 2]] = 4 − 20/3 = −8/3 ≠ 0 (3×-cleared integer determinant "
                        "det [[6, 3], [20, 6]] = −24 ≠ 0). Doubling crystal mass M at halved hold time t / 4 keeps "
                        "Newtonian phase Δφ_Q ∝ M² t constant at 1.0000× while multiplying ϑ_AH ∝ M²⁰/³ t² by "
                        "2²⁰/³ × 4⁻² = 2⁸/³ = 6.3496×, providing an independent single-species log-slope check alongside "
                        "the ¹²C-to-¹⁷³Yb composition swap."
                    ),
                    "es": (
                        "Incluso dentro de una sola especie cristalina como el diamante ¹²C, barrer la masa total M y el "
                        "tiempo de retención t rompe la degeneración entre la acción newtoniana y el acoplamiento cuadrado "
                        "ϑ_AH sin cambiar de material. Como ln Δφ_Q tiene exponentes (2, 1) en (ln M, ln t) mientras "
                        "ln ϑ_AH tiene exponentes (20/3, 2) a densidad constante, su jacobiano logarítmico de 2 × 2 vale "
                        "det [[2, 1], [20/3, 2]] = 4 − 20/3 = −8/3 ≠ 0 (determinante entero escalado 3× igual a "
                        "det [[6, 3], [20, 6]] = −24 ≠ 0). Duplicar la masa M reduciendo el tiempo a t / 4 mantiene "
                        "constante la fase newtoniana Δφ_Q ∝ M² t en 1.0000× mientras multiplica ϑ_AH ∝ M²⁰/³ t² por "
                        "2²⁰/³ × 4⁻² = 2⁸/³ = 6.3496×, brindando una prueba independiente con una sola especie junto al "
                        "intercambio entre ¹²C y ¹⁷³Yb."
                    ),
                },
            ],
        },
        {
            "id": "active-quantum-clocks",
            "h2_en": "IV · Active Quantum Clocks & Relativistic Proper-Time Interferometry",
            "h2_es": "IV · Relojes Cuánticos Activos e Interferometría Relativista de Tiempo Propio",
            "short_en": "IV · Active Proper-Time Clocks",
            "short_es": "IV · Relojes de Tiempo Propio",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Passive QGEM interferometers treat each nanocrystal as an internal structureless rest mass M whose "
                        "branches accumulate Newtonian action phase Δφ_pair / 2 = (M / ħ) ΔΦ_grav t, where "
                        "ΔΦ_grav = G m_src (1 / D − 1 / √(D² + Δx²)). What changes when each delocalized mass also carries "
                        "an active internal two-level quantum clock prepared in (|g⟩ + |e⟩) / √2 at transition frequency "
                        "ω_clock? As shown by Zych, Costa, Pikovski, and Brukner (2011), recently tested in optical-ion "
                        "proper-time protocols by Sorci et al. (2026), and extended to gravitationally induced entanglement "
                        "with massive clocks by Tobar, Aspelmeyer, and Zych (2026), general-relativistic time dilation "
                        "Δτ = ΔΦ_grav t / c² entangles the internal clock state with the spatial path, modulating spatial "
                        "interferometric visibility as V_clock(t) = |cos(ΔΦ_clock / 2)| with "
                        "ΔΦ_clock = (ω_clock / c²) ΔΦ_grav t."
                    ),
                    "es": (
                        "Los interferómetros QGEM pasivos tratan cada nanocristal como una masa en reposo sin estructura M "
                        "cuyas ramas acumulan fase de acción newtoniana Δφ_pair / 2 = (M / ħ) ΔΦ_grav t, con "
                        "ΔΦ_grav = G m_src (1 / D − 1 / √(D² + Δx²)). ¿Qué cambia cuando cada masa deslocalizada porta "
                        "además un reloj cuántico interno activo en (|g⟩ + |e⟩) / √2 a frecuencia ω_clock? Como demostraron "
                        "Zych, Costa, Pikovski y Brukner (2011), exploraron en relojes iónicos ópticos Sorci et al. (2026) y "
                        "extendieron al entrelazamiento gravitatorio con relojes masivos Tobar, Aspelmeyer y Zych (2026), la "
                        "dilatación relativista del tiempo propio Δτ = ΔΦ_grav t / c² entrelaza el reloj interno con la "
                        "trayectoria espacial, modulando la visibilidad según V_clock(t) = |cos(ΔΦ_clock / 2)| con "
                        "ΔΦ_clock = (ω_clock / c²) ΔΦ_grav t."
                    ),
                },
                {
                    "type": "table",
                    "caption_en": "Table ES.09-B · Passive Action Phase vs. Active Internal Clock Proper-Time Probes (t_π = 2.6120 s)",
                    "caption_es": "Tabla ES.09-B · Fase de Acción Pasiva frente a Relojes Internos Activos de Tiempo Propio (t_π = 2.6120 s)",
                    "headers_en": ["Probe Architecture", "Frequency ω (rad/s)", "10⁻¹⁴ kg Source Phase (D = 75 µm)", "Earth g = 9.81 m/s² Phase (250 µm)", "Ratio ħω / (M c²)"],
                    "headers_es": ["Arquitectura Sonda", "Frecuencia ω (rad/s)", "Fase Fuente 10⁻¹⁴ kg (D = 75 µm)", "Fase Tierra g = 9.81 m/s² (250 µm)", "Razón ħω / (M c²)"],
                    "rows": [
                        [
                            ("⁸⁷Sr Optical Clock (429.2 THz)", "Reloj Óptico ⁸⁷Sr (429.2 THz)"),
                            ("2.70 × 10¹⁵", "2.70 × 10¹⁵"),
                            ("4.97 × 10⁻²² rad", "4.97 × 10⁻²² rad"),
                            ("1.92 × 10⁻⁴ rad", "1.92 × 10⁻⁴ rad"),
                            ("3.16 × 10⁻²²", "3.16 × 10⁻²²"),
                        ],
                        [
                            ("²²⁹Th Nuclear Clock (2020.4 THz)", "Reloj Nuclear ²²⁹Th (2020.4 THz)"),
                            ("1.27 × 10¹⁶", "1.27 × 10¹⁶"),
                            ("2.34 × 10⁻²¹ rad", "2.34 × 10⁻²¹ rad"),
                            ("9.05 × 10⁻⁴ rad", "9.05 × 10⁻⁴ rad"),
                            ("1.49 × 10⁻²¹", "1.49 × 10⁻²¹"),
                        ],
                        [
                            ("Passive Rest-Mass Action (M c² / ħ)", "Acción Pasiva de Masa (M c² / ħ)"),
                            ("8.52 × 10³⁶", "8.52 × 10³⁶"),
                            ("1.5708 rad (π / 2)", "1.5708 rad (π / 2)"),
                            ("6.07 × 10¹⁷ rad", "6.07 × 10¹⁷ rad"),
                            ("1.0000", "1.0000"),
                        ],
                    ],
                },
                {
                    "type": "p",
                    "en": (
                        "Dividing the active clock phase by the single-bond Newtonian action phase exposes the exact "
                        "Equivalence Principle bridge ΔΦ_clock / (Δφ_pair / 2) = ħ ω_clock / (M c²): a 10⁻¹⁴ kg crystal "
                        "acts as an intrinsic Compton clock ticking at Ω_C = M c² / ħ = 8.52 × 10³⁶ rad/s, which is why "
                        "center-of-mass entanglement reaches O(1) radians at D = 75 µm whereas a single embedded ⁸⁷Sr "
                        "optical transition (2.70 × 10¹⁵ rad/s) or ²²⁹Th nuclear transition (1.27 × 10¹⁶ rad/s, a 4.71× "
                        "gain) accumulates 4.97 × 10⁻²² rad or 2.34 × 10⁻²¹ rad from a 10⁻¹⁴ kg source. Conversely, in "
                        "Earth's gravitational field (g = 9.80665 m/s²), active clocks shine as differential proper-time "
                        "witnesses: a ⁸⁷Sr clock split across Δh = 250 µm acquires 1.92 × 10⁻⁴ rad in 2.6120 s and hits "
                        "complete Zych–Brukner visibility extinction V_clock = 0 at vertical split Δh_π = 4.09 m, while "
                        "doped crystals hosting N_ens ~ 10⁶ GHZ-entangled ²²⁹Th nuclei near milligram source masses open "
                        "the direct proper-time entanglement regime analyzed by Tobar, Aspelmeyer, and Zych (2026)."
                    ),
                    "es": (
                        "Dividir la fase del reloj activo entre la fase de acción newtoniana revela la identidad exacta del "
                        "Principio de Equivalencia ΔΦ_clock / (Δφ_pair / 2) = ħ ω_clock / (M c²): un cristal de 10⁻¹⁴ kg "
                        "opera como un reloj de Compton intrínseco a Ω_C = M c² / ħ = 8.52 × 10³⁶ rad/s, razón por la cual "
                        "la fase de centro de masa alcanza O(1) radianes en D = 75 µm mientras una sola transición óptica "
                        "de ⁸⁷Sr (2.70 × 10¹⁵ rad/s) o nuclear de ²²⁹Th (1.27 × 10¹⁶ rad/s, ganancia de 4.71×) acumula "
                        "4.97 × 10⁻²² rad o 2.34 × 10⁻²¹ rad ante una fuente de 10⁻¹⁴ kg. En cambio, en el campo terrestre "
                        "(g = 9.80665 m/s²), un reloj de ⁸⁷Sr dividido Δh = 250 µm adquiere 1.92 × 10⁻⁴ rad en 2.6120 s y "
                        "alcanza extinción completa V_clock = 0 en Δh_π = 4.09 m, mientras cristales dopados con "
                        "N_ens ~ 10⁶ núcleos entrelazados de ²²⁹Th junto a masas fuente de miligramos abren el régimen de "
                        "tiempo propio de Tobar, Aspelmeyer y Zych (2026)."
                    ),
                },
                {
                    "type": "bridge",
                    "kicker_en": "Cross-Scale Structural Bridge · Stabilizer Syndromes & Three-Site Allostery",
                    "kicker_es": "Puente Estructural entre Escalas · Síndromes Estabilizadores y Alostería de Tres Sitios",
                    "title_en": "Why Commuting Parity Pointers Protect Fragile Multi-Body Coherence",
                    "title_es": "Por Qué los Punteros de Paridad Conmutativos Protegen la Coherencia Multicuerpo",
                    "paras": [
                        (
                            "The algebraic reason −X_i Z_j Z_k survives environmental localization with single-qubit damping "
                            "η¹ rather than η³ is identical to parity-check syndrome extraction in surface-code quantum "
                            "error correction simulated at scale by Gidney (2021) (Bounty B.02): aligning readout operators "
                            "with the noise basis prevents spectator qubits from multiplying decoherence weight. And at the "
                            "molecular scale, certifying M₃ > 2√2 = 2.8284 mirrors non-additive three-site allosteric "
                            "cooperativity in the CFTR anion channel studied in cystic fibrosis biophysics, where "
                            "simultaneous coupling across two nucleotide-binding domains and the regulatory domain governs "
                            "pore gating in ways pairwise domain marginals cannot capture.",
                            "La razón algebraica por la que −X_i Z_j Z_k sobrevive a la localización ambiental con "
                            "amortiguamiento η¹ en vez de η³ es idéntica a la extracción de síndromes de paridad en códigos "
                            "superficiales simulados a gran escala por Gidney (2021) (Bounty B.02): alinear los punteros "
                            "con la base del ruido evita multiplicar el peso de decoherencia. Y a escala molecular, "
                            "certificar M₃ > 2√2 = 2.8284 refleja la cooperatividad alostérica no aditiva de tres sitios en "
                            "el canal CFTR estudiado en biofísica de fibrosis quística, donde el acoplamiento conjunto de "
                            "dos dominios de unión a nucleótidos y el dominio regulador gobierna la apertura más allá de "
                            "marginales por pares.",
                        ),
                    ],
                },
            ],
        },
        {
            "id": "lean4-multipartite-spine",
            "h2_en": "V · Zero-Sorry Core Lean 4 Certification of the Multipartite & Clock Spine",
            "h2_es": "V · Certificación sin Sorry en Lean 4 Base de la Columna Multipartita y de Relojes",
            "short_en": "V · Lean 4 Proof Spine",
            "short_es": "V · Prueba en Lean 4",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Following the formal digitalization methodology of Tooby-Smith (2025) and Essays ES.06–ES.08, "
                        "MultipartiteWitness.lean encodes 9 zero-sorry theorems and 9 universal quantifiers in pure core "
                        "Lean 4 Prelude with 0 external imports. Theorem 1 (multipartite_clock_si_homogeneity) verifies by "
                        "kernel reduction (rfl) 6 governing SI dimensional identities: Newtonian pair phase, Aziz–Howl "
                        "printed √ϑ_AH amplitude, active clock gravitational redshift phase, the Compton-to-clock "
                        "equivalence ratio, Oppenheim's [D_p Δx² / ħ²] = T⁻¹ spatial decoherence rate with [D_p] = M² L² T⁻³, "
                        "and the proper-time gravitational beat frequency."
                    ),
                    "es": (
                        "Siguiendo la metodología de digitalización formal de Tooby-Smith (2025) y de los Ensayos "
                        "ES.06–ES.08, MultipartiteWitness.lean codifica 9 teoremas sin sorry y 9 cuantificadores universales "
                        "en Lean 4 Prelude puro con 0 importaciones externas. El Teorema 1 (multipartite_clock_si_homogeneity) "
                        "verifica por reducción del núcleo (rfl) 6 identidades dimensionales SI: fase newtoniana por par, "
                        "amplitud impresa √ϑ_AH de Aziz–Howl, fase de corrimiento gravitatorio de reloj activo, razón de "
                        "equivalencia de Compton, tasa de decoherencia espacial [D_p Δx² / ħ²] = T⁻¹ de Oppenheim con "
                        "[D_p] = M² L² T⁻³ y frecuencia de batido gravitatorio de tiempo propio."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Theorems 2, 3, and 4 certify the multipartite Bell hierarchy: mermin_lhv_bound_all_64 proves "
                        "−2 ≤ M₃ ≤ 2 across all 64 deterministic 3-local hidden-variable assignments; "
                        "svetlichny_biseparable_bound_and_quantum_witness proves −4 ≤ S₃ ≤ 4 across all 64 AB|C joint "
                        "assignments while witnessing M₃ = +4 on non-factorable joint correlations; and "
                        "biseparable_threshold_integer_certificate proves 20,000² < 8 × 10,000² < 36,741² (2 < 2√2 < 3.6741). "
                        "Theorems 5 through 9 certify the non-degenerate 3×-cleared scaling determinants (det = 36 ≠ 0 and "
                        "det = −24 ≠ 0), global Z₂ Ising-sum parity invariance, exact 2h² + d² nearest-neighbour equality "
                        "on the collinear (x̂, ŷ, x̂) stack, the general ℤ³ Euclidean three-orthogonal-vector obstruction via "
                        "2-D Lagrange and Cramer elimination, and the 3308 < 3493 < 4112 (33.08 µm < 34.93 µm < 41.12 µm) "
                        "3-body Diósi–Penrose horizon chain—all DERIVED (NOT MEASURED) and checked offline in < 6 s."
                    ),
                    "es": (
                        "Los Teoremas 2, 3 y 4 certifican la jerarquía de Bell multipartita: mermin_lhv_bound_all_64 prueba "
                        "−2 ≤ M₃ ≤ 2 en las 64 asignaciones deterministas 3-locales; "
                        "svetlichny_biseparable_bound_and_quantum_witness prueba −4 ≤ S₃ ≤ 4 en las 64 asignaciones "
                        "conjuntas AB|C exhibiendo M₃ = +4 para correlaciones conjuntas no factorizables; y "
                        "biseparable_threshold_integer_certificate demuestra 20,000² < 8 × 10,000² < 36,741² (2 < 2√2 < "
                        "3.6741). Los Teoremas 5 al 9 certifican los determinantes de escalamiento 3× (det = 36 ≠ 0 y "
                        "det = −24 ≠ 0), la invariancia de paridad Z₂ de Ising, la igualdad exacta 2h² + d² en la pila "
                        "colineal (x̂, ŷ, x̂), la obstrucción euclídea general en ℤ³ vía identidades 2-D de Lagrange y Cramer, "
                        "y la cadena 3308 < 3493 < 4112 (33.08 µm < 34.93 µm < 41.12 µm) de Diósi–Penrose de 3 cuerpos, "
                        "todo DERIVADO (NO MEDIDO) y verificado sin red en < 6 s."
                    ),
                },
            ],
        },
    ],
    "sidenotes": [
        {
            "label_en": "Sidenote 1 · Why Pairwise Marginals Look Unentangled at t_π",
            "label_es": "Nota al Margen 1 · Por Qué las Marginales por Pares Lucen Separables en t_π",
            "en": (
                "At Δφ(t_π) = π on the equilateral prism, tracing out mass 3 multiplies off-diagonal coherences of ρ₁₂ "
                "by cos(Δφ / 2) = cos(π / 2) = 0, turning the 3-qubit GHZ-equivalent state into a separable 2-body "
                "marginal while ⟨M₃(t_π)⟩ = 3.6741 > 2.8284 witnesses full 3-body entanglement."
            ),
            "es": (
                "En Δφ(t_π) = π sobre el prisma equilátero, trazar la masa 3 multiplica las coherencias fuera de la "
                "diagonal de ρ₁₂ por cos(Δφ / 2) = cos(π / 2) = 0, convirtiendo el estado equivalente GHZ de 3 qubits en "
                "una marginal de 2 cuerpos separable mientras ⟨M₃(t_π)⟩ = 3.6741 > 2.8284 certifica el entrelazamiento de 3 cuerpos."
            ),
        },
        {
            "label_en": "Sidenote 2 · Collective (√17 − 1) / 2 Root of 1|23 Partial Transpose",
            "label_es": "Nota al Margen 2 · Raíz Colectiva (√17 − 1) / 2 en la Transpuesta Parcial 1|23",
            "en": (
                "Expanding ρ₁₂₃^{DP, T₁}(τ) to O(τ²) on the equilateral prism yields characteristic polynomial "
                "λ⁴ − 9λ² + 16 = (λ² + λ − 4)(λ² − λ − 4) = 0 for a / b, fixing λ_{1|23} = (√17 − 1) / 2 = 1.5616 > "
                "√2 = 1.4142 and σ_c^(1|23) = 34.93 µm."
            ),
            "es": (
                "Desarrollar ρ₁₂₃^{DP, T₁}(τ) hasta O(τ²) en el prisma equilátero produce el polinomio característico "
                "λ⁴ − 9λ² + 16 = (λ² + λ − 4)(λ² − λ − 4) = 0 para a / b, fijando λ_{1|23} = (√17 − 1) / 2 = 1.5616 > "
                "√2 = 1.4142 y σ_c^(1|23) = 34.93 µm."
            ),
        },
        {
            "label_en": "Sidenote 3 · Printed √ϑ_AH vs. Squared ϑ_AH Convention",
            "label_es": "Nota al Margen 3 · Convención Impresa √ϑ_AH frente al Cuadrado ϑ_AH",
            "en": (
                "Aziz & Howl (2025) Eq. 85 writes √ϑ_AH ∝ m_atom² M³ R t / D, so squaring gives ϑ_AH ∝ m_atom⁴ M⁶ R² t² / D² "
                "(M²⁰/³ at constant density). Swapping ¹²C for ¹⁷³Yb boosts √ϑ_AH by 165.8× and ϑ_AH by 165.83² = 27,500×."
            ),
            "es": (
                "La Ec. 85 de Aziz y Howl (2025) escribe √ϑ_AH ∝ m_atom² M³ R t / D, cuyo cuadrado es "
                "ϑ_AH ∝ m_atom⁴ M⁶ R² t² / D² (M²⁰/³ a densidad fija). Cambiar ¹²C por ¹⁷³Yb eleva √ϑ_AH por 165.8× y "
                "ϑ_AH por 165.83² = 27,500×."
            ),
        },
        {
            "label_en": "Sidenote 4 · Nuclear Isomer Gain in ²²⁹Th vs. ⁸⁷Sr Clocks",
            "label_es": "Nota al Margen 4 · Ganancia del Isómero Nuclear ²²⁹Th frente a ⁸⁷Sr",
            "en": (
                "The vacuum-ultraviolet 8.36 eV nuclear transition of ²²⁹Th (2020.4 THz) ticks 4.71× faster than the "
                "429.2 THz ⁸⁷Sr optical lattice transition and can be doped directly into solid-state host crystals."
            ),
            "es": (
                "La transición nuclear de 8.36 eV en ²²⁹Th (2020.4 THz) oscila 4.71× más rápido que la transición óptica "
                "de 429.2 THz en ⁸⁷Sr y permite dopaje directo dentro de cristales sólidos."
            ),
        },
    ],
    "sources": [
        {
            "id": "ES09-ZYCH2011",
            "citation": "Zych, M., Costa, F., Pikovski, I., & Brukner, Č. — Quantum interferometric visibility as a witness of general relativistic proper time, Nature Communications 2, 505",
            "doi": "10.1038/ncomms1498",
            "year": 2011,
            "role_en": "Establishes interferometric visibility modulation V = |cos(ΔΦ_clock / 2)| from general-relativistic proper time.",
            "role_es": "Establece la modulación de visibilidad V = |cos(ΔΦ_clock / 2)| por dilatación relativista del tiempo propio.",
        },
        {
            "id": "ES09-BOSE2017",
            "citation": "Bose, S., Mazumdar, A., Morley, G. W., Ulbricht, H., Toroš, M., Paternostro, M., Geraci, A. A., Barker, P. F., Kim, M. S., & Milburn, G. — Spin entanglement witness for quantum gravity, Physical Review Letters 119(24), 240401",
            "doi": "10.1103/physrevlett.119.240401",
            "year": 2017,
            "role_en": "Defines the mesoscopic Stern–Gerlach matter-wave protocol generalized here to an 8 × 8 equilateral prism.",
            "role_es": "Define el protocolo mesoscópico Stern–Gerlach generalizado aquí a un prisma equilátero de 8 × 8.",
        },
        {
            "id": "ES09-MARLETTO2017",
            "citation": "Marletto, C., & Vedral, V. — Gravitationally induced entanglement between two massive particles is sufficient evidence of quantum effects in gravity, Physical Review Letters 119(24), 240402",
            "doi": "10.1103/physrevlett.119.240402",
            "year": 2017,
            "role_en": "Proves LOCC classical channels cannot entangle initially separable quantum masses.",
            "role_es": "Demuestra que canales clásicos LOCC no pueden entrelazar masas cuánticas inicialmente separables.",
        },
        {
            "id": "ES09-GIDNEY2021",
            "citation": "Gidney, C. — Stim: a fast stabilizer circuit simulator, Quantum 5, 497",
            "doi": "10.22331/q-2021-07-06-497",
            "year": 2021,
            "role_en": "Anchors the stabilizer parity-check bridge explaining single-qubit η¹ noise protection in −X_i Z_j Z_k.",
            "role_es": "Ancla el puente con síndromes estabilizadores que explica la protección η¹ del término −X_i Z_j Z_k.",
        },
        {
            "id": "ES09-OPPENHEIM2023",
            "citation": "Oppenheim, J., Sparaciari, C., Šoda, B., & Weller-Davies, Z. — Gravitationally induced decoherence vs space-time diffusion: testing the quantum nature of gravity, Nature Communications 14, 7910",
            "doi": "10.1038/s41467-023-43348-2",
            "year": 2023,
            "role_en": "Supplies the Markovian momentum-diffusion bound contrasted against coherent unitary revival at 2t_π.",
            "role_es": "Aporta la cota markoviana de difusión de momento contrastada con la reviviscencia unitaria en 2t_π.",
        },
        {
            "id": "ES09-SCHUT2024",
            "citation": "Schut, M., Geraci, A., Bose, S., & Mazumdar, A. — Micrometer-size spatial superpositions for the QGEM protocol via screening and trapping, Physical Review Research 6(1), 013199",
            "doi": "10.1103/physrevresearch.6.013199",
            "year": 2024,
            "role_en": "Motivates screened parallel interferometer geometries extended to 3-body prisms and collinear stacks.",
            "role_es": "Motiva las geometrías paralelas apantalladas extendidas a prismas de 3 cuerpos y pilas colineales.",
        },
        {
            "id": "ES09-TRILLO2025",
            "citation": "Trillo, D., & Navascués, M. — Diósi–Penrose model of classical gravity predicts gravitationally induced entanglement, Physical Review D 111(12), L121101",
            "doi": "10.1103/physrevd.111.l121101",
            "year": 2025,
            "role_en": "Provides the N-body Diósi–Penrose hybrid master equation solved for 1|23 collective negativity in Section II.",
            "role_es": "Proporciona la ecuación maestra híbrida N-cuerpos de Diósi–Penrose resuelta en la bipartición 1|23.",
        },
        {
            "id": "ES09-AZIZ2025",
            "citation": "Aziz, J., & Howl, R. — Classical theories of gravity produce entanglement, Nature 646, 813–817",
            "doi": "10.1038/s41586-025-09595-7",
            "year": 2025,
            "role_en": "Supplies Eq. 85 higher-order matter-vertex scaling discriminated via ¹²C vs. ¹⁷³Yb composition tomography.",
            "role_es": "Aporta el escalamiento de vértices de materia de la Ec. 85 discriminado mediante tomografía ¹²C frente a ¹⁷³Yb.",
        },
        {
            "id": "ES09-TOOBYSMITH2025",
            "citation": "Tooby-Smith, J. — HepLean: Digitalising high energy physics, Computer Physics Communications 308, 109457",
            "doi": "10.1016/j.cpc.2024.109457",
            "year": 2025,
            "role_en": "Establishes the Lean 4 SI dimensional and algebraic formalization methodology used in MultipartiteWitness.lean.",
            "role_es": "Establece la metodología de formalización dimensional y algebraica en Lean 4 usada en MultipartiteWitness.lean.",
        },
        {
            "id": "ES09-SCHNEIDER2026",
            "citation": "Schneider, M., et al. — A demonstration that classical gravity does not produce entanglement, Classical and Quantum Gravity",
            "doi": "10.1088/1361-6382/ae6f62",
            "year": 2026,
            "role_en": "Demonstrates why classical gravitational fields without quantum mediator degrees of freedom fail to generate operational entanglement.",
            "role_es": "Demuestra por qué campos gravitatorios clásicos sin grados cuánticos mediadores no generan entrelazamiento operacional.",
        },
        {
            "id": "ES09-SORCI2026",
            "citation": "Sorci, J., et al. — Quantum signatures of proper time in optical ion clocks, Physical Review Letters",
            "doi": "10.1103/qhj9-pc2b",
            "year": 2026,
            "role_en": "Demonstrates quantum proper-time interferometric signatures in trapped optical ion clock transitions.",
            "role_es": "Demuestra firmas interferométricas cuánticas de tiempo propio en transiciones ópticas de relojes de iones.",
        },
        {
            "id": "ES09-TOBAR2026",
            "citation": "Tobar, G., Aspelmeyer, M., & Zych, M. — Testing gravitationally-induced-entanglement with massive particles and quantum clocks, arXiv:2611.08313",
            "doi": "10.48550/arxiv.2611.08313",
            "year": 2026,
            "role_en": "Formulates gravitationally induced entanglement protocols coupling delocalized massive particles to quantum clocks.",
            "role_es": "Formula protocolos de entrelazamiento gravitatorio que acoplan partículas masivas deslocalizadas con relojes cuánticos.",
        },
    ],
    "skill_path": "skills/essays/multipartite-witnesses-active-clocks/SKILL.md",
    "verifier_path": "skills/essays/multipartite-witnesses-active-clocks/verify_essay_multipartite_witnesses.py",
    "ai_line_en": (
        "AI contribution to cited primary literature: none. Essay prose, bilingual es-MX twin, 8 × 8 multipartite "
        "quantum & Diósi–Penrose solver, ¹⁷³Yb composition & active-clock kernels, core Lean 4 specification, and "
        "Python verifier were drafted with AI assistance and checked deterministically against cached primary DOIs."
    ),
    "ai_line_es": (
        "Contribución de IA a la literatura primaria citada: ninguna. El ensayo, su gemelo es-MX, el solucionador "
        "multipartito 8 × 8 cuántico y de Diósi–Penrose, los núcleos de ¹⁷³Yb y relojes activos, la especificación en "
        "Lean 4 y el verificador en Python se redactaron con apoyo de IA y se verificaron contra DOIs primarios en caché."
    ),
}
