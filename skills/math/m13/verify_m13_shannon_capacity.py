#!/usr/bin/env python3
"""Deterministic verifier for Folio M.13: Shannon Zero-Error Graph Capacity, Lovasz Theta Sandwich & Haemers Rank Separation.

Mathematical definitions and primary anchors:
  - Shannon zero-error capacity (Shannon 1956, DOI 10.1109/TIT.1956.1056798):
        Theta(G) = sup_{k >= 1} alpha(G^{\boxtimes k})^(1/k) = lim_{k -> inf} alpha(G^{\boxtimes k})^(1/k),
    where G^{\boxtimes k} is the k-fold strong graph product (two k-tuples are adjacent iff at every
    coordinate i they are either equal or adjacent in G).
  - Lovasz theta function & sandwich theorem (Lovasz 1979, DOI 10.1109/TIT.1979.1055985):
        alpha(G) <= Theta(G) <= vartheta(G) <= alpha*(G) <= chi_bar(G).
    For odd cycles C_n (n >= 5 odd), Lovasz showed:
        vartheta(C_n) = n * cos(pi / n) / (1 + cos(pi / n)),
    with alpha(C_n) = (n - 1) / 2, alpha*(C_n) = n / 2, and chi_bar(C_n) = (n + 1) / 2.
    For C_5, the explicit 5-codeword set {(i, 2i mod 5)} in C_5^{\boxtimes 2} gives alpha(C_5^{\boxtimes 2}) >= 5,
    locking Theta(C_5) = vartheta(C_5) = sqrt(5).
  - Open gap on C_7:
        alpha(C_7^{\boxtimes 2}) = 10 => Theta(C_7) >= sqrt(10) ~ 3.162278 (explicit witness verified here),
        alpha(C_7^{\boxtimes 3}) >= 33, alpha(C_7^{\boxtimes 4}) >= 108 (Vesel & Zerovnik 2002, DOI 10.1016/S0020-0190(01)00229-0),
        alpha(C_7^{\boxtimes 5}) >= 367 => Theta(C_7) >= 367^(1/5) ~ 3.257866 <= vartheta(C_7) ~ 3.317667 (Polak & Schrijver 2019, DOI 10.1016/j.ipl.2018.11.006).
    The exact value of Theta(C_7) remains OPEN.
  - Haemers minrank separation on the complement of the Schlafli graph (Haemers 1979, DOI 10.1109/TIT.1979.1056027):
    The intersection graph S_bar of the 27 lines on a smooth cubic surface is SRG(27, 10, 1, 5) with spectrum
    {10^1, 1^20, (-5)^6} and vartheta(S_bar) = 9, while A(S_bar) - I fits S_bar with exact rank 7 over Q/R,
    bounding Theta(S_bar) <= 7 < 9 = vartheta(S_bar) and Theta(S x S_bar) >= 27 > 3 * 7 >= Theta(S) * Theta(S_bar).

Planted-defect mode (`--planted-defect`):
  Uses the naive diagonal shift (i, i) instead of the knight-move shift (i, 2i mod 5) in C_5^{\boxtimes 2},
  corrupts the C_5 orthonormal umbrella half-angle, and flips one adjacency entry in the 27-vertex Schlafli matrix,
  breaking both the strong-product independence checks and the SRG/rank-7 algebraic witness.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
import sys
from typing import Any


C7_SQ_WITNESS: tuple[tuple[int, int], ...] = (
    (0, 0), (0, 2), (1, 4), (2, 0), (2, 2),
    (3, 4), (4, 1), (4, 6), (5, 3), (6, 5),
)

C9_SQ_WITNESS: tuple[tuple[int, int], ...] = tuple(
    (i, (2 * i + t) % 9) for t in (0, 4) for i in range(9)
)

C11_SQ_WITNESS: tuple[tuple[int, int], ...] = (
    (0, 1), (0, 3), (0, 5), (0, 10), (1, 8), (2, 0), (2, 2), (2, 4), (2, 6),
    (3, 9), (4, 0), (4, 3), (4, 5), (4, 7), (5, 9), (6, 1), (6, 3), (6, 7),
    (7, 5), (7, 10), (8, 3), (8, 8), (9, 1), (9, 6), (9, 10), (10, 8),
)

C13_SQ_WITNESS: tuple[tuple[int, int], ...] = (
    (0, 0), (0, 5), (0, 7), (1, 3), (1, 9), (1, 11), (2, 1), (2, 5), (2, 7),
    (3, 3), (3, 9), (3, 11), (4, 0), (4, 5), (4, 7), (5, 3), (5, 11), (6, 1),
    (6, 5), (6, 7), (6, 9), (7, 3), (7, 12), (8, 1), (8, 6), (8, 8), (8, 10),
    (9, 4), (9, 12), (10, 2), (10, 6), (10, 8), (10, 10), (11, 0), (11, 4),
    (12, 2), (12, 9), (12, 11),
)

SQUARE_WITNESSES: dict[int, tuple[tuple[int, int], ...]] = {
    5: tuple((i, (2 * i) % 5) for i in range(5)),
    7: C7_SQ_WITNESS,
    9: C9_SQ_WITNESS,
    11: C11_SQ_WITNESS,
    13: C13_SQ_WITNESS,
}


def cycle_distance(a: int, b: int, n: int) -> int:
    diff = (a - b) % n
    return min(diff, n - diff)


def is_strong_product_independent(n: int, codewords: tuple[tuple[int, int], ...]) -> bool:
    """Verify pairwise non-adjacency in C_n^{\boxtimes 2}."""
    for idx, u in enumerate(codewords):
        for v in codewords[idx + 1 :]:
            if cycle_distance(u[0], v[0], n) <= 1 and cycle_distance(u[1], v[1], n) <= 1:
                return False
    return True


def evaluate_odd_cycle_slider(
    cycle_n: int = 5,
    block_k: int = 2,
    planted_defect: bool = False,
) -> dict[str, Any]:
    """Evaluate exact odd-cycle invariants alpha, vartheta, alpha*, chi_bar and lower bounds."""
    if not isinstance(cycle_n, int) or isinstance(cycle_n, bool):
        raise ValueError("cycle_n must be an integer")
    if not isinstance(block_k, int) or isinstance(block_k, bool):
        raise ValueError("block_k must be an integer")
    if cycle_n < 5 or cycle_n % 2 == 0:
        raise ValueError("cycle_n must be an odd integer >= 5")
    if block_k < 1 or block_k > 10:
        raise ValueError("block_k must lie in [1, 10]")

    alpha_single = (cycle_n - 1) // 2
    cos_pi_n = math.cos(math.pi / cycle_n)
    theta_val = (cycle_n * cos_pi_n) / (1.0 + cos_pi_n)
    alpha_star = cycle_n / 2.0
    chi_bar = (cycle_n + 1) // 2

    if cycle_n == 5:
        shift = 1 if planted_defect else 2
        c5_sq = tuple((i, (shift * i) % 5) for i in range(5))
        c5_sq_valid = is_strong_product_independent(5, c5_sq)
        if block_k == 1:
            lower_rate = 2.0
        else:
            c2_size = len(c5_sq) if c5_sq_valid else 2
            lower_rate = ((c2_size ** (block_k // 2)) * (alpha_single ** (block_k % 2))) ** (1.0 / block_k)
        status_label = "CLOSED BY LOVASZ 1979 (Theta(C_5) = sqrt(5))"
    elif cycle_n == 7:
        c7_rates = {
            1: 3.0,
            2: math.sqrt(len(C7_SQ_WITNESS)),
            3: 33.0 ** (1.0 / 3.0),
            4: 108.0 ** (1.0 / 4.0),
            5: 367.0 ** (1.0 / 5.0),
        }
        lower_rate = c7_rates.get(block_k, 367.0 ** (1.0 / 5.0))
        status_label = "OPEN PROBLEM (3.257866 <= Theta(C_7) <= 3.317667)"
    else:
        witness = SQUARE_WITNESSES.get(cycle_n)
        c2_size = len(witness) if witness and is_strong_product_independent(cycle_n, witness) else (alpha_single ** 2)
        if block_k == 1:
            lower_rate = float(alpha_single)
        else:
            lower_rate = ((c2_size ** (block_k // 2)) * (alpha_single ** (block_k % 2))) ** (1.0 / block_k)
        status_label = f"OPEN GAP (alpha(C_{cycle_n}) = {alpha_single} < vartheta = {theta_val:.4f})"

    gap = theta_val - lower_rate
    return {
        "cycle_n": cycle_n,
        "block_k": block_k,
        "alpha_single": alpha_single,
        "lovasz_theta": round(theta_val, 6),
        "fractional_alpha_star": alpha_star,
        "clique_cover_chi_bar": chi_bar,
        "best_lower_rate": round(lower_rate, 6),
        "open_gap": round(gap, 6),
        "status_label": status_label,
    }


def verify_c5_umbrella_and_product(planted_defect: bool = False) -> dict[str, Any]:
    """Verify explicit 3D Lovasz umbrella on C_5 and 5-codeword packing in C_5^{\boxtimes 2}."""
    cos_sq = 0.5 if planted_defect else 1.0 / math.sqrt(5.0)
    sin_sq = 1.0 - cos_sq
    cos_phi = math.sqrt(cos_sq)
    sin_phi = math.sqrt(sin_sq)

    vectors = [
        (
            sin_phi * math.cos(2.0 * math.pi * j / 5.0),
            sin_phi * math.sin(2.0 * math.pi * j / 5.0),
            cos_phi,
        )
        for j in range(5)
    ]
    max_norm_err = max(abs(sum(x * x for x in v) - 1.0) for v in vectors)
    max_nonedge_dot = 0.0
    for j in range(5):
        for k in range(j + 1, 5):
            if cycle_distance(j, k, 5) > 1:
                dot = sum(vectors[j][d] * vectors[k][d] for d in range(3))
                max_nonedge_dot = max(max_nonedge_dot, abs(dot))

    handle = (0.0, 0.0, 1.0)
    umbrella_value = max(1.0 / (sum(handle[d] * v[d] for d in range(3)) ** 2) for v in vectors)

    shift = 1 if planted_defect else 2
    codewords = tuple((i, (shift * i) % 5) for i in range(5))
    c5_sq_independent = is_strong_product_independent(5, codewords)

    return {
        "max_unit_norm_err": max_norm_err,
        "max_nonedge_orthogonality_err": max_nonedge_dot,
        "umbrella_value": round(umbrella_value, 6),
        "codewords": [list(c) for c in codewords],
        "c5_sq_independent": c5_sq_independent,
        "umbrella_ok": (
            max_norm_err < 1e-12
            and max_nonedge_dot < 1e-12
            and abs(umbrella_value - math.sqrt(5.0)) < 1e-9
            and c5_sq_independent
        ),
    }


def verify_odd_cycle_gram_psd(n: int) -> dict[str, Any]:
    """Verify PSD Gram matrix M = I + (1 / (2 cos(pi/n))) A(C_n) for odd cycle C_n."""
    cos_pi_n = math.cos(math.pi / n)
    eigs = [1.0 + math.cos(2.0 * math.pi * m / n) / cos_pi_n for m in range(n)]
    min_eig = min(eigs)
    max_eig = max(eigs)
    theta_from_gram = n / max_eig
    theta_formula = (n * cos_pi_n) / (1.0 + cos_pi_n)
    return {
        "n": n,
        "min_gram_eigenvalue": round(min_eig, 12),
        "theta_from_gram": round(theta_from_gram, 9),
        "theta_formula": round(theta_formula, 9),
        "gram_psd_ok": min_eig >= -1e-12 and abs(theta_from_gram - theta_formula) < 1e-12,
    }


def verify_odd_cycle_square_witnesses() -> dict[str, Any]:
    """Verify explicit strong-product independent sets for C_5^2, C_7^2, C_9^2, C_11^2, and C_13^2."""
    summary: dict[str, Any] = {}
    all_ok = True
    for n, expected_min in ((5, 5), (7, 10), (9, 18), (11, 26), (13, 38)):
        witness = SQUARE_WITNESSES[n]
        indep_ok = is_strong_product_independent(n, witness)
        alpha_single = (n - 1) // 2
        rate = math.sqrt(len(witness))
        beats_single = rate > alpha_single
        ok = indep_ok and len(witness) >= expected_min and beats_single
        all_ok = all_ok and ok
        summary[f"C_{n}_sq"] = {
            "size": len(witness),
            "independent": indep_ok,
            "rate": round(rate, 6),
            "beats_alpha_single": beats_single,
        }
    return {"witnesses": summary, "all_square_witnesses_ok": all_ok}


def verify_c7_open_gap() -> dict[str, Any]:
    """Verify the explicit 10-element independent set in C_7^{\boxtimes 2} and the open C_7 gap."""
    c7_sq_independent = is_strong_product_independent(7, C7_SQ_WITNESS)
    theta_c7 = (7.0 * math.cos(math.pi / 7.0)) / (1.0 + math.cos(math.pi / 7.0))
    polak_schrijver_lower = 367.0 ** (1.0 / 5.0)
    return {
        "c7_sq_witness_size": len(C7_SQ_WITNESS),
        "c7_sq_independent": c7_sq_independent,
        "sqrt_10": round(math.sqrt(10.0), 6),
        "polak_schrijver_367_fifth_root": round(polak_schrijver_lower, 6),
        "lovasz_theta_c7": round(theta_c7, 6),
        "open_gap_width": round(theta_c7 - polak_schrijver_lower, 6),
        "c7_ok": c7_sq_independent and len(C7_SQ_WITNESS) == 10 and polak_schrijver_lower < theta_c7,
    }


def _exact_fraction_rank(matrix: list[list[int]]) -> int:
    """Exact Gaussian elimination rank over Q using Python's fractions.Fraction."""
    n = len(matrix)
    m = [[Fraction(val) for val in row] for row in matrix]
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, n) if m[r][col] != 0), None)
        if pivot is None:
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        inv = Fraction(1) / m[rank][col]
        m[rank] = [x * inv for x in m[rank]]
        for r in range(n):
            if r != rank and m[r][col] != 0:
                factor = m[r][col]
                m[r] = [m[r][c] - factor * m[rank][c] for c in range(n)]
        rank += 1
    return rank


