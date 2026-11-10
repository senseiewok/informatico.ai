---
name: timegravity-t05-entanglement-channels
description: Rebuild and verify the Time & Gravity T.05 instrument - the Bose-Marletto-Vedral four-branch entanglement phase (phi_ij = G m^2 t / hbar d_ij, concurrence |sin(delta phi / 2)|, Peres negativity under local dephasing) with three channels at equal weight (quantum, classical LOCC, disputed classical non-LOCC) - with a planted defect that lets a LOCC channel entangle.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Does Gravity Entangle, and Would That Settle It? (T.05 · Time & Gravity)

> **Fixed Boundary (`EN`):** Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up.
>
> **Frontera Fija (`ES-MX`):** Nada en esta página es una teoría del todo, y este sitio no propone ninguna. Cada afirmación lleva una de seis etiquetas, cada una ligada a una fila del libro de registro: MEDIDO, DERIVADO, COTA, PROPUESTO, ABIERTO o RESULTADO ÚNICO. Las prepublicaciones nunca suben de PROPUESTO. Cada página termina con una pregunta abierta que la siguiente página retoma.

## 1. Page, canonical URL and governing equations
- **Track page**: `T.05` (Time & Gravity, reading order 6 of 9, dated `2026-11-09`). Page label **OPEN**: the experiment has not run, and the literature disputes what a positive result would prove.
- **Canonical URL**: https://informatico.ai/timegravity/t05/ (Spanish: https://informatico.ai/es-mx/timegravity/t05/)
- **Branch phases**: `φ_ij = G m² t / (ħ d_ij)` with `d_LL = d_RR = d`, `d_LR = d + Δx`, `d_RL = d − Δx`.
- **Entanglement phase**: `Δφ = φ_LR + φ_RL − φ_LL − φ_RR`; the four-branch state is a product exactly when `Δφ ≡ 0 (mod 2π)`.
- **Measures**: concurrence `C = 2|ad − bc| = |sin(Δφ/2)|` (Wootters 1998); negativity from the partial transpose (Peres 1996), `N = C/2` for the pure state; local dephasing `e^{−γt}` on each mass.
- **Channels** (equal weight): `quantum` (the four phases as written); `locc` (each mass feels the mean field of the other: `φ_ij = α_i + β_j`, `Δφ = 0`); `disputed` (classical, non-LOCC: no single prediction; carried as the interval `[0, C_quantum]`).
- **Central numbers (2017 geometry: 10⁻¹⁴ kg, d = 450 µm, Δx = 250 µm, t = 2.5 s)**: `Δφ = 0.314 rad`, `C = 0.156`, `N = 0.078`; `C = 1` at `t = 25.0 s`; negativity vanishes at `γt = 0.156`; LOCC channel `< 10⁻¹²`.
- **Generator**: `python skills/timegravity/t05/make_t05.py`
- **Verifier**: `python skills/timegravity/t05/verify_t05_entanglement_channels.py`
- **Dispute kernel** (`tools/timegravity_kernel_dispute.py`): the band's computed edges. Lower: Kafri–Taylor–Milburn channel at `K Δx²/2ħ` per mass (`K = 2Gm²/d³`) equals this page's dephasing threshold in the small-split limit (ratio 1.000 at 2 µm). Upper: the Diósi–Penrose model as Trillo & Navascués write it (σ-smeared, `H = 0`), `⟨x|ρ(t)|y⟩ = exp[(G/2ħ) g(x,y) t]⟨x|ρ(0)|y⟩`, predicts entanglement only below `d_c = 0.8508σ` (letter 0.8501σ, appendix 0.850872σ); Fig. 3 geometry (10⁻¹⁵ kg, 23 µm, 24 µm): none at σ = 50 µm, about 5 h / 16 h / 20 d at 75 / 100 / 250 µm; 2017 geometry needs σ > 525 µm and shows < 10⁻³ at 2.5 s; the smeared pull is `erf(d/2σ)` of Newton's. Decomposition: `tn_state(..., part="interaction" | "noise")`; the noise part alone entangles nothing, the interaction part alone (the smeared pair potential as a Hamiltonian) gives at least the full negativity and equals the quantum channel as σ → 0 (0.078 for the 2017 geometry); letter geometry at σ = 75 µm: 0.024 full vs 0.152 interaction-only; at 50 µm: 0 vs 0.363. Pure collapse (`dp_collapse_state`, quantum phases plus Diósi's two-body damping, Newton intact): critical σ 130 µm for the 2017 geometry, 14.3 µm for the letter's; `dp_collapse_scaling` shows the threshold scales with the geometry's size (×0.5 → 65.6 µm, ×2 → 259 µm) and moves under 1 % for a tenfold mass change or 1 s vs 2.5 s while the phase is small. `rijavec_tau_g`: τ_G = ħd[(d/Δx)² − 1]/(Gm²) of Rijavec et al. 2021; this page's dephasing threshold 0.0623 /s is 0.992 of their 1/τ_G. `threshold_map`: over r = split/nearest from 0.03 to 32, the hybrid dynamics entangles above G(r)·d with G from 1.21 to 37.8 and the witness survives pure collapse above F(r)·d with F from 0.37 to 1.0, both mass-independent (Plate T.05-M, `data-tg-figure="threshold-map"`). `map_with_isl`: the map read with the 2020 data: the smeared pull at the 2017 geometry's hybrid threshold (525 µm) removes 100 % of the 52 µm torque, at the letter's (55 µm) 6.2 % against the published edge's 2.5 %; at the 44 µm estimate the model reaches nearest approaches of 36 µm (r = 0.03) and 19 µm (r = 1) against Casimir floors of 17.1 / 26.5 / 41.5 µm at 10⁻¹⁵ / 10⁻¹⁴ / 10⁻¹³ kg; a pair at the 10⁻¹⁵ kg floor needs σ > 20.7 µm (r = 0.03). Verifier `python skills/timegravity/t05/verify_t05_dispute_kernel.py`; `--planted-defect` (decoherence dropped, no critical separation) must exit non-zero.
- **Smeared-gravity kernel** (`tools/timegravity_kernel_isl.py`): the model's pair potential `G m₁m₂ erf(d/2σ)/d` set beside the sub-millimetre inverse-square-law tests. Between two patterned plates each in-plane mode `q` pulls as `R(q, s; σ) = ½[erfc(qσ − s/2σ) + e^(2qs) erfc(qσ + s/2σ)]` of Newton's `e^(−qs)` (closed form vs direct quadrature 1e-14; limits σ → 0, s ≫ σ, q → 0 give Newton, s = 0 gives erfc(qσ); monotone fall with `q`, so the pattern's lowest wavenumber bounds each harmonic's deficit from below up to the Bessel tail). Eöt-Wash 2020 (Pt plates 54 / 99 µm, patterns 52 mm across, 18- and 120-fold, s = 52 µm … 3.0 mm, λ < 38.6 µm at 95 %): 120-fold deficit at 52 µm 10.4 % (σ = 75 µm), 2.5 % (50 µm), 0.2 % (30 µm), 3.7 % at σ_c = 55 µm of the letter's geometry; Yukawa at the edge (α = −1, λ = 38.6 µm) 1.5 %; matching σ 44 µm; best-mimic Yukawa λ ≈ 49 µm, α ≈ −3.2 (a curve match). A one-mode estimate of predicted signal sizes, not a bound on σ; HUST 2020 (λ = 48 µm) quoted as published. Verifier `python skills/timegravity/t05/verify_t05_smeared_isl.py`; `--planted-defect` (the closed form's `e^(2qs) erfc` term dropped) must exit non-zero.
- **Wedge kernel** (`tools/timegravity_kernel_wedge.py`): the full Eöt-Wash 2020 geometry from Lee's 2020 dissertation (hdl.handle.net/1773/45542; 120 wedges 13.004–22.998 mm at 1.490°, 18 wedges 23.505–26.000 mm at 9.984°, foils 54 / 99 µm, glue 1.162 g/cm³) under the collaboration's Fourier–Bessel expansion (Lee et al. 2021, Eqs. 7–19): `T_N(s) = 8 N G ρc² sin²(Nβ) ∫dk R(N,k)² Z(k,s)`, stdlib Bessel functions (Miller recurrence; checked against the integral representation to 1e-9), radial series with a truncation that grows with `k·r₁` (checked against quadrature to 1e-6). Newtonian 120-fold torque 1.51 fN·m at 72 µm (the letter's 'roughly 1 %' magnetic subtraction implies about 1.6). Smeared deficits at 52 µm: 17.0 % (σ = 75 µm), 4.3 % (50), 0.3 % (30), 6.3 % (55 µm, σ_c of the letter's geometry); Yukawa at the edge 2.5 %; matching σ 44.1 µm (one-mode bound: 44.4 µm); mimic Yukawa λ ≈ 49 µm, α ≈ −3.1. Window at σ ≤ 44 µm: d_c 37.5 µm (small split), 14.9 µm (23 µm split), the letter's geometry never. Same verifier; `--planted-defect` also plants a fixed 250-term truncation, which the quadrature double entry rejects.
- **Knockout check**: `python skills/timegravity/t05/verify_t05_entanglement_channels.py --planted-defect` (must exit non-zero: a LOCC channel that entangles)
- **Label lint**: `python tools/check_timegravity_labels.py` (and `--planted-defect`, `--mutants`)

