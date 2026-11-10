#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-command runner for Time & Gravity (T.00 hub + shipped pages).

Runs the generator and verifier of every shipped page (verify_t0x_*.py, then --planted-defect which must fail),
the ledger-driven label lint (then its --planted-defect, which must fail), and the offline citation gate.
"""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
SLUGS = ("t01", "t02", "t03", "t04", "t05", "t06", "t07", "t08", "t09", "t10", "t11", "t12")


def run(cmd: list[str], must_fail: bool = False) -> int:
    res = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, encoding="utf-8")
    if must_fail:
        if res.returncode == 0 or "FAIL" not in res.stderr:
            print(f"FAIL (expected a rejection): {' '.join(cmd)}\n{res.stdout}\n{res.stderr}", file=sys.stderr)
            return 1
        script = next((Path(c).name for c in cmd if c.endswith(".py")), cmd[-1])
        print(f"REJECTED_AS_EXPECTED: {script} --planted-defect")
        return 0
    if res.returncode != 0:
        print(f"FAIL: {' '.join(cmd)}\n{res.stdout}\n{res.stderr}", file=sys.stderr)
        return res.returncode
    for line in res.stdout.strip().splitlines():
        if line.startswith(("PASS", "SUMMARY", "REJECTED")) or '"status"' in line:
            print(line.strip())
    return 0


def main() -> int:
    py = [sys.executable, "-X", "utf8"]
    steps: list[tuple[list[str], bool]] = []
    for slug in SLUGS:
        sdir = ROOT / "skills" / "timegravity" / slug
        steps.append((py + [str(sdir / f"make_{slug}.py")], False))
        for v in sorted(sdir.glob("verify_*.py")):
            steps.append((py + [str(v)], False))
            steps.append((py + [str(v), "--planted-defect"], True))
    steps.append((py + [str(ROOT / "tools" / "check_timegravity_labels.py")], False))
    steps.append((py + [str(ROOT / "tools" / "check_timegravity_labels.py"), "--planted-defect"], True))
    steps.append((py + [str(ROOT / "tools" / "check_folio_citations.py"), "--offline"], False))

    for cmd, must_fail in steps:
        rc = run(cmd, must_fail)
        if rc:
            return rc
    print(f"PASS: Time & Gravity: {len(SLUGS)} page generator(s) and verifier(s), both planted defects rejected, label lint and citation gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
