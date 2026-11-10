#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for the T.05 dispute kernel (Does Gravity Entangle, and Would That Settle It?).
Canonical URL: https://informatico.ai/timegravity/t05/
Central numbers: in the Diósi–Penrose model as Trillo & Navascués write it (mass density smeared over σ, H = 0), the dynamics
entangles two masses only when their nearest separation is below d_c = 0.8509 σ (their appendix: 0.850872 σ; here the analytic
criterion E_− and the master equation's Peres negativity agree within 1 %); for their Fig. 3 geometry (10⁻¹⁵ kg, split 23 µm,
separation 24 µm) nothing is entangled at σ = 50 µm, and at σ = 75, 100 and 250 µm the entanglement is transient and lasts about
5 h, 16 h and 20 days; for the 2017 geometry (split 250 µm, nearest 200 µm) the model needs σ above 525 µm and shows less than
10⁻³ of negativity at 2.5 s. For σ → 0 the model's phases are the Newtonian ones of the T.05 kernel (1e-6). The classical channel
of Kafri, Taylor and Milburn adds dephasing K Δx²/(2ħ) per mass; the T.05 kernel's threshold γt_zero equals it in the small-split
limit (1 %), and the channel's own linearised model entangles nothing. Planted defect: the model's decoherence dropped while its
phases are kept; the critical separation then disappears (the channel entangles at every distance) and `--planted-defect` must
exit non-zero with FAIL on stderr. Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_dispute import DISPUTE_TOL, TN_DC_OVER_SIGMA_APPENDIX, check_dispute  # noqa: E402

FILES_DIR = ROOT / "src" / "research" / "timegravity" / "t05" / "files"


