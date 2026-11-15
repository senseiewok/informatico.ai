---
name: zeta-spectral-zero-density
description: AI-agnostic analytic number theory and spectral gap skill for Riemann zeta zero-density bounds N(sigma, T), large sieve inequalities, and Cheeger-Fiedler mixing times.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Riemann Zeta Zero-Density Estimates and Large Sieve Inequalities (Folio M.02)

A plain-text companion to the essay at https://informatico.ai/math/m02/ (`M.02 · Analytic Number Theory`, `REV 1.4`, redated `2026-11-14`).

## The governing relation
`Zero-density estimates · Large Sieve · Zeta23 (README statement)`

## Rules the essay derives
1. Quote zero-density exponents N(sigma, T) <= T^(c(1-sigma) + eps) with their sources: Ingham c = 3/(2-sigma) and Huxley c = 12/5 (both give total exponent 3/5 at sigma = 3/4), and Guth-Maynard c = 30/13.
2. State the Cheeger-Fiedler inequalities h_G^2 / 2 <= lambda_2 <= 2 h_G as classical results, and say when a Markov-chain picture is only an analogy.
3. When citing a Lean 4 repository, report what its README states and whether you built it; do not assert that it is free of sorry unless you checked.

## How it works, in four stages
- Stage 1 (Dirichlet Polynomial Mollification): A mollifier M(s) is a short Dirichlet polynomial chosen so that ζ(s)M(s) stays close to 1 away from zeros; it is a standard tool for studying zeros near the critical line Re(s) = 1/2.
- Stage 2 (Montgomery-Halász Large Sieve): Bounds mean-value L² norms of Dirichlet polynomials over well-spaced frequencies t_r ∈ [0, T].
- Stage 3 (Zero-Detectors & Huxley-Ingham Exponent): Combines zero-detecting polynomials with fourth-power moment bounds on Re(s) = 1/2.
- Stage 4 (The Resulting Bound): Zero-density estimates of the form N(σ, T) ≪ T^(c(1-σ)+ε) limit how many zeros can lie off the critical line. Ingham gives c = 3/(2-σ) and Huxley gives c = 12/5; at σ = 3/4 both give c = 12/5 and the total exponent c(1-σ) = 3/5. Comparing this with a spectral gap is the folio's own analogy.

## Reference values stated in the essay
- **Total Zero-Density Exponent c(σ)(1-σ)**: `0.600 (at σ = 0.75, Ingham and Huxley agree)`
- **Spectral Gap Ratio (λ_2 / λ_max)**: `0.418 (fixed illustrative value)`
- **Zeta23 Statement in formal-math**: `stated by its README (not built or checked here)`
- **Cheeger Inequality Bound**: `h_G² / 2 ≤ λ_2 ≤ 2 h_G (classical)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1515/crll.1989.399.1 (Scite report: https://scite.ai/reports/10.1515/crll.1989.399.1)
- What the essay compares against: Ingham-Huxley Zero-Density N(σ, T) ≪ T^(c(1-σ)+ε), total exponent 3/5 at σ = 3/4

## Recent research context
- **Huxley's Zero-Density Bound, Conrey's Critical-Line Result and a Lean 4 Repository Statement**: Martin Huxley's zero-density estimate N(sigma, T) <= T^(12(1-sigma)/5 + eps) (Invent. Math. DOI 10.1007/BF01418933) and J. B. Conrey's result that more than 2/5 of the zeros of zeta lie on Re(s) = 1/2 (J. Reine Angew. Math. DOI 10.1515/crll.1989.399.1) are classical. The README of anthropics/formal-math also lists a Lean 4 project, zeta23, for a more recent critical-line result. This site reports that statement and has not built the project or checked the mathematics.
