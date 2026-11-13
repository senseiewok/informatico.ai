# Informatico.ai Volume VI — Grounding Audit & Submit-on-Publish Outreach Kit

## 1. Grounding Audit Summary (`T0–T3` Truth Boundary)

All **48 Informatico.ai Folios** (and **40 CF Folios** = **88 total essays**) pass `python -X utf8 tools/check_folio_citations.py --include-informatico --offline` with **`fail=0 warn=0 unchecked=0`**. Every Volume VI Folio (`E.11–E.12`, `A.11–A.12`, `P.11–P.12`, `M.11–M.12`) is anchored to its own unique Crossref-verified primary DOI:

| Folio | Primary Anchor DOI (Crossref Verified) | Open-Source / Formal Verification Stack |
| :--- | :--- | :--- |
| **`E.11`** | `10.1007/s001580050176` (Sigmund 2001 SIMP) & `10.1109/TAC.2002.803532` (Smith 2002 Inerter) | `FEniCS/dolfinx` + `anthropics/formal-math` |
| **`E.12`** | `10.1109/TAC.2016.2638961` (Ames et al. 2017 Control Barrier Functions) | `anthropics/theorem-riscv` + `PyPSA/PyPSA` |
| **`A.11`** | `10.1016/j.cad.2015.01.006` (Akbarzadeh, Van Mele & Block 2015 3D Graphic Statics) | `compas-dev/compas` |
| **`A.12`** | `10.1126/science.aat9513` (Mandal et al. 2018 Porous Radiative Sky-Cooling, *Science*) | `NREL/EnergyPlus` + `compas-dev/compas` |
| **`P.11`** | `10.1103/PhysRevA.86.032324` (Fowler et al. 2012 Surface Codes) & `10.1073/pnas.1619152114` (Reiher et al. 2017 FeMoCo) | `quantumlib/Stim` + `pyscf/pyscf` |
| **`P.12`** | `10.1007/s00222-003-0316-5` (Golse & Saint-Raymond 2003 Boltzmann-to-Navier–Stokes) & `arXiv:2503.01800` (Deng–Hani–Ma 2025) | `FEniCS/dolfinx` + `GraphCast` |
| **`M.11`** | `10.4007/annals.2015.182.1.9` (Bourgain & Demeter 2015 $\ell^2$ Decoupling) & `arXiv:2502.17655` (Wang–Zahl 2025 3D Kakeya) | `anthropics/formal-math` (`Zeta23.lean`, `Challenge/XiPrime.lean`) |
| **`M.12`** | `10.1145/1568318.1568324` (Regev 2009 Learning With Errors) & `NIST FIPS 203` (ML-KEM) | `anthropics/formal-math` (`ETHIsFalse.lean`, `EightSquare.lean`) + `open-quantum-safe/liboqs` |

---

## 2. Should We Submit as We Publish? (The Two-Track Decision Rule)

- **Track A — YES, Submit Immediately as We Publish (Open-Source Registries, Benchmark Hubs & Educational Showcases):**
  - **Unitary Foundation / `Metriq.info`** (`BOUNTY-P1` · Folio `P.11`): Welcomes interactive quantum error-correction benchmarks and resource-estimation tools immediately upon publication.
  - **Lean Prover Zulip (`#formalization` / `#showcase`) & `erdosproblems.com` Discussion Thread** (`BOUNTY-M1` · Folios `M.01`, `M.02`, `M.11`, `M.12`): Welcomes interactive blueprint visualizers, educational expositions of `anthropics/fermats-last-theorem` and `anthropics/formal-math`, and verified Lean 4 companions.
  - **ETH Zürich COMPAS / Block Research Group & NREL EnergyPlus Showcases** (`BOUNTY-A1` · Folios `A.11`, `A.12`): Welcomes open-access bilingual (`EN` + `ES-MX`) interactive teaching monographs demonstrating 3D polyhedral graphic statics and radiative cooling.
  - **FEniCS Project (`dolfinx`) & PyPSA Community Showcases** (`BOUNTY-E1` · Folios `E.11`, `E.12`): Welcomes interactive browser companions with downloadable Python verifiers and AI `SKILL.md` specs.
- **Track B — DO NOT Email a Cash-Prize Claim Yet (Requires Novel Proof or Physical Hardware Pilot First):**
  - **Erdős Cash Bounties (\$500–\$10,000)** require a **new mathematical proof of an unsolved (`OPEN`) problem** verified in Lean 4 (`0 sorry`).
  - **XPRIZE Quantum (\$5M), XPRIZE Carbon Removal (\$100M), Global Cooling Prize (\$3M), and Holcim Awards (\$1M)** require formal portal registration during open competition windows plus either a novel quantum algorithm paper (`XPRIZE Quantum`) or instrumented physical hardware prototypes (`XPRIZE Carbon`, `Holcim`). Two of these have closed: XPRIZE Carbon Removal and the Global Cooling Prize. The 45 kg CO₂e/m² slab line and the vault and sky-cooling thresholds on the bounty pages are the folios' own design targets, not criteria of any prize.

