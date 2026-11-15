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
1. Compute both Sabine T_60 = 0.161 V / A and Eyring T_60 = 0.161 V / (-S ln(1 - alpha_bar)) across 125 Hz - 4 kHz octave bands.
2. Size Schroeder quadratic-residue diffuser wells via d_n = (n^2 mod p) * c / (2 p f_0) to prevent focal caustics under curved vaults.
3. Use the folio's own design targets of STI >= 0.68 and background noise <= NC-28 for consultation rooms and civic halls (folio targets, not requirements of a cited standard).

## How it works, in four stages
- Stage 1 (Direct & Early Reflections 0–50 ms): Vault geometry directs early energy to listeners within the first 50 ms (an illustrative early clarity C_50 = +4.8 dB, not computed here).
- Stage 2 (Schroeder Quadratic-Residue Diffusion): Coffered timber wells of depth d_n = (n² mod p)·λ/(2p) spread reflections across many directions instead of one mirror-like bounce.
- Stage 3 (Micro-Perforated Helmholtz Absorption): 0.8 mm perforated timber veneer over mineral wool, with an assumed mean absorption α_bar = 0.44.
- Stage 4 (Eyring Decay): For V = 2,400 m³ and an assumed surface area S ≈ 1,075 m², T_60,Eyring = 0.161 × 2,400 / (−1,075 × ln 0.56) = 0.62 s (Sabine gives 0.82 s). The STI of 0.74 is an illustrative value, not a measurement.

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
- **Prime-Sequence Quadratic Residue Coffered Vaults: A Reverberation Model for Clearer Speech**: Combining Carl Eyring's logarithmic reverberation law (JASA DOI 10.1121/1.1915175) with Manfred Schroeder's prime-sequence quadratic residue diffusers (JASA DOI 10.1121/1.382601), this folio models a 2,400 m³ vault with T_60 = 0.62 s and shows an illustrative Speech Transmission Index of 0.74. It measured no room and makes no health claim.
