#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.11 (What Selects the World a Clock Sees?).
Canonical URL: https://informatico.ai/timegravity/t11/
Writes src/research/timegravity/t11/files/t11_reference.json (the 1+6 qubit pure-dephasing Quantum Darwinism
statevector partial-trace mutual-information curve I(S : E_k) against Zurek's closed-form binary entropy formula,
and the Joos-Zeh / Romero-Isart thermal photon scattering localization table) and manifest.json.
Standard library only; byte-for-byte reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_einselection import (  # noqa: E402
    EINSELECTION_TOL,
    N_ENV_DEFAULT,
    THETA_DEFAULT,
    check_einselection,
    photon_bath_localization_table,
    statevector_quantum_darwinism,
)

FILES_DIR = ROOT / "src" / "research" / "timegravity" / "t11" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def build_reference() -> dict:
    qd = statevector_quantum_darwinism(THETA_DEFAULT, N_ENV_DEFAULT, planted_defect=False)
    bad = statevector_quantum_darwinism(THETA_DEFAULT, N_ENV_DEFAULT, planted_defect=True)
    phot = photon_bath_localization_table(10e-6)
    chk = check_einselection()
    return {
        "folio_id": "T.11",
        "title": "What Selects the World a Clock Sees?",
        "construction": (
            "|Psi_SE> = (|0>_S x |0>^{x N} + |1>_S x (cos theta |0> + sin theta |1>)^{x N}) / sqrt(2); "
            "I(S : E_k) = h_2(gamma^N) + h_2(gamma^k) - h_2(gamma^{N-k}), gamma = |cos theta|; "
            "Lambda_sc = (8! 8 zeta(9) c R^6 / 9 pi) (k_B T_e / hbar c)^9 Re[(eps-1)/(eps+2)]^2"
        ),
        "parameters": {
            "n_env_modes": N_ENV_DEFAULT,
            "statevector_dim": qd["statevector_dim"],
            "theta_rad": r12(THETA_DEFAULT),
            "gamma_overlap": r12(qd["gamma"]),
            "tolerance": EINSELECTION_TOL,
        },
        "coherence_ratio_n6": r12(qd["coherence_ratio_statevector"]),
        "coherence_ratio_abs_dev": r12(qd["coherence_ratio_abs_dev"]),
        "s_system_nats": r12(qd["s_system_jacobi_nats"]),
        "max_mi_dev_nats": r12(qd["max_mi_dev_nats"]),
        "sweep_max_mi_dev_nats": r12(chk["sweep_max_mi_dev_nats"]),
        "midpoint_identity_err": r12(qd["midpoint_identity_err"]),
        "full_bath_identity_err": r12(qd["full_bath_identity_err"]),
        "k2_plateau_bits": r12(qd["k2_plateau_bits"]),
        "k__f__i_jacobi_nats__i_analytic_nats__i_bits": [
            [
                row["k"],
                r12(row["fraction_f"]),
                r12(row["i_s_ek_jacobi_nats"]),
                r12(row["i_s_ek_analytic_nats"]),
                r12(row["i_s_ek_jacobi_bits"]),
            ]
            for row in qd["fragments"]
        ],
        "photon_bath_localization": {
            "dx_m": r12(phot["dx_m"]),
            "t_cmb_k": r12(phot["t_cmb_k"]),
            "t_room_k": r12(phot["t_room_k"]),
            "dust_10um_tau_cmb_s": r12(phot["dust_10um_dielectric"]["tau_cmb_s"]),
            "dust_10um_tau_300k_s": r12(phot["dust_10um_dielectric"]["tau_300k_s"]),
            "dust_10um_conductor_lambda_cmb_cm2_s": r12(phot["dust_10um_conductor_cmb"]["lambda_cmb_cm2_s"]),
            "qgem_1um_tau_cmb_s": r12(phot["qgem_1um_dielectric"]["tau_cmb_s"]),
            "qgem_1um_tau_300k_s": r12(phot["qgem_1um_dielectric"]["tau_300k_s"]),
            "dark_sector_lambda_300k_m2_s": r12(phot["dark_sector_eps1"]["lambda_300k_m2_s"]),
            "r6_scaling_rel_err": r12(phot["r6_scaling_rel_err"]),
            "t9_scaling_rel_err": r12(phot["t9_scaling_rel_err"]),
        },
        "planted_defect": {
            "k2_plateau_bits": r12(bad["k2_plateau_bits"]),
            "coherence_ratio": r12(bad["coherence_ratio_statevector"]),
        },
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t11_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.11",
        "generator": "skills/timegravity/t11/make_t11.py",
        "verifier": "skills/timegravity/t11/verify_t11_einselection.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.11 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
