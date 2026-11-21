---
name: barragan-kubelka-munk-radiosity
description: AI-agnostic architectural daylighting and color-physics skill for Luis Barragan chromatic tectonics, Kubelka-Munk pigment reflectance, and Fredholm diffuse radiosity.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Luis Barragán's Chromatic Tectonics, Kubelka–Munk Pigment Radiosity & Emotional Spatial Wavefields (Folio A.07)

A plain-text companion to the essay at https://informatico.ai/architecture/a07/ (`A.07 · Barragán Chromatic Tectonics & Radiosity · CSI 09 24 00`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`K/S = (1 − R_∞)² / (2 R_∞) · B(x,λ) = E(x,λ) + ρ(x,λ) ∫ B(y,λ) F(x,y) dA_y · CSI 09 24 00`

## Rules the essay derives
1. Compute infinite-thickness Kubelka-Munk diffuse reflectance R_inf = 1 + (K/S) - sqrt((K/S)^2 + 2*(K/S)) from absorption K and scattering S (Kubelka 1948, DOI 10.1364/JOSA.38.000448).
2. Solve wavelength-resolved diffuse radiosity B_i(lambda) = E_i(lambda) + rho_i(lambda) * sum_j F_ij * B_j(lambda) across 380-780 nm (Goral et al. 1984, DOI 10.1145/800031.808601; Ruppertsberg & Bloj 2008, DOI 10.3758/BRM.40.1.304).
3. Specify matte, vapor-permeable lime plaster (Cultrone et al. 2005, DOI 10.1016/j.cemconres.2004.12.012; Parra-Fernández & Varas-Muriel 2025, DOI 10.3989/mc.2025.379124) with an unmeasured 85-degree gloss < 2 GU target so diffuse bounce dominates over specular glare.

## How it works, in four stages
- Stage 1 (Corridor Spectral Filtering, λ ≈ 582 nm): In Casa Gilardi (1976; Coelho 2015, DOI 10.4000/ambiances.606), daylight passing yellow glazing loses short-wave blue light; about 582 nm is an illustrative dominant wavelength.
- Stage 2 (Kubelka–Munk Scattering): For K/S = 0.48, Kubelka's infinite-thickness equation (1948, DOI 10.1364/JOSA.38.000448) gives R_∞ = 1 + K/S − √((K/S)² + 2 K/S) = 0.389, assuming a matte Lambertian layer.
- Stage 3 (Enclosure Inter-Reflection): Following the diffuse radiosity balance (Goral et al. 1984, DOI 10.1145/800031.808601), a one-parameter enclosure series with effective return factor F_12 = 0.61 gives gain 1 / (1 − R_∞ F_12) − 1 ≈ +31.1% (multiplier 1.311) at R_∞ = 0.389—an illustrative model value, not a measured color shift.
- Stage 4 (Torres de Satélite Parallax & Albers Contrast): Built by Barragán and Mathias Goeritz (1957–58; Pelletier 2008, DOI 10.1111/j.1531-314X.2008.00234.x), the towers—the tallest about 52 m—shift silhouette from moving cars while juxtaposed planes illustrate relational contrast (Albers 1963).

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
- **A Kubelka–Munk and Radiosity Reading of Luis Barragán's Architecture of Color**: Combining Paul Kubelka's two-flux scattering law (1948, DOI 10.1364/JOSA.38.000448), diffuse radiosity (Goral et al. 1984, DOI 10.1145/800031.808601), and Josef Albers's Interaction of Color (1963), this folio models how matte walls in rooms such as Casa Gilardi (Coelho 2015, DOI 10.4000/ambiances.606) inter-reflect light: R_∞ = 0.389 at K/S = 0.48 and an illustrative +31.1% bounce gain at F_12 = 0.61. No building was measured.
