#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for the T.05 smeared-gravity kernels (Does Gravity Entangle, and Would That Settle It?).
Canonical URL: https://informatico.ai/timegravity/t05/
Central numbers: in the Diósi–Penrose model as Trillo & Navascués write it the pair potential is G m₁m₂ erf(d/2σ)/d; between two
patterned plates each in-plane mode of wavenumber q then pulls as R(q, s; σ) = ½[erfc(qσ − s/2σ) + e^{2qs} erfc(qσ + s/2σ)] of
Newton's e^{−qs}, a closed form checked against direct quadrature (1e-9), its four limits and monotone fall with q. On the full
2020 Eöt-Wash wedge geometry (120 wedges between 13.004 and 22.998 mm, 18 between 23.505 and 26.000 mm, 50 % duty, platinum foils
54 and 99 µm against glue of 1.162 g/cm³, from Lee's 2020 dissertation) and with the collaboration's own Fourier–Bessel expansion
(Lee et al. 2021), rebuilt here with stdlib Bessel functions checked against their integral representation (1e-9) and a radial
series checked against quadrature (1e-6): the Newtonian 120-fold torque is 1.51 fN·m at 72 µm (the letter's "roughly 1 %"
magnetic subtraction of 0.0165 fN·m implies about 1.6); the smeared potential removes 17.0 % of it at 52 µm for σ = 75 µm (4.3 %
at 50 µm, 0.3 % at 30 µm, 6.3 % at the 55 µm that first entangles the letter's own geometry), 0.1 % at 300 µm; the Yukawa at the
published 95 % edge (α = −1, λ = 38.6 µm) removes 2.5 %; a smearing of 44 µm matches that edge at the single 52 µm separation (the
one-mode lower bound at the pattern's lowest wavenumber gave 10.4 % and the same 44 µm), a reading retired in favour of the recast of
the published limits over the full pattern (verify_t05_recast.py: σ above 33 µm excluded at 95 %); the Yukawa shape closest to the
σ = 75 µm curve has λ ≈ 49 µm and α ≈ −3.1. With σ at most 33 µm the model entangles only nearest separations below 27 µm (small
split) or 6 µm (23 µm split), and never the letter's own geometry. Two predicted signal sizes side by side; the experiment's own fit
is not recomputed here.
Planted defects (`--planted-defect`): the plate-mode closed form drops its e^{2qs} erfc term, and the radial Bessel series keeps a
fixed 250 terms whatever k; the quadrature double entries then disagree and the run must exit non-zero with FAIL on stderr.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_isl import EW_YUKAWA_EDGE_LAMBDA_M, HUST_LAMBDA_M, ISL_TOL, check_isl  # noqa: E402
from timegravity_kernel_wedge import WEDGE_TOL, check_wedge  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t05" / "files"


def verify_reference_block() -> dict:
    ref = json.loads((FILES_DIR / "t05_reference.json").read_text(encoding="utf-8"))
    block = ref.get("smeared_isl_kernel")
    assert block, "t05_reference.json has no smeared_isl_kernel block; run make_t05.py"
    ew = block["eotwash"]
    assert abs(ew["deficit_at_s_min_by_sigma"]["75um"]["120fold"] - 0.1037) < 2e-3, "reference one-mode σ = 75 µm deficit off"
    wd = block.get("wedge")
    assert wd, "t05_reference.json has no wedge block; run make_t05.py"
    assert abs(wd["deficit_at_52um_by_sigma"]["75um"]["120fold"] - 0.1699) < 3e-3, "reference full-pattern σ = 75 µm deficit off"
    assert abs(wd["sigma_matching_edge_120fold_m"] * 1e6 - 44.1) < 0.5, "reference matching σ off"
    return {"one_mode_deficit_75um_120fold": ew["deficit_at_s_min_by_sigma"]["75um"]["120fold"],
            "wedge_deficit_75um_120fold": wd["deficit_at_52um_by_sigma"]["75um"]["120fold"], "sigma_matching_edge_m": wd["sigma_matching_edge_120fold_m"]}


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_isl(planted_defect=planted)
        assert res["quad_ok"], (
            "the closed-form plate-mode ratio disagrees with direct quadrature: "
            + "; ".join(f"q={p['q_per_m']:.0f} s={p['s_m'] * 1e6:.0f}um σ={p['sigma_m'] * 1e6:.0f}um closed {p['closed']:.6f} vs quadrature {p['quadrature']:.6f}" for p in res["quadrature_probes"])
            + f" (tolerance {ISL_TOL}; with the e^(2qs) erfc term dropped the ratio no longer tends to Newton's)"
        )
        assert res["limits_ok"], f"the plate-mode ratio's limits are wrong: {res['limits']}"
        assert res["monotone_ok"], "the plate-mode ratio does not fall monotonically with q, so the outer-edge wavenumber would not bound the harmonic's deficit"
        assert res["ew_ok"], "the one-mode Eöt-Wash mapping does not reproduce: σ = 75 µm must exceed the published Yukawa edge's deficit and σ = 30 µm must not; the matching σ must lie between 20 and 75 µm; the best-fit Yukawa must lie beyond the published λ with α < −1"
        assert res["defect_rejected"], "the planted dropped-term defect was not detectable"
        wd = check_wedge(planted_defect=planted)
        assert wd["bessel_ok"], "the stdlib Bessel functions disagree with the integral representation: " + "; ".join(f"J_{b['n']}({b['x']}) {b['recurrence']:.6e} vs {b['integral']:.6e}" for b in wd["bessel_probes"])
        assert wd["radial_ok"], (
            "the radial Bessel series disagrees with direct quadrature of ρ J_m(kρ): "
            + "; ".join(f"{r['n_fold']}-fold k={r['k_per_m']:.0f} series {r['series']:.4e} vs quadrature {r['quadrature']:.4e}" for r in wd["radial_probes"] if r["rel_diff"] > WEDGE_TOL)
            + " (a series truncated at a fixed 250 terms stops converging once k·r₁ exceeds the order)"
        )
        assert wd["newton_ok"], f"the Newtonian 120-fold torque at 72 µm, {wd['newton_torques']['72um']['T120_fNm']:.3f} fN·m, is not within 30 % of the {wd['t120_at_72um_implied_by_letter_fNm']} fN·m the letter implies"
        assert wd["wedge_ok"], "the full-pattern mapping does not reproduce: σ = 75 µm must exceed the Yukawa edge's deficit and σ = 30 µm must not; the matching σ must lie between 30 and 60 µm; the mimic Yukawa must lie beyond the published λ with α < −1"
        assert wd["window_ok"], "the window at the matching σ is wrong: the letter's geometry must not entangle and d_c must stay below 0.86 σ"
        assert wd["defect_rejected"], "the planted fixed-truncation defect was not detectable"
        ref = verify_reference_block()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.05", "error": str(exc)}), file=sys.stderr)
        return 1
    ew = res["eotwash"]
    win = wd["window_at_matching_sigma"]
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.05",
        "canonical_url": "https://informatico.ai/timegravity/t05/",
        "central_number": {
            "plate_mode_closed_vs_quadrature_max_diff": max(abs(p["diff"]) for p in res["quadrature_probes"]),
            "one_mode_eotwash_deficit_at_52um_by_sigma": {k: v["120fold"] for k, v in ew["deficit_at_s_min_by_sigma"].items()},
            "one_mode_yukawa_edge_deficit_120fold": ew["yukawa_edge_deficit_alpha_minus_1_lambda_38p6um"]["120fold"],
            "one_mode_sigma_matching_edge_120fold_m": ew["sigma_matching_edge_120fold_m"],
            "bessel_max_abs_diff": max(abs(b["recurrence"] - b["integral"]) for b in wd["bessel_probes"]),
            "radial_series_max_rel_diff": max(r["rel_diff"] for r in wd["radial_probes"]),
            "newton_torque_fNm": wd["newton_torques"],
            "t120_at_72um_implied_by_letter_fNm": wd["t120_at_72um_implied_by_letter_fNm"],
            "wedge_deficit_at_52um_by_sigma": {k: v["120fold"] for k, v in wd["deficit_at_52um_by_sigma"].items()},
            "wedge_18fold_deficit_at_52um_sigma_75um": wd["deficit_at_52um_by_sigma"]["75um"]["18fold"],
            "wedge_yukawa_edge_deficit_120fold": wd["yukawa_edge_deficit_at_52um"]["120fold"],
            "wedge_deficit_sigma_75um_by_separation": {k: v["sigma_75um_120fold"] for k, v in wd["deficit_by_separation"].items()},
            "wedge_sigma_matching_edge_120fold_m": wd["sigma_matching_edge_120fold_m"],
            "wedge_best_yukawa_for_sigma_75um_120fold": {"lambda_m": wd["best_yukawa_for_sigma_75um_120fold"]["lambda_m"], "alpha": wd["best_yukawa_for_sigma_75um_120fold"]["alpha"]},
            "wedge_ratio_sigma_75um_to_edge_120fold": wd["ratio_sigma_75um_to_edge_120fold"],
            "eotwash_yukawa_edge_lambda_m": EW_YUKAWA_EDGE_LAMBDA_M,
            "sigma_c_letter_geometry_m": ew["sigma_c_letter_geometry_m"],
            "window_at_matching_sigma": {"sigma_m": win["sigma_m"], "d_c_small_split_m": win["d_c_small_split_m"], "d_c_letter_split_m": win["d_c_letter_split_m"],
                                         "letter_geometry_entangles": win["letter_geometry"]["last_entangled_time_s"] is not None,
                                         "examples": {k: {"d_c_m": v["d_c_m"], "peak_negativity_at_half_d_c": v["at_half_d_c"]["peak_negativity"], "peak_time_s": v["at_half_d_c"]["peak_time_s"]} for k, v in win["examples"].items()}},
            "hust_lambda_m_as_published": HUST_LAMBDA_M,
            "hust_pair_level": res["hust_pair_level"],
        },
        "geometry_checks": {
            "closed_form_vs_quadrature": "PASS",
            "limits_newton_and_erfc": "PASS",
            "monotone_in_wavenumber": "PASS",
            "one_mode_eotwash_mapping": "PASS",
            "bessel_vs_integral_representation": "PASS",
            "radial_series_vs_quadrature": "PASS",
            "newton_torque_vs_letter": "PASS",
            "full_wedge_pattern_mapping": "PASS",
            "model_window": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
        },
        "reference_block": ref,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
