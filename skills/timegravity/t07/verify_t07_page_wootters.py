#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.07 (The Equation with No Time).
Canonical URL: https://informatico.ai/timegravity/t07/
Central number: a Page–Wootters history state on a 16-level clock and a qubit satisfies H|Ψ⟩⟩ = 0 (residual < 1e-10);
conditioning on the clock's time states gives P(+x | t_n) = cos²(ε t_n / 2), the closed-form Schrödinger solution,
within 1e-10; conditioning on the clock's energy basis gives P = 1/2 for every reading (no time in that split); a
pure-Python Jacobi eigensolver on the 64×64 real embedding finds the state entirely in the constraint's kernel.
Planted defect: a clock whose generator does not match the constraint (quadratic spectrum): the residual is of
order 10 and the stationarity check must fail; `--planted-defect` exits non-zero with FAIL on stderr.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_quantum import PW_TOL, check_page_wootters  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t07" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t07_reference.json").read_text(encoding="utf-8"))
    assert ref["constraint_residual"] < PW_TOL, "reference history state is not stationary"
    assert ref["jacobi_kernel"]["kernel_dim"] >= 1, "reference kernel is empty"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_page_wootters(planted_defect=planted)
        assert res["stationary"], (
            f"H|Psi>> != 0: residual {res['constraint_residual']:.3e} (> {PW_TOL:g}); the clock's generator does not match the constraint"
        )
        assert res["schroedinger"], f"conditional probabilities miss cos^2(eps t/2) by {res['max_dev_from_schroedinger']:.3e}"
        assert res["flat_other_split"], "conditioning on the clock energy basis should carry no evolution"
        assert res["in_kernel"], f"history state not in the Jacobi kernel (projection {res['projection_onto_kernel']:.6f})"
        assert res["defect_rejected"], "planted non-commuting clock was accepted"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.07", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.07",
        "canonical_url": "https://informatico.ai/timegravity/t07/",
        "central_number": {"constraint_residual": res["constraint_residual"], "max_dev_from_schroedinger": res["max_dev_from_schroedinger"],
                           "kernel_dim": res["kernel_dim"], "projection_onto_kernel": res["projection_onto_kernel"], "tolerance": PW_TOL},
        "geometry_checks": {
            "history_state_stationary": "PASS",
            "conditioning_recovers_schroedinger": "PASS",
            "other_split_has_no_time": "PASS",
            "jacobi_kernel_membership": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
            "planted_residual": res["planted_residual"],
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
