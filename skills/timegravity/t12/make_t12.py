#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.12 (Two Clocks That Only Meet in Gravity).
Canonical URL: https://informatico.ai/timegravity/t12/
Writes src/timegravity/t12/files/t12_reference.json (the Planck 2018 dark-to-baryonic matter budget,
the closed-form arsinh vs. composite Gauss-Legendre quadrature proper-time shift of an electromagnetically
transparent flyby, and the ultralight scalar clock modulation bound) and manifest.json.
Standard library only; byte-for-byte reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_dark_clock import (  # noqa: E402
    B_IMPACT_DEFAULT_M,
    BASELINE_DEFAULT_M,
    DARK_CLOCK_TOL,
    M_TRANSIT_DEFAULT_KG,
    T_HALF_WINDOW_S,
    V_VIRIAL_M_S,
    check_dark_clock,
    cosmological_matter_budget,
    dark_transit_clock_shift,
    ultralight_scalar_clock_bound,
)

FILES_DIR = ROOT / "src" / "timegravity" / "t12" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def build_reference() -> dict:
    cosmo = cosmological_matter_budget()
    tr = dark_transit_clock_shift()
    bad = dark_transit_clock_shift(planted_defect=True)
    uldm0 = ultralight_scalar_clock_bound(1.0e-15, d_e=0.0)
    uldm1 = ultralight_scalar_clock_bound(1.0e-15, d_e=1.0e-4)
    chk = check_dark_clock()
    return {
        "folio_id": "T.12",
        "title": "Two Clocks That Only Meet in Gravity",
        "construction": (
            "Omega_c / Omega_b = 0.1200 / 0.02237; "
            "Delta tau(T) = -(2 G M_DM / c^2 v_0) [arsinh(v_0 T / b_1) - arsinh(v_0 T / b_2)] -> -(2 G M_DM / c^2 v_0) ln(b_2 / b_1); "
            "Phi_Pl = hbar sqrt(8 pi G rho_DM) / (m_phi c^3)"
        ),
        "parameters": {
            "transit_mass_kg": r12(M_TRANSIT_DEFAULT_KG),
            "b1_m": r12(B_IMPACT_DEFAULT_M),
            "baseline_m": r12(BASELINE_DEFAULT_M),
            "v_virial_m_s": r12(V_VIRIAL_M_S),
            "t_half_window_s": r12(T_HALF_WINDOW_S),
            "tolerance": DARK_CLOCK_TOL,
        },
        "cosmological_budget": {
            "omega_c_h2": r12(cosmo["omega_c_h2"]),
            "omega_b_h2": r12(cosmo["omega_b_h2"]),
            "dark_to_baryon_ratio": r12(cosmo["dark_to_baryon_ratio"]),
            "dark_to_baryon_ratio_err": r12(cosmo["dark_to_baryon_ratio_err"]),
            "dark_fraction_of_matter": r12(cosmo["dark_fraction_of_matter"]),
            "err_propagation_rel_diff": r12(cosmo["err_propagation_rel_diff"]),
        },
        "gravitational_transit": {
            "delta_tau_analytic_s": r12(tr["delta_tau_analytic_s"]),
            "delta_tau_quadrature_s": r12(tr["delta_tau_quadrature_s"]),
            "delta_tau_asymptotic_s": r12(tr["delta_tau_asymptotic_s"]),
            "quadrature_rel_err": r12(tr["quadrature_rel_err"]),
            "sweep_quad_max_err": r12(chk["sweep_quad_max_err"]),
            "dv_perp_m_s": r12(tr["dv_perp_m_s"]),
            "impulse_rel_err": r12(tr["impulse_rel_err"]),
            "zero_baseline_shift_s": r12(tr["zero_baseline_shift_s"]),
            "em_scattering_rate_s": r12(tr["em_scattering_rate_s"]),
            "vt_over_b1__t_s__delta_nu_over_nu": [
                [r12(p["vt_over_b1"]), r12(p["t_s"]), r12(p["delta_nu_over_nu"])]
                for p in tr["profile"]
            ],
        },
        "ultralight_scalar_bound": {
            "m_phi_ev": r12(uldm0["m_phi_ev"]),
            "compton_freq_hz": r12(uldm0["compton_freq_hz"]),
            "rho_dm_gev_cm3": r12(uldm0["rho_dm_gev_cm3"]),
            "phi_planck_dimensionless": r12(uldm0["phi_planck_dimensionless"]),
            "rho_roundtrip_rel_err": r12(uldm0["rho_roundtrip_rel_err"]),
            "pure_gravity_colocated_mod": r12(uldm0["fractional_freq_modulation"]),
            "portal_de1e4_colocated_mod": r12(uldm1["fractional_freq_modulation"]),
        },
        "planted_defect": {
            "delta_tau_analytic_s": r12(bad["delta_tau_analytic_s"]),
            "quadrature_rel_err": r12(bad["quadrature_rel_err"]),
        },
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t12_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.12",
        "generator": "skills/timegravity/t12/make_t12.py",
        "verifier": "skills/timegravity/t12/verify_t12_dark_clock.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.12 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
