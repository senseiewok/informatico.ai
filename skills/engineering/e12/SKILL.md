---
name: verified-riscv-cbf-grid-sync
description: AI-agnostic cyber-physical systems skill for Virtual Synchronous Machine (VSM) grid-forming inverters, Control Barrier Function (CBF-QP) forward invariance, and the published Coq (Rocq) and Kami precedents for machine-checked RISC-V processors.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Silicon-to-Grid Safety: Control Barrier Functions, Firefly-Synchronized Renewable Grids & the Case for a Verified Relay Processor (Folio E.12)

A plain-text companion to the essay at https://informatico.ai/engineering/e12/ (`E.12 · RISC-V & Grid Control Barrier Functions`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`sup_u [L_f h(x) + L_g h(x) u] ≥ −α(h(x)) · M dΔω/dt + D Δω = P_m − P_e`

## Rules the essay derives
1. Enforce Nagumo forward invariance of safe set C = {x : h(x) >= 0} via CBF constraint L_f h(x) + L_g h(x) * u >= -alpha * h(x).
2. Bound grid Rate of Change of Frequency |df/dt| <= f_0 * Delta_P / (2 * H_virt * S_base); the folio model targets less than 0.5 Hz/s after the loss of one large unit.
3. Treat processor correctness as a stated assumption. Cite published machine-checked RISC-V work (Kami, DOI 10.1145/3110268; Erbsen et al. 2021, DOI 10.1145/3453483.3454065) and never claim a verified relay processor without a public proof artifact.

## How it works, in four stages
- Stage 1 (Firefly-Style Phase-Locking on the Power Grid, Continuing P.02): Solar and battery grid-forming inverters hold a common rhythm through coupled phase angles θ_i, M d²θ_i/dt² + D dθ_i/dt = P_i − ∑ K_ij sin(θ_i − θ_j), a member of the coupled-oscillator family studied in 'Synchronization in complex oscillator networks and smart grids' (Dörfler, Chertkov & Bullo 2013, DOI 10.1073/pnas.1212134110). The firefly is an analogy, not the same equation.
- Stage 2 (Synthetic Inertia via Virtual Synchronous Machines): In the folio model, when a 1.2 GW loss hits, battery inverters inject power proportional to −H_virt dω/dt, in the manner of synchronverters (Zhong & Weiss 2011, DOI 10.1109/TIE.2010.2048839), and at the default H_virt = 4.8 s the initial Rate of Change of Frequency (RoCoF) is 0.42 Hz/s. It stays below 0.5 Hz/s only for H_virt above about 4.0 s.
- Stage 3 (Control Barrier Function Quadratic Program Filter, Continuing M.07): A real-time QP filter enforces L_f h(x) + L_g h(x)u ≥ −α(h(x)). For the modelled dynamics, and while the QP stays feasible, the state x does not leave the safe set h(x) ≥ 0 (Ames et al. 2017, DOI 10.1109/TAC.2016.2638961).
- Stage 4 (Processor Layer, a Design Assumption): The filter is only as sound as the chip that runs it. Machine-checked RISC-V processors exist at small scale: Kami (Choi et al. 2017, DOI 10.1145/3110268) and the embedded system of Erbsen et al. (2021, DOI 10.1145/3453483.3454065), both in the Coq proof assistant, now named Rocq. This folio knows of no published machine-checked proof for the processor of a grid protection relay; here it is assumed, not shown.

## Reference values stated in the essay
- **Grid Frequency Nadir (f_min)**: `59.82 Hz (model value)`
- **Initial RoCoF Before Filter**: `0.42 Hz/s (< 0.50 model limit)`
- **CBF Barrier Margin h(x)**: `+0.72 Hz above 59.1 Hz trip (model)`
- **CBF Filter State**: `IDLE · constraint slack (model)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1109/TAC.2016.2638961 (Scite report: https://scite.ai/reports/10.1109/TAC.2016.2638961)
- What the essay compares against: Model values: RoCoF 0.42 Hz/s · h(x_grid) = +0.72 Hz · processor proof assumed, not shown

## Recent research context
- **Control Barrier Functions and Virtual Inertia for Low-Inertia Grids, with a Verified Processor as the Missing Layer**: Low-inertia grids are an active research field (Milano et al. 2018, DOI 10.23919/PSCC.2018.8450880). This folio pairs Control Barrier Function QP filters (Ames et al. 2017, DOI 10.1109/TAC.2016.2638961) with a reduced virtual-inertia model, and points to machine-checked RISC-V work in Coq (Choi et al. 2017, DOI 10.1145/3110268; Erbsen et al. 2021, DOI 10.1145/3453483.3454065) as the precedent for a verified protection processor, which this folio assumes and does not show.
