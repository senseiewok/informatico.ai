"""CC.01 (Golf GTI cult classic): grounding, privacy, CSP and accessibility guards.

These encode the decisions of the 2026-11-15 proposal review: neutral easter-egg caption, no paint name, no owner,
no unearned superlatives, every stamp resolving to a listed source, no inline script or style, a pause control and a
static page under reduced motion.
"""
from __future__ import annotations

import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
sys.path.insert(0, str(ROOT / "tools"))

from folios.classics import cc01 as C  # noqa: E402

EN = SRC / "classics" / C.SLUG / "index.html"
ES = SRC / "es-mx" / "classics" / C.SLUG / "index.html"
CSS = SRC / "cult-classics.css"
JS = SRC / "modules" / "cult-classics.mjs"
PHOTO = SRC / C.EGG["image"]


class Visible(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.text: list[str] = []
        self.attrs: list[tuple[str, str, str]] = []
        self.tags: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag in ("script", "style"):
            self._skip += 1
        for k, v in attrs:
            self.attrs.append((tag, k, v or ""))

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.text.append(data)


def parse_text(html: str) -> list[str]:
    v = Visible()
    v.feed(html)
    return v.text


def parse(path: Path) -> Visible:
    v = Visible()
    v.feed(path.read_text(encoding="utf-8"))
    return v


class CultClassicPages(unittest.TestCase):
    def test_both_languages_exist_with_their_own_language(self):
        self.assertIn('<html lang="en">', EN.read_text(encoding="utf-8"))
        es = ES.read_text(encoding="utf-8")
        self.assertIn('<html lang="es-MX">', es)
        self.assertIn("Un reto, ocho respuestas", es)
        for value in C.VALUE_ES.values():
            self.assertIn(value, es, "spec-plate value left in English on the Spanish page")

    def test_no_inline_script_style_or_style_attribute(self):
        sys.path.insert(0, str(ROOT / "deploy"))
        from check_upload import _InlineScriptChecker  # noqa: E402  (HTML tokenizer, not a tag regex)

        for page in (EN, ES):
            v = parse(page)
            self.assertNotIn("style", v.tags, page)
            self.assertFalse(any(k == "style" for _t, k, _v in v.attrs), f"{page}: style attribute")
            checker = _InlineScriptChecker()
            checker.feed(page.read_text(encoding="utf-8"))
            self.assertFalse(checker.has_executable_inline_script, f"{page}: executable inline script")

    def test_no_unearned_superlatives_or_ownership(self):
        for page in (EN, ES):
            visible = " ".join(parse(page).text).lower()
            for phrase in C.BANNED:
                self.assertNotIn(phrase.lower(), visible, f"{page}: banned phrase {phrase!r}")

    def test_easter_egg_caption_is_the_maintainers_decision(self):
        # Maintainer decision 2026-11-15: name the paint and the wheel maker, link the maker, name no owner.
        self.assertEqual(C.EGG["caption_en"], "A 2018 Mk7.5 Golf GTI with a Cobb Stage 2 tune and BBS wheels, in Dark Iron Blue Metallic.")
        self.assertEqual(C.EGG["caption_es"], "Un Golf GTI Mk7.5 2018 con reprogramación Cobb Stage 2 y rines BBS, en Dark Iron Blue Metallic.")
        owner = re.compile(r"\b(my|mine|our|owner|owned|mi|mío|nuestro|dueño)\b", re.I)
        for key in ("caption_en", "caption_es", "alt_en", "alt_es"):
            self.assertIsNone(owner.search(C.EGG[key]), key)
        for page in (EN, ES):
            self.assertIn('<a href="https://www.bbs.com/" rel="noopener noreferrer">BBS</a>', page.read_text(encoding="utf-8"))
            self.assertIn('<a href="https://momo.com/" rel="noopener noreferrer">MOMO</a>', page.read_text(encoding="utf-8"))
            self.assertIn('<a href="https://www.cobbtuning.com/" rel="noopener noreferrer">Cobb</a>', page.read_text(encoding="utf-8"))
        # A caption may name parts; it may not state performance figures for the photographed car.
        self.assertIsNone(re.search(r"\\d+\\s?(?:hp|PS|bhp|Nm|lb-ft|kW)", C.EGG['caption_en'] + C.EGG['caption_es']))
        # Two photographs ship with the feature (maintainer, 2026-11-15): hood-up and side-on track.
        self.assertEqual(sorted(p.name for p in PHOTO.parent.iterdir()), sorted([PHOTO.name, Path(C.EGG_SIDE['image']).name]))

    def test_lap_arithmetic_in_the_copy_follows_from_the_table(self):
        secs = {car: s for _g, car, _y, _ps, _ts, s, *_rest in C.LAPS}
        first, cs_s = secs["Golf IV GTI “25 Jahre GTI”"], secs["Golf VII GTI Clubsport S"]
        self.assertEqual(round(first - cs_s), 57)
        self.assertIn("57 seconds", C.LAPS_TEXT["read_en"])
        self.assertEqual(round(first - secs["Golf VII GTI Performance"]), 25)
        self.assertIn("25 seconds", C.LAPS_TEXT["read_en"])
        specials = [lap[5] for lap in C.LAPS if lap[2] >= 2016]
        self.assertLessEqual(max(specials) - min(specials), 10)
        self.assertIn("within ten seconds", C.LAPS_TEXT["read_en"])
        for lap in C.LAPS:
            ts, s = lap[4], lap[5]
            m, rest = ts.split(":")
            self.assertAlmostEqual(int(m) * 60 + float(rest), s, places=2, msg=ts)
            self.assertIn(f">{ts}<", EN.read_text(encoding="utf-8"))

    def test_photo_carries_no_metadata(self):
      for photo in (PHOTO, SRC / C.EGG_SIDE['image']):
        data = photo.read_bytes()
        self.assertTrue(data.startswith(b"\xff\xd8"), "not a JPEG")
        for marker in (b"Exif\x00\x00", b"http://ns.adobe.com/xap", b"ICC_PROFILE", b"GPS"):
            self.assertNotIn(marker, data[:65536], f"photo carries {marker!r}")

    def test_every_stamp_resolves_and_every_source_is_used(self):
        txt = EN.read_text(encoding="utf-8")
        used = set(re.findall(r'href="#src-([a-z0-9-]+)"', txt))
        listed = set(re.findall(r'<li id="src-([a-z0-9-]+)"', txt))
        self.assertEqual(listed, set(C.SOURCES))
        self.assertTrue(used <= listed, used - listed)
        self.assertEqual(used, listed, f"listed but never cited: {listed - used}")
        for key, s in C.SOURCES.items():
            self.assertIn(s["kind"], C.KIND_LABEL, key)
            self.assertTrue(s["url"].startswith("https://"), key)
            if s["kind"] == "paper":
                self.assertTrue(s["url"].startswith("https://doi.org/10."), key)

    def test_papers_are_framed_as_general_mechanisms(self):
        for block in (C.DIFF_TEXT["science_en"], C.DCT_TEXT["science_en"], C.UNSPRUNG_TEXT["en"], C.BOOST["note_en"]):
            self.assertRegex(block, r"not a Golf|Neither (?:paper|review) tested|not hot hatches", block[:60])
        self.assertIn("not the Nordschleife’s shape", C.LAPS_TEXT["loop_en"])
        self.assertIn("not part of this comparison", C.LAPS_TEXT["caveat_en"])

    def test_motion_is_pausable_and_static_when_reduced(self):
        txt = EN.read_text(encoding="utf-8")
        self.assertIn('class="cc-parade" aria-hidden="true"', txt)
        self.assertIn('class="cc-track" viewBox="0 0 1600 1000" preserveAspectRatio="xMidYMid slice" aria-hidden="true"', txt)
        js = JS.read_text(encoding="utf-8")
        self.assertIn('passive: true', js)
        self.assertIn('reduceMotion.matches || document.documentElement.classList.contains("cc-paused")', js)
        self.assertIn("data-cc-pause", txt)
        css = CSS.read_text(encoding="utf-8")
        self.assertIn("@media (prefers-reduced-motion: reduce)", css)
        self.assertIn("html.cc-paused .cc-lane", css)
        self.assertIn("@media (forced-colors: active)", css)
        self.assertIn("@media print", css)

    def test_controls_are_labelled_native_inputs(self):
        txt = EN.read_text(encoding="utf-8")
        for rid in ("cc-throttle", "cc-steer-range"):
            self.assertIn(f'<label class="cc-range-label" for="{rid}">', txt)
            self.assertRegex(txt, rf'<input id="{rid}" class="cc-range" type="range"[^>]*aria-valuetext=')
        self.assertIn('aria-controls="cc-egg-panel"', txt)
        self.assertIn('aria-live="polite"', txt)

    def test_script_respects_trusted_types_and_csp(self):
        js = JS.read_text(encoding="utf-8")
        for bad in ("innerHTML", "outerHTML", "insertAdjacentHTML", ".style.", "eval(", "new Function"):
            self.assertNotIn(bad, js, bad)

    def test_mechanics_lab_verifier_passes_and_every_knockout_fails(self):
        import subprocess
        verify = ROOT / "skills" / "classics" / "cc01" / "verify_cc01_mechanics.py"
        self.assertTrue((verify.parent / "SKILL.md").is_file())
        ok = subprocess.run([sys.executable, "-X", "utf8", str(verify)], capture_output=True, text=True, encoding="utf-8", timeout=60)
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertIn('"status": "PASS"', ok.stdout)
        for variant in ("", "=open-factor", "=config", "=swap-k"):
            bad = subprocess.run([sys.executable, "-X", "utf8", str(verify), "--planted-defect" + variant],
                                 capture_output=True, text=True, encoding="utf-8", timeout=60)
            self.assertNotEqual(bad.returncode, 0, f"knockout {variant or 'lsd-direction'} passed")

    def test_lab_labels_model_values_and_cites_its_physics(self):
        txt = EN.read_text(encoding="utf-8")
        self.assertIn('id="part-6"', txt)
        self.assertIn("Inputs (MODEL)", txt)
        for key in ("scamarcio2023", "micromachines2026", "ahmadian2000", "kakalis2008"):
            self.assertIn(f'href="#src-{key}"', txt)
        self.assertEqual(txt.count('data-lap-kmh="'), 4)  # only rows with a stated track length
        self.assertEqual(txt.count("cc-ghost-nolen"), 8)  # 4 hollow dots + 4 hollow legend keys

    def test_both_languages_print_the_same_figures(self):
        """Every number with a unit (PS, Nm, km/h, Hz, kg, mm, s, lap times) appears in both languages."""
        unit = re.compile(r"\b\d[\d,.]*\s?(?:PS|Nm|km/h|Hz|kg|mm|N/m)\b|\b\d:\d\d(?:\.\d\d)?\b")

        def figures(page: Path) -> set[str]:
            html = page.read_text(encoding="utf-8")
            body = html[html.index('<article class="cc-feature'):html.index('id="sources"')]
            text = " ".join(parse_text(body))
            return {re.sub(r"\s", "", m) for m in unit.findall(text)}

        en, es = figures(EN), figures(ES)
        self.assertEqual(en - es, set(), "figures only in English")
        self.assertEqual(es - en, set(), "figures only in Spanish")

    def test_sitemap_and_llms_list_the_feature(self):
        xml = (SRC / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn(f"<loc>https://informatico.ai/classics/{C.SLUG}/</loc>", xml)
        self.assertIn(f"<loc>https://informatico.ai/es-mx/classics/{C.SLUG}/</loc>", xml)
        self.assertIn(f"https://informatico.ai/classics/{C.SLUG}/", (SRC / "llms.txt").read_text(encoding="utf-8"))

    def test_revamp_monograph_sections_audio_crossword_and_racks(self):
        en_html = EN.read_text(encoding="utf-8")
        es_html = ES.read_text(encoding="utf-8")
        self.assertEqual(len(C.SOURCES), 37)
        self.assertNotIn("jugada", es_html.lower())
        for needle in (
            'id="relay"',
            'id="axle-anatomy"',
            'id="atelier"',
            'id="cc-webgl-canvas"',
            'data-cc-export="glb"',
            'data-cc-export="dxf"',
            'id="engineers-study"',
            'id="visuals"',
            'id="cc-lightbox"',
            '<tp-article-audio data-folio="CC.01"',
            'id="act-puzzle-cc01"',
        ):
            self.assertIn(needle, en_html, f"missing in EN: {needle}")
            self.assertIn(needle, es_html, f"missing in ES: {needle}")
        new_dois = (
            "karnopp1974", "cronin1981", "pacejka1992", "hac1992", "zhao1999",
            "abe2001", "fichera2004", "trachtler2004", "rubin2015",
        )
        for key in new_dois:
            self.assertIn(f'href="#src-{key}"', en_html)
            self.assertIn(f'id="src-{key}"', en_html)
        for p in (SRC / "engineering" / "index.html", SRC / "es-mx" / "engineering" / "index.html"):
            txt = p.read_text(encoding="utf-8")
            self.assertIn('id="cult-classics-eng"', txt)
            self.assertNotIn('Standalone Engineering Monographs', txt)
            self.assertIn('id="all-essays"', txt)
            self.assertLess(txt.index('id="all-essays"'), txt.index('id="cult-classics-eng"'))
        for p in (SRC / "physics" / "index.html", SRC / "es-mx" / "physics" / "index.html"):
            self.assertNotIn('id="cult-classics"', p.read_text(encoding="utf-8"))
        # Magazine pass, phase 2 (2026-11-28): the cover names the three classics in "More to explore" instead.
        for p in (SRC / "index.html", SRC / "es-mx" / "index.html"):
            txt = p.read_text(encoding="utf-8")
            self.assertNotIn('id="cult-classics"', txt)
            for slug in ("golf-gti", "sagrada-familia", "mini-jcw"):
                self.assertIn(f'class="tp-text-link" href="classics/{slug}/"', txt)
        audio_js = (SRC / "modules" / "article-audio.mjs").read_text(encoding="utf-8")
        self.assertIn("GTI_ACT_DEFS", audio_js)
        self.assertIn("sanitizeAudioTrackPath", audio_js)

    def test_gti_images_unique_zero_exif_law8_and_license_hygiene(self):
        import hashlib
        gti_dir = SRC / "images" / "golf-gti"
        jpgs = sorted(gti_dir.glob("*.jpg"))
        self.assertEqual(len(jpgs), 14)
        digests = {hashlib.sha256(p.read_bytes()).hexdigest() for p in jpgs}
        self.assertEqual(len(digests), 14, "duplicate image bytes detected")
        for p in jpgs:
            data = p.read_bytes()
            self.assertEqual(data[:2], b"\xff\xd8", f"{p.name} not JPEG")
            pos = 2
            while pos + 4 <= len(data) and data[pos] == 0xFF:
                marker = data[pos + 1]
                if marker == 0xDA:  # SOS
                    break
                if 0xE1 <= marker <= 0xEF:
                    self.fail(f"{p.name} contains metadata marker 0xFF{marker:02X}")
                seg_len = int.from_bytes(data[pos + 2:pos + 4], "big")
                pos += 2 + seg_len
        for ph in C.PHOTOS:
            self.assertNotIn("by-sa", ph["license"].lower())
        for pl in C.PLATES:
            self.assertIn("conceptual visualization", pl["alt_en"].lower())
            self.assertIn("visualización conceptual", pl["alt_es"].lower())
            self.assertIn("conceptual visualization", pl["caption_en"].lower())
            self.assertIn("visualización conceptual", pl["caption_es"].lower())


if __name__ == "__main__":
    unittest.main()
