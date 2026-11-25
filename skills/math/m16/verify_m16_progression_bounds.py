#!/usr/bin/env python3
"""Deterministic verifier for Folio M.16: Three-Term Arithmetic Progressions, Behrend Spheres & Fourier Bounds.

Mathematical definitions and primary anchors:
  - Progression-free extremal function r_3(N) (Erdos & Turan 1936, DOI 10.1112/jlms/s1-11.4.261):
        r_3(N) = max { |A| : A subseteq {1, ..., N}, no distinct x, y, z in A satisfy x + z = 2y }.
    Recomputed from scratch here for N = 1..24 via exact bitmask branch-and-bound, cross-checked against
    exhaustive power-set enumeration for N = 1..14, and compared against the shifted base-3 {0, 1} construction
    (attributed to G. Szekeres in Erdos & Turan 1936), written here as
        C_3(N) = { 1 + n in {1, ..., N} : n has only digits {0, 1} in base 3 }.
  - Behrend spherical-shell construction (Behrend 1946, DOI 10.1073/pnas.32.12.331; refined by Elkin 2011,
    DOI 10.1007/s11856-011-0061-1, and Green & Wolf 2010, DOI 10.1007/978-0-387-68361-4_9):
    For digit bound d in [2..8] and dimension m in [2..6], let
        S_m(R^2) = |{ x in {0, ..., d - 1}^m : sum_{i=0}^{m-1} x_i^2 = R^2 }|,   R^2 in [0, m(d - 1)^2].
    Then sum_{R^2} S_m(R^2) = d^m, so the modal shell R*^2 = argmax_{R^2} S_m(R^2) (smallest R^2 on ties)
    satisfies the pigeonhole bound
        S_m(R*^2) >= ceil( d^m / (m(d - 1)^2 + 1) ).
    Mapping shell vectors into {1, ..., (2d - 1)^m} via base b = 2d - 1:
        B(d, m) = { 1 + sum_{i=0}^{m-1} x_i (2d - 1)^i : x in {0, ..., d - 1}^m, ||x||_2^2 = R*^2 }
    prevents base-(2d - 1) carries in x_i + z_i = 2 y_i (since 0 <= x_i + z_i <= 2d - 2 < 2d - 1), while strict
    Euclidean convexity ||x||_2^2 + ||z||_2^2 - 2||(x + z)/2||_2^2 = (1/2)||x - z||_2^2 > 0 for x != z forces
    every solution to a + c = 2b in B(d, m) to be trivial (a = b = c).
  - Roth's continuous circle method vs. this folio's odd-modulus Z_{2N+1} discretization (Roth 1953,
    DOI 10.1112/jlms/s1-28.1.104; Bourgain 1999, DOI 10.1007/s000390050105; Sanders 2011,
    DOI 10.4007/annals.2011.174.1.20):
    Roth (1953) adapted the continuous Hardy-Littlewood circle method on [0, 1] to establish r_3(N) = O(N / log log N).
    To verify finite sets exactly, this script discretizes that orthogonality identity onto the odd cyclic group Z_M
    of order M = 2N + 1, eliminating modular wrap-around (2 <= x + z <= 2N < M, so x + z == 2y (mod M) iff x + z = 2y
    in Z) and ensuring gcd(2, M) = 1. With A_hat(r) = sum_{x in A} exp(-2*pi*i*r*x / M), orthogonality gives:
        T(A) = |{ (x, y, z) in A^3 : x + z = 2y }| = (1 / M) * sum_{r=0}^{M-1} A_hat(r)^2 * conj(A_hat((2r) % M)).
    When A is 3-AP-free, T(A) = |A| (trivial triples x = y = z only). Isolating r = 0 (A_hat(0) = |A|) and applying
    Parseval sum_{r=1}^{M-1} |A_hat(r)|^2 = |A|(M - |A|) yields this folio's finite linear Fourier bias floor
        max_{1 <= r < M} |A_hat(r)| >= ||A|^2 - M| / (M - |A|),
    alongside the universal Parseval root-mean-square floor sqrt(|A|(M - |A|) / (M - 1)).
  - Quasi-polynomial upper bounds and open exponent window:
    Kelley & Meka (2023, DOI 10.1109/focs57990.2023.00059, arXiv:2302.05537) established exp(-c(log N)^{1/12}) * N
    (c > 0); Bloom & Sisask (2023, Essential Number Theory, DOI 10.2140/ent.2023.2.15) gave a streamlined integer-
    interval exposition at exponent 1/12 and sharpened the exponent in preprint arXiv:2309.02353 to
    exp(-c'(log N)^{1/9}) * N (for N >= 3), framing the open log-exponent gap [1/9, 1/2].

Planted-defect mode (`--planted-defect`):
  1. Drops base b = 2d - 1 down to base b = d on genuine L^2 shells, introducing carry collisions/3-APs (e.g. d=3, m=3).
  2. Replaces quadratic shell ||x||_2^2 = R^2 with flat L^1 hyperplane sum x_i = S in carry-free base 2d - 1 (d >= 3).
  3. Replaces conj(A_hat(2r mod M)) with conj(A_hat(r)) in the cyclic DFT identity, counting x + z == y instead of 2y.
  4. Corrupts the nontrivial 3-AP test in r_3(N) by ignoring common differences d_step == 1, inflating r_3(N).
"""
from __future__ import annotations

