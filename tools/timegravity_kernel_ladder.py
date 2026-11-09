#!/usr/bin/env python3
"""σ-ladder kernel for Time & Gravity · T.06 and T.05 (standard library only): where the Diósi–Penrose smearing may live.

One parameter, several uses. The Diósi–Penrose model smears each mass over a Gaussian of width σ (R0 in the collapse
literature). Its rungs, each with a source on the ledger:
  · the authors' own scale: Tilloy & Diósi 2016, footnote 3, "the natural cutoff σ ∼ 10⁻¹² cm" (10⁻¹⁴ m);
  · lower bounds from the radiation the model predicts: LISA Pathfinder (Helou et al. 2017) σ ≥ 40.1 fm; Gran Sasso (Donadi et al.
    2021) R0 > 0.54 Å; XENONnT 2026 R0 > 4.9 Å (90 %);
  · the one biological use, Orch-OR (Hameroff & Penrose 2014): consciousness-related collapse follows "the specific Diósi-Penrose
    scheme" — the kernel computes what Penrose's formula then says about a tubulin at each rung;
  · the entanglement letter (Trillo & Navascués 2025): entanglement in the laboratory needs σ between 50 and 250 µm;
  · this site's estimate (T.05 wedge kernel): the model's softened pull matches the Yukawa the Eöt-Wash test excludes at σ = 44 µm.

Point-mass decoherence. For a point mass m in two places Δx apart the DP decoherence rate is Γ = (G m²/ħ)[f̃(0) − f̃(Δx)] with
    f̃(z) = erf(z/2σ)/z and f̃(0) = 1/(σ√π) (the kernel of the T.05 dispute kernel). For Δx ≪ σ the two terms cancel to many
    digits, so the kernel switches to the series f̃(0) − f̃(z) = z²/(12√π σ³) − z⁴/(160√π σ⁵) + … (Trillo & Navascués Eq. 15 and
    its next term); the two branches are checked against each other where both are accurate. The lifetime is τ = 1/Γ.
    For Δx ≫ σ, Γ → G m²/(ħ σ√π): the lifetime grows as σ; for Δx ≪ σ it grows as σ³.

Casimir floor. Van De Kamp et al. 2020 screen the Casimir force between the two masses with a conducting plate of width W ≈ 1 µm
    and demand that the Casimir pull of a mass toward the plate stay below a tenth of the magnetic pull that closes the
    interferometer (their Eq. 14): x ≥ [90 ħc/(8ρπ²) · (ε−1)/(ε+2) · m/(g μ_B ∂B)]^{1/5}, with ρ the mass density, ε its dielectric
    constant, g = 2, ∂B the field gradient. The nearest separation of the two inner states is then at least 2x + W. The kernel
    evaluates this with their numbers (ρ = 3.5 g/cm³, ∂B = 10⁴ T/m, diamond ε = 5.7) and sets it beside the window the T.05
    estimate leaves the model (the critical separation d_c of the dispute kernel at σ = 44 µm for several splits).

Planted defect: the small-Δx series dropped, so the direct difference is used everywhere; at laboratory σ the cancellation
    returns garbage (negative or non-monotone lifetimes) and the verifier must reject it.
"""
from __future__ import annotations

import math

from timegravity_kernel import G_NEWTON
from timegravity_kernel_dispute import TN_D_M, TN_L_M, f_tilde, tn_critical_separation_from_e_minus, tn_survival
from timegravity_kernel_entangle import HBAR

HBAR_C = 3.1615267734966903e-26          # J·m
MU_B = 9.2740100783e-24                   # J/T
LANDE_G = 2.0
AMU = 1.66053906660e-27
TUBULIN_KG = 55000.0 * AMU                # a tubulin monomer, about 55 kDa
TUBULIN_SIZE_M = 8e-9                     # the protein's own size
NUCLEON_RADIUS_M = 2.5e-15
ORCH_OR_TAU_S = 0.025                     # the 25 ms the Orch-OR literature works with (40 Hz)
UNIVERSE_AGE_S = 13.8e9 * 365.25 * 86400.0

