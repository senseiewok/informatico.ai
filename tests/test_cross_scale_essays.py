"""Deterministic verification suite for Informatico.ai Cross-Scale Featured Essays (/essays/ & /es-mx/essays/)."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "src"
SKILLS = ROOT / "skills" / "essays"
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tests"))

import build_cross_scale_essays as cse  # noqa: E402
import build_longform_folios as builder  # noqa: E402
from folios.essays import ESSAYS  # noqa: E402
from folios.seo_copy import BRAND  # noqa: E402,F401
from test_informatico_seo import DANGLING, FORMULA, SITE, parse, url_to_file  # noqa: E402


class CrossScaleEssaysTests(unittest.TestCase):
    def test_seven_essays_and_hub_built_in_english_and_spanish_with_seo_and_jsonld(self) -> None:
        self.assertEqual([e["code"] for e in ESSAYS], ["ES.01", "ES.02", "ES.03", "ES.04", "ES.05", "ES.06", "ES.07"])
        self.assertEqual(
            [e["slug"] for e in ESSAYS],
            [
                "mesoscopic-floor",
                "derived-not-measured",
                "barriers-pores-clocks",
                "tensegrity-microcausality-zero-modes",
                "islands-blinders-conditional-survival",
                "coupled-constraints-formal-proof",
                "loophole-free-parallel-horizon",
            ],
        )

        routes = [("essays/", RESEARCH / "essays" / "index.html", RESEARCH / "es-mx" / "essays" / "index.html")]
        for e in ESSAYS:
            slug = e["slug"]
            t_en, d_en, t_es, d_es = e["seo"]
            for t_str in (t_en, t_es):
                self.assertTrue(18 <= len(t_str) <= 52, f"{slug}: title length {len(t_str)} out of 18..52: {t_str!r}")
            for d_str in (d_en, d_es):
                self.assertTrue(110 <= len(d_str) <= 158 and d_str.endswith("."), f"{slug}: desc budget failed: {d_str!r}")
                self.assertIsNone(FORMULA.search(d_str), f"{slug}: formula char in desc: {d_str!r}")
                self.assertNotIn("medical", d_str.lower())
                self.assertNotIn("médic", d_str.lower())
                last = re.findall(r"[\wÀ-ÿ]+", d_str)[-1].lower()
                self.assertNotIn(last, DANGLING, f"{slug}: dangling end word in {d_str!r}")
            routes.append((f"essays/{slug}/", RESEARCH / "essays" / slug / "index.html", RESEARCH / "es-mx" / "essays" / slug / "index.html"))

        for path, en_file, es_file in routes:
            self.assertTrue(en_file.is_file(), f"Missing {en_file}")
            self.assertTrue(es_file.is_file(), f"Missing {es_file}")
            en, es = parse(en_file), parse(es_file)
            en_url, es_url = SITE + path, SITE + "es-mx/" + path
            self.assertEqual(en.html_lang, "en", path)
            self.assertEqual(es.html_lang, "es-MX", path)
            self.assertNotEqual(en.title, es.title, path)
            self.assertNotEqual(en.h1, es.h1, path)
            for doc, canon, lang_code in ((en, en_url, "en"), (es, es_url, "es-MX")):
                links = {(l.get("rel"), l.get("hreflang")): l.get("href") for l in doc.links}
                self.assertEqual(links[("canonical", None)], canon)
                self.assertEqual(links[("alternate", "en")], en_url)
                self.assertEqual(links[("alternate", "es-MX")], es_url)
                self.assertEqual(links[("alternate", "x-default")], en_url)
                data = json.loads(doc.ld[0])
                node = data["@graph"][0]
                self.assertEqual(node["inLanguage"], lang_code)
                self.assertEqual(node["@type"], "CollectionPage" if path == "essays/" else "ScholarlyArticle")
            # Spanish address resolution
            base = SITE + "es-mx/" + path
            for attr, value in es.refs:
                if value.startswith(("#", "mailto:", "data:")) or (value.startswith("http") and not value.startswith(SITE)):
                    continue
                target = url_to_file(urljoin(base, value))
                if target is not None:
                    self.assertTrue(target.exists(), f"/es-mx/{path}: {attr}={value!r} -> {target} missing")
                    if attr == "href" and target.name == "index.html" and "/es-mx/" not in urljoin(base, value) and not value.startswith("http"):
                        self.fail(f"/es-mx/{path}: page link {value!r} leaves Spanish tree")
            # No-op Spanish static copier identity
            en_raw = en_file.read_text(encoding="utf-8")
            self.assertEqual(builder.to_spanish_static(en_raw, swap=False, shift=False), en_raw)

    def test_unique_plates_cached_dois_and_verifiers_with_planted_defects(self) -> None:
        cache = json.loads((ROOT / "data" / "folio-citations.cache.json").read_text(encoding="utf-8"))
        seen_hashes: dict[str, str] = {}
        for e in ESSAYS:
            pslug = e["plate_slug"]
            p = RESEARCH / "plates" / f"{pslug}.png"
            self.assertTrue(p.is_file(), f"Missing {p}")
            raw = p.read_bytes()
            self.assertEqual(raw[:8], b"\x89PNG\r\n\x1a\n")
            digest = hashlib.sha256(raw).hexdigest()
            self.assertNotIn(digest, seen_hashes, f"Duplicate PNG plate {pslug}")
            seen_hashes[digest] = pslug

            self.assertGreaterEqual(len(e["sources"]), 6, e["code"])
            for s in e["sources"]:
                key = f"doi:{s['doi'].lower()}"
                self.assertIn(key, cache, f"{e['code']} source {key} missing from offline DOI cache")

            skill_md = ROOT / e["skill_path"]
            ver_py = ROOT / e["verifier_path"]
            self.assertTrue(skill_md.is_file(), f"Missing {skill_md}")
            self.assertTrue(ver_py.is_file(), f"Missing {ver_py}")

            ok = subprocess.run([sys.executable, "-X", "utf8", str(ver_py)], capture_output=True, text=True, encoding="utf-8", timeout=30)
            self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
            payload = json.loads(ok.stdout)
            self.assertEqual(payload.get("status"), "PASS")

            bad = subprocess.run([sys.executable, "-X", "utf8", str(ver_py), "--planted-defect"], capture_output=True, text=True, encoding="utf-8", timeout=30)
            self.assertNotEqual(bad.returncode, 0, f"{ver_py} must fail closed on --planted-defect")

    def test_featured_linking_on_home_physics_timegravity_and_contents(self) -> None:
        for rel in ("index.html", "physics/index.html", "timegravity/index.html"):
            txt = (RESEARCH / rel).read_text(encoding="utf-8")
            self.assertIn('id="cross-scale-essays"', txt, rel)
            for e in ESSAYS:
                self.assertIn(f"essays/{e['slug']}/", txt, rel)
        for lean_rel, min_thms in (
            (SKILLS / "coupled-constraints-formal-proof" / "IRUG_Unification.lean", 4),
            (SKILLS / "loophole-free-parallel-horizon" / "ParallelHorizon.lean", 9),
        ):
            self.assertTrue(lean_rel.is_file(), f"Missing Lean 4 companion {lean_rel}")
            lean_src = lean_rel.read_text(encoding="utf-8")
            lean_code = re.sub(r"/--?.*?-/", "", lean_src, flags=re.S)
            lean_code = re.sub(r"--.*?$", "", lean_code, flags=re.M)
            self.assertIsNone(re.search(r"\b(sorry|sorryAx|admit|axiom)\b", lean_code), f"Forbidden sorry/admit/axiom in {lean_rel.name}")
            self.assertGreaterEqual(len(re.findall(r"\btheorem\s+\w+", lean_code)), min_thms)
        catalog = builder.update_catalogs()
        for e in ESSAYS:
            slug = e["slug"]
            en_expected = cse.render_essay_page(e, list(ESSAYS), catalog, "en")
            es_expected = builder.to_spanish_static(cse.render_essay_page(e, list(ESSAYS), catalog, "es"))
            self.assertEqual((RESEARCH / "essays" / slug / "index.html").read_text(encoding="utf-8"), en_expected)
            self.assertEqual((RESEARCH / "es-mx" / "essays" / slug / "index.html").read_text(encoding="utf-8"), es_expected)


if __name__ == "__main__":
    unittest.main()
