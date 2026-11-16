#!/usr/bin/env python3
"""Build CC.02 · One Stone Forest, Eight Moves: La Sagrada Família architectural & stereotomy showcase.

Single source of truth for text and citations lives in tools/folios/classics/cc02.py; mathematical models live in
tools/folios/classics/cc02_mechanics.py; page shell comes from build_longform_folios (head, masthead, contents dialog,
crossword, footer); interactive WebGL2 + 2D SVG + CAD export lives in src/modules/sagrada-familia.mjs.
Strict CSP compliance: zero inline scripts, zero inline style= attributes.

Run on its own: python -X utf8 tools/build_sagrada_masterpiece.py   (also invoked from build_longform_folios.main)
"""
from __future__ import annotations

import hashlib
import html
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_longform_folios as B  # noqa: E402
from folios.classics import cc02 as C  # noqa: E402
from folios.classics import cc02_mechanics as M  # noqa: E402
from folios.seo_copy import BRAND  # noqa: E402

RESEARCH = ROOT / "src"
PATH = f"classics/{C.SLUG}/"
PLATE = RESEARCH / "plates" / "cc02.png"


def a(s: str) -> str:
    return html.escape(str(s), quote=True)


def t(s: str) -> str:
    return html.escape(str(s), quote=False)


def bi(tag: str, en: str, es: str, cls: str = "", extra: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    x = f" {extra}" if extra else ""
    return f'<{tag}{c}{x} data-en="{a(en)}" data-es="{a(es)}">{t(en)}</{tag}>'


def stamp(key: str) -> str:
    s = C.SOURCES[key]
    return bi("a", s["short"], s.get("short_es", s["short"]), f"sf-stamp sf-stamp-{s['kind']}", f'href="#src-{a(key)}"')


def cite(keys: list[str]) -> str:
    if not keys:
        return ""
    return f'<p class="sf-cite">{" ".join(stamp(k) for k in keys)}</p>'


# --------------------------------------------------------------------------------------------- backdrop & SVG helpers

def render_catenary_backdrop() -> str:
    """Fixed geometric parchment/blueprint SVG with subtle catenary cords, survey grid, and 8 spire silhouette lanes."""
    grid_lines = []
    for x in range(120, 1600, 160):
        grid_lines.append(f'<line x1="{x}" y1="0" x2="{x}" y2="2000"/>')
    for y in range(100, 2000, 160):
        grid_lines.append(f'<line x1="0" y1="{y}" x2="1600" y2="{y}"/>')
    grid = "".join(grid_lines)

    cord_d = "M 180 60 Q 490 520 800 580 Q 1110 520 1420 60 M 320 60 Q 560 440 800 490 Q 1040 440 1280 60"
    spires_d = "M 640 940 L 680 420 Q 720 160 760 420 L 800 120 L 840 420 Q 880 160 920 420 L 960 940"

    lanes = []
    for idx, card in enumerate(C.CARDS):
        h_pct = 38 + idx * 7
        top_y = max(18, 220 - h_pct * 1.9)
        lane_svg = (
            f'<svg class="sf-skyline-lane" data-move="{a(card["id"])}" viewBox="0 0 160 260" width="160" height="260" '
            f'aria-hidden="true" focusable="false">'
            f'<path d="M 35 250 L 58 {top_y + 38:.1f} Q 80 {top_y:.1f} 102 {top_y + 38:.1f} L 125 250" '
            f'fill="none" stroke="var(--sf-ink)" stroke-width="1.4"/>'
            f'<line x1="80" y1="{top_y:.1f}" x2="80" y2="{max(8, top_y - 18):.1f}" stroke="var(--sf-red)" stroke-width="1.6"/>'
            f'<line x1="72" y1="{max(12, top_y - 10):.1f}" x2="88" y2="{max(12, top_y - 10):.1f}" stroke="var(--sf-red)" stroke-width="1.6"/>'
            f"</svg>"
        )
        lanes.append(lane_svg)

    return f"""  <svg class="sf-catenary-backdrop" viewBox="0 0 1600 1000" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
    <g class="sf-layer sf-layer-grid" data-depth="0.06">{grid}</g>
    <g class="sf-layer sf-layer-cords" data-depth="0.14"><path d="{cord_d}"/><path d="{cord_d}" transform="translate(0 800)"/></g>
    <g class="sf-layer sf-layer-spires" data-depth="0.22"><path d="{spires_d}"/><path d="{spires_d}" transform="translate(0 800)"/></g>
  </svg>
  <div class="sf-skyline-lanes" aria-hidden="true">
    {"".join(lanes)}
  </div>"""


def render_era_rail() -> str:
    chips = []
    for i, c in enumerate(C.CARDS):
        cls = "sf-era-chip is-current" if i == 0 else "sf-era-chip"
        aria = ' aria-current="true"' if i == 0 else ""
        chips.append(
            f'<a class="{cls}" href="#move-{a(c["id"])}" data-move="{a(c["id"])}"{aria} '
            f'data-en="{a(c["era"])}" data-es="{a(c["era"])}">{t(c["era"])}</a>'
        )
    return f'      <nav class="sf-era-rail" aria-label="Architecture moves timeline">{"".join(chips)}</nav>'


# --------------------------------------------------------------------------------------------- editorial cards & drawer

def _media_map() -> dict[str, dict]:
    return {item["id"]: item for item in (*C.PHOTOS, *C.PLATES)}


def render_media_figure(item: dict, is_es: bool, in_gallery: bool = False) -> str:
    vg = C.VISUAL_GALLERY_TEXT
    is_photo = item["kind"] == "photo"
    badge_en = f"{vg['badge_photo_en']} · {item['license']}" if is_photo else f"{vg['badge_render_en']} · {item['era']}"
    badge_es = f"{vg['badge_photo_es']} · {item['license']}" if is_photo else f"{vg['badge_render_es']} · {item['era']}"
    badge_cls = "sf-media-badge sf-media-badge-photo" if is_photo else "sf-media-badge sf-media-badge-render"
    alt_txt = item["alt_es"] if is_es else item["alt_en"]
    fig_id = f' id="{a(item["id"])}"' if not in_gallery else ""
    extra_btn = (
        f' data-alt-en="{a(item["alt_en"])}" data-alt-es="{a(item["alt_es"])}"'
        f' data-cap-en="{a(item["caption_en"])}" data-cap-es="{a(item["caption_es"])}"'
        f' data-badge-en="{a(badge_en)}" data-badge-es="{a(badge_es)}" data-kind="{a(item["kind"])}"'
        if in_gallery else ""
    )
    return f"""        <figure class="sf-media-card" data-sf-media-kind="{a(item['kind'])}" data-sf-media-id="{a(item['id'])}"{fig_id}>
          <div class="sf-media-head">
            <span class="{badge_cls}" data-en="{a(badge_en)}" data-es="{a(badge_es)}">{t(badge_es if is_es else badge_en)}</span>
            <button type="button" class="sf-btn sf-btn-quiet sf-zoom-btn" data-sf-open-media="{a(item['id'])}"{extra_btn} data-en="Inspect plate" data-es="Ampliar lámina">{t('Ampliar lámina' if is_es else 'Inspect plate')}</button>
          </div>
          <div class="sf-media-frame">
            <img src="../../{a(item['image'])}" width="{item['width']}" height="{item['height']}" loading="lazy" decoding="async" alt="{a(alt_txt)}" data-alt-en="{a(item['alt_en'])}" data-alt-es="{a(item['alt_es'])}">
          </div>
          {bi("figcaption", item["caption_en"], item["caption_es"])}
          {cite(item["src"])}
        </figure>"""


def render_media_diptych(item_ids: tuple[str, str], is_es: bool, title_en: str, title_es: str) -> str:
    by_id = _media_map()
    cards = "\n".join(render_media_figure(by_id[mid], is_es, in_gallery=False) for mid in item_ids)
    return f"""      <aside class="sf-diptych-wrap" aria-label="{a(title_es if is_es else title_en)}">
        <p class="tp-kicker">{bi("span", title_en, title_es)}</p>
        <div class="sf-diptych">
{cards}
        </div>
      </aside>"""


def render_plaster_drawer(is_es: bool) -> str:
    e = C.EGG_BUTTON
    open_txt = e["button_es"] if is_es else e["button_en"]
    close_txt = e["close_es"] if is_es else e["close_en"]
    shard_svg = """<svg class="sf-shard-svg" viewBox="0 0 180 90" width="144" height="72" aria-hidden="true" focusable="false">
                <path class="sf-shard-body" d="M 18 76 L 18 32 L 154 32 L 154 76 Z"/>
                <line class="sf-shard-ruling" x1="28" y1="36" x2="72" y2="72"/>
                <line class="sf-shard-ruling" x1="56" y1="36" x2="100" y2="72"/>
                <line class="sf-shard-ruling" x1="84" y1="36" x2="128" y2="72"/>
                <line class="sf-shard-ruling" x1="112" y1="36" x2="148" y2="66"/>
                <g class="sf-shard-lid">
                  <path class="sf-shard-body" d="M 16 32 L 26 14 L 160 14 L 156 32 Z"/>
                  <line class="sf-shard-ruling" x1="36" y1="23" x2="144" y2="23"/>
                </g>
              </svg>"""
    by_id = _media_map()
    figs = [render_media_figure(by_id["photo-1988-site"], is_es), render_media_figure(by_id["plate-stereotomy-atelier"], is_es)]
    return f"""          <div class="sf-drawer">
            <button type="button" class="sf-drawer-btn" aria-expanded="false" aria-controls="sf-drawer-panel" data-label-open="{a(open_txt)}" data-label-close="{a(close_txt)}">
              {shard_svg}
              <span class="sf-drawer-copy">{bi("span", e["hint_en"], e["hint_es"], "sf-drawer-hint")}{bi("span", e["button_en"], e["button_es"], "sf-drawer-label")}</span>
            </button>
            <div class="sf-drawer-panel" id="sf-drawer-panel" hidden>
{chr(10).join(figs)}
            </div>
          </div>"""


def render_card(card: dict, is_es: bool) -> str:
    rows = []
    for en, es, value, key in card["plate"]:
        rows.append(
            f'<div class="sf-plate-row">{bi("dt", en, es)}<dd>{bi("span", value, C.VALUE_ES.get(value, value))} '
            f'{stamp(key)}</dd></div>'
        )
    drawer = render_plaster_drawer(is_es) if card.get("egg") else ""
    aria_plate = f"Ficha técnica {card['era']}" if is_es else f"Specification plate {card['era']}"
    return f"""        <article class="sf-card" id="move-{a(card['id'])}" data-move="{a(card['id'])}">
          <header>
            <p class="sf-card-era"><span>{t(card['era'])}</span> <span class="sf-card-years">{t(card['years'])}</span></p>
            {bi("h3", card["title_en"], card["title_es"], "sf-card-move")}
          </header>
          {bi("p", card["body_en"], card["body_es"], "sf-card-body")}
          <div class="sf-plate" role="group" aria-label="{a(aria_plate)}">
            <dl>{''.join(rows)}</dl>
            <p class="sf-plate-foot" data-en="Sources consulted {a(C.ACCESSED)}" data-es="Fuentes consultadas {a(C.ACCESSED)}">Sources consulted {t(C.ACCESSED)}</p>
          </div>
{drawer}
        </article>"""


def render_interlude(kind: str, is_es: bool) -> str:
    if kind == "ruled-comparison":
        rc = C.RULED_COMPARE
        head = "".join(bi("th", en, es, "", 'scope="col"') for en, es in zip(rc["head_en"], rc["head_es"]))
        rows = "".join(
            f'<tr>{bi("th", r[0], r[1], "", "scope=\"row\"")}{bi("td", r[2], r[3])}{bi("td", r[4], r[5])}</tr>'
            for r in rc["rows"]
        )
        return f"""          <aside class="sf-interlude" aria-labelledby="sf-int-cat">
            {bi("h3", rc["title_en"], rc["title_es"], "sf-int-h", 'id="sf-int-cat"')}
            <div class="sf-table-wrap"><table class="sf-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
            {bi("p", rc["note_en"], rc["note_es"], "sf-small")}
            {cite(rc["src"])}
          </aside>"""
    if kind == "quadrics":
        ql = C.QUADRICS_LEDGER
        rows = "".join(
            f'<div class="sf-anat-row">{bi("dt", en_t, es_t)}{bi("dd", en_b, es_b)}</div>'
            for en_t, es_t, en_b, es_b in ql["items"]
        )
        return f"""          <aside class="sf-interlude" aria-labelledby="sf-int-quad">
            {bi("h3", ql["title_en"], ql["title_es"], "sf-int-h", 'id="sf-int-quad"')}
            <dl>{rows}</dl>
            {cite(ql["src"])}
          </aside>"""
    if kind == "stone-hierarchy":
        cols = (("Points n", "Puntas n"), ("Stone", "Piedra"), ("Nave location", "Ubicación"),
                ("Total height (2n m)", "Altura total (2n m)"), ("Shaft (10·D_in)", "Fuste (10·D_int)"))
        head = "".join(bi("th", en, es, "", 'scope="col"') for en, es in cols)
        rows = "".join(
            f'<tr><td class="sf-num">{n}</td>{bi("th", st_en, st_es, "", "scope=\"row\"")}'
            f'{bi("td", pos_en, pos_es)}<td class="sf-num">{2 * n} m</td><td class="sf-num">{10 * d_in:.1f} m</td></tr>'
            for n, st_en, st_es, pos_en, pos_es, d_in, _ld in M.COLUMN_TIERS
        )
        return f"""          <aside class="sf-interlude" aria-labelledby="sf-int-stone">
            {bi("h3", "The four-stone hierarchical progression", "La progresión jerárquica de cuatro piedras", "sf-int-h", 'id="sf-int-stone"')}
            <div class="sf-table-wrap"><table class="sf-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
            {cite(["sf-booklets", "barrios2006", "grima2007"])}
          </aside>"""
    if kind == "towers-ledger":
        cols = (("Structure / Tower", "Estructura / Torre"), ("Elevation", "Elevación"), ("Attribution", "Atribución"))
        head = "".join(bi("th", en, es, "", 'scope="col"') for en, es in cols)
        rows = "".join(
            f'<tr>{bi("th", en, es, "", "scope=\"row\"")}<td class="sf-num sf-strong">{h_m:.1f} m</td><td>{t(src_note)}</td></tr>'
            for en, es, h_m, src_note in M.TOWERS_LEDGER
        )
        return f"""          <aside class="sf-interlude" aria-labelledby="sf-int-towers">
            {bi("h3", "18 Basilica spires vs. Ulm Minster &amp; Montjuïc", "Las 18 torres frente a Ulm y Montjuïc", "sf-int-h", 'id="sf-int-towers"')}
            <div class="sf-table-wrap"><table class="sf-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
            {cite(["sf-cross-2026", "sf-evangelists", "sf-inauguration-2026"])}
          </aside>"""
    return ""


def render_tectonic_loupe_section(is_es: bool) -> str:
    """Dual-scale 1:500 Basilica elevation hotspots paired with 1:10 stereotomy detail views."""
    lx = C.TECTONIC_LOUPE_TEXT
    btns = "".join(
        f'<button type="button" class="sf-pill-btn" data-sf-node="{i}" aria-pressed="{"true" if i == 0 else "false"}" '
        f'data-en="{a(n["short_en"])}" data-es="{a(n["short_es"])}">{t(n["short_es"] if is_es else n["short_en"])}</button>'
        for i, n in enumerate(C.LOUPE_NODES)
    )
    info_cards = []
    for i, n in enumerate(C.LOUPE_NODES):
        hid = "" if i == 0 else " hidden"
        info_cards.append(
            f"""            <div class="sf-loupe-detail" data-sf-node-card="{i}"{hid}>
              <div class="sf-relay-head">{bi("h3", n["title_en"], n["title_es"], "sf-card-move")}<span class="sf-panel-tag">{t(n["elev"])}</span></div>
              {bi("p", n["summary_en"], n["summary_es"], "sf-small")}
              {cite(n["src"])}
            </div>"""
        )
    sec_svg = """<svg class="sf-svg-stage" viewBox="0 0 260 320" width="260" height="320" role="img" aria-labelledby="sf-sec-500-t">
              <title id="sf-sec-500-t">1:500 Basilica schematic elevation with four clickable structural scale markers</title>
              <line class="sf-funicular-axis" x1="20" y1="290" x2="240" y2="290"/>
              <path class="sf-loupe-sec-hull" d="M 52 290 L 58 210 L 82 210 L 94 140 L 112 72 L 130 28 L 148 72 L 166 140 L 178 210 L 202 210 L 208 290 Z"/>
              <line class="sf-funicular-column" x1="92" y1="290" x2="96" y2="210"/>
              <line class="sf-funicular-column" x1="168" y1="290" x2="164" y2="210"/>
              <line class="sf-stress-tens" x1="130" y1="18" x2="130" y2="38"/>
              <line class="sf-stress-tens" x1="122" y1="26" x2="138" y2="26"/>
              <g class="sf-loupe-node is-active" data-sf-node-dot="0"><circle cx="92" cy="290" r="8"/><text class="sf-svg-sub-text" x="108" y="294">0 m</text></g>
              <g class="sf-loupe-node" data-sf-node-dot="1"><circle cx="96" cy="240" r="8"/><text class="sf-svg-sub-text" x="112" y="244">24 m</text></g>
              <g class="sf-loupe-node" data-sf-node-dot="2"><circle cx="130" cy="204" r="8"/><text class="sf-svg-sub-text" x="145" y="208">45–60 m</text></g>
              <g class="sf-loupe-node" data-sf-node-dot="3"><circle cx="130" cy="48" r="8"/><text class="sf-svg-sub-text" x="146" y="52">172.5 m</text></g>
            </svg>"""
    loupe_svg = """<svg class="sf-svg-stage" viewBox="0 0 320 260" width="320" height="260" role="img" aria-labelledby="sf-loupe-10-t">
              <title id="sf-loupe-10-t">1:10 architectural stereotomy and joint detail matching selected zone</title>
              <g class="sf-loupe-view is-active" data-sf-loupe-view="0">
                <rect class="sf-panel-outline" x="50" y="185" width="220" height="36" rx="2"/>
                <rect class="sf-loupe-sec-hull" x="104" y="45" width="112" height="140" rx="4"/>
                <line class="sf-funicular-catenary" x1="125" y1="45" x2="125" y2="215"/>
                <line class="sf-funicular-catenary" x1="160" y1="45" x2="160" y2="215"/>
                <line class="sf-funicular-catenary" x1="195" y1="45" x2="195" y2="215"/>
                <text class="sf-svg-caption-text" x="160" y="32" text-anchor="middle">1:10 Crypt Bearing Plinth (1882)</text>
              </g>
              <g class="sf-loupe-view" data-sf-loupe-view="1" hidden>
                <rect class="sf-loupe-sec-hull" x="132" y="138" width="56" height="96"/>
                <polygon class="sf-star-core" points="124,132 160,104 196,132 160,152"/>
                <line class="sf-funicular-column" x1="142" y1="120" x2="72" y2="38"/>
                <line class="sf-funicular-column" x1="160" y1="112" x2="160" y2="34"/>
                <line class="sf-funicular-column" x1="178" y1="120" x2="248" y2="38"/>
                <text class="sf-svg-caption-text" x="160" y="24" text-anchor="middle">1:10 Ellipsoid Branch Knot</text>
              </g>
              <g class="sf-loupe-view" data-sf-loupe-view="2" hidden>
                <path class="sf-hyp-ruling-pos" d="M 60 56 Q 160 112 260 56"/>
                <path class="sf-hyp-ruling-pos" d="M 76 206 Q 160 144 244 206"/>
                <line class="sf-hyp-ruling-neg" x1="68" y1="60" x2="220" y2="202"/>
                <line class="sf-hyp-ruling-neg" x1="252" y1="60" x2="100" y2="202"/>
                <circle class="sf-star-core" cx="160" cy="130" r="24"/>
                <text class="sf-svg-caption-text" x="160" y="30" text-anchor="middle">1:10 Ruled Hyperboloid Oculus Ring</text>
              </g>
              <g class="sf-loupe-view" data-sf-loupe-view="3" hidden>
                <rect class="sf-panel-outline" x="92" y="54" width="136" height="162" rx="4"/>
                <rect class="sf-loupe-sec-hull" x="122" y="84" width="76" height="102" rx="2"/>
                <line class="sf-duct-line" x1="107" y1="42" x2="107" y2="228"/>
                <line class="sf-duct-line" x1="213" y1="42" x2="213" y2="228"/>
                <line class="sf-stress-tens" x1="160" y1="40" x2="160" y2="82"/>
                <text class="sf-svg-caption-text" x="160" y="28" text-anchor="middle">1:10 Hollow PT Panel &amp; Rods</text>
              </g>
            </svg>"""
    return f"""      <section class="sf-observatory" id="tectonic-section" data-sf-loupe aria-labelledby="sf-loupe-h">
        <p class="tp-kicker">{bi("span", lx["kicker_en"], lx["kicker_es"])}</p>
        {bi("h2", lx["title_en"], lx["title_es"], "sf-h2", 'id="sf-loupe-h"')}
        {bi("p", lx["intro_en"], lx["intro_es"], "sf-lede")}
        <div class="sf-pill-bar" role="group" aria-label="Structural scale selector">{btns}</div>
        <div class="sf-loupe-grid">
          <div class="sf-panel">
            <div class="sf-panel-head">{bi("span", "1:500 Schematic Section", "Sección esquemática 1:500", "sf-panel-tag")}<span class="sf-panel-tag">SVG · CLICK NODE</span></div>
            {sec_svg}
          </div>
          <div class="sf-panel">
            <div class="sf-panel-head">{bi("span", "1:10 Nodal Stereotomy Loupe", "Lupa estereotómica 1:10", "sf-panel-tag")}<span class="sf-panel-tag">DETAIL VIEW</span></div>
            {loupe_svg}
{chr(10).join(info_cards)}
          </div>
        </div>
      </section>"""


def render_sankey_ribbon(is_es: bool) -> str:
    """Alluvial / Sankey conservation ribbon comparing branched piers vs flying-buttress thrust split."""
    sx = C.SANKEY_TEXT
    btn_g = f'<button type="button" class="sf-pill-btn" data-sf-loadpath="gaudi" aria-pressed="true" data-en="Gaudí Branched Canopy" data-es="Bosque ramificado (Gaudí)">{t("Bosque ramificado (Gaudí)" if is_es else "Gaudí Branched Canopy")}</button>'
    btn_c = f'<button type="button" class="sf-pill-btn" data-sf-loadpath="gothic" aria-pressed="false" data-en="Gothic Flying-Buttress Split" data-es="Arbotantes góticos">{t("Arbotantes góticos" if is_es else "Gothic Flying-Buttress Split")}</button>'
    svg = """<svg class="sf-svg-stage sf-sankey-svg" viewBox="0 0 640 210" width="640" height="210" role="img" aria-labelledby="sf-sankey-t">
              <title id="sf-sankey-t">Alluvial gravity load path diagram comparing branched internal piers against external flying buttresses</title>
              <rect class="sf-loupe-sec-hull" x="28" y="64" width="24" height="82" rx="3"/>
              <text class="sf-svg-caption-text" x="16" y="48" text-anchor="start">360 kN Vault</text>
              <g class="is-active" data-sf-sankey-mode="gaudi">
                <path class="sf-sankey-flow sf-sankey-primary" d="M 52 84 C 170 84, 210 66, 320 66 L 560 66"/>
                <path class="sf-sankey-flow sf-sankey-secondary" d="M 52 126 C 170 126, 210 132, 320 132 L 560 132"/>
                <rect class="sf-star-core" x="560" y="42" width="24" height="114" rx="3"/>
                <text class="sf-svg-sub-text" x="305" y="48" text-anchor="middle">180 kN primary piers + 180 kN aisle piers (internal)</text>
                <text class="sf-svg-caption-text" x="572" y="182" text-anchor="end">External crutches: 0 kN</text>
              </g>
              <g data-sf-sankey-mode="gothic" hidden>
                <path class="sf-sankey-flow sf-sankey-primary" d="M 52 90 C 170 90, 210 74, 320 74 L 560 74"/>
                <path class="sf-sankey-flow sf-sankey-crutch" d="M 52 134 C 170 134, 210 170, 320 170 L 560 170"/>
                <rect class="sf-star-core" x="560" y="54" width="24" height="44" rx="3"/>
                <rect class="sf-loupe-sec-hull" x="560" y="152" width="24" height="36" rx="3"/>
                <text class="sf-svg-sub-text" x="305" y="56" text-anchor="middle">240 kN vertical shaft</text>
                <text class="sf-svg-sub-text" x="305" y="192" text-anchor="middle">120 kN lateral thrust bypassed externally</text>
              </g>
            </svg>"""
    return f"""        <div class="sf-sankey-box" data-sf-sankey>
          <div class="sf-panel-head">
            {bi("span", sx["kicker_en"], sx["kicker_es"], "sf-panel-tag")}
            <span class="sf-panel-tag">SVG · ALLUVIAL FLOW</span>
          </div>
          {bi("h3", sx["title_en"], sx["title_es"], "sf-card-move")}
          {bi("p", sx["intro_en"], sx["intro_es"], "sf-small")}
          <div class="sf-pill-bar" role="group" aria-label="Load path comparison">{btn_g}{btn_c}</div>
          <div class="sf-svg-scroll">{svg}</div>
          <p class="sf-readout" data-sf-sankey-readout aria-live="polite" data-gaudi-en="{a(sx['readout_gaudi_en'])}" data-gaudi-es="{a(sx['readout_gaudi_es'])}" data-gothic-en="{a(sx['readout_gothic_en'])}" data-gothic-es="{a(sx['readout_gothic_es'])}">{t(sx['readout_gaudi_es'] if is_es else sx['readout_gaudi_en'])}</p>
          <table class="sr-only"><caption>MODEL 360 kN canopy load split comparison</caption><thead><tr><th>Topology</th><th>Internal Piers</th><th>External Flying Buttresses</th></tr></thead><tbody><tr><td>Gaudí Branched Canopy</td><td>360 kN</td><td>0 kN</td></tr><tr><td>Gothic Split</td><td>240 kN</td><td>120 kN</td></tr></tbody></table>
          {cite(sx["src"])}
        </div>"""


def render_polar_radar(is_es: bool) -> str:
    """6-Axis Polar Structural & Acoustic Comparative Radar (MODEL comparative index 0-100)."""
    rx = C.RADAR_TEXT
    axes_en, axes_es = rx["axes_en"], rx["axes_es"]
    cx, cy, r_max = 240.0, 160.0, 94.0
    angles = [-math.pi / 2 + i * (math.pi / 3) for i in range(6)]
    rings = ""
    for frac in (0.33, 0.66, 1.0):
        pts = " ".join(f"{cx + r_max * frac * math.cos(th):.1f},{cy + r_max * frac * math.sin(th):.1f}" for th in angles)
        rings += f'<polygon class="sf-funicular-parabola" points="{pts}"/>'
    spokes = "".join(
        f'<line class="sf-funicular-axis" x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx + r_max * math.cos(th):.1f}" y2="{cy + r_max * math.sin(th):.1f}"/>'
        for th in angles
    )
    labels = ""
    for i, th in enumerate(angles):
        lx = cx + (r_max + 20) * math.cos(th)
        ly = cy + (r_max + 20) * math.sin(th) + 4
        anc = "middle" if abs(math.cos(th)) < 0.25 else ("start" if math.cos(th) > 0 else "end")
        labels += f'<text class="sf-svg-sub-text" x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anc}" data-en="{a(axes_en[i])}" data-es="{a(axes_es[i])}">{t(axes_es[i] if is_es else axes_en[i])}</text>'
    init_scores = C.RADAR_ERAS[-1]["scores"]
    init_pts = " ".join(f"{cx + r_max * (sc / 100.0) * math.cos(angles[i]):.1f},{cy + r_max * (sc / 100.0) * math.sin(angles[i]):.1f}" for i, sc in enumerate(init_scores))
    era_btns = "".join(
        f'<button type="button" class="sf-pill-btn" data-sf-radar-era="{a(e["id"])}" '
        f'data-scores="{",".join(str(x) for x in e["scores"])}" '
        f'data-note-en="{a(e["note_en"])}" data-note-es="{a(e["note_es"])}" '
        f'aria-pressed="{"true" if idx == len(C.RADAR_ERAS) - 1 else "false"}" '
        f'data-en="{a(e["label_en"])}" data-es="{a(e["label_es"])}">{t(e["label_es"] if is_es else e["label_en"])}</button>'
        for idx, e in enumerate(C.RADAR_ERAS)
    )
    sr_rows = "".join(
        f"<tr><th scope='row'>{t(e['label_en'])}</th>" + "".join(f"<td>{sc}</td>" for sc in e["scores"]) + "</tr>"
        for e in C.RADAR_ERAS
    )
    init_e = C.RADAR_ERAS[-1]
    return f"""        <div class="sf-part sf-radar-panel" data-sf-radar aria-labelledby="sf-radar-h">
          <p class="tp-kicker">{bi("span", rx["kicker_en"], rx["kicker_es"])}</p>
          {bi("h2", rx["title_en"], rx["title_es"], "sf-h2", 'id="sf-radar-h"')}
          {bi("p", rx["intro_en"], rx["intro_es"], "sf-lede")}
          <div class="sf-bench">
            <svg class="sf-svg-stage sf-radar-svg" viewBox="0 0 480 320" width="480" height="320" role="img" aria-labelledby="sf-radar-t">
              <title id="sf-radar-t">Six-axis polar structural and acoustic envelope comparison (MODEL comparative index 0 to 100)</title>
              {rings}{spokes}
              <polygon class="sf-radar-poly" points="{init_pts}"/>
              {labels}
            </svg>
            <div class="sf-controls">
              <div class="sf-pill-bar" role="group" aria-label="Era radar comparison selector">{era_btns}</div>
              <p class="sf-readout" data-sf-radar-readout aria-live="polite">{t(init_e['note_es'] if is_es else init_e['note_en'])}</p>
              <table class="sr-only"><caption>MODEL 6-axis comparative structural and acoustic scores</caption><thead><tr><th>Era</th>{"".join(f"<th>{t(ax)}</th>" for ax in axes_en)}</tr></thead><tbody>{sr_rows}</tbody></table>
              {cite(rx["src"])}
            </div>
          </div>
        </div>"""


def render_visual_gallery_section(is_es: bool) -> str:
    """Filterable 10-item Visual Media Archive paired with a CSP-safe native <dialog> lightbox."""
    vg = C.VISUAL_GALLERY_TEXT
    cards = "\n".join(render_media_figure(item, is_es, in_gallery=True) for item in (*C.PHOTOS, *C.PLATES))
    btns = (
        f'<button type="button" class="sf-pill-btn" data-sf-filter="all" aria-pressed="true" data-en="{a(vg["all_en"])}" data-es="{a(vg["all_es"])}">{t(vg["all_es"] if is_es else vg["all_en"])}</button>'
        f'<button type="button" class="sf-pill-btn" data-sf-filter="photo" aria-pressed="false" data-en="{a(vg["photos_en"])}" data-es="{a(vg["photos_es"])}">{t(vg["photos_es"] if is_es else vg["photos_en"])}</button>'
        f'<button type="button" class="sf-pill-btn" data-sf-filter="render" aria-pressed="false" data-en="{a(vg["renders_en"])}" data-es="{a(vg["renders_es"])}">{t(vg["renders_es"] if is_es else vg["renders_en"])}</button>'
    )
    return f"""      <section class="sf-observatory" id="visuals" data-sf-gallery aria-labelledby="sf-vis-h">
        <p class="tp-kicker">{bi("span", vg["kicker_en"], vg["kicker_es"])}</p>
        {bi("h2", vg["title_en"], vg["title_es"], "sf-h2", 'id="sf-vis-h"')}
        {bi("p", vg["intro_en"], vg["intro_es"], "sf-lede")}
        <div class="sf-pill-bar" role="group" aria-label="Visual media filter">{btns}</div>
        <div class="sf-gallery-grid">
{cards}
        </div>
        <dialog class="sf-lightbox" id="sf-lightbox" aria-labelledby="sf-lb-badge" aria-describedby="sf-lb-cap">
          <div class="sf-lightbox-bar">
            <span class="sf-panel-tag" id="sf-lb-badge">MEDIA</span>
            <div class="sf-pill-bar">
              <button type="button" class="sf-btn sf-btn-quiet" data-sf-lb-prev data-en="Prev" data-es="Anterior">{t("Anterior" if is_es else "Prev")}</button>
              <button type="button" class="sf-btn sf-btn-quiet" data-sf-lb-next data-en="Next" data-es="Siguiente">{t("Siguiente" if is_es else "Next")}</button>
              <button type="button" class="sf-btn" data-sf-lb-close data-en="Close" data-es="Cerrar">{t("Cerrar" if is_es else "Close")}</button>
            </div>
          </div>
          <div class="sf-lightbox-stage">
            <img id="sf-lightbox-img" src="../../images/sagrada-familia/photo-2026-completed-cross.jpg" width="1280" height="1855" decoding="async" alt="">
          </div>
          <p class="sf-small" id="sf-lb-cap"></p>
        </dialog>
      </section>"""


def render_part(part: dict, is_es: bool) -> str:
    cards = {c["id"]: c for c in C.CARDS}
    opener_paras = []
    for i, p in enumerate(part["opener"]):
        cls = "sf-dropcap" if i == 0 else ""
        opener_paras.append(f'          {bi("p", p["en"], p["es"], cls)}\n          {cite(p["src"])}')
    cards_html = "\n".join(render_card(cards[cid], is_es) for cid in part["cards"])
    interlude_html = render_interlude(part["interlude"], is_es)
    part_visuals = ""
    if part["id"] == "part-1":
        part_visuals = render_media_diptych(
            ("photo-catenary-model", "plate-reus-forge"),
            is_es,
            "Part I Visual Study · Hanging-Chain Statics Photo & Reus Coppersmith Visualization",
            "Estudio visual Parte I · Foto de maqueta funicular e imaginación del taller de Reus",
        )
    elif part["id"] == "part-2":
        part_visuals = (
            render_tectonic_loupe_section(is_es)
            + "\n"
            + render_media_diptych(
                ("photo-nativity-facade", "photo-nave-columns"),
                is_es,
                "Part II Site Photographs · Exterior Parabolic Spires & Interior Four-Stone Tree Canopy",
                "Fotografías Parte II · Campanarios del Nacimiento y bosque interior de cuatro piedras",
            )
        )
    elif part["id"] == "part-4":
        part_visuals = render_media_diptych(
            ("plate-nave-forest", "plate-tensioned-crown"),
            is_es,
            "Part IV Conceptual Studies · Interior Stained-Glass Forest & Hollow Post-Tensioned Stone",
            "Estudios conceptuales Parte IV · Vitrales en el bosque pétreo y paneles huecos pretensados",
        )
    return f"""      <section class="sf-part" id="{a(part['id'])}" aria-labelledby="{a(part['id'])}-h">
        <header class="sf-part-head">
          <p class="sf-part-num" aria-hidden="true">{t(part['numeral'])}</p>
          <h2 class="sf-h2 sf-part-title" id="{a(part['id'])}-h"><span data-en="Part {a(part['numeral'])}" data-es="Parte {a(part['numeral'])}">Part {t(part['numeral'])}</span> · {bi("span", part["title_en"], part["title_es"])}</h2>
          <p class="sf-part-years">{t(part['years'])}</p>
        </header>
        <div class="sf-part-opener-grid">
          <div class="sf-part-opener">
{chr(10).join(opener_paras)}
          </div>
          {bi("blockquote", part["pull_en"], part["pull_es"], "sf-pull")}
        </div>
{cards_html}
{interlude_html}
{part_visuals}
      </section>"""


# --------------------------------------------------------------------------------------------- interactive observatories

def render_atelier_section(is_es: bool) -> str:
    ax = C.ATELIER_TEXT
    f = M.FUNICULAR_MODEL
    eq = M.funicular_equilibrium()
    surface_modes = [
        ("column", "Star Column", "Columna estrellada"),
        ("hyperboloid", "Hyperboloid Oculus", "Hiperboloide"),
        ("hypar", "Hypar Saddle", "Paraboloide"),
        ("conoid", "Schools Conoid", "Conoide"),
    ]
    surf_btns = "".join(
        f'<button type="button" class="sf-pill-btn" data-sf-surface="{m}" aria-pressed="{"true" if m == "column" else "false"}" '
        f'data-en="{a(en)}" data-es="{a(es)}">{t(es if is_es else en)}</button>'
        for m, en, es in surface_modes
    )
    n_btns = "".join(
        f'<button type="button" class="sf-pill-btn" data-sf-n="{n}" aria-pressed="{"true" if n == 12 else "false"}">{n}-pt</button>'
        for n in (6, 8, 10, 12)
    )
    svg_fun = """<svg class="sf-funicular-svg sf-svg-stage" viewBox="0 0 460 330" width="460" height="330" role="img" aria-labelledby="sf-fun-svg-title">
              <title id="sf-fun-svg-title">Coupled 2D hanging catenary vs parabola diagram driving pier inclination angle</title>
              <line class="sf-funicular-axis" x1="36" y1="248" x2="424" y2="248"/>
              <line class="sf-funicular-axis" x1="230" y1="32" x2="230" y2="306"/>
              <g class="sf-funicular-buttress-l"><line class="sf-funicular-buttress" x1="60" y1="248" x2="28" y2="302"/><line class="sf-funicular-buttress" x1="28" y1="200" x2="28" y2="310"/></g>
              <g class="sf-funicular-buttress-r"><line class="sf-funicular-buttress" x1="400" y1="248" x2="432" y2="302"/><line class="sf-funicular-buttress" x1="432" y1="200" x2="432" y2="310"/></g>
              <line class="sf-funicular-column sf-funicular-column-l" x1="60" y1="248" x2="42" y2="307"/>
              <line class="sf-funicular-column sf-funicular-column-r" x1="400" y1="248" x2="418" y2="307"/>
              <path class="sf-funicular-parabola" d="M 60 248 Q 230 100 400 248"/>
              <path class="sf-funicular-catenary" d="M 60 248 Q 230 92 400 248"/>
              <path class="sf-funicular-load" d="M 230 56 L 230 88"/>
              <circle class="sf-funicular-node" cx="60" cy="248" r="4.5"/>
              <circle class="sf-funicular-node" cx="400" cy="248" r="4.5"/>
              <text class="sf-svg-caption-text" x="48" y="320" data-en="Inclined pier line θ = arctan(H/V)" data-es="Línea de columna θ = arctan(H/V)">Inclined pier line θ = arctan(H/V)</text>
              <text class="sf-svg-sub-text" x="308" y="42" data-en="Dashed: Parabola" data-es="Punteado: Parábola">Dashed: Parabola</text>
            </svg>"""
    return f"""      <section class="sf-observatory" id="atelier" data-sf-atelier data-span="{f['span_m']}" data-wkn="{f['w_kn_per_m']}" aria-labelledby="sf-atelier-h">
        <p class="tp-kicker">{bi("span", ax["kicker_en"], ax["kicker_es"])}</p>
        {bi("h2", ax["title_en"], ax["title_es"], "sf-h2", 'id="sf-atelier-h"')}
        {bi("p", ax["intro_en"], ax["intro_es"], "sf-lede sf-dropcap")}
        <div class="sf-atelier-grid">
          <div class="sf-panel">
            <div class="sf-panel-head">
              {bi("span", "2D Hanging Chain Solver", "Solucionador 2D de Catenaria", "sf-panel-tag")}
              <span class="sf-panel-tag">SVG · LIVE STATICS</span>
            </div>
            {svg_fun}
            <div class="sf-controls-row">
              <div class="sf-control-group">
                <label class="sf-range-label" for="sf-lantern-range"><span>{bi("span", "Crown lantern load W_top", "Carga de linterna W_top")}</span><span class="sf-range-val" id="sf-lantern-val">{f['lantern_load_kn']:.0f} kN</span></label>
                <input id="sf-lantern-range" class="sf-range" type="range" min="{f['lantern_min_kn']:.0f}" max="{f['lantern_max_kn']:.0f}" step="10" value="{f['lantern_load_kn']:.0f}" aria-valuetext="{f['lantern_load_kn']:.0f} kN">
              </div>
              <div class="sf-control-group">
                <label class="sf-range-label" for="sf-catenary-a-range"><span>{bi("span", "Catenary scale a = H/w", "Parámetro catenario a = H/w")}</span><span class="sf-range-val" id="sf-catenary-a-val">{f['catenary_a_m']:.1f} m</span></label>
                <input id="sf-catenary-a-range" class="sf-range" type="range" min="4.0" max="10.0" step="0.2" value="{f['catenary_a_m']:.1f}" aria-valuetext="{f['catenary_a_m']:.1f} m">
              </div>
            </div>
            <div class="sf-check-row">
              <label class="sf-check"><input type="checkbox" id="sf-invert-gravity" checked> {bi("span", "Invert hanging cord into compression arch", "Invertir cordel en arco a compresión")}</label>
              <label class="sf-check"><input type="checkbox" id="sf-show-buttress" checked> {bi("span", "Show external Gothic crutches", "Mostrar arbotantes góticos externos")}</label>
            </div>
            <p class="sf-readout" data-sf-fun-readout aria-live="polite">MODEL thrust H = {eq['H_kn']:.1f} kN · V = {eq['V_kn']:.1f} kN · Column tilt from vertical θ = {eq['tilt_from_vertical_deg']:.2f}°</p>
          </div>
          <div class="sf-panel">
            <div class="sf-panel-head">
              {bi("span", "3D Watertight Ruled Stereotomy", "Estereotomía Reglada 3D Cerrada", "sf-panel-tag")}
              <span class="sf-panel-tag">WebGL2 · .GLB · .DXF</span>
            </div>
            <div class="sf-pill-bar" role="group" aria-label="Surface family selector">{surf_btns}</div>
            <div class="sf-pill-bar" role="group" aria-label="Star column points selector">{n_btns}</div>
            <div class="sf-canvas-wrap">
              <canvas id="sf-webgl-canvas" class="sf-webgl-canvas" width="640" height="480" tabindex="0" aria-label="Interactive 3D stereotomy turntable (drag to orbit, wheel to zoom, arrow keys to rotate)"></canvas>
            </div>
            <div class="sf-check-row">
              <label class="sf-check"><input type="checkbox" id="sf-show-rulings" checked> {bi("span", "Overlay straight wire-cut rulings", "Superponer rectas generatrices")}</label>
            </div>
            <div class="sf-export-row">
              <button type="button" class="sf-btn" data-sf-export="glb" data-en="Export 3D Model (.glb)" data-es="Exportar Modelo 3D (.glb)">Export 3D Model (.glb)</button>
              <button type="button" class="sf-btn sf-btn-quiet" data-sf-export="dxf" data-en="Export CAD Wireframe (.dxf)" data-es="Exportar Plantilla CAD (.dxf)">Export CAD Wireframe (.dxf)</button>
            </div>
            <p class="sf-readout" data-sf-cad-readout aria-live="polite">Stereotomy mesh ready · Tilt θ = {eq['tilt_from_vertical_deg']:.2f}°</p>
          </div>
        </div>
        <div class="sf-science">
          {bi("p", ax["science_en"], ax["science_es"])}
          {cite(["heyman1966", "huerta2006", "akbarzadeh2015"])}
        </div>
{render_sankey_ribbon(is_es)}
      </section>"""


def render_relay_section(is_es: bool) -> str:
    """Five-generation human continuity observatory (1882–2026+)."""
    rx = C.RELAY_TEXT
    btns = []
    segs = []
    cards = []
    # Proportional 1882–2026+ spans across 680 px SVG bar
    seg_x = (16, 174, 294, 418, 538)
    seg_w = (148, 110, 114, 110, 126)
    for i, g in enumerate(C.GENERATIONS_RELAY):
        pressed = "true" if i == 0 else "false"
        active_cls = " sf-relay-seg is-active" if i == 0 else " sf-relay-seg"
        btns.append(
            f'<button type="button" class="sf-pill-btn" data-sf-gen="{i}" aria-pressed="{pressed}" '
            f'data-en="{a(g["span_label"])}" data-es="{a(g["span_label_es"])}">{t(g["span_label_es"] if is_es else g["span_label"])}</button>'
        )
        segs.append(
            f'<g class="{active_cls.strip()}" data-sf-seg="{i}">'
            f'<rect class="sf-relay-bar" x="{seg_x[i]}" y="22" width="{seg_w[i]}" height="26" rx="4"/>'
            f'<text class="sf-svg-caption-text" x="{seg_x[i] + seg_w[i] / 2:.1f}" y="39" text-anchor="middle">{t(g["years"])}</text>'
            f'<text class="sf-svg-sub-text" x="{seg_x[i] + seg_w[i] / 2:.1f}" y="68" text-anchor="middle">Gen {i + 1}</text>'
            f"</g>"
        )
        hid = "" if i == 0 else " hidden"
        cards.append(
            f"""          <article class="sf-relay-card" data-sf-relay-card="{i}"{hid}>
            <div class="sf-relay-head">
              {bi("h3", g["title_en"], g["title_es"], "sf-card-move")}
              <span class="sf-panel-tag">{t(g["elevation"])}</span>
            </div>
            <dl class="sf-relay-grid">
              <div class="sf-relay-row">{bi("dt", "Who held the site", "Quién sostuvo la obra")}{bi("dd", g["hands_en"], g["hands_es"])}</div>
              <div class="sf-relay-row">{bi("dt", "Historical crucible", "Prueba histórica")}{bi("dd", g["challenge_en"], g["challenge_es"])}</div>
              <div class="sf-relay-row">{bi("dt", "Gift handed forward", "Legado al relevo siguiente")}{bi("dd", g["gift_en"], g["gift_es"])}</div>
            </dl>
            {cite(g["src"])}
          </article>"""
        )

    timeline_svg = f"""<svg class="sf-svg-stage sf-relay-stage" viewBox="0 0 680 88" width="680" height="88" role="img" aria-labelledby="sf-relay-svg-t">
              <title id="sf-relay-svg-t">Five architectural generations carrying the Sagrada Família across 1882 to 2026+</title>
              <line class="sf-funicular-axis" x1="16" y1="35" x2="664" y2="35"/>
              {"".join(segs)}
            </svg>"""
    return f"""      <section class="sf-observatory sf-relay" id="relay" data-sf-relay aria-labelledby="sf-relay-h">
        <p class="tp-kicker">{bi("span", rx["kicker_en"], rx["kicker_es"])}</p>
        {bi("h2", rx["title_en"], rx["title_es"], "sf-h2", 'id="sf-relay-h"')}
        {bi("p", rx["intro_en"], rx["intro_es"], "sf-lede")}
        <div class="sf-pill-bar" role="group" aria-label="Generation relay selector">{"".join(btns)}</div>
        {timeline_svg}
{chr(10).join(cards)}
      </section>"""


def render_shard_svg() -> str:
    """Multi-point 3.0 m hyperboloid profile recovered from a 0.35 m 1936 plaster shard vs unruled Taylor drift."""
    p = M.SHARD_RECOVERY_MODEL
    a_t, c_t = p["a_true_m"], p["c_true_m"]
    k_t = (a_t / c_t) ** 2
    z1, z2, z_top = p["z1_m"], p["z2_m"], p["z_target_m"]
    r_true = lambda z: math.sqrt(a_t * a_t + k_t * z * z)
    r1 = r_true(z1)
    dr1 = (k_t * z1) / r1
    d2r1 = (k_t * a_t * a_t) / (r1 ** 3)
    r_free = lambda z: r1 + dr1 * (z - z1) + 0.5 * d2r1 * ((z - z1) ** 2)
    pts_str = lambda fn, z0, z1_, steps: " ".join(
        f"{75.0 + ((fn(z0 + (z1_ - z0) * i / steps) - 1.5) / 1.8) * 215.0:.1f},"
        f"{220.0 - ((z0 + (z1_ - z0) * i / steps) / z_top) * 190.0:.1f}"
        for i in range(steps + 1)
    )
    pts_t = pts_str(r_true, 0.0, z_top, 15)
    pts_f = pts_str(r_free, z1, z_top, 14)
    pts_p = pts_str(r_true, z1, z2, 4)
    return f"""<svg class="sf-shard-recover-svg sf-svg-stage" viewBox="0 0 340 250" width="340" height="250" role="img" aria-labelledby="sf-shard-svg-t">
              <title id="sf-shard-svg-t">Full 3.0 m hyperboloid profile recovered from a 0.35 m 1936 plaster shard vs unruled freeform Taylor drift</title>
              <line class="sf-funicular-axis" x1="48" y1="220" x2="310" y2="220"/>
              <line class="sf-funicular-axis" x1="48" y1="20" x2="48" y2="220"/>
              <polyline class="sf-shard-true" points="{pts_t}"/>
              <polyline class="sf-shard-freeform" points="{pts_f}"/>
              <polyline class="sf-shard-ruled" points="{pts_t}"/>
              <polyline class="sf-shard-piece" points="{pts_p}"/>
              <text class="sf-svg-caption-text" x="56" y="24" data-en="z = 3.00 m vault rim" data-es="z = 3.00 m corona de bóveda">z = 3.00 m vault rim</text>
              <text class="sf-svg-sub-text" x="180" y="200" data-en="0.35 m surviving shard" data-es="Fragmento 0.35 m">0.35 m surviving shard</text>
            </svg>"""


def render_benches_section(is_es: bool) -> str:
    cb, tb, lb = C.COL_BENCH_TEXT, C.TOWER_BENCH_TEXT, C.LIGHT_BENCH_TEXT
    tier_radios = "".join(
        f'<label class="sf-check"><input type="radio" name="sf-col-tier" value="{n}"{" checked" if n == 12 else ""}> '
        f'{bi("span", f"{n}-pt · {st_en}", f"{n} pts · {st_es}")}</label>'
        for n, st_en, st_es, *_r in M.COLUMN_TIERS
    )
    s12 = M.counter_twisted_section(12, 2.10, 29000.0, 0.5)

    # 18-Tower Skyline Bar Chart SVG (scaled 0..190 m -> y 210..20)
    bar_elems = []
    for i, (en, es, h_m, _src) in enumerate(M.TOWERS_LEDGER):
        bx = 34 + i * 38
        bh = (h_m / 190.0) * 180.0
        by = 205.0 - bh
        if abs(h_m - 172.5) < 0.2:
            cls = "sf-tower-bar sf-tower-bar-jc"
        elif abs(h_m - 161.5) < 0.2:
            cls = "sf-tower-bar sf-tower-bar-ulm"
        else:
            cls = "sf-tower-bar"
        bar_elems.append(f'<rect class="{cls}" x="{bx}" y="{by:.1f}" width="26" height="{bh:.1f}" rx="2"/>')
        bar_elems.append(f'<text class="sf-svg-caption-text" x="{bx + 13}" y="{by - 5:.1f}" text-anchor="middle">{h_m:.1f}</text>')
    mont_y = 205.0 - (177.7 / 190.0) * 180.0
    skyline_svg = f"""<svg class="sf-svg-stage" viewBox="0 0 385 230" width="385" height="230" role="img" aria-labelledby="sf-tower-svg-t">
              <title id="sf-tower-svg-t">Heights of Sagrada Família towers compared against Ulm Minster (161.5 m) and Montjuïc (177.7 m)</title>
              <line class="sf-funicular-axis" x1="20" y1="205" x2="375" y2="205"/>
              <line class="sf-datum-line" x1="20" y1="{mont_y:.1f}" x2="375" y2="{mont_y:.1f}"/>
              <text class="sf-svg-caption-text" x="26" y="{mont_y - 6:.1f}">Montjuïc 177.7 m (datum)</text>
              {"".join(bar_elems)}
            </svg>"""
    pt0 = M.panel_decompression()
    p_tp = M.TOWER_PANEL_MODEL
    stress_svg = """<svg class="sf-svg-stage" viewBox="0 0 260 190" width="260" height="190" role="img" aria-labelledby="sf-pt-svg-t">
              <title id="sf-pt-svg-t">Joint compressive stress profile across thickness t under wind overturning moment</title>
              <line class="sf-funicular-axis" x1="28" y1="112" x2="232" y2="112"/>
              <polygon class="sf-stress-trap sf-stress-comp" points="40,112 40,89.4 220,39.0 220,112"/>
              <text class="sf-svg-caption-text" x="34" y="130">0.0 MPa (joint contact datum)</text>
              <text class="sf-svg-sub-text" x="34" y="24" data-en="Compression ↑ / Tension ↓" data-es="Compresión ↑ / Tracción ↓">Compression ↑ / Tension ↓</text>
            </svg>"""
    return f"""      <section id="benches" class="sf-benches-wrap" aria-label="Interactive architectural benches">
        <div class="sf-part" aria-labelledby="sf-col-bench-h">
          <p class="tp-kicker">{bi("span", cb["kicker_en"], cb["kicker_es"])}</p>
          {bi("h2", cb["title_en"], cb["title_es"], "sf-h2", 'id="sf-col-bench-h"')}
          {bi("p", cb["intro_en"], cb["intro_es"], "sf-lede")}
          <div class="sf-bench" data-sf-columns>
            <svg class="sf-star-svg sf-svg-stage" viewBox="0 0 300 280" width="300" height="280" role="img" aria-labelledby="sf-star-t">
              <title id="sf-star-t">Cross-section of two counter-rotating n-point star prisms forming the stone column</title>
              <polygon class="sf-star-ghost-a" points="150,70 220,140 150,210 80,140"/>
              <polygon class="sf-star-ghost-b" points="150,70 220,140 150,210 80,140"/>
              <polygon class="sf-star-core" points="150,75 215,140 150,205 85,140"/>
              <circle class="sf-star-void" cx="150" cy="140" r="9"/>
            </svg>
            <div class="sf-controls">
              <div class="sf-check-row">{tier_radios}</div>
              <div class="sf-control-group">
                <label class="sf-range-label" for="sf-col-z-range"><span>{bi("span", "Shaft fraction z / H_shaft", "Fracción de altura z / H_fuste")}</span><span class="sf-range-val" id="sf-col-z-val">0.50</span></label>
                <input id="sf-col-z-range" class="sf-range" type="range" min="0" max="100" step="1" value="50" aria-valuetext="0.50">
              </div>
              <p class="sf-readout" data-sf-col-readout aria-live="polite">{t(f"Pórfido rojo 12 puntas · H_total = 24 m · D_int = 2.10 m · A_neta = {s12['area_net_m2']:.2f} m² · MODELO σ = {s12['stress_mpa']:.2f} MPa" if is_es else f"12-pt Red porphyry · H_total = 24 m · D_in = 2.10 m · A_net = {s12['area_net_m2']:.2f} m² · MODEL σ = {s12['stress_mpa']:.2f} MPa")}</p>
              {cite(["sf-booklets", "barrios2006"])}
            </div>
          </div>
        </div>

        <div class="sf-part" aria-labelledby="sf-shard-bench-h">
          <p class="tp-kicker">{bi("span", C.SHARD_BENCH_TEXT["kicker_en"], C.SHARD_BENCH_TEXT["kicker_es"])}</p>
          {bi("h2", C.SHARD_BENCH_TEXT["title_en"], C.SHARD_BENCH_TEXT["title_es"], "sf-h2", 'id="sf-shard-bench-h"')}
          {bi("p", C.SHARD_BENCH_TEXT["intro_en"], C.SHARD_BENCH_TEXT["intro_es"], "sf-lede")}
          <div class="sf-bench" data-sf-shard>
            {render_shard_svg()}
            <div class="sf-controls">
              <div class="sf-control-group">
                <label class="sf-range-label" for="sf-caliper-range"><span>{bi("span", "Shard caliper perturbation ±δr", "Error de calibrador ±δr")}</span><span class="sf-range-val" id="sf-caliper-val">0.0 mm</span></label>
                <input id="sf-caliper-range" class="sf-range" type="range" min="0.0" max="{M.SHARD_RECOVERY_MODEL['caliper_max_mm']:.1f}" step="0.1" value="0.0" aria-valuetext="0.0 mm">
              </div>
              <p class="sf-readout" data-sf-shard-readout aria-live="polite">{t(f"MODELO recuperado a = 1.800 m · c = 2.400 m · Error reglado = 0.0 mm vs Deriva libre = {M.shard_vault_recovery(0.0)['freeform_err_mm']:.1f} mm" if is_es else f"MODEL recovered a = 1.800 m · c = 2.400 m · Ruled rim err = 0.0 mm vs Freeform drift = {M.shard_vault_recovery(0.0)['freeform_err_mm']:.1f} mm")}</p>
              {cite(["burry1996", "sf-history"])}
            </div>
          </div>
        </div>

        <div class="sf-part" aria-labelledby="sf-tower-bench-h">
          <p class="tp-kicker">{bi("span", tb["kicker_en"], tb["kicker_es"])}</p>
          {bi("h2", tb["title_en"], tb["title_es"], "sf-h2", 'id="sf-tower-bench-h"')}
          {bi("p", tb["intro_en"], tb["intro_es"], "sf-lede")}
          <div class="sf-bench" data-sf-towers>
            {skyline_svg}
            <div class="sf-controls">
              {stress_svg}
              <div class="sf-control-group">
                <label class="sf-range-label" for="sf-fpt-range"><span>{bi("span", "Post-tensioning force F_pt", "Fuerza de pretensado F_pt")}</span><span class="sf-range-val" id="sf-fpt-val">{p_tp['prestress_kn']:.0f} kN</span></label>
                <input id="sf-fpt-range" class="sf-range" type="range" min="{p_tp['prestress_min_kn']:.0f}" max="{p_tp['prestress_max_kn']:.0f}" step="50" value="{p_tp['prestress_kn']:.0f}" aria-valuetext="{p_tp['prestress_kn']:.0f} kN">
              </div>
              <div class="sf-control-group">
                <label class="sf-range-label" for="sf-wind-range"><span>{bi("span", "Characteristic wind gust q_wind", "Ráfaga de viento q_viento")}</span><span class="sf-range-val" id="sf-wind-val">{p_tp['wind_kpa']:.2f} kPa</span></label>
                <input id="sf-wind-range" class="sf-range" type="range" min="{p_tp['wind_min_kpa']:.2f}" max="{p_tp['wind_max_kpa']:.2f}" step="0.05" value="{p_tp['wind_kpa']:.2f}" aria-valuetext="{p_tp['wind_kpa']:.2f} kPa">
              </div>
              <p class="sf-readout" data-sf-pt-readout aria-live="polite">MODEL M_wind = {pt0['m_wind_knm']:.2f} kN·m · σ_min = {pt0['sigma_min_mpa']:.2f} MPa · σ_max = {pt0['sigma_max_mpa']:.2f} MPa</p>
              {cite(["ingenia-arup", "sf-cross-2026", "sf-evangelists", "sf-inauguration-2026"])}
            </div>
          </div>
        </div>

        <div class="sf-part" aria-labelledby="sf-light-bench-h">
          <p class="tp-kicker">{bi("span", lb["kicker_en"], lb["kicker_es"])}</p>
          {bi("h2", lb["title_en"], lb["title_es"], "sf-h2", 'id="sf-light-bench-h"')}
          {bi("p", lb["intro_en"], lb["intro_es"], "sf-lede")}
          <div class="sf-bench" data-sf-light>
            <svg class="sf-svg-stage" viewBox="0 0 360 220" width="360" height="220" role="img" aria-labelledby="sf-light-t">
              <title id="sf-light-t">Nave cross-section showing east Nativity blue-green rays shifting through zenith oculi to west Passion amber light</title>
              <path class="sf-nave-outline" d="M 38 190 L 38 66 Q 110 28 180 24 Q 250 28 322 66 L 322 190 Z"/>
              <line class="sf-funicular-axis" x1="128" y1="54" x2="128" y2="190"/>
              <line class="sf-funicular-axis" x1="232" y1="54" x2="232" y2="190"/>
              <polygon class="sf-light-ray sf-ray-dawn" points="40,70 40,115 245,190 190,190"/>
              <text class="sf-svg-caption-text" x="44" y="208" data-en="East · Nativity" data-es="Oriente · Nacimiento">East · Nativity</text>
              <text class="sf-svg-caption-text" x="316" y="208" text-anchor="end" data-en="West · Passion" data-es="Poniente · Pasión">West · Passion</text>
            </svg>
            <div class="sf-controls">
              <div class="sf-control-group">
                <label class="sf-range-label" for="sf-solar-range"><span>{bi("span", "Solar azimuth hour", "Hora solar")}</span><span class="sf-range-val" id="sf-solar-val">09:30</span></label>
                <input id="sf-solar-range" class="sf-range" type="range" min="7.0" max="19.0" step="0.25" value="9.5" aria-valuetext="09:30">
              </div>
              <p class="sf-readout" data-sf-light-readout aria-live="polite">09:30 · East Nativity glass · MODEL Eyring stone RT60 ≈ 4.6 s</p>
              {cite(["eyring1930", "zhaoburry2024", "yoshikawa2004"])}
            </div>
          </div>
        </div>
{render_polar_radar(is_es)}
      </section>"""


# --------------------------------------------------------------------------------------------- Part VI Mechanics Lab

def render_lab_section(is_es: bool) -> str:
    L = C.LAB
    hyp = M.hyperboloid_saddle_metrics()
    fmod = M.FUNICULAR_MODEL
    eq0 = M.funicular_equilibrium(0.0)
    fun_rows = []
    for w_top in (0.0, fmod["lantern_load_kn"], fmod["lantern_max_kn"]):
        feq = M.funicular_equilibrium(w_top)
        fun_rows.append(
            f'<tr data-lantern-kn="{int(w_top)}">'
            f'<th scope="row" class="sf-num">{w_top:.0f} kN</th>'
            f'<td class="sf-num">{feq["H_kn"]:.1f} kN</td>'
            f'<td class="sf-num">{feq["V_kn"]:.2f} kN</td>'
            f'<td class="sf-num">{feq["rise_loaded_m"]:.2f} m</td>'
            f'<td class="sf-num sf-strong">{feq["tilt_from_vertical_deg"]:.2f}°</td>'
            f'<td class="sf-num">{feq["crown_kink_deg"]:.2f}°</td></tr>'
        )
    fhead = "".join(
        bi("th", en, es, "", 'scope="col"') for en, es in (
            ("Lantern W_top (MODEL)", "Linterna W_top (MODELO)"),
            ("Thrust H", "Empuje H"),
            ("Vertical reaction V", "Reacción vertical V"),
            ("Vault rise", "Flecha de bóveda"),
            ("Column tilt θ", "Inclinación θ"),
            ("Crown kink", "Quiebre en clave"),
        )
    )

    col_rows = []
    for n, st_en, st_es, _p_en, _p_es, d_in, load_kn in M.COLUMN_TIERS:
        s0 = M.counter_twisted_section(n, d_in, load_kn, 0.0)
        s1 = M.counter_twisted_section(n, d_in, load_kn, 1.0)
        col_rows.append(
            f'<tr data-col-n="{n}">'
            f'{bi("th", f"{n}-pt ({st_en})", f"{n} pts ({st_es})", "", "scope=\"row\"")}'
            f'<td class="sf-num">{s0["total_height_m"]:.0f} m</td>'
            f'<td class="sf-num">{s0["shaft_height_m"]:.1f} m</td>'
            f'<td class="sf-num">{s0["area_net_m2"]:.4f} m²</td>'
            f'<td class="sf-num">{s1["area_net_m2"]:.4f} m²</td>'
            f'<td class="sf-num">{s0["stress_mpa"]:.2f} MPa</td>'
            f'<td class="sf-num sf-strong">{s1["stress_mpa"]:.2f} MPa</td></tr>'
        )
    chead = "".join(
        bi("th", en, es, "", 'scope="col"') for en, es in (
            ("Tier", "Rango"),
            ("H_total (2n)", "H_total (2n)"),
            ("H_shaft (10·D_in)", "H_fuste (10·D_int)"),
            ("A_net(0) base", "A_neta(0) base"),
            ("A_net(1) top", "A_neta(1) cima"),
            ("σ(0) MODEL", "σ(0) MODELO"),
            ("σ(1) MODEL", "σ(1) MODELO"),
        )
    )

    pt_rows = []
    q_wind = M.TOWER_PANEL_MODEL["wind_kpa"]
    for f_pt in (0.0, M.TOWER_PANEL_MODEL["prestress_kn"]):
        pd = M.panel_decompression(prestress_kn=f_pt, wind_kpa=q_wind)
        lbl_en = "Unprestressed (F_pt = 0)" if f_pt == 0.0 else f"Post-tensioned ({f_pt:.0f} kN MODEL)"
        lbl_es = "Sin pretensar (F_pt = 0)" if f_pt == 0.0 else f"Pretensado ({f_pt:.0f} kN MODELO)"
        state_en = "In compression" if pd["compressed_joint"] else "Tension decompression"
        state_es = "En compresión" if pd["compressed_joint"] else "Descompresión a tracción"
        pt_rows.append(
            f'<tr data-pt-kn="{int(f_pt)}">'
            f'{bi("th", lbl_en, lbl_es, "", "scope=\"row\"")}'
            f'<td class="sf-num">{pd["m_wind_knm"]:.2f} kN·m</td>'
            f'<td class="sf-num sf-strong">{pd["sigma_min_mpa"]:+.3f} MPa</td>'
            f'<td class="sf-num">{pd["sigma_max_mpa"]:+.3f} MPa</td>'
            f'<td>{bi("span", state_en, state_es)}</td></tr>'
        )
    pthead = "".join(
        bi("th", en, es, "", 'scope="col"') for en, es in (
            ("Joint state", "Estado de junta"),
            ("Wind moment M_w", "Momento M_viento"),
            ("Windward σ_min", "σ_min barlovento"),
            ("Leeward σ_max", "σ_max sotavento"),
            ("Joint response", "Respuesta"),
        )
    )

    hm = M.HYPERBOLOID_MODEL
    sr0 = M.shard_vault_recovery(0.0)
    shard_rows = []
    for err in (0.0, 0.5, 1.0):
        sr = M.shard_vault_recovery(err)
        shard_rows.append(
            f'<tr data-caliper-mm="{err:.1f}">'
            f'<th scope="row" class="sf-num">±{err:.1f} mm</th>'
            f'<td class="sf-num">{sr["a_rec_m"]:.4f} m</td>'
            f'<td class="sf-num">{sr["c_rec_m"]:.4f} m</td>'
            f'<td class="sf-num">{sr["r_ruled_top_m"]:.4f} m</td>'
            f'<td class="sf-num sf-strong">{sr["ruled_err_mm"]:.2f} mm</td></tr>'
        )
    shead = "".join(
        bi("th", en, es, "", 'scope="col"') for en, es in (
            ("Caliper δr (MODEL)", "Error calibrador δr (MODELO)"),
            ("Recovered a", "Radio a recuperado"),
            ("Recovered c", "Escala c recuperada"),
            ("Ruled r(3.0 m)", "Radio r(3.0 m) reglado"),
            ("Ruled rim err", "Desvío en corona"),
        )
    )
    return f"""      <section class="sf-part sf-lab" id="part-6" aria-labelledby="part-6-h">
        <header class="sf-part-head">
          <p class="sf-part-num" aria-hidden="true">VI</p>
          <h2 class="sf-h2 sf-part-title" id="part-6-h">{bi("span", "Part VI", "Parte VI")} · {bi("span", L["title_en"], L["title_es"])}</h2>
          <p class="sf-part-years" data-en="Model · Derived · Checked by script" data-es="Modelo · Derivado · Comprobado por script">Model · Derived · Checked by script</p>
        </header>
        {bi("p", L["intro_en"], L["intro_es"], "sf-lede sf-dropcap")}

        <article class="sf-lab-block" id="lab-hyperboloid">
          {bi("h3", L["hyp_h_en"], L["hyp_h_es"])}
          {bi("p", L["hyp_en"], L["hyp_es"])}
          <p class="sf-eq"><code>r(u, v) = (a(cos u − s·v·sin u), b(sin u + s·v·cos u), v·c)</code> · <code>(x/a)² + (y/b)² − (z/c)² = 1</code></p>
          <p class="sf-small">{bi("span", f"MODEL throat a = {hm['a_m']:.2f} m, b = {hm['b_m']:.2f} m, c = {hm['c_m']:.2f} m, |v| ≤ {hm['v_max']:.2f}:", f"Garganta MODELO a = {hm['a_m']:.2f} m, b = {hm['b_m']:.2f} m, c = {hm['c_m']:.2f} m, |v| ≤ {hm['v_max']:.2f}:")} <strong data-hyp-throat>{hyp['area_throat_m2']:.2f} m²</strong> → <strong data-hyp-top>{hyp['area_top_m2']:.2f} m²</strong> (<span data-hyp-ratio>{hyp['aperture_ratio']:.4f}×</span>, pitch <span data-hyp-pitch>{hyp['ruling_pitch_deg']:.2f}°</span>).</p>
          {cite(["sf-booklets", "cortes2019"])}
        </article>

        <article class="sf-lab-block" id="lab-funicular">
          {bi("h3", L["fun_h_en"], L["fun_h_es"])}
          {bi("p", L["fun_en"], L["fun_es"])}
          <p class="sf-eq"><code>y(x) = a·[cosh(L/(2a) + α₀) − cosh(|x|/a + α₀)], α₀ = arcsinh(W_top / 2H), θ = arctan(H / V)</code></p>
          <div class="sf-table-wrap"><table class="sf-table"><thead><tr>{fhead}</tr></thead><tbody>{''.join(fun_rows)}</tbody></table></div>
          <p class="sf-small">{bi("span", f"Unloaded equal-span, equal-rise catenary vs. parabola maximum vertical separation (MODEL span L = {fmod['span_m']:.1f} m, a = {fmod['catenary_a_m']:.1f} m):", f"Separación vertical máxima catenaria vs. parábola de igual claro y flecha (MODELO L = {fmod['span_m']:.1f} m, a = {fmod['catenary_a_m']:.1f} m):")} <strong class="sf-cat-gap-mm">{eq0['catenary_parabola_max_gap_mm']:.1f} mm</strong>.</p>
          {cite(["heyman1966", "huerta2006", "akbarzadeh2015"])}
        </article>

        <article class="sf-lab-block" id="lab-columns">
          {bi("h3", L["col_h_en"], L["col_h_es"])}
          {bi("p", L["col_en"], L["col_es"])}
          <p class="sf-eq"><code>H_total = 2n m · H_shaft = 10·D_in · θ(z) = ±(π / 2n)·(z / H_shaft)</code></p>
          <div class="sf-table-wrap"><table class="sf-table"><thead><tr>{chead}</tr></thead><tbody>{''.join(col_rows)}</tbody></table></div>
          {cite(["barrios2006", "grima2007"])}
        </article>

        <article class="sf-lab-block" id="lab-post-tension">
          {bi("h3", L["pt_h_en"], L["pt_h_es"])}
          {bi("p", L["pt_en"], L["pt_es"])}
          <p class="sf-eq"><code>σ_min = (F_pt + N_dead) / A_net − M_wind / Z_net ≥ 0</code></p>
          <div class="sf-table-wrap"><table class="sf-table"><thead><tr>{pthead}</tr></thead><tbody>{''.join(pt_rows)}</tbody></table></div>
          {cite(["ingenia-arup", "rodriguez2017"])}
        </article>

        <article class="sf-lab-block" id="lab-shard">
          {bi("h3", L["shard_h_en"], L["shard_h_es"])}
          {bi("p", L["shard_en"], L["shard_es"])}
          <p class="sf-eq"><code>r²(z) = a² + (a²/c²)·z² · z₁ = 0.20 m, z₂ = 0.55 m → r(3.00 m)</code></p>
          <div class="sf-table-wrap"><table class="sf-table"><thead><tr>{shead}</tr></thead><tbody>{''.join(shard_rows)}</tbody></table></div>
          <p class="sf-small">{bi("span", "Unruled quadratic Taylor extrapolation from the same z₁ = 0.20 m fragment diverges at z = 3.00 m by:", "La extrapolación libre cuadrática de Taylor desde el mismo fragmento z₁ = 0.20 m se desvía en z = 3.00 m por:")} <strong class="sf-freeform-err-mm">{sr0['freeform_err_mm']:.1f} mm</strong>.</p>
          {cite(["burry1996", "gomez2009"])}
        </article>

        <aside class="sf-interlude sf-verify-box" aria-labelledby="sf-verify-h">
          {bi("h3", L["verify_h_en"], L["verify_h_es"], "sf-int-h", 'id="sf-verify-h"')}
          {bi("p", L["verify_en"], L["verify_es"])}
          <p class="sf-eq"><code>python skills/classics/cc02/verify_cc02_sagrada.py</code><br><code>python skills/classics/cc02/verify_cc02_sagrada.py --planted-defect</code></p>
        </aside>
      </section>"""


# --------------------------------------------------------------------------------------------- silent & sources

def render_silent(is_es: bool) -> str:
    rows = "".join(
        f'<div class="sf-silent-row">{bi("dt", q["q_en"], q["q_es"])}{bi("dd", q["a_en"], q["a_es"])}</div>' for q in C.SILENT
    )
    aria = "Lo que las fuentes no dicen" if is_es else "What the sources do not say"
    return f"""        <aside class="sf-silent" aria-label="{a(aria)}">
          {bi("h2", "What the sources do not state", "Lo que las fuentes no afirman", "sf-h2")}
          <dl>{rows}</dl>
        </aside>"""


def render_sources(is_es: bool) -> str:
    items = []
    for key, s in C.SOURCES.items():
        en, es = C.KIND_LABEL[s["kind"]]
        items.append(
            f'<li id="src-{a(key)}"><span class="sf-stamp sf-stamp-{s["kind"]}" data-en="{a(en)}" data-es="{a(es)}">{t(es if is_es else en)}</span> '
            f'<a href="{a(s["url"])}" rel="noopener noreferrer">{t(s["label"])}</a></li>'
        )
    note_en = (
        f"All read on {C.ACCESSED}. Basílica marks official Basílica de la Sagrada Família publications; Engineering marks "
        "Ingenia / Royal Academy of Engineering coverage; Paper marks peer-reviewed journal articles checked in Crossref "
        "and Scite on the same day with zero retractions; Photo Archive marks Wikimedia Commons documentary photographs under "
        "Public Domain, CC0, or CC BY attribution."
    )
    note_es = (
        f"Todas consultadas el {C.ACCESSED}. Basílica marca publicaciones oficiales del templo; Ingeniería marca cobertura técnica "
        "de Ingenia / Royal Academy of Engineering; Artículo marca artículos arbitrados revisados en Crossref y Scite el mismo día "
        "sin retractaciones; Archivo Fotográfico marca fotografías documentales de Wikimedia Commons en Dominio Público, CC0 o CC BY."
    )
    return f"""      <section class="sf-sources" id="sources" aria-labelledby="sf-src-h">
        {bi("h2", "Sources", "Fuentes", "sf-h2", 'id="sf-src-h"')}
        {bi("p", note_en, note_es, "sf-small")}
        <ol class="sf-source-list">
{chr(10).join('          ' + i for i in items)}
        </ol>
      </section>"""


# --------------------------------------------------------------------------------------------- page assembly

def render_page(catalog: dict, lang: str = "en") -> str:
    is_es = lang == "es"
    rel = "../.."
    t_en, d_en, t_es, d_es = C.SEO
    title = t_es if is_es else t_en
    desc = d_es if is_es else d_en
    canon = B.page_url(PATH, lang)
    image = "https://informatico.ai/plates/cc02.png"
    crumbs = [
        (BRAND, B.page_url("", lang)),
        ("Arquitectura" if is_es else "Architecture", B.page_url("architecture/", lang)),
        (C.CODE, canon),
    ]
    ld = B._ld("ScholarlyArticle", title, desc, canon, lang, image=image, date_published=C.DATE,
               date_modified=C.DATE, crumbs=crumbs)
    head = B.render_head(f"{title} | {BRAND}", desc, PATH, "article", image, rel, rel, ld, lang)
    head = head.replace("</head>", f'  <link rel="stylesheet" href="{rel}/sagrada-familia.css">\n</head>')

    h = C.HERO
    pause_label = ("Pausar movimiento", "Reanudar movimiento") if is_es else ("Pause motion", "Resume motion")
    opening = "\n".join(f'        {bi("p", p["en"], p["es"])}\n        {cite(p["src"])}' for p in C.OPENING)
    parts = "\n".join(render_part(p, is_es) for p in C.PARTS)
    closing = "\n".join(f'        {bi("p", p["en"], p["es"])}' for p in C.CLOSING)

    jumps = [("#relay", "5 Generations", "5 Generaciones")]
    jumps += [(f"#{p['id']}", f"{p['numeral']} · {p['title_en']}", f"{p['numeral']} · {p['title_es']}") for p in C.PARTS]
    jumps += [
        ("#tectonic-section", "1:500 ↔ 1:10 Section", "Sección 1:500 ↔ 1:10"),
        ("#atelier", "2D ↔ 3D Atelier", "Atelier 2D ↔ 3D"),
        ("#benches", "Benches", "Bancos"),
        ("#visuals", "Visual Archive", "Archivo Visual"),
        ("#part-6", "VI · Lab", "VI · Laboratorio"),
        ("#act-puzzle-cc02", "Crossword", "Crucigrama"),
        ("#sources", "Sources", "Fuentes"),
    ]
    hero_diptych = render_media_diptych(
        ("photo-1909-escoles", "photo-2026-cross"),
        is_es,
        "1909 → 2026 Documentary Diptych · From Workers’ Brick Schools to the 172.5 m Cross",
        "Díptico documental 1909 → 2026 · De las Escuelas obreras a la Cruz de 172.5 m",
    )
    jump_html = " ".join(f'<a class="tp-essay-jump-pill" href="{jh}" data-en="{a(je)}" data-es="{a(js)}">{t(es_or_en(je, js, is_es))}</a>' for jh, je, js in jumps)
    aria_crumb = "Ruta de navegación" if is_es else "Breadcrumb"
    aria_jump = "Secciones" if is_es else "Sections"
    crossword = B.render_folio_crossword_section("cc02", C.CODE)

    return f"""{head}
<body class="tp-body tp-page-folio sf-page">
{B.render_masthead(rel, "architecture", lang)}
{B.render_contents_dialog(rel, catalog, C.SLUG)}
{render_catenary_backdrop()}
  <main id="main" class="tp-shell sf-shell" tabindex="-1">
    <nav class="tp-breadcrumb-bar" aria-label="{aria_crumb}">
      <ol class="tp-breadcrumb-list">
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="../../">Informatico.ai</a></li>
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="../../architecture/#cult-classics-arch" data-en="Architecture" data-es="Arquitectura">Architecture</a></li>
        <li class="tp-crumb-item" aria-current="page"><span>{t(C.CODE)}</span></li>
      </ol>
    </nav>
    <article class="sf-feature tp-prose" data-folio-id="{a(C.CODE)}">
      <header class="sf-hero tp-hero">
        <p class="tp-kicker">{bi("span", h["kicker_en"], h["kicker_es"])} · {bi("span", h["reading_en"], h["reading_es"])}</p>
        <h1 class="tp-h1 sf-h1" data-en="{a(h['title_en'])}" data-es="{a(h['title_es'])}">{t(h['title_en'])}</h1>
        {bi("p", h["dek_en"], h["dek_es"], "tp-standfirst")}
        <div class="sf-hero-tools">
          <button type="button" class="sf-btn sf-btn-quiet" data-sf-pause aria-pressed="false" data-label-pause="{a(pause_label[0])}" data-label-resume="{a(pause_label[1])}">{t(pause_label[0])}</button>
          <tp-article-audio data-folio="{a(C.CODE)}" data-reading-time="{a(h['reading_es'] if is_es else h['reading_en'])}"></tp-article-audio>
        </div>
        {bi("p", C.BRIEF_NOTE["en"], C.BRIEF_NOTE["es"], "sf-brief")}
      </header>
      <nav class="tp-essay-jump-bar" aria-label="{aria_jump}">{jump_html}</nav>
{render_era_rail()}
      <section class="sf-opening" aria-label="{a('Inicio' if is_es else 'Opening')}">
{opening}
      </section>
{hero_diptych}
{render_relay_section(is_es)}
{parts}
{render_atelier_section(is_es)}
{render_benches_section(is_es)}
{render_visual_gallery_section(is_es)}
{render_lab_section(is_es)}
{crossword}
{render_silent(is_es)}
      <section class="sf-closing" aria-label="{a('Cierre' if is_es else 'Closing')}">
{closing}
      </section>
{render_sources(is_es)}
      {bi("p", C.FOOTER_NOTE["en"], C.FOOTER_NOTE["es"], "sf-footnote")}
    </article>
{B.render_site_footer(rel)}
  </main>
  <script type="module" src="{rel}/modules/main.mjs"></script>
  <script type="module" src="{rel}/modules/sagrada-familia.mjs"></script>
</body>
</html>
"""


def es_or_en(en: str, es: str, is_es: bool) -> str:
    return es if is_es else en


# --------------------------------------------------------------------------------------------- share plate & output

def write_plate() -> None:
    """1200×630 zero-text schematic plate: Montjuïc datum, 18-spire parabolic profile, and hyperboloid straight rulings."""
    import build_cross_scale_essays as E  # noqa: E402

    w, h = 1200, 630
    buf = E._make_canvas(w, h, (242, 237, 228))
    # Blueprint / drafting border grid
    for gx in range(80, w, 120):
        E._draw_line(buf, w, h, gx, 40, gx, h - 40, 1, (196, 189, 174), 0.35)
    for gy in range(70, h, 90):
        E._draw_line(buf, w, h, 60, gy, w - 60, gy, 1, (196, 189, 174), 0.35)

    # Montjuïc Hill datum hairline at y = 92 (above 172.5 m spire tip at y = 112)
    E._draw_line(buf, w, h, 80, 92, w - 80, 92, 2, (42, 125, 118), 0.85)
    E._fill_rect(buf, w, h, 80, 520, w - 80, 525, (28, 36, 48), 0.90)

    # 18-spire schematic parabolic skyline rising cleanly toward central lantern
    spire_specs = [
        (170, 290, 26), (220, 265, 24), (270, 265, 24), (320, 290, 26),
        (430, 210, 32), (510, 200, 36), (600, 112, 46), (690, 210, 32),
        (780, 260, 26), (840, 248, 24), (900, 248, 24), (960, 260, 26),
    ]
    for cx, top_y, half_b in spire_specs:
        color = (176, 48, 30) if cx == 600 else (28, 56, 92)
        alpha = 0.95 if cx == 600 else 0.65
        E._draw_line(buf, w, h, cx - half_b, 520, cx - half_b * 0.45, (520 + top_y) * 0.5, 2, color, alpha)
        E._draw_line(buf, w, h, cx - half_b * 0.45, (520 + top_y) * 0.5, cx, top_y, 2, color, alpha)
        E._draw_line(buf, w, h, cx + half_b, 520, cx + half_b * 0.45, (520 + top_y) * 0.5, 2, color, alpha)
        E._draw_line(buf, w, h, cx + half_b * 0.45, (520 + top_y) * 0.5, cx, top_y, 2, color, alpha)
        if cx == 600:
            E._draw_line(buf, w, h, cx, top_y - 2, cx, top_y + 24, 3, (176, 48, 30), 1.0)
            E._draw_line(buf, w, h, cx - 10, top_y + 9, cx + 10, top_y + 9, 3, (176, 48, 30), 1.0)

    # Inverted catenary arch ribbon & ruled hyperboloid rings at lower right
    for i in range(-10, 11):
        u = i * 0.15
        x0 = 1010 + 75 * math.cos(u)
        x1 = 1010 + 115 * math.cos(u + 0.95)
        E._draw_line(buf, w, h, x0, 220, x1, 470, 2, (28, 56, 92), 0.45)
        x2 = 1010 + 115 * math.cos(u - 0.95)
        E._draw_line(buf, w, h, x0, 220, x2, 470, 2, (176, 48, 30), 0.42)
    E._draw_ring(buf, w, h, 1010, 345, 58, 2, (28, 36, 48), 0.78)
    E._draw_ring(buf, w, h, 1010, 345, 28, 2, (176, 48, 30), 0.85)

    PLATE.parent.mkdir(parents=True, exist_ok=True)
    PLATE.write_bytes(E._encode_png(w, h, buf))


def write_pages(catalog: dict | None = None) -> list[Path]:
    catalog = catalog or B.update_catalogs()
    write_plate()
    en_dir = RESEARCH / "classics" / C.SLUG
    es_dir = RESEARCH / B.ES_PREFIX.strip("/") / "classics" / C.SLUG
    en_dir.mkdir(parents=True, exist_ok=True)
    es_dir.mkdir(parents=True, exist_ok=True)
    (en_dir / "index.html").write_text(render_page(catalog, "en"), encoding="utf-8")
    (es_dir / "index.html").write_text(B.to_spanish_static(render_page(catalog, "es")), encoding="utf-8")
    return [en_dir / "index.html", es_dir / "index.html"]


def main() -> int:
    catalog = B.update_catalogs()
    written = write_pages(catalog)
    (RESEARCH / "sitemap.xml").write_text(B.render_research_sitemap(catalog), encoding="utf-8")
    (RESEARCH / "llms.txt").write_text(B.render_llms_txt(catalog), encoding="utf-8")
    digest = hashlib.sha256(PLATE.read_bytes()).hexdigest()[:12]
    print(f"PASS: Built {C.CODE} ({len(written)} pages, EN + ES-MX), plate cc02.png ({digest}), sitemap.xml and llms.txt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
