---
name: radiative-sky-cooling-stefan-pcm
description: AI-agnostic building-physics and photonic-envelope skill for daytime radiative sky cooling across the 8-13 um atmospheric window and Stefan phase-change thermal storage.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# AI-Designed Daytime Radiative Sky-Cooling Photonic Roofs (8–13 μm Window) & Stefan Phase-Change Envelopes (Folio A.08)

A plain-text companion to the essay at https://informatico.ai/architecture/a08/ (`A.08 · Photonic Sky-Cooling & Stefan PCM · CSI 07 54 00`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`P_net = P_rad(T) − P_atm(T_a) − (1 − R_sol)I_sol − h_c(T_a − T) · s(t) = 2λ_s√(α t) · CSI 07 54 00`

## Rules the essay derives
1. Evaluate net radiative cooling flux P_net(T) = epsilon_LWIR * sigma * T^4 - P_atm(T_amb) - (1 - R_solar) * I_solar - h_c * (T_amb - T).
2. Treat R_solar >= 0.94 across 0.3-2.5 um and epsilon_LWIR >= 0.90 across 8-13 um as this folio's own design targets under I_solar = 1000 W/m^2; report P_net and Delta T as model values, never as measured results.
3. Compute Stefan phase-change melting front depth s(t) = 2 * lambda_s * sqrt(alpha_th * t) where lambda_s * exp(lambda_s^2) * erf(lambda_s) = Ste / sqrt(pi).

## How it works, in four stages
- Stage 1 (Solar Reflection, 0.3–2.5 μm): In the model the roof reflects 97.0% of an assumed 1,000 W/m² of midday sunlight, so it absorbs (1 − 0.97) × 1,000 = 30 W/m².
- Stage 2 (Emission in the 8–13 μm Window): The model assigns the roof a net radiative exchange with the sky of 116.4 W/m² at air temperature (emission minus absorbed atmospheric radiation). This is a fixed illustrative value, not a measurement.
- Stage 3 (Sub-Ambient Equilibrium Below Air Temperature): Net cooling power P_net = 116.4 − 30 = +86.4 W/m². Divided by an assumed combined heat-exchange coefficient of about 13.9 W/(m²·K), that gives a roof surface about 6.2 °C below outdoor air in the model.
- Stage 4 (Stefan Phase-Change Thermal Ceiling Buffer): A proposed 21 °C PCM ceiling panel would absorb indoor heat along a moving melting front s(t) = 2λ_s√(α t). The panel is a design proposal and was not sized or tested here.

## Reference values stated in the essay
- **Absorbed Solar Flux (P_sun)**: `30.0 W/m² (R_sol = 97.0%)`
- **Net Sky Cooling Power (P_net, Model)**: `+86.4 W/m² (Noon Sun, Model)`
- **Sub-Ambient Temp Drop (ΔT_sub, Model)**: `−6.2 °C Below Ambient (Model)`
- **Model Check**: `NET COOLING IN MODEL (P_net > 0)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1038/nature13883 (Scite report: https://scite.ai/reports/10.1038/nature13883)
- What the essay compares against: Model values: R_solar = 97.0% · ε_LWIR = 95.0% · P_net = +86.4 W/m² (−6.2 °C)

## Recent research context
- **How a Roof Can Radiate Building Heat Through the 8–13 μm Sky Window in Daylight: A Design Model**: Raman, Anoma, Zhu, Rephaeli & Fan measured a surface 4.9 °C below air temperature in direct sunlight (Nature, DOI 10.1038/nature13883), and Mandal et al. reported a porous polymer coating with similar behavior (Science, DOI 10.1126/science.aat9513). This folio models a roof with 97% solar reflectance and 95% sky-window emissivity: 86.4 W/m² of midday cooling in the model, paired with a proposed PCM ceiling. Model values, not measurements.
