#!/usr/bin/env python3
"""Pillar & Essay Registry for Informatico.ai (4 Pillars x 12 Essays = 48 Folios + 6 Bounties)."""
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

PLATE_CAPTIONS.update(
    {
        "b01": {
            "alt": "Conceptual illustration imagining a non-redundant Golomb ruler optical interferometer and phased-array radio telescope dish on a sunlit oak laboratory table (artistic impression, not a measured structure).",
            "caption": "Plate B.01-V · Conceptual illustration imagining a non-redundant Golomb ruler optical interferometer and phased-array radio receiver spacing where every pairwise distance is strictly distinct (artistic impression, not a measured structure). Exact Sidon B₂ sumset bounds and Lean 4 formalization rules are verified below.",
        },
        "b02": {
            "alt": "Conceptual illustration imagining a gold cryogenic quantum dilution refrigerator chandelier beside an illuminated FeMoCo iron-molybdenum-sulfur catalyst cluster model (artistic impression, not a measured structure).",
            "caption": "Plate B.02-V · Conceptual illustration imagining a fault-tolerant superconducting dilution refrigerator chandelier paired with a glowing [Fe₇MoS₉C] nitrogenase cofactor model for room-temperature nitrogen fixation (artistic impression, not a measured structure). Exact Kitaev surface-code threshold scaling and active-volume qubit footprints are verified below.",
        },
        "b03": {
            "alt": "Conceptual illustration imagining a sculpted biomimetic SIMP topology-optimized vaulted concrete floor slab cured with mineralized carbonate aggregates in a sunlit structural test hall (artistic impression, not a measured structure).",
            "caption": "Plate B.03-V · Conceptual illustration imagining a Bendsøe–Sigmund SIMP topology-optimized ribbed floor slab with trabecular voids and carbonated mineral aggregate curing (artistic impression, not a measured structure). Exact FEniCS/dolfinx compliance ratios and sub-45 kg CO₂e/m² mass balances are verified below.",
        },
        "b04": {
            "alt": "Conceptual illustration imagining an unreinforced limestone and terracotta funicular vault crowned by a white radiative sky-cooling membrane over a courtyard pool (artistic impression, not a measured structure).",
            "caption": "Plate B.04-V · Conceptual illustration imagining a zero-rebar compression-only stone and tile vault derived from 3D polyhedral graphic statics and crowned by an 8–13 μm radiative sky-cooling shell (artistic impression, not a measured structure). Exact Minkowski force-polyhedron equilibrium and midday radiative flux balances are verified below.",
        },
        "b05": {
            "alt": "Conceptual illustration imagining a transparent quartz hydrodynamic flume tank illuminated by laser particle-image velocimetry revealing emerald and amber vortex streets and shock fronts (artistic impression, not a measured structure).",
            "caption": "Plate B.05-V · Conceptual illustration imagining a laser-illuminated hydrodynamic flume where noisy velocity trajectories are distilled into sparse nonlinear PDEs via PySR and PySINDy (artistic impression, not a measured structure). Exact STLSQ hard-thresholding and Pareto Minimum Description Length curves are verified below.",
        },
        "b06": {
            "alt": "Conceptual illustration imagining an ultracold-atom optical lattice vacuum chamber where ruby and emerald laser beams trap a glowing one-dimensional quantum spin chain (artistic impression, not a measured structure).",
            "caption": "Plate B.06-V · Conceptual illustration imagining an ultracold-atom optical lattice trapping a critical 1D quantum spin chain alongside chiral gauge-symmetry geometry (artistic impression, not a measured structure). Exact HEPLean/PhysLean four-trace anomaly cancellation and ITensors.jl Calabrese–Cardy entanglement bounds are verified below.",
        },
    }
)
