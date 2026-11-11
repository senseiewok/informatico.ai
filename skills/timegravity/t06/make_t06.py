#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.06 (Does Gravity Collapse the Wave?).
Canonical URL: https://informatico.ai/timegravity/t06/
Writes src/timegravity/t06/files/t06_reference.json (E_G and τ for a grid of masses and radii, the Gran Sasso
bound recomputed from the counts, the parameter-free prediction) and manifest.json. Standard library only; reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_ladder import check_ladder  # noqa: E402
from timegravity_kernel_bounds import (  # noqa: E402
    GS_A_M3, GS_BACKGROUND, GS_DAYS, GS_MEASURED, GS_R0_BOUND_M, GS_R0_PARAMFREE_M, XENONNT_R0_90, XENONNT_R0_95,
    dp_collapse_time, dp_rate_prefactor_order_of_magnitude, dp_self_energy_difference, gran_sasso_r0_bound,
    gran_sasso_signal_counts, poisson_upper_limit,
)

FILES_DIR = ROOT / "src" / "timegravity" / "t06" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def build_reference() -> dict:
    table = []
    for log_m in (-20, -18, -16, -14, -12):
        for log_r in (-9, -7, -6, -5):
            m, R = 10.0 ** log_m, 10.0 ** log_r
            table.append([log_m, log_r, r12(dp_self_energy_difference(m, R, 2.0 * R)), r12(dp_collapse_time(m, R, 2.0 * R))])
    return {
        "folio_id": "T.06",
        "title": "Does Gravity Collapse the Wave?",
        "model": "Diosi-Penrose: tau = hbar / E_G; E_G = 2 U_self - U_int for two displaced uniform spheres (proposal, not a derivation)",
        "gran_sasso": {"measured": GS_MEASURED, "background": GS_BACKGROUND, "days": GS_DAYS, "a_m3": GS_A_M3,
                       "excess_upper_limit_95": r12(poisson_upper_limit(GS_MEASURED, GS_BACKGROUND, 0.95)),
                       "r0_bound_recomputed_m": r12(gran_sasso_r0_bound(0.95)), "r0_bound_paper_m": GS_R0_BOUND_M,
                       "r0_paramfree_m": GS_R0_PARAMFREE_M, "counts_at_paramfree": r12(gran_sasso_signal_counts(GS_R0_PARAMFREE_M)),
                       "a_recomputed_no_efficiency_m3": r12(dp_rate_prefactor_order_of_magnitude())},
        "xenonnt": {"r0_bound_90_m": XENONNT_R0_90, "r0_bound_95_m": XENONNT_R0_95},
        "sigma_ladder": {k: v for k, v in check_ladder().items() if k not in ("branch_probes",)},
        "table_log10m_kg__log10R_m__E_G_J__tau_s": table,
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t06_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.06",
        "generator": "skills/timegravity/t06/make_t06.py",
        "verifier": "skills/timegravity/t06/verify_t06_collapse_bound.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.06 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
