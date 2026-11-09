#!/usr/bin/env python3
"""Smeared-gravity kernel for Time & Gravity · T.05 (standard library only): the model's softened pull set beside the
sub-millimetre inverse-square-law tests.

In the Diósi–Penrose model as Trillo & Navascués write it (PRD 111, L121101, 2025), the mass density is smeared over a width σ
and the master equation's imaginary part is a commutator with (G/2)∫∫ μ_σ μ_σ / |r − s|; for two masses that is the pair potential
−G m₁ m₂ erf(d/2σ)/d, Newton's for d ≫ σ and a constant below about σ (`tn_potential_ratio` in the dispute kernel; the dispute
kernel also checks that the model's phases become the Newtonian ones as σ → 0). The same potential must act between the test
bodies of any laboratory test of Newton's law. This kernel computes what the smearing does to the quantity those tests measure.

Plate modes. The smeared pair potential is the Newtonian potential between two Gaussian clouds of width σ, so its 3D Fourier
    transform is K̃(Q) = (4π/Q²) e^{−Q²σ²}. Two thin sheets with in-plane mass patterns at vertical separation s interact mode by
    mode in the in-plane wavenumber q: Newton gives (2π/q) e^{−qs}; writing 1/(q² + q_z²) as ∫₀^∞ e^{−u(q²+q_z²)} du, the q_z
    integral is Gaussian and the u integral is an incomplete-Gaussian pair, so the smeared sheet kernel is
        (2π/q) · ½ [ e^{−qs} erfc(qσ − s/2σ) + e^{qs} erfc(qσ + s/2σ) ],
    and the ratio to Newton is R(q, s; σ) = ½ [ erfc(qσ − s/2σ) + e^{2qs} erfc(qσ + s/2σ) ]  (`plate_mode_ratio`).
    Limits: R → 1 for σ → 0, for s ≫ σ and for q → 0; R → erfc(qσ) at s = 0. The closed form is checked against direct quadrature
    of ∫ dq_z cos(q_z s) e^{−(q²+q_z²)σ²}/(q² + q_z²) (`plate_mode_ratio_quadrature`); R is checked to fall monotonically with q and to stay within [0, 1].
    Plates of finite thickness carry the pattern through their thickness: the sheet kernel is integrated over both thicknesses with
    the gap s + z₁ + z₂ (`thick_plate_ratio`); a Yukawa V_N(r)[1 + α e^{−r/λ}] gets the same treatment with its sheet kernel
    (2π/q) e^{−qs} + α (2π/κ) e^{−κs}, κ = √(q² + λ⁻²) (`yukawa_thick_plate_ratio`).

Eöt-Wash 2020 (Lee, Adelberger, Cook, Fleischer & Heckel, PRL 124, 101101; arXiv:2002.11761). Platinum test bodies, detector
    54 µm and attractor 99 µm thick, 50 %-transparent hole patterns 52 mm across with 18-fold and 120-fold azimuthal symmetry;
    torques at 18ω and 120ω measured against the separation s between facing surfaces, 52 µm to 3.0 mm; known masses, calibrated
    scale; Newtonian fit χ² = 275.0 for 285 degrees of freedom; "any gravitational-strength Yukawa interaction must have
    λ < 38.6 µm" at 95 %. An N-fold pattern of outer radius r_out has its spectrum at q ≳ N/r_out (J_N(qr) is small for qr < N),
    and R falls with q, so the deficit at q = N/r_out bounds the deficit of the N-fold harmonic from below whatever the pattern's
    inner radius and hole shapes, which the paper does not give, up to the Bessel tail just below N/r_out (width about N^{1/3}
    in qr); the kernel also reports the deficit at q = (N − 2N^{1/3})/r_out, where that tail has died away, and the page says
    "about a tenth" rather than "at least". The kernel reports, for the 120-fold and 18-fold modes at the
    closest separation, the smeared deficit at several σ, the deficit of the Yukawa at the published edge (α = −1, λ = 38.6 µm),
    the σ whose deficit matches that edge, and the Yukawa (α, λ) that best mimics the smeared curve across the separation range.
    HUST 2020 (Tan et al., PRL 124, 051301; |α| ≤ 1 down to λ = 48 µm) is quoted as published: its geometry is not in open text.

The kernel compares one model's prediction with the published Yukawa envelope and does no more: the experiment's own fit, with
    its floating offset, roughness correction and calibrated scale, is not recomputed here, and the page says so.

Planted defect: the closed-form ratio drops its second term, e^{2qs} erfc(qσ + s/2σ). The limits then fail (R → ½ at q → 0 and
    for σ → 0) and the quadrature double entry disagrees, so the verifier must reject it.
"""
from __future__ import annotations

