---
name: herschel-bulkley-yield-rheology
description: AI-agnostic civil and non-Newtonian fluid mechanics skill for Herschel-Bulkley and Bingham concrete pumping rheology, plug-flow radius r_p/R = tau_0/tau_w, and thixotropic dispersion.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Herschel–Bulkley Yield-Stress Rheology: High-Performance Concrete Pumping & Tremie Placement (Folio E.02)

A plain-text companion to the essay at https://informatico.ai/engineering/e02/ (`E.02 · Concrete Yield Rheology · CSI 03 30 00`, `REV 1.4`, redated `2026-11-14`).

## The governing relation
`τ = τ_0 + K γ̇^n · r_p / R = τ_0 / τ_w · ΔP/L = 2τ_w/R`

## Rules the essay derives
1. Check slickline yield mobilization: pumping requires wall shear stress tau_w = (DeltaP * R)/(2L) > tau_0 (plug ratio r_p / R = tau_0 / tau_w < 1).
2. Evaluate Buckingham-Reiner volumetric flow multiplier Q / Q_Newtonian = 1 - (4/3)*(tau_0/tau_w) + (1/3)*(tau_0/tau_w)^4 for Bingham plastics.
3. Account for shear-thinning power-law index n < 1 in the sheared annulus, and state that real pumped concrete also forms a paste-rich lubrication layer at the wall that a homogeneous model leaves out.

## How it works, in four stages
- Stage 1 (Unmobilized Solid Arrest, τ_w ≤ τ_0): When wall shear stress falls below yield stress τ_0, the concrete locks into zero-flow solid arrest.
- Stage 2 (Central Unsheared Plug Core, r ≤ r_p): For τ_w > τ_0, an unsheared solid plug of radius r_p/R = τ_0/τ_w translates along the pipe center.
- Stage 3 (Annular Shear-Thinning Layer): Shear is confined to the annulus r_p < r ≤ R. The page uses a power-law index n = 0.65 and consistency K = 8.5 Pa·sⁿ, fixed illustrative values rather than measured ones.
- Stage 4 (Polycarboxylate Dispersion): PCE superplasticizers disperse cement grains and lower the yield stress; how much depends on the mix and dose, and the page does not model a specific reduction.

## Reference values stated in the essay
- **Wall Shear Stress**: `75.0 Pa`
- **Plug Core Radius Ratio**: `37.3% (23.3 mm)`
- **Discharge Output**: `6.6 m³/hr (8.6 yd³/hr) · model, K = 8.5 Pa·sⁿ, n = 0.65`
- **Pumping State**: `MOBILIZED IN THE MODEL (τ_w > τ_0)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/j.cemconcomp.2015.11.002 (Scite report: https://scite.ai/reports/10.1016/j.cemconcomp.2015.11.002)
- What the essay compares against: Model values: 125 mm pipe · τ_w = 75.0 Pa and r_p/R = 37.3% at defaults

## Recent research context
- **The Paste Layer at the Pipe Wall Shapes Concrete Pumping Pressure**: The Bingham (1922) and Herschel–Bulkley (1926) laws treat concrete as a uniform yield-stress fluid. Pumping research adds a lubrication layer of cement paste that forms at the pipe wall: Feys, Khayat & Khatib (Cement and Concrete Composites, 2016, DOI 10.1016/j.cemconcomp.2015.11.002) examined how rheology, tribology, flow rate and pipe radius influence pumping pressure, and De Schutter & Feys (2016, DOI 10.21809/rilemtechlett.2016.15) reviewed how that layer forms.
