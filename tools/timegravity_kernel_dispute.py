#!/usr/bin/env python3
"""Dispute kernel for Time & Gravity · T.05 (standard library only): the hatched band gets computed edges.

The T.05 page carries a disputed channel, "classical but not LOCC", as an interval between two published answers. This kernel
computes what each side's own model predicts for the two-masses-in-two-places experiment, so that the band's edges are numbers
with named assumptions instead of a literature interval. It picks no side: every number is labelled with the model it comes from.

Lower edge · Kafri–Taylor–Milburn 2014 (NJP 16, 065020). Gravity as a classical channel: each mass's position is continuously
    measured and the record drives a classical force on the other. Linearised coupling K = 2 G m² / d³; the channel reproduces the
    Newtonian phase and adds position decoherence at the rate (K/2ħ)(x − x')², "minimal in the sense that, if it were any smaller,
    evolution ... would immediately entangle". In the four-branch basis that is a local dephasing γ_K = K Δx² / (2ħ) per mass,
    i.e. γ_K t = Δφ_lin / 2. The kernel checks that the T.05 dephasing threshold γt_zero (where the negativity vanishes) is that
    value in the small-split limit: the classical channel sits exactly on the edge of entangling nothing.

Upper edge · Trillo & Navascués 2025 (PRD 111, L121101). The Diósi–Penrose model written as hybrid classical-gravity /
    quantum-matter dynamics with the mass density smeared over a width σ, the model's only free parameter (the R0 that T.06
    bounded from below). With H = 0 their master equation integrates to ⟨x|ρ(t)|y⟩ = exp[(G/2ħ) g(x,y) t] ⟨x|ρ(0)|y⟩ with
        g(x,y) = Σ_jk m_j m_k [ (i−1) f(x_j,x_k) + (−i−1) f(y_j,y_k) + 2 f(x_j,y_k) ],   f(z,z') = erf(|z−z'|/2σ)/|z−z'|,  f(z,z) = 1/(σ√π).
    Its imaginary part is the smeared Newtonian pair phase; its real part is the DP decoherence, with cross terms between the two
    masses. The kernel integrates the four-branch state, computes the Peres negativity, and reproduces the paper's two statements.
    First, entanglement is generated iff the nearest separation is below a critical d_c proportional to σ: the paper quotes
    d_c ≈ 0.8501 σ in its text and 0.850872 σ in its appendix; the kernel's small-split root of their analytic criterion E_− (Eq. 20)
    is 0.8508 σ, checked against the appendix value within 1e-3, and the master equation's negativity agrees with E_− on d_c within
    1 %. Second, for their Fig. 3 geometry (10⁻¹⁵ kg, split 23 µm, separation 24 µm,
    σ = 50 … 250 µm) the entanglement is absent at σ = 50 µm and otherwise transient, lasting longer than a day for the larger σ.

Planted defect: the DP decoherence dropped (Re g := 0) while the phases are kept. The channel then entangles for every σ and
    every separation, there is no critical separation, and the d_c check fails, as it must.
"""
from __future__ import annotations

import cmath
import math

from timegravity_kernel import G_NEWTON
from timegravity_kernel_entangle import (
    BMV_D_M, BMV_DX_M, BMV_M_KG, BMV_T_S, BRANCHES, HBAR, branch_phases, entanglement_phase, four_branch_state, negativity,
    negativity_threshold_gamma_t,
)

# Trillo & Navascués 2025, Fig. 3 (lengths and masses from Van De Kamp et al. 2020)
TN_M_KG = 1e-15
TN_L_M = 23e-6            # superposition size (their L)
TN_D_M = 24e-6            # nearest separation (their d)
TN_SIGMAS_M = (50e-6, 75e-6, 100e-6, 250e-6)
TN_DC_OVER_SIGMA_TEXT = 0.8501
TN_DC_OVER_SIGMA_APPENDIX = 0.850872
DAY_S = 86400.0
DISPUTE_TOL = 1e-3


# ------------------------------------------------------------------------------------------------- Trillo–Navascués
def f_tilde(z: float, sigma: float) -> float:
    """erf(z/2σ)/z, with the finite limit 1/(σ√π) at z = 0 (their Eq. 14)."""
    return math.erf(z / (2.0 * sigma)) / z if z > 0.0 else 1.0 / (sigma * math.sqrt(math.pi))


def tn_g(x: tuple[float, float], y: tuple[float, float], masses: tuple[float, float], sigma: float, planted_defect: bool = False) -> complex:
    """g(x,y) of their Eqs. 12–14 for two particles at 1-D positions x = (x₁, x₂) in the ket branch and y in the bra branch."""
    total = 0j
    for j in range(2):
        for k in range(2):
            mm = masses[j] * masses[k]
            total += mm * ((1j - 1.0) * f_tilde(abs(x[j] - x[k]), sigma)
                           + (-1j - 1.0) * f_tilde(abs(y[j] - y[k]), sigma)
                           + 2.0 * f_tilde(abs(x[j] - y[k]), sigma))
    if planted_defect:
        total = complex(0.0, total.imag)   # decoherence dropped: a channel that keeps the phases and forgets its own noise
    return total


