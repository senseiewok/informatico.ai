---
name: bridge-flutter-pinn-twin
description: AI-agnostic structural and wind civil engineering skill for Scanlan bridge aeroelastic flutter derivatives, critical wind speed U_crit, and Physics-Informed Neural Network (PINN) virtual stress sensing.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Long-Span Suspension Bridge Aeroelastic Flutter, Scanlan Derivatives & Physics-Informed Neural Network (PINN) Digital Twins (Folio E.07)

A plain-text companion to the essay at https://informatico.ai/engineering/e07/ (`E.07 · Bridge Aeroelastic Flutter & PINN SHM · CSI 05 12 00`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`ζ_net = ζ_s − (ρ B⁴ / 2 I_α) A_2*(K) · L_total = L_data + λ_pde ‖R_pde‖² · CSI 05 12 00`

## Rules the essay derives
1. Compute dimensionless reduced velocity U_red = U / (f_alpha * B) and reduced frequency K = B * omega / U = 2 * pi / U_red.
2. Evaluate net torsional aeroelastic damping zeta_net = zeta_struct - (rho * B^4 / (2 * I_alpha)) * A_2*(K); instability (flutter) occurs when zeta_net <= 0.
3. Balance PINN composite loss L_total = L_data + lambda_pde * ||E*I*u_xxxx + m*u_tt - f_aero||^2 so sparse sensor noise does not violate Euler-Bernoulli equilibrium.

## How it works, in four stages
- Stage 1 (Coupled Heave-Torsion Modal Kinematics): A model 2,100 m suspension span with deck width B = 36 m oscillates in vertical bending h(x,t) (f_h = 0.095 Hz) and torsion α(x,t) (f_α = 0.235 Hz). These are illustrative values, not a surveyed bridge.
- Stage 2 (Scanlan Aeroelastic Flutter Derivatives): Motion-induced pitching moment M_ae scales with A_2*(K) at reduced velocity U / (f_α B); in the folio model the vented twin-box girder keeps A_2*(K) < 0 up to U_crit = 76.4 m/s, a fixed illustrative value.
- Stage 3 (Physics-Informed Neural Network Virtual Sensing): Embedding the coupled Euler–Bernoulli + Saint-Venant PDE residual R_pde into L_total is the proposed way to reconstruct full-span bending stress from 8 accelerometers. No network was trained for this folio.
- Stage 4 (Orthotropic Steel Deck Fatigue Check, a Proposal): Stress histories from such a digital twin could be compared with the fatigue provisions of a design code such as the AASHTO LRFD Bridge Design Specifications at rib-to-deck welds. The folio performs no code check.

## Reference values stated in the essay
- **Reduced Wind Velocity U/(f_α B)**: `6.15 (U = 52.0 m/s, B = 36 m)`
- **Net Torsional Damping (ζ_net)**: `+2.84% (illustrative; U_crit = 76.4 m/s)`
- **PINN Virtual Stress Error**: `1.42% (illustrative; λ_pde = 1.00)`
- **Bridge Aeroelastic Verdict**: `STABLE IN MODEL (ζ_net > 0)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/j.jcp.2018.10.045 (Scite report: https://scite.ai/reports/10.1016/j.jcp.2018.10.045)
- What the essay compares against: Illustrative model values: U_crit = 76.4 m/s · PINN stress error 1.42% (8 sensors; no network trained)

## Recent research context
- **Could Physics-Informed Neural Networks Turn Sparse Bridge Accelerometers Into Full-Span Stress Estimates?**: This folio pairs Robert Scanlan's aeroelastic flutter derivatives (Scanlan & Tomko 1971, DOI 10.1061/JMCEA3.0001526) with the Physics-Informed Neural Networks of Raissi, Perdikaris & Karniadakis (J. Comput. Phys., DOI 10.1016/j.jcp.2018.10.045). It proposes that a bridge digital twin could embed Euler–Bernoulli and torsional PDEs in its loss function to estimate stress and flutter margin along a 2,000 m span from about 8 accelerometer stations. It is a design study: nothing was trained or deployed.
