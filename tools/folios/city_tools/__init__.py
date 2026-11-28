# -*- coding: utf-8 -*-
"""City tools: the Toolbox's second kind of entry (tools/folios/city_tools/).

A city tool answers one question someone who plans, builds or looks after a city would ask, as a first estimate a
person can check: the question, the inputs, a result with its range, the sources, the limits, and the code behind it.
It has no CAD files, no plate and no audio, so it never goes through the CAD Toolbox builders
(``render_toolchain_folio_page``, ``write_toolchain_skills_and_assets``, ``generate_folio_assets``). Its pages live at
``src/toolchain/<slug>/`` and ``src/es-mx/toolchain/<slug>/`` and are written by ``render_city_tool_page`` and
``write_city_tool_assets`` in ``tools/build_longform_folios.py``.

Each entry of ``CITY_TOOLS`` is a dict with these keys (``validate_city_tool`` checks them):

- ``slug`` (``"c01"``, ``"c02"``, ...), ``tool_id`` (``"C.01"``), ``date_published``, ``date_redated`` (ISO dates).
- ``question_en`` / ``question_es``: the question, in the asker's words.
- ``audience_en`` / ``audience_es``: one sentence saying who the tool is for.
- ``seo``: ``(title_en, desc_en, title_es, desc_es)``.
- ``module``: the hand-written native ES module in ``src/toolchain/<slug>/files/``. It reads only ``model.json``,
  found beside itself with ``new URL("./model.json", import.meta.url)``, and mounts on ``form[data-city-tool]``.
- ``python_twin``: file name of the standard-library twin in ``skills/toolchain/<slug>/`` (served beside the page
  as ``<name>.py.txt``, because the deploy gate does not upload ``.py``). It exposes
  ``estimate(inputs: dict, model: dict) -> dict`` returning ``low``, ``high``, ``unit``, ``driver`` (the input id
  that moves the result most) and ``steps`` (a list of ``{"label_en", "label_es", "value", "unit"}``). Every
  number the page prints is computed by calling it; nothing is typed into the page by hand.
- ``inputs``: at most seven ``{"id", "label_en", "label_es", "unit", "min", "max", "step", "default",
  "source_en", "source_es"}``. ``default`` is ``None`` for a value the user must supply ("your value"); otherwise
  ``source_en`` / ``source_es`` say where the default comes from and under what conditions.
- ``worked_example``: the input values of the worked example the page prints in full.
- ``perspectives``: at least three ``{"kind", "heading_en", "heading_es", "body_en", "body_es"}`` with ``kind`` in
  ``PERSPECTIVE_KINDS`` and bodies as lists of paragraphs.
- ``misleading_en`` / ``misleading_es``: the strongest reason this answer could mislead (lists of paragraphs).
- ``limits_en`` / ``limits_es``: where this stops (lists of items).
- ``next_en`` / ``next_es``: what to do next (lists of items).
- ``sources``: three to six ``{"label", "url", "takes_en", "takes_es"}``, each ``url`` starting ``https://``.
"""

from __future__ import annotations

# Fixed boundary statement every city tool page carries, in English and Mexican Spanish.
CITY_TOOL_BOUNDARY_EN = (
    "This tool gives a first estimate for comparing options. It is not a design, a permit or professional advice, and "
    "no organization named in its sources has reviewed or endorsed it. Check it with local data and with a qualified "
    "professional before acting on it."
)
CITY_TOOL_BOUNDARY_ES = (
    "Esta herramienta da una primera estimación para comparar opciones. No es un diseño, un permiso ni asesoría "
    "profesional, y ninguna organización citada en sus fuentes la ha revisado ni avalado. Verifíquela con datos locales "
    "y con un profesional calificado antes de actuar."
)

# The one statement of the "City tools" group on the Toolbox hub and the home page.
CITY_TOOLS_GROUP_TITLE_EN = "City tools"
CITY_TOOLS_GROUP_TITLE_ES = "Herramientas para ciudades"
CITY_TOOLS_GROUP_EN = (
    "Free tools for people who plan, build and look after cities: a first estimate you can check, with its sources, "
    "its limits and the code it is computed with. They are offered to help. They are not professional advice, and no "
    "organization named in their sources has reviewed or endorsed them."
)
CITY_TOOLS_GROUP_ES = (
    "Herramientas gratuitas para quienes planean, construyen y cuidan ciudades: una primera estimación que se puede "
    "revisar, con sus fuentes, sus límites y el código con que se calcula. Se ofrecen para ayudar. No son asesoría "
    "profesional, y ninguna organización citada en sus fuentes las ha revisado ni avalado."
)

PERSPECTIVE_KINDS = ("first_principles", "measured_evidence", "trade_off", "who_is_reached", "rule_of_thumb")
PERSPECTIVE_LABELS = {
    "first_principles": ("First principles", "Primeros principios"),
    "measured_evidence": ("Measured evidence", "Evidencia medida"),
    "trade_off": ("Trade-off", "Costo y compromiso"),
    "who_is_reached": ("Who is reached", "A quién alcanza"),
    "rule_of_thumb": ("Rule of thumb", "Regla práctica"),
}
MAX_INPUTS = 7
MIN_SOURCES, MAX_SOURCES = 3, 6
MIN_PERSPECTIVES = 3