def collinear_branches(split: float, nearest: float) -> list[tuple[float, float]]:
    """Mass A at {−L, 0}, mass B at {d, d + L}: nearest separation d, farthest d + 2L; branch order LL, LR, RL, RR."""
    a_pos = (-split, 0.0)
    b_pos = (nearest, nearest + split)
    return [(a, b) for a in a_pos for b in b_pos]


def tn_state(split: float, nearest: float, masses: tuple[float, float], sigma: float, t: float,
             planted_defect: bool = False) -> list[list[complex]]:
    """ρ(t) on the four branches from an equal superposition at t = 0, H = 0 (their Eq. 24)."""
    br = collinear_branches(split, nearest)
    rho = [[0j] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            rho[r][c] = 0.25 * cmath.exp((G_NEWTON / (2.0 * HBAR)) * tn_g(br[r], br[c], masses, sigma, planted_defect) * t)
    return rho


def tn_negativity(split: float, nearest: float, m: float, sigma: float, t: float, planted_defect: bool = False) -> float:
    return negativity(tn_state(split, nearest, (m, m), sigma, t, planted_defect))


def tn_entanglement_phase(split: float, nearest: float, m: float, sigma: float, t: float) -> float:
    """Δφ of the model's unitary part: (G/2ħ) t [Im g(LR,LR→) …], read off the branch phases Im g(x, x₀) against a reference."""
    br = collinear_branches(split, nearest)
    phases = [(G_NEWTON / (2.0 * HBAR)) * t * tn_g(b, br[0], (m, m), sigma).imag for b in br]   # relative to LL
    return phases[1] + phases[2] - phases[0] - phases[3]


def tn_potential_ratio(d: float, sigma: float) -> float:
    """The model's pair potential over Newton's at separation d: erf(d/2σ). Below about 2σ the smearing softens gravity itself."""
    return math.erf(d / (2.0 * sigma))


def tn_e_minus(m: float, split: float, nearest: float, sigma: float) -> float:
    """Their Eq. 20: the dynamics is entangling when E_− < 0."""
    L, d, s = split, nearest, sigma
    return (G_NEWTON * m * m / (2.0 * HBAR)) * (
        1.0 / (math.sqrt(math.pi) * s) - f_tilde(L, s)
        - (1.0 / math.sqrt(2.0)) * abs(f_tilde(d + 2.0 * L, s) + f_tilde(d, s) - 2.0 * f_tilde(L + d, s))
    )


def tn_critical_separation_from_e_minus(sigma: float, split: float, m: float = TN_M_KG) -> float | None:
    """Largest nearest separation with E_− < 0 (bisection); None when the dynamics never entangles."""
    lo, hi = 1e-12, 20.0 * sigma
    if tn_e_minus(m, split, lo, sigma) >= 0.0:
        return None
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if tn_e_minus(m, split, mid, sigma) < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def tn_critical_separation_from_negativity(sigma: float, split: float, m: float = TN_M_KG, planted_defect: bool = False) -> float | None:
    """Double entry: the largest nearest separation at which the master equation's negativity grows from zero."""
    rate = G_NEWTON * m * m / (HBAR * sigma)
    t_small = 1e-4 / rate

    def entangling(d: float) -> bool:
        return tn_negativity(split, d, m, sigma, t_small, planted_defect) > 1e-14

    lo, hi = 1e-12, 20.0 * sigma
    if not entangling(lo):
        return None
    if entangling(hi):
        return float("inf")   # no critical separation: entangles everywhere (the planted defect)
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if entangling(mid):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def tn_critical_sigma(m: float, split: float, nearest: float) -> float:
    """Smallest σ for which the dynamics entangles this geometry (E_− < 0); E_− is negative for every large σ (the smearing
    removes the decoherence faster than the phase), so the bisection runs between a tiny σ and a metre."""
    lo, hi = 1e-9, 1.0
    assert tn_e_minus(m, split, nearest, hi) < 0.0
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if tn_e_minus(m, split, nearest, mid) < 0.0:
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


def tn_survival(split: float, nearest: float, m: float, sigma: float, planted_defect: bool = False) -> dict:
    """Negativity against time on a log grid: peak, its time, and the last time with N > 0 (None when never entangled)."""
    best_t, best_n, last_t = None, 0.0, None
    for k in range(-12, 44):
        t = 10.0 ** (k / 4.0)
        n = tn_negativity(split, nearest, m, sigma, t, planted_defect)
        if n > best_n:
            best_t, best_n = t, n
        if n > 1e-9:
            last_t = t
    return {"peak_negativity": best_n, "peak_time_s": best_t, "last_entangled_time_s": last_t}


# ------------------------------------------------------------------------------------------------- Kafri–Taylor–Milburn
def ktm_coupling(m: float, d: float) -> float:
    """K = 2 G m² / d³ (their Eq. 5), the linearised gravitational spring between the two masses."""
    return 2.0 * G_NEWTON * m * m / d**3


def ktm_dephasing_rate(m: float, d: float, dx: float) -> float:
    """Position decoherence at (K/2ħ)(x − x')² (their Eq. 21) for a superposition of size Δx: K Δx² / (2ħ), per mass."""
    return ktm_coupling(m, d) * dx * dx / (2.0 * HBAR)


def ktm_linear_phases(m: float, d: float, dx: float, t: float) -> dict[str, float]:
    """The channel's own Hamiltonian K x₁x₂ on the four branches (x = ∓Δx/2): LL and RR carry −K Δx² t/(4ħ), LR and RL +K Δx² t/(4ħ)."""
    phi = ktm_coupling(m, d) * dx * dx * t / (4.0 * HBAR)
    return {"LL": -phi, "RR": -phi, "LR": phi, "RL": phi}


def ktm_edge(m: float, d: float, dx: float, t: float) -> dict:
    """The classical channel's prediction for the four-branch experiment, two ways: its own linearised model (spring phases plus
    the minimal dephasing, which entangles nothing to first order), and the same dephasing applied to the exact Newtonian phases
    (which, for a split that is not small against the separation, leaves some entanglement because the linearisation underestimates
    the phase)."""
    gt = ktm_dephasing_rate(m, d, dx) * t
    lin = ktm_linear_phases(m, d, dx, t)
    q = branch_phases(m, d, dx, t, "quantum")
    small = 1e-3 * d
    lin_small = ktm_linear_phases(m, d, small, t)
    return {"gamma_t": gt, "linear_model_entanglement_phase_rad": entanglement_phase(lin), "exact_entanglement_phase_rad": entanglement_phase(q),
            "linear_model_negativity": negativity(four_branch_state(lin, gt)),
            "linear_model_negativity_small_split": negativity(four_branch_state(lin_small, ktm_dephasing_rate(m, d, small) * t)),
            "exact_phases_with_ktm_dephasing_negativity": negativity(four_branch_state(q, gt))}


# ------------------------------------------------------------------------------------------------- verifier
def check_dispute(planted_defect: bool = False) -> dict:
    # 1. Trillo–Navascués: critical separation in the small-split limit, analytic criterion against the master equation.
    sigma = 50e-6
    dc_e_small = tn_critical_separation_from_e_minus(sigma, sigma * 1e-4)
    dc_ratio_e = dc_e_small / sigma if dc_e_small else None
    dc_e_mid = tn_critical_separation_from_e_minus(sigma, sigma / 500.0)
    dc_n_mid = tn_critical_separation_from_negativity(sigma, sigma / 500.0, planted_defect=planted_defect)
    dc_paper_ok = dc_ratio_e is not None and abs(dc_ratio_e - TN_DC_OVER_SIGMA_APPENDIX) / TN_DC_OVER_SIGMA_APPENDIX < DISPUTE_TOL
    dc_double_entry_ok = (dc_e_mid is not None and dc_n_mid is not None and math.isfinite(dc_n_mid)
                          and abs(dc_n_mid - dc_e_mid) / dc_e_mid < 1e-2)
    # 2. Their Fig. 3 geometry: no entanglement at σ = 50 µm, transient entanglement otherwise, longer than a day for the largest σ.
    fig3 = {}
    for s in TN_SIGMAS_M:
        surv = tn_survival(TN_L_M, TN_D_M, TN_M_KG, s, planted_defect)
        surv["e_minus_J_per_s"] = tn_e_minus(TN_M_KG, TN_L_M, TN_D_M, s)
        fig3[f"{s * 1e6:.0f}um"] = surv
    fig3_ok = (fig3["50um"]["last_entangled_time_s"] is None and fig3["50um"]["e_minus_J_per_s"] > 0.0
               and all(fig3[k]["last_entangled_time_s"] is not None and fig3[k]["e_minus_J_per_s"] < 0.0 for k in ("75um", "100um", "250um"))
               and fig3["250um"]["last_entangled_time_s"] > DAY_S)
    # 3. The 2017 geometry on this model: with a split of 250 µm the critical σ is found from E_− (bisection in σ); above it the
    #    entanglement exists but builds slowly; and as σ → ∞ the model's decoherence vanishes and it becomes the quantum channel.
    nearest_2017 = BMV_D_M - BMV_DX_M
    sigma_c_2017 = tn_critical_sigma(BMV_M_KG, BMV_DX_M, nearest_2017)
    tn_2017 = {}
    for label, s in (("half_sigma_c", 0.5 * sigma_c_2017), ("twice_sigma_c", 2.0 * sigma_c_2017), ("ten_sigma_c", 10.0 * sigma_c_2017)):
        surv = tn_survival(BMV_DX_M, nearest_2017, BMV_M_KG, s, planted_defect)
        surv["sigma_m"] = s
        surv["negativity_at_2p5_s"] = tn_negativity(BMV_DX_M, nearest_2017, BMV_M_KG, s, BMV_T_S, planted_defect)
        tn_2017[label] = surv
    # The smearing acts on the interaction too: the pair potential is G m² erf(d/2σ)/d, so for σ → 0 the model's phases are the
    # Newtonian ones of the T.05 kernel (checked here), while for σ ≫ d both the phase and the decoherence fall as σ⁻³.
    dphi_newton = entanglement_phase(branch_phases(BMV_M_KG, BMV_D_M, BMV_DX_M, BMV_T_S, "quantum"))
    dphi_tn_tiny_sigma = tn_entanglement_phase(BMV_DX_M, nearest_2017, BMV_M_KG, 1e-9, BMV_T_S)
    potential_ratio_fig3 = {f"{s * 1e6:.0f}um": tn_potential_ratio(TN_D_M, s) for s in TN_SIGMAS_M}
    tn_2017_ok = (tn_2017["half_sigma_c"]["last_entangled_time_s"] is None and tn_2017["twice_sigma_c"]["last_entangled_time_s"] is not None
                  and abs(dphi_tn_tiny_sigma - dphi_newton) / abs(dphi_newton) < 1e-6
                  and tn_2017["twice_sigma_c"]["negativity_at_2p5_s"] < 1e-3)
    # 4. Kafri–Taylor–Milburn: the dephasing threshold of the T.05 kernel is the channel's minimal rate in the small-split limit,
    #    and the channel's own linearised model (spring phases plus its minimal dephasing) entangles nothing to first order.
    ratios = []
    for dx in (BMV_DX_M, 50e-6, 10e-6, 2e-6):
        q = branch_phases(BMV_M_KG, BMV_D_M, dx, BMV_T_S, "quantum")
        gt_zero = negativity_threshold_gamma_t(q, hi=50.0)
        gt_ktm = ktm_dephasing_rate(BMV_M_KG, BMV_D_M, dx) * BMV_T_S
        ratios.append({"dx_um": dx * 1e6, "gamma_t_zero": gt_zero, "gamma_t_ktm": gt_ktm, "ratio": gt_zero / gt_ktm if gt_ktm > 0 else None})
    ktm_ok = abs(ratios[-1]["ratio"] - 1.0) < 1e-2 and all(r["ratio"] is not None for r in ratios)
    ktm_2017 = ktm_edge(BMV_M_KG, BMV_D_M, BMV_DX_M, BMV_T_S)
    ktm_edge_ok = ktm_2017["linear_model_negativity"] < 1e-3 and ktm_2017["linear_model_negativity_small_split"] < 1e-9
    defect_rejected = tn_critical_separation_from_negativity(sigma, sigma / 500.0, planted_defect=True) == float("inf")
    return {
        "tn_dc_over_sigma_e_minus_small_split": dc_ratio_e, "tn_dc_paper_text": TN_DC_OVER_SIGMA_TEXT, "tn_dc_paper_appendix": TN_DC_OVER_SIGMA_APPENDIX,
        "tn_dc_e_minus_split_sigma_over_500": dc_e_mid, "tn_dc_negativity_split_sigma_over_500": dc_n_mid,
        "tn_fig3": fig3, "tn_2017_nearest_m": nearest_2017, "tn_2017_sigma_c_m": sigma_c_2017, "tn_2017_by_sigma": tn_2017,
        "tn_phase_tiny_sigma_rad": dphi_tn_tiny_sigma, "newton_phase_rad": dphi_newton, "tn_potential_ratio_fig3": potential_ratio_fig3,
        "ktm_threshold_ratios": ratios, "ktm_2017": ktm_2017,
        "dc_paper_ok": dc_paper_ok, "dc_double_entry_ok": dc_double_entry_ok, "fig3_ok": fig3_ok, "tn_2017_ok": tn_2017_ok,
        "ktm_ok": ktm_ok, "ktm_edge_ok": ktm_edge_ok, "defect_rejected": defect_rejected,
        "ok": dc_paper_ok and dc_double_entry_ok and fig3_ok and tn_2017_ok and ktm_ok and ktm_edge_ok and defect_rejected,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(check_dispute(), indent=2, default=str))
