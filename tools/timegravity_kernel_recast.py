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


_DEFICIT_CACHE: dict = {}


class Recast:
    """One recast configuration (harmonic, separation grid, λ window) with the Yukawa shapes computed once."""

    def __init__(self, n_fold: int = 120, grid: str = "log52-3000", n_sep: int | None = None, lam_min: float = 10e-6, lam_max: float = 400e-6,
                 weighting: str = "equal"):
        self.table = load_table()
        self.rows = {r["lambda_m"]: r for r in self.table["rows"]}
        self.lams = [r["lambda_m"] for r in self.table["rows"] if lam_min <= r["lambda_m"] <= lam_max]
        self.n_fold, self.grid = n_fold, grid
        self.seps = separation_grid(grid, n_sep)
        self.t_newton = [wedge_torque(n_fold, s, "newton") for s in self.seps]
        self.shapes = unit_yukawa_shapes(n_fold, self.seps, self.lams, self.t_newton)
        self.weighting = weighting
        self.weights = [t * t for t in self.t_newton] if weighting == "abs_torque" else None

    def at_sigma(self, sigma: float, planted_defect: bool = False) -> dict:
        """Best-mimic λ, effective strength, shape residual, the published signed limit there and the verdict."""
        if planted_defect:
            # The retired reading: compare the deficit at the single 52 µm separation with the |α| = 1 edge there (no shapes, no limits table).
            d52 = 1.0 - wedge_torque(self.n_fold, EW_S_MIN_M, "smeared", sigma=sigma) / wedge_torque(self.n_fold, EW_S_MIN_M)
            edge = 1.0 - wedge_torque(self.n_fold, EW_S_MIN_M, "yukawa", lam=EDGE_LAMBDA_M, alpha=-1.0) / wedge_torque(self.n_fold, EW_S_MIN_M)
            return {"sigma_m": sigma, "lambda_m": EDGE_LAMBDA_M, "alpha_eff": -d52 / edge, "shape_residual": float("nan"),
                    "alpha95_minus": -1.0, "excluded": d52 > edge, "gaussian_z2": float("nan")}
        key = (self.n_fold, tuple(self.seps), sigma)  # the deficits do not depend on the weighting, so the variants share them
        d = _DEFICIT_CACHE.get(key)
        if d is None:
            d = _DEFICIT_CACHE[key] = smeared_deficit(self.n_fold, self.seps, sigma, self.t_newton)
        best = None
        for lam in self.lams:
            a_eff, resid = project(d, self.shapes[lam], self.weights)
            if best is None or resid < best[1]:
                best = (lam, resid, a_eff)
        lam, resid, a_eff = best
        row = self.rows[lam]
        return {"sigma_m": sigma, "lambda_m": lam, "alpha_eff": a_eff, "shape_residual": resid, "alpha_star": row["alpha_star"],
                "sigma_alpha": row["sigma_alpha"], "alpha95_minus": row["alpha95_minus"], "excluded": a_eff < row["alpha95_minus"],
                # a reading aid only: the thesis' signed limit encodes the exact, asymmetric Δχ² = 6.17 boundary; this is the Gaussian z² about α*
                "gaussian_z2": ((a_eff - row["alpha_star"]) / row["sigma_alpha"]) ** 2}

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
    variants = {"120-log52-3000-12": s95,
                "120-log52-3000-12-abs_torque": Recast(120, "log52-3000", n_sep=12, lam_min=10e-6, lam_max=100e-6, weighting="abs_torque").sigma_95(planted_defect=planted_defect)}
    if not quick:
        for n_fold in (120, 18):
            for grid in ("log52-3000", "lin52-3000", "log52-200", "log52-100"):
                variants[f"{n_fold}-{grid}"] = Recast(n_fold, grid, lam_min=10e-6, lam_max=400e-6).sigma_95(planted_defect=planted_defect)
    spread = max(variants.values()) - min(variants.values()) if all(math.isfinite(v) for v in variants.values()) else float("inf")
    recast_ok = (table_ok and edge_ok and 32e-6 < s95 < 35e-6 and spread < 1.0e-6
                 and (not at33["excluded"]) and at35["excluded"] and at44["excluded"] and at44["gaussian_z2"] > 10.0
                 and all(r["alpha_star"] > 0 for r in table["rows"] if 5e-6 <= r["lambda_m"] <= 100e-6)  # the data lean the other way in the window
                 and (math.isnan(at33["shape_residual"]) or at33["shape_residual"] < 0.05)
                 and 0.4 < at33["lambda_m"] / 33e-6 < 0.7)
    # the planted defect (single-separation edge match) must give the retired 44 µm, not a value below 35 µm
    defect_rejected = not (32e-6 < Recast(120, "log52-3000", n_sep=12).sigma_95(planted_defect=True) < 35e-6) if not planted_defect else None
    return {"table_rows": n_rows, "edge_crossing_lambda_m": edge, "sigma_95_m": s95, "variants_sigma_95_m": variants, "spread_m": spread,
            "at_33um": at33, "at_35um": at35, "at_edge_match_44um": at44, "retired_edge_match_sigma_m": EDGE_MATCH_SIGMA_M,
            "table_ok": table_ok, "edge_ok": edge_ok, "recast_ok": recast_ok, "defect_rejected": defect_rejected,
            "ok": bool(recast_ok and (defect_rejected is None or defect_rejected))}


if __name__ == "__main__":
    import sys, time
    t0 = time.time()
    res = check_recast(planted_defect="--planted-defect" in sys.argv, quick="--full" not in sys.argv)
    res["seconds"] = round(time.time() - t0, 1)
    print(json.dumps(res, indent=2, default=str))
