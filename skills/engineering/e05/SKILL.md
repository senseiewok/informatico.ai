---
name: terzaghi-cfa-geotechnical-piling
description: Explanatory geotechnical reference (not a foundation or structural design method) for Terzaghi 1D consolidation, effective stress, and an illustrative continuous flight auger pile algebraic model; no number here may be used on a real structure.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Terzaghi Soil Mechanics, CFA Augercast Deep Foundation Piling & Excess Pore Pressure (Folio E.05)

A plain-text companion to the essay at https://informatico.ai/engineering/e05/ (`E.05 · Geotechnical & Deep Foundations · Teaching Model`, `REV 1.2`, redated `2026-11-14`).

## The governing relation
`∂u/∂t = c_v ∂²u/∂z² · Q_ult = Q_skin + Q_toe · r_u = Δu / σ'_{v0}`

## Rules the essay derives
1. Explanatory model only, not a geotechnical or structural design method (no number here may be used on a real structure): with assumed H_dr = 6 m and t = 3.6 yr, compute T_v = c_v * t / H_dr^2, piecewise U_avg(T_v), and assumed S_c = (Delta_q / 120) * 66.7 * U_avg.
2. Evaluate illustrative Q_ult = max(650, 2,380 * (1 - 0.65 * r_u) + 1,980 * (1 - 0.35 * r_u)) against assumed P_design = 1,400 + 1.25 * Delta_q using r_u = min(0.98, Delta_q * (1 - U_avg) / 200) (untested assumptions, not code values).
3. Treat r_u >= 0.70 or FS = Q_ult / P_design < 2.0 as an illustrative alert, not a code check; cyclic liquefaction (Seed & Idriss 1971, DOI 10.1061/JSFEAQ.0001662) requires site testing.

## How it works, in four stages
- Stage 1 (Undrained Surcharge Application, t = 0⁺): Assumed surcharge Δq = 120 kPa transfers initially into excess pore pressure Δu(z, 0) = Δq in saturated clay (Terzaghi 1925).
- Stage 2 (Terzaghi Hydrodynamic Dissipation): With assumed H_dr = 6 m and t = 3.6 yr at c_v = 3.2 m²/yr, T_v = 0.320 gives U_avg = 63.2% and assumed settlement S_c = (Δq / 120) × 66.7 × U_avg = 42.2 mm.
- Stage 3 (Assumed CFA Shaft + Toe Model): Illustrative 750 mm by 24 m CFA capacities follow Q_ult = 2,380 × (1 − 0.65 r_u) + 1,980 × (1 − 0.35 r_u) = 3,865 kN at unrounded r_u = 0.2208 against assumed P_design = 1,400 + 1.25 Δq = 1,550 kN (FS = 2.49; untested assumptions, not a design method).
- Stage 4 (Consolidation Pore-Pressure Ratio): Residual Δu = Δq (1 − U_avg) = 44.2 kPa over assumed σ'_{v0} = 200 kPa gives r_u = 0.22 (σ'_v = 156 kPa), distinct from seismic liquefaction (Seed & Idriss 1971, DOI 10.1061/JSFEAQ.0001662); r_u ≥ 0.70 or FS < 2.0 is an illustrative alert.

## Reference values stated in the essay
- **Average Consolidation U_avg (Model)**: `63.2% (S_c = 42.2 mm, model)`
- **CFA Pile Capacity (Illustrative)**: `3,865 kN (FS = 2.49, model)`
- **Consolidation Ratio r_u (Assumed)**: `0.22 (σ'_v = 156 kPa)`
- **Illustrative Model Check**: `MODEL FS ≥ 2.0 · ILLUSTRATIVE, NOT A SITE DESIGN`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1061/(ASCE)GT.1943-5606.0000073 (Scite report: https://scite.ai/reports/10.1061/(ASCE)GT.1943-5606.0000073)
- What the essay compares against: Assumed defaults: T_v = 0.320 · U_avg = 63.2% · Q_ult = 3,865 kN

## Recent research context
- **A Century After Erdbaumechanik: Effective Stress, Consolidation, and Monitored CFA Piles**: Connecting Terzaghi's 1925 effective stress model with FHWA GEC No. 8 rig monitoring (Brown et al. 2007) and sand shaft tests (Gavin, Cadogan & Casey 2009, DOI 10.1061/(ASCE)GT.1943-5606.0000073). This untested explanation estimates U_avg = 63.2% and Q_ult = 3,865 kN under assumed inputs; no figure belongs on a real structure.