LADDER_RUNGS = [
    # (key, sigma_m, kind, ledger_id, en, es)
    ("natural", 1e-14, "proposed", "T05-TILLOY2016", "authors' natural cut-off", "corte natural de los autores"),
    ("lisa", 40.1e-15, "bound", "T06-HELOU2017", "LISA Pathfinder ≥ 40 fm", "LISA Pathfinder ≥ 40 fm"),
    ("gransasso", 0.54e-10, "bound", "T06-DONADI2021", "Gran Sasso > 0.54 Å", "Gran Sasso > 0.54 Å"),
    ("xenonnt", 4.9e-10, "single", "T06-XENONNT2026", "XENONnT > 4.9 Å", "XENONnT > 4.9 Å"),
    ("eotwash", 44.07e-6, "estimate", "T05-LEE2021", "T.05 estimate: Newton tests ≲ 44 µm", "estimación T.05: pruebas de Newton ≲ 44 µm"),
    ("letter_lo", 50e-6, "proposed", "T05-TRILLO2025", "2025 letter: 50 µm", "carta de 2025: 50 µm"),
    ("letter_hi", 250e-6, "proposed", "T05-TRILLO2025", "2025 letter: 250 µm", "carta de 2025: 250 µm"),
]
EW_MATCH_SIGMA_M = 44.07e-6
LADDER_TOL = 1e-6

# Van De Kamp et al. 2020 numbers
VDK_MASS_KG = 1e-15
VDK_RHO = 3500.0
VDK_EPS = 5.7
VDK_DB_T_PER_M = 1e4
VDK_PLATE_W_M = 1e-6
VDK_INNER_SEPARATION_M = 24e-6            # their N = 57 with R ≈ 0.42 µm: d − Δx = N R


def dp_point_gap(dx: float, sigma: float, planted_defect: bool = False) -> float:
    """f̃(0) − f̃(Δx) for the point-mass kernel, with the small-Δx series where the direct difference would cancel."""
    z = dx / sigma
    if z < 1e-2 and not planted_defect:
        return (dx * dx / (12.0 * math.sqrt(math.pi) * sigma ** 3)) * (1.0 - 3.0 * z * z / 40.0)
    return f_tilde(0.0, sigma) - f_tilde(dx, sigma)


def dp_point_rate(m: float, dx: float, sigma: float, planted_defect: bool = False) -> float:
    return G_NEWTON * m * m / HBAR * dp_point_gap(dx, sigma, planted_defect)


def dp_point_lifetime(m: float, dx: float, sigma: float, planted_defect: bool = False) -> float:
    r = dp_point_rate(m, dx, sigma, planted_defect)
    return 1.0 / r if r > 0 else float("inf") if r == 0 else -1.0 / abs(r)


def tubulin_table(planted_defect: bool = False) -> dict:
    """Lifetime of one tubulin in two places, and how many would have to collapse together for 25 ms, at every rung."""
    out = {}
    for key, sigma, *_ in LADDER_RUNGS:
        row = {"sigma_m": sigma}
        for dname, dx in (("protein_size", TUBULIN_SIZE_M), ("nucleon_radius", NUCLEON_RADIUS_M)):
            tau = dp_point_lifetime(TUBULIN_KG, dx, sigma, planted_defect)
            row[dname] = {"lifetime_s": tau, "tubulins_for_25ms": tau / ORCH_OR_TAU_S if tau > 0 else None,
                          "lifetime_over_universe_age": tau / UNIVERSE_AGE_S if tau > 0 else None}
        out[key] = row
    return out


def casimir_floor_gap(m: float = VDK_MASS_KG, rho: float = VDK_RHO, eps: float = VDK_EPS, db: float = VDK_DB_T_PER_M) -> float:
    """Van De Kamp et al. 2020, Eq. 14: the smallest mass-to-plate gap at which the Casimir pull stays below a tenth of the magnetic one."""
    return (90.0 * HBAR_C / (8.0 * rho * math.pi ** 2) * (eps - 1.0) / (eps + 2.0) * m / (LANDE_G * MU_B * db)) ** 0.2


