---
name: tectonic-funicular-envelope
description: AI-agnostic architectural and structural engineering skill for funicular vault graphic statics (middle-third rule |e| <= t/6 as a design target) and a 1:5 thermal-break node check.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Funicular Thrust Surfaces, Maxwell–Cremona Duals, and 1:5 Nodal Tectonics (Folio A.01)

A plain-text companion to the essay at https://informatico.ai/architecture/a01/ (`A.01 · Vaults & Thermal Nodes`, `REV 1.4`, redated `2026-11-14`).

## The governing relation
`H = qL² / (8f) · |e| ≤ t/6`

## Rules the essay derives
1. Horizontal Thrust: H = q * L^2 / (8 * f) under uniform line load q across span L and rise f.
2. Thrust-line check: compute the geometric factor SF = t / (2 * |e|). SF >= 3 means the thrust line is inside the middle third (|e| <= t / 6); SF = 1 means it has reached the edge, where a hinge can form. Report this as a model result, not as proof of safety.
3. 1:5 Springer Thermal Node: check T_si > T_dew and the temperature factor f_Rsi = (T_si - T_e) / (T_i - T_e) defined in ISO 13788. The target f_Rsi >= 0.70 is this folio's own choice, not a requirement of the standard; state T_i, T_e and humidity with every result.

## How it works, in four stages
- Stage 1 (Dead-Load Catenary): Under self-weight, the inverted catenary thrust line follows the center line of the vault (e = 0 mm).
- Stage 2 (Asymmetric Haunch Load): Live load at the quarter-span shifts the funicular thrust line toward the extrados at the loaded haunch; at the default e = 32 mm the geometric factor is t/(2|e|) = 600/64 = 9.38.
- Stage 3 (Maxwell-Cremona Reciprocal Dual): With q = 24 kN/m, L = 18 m and f = 4.5 m, the horizontal ray H = qL²/(8f) = 216.0 kN and the vertical reaction V = qL/2 = 216.0 kN close the force polygon.
- Stage 4 (1:5 Springer Node A-04): A load-bearing thermal break with an assumed λ = 0.19 W/(m·K) is modeled as keeping the interior surface at T_si = 16.4 °C, above the dew point T_dew = 9.3 °C of air at 20 °C and 50% RH. T_si is a fixed illustrative value, not a calculated or measured one.

## Reference values stated in the essay
- **Horizontal Thrust (H)**: `216.0 kN`
- **Eccentricity vs Middle-Third**: `32 / 100 mm`
- **Middle-Third Check (Model)**: `INSIDE MIDDLE THIRD (SF 9.38)`
- **Thermal Node (Illustrative)**: `T_si = 16.4 °C > T_dew = 9.3 °C`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1017/CBO9781107050310 (Scite report: https://scite.ai/reports/10.1017/CBO9781107050310)
- What the essay compares against: Model: middle-third rule |e| ≤ t/6 (geometric factor ≥ 3)

## Recent research context
- **3D Graphic Statics & Thrust Network Analysis Extend Heyman's Safe Theorem to Freeform Vaults**: Jacques Heyman's safe theorem for masonry (DOI 10.1017/CBO9781107050310) says a vault stands if a thrust line can be found inside the stone. Three-dimensional graphic statics (Akbarzadeh, Van Mele and Block 2015, DOI 10.1016/j.cad.2015.01.006) extends the form-and-force diagrams of the nineteenth century to freeform shells. This folio shows the two-dimensional version as a teaching model.
