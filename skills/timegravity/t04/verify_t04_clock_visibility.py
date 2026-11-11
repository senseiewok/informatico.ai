#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.04 (A Clock in Two Places).
Canonical URL: https://informatico.ai/timegravity/t04/
Central number: for a two-level clock in a superposition of two heights, V = |cos(ω Δτ / 2)| with Δτ = g Δh T / c²
(Zych et al. 2011); the closed form equals the explicit state overlap within 1e-12 on a grid; V(Δh = 0) = 1; for a
Sr optical clock the visibility first vanishes at Δh·T ≈ 10.7 m·s. Planted defect: a clock that never decoheres
(ω = 0, so V ≡ 1); the "visibility vanishes" check must fail and `--planted-defect` must exit non-zero with FAIL.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_quantum import ZYCH_TOL, check_zych  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t04" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t04_reference.json").read_text(encoding="utf-8"))
    for row in ref["table_dh_m__T_s__dtau_s__V_closed__V_overlap"]:
        assert abs(row[3] - row[4]) < 1e-9, "reference table: closed form and overlap disagree"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_zych(planted_defect=planted)
        assert res["double_entry"], f"closed form and state overlap disagree by {res['max_dev_closed_vs_overlap']:.3e}"
        assert res["unit_at_zero"], "visibility at zero separation is not 1"
        assert res["decoheres"], (
            f"visibility at the first zero is {res['v_at_first_zero']:.3e}, not 0: this clock never decoheres (omega = {res['omega_used']:.3e})"
        )
        assert res["defect_rejected"], "planted never-decohering clock was accepted"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.04", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.04",
        "canonical_url": "https://informatico.ai/timegravity/t04/",
        "central_number": {"first_zero_dh_T_m_s": res["first_zero_dh_T_m_s"], "v_1m_1s_sr_clock": res["v_1m_1s_sr_clock"],
                           "dtau_1m_1s_s": res["dtau_1m_1s_s"], "max_dev_closed_vs_overlap": res["max_dev_closed_vs_overlap"], "tolerance": ZYCH_TOL},
        "geometry_checks": {
            "closed_form_equals_state_overlap": "PASS",
            "unit_visibility_at_zero_separation": "PASS",
            "visibility_vanishes_at_first_zero": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
