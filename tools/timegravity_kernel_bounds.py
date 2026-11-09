#!/usr/bin/env python3
"""Collapse-bound and counting-argument kernel for the Time & Gravity track (standard library only).

T.06  Does gravity collapse the wave? The Diósi–Penrose (DP) proposal: a superposition of two mass distributions
      decays in a time τ = ħ / E_G, where E_G is the gravitational self-energy of the difference between the two
      distributions. For two displaced uniform spheres E_G has a closed form, checked here against a direct
      numerical integration. The model also predicts spontaneous radiation from charged matter at a rate
      ∝ 1/R0³ (Donadi et al. 2021, Eq. 4); the Gran Sasso counts (576 measured, 506 background, 62 days) give the
      bound R0 > 0.54 × 10⁻¹⁰ m at 95 %, which this kernel recomputes from the counts, and which excludes the
      parameter-free value R0 = 0.05 × 10⁻¹⁰ m. Planted defect: the bound drawn on the wrong side.
T.10  Page's counting argument. For a random pure state on a Hilbert space of dimension m·n (m ≤ n), the average
      entanglement entropy of the m-dimensional part is S(m,n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n) (Page 1993).
      A Haar-random toy on 10 qubits reproduces the Page curve (entropy of the "radiation" rises, turns over at
      half the qubits, and falls), asserted against the closed form, with eigenvalues from a pure-Python Jacobi
      solver. Hawking's line (entropy rising forever) is the planted defect: a toy that never turns over.
"""
from __future__ import annotations

import math
import random

from timegravity_kernel import C, G_NEWTON
from timegravity_kernel_quantum import jacobi_eigen

HBAR = 1.054571817e-34        # J s
E_CHARGE = 1.602176634e-19    # C
EPS0 = 8.8541878128e-12       # F/m

# Gran Sasso (Donadi et al. 2021) numbers, from the paper
GS_MEASURED = 576
GS_BACKGROUND = 506
GS_DAYS = 62.0
GS_A_M3 = 1.8e-29              # z_s(R0) = a / R0³ with a ≈ 1.8e-29 m³ (paper, Eq. 5)
GS_R0_BOUND_M = 0.54e-10       # 95 % lower bound
GS_R0_PARAMFREE_M = 0.05e-10   # Penrose's parameter-free value for the Ge crystal (Debye–Waller)
GS_ROI_KEV = (1000.0, 3800.0)
GE_Z = 32
GE_DENSITY_G_CM3 = 5.323
GE_ATOMIC_MASS_U = 72.63
GE_VOLUME_CM3 = 375.0
XENONNT_R0_90 = 4.9e-10        # XENONnT 2026, 90 % C.L.
XENONNT_R0_95 = 4.5e-10        # XENONnT 2026, 95 % C.L.
DP_TOL = 1e-3


# ------------------------------------------------------------------------------------------------------- T.06
def sphere_interaction_energy(m: float, R: float, d: float) -> float:
    """Magnitude of the Newtonian interaction energy of two identical uniform spheres (mass m, radius R) a distance d apart."""
    if d >= 2.0 * R:
        return G_NEWTON * m * m / d
    lam = d / (2.0 * R)
    return (G_NEWTON * m * m / R) * (6.0 / 5.0 - 2.0 * lam**2 + 1.5 * lam**3 - 0.2 * lam**5)


def dp_self_energy_difference(m: float, R: float, d: float) -> float:
    """E_G for a sphere displaced by d: the self-energy of (ρ₁ − ρ₂) = U_self(ρ₁) + U_self(ρ₂) − ∫ρ₁Φ₂ = 2 U_self − U_int,
    with U_self = (3/5) G m²/R and U_int the full interaction energy (→ G m²/d far apart, → 2 U_self when coincident)."""
    return 2.0 * (0.6 * G_NEWTON * m * m / R) - sphere_interaction_energy(m, R, d)


