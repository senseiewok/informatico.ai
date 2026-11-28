#!/usr/bin/env python3
"""Build CC.01 · One Brief, Eight Answers: the Golf GTI engineering & chassis feature (/classics/golf-gti/ and /es-mx/classics/golf-gti/).

Single source of truth for text and citations lives in tools/folios/classics/cc01.py; mathematical models live in
tools/folios/classics/cc01_mechanics.py; page shell comes from build_longform_folios (head, masthead, contents dialog,
crossword, footer); interactive WebGL2 + 2D SVG + CAD export + audio/lightbox lives in src/modules/cult-classics.mjs.
Strict CSP compliance: zero inline scripts, zero inline style= attributes.

Run on its own: python -X utf8 tools/build_cult_classics.py   (also called from build_longform_folios.main)
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
from folios.classics import cc01 as C  # noqa: E402
from folios.classics import cc01_mechanics as M  # noqa: E402
from folios.seo_copy import BRAND  # noqa: E402

RESEARCH = ROOT / "src"
PATH = f"classics/{C.SLUG}/"
PLATE = RESEARCH / "plates" / "cc01.png"


def a(s: str) -> str:
    return html.escape(str(s), quote=True)


def t(s: str) -> str:
    return html.escape(str(s), quote=False)


def bi(tag: str, en: str, es: str, cls: str = "", extra: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    x = f" {extra}" if extra else ""
    return f'<{tag}{c}{x} data-en="{a(en)}" data-es="{a(es)}">{t(en)}</{tag}>'


def es_or_en(en: str, es: str, is_es: bool) -> str:
    return es if is_es else en


def stamp(key: str) -> str:
    s = C.SOURCES[key]
    return bi("a", s["short"], s.get("short_es", s["short"]), f"cc-stamp cc-stamp-{s['kind']}", f'href="#src-{a(key)}"')


def cite(keys: list[str]) -> str:
    if not keys:
        return ""
    return f'<p class="cc-cite">{" ".join(stamp(k) for k in keys)}</p>'


def _media_map() -> dict[str, dict]:
    return {item["id"]: item for item in (*C.PHOTOS, *C.PLATES)}


# --------------------------------------------------------------------------------------------- schematic background & navigation

def hatch_path(k: float) -> str:
    """Schematic hatchback side profile in a 300×110 box; k=0 boxy (Mk1) … k=1 crisp (Mk8). Freehand proportions."""
    ground = 92
    roof_y = 24 + 5 * k
    nose_top = 62 - 2 * k
    ws_base_x = 104 - 10 * k
    roof_front_x = 132 - 6 * k + 10 * k * k
    roof_rear_x = 222 + 6 * k
    hatch_x = 280 - 2 * k
    hatch_y = 50 + 6 * k
    tail_x = 290
    p = [
        f"M 10 {ground - 10}",
        f"L 8 {nose_top + 6:.1f}",
        f"Q 9 {nose_top:.1f} {18 + 4 * k:.1f} {nose_top - 1:.1f}",
        f"L {ws_base_x:.1f} {52 - 4 * k:.1f}",
        f"L {roof_front_x:.1f} {roof_y:.1f}",
        f"L {roof_rear_x:.1f} {roof_y + 1 + 2 * k:.1f}",
        f"Q {roof_rear_x + 10:.1f} {roof_y + 2:.1f} {hatch_x:.1f} {hatch_y:.1f}",
        f"L {tail_x} {hatch_y + 8:.1f}",
        f"L {tail_x} {ground - 10}",
        f"L 252 {ground - 10}",
        f"A 20 20 0 0 0 212 {ground - 10}",
        f"L 82 {ground - 10}",
        f"A 20 20 0 0 0 42 {ground - 10}",
        "Z",
    ]
    return " ".join(p)


def wheel(cx: float, cy: float, r: float) -> str:
    spokes = "".join(
        f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx + r * 0.78 * math.cos(i * math.pi / 2.5):.1f}" '
        f'y2="{cy + r * 0.78 * math.sin(i * math.pi / 2.5):.1f}"/>'
        for i in range(5)
    )
    return (
        f'<g class="cc-wheel"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"/>'
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r * 0.55:.1f}"/>{spokes}</g>'
    )


def silhouette(k: float, gen: str, extra_cls: str = "") -> str:
    r = 15 + 3 * k
    return (
        f'<svg class="cc-car {extra_cls}" data-gen="{a(gen)}" viewBox="0 0 300 110" width="300" height="110" '
        f'focusable="false" aria-hidden="true"><path class="cc-car-body" d="{hatch_path(k)}"/>'
        f'<line class="cc-car-red" x1="12" y1="{70 - 2 * k:.1f}" x2="40" y2="{70 - 2 * k:.1f}"/>'
        f'{wheel(62, 92 - r + 6, r)}{wheel(232, 92 - r + 6, r)}</svg>'
    )


def render_track_layers() -> str:
    hills = "M0 260 C 200 200 360 240 520 210 S 860 170 1040 220 S 1380 190 1600 230"
    ribbon = "M -40 980 C 300 860 220 640 560 560 S 1160 520 1240 360 S 1500 120 1660 40"
    kerb = "M 1180 1000 C 1260 900 1380 860 1460 760 S 1560 600 1640 560"

    def twice(d: str) -> str:
        return f'<path d="{d}"/><path d="{d}" transform="translate(0 1000)"/>'

    return f"""  <svg class="cc-track" viewBox="0 0 1600 1000" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
    <g class="cc-layer cc-layer-far" data-depth="0.06">{twice(hills)}</g>
    <g class="cc-layer cc-layer-ribbon" data-depth="0.18">{twice(ribbon)}</g>
    <g class="cc-layer cc-layer-centre" data-depth="0.18">{twice(ribbon)}</g>
    <g class="cc-layer cc-layer-kerb" data-depth="0.4">{twice(kerb)}</g>
  </svg>"""


def render_parade() -> str:
    cars = []
    for i, card in enumerate(C.CARDS):
        k = i / (len(C.CARDS) - 1)
        extra = "cc-car-tint" if card.get("egg") else ""
        cars.append(f'    <div class="cc-lane cc-lane-{i + 1}">{silhouette(k, card["gen"], extra)}</div>')
    return render_track_layers() + '\n  <div class="cc-parade" aria-hidden="true">\n' + "\n".join(cars) + "\n  </div>"


def render_gen_rail(is_es: bool) -> str:
    chips = []
    for i, c in enumerate(C.CARDS):
        cls = "cc-gen-chip is-current" if i == 0 else "cc-gen-chip"
        aria = ' aria-current="step"' if i == 0 else ""
        chips.append(
            f'<a class="{cls}" href="#{a(c["id"])}" data-gen="{a(c["gen"])}"{aria}>'
            f'{t(c["gen"])} · {t(c["years"].split(" · ")[0])}</a>'
        )
    label = "Generaciones" if is_es else "Generations"
    return f'        <nav class="cc-gen-rail" aria-label="{label}">{"".join(chips)}</nav>'


# --------------------------------------------------------------------------------------------- figures, gallery & bonnet egg

def render_inline_figure(item: dict, is_es: bool, extra_cls: str = "", include_id: bool = True) -> str:
    vg = C.VISUAL_GALLERY_TEXT
    is_photo = item["kind"] == "photo"
    badge_en = f"{vg['badge_photo_en']} · {item['license']}" if is_photo else f"{vg['badge_render_en']} · {item['era']}"
    badge_es = f"{vg['badge_photo_es']} · {item['license']}" if is_photo else f"{vg['badge_render_es']} · {item.get('era_es', item['era'])}"
    badge_cls = "cc-media-badge cc-media-badge-photo" if is_photo else "cc-media-badge cc-media-badge-render"
    alt_txt = item["alt_es"] if is_es else item["alt_en"]
    fig_id = f' id="{a(item["id"])}"' if include_id else ""
    cls_str = f"cc-inline-figure {extra_cls}".strip()
    return f"""        <figure class="{a(cls_str)}" data-cc-media-kind="{a(item['kind'])}" data-cc-media-id="{a(item['id'])}"{fig_id}>
          <div class="cc-inline-head">
            {bi("span", item["era"], item.get("era_es", item["era"]), "cc-inline-era")}
            <span class="{badge_cls}" data-en="{a(badge_en)}" data-es="{a(badge_es)}">{t(badge_es if is_es else badge_en)}</span>
          </div>
          <div class="cc-inline-frame" data-cc-open-media-frame="{a(item['id'])}">
            <img src="../../{a(item['image'])}" width="{item['width']}" height="{item['height']}" loading="lazy" decoding="async" alt="{a(alt_txt)}" data-alt-en="{a(item['alt_en'])}" data-alt-es="{a(item['alt_es'])}">
          </div>
          {bi("figcaption", item["caption_en"], item["caption_es"])}
          <div class="cc-inline-foot">
            {cite(item["src"])}
            <button type="button" class="cc-btn cc-btn-quiet cc-zoom-btn" data-cc-open-media="{a(item['id'])}" data-en="Fullscreen plate" data-es="Ampliar lámina">{t("Ampliar lámina" if is_es else "Fullscreen plate")}</button>
          </div>
        </figure>"""


def render_media_figure(item: dict, is_es: bool, in_gallery: bool = False) -> str:
    vg = C.VISUAL_GALLERY_TEXT
    is_photo = item["kind"] == "photo"
    badge_en = f"{vg['badge_photo_en']} · {item['license']}" if is_photo else f"{vg['badge_render_en']} · {item['era']}"
    badge_es = f"{vg['badge_photo_es']} · {item['license']}" if is_photo else f"{vg['badge_render_es']} · {item.get('era_es', item['era'])}"
    badge_cls = "cc-media-badge cc-media-badge-photo" if is_photo else "cc-media-badge cc-media-badge-render"
    alt_txt = item["alt_es"] if is_es else item["alt_en"]
    fig_id = f' id="{a(item["id"])}"' if not in_gallery else ""
    extra_btn = (
        f' data-alt-en="{a(item["alt_en"])}" data-alt-es="{a(item["alt_es"])}"'
        f' data-cap-en="{a(item["caption_en"])}" data-cap-es="{a(item["caption_es"])}"'
        f' data-badge-en="{a(badge_en)}" data-badge-es="{a(badge_es)}" data-kind="{a(item["kind"])}"'
        if in_gallery else ""
    )
    return f"""        <figure class="cc-media-card" data-cc-media-kind="{a(item['kind'])}" data-cc-media-id="{a(item['id'])}"{fig_id}>
          <div class="cc-media-head">
            <span class="{badge_cls}" data-en="{a(badge_en)}" data-es="{a(badge_es)}">{t(badge_es if is_es else badge_en)}</span>
            <button type="button" class="cc-btn cc-btn-quiet cc-zoom-btn" data-cc-open-media="{a(item['id'])}"{extra_btn} data-en="Inspect plate" data-es="Ampliar lámina">{t("Ampliar lámina" if is_es else "Inspect plate")}</button>
          </div>
          <div class="cc-media-frame" data-cc-open-media-frame="{a(item['id'])}">
            <img src="../../{a(item['image'])}" width="{item['width']}" height="{item['height']}" loading="lazy" decoding="async" alt="{a(alt_txt)}" data-alt-en="{a(item['alt_en'])}" data-alt-es="{a(item['alt_es'])}">
          </div>
          {bi("figcaption", item["caption_en"], item["caption_es"])}
          {cite(item["src"])}
        </figure>"""


def linked_caption(item: dict, is_es: bool) -> str:
    """Caption with maker links preserved intact under the 2026-11-15 decision."""
    out = t(item["caption_es"] if is_es else item["caption_en"])
    for label, url in item["links"]:
        out = out.replace(t(label), f'<a href="{a(url)}" rel="noopener noreferrer">{t(label)}</a>', 1)
    return out


def gti_rim(cx: float, cy: float) -> str:
    spokes = "".join(
        f'<line x1="{cx + 4.5 * math.cos(ang + d):.1f}" y1="{cy + 4.5 * math.sin(ang + d):.1f}" '
        f'x2="{cx + 14 * math.cos(ang + d):.1f}" y2="{cy + 14 * math.sin(ang + d):.1f}"/>'
        for ang in (i * 2 * math.pi / 5 for i in range(5)) for d in (-0.13, 0.13)
    )
    return (
        f'<g class="cc-egg-wheel"><circle class="cc-egg-tyre" cx="{cx}" cy="{cy}" r="19.4"/>'
        f'<circle class="cc-egg-rim" cx="{cx}" cy="{cy}" r="15"/>'
        f'<path class="cc-egg-caliper" d="M {cx - 10} {cy - 7} A 12 12 0 0 1 {cx + 2} {cy - 12}"/>'
        f'<g class="cc-wheel">{spokes}<circle cx="{cx}" cy="{cy}" r="3.6"/></g></g>'
    )


def gti_profile() -> str:
    body = (
        "M 24 96 L 20 90 Q 18 78 20 68 L 24 62 Q 60 50 100 44 L 140 20 Q 190 15 236 18 L 252 21 L 254 26 "
        "L 249 27 Q 262 38 268 50 L 279 56 Q 283 72 281 90 L 274 96 L 257 96 A 23.5 23.5 0 0 0 210 96 "
        "L 97 96 A 23.5 23.5 0 0 0 50 96 Z"
    )
    glass = "M 110 45 L 143 23 Q 190 20 226 22 L 246 42 Q 180 44 110 45 Z"
    return f"""<rect class="cc-egg-glow" x="28" y="46" width="70" height="14" rx="5"/>
                <path class="cc-egg-body" d="{body}"/>
                <path class="cc-egg-glass" d="{glass}"/>
                <line class="cc-egg-pillar" x1="176" y1="21" x2="172" y2="44"/>
                <path class="cc-egg-cpillar" d="M 214 22 L 228 22 L 248 42 L 222 43 Z"/>
                <path class="cc-egg-shoulder" d="M 28 60 Q 150 52 278 54"/>
                <path class="cc-egg-skirt" d="M 98 92 L 209 92"/>
                <path class="cc-egg-handle" d="M 148 52 L 158 52 M 196 51 L 205 51"/>
                <path class="cc-egg-light" d="M 21 62 L 46 56 L 48 63 L 23 67 Z"/>
                <line class="cc-egg-red" x1="20" y1="65" x2="47" y2="60"/>
                <path class="cc-egg-grille" d="M 20 73 L 40 71 M 20 78 L 40 76 M 21 83 L 40 81"/>
                <path class="cc-egg-taillight" d="M 268 50 L 280 56 L 280 63 L 268 59 Z"/>
                <path class="cc-egg-exhaust" d="M 262 95 L 270 95"/>
                <g class="cc-egg-hood"><path d="M 24 62 Q 60 50 100 44 L 101 48 Q 61 54 25 66 Z"/></g>
                {gti_rim(73.6, 84.6)}{gti_rim(233.6, 84.6)}"""


def render_egg(is_es: bool) -> str:
    e = C.EGG
    hint_en, hint_es = "There is one more car on this page.", "En esta página hay un auto más."
    car = f"""<svg class="cc-egg-car" viewBox="0 0 300 110" width="200" height="73" aria-hidden="true" focusable="false">
                {gti_profile()}
              </svg>"""
    return f"""          <div class="cc-egg">
            <button type="button" class="cc-egg-btn" aria-expanded="false" aria-controls="cc-egg-panel" data-label-open="{a(e['button_es'] if is_es else e['button_en'])}" data-label-close="{a(e['close_es'] if is_es else e['close_en'])}">
              {car}
              <span class="cc-egg-copy">{bi("span", hint_en, hint_es, "cc-egg-hint")}{bi("span", e["button_en"], e["button_es"], "cc-egg-label")}</span>
            </button>
            <div class="cc-egg-panel" id="cc-egg-panel" hidden>
              <figure class="cc-egg-photo">
                <img src="../../{e['image']}" width="{e['width']}" height="{e['height']}" loading="lazy" decoding="async" alt="{a(e['alt_es'] if is_es else e['alt_en'])}">
                <figcaption>{linked_caption(e, is_es)}</figcaption>
              </figure>
              <figure class="cc-egg-photo">
                <img src="../../{C.EGG_SIDE['image']}" width="{C.EGG_SIDE['width']}" height="{C.EGG_SIDE['height']}" loading="lazy" decoding="async" alt="{a(C.EGG_SIDE['alt_es'] if is_es else C.EGG_SIDE['alt_en'])}">
                <figcaption>{linked_caption(C.EGG_SIDE, is_es)}</figcaption>
              </figure>
            </div>
          </div>"""


# --------------------------------------------------------------------------------------------- editorial cards & legacy SVG benches

def render_diff_svg() -> str:
    plates = "".join(
        f'<rect class="cc-plate-disc {"cc-plate-a" if i % 2 == 0 else "cc-plate-b"}" data-i="{i}" x="{170 + i * 6}" '
        f'y="44" width="3" height="32" rx="1"/>' for i in range(5)
    )
    return f"""<svg class="cc-diff-svg" viewBox="0 0 360 230" width="360" height="230" role="img" aria-labelledby="cc-diff-title">
          <title id="cc-diff-title">Top view of a front axle in a left-hand corner</title>
          <defs>
            <marker id="cc-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" class="cc-arrow-head"/></marker>
          </defs>
          <path class="cc-diff-body" d="M 70 30 Q 180 10 290 30 L 300 215 L 60 215 Z"/>
          <line class="cc-axle" x1="60" y1="60" x2="300" y2="60"/>
          <rect class="cc-tyre cc-tyre-in" x="30" y="30" width="26" height="60" rx="6"/>
          <rect class="cc-tyre cc-tyre-out" x="304" y="30" width="26" height="60" rx="6"/>
          <g class="cc-slip" aria-hidden="true"><path d="M 20 40 q -8 20 0 40"/><path d="M 12 36 q -10 24 0 48"/></g>
          <rect class="cc-caliper" x="56" y="44" width="8" height="32" rx="2"/>
          <rect class="cc-diff-case" x="150" y="40" width="60" height="40" rx="6"/>
          <g class="cc-plates">{plates}</g>
          <line class="cc-torque cc-torque-in" x1="150" y1="60" x2="110" y2="60" marker-end="url(#cc-arrow)"/>
          <line class="cc-torque cc-torque-out" x1="210" y1="60" x2="250" y2="60" marker-end="url(#cc-arrow)"/>
          <text class="cc-svg-label" x="43" y="110" text-anchor="middle" data-en="inside" data-es="interior">inside</text>
          <text class="cc-svg-label" x="317" y="110" text-anchor="middle" data-en="outside" data-es="exterior">outside</text>
          <path class="cc-turn" d="M 180 200 Q 120 196 96 150" marker-end="url(#cc-arrow)"/>
        </svg>"""


def render_dct_svg() -> str:
    def gear(n: int, x: float, y: float) -> str:
        return (
            f'<g class="cc-gear" data-gear="{n}"><circle cx="{x}" cy="{y}" r="17"/>'
            f'<text x="{x}" y="{y + 5}" text-anchor="middle">{n}</text></g>'
        )
    odd = "".join(gear(n, 150 + i * 55, 60) for i, n in enumerate((1, 3, 5)))
    even = "".join(gear(n, 150 + i * 55, 150) for i, n in enumerate((2, 4, 6)))
    return f"""<svg class="cc-dct-svg" viewBox="0 0 360 210" width="360" height="210" role="img" aria-labelledby="cc-dct-title">
          <title id="cc-dct-title">Schematic of a six-speed dual-clutch gearbox: odd gears on one shaft, even gears on the other</title>
          <line class="cc-shaft cc-shaft-odd" x1="70" y1="60" x2="320" y2="60"/>
          <line class="cc-shaft cc-shaft-even" x1="70" y1="150" x2="320" y2="150"/>
          <g class="cc-clutch cc-clutch-odd"><rect x="74" y="40" width="5" height="40"/><rect class="cc-clutch-move" x="86" y="40" width="5" height="40"/></g>
          <g class="cc-clutch cc-clutch-even"><rect x="74" y="130" width="5" height="40"/><rect class="cc-clutch-move" x="86" y="130" width="5" height="40"/></g>
          <line class="cc-input" x1="20" y1="105" x2="74" y2="105"/>
          <line class="cc-input" x1="74" y1="60" x2="74" y2="150"/>
          <text class="cc-svg-label" x="22" y="96" data-en="engine" data-es="motor">engine</text>
          <text class="cc-svg-label" x="100" y="30" data-en="clutch 1 · odd" data-es="embrague 1 · nones">clutch 1 · odd</text>
          <text class="cc-svg-label" x="100" y="196" data-en="clutch 2 · even" data-es="embrague 2 · pares">clutch 2 · even</text>
          {odd}{even}
          <line class="cc-output" x1="330" y1="60" x2="330" y2="150"/>
          <text class="cc-svg-label" x="338" y="110" data-en="out" data-es="salida">out</text>
        </svg>"""


def render_weight_svg() -> str:
    blocks = []
    x = 20
    for i, (_en, _es, kg) in enumerate(C.WEIGHT_LEDGER):
        w = kg * 40
        blocks.append(
            f'<g class="cc-weight cc-weight-{i + 1}"><rect x="{x}" y="30" width="{w:.0f}" height="44" rx="4"/>'
            f'<text x="{x + w / 2:.0f}" y="58" text-anchor="middle">{kg:.1f} kg</text></g>'
        )
        x += w + 14
    total = sum(kg for *_r, kg in C.WEIGHT_LEDGER)
    return f"""<svg class="cc-weight-svg" viewBox="0 0 400 110" width="400" height="110" role="img" aria-labelledby="cc-weight-title">
          <title id="cc-weight-title">Volkswagen’s itemised Mk7 GTI suspension savings: 1.6, 2.8 and 4.0 kilograms, {total:.1f} kilograms in all</title>
          {''.join(blocks)}
          <line class="cc-scale" x1="10" y1="92" x2="390" y2="92"/>
        </svg>"""


def render_steer_svg() -> str:
    def sw(cx: int, cls: str) -> str:
        return (
            f'<g class="cc-steer {cls}" transform="rotate(0 {cx} 60)"><circle cx="{cx}" cy="60" r="40"/>'
            f'<circle cx="{cx}" cy="60" r="9"/><line x1="{cx - 38}" y1="60" x2="{cx - 9}" y2="60"/>'
            f'<line x1="{cx + 9}" y1="60" x2="{cx + 38}" y2="60"/><line x1="{cx}" y1="69" x2="{cx}" y2="98"/>'
            f'<line class="cc-steer-mark" x1="{cx}" y1="20" x2="{cx}" y2="30"/></g>'
        )
    return f"""<svg class="cc-steer-svg" viewBox="0 0 320 140" width="320" height="140" role="img" aria-labelledby="cc-steer-title">
          <title id="cc-steer-title">Two steering wheels turned to the same road-wheel angle: the progressive rack needs less rotation</title>
          {sw(80, "cc-steer-prog")}{sw(240, "cc-steer-std")}
          <text class="cc-svg-label" x="80" y="132" text-anchor="middle" data-en="GTI, progressive" data-es="GTI, progresiva">GTI, progressive</text>
          <text class="cc-svg-label" x="240" y="132" text-anchor="middle" data-en="lesser Golf" data-es="Golf menos potente">lesser Golf</text>
        </svg>"""


def render_mk7_extras(is_es: bool) -> str:
    total = sum(kg for *_r, kg in C.WEIGHT_LEDGER)
    rows = "".join(f'<li>{bi("span", en, es)} <strong>{kg:.1f} kg</strong></li>' for en, es, kg in C.WEIGHT_LEDGER)
    label_steer = "Ángulo de las ruedas delanteras" if is_es else "Front-wheel steering angle"
    return f"""          <figure class="cc-figure cc-weights" data-cc-reveal>
            {render_weight_svg()}
            <figcaption>
              <ul class="cc-weight-list">{rows}</ul>
              {bi("p", f"Volkswagen’s itemised savings against the previous GTI. Our sum: {total:.1f} kg.", f"Ahorros detallados por Volkswagen frente al GTI anterior. Nuestra suma: {total:.1f} kg.")}
            </figcaption>
          </figure>
          {cite(["vw-mk7-chassis"])}
          <div class="cc-science">
            {bi("p", C.UNSPRUNG_TEXT["en"], C.UNSPRUNG_TEXT["es"])}
            {cite(["woo2021"])}
          </div>
          <figure class="cc-figure cc-steering">
            {render_steer_svg()}
            <figcaption>
              <label class="cc-range-label" for="cc-steer-range">{t(label_steer)}</label>
              <input id="cc-steer-range" class="cc-range" type="range" min="0" max="100" value="0" step="1" aria-valuetext="{a('Centrado' if is_es else 'Centred')}">
              {bi("p", "VW gives about 2.1 turns lock to lock for the GTI’s progressive steering and prints 380° beside it, against 2.75 turns (500°) for the standard rack of lesser Golfs. The wheels here turn by those printed degree figures.", "VW da unas 2.1 vueltas de tope a tope para la dirección progresiva del GTI e imprime 380° junto a ese dato, frente a 2.75 vueltas (500°) para la cremallera estándar de los Golf menos potentes. Los volantes de aquí giran según esas cifras impresas en grados.", "cc-steer-readout", 'aria-live="polite"')}
            </figcaption>
          </figure>
          {cite(["vw-mk7-chassis"])}
          <aside class="cc-clubsport" aria-labelledby="cc-cs-title">
            {bi("h4", "Clubsport S · weight where it matters", "Clubsport S · el peso donde importa", "", 'id="cc-cs-title"')}
            {bi("p", C.CLUBSPORT_S["en"], C.CLUBSPORT_S["es"])}
            <figure class="cc-figure cc-lap">
              <svg class="cc-lap-svg" viewBox="0 0 360 80" width="360" height="80" role="img" aria-labelledby="cc-lap-title">
                <title id="cc-lap-title">Two lap times, 7:49.21 and 7:50.63: a gap of 1.42 seconds, about 0.3 percent of a lap</title>
                <rect class="cc-lap-a" x="10" y="14" width="338" height="18" rx="3"/>
                <rect class="cc-lap-b" x="10" y="44" width="339" height="18" rx="3"/>
                <rect class="cc-lap-gap" x="348" y="44" width="1.4" height="18"/>
                <text x="14" y="28">7:49.21</text><text x="14" y="58">7:50.63</text>
              </svg>
              {bi("figcaption", "Drawn to scale: the 1.42 s gap is the sliver at the end, about 0.3% of a lap (our arithmetic).", "A escala: la diferencia de 1.42 s es la franja del final, alrededor de 0.3 % de una vuelta (nuestro cálculo).")}
            </figure>
            {cite(C.CLUBSPORT_S["src"])}
          </aside>
