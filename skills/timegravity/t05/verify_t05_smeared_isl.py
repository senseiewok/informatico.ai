#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for the T.05 smeared-gravity kernel (Does Gravity Entangle, and Would That Settle It?).
Canonical URL: https://informatico.ai/timegravity/t05/
Central numbers: in the Diósi–Penrose model as Trillo & Navascués write it the pair potential is G m₁m₂ erf(d/2σ)/d; between two
patterned plates each in-plane mode of wavenumber q then pulls as R(q, s; σ) = ½[erfc(qσ − s/2σ) + e^{2qs} erfc(qσ + s/2σ)] of
Newton's e^{−qs}, a closed form checked here against direct quadrature (1e-9), against its four limits (σ → 0, s ≫ σ, q → 0 give
Newton; s = 0 gives erfc(qσ)) and for monotone fall with q. Mapped onto the 2020 Eöt-Wash geometry (platinum plates 54 and 99 µm
thick, hole patterns 52 mm across with 18- and 120-fold symmetry, separations 52 µm to 3.0 mm), the 120-fold mode at the lowest
wavenumber the pattern allows loses at least 10 % of its Newtonian torque at 52 µm for σ = 75 µm, 2.5 % for σ = 50 µm, 0.2 % for
σ = 30 µm, and 3.7 % at the smallest σ (55 µm) that entangles the letter's own geometry; the Yukawa at the published 95 % edge
(α = −1, λ = 38.6 µm) loses 1.5 % in the same mode at the same separation; a smearing of 44 µm matches that edge; the Yukawa that
best mimics the σ = 75 µm curve has λ ≈ 49 µm and α ≈ −3.2. The experiment's own fit is not recomputed; the page says so.
Planted defect: the closed form drops its e^{2qs} erfc(qσ + s/2σ) term; the limits and the quadrature double entry then disagree
and `--planted-defect` must exit non-zero with FAIL on stderr. Boundary: Nothing on this page is a theory of everything, and this
site proposes none.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_isl import EW_YUKAWA_EDGE_LAMBDA_M, HUST_LAMBDA_M, ISL_TOL, check_isl  # noqa: E402

FILES_DIR = ROOT / "src" / "research" / "timegravity" / "t05" / "files"


def verify_reference_block() -> dict:
    ref = json.loads((FILES_DIR / "t05_reference.json").read_text(encoding="utf-8"))
    block = ref.get("smeared_isl_kernel")
    assert block, "t05_reference.json has no smeared_isl_kernel block; run make_t05.py"
    ew = block["eotwash"]
    assert abs(ew["deficit_at_s_min_by_sigma"]["75um"]["120fold"] - 0.1037) < 2e-3, "reference σ = 75 µm deficit off"
    assert abs(ew["sigma_matching_edge_120fold_m"] * 1e6 - 44.4) < 0.5, "reference matching σ off"
    return {"deficit_75um_120fold": ew["deficit_at_s_min_by_sigma"]["75um"]["120fold"], "sigma_matching_edge_m": ew["sigma_matching_edge_120fold_m"]}


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
        assert res["ew_ok"], "the Eöt-Wash mapping does not reproduce: σ = 75 µm must exceed the published Yukawa edge's deficit and σ = 30 µm must not; the matching σ must lie between 20 and 75 µm; the best-fit Yukawa must lie beyond the published λ with α < −1"
        assert res["defect_rejected"], "the planted dropped-term defect was not detectable"
        ref = verify_reference_block()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.05", "error": str(exc)}), file=sys.stderr)
        return 1
    ew = res["eotwash"]
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.05",
        "canonical_url": "https://informatico.ai/timegravity/t05/",
        "central_number": {
            "plate_mode_closed_vs_quadrature_max_diff": max(abs(p["diff"]) for p in res["quadrature_probes"]),
            "eotwash_deficit_at_52um_by_sigma": {k: v["120fold"] for k, v in ew["deficit_at_s_min_by_sigma"].items()},
            "eotwash_18fold_deficit_at_52um_sigma_75um": ew["deficit_at_s_min_by_sigma"]["75um"]["18fold"],
            "eotwash_yukawa_edge_deficit_120fold": ew["yukawa_edge_deficit_alpha_minus_1_lambda_38p6um"]["120fold"],
            "eotwash_yukawa_edge_lambda_m": EW_YUKAWA_EDGE_LAMBDA_M,
            "ratio_sigma_75um_to_edge_120fold": ew["ratio_sigma_75um_to_edge_120fold"],
            "sigma_matching_edge_120fold_m": ew["sigma_matching_edge_120fold_m"],
            "best_yukawa_for_sigma_75um_120fold": {"lambda_m": ew["best_yukawa_for_sigma_75um_120fold"]["lambda_m"], "alpha": ew["best_yukawa_for_sigma_75um_120fold"]["alpha"]},
            "sigma_c_letter_geometry_m": ew["sigma_c_letter_geometry_m"],
            "deficit_120fold_at_sigma_c_letter_geometry": ew["deficit_120fold_at_sigma_c_letter_geometry"],
            "deficit_120fold_sigma_75um_at_300um": ew["deficit_120fold_sigma_75um_by_separation"]["300um"],
            "hust_lambda_m_as_published": HUST_LAMBDA_M,
        },
        "geometry_checks": {
            "closed_form_vs_quadrature": "PASS",
            "limits_newton_and_erfc": "PASS",
            "monotone_in_wavenumber": "PASS",
            "eotwash_mapping": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
        },
        "reference_block": ref,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
