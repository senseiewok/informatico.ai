# -*- coding: utf-8 -*-
"""Cross-Scale Essay ES.12 · Cycle Affinity, Time-Reversal Asymmetry & Irreversible Gates.

Pure-Python stdlib stochastic-thermodynamics kernel, multivariate Fraction verifier,
Lean 4 Prelude audit harness, and bilingual (EN / es-MX) monograph data for Informatico.ai's
Cross-Scale Essay ES.12 (/essays/cycle-affinity-tur-gates/).

Synthesizes four coupled analytical and formal-verification results:
  1. Iso-P_o Gauge Equivalence on a 3-State Cyclic Channel (C1 <-> C2 <-> O <-> C1):
     Adding a divergence-free forward cycle flux +J >= 0 to all three bond currents while
     holding reverse fluxes fixed at heterogeneous conductances w0 = (2.0, 1.5, 1.0) s^-1
     keeps stationary occupancy pi = (0.35, 0.25, 0.40) and scalar open probability P_o = 0.40
     identically invariant across equilibrium (J = 0, A = 0) and driven regimes (J > 0, A > 0),
     checked in exact fractions.Fraction arithmetic and numerical nullspace residuals (< 1e-14).
  2. Heterogeneous 3-State Cycle Variance & Dimensionless Barato-Seifert TUR:
     Dual independent solvers (characteristic-polynomial implicit differentiation of the tilted
     generator W(chi) and finite-difference dominant eigenvalue check) compute current diffusivity
     D_J = lambda''(0) / 2 and verify Q_TUR = (sigma / k_B) * (2 D_J) / J^2 >= 2 across every
     J > 0 (e.g. J = 4.0 s^-1 -> A = 4.0073 k_B T, sigma/k_B = 16.0293 s^-1, Q_TUR = 2.3203 >= 2;
     hydrolysis-scale w0 = (0.02, 0.015, 0.01) s^-1 at J = 10.0 s^-1 -> A = 19.6291 k_B T).
  3. 4-State Open-Subspace Complete-Monotonicity Breaking (C1 <-> C2 <-> O1 <-> O2 <-> C1):
     At detailed balance (A = 0) under equilibrium-flux entry p_eq proportional to (pi_O1 e1, pi_O2 e2),
     the open-burst exit-time PDF f_eq(t) has non-positive initial slope
     f'_eq(0) = -(pi_O1 e1^3 + pi_O2 e2^3 + pi_O1 k12 (e1 - e2)^2) / (pi_O1 e1 + pi_O2 e2) <= 0
     (-42.3333 s^-2 at e1=1, e2=5, k12=k21=8, pi_O1=pi_O2=0.2) and remains completely monotone
     (t_peak = 0). Under hydrolysis-driven entry into O1 (p_drv = (1, 0)), the initial slope flips
     to f'_drv(0) = k12 e2 - e1(e1 + k12) = +31.0 s^-2 > 0, creating a peak f_peak = 2.0166 s^-1
     at t_peak = 0.094 s (94 ms), whereas a single-open-state ring remains monotone (-e^2 <= 0).
  4. Non-vacuous 10-theorem Core Lean 4 Prelude companion (CycleAffinityGates.lean) plus
     exact multivariate Fraction polynomial checks and a falsifiable cross-scale table spanning
     hydraulic check-valves, chemical cycles, non-hydrolytic gates, and ATP-gated CFTR (PDB 6MSM).
"""
from __future__ import annotations

from decimal import Decimal, InvalidOperation
from fractions import Fraction
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time

CODE = "ES.12"
SLUG = "cycle-affinity-tur-gates"
PLATE_SLUG = "essay12"

_SUB_SUP_DIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻₀₁₂₃₄₅₆₇₈₉", "0123456789-0123456789")
_NUM_RE = re.compile(r"(?<![A-Za-z])[-−]?\d+(?:,\d{3})*(?:\.\d+)?(?:[eE][-−+]?\d+)?")

_LEAN_SECONDS = [0.0]


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


# ---------------------------------------------------------------------------
# 1. Exact 3-State Iso-P_o Gauge & Heterogeneous Cycle TUR Kernel
# ---------------------------------------------------------------------------

def evaluate_three_state_iso_po_ring(
    pi: tuple[float, float, float] = (0.35, 0.25, 0.40),
    w0: tuple[float, float, float] = (2.0, 1.5, 1.0),
    flux_j: float = 4.0,
    planted_defect: bool = False,
) -> dict[str, float]:
    """Evaluate the 3-state iso-P_o Markov cycle family and cross-check D_J with tilted eigenvalues."""
    if planted_defect:
        pi = (0.45, 0.30, 0.25)
    p1, p2, p3 = pi
    if abs((p1 + p2 + p3) - 1.0) > 1.0e-12 or min(pi) <= 0.0:
        raise ValueError(f"Stationary distribution must be positive and sum to 1, got {pi}")
    if min(w0) <= 0.0:
        raise ValueError(f"Base conductances must be positive, got {w0}")
    if flux_j < 0.0:
        raise ValueError(f"Forward cycle flux J must be non-negative, got {flux_j}")

    f12p, f12m = w0[0] + flux_j, w0[0]
    f23p, f23m = w0[1] + flux_j, w0[1]
    f31p, f31m = w0[2] + flux_j, w0[2]

    k12, k21 = f12p / p1, f12m / p2
    k23, k32 = f23p / p2, f23m / p3
    k31, k13 = f31p / p3, f31m / p1

    # Exact Fraction check for Kirchhoff node balance and P_o invariance
    f_pi = tuple(Fraction(str(x)) for x in pi)
    f_w0 = tuple(Fraction(str(x)) for x in w0)
    f_j = Fraction(str(flux_j))
    k_frac = (
        (f_w0[0] + f_j) / f_pi[0], f_w0[0] / f_pi[1],
        (f_w0[1] + f_j) / f_pi[1], f_w0[1] / f_pi[2],
        (f_w0[2] + f_j) / f_pi[2], f_w0[2] / f_pi[0],
    )
    kcl_node1 = (f_pi[2] * k_frac[4] - f_pi[0] * k_frac[5]) - (f_pi[0] * k_frac[0] - f_pi[1] * k_frac[1])
    kcl_node2 = (f_pi[0] * k_frac[0] - f_pi[1] * k_frac[1]) - (f_pi[1] * k_frac[2] - f_pi[2] * k_frac[3])
    kcl_node3 = (f_pi[1] * k_frac[2] - f_pi[2] * k_frac[3]) - (f_pi[2] * k_frac[4] - f_pi[0] * k_frac[5])
    if kcl_node1 != 0 or kcl_node2 != 0 or kcl_node3 != 0:
        raise AssertionError("Fraction Kirchhoff node balance failed")

    # Generator matrix W[i][j] = rate i -> j
    w_mat = [
        [-(k12 + k13), k12, k13],
        [k21, -(k21 + k23), k23],
        [k31, k32, -(k31 + k32)],
    ]
    max_wt_pi_res = max(abs(sum(w_mat[i][j] * pi[i] for i in range(3))) for j in range(3))

    c2 = -(w_mat[0][0] + w_mat[1][1] + w_mat[2][2])
    c1 = (
        (-w_mat[0][0]) * (-w_mat[1][1]) - w_mat[0][1] * w_mat[1][0]
        + (-w_mat[0][0]) * (-w_mat[2][2]) - w_mat[0][2] * w_mat[2][0]
        + (-w_mat[1][1]) * (-w_mat[2][2]) - w_mat[1][2] * w_mat[2][1]
    )
    p_plus = k12 * k23 * k31
    p_minus = k13 * k32 * k21

    lam1 = (p_plus - p_minus) / c1
    lam2_poly = ((p_plus + p_minus) - 2.0 * c2 * (lam1 * lam1)) / c1
    d_j_poly = 0.5 * lam2_poly

    # Independent Solver 2: direct Newton root of tilted characteristic polynomial det(lam I - W(chi)) = 0
    def dominant_tilted_eigenvalue(chi: float) -> float:
        c0 = -(p_plus * (math.exp(chi) - 1.0) + p_minus * (math.exp(-chi) - 1.0))
        lam = 0.0
        for _ in range(16):
            val = lam * lam * lam + c2 * lam * lam + c1 * lam + c0
            deriv = 3.0 * lam * lam + 2.0 * c2 * lam + c1
            lam -= val / deriv
        return lam

    h = 1.0e-4
    lp = dominant_tilted_eigenvalue(h)
    l0 = dominant_tilted_eigenvalue(0.0)
    lm = dominant_tilted_eigenvalue(-h)
    lam1_fd = (lp - lm) / (2.0 * h)
    lam2_fd = (lp - 2.0 * l0 + lm) / (h * h)
    solver_diff = abs(lam2_poly - lam2_fd)

    flux_ratio = (f12p * f23p * f31p) / (f12m * f23m * f31m)
    affinity_kb = math.log(flux_ratio) if flux_j > 0.0 else 0.0
    sigma_kb_per_s = lam1 * affinity_kb
    # Quadratic linear-response TUR saturates at Q_TUR -> 2 in the J -> 0+ limit
    q_tur = (sigma_kb_per_s * lam2_poly) / (lam1 * lam1) if flux_j > 0.0 else 2.0

    return {
        "p_open": p3,
        "flux_j": lam1,
        "flux_j_fd": lam1_fd,
        "max_stationarity_residual": max_wt_pi_res,
        "affinity_kb": affinity_kb,
        "flux_ratio": flux_ratio,
        "sigma_kb_per_s": sigma_kb_per_s,
        "lam2_poly": lam2_poly,
        "lam2_fd": lam2_fd,
        "d_j": d_j_poly,
        "solver_diff": solver_diff,
        "q_tur": q_tur,
    }


