---
name: archigram-hightech-exoskeleton
description: Explanatory architectural and statics reference (not a structural design method) for cast-steel gerberette lever equilibrium, the Maxwell-Calladine counting rule, and Stewart Brand shearing layers; no number here may be used on a real structure.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# From Archigram's Plug-In Megastructures to British High-Tech Exoskeletons: Gerberette Cantilevers, Maxwell Space Frames & Shearing-Layer Pods (Folio A.04)

A plain-text companion to the essay at https://informatico.ai/architecture/a04/ (`A.04 · Archigram to High-Tech Exoskeletons · Teaching Model`, `REV 1.3`, redated `2026-11-14`).

## The governing relation
`T_tie = V_p · (a / c) · b − 3j + 6 = s − m · τ_pod ≪ τ_frame`

## Rules the essay derives
1. Explanatory, untested model only, not a structural design method (no number here may be used on a real structure): under assumed V_p = 4,800 kN, compute T_tie = V_p * (a / c) and C_col = V_p * (1 + a / c), with browser surrogate SF = 3.12 * (1,280 / max(100, T_tie)) flagging SF < 1.50 above 2,662.4 kN.
2. State the 3D Maxwell-Calladine count b - 3j + 6 = s - m (Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4); here m = 0, about 48 m clear span, and 15 yr / 100 yr lifetimes remain fixed reference text, not verified matrix outputs.
3. Treat separating shorter-lived services (about 7-15 yr in Brand 1994) from long-lived structure (about 30-300 yr in Brand 1994; Habraken 2021, DOI 10.4324/9781003014713) as an untested concept caveat, not a facility code.

## How it works, in four stages
- Stage 1 (Archigram Plug-In Matrix, 1961–1964): Cook's Plug-In City and Herron's Walking City depict a frame carrying replaceable capsules (Beslioglu 2014, DOI 10.4995/vlc.2014.1829; the 100-year and 15-year lifetimes are fixed illustrative values).
- Stage 2 (Pompidou Gerberette Lever, 1971–1977): Under the stated assumptions (V_p = 4,800 kN, a = 1.60 m, c = 6.00 m), T_tie = V_p·(a/c) = 1,280.0 kN and C_col = 6,080.0 kN (illustrative values, not real building loads).
- Stage 3 (Foster & Rogers Perimeter Structure, 1978–1986): Norman Foster (HSBC Hong Kong) hangs floors from masts, and Richard Rogers (Lloyd's) places service towers outside main floor plates.
- Stage 4 (Brand's Shearing Layers): Stewart Brand (1994) separates long-lived frames from faster-aging services; placing replaceable service pods outside the frame could remain an untested architectural proposal.

## Reference values stated in the essay
- **Exoskeleton Clear Span (Reported)**: `About 48 m (fixed reference text)`
- **Gerberette Tie-Rod Tension (Model)**: `1,280.0 kN (SF = 3.12, illustrative)`
- **Shearing-Layer Ratio (Illustrative)**: `τ_pod = 15 yr / τ_frame = 100 yr (fixed text)`
- **Rigidity & Surrogate Tie Check**: `m = 0 assumed (fixed) · SF ≥ 1.50 (illustrative)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/0020-7683(86)90014-4 (Scite report: https://scite.ai/reports/10.1016/0020-7683(86)90014-4)
- What the essay compares against: Assumed & illustrative values: T_tie = 4,800 × 1.60 / 6.00 = 1,280.0 kN (V_p assumed) · SF = 3.12 illustrative

## Recent research context
- **From Archigram's 1964 Plug-In Capsules to High-Tech Exoskeletons: A Lever Model of the Gerberette**: Connecting Cook & Herron's Plug-In drawings (Beslioglu 2014, DOI 10.4995/vlc.2014.1829) with Centre Pompidou gerberettes (Hamzeian 2018, DOI 10.1201/9780429506208-91) and Pellegrino–Calladine counting (DOI 10.1016/0020-7683(86)90014-4), this untested explanation estimates T_tie = 1,280.0 kN under stated assumptions; no figure belongs on a real structure.
