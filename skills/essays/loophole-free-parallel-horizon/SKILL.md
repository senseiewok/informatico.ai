---
name: essay-es07-loophole-free-parallel-horizon
description: Verify Cross-Scale Essay ES.07 (The Parallel Horizon and The Loophole-Free Quantum Island) - closed-form 2-D and 3-D skewed Diósi-Penrose parallel hybrid block diagonalization, 1.5471 sigma to 2.2109 sigma horizon expansion, 73.14 um Eöt-Wash ceiling, D = 75 um quantum island, 4 cryogenic vacuum ensembles, 90-degree midpoint null control, and 9 zero-sorry core Lean 4 theorems.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# The Parallel Horizon & The Loophole-Free Quantum Island: Exact Bounds, Cryogenic Valleys, and Why This Is Not a Theory of Everything (`ES.07` · Cross-Scale Essay)

## 1. Essay identity, canonical URLs, and owned artifacts
- **Essay code & slug**: `ES.07` · `loophole-free-parallel-horizon` (dated `2026-11-10`, plate `essay07`, instrument `parallel_horizon`)
- **Canonical URL**: https://informatico.ai/essays/loophole-free-parallel-horizon/ (Spanish twin: https://informatico.ai/es-mx/essays/loophole-free-parallel-horizon/)
- **Physics kernel & bilingual monograph module**: `tools/folios/essays/e07_parallel_hybrid_horizon.py` (coupled to `tools/timegravity_kernel_dispute.py`)
- **Companion zero-sorry formal specification**: `skills/essays/loophole-free-parallel-horizon/ParallelHorizon.lean` (pure core Lean 4 Prelude, zero external imports)
- **Standalone deterministic verifier**: `python -X utf8 skills/essays/loophole-free-parallel-horizon/verify_essay_parallel_horizon.py`
- **Planted-defect knockout check**: `python -X utf8 skills/essays/loophole-free-parallel-horizon/verify_essay_parallel_horizon.py --planted-defect` (must exit `1`)

## 2. Five coupled physics & epistemic pillars
1. **Closed-Form 2-D & 3-D Skewed Parallel Hybrid Block Diagonalization (`Diósi 1987`; `Peres 1996`; `Trillo & Navascués 2025`)**:
   - Midpoint-centred branches `(0, ∓Δx/2, 0)` and `(D, ∓(Δx/2)cos θ, ∓(Δx/2)sin θ)` reduce all inter-particle distances to `r_same(θ) = √(D² + ½ Δx²(1 − cos θ))` and `r_diff(θ) = √(D² + ½ Δx²(1 + cos θ))`, block-diagonalizing the `4 × 4` partial-transpose matrix into two `2 × 2` blocks with `0 ≤ b(θ) ≤ a ≤ ã`.
   - Yields an overflow-free closed form for `N_hyb(t)` across all `t ∈ [0, ∞)` (matching `4 × 4` matrix diagonalization to `< 10⁻¹³`) and the exact critical environmental dephasing threshold `γ_crit^hyb = (G m² / ħ) max(0, √2 b − a)`.
2. **Universal Parallel Horizon Expansion (`1.5471 σ` to `2.2109 σ`) & `D = 75 µm` Quantum Island (`Lee et al. 2020`; `Van De Kamp et al. 2020`; `Sellner et al. 2017`)**:
   - Unlike collinear interferometers where `d_c / σ` shrinks from `0.8509` to `0`, the parallel hybrid horizon expands monotonically from `D_{c,0} = 1.547134 σ` (`σ_c / D = 0.6464`) at small splits to `D_{c,∞} = 2.210928 σ` (`σ_c / D = 0.4523`) as `Δx / σ → ∞`.
   - Under the `σ_95 = 33.08 µm` signed Yukawa recast of Lee et al. (2020), every parallel gap `D ≥ 73.14 µm` (`73.18 µm` at `33.1 µm`) forces `N_hyb(t) = 0` identically for all splits and hold times, exposing the `D = 60 µm` small-split extrapolation trap (`σ_c = 31.65 µm`) and opening a clean corridor above the `28.29 µm` Casimir + `2R` wall at `10⁻¹⁴ kg` (`N_Q = 0.4302..0.4902` at `D = 75 µm, Δx = 250 µm, t = 2.5 s`) that pinches shut at `10⁻¹² kg` (`73.30 µm > 73.14 µm`).