# ---------------------------------------------------------------------------
# 2. 4-State Open-Subspace Dwell-Time Monotonicity Kernel
# ---------------------------------------------------------------------------

def open_subspace_exit_pdf(
    e1: float,
    e2: float,
    k12: float,
    k21: float,
    p1: float,
    p2: float,
    t: float,
) -> float:
    """Exact 2x2 matrix-exponential exit-time PDF f(t) = p(t) . [e1, e2] for {O1, O2}."""
    a, b = -(e1 + k12), k12
    c, d = k21, -(e2 + k21)
    tr = a + d
    disc = math.sqrt(max(0.0, (a - d) * (a - d) + 4.0 * b * c))
    l1 = 0.5 * (tr + disc)
    l2 = 0.5 * (tr - disc)
    e_l1 = math.exp(l1 * t)
    e_l2 = math.exp(l2 * t)
    if abs(l1 - l2) > 1.0e-12:
        m00 = ((a - l2) * e_l1 - (a - l1) * e_l2) / (l1 - l2)
        m01 = (b * e_l1 - b * e_l2) / (l1 - l2)
        m10 = (c * e_l1 - c * e_l2) / (l1 - l2)
        m11 = ((d - l2) * e_l1 - (d - l1) * e_l2) / (l1 - l2)
    else:
        m00 = (1.0 + (a - l1) * t) * e_l1
        m01 = b * t * e_l1
        m10 = c * t * e_l1
        m11 = (1.0 + (d - l1) * t) * e_l1
    po1 = p1 * m00 + p2 * m10
    po2 = p1 * m01 + p2 * m11
    return po1 * e1 + po2 * e2


def evaluate_four_state_open_burst(
    e1: float = 1.0,
    e2: float = 5.0,
    k12: float = 8.0,
    k21: float = 8.0,
    pi_o1: float = 0.20,
    pi_o2: float = 0.20,
    planted_defect: bool = False,
) -> dict[str, object]:
    """Compare equilibrium-flux entry vs hydrolysis-driven entry on {O1, O2}."""
    if min(e1, e2, k12, k21, pi_o1, pi_o2) <= 0.0:
        raise ValueError("All open-subspace rates and occupancies must be positive")
    if abs(pi_o1 * k12 - pi_o2 * k21) > 1.0e-12:
        raise ValueError(
            f"4-state open subspace violates detailed balance: pi_O1*k12={pi_o1 * k12} != pi_O2*k21={pi_o2 * k21}"
        )
    # Equilibrium detailed-balance entry weights p_eq proportional to (pi_O1*e1, pi_O2*e2)
    z_eq = pi_o1 * e1 + pi_o2 * e2
    p1_eq = (pi_o1 * e1) / z_eq
    p2_eq = (pi_o2 * e2) / z_eq

    # Hydrolysis-driven pure O1 entry (p_drv = (1, 0))
    p1_drv, p2_drv = (p1_eq, p2_eq) if planted_defect else (1.0, 0.0)

    slope0_eq = p1_eq * (k12 * e2 - e1 * (e1 + k12)) + p2_eq * (k21 * e1 - e2 * (e2 + k21))
    slope0_drv = p1_drv * (k12 * e2 - e1 * (e1 + k12)) + p2_drv * (k21 * e1 - e2 * (e2 + k21))

    # Closed-form check for equilibrium slope: -(pi_O1 e1^3 + pi_O2 e2^3 + pi_O1 k12 (e1 - e2)^2) / z_eq
    slope0_eq_closed = -(pi_o1 * (e1 ** 3) + pi_o2 * (e2 ** 3) + pi_o1 * k12 * ((e1 - e2) ** 2)) / z_eq

    # Sample at 1 ms grid on [0, 1.0] s for interior peak, and integrate [0, 15.0] s for normalization
    ts = [i * 0.001 for i in range(1001)]
    eq_vals = [open_subspace_exit_pdf(e1, e2, k12, k21, p1_eq, p2_eq, t) for t in ts]
    drv_vals = [open_subspace_exit_pdf(e1, e2, k12, k21, p1_drv, p2_drv, t) for t in ts]

    eq_monotone = all(eq_vals[i + 1] <= eq_vals[i] + 1.0e-12 for i in range(len(eq_vals) - 1))
    t_peak_drv, f_peak_drv = max(zip(ts, drv_vals), key=lambda pair: pair[1])
    ts_long = [i * 0.005 for i in range(3001)]
    eq_long = [open_subspace_exit_pdf(e1, e2, k12, k21, p1_eq, p2_eq, t) for t in ts_long]
    drv_long = [open_subspace_exit_pdf(e1, e2, k12, k21, p1_drv, p2_drv, t) for t in ts_long]
    integral_eq = sum(0.5 * (eq_long[i] + eq_long[i + 1]) * 0.005 for i in range(len(ts_long) - 1))
    integral_drv = sum(0.5 * (drv_long[i] + drv_long[i + 1]) * 0.005 for i in range(len(ts_long) - 1))

    return {
        "p_open_total": pi_o1 + pi_o2,
        "p_eq": (p1_eq, p2_eq),
        "f0_eq": eq_vals[0],
        "f0_drv": drv_vals[0],
        "slope0_eq": slope0_eq,
        "slope0_eq_closed": slope0_eq_closed,
        "slope0_eq_err": abs(slope0_eq - slope0_eq_closed),
        "slope0_drv": slope0_drv,
        "eq_monotone": eq_monotone,
        "t_peak_drv_s": t_peak_drv,
        "f_peak_drv": f_peak_drv,
        "integral_eq": integral_eq,
        "integral_drv": integral_drv,
    }


# ---------------------------------------------------------------------------
# 3. Lean 4 Prelude Verification & Polynomial Checks
# ---------------------------------------------------------------------------

def _lean_path() -> Path:
    return Path(__file__).resolve().parents[3] / "skills" / "essays" / SLUG / "CycleAffinityGates.lean"


def _strip_lean_comments(src: str) -> str:
    no_block = re.sub(r"/-.*?-/", "", src, flags=re.S)
    return re.sub(r"--.*?$", "", no_block, flags=re.M)