def casimir_floor_separation(m: float = VDK_MASS_KG, plate_w: float = VDK_PLATE_W_M, **kw) -> float:
    """The smallest nearest separation of the two inner states: a gap on each side of the plate plus its width."""
    return 2.0 * casimir_floor_gap(m, **kw) + plate_w


def window_vs_floor(sigma: float = EW_MATCH_SIGMA_M, masses: tuple[float, ...] = (1e-15, 1e-14), splits: tuple[float, ...] = (TN_L_M, 10e-6, 5e-6, 1e-6)) -> dict:
    """For each mass: the Casimir floor and, for each split, the model's critical separation at σ; open when d_c exceeds the floor."""
    out = {"sigma_m": sigma, "by_mass": {}}
    for m in masses:
        floor = casimir_floor_separation(m)
        rows = {}
        for L in splits:
            dc = tn_critical_separation_from_e_minus(sigma, L)
            entry = {"split_m": L, "d_c_m": dc, "floor_m": floor, "open": bool(dc and dc > floor)}
            if dc and dc > floor:
                d = 0.5 * (dc + floor)      # a separation inside the open window
                entry["example_separation_m"] = d
                entry["example"] = tn_survival(L, d, m, sigma)
            rows[f"split_{L * 1e6:.0f}um"] = entry
        out["by_mass"][f"{m:.0e}"] = {"mass_kg": m, "casimir_gap_m": casimir_floor_gap(m), "floor_separation_m": floor, "splits": rows}
    return out


# ---- Oppenheim et al. 2023, Appendix F: the diffusion ceiling of the Diósi–Penrose-kernel class, with Eöt-Wash inputs
# Their Eq. F16 (as printed, the bound is on l_P² D2 in kg² s m⁻¹): l_P² D2 ≤ T σ_a² N r_N³ / G², from the variance of the
# time-averaged force on a composite mass of N atoms, dominated by the nuclear-scale self terms (Var F_total = N Var F_atom:
# the atomic forces are incoherent, and that is where the factor N comes from). Their inputs: Cavendish-type torsion balances,
# σ_a ∼ 10⁻⁷ m/s², T ∼ 10² s, N ∼ 10²⁶, r_N ∼ 10⁻¹⁵ m, printed as 10⁻⁹ kg² s m⁻¹; the interferometry floor is 10⁻⁴⁰.
OPP_CAVENDISH = {"sigma_a": 1e-7, "T_s": 1e2, "N": 1e26, "r_N_m": 1e-15, "printed_ceiling": 1e-9, "interferometry_floor": 1e-40}
# Eöt-Wash 2020 inputs (Lee et al.): a torque uncertainty of 0.0054 fN·m at s = 72 µm (the magnetic-correction uncertainty, Fig. 4),
# read as the torque residual of one averaged point; the pendulum's platinum foil, 54 µm thick, 5.5 cm across, with a quarter of
# its area removed in the hole patterns (about 2 g of platinum, 6 × 10²¹ atoms); a lever arm of 18 mm (the 120-fold pattern's mean
# radius); the averaging time of a point is not stated and is carried as an assumption, 10³ to 10⁴ s.
EW_TORQUE_RESIDUAL_NM = 0.0054e-15
EW_LEVER_M = 18e-3
EW_FOIL_MASS_KG = 21450.0 * 54e-6 * math.pi * (27.5e-3) ** 2 * 0.75
EW_N_ATOMS = EW_FOIL_MASS_KG / (195.08 * AMU)
EW_T_ASSUMED_S = (1e3, 1e4)
PT_NUCLEAR_RADIUS_M = 7e-15


def diffusion_ceiling(T: float, sigma_a: float, n_atoms: float, r_n: float) -> float:
    """l_P² D2 ≤ T σ_a² N r_N³ / G² (Oppenheim et al. 2023, Eq. F16), in kg² s m⁻¹."""
    return T * sigma_a * sigma_a * n_atoms * r_n ** 3 / (G_NEWTON * G_NEWTON)


