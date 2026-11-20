---
name: biot-poroelasticity-fault-slip
description: AI-agnostic civil geomechanics skill for Biot 3D poroelasticity (alpha = 1 - K_d/K_s), Rice-Cleary Skempton B coupling, and cohesionless Mohr-Coulomb fault slip margin under subsurface fluid injection.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Biot 3D Poroelasticity, Skempton Undrained Coupling & Mohr–Coulomb Fault Slip Margin in Geologic CO2 Storage (Folio E.13)

A plain-text companion to the essay at https://informatico.ai/engineering/e13/ (`E.13 · Biot Poroelasticity & Fault Slip Margin · REV 1.0`, `REV 1.0`, redated `2026-11-20`).

## The governing relation
`α = 1 − K_d / K_s · Δp_u = +B Δσ_mean · |τ| / (σ_n − α_fault(p_0 + Δp_inj)) < μ_f`

## Rules the essay derives
1. Compute intact-matrix Biot-Willis coefficient alpha = 1 - K_d / K_s (requiring 0 < K_d < K_s) and Skempton undrained coefficient B = (1/K_d - 1/K_s) / [1/K_d - 1/K_s + phi*(1/K_f - 1/K_s)] under compression-positive sign convention delta_p_u = +B * delta_sigma_mean.
2. Keep fault-plane Terzaghi effective stress alpha_fault = 1.0 distinct from matrix alpha, and apply alpha_fault consistently in both sigma_n_eff = sigma_n - alpha_fault*(p_0 + delta_p_inj) and critical_delta_p = (sigma_n - |tau|/mu_f)/alpha_fault - p_0; state explicitly when total stress sigma_h is held uncoupled from eta_poro * delta_p_inj.
3. Check both shear slip tendency |tau| / sigma_n_eff < mu_f and tensile hydraulic margin min(sigma_v, sigma_h) - (p_0 + delta_p_inj) > 0; treat sigma_n_eff <= 0 explicitly as tensile failure with undefined shear slip tendency.
4. Frame injection stability as a site-dependent Tier T1-T2 hypothesis bounded by stress ratio k_0 and basement fault proximity; never extrapolate closed-form screening outputs into site-specific permit claims.

## How it works, in four stages
- Stage 1 (Biot–Willis 3D Effective Stress, Continuing E.05): Whereas Terzaghi's 1D soil limit treats solid grains as incompressible (α → 1), stiff porous sandstone with drained bulk modulus K_d = 12.0 GPa and solid mineral grain modulus K_s = 36.0 GPa carries part of the hydrostatic stress in its grain skeleton, yielding α = 1 − K_d / K_s = 0.667 (Biot 1941, DOI 10.1063/1.1712886; Biot & Willis 1957, DOI 10.1115/1.4011606).
- Stage 2 (Skempton Undrained Pore-Pressure Response B): Under compression-positive geomechanics (Δp_u = +B Δσ_mean), Skempton (1954, DOI 10.1680/geot.1954.4.4.143) and Rice & Cleary (1976, DOI 10.1029/RG014i002p00227) write B = (1/K_d − 1/K_s) / [1/K_d − 1/K_s + φ(1/K_f − 1/K_s)]. For φ = 0.20 and brine bulk modulus K_f = 2.2 GPa, B = 0.394; replacing brine with compressible supercritical CO2 (K_f = 0.20 GPa) lowers B to 0.053 in the folio model.
- Stage 3 (Mohr–Coulomb Fault Slip Margin & Stress-Regime Contrast): On a cohesionless fault dipping 60° (fault-plane angle β = 30° from vertical σ_v, normal 30° from σ_h; σ_v = 50.0 MPa, hydrostatic p_0 = 20.0 MPa, μ_f = 0.60, α_fault = 1.0, and uncoupled total stress σ_h = k_0 σ_v), a sedimentary stress ratio k_0 = 0.72 gives σ_n = 39.50 MPa, τ = 6.062 MPa, and Δp_crit = 9.40 MPa; at Δp_inj = 4.5 MPa, slip tendency τ/σ'_n = 0.404 stays below 0.60. In a critically stressed crystalline basement (k_0 = 0.60), Δp_crit drops to 0.57 MPa and Δp_inj = 4.5 MPa raises τ/σ'_n to 0.825 (> 0.60).
- Stage 4 (Open Hypothesis, Tier T1–T2, and Falsification Condition): Hypothesis (Tier T1–T2): in stiff porous sedimentary storage reservoirs where stress ratio k_0 keeps Δp_inj < Δp_crit and compressible supercritical CO2 lowers undrained B while keeping overpressure moderate (Vilarrasa & Carrera 2015, DOI 10.1073/pnas.1413284112), fault slip tendency remains below μ_f; this hypothesis is falsified in any site where pore pressure reaches critically stressed basement faults (Zoback & Gorelick 2012, DOI 10.1073/pnas.1202473109; Ellsworth 2013, DOI 10.1126/science.1225942), drives σ'_n ≤ 0, or where coupled poroelastic stress transfer pushes |τ|/σ'_n ≥ μ_f.

## Reference values stated in the essay
- **Biot α & Skempton B (Brine / CO2)**: `α = 0.667 · B = 0.394 / 0.053 (model)`
- **Fault Slip Tendency (|τ| / σ'_n)**: `0.404 < 0.60 (Δp_crit = 9.40 MPa, model)`
- **Shear & Hydraulic Margins**: `Slip +4.90 MPa · Tensile +11.50 MPa (model)`
- **Mohr–Coulomb Fault Status**: `BELOW SLIP THRESHOLD (model, uncoupled σ_h)`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/engineering/e13/verify_e13_biot_poroelasticity.py
python skills/engineering/e13/verify_e13_biot_poroelasticity.py --planted-defect
```

## Primary source
- https://doi.org/10.1063/1.1712886 (Scite report: https://scite.ai/reports/10.1063/1.1712886)
- What the essay compares against: Model values (sedimentary k_0 = 0.72, Δp_inj = 4.5 MPa): α = 0.667 · B = 0.394 (brine) / 0.053 (CO2) · τ/σ'_n = 0.404 < 0.60 · Δp_crit = 9.40 MPa

## Recent research context
- **Biot 3D Poroelasticity, Skempton Fluid Contrast & the Sedimentary-vs-Basement Fault Debate**: Whether large-scale CO2 storage reactivates faults hinges on stress regime and fluid compressibility: Zoback & Gorelick (2012, DOI 10.1073/pnas.1202473109) and Ellsworth (2013, DOI 10.1126/science.1225942) highlight critically stressed basement faults (Δp_crit = 0.57 MPa at k_0 = 0.60 in this model), whereas Vilarrasa & Carrera (2015, DOI 10.1073/pnas.1413284112) emphasize softer sedimentary basins (Δp_crit = 9.40 MPa at k_0 = 0.72) and low-viscosity CO2 behavior (B = 0.053 vs. 0.394 brine).
