#!/usr/bin/env python3
"""Shared physics kernel for Time & Gravity · T.01 (standard library only).

A body released at rest in the 1+1 metric ds² = −A(z) c² dt² + dz², A(z) = 1 + 2 g z / c², where only the
time-time component varies with height. The geodesic equation has no force term; the only surviving connection
term is Γ^z_tt = A'(z)/2 (x⁰ = ct), so

    d²z/dτ² = −(A'/2) (c dt/dτ)²,      d²t/dτ² = −(A'/A) (dt/dτ)(dz/dτ).

Used by skills/timegravity/t01/make_t01.py (reference artefact), skills/timegravity/t01/verify_t01_*.py
(acceptance gate with planted defect) and tools/build_timegravity.py (static SVG fallback).
"""
from __future__ import annotations

import math

C = 299792458.0          # m/s, exact
G0 = 9.80665             # m/s², standard gravity
T_PROPER = 1.0           # s of proper time integrated
N_STEPS = 20000
REL_TOL = 1e-6           # |a + g| / g
FLAT_TOL = 1e-12         # |a| with the gradient flattened


def integrate(slope_on: bool = True, sign: float = +1.0, g: float = G0, T: float = T_PROPER, n: int = N_STEPS,
              sample_every: int = 0) -> dict:
    """RK4 integration from rest. Returns the effective acceleration 2 z(T) / T² and optional samples."""
    Ap = (2.0 * g / C**2) * sign if slope_on else 0.0
    z, t, dz, dt = 0.0, 0.0, 0.0, 1.0  # dt/dτ = 1/√A(0) = 1
    h = T / n
    samples: list[tuple[float, float, float]] = []

    def acc(z_: float, dz_: float, dt_: float) -> tuple[float, float]:
        A = 1.0 + Ap * z_
        return -(Ap / 2.0) * (C * dt_) ** 2, -(Ap / A) * dt_ * dz_

    for i in range(n):
        if sample_every and i % sample_every == 0:
            samples.append((i * h, t, z))
        ddz1, ddt1 = acc(z, dz, dt)
        z2, dz2, dt2 = z + 0.5 * h * dz, dz + 0.5 * h * ddz1, dt + 0.5 * h * ddt1
        ddz2, ddt2 = acc(z2, dz2, dt2)
        z3, dz3, dt3 = z + 0.5 * h * dz2, dz + 0.5 * h * ddz2, dt + 0.5 * h * ddt2
        ddz3, ddt3 = acc(z3, dz3, dt3)
        z4, dz4, dt4 = z + h * dz3, dz + h * ddz3, dt + h * ddt3
        ddz4, ddt4 = acc(z4, dz4, dt4)
        z += h * (dz + 2 * dz2 + 2 * dz3 + dz4) / 6
        dz += h * (ddz1 + 2 * ddz2 + 2 * ddz3 + ddz4) / 6
        dt += h * (ddt1 + 2 * ddt2 + 2 * ddt3 + ddt4) / 6
        t += h * (dt + 2 * dt2 + 2 * dt3 + dt4) / 6
    if sample_every:
        samples.append((T, t, z))
    return {"a_eff": 2.0 * z / T**2, "z_T": z, "t_T": t, "slope_Ap": Ap, "samples": samples}


def rate_ratio(h: float, g: float = G0) -> float:
    """Clock-rate ratio between two heights h apart in the weak field: √A(h)/√A(0) − 1 ≈ g h / c²."""
    # expm1/log1p keep the 1e-19-sized answer that 1 + 2gh/c² would round away in double precision.
    return math.expm1(0.5 * math.log1p(2.0 * g * h / C**2))


def run_checks(g: float = G0, T: float = T_PROPER, n: int = N_STEPS, planted_defect: bool = False) -> dict:
    """The verifier's three checks. With planted_defect the 'real' run uses a flipped slope and must fail."""
    main = integrate(True, -1.0 if planted_defect else +1.0, g, T, n)
    flat = integrate(False, +1.0, g, T, n)
    flip = integrate(True, -1.0, g, T, n)
    a, a_flat, a_flip = main["a_eff"], flat["a_eff"], flip["a_eff"]
    falls_at_g = abs(a + g) / g < REL_TOL
    knockout_still = abs(a_flat) < FLAT_TOL
    flip_rejected = not (abs(a_flip + g) / g < REL_TOL)
    return {
        "a_eff": a,
        "a_flat": a_flat,
        "a_flip": a_flip,
        "rel_err": abs(a + g) / g,
        "falls_at_g": falls_at_g,
        "knockout_still": knockout_still,
        "flip_rejected": flip_rejected,
        "ok": falls_at_g and knockout_still and flip_rejected,
    }
