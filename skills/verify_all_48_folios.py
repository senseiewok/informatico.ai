#!/usr/bin/env python3
"""Run all 48 standalone Informatico.ai Folio Python verifiers and confirm 48/48 PASS."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> int:
    verifiers = sorted(ROOT.glob("*/*/verify_*.py"))
    if len(verifiers) != 48:
        print(f"FAIL: expected 48 verifiers, found {len(verifiers)}", file=sys.stderr)
        return 1
    for v in verifiers:
        res = subprocess.run([sys.executable, "-X", "utf8", str(v)], capture_output=True, text=True, encoding="utf-8", timeout=15)
        if res.returncode != 0:
            print(f"FAIL: {v} exited with {res.returncode}:\n{res.stderr}", file=sys.stderr)
            return 1
        payload = json.loads(res.stdout)
        if payload.get("status") != "PASS":
            print(f"FAIL: {v} status={payload.get('status')}", file=sys.stderr)
            return 1
    print(f"PASS: All {len(verifiers)}/48 standalone Folio Python verifiers passed deterministic checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
