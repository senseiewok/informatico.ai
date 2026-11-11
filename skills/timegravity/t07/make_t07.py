#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.07 (The Equation with No Time).
Canonical URL: https://informatico.ai/timegravity/t07/
Writes src/timegravity/t07/files/t07_reference.json (the Page–Wootters history state's conditional
probabilities against the closed form, the constraint residual, the Jacobi kernel check) and manifest.json.
Standard library only; byte-for-byte reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_quantum import PW_D, PW_K, PW_TOL, pw_history_state, pw_kernel_check  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t07" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def build_reference() -> dict:
    st = pw_history_state()
    kern = pw_kernel_check(st)
    bad = pw_history_state(planted_defect=True)
    return {
        "folio_id": "T.07",
        "title": "The Equation with No Time",
        "construction": "H = H_C x 1 + 1 x H_S, H|Psi>> = 0; |Psi>> = (1/sqrt d) sum_n |t_n> x exp(-i H_S n)|+x>; d-level cyclic clock (Pegg-Barnett)",
        "parameters": {"clock_levels_d": PW_D, "k": PW_K, "eps": r12(st["eps"]), "hilbert_dim": 2 * PW_D, "tolerance": PW_TOL},
        "constraint_residual": r12(st["constraint_residual"]),
        "max_dev_from_schroedinger": r12(st["max_dev_from_schroedinger"]),
        "conditional_n__p_plus_x__cos2": [[c["n"], r12(c["p_plus_x"]), r12(c["closed_form"])] for c in st["conditional"]],
        "energy_split_m__p_plus_x": [[e["m"], r12(e["p_plus_x"]) if e["weight"] > 1e-12 else None] for e in st["energy_split"]],
        "jacobi_kernel": {"kernel_dim": kern["kernel_dim"], "projection_onto_kernel": r12(kern["projection_onto_kernel"]),
                          "eigenvalue_min": r12(kern["eigenvalue_min"]), "eigenvalue_max": r12(kern["eigenvalue_max"])},
        "planted_defect_constraint_residual": r12(bad["constraint_residual"]),
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t07_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.07",
        "generator": "skills/timegravity/t07/make_t07.py",
        "verifier": "skills/timegravity/t07/verify_t07_page_wootters.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.07 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
