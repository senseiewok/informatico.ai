#!/usr/bin/env python3
"""Deterministic Dedekind Frobenius cycle-type verifier for Folio M.15 (SAIR IGP24).

Executes exact finite-field polynomial distinct-degree factorization in F_p[x] for
f(x) = x^4 - x - 1 (discriminant -283, Galois group S_4 over Q) across the first 50
unramified primes p != 283, checking that 4-cycles, 3-cycles, and transpositions
all occur (generating S_4 of order 24) and that observed 4-cycle density aligns with
Chebotarev's 6/24 = 0.25 expectation. Passing --planted-defect substitutes Frobenius
exponent p * d for p^d, breaking distinct-degree factorization.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter


def poly_mod(a: list[int], p: int) -> list[int]:
    out = [c % p for c in a]
    while out and out[-1] == 0:
        out.pop()
    return out


def poly_sub(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    res = [((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p for i in range(n)]
    return poly_mod(res, p)


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    if not a or not b:
        return []
    res = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            res[i + j] = (res[i + j] + ca * cb) % p
    return poly_mod(res, p)


def poly_divmod(a: list[int], b: list[int], p: int) -> tuple[list[int], list[int]]:
    a = poly_mod(a, p)
    b = poly_mod(b, p)
    inv_lead = pow(b[-1], -1, p)
    q = [0] * max(1, len(a) - len(b) + 1)
    r = list(a)
    while len(r) >= len(b):
        deg = len(r) - len(b)
        coef = (r[-1] * inv_lead) % p
        q[deg] = coef
        for i, cb in enumerate(b):
            r[deg + i] = (r[deg + i] - coef * cb) % p
        r = poly_mod(r, p)
    return poly_mod(q, p), r


def poly_gcd(a: list[int], b: list[int], p: int) -> list[int]:
    while b:
        _, r = poly_divmod(a, b, p)
        a, b = b, r
    if a:
        inv_lead = pow(a[-1], -1, p)
        a = [(c * inv_lead) % p for c in a]
    return a


def poly_powmod(base: list[int], exp: int, modp: list[int], p: int) -> list[int]:
    res = [1]
    cur = poly_divmod(base, modp, p)[1]
    while exp > 0:
        if exp & 1:
            res = poly_divmod(poly_mul(res, cur, p), modp, p)[1]
        cur = poly_divmod(poly_mul(cur, cur, p), modp, p)[1]
        exp >>= 1
    return res


def frobenius_cycle_type(p: int, defect: bool = False) -> tuple[int, ...]:
    """Distinct-degree factorization of x^4 - x - 1 over F_p."""
    f = [-1 % p, -1 % p, 0, 0, 1]
    x_poly = [0, 1]
    degrees: list[int] = []
    h = list(x_poly)
    for d in range(1, 5):
        if defect:
            # Corrupted exponent p * d rather than iterative p-th power composition x^(p^d).
            h = poly_powmod(x_poly, p * d, f, p)
        else:
            h = poly_powmod(h, p, f, p)
        g = poly_gcd(poly_sub(h, x_poly, p), f, p)
        if len(g) > 1:
            deg_g = len(g) - 1
            if deg_g % d != 0:
                return ()
            mult = deg_g // d
            degrees.extend([d] * mult)
            f, _ = poly_divmod(f, g, p)
    if sum(degrees) != 4:
        return ()
    return tuple(sorted(degrees, reverse=True))


def first_unramified_primes(count: int = 50, ramified: int = 283) -> list[int]:
    primes: list[int] = []
    cand = 2
    while len(primes) < count:
        if cand != ramified and all(cand % d != 0 for d in range(2, int(cand**0.5) + 1)):
            primes.append(cand)
        cand += 1
    return primes


def verify(prime_count: int = 50, planted_defect: bool = False) -> tuple[bool, dict[str, object]]:
    # For depressed quartic x^4 + p x + q: disc = 256 q^3 - 27 p^4.
    disc = 256 * ((-1) ** 3) - 27 * ((-1) ** 4)
    primes = first_unramified_primes(count=prime_count, ramified=abs(disc))
    tally: Counter[str] = Counter()
    invalid_factorizations = 0
    for pr in primes:
        ct = frobenius_cycle_type(pr, defect=planted_defect)
        if not ct:
            invalid_factorizations += 1
        else:
            tally[str(ct)] += 1

    has_4_cycle = tally.get("(4,)", 0) > 0
    has_3_cycle = tally.get("(3, 1)", 0) > 0
    has_2_cycle = tally.get("(2, 1, 1)", 0) > 0
    obs_4cycle_share = tally.get("(4,)", 0) / float(prime_count)
    chebotarev_close = abs(obs_4cycle_share - 0.25) <= 0.10

    ok = (
        disc == -283
        and invalid_factorizations == 0
        and has_4_cycle
        and has_3_cycle
        and has_2_cycle
        and chebotarev_close
    )

    payload: dict[str, object] = {
        "folio_id": "M.15",
        "status": "PASS" if ok else "FAIL",
        "polynomial": "x^4 - x - 1",
        "discriminant": disc,
        "unramified_primes_sampled": prime_count,
        "invalid_factorizations": invalid_factorizations,
        "cycle_type_counts": dict(tally),
        "observed_4cycle_share": round(obs_4cycle_share, 4),
        "chebotarev_expected_4cycle_share": 0.25,
        "generates_s4": has_4_cycle and has_3_cycle and has_2_cycle,
        "planted_defect": planted_defect,
    }
    return ok, payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify Dedekind Frobenius cycle types for x^4 - x - 1 (Folio M.15).")
    parser.add_argument("--primes", type=int, default=50, help="Unramified primes to sample (default: 50)")
    parser.add_argument("--planted-defect", action="store_true", help="Substitute p*d for Frobenius power p^d.")
    args = parser.parse_args(argv)

    ok, payload = verify(prime_count=args.primes, planted_defect=args.planted_defect)
    print(json.dumps(payload, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
