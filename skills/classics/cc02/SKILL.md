---
name: classics-cc02-sagrada-stereotomy
description: Rebuild and verify the CC.02 Stereotomy & Mechanics Lab (La Sagrada Família feature on informatico.ai) — doubly-ruled one-sheet hyperboloid straightness, hanging catenary vs. parabola equilibrium & column tilt angle, double-twisted 6/8/10/12 star column Boolean cross-sections, post-tensioned stone panel decompression, and 1936 plaster-shard algebraic hyperboloid recovery vs. freeform drift — using a standard-library Python verifier that checks the published English and Spanish pages and exits non-zero under five planted defects.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# One Stone Forest, Eight Moves · Stereotomy & Mechanics Lab (CC.02)

> **Boundary (`EN`):** Independent educational monograph. Values labeled MODEL illustrate geometric and structural mechanisms only and are not engineering calculations for construction. Basilica dimensions are attributed to Basílica de la Sagrada Família; post-tensioned panel systems are attributed to Ingenia / Arup; peer-reviewed papers were checked in Crossref and Scite on 2026-11-15 with zero retractions.
>
> **Límite (`ES-MX`):** Monografía educativa independiente. Los valores marcados MODELO ilustran mecanismos geométricos y estructurales únicamente y no constituyen dictámenes ni cálculos de obra. Las dimensiones de la Basílica se atribuyen a Basílica de la Sagrada Família; los paneles pretensados a Ingenia / Arup; los artículos arbitrados se verificaron en Crossref y Scite el 2026-11-15 sin retractaciones.

## 1. Page and files
- **Page**: https://informatico.ai/classics/sagrada-familia/#part-6 (Spanish: https://informatico.ai/es-mx/classics/sagrada-familia/#part-6)
- **Models**: `tools/folios/classics/cc02_mechanics.py` (used by the page builder)
- **Content and data**: `tools/folios/classics/cc02.py` (eight historical moves, five generations relay, 41 sources, copy)
- **Builder**: `python -X utf8 tools/build_sagrada_masterpiece.py`
- **Verifier**: `python -X utf8 skills/classics/cc02/verify_cc02_sagrada.py`
- **Knockouts** (each must exit non-zero):
  - `--planted-defect` (default `non-tangent-ruling`): twists the straight ruling off the quadric shell so `(x/a)² + (y/b)² − (z/c)² = 1` breaks
  - `--planted-defect=parabola-catenary`: substitutes a quadratic parabola for the self-weight catenary, breaking arc-weight equilibrium and page gap values
  - `--planted-defect=twist-pinch`: applies co-rotating instead of counter-rotating twist to the star prisms, breaking intersection area and stress tables
  - `--planted-defect=unprestressed-wind`: removes post-tensioning force `F_pt = 0`, driving windward joint stress `σ_min` into tension
  - `--planted-defect=shard-freeform`: substitutes local unruled quadratic Taylor extrapolation around the surviving `0.35 m` plaster shard instead of solving global `r²(z) = a² + (a²/c²)·z²`, blowing up rim drift to `311.6 mm` even at zero caliper noise

## 2. Governing equations
- **One-sheet hyperboloid straight ruling**: `r(u, v) = (a(cos u − s·v·sin u), b(sin u + s·v·cos u), v·c)`, `s ∈ {+1, −1}`, lying on `(x/a)² + (y/b)² − (z/c)² = 1`
- **Self-weight catenary with crown lantern `W_top`**: `y(x) = a·[cosh(L/(2a) + α₀) − cosh(|x|/a + α₀)]`, `α₀ = arcsinh(W_top / (2H))`, `V = H·sinh(L/(2a) + α₀)`, column tilt from vertical `θ = arctan(H / V)`
- **Counter-rotating star columns (`n ∈ {6, 8, 10, 12}`)**: `H_total = 2n` m, `H_shaft = 10·D_in`, Boolean intersection `P₁(+θ) ∩ P₂(−θ)` over `θ ∈ [0, π/(2n)]`
- **Post-tensioned tower panel extreme fiber stress**: `σ_min = (F_pt + N_dead) / A_net − M_wind / Z_net ≥ 0`
- **1936 shard algebraic recovery**: `r²(z) = a² + k·z²` with `k = a² / c²`, solved via Vandermonde `2×2` elimination from `(z₁, r₁ ± δr)` and `(z₂, r₂ ∓ δr)`

## 3. How to use this with any AI
Edit a MODEL parameter in `cc02_mechanics.py`, rebuild both language pages, update `PINNED_SHA256` after review, and run `verify_cc02_sagrada.py` alongside all five `--planted-defect` knockouts.
