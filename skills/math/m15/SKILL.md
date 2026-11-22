---
name: diagonal-ramsey-paley-book-bounds
description: AI-agnostic extremal and probabilistic combinatorics skill for diagonal Ramsey numbers R(k, k), Goodman triangle multiplicity, Paley P(17), rational Erdos first-moment floors, and asymmetric book bounds.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Diagonal Ramsey Numbers: Paley Colorings, Erdős Random Floors, the Book Algorithm & Open Gaps (Folio M.15)

A plain-text companion to the essay at https://informatico.ai/math/m15/ (`M.15 · Diagonal Ramsey Numbers & Book Bounds · REV 1.0`, `REV 1.0`, redated `2026-11-21`).

## The governing relation
`E[X_k(n, p)] = C(n, k)[p^C(k,2) + (1 − p)^C(k,2)] · √2 ≤ lim inf R(k,k)^(1/k) ≤ lim sup R(k,k)^(1/k) ≤ 4 − ε`

## Rules the essay derives
1. Require strict inequality E[X_k(n, p)] = C(n, k) * (p^C(k,2) + (1 - p)^C(k,2)) < 1 in rational arithmetic when computing the first-moment witness n_1(k, p), since E = 1 (as at k = 3, n = 4, p = 0.50) permits constant-1 random variables with zero clique-free colorings.
2. Distinguish continuous expectation minimization at p = 0.50 from integer quantization plateaus of n_1(k, p) at k = 3 (n_1 = 3 across [0.20, 0.80]) and k = 4 (n_1 = 6 across [0.40, 0.60]).
3. Verify R(3, 3) = 6, R(3, 4) = 9, and R(4, 4) = 18 via explicit witnesses (C_5, Z_8 circulant {1, 4, 7}, and self-complementary Paley P(17) over F_17) paired with Goodman multiplicity and degree-sum parity.
4. Keep R(5, 5) explicitly labeled OPEN inside [43, 46] (Exoo 1989; Angeltveit & McKay 2026) and state the asymptotic root bracket as lim inf >= sqrt(2) and lim sup <= 4 - epsilon (Campos et al. 2026) without assuming the limit exists or inventing a numerical value for epsilon.