import math

from timegravity_kernel_dispute import TN_D_M, TN_L_M, TN_M_KG, tn_critical_sigma

EW_R_OUT_M = 26e-3           # hole-pattern diameter 52 mm
EW_T_DETECTOR_M = 54e-6
EW_T_ATTRACTOR_M = 99e-6
EW_S_MIN_M = 52e-6
EW_S_MAX_M = 3.0e-3
EW_N_FOLDS = (18, 120)
EW_YUKAWA_EDGE_LAMBDA_M = 38.6e-6   # α = −1 excluded beyond this range at 95 %
HUST_LAMBDA_M = 48e-6               # |α| ≤ 1 down to this range at 95 %
HUST_GAP_M = 210e-6                 # surface-to-surface gap of the 2020 apparatus (Murata, Fujiie & Suzuki 2026, Fig. 8 caption)
ISL_SIGMAS_M = (30e-6, 40e-6, 50e-6, 75e-6, 100e-6, 250e-6)
ISL_TOL = 1e-9
GL_POINTS = 24


def _log_erfc(x: float) -> float:
    """log erfc(x), stable for large positive x (asymptotic series beyond 25)."""
    if x > 25.0:
        x2 = x * x
        return -x2 - math.log(x * math.sqrt(math.pi)) + math.log(1.0 - 1.0 / (2.0 * x2) + 3.0 / (4.0 * x2 * x2))
    return math.log(math.erfc(x))


def plate_mode_ratio(q: float, s: float, sigma: float, planted_defect: bool = False) -> float:
    """Smeared-to-Newton ratio of the sheet kernel for in-plane wavenumber q (1/m) at vertical gap s under smearing σ."""
    a = q * sigma
    b = s / (2.0 * sigma)
    first = math.erfc(a - b)
    second = 0.0 if planted_defect else math.exp(2.0 * q * s + _log_erfc(a + b))
    return 0.5 * (first + second)


def plate_mode_ratio_quadrature(q: float, s: float, sigma: float, n: int = 200000) -> float:
    """Direct trapezoid quadrature of ∫ dq_z cos(q_z s) e^{−(q²+q_z²)σ²}/(q² + q_z²), divided by Newton's (π/q) e^{−qs}."""
    qz_max = max(40.0 / sigma, 60.0 / s if s > 0 else 0.0, 60.0 * q)
    h = qz_max / n
    total = 0.0
    for i in range(n + 1):
        qz = i * h
        w = 0.5 if i in (0, n) else 1.0
        total += w * math.cos(qz * s) * math.exp(-(q * q + qz * qz) * sigma * sigma) / (q * q + qz * qz)
    return (2.0 * total * h) / (math.pi / q * math.exp(-q * s))


def gauss_legendre(n: int) -> tuple[list[float], list[float]]:
    """Nodes and weights on [−1, 1] by Newton iteration on the Legendre recurrence."""
    xs, ws = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        dp = 1.0
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1.0)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-15:
                break
        xs.append(x)
        ws.append(2.0 / ((1.0 - x * x) * dp * dp))
    return xs, ws


_GL_X, _GL_W = gauss_legendre(GL_POINTS)


def thick_plate_ratio(q: float, s: float, sigma: float, t1: float = EW_T_DETECTOR_M, t2: float = EW_T_ATTRACTOR_M,
                      planted_defect: bool = False) -> float:
    """Smeared-to-Newton ratio of the q mode between two plates of thickness t1, t2 whose facing surfaces are s apart."""
    num = den = 0.0
    for xi, wi in zip(_GL_X, _GL_W):
        z1 = 0.5 * t1 * (xi + 1.0)
        for xj, wj in zip(_GL_X, _GL_W):
            gap = s + z1 + 0.5 * t2 * (xj + 1.0)
            base = wi * wj * math.exp(-q * gap)
            den += base
            num += base * plate_mode_ratio(q, gap, sigma, planted_defect)
    return num / den