## 2. Ledger rows this page may cite (timegravity/ledger.json)
| Row | Label | Source | DOI |
| --- | --- | --- | --- |
| `T05-BOSE2017` | PROPOSED | Bose et al. 2017, spin entanglement witness | https://doi.org/10.1103/PhysRevLett.119.240401 |
| `T05-MARLETTO2017` | PROPOSED | Marletto & Vedral 2017, sufficiency argument | https://doi.org/10.1103/PhysRevLett.119.240402 |
| `T05-WESTPHAL2021` | MEASURED | Westphal et al. 2021, gravity between 90 mg spheres | https://doi.org/10.1038/s41586-021-03250-7 |
| `T05-FUCHS2024` | MEASURED | Fuchs et al. 2024, 0.4 mg levitated test mass | https://doi.org/10.1126/sciadv.adk2949 |
| `T05-AGAFONOVA2026` | SINGLE RESULT (young) | Agafonova et al. 2026, 1 mg pendulum at 240 µK | https://doi.org/10.1038/s42005-026-02514-w |
| `T05-TROYER2026` | SINGLE RESULT (young) | Troyer et al. 2026, librational ground state | https://doi.org/10.1038/s41567-026-03219-1 |
| `T05-KTM2014` | PROPOSED | Kafri, Taylor & Milburn 2014, classical channel model | https://doi.org/10.1088/1367-2630/16/6/065020 |
| `T05-PERES1996` | DERIVED | Peres 1996, separability criterion | https://doi.org/10.1103/PhysRevLett.77.1413 |
| `T05-WOOTTERS1998` | DERIVED | Wootters 1998, two-qubit concurrence | https://doi.org/10.1103/PhysRevLett.80.2245 |
| `T05-AZIZ2025` | PROPOSED (young, disputed) | Aziz & Howl 2025, Nature | https://doi.org/10.1038/s41586-025-09595-7 |
| `T05-TRILLO2025` | PROPOSED (young) | Trillo & Navascués 2025, PRD Letter | https://doi.org/10.1103/PhysRevD.111.L121101 |
| `T05-SCHNEIDER2026` | PROPOSED (young) | Schneider, Huggett & Linnemann 2026, CQG | https://doi.org/10.1088/1361-6382/ae6f62 |
| `T05-MARLETTO2025` | PROPOSED (preprint) | Marletto & Vedral 2025, rebuttal | https://doi.org/10.48550/arXiv.2510.19969 |
| `T05-DIOSI2025` | PROPOSED (preprint) | Diósi 2025, rebuttal | https://doi.org/10.48550/arXiv.2511.00852 |
| `T05-TOBAR2026` | PROPOSED (preprint) | Tobar, Aspelmeyer & Zych 2026, clock proposal | https://doi.org/10.48550/arXiv.2611.08313 |
| `T05-TILLOY2016` | PROPOSED | Tilloy & Diósi 2016, hybrid construction | https://doi.org/10.1103/PhysRevD.93.024026 |
| `T05-VANDEKAMP2020` | PROPOSED | Van De Kamp et al. 2020, the Fig. 3 geometry | https://doi.org/10.1103/PhysRevA.102.062807 |
| `T05-LEE2020` | MEASURED | Lee et al. 2020, 1/r² down to 52 µm | https://doi.org/10.1103/PhysRevLett.124.101101 |
| `T05-TAN2020` | MEASURED | Tan et al. 2020, |α| ≤ 1 down to 48 µm | https://doi.org/10.1103/PhysRevLett.124.051301 |

