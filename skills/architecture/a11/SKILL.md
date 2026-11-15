---
name: 3d-polyhedral-graphic-statics
description: AI-agnostic architectural and structural skill for 3D Polyhedral Graphic Statics (Maxwell-Rankine dual polyhedra), strictly concave Airy stress surfaces, 8-13 um daytime radiative sky-cooling vault envelopes, and Toolbox X.03 STEP AP242 voussoir coupling.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# 3D Polyhedral Graphic Statics & Airy Stress Surfaces: Maxwell–Rankine Reciprocal Polyhedra, Guastavino Tile Vaulting & Zero-Rebar Floors (Folio A.11)

A plain-text companion to the essay at https://informatico.ai/architecture/a11/ (`A.11 · 3D Polyhedral Graphic Statics & Passive Sky-Cooling Vaults · REV 1.5`, `REV 1.5`, redated `2026-11-14`).

## The governing relation
`σ_xx = Φ_yy · σ_yy = Φ_xx · det(H_Φ) > 0 · N_i ∝ A_i^* · q_net(8–13 μm) (folio design target ≥ 80 W/m²)`

## Rules the essay derives
1. Check 3D nodal equilibrium by requiring every polyhedral cell c_v^* in the reciprocal force diagram Gamma^* to close within a numerical tolerance (for example ||sum F_i|| < 1e-12 kN).
2. Check that the model stress field is compressive by testing the Airy stress Hessian: Phi_xx < 0, Phi_yy < 0, and det(H_Phi) = Phi_xx*Phi_yy - Phi_xy^2 > 0. This is a model check for one load case, not a structural assessment of a real vault.
3. Evaluate daytime radiative sky-cooling net flux q_net = q_rad(T_s) - q_atm(T_a) - q_solar*(1 - R_solar) - h_c*(T_a - T_s); treat q_net >= 80 W/m^2 at T_a = 303.15 K and Delta T_eq <= -4.5 C as this folio's own design targets, and report results as model values, never as measurements.

## How it works, in four stages
- Stage 1 (Airy Stress Function & Negative-Definite Hessian): In-plane membrane stresses are written through an Airy stress function Φ(x, y) as σ_xx = Φ_yy, σ_yy = Φ_xx, σ_xy = −Φ_xy. In his 1870 paper on reciprocal figures Maxwell read a polyhedron lifted over a frame as a discrete stress function of this kind.
- Stage 2 (Rankine–Minkowski Reciprocal Polyhedra Γ ↔ Γ^*): In 3D polyhedral graphic statics (Akbarzadeh, Van Mele & Block 2015, DOI 10.1016/j.cad.2015.01.006), each member of the form diagram is perpendicular to a face of a closed cell in the force diagram, and the face area is proportional to the member force; a closed cell means the forces at that node balance.
- Stage 3 (Concavity and Compression): If the Hessian of Φ is negative-definite (Φ_xx < 0, Φ_yy < 0, det(H_Φ) = Φ_xx Φ_yy − Φ_xy² > 0), the in-plane stress field of the model is compressive everywhere. That is a property of the model under the load case considered, not a structural check of a real shell; the 52 mm thickness is an illustrative value.
- Stage 4 (8–13 μm Radiative Sky-Cooling Extrados & Toolbox X.03 CAD Bridge): With a porous P(VdF-HFP)-type coating (Mandal et al. 2018, DOI 10.1126/science.aat9513) assumed at R_solar = 0.96 under 890 W/m² of sun, the extrados absorbs 35.6 W/m². The model assigns a net radiative exchange with the sky of 134.0 W/m² at air temperature (a fixed illustrative value), so q_net = 134.0 − 35.6 = 98.4 W/m²; divided by an assumed combined heat-exchange coefficient of 13.9 W/(m²·K), that gives ΔT_eq ≈ −7.08 °C. Toolbox X.03 provides the STEP AP242 voussoir geometry.

## Reference values stated in the essay
- **Airy Hessian Determinant det(H_Φ)**: `+1.84 > 0 (Illustrative, Compressive in Model)`
- **Dual Polyhedron Closure Error**: `Closed by Construction (Model, No Solver Run)`
- **8–13 μm Sky-Cooling Net Flux**: `98.4 W/m² · ΔT_eq = −7.08 °C (Model)`
- **A.11 ↔ X.03 Model Status**: `COMPRESSION-ONLY IN MODEL · NOT A STRUCTURAL CHECK`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/j.cad.2015.01.006 (Scite report: https://scite.ai/reports/10.1016/j.cad.2015.01.006)
- What the essay compares against: Model values: det(H_Φ) = +1.84 (illustrative) · q_net = 98.4 W/m² at air temperature · ΔT_eq = −7.08 °C for an assumed 13.9 W/(m²·K)

## Recent research context
- **A Design Study: 3D Polyhedral Graphic Statics & 8–13 μm Sky-Cooling Coatings on Compression-Only Vaults**: This folio pairs compression-only vault geometry from 3D graphic statics (Akbarzadeh et al., DOI 10.1016/j.cad.2015.01.006) and Toolbox X.03 STEP AP242 voussoir kits with a porous P(VdF-HFP) sky-cooling coating on the extrados (DOI 10.1038/nature13883, DOI 10.1126/science.aat9513). In its model the coating gives 98.4 W/m^2 of cooling at air temperature and a surface about 7.08 C below the air for an assumed heat-exchange coefficient. Model values, not measurements; one published unreinforced funicular floor uses about a third of the material of a flat slab (Küpfer et al. 2025).
