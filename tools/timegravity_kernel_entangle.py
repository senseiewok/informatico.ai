#!/usr/bin/env python3
"""Gravity-mediated entanglement kernel for the Time & Gravity track (standard library only).

T.05  Does gravity entangle, and would that settle it? The Bose–Marletto–Vedral (BMV) proposal: two masses, each in a
      superposition of two positions, interact only through Newtonian gravity for a time t. Each of the four branches
      (LL, LR, RL, RR) accumulates the phase φ_ij = G m² t / (ħ d_ij), and the two-mass state is entangled exactly
      when the entanglement phase Δφ = φ_LR + φ_RL − φ_LL − φ_RR is not a multiple of 2π; its concurrence is
      |sin(Δφ/2)| and its negativity half that. Three channels are modelled at equal weight:
        quantum   the four Newtonian phases as written (a quantum mediator);
        locc      each mass feels only the mean field of the other (a classical channel: local operations and classical
                  communication, Kafri–Taylor–Milburn 2014): phases of the form α_i + β_j, Δφ = 0, no entanglement;
        disputed  a classical but non-LOCC channel, whose entangling power the 2025 literature disputes; the kernel
                  returns no single number for it, only the interval between the two published answers (0 and the
                  quantum value) so that the page cannot pretend to settle it.
      A local dephasing budget e^{−γt} on each mass turns the pure state into a mixed one; the Peres partial-transpose
      negativity is computed from a Hermitian 4×4 matrix through the real 8×8 embedding and the track's Jacobi solver.
      Planted defect: a LOCC channel that entangles (its phases silently copied from the quantum channel).
"""
from __future__ import annotations

import cmath
import math

from timegravity_kernel import G_NEWTON
from timegravity_kernel_quantum import jacobi_eigen

HBAR = 1.054571817e-34        # J s

# Bose et al. 2017, illustrative geometry (their Fig. 1 scheme): m ~ 1e-14 kg, d ~ 450 µm, Δx ~ 250 µm, τ ~ 2.5 s,
# closest approach d − Δx ≈ 200 µm (Casimir–Polder a tenth of gravity), P = 1e-15 Pa, internal temperature 0.15 K.
BMV_M_KG = 1e-14
BMV_D_M = 450e-6
BMV_DX_M = 250e-6
BMV_T_S = 2.5
BMV_P_PA = 1e-15
BMV_TEMP_K = 0.15
BMV_FALL_TIME_S = 3.5          # τ + 2 τ_acc in the paper's scheme
BMV_PAPER_PHASES = (0.7, -0.2)  # Δφ_RL and Δφ_LR as the paper quotes them ("~")
CHANNELS = ("quantum", "locc", "disputed")
BRANCHES = ("LL", "LR", "RL", "RR")
ENT_TOL = 1e-12
NEG_TOL = 1e-9


# ------------------------------------------------------------------------------------------------- geometry
def branch_separations(d: float, dx: float) -> dict[str, float]:
    """Mass A sits at ∓dx/2 (L/R), mass B at d ∓ dx/2 (L/R); the four centre separations."""
    return {"LL": d, "LR": d + dx, "RL": d - dx, "RR": d}


def newton_phase(m: float, sep: float, t: float, G: float = G_NEWTON) -> float:
    """Phase accumulated by two point masses m a distance sep apart for a time t: G m² t / (ħ sep)."""
    return G * m * m * t / (HBAR * sep)


def branch_phases(m: float, d: float, dx: float, t: float, channel: str = "quantum",
                  G: float = G_NEWTON, planted_defect: bool = False) -> dict[str, float]:
    """The four branch phases for a channel. 'disputed' has no single prediction and raises; callers use the interval."""
    seps = branch_separations(d, dx)
    q = {b: newton_phase(m, seps[b], t, G) for b in BRANCHES}
    if channel == "quantum":
        return q
    if channel == "locc":
        if planted_defect:
            return dict(q)    # the planted defect: a classical channel that carries the quantum phases, and so entangles
        # Mean field: mass A on branch i feels the average of B's two positions, and vice versa; α_i + β_j is a product.
        alpha = {"L": 0.5 * (q["LL"] + q["LR"]), "R": 0.5 * (q["RL"] + q["RR"])}
        beta = {"L": 0.5 * (q["LL"] + q["RL"]), "R": 0.5 * (q["LR"] + q["RR"])}
        return {i + j: 0.5 * (alpha[i] + beta[j]) for i in "LR" for j in "LR"}
    if channel == "disputed":
        raise ValueError("the disputed channel has no single prediction; use disputed_interval()")
    raise ValueError(f"unknown channel {channel!r}")


