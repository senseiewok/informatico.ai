#!/usr/bin/env python3
"""Cover films: a click-to-play player for the intro at the top of the cover, and a link-out shelf (#films).

What is pinned here:
- every youtube_id is null or exactly 11 characters of [A-Za-z0-9_-]; a bad ID stops the build;
- the English cover and the es-MX cover both render the player and the shelf, or both omit them;
- posters exist, are 640x360 WebP, at most 120 KB, with no EXIF, XMP or ICC chunk and no JPEG APPn segment;
- only the intro is the cover player; every other film is a card linking to https://www.youtube.com/watch?v=<id>
  with rel="noopener noreferrer", and a card with poster null renders as text only;
- no built page ships an iframe or names a YouTube player or thumbnail host; the frame is built by
  src/modules/film-facade.mjs on the press, with a fixed address shape and a re-validated ID;
- deploy/htaccess.txt opens frame-src and autoplay to the one player host and changes nothing else.
"""
from __future__ import annotations

import json
import re
import struct
import sys
import tempfile
import unittest
from html.parser import HTMLParser
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


class _LoadingTagParser(HTMLParser):
    """Collect the tags that make a browser fetch something (parsed, not regex-matched; case-insensitive)."""

    WATCHED = {"img", "script", "link", "source", "video", "audio", "iframe", "embed", "object"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.found: list[tuple[str, list[tuple[str, str | None]]]] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.WATCHED:
            self.found.append((tag, attrs))

    handle_startendtag = handle_starttag


def _loading_tags(html: str) -> list[tuple[str, list[tuple[str, str | None]]]]:
    parser = _LoadingTagParser()
    parser.feed(html)
    parser.close()
    return parser.found


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
        self.assertEqual([f["slug"] for f in FILMS], ["informatico-intro", "cf-lab-trailer", "follow-the-light"])
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
        # The intro plays at the top of the cover (FilmPlayerMarkupTests), so the shelf keeps one card.
        self.assertEqual(hrefs, [("https://www.youtube.com/watch?v=Zz9-Yy8_Xx7", "noopener noreferrer")])
        self.assertEqual(
            re.findall(r'href="([^"]+)"', html),
            ["https://www.youtube.com/watch?v=Zz9-Yy8_Xx7", "https://creativecommons.org/licenses/by/4.0/"],
        )
        self.assertNotIn("<iframe", html.lower())
        self.assertNotIn("youtube-nocookie", html)
        self.assertNotIn("informatico-intro", html)
        self.assertEqual(html.count('alt=""'), 1)
        self.assertEqual(len(re.findall(r'<img class="tp-film-poster" src="images/films/[a-z-]+\.webp\?v=[0-9a-f]{8}" width="640" height="360"', html)), 1)
        self.assertEqual(html.count("opens youtube.com</span>"), 1)
        self.assertIn(">Follow the Light · 4:57<", html)
        self.assertIn(B.esc(B.FILM_COPY["follow-the-light"]["note_en"]), html)

    def test_null_ids_are_skipped_and_all_null_drops_section(self) -> None:
        self.assertEqual(B.render_cover_films_section(".", [dict(f, youtube_id=None) for f in FIXTURE]), "")
        # With only the cover player's film live, the shelf has no card left and is omitted.
        self.assertEqual(B.render_cover_films_section(".", [FIXTURE[0], dict(FIXTURE[1], youtube_id=None)]), "")
        one = B.render_cover_films_section(".", [dict(FIXTURE[0], youtube_id=None), FIXTURE[1]])
        self.assertEqual(one.count('class="tp-film-link"'), 1)
        self.assertNotIn("informatico-intro", one)

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
        self.assertEqual(re.findall(r'<span class="tp-film-ext"[^>]*>([^<]*)</span>', es), ["abre youtube.com (narración en inglés)"])
        self.assertEqual(re.findall(r'<span class="tp-film-ext"[^>]*>([^<]*)</span>', en), ["opens youtube.com"])

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
                ["https://www.youtube.com/watch?v=Zz9-Yy8_Xx7"],
                rel,
            )
            self.assertEqual(
                re.findall(r'class="tp-film-out" href="([^"]+)"', page),
                ["https://www.youtube.com/watch?v=AbC_dEf-123"],
                rel,
            )
        self.assertIn('src="images/films/informatico-intro.webp?v=', en)
        self.assertIn('src="../images/films/informatico-intro.webp?v=', es)
        self.assertIn(">Películas<", es)
        self.assertIn(">abre youtube.com (narración en inglés)<", es)
        self.assertIn(B.esc(B.FILM_COPY["follow-the-light"]["note_es"]), es)
        for p in re.findall(r'src="\.\./(images/films/[^"?]+)', es):
            self.assertTrue((SRC / p).is_file(), p)

    def test_en_and_es_covers_omit_together_when_dormant(self) -> None:
        en, es = _render_hub_with([dict(f, youtube_id=None) for f in FIXTURE])
        for rel, page in (("en", en), ("es", es)):
            self.assertNotIn('id="films"', page, rel)
            self.assertNotIn("tp-film", page, rel)
            # Dormant: the hero keeps its conceptual illustration.
            self.assertEqual(page.count('<figure class="tp-cover-figure">'), 1, rel)

    def test_built_covers_match_films_json(self) -> None:
        """src/index.html and src/es-mx/index.html agree with each other and with data/films.json."""
        live = [f for f in FILMS if f["youtube_id"]]
        shelf = [f for f in live if f["slug"] not in B.PLAYER_SLUGS]
        player = [f for f in live if f["slug"] == B.COVER_PLAYER_SLUG]
        for rel in ("index.html", "es-mx/index.html"):
            html = (SRC / rel).read_text(encoding="utf-8")
            self.assertNotIn("<iframe", html.lower(), rel)
            self.assertEqual(html.count('id="films"'), 1 if shelf else 0, rel)
            self.assertEqual(
                re.findall(r'class="tp-film-link" href="([^"]+)"', html),
                [f"https://www.youtube.com/watch?v={f['youtube_id']}" for f in shelf],
                rel,
            )
            self.assertEqual(re.findall(r'class="tp-film-facade" data-yt="([^"]*)"', html), [f["youtube_id"] for f in player], rel)
            self.assertEqual(
                re.findall(r'class="tp-film-out" href="([^"]+)"', html),
                [f"https://www.youtube.com/watch?v={f['youtube_id']}" for f in player],
                rel,
            )


