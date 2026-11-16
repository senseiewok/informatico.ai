# Cryptographic Publishing Proof & Reproducibility Ledger (`informatico.ai`)

Every Grand-Challenge Bounty harness (`bounties/`) and interactive Folio companion (`skills/`) in [`senseiewok/informatico.ai`](https://github.com/senseiewok/informatico.ai) is anchored to an immutable Git commit hash and tree SHA on GitHub.

---

## 1. How GitHub Serves as Our Timestamped Publishing Proof

When referencing open-source benchmark companions, formalization links, or technical baselines alongside grand-challenge registries (`Erdős Problems`, closed `XPRIZE Quantum Applications`, concluded `unitaryHACK 2026` / active Unitary Microgrants, closed `XPRIZE Carbon Removal` / `IStructE`, closed 8th `Holcim Awards` / `Global Cooling Prize`, and successor `SAIR Foundation` challenges covered in `M.13–M.15`), this repository provides **four layers of verifiable cryptographic proof**:

1. **Immutable Git Tree & Commit SHA (`git rev-parse HEAD`)**
   - Every commit on [`https://github.com/senseiewok/informatico.ai/commits/main`](https://github.com/senseiewok/informatico.ai/commits/main) records the cryptographic hash of all 57 `SKILL.md` monographs (51 Pillar Folios + 6 Grand-Challenge Folios, plus 6 Toolbox `SKILL.md` companions), the proof harnesses under `bounties/`, and the verifiers under `skills/` (Volume VII Math `M.13–M.15`, Toolbox, Time & Gravity and cross-scale essays; other pillar and bounty skills are plain text), and the offline Crossref DOI citation cache (`data/folio-citations.cache.json`).
2. **Zero-Dependency Deterministic Reproduction (`< 3 seconds`)**
   - Any reviewer, prize judge, or automated CI runner can verify the exact numerical claims from a clean Python 3.10+ standard-library environment without external dependencies:
     ```bash
     git clone https://github.com/senseiewok/informatico.ai.git
     cd informatico.ai
     git log -1 --format="Commit SHA: %H | Date: %cI | Tree: %T"
     python -X utf8 bounties/run_all_bounties.py
     python -X utf8 skills/verify_all_48_folios.py
     python -X utf8 -m unittest discover -s tests -v
     ```
3. **Offline Primary Literature & Theorem Verification**
   - All 51 Pillar Folios (100% of Volume I–VII essays) are verified against primary Crossref DOIs (`data/folio-citations.cache.json`), and link directly to open-source formalization repositories:
     - [`anthropics/formal-math`](https://github.com/anthropics/formal-math): its README, read on 2026-11-14, lists three Lean 4 projects, `zeta23`, `3sum-apsp` and `eth` (the last described there as refuting the Exponential Time Hypothesis, a statement this project has not checked). Files named `ETHIsFalse.lean`, `EightSquare.lean` and `ThreeSUM_APSP.lean`, cited in earlier versions of this page, do not appear in the repository's file tree read the same day.
     - [`anthropics/fermats-last-theorem`](https://github.com/anthropics/fermats-last-theorem): its README, read on 2026-11-14, describes a complete, machine-checked Lean 4 proof of Fermat's Last Theorem in which no module contains `sorry` or an added `axiom`. That README states no line count; the `13,000,000+` lines given in earlier versions of this page are withdrawn.
     - These are the repositories' own statements. This project has not built either repository.
4. **Single-Owner Repository Integrity (`@senseiewok` Only)**
   - To protect provenance and prevent unverified third-party code injection into the publishing ledger, `senseiewok/informatico.ai` enforces GitHub interaction limits (`collaborators_only`), `CODEOWNERS` protection (`* @senseiewok`), and automated closure of any external pull request (`.github/workflows/lock-external-prs.yml`).

---

## 2. Benchmark Proof Summary Table

`PASS` below means a harness reproduces its own worked example. It is not a prize result, and none of these prizes has been won or awarded to this project. Status audited `2026-11-15`: AIMO closed `2026-09-16` (XTX shifted to Lean FRO, Mathlib & SAIR `M.13–M.15`), XPRIZE Quantum closed to new entrants May 2026 and `unitaryHACK 2026` concluded June 2026, XPRIZE Carbon concluded April 2025, 8th Holcim Awards closed February/November 2025, and the Global Cooling Prize closed in 2021; the 45 kg CO₂e/m² slab line and the vault and sky-cooling thresholds are the folios' own design targets.

| Bounty ID | Related Grand Challenge / Registry (`2026-11-15` Status) | Verifier Script | Deterministic Output | Folio Companions |
| :--- | :--- | :--- | :--- | :--- |
| **`BOUNTY-M1` (`B.01`)** — [https://informatico.ai/bounties/b01/](https://informatico.ai/bounties/b01/) | Erdős #30 (`$1,000` Open) · AIMO Closed `2026-09-16` (SAIR in `M.13–M.15`) | [`bounties/bounty_m1_erdos_sidon_lean4.py`](bounty_m1_erdos_sidon_lean4.py) | `N=500: \|A\|=20 <= 28.09 · Unique sums=True · PASS` | `M.13`, `M.11`, `M.12` |
| **`BOUNTY-P1` (`B.02`)** — [https://informatico.ai/bounties/b02/](https://informatico.ai/bounties/b02/) | XPRIZE Quantum (Finalists Only May 2026) · `unitaryHACK` Concluded · Rolling Unitary Microgrants & `Metriq` | [`bounties/bounty_p1_surface_code_femoco.py`](bounty_p1_surface_code_femoco.py) | `d=27, p_phys=0.001 -> P_L=3.00e-16, Q_phys=428,652 · PASS` | `P.11`, `P.12` |
| **`BOUNTY-E1` (`B.03`)** — [https://informatico.ai/bounties/b03/](https://informatico.ai/bounties/b03/) | XPRIZE Carbon Removal (Concluded Apr 2025) & IStructE (Built Works Only) | [`bounties/bounty_e1_simp_carbon_slab.py`](bounty_e1_simp_carbon_slab.py) | `V/V0=0.35 -> Net CO2=39.4 kg/m2 (<45 target), c/c0=1.224 · PASS` | `E.11`, `E.12` |
| **`BOUNTY-A1` (`B.04`)** — [https://informatico.ai/bounties/b04/](https://informatico.ai/bounties/b04/) | Holcim Awards (8th Cycle Concluded Nov 2025) & Global Cooling Prize (Closed 2021) | [`bounties/bounty_a1_graphic_statics_sky_cooling.py`](bounty_a1_graphic_statics_sky_cooling.py) | `L=16m, f/L=0.16, H=100kN, 0kg rebar, q_net=98.4 W/m2, dT=-5.2C · PASS` | `A.11`, `A.12` |
| **`BOUNTY-P2` (`B.05`)** — [https://informatico.ai/bounties/b05/](https://informatico.ai/bounties/b05/) | Symbolic PDE Discovery (`PySR` + `PySINDy` Pareto Frontier) | [`bounties/bounty_p2_pysr_pysindy_pde_discovery.py`](bounty_p2_pysr_pysindy_pde_discovery.py) | `terms=['u*u_x', 'u_xx'] law='-u * u_x + 0.10 * u_xx' · PASS` | `P.11`, `P.12` |
| **`BOUNTY-M2` (`B.06`)** — [https://informatico.ai/bounties/b06/](https://informatico.ai/bounties/b06/) | `PhysLean` Gauge Anomaly Cancellation & Tensor Network DMRG | [`bounties/bounty_m2_physlean_itensor_quantum_gauge.py`](bounty_m2_physlean_itensor_quantum_gauge.py) | `Tr[Y^3]=0.0, E0/N=-1.273240, S_vN=0.883 · PASS` | `M.11`, `M.12` |

---

## 5. Anchored Genesis Commit SHA Ledger

- **Genesis Publishing Commit SHA (`main`)**: [`1d9bebaf7bb60348d942f3cb05916305fc304ef0`](https://github.com/senseiewok/informatico.ai/commit/1d9bebaf7bb60348d942f3cb05916305fc304ef0) (`1d9beba`)
- **Live Commit Verification Link**: [https://github.com/senseiewok/informatico.ai/commit/1d9bebaf7bb60348d942f3cb05916305fc304ef0](https://github.com/senseiewok/informatico.ai/commit/1d9bebaf7bb60348d942f3cb05916305fc304ef0)
- **Verification Status**: every verifier under `skills/` passes and fails under its planted defect (`skills/verify_all_48_folios.py`) · `6/6` Bounty Harnesses PASS (`bounties/run_all_bounties.py`) · `fail=0` Crossref Citations (`tools/check_folio_citations.py --offline`).

## Correction, 2026-11-13

On 2026-11-13, 54 generated placeholder scripts were removed from `skills/` (48 pillar essays and 6 bounty skills). They stored each essay's values as text and printed PASS without computing anything. Those skills are now plain-text `SKILL.md` files, and `skills/verify_all_48_folios.py` now rejects any verifier that cannot fail. The earlier files remain in git history.
