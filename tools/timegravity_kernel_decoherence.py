# -*- coding: utf-8 -*-
"""Time & Gravity · T.05 decoherence-budget kernel: the dephasing rate as residual gas and thermal photons, and the ceilings it implies.

T.05's instrument applies one local dephasing rate γ per mass: each mass's left/right coherence shrinks as e^{−γt}, so the element in
which both masses differ shrinks as e^{−2γt}. That is the convention of Schut et al. 2024 (their Eq. 23) and of Rijavec et al. 2021
(their Eq. 13, Γ per particle), and it is the decoherence function F(Δx) of the position-localization master equation
⟨x|ρ̇|x′⟩ = … − F(x − x′)⟨x|ρ|x′⟩ evaluated at the mass's own split Δx. No factor of two is hidden between the three.

This kernel replaces the assumed number with its two standard physical sources.

Residual gas. For a sphere far larger than the gas's thermal wavelength, split far wider than that wavelength, the rate saturates: it no
longer depends on the split. Two saturated rates are carried, and they differ by a stated factor:
  kinetic   n v̄ πR² = √(8π) P R²/√(m_g k_B T): the rate at which gas atoms strike the sphere (n = P/k_B T, v̄ = √(8 k_B T/π m_g)). It is
            the lowest defensible saturated rate, so the pressure ceiling it gives is the necessary condition. (Counting diffracted
            atoms too, the short-wavelength total cross-section 2πR², would double the rate; those atoms carry a momentum of order ħ/R
            and only partly resolve a split of about a diameter, so the page does not count them.)
  cited     Γ₀ = λ_th² Λ = (16π√(2π)/3) P R²/√(m_g k_B T), with λ_th = 2πħ/√(2π m_g k_B T) and Λ = 8√(2π) √(m_g k_B T) P R²/(3ħ²): the
            closed form the proposals use (Romero-Isart 2011, Phys. Rev. A 84, 052121, Eqs. 25–27; with explicit temperature in Rijavec et
            al. 2021, Table 2; again as van de Kamp et al. 2020, Eq. 33). It extends the long-wavelength Λ through the one-parameter
            ansatz F(Δx) = Γ₀(1 − e^{−Δx²/4a²}), a = λ_th/2, and exceeds the kinetic rate by exactly 8π/3 ≈ 8.4 (and 2πR² by 4π/3). Its
            ceilings are the proposals' own, stricter, working figures.

Thermal photons, in the long-wavelength limit (Romero-Isart 2011, Eqs. 28–29; Rijavec et al. 2021, Table 2), F = ΛΔx²:
  scattering   Λ = (8!·8 ζ(9) c R⁶/9π) (k_B T_e/ħc)⁹ Re[(ε−1)/(ε+2)]²
  emission     Λ = (16π⁵ c R³/189) (k_B T_i/ħc)⁶ Im[(ε−1)/(ε+2)]      (absorption: the same form at the environment's temperature)
with the same ansatz and a = λ_bb/2, λ_bb = π^{2/3} ħc/(k_B T), for the general case.

Regimes are checked before a form is used: for helium at 1–4 K the gas wavelength is under a nanometre, at most about 0.5 % of any
split of the 2024 proposal (0.17–23 µm), so the gas rate is saturated; the photon wavelength at every temperature ceiling the kernel
returns is at least ten splits, so the photon rate is ΛΔx²; the spheres are hundreds of gas wavelengths across and under 2 % of the
photon wavelength.

Diamond's far-infrared absorption is poorly known: Im ε = 10⁻⁴ (the value Rijavec et al. take; an assumed value) is carried with a decade
either side. With cold surroundings emission dominates and a temperature ceiling moves as the sixth root of the rate and of Im ε; with
surroundings as warm as the sphere, photon scattering (T⁹, independent of Im ε) joins in and that scaling no longer holds.

Transcription checks against print (they reproduce the papers' own formulas; they are not independent measurements): Bose et al. 2017,
10⁻¹⁵ Pa and 0.15 K, a collisional decoherence time 'the same order of magnitude' as the fall time (about 3.5 s): the cited form gives
2.8 s for helium (the kinetic rate 23 s). Rijavec et al. 2021 (R = 1 µm, Δx = 250 µm, helium, T_i = T): 1/τ_G ≃ 0.06 s⁻¹; 'temperatures
lower than 4 K': the photon forms reach 1/τ_G at 3.5 K, about a factor of two in rate stricter than the printed figure; 'pressures lower
than 10⁻¹⁶ Pa': the cited gas rate there is an order below 1/τ_G. van de Kamp et al. 2020: Eq. 33 equals the cited form through the
ideal-gas law; n_V ~ 10⁷ m⁻³ at 5 × 10⁻¹⁶ Pa is 3.6 K, their 'O(1) K'. Schut et al. 2024 state a rate (γ ~ 10⁻² Hz 'for the ambient
temperatures of ~1 K') and no pressure; the kernel reports the pressure that rate implies.

What it does not cover: hydrogen and other species beside helium (each adds to the rate; hydrogen dephases about 1.4 times faster per
pascal), dipole and Casimir–Polder couplings, gravity-gradient and acceleration noise, phonons, the trap and the spin control, and any
time dependence of the split. Each ceiling lets one source use the whole threshold; together the sources must share it. Nothing here
pronounces on feasibility. Planted defect: the gas rate left in its long-wavelength form ΛΔx² outside its regime.

Stdlib only.
"""
from __future__ import annotations

