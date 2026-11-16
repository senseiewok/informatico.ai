"""CC.02 Stereotomy & Structural Mechanics Lab: four deterministic models behind the Sagrada Família feature.

Standard library only. Every input that is not a published Basilica proportion is labeled MODEL: illustrative, chosen
to make the structural or geometric mechanism visible, and not an engineering calculation for any real member of the
temple. The repository verifier (skills/classics/cc02/verify_cc02_sagrada.py) recomputes every value below with an
independent implementation and checks both language pages against it.

1. Doubly-ruled one-sheet hyperboloid (vault skylights & nave oculi):
   r(u, v) = (a*(cos u - s*v*sin u), b*(sin u + s*v*cos u), v*c),  s in {+1, -1}.
   Satisfies (x/a)^2 + (y/b)^2 - (z/c)^2 = 1 for all u, v and traces straight lines for fixed u.
2. Hanging catenary vs parabola & concentrated lantern load:
   Pure self-weight catenary y(x) = a*(cosh(L/(2a)) - cosh(x/a)) vs equal-span, equal-rise parabola, plus central
   lantern load W_top introducing crown slope parameter alpha_0 = asinh(W_top / (2*H)) and column inclination from
   vertical theta = atan(H / V).
3. Gaudí counter-rotating star columns (n in {6, 8, 10, 12}):
   Basilica total height H_total = 2*n m and shaft proportion H_shaft = 10*D_in; two counter-rotating n-star prisms
   (twist +/- theta(z), with theta(H_shaft) = pi/(2*n)) intersect cleanly from n to 2*n flutes without pinch.
4. Post-tensioned stone tower panel decompression under wind overturning moment:
   sigma_min = (F_pt + N_dead) / A_net - F_pt * |e_pt| / Z_net - M_wind / Z_net >= 0 keeps joints in compression.
"""
from __future__ import annotations

import math

# --------------------------------------------------------------------------------------------- 1. ruled hyperboloid ----
HYPERBOLOID_MODEL = {
    "a_m": 1.80,       # MODEL: semi-major throat radius, m
    "b_m": 1.50,       # MODEL: semi-minor throat radius (elliptical hyperboloid section), m
    "c_m": 2.40,       # MODEL: vertical focal scale c, m
    "v_max": 1.25,     # MODEL: dimensionless half-height parameter |v| <= 1.25 (z = +/- 3.00 m)
}


def hyperboloid_ruling_point(u_rad: float, v: float, family: int = 1, m: dict = HYPERBOLOID_MODEL) -> tuple[float, float, float]:
    """Point on one of the two straight-line ruling families (family in {+1, -1}) of an elliptical one-sheet hyperboloid."""
    s = 1.0 if family >= 0 else -1.0
    a, b, c = m["a_m"], m["b_m"], m["c_m"]
    x = a * (math.cos(u_rad) - s * v * math.sin(u_rad))
    y = b * (math.sin(u_rad) + s * v * math.cos(u_rad))
    z = c * v
    return x, y, z


def hyperboloid_quadric_residual(x: float, y: float, z: float, m: dict = HYPERBOLOID_MODEL) -> float:
    """Evaluates (x/a)^2 + (y/b)^2 - (z/c)^2 - 1.0; identically zero on the hyperboloid surface."""
    return (x / m["a_m"]) ** 2 + (y / m["b_m"]) ** 2 - (z / m["c_m"]) ** 2 - 1.0


