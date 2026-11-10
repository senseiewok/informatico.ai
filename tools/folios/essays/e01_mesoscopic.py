# -*- coding: utf-8 -*-
"""Cross-Scale Essay ES.01 · The Mesoscopic Floor.

Pure-Python stdlib physics kernel and bilingual (EN / es-MX) monograph data for
Informatico.ai's first Cross-Scale Featured Essay (/essays/mesoscopic-floor/).

Bridges two mesoscopic thermal baths separated by nineteen decades in Knudsen number:
  1. Ultra-high-vacuum cryogenics (4.0 K helium at 10^-15 Pa around an M = 10^-14 kg,
     R = 0.879 um diamond sphere split by Delta_x = 250 um), where Kn >> 1 puts drag
     into the free-molecular Epstein regime, short thermal de Broglie wavelengths
     (lambda_th = 0.436 nm << Delta_x) saturate collisional decoherence independent of
     Delta_x, and long black-body wavelengths (lambda_bb = 1228 um >> Delta_x) leave
     thermal photons in the dipole Delta_x^2 localization regime.
  2. Warm aqueous polymer hydrogels (310.15 K water, eta = 0.691e-3 Pa*s, around an
     R = 50 nm nanoparticle), where Kn << 1 enforces continuum Stokes-Einstein diffusion
     D_0 = k_B T / (6 pi eta R) = 6.58 um^2/s and polymer fibers (r_f = 3.5 nm) impose
     the dimensionless Ogston-Amsden steric hindrance factor
     D_eff / D_0 = exp(-pi * ((R + r_f) / (xi + 2 * r_f))^2).

Across every regime, momentum diffusion and mechanical damping obey the universal
fluctuation-dissipation identity D_p = gamma_m * M * k_B * T.
"""
from __future__ import annotations

import math

# Exact SI 2019 & material constants (aligned with tools/timegravity_kernel_decoherence.py
# and src/research/modules/cross-scale-essays.mjs)
K_B = 1.380649e-23
H_PLANCK = 6.62607015e-34
HBAR = H_PLANCK / (2.0 * math.pi)
C_LIGHT = 299792458.0
ATOMIC_MASS_UNIT_KG = 1.66053906660e-27
HELIUM_MASS_KG = 4.002602 * ATOMIC_MASS_UNIT_KG
HELIUM_KINETIC_DIAMETER_M = 2.60e-10
ZETA_9 = 1.0020083928260822

DIAMOND_DENSITY_KG_M3 = 3510.0
DIAMOND_MASS_QGEM_KG = 1.0e-14
DIAMOND_EPS = complex(5.7, 1.0e-4)

SILICA_DENSITY_KG_M3 = 2200.0
NANOPARTICLE_DENSITY_KG_M3 = 1050.0
NANOPARTICLE_RADIUS_M = 50.0e-9
HYDROGEL_FIBER_RADIUS_M = 3.5e-9
WATER_VISCOSITY_310K_PA_S = 0.691e-3
WATER_EFFECTIVE_MFP_M = 0.28e-9
BODY_TEMP_K = 310.15
CRYO_TEMP_K = 4.0
UHV_PRESSURE_PA = 1.0e-15
QGEM_SPLIT_M = 250.0e-6

GAS_COEFF = {
    "kinetic": math.sqrt(8.0 * math.pi),
    "cited": 16.0 * math.pi * math.sqrt(2.0 * math.pi) / 3.0,
}


def sphere_radius(mass_kg: float, density_kg_m3: float = DIAMOND_DENSITY_KG_M3) -> float:
    """Radius R (m) of a homogeneous sphere of mass M and density rho."""
    return ((3.0 * mass_kg) / (4.0 * math.pi * density_kg_m3)) ** (1.0 / 3.0)


def sphere_mass(radius_m: float, density_kg_m3: float) -> float:
    """Mass M (kg) of a homogeneous sphere of radius R and density rho."""
    return (4.0 / 3.0) * math.pi * (radius_m ** 3) * density_kg_m3


def mean_free_path_gas(
    pressure_pa: float,
    temp_k: float,
    d_mol_m: float = HELIUM_KINETIC_DIAMETER_M,
) -> float:
    """Maxwell hard-sphere gas mean free path lambda_mfp = k_B T / (sqrt(2) pi d^2 P)."""
    return (K_B * temp_k) / (math.sqrt(2.0) * math.pi * (d_mol_m ** 2) * pressure_pa)


def knudsen_number(lambda_mfp_m: float, radius_m: float) -> float:
    """Dimensionless Knudsen number Kn = lambda_mfp / R."""
    return lambda_mfp_m / radius_m


def cunningham_slip_factor(kn: float) -> float:
    """Millikan-Cunningham-Davies slip factor C_c(Kn) bridging Kn << 1 to Kn >> 1."""
    if kn <= 0.0:
        return 1.0
    return 1.0 + kn * (1.257 + 0.400 * math.exp(-1.10 / kn))


def epstein_damping_rate(
    pressure_pa: float,
    temp_k: float,
    radius_m: float,
    density_kg_m3: float = DIAMOND_DENSITY_KG_M3,
    m_gas_kg: float = HELIUM_MASS_KG,
    diffuse: bool = False,
) -> float:
    """Free-molecular Epstein (1924) mechanical damping rate gamma_m (1/s) for Kn >> 1.

    Specular reflection gives beta = (4/3) pi R^2 n m_g v_bar; full diffuse thermal
    accommodation multiplies by (1 + pi/8). Dividing beta by M = (4/3) pi R^3 rho yields
    gamma_m = (P / (R * rho)) * sqrt(8 m_g / (pi k_B T)) * [1 or (1 + pi/8)].
    """
    n_gas = pressure_pa / (K_B * temp_k)
    v_bar = math.sqrt((8.0 * K_B * temp_k) / (math.pi * m_gas_kg))
    beta_spec = (4.0 / 3.0) * math.pi * (radius_m ** 2) * n_gas * m_gas_kg * v_bar
    accom = (1.0 + math.pi / 8.0) if diffuse else 1.0
    mass_kg = sphere_mass(radius_m, density_kg_m3)
    return (beta_spec * accom) / mass_kg


def stokes_damping_rate(
    eta_pa_s: float,
    radius_m: float,
    density_kg_m3: float = NANOPARTICLE_DENSITY_KG_M3,
) -> float:
    """Continuum no-slip Stokes mechanical damping rate gamma_m = 6 pi eta R / M (1/s)."""
    mass_kg = sphere_mass(radius_m, density_kg_m3)
    return (6.0 * math.pi * eta_pa_s * radius_m) / mass_kg


def momentum_diffusion(gamma_m_s: float, mass_kg: float, temp_k: float) -> float:
    """Universal Fluctuation-Dissipation identity D_p = gamma_m * M * k_B * T (kg^2 m^2 / s^3)."""
    return gamma_m_s * mass_kg * K_B * temp_k


def stokes_einstein_diffusivity(
    temp_k: float = BODY_TEMP_K,
    eta_pa_s: float = WATER_VISCOSITY_310K_PA_S,
    radius_m: float = NANOPARTICLE_RADIUS_M,
) -> float:
    """Continuum Stokes-Einstein spatial diffusivity D_0 = k_B T / (6 pi eta R) (m^2/s)."""
    return (K_B * temp_k) / (6.0 * math.pi * eta_pa_s * radius_m)


def gas_thermal_wavelength(m_gas_kg: float = HELIUM_MASS_KG, temp_k: float = CRYO_TEMP_K) -> float:
    """Thermal de Broglie wavelength lambda_th = h / sqrt(2 pi m_g k_B T) (m)."""
    return (2.0 * math.pi * HBAR) / math.sqrt(2.0 * math.pi * m_gas_kg * K_B * temp_k)


def photon_thermal_wavelength(temp_k: float = CRYO_TEMP_K) -> float:
    """Characteristic thermal photon wavelength lambda_bb = pi^(2/3) hbar c / (k_B T) (m)."""
    return (math.pi ** (2.0 / 3.0)) * HBAR * C_LIGHT / (K_B * temp_k)


def gas_localization_long(
    pressure_pa: float,
    temp_k: float,
    radius_m: float,
    m_gas_kg: float = HELIUM_MASS_KG,
) -> float:
    """Long-wavelength collisional localization parameter Lambda_gas (1 / (m^2 s))."""
    return (
        8.0
        * math.sqrt(2.0 * math.pi)
        * math.sqrt(m_gas_kg * K_B * temp_k)
        * pressure_pa
        * (radius_m ** 2)
        / (3.0 * (HBAR ** 2))
    )


def gas_decoherence_saturated(
    pressure_pa: float,
    temp_k: float,
    radius_m: float,
    m_gas_kg: float = HELIUM_MASS_KG,
    form: str = "kinetic",
) -> float:
    """Short-wavelength saturated gas positional decoherence rate Gamma_gas_sat (1/s)."""
    return GAS_COEFF[form] * pressure_pa * (radius_m ** 2) / math.sqrt(m_gas_kg * K_B * temp_k)


def _localization_ansatz(gamma0: float, half_wavelength_m: float, dx_m: float) -> float:
    x = (dx_m * dx_m) / (4.0 * half_wavelength_m * half_wavelength_m)
    return gamma0 * (-math.expm1(-x))


def gas_decoherence_rate(
    dx_m: float,
    pressure_pa: float,
    temp_k: float,
    radius_m: float,
    m_gas_kg: float = HELIUM_MASS_KG,
    form: str = "kinetic",
    planted_defect: bool = False,
) -> float:
    """Collisional positional decoherence rate F_gas(Delta_x) (1/s).

    When planted_defect=True, erroneously applies the long-wavelength quadratic form
    Lambda_gas * Delta_x^2 outside its validity domain (lambda_th << Delta_x).
    """
    if planted_defect:
        return gas_localization_long(pressure_pa, temp_k, radius_m, m_gas_kg) * (dx_m ** 2)
    gamma0 = gas_decoherence_saturated(pressure_pa, temp_k, radius_m, m_gas_kg, form=form)
    a = gas_thermal_wavelength(m_gas_kg, temp_k) / 2.0
    return _localization_ansatz(gamma0, a, dx_m)


def clausius_mossotti(eps: complex = DIAMOND_EPS) -> complex:
    return (eps - 1.0) / (eps + 2.0)


