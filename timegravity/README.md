# Time & Gravity (`T.00`–`T.07`, `T.10`) · a track where the open problem is the subject

**Live:** [https://informatico.ai/timegravity/](https://informatico.ai/timegravity/) · **Español (es-MX):** [https://informatico.ai/es-mx/timegravity/](https://informatico.ai/es-mx/timegravity/)

> **Fixed boundary, printed on every T page and asserted by the lint:** Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up.

A sibling track beside *Tech & Tools · The Toolbox* (`X.01`–`X.06`), outside the Folio count of 48. The hub states a common intuition once, in the third person, as a question, and carries no claims. Each later page ships six things, and the build refuses a page that lacks one:

1. **One instrument**, hand-written SVG, reduced-motion and keyboard paths, a static plate fallback; the knockout is the argument.
2. **A standard-library verifier** that recomputes the page's central number and fails on a planted defect.
3. **A grounding ledger and a ledger-driven label lint** (`timegravity/ledger.json`, `tools/check_timegravity_labels.py`).
4. **A `SKILL.md` companion** (`skills/timegravity/<slug>/SKILL.md`).
5. **A 5-pace distillation ladder and es-MX** in the same commit.
6. **An AI-contribution line** naming any AI system that contributed to a cited result and the human who checked it.

## Shipped pages (batch 1)

| Code | Page | Instrument and knockout | Verifier's central number · planted defect | Labels on the page |
| --- | --- | --- | --- | --- |
| `T.00` | [The hub](https://informatico.ai/timegravity/) | A worldline with a movable "now" marker: a picture of the question, not a result | none; the lint asserts zero claim spans | none |
| `T.01` | [Gravity as a Slope in the Rate of Time](https://informatico.ai/timegravity/t01/) | 1+1 geodesic where only `g_tt` varies with height; the body falls at g with no force term; knockout flattens the gradient and nothing falls | `a = −9.80665 m/s²` within `1e-6` relative · sign flip makes the body rise | MEASURED, SINGLE RESULT, DERIVED, OPEN |

Reading order of the whole track and the open question each page ends with: `tools/folios/timegravity/__init__.py` (`TRACK_MAP`). Batch 2 onward (T.02, T.03, then T.07, T.04, then T.05, T.06, T.10) reuses this scaffold.

## The ledger and the label lint

`timegravity/ledger.json` has one row per cited source with the fields `id`, `label`, `doi`, `year`, `collaboration`, `kind`, `review_by` (schema: `timegravity/ledger.schema.json`). A claim on a page is a span:

```html
<span class="tg-claim" data-tg-label="MEASURED" data-tg-ledger="T01-PR1960,T01-HK1972O">…</span>
```

`tools/check_timegravity_labels.py` enforces: MEASURED needs at least two rows from different collaborations with peer-reviewed DOIs; BOUND is for exclusion limits; DERIVED names a parent MEASURED row (`data-tg-parent`); rows younger than 24 months or preprints cap at SINGLE RESULT or PROPOSED; press URLs cannot back a claim; every DOI resolves in the offline Crossref cache (`data/folio-citations.cache.json`); English and es-MX pages carry identical label sequences; the build fails when a `review_by` date has passed; a banned-phrase backstop in both languages; the hub-only sentence appears on no other page. The lint's own planted defect (`--planted-defect`) flips one label upward and must fail. The lint checks mechanics; a human checklist decides the label.

New DOIs enter the cache with `python timegravity/refresh_crossref_cache.py` (the only network call in the track; run by a maintainer, sends no personal data).

## One-command runner

```bash
python timegravity/run_all_timegravity.py
```

runs `make_t01.py`, `verify_t01_time_slope_geodesic.py` (and `--planted-defect`, which must fail), the label lint (and its `--planted-defect`, which must fail) and `tools/check_folio_citations.py --offline`. Pages are built by `python tools/build_timegravity.py` (also called at the end of `tools/build_longform_folios.py`); plates by `python timegravity/make_plates.py`. Tests: `python -m unittest tests.test_timegravity_track`.