"""


def render_card(card: dict, is_es: bool) -> str:
    by_id = _media_map()
    rows = []
    for en, es, value, key in card["plate"]:
        rows.append(
            f'<div class="cc-plate-row">{bi("dt", en, es)}<dd>{bi("span", value, C.VALUE_ES.get(value, value), "cc-plate-val")} '
            f'{stamp(key)}</dd></div>'
        )
    egg = render_egg(is_es) if card.get("egg") else ""
    extra = render_mk7_extras(is_es) if card["id"] == "mk7" else ""
    media_id = card.get("inline_media")
    inline_fig = render_inline_figure(by_id[media_id], is_es, "cc-gen-figure") if media_id and media_id in by_id else ""
    aria_plate = f"Placa de especificaciones {card['gen']}" if is_es else f"Spec plate {card['gen']}"
    return f"""        <article class="cc-card" id="{a(card['id'])}" data-gen="{a(card['gen'])}">
          <header class="cc-card-head">
            <p class="cc-card-gen"><span>{t(card['gen'])}</span> <span class="cc-card-years">{t(card['years'])}</span></p>
            {bi("h3", card["move_en"], card["move_es"], "cc-card-move")}
          </header>
          <div class="cc-card-split">
            <div class="cc-card-main">
              {bi("p", card["body_en"], card["body_es"], "cc-card-body")}
              <div class="cc-plate" role="group" aria-label="{a(aria_plate)}">
                <dl>{''.join(rows)}</dl>
                <p class="cc-plate-foot" data-en="Read {a(C.ACCESSED)}" data-es="Consultado {a(C.ACCESSED)}">Read {t(C.ACCESSED)}</p>
              </div>
{extra}{egg}
            </div>
{inline_fig}
          </div>
        </article>"""


def render_interlude(kind: str, is_es: bool) -> str:
    if kind == "mk1-details":
        d = C.MK1_DETAILS
        items = "".join(f'<li>{bi("span", en, es)}</li>' for en, es in d["items"])
        return f"""          <aside class="cc-interlude" aria-labelledby="cc-int-mk1">
            {bi("h3", d["title_en"], d["title_es"], "cc-int-h", 'id="cc-int-mk1"')}
            <ul class="cc-ledger-list">{items}</ul>
            {cite(d["src"] + ["vw-history"])}
          </aside>"""
    if kind == "boost":
        b = C.BOOST
        col, row = 'scope="col"', 'scope="row"'
        head = "".join(bi("th", en, es, "", col) for en, es in zip(b["head_en"], b["head_es"]))
        rows = "".join(
            "<tr>" + bi("th", r[0], r[1], "", row) + bi("td", r[2], r[3]) + bi("td", r[4], r[5]) + "</tr>" for r in b["rows"]
        )
        return f"""          <aside class="cc-interlude" aria-labelledby="cc-int-boost">
            {bi("h3", b["title_en"], b["title_es"], "cc-int-h", 'id="cc-int-boost"')}
            <div class="cc-table-wrap"><table class="cc-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
            {bi("p", b["note_en"], b["note_es"], "cc-small")}
            {cite(b["src"])}
          </aside>"""
    if kind == "anatomy":
        d = C.ANATOMY
        rows = "".join(f'<div class="cc-anat-row">{bi("dt", r[0], r[1])}{bi("dd", r[2], r[3])}</div>' for r in d["items"])
        return f"""          <aside class="cc-interlude cc-anatomy" aria-labelledby="cc-int-anat">
            {bi("h3", d["title_en"], d["title_es"], "cc-int-h", 'id="cc-int-anat"')}
            <dl>{rows}</dl>
            {cite(d["src"])}
          </aside>"""
    if kind == "editions":
        e = C.EDITIONS_TEXT
        cols = (("Year", "Año"), ("Edition", "Edición"), ("Output (VW)", "Potencia (VW)"))
        head = "".join(bi("th", en, es, "", 'scope="col"') for en, es in cols)
        rows = "".join(f'<tr><td>{t(y)}</td><th scope="row">{t(n)}</th><td>{t(o)}</td></tr>' for y, n, o, _k in C.EDITIONS)
        return f"""          <aside class="cc-interlude" aria-labelledby="cc-int-ed">
            {bi("h3", e["title_en"], e["title_es"], "cc-int-h", 'id="cc-int-ed"')}
            <div class="cc-table-wrap"><table class="cc-table cc-editions"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
            {bi("p", e["note_en"], e["note_es"], "cc-small")}
            {cite(["vw-history"])}
          </aside>"""
    return ""


def render_diff_section(is_es: bool) -> str:
    modes = [
        ("open", "Open differential", "Diferencial abierto"),
        ("xds", "XDS+ · brake the inside wheel", "XDS+ · frenar la rueda interior"),
        ("lock", "Clutch-pack lock", "Bloqueo por embragues"),
    ]
    radios = "".join(
        f'<label class="cc-mode"><input type="radio" name="cc-diff-mode" value="{m}"{" checked" if m == "open" else ""}> {bi("span", en, es)}</label>'
        for m, en, es in modes
    )
    legend = "Estrategia" if is_es else "Strategy"
    thr = "Acelerador" if is_es else "Throttle"
    return f"""      <section class="cc-observatory" id="differential" aria-labelledby="cc-diff-h">
        {bi("h2", "The differential bench", "El banco de diferenciales", "cc-h2", 'id="cc-diff-h"')}
        {bi("p", C.DIFF_TEXT["intro_en"], C.DIFF_TEXT["intro_es"], "cc-lede")}
        <div class="cc-bench" data-cc-diff data-r="{M.DIFF_MODEL['radius_m']}" data-mu="{M.DIFF_MODEL['mu']}" data-nin="{M.DIFF_MODEL['load_in_n']}" data-nout="{M.DIFF_MODEL['load_out_n']}" data-brake="{M.DIFF_MODEL['brake_max_nm']}" data-lock="{M.DIFF_MODEL['lock_max_nm']}" data-demand="{M.DIFF_MODEL['demand_max_nm']}">
          {render_diff_svg()}
          <div class="cc-controls">
            <fieldset class="cc-modes"><legend>{t(legend)}</legend>{radios}</fieldset>
            <label class="cc-range-label" for="cc-throttle">{t(thr)}</label>
            <input id="cc-throttle" class="cc-range" type="range" min="0" max="100" value="0" step="1" aria-valuetext="0%">
            <p class="cc-readout" aria-live="polite" data-en="Throttle closed: both wheels grip." data-es="Acelerador cerrado: las dos ruedas agarran.">Throttle closed: both wheels grip.</p>
          </div>
        </div>
        {bi("p", C.DIFF_TEXT["caption_en"], C.DIFF_TEXT["caption_es"], "cc-small")}
        {cite(["vw-mk7-chassis", "vw-history"])}
        <div class="cc-science">
          {bi("p", C.DIFF_TEXT["science_en"], C.DIFF_TEXT["science_es"])}
          {cite(["kakalis2008"])}
        </div>
      </section>"""


def render_dct_section(is_es: bool) -> str:
    by_id = _media_map()
    return f"""      <section class="cc-observatory" id="two-clutches" aria-labelledby="cc-dct-h">
        {bi("h2", "Two clutches", "Dos embragues", "cc-h2", 'id="cc-dct-h"')}
        {bi("p", C.DCT_TEXT["intro_en"], C.DCT_TEXT["intro_es"], "cc-lede")}
        <div class="cc-bench" data-cc-dct>
          {render_dct_svg()}
          <div class="cc-controls">
            <button type="button" class="cc-btn" data-cc-shift data-en="Shift up" data-es="Subir velocidad">Shift up</button>
            <p class="cc-readout" aria-live="polite" data-en="First gear on clutch 1. Second is already selected on the even shaft." data-es="Primera en el embrague 1. La segunda ya está seleccionada en la flecha de pares.">First gear on clutch 1. Second is already selected on the even shaft.</p>
          </div>
        </div>
        <div class="cc-science">
          {bi("p", C.DCT_TEXT["science_en"], C.DCT_TEXT["science_es"])}
          {cite(["galvagno2011", "brancati2023"])}
        </div>
{render_inline_figure(by_id["plate-dsg-cutaway"], is_es, "cc-light-figure")}
      </section>"""


def render_part(part: dict, is_es: bool) -> str:
    cards = {c["id"]: c for c in C.CARDS}
    opener = []
    for i, p in enumerate(part["opener"]):
        cls = "cc-dropcap" if i == 0 else ""
        opener.append(f'          {bi("p", p["en"], p["es"], cls)}\n          {cite(p["src"])}')
    body = "\n".join(render_card(cards[cid], is_es) for cid in part["cards"])
    extra = ""
    if part["id"] == "part-3":
        extra = render_dct_section(is_es)
    elif part["id"] == "part-4":
        extra = render_diff_section(is_es)
    return f"""      <section class="cc-part" id="{a(part['id'])}" aria-labelledby="{a(part['id'])}-h">
        <header class="cc-part-head">
          <p class="cc-part-num" aria-hidden="true">{t(part['numeral'])}</p>
          <h2 class="cc-h2 cc-part-title" id="{a(part['id'])}-h"><span data-en="Part {a(part['numeral'])}" data-es="Parte {a(part['numeral'])}">Part {t(part['numeral'])}</span> · {bi("span", part["title_en"], part["title_es"])}</h2>
          <p class="cc-part-years">{t(part['years'])}</p>
        </header>
        <div class="cc-part-opener-grid">
          <div class="cc-part-opener">
{chr(10).join(opener)}
          </div>
          {bi("blockquote", part["pull_en"], part["pull_es"], "cc-pull")}
        </div>
{body}
{render_interlude(part["interlude"], is_es)}
{extra}
      </section>"""


# --------------------------------------------------------------------------------------------- interactive relay, loupe, atelier & study

def render_relay_section(is_es: bool) -> str:
    rx = C.RELAY_TEXT
    by_id = _media_map()
    btns = []
    segs = []
    cards = []
    seg_x = (16, 152, 288, 424, 560)
    seg_w = (120, 120, 120, 120, 108)
    for i, g in enumerate(C.GENERATIONS_RELAY):
        pressed = "true" if i == 0 else "false"
        active_cls = "cc-relay-seg is-active" if i == 0 else "cc-relay-seg"
        btns.append(
            f'<button type="button" class="cc-pill-btn" data-cc-gen-btn="{i}" aria-pressed="{pressed}" '
            f'data-en="{a(g["name_en"])}" data-es="{a(g["name_es"])}">{t(g["name_es"] if is_es else g["name_en"])}</button>'
        )
        segs.append(
            f'<g class="{active_cls}" data-cc-seg="{i}">'
            f'<rect class="cc-relay-bar" x="{seg_x[i]}" y="20" width="{seg_w[i]}" height="28" rx="4"/>'
            f'<text class="cc-svg-caption-text" x="{seg_x[i] + seg_w[i] / 2:.1f}" y="38" text-anchor="middle">{t(g["era"])}</text>'
            f'<text class="cc-svg-sub-text" x="{seg_x[i] + seg_w[i] / 2:.1f}" y="68" text-anchor="middle">Era {i + 1}</text>'
            f"</g>"
        )
        hid = "" if i == 0 else " hidden"
        mid = g.get("media_id")
        relay_fig = render_inline_figure(by_id[mid], is_es, "cc-relay-portrait") if mid and mid in by_id else ""
        card_body = f"""            <div class="cc-relay-main">
              <div class="cc-relay-head">
                {bi("h3", g["name_en"], g["name_es"], "cc-card-move")}
                <span class="cc-panel-tag">{t(g["lead_es"] if is_es else g["lead_en"])}</span>
              </div>
              <dl class="cc-relay-grid">
                <div class="cc-relay-row">{bi("dt", "Physical limit faced", "Límite físico enfrentado")}{bi("dd", g["challenge_en"], g["challenge_es"])}</div>
                <div class="cc-relay-row">{bi("dt", "Engineering move", "Solución de ingeniería")}{bi("dd", g["gift_en"], g["gift_es"])}</div>
              </dl>
              {cite(g["src"])}
            </div>"""
        cards.append(
            f"""          <article class="cc-relay-card{' cc-relay-card-media' if relay_fig else ''}" data-cc-relay-card="{i}"{hid}>
{card_body}
{relay_fig}
          </article>"""
        )

    timeline_svg = f"""<svg class="cc-svg-stage cc-relay-stage" viewBox="0 0 684 84" width="684" height="84" role="img" aria-labelledby="cc-relay-svg-t">
              <title id="cc-relay-svg-t">Five engineering eras across fifty years of the Golf GTI (1974 to 2026)</title>
              <line class="cc-stage-axis" x1="16" y1="34" x2="668" y2="34"/>
              {"".join(segs)}
            </svg>"""
    return f"""      <section class="cc-observatory cc-relay" id="relay" data-cc-relay aria-labelledby="cc-relay-h">
        <p class="tp-kicker">{bi("span", rx["kicker_en"], rx["kicker_es"])}</p>
        {bi("h2", rx["title_en"], rx["title_es"], "cc-h2", 'id="cc-relay-h"')}
        {bi("p", rx["intro_en"], rx["intro_es"], "cc-lede")}
        <div class="cc-pill-bar" role="group" aria-label="{a('Selector de etapa de ingeniería' if is_es else 'Generation engineering era selector')}">{"".join(btns)}</div>
        {timeline_svg}
{chr(10).join(cards)}
      </section>"""


def render_axle_loupe_section(is_es: bool) -> str:
    """Dual-scale 1:20 transverse front bay schematic paired with 1:5 mechanical cutaway nodes."""
    lx = C.AXLE_LOUPE_TEXT
    btns = "".join(
        f'<button type="button" class="cc-pill-btn" data-cc-node="{i}" aria-pressed="{"true" if i == 0 else "false"}" '
        f'data-en="{a(n["short_en"])}" data-es="{a(n["short_es"])}">{t(n["short_es"] if is_es else n["short_en"])}</button>'
        for i, n in enumerate(C.LOUPE_NODES)
    )
    info_cards = []
    for i, n in enumerate(C.LOUPE_NODES):
        hid = "" if i == 0 else " hidden"
        info_cards.append(
            f"""            <div class="cc-loupe-detail" data-cc-node-card="{i}"{hid}>
              <div class="cc-relay-head">{bi("h3", n["title_en"], n["title_es"], "cc-card-move")}<span class="cc-panel-tag">1:20 ↔ 1:5</span></div>
              {bi("p", n["summary_en"], n["summary_es"], "cc-small")}
              {cite(n["src"])}
            </div>"""
        )
    sec_svg = """<svg class="cc-svg-stage" viewBox="0 0 280 260" width="280" height="260" role="img" aria-labelledby="cc-bay-t">
              <title id="cc-bay-t">1:20 schematic front axle bay with MacPherson struts, dual-clutch transaxle, VAQ clutch pack, and ventilated rotors</title>
              <line class="cc-stage-axis" x1="20" y1="226" x2="260" y2="226"/>
              <rect class="cc-loupe-hull" x="34" y="136" width="26" height="80" rx="5"/>
              <rect class="cc-loupe-hull" x="220" y="136" width="26" height="80" rx="5"/>
              <line class="cc-axle-line" x1="60" y1="176" x2="220" y2="176"/>
              <rect class="cc-panel-outline" x="96" y="148" width="52" height="52" rx="4"/>
              <rect class="cc-star-accent" x="156" y="156" width="28" height="40" rx="3"/>
              <line class="cc-strut-line" x1="64" y1="168" x2="86" y2="62"/>
              <line class="cc-strut-line" x1="216" y1="168" x2="194" y2="62"/>
              <line class="cc-stage-axis" x1="64" y1="206" x2="122" y2="206"/>
              <line class="cc-stage-axis" x1="216" y1="206" x2="158" y2="206"/>
              <g class="cc-loupe-node is-active" data-cc-node-dot="0"><circle cx="80" cy="100" r="8"/><text class="cc-svg-sub-text" x="94" y="104">Strut</text></g>
              <g class="cc-loupe-node" data-cc-node-dot="1"><circle cx="170" cy="176" r="8"/><text class="cc-svg-sub-text" x="170" y="146" text-anchor="middle">VAQ</text></g>
              <g class="cc-loupe-node" data-cc-node-dot="2"><circle cx="122" cy="174" r="8"/><text class="cc-svg-sub-text" x="122" y="138" text-anchor="middle">DCT</text></g>
              <g class="cc-loupe-node" data-cc-node-dot="3"><circle cx="58" cy="198" r="8"/><text class="cc-svg-sub-text" x="48" y="128" text-anchor="middle">Hub</text></g>
            </svg>"""
    loupe_svg = """<svg class="cc-svg-stage" viewBox="0 0 320 250" width="320" height="250" role="img" aria-labelledby="cc-loupe-detail-t">
              <title id="cc-loupe-detail-t">1:5 enlarged mechanical node view for the selected front-axle zone</title>
              <g class="cc-loupe-view is-active" data-cc-loupe-view="0">
                <line class="cc-stage-axis" x1="160" y1="26" x2="160" y2="222"/>
                <line class="cc-strut-line" x1="186" y1="36" x2="146" y2="210"/>
                <path class="cc-torque-flow-b" d="M 128 60 L 178 72 L 132 88 L 180 100 L 134 116 L 182 128"/>
                <circle class="cc-loupe-hull" cx="146" cy="208" r="10"/>
                <text class="cc-svg-caption-text" x="160" y="24" text-anchor="middle">1:5 Kingpin &amp; Damper Axis</text>
              </g>
              <g class="cc-loupe-view" data-cc-loupe-view="1" hidden>
                <rect class="cc-loupe-hull" x="68" y="76" width="184" height="96" rx="6"/>
                <line class="cc-axle-line" x1="40" y1="124" x2="280" y2="124"/>
                <rect class="cc-star-accent" x="150" y="88" width="10" height="72"/>
                <rect class="cc-star-accent" x="168" y="88" width="10" height="72"/>
                <rect class="cc-star-accent" x="186" y="88" width="10" height="72"/>
                <rect class="cc-star-accent" x="204" y="88" width="10" height="72"/>
                <text class="cc-svg-caption-text" x="160" y="34" text-anchor="middle">1:5 Right-Halfshaft Wet Disc Pack</text>
              </g>
              <g class="cc-loupe-view" data-cc-loupe-view="2" hidden>
                <line class="cc-torque-flow-a" x1="42" y1="124" x2="278" y2="124"/>
                <rect class="cc-panel-outline" x="88" y="102" width="140" height="44" rx="4"/>
                <circle class="cc-star-accent" cx="142" cy="178" r="24"/>
                <circle class="cc-loupe-hull" cx="196" cy="74" r="22"/>
                <text class="cc-svg-caption-text" x="160" y="28" text-anchor="middle">1:5 Solid + Hollow Coaxial Input</text>
              </g>
              <g class="cc-loupe-view" data-cc-loupe-view="3" hidden>
                <circle class="cc-loupe-hull" cx="160" cy="128" r="68"/>
                <circle class="cc-panel-outline" cx="160" cy="128" r="30"/>
                <path class="cc-strut-line" d="M 96 76 A 78 78 0 0 1 132 52 L 144 82 A 42 42 0 0 0 116 98 Z"/>
                <text class="cc-svg-caption-text" x="160" y="30" text-anchor="middle">1:5 Ventilated Disc &amp; Alloy Bell</text>
              </g>
            </svg>"""
    return f"""      <section class="cc-observatory" id="axle-anatomy" data-cc-loupe aria-labelledby="cc-loupe-h">
        <p class="tp-kicker">{bi("span", lx["kicker_en"], lx["kicker_es"])}</p>
        {bi("h2", lx["title_en"], lx["title_es"], "cc-h2", 'id="cc-loupe-h"')}
        {bi("p", lx["intro_en"], lx["intro_es"], "cc-lede")}
        <div class="cc-pill-bar" role="group" aria-label="{a('Selector de escala del eje delantero' if is_es else 'Front bay scale selector')}">{btns}</div>
        <div class="cc-loupe-grid">
          <div class="cc-panel">
            <div class="cc-panel-head">{bi("span", "1:20 Front Bay Layout", "Esquema 1:20 del Eje Delantero", "cc-panel-tag")}<span class="cc-panel-tag">SVG · CLICK NODE</span></div>
            {sec_svg}
          </div>
          <div class="cc-panel">
            <div class="cc-panel-head">{bi("span", "1:5 Mechanical Detail Loupe", "Lupa Mecánica 1:5", "cc-panel-tag")}<span class="cc-panel-tag">DETAIL VIEW</span></div>
            {loupe_svg}
{chr(10).join(info_cards)}
          </div>
        </div>
      </section>"""


def render_sankey_ribbon(is_es: bool) -> str:
    sx = C.SANKEY_TEXT
    buttons = [
        ("lock", "VAQ 1,600 Nm Lock", "Bloqueo VAQ 1,600 Nm", True),
        ("xds", "XDS+ Brake Vectoring", "Vectorización XDS+", False),
        ("open", "Open Differential", "Diferencial Abierto", False),
    ]
    btns_html = "".join(
        f'<button type="button" class="cc-pill-btn" data-cc-flow="{k}" aria-pressed="{"true" if act else "false"}" '
        f'data-en="{a(en)}" data-es="{a(es)}">{t(es if is_es else en)}</button>'
        for k, en, es, act in buttons
    )
    svg = """<svg class="cc-svg-stage cc-sankey-svg" viewBox="0 0 640 215" width="640" height="215" role="img" aria-labelledby="cc-sankey-t">
              <title id="cc-sankey-t">Alluvial front-axle torque flow ribbon across open, XDS+, and VAQ lock at 3,000 Nm demand</title>
              <rect class="cc-loupe-hull" x="24" y="64" width="24" height="86" rx="3"/>
              <text class="cc-svg-caption-text" x="14" y="48">3,000 Nm Axle</text>
              <g class="is-active" data-cc-sankey-mode="lock">
                <path class="cc-sankey-flow cc-sankey-out" d="M 48 92 C 180 92, 240 60, 560 60"/>
                <path class="cc-sankey-flow cc-sankey-in" d="M 48 134 C 180 134, 240 128, 560 128"/>
                <rect class="cc-star-accent" x="560" y="34" width="24" height="122" rx="3"/>
                <text class="cc-svg-sub-text" x="305" y="46" text-anchor="middle">1,728 Nm Outside + 832 Nm Inside = 2,560 Nm Tarmac</text>
                <text class="cc-svg-caption-text" x="572" y="186" text-anchor="end">Brake Heat: 0 Nm</text>
              </g>
              <g data-cc-sankey-mode="xds" hidden>
                <path class="cc-sankey-flow cc-sankey-out" d="M 48 86 C 180 86, 240 60, 560 60"/>
                <path class="cc-sankey-flow cc-sankey-in" d="M 48 118 C 180 118, 240 114, 560 114"/>
                <path class="cc-sankey-flow cc-sankey-waste" d="M 48 144 C 180 144, 240 168, 560 168"/>
                <rect class="cc-star-accent" x="560" y="40" width="24" height="92" rx="3"/>
                <rect class="cc-loupe-hull" x="560" y="150" width="24" height="36" rx="3"/>
                <text class="cc-svg-sub-text" x="305" y="46" text-anchor="middle">1,332 Nm Out + 832 Nm In = 2,164 Nm Tarmac</text>
                <text class="cc-svg-caption-text" x="305" y="190" text-anchor="middle">500 Nm Inside Brake Dissipation</text>
              </g>
              <g data-cc-sankey-mode="open" hidden>
                <path class="cc-sankey-flow cc-sankey-in" d="M 48 84 C 180 84, 240 72, 560 72"/>
                <path class="cc-sankey-flow cc-sankey-waste" d="M 48 134 C 180 134, 240 162, 560 162"/>
                <rect class="cc-star-accent" x="560" y="54" width="24" height="44" rx="3"/>
                <rect class="cc-loupe-hull" x="560" y="142" width="24" height="44" rx="3"/>
                <text class="cc-svg-sub-text" x="305" y="54" text-anchor="middle">832 Nm + 832 Nm = 1,664 Nm Balanced Road Cap</text>
                <text class="cc-svg-caption-text" x="305" y="186" text-anchor="middle">1,336 Nm Unused / Inside Spin</text>
              </g>
            </svg>"""
    return f"""        <div class="cc-sankey-box" data-cc-sankey>
          <div class="cc-panel-head">
            {bi("span", sx["kicker_en"], sx["kicker_es"], "cc-panel-tag")}
            <span class="cc-panel-tag">SVG · ALLUVIAL FLOW</span>
          </div>
          {bi("h3", sx["title_en"], sx["title_es"], "cc-card-move")}
          {bi("p", sx["intro_en"], sx["intro_es"], "cc-small")}
          <div class="cc-pill-bar" role="group" aria-label="{a('Selector de estrategia de flujo de par' if is_es else 'Torque flow strategy selector')}">{btns_html}</div>
          <div class="cc-svg-scroll">{svg}</div>
          <p class="cc-readout" data-cc-sankey-readout aria-live="polite" data-lock-en="{a(sx['readout_lock_en'])}" data-lock-es="{a(sx['readout_lock_es'])}" data-xds-en="{a(sx['readout_xds_en'])}" data-xds-es="{a(sx['readout_xds_es'])}" data-open-en="{a(sx['readout_open_en'])}" data-open-es="{a(sx['readout_open_es'])}">{t(sx['readout_lock_es'] if is_es else sx['readout_lock_en'])}</p>
          <table class="sr-only"><caption>MODEL 3,000 Nm differential torque conservation</caption><thead><tr><th>Strategy</th><th>Road Drive</th><th>Brake / Unused</th></tr></thead><tbody><tr><td>VAQ 1,600 Nm</td><td>2,560 Nm</td><td>0 Nm</td></tr><tr><td>XDS+</td><td>2,164 Nm</td><td>500 Nm</td></tr><tr><td>Open</td><td>1,664 Nm</td><td>1,336 Nm</td></tr></tbody></table>
          {cite(sx["src"])}
        </div>"""


def render_polar_radar(is_es: bool) -> str:
    rx = C.RADAR_TEXT
    axes_en, axes_es = rx["axes_en"], rx["axes_es"]
    cx, cy, r_max = 240.0, 160.0, 94.0
    angles = [-math.pi / 2 + i * (math.pi / 3) for i in range(6)]
    rings = "".join(
        f'<polygon class="cc-radar-ring" points="{" ".join(f"{cx + r_max * frac * math.cos(th):.1f},{cy + r_max * frac * math.sin(th):.1f}" for th in angles)}"/>'
        for frac in (0.33, 0.66, 1.0)
    )
    spokes = "".join(
        f'<line class="cc-stage-axis" x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx + r_max * math.cos(th):.1f}" y2="{cy + r_max * math.sin(th):.1f}"/>'
        for th in angles
    )
    labels = ""
    for i, th in enumerate(angles):
        lx = cx + (r_max + 20) * math.cos(th)
        ly = cy + (r_max + 20) * math.sin(th) + 4
        anc = "middle" if abs(math.cos(th)) < 0.25 else ("start" if math.cos(th) > 0 else "end")
        labels += f'<text class="cc-svg-sub-text" x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anc}" data-en="{a(axes_en[i])}" data-es="{a(axes_es[i])}">{t(axes_es[i] if is_es else axes_en[i])}</text>'
    init_scores = C.RADAR_ERAS[-1]["scores"]
    init_pts = " ".join(f"{cx + r_max * (sc / 100.0) * math.cos(angles[i]):.1f},{cy + r_max * (sc / 100.0) * math.sin(angles[i]):.1f}" for i, sc in enumerate(init_scores))
    era_btns = "".join(
        f'<button type="button" class="cc-pill-btn" data-cc-radar-era="{a(e["id"])}" '
        f'data-scores="{",".join(str(x) for x in e["scores"])}" '
        f'data-note-en="{a(e["note_en"])}" data-note-es="{a(e["note_es"])}" '
        f'aria-pressed="{"true" if idx == len(C.RADAR_ERAS) - 1 else "false"}" '
        f'data-en="{a(e["label_en"])}" data-es="{a(e["label_es"])}">{t(e["label_es"] if is_es else e["label_en"])}</button>'
        for idx, e in enumerate(C.RADAR_ERAS)
    )
    init_e = C.RADAR_ERAS[-1]
    return f"""      <section class="cc-observatory cc-radar-panel" id="envelope-radar" data-cc-radar aria-labelledby="cc-radar-h">
        <p class="tp-kicker">{bi("span", rx["kicker_en"], rx["kicker_es"])}</p>
        {bi("h2", rx["title_en"], rx["title_es"], "cc-h2", 'id="cc-radar-h"')}
        {bi("p", rx["intro_en"], rx["intro_es"], "cc-lede")}
        <div class="cc-bench">
          <svg class="cc-svg-stage cc-radar-svg" viewBox="0 0 480 320" width="480" height="320" role="img" aria-labelledby="cc-radar-t">
            <title id="cc-radar-t">Six-axis polar vehicle-dynamics envelope comparison (MODEL comparative index 0 to 100)</title>
            {rings}{spokes}
            <polygon class="cc-radar-poly" points="{init_pts}"/>
            {labels}
          </svg>
          <div class="cc-controls">
            <div class="cc-pill-bar" role="group" aria-label="{a('Selector de etapa en gráfica polar' if is_es else 'Era radar comparison selector')}">{era_btns}</div>
            <p class="cc-readout" data-cc-radar-readout aria-live="polite">{t(init_e["note_es"] if is_es else init_e["note_en"])}</p>
            {cite(rx["src"])}
          </div>
        </div>
      </section>"""


def render_atelier_section(is_es: bool) -> str:
    """Coupled 2D Cornering Grip-Circle SVG + 3D WebGL2 4-mode Hardware Atelier with .GLB & .DXF CAD export."""
    ax = C.ATELIER_TEXT
    y0 = M.corner_load_and_yaw(0.70, 2400.0, "lock")
    m_d = M.DIFF_MODEL
    m_c = M.CORNER_YAW_MODEL
    modes = [
        ("vaq", "VAQ + Differential", "Diferencial + VAQ"),
        ("strut", "MacPherson Strut", "Puntal MacPherson"),
        ("dct", "Coaxial 6-Spd DCT", "Doble Embrague DSG"),
        ("rear", "Quarter-Car Spring", "Cuarto de Auto"),
    ]
    mode_btns = "".join(
        f'<button type="button" class="cc-pill-btn" data-cc-hardware="{k}" aria-pressed="{"true" if k == "vaq" else "false"}" '
        f'data-en="{a(en)}" data-es="{a(es)}">{t(es if is_es else en)}</button>'
        for k, en, es in modes
    )
    strat_modes = [("open", "Open"), ("xds", "XDS+"), ("lock", "VAQ")]
    strat_btns = "".join(
        f'<button type="button" class="cc-pill-btn" data-cc-strat="{k}" aria-pressed="{"true" if k == "lock" else "false"}">{t(lbl)}</button>'
        for k, lbl in strat_modes
    )
    ay_label = "Aceleración lateral en curva a_y" if is_es else "Cornering lateral acceleration a_y"
    dem_label = "Demanda de par al eje delantero T_req" if is_es else "Front axle torque demand T_req"
    corner_svg_title = (
        "Transferencia lateral de carga 2D y elipses de agarre conectadas al modelo 3D"
        if is_es else "Coupled 2D cornering weight transfer and front traction circles driving 3D hardware stresses"
    )
    canvas_aria = (
        "Ensamble 3D interactivo del chasis GTI (arrastra para orbitar, rueda o +/- para zoom, flechas para rotar, R para reiniciar)"
        if is_es else "Interactive 3D GTI chassis assembly (drag to orbit, wheel or +/- to zoom, arrows to rotate, R to reset)"
    )
    svg_2d = f"""<svg class="cc-corner-svg sf-svg-stage cc-svg-stage" viewBox="0 0 460 320" width="460" height="320" role="img" aria-labelledby="cc-corner-svg-t">
              <title id="cc-corner-svg-t">{t(corner_svg_title)}</title>
              <line class="cc-stage-axis" x1="32" y1="228" x2="428" y2="228"/>
              <line class="cc-stage-axis" x1="230" y1="32" x2="230" y2="296"/>
              <line class="cc-chassis-roll" x1="76" y1="92" x2="384" y2="92"/>
              <circle class="cc-grip-circle cc-grip-in" cx="122" cy="184" r="46"/>
              <circle class="cc-grip-circle cc-grip-out" cx="338" cy="184" r="68"/>
              <line class="cc-torque-vec cc-vec-in" x1="122" y1="184" x2="122" y2="142"/>
              <line class="cc-torque-vec cc-vec-out" x1="338" y1="184" x2="338" y2="106"/>
              <path class="cc-yaw-arc" d="M 192 260 A 44 44 0 0 0 268 260"/>
              <text class="cc-svg-caption-text" x="122" y="252" text-anchor="middle" data-en="Inside Grip μ·N_in·r" data-es="Agarre Interior μ·N_in·r">Inside Grip μ·N_in·r</text>
              <text class="cc-svg-caption-text" x="338" y="274" text-anchor="middle" data-en="Outside Grip μ·N_out·r" data-es="Agarre Exterior μ·N_out·r">Outside Grip μ·N_out·r</text>
              {bi("text", "Direct Yaw Couple M_z", "Par Directo de Guiñada M_z", "cc-svg-sub-text", 'x="230" y="294" text-anchor="middle"')}
            </svg>"""
    return f"""      <section class="cc-observatory" id="atelier" data-cc-atelier data-r="{m_d['radius_m']}" data-mu="{m_d['mu']}" data-brake="{m_d['brake_max_nm']}" data-lock="{m_d['lock_max_nm']}" data-n0="{m_c['static_wheel_n']}" data-tref="{m_c['transfer_ref_n']}" data-ayref="{m_c['ay_ref_g']}" data-track="{m_c['track_front_m']}" aria-labelledby="cc-atelier-h">
        <p class="tp-kicker">{bi("span", ax["kicker_en"], ax["kicker_es"])}</p>
        {bi("h2", ax["title_en"], ax["title_es"], "cc-h2", 'id="cc-atelier-h"')}
        {bi("p", ax["intro_en"], ax["intro_es"], "cc-lede cc-dropcap")}
        <div class="cc-atelier-grid">
          <div class="cc-panel">
            <div class="cc-panel-head">
              {bi("span", "2D Cornering Grip Circles & Yaw Solver", "Elipses de Agarre y Guiñada 2D", "cc-panel-tag")}
              <span class="cc-panel-tag">SVG · LIVE DYNAMICS</span>
            </div>
            {svg_2d}
            <div class="cc-pill-bar" role="group" aria-label="{a('Estrategia diferencial en curva' if is_es else 'Cornering differential strategy')}">{strat_btns}</div>
            <div class="cc-controls-row">
              <div class="cc-control-group">
                <label class="cc-range-label" for="cc-ay-range"><span>{t(ay_label)}</span><span class="cc-range-val" id="cc-ay-val">0.70 g</span></label>
                <input id="cc-ay-range" class="cc-range" type="range" min="0.00" max="0.95" step="0.05" value="0.70" aria-valuetext="0.70 g">
              </div>
              <div class="cc-control-group">
                <label class="cc-range-label" for="cc-demand-range"><span>{t(dem_label)}</span><span class="cc-range-val" id="cc-demand-val">2,400 Nm</span></label>
                <input id="cc-demand-range" class="cc-range" type="range" min="0" max="3000" step="100" value="2400" aria-valuetext="2,400 Nm">
              </div>
            </div>
            <p class="cc-readout" data-cc-corner-readout aria-live="polite" data-en="MODEL N_in = {y0['load_in_n']:.0f} N · N_out = {y0['load_out_n']:.0f} N · T_road = {y0['road']:.0f} Nm · M_z = {y0['yaw_knm']:.2f} kN·m" data-es="MODELO N_in = {y0['load_in_n']:.0f} N · N_out = {y0['load_out_n']:.0f} N · T_road = {y0['road']:.0f} Nm · M_z = {y0['yaw_knm']:.2f} kN·m">{'MODELO' if is_es else 'MODEL'} N_in = {y0['load_in_n']:.0f} N · N_out = {y0['load_out_n']:.0f} N · T_road = {y0['road']:.0f} Nm · M_z = {y0['yaw_knm']:.2f} kN·m</p>
          </div>
          <div class="cc-panel">
            <div class="cc-panel-head">
              {bi("span", "3D Watertight Chassis Hardware", "Hardware de Chasis 3D Cerrado", "cc-panel-tag")}
              <span class="cc-panel-tag">WebGL2 · .GLB · .DXF</span>
            </div>
            <div class="cc-pill-bar" role="group" aria-label="{a('Selector de subsistema mecánico 3D' if is_es else '3D Mechanical subsystem selector')}">{mode_btns}</div>
            <div class="cc-canvas-wrap">
              <canvas id="cc-webgl-canvas" class="cc-webgl-canvas" width="640" height="480" tabindex="0" aria-label="{a(canvas_aria)}"></canvas>
            </div>
            <div class="cc-check-row">
              <label class="cc-check"><input type="checkbox" id="cc-show-wire" checked> {bi("span", "Overlay kinematic torque vectors & streamlines", "Superponer ejes cinemáticos y líneas")}</label>
            </div>
            <div class="cc-export-row">
              <button type="button" class="cc-btn" data-cc-export="glb" data-en="Export 3D Model (.glb)" data-es="Exportar Modelo 3D (.glb)">Export 3D Model (.glb)</button>
              <button type="button" class="cc-btn cc-btn-quiet" data-cc-export="dxf" data-en="Export CAD Wireframe (.dxf)" data-es="Exportar Plantilla CAD (.dxf)">Export CAD Wireframe (.dxf)</button>
            </div>
            <p class="cc-readout" data-cc-cad-readout aria-live="polite" data-en="3D VAQ assembly ready · Yaw M_z = {y0['yaw_knm']:.2f} kN·m" data-es="Ensamble 3D VAQ listo · Guiñada M_z = {y0['yaw_knm']:.2f} kN·m">{t(f"Ensamble 3D VAQ listo · Guiñada M_z = {y0['yaw_knm']:.2f} kN·m" if is_es else f"3D VAQ assembly ready · Yaw M_z = {y0['yaw_knm']:.2f} kN·m")}</p>
          </div>
        </div>
        <div class="cc-science">
          {bi("p", ax["science_en"], ax["science_es"])}
          {cite(["pacejka1992", "abe2001", "rubin2015", "trachtler2004"])}
        </div>
{render_sankey_ribbon(is_es)}
      </section>"""


def render_engineers_study_section(is_es: bool) -> str:
    """For studying automotive & chassis engineers: 4 Subsystem Atlas, Grammar Table, 6-Station Lineage + 2 Cutaway Plates."""
    ex = C.ENGINEERS_STUDY
    by_id = _media_map()
    sub_cards = "".join(
        f"""          <article class="cc-quadric-card">
            {bi("h3", s["name_en"], s["name_es"], "cc-card-move")}
            {bi("p", s["rule_en"], s["rule_es"], "cc-small")}
            <p class="cc-quadric-loc">{bi("span", s["where_en"], s["where_es"])}</p>
          </article>"""
        for s in ex["subsystems"]
    )
    sub_svg = """<svg class="cc-svg-stage cc-subsystems-svg" viewBox="0 0 760 175" width="760" height="175" role="img" aria-labelledby="cc-sub-svg-t">
              <title id="cc-sub-svg-t">Four automotive engineering schematics: MacPherson strut axis, boosted GDI chamber, coaxial dual clutch, and rear suspension compliance</title>
              <g transform="translate(20 15)">
                <rect class="cc-panel-outline" x="0" y="0" width="165" height="145" rx="4"/>
                <line class="cc-strut-line" x1="108" y1="24" x2="64" y2="110"/>
                <line class="cc-stage-axis" x1="64" y1="110" x2="132" y2="110"/>
                <path class="cc-torque-flow-b" d="M 86 38 L 106 48 L 80 62 L 100 72 L 74 86"/>
                <text class="cc-svg-caption-text" x="82" y="134" text-anchor="middle">1 · MacPherson Axis</text>
              </g>
              <g transform="translate(205 15)">
                <rect class="cc-panel-outline" x="0" y="0" width="165" height="145" rx="4"/>
                <circle class="cc-star-accent" cx="56" cy="70" r="24"/>
                <path class="cc-torque-flow-a" d="M 80 62 Q 112 42 138 68"/>
                <rect class="cc-loupe-hull" x="96" y="82" width="44" height="30" rx="3"/>
                <text class="cc-svg-caption-text" x="82" y="134" text-anchor="middle">2 · GDI + Turbo Boost</text>
              </g>
              <g transform="translate(390 15)">
                <rect class="cc-panel-outline" x="0" y="0" width="165" height="145" rx="4"/>
                <line class="cc-torque-flow-a" x1="22" y1="62" x2="142" y2="62"/>
                <line class="cc-strut-line" x1="22" y1="88" x2="142" y2="88"/>
                <circle class="cc-star-accent" cx="96" cy="62" r="14"/>
                <circle class="cc-loupe-hull" cx="122" cy="88" r="14"/>
                <text class="cc-svg-caption-text" x="82" y="134" text-anchor="middle">3 · Coaxial DSG + VAQ</text>
              </g>
              <g transform="translate(575 15)">
                <rect class="cc-panel-outline" x="0" y="0" width="165" height="145" rx="4"/>
                <line class="cc-stage-axis" x1="28" y1="112" x2="138" y2="112"/>
                <line class="cc-strut-line" x1="40" y1="42" x2="128" y2="66"/>
                <line class="cc-torque-flow-b" x1="40" y1="84" x2="128" y2="76"/>
                <circle class="cc-loupe-hull" cx="128" cy="72" r="16"/>
                <text class="cc-svg-caption-text" x="82" y="134" text-anchor="middle">4 · Rear Kinematics</text>
              </g>
            </svg>"""
    ghead = "".join(bi("th", en, es, "", 'scope="col"') for en, es in zip(ex["grammar_head_en"], ex["grammar_head_es"]))
    grows = "".join(
        f'<tr>{bi("th", r_en, r_es, "", "scope=\"row\"")}{bi("td", f_en, f_es, "cc-num")}{bi("td", w_en, w_es)}<td>{stamp(skey)}</td></tr>'
        for r_en, r_es, f_en, f_es, w_en, w_es, skey in ex["grammar_rows"]
    )

    lin_btns = []
    lin_svg_nodes = []
    lin_cards = []
    node_xs = (74, 212, 350, 488, 626, 764)
    for idx, node in enumerate(ex["lineage"]):
        pressed = "true" if idx == 0 else "false"
        active = "cc-relay-seg is-active" if idx == 0 else "cc-relay-seg"
        lbl_en = f"{node['year']} · {node['short_en']}"
        lbl_es = f"{node['year']} · {node['short_es']}"
        lin_btns.append(
            f'<button type="button" class="cc-pill-btn" data-cc-lineage-btn="{idx}" aria-pressed="{pressed}" '
            f'data-en="{a(lbl_en)}" data-es="{a(lbl_es)}">{t(lbl_es if is_es else lbl_en)}</button>'
        )
        lin_svg_nodes.append(
            f'<g class="{active}" data-cc-lineage-node="{idx}">'
            f'<rect class="cc-relay-bar" x="{node_xs[idx] - 64}" y="18" width="128" height="28" rx="4"/>'
            f'<text class="cc-svg-caption-text" x="{node_xs[idx]}" y="36" text-anchor="middle">{t(node["short_es"] if is_es else node["short_en"])}</text>'
            f'<text class="cc-svg-sub-text" x="{node_xs[idx]}" y="66" text-anchor="middle">{t(node["year"])}</text></g>'
        )
        hid = "" if idx == 0 else " hidden"
        lin_cards.append(
            f"""          <article class="cc-relay-card cc-lineage-card" data-cc-lineage-card="{idx}"{hid}>
            <div class="cc-relay-head">
              {bi("h3", node["title_en"], node["title_es"], "cc-card-move")}
              <span class="cc-panel-tag">{t(node["who_en"])}</span>
            </div>
            {bi("p", node["note_en"], node["note_es"], "cc-card-body")}
            {bi("p", node["boundary_en"], node["boundary_es"], "cc-small")}
            {cite(node["src"])}
          </article>"""
        )
    lineage_svg = f"""<svg class="cc-svg-stage cc-relay-stage" viewBox="0 0 840 84" width="840" height="84" role="img" aria-labelledby="cc-lin-svg-t">
              <title id="cc-lin-svg-t">Vehicle dynamics peer-reviewed scholarship lineage across ride, MacPherson struts, tyres, GDI combustion, rear suspension, and VDM control</title>
              <line class="cc-stage-axis" x1="16" y1="32" x2="824" y2="32"/>
              {"".join(lin_svg_nodes)}
            </svg>"""
    return f"""      <section class="cc-observatory cc-engineers-study" id="engineers-study" aria-labelledby="cc-eng-study-h">
        <p class="tp-kicker">{bi("span", ex["kicker_en"], ex["kicker_es"])}</p>
        {bi("h2", ex["title_en"], ex["title_es"], "cc-h2", 'id="cc-eng-study-h"')}
        {bi("p", ex["intro_en"], ex["intro_es"], "cc-lede")}
        {sub_svg}
        <div class="cc-quadric-cards">
{sub_cards}
        </div>
        <div class="cc-study-plates-grid">
{render_inline_figure(by_id["plate-turbo-gdi"], is_es, "cc-study-plate")}
{render_inline_figure(by_id["plate-vaq-corner"], is_es, "cc-study-plate")}
        </div>
        <div class="cc-interlude">
          {bi("h3", "Chassis & Powertrain Constructive Grammar", "Gramática constructiva de chasis y tren motriz", "cc-int-h")}
          <div class="cc-table-wrap"><table class="cc-table"><thead><tr>{ghead}</tr></thead><tbody>{grows}</tbody></table></div>
        </div>
        <div class="cc-lineage-box" data-cc-lineage>
          {bi("h3", ex["lineage_title_en"], ex["lineage_title_es"], "cc-int-h")}
          {bi("p", ex["lineage_intro_en"], ex["lineage_intro_es"], "cc-small")}
          <div class="cc-pill-bar" role="group" aria-label="{a('Hitos bibliográficos de dinámica vehicular' if is_es else 'Engineering literature timeline stations')}">{"".join(lin_btns)}</div>
          {lineage_svg}
{chr(10).join(lin_cards)}
        </div>
{render_inline_figure(by_id["plate-vdm-apex"], is_es, "cc-light-figure")}
      </section>"""


# --------------------------------------------------------------------------------------------- Ghost Race & Mechanics Lab Part VI

LOOP = "M 80 60 L 420 60 C 520 60 540 140 480 180 L 360 250 C 320 274 320 300 360 300 L 520 300 C 600 300 600 400 520 400 L 80 400 C 20 400 20 60 80 60 Z"


def render_laps_section(is_es: bool) -> str:
    x = C.LAPS_TEXT
    fastest = min(lap[5] for lap in C.LAPS)
    dots, legend, rows = [], [], []
    for i, (gen, car, year, ps, ts, secs, driver, tyres, cfg) in enumerate(C.LAPS):
        hue = ("cc-dot-a", "cc-dot-b", "cc-dot-c", "cc-dot-d", "cc-dot-e", "cc-dot-f", "cc-dot-g", "cc-dot-h")[i]
        nolen = "" if cfg else " cc-ghost-nolen"
        dots.append(
            f'<g class="cc-ghost {hue}{nolen}" data-secs="{secs}"><circle r="9" cx="80" cy="60"/>'
            f'<text x="80" y="64" text-anchor="middle">{i + 1}</text></g>'
        )
        legend.append(f'<li class="{hue}{nolen}"><span class="cc-ghost-key" aria-hidden="true">{i + 1}</span> {t(gen)} · {t(car)} ({year})</li>')
        cfg_cell = cfg if cfg else ("en blanco" if is_es else "blank")
        tyres_cell = tyres if tyres != "not stated" else ("no se indica" if is_es else "not stated")
        rows.append(
            f'<tr><td>{i + 1}</td><td>{t(gen)}</td><th scope="row">{t(car)}</th><td>{year}</td><td>{ps} PS</td>'
            f'<td class="cc-num">{t(ts)}</td><td>{t(driver)}</td><td>{t(tyres_cell)}</td><td>{t(cfg_cell)}</td></tr>'
        )
    cols = [
        ("#", "#"), ("Gen", "Gen"), ("Car, as listed", "Auto, como aparece"), ("Year", "Año"), ("Output", "Potencia"),
        ("Lap", "Vuelta"), ("Driver", "Piloto"), ("Tyres", "Llantas"), ("Configuration", "Configuración"),
    ]
    head = "".join(bi("th", en, es, "", 'scope="col"') for en, es in cols)
    start = ("Iniciar carrera", "Repetir") if is_es else ("Start the race", "Run it again")
    return f"""      <section class="cc-observatory cc-laps" id="ghost-race" aria-labelledby="cc-laps-h">
        {bi("h2", x["title_en"], x["title_es"], "cc-h2", 'id="cc-laps-h"')}
        {bi("p", x["intro_en"], x["intro_es"], "cc-lede cc-dropcap")}
        <div class="cc-bench cc-race" data-cc-race data-fastest="{fastest}">
          <svg class="cc-loop-svg" viewBox="0 0 620 460" width="620" height="460" role="img" aria-labelledby="cc-loop-title">
            <title id="cc-loop-title">Schematic loop with eight numbered dots, one per lap time</title>
            <path class="cc-loop-tar" d="{LOOP}"/>
            <path class="cc-loop-line" id="cc-loop-path" d="{LOOP}"/>
            <line class="cc-loop-flag" x1="80" y1="44" x2="80" y2="76"/>
            {''.join(dots)}
          </svg>
          <div class="cc-controls">
            <button type="button" class="cc-btn" data-cc-race-start data-label-start="{a(start[0])}" data-label-again="{a(start[1])}">{t(start[0])}</button>
            <ol class="cc-ghost-legend">{''.join(legend)}</ol>
            <p class="cc-readout" aria-live="polite" data-en="Eight cars on the grid." data-es="Ocho autos en la parrilla.">Eight cars on the grid.</p>
          </div>
        </div>
        {bi("p", x["loop_en"], x["loop_es"], "cc-small")}
        <div class="cc-table-wrap"><table class="cc-table cc-lap-table"><thead><tr>{head}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>
        {cite(["wiki-nords"])}
        {bi("p", x["read_en"], x["read_es"], "cc-lede")}
        <div class="cc-science">
          {bi("p", x["caveat_en"], x["caveat_es"])}
          {cite(["wiki-nords", "vw-history"])}
        </div>
      </section>"""


def _nm(x: float) -> str:
    return f"{round(x):,} Nm"


def render_lab_section(is_es: bool) -> str:
    """Part VI · Mechanics Lab: blocks 1–3 strictly match verify_cc01_mechanics.py; 4–5 expand cornering yaw & DCT shifts."""
    L = C.LAB
    m = M.DIFF_MODEL
    demand = m["demand_max_nm"]
    modes = [("open", "Open differential", "Diferencial abierto"), ("xds", "XDS+ brake", "Freno XDS+"), ("lock", "Clutch-pack lock", "Bloqueo por embragues")]
    rows = []
    for key, en, es in modes:
        r = M.axle_split(demand, key)
        rows.append(
            f'<tr data-mode="{key}">{bi("th", en, es, "", "scope=\"row\"")}<td class="cc-num">{_nm(r["road_in"])}</td>'
            f'<td class="cc-num">{_nm(r["road_out"])}</td><td class="cc-num">{_nm(r["brake"])}</td>'
            f'<td class="cc-num cc-strong">{_nm(r["road"])}</td></tr>'
        )
    dcols = [("Strategy", "Estrategia"), ("Inside wheel", "Rueda interior"), ("Outside wheel", "Rueda exterior"), ("Brake", "Freno"), ("To the road", "Al camino")]
    dhead = "".join(bi("th", en, es, "", 'scope="col"') for en, es in dcols)
    g_in, g_out = M.grip_nm(m["load_in_n"]), M.grip_nm(m["load_out_n"])
    inputs_en = (
        f"Inputs (MODEL): axle torque demand {round(demand):,} Nm, wheel radius {m['radius_m']} m, friction "
        f"coefficient {m['mu']}, inside load {round(m['load_in_n']):,} N, outside load {round(m['load_out_n']):,} N, "
        f"brake up to {round(m['brake_max_nm'])} Nm. Locking torque 1,600 Nm (VW). Grip limits: inside "
        f"{_nm(g_in)}, outside {_nm(g_out)}."
    )
    inputs_es = (
        f"Entradas (MODELO): par pedido al eje {round(demand):,} Nm, radio de rueda {m['radius_m']} m, coeficiente "
        f"de fricción {m['mu']}, carga interior {round(m['load_in_n']):,} N, carga exterior {round(m['load_out_n']):,} N, "
        f"freno de hasta {round(m['brake_max_nm'])} Nm. Par de bloqueo 1,600 Nm (VW). Límites de agarre: interior "
        f"{_nm(g_in)}, exterior {_nm(g_out)}."
    )
    lap_rows = []
    for gen, car, year, _ps, ts, secs, *_r, cfg in C.LAPS:
        if not cfg:
            continue
        lap_rows.append(
            f'<tr><td>{t(gen)}</td><th scope="row">{t(car)}</th><td>{year}</td><td class="cc-num">{t(ts)}</td>'
            f'<td class="cc-num cc-strong" data-lap-kmh="{secs}">{M.lap_speed_kmh(secs):.1f} km/h</td></tr>'
        )
    lcols = [("Gen", "Gen"), ("Car, as listed", "Auto, como aparece"), ("Year", "Año"), ("Lap", "Vuelta"), ("Average (DERIVED)", "Promedio (DERIVADO)")]
    lhead = "".join(bi("th", en, es, "", 'scope="col"') for en, es in lcols)
    q = M.QUARTER_MODEL
    f_body, f_hop = M.quarter_car_hz(q["m_u_start"])
    q_inputs_en = f"Inputs (MODEL): sprung mass {round(q['m_s'])} kg, suspension rate {round(q['k_s']):,} N/m, tyre rate {round(q['k_t']):,} N/m."
    q_inputs_es = f"Entradas (MODELO): masa suspendida {round(q['m_s'])} kg, rigidez de suspensión {round(q['k_s']):,} N/m, rigidez de llanta {round(q['k_t']):,} N/m."
    qlabel = "Masa no suspendida" if is_es else "Unsprung mass"

    # Block 4: Corner load transfer + yaw couple at 2,400 Nm demand (MODEL)
    yaw_rows = []
    for ay, key, en_lbl, es_lbl in (
        (0.00, "lock", "0.00 g · VAQ (straight)", "0.00 g · VAQ (recta)"),
        (0.70, "open", "0.70 g · Open differential", "0.70 g · Diferencial abierto"),
        (0.70, "xds", "0.70 g · XDS+ (500 Nm max brake)", "0.70 g · XDS+ (500 Nm freno máx)"),
        (0.70, "lock", "0.70 g · VAQ (1,600 Nm max lock)", "0.70 g · VAQ (1,600 Nm bloqueo máx)"),
    ):
        yr = M.corner_load_and_yaw(ay, 2400.0, key)
        yaw_rows.append(
            f'<tr>{bi("th", en_lbl, es_lbl, "", "scope=\"row\"")}<td class="cc-num">{yr["load_in_n"]:.0f} N / {yr["load_out_n"]:.0f} N</td>'
            f'<td class="cc-num">{round(yr["road_in"]):,} / {round(yr["road_out"]):,}</td>'
            f'<td class="cc-num">{round(yr["road"]):,}</td><td class="cc-num cc-strong">{yr["yaw_knm"]:.2f} kN·m</td></tr>'
        )
    yhead = "".join(bi("th", en, es, "", 'scope="col"') for en, es in (
        ("Lateral g & Strategy", "Aceleración y Estrategia"),
        ("Loads N_in / N_out (MODEL)", "Cargas N_in / N_out (MODELO)"),
        ("Wheel Torque In / Out", "Par Rueda Int / Ext"),
        ("Road Total", "Al Camino"),
        ("Yaw Couple M_z", "Par de Guiñada M_z"),
    ))

    # Block 5: Coaxial 6-speed DCT upshift table (MODEL)
    dct_rows = []
    for gf in range(1, 6):
        dr = M.dct_shift_kinematics(gf)
        dct_rows.append(
            f'<tr><th scope="row" class="cc-num">{dr["shift_label"]}</th>'
            f'<td class="cc-num">{dr["r_cur"]:.2f} → {dr["r_next"]:.2f}</td>'
            f'<td class="cc-num">{dr["delta_rpm"]:.0f} rpm</td>'
            f'<td class="cc-num">{round(dr["wheel_torque_nm"]):,} Nm</td>'
            f'<td class="cc-num cc-strong">{dr["slip_energy_kj"]:.2f} kJ</td></tr>'
        )
    d_h = "".join(bi("th", en, es, "", 'scope="col"') for en, es in (
        ("Upshift", "Cambio"),
        ("Ratio Step (MODEL)", "Relación (MODELO)"),
        ("Speed Drop Δrpm", "Salto Δrpm"),
        ("Next-Gear Axle Torque", "Par Siguiente Marcha"),
        ("Overlap Slip Energy", "Energía de Traslape"),
    ))

    return f"""      <section class="cc-part cc-lab" id="part-6" aria-labelledby="part-6-h">
        <header class="cc-part-head">
          <p class="cc-part-num" aria-hidden="true">VI</p>
          <h2 class="cc-h2 cc-part-title" id="part-6-h">{bi("span", "Part VI", "Parte VI")} · {bi("span", L["title_en"], L["title_es"])}</h2>
          <p class="cc-part-years" data-en="Model · Derived · Verified by script" data-es="Modelo · Derivado · Verificado por script">Model · Derived · Verified by script</p>
        </header>
        {bi("p", L["intro_en"], L["intro_es"], "cc-lede cc-dropcap")}
        <article class="cc-lab-block" id="lab-differential">
          {bi("h3", L["diff_h_en"], L["diff_h_es"])}
          {bi("p", L["diff_en"], L["diff_es"])}
          <p class="cc-eq"><code>T_road,max(open) = 2 · μ · N_in · r</code><br><code>T_road(lock) = T_in + min(ΔT, 1,600 Nm, μ · N_out · r − T_in)</code></p>
          <div class="cc-table-wrap"><table class="cc-table cc-lab-diff"><thead><tr>{dhead}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>
          {bi("p", inputs_en, inputs_es, "cc-small")}
          {cite(["scamarcio2023", "kakalis2008", "vw-mk7-chassis"])}
        </article>
        <article class="cc-lab-block" id="lab-laps">
          {bi("h3", L["laps_h_en"], L["laps_h_es"])}
          {bi("p", L["laps_en"], L["laps_es"])}
          <p class="cc-eq"><code>v̄ = 20,600 m ÷ t_lap</code></p>
          <div class="cc-table-wrap"><table class="cc-table cc-lab-laps"><thead><tr>{lhead}</tr></thead><tbody>{''.join(lap_rows)}</tbody></table></div>
          {cite(["wiki-nords"])}
        </article>
        <article class="cc-lab-block" id="lab-quarter-car">
          {bi("h3", L["qc_h_en"], L["qc_h_es"])}
          {bi("p", L["qc_en"], L["qc_es"])}
          <p class="cc-eq"><code>m_s·m_u·ω⁴ − (m_s(k_s + k_t) + m_u·k_s)·ω² + k_s·k_t = 0,  f = ω / 2π</code></p>
          <div class="cc-bench cc-qc" data-cc-qc data-ms="{q['m_s']}" data-ks="{q['k_s']}" data-kt="{q['k_t']}">
            <svg class="cc-qc-svg" viewBox="0 0 220 240" width="220" height="240" role="img" aria-labelledby="cc-qc-title">
              <title id="cc-qc-title">A body block on a spring above a wheel block on a tyre spring, on the road</title>
              <rect class="cc-qc-body" x="50" y="20" width="120" height="50" rx="4"/>
              <path class="cc-qc-spring" d="M110 70 l-14 8 l28 8 l-28 8 l28 8 l-28 8 l28 8 l-14 8"/>
              <rect class="cc-qc-wheel" x="80" y="134" width="60" height="34" rx="4"/>
              <path class="cc-qc-spring cc-qc-tyre" d="M110 168 l-10 6 l20 6 l-20 6 l20 6 l-10 6"/>
              <line class="cc-qc-road" x1="20" y1="204" x2="200" y2="204"/>
              <text class="cc-svg-label" x="176" y="50" data-en="body" data-es="carrocería">body</text>
              <text class="cc-svg-label" x="146" y="156" data-en="wheel" data-es="rueda">wheel</text>
            </svg>
            <div class="cc-controls">
              <label class="cc-range-label" for="cc-qc-range">{t(qlabel)}</label>
              <input id="cc-qc-range" class="cc-range" type="range" min="{q['m_u_min']:.0f}" max="{q['m_u_max']:.0f}" value="{q['m_u_start']:.0f}" step="1" aria-valuetext="{q['m_u_start']:.0f} kg">
              <p class="cc-readout cc-qc-readout" aria-live="polite"><span class="cc-qc-mu">{q['m_u_start']:.0f} kg</span> · <span data-en="body bounce" data-es="rebote de carrocería">body bounce</span> <strong class="cc-qc-body-hz">{f_body:.2f} Hz</strong> · <span data-en="wheel hop" data-es="salto de rueda">wheel hop</span> <strong class="cc-qc-hop-hz">{f_hop:.1f} Hz</strong></p>
            </div>
          </div>
          {bi("p", q_inputs_en, q_inputs_es, "cc-small")}
          {cite(["micromachines2026", "ahmadian2000", "woo2021", "karnopp1974", "hac1992"])}
        </article>
        <article class="cc-lab-block" id="lab-corner-yaw">
          {bi("h3", L["yaw_h_en"], L["yaw_h_es"])}
          {bi("p", L["yaw_en"], L["yaw_es"])}
          <p class="cc-eq"><code>M_z = ((T_out − T_in) / r_w) · (b_f / 2)</code></p>
          <div class="cc-table-wrap"><table class="cc-table"><thead><tr>{yhead}</tr></thead><tbody>{''.join(yaw_rows)}</tbody></table></div>
          {cite(["pacejka1992", "abe2001", "rubin2015"])}
        </article>
        <article class="cc-lab-block" id="lab-dct-handover">
          {bi("h3", L["dct_h_en"], L["dct_h_es"])}
          {bi("p", L["dct_en"], L["dct_es"])}
          <p class="cc-eq"><code>E_slip = 0.5 · T_in · |Δω| · t_overlap</code></p>
          <div class="cc-table-wrap"><table class="cc-table"><thead><tr>{d_h}</tr></thead><tbody>{''.join(dct_rows)}</tbody></table></div>
          {cite(["galvagno2011", "brancati2023"])}
        </article>
        <aside class="cc-interlude cc-verify-box" aria-labelledby="cc-verify-h">
          {bi("h3", L["verify_h_en"], L["verify_h_es"], "cc-int-h", 'id="cc-verify-h"')}
          {bi("p", L["verify_en"], L["verify_es"])}
          <p class="cc-eq"><code>python skills/classics/cc01/verify_cc01_mechanics.py</code><br><code>python skills/classics/cc01/verify_cc01_mechanics.py --planted-defect</code></p>
        </aside>
      </section>"""


def render_visual_gallery_section(is_es: bool) -> str:
    """Single consolidated 14-item visual media archive paired with a zero-jump CSP-safe native <dialog> lightbox."""
    vg = C.VISUAL_GALLERY_TEXT
    cards = "\n".join(render_media_figure(item, is_es, in_gallery=True) for item in (*C.PHOTOS, *C.PLATES))
    btns = (
        f'<button type="button" class="cc-pill-btn" data-cc-filter="all" aria-pressed="true" data-en="{a(vg["all_en"])}" data-es="{a(vg["all_es"])}">{t(vg["all_es"] if is_es else vg["all_en"])}</button>'
        f'<button type="button" class="cc-pill-btn" data-cc-filter="photo" aria-pressed="false" data-en="{a(vg["photos_en"])}" data-es="{a(vg["photos_es"])}">{t(vg["photos_es"] if is_es else vg["photos_en"])}</button>'
        f'<button type="button" class="cc-pill-btn" data-cc-filter="render" aria-pressed="false" data-en="{a(vg["renders_en"])}" data-es="{a(vg["renders_es"])}">{t(vg["renders_es"] if is_es else vg["renders_en"])}</button>'
    )
    hint_en = "← / → Prev & Next · Esc Close"
    hint_es = "← / → Anterior y Siguiente · Esc Cerrar"
    return f"""      <section class="cc-observatory" id="visuals" data-cc-gallery aria-labelledby="cc-vis-h">
        <p class="tp-kicker">{bi("span", vg["kicker_en"], vg["kicker_es"])}</p>
        {bi("h2", vg["title_en"], vg["title_es"], "cc-h2", 'id="cc-vis-h"')}
        {bi("p", vg["intro_en"], vg["intro_es"], "cc-lede")}
        <div class="cc-pill-bar" role="group" aria-label="{a('Filtro de archivo visual' if is_es else 'Visual media filter')}">{btns}</div>
        <div class="cc-gallery-grid">
{cards}
        </div>
        <dialog class="cc-lightbox" id="cc-lightbox" aria-labelledby="cc-lb-badge" aria-describedby="cc-lb-cap">
          <div class="cc-lightbox-bar">
            <span class="cc-panel-tag" id="cc-lb-badge">MEDIA</span>
            {bi("span", hint_en, hint_es, "cc-lb-hint")}
            <div class="cc-pill-bar">
              <button type="button" class="cc-btn cc-btn-quiet" data-cc-lb-prev data-en="Prev" data-es="Anterior">{t("Anterior" if is_es else "Prev")}</button>
              <button type="button" class="cc-btn cc-btn-quiet" data-cc-lb-next data-en="Next" data-es="Siguiente">{t("Siguiente" if is_es else "Next")}</button>
              <button type="button" class="cc-btn" data-cc-lb-close data-en="Close" data-es="Cerrar">{t("Cerrar" if is_es else "Close")}</button>
            </div>
          </div>
          <div class="cc-lightbox-stage">
            <img id="cc-lightbox-img" src="../../images/golf-gti/photo-mk8-gti.jpg" width="1280" height="853" decoding="async" alt="">
          </div>
          <p class="cc-small" id="cc-lb-cap"></p>
        </dialog>
      </section>"""


def render_silent(is_es: bool) -> str:
    rows = "".join(
        f'<div class="cc-silent-row">{bi("dt", q["q_en"], q["q_es"])}{bi("dd", q["a_en"], q["a_es"])}</div>' for q in C.SILENT
    )
    aria = "Lo que las fuentes no dicen" if is_es else "What the sources don't say"
    return f"""        <aside class="cc-silent" aria-label="{a(aria)}">
          {bi("h2", "The sources don’t say", "Las fuentes no lo dicen", "cc-h2")}
          <dl>{rows}</dl>
        </aside>"""


def render_sources(is_es: bool) -> str:
    items = []
    for key, s in C.SOURCES.items():
        en, es = C.KIND_LABEL[s["kind"]]
        items.append(
            f'<li id="src-{a(key)}"><span class="cc-stamp cc-stamp-{s["kind"]}" data-en="{a(en)}" data-es="{a(es)}">{t(es if is_es else en)}</span> '
            f'<a href="{a(s["url"])}" rel="noopener noreferrer">{t(s["label"])}</a></li>'
        )
    note_en = (
        f"All read on {C.ACCESSED}. VW marks a Volkswagen statement; Press marks independent coverage; Paper marks 15 "
        "peer-reviewed articles checked in Crossref and Scite on the same day with zero retractions (general "
        "mechanisms, none tested these cars); Photo Archive marks Wikimedia Commons photographs under PD, CC0, or CC BY attribution."
    )
    note_es = (
        f"Todas consultadas el {C.ACCESSED}. VW marca una declaración de Volkswagen; Prensa, cobertura independiente; "
        "Artículo marca 15 textos arbitrados verificados en Crossref y Scite el mismo día sin retractaciones (mecanismos "
        "generales, ninguno probó estos autos); Archivo Fotográfico marca fotografías reales de Wikimedia Commons en DP, CC0 o CC BY."
    )
    return f"""      <section class="cc-sources" id="sources" aria-labelledby="cc-src-h">
        {bi("h2", "Sources", "Fuentes", "cc-h2", 'id="cc-src-h"')}
        {bi("p", note_en, note_es, "cc-small")}
        <ol class="cc-source-list">
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
    image = "https://informatico.ai/plates/cc01.png"
    crumbs = [(BRAND, B.page_url("", lang)), ("Ingeniería" if is_es else "Engineering", B.page_url("engineering/", lang)), (C.CODE, canon)]
    ld = B._ld("ScholarlyArticle", title, desc, canon, lang, image=image, date_published=C.DATE, date_modified=C.DATE, crumbs=crumbs)
    head = B.render_head(f"{title} | {BRAND}", desc, PATH, "article", image, rel, rel, ld, lang)
    head = head.replace("</head>", f'  <link rel="stylesheet" href="{rel}/cult-classics.css">\n</head>')

    h = C.HERO
    ht = C.HERO_TRIBUTE
    sketch_item = _media_map()["plate-1974-sketch"]
    pause_label = ("Pausar movimiento", "Reanudar movimiento") if is_es else ("Pause motion", "Resume motion")
    parts = "\n".join(render_part(p, is_es) for p in C.PARTS)
    opening = "\n".join(f'        {bi("p", p["en"], p["es"])}\n        {cite(p["src"])}' for p in C.OPENING)
    closing = "\n".join(f'        {bi("p", p["en"], p["es"])}' for p in C.CLOSING)
    hero_sketch = render_inline_figure(sketch_item, is_es, "cc-hero-sketch", include_id=True)
    honor_roll = f"""        <aside class="cc-honor-roll" aria-label="{a(ht['kicker_es'] if is_es else ht['kicker_en'])}">
          <p class="tp-kicker">{bi("span", ht["kicker_en"], ht["kicker_es"])}</p>
          <dl class="cc-honor-dl">
            <div class="cc-honor-row">{bi("dt", ht["architects_label_en"], ht["architects_label_es"])}{bi("dd", ht["architects_en"], ht["architects_es"])}</div>
            <div class="cc-honor-row">{bi("dt", ht["makers_label_en"], ht["makers_label_es"])}{bi("dd", ht["makers_en"], ht["makers_es"])}</div>
          </dl>
          {cite(ht["src"])}
        </aside>"""

    jumps = [
        ("#relay", "5 Eras", "5 Eras"),
        ("#part-1", "Mk1–Mk8 (1976–2026)", "Mk1–Mk8 (1976–2026)"),
        ("#axle-anatomy", "1:20 ↔ 1:5 Axle", "Eje 1:20 ↔ 1:5"),
        ("#atelier", "2D ↔ 3D Atelier", "Atelier 2D ↔ 3D"),
        ("#engineers-study", "Engineers’ Study", "Estudio de Chasis"),
        ("#ghost-race", "Ghost race", "Carrera fantasma"),
        ("#part-6", "VI · Lab", "VI · Laboratorio"),
        ("#visuals", "Visual Archive (14)", "Archivo Visual (14)"),
        ("#sources", "Sources", "Fuentes"),
    ]
    jump_html = " ".join(f'<a class="tp-essay-jump-pill" href="{jh}" data-en="{a(je)}" data-es="{a(js)}">{t(es_or_en(je, js, is_es))}</a>' for jh, je, js in jumps)
    aria_crumb = "Ruta de navegación" if is_es else "Breadcrumb"
    aria_jump = "Secciones" if is_es else "Sections"
    crossword = B.render_folio_crossword_section("cc01", C.CODE)

    return f"""{head}
<body class="tp-body tp-page-folio cc-page">
{B.render_masthead(rel, "engineering", lang)}
{B.render_contents_dialog(rel, catalog, C.SLUG, active_pillar="engineering")}
{render_parade()}
  <main id="main" class="tp-shell cc-shell" tabindex="-1">
    <nav class="tp-breadcrumb-bar" aria-label="{aria_crumb}">
      <ol class="tp-breadcrumb-list">
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="../../">Informatico.ai</a></li>
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="../../engineering/#cult-classics-eng" data-en="Engineering" data-es="Ingeniería">{"Ingeniería" if is_es else "Engineering"}</a></li>
        <li class="tp-crumb-item" aria-current="page"><span>{t(C.CODE)}</span></li>
      </ol>
    </nav>
    <article class="cc-feature tp-prose" data-folio-id="{a(C.CODE)}">
      <header class="cc-hero tp-hero">
        <div class="cc-hero-grid">
          <div class="cc-hero-copy">
            <p class="tp-kicker">{bi("span", h["kicker_en"], h["kicker_es"])} · {bi("span", h["reading_en"], h["reading_es"])}</p>
            <h1 class="tp-h1 cc-h1" data-en="{a(h['title_en'])}" data-es="{a(h['title_es'])}">{t(h['title_en'])}</h1>
            {bi("p", h["dek_en"], h["dek_es"], "tp-standfirst")}
            {bi("p", C.BRIEF_NOTE["en"], C.BRIEF_NOTE["es"], "cc-brief")}
          </div>
{hero_sketch}
        </div>
{honor_roll}
        <div class="cc-hero-tools">
          <button type="button" class="cc-btn cc-btn-quiet" data-cc-pause aria-pressed="false" data-label-pause="{a(pause_label[0])}" data-label-resume="{a(pause_label[1])}">{t(pause_label[0])}</button>
          <tp-article-audio data-folio="{a(C.CODE)}" data-reading-time="{a(h['reading_es'] if is_es else h['reading_en'])}"></tp-article-audio>
        </div>
      </header>
      <nav class="tp-essay-jump-bar" aria-label="{aria_jump}">{jump_html}</nav>
      <section class="cc-opening" aria-label="{a('Inicio' if is_es else 'Opening')}">
{opening}
      </section>
{render_relay_section(is_es)}
      <div class="cc-chronology-track">
{render_gen_rail(is_es)}
{parts}
      </div>
{render_axle_loupe_section(is_es)}
{render_atelier_section(is_es)}
{render_polar_radar(is_es)}
{render_laps_section(is_es)}
{render_engineers_study_section(is_es)}
{render_lab_section(is_es)}
{render_visual_gallery_section(is_es)}
{crossword}
{render_silent(is_es)}
      <section class="cc-closing" aria-label="{a('Cierre' if is_es else 'Closing')}">
{closing}
      </section>
{render_sources(is_es)}
      {bi("p", C.FOOTER_NOTE["en"], C.FOOTER_NOTE["es"], "cc-footnote")}
    </article>
{B.render_site_footer(rel)}
  </main>
  <script type="module" src="{rel}/modules/main.mjs"></script>
  <script type="module" src="{rel}/modules/cult-classics.mjs"></script>
</body>
</html>
"""


