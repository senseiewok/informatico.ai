---
name: pfr-entropic-combinatorics
description: AI-agnostic additive combinatorics and universal algebra skill for Ruzsa entropic distance, Polynomial Freiman-Ruzsa coset bounds, and equational magma implication graphs.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Polynomial Freiman–Ruzsa (PFR) Entropy Calculus and the 22-Million Equational Magma Graph (Folio M.04)

A plain-text companion to the essay at https://informatico.ai/math/m04/ (`M.04 · Additive Combinatorics & Algebra`, `REV 1.2`, redated `2026-11-14`).

## The governing relation
`PFR entropy proof · Lean 4 project (README) · 22,028,942 magma-law pairs`

## Rules the essay derives
1. Compute Ruzsa entropic distance d(X, Y) = H(X - Y') - 0.5*(H(X) + H(Y')) for independent copies X, Y' on abelian groups.
2. State the Ruzsa triangle inequality d(X, Z) <= d(X, Y) + d(Y, Z) and the PFR covering bound <= 2 * K^12 as results of the cited paper and project README.
3. Treat an implication between magma laws as established only when a Lean proof or a finite counterexample is cited, and say when you have not checked it.

## How it works, in four stages
- Stage 1 (Small Doubling Hypothesis): A subset A ⊂ F_2^n satisfies |A + A| ≤ K|A|, indicating hidden approximate subgroup structure.
- Stage 2 (Ruzsa Entropic Triangle Inequality): Defines entropic distance d(X, Y) = H(X - Y') - (H(X) + H(Y'))/2 and evaluates submodularity bounds.
- Stage 3 (Tau-Minimizer): The proof studies a minimizer of an entropic functional τ and uses it to show that d(X, U_H) is small for the uniform distribution U_H on a subgroup H. This page's slider is a simplified picture of that step, not the paper's argument.
- Stage 4 (Polynomial Coset Covering): The theorem, as stated in the README of the Lean project, says A is covered by at most 2·K^12 cosets of a subspace H of size at most |A|. Separately, the Equational Theories project concerns 4,694 × 4,693 = 22,028,942 ordered pairs of magma laws.

## Reference values stated in the essay
- **Polynomial Coset Bound**: `≤ 2 · K^12 Cosets (per project README)`
- **Equational Theories Pairs**: `22,028,942 ordered pairs (4694 × 4693; progress not checked here)`
- **Lean 4 Project Status**: `README: main proof formalized (not built here)`
- **Entropic Contraction Picture**: `simplified illustration, not the paper's argument`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.4007/annals.2025.201.2.5 (Scite report: https://scite.ai/reports/10.4007/annals.2025.201.2.5)
- What the essay compares against: Doubling |A + A| ≤ K|A| ⇒ covered by ≤ 2K^12 cosets (as stated in the project README)

## Recent research context
- **Gowers, Green, Manners & Tao's Shannon-Entropy Proof of PFR, and Two Public Lean 4 Projects**: Published in Annals of Mathematics (Gowers, Green, Manners & Tao 2025, DOI 10.4007/annals.2025.201.2.5), the proof covers a set A in F_2^n with |A + A| <= K|A| by at most 2 K^12 cosets, as stated in the README of teorth/pfr, which also states that its Lean 4 formalization was completed. The Equational Theories project concerns 4,694 magma laws and 22,028,942 ordered pairs. This site reports those statements and has not built either project.