def dp_collapse_time(m: float, R: float, d: float) -> float:
    e = dp_self_energy_difference(m, R, d)
    return float("inf") if e <= 0 else HBAR / e


def sphere_potential(m: float, R: float, r: float) -> float:
    """Gravitational potential of a uniform sphere (positive magnitude): G m (3R² − r²)/(2R³) inside, G m / r outside."""
    if r >= R:
        return G_NEWTON * m / r
    return G_NEWTON * m * (3.0 * R * R - r * r) / (2.0 * R**3)


def sphere_interaction_energy_numeric(m: float, R: float, d: float, n: int = 48) -> float:
    """Double entry: integrate the potential of sphere 1 over the volume of sphere 2 (midpoint rule, cylindrical symmetry).
    Sphere 2 is centred at (0, 0, d); the integral runs over (ρ, z) with weight 2πρ."""
    rho_density = m / (4.0 / 3.0 * math.pi * R**3)
    h = 2.0 * R / n
    total = 0.0
    for i in range(n):
        z = d - R + (i + 0.5) * h
        rmax = math.sqrt(max(0.0, R * R - (z - d) ** 2))
        if rmax <= 0:
            continue
        nr = max(2, int(n * rmax / R))
        hr = rmax / nr
        for j in range(nr):
            rho = (j + 0.5) * hr
            r = math.sqrt(rho * rho + z * z)
            total += sphere_potential(m, R, r) * 2.0 * math.pi * rho * hr * h
    return rho_density * total


def gran_sasso_signal_counts(R0: float, a: float = GS_A_M3) -> float:
    """Expected spontaneous-radiation counts in the Gran Sasso ROI for a given R0: z_s = a / R0³ (paper, Eq. 5)."""
    return a / R0**3


def poisson_upper_limit(measured: int, background: float, cl: float = 0.95) -> float:
    """Classical upper limit on a Poisson signal s given n measured counts and known background b: the largest s with
    P(N ≤ n | b + s) ≥ 1 − cl, found by bisection with a direct Poisson CDF sum."""
    def cdf(n: int, mu: float) -> float:
        term = math.exp(-mu)
        total = term
        for k in range(1, n + 1):
            term *= mu / k
            total += term
        return total
    lo, hi = 0.0, 10.0 * math.sqrt(measured) + 50.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if cdf(measured, background + mid) >= 1.0 - cl:
            lo = mid
        else:
            hi = mid
    return lo


def gran_sasso_r0_bound(cl: float = 0.95) -> float:
    """R0 lower bound from the counts: z_s(R0) ≤ upper limit on the signal ⇒ R0 ≥ (a / limit)^(1/3)."""
    limit = poisson_upper_limit(GS_MEASURED, GS_BACKGROUND, cl)
    return (GS_A_M3 / limit) ** (1.0 / 3.0)


def dp_rate_prefactor_order_of_magnitude(days: float = GS_DAYS) -> float:
    """Order-of-magnitude recomputation of a (m³) from Donadi et al. Eq. 4, dΓ/dω = (2/3) G e² N² N_a / (π^{3/2} ε0 c³ R0³ ω),
    integrated over the ROI and the acquisition time, with no detection efficiency (so it overestimates a)."""
    atoms = GE_DENSITY_G_CM3 * GE_VOLUME_CM3 / (GE_ATOMIC_MASS_U * 1.66053906660e-24)
    pref = (2.0 / 3.0) * G_NEWTON * E_CHARGE**2 * GE_Z**2 * atoms / (math.pi**1.5 * EPS0 * C**3)
    return pref * math.log(GS_ROI_KEV[1] / GS_ROI_KEV[0]) * days * 86400.0


