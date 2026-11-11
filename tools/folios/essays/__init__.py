"""Cross-Scale Featured Essays (ES.01–ES.11) for Informatico.ai."""
from __future__ import annotations

from .e01_mesoscopic import ESSAY as E01
from .e02_derived_not_measured import ESSAY as E02
from .e03_barriers_pores_clocks import ESSAY as E03
from .e04_tensegrity_microcausality import ESSAY as E04
from .e05_islands_conditional_survival import ESSAY as E05
from .e06_coupled_constraints_proof import ESSAY as E06
from .e07_parallel_hybrid_horizon import ESSAY as E07
from .e08_schur_identifiability import ESSAY as E08
from .e09_multipartite_witnesses import ESSAY as E09
from .e10_four_gate_sieve import ESSAY as E10
from .e11_seven_gate_crown import ESSAY as E11

ESSAYS: tuple[dict, ...] = (E01, E02, E03, E04, E05, E06, E07, E08, E09, E10, E11)

__all__ = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "ESSAYS"]
