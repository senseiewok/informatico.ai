#!/usr/bin/env python3
"""BOUNTY-P1 Benchmark Harness — Surface-Code Quantum Error Correction & FeMoCo Nitrogenase Resource Estimator."""
from __future__ import annotations

import json
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def estimate_femoco_surface_code(p_phys: float = 0.001, distance: int = 27, p_th: float = 0.01) -> dict:
    exponent = (distance + 1) // 2
    p_logical_per_round = 0.03 * ((p_phys / p_th) ** exponent)
    total_logical_tiles = 114 + 180
    total_physical_qubits = total_logical_tiles * 2 * (distance ** 2)
    verdict = "PASS" if (p_phys < p_th and p_logical_per_round < 1e-12) else "FAIL"
    return {
        "bounty_id": "BOUNTY-P1",
        "code_distance_d": distance,
        "p_phys": p_phys,
        "logical_error_per_round": p_logical_per_round,
        "total_physical_qubits": total_physical_qubits,
        "verdict": verdict,
    }


def main() -> int:
    rep = estimate_femoco_surface_code()
    if "--json" in sys.argv:
        print(json.dumps(rep, indent=2))
    else:
        print(f"[BOUNTY-P1] d={rep['code_distance_d']}, p_phys={rep['p_phys']} -> P_L={rep['logical_error_per_round']:.2e}, Q_phys={rep['total_physical_qubits']:,} · {rep['verdict']}")
    return 0 if rep["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
