---
name: reciprocal-timber-nexorade
description: AI-agnostic structural timber engineering skill for reciprocal gridshells (nexorades), engagement ratio kinematics, and Eurocode 5 notched lap joint verification.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Reciprocal Timber Gridshells (Nexorades), Eccentric Lap Moments, and 1:5 Shear-Block Joinery (Folio A.02)

A plain-text companion to the essay at https://informatico.ai/architecture/a02/ (`A.02 · Reciprocal Timber Gridshells`, `REV 1.2`, redated `2026-11-02`).

## The governing relation
`M_lap = V_lap a (1 − λ) · τ_d ≤ k_v f_{v,d}`

## Rules the essay derives
1. Compute reciprocal lap bending moment M_lap = V_lap * a * (1 - lambda_lap) for engagement ratio lambda_lap = a / L.
2. Verify Eurocode 5 notched joint shear utilization tau_d / (k_v * f_{v,d}) <= 1.0 using effective depth h_eff.
3. Provide full-thread self-tapping screw reinforcement perpendicular to grain where tension splitting stress exceeds f_{t,90,d}.

## How it works, in four stages
- Stage 1 (4-Valence Reciprocal Fan): Four GL28h larch members interlock in a pinwheel cyclic dependency so no more than two members meet at any single point.
- Stage 2 (Eccentricity-Induced Dome Rise): Vertical offset e_z = 85 mm at each lap joint automatically generates the Gaussian synclastic curvature of the dome.
- Stage 3 (Eurocode 5 Notch Shear & Bending Check): Evaluates bending stress σ_m = 6 M_y / (b h_eff²) and reduced notch shear τ_d ≤ k_v f_{v,d}.
- Stage 4 (1:5 CNC Dovetail Shear-Block Node): Hardwood beech dowels and EPDM acoustic gaskets transfer shear without exposed steel plates.

## Reference values stated in the essay
- **Joint Shear Force (V_lap)**: `18.4 kN`
- **Induced Bending Moment**: `5.15 kN·m`
- **Eurocode 5 Utilization**: `0.64 ≤ 1.00 (SAFE)`
- **Gridshell Buckling Verdict**: `SF = 3.74 · EN 1995-1-1 PASS`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/j.jobe.2019.100867 (Scite report: https://scite.ai/reports/10.1016/j.jobe.2019.100867)
- What the essay compares against: Eurocode 5 (EN 1995-1-1) Combined Bending & Shear

## Recent research context
- **5-Axis CNC Reciprocal Timber Gridshells & Beechwood Shear Keys Span 4x-6x Single-Billet Length**: Extending Villard de Honnecourt's medieval floor frames and Olga Popovic Larsen's Reciprocal Frame Architecture (DOI 10.4324/9780080556000; Asefi & Bahremandi-Tolou, J. Build. Eng. 2019, DOI 10.1016/j.jobe.2019.100867), modern 5-axis CNC GL28h larch nexorades use engagement eccentricity e_z = 85 mm and Eurocode 5 notch verification (utilization 0.64 <= 1.00, buckling SF = 3.74) to build column-free timber shells—mirroring the reciprocal NBD1-NBD2 dimer interlock in rescued F508del-CFTR (PDB 8EIQ).
