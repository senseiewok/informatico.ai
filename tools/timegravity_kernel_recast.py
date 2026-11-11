# -*- coding: utf-8 -*-
"""Time & Gravity · T.05 recast kernel: the Eöt-Wash 2020 published Yukawa limits recast onto the smeared pair potential.

The 2025 letter's hybrid Diósi–Penrose model smears Newton's pair potential to −Gmm′ erf(r/2σ)/r. J. G. Lee's dissertation (University of
Washington, 2020; the thesis behind Lee et al., PRL 124, 101101) tabulates in its Table 11.4, for 66 Yukawa ranges λ from 5 µm to 8.9 mm,
the fitted strength α* ± σ_α and the signed 95 % limits +α95 and −α95 of the 2020 wedge experiment (fits with free Newtonian offset s0 and
scale γ). This kernel projects the smeared pull's torque deficit, computed on the full Fourier–Bessel wedge pattern
(timegravity_kernel_wedge), onto the unit Yukawa torque shape at each tabulated λ over the experiment's separation range, picks the λ the
smeared shape mimics best, and compares the effective strength with the published signed limit there. It is a recast of published limits,
not a refit of the data; the separation weighting of the 95 real runs is not public, so the result is stressed over four separation grids,
an absolute-torque weighting (w = T_N², the weighting a constant torque noise implies) and two harmonics. The smeared pull weakens
short-range gravity (α_eff < 0) while the experiment's own best fit in the 5–100 µm window leans slightly the other way (α* > 0, e.g.
+18.9 ± 12.0 at λ = 18 µm), which is why the signed limit −α95 the smeared pull faces is much tighter than |α95| there; the thesis'
signed limits come from its Δχ² = 6.17 profile over the nuisance parameters and are asymmetric about α* (about 2.2σ_α below, 2.5σ_α
above), so the comparison uses the signed column directly and reports the Gaussian z² only as a reading aid. The planted defect is the retired method: matching the gravitational-strength edge at the single 52 µm separation.

Stdlib only. Data: data/eotwash2020_table11_4.json (provenance inside).
"""
from __future__ import annotations

import json
import math
import pathlib

from timegravity_kernel_wedge import wedge_torque

DATA_PATH = pathlib.Path(__file__).resolve().parents[1] / "data" / "eotwash2020_table11_4.json"
EW_S_MIN_M = 52e-6
EW_S_MAX_M = 3.0e-3
EDGE_LAMBDA_M = 38.6e-6     # the published gravitational-strength (|α| = 1) exclusion edge
EDGE_MATCH_SIGMA_M = 44.07e-6  # the retired single-separation edge match (T.05's earlier estimate)


def load_table() -> dict:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def separation_grid(kind: str = "log52-3000", n: int | None = None) -> list[float]:
    """Separation grids standing in for the experiment's 95 runs (their weighting is not public)."""
    if kind == "log52-3000":
        n = n or 30; return [EW_S_MIN_M * (EW_S_MAX_M / EW_S_MIN_M) ** (i / (n - 1)) for i in range(n)]
    if kind == "lin52-3000":
        n = n or 30; return [EW_S_MIN_M + (EW_S_MAX_M - EW_S_MIN_M) * i / (n - 1) for i in range(n)]
    if kind == "log52-200":
        n = n or 20; return [EW_S_MIN_M * (200e-6 / EW_S_MIN_M) ** (i / (n - 1)) for i in range(n)]
    if kind == "log52-100":
        n = n or 15; return [EW_S_MIN_M * (100e-6 / EW_S_MIN_M) ** (i / (n - 1)) for i in range(n)]
    raise ValueError(kind)


def unit_yukawa_shapes(n_fold: int, seps: list[float], lams: list[float], t_newton: list[float]) -> dict[float, list[float]]:
    """y_λ(s) = T_Yukawa(α = 1, λ)(s) / T_Newton(s) − 1 on the wedge pattern."""
    return {lam: [wedge_torque(n_fold, s, "yukawa", lam=lam, alpha=1.0) / t_newton[i] - 1.0 for i, s in enumerate(seps)] for lam in lams}


def smeared_deficit(n_fold: int, seps: list[float], sigma: float, t_newton: list[float]) -> list[float]:
    """d(s) = 1 − T_smeared(s) / T_Newton(s): the fraction of the Newtonian torque the smeared pull removes."""
    return [1.0 - wedge_torque(n_fold, s, "smeared", sigma=sigma) / t_newton[i] for i, s in enumerate(seps)]


