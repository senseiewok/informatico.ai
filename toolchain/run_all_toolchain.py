#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-command runner for Tech & Tools · The Toolbox (X.01–X.06).

Executes all 6 deterministic Python generators (make_x01.py..make_x06.py),
all 6 byte-level verifiers (verify_x01..verify_x06), and the toolchain claim gate.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    steps = [
        [sys.executable, str(ROOT / "tools" / "toolchain_uga.py"), "--verify"],
        [sys.executable, str(ROOT / "tools" / "check_toolchain_claims.py")],
    ]
    for slug in ("x01", "x02", "x03", "x04", "x05", "x06"):
        tdir = ROOT / "skills" / "toolchain" / slug
        steps.append([sys.executable, str(tdir / f"make_{slug}.py")])
        for vpath in sorted(tdir.glob("verify_*.py")):
            steps.append([sys.executable, str(vpath)])

    for cmd in steps:
        res = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
        if res.returncode != 0:
            print(f"FAIL: {' '.join(cmd)}\n{res.stdout}\n{res.stderr}", file=sys.stderr)
            return res.returncode
        for line in res.stdout.strip().splitlines():
            print(line)

    print("PASS: All 6 Tech & Tools (The Toolbox) generators, byte-level verifiers, and claim gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
