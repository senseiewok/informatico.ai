---
name: 3dcp-roussel-thixotropy-buildability
description: AI-agnostic additive civil engineering skill for 3D Concrete Printing (3DCP) Roussel thixotropic structuration (tau_0(t) = tau_00 + A_thix * t), plastic yield collapse, and Suiker elastic wall buckling.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# 3D Concrete Printing (3DCP) Extrusion Rheology & Buildability: Roussel Thixotropic Structuration, Elastic Buckling vs. Plastic Collapse & Robotic Toolpath Control (Folio E.10)

A plain-text companion to the essay at https://informatico.ai/engineering/e10/ (`E.10 · 3D Concrete Printing Rheology & Buildability`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`τ_0(t) = τ_{0,0} + A_thix t · H_plast = √3 τ_0(t)/(ρg) (von Mises)`

## Rules the essay derives
1. Evaluate static yield stress evolution tau_0(t) = tau_00 + A_thix * t and require A_thix > (rho * g * v_build) / sqrt(3) to prevent bottom-layer plastic collapse.
2. Remember that self-weight elastic buckling (Suiker 2018) also limits wall height; this folio does not compute it, so its H_crit is the plastic-collapse height H_plast only.
3. Verify interlayer cycle time t_cycle = L_perim / v_nozzle stays below open time t_open to prevent interfacial cold joints.

## How it works, in four stages
- Stage 1 (Nozzle Shear Rejuvenation, Continuing E.02): High shear inside the robotic printhead breaks colloidal links; this folio takes an illustrative initial yield stress τ_{0,0} = 420 Pa at deposition.
- Stage 2 (Roussel Linear Thixotropic Structuration): At rest, flocculation and early hydration rebuild static yield stress, modelled as τ_0(t) = τ_{0,0} + A_thix t (A_thix = 0.85 Pa/s). The linear law is a short-time approximation; over longer times strength can grow faster than linearly.
- Stage 3 (Plastic Yield vs. Suiker Buckling): The bottom layer must resist gravity shear τ_b = ρ g H / √3 (the von Mises criterion). With ρ = 2,200 kg/m³ (assumed) and v_build = 1.6 m/hr, gravity shear grows at 5.5 Pa/s against A_thix = 0.85 Pa/s, so in this model the base yields at H ≈ 0.04 m. Self-weight elastic buckling (Suiker 2018) also limits wall height; it is not computed on this page.
- Stage 4 (Corrugated Funicular Toolpath, Continuing A.01): Corrugating the toolpath raises the wall's second moment of area and so its buckling resistance; this folio does not compute by how much, or how much cement it saves.

## Reference values stated in the essay
- **Plastic Collapse Height (model, defaults)**: `H ≈ 0.04 m (ρ = 2,200 kg/m³ assumed)`
- **Structuration vs. Gravity Shear Rate**: `A_thix 0.85 < ρgv/√3 ≈ 5.5 Pa/s`
- **Governing Failure Mode (model)**: `PLASTIC YIELD (buckling not computed)`
- **Model Buildability Status**: `NOT BUILDABLE AT THESE SETTINGS (model)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/j.cemconres.2018.04.005 (Scite report: https://scite.ai/reports/10.1016/j.cemconres.2018.04.005)
- What the essay compares against: Model, ρ = 2,200 kg/m³ assumed: A_thix = 0.85 Pa/s < ρ g v_build/√3 = 5.5 Pa/s at v_build = 1.6 m/hr ⇒ base yields at H ≈ 0.04 m

## Recent research context
- **Roussel Thixotropic Structuration vs. Self-Weight: A Simple Model of Formwork-Free 3D Concrete Printing**: Picking up from Folio E.02's Herschel–Bulkley slickline pumping and Folio A.01's funicular shells, this folio uses Nicolas Roussel's printability criterion (Cem. Concr. Res. DOI 10.1016/j.cemconres.2018.04.005) and Suiker's buckling analysis to show how yield build-up A_thix must outpace self-weight. At its default values the simple model predicts early plastic collapse.