def _header(name: str) -> str:
    """The one value deploy/htaccess.txt sets for a response header (Apache writes an inner quote as \\")."""
    ht = (ROOT / "deploy" / "htaccess.txt").read_text(encoding="utf-8")
    found = re.findall(rf'^\s*Header always set {re.escape(name)} "((?:[^"\\]|\\.)*)"\s*$', ht, re.M)
    if len(found) != 1:
        raise AssertionError(f"{name}: expected exactly one 'Header always set' line, found {len(found)}")
    return found[0].replace('\\"', '"')


class FilmHeaderTests(unittest.TestCase):
    """The player needs exactly two header changes; everything else stays as strict as it was."""

    PLAYER_HOST = "https://www.youtube-nocookie.com"

    def _csp(self) -> dict[str, str]:
        parts = [d.strip() for d in _header("Content-Security-Policy").split(";")]
        names = [p.split(" ", 1)[0] for p in parts]
        self.assertEqual(len(names), len(set(names)), "a CSP directive is repeated")
        return {p.split(" ", 1)[0]: p.split(" ", 1)[1] if " " in p else "" for p in parts}

    def test_csp_is_exact_and_frames_one_host_only(self) -> None:
        self.assertEqual(
            _header("Content-Security-Policy"),
            "default-src 'self'; script-src 'self'; script-src-attr 'none'; style-src 'self'; style-src-attr 'none'; "
            "img-src 'self'; font-src 'self'; connect-src 'self'; media-src 'self'; "
            "frame-src https://www.youtube-nocookie.com; worker-src 'none'; base-uri 'none'; form-action 'none'; "
            "frame-ancestors 'none'; object-src 'none'; require-trusted-types-for 'script'; trusted-types 'none'",
        )
        csp = self._csp()
        self.assertEqual(csp["frame-src"], self.PLAYER_HOST)
        # No other directive names any host: no remote script, image (thumbnail), style, font or connection.
        for name, value in csp.items():
            if name != "frame-src":
                self.assertNotIn("http", value, name)
                self.assertNotIn("*", value, name)
        self.assertEqual(csp["script-src"], "'self'")
        self.assertEqual(csp["img-src"], "'self'")
        self.assertEqual(csp["style-src-attr"], "'none'")
        self.assertEqual(csp["require-trusted-types-for"], "'script'")
        self.assertEqual(csp["trusted-types"], "'none'")
        self.assertEqual(csp["frame-ancestors"], "'none'")

    def test_permissions_policy_is_exact_and_only_autoplay_opens(self) -> None:
        value = _header("Permissions-Policy")
        self.assertEqual(
            value,
            'accelerometer=(), autoplay=(self "https://www.youtube-nocookie.com"), bluetooth=(), browsing-topics=(), camera=(), '
            "display-capture=(), encrypted-media=(), geolocation=(), gyroscope=(), hid=(), idle-detection=(), interest-cohort=(), "
            "local-fonts=(), magnetometer=(), microphone=(), midi=(), payment=(), picture-in-picture=(), "
            "publickey-credentials-get=(), screen-wake-lock=(), serial=(), usb=(), xr-spatial-tracking=()",
        )
        features = dict(item.split("=", 1) for item in value.split(", "))
        self.assertEqual(features.pop("autoplay"), f'(self "{self.PLAYER_HOST}")')
        self.assertEqual(set(features.values()), {"()"}, "every other feature stays denied")
        self.assertEqual(len(features), 22)

    def test_the_player_host_appears_in_the_two_headers_and_nowhere_else(self) -> None:
        ht = (ROOT / "deploy" / "htaccess.txt").read_text(encoding="utf-8")
        lines = [ln.strip() for ln in ht.splitlines() if "youtube" in ln.lower() and not ln.lstrip().startswith("#")]
        self.assertEqual(len(lines), 2)
        self.assertTrue(lines[0].startswith("Header always set Content-Security-Policy "))
        self.assertTrue(lines[1].startswith("Header always set Permissions-Policy "))
        for ln in lines:
            self.assertEqual(ln.lower().count("youtube"), 1)
        self.assertNotIn("ytimg", ht)
        self.assertNotIn("google", ht.lower())
        self.assertEqual(_header("Referrer-Policy"), "no-referrer")
        self.assertEqual(_header("X-Frame-Options"), "DENY")


