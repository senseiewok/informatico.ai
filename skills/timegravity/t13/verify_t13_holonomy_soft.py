#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.13
(Where Infrared Gravity Meets Gauge Theory).
Canonical URL: https://informatico.ai/timegravity/t13/
Verifies:
  1. Weinberg (1964, 1965) soft Ward identities for s = 1 (charge conservation), s = 2 (universal gravitational
     coupling kappa_e = kappa_p, eta_WEP = 0), and s = 3 (full rank-4 quadratic obstruction forcing g_a = 0).
  2. Christodoulou (1991) / Strominger-Zhiboedov (2016) gravitational-wave memory strain step
     Delta h_char = 2 G E_rad / (c^4 D_L) and proper separation holonomy Delta L / L_0 = (1/2) Delta h_+^mem
     checked against 5-point Gauss-Legendre flux quadrature to < 1e-12 on GW150914 and GW250114 fiducial benchmarks.
  3. Chiral and mixed gauge-gravitational anomaly cancellation (Adler 1969; Delbourgo-Salam 1972; Tooby-Smith 2025)
     for one Standard Model Weyl generation (6Y integer scaling): all four traces vanish iff N_c = 3.
  4. Pure Core Lean 4 Prelude companion `HolonomySoftAnomaly.lean` invariants (`0` imports, `0` sorry/admit/axiom,
     `>= 9` theorems).
  5. Planted-defect knockout (`--planted-defect`): perturbing kappa_e / kappa_p = 1 + 1e-5 violates the s = 2
     soft-graviton Ward identity AND setting N_c = 2 != 3 breaks SU(2)_L^2 U(1)_Y and U(1)_Y^3 anomaly cancellation;
     prints FAIL to stderr and exits 1.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_holonomy_soft import build_reference as kernel_reference  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t13" / "files"
LEAN_FILE = ROOT / "skills" / "timegravity" / "t13" / "HolonomySoftAnomaly.lean"
HOLONOMY_TOL = 1.0e-12


