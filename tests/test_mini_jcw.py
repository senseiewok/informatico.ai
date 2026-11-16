"""CC.03 (MINI -> F56 John Cooper Works Hot Chili cult classic): grounding, privacy, North America, CSP and accessibility guards."""
from __future__ import annotations

import re
import subprocess
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
sys.path.insert(0, str(ROOT / "tools"))

from folios.classics import cc03 as C  # noqa: E402

EN = SRC / "classics" / C.SLUG / "index.html"
ES = SRC / "es-mx" / "classics" / C.SLUG / "index.html"
CSS = SRC / "cult-classics.css"
JS = SRC / "modules" / "cult-classics.mjs"
PHOTO = SRC / C.EGG["image"]
EGG_ITEMS = (C.EGG, C.EGG_SKETCH)


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


def jpeg_markers(data: bytes) -> list[int]:
    """Walk JPEG header markers up to SOS (0xFFDA) or EOI (0xFFD9)."""
    markers: list[int] = []
    pos = 2
    n = len(data)
    while pos + 1 < n:
        if data[pos] != 0xFF:
            pos += 1
            continue
        while pos < n and data[pos] == 0xFF:
            pos += 1
        if pos >= n:
            break
        marker = data[pos]
        pos += 1
        if marker == 0x00:
            continue
        markers.append(marker)
        if marker in (0xD9, 0xDA):
            break
        if 0xD0 <= marker <= 0xD8 or marker == 0x01:
            continue
        if pos + 2 > n:
            break
        seg_len = int.from_bytes(data[pos:pos + 2], "big")
        pos += seg_len
    return markers


