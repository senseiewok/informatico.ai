# Time & Gravity (`T`) · agent skills, generators and verifiers

One folder per shipped page under `skills/timegravity/<slug>/`:

| Page | Folder | Generator | Verifier (stdlib, planted defect) | Companion |
| --- | --- | --- | --- | --- |
| `T.01` Gravity as a Slope in the Rate of Time | `t01/` | `make_t01.py` | `verify_t01_time_slope_geodesic.py` (`--planted-defect` must exit non-zero) | `SKILL.md` |

The hub `T.00` has no generator and no verifier: it carries no claims, and `tools/check_timegravity_labels.py` asserts that.

Shared pieces:
- `tools/timegravity_kernel.py` — the RK4 geodesic kernel the generator, the verifier and the static-plate renderer share.
- `timegravity/ledger.json` — the grounding ledger (`id`, `label`, `doi`, `year`, `collaboration`, `kind`, `review_by`).
- `tools/check_timegravity_labels.py` — the ledger-driven label lint; its own planted defect flips one label upward and must fail.
- `timegravity/run_all_timegravity.py` — one-command runner for all of the above.

Every verifier prints one JSON object with `"status": "PASS"` on success and `FAIL` on stderr with a non-zero exit on a defect, the same contract as `skills/toolchain/` and `skills/verify_all_48_folios.py`.