def yukawa_thick_plate_ratio(q: float, s: float, alpha: float, lam: float, t1: float = EW_T_DETECTOR_M, t2: float = EW_T_ATTRACTOR_M) -> float:
    """Yukawa-to-Newton ratio of the q mode between two plates: sheet kernel (2π/q)e^{−qs} + α(2π/κ)e^{−κs}, κ = √(q² + λ⁻²)."""
    kappa = math.sqrt(q * q + 1.0 / (lam * lam))
    num = den = 0.0
    for xi, wi in zip(_GL_X, _GL_W):
        z1 = 0.5 * t1 * (xi + 1.0)
        for xj, wj in zip(_GL_X, _GL_W):
            gap = s + z1 + 0.5 * t2 * (xj + 1.0)
            den += wi * wj * math.exp(-q * gap) / q
            num += wi * wj * (math.exp(-q * gap) / q + alpha * math.exp(-kappa * gap) / kappa)
    return num / den


def pair_deviation_smeared(r: float, sigma: float) -> float:
    """Fraction of Newton's pull between two point elements r apart that the smeared potential removes: 1 − erf(r/2σ) = erfc(r/2σ)."""
    return math.erfc(r / (2.0 * sigma))


def pair_deviation_yukawa(r: float, alpha: float = 1.0, lam: float = HUST_LAMBDA_M) -> float:
    """Fraction of Newton's pull between two point elements r apart that a Yukawa α e^{−r/λ} adds or removes."""
    return alpha * math.exp(-r / lam)


def hust_pair_level(sigmas: tuple[float, ...] = (44e-6, 55e-6, 75e-6, 100e-6)) -> dict:
    """At the HUST 2020 gap, pair-level deviations for several σ against the α = 1 Yukawa at that group's 95 % edge. The apparatus
    (a 0.2 mm pendulum plate facing a 1.8 mm plate at 210 µm, a rotating eight-plate far source) is not modelled: its modulation and
    compensation scheme is not in open text."""
    return {"gap_m": HUST_GAP_M, "yukawa_edge_alpha_1_lambda_48um": pair_deviation_yukawa(HUST_GAP_M),
            "smeared_by_sigma": {f"{s * 1e6:.0f}um": pair_deviation_smeared(HUST_GAP_M, s) for s in sigmas},
            "sigma_matching_edge_m": 0.5 * HUST_GAP_M / _erfc_inverse(pair_deviation_yukawa(HUST_GAP_M))}


def _erfc_inverse(y: float) -> float:
    """x with erfc(x) = y, by bisection on [0, 10]."""
    lo, hi = 0.0, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if math.erfc(mid) > y:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def eotwash_mode_wavenumber(n_fold: int) -> float:
    """Lowest in-plane wavenumber of an n-fold pattern of outer radius EW_R_OUT_M (where the smearing bites least)."""
    return n_fold / EW_R_OUT_M


def eotwash_deficit(sigma: float, n_fold: int = 120, s: float = EW_S_MIN_M, planted_defect: bool = False) -> float:
    """Lower bound on the fraction of the n-fold Newtonian torque the smeared potential removes at separation s."""
    return 1.0 - thick_plate_ratio(eotwash_mode_wavenumber(n_fold), s, sigma, planted_defect=planted_defect)


def eotwash_yukawa_edge_deficit(n_fold: int = 120, s: float = EW_S_MIN_M, alpha: float = -1.0, lam: float = EW_YUKAWA_EDGE_LAMBDA_M) -> float:
    """Fraction of the n-fold Newtonian torque the Yukawa at the published 95 % edge removes at separation s."""
    return 1.0 - yukawa_thick_plate_ratio(eotwash_mode_wavenumber(n_fold), s, alpha, lam)


def sigma_matching_yukawa_edge(n_fold: int = 120, s: float = EW_S_MIN_M) -> float:
    """The σ whose n-fold deficit at s equals the published Yukawa edge's (geometric bisection)."""
    target = eotwash_yukawa_edge_deficit(n_fold, s)
    lo, hi = 1e-7, 1e-2
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if eotwash_deficit(mid, n_fold, s) > target:
            hi = mid
        else:
            lo = mid
        if hi / lo < 1.0 + 1e-10:
            break
    return math.sqrt(lo * hi)


