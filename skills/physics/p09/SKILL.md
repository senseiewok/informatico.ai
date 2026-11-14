---
name: taylor-cone-ehd-rayleigh-aerosol
description: AI-agnostic fluid and electrohydrodynamic physics skill for Sir Geoffrey Taylor's 49.3-degree cone (P_{1/2}(cos theta_0) = 0), Lord Rayleigh's droplet fission limit, and Ganan-Calvo monodisperse aerosol scaling.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Electrohydrodynamic Taylor Cones (49.3°), Rayleigh Fission Limits & Precision Monodisperse Aerosol Jet Physics (Folio P.09)

A plain-text companion to the essay at https://informatico.ai/physics/p09/ (`P.09 · Taylor Cone EHD & Rayleigh Aerosol Physics`, `REV 1.0`, redated `2026-11-03`).

## The governing relation
`P_{1/2}(cos θ_0) = 0 ⇒ θ_T = 49.3° · q_R = 8π √(ε_0 γ R³) · d_drop ~ (ρ ε_0 Q³ / γ K)^(1/6)`

## Rules the essay derives
1. Verify Taylor cone onset voltage V_onset ~ sqrt(gamma * d_nozzle / epsilon_0) and equilibrium half-angle alpha_T = 49.29 deg from P_{1/2}(cos(pi - alpha_T)) = 0.
2. Compute Ganan-Calvo cone-jet droplet diameter d_drop ~ (rho * epsilon_0 * Q^3 / (gamma * K_cond))^(1/6) and verify 1.5 um <= MMAD <= 3.5 um for tracheobronchial targeting.
3. Enforce Rayleigh fissility stability q < q_R = 8 * pi * sqrt(epsilon_0 * gamma * R^3) and Weber shear stability We_shear < We_crit to prevent LNP rupture.

## How it works, in four stages
- Stage 1 (Taylor Equipotential Cone Equilibrium, DOI 10.1098/rspa.1964.0151): Balancing Maxwell electrostatic stress ½ ε_0 E_n² against Laplace pressure γ cot α / r fixes P_{1/2}(cos 130.7°) = 0 and θ_T = 49.3°.
- Stage 2 (Gañán-Calvo Apex Cone-Jet Necking): Charge relaxation τ_e = ε / K accelerates a sub-micrometer liquid microjet from the cone tip without high-shear wall cavitation.
- Stage 3 (Monodisperse Capillary Breakup in the 1.5–3.5 μm Window): At Q = 1.20 μL/min and K = 0.45 S/m, jet varicose breakup yields d_drop = 2.42 μm (GSD = 1.18) for deep bronchial deposition.
- Stage 4 (Rayleigh Fission Guard & Intact 4.5 kb mRNA Survival, Continuing P.06): Holds droplet charge ratio q / q_R = 0.68 < 1.00, preserving 97.4% LNP lipid-bilayer encapsulation.

## Reference values stated in the essay
- **Taylor Half-Angle (θ_T)**: `49.29° (P_{1/2} Zero)`
- **Monodisperse Droplet (d_drop)**: `2.42 μm (Bronchial Window)`
- **Rayleigh Charge Ratio (q/q_R)**: `0.68 (< 1.00 Stable)`
- **Aerosol & LNP Verdict**: `97.4% INTACT mRNA · PASS`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1098/rspa.1964.0151 (Scite report: https://scite.ai/reports/10.1098/rspa.1964.0151)
- What the essay compares against: Q = 1.20 μL/min · K = 0.45 S/m ⇒ d_drop = 2.42 μm · q/q_R = 0.68

## Recent research context
- **Sir Geoffrey Taylor's 49.3° Electrohydrodynamic Cone & Rayleigh Fission Limits Protect Inhaled mRNA Nanoparticles**: Completing the biophysical delivery sequence of Folios P.03, P.04, and P.06, Sir Geoffrey Ingram Taylor's P_{1/2}(cos θ_0) = 0 equilibrium cone (Proc. R. Soc. A DOI 10.1098/rspa.1964.0151) and Gañán-Calvo's cone-jet scaling generate monodisperse 2.4 μm bronchial droplets without shearing fragile 4.5 kb CFTR mRNA lipid nanoparticles.
