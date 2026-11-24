---
name: tensegrity-nullspace-skycooling
description: Explanatory companion for Pellegrino-Calladine tensegrity equilibrium matrix subspaces (s = dim ker(A), m = dim ker(A^T)), geometric prestress stiffening K_G(t_0), and exterior 8-13 um sky-cooling arithmetic. Explanation only, not a design method; no folio number may be used on a real structure.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Tensegrity Cable-Strut Domes & Radiative Sky-Cooling Envelopes: Pellegrino Equilibrium Nullspaces, Prestress Stiffening & Zero-Energy Cooling (Folio A.12)

A plain-text companion to the essay at https://informatico.ai/architecture/a12/ (`A.12 · Tensegrity Frameworks & Exterior 8–13 μm Sky-Cooling Pairing`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`A t = f · K_T = K_E + K_G(t_0) ≻ 0 · q_net(T_a) = q_sky_net(T_a) − (1 − R_solar) I_sun`

## Rules the essay derives
1. Explanation only, not a structural or thermal design method: none of this folio's untested numbers (185 kN, +42.8 kN/m, 12.4 kg/m^2, 98.4 W/m^2, -5.2 C) may be used on a real structure; analyze the four subspaces of equilibrium matrix A (Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4).
2. In an idealized pin-jointed frame, check u^T * K_G(t_0) * u > 0 on mechanism modes u in ker(A^T); this omits strut buckling, cable slackening, wind flutter, ponding, and support movement.
3. Separate radiative arithmetic from statics: in q_net(T_a) = q_sky_net(T_a) - (1 - R_solar) * I_sun, state every assumed constant (R_solar = 0.97, I_sun = 1,000 W/m^2, sky exchange 128.4 W/m^2, h_comb = 18.9 W/(m^2*K)) as model values.

## How it works, in four stages
- Stage 1 (Snelson–Fuller Floating Compression): Isolated compression struts sit suspended without touching one another inside a continuous tensioned cable network (Calladine 1978, DOI 10.1016/0020-7683(78)90052-5).
- Stage 2 (Pellegrino–Calladine Equilibrium Matrix Subspaces): Row-echelon subspace analysis of equilibrium matrix A (Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4) separates s = dim ker(A) self-stress states from m = dim ker(Aᵀ) mechanisms.
- Stage 3 (Prestress Stiffening & Safety Boundary): In an idealized pin-jointed model, cable prestress t_0 makes K_G(t_0) positive on mechanism modes. Explanation only, not a design method; no figure here (185 kN, +42.8 kN/m, 12.4 kg/m² for 120 m) may be used on a real structure.
- Stage 4 (Separate Sky-Cooling Arithmetic, Continuing A.08): Assuming R_solar = 0.97 under I_sun = 1,000 W/m² (after Raman et al. 2014, DOI 10.1038/nature13883) absorbs 30 W/m². With fixed lumped sky exchange 128.4 W/m² at air temperature and assumed h_comb = 18.9 W/(m²·K), q_net(T_a) = 98.4 W/m² and ΔT ≈ −5.2 °C.

## Reference values stated in the essay
- **Tangent Stiffness λ_min(K_E + K_G)**: `+42.8 kN/m (Fixed Illustrative Text, No Solver)`
- **Structural Steel Aerial Mass**: `12.4 kg/m² for 120 m Span (Fixed Illustrative Text)`
- **Net Daytime Sky-Cooling Flux**: `98.4 W/m² at Air Temp · ΔT ≈ −5.2 °C (Fixed Text)`
- **A.12 Model Boundary**: `EXPLANATORY MODEL · NOT A DESIGN METHOD`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1126/science.aat9513 (Scite report: https://scite.ai/reports/10.1126/science.aat9513)
- What the essay compares against: Fixed illustrative values: t_0 = 185 kN · q_net(T_a) = 98.4 W/m² ⇒ ΔT ≈ −5.2 °C (assumed 128.4 W/m², 18.9 W/(m²·K))

## Recent research context
- **Explanatory Model: Pellegrino–Calladine Tensegrity Frameworks & Exterior 8–13 μm Sky-Cooling Coatings**: This folio explains Sergio Pellegrino and C. R. Calladine's equilibrium-matrix subspaces for prestressed frameworks (DOI 10.1016/0020-7683(86)90014-4) alongside a separate exterior roof-cooling arithmetic example citing Raman et al. (DOI 10.1038/nature13883) and Mandal et al. (DOI 10.1126/science.aat9513). Under stated assumptions (128.4 W/m² sky exchange at air temperature, h_comb = 18.9 W/(m²·K)), the example gives 98.4 W/m² and about −5.2 °C on the membrane surface. Explanatory model only, not a design method; nothing was built or simulated.
