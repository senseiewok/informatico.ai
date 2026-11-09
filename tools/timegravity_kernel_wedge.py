#!/usr/bin/env python3
"""Wedge-pattern Fourier–Bessel torque kernel for Time & Gravity · T.05 (standard library only, own Bessel functions):
the full Eöt-Wash 2020 test-body geometry under Newton, the smeared pair potential erf(r/2σ)/r, and a Yukawa.

Geometry (J. G. Lee, "A Fourier-Bessel Test of the Gravitational Inverse-Square Law", dissertation, University of Washington
2020, hdl.handle.net/1773/45542; Tables 4.1–4.5 and 4.8; the PRL 124, 101101 letter gives only the pattern diameter): two
concentric sets of wedge-shaped holes cut from platinum foils and filled with glue; 120-fold wedges between 13.004 and 22.998 mm
subtending 1.490° each (nominal 1.5°, so 50 % duty), 18-fold wedges between 23.505 and 26.000 mm subtending 9.984° (nominal 10°);
detector foils about 54 µm thick, attractor foils about 99 µm; glue (Stycast 1266) 1.162 g/cm³ against platinum 21.45 g/cm³;
the same pattern on detector and attractor; separation s between facing surfaces.

Formalism (Lee, Adelberger, Marcoline, Terrano & Heckel, Class. Quantum Grav. 38, 085020, 2021, Eqs. 7–19; rederived here):
    1/|r₁ − r₂| = Σ_m e^{im(φ₁−φ₂)} ∫₀^∞ dk J_m(kρ₁) J_m(kρ₂) e^{−k|z₁−z₂|}.
    An N-fold wedge pattern of angular half-width β has azimuthal components only at m = hN, each carrying N·2 sin(mβ)/m; the
    radial factor is R(m, k) = ∫_{r₀}^{r₁} ρ J_m(kρ) dρ; the vertical factor for two slabs of thickness t₁, t₂ whose facing surfaces
    are s apart is Z(k, s) = e^{−ks}(1 − e^{−kt₁})(1 − e^{−kt₂})/k². For h = 1 and the optimal β = π/2N the torque amplitude is
        T_N(s) = 8 N G ρc² sin²(Nβ) ∫₀^∞ dk R₁(N, k) R₂(N, k) Z(k, s),
    with ρc the density contrast (platinum minus glue). The smeared potential multiplies the vertical kernel by the plate-mode ratio
    of the smeared-gravity kernel, Z_σ(k, s) = ∫∫ dz₁dz₂ e^{−k(s+z₁+z₂)} R_σ(k, s+z₁+z₂); a Yukawa adds α (k/γ) e^{−γs}(1 − e^{−γt₁})
    (1 − e^{−γt₂})/γ², γ = √(k² + λ⁻²). R(m, k) is evaluated with the paper's Bessel series (their Eq. 16),
        R(m, k) = (2m/k) Σ_j (n/((n−1)(n+1))) [r₁ J_n(kr₁) − r₀ J_n(kr₀)],  n = m + 2j + 1,
    whose truncation must grow with k·r₁ (the terms only die once n exceeds the argument); the kernel checks the series against
    direct Gauss–Legendre quadrature of ρ J_m(kρ), and its Bessel functions (Miller backward recurrence, Hankel asymptotics for
    J₀, J₁) against the integral representation J_n(x) = (1/π)∫₀^π cos(nτ − x sin τ) dτ.

Checks: the Newtonian 120-fold torque the kernel gives, 1.51 fN·m at 72 µm, is compared with what the letter implies there (its
    magnetic subtraction of 0.0165 fN·m is "roughly 1 %" of the signal, about 1.6 fN·m); the smeared deficits are compared with the
    one-mode lower bound of the smeared-gravity kernel (the full pattern must remove more, since its wavenumbers exceed N/r_out).

Planted defect: the radial series truncated at a fixed 250 terms whatever k (the "sufficient" count the paper quotes for its own
    k range); at k·r₁ beyond the order the series stops converging, the double entry against quadrature fails, and the verifier must
    reject it.
"""
from __future__ import annotations

import math

from timegravity_kernel import G_NEWTON
from timegravity_kernel_dispute import TN_D_M, TN_L_M, TN_M_KG, tn_critical_separation_from_e_minus, tn_survival
from timegravity_kernel_isl import EW_T_ATTRACTOR_M, EW_T_DETECTOR_M, EW_YUKAWA_EDGE_LAMBDA_M, gauss_legendre, plate_mode_ratio

