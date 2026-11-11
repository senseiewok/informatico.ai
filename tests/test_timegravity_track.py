"""Verification suite for the Time & Gravity track (T.00 hub + T.01), beside the Folio count of 48."""
from __future__ import annotations

import json
import math
import re
import subprocess
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "src"
TG = RESEARCH / "timegravity"
TG_ES = RESEARCH / "es-mx" / "timegravity"
SKILLS = ROOT / "skills" / "timegravity"
sys.path.insert(0, str(ROOT / "tools"))

import build_longform_folios as builder  # noqa: E402
from folios.timegravity import BOUNDARY_EN, BOUNDARY_ES, HUB_ONLY_PHRASES, PAGES, TRACK_MAP  # noqa: E402

PY = [sys.executable, "-X", "utf8"]


class _Spans(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.labels: list[str] = []
        self.text: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "tg-claim" in (a.get("class") or "").split():
            self.labels.append(a.get("data-tg-label", ""))

    def handle_data(self, data):
        self.text.append(data)


def labels_of(path: Path) -> list[str]:
    p = _Spans()
    p.feed(path.read_text(encoding="utf-8"))
    return p.labels


def text_of(path: Path) -> str:
    """Rendered text only (no attributes), whitespace-normalised, lower-case."""
    p = _Spans()
    p.feed(path.read_text(encoding="utf-8"))
    return " ".join(" ".join(p.text).split()).lower()


def run(cmd: list[str], timeout: int = 60) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=timeout, cwd=str(ROOT))


