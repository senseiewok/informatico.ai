#!/usr/bin/env python3
"""Run all 79 standalone Informatico.ai Folio, Bounty, Toolbox, Time and Gravity & Cross-Scale Essay Python verifiers (48 Pillar Folios + 6 Bounty Folios + 6 Tech & Tools Folios + 16 Time & Gravity + 3 Cross-Scale Essays) and confirm 79/79 PASS."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> int:
    verifiers = sorted(ROOT.glob("*/*/verify_*.py"))
    if len(verifiers) != 79:
        print(f"FAIL: expected 79 verifiers (48 Folios + 6 Bounties + 6 Tech & Tools + 16 Time & Gravity + 3 Cross-Scale Essays), found {len(verifiers)}", file=sys.stderr)
        return 1
    for v in verifiers:
        res = subprocess.run([sys.executable, "-X", "utf8", str(v)], capture_output=True, text=True, encoding="utf-8", timeout=60)
        if res.returncode != 0:
            print(f"FAIL: {v} exited with {res.returncode}:\n{res.stderr}", file=sys.stderr)
            return 1
        payload = json.loads(res.stdout)
        if payload.get("status") != "PASS":
            print(f"FAIL: {v} status={payload.get('status')}", file=sys.stderr)
            return 1
    print(f"PASS: All {len(verifiers)}/79 standalone Folio, Bounty, Toolbox, Time and Gravity & Cross-Scale Essay Python verifiers passed deterministic checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