def hyperboloid_saddle_metrics(m: dict = HYPERBOLOID_MODEL) -> dict:
    """Throat ellipse, top aperture at v_max, ruling angle and straightness residual."""
    v = m["v_max"]
    scale_top = math.sqrt(1.0 + v * v)
    area_throat = math.pi * m["a_m"] * m["b_m"]
    area_top = math.pi * (m["a_m"] * scale_top) * (m["b_m"] * scale_top)
    ruling_slope_deg = math.degrees(math.atan2(m["c_m"], m["a_m"]))
    p0 = hyperboloid_ruling_point(0.7, -v, 1, m)
    pm = hyperboloid_ruling_point(0.7, 0.0, 1, m)
    p1 = hyperboloid_ruling_point(0.7, v, 1, m)
    collinear_err = math.sqrt(sum((p0[k] + p1[k] - 2.0 * pm[k]) ** 2 for k in range(3)))
    return {
        "area_throat_m2": area_throat,
        "area_top_m2": area_top,
        "aperture_ratio": area_top / area_throat,
        "ruling_pitch_deg": ruling_slope_deg,
        "quadric_residual": abs(hyperboloid_quadric_residual(*p1, m=m)),
        "collinear_err_m": collinear_err,
    }


# ------------------------------------------------------------------------------------ 2. funicular catenary & tilt ----
FUNICULAR_MODEL = {
    "span_m": 15.0,            # MODEL: central nave vault span order, m
    "catenary_a_m": 6.0,       # MODEL: catenary scale parameter a = H / w, m
    "w_kn_per_m": 18.0,        # MODEL: self-weight per meter of vault arc, kN/m
    "lantern_load_kn": 160.0,  # MODEL: concentrated crown lantern load at x = 0, kN
    "lantern_min_kn": 0.0,
    "lantern_max_kn": 320.0,
}


def catenary_y(x_m: float, span_m: float, a_m: float, h_thrust_kn: float, lantern_kn: float) -> float:
    """Elevation y(x) >= 0 of an inverted compression catenary arch carrying self-weight plus a crown point load."""
    alpha0 = math.asinh(lantern_kn / (2.0 * h_thrust_kn)) if lantern_kn > 0.0 else 0.0
    return a_m * (math.cosh(span_m / (2.0 * a_m) + alpha0) - math.cosh(abs(x_m) / a_m + alpha0))


def funicular_equilibrium(lantern_kn: float | None = None, f: dict = FUNICULAR_MODEL) -> dict:
    """Thrust H, support vertical reaction V, crown kink, column angle from vertical, and catenary-vs-parabola gap."""
    L = f["span_m"]
    a = f["catenary_a_m"]
    w = f["w_kn_per_m"]
    W_top = f["lantern_load_kn"] if lantern_kn is None else float(lantern_kn)

    H_kn = w * a
    alpha0 = math.asinh(W_top / (2.0 * H_kn)) if W_top > 0.0 else 0.0
    V_kn = H_kn * math.sinh(L / (2.0 * a) + alpha0)
    rise_loaded_m = catenary_y(0.0, L, a, H_kn, W_top)
    half_arc_m = a * (math.sinh(L / (2.0 * a) + alpha0) - math.sinh(alpha0))
    tilt_from_vertical_deg = math.degrees(math.atan2(H_kn, V_kn))
    kink_deg = 2.0 * math.degrees(math.atan2(0.5 * W_top, H_kn))

    # Pure self-weight catenary (W_top = 0) vs equal-span, equal-rise parabola y_p = f0 * (1 - (2x/L)^2)
    rise_unloaded_m = a * (math.cosh(L / (2.0 * a)) - 1.0)
    max_gap_m = 0.0
    n_samples = 200
    for i in range(n_samples + 1):
        x = (L / 2.0) * (i / n_samples)
        yc = a * (math.cosh(L / (2.0 * a)) - math.cosh(x / a))
        yp = rise_unloaded_m * (1.0 - (2.0 * x / L) ** 2)
        gap = abs(yc - yp)
        if gap > max_gap_m:
            max_gap_m = gap

    return {
        "H_kn": H_kn,
        "V_kn": V_kn,
        "total_arch_weight_kn": 2.0 * w * half_arc_m + W_top,
        "rise_loaded_m": rise_loaded_m,
        "rise_unloaded_m": rise_unloaded_m,
        "half_arc_m": half_arc_m,
        "tilt_from_vertical_deg": tilt_from_vertical_deg,
        "crown_kink_deg": kink_deg,
        "catenary_parabola_max_gap_mm": max_gap_m * 1000.0,
    }