def photon_lambda_scattering(
    radius_m: float,
    temp_env_k: float,
    eps: complex = DIAMOND_EPS,
) -> float:
    """Rayleigh thermal-photon scattering localization parameter Lambda_sc propto R^6 T^9 (1/(m^2 s))."""
    cm_re = clausius_mossotti(eps).real
    k_th = (K_B * temp_env_k) / (HBAR * C_LIGHT)
    return ((40320.0 * 8.0 * ZETA_9 * C_LIGHT * (radius_m ** 6)) / (9.0 * math.pi)) * (k_th ** 9) * (cm_re ** 2)


def photon_lambda_emission(
    radius_m: float,
    temp_k: float,
    eps: complex = DIAMOND_EPS,
) -> float:
    """Dipole thermal-photon emission/absorption localization parameter Lambda_em propto R^3 T^6 (1/(m^2 s))."""
    cm_im = clausius_mossotti(eps).imag
    k_th = (K_B * temp_k) / (HBAR * C_LIGHT)
    return ((16.0 * (math.pi ** 5) * C_LIGHT * (radius_m ** 3)) / 189.0) * (k_th ** 6) * cm_im


def photon_decoherence_rates(
    dx_m: float,
    radius_m: float,
    temp_int_k: float = CRYO_TEMP_K,
    temp_env_k: float = CRYO_TEMP_K,
    eps: complex = DIAMOND_EPS,
) -> dict[str, float]:
    """Long-wavelength thermal-photon decoherence rates (scattering, absorption, emission, total) in 1/s."""
    out: dict[str, float] = {}
    for name, lam, t_k in (
        ("scattering", photon_lambda_scattering(radius_m, temp_env_k, eps), temp_env_k),
        ("absorption", photon_lambda_emission(radius_m, temp_env_k, eps), temp_env_k),
        ("emission", photon_lambda_emission(radius_m, temp_int_k, eps), temp_int_k),
    ):
        a = photon_thermal_wavelength(t_k) / 2.0
        out[name] = _localization_ansatz(4.0 * a * a * lam, a, dx_m)
    out["total"] = out["scattering"] + out["absorption"] + out["emission"]
    return out


def ogston_amsden_hindrance(
    radius_m: float = NANOPARTICLE_RADIUS_M,
    r_fiber_m: float = HYDROGEL_FIBER_RADIUS_M,
    xi_m: float = 300.0e-9,
    planted_defect: bool = False,
) -> float:
    """Dimensionless Ogston-Amsden polymer-mesh steric hindrance factor D_eff / D_0.

    D_eff / D_0 = exp(-pi * ((R + r_f) / (xi + 2 * r_f))^2).
    When planted_defect=True, omits fiber hindrance and returns 1.0 (pure water).
    """
    if planted_defect:
        return 1.0
    ratio = (radius_m + r_fiber_m) / (xi_m + 2.0 * r_fiber_m)
    return math.exp(-math.pi * (ratio ** 2))


def effective_hydrogel_diffusivity(
    xi_m: float,
    temp_k: float = BODY_TEMP_K,
    eta_pa_s: float = WATER_VISCOSITY_310K_PA_S,
    radius_m: float = NANOPARTICLE_RADIUS_M,
    r_fiber_m: float = HYDROGEL_FIBER_RADIUS_M,
    planted_defect: bool = False,
) -> float:
    """Effective Stokes-Einstein-Ogston nanoparticle diffusivity D_eff (m^2/s) in a hydrogel."""
    d0 = stokes_einstein_diffusivity(temp_k, eta_pa_s, radius_m)
    return d0 * ogston_amsden_hindrance(radius_m, r_fiber_m, xi_m, planted_defect=planted_defect)


def evaluate_mesoscopic_floor(planted_defect: bool = False) -> dict:
    """Compute all benchmark quantities checked by verify_essay_mesoscopic_floor.py."""
    r_diam = sphere_radius(DIAMOND_MASS_QGEM_KG, DIAMOND_DENSITY_KG_M3)
    mfp_uhv = mean_free_path_gas(UHV_PRESSURE_PA, CRYO_TEMP_K)
    kn_uhv = knudsen_number(mfp_uhv, r_diam)
    lam_th_4k = gas_thermal_wavelength(HELIUM_MASS_KG, CRYO_TEMP_K)
    lam_bb_4k = photon_thermal_wavelength(CRYO_TEMP_K)

    gamma_epstein_spec = epstein_damping_rate(UHV_PRESSURE_PA, CRYO_TEMP_K, r_diam, DIAMOND_DENSITY_KG_M3, diffuse=False)
    gamma_epstein_diff = epstein_damping_rate(UHV_PRESSURE_PA, CRYO_TEMP_K, r_diam, DIAMOND_DENSITY_KG_M3, diffuse=True)
    dp_uhv = momentum_diffusion(gamma_epstein_spec, DIAMOND_MASS_QGEM_KG, CRYO_TEMP_K)

    gas_100um = gas_decoherence_rate(100.0e-6, UHV_PRESSURE_PA, CRYO_TEMP_K, r_diam, form="kinetic", planted_defect=planted_defect)
    gas_200um = gas_decoherence_rate(200.0e-6, UHV_PRESSURE_PA, CRYO_TEMP_K, r_diam, form="kinetic", planted_defect=planted_defect)
    gas_250um_kin = gas_decoherence_rate(QGEM_SPLIT_M, UHV_PRESSURE_PA, CRYO_TEMP_K, r_diam, form="kinetic", planted_defect=planted_defect)
    gas_250um_cited = gas_decoherence_rate(QGEM_SPLIT_M, UHV_PRESSURE_PA, CRYO_TEMP_K, r_diam, form="cited", planted_defect=planted_defect)
    gas_250um_naive_long = gas_localization_long(UHV_PRESSURE_PA, CRYO_TEMP_K, r_diam) * (QGEM_SPLIT_M ** 2)

    phot_100um = photon_decoherence_rates(100.0e-6, r_diam, CRYO_TEMP_K, CRYO_TEMP_K)
    phot_200um = photon_decoherence_rates(200.0e-6, r_diam, CRYO_TEMP_K, CRYO_TEMP_K)
    phot_250um = photon_decoherence_rates(QGEM_SPLIT_M, r_diam, CRYO_TEMP_K, CRYO_TEMP_K)

    m_np = sphere_mass(NANOPARTICLE_RADIUS_M, NANOPARTICLE_DENSITY_KG_M3)
    kn_water = knudsen_number(WATER_EFFECTIVE_MFP_M, NANOPARTICLE_RADIUS_M)
    gamma_stokes = stokes_damping_rate(WATER_VISCOSITY_310K_PA_S, NANOPARTICLE_RADIUS_M, NANOPARTICLE_DENSITY_KG_M3)
    dp_water = momentum_diffusion(gamma_stokes, m_np, BODY_TEMP_K)
    d0_water = stokes_einstein_diffusivity(BODY_TEMP_K, WATER_VISCOSITY_310K_PA_S, NANOPARTICLE_RADIUS_M)
    d0_from_fdt = (K_B * BODY_TEMP_K) / (m_np * gamma_stokes)

    # Magrini et al. (2021) high-vacuum optomechanics benchmark: R = 71.5 nm silica in 295 K, 0.9 uPa N2
    r_mag = 71.5e-9
    rho_mag = 2200.0
    p_mag = 9.0e-7
    t_mag = 295.0
    m_n2 = 28.0134 * 1.66053906660e-27
    d_n2 = 3.64e-10
    mfp_mag = mean_free_path_gas(p_mag, t_mag, d_n2)
    kn_mag = knudsen_number(mfp_mag, r_mag)
    gamma_mag_diff = epstein_damping_rate(p_mag, t_mag, r_mag, rho_mag, m_gas_kg=m_n2, diffuse=True)
    dp_mag_diff = momentum_diffusion(gamma_mag_diff, sphere_mass(r_mag, rho_mag), t_mag)

    h_open_300 = ogston_amsden_hindrance(NANOPARTICLE_RADIUS_M, HYDROGEL_FIBER_RADIUS_M, 300.0e-9, planted_defect=planted_defect)
    h_mid_120 = ogston_amsden_hindrance(NANOPARTICLE_RADIUS_M, HYDROGEL_FIBER_RADIUS_M, 120.0e-9, planted_defect=planted_defect)
    h_dense_70 = ogston_amsden_hindrance(NANOPARTICLE_RADIUS_M, HYDROGEL_FIBER_RADIUS_M, 70.0e-9, planted_defect=planted_defect)
    h_severe_63 = ogston_amsden_hindrance(NANOPARTICLE_RADIUS_M, HYDROGEL_FIBER_RADIUS_M, 63.0e-9, planted_defect=planted_defect)

    return {
        "uhv_diamond": {
            "mass_kg": DIAMOND_MASS_QGEM_KG,
            "radius_m": r_diam,
            "pressure_pa": UHV_PRESSURE_PA,
            "temp_k": CRYO_TEMP_K,
            "split_m": QGEM_SPLIT_M,
            "mean_free_path_m": mfp_uhv,
            "knudsen": kn_uhv,
            "lambda_th_m": lam_th_4k,
            "lambda_bb_m": lam_bb_4k,
            "gamma_m_epstein_specular_s": gamma_epstein_spec,
            "gamma_m_epstein_diffuse_s": gamma_epstein_diff,
            "dp_epstein_kg2_m2_s3": dp_uhv,
            "gamma_gas_100um_s": gas_100um,
            "gamma_gas_200um_s": gas_200um,
            "gamma_gas_250um_kinetic_s": gas_250um_kin,
            "gamma_gas_250um_cited_s": gas_250um_cited,
            "gamma_gas_250um_naive_long_s": gas_250um_naive_long,
            "photon_100um_scattering_s": phot_100um["scattering"],
            "photon_200um_scattering_s": phot_200um["scattering"],
            "photon_250um_rates_s": phot_250um,
        },
        "aqueous_hydrogel": {
            "radius_m": NANOPARTICLE_RADIUS_M,
            "fiber_radius_m": HYDROGEL_FIBER_RADIUS_M,
            "mass_kg": m_np,
            "temp_k": BODY_TEMP_K,
            "eta_pa_s": WATER_VISCOSITY_310K_PA_S,
            "knudsen_effective": kn_water,
            "gamma_m_stokes_s": gamma_stokes,
            "dp_stokes_kg2_m2_s3": dp_water,
            "d0_m2_s": d0_water,
            "d0_um2_s": d0_water * 1.0e12,
            "d0_from_fdt_m2_s": d0_from_fdt,
            "hindrance_xi_300nm": h_open_300,
            "hindrance_xi_120nm": h_mid_120,
            "hindrance_xi_70nm": h_dense_70,
            "hindrance_xi_63nm": h_severe_63,
            "deff_xi_300nm_um2_s": d0_water * h_open_300 * 1.0e12,
            "deff_xi_120nm_um2_s": d0_water * h_mid_120 * 1.0e12,
            "deff_xi_70nm_um2_s": d0_water * h_dense_70 * 1.0e12,
            "deff_xi_63nm_um2_s": d0_water * h_severe_63 * 1.0e12,
            "slowdown_300_over_70": h_open_300 / h_dense_70,
            "slowdown_300_over_63": h_open_300 / h_severe_63,
        },
        "magrini_hv_silica": {
            "knudsen_n2": kn_mag,
            "gamma_m_epstein_diffuse_n2_s": gamma_mag_diff,
            "dp_epstein_diffuse_n2_kg2_m2_s3": dp_mag_diff,
        },
        "knudsen_span_decades": math.log10(kn_uhv / kn_water),
    }


