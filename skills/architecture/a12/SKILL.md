---
name: tensegrity-nullspace-skycooling
description: AI-agnostic architectural engineering skill for Pellegrino-Calladine tensegrity equilibrium matrix SVD (s = dim ker(A), m = dim ker(A^T)), geometric prestress stiffening K_G(t_0), and 8-13 um radiative sky-cooling membranes.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Tensegrity Cable-Strut Domes & Radiative Sky-Cooling Envelopes: Pellegrino Equilibrium Nullspaces, Prestress Stiffening & Zero-Energy Cooling (Folio A.12)

A plain-text companion to the essay at https://informatico.ai/architecture/a12/ (`A.12 · Tensegrity Cable-Strut Domes & 8–13 μm Sky-Cooling Canopies · ASCE 19`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`A t = f · K_T = K_E + K_G(t_0) ≻ 0 · P_cool = P_rad(T_s) − P_atm(T_amb) − P_sun`

## Rules the essay derives
1. Compute Singular Value Decomposition of equilibrium matrix A to extract self-stress vector t_0 in ker(A) with strictly positive tension in all cables.
2. Verify first-order prestress stability by checking u^T * K_G(t_0) * u > 0 for all inextensional mechanism modes u in ker(A^T).
3. Evaluate net daytime radiative cooling flux q_net = P_rad(T_s) - P_atm(T_amb) - (1 - R_solar) * I_sun across the 8-13 um atmospheric window.

## How it works, in four stages
- Stage 1 (Snelson–Fuller Islands of Compression in an Ocean of Tension): Isolated steel compression struts float without touching one another, suspended inside a continuous prestressed cable net (Calladine 1978, DOI 10.1016/0020-7683(78)90052-5).
- Stage 2 (Pellegrino–Calladine Equilibrium Matrix SVD): Singular Value Decomposition of the equilibrium matrix A (Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4) identifies s = dim ker(A) self-stress states and m = dim ker(Aᵀ) infinitesimal mechanisms.
- Stage 3 (Geometric Prestress Stiffening K_G(t_0) ≻ 0): Just as tightening a guitar string raises its pitch, cable prestress t_0 makes the geometric stiffness matrix K_G(t_0) positive on the mechanism modes, so the prestressed structure is stiff in the model. The structural mass figure of 12.4 kg/m² shown on this page is illustrative, not a design result.
- Stage 4 (Daytime Radiative Sky-Cooling Membrane Canopy, Continuing A.08): The membrane is assumed to reflect 97% of an assumed 1,000 W/m² of sunlight, as the photonic surface of Raman et al. did (2014, DOI 10.1038/nature13883), so it absorbs 30 W/m². The model assigns a net radiative exchange with the sky of 128.4 W/m² at air temperature, a fixed illustrative value, so q_net = 128.4 − 30 = 98.4 W/m². Divided by an assumed combined heat-exchange coefficient of about 18.9 W/(m²·K), that gives a membrane surface about 5.2 °C below the air in the model.

## Reference values stated in the essay
- **Tangent Stiffness λ_min(K_E + K_G)**: `+42.8 kN/m (Illustrative, Positive in Model)`
- **Structural Steel Aerial Mass**: `12.4 kg/m² (Illustrative, 120 m Span)`
- **Net Daytime Sky-Cooling Flux**: `98.4 W/m² (Model, at Air Temperature)`
- **Sub-Ambient Canopy Drop (ΔT)**: `−5.2 °C Membrane Surface (Model)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1126/science.aat9513 (Scite report: https://scite.ai/reports/10.1126/science.aat9513)
- What the essay compares against: Model values: t_0 = 185 kN · q_net = 98.4 W/m² at air temperature ⇒ ΔT ≈ −5.2 °C for an assumed 18.9 W/(m²·K)

## Recent research context
- **A Design Study: Prestressed Tensegrity Cable Domes Clad in 8–13 μm Radiative-Cooling Membranes**: This folio pairs Sergio Pellegrino and C. R. Calladine's equilibrium-matrix analysis of prestressed frameworks (DOI 10.1016/0020-7683(86)90014-4) with daytime radiative sky cooling as reported by Raman et al. (DOI 10.1038/nature13883). In its model the membrane gives 98.4 W/m² of cooling at air temperature and sits about 5.2 °C below the air for an assumed heat-exchange coefficient. Model values, not measurements; nothing was built or simulated.
