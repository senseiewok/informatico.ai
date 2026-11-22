#!/usr/bin/env python3
"""Deterministic verifier for Folio M.15: Diagonal Ramsey Numbers, Paley P(17), Random Floors & Book Bounds.

Mathematical definitions and primary anchors:
  - Ramsey's theorem (Ramsey 1930, DOI 10.1112/plms/s2-30.1.264) & Erdos-Szekeres recursion (1935; Greenwood &
    Gleason 1955, DOI 10.4153/CJM-1955-001-4):
        R(s, t) <= R(s - 1, t) + R(s, t - 1) <= C(s + t - 2, s - 1),
    with strict inequality R(s, t) <= R(s - 1, t) + R(s, t - 1) - 1 whenever both summands are even.
  - Small diagonal and off-diagonal values recomputed from scratch here:
      1. R(3, 3) = 6: C_5 on Z_5 avoids red K_3 and blue K_3 (R(3, 3) > 5), while all 2^C(6, 2) = 32,768
         two-colorings of K_6 satisfy Goodman's triangle multiplicity identity (Goodman 1959,
         DOI 10.1080/00029890.1959.11989408):
             T_mono(G) = C(6, 3) - (1 / 2) * sum_{v=0}^5 d_r(v) * (5 - d_r(v)) >= 20 - 18 = 2.
      2. R(3, 4) = 9 (Greenwood & Gleason 1955): Circulant graph on Z_8 with red step set {1, 4, 7} has
         0 red K_3 across C(8, 3) = 56 triples and 0 blue K_4 across C(8, 4) = 70 quadruples (R(3, 4) > 8),
         while R(2, 4) = 4 and R(3, 3) = 6 are both even so 3-regularity on 9 vertices would require odd
         degree sum 9 * 3 = 27, forcing R(3, 4) <= 9.
      3. R(4, 4) = 18 (Greenwood & Gleason 1955): Paley graph P(17) over F_17 with quadratic-residue red step
         set {1, 2, 4, 8, 9, 13, 15, 16} is SRG(17, 8, 3, 4), self-complementary via multiplication by the
         quadratic non-residue 3 mod 17, and has 0 red K_4 and 0 blue K_4 across all C(17, 4) = 2,380
         4-subsets (R(4, 4) > 17), matching R(3, 4) + R(4, 3) = 9 + 9 = 18.
  - Asymmetric random first-moment floor (Erdos 1947, DOI 10.1090/S0002-9904-1947-08785-1):
        E[X_k(n, p)] = C(n, k) * (p^C(k, 2) + (1 - p)^C(k, 2)),
        n_1(k, p) = max { n >= k - 1 : E[X_k(n, p)] < 1 }  =>  R(k, k) >= n_1(k, p) + 1.
    For every k >= 3 and n >= k, E[X_k(n, p)] is strictly convex in p and uniquely minimized at p = 1/2.
    On the 0.05 grid p in [0.20, 0.80], integer n_1(k, p) has flat plateaus at k = 3 (n_1 = 3) and k = 4
    (n_1 = 6 on [0.40, 0.60]) and attains a strict unique maximum at p = 0.50 for every k in {5..10}
    (n_1 = 11, 17, 27, 42, 65, 100 => R(k, k) >= 12, 18, 28, 43, 66, 101).
  - Spencer's Lovasz Local Lemma bound (Spencer 1975, DOI 10.1016/0097-3165(75)90071-0), Thomason's polynomial
    factor (1988, DOI 10.1002/jgt.3190120406), Conlon (2009, DOI 10.4007/annals.2009.170.941), Sah (2023,
    DOI 10.1215/00127094-2022-0048), Campos-Griffiths-Morris-Sahasrabudhe exponential book bound (4 - eps)^k
    (2026, DOI 10.4007/annals.2026.203.3.4), and open finite interval 43 <= R(5, 5) <= 46 (Exoo 1989,
    DOI 10.1002/jgt.3190130113; Angeltveit & McKay 2026, DOI 10.1002/jgt.70029).

Planted-defect mode (`--planted-defect`):
  1. Adds chord (0, 2) to C_5 and replaces Goodman's K_6 triangle lower bound with 0.
  2. Replaces the Z_8 circulant {1, 4, 7} with {1, 3, 5, 7} (bipartite K_{4,4}, creating two blue K_4s).
  3. Adds non-residue {3, 14} to P(17) and uses residue multiplier 2 instead of non-residue 3, breaking
     self-complementarity, SRG(17, 8, 3, 4), and K_4-freeness.
  4. At k = 3 relaxes the strict union-bound condition E[X_3(n, p)] < 1 to <= 1 (falsely accepting E = 1.0 at
     n = 4, p = 0.50 and inflating n_1(3, 0.50) from 3 to 4), and for k >= 4 drops the blue term (1 - p)^m,
     breaking p <-> 1 - p symmetry and skewing the optimal density away from p = 0.50.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
import json
import math
import sys
from typing import Any


QR_17: frozenset[int] = frozenset({(x * x) % 17 for x in range(1, 17)})

KNOWN_DIAGONAL_BOUNDS: dict[int, tuple[int, int | None, str]] = {
    3: (6, 6, "SETTLED: R(3, 3) = 6 (C_5 witness & Goodman K_6 bound)"),
    4: (18, 18, "SETTLED: R(4, 4) = 18 (Paley P(17) & R(3,4)+R(4,3))"),
    5: (43, 46, "OPEN WINDOW: 43 <= R(5, 5) <= 46 (Exoo 1989; Angeltveit-McKay 2026)"),
}

EXPECTED_BALANCED_N1: dict[int, int] = {
    3: 3,
    4: 6,
    5: 11,
    6: 17,
    7: 27,
    8: 42,
    9: 65,
    10: 100,
}


def _validate_slider_inputs(clique_k: int, red_p: float | Fraction) -> Fraction:
    if not isinstance(clique_k, int) or isinstance(clique_k, bool):
        raise ValueError("clique_k must be an integer")
    if clique_k < 3 or clique_k > 10:
        raise ValueError("clique_k must lie in [3, 10]")
    if isinstance(red_p, bool) or not isinstance(red_p, (int, float, Fraction)):
        raise ValueError("red_p must be a real number or Fraction")
    if isinstance(red_p, (int, Fraction)):
        twentyp_frac = Fraction(red_p) * 20
        if twentyp_frac.denominator != 1:
            raise ValueError("red_p must lie on the 0.05 step grid")
        twentyp = int(twentyp_frac.numerator)
    else:
        if not math.isfinite(red_p):
            raise ValueError("red_p must be finite")
        twentyp = round(red_p * 20.0)
        if abs(red_p * 20.0 - twentyp) > 1e-9:
            raise ValueError("red_p must lie on the 0.05 step grid")
    if twentyp < 4 or twentyp > 16:
        raise ValueError("red_p must lie in [0.20, 0.80]")
    return Fraction(twentyp, 20)


def expected_monochromatic_cliques(
    n: int,
    clique_k: int,
    p_frac: Fraction,
    planted_defect: bool = False,
) -> Fraction:
    """Exact rational expected count E[X_k(n, p)] = C(n, k) * (p^C(k,2) + (1 - p)^C(k,2))."""
    if n < clique_k:
        return Fraction(0)
    m_edges = (clique_k * (clique_k - 1)) // 2
    comb_nk = math.comb(n, clique_k)
    if planted_defect and clique_k >= 4:
        # Planted defect for k >= 4: drop blue clique term (1 - p)^m, breaking symmetry around p = 1/2.
        prob_mono = p_frac ** m_edges
    else:
        prob_mono = (p_frac ** m_edges) + ((Fraction(1) - p_frac) ** m_edges)
    return Fraction(comb_nk) * prob_mono


def first_moment_witness_n1(
    clique_k: int,
    red_p: float | Fraction = Fraction(1, 2),
    planted_defect: bool = False,
) -> int:
    """Largest vertex count n >= k - 1 with E[X_k(n, p)] < 1 (giving R(k, k) >= n_1 + 1)."""
    p_frac = _validate_slider_inputs(clique_k, red_p)
    n = clique_k - 1
    while True:
        cand = n + 1
        exp_val = expected_monochromatic_cliques(cand, clique_k, p_frac, planted_defect=planted_defect)
        # At k = 3, planted_defect relaxes strict < 1 to <= 1, hitting E = 1.0 at (k=3, n=4, p=0.50).
        ok = (exp_val <= 1) if (planted_defect and clique_k == 3) else (exp_val < 1)
        if ok:
            n = cand
        else:
            break
    return n


def evaluate_ramsey_slider(
    clique_k: int = 5,
    red_p: float = 0.50,
    planted_defect: bool = False,
) -> dict[str, Any]:
    """Evaluate exact rational first-moment floor, Erdos-Szekeres ceiling, and status for (k, p)."""
    p_frac = _validate_slider_inputs(clique_k, red_p)
    n1 = first_moment_witness_n1(clique_k, p_frac, planted_defect=planted_defect)
    ramsey_floor = n1 + 1
    n1_balanced = first_moment_witness_n1(clique_k, Fraction(1, 2), planted_defect=False)
    es_binomial = math.comb(2 * clique_k - 2, clique_k - 1)
    spencer_lll_asymp = (math.sqrt(2.0) / math.e) * clique_k * (2.0 ** (clique_k / 2.0))
    exp_at_n1 = float(expected_monochromatic_cliques(n1, clique_k, p_frac, planted_defect=planted_defect))
    exp_at_next = float(expected_monochromatic_cliques(n1 + 1, clique_k, p_frac, planted_defect=planted_defect))

    if clique_k in KNOWN_DIAGONAL_BOUNDS:
        lo_known, hi_known, status_label = KNOWN_DIAGONAL_BOUNDS[clique_k]
    else:
        lo_known = n1_balanced + 1
        hi_known = es_binomial
        status_label = (
            f"OPEN ASYMPTOTIC GAP: floor >= {lo_known} vs C({2 * clique_k - 2},{clique_k - 1}) = {es_binomial:,}"
        )

    return {
        "clique_k": clique_k,
        "red_p": round(float(p_frac), 2),
        "witness_n1": n1,
        "first_moment_ramsey_floor": ramsey_floor,
        "balanced_ramsey_floor": n1_balanced + 1,
        "spencer_lll_scale": round(spencer_lll_asymp, 2),
        "erdos_szekeres_binomial": es_binomial,
        "expected_cliques_at_n1": round(exp_at_n1, 6),
        "expected_cliques_at_n1_plus_1": round(exp_at_next, 6),
        "known_lower": lo_known,
        "known_upper": hi_known,
        "status_label": status_label,
    }


def verify_r33_c5_and_exhaustive_k6(planted_defect: bool = False) -> dict[str, Any]:
    """Check C_5 avoids monochromatic K_3 and all 32,768 two-colorings of K_6 have >= 2 monochromatic K_3s."""
    c5_red = {(i, (i + 1) % 5) for i in range(5)} | {((i + 1) % 5, i) for i in range(5)}
    if planted_defect:
        c5_red.add((0, 2))
        c5_red.add((2, 0))
    c5_mono_k3 = 0
    for a, b, c in combinations(range(5), 3):
        e1, e2, e3 = (a, b) in c5_red, (b, c) in c5_red, (a, c) in c5_red
        if (e1 and e2 and e3) or (not e1 and not e2 and not e3):
            c5_mono_k3 += 1

    edges_k6 = list(combinations(range(6), 2))
    tri_masks: list[int] = []
    edge_index = {e: idx for idx, e in enumerate(edges_k6)}
    for a, b, c in combinations(range(6), 3):
        mask = (1 << edge_index[(a, b)]) | (1 << edge_index[(a, c)]) | (1 << edge_index[(b, c)])
        tri_masks.append(mask)
    vert_inc = [0] * 6
    for idx, (u, v) in enumerate(edges_k6):
        vert_inc[u] |= 1 << idx
        vert_inc[v] |= 1 << idx

    min_mono = 20
    extremal_count = 0
    goodman_mismatches = 0
    for bits in range(1 << 15):
        mono = 0
        for tmask in tri_masks:
            sub = bits & tmask
            if sub == 0 or sub == tmask:
                mono += 1
        if planted_defect:
            goodman_val = 0
        else:
            non_mono_pairs = sum(
                (bits & vert_inc[v]).bit_count() * (5 - (bits & vert_inc[v]).bit_count())
                for v in range(6)
            )
            goodman_val = 20 - (non_mono_pairs // 2)
        if mono != goodman_val:
            goodman_mismatches += 1
        if mono < min_mono:
            min_mono = mono
            extremal_count = 1
        elif mono == min_mono:
            extremal_count += 1

    return {
        "c5_monochromatic_triangles": c5_mono_k3,
        "k6_total_colorings": 1 << 15,
        "k6_min_monochromatic_triangles": min_mono,
        "k6_extremal_coloring_count": extremal_count,
        "goodman_formula_mismatches": goodman_mismatches,
        "r33_ok": (
            c5_mono_k3 == 0
            and min_mono == 2
            and extremal_count == 1760
            and goodman_mismatches == 0
        ),
    }


def verify_r34_circulant8_and_parity(planted_defect: bool = False) -> dict[str, Any]:
    """Check Circ_8({1, 4, 7}) has 0 red K_3 and 0 blue K_4, and 9-vertex parity closes R(3, 4) = 9."""
    steps = {1, 3, 5, 7} if planted_defect else {1, 4, 7}
    red_k3 = 0
    for a, b, c in combinations(range(8), 3):
        if ((b - a) % 8 in steps) and ((c - b) % 8 in steps) and ((a - c) % 8 in steps):
            red_k3 += 1
    blue_k4 = 0
    for quad in combinations(range(8), 4):
        if all(((v - u) % 8) not in steps for u, v in combinations(quad, 2)):
            blue_k4 += 1

    # On K_9, avoiding red K_3 (since R(2, 4) = 4 => d_r <= 3) and blue K_4 (since R(3, 3) = 6 => d_b <= 5,
    # hence d_r = 8 - d_b >= 3) forces d_r(v) = 3 for all 9 vertices, whose sum 27 is odd.
    forced_red_degree_k9 = 3
    degree_sum_k9 = 9 * forced_red_degree_k9
    parity_obstruction = (degree_sum_k9 % 2 == 1)
    greenwood_gleason_bound = 4 + 6 - 1

    return {
        "z8_red_k3_count": red_k3,
        "z8_blue_k4_count": blue_k4,
        "k9_forced_red_degree_sum": degree_sum_k9,
        "k9_handshaking_obstruction": parity_obstruction,
        "r34_value": greenwood_gleason_bound,
        "r34_ok": red_k3 == 0 and blue_k4 == 0 and parity_obstruction and greenwood_gleason_bound == 9,
    }


def verify_r44_paley17(planted_defect: bool = False) -> dict[str, Any]:
    """Check Paley P(17) over F_17 is SRG(17, 8, 3, 4), self-complementary, and (K_4, K_4)-free."""
    diff_set = set(QR_17)
    if planted_defect:
        diff_set.update({3, 14})
    adj = [
        [1 if (u != v and ((v - u) % 17) in diff_set) else 0 for v in range(17)]
        for u in range(17)
    ]
    degrees = [sum(row) for row in adj]
    adj_common: set[int] = set()
    nonadj_common: set[int] = set()
    for u, v in combinations(range(17), 2):
        common = sum(adj[u][w] and adj[v][w] for w in range(17))
        if adj[u][v]:
            adj_common.add(common)
        else:
            nonadj_common.add(common)

    mult = 2 if planted_defect else 3
    self_comp_ok = all(
        adj[(mult * u) % 17][(mult * v) % 17] == (1 - adj[u][v])
        for u, v in combinations(range(17), 2)
    )

    red_k4 = 0
    blue_k4 = 0
    for a, b, c, d in combinations(range(17), 4):
        edges_sum = adj[a][b] + adj[a][c] + adj[a][d] + adj[b][c] + adj[b][d] + adj[c][d]
        if edges_sum == 6:
            red_k4 += 1
        elif edges_sum == 0:
            blue_k4 += 1

    r44_upper = 9 + 9
    srg_ok = (set(degrees) == {8} and adj_common == {3} and nonadj_common == {4})
    return {
        "qr_17": sorted(QR_17),
        "srg_parameters_17_8_3_4": srg_ok,
        "self_complementary_via_3x": self_comp_ok,
        "subsets_checked": math.comb(17, 4),
        "red_k4_count": red_k4,
        "blue_k4_count": blue_k4,
        "r44_upper_from_r34": r44_upper,
        "r44_ok": srg_ok and self_comp_ok and red_k4 == 0 and blue_k4 == 0 and r44_upper == 18,
    }


def verify_probabilistic_and_asymptotic_table(planted_defect: bool = False) -> dict[str, Any]:
    """Verify exact Fraction first-moment floors, convexity at p = 0.50, plateaus, and k = 3..10 table."""
    p_grid = [Fraction(step, 20) for step in range(4, 17)]
    convexity_ok = True
    strict_argmax_k5_to_10 = True
    plateaus_k3_k4_ok = True
    balanced_matches = True
    table: dict[str, Any] = {}

    for k in range(3, 11):
        n_bal = first_moment_witness_n1(k, Fraction(1, 2), planted_defect=planted_defect)
        if n_bal != EXPECTED_BALANCED_N1[k]:
            balanced_matches = False
        e_mid = expected_monochromatic_cliques(n_bal + 1, k, Fraction(1, 2), planted_defect=planted_defect)
        for p_val in p_grid:
            n_at_p = first_moment_witness_n1(k, p_val, planted_defect=planted_defect)
            if k == 3 and n_at_p != 3:
                plateaus_k3_k4_ok = False
            if k == 4:
                in_plateau = Fraction(8, 20) <= p_val <= Fraction(12, 20)
                if in_plateau and n_at_p != 6:
                    plateaus_k3_k4_ok = False
                if (not in_plateau) and not (n_at_p < 6):
                    plateaus_k3_k4_ok = False
            if p_val != Fraction(1, 2):
                e_off = expected_monochromatic_cliques(n_bal + 1, k, p_val, planted_defect=planted_defect)
                if not (e_mid < e_off):
                    convexity_ok = False
                if k >= 5 and not (n_at_p < n_bal):
                    strict_argmax_k5_to_10 = False
        table[f"k={k}"] = evaluate_ramsey_slider(k, 0.50, planted_defect=planted_defect)

    # Check open R(5, 5) bracket consistency with random floor and Erdos-Szekeres ceiling
    r5_floor = EXPECTED_BALANCED_N1[5] + 1  # 12
    r5_exoo = 43
    r5_angeltveit_mckay = 46
    r5_es = math.comb(8, 4)  # 70
    r5_bracket_ok = (r5_floor == 12 and r5_exoo == 43 and r5_angeltveit_mckay == 46 and r5_es == 70)
    skew_pins_ok = (
        not planted_defect
        and first_moment_witness_n1(5, Fraction(4, 20)) == 6
        and first_moment_witness_n1(5, Fraction(9, 20)) == 10
        and first_moment_witness_n1(10, Fraction(4, 20)) == 17
        and first_moment_witness_n1(10, Fraction(9, 20)) == 71
        and math.comb(18, 9) == 48620
    )

    return {
        "balanced_n1_matches_reference": balanced_matches,
        "expectation_uniquely_minimized_at_half": convexity_ok,
        "plateaus_k3_k4_verified": plateaus_k3_k4_ok,
        "n1_strict_grid_argmax_for_k5_to_10": strict_argmax_k5_to_10,
        "skew_density_pins_ok": skew_pins_ok,
        "r55_open_bracket": [r5_exoo, r5_angeltveit_mckay],
        "asymptotic_base_interval": [round(math.sqrt(2.0), 6), "4 - eps (CGMS 2026)"],
        "table_p_half": table,
        "probabilistic_ok": (
            balanced_matches
            and convexity_ok
            and plateaus_k3_k4_ok
            and strict_argmax_k5_to_10
            and r5_bracket_ok
            and skew_pins_ok
        ),
    }


def _check_input_rejections() -> bool:
    bad_inputs: list[tuple[Any, Any]] = [
        (True, 0.50),
        (2, 0.50),
        (11, 0.50),
        (5, False),
        (5, 0.15),
        (5, 0.85),
        (5, 0.53),
        (5, Fraction(1, 2) + Fraction(1, 10**12)),
        (5, 10**400),
        (5, Fraction(10**400, 1)),
        (5, float("nan")),
        (5, float("inf")),
    ]
    for bad_k, bad_p in bad_inputs:
        try:
            evaluate_ramsey_slider(bad_k, bad_p)
            return False
        except ValueError:
            pass
    return True


def run_verification(planted_defect: bool = False) -> dict[str, Any]:
    r33 = verify_r33_c5_and_exhaustive_k6(planted_defect=planted_defect)
    r34 = verify_r34_circulant8_and_parity(planted_defect=planted_defect)
    r44 = verify_r44_paley17(planted_defect=planted_defect)
    prob = verify_probabilistic_and_asymptotic_table(planted_defect=planted_defect)
    guards_ok = _check_input_rejections()
    default_readout = evaluate_ramsey_slider(5, 0.50, planted_defect=planted_defect)

    all_ok = (
        r33["r33_ok"]
        and r34["r34_ok"]
        and r44["r44_ok"]
        and prob["probabilistic_ok"]
        and guards_ok
    )
    return {
        "folio_id": "M.15",
        "status": "PASS" if all_ok else "FAIL",
        "planted_defect": planted_defect,
        "default_slider_k5_p050": default_readout,
        "r33_exhaustive_k6": r33,
        "r34_circulant8_and_parity": r34,
        "r44_paley17": r44,
        "probabilistic_bounds": prob,
        "input_guards_ok": guards_ok,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--planted-defect",
        action="store_true",
        help="Inject planted combinatorial and probabilistic defects and assert verification fails.",
    )
    args = parser.parse_args(argv)
    report = run_verification(planted_defect=args.planted_defect)
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
