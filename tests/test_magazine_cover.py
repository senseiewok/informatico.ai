#!/usr/bin/env python3
"""The cover's first impression (magazine pass, phase 1, 2026-11-28).

A reader who is not a developer said the site "looks like a developer site". What this file holds in place:

- the hero says what the site is in plain words, with three buttons, and none of the builder copy (SKILL.md,
  verifiers, clone, planted defect), which now lives on /about/ under "For builders and coders";
- the section tiles use everyday names, carry no folio codes, and are never cut off with an ellipsis;
- "This week's essay" and "Coming next" show an essay and a short list, with no slot numbers, code pills, script
  names or formulas; each standfirst is word for word from the essay it points to;
- on an essay card the title comes first and the folio code last, in small grey sans-serif;
- a card with no picture is a text card, never an empty grey box;
- an act pill's label names the section its own link opens (theme-plate.mjs once relabelled pills by position);
- on a phone the headline, the deck and Start reading come before the film, and the film before the tiles.

Part one reads the built pages with html.parser (no browser). Part two drives Chromium under the
Content-Security-Policy from deploy/htaccess.txt and is skipped when Playwright or Chromium is not installed.
"""
from __future__ import annotations

import json
import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:  # pragma: no cover
    sync_playwright = None

from tests.test_a11y_axe import _load_csp_header, find_chrome
from tests.test_film_facade_browser import serve_with_headers

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(ROOT / "tools"))
import build_longform_folios as B  # noqa: E402

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
COVERS = (("index.html", "en"), ("es-mx/index.html", "es"))
PILLARS = ("engineering", "architecture", "physics", "math")
CODE_RE = re.compile(r"\b(?:[AEMPBXT]|CC|ES)\.\d{2}\b")
BUILDER_WORDS = ("SKILL.md", "verifier", "verificador", "clone", "clon ", "planted", "plantado")
MACHINERY_WORDS = (
    "Slot", "Turno", "Rotates", "Rota cada", "Gated by", "Sujeta a", "build_", "check_", ".py", "Release Queue",
    "Release Desk", "Monograph", "Monografía", "12h", "09:00", "Rotating", "Rotativa",
)
DECK_EN = (
    "Long illustrated essays on how buildings, bridges, physics and math work. "
    "Each one starts with a story, explains the idea in plain words, and gives you a model you can move."
)
DECK_ES = (
    "Ensayos largos e ilustrados sobre cómo funcionan los edificios, los puentes, la física y las matemáticas. "
    "Cada uno empieza con una historia, explica la idea en palabras sencillas y te da un modelo que puedes mover."
)


class Node:
    def __init__(self, tag: str, attrs: dict, parent: "Node | None") -> None:
        self.tag, self.attrs, self.parent = tag, attrs, parent
        self.children: list = []  # Node or str, in document order

    @property
    def classes(self) -> list[str]:
        return (self.attrs.get("class") or "").split()

    def walk(self):
        for child in self.children:
            if isinstance(child, Node):
                yield child
                yield from child.walk()

    def find_all(self, tag: str | None = None, cls: str | None = None, attr: str | None = None) -> list["Node"]:
        return [
            n for n in self.walk()
            if (tag is None or n.tag == tag) and (cls is None or cls in n.classes) and (attr is None or attr in n.attrs)
        ]

    def find(self, tag: str | None = None, cls: str | None = None, attr: str | None = None) -> "Node | None":
        found = self.find_all(tag, cls, attr)
        return found[0] if found else None

    def by_id(self, ident: str) -> "Node | None":
        return next((n for n in self.walk() if n.attrs.get("id") == ident), None)

    def text(self) -> str:
        parts: list[str] = []

        def gather(node: "Node") -> None:
            for child in node.children:
                if isinstance(child, str):
                    parts.append(child)
                elif child.tag not in ("script", "style"):
                    gather(child)

        gather(self)
        return " ".join("".join(parts).split())

    def elements(self) -> list["Node"]:
        return [c for c in self.children if isinstance(c, Node)]