import argparse
import cmath
from fractions import Fraction
import itertools
import json
import math
import re
import sys
from typing import Any


def _validate_slider_inputs(digit_d: int, dim_m: int) -> tuple[int, int]:
    if isinstance(digit_d, bool) or not isinstance(digit_d, int):
        raise ValueError("digit_d must be an integer")
    if digit_d < 2 or digit_d > 8:
        raise ValueError("digit_d must lie in [2, 8]")
    if isinstance(dim_m, bool) or not isinstance(dim_m, int):
        raise ValueError("dim_m must be an integer")
    if dim_m < 2 or dim_m > 6:
        raise ValueError("dim_m must lie in [2, 6]")
    return digit_d, dim_m


def count_nontrivial_3aps(elements: list[int] | set[int]) -> int:
    """Count ordered nontrivial 3-APs (a, b, c) with a < b < c and a + c == 2*b."""
    pts = sorted(set(elements))
    member = set(pts)
    k = len(pts)
    found = 0
    for i in range(k):
        a = pts[i]
        for j in range(i + 1, k):
            b = pts[j]
            c = 2 * b - a
            if c in member:
                found += 1
    return found


def cantor_base3_set(limit_n: int) -> list[int]:
    """Shifted ternary Cantor set C_3(N) = {1 + n in [1..N] : base-3 digits of n lie in {0, 1}}."""
    if isinstance(limit_n, bool) or not isinstance(limit_n, int) or limit_n < 1:
        raise ValueError("limit_n must be a positive integer")
    out: list[int] = []
    for x in range(1, limit_n + 1):
        val = x - 1
        ok = True
        while val > 0:
            if val % 3 == 2:
                ok = False
                break
            val //= 3
        if ok:
            out.append(x)
    return out


