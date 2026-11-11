---
name: timegravity-t11-einselection
description: Rebuild and verify the Time & Gravity T.11 toy - a 1+6 qubit pure-dephasing pointer-state and Quantum Darwinism statevector model whose Jacobi-diagonalised partial traces match Zurek's closed-form mutual-information plateau I(S : E_k) = h_2(gamma^N) + h_2(gamma^k) - h_2(gamma^{N-k}) within 1e-12, paired with the Joos-Zeh and Romero-Isart R^6 T^9 dipole photon scattering localization table - with a planted defect (theta = 0 zero pointer imprinting).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# What Selects the World a Clock Sees? (T.11 · Time & Gravity)

> **Fixed Boundary (`EN`):** Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up.
>
> **Frontera Fija (`ES-MX`):** Nada en esta página es una teoría del todo, y este sitio no propone ninguna. Cada afirmación lleva una de seis etiquetas, cada una ligada a una fila del libro de registro: MEDIDO, DERIVADO, COTA, PROPUESTO, ABIERTO o RESULTADO ÚNICO. Las prepublicaciones nunca suben de PROPUESTO. Cada página termina con una pregunta abierta que la siguiente página retoma.

## 1. Page, canonical URL and governing equations
- **Track page**: `T.11` (Time & Gravity, reading order 12 of 13, dated `2026-11-10`)
- **Canonical URL**: https://informatico.ai/timegravity/t11/ (Spanish: https://informatico.ai/es-mx/timegravity/t11/)
- **Pointer-basis commutation condition**: `[H_int, Π̂] = 0` (`Π̂ = σ_z` or position `x̂`); pointer states remain unentangled while each bath mode rotates by `|E_j^(1)⟩ = cos(θ)|0⟩ + sin(θ)|1⟩`, overlap `γ = |cos(θ)|`.
- **Off-diagonal suppression & Quantum Darwinism mutual information**: `|ρ_{S,01}(N)| / |ρ_{S,01}(0)| = γ^N`, `I(S : E_k) = h_2(γ^N) + h_2(γ^k) − h_2(γ^{N−k})`.
- **Thermal photon dipole scattering**: `Λ_sc = (8! · 8 ζ(9) c R^6 / 9π) (k_B T_e / ħc)^9 Re[(ε−1)/(ε+2)]^2`, `Γ_sc = Λ_sc Δx²`.
- **Central numbers**: on `1 + 6` qubits (`dim = 128`, `θ = 1.35 rad`, `γ = 0.2190`), statevector partial traces diagonalised via Jacobi match closed-form `I(S : E_k)` within `1.69e-14 nats` (`< 1e-12`), reaching `0.9983 bits` by `k = 2` modes while `|ρ_{S,01}| / |ρ_{S,01}(0)| = 1.103 × 10^{-4}`; for Joos & Zeh's `R = 10 µm` dust grain at `Δx = 10 µm`, `τ_CMB = 1.634 s` (`ε = 5.7`) or `0.609 s` (conductor, `Λ_CMB = 1.643 × 10^6 cm^{-2} s^{-1}`) vs `τ_300K = 6.888 × 10^{-19} s`, while an `R = 1 µm` microsphere is `10^6` times slower (`R^6` scaling within `6.98e-16`) and an electromagnetically uncoupled sector (`ε = 1`) has `Λ_EM = 0`.
- **Generator**: `python skills/timegravity/t11/make_t11.py`
- **Verifier**: `python skills/timegravity/t11/verify_t11_einselection.py`
- **Knockout check**: `python skills/timegravity/t11/verify_t11_einselection.py --planted-defect` (must exit non-zero: `θ = 0` zero pointer imprinting collapses `I(S : E_k)` to `0`)
- **Label lint**: `python tools/check_timegravity_labels.py` (and `--planted-defect`, `--mutants`)

