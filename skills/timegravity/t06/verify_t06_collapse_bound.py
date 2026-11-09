#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.06 (Does Gravity Collapse the Wave?).
Canonical URL: https://informatico.ai/timegravity/t06/
Central number: from the Gran Sasso counts (576 measured, 506 background, 62 days) and the paper's rate constant
z_s = a/R0³, a ≈ 1.8e-29 m³, the 95 % lower bound on R0 recomputes to 0.545e-10 m, within 20 % (actually 2 %) of the
published 0.54e-10 m; the parameter-free R0 = 0.05e-10 m would have produced about 1.4e5 photons and is excluded;
E_G for two displaced uniform spheres agrees with a direct numerical integration within 1e-3. Planted defect: the
bound drawn on the wrong side (small R0 treated as allowed); `--planted-defect` must exit non-zero with FAIL on stderr.
The σ ladder (tools/timegravity_kernel_ladder.py): one tubulin a nucleon radius apart lives 6.5e8 s at σ = 1e-14 m (2.6e10 tubulins for
25 ms) and 5.5e37 s at 44 µm; the Casimir floor of Van De Kamp et al. is 17.1 µm at 1e-15 kg; the σ³ law holds between the top rungs;
its planted defect (the small-displacement series dropped) breaks that law and `--planted-defect` must exit non-zero.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_bounds import DP_TOL, GS_R0_BOUND_M, check_dp  # noqa: E402
from timegravity_kernel_ladder import check_ladder  # noqa: E402

FILES_DIR = ROOT / "src" / "research" / "timegravity" / "t06" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t06_reference.json").read_text(encoding="utf-8"))
    assert abs(ref["gran_sasso"]["r0_bound_recomputed_m"] - GS_R0_BOUND_M) / GS_R0_BOUND_M < 0.2, "reference bound off"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_dp(planted_defect=planted)
        assert res["double_entry_ok"], f"E_G closed form vs quadrature differ by {res['max_rel_err_interaction_energy']:.2e} (> {DP_TOL})"
        assert res["limits_ok"], "E_G limits (6/5 G M^2/R at large d, 0 at d = 0) not recovered"
        assert res["bound_ok"], f"recomputed R0 bound {res['r0_bound_recomputed_m']:.3e} m is not within 20% of {GS_R0_BOUND_M:.2e} m"
        assert res["a_within_decade"], f"rate prefactor {res['a_recomputed_no_efficiency_m3']:.2e} not within a decade of the paper's {res['a_paper_m3']:.2e}"
        assert res["paramfree_excluded"], (
            "the parameter-free R0 = 0.05e-10 m is treated as allowed: the bound is drawn on the wrong side "
            f"(it would have produced {res['counts_at_paramfree_r0']:.2e} photons against an excess limit of {res['excess_upper_limit_counts']:.0f})"
        )
        assert res["xenonnt_consistent"], "the XENONnT bound does not sit on the allowed side above Gran Sasso's"
        assert res["defect_rejected"], "planted bound inversion was accepted"
        lad = check_ladder(planted_defect=planted)
        assert lad["branch_ok"], "the point-mass gap series disagrees with the direct difference where both are accurate"
        assert lad["positive_ok"] and lad["monotone_ok"], "tubulin lifetimes are not positive and increasing along the ladder"
        assert lad["count_ok"], f"tubulins for 25 ms at the natural cut-off, {lad['tubulins_for_25ms_at_natural_cutoff']:.2e}, not within 1e10 … 1e11"
        assert lad["span_ok"], "the lifetime span from the natural cut-off to the laboratory rung is not above 1e20"
        assert lad["rung_ok"], f"the ladder's Eöt-Wash rung {lad['eotwash_matching_sigma_live_m']:.3e} m does not match the wedge kernel within 1 %"
        assert lad["floor_ok"], f"the Casimir floor {lad['casimir']['floor_1e-15_m'] * 1e6:.1f} µm is not between 15 and 20 µm or the proposal's 24 µm does not clear it"
        assert lad["window_ok"], "the window at the matching σ is not closed for the 23 µm split and open for 10 and 1 µm"
        assert lad["scaling_ok"], f"the σ³ law between the top rungs fails: ratio {lad['sigma_cubed_ratio']:.4g} vs {lad['sigma_cubed_ratio_expected']:.4g} (the small-displacement series dropped returns rounding noise)"
        assert lad["defect_rejected"], "the planted series-dropped defect was not detectable"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.06", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.06",
        "canonical_url": "https://informatico.ai/timegravity/t06/",
        "central_number": {"ladder_tubulins_for_25ms_at_natural_cutoff": lad["tubulins_for_25ms_at_natural_cutoff"], "ladder_tubulin_lifetime_at_44um_s": lad["tubulin"]["eotwash"]["nucleon_radius"]["lifetime_s"], "ladder_casimir_floor_1e-15_m": lad["casimir"]["floor_1e-15_m"], "ladder_casimir_floor_1e-14_m": lad["casimir"]["floor_1e-14_m"], "ladder_window_23um_split_open": lad["window"]["by_mass"]["1e-15"]["splits"]["split_23um"]["open"], "ladder_window_10um_split_open": lad["window"]["by_mass"]["1e-15"]["splits"]["split_10um"]["open"], "ladder_sigma_cubed_ratio": lad["sigma_cubed_ratio"], "r0_bound_recomputed_m": res["r0_bound_recomputed_m"], "r0_bound_paper_m": res["r0_bound_paper_m"],
                           "excess_upper_limit_counts_95": res["excess_upper_limit_counts"], "counts_at_paramfree_r0": res["counts_at_paramfree_r0"],
                           "tau_1um_1e-14kg_2R_s": res["tau_1um_1e-14kg_2R_s"], "max_rel_err_E_G": res["max_rel_err_interaction_energy"]},
        "geometry_checks": {"sigma_ladder_tubulin_and_casimir_floor": "PASS", "sigma_cubed_law": "PASS", 
            "E_G_closed_form_vs_quadrature": "PASS",
            "bound_recomputed_from_counts": "PASS",
            "paramfree_value_excluded": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
