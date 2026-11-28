#!/usr/bin/env python3
"""The cover's first impression (magazine pass, phases 1 and 2, 2026-11-28).

A reader who is not a developer said the site "looks like a developer site". What this file holds in place:

- the hero says what the site is in plain words, with three buttons, and none of the builder copy (SKILL.md,
  verifiers, clone, planted defect), which now lives on /about/ under "For builders and coders";
- four section fronts (a lead essay with its picture and its own opening words, three headlines, a link to the
  section) and a "More to explore" row use everyday names, carry no folio codes, and are never clamped or cut;
- nothing in the cover's <main> shows a folio code or a word of site machinery, except the film's own caption;
- "This week's essay" and "Coming next" show an essay and a short list, with no slot numbers, code pills, script
  names or formulas; each standfirst is word for word from the essay it points to;
- on an essay card the title comes first and the folio code last, in small grey sans-serif;
- a card with no picture is a text card, never an empty grey box;
- an act pill's label names the section its own link opens (theme-plate.mjs once relabelled pills by position);
- on a phone the headline, the deck and Start reading come before the film, and the film before the rest.

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
    "Each one has a model you can move, and most start with a story told in plain words."
)
DECK_ES = (
    "Ensayos largos e ilustrados sobre cómo funcionan los edificios, los puentes, la física y las matemáticas. "
    "Cada uno tiene un modelo que puedes mover, y la mayoría empieza con una historia contada en palabras sencillas."
)
# Every family of pages the cover calls an essay or puts in "This week's essay" (Bounties are "6 essays" on a tile).
ESSAY_FAMILIES = ("engineering", "architecture", "physics", "math", "bounties", "classics", "timegravity")


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
        """"Each one has a model you can move, and most start with a story told in plain words.\"

        Checked on every page the cover calls an essay, in both languages: each has a range control; more than half
        have a plain-words box. The 58 pillar essays also keep their story and lab sections.
        """
        pages = 0
        with_plain = 0
        for prefix in ("", "es-mx/"):
            for family in ESSAY_FAMILIES:
                for essay in sorted((SRC / prefix / family).glob("*/index.html")):
                    rel = essay.relative_to(SRC).as_posix()
                    tree = parse(essay.read_text(encoding="utf-8"))
                    pages += 1
                    movable = [n for n in tree.find_all("input") if n.attrs.get("type") == "range"]
                    self.assertTrue(movable, f"{rel}: no control to move the model with")
                    if tree.find_all("div", "tp-plain-bridge-box"):
                        with_plain += 1
            # Every featured essay too, including the series front page (timegravity/) and the Toolbox entry.
            for item in B.INFORMATICO_SPOTLIGHT_ROTATION:
                featured = SRC / prefix / item["href"] / "index.html"
                tree = parse(featured.read_text(encoding="utf-8"))
                movable = [n for n in tree.find_all("input") if n.attrs.get("type") == "range"]
                self.assertTrue(movable, f"{prefix}{item['href']}: a featured essay has no control to move the model with")
        self.assertGreater(pages, 150)
        self.assertGreater(with_plain * 2, pages, f"only {with_plain} of {pages} essays have plain-words text")
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
        """Document order is copy, then film; the 860px rule must not pull the film above the headline again.
        The 11-tile strip left the hero in phase 2."""
        for rel, _lang in COVERS:
            root = page(rel)
            kids = [n for n in root.find("section", "tp-cover-hero").elements()]
            self.assertEqual(
                [("tp-cover-copy" in k.classes, "tp-cover-film" in k.classes) for k in kids],
                [(True, False), (False, True)],
                rel,
            )
            self.assertFalse(root.find_all(None, "tp-cover-track-strip"), rel)
            self.assertFalse(root.find_all(None, "tp-track-chip"), rel)
        css = " ".join((SRC / "informatico.css").read_text(encoding="utf-8").split())
        self.assertIn(
            "@media (max-width: 860px) { .tp-page-cover .tp-cover-copy { order: 1; } .tp-page-cover .tp-cover-film { order: 2; } }",
            css,
        )
        self.assertGreater(css.rindex(".tp-page-cover .tp-cover-film { order: 2; }"), css.rindex(".tp-cover-film { order: 0;"))
        self.assertIn('class="tp-body tp-page-cover"', (SRC / "index.html").read_text(encoding="utf-8"))

    def test_one_filled_button_per_block(self) -> None:
        for rel, _lang in COVERS:
            main = page(rel).find("main")
            hero = main.find("section", "tp-cover-hero")
            self.assertEqual(len(hero.find_all(None, "tp-cta-primary")), 1, rel)
            shown = [s for s in main.find_all("article", "tp-spotlight-slide") if "hidden" not in s.attrs]
            self.assertEqual([len(s.find_all(None, "tp-cta-primary")) for s in shown], [1], rel)
            for block in main.find_all("section", "tp-front") + main.find_all("section", "tp-more"):
                self.assertFalse(block.find_all(None, "tp-cta"), f"{rel}: a button on a section front or row")
        css = " ".join((SRC / "informatico.css").read_text(encoding="utf-8").split())
        self.assertIn(
            ".tp-body .tp-text-link, .tp-page-cover a.tp-cta:not(.tp-cta-primary), .tp-page-cover button.tp-cta:not(.tp-cta-primary), "
            ".tp-page-hub a.tp-cta:not(.tp-cta-primary) { padding: 0; border: 0; border-radius: 0; background: none;",
            css,
        )


FRONT_TEXT_CLASSES = ("tp-front-name", "tp-front-title", "tp-front-dek", "tp-front-time", "tp-front-link", "tp-front-all")
MORE_TEXT_CLASSES = ("tp-more-title", "tp-more-desc", "tp-more-links")


def shown_strings(node: Node) -> list[str]:
    """Everything a reader, a translator or a screen reader gets from a subtree: its text, both languages of
    every data-en/data-es pair, and every alt, aria-label and title."""
    out = [node.text()]
    for n in [node] + list(node.walk()):
        for attr in ("data-en", "data-es", "alt", "aria-label", "title"):
            if n.attrs.get(attr):
                out.append(n.attrs[attr])
    return out


class CoverFrontsTests(unittest.TestCase):
    def test_picks_exist_have_plates_and_are_not_in_the_rotation(self) -> None:
        rotation = {item["href"] for item in B.INFORMATICO_SPOTLIGHT_ROTATION}
        self.assertEqual(tuple(B.COVER_FRONTS), PILLARS)
        seen: set[str] = set()
        for pillar, pick in B.COVER_FRONTS.items():
            slugs = (pick["lead"],) + tuple(pick["links"])
            self.assertEqual(len(pick["links"]), 3, pillar)
            catalogue = {f["slug"] for f in B.NEW_FOLIOS[pillar]}
            for slug in slugs:
                self.assertIn(slug, catalogue, f"{pillar}: {slug} is not an essay of this section")
                self.assertNotIn(f"{pillar}/{slug}/", rotation, f"{slug} is already in the weekly rotation")
                self.assertNotIn(slug, seen, f"{slug} is on two fronts")
                seen.add(slug)
                self.assertTrue((SRC / pillar / slug / "index.html").is_file(), slug)
                self.assertTrue((SRC / "es-mx" / pillar / slug / "index.html").is_file(), slug)
            self.assertTrue(B.plate_exists(pick["lead"]), f"{pick['lead']} has no plate")
            self.assertTrue((SRC / "plates" / f"{pick['lead']}.jpg").is_file(), pick["lead"])
        self.assertEqual(B.COVER_FRONTS["engineering"], {"lead": "e07", "links": ("e06", "e08", "e09")})
        self.assertEqual(B.COVER_FRONTS["architecture"], {"lead": "a01", "links": ("a07", "a08", "a09")})
        self.assertEqual(B.COVER_FRONTS["math"], {"lead": "m08", "links": ("m12", "m07", "m10")})
        with self.assertRaises(ValueError):
            B._front_essay("math", "m11")  # in the rotation
        with self.assertRaises(ValueError):
            B._front_essay("math", "zz99")

    def test_four_fronts_in_order_with_a_lead_three_links_and_see_all(self) -> None:
        names = B.COVER_SECTION_NAMES
        for rel, lang in COVERS:
            root = page(rel)
            wrap = root.find("section", "tp-fronts")
            self.assertIsNotNone(wrap, rel)
            fronts = wrap.find_all("section", "tp-front")
            self.assertEqual([f.attrs["aria-labelledby"] for f in fronts], [f"pillar-{p}" for p in PILLARS], rel)
            for pillar, front in zip(PILLARS, fronts):
                pick = B.COVER_FRONTS[pillar]
                by_slug = {f["slug"]: f for f in B.NEW_FOLIOS[pillar]}
                self.assertEqual([c.classes[0] for c in front.elements()], ["tp-front-name", "tp-front-lead", "tp-front-list", "tp-front-all"], rel)
                name = front.by_id(f"pillar-{pillar}")
                self.assertEqual(name.tag, "h2", rel)
                name_link = name.find("a")
                self.assertEqual((name_link.attrs["data-en"], name_link.attrs["data-es"]), names[pillar], rel)
                self.assertEqual(name_link.attrs["href"], f"{pillar}/", rel)
                self.assertTrue(resolves(rel, name_link.attrs["href"]), rel)

                lead = front.find("article", "tp-front-lead")
                img = lead.find("img", "tp-front-img")
                self.assertEqual((img.attrs["loading"], img.attrs["width"], img.attrs["height"]), ("lazy", "1280", "720"), rel)
                src = img.attrs["src"].split("?", 1)[0]
                self.assertTrue(src.endswith(f"plates/{pick['lead']}.jpg"), src)
                self.assertTrue((SRC / rel).parent.joinpath(src).resolve().is_file(), src)
                self.assertNotIn("v=00000000", img.attrs["src"], rel)
                # The picture's link repeats the title's link, so it is kept out of the tab order and the name tree.
                figure = lead.find("a", "tp-front-figure")
                self.assertEqual((figure.attrs["tabindex"], figure.attrs["aria-hidden"], img.attrs["alt"]), ("-1", "true", ""), rel)
                title = lead.find("h3", "tp-front-title").find("a")
                self.assertEqual(title.attrs["href"], f"{pillar}/{pick['lead']}/", rel)
                self.assertEqual(figure.attrs["href"], title.attrs["href"], rel)
                self.assertTrue(resolves(rel, title.attrs["href"]), rel)
                self.assertEqual(title.attrs["data-en"], B.decf_title(by_slug[pick["lead"]]["title"]), rel)
                self.assertEqual(title.text(), title.attrs["data-es" if lang == "es" else "data-en"], rel)
                time = lead.find("p", "tp-front-time")
                self.assertEqual((time.attrs["data-en"], time.attrs["data-es"]), B.short_reading_time(pick["lead"]), rel)

                items = front.find("ul", "tp-front-list").find_all("li", "tp-front-item")
                self.assertEqual([i.find("a").attrs["href"] for i in items], [f"{pillar}/{s}/" for s in pick["links"]], rel)
                for slug, item in zip(pick["links"], items):
                    link = item.find("a", "tp-front-link")
                    self.assertTrue(resolves(rel, link.attrs["href"]), rel)
                    self.assertEqual(link.attrs["data-en"], B.decf_title(by_slug[slug]["title"]), rel)
                    self.assertTrue(link.attrs["data-es"].strip(), rel)
                    t = item.find("span", "tp-front-time")
                    self.assertEqual((t.attrs["data-en"], t.attrs["data-es"]), B.short_reading_time(slug), rel)

                n = len(B.NEW_FOLIOS[pillar])  # the count comes from the catalogue
                more = front.find("p", "tp-front-all").find("a")
                self.assertEqual((more.attrs["data-en"], more.attrs["data-es"]), (f"See all {n} essays →", f"Ver los {n} ensayos →"), rel)
                self.assertEqual(more.attrs["href"], f"{pillar}/", rel)
            # The 58 essay cards are on the four hubs, not on the cover.
            self.assertFalse(root.find("main").find_all("a", "tp-rack-card"), rel)

    def test_each_front_standfirst_is_word_for_word_from_its_essay(self) -> None:
        """Grounding rule: the cover writes no teasers. Each lead's standfirst is found in the essay it points to,
        in the language of the page, and both languages of the pair are found in their own essays."""
        for rel, lang in COVERS:
            for pillar, front in zip(PILLARS, page(rel).find_all("section", "tp-front")):
                slug = B.COVER_FRONTS[pillar]["lead"]
                dek = front.find("p", "tp-front-dek")
                self.assertEqual(dek.text(), dek.attrs["data-es" if lang == "es" else "data-en"], rel)
                for attr, prefix in (("data-en", ""), ("data-es", "es-mx/")):
                    shown = dek.attrs[attr]
                    self.assertGreater(len(shown), 40, shown)
                    essay = norm(parse((SRC / prefix / pillar / slug / "index.html").read_text(encoding="utf-8")).text())
                    self.assertIn(norm(shown), essay, f"{rel}: the {attr} standfirst for {slug} is not in that essay: {shown!r}")
                    self.assertNotRegex(shown, r"(?i)^(?:this|these|that|esta|este|estos|estas)\b", shown)
                folio = next(f for f in B.NEW_FOLIOS[pillar] if f["slug"] == slug)
                es_meta = B.get_folio_es_meta(slug, folio, folio["colophon"])
                self.assertEqual(dek.attrs["data-en"], B._standfirst_excerpt(B.decf(B.LONGFORM[slug]["act1_plain_bridge"])), rel)
                self.assertEqual(dek.attrs["data-es"], B._standfirst_excerpt(B.decf(es_meta["plain_es"])), rel)

    def test_each_front_standfirst_lines_up_in_both_languages(self) -> None:
        # Structural only (sentence count, figures, length): a digit-free clause present in one language can
        # pass. The Spanish meaning is checked by the es-MX reviewer, not by this test.
        """The reported fault: the Architecture and Mathematics fronts showed one passage in English and another
        in Spanish (a citation sentence with two DOIs; a sentence about 1994). Both languages come from the
        essay's plain-words pair (act1_plain_bridge and plain_es), and the excerpts must line up: the same
        number of sentences, the same figures, a comparable length, and no citation in either."""
        for rel, _lang in COVERS:
            fronts = page(rel).find_all("section", "tp-front")
            self.assertEqual(len(fronts), len(PILLARS), rel)
            for pillar, front in zip(PILLARS, fronts):
                slug = B.COVER_FRONTS[pillar]["lead"]
                dek = front.find("p", "tp-front-dek")
                en, es_text = dek.attrs.get("data-en", "").strip(), dek.attrs.get("data-es", "").strip()
                self.assertTrue(en and es_text, f"{rel}: {slug} is missing a language")
                self.assertNotEqual(en, es_text, f"{rel}: {slug} shows the English text in Spanish")
                self.assertEqual(
                    len(B._SENTENCE_END_RE.split(en)), len(B._SENTENCE_END_RE.split(es_text)),
                    f"{slug}: a different number of sentences in each language: {en!r} / {es_text!r}",
                )
                self.assertEqual(
                    sorted(re.findall(r"\d+(?:[.,]\d+)?", en)), sorted(re.findall(r"\d+(?:[.,]\d+)?", es_text)),
                    f"{slug}: the figures differ between the languages: {en!r} / {es_text!r}",
                )
                self.assertLess(max(len(en), len(es_text)) / min(len(en), len(es_text)), 1.6, f"{slug}: {en!r} / {es_text!r}")
                for text in (en, es_text):
                    self.assertIsNone(re.search(r"\(\s*[A-ZÁÉÍÓÚ][^()]*\b(?:1[6-9]|20)\d\d\b[^()]*\)", text), f"{slug}: a citation in {text!r}")

    def test_no_cover_standfirst_carries_a_doi(self) -> None:
        """A standfirst is an opening picture, not a reference: none on the cover (the four fronts and every
        slide of the weekly rotation, in both languages) contains "DOI" or a DOI's "10." prefix."""
        doi = re.compile(r"\bDOI\b|\b10\.\d", re.I)
        self.assertIsNotNone(doi.search("(Kubelka 1948, DOI 10.1364/JOSA.38.000448)"))
        self.assertIsNotNone(doi.search("see 10.1016/j.cemconres.2004.12.012"))
        self.assertIsNone(doi.search("About 10 parts in 110.5"))
        for rel, _lang in COVERS:
            root = page(rel)
            deks = root.find_all("p", "tp-front-dek") + root.by_id("tp-featured-edition-desk").find_all("p", "tp-spotlight-dek")
            self.assertEqual(len(deks), len(PILLARS) + len(B.INFORMATICO_SPOTLIGHT_ROTATION), rel)
            for dek in deks:
                for text in (dek.attrs["data-en"], dek.attrs["data-es"], dek.text()):
                    hit = doi.search(text)
                    self.assertIsNone(hit, f"{rel}: {hit.group(0) if hit else ''!r} in the standfirst {text!r}")

    def test_more_to_explore_row_is_plain_names_and_one_line_each(self) -> None:
        names = B.COVER_SECTION_NAMES
        steps = len(B.TIMEGRAVITY_PAGES)
        self.assertEqual(steps, 14)
        expected = [
            ("bounties/", names["bounties"], ("Open problems and prize challenges, explained", "Problemas abiertos y retos con premio, explicados")),
            ("toolchain/", names["toolchain"], ("Open 3D files for small studios", "Archivos 3D abiertos para estudios pequeños")),
            ("timegravity/", names["timegravity"], (
                f"A {steps}-step series · Why a higher clock runs faster",
                f"Una serie de {steps} pasos · Por qué un reloj a mayor altura avanza más rápido",
            )),
        ]
        self.assertEqual(names["bounties"][0], "Unsolved puzzles")
        self.assertEqual(names["toolchain"][0], "For makers: 3D tools")
        for rel, lang in COVERS:
            row = page(rel).find("section", "tp-more")
            heading = row.find("h2")
            self.assertEqual((heading.attrs["data-en"], heading.attrs["data-es"]), ("More to explore", "Más para explorar"), rel)
            items = row.find("ul", "tp-more-list").elements()
            self.assertEqual(len(items), 4, rel)
            for item, (href, name, desc) in zip(items, expected):
                title = item.find("a", "tp-more-title")
                self.assertEqual(title.attrs["href"], href, rel)
                self.assertTrue(resolves(rel, href), rel)
                self.assertEqual((title.attrs["data-en"], title.attrs["data-es"]), name, rel)
                line = item.find("span", "tp-more-desc")
                self.assertEqual((line.attrs["data-en"], line.attrs["data-es"]), desc, rel)
            classics = items[3]
            label = classics.find("span", "tp-more-title")
            self.assertEqual((label.attrs["data-en"], label.attrs["data-es"]), names["classics"], rel)
            links = classics.find("ul", "tp-more-links").find_all("a")
            self.assertEqual([a.attrs["href"] for a in links], ["classics/golf-gti/", "classics/sagrada-familia/", "classics/mini-jcw/"], rel)
            self.assertEqual([a.attrs["data-en"] for a in links], ["the Golf GTI", "La Sagrada Família", "the MINI JCW"], rel)
            for a in links:
                self.assertTrue(resolves(rel, a.attrs["href"]), rel)

    def test_small_links_for_coders_and_for_the_essays_across_scales(self) -> None:
        for rel, lang in COVERS:
            root = page(rel)
            self.assertFalse(root.find_all("a", "tp-track-chip-skills"), rel)
            main = root.find("main")
            self.assertFalse([a for a in main.find("section", "tp-fronts").find_all("a") if a.attrs["href"].startswith("http")], rel)
            links = root.find("p", "tp-cover-coders").find_all("a")
            self.assertEqual([a.attrs["href"] for a in links], ["about/#for-builders", "essays/"], rel)  # each language has its own
            self.assertEqual(links[0].attrs["data-en"], "For builders and coders: use these essays with AI tools →")
            for a in links:
                self.assertTrue(resolves(rel, a.attrs["href"]), rel)
            # The jargon label is replaced by the hub's own words: its title names clocks, stone and living matter,
            # and its standfirst says the same mathematical structures recur at very different sizes.
            self.assertEqual(
                (links[1].attrs["data-en"], links[1].attrs["data-es"]),
                (
                    "Clocks, stone and living matter: the same math at different scales →",
                    "Relojes, piedra y materia viva: las mismas matemáticas a distintas escalas →",
                ),
                rel,
            )
            # (The site footer, which every page shares, still lists the hub by its own title.)
            for block in [c for c in main.elements() if c.tag != "footer"]:
                for text in shown_strings(block):
                    self.assertNotIn("cross-scale", text.casefold(), rel)
                    self.assertNotIn("entre escalas", text.casefold(), rel)
        hub = page("essays/index.html").find("main")
        self.assertIn("Clocks, Stone, and Living Matter", hub.find("h1").attrs["data-en"])
        self.assertIn("the same mathematical structures", hub.find("p", "tp-standfirst").attrs["data-en"])

    def test_no_folio_code_or_machinery_word_in_the_cover_main(self) -> None:
        """Everything in <main> except the hero film's own caption (it names the film and where it plays)."""
        for rel, _lang in COVERS:
            main = page(rel).find("main")
            captions = main.find_all("figcaption", "tp-film-caption")
            self.assertLessEqual(len(captions), 1, rel)
            skip = set()
            for cap in captions:
                self.assertIn("tp-cover-film", cap.parent.classes, rel)
                skip.update(id(n) for n in [cap] + list(cap.walk()))

            strings: list[str] = []

            def gather(node: Node) -> None:
                for attr in ("data-en", "data-es", "alt", "aria-label", "title"):
                    if node.attrs.get(attr):
                        strings.append(node.attrs[attr])
                for child in node.children:
                    if isinstance(child, str):
                        strings.append(child)
                    elif id(child) not in skip and child.tag not in ("script", "style"):
                        gather(child)

            gather(main)
            self.assertGreater(len(strings), 150, rel)
            for text in strings:
                self.assertIsNone(CODE_RE.search(text), f"{rel}: folio code in {text!r}")
                for word in MACHINERY_WORDS:
                    self.assertNotIn(word, text, f"{rel}: {word!r} in {text!r}")

    def test_lower_sections_left_the_cover_and_the_films_shelf_is_absent(self) -> None:
        gone = (
            "tp-toolchain-toolbox", "tp-city-tools", "tp-bounty-crucible", "featured-timegravity", "cult-classics",
            "cross-scale-essays", "films",
        )
        homes = {
            "tp-toolchain-toolbox": "toolchain/index.html", "tp-city-tools": "toolchain/index.html",
            "tp-bounty-crucible": "bounties/index.html", "timegravity-series": "physics/index.html",
            "cult-classics-eng": "engineering/index.html", "cult-classics-arch": "architecture/index.html",
            "cross-scale-essays": "physics/index.html",
        }
        for rel, _lang in COVERS:
            root = page(rel)
            for ident in gone:
                self.assertIsNone(root.by_id(ident), f"{rel}: #{ident} is back on the cover")
            for cls in ("tp-cover-films", "tp-film-link", "tp-films-list", "tp-cover-pillar", "tp-bounty-card", "tp-featured-steps-rail"):
                self.assertFalse(root.find_all(None, cls), f"{rel}: .{cls} is back on the cover")
            # The hero's click-to-play film and its privacy line stay.
            film = root.by_id("film-informatico-intro")
            self.assertIsNotNone(film, rel)
            self.assertEqual(film.find("span", "tp-film-privacy").attrs["data-en"], B.FILM_PRIVACY_EN, rel)
        for prefix in ("", "es-mx/"):
            for ident, home in homes.items():
                self.assertIsNotNone(page(prefix + home).by_id(ident), f"{prefix}{home}: #{ident} should live here")
        films = json.loads((ROOT / "data" / "films.json").read_text(encoding="utf-8"))
        self.assertIsNone(next(f for f in films if f["slug"] == "follow-the-light")["youtube_id"])

    def test_nothing_on_a_front_or_row_is_clamped_or_cut(self) -> None:
        for rel, _lang in COVERS:
            main = page(rel).find("main")
            for block in main.find_all("section", "tp-front") + main.find_all("section", "tp-more"):
                for text in shown_strings(block):
                    self.assertNotIn("…", text, rel)
                    self.assertNotIn("...", text, rel)
        css = " ".join((SRC / "informatico.css").read_text(encoding="utf-8").split())
        block = css[css.index("/* Magazine pass, phase 2"):css.index("/* Essay cards without the box")]
        for cls in FRONT_TEXT_CLASSES + MORE_TEXT_CLASSES + ("tp-fronts", "tp-front", "tp-more-list", "tp-more-item"):
            self.assertIn(f".{cls}", block, cls)
        for banned in ("line-clamp", "text-overflow", "nowrap", "overflow: hidden", "max-height", "-webkit-box"):
            self.assertNotIn(banned, block, f"{banned!r} in the section-front styles")
        # No older rule clamps these classes either.
        for cls in FRONT_TEXT_CLASSES + MORE_TEXT_CLASSES:
            self.assertEqual(css.count(f".{cls}"), block.count(f".{cls}"), f".{cls} is styled outside the phase 2 block")

    def test_section_dividers_use_the_strong_rule(self) -> None:
        css = " ".join((SRC / "informatico.css").read_text(encoding="utf-8").split())
        self.assertIn(
            ".tp-page-cover .tp-featured-edition-desk.tp-this-week, .tp-page-cover .tp-cover-films, .tp-fronts, .tp-more, "
            ".tp-page-cover .tp-puzzle-atelier, .tp-cover-coders { margin: clamp(3rem, 6vw, 5rem) 0 0; "
            "padding: clamp(1.5rem, 3vw, 2.25rem) 0 0; border: 0; border-top: 1px solid var(--tp-rule-strong);",
            css,
        )
        self.assertIn(".tp-front-item { padding: 0.75rem 0; border-top: 1px solid var(--tp-rule); }", css)
        self.assertIn(".tp-masthead.tp-masthead-slim { border-bottom: 1px solid var(--tp-rule); }", css)

    def test_warm_palette_tokens_and_theme_color(self) -> None:
        css = (SRC / "informatico.css").read_text(encoding="utf-8")
        light, rest = css.split('html[data-theme="blueprint"],', 1)
        dark = rest.split("@media (prefers-contrast: more)", 1)[0]
        for token, value in (
            ("--tp-stone", "#f6f1e7"), ("--tp-vellum", "#fbf8f1"), ("--tp-stone-deep", "#e9e1d2"), ("--tp-mortar", "#ece5d7"),
            ("--tp-ink", "#1c1814"), ("--tp-graphite", "#3b352e"), ("--tp-slate", "#5a5248"), ("--tp-minium", "#b0301e"),
            ("--tp-rule", "rgba(28, 24, 20, 0.16)"), ("--tp-rule-strong", "rgba(28, 24, 20, 0.36)"),
        ):
            self.assertIn(f"{token}: {value};", light, token)
        for token, value in (
            ("--tp-stone", "#14110e"), ("--tp-vellum", "#1c1814"), ("--tp-stone-deep", "#26211b"), ("--tp-mortar", "#2c261f"),
            ("--tp-ink", "#f3ede2"), ("--tp-graphite", "#d9d0c2"), ("--tp-slate", "#b3a898"), ("--tp-minium", "#ff9b8a"),
            ("--tp-rule", "rgba(243, 237, 226, 0.16)"), ("--tp-rule-strong", "rgba(243, 237, 226, 0.38)"),
            ("--text-1", "#f3ede2"), ("--ink-primary", "#f3ede2"), ("--ink-secondary", "#d9d0c2"), ("--muted", "#b3a898"),
            ("--bg-dark", "#14110e"), ("--surface-page", "#14110e"), ("--surface-1", "#1c1814"),
        ):
            self.assertIn(f"{token}: {value};", dark, token)

        def luminance(hex_color: str) -> float:
            parts = [int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
            lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in parts]
            return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]

        def contrast(a: str, b: str) -> float:
            hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
            return (hi + 0.05) / (lo + 0.05)

        # WCAG AA for body text (4.5:1) on both the page and the surface colour, in both themes.
        for page_bg, surface, deep, texts in (
            ("#f6f1e7", "#fbf8f1", "#e9e1d2", ("#1c1814", "#3b352e", "#5a5248", "#b0301e")),
            ("#14110e", "#1c1814", "#26211b", ("#f3ede2", "#d9d0c2", "#b3a898", "#ff9b8a")),
        ):
            for fg in texts:
                for bg in (page_bg, surface, deep):
                    self.assertGreaterEqual(contrast(fg, bg), 4.5, f"{fg} on {bg}")
        for rel in ("index.html", "es-mx/index.html", "math/m01/index.html", "physics/index.html", "about/index.html"):
            metas = [m for m in page(rel).find_all("meta") if m.attrs.get("name") == "theme-color"]
            self.assertEqual([m.attrs["content"] for m in metas], ["#f6f1e7"], rel)