# -------------------------------------------------------------------------- 3. counter-rotating star column hierarchy --
COLUMN_MODEL = {
    "star_tip_ratio": 1.18,   # MODEL: outer star tip radius / inner valley radius
    "duct_radius_frac": 0.14, # MODEL: hollow central service/drainage conduit radius as fraction of R_in (0.14*R_in)
}

# (n_points, stone_en, stone_es, position_en, position_es, inner_diameter_m, model_axial_load_kn)
COLUMN_TIERS = (
    (6,  "Montjuïc sandstone", "Arenisca de Montjuïc", "Side naves", "Naves laterales", 1.05, 4200.0),
    (8,  "Gray granite",       "Granito gris",         "Central nave", "Nave central", 1.40, 8800.0),
    (10, "Black basalt",       "Basalto negro",        "Crossing perimeter", "Perímetro del crucero", 1.75, 16500.0),
    (12, "Red porphyry",       "Pórfido rojo",         "Central crossing (4 pillars)", "Crucero central (4 pilares)", 2.10, 29000.0),
)


def _star_radius(psi: float, n: int, r_in: float, ratio: float) -> float:
    """Exact polar radius of a regular n-pointed star/fluted polygon with valley r_in and tip r_out = r_in * ratio."""
    r_out = r_in * ratio
    sector = 2.0 * math.pi / n
    half = math.pi / n
    phi = abs(((psi + half) % sector) - half)
    denom = r_in * math.sin(half) * math.cos(phi) + (r_out - r_in * math.cos(half)) * math.sin(phi)
    return (r_out * r_in * math.sin(half)) / denom


def counter_twisted_section(n: int, inner_diameter_m: float, axial_load_kn: float, z_frac: float = 0.0,
                            m: dict = COLUMN_MODEL, samples: int = 720) -> dict:
    """Boolean intersection P1(+theta) cap P2(-theta) at shaft fraction z_frac in [0, 1], with theta_max = pi/(2n)."""
    r_in = inner_diameter_m / 2.0
    ratio = m["star_tip_ratio"]
    theta = (math.pi / (2.0 * n)) * max(0.0, min(1.0, z_frac))

    dphi = (2.0 * math.pi) / samples
    area_gross = 0.0
    for i in range(samples):
        phi0 = i * dphi
        phi1 = (i + 0.5) * dphi
        phi2 = (i + 1.0) * dphi
        r0 = min(_star_radius(phi0 - theta, n, r_in, ratio), _star_radius(phi0 + theta, n, r_in, ratio))
        r1 = min(_star_radius(phi1 - theta, n, r_in, ratio), _star_radius(phi1 + theta, n, r_in, ratio))
        r2 = min(_star_radius(phi2 - theta, n, r_in, ratio), _star_radius(phi2 + theta, n, r_in, ratio))
        # Simpson integration of 1/2 r^2 dphi
        area_gross += 0.5 * (dphi / 6.0) * (r0 * r0 + 4.0 * r1 * r1 + r2 * r2)

    r_void = r_in * m["duct_radius_frac"]
    void_area = math.pi * r_void * r_void
    area_net = area_gross - void_area
    # Axial compressive stress: kN / m^2 = kPa; divide by 1000 -> MPa
    stress_mpa = (axial_load_kn / area_net) / 1000.0
    total_height_m = 2.0 * n         # SOURCED Basilica rule: height in meters = double the star points
    shaft_height_m = 10.0 * inner_diameter_m  # SOURCED Basilica rule: 1:10 inner-diameter to shaft-height ratio
    max_twist_deg = math.degrees(math.pi / (2.0 * n))
    edge_flutes = n if z_frac <= 1e-6 else (2 * n)
    return {
        "n": n,
        "total_height_m": total_height_m,
        "shaft_height_m": shaft_height_m,
        "inner_diameter_m": inner_diameter_m,
        "area_gross_m2": area_gross,
        "area_net_m2": area_net,
        "void_area_m2": void_area,
        "stress_mpa": stress_mpa,
        "max_twist_deg": max_twist_deg,
        "edge_flutes": edge_flutes,
    }


