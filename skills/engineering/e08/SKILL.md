---
name: epb-tbm-peck-settlement
description: AI-agnostic geotechnical and tunneling civil engineering skill for EPB-TBM face pressure equilibrium, Peck-Mair Gaussian settlement troughs, and GNN subsurface digital twins.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Earth-Pressure-Balance Tunnel Boring Machines (EPB-TBM), Peck–Mair Gaussian Settlement Troughs & GNN Subsurface Digital Twins (Folio E.08)

A plain-text companion to the essay at https://informatico.ai/engineering/e08/ (`E.08 · EPB-TBM Tunneling & Peck–Mair Settlement · CSI 31 71 19`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`S(y) = S_max exp(−y² / 2i²) · V_s = V_L (π D² / 4) · i = K (z_0 − z) · CSI 31 71 19`

## Rules the essay derives
1. Compute trough inflection distance i = K * (z_0 - z) (K about 0.5 for clays at the surface, lower for sands; treat constant K below the surface as a simplification) and tunnel cross-sectional area A_t = pi * D^2 / 4.
2. Calculate centerline maximum settlement S_max = (V_L * A_t) / (sqrt(2 * pi) * i) and maximum transverse slope beta_max = 0.6065 * S_max / i at y = +/- i.
3. Verify EPB face pressure P_face stays between active collapse pressure sigma_h,active + u_0 and passive blowout pressure sigma_v0.

## How it works, in four stages
- Stage 1 (Chamber Balance, Anagnostou & Kovári 1996, DOI 10.1016/0886-7798(96)00017-X): At z_0 = 24.0 m, P_face = 210 kPa is an assumed point under stated assumptions, not a soil-profile check.
- Stage 2 (Soil Conditioning, Merritt & Mair 2006, DOI 10.1680/geot.2006.56.9.605; Budach & Thewes 2015, DOI 10.1016/j.tust.2015.08.006): Foam may condition clay or coarse ground in the screw conveyor; about 120 mm slump is illustrative.
- Stage 3 (Peck Trough, DOI 10.1680/geot.1993.43.2.315): V_L = 0.75% across D = 9.8 m gives V_s = 0.566 m³ per meter and S_max = 18.8 mm at i = 12.0 m.
- Stage 4 (Proposed GNN Twin): Torque and grout pressures could suggest updates to keep β_max < 1/500 (cf. Skempton & MacDonald 1956, DOI 10.1680/ipeds.1956.12202). Untested; no network was built.

## Reference values stated in the essay
- **Trough Inflection Width (i = K z_0)**: `12.0 m (K = 0.50, z_0 = 24 m)`
- **Centerline Max Settlement (S_max)**: `18.8 mm (at V_L = 0.75%)`
- **Max Trough Slope (β_max)**: `1 / 1,050 (< 1/500 model limit)`
- **Geotechnical TBM Verdict**: `WITHIN MODEL WINDOW (ASSUMED FACE BALANCE)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1680/geot.1993.43.2.315 (Scite report: https://scite.ai/reports/10.1680/geot.1993.43.2.315)
- What the essay compares against: D = 9.8 m · z_0 = 24.0 m · V_L = 0.75% ⇒ S_max = 18.8 mm

## Recent research context
- **Could Graph Neural Networks and Peck–Mair Gaussian Troughs Forecast Urban Settlement Ahead of the Cutterhead?**: Building on Peck (1969) and Mair, Taylor & Bracegirdle (1993, DOI 10.1680/geot.1993.43.2.315; Mair 2008, DOI 10.1680/geot.2008.58.9.695), this folio proposes feeding TBM torque, chamber pressure, and InSAR radar to a physics-constrained GNN. Default slope is 1/1,050; no network was trained.
