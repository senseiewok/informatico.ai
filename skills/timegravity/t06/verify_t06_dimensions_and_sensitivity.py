#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Standalone verifier for Time & Gravity Rational SI Dimensional Homogeneity (AH-14),
Parameter Provenance (AH-9), ±25% Perturbation Sensitivity Envelopes (AH-11), and Complex-Step Parity.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_dimensions_sensitivity import run_all_checks  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--planted-defect", action="store_true")
    args = ap.parse_args()
    report = run_all_checks(planted_defect=args.planted_defect)
    if report["status"] != "PASS":
        print(f"FAIL: dimensional/sensitivity gate rejected planted defect: {json.dumps(report)}", file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
