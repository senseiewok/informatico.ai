#!/usr/bin/env python3
"""Deterministic kernel reduction benchmark for Folio M.13: SAIR Lean Kernel Challenge.

Compares O(log n) binary fast-doubling modular Fibonacci reduction against an O(n)
iterative Peano-step reference for n = 1024 modulo 1_000_000_007, checking recursion
depth, multiplication step budget, and value identity. Passing --planted-defect
corrupts the fast-doubling recurrence sign so the reduced value diverges from the
linear reference.
"""
from __future__ import annotations

import argparse
import json
import sys


MOD = 1_000_000_007


def fast_doubling_fib(n: int, mod: int = MOD, defect: bool = False) -> tuple[int, int, dict[str, int]]:
    """Return (F_n mod, F_{n+1} mod, stats) tracking recursion depth and modular muls."""
    stats = {"depth": 0, "muls": 0}

    def _rec(k: int, cur_depth: int) -> tuple[int, int]:
        if cur_depth > stats["depth"]:
            stats["depth"] = cur_depth
        if k == 0:
            return (0, 1)
        a, b = _rec(k >> 1, cur_depth + 1)
        two_b = (2 * b) % mod
        term = (two_b + a) % mod if defect else (two_b - a) % mod
        c = (a * term) % mod
        d = ((a * a) + (b * b)) % mod
        stats["muls"] += 3
        if k & 1:
            return (d, (c + d) % mod)
        return (c, d)

    fn, fn1 = _rec(n, 1)
    return fn, fn1, stats


def linear_peano_fib(n: int, mod: int = MOD) -> tuple[int, int]:
    """O(n) unary successor reference computing F_n mod."""
    a, b = 0, 1
    steps = 0
    for _ in range(n):
        a, b = b, (a + b) % mod
        steps += 1
    return a, steps


def verify(n: int = 1024, planted_defect: bool = False) -> tuple[bool, dict[str, object]]:
    fast_val, _, stats = fast_doubling_fib(n=n, mod=MOD, defect=planted_defect)
    ref_val, peano_steps = linear_peano_fib(n=n, mod=MOD)

    matches_reference = fast_val == ref_val
    depth_ok = stats["depth"] == n.bit_length() + 1
    muls_ok = stats["muls"] <= 3 * n.bit_length()
    ok = matches_reference and depth_ok and muls_ok

    payload: dict[str, object] = {
        "folio_id": "M.13",
        "status": "PASS" if ok else "FAIL",
        "n": n,
        "mod": MOD,
        "fast_doubling_value": fast_val,
        "linear_reference_value": ref_val,
        "matches_reference": matches_reference,
        "recursion_depth": stats["depth"],
        "modular_multiplications": stats["muls"],
        "unary_peano_steps": peano_steps,
        "step_speedup_ratio": round(peano_steps / max(1, stats["muls"]), 2),
        "planted_defect": planted_defect,
    }
    return ok, payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify binary reflection vs unary Peano reduction for Folio M.13.")
    parser.add_argument("--n", type=int, default=1024, help="Fibonacci index (default: 1024)")
    parser.add_argument("--planted-defect", action="store_true", help="Corrupt fast-doubling recurrence sign.")
    args = parser.parse_args(argv)

    ok, payload = verify(n=args.n, planted_defect=args.planted_defect)
    print(json.dumps(payload, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