## How it works, in four stages
- Stage 1 (Small Settled Thresholds and Goodman Multiplicity, 1930–1959): Frank Ramsey (1930, DOI 10.1112/plms/s2-30.1.264) showed that every two-coloring of a large enough complete graph contains a monochromatic k-clique. On five vertices, a red pentagon C_5 and its blue pentagram complement avoid monochromatic triangles, whereas on K_6 Goodman’s degree identity (1959, DOI 10.1080/00029890.1959.11989408) gives T_mono = 20 − (1/2)∑ d_r(v)(5 − d_r(v)) ≥ 2 across all 32,768 colorings (attained 1,760 times), pinning R(3, 3) = 6. On eight vertices, the circulant step set {1, 4, 7} avoids red K_3 and blue K_4, while forced 3-regularity on K_9 gives odd degree sum 9 × 3 = 27, pinning R(3, 4) = 9.
- Stage 2 (Quadratic Residues on F_17 and the Open Five-Clique Window, 1955–2026): Greenwood and Gleason (1955, DOI 10.4153/CJM-1955-001-4) colored K_17 by connecting u and v in red whenever (v − u) mod 17 lies in the quadratic residue set {1, 2, 4, 8, 9, 13, 15, 16}. Multiplication by non-residue 3 mod 17 swaps red and blue edges, yielding strongly regular Paley graph P(17) = SRG(17, 8, 3, 4) with zero monochromatic K_4 across all 2,380 four-subsets; combining with R(4, 4) ≤ R(3, 4) + R(4, 3) = 18 settles R(4, 4) = 18. By contrast, R(5, 5) stays open between 43 (Exoo 1989, DOI 10.1002/jgt.3190130113) and 46 (Angeltveit & McKay 2026, DOI 10.1002/jgt.70029).
- Stage 3 (Erdős First-Moment Floor, Convexity at p = 1/2, and Spencer’s Local Lemma, 1947–1975): Paul Erdős (1947, DOI 10.1090/S0002-9904-1947-08785-1) colored edges independently with red probability p, giving expected monochromatic k-cliques E[X_k(n, p)] = C(n, k)[p^C(k,2) + (1 − p)^C(k,2)]. Whenever E[X_k(n, p)] < 1, at least one coloring avoids monochromatic K_k, so R(k, k) ≥ n_1(k, p) + 1. Convexity of p^m + (1 − p)^m minimizes E[X_k] at p = 0.50, yielding asymptotic base √2 ≈ 1.414214; Joel Spencer (1975, DOI 10.1016/0097-3165(75)90071-0) doubled the prefactor to (√2/e) k 2^(k/2) via the Lovász Local Lemma.
- Stage 4 (Asymmetric Book Algorithm, Tier T0–T1 Hypothesis, and Falsification Conditions, 1988–2026): Thomason (1988, DOI 10.1002/jgt.3190120406), Conlon (2009, DOI 10.4007/annals.2009.170.941), and Sah (2023, DOI 10.1215/00127094-2022-0048) shaved sub-exponential factors off Erdős–Szekeres C(2k − 2, k − 1) < 4^k. Campos, Griffiths, Morris, and Sahasrabudhe (2026, DOI 10.4007/annals.2026.203.3.4) achieved an exponential reduction R(k, k) ≤ (4 − ε)^k for a constant ε > 0 via an asymmetric book algorithm. Hypothesis (Tier T0–T1): skewing p off 0.50 drops n_1(k, p) for every k ≥ 5 (from 100 at p = 0.50 to 71 at p = 0.45 and 17 at p = 0.20 when k = 10), yet finite algebraic colorings beat n_1 + 1 at k = 3, 4, 5 while leaving both R(5, 5) ∈ [43, 46] and whether lim R(k, k)^(1/k) exists inside [√2, 4 − ε] open. Any 43-vertex (K_5, K_5)-free coloring refutes R(5, 5) = 43; any family exceeding base √2 narrows the asymptotic gap from below.

## Reference values stated in the essay
- **First-Moment Floor n_1(k, p) + 1**: `R(5, 5) ≥ 12 (n_1 = 11, E = 0.902344)`
- **Binomial Ceiling & LLL Scale**: `C(8, 4) = 70 · Spencer LLL scale 14.72`
- **Published Finite / Book Bracket**: `43 ≤ R(5, 5) ≤ 46 (Exoo 1989; Angeltveit–McKay 2026)`
- **Threshold Status & Open Horizon**: `OPEN FINITE WINDOW [43, 46] · BASE [√2, 4 − ε]`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/math/m15/verify_m15_ramsey_bounds.py
python skills/math/m15/verify_m15_ramsey_bounds.py --planted-defect
```

## Primary source
- https://doi.org/10.1112/plms/s2-30.1.264 (Scite report: https://scite.ai/reports/10.1112/plms/s2-30.1.264)
- What the essay compares against: R(3, 3) = 6 (1,760 extremal K_6 colorings at 2 triangles) · R(4, 4) = 18 via P(17) · 43 ≤ R(5, 5) ≤ 46 (OPEN) · n_1(5, 0.50) = 11 vs C(8, 4) = 70

## Recent research context
- **Breaking the Eighty-Eight-Year Base-Four Ceiling While R(5, 5) Narrows to [43, 46]**: For eighty-eight years after Erdős and Szekeres (1935), upper bounds on diagonal Ramsey numbers R(k, k) remained at base 4 − o(1). Campos, Griffiths, Morris, and Sahasrabudhe (2026, Annals of Mathematics, DOI 10.4007/annals.2026.203.3.4) lowered the exponential base to 4 − ε, giving R(k, k) ≤ (4 − ε)^k via an asymmetric book algorithm, while Angeltveit and McKay (2026, DOI 10.1002/jgt.70029) compressed R(5, 5) into [43, 46].
