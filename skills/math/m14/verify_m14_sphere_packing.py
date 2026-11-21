#!/usr/bin/env python3
"""Deterministic verifier for Folio M.14: Sphere Packing, Cohn-Elkies LP Bounds & E8/Leech Lattices.

Pure Python standard library offline verification (math, fractions, itertools).
Primary mathematical anchors:
  - Rogers (1958, DOI 10.1112/plms/s3-8.4.609)
  - Cohn & Elkies (2003, DOI 10.4007/annals.2003.157.689)
  - Musin (2008, DOI 10.4007/annals.2008.168.1)
  - Viazovska (2017, DOI 10.4007/annals.2017.185.3.7)
  - Cohn, Kumar, Miller, Radchenko & Viazovska (2017, DOI 10.4007/annals.2017.185.3.8)
  - Hales et al. (2017, DOI 10.1017/fmp.2017.1)
  - Cohn, Kumar, Miller, Radchenko & Viazovska (2022, DOI 10.4007/annals.2022.196.3.3)
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from fractions import Fraction


def laguerre_coeffs_exact(k: int, alpha: Fraction) -> list[Fraction]:
    """Exact rational coefficients [c_0, ..., c_k] of generalized Laguerre polynomial L_k^(alpha)(u)."""
    if k == 0:
        return [Fraction(1)]
    if k == 1:
        return [alpha + 1, Fraction(-1)]
    p_prev = [Fraction(1)]
    p_curr = [alpha + 1, Fraction(-1)]
    for j in range(1, k):
        p_next = [Fraction(0)] * (j + 2)
        c1 = Fraction(2 * j + 1) + alpha
        c2 = Fraction(j) + alpha
        denom = Fraction(j + 1)
        for idx, val in enumerate(p_curr):
            p_next[idx] += c1 * val / denom
            p_next[idx + 1] -= val / denom
        for idx, val in enumerate(p_prev):
            p_next[idx] -= c2 * val / denom
        p_prev, p_curr = p_curr, p_next
    return p_curr


def mul_poly_exact(p: list[Fraction], q: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def eval_poly_exact(poly: list[Fraction], u: Fraction) -> Fraction:
    acc = Fraction(0)
    for coef in reversed(poly):
        acc = acc * u + coef
    return acc


def shift_poly_exact(poly: list[Fraction], u0: Fraction) -> list[Fraction]:
    """Expand P(u0 + w) in powers of w using exact Binomial/Horner shift."""
    deg = len(poly) - 1
    out = [Fraction(0)] * (deg + 1)
    for k, coef in enumerate(poly):
        if coef == 0:
            continue
        # coef * (u0 + w)^k
        term = [Fraction(1)]
        lin = [u0, Fraction(1)]
        for _ in range(k):
            term = mul_poly_exact(term, lin)
        for j, tv in enumerate(term):
            out[j] += coef * tv
    return out


def monomial_to_laguerre_exact(poly: list[Fraction], alpha: Fraction) -> list[Fraction]:
    """Express polynomial in exact Laguerre eigenbasis L_0^(alpha) .. L_M^(alpha)."""
    deg = len(poly) - 1
    l_basis = [laguerre_coeffs_exact(k, alpha) + [Fraction(0)] * (deg - k) for k in range(deg + 1)]
    rem = list(poly)
    coeffs = [Fraction(0)] * (deg + 1)
    for k in range(deg, -1, -1):
        c = rem[k] / l_basis[k][k]
        coeffs[k] = c
        for j in range(k + 1):
            rem[j] -= c * l_basis[k][j]
    if any(r != 0 for r in rem):
        raise AssertionError("Non-zero remainder in Laguerre decomposition")
    return coeffs


def laguerre_to_monomial_exact(coeffs: list[Fraction], alpha: Fraction) -> list[Fraction]:
    deg = len(coeffs) - 1
    out = [Fraction(0)] * (deg + 1)
    for k, ck in enumerate(coeffs):
        lk = laguerre_coeffs_exact(k, alpha)
        for j, lv in enumerate(lk):
            out[j] += ck * lv
    return out


def build_phat_factored(alpha_shift: Fraction, double_roots: list[Fraction]) -> list[Fraction]:
    """Construct P_hat(u) = (u + alpha_shift) * prod_j (u - s_j)^2 >= 0 for all u >= 0."""
    poly = [alpha_shift, Fraction(1)]
    for s in double_roots:
        sq = [s * s, Fraction(-2) * s, Fraction(1)]
        poly = mul_poly_exact(poly, sq)
    return poly


def verify_cohn_elkies_bound(
    d: int,
    alpha_shift: Fraction,
    double_roots: list[Fraction],
    planted_defect: bool = False,
) -> dict:
    """Evaluate and check a Laguerre-Gaussian Cohn-Elkies test function in even dimension d.

    Fourier convention: f_hat(t) = int_{R^d} f(x) exp(-2*pi*i x.t) dx.
    Eigenbasis: psi_k(x) = L_k^(d/2 - 1)(2*pi*|x|^2) exp(-pi*|x|^2) has f_hat = (-1)^k psi_k.
    With u = 2*pi*r^2, f_hat(t) >= 0 iff P_hat(u) >= 0 for all u >= 0,
    and f(x) <= 0 for |x| >= r_cut iff P(u) <= 0 for all u >= u_cut = 2*pi*r_cut^2.
    For even d, Vol(B_d(r_cut/2)) = (u_cut / 8)^(d/2) / (d/2)! is strictly rational.
    """
    if d % 2 != 0 or d < 2:
        raise ValueError("Even dimension d >= 2 required for rational Laguerre volume formula")
    alpha = Fraction(d, 2) - 1
    phat_poly = build_phat_factored(alpha_shift, double_roots)
    if planted_defect:
        # Corrupt P_hat by subtracting a constant offset so P_hat(s_1) < 0
        # and pass it through the same admissibility check.
        phat_poly[0] -= Fraction(1, 2) * (alpha_shift + double_roots[0])

    # 1. Check P_hat(u) >= 0 at 0, at all double roots, and on a dense grid [0, 80]
    phat_0 = phat_poly[0]
    if phat_0 <= 0:
        raise ValueError(f"Cohn-Elkies violation in d={d}: P_hat(0)={phat_0} <= 0")
    for s in double_roots:
        val_s = eval_poly_exact(phat_poly, s)
        if val_s < 0:
            raise ValueError(f"Cohn-Elkies dual negativity in d={d}: P_hat({s})={float(val_s)} < 0")
    for grid_i in range(0, 321):
        u_test = Fraction(grid_i, 4)
        if eval_poly_exact(phat_poly, u_test) < 0:
            raise ValueError(f"Cohn-Elkies dual negativity in d={d} at u={u_test}")

    # 2. Convert P_hat to Laguerre basis and apply exact Fourier eigenvalue (-1)^k
    c_hat = monomial_to_laguerre_exact(phat_poly, alpha)
    c_primal = [((-1) ** k) * ck for k, ck in enumerate(c_hat)]
    p_poly = laguerre_to_monomial_exact(c_primal, alpha)

    p_0 = p_poly[0]
    if p_0 <= 0:
        raise ValueError(f"Cohn-Elkies primal violation in d={d}: P(0)={p_0} <= 0")
    if p_poly[-1] >= 0:
        raise ValueError(f"Cohn-Elkies primal tail violation in d={d}: leading coeff {p_poly[-1]} >= 0")

    # 3. Scan for last positive sample and bisect tightly to a rational upper bound u_cut
    step = Fraction(1, 16)
    last_pos = Fraction(0)
    for idx in range(1, 1600):
        u = idx * step
        if eval_poly_exact(p_poly, u) > 0:
            last_pos = u
    u_lo = last_pos
    u_hi = last_pos + step
    while eval_poly_exact(p_poly, u_hi) > 0:
        u_hi += step
    for _ in range(28):
        mid = (u_lo + u_hi) / 2
        if eval_poly_exact(p_poly, mid) > 0:
            u_lo = mid
        else:
            u_hi = mid
    u_cut = u_hi

    # 4. Symbolic Descartes tail check: expand P(u_cut + w) and verify EVERY coefficient <= 0
    shifted = shift_poly_exact(p_poly, u_cut)
    if any(coef > 0 for coef in shifted) or shifted[-1] >= 0:
        raise ValueError(f"Shifted polynomial P(u_cut + w) in d={d} has positive coefficient: {shifted}")

    # 5. Exact rational Cohn-Elkies density upper bound
    half_d = d // 2
    vol_factor = (u_cut / 8) ** half_d / math.factorial(half_d)
    bound_exact = vol_factor * (p_0 / phat_0)
    r_cut = math.sqrt(float(u_cut) / (2.0 * math.pi))
    return {
        "dimension": d,
        "degree": len(phat_poly) - 1,
        "alpha_shift": float(alpha_shift),
        "double_roots_u": [float(s) for s in double_roots],
        "u_cut_approx": round(float(u_cut), 8),
        "r_cut": round(r_cut, 8),
        "p0_over_phat0": round(float(p_0 / phat_0), 8),
        "density_upper_bound": round(float(bound_exact), 8),
        "shifted_nonpositive_checked": True,
    }


def verify_golay_g24_and_leech_kissing() -> dict:
    """Generate all 4,096 codewords of the extended binary Golay code G24 and count Leech minimal vectors."""
    # Canonical 12x12 circulant complement adjacency matrix B_12 (from residues mod 11 + infinity)
    qr11 = {1, 3, 4, 5, 9}
    b_rows: list[int] = []
    # Row 0..10: column 11 is 1; columns 0..10 have 1 iff (j - i) mod 11 not in qr11?
    # Standard construction: S has 0 on diagonal? No: 1 on diagonal and 1 at non-residues, or 0 at residues:
    # Let M_{i,j} = 1 if i == j or (j - i) mod 11 not in qr11; wait: quadratic residue matrix:
    # Standard G_24 matrix [I_12 | A] where A has row 0..10 = cyclic shifts of [0,1,1,1,0,1,1,0,1,0,0]?
    # Wait: let's verify exact self-duality (G * G^T = 0 mod 2) and min weight 8!
    # For Paley-type B_12 of size 12: top-left 11x11 has c_{i,j} = 1 if (j-i)%11 in qr11 else 0, bordered by 1s with 0 in bottom-right!
    # Wait: let's check weight of rows of A: each of first 11 rows has 5 ones in 11x11 + 1 in border = 6, wait 6 + 1 = 7 (odd, not 8)!
    # For self-dual doubly-even G24, each row of A must have weight 7 (so [1 | 7] = 8) or 11!
    # Take complement of Paley 11x11 (weight 11 - 5 = 6 ones, or 0 on diagonal -> 6 ones + 1 in border = 7 ones!).
    for i in range(11):
        row = 0
        for j in range(11):
            diff = (j - i) % 11
            bit = 1 if (diff == 0 or diff not in qr11) else 0
            row |= bit << j
        row |= 1 << 11
        b_rows.append(row)
    # Row 11: [1,1,...,1, 0] (weight 11 -> [1 | 11] = 12!)
    b_rows.append((1 << 11) - 1)

    codewords: list[tuple[int, int]] = [(0, 0)]
    for i in range(12):
        l_bit = 1 << i
        r_bits = b_rows[i]
        new_items = [(lw ^ l_bit, rw ^ r_bits) for lw, rw in codewords]
        codewords.extend(new_items)

    weights: dict[int, int] = {}
    for lw, rw in codewords:
        w = lw.bit_count() + rw.bit_count()
        weights[w] = weights.get(w, 0) + 1

    if weights != {0: 1, 8: 759, 12: 2576, 16: 759, 24: 1}:
        raise AssertionError(f"Invalid G24 weight enumerator: {weights}")

    type_a = 4 * math.comb(24, 2)  # ((±4)^2, 0^22) in (1/sqrt(8)) Z^24 coords, unscaled norm^2 = 32
    type_b = weights[8] * (2 ** 7)  # ((±2)^8, 0^16) on octads with even minus signs
    type_c = 24 * (2 ** 12)  # ((±1)^23, ∓3) aligned with G24 parity
    kissing_24 = type_a + type_b + type_c
    if kissing_24 != 196560:
        raise AssertionError(f"Expected 196560 Leech minimal vectors, got {kissing_24}")
    return {
        "golay_codewords": len(codewords),
        "weight_enumerator": {str(k): v for k, v in sorted(weights.items())},
        "leech_kissing_breakdown": {"type_2sq": type_a, "type_octad": type_b, "type_3_1": type_c},
        "leech_kissing_number": kissing_24,
    }


def verify_root_lattice_kissing() -> dict:
    """Count exact minimal vectors of A2, D3, D4, and E8 by explicit lattice enumeration."""
    # A2: a^2 + ab + b^2 = 1 for a, b in {-1, 0, 1}
    a2_vecs = [(a, b) for a, b in itertools.product((-1, 0, 1), repeat=2) if a * a + a * b + b * b == 1]
    # D3 and D4: integer vectors with sum(x^2) = 2 and sum(x) even
    d3_vecs = [v for v in itertools.product((-1, 0, 1), repeat=3) if sum(x * x for x in v) == 2 and sum(v) % 2 == 0]
    d4_vecs = [v for v in itertools.product((-1, 0, 1), repeat=4) if sum(x * x for x in v) == 2 and sum(v) % 2 == 0]
    # E8: integer vectors of norm^2 = 2 (112) + half-integer (±1/2)^8 with even minus count (128)
    e8_int = 4 * math.comb(8, 2)
    e8_half = sum(1 for bits in itertools.product((-1, 1), repeat=8) if bits.count(-1) % 2 == 0)
    e8_total = e8_int + e8_half
    if (len(a2_vecs), len(d3_vecs), len(d4_vecs), e8_total) != (6, 12, 24, 240):
        raise AssertionError("Kissing number mismatch in A2/D3/D4/E8")
    return {"A2": len(a2_vecs), "D3": len(d3_vecs), "D4": len(d4_vecs), "E8": e8_total}


def run_verification(planted_defect: bool = False) -> dict:
    kissing_low = verify_root_lattice_kissing()
    golay_leech = verify_golay_g24_and_leech_kissing()

    lattices = {
        "d2_A2": {"dimension": 2, "density": round(math.pi / math.sqrt(12.0), 8), "kissing": kissing_low["A2"], "status": "PROVEN_OPTIMAL_FEJES_TOTH"},
        "d3_D3": {"dimension": 3, "density": round(math.pi / (3.0 * math.sqrt(2.0)), 8), "kissing": kissing_low["D3"], "status": "PROVEN_OPTIMAL_HALES_2017"},
        "d4_D4": {"dimension": 4, "density": round((math.pi ** 2) / 16.0, 8), "kissing": kissing_low["D4"], "status": "OPEN_DENSITY_PROVEN_KISSING_MUSIN_2008"},
        "d8_E8": {"dimension": 8, "density": round((math.pi ** 4) / 384.0, 8), "kissing": kissing_low["E8"], "status": "PROVEN_OPTIMAL_VIAZOVSKA_2017"},
        "d24_Leech": {"dimension": 24, "density": round((math.pi ** 12) / math.factorial(12), 8), "kissing": golay_leech["leech_kissing_number"], "status": "PROVEN_OPTIMAL_CKMRV_2017"},
    }

    # Exact rational Laguerre-Gaussian Cohn-Elkies bounds (degree 3 and degree 5)
    bounds = {
        "d4_deg3": verify_cohn_elkies_bound(4, Fraction(7, 4), [Fraction(19, 2)], planted_defect=planted_defect),
        "d4_deg5": verify_cohn_elkies_bound(4, Fraction(3, 2), [Fraction(7), Fraction(37, 2)]),
        "d8_deg3": verify_cohn_elkies_bound(8, Fraction(2), [Fraction(27, 2)]),
        "d8_deg5": verify_cohn_elkies_bound(8, Fraction(2), [Fraction(10), Fraction(22)]),
        "d24_deg3": verify_cohn_elkies_bound(24, Fraction(9, 4), [Fraction(79, 4)]),
        "d24_deg5": verify_cohn_elkies_bound(24, Fraction(2), [Fraction(24), Fraction(40)]),
    }

    # Verify monotonicity and gap relationships
    for d_key, lat_key in [("d4", "d4_D4"), ("d8", "d8_E8"), ("d24", "d24_Leech")]:
        b3 = bounds[f"{d_key}_deg3"]["density_upper_bound"]
        b5 = bounds[f"{d_key}_deg5"]["density_upper_bound"]
        lat_d = lattices[lat_key]["density"]
        if not (b5 < b3 and lat_d < b5):
            raise AssertionError(f"Expected lattice < deg5 < deg3 in {d_key}: {lat_d}, {b5}, {b3}")

    return {
        "status": "PASS",
        "folio_id": "M.14",
        "slug": "m14",
        "planted_defect": planted_defect,
        "lattices": lattices,
        "golay_g24": golay_leech,
        "cohn_elkies_bounds": bounds,
        "d4_deg5_ratio_to_D4": round(bounds["d4_deg5"]["density_upper_bound"] / lattices["d4_D4"]["density"], 6),
        "d8_deg5_ratio_to_E8": round(bounds["d8_deg5"]["density_upper_bound"] / lattices["d8_E8"]["density"], 6),
        "d24_deg5_ratio_to_Leech": round(bounds["d24_deg5"]["density_upper_bound"] / lattices["d24_Leech"]["density"], 6),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Folio M.14 sphere packing & Cohn-Elkies bounds.")
    parser.add_argument("--planted-defect", action="store_true", help="Inject a Fourier dual negativity defect.")
    args = parser.parse_args()
    try:
        report = run_verification(planted_defect=args.planted_defect)
        print(json.dumps(report, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "folio_id": "M.14", "error": str(exc)}, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())