def compute_exact_r3_sequence(max_n: int = 24, planted_defect: bool = False) -> tuple[dict[int, int], dict[int, list[int]]]:
    """Compute exact r_3(N) and a lexicographically first witness for every N in 1..max_n."""
    if isinstance(max_n, bool) or not isinstance(max_n, int) or max_n < 1 or max_n > 30:
        raise ValueError("max_n must be an integer in [1, 30]")

    r3_vals: dict[int, int] = {}
    witnesses: dict[int, list[int]] = {}

    for n in range(1, max_n + 1):
        prefix_bounds = [0] * (n + 1)
        for m in range(1, n):
            prefix_bounds[m] = r3_vals[m]
        prefix_bounds[n] = n

        best_size = 0
        best_mask = 0

        def dfs(pos: int, chosen_mask: int, chosen_count: int, forbidden_mask: int) -> None:
            nonlocal best_size, best_mask
            remaining = n - pos + 1
            if chosen_count + remaining <= best_size:
                return
            if chosen_count > best_size:
                best_size = chosen_count
                best_mask = chosen_mask
            if pos > n:
                return

            bit = 1 << (pos - 1)
            if not (forbidden_mask & bit):
                next_count = chosen_count + 1
                if planted_defect or pos == n or next_count <= prefix_bounds[pos]:
                    new_forb = forbidden_mask
                    prev = chosen_mask
                    while prev:
                        lsb = prev & -prev
                        b_val = lsb.bit_length()
                        prev ^= lsb
                        step = pos - b_val
                        if planted_defect and step == 1:
                            # Planted defect #4: ignore consecutive-step (d=1) arithmetic progressions!
                            continue
                        c_val = pos + step
                        if c_val <= n:
                            new_forb |= 1 << (c_val - 1)
                    dfs(pos + 1, chosen_mask | bit, next_count, new_forb)

            dfs(pos + 1, chosen_mask, chosen_count, forbidden_mask)

        cantor = cantor_base3_set(n)
        best_size = len(cantor)
        best_mask = sum(1 << (x - 1) for x in cantor)
        dfs(1, 0, 0, 0)

        r3_vals[n] = best_size
        witnesses[n] = [i + 1 for i in range(n) if (best_mask >> i) & 1]

    return r3_vals, witnesses


def brute_force_r3(limit_n: int) -> int:
    """Independent exhaustive power-set check for r_3(N) on small N <= 14."""
    if isinstance(limit_n, bool) or not isinstance(limit_n, int) or limit_n < 1 or limit_n > 16:
        raise ValueError("limit_n must be an integer in [1, 16]")
    best = 0
    universe = list(range(1, limit_n + 1))
    for size in range(limit_n, 0, -1):
        for comb in itertools.combinations(universe, size):
            if count_nontrivial_3aps(list(comb)) == 0:
                return size
    return best


def shell_histogram_dp(digit_d: int, dim_m: int, planted_defect: bool = False) -> list[int]:
    """Exact integer DP histogram of ||x||_2^2 (or L^1 sum under planted_defect) over {0, ..., d-1}^m."""
    digit_d, dim_m = _validate_slider_inputs(digit_d, dim_m)
    max_single = (digit_d - 1) if planted_defect else (digit_d - 1) ** 2
    max_sum = dim_m * max_single
    dp = [0] * (max_sum + 1)
    dp[0] = 1
    step_vals = [x if planted_defect else (x * x) for x in range(digit_d)]
    for _ in range(dim_m):
        nxt = [0] * (max_sum + 1)
        for cur_s, ways in enumerate(dp):
            if ways == 0:
                continue
            for inc in step_vals:
                nxt[cur_s + inc] += ways
        dp = nxt
    return dp


