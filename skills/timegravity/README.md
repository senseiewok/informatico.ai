# Time & Gravity (`T`) · agent skills, generators and verifiers

One folder per shipped page under `skills/timegravity/<slug>/`:

| Page | Folder | Generator | Verifier (stdlib, planted defect) | Companion |
| --- | --- | --- | --- | --- |
| `T.01` Gravity as a Slope in the Rate of Time | `t01/` | `make_t01.py` | `verify_t01_time_slope_geodesic.py` (`--planted-defect` must exit non-zero) | `SKILL.md` |
| `T.02` Everyone Moves at One Rate | `t02/` | `make_t02.py` | `verify_t02_gps_one_rate.py` (sign flip must exit non-zero; two calculation paths must agree) | `SKILL.md` |
| `T.03` What Sets the Slope | `t03/` | `make_t03.py` | `verify_t03_poisson_equivalence.py` (η = 10⁻³ must exit non-zero) | `SKILL.md` |
| `T.04` A Clock in Two Places | `t04/` | `make_t04.py` | `verify_t04_clock_visibility.py` (a clock that never decoheres must exit non-zero) | `SKILL.md` |
| `T.05` Does Gravity Entangle, and Would That Settle It? (also `tools/timegravity_refit_smeared.py`: profile-likelihood refit of a short-range torque dataset for the smeared pair potential; `--demo` on synthetic data) | `t05/` | `make_t05.py` | `verify_t05_entanglement_channels.py` (a classical LOCC channel that entangles must exit non-zero) · `verify_t05_dispute_kernel.py` (the Diósi–Penrose model with its decoherence dropped must exit non-zero) · `verify_t05_smeared_isl.py` (the plate-mode closed form with its second term dropped, and the wedge kernel's radial series with a fixed truncation, must exit non-zero) | `SKILL.md` |
| `T.06` Does Gravity Collapse the Wave? | `t06/` | `make_t06.py` | `verify_t06_collapse_bound.py` (the bound drawn on the wrong side must exit non-zero) · the σ ladder (`tools/timegravity_kernel_ladder.py`: tubulin lifetimes per rung, the Casimir floor; the small-displacement series dropped must exit non-zero) | `SKILL.md` |
| `T.07` The Equation with No Time | `t07/` | `make_t07.py` | `verify_t07_page_wootters.py` (a clock spectrum that ignores the constraint must exit non-zero) | `SKILL.md` |
| `T.08` A Horizon Has a Temperature | `t08/` | `make_t08.py` | `verify_t08_horizon_thermodynamics.py` (severing cross-horizon entanglement must exit non-zero) | `SKILL.md` |
| `T.09` A Horizon Rings Like a Bell | `t09/` | `make_t09.py` | `verify_t09_kerr_ringdown.py` (corrupting the Kerr radical `√(1 − χ²) → √(1 + χ²)` must exit non-zero) | `SKILL.md` |
| `T.10` Page's Counting Argument | `t10/` | `make_t10.py` | `verify_t10_page_curve.py` (a non-unitary toy that never turns over must exit non-zero) | `SKILL.md` |
| `T.11` What Selects the World a Clock Sees? | `t11/` | `make_t11.py` | `verify_t11_einselection.py` (scrambling the pointer commutator `[Ĥ_int, Z_S] = 0` must exit non-zero) | `SKILL.md` |
| `T.12` Two Clocks That Only Meet in Gravity | `t12/` | `make_t12.py` | `verify_t12_dark_clock.py` (dropping the factor of 2 in the proper-time step must exit non-zero) | `SKILL.md` |

The hub `T.00` has no generator and no verifier: it carries no claims, and `tools/check_timegravity_labels.py` asserts that.

Shared pieces:
- `tools/timegravity_kernel.py` — the RK4 geodesic kernel the generator, the verifier and the static-plate renderer share.
- `timegravity/ledger.json` — the grounding ledger (`id`, `label`, `doi`, `year`, `collaboration`, `kind`, `review_by`).
- `tools/check_timegravity_labels.py` — the ledger-driven label lint; its own planted defect flips one label upward and must fail.
- `timegravity/run_all_timegravity.py` — one-command runner for all of the above.

Every verifier prints one JSON object with `"status": "PASS"` on success and `FAIL` on stderr with a non-zero exit on a defect, the same contract as `skills/toolchain/` and `skills/verify_all_48_folios.py`.