def eotwash_sigma_a(torque_residual: float = EW_TORQUE_RESIDUAL_NM, lever: float = EW_LEVER_M, mass: float = EW_FOIL_MASS_KG) -> float:
    """Torque residual → force residual by the lever arm → acceleration of the foil: a heuristic at the same level as their Cavendish
    estimate (random forces on the atoms add in variance; a torque weights them by radius, which the single lever arm stands for)."""
    return torque_residual / lever / mass


def diffusion_table() -> dict:
    """Their inputs reproduced, then the Eöt-Wash inputs under the stated assumptions."""
    opp = diffusion_ceiling(OPP_CAVENDISH["T_s"], OPP_CAVENDISH["sigma_a"], OPP_CAVENDISH["N"], OPP_CAVENDISH["r_N_m"])
    out = {"oppenheim_inputs_ceiling": opp, "oppenheim_printed_ceiling": OPP_CAVENDISH["printed_ceiling"],
           "orders_between_recomputed_and_printed": math.log10(OPP_CAVENDISH["printed_ceiling"] / opp),
           "interferometry_floor": OPP_CAVENDISH["interferometry_floor"], "eotwash_sigma_a": eotwash_sigma_a(), "eotwash_n_atoms": EW_N_ATOMS, "eotwash": {}}
    for T in EW_T_ASSUMED_S:
        for r_n, rname in ((1e-15, "r_N_1fm"), (PT_NUCLEAR_RADIUS_M, "r_N_7fm_platinum")):
            c = diffusion_ceiling(T, eotwash_sigma_a(), EW_N_ATOMS, r_n)
            out["eotwash"][f"T_{T:.0e}_{rname}"] = {"ceiling": c, "orders_below_printed": math.log10(OPP_CAVENDISH["printed_ceiling"] / c),
                                                     "orders_above_floor": math.log10(c / OPP_CAVENDISH["interferometry_floor"])}
    return out


