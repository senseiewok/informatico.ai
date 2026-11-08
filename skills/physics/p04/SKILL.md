---
name: periciliary-osmotic
description: AI-agnostic physical skill for Nernst-Planck electrokinetics, Donnan membrane equilibrium, and periciliary liquid layer hydration balance.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Electrokinetics, Donnan Equilibrium, and the Catastrophic Osmotic Collapse of the Periciliary Layer (Folio P.04)

## 1. Governing Law & Tectonic Identity
- **Folio**: `P.04 · Electrokinetics & Osmosis` (`REV 1.2`, Redated `2026-11-02`)
- **Governing Equation**: `J_k = −D_k (∇c_k + (z_k F / RT) c_k ∇Φ) · dh_PCL/dt = L_p (ΔΠ_osm − ΔP_hydro)`
- **Primary Verification Kernel**: `skills/physics/p04/verify_p04.py`
- **Verification Benchmarks**: `Ussing Chamber Short-Circuit Currents (I_sc) · PCL Optical Micro-OCT`
- **Primary Scite Anchor DOI**: https://doi.org/10.1126/science.1223012 (Scite Report: https://scite.ai/reports/10.1126/science.1223012)

## 2. Deterministic Verification & Falsification Rules
1. Balance apical Cl- secretion against basolateral Na/K ATPase and ENaC uptake. 2. Verify PCL steady-state thickness h_PCL >= 6.5 μm for healthy classification. 3. Flag osmotic collapse when net solute reabsorption exceeds 1.5 μEq/(cm^2*h).

## 3. 4-Stage Physical & Mathematical Mechanism
- Stage 1 (Hydrated Epithelium): CSI-MasterFormat Cl^- secretion balances ENaC Na^+ absorption, maintaining PCL osmotic equilibrium (h ≈ 7.0 μm).
- Stage 2 (CSI-MasterFormat Defect & Unchecked ENaC): Loss of Cl^- permeability and 2.5x ENaC activity creates a net hyperosmolar reabsorptive drive.
- Stage 3 (Osmotic Desiccation): Trans-epithelial water flux drains the periciliary space, causing osmotic pressure to rise from 0.7 to 2.5 kPa.
- Stage 4 (Grafted Brush Compression): Tethered cell-surface mucins (MUC1, MUC4, MUC16) collapse under mechanical compression, permanently disabling clearance.

## 4.