3. **Four Cryogenic Ensembles & Hardware-Free `θ = 90°` Null Control**:
   - Contrasts isobaric (`P = const`, analytical valley `T* = 2.04 K` at `2.7 × 10⁻¹⁶ Pa` and `2.50 K` at `10⁻¹⁵ Pa`), sealed isochoric (`n = const`), Knudsen (`P / √T = const`), and cryo-pumped (`P_vap(T)`) vacuum ensembles.
   - Rotating one Stern–Gerlach axis to `θ = 90°` about its midpoint (`+` cross) equates `r_same = r_diff = 192.03 µm`, cancelling central pair potentials to all multipole orders (contrasted with the uncentred corner-aligned `+(3/4) Δx⁴ / D⁵` trap, `1.335 rad`).
4. **Four Sharp Epistemic Boundaries (Why This Is Not a Theory of Everything)**:
   - Separates weak-field IR Newtonian superposition from Planck-scale UV completion, distinguishes `σ`-smeared / Markovian diffusive bounds (`Oppenheim et al. 2023`) from higher-order matter-vertex couplings (`Aziz & Howl 2025`), separates published-table recasting from a raw 95-run Eöt-Wash refit, and enforces `DERIVED (NOT MEASURED)` provenance.
5. **Nine Zero-`sorry` Core Lean 4 Prelude Theorems (`ParallelHorizon.lean`; `Tooby-Smith 2025`)**:
   - Certifies `6` SI dimensional equations, partial-transpose discriminant positivity, `3-D` skewed midpoint difference (`r_diff² − r_same² = Δx² cos θ`), `θ = 90°` all-multipole nullity, uncentred `+6 Δx⁴` Taylor residue, `3(k+2)⁴ < (k+2)⁸`, dephasing monotonicity, and the `10⁻¹⁵..10⁻¹² kg` mass pinch.

## 3. Primary Crossref DOIs verified offline (`13 / 13` cached)
| Source ID | Reference | DOI |
| --- | --- | --- |
| `ES07-LINDBLAD1976` | Lindblad (1976), *Commun. Math. Phys.* | https://doi.org/10.1007/bf01608499 |
| `ES07-DIOSI1987` | Diósi (1987), *Phys. Lett. A* | https://doi.org/10.1016/0375-9601(87)90681-5 |
| `ES07-PERES1996` | Peres (1996), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.77.1413 |
| `ES07-SELLNER2017` | Sellner et al. / BASE (2017), *New J. Phys.* | https://doi.org/10.1088/1367-2630/aa7e73 |
| `ES07-BOSE2017` | Bose et al. (2017), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.119.240401 |
| `ES07-MARLETTO2017` | Marletto & Vedral (2017), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.119.240402 |
| `ES07-LEE2020` | Lee et al. / Eöt-Wash (2020), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.124.101101 |
| `ES07-VANDEKAMP2020` | Van De Kamp et al. (2020), *Phys. Rev. A* | https://doi.org/10.1103/physreva.102.062807 |
| `ES07-OPPENHEIM2023` | Oppenheim et al. (2023), *Nat. Commun.* | https://doi.org/10.1038/s41467-023-43348-2 |
| `ES07-SCHUT2024` | Schut et al. (2024), *Phys. Rev. Research* | https://doi.org/10.1103/physrevresearch.6.013199 |
| `ES07-TRILLO2025` | Trillo & Navascués (2025), *Phys. Rev. D* | https://doi.org/10.1103/physrevd.111.l121101 |
| `ES07-AZIZ2025` | Aziz & Howl (2025), *Nature* | https://doi.org/10.1038/s41586-025-09595-7 |
| `ES07-TOOBYSMITH2025` | Tooby-Smith / HepLean (2025), *Comput. Phys. Commun.* | https://doi.org/10.1016/j.cpc.2024.109457 |
