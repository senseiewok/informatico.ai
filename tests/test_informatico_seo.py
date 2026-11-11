"""informatico.ai search fixes (council SEO review, 2026-11-04).

Pins what the review found and what fixed it:
  1. Spanish had no address of its own: ?lang=es served the English HTML. Now every page has a static Spanish twin
     under /es-mx/ with Spanish text in the HTML, its own canonical and a reciprocal hreflang pair.
  2. Titles and descriptions were cut at a fixed width ("...membranes—maintaining.") and ended with an off-topic
     "Research, not medical advice." Now they come from tools/folios/seo_copy.py, written per essay, within budget.
  3. JSON-LD gains author, dates, image, a per-page inLanguage and a breadcrumb trail; pages gain Twitter cards.
  4. senseiewok.ai/research/ duplicates and old ?lang=es links redirect (deploy/htaccess.txt section 4c), and
     informatico.ai has its own 404 page.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
RESEARCH = SRC / "research"
sys.path.insert(0, str(ROOT / "tools"))

import build_longform_folios as builder  # noqa: E402
from folios.seo_copy import BOUNTY_SEO, FOLIO_SEO, HUB_SEO, PILLAR_SEO  # noqa: E402

SITE = "https://informatico.ai/"
PILLARS = ("engineering", "architecture", "physics", "math")
FORMULA = re.compile(r"[=√∂²³∑∫δ_^]|\bexp\(")
# A description that stops on one of these words was cut, not written.
DANGLING = {"a", "an", "the", "and", "or", "of", "to", "in", "with", "by", "for", "under", "y", "de", "del", "la", "el", "los", "las", "en", "con", "por"}


class Head(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self._in_title, self.meta, self.links, self.ld, self._in_ld, self.html_lang = "", False, {}, [], [], False, None
        self.refs: list[tuple[str, str]] = []
        self.h1: list[str] = []
        self._in_h1 = False
        self._head_done = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.html_lang = a.get("lang")
        if tag == "title" and not self._head_done:
            self._in_title = True
        if tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key] = a.get("content")
        if tag == "link":
            self.links.append(a)
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True
            self.ld.append("")
        if tag == "h1":
            self._in_h1 = True
            self.h1.append("")
        for name in ("href", "src", "data-plate-prefix", "data-audio-src", "data-audio-src-es"):
            if a.get(name) is not None:
                self.refs.append((name, a[name]))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "head":
            self._head_done = True
        if tag == "script":
            self._in_ld = False
        if tag == "h1":
            self._in_h1 = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_ld:
            self.ld[-1] += data
        if self._in_h1:
            self.h1[-1] += data


def parse(path: Path) -> Head:
    h = Head()
    h.feed(path.read_text(encoding="utf-8"))
    return h


def pages() -> list[tuple[str, Path, Path]]:
    """(path, English file, Spanish file) for every page: cover, 4 pillar hubs, 48 essays, bounties hub, 6 bounty folios."""
    out = [("", RESEARCH / "index.html", RESEARCH / "es-mx" / "index.html")]
    for p in PILLARS:
        out.append((f"{p}/", RESEARCH / p / "index.html", RESEARCH / "es-mx" / p / "index.html"))
        for slug in sorted(d.name for d in (RESEARCH / p).iterdir() if d.is_dir()):
            out.append((f"{p}/{slug}/", RESEARCH / p / slug / "index.html", RESEARCH / "es-mx" / p / slug / "index.html"))
    out.append(("bounties/", RESEARCH / "bounties" / "index.html", RESEARCH / "es-mx" / "bounties" / "index.html"))
    for bslug in sorted(d.name for d in (RESEARCH / "bounties").iterdir() if d.is_dir()):
        out.append((f"bounties/{bslug}/", RESEARCH / "bounties" / bslug / "index.html", RESEARCH / "es-mx" / "bounties" / bslug / "index.html"))
    out.append(("about/", RESEARCH / "about" / "index.html", RESEARCH / "es-mx" / "about" / "index.html"))
    return out


def url_to_file(url: str) -> Path | None:
    """Where informatico.ai serves an address from (deploy/htaccess.txt section 4c, rule 6)."""
    parts = urlsplit(url)
    if parts.netloc != "informatico.ai":
        return None
    path = parts.path
    if re.match(r"^/(images|fonts|scripts)/|^/styles\.css$", path):
        f = SRC / path.lstrip("/")
    else:
        f = RESEARCH / path.lstrip("/")
    return f / "index.html" if path.endswith("/") else f


class SeoCopyBudgets(unittest.TestCase):
    def test_every_essay_has_hand_written_copy_in_both_languages(self):
        slugs = {d.name for p in PILLARS for d in (RESEARCH / p).iterdir() if d.is_dir()}
        self.assertEqual(len(slugs), 48)
        self.assertEqual(set(FOLIO_SEO), slugs)

    def test_titles_and_descriptions_are_whole_and_within_budget(self):
        rows = [(k, *v) for k, v in FOLIO_SEO.items()] + [(k, *v) for k, v in BOUNTY_SEO.items()]
        for slug, t_en, d_en, t_es, d_es in rows:
            for t in (t_en, t_es):
                self.assertLessEqual(len(t), 53, f"{slug}: {t!r}")
                self.assertGreaterEqual(len(t), 15, f"{slug}: {t!r}")
            for d in (d_en, d_es):
                self.assertTrue(110 <= len(d) <= 158, f"{slug}: {len(d)} chars: {d!r}")
                self.assertTrue(d.endswith("."), f"{slug}: {d!r}")
                self.assertIsNone(FORMULA.search(d), f"{slug}: formula in description: {d!r}")
                self.assertNotIn("medical", d.lower())
                self.assertNotIn("médic", d.lower())
                last = re.findall(r"[\wÀ-ÿ]+", d)[-1].lower()
                self.assertNotIn(last, DANGLING, f"{slug}: ends on a dangling word: {d!r}")
        for key in ("en", "es"):
            i = 0 if key == "en" else 2
            titles = [v[i] for v in FOLIO_SEO.values()] + [v[i] for v in BOUNTY_SEO.values()]
            descs = [v[i + 1] for v in FOLIO_SEO.values()] + [v[i + 1] for v in BOUNTY_SEO.values()]
            self.assertEqual(len(set(titles)), 54, f"duplicate {key} title")
            self.assertEqual(len(set(descs)), 54, f"duplicate {key} description")
        for p, (t_en, d_en, t_es, d_es) in PILLAR_SEO.items():
            for t in (t_en, t_es):
                self.assertTrue(20 <= len(t) <= 70, f"{p}: {t!r}")
            for d in (d_en, d_es):
                self.assertTrue(110 <= len(d) <= 158 and d.endswith("."), f"{p}: {d!r}")
        t_en, d_en, t_es, d_es = (x.replace("{total}", "48") for x in HUB_SEO)
        self.assertTrue(20 <= len(t_en) <= 70 and 20 <= len(t_es) <= 70)
        self.assertTrue(110 <= len(d_en) <= 158 and 110 <= len(d_es) <= 158)


class BuiltPages(unittest.TestCase):
    def test_45_pages_each_have_a_spanish_twin_with_reciprocal_hreflang(self):
        listed = pages()
        self.assertEqual(len(listed), 61)
        for path, en_file, es_file in listed:
            self.assertTrue(es_file.is_file(), f"missing Spanish twin of /{path}")
            en, es = parse(en_file), parse(es_file)
            en_url, es_url = SITE + path, SITE + "es-mx/" + path
            self.assertEqual(en.html_lang, "en", path)
            self.assertEqual(es.html_lang, "es-MX", path)
            for doc, canon in ((en, en_url), (es, es_url)):
                links = {(l.get("rel"), l.get("hreflang")): l.get("href") for l in doc.links}
                self.assertEqual(links[("canonical", None)], canon, path)
                self.assertEqual(links[("alternate", "en")], en_url, path)
                self.assertEqual(links[("alternate", "es-MX")], es_url, path)
                self.assertEqual(links[("alternate", "es")], es_url, path)
                self.assertEqual(links[("alternate", "x-default")], en_url, path)
                self.assertEqual(doc.meta.get("og:url"), canon, path)
                self.assertEqual(doc.meta.get("og:title"), doc.title, path)
                self.assertEqual(doc.meta.get("og:description"), doc.meta.get("description"), path)
                self.assertEqual(doc.meta.get("twitter:card"), "summary_large_image", path)
                self.assertEqual(doc.meta.get("twitter:image"), doc.meta.get("og:image"), path)
                self.assertNotIn("lang=es", " ".join(l.get("href") or "" for l in doc.links), path)
            self.assertEqual(es.meta.get("og:locale"), "es_MX", path)
            self.assertNotEqual(en.title, es.title, path)
            self.assertNotEqual(en.meta["description"], es.meta["description"], path)
            self.assertNotEqual(en.h1, es.h1, f"/{path}: the Spanish page's H1 is still English")
            es_html = es_file.read_text(encoding="utf-8")
            self.assertIn('data-es="Ingeniería">Ingeniería</a>', es_html, path)
            self.assertIn('id="tp-lang-toggle" class="tp-tool-btn" type="button" aria-pressed="true" aria-label="Read in English" title="English">EN</button>', es_html, path)
            if path.count("/") == 2:
                self.assertIn('data-es="Por qué importa">Por qué importa</span>', es_html, path)
                self.assertIn('data-es="I · Historia">I · Historia</a>', es_html, path)
                self.assertIn('data-es="Sobre esta ilustración">Sobre esta ilustración</summary>', es_html, path)

    def test_head_text_comes_from_the_hand_written_copy(self):
        for p in PILLARS:
            for d in (RESEARCH / p).iterdir():
                if not d.is_dir():
                    continue
                t_en, d_en, t_es, d_es = FOLIO_SEO[d.name]
                en, es = parse(d / "index.html"), parse(RESEARCH / "es-mx" / p / d.name / "index.html")
                self.assertEqual(en.title, f"{t_en} | Informatico.ai")
                self.assertEqual(en.meta["description"], d_en)
                self.assertEqual(es.title, f"{t_es} | Informatico.ai")
                self.assertEqual(es.meta["description"], d_es)
        for d in (RESEARCH / "bounties").iterdir():
            if not d.is_dir():
                continue
            t_en, d_en, t_es, d_es = BOUNTY_SEO[d.name]
            en, es = parse(d / "index.html"), parse(RESEARCH / "es-mx" / "bounties" / d.name / "index.html")
            self.assertEqual(en.title, f"{t_en} | Informatico.ai")
            self.assertEqual(en.meta["description"], d_en)
            self.assertEqual(es.title, f"{t_es} | Informatico.ai")
            self.assertEqual(es.meta["description"], d_es)

    def test_json_ld_names_author_dates_image_language_and_breadcrumbs(self):
        for path, en_file, es_file in pages():
            for f, lang in ((en_file, "en"), (es_file, "es-MX")):
                blobs = parse(f).ld
                self.assertEqual(len(blobs), 1, f)
                data = json.loads(blobs[0])
                if path == "":
                    self.assertEqual(data["@type"], "WebSite")
                    continue
                graph = data["@graph"]
                node = graph[0]
                self.assertEqual(node["inLanguage"], lang, f)
                self.assertLessEqual(len(node["headline"]), 110, f)
                self.assertTrue(node["image"].startswith("https://informatico.ai/plates/"), f)
                crumbs = graph[1]
                self.assertEqual(crumbs["@type"], "BreadcrumbList")
                self.assertEqual(crumbs["itemListElement"][-1]["item"], node["url"], f)
                if path.count("/") == 2:
                    self.assertEqual(node["@type"], "ScholarlyArticle")
                    self.assertEqual(node["author"]["name"], "Informatico.ai")
                    self.assertRegex(node["datePublished"], r"^\d{4}-\d{2}-\d{2}$")
                    self.assertRegex(node["dateModified"], r"^\d{4}-\d{2}-\d{2}$")
                    self.assertGreaterEqual(node["dateModified"], node["datePublished"])

    def test_no_meta_description_carries_the_medical_suffix(self):
        for _path, en_file, es_file in pages():
            for f in (en_file, es_file):
                self.assertNotIn("medical advice", parse(f).meta["description"].lower(), f)

    def test_every_address_on_a_spanish_page_resolves_to_a_file(self):
        """The Spanish twin sits one folder deeper: page links must land on Spanish pages, files on real files."""
        for path, _en_file, es_file in pages():
            base = SITE + "es-mx/" + path
            for attr, value in parse(es_file).refs:
                if value.startswith(("#", "mailto:", "data:")) or (value.startswith("http") and not value.startswith(SITE)):
                    continue
                target = url_to_file(urljoin(base, value))
                if target is None:
                    continue
                if attr == "data-plate-prefix":
                    target = target.parent  # a folder the scripts append "<slug>.jpg" to
                    self.assertTrue((target / f"{es_file.parent.name}.jpg").is_file(), f"/es-mx/{path}: {value!r} -> {target}")
                self.assertTrue(target.exists(), f"/es-mx/{path}: {attr}={value!r} -> {target} does not exist")
                if attr == "href" and target.name == "index.html" and "/es-mx/" not in urljoin(base, value) and not value.startswith("http"):
                    self.fail(f"/es-mx/{path}: page link {value!r} leaves the Spanish pages")

    def test_spanish_twin_is_the_english_page_with_only_text_and_depth_changed(self):
        """With no swap and no shift the copier returns its input byte for byte, on every page."""
        for _path, en_file, _es_file in pages():
            text = en_file.read_text(encoding="utf-8")
            self.assertEqual(builder.to_spanish_static(text, swap=False, shift=False), text, en_file)

    def test_copier_swaps_text_and_shifts_only_file_addresses(self):
        src = ('<a href="engineering/" data-en="Engineering" data-es="Ingeniería">Engineering <b>x</b></a>'
               '<img src="plates/e01.jpg" alt=""><link href="../styles.css"><a href="#main">s</a>'
               '<div data-plate-prefix="../../plates/" data-en="A" data-es="">A</div><svg><linearGradient id="g"></linearGradient></svg>')
        out = builder.to_spanish_static(src)
        self.assertIn('<a href="engineering/" data-en="Engineering" data-es="Ingeniería">Ingeniería</a>', out)
        self.assertIn('src="../plates/e01.jpg"', out)
        self.assertIn('href="../../styles.css"', out)
        self.assertIn('href="#main"', out)
        self.assertIn('data-plate-prefix="../../../plates/" data-en="A" data-es="">A</div>', out)
        self.assertIn("</linearGradient>", out)


class SiteFiles(unittest.TestCase):
    def test_sitemap_lists_both_languages_with_alternates_and_real_dates(self):
        xml = (RESEARCH / "sitemap.xml").read_text(encoding="utf-8")
        locs = re.findall(r"<loc>([^<]+)</loc>", xml)
        self.assertEqual(len(locs), 182)
        self.assertEqual(len(set(locs)), 182)
        self.assertEqual(sum("/es-mx/" in u for u in locs), 91)
        self.assertNotIn("lang=es", xml)
        for loc in locs:
            self.assertIsNotNone(url_to_file(loc))
            self.assertTrue(url_to_file(loc).is_file(), loc)
        self.assertEqual(xml.count('hreflang="es-MX"'), 182)
        dates = set(re.findall(r"<lastmod>([^<]+)</lastmod>", xml))
        for d in dates:
            self.assertRegex(d, r"^\d{4}-\d{2}-\d{2}$")

    def test_llms_txt_lists_every_english_page(self):
        text = (RESEARCH / "llms.txt").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Informatico.ai\n"))
        urls = re.findall(r"\]\((https://informatico\.ai/[^)]*)\)", text)
        self.assertEqual(len(urls), 90)  # 4 hubs + 48 essays + bounties hub + 6 bounty folios + toolbox hub + 6 tools + Time & Gravity hub + T.01-T.12 + Cross-Scale Essays hub + 9 essays + about
        for u in urls:
            self.assertTrue(url_to_file(u).is_file(), u)

    def test_404_page_is_absolute_noindex_and_bilingual(self):
        h = parse(RESEARCH / "404.html")
        self.assertEqual(h.meta.get("robots"), "noindex")
        for _attr, value in h.refs:
            self.assertTrue(value.startswith("/"), f"404 page address {value!r} must be absolute: it is served at any depth")
            self.assertTrue(url_to_file(urljoin(SITE + "a/b/c/", value)).exists(), value)
        self.assertIn("/es-mx/", (RESEARCH / "404.html").read_text(encoding="utf-8"))

    def test_htaccess_routes_old_spanish_links_duplicates_and_errors(self):
        if not (ROOT / "deploy" / "htaccess.txt").is_file():
            return
        ht = (ROOT / "deploy" / "htaccess.txt").read_text(encoding="utf-8")
        block = ht[ht.index("# ---- 4c."):ht.index("# ---- 5.")]
        rules = [ln.strip() for ln in block.splitlines() if ln.strip().startswith(("RewriteCond", "RewriteRule"))]
        self.assertIn(r"RewriteRule ^es(?:/(.*))?$ https://informatico.ai/es-mx/$1 [R=301,L]", rules)
        self.assertIn(r"RewriteRule ^(?!es-mx(?:/|$))(.*)$ https://informatico.ai/es-mx/$1? [R=301,L]", rules)
        self.assertIn(r"RewriteCond %{QUERY_STRING} (?:^|&)lang=es(?:-mx)?(?:&|$) [NC]", rules)
        self.assertIn(r"RewriteRule ^research(?:/(.*))?$ https://informatico.ai/$1 [R=301,L,QSA]", rules)
        self.assertEqual(rules.count(r"RewriteCond %{ENV:REDIRECT_STATUS} ^$"), 2, "both new redirects fire only on the visitor's request")
        # rule 0: www.senseiewok.ai -> apex comes first, limited to that host, and leaves certificate challenges alone (SEO pass 2026-11-08)
        self.assertEqual(rules[0:3], [r"RewriteCond %{HTTP_HOST} ^www\.senseiewok\.ai$ [NC]",
                                      r"RewriteCond %{REQUEST_URI} !^/\.well-known/",
                                      r"RewriteRule ^(.*)$ https://senseiewok.ai/$1 [R=301,L,QSA]"])
        alias = rules[-2]
        self.assertNotIn("404", alias, "/404.html must be rewritten on informatico.ai so the ErrorDocument finds research/404.html")
        self.assertEqual(rules[-1], r"RewriteRule ^(.*)$ /research/$1 [L,QSA]")
        # the senseiewok.ai redirect must come before the transparent rewrite and be limited to that host
        i = rules.index(r"RewriteRule ^research(?:/(.*))?$ https://informatico.ai/$1 [R=301,L,QSA]")
        self.assertEqual(rules[i - 2], r"RewriteCond %{HTTP_HOST} ^(?:www\.)?senseiewok\.ai$ [NC]")
        # section 4b still claims /es/ for senseiewok.ai, which is why the Spanish pages are under /es-mx/
        self.assertIn('RedirectMatch 301 "^/es/?$"', ht)
        self.assertEqual(builder.ES_PREFIX, "es-mx/")
        # verify the regex behaviors directly
        es_rule_pat = re.compile(r"^(?!es-mx(?:/|$))(.*)$")
        self.assertIsNone(es_rule_pat.match("es-mx"))
        self.assertIsNone(es_rule_pat.match("es-mx/"))
        self.assertIsNone(es_rule_pat.match("es-mx/engineering/"))
        self.assertEqual(es_rule_pat.match("engineering/e01/").group(1), "engineering/e01/")
        qs_pat = re.compile(r"(?:^|&)lang=es(?:-mx)?(?:&|$)", re.IGNORECASE)
        self.assertIsNotNone(qs_pat.search("lang=es"))
        self.assertIsNotNone(qs_pat.search("foo=1&lang=es-MX&bar=2"))
        self.assertIsNone(qs_pat.search("lang=en"))

    def test_language_button_follows_the_pages_own_alternate(self):
        js = (RESEARCH / "modules" / "theme-plate.mjs").read_text(encoding="utf-8")
        self.assertIn('link[rel="alternate"][hreflang="', js)
        self.assertIn("target.origin === window.location.origin", js)
        self.assertIn("window.location.assign(target.toString())", js)


    def test_about_page_essay_zero_styles_remain_bundled(self):
        """Essay Zero (/about/ and /es-mx/about/) relies on .tz-* rules in informatico.css and css_bundle.py."""
        css = (RESEARCH / "informatico.css").read_text(encoding="utf-8")
        bundle = (ROOT / "tools" / "folios" / "css_bundle.py").read_text(encoding="utf-8")
        for required in (
            ".tz-dignity-stamp",
            "button.tz-sentence",
            ".tz-tier-mark",
            ".tz-svg-kicker",
            ".tz-rosette-group",
            ".tz-legend-btn",
            ".tz-rosette-btn",
            ".tz-table",
            ".tz-panel",
            ".tz-bridge-grid",
            ".tz-bridge-card",
            ".tz-bridge-thumb",
            ".tz-council-grid",
            ".tz-council-card",
            ".tz-cff-card",
            ".tz-cff-cta",
            ".tp-body .tz-cff-cta",
        ):
            self.assertIn(required, css, f"Missing {required} in src/research/informatico.css")
            self.assertIn(required, bundle, f"Missing {required} in tools/folios/css_bundle.py")


if __name__ == "__main__":
    unittest.main()