def construct_behrend_set(
    digit_d: int,
    dim_m: int,
    planted_defect: bool = False,
    *,
    radix_override: int | None = None,
    use_l1_norm: bool = False,
) -> dict[str, Any]:
    """Explicitly materialize B(d, m) for moderate d^m and count nontrivial 3-APs."""
    digit_d, dim_m = _validate_slider_inputs(digit_d, dim_m)
    if (digit_d ** dim_m) > 50_000:
        raise ValueError("construct_behrend_set requires d^m <= 50000 for explicit enumeration")
    # Keep radix-drop and L^1-flattening orthogonal unless use_l1_norm is explicitly passed:
    # planted_defect alone drops radix from 2d - 1 to d on genuine L^2 shells.
    l1_flag = bool(use_l1_norm)
    hist = shell_histogram_dp(digit_d, dim_m, planted_defect=l1_flag)
    modal_level = max(range(len(hist)), key=lambda idx: (hist[idx], -idx))
    modal_count = hist[modal_level]
    if radix_override is not None:
        if isinstance(radix_override, bool) or not isinstance(radix_override, int) or radix_override < 2:
            raise ValueError("radix_override must be an integer >= 2")
        radix = radix_override
    else:
        radix = digit_d if planted_defect else (2 * digit_d - 1)
    ambient_n = radix ** dim_m

    encoded: list[int] = []
    for coords in itertools.product(range(digit_d), repeat=dim_m):
        level = sum(coords) if l1_flag else sum(c * c for c in coords)
        if level == modal_level:
            val = 1
            mult = 1
            for c in coords:
                val += c * mult
                mult *= radix
            encoded.append(val)

    return {
        "digit_d": digit_d,
        "dim_m": dim_m,
        "radix": radix,
        "use_l1_norm": l1_flag,
        "ambient_n": ambient_n,
        "modal_level": modal_level,
        "shell_vector_count": modal_count,
        "distinct_integer_count": len(set(encoded)),
        "nontrivial_3ap_count": count_nontrivial_3aps(encoded),
        "elements_sample": sorted(set(encoded))[:12],
    }


def evaluate_behrend_slider(
    digit_d: int = 5,
    dim_m: int = 4,
    planted_defect: bool = False,
) -> dict[str, Any]:
    """Evaluate exact Behrend shell metrics, ternary Cantor baseline, and asymptotic exponent bracket for (d, m)."""
    digit_d, dim_m = _validate_slider_inputs(digit_d, dim_m)
    hist = shell_histogram_dp(digit_d, dim_m, planted_defect=planted_defect)
    total_grid = sum(hist)
    num_shells = len(hist)
    modal_r2 = max(range(num_shells), key=lambda r2: (hist[r2], -r2))
    modal_size = hist[modal_r2]
    pigeonhole_floor = ((digit_d ** dim_m) + num_shells - 1) // num_shells
    radix = 2 * digit_d - 1
    ambient_n = radix ** dim_m

    limit_minus_1 = ambient_n - 1
    trits: list[int] = []
    tmp = limit_minus_1
    while tmp > 0:
        trits.append(tmp % 3)
        tmp //= 3
    trits.reverse()
    cantor_count = 0
    tight = True
    k_trits = len(trits)
    for idx, tr in enumerate(trits):
        rem = k_trits - idx - 1
        if tr == 0:
            continue
        elif tr == 1:
            cantor_count += 1 << rem
        else:
            cantor_count += 1 << (rem + 1)
            tight = False
            break
    if tight:
        cantor_count += 1

    density_frac = Fraction(modal_size, ambient_n)
    ratio_vs_cantor = Fraction(modal_size, cantor_count)

    return {
        "digit_d": digit_d,
        "dim_m": dim_m,
        "radix": radix,
        "ambient_n": ambient_n,
        "total_grid_vectors": total_grid,
        "shell_count": num_shells,
        "modal_r2": modal_r2,
        "modal_shell_size": modal_size,
        "pigeonhole_floor": pigeonhole_floor,
        "cantor_base3_size": cantor_count,
        "shell_density": float(density_frac),
        "shell_vs_cantor_ratio": float(ratio_vs_cantor),
        "beats_cantor": modal_size > cantor_count,
        "open_exponent_bracket": "[1/9, 1/2]",
    }


