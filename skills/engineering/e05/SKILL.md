---
name: terzaghi-cfa-geotechnical-piling
description: AI-agnostic civil geotechnical engineering skill for Terzaghi 1D consolidation (du/dt = c_v d^2u/dz^2), effective stress sigma'_v = sigma_v - u, CFA deep foundation capacity, and excess pore-pressure r_u screening.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Terzaghi Soil Mechanics, CFA Augercast Deep Foundation Piling & Excess Pore Pressure (Folio E.05)

A plain-text companion to the essay at https://informatico.ai/engineering/e05/ (`E.05 · Geotechnical & Deep Foundations · CSI 31 63 23`, `REV 1.2`, redated `2026-11-14`).

## The governing relation
`∂u/∂t = c_v ∂²u/∂z² · Q_ult = Q_skin + Q_toe · r_u = Δu / σ'_{v0}`

## Rules the essay derives
1. Compute Terzaghi dimensionless time factor T_v = (c_v * t) / H_dr^2 and degree of consolidation U_avg = sqrt(4*T_v/pi) for T_v <= 0.286 or U_avg = 1 - (8/pi^2)*exp(-pi^2 * T_v / 4) for T_v > 0.286.
2. Evaluate axial CFA pile ultimate capacity Q_ult = Q_skin + Q_toe using effective overburden stress sigma'_v(z) = sigma_v(z) - u(z); this folio assumes the shaft term is scaled by (1 - 0.65 r_u) and the toe term by (1 - 0.35 r_u), its own illustrative factors.
3. Flag the design for review whenever excess pore-pressure ratio r_u = Delta_u / sigma'_v0 >= 0.70 or factor of safety FS = Q_ult / P_design < 2.0 (both are this folio's screening choices, not code values); a real liquefaction assessment needs a site-specific cyclic analysis.

## How it works, in four stages
- Stage 1 (Undrained Surcharge Application, t = 0⁺): Structural surcharge Δq = 120 kPa transfers initially 100% into excess pore-water pressure Δu(z, 0) = Δq.
- Stage 2 (Terzaghi Hydrodynamic Dissipation): Pore water drains toward permeable sand boundaries via ∂u/∂t = c_v ∂²u/∂z². The page assumes a drainage path H_dr = 6 m and an elapsed time t = 3.6 years, so T_v = 3.2 × 3.6 / 6² = 0.320 and U_avg = 1 − (8/π²) exp(−π² T_v / 4) = 63.2%.
- Stage 3 (CFA Augercast Shaft + Toe Mobilization): A 750 mm diameter, 24 m deep CFA pile carries load by shaft friction and toe bearing. The page uses fixed illustrative capacities of 2,380 kN (shaft) and 1,980 kN (toe), and the folio assumes that residual pore pressure reduces them by factors of 0.65 r_u (shaft) and 0.35 r_u (toe): Q_ult = 2,380 × (1 − 0.65 r_u) + 1,980 × (1 − 0.35 r_u). With r_u = 0.221 (Stage 4, unrounded) this gives Q_ult = 3,865 kN against an assumed design load of 1,400 kN + 1.25 kN per kPa of surcharge (FS = 2.49). The 0.65 and 0.35 factors are this folio's own assumptions, not code values.
- Stage 4 (Pore-Pressure Ratio, r_u = Δu / σ'_{v0}): The residual excess pore pressure after consolidation, Δu = Δq (1 − U_avg) = 44.2 kPa, over an assumed σ'_{v0} = 200 kPa gives r_u = 0.22. This is a consolidation ratio, not a seismic liquefaction analysis; r_u = 1 would mean zero effective stress, and the page flags r_u ≥ 0.70 as its own screening choice.

## Reference values stated in the essay
- **Average Consolidation U_avg**: `63.2% (S_c = 42.2 mm, model)`
- **CFA Ultimate Pile Capacity**: `3,865 kN (FS = 2.49, model)`
- **Pore-Pressure Ratio r_u**: `0.22 (σ'_v = 156 kPa)`
- **Geotechnical Verdict**: `MODEL FS ≥ 2.0 · ILLUSTRATIVE, NOT A SITE DESIGN`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1061/(ASCE)GT.1943-5606.0000073 (Scite report: https://scite.ai/reports/10.1061/(ASCE)GT.1943-5606.0000073)
- What the essay compares against: Model values at defaults: T_v = 0.320 · U_avg = 63.2% (H_dr = 6 m, t = 3.6 yr)

## Recent research context
- **A Century After Erdbaumechanik: Instrumented CFA Piles and Effective Stress**: One century after Karl Terzaghi's Erdbaumechanik (1925), continuous flight auger (CFA) piles are installed with rigs that record depth, torque and grout volume (FHWA GEC No. 8), and field tests show how their shaft resistance develops in sand (Gavin, Cadogan & Casey 2009, DOI 10.1061/(ASCE)GT.1943-5606.0000073). In a different field, Button and colleagues (Science 2012, DOI 10.1126/science.1223012) described osmotic compression of the airway periciliary brush, an idea this folio offers only as an analogy.
