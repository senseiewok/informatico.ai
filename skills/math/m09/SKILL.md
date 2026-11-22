---
name: wasserstein-optimal-transport-benamou-brenier
description: AI-agnostic optimal-transport skill for Monge-Kantorovich couplings, Brenier polar factorization, Benamou-Brenier Wasserstein-2 fluid geodesics, Bures-Wasserstein Gaussian displacement interpolation, and entropic Sinkhorn scaling.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Monge–Kantorovich Optimal Transport, Benamou–Brenier Wasserstein-2 Geodesic Fluid Dynamics, Sinkhorn Entropic Regularization & Flow Matching (Folio M.09)

A plain-text companion to the essay at https://informatico.ai/math/m09/ (`M.09 · Benamou–Brenier Wasserstein-2 Optimal Transport`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`W_2²(μ_0, μ_1) = inf ∫_0^1 ∫ ρ|v|² dx dt · ∂_t ρ + ∇·(ρ∇ψ) = 0 · ∂_t ψ + ½|∇ψ|² = 0`

## Rules the essay derives
1. Relate W_2^2(mu_0, mu_1) = inf int_0^1 int rho |v|^2 dx dt under d_t rho + nabla.(rho v) = 0 to kinetic saddle point (1/2) W_2^2 = inf int_0^1 int (1/2) rho |v|^2 dx dt, giving v = nabla psi and d_t psi + (1/2)|nabla psi|^2 = 0 (DOI 10.1007/s002110050002).
2. Check that mu_0 vanishes on Lebesgue-null sets before asserting T = nabla Phi (DOI 10.1002/cpa.3160440402), and interpolate both mean m_t = (1-t)m_0 + t m_1 and covariance along McCann paths (DOI 10.1006/aima.1997.1634; DOI 10.1016/j.exmath.2018.01.002).
3. Stabilize Sinkhorn scaling pi_ij = u_i exp(-c_ij / epsilon) v_j in the log domain for small epsilon > 0, note its O(epsilon) bias (arXiv:1306.0895), and state when readouts are fixed illustrative values.

## How it works, in four stages
- Stage 1 (Kantorovich Couplings): Relaxes Monge maps T_# μ_0 = μ_1 into a linear program over couplings π ∈ Π(μ_0, μ_1) when discrete mass splits (DOI 10.1561/2200000073).
- Stage 2 (Brenier Polar Factorization, DOI 10.1002/cpa.3160440402): When μ_0, μ_1 ∈ P_2(ℝ^d) and μ_0 vanishes on Lebesgue-null sets, T(x) = ∇Φ(x) = x + ∇ψ_0(x) for convex Φ.
- Stage 3 (Benamou–Brenier Geodesic, DOI 10.1007/s002110050002): Minimizing ½∬ ρ|v|² dx dt = ½W_2² under ∂_t ρ + ∇·(ρv) = 0 gives v = ∇ψ and ∂_t ψ + ½|∇ψ|² = 0 (DOI 10.1006/aima.1997.1634).
- Stage 4 (Sinkhorn Scaling, arXiv:1306.0895): Penalty ε KL(π || μ_0⊗μ_1) gives π_ij = u_i K_ij v_j with K_ij = exp(−||x_i − y_j||² / ε) and O(ε) bias (18 steps fixed illustrative).

## Reference values stated in the essay
- **Squared Wasserstein Distance (W_2², model)**: `4.82 (fixed illustrative Gaussian pair)`
- **Midpoint Mean & Spread (t = 0.50, model)**: `μ_0.5 = 0.00 · σ_0.5 = 1.15 (fixed illustrative)`
- **Sinkhorn Scaling Step Count (model)**: `18 steps at ε = 0.05 (fixed illustrative)`
- **Model Geometry**: `Benamou–Brenier geodesic (teaching model, not a solver)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1007/s002110050002 (Scite report: https://scite.ai/reports/10.1007/s002110050002)
- What the essay compares against: Illustrative 1D Gaussians: W_2² = 4.82 · t = 0.50 (σ = 1.15) · ε = 0.05 (18 steps)

## Recent research context
- **Benamou–Brenier Dynamic Optimal Transport, McCann Geodesics & Entropic Scaling**: Links Brenier’s polar factorization (DOI 10.1002/cpa.3160440402) and McCann’s displacement interpolation (DOI 10.1006/aima.1997.1634) with Benamou & Brenier’s fluid formulation (DOI 10.1007/s002110050002), Otto’s calculus (DOI 10.1081/PDE-100002243), and Sinkhorn scaling (arXiv:1306.0895; DOI 10.1561/2200000073). Values shown are illustrative.
