#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.02 (Everyone Moves at One Rate).
Canonical URL: https://informatico.ai/timegravity/t02/
Central number: the GPS satellite clock gains about +45.7 µs/day from the weaker potential and loses about −7.2 µs/day
from its speed, net about +38.5 µs/day (Ashby 2003), recomputed from GM, the orbit radius and c. Double entry: the
same net gain from the Schwarzschild rate ratio dτ/dt of each clock must agree within 0.3 µs/day. Planted defect: a
sign flip of the gravitational term; `--planted-defect` must exit non-zero with FAIL on stderr.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel import GPS_DOUBLE_ENTRY_TOL_US, GPS_TOL_US, check_gps  # noqa: E402

FILES_DIR = ROOT / "src" / "research" / "timegravity" / "t02" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t02_reference.json").read_text(encoding="utf-8"))
    assert abs(ref["gps_first_order_us_per_day"]["net_us"] - 38.5) < GPS_TOL_US, "reference net offset off"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_gps(planted_defect=planted)
        assert res["grav_ok"], f"gravitational term {res['grav_us']:+.2f} µs/day is not about +45.7 (a flipped sign makes the satellite clock run slow)"
        assert res["vel_ok"], f"velocity term {res['vel_us']:+.2f} µs/day is not about -7.2"
        assert res["net_ok"], f"net {res['net_us']:+.2f} µs/day is not within ±{GPS_TOL_US} of +38.5"
        assert res["double_entry_ok"], f"double entry disagrees by {res['double_entry_diff_us']:.3f} µs/day (> {GPS_DOUBLE_ENTRY_TOL_US})"
        assert res["flip_rejected"], "sign-flip defect was accepted"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.02", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.02",
        "canonical_url": "https://informatico.ai/timegravity/t02/",
        "central_number": {"grav_us_per_day": res["grav_us"], "vel_us_per_day": res["vel_us"], "net_us_per_day": res["net_us"],
                           "net_schwarzschild_us_per_day": res["net_schwarzschild_us"], "double_entry_diff_us": res["double_entry_diff_us"],
                           "position_error_per_day_m": res["position_error_per_day_m"], "window_us": GPS_TOL_US},
        "geometry_checks": {
            "first_order_terms": "PASS",
            "double_entry_schwarzschild": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
