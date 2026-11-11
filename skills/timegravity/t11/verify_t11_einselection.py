#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.11 (What Selects the World a Clock Sees?).
Canonical URL: https://informatico.ai/timegravity/t11/
Central number: for a system qubit S coupled via a pointer-commuting interaction [H_int, sigma_z] = 0 to N = 6
environment modes (statevector dimension 2^7 = 128), the Jacobi-diagonalised partial-trace mutual information
I(S : E_k) matches Zurek's closed-form binary entropy curve h_2(gamma^N) + h_2(gamma^k) - h_2(gamma^{N-k}) within
1e-12 across all k in {0 .. 6} and all scattering angles theta, reaching 0.9983 bits of classical redundancy by
k = 2 modes at theta = 1.35 rad while satisfying the exact midpoint identity I(S : E_{N/2}) = S(rho_S); for
Joos & Zeh's R = 10 um dust grain at dx = 10 um, dipole photon scattering gives tau_CMB = 1.634 s vs tau_300K =
6.888e-19 s (and 0 for an electromagnetically uncoupled sector eps = 1). Planted defect: setting theta = 0
(no pointer-commuting bath imprinting) collapses the redundancy plateau to zero; `--planted-defect` exits non-zero.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_einselection import EINSELECTION_TOL, check_einselection  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t11" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t11_reference.json").read_text(encoding="utf-8"))
    assert ref["max_mi_dev_nats"] < EINSELECTION_TOL, "reference statevector I(S:E_k) misses closed-form Zurek formula"
    assert ref["k2_plateau_bits"] > 0.90, "reference Quantum Darwinism plateau missing at k = 2"
    assert ref["photon_bath_localization"]["r6_scaling_rel_err"] < EINSELECTION_TOL, "reference R^6 Rayleigh scaling error"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_einselection(planted_defect=planted)
        assert res["statevector_ok"], (
            f"1+6 qubit statevector partial trace misses closed-form I(S:E_k) by {res['max_mi_dev_nats']:.3e} (> {EINSELECTION_TOL:g})"
        )
        assert res["plateau_ok"], (
            f"pointer redundancy plateau collapsed (k=2 mutual information = {res['k2_plateau_bits']:.4f} bits, "
            f"coherence ratio = {res['coherence_ratio_n6']:.4f}); without pointer-commuting scattering no classical record forms"
        )
        assert res["photon_scaling_ok"], f"Joos-Zeh photon scattering scaling error {res['r6_scaling_rel_err']:.3e}"
        assert res["defect_rejected"], "planted zero-imprinting state was accepted as having a redundancy plateau"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.11", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.11",
        "canonical_url": "https://informatico.ai/timegravity/t11/",
        "central_number": {
            "max_mi_dev_nats": res["max_mi_dev_nats"],
            "k2_plateau_bits": res["k2_plateau_bits"],
            "coherence_ratio_n6": res["coherence_ratio_n6"],
            "dust_10um_tau_cmb_s": res["dust_10um_tau_cmb_s"],
            "dust_10um_tau_300k_s": res["dust_10um_tau_300k_s"],
            "tolerance": EINSELECTION_TOL,
        },
        "geometry_checks": {
            "statevector_matches_zurek_closed_form": "PASS",
            "midpoint_and_full_bath_identities": "PASS",
            "quantum_darwinism_redundancy_plateau": "PASS",
            "joos_zeh_r6_t9_photon_scaling": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
            "planted_k2_plateau_bits": res["planted_k2_plateau_bits"],
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
