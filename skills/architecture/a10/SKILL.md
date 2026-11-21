---
name: kinetic-origami-miura-facade
description: AI-agnostic architectural and mechanical-metamaterial skill for Miura-ori rigid origami kinematics, Kawasaki flat-foldability, Schenk-Guest negative Poisson ratio (nu_xy = -tan^2(phi)), and kinetic solar facades.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Kinetic Origami & Miura-Ori Deployable Biomimetic Facades: Isometric Crease Kinematics, Auxetic Poisson Ratio Inversion & Solar Mashrabiya Envelopes (Folio A.10)

A plain-text companion to the essay at https://informatico.ai/architecture/a10/ (`A.10 · Kinetic Origami & Auxetic Mashrabiya Facades · CSI 10 71 13`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`tan(γ_2/2) = cos α · tan(γ_1/2) · ν_xy = −tan² φ < 0 · Kawasaki ∑ α_{2i} = π · CSI 10 71 13`

## Rules the essay derives
1. Enforce Kawasaki's flat-foldability theorem sum(alpha_even) = sum(alpha_odd) = pi and Maekawa's mountain-valley rule |M - V| = 2 at every interior degree-4 vertex (Hull 2020, DOI 10.1017/9781108778633).
2. Compute the semi-width angle phi from this folio's simplified parametrization cos(phi) = sin(alpha) * cos(theta / 2) and evaluate nu_xy = -tan^2(phi) < 0 (about -0.37 at alpha = 64, theta = 36); note that Schenk & Guest (2013, DOI 10.1073/pnas.1217998110) parametrize the fold differently.
3. Couple facade deployment angle theta to solar altitude; treat SHGC <= 0.22 at peak insolation and >= 250 EML daylight as this folio's own design targets and report SHGC as a model value, not a measurement.

## How it works, in four stages
- Stage 1 (Kawasaki & Maekawa Flat-Foldable Vertex, Continuing M.05): Four rigid parallelogram facets meet at a degree-4 vertex satisfying Kawasaki alternating-angle sums (π) and Maekawa mountain-valley parity (|M − V| = 2; Hull 2020, DOI 10.1017/9781108778633), leaving one degree of freedom in the ideal rigid sheet (Miura 1985).
- Stage 2 (Spherical Trigonometry Dihedral Coupling): With primary fold angle γ_1 = θ = 36° and α = 64°, tan(γ_2/2) = cos α · tan(γ_1/2) yields secondary fold angle γ_2 ≈ 16.2° for zero-thickness facets (real thick panels require hinge-offset geometry; Tachi 2011, DOI 10.1201/b10971-24).
- Stage 3 (Auxetic Poisson Ratio, after Schenk & Guest 2013, DOI 10.1073/pnas.1217998110): Schenk and Guest showed that a Miura-ori sheet exhibits a negative in-plane Poisson ratio. In this folio's simplified parametrization, cos φ = sin α · cos(θ/2) gives φ ≈ 31.3° and ν_xy = −tan² φ ≈ −0.37 at default settings.
- Stage 4 (Mashrabiya-Inspired Solar Shading, Continuing A.03/A.04): With assumed bare-glazing SHGC_glass = 0.60 and shading effectiveness η_shade = 0.845, the folio's illustrative rule SHGC = SHGC_glass · (1 − η_shade · cos θ) gives 0.19 at θ = 36° (−68.4% solar heat gain in the model); published origami facade simulations (Meloni et al. 2023, DOI 10.1016/j.scs.2023.104740; Kahramanoğlu & Çakıcı Alp 2023, DOI 10.1016/j.jobe.2023.106241) motivate this study, though cooling loads and daylight are not computed here.

## Reference values stated in the essay
- **In-Plane Poisson Ratio (ν_xy)**: `−0.37 (Model, −tan² φ)`
- **Effective Facade SHGC**: `0.19 (Model, −68.4% vs Bare Glazing)`
- **Coupled Dihedral Angle (γ_2)**: `16.2° (Model, γ_1 = θ)`
- **Kinematic Model Check**: `ONE DEGREE OF FREEDOM (IDEAL RIGID MODEL)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1073/pnas.1217998110 (Scite report: https://scite.ai/reports/10.1073/pnas.1217998110)
- What the essay compares against: Model values: α = 64° · θ = 36° ⇒ ν_xy ≈ −0.37 (folio parametrization) · SHGC = 0.19 (assumed SHGC_glass = 0.60, η_shade = 0.845)

## Recent research context
- **Miura-Ori Spherical Vertex Kinematics & Negative Poisson Ratios in a Design Model for Deployable Solar Mashrabiya Envelopes**: Schenk & Guest showed that a Miura-folded sheet has a negative in-plane Poisson ratio (PNAS, DOI 10.1073/pnas.1217998110). This design study, continuing Folios A.04, A.03 and M.05, uses that geometry for a proposed one-actuator solar screen: in the folio's simplified model ν_xy ≈ −0.37 and SHGC = 0.19 at default settings. Model values, not measurements.
