---
name: netzero-water-pathogen-plumbing
description: AI-agnostic architectural hydro-engineering skill for Kadlec-Knight subsurface constructed wetlands and biofilm-control clinical plumbing design targets.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Net-Zero Water & Greywater Constructed Wetlands: Subsurface Darcy Filtration, UV-C Photolysis, and Pathogen-Control Plumbing (CSI 22 13 00) (Folio A.06)

A plain-text companion to the essay at https://informatico.ai/architecture/a06/ (`A.06 · Hydro-Tectonics · CSI 22 13 00`, `REV 1.2`, redated `2026-11-14`).

## The governing relation
`C_out = C* + (C_in−C*)e^(−kτ) · 5.4-Log UV-C`

## Rules the essay derives
1. Size subsurface horizontal-flow wetlands via Darcy's law Q = K_s A_c S and Kadlec-Knight kinetics C_out = C* + (C_in - C*) exp(-k_v * tau).
2. Maintain potable hot-water recirculation >= 60 C at velocity >= 0.6 m/s with zero dead-legs > 1.5 pipe diameters.
3. Apply the folio's design targets of a 4-log model reduction (254 nm UV-C fluence H >= 34 mJ/cm^2 at 0.12 log per mJ/cm^2) and non-splashing offset drains; report log reductions as model values, never as measured outcomes.

## How it works, in four stages
- Stage 1 (Subsurface Horizontal Darcy Filtration): Greywater flows 150 mm beneath dry washed basalt gravel (φ = 0.38, K_s = 120 m/d) with no open water surface.
- Stage 2 (Rhizosphere Biofilm Oxidation): Phragmites root-zone oxygen transfer drives Kadlec-Knight exponential BOD_5 decay from 140 mg/L to 6.8 mg/L (τ = 3.2 d) in the folio model.
- Stage 3 (Dead-Leg-Free 60 °C Potable Recirculation): Copper-silver / stainless manifold designed to target v ≥ 0.6 m/s and T ≥ 60 °C up to every point-of-use mixing valve (design target, not measured).
- Stage 4 (254 nm UV-C Photolysis & Thermal Trap Purge): Delivers H = 45 mJ/cm² UV-C fluence (a 5.4-log reduction in the folio's Chick-Watson model) plus self-heating sink traps.

## Reference values stated in the essay
- **Wetland BOD_5 Reduction**: `95.1% (140 → 6.8 mg/L)`
- **UV-C Log Reduction (Model)**: `5.4-Log (45 mJ/cm²)`
- **Thermal Loop Design Target**: `60.0 °C (v = 0.65 m/s)`
- **Design Check (Model)**: `DESIGN TARGETS MET (MODEL)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1201/9781420012514 (Scite report: https://scite.ai/reports/10.1201/9781420012514)
- What the essay compares against: Model values: 95.1% BOD_5 removal · 5.4-log UV-C design dose

## Recent research context
- **Sink Drains as Bacterial Reservoirs: What Thermal Recirculation and UV-C Are Designed to Limit**: Kotay et al. (2017, DOI 10.1128/AEM.03327-16) used a fluorescent marker organism to model bacterial dispersion from hand-washing sink traps. This folio pairs an external Kadlec–Knight greywater wetland with an internal 45 mJ/cm² UV-C and 60 °C recirculation loop as a design response; the 5.4-log figure is a model value, not a measured result.
