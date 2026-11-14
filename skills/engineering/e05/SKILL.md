---
name: terzaghi-cfa-geotechnical-piling
description: AI-agnostic civil geotechnical engineering skill for Terzaghi 1D consolidation (du/dt = c_v d^2u/dz^2), effective stress sigma'_v = sigma_v - u, CFA deep foundation capacity, and liquefaction r_u screening.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Terzaghi Soil Mechanics, CFA Augercast Deep Foundation Piling & Liquefaction Surcharge (Folio E.05)

A plain-text companion to the essay at https://informatico.ai/engineering/e05/ (`E.05 · Geotechnical & Deep Foundations · CSI 31 63 23`, `REV 1.1`, redated `2026-11-02`).

## The governing relation
`∂u/∂t = c_v ∂²u/∂z² · Q_ult = Q_skin + Q_toe · r_u = Δu / σ'_{v0}`

## Rules the essay derives
1. Compute Terzaghi dimensionless time factor T_v = (c_v * t) / H_dr^2 and degree of consolidation U_avg = sqrt(4*T_v/pi) for T_v <= 0.286 or U_avg = 1 - (8/pi^2)*exp(-pi^2 * T_v / 4) for T_v > 0.286.
2. Evaluate axial CFA pile ultimate capacity Q_ult = Q_skin + Q_toe using effective overburden stress sigma'_v(z) = sigma_v(z) - u(z) reduced by excess pore-pressure ratio (1 - r_u).
3. Flag seismic or undrained liquefaction instability whenever excess pore-pressure ratio r_u = Delta_u / sigma'_v0 >= 0.75 or factor of safety FS = Q_ult / P_design < 2.0.

## How it works, in four stages
- Stage 1 (Undrained Surcharge Application, t = 0⁺): Structural surcharge Δq = 120 kPa transfers initially 100% into excess pore-water pressure Δu(z, 0) = Δq.
- Stage 2 (Terzaghi Hydrodynamic Dissipation): Pore water drains toward permeable sand boundaries via ∂u/∂t = c_v ∂²u/∂z² (T_v = c_v t / H_dr² = 0.322, U_avg = 64.2%).
- Stage 3 (CFA Augercast Shaft + Toe Mobilization): 750 mm diameter, 24 m deep CFA pile mobilizes cylindrical skin friction Q_skin and dense sand toe bearing Q_toe (Q_ult = 4,180 kN).
- Stage 4 (Liquefaction Pore-Pressure Guard, r_u = Δu / σ'_{v0}): Verifies excess pore-pressure ratio r_u = 0.28 stays well below the r_u ≥ 0.80 liquefaction onset threshold.

## Reference values stated in the essay
- **Average Consolidation U_avg**: `64.2% (S_c = 42.8 mm)`
- **CFA Ultimate Pile Capacity**: `4,180 kN (FS = 2.79)`
- **Pore-Pressure Ratio r_u**: `0.28 (σ'_v = 144 kPa)`
- **Geotechnical Verdict**: `SAFE BEARING · NO LIQUEFACTION`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1061/(ASCE)GT.1943-5606.0000073 (Scite report: https://scite.ai/reports/10.1061/(ASCE)GT.1943-5606.0000073)
- What the essay compares against: FHWA GEC-8 CFA Piles · Seed-Idriss Liquefaction

## Recent research context
- **Real-Time Drilling Torque/Grout Telemetry Meets Terzaghi Consolidation & Two-Gel Airway Surface Physics**: One century after Karl Terzaghi's Erdbaumechanik (1925), modern Continuous Flight Auger (CFA) piling rigs (FHWA GEC-8; ASCE J. Geotech. Geoenviron. Eng. DOI 10.1061/(ASCE)GT.1943-5606.0000073) combine real-time specific-energy torque profiles with Seed–Idriss liquefaction screening, while Button, Rubinstein & Boucher (Science DOI 10.1126/science.1223012) proved that the exact same Terzaghi poroelastic consolidation law governs osmotic collapse of the periciliary airway brush.