def verify_lean4_companion(planted_defect: bool = False) -> dict[str, object]:
    lean_file = _lean_path()
    src = lean_file.read_text(encoding="utf-8")
    code = _strip_lean_comments(src)

    # Check exact polynomial identity for Cauchy-Schwarz Lagrange defect over Fractions
    test_pts = (
        (Fraction(2), Fraction(3), Fraction(5), Fraction(1), Fraction(4), Fraction(-2), Fraction(3), Fraction(-1), Fraction(2)),
        (Fraction(1, 2), Fraction(3, 4), Fraction(1, 3), Fraction(7), Fraction(2), Fraction(5), Fraction(-3), Fraction(4), Fraction(1)),
    )
    cs_res_zero = True
    for w1, w2, w3, a1, a2, a3, b1, b2, b3 in test_pts:
        s_aa = w1 * a1 * a1 + w2 * a2 * a2 + w3 * a3 * a3
        s_bb = w1 * b1 * b1 + w2 * b2 * b2 + w3 * b3 * b3
        s_ab = w1 * a1 * b1 + w2 * a2 * b2 + w3 * a3 * b3
        rhs = (
            w1 * w2 * ((a1 * b2 - a2 * b1) ** 2)
            + w1 * w3 * ((a1 * b3 - a3 * b1) ** 2)
            + w2 * w3 * ((a2 * b3 - a3 * b2) ** 2)
        )
        if s_aa * s_bb - s_ab * s_ab != rhs:
            cs_res_zero = False

    if planted_defect:
        code = code + "\ntheorem planted_bad : (1 : Int) = 1 := by sorry\n"

    forbidden = re.findall(r"\b(sorry|sorryAx|admit|axiom)\b", code)
    imports = re.findall(r"^\s*import\b", code, flags=re.M)
    theorems = re.findall(r"\btheorem\s+(\w+)", code)

    lean_exe = shutil.which("lean")
    compiled = False
    lean_elapsed = 0.0
    if lean_exe:
        t0 = time.perf_counter()
        with tempfile.TemporaryDirectory() as td:
            tmp_lean = Path(td) / "CycleAffinityGates.lean"
            tmp_lean.write_text(src if not planted_defect else code, encoding="utf-8")
            res = subprocess.run(
                [lean_exe, "-DwarningAsError=true", str(tmp_lean)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=30,
            )
            compiled = res.returncode == 0
        lean_elapsed = time.perf_counter() - t0
        _LEAN_SECONDS[0] += lean_elapsed

    return {
        "lean_file": str(lean_file.name),
        "imports": len(imports),
        "forbidden_tokens": forbidden,
        "theorem_names": theorems,
        "theorem_count": len(theorems),
        "cauchy_schwarz_fraction_identity": cs_res_zero,
        "lean_available": bool(lean_exe),
        "compiled": compiled,
        "lean_seconds": lean_elapsed,
    }


def evaluate_cycle_affinity_gates(planted_defect: bool = False) -> dict[str, object]:
    """Run the full ES.12 deterministic synthesis."""
    # Equilibrium vs driven 3-state ring at heterogeneous w0 = (2.0, 1.5, 1.0) s^-1
    r_eq = evaluate_three_state_iso_po_ring(flux_j=0.0, planted_defect=planted_defect)
    r_lim = evaluate_three_state_iso_po_ring(flux_j=1.0e-4)
    r_mid = evaluate_three_state_iso_po_ring(flux_j=0.5)
    r_drv = evaluate_three_state_iso_po_ring(flux_j=4.0)
    # ATP-hydrolysis scale (~20 k_B T): w0 = (0.02, 0.015, 0.01) s^-1 at J = 10.0 s^-1
    r_atp = evaluate_three_state_iso_po_ring(w0=(0.02, 0.015, 0.01), flux_j=10.0)

    burst = evaluate_four_state_open_burst(planted_defect=planted_defect)
    burst_sub = evaluate_four_state_open_burst(e1=4.0, e2=3.0, k12=2.0, k21=2.0, planted_defect=planted_defect)
    lean_info = verify_lean4_companion(planted_defect=planted_defect)

    return {
        "ring_eq": r_eq,
        "ring_lim": r_lim,
        "ring_mid": r_mid,
        "ring_drv": r_drv,
        "ring_atp": r_atp,
        "burst_4state": burst,
        "burst_subthreshold": burst_sub,
        "lean": lean_info,
    }


# ---------------------------------------------------------------------------
# 4. Bilingual ES.12 Monograph Data (EN / es-MX)
# ---------------------------------------------------------------------------

ESSAY: dict = {
    "code": CODE,
    "slug": SLUG,
    "skill_dir": SLUG,
    "verifier": "verify_essay_cycle_affinity.py",
    "plate_slug": PLATE_SLUG,
    "plate": PLATE_SLUG,
    "date": "2026-11-21",
    "published": "2026-11-21",
    "seo": (
        "Cycle Affinity and Irreversible Gates",
        "Closed-form Markov cycle models show why scalar open probability hides ATP-driven gating while flux asymmetry and burst peaks separate equilibrium.",
        "Afinidad Cíclica y Compuertas Irreversibles",
        "Modelos markovianos muestran por qué la probabilidad abierta oculta el gasto de ATP mientras la asimetría de flujo y los picos separan el equilibrio.",
    ),
    "kicker_en": "Cross-Scale Essay · ES.12 · Movement IV Coda · Cycle Affinity, TUR & Irreversible Gating",
    "kicker_es": "Ensayo entre Escalas · ES.12 · Coda del Movimiento IV · Afinidad Cíclica, TUR y Compuertas",
    "reading_time_en": "15 min read",
    "reading_time_es": "15 min de lectura",
    "title_en": "Cycle Affinity, Time-Reversal Asymmetry, and the Irreversible Gate: From Hydraulic Check-Valves to ATP-Driven Channels",
    "title_es": "Afinidad Cíclica, Asimetría Temporal y Compuertas Irreversibles: De Válvulas Hidráulicas a Canales por ATP",
    "standfirst_en": (
        "When an engineered check-valve or a nanoscale protein pore spends half its time open, can a steady occupancy number "
        "by itself tell whether energy is being burned to hold the rhythm? Closed-form 3-state and 4-state Markov cycle models "
        "show how an entire family of driven cycles shares the identical open probability P_o = 0.40 while breaking time-reversal "
        "symmetry, paying the Barato–Seifert thermodynamic uncertainty floor Q_TUR ≥ 2, and turning decaying open-burst distributions "
        "into peaked clocks."
    ),
    "standfirst_es": (
        "Cuando una válvula hidráulica o un poro proteico pasa la mitad del tiempo abierto, ¿puede un promedio estacionario "
        "indicar por sí solo si el sistema consume energía para sostener su ritmo? Modelos markovianos de 3 y 4 estados "
        "muestran cómo toda una familia de ciclos impulsados comparte la misma probabilidad abierta P_o = 0.40 mientras rompe "
        "la simetría temporal, paga el piso de incertidumbre termodinámica Q_TUR ≥ 2 y transforma ráfagas decrecientes en pulsos con pico."
    ),
    "card_dek_en": (
        "Iso-P_o gauge equivalence (P_o = 0.40), heterogeneous Barato–Seifert TUR (Q_TUR ≥ 2), 4-state burst peaks (t = 94 ms), and 10 Lean 4 theorems."
    ),
    "card_dek_es": (
        "Equivalencia de calibre iso-P_o (P_o = 0.40), TUR heterogénea (Q_TUR ≥ 2), picos de ráfaga en 4 estados (t = 94 ms) y 10 teoremas en Lean 4."
    ),
    "instrument_kind": "cycle_affinity",
    "instrument": {"kind": "cycle_affinity"},
    "predict": {
        "question_en": (
            "Suppose two 3-state cyclic channels share the identical stationary open probability P_o = 0.40, one at thermal "
            "equilibrium (J = 0) and one driven by cycle flux J = 4.0 s⁻¹. Which observable distinguishes them?"
        ),
        "question_es": (
            "Suponga que dos canales cíclicos de 3 estados comparten la misma probabilidad abierta estacionaria P_o = 0.40, "
            "uno en equilibrio térmico (J = 0) y otro impulsado con flujo J = 4.0 s⁻¹. ¿Qué observable los separa?"
        ),
        "choices": [
            {
                "id": "a",
                "en": "Steady-state P_o shifts upward in proportion to cycle affinity A whenever detailed balance is broken.",
                "es": "La probabilidad estacionaria P_o sube en proporción a la afinidad cíclica A al romperse el balance detallado.",
            },
            {
                "id": "b",
                "en": "Scalar P_o can stay identically flat at 0.40 across all J ≥ 0; only directional cycle-flux asymmetry (or a rising burst peak when ≥ 2 open states couple irreversibly) detects broken detailed balance.",
                "es": "El escalar P_o puede permanecer plano en 0.40 para todo J ≥ 0; solo la asimetría direccional de flujo (o un pico creciente con ≥ 2 estados abiertos acoplados) detecta la ruptura del balance detallado.",
            },
            {
                "id": "c",
                "en": "A single open state O already produces a peaked dwell-time histogram as soon as cycle affinity A exceeds 2 k_B T.",
                "es": "Un único estado abierto O ya produce un histograma con pico en cuanto la afinidad A supera 2 k_B T.",
            },
        ],
        "answer": "b",
        "explain_en": (
            "Adding a divergence-free cycle flux +J to forward edges keeps Kirchhoff balance zero at every node, so P_o = 0.40 "
            "remains flat while cycle affinity A = 4.0073 k_B T and dissipation σ/k_B = 16.0293 s⁻¹ grow. A single open state O "
            "still has exponential dwell slope f'(0) = −e² ≤ 0; either path-reversal asymmetry (55.0× here) or ≥ 2 coupled open "
            "states (O₁ → O₂, giving f'(0) = +31.0 s⁻² and a 94 ms peak) is required to reveal driving."
        ),
        "explain_es": (
            "Sumar un flujo cíclico +J sin divergencia a las aristas directas mantiene nulo el balance de Kirchhoff en cada nodo, "
            "así que P_o = 0.40 permanece plano mientras crecen A = 4.0073 k_B T y σ/k_B = 16.0293 s⁻¹. Un solo estado abierto O "
            "conserva pendiente exponencial f'(0) = −e² ≤ 0; se requiere asimetría de trayectoria (55.0× aquí) o ≥ 2 estados abiertos "
            "acoplados (O₁ → O₂, con f'(0) = +31.0 s⁻² y pico en 94 ms) para detectar el impulso."
        ),
    },
    "sections": [
        {
            "id": "the-quiet-valve-paradox",
            "h2_en": "I · Why an Open Fraction Hides the Fuel Bill",
            "h2_es": "I · Por Qué la Fracción Abierta Oculta el Gasto de Energía",
            "short_en": "I · Open Fraction",
            "short_es": "I · Fracción Abierta",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Watch a brass swing check-valve in a quiet basement loop through a frosted sight-glass that only tells "
                        "you whether the flapper is up or down. If a pump pushes water around the loop in one direction and the "
                        "flapper sits lifted forty percent of the afternoon, the sight-glass reports one number: 0.40. Now shut the "
                        "pump off, warm the fluid slightly so thermal eddies rattle the hinge back and forth equally, and tune "
                        "the counterweight until the flapper again spends forty percent of the hour lifted. From the sight-glass "
                        "by itself, both rooms look identical—even though one loop circulates water and burns energy while the "
                        "other sits at thermal rest."
                    ),
                    "es": (
                        "Observe una válvula de columpio de latón en un circuito hidráulico a través de una mirilla esmerilada que "
                        "solo deja ver si la compuerta está arriba o abajo. Si una bomba empuja agua en un sentido y la compuerta "
                        "pasa el cuarenta por ciento de la tarde levantada, la mirilla marca un número: 0.40. Ahora apague la "
                        "bomba, entibie el fluido para que la agitación térmica mueva la bisagra en ambos sentidos y ajuste el "
                        "contrapeso hasta que vuelva a pasar el cuarenta por ciento del tiempo abierta. Desde la mirilla, ambas "
                        "salas parecen iguales, aunque en una circula flujo con gasto continuo y en la otra reina el reposo."
                    ),
                },
                {
                    "type": "bridge",
                    "kicker_en": "In Plain Words · The Sight-Glass Trap",
                    "kicker_es": "En Palabras Claras · La Trampa de la Mirilla",
                    "title_en": "Static occupancy cannot see which way a loop is turning",
                    "title_es": "La ocupación estática no distingue hacia dónde gira un ciclo",
                    "paras": [
                        (
                            "A static average such as open probability counts how often a gate sits in state O, not the order "
                            "in which states are visited. Under thermal equilibrium (Onsager, 1931), every closed loop visits "
                            "its forward and backward routes equally often. Under chemical or hydraulic driving, the gate "
                            "completes cycles in a preferred direction, leaving the same average occupancy intact.",
                            "Un promedio estático como la probabilidad abierta cuenta cuánto tiempo pasa una compuerta en el estado O, "
                            "no el orden en que visita sus estados. En equilibrio térmico (Onsager, 1931), todo lazo cerrado recorre sus "
                            "rutas hacia adelante y hacia atrás por igual. Bajo un impulso químico o hidráulico, la compuerta completa "
                            "ciclos en un sentido preferente y puede conservar exactamente la misma ocupación media.",
                        ),
                    ],
                },
                {
                    "type": "p",
                    "en": (
                        "What makes that sight-glass illusion tricky in both engineering and molecular biophysics is not instrumental "
                        "noise; it is structural degeneracy. An equilibrium Boltzmann landscape sets a fixed depth ratio between open "
                        "and closed wells, so its stationary probability vector sums equilibrium weights and forgets every cycle "
                        "arrow. A steady non-equilibrium pump can hold the exact same fraction in state O while churning around the "
                        "loop tens of times per second. Only observables sensitive to time ordering—which transition happened first, "
                        "how tightly current variance shrinks per dissipated joule, or how open dwell distributions bend near time zero—"
                        "separate those two rooms cleanly."
                    ),
                    "es": (
                        "Lo que vuelve engañosa esa ilusión de la mirilla tanto en ingeniería como en biofísica molecular no es el ruido "
                        "instrumental, sino una degeneración estructural. Un paisaje de equilibrio de Boltzmann fija una razón de "
                        "profundidades entre pozos abiertos y cerrados, así que su vector estacionario suma pesos y olvida toda "
                        "flecha cíclica. Una bomba estacionaria fuera de equilibrio puede sostener la misma fracción en O mientras "
                        "recorre el lazo decenas de veces por segundo. Solo los observables sensibles al orden temporal —qué transición "
                        "ocurrió primero, cuánto cae la varianza por julio disipado o cómo se curva la estadía cerca del origen—"
                        "separan ambas salas con claridad."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "A direct thought experiment illustrates the distinction cleanly. Film a single gate over one hundred switching "
                        "events and project the recording forward and in reverse. At thermodynamic equilibrium, the time-reversed film "
                        "is statistically indistinguishable from the forward film: every loop excursion in one orientation occurs just as "
                        "often as its mirror opposite, so net cycle flux vanishes by detailed balance. Under external driving, however, "
                        "running the film backward flips the dominant sequence of steps, turning preferred forward cycles into rare "
                        "uphill fluctuations. Yet a stationary average such as P_o discards the clock axis altogether, collapsing both "
                        "movies onto the same single summary fraction."
                    ),
                    "es": (
                        "Un experimento mental directo ilustra esta diferencia con nitidez. Filme una sola compuerta a lo largo de cien "
                        "eventos de conmutación y proyecte la grabación hacia adelante y en reversa. En equilibrio termodinámico, la "
                        "película invertida en el tiempo es estadísticamente indistinguible de la original: cada excursión en un sentido "
                        "ocurre con la misma frecuencia que su opuesta, así que el flujo cíclico neto se anula por balance detallado. "
                        "Bajo un impulso externo, en cambio, correr el video al revés invierte la secuencia dominante y convierte el ciclo "
                        "preferente en una fluctuación cuesta arriba poco común. Aun así, un promedio estacionario como P_o descarta "
                        "el eje temporal por completo y colapsa ambas películas en el mismo número."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Closing Movement IV (ES.10–ES.12), this essay turns the lens from gravity scales to the universal "
                        "thermodynamics of cyclic gates. Building on Lars Onsager's 1931 reciprocity law (DOI 10.1103/physrev.37.405), "
                        "Udo Seifert's stochastic thermodynamics (DOI 10.1088/0034-4885/75/12/126001), and the thermodynamic uncertainty "
                        "bounds of Barato and Seifert (DOI 10.1103/physrevlett.114.158101) and Gingrich et al. (DOI 10.1103/physrevlett.116.120601), "
                        "we test a sharp, falsifiable question: if scalar open probability P_o cannot separate equilibrium from "
                        "fuel-burning gating, what exact measurements can?"
                    ),
                    "es": (
                        "Al cerrar el Movimiento IV (ES.10–ES.12), este ensayo enfoca la termodinámica universal de las compuertas "
                        "cíclicas. Apoyados en la reciprocidad de Lars Onsager de 1931 (DOI 10.1103/physrev.37.405), la termodinámica "
                        "estocástica de Udo Seifert (DOI 10.1088/0034-4885/75/12/126001) y las cotas de incertidumbre termodinámica "
                        "de Barato y Seifert (DOI 10.1103/physrevlett.114.158101) y Gingrich et al. (DOI 10.1103/physrevlett.116.120601), "
                        "examinamos una pregunta falsable: si la probabilidad abierta P_o no distingue el equilibrio de una compuerta "
                        "alimentada por combustible, ¿qué mediciones sí lo hacen?"
                    ),
                },
            ],
        },
        {
            "id": "iso-po-gauge-family",
            "h2_en": "II · The Iso-P_o Gauge Family & Heterogeneous Cycle TUR",
            "h2_es": "II · La Familia de Calibre Iso-P_o y la TUR Heterogénea",
            "short_en": "II · Iso-P_o Gauge",
            "short_es": "II · Calibre Iso-P_o",
            "blocks": [
                {
                    "type": "analogy",
                    "kicker_en": "Tactile Analogy · The Three-Station Turnstile",
                    "kicker_es": "Analogía Táctil · El Torniquete de Tres Estaciones",
                    "title_en": "Adding a steady stream around a traffic circle without changing crowd counts",
                    "title_es": "Sumar una corriente circular sin alterar cuánta gente hay en cada esquina",
                    "paras": [
                        (
                            "Imagine three subway platforms linked in a triangle where as many riders enter each platform per "
                            "minute as leave it. If you add four extra clockwise riders per minute on all three tracks at once, "
                            "each platform still gains four and loses four, so the crowd standing on platform O stays frozen at "
                            "forty percent. This analogy stops at linear traffic: in real molecules, rates also obey physical "
                            "barriers and finite substrate concentrations.",
                            "Imagine tres andenes unidos en triángulo donde entran tantos pasajeros por minuto como salen. Si suma "
                            "cuatro pasajeros extra en sentido horario en los tres tramos a la vez, cada andén gana cuatro y pierde "
                            "cuatro, de modo que la multitud en el andén O permanece fija en cuarenta por ciento. La analogía se "
                            "detiene en el flujo lineal: en moléculas reales, las tasas también dependen de barreras físicas.",
                        ),
                    ],
                },
                {
                    "type": "p",
                    "en": (
                        "Formally, take a 3-state cyclic network C₁ ↔ C₂ ↔ O ↔ C₁ with target stationary occupancies "
                        "π = (0.35, 0.25, 0.40) and heterogeneous equilibrium bond conductances w₀ = (2.0, 1.5, 1.0) s⁻¹. "
                        "Adding a positive cycle flux J ≥ 0 strictly to the forward bond currents (φ⁺ = w₀ + J, φ⁻ = w₀) keeps "
                        "all transition rates k_ij = φ_ij⁺ / π_i and k_ji = φ_ij⁻ / π_j strictly positive and preserves Kirchhoff "
                        "node balance identically at every vertex. Consequently, P_o = π₃ = 0.40 stays unchanged for all J ≥ 0."
                    ),
                    "es": (
                        "Formalmente, tome una red cíclica de 3 estados C₁ ↔ C₂ ↔ O ↔ C₁ con ocupaciones estacionarias objetivo "
                        "π = (0.35, 0.25, 0.40) y conductancias de equilibrio heterogéneas w₀ = (2.0, 1.5, 1.0) s⁻¹. Sumar un flujo "
                        "positivo J ≥ 0 únicamente a las corrientes directas (φ⁺ = w₀ + J, φ⁻ = w₀) conserva todas las tasas "
                        "k_ij = φ_ij⁺ / π_i y k_ji = φ_ij⁻ / π_j estrictamente positivas y mantiene idéntico el balance de Kirchhoff "
                        "en cada nodo. Así, P_o = π₃ = 0.40 permanece inalterado para todo J ≥ 0."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Iso-P_o Cycle Affinity & Heterogeneous 3-State TUR",
                    "label_es": "Afinidad Cíclica Iso-P_o y TUR Heterogénea de 3 Estados",
                    "formula": "A(J) = ln[(w12+J)(w23+J)(w31+J) / (w12 w23 w31)],   sigma/k_B = J A,   Q_TUR = (sigma/k_B) * [(P_+ + P_-) - 2 c_2 J^2] / (c_1 J^2) >= 2",
                    "note_en": (
                        "Unlike ES.03's homogeneous ring formula, a heterogeneous 3-state cycle requires the full tilted-generator "
                        "second cumulant λ''(0) = [(P_+ + P_-) − 2 c₂ J²] / c₁, where P_+ = k₁₂k₂₃k₃₁ and P_- = k₁₃k₃₂k₂₁."
                    ),
                    "note_es": (
                        "A diferencia del anillo homogéneo de ES.03, un ciclo heterogéneo de 3 estados requiere el segundo cumulante "
                        "completo del generador inclinado λ''(0) = [(P_+ + P_-) − 2 c₂ J²] / c₁, con P_+ = k₁₂k₂₃k₃₁ y P_- = k₁₃k₃₂k₂₁."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "At J = 4.0 s⁻¹, the forward-to-backward path ratio reaches Φ⁺/Φ⁻ = 55.0 (cycle affinity A = 4.0073 k_B T, "
                        "entropy production σ/k_B = 16.0293 s⁻¹). Closed-form implicit differentiation of det(λI − W(χ)) = 0 yields "
                        "λ''(0) = 2.3160 s⁻¹ (current diffusivity D_J = 1.1580 s⁻¹), giving Q_TUR = 2.3203 ≥ 2—matching direct "
                        "finite-difference tilted eigenvalues to 1.8 × 10⁻⁸. Scaling the base conductances down to "
                        "w₀ = (0.02, 0.015, 0.01) s⁻¹ at J = 10.0 s⁻¹ reaches physiological ATP-hydrolysis affinity "
                        "A = 19.6291 k_B T (σ/k_B = 196.2915 s⁻¹, Q_TUR = 6.7903 ≥ 2), while P_o remains identically 0.40."
                    ),
                    "es": (
                        "En J = 4.0 s⁻¹, la razón de trayectorias directas frente a inversas alcanza Φ⁺/Φ⁻ = 55.0 (afinidad cíclica "
                        "A = 4.0073 k_B T, producción de entropía σ/k_B = 16.0293 s⁻¹). La diferenciación implícita de "
                        "det(λI − W(χ)) = 0 entrega λ''(0) = 2.3160 s⁻¹ (difusividad D_J = 1.1580 s⁻¹) y Q_TUR = 2.3203 ≥ 2, en "
                        "acuerdo con eigenvalores inclinados directos hasta 1.8 × 10⁻⁸. Al escalar las conductancias base a "
                        "w₀ = (0.02, 0.015, 0.01) s⁻¹ en J = 10.0 s⁻¹ se alcanza la afinidad fisiológica del ATP A = 19.6291 k_B T "
                        "(σ/k_B = 196.2915 s⁻¹, Q_TUR = 6.7903 ≥ 2), manteniendo P_o idéntico en 0.40."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Just as strikingly, the J → 0⁺ limit shows why homogeneous rings understate the dissipation floor "
                        "away from equilibrium. Near detailed balance, linear response saturates Q_TUR → 2.0000 because the current "
                        "variance and the affinity scale linearly together at leading order in J. Even at a tiny non-zero drive "
                        "J = 10⁻⁴ s⁻¹, the exact polynomial cumulant sits at Q_TUR = 2.000000001. Once asymmetry grows, "
                        "heterogeneity across w₀ = (2.0, 1.5, 1.0) s⁻¹ lifts Q_TUR above 2 to 2.3203, reflecting bottlenecked dwell "
                        "variance along the slowest step. A mild J = 0.5 s⁻¹ midpoint already gives Φ⁺/Φ⁻ = 2.50, affinity "
                        "A = 0.9163 k_B T, and Q_TUR = 2.0186 while leaving P_o = 0.4000 flat to machine precision (< 10⁻¹³ residual)."
                    ),
                    "es": (
                        "Igualmente revelador es el límite J → 0⁺, donde los anillos homogéneos subestiman el piso de disipación "
                        "lejos del equilibrio. Cerca del balance detallado, la respuesta lineal satura Q_TUR → 2.0000 porque la "
                        "varianza de corriente y la afinidad escalan juntas a orden dominante en J. Incluso con un impulso diminuto "
                        "de J = 10⁻⁴ s⁻¹, el cumulante polinomial arroja Q_TUR = 2.000000001. Al crecer la asimetría, la "
                        "heterogeneidad en w₀ = (2.0, 1.5, 1.0) s⁻¹ eleva Q_TUR sobre 2 hasta 2.3203 debido al cuello de botella "
                        "en la tasa lenta. Un punto intermedio de J = 0.5 s⁻¹ ya alcanza Φ⁺/Φ⁻ = 2.50, afinidad A = 0.9163 k_B T "
                        "y Q_TUR = 2.0186 manteniendo P_o = 0.4000 plano hasta precisión de máquina (residuo < 10⁻¹³)."
                    ),
                },
            ],
        },
        {
            "id": "complete-monotonicity-breaking",
            "h2_en": "III · Why Equilibrium Open Bursts Cannot Peak (and Driven Dual-Open Cycles Can)",
            "h2_es": "III · Por Qué las Ráfagas en Equilibrio No Tienen Pico (y los Ciclos Impulsados Sí)",
            "short_en": "III · Burst Peaks",
            "short_es": "III · Picos de Ráfaga",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "What if an experiment records only open versus closed dwell times without resolving two closed sub-states? "
                        "In a 3-state cycle with a single open state O (exit rate e), the open dwell density is exponential with "
                        "initial slope f'(0) = −e² ≤ 0 even when A = 20 k_B T. Open-time distribution shape cannot detect driving in "
                        "a 1-open-state graph; only directional transitions between closed states can."
                    ),
                    "es": (
                        "¿Qué sucede si un experimento registra solo tiempos abiertos frente a cerrados sin distinguir dos subestados "
                        "cerrados? En un ciclo de 3 estados con un único estado abierto O (tasa de salida e), la densidad abierta es "
                        "exponencial con pendiente inicial f'(0) = −e² ≤ 0 incluso con A = 20 k_B T. La forma del tiempo abierto no "
                        "detecta el impulso en un grafo con 1 estado abierto; solo las transiciones direccionales pueden hacerlo."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Split O into two coupled open configurations O₁ ↔ O₂ inside a 4-state cycle C₁ ↔ C₂ ↔ O₁ ↔ O₂ ↔ C₁, with "
                        "exit rates e₁ = 1.0 s⁻¹ (from O₁) and e₂ = 5.0 s⁻¹ (from O₂), and internal rates k₁₂ = k₂₁ = 8.0 s⁻¹ "
                        "(π_O1 = π_O2 = 0.20, P_o = 0.40). Under detailed balance (A = 0), stationary entry enters O₁ and O₂ in "
                        "proportion to equilibrium exit flux p_eq = (π_O1 e₁, π_O2 e₂) / (π_O1 e₁ + π_O2 e₂) = (1/6, 5/6). "
                        "Algebraic cancellation forces f'_eq(0) = −(π_O1 e₁³ + π_O2 e₂³ + π_O1 k₁₂(e₁ − e₂)²) / (π_O1 e₁ + π_O2 e₂) = "
                        "−42.3333 s⁻² ≤ 0, so f_eq(t) decays monotonically from f_eq(0) = 4.3333 s⁻¹ with t_peak = 0.000 s."
                    ),
                    "es": (
                        "Divida O en dos configuraciones abiertas acopladas O₁ ↔ O₂ dentro de un ciclo de 4 estados "
                        "C₁ ↔ C₂ ↔ O₁ ↔ O₂ ↔ C₁, con tasas de salida e₁ = 1.0 s⁻¹ (desde O₁) y e₂ = 5.0 s⁻¹ (desde O₂) y tasas "
                        "internas k₁₂ = k₂₁ = 8.0 s⁻¹ (π_O1 = π_O2 = 0.20, P_o = 0.40). Bajo balance detallado (A = 0), la entrada "
                        "estacionaria sigue el flujo de equilibrio p_eq = (π_O1 e₁, π_O2 e₂) / (π_O1 e₁ + π_O2 e₂) = (1/6, 5/6). La "
                        "cancelación algebraica fija f'_eq(0) = −(π_O1 e₁³ + π_O2 e₂³ + π_O1 k₁₂(e₁ − e₂)²) / (π_O1 e₁ + π_O2 e₂) = "
                        "−42.3333 s⁻² ≤ 0, así que f_eq(t) decae monótonamente desde f_eq(0) = 4.3333 s⁻¹ con t_peak = 0.000 s."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Now break detailed balance so irreversible entry arrives via O₁ (p_drv = (1, 0)) before exiting mainly "
                        "via O₂. The initial slope flips to f'_drv(0) = k₁₂ e₂ − e₁(e₁ + k₁₂) = +31.0000 s⁻² > 0, climbing from "
                        "f_drv(0) = 1.0000 s⁻¹ to an interior maximum f_peak = 2.0166 s⁻¹ at t_peak = 0.094 s (94 ms). Notice "
                        "that A > 0 is necessary but not sufficient for a peak: if direct exit e₁ = 4.0 s⁻¹ exceeds fast "
                        "forward coupling (k₁₂ = 2.0, e₂ = 3.0 s⁻¹), then k₁₂ e₂ − e₁(e₁ + k₁₂) = −18 < 0 and the burst stays "
                        "monotone despite non-zero cycle flux."
                    ),
                    "es": (
                        "Rompa ahora el balance detallado de modo que la entrada irreversible ocurra por O₁ (p_drv = (1, 0)) antes "
                        "de salir principalmente por O₂. La pendiente inicial cambia de signo a f'_drv(0) = k₁₂ e₂ − e₁(e₁ + k₁₂) = "
                        "+31.0000 s⁻² > 0, subiendo desde f_drv(0) = 1.0000 s⁻¹ hasta un máximo interior f_peak = 2.0166 s⁻¹ en "
                        "t_peak = 0.094 s (94 ms). Note que A > 0 es necesario pero no suficiente para un pico: si la salida directa "
                        "e₁ = 4.0 s⁻¹ domina sobre el acoplamiento directo (k₁₂ = 2.0, e₂ = 3.0 s⁻¹), entonces k₁₂ e₂ − e₁(e₁ + k₁₂) = "
                        "−18 < 0 y la ráfaga sigue siendo monótona pese al flujo neto."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Why can equilibrium never produce an interior burst maximum on any finite reversible network? Because under "
                        "detailed balance, the generator inside the open subset O = {O₁, O₂} is symmetrizable by π_O¹/²: its "
                        "eigenvalues are strictly negative real numbers, and the equilibrium-entry vector weights each relaxation "
                        "mode with non-negative spectral coefficients. Every completely monotone sum of decaying exponentials drops "
                        "steepest at t = 0 and bends strictly upward forever after. Turning an open histogram into a peaked clock "
                        "requires two simultaneous conditions: at least two open states linked inside a loop, and asymmetric "
                        "driven entry strong enough to beat direct escape from O₁."
                    ),
                    "es": (
                        "¿Por qué el equilibrio jamás produce un máximo interior de ráfaga en una red reversible finita? Porque bajo "
                        "balance detallado el generador del subespacio abierto O = {O₁, O₂} es simetrizable por π_O¹/²: sus "
                        "eigenvalores son estrictamente reales negativos y el vector de entrada de equilibrio pondera cada modo de "
                        "relajación con coeficientes espectrales no negativos. Toda suma completamente monótona de exponenciales cae "
                        "con mayor pendiente en t = 0 y es convexa después. Convertir una ráfaga en un reloj con pico exige dos "
                        "condiciones a la vez: al menos dos estados abiertos en ciclo y una entrada asimétrica capaz de superar "
                        "el escape directo desde O₁."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "From an experimental standpoint, catching that rising phase places a strict requirement on temporal resolution: "
                        "if a detector bins bursts coarsely beyond roughly 94 ms, the initial upward climb gets averaged together with "
                        "the exponential tail and disappears. Conversely, resetting a simulation without preserving true equilibrium entry "
                        "—for instance starting every trajectory artificially at O₁ while asserting A = 0— creates an apparent burst "
                        "bump even on a reversible network. The interactive observatory and Python harness enforce this separation directly "
                        "so stationary entry is never conflated with irreversible catalysis."
                    ),
                    "es": (
                        "Desde el punto de vista experimental, capturar esa fase creciente impone un requisito estricto de resolución "
                        "temporal: si un detector agrupa las ráfagas en intervalos mayores que cerca de 94 ms, el ascenso inicial se "
                        "promedia con la cola exponencial y desaparece. A la inversa, reiniciar una simulación sin respetar la entrada "
                        "estacionaria —por ejemplo iniciando cada trayectoria artificialmente en O₁ aunque A = 0— genera un abultamiento "
                        "aparente incluso en una red reversible. El observatorio interactivo y el núcleo en Python vigilan esa frontera "
                        "para no confundir inicialización con catálisis irreversible."
                    ),
                },
            ],
        },
        {
            "id": "cross-scale-gates-and-cftr",
            "h2_en": "IV · Across Scales: Check-Valves, Chemical Cycles & ATP-Gated Channels",
            "h2_es": "IV · Entre Escalas: Válvulas, Ciclos Químicos y Canales por ATP",
            "short_en": "IV · Cross-Scale Gates",
            "short_es": "IV · Compuertas por Escala",
            "blocks": [
                {
                    "type": "table",
                    "caption_en": "Four Iso-P_o Architectures (P_o = 0.40) × Three Irreversibility Observables",
                    "caption_es": "Cuatro Arquitecturas Iso-P_o (P_o = 0.40) × Tres Observables de Irreversibilidad",
                    "headers_en": ["Architecture", "Scalar P_o", "Cycle Flux J (s⁻¹)", "Flux Ratio Φ⁺/Φ⁻", "Initial Burst Slope f'(0)"],
                    "headers_es": ["Arquitectura", "Escalar P_o", "Flujo Cíclico J (s⁻¹)", "Razón Φ⁺/Φ⁻", "Pendiente Inicial f'(0)"],
                    "rows": [
                        [("Equilibrium 2-state / detailed-balance hinge", "Bisagra en equilibrio (2 estados / balance detallado)"), "0.4000", "0.0000", "1.0", ("≤ 0 (monotone, t_peak = 0)", "≤ 0 (monótona, t_peak = 0)")],
                        [("Equilibrium 4-state {O₁, O₂} (A = 0, p_eq)", "Equilibrio 4 estados {O₁, O₂} (A = 0, p_eq)"), "0.4000", "0.0000", "1.0", ("−42.3333 s⁻² (t_peak = 0.000 s)", "−42.3333 s⁻² (t_peak = 0.000 s)")],
                        [("Driven 3-state 1-open ring (J = 4.0 s⁻¹)", "Anillo impulsado 3 estados, 1 abierto (J = 4.0 s⁻¹)"), "0.4000", "4.0000", "55.0", ("−e² < 0 (exponential dwell)", "−e² < 0 (estadía exponencial)")],
                        [("Driven 4-state {O₁, O₂} (p_drv = (1, 0))", "Ciclo impulsado 4 estados {O₁, O₂} (p_drv = (1, 0))"), "0.4000", "> 0", "> 1", ("+31.0000 s⁻² (peak 2.0166 s⁻¹ at 0.094 s)", "+31.0000 s⁻² (pico 2.0166 s⁻¹ en 0.094 s)")],
                    ],
                },
                {
                    "type": "bridge",
                    "kicker_en": "Physical Unification · Why Order Matters Across 10 Orders of Magnitude",
                    "kicker_es": "Unificación Física · Por Qué Importa el Orden en 10 Órdenes de Magnitud",
                    "title_en": "From millijoule check-valves to 20 k_B T ATP cycles, symmetry breaking hides in time ordering",
                    "title_es": "De válvulas de milajulios a ciclos de ATP de 20 k_B T, la ruptura de simetría vive en el orden temporal",
                    "paras": [
                        (
                            "In a macroscopic swing valve, pressure drops maintain a macroscopic one-way flux ratio well above 55× "
                            "even if the average opening stops at 0.40. In an open chemical network or a nanomachine powered near "
                            "20 k_B T, thermal noise occasionally drives backward steps, yet the same directional ratio Φ⁺/Φ⁻ = exp(A/k_B T) "
                            "measures dissipation exactly.",
                            "En una válvula hidráulica macroscópica, la caída de presión sostiene una razón unidireccional muy superior "
                            "a 55× aunque la apertura media quede en 0.40. En una red química abierta o nanomáquina impulsada cerca de "
                            "20 k_B T, el ruido térmico aún dispara pasos inversos, pero la misma razón direccional Φ⁺/Φ⁻ = exp(A/k_B T) "
                            "cuantifica la disipación con exactitud.",
                        ),
                    ],
                },
                {
                    "type": "p",
                    "en": (
                        "Across engineered and living systems, the same separation holds. In open chemical reaction networks "
                        "(Rao & Esposito, 2016, DOI 10.1103/physrevx.6.041064), Harada–Sasa fluctuation-response violations "
                        "(DOI 10.1103/physrevlett.95.130602), and finite-time speed bounds (Van Vu & Hasegawa, 2021, "
                        "DOI 10.1103/physrevlett.126.010601), steady-state populations hide cycle currents unless directional "
                        "asymmetry or phase-resolved responses are sampled. A single scalar occupancy average cannot separate a "
                        "quiescent catalyst pool resting at detailed balance from a driven catalytic turnover loop consuming substrate "
                        "free energy; only net cycle affinities summed along fundamental cords break the ambiguity."
                    ),
                    "es": (
                        "En sistemas diseñados y materia viva rige la misma separación. En redes de reacciones químicas abiertas "
                        "(Rao y Esposito, 2016, DOI 10.1103/physrevx.6.041064), violaciones de fluctuación-respuesta de Harada y Sasa "
                        "(DOI 10.1103/physrevlett.95.130602) y cotas geométricas de velocidad (Van Vu y Hasegawa, 2021, "
                        "DOI 10.1103/physrevlett.126.010601), las poblaciones estacionarias ocultan las corrientes cíclicas salvo "
                        "que se mida la asimetría direccional o la respuesta temporal. Un promedio escalar de ocupación tampoco "
                        "distingue un catalizador en equilibrio de un lazo catalítico impulsado que consume energía libre; solo las "
                        "afinidades cíclicas sumadas sobre cuerdas fundamentales resuelven esa ambigüedad."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "In molecular biophysics, human CFTR (ABCC7)—the chloride channel studied in cystic fibrosis research and "
                        "resolved in ATP-bound phosphorylated Cryo-EM coordinates (Zhang et al., 2018, "
                        "DOI 10.1073/pnas.1815287115)—exemplifies the driven regime: Csanády, Nairn, and Gadsby (2006, "
                        "DOI 10.1085/jgp.200609558) showed that ATP binding and irreversible hydrolysis drive an asymmetric gating "
                        "cycle with peaked open-burst timing, whereas suppressing hydrolysis leaves a symmetric equilibrium "
                        "pathway whose dwell histogram flattens into monotonic decay even when macroscopic open fraction overlaps. "
                        "Treating scalar occupancy as a full readout of gating energetics therefore misses the energetic signature "
                        "that coupled open states make visible in dwell-time shapes and directional transition probabilities."
                    ),
                    "es": (
                        "En biofísica molecular, el canal humano CFTR (ABCC7) —estudiado en la investigación de fibrosis quística "
                        "y resuelto en coordenadas crio-EM unido a ATP (Zhang et al., 2018, DOI 10.1073/pnas.1815287115)— ejemplifica "
                        "el régimen impulsado: Csanády, Nairn y Gadsby (2006, DOI 10.1085/jgp.200609558) mostraron que la unión e "
                        "hidrólisis irreversible de ATP impulsan un ciclo asimétrico con ráfagas con pico, mientras que suprimir "
                        "la hidrólisis deja una vía simétrica en equilibrio cuyo histograma cae de forma monótona aun con fracción "
                        "abierta similar. Tomar la ocupación escalar como lectura energética completa oculta la firma de disipación "
                        "que los estados abiertos acoplados revelan en la forma temporal y el orden de transiciones."
                    ),
                },
            ],
        },
        {
            "id": "lean4-verification-and-hypothesis",
            "h2_en": "V · Machine-Checked Lean 4 Algebra & Falsifiable Hypothesis",
            "h2_es": "V · Álgebra Verificada en Lean 4 e Hipótesis Falsable",
            "short_en": "V · Lean 4 & Falsification",
            "short_es": "V · Lean 4 y Falsación",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "To keep every algebraic identity free of floating-point illusions, CycleAffinityGates.lean formalizes "
                        "four universal mathematical claims in core Lean 4 Prelude (zero external imports, no axioms, zero sorry "
                        "placeholders): (1) SI dimensional homogeneity checks unit consistency across cycle flux [J] = T⁻¹, "
                        "entropy production [σ/k_B] = T⁻¹, diffusivity [D_J] = T⁻¹, dimensionless TUR ratio [Q_TUR] = 1, and "
                        "burst slope [f'(0)] = T⁻²; (2) adding +J across every ring bond preserves Kirchhoff node balance for "
                        "arbitrary equilibrium conductances w₁, w₂, w₃ and occupancies; (3) the Lagrange identity "
                        "(Σ wᵢ aᵢ²)(Σ wᵢ bᵢ²) − (Σ wᵢ aᵢ bᵢ)² equals the weighted pairwise determinant sum, directly underpinning "
                        "4ab ≤ (a + b)² and TUR bounds; and (4) at equilibrium flux entry, the cubic-in-rate numerator of f'_eq(0) "
                        "is identically −(π₁ e₁³ + π₂ e₂³ + π₁ k₁₂(e₁ − e₂)²) ≤ 0 for all non-negative rates."
                    ),
                    "es": (
                        "Para blindar cada identidad algebraica contra ilusiones de punto flotante, CycleAffinityGates.lean formaliza "
                        "cuatro proposiciones universales en Lean 4 Prelude puro (cero imports externos, sin axiomas ni marcadores "
                        "sorry): (1) la homogeneidad dimensional en el SI verifica la consistencia entre flujo cíclico [J] = T⁻¹, "
                        "producción de entropía [σ/k_B] = T⁻¹, difusividad [D_J] = T⁻¹, razón TUR adimensional [Q_TUR] = 1 y "
                        "pendiente [f'(0)] = T⁻²; (2) sumar +J en todo el anillo preserva el balance de Kirchhoff para conductancias "
                        "arbitrarias w₁, w₂, w₃ y ocupaciones; (3) la identidad de Lagrange (Σ wᵢ aᵢ²)(Σ wᵢ bᵢ²) − (Σ wᵢ aᵢ bᵢ)² "
                        "iguala la suma de determinantes ponderados, base de 4ab ≤ (a + b)² y las cotas TUR; y (4) bajo entrada de "
                        "equilibrio, el numerador cúbico en las tasas de f'_eq(0) es idénticamente −(π₁ e₁³ + π₂ e₂³ + π₁ k₁₂(e₁ − e₂)²) "
                        "≤ 0 para toda tasa no negativa."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Alongside those universal integer propositions (10 core theorems supported by 2 square-nonnegativity lemmas), "
                        "exact rational checks in Python's fractions.Fraction evaluate the heterogeneous TUR Lagrange defect and "
                        "node conservation to zero residual, while dual tilted-eigenvalue solvers verify Q_TUR = 2.3203 ≥ 2. "
                        "Running the verification suite with the planted-defect flag simultaneously corrupts P_o away from 0.40, "
                        "conflates p_eq into the driven exit trace so f'_drv(0) collapses below zero, and appends a forbidden "
                        "sorry lemma compiled under warning-as-error flags—forcing an immediate non-zero exit."
                    ),
                    "es": (
                        "Junto con esas proposiciones enteras universales (10 teoremas centrales apoyados por 2 lemas de no "
                        "negatividad cuadrática), verificaciones racionales en fractions.Fraction de Python evalúan el defecto "
                        "de Lagrange de la TUR y la conservación nodal con residuo nulo, mientras dos solubilizadores de eigenvalores "
                        "inclinados verifican Q_TUR = 2.3203 ≥ 2. Al activar la bandera de defecto plantado, el verificador corrompe "
                        "P_o lejos de 0.40, mezcla p_eq en la ráfaga impulsada para hundir f'_drv(0) bajo cero e inyecta un sorry "
                        "prohibido compilado con advertencias como error, forzando una salida distinta de cero."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Hypothesis and falsification boundary (Tier T1/T2 model deduction; zero clinical claims): In any finite "
                        "Markovian gate sharing a fixed scalar P_o, broken detailed balance cannot be identified from steady-state P_o "
                        "by itself; detecting it requires a time-asymmetric observable such as directional cycle-flux ratios, "
                        "Harada–Sasa fluctuation–response violations, or multi-open-state rising-phase kinetics (k₁₂ e₂ > e₁(e₁ + k₁₂)), "
                        "with steady-state precision constrained by Q_TUR ≥ 2. Observation of a stationary equilibrium gate "
                        "(A = 0, zero external energy input) under equilibrium-flux entry exhibiting a rising-phase open-burst "
                        "density f'(t) > 0, or any stationary Markov cycle violating Q_TUR ≥ 2, would refute this model directly. "
                        "In CycleAffinityGates.lean (core Lean 4 Prelude, zero imports, without unproven placeholders or axioms), "
                        "10 core theorems (plus 2 positivity helper lemmas) machine-check the Kirchhoff iso-P_o balance, Cauchy–Schwarz "
                        "variance identity, equilibrium slope non-positivity, and the +31 versus −18 driven burst sign split."
                    ),
                    "es": (
                        "Hipótesis y frontera de falsación (deducción de modelo Nivel T1/T2; cero afirmaciones clínicas): En toda "
                        "compuerta markoviana finita con escalar P_o fijo, la ruptura del balance detallado no puede identificarse a "
                        "partir de P_o por sí solo; detectarla exige un observable asimétrico en el tiempo, como razones direccionales "
                        "de flujo cíclico, violaciones fluctuación-respuesta de Harada–Sasa o cinética creciente multiestado "
                        "(k₁₂ e₂ > e₁(e₁ + k₁₂)), con precisión acotada por Q_TUR ≥ 2. Observar una compuerta estacionaria en "
                        "equilibrio (A = 0, sin aporte externo) bajo entrada de equilibrio con pendiente creciente f'(t) > 0, o "
                        "cualquier ciclo markoviano estacionario con Q_TUR < 2, refutaría este modelo directamente. En CycleAffinityGates.lean "
                        "(Lean 4 Prelude puro, cero imports, sin axiomas ni marcadores sin prueba), 10 teoremas centrales (más 2 lemas "
                        "auxiliares de positividad) verifican el balance de Kirchhoff iso-P_o, la identidad de Cauchy–Schwarz, la no "
                        "positividad en equilibrio y la división de signos +31 frente a −18."
                    ),
                },
            ],
        },
    ],
    "sidenotes": [
        {
            "label_en": "Sidenote 1 · Why +J Shifts Forward Flux Only",
            "label_es": "Nota al Margen 1 · Por Qué +J Suma Solo al Sentido Directo",
            "en": (
                "Subtracting J/2 from reverse edges would turn rates negative once J/2 > min(w₀); shifting forward fluxes "
                "w₀ + J leaves every reverse rate w₀ / π_j > 0 finite for all J ≥ 0."
            ),
            "es": (
                "Restar J/2 a los flujos inversos volvería negativas las tasas cuando J/2 > mín(w₀); sumar +J solo a las "
                "aristas directas mantiene todas las tasas inversas w₀ / π_j > 0 finitas para todo J ≥ 0."
            ),
        },
        {
            "label_en": "Sidenote 2 · Equilibrium-Entry Requirement",
            "label_es": "Nota al Margen 2 · Requisito de Entrada en Equilibrio",
            "en": (
                "Complete monotonicity f'_eq(t) ≤ 0 at A = 0 holds for equilibrium-flux entry p_eq ∝ (π_O1 e₁, π_O2 e₂). "
                "Artificial non-stationary initialization can transiently tilt f'(0) even on a symmetric graph."
            ),
            "es": (
                "La monotonicidad completa f'_eq(t) ≤ 0 en A = 0 rige para la entrada de equilibrio p_eq ∝ (π_O1 e₁, π_O2 e₂). "
                "Una inicialización no estacionaria artificial puede inclinar f'(0) incluso en un grafo simétrico."
            ),
        },
        {
            "label_en": "Sidenote 3 · ATP Affinity Scale",
            "label_es": "Nota al Margen 3 · Escala de Afinidad del ATP",
            "en": (
                "With w₀ = (0.02, 0.015, 0.01) s⁻¹ and J = 10.0 s⁻¹, A = 19.6291 k_B T matches physiological nucleotide "
                "hydrolysis (~20 k_B T) while keeping P_o fixed at 0.4000."
            ),
            "es": (
                "Con w₀ = (0.02, 0.015, 0.01) s⁻¹ y J = 10.0 s⁻¹, A = 19.6291 k_B T coincide con la hidrólisis fisiológica "
                "de nucleótidos (~20 k_B T) manteniendo P_o fijo en 0.4000."
            ),
        },
        {
            "label_en": "Sidenote 4 · What Lean Checks vs. What Experiments Test",
            "label_es": "Nota al Margen 4 · Qué Revisa Lean frente al Experimento",
            "en": (
                "CycleAffinityGates.lean checks integer algebraic identities and sign inequalities (DERIVED, NOT MEASURED). "
                "Whether a real channel obeys a 3- or 4-state Markov topology rests on single-molecule recording."
            ),
            "es": (
                "CycleAffinityGates.lean verifica identidades algebraicas enteras y desigualdades de signo (DERIVADO, NO MEDIDO). "
                "Si un canal real obedece una topología de 3 o 4 estados depende del registro de molécula única."
            ),
        },
    ],
    "sources": [
        {
            "id": "ES12-ONSAGER1931",
            "citation": "Onsager, L. — Reciprocal Relations in Irreversible Processes. I., Physical Review 37(4), 405–426",
            "doi": "10.1103/physrev.37.405",
            "year": 1931,
            "role_en": "Establishes microscopic reversibility and zero net cycle flux at thermodynamic equilibrium (A = 0).",
            "role_es": "Establece la reversibilidad microscópica y el flujo cíclico nulo en equilibrio termodinámico (A = 0).",
        },
        {
            "id": "ES12-HARADA2005",
            "citation": "Harada, T., & Sasa, S.-i. — Equality Connecting Energy Dissipation with a Violation of the Fluctuation-Response Relation, Physical Review Letters 95(13), 130602",
            "doi": "10.1103/physrevlett.95.130602",
            "year": 2005,
            "role_en": "Links steady-state energy dissipation directly to violations of equilibrium fluctuation-response symmetry.",
            "role_es": "Conecta la disipación estacionaria directamente con la violación de la relación fluctuación-respuesta.",
        },
        {
            "id": "ES12-CSANADY2006",
            "citation": "Csanády, L., Nairn, A. C., & Gadsby, D. C. — Thermodynamics of CFTR Channel Gating: A Spreading Conformational Change Initiates an Irreversible Gating Cycle, Journal of General Physiology 128(5), 523–533",
            "doi": "10.1085/jgp.200609558",
            "year": 2006,
            "role_en": "Measures irreversible ATP-driven gating cycle asymmetry and non-monotonic burst timing in CFTR channels.",
            "role_es": "Mide la asimetría irreversible del ciclo de compuerta por ATP y las ráfagas en canales CFTR.",
        },
        {
            "id": "ES12-SEIFERT2012",
            "citation": "Seifert, U. — Stochastic thermodynamics, fluctuation theorems and molecular machines, Reports on Progress in Physics 75(12), 126001",
            "doi": "10.1088/0034-4885/75/12/126001",
            "year": 2012,
            "role_en": "Formulates Schnakenberg cycle affinities, trajectory entropy production, and fluctuation identities on Markov graphs.",
            "role_es": "Formula las afinidades cíclicas de Schnakenberg, entropía por trayectoria y teoremas de fluctuación.",
        },
        {
            "id": "ES12-BARATO2015",
            "citation": "Barato, A. C., & Seifert, U. — Thermodynamic Uncertainty Relation for Biomolecular Processes, Physical Review Letters 114(15), 158101",
            "doi": "10.1103/physrevlett.114.158101",
            "year": 2015,
            "role_en": "Bounds steady-state current precision by dissipation via Q_TUR = (sigma / k_B) (2 D_J) / J^2 >= 2.",
            "role_es": "Acota la precisión de corrientes estacionarias mediante la disipación Q_TUR = (sigma / k_B) (2 D_J) / J^2 >= 2.",
        },
        {
            "id": "ES12-GINGRICH2016",
            "citation": "Gingrich, T. R., Horowitz, J. M., Perunov, N., & England, J. L. — Dissipation Bounds All Steady-State Current Fluctuations, Physical Review Letters 116(12), 120601",
            "doi": "10.1103/physrevlett.116.120601",
            "year": 2016,
            "role_en": "Derives the large-deviation quadratic bound governing current variance in arbitrary heterogeneous Markov networks.",
            "role_es": "Deriva la cota cuadrática de grandes desviaciones que gobierna la varianza de corrientes en redes heterogéneas.",
        },
        {
            "id": "ES12-RAO2016",
            "citation": "Rao, R., & Esposito, M. — Nonequilibrium Thermodynamics of Chemical Reaction Networks: Wisdom from Stochastic Thermodynamics, Physical Review X 6(4), 041064",
            "doi": "10.1103/physrevx.6.041064",
            "year": 2016,
            "role_en": "Generalizes cycle-affinity decomposition and non-equilibrium dissipation to open chemical reaction loops.",
            "role_es": "Generaliza la descomposición en afinidades cíclicas y disipación a redes abiertas de reacciones químicas.",
        },
        {
            "id": "ES12-ZHANG2018",
            "citation": "Zhang, Z., Liu, F., & Chen, J. — Molecular structure of the ATP-bound, phosphorylated human CFTR, Proceedings of the National Academy of Sciences 115(50), 12757–12762",
            "doi": "10.1073/pnas.1815287115",
            "year": 2018,
            "role_en": "Supplies ATP-bound phosphorylated human CFTR structural coordinates (PDB 6MSM) grounding nucleotide-dimer states.",
            "role_es": "Aporta las coordenadas estructurales de CFTR humano fosforilado unido a ATP (PDB 6MSM).",
        },
        {
            "id": "ES12-VANVU2021",
            "citation": "Van Vu, T., & Hasegawa, Y. — Geometrical Bounds of the Irreversibility in Markovian Systems, Physical Review Letters 126(1), 010601",
            "doi": "10.1103/physrevlett.126.010601",
            "year": 2021,
            "role_en": "Sets geometric Wasserstein speed limits relating state-distribution shifts to irreversible entropy production.",
            "role_es": "Fija cotas geométricas de Wasserstein que vinculan cambios de estado con producción irreversible de entropía.",
        },
    ],
    "skill_path": f"skills/essays/{SLUG}/SKILL.md",
    "verifier_path": f"skills/essays/{SLUG}/verify_essay_cycle_affinity.py",
    "ai_line_en": (
        "AI contribution to cited primary literature: none. Essay prose, bilingual es-MX twin, 3-state iso-P_o and "
        "4-state open-burst kernels, 10-theorem core Lean 4 Prelude companion, and Python verifier were drafted with AI "
        "assistance and checked against cached DOIs."
    ),
    "ai_line_es": (
        "Contribución de IA a la literatura primaria citada: ninguna. El ensayo, su gemelo es-MX, los núcleos de 3 y 4 "
        "estados, los 10 teoremas en Lean 4 Prelude y el verificador en Python se redactaron con apoyo de IA y DOIs en caché."
    ),
}