class HubPlainWordsTests(unittest.TestCase):
    """The four section hubs and the sections that moved off the cover, in plain words (phase 2)."""

    def test_hub_kickers_and_rack_heads(self) -> None:
        steps = len(B.TIMEGRAVITY_PAGES)
        for pillar in PILLARS:
            n = len(B.NEW_FOLIOS[pillar])
            for prefix, lang in (("", "en"), ("es-mx/", "es")):
                rel = f"{prefix}{pillar}/index.html"
                root = page(rel)
                kicker = root.find("section", "tp-pillar-hero").find("p", "tp-kicker")
                want_en = f"{n} essays" + (f" and a {steps}-step series" if pillar == "physics" else "")
                want_es = f"{n} ensayos" + (f" y una serie de {steps} pasos" if pillar == "physics" else "")
                self.assertEqual((kicker.attrs["data-en"], kicker.attrs["data-es"]), (want_en, want_es), rel)
                rack = root.by_id("all-essays")
                self.assertEqual(rack.attrs["aria-labelledby"], "all-essays-heading", rel)
                head = rack.find("div", "tp-issue-rack-head")
                self.assertFalse(head.find_all("p", "tp-kicker"), f"{rel}: a 'Standalone ... Monographs' kicker is back")
                h2 = root.by_id("all-essays-heading")
                self.assertEqual((h2.attrs["data-en"], h2.attrs["data-es"]), (f"All {n} essays", f"Los {n} ensayos"), rel)
                self.assertEqual(len([c for c in rack.find_all("a", "tp-rack-card") if "data-folio-volume" in c.attrs]), n, rel)
                for text in shown_strings(root.find("section", "tp-pillar-hero")) + shown_strings(head):
                    for word in ("Pillar", "Pilar", "Monograph", "Monografía", "Standalone"):
                        self.assertNotIn(word, text, f"{rel}: {text!r}")

    def test_time_and_gravity_rack_on_physics(self) -> None:
        rows = B._tg_ledger_rows()
        self.assertGreater(rows, 100)
        for prefix in ("", "es-mx/"):
            rel = f"{prefix}physics/index.html"
            rack = page(rel).by_id("timegravity-series")
            kicker = rack.find("p", "tp-kicker")
            self.assertEqual((kicker.attrs["data-en"], kicker.attrs["data-es"]), ("A 14-step series", "Una serie de 14 pasos"), rel)
            h2 = rack.find("h2").find("a")
            self.assertEqual((h2.attrs["data-en"], h2.attrs["data-es"]), B.COVER_SECTION_NAMES["timegravity"], rel)
            stand = rack.find("p", "tp-standfirst")
            self.assertTrue(stand.attrs["data-en"].endswith(f"hold every claim to a {rows}-row offline ledger."), rel)
            self.assertTrue(stand.attrs["data-es"].endswith(f"frente a un registro fuera de línea de {rows} filas."), rel)
            # The Spanish says what the English says: "six strict evidence labels", an offline ledger.
            self.assertIn("six strict evidence labels (including DERIVED (NOT MEASURED))", stand.attrs["data-en"], rel)
            self.assertIn("seis etiquetas estrictas de evidencia (incluida DERIVADO (NO MEDIDO))", stand.attrs["data-es"], rel)
            self.assertNotIn("libro", stand.attrs["data-es"], rel)
            ctas = rack.find("div", "tp-series-rack-ctas").find_all("a")
            self.assertEqual(
                [(a.attrs["data-en"], a.attrs["data-es"]) for a in ctas],
                [
                    ("Enter the Series Hub →", "Ir al índice de la serie →"),
                    ("Begin Step 2 · Everyone Moves at One Rate →", "Empieza en el paso 2 · Todos Avanzamos a un Mismo Ritmo →"),
                ],
                rel,
            )
            self.assertEqual([a.attrs["href"] for a in ctas], ["../timegravity/", "../timegravity/t02/"], rel)
            # The second button names the page it opens by that page's own title, in each language.
            t02 = page(f"{prefix}timegravity/t02/index.html").find("h1")
            self.assertTrue(ctas[1].attrs["data-en"].endswith(f"· {t02.attrs['data-en']} →"), rel)
            self.assertTrue(ctas[1].attrs["data-es"].endswith(f"· {t02.attrs['data-es']} →"), rel)
            self.assertEqual(["tp-cta-primary" in a.classes for a in ctas], [True, False], rel)
            self.assertEqual(len(rack.find_all("a", "tp-rack-card-series")), 14, rel)

    def test_time_and_gravity_step_count_agrees_on_physics_and_cover(self) -> None:
        """The series length is counted once (B._tg_steps) for the /physics/ hub kicker, the rack kicker, the
        standfirst's spelled-out number, each card's "Step i of N", and the cover row. Not covered: the Contents
        drawer label and the /timegravity/ pages, which still state 14 directly."""
        steps = B._tg_steps()
        self.assertEqual(steps, len(B.TIMEGRAVITY_PAGES))
        word_en, word_es = B._number_words(steps)
        for prefix in ("", "es-mx/"):
            rel = f"{prefix}physics/index.html"
            root = page(rel)
            hero = root.find("section", "tp-pillar-hero").find("p", "tp-kicker")
            self.assertTrue(hero.attrs["data-en"].endswith(f"and a {steps}-step series"), rel)
            self.assertTrue(hero.attrs["data-es"].endswith(f"y una serie de {steps} pasos"), rel)
            rack = root.by_id("timegravity-series")
            kicker = rack.find("p", "tp-kicker")
            self.assertEqual((kicker.attrs["data-en"], kicker.attrs["data-es"]), (f"A {steps}-step series", f"Una serie de {steps} pasos"), rel)
            stand = rack.find("p", "tp-standfirst")
            self.assertIn(f"A guided {word_en}-step inquiry", stand.attrs["data-en"], rel)
            self.assertIn(f"Una investigación guiada de {word_es} pasos", stand.attrs["data-es"], rel)
            ids = [c.find("span", "tp-rack-id") for c in rack.find_all("a", "tp-rack-card-series")]
            self.assertEqual(len(ids), steps, rel)
            for i, node in enumerate(ids, 1):
                self.assertTrue(node.attrs["data-en"].startswith(f"Step {i} of {steps} · "), node.attrs["data-en"])
                self.assertTrue(node.attrs["data-es"].startswith(f"Paso {i} de {steps} · "), node.attrs["data-es"])
        # A shorter series changes every one of them together; a hand-typed "14" or "fourteen" would not follow.
        saved = B.TIMEGRAVITY_TRACK_MAP
        B.TIMEGRAVITY_TRACK_MAP = saved[:-1]
        try:
            shorter = parse(B.render_timegravity_series_rack(".."))
            self.assertEqual(B._tg_steps(), steps - 1)
            w_en, w_es = B._number_words(steps - 1)
            texts = " ".join(shown_strings(shorter))
            self.assertIn(f"A {steps - 1}-step series", texts)
            self.assertIn(f"A guided {w_en}-step inquiry", texts)
            self.assertIn(f"Una investigación guiada de {w_es} pasos", texts)
            self.assertIn(f"Step {steps - 1} of {steps - 1} · ", texts)
            self.assertNotIn(f"of {steps}", texts)
            self.assertNotIn(f"de {steps} ", texts)
            self.assertNotIn(word_en, texts)
            self.assertNotIn(word_es, texts)
        finally:
            B.TIMEGRAVITY_TRACK_MAP = saved
        with self.assertRaises(ValueError):
            B._number_words(99)

    def test_toolbox_heading_and_sentences_say_what_the_site_ships(self) -> None:
        """The heading promised "a Check for Each File". What exists is one checking script per CAD Folio, which
        checks that folio's file set and fails under a planted defect; the heading now says that, and this test
        holds it to the catalogue and to the scripts on disk."""
        self.assertIn("a Checking Script for Each CAD Folio", B.TOOLBOX_HEADING_EN)
        self.assertIn("un Script de Revisión para Cada Folio CAD", B.TOOLBOX_HEADING_ES)
        self.assertIn("Archivos Descargables STEP, 3MF, GLB y DXF", B.TOOLBOX_HEADING_ES)
        for word in ("Each File", "Cada Archivo", "Check for"):
            self.assertNotIn(word, B.TOOLBOX_HEADING_EN + B.TOOLBOX_HEADING_ES)
        formats: set[str] = set()
        for tool in B.TOOLCHAIN_FOLIOS:
            scripts = list((ROOT / "skills" / "toolchain" / tool["slug"]).glob("verify_*.py"))
            self.assertEqual(len(scripts), 1, f"{tool['slug']}: one checking script per CAD Folio")
            self.assertIn("--planted-defect", scripts[0].read_text(encoding="utf-8"), tool["slug"])
            self.assertTrue(tool["formats"], tool["slug"])
            formats.update(tool["formats"])
        self.assertEqual(formats, {"step", "3mf", "glb", "dxf"})  # the four formats the heading names
        es_sentence = (
            "Cada Folio CAD incluye el script de Python que genera sus archivos, archivos neutros descargables "
            "(.glb, .step, .3mf, .dxf) con una lista de sumas de verificación, un visor 3D en vivo en el navegador, un script "
            "de revisión que debe fallar cuando se le introduce un defecto a propósito y su SKILL.md portátil."
        )
        for prefix in ("", "es-mx/"):
            rel = f"{prefix}toolchain/index.html"
            root = page(rel)
            link = root.by_id("toolchain-toolbox-heading").find("a")
            self.assertEqual((link.attrs["data-en"], link.attrs["data-es"]), (B.TOOLBOX_HEADING_EN, B.TOOLBOX_HEADING_ES), rel)
            section = root.by_id("tp-toolchain-toolbox").find("p", "tp-standfirst")
            self.assertTrue(section.attrs["data-es"].endswith(es_sentence), rel)
            self.assertIn("a checking script that must fail when a defect is planted", section.attrs["data-en"], rel)
            hero = root.find("section", "tp-pillar-hero")
            hook = hero.find("p", "tp-standfirst").attrs["data-es"]
            self.assertIn("un visor 3D en vivo en el navegador, un script de revisión que debe fallar cuando se le introduce un defecto a propósito y su SKILL.md portátil.", hook, rel)
            self.assertIn("archivos neutros descargables", hook, rel)
            # One term for small studios in the page's own headings and sentences (essay titles keep theirs).
            for node in (hero.find("h1"), hero.find("p", "tp-kicker"), link, root.by_id("tp-toolchain-toolbox").find("p", "tp-kicker")):
                self.assertNotIn("Pequeños Estudios", node.attrs["data-es"], rel)
            self.assertIn("Pequeños Despachos", hero.find("h1").attrs["data-es"], rel)
            charters = [n.attrs["data-es"] for n in root.find_all("span") if "FOSS" in n.attrs.get("data-es", "")]
            self.assertGreaterEqual(len(charters), 2, rel)
            for text in charters:
                self.assertTrue(text.startswith("Carta Global Legal y FOSS:"), text[:60])
        for slug in ("x01", "x08"):
            text = (SRC / "es-mx" / "toolchain" / slug / "index.html").read_text(encoding="utf-8")
            self.assertIn("Carta Global Legal y FOSS (GCC-01", text, slug)
            self.assertNotIn("Carta Legal y FOSS Global", text, slug)

    def test_bounties_standfirst_names_the_same_things_in_both_languages(self) -> None:
        for prefix in ("", "es-mx/"):
            rel = f"{prefix}bounties/index.html"
            stand = page(rel).by_id("tp-bounty-crucible").find("p", "tp-standfirst")
            en, es_text = stand.attrs["data-en"], stand.attrs["data-es"]
            self.assertTrue(es_text.startswith("Revisado el 2026-11-15 contra los avisos vigentes de cada certamen: seis "), rel)
            self.assertTrue(en.startswith("Checked on 2026-11-15 against the competitions' current notices: six "), rel)
            for name in ("Global Cooling 2021", "XPRIZE Carbon 2025", "Holcim 2025", "AIMO", "Metriq", "PhysLean", "Unitary Foundation", "B.01–B.06", "#30"):
                self.assertIn(name, en, rel)
                self.assertIn(name, es_text, rel)
            self.assertNotIn("Cooling Prize 2021", es_text, rel)
            self.assertIn("microbecas continuas de Unitary Foundation", es_text, rel)
            self.assertTrue(es_text.endswith("cada uno con un laboratorio contrafactual en vivo y un verificador en Python sin dependencias."), rel)
            self.assertTrue(en.endswith("each paired with a live counterfactual workbench and zero-dependency Python verifier."), rel)
            self.assertEqual(sorted(re.findall(r"\d+", en)), sorted(re.findall(r"\d+", es_text)), rel)

    def test_builders_box_sits_below_the_essays_under_a_plain_heading(self) -> None:
        """The quick-start steps ("Run python ...") opened the Bounties and Toolbox hubs, above the essays. They
        now follow the essay cards, under a heading a first-time reader can skip past."""
        headings = {
            "bounties": ("For builders: run the examples yourself", "Para quienes programan: corre los ejemplos tú mismo"),
            "toolchain": (
                "For builders: open the files and run the scripts yourself",
                "Para quienes construyen y programan: abre los archivos y corre los scripts tú mismo",
            ),
        }
        for hub, want in headings.items():
            for prefix in ("", "es-mx/"):
                rel = f"{prefix}{hub}/index.html"
                main = page(rel).find("main")
                hero = main.find("section", "tp-pillar-hero")
                self.assertFalse(hero.find_all("div", "tp-studio-quickstart"), f"{rel}: the quick-start box is back in the hero")
                order = [n for n in main.walk()]
                box = main.find("section", "tp-builders-box")
                self.assertIsNotNone(box, rel)
                cards = [c for c in main.find_all("a", "tp-rack-card") if c.attrs.get("data-folio-slug")]
                self.assertGreaterEqual(len(cards), 6, rel)
                self.assertGreater(order.index(box), order.index(cards[-1]), f"{rel}: the box is above the essays")
                h2 = box.find("h2")
                self.assertEqual((h2.attrs["data-en"], h2.attrs["data-es"]), want, rel)
                self.assertEqual(box.attrs["aria-labelledby"], h2.attrs["id"], rel)
                quick = box.find("div", "tp-studio-quickstart")
                # The content is kept: the badge, three steps, and the command.
                self.assertEqual(len(quick.find_all("div", "tp-studio-step-card")), 3, rel)
                self.assertEqual(len(quick.find_all("h3", "tp-studio-step-title")), 3, rel)
                self.assertFalse(quick.find_all("h2"), f"{rel}: step titles outrank the box heading")
                self.assertIn("QUICK-START", quick.find("span", "tp-studio-quickstart-badge").attrs["data-en"], rel)
                self.assertIn("run_all_bounties.py" if hub == "bounties" else "run_all_toolchain.py", quick.text(), rel)
                for text in shown_strings(quick):
                    self.assertNotRegex(text, r"(?i)\) below\b|\babajo\b|a continuación", f"{rel}: the essays are above the box now: {text!r}")

    def test_hub_cards_are_not_cut_and_show_only_the_short_code(self) -> None:
        """Card blurbs on the hubs ended in "..." at three lines. Nothing clamps them now, and the Bounties and
        Toolbox cards show B.01 or X.06 without the internal id (BOUNTY-M1, TOOL-PHYS-MATH-1)."""
        css = " ".join((SRC / "informatico.css").read_text(encoding="utf-8").split())
        # Every rule whose selector list mentions a card title or blurb, however it is written
        # (".a, .tp-rack-dek", ".x .tp-rack-dek:not(y)"), may not clip text.
        found = 0
        for head, body in re.findall(r"([^{}]+)\{([^{}]*)\}", re.sub(r"/\*.*?\*/", "", css)):
            if "tp-rack-dek" in head or "tp-rack-title" in head:
                found += 1
                for banned in ("line-clamp", "text-overflow", "-webkit-box", "overflow: hidden", "max-height", "nowrap"):
                    self.assertNotIn(banned, body, f"{head.strip()} {banned}")
        self.assertGreater(found, 2)
        for hub in ("physics", "bounties", "toolchain", "engineering", "architecture", "math"):
            for prefix in ("", "es-mx/"):
                rel = f"{prefix}{hub}/index.html"
                cards = page(rel).find("main").find_all("a", "tp-rack-card")
                self.assertGreaterEqual(len(cards), 6, rel)
                for card in cards:
                    for cls in ("tp-rack-title", "tp-rack-dek"):
                        for node in card.find_all(None, cls):
                            for text in (node.text(), node.attrs.get("data-en", ""), node.attrs.get("data-es", "")):
                                self.assertFalse(text.rstrip().endswith(("...", "…")), f"{rel}: {text!r}")
        for hub, letter in (("bounties", "B"), ("toolchain", "X")):
            for prefix in ("", "es-mx/"):
                rel = f"{prefix}{hub}/index.html"
                cards = [c for c in page(rel).find("main").find_all("a", "tp-rack-card") if c.attrs.get("data-folio-slug")]
                for card in cards:
                    slug = card.attrs["data-folio-slug"]
                    self.assertEqual(card.attrs["href"], f"./{slug}/", rel)
                    self.assertEqual(card.find("span", "tp-rack-id").text(), f"{letter}.{slug[1:]}", rel)
                    for text in shown_strings(card.find("span", "tp-rack-top")):
                        self.assertNotRegex(text, r"BOUNTY-|TOOL-", f"{rel}: {text!r}")

    def test_section_headings_that_link_look_like_headings(self) -> None:
        """The "Special feature" heading on /bounties/ (and the Toolbox section heading) is an h2 around a link;
        it was drawn as a default blue underlined link."""
        css = " ".join((SRC / "informatico.css").read_text(encoding="utf-8").split())
        self.assertIn(".tp-bounty-header .tp-h2 a { color: inherit; text-decoration: none; }", css)
        self.assertIn(".tp-bounty-header .tp-h2 a:hover, .tp-bounty-header .tp-h2 a:focus-visible { text-decoration: underline; }", css)
        for rel, ident in (("bounties/index.html", "bounty-crucible-heading"), ("toolchain/index.html", "toolchain-toolbox-heading")):
            h2 = page(rel).by_id(ident)
            self.assertEqual((h2.tag, "tp-h2" in h2.classes, "tp-bounty-header" in h2.parent.classes), ("h2", True, True), rel)
            self.assertIsNotNone(h2.find("a"), rel)

    def test_moved_sections_read_in_plain_words_and_keep_their_notices(self) -> None:
        for prefix, lang in (("", "en"), ("es-mx/", "es")):
            tool_rel = f"{prefix}toolchain/index.html"
            tool = (SRC / tool_rel).read_text(encoding="utf-8")
            for phrase in ("make_x01.py..make_x08.py", "SHA-256 manifest", "manifiesto SHA-256", "Byte-Level Verifiers &amp; Small-Studio Skills", "GCC-01"):
                self.assertNotIn(phrase, tool, f"{tool_rel}: {phrase!r}")
            self.assertIn(B.esc(B.BOUNDARY_ES if lang == "es" else B.BOUNDARY_EN), tool, tool_rel)
            self.assertIn(
                "Los archivos no afirman cumplir ningún reglamento de construcción" if lang == "es"
                else "The files make no claim of compliance with any building code",
                tool, tool_rel,
            )
            bounty_rel = f"{prefix}bounties/index.html"
            bounty = (SRC / bounty_rel).read_text(encoding="utf-8")
            for phrase in ("bounty_crucible_council_ledger.json", "Reproducible Harnesses", "Six Problem Folios"):
                self.assertNotIn(phrase, bounty, f"{bounty_rel}: {phrase!r}")
            self.assertIn(B.esc(B.BOUNTY_BOUNDARY_ES if lang == "es" else B.BOUNTY_BOUNDARY_EN), bounty, bounty_rel)
            self.assertIn(B.esc(B.BOUNTY_BOUNDARY_EN), B.bounty_boundary_html())
        self.assertEqual(
            B.BOUNTY_BOUNDARY_EN,
            "Independent study, not a prize entry. Informatico.ai has not won or been awarded any prize, bounty or award "
            "named on this page, and is not affiliated with or endorsed by their organizers. PASS means the folio's own worked "
            "example is consistent with the formulas it cites; it is not a judgment by any prize.",
        )
        # The dead release-queue strings are gone from the builder, and no page says them.
        source = (ROOT / "tools" / "build_longform_folios.py").read_text(encoding="utf-8")
        for dead in ("gate_en", "gate_es", "Gated by build_timegravity.py", "INFORMATICO_RELEASE_SCHEDULE", "render_cover_timegravity_feature"):
            self.assertNotIn(dead, source, dead)

    def test_orphan_comments_are_gone_and_the_cover_figure_rule_is_kept_on_purpose(self) -> None:
        """Comments that described removed cover parts are gone from the stylesheet and the modules. The
        .tp-cover-figure rules were also reported as dead, but they are not: the builder still writes that figure
        on / and /about/ whenever a film has no YouTube id (tests/test_films.py renders both that way), so the
        rules stay while the builder can emit the class, and must go when it no longer can."""
        css = (SRC / "informatico.css").read_text(encoding="utf-8")
        bundle = (ROOT / "tools" / "folios" / "css_bundle.py").read_text(encoding="utf-8")
        for dead in (
            "Above-the-Fold 6-Track", "Skills Navigator Strip", "One grid cell for the pillar's links",
            "Cover Featured Series Essay-Showcase", "#featured-timegravity", "then the tiles", "Section tiles:",
            "two-line deck",
        ):
            self.assertNotIn(dead, css, dead)
            self.assertNotIn(dead, bundle, dead)
        module = (SRC / "modules" / "physics-discovery-crucible.mjs").read_text(encoding="utf-8")
        self.assertNotIn("on cover", module)
        self.assertIn("category filter bar on /bounties/", module)
        builder = (ROOT / "tools" / "build_longform_folios.py").read_text(encoding="utf-8")
        emitted = '<figure class="tp-cover-figure">' in builder
        self.assertEqual(emitted, ".tp-cover-figure" in css, "the .tp-cover-figure rules and the builder's fallback figure go together")
        self.assertTrue(emitted)
        for rel in ("index.html", "es-mx/index.html", "about/index.html"):  # films are live, so no page shows the fallback
            self.assertFalse(page(rel).find_all("figure", "tp-cover-figure"), rel)

    def test_dead_cover_styles_are_gone(self) -> None:
        css = (SRC / "informatico.css").read_text(encoding="utf-8") + (SRC / "timegravity.css").read_text(encoding="utf-8")
        for cls in (
            "tp-featured-desk-head", "tp-featured-desk-controls", "tp-featured-desk-grid", "tp-spotlight-pill", "tp-spotlight-step-btn",
            "tp-spotlight-counter", "tp-spotlight-badge", "tp-spotlight-law", "tp-release-", "tp-track-chip", "tp-cover-pillar",
            "tp-cover-row", "tp-cover-hook", "tp-cover-track-strip", "tp-featured-series-", "tp-featured-step",
        ):
            self.assertNotIn(cls, css, cls)
            for rel in ("index.html", "es-mx/index.html", "physics/index.html", "timegravity/index.html", "essays/index.html"):
                used = {c for n in page(rel).walk() for c in n.classes}
                self.assertFalse([c for c in used if c == cls or (cls.endswith("-") and c.startswith(cls)) or c.startswith(cls + "-")], f"{rel}: {cls}")


