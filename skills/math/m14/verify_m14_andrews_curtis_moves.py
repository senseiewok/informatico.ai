#!/usr/bin/env python3
"""Deterministic Andrews-Curtis move verifier for Folio M.14.

Executes a free-group presentation engine over <x, y> supporting the three
Andrews-Curtis moves: relator inversion (INV), relator multiplication (MUL_L/MUL_R),
and free-group conjugation (CONJ). Replays an explicit 23-step elementary AC sequence
reducing Akbulut-Kirby AK(2) = <x, y | x y x = y x y, x^2 = y^3> (total relator length 11)
to <x, y | x, y> (total length 2). Passing --planted-defect drops the inverse on
conjugation (w r w instead of w r w^-1), causing reduction to fail.
"""
from __future__ import annotations

import argparse
import json
import sys

Word = tuple[tuple[str, int], ...]

X: Word = (("x", 1),)
XI: Word = (("x", -1),)
Y: Word = (("y", 1),)
YI: Word = (("y", -1),)

AK2_TRIVIALIZING_TRACE: list[tuple[str, int, Word]] = [
    ("CONJ", 1, YI),
    ("INV", 1, ()),
    ("CONJ", 0, YI),
    ("MUL_R", 1, ()),
    ("CONJ", 1, YI),
    ("MUL_L", 0, ()),
    ("CONJ", 0, YI),
    ("INV", 1, ()),
    ("MUL_R", 0, ()),
    ("CONJ", 0, X),
    ("CONJ", 0, YI),
    ("MUL_L", 1, ()),
    ("CONJ", 0, XI),
    ("INV", 0, ()),
    ("CONJ", 1, YI),
    ("MUL_R", 0, ()),
    ("CONJ", 0, X),
    ("INV", 1, ()),
    ("MUL_R", 1, ()),
    ("MUL_L", 0, ()),
    ("MUL_R", 1, ()),
    ("INV", 0, ()),
    ("INV", 1, ()),
]


def free_reduce(word: Word) -> Word:
    stack: list[tuple[str, int]] = []
    for gen, sign in word:
        if stack and stack[-1][0] == gen and stack[-1][1] == -sign:
            stack.pop()
        else:
            stack.append((gen, sign))
    return tuple(stack)


def invert_word(word: Word) -> Word:
    return tuple((gen, -sign) for gen, sign in reversed(word))


def apply_ac_move(
    relators: list[Word],
    op: str,
    target_idx: int,
    conjugator: Word = (),
    defect: bool = False,
) -> list[Word]:
    out = list(relators)
    other_idx = 1 - target_idx
    if op == "INV":
        out[target_idx] = invert_word(out[target_idx])
    elif op == "MUL_R":
        out[target_idx] = free_reduce(out[target_idx] + out[other_idx])
    elif op == "MUL_L":
        out[target_idx] = free_reduce(out[other_idx] + out[target_idx])
    elif op == "CONJ":
        right_side = conjugator if defect else invert_word(conjugator)
        out[target_idx] = free_reduce(conjugator + out[target_idx] + right_side)
    else:
        raise ValueError(f"Unknown AC move: {op}")
    return out


def ak_presentation(n: int) -> list[Word]:
    r1 = free_reduce(X + Y + X + YI + XI + YI)
    r2 = free_reduce((X * n) + (YI * (n + 1)))
    return [r1, r2]


def abelianization_det(relators: list[Word]) -> int:
    """Compute |det| of 2x2 exponent-sum matrix for <x, y | r1, r2>."""
    rows = []
    for w in relators:
        cx = sum(p for g, p in w if g == "x")
        cy = sum(p for g, p in w if g == "y")
        rows.append((cx, cy))
    return abs(rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0])


def verify(planted_defect: bool = False) -> tuple[bool, dict[str, object]]:
    ak2 = ak_presentation(2)
    ak3 = ak_presentation(3)
    cur = list(ak2)
    max_word_len = len(cur[0]) + len(cur[1])
    for op, idx, conj in AK2_TRIVIALIZING_TRACE:
        cur = apply_ac_move(cur, op, idx, conj, defect=planted_defect)
        max_word_len = max(max_word_len, len(cur[0]) + len(cur[1]))

    trivialized = set(cur) == {X, Y}
    ak2_abel_trivial = abelianization_det(ak2) == 1
    ak3_abel_trivial = abelianization_det(ak3) == 1
    ak2_len = sum(len(r) for r in ak2)
    ak3_len = sum(len(r) for r in ak3)
    ok = trivialized and ak2_abel_trivial and ak3_abel_trivial and (ak2_len == 11) and (ak3_len == 13)

    payload: dict[str, object] = {
        "folio_id": "M.14",
        "status": "PASS" if ok else "FAIL",
        "ak2_initial_length": ak2_len,
        "ak3_initial_length": ak3_len,
        "ak2_abelianization_det": abelianization_det(ak2),
        "ak3_abelianization_det": abelianization_det(ak3),
        "ac_moves_replayed": len(AK2_TRIVIALIZING_TRACE),
        "max_intermediate_length": max_word_len,
        "final_total_length": sum(len(r) for r in cur),
        "reached_trivial_basis": trivialized,
        "planted_defect": planted_defect,
    }
    return ok, payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify explicit AK(2) Andrews-Curtis reduction sequence for Folio M.14.")
    parser.add_argument("--planted-defect", action="store_true", help="Drop inverse on free-group conjugation.")
    args = parser.parse_args(argv)

    ok, payload = verify(planted_defect=args.planted_defect)
    print(json.dumps(payload, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
