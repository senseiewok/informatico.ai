"""CC.02 (La Sagrada Família masterpiece): grounding, privacy, CSP, conceptual disclosure, WebGL2/CAD, and verifier."""
from __future__ import annotations

import hashlib
import json
import re
import struct
import subprocess
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
sys.path.insert(0, str(ROOT / "tools"))

from folios.classics import cc02 as C  # noqa: E402

EN = SRC / "classics" / C.SLUG / "index.html"
ES = SRC / "es-mx" / "classics" / C.SLUG / "index.html"
CSS = SRC / "sagrada-familia.css"
JS = SRC / "modules" / "sagrada-familia.mjs"
PLATE = SRC / "plates" / "cc02.png"
IMG_DIR = SRC / "images" / "sagrada-familia"


class _Visible(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.text: list[str] = []
        self.attrs: list[tuple[str, str, str]] = []
        self.tags: list[str] = []
        self.puzzle_payloads: list[str] = []
        self._skip = 0
        self._in_puzzle = False
        self._puzzle_buf: list[str] = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        attr_map = dict(attrs)
        if tag == "script" and attr_map.get("class") == "tp-puzzle-payload":
            self._in_puzzle = True
            self._puzzle_buf = []
        if tag in ("script", "style"):
            self._skip += 1
        for k, v in attrs:
            self.attrs.append((tag, k, v or ""))

    def handle_endtag(self, tag):
        if tag == "script" and self._in_puzzle:
            self.puzzle_payloads.append("".join(self._puzzle_buf))
            self._in_puzzle = False
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._in_puzzle:
            self._puzzle_buf.append(data)
        elif not self._skip:
            self.text.append(data)


def _parse(path: Path) -> _Visible:
    v = _Visible()
    v.feed(path.read_text(encoding="utf-8"))
    return v


class SagradaMasterpieceTests(unittest.TestCase):
    def test_both_languages_exist_with_proper_translation(self) -> None:
        self.assertIn('<html lang="en">', EN.read_text(encoding="utf-8"))
        es_html = ES.read_text(encoding="utf-8")
        self.assertIn('<html lang="es-MX">', es_html)
        self.assertIn("Un bosque de piedra, ocho hitos", es_html)
        self.assertNotIn("jugada", es_html.lower())
        for val_es in C.VALUE_ES.values():
            self.assertIn(val_es, es_html, f"missing translated plate value: {val_es!r}")

    def test_strict_csp_no_inline_script_or_style(self) -> None:
        sys.path.insert(0, str(ROOT / "deploy"))
        from check_upload import _InlineScriptChecker  # noqa: E402

        for page in (EN, ES):
            v = _parse(page)
            self.assertNotIn("style", v.tags, page)
            self.assertFalse(any(k == "style" for _t, k, _v in v.attrs), f"{page}: inline style attribute")
            checker = _InlineScriptChecker()
            checker.feed(page.read_text(encoding="utf-8"))
            self.assertFalse(checker.has_executable_inline_script, f"{page}: executable inline script")

        js = JS.read_text(encoding="utf-8")
        for bad in ("innerHTML", "outerHTML", "insertAdjacentHTML", ".style.", "eval(", "new Function"):
            self.assertNotIn(bad, js, f"CSP violation in JS: {bad}")

    def test_no_banned_phrases_or_uncited_sources(self) -> None:
        for page in (EN, ES):
            visible = " ".join(_parse(page).text).lower()
            for phrase in C.BANNED:
                self.assertNotIn(phrase.lower(), visible, f"{page}: banned phrase {phrase!r}")

        txt = EN.read_text(encoding="utf-8")
        self.assertEqual(len(C.SOURCES), 29)
        used = set(re.findall(r'href="#src-([a-z0-9-]+)"', txt))
        listed = set(re.findall(r'<li id="src-([a-z0-9-]+)"', txt))
        self.assertEqual(listed, set(C.SOURCES))
        self.assertTrue(used <= listed, used - listed)
        self.assertEqual(used, listed, f"listed but uncited sources: {listed - used}")
        legacy_404 = ("/en/architecture", "/en/the-columns", "/en/towers", "/en/tower-of-jesus-christ")
        for key, src in C.SOURCES.items():
            self.assertIn(src["kind"], C.KIND_LABEL, key)
            self.assertTrue(src["url"].startswith("https://"), key)
            self.assertNotIn("BY-SA", src["label"].upper(), f"ShareAlike license conflict in {key}")
            for slug in legacy_404:
                self.assertNotIn(slug, src["url"], f"stale 404 slug in {key}")
            if src["kind"] == "paper":
                self.assertTrue(src["url"].startswith("https://doi.org/10."), key)
        for slug in legacy_404:
            self.assertNotIn(f"sagradafamilia.org{slug}", txt)

    def test_conceptual_plates_zero_metadata_and_labeled(self) -> None:
        all_media = [*C.PHOTOS, *C.PLATES]
        self.assertEqual(len(all_media), 10)
        expected_names = sorted(Path(p["image"]).name for p in all_media)
        actual_names = sorted(p.name for p in IMG_DIR.iterdir())
        self.assertEqual(actual_names, expected_names)

        digests: set[str] = set()
        for media_info in all_media:
            path = SRC / media_info["image"]
            raw = path.read_bytes()
            self.assertTrue(raw.startswith(b"\xff\xd8"), f"{path.name}: not a JPEG")
            for marker in (b"Exif\x00\x00", b"http://ns.adobe.com/xap", b"ICC_PROFILE", b"GPS"):
                self.assertNotIn(marker, raw[:65536], f"{path.name}: contains metadata {marker!r}")
            digests.add(hashlib.sha256(raw).hexdigest())

        self.assertEqual(len(digests), 10, "duplicate SHA-256 detected among CC.02 visual assets")

        for plate_info in C.PLATES:
            self.assertIn("Conceptual visualization", plate_info["alt_en"])
            self.assertIn("Conceptual visualization", plate_info["caption_en"])
            self.assertIn("Visualización conceptual", plate_info["alt_es"])
            self.assertIn("Visualización conceptual", plate_info["caption_es"])

        for photo_info in C.PHOTOS:
            self.assertNotIn("BY-SA", photo_info["license"].upper(), photo_info["id"])
            self.assertTrue(
                any(C.SOURCES[k]["url"].startswith("https://commons.wikimedia.org/wiki/File:") for k in photo_info["src"]),
                f"missing Commons File source for {photo_info['id']}",
            )

    def test_share_plate_png_dimensions(self) -> None:
        data = PLATE.read_bytes()
        self.assertTrue(data.startswith(b"\x89PNG\r\n\x1a\n"))
        width, height = struct.unpack(">II", data[16:24])
        self.assertEqual((width, height), (1200, 630))

    def test_controls_crossword_audio_and_accessibility(self) -> None:
        txt = EN.read_text(encoding="utf-8")
        self.assertIn('data-sf-pause', txt)
        self.assertIn('<tp-article-audio data-folio="CC.02"', txt)
        self.assertNotIn("data-audio-src", txt)
        self.assertIn('id="act-puzzle-cc02"', txt)
        self.assertIn('data-sf-export="glb"', txt)
        self.assertIn('data-sf-export="dxf"', txt)
        self.assertIn('data-sf-relay', txt)
        self.assertIn('data-sf-shard', txt)
        self.assertIn('data-sf-loupe', txt)
        self.assertIn('data-sf-sankey', txt)
        self.assertIn('data-sf-radar', txt)
        self.assertIn('data-sf-gallery', txt)
        self.assertIn('<dialog class="sf-lightbox" id="sf-lightbox"', txt)
        es_txt = ES.read_text(encoding="utf-8")
        for attr in ('data-sf-loupe', 'data-sf-sankey', 'data-sf-radar', 'data-sf-gallery', 'id="sf-lightbox"'):
            self.assertIn(attr, es_txt)
        for i in range(5):
            self.assertIn(f'data-sf-gen="{i}"', txt)
            self.assertIn(f'data-sf-relay-card="{i}"', txt)
        self.assertIn('id="sf-webgl-canvas"', txt)
        for rid in (
            "sf-lantern-range", "sf-catenary-a-range", "sf-col-z-range",
            "sf-caliper-range", "sf-fpt-range", "sf-wind-range", "sf-solar-range",
        ):
            self.assertIn(f'for="{rid}"', txt)
            self.assertRegex(txt, rf'<input id="{rid}" class="sf-range" type="range"[^>]*aria-valuetext=')

        parsed_en = _parse(EN)
        self.assertTrue(parsed_en.puzzle_payloads, "missing cc02 crossword payload")
        payload = json.loads(parsed_en.puzzle_payloads[0])
        self.assertEqual(len(payload["en"]["grid"]), 10)
        self.assertEqual(len(payload["es"]["grid"]), 10)

        css = CSS.read_text(encoding="utf-8")
        self.assertIn("@media (prefers-reduced-motion: reduce)", css)
        self.assertIn("@media (forced-colors: active)", css)
        self.assertIn("@media print", css)

    def test_verifier_passes_and_five_knockouts_fail(self) -> None:
        verify = ROOT / "skills" / "classics" / "cc02" / "verify_cc02_sagrada.py"
        self.assertTrue((verify.parent / "SKILL.md").is_file())
        ok = subprocess.run([sys.executable, "-X", "utf8", str(verify)], capture_output=True, text=True, encoding="utf-8", timeout=60)
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertIn('"status": "PASS"', ok.stdout)
        for variant in ("", "=parabola-catenary", "=twist-pinch", "=unprestressed-wind", "=shard-freeform"):
            bad = subprocess.run(
                [sys.executable, "-X", "utf8", str(verify), "--planted-defect" + variant],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=60,
            )
            self.assertNotEqual(bad.returncode, 0, f"knockout {variant or 'non-tangent-ruling'} unexpectedly passed")

    def test_site_hub_arch_rack_sitemap_and_llms_integration(self) -> None:
        xml = (SRC / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn(f"<loc>https://informatico.ai/classics/{C.SLUG}/</loc>", xml)
        self.assertIn(f"<loc>https://informatico.ai/es-mx/classics/{C.SLUG}/</loc>", xml)
        self.assertIn(f"https://informatico.ai/classics/{C.SLUG}/", (SRC / "llms.txt").read_text(encoding="utf-8"))
        arch = (SRC / "architecture" / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="../classics/sagrada-familia/"', arch)
        self.assertIn('class="tp-rack-thumb tp-rack-thumb-series"', arch)
        hub = (SRC / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="classics/sagrada-familia/"', hub)


if __name__ == "__main__":
    unittest.main()
