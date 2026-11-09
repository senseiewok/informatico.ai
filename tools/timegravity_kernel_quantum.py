#!/usr/bin/env python3
"""Quantum-clock kernel for the Time & Gravity track (standard library only).

T.07  The equation with no time: a Page–Wootters history state on a d-level cyclic clock and a qubit. The global
      state satisfies the constraint H|Ψ⟩⟩ = 0 exactly; conditioning on the clock's time states recovers the
      closed-form Schrödinger evolution of the qubit; conditioning on a different clock basis (the energy basis, a
      different "split") carries no evolution at all. A pure-Python Jacobi eigensolver checks that the state lies in
      the constraint's kernel. Planted defect: a clock whose generator does not match the constraint.
T.04  A clock in two places: the interferometric visibility of a two-level clock in a superposition of two heights,
      V = |cos(ω Δτ / 2)| with Δτ = g Δh T / c² (Zych et al. 2011), computed twice (closed form and explicit state
      overlap). Planted defect: a clock that never decoheres (ω = 0).

Used by skills/timegravity/t07 and t04 (make_*, verify_*), tools/build_timegravity.py (static SVG) and make_plates.py.
"""
from __future__ import annotations

import math

from timegravity_kernel import C, G0

# ---------------------------------------------------------------------------------------------------------- T.07
PW_D = 16          # clock levels (Pegg–Barnett cyclic clock, δ = 1); Hilbert space 2·d = 32
PW_K = 1           # qubit half-splitting in units of the clock quantum 2π/d
PW_TOL = 1e-10