def verify_cyclic_fourier_identity(
    subset: list[int] | set[int],
    limit_n: int,
    planted_defect: bool = False,
) -> dict[str, Any]:
    """Verify T(A) = (1/M) sum_{r=0}^{M-1} A_hat(r)^2 conj(A_hat(2r mod M)) on odd Z_M (M = 2N + 1)."""
    if isinstance(limit_n, bool) or not isinstance(limit_n, int) or limit_n < 1:
        raise ValueError("limit_n must be a positive integer")
    raw_items = list(subset)
    if any(isinstance(x, bool) or not isinstance(x, int) for x in raw_items):
        raise ValueError("subset elements must be integers")
    pts = sorted(set(raw_items))
    if not pts or pts[0] < 1 or pts[-1] > limit_n:
        raise ValueError("subset must be a non-empty subset of {1, ..., limit_n}")

    modulus_m = 2 * limit_n + 1
    size_a = len(pts)

    nontrivial_unordered = count_nontrivial_3aps(pts)
    exact_ordered_triples = size_a + 2 * nontrivial_unordered

    two_pi_over_m = -2.0 * math.pi / modulus_m
    a_hat: list[complex] = []
    for r in range(modulus_m):
        acc = 0j
        for x in pts:
            acc += cmath.exp(1j * two_pi_over_m * ((r * x) % modulus_m))
        a_hat.append(acc)

    dft_sum = 0j
    for r in range(modulus_m):
        target_idx = r if planted_defect else ((2 * r) % modulus_m)
        dft_sum += (a_hat[r] * a_hat[r]) * a_hat[target_idx].conjugate()
    dft_triples = dft_sum.real / modulus_m
    dft_imag = abs(dft_sum.imag) / modulus_m

    parseval_nonzero = sum(abs(a_hat[r]) ** 2 for r in range(1, modulus_m))
    expected_parseval = float(size_a * (modulus_m - size_a))
    max_nonzero_mag = max(abs(a_hat[r]) for r in range(1, modulus_m))
    parseval_rms_floor = math.sqrt(expected_parseval / (modulus_m - 1))
    # Finite Z_M linear bias floor when T(A) = |A| (3-AP-free A subseteq {1..N})
    linear_bias_floor = (
        abs(size_a * size_a - modulus_m) / (modulus_m - size_a)
        if nontrivial_unordered == 0 and size_a < modulus_m
        else 0.0
    )

    return {
        "limit_n": limit_n,
        "modulus_m": modulus_m,
        "size_a": size_a,
        "exact_ordered_triples": exact_ordered_triples,
        "dft_triples": dft_triples,
        "dft_abs_error": abs(dft_triples - exact_ordered_triples),
        "dft_imag_residual": dft_imag,
        "parseval_nonzero_error": abs(parseval_nonzero - expected_parseval),
        "max_nonzero_fourier": max_nonzero_mag,
        "roth_linear_bias_floor": linear_bias_floor,
        "parseval_rms_floor": parseval_rms_floor,
    }


def _check_input_rejections() -> bool:
    bad_sliders: list[tuple[Any, Any, str]] = [
        (True, 4, r"digit_d must be an integer"),
        (1, 4, r"digit_d must lie in \[2, 8\]"),
        (9, 4, r"digit_d must lie in \[2, 8\]"),
        (5.0, 4, r"digit_d must be an integer"),
        (5, False, r"dim_m must be an integer"),
        (5, 1, r"dim_m must lie in \[2, 6\]"),
        (5, 7, r"dim_m must lie in \[2, 6\]"),
        (5, 4.0, r"dim_m must be an integer"),
        (float("nan"), 4, r"digit_d must be an integer"),
        (5, float("inf"), r"dim_m must be an integer"),
    ]
    for bd, bm, pat in bad_sliders:
        try:
            evaluate_behrend_slider(bd, bm)
            return False
        except ValueError as exc:
            if not re.search(pat, str(exc)):
                return False
    for bad_n in (0, -3, True, 3.5):
        try:
            cantor_base3_set(bad_n)  # type: ignore[arg-type]
            return False
        except ValueError as exc:
            if not re.search(r"limit_n must be a positive integer", str(exc)):
                return False
    bad_fourier: list[tuple[Any, Any, str]] = [
        ([], 5, r"subset must be a non-empty subset"),
        ([0, 1], 5, r"subset must be a non-empty subset"),
        ([1, 6], 5, r"subset must be a non-empty subset"),
        ([True, 2], 5, r"subset elements must be integers"),
        ([1.5, 2.5], 5, r"subset elements must be integers"),
        ([1, 2], 0, r"limit_n must be a positive integer"),
        ([1, 2], True, r"limit_n must be a positive integer"),
    ]
    for bad_sub, bad_lim, pat in bad_fourier:
        try:
            verify_cyclic_fourier_identity(bad_sub, bad_lim)
            return False
        except ValueError as exc:
            if not re.search(pat, str(exc)):
                return False
    return True