class ThisWeekTests(unittest.TestCase):
    def test_this_week_and_coming_next_show_no_machinery(self) -> None:
        for rel, lang in COVERS:
            desk = page(rel).by_id("tp-featured-edition-desk")
            self.assertIsNotNone(desk, rel)
            headings = [(h.attrs["data-en"], h.attrs["data-es"]) for h in desk.find_all("h2")]
            self.assertEqual(headings, [("This week’s essay", "El ensayo de la semana"), ("Read next", "Lo que sigue")], rel)
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
                # The module copies a slide's href into "Start reading" only when it matches this pattern.
                self.assertRegex(title.attrs["href"], r"^(?:\.\.?/)*[a-z0-9-]+(?:/[a-z0-9-]+)*/$", rel)
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
                # The cover shows no heading for the excerpt to lean on, so it must not open by pointing back.
                self.assertNotRegex(
                    shown, r"(?i)^(?:this|these|that|esta|este|estos|estas)\b|^to (?:picture|see|imagine) (?:this|these)\b",
                    f"{rel}: the standfirst for {href} opens by pointing back at something the cover does not show",
                )

    def test_standfirst_excerpt_only_quotes(self) -> None:
        self.assertEqual(B._standfirst_excerpt("In plain words, a grid is a bicycle. It rolls. It stops."), "A grid is a bicycle. It rolls.")
        self.assertEqual(B._standfirst_excerpt("En palabras sencillas, una red es una bicicleta. Rueda."), "Una red es una bicicleta. Rueda.")
        self.assertEqual(B._standfirst_excerpt("To picture this mystery, imagine a car. It turns."), "Imagine a car. It turns.")
        self.assertEqual(B._standfirst_excerpt("One  sentence only"), "One sentence only")
        long_second = "Short first. " + "x" * 300 + "."
        self.assertEqual(B._standfirst_excerpt(long_second), "Short first.")
        self.assertEqual(B._standfirst_excerpt("About 1.09 parts. Is it physics? Yes."), "About 1.09 parts. Is it physics?")
        # The reported cut: "... calcite crystal network (Cultrone et al." on the Architecture front.
        self.assertEqual(
            B._standfirst_excerpt("Paint is a mirror. Lime turns to calcite (Cultrone et al. 2004). It hardens."),
            "Paint is a mirror. Lime turns to calcite (Cultrone et al. 2004).",
        )
        self.assertEqual(B._standfirst_excerpt("Arches stand. J. Heyman said so. Yes."), "Arches stand. J. Heyman said so.")

    def test_standfirst_excerpt_does_not_stop_at_an_abbreviation(self) -> None:
        cases = (
            ("Mide aprox. 5 m de alto. Es alto. Fin.", "Mide aprox. 5 m de alto. Es alto."),
            ("It is approx. 5 m tall. It is tall. End.", "It is approx. 5 m tall. It is tall."),
            ("Usa metal, p. ej. acero o cobre. Sirve. Fin.", "Usa metal, p. ej. acero o cobre. Sirve."),
            ("Usa metal (ej. acero) siempre. Sirve. Fin.", "Usa metal (ej. acero) siempre. Sirve."),
            ("En EE. UU. se usa mucho. Sirve. Fin.", "En EE. UU. se usa mucho. Sirve."),
            ("El Dr. Shor lo vio. Sirve. Fin.", "El Dr. Shor lo vio. Sirve."),
            ("El Sr. Paz lo vio. Sirve. Fin.", "El Sr. Paz lo vio. Sirve."),
            ("La Sra. Ruiz lo vio. Sirve. Fin.", "La Sra. Ruiz lo vio. Sirve."),
            ("See Fig. 3 for the arch. It stands. End.", "See Fig. 3 for the arch. It stands."),
            ("Rule No. 5 holds here. It stands. End.", "Rule No. 5 holds here. It stands."),
            ("La regla núm. 5 vale aquí. Sirve. Fin.", "La regla núm. 5 vale aquí. Sirve."),
            ("Stone, brick, etc. are heavy. They stand. End.", "Stone, brick, etc. are heavy. They stand."),
            ("Arches (cf. Heyman) stand. They last. End.", "Arches (cf. Heyman) stand. They last."),
        )
        for text, want in cases:
            self.assertEqual(B._standfirst_excerpt(text), want, text)
        # "No." is an abbreviation only before a number; on its own it is a sentence.
        self.assertEqual(B._standfirst_excerpt("Is it physics? No. It is not. End."), "Is it physics? No.")
        # The box labels are dropped in both languages.
        self.assertEqual(B._standfirst_excerpt("Everyday picture: shiny paint is a mirror. It glares. End."), "Shiny paint is a mirror. It glares.")
        self.assertEqual(B._standfirst_excerpt("Imagen cotidiana: la pintura es un espejo. Brilla. Fin."), "La pintura es un espejo. Brilla.")

    def test_standfirst_excerpt_fails_closed_on_an_overlong_first_sentence(self) -> None:
        """A first sentence longer than the limit means a paragraph with no recognised full stop. The build stops
        there; it does not print the paragraph or cut it."""
        with self.assertRaises(ValueError):
            B._standfirst_excerpt("word " * 80 + "end. Short.")
        with self.assertRaises(ValueError):
            B._standfirst_excerpt("Short enough here. Second.", max_chars=10)
        self.assertEqual(B._standfirst_excerpt("x" * 280), "x" * 280)
        for item in B.INFORMATICO_SPOTLIGHT_ROTATION:  # every cover feature fits
            story = B._spotlight_story(item)
            self.assertLessEqual(max(len(story["stand_en"]), len(story["stand_es"])), 280, item["code"])

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
            self.assertEqual((link.attrs["data-en"], link.attrs["data-es"]), ("Agent Skills & Verifiers on GitHub →", "Skills de IA y verificadores en GitHub →"), rel)


