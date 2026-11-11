---
name: essay-es11-seven-gate-crown-sieve
description: Verify Cross-Scale Essay ES.11 (The Seven-Gate Crown Sieve) - Geng-Marshak-Fermat cubic hypercharge anomaly lock vs Minahan-Ramond-Warner irrational e = 54^(1/3) branch, Jackiw-Rebbi / Kaplan domain-wall Spin(10) chirality, 88.11 um Planck 2018 dark-energy horizon scale and Jacobson null-ray vacuum decoupling, Biswas et al. Weierstrass entire exp(l_*^2 q^2) -> erf(r / 2 l_*) UV gravity bounded at l_* < 32.98 um, 8 x 7 crown sieve, and 12 zero-sorry core Lean 4 Prelude theorems.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# The Seven-Gate Crown Sieve: Chiral Anomaly Locks, the 88.11 µm Vacuum Scale, and Ghost-Free Entire Gravity (`ES.11` · Cross-Scale Essay)

## 1. Essay identity, canonical URLs, and owned artifacts
- **Essay code & slug**: `ES.11` · `seven-gate-crown-sieve` (dated `2026-11-11`, plate `essay11`, instrument `seven_gate_crown`)
- **Canonical URL**: https://informatico.ai/essays/seven-gate-crown-sieve/ (Spanish twin: https://informatico.ai/es-mx/essays/seven-gate-crown-sieve/)
- **Interactive observatory module**: `src/modules/cross-scale-essays.mjs` (`data-cs-instrument="seven_gate_crown"`)
- **Physics kernel & bilingual monograph module**: `tools/folios/essays/e11_seven_gate_crown.py` (coupled strictly to `timegravity_kernel.py`, `timegravity_kernel_isl.py`, `timegravity_kernel_recast.py`, `timegravity_kernel_wedge.py`, `timegravity_kernel_decoherence.py`, `timegravity_kernel_dispute.py`, and `timegravity_kernel_entangle.py`)
- **Companion zero-sorry formal specification**: `skills/essays/seven-gate-crown-sieve/SevenGateCrown.lean` (pure core Lean 4 Prelude, zero external imports, `namespace Informatico.Essays.ES11`)
- **Standalone deterministic verifier**: `python -X utf8 skills/essays/seven-gate-crown-sieve/verify_essay_seven_gate_crown.py`
- **Planted-defect knockout check**: `python -X utf8 skills/essays/seven-gate-crown-sieve/verify_essay_seven_gate_crown.py --planted-defect` (must exit `1`)

## 2. Five coupled analytical, experimental & formal-verification pillars
1. **Extension of the Mesoscopic Four-Gate Operator Sieve (`G1`–`G4` → `G5`–`G7`)**:
   - Retains `ES.10`'s four mesoscopic gates—`G1` (`σ < 32.98 µm`, `ℓ_b < 27.22 µm` Schur bounds on `Lee et al. 2020`), `G2` (`Cassini` `γ_PPN = 1.000021 ± 0.000023` rejecting scalar sheets at `43,479σ`, Hilbert unitarity & Lorentz invariance), `G3` (`2.0 K` equilateral-prism Mermin witness `⟨M₃⟩ = 3.6741 > 2√2 = 2.8284` at `D = 75 µm` vs `0.3227` for `Diósi–Penrose` at `33.08 µm`), and `G4` (universal `T_μν` proper-time clocks vs `Barato–Seifert` `20,000 k_B = 1,000 ATP` `1%` TUR floor)—and couples them to chiral anomalies (`G5`), dark-energy horizons (`G6`), and ghost-free UV gravity (`G7`).
2. **Gate `G5` · Domain-Wall Chirality & the Geng–Marshak–Fermat Cubic Lock (`Fritzsch & Minkowski 1975`; `Jackiw & Rebbi 1976`; `Geng & Marshak 1989`; `Minahan, Ramond & Warner 1990`; `Kaplan 1992`)**:
   - Transverse mass kink `m(w) = m₀ tanh(w / ℓ_w)` (`−m₀ < 0 < +m₀`) localizes a single normalizable chiral zero mode `ψ₀(w) ∝ cosh(w / ℓ_w)^{−m₀ℓ_w}` (overcoming vectorlike `χ = 0` mirror pairing on smooth `5`-D `S¹`).
   - Over integer weak hypercharges `y_int = 6Y` (`l = −3`), `[SU(2)_L]²U(1)_Y = 0` (`q = 1`) and `[SU(3)_C]²U(1)_Y = 0` (`u + d = −2`) reduce `[U(1)_Y]³ = 0` to `(u + 4)³ + (d + 4)³ = e³`. Omitting `[Grav]²U(1)_Y = 0` leaves the continuous irrational family `e(t) = [18(t² + 3)]^{1/3}` (`e(0) = 54^{1/3} ≈ 3.7798`, `3³ < 54 < 4³`), whereas enforcing `[Grav]²U(1)_Y = 0` pins `e = 6` and `{u, d} = {−4, +2}`, locking Hydrogen neutrality `Q_p + Q_e = 0`, `Tr(y_int²) = 120`, and `15 + 1 = 16 = 1 + 10 + 5̄` in `Spin(10)`.
