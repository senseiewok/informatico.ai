#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.06 (Does Gravity Collapse the Wave?).
Canonical URL: https://informatico.ai/timegravity/t06/
Central number: from the Gran Sasso counts (576 measured, 506 background, 62 days) and the paper's rate constant
z_s = a/R0³, a ≈ 1.8e-29 m³, the 95 % lower bound on R0 recomputes to 0.545e-10 m, within 20 % (actually 2 %) of the
published 0.54e-10 m; the parameter-free R0 = 0.05e-10 m would have produced about 1.4e5 photons and is excluded;
E_G for two displaced uniform spheres agrees with a direct numerical integration within 1e-3. Planted defect: the
bound drawn on the wrong side (small R0 treated as allowed); `--planted-defect` must exit non-zero with FAIL on stderr.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_bounds import DP_TOL, GS_R0_BOUND_M, check_dp  # noqa: E402

FILES_DIR = ROOT / "src" / "research" / "timegravity" / "t06" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t06_reference.json").read_text(encoding="utf-8"))
    assert abs(ref["gran_sasso"]["r0_bound_recomputed_m"] - GS_R0_BOUND_M) / GS_R0_BOUND_M < 0.2, "reference bound off"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_dp(planted_defect=planted)
        assert res["double_entry_ok"], f"E_G closed form vs quadrature differ by {res['max_rel_err_interaction_energy']:.2e} (> {DP_TOL})"
        assert res["limits_ok"], "E_G limits (6/5 G M^2/R at large d, 0 at d = 0) not recovered"
        assert res["bound_ok"], f"recomputed R0 bound {res['r0_bound_recomputed_m']:.3e} m is not within 20% of {GS_R0_BOUND_M:.2e} m"
        assert res["a_within_decade"], f"rate prefactor {res['a_recomputed_no_efficiency_m3']:.2e} not within a decade of the paper's {res['a_paper_m3']:.2e}"
        assert res["paramfree_excluded"], (
            "the parameter-free R0 = 0.05e-10 m is treated as allowed: the bound is drawn on the wrong side "
            f"(it would have produced {res['counts_at_paramfree_r0']:.2e} photons against an excess limit of {res['excess_upper_limit_counts']:.0f})"
        )
        assert res["xenonnt_consistent"], "the XENONnT bound does not sit on the allowed side above Gran Sasso's"
        assert res["defect_rejected"], "planted bound inversion was accepted"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.06", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.06",
        "canonical_url": "https://informatico.ai/timegravity/t06/",
        "central_number": {"r0_bound_recomputed_m": res["r0_bound_recomputed_m"], "r0_bound_paper_m": res["r0_bound_paper_m"],
                           "excess_upper_limit_counts_95": res["excess_upper_limit_counts"], "counts_at_paramfree_r0": res["counts_at_paramfree_r0"],
                           "tau_1um_1e-14kg_2R_s": res["tau_1um_1e-14kg_2R_s"], "max_rel_err_E_G": res["max_rel_err_interaction_energy"]},
        "geometry_checks": {
            "E_G_closed_form_vs_quadrature": "PASS",
            "bound_recomputed_from_counts": "PASS",
            "paramfree_value_excluded": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
