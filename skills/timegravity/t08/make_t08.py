#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.08 (A Horizon Has a Temperature).
Canonical URL: https://informatico.ai/timegravity/t08/
Writes src/timegravity/t08/files/t08_reference.json (the two-mode Rindler thermofield double's reduced
density matrix eigenvalues against the Planck and truncated-Gibbs weights, the Hawking-Bekenstein first-law
quadrature check, and the Rindler proper-time redshift table) and manifest.json.
Standard library only; byte-for-byte reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_horizon import (  # noqa: E402
    FOCK_D,
    HORIZON_TOL,
    M_SUN,
    XI_DEFAULT,
    check_horizon,
    first_law_area_check,
    rindler_worldline,
    schwarzschild_thermodynamics,
    two_mode_squeezed_wedge,
)

FILES_DIR = ROOT / "src" / "timegravity" / "t08" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def build_reference() -> dict:
    tfd = two_mode_squeezed_wedge(XI_DEFAULT, FOCK_D)
    rw = rindler_worldline(1.0e20)
    bh_solar = schwarzschild_thermodynamics(M_SUN)
    fl = first_law_area_check(M_SUN)
    chk = check_horizon()
    bad = two_mode_squeezed_wedge(XI_DEFAULT, FOCK_D, planted_defect=True)
    return {
        "folio_id": "T.08",
        "title": "A Horizon Has a Temperature",
        "construction": (
            "|0_M> = Z_d(xi)^{-1/2} sum_{n=0}^{d-1} exp(-n xi / 2) |n>_L x |n>_R (normalized on d levels); "
            "rho_R = Tr_L |0_M><0_M|; T_U = hbar a / (2 pi k_B c); T_H = hbar c^3 / (8 pi G M k_B); S_BH = k_B c^3 A / (4 G hbar)"
        ),
        "parameters": {
            "fock_cutoff_d": FOCK_D,
            "default_xi": XI_DEFAULT,
            "truncation_tail": r12(tfd["truncation_tail"]),
            "tolerance": HORIZON_TOL,
        },
        "max_dev_from_planck": r12(tfd["max_dev_from_planck"]),
        "max_dev_from_truncated_gibbs": r12(tfd["max_dev_from_truncated_gibbs"]),
        "sweep_truncated_gibbs_max_dev": r12(chk["sweep_truncated_gibbs_max_dev"]),
        "entropy_nats": r12(tfd["entropy_jacobi_nats"]),
        "planck_entropy_nats": r12(tfd["entropy_planck_nats"]),
        "entropy_dev_from_planck": r12(tfd["entropy_dev_from_planck"]),
        "n_bar": r12(tfd["n_bar_jacobi"]),
        "n_bar_planck": r12(tfd["n_bar_planck"]),
        "fock_n__p_jacobi__p_gibbs__p_planck": [
            [n, r12(tfd["eigenvalues"][n]), r12(tfd["gibbs_truncated"][n]), r12(tfd["planck_probabilities"][n])]
            for n in range(FOCK_D)
        ],
        "rindler_redshift": {
            "accel_m_s2": r12(rw["accel_m_s2"]),
            "horizon_distance_x0_m": r12(rw["horizon_distance_x0_m"]),
            "unruh_temp_k": r12(rw["unruh_temp_k"]),
            "max_hyperbola_invariant_err": r12(rw["max_hyperbola_invariant_err"]),
            "max_four_velocity_norm_err": r12(rw["max_four_velocity_norm_err"]),
        },
        "hawking_bekenstein": {
            "quadrature_vs_area_quarter_rel_err": r12(fl["quadrature_vs_area_quarter_rel_err"]),
            "bch_first_law_rel_err": r12(fl["bch_first_law_rel_err"]),
            "solar_mass_row": {
                "m_over_msun": r12(bh_solar["mass_solar"]),
                "r_s_m": r12(bh_solar["r_s_m"]),
                "kappa_m_s2": r12(bh_solar["kappa_m_s2"]),
                "hawking_temp_k": r12(bh_solar["t_hawking_k"]),
                "s_bh_over_kb": r12(bh_solar["s_bh_over_kb"]),
                "t_cmb_over_t_hawking": r12(bh_solar["t_cmb_over_t_hawking"]),
            },
        },
        "planted_defect": {
            "entropy_nats": r12(bad["entropy_jacobi_nats"]),
            "max_dev_from_planck": r12(bad["max_dev_from_planck"]),
        },
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t08_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.08",
        "generator": "skills/timegravity/t08/make_t08.py",
        "verifier": "skills/timegravity/t08/verify_t08_horizon_thermodynamics.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.08 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