3. **Gate `G6` · `88.11 µm` Dark-Energy Scale, Null-Ray Vacuum Decoupling & Bulk-Singlet Ladder (`Weinberg 1989`; `Jacobson 1995`; `Kapner et al. 2007`; `Planck Collaboration 2020`)**:
   - `Planck 2018` (`H₀ = 67.36 km s⁻¹ Mpc⁻¹`, `Ω_Λ = 0.6847`) yields `ρ_Λ = 5.24470 × 10⁻¹⁰ J/m³` and `ℓ_Λ = (ℏc / ρ_Λ)^{1/4} = 88.11 µm` (`E_Λ = 2.24 meV`; `Kapner 2007` `3.8 keV/cm³` gives `84.89 µm`), falsifying fat-graviton cutoffs via `32.98 µm < 84.89 µm`, while `T_μν^vac = −ρ_vac g_μν` decouples identically along null generators `g_μν k^μ k^ν = 0`.
   - Explicitly badges (`OPEN / PROPOSED`) the gauge-neutral bulk-singlet correlation ladder (`ℏc = 197.32698 meV·µm`): only the graviton and sterile singlet `ν_R^c` (`y_int = 0`) carry `0` Standard Model gauge charge and can probe `σ < 32.98 µm` (`M_* > 5.983 meV`, FWHM `< 77.66 µm`), bracketed by solar `√(Δm₂₁²) = 8.61 meV` (`λ_{ν,2} = 22.92 µm`) and atmospheric `√(Δm₃₁²) = 50.11 meV` (`λ_{ν,3} = 3.94 µm`).
4. **Gate `G7` · Entire Weierstrass UV Gravity & Bounded Force Deficit (`Stelle 1977`; `Biswas et al. 2012`; `Lee et al. 2020`)**:
   - Root-free entire propagator modifier `F(ℓ_*²q²) = exp(ℓ_*²q²)` avoids Stelle's spin-`2` ghost (`−1`), inverts in `3`-D to `V(r) = −(Gm₁m₂ / r) erf(r / 2ℓ_*)` (`< 10⁻¹⁵` quadrature error) with finite `V(0) = −Gm₁m₂ / (√π ℓ_*)`, obeys `0 < F_erf / F_N < 1` (`|ΔF / F_N| ≤ 1`, invisible to `|α|_95 >> 1` Casimir cantilevers at `1–25 µm`), satisfies `ℓ_* < 32.98 µm` (signed Schur) / `44.95 µm` (unsigned), preserves `2.0 K` Mermin GTE (`⟨M₃⟩ = 3.6740 > 2.8284` at `ℓ_* = 18 µm`), and marks `r ≲ ℓ_*` micro-acausality explicitly `OPEN`.
5. **Twelve Zero-`sorry` Core Lean 4 Prelude Theorems (`SevenGateCrown.lean`)**:
   - Certifies `seven_gate_crown_si_homogeneity`, `sm_hypercharge_uniqueness`, `pure_gauge_fermat_and_vectorlike_branch`, `gell_mann_nishijima_hydrogen_neutrality`, `spin10_weyl_and_jackiw_rebbi_chirality`, `jacobson_null_ray_vacuum_decoupling`, `vacuum_length_scale_window_ordering`, `stelle_ghost_vs_weierstrass_positivity`, `erf_uv_origin_regularization_positivity`, `nonlocal_lstar_eotwash_and_mermin_island`, `six_gate_eft_survivors`, and `seven_gate_crown_unique_corridor`, mirrored by `4` exact multivariate `Fraction` polynomial checks.

## 3. Primary Crossref DOIs verified offline (`16 / 16` cached)
| Source ID | Reference | DOI |
| --- | --- | --- |
| `ES11-FRITZSCH1975` | Fritzsch & Minkowski (1975), *Ann. Phys.* | https://doi.org/10.1016/0003-4916(75)90211-0 |
| `ES11-JACKIW1976` | Jackiw & Rebbi (1976), *Phys. Rev. D* | https://doi.org/10.1103/physrevd.13.3398 |
| `ES11-STELLE1977` | Stelle (1977), *Phys. Rev. D* | https://doi.org/10.1103/physrevd.16.953 |
| `ES11-WEINBERG1989` | Weinberg (1989), *Rev. Mod. Phys.* | https://doi.org/10.1103/revmodphys.61.1 |
| `ES11-GENG1989` | Geng & Marshak (1989), *Phys. Rev. D* | https://doi.org/10.1103/physrevd.39.693 |
| `ES11-MINAHAN1990` | Minahan, Ramond & Warner (1990), *Phys. Rev. D* | https://doi.org/10.1103/physrevd.41.715 |
| `ES11-KAPLAN1992` | Kaplan (1992), *Phys. Lett. B* | https://doi.org/10.1016/0370-2693(92)91112-m |
| `ES11-JACOBSON1995` | Jacobson (1995), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.75.1260 |
| `ES11-RANDALL1999` | Randall & Sundrum (1999), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.83.4690 |
| `ES11-BERTOTTI2003` | Bertotti, Iess & Tortora (2003), *Nature* | https://doi.org/10.1038/nature01997 |
| `ES11-KAPNER2007` | Kapner et al. (2007), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.98.021101 |
| `ES11-BISWAS2012` | Biswas, Gerwick, Koivisto & Mazumdar (2012), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.108.031101 |
| `ES11-BARATO2015` | Barato & Seifert (2015), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.114.158101 |
| `ES11-PLANCK2020` | Planck Collaboration (2020), *Astron. Astrophys.* | https://doi.org/10.1051/0004-6361/201833910 |
| `ES11-LEE2020` | Lee et al. / Eöt-Wash (2020), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.124.101101 |
| `ES11-TRILLO2025` | Trillo & Navascués (2025), *Phys. Rev. D* | https://doi.org/10.1103/physrevd.111.l121101 |