---

## 3. Ready-to-Send Submit-on-Publish Emails & Community Notes

### Email 1 — Unitary Foundation & `Metriq.info` (Folio `P.11` · `BOUNTY-P1`)

- **To:** `info@unitary.foundation` (or submit via `https://metriq.info/` / Unitary Foundation Discord `#showcase`)
- **Subject:** Open Bilingual Interactive Monograph & `SKILL.md` Verifier: Surface-Code Thresholds (`Stim`) + `FeMoCo` Nitrogenase Resource Estimation (`Informatico.ai` Folio P.11)

```text
Dear Unitary Foundation & Metriq Team,

We just published Volume VI of Informatico.ai—an open, zero-build, bilingual (English + Mexican Spanish) interactive scientific monograph series—and wanted to share Folio P.11 with the Unitary Foundation and Metriq community:

- Dedicated Bounty Folio B.02 (BOUNTY-P1 Story, Proof & Code): https://informatico.ai/bounties/b02/
- Dedicated Bounty Folio B.02 in Español (ES-MX): https://informatico.ai/es-mx/bounties/b02/
- Companion Long-Form Essay P.11 (EN / ES-MX): https://informatico.ai/physics/p11/ | https://informatico.ai/es-mx/physics/p11/
- All 6 Open-Bounty & Prize Folios Hub: https://informatico.ai/bounties/

What Folio P.11 provides for learners and researchers:
1. Interactive Surface-Code & Anyon Braiding Workbench: Readers scrub physical gate error rates (p_phys) against code distance (d) to watch logical error rates P_L ~ (p / p_th)^((d+1)/2) and active-volume T-factory footprints update in real time for FeMoCo [Fe7MoS9C] nitrogen fixation (anchored to Fowler et al. 2012, DOI 10.1103/PhysRevA.86.032324, and Reiher et al. 2017, DOI 10.1073/pnas.1619152114).
2. Direct Links to Open-Source Quantum Tooling: Highlights quantumlib/Stim, PySCF, Qiskit, PennyLane, and unitaryHACK / XPRIZE Quantum Applications.
3. Downloadable Python Verifier & Portable SKILL.md: Every page includes a zero-dependency Python verifier and an AI-agnostic SKILL.md companion so students and researchers can run the exact equations locally.

We would be honored to list Folio P.11 as a community educational resource on Metriq.info or share it with unitaryHACK participants. Thank you for everything you build for open quantum science!

Warm regards,
Informatico.ai Editorial & Engineering Lab
https://informatico.ai/
Public GitHub Repository (54 SKILL.md & Python Verifiers): https://github.com/senseiewok/informatico.ai
```

---

### Email 2 — Lean Prover Community / `erdosproblems.com` Educational Showcase (Folios `M.01`, `M.02`, `M.11`, `M.12` · `BOUNTY-M1`)

- **To:** Lean Zulip `#formalization` / `#general` showcase thread (or educational link note to `erdosproblems.com` maintainer)
- **Subject:** Interactive Bilingual Explorable Monographs for Lean 4 Formalizations (`fermats-last-theorem`, `formal-math`, `pfr`, `equational_theories`) + Open-Bounty Crucible

```text
Hi everyone,

We have published Volume VI of Informatico.ai, an open-access bilingual (EN + ES-MX) collection of interactive mathematical and physical monographs designed to make frontier formalizations tactile for students, engineers, and mathematicians:

- Dedicated Bounty Folio B.01 (BOUNTY-M1 Erdős Sidon Sets & Lean 4 Story, Proof & Code): https://informatico.ai/bounties/b01/ (ES-MX: https://informatico.ai/es-mx/bounties/b01/)
- Dedicated Bounty Folio B.06 (BOUNTY-M2 PhysLean Gauge Anomaly & DMRG Story, Proof & Code): https://informatico.ai/bounties/b06/ (ES-MX: https://informatico.ai/es-mx/bounties/b06/)
- All 6 Open-Bounty & Prize Folios Hub: https://informatico.ai/bounties/
- Folio M.01 (Fermat's Last Theorem & 13M-Line Lean 4 Blueprint): https://informatico.ai/math/m01/
- Folio M.02 (Riemann Zero-Density & Challenge/XiPrime.lean): https://informatico.ai/math/m02/
- Folio M.04 (Polynomial Freiman-Ruzsa teorth/pfr & 22M Magma Graph): https://informatico.ai/math/m04/
- Folio M.11 (Wang-Zahl 3D Kakeya & Guth-Maynard 30/13 Zero-Density): https://informatico.ai/math/m11/
- Folio M.12 (Anthropic formal-math ETHIsFalse.lean, EightSquare.lean & NIST FIPS 203 Lattices): https://informatico.ai/math/m12/

Note on Grounding: These essays are educational interactive companions and deterministic numeric verifiers (not new claims on open Erdős cash bounties). Each Folio links directly to the primary repositories (anthropics/fermats-last-theorem, anthropics/formal-math, teorth/pfr, teorth/equational_theories) and includes an interactive Counterfactual Axiom Knockout mode plus a downloadable Python verifier and SKILL.md.

Feedback from the formalization community is very welcome!

Best regards,
Informatico.ai Editorial & Engineering Lab
https://informatico.ai/
Public GitHub Repository (54 SKILL.md & Python Verifiers): https://github.com/senseiewok/informatico.ai
```