import math

from timegravity_kernel_dispute import (DIAMOND_DENSITY, HBAR, PROPOSALS, SIGMA_ESTIMATE_M, branches_parallel, dephasing_threshold_points,
                                        hybrid_state_points, quantum_state_points, rijavec_tau_g, sphere_radius)

K_B = 1.380649e-23               # J/K (exact, SI 2019)
C_LIGHT = 299792458.0            # m/s (exact)
ATOMIC_MASS_UNIT_KG = 1.66053906660e-27
HELIUM_MASS_KG = 4.002602 * ATOMIC_MASS_UNIT_KG   # 6.65e-27 kg; Rijavec et al. 2021 take 6.6e-27 kg ('a atom of helium')
HYDROGEN_MASS_KG = 2.01588 * ATOMIC_MASS_UNIT_KG  # the H₂ molecule
AIR_MASS_KG = 28.97 * ATOMIC_MASS_UNIT_KG         # Romero-Isart 2011, Table 3
ZETA_9 = 1.0020083928260822
DIAMOND_EPS = complex(5.7, 1e-4)                  # Rijavec et al. 2021, Table 2 caption
DIAMOND_EPS_IM_RANGE = (1e-5, 1e-3)               # a decade either side: the far-infrared absorption is poorly known
# Sellner et al. (BASE) 2017, New J. Phys. 19, 083023: partial-pressure upper limits inferred from antiproton storage, 68 % C.L.
BASE_PARTIAL_PRESSURE_PA = {"hydrogen": 1.2e-16, "helium": 2.7e-16}   # 1.2e-18 and 2.7e-18 mbar; that trap, at its own temperature
BUDGET_GEOMETRIES = ("schut2024_z10", "schut2024_z5", "schut2024_z10_1e-15", "schut2024_z10_1e-13")
GAS_TEMPERATURES_K = (1.0, 4.0)
GAS_COEFF = {"kinetic": math.sqrt(8.0 * math.pi),                          # n v̄ πR²
             "cited": 16.0 * math.pi * math.sqrt(2.0 * math.pi) / 3.0}     # λ_th² Λ, the proposals' form


def gas_thermal_wavelength(m_gas: float, temp: float) -> float:
    return 2.0 * math.pi * HBAR / math.sqrt(2.0 * math.pi * m_gas * K_B * temp)


def photon_thermal_wavelength(temp: float) -> float:
    return math.pi ** (2.0 / 3.0) * HBAR * C_LIGHT / (K_B * temp)


def gas_localization(pressure: float, temp: float, radius: float, m_gas: float = HELIUM_MASS_KG) -> float:
    """Λ of residual gas in the long-wavelength limit, 1/(m² s)."""
    return 8.0 * math.sqrt(2.0 * math.pi) * math.sqrt(m_gas * K_B * temp) * pressure * radius ** 2 / (3.0 * HBAR ** 2)


def gas_rate_saturated(pressure: float, temp: float, radius: float, m_gas: float = HELIUM_MASS_KG, form: str = "kinetic") -> float:
    """The saturated gas rate, 1/s: 'kinetic' (atoms striking the sphere) or 'cited' (the proposals' interpolation λ_th² Λ)."""
    return GAS_COEFF[form] * pressure * radius ** 2 / math.sqrt(m_gas * K_B * temp)


def _ansatz(gamma0: float, a: float, dx: float) -> float:
    x = dx * dx / (4.0 * a * a)
    return gamma0 * (-math.expm1(-x))


