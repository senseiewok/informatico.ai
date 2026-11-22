---
name: bridge-pier-scour-timescale
description: AI-agnostic hydraulic engineering skill for Shields critical velocity V_c, Sheppard-Melville and HEC-18 CSU circular pier scour, and Melville-Chiew clear-water flood-duration time-scale factor K_t.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Bridge Pier Local Scour, Shields Sediment Threshold & Flood-Duration Time-Scale Lag (Folio E.16)

A plain-text companion to the essay at https://informatico.ai/engineering/e16/ (`E.16 · Bridge Pier Scour & Flood Time-Scale Lag · REV 1.0`, `REV 1.0`, redated `2026-11-21`).

## The governing relation
`y_s,SM = 2.5 a* f_1 f_2 f_3 · y_s,CSU = 2.0 K_1 K_2 K_3 y_1 (a* / y_1)^0.65 Fr_1^0.43 · K_t(t_d) = exp(−0.03 |(V_c / V_1) ln((t_d / 24) / t_e)|^1.6) · y_s(t_d) = K_t(t_d) y_s,SM`

## Rules the essay derives
1. Enforce finite positive pier diameter a*, approach depth y_1, median grain size d_50, gravity g, sediment specific gravity s > 1.0, relative roughness 5.53 y_1 / d_50 > 1.0, and clear-water intensity ratio V_1 / V_c in [0.405, 1.00].
2. Evaluate Sheppard-Melville clear-water equilibrium scour y_s,SM = 2.5 a* f_1 f_2 f_3 alongside Froude-capped HEC-18 CSU y_s,CSU, keeping grain-coarseness attenuation f_3 active rather than setting f_3 = 1.
3. Convert dimensionless time scale t* = V_1 t_e,sec / a* using explicit SI inputs (a* in m, V_1 in m/s, empirical factor 30.89 days*s^-1 for y_1 / a* <= 6 or 48.26 days*s^-1 for y_1 / a* > 6) and clamp K_t(t_d) = 1.0 whenever flood duration t_d / 24 >= t_e.
4. Label transient clear-water scour y_s(t_d) = K_t(t_d) y_s,SM as a Tier T1-T2 illustrative hydraulic hypothesis falsified by live-bed transport (V_1 / V_c > 1), graded armor-layer breach, multi-flood deposition-erosion cycles, cohesive soils, or debris rafts.
5. State that this is an illustrative single-event model. Design practice uses equilibrium or envelope scour depth on purpose because scour accumulates across floods; never use K_t or any value from this skill to assess or reduce scour depth at a real bridge.

