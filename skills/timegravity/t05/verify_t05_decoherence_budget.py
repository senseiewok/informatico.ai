#!/usr/bin/env python3
"""T.05 · Decoherence-budget verifier: the page's single dephasing rate as residual gas and thermal photons, and the ceilings it implies.

Checks (tools/timegravity_kernel_decoherence.py): the closed-form identities (the proposals' cited gas form = λ_th² Λ; cited form over
the kinetic collision rate = 8π/3; van de Kamp et al. 2020 Eq. 33 = the cited form through the ideal-gas law); the regimes for every
2024 geometry (gas wavelength under 1 % of the split, photon wavelength over ten splits at the highest temperature ceiling, sphere far
above the gas wavelength and far below the photon wavelength, gas rate saturated); the transcription checks against printed statements,
with windows no wider than the statements (Bose et al. 2017: 10⁻¹⁵ Pa and 0.15 K give a collisional time within a factor of two of the
3.5 s fall on the cited form; Rijavec et al. 2021: 1/τ_G ≃ 0.06 s⁻¹, the photon forms reach it below 4 K and are about a factor of two
stricter in rate at 4 K, the cited gas rate at 10⁻¹⁶ Pa is an order below it; van de Kamp et al. 2020: 'O(1) K'); the ceilings on the
kinetic rate and on the cited form (pressure falls by the full ratio of the two channels' thresholds; with cold surroundings the internal
temperature falls by its sixth root and a decade in diamond's absorption moves it by 10^{1/6}; with warm surroundings it does not); the
helium ceilings beside the antiproton-trap helium limit; and the handed-in estimate (1.6 × 10⁻¹⁷ Pa and 1.6 × 10⁻¹⁵ Pa on the kinetic rate).
These checks reproduce the papers' formulas; they validate no physics. Planted defect: the gas rate left in its long-wavelength form
ΛΔx² outside its regime; `--planted-defect` must exit 1 with FAIL on stderr."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_decoherence import check_decoherence  # noqa: E402


def main() -> int:
    planted = "--planted-defect" in sys.argv
    try:
        res = check_decoherence(planted_defect=planted)
        assert res["identity_ok"], "a closed-form identity failed (cited form = λ_th² Λ, the 8π/3 ratio or Eq. 33)"
        assert res["regime_ok"], "a regime check failed: the gas rate is not the saturated one, or a wavelength condition is not met"
        assert res["transcription_ok"], "a transcription check against a printed statement failed (Bose 2017, Rijavec 2021 or van de Kamp 2020)"
        assert res["ceilings_ok"], "the pressure or temperature ceilings, or their comparison with the trap limit, are not as expected"
        assert res["estimate_ok"], "the handed-in estimate on the kinetic rate is not reproduced"
        z10 = res["budgets"]["schut2024_z10"]
        out = {
            "status": "PASS", "folio_id": "T.05",
            "central_number": {
                "geometry": "schut2024_z10", "rates_per_s": z10["rates_per_s"],
                "pressure_ceiling_pa": z10["pressure_ceiling_pa"], "number_density_ceiling_per_m3": z10["number_density_ceiling_per_m3"],
                "temperature_ceiling_k": z10["temperature_ceiling_k"],
                "rate_ratio_quantum_over_hybrid_33um": res["rate_ratio_quantum_over_hybrid_33um"],
                "gas_rate_per_pa_at_4K_1e-14kg_per_s": res["gas_rate_per_pa_at_4K_1e-14kg_per_s"],
                "base_partial_pressure_pa": res["base_partial_pressure_pa"], "vacuum_comparison_helium": res["vacuum_comparison_helium"], "hydrogen_over_helium_rate_at_equal_pressure": res["hydrogen_over_helium_rate_at_equal_pressure"],
                "transcription_checks": res["transcription_checks"], "estimate": res["estimate"],
                "other_geometries": {k: {"rates_per_s": b["rates_per_s"], "pressure_ceiling_pa": b["pressure_ceiling_pa"],
                                         "number_density_ceiling_per_m3": b["number_density_ceiling_per_m3"],
                                         "temperature_ceiling_k": b["temperature_ceiling_k"], "regime": b["regime"]}
                                     for k, b in res["budgets"].items() if k != "schut2024_z10"}},
            "geometry_checks": {"closed_form_identities": "PASS", "regimes_checked_before_use": "PASS", "transcription_checks_against_print": "PASS",
                                "pressure_by_ratio_temperature_by_sixth_root_cold_surroundings": "PASS", "helium_ceilings_beside_trap_limit": "PASS",
                                "handed_in_estimate_reproduced": "PASS", "planted_long_wavelength_gas_form": "run with --planted-defect"},
        }
        print(json.dumps(out, indent=2, default=str))
        return 0
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "T.05", "error": str(exc)}), file=sys.stderr)  # run_all reads FAIL on stderr
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