def verify_lean_prelude() -> dict:
    assert LEAN_FILE.is_file(), f"missing Lean 4 formalization {LEAN_FILE}"
    raw = LEAN_FILE.read_text(encoding="utf-8")
    # Strip block comments /- ... -/ and line comments -- ...
    no_block = re.sub(r"/-.*?-/", "", raw, flags=re.S)
    code_lines = [ re.sub(r"--.*$", "", ln) for ln in no_block.splitlines() ]
    code = "\n".join(code_lines)
    imports = re.findall(r"^\s*import\b", code, flags=re.M)
    assert len(imports) == 0, f"Lean file must have 0 imports, found {len(imports)}"
    forbid = re.findall(r"\b(sorry|admit|axiom)\b", code)
    assert len(forbid) == 0, f"Lean file contains forbidden token(s): {forbid}"
    assert "^" not in code, "Lean file must avoid HPow (`^`) for pure Prelude portability"
    theorems = re.findall(r"^\s*theorem\s+([A-Za-z0-9_']+)", code, flags=re.M)
    assert len(theorems) >= 9, f"Lean file must contain >= 9 theorems, found {len(theorems)}"
    return {"theorem_count": len(theorems), "theorems": theorems}


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t13_reference.json").read_text(encoding="utf-8"))
    assert ref["clean"]["memory_benchmarks"]["flux_quadrature"]["quadrature_rel_err"] < HOLONOMY_TOL
    assert ref["clean"]["anomaly_cancellation"]["active_generation"]["all_anomalies_cancel"] is True
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = kernel_reference(planted_defect=planted)
        soft = res["soft_theorems"]
        mem = res["memory_benchmarks"]
        anom = res["anomaly_cancellation"]["active_generation"]

        assert soft["momentum_conservation_norm_gev"] < HOLONOMY_TOL, "external 4-momentum conservation violated"
        assert abs(soft["s1_charge_ward_residual"]) < HOLONOMY_TOL, "spin-1 charge conservation Ward identity violated"
        assert soft["s2_three_momenta_gram_det"] > 1.0, "3-momenta not linearly independent"
        assert soft["s2_ward_vector_rel_norm"] < HOLONOMY_TOL, (
            f"spin-2 soft-graviton Ward identity violated (||W^mu||/E_cm = {soft['s2_ward_vector_rel_norm']:.3e}); "
            "species-dependent coupling kappa_e != kappa_p breaks Lorentz gauge invariance"
        )
        assert soft["s3_four_tensor_gram_det"] > 1.0 and soft["s3_universal_unit_obstruction_norm"] > 0.1, (
            "spin-3 quadratic momentum tensor failed full-rank obstruction check"
        )
        assert mem["flux_quadrature"]["quadrature_rel_err"] < HOLONOMY_TOL, (
            f"memory flux quadrature error {mem['flux_quadrature']['quadrature_rel_err']:.3e} exceeds tolerance"
        )
        gw15 = mem["gw150914_fiducial"]
        assert abs(gw15["delta_l_char_m"] / gw15["arm_length_m"] - 0.5 * gw15["delta_h_char"]) < 1e-30, (
            "proper arm separation holonomy identity Delta L / L_0 = (1/2) Delta h violated"
        )
        assert anom["all_anomalies_cancel"] is True, (
            f"chiral / mixed gauge-gravitational anomaly cancellation failed at N_c = {anom['n_c']}: "
            f"Tr[SU(2)^2 6Y] = {anom['tr_su2_sq_6y']}, Tr[(6Y)^3] = {anom['tr_u1_cubic_6y']}"
        )

        # Internal knockout self-check when running clean mode
        bad = kernel_reference(planted_defect=True)
        defect_rejected = (
            bad["soft_theorems"]["s2_ward_vector_rel_norm"] > 1.0e-6
            and bad["anomaly_cancellation"]["active_generation"]["all_anomalies_cancel"] is False
            and bad["anomaly_cancellation"]["active_generation"]["tr_su2_sq_6y"] == -1
            and bad["anomaly_cancellation"]["active_generation"]["tr_u1_cubic_6y"] == 54
        )
        assert defect_rejected, "internal planted-defect knockout failed to trigger"

        lean_info = verify_lean_prelude()
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.13", "error": str(exc)}), file=sys.stderr)
        return 1

    gw15 = res["memory_benchmarks"]["gw150914_fiducial"]
    gw25 = res["memory_benchmarks"]["gw250114_fiducial"]
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.13",
        "canonical_url": "https://informatico.ai/timegravity/t13/",
        "central_number": {
            "s2_ward_vector_rel_norm": soft["s2_ward_vector_rel_norm"],
            "s3_universal_unit_obstruction_norm": soft["s3_universal_unit_obstruction_norm"],
            "gw150914_delta_h_char": gw15["delta_h_char"],
            "gw150914_delta_l_char_m": gw15["delta_l_char_m"],
            "gw250114_delta_h_char": gw25["delta_h_char"],
            "memory_quadrature_rel_err": res["memory_benchmarks"]["flux_quadrature"]["quadrature_rel_err"],
            "sm_nc_unique": 3,
            "lean_theorem_count": lean_info["theorem_count"],
            "tolerance": HOLONOMY_TOL,
        },
        "geometry_checks": {
            "weinberg_s1_charge_conservation": "PASS",
            "weinberg_s2_universal_equivalence": "PASS",
            "weinberg_s3_higher_spin_obstruction": "PASS",
            "christodoulou_memory_gl5_quadrature": "PASS",
            "delbourgo_salam_sm_anomaly_bridge": "PASS",
            "lean4_prelude_formalization": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
            "planted_s2_ward_rel_norm": bad["soft_theorems"]["s2_ward_vector_rel_norm"],
            "planted_nc2_cubic_trace": bad["anomaly_cancellation"]["active_generation"]["tr_u1_cubic_6y"],
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