def gas_rate(dx: float, pressure: float, temp: float, radius: float, m_gas: float = HELIUM_MASS_KG, form: str = "kinetic",
             planted_defect: bool = False) -> float:
    """F(Δx) for residual gas. Planted defect: the long-wavelength form ΛΔx² used whatever the regime."""
    if planted_defect:
        return gas_localization(pressure, temp, radius, m_gas) * dx * dx
    return _ansatz(gas_rate_saturated(pressure, temp, radius, m_gas, form), gas_thermal_wavelength(m_gas, temp) / 2.0, dx)


def clausius_mossotti(eps: complex) -> complex:
    return (eps - 1.0) / (eps + 2.0)


def photon_lambda_scattering(radius: float, temp_env: float, eps: complex = DIAMOND_EPS) -> float:
    return (40320.0 * 8.0 * ZETA_9 * C_LIGHT * radius ** 6 / (9.0 * math.pi)) * (K_B * temp_env / (HBAR * C_LIGHT)) ** 9 * clausius_mossotti(eps).real ** 2


def photon_lambda_emission(radius: float, temp: float, eps: complex = DIAMOND_EPS) -> float:
    """Emission at the internal temperature; the same form at the environment's temperature is absorption."""
    return (16.0 * math.pi ** 5 * C_LIGHT * radius ** 3 / 189.0) * (K_B * temp / (HBAR * C_LIGHT)) ** 6 * clausius_mossotti(eps).imag


def photon_rate(dx: float, radius: float, temp_int: float, temp_env: float, eps: complex = DIAMOND_EPS) -> dict:
    """F(Δx) for thermal photons: scattering and absorption at the environment's temperature, emission at the internal one."""
    out = {}
    for name, lam, temp in (("scattering", photon_lambda_scattering(radius, temp_env, eps), temp_env),
                            ("absorption", photon_lambda_emission(radius, temp_env, eps), temp_env),
                            ("emission", photon_lambda_emission(radius, temp_int, eps), temp_int)):
        a = photon_thermal_wavelength(temp) / 2.0
        out[name] = _ansatz(4.0 * a * a * lam, a, dx)
    out["total"] = out["scattering"] + out["absorption"] + out["emission"]
    return out


def pressure_ceiling(rate: float, dx: float, temp: float, radius: float, m_gas: float = HELIUM_MASS_KG, form: str = "kinetic",
                     planted_defect: bool = False) -> float:
    """The pressure at which the gas alone dephases at `rate` (the rate is linear in pressure)."""
    return rate / gas_rate(dx, 1.0, temp, radius, m_gas, form, planted_defect)


def temperature_ceiling(rate: float, dx: float, radius: float, eps: complex = DIAMOND_EPS, temp_env: float | None = None) -> float:
    """The internal temperature at which thermal photons alone dephase at `rate`: environment held at temp_env, or as warm as the
    sphere (temp_env None, the simplification of Rijavec et al.). Bisection; the rate rises monotonically with temperature."""
    def total(t: float) -> float:
        return photon_rate(dx, radius, t, t if temp_env is None else temp_env, eps)["total"]
    lo, hi = 1e-3, 1e4
    if total(lo) > rate:
        return 0.0
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if total(mid) > rate:
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


def thresholds(key: str, sigmas: tuple = (SIGMA_ESTIMATE_M, 20e-6)) -> dict:
    """The dephasing rates above which each channel shows no entanglement at any time (dispute kernel), for one published geometry."""
    _, layout, m, split, gap = next(p for p in PROPOSALS if p[0] == key)
    if layout != "parallel":
        raise ValueError("the budget is computed for the 2024 side-by-side geometries")
    br = branches_parallel(split, gap)
    return {"key": key, "m_kg": m, "split_m": split, "gap_m": gap, "radius_m": sphere_radius(m, DIAMOND_DENSITY),
            "quantum_per_s": dephasing_threshold_points(quantum_state_points, br, m),
            "hybrid_per_s": {f"{s * 1e6:.0f}um": dephasing_threshold_points(hybrid_state_points, br, m, s) for s in sigmas}}


