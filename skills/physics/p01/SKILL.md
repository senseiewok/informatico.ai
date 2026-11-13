---
name: keizer-fluctuation-dissipation
description: AI-agnostic physical skill for non-equilibrium chemical reaction-diffusion fluctuation covariance, Harada-Sasa dissipation, and Hill cycle diagrams.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Non-Equilibrium Fluctuation-Dissipation Theorems and Allosteric Gating Energetics (Folio P.01)

A plain-text companion to the essay at https://informatico.ai/physics/p01/ (`P.01 · Non-Equilibrium Gating`, `REV 1.2`, redated `2026-11-02`).

## The governing relation
`σ_ij = −k_B (∂²S / ∂α_i ∂α_j)⁻¹ · A_r = k_B T ln(v_r⁺ / v_r⁻)`

## Rules the essay derives
1. Evaluate covariance sigma_ij from second entropy derivatives and linear stability matrix M.
2. Enforce positive coupling efficiency >= 0.75 for functional cyclic transport.
3. Check dissipation-fluctuation ratio <= 2.0 to exclude kinetic traps.

## How it works, in four stages
- Stage 1 (Uncoupled Kinetic Trap, G551D): Gating cross-covariance sigma_ATP,Cl ≈ 0.05 fails to transmit chemical affinity into pore dilation.
- Stage 2 (Fluctuation-Dissipation Coupling): Keizer matrix d sigma/dt = M sigma + sigma M^T + Gamma matches forward and backward reaction fluxes.
- Stage 3 (Dual-Corrector Stabilization): Ivacaftor/Trikafta lowers activation barrier Delta G^‡ and restores coupling efficiency to 0.84.
- Stage 4 (Stationary NESS Cycle): Bounded dissipation-fluctuation ratio (1.12 <= 2.0) maintains stable open-state chloride conduction.

## Reference values stated in the essay
- **Coupling Efficiency**: `0.88 (WT) vs 0.08 (G551D)`
- **Dissipation-Fluctuation Ratio**: `1.12 (Coupled Cycle)`
- **Gating Regime**: `STABLE_COUPLED_CYCLE`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1088/0034-4885/75/12/126001 (Scite report: https://scite.ai/reports/10.1088/0034-4885/75/12/126001)
- What the essay compares against: Cryo-EM 6MSM / 8EIQ · Eyring Rate Theory

## Recent research context
- **Single-Molecule Non-Equilibrium Thermodynamics Decodes ATP-Driven ABC-transporter Channel Gating**: Extending Keizer's fluctuation-dissipation theorem and Csanády's irreversible ABC-transporter gating cycle (J. Gen. Physiol. DOI 10.1085/jgp.200609558; Seifert Rep. Prog. Phys. DOI 10.1088/0034-4885/75/12/126001), next-generation triple modulators (vanzacaftor/tezacaftor/deutivacaftor, Alyftrek DOI 10.58347/tml.2025.1724a) stabilize the NBD1-NBD2 dimer to restore open probability P_o > 0.75.