def check_dp(planted_defect: bool = False) -> dict:
    """The T.06 verifier. Planted defect: the bound drawn on the wrong side (R0 < bound treated as allowed)."""
    # Double entry on E_G for a 1 µm sphere of 1e-14 kg displaced by 0.5, 2 and 5 radii.
    m, R = 1e-14, 1e-6
    max_rel = 0.0
    for d in (0.5 * R, 2.0 * R, 5.0 * R):
        closed = sphere_interaction_energy(m, R, d)
        numeric = sphere_interaction_energy_numeric(m, R, d)
        max_rel = max(max_rel, abs(closed - numeric) / closed)
    far = 1.2 * G_NEWTON * m * m / R
    limits_ok = abs(dp_self_energy_difference(m, R, 1e8 * R) - far) / far < 1e-6 \
        and abs(dp_self_energy_difference(m, R, 0.0)) < 1e-12 * far
    tau = dp_collapse_time(m, R, 2.0 * R)
    r0_bound = gran_sasso_r0_bound(0.95)
    bound_ok = abs(r0_bound - GS_R0_BOUND_M) / GS_R0_BOUND_M < 0.2   # within 20 % of the paper's 0.54e-10 m
    counts_paramfree = gran_sasso_signal_counts(GS_R0_PARAMFREE_M)
    excess_limit = poisson_upper_limit(GS_MEASURED, GS_BACKGROUND, 0.95)
    # Which side is allowed? Correct: R0 >= bound allowed, R0 < bound excluded. Planted: inverted.
    def allowed(r0: float) -> bool:
        return (r0 < r0_bound) if planted_defect else (r0 >= r0_bound)
    paramfree_excluded = not allowed(GS_R0_PARAMFREE_M)
    xenonnt_consistent = allowed(XENONNT_R0_95) and XENONNT_R0_95 > GS_R0_BOUND_M
    a_order = dp_rate_prefactor_order_of_magnitude()
    a_within_decade = 0.1 < a_order / GS_A_M3 < 10.0
    # The planted inversion would call the parameter-free value "allowed"; the correct side excludes it.
    defect_rejected = GS_R0_PARAMFREE_M < r0_bound
    return {"max_rel_err_interaction_energy": max_rel, "limits_ok": limits_ok, "tau_1um_1e-14kg_2R_s": tau,
            "r0_bound_recomputed_m": r0_bound, "r0_bound_paper_m": GS_R0_BOUND_M, "excess_upper_limit_counts": excess_limit,
            "counts_at_paramfree_r0": counts_paramfree, "a_recomputed_no_efficiency_m3": a_order, "a_paper_m3": GS_A_M3,
            "double_entry_ok": max_rel < DP_TOL, "bound_ok": bound_ok, "paramfree_excluded": paramfree_excluded,
            "xenonnt_consistent": xenonnt_consistent, "a_within_decade": a_within_decade, "defect_rejected": defect_rejected,
            "ok": max_rel < DP_TOL and limits_ok and bound_ok and paramfree_excluded and xenonnt_consistent and a_within_decade and defect_rejected}


# ------------------------------------------------------------------------------------------------------- T.10
PAGE_N_QUBITS = 10
PAGE_SAMPLES = 8
PAGE_TOL_NATS = 0.03
PAGE_SEED = 20261109


def page_average_entropy(m: int, n: int) -> float:
    """Page 1993 (average entropy of a subsystem): S(m,n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n) for m ≤ n, in nats."""
    if m > n:
        m, n = n, m
    return sum(1.0 / k for k in range(n + 1, m * n + 1)) - (m - 1) / (2.0 * n)


def haar_random_state(dim: int, rng: random.Random) -> list[complex]:
    v = [complex(rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)) for _ in range(dim)]
    norm = math.sqrt(sum(abs(x) ** 2 for x in v))
    return [x / norm for x in v]


