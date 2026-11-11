#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.05 (Does Gravity Entangle, and Would That Settle It?).
Canonical URL: https://informatico.ai/timegravity/t05/
Central number: for the 2017 proposal's own geometry (1e-14 kg, 450 µm apart, each split by 250 µm, held 2.5 s) the four
Newtonian branch phases give an entanglement phase Δφ = 0.314 rad, concurrence |sin(Δφ/2)| = 0.156, recomputed from the
reduced-state purity within 1e-12, and a Peres negativity of 0.078 (= C/2) from the partial transpose through the track's Jacobi
solver; full entanglement at 25.0 s; a classical mean-field (LOCC) channel entangles nothing (< 1e-12) on a grid of geometries,
and the disputed classical non-LOCC channel is carried as an interval, never a point. Planted defect: a LOCC channel that
entangles (its phases copied from the quantum channel); `--planted-defect` must exit non-zero with FAIL on stderr.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_entangle import ENT_TOL, NEG_TOL, check_bmv  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t05" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t05_reference.json").read_text(encoding="utf-8"))
    assert abs(ref["quantum_channel"]["concurrence"] - 0.1563) < 1e-3, "reference concurrence off"
    assert ref["locc_channel"]["concurrence"] < ENT_TOL, "reference LOCC channel entangles"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_bmv(planted_defect=planted)
        assert res["double_entry_ok"], f"concurrence closed form {res['concurrence_closed']:.12f} vs purity {res['concurrence_from_purity']:.12f} differ by more than {ENT_TOL}"
        assert res["negativity_ok"], f"negativity {res['negativity']:.9f} is not C/2 within {NEG_TOL}"
        assert res["paper_consistent"], "the recomputed phases are not within a factor of 4 of the proposal's order-of-magnitude values (0.7, -0.2)"
        assert res["full_ok"], f"concurrence at Δφ = π is {res['concurrence_at_pi']}, not 1"
        assert res["knockout_ok"], "with G = 0 the state is still entangled"
        assert res["locc_ok"], (
            "the classical LOCC channel entangles: worst concurrence/negativity "
            f"{res['worst_locc_entanglement']:.3e} (> {ENT_TOL}); a channel of local operations and classical communication cannot create entanglement"
        )
        assert res["mean_ok"], "the LOCC channel does not reproduce the mean Newtonian phase"
        assert res["budget_ok"], "no finite dephasing budget found"
        assert res["disputed_ok"], "the disputed channel is not carried as the interval [0, C_quantum]"
        assert res["defect_rejected"], "the planted entangling LOCC channel was not detectable"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.05", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.05",
        "canonical_url": "https://informatico.ai/timegravity/t05/",
        "central_number": {"entanglement_phase_rad": res["entanglement_phase_rad"], "concurrence": res["concurrence_closed"],
                           "negativity": res["negativity"], "time_to_full_entanglement_s": res["time_to_full_entanglement_s"],
                           "gamma_t_negativity_zero": res["gamma_t_negativity_zero"], "worst_locc_entanglement": res["worst_locc_entanglement"],
                           "disputed_interval": res["disputed_interval"], "phase_rl_rad": res["paper_phase_rl_rad"], "phase_lr_rad": res["paper_phase_lr_rad"]},
        "geometry_checks": {
            "concurrence_closed_form_vs_purity": "PASS",
            "negativity_is_half_concurrence": "PASS",
            "locc_channel_entangles_nothing": "PASS",
            "disputed_channel_carried_as_interval": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
