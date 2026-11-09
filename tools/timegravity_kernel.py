#!/usr/bin/env python3
"""Shared physics kernel for the Time & Gravity track (standard library only).

T.01  A body released at rest in the 1+1 metric ds² = −A(z) c² dt² + dz², A(z) = 1 + 2 g z / c², where only the
      time-time component varies with height. The geodesic equation has no force term; the only surviving
      connection term is Γ^z_tt = A'(z)/2 (x⁰ = ct):
          d²z/dτ² = −(A'/2) (c dt/dτ)²,      d²t/dτ² = −(A'/A) (dt/dτ)(dz/dτ).
T.02  The GPS daily clock correction recomputed from GM, the orbit radius and c (Ashby 2003), two ways
      (first-order terms, and the Schwarzschild rate ratio as a double-entry counter-calculation), with a
      metrology-style uncertainty budget.
T.03  The weak-field Einstein equation reduced to Poisson's equation, solved on a radial grid for a uniform
      sphere and compared with GM/r outside; and the equivalence principle as two bodies of different
      composition released together (Eötvös parameter η).

Used by skills/timegravity/t0x/make_t0x.py (reference artefacts), skills/timegravity/t0x/verify_t0x_*.py
(acceptance gates with planted defects), tools/build_timegravity.py (static SVG fallbacks) and timegravity/make_plates.py.
"""
from __future__ import annotations

import math

C = 299792458.0          # m/s, exact
G0 = 9.80665             # m/s², standard gravity
T_PROPER = 1.0           # s of proper time integrated (T.01)
N_STEPS = 20000
REL_TOL = 1e-6           # |a + g| / g
FLAT_TOL = 1e-12         # |a| with the gradient flattened

# T.02 constants (IERS 2010 / GPS ICD values; the uncertainty budget below says how much each matters)
GM_EARTH = 3.986004418e14     # m³ s⁻², IERS 2010 (geocentric, including atmosphere)
GM_EARTH_SIGMA = 8.0e5        # m³ s⁻², IERS 2010 stated uncertainty
R_EARTH = 6378137.0           # m, equatorial radius (ground clock placed on the equator)
R_EARTH_SIGMA = 1.0e4         # m, the spread a ground clock's height and the geoid introduce (budget input, not a measurement)
A_GPS = 26561750.0            # m, GPS semi-major axis (period 11 h 58 min)
A_GPS_SIGMA = 5.0e3           # m, spread of semi-major axes across the constellation (budget input)
OMEGA_EARTH = 7.2921150e-5    # rad/s
DAY = 86400.0
GPS_TOL_US = 0.7              # µs/day, acceptance window around the reference net value
GPS_DOUBLE_ENTRY_TOL_US = 0.3  # µs/day, the two calculation paths must agree this closely

# T.03 constants
G_NEWTON = 6.67430e-11        # m³ kg⁻¹ s⁻², CODATA 2018
POISSON_REL_TOL = 2e-3        # grid solution against GM/r outside the body
EP_SEP_TOL = 1e-12            # m, allowed separation of two bodies released together (η = 0)


# ----------------------------------------------------------------------------------------------------------------
# T.01 — fall from a slope in the rate of time
# ----------------------------------------------------------------------------------------------------------------
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
    """The T.01 verifier's three checks. With planted_defect the 'real' run uses a flipped slope and must fail."""
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


# ----------------------------------------------------------------------------------------------------------------
# T.02 — everyone moves at one rate: the GPS correction two ways, with an uncertainty budget
# ----------------------------------------------------------------------------------------------------------------
def gps_terms(a: float = A_GPS, gm: float = GM_EARTH, r_ground: float = R_EARTH, sign: float = +1.0) -> dict:
    """First-order terms (Ashby 2003): gravitational (satellite clock runs fast) and velocity (runs slow), µs/day."""
    grav = sign * (gm / C**2) * (1.0 / r_ground - 1.0 / a)
    vel = -(gm / a) / (2.0 * C**2)
    return {"grav_us": grav * DAY * 1e6, "vel_us": vel * DAY * 1e6, "net_us": (grav + vel) * DAY * 1e6}


def gps_schwarzschild_net(a: float = A_GPS, gm: float = GM_EARTH, r_ground: float = R_EARTH,
                          omega: float = OMEGA_EARTH) -> float:
    """Double-entry counter-calculation: the rate ratio from dτ/dt of each clock in the Schwarzschild metric.

    Circular orbit: dτ/dt = √(1 − 3GM/(a c²)) (the 3 folds the orbital speed in). Ground clock on the rotating
    equator: dτ/dt = √(1 − 2GM/(R c²) − (ΩR)²/c²). Returns the net satellite gain in µs per day of ground time.
    """
    sat = math.sqrt(1.0 - 3.0 * gm / (a * C**2))
    ground = math.sqrt(1.0 - 2.0 * gm / (r_ground * C**2) - (omega * r_ground) ** 2 / C**2)
    return (sat / ground - 1.0) * DAY * 1e6


