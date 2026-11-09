# Time & Gravity (`T`) · agent skills, generators and verifiers

One folder per shipped page under `skills/timegravity/<slug>/`:

| Page | Folder | Generator | Verifier (stdlib, planted defect) | Companion |
| --- | --- | --- | --- | --- |
| `T.01` Gravity as a Slope in the Rate of Time | `t01/` | `make_t01.py` | `verify_t01_time_slope_geodesic.py` (`--planted-defect` must exit non-zero) | `SKILL.md` |
| `T.02` Everyone Moves at One Rate | `t02/` | `make_t02.py` | `verify_t02_gps_one_rate.py` (sign flip must exit non-zero; two calculation paths must agree) | `SKILL.md` |
| `T.03` What Sets the Slope | `t03/` | `make_t03.py` | `verify_t03_poisson_equivalence.py` (η = 10⁻³ must exit non-zero) | `SKILL.md` |
| `T.04` A Clock in Two Places | `t04/` | `make_t04.py` | `verify_t04_clock_visibility.py` (a clock that never decoheres must exit non-zero) | `SKILL.md` |
| `T.05` Does Gravity Entangle, and Would That Settle It? | `t05/` | `make_t05.py` | `verify_t05_entanglement_channels.py` (a classical LOCC channel that entangles must exit non-zero) | `SKILL.md` |
| `T.06` Does Gravity Collapse the Wave? | `t06/` | `make_t06.py` | `verify_t06_collapse_bound.py` (the bound drawn on the wrong side must exit non-zero) | `SKILL.md` |
| `T.07` The Equation with No Time | `t07/` | `make_t07.py` | `verify_t07_page_wootters.py` (a clock spectrum that ignores the constraint must exit non-zero) | `SKILL.md` |
| `T.10` Page's Counting Argument | `t10/` | `make_t10.py` | `verify_t10_page_curve.py` (a non-unitary toy that never turns over must exit non-zero) | `SKILL.md` |

The hub `T.00` has no generator and no verifier: it carries no claims, and `tools/check_timegravity_labels.py` asserts that.

Shared pieces:
- `tools/timegravity_kernel.py` — the RK4 geodesic kernel the generator, the verifier and the static-plate renderer share.
- `timegravity/ledger.json` — the grounding ledger (`id`, `label`, `doi`, `year`, `collaboration`, `kind`, `review_by`).
- `tools/check_timegravity_labels.py` — the ledger-driven label lint; its own planted defect flips one label upward and must fail.
- `timegravity/run_all_timegravity.py` — one-command runner for all of the above.

Every verifier prints one JSON object with `"status": "PASS"` on success and `FAIL` on stderr with a non-zero exit on a defect, the same contract as `skills/toolchain/` and `skills/verify_all_48_folios.py`.
