---
name: wkb-quantum-tunneling-catalysis
description: AI-agnostic physics skill for WKB quantum barrier penetration, Bell parabolic tunneling corrections, Marcus reorganization energy, and enzymatic Kinetic Isotope Effects (KIE).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Quantum WKB Barrier Penetration, Proton-Coupled Electron Transfer, and Deaminase Base-Editing Catalysis (Folio P.05)

A plain-text companion to the essay at https://informatico.ai/physics/p05/ (`P.05 · Quantum & Chemical Physics`, `REV 1.1`, redated `2026-11-02`).

## The governing relation
`T_WKB ~ exp(−2/ℏ ∫√(2m(V−E))dx) · k_H/k_D = 6.84`

## Rules the essay derives
1. Compute WKB barrier transmission as T(E) = exp(-2/hbar * integral sqrt(2 m (V(x) - E)) dx) between classical turning points x_1 and x_2.
2. Apply the Bell tunneling factor kappa_tun = (u_b / 2) / sin(u_b / 2) with u_b = hbar * omega_b / (k_B T) to Eyring-Kramers transition-state rates.
3. Evaluate primary H/D Kinetic Isotope Effects (k_H / k_D) to distinguish quantum proton tunneling from classical over-the-barrier activation.

## How it works, in four stages
- Stage 1 (Marcus Environmental Reorganization λ): Thermal fluctuations align solvent and catalytic zinc dipoles to bring donor and acceptor orbitals into degeneracy.
- Stage 2 (Promoting Vibration Donor-Acceptor Compression): Picosecond protein breathing modes compress the hydrogen-bond bridge from 2.90 Å to 2.58 Å (Δx = 0.52 Å).
- Stage 3 (WKB Semiclassical Wave Penetration): Proton wavefunction tunnels through the 16.4 kcal/mol barrier with Bell correction κ_tun = (u_b/2)/sin(u_b/2) and KIE k_H/k_D = 6.84.
- Stage 4 (TadA-8e Adenine Deamination Lock): Converts target adenosine to inosine (read as guanosine), restoring canonical CFTR splicing at 1717-1G>A.

## Reference values stated in the essay
- **Tunneling Coupling Efficiency**: `0.88 (WT-Coupled)`
- **Kinetic Isotope Ratio k_H/k_D**: `6.84 (WKB Verified)`
- **Barrier Width Δx**: `0.52 Å (42× Boost)`
- **Catalytic Regime**: `STABLE_COUPLED_CYCLE`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1103/RevModPhys.35.724 (Scite report: https://scite.ai/reports/10.1103/RevModPhys.35.724)
- What the essay compares against: Gamow 1928 · Marcus 1956 · DOI 10.1103/RevModPhys.35.724

## Recent research context
- **Quantum Mechanical Proton Tunneling & Kinetic Isotope Effects Guide High-Fidelity Adenine Base Editing**: Coupling Gamow–WKB quantum tunneling with Löwdin's proton-transfer tautomeric model (Rev. Mod. Phys. DOI 10.1103/RevModPhys.35.724), engineered TadA deaminases and prime editors (Cell Reports Medicine DOI 10.1016/j.xcrm.2024.101544) correct stop-codon and splice-site CFTR mutations in patient-derived organoids without double-strand DNA breaks.