class EssayCardTests(unittest.TestCase):
    # The cards left the cover in phase 2: each essay has one card per language, on its section's hub.
    HUBS = [(f"{prefix}{p}/index.html", lang) for p in PILLARS for prefix, lang in (("", "en"), ("es-mx/", "es"))]

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
        self.assertEqual(seen, 2 * sum(len(v) for v in B.NEW_FOLIOS.values()))

    def test_hub_card_titles_do_not_open_with_a_code(self) -> None:
        """Bounties and Toolbox hubs: the code sits in the small meta line, the title is the title."""
        for rel in ("bounties/index.html", "es-mx/bounties/index.html", "toolchain/index.html", "es-mx/toolchain/index.html"):
            cards = [c for c in page(rel).find_all("a", "tp-rack-card") if c.attrs.get("data-folio-slug")]
            self.assertGreaterEqual(len(cards), 6, rel)
            for card in cards:
                title = card.find("strong", "tp-rack-title")
                for value in (title.attrs["data-en"], title.attrs["data-es"]):
                    self.assertIsNone(CODE_RE.match(value), f"{rel}: {value!r}")
                self.assertRegex(card.find("span", "tp-rack-id").text(), r"^[BX]\.\d{2}$", rel)

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
        self.assertIn("font-family: var(--font-serif", last_rule(".tp-front-title {"))
        self.assertIn("font-family: var(--font-serif", last_rule(".tp-front-link {"))
        # Phase 2: no box around a card; the picture keeps soft corners.
        card = last_rule(".tp-body .tp-rack-card {")
        self.assertIn("border-width: 0", card)
        self.assertIn("background-color: transparent", card)
        self.assertIn("border-radius: 6px", last_rule(".tp-body .tp-rack-thumb-wrap {"))

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
DAY_MS = 24 * 3600 * 1000
MONDAY_SHIFT_MS = 3 * DAY_MS  # the epoch is a Thursday; weeks turn over on Monday 00:00 UTC
BOXES_JS = """() => {
  const box = (sel) => { const r = document.querySelector(sel).getBoundingClientRect(); return {top: r.top, bottom: r.bottom, left: r.left, right: r.right}; };
  return {
    h1: box('#cover-heading'), deck: box('.tp-cover-hero .tp-standfirst'), start: box('[data-spotlight-start]'),
    film: box('.tp-cover-film'), privacy: box('.tp-film-privacy'), desk: box('#tp-featured-edition-desk'),
    fronts: box('.tp-fronts'), more: box('.tp-more'),
    frontBoxes: [...document.querySelectorAll('.tp-front')].map((el) => { const r = el.getBoundingClientRect(); return {left: r.left, top: r.top, width: r.width}; }),
    scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth,
    clipped: [...document.querySelectorAll('.tp-fronts *, .tp-more *')]
      .filter((el) => {
        if (el.tagName === 'IMG') return false;
        const cs = getComputedStyle(el);
        return el.scrollWidth > el.clientWidth + 1 && cs.display !== 'inline'
          || cs.textOverflow === 'ellipsis' || cs.webkitLineClamp !== 'none' || cs.whiteSpace === 'nowrap' || cs.overflow === 'hidden';
      }).map((el) => el.className + ': ' + el.textContent.trim().slice(0, 40)),
    images: [...document.querySelectorAll('.tp-front-img')].map((i) => ({h: i.getBoundingClientRect().height, w: i.getBoundingClientRect().width})),
    rules: ['#tp-featured-edition-desk', '.tp-fronts', '.tp-more'].map((sel) => { const cs = getComputedStyle(document.querySelector(sel)); return [cs.borderTopWidth, cs.borderTopStyle]; }),
    textLinks: [...document.querySelectorAll('.tp-cover-ctas .tp-cta:not(.tp-cta-primary), .tp-front-all a')].map((el) => { const cs = getComputedStyle(el); return [cs.textDecorationLine, cs.borderTopWidth, cs.backgroundColor]; }),
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

    def test_phone_first_screen_is_headline_deck_and_start_reading_then_film_then_fronts(self) -> None:
        for route in ("", "es-mx/"):
            ctx, tab, problems = self._open(route, PHONE, mobile=True)
            try:
                tab.wait_for_function("!document.querySelector('.tp-film-privacy').hasAttribute('hidden')")
                b = tab.evaluate(BOXES_JS)
                self.assertLess(b["h1"]["bottom"], b["deck"]["top"] + 1, route)
                self.assertLess(b["deck"]["bottom"], b["start"]["top"] + 1, route)
                self.assertLessEqual(b["start"]["bottom"], PHONE["height"], f"{route}: Start reading is below the first screen")
                self.assertLess(b["start"]["bottom"], b["film"]["top"], f"{route}: the film is above Start reading")
                self.assertGreater(b["privacy"]["bottom"] - b["privacy"]["top"], 10, f"{route}: the privacy line is not shown")
                self.assertLess(b["privacy"]["bottom"], b["desk"]["top"] + 1, route)
                self.assertLess(b["film"]["bottom"], b["desk"]["top"] + 1, f"{route}: this week's essay is above the film")
                self.assertLess(b["desk"]["bottom"], b["fronts"]["top"] + 1, route)
                self.assertLess(b["fronts"]["bottom"], b["more"]["top"] + 1, route)
                self.assertLessEqual(b["scrollWidth"], b["clientWidth"], f"{route}: the page scrolls sideways")
                self.assertEqual(b["clipped"], [], f"{route}: text on a section front or row is cut off")
                # One column on a phone: the four fronts stack.
                self.assertEqual(len({round(f["left"]) for f in b["frontBoxes"]}), 1, route)
                self.assertEqual(len(b["frontBoxes"]), 4, route)
                self.assertEqual(problems, [], route)
            finally:
                ctx.close()

    def test_desktop_keeps_the_film_beside_the_headline(self) -> None:
        ctx, tab, problems = self._open("", DESKTOP)
        try:
            b = tab.evaluate(BOXES_JS)
            self.assertGreater(b["film"]["left"], b["deck"]["right"], "the film is not in the right column")
            # No wide empty band between the words and the film (it was over 400 px at this width).
            self.assertLess(b["film"]["left"] - max(b["h1"]["right"], b["deck"]["right"]), 160, b)
            self.assertGreater(b["film"]["right"] - b["film"]["left"], 640, "the film does not fill its column")
            self.assertLess(b["film"]["top"], b["start"]["bottom"])
            self.assertLessEqual(b["start"]["bottom"], DESKTOP["height"])
            self.assertEqual(b["clipped"], [], "text on a section front or row is cut off")
            # Two by two at this width, each lead picture drawn 16:9, one visible hairline above each cover section.
            lefts = sorted({round(f["left"]) for f in b["frontBoxes"]})
            self.assertEqual(len(lefts), 2, b["frontBoxes"])
            self.assertEqual([round(f["left"]) for f in b["frontBoxes"]], [lefts[0], lefts[1], lefts[0], lefts[1]])
            for img in b["images"]:
                self.assertAlmostEqual(img["w"] / img["h"], 16 / 9, delta=0.02)
            self.assertEqual(b["rules"], [["1px", "solid"]] * 3)
            for line, border, background in b["textLinks"]:
                self.assertEqual((line, border, background), ("underline", "0px", "rgba(0, 0, 0, 0)"))
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
                active = ((s["now"] + MONDAY_SHIFT_MS) // WEEK_MS) % total
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
                  const D = 24 * 3600 * 1000;
                  const MON = 4 * D; // Monday 5 January 1970, 00:00 UTC
                  return {
                    slots: [0, MON - 1, MON, MON + W - 1, MON + W, MON + 9 * W].map((t) => m.computeWeekSlot(9, t)),
                    weekday: [MON, MON + 9 * W, Date.UTC(2026, 10, 30)].map((t) => new Date(t).getUTCDay()),
                    turnover: [Date.UTC(2026, 10, 29, 23, 59), Date.UTC(2026, 10, 30, 0, 0)].map((t) => m.computeWeekSlot(9, t)),
                    guard: [m.computeWeekSlot(0, W), m.computeWeekSlot(NaN, W), m.computeWeekSlot(9, -5)],
                    next: [m.comingNextSlots(0, 9), m.comingNextSlots(7, 9), m.comingNextSlots(8, 9), m.comingNextSlots(0, 3), m.comingNextSlots(0, 1)],
                  };
                }"""
            )
            self.assertEqual(got["slots"], [0, 0, 1, 1, 2, 1])
            self.assertEqual(got["weekday"], [1, 1, 1])  # every turnover instant is a Monday
            self.assertNotEqual(got["turnover"][0], got["turnover"][1], "the essay must change at Monday 00:00 UTC")
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
        for route in ("engineering/", "architecture/"):
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
            after = tab.evaluate(CARDS_JS)
            empty = [c["slug"] for c in after if c["wrapShown"] and c["imgOk"] is False]
            self.assertEqual(empty, [], "a card shows an image box with no picture in it")
            # Only the picture we broke may turn its card into a text card: a lazy image must never be caught early.
            self.assertEqual([c["slug"] for c in after if c["noimg"]], ["a12"])
            self.assertEqual(problems, [])
        finally:
            ctx.close()


if __name__ == "__main__":
    unittest.main()
