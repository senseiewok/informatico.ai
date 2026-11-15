---
name: simp-topology-inerter-damping
description: AI-agnostic structural engineering skill for Bendsøe-Sigmund SIMP continuum topology optimization, Helmholtz PDE sensitivity filtering, Michell funicular trusses, and tuned inerter dampers.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Continuum Topology Optimization & Skyscraper Inerter Damping: SIMP Penalization, Michell Funicular Trusses & Trabecular Bone Mechanics (Folio E.11)

A plain-text companion to the essay at https://informatico.ai/engineering/e11/ (`E.11 · SIMP Topology Optimization & Inerter Damping · Eurocode 2 / ACI 318`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`min_ρ c(ρ) = Uᵀ K(ρ) U · E_e(ρ_e) = E_min + ρ_e^p (E_0 − E_min) · F_inerter = b (ü_2 − ü_1)`

## Rules the essay derives
1. Penalize intermediate element densities via SIMP law E_e(rho_e) = E_min + rho_e^p * (E_0 - E_min) with p >= 3 and E_min = 1e-9 * E_0.
2. Apply Helmholtz PDE density filter -r_min^2 * laplacian(rho_tilde) + rho_tilde = rho to guarantee mesh-independent minimum member size.
3. Size two-terminal flywheel inerter inertance b (kg) via F = b * (a_2 - a_1) to achieve target apparent-mass ratio mu_b = b / m_modal.

## How it works, in four stages
- Stage 1 (Wolff's Trabecular Bone Remodeling & Principal Stress Trajectories): Under gravity and wind loads, a continuum finite-element model (FEniCS/dolfinx is one open-source tool a reader could use; this folio ran no FE model) gives principal tensile and compressive stress trajectories σ_1, σ_2.
- Stage 2 (SIMP Power-Law Penalization & Helmholtz PDE Filtering): Element stiffness E_e(ρ_e) = E_min + ρ_e^p (E_0 − E_min) with p = 3 pushes intermediate densities toward 0 or 1, while a filter radius r_min suppresses checkerboard patterns and mesh dependency.
- Stage 3 (Toward Michell-like Layouts): For simple load cases, optimized layouts tend to resemble Anthony Michell's 1904 minimum-weight trusses. Keeping V/V_0 = 0.35 means 65% less concrete volume in the optimized slab region than a solid slab of the same envelope; whole-building savings would be smaller.
- Stage 4 (Flywheel Inerter): A ball-screw or rack-and-pinion flywheel inerter F = b(ü_2 − ü_1) has inertance b much larger than its own mass: for a ring flywheel on a screw, b = m_fly (2π r / P)², so r = 45 mm and lead P = 20 mm give b ≈ 200 m_fly (illustrative). Inerter-based devices have been studied for structural vibration suppression (Lazar et al. 2013); the drift reduction in the lab is illustrative.

## Reference values stated in the essay
- **Compliance Ratio (rough scaling, c / c_0)**: `≈ 2.9× (c ∝ 1/(V/V_0), illustrative)`
- **Slab Concrete Volume Reduction**: `−65% (1 − V/V_0; CO2e assumed proportional)`
- **Inerter Apparent Mass Gain**: `≈ 200× flywheel mass (r = 45 mm, P = 20 mm)`
- **Model Filter Status**: `FILTERED · no checkerboard in illustrative layout`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1007/s001580050176 (Scite report: https://scite.ai/reports/10.1007/s001580050176)
- What the essay compares against: V/V_0 = 0.35 · p = 3.0 ⇒ 1 − V/V_0 = 65% less slab concrete volume · b/m = 0.18 inerter ratio (drift reduction not computed)

## Recent research context
- **A Design Study: SIMP Topology Optimization and Flywheel Inerters for Lighter Floor Slabs**: This folio sketches how Bendsøe–Sigmund SIMP topology optimization (Sigmund 2001, DOI 10.1007/s001580050176), printable concretes (Roussel 2018, DOI 10.1016/j.cemconres.2018.04.005) and Smith's inerter (DOI 10.1109/TAC.2002.803532) could together replace solid flat slabs with bone-like ribs while inerters help manage wind sway. Its figures are illustrative.
