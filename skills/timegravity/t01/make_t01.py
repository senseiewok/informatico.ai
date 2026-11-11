#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.01 (Gravity as a Slope in the Rate of Time).
Canonical URL: https://informatico.ai/timegravity/t01/
Writes src/timegravity/t01/files/t01_reference.json (constants, sampled worldline, the three accelerations)
and manifest.json (byte counts and SHA-256). Standard library only; byte-for-byte reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel import C, FLAT_TOL, G0, N_STEPS, REL_TOL, T_PROPER, integrate  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t01" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def build_reference() -> dict:
    main = integrate(True, +1.0, sample_every=1000)
    flat = integrate(False, +1.0)
    flip = integrate(True, -1.0)
    return {
        "folio_id": "T.01",
        "title": "Gravity as a Slope in the Rate of Time",
        "metric": "ds^2 = -A(z) c^2 dt^2 + dz^2, A(z) = 1 + 2 g z / c^2 (only g_tt varies with height; no force term)",
        "constants": {"c_m_per_s": C, "g_m_per_s2": G0, "T_proper_s": T_PROPER, "rk4_steps": N_STEPS},
        "tolerances": {"rel_tol_a_vs_g": REL_TOL, "flat_abs_tol": FLAT_TOL},
        "slope_Ap_per_m": r12(main["slope_Ap"]),
        "a_eff_m_per_s2": r12(main["a_eff"]),
        "a_flat_m_per_s2": r12(flat["a_eff"]),
        "a_flip_m_per_s2": r12(flip["a_eff"]),
        "samples_tau_t_z": [[r12(a), r12(b), r12(c)] for a, b, c in main["samples"]],
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t01_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.01",
        "generator": "skills/timegravity/t01/make_t01.py",
        "verifier": "skills/timegravity/t01/verify_t01_time_slope_geodesic.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.01 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
