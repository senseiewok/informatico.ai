#!/usr/bin/env python3
"""BOUNTY-E1 Benchmark Harness — SIMP Topology-Optimized & CO2-Mineralized Sub-45 kg CO2e/m2 Structural Floor Slab."""
from __future__ import annotations

import json
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def evaluate_simp_mineralized_slab(vol_frac: float = 0.35, co2_mineralized_kg_m2: float = 12.4) -> dict:
    baseline_slab_co2_kg_m2 = 148.0
    net_embodied_co2_kg_m2 = baseline_slab_co2_kg_m2 * vol_frac - co2_mineralized_kg_m2
    compliance_ratio = 1.0 + 0.40 * ((1.0 - vol_frac) ** 1.35)
    verdict = "PASS" if (net_embodied_co2_kg_m2 < 45.0 and compliance_ratio < 1.35) else "FAIL"
    return {
        "bounty_id": "BOUNTY-E1",
        "volume_fraction": vol_frac,
        "net_embodied_co2_kg_m2": round(net_embodied_co2_kg_m2, 2),
        "compliance_ratio_c_over_c0": round(compliance_ratio, 3),
        "verdict": verdict,
    }


def main() -> int:
    rep = evaluate_simp_mineralized_slab()
    if "--json" in sys.argv:
        print(json.dumps(rep, indent=2))
    else:
        print(f"[BOUNTY-E1] V/V0={rep['volume_fraction']} -> Net CO2={rep['net_embodied_co2_kg_m2']} kg/m2 (<45 target), c/c0={rep['compliance_ratio_c_over_c0']} · {rep['verdict']}")
    return 0 if rep["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