def entanglement_phase(phases: dict[str, float]) -> float:
    """Δφ = φ_LR + φ_RL − φ_LL − φ_RR, the paper's Δφ_LR + Δφ_RL; zero exactly when the state is a product."""
    return phases["LR"] + phases["RL"] - phases["LL"] - phases["RR"]


def concurrence_closed(dphi: float) -> float:
    """Wootters concurrence of the pure four-branch state: 2|ad − bc| = |sin(Δφ/2)|."""
    return abs(math.sin(0.5 * dphi))


def disputed_interval(m: float, d: float, dx: float, t: float, G: float = G_NEWTON) -> tuple[float, float]:
    """The published answers for a classical non-LOCC channel disagree: no entanglement (Marletto–Vedral, Diósi, Schneider
    et al.) against entanglement (Aziz–Howl, Trillo–Navascués). The kernel reports the interval, never a point."""
    return 0.0, concurrence_closed(entanglement_phase(branch_phases(m, d, dx, t, "quantum", G)))


# ------------------------------------------------------------------------------------------------- states
def four_branch_state(phases: dict[str, float], gamma_t: float = 0.0) -> list[list[complex]]:
    """Density matrix of (1/2) Σ e^{iφ_ij} |ij⟩ after local dephasing by e^{−γt} on each mass (off-diagonals in that
    mass's L/R basis shrink by η = e^{−γt})."""
    eta = math.exp(-gamma_t)
    amp = {b: 0.5 * cmath.exp(1j * phases[b]) for b in BRANCHES}
    rho = [[0j] * 4 for _ in range(4)]
    for r, br in enumerate(BRANCHES):
        for c, bc in enumerate(BRANCHES):
            damp = (eta if br[0] != bc[0] else 1.0) * (eta if br[1] != bc[1] else 1.0)
            rho[r][c] = amp[br] * amp[bc].conjugate() * damp
    return rho


def reduced_a(rho: list[list[complex]]) -> list[list[complex]]:
    """Partial trace over mass B: index (i, j) = 2i + j."""
    out = [[0j, 0j], [0j, 0j]]
    for i in range(2):
        for k in range(2):
            out[i][k] = sum(rho[2 * i + j][2 * k + j] for j in range(2))
    return out


def concurrence_from_purity(rho: list[list[complex]]) -> float:
    """Double entry for a pure two-qubit state: C = sqrt(2 (1 − Tr ρ_A²))."""
    ra = reduced_a(rho)
    purity = sum((ra[i][k] * ra[k][i]).real for i in range(2) for k in range(2))
    return math.sqrt(max(0.0, 2.0 * (1.0 - purity)))


