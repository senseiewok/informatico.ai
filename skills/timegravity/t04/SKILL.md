---
name: timegravity-t04-clock-visibility
description: Rebuild and verify the Time & Gravity T.04 experiment description - a two-level clock in a superposition of two heights loses interferometric visibility V = |cos(omega dtau / 2)| as its proper times decohere (Zych et al. 2011) - with a standard-library Python verifier (closed form against explicit state overlap) whose planted defect is a clock that never decoheres.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# A Clock in Two Places (T.04 · Time & Gravity)

> **Fixed Boundary (`EN`):** Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up.
>
> **Frontera Fija (`ES-MX`):** Nada en esta página es una teoría del todo, y este sitio no propone ninguna. Cada afirmación lleva una de seis etiquetas, cada una ligada a una fila del libro de registro: MEDIDO, DERIVADO, COTA, PROPUESTO, ABIERTO o RESULTADO ÚNICO. Las prepublicaciones nunca suben de PROPUESTO. Cada página termina con una pregunta abierta que la siguiente página retoma.

## 1. Page, canonical URL and governing equations
- **Track page**: `T.04` (Time & Gravity, reading order 5 of 9, dated `2026-11-09`). Page label **PROPOSED**: an experiment description, not a result; no gravitational version has run.
- **Canonical URL**: https://informatico.ai/timegravity/t04/ (Spanish: https://informatico.ai/es-mx/timegravity/t04/)
- **Proper-time difference**: `Δτ = g Δh T / c²` between arms Δh apart for time T (weak field).
- **Visibility**: `V = |cos(ω Δτ / 2)|` for a clock prepared in `|+⟩`, `ω = ΔE/ħ` (Zych, Costa, Pikovski & Brukner 2011).
- **Central numbers**: closed form equals the explicit state overlap within `1e-12`; `V(0) = 1`; for a Sr optical clock (`ω/2π ≈ 429 THz`) `V(1 m, 1 s) ≈ 0.989` and the first zero sits at `Δh·T ≈ 10.7 m·s`.
- **Generator**: `python skills/timegravity/t04/make_t04.py`
- **Verifier**: `python skills/timegravity/t04/verify_t04_clock_visibility.py`
- **Knockout check**: `python skills/timegravity/t04/verify_t04_clock_visibility.py --planted-defect` (must exit non-zero: `ω = 0`, a clock that never decoheres, `V ≡ 1`)
- **Label lint**: `python tools/check_timegravity_labels.py` (and `--planted-defect`, `--mutants`)

## 2. Ledger rows this page may cite (timegravity/ledger.json)
| Row | Label | Source | DOI |
| --- | --- | --- | --- |
| `T04-ZYCH2011` | DERIVED | Zych et al. 2011, visibility as a witness of proper time | https://doi.org/10.1038/ncomms1498 |
| `T01-PR1960` | MEASURED (parent) | Pound & Rebka 1960, the redshift that fixes Δτ | https://doi.org/10.1103/PhysRevLett.4.337 |
| `T04-MARGALIT2015` | SINGLE RESULT | Margalit et al. 2015, self-interfering clock (magnetic gradient, not gravity) | https://doi.org/10.1126/science.aac6498 |
| `T04-PACZOS2025` | PROPOSED | Paczos, Foo & Zych 2025, trapped-atom interferometers (Quantum) | https://doi.org/10.22331/q-2025-08-08-1827 |
| `T04-SORCI2026` | PROPOSED | Sorci et al. 2026, proper time in optical ion clocks (PRL) | https://doi.org/10.1103/qhj9-pc2b |
| `T07-GIAC2019` | DERIVED | Giacomini et al. 2019, quantum reference frames (for the OPEN question) | https://doi.org/10.1038/s41467-018-08155-0 |

## 3. Tool-neutral agent packet and security boundary (`security-runtime`)
1. **Rebuild locally**: `python skills/timegravity/t04/make_t04.py`; standard library only; writes only under `src/research/timegravity/t04/files/`.
2. **Acceptance gate**: `python skills/timegravity/t04/verify_t04_clock_visibility.py` must print `"status": "PASS"`; `--planted-defect` must exit non-zero. Then `python tools/check_timegravity_labels.py`.
3. **Security boundary (`security-runtime`)**: no shell outside the repository, no home-directory access, no outbound network for this task; the cache refresher is the only network script, run by hand by a maintainer.

## 4. Deterministic verification and falsification rules
1. `|V_closed − |⟨ψ(0)|ψ(Δτ)⟩|| < 1e-12` on a grid of Δh ∈ {0, 0.1, 1, 3, 10} m and T ∈ {0.1, 1, 5} s.
2. `V(Δh = 0) = 1`.
3. At `Δh·T = π c²/(g ω)` the visibility is below `1e-6`.
4. Planted defect: `ω = 0` keeps `V ≡ 1`; rule 3 fails and `--planted-defect` exits non-zero.
5. `t04_reference.json` matches `manifest.json` and regenerates byte for byte.

## 5. What the instrument shows (reader side)
- The visibility curve against height difference for the chosen hold time and clock frequency; a marker at the chosen Δh; two clock faces on the two arms.
- Knockout: switch gravity off (g → 0) and the curve is flat at 1: without the slope in the rate of time there is no which-path information. Planted defect: a clock that never ticks (ω → 0), also flat at 1, which is why the verifier insists on a zero.
- Predict before you reveal: the reader guesses how much visibility a 1 m, 1 s optical clock loses.

## 6. Exact T0–T3 truth boundary
### In the repository today (T0/T1)
- Kernel functions `proper_time_difference`, `zych_visibility`, `clock_overlap`, `zych_first_zero`, `check_zych` in `tools/timegravity_kernel_quantum.py`; generator, verifier, ledger rows above.

### Not on this page (T2/T3)
- No gravitational clock interferometer has run; the 2015 experiment used a magnetic gradient and is stated as such. The 2025 and 2026 items are proposals.
- Which time the clock reads in superposition is OPEN.
