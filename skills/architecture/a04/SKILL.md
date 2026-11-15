---
name: archigram-hightech-exoskeleton
description: AI-agnostic architectural and structural engineering skill for Archigram Plug-In megastructures, British High-Tech exoskeletons (Foster, Rogers, Piano, Rice), gerberette cantilever statics, Maxwell-Calladine space-frame rigidity, and Stewart Brand shearing layers.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# From Archigram's Plug-In Megastructures to British High-Tech Exoskeletons: Gerberette Cantilevers, Maxwell Space Frames & Shearing-Layer Pods (Folio A.04)

A plain-text companion to the essay at https://informatico.ai/architecture/a04/ (`A.04 · Archigram to High-Tech Exoskeletons · CSI 05 12 13`, `REV 1.3`, redated `2026-11-14`).

## The governing relation
`T_tie = V_p · (a / c) · b − 3j + 6 = s − m · τ_pod ≪ τ_frame`

## Rules the essay derives
1. Evaluate cast-steel gerberette cantilever equilibrium: exterior tension tie force T_tie = V_floor * (a / c) and column compression C_col = V_floor * (1 + a / c).
2. Verify 3D space-frame static and kinematic determinacy via the Maxwell-Calladine matrix index b - 3j + 6 = s - m (ensuring m = 0 internal mechanisms).
3. Decouple Stewart Brand's 6 Shearing Layers by routing all Services (HVAC, medical gases, cleanroom exhaust, tau = 7-15 yr) on the exterior exoskeleton outside the 48 m column-free Structure (tau = 60-100 yr).

## How it works, in four stages
- Stage 1 (Archigram Plug-In Matrix, 1961–1964): Peter Cook's Plug-In City and Ron Herron's Walking City imagine a long-lived structural frame carrying short-lived clip-on capsules (the 100-year and 15-year lifetimes used here are the folio's illustrative values).
- Stage 2 (Pompidou Cast-Steel Gerberette Equilibrium, 1971–1977): In the folio's lever model, an assumed floor reaction V_p = 4,800 kN acts at a = 1.60 m outside the column and is balanced by an exterior tie: T_tie = V_p·(a/c) = 4,800 × 1.60 / 6.00 = 1,280.0 kN at c = 6.00 m. These are teaching values, not the loads of the real building.
- Stage 3 (Foster & Rogers High-Tech Mast Suspension, 1978–1986): Norman Foster (HSBC Hong Kong) hangs floors from masts, and Richard Rogers (Lloyd's of London) places service towers and prefabricated service pods outside the main floor plates.
- Stage 4 (Brand's Shearing Layers & Replaceable Service Modules): Stewart Brand describes building layers that change at different rates. Keeping services outside the long-life frame could, as a proposal, make it easier to replace clinical or laboratory service modules.

## Reference values stated in the essay
- **Exoskeleton Clear Span (Pompidou, as Reported)**: `About 48 m (column-free floors)`
- **Gerberette Tie-Rod Tension (Model)**: `1,280.0 kN (SF = 3.12, illustrative)`
- **Shearing-Layer Ratio (Illustrative)**: `τ_pod = 15 yr / τ_frame = 100 yr`
- **Maxwell-Calladine Index (Assumed)**: `m = 0 assumed, not computed`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/0020-7683(86)90014-4 (Scite report: https://scite.ai/reports/10.1016/0020-7683(86)90014-4)
- What the essay compares against: Model values: T_tie = 4,800 × 1.60 / 6.00 = 1,280 kN (V_p assumed) · SF 3.12 illustrative

## Recent research context
- **From Archigram's 1964 Plug-In Capsules to High-Tech Exoskeletons: A Lever Model of the Gerberette**: Connecting Peter Cook & Ron Herron's Archigram Plug-In drawings (1961–1974) with the Centre Pompidou's cast-steel gerberettes, Norman Foster's HSBC suspended floors, and the Pellegrino–Calladine counting rule for frameworks (Int. J. Solids Struct. DOI 10.1016/0020-7683(86)90014-4; Calladine DOI 10.1016/0020-7683(78)90052-5), this folio models the gerberette as a lever (T_tie = V_p a/c = 1,280.0 kN for assumed inputs) and proposes, without claiming any built example, frames whose service modules could be replaced.
