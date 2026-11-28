"""City tools: the Toolbox's second kind of entry (tools/folios/city_tools/).

Pins the kind before any tool exists: the fixed boundary and group statements, the "City tools" group on the Toolbox
hub and the home page in both languages, the CAD-only wording of sentences that once spoke for every Toolbox entry,
and what the page renderer prints for a tool. The renderer is exercised with a synthetic fixture that lives only in
this file; it is never written to src/ and is not a tool.

When a city tool is added, the tests its own run adds go here as well (verifier and planted defect, figures equal to
the Python twin, a range on the page, model.json sources and ranges, no storage or network calls in the module).
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
sys.path.insert(0, str(ROOT / "tools"))

import build_longform_folios as builder  # noqa: E402
from folios import city_tools  # noqa: E402
from folios.city_tools import (  # noqa: E402
    CITY_TOOL_BOUNDARY_EN,
    CITY_TOOL_BOUNDARY_ES,
    CITY_TOOLS,
    CITY_TOOLS_GROUP_EN,
    CITY_TOOLS_GROUP_ES,
    validate_city_tool,
)
from folios.toolchain_data import TOOLCHAIN_FOLIOS  # noqa: E402

BOUNDARY_EN = (
    "This tool gives a first estimate for comparing options. It is not a design, a permit or professional advice, and "
    "no organization named in its sources has reviewed or endorsed it. Check it with local data and with a qualified "
    "professional before acting on it."
)
BOUNDARY_ES = (
    "Esta herramienta da una primera estimación para comparar opciones. No es un diseño, un permiso ni asesoría "
    "profesional, y ninguna organización citada en sus fuentes la ha revisado ni avalado. Verifíquela con datos locales "
    "y con un profesional calificado antes de actuar."
)
GROUP_EN = (
    "Free tools for people who plan, build and look after cities: a first estimate you can check, with its sources, "
    "its limits and the code it is computed with. They are offered to help. They are not professional advice, and no "
    "organization named in their sources has reviewed or endorsed them."
)
GROUP_ES = (
    "Herramientas gratuitas para quienes planean, construyen y cuidan ciudades: una primera estimación que se puede "
    "revisar, con sus fuentes, sus límites y el código con que se calcula. Se ofrecen para ayudar. No son asesoría "
    "profesional, y ninguna organización citada en sus fuentes las ha revisado ni avalado."
)


def _fixture_tool() -> dict:
    """A synthetic, complete tool record for exercising the renderer. Not a tool; never written to disk."""
    return {
        "slug": "c99", "tool_id": "C.99", "date_published": "2026-11-27", "date_redated": "2026-11-27",
        "question_en": "Fixture question?", "question_es": "¿Pregunta de prueba?",
        "audience_en": "For the test suite only.", "audience_es": "Solo para las pruebas.",
        "seo": ("Fixture", "Fixture description.", "Prueba", "Descripción de prueba."),
        "module": "fixture.mjs", "python_twin": "fixture.py",
        "inputs": [
            {"id": "a", "label_en": "Length", "label_es": "Longitud", "unit": "m", "min": 1, "max": 100, "step": 1,
             "default": 10, "source_en": "Fixture source, fixture conditions", "source_es": "Fuente de prueba"},
            {"id": "b", "label_en": "Share", "label_es": "Fracción", "unit": "%", "min": 0, "max": 100, "step": 1,
             "default": None},
        ],
        "worked_example": {"a": 10, "b": 50},
        "perspectives": [
            {"kind": k, "heading_en": f"H {k}", "heading_es": f"T {k}", "body_en": [f"Body {k}."], "body_es": [f"Cuerpo {k}."]}
            for k in ("first_principles", "measured_evidence", "trade_off")
        ],
        "misleading_en": ["Fixture caveat."], "misleading_es": ["Advertencia de prueba."],
        "limits_en": ["Fixture limit."], "limits_es": ["Límite de prueba."],
        "next_en": ["Fixture next step."], "next_es": ["Paso de prueba."],
        "sources": [
            {"label": f"Source {i}", "url": f"https://example.org/{i}", "takes_en": f"takes {i}", "takes_es": f"toma {i}"}
            for i in range(3)
        ],
    }


def _fixture_estimate(inputs: dict, model: dict) -> dict:
    mid = inputs["a"] * inputs["b"] / 100
    return {"low": mid * 0.8, "high": mid * 1.2, "unit": "m", "driver": "b",
            "steps": [{"label_en": "Midpoint", "label_es": "Punto medio", "value": mid, "unit": "m"}]}


class CityToolsKind(unittest.TestCase):
    def test_fixed_statements_are_exact(self) -> None:
        self.assertEqual(CITY_TOOL_BOUNDARY_EN, BOUNDARY_EN)
        self.assertEqual(CITY_TOOL_BOUNDARY_ES, BOUNDARY_ES)
        self.assertEqual(CITY_TOOLS_GROUP_EN, GROUP_EN)
        self.assertEqual(CITY_TOOLS_GROUP_ES, GROUP_ES)

    def test_city_tools_stay_out_of_the_cad_list(self) -> None:
        cad_slugs = {t["slug"] for t in TOOLCHAIN_FOLIOS}
        self.assertTrue(all(s.startswith("x") for s in cad_slugs))
        for c in CITY_TOOLS:
            self.assertNotIn(c["slug"], cad_slugs)
            self.assertEqual(validate_city_tool(c), [], c["slug"])

    def test_every_listed_city_tool_has_both_pages(self) -> None:
        for c in CITY_TOOLS:
            self.assertTrue((SRC / "toolchain" / c["slug"] / "index.html").is_file(), c["slug"])
            self.assertTrue((SRC / "es-mx" / "toolchain" / c["slug"] / "index.html").is_file(), c["slug"])
            self.assertFalse((SRC / "toolchain" / c["slug"] / "files" / "manifest.json").exists(), c["slug"])

    def test_group_on_toolbox_hub_and_home_in_both_languages(self) -> None:
        for rel, statement in (
            ("toolchain/index.html", GROUP_EN), ("es-mx/toolchain/index.html", GROUP_ES),
        ):
            html = (SRC / rel).read_text(encoding="utf-8")
            self.assertEqual(html.count('id="tp-city-tools"'), 1, rel)
            self.assertIn(statement, html, rel)
        # Magazine pass, phase 2 (2026-11-28): the Toolbox showcase left the cover, which now links to the hub.
        for rel in ("index.html", "es-mx/index.html"):
            html = (SRC / rel).read_text(encoding="utf-8")
            self.assertNotIn('id="tp-city-tools"', html, rel)
            self.assertIn('class="tp-more-title" href="toolchain/"', html, rel)

    def test_group_sits_below_the_cad_tools_on_the_hub(self) -> None:
        html = (SRC / "toolchain" / "index.html").read_text(encoding="utf-8")
        self.assertLess(html.index('data-folio-slug="x08"'), html.index('id="tp-city-tools"'))

    def test_sentences_about_every_toolbox_entry_name_the_cad_tools(self) -> None:
        for rel in ("toolchain/index.html", "index.html"):
            html = (SRC / rel).read_text(encoding="utf-8")
            self.assertNotIn("Every Folio ships", html, rel)
            self.assertNotIn(">All 8 Toolbox Folios", html, rel)
            self.assertNotIn("Every Toolbox Folio (X.01", html, rel)
        for rel in ("es-mx/toolchain/index.html", "es-mx/index.html"):
            html = (SRC / rel).read_text(encoding="utf-8")
            self.assertNotIn("Cada Folio entrega", html, rel)
            self.assertNotIn("Cada Folio incluye", html, rel)


class CityToolValidation(unittest.TestCase):
    def test_fixture_is_complete(self) -> None:
        self.assertEqual(validate_city_tool(_fixture_tool()), [])

    def test_validator_rejects_what_a_city_tool_must_not_lack(self) -> None:
        t = _fixture_tool()
        t["perspectives"] = t["perspectives"][:2]
        self.assertTrue(any("ways of thinking" in e for e in validate_city_tool(t)))
        t = _fixture_tool()
        t["sources"] = t["sources"][:2]
        self.assertTrue(any("sources" in e for e in validate_city_tool(t)))
        t = _fixture_tool()
        t["inputs"][0]["source_en"] = ""
        self.assertTrue(any("default with no source" in e for e in validate_city_tool(t)))
        t = _fixture_tool()
        t["inputs"] = t["inputs"] * 4
        self.assertTrue(any("inputs" in e for e in validate_city_tool(t)))
        t = _fixture_tool()
        t["perspectives"][0]["kind"] = "opinion"
        self.assertTrue(any("unknown perspective" in e for e in validate_city_tool(t)))
        t = _fixture_tool()
        t["python_twin"] = "../../outside.py"
        self.assertTrue(any("bare file name" in e for e in validate_city_tool(t)))
        t = _fixture_tool()
        t["sources"][0]["url"] = "javascript:alert(1)"
        self.assertTrue(any("https://" in e for e in validate_city_tool(t)))
        t = _fixture_tool()
        del t["inputs"][0]["max"]
        self.assertTrue(any("missing max" in e for e in validate_city_tool(t)))

    def test_numbers_print_plainly(self) -> None:
        self.assertEqual(builder._fmt_num(0.00001234), "0.0000123")
        self.assertEqual(builder._fmt_num(1234.6), "1,235")
        self.assertEqual(builder._fmt_num(12.34), "12.3")
        self.assertNotIn("e", builder._fmt_num(0.000005))


class CityToolPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        catalog = json.loads((SRC / "data" / "magazine_catalog.json").read_text(encoding="utf-8"))
        twin = mock.Mock(estimate=_fixture_estimate)
        with mock.patch.object(builder, "_city_tool_twin", return_value=twin), \
                mock.patch.object(builder, "_city_tool_model", return_value={}):
            cls.en = builder.render_city_tool_page(_fixture_tool(), catalog, "en")
            cls.es = builder.to_spanish_static(builder.render_city_tool_page(_fixture_tool(), catalog, "es"))

    def test_question_first_and_boundary_in_both_languages(self) -> None:
        self.assertIn('<h1 id="city-tool-question"', self.en)
        self.assertIn(">Fixture question?</h1>", self.en)
        self.assertIn("¿Pregunta de prueba?", self.es)
        self.assertIn(BOUNDARY_EN, self.en)
        self.assertIn(BOUNDARY_ES, self.es)

    def test_result_is_a_range_computed_by_the_twin(self) -> None:
        self.assertIn("4.00 – 6.00 m", self.en)  # 10 × 50 % = 5, ±20 % in the fixture twin
        self.assertIn('data-city-driver', self.en)
        self.assertIn(">Share</span>", self.en)

    def test_every_required_section_is_present(self) -> None:
        for marker in ('data-city-perspective="first_principles"', 'data-city-perspective="measured_evidence"',
                       'data-city-perspective="trade_off"', "data-city-misleading", "data-city-limits",
                       "data-city-next", 'id="city-tool-sources"', "data-city-worked-steps"):
            self.assertIn(marker, self.en, marker)

    def test_inputs_carry_range_and_source_or_your_value(self) -> None:
        self.assertIn('min="1" max="100"', self.en)
        self.assertIn("Fixture source, fixture conditions", self.en)
        self.assertIn(">Your value</span>", self.en)
        self.assertIn(">Su valor</span>", self.es)

    def test_no_plate_and_downloads_named(self) -> None:
        self.assertNotIn("/plates/c99", self.en)
        for fn in ("model.json", "worked-example.csv", "fixture.py.txt", "fixture.mjs", "downloads.json"):
            self.assertIn(f'href="../../toolchain/c99/files/{fn}"', self.en)
        self.assertIn('download="fixture.py"', self.en)
        self.assertNotIn("manifest.json", self.en.split('id="city-tool-sources"')[1].split("</section>")[0])

    def test_spanish_twin_loads_files_from_the_english_folder(self) -> None:
        # /es-mx/toolchain/c99/ is one folder deeper; ../../../toolchain/c99/files/ resolves to the one copy on disk.
        for fn in ("model.json", "fixture.py.txt", "fixture.mjs", "downloads.json"):
            self.assertIn(f'href="../../../toolchain/c99/files/{fn}"', self.es)
        self.assertIn('src="../../../toolchain/c99/files/fixture.mjs"', self.es)
        self.assertNotIn('"./files/', self.es)

    def test_served_files_pass_the_deploy_type_gate(self) -> None:
        sys.path.insert(0, str(ROOT / "deploy"))
        import check_upload  # noqa: E402

        for fn in ("model.json", "worked-example.csv", "fixture.py.txt", "fixture.mjs", "downloads.json"):
            self.assertIn(Path(fn).suffix, check_upload.ALLOWED, fn)

    def test_renderer_refuses_an_incomplete_tool(self) -> None:
        t = _fixture_tool()
        del t["sources"]
        with self.assertRaises(ValueError):
            builder.render_city_tool_page(t, {}, "en")


if __name__ == "__main__":
    unittest.main()