def budget(key: str, planted_defect: bool = False) -> dict:
    """One geometry: thresholds, regime checks, and the pressure and internal-temperature ceilings each threshold implies."""
    th = thresholds(key)
    dx, radius = th["split_m"], th["radius_m"]
    rates = {"quantum": th["quantum_per_s"], **{f"hybrid_{k}": v for k, v in th["hybrid_per_s"].items()}}
    out = {**th, "rates_per_s": rates, "pressure_ceiling_pa": {}, "number_density_ceiling_per_m3": {}, "temperature_ceiling_k": {}, "regime": {}}
    for name, rate in rates.items():
        out["pressure_ceiling_pa"][name] = {
            f"{t:g}K": {form: pressure_ceiling(rate, dx, t, radius, form=form, planted_defect=planted_defect) for form in GAS_COEFF}
            for t in GAS_TEMPERATURES_K}
        out["number_density_ceiling_per_m3"][name] = {   # the kinetic ceiling as atoms per cubic metre, n = P/k_B T
            f"{t:g}K": out["pressure_ceiling_pa"][name][f"{t:g}K"]["kinetic"] / (K_B * t) for t in GAS_TEMPERATURES_K}
        out["temperature_ceiling_k"][name] = {
            "env_1K": temperature_ceiling(rate, dx, radius, temp_env=1.0),   # the 2024 proposal's ambient; emission dominates
            "env_1K_im_low": temperature_ceiling(rate, dx, radius, complex(DIAMOND_EPS.real, DIAMOND_EPS_IM_RANGE[0]), temp_env=1.0),
            "env_1K_im_high": temperature_ceiling(rate, dx, radius, complex(DIAMOND_EPS.real, DIAMOND_EPS_IM_RANGE[1]), temp_env=1.0),
            "env_equal": temperature_ceiling(rate, dx, radius)}   # environment as warm as the sphere: photon scattering (T⁹) joins in
    t_hot = max(v["env_1K_im_low"] for v in out["temperature_ceiling_k"].values())
    lam_gas = max(gas_thermal_wavelength(HELIUM_MASS_KG, t) for t in GAS_TEMPERATURES_K)
    out["regime"] = {
        "gas_wavelength_over_split": lam_gas / dx,
        "photon_wavelength_over_split": photon_thermal_wavelength(t_hot) / dx,
        "radius_over_gas_wavelength": radius / lam_gas,
        "radius_over_photon_wavelength": radius / photon_thermal_wavelength(t_hot),
        "gas_rate_over_saturated": gas_rate(dx, 1.0, 4.0, radius, planted_defect=planted_defect) / gas_rate_saturated(1.0, 4.0, radius)}
    return out


def transcription_checks(planted_defect: bool = False) -> dict:
    """The kernel's forms against what four papers print. These reproduce the papers' own formulas; they validate no physics."""
    # Bose et al. 2017: 10⁻¹⁵ Pa, 0.15 K, r ~ 1 µm, Δx ~ 250 µm; 'the same order of magnitude' as the fall time (about 3.5 s).
    bose = {form: 1.0 / gas_rate(250e-6, 1e-15, 0.15, 1e-6, HELIUM_MASS_KG, form, planted_defect) for form in GAS_COEFF}
    bose_air = 1.0 / gas_rate(250e-6, 1e-15, 0.15, 1e-6, AIR_MASS_KG, "cited", planted_defect)
    # Rijavec et al. 2021: m = 10⁻¹⁴ kg, R = 10⁻⁶ m, d = 450 µm, Δx = 250 µm, helium, T_i = T, ε = 5.7 + i 10⁻⁴.
    inv_tau_g = 1.0 / rijavec_tau_g()
    rij_gas = gas_rate(250e-6, 1e-16, 4.0, 1e-6, form="cited", planted_defect=planted_defect)
    rij_t = temperature_ceiling(inv_tau_g, 250e-6, 1e-6)
    rij_4k = photon_rate(250e-6, 1e-6, 4.0, 4.0)["total"]
    rij_1k = gas_rate(250e-6, 1e-16, 1.0, 1e-6, form="cited", planted_defect=planted_defect) + photon_rate(250e-6, 1e-6, 1.0, 1.0)["total"]
    # van de Kamp et al. 2020, Eq. 33: Γ = (16π n_V R²/3) √(2π k_B T/m), n_V ~ 10⁷ m⁻³, P ~ 5 × 10⁻¹⁶ Pa, T_ex ~ O(1) K, R ~ 100 nm.
    n_v, p_vdk, r_vdk = 1e7, 5e-16, 100e-9
    t_vdk = p_vdk / (n_v * K_B)
    eq33 = (16.0 * math.pi * n_v * r_vdk ** 2 / 3.0) * math.sqrt(2.0 * math.pi * K_B * t_vdk / HELIUM_MASS_KG)
    # Schut et al. 2024 state γ ~ 10⁻² Hz 'for the ambient temperatures of ~1 K' (10⁻¹⁴ kg diamond) and no pressure: the implied pressure.
    r14 = sphere_radius(1e-14, DIAMOND_DENSITY)
    return {"bose2017_decoherence_time_s": {"helium_cited": bose["cited"], "helium_kinetic": bose["kinetic"], "air_cited": bose_air, "fall_time_s": 3.5},
            "rijavec2021": {"inv_tau_g_per_s": inv_tau_g, "gas_rate_cited_at_1e-16Pa_4K_per_s": rij_gas, "photon_temperature_at_inv_tau_g_k": rij_t,
                            "photon_rate_at_4K_over_inv_tau_g": rij_4k / inv_tau_g, "total_rate_at_1K_1e-16Pa_per_s": rij_1k},
            "vandekamp2020": {"temperature_from_n_and_p_k": t_vdk, "eq33_per_s": eq33,
                              "eq33_over_cited": eq33 / gas_rate_saturated(p_vdk, t_vdk, r_vdk, form="cited")},
            "schut2024_implied_pressure_for_1e-2Hz_at_1K_pa": {form: 1e-2 / gas_rate_saturated(1.0, 1.0, r14, form=form) for form in GAS_COEFF}}


