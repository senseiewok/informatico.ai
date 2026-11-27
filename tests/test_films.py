#!/usr/bin/env python3
"""Cover films shelf (#films): dormant until data/films.json holds a YouTube ID, link-out only, no embed.

What is pinned here:
- every youtube_id is null or exactly 11 characters of [A-Za-z0-9_-]; a bad ID stops the build;
- the English cover and the es-MX cover both render the section or both omit it;
- posters exist, are 640x360 WebP, at most 120 KB, with no EXIF, XMP or ICC chunk and no JPEG APPn segment;
- with a fixture, each item links to exactly https://www.youtube.com/watch?v=<id> with rel="noopener noreferrer";
- no iframe on either cover, and a film with poster null renders as text only.
"""
from __future__ import annotations

import json
import re
import struct
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(ROOT / "tools"))

import build_longform_folios as B  # noqa: E402

FILMS = json.loads((ROOT / "data" / "films.json").read_text(encoding="utf-8"))
FIXTURE = [
    {"slug": "informatico-intro", "youtube_id": "AbC_dEf-123", "duration": "0:45", "poster": "images/films/informatico-intro.webp"},
    {"slug": "follow-the-light", "youtube_id": "Zz9-Yy8_Xx7", "duration": "4:57", "poster": "images/films/follow-the-light.webp"},
]
POSTER_MAX_BYTES = 120 * 1024


def _webp_chunks(data: bytes) -> list[tuple[bytes, bytes]]:
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise AssertionError("not a RIFF/WEBP file")
    chunks, i = [], 12
    while i + 8 <= len(data):
        fourcc, size = data[i : i + 4], struct.unpack("<I", data[i + 4 : i + 8])[0]
        chunks.append((fourcc, data[i + 8 : i + 8 + size]))
        i += 8 + size + (size & 1)
    return chunks


def _webp_size(chunks: list[tuple[bytes, bytes]]) -> tuple[int, int]:
    for fourcc, body in chunks:
        if fourcc == b"VP8X":
            w = int.from_bytes(body[4:7], "little") + 1
            h = int.from_bytes(body[7:10], "little") + 1
            return w, h
        if fourcc == b"VP8 ":
            assert body[3:6] == b"\x9d\x01\x2a", "VP8 start code missing"
            w, h = struct.unpack("<HH", body[6:10])
            return w & 0x3FFF, h & 0x3FFF
        if fourcc == b"VP8L":
            bits = int.from_bytes(body[1:5], "little")
            return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    raise AssertionError("no image chunk")


def _render_hub_with(films: list[dict]) -> tuple[str, str]:
    """Render both covers in memory with a temporary films.json; nothing under src/ is written."""
    catalog = json.loads((SRC / "data" / "magazine_catalog.json").read_text(encoding="utf-8"))
    saved = B.FILMS_JSON
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "films.json"
        p.write_text(json.dumps(films), encoding="utf-8")
        B.FILMS_JSON = p
        try:
            en = B.render_hub_index(catalog)
            es = B.to_spanish_static(B.render_hub_index(catalog, "es"))
        finally:
            B.FILMS_JSON = saved
    return en, es


