---
name: f1-ground-effect-active-aero
description: AI-agnostic fluid-dynamics and motorsport physics skill for Formula 1 ground-effect Venturi aerodynamics, Lamb-Oseen vortex sealing, 2026 Active Aero X/Z-modes, and porpoising Hopf bifurcation stability.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Formula 1 Ground-Effect Venturi Aerodynamics, 2026 Active X/Z-Mode Wings, Outwash Vortex Sealing & Porpoising Limit Cycles (Folio P.07)

A plain-text companion to the essay at https://informatico.ai/physics/p07/ (`P.07 · Formula 1 Ground-Effect & 2026 Active Aero · FIA Art. 3`, `REV 1.0`, redated `2026-11-02`).

## The governing relation
`C_p = 1 − (U/U_∞)² · Γ_v = ∮ u·dl · m z̈ + c_a(z) ż + k_s z = −½ρU²A C_L(z, δ_wing)`

## Rules the essay derives
1. Compute underfloor pressure coefficient C_p = 1 - (U_local / U_inf)^2 and Lamb-Oseen azimuthal vortex velocity u_theta(r) = (Gamma_v / (2*pi*r)) * (1 - exp(-r^2 / r_c^2)).
2. Model ground-effect downforce -C_L(h_ride, delta_wing) with peak suction at h_opt ~ 22-26 mm and sharp Stratford boundary-layer stall for h_ride < h_crit = 19 mm.
3. Evaluate aero-elastic heave stability from m * z_ddot + c_a(z) * z_dot + k_s * z = -0.5 * rho * U^2 * A * C_L(z, delta_wing); porpoising limit cycles occur when c_a(z) < 0.

## How it works, in four stages
- Stage 1 (Front-Wing Outwash & Tire Squirt Control): Counter-rotating wingtip and floor-strake vortices deflect turbulent front-tire wake outboard, feeding clean total pressure into the floor.
- Stage 2 (Underfloor Venturi Throat Acceleration, h_ride = 26 mm): Flow accelerates to 1.96 U_∞ at the minimum throat, generating peak suction −C_p = 2.84 and downforce −C_L = 3.38.
- Stage 3 (2026 Active Aero Z-Mode vs. X-Mode Transition): Flattening front and rear flaps to δ_wing = 6° on straights (X-Mode) sheds 38% aerodynamic drag and prevents floor bottoming.
- Stage 4 (Stratford Separation & Porpoising Hopf Bifurcation, h_ride < 19 mm): Choking the throat below 19 mm bursts the Lamb–Oseen sealing vortex, triggering 5.8 Hz aero-elastic porpoising.

## Reference values stated in the essay
- **Underfloor Suction Peak (−C_p)**: `2.84 (at h_ride = 26 mm)`
- **Total Downforce Coefficient (−C_L)**: `3.38 (L/D = 3.92 Z-Mode)`
- **Edge Vortex Circulation (Γ_v)**: `4.65 m²/s (Vortex Sealed)`
- **Aero-Elastic Stability Verdict**: `ATTACHED · ZERO PORPOISING`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1146/annurev.fluid.38.050304.092016 (Scite report: https://scite.ai/reports/10.1146/annurev.fluid.38.050304.092016)
- What the essay compares against: −C_p,peak = 2.84 · −C_L = 3.38 (Z-Mode) · −40% Drag (X-Mode)

## Recent research context
- **2026 FIA Active X/Z-Mode Wings & Lamb–Oseen Vortex Sealing Tame Ground-Effect Porpoising**: Grounded in Joseph Katz's fluid mechanics of race-car aerodynamics (Annu. Rev. Fluid Mech. 2006, DOI 10.1146/annurev.fluid.38.050304.092016), the 2026 Formula 1 regulations pair underfloor Venturi diffusers with full-time Active Aerodynamics—switching between high-downforce Z-Mode in corners and low-drag X-Mode on straights to suppress Hopf bifurcation porpoising.
