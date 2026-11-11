#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.02 (Everyone Moves at One Rate).
Canonical URL: https://informatico.ai/timegravity/t02/
Writes src/timegravity/t02/files/t02_reference.json (GPS terms two ways, the uncertainty budget, a
light-clock table) and manifest.json (byte counts and SHA-256). Standard library only; byte-for-byte reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel import (  # noqa: E402
    A_GPS, C, GM_EARTH, GPS_DOUBLE_ENTRY_TOL_US, GPS_TOL_US, R_EARTH,
    gps_position_error_per_day_m, gps_schwarzschild_net, gps_terms, gps_uncertainty_budget, light_clock_dilation,
)

FILES_DIR = ROOT / "src" / "timegravity" / "t02" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def build_reference() -> dict:
    terms = gps_terms()
    budget = gps_uncertainty_budget()
    return {
        "folio_id": "T.02",
        "title": "Everyone Moves at One Rate",
        "constants": {"c_m_per_s": C, "GM_m3_s2": GM_EARTH, "a_gps_m": A_GPS, "R_ground_m": R_EARTH},
        "tolerances": {"net_window_us_per_day": GPS_TOL_US, "double_entry_us_per_day": GPS_DOUBLE_ENTRY_TOL_US},
        "gps_first_order_us_per_day": {k: r12(v) for k, v in terms.items()},
        "gps_schwarzschild_net_us_per_day": r12(gps_schwarzschild_net()),
        "position_error_per_day_m": r12(gps_position_error_per_day_m(terms["net_us"])),
        "uncertainty_budget": {
            "combined_sigma_us_per_day": r12(budget["combined_sigma_us"]),
            "ground_rotation_effect_us_per_day": r12(budget["ground_rotation_effect_us"]),
            "rows": [{"input": r["input"], "value": r12(r["value"]), "sigma": r12(r["sigma"]),
                      "contribution_us_per_day": r12(r["contribution_us"])} for r in budget["rows"]],
            "note": budget["note"],
        },
        "light_clock_gamma": [[b, r12(light_clock_dilation(b))] for b in (0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99)],
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t02_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.02",
        "generator": "skills/timegravity/t02/make_t02.py",
        "verifier": "skills/timegravity/t02/verify_t02_gps_one_rate.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.02 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