# ------------------------------------------------------------------ 4. 18-tower hierarchy & post-tensioned stone panel -
TOWERS_LEDGER = (
    ("Nativity apostles (outer)",  "Apóstoles Natividad (ext.)",  98.4,  "Basilica (~98.4 m)"),
    ("Nativity apostles (inner)",  "Apóstoles Natividad (int.)", 107.0,  "Basilica (~107 m)"),
    ("Passion apostles (outer)",   "Apóstoles Pasión (ext.)",    107.4,  "Basilica (~107.4 m)"),
    ("Passion apostles (inner)",   "Apóstoles Pasión (int.)",    112.2,  "Basilica (~112.2 m)"),
    ("Four Evangelists (each)",    "Cuatro Evangelistas (c/u)",  135.0,  "Basilica (135 m)"),
    ("Virgin Mary",                "Virgen María",               138.0,  "Basilica (138 m)"),
    ("Ulm Minster (reference)",    "Catedral de Ulm (ref.)",     161.5,  "Reference (161.5 m)"),
    ("Jesus Christ (2026)",        "Jesucristo (2026)",          172.5,  "Basilica (172.5 m)"),
    ("Montjuïc Hill (datum)",      "Montaña de Montjuïc (cota)", 177.7,  "Datum (177.7 m)"),
)

TOWER_PANEL_MODEL = {
    "width_m": 2.40,        # MODEL: prefabricated stone panel width b, m
    "thickness_m": 0.45,    # MODEL: stone panel thickness t, m
    "height_m": 4.80,       # MODEL: single story panel height h, m
    "n_ducts": 4,           # MODEL: unbonded post-tensioning tendon ducts
    "duct_radius_m": 0.030, # MODEL: circular duct radius, m
    "pt_eccentricity_m": 0.0,  # MODEL: concentric tendons on centroidal axis
    "dead_load_kn": 320.0,  # MODEL: gravity axial load carried by panel, kN
    "prestress_kn": 1200.0, # MODEL: total post-tensioning force F_pt, kN
    "prestress_min_kn": 0.0,
    "prestress_max_kn": 2000.0,
    "wind_kpa": 1.80,       # MODEL: characteristic wind gust pressure on cantilevered panel strip, kPa
    "wind_min_kpa": 0.50,
    "wind_max_kpa": 3.50,
}


def panel_decompression(prestress_kn: float | None = None, wind_kpa: float | None = None,
                        p: dict = TOWER_PANEL_MODEL) -> dict:
    """Net section area/modulus and minimum extreme-fiber joint stress sigma_min under gravity + PT + wind."""
    b, t, h = p["width_m"], p["thickness_m"], p["height_m"]
    n_d, r_d = p["n_ducts"], p["duct_radius_m"]
    F_pt = p["prestress_kn"] if prestress_kn is None else float(prestress_kn)
    q_w = p["wind_kpa"] if wind_kpa is None else float(wind_kpa)

    a_gross = b * t
    a_ducts = n_d * math.pi * r_d * r_d
    a_net = a_gross - a_ducts
    i_gross = (b * (t ** 3)) / 12.0
    i_ducts = n_d * (math.pi * (r_d ** 4) / 4.0)
    i_net = i_gross - i_ducts
    z_net = i_net / (t / 2.0)

    # Cantilever wind moment M_w = 0.5 * q_w * b * h^2 (kN*m)
    m_wind_knm = 0.5 * q_w * b * (h ** 2)
    sigma_axial_mpa = ((F_pt + p["dead_load_kn"]) / a_net) / 1000.0
    sigma_pt_ecc_mpa = ((F_pt * abs(p["pt_eccentricity_m"])) / z_net) / 1000.0
    sigma_bend_mpa = (m_wind_knm / z_net) / 1000.0
    sigma_min_mpa = sigma_axial_mpa - sigma_pt_ecc_mpa - sigma_bend_mpa
    sigma_max_mpa = sigma_axial_mpa + sigma_pt_ecc_mpa + sigma_bend_mpa

    return {
        "a_net_m2": a_net,
        "z_net_m3": z_net,
        "m_wind_knm": m_wind_knm,
        "sigma_axial_mpa": sigma_axial_mpa,
        "sigma_bend_mpa": sigma_bend_mpa,
        "sigma_min_mpa": sigma_min_mpa,
        "sigma_max_mpa": sigma_max_mpa,
        "compressed_joint": sigma_min_mpa >= 0.0,
    }


