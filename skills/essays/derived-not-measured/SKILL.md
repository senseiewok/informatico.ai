---
name: essay-es02-derived-not-measured
description: Verify Essay ES.02 (Derived, Not Measured) on Informatico.ai - pure-Python stdlib epistemic lattice classifier, three-absence probes (PROPOSED unbuilt witnesses, OPEN unresolved Cryo-EM coordinates, and DERIVED (NOT MEASURED) parent-provenance recasts), and an 8-mutant falsification harness with --planted-defect knockout.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Derived, Not Measured (Essay ES.02 · Informatico.ai)

## 1. Scope and Epistemic Boundary
- **Essay code & slug**: `ES.02` (`derived-not-measured`), instrument kind `epistemic`, dated `2026-11-10`.
- **Module**: `tools/folios/essays/e02_derived_not_measured.py`
- **Verifier**: `skills/essays/derived-not-measured/verify_essay_derived_not_measured.py`
- **Core thesis**: Numerical agreement to `10^-12` audits the algebra, never the apparatus. Scientific software must distinguish three distinct kinds of empirical absence instead of blurring them under a single hedge word:
  1. **Unbuilt / Unobserved Phenomenon (`PROPOSED`)**: E.g., the `2017` Bose–Marletto–Vedral gravitationally induced entanglement witness (`10^-14 kg`, `450 um` separation, `250 um` split, `2.5 s` free fall; `Delta_phi = 0.31 rad`, concurrence `0.16`), plus `2025` classical-gravity entanglement proposals and all arXiv preprints.
  2. **Physically Present, Experimentally Unresolved (`OPEN`)**: E.g., across the `4` canonical human CFTR Cryo-EM coordinate maps (`5UAK` Liu `2017`, `5W81` Zhang `2017`, `6MSM` Zhang `2018`, `8EIQ` Fiedorczuk & Chen `2022`), wild-type `Phe508` is resolved in `5UAK`, `5W81`, and `6MSM` and genetically deleted in `8EIQ` (`DeltaF508`), whereas the ~`200`-residue disordered regulatory R-domain is physically tethered in the specimen yet left unmodeled across all `4` maps because conformational motion smears out electron density.
  3. **Mathematically Computed from a Measured Parent (`DERIVED (NOT MEASURED)`)**: E.g., computing Wootters concurrence `0.16` to `10^-12` from `T05-WESTPHAL2021` (`90 mg` gold spheres at `400 um`), or projecting the `2025` smeared pair potential `-G m_1 m_2 erf(r / 2*sigma) / r` onto `T05-LEE2020`'s `52 um` Eöt-Wash Fourier–Bessel limits (`alpha_eff = -7.3` vs `-7.4` at `33 um`, `-10.2` at `35 um`, excluding `sigma > 33 um` at `95 %`).

## 2. Deterministic Acceptance Gate & Knockout Check
Run from the repository root (`Python 3`, standard library only, zero network calls):

```powershell
python -X utf8 skills/essays/derived-not-measured/verify_essay_derived_not_measured.py
python -X utf8 skills/essays/derived-not-measured/verify_essay_derived_not_measured.py --planted-defect
```

- **Normal run (`no args`)**: Must exit `0` and print valid JSON to `stdout` with `"status": "PASS"`, `"essay": "ES.02"`, `"slug": "derived-not-measured"`, `"mutants_killed": 8`, `"mutants_total": 8`.
- **Knockout run (`--planted-defect`)**: Relaxes the `DERIVED (NOT MEASURED)` measured-parent constraint so mutant `M3_DERIVED_PROPOSED_PARENT` survives (`7/8` killed); must exit non-zero (`1`) with `"status": "FAIL"` on `stderr`.

## 3. Eight Planted Epistemic Corruptions (`8/8` Killed)
1. `M1_PREPRINT_TO_MEASURED` — Promotes an arXiv preprint above the `PROPOSED` ceiling to `MEASURED`.
2. `M2_DERIVED_MISSING_PARENT` — Strips `parent_id` from a `DERIVED (NOT MEASURED)` claim.
3. `M3_DERIVED_PROPOSED_PARENT` — Re-points a `DERIVED (NOT MEASURED)` claim from its `MEASURED` parent to an unbuilt `PROPOSED` row.
4. `M4_SINGLE_GROUP_TO_MEASURED` — Promotes a `1`-collaboration `< 24`-month result (`2026` run) to `MEASURED`.
5. `M5_UNRESOLVED_INTERPOLATED_AS_MEASURED` — Interpolates the ~`200` unresolved Cryo-EM R-domain residues from `OPEN` into `MEASURED`.
6. `M6_EXCLUSION_BOUND_AS_DETECTION` — Misreads a null-excess exclusion `BOUND` (`Donadi 2021`) as a positive `MEASURED` detection.
7. `M7_BILINGUAL_NUMERIC_DRIFT` — Introduces EN/`es-MX` numeric drift (`0.31 rad` vs `0.39 rad`).
8. `M8_UNAUDITED_CONTRASTING_DOMINANCE` — Clears the `>= 20`-character `contrasting_audit` note on a row where `Scite` contrasting citations exceed supporting citations.

## 4. Security & Provenance Guardrails (`security-runtime`)
- Pure Python standard library only; zero external network requests; every cited DOI resolves offline in `data/folio-citations.cache.json`.
- Proportional domain guardrail: `<= 2` mentions of Cystic Fibrosis across the essay, zero clinical claims, and exact numeric parity between English and Mexican Spanish (`es-MX`, `.` decimal separator).
