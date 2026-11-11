#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.03 (What Sets the Slope).
Canonical URL: https://informatico.ai/timegravity/t03/
Writes src/timegravity/t03/files/t03_reference.json (the Poisson grid solution for an Earth-mass uniform
sphere, sampled, and the two-body fall) and manifest.json. Standard library only; byte-for-byte reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel import EP_SEP_TOL, G_NEWTON, GM_EARTH, POISSON_REL_TOL, R_EARTH, fall_two_bodies, poisson_radial  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t03" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def build_reference() -> dict:
    mass = GM_EARTH / G_NEWTON
    n = 2000
    sol = poisson_radial(mass, R_EARTH, 4.0 * R_EARTH, n)
    step = n // 40
    samples = [[r12(sol["r"][i] / R_EARTH), r12(sol["phi"][i] / (G_NEWTON * mass / R_EARTH)), r12(sol["g"][i] / (G_NEWTON * mass / R_EARTH**2))]
               for i in range(0, n + 1, step)]
    fall0 = fall_two_bodies(0.0)
    fall1 = fall_two_bodies(1e-3)
    return {
        "folio_id": "T.03",
        "title": "What Sets the Slope",
        "equation": "nabla^2 Phi = 4 pi G rho (weak-field, static limit of G_00 = 8 pi G T_00 / c^4)",
        "constants": {"G_m3_kg_s2": G_NEWTON, "GM_m3_s2": GM_EARTH, "R_m": R_EARTH, "mass_kg": r12(mass), "grid_points": n, "r_max_over_R": 4.0},
        "tolerances": {"poisson_rel_tol": POISSON_REL_TOL, "ep_separation_tol_m": EP_SEP_TOL},
        "poisson_worst_rel_err_exterior": r12(sol["worst_rel_err_exterior"]),
        "poisson_g_surface_rel_err": r12(sol["g_surface_rel_err"]),
        "phi_center_over_GM_R": r12(sol["phi_center"] / (G_NEWTON * mass / R_EARTH)),
        "phi_center_analytic_over_GM_R": -1.5,
        "samples_r_over_R__phi_over_GM_R__g_over_GM_R2": samples,
        "two_bodies_eta_0_separation_m": r12(fall0["separation_m"]),
        "two_bodies_eta_1e-3_separation_m": r12(fall1["separation_m"]),
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t03_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.03",
        "generator": "skills/timegravity/t03/make_t03.py",
        "verifier": "skills/timegravity/t03/verify_t03_poisson_equivalence.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.03 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