ESSAY: dict = {
    "code": "ES.01",
    "slug": "mesoscopic-floor",
    "plate_slug": "essay01",
    "date": "2026-11-10",
    "seo": (
        "The Mesoscopic Floor: From Vacuum to Hydrogels",
        "How one thermal bath governs falling diamonds in ultra-high vacuum and hindered nanoparticles in polymer hydrogels across nineteen Knudsen decades.",
        "El Piso Mesoscópico: Del Vacío a los Hidrogeles",
        "Cómo un mismo baño térmico gobierna diamantes en ultra-alto vacío y nanopartículas frenadas en hidrogeles poliméricos en diecinueve décadas Knudsen.",
    ),
    "kicker_en": "Cross-Scale Essay · ES.01 · Stochastic Mechanics, Optomechanics & Soft Matter",
    "kicker_es": "Ensayo Transescalar · ES.01 · Mecánica Estocástica, Optomecánica y Materia Blanda",
    "reading_time_en": "14 min read",
    "reading_time_es": "14 min de lectura",
    "title_en": "The Mesoscopic Floor: Falling Diamonds, Thermal Baths, and Polymer Sieves",
    "title_es": "El Piso Mesoscópico: Diamantes en Caída, Baños Térmicos y Tamices Poliméricos",
    "standfirst_en": (
        "Between single atoms and bulk continua lies a narrow band of matter—roughly 1 nm to 10 µm—where "
        "every surrounding molecule is simultaneously a mechanical brake, a stochastic kick, and a quantum "
        "which-path witness. Follow one fluctuation–dissipation law across 19.6 decades of Knudsen number: "
        "from a 10⁻¹⁴ kg diamond held in spatial superposition at 4.0 K and 10⁻¹⁵ Pa to a 100 nm nanoparticle "
        "threading a 310.15 K polymer hydrogel."
    ),
    "standfirst_es": (
        "Entre los átomos individuales y los medios continuos existe una franja estrecha de materia —de 1 nm a 10 µm— "
        "donde cada molécula vecina actúa a la vez como freno mecánico, impulso estocástico y testigo cuántico de "
        "trayectoria. Sigue una misma ley de fluctuación-disipación a través de 19.6 décadas del número de Knudsen: "
        "desde un diamante de 10⁻¹⁴ kg en superposición espacial a 4.0 K y 10⁻¹⁵ Pa hasta una nanopartícula de 100 nm "
        "cruzando un hidrogel polimérico a 310.15 K."
    ),
    "card_dek_en": (
        "One fluctuation–dissipation floor links 4.0 K vacuum decoherence of 10⁻¹⁴ kg falling diamonds "
        "to Ogston–Amsden steric sieving of 100 nm probes in 310.15 K hydrogels."
    ),
    "card_dek_es": (
        "Un mismo piso de fluctuación-disipación enlaza la decoherencia en vacío a 4.0 K de diamantes de 10⁻¹⁴ kg "
        "con el tamizado estérico de Ogston–Amsden de sondas de 100 nm en hidrogeles a 310.15 K."
    ),
    "instrument_kind": "mesoscopic",
    "predict": {
        "question_en": (
            "A 10⁻¹⁴ kg diamond sphere (radius 0.879 µm) falls at 4.0 K through 10⁻¹⁵ Pa helium gas. "
            "If you double its spatial superposition split Δx from 100 µm to 200 µm, what happens to the "
            "collisional decoherence rate caused by helium atoms—and how do 4.0 K thermal photons compare?"
        ),
        "question_es": (
            "Una esfera de diamante de 10⁻¹⁴ kg (radio 0.879 µm) cae a 4.0 K en gas helio a 10⁻¹⁵ Pa. "
            "Si duplicas su separación espacial Δx de 100 µm a 200 µm, ¿qué ocurre con la tasa de decoherencia "
            "colisional por átomos de helio y cómo se comportan en cambio los fotones térmicos a 4.0 K?"
        ),
        "choices": [
            {
                "id": "a",
                "en": "Both rates quadruple (4×), because wider splits always expose superpositions as Δx².",
                "es": "Ambas tasas se cuadruplican (4×), porque una división mayor siempre expone la superposición como Δx².",
            },
            {
                "id": "b",
                "en": "Helium gas decoherence stays unchanged (1×, already single-hit saturated), while photon decoherence quadruples (4×).",
                "es": "La decoherencia por helio no cambia (1×, ya saturada a un solo impacto), mientras la fotónica se cuadruplica (4×).",
            },
        ],
        "answer": "b",
        "explain_en": (
            "At 4.0 K, helium's thermal de Broglie wavelength is 0.436 nm—more than 200000 times smaller than a "
            "100 µm split. A single colliding atom already resolves which branch the diamond occupies, saturating "
            "the kinetic rate at 6.40 × 10⁻³ s⁻¹ regardless of whether Δx is 100 µm or 200 µm (1×). Thermal photons "
            "at 4.0 K have a 1228 µm wavelength, far wider than Δx, so their dipole localization rate scales as Δx² "
            "and quadruples (4×)."
        ),
        "explain_es": (
            "A 4.0 K, la longitud de onda térmica de de Broglie del helio es 0.436 nm, más de 200000 veces menor que "
            "una división de 100 µm. Un solo átomo que choca ya resuelve qué rama ocupa el diamante, saturando la tasa "
            "cinética en 6.40 × 10⁻³ s⁻¹ tanto en Δx de 100 µm como de 200 µm (1×). Los fotones térmicos a 4.0 K tienen "
            "longitud de onda de 1228 µm, mucho mayor que Δx, por lo que su localización dipolar escala como Δx² y sube 4×."
        ),
    },
    "sections": [
        {
            "id": "thermal-floor",
            "h2_en": "I · One Thermal Floor, Two Opposite Experiments",
            "h2_es": "I · Un Mismo Piso Térmico, Dos Experimentos Opuestos",
            "short_en": "I · Thermal Floor",
            "short_es": "I · Piso Térmico",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Picture two spheres of matter, each invisible to the unaided eye yet composed of billions "
                        "of bound atoms. The first is a monocrystalline diamond microsphere of mass 10⁻¹⁴ kg and "
                        "density 3510 kg/m³, giving a radius of 0.879 µm. In tabletop quantum-gravity proposals "
                        "following Bose et al. (2017) and Schut et al. (2024), that diamond drops inside a 4.0 K "
                        "cryogenic chamber evacuated to 10⁻¹⁵ Pa while a magnetic gradient splits its center of mass "
                        "into two spatial branches separated by Δx = 250 µm for 2.5 s. The second object is an "
                        "uncharged dielectric nanoparticle 100 nm in diameter (radius 50 nm, mass 5.50 × 10⁻¹⁹ kg "
                        "at density 1050 kg/m³) immersed in water at 310.15 K (37 °C) inside an entangled polymer "
                        "hydrogel, the canonical probe of Mason and Weitz (1995) and Lai et al. (2009)."
                    ),
                    "es": (
                        "Imagina dos esferas de materia, ambas invisibles a simple vista pero formadas por miles de "
                        "millones de átomos enlazados. La primera es una microesfera monocristalina de diamante con "
                        "masa de 10⁻¹⁴ kg y densidad de 3510 kg/m³, lo que fija un radio de 0.879 µm. En las propuestas "
                        "de gravedad cuántica de mesa que siguen a Bose et al. (2017) y Schut et al. (2024), ese "
                        "diamante cae dentro de una cámara criogénica a 4.0 K evacuada a 10⁻¹⁵ Pa mientras un gradiente "
                        "magnético divide su centro de masa en dos ramas espaciales separadas por Δx = 250 µm durante "
                        "2.5 s. El segundo objeto es una nanopartícula dieléctrica neutra de 100 nm de diámetro (radio "
                        "de 50 nm, masa de 5.50 × 10⁻¹⁹ kg a densidad de 1050 kg/m³) inmersa en agua a 310.15 K (37 °C) "
                        "dentro de un hidrogel polimérico entrelazado, la sonda clásica de Mason y Weitz (1995) y Lai et al. (2009)."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "At first glance the two experiments belong to distant worlds. One spends every resource "
                        "preventing the environment from learning where the sphere sits; a single helium atom "
                        "striking either branch writes which-path data into the gas and collapses the witness. The "
                        "other relies on relentless thermal bombardment by liquid water to jostle the 50 nm sphere "
                        "across micrometres of porous gel, since at zero Reynolds number an unagitated passive bead "
                        "stands frozen. Yet both inhabit the mesoscopic floor—the 1 nm to 10 µm band where discrete "
                        "impacts, internal modes, and continuum fields meet on equal footing."
                    ),
                    "es": (
                        "A primera vista, los dos experimentos pertenecen a mundos lejanos. Uno invierte cada recurso "
                        "en impedir que el entorno averigüe dónde está la esfera; un solo átomo de helio que golpee "
                        "cualquiera de las ramas inscribe datos de trayectoria en el gas y destruye el testigo. El "
                        "otro depende del bombardeo térmico incesante del agua líquida para empujar la esfera de 50 nm "
                        "a través de micrómetros de gel poroso, pues a Reynolds nulo una esfera pasiva sin agitación "
                        "queda inmóvil. Sin embargo, ambos pisan el piso mesoscópico: la franja de 1 nm a 10 µm donde "
                        "choques discretos, modos internos y campos continuos convergen por igual."
                    ),
                },
                {
                    "type": "bridge",
                    "kicker_en": "Plain-Language Bridge · Why Friction and Jitter Are One Coin",
                    "kicker_es": "Puente en Lenguaje Claro · Por Qué Fricción y Agitación Son una Misma Moneda",
                    "title_en": "You cannot drain momentum from a particle without kicking it back",
                    "title_es": "No puedes drenar momento de una partícula sin devolverle impulsos",
                    "paras": [
                        (
                            "Whenever a fluid or gas slows a moving sphere at mechanical damping rate γ_m, the drag "
                            "does not come from a smooth mathematical syrup; it comes from individual bath quanta—gas "
                            "atoms, liquid molecules, or thermal photons—bouncing off the surface. At temperature T, "
                            "those same collisions hammer the sphere from every side even when its average velocity "
                            "is 0, feeding random momentum variance into its motion at rate 2 D_p per spatial axis.",
                            "Siempre que un fluido o un gas frena una esfera en movimiento con tasa mecánica γ_m, el "
                            "arrastre no proviene de un jarabe matemático continuo, sino de cuantos individuales del "
                            "baño —átomos de gas, moléculas líquidas o fotones térmicos— que rebotan contra su superficie. "
                            "A temperatura T, esos mismos choques golpean la esfera desde todas direcciones incluso cuando "
                            "su velocidad media es 0, inyectando varianza aleatoria de momento a razón de 2 D_p por eje.",
                        ),
                        (
                            "In cryogenic optomechanics, D_p is the enemy: momentum kicks heat the center-of-mass "
                            "oscillator and localize quantum superpositions. In warm soft-matter physics, D_p is the "
                            "engine: divided by squared friction (M γ_m)², the exact same momentum noise becomes the "
                            "Stokes–Einstein spatial diffusivity D_0 that carries nanoparticles through tissue.",
                            "En la optomecánica criogénica, D_p es el enemigo: los impulsos calientan el oscilador del "
                            "centro de masa y localizan las superposiciones cuánticas. En la materia blanda cálida, D_p "
                            "es el motor: dividido entre la fricción al cuadrado (M γ_m)², ese mismo ruido de momento se "
                            "convierte en la difusividad espacial D_0 de Stokes–Einstein que transporta nanopartículas.",
                        ),
                    ],
                },
                {
                    "type": "equation",
                    "label_en": "Universal Fluctuation–Dissipation Identity",
                    "label_es": "Identidad Universal de Fluctuación–Disipación",
                    "formula": "D_p = γ_m M k_B T    ⟺    D_0 = k_B T / (M γ_m) = D_p / (M γ_m)²",
                    "note_en": (
                        "Reviewed across stochastic thermodynamics by Seifert (2012): for a sphere of mass M in "
                        "thermal equilibrium at temperature T, the momentum diffusion constant D_p (kg²·m²/s³) and "
                        "mechanical energy-damping rate γ_m (s⁻¹) lock together regardless of pressure or viscosity."
                    ),
                    "note_es": (
                        "Revisada en la termodinámica estocástica por Seifert (2012): para una esfera de masa M en "
                        "equilibrio térmico a temperatura T, la difusión de momento D_p (kg²·m²/s³) y el amortiguamiento "
                        "mecánico γ_m (s⁻¹) quedan acoplados sin importar la presión ni la viscosidad."
                    ),
                },
            ],
        },
        {
            "id": "knudsen-crossover",
            "h2_en": "II · Nineteen Decades of Knudsen Number: From Stokes Drag to Epstein Ballistics",
            "h2_es": "II · Diecinueve Décadas del Número de Knudsen: Del Arrastre de Stokes a la Balística de Epstein",
            "short_en": "II · Knudsen Crossover",
            "short_es": "II · Cruce de Knudsen",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "While D_p = γ_m M k_B T never breaks across equilibrium baths, the physical law that "
                        "determines γ_m changes completely when we pump out the chamber or immerse the sphere in "
                        "water. The single dimensionless ratio governing that transition is the Knudsen number, "
                        "Kn = λ_mfp / R, comparing the bath's molecular mean free path λ_mfp against the sphere's "
                        "radius R. When Kn << 1, molecules collide with one another thousands of times before "
                        "escaping the sphere's hydrodynamic wake; momentum diffuses collectively as viscous shear η, "
                        "and drag scales linearly with radius as 6π η R. When Kn >> 1, bath molecules travel "
                        "ballistically from wall to sphere without mutual collisions; bulk viscosity η ceases to "
                        "have local meaning, and drag scales with geometric cross-section π R²."
                    ),
                    "es": (
                        "Aunque D_p = γ_m M k_B T nunca se rompe en baños en equilibrio, la ley física que fija γ_m "
                        "cambia por completo al evacuar la cámara o sumergir la esfera en agua. El cociente adimensional "
                        "que gobierna esa transición es el número de Knudsen, Kn = λ_mfp / R, que compara el recorrido "
                        "libre medio molecular λ_mfp del baño con el radio R de la esfera. Cuando Kn << 1, las moléculas "
                        "chocan entre sí miles de veces antes de escapar de la estela hidrodinámica; el momento se "
                        "difunde colectivamente como cortante viscoso η y el arrastre escala linealmente con el radio "
                        "como 6π η R. Cuando Kn >> 1, las moléculas viajan balísticamente de la pared a la esfera sin "
                        "choques mutuos; la viscosidad η pierde significado local y el arrastre escala con el área π R²."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Evaluate Kn at both ends of our mesoscopic span. In liquid water at 310.15 K (viscosity "
                        "η = 0.691 × 10⁻³ Pa·s), the effective intermolecular cage spacing is roughly 0.28 nm. "
                        "Around an R = 50 nm nanoparticle, Kn ≈ 5.6 × 10⁻³, deep inside the no-slip Stokes continuum. "
                        "Its mechanical velocity relaxes at γ_m = 6π η R / M = 1.18 × 10⁹ s⁻¹—in less than 1 ns—while "
                        "momentum fluctuations enter at D_p = 2.79 × 10⁻³⁰ kg²·m²/s³, yielding a free-water spatial "
                        "diffusivity D_0 = 6.58 µm²/s. Now step into high-vacuum optomechanics: Magrini et al. (2021) "
                        "optically trapped a 143 nm silica sphere (R = 71.5 nm) at room temperature and 9 × 10⁻⁹ mbar, "
                        "using real-time Kalman feedback to cool its center-of-mass motion to an average occupancy of "
                        "0.56 phonons, while Dania et al. (2024) levitated a silica nanoparticle in an ion Paul trap "
                        "down to 7 × 10⁻¹¹ mbar, confirming that gas damping falls strictly linearly with pressure P "
                        "to quality factors exceeding 10¹⁰."
                    ),
                    "es": (
                        "Evaluemos Kn en ambos extremos de nuestro arco mesoscópico. En agua líquida a 310.15 K "
                        "(viscosidad η = 0.691 × 10⁻³ Pa·s), el espaciamiento intermolecular efectivo ronda 0.28 nm. "
                        "Alrededor de una nanopartícula de R = 50 nm, Kn ≈ 5.6 × 10⁻³, plenamente dentro del continuo "
                        "de Stokes sin deslizamiento. Su velocidad mecánica se relaja a γ_m = 6π η R / M = 1.18 × 10⁹ s⁻¹ "
                        "—en menos de 1 ns—, mientras las fluctuaciones de momento entran con D_p = 2.79 × 10⁻³⁰ kg²·m²/s³, "
                        "produciendo una difusividad espacial en agua libre de D_0 = 6.58 µm²/s. Pasemos ahora a la "
                        "optomecánica en alto vacío: Magrini et al. (2021) atraparon ópticamente una esfera de sílice "
                        "de 143 nm (R = 71.5 nm) a temperatura ambiente y 9 × 10⁻⁹ mbar, enfriando su movimiento por "
                        "retroalimentación óptima de Kalman hasta 0.56 fonones, mientras Dania et al. (2024) levitaron "
                        "sílice en una trampa de Paul hasta 7 × 10⁻¹¹ mbar, confirmando que el amortiguamiento por gas "
                        "cae linealmente con la presión P hasta factores de calidad superiores a 10¹⁰."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Carry that evacuation all the way to the 4.0 K, 10⁻¹⁵ Pa helium bath of the 0.879 µm QGEM "
                        "diamond. With a helium kinetic diameter of 0.260 nm, the Maxwell mean free path stretches "
                        "to λ_mfp = 1.84 × 10¹¹ m—wider than Earth's orbital radius—giving Kn = 2.09 × 10¹⁷. Between "
                        "the warm hydrogel and the cryogenic drop tower lie 19.6 orders of magnitude in Knudsen "
                        "number. Here the Cunningham–Millikan slip factor C_c(Kn) leaves Stokes's law behind and "
                        "converges onto Epstein's free-molecular drag: γ_m = 5.67 × 10⁻¹⁵ s⁻¹ for specular helium "
                        "rebounds (or 7.90 × 10⁻¹⁵ s⁻¹ for full diffuse thermal accommodation, 1 + π/8), corresponding "
                        "to D_p = 3.13 × 10⁻⁵¹ kg²·m²/s³. Mechanical velocity would take millions of years to damp—yet "
                        "quantum spatial coherence is vastly more fragile than classical velocity."
                    ),
                    "es": (
                        "Llevemos esa evacuación hasta el baño de helio a 4.0 K y 10⁻¹⁵ Pa del diamante QGEM de "
                        "0.879 µm. Con un diámetro cinético del helio de 0.260 nm, el recorrido libre medio de Maxwell "
                        "se estira hasta λ_mfp = 1.84 × 10¹¹ m —mayor que el radio orbital terrestre—, dando "
                        "Kn = 2.09 × 10¹⁷. Entre el hidrogel cálido y la torre criogénica median 19.6 órdenes de "
                        "magnitud en el número de Knudsen. Aquí el factor de deslizamiento de Cunningham–Millikan "
                        "C_c(Kn) deja atrás la ley de Stokes y converge al régimen molecular libre de Epstein: "
                        "γ_m = 5.67 × 10⁻¹⁵ s⁻¹ para rebotes especulares de helio (o 7.90 × 10⁻¹⁵ s⁻¹ con acomodación "
                        "difusa completa, 1 + π/8), lo que fija D_p = 3.13 × 10⁻⁵¹ kg²·m²/s³. La velocidad clásica "
                        "tardaría millones de años en frenarse, pero la coherencia cuántica espacial es mucho más frágil."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Knudsen Crossover & Free-Molecular Epstein Damping",
                    "label_es": "Cruce de Knudsen y Amortiguamiento Molecular Libre de Epstein",
                    "formula": "Kn = λ_mfp / R ,    γ_m(Kn ≫ 1) = (P / (ρ R)) √(8 m_g / (π k_B T)) · [1  or  1 + π/8]",
                    "note_en": (
                        "In the continuum limit (Kn << 1), γ_m = 6π η R / M depends on viscosity η and scales as R⁻² "
                        "at fixed density ρ. In the free-molecular limit (Kn >> 1), Cunningham slip C_c(Kn) ∝ Kn "
                        "cancels η and λ_mfp so γ_m scales linearly with pressure P and inversely with R."
                    ),
                    "note_es": (
                        "En el límite continuo (Kn << 1), γ_m = 6π η R / M depende de la viscosidad η y escala como R⁻² "
                        "a densidad fija ρ. En el límite molecular libre (Kn >> 1), el deslizamiento C_c(Kn) ∝ Kn "
                        "cancela η y λ_mfp de modo que γ_m escala linealmente con la presión P e inversamente con R."
                    ),
                },
            ],
        },
        {
            "id": "wavelength-saturation",
            "h2_en": "III · When One Atom Resolves Two Worlds: Short-Wavelength Saturation vs Photon Dipoles",
            "h2_es": "III · Cuando un Átomo Resuelve Dos Mundos: Saturación de Onda Corta frente a Dipolos Fotónicos",
            "short_en": "III · Decoherence Regimes",
            "short_es": "III · Regímenes de Decoherencia",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Why can a 4.0 K helium bath whose mechanical damping time exceeds 10¹⁴ s still erase a "
                        "quantum superposition in a few seconds? Joos and Zeh (1985) answered this by tracking the "
                        "off-diagonal elements ⟨x|ρ|x′⟩ of the reduced center-of-mass density matrix. Stopping a "
                        "0.879 µm diamond classically requires transferring momentum comparable to its whole mass, "
                        "whereas destroying interference between two spatial branches x and x′ separated by Δx = |x − x′| "
                        "requires only that a single scattered bath quantum leave in an orthogonal quantum state "
                        "|χ_x⟩ versus |χ_{x′}⟩. Whether one scatterer suffices depends on a second dimensionless "
                        "ratio: the bath particle's thermal wavelength λ divided by the branch separation Δx."
                    ),
                    "es": (
                        "¿Por qué un baño de helio a 4.0 K cuyo tiempo de frenado mecánico supera 10¹⁴ s puede borrar "
                        "una superposición cuántica en pocos segundos? Joos y Zeh (1985) respondieron siguiendo los "
                        "elementos fuera de la diagonal ⟨x|ρ|x′⟩ de la matriz de densidad reducida del centro de masa. "
                        "Frenar clásicamente un diamante de 0.879 µm exige transferir momento comparable al de toda su "
                        "masa, mientras que destruir la interferencia entre dos ramas x y x′ separadas por Δx = |x − x′| "
                        "solo requiere que un cuanto dispersado salga en estados ortogonales |χ_x⟩ frente a |χ_{x′}⟩. "
                        "Que baste un solo choque depende de un segundo cociente adimensional: la longitud de onda "
                        "térmica λ del baño dividida entre la separación Δx."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "In 2003, Hornberger et al. proved single-collision saturation experimentally by sending C₇₀ "
                        "fullerene matter waves through controlled background gases in a Talbot–Lau interferometer, "
                        "and a year later Hackermüller et al. (2004) watched internal heating of C₇₀ above 1000 K "
                        "suppress interference fringes via emitted thermal photons. Apply both mechanisms to our "
                        "10⁻¹⁴ kg diamond at 4.0 K and Δx = 250 µm. For helium-4 atoms (mass 6.65 × 10⁻²⁷ kg), the "
                        "thermal de Broglie wavelength is λ_th = h / √(2π m_He k_B T) = 0.436 nm. Because "
                        "λ_th / Δx = 1.75 × 10⁻⁶ << 1, every atom striking the diamond resolves the 250 µm split "
                        "overwhelmingly on impact. Collisional decoherence is therefore completely saturated: the "
                        "kinetic collision rate n v̄ π R² = 6.40 × 10⁻³ s⁻¹ at 10⁻¹⁵ Pa (or 5.36 × 10⁻² s⁻¹ in the "
                        "8π/3 interpolated convention used by QGEM proposals) has zero dependence on Δx. Had one "
                        "carelessly plugged Δx = 250 µm into the textbook long-wavelength formula Λ_gas Δx², one "
                        "would obtain 1.76 × 10¹⁰ s⁻¹—an error of 3.28 × 10¹¹ caused purely by ignoring λ_th << Δx."
                    ),
                    "es": (
                        "En 2003, Hornberger et al. demostraron experimentalmente la saturación por colisión única "
                        "haciendo pasar ondas de materia de fulerenos C₇₀ a través de gases controlados en un "
                        "interferómetro de Talbot–Lau, y un año después Hackermüller et al. (2004) observaron cómo "
                        "el calentamiento interno de C₇₀ por encima de 1000 K borraba las franjas por emisión de "
                        "fotones térmicos. Apliquemos ambos mecanismos a nuestro diamante de 10⁻¹⁴ kg a 4.0 K y "
                        "Δx = 250 µm. Para átomos de helio-4 (masa 6.65 × 10⁻²⁷ kg), la longitud de onda térmica de "
                        "de Broglie es λ_th = h / √(2π m_He k_B T) = 0.436 nm. Como λ_th / Δx = 1.75 × 10⁻⁶ << 1, cada "
                        "átomo que impacta el diamante resuelve con creces la separación de 250 µm. La decoherencia "
                        "colisional queda por tanto saturada: la tasa cinética n v̄ π R² = 6.40 × 10⁻³ s⁻¹ a 10⁻¹⁵ Pa "
                        "(o 5.36 × 10⁻² s⁻¹ en la convención interpolada por 8π/3 de las propuestas QGEM) no depende "
                        "de Δx. Si alguien aplicara descuidadamente la forma de onda larga Λ_gas Δx² a Δx = 250 µm, "
                        "obtendría 1.76 × 10¹⁰ s⁻¹, un error de 3.28 × 10¹¹ por ignorar λ_th << Δx."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Black-body photons at the exact same 4.0 K temperature sit on the opposite side of the "
                        "wavelength divide. Their characteristic thermal wavelength is λ_bb = π^(2/3) ħ c / (k_B T) = "
                        "1228 µm, nearly 5 times wider than the 250 µm branch separation and nearly 1400 times larger "
                        "than the 0.879 µm sphere radius. A single 4.0 K photon cannot pinpoint which branch emitted "
                        "or scattered it; instead, thousands of weak dipole interactions accumulate phase-space "
                        "distinguishability quadratically as Γ_ph = Λ_ph Δx². Elastic Rayleigh scattering off "
                        "diamond's real dielectric constant (Re ε = 5.7) scales steeply as R⁶ T⁹, yielding "
                        "5.59 × 10⁻³ s⁻¹ at 4.0 K and Δx = 250 µm, whereas dipole thermal emission and absorption "
                        "(assuming Im ε = 10⁻⁴) scale as R³ T⁶, adding 4.75 × 10⁻² s⁻¹ each when sphere and walls "
                        "both sit at 4.0 K. Cooling from 4.0 K to 1.0 K slashes photon scattering by 4⁹ = 262144, "
                        "leaving saturated residual gas as the lone standing floor."
                    ),
                    "es": (
                        "Los fotones de cuerpo negro a esa misma temperatura de 4.0 K caen del lado opuesto de la "
                        "frontera ondulatoria. Su longitud de onda térmica característica es λ_bb = π^(2/3) ħ c / (k_B T) "
                        "= 1228 µm, casi 5 veces mayor que la separación de 250 µm y casi 1400 veces mayor que el radio "
                        "de 0.879 µm. Un solo fotón a 4.0 K no logra distinguir qué rama lo emitió o dispersó; en "
                        "cambio, miles de interacciones dipolares débiles acumulan distinguibilidad cuadrática como "
                        "Γ_ph = Λ_ph Δx². La dispersión elástica de Rayleigh sobre la permitividad real del diamante "
                        "(Re ε = 5.7) escala abruptamente como R⁶ T⁹, dando 5.59 × 10⁻³ s⁻¹ a 4.0 K y Δx = 250 µm, "
                        "mientras la emisión y absorción dipolares (con Im ε = 10⁻⁴) escalan como R³ T⁶ y suman "
                        "4.75 × 10⁻² s⁻¹ cada una si esfera y paredes están a 4.0 K. Enfriar de 4.0 K a 1.0 K reduce "
                        "la dispersión fotónica por 4⁹ = 262144, dejando al gas saturado como único piso."
                    ),
                },
                {
                    "type": "analogy",
                    "kicker_en": "Structural Analogy · Harbor Buoys in Rain and Ocean Swell",
                    "kicker_es": "Analogía Estructural · Boyas Portuarias bajo Lluvia y Marejada",
                    "title_en": "Sharp raindrops saturate on impact; broad swells resolve splits as (Δx / λ)²",
                    "title_es": "Las gotas finas saturan al primer golpe; el oleaje largo resuelve como (Δx / λ)²",
                    "paras": [
                        (
                            "Imagine trying to tell from splash echoes whether a harbor post stands at pier A or "
                            "pier B separated by 100 m. If sparse 2 mm raindrops fall from overhead, the very first "
                            "drop that strikes the post splatters locally within millimetres: moving pier B from "
                            "100 m to 200 m away does not make each splash any more informative, because 1 hit "
                            "already settles the post's address. By contrast, a gentle ocean swell of 1200 m "
                            "wavelength rocks both locations with almost identical phase; only the tiny phase lag "
                            "proportional to Δx lets a distant observer infer which pier scattered the wave, so "
                            "scattered wave power carrying position contrast grows as (Δx / λ)².",
                            "Imagina intentar deducir por ecos en el agua si un poste portuario está en el muelle A o "
                            "en el muelle B, separados por 100 m. Si caen gotas aisladas de 2 mm, la primera gota que "
                            "golpea el poste salpica localmente en milímetros: alejar el muelle B de 100 m a 200 m no "
                            "vuelve más informativa cada salpicadura, porque 1 impacto ya fija la dirección. En cambio, "
                            "una marejada suave de 1200 m de longitud de onda mece ambos puntos casi con la misma fase; "
                            "solo el pequeño desfase proporcional a Δx delata qué muelle dispersó la onda, por lo que "
                            "la potencia con contraste posicional crece como (Δx / λ)².",
                        ),
                        (
                            "Where the analogy stops: a classical harbor post always occupies either pier A or pier B "
                            "before any drop lands. In the QGEM interferometer, the diamond is entangled with an "
                            "embedded nitrogen-vacancy spin across both branches simultaneously; decoherence is the "
                            "entanglement of bath states |χ_L⟩ and |χ_R⟩ that drives ⟨χ_R|χ_L⟩ → 0 without moving "
                            "center-of-mass energy. Furthermore, quantum matter waves diffract around the sphere "
                            "within a forward shadow cone of angle ħ / (p R), doubling the total cross-section to "
                            "2π R²—a purely wave-mechanical shadow absent from classical raindrops.",
                            "Dónde termina la analogía: un poste clásico ocupa siempre el muelle A o el muelle B antes "
                            "de cualquier gota. En el interferómetro QGEM, el diamante está entrelazado con un espín "
                            "nitrógeno-vacante en ambas ramas a la vez; la decoherencia es el entrelazamiento con los "
                            "estados del baño |χ_L⟩ y |χ_R⟩ que lleva ⟨χ_R|χ_L⟩ → 0 sin transferir energía macroscópica. "
                            "Además, las ondas de materia difractan alrededor de la esfera en un cono frontal de ángulo "
                            "ħ / (p R), duplicando la sección eficaz total a 2π R², una sombra ondulatoria ausente en gotas clásicas.",
                        ),
                    ],
                },
                {
                    "type": "equation",
                    "label_en": "Asymptotic Positional Decoherence Split Scaling",
                    "label_es": "Escalamiento Asintótico de Decoherencia Posicional",
                    "formula": "Γ_gas(λ_th ≪ Δx) = √(8π) P R² / √(m_g k_B T) ,    Γ_ph(λ_bb ≫ Δx) = (Λ_sc + Λ_em + Λ_abs) Δx²",
                    "note_en": (
                        "At 4.0 K and 10⁻¹⁵ Pa around R = 0.879 µm, helium atoms sit in the Δx⁰ short-wavelength "
                        "plateau (λ_th = 0.436 nm), whereas thermal photons sit in the Δx² dipole regime "
                        "(λ_bb = 1228 µm, Λ_sc ∝ R⁶ T⁹, Λ_em ∝ R³ T⁶)."
                    ),
                    "note_es": (
                        "A 4.0 K y 10⁻¹⁵ Pa alrededor de R = 0.879 µm, los átomos de helio están en la meseta Δx⁰ de "
                        "onda corta (λ_th = 0.436 nm), mientras los fotones térmicos están en el régimen dipolar Δx² "
                        "(λ_bb = 1228 µm, Λ_sc ∝ R⁶ T⁹, Λ_em ∝ R³ T⁶)."
                    ),
                },
            ],
        },
        {
            "id": "hydrogel-hindrance",
            "h2_en": "IV · The Warm Continuum Sieve: Stokes–Einstein Motion and Ogston–Amsden Mesh Hindrance",
            "h2_es": "IV · El Tamiz Continuo Cálido: Movimiento de Stokes–Einstein e Impedimento de Malla de Ogston–Amsden",
            "short_en": "IV · Hydrogel Sieve",
            "short_es": "IV · Tamiz de Hidrogel",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Now warm the bath from 4.0 K to 310.15 K (37 °C), flood the vacuum with liquid water "
                        "(η = 0.691 × 10⁻³ Pa·s), and shrink the test sphere to an R = 50 nm nanoparticle (100 nm "
                        "diameter). Quantum spatial superpositions across micrometres vanish in picoseconds here, "
                        "yet the exact same thermal bath energy k_B T = 4.28 × 10⁻²¹ J becomes a measurable "
                        "transport resource. In pure water, Stokes–Einstein diffusion drives mean-squared "
                        "displacement ⟨Δr²(τ)⟩ = 6 D_0 τ at D_0 = 6.58 µm²/s. Mason and Weitz (1995) showed that "
                        "recording those thermal trajectories optically turns a passive sub-micrometre bead into a "
                        "broadband mechanical rheometer: whenever surrounding macromolecular chains store elastic "
                        "energy or obstruct pores, ⟨Δr²(τ)⟩ bends below the pure-water line by the exact compliance "
                        "of the network."
                    ),
                    "es": (
                        "Calentemos ahora el baño de 4.0 K a 310.15 K (37 °C), inundemos el vacío con agua líquida "
                        "(η = 0.691 × 10⁻³ Pa·s) y reduzcamos la esfera de prueba a una nanopartícula de R = 50 nm "
                        "(100 nm de diámetro). Aquí las superposiciones espaciales micrométricas desaparecen en "
                        "picosegundos, pero esa misma energía térmica k_B T = 4.28 × 10⁻²¹ J se vuelve un recurso "
                        "medible de transporte. En agua pura, la difusión de Stokes–Einstein impulsa el desplazamiento "
                        "cuadrático medio ⟨Δr²(τ)⟩ = 6 D_0 τ con D_0 = 6.58 µm²/s. Mason y Weitz (1995) demostraron "
                        "que registrar ópticamente esas trayectorias convierte una esfera pasiva submicrométrica en "
                        "un reómetro mecánico de banda ancha: cuando las cadenas macromoleculares almacenan energía "
                        "elástica u obstruyen poros, ⟨Δr²(τ)⟩ cae por debajo de la recta del agua según la red."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Consider what happens when our non-adhesive R = 50 nm probe enters an entangled biopolymer "
                        "hydrogel built from flexible glycoprotein fibers of radius r_f = 3.5 nm (7.0 nm diameter) "
                        "separated by correlation mesh spacing ξ. Even when interstitial water between fibers keeps "
                        "its bulk viscosity 0.691 × 10⁻³ Pa·s and surface PEGylation prevents chemical sticking "
                        "(Lai et al., 2009), random fiber crossings act as a stochastic geometric sieve. Under the "
                        "dimensionless Ogston–Amsden steric hindrance law, the probability that a thermal step "
                        "finds an unobstructed opening of effective radius R + r_f inside a pore cell of span "
                        "ξ + 2 r_f decays Gaussianly with their squared ratio: "
                        "D_eff / D_0 = exp(−π ((R + r_f) / (ξ + 2 r_f))²)."
                    ),
                    "es": (
                        "Veamos qué ocurre cuando nuestra sonda no adhesiva de R = 50 nm entra en un hidrogel "
                        "biopolimérico entrelazado formado por fibras glucoproteicas flexibles de radio r_f = 3.5 nm "
                        "(7.0 nm de diámetro) con espaciamiento de correlación ξ. Incluso cuando el agua intersticial "
                        "entre fibras conserva su viscosidad de 0.691 × 10⁻³ Pa·s y el recubrimiento denso con PEG "
                        "evita la adhesión química (Lai et al., 2009), los cruces aleatorios de fibras actúan como un "
                        "tamiz geométrico estocástico. Según la ley adimensional de impedimento estérico de "
                        "Ogston–Amsden, la probabilidad de hallar una abertura libre de radio efectivo R + r_f en una "
                        "celda de ancho ξ + 2 r_f decae gaussianamente con su cociente al cuadrado: "
                        "D_eff / D_0 = exp(−π ((R + r_f) / (ξ + 2 r_f))²)."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Because the steric ratio sits inside a negative quadratic exponential, modest osmotic "
                        "compression of the mesh triggers a sharp transport cliff. In an open, well-hydrated polymer "
                        "network with ξ = 300 nm, (R + r_f) / (ξ + 2 r_f) = 53.5 / 307.0 = 0.174, giving "
                        "D_eff / D_0 = 0.909 (90.9% of free water, or D_eff = 5.98 µm²/s). Compress the mesh to an "
                        "intermediate spacing of ξ = 120 nm—the default setting of the interactive instrument above—and "
                        "D_eff / D_0 drops to 0.573 (3.77 µm²/s). When osmotic dehydration concentrates mucin solids "
                        "above 8%, collapsing the periciliary-adjacent gel mesh into the 70 nm to 63 nm window "
                        "characterized by Button et al. (2012) in biophysical studies of Cystic Fibrosis airway "
                        "hydrogels, hindrance plunges to D_eff / D_0 = 0.220 at ξ = 70 nm (1.44 µm²/s, 4.14× slower "
                        "than the 300 nm mesh) and 0.160 at ξ = 63 nm (1.05 µm²/s, 5.70× slower than the open mesh "
                        "and 6.27× slower than pure water). Crossing a 25 µm hydrogel slab by 1D Brownian passage "
                        "(τ = L² / (2 D_eff)) stretches from 52.3 s at ξ = 300 nm to 216.6 s at ξ = 70 nm and "
                        "298.3 s at ξ = 63 nm—before any hydrophobic or electrostatic binding is even counted."
                    ),
                    "es": (
                        "Como el cociente estérico aparece dentro de una exponencial cuadrática negativa, una "
                        "compresión osmótica moderada de la malla dispara un desplome abrupto del transporte. En una "
                        "red polimérica abierta y bien hidratada con ξ = 300 nm, (R + r_f) / (ξ + 2 r_f) = 53.5 / 307.0 "
                        "= 0.174, lo que arroja D_eff / D_0 = 0.909 (90.9% del agua libre, o D_eff = 5.98 µm²/s). Al "
                        "comprimir la malla a un espaciamiento intermedio de ξ = 120 nm —el valor inicial del instrumento "
                        "interactivo—, D_eff / D_0 baja a 0.573 (3.77 µm²/s). Cuando la deshidratación osmótica concentra "
                        "sólidos de mucina por encima de 8%, colapsando los poros del gel hacia la ventana de 70 nm a "
                        "63 nm medida por Button et al. (2012) en estudios biofísicos de hidrogeles de vías aéreas con "
                        "fibrosis quística, el factor cae a D_eff / D_0 = 0.220 en ξ = 70 nm (1.44 µm²/s, 4.14× más "
                        "lento que la malla de 300 nm) y a 0.160 en ξ = 63 nm (1.05 µm²/s, 5.70× más lento que la malla "
                        "abierta y 6.27× más lento que el agua pura). Cruzar una capa de 25 µm en difusión 1D "
                        "(τ = L² / (2 D_eff)) pasa de 52.3 s en ξ = 300 nm a 216.6 s en ξ = 70 nm y 298.3 s en ξ = 63 nm, "
                        "incluso antes de contar cualquier atrapamiento electrostático o hidrofóbico."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Stokes–Einstein–Ogston–Amsden Hydrogel Transport",
                    "label_es": "Transporte en Hidrogel de Stokes–Einstein–Ogston–Amsden",
                    "formula": "D_eff(R, ξ) = [ k_B T / (6π η R) ] · exp( −π [ (R + r_f) / (ξ + 2 r_f) ]² )",
                    "note_en": (
                        "For an R = 50 nm stealth nanoparticle in 310.15 K water (η = 0.691 × 10⁻³ Pa·s, D_0 = 6.58 µm²/s) "
                        "among r_f = 3.5 nm fibers, shrinking ξ from 300 nm to 70 nm and 63 nm cuts D_eff / D_0 from "
                        "0.909 to 0.220 and 0.160."
                    ),
                    "note_es": (
                        "Para una nanopartícula furtiva de R = 50 nm en agua a 310.15 K (η = 0.691 × 10⁻³ Pa·s, "
                        "D_0 = 6.58 µm²/s) entre fibras de r_f = 3.5 nm, reducir ξ de 300 nm a 70 nm y 63 nm recorta "
                        "D_eff / D_0 de 0.909 a 0.220 y 0.160."
                    ),
                },
            ],
        },
        {
            "id": "dual-regime-synthesis",
            "h2_en": "V · Two Fights Against One Bath, Verified Without Shortcuts",
            "h2_es": "V · Dos Luchas Contra un Mismo Baño, Verificadas sin Atajos",
            "short_en": "V · Verification",
            "short_es": "V · Verificación",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Set the four benchmark regimes side by side and a single architectural lesson emerges. "
                        "Nature does not switch off thermal physics when an experimenter bolts on a turbomolecular "
                        "pump, nor does it grant continuum bulk diffusivity when a particle's radius approaches the "
                        "spacing of surrounding polymer strands. Every shortcut that skips a dimensionless regime "
                        "gate—Kn = λ_mfp / R for momentum transport, λ / Δx for quantum localization, or "
                        "(R + r_f) / (ξ + 2 r_f) for steric sieving—produces not a mild rounding error, but a "
                        "qualitatively false physical scaling."
                    ),
                    "es": (
                        "Al colocar los cuatro regímenes de referencia uno junto al otro emerge una misma lección "
                        "arquitectónica. La naturaleza no apaga la física térmica cuando un laboratorio instala una "
                        "bomba turbomolecular, ni concede difusividad de volumen cuando el radio de una partícula se "
                        "acerca al espaciamiento de las hebras poliméricas vecinas. Cada atajo que omite una compuerta "
                        "adimensional de régimen —Kn = λ_mfp / R en momento, λ / Δx en localización cuántica o "
                        "(R + r_f) / (ξ + 2 r_f) en tamizado estérico— produce no un redondeo menor, sino una ley "
                        "física cualitativamente falsa."
                    ),
                },
                {
                    "type": "table",
                    "caption_en": "Table ES.01 · Four Mesoscopic Regimes Governed by D_p = γ_m M k_B T",
                    "caption_es": "Tabla ES.01 · Cuatro Regímenes Mesoscópicos Gobernados por D_p = γ_m M k_B T",
                    "headers_en": [
                        "System & Bath",
                        "Kn = λ_mfp / R",
                        "Damping γ_m (s⁻¹)",
                        "Momentum Noise D_p (kg²·m²/s³)",
                        "Governing Observable",
                    ],
                    "headers_es": [
                        "Sistema y Baño",
                        "Kn = λ_mfp / R",
                        "Amortiguamiento γ_m (s⁻¹)",
                        "Ruido de Momento D_p (kg²·m²/s³)",
                        "Observable Gobernante",
                    ],
                    "rows": [
                        [
                            (
                                "QGEM diamond (R = 0.879 µm, 10⁻¹⁴ kg) in 4.0 K, 10⁻¹⁵ Pa He",
                                "Diamante QGEM (R = 0.879 µm, 10⁻¹⁴ kg) en He a 4.0 K, 10⁻¹⁵ Pa",
                            ),
                            ("2.09 × 10¹⁷ (Epstein)", "2.09 × 10¹⁷ (Epstein)"),
                            ("5.67 × 10⁻¹⁵ (specular)", "5.67 × 10⁻¹⁵ (especular)"),
                            ("3.13 × 10⁻⁵¹", "3.13 × 10⁻⁵¹"),
                            (
                                "Gas saturated Γ = 6.40 × 10⁻³ s⁻¹ (Δx⁰); photons ∝ Δx²",
                                "Gas saturado Γ = 6.40 × 10⁻³ s⁻¹ (Δx⁰); fotones ∝ Δx²",
                            ),
                        ],
                        [
                            (
                                "Levitated silica (R = 71.5 nm) at 295 K, 0.9 µPa N₂ (Magrini 2021)",
                                "Sílice levitada (R = 71.5 nm) a 295 K, N₂ a 0.9 µPa (Magrini 2021)",
                            ),
                            ("1.08 × 10¹¹ (Epstein)", "1.08 × 10¹¹ (Epstein)"),
                            ("4.30 × 10⁻⁵ (diffuse N₂)", "4.30 × 10⁻⁵ (N₂ difuso)"),
                            ("5.90 × 10⁻⁴³", "5.90 × 10⁻⁴³"),
                            (
                                "Kalman feedback cools motion to 0.56 phonons",
                                "Control de Kalman enfría movimiento a 0.56 fonones",
                            ),
                        ],
                        [
                            (
                                "Nanoparticle (R = 50 nm) in 310.15 K open hydrogel (ξ = 300 nm)",
                                "Nanopartícula (R = 50 nm) en hidrogel abierto a 310.15 K (ξ = 300 nm)",
                            ),
                            ("5.60 × 10⁻³ (Stokes)", "5.60 × 10⁻³ (Stokes)"),
                            ("1.18 × 10⁹ (no-slip)", "1.18 × 10⁹ (sin deslizamiento)"),
                            ("2.79 × 10⁻³⁰", "2.79 × 10⁻³⁰"),
                            (
                                "D_eff = 5.98 µm²/s (90.9% of D_0 = 6.58 µm²/s)",
                                "D_eff = 5.98 µm²/s (90.9% de D_0 = 6.58 µm²/s)",
                            ),
                        ],
                        [
                            (
                                "Nanoparticle (R = 50 nm) in 310.15 K dense hydrogel (ξ = 70 nm / 63 nm)",
                                "Nanopartícula (R = 50 nm) en hidrogel denso a 310.15 K (ξ = 70 nm / 63 nm)",
                            ),
                            ("5.60 × 10⁻³ (Stokes)", "5.60 × 10⁻³ (Stokes)"),
                            ("1.18 × 10⁹ (interstitial)", "1.18 × 10⁹ (intersticial)"),
                            ("2.79 × 10⁻³⁰", "2.79 × 10⁻³⁰"),
                            (
                                "D_eff = 1.44 µm²/s (22.0%) at 70 nm; 1.05 µm²/s (16.0%) at 63 nm",
                                "D_eff = 1.44 µm²/s (22.0%) a 70 nm; 1.05 µm²/s (16.0%) a 63 nm",
                            ),
                        ],
                    ],
                },
                {
                    "type": "p",
                    "en": (
                        "Toggle the planted-defect knockout in the instrument above—or run "
                        "verify_essay_mesoscopic_floor.py --planted-defect—to watch both regime errors fail "
                        "deterministically. In the cryostat, replacing single-hit saturation with naive Δx² scaling "
                        "makes a 200 µm split look 4 times noisier than 100 µm when helium collisions are invariant, "
                        "and inflates the 250 µm rate by 3.28 × 10¹¹. In the hydrogel, setting the Ogston–Amsden "
                        "exponent to 0 treats a 70 nm mucin mesh as pure water, overpredicting flux by 4.56× (and "
                        "6.27× at 63 nm). Respecting exact dimensionless boundaries is where honest modeling begins."
                    ),
                    "es": (
                        "Activa el apagado de defecto plantado en el instrumento de arriba —o ejecuta "
                        "verify_essay_mesoscopic_floor.py --planted-defect— para ver fallar de forma determinista "
                        "ambos errores de régimen. En el criostato, sustituir la saturación de impacto único por un "
                        "escalamiento ingenuo Δx² hace que 200 µm parezcan 4 veces más ruidosos que 100 µm cuando el "
                        "helio es invariante, e infla la tasa a 250 µm por 3.28 × 10¹¹. En el hidrogel, fijar en 0 el "
                        "exponente de Ogston–Amsden trata una malla de 70 nm como agua pura, sobreestimando el flujo "
                        "por 4.56× (y 6.27× en 63 nm). Respetar fronteras adimensionales exactas es donde inicia el modelado honesto."
                    ),
                },
            ],
        },
    ],
    "sidenotes": [
        {
            "label_en": "Sidenote 1 · The 8π/3 Interpolation Factor",
            "label_es": "Nota al Margen 1 · El Factor de Interpolación 8π/3",
            "en": (
                "Why do QGEM decoherence tables quote a saturated gas rate 8π/3 ≈ 8.38 times higher than the "
                "geometric collision rate n v̄ π R²? Extending the long-wavelength rate Λ_gas Δx² through the "
                "single-scale Gaussian ansatz F(Δx) = Γ_0 (1 − exp(−Δx² / λ_th²)) fixes Γ_0 = λ_th² Λ_gas = "
                "(16π√(2π)/3) P R² / √(m_g k_B T). Both rates share the exact Δx⁰ saturation plateau; our "
                "kernel carries both and checks their 8π/3 ratio to 10⁻¹²."
            ),
            "es": (
                "¿Por qué las tablas QGEM citan una tasa saturada de gas 8π/3 ≈ 8.38 veces mayor que la tasa "
                "geométrica n v̄ π R²? Extender la tasa de onda larga Λ_gas Δx² mediante el ansatz gaussiano "
                "F(Δx) = Γ_0 (1 − exp(−Δx² / λ_th²)) fija Γ_0 = λ_th² Λ_gas = (16π√(2π)/3) P R² / √(m_g k_B T). "
                "Ambas comparten la misma meseta Δx⁰; nuestro núcleo conserva las dos y verifica su razón 8π/3 a 10⁻¹²."
            ),
        },
        {
            "label_en": "Sidenote 2 · Specular vs Diffuse Epstein Drag",
            "label_es": "Nota al Margen 2 · Arrastre de Epstein Especular frente a Difuso",
            "en": (
                "Epstein's 1924 free-molecular formula multiplies specular momentum transfer by 1 + π/8 ≈ 1.393 "
                "when gas atoms thermally accommodate to the surface before desorbing diffusely. Dania et al. "
                "(2024) measured this linear-in-pressure Epstein damping across 7 decades of vacuum down to "
                "7 × 10⁻¹¹ mbar on a Paul-trapped silica nanosphere."
            ),
            "es": (
                "La fórmula molecular libre de Epstein de 1924 multiplica la transferencia especular de momento por "
                "1 + π/8 ≈ 1.393 cuando los átomos de gas se acomodan térmicamente antes de desorberse de forma "
                "difusa. Dania et al. (2024) midieron este amortiguamiento lineal en presión a lo largo de 7 décadas "
                "de vacío hasta 7 × 10⁻¹¹ mbar en una nanoesfera de sílice."
            ),
        },
        {
            "label_en": "Sidenote 3 · Diamond's Far-Infrared Uncertainty",
            "label_es": "Nota al Margen 3 · Incertidumbre Infrarroja Lejana del Diamante",
            "en": (
                "At 4.0 K, thermal photons peak near millimetre wavelengths where bulk diamond's imaginary "
                "permittivity Im ε is poorly measured; QGEM budgets assume Im ε = 10⁻⁴ with a 10× uncertainty "
                "band from 10⁻⁵ to 10⁻³. Elastic Rayleigh scattering (∝ R⁶ T⁹) depends only on Re ε = 5.7 and "
                "remains unaffected by absorption uncertainty."
            ),
            "es": (
                "A 4.0 K, los fotones térmicos alcanzan su máximo cerca de longitudes milimétricas donde la "
                "permitividad imaginaria Im ε del diamante es poco conocida; los presupuestos QGEM asumen "
                "Im ε = 10⁻⁴ con una banda de incertidumbre de 10× entre 10⁻⁵ y 10⁻³. La dispersión de Rayleigh "
                "(∝ R⁶ T⁹) solo depende de Re ε = 5.7 y no cambia con esa incertidumbre."
            ),
        },
        {
            "label_en": "Sidenote 4 · Pure Steric Bound vs Adhesive Trapping",
            "label_es": "Nota al Margen 4 · Cota Estérica Pura frente a Atrapamiento Adhesivo",
            "en": (
                "Ogston–Amsden hindrance describes an inert, non-stick sphere coated densely with neutral "
                "brush polymers such as low-molecular-weight PEG (Lai et al., 2009). Uncoated cationic or "
                "hydrophobic spheres bind polyanionic mucin fibers directly, slowing transport by 10³× to 10⁴× "
                "below pure steric sieving."
            ),
            "es": (
                "El impedimento de Ogston–Amsden describe una esfera inerte y antiadherente recubierta densamente "
                "con polímeros neutros como PEG de bajo peso molecular (Lai et al., 2009). Las esferas catiónicas "
                "o hidrofóbicas sin recubrir se enlazan a las fibras polianiónicas de mucina, frenando el transporte "
                "de 10³× a 10⁴× por debajo del tamizado estérico puro."
            ),
        },
    ],
    "sources": [
        {
            "id": "ES01-JOOS1985",
            "citation": "Joos, E., & Zeh, H. D. — The emergence of classical properties through interaction with the environment, Zeitschrift für Physik B Condensed Matter 59(2), 223–243",
            "doi": "10.1007/bf01725541",
            "year": 1985,
            "role_en": "Derives the spatial position-localization master equation for scattering environments.",
            "role_es": "Deriva la ecuación maestra de localización espacial por dispersión ambiental.",
        },
        {
            "id": "ES01-MASON1995",
            "citation": "Mason, T. G., & Weitz, D. A. — Optical measurements of frequency-dependent linear viscoelastic moduli of complex fluids, Physical Review Letters 74(7), 1250–1253",
            "doi": "10.1103/physrevlett.74.1250",
            "year": 1995,
            "role_en": "Establishes generalized Stokes–Einstein passive thermal microrheology of polymer networks.",
            "role_es": "Establece la microrreología térmica pasiva de Stokes–Einstein generalizada en redes poliméricas.",
        },
        {
            "id": "ES01-HORNBERGER2003",
            "citation": "Hornberger, K., Uttenthaler, S., Brezger, B., Hackermüller, L., Arndt, M., & Zeilinger, A. — Collisional decoherence observed in matter wave interferometry, Physical Review Letters 90(16), 160401",
            "doi": "10.1103/physrevlett.90.160401",
            "year": 2003,
            "role_en": "Demonstrates single-collision short-wavelength decoherence saturation in C₇₀ interferometry.",
            "role_es": "Demuestra la saturación de decoherencia de onda corta por colisión única en interferometría de C₇₀.",
        },
        {
            "id": "ES01-HACKERMULLER2004",
            "citation": "Hackermüller, L., Hornberger, K., Brezger, B., Zeilinger, A., & Arndt, M. — Decoherence of matter waves by thermal emission of radiation, Nature 427(6976), 711–714",
            "doi": "10.1038/nature02276",
            "year": 2004,
            "role_en": "Measures matter-wave visibility loss from internal black-body photon emission in C₇₀.",
            "role_es": "Mide la pérdida de visibilidad ondulatoria por emisión interna de fotones térmicos en C₇₀.",
        },
        {
            "id": "ES01-LAI2009",
            "citation": "Lai, S. K., Wang, Y.-Y., & Hanes, J. — Mucus-penetrating nanoparticles for drug and gene delivery to mucosal tissues, Advanced Drug Delivery Reviews 61(2), 158–171",
            "doi": "10.1016/j.addr.2008.11.002",
            "year": 2009,
            "role_en": "Quantifies steric mesh sieving versus adhesive trapping for 100 nm stealth probes in mucin hydrogels.",
            "role_es": "Cuantifica el tamizado estérico frente al atrapamiento adhesivo para sondas furtivas de 100 nm en mucina.",
        },
        {
            "id": "ES01-SEIFERT2012",
            "citation": "Seifert, U. — Stochastic thermodynamics, fluctuation theorems and molecular machines, Reports on Progress in Physics 75(12), 126001",
            "doi": "10.1088/0034-4885/75/12/126001",
            "year": 2012,
            "role_en": "Reviews exact fluctuation–dissipation identities and Langevin energetics for mesoscopic particles.",
            "role_es": "Revisa identidades exactas de fluctuación-disipación y energética de Langevin en partículas mesoscópicas.",
        },
        {
            "id": "ES01-BUTTON2012",
            "citation": "Button, B., Cai, L.-H., Ehre, C., Kesimer, M., Hill, D. B., Sheehan, J. K., Boucher, R. C., & Rubinstein, M. — A periciliary brush promotes the lung health by separating the mucus layer from airway epithelia, Science 337(6097), 937–941",
            "doi": "10.1126/science.1223012",
            "year": 2012,
            "role_en": "Measures airway hydrogel correlation mesh collapse under osmotic dehydration.",
            "role_es": "Mide el colapso del tamaño de malla del hidrogel respiratorio bajo deshidratación osmótica.",
        },
        {
            "id": "ES01-BOSE2017",
            "citation": "Bose, S., Mazumdar, A., Morley, G. W., Ulbricht, H., Toroš, M., Paternostro, M., Geraci, A. A., Barker, P. F., Kim, M. S., & Milburn, G. — Spin entanglement witness for quantum gravity, Physical Review Letters 119(24), 240401",
            "doi": "10.1103/physrevlett.119.240401",
            "year": 2017,
            "role_en": "Defines the 10⁻¹⁴ kg, Δx = 250 µm, 10⁻¹⁵ Pa falling-diamond QGEM benchmark geometry.",
            "role_es": "Define la geometría de referencia QGEM de diamante en caída de 10⁻¹⁴ kg, Δx = 250 µm y 10⁻¹⁵ Pa.",
        },
        {
            "id": "ES01-MAGRINI2021",
            "citation": "Magrini, L., Rosenzweig, P., Bach, C., Deutschmann-Olek, A., Hofer, S. G., Hong, S., Kiesel, N., Kugi, A., & Aspelmeyer, M. — Real-time optimal quantum control of mechanical motion at room temperature, Nature 595(7867), 373–377",
            "doi": "10.1038/s41586-021-03602-3",
            "year": 2021,
            "role_en": "Cools a 143 nm levitated silica nanosphere in high vacuum to 0.56 motional phonons via optimal feedback.",
            "role_es": "Enfría una nanoesfera de sílice levitada de 143 nm en alto vacío hasta 0.56 fonones mediante control óptimo.",
        },
        {
            "id": "ES01-DANIA2024",
            "citation": "Dania, L., Bykov, D. S., Goschin, M., Teller, M., Kassid, A., & Northup, T. E. — Ultrahigh quality factor of a levitated nanomechanical oscillator, Physical Review Letters 132(13), 133602",
            "doi": "10.1103/physrevlett.132.133602",
            "year": 2024,
            "role_en": "Verifies linear free-molecular Epstein gas damping down to 7 × 10⁻¹¹ mbar at quality factors above 10¹⁰.",
            "role_es": "Verifica el amortiguamiento molecular libre de Epstein lineal hasta 7 × 10⁻¹¹ mbar con factores de calidad sobre 10¹⁰.",
        },
    ],
    "skill_path": "skills/essays/mesoscopic-floor/SKILL.md",
    "verifier_path": "skills/essays/mesoscopic-floor/verify_essay_mesoscopic_floor.py",
    "ai_line_en": (
        "AI contribution to cited primary literature: none. Essay prose, bilingual es-MX twin, interactive "
        "mesoscopic regime instrument, and deterministic Python verifier were drafted with AI assistance and "
        "verified against primary DOIs and exact stdlib equations."
    ),
    "ai_line_es": (
        "Contribución de IA a la literatura primaria citada: ninguna. El texto del ensayo, su gemelo bilingüe es-MX, "
        "el instrumento mesoscópico interactivo y el verificador determinista en Python se redactaron con asistencia "
        "de IA y se verificaron contra DOIs primarios y ecuaciones exactas."
    ),
}
