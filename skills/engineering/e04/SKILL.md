---
name: counter-current-enthalpy-exchanger
description: AI-agnostic thermal and psychrometric engineering skill for counter-current heat and enthalpy recovery exchangers (epsilon-NTU), membrane moisture sorption, and frost-limit psychrometrics.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Counter-Current Enthalpy Recovery Exchangers: Effectiveness–NTU, Membrane Sorption, and Frost Limits (Folio E.04)

A plain-text companion to the essay at https://informatico.ai/engineering/e04/ (`E.04 · Coupled Heat & Mass Transfer · CSI 23 72 23`, `REV 1.2`, redated `2026-11-14`).

## The governing relation
`ε = NTU / (1 + NTU) · Bi_m = h_m δ_m / D_w · CSI 23 72 23`

## Rules the essay derives
1. For balanced counter-current flow (C_min / C_max = 1), compute effectiveness epsilon = NTU / (1 + NTU).
2. Evaluate membrane latent NTU_m = A_tot * U_m / m_dot_da where 1/U_m = 2/h_m + delta_m / D_eff_membrane.
3. Check exhaust plate surface temperature T_plate_cold > T_frost(omega_exhaust) to avoid ice blockage.

## How it works, in four stages
- Stage 1 (Balanced Counter-Current Flow, C_r = 1.0): At NTU = 7.5, sensible effectiveness reaches ε_s = NTU / (1 + NTU) = 7.5 / 8.5 = 88.2%.
- Stage 2 (Membrane Vapor Permeation): Water vapor dissolves into and diffuses across a dense hydrophilic membrane. The page assumes a 25 μm membrane with Bi_m = 0.26, illustrative values; how well a real membrane holds back other gases depends on the product and was not modelled.
- Stage 3 (Frost Threshold): Moving moisture across the membrane lowers the dew point of the exhaust stream, so frost starts at colder outdoor temperatures. The page uses a simple linear estimate, T_frost = −3.0 − 9.5 (ε_l / 79.4%) °C, which gives −12.5 °C at the defaults; it is an illustration, not a psychrometric calculation.
- Stage 4 (Channel Geometry): Fully developed laminar flow between wide parallel plates has Nu ≈ 7.54 at constant wall temperature. The core pressure drop of 118 Pa at 2.1 m/s is a fixed illustrative value.

## Reference values stated in the essay
- **Sensible Effectiveness (ε_s)**: `88.2% (NTU = 7.5)`
- **Latent Moisture Recovery (ε_l)**: `79.4% (NTU_m = 3.85)`
- **Frost-Free Outdoor Limit**: `-12.5 °C (illustrative linear estimate; -3.0 °C sensible-only)`
- **Model Status**: `MODEL VALUES · BALANCED FLOW (C_r = 1)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1115/1.3644004 (Scite report: https://scite.ai/reports/10.1115/1.3644004)
- What the essay compares against: Model values: ε_s = 7.5/8.5 = 88.2% · ε_l = 3.85/4.85 = 79.4%

## Recent research context
- **Membrane Enthalpy Cores Move Water Vapor as Well as Heat**: Extending Kays & London's ε-NTU compact heat exchanger method (record: DOI 10.1115/1.3644004), membrane enthalpy cores move water vapor by solution-diffusion as well as heat, which can reduce condensation and frost in cold weather (Van Vu & Dvořák 2017, DOI 10.1051/epjconf/201714302080). At the default settings this page models 79.4% latent effectiveness; its frost limit of −12.5 °C is an illustrative estimate.
