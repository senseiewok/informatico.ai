---
name: progression-free-behrend-kelley-meka-bounds
description: AI-agnostic additive and extremal combinatorics skill for three-term progression-free sets r_3(N), carry-free base-(2d-1) Behrend spherical shells, odd-modulus cyclic Fourier identities, and Kelley-Meka quasi-polynomial bounds.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Three-Term Arithmetic Progressions: Behrend Spheres, Fourier Bias & Kelley–Meka Bounds (Folio M.16)

A plain-text companion to the essay at https://informatico.ai/math/m16/ (`M.16 · Three-Term Arithmetic Progressions & Behrend Spheres · REV 1.0`, `REV 1.0`, redated `2026-11-24`).

## The governing relation
`For N ≥ 3: T(A) = (1/M) ∑_r Â(r)² conj(Â(2r mod M)) · N exp(−c √(log N)) ≤ r_3(N) ≤ N exp(−c′ (log N)^(1/9))`

## Rules the essay derives
1. Encode Behrend shell vectors x in {0, ..., d - 1}^m using radix b = 2d - 1 (never b = d) and strict Euclidean norm sum(x_i^2) = R^2 (never L^1 sum), blocking carries in x_i + z_i = 2*y_i while strict sphere convexity forces x = y = z.
2. Distinguish Roth’s 1953 continuous circle-method bound O(N / log log N) from this folio’s finite odd-modulus cyclic discretization Z_M (M = 2N + 1), and retain the complex square A_hat(r)^2 (not |A_hat(r)|^2) in T(A) = (1/M) * sum_r A_hat(r)^2 * conj(A_hat(2r mod M)).
3. Separate finite-N behavior from asymptotic growth: C_3(N) matches r_3(N) at N = 14 (8) yet trails at N = 9 (4 vs 5), N = 20 (8 vs 9), and N = 24 (8 vs 10), and |C_3((2d - 1)^m)| exceeds |B(d, m)| across d in [2..8], m in [2..6] before Behrend’s exp(-c * sqrt(log N)) density overtakes N^(log_3 2) at large m.
4. Keep the upper-bound milestones distinct—Bloom-Sisask arXiv:2007.03528 logarithmic-barrier break, Kelley-Meka 2023 (DOI 10.1109/focs57990.2023.00059) explicit exp(-c * (log N)^(1/12)) * N bound, Bloom-Sisask 2023 Essential Number Theory (DOI 10.2140/ent.2023.2.15) 1/12 exposition, and preprint arXiv:2309.02353 exponent 1/9—and keep the log-exponent gap [1/9, 1/2] explicitly labeled OPEN.

