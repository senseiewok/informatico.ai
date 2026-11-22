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
1. Compute U_red = U / (f_alpha * B) and K = B * omega / U = 2 * pi / U_red.
2. Under Scanlan 1971 2B^2 moment scaling (per-span I_alpha in kg*m^2/m), evaluate zeta_net = zeta_s - (rho * B^4 / (2 * I_alpha)) * A_2*^(1971)(K) = zeta_s - (rho * B^4 / (4 * I_alpha)) * A_2*^(1996)(K) with A_2*^(1996) = 2 * A_2*^(1971); flutter starts at zeta_net <= 0.
3. Weight non-dimensionalized bending (E I ∂⁴h/∂x⁴ − H_w ∂²h/∂x² + m ∂²h/∂t² − L_aero) and torsion (I_α ∂²α/∂t² − G J ∂²α/∂x² − M_ae) residuals in L_total = L_data + λ_pde ‖R_pde‖²; unmeasured wind makes sparse inversion ill-posed.
4. State that these are explanatory single-mode relations with illustrative constants: not a design or assessment method, and no value here applies to a real bridge.

## How it works, in four stages
- Stage 1 (Modal Kinematics): Model 2,100 m span (B = 36 m) with heave h(x,t) (f_h = 0.095 Hz) and torsion α(x,t) (f_α = 0.235 Hz); illustrative values, not a surveyed bridge.
- Stage 2 (Scanlan Derivatives): Under 1971 2B² moment scaling with per-span I_α, A_2*(K) < 0 keeps the vented twin-box model stable up to an illustrative U_crit = 76.4 m/s.
- Stage 3 (Proposed PINN Residual): Penalizing non-dimensionalized beam and Saint-Venant PDE residuals R_pde could aid 8-sensor stress estimation; untested, no network trained.
- Stage 4 (Proposed Weld Fatigue Check): Estimated rib-to-deck weld stress ranges could be compared against AASHTO LRFD fatigue provisions; no code check is run.

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
- **Could Physics-Informed Neural Networks Turn Sparse Bridge Accelerometers Into Full-Span Stress Estimates?**: Pairs Scanlan's flutter derivatives (DOI 10.1061/JMCEA3.0001526; Jain et al. 1996, DOI 10.1061/(ASCE)0733-9445(1996)122:7(716)) and twin-box slot mechanics (Yang et al. 2015, DOI 10.1061/(ASCE)BE.1943-5592.0000645) with PINNs (Raissi et al. 2019, DOI 10.1016/j.jcp.2018.10.045; Al-Adly & Kripakaran 2024, DOI 10.1017/dce.2024.4) for sparse bridge sensing; untested proposal.