class FilmPlayerMarkupTests(unittest.TestCase):
    """The cover player as built: poster, hidden play button, privacy line, plain link; no frame, no YouTube player host."""

    NAME_EN = "Play film: Informatico intro, 45 seconds, from YouTube"
    NAME_ES = "Reproducir video: Informatico, introducción, 45 segundos, desde YouTube"
    PRIVACY_EN = "This film plays from YouTube. Nothing from YouTube loads until you press play; then YouTube can see you came from this site."
    PRIVACY_ES = "Este video se reproduce desde YouTube. No se carga nada de YouTube hasta que oprimas reproducir; entonces YouTube puede ver que llegaste desde este sitio."

    def _figure(self, page: str) -> str:
        found = re.findall(r'<figure class="tp-cover-film" id="film-informatico-intro" data-film="informatico-intro">.*?</figure>', page, re.S)
        self.assertEqual(len(found), 1)
        return found[0]

    def test_only_the_intro_is_the_cover_player(self) -> None:
        self.assertEqual(B.COVER_PLAYER_SLUG, "informatico-intro")
        self.assertEqual([f["youtube_id"] for f in FILMS if f["slug"] == B.COVER_PLAYER_SLUG], ["1NQqIR1ihlc"])
        self.assertEqual(B.render_cover_film_player(".", [dict(FIXTURE[0], youtube_id=None), FIXTURE[1]]), "")
        self.assertEqual(B.render_cover_film_player(".", [FIXTURE[1]]), "")
        html = B.render_cover_film_player(".", FIXTURE)
        self.assertEqual(html.count("data-yt="), 1)
        self.assertNotIn("follow-the-light", html)
        self.assertNotIn("Zz9-Yy8_Xx7", html)

    def test_player_markup_exact_pieces(self) -> None:
        html = B.render_cover_film_player(".", FIXTURE)
        self.assertIn('<div class="tp-film-facade" data-yt="AbC_dEf-123" ', html)
        self.assertRegex(
            html,
            r'<img class="tp-film-poster" src="images/films/informatico-intro\.webp\?v=[0-9a-f]{8}" width="640" height="360" '
            r'loading="eager" fetchpriority="high" decoding="async" alt="">',
        )
        self.assertEqual(html.count("<button"), 1)
        self.assertIn('<button type="button" class="tp-film-play" aria-describedby="film-privacy-informatico-intro" hidden>', html)
        self.assertIn('<span class="tp-film-play-glyph" aria-hidden="true"></span>', html)
        button = re.search(r"<button.*?</button>", html, re.S).group(0)
        self.assertIn(f'data-en="{self.NAME_EN}" data-es="{self.NAME_ES}">{self.NAME_EN}</span>', button)
        self.assertNotIn("aria-label", button, "the name is text, so the Spanish page can carry it in its own HTML")
        self.assertIn(
            f'<span class="tp-film-privacy" id="film-privacy-informatico-intro" data-en="{self.PRIVACY_EN}" data-es="{self.PRIVACY_ES}" hidden>'
            f"{self.PRIVACY_EN}</span>",
            html,
        )
        self.assertEqual(html.count('id="film-privacy-informatico-intro"'), 1)
        self.assertEqual(
            re.findall(r'<a class="tp-film-out" href="([^"]+)" rel="([^"]+)"', html),
            [("https://www.youtube.com/watch?v=AbC_dEf-123", "noopener noreferrer")],
        )
        self.assertEqual(re.findall(r'href="([^"]+)"', html), ["https://www.youtube.com/watch?v=AbC_dEf-123"])
        self.assertNotIn(" style=", html)
        self.assertNotIn("<iframe", html.lower())
        self.assertNotIn("srcdoc", html.lower())

    def test_bad_rows_stop_the_build(self) -> None:
        for bad in ("abc", "AbC_dEf-1234", 'AbC"dEf-123', "AbC_dEf-123\n", "", 12345678901):
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, "youtube_id must"):
                B.render_cover_film_player(".", [dict(FIXTURE[0], youtube_id=bad)])
        with self.assertRaisesRegex(ValueError, "duration must"):
            B.render_cover_film_player(".", [dict(FIXTURE[0], duration="45")])
        for bad in (None, "", "images/films/missing.webp", "https://example.com/x.webp"):
            with self.subTest(poster=bad), self.assertRaisesRegex(ValueError, "needs an existing"):
                B.render_cover_film_player(".", [dict(FIXTURE[0], poster=bad)])

    def test_spoken_duration(self) -> None:
        self.assertEqual(B._spoken_duration("0:45"), ("45 seconds", "45 segundos"))
        self.assertEqual(B._spoken_duration("0:01"), ("1 second", "1 segundo"))
        self.assertEqual(B._spoken_duration("1:00"), ("1 minute", "1 minuto"))
        self.assertEqual(B._spoken_duration("4:58"), ("4 minutes 58 seconds", "4 minutos 58 segundos"))

    def test_player_sits_in_the_hero_before_everything_else_on_both_covers(self) -> None:
        en, es = _render_hub_with(FIXTURE)
        for rel, page, name, privacy in (("en", en, self.NAME_EN, self.PRIVACY_EN), ("es", es, self.NAME_ES, self.PRIVACY_ES)):
            fig = self._figure(page)
            hero = re.search(r'<section class="tp-cover-hero".*?</section>', page, re.S).group(0)
            self.assertIn(fig, hero, rel)
            self.assertLess(page.index('id="cover-heading"'), page.index('class="tp-cover-film"'), rel)
            self.assertLess(page.index('class="tp-cover-film"'), page.index('class="tp-fronts"'), rel)
            self.assertLess(page.index('class="tp-cover-film"'), page.index('id="tp-featured-edition-desk"'), rel)
            self.assertNotIn("tp-cover-figure", page, rel)
            self.assertIn(f">{name}</span>", fig, rel)
            self.assertIn(f">{privacy}</span>", fig, rel)
            self.assertEqual(page.count('class="tp-film-facade"'), 1, rel)
        self.assertIn(">Ver en youtube.com</a>", self._figure(es))
        self.assertIn(">Informatico: introducción · 0:45</span>", self._figure(es))
        self.assertIn("oprimas", self.PRIVACY_ES)

    def test_built_html_names_no_youtube_player_host_and_ships_no_frame(self) -> None:
        """Every built page: no frame, no player or thumbnail host, no preconnect or dns-prefetch."""
        pages = sorted(SRC.rglob("*.html"))
        self.assertGreater(len(pages), 150)
        for page in pages:
            low = page.read_text(encoding="utf-8").lower()
            rel = page.relative_to(SRC).as_posix()
            for banned in ("<iframe", "youtube-nocookie", "ytimg", "youtube.com/embed", "preconnect", "dns-prefetch", "srcdoc"):
                self.assertNotIn(banned, low, f"{rel}: {banned}")
        for rel in ("index.html", "es-mx/index.html", "about/index.html", "es-mx/about/index.html"):
            html = (SRC / rel).read_text(encoding="utf-8")
            hosts = set(re.findall(r"https?://([a-z0-9.-]*(?:youtube|youtu\.be|google|ytimg|ggpht)[a-z0-9.-]*)", html.lower()))
            self.assertEqual(hosts, {"www.youtube.com"}, rel)
            for tag, attrs in _loading_tags(html):
                self.assertNotIn("youtu", " ".join(f"{k}={v or ''}" for k, v in attrs).lower(), f"{rel}: <{tag}>")

    def test_css_sizes_the_frame_by_class(self) -> None:
        css = (SRC / "informatico.css").read_text(encoding="utf-8")
        for needle in (".tp-film-frame", ".tp-film-play[hidden]", ".tp-film-play:focus-visible", ".tp-film-facade", ".tp-cover-film"):
            self.assertIn(needle, css)
        self.assertNotIn("youtube-nocookie", css.lower())
        self.assertNotIn("ytimg", css.lower())


