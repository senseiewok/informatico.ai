---
name: riemannian-color-schrodinger-geodesic
description: AI-agnostic colorimetry and differential-geometry skill for Grassmann projections, Cohen-Kappauf metamer projectors, MacAdam ellipses, Weber-Fechner geodesics, and non-Riemannian large-difference limits.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Riemannian Differential Geometry of Color Perception: Helmholtz–Schrödinger Geodesics, MacAdam Metric Tensors & Grassmann Spectral Hilbert Projections (Folio M.08)

A plain-text companion to the essay at https://informatico.ai/math/m08/ (`M.08 · Riemannian Color Manifold & Metamer Nullspace · CIE`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`Π_T: L²([380,780]) → ℝ³ · ds² = ∑ g_ij(x) dx^i dx^j (x ∈ ℝ³₊) · ẍ^k + Γ^k_ij ẋ^i ẋ^j = 0`

## Rules the essay derives
1. Map reflectance rho(lambda) in [0, 1] to x_k = int S(lambda, T) rho(lambda) c_bar_k(lambda) d_lambda in R^3_{>=0} (strictly positive rho(lambda) in (0, 1] lands in R^3_+), keeping linear codomain R^3 distinct from R^3_+.
2. Use Cohen and Kappauf (1982) projector A(A^T A)^{-1}A^T on radiant stimuli, or weighted P_{A_T} = A_T (A_T^T A_T)^{-1} A_T^T on discrete reflectances rho, to separate 3D fundamentals from metameric blacks.
3. Distinguish Helmholtz (1891-1892) self-light offsets c_k from Stiles (1946) unequal Fechner weights in model ds^2 = sum a_k (dx^k / x^k)^2, and note Bujack et al. (2022) diminishing returns at large color intervals.

## How it works, in four stages
- Stage 1 (Grassmann Projection Π_T: L² → ℝ³): Positive reflectance ρ(λ) ∈ (0, 1] maps to cone signals x_k = ∫ S(λ, T_illum) ρ(λ) c̄_k(λ) dλ in ℝ³₊ (Grassmann 1853).
- Stage 2 (Reflectance Projector): Weighted P_{A_T} = A_T (A_Tᵀ A_T)⁻¹ A_Tᵀ splits discrete reflectances ρ into a 3D fundamental component and metameric black (adapting Cohen & Kappauf 1982).
- Stage 3 (Weber–Fechner Model Metric): Combining zero self-light offsets (c_k = 0 in Helmholtz 1891–1892) with Stiles’s (1946) Fechner weights yields model ds² = ∑ a_k (dx^k / x^k)².
- Stage 4 (Log-Geodesics & Scale Caveat): Solving ẍ^k + Γ^k_ij ẋ^i ẋ^j = 0 gives x^k(t) = x^k(0)^(1−t) x^k(1)^t (+9.4° illustrative); Bujack et al. (2022) show diminishing returns at large steps.

## Reference values stated in the essay
- **Geodesic Arc Length (model)**: `Δs_geo = 42.8 at t = 0.50 (fixed illustrative)`
- **Chord vs. Geodesic Hue Shift (model)**: `+9.4° for the flat chord (fixed illustrative)`
- **Near-Metamer Index (model)**: `ΔE_00 = 0.18 at 6500 K (fixed illustrative)`
- **Model Geometry**: `c_k = 0 Weber–Fechner metric (model, not a proof)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1002/andp.19203682202 (Scite report: https://scite.ai/reports/10.1002/andp.19203682202)
- What the essay compares against: dim ker(Π_T) = ∞ · illustrative Δs_geo = 42.8, +9.4°, ΔE_00 = 0.18

## Recent research context
- **Schrödinger's 1920 Color Metric, Cohen–Kappauf Metamers & Non-Riemannian Limits**: Links Grassmann's 1853 laws (DOI 10.1002/andp.18531650505) and Cohen & Kappauf's projector (DOI 10.2307/1422186) with Schrödinger–Stiles line elements (DOI 10.1002/andp.19203682202; DOI 10.1088/0959-5309/58/1/305), MacAdam ellipses (DOI 10.1364/JOSA.32.000247), and Bujack et al. (2022, DOI 10.1073/pnas.2119753119). Values shown are illustrative.
