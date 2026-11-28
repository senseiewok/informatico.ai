---
name: asce7-seismic-base-isolation
description: AI-agnostic structural dynamics and earthquake engineering skill for ASCE 7-22 Chapter 17 seismic base isolation, bilinear lead-rubber bearing hysteresis, and inelastic response spectra. Explanation, not a design method; none of its numbers may be used on a real structure.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Nonlinear Structural Dynamics, ASCE 7-22 Inelastic Response Spectra & Seismic Base-Isolation Dampers (Folio E.06)

A plain-text companion to the essay at https://informatico.ai/engineering/e06/ (`E.06 · Seismic Structural Dynamics · CSI 13 48 00`, `REV 1.2`, redated `2026-11-14`).

## The governing relation
`M ü + C u̇ + F_s(u) = −M ü_g(t) · V_b = C_s W · μ_Δ = Δ_max / Δ_y`

## Rules the essay derives
1. Explanation, not a design method: none of this folio's assumed numbers (T_M = 2.85 s, beta_eff = 22%, B_M = 1.54, D_M = 276 mm, C_s = 0.137, the 400 mm moat, the bearing dimensions) may be used on a real structure.
2. Compute secant isolator stiffness k_eff = Q_d / D_M + k_d and effective isolated period T_M = 2 * pi * sqrt(W / (g * k_eff)).
3. Evaluate bilinear hysteretic loop energy E_loop = 4 * Q_d * (D_M - D_y), equivalent viscous damping beta_eff = E_loop / (2 * pi * k_eff * D_M^2), and ASCE 7-22 damping factor B_M.
4. Check that the design displacement D_M = (g * S * T_M) / (4 * pi^2 * B_M) stays within the moat clearance and that story drift meets the limits of the governing code; take the spectral value S, the B_M table and the drift limits from the current edition of the standard, not from this skill.

## How it works, in four stages
- Stage 1 (Fixed-Base Response): The page assumes S_D1 = 0.60 S_DS, so at S_DS = 1.00 g the spectral plateau ends at T_s = 0.60 s. An unisolated frame with T_fixed = 0.65 s sits just past it, at S_a = 0.60/0.65 = 0.92 g.
- Stage 2 (Lead-Rubber Period Lengthening, T_M = 2.85 s): Lengthening the period to 2.85 s moves the building onto the 1/T branch, S_a = 0.60/2.85 = 0.21 g, about 77% below the fixed-base value before any damping is counted.
- Stage 3 (Bilinear Lead-Core Hysteretic Energy Dissipation): Plastic shear yielding of the central lead plug dissipates E_loop = 4 Q_d (D_M − D_y) per cycle. The page takes β_eff = 22% from the slider rather than computing it from the bearing properties, and B_M = 1.54 by interpolating 1.5 (20%) and 1.7 (30%).
- Stage 4 (Model Check, Not a Code Check): With D_M = g S_D1 T_M / (4π² B_M) the model gives D_M = 276 mm, inside the assumed 400 mm moat, and C_s = S_D1 / (T_M B_M) = 0.137. Drift, floor acceleration and a full ASCE/SEI 7-22 Chapter 17 design were not checked.

## Reference values stated in the essay
- **Isolated Period & Damping**: `T_M = 2.85 s (B_M = 1.54)`
- **Isolator Displacement D_M**: `276 mm (assumed moat 400 mm)`
- **Seismic Base Shear Ratio**: `V_b / W = 0.137 (−86% vs S_DS)`
- **Model Verdict**: `WITHIN ASSUMED MOAT · NOT A CODE CHECK`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1061/9780784415788 (Scite report: https://scite.ai/reports/10.1061/9780784415788)
- What the essay compares against: Model values: D_M = 276 mm and C_s = 0.137 at S_DS = 1.00 g, S_D1 = 0.60 g, B_M = 1.54

## Recent research context
- **ASCE 7-22 Chapter 17 Multi-Period MCE_R Spectra & Bilinear Lead-Rubber Hospital Isolation**: Building on Maurice Biot's 1932 response spectrum and William Robinson's tests of lead-rubber bearings (1982, DOI 10.1002/eqe.4290100408), ASCE/SEI 7-22 (DOI 10.1061/9780784415788) sets requirements for seismically isolated structures in its Chapter 17. In this page's equivalent-linear model, isolating a building at T_M = 2.85 s with 22% damping lowers the base shear coefficient from 0.92 to 0.137.
