---
name: topological-photonics-haldane-chern
description: AI-agnostic wave-physics and metamaterial skill for Haldane-Raghu photonic Chern insulators, Berry curvature integration, Dirac mass inversions, and backscatter-free chiral edge waveguides.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Topological Photonics, Haldane–Raghu Photonic Chern Insulators, Berry Curvature & Backscatter-Free Chiral Edge Waveguides (Folio P.10)

A plain-text companion to the essay at https://informatico.ai/physics/p10/ (`P.10 · Haldane–Raghu Topological Photonics & Berry Curvature`, `REV 1.0`, redated `2026-11-03`).

## The governing relation
`C_n = (1/2π) ∮_{BZ} Ω_n(k) d²k ∈ ℤ · Ω_n = i⟨∇_k u_n | × | ∇_k u_n⟩ · |m_T| > |m_P| ⇒ |C| = 1`

## Rules the essay derives
1. Evaluate valley Dirac masses M_K = m_P - m_T and M_K' = m_P + m_T and compute First Chern Number C = (sgn(m_P + m_T) - sgn(m_P - m_T)) / 2.
2. Verify topological phase condition |m_T| > |m_P| (|C| = 1) and relative bandgap width Delta_omega / omega_0 proportional to ||m_T| - |m_P||.
3. Invoke bulk-boundary correspondence Delta_C = C_bulk - C_clad to count the number of unidirectional chiral edge modes immune to Anderson backscattering.

## How it works, in four stages
- Stage 1 (Honeycomb Dirac Degeneracy, Continuing P.08 Bragg Optics): Time-reversal & inversion-symmetric honeycomb photonic crystal exhibits gapless Dirac cones at K and K'.
- Stage 2 (Haldane–Raghu Gyromagnetic Gap Opening, DOI 10.1103/PhysRevLett.100.013904): Breaking T-symmetry with m_T = 0.55 > m_P = 0.25 inverts the K' valley mass and opens a 14.2% topological bandgap.
- Stage 3 (Quantized Berry Flux & Chern Number C = +1): Integrating Berry curvature Ω_-(k) across the Brillouin zone yields C = +1, guaranteeing a chiral gapless boundary state.
- Stage 4 (Backscatter-Free 90° Bend & Defect Bypass): Even under strong structural disorder σ_def = 0.30, the one-way edge wave maintains 99.8% forward transmission (vs. 34% in trivial guides).

## Reference values stated in the essay
- **Topological Chern Invariant**: `C = +1 (Topological Phase)`
- **Relative Bandgap (Δω / ω_0)**: `14.2% (|m_T − m_P| Gap)`
- **Forward Defect Transmission**: `99.8% (vs 34.2% Trivial)`
- **Bulk-Boundary Verdict**: `BACKSCATTER-FREE · PASS`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1103/PhysRevLett.100.013904 (Scite report: https://scite.ai/reports/10.1103/PhysRevLett.100.013904)
- What the essay compares against: m_T = 0.55 > m_P = 0.25 ⇒ C = +1 · Δω/ω_0 = 14.2% · T_forward = 99.8%

## Recent research context
- **Haldane–Raghu Photonic Chern Insulators & Berry Curvature Route Light Around 90° Defects With Zero Backscatter**: Synthesizing the acoustic and optical wave monographs of Folios E.03, A.05, A.08, and P.08, F. Duncan M. Haldane & Srinivas Raghu (Phys. Rev. Lett. DOI 10.1103/PhysRevLett.100.013904) proved that non-zero Berry curvature in gyromagnetic honeycomb lattices creates topologically protected C = +1 chiral edge highways immune to disorder.