class _Tree(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", {}, None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag, {k: (v if v is not None else "") for k, v in attrs}, self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, {k: (v if v is not None else "") for k, v in attrs}, self.cur))

    def handle_endtag(self, tag):
        node = self.cur
        while node is not self.root and node.tag != tag:
            node = node.parent
        if node is not self.root:
            self.cur = node.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def parse(html_text: str) -> Node:
    tree = _Tree()
    tree.feed(html_text)
    tree.close()
    return tree.root


_PAGES: dict[str, Node] = {}


def page(rel: str) -> Node:
    if rel not in _PAGES:
        _PAGES[rel] = parse((SRC / rel).read_text(encoding="utf-8"))
    return _PAGES[rel]


def norm(text: str) -> str:
    return " ".join(text.split()).casefold()


def resolves(rel: str, href: str) -> bool:
    clean = href.split("#", 1)[0].split("?", 1)[0]
    base = (SRC / rel).parent
    target = (base / clean / "index.html") if clean.endswith("/") or clean == "" else (base / clean)
    return target.resolve().is_file()


class CoverHeroTests(unittest.TestCase):
    def test_hero_says_what_the_site_is_in_plain_words(self) -> None:
        for rel, lang in COVERS:
            hero = page(rel).find("section", "tp-cover-hero")
            self.assertIsNotNone(hero, rel)
            copy = hero.find("div", "tp-cover-copy")
            h1 = copy.find("h1")
            self.assertEqual(h1.attrs["data-en"], "How the built world works, explained and made explorable.", rel)
            deck = copy.find("p", "tp-standfirst")
            self.assertEqual(deck.attrs["data-en"], DECK_EN, rel)
            self.assertEqual(deck.attrs["data-es"], DECK_ES, rel)
            self.assertEqual(deck.text(), DECK_ES if lang == "es" else DECK_EN, rel)
            seen = copy.text() + " " + " ".join(n.attrs.get("data-en", "") + n.attrs.get("data-es", "") for n in copy.walk())
            for word in BUILDER_WORDS:
                self.assertNotIn(word.casefold(), seen.casefold(), f"{rel}: builder copy {word!r} is back in the hero")
            self.assertIsNone(CODE_RE.search(seen), f"{rel}: a folio code in the hero")

    def test_deck_is_true_of_every_essay(self) -> None:
        """"Each one starts with a story, explains the idea in plain words, and gives you a model you can move.\""""
        count = 0
        for pillar in PILLARS:
            for folio_page in sorted((SRC / pillar).glob("*/index.html")):
                tree = parse(folio_page.read_text(encoding="utf-8"))
                slug = folio_page.parent.name
                count += 1
                self.assertIsNotNone(tree.by_id(f"act1-heading-{slug}"), f"{slug}: no story section")
                self.assertTrue(tree.find_all("div", "tp-plain-bridge-box"), f"{slug}: no plain-words box")
                self.assertIsNotNone(tree.by_id(f"act3-heading-{slug}"), f"{slug}: no lab section")
                movable = [n for n in tree.find_all("input") if n.attrs.get("type") == "range"]
                self.assertTrue(movable, f"{slug}: no control to move the model with")
        self.assertEqual(count, sum(len(v) for v in B.NEW_FOLIOS.values()))

    def test_three_buttons_start_browse_and_film(self) -> None:
        films = json.loads((ROOT / "data" / "films.json").read_text(encoding="utf-8"))
        intro = next(f for f in films if f["slug"] == "informatico-intro")
        for rel, lang in COVERS:
            root = page(rel)
            ctas = root.find("section", "tp-cover-hero").find("div", "tp-cover-ctas").elements()
            labels = [(n.tag, n.attrs.get("data-en"), n.attrs.get("data-es")) for n in ctas]
            expected = [("a", "Start reading", "Empezar a leer"), ("button", "Browse all essays", "Ver todos los ensayos")]
            if intro["youtube_id"] is not None:
                self.assertEqual(intro["duration"], "0:45")
                expected.append(("a", "Watch the 45-second film", "Ver el video de 45 segundos"))
            self.assertEqual(labels, expected, rel)
            start = ctas[0]
            self.assertIn("data-spotlight-start", start.attrs, rel)
            self.assertTrue(resolves(rel, start.attrs["href"]), f"{rel}: Start reading -> {start.attrs['href']}")
            first_slide = root.by_id("tp-featured-edition-desk").find("article", "tp-spotlight-slide")
            self.assertEqual(start.attrs["href"], first_slide.find("a").attrs["href"], rel)
            self.assertIn("data-open-contents", ctas[1].attrs, rel)
            if intro["youtube_id"] is not None:
                self.assertEqual(ctas[2].attrs["href"], "#film-informatico-intro", rel)
                figure = root.by_id("film-informatico-intro")
                self.assertEqual((figure.tag, "tp-cover-film" in figure.classes), ("figure", True), rel)
                privacy = figure.find("span", "tp-film-privacy")
                self.assertEqual(privacy.attrs["data-en"], B.FILM_PRIVACY_EN, rel)
                self.assertEqual(privacy.attrs["data-es"], B.FILM_PRIVACY_ES, rel)

    def test_watch_film_label(self) -> None:
        self.assertEqual(B._watch_film_label("0:45"), ("Watch the 45-second film", "Ver el video de 45 segundos"))
        self.assertEqual(B._watch_film_label("4:58"), ("Watch the film (4:58)", "Ver el video (4:58)"))

    def test_phone_order_is_in_the_stylesheet(self) -> None:
        """Document order is copy, film, tiles; the 860px rule must not pull the film above the headline again."""
        for rel, _lang in COVERS:
            kids = [n for n in page(rel).find("section", "tp-cover-hero").elements()]
            self.assertEqual(
                [("tp-cover-copy" in k.classes, "tp-cover-film" in k.classes, "tp-cover-track-strip" in k.classes) for k in kids],
                [(True, False, False), (False, True, False), (False, False, True)],
                rel,
            )
        css = " ".join((SRC / "informatico.css").read_text(encoding="utf-8").split())
        self.assertIn(
            "@media (max-width: 860px) { .tp-page-cover .tp-cover-copy { order: 1; } .tp-page-cover .tp-cover-film { order: 2; } "
            ".tp-page-cover .tp-cover-track-strip { order: 3; } }",
            css,
        )
        self.assertGreater(css.rindex(".tp-page-cover .tp-cover-film { order: 2; }"), css.rindex(".tp-cover-film { order: 0;"))
        self.assertIn('class="tp-body tp-page-cover"', (SRC / "index.html").read_text(encoding="utf-8"))


class CoverTilesTests(unittest.TestCase):
    def test_tiles_use_everyday_names_and_no_codes(self) -> None:
        names = B.COVER_SECTION_NAMES
        self.assertEqual(names["engineering"][0], "Engineering & construction")
        self.assertEqual(names["bounties"][0], "Unsolved puzzles")
        self.assertEqual(names["toolchain"][0], "For makers: 3D tools")
        expected_hrefs = [
            "engineering/", "architecture/", "physics/", "math/", "bounties/", "toolchain/", "timegravity/",
            "classics/golf-gti/", "classics/sagrada-familia/", "classics/mini-jcw/",
        ]
        for rel, lang in COVERS:
            strip = page(rel).find("nav", "tp-cover-track-strip")
            tiles = strip.find_all("a", "tp-track-chip")
            self.assertEqual([t.attrs["href"] for t in tiles], expected_hrefs, rel)
            for tile in tiles:
                self.assertTrue(resolves(rel, tile.attrs["href"]), f"{rel}: {tile.attrs['href']}")
                kicker, title, meta = (tile.find(None, c) for c in ("tp-track-chip-kicker", "tp-track-chip-title", "tp-track-chip-meta"))
                for part in (kicker, title, meta):
                    for value in (part.attrs["data-en"], part.attrs["data-es"], part.text()):
                        self.assertTrue(value.strip(), rel)
                        self.assertIsNone(CODE_RE.search(value), f"{rel}: folio code on a tile: {value!r}")
                        self.assertNotIn("…", value, rel)
                        self.assertNotIn("...", value, rel)
                        for word in ("Pillar", "Pilar", "PILAR", "Folio", "SKILL", "WebGL", "GLB", "DXF", "Monograph"):
                            self.assertNotIn(word, value, f"{rel}: {value!r}")
                # Short enough to sit on a tile without being cut: a line or two at phone width.
                self.assertLessEqual(len(meta.attrs["data-en"]), 60, meta.attrs["data-en"])
                self.assertLessEqual(len(meta.attrs["data-es"]), 80, meta.attrs["data-es"])
            section_tiles = dict(zip(("engineering", "architecture", "physics", "math", "bounties", "toolchain", "timegravity"), tiles))
            for key, tile in section_tiles.items():
                title = tile.find("strong", "tp-track-chip-title")
                self.assertEqual((title.attrs["data-en"], title.attrs["data-es"]), names[key], rel)
            for tile in tiles[7:]:
                kicker = tile.find("span", "tp-track-chip-kicker")
                self.assertEqual((kicker.attrs["data-en"], kicker.attrs["data-es"]), names["classics"], rel)

    def test_tile_counts_come_from_the_catalogue(self) -> None:
        strip = page("index.html").find("nav", "tp-cover-track-strip")
        kickers = [t.find("span", "tp-track-chip-kicker").attrs["data-en"] for t in strip.find_all("a", "tp-track-chip")]
        n = {p: len(B.NEW_FOLIOS[p]) for p in PILLARS}
        steps = len(B.TIMEGRAVITY_PAGES)
        self.assertEqual(steps, 14)
        self.assertEqual(
            kickers[:7],
            [
                f"{n['engineering']} essays", f"{n['architecture']} essays", f"{n['physics']} essays and a {steps}-step series",
                f"{n['math']} essays", f"{len(B.BOUNTY_FOLIOS)} essays", f"{len(B.TOOLCHAIN_FOLIOS)} guides", f"A {steps}-step series",
            ],
        )

    def test_skills_tile_left_the_grid_for_a_small_link(self) -> None:
        for rel, lang in COVERS:
            root = page(rel)
            strip = root.find("nav", "tp-cover-track-strip")
            self.assertFalse([a for a in strip.find_all("a") if a.attrs["href"].startswith("http")], rel)
            self.assertFalse(root.find_all("a", "tp-track-chip-skills"), rel)
            link = root.find("p", "tp-cover-coders").find("a")
            self.assertEqual(link.attrs["href"], "about/#for-builders", rel)  # each language has its own /about/
            self.assertEqual(link.attrs["data-en"], "For builders and coders: use these essays with AI tools →")
            self.assertTrue(resolves(rel, link.attrs["href"]), rel)

    def test_tile_labels_are_not_clipped_by_the_stylesheet(self) -> None:
        css = " ".join((SRC / "informatico.css").read_text(encoding="utf-8").split())
        for selector in (".tp-track-chip-meta {", ".tp-track-chip-toolchain .tp-track-chip-kicker {"):
            last = css[css.rindex(selector):]
            rule = last[: last.index("}")]
            self.assertIn("white-space: normal", rule, selector)
            self.assertIn("text-overflow: clip", rule, selector)
            self.assertNotIn("monospace", rule, selector)

    def test_pillar_rows_drop_the_pillar_numbers(self) -> None:
        for rel, _lang in COVERS:
            for row in page(rel).find_all("section", "tp-cover-pillar"):
                kicker = row.find("p", "tp-kicker")
                self.assertRegex(kicker.attrs["data-en"], r"^\d+ essays$", rel)
                self.assertRegex(kicker.attrs["data-es"], r"^\d+ ensayos$", rel)
                for more in row.find_all("a", "tp-cover-more"):
                    self.assertIsNone(CODE_RE.search(more.attrs["data-en"] + more.attrs["data-es"]), rel)


class ThisWeekTests(unittest.TestCase):
    def test_this_week_and_coming_next_show_no_machinery(self) -> None:
        for rel, lang in COVERS:
            desk = page(rel).by_id("tp-featured-edition-desk")
            self.assertIsNotNone(desk, rel)
            headings = [(h.attrs["data-en"], h.attrs["data-es"]) for h in desk.find_all("h2")]
            self.assertEqual(headings, [("This week’s essay", "El ensayo de la semana"), ("Read next", "Para leer después")], rel)
            self.assertFalse(desk.find_all("code"), f"{rel}: a formula or code on the cover feature")
            self.assertFalse(desk.find_all("button"), f"{rel}: rotation controls on the cover feature")
            for cls in ("tp-spotlight-pill", "tp-spotlight-badge", "tp-spotlight-law", "tp-release-item", "tp-spotlight-counter"):
                self.assertFalse(desk.find_all(None, cls), f"{rel}: {cls}")
            shown = desk.text() + " " + " ".join(n.attrs.get("data-en", "") + " " + n.attrs.get("data-es", "") for n in desk.walk())
            for word in MACHINERY_WORDS:
                self.assertNotIn(word, shown, f"{rel}: {word!r} on the cover feature")
            kickers = [k.attrs["data-en"] + k.attrs["data-es"] for k in desk.find_all("p", "tp-spotlight-kicker")]
            sections = [s.attrs["data-en"] + s.attrs["data-es"] for s in desk.find_all("span", "tp-coming-section")]
            for value in kickers + sections:
                self.assertIsNone(CODE_RE.search(value), f"{rel}: folio code in {value!r}")

    def test_one_essay_shows_and_three_follow(self) -> None:
        total = len(B.INFORMATICO_SPOTLIGHT_ROTATION)
        for rel, lang in COVERS:
            desk = page(rel).by_id("tp-featured-edition-desk")
            slides = desk.find_all("article", "tp-spotlight-slide")
            self.assertEqual([s.attrs["data-spotlight-slot"] for s in slides], [str(i) for i in range(total)], rel)
            self.assertEqual([i for i, s in enumerate(slides) if "hidden" not in s.attrs], [0], rel)
            for slide, item in zip(slides, B.INFORMATICO_SPOTLIGHT_ROTATION):
                title = slide.find("h3", "tp-spotlight-slide-title").find("a")
                self.assertEqual(title.attrs["data-en"], item["title_en"], rel)
                self.assertTrue(resolves(rel, title.attrs["href"]), f"{rel}: {title.attrs['href']}")
                img = slide.find("img")
                self.assertTrue((SRC / rel).parent.joinpath(img.attrs["src"].split("?", 1)[0]).resolve().is_file(), img.attrs["src"])
                self.assertTrue(img.attrs["alt"].strip(), rel)
                kicker = slide.find("p", "tp-spotlight-kicker")
                self.assertRegex(kicker.attrs["data-en"], r"^[A-Z][^·]+ · \d+ min read$", rel)
                self.assertRegex(kicker.attrs["data-es"], r"^[A-ZÁÉÍÓÚ][^·]+ · \d+ min de lectura$", rel)
                cta = slide.find("a", "tp-cta")
                self.assertEqual((cta.attrs["data-en"], cta.attrs["data-es"]), ("Read this essay →", "Leer este ensayo →"), rel)
            coming = desk.find_all("li", "tp-coming-item")
            self.assertEqual([c.attrs["data-coming-slot"] for c in coming], [str(i) for i in range(total)], rel)
            self.assertEqual([i for i, c in enumerate(coming) if "hidden" not in c.attrs], [1, 2, 3], rel)
            for item_node, item in zip(coming, B.INFORMATICO_SPOTLIGHT_ROTATION):
                link = item_node.find("a", "tp-coming-title")
                self.assertEqual(link.attrs["data-en"], item["title_en"], rel)
                self.assertTrue(resolves(rel, link.attrs["href"]), f"{rel}: {link.attrs['href']}")
            note = desk.find("p", "tp-coming-note")
            self.assertIn("already on the site", note.attrs["data-en"], rel)

    def test_each_standfirst_is_word_for_word_from_its_essay(self) -> None:
        """No new claims on the cover: the standfirst must be found in the essay it points to, in each language."""
        for rel, lang in COVERS:
            desk = page(rel).by_id("tp-featured-edition-desk")
            for slide in desk.find_all("article", "tp-spotlight-slide"):
                href = slide.find("h3").find("a").attrs["href"]
                dek = slide.find("p", "tp-spotlight-dek")
                target = (SRC / rel).parent / href / "index.html"
                essay = norm(parse(target.read_text(encoding="utf-8")).text())
                shown = dek.attrs["data-es" if lang == "es" else "data-en"]
                self.assertEqual(dek.text(), shown, rel)
                self.assertLessEqual(len(shown), 280, shown)
                self.assertIn(norm(shown), essay, f"{rel}: the standfirst for {href} is not in that essay: {shown!r}")

    def test_standfirst_excerpt_only_quotes(self) -> None:
        self.assertEqual(B._standfirst_excerpt("In plain words, a grid is a bicycle. It rolls. It stops."), "A grid is a bicycle. It rolls.")
        self.assertEqual(B._standfirst_excerpt("En palabras sencillas, una red es una bicicleta. Rueda."), "Una red es una bicicleta. Rueda.")
        self.assertEqual(B._standfirst_excerpt("One  sentence only"), "One sentence only")
        long_second = "Short first. " + "x" * 300 + "."
        self.assertEqual(B._standfirst_excerpt(long_second), "Short first.")
        self.assertEqual(B._standfirst_excerpt("About 1.09 parts. Is it physics? Yes."), "About 1.09 parts. Is it physics?")

    def test_module_rotates_weekly_without_innerhtml(self) -> None:
        mod = (SRC / "modules" / "featured-spotlight.mjs").read_text(encoding="utf-8")
        main = (SRC / "modules" / "main.mjs").read_text(encoding="utf-8")
        self.assertIn("export function computeWeekSlot", mod)
        self.assertIn("const WEEK_MS = 7 * 24 * 3600 * 1000;", mod)
        self.assertIn("export function comingNextSlots", mod)
        self.assertNotIn("innerHTML", mod.split("*/", 1)[1])
        self.assertNotIn("Rotates every", mod)
        self.assertIn("initFeaturedSpotlight(scope);", main)


class AboutBuildersTests(unittest.TestCase):
    def test_builder_copy_moved_to_about_intact(self) -> None:
        sys.path.insert(0, str(ROOT / "timegravity"))
        verifiers = B._verifier_count()
        skills = len(list((ROOT / "skills").glob("*/*/SKILL.md")))
        total = sum(len(v) for v in B.NEW_FOLIOS.values())
        en = (
            f"{total} long-form essays and 6 Grand-Challenge & Open-Problem monographs. Each one tells the human story, "
            "builds the everyday intuition, and hands you a live model and a plain-text AI SKILL.md to push, pull and test. "
            f"{verifiers} verifiers across the Toolbox, Time and Gravity and the cross-scale essays can be run from a clone "
            "and must fail under a planted defect."
        )
        es = (
            f"{total} ensayos de largo aliento y 6 monografías de grandes retos y problemas abiertos. Cada uno cuenta la "
            "historia humana, construye la intuición cotidiana y te entrega un modelo vivo y un SKILL.md en texto plano para "
            f"probar. {verifiers} verificadores de la Caja de Herramientas, Tiempo y Gravedad y los ensayos entre escalas se "
            "ejecutan desde un clon y deben fallar ante un defecto plantado."
        )
        for rel, lang in (("about/index.html", "en"), ("es-mx/about/index.html", "es")):
            root = page(rel)
            heading = root.by_id("for-builders")
            self.assertEqual(heading.tag, "h2", rel)
            self.assertEqual((heading.attrs["data-en"], heading.attrs["data-es"]), ("For builders and coders", "Para quienes programan y construyen"), rel)
            siblings = heading.parent.elements()
            para, skills_line = siblings[siblings.index(heading) + 1], siblings[siblings.index(heading) + 2]
            self.assertEqual((para.attrs["data-en"], para.attrs["data-es"]), (en, es), rel)
            self.assertEqual(para.text(), es if lang == "es" else en, rel)
            span, link = skills_line.find("span"), skills_line.find("a")
            self.assertEqual(span.attrs["data-en"], f"{skills} AI SKILL.md · {verifiers} verifiers · Claude · Copilot · Cursor · Antigravity: ", rel)
            self.assertEqual(span.attrs["data-es"], f"{skills} SKILL.md · {verifiers} verificadores · Claude · Copilot · Cursor · Antigravity: ", rel)
            self.assertEqual(link.attrs["href"], "https://github.com/senseiewok/informatico.ai/tree/main/skills", rel)
            self.assertEqual((link.attrs["data-en"], link.attrs["data-es"]), ("Agent Skills & Verifiers on GitHub →", "Skills de IA y Verificadores en GitHub →"), rel)


class EssayCardTests(unittest.TestCase):
    HUBS = [("index.html", "en"), ("es-mx/index.html", "es")] + [
        (f"{prefix}{p}/index.html", lang) for p in PILLARS for prefix, lang in (("", "en"), ("es-mx/", "es"))
    ]

    def _folio_cards(self, rel: str) -> list[Node]:
        return [c for c in page(rel).find_all("a", "tp-rack-card") if "data-folio-volume" in c.attrs]

    def test_title_first_code_last_on_every_essay_card(self) -> None:
        seen = 0
        for rel, _lang in self.HUBS:
            for card in self._folio_cards(rel):
                seen += 1
                parts = [c for c in card.elements() if "tp-rack-thumb-wrap" not in c.classes]
                self.assertEqual([p.classes[0] for p in parts], ["tp-rack-title", "tp-rack-dek", "tp-rack-top"], rel)
                self.assertEqual(parts[0].tag, "strong", rel)
                self.assertIsNone(CODE_RE.match(parts[0].text()), f"{rel}: a card title starts with a code: {parts[0].text()!r}")
                meta = parts[2].elements()
                self.assertEqual([m.classes[0] for m in meta], ["tp-rack-badge", "tp-rack-id"], rel)
                self.assertRegex(meta[1].text(), r"^[AEMP]\.\d{2}$", rel)
                # Codes still identify the card for links and scripts.
                self.assertRegex(card.attrs["data-folio-slug"], r"^[aemp]\d{2}$", rel)
                self.assertTrue(resolves(rel, card.attrs["href"]), f"{rel}: {card.attrs['href']}")
        self.assertEqual(seen, 4 * sum(len(v) for v in B.NEW_FOLIOS.values()))

    def test_hub_card_titles_do_not_open_with_a_code(self) -> None:
        """Bounties and Toolbox hubs: the code sits in the small meta line, the title is the title."""
        for rel in ("bounties/index.html", "es-mx/bounties/index.html", "toolchain/index.html", "es-mx/toolchain/index.html"):
            cards = [c for c in page(rel).find_all("a", "tp-rack-card") if c.attrs.get("data-folio-slug")]
            self.assertGreaterEqual(len(cards), 6, rel)
            for card in cards:
                title = card.find("strong", "tp-rack-title")
                for value in (title.attrs["data-en"], title.attrs["data-es"]):
                    self.assertIsNone(CODE_RE.match(value), f"{rel}: {value!r}")
                self.assertRegex(card.find("span", "tp-rack-id").text(), r"^[BX]\.\d{2} · ", rel)

    def test_codes_are_small_grey_sans_and_titles_serif(self) -> None:
        css = " ".join((SRC / "informatico.css").read_text(encoding="utf-8").split())

        def last_rule(selector: str) -> str:
            tail = css[css.rindex(selector):]
            return tail[: tail.index("}")]

        code = last_rule(".tp-body .tp-rack-id {")
        self.assertIn("font-family: var(--tp-font-ui", code)
        self.assertNotIn("mono", code)
        self.assertIn("color: var(--tp-slate)", code)
        self.assertIn("font-size: 0.72rem", code)
        self.assertIn("order: 2", code)
        self.assertIn("font-family: var(--font-serif", last_rule(".tp-body .tp-rack-title {"))
        self.assertIn("order: 3", last_rule(".tp-body .tp-rack-top {"))
        self.assertIn("font-family: var(--font-serif", last_rule(".tp-track-chip-title {"))

    def test_every_card_picture_is_on_disk(self) -> None:
        for rel, _lang in self.HUBS + [("bounties/index.html", "en"), ("toolchain/index.html", "en"), ("essays/index.html", "en")]:
            for wrap in page(rel).find_all("span", "tp-rack-thumb-wrap"):
                img = wrap.find("img")
                self.assertIsNotNone(img, f"{rel}: an image box with no image in it")
                src = img.attrs["src"].split("?", 1)[0]
                self.assertTrue((SRC / rel).parent.joinpath(src).resolve().is_file(), f"{rel}: card picture missing: {src}")
                self.assertNotIn("v=00000000", img.attrs["src"], rel)

    def test_folio_without_a_plate_gets_a_text_card(self) -> None:
        real = B.NEW_FOLIOS["architecture"][0]
        self.assertTrue(B.plate_exists(real["slug"]))
        with_plate = parse(B.render_rack_cards("architecture", [real], "architecture/", "plates/")).find("a")
        self.assertNotIn("tp-rack-card-textonly", with_plate.classes)
        self.assertEqual(len(with_plate.find_all("img")), 1)

        slug = real["slug"]
        self.assertFalse(B.plate_exists("no-such-plate"))
        original = B.plate_exists
        B.plate_exists = lambda s: False if s == slug else original(s)
        try:
            card = parse(B.render_rack_cards("architecture", [real], "architecture/", "plates/")).find("a")
        finally:
            B.plate_exists = original
        self.assertEqual(card.classes, ["tp-rack-card", "tp-rack-card-textonly"])
        self.assertFalse(card.find_all("img"))
        self.assertFalse(card.find_all("span", "tp-rack-thumb-wrap"), "an empty image box was drawn")
        self.assertEqual([c.classes[0] for c in card.elements()], ["tp-rack-title", "tp-rack-dek", "tp-rack-top"])
        self.assertTrue(card.find("strong", "tp-rack-title").text())

        css = " ".join((SRC / "informatico.css").read_text(encoding="utf-8").split())
        self.assertIn(".tp-body .tp-rack-card-textonly .tp-rack-thumb-wrap, .tp-body .tp-rack-card-noimg .tp-rack-thumb-wrap { display: none; }", css)
        mod = (SRC / "modules" / "card-images.mjs").read_text(encoding="utf-8")
        self.assertIn('"tp-rack-card-noimg"', mod)
        self.assertNotIn("innerHTML", mod)
        self.assertIn("initCardImages(scope);", (SRC / "modules" / "main.mjs").read_text(encoding="utf-8"))


ROMAN = {"1": "I", "2": "II", "3": "III", "4": "IV", "5": "V"}


class ActPillTests(unittest.TestCase):
    def test_theme_module_no_longer_relabels_pills_by_position(self) -> None:
        js = (SRC / "modules" / "theme-plate.mjs").read_text(encoding="utf-8")
        self.assertNotIn("actPills:", js)
        self.assertNotIn("dict.actPills", js)
        self.assertNotIn("pill.textContent", js)
        self.assertIn('rootScope.querySelectorAll("[data-en][data-es]")', js)

    def test_every_pill_names_the_section_it_opens(self) -> None:
        bars = 0
        eight = 0
        for section in PILLARS + ("bounties", "toolchain"):
            for prefix, lang in (("", "en"), ("es-mx/", "es")):
                for folio_page in sorted((SRC / prefix / section).glob("*/index.html")):
                    rel = folio_page.relative_to(SRC).as_posix()
                    root = parse(folio_page.read_text(encoding="utf-8"))
                    slug = folio_page.parent.name
                    for bar in root.find_all("nav", "tp-act-jump-bar"):
                        bars += 1
                        pills = bar.find_all("a", "tp-act-pill")
                        eight += len(pills) == 8
                        labels = [p.attrs["data-en"] for p in pills]
                        self.assertEqual(len(set(labels)), len(labels), f"{rel}: a label is on two pills: {labels}")
                        self.assertEqual(len({p.attrs["href"] for p in pills}), len(pills), rel)
                        for pill in pills:
                            href = pill.attrs["href"]
                            self.assertTrue(href.startswith("#"), rel)
                            self.assertIsNotNone(root.by_id(href[1:]), f"{rel}: pill {pill.attrs['data-en']!r} opens nothing ({href})")
                            self.assertEqual(pill.text(), pill.attrs["data-es" if lang == "es" else "data-en"], rel)
                            act = re.fullmatch(rf"#act([1-5])-heading-{re.escape(slug)}", href)
                            if act:
                                for value in (pill.attrs["data-en"], pill.attrs["data-es"]):
                                    self.assertTrue(value.startswith(ROMAN[act.group(1)] + " · "), f"{rel}: {value!r} -> {href}")
                            if href == f"#act-puzzle-{slug}":
                                self.assertEqual((pill.attrs["data-en"], pill.attrs["data-es"]), ("VI · Puzzle", "VI · Crucigrama"), rel)
                            if "Sources" in pill.attrs["data-en"]:
                                self.assertEqual(href, f"#act5-heading-{slug}", rel)
        self.assertGreaterEqual(bars, 2 * (sum(len(v) for v in B.NEW_FOLIOS.values()) + len(B.BOUNTY_FOLIOS) + len(B.TOOLCHAIN_FOLIOS)))
        self.assertGreaterEqual(eight, 2 * sum(len(v) for v in B.NEW_FOLIOS.values()), "the eight-pill essay bar is the case that broke")


PHONE = {"width": 390, "height": 844}
DESKTOP = {"width": 1440, "height": 900}
WEEK_MS = 7 * 24 * 3600 * 1000
BOXES_JS = """() => {
  const box = (sel) => { const r = document.querySelector(sel).getBoundingClientRect(); return {top: r.top, bottom: r.bottom, left: r.left, right: r.right}; };
  return {
    h1: box('#cover-heading'), deck: box('.tp-cover-hero .tp-standfirst'), start: box('[data-spotlight-start]'),
    film: box('.tp-cover-film'), privacy: box('.tp-film-privacy'), strip: box('.tp-cover-track-strip'), desk: box('#tp-featured-edition-desk'),
    scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth,
    clipped: [...document.querySelectorAll('.tp-track-chip-kicker, .tp-track-chip-meta, .tp-track-chip-title')]
      .filter((el) => el.scrollWidth > el.clientWidth + 1 || getComputedStyle(el).textOverflow === 'ellipsis').map((el) => el.textContent),
  };
}"""
SPOTLIGHT_JS = """() => {
  const desk = document.getElementById('tp-featured-edition-desk');
  const visible = (el) => !el.hasAttribute('hidden') && el.getClientRects().length > 0;
  const slides = [...desk.querySelectorAll('[data-spotlight-slot]')];
  const shown = slides.filter(visible);
  return {
    ready: desk.dataset.spotlightReady, total: slides.length,
    shown: shown.map((s) => Number(s.dataset.spotlightSlot)),
    href: shown.length ? shown[0].querySelector('.tp-spotlight-slide-title a').getAttribute('href') : null,
    start: document.querySelector('[data-spotlight-start]').getAttribute('href'),
    coming: [...desk.querySelectorAll('[data-coming-slot]')].filter(visible).map((c) => Number(c.dataset.comingSlot)),
    now: Date.now(),
  };
}"""
PILLS_JS = """() => [...document.querySelectorAll('.tp-act-jump-bar .tp-act-pill')].map((p) => ({
  text: p.textContent, en: p.dataset.en, es: p.dataset.es, href: p.getAttribute('href'),
  target: !!document.getElementById(p.getAttribute('href').slice(1)),
}))"""
CARDS_JS = """() => [...document.querySelectorAll('.tp-rack-card')].map((card) => {
  const id = card.querySelector('.tp-rack-id'), title = card.querySelector('.tp-rack-title'), wrap = card.querySelector('.tp-rack-thumb-wrap');
  const img = card.querySelector('.tp-rack-thumb');
  return {
    slug: card.dataset.folioSlug || card.getAttribute('href'),
    noimg: card.classList.contains('tp-rack-card-noimg'),
    wrapShown: wrap ? getComputedStyle(wrap).display !== 'none' : false,
    wrapHeight: wrap ? wrap.getBoundingClientRect().height : 0,
    imgOk: img ? img.complete && img.naturalWidth > 0 : null,
    idFont: id ? getComputedStyle(id).fontFamily : '', idSize: id ? parseFloat(getComputedStyle(id).fontSize) : 0,
    idTop: id ? id.getBoundingClientRect().top : 0, titleTop: title ? title.getBoundingClientRect().top : 0,
    titleBottom: title ? title.getBoundingClientRect().bottom : 0, titleSize: title ? parseFloat(getComputedStyle(title).fontSize) : 0,
    titleFont: title ? getComputedStyle(title).fontFamily : '',
    titleText: title ? title.textContent.trim() : '',
  };
})"""


@unittest.skipIf(sync_playwright is None, "Playwright is not installed in this Python")
class MagazineCoverBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome = find_chrome()
        if not cls.chrome:
            raise unittest.SkipTest("no Chromium found (set CHROME_PATH)")
        cls.httpd, cls.base = serve_with_headers(SRC, {"Content-Security-Policy": _load_csp_header()})
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch(
            executable_path=cls.chrome, headless=True, args=["--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE 127.0.0.1"]
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
        cls.pw.stop()
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def _open(self, route: str, viewport: dict, mobile: bool = False, abort: str | None = None):
        ctx = self.browser.new_context(viewport=viewport, is_mobile=mobile, has_touch=mobile)
        tab = ctx.new_page()
        problems: list[str] = []
        tab.on("console", lambda m: problems.append(m.text) if m.type == "error" and (abort is None or "ERR_FAILED" not in m.text) else None)
        tab.on("pageerror", lambda e: problems.append(str(e)))
        if abort:
            tab.route(abort, lambda r: r.abort())
        tab.goto(self.base + route, wait_until="load")
        tab.wait_for_function("document.getElementById('tp-contents') && document.getElementById('tp-contents').dataset.bound === 'true'")
        return ctx, tab, problems

    def test_phone_first_screen_is_headline_deck_and_start_reading_then_film_then_tiles(self) -> None:
        for route in ("", "es-mx/"):
            ctx, tab, problems = self._open(route, PHONE, mobile=True)
            try:
                tab.wait_for_function("!document.querySelector('.tp-film-privacy').hasAttribute('hidden')")
                b = tab.evaluate(BOXES_JS)
                self.assertLess(b["h1"]["bottom"], b["deck"]["top"] + 1, route)
                self.assertLess(b["deck"]["bottom"], b["start"]["top"] + 1, route)
                self.assertLessEqual(b["start"]["bottom"], PHONE["height"], f"{route}: Start reading is below the first screen")
                self.assertLess(b["start"]["bottom"], b["film"]["top"], f"{route}: the film is above Start reading")
                self.assertLess(b["film"]["bottom"], b["strip"]["top"] + 1, f"{route}: the tiles are above the film")
                self.assertGreater(b["privacy"]["bottom"] - b["privacy"]["top"], 10, f"{route}: the privacy line is not shown")
                self.assertLess(b["privacy"]["bottom"], b["strip"]["top"] + 1, route)
                self.assertLess(b["strip"]["bottom"], b["desk"]["top"] + 1, route)
                self.assertLessEqual(b["scrollWidth"], b["clientWidth"], f"{route}: the page scrolls sideways")
                self.assertEqual(b["clipped"], [], f"{route}: a tile label is cut off")
                self.assertEqual(problems, [], route)
            finally:
                ctx.close()

    def test_desktop_keeps_the_film_beside_the_headline(self) -> None:
        ctx, tab, problems = self._open("", DESKTOP)
        try:
            b = tab.evaluate(BOXES_JS)
            self.assertGreater(b["film"]["left"], b["deck"]["right"], "the film is not in the right column")
            self.assertLess(b["film"]["top"], b["start"]["bottom"])
            self.assertLessEqual(b["start"]["bottom"], DESKTOP["height"])
            self.assertEqual(b["clipped"], [], "a tile label is cut off")
            self.assertLessEqual(b["scrollWidth"], b["clientWidth"])
            self.assertEqual(problems, [])
        finally:
            ctx.close()

    def test_film_button_jumps_to_the_player_and_loads_nothing_from_youtube(self) -> None:
        ctx, tab, problems = self._open("", PHONE, mobile=True)
        requests: list[str] = []
        tab.on("request", lambda r: requests.append(r.url))
        try:
            tab.locator(".tp-cta-film").click()
            tab.wait_for_function("() => { const r = document.getElementById('film-informatico-intro').getBoundingClientRect(); return r.top >= 0 && r.top < 400; }")
            self.assertTrue(tab.url.endswith("#film-informatico-intro"))
            self.assertEqual(tab.locator("iframe").count(), 0, "the jump must not start the film")
            self.assertFalse([u for u in requests if "youtube" in u or "ytimg" in u], requests)
            self.assertEqual(problems, [])
        finally:
            ctx.close()

    def test_this_weeks_essay_follows_the_week_and_start_reading_opens_it(self) -> None:
        for route in ("", "es-mx/"):
            ctx, tab, problems = self._open(route, DESKTOP)
            try:
                tab.wait_for_function("document.getElementById('tp-featured-edition-desk').dataset.spotlightReady === '1'")
                s = tab.evaluate(SPOTLIGHT_JS)
                total = len(B.INFORMATICO_SPOTLIGHT_ROTATION)
                self.assertEqual(s["total"], total, route)
                active = (s["now"] // WEEK_MS) % total
                self.assertEqual(s["shown"], [active], route)
                self.assertEqual(s["coming"], [(active + k) % total for k in (1, 2, 3)], route)
                self.assertEqual(s["start"], s["href"], f"{route}: Start reading does not open this week's essay")
                self.assertEqual(s["href"].rstrip("/").split("/")[-1], B.INFORMATICO_SPOTLIGHT_ROTATION[active]["href"].rstrip("/").split("/")[-1], route)
                self.assertEqual(problems, [], route)
            finally:
                ctx.close()

    def test_rotation_arithmetic(self) -> None:
        ctx, tab, _problems = self._open("", DESKTOP)
        try:
            got = tab.evaluate(
                """async () => {
                  const m = await import('/modules/featured-spotlight.mjs');
                  const W = 7 * 24 * 3600 * 1000;
                  return {
                    slots: [0, W - 1, W, 9 * W, 10 * W + 5].map((t) => m.computeWeekSlot(9, t)),
                    guard: [m.computeWeekSlot(0, W), m.computeWeekSlot(NaN, W), m.computeWeekSlot(9, -5)],
                    next: [m.comingNextSlots(0, 9), m.comingNextSlots(7, 9), m.comingNextSlots(8, 9), m.comingNextSlots(0, 3), m.comingNextSlots(0, 1)],
                  };
                }"""
            )
            self.assertEqual(got["slots"], [0, 0, 1, 0, 1])
            self.assertEqual(got["guard"], [0, 0, 0])
            self.assertEqual(got["next"], [[1, 2, 3], [8, 0, 1], [0, 1, 2], [1, 2], []])
        finally:
            ctx.close()

    def test_act_pills_keep_their_own_labels_in_the_browser(self) -> None:
        """The reported bug: on math/m01 and physics/p01 "V · Sources" and "VI · Puzzle" each showed twice."""
        for route, lang in (
            ("math/m01/", "en"), ("physics/p01/", "en"), ("bounties/b01/", "en"), ("toolchain/x01/", "en"),
            ("es-mx/math/m01/", "es"), ("es-mx/physics/p01/", "es"),
        ):
            ctx, tab, problems = self._open(route, DESKTOP)
            try:
                pills = tab.evaluate(PILLS_JS)
                self.assertGreaterEqual(len(pills), 6, route)
                texts = [p["text"] for p in pills]
                self.assertEqual(texts, [p[lang] for p in pills], f"{route}: a pill was relabelled")
                self.assertEqual(len(set(texts)), len(texts), f"{route}: duplicate pills: {texts}")
                self.assertTrue(all(p["target"] for p in pills), route)
                if "/m01/" in route or "/p01/" in route:
                    self.assertEqual(len(pills), 8, route)
                    slug = route.rstrip("/").split("/")[-1]
                    by_href = {p["href"]: p["en"] for p in pills}
                    self.assertEqual(by_href[f"#act5-heading-{slug}"], "V · Sources", route)
                    self.assertEqual(by_href[f"#act-puzzle-{slug}"], "VI · Puzzle", route)
                    self.assertEqual(by_href[f"#act3-heading-{slug}"], "III · Lab & Benchmark", route)
                self.assertEqual(problems, [], route)
            finally:
                ctx.close()

    def test_codes_are_small_and_after_the_title_on_the_page(self) -> None:
        for route in ("", "architecture/"):
            ctx, tab, problems = self._open(route, DESKTOP)
            try:
                cards = [c for c in tab.evaluate(CARDS_JS) if c["idFont"]]
                self.assertGreater(len(cards), 10, route)
                for card in cards:
                    self.assertNotIn("mono", card["idFont"].lower(), f"{route}: {card['slug']}")
                    self.assertGreaterEqual(card["idTop"], card["titleBottom"] - 1, f"{route}: the code is above the title on {card['slug']}")
                    self.assertLess(card["idSize"], card["titleSize"] * 0.8, f"{route}: {card['slug']}")
                    self.assertNotIn("grotesk", card["titleFont"].split(",")[0].lower(), f"{route}: {card['slug']}")
                self.assertEqual(problems, [], route)
            finally:
                ctx.close()

    def test_card_whose_picture_fails_becomes_a_text_card(self) -> None:
        ctx, tab, problems = self._open("architecture/", DESKTOP, abort="**/plates/a12.jpg*")
        try:
            tab.wait_for_function("document.querySelector('[data-folio-slug=\"a12\"]').classList.contains('tp-rack-card-noimg')")
            cards = {c["slug"]: c for c in tab.evaluate(CARDS_JS)}
            broken = cards["a12"]
            self.assertFalse(broken["wrapShown"], "an empty image box is still drawn")
            self.assertEqual(broken["wrapHeight"], 0)
            self.assertTrue(broken["titleText"])
            for slug in ("a11", "a13", "a14"):
                self.assertFalse(cards[slug]["noimg"], slug)
                self.assertTrue(cards[slug]["wrapShown"], slug)
            tab.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            tab.wait_for_function("[...document.querySelectorAll('.tp-rack-thumb')].every((i) => i.complete)")
            empty = [c["slug"] for c in tab.evaluate(CARDS_JS) if c["wrapShown"] and c["imgOk"] is False]
            self.assertEqual(empty, [], "a card shows an image box with no picture in it")
            self.assertEqual(problems, [])
        finally:
            ctx.close()


if __name__ == "__main__":
    unittest.main()
