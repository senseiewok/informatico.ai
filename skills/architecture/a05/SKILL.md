---
name: tectonic-acoustics-sabine-eyring
description: AI-agnostic architectural acoustics skill for Sabine/Eyring reverberation, Schroeder QRD coffered vaults, and ISO 3382 Speech Transmission Index (STI).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Acoustic Sabin–Eyring Reverberation, Diffusive Coffered Vaults, and Speech Intelligibility (STI ≥ 0.68) (Folio A.05)

A plain-text companion to the essay at https://informatico.ai/architecture/a05/ (`A.05 · Architectural Acoustics · CSI 09 84 00`, `REV 1.1`, redated `2026-11-02`).

## The governing relation
`T_60 = 0.161V / [−S ln(1−α)] · STI = 0.74`

## Rules the essay derives
1. Compute both Sabine T_60 = 0.161 V / A and Eyring T_60 = 0.161 V / (-S ln(1 - alpha_bar)) across 125 Hz - 4 kHz octave bands.
2. Size Schroeder quadratic-residue diffuser wells via d_n = (n^2 mod p) * c / (2 p f_0) to prevent focal caustics under curved vaults.
3. Enforce STI >= 0.68 and background noise <= NC-28 in clinical consultation rooms and civic halls.

## How it works, in four stages
- Stage 1 (Direct & Early Reflections 0–50 ms): Vault geometry directs early energy to listeners within the 50 ms Haas integration window (C_50 = +4.8 dB).
- Stage 2 (Schroeder Quadratic-Residue Diffusion): Coffered timber wells of depth d_n = (n² mod p)·λ/(2p) scatter flutter echoes uniformly.
- Stage 3 (Micro-Perforated Helmholtz Absorption): 0.8 mm laser-drilled timber veneer over mineral wool achieves α_bar = 0.44 broadband absorption.
- Stage 4 (Eyring Decay & STI Verification): Certifies T_{60,Eyring} = 0.62 s and Speech Transmission Index STI = 0.74 (ISO 3382 Grade A).

## Reference values stated in the essay
- **Eyring Reverberation T_60**: `0.62 s (vs 1.85 s)`
- **Speech Intelligibility STI**: `0.74 (Excellent ≥ 0.68)`
- **Early Clarity Index C_50**: `+4.8 dB (NC-26)`
- **ISO 3382 / FGI Verdict**: `SAFE KERN & ACOUSTIC PASS`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1121/1.1901884 (Scite report: https://scite.ai/reports/10.1121/1.1901884)
- What the essay compares against: ISO 3382-1 · Schroeder Prime QRD Vaults

## Recent research context
- **Prime-Sequence Quadratic Residue Coffered Vaults Eliminate Clinical Alarm Fatigue**: Combining Carl Eyring's logarithmic reverberation law (JASA DOI 10.1121/1.1901884) with Manfred Schroeder's prime-sequence quadratic residue diffusers (QRD, JASA DOI 10.1121/1.380425) raises clinical consultation Speech Transmission Index to STI = 0.74, protecting pediatric CF patients from auditory strain.
