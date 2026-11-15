---
name: riemannian-color-schrodinger-geodesic
description: AI-agnostic mathematical colorimetry and differential-geometry skill for Grassmann spectral Hilbert projections, Cohen metameric black nullspaces, MacAdam metric tensors, and Schrodinger color geodesics.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Riemannian Differential Geometry of Color Perception: Helmholtz–Schrödinger Geodesics, MacAdam Metric Tensors & Grassmann Spectral Hilbert Projections (Folio M.08)

A plain-text companion to the essay at https://informatico.ai/math/m08/ (`M.08 · Riemannian Color Manifold & Metamer Nullspace · CIE`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`ds² = ∑ g_ij(x) dx^i dx^j · ẍ^k + Γ^k_ij ẋ^i ẋ^j = 0 · Π: L²([380,780]) → ℝ³₊`

## Rules the essay derives
1. Project spectral reflectance R(lambda) under illuminant S(lambda, T) onto tristimulus cone space via x_k = int_{380}^{780} S(lambda, T) * R(lambda) * c_bar_k(lambda) d_lambda.
2. Decompose R = P_R * R + (I - P_R) * R using Cohen's projection matrix P_R = A * (A^T * A)^{-1} * A^T to isolate fundamental color from metameric blacks in ker(Pi).
3. Integrate Riemannian color geodesics under a stated model metric ds^2 = g_ij(x) dx^i dx^j rather than Euclidean chords, and report that the hue paths depend on the chosen metric.

## How it works, in four stages
- Stage 1 (Grassmann Hilbert Space Projection Π: L² → ℝ³₊): Continuous electromagnetic spectra I(λ) project onto 3 cone coordinates X_k = ∫ S(λ, T_illum) R(λ) c̄_k(λ) dλ.
- Stage 2 (Cohen's Fundamental Metamer Decomposition): Because dim ker(Π) = ∞, any spectrum decomposes into R(λ) = R*(λ) + B(λ), where metameric black B(λ) vanishes under D65 (6500 K) but emerges at sunset (3000 K).
- Stage 3 (Helmholtz-Type Line Element g_ij, the folio's model): Discrimination ellipses such as those MacAdam measured in 1942 show that equal perceptual steps are not equal Euclidean steps. The folio models this with a Helmholtz-type line element ds² = ∑ a_k (dx^k / x^k)².
- Stage 4 (Geodesic Hue Interpolation, model): Solvingẍ^k + Γ^k_ij ẋ^i ẋ^j = 0 for that model metric between a cobalt blue and a magenta (rosa mexicano) gives a curved path. The +9.4° hue difference from a flat RGB chord is an illustrative model value, not a measured Abney-effect correction.

## Reference values stated in the essay
- **Riemannian Geodesic Distance (model)**: `ds_geo = 42.8 (illustrative units, t = 0.50)`
- **Chord vs. Geodesic Hue Difference (model)**: `+9.4° for the flat chord (illustrative)`
- **Illuminant Metamerism Index (model)**: `ΔE_00 = 0.18 at 6500 K (illustrative)`
- **Model Geometry**: `Helmholtz-type metric (a model, not a proof)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1002/andp.19203682202 (Scite report: https://scite.ai/reports/10.1002/andp.19203682202)
- What the essay compares against: dim ker(Π) = ∞ · model hue drift and ΔE_00 values are illustrative

## Recent research context
- **Schrödinger's 1920 Color Metric and the Spectral Nullspace Behind Metamerism**: A teaching study linking Grassmann's 1853 laws of color mixing, read as a projection to three dimensions, with Erwin Schrödinger's Riemannian theory of color measurement (Annalen der Physik DOI 10.1002/andp.19203682202) and David MacAdam's discrimination ellipses (JOSA DOI 10.1364/JOSA.32.000247). Hue paths and values shown come from a model metric.
