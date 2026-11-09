"""Verification suite for the Time & Gravity track (T.00 hub + T.01), beside the Folio count of 48."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "src" / "research"
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
        self.assertEqual(len(TRACK_MAP), 9)
        self.assertEqual([m["code"] for m in TRACK_MAP], ["T.00", "T.02", "T.01", "T.03", "T.04", "T.05", "T.06", "T.07", "T.10"])

    def test_scaffold_files_exist(self) -> None:
        for rel in ("timegravity/README.md", "timegravity/run_all_timegravity.py", "timegravity/ledger.json",
                    "timegravity/ledger.schema.json", "timegravity/make_plates.py", "timegravity/refresh_crossref_cache.py",
                    "tools/check_timegravity_labels.py", "tools/build_timegravity.py", "tools/timegravity_kernel.py",
                    "skills/timegravity/README.md", "skills/timegravity/t01/SKILL.md", "skills/timegravity/t01/make_t01.py",
                    "skills/timegravity/t01/verify_t01_time_slope_geodesic.py", "src/research/modules/timegravity-slope.mjs",
                    "src/research/timegravity.css", "src/research/plates/t00.png", "src/research/plates/t01.png",
                    "src/research/timegravity/t01/files/t01_reference.json", "src/research/timegravity/t01/files/manifest.json"):
            self.assertTrue((ROOT / rel).is_file(), f"missing {rel}")

    def test_ledger_schema_fields_and_offline_crossref_resolution(self) -> None:
        ledger = json.loads((ROOT / "timegravity" / "ledger.json").read_text(encoding="utf-8"))
        cache = json.loads((ROOT / "data" / "folio-citations.cache.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(ledger["rows"]), 6)
        for row in ledger["rows"]:
            self.assertEqual(set(row) - {"note"}, {"id", "label", "doi", "year", "collaboration", "kind", "review_by"}, row["id"])
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
            self.assertEqual(raw.count("<li data-built="), 9)
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
        self.assertIn('class="tp-pager-link tp-pager-next" href="../timegravity/t01/"', en_hub)

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
        es_hub = (RESEARCH / "es-mx" / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="timegravity/"', es_hub)
        xml = (RESEARCH / "sitemap.xml").read_text(encoding="utf-8")
        for url in ("https://informatico.ai/timegravity/", "https://informatico.ai/timegravity/t01/",
                    "https://informatico.ai/es-mx/timegravity/", "https://informatico.ai/es-mx/timegravity/t01/"):
            self.assertIn(f"<loc>{url}</loc>", xml)
        llms = (RESEARCH / "llms.txt").read_text(encoding="utf-8")
        self.assertIn("(https://informatico.ai/timegravity/)", llms)
        self.assertIn("(https://informatico.ai/timegravity/t01/)", llms)
        self.assertIn("## Time & Gravity", llms)

    def test_one_command_runner_passes(self) -> None:
        res = run(PY + [str(ROOT / "timegravity" / "run_all_timegravity.py")], timeout=120)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("PASS: Time & Gravity:", res.stdout)
        self.assertEqual(res.stdout.count("REJECTED_AS_EXPECTED:"), 2)

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


if __name__ == "__main__":
    unittest.main()
