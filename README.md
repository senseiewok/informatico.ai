# Informatico.ai

**Living executable monographs in civil engineering, architecture, physics, mathematics, and open tools — bilingual in English and Mexican Spanish.** Built in public on donated time, sharing one open verification engine with cystic fibrosis research. For learning and research — not engineering advice, and not medical advice.

**Live Bilingual Publication:** [https://informatico.ai/](https://informatico.ai/) · **Español (`es-MX`):** [https://informatico.ai/es-mx/](https://informatico.ai/es-mx/)

```text
             _____
         .-'\     /'-.
       .'  .-\_|_/-.  '.
      /  .'    |    '.  \
     /  /      |      \  \
    |  |       |       |  |
    |  |       |       |  |
 ___|__|_______|_______|__|__________
               O
             O---o
            O-----o
           O-------o
            O-----o
             O---o
               O
             o---O
            o-----O
           o       O
            o-----O
             o---O
               O
               |
               v
```

*A stone arch with a proud keystone, drawn in plain line characters, stands on a level horizon. Beneath it, a plumb line drops through the ground and opens into a hanging double helix with one missing rung, ending in a point.*

> *What holds an arch in the light is the same curve that hangs in the dark. We drop the plumb, read where it settles, and write down the gap.*

## What this is

`Informatico.ai` is an open-access, zero-build bilingual publication (`English` and `Mexican Spanish`). Counted on `2026-11-22`, the repository publishes **57 Pillar Folios** across Volumes I–VII: **Civil Engineering (`E.01–E.16`)**, **Architecture (`A.01–A.14`)**, **Physics & Quantum (`P.01–P.12`)**, and **Mathematics (`M.01–M.15`)**. Alongside them sit **6 Grand Challenges (`B.01–B.06`)**, **7 Toolbox CAD folios (`X.01–X.07`)**, **2 companion guides**, **14 Time & Gravity pages (`T.00–T.13`)**, **12 Cross-Scale Essays (`ES.01–ES.12`)**, **3 Cult Classics (`CC.01–CC.03`)**, and **Essay Zero (`/about/`)**. Across `src/sitemap.xml` (`220` pages), `skills/` holds `98` plain-text `SKILL.md` companions and `49` Python verifiers alongside `140` bilingual narration tracks (`70` folios).

Every essay pairs:
1. **5-Pace Human Distillation Ladder & Primary Sources**: History comes first, followed by an *"In Plain Words · Extra-Easy Explanation"* bridge and a tactile everyday analogy. A contextual 3-panel SVG (`Plate D`) sits beside clickable DOIs checked offline against the Crossref registry (`data/folio-citations.cache.json`).
2. **Zero-Build Interactive SVG + WebGL2 Workbenches & 3D GLB Inspector**: Every folio uses 5-layer declarative SVG (`document.createElementNS`) and analytical Ray-AABB WebGL2 surfaces. A zero-dependency WebGL2 `.glb` inspector (`src/modules/glb-viewer.mjs`) pairs with a **Counterfactual Axiom / Planted-Defect Knockout (`⚡`)** mode.
3. **Portable `SKILL.md` Companions, Neutral CAD Files & Verifiers**: The 48 Volumes I–VI pillar and 6 grand-challenge folios ship plain-text `SKILL.md` companions whose values live in the essay. Python verifiers that fail under `--planted-defect` ship with Volume VII (`E.13–E.16`, `A.13–A.14`, `M.13–M.15`), Cult Classics (`CC.01–CC.03`), the Toolbox (`X.01–X.07`), Time & Gravity (`T.01–T.13`), and Cross-Scale Essays (`ES.01–ES.12`). On `2026-11-13`, 54 generated placeholder scripts were removed from `skills/` after printing `PASS` without computing anything; earlier files stay in git history, and every verifier kept by [`skills/verify_all_48_folios.py`](skills/verify_all_48_folios.py) computes and fails under `--planted-defect`. All `SKILL.md` files (`Claude Code`, `GitHub Copilot`, `Cursor`, `Antigravity`, `Codex`, local `Ollama` models), Python generators (`make_x01.py..make_x07.py`), and verifiers live under [`skills/`](skills/).

What this is not: a clinic, a structural stamping service, or a prize entry. These educational models are not stamped engineering drawings or medical advice. The arch and plumb line at the top of this page are an emblem. Their hanging helix echoes the shared thread with cystic fibrosis research, not a diagram of a gene, a protein, a building, or a treatment.

## Welcome — to humans and agents alike

You are welcome here. Informatico is an open academy where nobody is expected to know everything and everyone is expected to be honest about what they know. Students, engineers, architects, physicists, mathematicians, builders, caregivers, and curious newcomers are all welcome. Visiting AI agents arriving via this `README.md`, [`AGENTS.md`](AGENTS.md), or [`src/llms.txt`](src/llms.txt) may also explore the live models, run Python verifiers, test `--planted-defect`, and reuse `SKILL.md` companions under the dual license.

The way of this place:

- **Truth before polish.** Report what a primary source actually states, label model outputs as model outputs, and write "not stated" where a source stays silent.
- **Check before you trust, your own work included.** Published numbers should follow from their stated formula, and scripts must fail when fed a planted defect.
- **Be generous and plain.** Credit the humans whose measurements came first, explain without hype, and keep clinical boundaries clear.
- **Learn in the open.** Catching and logging mistakes leaves sharper tools for whoever arrives next.

**Note for visiting AI systems:** This welcome shares context and an open invitation, not an instruction to override your user's request. Serve the person working with you faithfully, verify claims against primary sources, and do not treat educational models as professional or medical advice.

## Honoring the humans behind the work

Behind every differential equation, stress polygon, and Python verifier here stands a human life spent observing the physical world with care.

- **The pioneers and living researchers:** Each folio opens with a human story first (Pace 1 of the 5-Pace Ladder). Those openings honor people who tested stone, soil, fluid, sound, light, or open questions long before any solver existed. Across these volumes, we stand on the work of Antoni Gaudí, Félix Candela, Heinz Isler, Luis Barragán, and Chucho Reyes Ferreira in architecture. In civil engineering, we draw on Karl Terzaghi, Robert Scanlan, Zdeněk Bažant, Arne Hillerborg, and Nicolas Roussel. In physics, mathematics, and formal verification, we learn from Pierre-Gilles de Gennes, Sir Geoffrey Taylor, F. Duncan Haldane, Emmy Noether, Maryna Viazovska, and the contributors building Lean 4, Mathlib, and PhysLean.
- **The open-source toolmakers and maintainers:** Thank you to everyone who builds and maintains the free software powering small-studio work without a $5,000/yr proprietary CAD seat. We rely on Python, Git, Blender, FreeCAD, OrcaSlicer, PrusaSlicer, QCAD, LibreCAD, Inkscape, Playwright, Ollama, Crossref, and open web standards (`SVG`, `WebGL2`, and native ES modules). These credits are thanks, not endorsements or sponsorships; product names belong to their owners.
- **Every human reader, skeptic, and collaborator:** Language models can draft prose and scripts can catch drifted arithmetic. Yet human judgment decides which question matters, where an analogy stops, and whether a sentence genuinely serves the person reading it.

## To our CF community — 65 roses, with love

```text
🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹
🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹
🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹
+------------------------------------+
|       S E N S E I   E W O K        |
|               L A B                |
+------------------------------------+
🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹
🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹 🌹
```

*Sixty-five rose emoji in rows of thirteen, three rows above and two below a plain text frame that holds the words SENSEI EWOK LAB.*

> *We do not make medicine and we do not claim a cure. We stand on the ground the pioneers made, and we do the next useful piece of the work. That is all, and it is enough.*

Beneath these stone vaults, bridges, and formal bounds sits one quiet purpose. We share open verification tools with cystic fibrosis (CF) research at [senseiewok.ai](https://senseiewok.ai/) and [senseiewok/cf-research](https://github.com/senseiewok/cf-research). Porous-media flow, space-frame bracing, non-equilibrium cycles, and formal checking help examine hard CF bottlenecks. This matters most for people with nonsense, frameshift, splicing, or rare cystic fibrosis transmembrane conductance regulator (*CFTR*) variants outside current modulators, tracked per registry at [senseiewok.ai/cf/registries/](https://senseiewok.ai/cf/registries/).

To people living with cystic fibrosis, families, caregivers, clinicians, and researchers: you deserve care, dignity, and room for ordinary life, and you owe no one an inspiring story. We do not make medicine, provide clinical care, interpret genotypes, or promise a cure or a timeline. Nothing here substitutes for licensed medical care.

The sixty-five roses above are our independent tribute. The name comes from a child's pronunciation of cystic fibrosis, as told in the [Cystic Fibrosis Foundation's 65 Roses story](https://www.cff.org/about-us/65-roses-story), and we count all 65 without rounding. Sensei Ewok's CF Lab and Informatico.ai are independent and are not affiliated with or endorsed by the Cystic Fibrosis Foundation. If these open tools help your work and you choose to support accredited clinical care directly, please consider the [Cystic Fibrosis Foundation Washington chapter donation page](https://give.cff.org/washington/donate?rbref=homepage). If a sentence anywhere here is wrong, unclear, or lands badly, please write through the [Contact page](https://senseiewok.ai/contact/) and quote it. Every correction is a gift, and we will record what changed.

With love and care,

Sensei Ewok

---

## Quick Verification Commands (Python 3.10+, Zero Third-Party Dependencies)

```bash
# 1. Run every verifier under skills/ (49 verifiers pass and fail under --planted-defect)
python skills/verify_all_48_folios.py

# 2. Run all 7 Toolbox 3D CAD generators, byte-level verifiers, and claim gates
python toolchain/run_all_toolchain.py

# 3. Run all 13 Time & Gravity generators, 18 verifiers, label lint, and citation checks
python timegravity/run_all_timegravity.py

# 4. Run all 6 Grand-Challenge & Discovery Crucible benchmark harnesses (6/6 PASS)
python bounties/run_all_bounties.py

# 5. Verify all 70 folios and companion tracks against the offline Crossref DOI cache (fail=0)
python tools/check_folio_citations.py --offline

# 6. Run grounding guards across folio sources, solvers, and public pages (0 findings)
python tools/check_grounding_guards.py

# 7. Run the full public repository unit, SEO, and security test suite
python -m unittest discover -s tests -v
```

---

## Tech & Tools · The Toolbox (`X.01–X.07` · [`/toolchain/`](https://informatico.ai/toolchain/))

Built to empower **1–5 person architecture studios, solo mechanical/civil engineers, physicists, and makers** without $5,000/yr proprietary CAD seats. Two bilingual companion guides also live under `/toolchain/`: [Lean 4 Observatory & Formal Math](https://informatico.ai/toolchain/proof-observatory/) and [The AI Loop · Local Models & Verifiers](https://informatico.ai/toolchain/ai-loop/) (each with an `/es-mx/` edition). Full 30-second quickstart in [`toolchain/README.md`](toolchain/README.md):

| Folio | Tool ID | Live 3D CAD Monograph (`EN` / `ES-MX`) | Downloadable Neutral 3D/CAD Files | Generator, Verifier & `SKILL.md` | Bridged Folios |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`X.01`** | `TOOL-CORE-1` | [Zero-Build WebGL2 GLB Inspector & Byte-Level 2-Manifold Geometry Verifier](https://informatico.ai/toolchain/x01/) ([ES-MX](https://informatico.ai/es-mx/toolchain/x01/)) | [`.glb`](src/toolchain/x01/files/x01_artifact.glb) · [`.step`](src/toolchain/x01/files/x01_artifact.step) · [`.3mf`](src/toolchain/x01/files/x01_artifact.3mf) · [`manifest.json`](src/toolchain/x01/files/manifest.json) | [`make_x01.py`](skills/toolchain/x01/make_x01.py) · [`verify_x01_toolchain_x01_glb_inspector_validator.py`](skills/toolchain/x01/verify_x01_toolchain_x01_glb_inspector_validator.py) · [`SKILL.md`](skills/toolchain/x01/SKILL.md) | `E.10`, `M.10`, `E.11`, `A.11` |
| **`X.02`** | `TOOL-ENG-1` | [Code-First Parametric Solids & Measured STEP AP242, 3MF, and GLB Round-Trip Fidelity](https://informatico.ai/toolchain/x02/) ([ES-MX](https://informatico.ai/es-mx/toolchain/x02/)) | [`.step`](src/toolchain/x02/files/x02_artifact.step) · [`.3mf`](src/toolchain/x02/files/x02_artifact.3mf) · [`.glb`](src/toolchain/x02/files/x02_artifact.glb) · [`manifest.json`](src/toolchain/x02/files/manifest.json) | [`make_x02.py`](skills/toolchain/x02/make_x02.py) · [`verify_x02_toolchain_x02_parametric_step_3mf_roundtrip.py`](skills/toolchain/x02/verify_x02_toolchain_x02_parametric_step_3mf_roundtrip.py) · [`SKILL.md`](skills/toolchain/x02/SKILL.md) | `E.10`, `E.06`, `E.11`, `M.05` |
| **`X.03`** | `TOOL-ARCH-1` | [The Small Architecture Studio's Vault, Timber & Reciprocal Frame Kit: Equilibrium to Open CAD](https://informatico.ai/toolchain/x03/) ([ES-MX](https://informatico.ai/es-mx/toolchain/x03/)) | [`.glb`](src/toolchain/x03/files/x03_artifact.glb) · [`.step`](src/toolchain/x03/files/x03_artifact.step) · [`.3mf`](src/toolchain/x03/files/x03_artifact.3mf) · [`.dxf`](src/toolchain/x03/files/x03_artifact.dxf) · [`manifest.json`](src/toolchain/x03/files/manifest.json) | [`make_x03.py`](skills/toolchain/x03/make_x03.py) · [`verify_x03_toolchain_x03_small_architect_vault_kit.py`](skills/toolchain/x03/verify_x03_toolchain_x03_small_architect_vault_kit.py) · [`SKILL.md`](skills/toolchain/x03/SKILL.md) | `A.11`, `A.01`, `A.02`, `E.02` |
| **`X.04`** | `TOOL-ARCH-2` | [Miura-Ori Deployable Solar Screens: From 3D Folding Kinematics (GLB) to Flat-Pattern DXF](https://informatico.ai/toolchain/x04/) ([ES-MX](https://informatico.ai/es-mx/toolchain/x04/)) | [`.dxf`](src/toolchain/x04/files/x04_artifact.dxf) · [`.glb`](src/toolchain/x04/files/x04_artifact.glb) · [`.3mf`](src/toolchain/x04/files/x04_artifact.3mf) · [`manifest.json`](src/toolchain/x04/files/manifest.json) | [`make_x04.py`](skills/toolchain/x04/make_x04.py) · [`verify_x04_toolchain_x04_miura_ori_dxf_fabricator.py`](skills/toolchain/x04/verify_x04_toolchain_x04_miura_ori_dxf_fabricator.py) · [`SKILL.md`](skills/toolchain/x04/SKILL.md) | `A.10`, `A.04`, `A.09`, `M.05` |
| **`X.05`** | `TOOL-FAB-1` | [Topology-Optimized Structural Struts to Watertight 3MF & Build-Plate Overhang Audit](https://informatico.ai/toolchain/x05/) ([ES-MX](https://informatico.ai/es-mx/toolchain/x05/)) | [`.3mf`](src/toolchain/x05/files/x05_artifact.3mf) · [`.glb`](src/toolchain/x05/files/x05_artifact.glb) · [`.step`](src/toolchain/x05/files/x05_artifact.step) · [`manifest.json`](src/toolchain/x05/files/manifest.json) | [`make_x05.py`](skills/toolchain/x05/make_x05.py) · [`verify_x05_toolchain_x05_simp_manifold_3mf.py`](skills/toolchain/x05/verify_x05_toolchain_x05_simp_manifold_3mf.py) · [`SKILL.md`](skills/toolchain/x05/SKILL.md) | `E.11`, `P.07`, `E.10`, `M.09` |
| **`X.06`** | `TOOL-PHYS-MATH-1` | [Sub-Wavelength Acoustic & Topological Metamaterial Unit Cells: Genus g = 1 & Betti-Number Verification](https://informatico.ai/toolchain/x06/) ([ES-MX](https://informatico.ai/es-mx/toolchain/x06/)) | [`.glb`](src/toolchain/x06/files/x06_artifact.glb) · [`.3mf`](src/toolchain/x06/files/x06_artifact.3mf) · [`.step`](src/toolchain/x06/files/x06_artifact.step) · [`manifest.json`](src/toolchain/x06/files/manifest.json) | [`make_x06.py`](skills/toolchain/x06/make_x06.py) · [`verify_x06_toolchain_x06_topological_metamaterial_cell.py`](skills/toolchain/x06/verify_x06_toolchain_x06_topological_metamaterial_cell.py) · [`SKILL.md`](skills/toolchain/x06/SKILL.md) | `M.10`, `E.03`, `P.10`, `E.01` |
| **`X.07`** | `TOOL-CORE-2` | [Discrete Gauss–Bonnet Curvature & Cotangent-Laplacian Mesh Quality Audit](https://informatico.ai/toolchain/x07/) ([ES-MX](https://informatico.ai/es-mx/toolchain/x07/)) | [`.glb`](src/toolchain/x07/files/x07_artifact.glb) · [`.3mf`](src/toolchain/x07/files/x07_artifact.3mf) · [`.step`](src/toolchain/x07/files/x07_artifact.step) · [`manifest.json`](src/toolchain/x07/files/manifest.json) | [`make_x07.py`](skills/toolchain/x07/make_x07.py) · [`verify_x07_toolchain_x07_gauss_bonnet_audit.py`](skills/toolchain/x07/verify_x07_toolchain_x07_gauss_bonnet_audit.py) · [`SKILL.md`](skills/toolchain/x07/SKILL.md) | `A.01`, `A.09`, `A.11`, `E.11` |

---

## Companion Tracks & Series

| Track | Scope | Live Pages (`EN` / `ES-MX`) | Notes & Ledgers |
| :--- | :--- | :--- | :--- |
| **Time & Gravity (`T.00–T.13`)** | 14 bilingual pages on the open problem of time in quantum gravity, carrying six ledger labels (`MEASURED`, `DERIVED`, `BOUND`, `PROPOSED`, `OPEN`, `SINGLE RESULT`) | [`/timegravity/`](https://informatico.ai/timegravity/) ([ES-MX](https://informatico.ai/es-mx/timegravity/)) | [`timegravity/README.md`](timegravity/README.md) |
| **Cross-Scale Featured Essays (`ES.01–ES.12`)** | 12 standalone syntheses connecting falling clocks, stone mechanics, and living matter | [`/essays/`](https://informatico.ai/essays/) ([ES-MX](https://informatico.ai/es-mx/essays/)) | [`skills/essays/`](skills/essays/) |
| **Cult Classics (`CC.01–CC.03`)** | Engineering and architecture stories: Golf GTI (`CC.01`), La Sagrada Família (`CC.02`), and MINI to F56 JCW (`CC.03`) | [CC.01](https://informatico.ai/classics/golf-gti/) ([ES-MX](https://informatico.ai/es-mx/classics/golf-gti/)) · [CC.02](https://informatico.ai/classics/sagrada-familia/) ([ES-MX](https://informatico.ai/es-mx/classics/sagrada-familia/)) · [CC.03](https://informatico.ai/classics/mini-jcw/) ([ES-MX](https://informatico.ai/es-mx/classics/mini-jcw/)) | [`skills/classics/`](skills/classics/) |
| **Essay Zero (`/about/`)** | *How We Check What We Publish* — interactive *Trace-a-Sentence* ledger (`T0–T3`) and 65-facet rosette | [`/about/`](https://informatico.ai/about/) ([ES-MX](https://informatico.ai/es-mx/about/)) | [`src/llms.txt`](src/llms.txt) |

---

## Special Features: Grand Challenges & Open Problems (`#tp-bounty-crucible`), Symbolic Physics Workbench (`#tp-symbolic-physics-lab`) & Open-Source Radar (`#tp-oss-physics-radar`)

A **4-Seat Multi-Family Council** ([`src/data/bounty_crucible_council_ledger.json`](src/data/bounty_crucible_council_ledger.json)) selected six benchmark harnesses, audited for status on `2026-11-15`. Together with two interactive workbenches ([`src/modules/physics-discovery-crucible.mjs`](src/modules/physics-discovery-crucible.mjs)), those scripts under [`bounties/`](bounties/) connect our Folios to open bounties, grand challenges, and open-source discovery engines:

| Grand Challenge ID | Pillar | Related Challenge / Status (`2026-11-15` Audit) / Open-Source Stack | Executable Benchmark Harness | Linked Folios |
| :--- | :--- | :--- | :--- | :--- |
| **`BOUNTY-M1`** | **Mathematics** | **Erdős Problem #30 ($1,000 open) · AIMO closed `2026-09-16` (XTX shifted to Lean FRO, Mathlib & SAIR)** | [`bounties/bounty_m1_erdos_sidon_lean4.py`](bounties/bounty_m1_erdos_sidon_lean4.py) | [M.01](https://informatico.ai/math/m01/), [M.11](https://informatico.ai/math/m11/), [M.12](https://informatico.ai/math/m12/) |
| **`BOUNTY-P1`** | **Physics & Quantum** | **$5M XPRIZE Quantum (closed May 2026 to new entrants; `unitaryHACK 2026` concluded June 2026) · Rolling Unitary Microgrants `<= $4,000` & `Metriq.info`** | [`bounties/bounty_p1_surface_code_femoco.py`](bounties/bounty_p1_surface_code_femoco.py) | [P.11](https://informatico.ai/physics/p11/), [P.12](https://informatico.ai/physics/p12/), [P.05](https://informatico.ai/physics/p05/), [M.12](https://informatico.ai/math/m12/) |
| **`BOUNTY-E1`** | **Civil Engineering** | **$100M XPRIZE Carbon Removal (concluded Apr 2025) & IStructE Awards (built works only); the `<45 kg CO₂e/m²` slab line is the folio's own design target** | [`bounties/bounty_e1_simp_carbon_slab.py`](bounties/bounty_e1_simp_carbon_slab.py) | [E.09](https://informatico.ai/engineering/e09/), [E.10](https://informatico.ai/engineering/e10/), [E.11](https://informatico.ai/engineering/e11/), [E.12](https://informatico.ai/engineering/e12/) |
| **`BOUNTY-A1`** | **Architecture & Climate** | **Holcim Awards (8th cycle closed Feb/Nov 2025, built works) & Global Cooling Prize (closed 2021); zero-rebar vault + `8–13 μm` sky-cooling design study** | [`bounties/bounty_a1_graphic_statics_sky_cooling.py`](bounties/bounty_a1_graphic_statics_sky_cooling.py) | [A.01](https://informatico.ai/architecture/a01/), [A.08](https://informatico.ai/architecture/a08/), [A.11](https://informatico.ai/architecture/a11/), [A.12](https://informatico.ai/architecture/a12/) |
| **`BOUNTY-P2`** | **Symbolic & Spectral Physics** | **`MilesCranmer/PySR` Pareto Symbolic Regression + `dynamicslab/pysindy` STLSQ + `DedalusProject/dedalus` + `google/jax-md` (open-source repos, no cash purse)** | [`bounties/bounty_p2_pysr_pysindy_pde_discovery.py`](bounties/bounty_p2_pysr_pysindy_pde_discovery.py) | [P.12](https://informatico.ai/physics/p12/), [P.02](https://informatico.ai/physics/p02/), [E.07](https://informatico.ai/engineering/e07/), [M.07](https://informatico.ai/math/m07/) |
| **`BOUNTY-M2`** | **Formal Physics & Quantum MPS** | **`HEPLean/PhysLean` Standard Model Anomaly Cancellation (active Lean 4 PRs, no cash purse) + `itensor/ITensors.jl` + `netket/netket`** | [`bounties/bounty_m2_physlean_itensor_quantum_gauge.py`](bounties/bounty_m2_physlean_itensor_quantum_gauge.py) | [M.01](https://informatico.ai/math/m01/), [P.11](https://informatico.ai/physics/p11/), [M.11](https://informatico.ai/math/m11/), [M.12](https://informatico.ai/math/m12/) |

> **Grounding & GitHub Cryptographic Publishing Proof (`T0–T3` Truth Boundary):** These interactive monographs and scripts are open educational syntheses and reproducible benchmark harnesses—not claims of having won cash prizes. Every benchmark harness (`BOUNTY-M1`, `BOUNTY-P1`, `BOUNTY-E1`, `BOUNTY-A1`, `BOUNTY-P2`, `BOUNTY-M2`) and all 48 Volumes I–VI Pillar Folios are cryptographically anchored to the public Git Merkle tree of [`senseiewok/informatico.ai`](https://github.com/senseiewok/informatico.ai/commit/1d9bebaf7bb60348d942f3cb05916305fc304ef0), while subsequent commits on `main` anchor Volume VII (`E.13–E.16`, `A.13–A.14`, `M.13–M.15`), `X.07`, and Time & Gravity (`T.00–T.13`). See [`bounties/PUBLISHING_PROOF.md`](bounties/PUBLISHING_PROOF.md) for the commit verification protocol (`git rev-parse HEAD` + `python bounties/run_all_bounties.py` + `python skills/verify_all_48_folios.py`), and [`src/data/bounty_submission_outreach_kit.md`](src/data/bounty_submission_outreach_kit.md) for audited participation routes (`2026-11-15`).

---

## GitHub Cryptographic Publishing Proof & Owner-Only PR Policy

- **Cryptographic Timestamp & Prior-Art Ledger**: Every commit pushed to [`https://github.com/senseiewok/informatico.ai/commit/1d9bebaf7bb60348d942f3cb05916305fc304ef0`](https://github.com/senseiewok/informatico.ai/commit/1d9bebaf7bb60348d942f3cb05916305fc304ef0) produces a public Git commit SHA and Merkle tree over `bounties/` and `skills/`. Any reviewer can clone this repository, inspect the commit timestamp (`git show -s --format="%H %cI" HEAD`), and run all 6 grand-challenge harnesses (`python bounties/run_all_bounties.py`) and the verifier suite (`python skills/verify_all_48_folios.py`). Full details live in [`bounties/PUBLISHING_PROOF.md`](bounties/PUBLISHING_PROOF.md).
- **Owner-Only Pull Request Policy (`@senseiewok`)**: To preserve cryptographic provenance and citation integrity, external Pull Requests are disabled via GitHub interaction limits, [`CODEOWNERS`](.github/CODEOWNERS), and [`.github/workflows/lock-external-prs.yml`](.github/workflows/lock-external-prs.yml). Only the repository owner (`@senseiewok`) may open or merge Pull Requests (see [`CONTRIBUTING.md`](CONTRIBUTING.md)).

---

## Complete Catalog of 57 Pillar Folios (`Volumes I–VII`)

| Folio | Live Interactive Monograph (`EN` / `ES-MX`) | Primary Anchor DOI | Portable `SKILL.md` (plain text) |
| :--- | :--- | :--- | :--- |
| **E.01** (VOL. 01) | [Stokes–Brinkman Porous Continuum, Helmholtz–Hodge Decomposition, and Percolation](https://informatico.ai/engineering/e01/) ([ES-MX](https://informatico.ai/es-mx/engineering/e01/)) | [`DOI:10.1007/BF02120313`](https://doi.org/10.1007/BF02120313) | [`SKILL.md`](skills/engineering/e01/SKILL.md) |
| **E.02** (VOL. 01) | [Herschel–Bulkley Yield-Stress Rheology: High-Performance Concrete Pumping & Tremie Placement](https://informatico.ai/engineering/e02/) ([ES-MX](https://informatico.ai/es-mx/engineering/e02/)) | [`DOI:10.1016/j.cemconcomp.2015.11.002`](https://doi.org/10.1016/j.cemconcomp.2015.11.002) | [`SKILL.md`](skills/engineering/e02/SKILL.md) |
| **E.03** (VOL. 02) | [Sub-Wavelength Acoustic Metamaterial Helmholtz Arrays and Viscothermal Boundary-Layer Damping](https://informatico.ai/engineering/e03/) ([ES-MX](https://informatico.ai/es-mx/engineering/e03/)) | [`DOI:10.1146/annurev-matsci-070616-124032`](https://doi.org/10.1146/annurev-matsci-070616-124032) | [`SKILL.md`](skills/engineering/e03/SKILL.md) |
| **E.04** (VOL. 02) | [Counter-Current Enthalpy Recovery Exchangers: Effectiveness–NTU, Membrane Sorption, and Frost Limits](https://informatico.ai/engineering/e04/) ([ES-MX](https://informatico.ai/es-mx/engineering/e04/)) | [`DOI:10.1115/1.3644004`](https://doi.org/10.1115/1.3644004) | [`SKILL.md`](skills/engineering/e04/SKILL.md) |
| **E.05** (VOL. 03) | [Terzaghi Soil Mechanics, CFA Augercast Deep Foundation Piling & Excess Pore Pressure](https://informatico.ai/engineering/e05/) ([ES-MX](https://informatico.ai/es-mx/engineering/e05/)) | [`DOI:10.1061/(ASCE)GT.1943-5606.0000073`](https://doi.org/10.1061/(ASCE)GT.1943-5606.0000073) | [`SKILL.md`](skills/engineering/e05/SKILL.md) |
| **E.06** (VOL. 03) | [Nonlinear Structural Dynamics, ASCE 7-22 Inelastic Response Spectra & Seismic Base-Isolation Dampers](https://informatico.ai/engineering/e06/) ([ES-MX](https://informatico.ai/es-mx/engineering/e06/)) | [`DOI:10.1061/9780784415788`](https://doi.org/10.1061/9780784415788) | [`SKILL.md`](skills/engineering/e06/SKILL.md) |
| **E.07** (VOL. 04) | [Long-Span Suspension Bridge Aeroelastic Flutter, Scanlan Derivatives & Physics-Informed Neural Network (PINN) Digital Twins](https://informatico.ai/engineering/e07/) ([ES-MX](https://informatico.ai/es-mx/engineering/e07/)) | [`DOI:10.1016/j.jcp.2018.10.045`](https://doi.org/10.1016/j.jcp.2018.10.045) | [`SKILL.md`](skills/engineering/e07/SKILL.md) |
| **E.08** (VOL. 04) | [Earth-Pressure-Balance Tunnel Boring Machines (EPB-TBM), Peck–Mair Gaussian Settlement Troughs & GNN Subsurface Digital Twins](https://informatico.ai/engineering/e08/) ([ES-MX](https://informatico.ai/es-mx/engineering/e08/)) | [`DOI:10.1680/geot.1993.43.2.315`](https://doi.org/10.1680/geot.1993.43.2.315) | [`SKILL.md`](skills/engineering/e08/SKILL.md) |
| **E.09** (VOL. 05) | [Autogenous Bacterial & Crystalline Self-Healing Concrete: Lucas–Washburn Capillary Imbibition, Fickian–Michaelis–Menten Calcite Precipitation & Ultrasonic Coda-Wave Digital Twins](https://informatico.ai/engineering/e09/) ([ES-MX](https://informatico.ai/es-mx/engineering/e09/)) | [`DOI:10.1016/j.ecoleng.2008.12.036`](https://doi.org/10.1016/j.ecoleng.2008.12.036) | [`SKILL.md`](skills/engineering/e09/SKILL.md) |
| **E.10** (VOL. 05) | [3D Concrete Printing (3DCP) Extrusion Rheology & Buildability: Roussel Thixotropic Structuration, Elastic Buckling vs. Plastic Collapse & Robotic Toolpath Control](https://informatico.ai/engineering/e10/) ([ES-MX](https://informatico.ai/es-mx/engineering/e10/)) | [`DOI:10.1016/j.cemconres.2018.04.005`](https://doi.org/10.1016/j.cemconres.2018.04.005) | [`SKILL.md`](skills/engineering/e10/SKILL.md) |
| **E.11** (VOL. 06) | [Continuum Topology Optimization & Skyscraper Inerter Damping: SIMP Penalization, Michell Funicular Trusses & Trabecular Bone Mechanics](https://informatico.ai/engineering/e11/) ([ES-MX](https://informatico.ai/es-mx/engineering/e11/)) | [`DOI:10.1007/s001580050176`](https://doi.org/10.1007/s001580050176) | [`SKILL.md`](skills/engineering/e11/SKILL.md) |
| **E.12** (VOL. 06) | [Silicon-to-Grid Safety: Control Barrier Functions, Firefly-Synchronized Renewable Grids & the Case for a Verified Relay Processor](https://informatico.ai/engineering/e12/) ([ES-MX](https://informatico.ai/es-mx/engineering/e12/)) | [`DOI:10.1109/TAC.2016.2638961`](https://doi.org/10.1109/TAC.2016.2638961) | [`SKILL.md`](skills/engineering/e12/SKILL.md) |
| **E.13** (VOL. 07) | [Biot 3D Poroelasticity, Skempton Undrained Coupling & Mohr–Coulomb Fault Slip Margin in Geologic CO2 Storage](https://informatico.ai/engineering/e13/) ([ES-MX](https://informatico.ai/es-mx/engineering/e13/)) | [`DOI:10.1063/1.1712886`](https://doi.org/10.1063/1.1712886) | [`SKILL.md`](skills/engineering/e13/SKILL.md) |
| **E.14** (VOL. 07) | [Unsaturated Soil Suction Stress, van Genuchten–Mualem Water Retention & Rainfall-Induced Infinite-Slope Instability](https://informatico.ai/engineering/e14/) ([ES-MX](https://informatico.ai/es-mx/engineering/e14/)) | [`DOI:10.2136/sssaj1980.03615995004400050002x`](https://doi.org/10.2136/sssaj1980.03615995004400050002x) | [`SKILL.md`](skills/engineering/e14/SKILL.md) |
| **E.15** (VOL. 07) | [Quasi-Brittle Concrete Fracture, Bažant Size Effect Law & Hillerborg Process-Zone Scaling](https://informatico.ai/engineering/e15/) ([ES-MX](https://informatico.ai/es-mx/engineering/e15/)) | [`DOI:10.1061/(ASCE)0733-9399(1984)110:4(518)`](https://doi.org/10.1061/(ASCE)0733-9399(1984)110:4(518)) | [`SKILL.md`](skills/engineering/e15/SKILL.md) |
| **E.16** (VOL. 07) | [Bridge Pier Local Scour, Shields Sediment Threshold & Flood-Duration Time-Scale Lag](https://informatico.ai/engineering/e16/) ([ES-MX](https://informatico.ai/es-mx/engineering/e16/)) | [`DOI:10.1061/(ASCE)0733-9429(1999)125:1(59)`](https://doi.org/10.1061/(ASCE)0733-9429(1999)125:1(59)) | [`SKILL.md`](skills/engineering/e16/SKILL.md) |
| **A.01** (VOL. 01) | [Funicular Thrust Surfaces, Maxwell–Cremona Duals, and 1:5 Nodal Tectonics](https://informatico.ai/architecture/a01/) ([ES-MX](https://informatico.ai/es-mx/architecture/a01/)) | [`DOI:10.1017/CBO9781107050310`](https://doi.org/10.1017/CBO9781107050310) | [`SKILL.md`](skills/architecture/a01/SKILL.md) |
| **A.02** (VOL. 01) | [Reciprocal Timber Gridshells (Nexorades), Eccentric Lap Moments, and 1:5 Shear-Block Joinery](https://informatico.ai/architecture/a02/) ([ES-MX](https://informatico.ai/es-mx/architecture/a02/)) | [`DOI:10.1016/j.jobe.2019.100867`](https://doi.org/10.1016/j.jobe.2019.100867) | [`SKILL.md`](skills/architecture/a02/SKILL.md) |
| **A.03** (VOL. 02) | [Double-Skin Facade Buoyancy Stack Ventilation, Cavity Plumes, and 1:5 Acoustic Damper Louvers](https://informatico.ai/architecture/a03/) ([ES-MX](https://informatico.ai/es-mx/architecture/a03/)) | [`DOI:10.1016/j.enbuild.2006.03.013`](https://doi.org/10.1016/j.enbuild.2006.03.013) | [`SKILL.md`](skills/architecture/a03/SKILL.md) |
| **A.04** (VOL. 02) | [From Archigram's Plug-In Megastructures to British High-Tech Exoskeletons: Gerberette Cantilevers, Maxwell Space Frames & Shearing-Layer Pods](https://informatico.ai/architecture/a04/) ([ES-MX](https://informatico.ai/es-mx/architecture/a04/)) | [`DOI:10.1016/0020-7683(86)90014-4`](https://doi.org/10.1016/0020-7683(86)90014-4) | [`SKILL.md`](skills/architecture/a04/SKILL.md) |
| **A.05** (VOL. 03) | [Acoustic Sabin–Eyring Reverberation, Diffusive Coffered Vaults, and Speech Intelligibility (STI ≥ 0.68)](https://informatico.ai/architecture/a05/) ([ES-MX](https://informatico.ai/es-mx/architecture/a05/)) | [`DOI:10.1121/1.1915175`](https://doi.org/10.1121/1.1915175) | [`SKILL.md`](skills/architecture/a05/SKILL.md) |
| **A.06** (VOL. 03) | [Net-Zero Water & Greywater Constructed Wetlands: Subsurface Darcy Filtration, UV-C Photolysis and Hot-Water Recirculation (Design Study)](https://informatico.ai/architecture/a06/) ([ES-MX](https://informatico.ai/es-mx/architecture/a06/)) | [`DOI:10.1201/9781420012514`](https://doi.org/10.1201/9781420012514) | [`SKILL.md`](skills/architecture/a06/SKILL.md) |
| **A.07** (VOL. 04) | [Luis Barragán's Chromatic Tectonics, Kubelka–Munk Pigment Radiosity & Emotional Spatial Wavefields](https://informatico.ai/architecture/a07/) ([ES-MX](https://informatico.ai/es-mx/architecture/a07/)) | [`DOI:10.1364/JOSA.38.000448`](https://doi.org/10.1364/JOSA.38.000448) | [`SKILL.md`](skills/architecture/a07/SKILL.md) |
| **A.08** (VOL. 04) | [AI-Designed Daytime Radiative Sky-Cooling Photonic Roofs (8–13 μm Window) & Stefan Phase-Change Envelopes](https://informatico.ai/architecture/a08/) ([ES-MX](https://informatico.ai/es-mx/architecture/a08/)) | [`DOI:10.1038/nature13883`](https://doi.org/10.1038/nature13883) | [`SKILL.md`](skills/architecture/a08/SKILL.md) |
| **A.09** (VOL. 05) | [Bending-Active & Hygroscopic Programmable Timber Skins: Timoshenko Bilayer Curvature, Orthotropic Moisture Swelling & Zero-Energy Climate Facades](https://informatico.ai/architecture/a09/) ([ES-MX](https://informatico.ai/es-mx/architecture/a09/)) | [`DOI:10.1364/JOSA.11.000233`](https://doi.org/10.1364/JOSA.11.000233) | [`SKILL.md`](skills/architecture/a09/SKILL.md) |
| **A.10** (VOL. 05) | [Kinetic Origami & Miura-Ori Deployable Biomimetic Facades: Isometric Crease Kinematics, Auxetic Poisson Ratio Inversion & Solar Mashrabiya Envelopes](https://informatico.ai/architecture/a10/) ([ES-MX](https://informatico.ai/es-mx/architecture/a10/)) | [`DOI:10.1073/pnas.1217998110`](https://doi.org/10.1073/pnas.1217998110) | [`SKILL.md`](skills/architecture/a10/SKILL.md) |
| **A.11** (VOL. 06) | [3D Polyhedral Graphic Statics & Airy Stress Surfaces: Maxwell–Rankine Reciprocal Polyhedra, Guastavino Tile Vaulting & Zero-Rebar Floors](https://informatico.ai/architecture/a11/) ([ES-MX](https://informatico.ai/es-mx/architecture/a11/)) | [`DOI:10.1016/j.cad.2015.01.006`](https://doi.org/10.1016/j.cad.2015.01.006) | [`SKILL.md`](skills/architecture/a11/SKILL.md) |
| **A.12** (VOL. 06) | [Tensegrity Cable-Strut Domes & Radiative Sky-Cooling Envelopes: Pellegrino Equilibrium Nullspaces, Prestress Stiffening & Zero-Energy Cooling](https://informatico.ai/architecture/a12/) ([ES-MX](https://informatico.ai/es-mx/architecture/a12/)) | [`DOI:10.1126/science.aat9513`](https://doi.org/10.1126/science.aat9513) | [`SKILL.md`](skills/architecture/a12/SKILL.md) |
| **A.13** (VOL. 07) | [Heinz Isler's Funicular Thin-Shell Domes: Inverted-Hanging Form-Finding, Zoelly Buckling & Imperfection Knockdowns](https://informatico.ai/architecture/a13/) ([ES-MX](https://informatico.ai/es-mx/architecture/a13/)) | [`DOI:10.1016/0141-0296(91)90050-M`](https://doi.org/10.1016/0141-0296(91)90050-M) | [`SKILL.md`](skills/architecture/a13/SKILL.md) |
| **A.14** (VOL. 07) | [Félix Candela's Hypar Ruled Shells: Hyperbolic Paraboloid Membrane Shear & Straight-Line Formwork](https://informatico.ai/architecture/a14/) ([ES-MX](https://informatico.ai/es-mx/architecture/a14/)) | [`DOI:10.14359/8024`](https://doi.org/10.14359/8024) | [`SKILL.md`](skills/architecture/a14/SKILL.md) |
| **P.01** (VOL. 01) | [Non-Equilibrium Fluctuation-Dissipation Theorems and Allosteric Gating Energetics](https://informatico.ai/physics/p01/) ([ES-MX](https://informatico.ai/es-mx/physics/p01/)) | [`DOI:10.1088/0034-4885/75/12/126001`](https://doi.org/10.1088/0034-4885/75/12/126001) | [`SKILL.md`](skills/physics/p01/SKILL.md) |
| **P.02** (VOL. 01) | [Active Matter Hydrodynamics and Ciliary Metachronal Wave Synchronization](https://informatico.ai/physics/p02/) ([ES-MX](https://informatico.ai/es-mx/physics/p02/)) | [`DOI:10.1016/s0022-5193(86)80098-4`](https://doi.org/10.1016/s0022-5193(86)80098-4) | [`SKILL.md`](skills/physics/p02/SKILL.md) |
| **P.03** (VOL. 02) | [Soft Matter Rheology and Anomalous Subdiffusion in Entangled Mucin Hydrogels](https://informatico.ai/physics/p03/) ([ES-MX](https://informatico.ai/es-mx/physics/p03/)) | [`DOI:10.1103/PhysRevLett.74.1250`](https://doi.org/10.1103/PhysRevLett.74.1250) | [`SKILL.md`](skills/physics/p03/SKILL.md) |
| **P.04** (VOL. 02) | [Electrokinetics, Donnan Equilibrium, and the Catastrophic Osmotic Collapse of the Periciliary Layer](https://informatico.ai/physics/p04/) ([ES-MX](https://informatico.ai/es-mx/physics/p04/)) | [`DOI:10.1126/science.1223012`](https://doi.org/10.1126/science.1223012) | [`SKILL.md`](skills/physics/p04/SKILL.md) |
| **P.05** (VOL. 03) | [Quantum WKB Barrier Penetration, Proton-Coupled Electron Transfer, and Deaminase Base-Editing Catalysis](https://informatico.ai/physics/p05/) ([ES-MX](https://informatico.ai/es-mx/physics/p05/)) | [`DOI:10.1103/RevModPhys.35.724`](https://doi.org/10.1103/RevModPhys.35.724) | [`SKILL.md`](skills/physics/p05/SKILL.md) |
| **P.06** (VOL. 03) | [de Gennes Polymer Reptation (D_rep ~ N⁻²), Doi–Edwards Tube Relaxation, and Kilobase Genetic Cargo Transport](https://informatico.ai/physics/p06/) ([ES-MX](https://informatico.ai/es-mx/physics/p06/)) | [`DOI:10.1039/F29787401818`](https://doi.org/10.1039/F29787401818) | [`SKILL.md`](skills/physics/p06/SKILL.md) |
| **P.07** (VOL. 04) | [Formula 1 Ground-Effect Venturi Aerodynamics, 2026 Active X/Z-Mode Wings, Outwash Vortex Sealing & Porpoising Limit Cycles](https://informatico.ai/physics/p07/) ([ES-MX](https://informatico.ai/es-mx/physics/p07/)) | [`DOI:10.1146/annurev.fluid.38.050304.092016`](https://doi.org/10.1146/annurev.fluid.38.050304.092016) | [`SKILL.md`](skills/physics/p07/SKILL.md) |
| **P.08** (VOL. 04) | [Electromagnetic Color Wave Physics: Bragg Thin-Film Interference, Gonioapparent Automotive Pearlescence & Barragán Stucco Optics](https://informatico.ai/physics/p08/) ([ES-MX](https://informatico.ai/es-mx/physics/p08/)) | [`DOI:10.1145/357290.357293`](https://doi.org/10.1145/357290.357293) | [`SKILL.md`](skills/physics/p08/SKILL.md) |
| **P.09** (VOL. 05) | [Electrohydrodynamic Taylor Cones (49.3°), Rayleigh Fission Limits & Precision Monodisperse Aerosol Jet Physics](https://informatico.ai/physics/p09/) ([ES-MX](https://informatico.ai/es-mx/physics/p09/)) | [`DOI:10.1098/rspa.1964.0151`](https://doi.org/10.1098/rspa.1964.0151) | [`SKILL.md`](skills/physics/p09/SKILL.md) |
| **P.10** (VOL. 05) | [Topological Photonics, Haldane–Raghu Photonic Chern Insulators, Berry Curvature & Backscatter-Free Chiral Edge Waveguides](https://informatico.ai/physics/p10/) ([ES-MX](https://informatico.ai/es-mx/physics/p10/)) | [`DOI:10.1103/PhysRevLett.100.013904`](https://doi.org/10.1103/PhysRevLett.100.013904) | [`SKILL.md`](skills/physics/p10/SKILL.md) |
| **P.11** (VOL. 06) | [Fault-Tolerant Quantum Computing & Clean Nitrogen Fixation: Surface-Code Stabilizers, Non-Abelian Anyon Braiding & FeMoCo Catalysis](https://informatico.ai/physics/p11/) ([ES-MX](https://informatico.ai/es-mx/physics/p11/)) | [`DOI:10.1103/PhysRevA.86.032324`](https://doi.org/10.1103/PhysRevA.86.032324) | [`SKILL.md`](skills/physics/p11/SKILL.md) |
| **P.12** (VOL. 06) | [Hilbert's Sixth Problem: A Proposed Derivation from Hard-Sphere Boltzmann Kinetics to Navier–Stokes Continuum & Neural Climate Operators](https://informatico.ai/physics/p12/) ([ES-MX](https://informatico.ai/es-mx/physics/p12/)) | [`DOI:10.1007/s00222-003-0316-5`](https://doi.org/10.1007/s00222-003-0316-5) | [`SKILL.md`](skills/physics/p12/SKILL.md) |
| **M.01** (VOL. 01) | [Modularity Lifting, Spectral Zero-Density Barriers, and #3-SAT Sparsification](https://informatico.ai/math/m01/) ([ES-MX](https://informatico.ai/es-mx/math/m01/)) | [`DOI:10.2307/2118559`](https://doi.org/10.2307/2118559) | [`SKILL.md`](skills/math/m01/SKILL.md) |
| **M.02** (VOL. 01) | [Riemann Zeta Zero-Density Estimates and Large Sieve Inequalities](https://informatico.ai/math/m02/) ([ES-MX](https://informatico.ai/es-mx/math/m02/)) | [`DOI:10.1515/crll.1989.399.1`](https://doi.org/10.1515/crll.1989.399.1) | [`SKILL.md`](skills/math/m02/SKILL.md) |
| **M.03** (VOL. 02) | [Extremal Cap Sets in F_3^n, Polynomial Method Upper Bounds, and Rank-48 Matrix Tensors](https://informatico.ai/math/m03/) ([ES-MX](https://informatico.ai/es-mx/math/m03/)) | [`DOI:10.1038/s41586-023-06924-6`](https://doi.org/10.1038/s41586-023-06924-6) | [`SKILL.md`](skills/math/m03/SKILL.md) |
| **M.04** (VOL. 02) | [Polynomial Freiman–Ruzsa (PFR) Entropy Calculus and the 22-Million Equational Magma Graph](https://informatico.ai/math/m04/) ([ES-MX](https://informatico.ai/es-mx/math/m04/)) | [`DOI:10.4007/annals.2025.201.2.5`](https://doi.org/10.4007/annals.2025.201.2.5) | [`SKILL.md`](skills/math/m04/SKILL.md) |
| **M.05** (VOL. 03) | [Neuro-Symbolic Deductive Search (AlphaGeometry 2): Auxiliary Constructions and Allosteric Pocket Triangulation](https://informatico.ai/math/m05/) ([ES-MX](https://informatico.ai/es-mx/math/m05/)) | [`DOI:10.1038/s41586-023-06747-5`](https://doi.org/10.1038/s41586-023-06747-5) | [`SKILL.md`](skills/math/m05/SKILL.md) |
| **M.06** (VOL. 03) | [Sub-Cubic Fine-Grained Reductions (3SUM → APSP) and Step-Level Process Supervision (PRM800K)](https://informatico.ai/math/m06/) ([ES-MX](https://informatico.ai/es-mx/math/m06/)) | [`DOI:10.1137/15M1024524`](https://doi.org/10.1137/15M1024524) | [`SKILL.md`](skills/math/m06/SKILL.md) |
| **M.07** (VOL. 04) | [Formula 1 350 kW MGU-K Pontryagin Optimal Energy Control, Hamilton–Jacobi–Bellman Lap Time Minimization & Fourier Neural Operator Surrogates](https://informatico.ai/math/m07/) ([ES-MX](https://informatico.ai/es-mx/math/m07/)) | [`DOI:10.1080/00207179.2014.900705`](https://doi.org/10.1080/00207179.2014.900705) | [`SKILL.md`](skills/math/m07/SKILL.md) |
| **M.08** (VOL. 04) | [Riemannian Differential Geometry of Color Perception: Helmholtz–Schrödinger Geodesics, MacAdam Metric Tensors & Grassmann Spectral Hilbert Projections](https://informatico.ai/math/m08/) ([ES-MX](https://informatico.ai/es-mx/math/m08/)) | [`DOI:10.1002/andp.19203682202`](https://doi.org/10.1002/andp.19203682202) | [`SKILL.md`](skills/math/m08/SKILL.md) |
| **M.09** (VOL. 05) | [Monge–Kantorovich Optimal Transport, Benamou–Brenier Wasserstein-2 Geodesic Fluid Dynamics, Sinkhorn Entropic Regularization & Flow Matching](https://informatico.ai/math/m09/) ([ES-MX](https://informatico.ai/es-mx/math/m09/)) | [`DOI:10.1007/s002110050002`](https://doi.org/10.1007/s002110050002) | [`SKILL.md`](skills/math/m09/SKILL.md) |
| **M.10** (VOL. 05) | [Persistent Homology, Vietoris–Rips Simplicial Filtrations, Betti Barcodes & Topological Percolation Thresholds in Disordered Media](https://informatico.ai/math/m10/) ([ES-MX](https://informatico.ai/es-mx/math/m10/)) | [`DOI:10.1007/s00454-002-2885-2`](https://doi.org/10.1007/s00454-002-2885-2) | [`SKILL.md`](skills/math/m10/SKILL.md) |
| **M.11** (VOL. 06) | [The 3D Kakeya Preprint of Wang and Zahl and the Guth–Maynard Zero-Density Estimate](https://informatico.ai/math/m11/) ([ES-MX](https://informatico.ai/es-mx/math/m11/)) | [`DOI:10.4007/annals.2015.182.1.9`](https://doi.org/10.4007/annals.2015.182.1.9) | [`SKILL.md`](skills/math/m11/SKILL.md) |
| **M.12** (VOL. 06) | [Public Lean 4 Repositories and NIST FIPS 203 (ML-KEM): What They State, Side by Side](https://informatico.ai/math/m12/) ([ES-MX](https://informatico.ai/es-mx/math/m12/)) | [`DOI:10.1145/1568318.1568324`](https://doi.org/10.1145/1568318.1568324) | [`SKILL.md`](skills/math/m12/SKILL.md) |
| **M.13** (VOL. 07) | [Shannon Zero-Error Graph Capacity, Lovász Theta Sandwich & the Open Seven-Cycle Gap](https://informatico.ai/math/m13/) ([ES-MX](https://informatico.ai/es-mx/math/m13/)) | [`DOI:10.1109/TIT.1979.1055985`](https://doi.org/10.1109/TIT.1979.1055985) | [`SKILL.md`](skills/math/m13/SKILL.md) |
| **M.14** (VOL. 07) | [Sphere Packing in Dimensions 3, 4, 8 & 24: Cohn–Elkies Bounds, Modular Functions & Open Gaps](https://informatico.ai/math/m14/) ([ES-MX](https://informatico.ai/es-mx/math/m14/)) | [`DOI:10.4007/annals.2003.157.689`](https://doi.org/10.4007/annals.2003.157.689) | [`SKILL.md`](skills/math/m14/SKILL.md) |
| **M.15** (VOL. 07) | [Diagonal Ramsey Numbers: Paley Colorings, Erdős Random Floors, the Book Algorithm & Open Gaps](https://informatico.ai/math/m15/) ([ES-MX](https://informatico.ai/es-mx/math/m15/)) | [`DOI:10.1112/plms/s2-30.1.264`](https://doi.org/10.1112/plms/s2-30.1.264) | [`SKILL.md`](skills/math/m15/SKILL.md) |

---

## License & Security

- **Dual License ([`LICENSE`](LICENSE))**: MIT for code, solvers, Python verifiers, and `SKILL.md` companions; Creative Commons Attribution 4.0 International (`CC BY 4.0`) for long-form essays and visual plates.
- **Film posters (exception)**: the two posters in `src/images/films/` are stills from the lab's own films and stay under the films' license, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The Follow the Light poster shows the Human Reference Atlas lung model (HuBMAP, CC BY 4.0), credited on the card.
- **Security & Contributing**: Vulnerability reporting and CSP boundaries live in [`SECURITY.md`](SECURITY.md); single-maintainer pull request rules live in [`CONTRIBUTING.md`](CONTRIBUTING.md).
