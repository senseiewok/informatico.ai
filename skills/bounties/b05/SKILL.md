---
name: bounty-b05-pysr-pysindy-pde-discovery
description: Governing law, 4-stage proof spine, and T0-T3 truth boundary for B.05 (BOUNTY-P2): Pareto Symbolic Regression (PySR) & Sparse PDE Discovery (PySINDy + Dedalus) from Noisy Sensor Fields. The proof harness is bounties/bounty_p2_pysr_pysindy_pde_discovery.py.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Pareto Symbolic Regression (PySR) & Sparse PDE Discovery (PySINDy + Dedalus) from Noisy Sensor Fields (B.05 · BOUNTY-P2)

## 1. Governing Law, Prize Registry & Canonical URL
- **Bounty Folio**: `B.05` (`BOUNTY-P2` · `REV 1.3`, Redated `2026-11-15`)
- **Canonical URL**: https://informatico.ai/bounties/b05/ (Spanish: https://informatico.ai/es-mx/bounties/b05/)
- **Prize / Challenge**: GRAND CHALLENGE B.05 (P-2) · PYSR + PYSINDY + DEDALUS
- **Official Registry**: [MilesCranmer/PySR (Symbolic Regression)](https://github.com/MilesCranmer/PySR)
- **Governing Equation**: `u_t = −1.00 u·u_x + 0.10 u_xx (∀ |ξ_k| < λ = 0.05 ⇒ ξ_k = 0) · L_MDL = (N/2) ln(MSE) + λ_MDL C_tree = −1073.45 nats (model value at σ = 0.02)`
- **Proof harness (computes the reference results; no planted-defect mode yet)**: `python bounties/bounty_p2_pysr_pysindy_pde_discovery.py`
- **Primary Scite Anchor DOI**: https://doi.org/10.1073/pnas.1517384113 (Scite Report: https://scite.ai/reports/10.1073/pnas.1517384113)

## 2. Falsification Rules
1. Target Support Recovery Invariant: STLSQ must recover the two-term support ['u*u_x', 'u_xx'] with zero false-positive operators and zero false-negative physical terms.
2. Viscosity Survival Bound (Underfit Prevention): Sparsity cutoff λ must satisfy λ ≤ |ν - 0.02 σ| = 0.0996 at σ = 0.02; setting λ ≥ 0.10 prunes the viscous dissipation term ν u_xx and leaves an inviscid shock truncation.
3. Noise Rejection Bound (Overfit Prevention): Threshold λ must exceed max_{k ∉ S} |σ · d_k| = 0.25 σ; when 0.25 σ ≥ λ (σ ≥ 4λ), spurious terms (starting with u³) leak into the discovered PDE.

## 3. 4-Stage Formal Proof & Benchmark Mechanism
- Stage 1: Reference Viscous Burgers Setup — Specify the reference viscous Burgers PDE u_t + u u_x = ν u_xx (ν = 0.10) on N = 200 sample points (external Dedalus Chebyshev–Fourier spectral rollouts apply to full fields; the offline harness models the 6-term operator weights directly).
- Stage 2: Noisy Operator Library Assembly — Construct Θ(u) = [1, u, u_x, u·u_x, u_xx, u³] with synthetic sensor-drift amplitude σ = 0.02.
- Stage 3: STLSQ Hard-Thresholding — Zero out all terms with |ξ_k| < λ = 0.05, pruning spurious weights [0.0036, -0.0044, 0.0030, 0.0050] to zero while retaining [-0.9992, 0.0996].
- Stage 4: Pareto MDL Selection — Evaluate L_MDL = (N/2) ln(MSE) + 0.45 C_tree across complexity levels C_tree ∈ {3, 6, 11}, selecting the knee at C_tree = 6 (L_MDL = -1073.4509 nats at σ = 0.02).

## 4. Reference Results Computed by the Harness (T0/T1)
- **Recovered PDE Support**: `['u*u_x', 'u_xx'] (2 / 6 active)`
- **PySR Selected Governing Law**: `u_t = −u·u_x + 0.10 u_xx`
- **Pareto MDL Score L_MDL**: `−1073.45 nats (C_tree = 6)`
- **Symbolic Discovery Gate**: `PASS · TARGET PDE SUPPORT`

## 5. Exact T0–T3 Truth Boundary
### Verified in Repository Today (T0/T1)
- Self-contained synthetic STLSQ operator pruning and Pareto MDL harness in bounties/bounty_p2_pysr_pysindy_pde_discovery.py (< 0.05s runtime, with --planted-defect overfit/underfit controls; does not execute Dedalus, PySINDy, PySR, or JAX-MD).
- Primary literature references checked against Brunton, Proctor & Kutz (2016, DOI 10.1073/pnas.1517384113), de Silva et al. (2020, DOI 10.21105/joss.02104), and Burns et al. (2020, DOI 10.1103/PhysRevResearch.2.023068).
- Mounted live on Informatico.ai's Cover, Physics Hub, and Math Hub via src/modules/physics-discovery-crucible.mjs.

### Open Global Prize Horizon (T2/T3)
- SRBench & PySR / PySINDy Open Research Track (open-source benchmark, no cash prize): Extending automated symbolic discovery to 3D turbulent closure tensors with energy-conserving symmetries checked in Lean 4.
