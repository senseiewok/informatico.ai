---
name: self-healing-concrete-washburn-calcite
description: AI-agnostic civil materials engineering skill for Lucas-Washburn capillary crack imbibition, Fickian-Michaelis-Menten bacterial CaCO3 precipitation, cubic Poiseuille permeability cutoff, and Coda-Wave Interferometry.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Autogenous Bacterial & Crystalline Self-Healing Concrete: Lucas–Washburn Capillary Imbibition, Fickian–Michaelis–Menten Calcite Precipitation & Ultrasonic Coda-Wave Digital Twins (Folio E.09)

A plain-text companion to the essay at https://informatico.ai/engineering/e09/ (`E.09 · Self-Healing Bio-Concrete · CSI 03 30 00`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`z(t) = √(γ r cos θ · t / 2μ) · ∂C/∂t = D_eff ∇²C − V_max C/(K_m + C) · CSI 03 30 00`

## Rules the essay derives
1. Compute Lucas-Washburn capillary penetration depth z(t) = sqrt((gamma * w_0 * cos(theta) / (4 * mu)) * t) for crack aperture w_0.
2. Integrate crack-closure kinetics dw/dt = -2 * V_m * V_max * [Ca2+] / (K_m + [Ca2+]) and evaluate cubic Poiseuille leakage ratio (w_rem / w_0)^3.
3. Treat the healing limit w_0 <= 0.45 mm and any Coda-Wave Interferometry recovery target as project design assumptions to be tested, not as values taken from a standard.

## How it works, in four stages
- Stage 1 (Lucas–Washburn Capillary Imbibition): A flexural microcrack of width w_0 = 0.30 mm, treated as a parallel-plate channel (r = w_0/2), draws moisture to depth z(t) = √(γ w_0 cos θ · t / 4μ), wetting embedded bacterial spores.
- Stage 2 (Spore Germination & Lactate-to-Calcite Conversion): Alkali-resistant bacteria metabolize calcium lactate, and calcium carbonate precipitates along the crack walls (the mechanism tested by Jonkers et al. 2010).
- Stage 3 (Cubic Parallel-Plate Flow, Q ∝ w³): In this model, narrowing w from 0.30 mm to an illustrative 0.018 mm (94.0% closure) gives (0.018/0.30)³ = 2.2 × 10⁻⁴, a 99.98% cut in idealized laminar flow. Real healed cracks are rough and partly filled, so this is an upper-bound idealization.
- Stage 4 (Ultrasonic Coda-Wave Interferometry): Multiply scattered ultrasonic coda waves are sensitive to very small relative velocity changes Δv/v, so CWI could be used to track stiffness recovery; the 96.4% recovery index shown in the lab is an illustrative model value, not a measurement.

## Reference values stated in the essay
- **Calcite Crack Closure (model, η_seal)**: `94.0% (w_rem = 0.018 mm, illustrative)`
- **Cubic Flow Reduction (w³ model)**: `−99.98% (idealized)`
- **Stiffness Recovery Index (model)**: `96.4% (illustrative)`
- **Model Healing Status**: `SEALED IN MODEL · design target w_0 ≤ 0.45 mm`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/j.ecoleng.2008.12.036 (Scite report: https://scite.ai/reports/10.1016/j.ecoleng.2008.12.036)
- What the essay compares against: Model: w_0 = 0.30 mm → w_rem = 0.018 mm (94.0% closure, illustrative) ⇒ (0.018/0.30)³ = 2.2 × 10⁻⁴ ⇒ −99.98% parallel-plate flow (w³ law)

## Recent research context
- **Capillary Imbibition & Dormant Bacillus Spores: A Model of Self-Sealing Concrete Microcracks**: Continuing the capillary pore mechanics of Folio E.01 and the structural monitoring of Folio E.07, this folio models bacterial self-healing concrete in the line of Jonkers et al. (Ecol. Eng. 2010, DOI 10.1016/j.ecoleng.2008.12.036) and proposes coda-wave monitoring. In its illustrative model, 94% closure of a 0.30 mm crack cuts ideal parallel-plate flow by 99.98%.