def run_verification(planted_defect: bool = False) -> tuple[bool, dict[str, Any], list[str]]:
    failures: list[str] = []
    guards_ok = _check_input_rejections()
    if not guards_ok:
        failures.append("input rejection guards failed to reject invalid parameters with expected messages")

    # 1. Exhaustive r_3(N) for N = 1..24 + independent power-set cross-check on N = 1..14
    r3_map, witnesses = compute_exact_r3_sequence(24, planted_defect=planted_defect)
    for n_chk in range(1, 15):
        bf = brute_force_r3(n_chk)
        if r3_map[n_chk] != bf:
            failures.append(f"r_3({n_chk}) mismatch: branch-and-bound={r3_map[n_chk]} vs brute-force={bf}")
    for n_chk, wit in witnesses.items():
        if len(wit) != r3_map[n_chk]:
            failures.append(f"witness length mismatch at N={n_chk}")
        ap_cnt = count_nontrivial_3aps(wit)
        if ap_cnt != 0:
            failures.append(f"witness at N={n_chk} contains {ap_cnt} nontrivial 3-APs: {wit}")

    cantor_sizes = {n: len(cantor_base3_set(n)) for n in range(1, 25)}
    if r3_map.get(9) != 5 or cantor_sizes[9] != 4:
        failures.append(f"expected r_3(9)=5 > |C_3(9)|=4, got r_3(9)={r3_map.get(9)}, |C_3(9)|={cantor_sizes[9]}")
    if r3_map.get(14) != 8 or cantor_sizes[14] != 8:
        failures.append(f"expected r_3(14)=|C_3(14)|=8, got r_3(14)={r3_map.get(14)}")
    if r3_map.get(20) != 9 or cantor_sizes[20] != 8:
        failures.append(f"expected r_3(20)=9 > |C_3(20)|=8, got r_3(20)={r3_map.get(20)}")
    if r3_map.get(24) != 10 or cantor_sizes[24] != 8:
        failures.append(f"expected r_3(24)=10 > |C_3(24)|=8, got r_3(24)={r3_map.get(24)}")

    # 2. Explicit Behrend shell construction & carry-free 3-AP-freeness sweep across (d in 2..5, m in 2..4)
    for d_it in range(2, 6):
        for m_it in range(2, 5):
            if (d_it ** m_it) > 10_000:
                continue
            # Under planted_defect, test BOTH isolated knockouts: (a) radix=d on L^2 shells, (b) L^1 slice in radix 2d-1
            b_res = construct_behrend_set(d_it, m_it, planted_defect=planted_defect, use_l1_norm=False)
            if b_res["distinct_integer_count"] != b_res["shell_vector_count"]:
                failures.append(
                    f"base encoding collision at (d={d_it}, m={m_it}): "
                    f"{b_res['distinct_integer_count']} != {b_res['shell_vector_count']}"
                )
            if b_res["nontrivial_3ap_count"] != 0:
                failures.append(
                    f"Behrend L2 shell at (d={d_it}, m={m_it}, radix={b_res['radix']}) contains "
                    f"{b_res['nontrivial_3ap_count']} nontrivial 3-APs"
                )
            if planted_defect and d_it == 3 and m_it == 3:
                l1_res = construct_behrend_set(3, 3, radix_override=5, use_l1_norm=True)
                if l1_res["nontrivial_3ap_count"] != 0:
                    failures.append(
                        f"L1 hyperplane slice at (d=3, m=3, radix=5) contains "
                        f"{l1_res['nontrivial_3ap_count']} nontrivial 3-APs"
                    )

    # Check full slider grid (d in 2..8, m in 2..6) pigeonhole & Cantor consistency
    grid_summary: dict[str, Any] = {}
    for d_it in range(2, 9):
        for m_it in range(2, 7):
            ev = evaluate_behrend_slider(d_it, m_it, planted_defect=planted_defect)
            if ev["total_grid_vectors"] != (d_it ** m_it):
                failures.append(f"histogram sum mismatch at ({d_it}, {m_it})")
            if ev["modal_shell_size"] < ev["pigeonhole_floor"]:
                failures.append(f"modal shell below pigeonhole floor at ({d_it}, {m_it})")
            grid_summary[f"d{d_it}_m{m_it}"] = ev

    # 3. Cyclic Z_{2N+1} Fourier 3-AP identity & bias floor sweep across N = 3..24
    max_dft_err = 0.0
    for n_it in range(3, 25):
        wit = witnesses[n_it] if count_nontrivial_3aps(witnesses[n_it]) == 0 else cantor_base3_set(n_it)
        f_res = verify_cyclic_fourier_identity(wit, n_it, planted_defect=planted_defect)
        max_dft_err = max(max_dft_err, f_res["dft_abs_error"], f_res["dft_imag_residual"])
        if f_res["dft_abs_error"] > 1e-12 or f_res["dft_imag_residual"] > 1e-12:
            failures.append(
                f"DFT 3-AP identity failed at N={n_it}: dft={f_res['dft_triples']:.6f} "
                f"vs exact={f_res['exact_ordered_triples']}"
            )
        if f_res["parseval_nonzero_error"] > 1e-11:
            failures.append(f"Parseval identity failed at N={n_it}")
        if f_res["max_nonzero_fourier"] + 1e-11 < max(f_res["roth_linear_bias_floor"], f_res["parseval_rms_floor"]):
            failures.append(f"Fourier peak below theoretical floor at N={n_it}")

    default_eval = evaluate_behrend_slider(5, 4, planted_defect=planted_defect)
    fourier_n14 = verify_cyclic_fourier_identity(cantor_base3_set(14), 14, planted_defect=planted_defect)
    fourier_n20 = verify_cyclic_fourier_identity(witnesses[20], 20, planted_defect=planted_defect)

    report = {
        "folio_id": "M.16",
        "status": "PASS" if not failures else "FAIL",
        "planted_defect": planted_defect,
        "input_guards_ok": guards_ok,
        "r3_1_to_24": r3_map,
        "cantor_1_to_24": cantor_sizes,
        "witness_n9": witnesses[9],
        "witness_n20": witnesses[20],
        "witness_n24": witnesses[24],
        "default_slider_d5_m4": default_eval,
        "grid_highlights": {
            k: grid_summary[k]
            for k in ("d2_m3", "d3_m3", "d4_m3", "d5_m4", "d6_m5", "d8_m6")
        },
        "fourier_n14_cantor": fourier_n14,
        "fourier_n20_extremal": fourier_n20,
        "max_dft_abs_error": max_dft_err,
        "failure_count": len(failures),
        "failures": failures[:10],
    }
    return len(failures) == 0, report, failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Deterministic verifier for Folio M.16 progression-free bounds.")
    parser.add_argument("--planted-defect", action="store_true", help="Run negative-control planted-defect knockouts.")
    parser.add_argument("--json", action="store_true", help="Print full JSON verification report (default behavior).")
    args = parser.parse_args(argv)

    ok, report, failures = run_verification(planted_defect=args.planted_defect)
    print(json.dumps(report, indent=2))
    if failures:
        for f in failures[:8]:
            print(f"FAIL: {f}", file=sys.stderr)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
