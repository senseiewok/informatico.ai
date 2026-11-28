"""Guard: bounty pages must say plainly that they are not prize entries (grounding review, 2026-11-13)."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
sys.path.insert(0, str(ROOT / "tools"))

# A readout or gate label must never read as a prize organizer's verdict.
PRIZE_VERDICT = re.compile(r"(XPRIZE|Holcim|Cooling Prize|IStructE|Erd\u0151s|AIMO)[^<>\"]{0,40}(Verdict|Veredicto|\bGate\b)")
# Words that would make a navigation entry read as a result: a verdict, a pass, a win or an award.
# The readout labels are matched as printed (PASS, FAIL, APROBADO); the ordinary words in any case. "Gate" alone
# is not here (an essay title says "Four-Gate Operator Sieve"); PRIZE_VERDICT catches it next to a prize name.
VERDICT_WORD = re.compile(
    r"\b(?:PASS(?:ED)?|FAIL(?:ED)?|APROBADO|(?i:verdict|veredicto|w[oi]n|winner|winning|gan[oó]|ganador(?:a|es)?|"
    r"award(?:ed)?|galard[oó]n(?:ado)?|premiad[oa]))\b"
)
PRIZE_NAME = re.compile(r"XPRIZE|Holcim|Cooling Prize|IStructE|AIMO|Erd\u0151s")
COVERS = (SRC / "index.html", SRC / "es-mx" / "index.html")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class _Collector(HTMLParser):
    """Every string a reader gets from one element (found by tag, or by tag and id): its text and its data-en,
    data-es, alt, aria-label and title values. Scripts and styles are left out."""

    def __init__(self, tag: str, ident: str | None = None) -> None:
        super().__init__(convert_charrefs=True)
        self.tag, self.ident = tag, ident
        self.depth = 0
        self.skip = 0
        self.found = 0
        self.strings: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.depth == 0 and tag == self.tag and (self.ident is None or attrs.get("id") == self.ident):
            self.depth = 1
            self.found += 1
        elif self.depth and tag not in VOID:
            self.depth += 1
        if self.depth:
            if tag in ("script", "style"):
                self.skip += 1
            for name in ("data-en", "data-es", "alt", "aria-label", "title"):
                if attrs.get(name):
                    self.strings.append(attrs[name])

    def handle_startendtag(self, tag, attrs):
        if self.depth:
            for name, value in attrs:
                if name in ("data-en", "data-es", "alt", "aria-label", "title") and value:
                    self.strings.append(value)

    def handle_endtag(self, tag):
        if self.depth and tag not in VOID:
            if tag in ("script", "style") and self.skip:
                self.skip -= 1
            self.depth -= 1

    def handle_data(self, data):
        if self.depth and not self.skip and data.strip():
            self.strings.append(data)


def strings_in(html: str, tag: str, ident: str | None = None) -> list[str]:
    parser = _Collector(tag, ident)
    parser.feed(html)
    parser.close()
    if parser.found != 1:
        raise AssertionError(f"expected one <{tag}{' id=' + ident if ident else ''}>, found {parser.found}")
    return parser.strings


class BountyBoundaryTests(unittest.TestCase):
    def pages(self) -> list[Path]:
        out = [SRC / "bounties" / "index.html", SRC / "es-mx" / "bounties" / "index.html"]
        for n in range(1, 7):
            out.append(SRC / "bounties" / f"b{n:02d}" / "index.html")
            out.append(SRC / "es-mx" / "bounties" / f"b{n:02d}" / "index.html")
        return out

    def test_every_bounty_page_carries_the_not_a_prize_entry_notice(self) -> None:
        import build_longform_folios as blf

        for page in self.pages():
            html = page.read_text(encoding="utf-8")
            self.assertIn("tp-bounty-boundary", html, page)
            self.assertIn(blf.esc(blf.BOUNTY_BOUNDARY_ES), html, page)
            if "es-mx" not in page.parts:
                self.assertIn(blf.esc(blf.BOUNTY_BOUNDARY_EN), html, page)

    def test_cover_main_names_no_prize_sum_or_verdict(self) -> None:
        """Checks the cover's <main> only (EN and es-MX): everything a reader gets there (text, both languages of
        each data-en/data-es pair, alt and aria-label values) names no prize, no sum of money and no verdict
        word, and <main> links to /bounties/, where the open-problems section and its notice live since the
        magazine pass of 2026-11-28. It does not look at the masthead or the Contents drawer; those are covered
        by test_cover_contents_drawer_may_name_prizes_but_never_a_verdict and
        test_no_label_reads_as_a_prize_verdict."""
        named = re.compile(r"XPRIZE|Holcim|Cooling Prize|IStructE|AIMO|Erd\u0151s Problem|\$\s?\d|\bPASS\b|APROBADO|\bw[oi]n\b|\bgan[oó]\b|award", re.I)
        for page in COVERS:
            html = page.read_text(encoding="utf-8")
            strings = strings_in(html, "main")
            self.assertGreater(len(strings), 150, page)
            for text in strings:
                hit = named.search(text)
                self.assertIsNone(hit, f"{page}: {hit.group(0) if hit else ''!r} in {text!r}")
            main = html[html.index("<main"):html.index("</main>")]
            self.assertIn('href="bounties/"', main, page)
            self.assertNotIn("tp-bounty-crucible", main, page)

    def test_cover_contents_drawer_may_name_prizes_but_never_a_verdict(self) -> None:
        """A decision, written down: the site-wide Contents drawer (<dialog id="tp-contents">) lists every essay
        by its title, so on the cover too it names prizes and their sums ("$5M XPRIZE Quantum Applications").
        That is navigation and is allowed. What it must never carry is a word that reads as a result: a verdict,
        a pass, a win or an award."""
        for page in COVERS:
            strings = strings_in(page.read_text(encoding="utf-8"), "dialog", "tp-contents")
            self.assertTrue([s for s in strings if PRIZE_NAME.search(s)], f"{page}: the drawer lists the bounty essays by title")
            for text in strings:
                hit = VERDICT_WORD.search(text)
                self.assertIsNone(hit, f"{page}: {hit.group(0) if hit else ''!r} in the Contents drawer: {text!r}")
        for bad in ("XPRIZE Carbon: PASS", "Ganador del Holcim", "Award-winning vault", "Erdős #30 Verdict", "Veredicto", "we won"):
            self.assertIsNotNone(VERDICT_WORD.search(bad), bad)
        for fine in ("$5M XPRIZE Quantum Applications", "Global Cooling Prize", "Holcim Awards 2025 names", "Passive cooling", "The Four-Gate Operator Sieve"):
            self.assertIsNone(VERDICT_WORD.search(fine), fine)

    def test_no_label_reads_as_a_prize_verdict(self) -> None:
        """The whole document of every bounty page and of the two covers (masthead, Contents drawer and <main>):
        no prize name is followed within a few words by Verdict, Veredicto or Gate."""
        for page in self.pages() + list(COVERS):
            html = page.read_text(encoding="utf-8")
            self.assertIn("<body", html, page)
            hit = PRIZE_VERDICT.search(html[html.index("<body"):])
            self.assertIsNone(hit, f"{page}: {hit.group(0) if hit else ''}")
        self.assertIsNotNone(PRIZE_VERDICT.search("XPRIZE Carbon Verdict"))

    def test_b05_matches_verifier_mdl_and_rejects_planted_defect(self) -> None:
        script = ROOT / "bounties" / "bounty_p2_pysr_pysindy_pde_discovery.py"
        normal = subprocess.run(
            [sys.executable, "-X", "utf8", str(script), "--json"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertEqual(normal.returncode, 0, normal.stdout + normal.stderr)
        payload = json.loads(normal.stdout)
        self.assertEqual(payload["verdict"], "PASS")
        self.assertAlmostEqual(payload["pysr_mdl_score"], -1073.4509, places=4)

        defect = subprocess.run(
            [sys.executable, "-X", "utf8", str(script), "--planted-defect", "--json"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertNotEqual(defect.returncode, 0, defect.stdout + defect.stderr)
        defect_payload = json.loads(defect.stdout)
        self.assertEqual(defect_payload["verdict"], "FAIL")
        self.assertEqual(defect_payload["overfit_case"]["verdict"], "FAIL")
        self.assertEqual(defect_payload["overfit_case"]["active_pde_terms"], ["u*u_x", "u_xx", "u^3"])
        self.assertEqual(defect_payload["underfit_case"]["verdict"], "FAIL")
        self.assertEqual(defect_payload["underfit_case"]["active_pde_terms"], ["u*u_x"])

        for path in (
            SRC / "bounties" / "b05" / "index.html",
            SRC / "es-mx" / "bounties" / "b05" / "index.html",
            ROOT / "skills" / "bounties" / "b05" / "SKILL.md",
            SRC / "modules" / "physics-discovery-crucible.mjs",
        ):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("1360.87", text, path)
            self.assertNotIn("1360.9", text, path)
            if path.suffix != ".mjs":
                self.assertIn("1073.45", text, path)


if __name__ == "__main__":
    unittest.main()
