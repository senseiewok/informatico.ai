---
name: essay-es05-islands-blinders-conditional-survival
description: Verify Cross-Scale Essay ES.05 (Islands, Blinders, and Conditional Survival) on Informatico.ai - contrasting unitary Gauss-dressed QES saddle switching (DERIVED, 2.079 nats peak, 0% discard), CPTP undressed subalgebra blinders (PROPOSED arXiv:2602.06543, 4.159 nats, 0% discard), and Doob h-transform conditional survival across absorbing barriers (DERIVED, V_Doob = 1.726 nats, 82.20% discard at N = 6, gamma = 0.25) in harmonized nats.
license: CC0-1.0
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Islands, Blinders, and Conditional Survival (ES.05 · Cross-Scale Essay)

## 1. Essay identity, canonical URLs, and module paths
- **Essay code & slug**: `ES.05` · `islands-blinders-conditional-survival` (dated `2026-11-10`)
- **Canonical URL**: https://informatico.ai/essays/islands-blinders-conditional-survival/ (Spanish twin: https://informatico.ai/es-mx/essays/islands-blinders-conditional-survival/)
- **Physics kernel & bilingual monograph module**: `tools/folios/essays/e05_islands_conditional_survival.py`
- **Interactive client instrument**: `src/modules/cross-scale-essays.mjs` (`[data-cs-instrument="island_page"]`)
- **Standalone deterministic verifier**: `python -X utf8 skills/essays/islands-blinders-conditional-survival/verify_essay_islands_conditional_survival.py`
- **Planted-defect knockout check**: `python -X utf8 skills/essays/islands-blinders-conditional-survival/verify_essay_islands_conditional_survival.py --planted-defect` (must exit `1`)

## 2. Three distinct mathematical regimes in harmonized `nats` (`N = 6`)
1. **Regime 1 — Unitary Gauss-Dressed / QES Saddle Switch (`DERIVED`; `Page 1993a`, `Page 1993b`, `Almheiri et al. 2019`, `Penington 2020`)**:
   - Discrete generalized-entropy saddle competition: `S_gen(k) = min(k ln 2, (N − k) ln 2)` in `nats`.
   - At `N = 6`: the empty Hawking saddle `k ln 2` dominates for `k < 3`, meets the interior Island saddle `(6 − k) ln 2` at `k = 3` (`3 ln 2 ≈ 2.0794 nats`; Haar-random Page average `S_Page(8, 8) = Σ_{j=9}^{64} 1/j − 7/16 ≈ 1.5885 nats`), and returns strictly to `S_gen(6) = 0 nats` via trace-preserving unitary dynamics (`Tr ρ = 1`, `h(k) = 1`, `0%` discarded runs, `V_Doob = 0 nats`). Semiclassical replica wormholes and QES saddles are `DERIVED`, never `MEASURED`.
2. **Regime 2 — Subalgebra Coarse-Graining / "Detector Blinders" (`PROPOSED` preprint critique; `Geng et al. 2026`, `arXiv:2602.06543`)**:
   - Restricting a globally pure `2N = 12`-qubit (`4096`-dimensional, `S_global = 0 nats`) evaporation state to an undressed local radiation subalgebra `A_undressed` that omits long-range Gauss-law gravitational dressing applies a completely positive, trace-preserving (`CPTP`) partial trace: `0%` of runs are discarded (`Tr ρ_undressed = 1`, `V_Doob = 0 nats`), while hidden interior–radiation correlations raise the coarse-grained von Neumann entropy linearly to `6 ln 2 ≈ 4.1589 nats` at `k = 6`.