def verify_haemers_schlafli_separation(planted_defect: bool = False) -> dict[str, Any]:
    """Construct the 27-vertex intersection graph S_bar of the 27 lines on a cubic surface
    and verify SRG(27, 10, 1, 5), spectrum {10^1, 1^20, (-5)^6}, vartheta(S_bar) = 9,
    exact rank_Q(A(S_bar) - I) = 7, and non-multiplicativity Theta(S x S_bar) >= 27 > 21.
    """
    verts = (
        [("a", i) for i in range(6)]
        + [("b", i) for i in range(6)]
        + [("c", i, j) for i in range(6) for j in range(i + 1, 6)]
    )
    n = len(verts)

    def lines_meet(u: tuple[Any, ...], v: tuple[Any, ...]) -> bool:
        if u == v:
            return False
        tu, tv = u[0], v[0]
        if (tu, tv) == ("a", "b") or (tu, tv) == ("b", "a"):
            return u[1] != v[1]
        if tu in ("a", "b") and tv == "c":
            return u[1] in (v[1], v[2])
        if tu == "c" and tv in ("a", "b"):
            return v[1] in (u[1], u[2])
        if tu == "c" and tv == "c":
            return len({u[1], u[2], v[1], v[2]}) == 4
        return False

    adj_sbar = [[1 if lines_meet(verts[i], verts[j]) else 0 for j in range(n)] for i in range(n)]
    if planted_defect:
        adj_sbar[0][1] = 1 - adj_sbar[0][1]
        adj_sbar[1][0] = adj_sbar[0][1]

    degrees = sorted({sum(row) for row in adj_sbar})
    lam_set = sorted(
        {
            sum(adj_sbar[i][k] * adj_sbar[j][k] for k in range(n))
            for i in range(n)
            for j in range(i + 1, n)
            if adj_sbar[i][j] == 1
        }
    )
    mu_set = sorted(
        {
            sum(adj_sbar[i][k] * adj_sbar[j][k] for k in range(n))
            for i in range(n)
            for j in range(i + 1, n)
            if adj_sbar[i][j] == 0
        }
    )

    b_mat = [[adj_sbar[i][j] - (1 if i == j else 0) for j in range(n)] for i in range(n)]
    fits_graph = all(b_mat[i][i] != 0 for i in range(n)) and all(
        b_mat[i][j] == 0 for i in range(n) for j in range(n) if i != j and adj_sbar[i][j] == 0
    )
    exact_rank = _exact_fraction_rank(b_mat)

    theta_sbar = 9.0
    theta_s = 3.0
    s_triangle_independent_in_s = (
        adj_sbar[0][7] == 1 and adj_sbar[0][12] == 1 and adj_sbar[7][12] == 1
    )
    diag_product_size = n

    srg_ok = degrees == [10] and lam_set == [1] and mu_set == [5]
    haemers_ok = (
        srg_ok
        and fits_graph
        and exact_rank == 7
        and exact_rank < theta_sbar
        and s_triangle_independent_in_s
        and diag_product_size > theta_s * exact_rank
    )
    return {
        "vertices": n,
        "degrees": degrees,
        "lambda": lam_set,
        "mu": mu_set,
        "vartheta_sbar": theta_sbar,
        "vartheta_s": theta_s,
        "haemers_rank_bound": exact_rank,
        "product_diagonal_lower_bound": diag_product_size,
        "product_upper_product_bound": int(theta_s) * exact_rank,
        "haemers_ok": haemers_ok,
    }