def best_yukawa_fit(sigma: float, n_fold: int = 120, s_min: float = EW_S_MIN_M, s_max: float = EW_S_MAX_M, n_s: int = 40) -> dict:
    """The Yukawa (α, λ) that best mimics the smeared n-fold deficit curve over a log grid of separations (equal weights):
    α is linear least squares at each λ on a geometric grid; the λ with the smallest residual wins."""
    q = eotwash_mode_wavenumber(n_fold)
    seps = [s_min * (s_max / s_min) ** (i / n_s) for i in range(n_s + 1)]
    deficits = [1.0 - thick_plate_ratio(q, s, sigma) for s in seps]
    best = None
    lam = 5e-6
    while lam < 2e-3:
        unit = [yukawa_thick_plate_ratio(q, s, 1.0, lam) - 1.0 for s in seps]   # by linearity in α, the deficit per unit of −α
        denom = sum(u * u for u in unit)
        minus_alpha = sum(u * d for u, d in zip(unit, deficits)) / denom
        resid = sum((minus_alpha * u - d) ** 2 for u, d in zip(unit, deficits))
        if best is None or resid < best["residual"]:
            best = {"lambda_m": lam, "alpha": -minus_alpha, "residual": resid, "rms_deficit": math.sqrt(resid / len(seps))}
        lam *= 1.02
    return best


