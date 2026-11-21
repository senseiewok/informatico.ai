---
name: unsaturated-suction-slope
description: AI-agnostic civil geotechnical skill for van Genuchten-Mualem unsaturated soil water retention, Lu-Godt-Wu closed-form suction stress sigma_s = -S_e * psi, and rainfall-induced infinite-slope Factor of Safety.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Unsaturated Soil Suction Stress, van Genuchten–Mualem Water Retention & Rainfall-Induced Infinite-Slope Instability (Folio E.14)

A plain-text companion to the essay at https://informatico.ai/engineering/e14/ (`E.14 · Unsaturated Suction Stress & Slope Margin · REV 1.0`, `REV 1.0`, redated `2026-11-21`).

## The governing relation
`S_e = [1 + (α_vG ψ)^n]^(−m) · σ^s = −S_e ψ · FS = tan φ' / tan β + (c' − σ^s tan φ') / (γ z sin β cos β)`

## Rules the essay derives
1. Enforce the physical domain psi = u_a - u_w >= 0 kPa, alpha_vg > 0 kPa^-1, and n > 1.0 (m = 1 - 1/n in (0, 1)) for van Genuchten effective saturation S_e(psi) = [1 + (alpha_vg * psi)^n]^(-m) and Mualem relative hydraulic conductivity K_r(S_e).
2. Compute Lu-Godt-Wu closed-form suction stress as sigma_s(psi) = -S_e(psi) * psi <= 0 (with sigma_s = 0 at psi = 0), keeping effective weighting chi = S_e rather than extrapolating Terzaghi chi = 1.0 into unsaturated soil.
3. Distinguish fine-grained monotonic retention (1 < n <= 2, silty loam where |sigma_s| grows monotonically with suction) from coarse-grained non-monotonic retention (n > 2, clean sand where |sigma_s| peaks near air-entry and declines toward zero upon drying).
4. Frame infinite-slope stability as a steady-suction, constant-gamma Tier T1-T2 screening hypothesis that requires 3D seepage, wetting-drying hysteresis, and field tensiometry before any site-level slope evaluation.

## How it works, in four stages
- Stage 1 (van Genuchten–Mualem Water Retention, Continuing E.05): Above the water table (ψ = u_a − u_w ≥ 0 kPa), soil pores hold both air and capillary water. van Genuchten (1980, DOI 10.2136/sssaj1980.03615995004400050002x) parameterizes effective saturation as S_e(ψ) = [1 + (α_vG ψ)^n]^(−m) with m = 1 − 1/n (requiring n > 1), and Mualem (1976, DOI 10.1029/WR012i003p00513) gives K_r(S_e) = S_e^(1/2) [1 − (1 − S_e^(1/m))^m]^2. In silty loam (α_vG = 0.02 kPa^−1, n = 1.60, m = 0.375) at ψ = 24.0 kPa, S_e = 0.904 and K_r = 0.1662.
- Stage 2 (Lu–Godt–Wu Suction Stress σ^s and Pore-Exponent Split): Lu, Godt & Wu (2010, DOI 10.1029/2009WR008646) unify Bishop effective stress σ' = (σ − u_a) − σ^s via closed-form suction stress σ^s(ψ) = −S_e(ψ) ψ ≤ 0 (compression-positive convention, so negative σ^s pulls grains together). For silty loam (1 < n ≤ 2), |σ^s| rises monotonically (−21.69 kPa at ψ = 24.0 kPa; −65.34 kPa at ψ = 120.0 kPa). For clean sand (n = 2.68 > 2, α_vG = 0.145 kPa^−1), |σ^s| peaks at ψ_peak = 7.964 kPa (−4.52 kPa) and declines to −2.08 kPa by ψ = 40.0 kPa.
- Stage 3 (Infinite-Slope Wetting Collapse While Still Unsaturated): Following Lu & Godt (2008, DOI 10.1029/2008WR006976) with steady uniform suction at z = 2.0 m, γ = 19.0 kN/m^3, c' = 2.0 kPa, and φ' = 28.0°, a steep silty-loam slope at β = 34.0° (> φ') stands at FS = 1.557 when ψ = 24.0 kPa. Rain wetting to ψ = 2.0 kPa drops FS to 0.962 (< 1.0) even before pore-water pressure turns positive, and saturation (ψ = 0 kPa, K_r = 1.0) drops FS to 0.902.
- Stage 4 (Open Hypothesis, Tier T1–T2, and Falsification Condition): Hypothesis (Tier T1–T2): in shallow unsaturated hillslopes steeper than their drained friction angle (β > φ'), storm-triggered collapse below FS = 1.0 tracks the loss of S_e ψ during wetting rather than waiting for positive u_w, whereas setting Bishop χ = 1.0 on dry clean sand (ψ = 40.0 kPa, γ = 18.0 kN/m^3, c' = 0, φ' = 32°, β = 36°) falsely inflates FS from 0.936 to 2.320. This 1D steady-suction hypothesis is falsified where 3D topographic flow convergence, macropore bypass (Iverson 2000, DOI 10.1029/2000WR900090), wetting-branch hysteresis, or root cohesion governs field failure.

## Reference values stated in the essay
- **Effective Saturation & Conductivity**: `S_e = 0.904 · K_r = 0.1662 (model)`
- **Lu–Godt–Wu Suction Stress (σ^s)**: `−21.69 kPa (σ'_n = 47.81 kPa, model)`
- **Infinite-Slope Factor of Safety (FS)**: `FS = 1.557 (τ = 17.62 kPa, model)`
- **Mohr–Coulomb Suction Regime**: `ABOVE LIMIT EQUILIBRIUM (FS >= 1.2, model)`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/engineering/e14/verify_e14_unsaturated_suction.py
python skills/engineering/e14/verify_e14_unsaturated_suction.py --planted-defect
```

## Primary source
- https://doi.org/10.2136/sssaj1980.03615995004400050002x (Scite report: https://scite.ai/reports/10.2136/sssaj1980.03615995004400050002x)
- What the essay compares against: Model values (silty loam ψ = 24.0 kPa, β = 34.0°): S_e = 0.904 · K_r = 0.1662 · σ^s = −21.69 kPa · FS = 1.557 (collapses to 0.962 at ψ = 2.0 kPa)

## Recent research context
- **Lu–Godt–Wu Suction Stress, van Genuchten Exponent n & Unsaturated Slope Collapse**: Why do steep unsaturated hillslopes fail before pore water turns positive, while dry clean sands lose capillary cohesion? Coupling van Genuchten–Mualem retention (1976, 1980) with Lu, Godt & Wu suction stress (2010, DOI 10.1029/2009WR008646) separates monotonic silty loam (n = 1.60; FS drops from 1.557 at ψ = 24 kPa to 0.962 at ψ = 2 kPa) from non-monotonic clean sand (n = 2.68; FS = 0.936 at ψ = 40 kPa).