def gps_position_error_per_day_m(net_us: float) -> float:
    """What an uncorrected clock would do to a pseudorange after one day: c × Δt."""
    return C * net_us * 1e-6


def gps_uncertainty_budget(a: float = A_GPS, gm: float = GM_EARTH, r_ground: float = R_EARTH) -> dict:
    """GUM-style budget: numerical sensitivities of the net term to each input, combined in quadrature (1σ)."""
    base = gps_terms(a, gm, r_ground)["net_us"]
    rows = []
    for name, value, sigma, kw in (
        ("GM (IERS 2010)", gm, GM_EARTH_SIGMA, "gm"),
        ("orbit semi-major axis a", a, A_GPS_SIGMA, "a"),
        ("ground clock radius R", r_ground, R_EARTH_SIGMA, "r_ground"),
    ):
        h = sigma
        args = {"a": a, "gm": gm, "r_ground": r_ground}
        args[kw] = value + h
        up = gps_terms(**args)["net_us"]
        args[kw] = value - h
        dn = gps_terms(**args)["net_us"]
        sens = (up - dn) / (2.0 * h)          # µs/day per unit of the input
        contrib = abs(sens * sigma)            # µs/day, 1σ
        rows.append({"input": name, "value": value, "sigma": sigma, "sensitivity_us_per_unit": sens, "contribution_us": contrib})
    combined = math.sqrt(sum(r["contribution_us"] ** 2 for r in rows))
    rotation_us = gps_schwarzschild_net(a, gm, r_ground) - gps_schwarzschild_net(a, gm, r_ground, omega=0.0)
    return {"net_us": base, "rows": rows, "combined_sigma_us": combined,
            "ground_rotation_effect_us": rotation_us,
            "note": "c is exact by definition; eccentricity (periodic, zero mean) and the geoid-vs-equator potential are not in the budget and are the reason the acceptance window is ±%.1f µs/day." % GPS_TOL_US}


def check_gps(planted_defect: bool = False) -> dict:
    """The T.02 verifier. Reference: about +45.7, −7.2 and +38.5 µs/day (Ashby 2003); planted defect: a sign flip."""
    main = gps_terms(sign=-1.0 if planted_defect else +1.0)
    ref = gps_terms()
    counter = gps_schwarzschild_net()
    g_ok = abs(main["grav_us"] - 45.7) < 0.6
    v_ok = abs(main["vel_us"] - (-7.2)) < 0.2
    net_ok = abs(main["net_us"] - 38.5) < GPS_TOL_US
    double_entry_ok = abs(ref["net_us"] - counter) < GPS_DOUBLE_ENTRY_TOL_US
    flipped = gps_terms(sign=-1.0)
    flip_rejected = not (abs(flipped["grav_us"] - 45.7) < 0.6 and abs(flipped["net_us"] - 38.5) < GPS_TOL_US)
    return {
        **main,
        "net_schwarzschild_us": counter,
        "double_entry_diff_us": ref["net_us"] - counter,
        "position_error_per_day_m": gps_position_error_per_day_m(ref["net_us"]),
        "grav_ok": g_ok, "vel_ok": v_ok, "net_ok": net_ok, "double_entry_ok": double_entry_ok,
        "flip_rejected": flip_rejected,
        "ok": g_ok and v_ok and net_ok and double_entry_ok and flip_rejected,
    }


def light_clock_dilation(beta: float) -> float:
    """Lorentz factor γ for a light clock moving at β = v/c: the tick takes γ times longer."""
    return 1.0 / math.sqrt(1.0 - beta * beta)


