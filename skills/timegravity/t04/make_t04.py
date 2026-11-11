#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.04 (A Clock in Two Places).
Canonical URL: https://informatico.ai/timegravity/t04/
Writes src/timegravity/t04/files/t04_reference.json (visibility against height difference and clock
frequency, closed form and state overlap) and manifest.json. Standard library only; byte-for-byte reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel import C, G0  # noqa: E402
from timegravity_kernel_quantum import OMEGA_SR, ZYCH_TOL, clock_overlap, proper_time_difference, zych_first_zero, zych_visibility  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t04" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def build_reference() -> dict:
    table = []
    for dh in (0.0, 0.5, 1.0, 2.0, 5.0, 10.0):
        for T in (0.1, 1.0, 10.0):
            table.append([dh, T, r12(proper_time_difference(dh, T)), r12(zych_visibility(dh, T, OMEGA_SR)), r12(clock_overlap(dh, T, OMEGA_SR))])
    return {
        "folio_id": "T.04",
        "title": "A Clock in Two Places",
        "formula": "V = |cos(omega * dtau / 2)|, dtau = g * dh * T / c^2 (Zych et al. 2011; omega = Delta E / hbar)",
        "constants": {"c_m_per_s": C, "g_m_per_s2": G0, "omega_sr_rad_per_s": r12(OMEGA_SR)},
        "tolerance_closed_form_vs_overlap": ZYCH_TOL,
        "first_zero_dh_T_m_s": r12(zych_first_zero(OMEGA_SR)),
        "table_dh_m__T_s__dtau_s__V_closed__V_overlap": table,
        "note": "An experiment description, not a result: no gravitational version of the clock interferometer has run.",
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t04_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.04",
        "generator": "skills/timegravity/t04/make_t04.py",
        "verifier": "skills/timegravity/t04/verify_t04_clock_visibility.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.04 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
