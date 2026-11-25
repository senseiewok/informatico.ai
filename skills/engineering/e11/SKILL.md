---
name: simp-topology-inerter-damping
description: Explanatory companion on Bendsøe-Sigmund SIMP optimization, Sigmund (2001) sensitivity filtering, Lazarov-Sigmund (2011) Helmholtz PDE density filtering, Michell trusses, and Smith (2002) inerters. Explanation, not a design method; none of its numbers apply to real structures.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Continuum Topology Optimization & Skyscraper Inerter Damping: SIMP Penalization, Michell Funicular Trusses & Trabecular Bone Mechanics (Folio E.11)

A plain-text companion to the essay at https://informatico.ai/engineering/e11/ (`E.11 · SIMP Topology Optimization & Inerter Damping · CSI 03 41 00`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`min_ρ c(ρ) = Uᵀ K(ρ) U · E_e(ρ_e) = E_min + ρ_e^p (E_0 − E_min) · F_inerter = b (ü_2 − ü_1)`

## Rules the essay derives
1. Explanation, not a design method: none of these assumed numbers (V/V_0 = 0.35, c/c_0 approx 2.9x, -65%, r_min = 45 mm, r approx 13.0 mm, r_fly = 45 mm, P = 20 mm, b approx 200 * m_fly, mu_b = 0.18) may be used on a real structure.
2. Separate SIMP E_e(rho_e) = E_min + rho_e^p * (E_0 - E_min) and Sigmund (2001, DOI 10.1007/s001580050176) cone sensitivity filtering (radius r_min) from Lazarov & Sigmund (2011, DOI 10.1002/nme.3072) PDE density filtering -r^2 * laplacian(rho_tilde) + rho_tilde = rho with r = r_min / (2*sqrt(3)).
3. Separate slider heuristics (1 / max(0.05, V/V_0) and -(1 - V/V_0)) from fixed-text readouts (thin-ring b = m_fly * (2*pi*r/P)^2 = 199.86 * m_fly vs solid disk approx 100 * m_fly; mu_b updates its label and schematic overlay, driving zero numerical readouts).

## How it works, in four stages
- Stage 1 (Stress Trajectories): A continuum finite-element model (FEniCS/dolfinx is one open-source option; none was run here) maps principal stress paths σ_1, σ_2.
- Stage 2 (SIMP & Filtering): E_e(ρ_e) = E_min + ρ_e^p (E_0 − E_min) with assumed p = 3 (Bendsøe 1989; Sigmund 2001 cone filter radius r_min) pairs with the Lazarov & Sigmund (2011, DOI 10.1002/nme.3072) Helmholtz PDE density filter −r² ∇²ρ̃ + ρ̃ = ρ (with PDE length r = r_min / (2√3)).
- Stage 3 (Slider Heuristic): Idealized point-load layouts recall Michell (1904) nets. At V/V_0 = 0.35, Readout 1 computes 1 / max(0.05, V/V_0) ≈ 2.9× and Readout 2 computes −65% slab-zone volume; not for real structures.
- Stage 4 (Flywheel Inerter): Smith's F = b(ü_2 − ü_1) with an assumed thin rim (I = m_fly r²) gives b = m_fly (2π r / P)² = 199.86 m_fly ≈ 200× at r = 45 mm, P = 20 mm (solid disk ≈ 100×); Lazar, Neild & Wagg (2014) studied inerters for building vibration. Readouts 3–4 remain fixed text.

## Reference values stated in the essay
- **Compliance Ratio (rough scaling, c / c_0)**: `≈ 2.9× (c ∝ 1/(V/V_0), illustrative)`
- **Slab Concrete Volume Reduction**: `−65% (1 − V/V_0; CO2e assumed proportional)`
- **Inerter Apparent Mass Gain**: `≈ 200× thin-ring mass (r = 45 mm, P = 20 mm; fixed text)`
- **Model Filter & Boundary Status**: `EXPLANATORY MODEL · NOT A DESIGN METHOD (fixed text)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1007/s001580050176 (Scite report: https://scite.ai/reports/10.1007/s001580050176)
- What the essay compares against: V/V_0 = 0.35 · p = 3.0 ⇒ 65% less slab-zone volume · μ_b = 0.18 (readouts 3–4 fixed text)

## Recent research context
- **Explanatory Model: SIMP Topology Optimization, PDE Filtering, and Flywheel Inerters for Lighter Floor Slabs**: This folio explains how Bendsøe–Sigmund SIMP optimization (Sigmund 2001, DOI 10.1007/s001580050176), Lazarov–Sigmund Helmholtz PDE filtering (2011, DOI 10.1002/nme.3072), printable-concrete rheology (Roussel 2018, DOI 10.1016/j.cemconres.2018.04.005), and Smith's inerter (DOI 10.1109/TAC.2002.803532) frame slab mass versus wind sway. All numbers are illustrative and not for real structures.