class FilmsDataTests(unittest.TestCase):
    def test_films_json_rows(self) -> None:
        self.assertIsInstance(FILMS, list)
        self.assertEqual([f["slug"] for f in FILMS], ["informatico-intro", "follow-the-light"])
        for f in FILMS:
            self.assertEqual(set(f), {"slug", "youtube_id", "duration", "poster"}, f["slug"])
            vid = f["youtube_id"]
            self.assertTrue(vid is None or (isinstance(vid, str) and B.YOUTUBE_ID_RE.fullmatch(vid)), f"{f['slug']}: bad youtube_id {vid!r}")
            self.assertRegex(f["duration"], B.FILM_DURATION_RE)
            self.assertIn(f["slug"], B.FILM_COPY)
            if f["poster"] is not None:
                self.assertRegex(f["poster"], B.FILM_POSTER_RE)

    def test_bad_ids_stop_the_build(self) -> None:
        for bad in ("abc", "AbC_dEf-1234", "AbC dEf-123", "https://youtu.be/AbC_dEf-123", 'AbC"dEf-123', '"><script>a', "AbC_dEf-123\n", "AbC_dEf-12١", "", 12345678901):
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, "youtube_id must"):
                B.render_cover_films_section(".", [dict(FIXTURE[0], youtube_id=bad)])

    def test_bad_durations_stop_the_build(self) -> None:
        for bad in ("４:５７", "٤:٥٧", "4:99", "4:5", "445", ""):
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, "duration must"):
                B.render_cover_films_section(".", [dict(FIXTURE[0], duration=bad)])

    def test_malformed_poster_is_an_error_not_text_only(self) -> None:
        for bad in ("", False, 0, [], "images/films/../x.webp"):
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, "poster must"):
                B.render_cover_films_section(".", [dict(FIXTURE[0], poster=bad)])

    def test_duplicate_slug_or_id_stops_the_build(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate slug"):
            B.render_cover_films_section(".", [FIXTURE[0], dict(FIXTURE[0], youtube_id=None)])
        with self.assertRaisesRegex(ValueError, "duplicate youtube_id"):
            B.render_cover_films_section(".", [FIXTURE[0], dict(FIXTURE[1], youtube_id=FIXTURE[0]["youtube_id"])])

    def test_missing_films_json_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp, self.assertRaises(FileNotFoundError):
            B.load_films(Path(tmp) / "films.json")

    def test_unknown_slug_and_bad_poster_stop_the_build(self) -> None:
        with self.assertRaisesRegex(ValueError, "no cover copy"):
            B.render_cover_films_section(".", [dict(FIXTURE[0], slug="not-a-film")])
        with self.assertRaisesRegex(ValueError, "poster must"):
            B.render_cover_films_section(".", [dict(FIXTURE[0], poster="https://example.com/x.webp")])
        with self.assertRaisesRegex(ValueError, "poster must"):
            B.render_cover_films_section(".", [dict(FIXTURE[0], poster="images/films/missing.webp")])


class FilmPosterTests(unittest.TestCase):
    def test_posters_are_small_clean_webp(self) -> None:
        posters = [f["poster"] for f in FILMS if f["poster"]]
        self.assertTrue(posters)
        for rel in posters:
            with self.subTest(poster=rel):
                path = SRC / rel
                self.assertTrue(path.is_file(), rel)
                data = path.read_bytes()
                self.assertLessEqual(len(data), POSTER_MAX_BYTES, rel)
                self.assertNotEqual(data[:2], b"\xff\xd8", f"{rel}: JPEG bytes in a .webp")
                chunks = _webp_chunks(data)
                kinds = {c for c, _ in chunks}
                self.assertLessEqual(kinds, {b"VP8 ", b"VP8L", b"VP8X", b"ALPH"}, f"{rel}: extra chunks {kinds}")
                for c, body in chunks:
                    if c == b"VP8X":
                        self.assertEqual(body[0] & 0b0010_1100, 0, f"{rel}: VP8X flags ICC/EXIF/XMP")
                for marker in (b"Exif", b"<x:xmpmeta", b"http://ns.adobe.com/xap/"):
                    self.assertNotIn(marker, data, f"{rel}: {marker!r}")
                self.assertIsNone(re.search(rb"\xff[\xe0-\xef]..(JFIF|Exif|http)", data), f"{rel}: JPEG APPn segment")
                self.assertEqual(_webp_size(chunks), (640, 360), rel)

    def test_no_stray_files_in_films_folder(self) -> None:
        listed = {f["poster"] for f in FILMS if f["poster"]}
        on_disk = {p.relative_to(SRC).as_posix() for p in (SRC / "images" / "films").glob("*")}
        self.assertEqual(on_disk, listed)


class FilmsSectionTests(unittest.TestCase):
    def test_fixture_hrefs_rel_and_no_iframe(self) -> None:
        html = B.render_cover_films_section(".", FIXTURE)
        hrefs = re.findall(r'<a class="tp-film-link" href="([^"]+)" rel="([^"]+)"', html)
        self.assertEqual(
            hrefs,
            [
                ("https://www.youtube.com/watch?v=AbC_dEf-123", "noopener noreferrer"),
                ("https://www.youtube.com/watch?v=Zz9-Yy8_Xx7", "noopener noreferrer"),
            ],
        )
        self.assertEqual(
            re.findall(r'href="([^"]+)"', html),
            [
                "https://www.youtube.com/watch?v=AbC_dEf-123",
                "https://www.youtube.com/watch?v=Zz9-Yy8_Xx7",
                "https://creativecommons.org/licenses/by/4.0/",
            ],
        )
        self.assertNotIn("<iframe", html.lower())
        self.assertNotIn("youtube-nocookie", html)
        self.assertEqual(html.count('alt=""'), 2)
        self.assertEqual(len(re.findall(r'<img class="tp-film-poster" src="images/films/[a-z-]+\.webp\?v=[0-9a-f]{8}" width="640" height="360"', html)), 2)
        self.assertEqual(html.count("opens youtube.com</span>"), 2)
        self.assertIn(">Informatico: intro · 0:45<", html)
        self.assertIn(">Follow the Light · 4:57<", html)
        for copy in B.FILM_COPY.values():
            self.assertIn(B.esc(copy["note_en"]), html)

    def test_null_ids_are_skipped_and_all_null_drops_section(self) -> None:
        self.assertEqual(B.render_cover_films_section(".", [dict(f, youtube_id=None) for f in FIXTURE]), "")
        one = B.render_cover_films_section(".", [FIXTURE[0], dict(FIXTURE[1], youtube_id=None)])
        self.assertEqual(one.count('class="tp-film-link"'), 1)
        self.assertNotIn("follow-the-light", one)

    def test_lung_model_credit_renders_whenever_its_poster_is_shown(self) -> None:
        credit_en = (
            '<p class="tp-film-credit"><span data-en="Lung model: Human Reference Atlas (HuBMAP),"'
        )
        cc_link = '<a href="https://creativecommons.org/licenses/by/4.0/" rel="noopener noreferrer license">CC BY 4.0</a>.</p>'
        en, es = _render_hub_with(FIXTURE)
        for rel, page, words in (
            ("en", en, ">Lung model: Human Reference Atlas (HuBMAP),</span> "),
            ("es", es, ">Modelo de pulmón: Human Reference Atlas (HuBMAP),</span> "),
        ):
            item = re.search(r'<li class="tp-film" data-film="follow-the-light">.*?</li>', page, re.S)
            self.assertIsNotNone(item, rel)
            item_html = item.group(0)
            self.assertIn('<img class="tp-film-poster" src="', item_html, rel)
            self.assertIn(credit_en, item_html, rel)
            self.assertIn(words + cc_link, item_html, rel)
            self.assertEqual(page.count('class="tp-film-credit"'), 1, rel)
        # The credit belongs to the poster: a text-only card carries no credit, and the intro has none.
        text_only = B.render_cover_films_section(".", [FIXTURE[0], dict(FIXTURE[1], poster=None)])
        self.assertNotIn("tp-film-credit", text_only)
        self.assertNotIn("Human Reference Atlas", text_only)

    def test_spanish_cover_says_follow_the_light_narration_is_english(self) -> None:
        en, es = _render_hub_with(FIXTURE)
        ext = dict(re.findall(r'data-film="([a-z-]+)">.*?<span class="tp-film-ext"[^>]*>([^<]*)</span>', es, re.S))
        self.assertEqual(ext, {"informatico-intro": "abre youtube.com", "follow-the-light": "abre youtube.com (narración en inglés)"})
        self.assertEqual(re.findall(r'<span class="tp-film-ext"[^>]*>([^<]*)</span>', en), ["opens youtube.com"] * 2)

    def test_null_poster_renders_text_only(self) -> None:
        html = B.render_cover_films_section(".", [dict(FIXTURE[1], poster=None)])
        self.assertNotIn("<img", html)
        self.assertIn("tp-film tp-film-textonly", html)
        self.assertIn("https://www.youtube.com/watch?v=Zz9-Yy8_Xx7", html)

    def test_en_and_es_covers_render_together_with_fixture(self) -> None:
        en, es = _render_hub_with(FIXTURE)
        for rel, page in (("en", en), ("es", es)):
            self.assertEqual(page.count('id="films"'), 1, rel)
            self.assertLess(page.index('id="tp-featured-edition-desk"'), page.index('id="films"'), rel)
            self.assertLess(page.index('id="films"'), page.index('id="pillar-engineering"'), rel)
            self.assertNotIn("<iframe", page.lower(), rel)
            self.assertEqual(
                re.findall(r'class="tp-film-link" href="([^"]+)"', page),
                ["https://www.youtube.com/watch?v=AbC_dEf-123", "https://www.youtube.com/watch?v=Zz9-Yy8_Xx7"],
                rel,
            )
        self.assertIn('src="images/films/informatico-intro.webp?v=', en)
        self.assertIn('src="../images/films/informatico-intro.webp?v=', es)
        self.assertIn(">Películas<", es)
        self.assertIn(">abre youtube.com<", es)
        self.assertIn(B.esc(B.FILM_COPY["follow-the-light"]["note_es"]), es)
        for p in re.findall(r'src="\.\./(images/films/[^"?]+)', es):
            self.assertTrue((SRC / p).is_file(), p)

    def test_en_and_es_covers_omit_together_when_dormant(self) -> None:
        en, es = _render_hub_with([dict(f, youtube_id=None) for f in FIXTURE])
        for rel, page in (("en", en), ("es", es)):
            self.assertNotIn('id="films"', page, rel)
            self.assertNotIn("tp-film", page, rel)

    def test_built_covers_match_films_json(self) -> None:
        """src/index.html and src/es-mx/index.html agree with each other and with data/films.json."""
        live = [f for f in FILMS if f["youtube_id"]]
        for rel in ("index.html", "es-mx/index.html"):
            html = (SRC / rel).read_text(encoding="utf-8")
            self.assertNotIn("<iframe", html.lower(), rel)
            self.assertEqual(html.count('id="films"'), 1 if live else 0, rel)
            self.assertEqual(
                re.findall(r'class="tp-film-link" href="([^"]+)"', html),
                [f"https://www.youtube.com/watch?v={f['youtube_id']}" for f in live],
                rel,
            )

    def test_csp_keeps_frames_off(self) -> None:
        ht = (ROOT / "deploy" / "htaccess.txt").read_text(encoding="utf-8")
        self.assertIn("frame-src 'none'", ht)
        self.assertNotIn("youtube", ht.lower())


if __name__ == "__main__":
    unittest.main()