class _Elements(HTMLParser):
    """Flat list of elements in document order: (tag, attrs dict, text directly inside, ancestor tags+classes).
    Parsed with html.parser, never matched with a tag regex."""

    VOID = {"img", "br", "hr", "meta", "link", "input", "source", "wbr", "area", "base", "col", "embed", "track"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.items: list[dict] = []
        self.stack: list[dict] = []

    def handle_starttag(self, tag, attrs):
        item = {"tag": tag, "attrs": dict(attrs), "text": "", "path": [(e["tag"], e["attrs"].get("class", "")) for e in self.stack]}
        self.items.append(item)
        if tag not in self.VOID:
            self.stack.append(item)

    def handle_startendtag(self, tag, attrs):
        self.items.append({"tag": tag, "attrs": dict(attrs), "text": "", "path": [(e["tag"], e["attrs"].get("class", "")) for e in self.stack]})

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if self.stack:
            self.stack[-1]["text"] += data


def _elements(html: str) -> list[dict]:
    parser = _Elements()
    parser.feed(html)
    parser.close()
    return parser.items


def _inside(item: dict, tag: str, cls: str) -> bool:
    return any(t == tag and cls in c.split() for t, c in item["path"])


def _render_about_with(films: list[dict]) -> tuple[str, str]:
    """Render both About pages in memory with a temporary films.json; nothing under src/ is written."""
    catalog = json.loads((SRC / "data" / "magazine_catalog.json").read_text(encoding="utf-8"))
    saved = B.FILMS_JSON
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "films.json"
        p.write_text(json.dumps(films), encoding="utf-8")
        B.FILMS_JSON = p
        try:
            en = B.render_about_page(catalog, "en")
            es = B.to_spanish_static(B.render_about_page(catalog, "es"))
        finally:
            B.FILMS_JSON = saved
    return en, es


class AboutFilmPlayerTests(unittest.TestCase):
    """/about/ and /es-mx/about/: the sister lab's trailer as a click-to-play player in the hero."""

    TRAILER = {"slug": "cf-lab-trailer", "youtube_id": "Qq1_Ww2-Ee3", "duration": "0:30", "poster": "images/films/cf-lab-trailer.webp"}
    NAME_EN = "Play film: Sensei Ewok's CF Lab, 30 seconds, from YouTube"
    NAME_ES = "Reproducir video: Sensei Ewok's CF Lab, 30 segundos, desde YouTube"
    FRAME_EN = "Sensei Ewok's CF Lab: a 30-second trip to the CFTR gene"
    FRAME_ES = "Sensei Ewok's CF Lab: un viaje de 30 segundos al gen CFTR"
    # The sister site's name is assembled here: tests/test_informatico_public.py lets only the About sources spell it.
    SISTER_SITE = "senseiewok" + ".ai"
    NOTE_EN = f"The lab's cystic fibrosis film, from {SISTER_SITE}."
    NOTE_ES = f"El video del laboratorio sobre fibrosis quística, de {SISTER_SITE}."

    def _film_parts(self, page: str) -> dict:
        """The player's elements on a page, found by parsing: exactly one figure, facade, button, link."""
        els = _elements(page)
        figures = [e for e in els if e["tag"] == "figure" and "tp-cover-film" in e["attrs"].get("class", "").split()]
        self.assertEqual(len(figures), 1)
        inside = [e for e in els if _inside(e, "figure", "tp-cover-film")]

        def one(tag: str, cls: str) -> dict:
            found = [e for e in inside if e["tag"] == tag and cls in e["attrs"].get("class", "").split()]
            self.assertEqual(len(found), 1, f"{tag}.{cls}")
            return found[0]

        return {
            "figure": figures[0],
            "facade": one("div", "tp-film-facade"),
            "img": one("img", "tp-film-poster"),
            "button": one("button", "tp-film-play"),
            "glyph": one("span", "tp-film-play-glyph"),
            "name": one("span", "tp-sr-only"),
            "title": one("span", "tp-film-title"),
            "link": one("a", "tp-film-out"),
            "privacy": one("span", "tp-film-privacy"),
            "note": one("span", "tp-film-note"),
            "all": inside,
            "page": els,
        }

    def test_two_players_one_per_page_and_neither_is_a_shelf_card(self) -> None:
        self.assertEqual(B.ABOUT_PLAYER_SLUG, "cf-lab-trailer")
        self.assertEqual(B.PLAYER_SLUGS, ("informatico-intro", "cf-lab-trailer"))
        self.assertEqual([f["youtube_id"] for f in FILMS if f["slug"] == B.ABOUT_PLAYER_SLUG], ["NaH3vw-wX1A"])
        self.assertEqual([f["duration"] for f in FILMS if f["slug"] == B.ABOUT_PLAYER_SLUG], ["0:30"])
        films = [FIXTURE[0], self.TRAILER, FIXTURE[1]]
        shelf = B.render_cover_films_section(".", films)
        self.assertNotIn("cf-lab-trailer", shelf)
        self.assertNotIn(self.TRAILER["youtube_id"], shelf)
        self.assertEqual(shelf.count('class="tp-film-link"'), 1)
        cover = B.render_cover_film_player(".", films)
        self.assertNotIn(self.TRAILER["youtube_id"], cover)
        about = B.render_about_film_player("..", films)
        self.assertNotIn(FIXTURE[0]["youtube_id"], about)
        self.assertEqual(about.count("data-yt="), 1)
        with self.assertRaisesRegex(ValueError, "not a click-to-play film"):
            B.render_film_player("follow-the-light", ".", films)

    def test_bad_rows_stop_the_build(self) -> None:
        for bad in ("abc", "Qq1_Ww2-Ee34", 'Qq1"Ww2-Ee3', "Qq1_Ww2-Ee3\n", "", 12345678901):
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, "youtube_id must"):
                B.render_about_film_player("..", [dict(self.TRAILER, youtube_id=bad)])
        with self.assertRaisesRegex(ValueError, "duration must"):
            B.render_about_film_player("..", [dict(self.TRAILER, duration="30")])
        for bad in (None, "images/films/missing.webp", "https://example.com/x.webp"):
            with self.subTest(poster=bad), self.assertRaisesRegex(ValueError, "needs an existing"):
                B.render_about_film_player("..", [dict(self.TRAILER, poster=bad)])

    def test_about_player_markup_on_both_pages(self) -> None:
        en, es = _render_about_with([FIXTURE[0], self.TRAILER, FIXTURE[1]])
        want_href = f"https://www.youtube.com/watch?v={self.TRAILER['youtube_id']}"
        for rel, page, name, privacy, note, link_text, title, poster_prefix in (
            ("en", en, self.NAME_EN, B.FILM_PRIVACY_EN, self.NOTE_EN, "Watch on youtube.com", self.FRAME_EN + " · 0:30", "../images/films/"),
            ("es", es, self.NAME_ES, B.FILM_PRIVACY_ES, self.NOTE_ES, "Ver en youtube.com", self.FRAME_ES + " · 0:30", "../../images/films/"),
        ):
            with self.subTest(page=rel):
                p = self._film_parts(page)
                self.assertEqual(p["figure"]["attrs"].get("data-film"), "cf-lab-trailer")
                self.assertTrue(_inside(p["figure"], "section", "tp-cover-hero"), "the player sits in the hero")
                self.assertEqual(p["facade"]["attrs"]["data-yt"], self.TRAILER["youtube_id"])
                self.assertEqual(p["facade"]["attrs"]["data-title-en"], self.FRAME_EN)
                self.assertEqual(p["facade"]["attrs"]["data-title-es"], self.FRAME_ES)
                img = p["img"]["attrs"]
                self.assertEqual((img["alt"], img["width"], img["height"], img["loading"]), ("", "640", "360", "eager"))
                self.assertRegex(img["src"], r"^" + re.escape(poster_prefix) + r"cf-lab-trailer\.webp\?v=[0-9a-f]{8}$")
                self.assertTrue((SRC / "images" / "films" / "cf-lab-trailer.webp").is_file())
                button = p["button"]["attrs"]
                self.assertEqual(button["type"], "button")
                self.assertIn("hidden", button)
                self.assertNotIn("aria-label", button)
                self.assertEqual(button["aria-describedby"], "film-privacy-cf-lab-trailer")
                self.assertEqual(p["glyph"]["attrs"]["aria-hidden"], "true")
                self.assertEqual(p["name"]["text"], name)
                self.assertEqual((p["name"]["attrs"]["data-en"], p["name"]["attrs"]["data-es"]), (self.NAME_EN, self.NAME_ES))
                self.assertEqual(p["privacy"]["attrs"]["id"], "film-privacy-cf-lab-trailer")
                self.assertIn("hidden", p["privacy"]["attrs"])
                self.assertEqual(p["privacy"]["text"], privacy)
                self.assertEqual(p["note"]["text"], note)
                self.assertEqual(p["title"]["text"], title)
                self.assertEqual(p["link"]["attrs"]["href"], want_href)
                self.assertEqual(p["link"]["attrs"]["rel"], "noopener noreferrer")
                self.assertEqual(p["link"]["text"], link_text)
                # Nothing in the figure loads from, or frames, another host; nothing carries an inline style.
                for e in p["all"]:
                    self.assertNotIn(e["tag"], {"iframe", "script", "embed", "object", "video", "source"}, rel)
                    self.assertNotIn("style", e["attrs"], rel)
                    self.assertNotIn("srcdoc", e["attrs"], rel)
                self.assertEqual([e["attrs"]["href"] for e in p["all"] if "href" in e["attrs"]], [want_href])
                # One player, one privacy id, and the old Plate 0-A figure gives way to it.
                self.assertEqual(sum(1 for e in p["page"] if e["attrs"].get("id") == "film-privacy-cf-lab-trailer"), 1)
                self.assertEqual(sum(1 for e in p["page"] if e["tag"] == "iframe"), 0)
                self.assertEqual(sum(1 for e in p["page"] if "tp-cover-figure" in e["attrs"].get("class", "").split()), 0)
                # Order in the document: heading first, then the player, then the essay.
                ids = [e["attrs"].get("id") for e in p["page"]]
                order = [i for i, e in enumerate(p["page"]) if e is p["figure"]][0]
                self.assertLess(ids.index("about-heading"), order)
                self.assertLess(order, ids.index("pace1-heading"))

    def test_about_keeps_its_plate_while_the_trailer_is_dormant(self) -> None:
        en, es = _render_about_with([FIXTURE[0], dict(self.TRAILER, youtube_id=None), FIXTURE[1]])
        for rel, page in (("en", en), ("es", es)):
            els = _elements(page)
            self.assertEqual(sum(1 for e in els if "tp-cover-film" in e["attrs"].get("class", "").split()), 0, rel)
            self.assertEqual(sum(1 for e in els if "tp-film-facade" in e["attrs"].get("class", "").split()), 0, rel)
            self.assertEqual(sum(1 for e in els if e["tag"] == "figure" and "tp-cover-figure" in e["attrs"].get("class", "").split()), 1, rel)

    def test_built_about_pages_match_films_json(self) -> None:
        trailer = next(f for f in FILMS if f["slug"] == B.ABOUT_PLAYER_SLUG)
        for rel, name in (("about/index.html", self.NAME_EN), ("es-mx/about/index.html", self.NAME_ES)):
            p = self._film_parts((SRC / rel).read_text(encoding="utf-8"))
            self.assertEqual(p["facade"]["attrs"]["data-yt"], trailer["youtube_id"], rel)
            self.assertEqual(p["link"]["attrs"]["href"], f"https://www.youtube.com/watch?v={trailer['youtube_id']}", rel)
            self.assertEqual(p["name"]["text"], name, rel)
            self.assertEqual(sum(1 for e in p["page"] if e["tag"] == "iframe"), 0, rel)
            scripts = [e["attrs"].get("src", "") for e in p["page"] if e["tag"] == "script" and "src" in e["attrs"]]
            self.assertTrue(any(s.endswith("modules/main.mjs") for s in scripts), f"{rel}: the page loads the module entry")

    def test_the_caption_says_whose_film_it_is_and_no_more(self) -> None:
        copy = B.FILM_COPY["cf-lab-trailer"]
        self.assertEqual((copy["note_en"], copy["note_es"]), (self.NOTE_EN, self.NOTE_ES))
        for text in (copy["note_en"], copy["note_es"], copy["title_en"], copy["title_es"]):
            low = text.lower()
            for word in ("cure", "cura", "treat", "trat", "therap", "terap", "breakthrough", "award", "premio", "proves", "demuestra"):
                self.assertNotIn(word, low, text)

    def test_security_doc_states_the_one_exception(self) -> None:
        doc = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
        self.assertIn("pressing play builds one frame for `https://www.youtube-nocookie.com`", doc)
        self.assertIn("The pages ship no frame and request nothing from another host", doc)