def check_ladder(planted_defect: bool = False) -> dict:
    # 1. The two branches of the point-mass gap agree where both are accurate (Δx/σ around 1e-2 … 3e-2).
    branch = []
    for sigma in (1e-10, 1e-6, 44e-6):
        for z in (0.01, 0.02, 0.03):
            dx = z * sigma
            series = (dx * dx / (12.0 * math.sqrt(math.pi) * sigma ** 3)) * (1.0 - 3.0 * z * z / 40.0)
            direct = f_tilde(0.0, sigma) - f_tilde(dx, sigma)
            branch.append({"sigma_m": sigma, "z": z, "series": series, "direct": direct, "rel_diff": abs(series - direct) / direct})
    branch_ok = all(b["rel_diff"] < 1e-5 for b in branch)
    # 2. Tubulin lifetimes: positive, monotone in σ, 25 ms count at the natural cut-off, and the span to the laboratory rungs.
    tub = tubulin_table(planted_defect)
    order = [k for k, *_ in LADDER_RUNGS]
    lifetimes = [tub[k]["nucleon_radius"]["lifetime_s"] for k in order]
    positive_ok = all(t > 0 for t in lifetimes) and all(tub[k]["protein_size"]["lifetime_s"] > 0 for k in order)
    monotone_ok = all(lifetimes[i] < lifetimes[i + 1] for i in range(len(lifetimes) - 1))
    n25 = tub["natural"]["nucleon_radius"]["tubulins_for_25ms"]
    count_ok = n25 is not None and 1e10 < n25 < 1e11
    span = tub["eotwash"]["nucleon_radius"]["lifetime_s"] / tub["natural"]["nucleon_radius"]["lifetime_s"] if positive_ok else None
    span_ok = span is not None and span > 1e20
    # 3. The ladder's Eöt-Wash rung is the wedge kernel's matching σ (cross-check against the live computation).
    from timegravity_kernel_wedge import wedge_sigma_matching_edge
    live = wedge_sigma_matching_edge(120)
    rung_ok = abs(live - EW_MATCH_SIGMA_M) / EW_MATCH_SIGMA_M < 1e-2
    # 4. The Casimir floor on the proposal's own condition, and the window set beside it.
    floor15 = casimir_floor_separation(1e-15)
    floor14 = casimir_floor_separation(1e-14)
    window = window_vs_floor()
    w15 = window["by_mass"]["1e-15"]["splits"]
    floor_ok = 15e-6 < floor15 < 20e-6 and floor14 > floor15 and VDK_INNER_SEPARATION_M > floor15
    window_ok = (not w15["split_23um"]["open"]) and w15["split_10um"]["open"] and w15["split_1um"]["open"] and tn_critical_separation_from_e_minus(EW_MATCH_SIGMA_M, TN_L_M) < TN_D_M
    # 4b. Oppenheim et al.'s Eq. F16 reproduced with their inputs (within two orders of their printed 1e-9) and read with Eöt-Wash inputs.
    diffusion = diffusion_table()
    diffusion_ok = (abs(diffusion["orders_between_recomputed_and_printed"]) < 2.5 and all(12.0 < v["orders_below_printed"] < 18.0 for v in diffusion["eotwash"].values())
                    and all(v["ceiling"] > diffusion["interferometry_floor"] for v in diffusion["eotwash"].values()))
    # 5. The σ³ law between the two laboratory rungs (Δx ≪ σ): τ(250 µm)/τ(44 µm) = (250/44.07)³ within 1 %.
    ratio = tub["letter_hi"]["nucleon_radius"]["lifetime_s"] / tub["eotwash"]["nucleon_radius"]["lifetime_s"]
    ratio_expected = (250e-6 / EW_MATCH_SIGMA_M) ** 3
    scaling_ok = abs(ratio / ratio_expected - 1.0) < 1e-2
    # 6. The planted defect (series dropped) returns rounding noise at the laboratory rungs: off the series by orders of magnitude
    #    and off the σ³ law; either check rejects it.
    bad = tubulin_table(planted_defect=True)
    bad_gap = dp_point_gap(NUCLEON_RADIUS_M, EW_MATCH_SIGMA_M, planted_defect=True)
    good_gap = dp_point_gap(NUCLEON_RADIUS_M, EW_MATCH_SIGMA_M)
    bad_ratio = bad["letter_hi"]["nucleon_radius"]["lifetime_s"] / bad["eotwash"]["nucleon_radius"]["lifetime_s"]
    defect_rejected = abs(bad_gap - good_gap) / good_gap > 1e-2 and abs(bad_ratio / ratio_expected - 1.0) > 1e-2
    return {
        "rungs": [{"key": k, "sigma_m": s, "kind": kind, "ledger_id": lid, "en": en, "es": es} for k, s, kind, lid, en, es in LADDER_RUNGS],
        "branch_probes": branch, "branch_ok": branch_ok, "tubulin": tub, "positive_ok": positive_ok, "monotone_ok": monotone_ok,
        "tubulins_for_25ms_at_natural_cutoff": n25, "count_ok": count_ok, "lifetime_span_eotwash_over_natural": span, "span_ok": span_ok,
        "eotwash_matching_sigma_live_m": live, "rung_ok": rung_ok,
        "casimir": {"gap_1e-15_m": casimir_floor_gap(1e-15), "floor_1e-15_m": floor15, "floor_1e-14_m": floor14, "vdk_inner_separation_m": VDK_INNER_SEPARATION_M,
                    "rho": VDK_RHO, "eps": VDK_EPS, "db_T_per_m": VDK_DB_T_PER_M, "plate_w_m": VDK_PLATE_W_M},
        "floor_ok": floor_ok, "window": window, "window_ok": window_ok,
        "sigma_cubed_ratio": ratio, "sigma_cubed_ratio_expected": ratio_expected, "scaling_ok": scaling_ok, "defect_rejected": defect_rejected,
        "diffusion": diffusion, "diffusion_ok": diffusion_ok,
        "ok": branch_ok and positive_ok and monotone_ok and count_ok and span_ok and rung_ok and floor_ok and window_ok and scaling_ok and diffusion_ok and defect_rejected,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(check_ladder(), indent=2, default=str))
