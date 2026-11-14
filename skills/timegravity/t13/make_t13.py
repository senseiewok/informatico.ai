#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.13 (Where Infrared Gravity Meets Gauge Theory).
Canonical URL: https://informatico.ai/timegravity/t13/
Writes src/timegravity/t13/files/t13_reference.json (Weinberg s = 1, 2, 3 soft Ward identities,
Christodoulou / Strominger-Zhiboedov gravitational-wave memory strain and proper arm holonomy vs composite
Gauss-Legendre quadrature, and one-loop Standard Model chiral & mixed gauge-gravitational anomaly traces)
and manifest.json.
Standard library only; byte-for-byte reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_holonomy_soft import build_reference as kernel_reference  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t13" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def _round_obj(obj):
    if isinstance(obj, bool) or obj is None or isinstance(obj, (int, str)):
        return obj
    if isinstance(obj, float):
        return r12(obj)
    if isinstance(obj, list):
        return [_round_obj(v) for v in obj]
    if isinstance(obj, dict):
        return {k: _round_obj(v) for k, v in obj.items()}
    return obj


def build_reference() -> dict:
    clean = _round_obj(kernel_reference(planted_defect=False))
    planted = _round_obj(kernel_reference(planted_defect=True))
    return {
        "folio_id": "T.13",
        "title": "Where Infrared Gravity Meets Gauge Theory",
        "construction": (
            "Weinberg soft theorems: sum_a eta_a q_a = 0 (s=1), sum_a eta_a kappa_a p_a^mu = 0 => kappa_a = kappa (s=2), "
            "sum_a eta_a g_a p_a^mu p_a^nu = 0 => g_a = 0 (s>=3); "
            "Memory holonomy: Delta h_char = G E_rad / (c^4 D_L), Delta L / L_0 = (1/2) Delta h_+^mem; "
            "Anomaly cancellation (6Y): Tr[6Y] = 0, Tr[SU(3)^2(6Y)] = 0, Tr[SU(2)^2(6Y)] = N_c - 3, Tr[(6Y)^3] = -54(N_c - 3)"
        ),
        "clean": clean,
        "planted_defect_snapshot": {
            "s2_ward_vector_rel_norm": planted["soft_theorems"]["s2_ward_vector_rel_norm"],
            "tr_su2_sq_6y": planted["anomaly_cancellation"]["active_generation"]["tr_su2_sq_6y"],
            "tr_u1_cubic_6y": planted["anomaly_cancellation"]["active_generation"]["tr_u1_cubic_6y"],
            "all_anomalies_cancel": planted["anomaly_cancellation"]["active_generation"]["all_anomalies_cancel"],
        },
        "lean_companion": "skills/timegravity/t13/HolonomySoftAnomaly.lean",
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t13_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.13",
        "generator": "skills/timegravity/t13/make_t13.py",
        "verifier": "skills/timegravity/t13/verify_t13_holonomy_soft.py",
        "lean_formalization": "skills/timegravity/t13/HolonomySoftAnomaly.lean",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.13 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
