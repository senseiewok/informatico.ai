---
name: kakeya-3d-guth-maynard-zero-density
description: AI-agnostic harmonic analysis and analytic number theory skill for the Wang-Zahl 3D Kakeya preprint (dim_H(K) = 3 as stated there), the Guth-Maynard 30/13 Riemann zero-density estimate, and reading Lean 4 repository READMEs such as anthropics/formal-math (zeta23).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# The 3D Kakeya Preprint of Wang and Zahl and the Guth–Maynard Zero-Density Estimate (Folio M.11)

A plain-text companion to the essay at https://informatico.ai/math/m11/ (`M.11 · 3D Kakeya Conjecture (arXiv:2502.17655) & Guth–Maynard 30/13 (arXiv:2405.20552)`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`dim_H(K) = dim_M(K) = 3 for Kakeya K ⊂ ℝ³ (as stated in the Wang–Zahl preprint) · N(σ, T) ≤ T^(30(1−σ)/13+o(1)) (Guth–Maynard)`

## Rules the essay derives
1. Bound the union volume of direction-separated delta-tubes in R^3 via |union T_i| >= C_eps * delta^eps * sum |T_i| to enforce dim_H(K) = dim_M(K) = 3.
2. Evaluate the Guth-Maynard zero-density bound N(sigma, T) <= T^(30(1 - sigma)/13 + o(1)) as stated in its abstract, compared with Huxley's 12/5 = 2.40; 30/13 = 2.3077.
3. Before citing a Lean repository as a formalisation of a theorem, read its README to verify which theorem it covers, and report what the README said with the date you read it (the anthropics/formal-math README read on 2026-11-14 lists zeta23 as Alpöge–Furman and does not list Guth–Maynard).

## How it works, in four stages
- Stage 1 (Besicovitch's 1919 Needle Paradox & The 3D Kakeya Conjecture): A unit needle can be rotated 360° inside a set of arbitrarily tiny volume (measure zero), yet the Kakeya Conjecture asserts its fractal Hausdorff dimension in ℝ³ must still be the full 3.000.
- Stage 2 (Wang–Zahl 2025, arXiv:2502.17655): In a preprint, Hong Wang and Joshua Zahl study sets of δ-tubes in ℝ³ in which not too many tubes lie inside a common convex set, and state a proof that the union of such tubes has almost maximal volume, from which they deduce that every Kakeya set in ℝ³ has Minkowski and Hausdorff dimension 3.
- Stage 3 (Guth–Maynard, arXiv:2405.20552; Annals 2026): New bounds on how often Dirichlet polynomials take large values give the zero-density estimate N(σ, T) ≤ T^(30(1−σ)/13+o(1)), improving on the uniform exponent 12/5 = 2.40 of Huxley (DOI 10.1007/BF01418933) and on the bound at σ = 3/4 going back to Ingham (1940).
- Stage 4 (Consequence and formal context): Guth and Maynard also deduce asymptotics for primes in short intervals of length x^(17/30+o(1)). Neither result is listed in the README of anthropics/formal-math read on 2026-11-14; that README lists Lean 4 projects on other theorems (see Act IV).

## Reference values stated in the essay
- **3D Kakeya Hausdorff Dimension**: `dim_H(K) = 3 (Wang–Zahl preprint)`
- **Zero-Density Exponent (Guth–Maynard)**: `30/13 ≈ 2.3077 (< 12/5 = 2.400)`
- **Short-Interval Prime Asymptotics**: `intervals of length x^(17/30+o(1)); 17/30 ≈ 0.5667`
- **Lean 4 Status**: `Not listed in the formal-math README (read 2026-11-14)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.4007/annals.2015.182.1.9 (Scite report: https://scite.ai/reports/10.4007/annals.2015.182.1.9)
- What the essay compares against: dim_H(K_3D) = 3 (Wang–Zahl preprint) · zero-density exponent 30/13 ≈ 2.3077 < 12/5 = 2.400 · primes in short intervals of length x^(17/30+o(1))

## Recent research context
- **Wang–Zahl on the 3D Kakeya Conjecture & Guth–Maynard on Zero Density**: A preprint by Hong Wang and Joshua Zahl (arXiv:2502.17655) states a proof that every Kakeya set in R^3 has dimension 3, and Larry Guth and James Maynard (Annals of Mathematics, DOI 10.4007/annals.2026.203.2.6) lower the zero-density exponent to 30/13 from the 12/5 of Huxley (DOI 10.1007/BF01418933). Two separate results, read side by side.
