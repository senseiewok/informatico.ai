---
name: color-wave-bragg-brdf
description: AI-agnostic wave-optics and surface-physics skill for Bragg thin-film interference, gonioapparent automotive pearlescent color flop, and Cook-Torrance vs. Lambertian BRDF modeling.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Electromagnetic Color Wave Physics: Bragg Thin-Film Interference, Gonioapparent Automotive Pearlescence & Barragán Stucco Optics (Folio P.08)

## 1. Governing Law & Tectonic Identity
- **Folio**: `P.08 · Electromagnetic Color Waves & BRDF · Optics` (`REV 1.1`, Redated `2026-11-14`)
- **Governing Equation**: `Δ_OPD = 2 d √(n_f² − sin²θ_i) = m λ · f_r = k_d(ρ/π) + k_s(D F G) / [4(n·l)(n·v)]`
- **Primary Verification Kernel**: `skills/physics/p08/verify_p08.py`
- **Verification Benchmarks**: `n_f = 2.45 (TiO₂) · d = 240 nm, m = 2 ⇒ λ_peak = 588 nm · Flop Δλ = −10.9 nm at 28°`
- **Primary Scite Anchor DOI**: https://doi.org/10.1145/357290.357293 (Scite Report: https://scite.ai/reports/10.1145/357290.357293)

## 2. Deterministic Verification & Falsification Rules
1. Calculate thin-film optical path difference Delta_OPD = 2 * d_film * sqrt(n_f^2 - sin^2(theta_i)) and constructive interference peak wavelength lambda_peak(theta_i).
2. Compute angular color-flop blue shift Delta_lambda(theta_i) = lambda_peak(theta_i) - lambda_peak(0) as viewing angle theta_i increases from normal (0 deg) to grazing.
3. Decompose surface reflectance via Cook-Torrance BRDF f_r = k_d*(rho/pi) + k_s*(D_GGX * F_Schlick * G_Smith) / (4*(n.l)*(n.v)) to contrast specular metallic coats with matte mineral plaster.

## 3. 4-Stage Physical & Mathematical Mechanism
- Stage 1 (Maxwell Transverse Electromagnetic Wave Packet): Incident white daylight carries continuous spectral modes λ ∈ [380, 780] nm across the clearcoat dielectric boundary.
- Stage 2 (Bragg–Snell Thin-Film Phase Addition): Inside a 240 nm TiO₂ nanolayer (n_f = 2.45) on mica platelets, optical path difference Δ_OPD = 2 d √(n_f² − sin²θ_i) = m λ selects, in second order (m = 2) at normal incidence, λ_peak = 588 nm.
- Stage 3 (Gonioapparent Automotive Blue-Shift Color Flop): Sweeping viewing angle θ_i from 0° to 65° along a curved car fender shrinks √(n_f² − sin²θ_i), shifting λ_peak blueward by about −42 nm for the 240 nm film.
- Stage 4 (Cook–Torrance Specular vs. Barragán Lambertian Limit): Low microfacet roughness (α_r = 0.04) concentrates metallic car highlights, while Barragán's calcite stucco (α_r = 0.88) scatters hue uniformly.

## 4. Reference Telemetry & Acceptance Bounds
- **Constructive Peak Wavelength**: `λ_peak = 588 nm at 0° (m = 2)`
- **Angular Color-Flop Blue Shift**: `Δλ = −10.9 nm (at θ_i = 28°)`
- **Fresnel–Cook Specular Gain**: `F ≈ 0.18 (fixed illustrative value) · GGX α_r = 0.04`
- **Wave Interference Verdict**: `PEAK IN VISIBLE BAND (MODEL)`

## 5. Frontier Discovery & Contemporary Research Context (2024–2026)
- **Electromagnetic Interference & Cook–Torrance Microfacet BRDFs Unite Automotive Paint Flop and Architectural Pigments**: Coupling Bragg–Snell thin-film optical path interference with Cook & Torrance's physical microfacet BRDF (ACM Trans. Graph. DOI 10.1145/357290.357293) explains why TiO2-coated mica nanoplatelets in curved sports-car finishes shift the model peak by about −42 nm between 0° and 65° ('color flop'), whereas Luis Barragán's porous calcite lime walls hold hue invariant across every angle.
