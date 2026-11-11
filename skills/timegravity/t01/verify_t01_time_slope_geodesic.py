#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.01 (Gravity as a Slope in the Rate of Time).
Canonical URL: https://informatico.ai/timegravity/t01/
Central number: a body released at rest in ds² = −A(z)c²dt² + dz², A(z) = 1 + 2gz/c², falls at a = −g with no force
term; recomputed by RK4 and required within 1e-6 relative. Knockout: flatten A'(z) to zero and nothing falls (|a| < 1e-12).
Planted defect: a sign flip of A'(z) makes the body rise; the check must reject it. `--planted-defect` runs the flipped
slope as if it were the real one and must exit non-zero with FAIL on stderr.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel import FLAT_TOL, G0, REL_TOL, run_checks  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t01" / "files"


def verify_reference_files() -> dict:
    """The committed reference artefact must match its manifest and the kernel's own numbers."""
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count {len(raw)} != manifest {entry['bytes']}"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t01_reference.json").read_text(encoding="utf-8"))
    assert abs(ref["a_eff_m_per_s2"] + G0) / G0 < REL_TOL, "reference a_eff does not fall at g"
    assert abs(ref["a_flat_m_per_s2"]) < FLAT_TOL, "reference a_flat is not zero"
    assert ref["a_flip_m_per_s2"] > 0, "reference a_flip should rise"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = run_checks(planted_defect=planted)
        assert res["falls_at_g"], (
            f"a = {res['a_eff']:+.9f} m/s^2 is not -g within {REL_TOL:g} relative (rel err {res['rel_err']:.3e}); "
            "a flipped slope makes the body rise"
        )
        assert res["knockout_still"], f"flattened gradient still moves the body: a = {res['a_flat']:.3e}"
        assert res["flip_rejected"], "sign-flip defect was accepted"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.01", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.01",
        "canonical_url": "https://informatico.ai/timegravity/t01/",
        "central_number": {"a_eff_m_per_s2": res["a_eff"], "g_m_per_s2": G0, "rel_err": res["rel_err"], "rel_tol": REL_TOL},
        "geometry_checks": {
            "falls_at_g_no_force_term": "PASS",
            "flattened_gradient_nothing_falls": "PASS",
            "a_flat_m_per_s2": res["a_flat"],
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
            "a_flip_m_per_s2": res["a_flip"],
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
