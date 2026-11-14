---
name: asce7-seismic-base-isolation
description: AI-agnostic structural dynamics and earthquake engineering skill for ASCE 7-22 Chapter 17 seismic base isolation, bilinear lead-rubber bearing hysteresis, and inelastic response spectra.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Nonlinear Structural Dynamics, ASCE 7-22 Inelastic Response Spectra & Seismic Base-Isolation Dampers (Folio E.06)

A plain-text companion to the essay at https://informatico.ai/engineering/e06/ (`E.06 · Seismic Structural Dynamics · CSI 13 48 00`, `REV 1.1`, redated `2026-11-02`).

## The governing relation
`M ü + C u̇ + F_s(u) = −M ü_g(t) · V_b = C_s W · μ_Δ = Δ_max / Δ_y`

## Rules the essay derives
1. Compute secant isolator stiffness k_eff = Q_d / D_M + k_d and effective isolated period T_M = 2 * pi * sqrt(W / (g * k_eff)).
2. Evaluate bilinear hysteretic loop energy E_loop = 4 * Q_d * (D_M - D_y), equivalent viscous damping beta_eff = E_loop / (2 * pi * k_eff * D_M^2), and ASCE 7-22 damping factor B_M.
3. Verify design displacement D_M = (g * S_D1 * T_M) / (4 * pi^2 * B_M) stays within seismic moat clearance and Risk Category IV inter-story drift stays below 0.010 h_sx.

## How it works, in four stages
- Stage 1 (Fixed-Base Resonance Amplification): An unisolated T_fixed = 0.65 s frame sits on the S_DS = 1.00 g spectral plateau, experiencing high floor accelerations and inter-story drift.
- Stage 2 (Lead-Rubber Period Lengthening, T_M = 2.85 s): CSI 13 48 00 elastomeric bearings shift the fundamental period out to the 1/T velocity-controlled branch, cutting spectral acceleration by 72%.
- Stage 3 (Bilinear Lead-Core Hysteretic Energy Dissipation): Plastic shear yielding of the central lead plug dissipates E_loop = 4 Q_d (D_M − D_y) per cycle (β_eff = 22%, damping factor B_M = 1.54).
- Stage 4 (ASCE 7-22 Risk Category IV Verification): Certifies isolator displacement D_M = 232 mm (< 400 mm moat limit), base shear C_s = 0.142 W, and superstructure drift ≤ 0.32%.

## Reference values stated in the essay
- **Isolated Period & Damping**: `T_M = 2.85 s (B_M = 1.54)`
- **Isolator Displacement D_M**: `232 mm (Moat Limit 400 mm)`
- **Seismic Base Shear Ratio**: `V_b / W = 0.142 g (−74%)`
- **ASCE 7-22 Cat IV Verdict**: `IMMEDIATE OCCUPANCY PASS`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1061/9780784415788 (Scite report: https://scite.ai/reports/10.1061/9780784415788)
- What the essay compares against: Risk Category IV Hospital · E_loop = 4 Q_d (D_M − D_y)

## Recent research context
- **ASCE 7-22 Chapter 17 Multi-Period MCE_R Spectra & Bilinear Lead-Rubber Hospital Isolation**: Uniting Maurice Biot's 1932 response spectrum and William Robinson's Lead-Rubber Bearing (LRB), the ASCE/SEI 7-22 standard (DOI 10.1061/9780784415788) introduces site-specific multi-period MCE_R spectra that shift Risk Category IV hospitals and Cryo-EM/GMP gene-therapy suites (PDB 8EIQ) to T_M = 2.85 s, slashing seismic base shear by 74%.
