---
name: hygroscopic-timber-timoshenko-bilayer
description: AI-agnostic architectural and timber-engineering skill for Stephen Timoshenko bilayer curvature, orthotropic wood moisture swelling (alpha_T vs alpha_L), and zero-energy responsive building skins.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Bending-Active & Hygroscopic Programmable Timber Skins: Timoshenko Bilayer Curvature, Orthotropic Moisture Swelling & Zero-Energy Climate Facades (Folio A.09)

A plain-text companion to the essay at https://informatico.ai/architecture/a09/ (`A.09 · Hygroscopic Timber Skins & Timoshenko Curvature · CSI 06 18 00`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`κ = 6(1+m)² Δα ΔMC / [h (3(1+m)² + (1+mn)(m² + 1/mn))] · EN 1995-1-1 · CSI 06 18 00`

## Rules the essay derives
1. Compute differential hygroscopic strain Delta_epsilon = (alpha_T - alpha_L) * Delta_MC below the Fiber Saturation Point (MC <= 28%).
2. Evaluate Timoshenko curvature kappa = 6 * (1 + m)^2 * Delta_epsilon / (h * (3 * (1 + m)^2 + (1 + m*n) * (m^2 + 1/(m*n)))) with m = h_1/h_2 and n = E_1/E_2.
3. Calculate cantilever aperture tip deflection delta_tip = (1 - cos(kappa * L)) / kappa approx 0.5 * kappa * L^2, state the m and n used, and check rolling shear against the timber code that applies; report results as model values.

## How it works, in four stages
- Stage 1 (Orthotropic Cell-Wall Sorption, Continuing E.04): Below fiber saturation (about 28% MC), the model assumes beech swells tangentially at α_T = 0.32%/%MC and along the grain at only α_L = 0.012%/%MC. Both coefficients are assumed round values.
- Stage 2 (Timoshenko Bilayer Formula, DOI 10.1364/JOSA.11.000233): Bonding an active tangential ply h_2 to a passive longitudinal ply h_1 turns the misfit strain Δε = (α_T − α_L)ΔMC = 0.0185 into curvature. With the folio's assumed m = h_1/h_2 = 2 and n = E_1/E_2 = 10.6 the geometry factor is 0.46 and κ = 1.42 m⁻¹. Equal plies of equal stiffness (m = n = 1) would give 4.62 m⁻¹.
- Stage 3 (Weather-Responsive Facade Petal, Model): A 425 mm cantilever petal moves δ_tip ≈ ½ κ L² = 128 mm at the tip as it dries. The 64.5% free vent area is a fixed illustrative value, not computed from the geometry. Rain-tightness was not assessed.
- Stage 4 (Self-Shaping CLT, Continuing A.02): Wood et al. (2020) describe curved cross-laminated timber components for the Urbach Tower that took their shape during drying instead of being milled or pressed to a curve.

## Reference values stated in the essay
- **Timoshenko Curvature (κ, Model)**: `1.42 m⁻¹ (R = 0.70 m)`
- **Petal Tip Deflection (δ_tip, Model)**: `128.2 mm (at L = 425 mm)`
- **Vent Opening (Illustrative)**: `64.5% Free Area (Illustrative)`
- **Model Check**: `ACTUATION WITHOUT MOTORS (MODEL)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1364/JOSA.11.000233 (Scite report: https://scite.ai/reports/10.1364/JOSA.11.000233)
- What the essay compares against: Model values: ΔMC = +6.0% · h = 6.0 mm · m = 2 · n = 10.6 ⇒ κ = 1.42 m⁻¹ · δ_tip = 128 mm

## Recent research context
- **Stephen Timoshenko's 1925 Bilayer Theorem & Cross-Grained Beech Skins Power Zero-Energy Climate Facades**: Completing the mass-timber and psychrometric threads of Folios A.02, E.04, and A.08, this folio applies Stephen Timoshenko's bilayer curvature formula (JOSA DOI 10.1364/JOSA.11.000233) to a wood bilayer whose plies swell very differently with moisture (about 27:1 with the assumed coefficients), the principle behind the meteorosensitive skins described by Reichert, Menges & Correa (DOI 10.1016/j.cad.2014.02.010). Model values, not measurements.