def verify_reference_block() -> dict:
    ref = json.loads((FILES_DIR / "t05_reference.json").read_text(encoding="utf-8"))
    block = ref.get("dispute_kernel")
    assert block, "t05_reference.json has no dispute_kernel block; run make_t05.py"
    assert abs(block["tn_dc_over_sigma"] - TN_DC_OVER_SIGMA_APPENDIX) / TN_DC_OVER_SIGMA_APPENDIX < DISPUTE_TOL, "reference d_c/σ off"
    assert block["tn_fig3"]["50um"]["last_entangled_time_s"] is None, "reference says σ = 50 µm entangles"
    return {"tn_dc_over_sigma": block["tn_dc_over_sigma"], "sigma_c_2017_m": block["tn_2017_sigma_c_m"]}


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_dispute(planted_defect=planted)
        assert res["dc_paper_ok"], f"critical separation {res['tn_dc_over_sigma_e_minus_small_split']} σ is not the paper's {TN_DC_OVER_SIGMA_APPENDIX} σ within {DISPUTE_TOL}"
        assert res["dc_double_entry_ok"], (
            "the master equation's negativity and the analytic criterion E_− disagree on the critical separation: "
            f"negativity {res['tn_dc_negativity_split_sigma_over_500']} vs E_− {res['tn_dc_e_minus_split_sigma_over_500']} "
            "(with the decoherence dropped there is no critical separation at all: the channel entangles everywhere)"
        )
        assert res["fig3_ok"], "the Fig. 3 geometry does not reproduce: no entanglement at σ = 50 µm, transient otherwise, longer than a day at 250 µm"
        assert res["tn_2017_ok"], "the 2017 geometry does not reproduce: none below σ_c, some above, Newtonian phases as σ → 0, < 1e-3 at 2.5 s"
        assert res["ktm_ok"], f"the T.05 dephasing threshold is not the Kafri–Taylor–Milburn minimal rate in the small-split limit: ratios {[round(r['ratio'], 4) for r in res['ktm_threshold_ratios']]}"
        assert res["ktm_edge_ok"], f"the classical channel's own linearised model entangles: negativity {res['ktm_2017']['linear_model_negativity']}"
        assert res["parts_ok"], ("the decomposition of the model's generator fails: the noise part alone must entangle nothing, the interaction part alone "
                                 "must give at least the full negativity, and at σ = 1 nm the interaction part must be the quantum channel")
        assert res["collapse_ok"], "pure Diósi–Penrose collapse against the quantum channel does not reproduce: no entanglement at σ = 100 µm, some at 500 µm, the quantum value at 1 mm, and the letter geometry's critical σ below the 2017 geometry's"
        assert res["scaling_ok"], "the collapse threshold does not scale as expected: insensitive to mass and hold time within 2 %, roughly linear in the geometry's size"
        assert res["rijavec_ok"], f"this page's dephasing threshold {res['dephasing_threshold_per_s']:.4f} /s is not the 2021 study's 1/τ_G = {1 / res['rijavec_tau_g_s']:.4f} /s within 2 %"
        assert res["map_ok"], "the geometry map is not as expected: both thresholds mass-independent, hybrid above collapse everywhere, both monotone in the ratio, 2017 point recovered"
        assert res["isl_ok"], "the map read with the 2020 data is not as expected: whole torque removed at the 2017 threshold, 2-3x the edge at the letter's, estimate at the edge, window above the 1e-15 kg floor only"
        assert res["timing_ok"], "the open-region timing is not as expected: hybrid negativity below 2e-3 at the quantum channel's full-entanglement time, peak 10-200x later and below 0.06"
        assert res["points_ok"], "the planar branch kernels do not reproduce the collinear 1-D kernels"
        assert res["parallel_ok"], "the side-by-side thresholds are not as expected (hybrid about 0.65 of the gap, collapse about 0.44)"
        assert res["proposals_ok"], "the published proposals on the map are not as expected (see check_dispute 4h)"
        assert res["decoh_ok"], "the decoherence comparison at the 2024 geometry is not as expected (quantum threshold = |omega_ent| to a part in ten thousand, hybrid thresholds 40-300x lower, nothing from the hybrid at 1e-3 /s)"
        assert res["defect_rejected"], "the planted decoherence-free channel was not detectable"
        ref = verify_reference_block()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.05", "error": str(exc)}), file=sys.stderr)
        return 1
    f3 = res["tn_fig3"]
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.05",
        "canonical_url": "https://informatico.ai/timegravity/t05/",
        "central_number": {
            "tn_dc_over_sigma": res["tn_dc_over_sigma_e_minus_small_split"], "tn_dc_paper_appendix": TN_DC_OVER_SIGMA_APPENDIX,
            "tn_fig3_last_entangled_time_s": {k: v["last_entangled_time_s"] for k, v in f3.items()},
            "tn_fig3_potential_over_newton": res["tn_potential_ratio_fig3"],
            "tn_2017_sigma_c_m": res["tn_2017_sigma_c_m"],
            "tn_2017_negativity_at_2p5_s_twice_sigma_c": res["tn_2017_by_sigma"]["twice_sigma_c"]["negativity_at_2p5_s"],
            "ktm_threshold_ratio_small_split": res["ktm_threshold_ratios"][-1]["ratio"],
            "ktm_2017_linear_model_negativity": res["ktm_2017"]["linear_model_negativity"],
            "ktm_2017_exact_phases_with_ktm_dephasing_negativity": res["ktm_2017"]["exact_phases_with_ktm_dephasing_negativity"],
            "entangling_parts": res["entangling_parts"], "quantum_channel_negativity_2017": res["quantum_channel_negativity_2017"],
            "pure_collapse": {k: {"critical_sigma_m": v["critical_sigma_m"], "half_sigma_m": v["half_sigma_m"], "quantum_negativity": v["quantum_negativity"]} for k, v in res["pure_collapse"].items()},
            "threshold_map": res["threshold_map"], "map_with_isl": res["map_with_isl"], "open_region_timing": res["open_region_timing"], "parallel_map": res["parallel_map"], "proposals": res["proposals"], "open_window_decoherence": res["open_window_decoherence"], "collapse_scaling": res["collapse_scaling"], "rijavec_tau_g_s": res["rijavec_tau_g_s"], "dephasing_threshold_per_s": res["dephasing_threshold_per_s"],
        },
        "geometry_checks": {
            "critical_separation_matches_paper": "PASS",
            "e_minus_vs_master_equation_double_entry": "PASS",
            "fig3_geometry_reproduced": "PASS",
            "ktm_minimal_rate_is_the_threshold": "PASS",
            "entangling_power_in_the_interaction_part": "PASS",
            "pure_collapse_critical_sigma": "PASS",
            "collapse_threshold_scaling_and_2021_cross_check": "PASS",
            "geometry_map_two_thresholds": "PASS",
            "map_against_2020_inverse_square_data": "PASS",
            "open_region_time_discriminator": "PASS",
            "planar_branches_parallel_map_and_published_proposals": "PASS",
            "decoherence_at_the_2024_geometry": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
        },
        "reference_block": ref,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
