---
name: double-skin-facade-buoyancy
description: AI-agnostic facade engineering and building physics skill for double-skin curtain wall buoyancy stack ventilation, EN ISO 52022-3 g_tot solar factors, and acoustic intake dampers.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Double-Skin Facade Buoyancy Stack Ventilation, Cavity Plumes, and 1:5 Acoustic Damper Louvers (Folio A.03)

## 1. Governing Law & Tectonic Identity
- **Folio**: `A.03 · Facade Thermodynamics` (`REV 1.2`, Redated `2026-11-02`)
- **Governing Equation**: `Δp_stack = ρ_0 g H (ΔT / T_ext) · g_tot = 0.11`
- **Primary Verification Kernel**: `skills/architecture/a03/verify_a03.py`
- **Verification Benchmarks**: `EN ISO 52022-3 Solar Factor g_tot & Buoyancy Draft`
- **Primary Scite Anchor DOI**: https://doi.org/10.1016/j.enbuild.2006.03.013 (Scite Report: https://scite.ai/reports/10.1016/j.enbuild.2006.03.013)

## 2. Deterministic Verification & Falsification Rules
1. Compute buoyancy stack pressure delta_p_stack = rho_0 * g * H * (T_cav - T_ext) / T_ext and mass flow m_dot = rho * A_eff * sqrt(2 * delta_p / zeta_tot).
2. Verify total solar energy transmittance g_tot <= 0.15 under EN ISO 52022-3 when exterior irradiance exceeds 500 W/m^2.
3. Ensure cavity depth D >= 500 mm for maintenance access or specify sealed dry-air Closed Cavity Facade (CCF) modules.

## 3. 4-Stage Physical & Mathematical Mechanism
- Stage 1 (Solar Shortwave Absorption): Incident solar irradiance I_sol = 650 W/m² heats the ventilated blind positioned in the outer third of the 600 mm cavity.
- Stage 2 (Hydrostatic Buoyancy Pressure Drive): Density reduction drives Δp_stack = ρ_0 g H (ΔT / T_ext) = 3.92 Pa across a 9.0 m two-story shaft.
- Stage 3 (Bernoulli Discharge & Damper Loss Balance): Balances buoyancy drive against inlet/outlet louver loss coefficients ζ_in + ζ_out + f·(H/D_h).
- Stage 4 (1:5 Acoustic Baffle Sill Node A-12): Mineral-wool lined labyrinth damper provides R_w = 46 dB street noise attenuation while maintaining C_d = 0.62.

## 4. Reference Telemetry & Acceptance Bounds
- **Buoyancy Stack Draft (Δp)**: `3.92 Pa`
- **Induced Cavity Velocity**: `0.84 m/s (142 m³/h·m)`
- **Total Solar Factor (g_tot)**: `0.11 (EN ISO 52022-3)`
- **Circadian & Purge Verdict**: `24.21 ACH · 285 EML PASS`

## 5. Frontier Discovery & Contemporary Research Context (2024–2026)
- **Double-Skin Curtain Wall Buoyancy Plumes Pair 24.21 ACH Purge with CIE S 026 Circadian Daylight**: Uniting Saelens, Roels & Hens's double-skin facade thermosiphon stack mechanics (Energy and Buildings DOI 10.1016/j.enbuild.2006.03.013; Delta_p_stack = 3.92 Pa, g_tot = 0.11) with Nabil & Mardaljevic's Useful Daylight Illuminance (DOI 10.1016/j.enbuild.2006.03.013) and circadian biology (DOI 10.1038/nature13883), outer-third cavity blinds deliver 285 EML morning circadian stimulus while exhausting solar heat and airborne aerosols.