3. **Regime 3 — Doob `h`-Transform / Post-Selected Conditional Survival (`DERIVED` probability theorem; `Doob 1957`, `Chetrite & Touchette 2015`)**:
   - Across `N = 6` sequential checkpoints with per-step absorption hazard `γ ∈ (0, 1)`, the survival harmonic function is `h(k) = (1 − γ)^(N − k)` (`h(∂) = 0`, `(P h)(k) = h(k)`).
   - Conditioning on intact arrival at `k = N` tilts transitions by `P^h(k, k + 1) = P(k, k + 1) h(k + 1) / h(k) = 1`, achieving `100%` conditional arrival ONLY at path-space Kullback–Leibler cost `V_Doob = D_KL(ℙ^h ‖ ℙ) = −ln h(0) = −N ln(1 − γ) nats`.
   - At `N = 6, γ = 0.25`: `h(0) = (3/4)⁶ = 729 / 4096 ≈ 0.1780` (`82.20%` discarded trajectories, `5.62` raw launches per survivor), paying `V_Doob ≈ 1.7261 nats`. Physically lowering hazard to `γ_shielded = 0.05` (e.g., low-loss waveguides or in vitro modulation of premature stop checkpoints, `Sharma et al. 2018`, `Lee et al. 2022`) lifts true unconditioned survival `4.13×` to `73.51%` with `0%` post-selection bias and cuts conditional `V_Doob` `5.61×` to `0.3078 nats`.

## 3. Deterministic verification and falsification rules
1. Pure-Python Jacobi diagonalization on dense DCT-II rotated reduced density matrices matches `min(k, 6 − k) ln 2` across `k = 0..6` to `< 10⁻¹²` with `Tr ρ = 1`.
2. `2N = 12`-qubit (`4096`-state) CPTP subalgebra partial trace preserves `Tr ρ_undressed = 1` (`0%` discard, `V_Doob = 0`) while matching `k ln 2` (`4.1589 nats` at `k = 6`) to `< 10⁻¹²`.
3. Asymmetric `2⁶ = 64`-path branching survival tree confirms discrete harmonicity `|(P h)(k) − h(k)| < 10⁻¹⁵`, tilted stochasticity, and path-sum `D_KL(ℙ^h ‖ ℙ) = −6 ln(1 − γ)` to `< 10⁻¹⁴`.
4. Epistemic and proportional guardrails: `Geng et al. (2026)` stays `PROPOSED` (`0%` discard, never strawmanned as run-rejection), QES saddles stay `DERIVED` (never `MEASURED`), combined `CFTR / cystic fibrosis` prose mentions stay `≤ 3` (`< 12%` of `<p>` blocks, zero clinical claims), `8–10` DOIs resolve offline in `data/folio-citations.cache.json`, and `100%` EN / `es-MX` numeric token parity holds.
5. **Planted-defect gate (`--planted-defect`)**: disables the `k > 3` island turnover, sets `V_Doob = 0` on `γ = 0.25` post-selection, strawmans Regime 2 as run-rejection, and promotes unmeasured saddles to `MEASURED`; the verifier exits `1`.

## 4. Primary DOIs verified offline (`data/folio-citations.cache.json`)
| Source ID | Reference | DOI |
| --- | --- | --- |
| `ES05-DOOB1957` | Doob (1957), *Bull. Soc. Math. France* | https://doi.org/10.24033/bsmf.1494 |
| `ES05-PAGE1993A` | Page (1993a), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.71.1291 |
| `ES05-PAGE1993B` | Page (1993b), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.71.3743 |
| `ES05-CHETRITE2015` | Chetrite & Touchette (2015), *Ann. Henri Poincaré* | https://doi.org/10.1007/s00023-014-0375-8 |
| `ES05-SHARMA2018` | Sharma et al. (2018), *PLOS Genetics* | https://doi.org/10.1371/journal.pgen.1007723 |
| `ES05-ALMHEIRI2019` | Almheiri, Engelhardt, Marolf & Maxfield (2019), *JHEP* | https://doi.org/10.1007/jhep12(2019)063 |
| `ES05-PENINGTON2020` | Penington (2020), *JHEP* | https://doi.org/10.1007/jhep09(2020)002 |
| `ES05-LEE2022` | Lee et al. (2022), *J. Clin. Invest.* | https://doi.org/10.1172/JCI154571 |
| `ES05-GENG2026` | Geng et al. (2026), *arXiv preprint* (`PROPOSED`) | https://doi.org/10.48550/arxiv.2602.06543 |
