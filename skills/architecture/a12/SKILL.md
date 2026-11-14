---
name: tensegrity-nullspace-skycooling
description: AI-agnostic architectural engineering skill for Pellegrino-Calladine tensegrity equilibrium matrix SVD (s = dim ker(A), m = dim ker(A^T)), geometric prestress stiffening K_G(t_0), and 8-13 um radiative sky-cooling membranes.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Tensegrity Cable-Strut Domes & Radiative Sky-Cooling Envelopes: Pellegrino Equilibrium Nullspaces, Prestress Stiffening & Zero-Energy Cooling (Folio A.12)

A plain-text companion to the essay at https://informatico.ai/architecture/a12/ (`A.12 · Tensegrity Cable-Strut Domes & 8–13 μm Sky-Cooling Canopies · ASCE 19`, `REV 1.0`, redated `2026-11-07`).

## The governing relation
`A t = f · K_T = K_E + K_G(t_0) ≻ 0 · P_cool = P_rad(T_s) − P_atm(T_amb) − P_sun`

## Rules the essay derives
1. Compute Singular Value Decomposition of equilibrium matrix A to extract self-stress vector t_0 in ker(A) with strictly positive tension in all cables.
2. Verify first-order prestress stability by checking u^T * K_G(t_0) * u > 0 for all inextensional mechanism modes u in ker(A^T).
3. Evaluate net daytime radiative cooling flux q_net = P_rad(T_s) - P_atm(T_amb) - (1 - R_solar) * I_sun across the 8-13 um atmospheric window.

## How it works, in four stages
- Stage 1 (Snelson–Fuller Islands of Compression in an Ocean of Tension): Isolated steel compression struts float without touching one another, suspended inside a continuous prestressed cable net (Calladine 1978, DOI 10.1016/0020-7683(78)90052-5).
- Stage 2 (Pellegrino–Calladine Equilibrium Matrix SVD): Singular Value Decomposition of the equilibrium matrix A (Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4) identifies s = dim ker(A) self-stress states and m = dim ker(Aᵀ) infinitesimal mechanisms.
- Stage 3 (Geometric Prestress Stiffening K_G(t_0) ≻ 0): Just as tightening a guitar string raises its pitch, cable prestress t_0 makes the geometric stiffness matrix K_G(t_0) positive-definite on the mechanism subspace, locking the dome at 12 kg/m².
- Stage 4 (Daytime Radiative Sky-Cooling Membrane Canopy, Continuing A.08): Cladding the tensegrity cable dome in a 97%-solar-reflective, 8–13 μm infrared-emissive fluoropolymer membrane (Raman et al. 2014, DOI 10.1038/nature13883) radiates 98.4 W/m² straight to 3 K outer space.

## Reference values stated in the essay
- **Tangent Stiffness λ_min(K_E + K_G)**: `+42.8 kN/m (STIFFENED PASS)`
- **Structural Steel Aerial Mass**: `12.4 kg/m² (120 m Span)`
- **Net Daytime Sky-Cooling Flux**: `98.4 W/m² (8–13 μm Window)`
- **Sub-Ambient Canopy Drop (ΔT)**: `−5.2 °C · 0 kWh COMPRESSOR`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1126/science.aat9513 (Scite report: https://scite.ai/reports/10.1126/science.aat9513)
- What the essay compares against: t_0 = 185 kN · m = 1 Stiffened Mechanism · q_net = 98.4 W/m² ⇒ ΔT = −5.2 °C Below Ambient

## Recent research context
- **Prestressed Tensegrity Cable Domes & 8–13 μm Photonic Membranes Cool Urban Plazas by 5.2 °C With Zero Power**: Synthesizing Sergio Pellegrino and C. R. Calladine's equilibrium matrix SVD (DOI 10.1016/0020-7683(86)90014-4) with Aaswath Raman's daytime radiative sky cooling (DOI 10.1038/nature13883) and open-source NREL/EnergyPlus creates 12.4 kg/m² civic canopies that passively cool cities.
