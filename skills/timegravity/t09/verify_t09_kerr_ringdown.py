#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.09 (A Horizon Rings Like a Bell).
Canonical URL: https://informatico.ai/timegravity/t09/
Central number: solving Leaver's (1985) coupled angular and radial 3-term continued fractions by homotopy from
Schwarzschild (chi = 0, A_22 = 4) across chi in [0, 0.90] gives residual < 1e-10 and matches published Leaver /
Berti-Cardoso-Starinets tables within 1e-6 for both l=m=2, n=0 and n=1; Smarr's identity M c^2 = (kappa c^2 / 4 pi G) A
+ 2 Omega_H J holds within 1e-13; at M = 62 M_sun, chi = 0.68, f_220 = 273.07 Hz and tau_220 = 3.747 ms.
Planted defect: flipping the spin sign under the radical in r_+ = r_g (1 + sqrt(1 + chi^2)) breaks the Kerr no-hair
geometry, violating Smarr's relation, the differential first law, and Leaver's radial continued fraction;
`--planted-defect` exits non-zero with FAIL on stderr.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_kerr import check_kerr  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t09" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t09_reference.json").read_text(encoding="utf-8"))
    assert ref["max_cf_residual"] < 1e-10, "reference Leaver continued-fraction residual exceeds tolerance"
    assert ref["max_published_dev_220"] < 1e-6, "reference (2,2,0) QNM misses published table"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_kerr(planted_defect=planted)
        assert res["first_law_ok"], (
            f"Kerr Smarr / differential first law violated (smarr={res['worst_smarr_rel_err']:.3e}, "
            f"first_law={res['worst_first_law_rel_err']:.3e})"
        )
        assert res["qnm_ok"], (
            f"Leaver radial/angular continued-fraction residual {res['max_cf_residual']:.3e} or published table deviation "
            f"{max(res['max_published_dev_220'], res['max_published_dev_221']):.3e}"
        )
        assert res["defect_rejected"], "planted non-Kerr radical sign was accepted"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.09", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.09",
        "canonical_url": "https://informatico.ai/timegravity/t09/",
        "central_number": {
            "worst_smarr_rel_err": res["worst_smarr_rel_err"],
            "worst_first_law_rel_err": res["worst_first_law_rel_err"],
            "max_cf_residual": res["max_cf_residual"],
            "max_published_dev_220": res["max_published_dev_220"],
            "max_published_dev_221": res["max_published_dev_221"],
            "gw150914_fiducial": res["fiducial_62msun_chi068"],
        },
        "geometry_checks": {
            "smarr_horizon_identity": "PASS",
            "kerr_differential_first_law": "PASS",
            "leaver_continued_fraction_roots": "PASS",
            "published_qnm_table_agreement": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
            "planted_first_law_rel_err": res["planted_first_law_rel_err"],
            "planted_cf_residual": res["planted_cf_residual"],
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
