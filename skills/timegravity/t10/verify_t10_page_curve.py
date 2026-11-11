#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.10 (Page's Counting Argument).
Canonical URL: https://informatico.ai/timegravity/t10/
Central number: for Haar-random pure states on 10 qubits the mean entanglement entropy of the a emitted qubits matches
Page's closed form S(m,n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n) within 0.03 nats at every cut (achieved ~0.002), is
symmetric about N/2, peaks at 5 qubits (2.97 nats) and falls to 0.69 nats at the last cut; eigenvalues come from a
pure-Python Jacobi solver. Planted defect: a non-unitary toy whose entropy follows Hawking's line a·ln 2 and never
turns over; `--planted-defect` must exit non-zero with FAIL on stderr.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_bounds import PAGE_TOL_NATS, check_page_curve  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t10" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t10_reference.json").read_text(encoding="utf-8"))
    for a, toy, page, _h in ref["curve_a__toy_mean__page__hawking_line"]:
        assert abs(toy - page) < PAGE_TOL_NATS, f"reference curve misses Page's formula at a = {a}"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_page_curve(planted_defect=planted)
        assert res["matches_page"], f"toy entropies miss Page's closed form by {res['max_dev_from_page_nats']:.3f} nats (> {PAGE_TOL_NATS})"
        assert res["turns_over"], (
            f"the radiation entropy never turns over: final {res['final_nats']:.3f} nats against a peak of {res['peak_nats']:.3f}; "
            "a non-unitary toy follows Hawking's line"
        )
        assert res["symmetric"], "the curve is not symmetric about N/2"
        assert res["defect_rejected"], "planted non-unitary toy was accepted"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.10", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.10",
        "canonical_url": "https://informatico.ai/timegravity/t10/",
        "central_number": {"n_qubits": res["n_qubits"], "samples": res["samples"], "max_dev_from_page_nats": res["max_dev_from_page_nats"],
                           "peak_nats": res["peak_nats"], "final_nats": res["final_nats"], "tolerance_nats": PAGE_TOL_NATS},
        "geometry_checks": {
            "matches_page_closed_form": "PASS",
            "turns_over_at_half": "PASS",
            "symmetric_about_half": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