# ------------------------------------------------------------------ 5. 1936 plaster-shard algebraic recovery vs drift --
SHARD_RECOVERY_MODEL = {
    "a_true_m": 1.80,       # MODEL: circular hyperboloid throat radius a, m
    "c_true_m": 2.40,       # MODEL: vertical focal scale c, m
    "z1_m": 0.20,           # MODEL: lower caliper chord elevation on 0.35 m plaster shard, m
    "z2_m": 0.55,           # MODEL: upper caliper chord elevation on 0.35 m plaster shard, m
    "z_target_m": 3.00,     # MODEL: full upper vault rim height reconstructed from shard, m
    "caliper_err_mm": 0.0,  # MODEL: default caliper perturbation magnitude, mm
    "caliper_max_mm": 2.0,  # MODEL: maximum caliper noise range for interactive slider, mm
}


def shard_vault_recovery(caliper_err_mm: float = 0.0, s: dict = SHARD_RECOVERY_MODEL) -> dict:
    """Recover global hyperboloid parameters (a, c) from two local chord radii vs local unruled Taylor drift."""
    a_t, c_t = s["a_true_m"], s["c_true_m"]
    z1, z2, zt = s["z1_m"], s["z2_m"], s["z_target_m"]

    def r_true(z: float) -> float:
        return a_t * math.sqrt(1.0 + (z / c_t) ** 2)

    delta_m = float(caliper_err_mm) / 1000.0
    # Apply opposite-sign perturbation at z1 and z2 to represent worst-case angular tilt across the shard
    r1 = r_true(z1) + delta_m
    r2 = r_true(z2) - delta_m

    # Linear system in z^2: r^2(z) = A + M * z^2 where A = a^2 and M = (a/c)^2
    slope_m = (r2 * r2 - r1 * r1) / (z2 * z2 - z1 * z1)
    intercept_a = r1 * r1 - slope_m * z1 * z1
    a_rec = math.sqrt(max(intercept_a, 1e-9))
    c_rec = a_rec / math.sqrt(max(slope_m, 1e-9))
    r_ruled_top = math.sqrt(max(intercept_a + slope_m * zt * zt, 1e-9))

    # Compare against unruled freeform quadratic Taylor continuation from z1
    q1 = math.sqrt(1.0 + (z1 / c_t) ** 2)
    dr1 = (a_t * z1) / (c_t * c_t * q1)
    d2r1 = (a_t / (c_t * c_t)) / (q1 ** 3)
    dz = zt - z1
    r_free_top = r_true(z1) + dr1 * dz + 0.5 * d2r1 * dz * dz

    r_true_top = r_true(zt)
    return {
        "caliper_err_mm": float(caliper_err_mm),
        "r_true_top_m": r_true_top,
        "a_rec_m": a_rec,
        "c_rec_m": c_rec,
        "r_ruled_top_m": r_ruled_top,
        "ruled_err_mm": abs(r_ruled_top - r_true_top) * 1000.0,
        "r_free_top_m": r_free_top,
        "freeform_err_mm": abs(r_free_top - r_true_top) * 1000.0,
    }
