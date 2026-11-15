---
name: extremal-capset-tensor-rank
description: AI-agnostic extremal combinatorics and algebraic complexity skill for F_3^n Cap Sets, slice-rank polynomial upper bounds, and bilinear matrix multiplication tensor decompositions.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Extremal Cap Sets in F_3^n, Polynomial Method Upper Bounds, and Rank-48 Matrix Tensors (Folio M.03)

A plain-text companion to the essay at https://informatico.ai/math/m03/ (`M.03 · Extremal Combinatorics & Tensors`, `REV 1.4`, redated `2026-11-14`).

## The governing relation
`FunSearch Cap Set (512 in F_3^8) · AlphaEvolve 48 products`

## Rules the essay derives
1. Check cap set three-term progression avoidance exactly: for all distinct x, y, z in S subset F_3^n, x + y + z != 0 (mod 3).
2. Quote the Ellenberg-Gijswijt bound as |S| = o(2.756^n) (their Corollary 5); the constant is the minimum over 0 < x < 1 of (1 + x + x^2)/x^(2/3), about 2.7551. Report the FunSearch F_3^8 size, 512, as the paper reports it.
3. Verify bilinear tensor decomposition sum_{r=1}^R (u_r . A)(v_r . B) w_r = A B exactly satisfies all n^6 Brent equations.

## How it works, in four stages
- Stage 1 (Affine Line-Free Constraint): A subset S ⊂ F_3^n is a Cap Set if no three distinct vectors x, y, z ∈ S satisfy x + y + z = 0 (mod 3).
- Stage 2 (Croot-Lev-Pach & Ellenberg-Gijswijt Polynomial Method): The polynomial method bounds the size of a cap set in F_3^n by o(2.756^n) (Ellenberg-Gijswijt, Corollary 5).
- Stage 3 (FunSearch Priority-Function Discovery): Romera-Paredes et al. report an evolutionary search over Python priority functions that found a 512-point cap set in F_3^8.
- Stage 4 (AlphaEvolve 48-Product Procedure): The AlphaEvolve white paper reports a procedure for 4×4 complex matrices with 48 scalar multiplications, against the 49 that Strassen's 1969 method gives when applied twice (7² = 49).

## Reference values stated in the essay
- **F_3^8 Cap Set Size**: `512 vectors (reported by FunSearch paper)`
- **Ellenberg-Gijswijt Base**: `o(2.756^n) upper bound (Corollary 5)`
- **4×4 Matrix Multiplication Products**: `48 < 49 (reported by AlphaEvolve, complex field)`
- **Exponent if used recursively**: `log_4(48) = 2.7925 (vs log_2(7) = 2.8074)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1038/s41586-023-06924-6 (Scite report: https://scite.ai/reports/10.1038/s41586-023-06924-6)
- What the essay compares against: Ellenberg-Gijswijt o(2.756^n) · 512^(1/8) = 2.1810 (products)

## Recent research context
- **FunSearch Reports a 512-Point Cap Set in F_3^8; AlphaEvolve Reports 48 Products for 4x4 Complex Matrices**: In Nature (Romera-Paredes et al. DOI 10.1038/s41586-023-06924-6), DeepMind's FunSearch paired an LLM with an evaluator and reports a cap set of 512 points in F_3^8. Ellenberg and Gijswijt (Annals of Math. DOI 10.4007/annals.2017.185.1.8) bound cap sets in F_3^n by o(2.756^n). The AlphaEvolve white paper (arXiv:2506.13131) reports a procedure for 4x4 complex matrix multiplication with 48 scalar multiplications. This site reports these results and did not reproduce them.
