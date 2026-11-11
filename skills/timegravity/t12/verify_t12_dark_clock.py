#!/usr/bin/env python3
"""Standalone stdlib verifier and planted-defect knockout for Time & Gravity · T.12 (Two Clocks That Only Meet in Gravity).
Canonical URL: https://informatico.ai/timegravity/t12/
Central number: Planck 2018 cosmic microwave background power spectra fix the dark-to-baryonic matter ratio at
Omega_c / Omega_b = 0.1200 / 0.02237 = 5.3643 (84.29 % of non-relativistic matter); for an electromagnetically
transparent mass M_DM flying past a two-clock network (b_1 = 1 m, baseline d_c = 1000 m, v_0 = 220 km/s),
composite Gauss-Legendre quadrature of the gravitational redshift integral matches the closed-form arsinh expression
-(2 G M_DM / c^2 v_0) [arsinh(v_0 T / b_1) - arsinh(v_0 T / b_2)] within 1e-11 and satisfies the transverse impulse
identity +c^2 d(Delta tau_inf)/db_1 = 2 G M_DM / (b_1 v_0) within 1e-9, while co-located clocks (d_c = 0) see zero
shift under pure gravity (d_e = 0). Planted defect: setting G_dark = 0 for the electromagnetically transparent mass
violates the Equivalence Principle and fails the quadrature check; `--planted-defect` exits non-zero.
Boundary: Nothing on this page is a theory of everything, and this site proposes none.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_dark_clock import DARK_CLOCK_TOL, check_dark_clock  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t12" / "files"


def verify_reference_files() -> dict:
    manifest = json.loads((FILES_DIR / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for entry in manifest["files"]:
        raw = (FILES_DIR / entry["filename"]).read_bytes()
        assert len(raw) == entry["bytes"], f"{entry['filename']}: byte count mismatch"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], f"{entry['filename']}: sha256 mismatch"
        out[entry["filename"]] = digest[:12]
    ref = json.loads((FILES_DIR / "t12_reference.json").read_text(encoding="utf-8"))
    assert ref["gravitational_transit"]["quadrature_rel_err"] < 1e-11, "reference dark-transit quadrature error too large"
    assert ref["ultralight_scalar_bound"]["rho_roundtrip_rel_err"] < DARK_CLOCK_TOL, "reference ULDM energy-density round-trip error"
    return out


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        res = check_dark_clock(planted_defect=planted)
        assert res["cosmo_ok"], f"cosmological dark-to-baryon budget error {res['cosmo_err_propagation_rel_diff']:.3e}"
        assert res["transit_ok"], (
            f"dark-transit proper-time shift misses gravitational trajectory integral (rel_err = {res['quadrature_rel_err']:.3e}); "
            "an electromagnetically transparent mass still curves proper time via G_N"
        )
        assert res["uldm_ok"], f"ultralight scalar clock round-trip error {res['uldm_rho_roundtrip_rel_err']:.3e}"
        assert res["defect_rejected"], "planted zero-gravity dark transit was accepted"
        files = verify_reference_files()
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.12", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "folio_id": "T.12",
        "canonical_url": "https://informatico.ai/timegravity/t12/",
        "central_number": {
            "dark_to_baryon_ratio": res["dark_to_baryon_ratio"],
            "dark_fraction_of_matter": res["dark_fraction_of_matter"],
            "delta_tau_analytic_s": res["delta_tau_analytic_s"],
            "quadrature_rel_err": res["quadrature_rel_err"],
            "impulse_rel_err": res["impulse_rel_err"],
            "uldm_1e15ev_phi_planck": res["uldm_1e15ev_phi_planck"],
            "tolerance": DARK_CLOCK_TOL,
        },
        "geometry_checks": {
            "planck_dark_baryon_budget": "PASS",
            "arsinh_matches_gl5_quadrature": "PASS",
            "transverse_impulse_from_clock_gradient": "PASS",
            "equivalence_principle_zero_baseline": "PASS",
            "uldm_energy_density_roundtrip": "PASS",
            "planted_defect_knockout": "REJECTED_AS_EXPECTED",
            "planted_delta_tau_s": res["planted_delta_tau_s"],
        },
        "reference_files_sha256_12": files,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
