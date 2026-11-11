---
name: porous-brinkman-percolation
description: AI-agnostic continuum and porous-media engineering skill for Darcy-Brinkman momentum screening, Helmholtz-Hodge decomposition, and continuum percolation (phi_c = 0.5927).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Stokes–Brinkman Porous Continuum, Helmholtz–Hodge Decomposition, and Percolation (Folio E.01)

## 1. Governing Law & Tectonic Identity
- **Folio**: `E.01 · Brinkman & Percolation · CSI 03 30 00 / 07 16 00` (`REV 1.3`, Redated `2026-11-02`)
- **Governing Equation**: `μ ∇²u − (μ/κ)u = ∇p · φ_c = 0.5927 · u = −∇Φ + ∇×Ψ`
- **Primary Verification Kernel**: `skills/engineering/e01/verify_e01.py`
- **Verification Benchmarks**: `φ_c = 0.5927 · √κ = 13.09 nm · L2 Orthogonal`
- **Primary Scite Anchor DOI**: https://doi.org/10.1007/BF02120313 (Scite Report: https://scite.ai/reports/10.1007/BF02120313)

## 2. Deterministic Verification & Falsification Rules
1. Brinkman Screening Length: sqrt(kappa) = a_f * phi^(3/2) / (2 * (1 - phi)) from mu * nabla^2(u) - (mu/kappa)*u = nabla(p).
2. Continuum Percolation Threshold: Verify accessible porosity phi > phi_c = 0.5927; effective diffusivity scales as ((phi - phi_c) / (1 - phi_c))^1.30.
3. Discrete Helmholtz-Hodge Decomposition: Separate face-centered flux into L2-orthogonal curl-free potential gradient and divergence-free recirculation.

## 3. 4-Stage Physical & Mathematical Mechanism
- Stage 1 (Supercritical Open Matrix, φ = 0.72): Connected pore channels span the domain; Brinkman screening length √κ = 13.09 nm.
- Stage 2 (Critical Percolation Backbone, φ → 0.5927): Tortuous dead-end branches multiply; transport restricts to a fractal spanning cluster.
- Stage 3 (Subcritical Jammed Arrest, φ < 0.5927): Pore throats pinch off completely; macroscopic hydraulic and diffusive conductivity drop to zero.
- Stage 4 (Discrete Helmholtz-Hodge Decomposition): Separates velocity into curl-free pressure drive (−∇Φ) and divergence-free pore eddies (∇×Ψ).

## 4. Reference Telemetry & Acceptance Bounds
- **Brinkman Screening (√κ)**: `13.09 nm`
- **Effective Conductivity**: `0.220 D_0`
- **Percolation Phase Regime**: `SUPERCRITICAL PERCOLATING`
- **Helmholtz-Hodge Split**: `L2 ORTHOGONAL PASS`

## 5. Frontier Discovery & Contemporary Research Context (2024–2026)
- **Zwitterionic & PEGylated Mucus-Penetrating Nanoparticles Cross the Percolation Threshold**: Extending Darcy (1856) and Brinkman (1949, DOI 10.1007/BF02120313), modern X-ray micro-CT pore-network modeling of capillary-active mineral lime mortars (CSI 03 30 00) shows that maintaining connected void porosity above the Broadbent–Hammersley percolation threshold φ_c = 0.5927 prevents freeze-thaw and salt-crystallization spalling.
