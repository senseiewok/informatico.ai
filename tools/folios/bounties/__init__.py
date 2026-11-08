# -*- coding: utf-8 -*-
"""Modular Open Bounties Folios package (B.01–B.06)."""

from .b01 import FOLIO as B01
from .b02 import FOLIO as B02
from .b03 import FOLIO as B03
from .b04 import FOLIO as B04
from .b05 import FOLIO as B05
from .b06 import FOLIO as B06

BOUNTY_FOLIOS: list[dict] = [B01, B02, B03, B04, B05, B06]
BOUNTY_BY_SLUG: dict[str, dict] = {b["slug"]: b for b in BOUNTY_FOLIOS}
