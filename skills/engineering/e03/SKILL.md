---
name: acoustic-helmholtz-metamaterial
description: AI-agnostic acoustics and wave-mechanics engineering skill for sub-wavelength Helmholtz resonator arrays, Stinson viscothermal boundary-layer impedance, and critical coupling.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Sub-Wavelength Acoustic Metamaterial Helmholtz Arrays and Viscothermal Boundary-Layer Damping (Folio E.03)

A plain-text companion to the essay at https://informatico.ai/engineering/e03/ (`E.03 · Acoustic Metamaterials & Viscothermal Damping · CSI 09 84 13`, `REV 1.3`, redated `2026-11-14`).

## The governing relation
`δ_v = √(2ν/ω) · Z_s = ρ_0 c_0 ⇒ α = 1.0 · CSI 09 84 13`

## Rules the essay derives
1. Compute viscous boundary layer thickness delta_v = sqrt(2 * nu / omega) and Womersley number Wo = r_neck * sqrt(omega / nu) = sqrt(2) * r_neck / delta_v (so the ratio r_neck / delta_v equals Wo / sqrt(2)).
2. Enforce critical coupling condition Re(Z_surface) = rho_0 * c_0 and Im(Z_surface) = 0 at target resonance omega_0 for unity absorption.
3. Include an end-correction length in the effective neck inductance; the approximate form delta_l = 0.85 * r_neck * (1 - 1.25 * sqrt(porosity)) is this folio's working choice and should be checked against an acoustics reference before design use.

## How it works, in four stages
- Stage 1 (Oscillatory Stokes Boundary Layer): At f_0 = 160 Hz, the viscous boundary layer in air is δ_v = √(2ν/ω) = 0.174 mm.
- Stage 2 (Complex Effective Density & Bulk Modulus): When neck radius r_neck = 0.65 mm approaches 3.7 δ_v, viscous shear dissipates acoustic kinetic energy.
- Stage 3 (Critical Impedance Matching, Z_s = Z_0): Reactance vanishes at Helmholtz resonance ω_0 while resistance matches ρ_0 c_0 ≈ 413 Pa·s/m. The page sets the resistance to 1.04 ρ_0 c_0 at the default neck radius, a fixed model value.
- Stage 4 (Broadband Detuned Array): A design idea, not a built panel: several detuned coiled cavities could spread absorption over roughly 125–315 Hz in a panel about 110 mm deep (1/19 of the 2.14 m wavelength at 160 Hz).

## Reference values stated in the essay
- **Viscous Boundary Layer (δ_v)**: `0.174 mm (at 160 Hz)`
- **Normalized Surface Impedance**: `Z_s / Z_0 = 1.04 + 0.00 i (model, at resonance)`
- **Peak Absorption Coefficient**: `α_peak = 0.9996 (model, near critical match)`
- **Acoustic Verdict**: `DESIGN TARGET · NOT TESTED`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1146/annurev-matsci-070616-124032 (Scite report: https://scite.ai/reports/10.1146/annurev-matsci-070616-124032)
- What the essay compares against: Model values: δ_v = 0.174 mm at 160 Hz · α = 0.9996 for Z_s/Z_0 = 1.04 at resonance

## Recent research context
- **Critically Coupled Resonators Absorb Low-Frequency Sound in Thin Panels**: Building on Helmholtz (1863) and Stinson's viscothermal theory (1991, DOI 10.1121/1.400379), coiled-space and labyrinthine absorbers can work at depths far below a quarter wavelength (review: DOI 10.1146/annurev-matsci-070616-124032). Romero-García and colleagues (2016, DOI 10.1038/srep19519) showed that when a resonator's losses balance its leakage, absorption at resonance can reach 100%.
