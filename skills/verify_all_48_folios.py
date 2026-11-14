#!/usr/bin/env python3
"""Run every standalone verifier under skills/ and refuse any that cannot fail.

A skill is either `verified` (it ships a verify_*.py here) or plain text (it ships none). This
runner discovers the verifiers from disk; it does not expect a fixed number. For each one:

  1. a normal run must exit 0 and print one JSON object with "status": "PASS";
  2. a run with --planted-defect must NOT pass (non-zero exit, or a status other than PASS);
  3. the planted-defect branch must do more than notice the flag: a script whose only reaction to
     the flag is to print or exit is rejected, because it would satisfy rule 2 without computing.

Rule 3 is a floor, not a proof. It catches the cheapest fake (exit when the flag is present). It
does not prove that a defect travels through the real computation; reading the script still does.

The file keeps its historical name because it is referenced widely. It no longer implies that all
48 pillar essays have a verifier: an essay without one is a text skill and is not listed here.

  python skills/verify_all_48_folios.py          run everything
  python skills/verify_all_48_folios.py --list   one line per verifier, no execution
"""
from __future__ import annotations

import ast
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FLAG = "--planted-defect"
TRIVIAL_CALLS = {"print", "exit", "quit", "sys.exit", "SystemExit", "json.dumps", "sys.stderr.write", "sys.stdout.write"}


def discover() -> list[Path]:
    return sorted(ROOT.glob("*/*/verify_*.py"))


def reacts_only_to_the_flag(source: str) -> bool:
    """True when no use of the planted-defect flag reaches a computation.

    The flag reaches a computation when a name bound from it is passed into a call, or when a branch
    on it calls something other than print/exit. A script that only prints or exits under the flag
    is the fake this rule exists to catch.
    """
    tree = ast.parse(source)
    names = {"planted", "planted_defect", "defect"}
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign)) and FLAG in ast.unparse(node):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            names |= {t.id for t in targets if isinstance(t, ast.Name)}
        if isinstance(node, ast.arg) and "planted" in node.arg:
            names.add(node.arg)

    def mentions(n: ast.AST) -> bool:
        text = ast.unparse(n)
        return FLAG in text or any(name in {x.id for x in ast.walk(n) if isinstance(x, ast.Name)} for name in names) \
            or any(isinstance(x, ast.Attribute) and "planted" in x.attr for x in ast.walk(n))

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = ast.unparse(node.func)
            passed = list(node.args) + [k.value for k in node.keywords]
            if func not in TRIVIAL_CALLS and "add_argument" not in func and any(mentions(a) for a in passed):
                return False                      # the flag is handed to a function that is not print/exit
            if any(k.arg and "planted" in k.arg for k in node.keywords) and func not in TRIVIAL_CALLS:
                return False
        if isinstance(node, (ast.If, ast.IfExp)) and mentions(node.test):
            body = node.body if isinstance(node, ast.If) else [node.body]
            calls = {ast.unparse(c.func) for b in body for c in ast.walk(b) if isinstance(c, ast.Call)}
            if calls - TRIVIAL_CALLS:
                return False                      # the branch on the flag computes something
    return True


def run(path: Path, planted: bool) -> tuple[int, str]:
    cmd = [sys.executable, "-X", "utf8", str(path)] + ([FLAG] if planted else [])
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=120)
    status = ""
    try:
        status = str(json.loads(res.stdout).get("status", ""))
    except (json.JSONDecodeError, AttributeError):
        pass
    return res.returncode, status


def check(path: Path) -> str | None:
    """Return None when the verifier is acceptable, else the reason it is not."""
    source = path.read_text(encoding="utf-8")
    if FLAG not in source:
        return "has no --planted-defect mode, so nothing shows it can fail"
    if reacts_only_to_the_flag(source):
        return "its planted-defect mode only prints or exits; the defect never reaches a computation"
    code, status = run(path, planted=False)
    if code != 0 or status != "PASS":
        return f"normal run did not pass (exit {code}, status {status!r})"
    code, status = run(path, planted=True)
    if code == 0 and status == "PASS":
        return "still passes with the planted defect"
    return None


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    verifiers = discover()
    if "--list" in argv:
        for v in verifiers:
            print(v.relative_to(ROOT).as_posix())
        return 0
    if not verifiers:
        print("FAIL: no verifiers found under skills/", file=sys.stderr)
        return 1
    failures = [(v, why) for v in verifiers if (why := check(v))]
    for v, why in failures:
        print(f"FAIL: {v.relative_to(ROOT).as_posix()}: {why}", file=sys.stderr)
    if failures:
        return 1
    groups: dict[str, int] = {}
    for v in verifiers:
        groups[v.relative_to(ROOT).parts[0]] = groups.get(v.relative_to(ROOT).parts[0], 0) + 1
    detail = ", ".join(f"{n} {g}" for g, n in sorted(groups.items()))
    print(f"PASS: {len(verifiers)} verifiers pass and each fails under its planted defect ({detail}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