# ----------------------------------------------------------------------------------------------------------------
# T.03 — what sets the slope: Poisson on a grid, and two bodies released together
# ----------------------------------------------------------------------------------------------------------------
def poisson_radial(mass: float, radius: float, r_max: float, n: int = 2000) -> dict:
    """Solve (1/r²) d/dr (r² dΦ/dr) = 4πGρ for a uniform sphere on a radial grid (Thomas algorithm).

    Boundary conditions: dΦ/dr = 0 at r = 0 (regularity) and Φ(r_max) = −GM/r_max (the exterior solution the
    field equation must reproduce). Returns the grid, Φ, g = −dΦ/dr and the worst relative error against the
    analytic exterior −GM/r for r > radius.
    """
    h = r_max / n
    rho = mass / (4.0 / 3.0 * math.pi * radius**3)
    r = [i * h for i in range(n + 1)]
    # Conservative finite-volume form: (r_{i+1/2}² (Φ_{i+1}-Φ_i) − r_{i-1/2}² (Φ_i-Φ_{i-1})) / (h² r_i²) = 4πGρ_i
    a = [0.0] * (n + 1)
    b = [0.0] * (n + 1)
    cc = [0.0] * (n + 1)
    d = [0.0] * (n + 1)
    def cell_density(ri: float) -> float:
        """Volume-weighted density of the shell [ri−h/2, ri+h/2]: exact at the surface cell, so no half-cell of mass is invented."""
        lo, hi = max(0.0, ri - 0.5 * h), ri + 0.5 * h
        inside_hi = min(hi, radius)
        if inside_hi <= lo:
            return 0.0
        return rho * (inside_hi**3 - lo**3) / (hi**3 - lo**3)

    for i in range(1, n):
        rm = (r[i] - 0.5 * h) ** 2
        rp = (r[i] + 0.5 * h) ** 2
        a[i] = rm / (h * h * r[i] ** 2)
        cc[i] = rp / (h * h * r[i] ** 2)
        b[i] = -(a[i] + cc[i])
        d[i] = 4.0 * math.pi * G_NEWTON * cell_density(r[i])
    # i = 0: regularity, Φ_1 − Φ_0 = 0 to second order (dΦ/dr = 0); use the half-cell balance: 3(Φ_1-Φ_0)/h² = 4πGρ_0
    b[0], cc[0], d[0] = -3.0 / (h * h), 3.0 / (h * h), 4.0 * math.pi * G_NEWTON * rho
    b[n], a[n], d[n] = 1.0, 0.0, -G_NEWTON * mass / r_max
    # Thomas algorithm
    cp = [0.0] * (n + 1)
    dp = [0.0] * (n + 1)
    cp[0] = cc[0] / b[0]
    dp[0] = d[0] / b[0]
    for i in range(1, n + 1):
        den = b[i] - a[i] * cp[i - 1]
        cp[i] = cc[i] / den if i < n else 0.0
        dp[i] = (d[i] - a[i] * dp[i - 1]) / den
    phi = [0.0] * (n + 1)
    phi[n] = dp[n]
    for i in range(n - 1, -1, -1):
        phi[i] = dp[i] - cp[i] * phi[i + 1]
    g = [0.0] * (n + 1)  # |g| = dΦ/dr (inward pull, reported as a positive magnitude)
    for i in range(1, n):
        g[i] = (phi[i + 1] - phi[i - 1]) / (2.0 * h)
    g[n] = (phi[n] - phi[n - 1]) / h
    worst = 0.0
    for i in range(n + 1):
        if r[i] > 1.05 * radius:
            worst = max(worst, abs(phi[i] + G_NEWTON * mass / r[i]) / (G_NEWTON * mass / r[i]))
    # Exterior acceleration against GM/r² at the surface and at 2R
    i_s = min(n, int(round(1.1 * radius / h)))
    g_s = g[i_s]
    g_ref = G_NEWTON * mass / r[i_s] ** 2
    return {"r": r, "phi": phi, "g": g, "rho": rho, "worst_rel_err_exterior": worst,
            "g_surface_rel_err": abs(g_s - g_ref) / g_ref, "phi_center": phi[0],
            "phi_center_analytic": -1.5 * G_NEWTON * mass / radius}


def fall_two_bodies(eta: float = 0.0, g: float = G0, T: float = 1.0) -> dict:
    """Two bodies released together; η is the Eötvös parameter 2(a₁ − a₂)/(a₁ + a₂). Separation after T seconds."""
    a1 = g * (1.0 + 0.5 * eta)
    a2 = g * (1.0 - 0.5 * eta)
    z1 = -0.5 * a1 * T * T
    z2 = -0.5 * a2 * T * T
    return {"a1": a1, "a2": a2, "z1": z1, "z2": z2, "separation_m": abs(z1 - z2)}


def check_poisson_ep(planted_defect: bool = False, n: int = 2000) -> dict:
    """The T.03 verifier: the grid solution recovers GM/r outside the sphere; two compositions fall together."""
    # Earth-like numbers: a uniform sphere with Earth's mass and radius, grid out to 4 R.
    mass = GM_EARTH / G_NEWTON
    sol = poisson_radial(mass, R_EARTH, 4.0 * R_EARTH, n)
    poisson_ok = sol["worst_rel_err_exterior"] < POISSON_REL_TOL and sol["g_surface_rel_err"] < POISSON_REL_TOL
    center_ok = abs(sol["phi_center"] - sol["phi_center_analytic"]) / abs(sol["phi_center_analytic"]) < POISSON_REL_TOL
    eta = 1e-3 if planted_defect else 0.0
    fall = fall_two_bodies(eta)
    ep_ok = fall["separation_m"] < EP_SEP_TOL
    planted = fall_two_bodies(1e-3)
    flip_rejected = not (planted["separation_m"] < EP_SEP_TOL)
    g_surface = G_NEWTON * mass / R_EARTH**2
    return {
        "poisson_worst_rel_err_exterior": sol["worst_rel_err_exterior"],
        "poisson_g_surface_rel_err": sol["g_surface_rel_err"],
        "phi_center_rel_err": abs(sol["phi_center"] - sol["phi_center_analytic"]) / abs(sol["phi_center_analytic"]),
        "g_surface_m_s2": g_surface,
        "separation_m": fall["separation_m"],
        "planted_separation_m": planted["separation_m"],
        "poisson_ok": poisson_ok, "center_ok": center_ok, "ep_ok": ep_ok, "flip_rejected": flip_rejected,
        "ok": poisson_ok and center_ok and ep_ok and flip_rejected,
    }