_REQUIRED = (
    "slug", "tool_id", "date_published", "date_redated", "question_en", "question_es", "audience_en", "audience_es",
    "seo", "module", "python_twin", "inputs", "worked_example", "perspectives", "misleading_en", "misleading_es",
    "limits_en", "limits_es", "next_en", "next_es", "sources",
)

# No city tool has been published yet. Each one is added here by the City Tools sentinel, one per pull request.
CITY_TOOLS: list[dict] = []
CITY_TOOLS_BY_SLUG: dict[str, dict] = {t["slug"]: t for t in CITY_TOOLS}


def validate_city_tool(tool: dict) -> list[str]:
    """Return every way ``tool`` falls short of what a city tool must have (empty when it is complete)."""
    errors: list[str] = []
    slug = tool.get("slug", "?")
    for key in _REQUIRED:
        if key not in tool or tool[key] in (None, "", [], {}):
            errors.append(f"{slug}: missing {key}")
    if errors:
        return errors
    if not (isinstance(slug, str) and len(slug) == 3 and slug[0] == "c" and slug[1:].isdigit()):
        errors.append(f"{slug}: slug must be c01, c02, ...")
    for key, ext in (("python_twin", ".py"), ("module", ".mjs")):
        name = str(tool[key])
        if "/" in name or "\\" in name or ".." in name or not name.endswith(ext) or len(name) <= len(ext):
            errors.append(f"{slug}: {key} must be a bare file name ending in {ext}")
    if len(tool["seo"]) != 4:
        errors.append(f"{slug}: seo must be (title_en, desc_en, title_es, desc_es)")
    inputs = tool["inputs"]
    if not 1 <= len(inputs) <= MAX_INPUTS:
        errors.append(f"{slug}: {len(inputs)} inputs; a city tool has 1 to {MAX_INPUTS}")
    ids = set()
    for inp in inputs:
        iid = inp.get("id", "?")
        ids.add(iid)
        for key in ("id", "label_en", "label_es", "unit", "min", "max", "step"):
            if key not in inp:
                errors.append(f"{slug}: input {iid} missing {key}")
        if not ("min" in inp and "max" in inp):
            continue
        if not inp["min"] < inp["max"]:
            errors.append(f"{slug}: input {iid} needs min < max")
        if inp.get("default") is not None:
            if not (inp.get("source_en") and inp.get("source_es")):
                errors.append(f"{slug}: input {iid} has a default with no source")
            elif not inp["min"] <= inp["default"] <= inp["max"]:
                errors.append(f"{slug}: input {iid} default lies outside its range")
    for iid in tool["worked_example"]:
        if iid not in ids:
            errors.append(f"{slug}: worked example names unknown input {iid}")
    for iid in ids:
        if iid not in tool["worked_example"]:
            errors.append(f"{slug}: worked example has no value for input {iid}")
    kinds = [p.get("kind") for p in tool["perspectives"]]
    if len(kinds) < MIN_PERSPECTIVES:
        errors.append(f"{slug}: {len(kinds)} ways of thinking; at least {MIN_PERSPECTIVES}")
    for k in kinds:
        if k not in PERSPECTIVE_KINDS:
            errors.append(f"{slug}: unknown perspective kind {k}")
    if len(set(kinds)) != len(kinds):
        errors.append(f"{slug}: each way of thinking appears once")
    if not MIN_SOURCES <= len(tool["sources"]) <= MAX_SOURCES:
        errors.append(f"{slug}: {len(tool['sources'])} sources; a city tool cites {MIN_SOURCES} to {MAX_SOURCES}")
    for src in tool["sources"]:
        for key in ("label", "url", "takes_en", "takes_es"):
            if not src.get(key):
                errors.append(f"{slug}: a source is missing {key}")
        if src.get("url") and not str(src["url"]).startswith("https://"):
            errors.append(f"{slug}: source address must start with https://")
    for pair in (("misleading_en", "misleading_es"), ("limits_en", "limits_es"), ("next_en", "next_es")):
        if len(tool[pair[0]]) != len(tool[pair[1]]):
            errors.append(f"{slug}: {pair[0]} and {pair[1]} differ in length")
    return errors


__all__ = [
    "CITY_TOOL_BOUNDARY_EN",
    "CITY_TOOL_BOUNDARY_ES",
    "CITY_TOOLS",
    "CITY_TOOLS_BY_SLUG",
    "CITY_TOOLS_GROUP_EN",
    "CITY_TOOLS_GROUP_ES",
    "CITY_TOOLS_GROUP_TITLE_EN",
    "CITY_TOOLS_GROUP_TITLE_ES",
    "MAX_INPUTS",
    "PERSPECTIVE_KINDS",
    "PERSPECTIVE_LABELS",
    "validate_city_tool",
]
