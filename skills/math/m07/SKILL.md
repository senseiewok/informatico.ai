---
name: f1-pontryagin-fno-control
description: AI-agnostic applied mathematics and operator-learning skill for Formula 1 350 kW MGU-K Pontryagin optimal energy management, HJB lap-time minimization, and Fourier Neural Operator PDE surrogates.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Formula 1 350 kW MGU-K Pontryagin Optimal Energy Control, Hamilton–Jacobi–Bellman Lap Time Minimization & Fourier Neural Operator Surrogates (Folio M.07)

A plain-text companion to the essay at https://informatico.ai/math/m07/ (`M.07 · F1 Pontryagin Control & FNO Surrogates · FIA 2026 Art. 5`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`H(x, u, λ) = 1/v + λ_v f_v(v, P_k, δ) − λ_E P_batt(P_k)/v ; u_{l+1} = σ(W u_l + F⁻¹(R_φ · F(u_l)))`

## Rules the essay derives
1. Formulate the minimum-Hamiltonian H = (1/v) + lambda_v * a_net(v, P_k, delta_wing) / v - lambda_E * P_batt(P_k) / v along arc-length s, with P_batt = P_k / eta_k for motoring (P_k >= 0) and eta_regen * P_k under braking.
2. Evaluate the motoring optimality condition dH/dP_k = lambda_v / (m * v^2) - lambda_E * (dP_batt/dP_k) / v = 0 (lambda_v, lambda_E < 0 under min_u H): affine losses (dP_batt/dP_k = 1/eta_k) switch at lambda_v / (m * v) = lambda_E / eta_k, whereas strictly convex losses P_batt(P_k) initiate smooth tapering below P_k,max where lambda_v / (m * v) = lambda_E * dP_batt/dP_k(P_k,max).
3. Evaluate spectral neural operator layer u_{l+1}(x) = sigma(W * u_l(x) + F^{-1}(R_phi * F(u_l))(x)) truncated at k_max Fourier modes.

## How it works, in four stages
- Stage 1 (Fourier Neural Operator Surrogate, proposed): An FNO layer u_{l+1} = σ(W u_l + F⁻¹(R_φ · F(u_l))) could map wing angle δ_wing and ride height h_ride to aerodynamic coefficients; no surrogate was trained here.
- Stage 2 (Distance-Domain Pontryagin Hamiltonian H): Rewrites minimum-time control in track distance ds/dt = v; on interior battery arcs, co-state λ_E* is constant across an assumed 4.0 MJ budget.
- Stage 3 (Convex-Loss Taper vs. Clipping): Above a switching speed, convex electrical losses taper P_k*(s) instead of clipping mid-straight (298.4 km/h and 0.42 s are illustrative).
- Stage 4 (Regenerative Braking Harvest): Under braking (P_k < 0), piecewise efficiency η_regen recovers kinetic energy so E_batt(L) = E_batt(0) closes the lap.

## Reference values stated in the essay
- **Straight-Line Lap Gain (Δt_lap, model)**: `−0.42 s vs. naive clipping (illustrative)`
- **Optimal Taper Velocity (v_switch, model)**: `298.4 km/h (illustrative)`
- **FNO Operator Error (k_max = 32, model)**: `0.82% (illustrative; no surrogate trained here)`
- **Pontryagin Model Outcome**: `Taper avoids clipping in the model (not a race result)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1080/00207179.2014.900705 (Scite report: https://scite.ai/reports/10.1080/00207179.2014.900705)
- What the essay compares against: Model values: P_k,max = 350 kW · ΔE_lap = 4.0 MJ (assumed budget) · FNO error 0.82% (illustrative, not measured)

## Recent research context
- **A Design Study: Pontryagin Energy Control for a 350 kW Hybrid Race Car, With Neural Operator Surrogates**: This folio pairs Limebeer, Perantoni & Rao's optimal control of Formula One energy recovery (Int. J. Control DOI 10.1080/00207179.2014.900705) with Li et al.'s Fourier Neural Operator (arXiv:2010.08895) as a proposal for faster co-state switching under the reported 2026 350 kW limit. Its lap-time and error figures are illustrative.