def check_isl(planted_defect: bool = False) -> dict:
    # 1. Closed form against direct quadrature, at six (q, s, σ) points.
    probes = [(eotwash_mode_wavenumber(120), 52e-6, 75e-6), (eotwash_mode_wavenumber(18), 52e-6, 75e-6), (4615.4, 300e-6, 75e-6),
              (4615.4, 52e-6, 250e-6), (1000.0, 1e-3, 100e-6), (4615.4, 2e-3, 75e-6)]
    quad = []
    for q, s, sg in probes:
        closed = plate_mode_ratio(q, s, sg, planted_defect)
        direct = plate_mode_ratio_quadrature(q, s, sg)
        quad.append({"q_per_m": q, "s_m": s, "sigma_m": sg, "closed": closed, "quadrature": direct, "diff": closed - direct})
    quad_ok = all(abs(p["diff"]) < ISL_TOL for p in quad)
    # 2. Limits: σ → 0, s ≫ σ, q → 0 give Newton; s = 0 gives erfc(qσ).
    q0 = eotwash_mode_wavenumber(120)
    limits = {
        "sigma_to_zero": plate_mode_ratio(q0, 52e-6, 1e-9, planted_defect),
        "s_much_larger_than_sigma": plate_mode_ratio(q0, 3e-3, 75e-6, planted_defect),
        "q_to_zero": plate_mode_ratio(1e-3, 52e-6, 75e-6, planted_defect),
        "s_zero": plate_mode_ratio(q0, 0.0, 75e-6, planted_defect), "erfc_q_sigma": math.erfc(q0 * 75e-6),
    }
    limits_ok = (abs(limits["sigma_to_zero"] - 1.0) < 1e-9 and abs(limits["s_much_larger_than_sigma"] - 1.0) < 1e-9
                 and abs(limits["q_to_zero"] - 1.0) < 1e-6 and abs(limits["s_zero"] - limits["erfc_q_sigma"]) < 1e-12)
    # 3. R falls with q at every separation (so the outer-edge wavenumber bounds each harmonic's deficit from below).
    q_grid = [10.0, 100.0, 300.0, 692.3, 1000.0, 2000.0, 4615.4, 8000.0, 20000.0, 50000.0]
    monotone_ok = True
    for s in (52e-6, 72e-6, 100e-6, 300e-6, 1e-3, 3e-3):
        vals = [plate_mode_ratio(q, s, 75e-6, planted_defect) for q in q_grid]
        monotone_ok = monotone_ok and all(vals[i] >= vals[i + 1] - 1e-12 for i in range(len(vals) - 1))
        monotone_ok = monotone_ok and all(-1e-12 <= v <= 1.0 + 1e-12 for v in vals)
    # 4. Eöt-Wash: deficits by σ and by separation, the Yukawa edge, the matching σ, the best-fit Yukawa.
    by_sigma = {f"{sg * 1e6:.0f}um": {f"{n}fold": eotwash_deficit(sg, n, planted_defect=planted_defect) for n in EW_N_FOLDS} for sg in ISL_SIGMAS_M}
    by_sep = {f"{s * 1e6:.0f}um": eotwash_deficit(75e-6, 120, s, planted_defect) for s in (52e-6, 72e-6, 100e-6, 150e-6, 200e-6, 300e-6, 500e-6, 1e-3)}
    edge = {f"{n}fold": eotwash_yukawa_edge_deficit(n) for n in EW_N_FOLDS}
    edge_plus = {f"{n}fold": -eotwash_yukawa_edge_deficit(n, alpha=1.0) for n in EW_N_FOLDS}
    sigma_match = sigma_matching_yukawa_edge(120)
    fit75 = best_yukawa_fit(75e-6)
    q_tail_120 = (120 - 2 * 120 ** (1.0 / 3.0)) / EW_R_OUT_M
    deficit_tail_75 = 1.0 - thick_plate_ratio(q_tail_120, EW_S_MIN_M, 75e-6, planted_defect=planted_defect)
    sigma_c_fig3 = tn_critical_sigma(TN_M_KG, TN_L_M, TN_D_M)
    deficit_at_sigma_c_fig3 = eotwash_deficit(sigma_c_fig3, 120, planted_defect=planted_defect)
    ratio_75_to_edge = by_sigma["75um"]["120fold"] / edge["120fold"]
    ew_ok = (by_sigma["75um"]["120fold"] > edge["120fold"] and by_sigma["30um"]["120fold"] < edge["120fold"]
             and 20e-6 < sigma_match < 75e-6 and by_sep["300um"] < 1e-3 and fit75["lambda_m"] > EW_YUKAWA_EDGE_LAMBDA_M and fit75["alpha"] < -1.0
             and sigma_c_fig3 > sigma_match and 0.08 < deficit_tail_75 < by_sigma["75um"]["120fold"])
    # 5. The planted defect is caught by the double entry (closed form against quadrature) and by the limits.
    bad = plate_mode_ratio(1e-3, 52e-6, 75e-6, planted_defect=True)
    defect_rejected = abs(bad - 1.0) > 0.1 and abs(plate_mode_ratio(*probes[0], planted_defect=True) - plate_mode_ratio_quadrature(*probes[0], n=20000)) > 1e-3
    return {
        "quadrature_probes": quad, "quad_ok": quad_ok, "limits": limits, "limits_ok": limits_ok, "monotone_ok": monotone_ok,
        "eotwash": {"r_out_m": EW_R_OUT_M, "t_detector_m": EW_T_DETECTOR_M, "t_attractor_m": EW_T_ATTRACTOR_M, "s_min_m": EW_S_MIN_M, "s_max_m": EW_S_MAX_M,
                    "q_per_m": {f"{n}fold": eotwash_mode_wavenumber(n) for n in EW_N_FOLDS},
                    "deficit_at_s_min_by_sigma": by_sigma, "deficit_120fold_sigma_75um_by_separation": by_sep,
                    "yukawa_edge_deficit_alpha_minus_1_lambda_38p6um": edge, "yukawa_edge_excess_alpha_plus_1": edge_plus,
                    "sigma_matching_edge_120fold_m": sigma_match, "best_yukawa_for_sigma_75um_120fold": fit75,
                    "ratio_sigma_75um_to_edge_120fold": ratio_75_to_edge,
                    "q_tail_120fold_per_m": q_tail_120, "deficit_120fold_sigma_75um_at_tail_wavenumber": deficit_tail_75,
                    "sigma_c_letter_geometry_m": sigma_c_fig3, "deficit_120fold_at_sigma_c_letter_geometry": deficit_at_sigma_c_fig3},
        "hust_lambda_m": HUST_LAMBDA_M, "hust_pair_level": hust_pair_level(), "ew_ok": ew_ok, "defect_rejected": defect_rejected,
        "ok": quad_ok and limits_ok and monotone_ok and ew_ok and defect_rejected,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(check_isl(), indent=2, default=str))
