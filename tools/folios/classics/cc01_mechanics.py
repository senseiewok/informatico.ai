"""CC.01 Mechanics Lab: the three small models behind the page (standard library only).

Every input that is not a sourced figure is a MODEL value: illustrative, chosen to make the mechanism visible, and
not a measurement of any Golf. The page labels them that way; the verifier (skills/classics/cc01) re-derives every
number below with an independent implementation and checks the rendered pages against it.

1. Front-axle torque split (open differential, brake-based XDS+, clutch-pack lock).
   - Open differential: each driven wheel receives half the axle torque (Scamarcio et al. 2023), so drive is capped
     at twice what the lighter inside wheel can hold.
   - Brake on the inside wheel: the braking torque lets the differential hold more torque before the inside wheel
     spins, so the outside wheel can receive more (Kakalis et al. 2008: brakes can create a yaw moment with a free
     differential).
   - Clutch pack: torque moves only from the faster wheel to the slower one (Kakalis et al. 2008), up to the locking
     torque; Volkswagen gives 1,600 Nm for the Mk7 GTI Performance front lock (VW 2013 running-gear page).
2. Lap kinematics: average speed = configuration length / lap time, only where the source states the 20,600 m length.
3. Quarter-car: the undamped two-mass, two-spring model, solved exactly; unsprung mass mainly moves the wheel-hop mode
   and sprung mass the body-bounce mode (Паринов 2026).
"""
from __future__ import annotations

import math

# ----------------------------------------------------------------------------------------------- 1. differential ----
DIFF_MODEL = {
    "radius_m": 0.32,          # MODEL: loaded wheel radius
    "mu": 1.0,                 # MODEL: dry-road friction coefficient
    "load_in_n": 2600.0,       # MODEL: inside front wheel load in a hard left-hander (weight moves outward)
    "load_out_n": 5400.0,      # MODEL: outside front wheel load
    "brake_max_nm": 500.0,     # MODEL: largest brake torque XDS+ is allowed to add
    "lock_max_nm": 1600.0,     # VW: maximum locking torque of the Mk7 GTI Performance front lock (2013)
    "demand_max_nm": 3000.0,   # MODEL: top of the throttle slider, torque at the axle
}


def grip_nm(load_n: float, m: dict = DIFF_MODEL) -> float:
    """Largest drive torque a wheel can put down before it spins: mu * N * r."""
    return m["mu"] * load_n * m["radius_m"]


def axle_split(demand_nm: float, mode: str, m: dict = DIFF_MODEL) -> dict:
    """Torque at each front wheel for an axle torque demand. Returns road torques, brake torque and the unused rest."""
    g_in, g_out = grip_nm(m["load_in_n"], m), grip_nm(m["load_out_n"], m)
    half = demand_nm / 2.0
    brake = 0.0
    if mode == "open":
        side = min(half, g_in)                      # both side gears carry the same torque
        road_in, road_out = side, side
    elif mode == "xds":
        side = min(half, g_in + m["brake_max_nm"], g_out)
        brake = max(0.0, side - g_in)               # brake only what the inside tyre cannot hold
        road_in, road_out = side - brake, side
    elif mode == "lock":
        road_in = min(half, g_in)
        # the clutch moves torque from the faster (spinning inside) wheel to the slower one, never the other way
        transfer = min(max(0.0, demand_nm - 2 * road_in), m["lock_max_nm"], g_out - road_in)
        road_out = road_in + max(0.0, transfer)
    else:
        raise ValueError(mode)
    road = road_in + road_out
    return {
        "road_in": road_in, "road_out": road_out, "brake": brake, "road": road,
        "unused": max(0.0, demand_nm - road - brake), "grip_in": g_in, "grip_out": g_out,
        "spinning": half > g_in + 1e-9,
    }


# --------------------------------------------------------------------------------------------- 2. lap kinematics ----
CONFIG_LENGTH_M = 20600.0  # sport auto configuration, stated in the source for the 2016-2021 rows only


def lap_speed_kmh(seconds: float) -> float:
    return CONFIG_LENGTH_M / seconds * 3.6


# ----------------------------------------------------------------------------------------------- 3. quarter car ----
QUARTER_MODEL = {
    "m_s": 350.0,      # MODEL: sprung mass at one corner, kg
    "k_s": 25000.0,    # MODEL: suspension spring rate at the wheel, N/m
    "k_t": 220000.0,   # MODEL: tyre vertical stiffness, N/m
    "m_u_min": 30.0,   # MODEL: slider range for unsprung mass, kg
    "m_u_max": 50.0,
    "m_u_start": 40.0,
}


def quarter_car_hz(m_u: float, q: dict = QUARTER_MODEL) -> tuple[float, float]:
    """Body-bounce and wheel-hop frequencies (Hz) of the undamped two-mass model, from its characteristic equation
    m_s m_u w^4 - (m_s (k_s + k_t) + m_u k_s) w^2 + k_s k_t = 0."""
    m_s, k_s, k_t = q["m_s"], q["k_s"], q["k_t"]
    a = m_s * m_u
    b = -(m_s * (k_s + k_t) + m_u * k_s)
    c = k_s * k_t
    disc = math.sqrt(b * b - 4 * a * c)
    lo, hi = (-b - disc) / (2 * a), (-b + disc) / (2 * a)
    return math.sqrt(lo) / (2 * math.pi), math.sqrt(hi) / (2 * math.pi)
