---
name: porous-brinkman-percolation
description: AI-agnostic continuum and porous-media engineering skill for Darcy-Brinkman momentum screening, Helmholtz-Hodge decomposition, and continuum percolation (phi_c = 0.5927).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Stokes–Brinkman Porous Continuum, Helmholtz–Hodge Decomposition, and Percolation (Folio E.01)

A plain-text companion to the essay at https://informatico.ai/engineering/e01/ (`E.01 · Brinkman & Percolation · CSI 03 30 00 / 07 16 00`, `REV 1.4`, redated `2026-11-14`).

## The governing relation
`μ ∇²u − (μ/κ)u = ∇p · φ_c = 0.5927 · u = −∇Φ + ∇×Ψ`

## Rules the essay derives
1. Brinkman Screening Length: sqrt(kappa) = a_f * phi^(3/2) / (2 * (1 - phi)) from mu * nabla^2(u) - (mu/kappa)*u = nabla(p).
2. Lattice Percolation Threshold (model): compare porosity phi with phi_c = 0.5927, the site threshold of the 2D square lattice; the model scales effective diffusivity as ((phi - phi_c) / (1 - phi_c))^1.30. State that this is a lattice idealization; a real material needs its own measured threshold.
3. Discrete Helmholtz-Hodge Decomposition: Separate face-centered flux into L2-orthogonal curl-free potential gradient and divergence-free recirculation.

## How it works, in four stages
- Stage 1 (Supercritical Open Matrix, φ = 0.72): In the lattice model, connected pore channels span the domain; with a_f = 12 nm the Brinkman screening length is √κ = a_f φ^(3/2) / (2(1 − φ)) = 13.09 nm.
- Stage 2 (Critical Percolation Backbone, φ → 0.5927): Tortuous dead-end branches multiply; transport restricts to a fractal spanning cluster. The value 0.5927 is the site-percolation threshold of the two-dimensional square lattice, used here as the model's threshold.
- Stage 3 (Subcritical Arrest, φ < 0.5927): In the lattice model the open sites no longer connect across the domain, so its macroscopic conductivity is zero. Real three-dimensional pore networks stay connected at much lower porosity.
- Stage 4 (Discrete Helmholtz-Hodge Decomposition): Separates velocity into curl-free pressure drive (−∇Φ) and divergence-free pore eddies (∇×Ψ).

## Reference values stated in the essay
- **Brinkman Screening (√κ)**: `13.09 nm`
- **Effective Conductivity**: `0.220 D_0`
- **Percolation Phase Regime**: `SUPERCRITICAL (φ > 0.5927, model)`
- **Helmholtz-Hodge Split**: `ORTHOGONAL BY DEFINITION · not computed here`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1007/BF02120313 (Scite report: https://scite.ai/reports/10.1007/BF02120313)
- What the essay compares against: Model values: φ_c = 0.5927 (square-lattice site threshold) · √κ = 13.09 nm at defaults

## Recent research context
- **Two Questions for Any Porous Material: How Much Drag, and Do the Pores Connect?**: This folio joins Darcy (1856), Brinkman (1949, DOI 10.1007/BF02120313) and the percolation processes of Broadbent & Hammersley (1957, DOI 10.1017/S0305004100032680) in one small model. Its threshold φ_c = 0.5927 is the site value for a square lattice, an idealization: the page does not show that any real mortar, stone or gel has that threshold.
