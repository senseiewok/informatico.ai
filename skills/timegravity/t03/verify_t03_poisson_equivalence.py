#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.03 (What Sets the Slope).
Canonical URL: https://informatico.ai/timegravity/t03/
Central number: the weak-field Einstein equation reduced to Poisson's equation, solved on a 2,000-point radial grid
for an Earth-mass uniform sphere, recovers Φ = −GM/r outside the body within 2e-3 relative and Φ(0) = −3GM/2R at the
centre; two bodies of different composition released together separate by less than 1e-12 m after one second
(η = 0). Planted defect: a composition-dependent fall (η = 1e-3) separates them by about 5 mm; `--planted-defect`
must exit non-zero with FAIL on stderr.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel import EP_SEP_TOL, POISSON_REL_TOL, check_poisson_ep  # noqa: E402

FILES_DIR = ROOT / "src" / "research" / "timegravity" / "t03" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t03_reference.json").read_text(encoding="utf-8"))
    assert ref["poisson_worst_rel_err_exterior"] < POISSON_REL_TOL, "reference Poisson solution off"
    assert ref["two_bodies_eta_0_separation_m"] < EP_SEP_TOL, "reference two-body fall separates"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_poisson_ep(planted_defect=planted)
        assert res["poisson_ok"], f"grid solution misses GM/r outside the body: worst rel err {res['poisson_worst_rel_err_exterior']:.2e}"
        assert res["center_ok"], f"central potential misses -3GM/2R: rel err {res['phi_center_rel_err']:.2e}"
        assert res["ep_ok"], (
            f"two compositions released together separated by {res['separation_m']:.3e} m after 1 s "
            f"(> {EP_SEP_TOL:g}); a composition-dependent fall violates the equivalence principle"
        )
        assert res["flip_rejected"], "planted composition-dependent fall was accepted"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.03", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.03",
        "canonical_url": "https://informatico.ai/timegravity/t03/",
        "central_number": {"poisson_worst_rel_err_exterior": res["poisson_worst_rel_err_exterior"],
                           "poisson_g_surface_rel_err": res["poisson_g_surface_rel_err"],
                           "phi_center_rel_err": res["phi_center_rel_err"],
                           "g_surface_m_s2": res["g_surface_m_s2"],
                           "two_body_separation_m": res["separation_m"], "rel_tol": POISSON_REL_TOL},
        "geometry_checks": {
            "poisson_recovers_GM_over_r": "PASS",
            "equivalence_principle_eta_0": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
            "planted_separation_m": res["planted_separation_m"],
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