def project(deficit: list[float], shape: list[float], weights: list[float] | None = None) -> tuple[float, float]:
    """Least-squares strength α_eff with T ≈ T_N (1 + α_eff y) ≈ T_N (1 − d), and the relative shape residual; optional weights
    (equal by default; w = T_N² is the weighting a constant absolute torque noise implies)."""
    w = weights or [1.0] * len(deficit)
    den = sum(wi * y * y for wi, y in zip(w, shape))
    a_eff = -sum(wi * d * y for wi, d, y in zip(w, deficit, shape)) / den
    resid = math.sqrt(sum(wi * (d + a_eff * y) ** 2 for wi, d, y in zip(w, deficit, shape)) / max(sum(wi * d * d for wi, d in zip(w, deficit)), 1e-300))
    return a_eff, resid


def _w_dot(u: list[float], v: list[float], weights: list[float] | None = None) -> float:
    if weights is None:
        return sum(ui * vi for ui, vi in zip(u, v))
    return sum(wi * ui * vi for wi, ui, vi in zip(weights, u, v))


def nuisance_orthonormal_basis(n_fold: int, seps: list[float], t_newton: list[float],
                               weights: list[float] | None = None, step_m: float = 1e-8) -> tuple[list[float], list[float]]:
    """Modified Gram–Schmidt W-orthonormal basis (q1, q2) for the linearized floating calibration tangent space
    N = span{ 1, s_ref * d/ds ln T_N(s) } corresponding to floating Newtonian scale γ and separation offset s0."""
    s_ref = seps[0]
    v1 = [1.0 for _ in seps]
    v2 = [
        s_ref * (wedge_torque(n_fold, s + step_m, "newton") - wedge_torque(n_fold, s - step_m, "newton")) / (2.0 * step_m * tn)
        for s, tn in zip(seps, t_newton)
    ]
    n1 = math.sqrt(max(_w_dot(v1, v1, weights), 1e-300))
    q1 = [x / n1 for x in v1]
    c12 = _w_dot(v2, q1, weights)
    u2 = [x - c12 * q1_i for x, q1_i in zip(v2, q1)]
    n2 = math.sqrt(max(_w_dot(u2, u2, weights), 1e-300))
    q2 = [x / n2 for x in u2]
    return q1, q2


def project_out_nuisance(vec: list[float], q1: list[float], q2: list[float], weights: list[float] | None = None) -> list[float]:
    """Apply the Fisher Schur-complement orthogonal projector P_perp = I - Q Q^T W to `vec`."""
    a1 = _w_dot(vec, q1, weights)
    a2 = _w_dot(vec, q2, weights)
    return [v - a1 * q1_i - a2 * q2_i for v, q1_i, q2_i in zip(vec, q1, q2)]


def _det3(m: list[list[float]]) -> float:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def _inv3(m: list[list[float]]) -> list[list[float]]:
    d = _det3(m)
    return [
        [(m[1][1] * m[2][2] - m[1][2] * m[2][1]) / d, (m[0][2] * m[2][1] - m[0][1] * m[2][2]) / d, (m[0][1] * m[1][2] - m[0][2] * m[1][1]) / d],
        [(m[1][2] * m[2][0] - m[1][0] * m[2][2]) / d, (m[0][0] * m[2][2] - m[0][2] * m[2][0]) / d, (m[0][2] * m[1][0] - m[0][0] * m[1][2]) / d],
        [(m[1][0] * m[2][1] - m[1][1] * m[2][0]) / d, (m[0][1] * m[2][0] - m[0][0] * m[2][1]) / d, (m[0][0] * m[1][1] - m[0][1] * m[1][0]) / d],
    ]


