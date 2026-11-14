---
name: zeta-spectral-zero-density
description: AI-agnostic analytic number theory and spectral gap skill for Riemann zeta zero-density bounds N(sigma, T), large sieve inequalities, and Cheeger-Fiedler mixing times.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Riemann Zeta Zero-Density Estimates, Large Sieve Inequalities, and XiPrime Spectral Bounds (Folio M.02)

A plain-text companion to the essay at https://informatico.ai/math/m02/ (`M.02 · Analytic Number Theory`, `REV 1.3`, redated `2026-11-06`).

## The governing relation
`Zeta23 · Challenge/XiPrime.lean · Large Sieve`

## Rules the essay derives
1. Bound zero-density exceptions N(sigma, T) in 1/2 < sigma <= 1 using Ingham N(sigma, T) <= T^(3(1-sigma)/(2-sigma) + eps) and Huxley N(sigma, T) <= T^(12(1-sigma)/5 + eps).
2. Verify Cheeger-Fiedler spectral conductance bounds h_G^2 / (2 d_max) <= lambda_2 <= 2 h_G for Markovian relaxation.
3. Require zero sorryAx axioms in transitive Lean 4 dependency cones for XiPrime spectral lemmas.

## How it works, in four stages
- Stage 1 (Dirichlet Polynomial Mollification): Constructs a mollifier M(s) to dampen normal oscillations of ζ(s) off the critical line Re(s) = 1/2.
- Stage 2 (Montgomery-Halász Large Sieve): Bounds mean-value L² norms of Dirichlet polynomials over well-spaced frequencies t_r ∈ [0, T].
- Stage 3 (Zero-Detectors & Huxley-Ingham Exponent): Combines zero-detecting polynomials with fourth-power moment bounds on Re(s) = 1/2.
- Stage 4 (XiPrime.lean Spectral Barrier): Certifies in Lean 4 that zero-density exceptions decay as T^(A(1-σ)(3-2σ)), locking spectral relaxation.

## Reference values stated in the essay
- **Zero-Density Exponent c(σ)**: `0.600 (at σ = 0.75)`
- **Spectral Gap Ratio (λ_2 / λ_max)**: `0.418`
- **XiPrime Lean 4 Status**: `0 sorryAx (Complete)`
- **Cheeger Inequality Bound**: `h_G² / 2 ≤ λ_2 ≤ 2 h_G`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1515/crll.1989.399.1 (Scite report: https://scite.ai/reports/10.1515/crll.1989.399.1)
- What the essay compares against: Ingham-Huxley Zero-Density N(σ, T) ≤ T^(c(1-σ))

## Recent research context
- **Machine-Checked Riemann XiPrime Bounds, Conrey Mollifiers & Huxley Zero-Density Crossover**: Uniting Martin Huxley's zero-density estimate N(sigma, T) <= T^(12(1-sigma)/5 + eps) (Invent. Math. DOI 10.1007/BF01418933) and J. B. Conrey's critical-line mollifier (> 2/5 of Riemann zeros on Re(s) = 1/2, J. Reine Angew. Math. DOI 10.1515/crll.1989.399.1) with Anthropic's Lean 4 Zeta23 and Challenge/XiPrime.lean formalizations, spectral gap bounds map directly onto Cheeger-Fiedler Markovian relaxation in CFTR ion channel gating (DOI 10.1085/jgp.200609558).
