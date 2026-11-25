---
name: double-skin-facade-buoyancy
description: Explanatory building-physics reference (not a facade design method) for double-skin curtain-wall buoyancy stack draft, EN ISO 52022-3 g_tot concepts, and acoustic intake dampers.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Double-Skin Facade Buoyancy Stack Ventilation, Cavity Plumes, and 1:5 Acoustic Damper Louvers (Folio A.03)

A plain-text companion to the essay at https://informatico.ai/architecture/a03/ (`A.03 · Facade Thermodynamics`, `REV 1.3`, redated `2026-11-14`).

## The governing relation
`Δp_stack = ρ_0 g H (ΔT / T_ext) · g_tot = 0.11 (assumed)`

## Rules the essay derives
1. Explanatory, untested model only, not a facade design method: none of these numbers may be used to design or size a real building or curtain wall.
2. Under stated assumptions, estimate hydrostatic stack draft delta_p_stack = rho_0 * g * H * (T_cav - T_ext) / T_ext (ideal-gas beta = 1 / T_ext; baseline assumes rho_0 = 1.2 kg/m^3, T_ext about 303 K, zeta_tot about 9.3, opening area A about 0.047 m^2/m), cavity speed v = sqrt(2 * delta_p_stack / (zeta_tot * rho_0)), and mass flow m_dot = rho_0 * A * v = A * sqrt(2 * rho_0 * delta_p_stack / zeta_tot).
3. Calculate total solar energy transmittance g_tot with the EN ISO 52022-3 method; this folio uses an illustrative target g_tot <= 0.15 above 500 W/m^2 (not a requirement of the standard), and in the browser lab g_tot = 0.11 and 285 EML remain fixed text while 24.21 ACH rescales with velocity.
4. This folio assumes a cavity depth D >= 500 mm for maintenance access (an assumed parameter, not a code requirement), or sealed dry-air Closed Cavity Facade (CCF) modules.

## How it works, in four stages
- Stage 1 (Solar Shortwave Absorption): An assumed solar irradiance I_sol = 650 W/m² heats the ventilated blind positioned in the outer third of the 600 mm cavity.
- Stage 2 (Hydrostatic Buoyancy Pressure Drive): Δp_stack = ρ_0 g H (ΔT / T_ext) = 1.2 × 9.81 × 9.0 × (11.2 / 303) = 3.92 Pa across a 9.0 m two-story shaft (ideal-gas β ≈ 1 / T_ext, T_ext ≈ 303 K, about 30 °C, assumed).
- Stage 3 (Bernoulli Discharge & Damper Loss Balance): Setting Δp = ζ_tot ρ v² / 2 gives v = 0.84 m/s for an assumed total loss coefficient ζ_tot ≈ 9.3. The 142 m³/h per meter of facade assumes an opening of about 0.047 m² per meter.
- Stage 4 (1:5 Acoustic Baffle Sill Node A-12): A proposed mineral-wool lined labyrinth damper with design targets of R_w = 46 dB and C_d = 0.62 (targets, not measured).

## Reference values stated in the essay
- **Buoyancy Stack Draft (Δp, Model)**: `3.92 Pa`
- **Induced Cavity Velocity (Model)**: `0.84 m/s (142 m³/h·m)`
- **Total Solar Factor (g_tot, Fixed Text)**: `0.11 (assumed; EN ISO 52022-3 method)`
- **Rescaled ACH & Fixed Daylight (Illustrative)**: `24.21 ACH · 285 EML (illustrative)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/j.enbuild.2006.03.013 (Scite report: https://scite.ai/reports/10.1016/j.enbuild.2006.03.013)
- What the essay compares against: Model values: Δp = 3.92 Pa (ρ_0 = 1.2 kg/m³, H = 9.0 m, ΔT = 11.2 K, T_ext ≈ 303 K) · g_tot = 0.11 fixed text

## Recent research context
- **Double-Skin Curtain Wall Buoyancy: An Explanatory Stack-Draft Model Beside Daylight Metrics**: Drawing on Saelens, Roels, and Hens's comparison of multiple-skin facade strategies (Building and Environment DOI 10.1016/j.buildenv.2006.06.024), Nabil and Mardaljevic's Useful Daylight Illuminance (DOI 10.1016/j.enbuild.2006.03.013), and the daytime light recommendation of Brown et al. (DOI 10.1371/journal.pbio.3001571), this folio models a 9.0 m cavity with an estimated stack draft of 3.92 Pa under stated assumptions. Its air-change and daylight readouts are illustrative, and it makes no health claim.
