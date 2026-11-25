---
name: hygroscopic-timber-timoshenko-bilayer
description: Explanatory companion adapting Stephen Timoshenko bilayer curvature (1925) to assumed wood moisture swelling. Explanation only, not a design method; none of its numbers may be used on a real structure.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Bending-Active & Hygroscopic Programmable Timber Skins: Timoshenko Bilayer Curvature, Orthotropic Moisture Swelling & Zero-Energy Climate Facades (Folio A.09)

A plain-text companion to the essay at https://informatico.ai/architecture/a09/ (`A.09 · Hygroscopic Timber Skins & Timoshenko Curvature · CSI 06 18 00`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`κ = 6(1+m)² Δα ΔMC / [h (3(1+m)² + (1+mn)(m² + 1/mn))] · EN 1995-1-1 · CSI 06 18 00`

## Rules the essay derives
1. Explanation only, not a design method: none of this folio's assumed numbers (alpha_T = 0.0032/%MC, alpha_L = 0.00012/%MC, m = 2, n = 10.6, kappa = 1.42 m^-1, 128.2 or 128.6 mm, 64.5%) may be used on a real structure.
2. Adapt Timoshenko (1925, DOI 10.1364/JOSA.11.000233) with passive longitudinal restraint ply 1 (h_1, E_1) and active tangential ply 2 (h_2, E_2), computing Delta_epsilon = (alpha_T - alpha_L) * Delta_MC below fiber saturation with assumed m = h_1/h_2 and n = E_1/E_2.
3. Separate unrounded kappa = 1.4234 m^-1 (128.6 mm parabolic, 124.7 mm arc at L = 425 mm) from the page slider (1.42 m^-1 giving 128.2 mm with 240 mm cap, vent 64.5% * (kappa/1.42) in [12%, 92%], label switch below 0.45 m^-1).

## How it works, in four stages
- Stage 1 (Orthotropic Cell-Wall Sorption): Below fiber saturation (assumed ~28% MC), this model assumes European beech swells tangentially at α_T = 0.0032 per %MC (0.32%/%MC) and longitudinally at α_L = 0.00012 per %MC (0.012%/%MC); both are assumed round constants.
- Stage 2 (Timoshenko Adaptation, DOI 10.1364/JOSA.11.000233): Bonding passive longitudinal restraint ply 1 (h_1, E_1) to active tangential ply 2 (h_2, E_2) with Δε = (α_T − α_L)ΔMC = 0.01848 and assumed m = h_1/h_2 = 2, n = E_1/E_2 = 10.6 gives f = 0.4621 and κ = 1.4234 m⁻¹ (1.42 m⁻¹ rounded; m = n = 1 gives 4.62 m⁻¹).
- Stage 3 (Slider Heuristic & Boundary): At L = 425 mm, unrounded κ = 1.4234 m⁻¹ gives ½ κ L² = 128.6 mm (124.7 mm arc), while the page slider scales from 1.42 m⁻¹ to 128.2 mm (240 mm cap) and scales vent area in [12%, 92%]. Not for real structures.
- Stage 4 (Self-Shaping Mass Timber): Grönquist et al. (2019, DOI 10.1126/sciadv.aax1311) modeled self-shaping wood bilayers for curved mass timber, applied in Urbach Tower components (Wood et al. 2020).

## Reference values stated in the essay
- **Timoshenko Curvature (κ, Model)**: `1.42 m⁻¹ (R = 0.70 m)`
- **Petal Tip Deflection (δ_tip, Model)**: `128.2 mm (at L = 425 mm)`
- **Vent Opening (Illustrative)**: `64.5% Free Area (Illustrative)`
- **Model Check**: `ACTUATION WITHOUT MOTORS (MODEL)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1364/JOSA.11.000233 (Scite report: https://scite.ai/reports/10.1364/JOSA.11.000233)
- What the essay compares against: Model values: ΔMC = +6.0% · h = 6.0 mm · m = 2 · n = 10.6 ⇒ κ = 1.42 m⁻¹ · δ_tip = 128.2 mm (slider) / 128.6 mm (unrounded ½ κ L²)

## Recent research context
- **Explanatory Model: Timoshenko's 1925 Strip Formula & Hygroscopic Wood Bilayers**: Adapting Timoshenko (1925, DOI 10.1364/JOSA.11.000233) with assumed 27:1 wood swelling anisotropy alongside Reichert et al. (2015, DOI 10.1016/j.cad.2014.02.010), Grönquist et al. (2019, DOI 10.1126/sciadv.aax1311), and Peng et al. (2023, DOI 10.1186/s10086-023-02105-1). Explanation only, not a design method; no figure may be used on a real structure.