class TimeGravityTrackTests(unittest.TestCase):
    def test_folio_count_is_still_48_and_the_track_sits_beside_it(self) -> None:
        count = sum(1 for p in ("math", "physics", "engineering", "architecture") for d in (RESEARCH / p).iterdir() if d.is_dir())
        self.assertEqual(count, 48)
        self.assertFalse((RESEARCH / "physics" / "t01").exists(), "T pages must not live inside a pillar")
        self.assertTrue((TG / "index.html").is_file())
        self.assertTrue((TG / "t01" / "index.html").is_file())
        self.assertTrue((TG_ES / "index.html").is_file())
        self.assertTrue((TG_ES / "t01" / "index.html").is_file())
        self.assertEqual(len(TRACK_MAP), 14)
        self.assertEqual([m["code"] for m in TRACK_MAP], ["T.00", "T.02", "T.01", "T.03", "T.04", "T.05", "T.06", "T.07", "T.08", "T.09", "T.10", "T.11", "T.12", "T.13"])

    def test_scaffold_files_exist(self) -> None:
        for rel in ("timegravity/README.md", "timegravity/run_all_timegravity.py", "timegravity/ledger.json",
                    "timegravity/ledger.schema.json", "timegravity/make_plates.py", "timegravity/refresh_crossref_cache.py",
                    "tools/check_timegravity_labels.py", "tools/build_timegravity.py", "tools/timegravity_kernel.py",
                    "skills/timegravity/README.md", "skills/timegravity/t01/SKILL.md", "skills/timegravity/t01/make_t01.py",
                    "skills/timegravity/t01/verify_t01_time_slope_geodesic.py", "src/modules/timegravity-slope.mjs",
                    "src/timegravity.css", "src/plates/t00.png", "src/plates/t01.png",
                    "src/timegravity/t01/files/t01_reference.json", "src/timegravity/t01/files/manifest.json"):
            self.assertTrue((ROOT / rel).is_file(), f"missing {rel}")

    def test_ledger_schema_fields_and_offline_crossref_resolution(self) -> None:
        ledger = json.loads((ROOT / "timegravity" / "ledger.json").read_text(encoding="utf-8"))
        cache = json.loads((ROOT / "data" / "folio-citations.cache.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(ledger["rows"]), 6)
        for row in ledger["rows"]:
            self.assertEqual(set(row) - {"note", "contrasting_audit"}, {"id", "label", "doi", "year", "collaboration", "kind", "review_by"}, row["id"])
            self.assertTrue(cache.get("doi:" + row["doi"].lower(), {}).get("found"), f"{row['id']} DOI not in offline cache")
            self.assertNotEqual(row["kind"], "press")
        ids = {r["id"] for r in ledger["rows"]}
        for doi in ("10.1103/PhysRevLett.4.337", "10.1126/science.177.4044.166", "10.1126/science.177.4044.168",
                    "10.1103/PhysRevLett.45.2081", "10.1126/science.1192720", "10.1038/s41586-021-04349-7"):
            self.assertIn(doi, {r["doi"] for r in ledger["rows"]})
        both = next(r for r in ledger["rows"] if r["doi"] == "10.1038/s41586-021-04349-7")
        self.assertEqual(both["label"], "SINGLE RESULT")
        self.assertIn("T01-PR1960", ids)

    def test_label_lint_passes_and_its_planted_defect_fails(self) -> None:
        ok = run(PY + [str(ROOT / "tools" / "check_timegravity_labels.py")])
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertIn("PASS: Time & Gravity label lint verified", ok.stdout)
        self.assertIn("planted_defect_knockout=REJECTED_AS_EXPECTED", ok.stdout)
        bad = run(PY + [str(ROOT / "tools" / "check_timegravity_labels.py"), "--planted-defect"])
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn("FAIL", bad.stderr)
        self.assertIn("MEASURED needs >= 2", bad.stderr)
        # A passed review date fails the build.
        stale = run(PY + [str(ROOT / "tools" / "check_timegravity_labels.py"), "--today", "2031-01-01"])
        self.assertNotEqual(stale.returncode, 0)
        self.assertIn("review_by", stale.stderr)

    def test_t01_verifier_passes_and_sign_flip_fails(self) -> None:
        verify = SKILLS / "t01" / "verify_t01_time_slope_geodesic.py"
        gen = run(PY + [str(SKILLS / "t01" / "make_t01.py")])
        self.assertEqual(gen.returncode, 0, gen.stdout + gen.stderr)
        res = run(PY + [str(verify)])
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        payload = json.loads(res.stdout)
        self.assertEqual(payload["status"], "PASS")
        self.assertLess(payload["central_number"]["rel_err"], 1e-6)
        self.assertAlmostEqual(payload["central_number"]["a_eff_m_per_s2"], -9.80665, places=5)
        self.assertEqual(payload["geometry_checks"]["planted_defect_knockout"], "REJECTED_AS_EXPECTED")
        self.assertLess(abs(payload["geometry_checks"]["a_flat_m_per_s2"]), 1e-12)
        bad = run(PY + [str(verify), "--planted-defect"])
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn("FAIL", bad.stderr)
        # The generator is byte-for-byte reproducible (the committed artefact matches regeneration).
        before = (TG / "t01" / "files" / "t01_reference.json").read_bytes()
        run(PY + [str(SKILLS / "t01" / "make_t01.py")])
        self.assertEqual(before, (TG / "t01" / "files" / "t01_reference.json").read_bytes())

    def test_hub_has_zero_claims_states_the_intuition_once_and_t01_never(self) -> None:
        for hub, phrase in ((TG / "index.html", "gravity is a slope in the rate of time"),
                            (TG_ES / "index.html", "la gravedad es una pendiente en el ritmo del tiempo")):
            self.assertEqual(labels_of(hub), [], f"{hub} carries claim spans")
            rendered = text_of(hub)
            self.assertEqual(rendered.count(phrase), 1, f"{hub}: the intuition is stated once, in the page's language")
            raw = hub.read_text(encoding="utf-8").lower()
            self.assertIn("a common intuition is that", raw)
            self.assertIn("tg-track-map", raw)
            self.assertEqual(raw.count("<li data-built="), 14)
            self.assertIn("what would change this page", raw)
        for page in (TG / "t01" / "index.html", TG_ES / "t01" / "index.html"):
            low = page.read_text(encoding="utf-8").lower()
            for phrase in HUB_ONLY_PHRASES:
                self.assertNotIn(phrase, low, f"{page}: hub-only phrase {phrase!r}")

    def test_t01_labels_identical_in_both_languages_and_contract_pieces_present(self) -> None:
        en, es = TG / "t01" / "index.html", TG_ES / "t01" / "index.html"
        en_labels, es_labels = labels_of(en), labels_of(es)
        self.assertEqual(en_labels, es_labels)
        self.assertIn("MEASURED", en_labels)
        self.assertIn("SINGLE RESULT", en_labels)
        self.assertIn("DERIVED", en_labels)
        self.assertIn("OPEN", en_labels)
        for path, boundary in ((en, BOUNDARY_EN), (es, BOUNDARY_ES)):
            txt = path.read_text(encoding="utf-8")
            self.assertIn(boundary, txt, f"{path} lacks the fixed boundary line")
            for cls in ('data-tg-instrument="slope"', 'class="tg-worldline"', "data-tg-knockout", "data-tg-flip",
                        'class="tp-plain-bridge-box"', 'class="tp-analogy-box"', 'class="tp-distill-figure"',
                        'class="tp-distill-svg"', 'class="tp-proof-spine"', 'class="tg-ai-line"', 'class="tg-change-box"',
                        'class="tg-open-question"', 'class="tp-skill-box"', 'class="tp-table tg-ledger-table"',
                        'timegravity-slope.mjs', 'timegravity.css', 'aria-live="polite"'):
                self.assertIn(cls, txt, f"{path} missing {cls}")
            self.assertEqual(txt.count('class="tp-proof-stage-block"'), 4, path)
        self.assertIn("What sets the slope?", en.read_text(encoding="utf-8"))
        self.assertIn('lang="es-MX"', es.read_text(encoding="utf-8"))
        self.assertIn('aria-pressed="true" aria-label="Read in English" title="English">EN</button>', es.read_text(encoding="utf-8"))

    def test_spanish_twin_is_the_english_page_through_the_site_copier(self) -> None:
        for en in (TG / "index.html", TG / "t01" / "index.html"):
            text = en.read_text(encoding="utf-8")
            self.assertEqual(builder.to_spanish_static(text, swap=False, shift=False), text, en)
        es = (TG_ES / "t01" / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="../../../timegravity.css"', es)
        self.assertIn('src="../../../modules/timegravity-slope.mjs"', es)
        self.assertIn('src="../../../plates/t01.png', es)
        self.assertIn('alt="Diagrama para T.01:', es)
        self.assertIn(">Descargar SKILL.md (timegravity-t01-time-slope-geodesic.SKILL.md)</button>", es)
        self.assertIn(">Copiar SKILL.md</button>", es)
        self.assertIn(">Descargar verificador en Python (verify_t01_time_slope_geodesic.py)</button>", es)
        self.assertIn(">Línea de mundo de un cuerpo soltado en reposo", es)
        en_hub = (TG / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-pager-link tp-pager-next" href="../timegravity/t0', en_hub)

    def test_label_lint_rejects_derived_tautology_rank_mismatch_and_handles_void_tags(self) -> None:
        import datetime as dt
        import check_timegravity_labels as lbl

        # Void tags (<br>, <wbr>) inside a claim span must not swallow the claim.
        p = lbl._Claims()
        p.feed('<p><span class="tg-claim" data-tg-label="OPEN" data-tg-ledger="T01-WILL2014">line 1<br>line 2<wbr></span></p>')
        self.assertEqual(len(p.claims), 1)
        self.assertEqual(p.claims[0]["label"], "OPEN")

        rows = {
            "T01-PR1960": {"id": "T01-PR1960", "label": "MEASURED", "doi": "10.1103/PhysRevLett.4.337", "year": 1960,
                           "collaboration": "Harvard", "kind": "peer-reviewed", "review_by": "2028-11-08"},
            "T01-WILL2014": {"id": "T01-WILL2014", "label": "OPEN", "doi": "10.12942/lrr-2014-4", "year": 2014,
                             "collaboration": "Will", "kind": "peer-reviewed", "review_by": "2028-11-08"},
            "T01-PREP2026": {"id": "T01-PREP2026", "label": "PROPOSED", "doi": "10.48550/arXiv.2601.00001", "year": 2026,
                             "collaboration": "Test", "kind": "preprint", "review_by": "2028-11-08"},
        }
        today = dt.date(2026, 11, 8)
        # DERIVED citing only its MEASURED parent (or parent + preprint) must fail.
        errs: list[str] = []
        lbl.check_claim("t01", 0, {"label": "DERIVED", "ids": ["T01-PR1960"], "parent": "T01-PR1960", "text": "x"}, rows, today, errs)
        self.assertTrue(any("DERIVED needs a mature peer-reviewed derivation row" in e for e in errs), errs)
        errs2: list[str] = []
        lbl.check_claim("t01", 0, {"label": "DERIVED", "ids": ["T01-PR1960", "T01-PREP2026"], "parent": "T01-PR1960", "text": "x"}, rows, today, errs2)
        self.assertTrue(any("DERIVED needs a mature peer-reviewed derivation row" in e for e in errs2), errs2)
        # SINGLE RESULT backed only by an OPEN peer-reviewed row must fail.
        errs3: list[str] = []
        lbl.check_claim("t01", 0, {"label": "SINGLE RESULT", "ids": ["T01-WILL2014"], "parent": None, "text": "x"}, rows, today, errs3)
        self.assertTrue(any("ledger label is >= SINGLE RESULT" in e for e in errs3), errs3)

    def test_plates_are_byte_for_byte_reproducible_and_doi_guard_rejects_traversal(self) -> None:
        t00_before = (RESEARCH / "plates" / "t00.png").read_bytes()
        t01_before = (RESEARCH / "plates" / "t01.png").read_bytes()
        res = run(PY + [str(ROOT / "timegravity" / "make_plates.py")])
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertEqual(t00_before, (RESEARCH / "plates" / "t00.png").read_bytes())
        self.assertEqual(t01_before, (RESEARCH / "plates" / "t01.png").read_bytes())
        sys.path.insert(0, str(ROOT / "timegravity"))
        import refresh_crossref_cache as rc
        with self.assertRaises(ValueError):
            rc.fetch("10.1103/../../etc/passwd")

    def test_module_is_hand_written_zero_network_and_reduced_motion_aware(self) -> None:
        mjs = (RESEARCH / "modules" / "timegravity-slope.mjs").read_text(encoding="utf-8")
        code_only = re.sub(r"//.*?$|/\*.*?\*/", "", mjs, flags=re.M | re.S)
        self.assertIsNone(re.search(r"\b(fetch|XMLHttpRequest|WebSocket|EventSource|sendBeacon|import\s*\()\b", code_only))
        self.assertNotIn("http", code_only)
        self.assertIn("prefers-reduced-motion", mjs)
        self.assertIn("299792458", mjs)
        self.assertIn("9.80665", mjs)
        css = (RESEARCH / "timegravity.css").read_text(encoding="utf-8")
        self.assertIn("prefers-reduced-motion", css)
        self.assertIn("focus-visible", css)
        self.assertIn('html[lang="es-MX"] .tg-claim::after', css)

    def test_index_sitemap_and_llms_carry_the_track(self) -> None:
        hub = (RESEARCH / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-track-chip tp-track-chip-timegravity" href="timegravity/"', hub)
        self.assertIn('id="featured-timegravity"', hub)
        self.assertLess(hub.index('id="featured-timegravity"'), hub.index('id="pillar-engineering"'))
        rail_start = hub.index('class="tp-featured-steps-rail"')
        rail = hub[rail_start:hub.index("</ol>", rail_start)]
        self.assertLess(rail.index('href="./timegravity/t02/"'), rail.index('href="./timegravity/t01/"'))
        es_hub = (RESEARCH / "es-mx" / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="timegravity/"', es_hub)
        self.assertIn('id="featured-timegravity"', es_hub)
        self.assertLess(es_hub.index('id="featured-timegravity"'), es_hub.index('id="pillar-engineering"'))
        phys = (RESEARCH / "physics" / "index.html").read_text(encoding="utf-8")
        es_phys = (RESEARCH / "es-mx" / "physics" / "index.html").read_text(encoding="utf-8")
        self.assertLess(phys.index('id="timegravity-series"'), phys.index("Standalone Physics Monographs"))
        self.assertLess(es_phys.index('id="timegravity-series"'), es_phys.index("Monografías Independientes de Física"))
        self.assertIn("T06-GERACI2008", (TG / "t06" / "index.html").read_text(encoding="utf-8"))
        xml = (RESEARCH / "sitemap.xml").read_text(encoding="utf-8")
        for url in ("https://informatico.ai/timegravity/", "https://informatico.ai/timegravity/t01/",
                    "https://informatico.ai/es-mx/timegravity/", "https://informatico.ai/es-mx/timegravity/t01/"):
            self.assertIn(f"<loc>{url}</loc>", xml)
        llms = (RESEARCH / "llms.txt").read_text(encoding="utf-8")
        self.assertIn("(https://informatico.ai/timegravity/)", llms)
        self.assertIn("(https://informatico.ai/timegravity/t01/)", llms)
        self.assertIn("(https://informatico.ai/timegravity/t13/)", llms)
        self.assertIn("84 SKILL.md companions", llms)
        self.assertLess(llms.index("timegravity/t02/"), llms.index("timegravity/t01/"))
        self.assertIn("## Time & Gravity", llms)

    def test_one_command_runner_passes(self) -> None:
        res = run(PY + [str(ROOT / "timegravity" / "run_all_timegravity.py")], timeout=300)  # 18 verifiers with planted defects; the two T.05 kernels take 12-15 s each
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("PASS: Time & Gravity:", res.stdout)
        self.assertEqual(res.stdout.count("REJECTED_AS_EXPECTED:"), 19)  # 18 verifiers (13 pages, T.05 with five, T.06 with two) + the label lint = 19

    def test_pages_rebuild_byte_for_byte_from_source(self) -> None:
        import build_timegravity as tg
        catalog = builder.update_catalogs()
        for page in PAGES:
            slug = page["slug"]
            rel = Path("timegravity") / slug if slug else Path("timegravity")
            en = (RESEARCH / rel / "index.html").read_text(encoding="utf-8")
            es = (RESEARCH / "es-mx" / rel / "index.html").read_text(encoding="utf-8")
            self.assertEqual(tg.render_page(page, catalog, "en"), en, f"{rel}: English page is stale; run tools/build_timegravity.py")
            self.assertEqual(builder.to_spanish_static(tg.render_page(page, catalog, "es")), es, f"{rel}: Spanish page is stale")


class TimeGravityBatch2Tests(unittest.TestCase):
    """T.02 and T.03, the Scite column, the lint mutation suite and the cross-field additions."""

    def test_t02_and_t03_pages_verifiers_and_planted_defects(self) -> None:
        for slug, vname, must_have in (
            ("t02", "verify_t02_gps_one_rate.py", ("double_entry_schwarzschild", "position_error_per_day_m")),
            ("t03", "verify_t03_poisson_equivalence.py", ("equivalence_principle_eta_0", "poisson_recovers_GM_over_r")),
        ):
            for path in (TG / slug / "index.html", TG_ES / slug / "index.html"):
                self.assertTrue(path.is_file(), f"missing {path}")
            gen = run(PY + [str(SKILLS / slug / f"make_{slug}.py")])
            self.assertEqual(gen.returncode, 0, gen.stdout + gen.stderr)
            res = run(PY + [str(SKILLS / slug / vname)])
            self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
            payload = json.loads(res.stdout)
            self.assertEqual(payload["status"], "PASS")
            self.assertEqual(payload["geometry_checks"]["planted_defect_knockout"], "REJECTED_AS_EXPECTED")
            for key in must_have:
                self.assertTrue(key in payload["geometry_checks"] or key in payload["central_number"], key)
            bad = run(PY + [str(SKILLS / slug / vname), "--planted-defect"])
            self.assertNotEqual(bad.returncode, 0)
            self.assertIn("FAIL", bad.stderr)
        t02 = json.loads(run(PY + [str(SKILLS / "t02" / "verify_t02_gps_one_rate.py")]).stdout)
        cn = t02["central_number"]
        self.assertAlmostEqual(cn["grav_us_per_day"], 45.7, delta=0.6)
        self.assertAlmostEqual(cn["vel_us_per_day"], -7.2, delta=0.2)
        self.assertAlmostEqual(cn["net_us_per_day"], 38.5, delta=0.7)
        self.assertLess(abs(cn["double_entry_diff_us"]), 0.3)
        self.assertAlmostEqual(cn["position_error_per_day_m"] / 1000, 11.5, delta=0.3)
        t03 = json.loads(run(PY + [str(SKILLS / "t03" / "verify_t03_poisson_equivalence.py")]).stdout)
        self.assertLess(t03["central_number"]["poisson_worst_rel_err_exterior"], 1e-4)
        self.assertLess(t03["central_number"]["two_body_separation_m"], 1e-12)
        self.assertAlmostEqual(t03["geometry_checks"]["planted_separation_m"], 4.9e-3, delta=1e-4)

    def test_t02_t03_labels_boundary_and_instruments(self) -> None:
        expect = {"t02": ("MEASURED", "DERIVED", "BOUND", "OPEN"), "t03": ("MEASURED", "SINGLE RESULT", "DERIVED", "OPEN")}
        for slug, labels in expect.items():
            en, es = TG / slug / "index.html", TG_ES / slug / "index.html"
            self.assertEqual(labels_of(en), labels_of(es), slug)
            for lab in labels:
                self.assertIn(lab, labels_of(en), f"{slug} lacks {lab}")
            for path, boundary in ((en, BOUNDARY_EN), (es, BOUNDARY_ES)):
                txt = path.read_text(encoding="utf-8")
                self.assertIn(boundary, txt)
                self.assertIn(f'data-tg-instrument="{"gps" if slug == "t02" else "poisson"}"', txt)
                self.assertIn("data-tg-predict", txt, f"{path} lacks predict-before-reveal")
                self.assertIn('class="tg-ai-line"', txt)
                self.assertIn("Scite", txt)
                for phrase in HUB_ONLY_PHRASES:
                    self.assertNotIn(phrase, txt.lower())
            self.assertEqual(builder.to_spanish_static(en.read_text(encoding="utf-8"), swap=False, shift=False), en.read_text(encoding="utf-8"))
        self.assertIn('id="budget"', (TG / "t02" / "index.html").read_text(encoding="utf-8"))
        self.assertNotIn("BOUND", labels_of(TG / "t03" / "index.html"))
        # Reading order: T.00 -> T.02 -> T.01 -> T.03 ; every built neighbour is a real link.
        hub = (TG / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-pager-link tp-pager-next" href="../timegravity/t02/"', hub)
        t02 = (TG / "t02" / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t01/"', t02)
        t01 = (TG / "t01" / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t03/"', t01)
        self.assertIn('class="tp-pager-link tp-pager-prev" href="../../timegravity/t02/"', t01)
        self.assertEqual(hub.count('data-built="true"'), 14)

    def test_lint_mutation_suite_kills_every_mutant_and_scite_tallies_are_cached(self) -> None:
        res = run(PY + [str(ROOT / "tools" / "check_timegravity_labels.py"), "--mutants"])
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("MUTANTS: 15/15 killed", res.stdout)
        self.assertNotIn("SURVIVED", res.stderr)
        ok = run(PY + [str(ROOT / "tools" / "check_timegravity_labels.py")])
        self.assertIn("mutants killed 15/15", ok.stdout)
        cache = json.loads((ROOT / "data" / "folio-citations.cache.json").read_text(encoding="utf-8"))
        ledger = json.loads((ROOT / "timegravity" / "ledger.json").read_text(encoding="utf-8"))
        for row in ledger["rows"]:
            sc = cache.get("scite:" + row["doi"].lower())
            self.assertTrue(sc and sc.get("found"), f"{row['id']} has no Scite tally in the cache")
            for key in ("supporting", "contrasting", "mentioning", "citing_publications", "fetched"):
                self.assertIn(key, sc)
        self.assertTrue((ROOT / "timegravity" / "LABEL-CHECKLIST.md").is_file())

    def test_module_covers_the_four_instruments_and_stays_offline(self) -> None:
        mjs = (RESEARCH / "modules" / "timegravity-slope.mjs").read_text(encoding="utf-8")
        for sel in ('data-tg-instrument="slope"', 'data-tg-instrument="worldline"', 'data-tg-instrument="gps"', 'data-tg-instrument="poisson"', "data-tg-predict"):
            self.assertIn(sel, mjs)
        code_only = re.sub(r"//.*?$|/\*.*?\*/", "", mjs, flags=re.M | re.S)
        self.assertIsNone(re.search(r"\b(fetch|XMLHttpRequest|WebSocket|EventSource|sendBeacon|import\s*\()\b", code_only))
        self.assertIn("poissonRadial", mjs)
        self.assertIn("gpsSchwarzschildNet", mjs)


class TimeGravityBatch3Tests(unittest.TestCase):
    """T.07 and T.04, and the site-wide navigation entry for the track."""

    def test_t07_and_t04_pages_verifiers_and_planted_defects(self) -> None:
        for slug, vname in (("t07", "verify_t07_page_wootters.py"), ("t04", "verify_t04_clock_visibility.py")):
            for path in (TG / slug / "index.html", TG_ES / slug / "index.html"):
                self.assertTrue(path.is_file(), f"missing {path}")
            gen = run(PY + [str(SKILLS / slug / f"make_{slug}.py")])
            self.assertEqual(gen.returncode, 0, gen.stdout + gen.stderr)
            res = run(PY + [str(SKILLS / slug / vname)])
            self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
            payload = json.loads(res.stdout)
            self.assertEqual(payload["status"], "PASS")
            self.assertEqual(payload["geometry_checks"]["planted_defect_knockout"], "REJECTED_AS_EXPECTED")
            bad = run(PY + [str(SKILLS / slug / vname), "--planted-defect"])
            self.assertNotEqual(bad.returncode, 0)
            self.assertIn("FAIL", bad.stderr)
        t07 = json.loads(run(PY + [str(SKILLS / "t07" / "verify_t07_page_wootters.py")]).stdout)
        self.assertLess(t07["central_number"]["constraint_residual"], 1e-10)
        self.assertLess(t07["central_number"]["max_dev_from_schroedinger"], 1e-10)
        self.assertGreaterEqual(t07["central_number"]["kernel_dim"], 1)
        self.assertAlmostEqual(t07["central_number"]["projection_onto_kernel"], 1.0, places=6)
        self.assertGreater(t07["geometry_checks"]["planted_residual"], 1.0)
        t04 = json.loads(run(PY + [str(SKILLS / "t04" / "verify_t04_clock_visibility.py")]).stdout)
        self.assertAlmostEqual(t04["central_number"]["first_zero_dh_T_m_s"], 10.7, delta=0.1)
        self.assertAlmostEqual(t04["central_number"]["v_1m_1s_sr_clock"], 0.989, delta=0.002)
        self.assertLess(t04["central_number"]["max_dev_closed_vs_overlap"], 1e-12)

    def test_t07_t04_labels_boundary_instruments_and_reading_order(self) -> None:
        expect = {"t07": ("MEASURED", "DERIVED", "SINGLE RESULT", "PROPOSED", "OPEN"), "t04": ("DERIVED", "SINGLE RESULT", "PROPOSED", "OPEN")}
        for slug, labels in expect.items():
            en, es = TG / slug / "index.html", TG_ES / slug / "index.html"
            self.assertEqual(labels_of(en), labels_of(es), slug)
            self.assertEqual(set(labels_of(en)), set(labels), f"{slug}: {labels_of(en)}")
            for path, boundary in ((en, BOUNDARY_EN), (es, BOUNDARY_ES)):
                txt = path.read_text(encoding="utf-8")
                self.assertIn(boundary, txt)
                self.assertIn(f'data-tg-instrument="{"pw" if slug == "t07" else "zych"}"', txt)
                self.assertIn("data-tg-predict", txt)
                self.assertIn('class="tg-ai-line"', txt)
                for phrase in HUB_ONLY_PHRASES:
                    self.assertNotIn(phrase, txt.lower())
            self.assertEqual(builder.to_spanish_static(en.read_text(encoding="utf-8"), swap=False, shift=False), en.read_text(encoding="utf-8"))
        self.assertNotIn("MEASURED", labels_of(TG / "t04" / "index.html"), "T.04 is an experiment description; nothing on it is MEASURED")
        t04 = (TG / "t04" / "index.html").read_text(encoding="utf-8")
        self.assertIn("magnetic field gradient, not by gravity", t04)
        self.assertIn("Which time does the clock read?", t04)
        self.assertIn("Whose clock?", (TG / "t07" / "index.html").read_text(encoding="utf-8"))
        # Reading order: T.03 -> T.04 -> T.05 -> T.06 -> T.07 -> T.08 -> T.09 -> T.10
        t03 = (TG / "t03" / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t04/"', t03)
        self.assertIn('class="tp-pager-link tp-pager-prev" href="../../timegravity/t03/"', t04)
        t07 = (TG / "t07" / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="../../timegravity/t04/"', t07)  # step rail link to T.04
        self.assertEqual((TG / "index.html").read_text(encoding="utf-8").count('data-built="true"'), 14)

    def test_series_lives_under_physics_not_in_the_masthead(self) -> None:
        """2026-11-09 council: Time & Gravity is a series inside Physics. No masthead item of its own; the Contents
        dialog lists it inside the Physics column on every page; /physics/ shows an eleven-card series rack; T pages
        mark Physics as the current masthead item and carry Physics in the breadcrumb."""
        pages = list(RESEARCH.rglob("index.html"))
        self.assertGreater(len(pages), 130)
        for page in pages:
            txt = page.read_text(encoding="utf-8")
            self.assertNotIn('data-tp-nav="timegravity"', txt, f"{page} still has a Time & Gravity masthead item")
            self.assertIn('aria-label="Time and Gravity track pages"', txt, f"{page} lacks the Contents-dialog series block")
            self.assertIn("T.07", txt, f"{page} Contents dialog lacks T.07")
            after_physics = txt.split('data-pillar="physics"', 1)[1]
            next_col = after_physics.find('class="tp-contents-col"')
            series_at = after_physics.find('class="tp-contents-series"')
            self.assertGreater(series_at, -1, f"{page}: no series block after the Physics column header")
            self.assertTrue(next_col == -1 or series_at < next_col, f"{page}: the series block is not inside the Physics column")
        for phys in (RESEARCH / "physics" / "index.html", RESEARCH / "es-mx" / "physics" / "index.html"):
            txt = phys.read_text(encoding="utf-8")
            self.assertEqual(txt.count('class="tp-rack-card tp-rack-card-series"'), 14, f"{phys}: fourteen series cards")
            self.assertIn('id="timegravity-series"', txt)
            self.assertIn("1 series of 14 steps", txt)
            self.assertLess(txt.index('id="timegravity-series"'), txt.index("tp-symbolic-physics-lab"),
                            "series rack sits above the interactive sections")
        for tpage in (TG / "index.html", TG / "t07" / "index.html", TG / "t13" / "index.html"):
            txt = tpage.read_text(encoding="utf-8")
            self.assertRegex(txt, r'data-tp-nav="physics" href="[^"]*physics/" aria-current="page"')
            self.assertIn('data-en="Physics" data-es="Física">Physics</a></li>', txt, "Physics breadcrumb")
        nf = (RESEARCH / "404.html").read_text(encoding="utf-8")
        self.assertIn("/timegravity/", nf)

    def test_way_in_and_way_through(self) -> None:
        """The hub hero links forward; every page shows its step; the closing card is the Continue link; the boundary
        sentence is on every page but boxed in full only on the hub; the stale 'not yet built' bullet is gone."""
        hub = (TG / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-cta tp-cta-primary tg-cta-begin" href="../timegravity/t02/"', hub)
        self.assertIn('class="tp-cta tg-cta-map" href="#map"', hub)
        self.assertIn('<div class="tg-boundary-banner" role="note"', hub)
        self.assertNotIn("tg-boundary-compact", hub)
        self.assertNotIn("not yet built", hub)
        self.assertIn("Step 1 of 14", hub)
        self.assertLess(hub.index('id="map"'), hub.index('id="contract"'), "the map comes before the reading contract")
        self.assertEqual(hub.count('class="tg-step tg-step-current" aria-current="step"'), 1)
        for code, slug, step, nxt in (("T.02", "t02", 2, "t01"), ("T.01", "t01", 3, "t03"), ("T.07", "t07", 8, "t08"), ("T.08", "t08", 9, "t09"), ("T.09", "t09", 10, "t10"), ("T.10", "t10", 11, "t11"), ("T.11", "t11", 12, "t12"), ("T.12", "t12", 13, "t13")):
            txt = (TG / slug / "index.html").read_text(encoding="utf-8")
            self.assertIn(f"Step {step} of 14", txt, code)
            self.assertNotIn("Reading order", txt, code)
            self.assertIn('<details class="tg-boundary-banner tg-boundary-compact">', txt, code)
            self.assertIn(BOUNDARY_EN, txt, code)
            self.assertIn(f'<a class="tg-next" href="../../timegravity/{nxt}/" rel="next">', txt, code)
            self.assertEqual(txt.count('aria-current="step"'), 1, code)
            self.assertEqual(txt.count('class="tg-step"'), 13, code)
        last = (TG / "t13" / "index.html").read_text(encoding="utf-8")
        self.assertIn('<a class="tg-next" href="../../timegravity/">', last)
        es = (RESEARCH / "es-mx" / "timegravity" / "t01" / "index.html").read_text(encoding="utf-8")
        self.assertIn("Paso 3 de 14", es)
        self.assertIn(BOUNDARY_ES, es)

class TimeGravityBatch4Tests(unittest.TestCase):
    """T.06 (collapse bound) and T.10 (Page's counting argument)."""

    def test_t06_and_t10_pages_verifiers_and_planted_defects(self) -> None:
        for slug, vname in (("t06", "verify_t06_collapse_bound.py"), ("t10", "verify_t10_page_curve.py")):
            for path in (TG / slug / "index.html", TG_ES / slug / "index.html"):
                self.assertTrue(path.is_file(), f"missing {path}")
            gen = run(PY + [str(SKILLS / slug / f"make_{slug}.py")])
            self.assertEqual(gen.returncode, 0, gen.stdout + gen.stderr)
            res = run(PY + [str(SKILLS / slug / vname)])
            self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
            payload = json.loads(res.stdout)
            self.assertEqual(payload["status"], "PASS")
            self.assertEqual(payload["geometry_checks"]["planted_defect_knockout"], "REJECTED_AS_EXPECTED")
            bad = run(PY + [str(SKILLS / slug / vname), "--planted-defect"])
            self.assertNotEqual(bad.returncode, 0)
            self.assertIn("FAIL", bad.stderr)
        t06 = json.loads(run(PY + [str(SKILLS / "t06" / "verify_t06_collapse_bound.py")]).stdout)["central_number"]
        self.assertAlmostEqual(t06["r0_bound_recomputed_m"] / 0.54e-10, 1.0, delta=0.2)
        self.assertGreater(t06["counts_at_paramfree_r0"], 1e5)
        self.assertLess(t06["max_rel_err_E_G"], 1e-3)
        self.assertAlmostEqual(t06["ladder_tubulins_for_25ms_at_natural_cutoff"] / 2.59e10, 1.0, delta=0.05)
        self.assertGreater(t06["ladder_tubulin_lifetime_at_recast_rung_s"], 1e37)
        self.assertAlmostEqual(t06["ladder_casimir_floor_1e-15_m"] * 1e6, 17.1, delta=0.3)
        self.assertFalse(t06["ladder_window_23um_split_open"])
        self.assertTrue(t06["ladder_window_10um_split_open"])
        self.assertAlmostEqual(t06["ladder_sigma_cubed_ratio"], (250 / 33.1) ** 3, delta=5.0)
        self.assertAlmostEqual(math.log10(t06["diffusion_ceiling_oppenheim_inputs"]), -10.7, delta=0.5)
        for k, v in t06["diffusion_orders_below_printed"].items():
            self.assertTrue(12.0 < v < 18.0, (k, v))
        t10 = json.loads(run(PY + [str(SKILLS / "t10" / "verify_t10_page_curve.py")]).stdout)["central_number"]
        self.assertLess(t10["max_dev_from_page_nats"], 0.03)
        self.assertAlmostEqual(t10["peak_nats"], 2.97, delta=0.05)
        self.assertAlmostEqual(t10["final_nats"], 0.69, delta=0.03)

    def test_t06_t10_labels_boundary_instruments_and_quoted_figures(self) -> None:
        expect = {"t06": {"PROPOSED", "DERIVED", "BOUND", "SINGLE RESULT", "OPEN"}, "t10": {"MEASURED", "SINGLE RESULT", "DERIVED", "PROPOSED", "OPEN"}}
        for slug, labels in expect.items():
            en, es = TG / slug / "index.html", TG_ES / slug / "index.html"
            self.assertEqual(labels_of(en), labels_of(es), slug)
            self.assertEqual(set(labels_of(en)), labels, f"{slug}: {labels_of(en)}")
            for path, boundary in ((en, BOUNDARY_EN), (es, BOUNDARY_ES)):
                txt = path.read_text(encoding="utf-8")
                self.assertIn(boundary, txt)
                self.assertIn(f'data-tg-instrument="{"dp" if slug == "t06" else "page"}"', txt)
                self.assertIn("data-tg-predict", txt)
                self.assertIn('class="tg-ai-line"', txt)
                for phrase in HUB_ONLY_PHRASES:
                    self.assertNotIn(phrase, txt.lower())
            self.assertEqual(builder.to_spanish_static(en.read_text(encoding="utf-8"), swap=False, shift=False), en.read_text(encoding="utf-8"))
        t06 = (TG / "t06" / "index.html").read_text(encoding="utf-8")
        self.assertNotIn("MEASURED", labels_of(TG / "t06" / "index.html"), "a bound page measures nothing")
        for s in ("576", "506", "0.54 × 10⁻¹⁰ m", "0.05 × 10⁻¹⁰ m", "4.9 × 10⁻¹⁰ m", "CSL is not a gravity model", "Where the smearing may live", 'data-tg-figure="sigma-ladder"',
                  "above 40 fm", "6.5 × 10⁸ s", "10¹⁹ ages of the universe", "a micro-cantilever about 25 µm from its source mass", "460,000 against 730,000", "Neither table reaches the room below the rung", "loses reach quickly", "some five thousand times too weak", "upper bounds can be put by observing no deviations", "not the preprint's", "the model is quiet", "a hundred thousand times or more", "a rung of another kind", "a window of another kind", "(PROPOSED, model-specific)", "not a bound on σ", "the deficit in the mean pull grows instead", "thirteen to sixteen orders lower", "not a bound: the step from a torque residual", "twenty-nine orders of magnitude", "does not assess Orch-OR", "D₂ ≤ 10⁻⁴¹", "draws no conclusion beyond it"):
            self.assertIn(s, t06, f"T.06 lacks {s!r}")
        t10 = (TG / "t10" / "index.html").read_text(encoding="utf-8")
        for s in ("signal-to-noise ratio of 80", "to high credibility", "does not recompute it", "Where does the information go, in our universe?"):
            self.assertIn(s, t10, f"T.10 lacks {s!r}")
        self.assertNotIn("solves the information paradox", t10.lower())
        self.assertEqual((TG / "index.html").read_text(encoding="utf-8").count('data-built="true"'), 14)
        # Reading order T.04 -> T.05 -> T.06 -> T.07 -> T.08 -> T.09 -> T.10 -> T.11 -> T.12
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t07/"', t06)
        self.assertIn('class="tp-pager-link tp-pager-prev" href="../../timegravity/t09/"', t10)
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t11/"', t10)


class TimeGravityBatch5Tests(unittest.TestCase):
    """T.05 (gravity-mediated entanglement, three channels at equal weight), the last page of the track."""

    def test_t05_page_verifier_and_planted_defect(self) -> None:
        for path in (TG / "t05" / "index.html", TG_ES / "t05" / "index.html"):
            self.assertTrue(path.is_file(), f"missing {path}")
        gen = run(PY + [str(SKILLS / "t05" / "make_t05.py")])
        self.assertEqual(gen.returncode, 0, gen.stdout + gen.stderr)
        res = run(PY + [str(SKILLS / "t05" / "verify_t05_entanglement_channels.py")])
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        payload = json.loads(res.stdout)
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(payload["geometry_checks"]["planted_defect_knockout"], "REJECTED_AS_EXPECTED")
        cn = payload["central_number"]
        self.assertAlmostEqual(cn["entanglement_phase_rad"], 0.314, delta=0.002)
        self.assertAlmostEqual(cn["concurrence"], 0.156, delta=0.001)
        self.assertAlmostEqual(cn["negativity"], 0.5 * cn["concurrence"], delta=1e-9)
        self.assertAlmostEqual(cn["time_to_full_entanglement_s"], 25.0, delta=0.1)
        self.assertLess(cn["worst_locc_entanglement"], 1e-12)
        self.assertEqual(cn["disputed_interval"][0], 0.0)
        bad = run(PY + [str(SKILLS / "t05" / "verify_t05_entanglement_channels.py"), "--planted-defect"])
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn("FAIL", bad.stderr)
        self.assertIn("LOCC channel entangles", bad.stderr)

    def test_t05_labels_three_channels_equal_weight_and_reading_order(self) -> None:
        en, es = TG / "t05" / "index.html", TG_ES / "t05" / "index.html"
        self.assertEqual(labels_of(en), labels_of(es))
        self.assertEqual(set(labels_of(en)), {"PROPOSED", "DERIVED", "OPEN", "MEASURED", "SINGLE RESULT"}, labels_of(en))
        self.assertEqual(labels_of(en).count("MEASURED"), 3, "milligram gravity, the inverse-square-law tests, and gas damping and heating of levitated silica")
        self.assertNotIn("BOUND", labels_of(en), "nothing on this page is an exclusion limit")
        for path, boundary in ((en, BOUNDARY_EN), (es, BOUNDARY_ES)):
            txt = path.read_text(encoding="utf-8")
            self.assertIn(boundary, txt)
            self.assertIn('data-tg-instrument="bmv"', txt)
            self.assertIn("data-tg-predict", txt)
            self.assertIn('class="tg-ai-line"', txt)
            for phrase in HUB_ONLY_PHRASES:
                self.assertNotIn(phrase, txt.lower())
            # Three channel buttons, equal weight: same class, one per channel, quantum pressed by default only.
            self.assertEqual(txt.count('data-tg-channel="'), 3)
            for ch in ("quantum", "locc", "disputed"):
                self.assertIn(f'class="tp-step-btn tp-knockout-btn" data-tg-channel="{ch}"', txt)
            # The three drawings share one stroke weight.
            self.assertEqual(txt.count('stroke-width="2.5"'), txt.count('stroke-width="2.5"'))
            self.assertIn('class="tg-bmv-q"', txt)
            self.assertIn('class="tg-bmv-l"', txt)
            self.assertIn('class="tg-bmv-band"', txt)
        self.assertEqual(builder.to_spanish_static(en.read_text(encoding="utf-8"), swap=False, shift=False), en.read_text(encoding="utf-8"))
        t05 = en.read_text(encoding="utf-8")
        for s in ("10⁻¹⁵ Pa", "0.15 K", "0.31 rad", "25.0 s", "GIE detection is not enough to validate quantum gravity",
                  "does not pick a side", "If a classical slope can entangle, what would count as quantum gravity?"):
            self.assertIn(s, t05, f"T.05 lacks {s!r}")
        low = t05.lower()
        for banned in ("proves that gravity", "proof that gravity is quantum", "gravity is therefore quantum", "unifies"):
            self.assertNotIn(banned, low)
        self.assertIn("does not say gravity is quantum, or that it is not", low)
        # Reading order: T.04 -> T.05 -> T.06, and the hub now lists eleven built pages.
        self.assertIn('class="tp-pager-link tp-pager-prev" href="../../timegravity/t04/"', t05)
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t06/"', t05)
        t04 = (TG / "t04" / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t05/"', t04)
        self.assertNotIn("in preparation", t04)
        self.assertEqual((TG / "index.html").read_text(encoding="utf-8").count('data-built="true"'), 14)


class TimeGravityDisputeKernelTests(unittest.TestCase):
    """The T.05 band's computed edges: Diósi–Penrose (Trillo–Navascués) upper edge and Kafri–Taylor–Milburn lower edge."""

    def test_dispute_verifier_numbers_and_planted_defect(self) -> None:
        res = run(PY + [str(SKILLS / "t05" / "verify_t05_dispute_kernel.py")])
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        payload = json.loads(res.stdout)
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(payload["geometry_checks"]["planted_defect_knockout"], "REJECTED_AS_EXPECTED")
        cn = payload["central_number"]
        self.assertAlmostEqual(cn["tn_dc_over_sigma"], 0.850872, delta=0.001)
        self.assertIsNone(cn["tn_fig3_last_entangled_time_s"]["50um"])
        self.assertGreater(cn["tn_fig3_last_entangled_time_s"]["250um"], 86400.0)
        self.assertAlmostEqual(cn["tn_fig3_potential_over_newton"]["75um"], 0.179, delta=0.002)
        self.assertAlmostEqual(cn["tn_2017_sigma_c_m"] * 1e6, 525.0, delta=2.0)
        self.assertLess(cn["tn_2017_negativity_at_2p5_s_twice_sigma_c"], 1e-3)
        self.assertAlmostEqual(cn["ktm_threshold_ratio_small_split"], 1.0, delta=0.01)
        self.assertEqual(cn["ktm_2017_linear_model_negativity"], 0.0)
        parts = cn["entangling_parts"]
        self.assertLess(max(v["noise"] for v in parts.values()), 1e-12)
        self.assertAlmostEqual(parts["fig3_sigma_75um_1e4s"]["full"], 0.02375, delta=0.0005)
        self.assertAlmostEqual(parts["fig3_sigma_75um_1e4s"]["interaction"], 0.1521, delta=0.001)
        self.assertLess(parts["fig3_sigma_50um_1e4s"]["full"], 1e-12)
        self.assertAlmostEqual(parts["fig3_sigma_50um_1e4s"]["interaction"], 0.3630, delta=0.001)
        self.assertAlmostEqual(parts["geometry_2017_sigma_1nm_2p5s"]["interaction"], cn["quantum_channel_negativity_2017"], delta=1e-6)
        pc = cn["pure_collapse"]
        self.assertAlmostEqual(pc["geometry_2017_2p5s"]["critical_sigma_m"] * 1e6, 130.0, delta=2.0)
        self.assertAlmostEqual(pc["geometry_2017_2p5s"]["half_sigma_m"] * 1e6, 177.0, delta=2.0)
        self.assertAlmostEqual(pc["letter_geometry_2p5s"]["critical_sigma_m"] * 1e6, 14.3, delta=0.5)
        sc = cn["collapse_scaling"]
        self.assertAlmostEqual(sc["by_geometry_scale"]["x0.5"] * 1e6, 65.6, delta=1.0)
        self.assertAlmostEqual(sc["by_geometry_scale"]["x2"] * 1e6, 259.0, delta=3.0)
        self.assertAlmostEqual(cn["dephasing_threshold_per_s"] * cn["rijavec_tau_g_s"], 1.0, delta=0.02)
        bad = run(PY + [str(SKILLS / "t05" / "verify_t05_dispute_kernel.py"), "--planted-defect"])
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn("FAIL", bad.stderr)
        self.assertIn("entangles everywhere", bad.stderr)
        ref = json.loads((TG / "t05" / "files" / "t05_reference.json").read_text(encoding="utf-8"))
        self.assertIn("dispute_kernel", ref)
        self.assertIsNone(ref["dispute_kernel"]["tn_fig3"]["50um"]["last_entangled_time_s"])

    def test_dispute_text_instrument_and_labels_pick_no_side(self) -> None:
        en, es = TG / "t05" / "index.html", TG_ES / "t05" / "index.html"
        self.assertEqual(labels_of(en), labels_of(es))
        txt = en.read_text(encoding="utf-8")
        for s in ("0.8508σ", "0.8501σ", "5 hours, 16 hours and 20 days", "18 % of", "525 µm", "KΔx²/(2ħ)", "ratio 1.000", "52 µm", "38.6 µm", "48 µm",
                  "the page still picks no side", "follows the gas pressure in proportion", "neither prepares a spatial superposition", "is not among the measurements this page found", "a collision rate 1.4 times higher at the same pressure", "6.4 × 10¹² per second for each pascal", "ten orders of magnitude lighter", "tests no physics", "1.2 × 10⁻¹⁷ Pa", "about 28 atoms in a cubic centimetre", "with its sixth root", "necessary conditions, not a budget", "pronounces on no experiment's feasibility", "model-dependent upper limits", "Table T.05-H", "leaves it open", "computed, not chosen", "predicts entanglement only", "also a collapse test", "unless σ is above 130 µm", "would not by itself separate", "more than five orders", "letter's closer geometry", "66 and 259 µm", "for any value of its parameters", "within 1 % of the 1/τ_G", "nonlocal features", "one geometric axis", "1.2 to 38 times d", "0.37 to 1.0 times d", "draws no conclusion from the gap", "data-tg-figure=\"threshold-map\"", "a model difference, not an exclusion region", "data-tg-read=\"col\"", "the hybrid σ_c above is 4.0 × this", "the one explicit classical model on the page", "remove the whole 120-fold torque", "beyond that reach could be attributed to this model only with", "this page assesses none of them", "the signed limit the smeared pull faces", "time does the separating", "full entanglement in 14 hours", "roughly four to sixty times later", "does not predict a witness of the quantum channel's size", "Side by side the threshold drops", "among the geometries mapped here it is", "data-tg-figure=\"proposals-table\"", "not exclusions of anything", "in the collinear layout of the 2017 proposal", "so the table carries both readings", "Decoherence enters the same way for both models", "forty-five to a hundred and twenty-five times lower", "computes the two thresholds and measures neither", "The dispute's other classical route can be put on the same map", "approaching the Planck mass and beyond", "order-of-magnitude readings, not a", "where the model's entangling power sits", "zero wherever the kernel looks", "0.024 against", "the noise term only takes away", 'data-tg-logsig', 'class="tg-bmv-dp"', 'data-tg-read="ktm"', 'data-tg-read="dp"', 'data-tg-read="soft"'):
            self.assertIn(s, txt, f"T.05 lacks {s!r}")
        low = txt.lower()
        for banned in ("the model is right", "the model is wrong", "classical gravity is ruled out", "classical gravity is confirmed", "unifies"):
            self.assertNotIn(banned, low)
        self.assertEqual(txt.count('data-tg-channel="'), 3)  # still three channels at equal weight
        mjs = (RESEARCH / "modules" / "timegravity-slope.mjs").read_text(encoding="utf-8")
        for s in ("export function tnNegativity", "export function tnCriticalSigma", "export function ktmGammaT", "export function dpCollapseNegativity", "export function dpCollapseSigma", "export function negativityOfRho"):
            self.assertIn(s, mjs)


class TimeGravitySmearedIslTests(unittest.TestCase):
    """The smeared pull set beside the sub-millimetre inverse-square-law tests: plate modes, the Eöt-Wash mapping, the page's wording."""

    def test_isl_verifier_numbers_and_planted_defect(self) -> None:
        res = run(PY + [str(SKILLS / "t05" / "verify_t05_smeared_isl.py")])
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        payload = json.loads(res.stdout)
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(payload["geometry_checks"]["planted_defect_knockout"], "REJECTED_AS_EXPECTED")
        cn = payload["central_number"]
        self.assertLess(cn["plate_mode_closed_vs_quadrature_max_diff"], 1e-9)
        self.assertAlmostEqual(cn["one_mode_eotwash_deficit_at_52um_by_sigma"]["75um"], 0.1037, delta=0.002)
        self.assertAlmostEqual(cn["one_mode_yukawa_edge_deficit_120fold"], 0.0152, delta=0.0005)
        self.assertAlmostEqual(cn["one_mode_sigma_matching_edge_120fold_m"] * 1e6, 44.4, delta=0.5)
        self.assertAlmostEqual(cn["sigma_c_letter_geometry_m"] * 1e6, 54.9, delta=0.3)
        self.assertLess(cn["bessel_max_abs_diff"], 1e-9)
        self.assertLess(cn["radial_series_max_rel_diff"], 1e-6)
        self.assertAlmostEqual(cn["newton_torque_fNm"]["72um"]["T120_fNm"], 1.508, delta=0.02)
        self.assertAlmostEqual(cn["wedge_deficit_at_52um_by_sigma"]["75um"], 0.1699, delta=0.003)
        self.assertAlmostEqual(cn["wedge_deficit_at_52um_by_sigma"]["50um"], 0.0433, delta=0.001)
        self.assertAlmostEqual(cn["wedge_deficit_at_52um_by_sigma"]["55um"], 0.0625, delta=0.001)
        self.assertAlmostEqual(cn["wedge_yukawa_edge_deficit_120fold"], 0.0254, delta=0.0005)
        self.assertAlmostEqual(cn["wedge_sigma_matching_edge_120fold_m"] * 1e6, 44.1, delta=0.5)
        self.assertGreater(cn["wedge_deficit_at_52um_by_sigma"]["75um"], cn["one_mode_eotwash_deficit_at_52um_by_sigma"]["75um"])  # the full pattern removes more than the bound
        fit = cn["wedge_best_yukawa_for_sigma_75um_120fold"]
        self.assertTrue(45e-6 < fit["lambda_m"] < 55e-6, fit)
        self.assertTrue(-3.6 < fit["alpha"] < -2.6, fit)
        self.assertLess(cn["wedge_deficit_sigma_75um_by_separation"]["300um"], 2e-3)
        win = cn["window_at_matching_sigma"]
        self.assertAlmostEqual(win["d_c_small_split_m"] * 1e6, 37.5, delta=0.5)
        self.assertAlmostEqual(win["d_c_letter_split_m"] * 1e6, 14.9, delta=0.5)
        hp = cn["hust_pair_level"]
        self.assertAlmostEqual(hp["smeared_by_sigma"]["75um"], 0.0477, delta=0.0005)
        self.assertAlmostEqual(hp["yukawa_edge_alpha_1_lambda_48um"], 0.0126, delta=0.0003)
        self.assertTrue(55e-6 < hp["sigma_matching_edge_m"] < 70e-6, hp)
        self.assertFalse(win["letter_geometry_entangles"])
        bad = run(PY + [str(SKILLS / "t05" / "verify_t05_smeared_isl.py"), "--planted-defect"])
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn("FAIL", bad.stderr)
        self.assertIn("quadrature", bad.stderr)
        ref = json.loads((TG / "t05" / "files" / "t05_reference.json").read_text(encoding="utf-8"))
        self.assertIn("smeared_isl_kernel", ref)
        self.assertAlmostEqual(ref["smeared_isl_kernel"]["eotwash"]["deficit_at_s_min_by_sigma"]["75um"]["120fold"], 0.1037, delta=0.002)
        self.assertAlmostEqual(ref["smeared_isl_kernel"]["wedge"]["deficit_at_52um_by_sigma"]["75um"]["120fold"], 0.1699, delta=0.003)

    def test_isl_text_readout_and_module(self) -> None:
        en, es = TG / "t05" / "index.html", TG_ES / "t05" / "index.html"
        self.assertEqual(labels_of(en), labels_of(es))
        txt = en.read_text(encoding="utf-8")
        for s in ("erfc(qσ − s/2σ)", "54 and 99 µm thick", "13.00 and 23.00 mm", "23.51 and 26.00 mm", "1.5 fN·m at 72 µm", "removes 17 %", "4.3 % at 50 µm", "6.3 % at 55 µm", "removes 2.5 %",
                  "33 µm", "one-mode lower bound", "near 49 µm", "recast of published limits, not a refit", "hundreds to thousands of times above", "not a gap in the data", "exclude σ above 33 µm at 95 %", "is superseded", "not a bound on σ", "surface gap of 210 µm", "4.8 % at σ = 75 µm", "the two match at σ ≈ 60 µm", "curve match with no data behind it", "below 27 µm", "below 6 µm", "was a looser reading and is superseded", "the change box keeps it", "had given 44.4 µm", "Casimir", "cannot fall below 17 µm", "it stays open, between 17 and 27 µm",
                  "previously untested", "leaves it open", "full wedge pattern", 'data-tg-read="isl"'):
            self.assertIn(s, txt, f"T.05 lacks {s!r}")
        low = txt.lower()
        for banned in ("is excluded", "is ruled out", "rules out the model", "excludes the model", "at least 10 %", "at least 17 %"):
            self.assertNotIn(banned, low)
        self.assertEqual(txt.count('data-tg-channel="'), 3)
        mjs = (RESEARCH / "modules" / "timegravity-slope.mjs").read_text(encoding="utf-8")
        for s in ("export function erfc", "export function plateModeRatio", "export function thickPlateRatio", "export function yukawaThickPlateRatio", "export function eotwashDeficit",
                  "export function besselJAll", "export function wedgeRadialSeries", "export function wedgeTorque", "export function wedgeDeficit"):
            self.assertIn(s, mjs)


class TimeGravityRefitScriptTests(unittest.TestCase):
    """The profile-likelihood refit script for the smeared pair potential, on its own synthetic data."""

    def test_refit_demo_bounds_newtonian_data_and_recovers_an_injected_sigma(self) -> None:
        res = run(PY + [str(ROOT / "tools" / "timegravity_refit_smeared.py"), "--demo", "--quick"], timeout=300)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        payload = json.loads(res.stdout)
        self.assertEqual(payload["status"], "PASS")
        nd = payload["newtonian_data"]
        self.assertTrue(20e-6 < nd["sigma_95_upper_m"] < 120e-6, nd)
        self.assertTrue(15e-6 < nd["lambda_95_upper_m_alpha_minus_1"] < 120e-6, nd)
        self.assertAlmostEqual(nd["gamma"], 1.0, delta=0.02)
        inj = payload["injected_sigma_75um"]
        self.assertIsNotNone(inj["smeared_best"])
        self.assertTrue(50e-6 < inj["smeared_best"]["param_m"] < 110e-6, inj)
        self.assertGreater(inj["chi2_newton"], inj["smeared_best"]["chi2"] + 3.84)
        lo, hi = inj["sigma_95_interval_m"]
        self.assertTrue(lo <= 75e-6 * 1.1 and hi >= 75e-6 * 0.9, inj)  # the injected value inside the 95 % interval, up to grid resolution


class TimeGravityBatch6Tests(unittest.TestCase):
    """T.08 (Horizon Thermodynamics / Rindler–Unruh–Hawking) and T.09 (Kerr Ringdown & Horizon Spectroscopy)."""

    def test_t08_and_t09_pages_verifiers_and_planted_defects(self) -> None:
        for slug, vname in (("t08", "verify_t08_horizon_thermodynamics.py"), ("t09", "verify_t09_kerr_ringdown.py")):
            for path in (TG / slug / "index.html", TG_ES / slug / "index.html", RESEARCH / "plates" / f"{slug}.png"):
                self.assertTrue(path.is_file(), f"missing {path}")
            gen = run(PY + [str(SKILLS / slug / f"make_{slug}.py")])
            self.assertEqual(gen.returncode, 0, gen.stdout + gen.stderr)
            res = run(PY + [str(SKILLS / slug / vname)])
            self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
            payload = json.loads(res.stdout)
            self.assertEqual(payload["status"], "PASS")
            self.assertEqual(payload["geometry_checks"]["planted_defect_knockout"], "REJECTED_AS_EXPECTED")
            bad = run(PY + [str(SKILLS / slug / vname), "--planted-defect"])
            self.assertNotEqual(bad.returncode, 0)
            self.assertIn("FAIL", bad.stderr)
        t08 = json.loads(run(PY + [str(SKILLS / "t08" / "verify_t08_horizon_thermodynamics.py")]).stdout)["central_number"]
        self.assertLess(t08["max_dev_from_planck"], 1e-12)
        self.assertLess(t08["entropy_dev_from_planck"], 1e-12)
        self.assertLess(t08["quadrature_vs_area_quarter_rel_err"], 1e-12)
        self.assertAlmostEqual(t08["solar_hawking_temp_k"] * 1e9, 61.7, delta=0.2)
        t09 = json.loads(run(PY + [str(SKILLS / "t09" / "verify_t09_kerr_ringdown.py")]).stdout)["central_number"]
        self.assertLess(t09["max_published_dev_220"], 1e-6)
        self.assertLess(t09["max_published_dev_221"], 1e-6)
        self.assertLess(t09["worst_smarr_rel_err"], 1e-12)
        self.assertLess(t09["max_cf_residual"], 1e-10)
        self.assertAlmostEqual(t09["gw150914_fiducial"]["f_220_hz"], 273.07, delta=0.5)
        self.assertAlmostEqual(t09["gw150914_fiducial"]["tau_220_ms"], 3.75, delta=0.05)

    def test_t08_t09_labels_boundary_instruments_and_reading_order(self) -> None:
        expect = {
            "t08": {"MEASURED", "DERIVED", "SINGLE RESULT", "OPEN"},
            "t09": {"MEASURED", "DERIVED", "SINGLE RESULT", "PROPOSED", "OPEN"},
        }
        for slug, labels in expect.items():
            en, es = TG / slug / "index.html", TG_ES / slug / "index.html"
            self.assertEqual(labels_of(en), labels_of(es), slug)
            self.assertEqual(set(labels_of(en)), labels, f"{slug}: {labels_of(en)}")
            for path, boundary in ((en, BOUNDARY_EN), (es, BOUNDARY_ES)):
                txt = path.read_text(encoding="utf-8")
                self.assertIn(boundary, txt)
                self.assertIn(f'data-tg-instrument="{"horizon" if slug == "t08" else "kerr"}"', txt)
                self.assertIn("data-tg-predict", txt)
                self.assertIn('class="tg-ai-line"', txt)
                for phrase in HUB_ONLY_PHRASES:
                    self.assertNotIn(phrase, txt.lower())
            self.assertEqual(builder.to_spanish_static(en.read_text(encoding="utf-8"), swap=False, shift=False), en.read_text(encoding="utf-8"))
        t08 = (TG / "t08" / "index.html").read_text(encoding="utf-8")
        for s in ("2.726 K", "61.7 nK", "Bose–Einstein condensate", "Does a real horizon have the hairless geometry"):
            self.assertIn(s, t08, f"T.08 lacks {s!r}")
        t09 = (TG / "t09" / "index.html").read_text(encoding="utf-8")
        for s in ("273.07 Hz", "3.747 ms", "266.80 Hz", "1.239 ms", "GW250114", "never recomputed from median masses", "If the classical horizon has no hair and only grows"):
            self.assertIn(s, t09, f"T.09 lacks {s!r}")
        # Reading order: T.07 -> T.08 -> T.09 -> T.10
        t07 = (TG / "t07" / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t08/"', t07)
        self.assertIn('class="tp-pager-link tp-pager-prev" href="../../timegravity/t07/"', t08)
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t09/"', t08)
        self.assertIn('class="tp-pager-link tp-pager-prev" href="../../timegravity/t08/"', t09)
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t10/"', t09)


class TimeGravityBatch7Tests(unittest.TestCase):
    """T.11 (Einselection, Pointer States & the Electromagnetic Bath) and T.12 (Dark Sectors, Equivalence & Clock Networks)."""

    def test_t11_and_t12_pages_verifiers_and_planted_defects(self) -> None:
        for slug, vname in (("t11", "verify_t11_einselection.py"), ("t12", "verify_t12_dark_clock.py")):
            for path in (TG / slug / "index.html", TG_ES / slug / "index.html", RESEARCH / "plates" / f"{slug}.png"):
                self.assertTrue(path.is_file(), f"missing {path}")
            gen = run(PY + [str(SKILLS / slug / f"make_{slug}.py")])
            self.assertEqual(gen.returncode, 0, gen.stdout + gen.stderr)
            res = run(PY + [str(SKILLS / slug / vname)])
            self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
            payload = json.loads(res.stdout)
            self.assertEqual(payload["status"], "PASS")
            self.assertEqual(payload["geometry_checks"]["planted_defect_knockout"], "REJECTED_AS_EXPECTED")
            bad = run(PY + [str(SKILLS / slug / vname), "--planted-defect"])
            self.assertNotEqual(bad.returncode, 0)
            self.assertIn("FAIL", bad.stderr)
        t11 = json.loads(run(PY + [str(SKILLS / "t11" / "verify_t11_einselection.py")]).stdout)["central_number"]
        self.assertLess(t11["max_mi_dev_nats"], 1e-12)
        self.assertGreater(t11["k2_plateau_bits"], 0.90)
        self.assertLess(t11["coherence_ratio_n6"], 1e-3)
        self.assertAlmostEqual(t11["dust_10um_tau_cmb_s"], 1.634, delta=0.02)
        t12 = json.loads(run(PY + [str(SKILLS / "t12" / "verify_t12_dark_clock.py")]).stdout)["central_number"]
        self.assertAlmostEqual(t12["dark_to_baryon_ratio"], 5.3643, delta=0.002)
        self.assertLess(t12["quadrature_rel_err"], 1e-11)
        self.assertLess(t12["impulse_rel_err"], 1e-9)
        self.assertAlmostEqual(t12["uldm_1e15ev_phi_planck"] * 1e16, 7.20, delta=0.05)

    def test_t11_t12_labels_boundary_instruments_and_reading_order(self) -> None:
        expect = {
            "t11": {"MEASURED", "DERIVED", "PROPOSED", "BOUND", "OPEN"},
            "t12": {"MEASURED", "DERIVED", "BOUND", "PROPOSED", "OPEN"},
        }
        for slug, labels in expect.items():
            en, es = TG / slug / "index.html", TG_ES / slug / "index.html"
            self.assertEqual(labels_of(en), labels_of(es), slug)
            self.assertEqual(set(labels_of(en)), labels, f"{slug}: {labels_of(en)}")
            for path, boundary in ((en, BOUNDARY_EN), (es, BOUNDARY_ES)):
                txt = path.read_text(encoding="utf-8")
                self.assertIn(boundary, txt)
                self.assertIn(f'data-tg-instrument="{"einselection" if slug == "t11" else "dark_clock"}"', txt)
                self.assertIn("data-tg-predict", txt)
                self.assertIn('class="tg-ai-line"', txt)
                for phrase in HUB_ONLY_PHRASES:
                    self.assertNotIn(phrase, txt.lower())
            self.assertEqual(builder.to_spanish_static(en.read_text(encoding="utf-8"), swap=False, shift=False), en.read_text(encoding="utf-8"))
        t11 = (TG / "t11" / "index.html").read_text(encoding="utf-8")
        for s in ("pointer states", "Quantum Darwinism", "0.9983 bits", "1.63 s", "Three distinct concepts", "how could our clocks ever detect a sector of matter that never scatters light at all?"):
            self.assertIn(s, t11, f"T.11 lacks {s!r}")
        t12 = (TG / "t12" / "index.html").read_text(encoding="utf-8")
        for s in ("5.364", "84.3%", "Bullet Cluster", "LUX-ZEPLIN", "penultimate step of the fourteen-step track"):
            self.assertIn(s, t12, f"T.12 lacks {s!r}")
        # Reading order: T.10 -> T.11 -> T.12 -> T.13 (last page has tp-pager-empty)
        t10 = (TG / "t10" / "index.html").read_text(encoding="utf-8")
        t13 = (TG / "t13" / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t11/"', t10)
        self.assertIn('class="tp-pager-link tp-pager-prev" href="../../timegravity/t10/"', t11)
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t12/"', t11)
        self.assertIn('class="tp-pager-link tp-pager-prev" href="../../timegravity/t11/"', t12)
        self.assertIn('class="tp-pager-link tp-pager-next" href="../../timegravity/t13/"', t12)
        self.assertIn('class="tp-pager-link tp-pager-prev" href="../../timegravity/t12/"', t13)
        self.assertIn('class="tp-pager-link tp-pager-empty"', t13)



    def test_t13_page_verifier_planted_defect_and_lean4_prelude(self) -> None:
        for path in (TG / "t13" / "index.html", TG_ES / "t13" / "index.html", RESEARCH / "plates" / "t13.png"):
            self.assertTrue(path.is_file(), f"missing {path}")
        gen = run(PY + [str(SKILLS / "t13" / "make_t13.py")])
        self.assertEqual(gen.returncode, 0, gen.stdout + gen.stderr)
        verify = SKILLS / "t13" / "verify_t13_holonomy_soft.py"
        res = run(PY + [str(verify)])
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        payload = json.loads(res.stdout)
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(payload["geometry_checks"]["planted_defect_knockout"], "REJECTED_AS_EXPECTED")
        cn = payload["central_number"]
        gc = payload["geometry_checks"]
        self.assertLess(cn["s2_ward_vector_rel_norm"], 1e-14)
        self.assertGreater(gc["planted_s2_ward_rel_norm"], 1e-6)
        self.assertAlmostEqual(cn["gw150914_delta_h_char"] * 1e22, 7.003, delta=0.02)
        self.assertLess(cn["memory_quadrature_rel_err"], 1e-12)
        self.assertEqual(cn["sm_nc_unique"], 3)
        self.assertEqual(gc["planted_nc2_cubic_trace"], 54)
        self.assertGreaterEqual(cn["lean_theorem_count"], 12)
        bad = run(PY + [str(verify), "--planted-defect"])
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn("FAIL", bad.stderr)

        en, es = TG / "t13" / "index.html", TG_ES / "t13" / "index.html"
        self.assertEqual(labels_of(en), labels_of(es))
        self.assertEqual(set(labels_of(en)), {"MEASURED", "DERIVED", "BOUND", "SINGLE RESULT", "PROPOSED", "OPEN"})
        for path, boundary in ((en, BOUNDARY_EN), (es, BOUNDARY_ES)):
            txt = path.read_text(encoding="utf-8")
            self.assertIn(boundary, txt)
            self.assertIn('data-tg-instrument="holonomy_soft"', txt)
            self.assertIn("data-tg-predict", txt)
            self.assertIn('class="tg-ai-line"', txt)
            for phrase in HUB_ONLY_PHRASES:
                self.assertNotIn(phrase, txt.lower())


class TimeGravityHumansAndPlatesTests(unittest.TestCase):
    """Human lineage vitrines, bespoke apparatus SVG medallions, and unique Plate {code}-D diagrams across all 13 pages."""

    def test_every_page_honors_the_humans_with_lineage_and_apparatus_medallions(self) -> None:
        slugs = ("", "t01", "t02", "t03", "t04", "t05", "t06", "t07", "t08", "t09", "t10", "t11", "t12", "t13")
        html_files: list[Path] = []
        for slug in slugs:
            en = (TG / slug / "index.html") if slug else (TG / "index.html")
            es = (TG_ES / slug / "index.html") if slug else (TG_ES / "index.html")
            html_files.extend([en, es])
            self.assertEqual(labels_of(en), labels_of(es), f"{slug or 'hub'}: EN/ES claim labels diverged")
            en_jump = ">The Humans</a>" if slug else ">Humans (1905–2026)</a>"
            es_jump = ">Las Personas</a>" if slug else ">Personas (1905–2026)</a>"
            for path, jump_label in ((en, en_jump), (es, es_jump)):
                txt = path.read_text(encoding="utf-8")
                self.assertIn('class="tg-hero-lineage"', txt, f"{path} lacks .tg-hero-lineage")
                self.assertIn('id="humans"', txt, f"{path} lacks #humans section")
                self.assertIn('class="tg-humans-section"', txt, f"{path} lacks .tg-humans-section")
                self.assertIn('class="tg-humans-grid"', txt, f"{path} lacks .tg-humans-grid")
                self.assertGreaterEqual(txt.count('class="tg-human-card"'), 3, f"{path} has fewer than 3 human cards")
                self.assertGreaterEqual(txt.count('class="tg-apparatus-svg"'), 3, f"{path} lacks apparatus SVG medallions")
                self.assertIn(jump_label, txt, f"{path} lacks #humans jump pill")
        self.assertEqual(len(html_files), 28)
        for app in ("rindler-wedge", "horn-antenna", "sonic-horizon"):
            self.assertIn(f'data-apparatus="{app}"', (TG / "t08" / "index.html").read_text(encoding="utf-8"))
        for app in ("kerr-ergosphere", "continued-fraction", "ligo-interferometer"):
            self.assertIn(f'data-apparatus="{app}"', (TG / "t09" / "index.html").read_text(encoding="utf-8"))
        self.assertIn('data-apparatus="ligo-interferometer"', (TG / "t10" / "index.html").read_text(encoding="utf-8"))
        for root in (TG, TG_ES):
            t11_txt = (root / "t11" / "index.html").read_text(encoding="utf-8")
            for app in ("pointer-darwinism", "photon-scattering", "cavity-buckminster"):
                self.assertIn(f'data-apparatus="{app}"', t11_txt)
            t12_txt = (root / "t12" / "index.html").read_text(encoding="utf-8")
            for app in ("bullet-cluster-lensing", "dark-clock-comparison", "underground-crystal"):
                self.assertIn(f'data-apparatus="{app}"', t12_txt)
            t13_txt = (root / "t13" / "index.html").read_text(encoding="utf-8")
            self.assertIn('data-apparatus="soft-triangle"', t13_txt)

    def test_every_step_has_its_own_bespoke_plate_d_visual_intuition_bridge(self) -> None:
        seen_titles: set[str] = set()
        for code, slug in (("T.01", "t01"), ("T.02", "t02"), ("T.03", "t03"), ("T.04", "t04"),
                           ("T.05", "t05"), ("T.06", "t06"), ("T.07", "t07"), ("T.08", "t08"),
                           ("T.09", "t09"), ("T.10", "t10"), ("T.11", "t11"), ("T.12", "t12"), ("T.13", "t13")):
            for root, prefix in ((TG, "PLATE"), (TG_ES, "LÁMINA")):
                path = root / slug / "index.html"
                txt = path.read_text(encoding="utf-8")
                self.assertIn(f'id="tp-distill-title-{slug}"', txt, f"{path} lacks bespoke Plate D title id")
                self.assertIn(f"{prefix} {code}-D", txt, f"{path} lacks {prefix} {code}-D")
                if slug != "t01":
                    self.assertNotIn(f"{prefix} T.01-D", txt, f"{path} still repeats {prefix} T.01-D")
            en_txt = (TG / slug / "index.html").read_text(encoding="utf-8")
            m = re.search(rf'<title id="tp-distill-title-{slug}"[^>]*>([^<]+)</title>', en_txt)
            self.assertIsNotNone(m, f"{slug} missing <title id='tp-distill-title-{slug}'>")
            seen_titles.add(m.group(1))
        self.assertEqual(len(seen_titles), 13, "Every step T.01..T.13 must have a distinct Plate {code}-D SVG title")

    def test_derived_not_measured_chip_and_parent_tooltips(self) -> None:
        css = (ROOT / "src" / "timegravity.css").read_text(encoding="utf-8")
        self.assertIn('content: "DERIVED (NOT MEASURED)"', css)
        self.assertIn('content: "DERIVADO (NO MEDIDO)"', css)
        self.assertIn('html[lang^="es"] .tg-claim[data-tg-label="DERIVED"]::after', css)
        hub_en = (TG / "index.html").read_text(encoding="utf-8")
        hub_es = (TG_ES / "index.html").read_text(encoding="utf-8")
        self.assertIn("computed, not directly measured", hub_en)
        self.assertIn("calculado, no medido directamente", hub_es)
        for slug in ("t05", "t06", "t11", "t12", "t13"):
            en_txt = (TG / slug / "index.html").read_text(encoding="utf-8")
            es_txt = (TG_ES / slug / "index.html").read_text(encoding="utf-8")
            self.assertIn('data-tg-qualifier="DERIVED (NOT MEASURED)"', en_txt)
            self.assertIn('data-tg-qualifier="DERIVADO (NO MEDIDO)"', es_txt)
            self.assertIn("Derived by mathematics/kernel from MEASURED parent row ", en_txt)
            self.assertIn("Derivado por matemáticas/kernel de la fila madre MEDIDA ", es_txt)
        # Epistemological guardrails: T.05 pure-collapse BMV hypothesis and T.12 unbuilt sensor proposal stay PROPOSED.
        self.assertEqual(labels_of(TG / "t05" / "index.html").count("DERIVED"), 12)
        self.assertEqual(labels_of(TG / "t06" / "index.html").count("DERIVED"), 2)
        self.assertEqual(labels_of(TG / "t12" / "index.html").count("PROPOSED"), 1)


if __name__ == "__main__":
    unittest.main()