def d_optimal_three_point_design(sigma: float = 33e-6, s_min: float = 25e-6, s_max: float = EW_S_MAX_M,
                                 n_grid: int = 25, n_fold: int = 120) -> dict:
    """Exact saturated 3-point Kiefer–Wolfowitz / Carathéodory D-optimal separation design on [s_min, s_max]
    for joint estimation of (γ, s0, α_smeared). Verifies the Kiefer–Wolfowitz Equivalence Theorem directional
    variance bound d(s) = x(s)^T M(ξ*)^-1 x(s) <= 3 across the entire grid, hitting 3 at the 3 support points."""
    seps = [s_min * (s_max / s_min) ** (i / (n_grid - 1)) for i in range(n_grid)]
    tn = [wedge_torque(n_fold, s, "newton") for s in seps]
    v2 = [
        s_min * (wedge_torque(n_fold, s + 1e-8, "newton") - wedge_torque(n_fold, s - 1e-8, "newton")) / (2.0e-8 * tn_i)
        for s, tn_i in zip(seps, tn)
    ]
    key = (n_fold, tuple(seps), sigma)
    sig_vec = _DEFICIT_CACHE.get(key)
    if sig_vec is None:
        sig_vec = _DEFICIT_CACHE[key] = smeared_deficit(n_fold, seps, sigma, tn)
    rows_x = [[1.0, v2[i], sig_vec[i]] for i in range(n_grid)]
    best_abs_det = -1.0
    best_triplet = (0, n_grid // 2, n_grid - 1)
    for i0 in range(n_grid - 2):
        for i1 in range(i0 + 1, n_grid - 1):
            for i2 in range(i1 + 1, n_grid):
                val = abs(_det3([rows_x[i0], rows_x[i1], rows_x[i2]]))
                if val > best_abs_det:
                    best_abs_det = val
                    best_triplet = (i0, i1, i2)
    m_opt = [[sum(rows_x[idx][r] * rows_x[idx][c] for idx in best_triplet) / 3.0 for c in range(3)] for r in range(3)]
    m_inv = _inv3(m_opt)
    d_curve = [
        sum(rows_x[k][r] * sum(m_inv[r][c] * rows_x[k][c] for c in range(3)) for r in range(3))
        for k in range(n_grid)
    ]
    return {
        "sigma_m": sigma,
        "s_min_m": s_min,
        "s_max_m": s_max,
        "n_grid": n_grid,
        "support_separations_m": [seps[i] for i in best_triplet],
        "support_weights": [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0],
        "max_directional_variance": max(d_curve),
        "support_directional_variances": [d_curve[i] for i in best_triplet],
        "kiefer_wolfowitz_certified": max(d_curve) <= 3.0 + 1e-9 and all(abs(d_curve[i] - 3.0) < 1e-9 for i in best_triplet),
    }


_DEFICIT_CACHE: dict = {}


class Recast:
    """One recast configuration (harmonic, separation grid, λ window) with the Yukawa shapes computed once.
    When `nuisance_orthogonal=True`, applies exact Fisher Schur-complement projection out of span{1, s_min d/ds ln T_N(s)}."""

    def __init__(self, n_fold: int = 120, grid: str = "log52-3000", n_sep: int | None = None, lam_min: float = 10e-6, lam_max: float = 400e-6,
                 weighting: str = "equal", nuisance_orthogonal: bool = False):
        self.table = load_table()
        self.rows = {r["lambda_m"]: r for r in self.table["rows"]}
        self.lams = [r["lambda_m"] for r in self.table["rows"] if lam_min <= r["lambda_m"] <= lam_max]
        self.n_fold, self.grid = n_fold, grid
        self.seps = separation_grid(grid, n_sep)
        self.t_newton = [wedge_torque(n_fold, s, "newton") for s in self.seps]
        self.raw_shapes = unit_yukawa_shapes(n_fold, self.seps, self.lams, self.t_newton)
        self.weighting = weighting
        self.weights = [t * t for t in self.t_newton] if weighting == "abs_torque" else None
        self.nuisance_orthogonal = nuisance_orthogonal
        if nuisance_orthogonal:
            self.q1, self.q2 = nuisance_orthonormal_basis(n_fold, self.seps, self.t_newton, self.weights)
            self.shapes = {
                lam: project_out_nuisance(sh, self.q1, self.q2, self.weights)
                for lam, sh in self.raw_shapes.items()
            }
        else:
            self.q1, self.q2 = [], []
            self.shapes = self.raw_shapes

    def at_sigma(self, sigma: float, planted_defect: bool = False) -> dict:
        """Best-mimic λ, effective strength, shape residual, the published signed limit there and the verdict."""
        if planted_defect:
            # The retired reading: compare the deficit at the single 52 µm separation with the |α| = 1 edge there (no shapes, no limits table).
            d52 = 1.0 - wedge_torque(self.n_fold, EW_S_MIN_M, "smeared", sigma=sigma) / wedge_torque(self.n_fold, EW_S_MIN_M)
            edge = 1.0 - wedge_torque(self.n_fold, EW_S_MIN_M, "yukawa", lam=EDGE_LAMBDA_M, alpha=-1.0) / wedge_torque(self.n_fold, EW_S_MIN_M)
            return {"sigma_m": sigma, "lambda_m": EDGE_LAMBDA_M, "alpha_eff": -d52 / edge, "shape_residual": float("nan"),
                    "alpha95_minus": -1.0, "excluded": d52 > edge, "gaussian_z2": float("nan")}
        key = (self.n_fold, tuple(self.seps), sigma)  # the deficits do not depend on the weighting, so the variants share them
        d_raw = _DEFICIT_CACHE.get(key)
        if d_raw is None:
            d_raw = _DEFICIT_CACHE[key] = smeared_deficit(self.n_fold, self.seps, sigma, self.t_newton)
        d = project_out_nuisance(d_raw, self.q1, self.q2, self.weights) if self.nuisance_orthogonal else d_raw
        best = None
        for lam in self.lams:
            a_eff, resid = project(d, self.shapes[lam], self.weights)
            if best is None or resid < best[1]:
                best = (lam, resid, a_eff)
        lam, resid, a_eff = best
        row = self.rows[lam]
        out = {"sigma_m": sigma, "lambda_m": lam, "alpha_eff": a_eff, "shape_residual": resid, "alpha_star": row["alpha_star"],
               "sigma_alpha": row["sigma_alpha"], "alpha95_minus": row["alpha95_minus"], "excluded": a_eff < row["alpha95_minus"],
               # a reading aid only: the thesis' signed limit encodes the exact, asymmetric Δχ² = 6.17 boundary; this is the Gaussian z² about α*
               "gaussian_z2": ((a_eff - row["alpha_star"]) / row["sigma_alpha"]) ** 2}
        if self.nuisance_orthogonal:
            d_norm2 = max(_w_dot(d, d, self.weights), 1e-300)
            raw_norm2 = max(_w_dot(d_raw, d_raw, self.weights), 1e-300)
            y_norm2 = max(_w_dot(self.shapes[lam], self.shapes[lam], self.weights), 1e-300)
            out["retained_norm_fraction"] = math.sqrt(d_norm2 / raw_norm2)
            out["fisher_retention_ratio"] = d_norm2 / raw_norm2
            out["cos_theta_perp"] = abs(_w_dot(d, self.shapes[lam], self.weights)) / math.sqrt(d_norm2 * y_norm2)
        return out

    def sigma_95(self, lo: float = 20e-6, hi: float = 60e-6, steps: int = 9, planted_defect: bool = False) -> float:
        """Smallest σ excluded at 95 % (log bisection; 9 steps give 0.2 % resolution over 20–60 µm)."""
        if not self.at_sigma(hi, planted_defect)["excluded"]:
            return float("inf")
        for _ in range(steps):
            mid = math.sqrt(lo * hi)
            if self.at_sigma(mid, planted_defect)["excluded"]:
                hi = mid
            else:
                lo = mid
        return math.sqrt(lo * hi)


def edge_crossing_lambda(table: dict) -> float:
    """Where the thesis' |α95| crosses 1 (log interpolation): its own 'λ > 39 µm excluded at gravitational strength'."""
    rows = sorted(table["rows"], key=lambda r: r["lambda_m"])
    for a, b in zip(rows, rows[1:]):
        ya, yb = a["alpha95_abs"], b["alpha95_abs"]
        if ya >= 1.0 >= yb:
            f = math.log(ya) / (math.log(ya) - math.log(yb))
            return math.exp(math.log(a["lambda_m"]) + f * (math.log(b["lambda_m"]) - math.log(a["lambda_m"])))
    return float("nan")


# Geraci et al. 2008 (Phys. Rev. D 78, 022002), Table 5: 95 % exclusion limits on |α| from a micro-cantilever at a nominal 25 µm
# face-to-face separation, the other published table that reaches below the balance's 52 µm.
GERACI2008_TABLE5 = ((4e-6, 3.1e7), (6e-6, 4.6e5), (10e-6, 1.4e4), (18e-6, 1.1e3), (34e-6, 2.5e2), (66e-6, 1.5e2))


def short_range_comparison() -> list[dict]:
    """Geraci et al. 2008's tabulated |α| limits beside the balance's own |α95| at the same range (log-log interpolation between the
    two neighbouring rows of the dissertation's table; None below its shortest row)."""
    rows = load_table()["rows"]
    out = []
    for lam, lim in GERACI2008_TABLE5:
        lo = [r for r in rows if r["lambda_m"] <= lam * (1.0 + 1e-9)]
        hi = [r for r in rows if r["lambda_m"] >= lam * (1.0 - 1e-9)]
        if not lo or not hi:
            bal = None
        else:
            a, b = lo[-1], hi[0]
            if a["lambda_m"] == b["lambda_m"]:
                bal = a["alpha95_abs"]
            else:
                f = math.log(lam / a["lambda_m"]) / math.log(b["lambda_m"] / a["lambda_m"])
                bal = math.exp(math.log(a["alpha95_abs"]) + f * (math.log(b["alpha95_abs"]) - math.log(a["alpha95_abs"])))
        out.append({"lambda_m": lam, "geraci_alpha95_abs": lim, "balance_alpha95_abs": bal, "geraci_over_balance": None if bal is None else lim / bal})
    return out


def reach_below_limit(sigmas_m: tuple[float, ...] = (25e-6, 18e-6, 13.6e-6)) -> list[dict]:
    """Why the balance loses reach below the rung: for each σ the best-mimic λ (table rows down to its shortest, 5 µm), the effective
    strength, the published signed limit there and their ratio (how many times too weak the smeared pull is to be seen)."""
    rc = Recast(120, "log52-3000", n_sep=12, lam_min=5e-6, lam_max=100e-6)
    lam_floor = min(r["lambda_m"] for r in rc.table["rows"])
    out = []
    for s in sigmas_m:
        a = rc.at_sigma(s)
        out.append({"sigma_m": s, "lambda_m": a["lambda_m"], "alpha_eff": a["alpha_eff"], "alpha95_minus": a["alpha95_minus"],
                    "times_too_weak": a["alpha95_minus"] / a["alpha_eff"], "shape_residual": a["shape_residual"],
                    "mimic_at_table_floor": a["lambda_m"] == lam_floor, "excluded": a["excluded"]})
    return out


def check_recast(planted_defect: bool = False, quick: bool = True) -> dict:
    """The verifier's gate. Quick: the primary configuration (120ω, log grid, 12 separations, λ 10–100 µm) with equal and absolute-torque
    weighting; full: the four grids × two harmonics as well."""
    table = load_table()
    n_rows = len(table["rows"])
    lam_sorted = [r["lambda_m"] for r in table["rows"]]
    table_ok = (n_rows >= 60 and lam_sorted == sorted(lam_sorted) and all(r["alpha95_minus"] < 0 < r["alpha95_plus"] and r["alpha95_abs"] > 0 for r in table["rows"])
                and all(r["sigma_alpha"] > 0 for r in table["rows"]))
    edge = edge_crossing_lambda(table)
    edge_ok = 37e-6 < edge < 40e-6  # the experiment states λ > 39 µm excluded at |α| = 1
    primary = Recast(120, "log52-3000", n_sep=12, lam_min=10e-6, lam_max=100e-6)
    s95 = primary.sigma_95(planted_defect=planted_defect)
    at33, at35, at44 = (primary.at_sigma(s, planted_defect) for s in (33e-6, 35e-6, EDGE_MATCH_SIGMA_M))
    schur_eq = Recast(120, "log52-3000", n_sep=12, lam_min=10e-6, lam_max=100e-6, nuisance_orthogonal=True)
    schur_abs = Recast(120, "log52-3000", n_sep=12, lam_min=10e-6, lam_max=100e-6, weighting="abs_torque", nuisance_orthogonal=True)
    schur_eq_33 = schur_eq.at_sigma(33e-6, planted_defect=planted_defect)
    schur_abs_33 = schur_abs.at_sigma(33e-6, planted_defect=planted_defect)
    s95_schur_eq = schur_eq.sigma_95(planted_defect=planted_defect)
    s95_schur_abs = schur_abs.sigma_95(planted_defect=planted_defect)
    variants = {"120-log52-3000-12": s95,
                "120-log52-3000-12-abs_torque": Recast(120, "log52-3000", n_sep=12, lam_min=10e-6, lam_max=100e-6, weighting="abs_torque").sigma_95(planted_defect=planted_defect),
                "120-log52-3000-12-schur_equal": s95_schur_eq,
                "120-log52-3000-12-schur_abs_torque": s95_schur_abs}
    if not quick:
        for n_fold in (120, 18):
            for grid in ("log52-3000", "lin52-3000", "log52-200", "log52-100"):
                variants[f"{n_fold}-{grid}"] = Recast(n_fold, grid, lam_min=10e-6, lam_max=400e-6).sigma_95(planted_defect=planted_defect)
    spread = max(variants.values()) - min(variants.values()) if all(math.isfinite(v) for v in variants.values()) else float("inf")
    schur_ok = (32e-6 < s95_schur_eq < 33.4e-6 and 32e-6 < s95_schur_abs < 33.4e-6
                and schur_eq_33.get("cos_theta_perp", 0.0) > 0.999 and schur_abs_33.get("cos_theta_perp", 0.0) > 0.9995)
    recast_ok = (table_ok and edge_ok and 32e-6 < s95 < 35e-6 and spread < 1.0e-6 and schur_ok
                 and (not at33["excluded"]) and at35["excluded"] and at44["excluded"] and at44["gaussian_z2"] > 10.0
                 and all(r["alpha_star"] > 0 for r in table["rows"] if 5e-6 <= r["lambda_m"] <= 100e-6)  # the data lean the other way in the window
                 and (math.isnan(at33["shape_residual"]) or at33["shape_residual"] < 0.05)
                 and 0.4 < at33["lambda_m"] / 33e-6 < 0.7)
    below = reach_below_limit()
    r25, r18, r13 = below
    below_ok = (3.0 < r25["times_too_weak"] < 20.0 and 100.0 < r18["times_too_weak"] < 300.0 and r13["times_too_weak"] > 1000.0
                and r13["mimic_at_table_floor"] and 10e-6 < r25["lambda_m"] < 12e-6 and 6.5e-6 < r18["lambda_m"] < 8e-6
                and not any(r["excluded"] for r in below))
    short = short_range_comparison()
    by_lam = {round(r["lambda_m"] * 1e6): r for r in short}
    short_ok = (all(r["geraci_over_balance"] is not None and r["geraci_over_balance"] > 1.0 for r in short if r["lambda_m"] >= 10e-6)
                and 4.0 < by_lam[10]["geraci_over_balance"] < 5.0 and 3000.0 < by_lam[10]["balance_alpha95_abs"] < 3200.0
                and by_lam[4]["balance_alpha95_abs"] is None    # the balance's table starts at 5 µm
                and 0.5 < by_lam[6]["geraci_over_balance"] < 0.8)   # at 6 µm the cantilever's |α| limit is the stronger
    need6 = reach_below_limit((17e-6,))[0]   # the smeared pull whose best mimic is the 6.3 µm row
    cantilever_over_need = by_lam[6]["geraci_alpha95_abs"] / abs(need6["alpha_eff"])
    short_ok = bool(short_ok and 6.0e-6 < need6["lambda_m"] < 6.6e-6 and 1500.0 < cantilever_over_need < 2600.0)
    recast_ok = recast_ok and below_ok and short_ok
    # the planted defect (single-separation edge match) must give the retired 44 µm, not a value below 35 µm
    defect_rejected = not (32e-6 < Recast(120, "log52-3000", n_sep=12).sigma_95(planted_defect=True) < 35e-6) if not planted_defect else None
    return {"table_rows": n_rows, "edge_crossing_lambda_m": edge, "sigma_95_m": s95, "variants_sigma_95_m": variants, "spread_m": spread,
            "schur_nuisance_orthogonal": {"sigma_95_equal_m": s95_schur_eq, "sigma_95_abs_torque_m": s95_schur_abs,
                                          "at_33um_equal": schur_eq_33, "at_33um_abs_torque": schur_abs_33},
            "at_33um": at33, "at_35um": at35, "at_edge_match_44um": at44, "retired_edge_match_sigma_m": EDGE_MATCH_SIGMA_M,
            "below_limit": below, "below_ok": below_ok, "short_range_comparison": short, "short_ok": short_ok, "cantilever_6um_limit_over_smeared_need": cantilever_over_need,
            "table_ok": table_ok, "edge_ok": edge_ok, "recast_ok": recast_ok, "defect_rejected": defect_rejected,
            "ok": bool(recast_ok and (defect_rejected is None or defect_rejected))}


if __name__ == "__main__":
    import sys, time
    t0 = time.time()
    res = check_recast(planted_defect="--planted-defect" in sys.argv, quick="--full" not in sys.argv)
    res["seconds"] = round(time.time() - t0, 1)
    print(json.dumps(res, indent=2, default=str))
