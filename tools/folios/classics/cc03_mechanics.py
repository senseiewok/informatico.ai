"""CC.03 Mechanics Lab: the four small models behind the MINI & F56 JCW page (standard library only).

Every input that is not a sourced figure is a MODEL value: illustrative, chosen to make the mechanism visible, and
not a measurement of any specific MINI. The page labels them that way; the verifier (skills/classics/cc03) re-derives
every number below with an independent implementation and checks the rendered pages against it.

1. Axle lateral load transfer and tire load sensitivity ("wheels at the corners"):
   - Steady cornering shifts vertical load ΔF_z = m_axle * g * a_y * h_cg / t_track from the inside tire to the
     outside tire. Ricco et al. (2020) model front-to-total anti-roll moment distribution to manage axle lateral load
     transfer in yaw control.
   - Because pneumatic tire peak lateral grip is sub-linear in vertical load, F_y(F_z) = F_z * (mu_0 - k_load * F_z)
     before wheel lift (strictly on the rising branch F_z_out < mu_0 / (2 * k_load)), shifting ΔF_z reduces total
     axle grip by 2 * k_load * (ΔF_z)^2. Widening track t_track and lowering h_cg cut ΔF_z and shrink that loss.
2. Single-stop front brake rotor adiabatic temperature rise (braking into Paddock Hill Bend):
   - Total kinetic energy shed from v1 to v2 is 0.5 * m_car * (v1^2 - v2^2). With front braking share f_front, each
     front rotor absorbs E_disc = 0.5 * f_front * E_total.
   - Dividing by rotor thermal mass (m_disc * c_p) gives the adiabatic single-stop upper bound ΔT (neglecting pad/hub
     split and airflow convection, which Adamowicz & Grzes 2011 study during repetitive braking).
3. Brands Hatch Indy lap kinematics:
   - Average speed = circuit length / lap time, ONLY where the timing table explicitly states 1.208 miles
     (1,944.087552 m), leaving the MINI CHALLENGE rows blank rather than borrowing a length from another table.
4. North America (US SAE mechanical hp / lb-ft) vs. Europe & Mexico (metric PS / Nm) unit equivalence:
   - The 2.0 L B48 JCW shaft rating of 170.0 kW converts to 227.97 SAE mechanical hp (1 hp = 745.699872 W -> 228 hp
     on MINI USA spec sheets) and 231.14 DIN metric PS (1 PS = 735.49875 W -> 231 PS / 231 hp on MINI Mexico and
     BMW Group releases), while 320 Nm -> 236.02 lb-ft (F56) and 380 Nm -> 280.27 lb-ft (F66).
"""
from __future__ import annotations

# ---------------------------------------------------------------------------- 1. lateral load transfer ----
LOAD_MODEL = {
    "m_axle_kg": 740.0,     # MODEL: illustrative front-axle mass share, kg
    "g": 9.81,              # SI standard gravity, m/s^2
    "ay_start_g": 0.85,     # MODEL: reference steady-state cornering acceleration, g
    "ay_max_g": 1.00,       # MODEL: top of the lateral-g slider, g
    "mu_0": 1.15,           # MODEL: unloaded peak friction intercept
    "k_load": 3.5e-5,       # MODEL: tire load-sensitivity slope, N^-1
    "geometries": {
        # (label_en, label_es, h_cg_m, track_m)
        "tall": ("Tall & narrow box (MODEL)", "Caja alta y angosta (MODELO)", 0.58, 1.36),
        "f56": ("F56 JCW track (1,485 mm)", "Ancho F56 JCW (1,485 mm)", 0.49, 1.485),
        "kart": ("Lowered track stance (MODEL)", "Postura baja de pista (MODELO)", 0.45, 1.50),
    },
}


def lateral_transfer_n(ay_g: float, h_cg_m: float, track_m: float, m: dict = LOAD_MODEL) -> float:
    """Steady-state lateral load transfer across an axle: m_axle * g * a_y * h_cg / t_track."""
    return m["m_axle_kg"] * m["g"] * ay_g * h_cg_m / track_m


def tire_lateral_n(fz_n: float, m: dict = LOAD_MODEL) -> float:
    """Nonlinear peak lateral force on one tyre: F_z * (mu_0 - k_load * F_z)."""
    return fz_n * (m["mu_0"] - m["k_load"] * fz_n)


def axle_cornering(ay_g: float, mode: str, m: dict = LOAD_MODEL) -> dict:
    """Inside/outside tyre vertical loads, total axle lateral grip, and load-sensitivity grip loss."""
    _en, _es, h_cg, track = m["geometries"][mode]
    fz0 = 0.5 * m["m_axle_kg"] * m["g"]
    dfz_raw = lateral_transfer_n(ay_g, h_cg, track, m)
    dfz = min(dfz_raw, fz0)
    fz_in = fz0 - dfz
    fz_out = fz0 + dfz
    fy_in = tire_lateral_n(fz_in, m)
    fy_out = tire_lateral_n(fz_out, m)
    fy_total = fy_in + fy_out
    fy_flat = 2.0 * tire_lateral_n(fz0, m)
    return {
        "h_cg_m": h_cg,
        "track_m": track,
        "fz0": fz0,
        "dfz": dfz,
        "fz_in": fz_in,
        "fz_out": fz_out,
        "fy_in": fy_in,
        "fy_out": fy_out,
        "fy_total": fy_total,
        "fy_flat": fy_flat,
        "grip_loss": max(0.0, fy_flat - fy_total),
        "lifted": dfz_raw >= fz0 - 1e-9,
    }