## 3. Tool-neutral agent packet and security boundary (`security-runtime`)
1. **Rebuild locally**: `python skills/timegravity/t05/make_t05.py`; standard library only; writes only under `src/research/timegravity/t05/files/`.
2. **Acceptance gate**: `python skills/timegravity/t05/verify_t05_entanglement_channels.py` must print `"status": "PASS"` with `locc_channel_entangles_nothing: PASS`; `--planted-defect` must exit non-zero. Then `python tools/check_timegravity_labels.py`.
3. **Security boundary (`security-runtime`)**: no shell outside the repository, no home-directory access, no outbound network for this task; the cache refresher is the track's only network script, run by hand by a maintainer.

## 4. Deterministic verification and falsification rules
1. Concurrence from the closed form `|sin(Δφ/2)|` and from the reduced-state purity `sqrt(2(1 − Tr ρ_A²))` agree within `10⁻¹²`.
2. The Peres negativity of the pure state equals `C/2` within `10⁻⁹` (partial transpose, Hermitian 4×4 through the real 8×8 embedding, Jacobi solver).
3. The recomputed phases `Δφ_RL = 0.44`, `Δφ_LR = −0.13` and `Δφ = 0.31 rad` lie within a factor of four of the proposal's order-of-magnitude values (0.7, −0.2, ≈ 0.5).
4. `C = 1` at `Δφ = π` (`t = 25.0 s` for the 2017 geometry); `C = 0` with `G = 0`.
5. The LOCC channel entangles nothing on a 3 × 3 × 3 grid of separations, splits and hold times (`< 10⁻¹²`) while reproducing the mean Newtonian phase; the disputed channel is carried as `[0, C_quantum]`.
6. Planted defect: the LOCC channel carries the quantum phases; rule 5 fails and `--planted-defect` exits non-zero.
7. `t05_reference.json` matches `manifest.json` and regenerates byte for byte.

## 5. What the instrument shows (reader side)
- Left: two masses each in two places and the four branch lines with their separations. Right: entanglement against hold time; the three channels drawn at equal weight (quantum curve, LOCC flat line, disputed hatched band).
- Knockout: switch the channel. Planted defect: a classical LOCC channel that entangles.
- Predict before you reveal: the concurrence after 2.5 s in the 2017 geometry.

## 6. Exact T0–T3 truth boundary
### In the repository today (T0/T1)
- Kernel `tools/timegravity_kernel_entangle.py` (`branch_phases`, `entanglement_phase`, `concurrence_closed`, `four_branch_state`, `negativity`, `negativity_threshold_gamma_t`, `disputed_interval`, `check_bmv`), generator, verifier, ledger rows above.

### Not on this page (T2/T3)
- No gravitationally induced entanglement has been measured; no claim is made about which of the 2025 positions is right.
- Casimir–Polder, magnetic and electrostatic forces, the witness statistics of the proposal, and the decoherence budgets of specific laboratories are not modelled beyond a single local dephasing rate.
