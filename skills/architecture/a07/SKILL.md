---
name: barragan-kubelka-munk-radiosity
description: AI-agnostic architectural daylighting and color-physics skill for Luis Barragan chromatic tectonics, Kubelka-Munk pigment reflectance, and Fredholm spectral radiosity.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Luis Barragán's Chromatic Tectonics, Kubelka–Munk Pigment Radiosity & Emotional Spatial Wavefields (Folio A.07)

A plain-text companion to the essay at https://informatico.ai/architecture/a07/ (`A.07 · Barragán Chromatic Tectonics & Radiosity · CSI 09 24 00`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`K/S = (1 − R_∞)² / (2 R_∞) · B(x,λ) = E(x,λ) + ρ(x,λ) ∫ B(y,λ) F(x,y) dA_y · CSI 09 24 00`

## Rules the essay derives
1. Compute infinite-thickness Kubelka-Munk diffuse reflectance R_inf = 1 + (K/S) - sqrt((K/S)^2 + 2*(K/S)) from absorption K and scattering S.
2. Solve wavelength-resolved enclosure radiosity B_i(lambda) = E_i(lambda) + rho_i(lambda) * sum_j F_ij * B_j(lambda) across 380-780 nm.
3. Maintain matte mineral surface roughness (85-degree specular gloss < 2 GU) so diffuse chromatic bounce dominates over specular glare.

## How it works, in four stages
- Stage 1 (Golden Corridor Spectral Filtering, λ ≈ 582 nm): Sunlight entering Casa Gilardi's yellow-glazed corridor loses much of its short-wave blue light, warming the light that reaches the room (582 nm is an illustrative dominant wavelength).
- Stage 2 (Kubelka–Munk Lime Scattering): For an assumed K/S = 0.48, the infinite-thickness diffuse reflectance is R_∞ = 1 + K/S − √((K/S)² + 2 K/S) = 1.48 − 1.091 = 0.389; the surface is assumed matte (Lambertian).
- Stage 3 (Wall-to-Water Inter-Reflection): In a simplified one-bounce-series model, the gain 1 / (1 − R_∞ F_12) = 1 / (1 − 0.389 × 0.61) gives +31.1% for an assumed view factor F_12 = 0.61; it is an illustrative model value, not a measured change in color.
- Stage 4 (Torres de Satélite Highway Parallax & Albers Contrast): The towers, the tallest about 52 m high, were designed to be seen from cars on the highway, so their silhouettes shift as viewers move.

## Reference values stated in the essay
- **Kubelka–Munk Reflectance (R_∞, Model)**: `0.389 (at K/S = 0.48)`
- **Inter-Reflection Gain (Illustrative)**: `+31.1% (assumed F_12 = 0.61)`
- **Dominant Wavelength Pair (Illustrative)**: `615 nm Rosa · 465 nm Cobalt`
- **Surface Assumption (Model)**: `LAMBERTIAN SURFACES ASSUMED`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1364/JOSA.38.000448 (Scite report: https://scite.ai/reports/10.1364/JOSA.38.000448)
- What the essay compares against: Model values: R_∞ = 0.389 at K/S = 0.48 · +31.1% bounce gain at F_12 = 0.61 (illustrative)

## Recent research context
- **A Kubelka–Munk and Radiosity Reading of Luis Barragán's Architecture of Color**: Using Paul Kubelka's two-flux pigment scattering theory (JOSA DOI 10.1364/JOSA.38.000448) alongside Josef Albers's Interaction of Color (1963), this folio models how matte colored walls in rooms like Luis Barragán's Casa Gilardi (1976) reflect and inter-reflect light: R_∞ = 0.389 at K/S = 0.48, and an illustrative bounce gain of about +31% for an assumed view factor. It measured no building.
