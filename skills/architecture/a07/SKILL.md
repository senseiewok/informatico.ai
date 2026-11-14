---
name: barragan-kubelka-munk-radiosity
description: AI-agnostic architectural daylighting and color-physics skill for Luis Barragan chromatic tectonics, Kubelka-Munk pigment reflectance, and Fredholm spectral radiosity.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Luis Barragán's Chromatic Tectonics, Kubelka–Munk Pigment Radiosity & Emotional Spatial Wavefields (Folio A.07)

A plain-text companion to the essay at https://informatico.ai/architecture/a07/ (`A.07 · Barragán Chromatic Tectonics & Radiosity · CSI 09 24 00`, `REV 1.0`, redated `2026-11-02`).

## The governing relation
`K/S = (1 − R_∞)² / (2 R_∞) · B(x,λ) = E(x,λ) + ρ(x,λ) ∫ B(y,λ) F(x,y) dA_y · CSI 09 24 00`

## Rules the essay derives
1. Compute infinite-thickness Kubelka-Munk diffuse reflectance R_inf = 1 + (K/S) - sqrt((K/S)^2 + 2*(K/S)) from absorption K and scattering S.
2. Solve wavelength-resolved enclosure radiosity B_i(lambda) = E_i(lambda) + rho_i(lambda) * sum_j F_ij * B_j(lambda) across 380-780 nm.
3. Maintain matte mineral surface roughness (85-degree specular gloss < 2 GU) so diffuse chromatic bounce dominates over specular glare.

## How it works, in four stages
- Stage 1 (Golden Corridor Spectral Filtering, λ ≈ 582 nm): Sunlight entering Casa Gilardi's yellow-glazed hall strips short-wave blue light, pre-warming the spectral power distribution.
- Stage 2 (Kubelka–Munk Mineral Lime Scattering): Unpolished volcanic-sand lime stucco with K/S = 0.48 yields diffuse reflectance R_∞ = 1 + K/S − √((K/S)² + 2 K/S) = 0.391 with zero specular glare.
- Stage 3 (Fredholm Wall-to-Water Chromatic Radiosity): Multi-bounce inter-reflection between the Rosa Mexicano pier (615 nm) and Cobalt pool (465 nm) amplifies ambient chroma by +31.4%.
- Stage 4 (Torres de Satélite Highway Parallax & Albers Contrast): Monumental 52 m striated concrete prisms shift apparent hue saturation across automotive viewing velocities.

## Reference values stated in the essay
- **Kubelka–Munk Reflectance (R_∞)**: `0.391 (at K/S = 0.48)`
- **Inter-Reflected Chroma Gain**: `+31.4% (Fredholm Cavity)`
- **Dominant Wavelength Pair**: `615 nm Rosa · 465 nm Cobalt`
- **Tectonic Light Verdict**: `LAMBERTIAN SERENITY · PASS`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1364/JOSA.38.000448 (Scite report: https://scite.ai/reports/10.1364/JOSA.38.000448)
- What the essay compares against: Casa Gilardi (1976) · Torres de Satélite (1957) · R_∞ = 0.391

## Recent research context
- **Wavelength-Resolved Kubelka–Munk Radiosity Decodes Luis Barragán's Emotional Architecture of Color**: Combining Paul Kubelka's two-flux pigment scattering theory (JOSA DOI 10.1364/JOSA.38.000448) and Josef Albers's Interaction of Color (1963) with 81-band spectral Fredholm radiosity reveals how Luis Barragán's Casa Gilardi (1976) and highway-scale Torres de Satélite (1957) use matte mineral lime cavities to amplify chromatic saturation by +31.4% without specular glare.