## 2. Ledger rows this page may cite (timegravity/ledger.json)
| Row | Label | Source | DOI |
| --- | --- | --- | --- |
| `T11-BRUNE1996` | MEASURED | Brune et al. 1996, cavity-QED mesoscopic Schrödinger cat decoherence | https://doi.org/10.1103/PhysRevLett.77.4887 |
| `T05-HORNBERGER2003` | MEASURED | Hornberger et al. 2003, collisional decoherence of C70 fullerenes | https://doi.org/10.1103/PhysRevLett.90.160401 |
| `T05-HACKERMULLER2004` | MEASURED | Hackermüller et al. 2004, thermal-photon emission decoherence of C70 | https://doi.org/10.1038/nature02276 |
| `T08-MATHER1994` | MEASURED | Mather et al. 1994, COBE FIRAS 2.726 K CMB blackbody spectrum | https://doi.org/10.1086/173574 |
| `T11-ZUREK1981` | DERIVED | Zurek 1981, pointer basis of quantum apparatus | https://doi.org/10.1103/PhysRevD.24.1516 |
| `T11-JOOS1985` | DERIVED | Joos & Zeh 1985, emergence of classical properties through environment scattering | https://doi.org/10.1007/BF01725541 |
| `T11-ZUREK2009` | DERIVED | Zurek 2009, Quantum Darwinism and classical redundancy plateau | https://doi.org/10.1038/nphys1202 |
| `T11-EVERETT1957` | PROPOSED | Everett 1957, relative-state formulation of quantum mechanics | https://doi.org/10.1103/RevModPhys.29.454 |
| `T06-DIOSI1989` | PROPOSED | Diósi 1989, gravitational self-energy objective reduction | https://doi.org/10.1103/PhysRevA.40.1165 |
| `T06-PENROSE1996` | PROPOSED | Penrose 1996, gravity's role in quantum state reduction | https://doi.org/10.1007/BF02105068 |
| `T06-DONADI2020` | BOUND | Donadi et al. 2020, VIP-2 underground Ge X-ray bound on parameter-free Diósi–Penrose | https://doi.org/10.1038/s41567-020-1008-4 |

## 3. Tool-neutral agent packet and security boundary (`security-runtime`)
1. **Rebuild locally**: `python skills/timegravity/t11/make_t11.py`; standard library only; writes only under `src/timegravity/t11/files/`.
2. **Acceptance gate**: `python skills/timegravity/t11/verify_t11_einselection.py` must print `"status": "PASS"` with `statevector_matches_zurek_closed_form: PASS`; `--planted-defect` must exit non-zero. Then `python tools/check_timegravity_labels.py`.
3. **Security boundary (`security-runtime`)**: no shell outside the repository, no home-directory access, no outbound network for this task.

## 4. Deterministic verification and falsification rules
1. Across `k ∈ {0 … 6}` and `θ ∈ {0, π/6, π/3, 1.35, π/2}`, Jacobi-diagonalised partial traces of the `128`-component `1 + 6` qubit statevector match `I(S : E_k) = h_2(γ^N) + h_2(γ^k) − h_2(γ^{N−k})` within `1e-12` and satisfy `I(S : E_{N/2}) = S(ρ_S)` and `I(S : E_N) = 2 S(ρ_S)` within `1e-12`.
2. At `θ = 1.35 rad`, a `k = 2` mode fragment carries `> 0.90 bits` (`0.9983 bits`) while off-diagonal system coherence drops to `< 10^{-3}` (`1.103 × 10^{-4}`).
3. Dipole photon scattering satisfies `Λ(R = 10 µm) / Λ(R = 1 µm) = 10^6` and `Λ(300 K) / Λ(T_CMB) = (300 / T_CMB)^9` within `1e-12`, and vanishes (`Λ = 0`) at `ε = 1`.
4. Planted defect: setting `θ = 0` (`γ = 1`, no pointer-commuting bath imprinting) collapses `I(S : E_2)` to `0`; rule 2 fails and `--planted-defect` exits non-zero.
5. `t11_reference.json` matches `manifest.json` and regenerates byte for byte.

## 5. What the instrument shows (reader side)
- Left panel: Quantum Darwinism mutual-information curve `I(S : E_k) / H(S)` across fragment size `k / N` alongside system off-diagonal coherence `|ρ_{S,01}(k)| / |ρ_{S,01}(0)| = γ^k`. Right panel: Joos–Zeh thermal photon coherence time `τ_sc = 1 / (Λ_sc Δx²)` across `T_e` (`2.725 K` CMB vs `300 K`) for `R = 10 µm` vs `R = 1 µm` vs an electromagnetically uncoupled test mass (`α_EM = 0`).
- Knockout: turn off pointer-commuting bath imprinting (`θ = 0`); the classical redundancy plateau flattens to `I(S : E_k) = 0`.
- Predict before you reveal: whether observing `2` out of `6` scattered photon modes already delivers nearly the entire `1 bit` of pointer position information without touching the system itself.

## 6. Exact T0–T3 truth boundary
### In the repository today (T0/T1)
- Kernel `tools/timegravity_kernel_einselection.py`, generator, verifier, ledger rows above, and the ES module `src/modules/timegravity-slope.mjs`.

### Not on this page (T2/T3)
- Whether decohered branches that have become orthogonal in the photon bath (`|⟨E^(0)|E^(1)⟩| = γ^N → 0`) persist as physical Everettian worlds (`PROPOSED`) or are pruned by an objective collapse mechanism (`PROPOSED`/`BOUND`) is `OPEN`.
- Decohered branches of ordinary matter in Hilbert space and electromagnetically uncoupled dark-matter sectors in spacetime (`T.12`) are distinct physical concepts and are never equated.
