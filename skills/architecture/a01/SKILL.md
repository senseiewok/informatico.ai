---
name: tectonic-funicular-envelope
description: AI-agnostic architectural and structural engineering skill for funicular vault graphic statics (Heyman Safe Theorem |e| <= t/6) and 1:5 ISO 10211 thermal-break detailing.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Funicular Thrust Surfaces, Maxwell–Cremona Duals, and 1:5 Nodal Tectonics (Folio A.01)

A plain-text companion to the essay at https://informatico.ai/architecture/a01/ (`A.01 · Vaults & Thermal Nodes`, `REV 1.3`, redated `2026-11-02`).

## The governing relation
`H = qL² / (8f) · |e| ≤ t/6`

## Rules the essay derives
1. Horizontal Thrust: H = q * L^2 / (8 * f) under uniform line load q across span L and rise f.
2. Heyman Safe Theorem: Verify thrust-line eccentricity |e| <= t / 6 (middle-third kern) and safety factor SF = t / (2 * |e|) >= 1.0.
3. 1:5 Springer Thermal Node (ISO 10211 & EN ISO 13788): Verify T_si > T_dew and temperature factor f_Rsi = (T_si - T_e) / (T_i - T_e) >= 0.70.

## How it works, in four stages
- Stage 1 (Dead-Load Catenary): Under self-weight alone, the inverted catenary thrust line passes through the centroidal axis (e = 0 mm, SF = 9.38).
- Stage 2 (Asymmetric Haunch Load): Live load at the quarter-span shifts the funicular thrust line toward the extrados at the loaded haunch.
- Stage 3 (Maxwell-Cremona Reciprocal Dual): Horizontal ray H = qL²/(8f) = 216.0 kN and vertical reaction V = 216.0 kN close the force polygon.
- Stage 4 (1:5 Springer Node A-04): UHPC structural thermal break (λ = 0.19 W/(m·K)) keeps interior surface T_si = 16.4 °C above dew point T_dew = 9.3 °C.

## Reference values stated in the essay
- **Horizontal Thrust (H)**: `216.0 kN`
- **Eccentricity vs Middle-Third**: `32 / 100 mm`
- **Heyman Safe Theorem Verdict**: `SAFE KERN (SF 9.38)`
- **ISO 10211 Thermal Node**: `T_si = 16.4 °C > T_dew (PASS)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1017/CBO9781107050310 (Scite report: https://scite.ai/reports/10.1017/CBO9781107050310)
- What the essay compares against: Heyman Safe Theorem (|e| ≤ t/6)

## Recent research context
- **3D Graphic Statics & Thrust Network Analysis Extend Heyman's Safe Theorem to Freeform Vaults**: Jacques Heyman's limit-state masonry theorem (DOI 10.1017/CBO9781107050310) and Block's Thrust Network Analysis (TNA) enable ultra-thin unreinforced stone and tile vaults with 70% lower embodied carbon, while the same reciprocal force-polygon equilibrium models structural stability across transmembrane helices in PDB 8EIQ.