## How it works, in four stages
- Stage 1 (Small Extremal Thresholds and Ternary Cantor Departures, 1936): Paul Erdős and Pál Turán (1936, DOI 10.1112/jlms/s1-11.4.261) introduced r_3(N), the maximum size of a subset of {1, …, N} containing no three distinct terms in arithmetic progression x + z = 2y, and recorded the base-3 {0, 1} construction (credited there to G. Szekeres), written here as C_3(N) of scale N^(log_3 2) ≈ N^0.63093. Exhaustive search in verify_m16_progression_bounds.py recomputes r_3(1..24) and pinpoints where optimal sets outgrow C_3(N): at N = 9, witness {1, 2, 4, 8, 9} gives r_3(9) = 5 > |C_3(9)| = 4; at N = 14, r_3(14) = |C_3(14)| = 8; at N = 20, {1, 2, 6, 7, 9, 14, 15, 18, 20} gives r_3(20) = 9 > 8; and at N = 24, r_3(24) = 10 > 8.
- Stage 2 (Behrend Spherical Shells and Carry-Free Base-(2d − 1) Projection, 1942–2011): Raphaël Salem and Donald Spencer (1942, DOI 10.1073/pnas.28.12.561) refuted sub-linear power-law ceilings O(N^(1 − ε)) on r_3(N), and Felix Behrend (1946, DOI 10.1073/pnas.32.12.331) intersected {0, …, d − 1}^m with quadratic shells ∑ x_i² = R², choosing modal shell R*² of size S_m(R*²) ≥ ⌈d^m / (m(d − 1)² + 1)⌉ and projecting via radix b = 2d − 1 into {1, …, (2d − 1)^m}. Because 0 ≤ x_i + z_i ≤ 2d − 2 < 2d − 1 blocks every base carry and strict Euclidean convexity forbids three distinct collinear sphere points, B(d, m) has zero nontrivial 3-APs; Michael Elkin (2011, DOI 10.1007/s11856-011-0061-1) and Ben Green with Julia Wolf (2010, DOI 10.1007/978-0-387-68361-4_9) thickened the sphere to a thin annulus, raising r_3(N) by a Θ(√(log N)) factor.
- Stage 3 (Roth’s Circle Method and Our Odd-Modulus Z_{2N+1} Discretization, 1953–2011): Klaus Roth (1953, DOI 10.1112/jlms/s1-28.1.104) adapted the continuous Hardy–Littlewood circle method on [0, 1] to establish r_3(N) = O(N / log log N). To check finite sets exactly, this folio discretizes Roth’s orthogonality identity onto the odd cyclic group Z_M of order M = 2N + 1, preventing wrap-around since 2 ≤ x + z ≤ 2N < M and giving T(A) = (1/M) ∑_{r=0}^{M−1} Â(r)² conj(Â(2r mod M)) with complex square Â(r)². When A is 3-AP-free, T(A) = |A|, yielding our finite linear bias floor max_{r≠0} |Â(r)| ≥ ||A|² − M| / (M − |A|) alongside Parseval’s RMS floor √(|A|(M − |A|)/(M − 1)); Jean Bourgain (1999, DOI 10.1007/s000390050105) and Tom Sanders (2011, DOI 10.4007/annals.2011.174.1.20) refined Bohr-set and almost-periodicity increments.
- Stage 4 (Kelley–Meka Physical-Space Sifting, Combined Display Note & Tier T0–T1 Falsification, 2020–2023): After Thomas Bloom and Olof Sisask crossed the logarithmic barrier in preprint arXiv:2007.03528, Zander Kelley and Raghu Meka (2023, DOI 10.1109/focs57990.2023.00059, arXiv:2302.05537) bypassed high-order Fourier inversions via Hölder decoupling, physical-space sifting, and spread subspaces to establish r_3(N) ≤ exp(−c (log N)^(1/12)) N (c > 0), expounded on integer intervals at β = 1/12 by Bloom and Sisask (2023, DOI 10.2140/ent.2023.2.15) and sharpened to β = 1/9 in preprint arXiv:2309.02353 (for N ≥ 3, combined in our governing header beside Behrend’s β = 1/2 lower bound and our Z_{2N+1} DFT identity). Hypothesis (Tier T0–T1): across d ∈ [2..8], m ∈ [2..6], radix-(2d − 1) overhead keeps |B(d, m)| < |C_3(N)| before asymptotic crossover, while valid log exponents in [1/9, 1/2] remain OPEN; any construction with β < 1/2 or upper bound with β > 1/9 narrows that open interval.

## Reference values stated in the essay
- **Modal Behrend Shell |B(d, m)|**: `|B(5, 4)| = 30 on R*² = 18 (in N = 6,561, base 9)`
- **Grid Pigeonhole & Ternary Baseline**: `Pigeonhole ≥ 10 (625 / 65 shells) · Cantor C_3(6,561) = 256`
- **Small Exact r_3(N) & Fourier Peak (Fixed Reference)**: `r_3(9) = 5, r_3(14) = 8, r_3(20) = 9, r_3(24) = 10 · max |Â(r)| = 5.15 at N = 20 (M = 41)`
- **Asymptotic Log-Exponent Window**: `OPEN EXPONENT GAP β ∈ [1/9, 1/2] · FINITE CROSSOVER REGIME`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/math/m16/verify_m16_progression_bounds.py
python skills/math/m16/verify_m16_progression_bounds.py --planted-defect
```

## Primary source
- https://doi.org/10.1112/jlms/s1-28.1.104 (Scite report: https://scite.ai/reports/10.1112/jlms/s1-28.1.104)
- What the essay compares against: r_3(9) = 5 > |C_3(9)| = 4 · r_3(20) = 9, r_3(24) = 10 · |B(5, 4)| = 30 on R*² = 18 in N = 6,561 · Open log exponent β ∈ [1/9, 1/2]

## Recent research context
- **Closing Seventy Years Between Roth’s Circle Method and Quasi-Polynomial 3-AP Bounds**: Seventy years after Klaus Roth (1953, DOI 10.1112/jlms/s1-28.1.104) established r_3(N) = O(N / log log N), Zander Kelley and Raghu Meka (2023, DOI 10.1109/focs57990.2023.00059, arXiv:2302.05537) bypassed high-order Fourier inversion via physical-space Hölder decoupling and sifting to establish r_3(N) ≤ exp(−c (log N)^(1/12)) N, expounded by Thomas Bloom and Olof Sisask (2023, DOI 10.2140/ent.2023.2.15) and sharpened to exponent 1/9 in preprint arXiv:2309.02353 toward Behrend’s 1946 spherical-shell exponent β = 1/2.
