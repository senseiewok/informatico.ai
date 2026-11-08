#!/usr/bin/env python3
"""Pillar & Essay Registry for Informatico.ai (4 Pillars x 10 Essays = 40 Folios)."""
from __future__ import annotations

from . import architecture, engineering, math, physics

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