## How it works, in four stages
- Stage 1 (Shields Incipient Motion & Logarithmic Critical Velocity V_c): Forensic analysis of 503 United States bridge failures from 1989 to 2000 by Wardhana and Hadipriono (2003, DOI 10.1061/(ASCE)0887-3828(2003)17:3(144)) attributed 266 failures (52.88%) to hydraulic flood, scour, and debris forces. Under Shields incipient-motion mechanics (documented by Buffington 1999, DOI 10.1061/(ASCE)0733-9429(1999)125:4(376)) and Melville (1997, DOI 10.1061/(ASCE)0733-9429(1997)123:2(125)), cohesionless quartz grains (specific gravity s = 2.65, d_50 = 2.00 mm, θ_c = 0.045) reach critical shear velocity u_*c = √(θ_c (s − 1) g d_50) = 0.03817 m/s and depth-averaged threshold velocity V_c = 5.75 u_*c log_10(5.53 y_1 / d_50) = 0.860 m/s at approach depth y_1 = 3.00 m.
- Stage 2 (Sheppard–Melville Equilibrium Scour vs. Froude-Only HEC-18 CSU): Sheppard, Melville, and Demir (2014, DOI 10.1061/(ASCE)HY.1943-7900.0000800) evaluated 23 pier-scour formulas across 569 laboratory and 928 field records (filtered to 441 laboratory and 791 field datasets), merging clear-water factors into y_s,SM = 2.5 a* f_1 f_2 f_3 with f_1 = tanh((y_1 / a*)^0.4), f_2 = max(0, 1 − 1.2 [ln(V_1 / V_c)]^2), and f_3 = (a* / d_50) / [0.4 (a* / d_50)^1.2 + 10.6 (a* / d_50)^(−0.13)]. For a* = 2.00 m (f_1 = 0.8262, f_3 = 0.6263), near-threshold flow V_1 / V_c = 0.45 gives y_s,SM,eq = 0.608 m versus Froude-based CSU y_s,CSU,eq = 1.629 m (2.682× higher because CSU omits V_c), whereas near the clear-water peak V_1 / V_c = 0.85 gives y_s,SM,eq = 2.505 m versus y_s,CSU,eq = 2.142 m.
- Stage 3 (Melville & Chiew Equilibrium Time Scale t_e and Transient Factor K_t): Melville and Chiew (1999, DOI 10.1061/(ASCE)0733-9429(1999)125:1(59)) showed that clear-water horseshoe-vortex scour approaches equilibrium over time scale t_e (days) = 30.89 (a* / V_1) (V_1 / V_c − 0.4) (y_1 / a*)^0.25 for y_1 / a* <= 6.0 (where empirical constant 30.89 = 2.669 × 10^6 / 86,400 days·s^(−1) converts dimensionless t* = V_1 t_e,sec / a* with a* in m and V_1 in m/s), with temporal fraction K_t(t_d) = exp(−0.03 |(V_c / V_1) ln((t_d / 24) / t_e)|^1.6) for t_d / 24 < t_e (clamped to 1.0 once t_d / 24 >= t_e). At V_1 / V_c = 0.85 (V_1 = 0.731 m/s), t_e = 42.09 days (1,010.1 h): a 2.0 h flash flood reaches K_t = 0.4841 (y_s = 1.213 m), and a 24.0 h storm reaches K_t = 0.7254 (y_s = 1.817 m). Applying a relation fitted to steady laboratory flows to a 2.00 m pier and to a flood duration is an extrapolation.
- Stage 4 (Open Hypothesis, Tier T1–T2, and Falsification Conditions): Hypothesis (Tier T1–T2): in uniform cohesionless sand or fine gravel around an unskewed circular pier under single-peak clear-water flow (0.45 <= V_1 / V_c <= 1.00), transient scour depth follows y_s(t_d) = K_t(t_d) y_s,SM,eq, excavating roughly half of equilibrium depth within two hours yet remaining below steady-state equilibrium across 24-hour floods (1.817 m vs. 2.505 m S/M and 2.142 m CSU). This hypothesis is falsified under live-bed sediment transport (V_1 / V_c > 1.0), in graded armored riverbeds where horseshoe vortices breach surface armor into finer sub-layers ("armor-break" scour, Kabiri-Samani, Fathi & Farooq 2026, DOI 10.2478/johh-2026-0004), across multi-flood deposition-erosion sequences (Link et al. 2020, DOI 10.1061/(ASCE)HY.1943-7900.0001696), or when woody debris rafts widen the effective pier obstruction.

## Reference values stated in the essay
- **Transient & S/M Eq. Scour**: `y_s(t_d) = 1.817 m · y_s,SM = 2.505 m (model)`
- **HEC-18 CSU & Time Factor**: `y_s,CSU = 2.142 m · K_t = 0.7254 (model)`
- **Threshold V_c & Eq. Time t_e**: `V_c = 0.860 m/s · t_e = 42.09 d (model)`
- **Clear-Water Scour Regime**: `TRANSIENT HYDROGRAPH LAG (0.65 <= K_t < 0.90, model)`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/engineering/e16/verify_e16_pier_scour_timescale.py
python skills/engineering/e16/verify_e16_pier_scour_timescale.py --planted-defect
```

## Primary source
- https://doi.org/10.1061/(ASCE)0733-9429(1999)125:1(59) (Scite report: https://scite.ai/reports/10.1061/(ASCE)0733-9429(1999)125:1(59))
- What the essay compares against: Model values (circular pier a* = 2.00 m, y_1 = 3.00 m, d_50 = 2.00 mm, V_1 / V_c = 0.85, t_d = 24.0 h): V_c = 0.860 m/s · y_s,SM,eq = 2.505 m · y_s,CSU,eq = 2.142 m · t_e = 42.09 days · K_t = 0.7254 · y_s(24 h) = 1.817 m (1.213 m at 2.0 h flash flood)

## Recent research context
- **Shields Sediment Threshold, Sheppard–Melville Pier Scour & Flash-Flood Time-Scale Lag**: In one survey, flood and scour accounted for 52.88% of U.S. bridge failures from 1989 to 2000 (Wardhana & Hadipriono 2003). Equilibrium formulas describe weeks of steady flow, not one short flood. Coupling Sheppard–Melville equilibrium scour (2014) with Melville–Chiew time lag (1999, DOI 10.1061/(ASCE)0733-9429(1999)125:1(59)) tracks y_s from 1.213 m at 2.0 h and 1.817 m at 24.0 h toward 2.505 m over t_e = 42.09 days.
