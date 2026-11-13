---
name: epb-tbm-peck-settlement
description: AI-agnostic geotechnical and tunneling civil engineering skill for EPB-TBM face pressure equilibrium, Peck-Mair Gaussian settlement troughs, and GNN subsurface digital twins.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Earth-Pressure-Balance Tunnel Boring Machines (EPB-TBM), Peck–Mair Gaussian Settlement Troughs & GNN Subsurface Digital Twins (Folio E.08)

A plain-text companion to the essay at https://informatico.ai/engineering/e08/ (`E.08 · EPB-TBM Tunneling & Peck–Mair Settlement · CSI 31 71 19`, `REV 1.0`, redated `2026-11-02`).

## The governing relation
`S(y) = S_max exp(−y² / 2i²) · V_s = V_L (π D² / 4) · i = K (z_0 − z) · CSI 31 71 19`

## Rules the essay derives
1. Compute trough inflection distance i = K * (z_0 - z) (with K = 0.50 for clays, 0.25-0.35 for sands) and tunnel cross-sectional area A_t = pi * D^2 / 4.
2. Calculate centerline maximum settlement S_max = (V_L * A_t) / (sqrt(2 * pi) * i) and maximum transverse slope beta_max = 0.6065 * S_max / i at y = +/- i.
3. Verify EPB face pressure P_face stays between active collapse pressure sigma_h,active + u_0 and passive blowout pressure sigma_v0.

## How it works, in four stages
- Stage 1 (Anagnostou–Kovári Chamber Pressure Balance): At depth z_0 = 24.0 m, EPB chamber pressure P_face = 210 kPa balances lateral earth + pore water pressure without passive blowout.
- Stage 2 (Foam-Conditioned Muck Rheology): Surfactant-polymer foam injection transforms excavated clay into a cohesive, low-permeability plastic paste (slump 120 mm) across the screw conveyor.
- Stage 3 (Peck–Mair Subsurface Gaussian Propagation): Volume loss V_L = 0.75% across D = 9.8 m creates a trough of inflection width i = K z_0 = 12.0 m and centerline S_max = 18.8 mm.
- Stage 4 (Graph Neural Network Subsurface Digital Twin): Real-time cutterhead torque and tail-void grout pressures update the GNN mesh to hold angular distortion β_max < 1/500 beneath historic masonry.

## Reference values stated in the essay
- **Trough Inflection Width (i = K z_0)**: `12.0 m (K = 0.50, z_0 = 24 m)`
- **Centerline Max Settlement (S_max)**: `18.8 mm (at V_L = 0.75%)`
- **Max Angular Distortion (β_max)**: `1 / 1,050 (< 1/500 Limit)`
- **Geotechnical TBM Verdict**: `FACE STABLE · RANKINE PASS`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1680/geot.1993.43.2.315 (Scite report: https://scite.ai/reports/10.1680/geot.1993.43.2.315)
- What the essay compares against: D = 9.8 m · z_0 = 24.0 m · V_L = 0.75% ⇒ S_max = 18.8 mm

## Recent research context
- **Graph Neural Networks & Peck–Mair Gaussian Troughs Prevent Urban Settlement Ahead of the Cutterhead**: Building on Ralph Peck's (1969) and Mair, Taylor & Bracegirdle's (Géotechnique DOI 10.1680/geot.1993.43.2.315) Gaussian subsurface settlement theory, modern Earth-Pressure-Balance Tunnel Boring Machines fuse real-time cutterhead torque, chamber pressure, and InSAR satellite radar into physics-constrained Graph Neural Networks to hold urban building distortion below 1/1,000.
