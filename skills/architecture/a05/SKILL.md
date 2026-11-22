---
name: tectonic-acoustics-sabine-eyring
description: AI-agnostic architectural acoustics skill for Sabine/Eyring reverberation, Schroeder QRD coffered vaults, and the IEC 60268-16 Speech Transmission Index (STI).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Acoustic Sabin–Eyring Reverberation, Diffusive Coffered Vaults, and Speech Intelligibility (STI ≥ 0.68) (Folio A.05)

A plain-text companion to the essay at https://informatico.ai/architecture/a05/ (`A.05 · Architectural Acoustics · CSI 09 84 00`, `REV 1.2`, redated `2026-11-14`).

## The governing relation
`T_60 = 0.161V / [−S ln(1−α)] · STI = 0.74`

## Rules the essay derives
1. Estimate SI-unit Sabine T_60 = 0.161 V / A and Eyring logarithmic decay T_60 = 0.161 V / (-S ln(1 - alpha_bar)) (after Eyring 1930, DOI 10.1121/1.1915175) for volume V and area S.
2. Size Schroeder diffuser wells for prime p via d_n = (n^2 mod p) * c / (2 p f_0) under curved vaults (Schroeder 1979, DOI 10.1121/1.382601).
3. Apply the folio's own targets of STI >= 0.68 and noise <= NC-28 as model caveats, not requirements of IEC 60268-16 or ISO 3382-1.

## How it works, in four stages
- Stage 1 (Early Window, cf. Bradley 1986, DOI 10.1121/1.393908): Early sound, within about 50 ms, aids speech; C_50 = +4.8 dB is an illustrative estimate.
- Stage 2 (Schroeder Diffusion, DOI 10.1121/1.382601): For prime p and design wavelength λ_0 = c/f_0, well depths d_n = (n² mod p)·λ_0/(2p) scatter reflections.
- Stage 3 (Perforated Veneer, cf. Maa 1998, DOI 10.1121/1.423870): Maa models micro-perforated panel absorbers; this untested sketch backs 0.8 mm oak veneer with wool (assumed α_bar = 0.44).
- Stage 4 (Eyring Decay, DOI 10.1121/1.1915175): For V = 2,400 m³ and S ≈ 1,075 m², Eyring gives 0.62 s (Sabine 0.82 s); STI = 0.74 is a linear estimate, not an MTF value (DOI 10.1121/1.384464).

## Reference values stated in the essay
- **Eyring Reverberation T_60 (Model)**: `0.62 s (vs 1.85 s illustrative untreated)`
- **Speech Transmission Index (Illustrative)**: `0.74 (folio target ≥ 0.68)`
- **Early Clarity Index C_50 (Illustrative)**: `+4.8 dB`
- **Folio Design Targets (Model)**: `ILLUSTRATIVE VALUES VS FOLIO TARGETS (NOT MEASURED)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1121/1.1915175 (Scite report: https://scite.ai/reports/10.1121/1.1915175)
- What the essay compares against: Model values: V = 2,400 m³, S ≈ 1,075 m², α_bar = 0.44 → Eyring 0.62 s, Sabine 0.82 s

## Recent research context
- **Prime-Sequence Quadratic Residue Coffered Vaults: A Reverberation Model for Clearer Speech**: Pairing Eyring's reverberation formula (DOI 10.1121/1.1915175) with Schroeder diffuser geometry (DOI 10.1121/1.382601), this folio models a 2,400 m³ vault with estimated T_60 = 0.62 s and a clamped linear STI estimate of 0.74, beside frontier metasurface diffusers (Zhu et al. 2017, DOI 10.1103/PhysRevX.7.021034). It measured no room and makes no health claim.