# Lee 2020 dissertation, Tables 4.3 (radii, mm), 4.5 (subtended angles, degrees), 4.8 (glue density)
EW_WEDGES = {
    120: {"r_inner_m": 13.004e-3, "r_outer_m": 22.998e-3, "wedge_deg": 1.490},
    18: {"r_inner_m": 23.505e-3, "r_outer_m": 26.000e-3, "wedge_deg": 9.984},
}
RHO_PLATINUM = 21450.0
RHO_GLUE = 1162.0
RHO_CONTRAST = RHO_PLATINUM - RHO_GLUE
EW_T120_AT_72UM_IMPLIED_FNM = 1.65      # 0.0165 fN·m magnetic contribution, "roughly 1 %" of the 120ω torque at s = 72 µm
K_MIN = 1.0
K_MAX = 4.0e5
K_PANELS_PER_DECADE = 6
WEDGE_TOL = 1e-6

_GL16 = gauss_legendre(16)
_GL24 = gauss_legendre(24)


# ---- Bessel functions of the first kind, integer order
def bessel_j0_j1(x: float) -> tuple[float, float]:
    """J₀(x), J₁(x) for x > 0: power series below 12, Hankel asymptotic expansion above (error about 1e-9)."""
    if x < 12.0:
        s0 = s1 = 0.0
        t0, t1 = 1.0, x / 2.0
        for k in range(60):
            s0 += t0
            s1 += t1
            t0 *= -(x * x / 4.0) / ((k + 1) ** 2)
            t1 *= -(x * x / 4.0) / ((k + 1) * (k + 2))
            if abs(t0) < 1e-18 and abs(t1) < 1e-18:
                break
        return s0, s1
    out = []
    for nu in (0.0, 1.0):
        mu = 4.0 * nu * nu
        a = [1.0]
        for k in range(1, 12):
            a.append(a[-1] * (mu - (2 * k - 1) ** 2) / (k * 8.0 * x))
        p = sum(((-1) ** (k // 2)) * a[k] for k in range(0, 12, 2))
        q = sum(((-1) ** ((k - 1) // 2)) * a[k] for k in range(1, 12, 2))
        chi = x - (nu / 2.0 + 0.25) * math.pi
        out.append(math.sqrt(2.0 / (math.pi * x)) * (p * math.cos(chi) - q * math.sin(chi)))
    return out[0], out[1]


def bessel_j_all(nmax: int, x: float) -> list[float]:
    """J₀(x) … J_nmax(x) for x > 0: forward recurrence from J₀, J₁ where it is stable (x well above the order), otherwise
    Miller's backward recurrence normalised with J₀ + 2 Σ J₂ₖ = 1."""
    if x > nmax + 20:
        j0, j1 = bessel_j0_j1(x)
        out = [j0, j1]
        for n in range(1, nmax):
            out.append(2.0 * n / x * out[-1] - out[-2])
        return out[:nmax + 1]
    start = int(max(nmax, x) + 15 + 2 * math.sqrt(max(nmax, x)))
    if start % 2:
        start += 1
    vals = [0.0] * (start + 1)
    jp1, j = 0.0, 1e-300
    vals[start] = j
    for n in range(start, 0, -1):
        jm1 = 2.0 * n / x * j - jp1
        jp1, j = j, jm1
        vals[n - 1] = j
        if abs(j) > 1e250:
            vals = [v * 1e-250 for v in vals]
            j *= 1e-250
            jp1 *= 1e-250
    norm = vals[0] + 2.0 * sum(vals[2:start + 1:2])
    return [v / norm for v in vals[:nmax + 1]]


def bessel_j_integral(n: int, x: float, steps: int = 20000) -> float:
    """Independent check: J_n(x) = (1/π)∫₀^π cos(nτ − x sin τ) dτ by the trapezoid rule (spectrally accurate for a periodic integrand)."""
    h = math.pi / steps
    total = 0.0
    for i in range(steps + 1):
        tau = i * h
        w = 0.5 if i in (0, steps) else 1.0
        total += w * math.cos(n * tau - x * math.sin(tau))
    return total * h / math.pi


# ---- radial pattern function
def wedge_radial_series(m: int, r0: float, r1: float, k: float, planted_defect: bool = False) -> float:
    """R(m, k) = ∫_{r₀}^{r₁} ρ J_m(kρ) dρ by the Bessel series (CQG 2021 Eq. 16); the truncation grows with k·r₁ unless the
    defect is planted (fixed 250 terms)."""
    jmax = 250 if planted_defect else max(250, int((k * r1 - m) / 2) + 40)
    nmax = m + 2 * jmax + 1
    b1 = bessel_j_all(nmax, k * r1)
    b0 = bessel_j_all(nmax, k * r0)
    total = 0.0
    for j in range(jmax + 1):
        n = m + 2 * j + 1
        total += n / ((n - 1.0) * (n + 1.0)) * (r1 * b1[n] - r0 * b0[n])
    return 2.0 * m * total / k


def wedge_radial_quadrature(m: int, r0: float, r1: float, k: float) -> float:
    """Direct Gauss–Legendre quadrature of ρ J_m(kρ) on panels narrower than half an oscillation."""
    xs, ws = _GL16
    npan = max(1, int((r1 - r0) * k / 3.0) + 1)
    edges = [r0 + (r1 - r0) * i / npan for i in range(npan + 1)]
    total = 0.0
    for a, b in zip(edges[:-1], edges[1:]):
        for xi, wi in zip(xs, ws):
            rho = 0.5 * (b - a) * xi + 0.5 * (a + b)
            total += 0.5 * (b - a) * wi * rho * bessel_j_all(m, k * rho)[m]
    return total


# ---- vertical factors and the k integral
def z_newton(k: float, s: float, t1: float, t2: float) -> float:
    return math.exp(-k * s) * (1.0 - math.exp(-k * t1)) * (1.0 - math.exp(-k * t2)) / (k * k)


def z_yukawa(k: float, s: float, t1: float, t2: float, lam: float) -> float:
    g = math.sqrt(k * k + 1.0 / (lam * lam))
    return (k / g) * math.exp(-g * s) * (1.0 - math.exp(-g * t1)) * (1.0 - math.exp(-g * t2)) / (g * g)


def z_smeared(k: float, s: float, t1: float, t2: float, sigma: float) -> float:
    xs, ws = _GL24
    total = 0.0
    for xi, wi in zip(xs, ws):
        z1 = 0.5 * t1 * (xi + 1.0)
        for xj, wj in zip(xs, ws):
            gap = s + z1 + 0.5 * t2 * (xj + 1.0)
            total += wi * wj * math.exp(-k * gap) * plate_mode_ratio(k, gap, sigma)
    return total * 0.25 * t1 * t2


def k_nodes(kmin: float = K_MIN, kmax: float = K_MAX, per_decade: int = K_PANELS_PER_DECADE) -> list[tuple[float, float]]:
    """Gauss–Legendre nodes and weights on log-spaced panels of k."""
    xs, ws = _GL16
    npan = int(math.log10(kmax / kmin) * per_decade) + 1
    edges = [kmin * (kmax / kmin) ** (i / npan) for i in range(npan + 1)]
    nodes = []
    for a, b in zip(edges[:-1], edges[1:]):
        for xi, wi in zip(xs, ws):
            nodes.append((0.5 * (b - a) * xi + 0.5 * (a + b), 0.5 * (b - a) * wi))
    return nodes


_K_NODES = k_nodes()
_R_CACHE: dict[tuple[int, bool], list[float]] = {}


def radial_table(n_fold: int, planted_defect: bool = False) -> list[float]:
    """R(N, k) at every k node for the N-fold pattern (same radii on detector and attractor), cached."""
    key = (n_fold, planted_defect)
    if key not in _R_CACHE:
        w = EW_WEDGES[n_fold]
        _R_CACHE[key] = [wedge_radial_series(n_fold, w["r_inner_m"], w["r_outer_m"], k, planted_defect) for k, _ in _K_NODES]
    return _R_CACHE[key]


def wedge_torque(n_fold: int, s: float, kind: str = "newton", sigma: float | None = None, lam: float | None = None,
                 alpha: float = 0.0, t1: float = EW_T_DETECTOR_M, t2: float = EW_T_ATTRACTOR_M, planted_defect: bool = False) -> float:
    """Torque amplitude (N·m) of the N-fold harmonic at facing-surface separation s under Newton, the smeared potential, or
    Newton plus a Yukawa α e^{−r/λ}."""
    w = EW_WEDGES[n_fold]
    beta = math.radians(w["wedge_deg"] / 2.0)
    pref = 8.0 * n_fold * G_NEWTON * RHO_CONTRAST * RHO_CONTRAST * math.sin(n_fold * beta) ** 2
    table = radial_table(n_fold, planted_defect)
    total = 0.0
    for (k, wk), r in zip(_K_NODES, table):
        if kind == "newton":
            z = z_newton(k, s, t1, t2)
        elif kind == "smeared":
            z = z_smeared(k, s, t1, t2, sigma)
        elif kind == "yukawa":
            z = z_newton(k, s, t1, t2) + alpha * z_yukawa(k, s, t1, t2, lam)
        else:
            raise ValueError(kind)
        total += wk * r * r * z
    return pref * total


def wedge_deficit(sigma: float, n_fold: int = 120, s: float = 52e-6, planted_defect: bool = False) -> float:
    """Fraction of the N-fold Newtonian torque the smeared potential removes at separation s, on the full wedge pattern."""
    return 1.0 - wedge_torque(n_fold, s, "smeared", sigma=sigma, planted_defect=planted_defect) / wedge_torque(n_fold, s, planted_defect=planted_defect)


def wedge_yukawa_edge_deficit(n_fold: int = 120, s: float = 52e-6, alpha: float = -1.0, lam: float = EW_YUKAWA_EDGE_LAMBDA_M) -> float:
    return 1.0 - wedge_torque(n_fold, s, "yukawa", lam=lam, alpha=alpha) / wedge_torque(n_fold, s)


def wedge_sigma_matching_edge(n_fold: int = 120, s: float = 52e-6) -> float:
    target = wedge_yukawa_edge_deficit(n_fold, s)
    lo, hi = 1e-5, 2e-4
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if wedge_deficit(mid, n_fold, s) > target:
            hi = mid
        else:
            lo = mid
        if hi / lo < 1.0 + 1e-9:
            break
    return math.sqrt(lo * hi)


def wedge_best_yukawa(sigma: float, n_fold: int = 120, seps: tuple[float, ...] = (52e-6, 72e-6, 100e-6, 150e-6, 200e-6, 300e-6, 500e-6, 1e-3)) -> dict:
    """The Yukawa (α, λ) whose N-fold deficit curve best mimics the smeared one over the given separations (equal weights):
    α by linear least squares at each λ on a geometric grid; a curve match, not a fit to data."""
    newton = [wedge_torque(n_fold, s) for s in seps]
    deficits = [1.0 - wedge_torque(n_fold, s, "smeared", sigma=sigma) / nw for s, nw in zip(seps, newton)]
    best = None
    lam = 10e-6
    while lam < 3e-4:
        unit = [wedge_torque(n_fold, s, "yukawa", lam=lam, alpha=1.0) / nw - 1.0 for s, nw in zip(seps, newton)]
        minus_alpha = sum(u * d for u, d in zip(unit, deficits)) / sum(u * u for u in unit)
        resid = sum((minus_alpha * u - d) ** 2 for u, d in zip(unit, deficits))
        if best is None or resid < best["residual"]:
            best = {"lambda_m": lam, "alpha": -minus_alpha, "residual": resid, "rms_deficit": math.sqrt(resid / len(seps))}
        lam *= 1.03
    return best


# ---- the window the estimate leaves the model
def model_window(sigma: float, m: float = TN_M_KG) -> dict:
    """What the Diósi–Penrose model (Trillo–Navascués form) can still do if its smearing is at most σ: the largest nearest
    separation that entangles, for the small-split limit and for the letter's 23 µm split, whether the letter's own geometry
    entangles, and example peak negativities and times at mass m (the criterion is mass-independent; times scale as 1/m²)."""
    out = {"sigma_m": sigma, "mass_kg": m}
    dc_small = tn_critical_separation_from_e_minus(sigma, sigma * 1e-4)
    dc_letter_split = tn_critical_separation_from_e_minus(sigma, TN_L_M)
    out["d_c_small_split_m"] = dc_small
    out["d_c_letter_split_m"] = dc_letter_split
    out["letter_geometry"] = tn_survival(TN_L_M, TN_D_M, m, sigma)
    examples = {}
    for split in (TN_L_M, 10e-6, 5e-6, 1e-6):
        dc = tn_critical_separation_from_e_minus(sigma, split)
        if dc:
            examples[f"split_{split * 1e6:.0f}um"] = {"d_c_m": dc, "at_half_d_c": tn_survival(split, 0.5 * dc, m, sigma)}
    out["examples"] = examples
    return out


def check_wedge(planted_defect: bool = False) -> dict:
    # 1. Bessel functions against the integral representation.
    probes = ((0, 5.0), (1, 30.0), (18, 10.0), (18, 200.0), (120, 100.0), (120, 500.0), (120, 3000.0), (621, 600.0), (621, 9000.0))
    bessel = [{"n": n, "x": x, "recurrence": bessel_j_all(n, x)[n], "integral": bessel_j_integral(n, x)} for n, x in probes]
    bessel_ok = all(abs(b["recurrence"] - b["integral"]) < 1e-9 for b in bessel)
    # 2. Radial series against quadrature, including k·r₁ beyond the fixed truncation.
    radial = []
    for n_fold in (120, 18):
        w = EW_WEDGES[n_fold]
        for k in (1000.0, 5000.0, 20000.0, 60000.0):
            ser = wedge_radial_series(n_fold, w["r_inner_m"], w["r_outer_m"], k, planted_defect)
            quad = wedge_radial_quadrature(n_fold, w["r_inner_m"], w["r_outer_m"], k)
            radial.append({"n_fold": n_fold, "k_per_m": k, "series": ser, "quadrature": quad, "rel_diff": abs(ser - quad) / max(abs(quad), 1e-300)})
    radial_ok = all(r["rel_diff"] < WEDGE_TOL for r in radial if abs(r["quadrature"]) > 1e-20)
    # 3. Newtonian torques and the letter's implied 120ω torque at 72 µm.
    newton = {f"{s * 1e6:.0f}um": {"T120_fNm": wedge_torque(120, s, planted_defect=planted_defect) * 1e15, "T18_fNm": wedge_torque(18, s, planted_defect=planted_defect) * 1e15}
              for s in (52e-6, 72e-6, 100e-6, 300e-6, 1e-3)}
    t120_72 = newton["72um"]["T120_fNm"]
    newton_ok = 0.7 * EW_T120_AT_72UM_IMPLIED_FNM < t120_72 < 1.3 * EW_T120_AT_72UM_IMPLIED_FNM
    # 4. Smeared deficits on the full pattern, the Yukawa edge, the matching σ, the mimic Yukawa, the deficit curve.
    by_sigma = {f"{sg * 1e6:.0f}um": {f"{n}fold": wedge_deficit(sg, n, planted_defect=planted_defect) for n in (120, 18)} for sg in (30e-6, 44e-6, 50e-6, 55e-6, 75e-6, 100e-6)}
    edge = {f"{n}fold": wedge_yukawa_edge_deficit(n) for n in (120, 18)}
    curve = {f"{s * 1e6:.0f}um": {"sigma_75um_120fold": wedge_deficit(75e-6, 120, s), "sigma_75um_18fold": wedge_deficit(75e-6, 18, s), "yukawa_edge_120fold": wedge_yukawa_edge_deficit(120, s)}
             for s in (52e-6, 72e-6, 100e-6, 150e-6, 200e-6, 300e-6, 500e-6)}
    sigma_match = wedge_sigma_matching_edge(120)
    mimic = wedge_best_yukawa(75e-6)
    wedge_ok = (by_sigma["75um"]["120fold"] > edge["120fold"] > by_sigma["30um"]["120fold"] and 30e-6 < sigma_match < 60e-6
                and curve["300um"]["sigma_75um_120fold"] < 2e-3 and mimic["lambda_m"] > EW_YUKAWA_EDGE_LAMBDA_M and mimic["alpha"] < -1.0)
    # 5. The window at the matching σ.
    window = model_window(sigma_match)
    window_ok = window["letter_geometry"]["last_entangled_time_s"] is None and window["d_c_small_split_m"] is not None and window["d_c_small_split_m"] < 0.86 * sigma_match
    # 6. The planted truncation is caught by the radial double entry.
    w18 = EW_WEDGES[18]
    bad_series = wedge_radial_series(18, w18["r_inner_m"], w18["r_outer_m"], 20000.0, planted_defect=True)
    good_quad = wedge_radial_quadrature(18, w18["r_inner_m"], w18["r_outer_m"], 20000.0)
    defect_rejected = abs(bad_series - good_quad) / abs(good_quad) > 1e-2   # the fixed truncation is off by a factor of ten here
    return {
        "geometry": EW_WEDGES, "rho_contrast_kg_m3": RHO_CONTRAST, "t_detector_m": EW_T_DETECTOR_M, "t_attractor_m": EW_T_ATTRACTOR_M,
        "bessel_probes": bessel, "bessel_ok": bessel_ok, "radial_probes": radial, "radial_ok": radial_ok,
        "newton_torques": newton, "t120_at_72um_implied_by_letter_fNm": EW_T120_AT_72UM_IMPLIED_FNM, "newton_ok": newton_ok,
        "deficit_at_52um_by_sigma": by_sigma, "yukawa_edge_deficit_at_52um": edge, "deficit_by_separation": curve,
        "sigma_matching_edge_120fold_m": sigma_match, "best_yukawa_for_sigma_75um_120fold": mimic,
        "ratio_sigma_75um_to_edge_120fold": by_sigma["75um"]["120fold"] / edge["120fold"], "wedge_ok": wedge_ok,
        "window_at_matching_sigma": window, "window_ok": window_ok, "defect_rejected": defect_rejected,
        "ok": bessel_ok and radial_ok and newton_ok and wedge_ok and window_ok and defect_rejected,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(check_wedge(), indent=2, default=str))
