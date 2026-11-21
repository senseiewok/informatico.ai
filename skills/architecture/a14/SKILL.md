---
name: candela-hypar-membrane-shear
description: AI-agnostic architectural and structural engineering skill for Félix Candela's doubly-ruled hyperbolic paraboloid (hypar) concrete shells, Pucher flat-projection membrane shear equilibrium, and idealized cantilever/rib bounds.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Félix Candela's Hypar Ruled Shells: Hyperbolic Paraboloid Membrane Shear & Straight-Line Formwork (Folio A.14)

A plain-text companion to the essay at https://informatico.ai/architecture/a14/ (`A.14 · Félix Candela Hypar Ruled Shells & Pucher Membrane Shear · REV 1.0`, `REV 1.0`, redated `2026-11-21`).

## The governing relation
`z = (h / (a b)) x y · N_xy = (q_0 a b) / (2 h) · σ_1 = +N_xy / t · σ_2 = -N_xy / t · M_x = M_y = 0`

## Rules the essay derives
1. Define one quadrant of a hyperbolic paraboloid saddle as z(x, y) = (h / (a * b)) * x * y with twist parameter c = (a * b) / h.
2. Compute Pucher flat-projection membrane shear resultant as N_xy = (q_0 * a * b) / (2 * h) under uniform projected gravity load q_0, noting omitted slope-angle weight amplification.
3. Resolve 45-degree principal stresses as sigma_1 = +N_xy / t (tension) and sigma_2 = -N_xy / t (compression) in the idealized interior membrane model.
4. Evaluate compressive margin lambda_comp = (0.45 * f_ck) / |sigma_2| alongside shell-field thickness savings relative to a 200 mm slab, and flag free-edge bending and buckling limits.

## How it works, in four stages
- Stage 1 (Doubly-Ruled Hypar Geometry & Unbent Timber Formwork): A hyperbolic paraboloid quadrant z(x, y) = (h / (a b)) x y has negative Gaussian curvature everywhere (an anticlastic saddle) yet contains two families of straight generating lines along constant x and constant y. Because every section parallel to the axes is a straight line, builders could assemble formwork from unbent straight timber planks without curved falsework (Cassinello et al. 2010, DOI 10.3989/ic.10.040; Garlock & Billington 2011, DOI 10.2749/101686611x13049248220564).
- Stage 2 (Pucher Projected Membrane Equilibrium): Under uniform plan-projected gravity load q_0 = 1.741 kN/m² (40.0 mm concrete at ρ = 2,400 kg/m³ giving 0.941 kN/m² plus 0.80 kN/m² superimposed load), Pucher's 1934 projected equilibrium equation cancels normal membrane terms because ∂²z/∂x² = 0 and ∂²z/∂y² = 0 identically. In this idealized interior membrane model with supported edges, N_x = N_y = M_x = M_y = 0 and uniform shear becomes N_xy = (q_0 a b) / (2 h) = 31.35 kN/m.
- Stage 3 (Diagonal Principal Arch-Tie Field & Thickness Ratio): Rotating 45 degrees onto the bisecting diagonals resolves pure shear into equal principal tension σ_1 = +N_xy / t = +0.784 MPa and principal compression σ_2 = -N_xy / t = -0.784 MPa. Against an allowable compressive threshold of 0.45 f_ck = 15.75 MPa (f_ck = 35 MPa), the model compressive ratio is λ_comp = 20.1, while the 40 mm shell field uses 80.0% less concrete volume than a 200 mm solid flat slab (excluding stem and ribs).
- Stage 4 (Central Stormwater Funnel & Tier T2 Model Boundary): Grouping four quadrants into a 24.0 m by 24.0 m (576 m²) umbrella slopes rainwater inward toward a central hollow stem, collecting 8.0 L/s (28.8 m³/h) under 50 mm/h design rain. Hypothesis (Tier T2 analytical model): straight-ruled anticlastic curvature carries symmetric gravity load primarily in in-plane shear rather than bending. This flat-projection model is falsified for physical cantilevered umbrellas where slope-angle self-weight growth, free-edge boundary bending, valley-rib concentration, concrete creep, or thin-shell buckling (Ramm & Mehlhorn 1991, DOI 10.1016/0141-0296(91)90050-M; Wang et al. 2020, DOI 10.1016/j.engstruct.2020.111156) govern failure.

## Reference values stated in the essay
- **Membrane Shear Force (N_xy)**: `31.35 kN/m (Uniform in Model Quadrant)`
- **Principal Compressive Stress (σ_2)**: `-0.784 MPa (Quadrant Field, Model Service Load)`
- **Model Compressive Margin (λ_comp)**: `λ_comp = 20.1 (80.0% Savings vs 200 mm)`
- **Stormwater Harvest Rate (50 mm/h)**: `8.0 L/s (28.8 m³/h, 576 m² Model Roof)`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/architecture/a14/verify_a14_candela_hypar.py
python skills/architecture/a14/verify_a14_candela_hypar.py --planted-defect
```

## Primary source
- https://doi.org/10.14359/8024 (Scite report: https://scite.ai/reports/10.14359/8024)
- What the essay compares against: Model values (not measurements): a = b = 12.0 m · h = 4.0 m · t = 40.0 mm · q_0 = 1.741 kN/m² · N_xy = 31.35 kN/m · σ_2 = -0.784 MPa · λ_comp = 20.1 · 80.0% shell-field thickness saving vs 200 mm slab · Q_storm = 8.0 L/s (576 m²)

## Recent research context
- **Straight-Board Rulings, Pucher Shear Flow, and the Edge Boundaries of Thin Hypar Umbrellas**: Pairing Félix Candela's 1960 ACI shell formulations (DOI 10.14359/8024, 10.14359/8026) with contemporary structural evaluations of 8-sided and hexagonal umbrellas (Wang et al. 2020, DOI 10.1016/j.engstruct.2020.111156; 2022, DOI 10.1016/j.engstruct.2022.114577), this folio inspects a 40 mm hypar quadrant (a = b = 12.0 m, h = 4.0 m) where model shear is 31.35 kN/m (σ_2 = -0.784 MPa, λ_comp = 20.1). Model values only, not field measurements.
