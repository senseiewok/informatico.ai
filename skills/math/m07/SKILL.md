---
name: f1-pontryagin-fno-control
description: AI-agnostic applied-mathematics teaching skill for hybrid Pontryagin energy pacing, Hamilton-Jacobi-Bellman formulations, and proposed Fourier Neural Operator PDE surrogates (not a vehicle or controller design method).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Formula 1 350 kW MGU-K Pontryagin Optimal Energy Control, Hamilton–Jacobi–Bellman Lap Time Minimization & Fourier Neural Operator Surrogates (Folio M.07)

A plain-text companion to the essay at https://informatico.ai/math/m07/ (`M.07 · Hybrid Pontryagin Control & FNO Surrogates (Teaching Model)`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`H(x, u, λ) = 1/v + λ_v a_net(v, P_k, δ)/v − λ_E P_batt(P_k)/v ; u_{l+1} = σ(W u_l + F⁻¹(R_φ · F(u_l)))`

## Rules the essay derives
1. Treat this skill strictly as an educational explanation, not as a vehicle, battery, or powertrain controller design method; none of its assumed or untested illustrative figures (-0.42 s, 298.4 km/h, 4.0 MJ, 0.82%, not verified) may be applied to real hardware, under the stated assumptions of H = (1/v) + lambda_v * a_net / v - lambda_E * P_batt(P_k) / v with interior d(lambda_E)/ds = 0 (lambda_E* < 0).
2. Separate motoring arcs (lambda_v < 0, F_brake = 0, P_k >= 0), the subgradient coasting deadband (P_k* = 0 when lambda_E* / eta_k <= lambda_v / (m * v) <= lambda_E* * eta_regen), lift-and-coast regen (lambda_E* * eta_regen < lambda_v / (m * v) < 0, F_brake = 0, P_k < 0), and corner friction braking (lambda_v > 0, F_brake > 0, P_k < 0, P_batt = eta_regen * P_k): under the stated assumptions, quadratic draw P_k / eta_k + alpha * P_k^2 (alpha > 0) could taper P_k*(s) = (lambda_v / (lambda_E* * m * v) - 1/eta_k) / (2α) on (v_switch, v_zero) with v_switch = lambda_v / (lambda_E* * m * (1/eta_k + 2α P_{k,max})) and v_zero = lambda_v * eta_k / (lambda_E* * m).
3. Write the Fourier Neural Operator layer u_{l+1}(x) = sigma(W * u_l(x) + F^{-1}(R_phi * F(u_l))(x)) truncated at k_max modes (Li et al. 2020, arXiv:2010.08895), noting the caveat that race-car aerodynamic simulation coupling is not yet tested and remains untested here.

## How it works, in four stages
- Stage 1 (Proposed FNO Surrogate): Layer u_{l+1} = σ(W u_l + F⁻¹(R_φ · F(u_l))) could map wing angle and ride height to flow fields (Li et al. 2020); untrained here.
- Stage 2 (Distance-Domain Hamiltonian H): Rewrites minimum-time control in ds/dt = v; on interior battery arcs, constant λ_E* < 0 allocates an assumed 4.0 MJ budget.
- Stage 3 (Convex-Loss Motoring Taper): For P_k ≥ 0, assumed draw P_batt(P_k) = P_k/η_k + α P_k² (α > 0) tapers P_k*(s) on (v_switch, v_zero) (298.4 km/h and −0.42 s are fixed illustrative figures).
- Stage 4 (Corner Braking & Harvest): On braking arcs (F_brake > 0, λ_v > 0, P_k < 0), P_batt = η_regen P_k recovers kinetic energy toward E_batt(L) = E_batt(0).

## Reference values stated in the essay
- **Straight-Line Lap Gain (Δt_lap, model)**: `−0.42 s vs. naive clipping (fixed illustrative)`
- **Optimal Taper Velocity (v_switch, model)**: `298.4 km/h (fixed illustrative)`
- **FNO Operator Error (k_max = 32, model)**: `0.82% (fixed illustrative; no surrogate trained)`
- **Pontryagin Model Outcome**: `Taper avoids clipping in the model (not a vehicle design)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1080/00207179.2014.900705 (Scite report: https://scite.ai/reports/10.1080/00207179.2014.900705)
- What the essay compares against: Illustrative constants: P_k,max = 350 kW · ΔE_lap = 4.0 MJ (assumed) · FNO error 0.82% (untrained)

## Recent research context
- **Pontryagin Energy Control & Proposed Neural Surrogates for a 350 kW Hybrid Teaching Model**: Pairs Limebeer, Perantoni & Rao's optimal control of Formula One energy recovery (DOI 10.1080/00207179.2014.900705) with Li et al.'s Fourier Neural Operator (arXiv:2010.08895) as a teaching explanation under the reported 2026 350 kW ceiling—not a vehicle design method, with illustrative figures.