def check_decoherence(planted_defect: bool = False) -> dict:
    """The verifier's gate."""
    budgets = {k: budget(k, planted_defect) for k in BUDGET_GEOMETRIES}
    tc = transcription_checks(planted_defect)
    z10 = budgets["schut2024_z10"]
    # identities and regimes
    r, t = 1e-6, 4.0
    a = gas_thermal_wavelength(HELIUM_MASS_KG, t) / 2.0
    identity_ok = (abs(gas_rate_saturated(1e-15, t, r, form="cited") / (4.0 * a * a * gas_localization(1e-15, t, r)) - 1.0) < 1e-12
                   and abs(GAS_COEFF["cited"] / GAS_COEFF["kinetic"] / (8.0 * math.pi / 3.0) - 1.0) < 1e-12
                   and abs(tc["vandekamp2020"]["eq33_over_cited"] - 1.0) < 1e-12)
    regime_ok = all(b["regime"]["gas_wavelength_over_split"] < 0.01 and b["regime"]["photon_wavelength_over_split"] > 10.0
                    and b["regime"]["radius_over_gas_wavelength"] > 100.0 and b["regime"]["radius_over_photon_wavelength"] < 0.05
                    and abs(b["regime"]["gas_rate_over_saturated"] - 1.0) < 1e-9 for b in budgets.values())
    # transcription checks, with windows no wider than the printed statements allow
    bose = tc["bose2017_decoherence_time_s"]
    rij = tc["rijavec2021"]
    transcription_ok = (3.5 / 2.0 < bose["helium_cited"] < 3.5 * 2.0                    # 'same order of magnitude' as the 3.5 s fall
                        and abs(bose["helium_kinetic"] / bose["helium_cited"] / (8.0 * math.pi / 3.0) - 1.0) < 1e-9
                        and 0.055 < rij["inv_tau_g_per_s"] < 0.065
                        and rij["gas_rate_cited_at_1e-16Pa_4K_per_s"] < 0.2 * rij["inv_tau_g_per_s"]   # 'pressures lower than 10⁻¹⁶ Pa'
                        and 3.0 < rij["photon_temperature_at_inv_tau_g_k"] < 4.0               # 'temperatures lower than 4 K'
                        and 1.5 < rij["photon_rate_at_4K_over_inv_tau_g"] < 3.0                # the kernel is stricter by about two in rate
                        and rij["total_rate_at_1K_1e-16Pa_per_s"] < rij["inv_tau_g_per_s"]      # '1 K and 10⁻¹⁶ Pa are sufficient'
                        and 1.0 < tc["vandekamp2020"]["temperature_from_n_and_p_k"] < 10.0)   # 'O(1) K'
    # ceilings
    pq = z10["pressure_ceiling_pa"]["quantum"]["4K"]
    ph = z10["pressure_ceiling_pa"]["hybrid_33um"]["4K"]
    tq = z10["temperature_ceiling_k"]["quantum"]
    thy = z10["temperature_ceiling_k"]["hybrid_33um"]
    rate_ratio = z10["rates_per_s"]["quantum"] / z10["rates_per_s"]["hybrid_33um"]
    he = BASE_PARTIAL_PRESSURE_PA["helium"]
    vac = {"helium_limit_over_quantum_kinetic": he / pq["kinetic"], "helium_limit_over_quantum_cited": he / pq["cited"],
           "helium_limit_over_hybrid_kinetic": he / ph["kinetic"], "helium_limit_over_hybrid_cited": he / ph["cited"]}
    ceilings_ok = (1.4e-15 < pq["kinetic"] < 1.7e-15 and 1.7e-16 < pq["cited"] < 2.0e-16
                   and 1.1e-17 < ph["kinetic"] < 1.4e-17 and 1.3e-18 < ph["cited"] < 1.6e-18
                   and abs(pq["kinetic"] / ph["kinetic"] / rate_ratio - 1.0) < 1e-9       # pressure falls by the full ratio
                   and 100.0 < rate_ratio < 150.0
                   and 2.5e7 < z10["number_density_ceiling_per_m3"]["quantum"]["4K"] < 3.1e7
                   and 2.0e5 < z10["number_density_ceiling_per_m3"]["hybrid_33um"]["4K"] < 2.5e5
                   and 6.0 < thy["env_1K"] < 9.0 and 14.0 < tq["env_1K"] < 18.0 and thy["env_equal"] < thy["env_1K"] and tq["env_equal"] < tq["env_1K"]
                   and abs(tq["env_1K"] / thy["env_1K"] / rate_ratio ** (1.0 / 6.0) - 1.0) < 0.03   # by its sixth root, cold surroundings
                   and abs(thy["env_1K_im_low"] / thy["env_1K"] / 10.0 ** (1.0 / 6.0) - 1.0) < 0.03
                   and abs(thy["env_1K"] / thy["env_1K_im_high"] / 10.0 ** (1.0 / 6.0) - 1.0) < 0.03
                   and tq["env_equal"] / thy["env_equal"] < 0.95 * rate_ratio ** (1.0 / 6.0)        # warm surroundings: no longer the sixth root
                   and 0.15 < vac["helium_limit_over_quantum_kinetic"] < 0.21 and 1.3 < vac["helium_limit_over_quantum_cited"] < 1.7
                   and 18.0 < vac["helium_limit_over_hybrid_kinetic"] < 27.0 and 150.0 < vac["helium_limit_over_hybrid_cited"] < 220.0)
    # the estimate handed in for testing: 10⁻¹⁴ kg, helium at 4 K, on the kinetic rate
    r14 = sphere_radius(1e-14, DIAMOND_DENSITY)
    est = {"p_for_1e-4_per_s_pa": 1e-4 / gas_rate_saturated(1.0, 4.0, r14), "p_for_quantum_pa": z10["rates_per_s"]["quantum"] / gas_rate_saturated(1.0, 4.0, r14)}
    estimate_ok = abs(est["p_for_1e-4_per_s_pa"] / 1.6e-17 - 1.0) < 0.05 and abs(est["p_for_quantum_pa"] / 1.6e-15 - 1.0) < 0.06
    # hydrogen beside helium at the same pressure and temperature: the kinetic rate goes as 1/√m
    h2 = gas_rate_saturated(1.0, 4.0, r14, m_gas=HYDROGEN_MASS_KG) / gas_rate_saturated(1.0, 4.0, r14)
    identity_ok = bool(identity_ok and abs(h2 / math.sqrt(HELIUM_MASS_KG / HYDROGEN_MASS_KG) - 1.0) < 1e-12 and 1.40 < h2 < 1.42)
    ok = bool(identity_ok and regime_ok and transcription_ok and ceilings_ok and estimate_ok)
    return {"budgets": budgets, "transcription_checks": tc, "estimate": est, "base_partial_pressure_pa": BASE_PARTIAL_PRESSURE_PA,
            "rate_ratio_quantum_over_hybrid_33um": rate_ratio, "vacuum_comparison_helium": vac, "hydrogen_over_helium_rate_at_equal_pressure": h2,
            "gas_rate_per_pa_at_4K_1e-14kg_per_s": {form: gas_rate_saturated(1.0, 4.0, r14, form=form) for form in GAS_COEFF},
            "identity_ok": identity_ok, "regime_ok": regime_ok, "transcription_ok": transcription_ok, "ceilings_ok": ceilings_ok,
            "estimate_ok": estimate_ok, "ok": ok}


if __name__ == "__main__":
    import json
    import sys
    print(json.dumps(check_decoherence("--planted-defect" in sys.argv), indent=2, default=str))
