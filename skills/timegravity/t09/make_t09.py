#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.09 (A Horizon Rings Like a Bell).
Canonical URL: https://informatico.ai/timegravity/t09/
Writes src/research/timegravity/t09/files/t09_reference.json (Leaver's continued-fraction Kerr quasinormal modes
for l=m=2, n=0 and n=1 across chi in [0, 0.90], Smarr and differential first-law checks, and GW150914-scale SI
frequencies and damping times) and manifest.json.
Standard library only; byte-for-byte reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_kerr import (  # noqa: E402
    FIDUCIAL_CHI,
    FIDUCIAL_MASS_SOLAR,
    KERR_SPINS,
    check_kerr,
    physical_ringdown,
    solve_kerr_qnm_branch,
)

FILES_DIR = ROOT / "src" / "research" / "timegravity" / "t09" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def build_reference() -> dict:
    b0 = {r["chi"]: r for r in solve_kerr_qnm_branch(KERR_SPINS, overtone_n=0)}
    b1 = {r["chi"]: r for r in solve_kerr_qnm_branch(KERR_SPINS, overtone_n=1)}
    chk = check_kerr()
    rows = []
    for chi in KERR_SPINS:
        r0 = b0[chi]
        r1 = b1[chi]
        phys0 = physical_ringdown(FIDUCIAL_MASS_SOLAR, r0["mw_re"], r0["mw_im"])
        rows.append([
            chi,
            r12(r0["mw_re"]),
            r12(r0["mw_im"]),
            r12(r1["mw_re"]),
            r12(r1["mw_im"]),
            r12(phys0["f_hz"]),
            r12(phys0["tau_ms"]),
        ])
    return {
        "folio_id": "T.09",
        "title": "A Horizon Rings Like a Bell",
        "construction": (
            "Kerr horizon r_+ = GM/c^2 (1 + sqrt(1 - chi^2)), A = 8 pi (GM/c^2)^2 (1 + sqrt(1 - chi^2)); "
            "Smarr M c^2 = (kappa c^2 / 4 pi G) A + 2 Omega_H J; Leaver (1985) coupled angular + radial "
            "3-term continued fractions for s = -2, l = m = 2, n in {0, 1}"
        ),
        "parameters": {
            "default_m_solar": FIDUCIAL_MASS_SOLAR,
            "default_chi": FIDUCIAL_CHI,
            "cf_tolerance": 1e-10,
            "benchmark_tolerance": 1e-6,
        },
        "worst_smarr_rel_err": r12(chk["worst_smarr_rel_err"]),
        "worst_first_law_rel_err": r12(chk["worst_first_law_rel_err"]),
        "max_cf_residual": r12(chk["max_cf_residual"]),
        "max_published_dev_220": r12(chk["max_published_dev_220"]),
        "max_published_dev_221": r12(chk["max_published_dev_221"]),
        "gw150914_fiducial": {
            "m_solar": FIDUCIAL_MASS_SOLAR,
            "chi": FIDUCIAL_CHI,
            "r_plus_km": r12(chk["fiducial_62msun_chi068"]["r_plus_km"]),
            "area_km2": r12(chk["fiducial_62msun_chi068"]["area_km2"]),
            "f_220_hz": r12(chk["fiducial_62msun_chi068"]["f_220_hz"]),
            "tau_220_ms": r12(chk["fiducial_62msun_chi068"]["tau_220_ms"]),
            "f_221_hz": r12(chk["fiducial_62msun_chi068"]["f_221_hz"]),
            "tau_221_ms": r12(chk["fiducial_62msun_chi068"]["tau_221_ms"]),
        },
        "qnm_chi__w220_re_im__w221_re_im__f220_hz__tau220_ms": rows,
        "planted_defect": {
            "planted_first_law_rel_err": r12(chk["planted_first_law_rel_err"]),
            "planted_cf_residual": r12(chk["planted_cf_residual"]),
        },
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t09_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.09",
        "generator": "skills/timegravity/t09/make_t09.py",
        "verifier": "skills/timegravity/t09/verify_t09_kerr_ringdown.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.09 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
