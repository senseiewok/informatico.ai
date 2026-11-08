#!/usr/bin/env python3
"""Track & Folio Registry for Informatico.ai (48 Pillar Folios + 6 Open Bounties + 6 Tech & Tools = 60 Folios)."""
from __future__ import annotations

from . import architecture, bounties, engineering, math, physics, toolchain
from .bounties import BOUNTY_BY_SLUG, BOUNTY_FOLIOS
from .toolchain import (
    BOUNDARY_EN,
    BOUNDARY_ES,
    PILLAR_FOLIO_TO_TOOLCHAIN,
    TOOLCHAIN_BY_SLUG,
    TOOLCHAIN_FOLIOS,
)

PILLAR_PACKAGES = {
    "engineering": engineering.ESSAY_MODULES,
    "architecture": architecture.ESSAY_MODULES,
    "physics": physics.ESSAY_MODULES,
    "math": math.ESSAY_MODULES,
}

FOLIOS_BY_PILLAR: dict[str, list[dict]] = {}
LONGFORM: dict[str, dict] = {}
PLATE_CAPTIONS: dict[str, dict] = {}
FRONTIER_DISCOVERY_DISPATCHES: dict[str, dict] = {}
FOLIO_3D_META: dict[str, tuple[str, str]] = {}
FOLIO_ES_TRANSLATIONS: dict[str, dict] = {}

for _pillar, _modules in PILLAR_PACKAGES.items():
    FOLIOS_BY_PILLAR[_pillar] = []
    for _mod in _modules:
        _slug = _mod.SLUG
        FOLIOS_BY_PILLAR[_pillar].append(_mod.FOLIO)
        LONGFORM[_slug] = _mod.LONGFORM_DATA
        if _mod.PLATE_CAPTION:
            PLATE_CAPTIONS[_slug] = _mod.PLATE_CAPTION
        if _mod.DISPATCH:
            FRONTIER_DISCOVERY_DISPATCHES[_slug] = _mod.DISPATCH
        if _mod.META_3D:
            FOLIO_3D_META[_slug] = _mod.META_3D
        if _mod.ES_TRANSLATION:
            FOLIO_ES_TRANSLATIONS[_slug] = _mod.ES_TRANSLATION

for _b in BOUNTY_FOLIOS:
    PLATE_CAPTIONS[_b["slug"]] = {
        "alt": f"Editorial illustration imagining the concept of Bounty {_b['folio_id']} ({_b['bounty_id']}): {_b['title']}",
        "caption": f"Plate {_b['folio_id']}-V · Editorial Vision Plate illustrating {_b['title']} ({_b['governing_law']}).",
    }

for _t in TOOLCHAIN_FOLIOS:
    PLATE_CAPTIONS[_t["slug"]] = {
        "alt": f"Editorial illustration imagining the 3D CAD and studio fabrication concept of Toolbox {_t['folio_id']} ({_t['tool_id']}): {_t['title']}",
        "caption": f"Plate {_t['folio_id']}-V · Editorial Vision Plate illustrating {_t['title']} ({_t['governing_law']}).",
    }

__all__ = [
    "BOUNDARY_EN",
    "BOUNDARY_ES",
    "BOUNTY_BY_SLUG",
    "BOUNTY_FOLIOS",
    "FOLIOS_BY_PILLAR",
    "FOLIO_3D_META",
    "FOLIO_ES_TRANSLATIONS",
    "FRONTIER_DISCOVERY_DISPATCHES",
    "LONGFORM",
    "PILLAR_FOLIO_TO_TOOLCHAIN",
    "PILLAR_PACKAGES",
    "PLATE_CAPTIONS",
    "TOOLCHAIN_BY_SLUG",
    "TOOLCHAIN_FOLIOS",
]
