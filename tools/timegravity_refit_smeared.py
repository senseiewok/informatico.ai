#!/usr/bin/env python3
"""Profile-likelihood refit of a short-range gravity dataset for the smeared pair potential V = −G m m′ erf(r/2σ)/r.

Companion to Time & Gravity · T.05 and T.06 (tools/timegravity_kernel_wedge.py). Standard library only.

What it does. Given harmonic torque measurements T_i ± δT_i at facing-surface separations s_i for the Eöt-Wash 2020 wedge geometry
(18ω and 120ω), it fits
    model(s) = γ · T_shape(s + s₀)
with γ a scale factor and s₀ a separation offset (the two parameters the 2020 analysis floats besides a roughness correction), for
three shapes: Newton; the smeared potential at a smearing width σ; and Newton plus a gravitational-strength Yukawa (α = −1) of range λ.
For each σ (and each λ) on a geometric grid, γ is solved in closed form and χ² recorded; s₀ is fitted on the Newtonian shape and held
there for the profiles. The 95 % one-sided bound on σ is where χ²(σ) − χ²_min = 3.84 (one profiled parameter); the same for λ.

Why. The 2020 letter's Yukawa analysis cannot tell what the erf shape does to its fit; this script shows the shape and the method on
the site's kernel so that anyone with the data (the collaboration) can run or adapt it. It is not a claim about the published data,
which the site does not hold.

Demo (--demo). Synthetic Newtonian data at 24 separations between 52 µm and 3.0 mm with 1 % Gaussian errors (fixed seed), and a
second set generated with σ = 75 µm, to show that the first returns a bound and the second recovers σ. --quick uses fewer points
and a coarser grid (for the test suite). --data FILE fits a CSV with columns s_m,harmonic,torque_Nm,sigma_Nm.

Caveat. The vertical thickness integral here uses an 8-point Gauss–Legendre rule per plate (the kernel's verifier uses 24) for speed;
on the Fig.-3 probe the difference is below 1e-5 relative. Harmonics other than 18 and 120 are not modelled.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from timegravity_kernel import G_NEWTON  # noqa: E402
from timegravity_kernel_isl import EW_T_ATTRACTOR_M, EW_T_DETECTOR_M, gauss_legendre, plate_mode_ratio  # noqa: E402
from timegravity_kernel_wedge import EW_WEDGES, RHO_CONTRAST, _K_NODES, radial_table, z_newton, z_yukawa  # noqa: E402

DELTA_CHI2_95 = 3.84


class WedgeShapes:
    """Torque shapes for one harmonic, with the radial table cached and a lighter vertical rule."""

    def __init__(self, n_fold: int, gl_points: int = 8):
        self.n = n_fold
        w = EW_WEDGES[n_fold]
        beta = math.radians(w["wedge_deg"] / 2.0)
        self.pref = 8.0 * n_fold * G_NEWTON * RHO_CONTRAST * RHO_CONTRAST * math.sin(n_fold * beta) ** 2
        self.table = radial_table(n_fold)
        self.gl = gauss_legendre(gl_points)

    def _z_smeared(self, k: float, s: float, sigma: float) -> float:
        xs, ws = self.gl
        t1, t2 = EW_T_DETECTOR_M, EW_T_ATTRACTOR_M
        total = 0.0
        for xi, wi in zip(xs, ws):
            z1 = 0.5 * t1 * (xi + 1.0)
            for xj, wj in zip(xs, ws):
                gap = s + z1 + 0.5 * t2 * (xj + 1.0)
                total += wi * wj * math.exp(-k * gap) * plate_mode_ratio(k, gap, sigma)
        return total * 0.25 * t1 * t2

    def torque(self, s: float, kind: str = "newton", sigma: float | None = None, lam: float | None = None, alpha: float = -1.0) -> float:
        total = 0.0
        for (k, wk), r in zip(_K_NODES, self.table):
            if kind == "newton":
                z = z_newton(k, s, EW_T_DETECTOR_M, EW_T_ATTRACTOR_M)
            elif kind == "smeared":
                z = self._z_smeared(k, s, sigma)
            else:
                z = z_newton(k, s, EW_T_DETECTOR_M, EW_T_ATTRACTOR_M) + alpha * z_yukawa(k, s, EW_T_DETECTOR_M, EW_T_ATTRACTOR_M, lam)
            total += wk * r * r * z
        return self.pref * total


def best_scale(obs: list[float], err: list[float], model: list[float]) -> tuple[float, float]:
    """Closed-form γ minimising χ² for model(s) = γ·shape(s), and the χ² at that γ."""
    num = sum(o * m / (e * e) for o, e, m in zip(obs, err, model))
    den = sum(m * m / (e * e) for e, m in zip(err, model))
    gamma = num / den if den > 0 else 0.0
    chi2 = sum(((o - gamma * m) / e) ** 2 for o, e, m in zip(obs, err, model))
    return gamma, chi2


def fit_offset_newton(rows: list[dict], shapes: dict[int, WedgeShapes], s0_range_m: float = 4e-6, steps: int = 9) -> tuple[float, float, float]:
    """Fit s₀ (grid then parabolic refinement) and γ on the Newtonian shape; returns (s0, gamma, chi2)."""
    obs = [r["torque"] for r in rows]
    err = [r["err"] for r in rows]

    def chi2_at(s0: float) -> tuple[float, float]:
        model = [shapes[r["harmonic"]].torque(r["s"] + s0) for r in rows]
        return best_scale(obs, err, model)

    grid = [-s0_range_m + 2 * s0_range_m * i / (steps - 1) for i in range(steps)]
    vals = [chi2_at(s0) for s0 in grid]
    i = min(range(steps), key=lambda j: vals[j][1])
    s0 = grid[i]
    if 0 < i < steps - 1:
        y0, y1, y2 = vals[i - 1][1], vals[i][1], vals[i + 1][1]
        h = grid[1] - grid[0]
        denom = y0 - 2 * y1 + y2
        if denom > 0:
            s0 = grid[i] - 0.5 * h * (y2 - y0) / denom
    gamma, chi2 = chi2_at(s0)
    return s0, gamma, chi2


def profile(rows: list[dict], shapes: dict[int, WedgeShapes], s0: float, kind: str, grid: list[float]) -> list[dict]:
    obs = [r["torque"] for r in rows]
    err = [r["err"] for r in rows]
    out = []
    for p in grid:
        if kind == "smeared":
            model = [shapes[r["harmonic"]].torque(r["s"] + s0, "smeared", sigma=p) for r in rows]
        else:
            model = [shapes[r["harmonic"]].torque(r["s"] + s0, "yukawa", lam=p) for r in rows]
        gamma, chi2 = best_scale(obs, err, model)
        out.append({"param_m": p, "gamma": gamma, "chi2": chi2})
    return out


def bound_95(prof: list[dict], chi2_min: float) -> float | None:
    """Smallest grid parameter at which χ² exceeds χ²_min + 3.84, interpolated in log(param); None if never exceeded."""
    prev = None
    for p in prof:
        if p["chi2"] - chi2_min > DELTA_CHI2_95:
            if prev is None:
                return p["param_m"]
            f = (DELTA_CHI2_95 - (prev["chi2"] - chi2_min)) / (p["chi2"] - prev["chi2"])
            return math.exp(math.log(prev["param_m"]) + f * (math.log(p["param_m"]) - math.log(prev["param_m"])))
        prev = p
    return None


def interval_95(prof: list[dict]) -> list[float]:
    """Two-sided 95 % interval around the profile minimum, crossings interpolated in log(param); grid edges when not crossed."""
    i = min(range(len(prof)), key=lambda j: prof[j]["chi2"])
    c0 = prof[i]["chi2"]

    def cross(a: dict, b: dict) -> float:
        f = (DELTA_CHI2_95 - (a["chi2"] - c0)) / (b["chi2"] - a["chi2"])
        return math.exp(math.log(a["param_m"]) + f * (math.log(b["param_m"]) - math.log(a["param_m"])))

    lo = prof[0]["param_m"]
    for j in range(i, 0, -1):
        if prof[j - 1]["chi2"] - c0 > DELTA_CHI2_95:
            lo = cross(prof[j], prof[j - 1])
            break
    hi = prof[-1]["param_m"]
    for j in range(i, len(prof) - 1):
        if prof[j + 1]["chi2"] - c0 > DELTA_CHI2_95:
            hi = cross(prof[j], prof[j + 1])
            break
    return [lo, hi]


def geometric_grid(lo: float, hi: float, n: int) -> list[float]:
    return [lo * (hi / lo) ** (i / (n - 1)) for i in range(n)]


def synthetic(shapes: dict[int, WedgeShapes], seps: list[float], rel_err: float, seed: int, sigma_true: float | None) -> list[dict]:
    rng = random.Random(seed)
    rows = []
    for n in (120, 18):
        for s in seps:
            truth = shapes[n].torque(s) if sigma_true is None else shapes[n].torque(s, "smeared", sigma=sigma_true)
            err = rel_err * shapes[n].torque(s)
            rows.append({"s": s, "harmonic": n, "torque": truth + rng.gauss(0.0, err), "err": err})
    return rows


def read_csv(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8", newline="") as f:
        for rec in csv.DictReader(f):
            rows.append({"s": float(rec["s_m"]), "harmonic": int(rec["harmonic"]), "torque": float(rec["torque_Nm"]), "err": float(rec["sigma_Nm"])})
    return rows


def run_fit(rows: list[dict], sigma_grid: list[float], lambda_grid: list[float], gl_points: int) -> dict:
    shapes = {n: WedgeShapes(n, gl_points) for n in sorted({r["harmonic"] for r in rows})}
    s0, gamma_n, chi2_n = fit_offset_newton(rows, shapes)
    prof_s = profile(rows, shapes, s0, "smeared", sigma_grid)
    prof_l = profile(rows, shapes, s0, "yukawa", lambda_grid)
    chi2_min_s = min(min(p["chi2"] for p in prof_s), chi2_n)
    chi2_min_l = min(min(p["chi2"] for p in prof_l), chi2_n)
    best_s = min(prof_s, key=lambda p: p["chi2"])
    prefers_smearing = best_s["chi2"] < chi2_n - DELTA_CHI2_95
    return {
        "n_points": len(rows), "newton": {"s0_m": s0, "gamma": gamma_n, "chi2": chi2_n, "dof": len(rows) - 2},
        "smeared_profile": prof_s, "smeared_best": best_s if prefers_smearing else None,
        "sigma_95_upper_m": None if prefers_smearing else bound_95(prof_s, chi2_min_s),
        "sigma_95_interval_m": interval_95(prof_s) if prefers_smearing else None,
        "yukawa_alpha_minus_1_profile": prof_l, "lambda_95_upper_m": bound_95(prof_l, chi2_min_l),
        "note": "s0 fitted on the Newtonian shape and held for the profiles; gamma refit at every grid point; 95 % = delta chi2 3.84",
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--demo", action="store_true", help="synthetic Newtonian data and a sigma = 75 um injection")
    ap.add_argument("--quick", action="store_true", help="fewer separations and a lighter vertical rule")
    ap.add_argument("--data", type=Path, help="CSV with s_m,harmonic,torque_Nm,sigma_Nm")
    ap.add_argument("--rel-err", type=float, default=0.01)
    ap.add_argument("--seed", type=int, default=20261109)
    args = ap.parse_args(argv)
    gl = 6 if args.quick else 8
    n_sep = 8 if args.quick else 24
    sigma_grid = geometric_grid(15e-6, 200e-6, 13)
    lambda_grid = geometric_grid(10e-6, 300e-6, 13)
    if args.data:
        res = run_fit(read_csv(args.data), sigma_grid, lambda_grid, gl)
        print(json.dumps({"status": "DONE", "fit": res}, indent=2))
        return 0
    if not args.demo:
        ap.print_help()
        return 2
    shapes = {120: WedgeShapes(120, gl), 18: WedgeShapes(18, gl)}
    seps = geometric_grid(52e-6, 3.0e-3, n_sep)
    newton_rows = synthetic(shapes, seps, args.rel_err, args.seed, None)
    injected_rows = synthetic(shapes, seps, args.rel_err, args.seed, 75e-6)
    fit_n = run_fit(newton_rows, sigma_grid, lambda_grid, gl)
    fit_i = run_fit(injected_rows, sigma_grid, lambda_grid, gl)
    ok = (fit_n["sigma_95_upper_m"] is not None and 20e-6 < fit_n["sigma_95_upper_m"] < 120e-6
          and fit_i["smeared_best"] is not None and 50e-6 < fit_i["smeared_best"]["param_m"] < 110e-6
          and fit_i["newton"]["chi2"] > fit_i["smeared_best"]["chi2"] + DELTA_CHI2_95)
    print(json.dumps({
        "status": "PASS" if ok else "FAIL", "quick": args.quick, "rel_err": args.rel_err, "separations_m": seps,
        "newtonian_data": {"chi2_newton": fit_n["newton"]["chi2"], "dof": fit_n["newton"]["dof"], "s0_m": fit_n["newton"]["s0_m"], "gamma": fit_n["newton"]["gamma"],
                           "sigma_95_upper_m": fit_n["sigma_95_upper_m"], "lambda_95_upper_m_alpha_minus_1": fit_n["lambda_95_upper_m"]},
        "injected_sigma_75um": {"chi2_newton": fit_i["newton"]["chi2"], "smeared_best": fit_i["smeared_best"], "sigma_95_interval_m": fit_i["sigma_95_interval_m"]},
        "smeared_profile_newtonian_data": [{"sigma_um": round(p["param_m"] * 1e6, 2), "chi2": round(p["chi2"], 3)} for p in fit_n["smeared_profile"]],
    }, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