# --------------------------------------------------------------------- 2. front brake rotor thermal rise ----
BRAKE_MODEL = {
    "m_car_kg": 1220.0,     # F56 JCW automatic kerb weight stated in Wikipedia Mini Hatch table
    "v1_min_kmh": 100.0,    # MODEL: slider min entry speed, km/h
    "v1_max_kmh": 200.0,    # MODEL: slider max entry speed, km/h
    "v1_start_kmh": 160.0,  # MODEL: reference heavy-braking entry speed, km/h
    "v2_kmh": 80.0,         # MODEL: corner apex speed, km/h
    "front_share": 0.72,    # MODEL: front axle share of braking energy under forward weight transfer
    "cp_j_kgk": 460.0,      # MODEL: cast-iron rotor specific heat capacity, J/(kg*K)
    "t_amb_c": 25.0,        # MODEL: ambient disc baseline, deg C
    "rotors": {
        # (label_en, label_es, m_disc_kg)
        "small": ("Small solid disc (3.2 kg, MODEL)", "Disco sólido chico (3.2 kg, MODELO)", 3.2),
        "mid": ("Mid vented disc (7.4 kg, MODEL)", "Disco ventilado medio (7.4 kg, MODELO)", 7.4),
        "brembo": ("Large 4-pot vented disc (9.8 kg, MODEL)", "Disco ventilado grande 4 pistones (9.8 kg, MODELO)", 9.8),
    },
}


def brake_stop_rise(v1_kmh: float, rotor_key: str, b: dict = BRAKE_MODEL) -> dict:
    """Adiabatic single-stop upper bound temperature rise per front brake rotor."""
    _en, _es, m_disc = b["rotors"][rotor_key]
    v1_ms = v1_kmh / 3.6
    v2_ms = b["v2_kmh"] / 3.6
    ke_total_j = 0.5 * b["m_car_kg"] * max(0.0, v1_ms * v1_ms - v2_ms * v2_ms)
    e_front_j = b["front_share"] * ke_total_j
    e_disc_j = e_front_j / 2.0
    dt_c = e_disc_j / (m_disc * b["cp_j_kgk"])
    return {
        "m_disc_kg": m_disc,
        "ke_total_kj": ke_total_j / 1000.0,
        "e_disc_kj": e_disc_j / 1000.0,
        "dt_c": dt_c,
        "t_peak_c": b["t_amb_c"] + dt_c,
    }


# ------------------------------------------------------------------------ 3. Brands Hatch Indy kinematics ----
INDY_MILES = 1.208         # stated in Mini 7 Racing Club lap-records table and Wikipedia Brands Hatch
METRES_PER_MILE = 1609.344
INDY_LENGTH_M = INDY_MILES * METRES_PER_MILE  # 1,944.087552 m


def indy_speed_kmh(seconds: float) -> float:
    return INDY_LENGTH_M / seconds * 3.6


def indy_speed_mph(seconds: float) -> float:
    return INDY_MILES / (seconds / 3600.0)


# ------------------------------------------------------- 4. US SAE hp / lb-ft vs. Europe/Mexico PS / Nm ----
POWER_UNIT_MODEL = {
    "kw": 170.0,                        # B48A20 / B48 JCW shaft output in BMW/MINI Group specifications
    "watts_per_hp_sae": 745.699872,     # Mechanical / SAE horsepower: 550 ft*lbf/s
    "watts_per_ps_metric": 735.49875,   # Metric PS (DIN 66036): 75 kgf*m/s
    "nm_f56": 320.0,                    # F56 JCW peak torque, Nm
    "nm_f66": 380.0,                    # F66 JCW peak torque, Nm
    "nm_per_lbft": 1.3558179483314004,  # Exact SI conversion factor: 1 ft*lbf in N*m
}


def power_ratings(kw: float = POWER_UNIT_MODEL["kw"], p: dict = POWER_UNIT_MODEL) -> dict:
    """Compare mechanical SAE hp and lb-ft (US specs) against metric PS and Nm (Mexico/EU specs)."""
    watts = kw * 1000.0
    return {
        "kw": kw,
        "hp_sae": watts / p["watts_per_hp_sae"],
        "ps_metric": watts / p["watts_per_ps_metric"],
        "lbft_f56": p["nm_f56"] / p["nm_per_lbft"],
        "lbft_f66": p["nm_f66"] / p["nm_per_lbft"],
    }
