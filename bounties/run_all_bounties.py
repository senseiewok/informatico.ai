#!/usr/bin/env python3
"""Run all 6 Council-selected Open-Bounty, Symbolic Physics & Formal Math Crucible benchmark harnesses."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent


def main() -> int:
    scripts = [
        "bounty_m1_erdos_sidon_lean4.py",
        "bounty_p1_surface_code_femoco.py",
        "bounty_e1_simp_carbon_slab.py",
        "bounty_a1_graphic_statics_sky_cooling.py",
        "bounty_p2_pysr_pysindy_pde_discovery.py",
        "bounty_m2_physlean_itensor_quantum_gauge.py",
    ]
    for s in scripts:
        res = subprocess.run(
            [sys.executable, "-X", "utf8", str(ROOT / s)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=15,
        )
        if res.returncode != 0:
            print(res.stdout + res.stderr, file=sys.stderr)
            return 1
        print(res.stdout.strip())
    print("PASS: 6/6 Open-Bounty & Physics/Math Discovery Crucible benchmarks verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
