#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.08 (A Horizon Has a Temperature).
Canonical URL: https://informatico.ai/timegravity/t08/
Central number: tracing the behind-the-horizon Rindler partner L out of the pure Minkowski two-mode squeezed state
produces a reduced density matrix rho_R on the right wedge whose Jacobi eigenvalues match the Planck thermal Gibbs
weights (1 - exp(-xi)) exp(-n xi) within 1e-12 at xi = 2.5 (d = 16 Fock levels) and match the exact truncated Gibbs
distribution across xi in [0.5, 4.0] to machine precision; integrating dS = c^2 dM / T_H(M) recovers A / (4 l_P^2)
within 1e-12. Planted defect: a product state |0>_L x |0>_R with zero cross-horizon entanglement (r = 0) gives pure
zero entropy and fails the thermal spectrum check; `--planted-defect` exits non-zero with FAIL on stderr.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_horizon import HORIZON_TOL, check_horizon  # noqa: E402

FILES_DIR = ROOT / "src" / "research" / "timegravity" / "t08" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t08_reference.json").read_text(encoding="utf-8"))
    assert ref["max_dev_from_planck"] < HORIZON_TOL, "reference Rindler trace misses Planck weights"
    assert ref["hawking_bekenstein"]["quadrature_vs_area_quarter_rel_err"] < HORIZON_TOL, "reference first-law integral misses A/(4 l_P^2)"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_horizon(planted_defect=planted)
        assert res["planck_ok"], (
            f"reduced state rho_R misses Planck thermal weights by {res['max_dev_from_planck']:.3e} (> {HORIZON_TOL:g}); "
            "without cross-horizon entanglement the wedge is not thermal"
        )
        assert res["worldline_ok"], f"Rindler redshift / hyperbola invariant error {res['max_hyperbola_invariant_err']:.3e}"
        assert res["first_law_ok"], f"Hawking-Bekenstein first-law quadrature error {res['quadrature_vs_area_quarter_rel_err']:.3e}"
        assert res["defect_rejected"], "planted zero-entanglement product state was accepted as thermal"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.08", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.08",
        "canonical_url": "https://informatico.ai/timegravity/t08/",
        "central_number": {
            "max_dev_from_planck": res["max_dev_from_planck"],
            "entropy_dev_from_planck": res["entropy_dev_from_planck"],
            "quadrature_vs_area_quarter_rel_err": res["quadrature_vs_area_quarter_rel_err"],
            "solar_hawking_temp_k": res["solar_hawking_temp_k"],
            "solar_s_bh_over_kb": res["solar_s_bh_over_kb"],
            "tolerance": HORIZON_TOL,
        },
        "geometry_checks": {
            "partial_trace_recovers_planck": "PASS",
            "truncated_gibbs_sweep": "PASS",
            "rindler_redshift_hyperbola": "PASS",
            "first_law_area_quarter_quadrature": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
            "planted_entropy_nats": res["planted_entropy_nats"],
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