# --------------------------------------------------------------------------------------------- share plate & output

def write_plate() -> None:
    """1200×630 zero-text schematic plate: drafting grid, Mk1/Mk5/Mk8 silhouettes, red rule, tartan check band & differential ring."""
    import build_cross_scale_essays as E  # noqa: E402

    w, h = 1200, 630
    buf = E._make_canvas(w, h, (236, 238, 240))
    for gx in range(80, w, 120):
        E._draw_line(buf, w, h, gx, 40, gx, h - 40, 1, (192, 198, 206), 0.35)
    for gy in range(70, h, 90):
        E._draw_line(buf, w, h, 60, gy, w - 60, gy, 1, (192, 198, 206), 0.35)
    for i in range(0, w, 60):
        E._fill_rect(buf, w, h, i, 520, i + 30, 630, (21, 53, 86), 0.18)
        E._fill_rect(buf, w, h, 0, 540 + (i // 60 % 3) * 24, w, 548 + (i // 60 % 3) * 24, (176, 48, 30), 0.06)
    E._fill_rect(buf, w, h, 80, 108, 620, 114, (176, 48, 30), 1.0)
    E._draw_line(buf, w, h, 80, 128, 420, 128, 2, (21, 53, 86), 0.55)
    for j, k in enumerate((0.0, 0.55, 1.0)):
        ox, oy, s = 120 + j * 335, 250 + j * 36, 1.02
        pts = [(10, 82), (8, 66), (20, 61), (104 - 10 * k, 52 - 4 * k), (132 - 6 * k, 24 + 5 * k),
               (222 + 6 * k, 26 + 7 * k), (280, 50 + 6 * k), (290, 58 + 6 * k), (290, 82), (10, 82)]
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            E._draw_line(buf, w, h, ox + x0 * s, oy + y0 * s, ox + x1 * s, oy + y1 * s, 3, (17, 22, 28), 0.88)
        for cx in (62, 232):
            E._draw_ring(buf, w, h, ox + cx * s, oy + 80 * s, 16, 3, (17, 22, 28), 0.88)
    # Coaxial differential / traction rings upper-right
    E._draw_ring(buf, w, h, 1015, 130, 54, 2, (21, 53, 86), 0.72)
    E._draw_ring(buf, w, h, 1015, 130, 32, 2, (176, 48, 30), 0.85)
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
    print(f"PASS: Built {C.CODE} ({len(written)} pages, EN + ES-MX), plate cc01.png ({digest}), sitemap.xml and llms.txt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
