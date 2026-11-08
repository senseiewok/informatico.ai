#!/usr/bin/env python3
"""BOUNTY-M1 Benchmark Harness — Erdős Sidon B_2 Sets (Golomb Rulers) & Lean 4 Formalization Invariants."""
from __future__ import annotations

import json
import math
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def mian_chowla_sidon(limit_n: int) -> list[int]:
    sidon: list[int] = []
    pairwise_sums: set[int] = set()
    for candidate in range(1, limit_n + 1):
        new_sums = {candidate + s for s in sidon} | {2 * candidate}
        if new_sums.isdisjoint(pairwise_sums):
            sidon.append(candidate)
            pairwise_sums |= new_sums
    return sidon


def verify_sidon_b2(elements: list[int]) -> bool:
    seen: dict[int, tuple[int, int]] = {}
    for i, a in enumerate(elements):
        for j in range(i, len(elements)):
            s = a + elements[j]
            if s in seen:
                return False
            seen[s] = (a, elements[j])
    return True


def main() -> int:
    n = 500
    sidon = mian_chowla_sidon(n)
    is_valid = verify_sidon_b2(sidon)
    erdos_turan_bound = math.sqrt(n) + (n ** 0.25) + 1.0
    verdict = "PASS" if (is_valid and len(sidon) <= erdos_turan_bound) else "FAIL"
    report = {
        "bounty_id": "BOUNTY-M1",
        "N": n,
        "mian_chowla_cardinality": len(sidon),
        "erdos_turan_upper_bound": round(erdos_turan_bound, 4),
        "pairwise_sums_unique": is_valid,
        "verdict": verdict,
    }
    if "--json" in sys.argv:
        print(json.dumps(report, indent=2))
    else:
        print(f"[BOUNTY-M1] N={n}: |A|={len(sidon)} <= Erdős-Turán bound {erdos_turan_bound:.2f} · Unique sums={is_valid} · {verdict}")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
