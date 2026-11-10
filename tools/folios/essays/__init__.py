"""Cross-Scale Featured Essays (ES.01–ES.03) for Informatico.ai."""
from __future__ import annotations

from .e01_mesoscopic import ESSAY as E01
from .e02_derived_not_measured import ESSAY as E02
from .e03_barriers_pores_clocks import ESSAY as E03

ESSAYS: tuple[dict, ...] = (E01, E02, E03)

__all__ = ["E01", "E02", "E03", "ESSAYS"]
