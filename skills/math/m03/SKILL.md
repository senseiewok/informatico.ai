---
name: extremal-capset-tensor-rank
description: AI-agnostic extremal combinatorics and algebraic complexity skill for F_3^n Cap Sets, slice-rank polynomial upper bounds, and bilinear matrix multiplication tensor decompositions.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Extremal Cap Sets in F_3^n, Polynomial Method Upper Bounds, and Rank-48 Matrix Tensors (Folio M.03)

A plain-text companion to the essay at https://informatico.ai/math/m03/ (`M.03 · Extremal Combinatorics & Tensors`, `REV 1.3`, redated `2026-11-06`).

## The governing relation
`FunSearch Cap Set (≥ 512) · AlphaEvolve Rank-48`

## Rules the essay derives
1. Verify Cap Set three-term progression avoidance: for all distinct x, y, z in S subset F_3^n, x + y + z != 0 (mod 3).
2. Enforce Ellenberg-Gijswijt slice-rank upper base ((1 + 2*theta)/theta^(2/3)) = 2.755104 vs FunSearch F_3^8 lower bound |S| >= 512.
3. Verify bilinear tensor decomposition sum_{r=1}^R (u_r . A)(v_r . B) w_r = A B exactly satisfies all n^6 Brent equations.

## How it works, in four stages
- Stage 1 (Affine Line-Free Constraint): A subset S ⊂ F_3^n is a Cap Set if no three distinct vectors x, y, z ∈ S satisfy x + y + z = 0 (mod 3).
- Stage 2 (Croot-Lev-Pach & Ellenberg-Gijswijt Polynomial Method): Vanishing slice rank of the indicator polynomial bounds |S| ≤ 3 · (2.755104)^n.
- Stage 3 (FunSearch Priority-Function Discovery): Evolutionary LLM search over Python priority functions constructs an explicit 512-vector cap set in F_3^8.
- Stage 4 (AlphaEvolve Rank-48 Tensor Decomposition): Beats Strassen's 1969 2-level recursion (7² = 49) by discovering a 48-product decomposition for 4×4 complex matrices.

## Reference values stated in the essay
- **F_3^8 Cap Set Lower Bound**: `512 vectors (FunSearch)`
- **Ellenberg-Gijswijt Base**: `2.7551^n Upper Bound`
- **4×4 Matrix Tensor Rank**: `48 < 49 (AlphaEvolve)`
- **Asymptotic Exponent ω_4**: `log_4(48) = 2.7925`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1038/s41586-023-06924-6 (Scite report: https://scite.ai/reports/10.1038/s41586-023-06924-6)
- What the essay compares against: Ellenberg-Gijswijt O(2.756^n) vs |S| ≥ 2.181^n

## Recent research context
- **FunSearch Evolutionary LLM Search (|S| >= 512 in F_3^8) Meets AlphaEvolve Rank-48 4x4 Matrix Tensors**: In Nature (Romera-Paredes et al. DOI 10.1038/s41586-023-06924-6), DeepMind's FunSearch paired an LLM with a deterministic verifier to construct a 512-vector Cap Set in F_3^8 beneath the Ellenberg–Gijswijt slice-rank ceiling (2.7551^n, Annals of Math. DOI 10.4007/annals.2017.185.1.8), while AlphaEvolve discovered a Rank-48 tensor decomposition for 4x4 complex matrix multiplication—directly informing non-immunogenic synonymous CFTR mRNA codon packing.
