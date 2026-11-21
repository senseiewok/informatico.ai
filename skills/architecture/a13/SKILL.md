---
name: isler-thin-shell-buckling
description: AI-agnostic architectural engineering skill for idealized thin spherical-cap membrane stress, Zoelly (1915) classical elastic buckling, and illustrative imperfection-sensitivity knockdown bounds.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Heinz Isler's Funicular Thin-Shell Domes: Inverted-Hanging Form-Finding, Zoelly Buckling & Imperfection Knockdowns (Folio A.13)

A plain-text companion to the essay at https://informatico.ai/architecture/a13/ (`A.13 · Heinz Isler Funicular Thin-Shell Domes & Imperfection Knockdowns · REV 1.0`, `REV 1.0`, redated `2026-11-20`).

## The governing relation
`R = (L² + 4f²)/(8f) · σ_mem = q R / (2t) · p_cr^cl = 2E / √(3(1−ν²)) · (t/R)² · p_cr^act = γ_kd · p_cr^cl`

## Rules the essay derives
1. Compute spherical-cap curvature radius R = (L^2 + 4 * f^2) / (8 * f) and uniform-projection crown membrane stress sigma_mem = (q * R) / (2 * t); record the rim slope factor sec(phi_0) omitted by uniform plan projection.
2. Compute Zoelly (1915) classical elastic buckling pressure p_cr^cl = (2 * E / sqrt(3 * (1 - nu^2))) * (t / R)^2 and verify quadratic (t/R)^2 scaling when thickness doubles.
3. Apply an explicit empirical-style knockdown function gamma_kd(R/t) = 0.14 + 0.32 * exp(-0.1 * sqrt(R / t)) as an illustrative bound (not a code rule) and check that thin 15 mm caps drop below lambda_b = 3.0.

## How it works, in four stages
- Stage 1 (Inverted-Hanging Cloth & Pneumatic Form-Finding): In his 1959 IASS Madrid lecture (published 1961), Swiss engineer Heinz Isler grouped thin concrete shell form-finding into three physical experiments: freely shaped hills, inflated pneumatic membranes, and hanging textiles stiffened with plaster or frozen in winter air and inverted. Because a hanging sheet carries gravity load in pure membrane tension, its inverted rigid geometry channels uniform dead load along compression-only trajectories with minimal bending.
- Stage 2 (Idealized Spherical-Cap Geometry & Uniform-Projection Membrane Stress): As a tractable analytical reference—distinct from Deitingen Süd's three-point free-edge wing shells, which share only the 90 mm double-rebar-cover thickness—the model evaluates a spherical cap of span L = 31.6 m and rise f = 4.2 m (curvature radius R = 31.82 m, rim half-angle φ_0 = 29.8°). At t = 90.0 mm (ρ = 2,400 kg/m³) plus 1.20 kN/m² superimposed load, uniform plan-projected gravity load is q = 3.318 kN/m² (neglecting the sec φ_0 = 1.152 slope factor at the rim and boundary haunches), giving crown compressive stress σ_mem = 0.587 MPa.
- Stage 3 (Zoelly Classical Elastic Buckling & Post-Buckling Sensitivity): Because σ_mem = 0.587 MPa is under 2% of an assumed 35 MPa concrete compressive strength, crushing does not govern this model. Instead, thin doubly curved shells face elastic snap-through buckling. R. Zoelly's 1915 linear-elastic formula for an ideal uniform sphere under normal pressure gives p_cr^cl = 282.9 kN/m² at E = 30.0 GPa and ν = 0.20—an idealized upper bound that omits concrete creep, cracking (Ramm & Mehlhorn 1991, DOI 10.1016/0141-0296(91)90050-M), asymmetric snow, and edge bending.
- Stage 4 (Illustrative Knockdown Curve & Tier T2 Hypothesis): Hutchinson (1967, DOI 10.1115/1.3607667), Gerasimidis et al. (2018, DOI 10.1115/1.4040455), and Abbasi, Derveni, and Reis (2023, DOI 10.1115/1.4056801) analyzed why tiny inward dimples sharply cut spherical shell buckling capacity below Zoelly's line. Applying an illustrative empirical-style knockdown function γ_kd = 0.14 + 0.32 exp(−0.1 √(R/t)) (NASA SP-8007 and Dulácska inspired, not a design code formula) at R/t = 353.5 yields γ_kd = 0.189, p_cr^act = 53.4 kN/m², and buckling ratio λ_b = 16.1. Hypothesis (Tier T2 model): elastic snap-through under inward dimples governs reserve rather than crushing; falsified for a physical shell if creep, cracking, asymmetric snow, or deeper inward dimples (δ_0 / t > 0.5) push collapse below λ_b = 3.0 or induce edge bending.

## Reference values stated in the essay
- **Membrane Compressive Stress**: `0.587 MPa (Crown, Model Service Load)`
- **Zoelly Classical Buckling Pressure**: `282.9 kN/m² (Idealized Linear Elastic)`
- **Illustrative Knockdown Pressure**: `γ_kd = 0.189 ⇒ p_cr = 53.4 kN/m² (Model)`
- **Model Buckling Ratio (λ_b)**: `16.1 (Model Value · Not a Structural Check)`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/architecture/a13/verify_a13_isler_buckling.py
python skills/architecture/a13/verify_a13_isler_buckling.py --planted-defect
```

## Primary source
- https://doi.org/10.1016/0141-0296(91)90050-M (Scite report: https://scite.ai/reports/10.1016/0141-0296(91)90050-M)
- What the essay compares against: Idealized spherical-cap model: L = 31.6 m · f = 4.2 m · R = 31.82 m · t = 90.0 mm · σ_mem = 0.587 MPa · p_cr^cl = 282.9 kN/m² · γ_kd = 0.189 · p_cr^act = 53.4 kN/m² · λ_b = 16.1

## Recent research context
- **Inward Dimples, Imperfection Knockdowns, and the Buckling Limit of Thin Funicular Concrete Shells**: Pairing Ramm and Mehlhorn's nonlinear concrete shell analysis (DOI 10.1016/0141-0296(91)90050-M) with spherical imperfection sensitivity from Hutchinson (1967, DOI 10.1115/1.3607667) and Abbasi, Derveni, and Reis (2023, DOI 10.1115/1.4056801), this folio evaluates an idealized 90 mm spherical cap (R = 31.82 m) where crown compression is 0.587 MPa and an illustrative knockdown curve yields λ_b = 16.1. Model values only, not field measurements.
