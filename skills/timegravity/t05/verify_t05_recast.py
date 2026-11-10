#!/usr/bin/env python3
"""T.05 · Recast verifier: the Eöt-Wash 2020 published Yukawa limits (Lee dissertation Table 11.4) recast onto the smeared pair potential.

Checks: the table (66 rows, monotone λ, signed limits of the right signs), the experiment's own gravitational-strength edge recovered
between 35 and 40 µm, the recast σ_95 between 32 and 35 µm on the quick configuration, consistency with the constant the dispute and
ladder kernels use, the shape mimic within 5 %, the retired 44 µm edge match excluded with Δχ² > 10, and the planted defect (the retired
single-separation method) rejected because it returns the 44 µm reading. `--full` adds the four separation weightings × two harmonics
(about twenty minutes). `--planted-defect` must exit 1."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_recast import check_recast  # noqa: E402
from timegravity_kernel_dispute import SIGMA_ESTIMATE_M  # noqa: E402
from timegravity_kernel_ladder import EW_MATCH_SIGMA_M  # noqa: E402


def main() -> int:
    planted = "--planted-defect" in sys.argv
    try:
        res = check_recast(planted_defect=planted, quick="--full" not in sys.argv)
        assert res["table_ok"], "Table 11.4 transcription failed its shape checks"
        assert res["edge_ok"], f"the published |α95| = 1 crossing is at {res['edge_crossing_lambda_m'] * 1e6:.1f} µm, not between 35 and 40 µm"
        assert res["recast_ok"], f"the recast is not as expected: σ_95 = {res['sigma_95_m'] * 1e6:.2f} µm, spread {res['spread_m'] * 1e6:.2f} µm"
        assert abs(res["sigma_95_m"] - SIGMA_ESTIMATE_M) < 0.4e-6, "the dispute kernel's SIGMA_ESTIMATE_M does not match the recast"
        assert abs(EW_MATCH_SIGMA_M - SIGMA_ESTIMATE_M) < 1e-12, "the ladder's EW_MATCH_SIGMA_M differs from the dispute kernel's constant"
        if res["defect_rejected"] is not None:
            assert res["defect_rejected"], "the planted single-separation method was not distinguishable from the recast"
        out = {
            "status": "PASS", "folio_id": "T.05",
            "central_number": {"sigma_95_m": res["sigma_95_m"], "variants_sigma_95_m": res["variants_sigma_95_m"], "spread_m": res["spread_m"],
                               "edge_crossing_lambda_m": res["edge_crossing_lambda_m"], "retired_edge_match_sigma_m": res["retired_edge_match_sigma_m"],
                               "at_33um": res["at_33um"], "at_35um": res["at_35um"], "at_edge_match_44um": res["at_edge_match_44um"], "table_rows": res["table_rows"]},
            "geometry_checks": {"table_11_4_transcription": "PASS", "gravitational_strength_edge_recovered": "PASS", "recast_sigma_95": "PASS", "abs_torque_weighting_agrees": "PASS", "data_lean_positive_in_window": "PASS",
                                "constants_consistent": "PASS", "planted_single_separation_method_rejected": "PASS" if res["defect_rejected"] else "n/a"},
        }
        print(json.dumps(out, indent=2, default=str))
        return 0
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.05", "error": str(exc)}), file=sys.stderr)  # run_all reads FAIL on stderr
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
