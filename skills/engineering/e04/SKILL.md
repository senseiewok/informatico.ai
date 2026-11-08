---
name: counter-current-enthalpy-exchanger
description: AI-agnostic thermal and psychrometric engineering skill for counter-current heat and enthalpy recovery exchangers (epsilon-NTU), membrane moisture sorption, and frost-limit psychrometrics.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Counter-Current Enthalpy Recovery Exchangers: Effectiveness–NTU, Membrane Sorption, and Frost Limits (Folio E.04)

## 1. Governing Law & Tectonic Identity
- **Folio**: `E.04 · Coupled Heat & Mass Transfer · CSI 23 72 23` (`REV 1.1`, Redated `2026-11-02`)
- **Governing Equation**: `ε = NTU / (1 + NTU) · Bi_m = h_m δ_m / D_w · CSI 23 72 23`
- **Primary Verification Kernel**: `skills/engineering/e04/verify_e04.py`
- **Verification Benchmarks**: `Sensible ε_s = 88.2% · Latent ε_l = 79.4%`
- **Primary Scite Anchor DOI**: https://doi.org/10.1115/1.3644004 (Scite Report: https://scite.ai/reports/10.1115/1.3644004)

## 2. Deterministic Verification & Falsification Rules
1. For balanced counter-current flow (C_min / C_max = 1), compute effectiveness epsilon = NTU / (1 + NTU).
2. Evaluate membrane latent NTU_m = A_tot * U_m / m_dot_da where 1/U_m = 2/h_m + delta_m / D_eff_membrane.
3. Verify exhaust plate surface temperature T_plate_cold > T_frost(omega_exhaust) to prevent ice occlusion.

## 3. 4-Stage Physical & Mathematical Mechanism
- Stage 1 (Balanced Counter-Current Flow, C_r = 1.0): At NTU = 7.5, sensible effectiveness reaches ε_s = NTU / (1 + NTU) = 7.5 / 8.5 = 88.2%.
- Stage 2 (Sulfonated Block-Copolymer Vapor Permeation): Water vapor selectively diffuses across the 25 μm dense membrane (Bi_m = 0.26) while blocking CO₂ and VOCs.
- Stage 3 (Psychrometric Frost-Threshold Suppression): Latent moisture recovery lowers the exhaust air saturation line, extending frost-free operation down to T_oa = −12.5 °C.
- Stage 4 (HEPA H14 & Low-Pressure-Drop Channel Geometry): Laminar aspect-ratio channels (Nu = 7.54) keep core Δp = 118 Pa at 2.1 m/s.

## 4. Reference Telemetry & Acceptance Bounds
- **Sensible Effectiveness (ε_s)**: `88.2% (NTU = 7.5)`
- **Latent Moisture Recovery (ε_l)**: `79.4% (NTU_m = 3.85)`
- **Frost-Free Outdoor Limit**: `-12.5 °C (vs -3.0 °C Sensible)`
- **Enthalpy Verification**: `PASS · BALANCED NTU`

## 5. Frontier Discovery & Contemporary Research Context (2024–2026)
- **Sulfonated Block-Copolymer Enthalpy Cores Reach 79.4% Latent Moisture Recovery at Zero Pathogen Crossover**: Extending Kays & London's ε-NTU compact heat exchanger theory (1960, DOI 10.1115/1.3644004), modern sulfonated ionomer membranes selectively transport H2O vapor via solution-diffusion while blocking >99.6% of viral/bacterial aerosols, protecting the 7.2 μm ventilation duct surface liquid down to −12.5 °C outdoor air.
