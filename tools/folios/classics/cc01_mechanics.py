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


# --------------------------------------------------------------------------------------------- 4. corner load + yaw ----
CORNER_YAW_MODEL = {
    "static_wheel_n": 4000.0,     # MODEL: static corner load on level road (average of 2600 N and 5400 N), N
    "transfer_ref_n": 1400.0,     # MODEL: lateral weight shift magnitude at ay = 0.70 g
    "ay_ref_g": 0.70,             # MODEL: reference lateral acceleration (g) restoring 2600 N / 5400 N in DIFF_MODEL
    "track_front_m": 1.54,        # MODEL: front track width for direct yaw-moment couple M_z, m
}


def corner_load_and_yaw(
    ay_g: float,
    demand_nm: float,
    mode: str,
    m: dict = DIFF_MODEL,
    c: dict = CORNER_YAW_MODEL,
) -> dict:
    """Couple lateral acceleration a_y (g) to front tyre vertical loads N_in / N_out and compute net drive + yaw moment."""
    ay_clamped = max(0.0, min(1.05, float(ay_g)))
    delta_n = min(c["static_wheel_n"] - 400.0, c["transfer_ref_n"] * (ay_clamped / c["ay_ref_g"]))
    n_in = c["static_wheel_n"] - delta_n
    n_out = c["static_wheel_n"] + delta_n
    local_diff = dict(m, load_in_n=n_in, load_out_n=n_out)
    res = axle_split(float(demand_nm), mode, local_diff)
    fx_in = res["road_in"] / m["radius_m"]
    fx_out = res["road_out"] / m["radius_m"]
    # Yaw moment around vehicle CoG from front tractive differential force: (Fx_out - Fx_in) * (track / 2)
    yaw_knm = ((fx_out - fx_in) * (c["track_front_m"] * 0.5)) / 1000.0
    return {
        "ay_g": ay_clamped,
        "load_in_n": n_in,
        "load_out_n": n_out,
        "road_in": res["road_in"],
        "road_out": res["road_out"],
        "brake": res["brake"],
        "road": res["road"],
        "unused": res["unused"],
        "grip_in": res["grip_in"],
        "grip_out": res["grip_out"],
        "yaw_knm": yaw_knm,
    }


# --------------------------------------------------------------------------------------------- 5. coaxial 6-spd DCT ----
DCT_SHIFT_MODEL = {
    "ratios": [3.46, 2.05, 1.30, 0.90, 0.72, 0.58],  # MODEL: illustrative 6-speed overdrive ratios
    "final_drive": 4.06,                              # MODEL: final drive ratio
    "rpm_shift": 6000.0,                              # MODEL: illustrative upshift engine speed
    "torque_in_nm": 280.0,                            # MODEL: illustrative crankshaft torque during powershift
    "overlap_s": 0.20,                                # MODEL: clutch handover overlap duration, s
}


def dct_shift_kinematics(gear_from: int, d: dict = DCT_SHIFT_MODEL) -> dict:
    """Coaxial odd/even shaft speed step and friction slip energy across a 1->2..5->6 powershift."""
    idx = max(0, min(len(d["ratios"]) - 2, int(gear_from) - 1))
    r_cur = d["ratios"][idx]
    r_next = d["ratios"][idx + 1]
    omega_in = d["rpm_shift"] * (2.0 * math.pi / 60.0)
    # Output shaft angular speed matches wheel rate dictated by current ratio before slip completes
    omega_out = omega_in / r_cur
    delta_omega = omega_in - omega_out * r_next
    slip_energy_kj = (0.5 * d["torque_in_nm"] * abs(delta_omega) * d["overlap_s"]) / 1000.0
    ratio_drop_pct = (1.0 - r_next / r_cur) * 100.0
    return {
        "shift_label": f"{idx + 1}→{idx + 2}",
        "r_cur": r_cur,
        "r_next": r_next,
        "ratio_drop_pct": ratio_drop_pct,
        "delta_rpm": abs(delta_omega) * (60.0 / (2.0 * math.pi)),
        "wheel_torque_nm": d["torque_in_nm"] * r_next * d["final_drive"],
        "slip_energy_kj": slip_energy_kj,
    }