def pw_clock_energies(d: int = PW_D, planted_defect: bool = False) -> list[float]:
    """Centred, equally spaced clock spectrum E_m = 2π m / d. The planted defect bends it to m·|m|: the clock's
    generator then no longer shifts the time states, and the history state is not annihilated by the constraint."""
    ms = list(range(-d // 2, d // 2))
    if planted_defect:
        return [2.0 * math.pi * (m * abs(m)) / d for m in ms]
    return [2.0 * math.pi * m / d for m in ms]


def _cexp(theta: float) -> complex:
    return complex(math.cos(theta), math.sin(theta))


def pw_history_state(d: int = PW_D, k: int = PW_K, planted_defect: bool = False) -> dict:
    """H = H_C ⊗ 1 + 1 ⊗ H_S with H_S = (ε/2) σ_z, ε/2 = 2π k / d, so both qubit energies sit on the clock lattice.
    |Ψ⟩⟩ = (1/√d) Σ_n |t_n⟩ ⊗ e^{-i H_S n}|+x⟩, with |t_n⟩ = (1/√d) Σ_m e^{-i E_m n}|E_m⟩. Basis index: m·2 + s."""
    E = pw_clock_energies(d, planted_defect)
    eps = 4.0 * math.pi * k / d
    e_sys = (+eps / 2.0, -eps / 2.0)
    dim = 2 * d
    inv = 1.0 / math.sqrt(d)
    psi = [0j] * dim
    for n in range(d):
        comp = [_cexp(-e_sys[s] * n) / math.sqrt(2.0) for s in (0, 1)]
        for mi, Em in enumerate(E):
            c_clock = _cexp(-Em * n) * inv
            for s in (0, 1):
                psi[mi * 2 + s] += inv * c_clock * comp[s]
    norm = math.sqrt(sum(abs(x) ** 2 for x in psi))
    psi = [x / norm for x in psi]
    h_diag = [E[i // 2] + e_sys[i % 2] for i in range(dim)]
    residual = math.sqrt(sum(abs(h_diag[i] * psi[i]) ** 2 for i in range(dim)))
    cond, max_dev = [], 0.0
    for n in range(d):
        amp = [0j, 0j]
        for mi, Em in enumerate(E):
            ph = _cexp(Em * n) * inv            # ⟨t_n|E_m⟩
            for s in (0, 1):
                amp[s] += ph * psi[mi * 2 + s]
        w = abs(amp[0]) ** 2 + abs(amp[1]) ** 2
        p_plus = abs((amp[0] + amp[1]) / math.sqrt(2.0)) ** 2 / w if w > 1e-18 else float("nan")
        closed = math.cos(eps * n / 2.0) ** 2
        max_dev = max(max_dev, abs(p_plus - closed))
        cond.append({"n": n, "p_plus_x": p_plus, "closed_form": closed, "weight": w})
    energy_split = []
    for mi in range(d):
        a0, a1 = psi[mi * 2], psi[mi * 2 + 1]
        w = abs(a0) ** 2 + abs(a1) ** 2
        p_plus = abs((a0 + a1) / math.sqrt(2.0)) ** 2 / w if w > 1e-18 else float("nan")
        energy_split.append({"m": mi - d // 2, "p_plus_x": p_plus, "weight": w})
    return {"d": d, "eps": eps, "clock_energies": E, "psi": psi, "h_diag": h_diag, "constraint_residual": residual,
            "conditional": cond, "max_dev_from_schroedinger": max_dev, "energy_split": energy_split}


def jacobi_eigen(a: list[list[float]], tol: float = 1e-12, max_sweeps: int = 60) -> tuple[list[float], list[list[float]]]:
    """Cyclic Jacobi eigensolver for a real symmetric matrix. Returns eigenvalues and eigenvectors (as columns)."""
    n = len(a)
    a = [row[:] for row in a]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_sweeps):
        off = math.sqrt(sum(a[i][j] ** 2 for i in range(n) for j in range(n) if i != j))
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                theta = (a[q][q] - a[p][p]) / (2.0 * a[p][q])
                t = (1.0 if theta >= 0 else -1.0) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k_ in range(n):
                    akp, akq = a[k_][p], a[k_][q]
                    a[k_][p], a[k_][q] = c * akp - s * akq, s * akp + c * akq
                for k_ in range(n):
                    apk, aqk = a[p][k_], a[q][k_]
                    a[p][k_], a[q][k_] = c * apk - s * aqk, s * apk + c * aqk
                for k_ in range(n):
                    vkp, vkq = v[k_][p], v[k_][q]
                    v[k_][p], v[k_][q] = c * vkp - s * vkq, s * vkp + c * vkq
    return [a[i][i] for i in range(n)], v


def pw_kernel_check(state: dict) -> dict:
    """Write H in the time ⊗ σ_x basis (dense Hermitian), embed it as a real symmetric 4d×4d matrix, diagonalise it
    with Jacobi and check that the history state lies entirely in the zero-eigenvalue subspace."""
    d, E, h_diag, psi = state["d"], state["clock_energies"], state["h_diag"], state["psi"]
    dim = 2 * d

    def u(row: int, col: int) -> complex:
        n, sx = divmod(row, 2)
        mi, sz = divmod(col, 2)
        ph = _cexp(E[mi] * n) / math.sqrt(d)
        hx = (1.0 if (sx == 0 or sz == 0) else -1.0) / math.sqrt(2.0)
        return ph * hx

    U = [[u(r, c) for c in range(dim)] for r in range(dim)]
    Hp = [[sum(U[r][k_] * h_diag[k_] * U[c][k_].conjugate() for k_ in range(dim)) for c in range(dim)] for r in range(dim)]
    psi_p = [sum(U[r][k_] * psi[k_] for k_ in range(dim)) for r in range(dim)]
    M = [[0.0] * (2 * dim) for _ in range(2 * dim)]
    for r in range(dim):
        for c in range(dim):
            M[r][c] = Hp[r][c].real
            M[r][c + dim] = -Hp[r][c].imag
            M[r + dim][c] = Hp[r][c].imag
            M[r + dim][c + dim] = Hp[r][c].real
    vals, vecs = jacobi_eigen(M)
    zero_idx = [i for i, lam in enumerate(vals) if abs(lam) < 1e-8]
    x = [z.real for z in psi_p] + [z.imag for z in psi_p]
    proj = 0.0
    for i in zero_idx:
        coef = sum(vecs[r][i] * x[r] for r in range(2 * dim))
        proj += coef * coef
    return {"zero_eigenvalues": len(zero_idx), "kernel_dim": len(zero_idx) // 2, "projection_onto_kernel": proj,
            "eigenvalue_min": min(vals), "eigenvalue_max": max(vals)}


def check_page_wootters(planted_defect: bool = False) -> dict:
    st = pw_history_state(planted_defect=planted_defect)
    kern = pw_kernel_check(st)
    good = pw_history_state(planted_defect=False)
    bad = pw_history_state(planted_defect=True)
    stationary = st["constraint_residual"] < PW_TOL
    schroedinger = st["max_dev_from_schroedinger"] < PW_TOL
    flat_other_split = all(abs(e["p_plus_x"] - 0.5) < 1e-9 for e in good["energy_split"] if e["weight"] > 1e-12)
    in_kernel = abs(kern["projection_onto_kernel"] - 1.0) < 1e-8 and kern["kernel_dim"] >= 1
    defect_rejected = not (bad["constraint_residual"] < PW_TOL and bad["max_dev_from_schroedinger"] < PW_TOL)
    return {"constraint_residual": st["constraint_residual"], "max_dev_from_schroedinger": st["max_dev_from_schroedinger"],
            "kernel_dim": kern["kernel_dim"], "projection_onto_kernel": kern["projection_onto_kernel"],
            "eigenvalue_min": kern["eigenvalue_min"], "eigenvalue_max": kern["eigenvalue_max"],
            "planted_residual": bad["constraint_residual"], "planted_max_dev": bad["max_dev_from_schroedinger"],
            "stationary": stationary, "schroedinger": schroedinger, "flat_other_split": flat_other_split,
            "in_kernel": in_kernel, "defect_rejected": defect_rejected,
            "ok": stationary and schroedinger and flat_other_split and in_kernel and defect_rejected}


# ---------------------------------------------------------------------------------------------------------- T.04
OMEGA_SR = 2.0 * math.pi * 429.228e12   # rad/s, the Sr optical clock transition as an order-of-magnitude anchor
ZYCH_TOL = 1e-12


def proper_time_difference(dh: float, T: float, g: float = G0) -> float:
    """Δτ ≈ g Δh T / c² between two arms held Δh apart for coordinate time T (weak field, first order)."""
    return g * dh * T / C**2


def zych_visibility(dh: float, T: float, omega: float, g: float = G0) -> float:
    """V = |cos(ω Δτ / 2)| for a two-level clock prepared in |+⟩ (Zych et al. 2011, ω = ΔE/ħ)."""
    return abs(math.cos(omega * proper_time_difference(dh, T, g) / 2.0))


def clock_overlap(dh: float, T: float, omega: float, g: float = G0) -> float:
    """Double entry: |⟨ψ(0)|ψ(Δτ)⟩| from explicit state vectors, ψ(τ) = (e^{-iωτ/2}|0⟩ + e^{+iωτ/2}|1⟩)/√2."""
    dtau = proper_time_difference(dh, T, g)

    def state(tau: float) -> list[complex]:
        return [_cexp(-omega * tau / 2) / math.sqrt(2), _cexp(omega * tau / 2) / math.sqrt(2)]

    a, b = state(0.0), state(dtau)
    return abs(sum(x.conjugate() * y for x, y in zip(a, b)))


def zych_first_zero(omega: float, g: float = G0) -> float:
    """The product Δh·T (m·s) at which the visibility first vanishes: ω g Δh T / c² = π."""
    return math.pi * C**2 / (g * omega)


def check_zych(planted_defect: bool = False) -> dict:
    omega = 0.0 if planted_defect else OMEGA_SR
    max_dev = 0.0
    for dh in (0.0, 0.1, 1.0, 3.0, 10.0):
        for T in (0.1, 1.0, 5.0):
            max_dev = max(max_dev, abs(zych_visibility(dh, T, OMEGA_SR) - clock_overlap(dh, T, OMEGA_SR)))
    double_entry = max_dev < ZYCH_TOL
    v0 = zych_visibility(0.0, 1.0, omega)
    dhT = zych_first_zero(OMEGA_SR)
    v_zero = zych_visibility(dhT, 1.0, omega)       # the planted clock keeps V = 1 here
    decoheres = v_zero < 1e-6
    planted_v = zych_visibility(dhT, 1.0, 0.0)
    defect_rejected = not (planted_v < 1e-6)
    return {"max_dev_closed_vs_overlap": max_dev, "v_at_zero_separation": v0, "first_zero_dh_T_m_s": dhT,
            "v_at_first_zero": v_zero, "v_1m_1s_sr_clock": zych_visibility(1.0, 1.0, OMEGA_SR),
            "dtau_1m_1s_s": proper_time_difference(1.0, 1.0), "omega_used": omega,
            "double_entry": double_entry, "unit_at_zero": abs(v0 - 1.0) < ZYCH_TOL, "decoheres": decoheres,
            "defect_rejected": defect_rejected,
            "ok": double_entry and abs(v0 - 1.0) < ZYCH_TOL and decoheres and defect_rejected}
