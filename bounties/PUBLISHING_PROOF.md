# Cryptographic Publishing Proof & Reproducibility Ledger (`informatico.ai`)

Every Grand-Challenge Bounty harness (`bounties/`) and interactive Folio companion (`skills/`) in [`senseiewok/informatico.ai`](https://github.com/senseiewok/informatico.ai) is anchored to an immutable Git commit hash and tree SHA on GitHub.

---

## 1. How GitHub Serves as Our Timestamped Publishing Proof

When submitting open-source benchmark companions, formalization links, or technical baselines to prize registries (`XPRIZE Quantum Applications`, `Unitary Foundation unitaryHACK`, `Erdős Problems / AIMO`, `XPRIZE Carbon Removal / IStructE`, `Holcim Awards / Global Cooling Prize`), this repository provides **four layers of verifiable cryptographic proof**:

1. **Immutable Git Tree & Commit SHA (`git rev-parse HEAD`)**
   - Every commit on [`https://github.com/senseiewok/informatico.ai/commits/main`](https://github.com/senseiewok/informatico.ai/commits/main) records the cryptographic hash of all 48 `SKILL.md` monographs, 48 zero-dependency Python verifiers (`skills/<pillar>/<slug>/verify_<slug>.py`), 6 Grand-Challenge bounty harnesses (`bounties/`), and the offline Crossref DOI citation cache (`data/folio-citations.cache.json`).
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
   - All 48 Folios (100% of Volume I–VI essays) are verified against primary Crossref DOIs (`data/folio-citations.cache.json`), and link directly to open-source formalization repositories:
     - [`anthropics/formal-math`](https://github.com/anthropics/formal-math) (`ETHIsFalse.lean`, `EightSquare.lean`, `ThreeSUM_APSP.lean`, `Zeta23.lean`, `XiPrime.lean`)
     - [`anthropics/fermats-last-theorem`](https://github.com/anthropics/fermats-last-theorem) (`13,000,000+` lines of Lean 4, zero `sorry`)
     - [`anthropics/theorem-riscv`](https://github.com/anthropics/theorem-riscv) (`180,000,000+` lines of Rocq RISC-V formal verification)
4. **Single-Owner Repository Integrity (`@senseiewok` Only)**
   - To guarantee provenance and prevent unverified third-party code injection into the publishing ledger, `senseiewok/informatico.ai` enforces GitHub interaction limits (`collaborators_only`), `CODEOWNERS` protection (`* @senseiewok`), and automated closure of any external pull request (`.github/workflows/lock-external-prs.yml`).

---

## 2. Benchmark Proof Summary Table

| Bounty ID | Target Grand Challenge / Registry | Verifier Script | Deterministic Output | Folio Companions |
| :--- | :--- | :--- | :--- | :--- |
| **`BOUNTY-M1`** | Erdős Problems (`#30` / `#155` Sidon $B_2$ sets) & `$10M` AIMO / Lean 4 | [`bounties/bounty_m1_erdos_sidon_lean4.py`](bounty_m1_erdos_sidon_lean4.py) | `N=500: \|A\|=20 <= 28.09 · Unique sums=True · PASS` | `M.11`, `M.12` |
| **`BOUNTY-P1`** | `$5M` XPRIZE Quantum Applications & Unitary Foundation `unitaryHACK` | [`bounties/bounty_p1_surface_code_femoco.py`](bounty_p1_surface_code_femoco.py) | `d=27, p_phys=0.001 -> P_L=3.00e-16, Q_phys=428,652 · PASS` | `P.11`, `P.12` |
| **`BOUNTY-E1`** | `$100M` XPRIZE Carbon Removal & IStructE Low-Carbon Benchmark | [`bounties/bounty_e1_simp_carbon_slab.py`](bounty_e1_simp_carbon_slab.py) | `V/V0=0.35 -> Net CO2=39.4 kg/m2 (<45 target), c/c0=1.224 · PASS` | `E.11`, `E.12` |
| **`BOUNTY-A1`** | `$1M` Holcim Awards & `$3M` Global Cooling Prize | [`bounties/bounty_a1_graphic_statics_sky_cooling.py`](bounty_a1_graphic_statics_sky_cooling.py) | `L=16m, f/L=0.16, H=100kN, 0kg rebar, q_net=98.4 W/m2, dT=-5.2C · PASS` | `A.11`, `A.12` |
| **`BOUNTY-P2`** | Symbolic PDE Discovery (`PySR` + `PySINDy` Pareto Frontier) | [`bounties/bounty_p2_symbolic_pde_discovery.py`](bounty_p2_symbolic_pde_discovery.py) | `terms=['u*u_x', 'u_xx'] law='-u * u_x + 0.10 * u_xx' · PASS` | `P.11`, `P.12` |
| **`BOUNTY-M2`** | `PhysLean` Gauge Anomaly Cancellation & Tensor Network DMRG | [`bounties/bounty_m2_physlean_tensor_anomaly.py`](bounty_m2_physlean_tensor_anomaly.py) | `Tr[Y^3]=0.0, E0/N=-1.273240, S_vN=0.883 · PASS` | `M.11`, `M.12` |