---

### Email 3 — ETH Zürich Block Research Group / `COMPAS` & `NREL EnergyPlus` Showcase (Folios `A.11`, `A.12` · `BOUNTY-A1`)

- **To:** `compas-dev` GitHub Discussions (`https://github.com/compas-dev/compas/discussions`) / Block Research Group outreach
- **Subject:** Showcase: Interactive Bilingual Monographs on 3D Polyhedral Graphic Statics (`COMPAS`) & Radiative Sky-Cooling (`Informatico.ai` Folios A.11 & A.12)

```text
Dear COMPAS & Block Research Group Team,

We wanted to share two new interactive, bilingual (English + Mexican Spanish) long-form monographs in Volume VI of Informatico.ai that highlight 3D polyhedral graphic statics and open-source computational form-finding with COMPAS:

- Dedicated Bounty Folio B.04 (BOUNTY-A1 Holcim & Global Cooling Prize Story, Proof & Code): https://informatico.ai/bounties/b04/ (ES-MX: https://informatico.ai/es-mx/bounties/b04/)
- Folio A.11 (3D Polyhedral Graphic Statics, Maxwell-Rankine Reciprocal Polyhedra & Zero-Rebar Vaults): https://informatico.ai/architecture/a11/
  (Anchored to Akbarzadeh, Van Mele & Block 2015, DOI 10.1016/j.cad.2015.01.006, and Heyman 1995, DOI 10.1017/cbo9781107050310)
- Folio A.12 (Tensegrity Cable-Strut Domes & 8-13 um Radiative Sky-Cooling Envelopes): https://informatico.ai/architecture/a12/
  (Anchored to Mandal et al. 2018, DOI 10.1126/science.aat9513, and Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4)

Both monographs feature live zero-build SVG + WebGL2 observatories where architecture and civil-engineering students can scrub rise-to-span ratios and polyhedral force-face areas, download a standalone Python equilibrium verifier, and link directly to compas-dev/compas.

Thank you for making COMPAS open to the world!

Warm regards,
Informatico.ai Editorial & Engineering Lab
https://informatico.ai/
Public GitHub Repository (54 SKILL.md & Python Verifiers): https://github.com/senseiewok/informatico.ai
```

---

### Email 4 — `FEniCS Project` (`dolfinx`) & `PyPSA` Community Showcase (Folios `E.11`, `E.12` · `BOUNTY-E1`)

- **To:** FEniCS Discourse (`https://fenicsproject.discourse.group/` `#showcase`) & PyPSA Community
- **Subject:** Showcase: Interactive Monographs on SIMP Topology Optimization (`FEniCS/dolfinx`) & Verified Renewable Grid Inertia (`PyPSA` + `Rocq RISC-V`)

```text
Dear FEniCS & PyPSA Maintainers,

We just published Folios E.11 and E.12 in Volume VI of Informatico.ai (in English and Mexican Spanish) to help civil and electrical engineers explore continuum topology optimization and grid-forming control using open-source solvers:

- Dedicated Bounty Folio B.03 (BOUNTY-E1 XPRIZE Carbon & IStructE Low-Carbon Slab Story, Proof & Code): https://informatico.ai/bounties/b03/ (ES-MX: https://informatico.ai/es-mx/bounties/b03/)
- Dedicated Bounty Folio B.05 (BOUNTY-P2 Symbolic PDE Discovery Story, Proof & Code): https://informatico.ai/bounties/b05/ (ES-MX: https://informatico.ai/es-mx/bounties/b05/)
- Folio E.11 (SIMP Topology Optimization, Michell Funicular Trusses & Skyscraper Inerter Damping): https://informatico.ai/engineering/e11/
  (Anchored to Sigmund 2001, DOI 10.1007/s001580050176, and Smith 2002, DOI 10.1109/TAC.2002.803532; links directly to FEniCS/dolfinx)
- Folio E.12 (Machine-Checked Silicon-to-Grid Safety: 180M-Line Rocq RISC-V Verification, Control Barrier Functions & Firefly-Synchronized Grids): https://informatico.ai/engineering/e12/
  (Anchored to Ames et al. 2017, DOI 10.1109/TAC.2016.2638961; links directly to PyPSA/PyPSA and anthropics/theorem-riscv)

Each essay pairs an interactive SVG/WebGL2 workbench with a downloadable Python verifier and an AI-agnostic SKILL.md file so readers can move seamlessly from browser intuition to FEniCS/dolfinx and PyPSA scripts.

Warm regards,
Informatico.ai Editorial & Engineering Lab
https://informatico.ai/
Public GitHub Repository (54 SKILL.md & Python Verifiers): https://github.com/senseiewok/informatico.ai
```
