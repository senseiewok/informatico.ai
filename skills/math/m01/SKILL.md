---
name: formal-math-modularity
description: AI-agnostic formal mathematics skill for Lean 4 FLT modularity lifting (R=T), Ribet level-lowering, and #3-SAT sunflower sparsification.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Modularity Lifting, Spectral Zero-Density Barriers, and #3-SAT Sparsification (Folio M.01)

A plain-text companion to the essay at https://informatico.ai/math/m01/ (`M.01 · Modularity & Counting`, `REV 1.5`, redated `2026-11-14`).

## The governing relation
`FLT · Taylor-Wiles R=T · #3-SAT sparsification`

## Rules the essay derives
1. Verify Frey curve semistability for prime exponent p >= 3 vs counterfactual p = 2 Pythagorean collapse (3^2 + 4^2 = 5^2).
2. Enforce Taylor-Wiles auxiliary prime patching R_Q = T_Q and cusp-form dimension dim S_2(Gamma_0(2)) = 0.
3. Bound #3-SAT worst-case time by Impagliazzo-Paturi-Zane sunflower sparsification 2^(s_3 * n) near alpha_c = 4.26.

## How it works, in four stages
- Stage 1 (Frey Curve & Semistability): Maps a^p + b^p = c^p to a semistable elliptic curve E/Q with minimal discriminant Δ_E = 2^(-8)(abc)^(2p).
- Stage 2 (Ribet Level-Lowering): Establishes that the mod-p Galois representation ρ_{E,p} is modular of level N = 2, creating a high-energy deductive bottleneck.
- Stage 3 (Taylor-Wiles R_Q = T_Q Patching): Auxiliary sets of primes Q_N make the comparison of R and T tractable. The folio draws this as a barrier falling from 8.39 to 3.59 in kcal/mol-style units; those two numbers are illustrative model values, not quantities found in the mathematics.
- Stage 4 (Cusp Form Contradiction): Forces ρ_{E,p} into weight-2 cusp forms S_2(Γ_0(2)), where dim S_2(Γ_0(2)) = 0 closes the proof.

## Reference values stated in the essay
- **Effective Peak Barrier (model)**: `3.59 vs 8.39 (illustrative units)`
- **Alluvial Hypothesis Flux (model)**: `68.4% (illustrative)`
- **#3-SAT Claim in formal-math/eth**: `2^o(n) stated by its README (not checked here)`
- **Lean 4 Repository Statement**: `29,511 theorems per README (not built here)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.2307/2118559 (Scite report: https://scite.ai/reports/10.2307/2118559)
- What the essay compares against: Model values only: barrier 8.39 → 3.59 (illustrative units) · no proof was built or checked here

## Recent research context
- **A Public Lean 4 Repository States a Complete Formal Proof of Fermat's Last Theorem**: Andrew Wiles's proof appeared in the Annals of Mathematics in 1995 (DOI 10.2307/2118559), with the companion paper by Taylor and Wiles (DOI 10.2307/2118560). The repository https://github.com/anthropics/fermats-last-theorem states that it holds a complete machine-checked Lean 4 proof following Frey, Serre, Ribet, Wiles and Taylor-Wiles, with a page for each of 29,511 theorems, built in part on the Imperial College London project led by Kevin Buzzard. This site reports that statement. It has not built the repository or checked the proof.
