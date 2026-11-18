---
name: reciprocal-timber-nexorade
description: AI-agnostic structural timber engineering skill for reciprocal gridshells (nexorades), engagement ratio kinematics, and Eurocode 5 notched lap joint verification.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Reciprocal Timber Gridshells (Nexorades), Eccentric Lap Moments, and 1:5 Shear-Block Joinery (Folio A.02)

A plain-text companion to the essay at https://informatico.ai/architecture/a02/ (`A.02 · Reciprocal Timber Gridshells`, `REV 1.3`, redated `2026-11-14`).

## The governing relation
`M_lap = V_lap a (1 − λ) · τ_d ≤ k_v f_{v,d}`

## Rules the essay derives
1. Compute reciprocal lap bending moment M_lap = V_lap * a * (1 - lambda_lap) for engagement ratio lambda_lap = a / L.
2. Verify Eurocode 5 notched joint shear utilization tau_d / (k_v * f_{v,d}) <= 1.0 using effective depth h_eff.
3. Provide full-thread self-tapping screw reinforcement perpendicular to grain where tension splitting stress exceeds f_{t,90,d}.

## How it works, in four stages
- Stage 1 (4-Valence Reciprocal Fan): Four GL28h larch members interlock in a pinwheel cyclic dependency so no more than two members meet at any single point.
- Stage 2 (Eccentricity-Induced Dome Rise): An assumed vertical offset e_z = 85 mm at each lap joint tilts each member, and repeated around the fan this gives the dome its rise.
- Stage 3 (Notch Shear & Bending Check, in the style of EN 1995-1-1): With V_lap = 18.4 kN, λ = 0.25 and an assumed member length L = 1.493 m (so a = λL = 0.373 m), M_lap = 18.4 × 0.373 × 0.75 = 5.15 kN·m. The notch utilization 0.64 is a fixed illustrative value, not a full design check.
- Stage 4 (1:5 CNC Dovetail Shear-Block Node): A proposed node in which hardwood beech dowels and EPDM gaskets carry shear without exposed steel plates (design proposal, not tested).

## Reference values stated in the essay
- **Joint Shear Force (V_lap)**: `18.4 kN`
- **Induced Bending Moment (Model)**: `5.15 kN·m`
- **Notch Utilization (Illustrative)**: `0.64 ≤ 1.00 (model)`
- **Buckling Factor (Illustrative)**: `SF = 3.74 (model value)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/j.jobe.2019.100867 (Scite report: https://scite.ai/reports/10.1016/j.jobe.2019.100867)
- What the essay compares against: Model values: M_lap = 5.15 kN·m (a = 0.373 m, λ = 0.25) · utilization 0.64 and SF 3.74 are illustrative

## Recent research context
- **Reciprocal Timber Gridshells: Short Members, Mutual Support, and the Bending at Every Notch**: Building on Villard de Honnecourt's medieval floor frames and Olga Popovic Larsen's Reciprocal Frame Architecture (DOI 10.4324/9780080556000; Asefi & Bahremandi-Tolou, J. Build. Eng. 2019, DOI 10.1016/j.jobe.2019.100867), this folio models a GL28h larch nexorade with an assumed eccentricity e_z = 85 mm, a lap moment of 5.15 kN·m, and illustrative values for notch utilization (0.64) and buckling (SF = 3.74).