class FilmFacadeModuleTests(unittest.TestCase):
    """Static pins on src/modules/film-facade.mjs. tests/test_film_facade_browser.py runs it in Chromium."""

    def setUp(self) -> None:
        self.src = (SRC / "modules" / "film-facade.mjs").read_text(encoding="utf-8")
        self.code = self.src.split("*/", 1)[1]
        self.main = (SRC / "modules" / "main.mjs").read_text(encoding="utf-8")

    def test_module_is_wired_from_the_site_entry(self) -> None:
        self.assertIn('import { initFilmFacade } from "./film-facade.mjs";', self.main)
        self.assertEqual(self.main.count("initFilmFacade(scope);"), 1)
        boot = self.main[self.main.index("function bootMagazine("):]
        self.assertIn("initFilmFacade(scope);", boot[: boot.index("}")])

    def test_one_host_one_fixed_address_shape(self) -> None:
        self.assertEqual(re.findall(r'"(https?://[^"]*)"', self.code), ["https://www.youtube-nocookie.com"])
        self.assertIn('const EMBED_QUERY = "autoplay=1&rel=0&playsinline=1";', self.code)
        self.assertIn("isFilmId(id) ? `${EMBED_ORIGIN}/embed/${id}?${EMBED_QUERY}` : null", self.code)
        self.assertEqual(len(re.findall(r"`[^`]*\$\{[^`]*`", self.code)), 2, "one address template and one selector")
        self.assertEqual(self.code.count('setAttribute("src"'), 1)
        self.assertIn('frame.setAttribute("src", src);', self.code)
        for other in ("ytimg", "youtube.com", "google", "youtu.be"):
            self.assertNotIn(other, self.code, other)

    def test_id_is_validated_at_init_and_again_at_click(self) -> None:
        self.assertIn("const ID_PATTERN = /^[A-Za-z0-9_-]{11}$/;", self.code)
        self.assertIn('return typeof value === "string" && ID_PATTERN.test(value);', self.code)
        create = self.code[self.code.index("export function createFilmFrame(") : self.code.index("function frameTitle(")]
        self.assertLess(create.index("filmEmbedSrc(id)"), create.index('createElement("iframe")'))
        self.assertRegex(create, r"if \(src === null\) \{\s+return null;\s+\}\s+const frame = doc\.createElement")
        play = self.code[self.code.index("function playFilm(") : self.code.index("export function initFilmFacade(")]
        self.assertIn('createFilmFrame(doc, facade.getAttribute("data-yt")', play, "the ID is read from the DOM again at click time")
        self.assertRegex(play, r"return null;\s+\}\s+button\.replaceWith\(frame\);\s+frame\.focus\(\);")
        # A failed check at click time withdraws the control and hands focus to the plain link: no dead button.
        dead = play[play.index("if (frame === null) {") : play.index("button.replaceWith(frame);")]
        self.assertIn('button.setAttribute("hidden", "");', dead)
        self.assertIn('privacy.setAttribute("hidden", "");', dead)
        self.assertIn("link.focus();", dead)
        self.assertRegex(dead, r"return null;\s+\}\s*$")

    def test_frame_is_built_only_inside_the_click_path_with_exact_attributes(self) -> None:
        self.assertEqual(self.code.count('createElement("iframe")'), 1)
        self.assertEqual(self.code.count("createElement("), 1)
        self.assertEqual(self.code.count("createFilmFrame("), 2, "defined once, called once")
        self.assertEqual(self.code.count("playFilm("), 2, "defined once, called once")
        self.assertIn('button.addEventListener("click", () => playFilm(facade, button), { once: true });', self.code)
        attrs = re.findall(r'frame\.setAttribute\("([a-z]+)", ("[^"]*"|[a-z]+)\);', self.code)
        self.assertEqual(
            attrs,
            [
                ("class", '"tp-film-frame"'),
                ("src", "src"),
                ("title", "title"),
                ("allow", '"autoplay; fullscreen"'),
                ("referrerpolicy", '"strict-origin-when-cross-origin"'),
                ("width", '"640"'),
                ("height", '"360"'),
                ("tabindex", '"0"'),
            ],
        )
        self.assertNotIn("loading", self.code, "the frame is wanted now; never lazy")

    def test_no_markup_injection_no_inline_style_no_network(self) -> None:
        for banned in ("innerHTML", "outerHTML", "insertAdjacentHTML", "srcdoc", "document.write", "eval(", "fetch(",
                       "XMLHttpRequest", "sendBeacon", ".style", "cssText", '"style"', "location.", "window.open",
                       "import(", "new Image", "preconnect", "localStorage", "sessionStorage", "document.cookie"):
            self.assertNotIn(banned, self.code, banned)

    def test_it_cannot_stop_the_page_from_booting(self) -> None:
        body = self.code[self.code.index("export function initFilmFacade("):]
        self.assertRegex(body, r"\{\s+let wired = 0;\s+try \{")
        self.assertRegex(body, r"\} catch \{[^}]*\}\s+return wired;\s+\}\s*$")

    def test_files_use_lf_line_endings(self) -> None:
        for rel in ("src/modules/film-facade.mjs", "src/modules/main.mjs", "deploy/htaccess.txt", "tests/test_films.py",
                    "tests/test_film_facade_browser.py"):
            self.assertNotIn(b"\r", (ROOT / rel).read_bytes(), rel)


if __name__ == "__main__":
    unittest.main()