def partial_transpose_b(rho: list[list[complex]]) -> list[list[complex]]:
    out = [[0j] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    out[2 * i + j][2 * k + l] = rho[2 * i + l][2 * k + j]
    return out


def hermitian_eigenvalues(h: list[list[complex]]) -> list[float]:
    """Eigenvalues of a Hermitian n×n matrix through the real symmetric 2n×2n embedding [[A, −B], [B, A]], whose spectrum
    is that of H with every eigenvalue doubled; the Jacobi solver of the track does the rest."""
    n = len(h)
    big = [[0.0] * (2 * n) for _ in range(2 * n)]
    for r in range(n):
        for c in range(n):
            big[r][c] = h[r][c].real
            big[r + n][c + n] = h[r][c].real
            big[r][c + n] = -h[r][c].imag
            big[r + n][c] = h[r][c].imag
    vals, _ = jacobi_eigen(big)
    vals = sorted(vals)
    return [0.5 * (vals[2 * k] + vals[2 * k + 1]) for k in range(n)]


def negativity(rho: list[list[complex]]) -> float:
    """Peres–Horodecki: the sum of the negative eigenvalues of the partial transpose, in magnitude."""
    return sum(-v for v in hermitian_eigenvalues(partial_transpose_b(rho)) if v < 0.0)


def negativity_threshold_gamma_t(phases: dict[str, float], hi: float = 20.0) -> float:
    """The dephasing budget γt at which the negativity reaches zero (bisection); ∞ if it never does within hi."""
    if negativity(four_branch_state(phases, 0.0)) <= NEG_TOL:
        return 0.0
    if negativity(four_branch_state(phases, hi)) > NEG_TOL:
        return float("inf")
    lo = 0.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if negativity(four_branch_state(phases, mid)) > NEG_TOL:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def time_to_full_entanglement(m: float, d: float, dx: float, G: float = G_NEWTON) -> float:
    """The hold time at which Δφ = π and the concurrence reaches 1 for this geometry."""
    rate = abs(entanglement_phase(branch_phases(m, d, dx, 1.0, "quantum", G)))
    return float("inf") if rate <= 0 else math.pi / rate


# ------------------------------------------------------------------------------------------------- verifier
def check_bmv(planted_defect: bool = False) -> dict:
    """The T.05 verifier. Planted defect: a LOCC channel that entangles."""
    m, d, dx, t = BMV_M_KG, BMV_D_M, BMV_DX_M, BMV_T_S
    q = branch_phases(m, d, dx, t, "quantum")
    dphi = entanglement_phase(q)
    c_closed = concurrence_closed(dphi)
    rho = four_branch_state(q)
    c_purity = concurrence_from_purity(rho)
    neg0 = negativity(rho)
    double_entry_ok = abs(c_closed - c_purity) < ENT_TOL
    negativity_ok = abs(neg0 - 0.5 * c_closed) < NEG_TOL
    # The paper's own order-of-magnitude phases, relative to the LL/RR branches.
    paper_rl, paper_lr = BMV_PAPER_PHASES
    ours_rl, ours_lr = q["RL"] - q["LL"], q["LR"] - q["LL"]
    paper_consistent = 0.25 < ours_rl / paper_rl < 4.0 and 0.25 < ours_lr / paper_lr < 4.0 \
        and 0.25 < dphi / (paper_rl + paper_lr) < 4.0
    # Full entanglement at Δφ = π; and nothing at all without gravity.
    t_pi = time_to_full_entanglement(m, d, dx)
    c_at_pi = concurrence_closed(entanglement_phase(branch_phases(m, d, dx, t_pi, "quantum")))
    full_ok = abs(c_at_pi - 1.0) < 1e-9
    knockout_ok = concurrence_closed(entanglement_phase(branch_phases(m, d, dx, t, "quantum", G=0.0))) == 0.0
    # The classical LOCC channel must entangle nothing, on a grid of geometries and times.
    worst_locc = 0.0
    for dd in (300e-6, 450e-6, 900e-6):
        for ddx in (50e-6, 150e-6, 250e-6):
            for tt in (0.5, 2.5, 25.0):
                ph = branch_phases(m, dd, ddx, tt, "locc", planted_defect=planted_defect)
                worst_locc = max(worst_locc, concurrence_closed(entanglement_phase(ph)),
                                 2.0 * negativity(four_branch_state(ph)))
    locc_ok = worst_locc < ENT_TOL
    # The honest LOCC channel still reproduces the mean Newtonian phase of each mass (it is a classical force, not nothing).
    locc_honest = branch_phases(m, d, dx, t, "locc")
    mean_ok = abs(sum(locc_honest.values()) - sum(q.values())) < 1e-9 * sum(q.values())
    # Decoherence budget: the dephasing γt at which the negativity vanishes for this geometry.
    gamma_t_zero = negativity_threshold_gamma_t(q)
    budget_ok = 0.0 < gamma_t_zero < float("inf")
    lo, hi = disputed_interval(m, d, dx, t)
    disputed_ok = lo == 0.0 and abs(hi - c_closed) < ENT_TOL
    defect_rejected = concurrence_closed(entanglement_phase(branch_phases(m, d, dx, t, "locc", planted_defect=True))) > 0.1
    return {
        "phases_rad": q, "entanglement_phase_rad": dphi, "concurrence_closed": c_closed, "concurrence_from_purity": c_purity,
        "negativity": neg0, "paper_phase_rl_rad": ours_rl, "paper_phase_lr_rad": ours_lr, "paper_phases_quoted": list(BMV_PAPER_PHASES),
        "time_to_full_entanglement_s": t_pi, "concurrence_at_pi": c_at_pi, "worst_locc_entanglement": worst_locc,
        "gamma_t_negativity_zero": gamma_t_zero, "disputed_interval": [lo, hi],
        "double_entry_ok": double_entry_ok, "negativity_ok": negativity_ok, "paper_consistent": paper_consistent, "full_ok": full_ok,
        "knockout_ok": knockout_ok, "locc_ok": locc_ok, "mean_ok": mean_ok, "budget_ok": budget_ok, "disputed_ok": disputed_ok,
        "defect_rejected": defect_rejected,
        "ok": double_entry_ok and negativity_ok and paper_consistent and full_ok and knockout_ok and locc_ok and mean_ok
        and budget_ok and disputed_ok and defect_rejected,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(check_bmv(), indent=2, default=str))