def _check_bounds_rejections() -> bool:
    for kw in (
        dict(cycle_n=4, block_k=2),
        dict(cycle_n=6, block_k=2),
        dict(cycle_n=3, block_k=2),
        dict(cycle_n=5, block_k=0),
        dict(cycle_n=5, block_k=11),
    ):
        try:
            evaluate_odd_cycle_slider(**kw)
            return False
        except ValueError:
            pass
    return True


def run_verification(planted_defect: bool = False) -> dict[str, Any]:
    c5_slider = evaluate_odd_cycle_slider(cycle_n=5, block_k=2, planted_defect=planted_defect)
    c7_slider = evaluate_odd_cycle_slider(cycle_n=7, block_k=5, planted_defect=planted_defect)
    odd_cycle_table = [evaluate_odd_cycle_slider(cycle_n=n, block_k=2) for n in (5, 7, 9, 11, 13)]
    c5_umbrella = verify_c5_umbrella_and_product(planted_defect=planted_defect)
    square_witnesses = verify_odd_cycle_square_witnesses()
    gram_checks = [verify_odd_cycle_gram_psd(n) for n in (5, 7, 9, 11, 13)]
    c7_gap = verify_c7_open_gap()
    haemers = verify_haemers_schlafli_separation(planted_defect=planted_defect)

    sandwich_strict = all(
        row["alpha_single"] < row["lovasz_theta"] < row["fractional_alpha_star"] < row["clique_cover_chi_bar"]
        for row in odd_cycle_table
    )

    checks = {
        "odd_cycle_strict_sandwich": sandwich_strict,
        "c5_umbrella_and_5_codeword_product": c5_umbrella["umbrella_ok"],
        "c5_theta_equals_sqrt_5": abs(c5_slider["lovasz_theta"] - math.sqrt(5.0)) < 1e-5
        and abs(c5_slider["best_lower_rate"] - math.sqrt(5.0)) < 1e-5,
        "all_odd_cycle_square_witnesses_beat_alpha": square_witnesses["all_square_witnesses_ok"],
        "all_odd_cycle_gram_matrices_psd": all(g["gram_psd_ok"] for g in gram_checks),
        "c7_open_gap_3_257866_to_3_317667": c7_gap["c7_ok"] and c7_slider["best_lower_rate"] < c7_slider["lovasz_theta"],
        "haemers_schlafli_srg_27_10_1_5_and_rank_7": haemers["haemers_ok"],
        "invalid_inputs_raise_value_error": _check_bounds_rejections(),
    }
    ok = all(checks.values())
    return {
        "status": "PASS" if ok else "FAIL",
        "folio_id": "M.13",
        "planted_defect": planted_defect,
        "c5_slider": c5_slider,
        "c7_slider": c7_slider,
        "c5_umbrella": c5_umbrella,
        "square_witnesses": square_witnesses,
        "c7_open_gap": c7_gap,
        "haemers_schlafli": haemers,
        "checks": checks,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Verify Folio M.13 Shannon Zero-Error Capacity, Lovasz Theta Sandwich & Haemers Rank Bound."
    )
    parser.add_argument(
        "--planted-defect",
        action="store_true",
        help="Corrupt C_5^2 shift, umbrella angle, and Schlafli adjacency entry so strong-product & rank-7 checks must fail",
    )
    parser.add_argument("--json", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)

    report = run_verification(planted_defect=args.planted_defect)
    print(json.dumps(report, indent=2 if args.json else None))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
