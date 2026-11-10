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
    negativity_threshold_gamma_t, time_to_full_entanglement,
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
             planted_defect: bool = False, part: str = "full") -> list[list[complex]]:
    """ρ(t) on the four branches from an equal superposition at t = 0, H = 0 (their Eq. 24). `part` keeps the whole generator
    ("full"), only its imaginary part ("interaction": the commutator with the smeared pair potential, a pure unitary), or only its
    real part ("noise": the model's own decoherence, a dephasing channel)."""
    br = collinear_branches(split, nearest)
    rho = [[0j] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            g = tn_g(br[r], br[c], masses, sigma, planted_defect)
            if part == "interaction":
                g = complex(0.0, g.imag)
            elif part == "noise":
                g = complex(g.real, 0.0)
            elif part != "full":
                raise ValueError(part)
            rho[r][c] = 0.25 * cmath.exp((G_NEWTON / (2.0 * HBAR)) * g * t)
    return rho


def tn_negativity(split: float, nearest: float, m: float, sigma: float, t: float, planted_defect: bool = False, part: str = "full") -> float:
    return negativity(tn_state(split, nearest, (m, m), sigma, t, planted_defect, part))


def dp_collapse_state(split: float, nearest: float, m: float, sigma: float, t: float) -> list[list[complex]]:
    """Quantum gravity plus Diósi–Penrose collapse, Newton intact: the Newtonian branch phases of the quantum channel with the
    DP decoherence (the real part of the hybrid generator, which is Diósi's two-body collapse functional) as damping."""
    br = collinear_branches(split, nearest)
    phases = [G_NEWTON * m * m * t / (HBAR * abs(b[1] - b[0])) for b in br]
    rho = [[0j] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            damp = (G_NEWTON / (2.0 * HBAR)) * tn_g(br[r], br[c], (m, m), sigma).real * t
            rho[r][c] = 0.25 * cmath.exp(1j * (phases[r] - phases[c])) * math.exp(damp)
    return rho


def dp_collapse_negativity(split: float, nearest: float, m: float, sigma: float, t: float) -> float:
    return negativity(dp_collapse_state(split, nearest, m, sigma, t))


def dp_collapse_sigma_at(split: float, nearest: float, m: float, t: float, fraction: float) -> float:
    """The smallest σ at which pure collapse leaves `fraction` of the quantum channel's negativity (fraction → 0 for the critical σ)."""
    target = fraction * negativity(dp_collapse_state(split, nearest, m, 1.0, t))
    lo, hi = 1e-10, 1.0
    for _ in range(90):
        mid = math.sqrt(lo * hi)
        if dp_collapse_negativity(split, nearest, m, mid, t) > max(target, 1e-9):
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


def dp_collapse_scaling() -> dict:
    """How the critical collapse σ of the 2017 geometry moves with mass, hold time and the geometry's overall size: both the Newtonian
    phases and the collapse damping scale as m² t, so while the phases stay small the threshold is set by the geometry alone."""
    nearest = BMV_D_M - BMV_DX_M
    base = dp_collapse_sigma_at(BMV_DX_M, nearest, BMV_M_KG, BMV_T_S, 0.0)
    return {
        "base_m": base,
        "by_mass_at_2p5s": {f"{m:.0e}": dp_collapse_sigma_at(BMV_DX_M, nearest, m, BMV_T_S, 0.0) for m in (1e-15, 1e-14)},
        "by_hold_time_1e-14kg": {f"{t:g}s": dp_collapse_sigma_at(BMV_DX_M, nearest, BMV_M_KG, t, 0.0) for t in (1.0, 2.5)},
        "by_geometry_scale": {f"x{k:g}": dp_collapse_sigma_at(BMV_DX_M * k, nearest * k, BMV_M_KG, BMV_T_S, 0.0) for k in (0.5, 1.0, 2.0)},
    }


MAP_RATIOS = (0.03, 0.1, 0.25, 0.5, 0.96, 1.25, 2.0, 4.0, 8.0, 16.0, 32.0)
MAP_SMALL_MASS_KG = 1e-16  # keeps the entangling phase small at a 100 µm nearest approach, where the collapse threshold is geometric


def threshold_map(ratios: tuple = MAP_RATIOS, nearest: float = 100e-6) -> list[dict]:
    """Both σ thresholds over the geometry ratio r = split / nearest approach, each divided by the nearest approach: G(r), above which
    the letter's hybrid dynamics entangles (E_− < 0), and F(r), above which the quantum witness survives pure Diósi–Penrose collapse
    at 2.5 s. Both scale with the nearest approach and, while the entangling phase is small, depend on nothing but r."""
    rows = []
    for r in ratios:
        split = r * nearest
        rows.append({
            "ratio": r,
            "hybrid_over_nearest": tn_critical_sigma(1e-15, split, nearest) / nearest,
            "hybrid_over_nearest_1e-14": tn_critical_sigma(1e-14, split, nearest) / nearest,
            "collapse_over_nearest": dp_collapse_sigma_at(split, nearest, MAP_SMALL_MASS_KG, BMV_T_S, 0.0) / nearest,
            "collapse_over_nearest_1e-15": dp_collapse_sigma_at(split, nearest, 1e-15, BMV_T_S, 0.0) / nearest,
        })
    return rows


SIGMA_ESTIMATE_M = 44.07e-6  # T.05's estimate of where the hybrid form could still live: the smeared pull matching the published Yukawa edge


def map_with_isl(sigma_estimate: float = SIGMA_ESTIMATE_M) -> dict:
    """The geometry map read with the 2020 inverse-square data: the 52 µm torque deficit the smeared pull would produce at each
    geometry's hybrid threshold, and the widest nearest approach the hybrid dynamics can entangle at the σ estimate, against the
    Casimir floor. Cross-kernel, so the wedge and ladder kernels are imported here."""
    from timegravity_kernel_wedge import wedge_deficit, wedge_yukawa_edge_deficit
    from timegravity_kernel_ladder import casimir_floor_separation
    thresholds = {
        "geometry_2017": tn_critical_sigma(BMV_M_KG, BMV_DX_M, BMV_D_M - BMV_DX_M),
        "letter_geometry": tn_critical_sigma(TN_M_KG, TN_L_M, TN_D_M),
    }
    deficits = {k: wedge_deficit(s) for k, s in thresholds.items()}
    deficits["estimate"] = wedge_deficit(sigma_estimate)
    rows = threshold_map()
    widest = {f"r{row['ratio']:g}": sigma_estimate / row["hybrid_over_nearest"] for row in rows}
    return {
        "sigma_estimate_m": sigma_estimate, "hybrid_threshold_m": thresholds, "torque_deficit_at_threshold": deficits,
        "published_edge_deficit": wedge_yukawa_edge_deficit(), "widest_entangling_nearest_m": widest,
        "casimir_floor_m": {f"{m:.0e}": casimir_floor_separation(m) for m in (1e-15, 1e-14, 1e-13)},
        # the hybrid threshold for a pair sitting at its own Casimir floor, at a split a thirtieth of the gap and at equal split and gap
        "hybrid_sigma_at_floor_m": {f"{m:.0e}_r{r:g}": tn_critical_sigma(m, r * casimir_floor_separation(m), casimir_floor_separation(m))
                                    for m in (1e-15, 1e-14) for r in (0.03, 1.0)},
    }


def open_region_timing(sigma_estimate: float = SIGMA_ESTIMATE_M) -> list[dict]:
    """Inside the region where the hybrid dynamics could still reach the witness (pairs at their Casimir floor, small splits, σ at the
    estimate or below): how fast and how strongly it entangles, against the quantum channel's time to full entanglement at the same
    geometry, and what the hybrid negativity is at that moment."""
    from timegravity_kernel_ladder import casimir_floor_separation
    rows = []
    for m, nearest, r in ((1e-15, casimir_floor_separation(1e-15), 0.03), (1e-15, casimir_floor_separation(1e-15), 0.25), (1e-15, 30e-6, 0.03),
                          (1e-14, casimir_floor_separation(1e-14), 0.03), (1e-14, casimir_floor_separation(1e-14), 0.25)):
        split = r * nearest
        t_full = time_to_full_entanglement(m, nearest + split, split)
        for sigma in (sigma_estimate, 30e-6):
            surv = tn_survival(split, nearest, m, sigma)
            rows.append({"m_kg": m, "nearest_m": nearest, "ratio": r, "sigma_m": sigma, "hybrid_critical_sigma_m": tn_critical_sigma(m, split, nearest),
                         "quantum_t_full_s": t_full, "hybrid_negativity_at_t_full": tn_negativity(split, nearest, m, sigma, t_full),
                         "hybrid_negativity_at_10_t_full": tn_negativity(split, nearest, m, sigma, 10.0 * t_full),
                         "hybrid_peak_negativity": surv["peak_negativity"], "hybrid_peak_time_s": surv["peak_time_s"], "hybrid_last_time_s": surv["last_entangled_time_s"]})
    return rows


# ---------------------------------------------------------------------------------------------------------------------------------
# Branches as points in a plane. The smeared pair potential of two Gaussian masses depends on their distance alone, so the 1-D
# kernels above generalise by replacing |x − y| with the Euclidean distance; the collinear layout reproduces them to rounding.
# ---------------------------------------------------------------------------------------------------------------------------------
def _dist(p: tuple, q: tuple) -> float:
    return math.hypot(p[0] - q[0], p[1] - q[1])


def tn_g_points(x: tuple, y: tuple, m: float, sigma: float) -> complex:
    """g(x, y) of the letter's Eqs. 12–14 for two branches given as pairs of 2-D points (particle A, particle B), equal masses."""
    re = im = 0.0
    for j in range(2):
        for k in range(2):
            fxx = f_tilde(_dist(x[j], x[k]), sigma); fyy = f_tilde(_dist(y[j], y[k]), sigma); fxy = f_tilde(_dist(x[j], y[k]), sigma)
            re += m * m * (-fxx - fyy + 2.0 * fxy)
            im += m * m * (fxx - fyy)
    return complex(re, im)


def branches_collinear(split: float, nearest: float) -> list[tuple]:
    """Mass A at {−L, 0}, mass B at {d, d + L} on one line: the layout of the 2017 proposal and of the kernels above."""
    return [((a, 0.0), (b, 0.0)) for a in (-split, 0.0) for b in (nearest, nearest + split)]


def branches_parallel(split: float, gap: float) -> list[tuple]:
    """The two superpositions side by side, a gap apart, each split along the same transverse direction (the 2024 screened
    proposal's parallel configuration): like branches sit at the gap, unlike branches at √(gap² + split²)."""
    return [((0.0, a), (gap, b)) for a in (0.0, split) for b in (0.0, split)]


def hybrid_state_points(br: list[tuple], m: float, sigma: float, t: float) -> list[list[complex]]:
    k0 = (G_NEWTON / (2.0 * HBAR)) * t
    return [[0.25 * cmath.exp(k0 * tn_g_points(br[r], br[c], m, sigma)) for c in range(4)] for r in range(4)]


def collapse_state_points(br: list[tuple], m: float, sigma: float, t: float) -> list[list[complex]]:
    phases = [G_NEWTON * m * m * t / (HBAR * _dist(b[0], b[1])) for b in br]
    k0 = (G_NEWTON / (2.0 * HBAR)) * t
    return [[0.25 * cmath.exp(1j * (phases[r] - phases[c])) * math.exp(k0 * tn_g_points(br[r], br[c], m, sigma).real) for c in range(4)]
            for r in range(4)]


def quantum_t_full_points(br: list[tuple], m: float) -> float:
    """Time at which the quantum channel's four-branch state is maximally entangled (entangling phase π)."""
    rate = [G_NEWTON * m * m / (HBAR * _dist(b[0], b[1])) for b in br]
    return math.pi / abs(rate[1] + rate[2] - rate[0] - rate[3])


def hybrid_survival_points(br: list[tuple], m: float, sigma: float) -> dict:
    best, t_best, last = 0.0, None, None
    for k in range(-12, 44):
        t = 10.0 ** (k / 4.0)
        n = negativity(hybrid_state_points(br, m, sigma, t))
        if n > best:
            best, t_best = n, t
        if n > 1e-9:
            last = t
    return {"peak_negativity": best, "peak_time_s": t_best, "last_entangled_time_s": last}


def hybrid_critical_sigma_points(br: list[tuple], m: float) -> float:
    """Smallest σ at which the hybrid dynamics entangles the geometry at any time on the log grid (the E_− criterion is written
    for the collinear layout, so the general case is decided on the master equation's negativity)."""
    entangles = lambda s: hybrid_survival_points(br, m, s)["peak_negativity"] > 1e-9
    lo, hi = 1e-7, 1.0
    if not entangles(hi):
        return float("inf")
    for _ in range(36):
        mid = math.sqrt(lo * hi)
        if entangles(mid):
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


def collapse_critical_sigma_points(br: list[tuple], m: float, t: float) -> float:
    lo, hi = 1e-10, 1.0
    for _ in range(60):
        mid = math.sqrt(lo * hi)
        if negativity(collapse_state_points(br, m, mid, t)) > 1e-9:
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


def parallel_map(ratios: tuple = (0.03, 0.1, 0.25, 0.5, 1.0, 2.0), gap: float = 100e-6) -> list[dict]:
    """The side-by-side counterpart of threshold_map: both thresholds over the gap, against split / gap."""
    rows = []
    for r in ratios:
        br = branches_parallel(r * gap, gap)
        rows.append({"ratio": r, "hybrid_over_gap": hybrid_critical_sigma_points(br, 1e-15) / gap,
                     "collapse_over_gap": collapse_critical_sigma_points(br, MAP_SMALL_MASS_KG, BMV_T_S) / gap})
    return rows


# Published geometries: (key, layout, mass kg, split m, nearest approach or gap m). Sources on the T.05 ledger.
PROPOSALS = (
    ("bose2017", "collinear", 1e-14, 250e-6, 200e-6),              # Bose et al. 2017: d = 450 µm centre to centre, Δx = 250 µm
    ("chevalier2020_d350", "collinear", 1e-14, 250e-6, 100e-6),    # Chevalier, Paige & Kim 2020: d = 350 µm, 2δ = 250 µm, closest approach 100 µm
    ("vandekamp2020", "collinear", 1e-15, 23e-6, 47e-6),           # van de Kamp et al. 2020: Δx = 23 µm, initial separation 47 µm behind a 1 µm plate
    ("schut2024_z30", "parallel", 1e-14, 8.5e-6, 61e-6),           # Schut et al. 2024 Table I: 10⁻¹⁴ kg, z = 30 µm (d = 61 µm), Δx = 8.5 µm
    ("schut2024_z10", "parallel", 1e-14, 1.7e-6, 21e-6),           # z = 10 µm (d = 21 µm), Δx = 1.7 µm
    ("schut2024_z5", "parallel", 1e-14, 0.65e-6, 11e-6),           # z = 5 µm (d = 11 µm), Δx = 0.65 µm
    ("schut2024_z10_1e-13", "parallel", 1e-13, 0.17e-6, 21e-6),    # 10⁻¹³ kg, z = 10 µm
    ("schut2024_z10_1e-15", "parallel", 1e-15, 23e-6, 21e-6),      # 10⁻¹⁵ kg, z = 10 µm
)


def proposals_table(sigmas: tuple = (SIGMA_ESTIMATE_M, 30e-6)) -> list[dict]:
    """Every published geometry on the map: the hybrid threshold and its 52 µm torque deficit, the pure-collapse threshold at the
    quantum channel's full-entanglement time, and at each σ the hybrid negativity at that time and its peak."""
    from timegravity_kernel_wedge import wedge_deficit
    rows = []
    for key, layout, m, split, near in PROPOSALS:
        br = branches_collinear(split, near) if layout == "collinear" else branches_parallel(split, near)
        sc = hybrid_critical_sigma_points(br, m)
        t_full = quantum_t_full_points(br, m)
        row = {"key": key, "layout": layout, "m_kg": m, "split_m": split, "nearest_m": near, "hybrid_sigma_c_m": sc,
               "torque_deficit_at_hybrid_sigma_c": wedge_deficit(sc) if sc < 1.0 else 1.0,
               "collapse_sigma_c_at_t_full_m": collapse_critical_sigma_points(br, m, t_full), "quantum_t_full_s": t_full, "at_sigma": {}}
        for s in sigmas:
            if s > sc:
                surv = hybrid_survival_points(br, m, s)
                row["at_sigma"][f"{s * 1e6:.0f}um"] = {"entangles": True, "hybrid_negativity_at_t_full": negativity(hybrid_state_points(br, m, s, t_full)), **surv}
            else:
                row["at_sigma"][f"{s * 1e6:.0f}um"] = {"entangles": False}
        rows.append(row)
    return rows


def rijavec_tau_g(m: float = BMV_M_KG, d: float = BMV_D_M, dx: float = BMV_DX_M) -> float:
    """τ_G = ħ d [(d/Δx)² − 1] / (G m²) of Rijavec, Carlesso, Bassi, Vedral & Marletto 2021 (their Eq. 7): the pair is separable at all
    times for a dephasing rate above 1/τ_G (their Eq. 15)."""
    return HBAR * d * ((d / dx) ** 2 - 1.0) / (G_NEWTON * m * m)


def tn_negativity_parts(split: float, nearest: float, m: float, sigma: float, t: float) -> dict[str, float]:
    """The model's negativity with its whole generator, with its interaction part alone, and with its noise part alone."""
    return {p: tn_negativity(split, nearest, m, sigma, t, part=p) for p in ("full", "interaction", "noise")}


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
    # 4c. Quantum gravity plus pure DP collapse (Newton intact): the σ below which the witness dies, for both geometries.
    collapse = {}
    for label, (L, d, mm, tt) in {"geometry_2017_2p5s": (BMV_DX_M, nearest_2017, BMV_M_KG, BMV_T_S), "letter_geometry_2p5s": (TN_L_M, TN_D_M, TN_M_KG, BMV_T_S),
                                 "letter_geometry_1s": (TN_L_M, TN_D_M, TN_M_KG, 1.0)}.items():
        collapse[label] = {"quantum_negativity": negativity(dp_collapse_state(L, d, mm, 1.0, tt)), "critical_sigma_m": dp_collapse_sigma_at(L, d, mm, tt, 0.0),
                           "half_sigma_m": dp_collapse_sigma_at(L, d, mm, tt, 0.5),
                           "negativity_by_sigma": {f"{s * 1e6:.0f}um": dp_collapse_negativity(L, d, mm, s, tt) for s in (44e-6, 100e-6, 200e-6, 500e-6, 1e-3)}}
    c17 = collapse["geometry_2017_2p5s"]
    # The damping is bounded (Re g ≤ 0, so every off-diagonal element shrinks); at σ = 1 m the state is the quantum channel's to 1e-9;
    # the quantum negativity is positive; and the negativity rises monotonically along the σ table.
    quantum_2017 = negativity(four_branch_state(branch_phases(BMV_M_KG, BMV_D_M, BMV_DX_M, BMV_T_S, "quantum")))
    seq17 = [c17["negativity_by_sigma"][k] for k in ("44um", "100um", "200um", "500um", "1000um")]
    collapse_ok = (c17["critical_sigma_m"] < c17["half_sigma_m"] and c17["negativity_by_sigma"]["100um"] < 1e-9 < c17["negativity_by_sigma"]["500um"]
                   and abs(c17["negativity_by_sigma"]["1000um"] - c17["quantum_negativity"]) / c17["quantum_negativity"] < 1e-2
                   and c17["quantum_negativity"] > 0.07 and abs(c17["quantum_negativity"] - quantum_2017) < 1e-9
                   and abs(dp_collapse_negativity(BMV_DX_M, nearest_2017, BMV_M_KG, 1.0, BMV_T_S) - quantum_2017) < 1e-9
                   and all(seq17[i] <= seq17[i + 1] + 1e-12 for i in range(len(seq17) - 1))
                   and collapse["letter_geometry_2p5s"]["critical_sigma_m"] < collapse["letter_geometry_2p5s"]["half_sigma_m"] < c17["critical_sigma_m"])
    # 4d. The threshold's scaling, and the 2021 study's 1/τ_G against this page's dephasing threshold.
    scaling = dp_collapse_scaling()
    sc_m = list(scaling["by_mass_at_2p5s"].values()); sc_t = list(scaling["by_hold_time_1e-14kg"].values()); sc_g = scaling["by_geometry_scale"]
    scaling_ok = (max(sc_m) / min(sc_m) < 1.02 and max(sc_t) / min(sc_t) < 1.02
                  and 0.4 < sc_g["x0.5"] / sc_g["x1"] < 0.6 and 1.7 < sc_g["x2"] / sc_g["x1"] < 2.3)
    gamma_zero = negativity_threshold_gamma_t(branch_phases(BMV_M_KG, BMV_D_M, BMV_DX_M, BMV_T_S, "quantum"), hi=50.0) / BMV_T_S
    tau_g = rijavec_tau_g()
    rijavec_ok = abs(gamma_zero * tau_g - 1.0) < 2e-2
    # 4e. The geometry map: both thresholds over r = split / nearest, mass-independent, G above F everywhere, F and G monotone.
    tmap = threshold_map()
    gs = [row["hybrid_over_nearest"] for row in tmap]; fs = [row["collapse_over_nearest"] for row in tmap]
    map_ok = (all(abs(row["hybrid_over_nearest_1e-14"] / row["hybrid_over_nearest"] - 1.0) < 1e-3 for row in tmap)
              and all(abs(row["collapse_over_nearest_1e-15"] / row["collapse_over_nearest"] - 1.0) < 1e-2 for row in tmap)
              and all(g > f for g, f in zip(gs, fs)) and all(b > a_ for a_, b in zip(gs, gs[1:])) and all(b > a_ for a_, b in zip(fs, fs[1:]))
              and 0.3 < fs[0] < 0.4 and 0.99 < fs[-1] < 1.01 and 1.15 < gs[0] < 1.25 and 3.0 < gs[0] / fs[0] < 3.6
              and abs(tmap[5]["collapse_over_nearest"] * 200e-6 / collapse["geometry_2017_2p5s"]["critical_sigma_m"] - 1.0) < 1e-2
              and abs(tmap[5]["hybrid_over_nearest"] * 200e-6 / tn_critical_sigma(BMV_M_KG, BMV_DX_M, BMV_D_M - BMV_DX_M) - 1.0) < 1e-3)
    # 4f. The map against the 2020 data: at the 2017 geometry's hybrid threshold the smeared pull removes the whole 52 µm torque; at the
    # letter's it is 2 to 3 times the published edge; the estimate reproduces the edge; the open window sits above the Casimir floor only
    # for small splits.
    isl = map_with_isl()
    isl_ok = (isl["torque_deficit_at_threshold"]["geometry_2017"] > 0.99
              and 2.0 < isl["torque_deficit_at_threshold"]["letter_geometry"] / isl["published_edge_deficit"] < 3.0
              and abs(isl["torque_deficit_at_threshold"]["estimate"] / isl["published_edge_deficit"] - 1.0) < 0.05
              and 34e-6 < isl["widest_entangling_nearest_m"]["r0.03"] < 38e-6 and 18e-6 < isl["widest_entangling_nearest_m"]["r0.96"] < 21e-6
              and isl["casimir_floor_m"]["1e-15"] < isl["widest_entangling_nearest_m"]["r0.03"]
              and isl["casimir_floor_m"]["1e-14"] > isl["widest_entangling_nearest_m"]["r0.96"]
              and isl["casimir_floor_m"]["1e-13"] > isl["widest_entangling_nearest_m"]["r0.03"]
              and 19e-6 < isl["hybrid_sigma_at_floor_m"]["1e-15_r0.03"] < 23e-6
              and 39e-6 < isl["hybrid_sigma_at_floor_m"]["1e-15_r1"] < 41e-6)
    # 4g. Time as the discriminator inside the open region: where the hybrid dynamics entangles at all (σ above its threshold), its
    # negativity at the quantum channel's full-entanglement time is below 2e-3, its peak comes 9 to 110 times later and stays below 0.06.
    timing = open_region_timing()
    live = [row for row in timing if row["sigma_m"] > row["hybrid_critical_sigma_m"]]
    timing_ok = (len(live) >= 6
                 and all(row["hybrid_negativity_at_t_full"] < 2e-3 for row in live)
                 and all(8.0 < row["hybrid_peak_time_s"] / row["quantum_t_full_s"] < 150.0 for row in live)
                 and all(0.0 < row["hybrid_peak_negativity"] < 0.06 for row in live)
                 and all(row["hybrid_peak_negativity"] < 1e-9 for row in timing if row["sigma_m"] <= row["hybrid_critical_sigma_m"]))
    # 4h. Points in a plane: the collinear layout reproduces the 1-D kernels; side by side the hybrid threshold is about 0.65 of the gap
    # for any split and the collapse threshold about 0.44; the published proposals' thresholds, deficits and timing.
    brc = branches_collinear(BMV_DX_M, BMV_D_M - BMV_DX_M)
    points_ok = (abs(negativity(hybrid_state_points(brc, BMV_M_KG, 1e-3, BMV_T_S)) - tn_negativity(BMV_DX_M, BMV_D_M - BMV_DX_M, BMV_M_KG, 1e-3, BMV_T_S)) < 1e-12
                 and abs(negativity(collapse_state_points(brc, BMV_M_KG, 1e-3, BMV_T_S)) - dp_collapse_negativity(BMV_DX_M, BMV_D_M - BMV_DX_M, BMV_M_KG, 1e-3, BMV_T_S)) < 1e-12
                 and abs(hybrid_critical_sigma_points(brc, BMV_M_KG) / tn_critical_sigma(BMV_M_KG, BMV_DX_M, BMV_D_M - BMV_DX_M) - 1.0) < 1e-3
                 and abs(quantum_t_full_points(brc, BMV_M_KG) / time_to_full_entanglement(BMV_M_KG, BMV_D_M, BMV_DX_M) - 1.0) < 1e-9)
    pmap = parallel_map()
    parallel_ok = all(0.59 < row["hybrid_over_gap"] < 0.66 for row in pmap) and all(0.42 < row["collapse_over_gap"] < 0.49 for row in pmap)
    props = proposals_table()
    pb = {row["key"]: row for row in props}
    live = [v for row in props for v in row["at_sigma"].values() if v["entangles"]]
    proposals_ok = (pb["bose2017"]["torque_deficit_at_hybrid_sigma_c"] > 0.99 and pb["chevalier2020_d350"]["torque_deficit_at_hybrid_sigma_c"] > 0.99
                    and 0.15 < pb["vandekamp2020"]["torque_deficit_at_hybrid_sigma_c"] < 0.30 and pb["schut2024_z30"]["torque_deficit_at_hybrid_sigma_c"] < 0.025
                    and 13e-6 < pb["schut2024_z10"]["hybrid_sigma_c_m"] < 14.5e-6 and pb["schut2024_z10"]["torque_deficit_at_hybrid_sigma_c"] < 1e-3
                    and not pb["bose2017"]["at_sigma"]["44um"]["entangles"] and not pb["vandekamp2020"]["at_sigma"]["44um"]["entangles"]
                    and pb["schut2024_z10"]["at_sigma"]["44um"]["entangles"] and pb["schut2024_z10"]["at_sigma"]["30um"]["entangles"]
                    and 150.0 < pb["schut2024_z10"]["quantum_t_full_s"] < 170.0
                    and len(live) >= 8 and all(v["hybrid_negativity_at_t_full"] < 2e-2 for v in live) and all(v["peak_negativity"] < 0.085 for v in live))
    # 5. Where the entangling power sits: the noise part alone entangles nothing at any σ or time; the interaction part alone gives
    #    at least the full model's negativity; and as σ → 0 the interaction part is the quantum channel exactly.
    parts = {}
    for label, (L, d, mm, s, tt) in {"fig3_sigma_75um_1e4s": (TN_L_M, TN_D_M, TN_M_KG, 75e-6, 1e4), "fig3_sigma_50um_1e4s": (TN_L_M, TN_D_M, TN_M_KG, 50e-6, 1e4),
                                     "geometry_2017_sigma_1mm_2p5s": (BMV_DX_M, nearest_2017, BMV_M_KG, 1e-3, BMV_T_S),
                                     "geometry_2017_sigma_1nm_2p5s": (BMV_DX_M, nearest_2017, BMV_M_KG, 1e-9, BMV_T_S)}.items():
        parts[label] = tn_negativity_parts(L, d, mm, s, tt)
    quantum_negativity = negativity(four_branch_state(branch_phases(BMV_M_KG, BMV_D_M, BMV_DX_M, BMV_T_S, "quantum")))
    parts_ok = (all(v["noise"] < 1e-12 for v in parts.values()) and all(v["interaction"] >= v["full"] - 1e-12 for v in parts.values())
                and abs(parts["geometry_2017_sigma_1nm_2p5s"]["interaction"] - quantum_negativity) < 1e-6
                and parts["fig3_sigma_50um_1e4s"]["full"] < 1e-12 < parts["fig3_sigma_50um_1e4s"]["interaction"])
    defect_rejected = tn_critical_separation_from_negativity(sigma, sigma / 500.0, planted_defect=True) == float("inf")
    return {
        "tn_dc_over_sigma_e_minus_small_split": dc_ratio_e, "tn_dc_paper_text": TN_DC_OVER_SIGMA_TEXT, "tn_dc_paper_appendix": TN_DC_OVER_SIGMA_APPENDIX,
        "tn_dc_e_minus_split_sigma_over_500": dc_e_mid, "tn_dc_negativity_split_sigma_over_500": dc_n_mid,
        "tn_fig3": fig3, "tn_2017_nearest_m": nearest_2017, "tn_2017_sigma_c_m": sigma_c_2017, "tn_2017_by_sigma": tn_2017,
        "tn_phase_tiny_sigma_rad": dphi_tn_tiny_sigma, "newton_phase_rad": dphi_newton, "tn_potential_ratio_fig3": potential_ratio_fig3,
        "ktm_threshold_ratios": ratios, "ktm_2017": ktm_2017,
        "entangling_parts": parts, "quantum_channel_negativity_2017": quantum_negativity, "parts_ok": parts_ok,
        "pure_collapse": collapse, "collapse_ok": collapse_ok,
        "threshold_map": tmap, "map_ok": map_ok, "map_with_isl": isl, "isl_ok": isl_ok, "open_region_timing": timing, "timing_ok": timing_ok, "points_ok": points_ok, "parallel_map": pmap, "parallel_ok": parallel_ok, "proposals": props, "proposals_ok": proposals_ok,
        "collapse_scaling": scaling, "scaling_ok": scaling_ok, "rijavec_tau_g_s": tau_g, "dephasing_threshold_per_s": gamma_zero, "rijavec_ok": rijavec_ok,
        "dc_paper_ok": dc_paper_ok, "dc_double_entry_ok": dc_double_entry_ok, "fig3_ok": fig3_ok, "tn_2017_ok": tn_2017_ok,
        "ktm_ok": ktm_ok, "ktm_edge_ok": ktm_edge_ok, "defect_rejected": defect_rejected,
        "ok": dc_paper_ok and dc_double_entry_ok and fig3_ok and tn_2017_ok and ktm_ok and ktm_edge_ok and parts_ok and collapse_ok and scaling_ok and rijavec_ok and map_ok and isl_ok and timing_ok and points_ok and parallel_ok and proposals_ok and defect_rejected,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(check_dispute(), indent=2, default=str))