class MiniJcwPages(unittest.TestCase):
    def test_both_languages_exist_with_their_own_language(self) -> None:
        self.assertIn('<html lang="en">', EN.read_text(encoding="utf-8"))
        es = ES.read_text(encoding="utf-8")
        self.assertIn('<html lang="es-MX">', es)
        self.assertIn("Ruedas en las esquinas", es)
        for value in C.VALUE_ES.values():
            self.assertIn(value, es, f"spec-plate value left in English on Spanish page: {value!r}")

    def test_no_inline_script_style_or_style_attribute(self) -> None:
        sys.path.insert(0, str(ROOT / "deploy"))
        from check_upload import _InlineScriptChecker  # noqa: E402

        for page in (EN, ES):
            v = parse(page)
            self.assertNotIn("style", v.tags, page)
            self.assertFalse(any(k == "style" for _t, k, _v in v.attrs), f"{page}: style attribute")
            checker = _InlineScriptChecker()
            checker.feed(page.read_text(encoding="utf-8"))
            self.assertFalse(checker.has_executable_inline_script, f"{page}: executable inline script")

    def test_no_unearned_superlatives_or_ownership(self) -> None:
        for page in (EN, ES):
            visible = " ".join(parse(page).text).lower()
            for phrase in C.BANNED:
                self.assertNotIn(phrase.lower(), visible, f"{page}: banned phrase {phrase!r}")

    def test_human_tribute_and_north_america_differences_present(self) -> None:
        en_html = EN.read_text(encoding="utf-8")
        es_html = ES.read_text(encoding="utf-8")
        self.assertIn('class="cc-honor-roll"', en_html)
        self.assertIn("Alec Issigonis", en_html)
        self.assertIn("Pat Moss", en_html)
        self.assertIn("Frank Stephenson", en_html)
        self.assertIn("Luis A. Perocarpi", en_html)
        self.assertIn('id="north-america-spec"', en_html)
        self.assertIn('id="north-america-spec"', es_html)
        for token in ("228 hp", "231 PS", "FMVSS 108", "Hot Chili", "Iconic", "236 lb-ft", "280 lb-ft"):
            self.assertIn(token, en_html, token)
            self.assertIn(token, es_html, token)
        self.assertIn('id="visuals"', en_html)
        self.assertIn('id="cc-lightbox"', en_html)
        self.assertEqual(en_html.count("data-cc-open-media="), 16)  # 8 inline/easter-egg + 8 in #visuals

    def test_easter_egg_captions_privacy_and_conceptual_disclosure(self) -> None:
        owner = re.compile(r"\b(my|mine|our|owner|owned|mi|mío|nuestro|dueño)\b", re.I)
        rating = re.compile(r"\d+\s?(?:hp|PS|bhp|Nm|lb-ft|kW)", re.I)
        for idx, item in enumerate(EGG_ITEMS):
            for key in ("caption_en", "caption_es", "alt_en", "alt_es"):
                self.assertIsNone(owner.search(item[key]), f"EGG[{idx}].{key} leaks ownership")
            for key in ("caption_en", "caption_es"):
                self.assertIsNone(rating.search(item[key]), f"EGG[{idx}].{key} states power/torque rating")

        for page in (EN, ES):
            self.assertIn('<a href="https://www.brembo.com/" rel="noopener noreferrer">Brembo</a>', page.read_text(encoding="utf-8"))

        # Law 8 explicit conceptual disclosure in both caption and alt (EN + ES-MX)
        for item in (C.EGG_SKETCH, C.MEDIA[0]):
            self.assertIn("Conceptual visualization", item["caption_en"])
            self.assertIn("Conceptual visualization", item["alt_en"])
            self.assertIn("Visualización conceptual", item["caption_es"])
            self.assertIn("Visualización conceptual", item["alt_es"])

        self.assertFalse((SRC / "images" / "mini-jcw" / "mini-jcw-rear-union-jack.jpg").exists())
        self.assertFalse((SRC / "images" / "mini-jcw" / "mini-jcw-sketched-track.jpg").exists())
        expected_files = sorted(Path(item["image"]).name for item in C.MEDIA)
        self.assertEqual(sorted(p.name for p in PHOTO.parent.iterdir()), expected_files)

    def test_photos_carry_zero_metadata_across_entire_file(self) -> None:
        forbidden_markers = set(range(0xE1, 0xF0)) | {0xFE}  # APP1..APP15, COM
        self.assertEqual(len(C.MEDIA), 8)
        for item in C.MEDIA:
            photo = SRC / item["image"]
            self.assertTrue(photo.is_file(), f"Missing image: {photo}")
            data = photo.read_bytes()
            self.assertTrue(data.startswith(b"\xff\xd8"), f"{photo.name}: not a JPEG")
            seen = set(jpeg_markers(data))
            self.assertFalse(seen & forbidden_markers, f"{photo.name}: unexpected JPEG markers {seen & forbidden_markers}")
            for sig in (b"Exif", b"http://ns.adobe.com/xap", b"ICC_PROFILE", b"GPS", b"8BIM"):
                self.assertNotIn(sig, data, f"{photo.name}: binary payload contains {sig!r}")

    def test_lap_arithmetic_and_brands_hatch_speeds(self) -> None:
        secs = {rid: s for rid, _era, _car, _y, _ts, s, *_rest in C.LAPS}
        self.assertEqual(round(secs["se7en-s"] - secs["jcw-qual"], 2), 8.65)
        self.assertIn("8.65 seconds", C.LAPS_TEXT["read_en"])
        self.assertEqual(round(secs["se7en"] - secs["miglia"], 2), 4.27)
        self.assertIn("4.27 seconds", C.LAPS_TEXT["read_en"])

        en_html = EN.read_text(encoding="utf-8")
        for _rid, _era, _car, _y, ts, s, *_rest in C.LAPS:
            m, rest = ts.split(":")
            self.assertAlmostEqual(int(m) * 60 + float(rest), s, places=3, msg=ts)
            self.assertIn(f">{ts}<", en_html)

    def test_every_stamp_resolves_and_every_source_is_used(self) -> None:
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

    def test_papers_are_framed_as_general_mechanisms(self) -> None:
        for block in (C.LOAD_SCIENCE["science_en"], C.BRAKE_SCIENCE["science_en"], C.INDUCTION["note_en"]):
            self.assertRegex(block, r"not a Mini|None of those papers tested|Neither paper tested", block[:80])
        self.assertIn("Same circuit, not the same day or class rules", C.LAPS_TEXT["caveat_en"])

    def test_motion_is_pausable_and_static_when_reduced(self) -> None:
        txt = EN.read_text(encoding="utf-8")
        self.assertIn('class="cc-parade" aria-hidden="true"', txt)
        self.assertIn('class="cc-track cc-track-sketch" viewBox="0 0 1600 1000" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false"', txt)
        js = JS.read_text(encoding="utf-8")
        self.assertIn("passive: true", js)
        self.assertIn('reduceMotion.matches || document.documentElement.classList.contains("cc-paused")', js)
        self.assertIn("data-cc-pause", txt)
        css = CSS.read_text(encoding="utf-8")
        self.assertIn("@media (prefers-reduced-motion: reduce)", css)
        self.assertIn("html.cc-paused .cc-lane", css)
        self.assertIn("@media (forced-colors: active)", css)
        self.assertIn("@media print", css)

    def test_controls_and_trusted_types_csp_rules(self) -> None:
        txt = EN.read_text(encoding="utf-8")
        for rid in ("cc-ay-range", "cc-brake-range"):
            self.assertIn(f'<label class="cc-range-label" for="{rid}">', txt)
            self.assertRegex(txt, rf'<input id="{rid}" class="cc-range" type="range"[^>]*aria-valuetext=')
        self.assertIn('aria-controls="cc-egg-panel"', txt)
        self.assertIn('aria-live="polite"', txt)
        js = JS.read_text(encoding="utf-8")
        for bad in ("innerHTML", "outerHTML", "insertAdjacentHTML", ".style.", "eval(", "new Function"):
            self.assertNotIn(bad, js, bad)
        self.assertIn("SAFE_MEDIA_SRC_RE", js)

    def test_mechanics_lab_verifier_passes_and_every_knockout_fails(self) -> None:
        verify = ROOT / "skills" / "classics" / "cc03" / "verify_cc03_mechanics.py"
        self.assertTrue((verify.parent / "SKILL.md").is_file())
        ok = subprocess.run([sys.executable, "-X", "utf8", str(verify)], capture_output=True, text=True, encoding="utf-8", timeout=60)
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertIn('"status": "PASS"', ok.stdout)
        for variant in ("", "=single-disc", "=config", "=unit-kmh", "=hp-ps"):
            bad = subprocess.run(
                [sys.executable, "-X", "utf8", str(verify), "--planted-defect" + variant],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=60,
            )
            self.assertNotEqual(bad.returncode, 0, f"knockout {variant or 'load-sign'} passed")

    def test_lab_labels_model_values_and_cites_its_physics(self) -> None:
        txt = EN.read_text(encoding="utf-8")
        self.assertIn('id="part-5"', txt)
        self.assertIn("(MODEL)", txt)
        for key in ("ricco2020", "adamowicz2011", "hu2016", "hu2017", "chiong2016", "kakalis2008"):
            self.assertIn(f'href="#src-{key}"', txt)
        self.assertEqual(txt.count('data-lap-kmh="'), 4)  # only rows with stated 1.208 mi circuit length
        self.assertEqual(txt.count("cc-ghost-nolen"), 8)  # 4 hollow circuit dots + 4 hollow legend keys

    def test_both_languages_print_the_same_figures(self) -> None:
        """Every number with a unit and every lap time appears in both languages."""
        unit = re.compile(r"\b\d[\d,.]*\s?(?:PS|hp|bhp|kW|Nm|lb-ft|km/h|mph|mi|kg|mm|°C|kJ)\b|\b0:\d\d\.\d\d\d\b")

        def figures(page: Path) -> set[str]:
            html = page.read_text(encoding="utf-8")
            body = html[html.index('<article class="cc-feature"'):html.index('id="sources"')]
            text = " ".join(parse_text(body))
            return {re.sub(r"\s", "", m) for m in unit.findall(text)}

        en, es = figures(EN), figures(ES)
        self.assertEqual(en - es, set(), f"figures only in English: {en - es}")
        self.assertEqual(es - en, set(), f"figures only in Spanish: {es - en}")

    def test_sitemap_and_llms_list_the_feature(self) -> None:
        xml = (SRC / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn(f"<loc>https://informatico.ai/classics/{C.SLUG}/</loc>", xml)
        self.assertIn(f"<loc>https://informatico.ai/es-mx/classics/{C.SLUG}/</loc>", xml)
        self.assertIn(f"https://informatico.ai/classics/{C.SLUG}/", (SRC / "llms.txt").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