def reduced_density_matrix(psi: list[complex], a: int, n_qubits: int) -> list[list[complex]]:
    """Trace out the last (n − a) qubits of a pure state on n qubits; the first a qubits index the rows."""
    m = 2 ** a
    nb = 2 ** (n_qubits - a)
    rho = [[0j] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            s = 0j
            for b in range(nb):
                s += psi[i * nb + b] * psi[j * nb + b].conjugate()
            rho[i][j] = s
    return rho


def von_neumann_entropy(rho: list[list[complex]]) -> float:
    """Entropy in nats from the eigenvalues of a Hermitian matrix, via the real 2m×2m embedding and Jacobi (eigenvalues pair up)."""
    m = len(rho)
    M = [[0.0] * (2 * m) for _ in range(2 * m)]
    for r in range(m):
        for c in range(m):
            M[r][c] = rho[r][c].real
            M[r][c + m] = -rho[r][c].imag
            M[r + m][c] = rho[r][c].imag
            M[r + m][c + m] = rho[r][c].real
    vals, _ = jacobi_eigen(M, tol=1e-13)
    vals = sorted(vals)
    s = 0.0
    for lam in vals[::2]:   # each eigenvalue of ρ appears twice in the embedding
        if lam > 1e-14:
            s -= lam * math.log(lam)
    return s


def page_curve_toy(n_qubits: int = PAGE_N_QUBITS, samples: int = PAGE_SAMPLES, seed: int = PAGE_SEED) -> dict:
    """Radiation entropy against emitted qubits a = 1..n−1 for Haar-random pure states, next to Page's closed form and Hawking's line."""
    rng = random.Random(seed)
    curve = []
    states = [haar_random_state(2 ** n_qubits, rng) for _ in range(samples)]
    for a in range(1, n_qubits):
        m, n = 2 ** a, 2 ** (n_qubits - a)
        if m <= n:
            ents = [von_neumann_entropy(reduced_density_matrix(psi, a, n_qubits)) for psi in states]
        else:
            # Entropy is symmetric between the two parts: compute on the smaller side.
            ents = [von_neumann_entropy(reduced_density_matrix(psi, n_qubits - a, n_qubits)) for psi in states]
        mean = sum(ents) / len(ents)
        curve.append({"a": a, "toy_mean_nats": mean, "page_nats": page_average_entropy(m, n), "hawking_line_nats": a * math.log(2.0),
                      "max_possible_nats": min(a, n_qubits - a) * math.log(2.0)})
    return {"n_qubits": n_qubits, "samples": samples, "seed": seed, "curve": curve}


def check_page_curve(planted_defect: bool = False) -> dict:
    """The T.10 verifier. Planted defect: a non-unitary toy whose radiation entropy follows Hawking's line and never turns over."""
    toy = page_curve_toy()
    curve = toy["curve"]
    if planted_defect:
        for c in curve:
            c["toy_mean_nats"] = c["hawking_line_nats"]
    max_dev = max(abs(c["toy_mean_nats"] - c["page_nats"]) for c in curve)
    half = len(curve) // 2
    peak = max(c["toy_mean_nats"] for c in curve)
    turns_over = curve[-1]["toy_mean_nats"] < 0.5 * peak and abs(curve[half]["toy_mean_nats"] - peak) < 1e-9 + 0.05 * peak
    symmetric = all(abs(curve[i]["toy_mean_nats"] - curve[len(curve) - 1 - i]["toy_mean_nats"]) < 2 * PAGE_TOL_NATS for i in range(half))
    matches_page = max_dev < PAGE_TOL_NATS
    bad = [c["hawking_line_nats"] for c in curve]
    defect_rejected = not (bad[-1] < 0.5 * max(bad))
    return {"n_qubits": toy["n_qubits"], "samples": toy["samples"], "max_dev_from_page_nats": max_dev,
            "peak_nats": peak, "final_nats": curve[-1]["toy_mean_nats"], "page_half_nats": curve[half]["page_nats"],
            "matches_page": matches_page, "turns_over": turns_over, "symmetric": symmetric, "defect_rejected": defect_rejected,
            "curve": curve, "ok": matches_page and turns_over and symmetric and defect_rejected}
