---
name: 3d-polyhedral-graphic-statics
description: Explanatory companion for 3D Polyhedral Graphic Statics, 2D Airy concavity, and exterior 8–13 μm sky-cooling arithmetic. Explanation only, not a design method; no folio number may be used on a real structure.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# 3D Polyhedral Graphic Statics & Airy Stress Surfaces: Maxwell–Rankine Reciprocal Polyhedra, Guastavino Tile Vaulting & Zero-Rebar Floors (Folio A.11)

A plain-text companion to the essay at https://informatico.ai/architecture/a11/ (`A.11 · 3D Polyhedral Graphic Statics & Sky-Cooling Vaults · REV 1.6`, `REV 1.6`, redated `2026-11-21`).

## The governing relation
`σ_xx = Φ_yy · σ_yy = Φ_xx · Φ_xx, Φ_yy < 0, det(H_Φ) > 0 (2D Airy) · N_i ∝ A_i^* (3D) · q_net(T_a)`

## Rules the essay derives
1. Explanation only, not a structural design method: no thickness, stress, or cooling number from this folio may be used on a real structure.
2. In 3D reciprocal force diagrams Gamma^*, verify each polyhedral cell closes (e.g. ||sum F_i|| < 1e-12 kN) with axial force proportional to face area (N_i proportional to A_i^*).
3. In a 2D Airy model (tension-positive), check Phi_xx < 0, Phi_yy < 0, and det(H_Phi) > 0 for one load case; this does not check buckling, sliding, support movement, or asymmetric loads.
4. For an exposed roof only, distinguish cooling power at air temperature q_net(T_a) = q_sky_net(T_a) - q_solar*(1 - R_solar) from steady-state q_net(T_s) = 0, and estimate Delta T_eq = -q_net(T_a) / h_comb under stated assumptions. Treat 80 W/m^2 and -4.5 C as untested illustrative benchmarks.

## How it works, in four stages
- Stage 1 (2D Airy Stress Surface): In 2D membrane models (tension-positive), σ_xx = Φ_yy, σ_yy = Φ_xx, σ_xy = −Φ_xy. Maxwell (1864, DOI 10.1080/14786446408643663; 1870) linked plane frames to polyhedra and stress functions; Thrust Network Analysis (Block & Ochsendorf 2007) projects 3D vault forces onto a 2D Airy surface.
- Stage 2 (3D Reciprocal Polyhedra Γ ↔ Γ^*): Separately, 3D polyhedral graphic statics (Akbarzadeh, Van Mele & Block 2015, DOI 10.1016/j.cad.2015.01.006) maps each bar perpendicular to a closed force-cell face, with axial force proportional to face area (N_i ∝ A_i^*); cell closure means nodal forces balance.
- Stage 3 (Concavity & Safety Boundary): Negative-definite Hessian (Φ_xx < 0, Φ_yy < 0, det(H_Φ) > 0) means the 2D model is compressive under one load case. This folio is an explanation, not a design method; none of its untested numbers (including t = 52 mm or det(H_Φ) = +1.84) may be used on a real structure.
- Stage 4 (Separate Exterior Sky-Cooling Pairing): For an exposed roof only (not a floor), assuming a P(VdF-HFP) coating (Mandal et al. 2018, DOI 10.1126/science.aat9513) with R_solar = 0.96 under 890 W/m² absorbs 35.6 W/m². With a lumped illustrative sky exchange of 134.0 W/m² at T_a = 303.15 K and assumed h_comb = 13.9 W/(m²·K), q_net(T_a) = 98.4 W/m² and ΔT_eq ≈ −7.08 °C. Toolbox X.03 (/toolchain/x03/) has a separate 7-voussoir arch STEP AP242 kit.

## Reference values stated in the essay
- **Airy Hessian Determinant det(H_Φ)**: `+1.84 > 0 (Fixed Text, Φ_xx, Φ_yy < 0)`
- **Dual Polyhedron Closure Error**: `Closed by Construction (Fixed Text, No Solver)`
- **8–13 μm Sky-Cooling Net Flux**: `98.4 W/m² at T_a · ΔT_eq ≈ −7.08 °C (Fixed Text)`
- **A.11 Model Boundary**: `EXPLANATORY MODEL · NOT A DESIGN METHOD`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/j.cad.2015.01.006 (Scite report: https://scite.ai/reports/10.1016/j.cad.2015.01.006)
- What the essay compares against: Fixed values: det(H_Φ) = +1.84 · q_net(T_a) = 98.4 W/m² · ΔT_eq ≈ −7.08 °C (assumed 134.0 W/m², 13.9 W/(m²·K))

## Recent research context
- **Explanatory Model: 3D Polyhedral Graphic Statics & Exterior 8–13 μm Sky-Cooling Coatings**: This folio explains 3D reciprocal force polyhedra (Akbarzadeh et al. 2015, DOI 10.1016/j.cad.2015.01.006) alongside a separate roof-only radiative cooling calculation citing Raman et al. (2014, DOI 10.1038/nature13883) and porous P(VdF-HFP) coatings from Mandal et al. (2018, DOI 10.1126/science.aat9513). Under stated assumptions (134.0 W/m² sky exchange at air temperature, h_comb = 13.9 W/(m²·K)), the model estimates 98.4 W/m² and about −7.08 °C. Separately, Küpfer et al. (2025) report an unreinforced funicular floor using about one-third the material of a flat slab. Explanatory model only, not a design method.
