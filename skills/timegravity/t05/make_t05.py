#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.05 (Does Gravity Entangle, and Would That Settle It?).
Canonical URL: https://informatico.ai/timegravity/t05/
Writes src/research/timegravity/t05/files/t05_reference.json (the four branch phases, entanglement phase, concurrence and
negativity for the 2017 proposal's geometry; a grid over mass, separation and hold time for the quantum and LOCC channels;
the dephasing budget) and manifest.json. Standard library only; reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_dispute import check_dispute  # noqa: E402
from timegravity_kernel_isl import check_isl  # noqa: E402
from timegravity_kernel_wedge import check_wedge  # noqa: E402
from timegravity_kernel_entangle import (  # noqa: E402
    BMV_D_M, BMV_DX_M, BMV_M_KG, BMV_P_PA, BMV_T_S, BMV_TEMP_K, branch_phases, concurrence_closed, disputed_interval,
    entanglement_phase, four_branch_state, negativity, negativity_threshold_gamma_t, time_to_full_entanglement,
)

FILES_DIR = ROOT / "src" / "research" / "timegravity" / "t05" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float | None:
    """12 significant digits; a non-finite value (no entanglement time, no dephasing threshold) becomes null, never an
    `Infinity` token that standard JSON parsers refuse."""
    import math
    return float(f"{x:.12g}") if math.isfinite(x) else None


def clean(x):
    """Round floats to 12 significant digits, recursively; non-finite values become null."""
    if isinstance(x, float):
        return r12(x)
    if isinstance(x, dict):
        return {k: clean(v) for k, v in x.items()}
    if isinstance(x, list):
        return [clean(v) for v in x]
    return x


def dispute_block() -> dict:
    """The computed edges of the disputed channel's band (tools/timegravity_kernel_dispute.py): what each side's own model predicts."""
    r = check_dispute()
    return clean({
        "note": "Trillo-Navascues DP master equation (sigma-smeared, H = 0) and the Kafri-Taylor-Milburn classical channel; "
                "every number is a model's prediction, labelled PROPOSED on the page; the page picks no side",
        "tn_dc_over_sigma": r["tn_dc_over_sigma_e_minus_small_split"], "tn_dc_paper_text": r["tn_dc_paper_text"], "tn_dc_paper_appendix": r["tn_dc_paper_appendix"],
        "tn_fig3": r["tn_fig3"], "tn_potential_ratio_fig3": r["tn_potential_ratio_fig3"],
        "tn_2017_nearest_m": r["tn_2017_nearest_m"], "tn_2017_sigma_c_m": r["tn_2017_sigma_c_m"], "tn_2017_by_sigma": r["tn_2017_by_sigma"],
        "tn_phase_tiny_sigma_rad": r["tn_phase_tiny_sigma_rad"], "newton_phase_rad": r["newton_phase_rad"],
        "ktm_threshold_ratios": r["ktm_threshold_ratios"], "ktm_2017": r["ktm_2017"],
        "entangling_parts": r["entangling_parts"], "quantum_channel_negativity_2017": r["quantum_channel_negativity_2017"],
        "pure_collapse": r["pure_collapse"], "collapse_scaling": r["collapse_scaling"], "threshold_map": r["threshold_map"], "map_with_isl": r["map_with_isl"], "open_region_timing": r["open_region_timing"], "rijavec_tau_g_s": r["rijavec_tau_g_s"], "dephasing_threshold_per_s": r["dephasing_threshold_per_s"],
    })


def isl_block() -> dict:
    """The smeared pull set beside the sub-millimetre inverse-square-law tests (tools/timegravity_kernel_isl.py): one model's
    predicted signal sizes in the plate mode the 2020 Eöt-Wash experiment measures; not a bound on σ."""
    r = check_isl()
    return clean({
        "note": "plate-mode ratio R(q, s; sigma) = 1/2 [erfc(q sigma - s/2sigma) + e^(2qs) erfc(q sigma + s/2sigma)] of Newton's e^(-qs), checked against "
                "quadrature and its limits; Eot-Wash 2020 geometry at the pattern's lowest wavenumber (a one-mode estimate); the Yukawa at the published "
                "edge is a predicted signal size for comparison, not a bound on sigma; HUST 2020 quoted as published; labelled PROPOSED and OPEN on the page",
        "quadrature_probes": r["quadrature_probes"], "limits": r["limits"], "eotwash": r["eotwash"], "hust_lambda_m": r["hust_lambda_m"],
        "hust_pair_level": r["hust_pair_level"],
        "wedge": {k: v for k, v in check_wedge().items() if k not in ("bessel_probes", "radial_probes")},
    })


def build_reference() -> dict:
    q = branch_phases(BMV_M_KG, BMV_D_M, BMV_DX_M, BMV_T_S, "quantum")
    locc = branch_phases(BMV_M_KG, BMV_D_M, BMV_DX_M, BMV_T_S, "locc")
    dphi = entanglement_phase(q)
    grid = []
    for log_m in (-15, -14, -13):
        for d_um in (300, 450, 900):
            for t_s in (0.5, 2.5, 25.0):
                m = 10.0 ** log_m
                pq = branch_phases(m, d_um * 1e-6, BMV_DX_M, t_s, "quantum")
                pl = branch_phases(m, d_um * 1e-6, BMV_DX_M, t_s, "locc")
                grid.append([log_m, d_um, t_s, r12(entanglement_phase(pq)), r12(concurrence_closed(entanglement_phase(pq))),
                             r12(concurrence_closed(entanglement_phase(pl)))])
    return {
        "folio_id": "T.05",
        "title": "Does Gravity Entangle, and Would That Settle It?",
        "model": "Bose-Marletto-Vedral four-branch phases phi_ij = G m^2 t / (hbar d_ij); delta phi = phi_LR + phi_RL - phi_LL - phi_RR; "
                 "concurrence |sin(delta phi / 2)|; Peres negativity under local dephasing exp(-gamma t); three channels at equal weight",
        "geometry_2017": {"m_kg": BMV_M_KG, "d_m": BMV_D_M, "dx_m": BMV_DX_M, "t_s": BMV_T_S, "pressure_pa": BMV_P_PA, "internal_temperature_k": BMV_TEMP_K},
        "quantum_channel": {"phases_rad": {k: r12(v) for k, v in q.items()}, "entanglement_phase_rad": r12(dphi),
                            "concurrence": r12(concurrence_closed(dphi)), "negativity": r12(negativity(four_branch_state(q))),
                            "time_to_full_entanglement_s": r12(time_to_full_entanglement(BMV_M_KG, BMV_D_M, BMV_DX_M)),
                            "gamma_t_at_which_negativity_vanishes": r12(negativity_threshold_gamma_t(q))},
        "locc_channel": {"phases_rad": {k: r12(v) for k, v in locc.items()}, "entanglement_phase_rad": r12(entanglement_phase(locc)),
                         "concurrence": r12(concurrence_closed(entanglement_phase(locc)))},
        "disputed_channel": {"concurrence_interval": [r12(x) for x in disputed_interval(BMV_M_KG, BMV_D_M, BMV_DX_M, BMV_T_S)],
                             "note": "no single prediction: the 2025 literature disagrees; the page carries the interval and the label OPEN"},
        "grid_log10m_kg__d_um__t_s__dphi_rad__C_quantum__C_locc": grid,
        "dispute_kernel": dispute_block(),
        "smeared_isl_kernel": isl_block(),
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t05_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.05",
        "generator": "skills/timegravity/t05/make_t05.py",
        "verifier": "skills/timegravity/t05/verify_t05_entanglement_channels.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.05 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
