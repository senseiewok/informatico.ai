# -*- coding: utf-8 -*-
"""Modular Tech & Tools (The Toolbox) Folios package (X.01–X.06)."""

from .x01 import FOLIO as X01
from .x02 import FOLIO as X02
from .x03 import FOLIO as X03
from .x04 import FOLIO as X04
from .x05 import FOLIO as X05
from .x06 import FOLIO as X06

BOUNDARY_EN = (
    "Educational and exploratory design calculation only. Nothing on this page, in the downloadable "
    "3D/CAD files, or in the accompanying Python scripts is a stamped architectural or structural "
    "engineering design, building-code compliance certificate, or fabrication warranty. Before "
    "cutting, printing, or building any physical part, a licensed architect or professional "
    "engineer of record must independently verify all loads, material properties, connections, "
    "and local code requirements."
)

BOUNDARY_ES = (
    "Calculo de diseno educativo y exploratorio unicamente. Nada en esta pagina, en los archivos "
    "3D/CAD descargables ni en los scripts de Python adjuntos constituye un diseno arquitectonico "
    "o de ingenieria estructural firmado, certificado de cumplimiento de codigo de construccion "
    "ni garantia de fabricacion. Antes de cortar, imprimir o construir cualquier pieza fisica, "
    "un arquitecto o ingeniero profesional con licencia debe verificar de forma independiente "
    "todas las cargas, propiedades de materiales, conexiones y requisitos normativos locales."
)

TOOLCHAIN_FOLIOS: list[dict] = [X01, X02, X03, X04, X05, X06]
TOOLCHAIN_BY_SLUG: dict[str, dict] = {f["slug"]: f for f in TOOLCHAIN_FOLIOS}

PILLAR_FOLIO_TO_TOOLCHAIN: dict[str, list[dict]] = {}
for _t in TOOLCHAIN_FOLIOS:
    for _p_key, _f_slug, _f_code, _f_title in _t["companion_folios"]:
        PILLAR_FOLIO_TO_TOOLCHAIN.setdefault(_f_slug, []).append(_t)
