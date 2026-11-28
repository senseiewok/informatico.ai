#!/usr/bin/env python3
"""Build CC.03, the MINI -> F56 John Cooper Works Hot Chili cult-classic feature (/classics/mini-jcw/ & /es-mx/classics/mini-jcw/).

Content lives in tools/folios/classics/cc03.py and mechanics models live in tools/folios/classics/cc03_mechanics.py.
This module lays out the HTML, generates the schematic SVGs (5-era MINI parade, sketched Brands Hatch parallax
track, F56 JCW side-elevation clamshell Easter egg, Brands Hatch Indy ghost loop, load-transfer & brake-thermal
benches), embeds the 8 verified media plates with zero-jump lightbox, renders the US/Mexico North America comparison
table, and writes src/plates/cc03.png. Behaviour lives in src/modules/cult-classics.mjs (strict CSP, zero inline JS/CSS).

Run on its own: python tools/build_mini_jcw.py   (also called from build_longform_folios.main)
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
from folios.classics import cc03 as C  # noqa: E402
from folios.classics import cc03_mechanics as M  # noqa: E402
from folios.seo_copy import BRAND  # noqa: E402

RESEARCH = ROOT / "src"
PATH = f"classics/{C.SLUG}/"
PLATE = RESEARCH / "plates" / "cc03.png"


def a(s: str) -> str:
    return html.escape(str(s), quote=True)


def t(s: str) -> str:
    return html.escape(str(s), quote=False)


def bi(tag: str, en: str, es: str, cls: str = "", extra: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    x = f" {extra}" if extra else ""
    return f'<{tag}{c}{x} data-en="{a(en)}" data-es="{a(es)}">{t(en)}</{tag}>'


def _media_map() -> dict[str, dict]:
    return {item["id"]: item for item in C.MEDIA}


# --------------------------------------------------------------------------------------------- drawings ----------

def mini_path(k: float) -> str:
    """Schematic Mini two-box side profile in a 300x110 box; k=0 1959 ADO15 ... k=1 F56/F66. Facing left."""
    ground = 94
    nose_x = 56 - 16 * k
    nose_y = 61 - 5 * k
    cowl_x = 104 + 2 * k
    cowl_y = 48 - 4 * k
    roof_front_x = 122 + 4 * k
    roof_y = 22 - 4 * k
    roof_rear_x = 216 + 14 * k
    tail_x = 236 + 12 * k
    tail_y = 54 + 2 * k
    w1, w2 = 82, 206 + 10 * k
    r_arch = 13 + 6 * k
    p = [
        f"M {nose_x:.1f} {ground - 7}",
        f"L {nose_x - 2:.1f} {nose_y + 7:.1f}",
        f"Q {nose_x + 4:.1f} {nose_y - 2:.1f} {cowl_x:.1f} {cowl_y:.1f}",
        f"L {roof_front_x:.1f} {roof_y:.1f}",
        f"L {roof_rear_x:.1f} {roof_y + 1:.1f}",
        f"Q {roof_rear_x + 12:.1f} {roof_y + 2:.1f} {tail_x:.1f} {tail_y:.1f}",
        f"L {tail_x + 2:.1f} {ground - 7}",
        f"L {w2 + r_arch:.1f} {ground - 7}",
        f"A {r_arch:.1f} {r_arch:.1f} 0 0 0 {w2 - r_arch:.1f} {ground - 7}",
        f"L {w1 + r_arch:.1f} {ground - 7}",
        f"A {r_arch:.1f} {r_arch:.1f} 0 0 0 {w1 - r_arch:.1f} {ground - 7}",
        "Z",
    ]
    return " ".join(p)


def wheel(cx: float, cy: float, r: float) -> str:
    spokes = "".join(
        f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx + r * 0.78 * math.cos(i * math.pi / 4):.1f}" '
        f'y2="{cy + r * 0.78 * math.sin(i * math.pi / 4):.1f}"/>'
        for i in range(8)
    )
    return (f'<g class="cc-wheel"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"/>'
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r * 0.56:.1f}"/>{spokes}</g>')


def silhouette(k: float, gen: str, extra_cls: str = "") -> str:
    r = 11.5 + 6.0 * k
    w1, w2 = 82, 206 + 10 * k
    nose_x = 56 - 16 * k
    accent_cls = "cc-car-gold" if k >= 0.6 else "cc-car-red"
    return (f'<svg class="cc-car {extra_cls}" data-gen="{a(gen)}" viewBox="0 0 300 110" width="300" height="110" '
            f'focusable="false" aria-hidden="true"><path class="cc-car-body" d="{mini_path(k)}"/>'
            f'<line class="{accent_cls}" x1="{nose_x:.1f}" y1="{72 - 3 * k:.1f}" x2="{nose_x + 20:.1f}" y2="{72 - 3 * k:.1f}"/>'
            f'{wheel(w1, 94 - r + 4, r)}{wheel(w2, 94 - r + 4, r)}</svg>')


def render_parade() -> str:
    cars = []
    n = max(1, len(C.CARDS) - 1)
    for i, card in enumerate(C.CARDS):
        k = i / n
        extra = "cc-car-tint" if card.get("egg") else ""
        cars.append(f'    <div class="cc-lane cc-lane-{i + 1}">{silhouette(k, card["gen"], extra)}</div>')
    return render_track_layers() + '\n  <div class="cc-parade" aria-hidden="true">\n' + "\n".join(cars) + "\n  </div>"


def render_track_layers() -> str:
    """Fixed, decorative pen-and-ink sketched parallax Brands Hatch Indy background.
    Each layer repeats at y and y+1000 so scroll wrapping is seamless."""
    hills = "M0 240 C 180 185 360 225 560 190 S 940 155 1140 205 S 1420 180 1600 215"
    ribbon = "M -60 980 C 260 850 180 650 560 560 S 1180 510 1290 340 S 1510 110 1660 25"
    edge_left = "M -90 950 C 225 818 148 622 528 532 S 1146 482 1255 314 S 1476 86 1624 2"
    edge_right = "M -25 1010 C 295 882 215 680 595 590 S 1215 540 1326 368 S 1545 138 1696 52"
    kerb = "M 1140 1000 C 1225 900 1350 855 1440 755 S 1545 595 1635 545"
    hatches = " ".join(f"M {120 + i * 95} 1000 L {40 + i * 95} 0" for i in range(16))

    def twice(d: str) -> str:
        return f'<path d="{d}"/><path d="{d}" transform="translate(0 1000)"/>'
    return f"""  <svg class="cc-track cc-track-sketch" viewBox="0 0 1600 1000" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
    <g class="cc-layer cc-layer-far" data-depth="0.06">{twice(hills)}</g>
    <g class="cc-layer cc-layer-hatch" data-depth="0.10">{twice(hatches)}</g>
    <g class="cc-layer cc-layer-ribbon" data-depth="0.18">{twice(ribbon)}</g>
    <g class="cc-layer cc-layer-edge" data-depth="0.18">{twice(edge_left)}{twice(edge_right)}</g>
    <g class="cc-layer cc-layer-centre" data-depth="0.18">{twice(ribbon)}</g>
    <g class="cc-layer cc-layer-kerb" data-depth="0.4">{twice(kerb)}</g>
  </svg>"""


# Schematic Brands Hatch Indy closed loop: Brabham Straight (start/finish flag at 252, 107) -> Paddock Hill -> Druids -> Graham Hill -> Cooper Straight -> Clearways -> Brabham Straight
BRANDS_INDY_LOOP = (
    "M 252 107 L 386 92 C 474 82 528 112 536 154 C 544 196 510 226 462 232 "
    "L 420 238 C 384 244 374 270 398 294 L 440 330 C 464 352 454 398 386 392 "
    "L 158 366 C 98 358 76 312 102 256 C 122 212 104 176 92 148 C 84 130 98 124 118 122 L 252 107 Z"
)


def render_laps_section(is_es: bool) -> str:
    x = C.LAPS_TEXT
    by_id = _media_map()
    fastest = min(lap[5] for lap in C.LAPS)
    dots, legend, rows = [], [], []
    for i, (_rid, era, car, year, ts, secs, driver, listed_mph, cfg, _skey) in enumerate(C.LAPS):
        hue = ("cc-dot-a", "cc-dot-b", "cc-dot-c", "cc-dot-d", "cc-dot-e", "cc-dot-f", "cc-dot-g", "cc-dot-h")[i]
        nolen = "" if cfg else " cc-ghost-nolen"
        dots.append(f'<g class="cc-ghost {hue}{nolen}" data-secs="{secs}"><circle r="9" cx="252" cy="107"/>'
                    f'<text x="252" y="110.5" text-anchor="middle">{i + 1}</text></g>')
        legend.append(f'<li class="{hue}{nolen}"><span class="cc-ghost-key" aria-hidden="true">{i + 1}</span> {t(era)} · {t(car)} ({year})</li>')
        cfg_cell = cfg if cfg else ("en blanco" if is_es else "blank")
        mph_cell = listed_mph if listed_mph != "not stated" else ("no se indica" if is_es else "not stated")
        rows.append(f'<tr><td>{i + 1}</td><td>{t(era)}</td><th scope="row">{t(car)}</th><td>{year}</td>'
                    f'<td class="cc-num">{t(ts)}</td><td>{t(driver)}</td><td class="cc-num">{t(mph_cell)}</td><td>{t(cfg_cell)}</td></tr>')
    cols = [("#", "#"), ("Era", "Época"), ("Class record", "Récord de categoría"), ("Year", "Año"),
            ("Lap", "Vuelta"), ("Driver", "Piloto"), ("Listed speed", "Velocidad citada"), ("Length", "Longitud")]
    head = "".join(bi("th", en, es, "", 'scope="col"') for en, es in cols)
    start = ("Iniciar carrera", "Repetir") if is_es else ("Start the race", "Run it again")
    svg_title = "Contorno esquemático de Brands Hatch Indy con ocho puntos de récord" if is_es else "Schematic Brands Hatch Indy circuit loop with eight lap-record dots"
    return f"""      <section class="cc-observatory cc-laps" id="ghost-race" aria-labelledby="cc-laps-h">
        {bi("h2", x["title_en"], x["title_es"], "cc-h2", 'id="cc-laps-h"')}
        {bi("p", x["intro_en"], x["intro_es"], "cc-lede cc-dropcap")}
        <div class="cc-bench cc-race" data-cc-race data-fastest="{fastest}" data-compress="10" data-decimals="3" data-gap-decimals="2">
          <svg class="cc-loop-svg" viewBox="0 0 620 460" width="620" height="460" role="img" aria-labelledby="cc-loop-title">
            <title id="cc-loop-title">{t(svg_title)}</title>
            <path class="cc-loop-tar" d="{BRANDS_INDY_LOOP}"/>
            <path class="cc-loop-line" id="cc-loop-path" d="{BRANDS_INDY_LOOP}"/>
            <line class="cc-loop-flag" x1="250" y1="89" x2="254" y2="125"/>
            <text class="cc-loop-corner" x="250" y="76" text-anchor="middle">Brabham Straight</text>
            <text class="cc-loop-corner" x="546" y="138" text-anchor="start">Paddock Hill</text>
            <text class="cc-loop-corner" x="492" y="250" text-anchor="start">Druids</text>
            <text class="cc-loop-corner" x="358" y="302" text-anchor="end">Graham Hill</text>
            <text class="cc-loop-corner" x="275" y="406" text-anchor="middle">Cooper Straight</text>
            <text class="cc-loop-corner" x="78" y="294" text-anchor="end">Clearways</text>
            {''.join(dots)}
          </svg>
          <div class="cc-controls">
            <button type="button" class="cc-btn" data-cc-race-start data-label-start="{a(start[0])}" data-label-again="{a(start[1])}">{t(start[0])}</button>
            <ol class="cc-ghost-legend">{''.join(legend)}</ol>
            <p class="cc-readout" aria-live="polite" data-en="Eight cars on the Brabham grid." data-es="Ocho autos en la parrilla de Brabham.">Eight cars on the Brabham grid.</p>
          </div>
        </div>
        {bi("p", x["loop_en"], x["loop_es"], "cc-small")}
        <div class="cc-table-wrap"><table class="cc-table cc-lap-table"><thead><tr>{head}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>
        {cite(["mini7-records", "mc-cooper-records", "mc-jcw-records", "brands-hatch"])}
        {bi("p", x["read_en"], x["read_es"], "cc-lede")}
        <div class="cc-science">
          {bi("p", x["caveat_en"], x["caveat_es"])}
          {cite(["mini7-club", "mc-cooper-class", "mc-jcw-class"])}
        </div>
        <div class="cc-inline-media">{render_media_figure(by_id["photo-2022-brands"], is_es)}</div>
      </section>"""


def render_load_svg() -> str:
    return """<svg class="cc-load-svg" viewBox="0 0 360 220" width="360" height="220" role="img" aria-labelledby="cc-load-title">
          <title id="cc-load-title">Front view of axle lateral load transfer and unequal vertical tire loads in a corner</title>
          <defs>
            <marker id="cc-arrow-gold" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker>
          </defs>
          <line class="cc-qc-road" x1="24" y1="184" x2="336" y2="184"/>
          <rect class="cc-tyre" x="62" y="140" width="30" height="44" rx="5"/>
          <rect class="cc-tyre" x="268" y="140" width="30" height="44" rx="5"/>
          <rect class="cc-load-body" x="76" y="76" width="208" height="62" rx="10" transform="rotate(0 180 120)"/>
          <circle class="cc-load-cg" cx="180" cy="124" r="6"/>
          <rect class="cc-load-bar-in" x="40" y="122" width="14" height="48" rx="2"/>
          <rect class="cc-load-bar-out" x="306" y="122" width="14" height="48" rx="2"/>
          <line class="cc-load-fy cc-load-fy-in" x1="77" y1="198" x2="112" y2="198"/>
          <line class="cc-load-fy cc-load-fy-out" x1="283" y1="198" x2="330" y2="198"/>
          <text class="cc-svg-label" x="47" y="66" text-anchor="middle" data-en="inside" data-es="interior">inside</text>
          <text class="cc-svg-label" x="313" y="66" text-anchor="middle" data-en="outside" data-es="exterior">outside</text>
          <text class="cc-svg-label" x="180" y="156" text-anchor="middle" data-en="CG · track" data-es="CG · vía">CG · track</text>
        </svg>"""


def render_load_section(is_es: bool) -> str:
    m = M.LOAD_MODEL
    g = m["geometries"]
    radios = "".join(
        f'<label class="cc-mode"><input type="radio" name="cc-load-mode" value="{k}"{" checked" if k == "f56" else ""}> {bi("span", g[k][0], g[k][1])}</label>'
        for k in ("tall", "f56", "kart")
    )
    legend = "Geometría de vía" if is_es else "Track geometry"
    ay_label = "Aceleración lateral" if is_es else "Lateral acceleration"
    return f"""      <section class="cc-observatory" id="load-transfer" aria-labelledby="cc-load-h">
        {bi("h2", "The cornering stance bench", "El banco de transferencia lateral", "cc-h2", 'id="cc-load-h"')}
        {bi("p", C.LOAD_SCIENCE["intro_en"], C.LOAD_SCIENCE["intro_es"], "cc-lede")}
        <div class="cc-bench" data-cc-load data-maxle="{m['m_axle_kg']}" data-g="{m['g']}" data-mu0="{m['mu_0']}" data-kload="{m['k_load']}" data-htall="{g['tall'][2]}" data-ttall="{g['tall'][3]}" data-hf56="{g['f56'][2]}" data-tf56="{g['f56'][3]}" data-hkart="{g['kart'][2]}" data-tkart="{g['kart'][3]}">
          {render_load_svg()}
          <div class="cc-controls">
            <fieldset class="cc-modes"><legend>{t(legend)}</legend>{radios}</fieldset>
            <label class="cc-range-label" for="cc-ay-range">{t(ay_label)}</label>
            <input id="cc-ay-range" class="cc-range" type="range" min="0" max="100" value="85" step="1" aria-valuetext="0.85 g">
            <p class="cc-readout" aria-live="polite" data-en="0.85 g cornering stance." data-es="0.85 g en apoyo lateral.">0.85 g cornering stance.</p>
          </div>
        </div>
        {bi("p", C.LOAD_SCIENCE["caption_en"], C.LOAD_SCIENCE["caption_es"], "cc-small")}
        {cite(["wiki-hatch"])}
        <div class="cc-science">
          {bi("p", C.LOAD_SCIENCE["science_en"], C.LOAD_SCIENCE["science_es"])}
          {cite(["ricco2020"])}
        </div>
      </section>"""


def render_brake_svg() -> str:
    bolts = "".join(
        f'<circle cx="{174 + 20 * math.cos(i * math.pi / 2.5):.1f}" cy="{105 + 20 * math.sin(i * math.pi / 2.5):.1f}" r="3.5" fill="var(--tp-slate)"/>'
        for i in range(5)
    )
    return f"""<svg class="cc-brake-svg" viewBox="0 0 360 210" width="360" height="210" role="img" aria-labelledby="cc-brake-title">
          <title id="cc-brake-title">Front vented brake rotor, four-piston caliper and cooling-duct airflow</title>
          <circle class="cc-brake-rotor" cx="174" cy="105" r="64"/>
          <circle class="cc-brake-glow" cx="174" cy="105" r="60"/>
          <circle cx="174" cy="105" r="30" fill="var(--tp-vellum)" stroke="var(--cc-ink)" stroke-width="1.5"/>
          {bolts}
          <path class="cc-brake-caliper" d="M 216 52 A 68 68 0 0 1 238 134 L 218 128 A 48 48 0 0 0 200 68 Z"/>
          <path class="cc-brake-air" d="M 20 85 Q 68 82 106 92"/>
          <path class="cc-brake-air" d="M 20 108 Q 68 108 104 108"/>
          <path class="cc-brake-air" d="M 20 131 Q 68 132 106 122"/>
          <text class="cc-svg-label" x="16" y="64" data-en="duct airflow" data-es="flujo del ducto">duct airflow</text>
          <text class="cc-svg-label" x="248" y="96" data-en="4-pot caliper" data-es="cáliper 4 pistones">4-pot caliper</text>
        </svg>"""


def render_brake_section(is_es: bool) -> str:
    b = M.BRAKE_MODEL
    rotors = b["rotors"]
    radios = "".join(
        f'<label class="cc-mode"><input type="radio" name="cc-brake-mode" value="{k}"{" checked" if k == "brembo" else ""}> {bi("span", rotors[k][0], rotors[k][1])}</label>'
        for k in ("small", "mid", "brembo")
    )
    legend = "Masa térmica del rotor" if is_es else "Rotor thermal mass"
    v_label = "Velocidad de entrada (hacia 80 km/h)" if is_es else "Entry speed (braking to 80 km/h)"
    return f"""      <section class="cc-observatory" id="brake-thermal" aria-labelledby="cc-brake-h">
        {bi("h2", "The Paddock Hill brake bench", "El banco térmico de frenos", "cc-h2", 'id="cc-brake-h"')}
        {bi("p", C.BRAKE_SCIENCE["intro_en"], C.BRAKE_SCIENCE["intro_es"], "cc-lede")}
        <div class="cc-bench" data-cc-brake data-mcar="{b['m_car_kg']}" data-v2="{b['v2_kmh']}" data-fshare="{b['front_share']}" data-cp="{b['cp_j_kgk']}" data-tamb="{b['t_amb_c']}" data-msmall="{rotors['small'][2]}" data-mmid="{rotors['mid'][2]}" data-mbrembo="{rotors['brembo'][2]}">
          {render_brake_svg()}
          <div class="cc-controls">
            <fieldset class="cc-modes"><legend>{t(legend)}</legend>{radios}</fieldset>
            <label class="cc-range-label" for="cc-brake-range">{t(v_label)}</label>
            <input id="cc-brake-range" class="cc-range" type="range" min="{b['v1_min_kmh']:.0f}" max="{b['v1_max_kmh']:.0f}" value="{b['v1_start_kmh']:.0f}" step="2" aria-valuetext="{b['v1_start_kmh']:.0f} km/h">
            <p class="cc-readout" aria-live="polite" data-en="Single-stop rotor heating." data-es="Calentamiento en una sola frenada.">Single-stop rotor heating.</p>
          </div>
        </div>
        {bi("p", C.BRAKE_SCIENCE["caption_en"], C.BRAKE_SCIENCE["caption_es"], "cc-small")}
        {cite(["wiki-hatch"])}
        <div class="cc-science">
          {bi("p", C.BRAKE_SCIENCE["science_en"], C.BRAKE_SCIENCE["science_es"])}
          {cite(["adamowicz2011"])}
        </div>
      </section>"""


# --------------------------------------------------------------------------------------------- page ----------

def cite(keys: list[str]) -> str:
    if not keys:
        return ""
    return f'<p class="cc-cite">{" ".join(stamp(k) for k in keys)}</p>'


def stamp(key: str) -> str:
    s = C.SOURCES[key]
    return bi("a", s["short"], s.get("short_es", s["short"]), f"cc-stamp cc-stamp-{s['kind']}", f'href="#src-{a(key)}"')


def jcw_rim(cx: float, cy: float) -> str:
    """10-Y-spoke gold cross-spoke style rim with a red front 4-piston caliper arc (side schematic)."""
    spokes = "".join(
        f'<line x1="{cx + 4.0 * math.cos(ang + d):.1f}" y1="{cy + 4.0 * math.sin(ang + d):.1f}" '
        f'x2="{cx + 14.8 * math.cos(ang + d * 2.2):.1f}" y2="{cy + 14.8 * math.sin(ang + d * 2.2):.1f}"/>'
        for ang in (i * 2 * math.pi / 5 for i in range(5)) for d in (-0.22, 0.22)
    )
    return (f'<g class="cc-egg-wheel cc-egg-wheel-gold"><circle class="cc-egg-tyre" cx="{cx}" cy="{cy}" r="19.6"/>'
            f'<circle class="cc-egg-rim-gold" cx="{cx}" cy="{cy}" r="15.2"/>'
            f'<path class="cc-egg-caliper" d="M {cx - 10} {cy - 7} A 12 12 0 0 1 {cx + 2} {cy - 12}"/>'
            f'<g class="cc-wheel">{spokes}<circle cx="{cx}" cy="{cy}" r="3.6"/></g></g>')


def mini_jcw_profile() -> str:
    """Schematic F56 MINI John Cooper Works 3-door side elevation, facing left."""
    body = (
        "M 40 89 L 38 78 Q 37 64 42 56 L 48 52 Q 74 46 106 44 L 126 18 L 228 18 "
        "L 246 13 L 249 19 L 238 24 Q 246 38 248 58 L 248 82 L 242 89 "
        "L 234 89 A 18.5 18.5 0 0 0 198 89 L 100 89 A 18.5 18.5 0 0 0 64 89 Z"
    )
    glass = "M 114 43 L 130 22 L 222 22 L 236 40 Q 176 42 114 43 Z"
    return f"""<rect class="cc-egg-glow" x="48" y="47" width="58" height="14" rx="5"/>
                <path class="cc-egg-body" d="{body}"/>
                <path class="cc-egg-glass" d="{glass}"/>
                <path class="cc-egg-roof-pillar" d="M 107 43 L 125 18 L 132 18 L 116 43 Z"/>
                <rect class="cc-egg-roof-pillar" x="172" y="21" width="5.5" height="20"/>
                <path class="cc-egg-roof-pillar" d="M 218 21 L 230 21 L 242 40 L 226 41 Z"/>
                <path class="cc-egg-shoulder" d="M 48 56 Q 146 49 245 52"/>
                <path class="cc-egg-skirt" d="M 101 85 L 197 85"/>
                <ellipse class="cc-egg-light" cx="55" cy="56" rx="9" ry="5.5" transform="rotate(-14 55 56)"/>
                <line class="cc-egg-gold" x1="39" y1="67" x2="57" y2="67"/>
                <path class="cc-egg-grille" d="M 39 73 L 55 72 M 39 78 L 55 77 M 40 83 L 56 82"/>
                <path class="cc-egg-taillight" d="M 239 48 L 248 53 L 248 64 L 239 61 Z"/>
                <path class="cc-egg-exhaust" d="M 234 88 L 243 88"/>
                <g class="cc-egg-hood"><path d="M 42 56 Q 66 49 76 46 L 85 44 L 87 46 L 106 44 L 106 48 Q 72 51 43 60 Z"/></g>
                {jcw_rim(82, 79)}{jcw_rim(216, 79)}"""


def linked_caption(item: dict, is_es: bool) -> str:
    out = t(item["caption_es"] if is_es else item["caption_en"])
    for label, url in item.get("links", []):
        out = out.replace(t(label), f'<a href="{a(url)}" rel="noopener noreferrer">{t(label)}</a>', 1)
    return out


def render_media_figure(item: dict, is_es: bool, extra_cls: str = "", in_gallery: bool = False) -> str:
    is_photo = item["kind"] == "photo"
    badge_en = f"{'Archival Photo' if is_photo else 'Conceptual Study'} · {item['era']}"
    badge_es = f"{'Foto de Archivo' if is_photo else 'Estudio Conceptual'} · {item['era']}"
    badge_cls = "cc-media-badge cc-media-badge-photo" if is_photo else "cc-media-badge cc-media-badge-render"
    alt_txt = item["alt_es"] if is_es else item["alt_en"]
    fig_id = "" if in_gallery else f' id="fig-{a(item["id"])}"'
    zoom_attr = (
        f' data-cc-open-media="{a(item["id"])}"'
        f' data-alt-en="{a(item["alt_en"])}" data-alt-es="{a(item["alt_es"])}"'
        f' data-cap-en="{a(item["caption_en"])}" data-cap-es="{a(item["caption_es"])}"'
        f' data-badge-en="{a(badge_en)}" data-badge-es="{a(badge_es)}"'
    )
    media_tag = f' data-cc-media-id="{a(item["id"])}"' if in_gallery else ""
    cls_str = f"cc-media-card{' ' + extra_cls if extra_cls else ''}"
    src_line = cite(item["src"]) if item.get("src") else ""
    return f"""        <figure class="{cls_str}"{media_tag}{fig_id}>
          <div class="cc-media-head">
            <span class="{badge_cls}" data-en="{a(badge_en)}" data-es="{a(badge_es)}">{t(badge_es if is_es else badge_en)}</span>
            <button type="button" class="cc-btn cc-btn-quiet cc-zoom-btn"{zoom_attr} data-en="Inspect plate" data-es="Ampliar lámina">{t('Ampliar lámina' if is_es else 'Inspect plate')}</button>
          </div>
          <div class="cc-media-frame" data-cc-open-media-frame="{a(item['id'])}">
            <img src="../../{a(item['image'])}" width="{item['width']}" height="{item['height']}" loading="lazy" decoding="async" alt="{a(alt_txt)}" data-alt-en="{a(item['alt_en'])}" data-alt-es="{a(item['alt_es'])}">
          </div>
          <figcaption>{linked_caption(item, is_es)}</figcaption>
          {src_line}
        </figure>"""


def render_egg(is_es: bool) -> str:
    e = C.EGG
    hint_en, hint_es = "There is one more MINI under this clamshell.", "Hay un MINI más debajo de este cofre."
    car = f"""<svg class="cc-egg-car cc-egg-mini" viewBox="0 0 300 110" width="200" height="73" aria-hidden="true" focusable="false">
                {mini_jcw_profile()}
              </svg>"""
    figs = [render_media_figure(C.EGG, is_es, "cc-egg-photo"), render_media_figure(C.EGG_SKETCH, is_es, "cc-egg-photo")]
    return f"""          <div class="cc-egg">
            <button type="button" class="cc-egg-btn" aria-expanded="false" aria-controls="cc-egg-panel" data-label-open="{a(e['button_es'] if is_es else e['button_en'])}" data-label-close="{a(e['close_es'] if is_es else e['close_en'])}">
              {car}
              <span class="cc-egg-copy">{bi("span", hint_en, hint_es, "cc-egg-hint")}{bi("span", e["button_en"], e["button_es"], "cc-egg-label")}</span>
            </button>
            <div class="cc-egg-panel cc-egg-panel-duo" id="cc-egg-panel" hidden>
{chr(10).join(figs)}
            </div>
          </div>
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
    body_and_plate = f"""          {bi("p", card["body_en"], card["body_es"], "cc-card-body")}
          <div class="cc-plate" role="group" aria-label="{a('Placa de especificaciones' if is_es else 'Spec plate')} {a(card['gen'])}">
            <dl>{''.join(rows)}</dl>
            <p class="cc-plate-foot" data-en="Read {a(C.ACCESSED)}" data-es="Consultado {a(C.ACCESSED)}">Read {t(C.ACCESSED)}</p>
          </div>"""
    if card.get("photo"):
        inner = f"""          <div class="cc-card-split">
            <div class="cc-card-main">
{body_and_plate}
            </div>
{render_media_figure(by_id[card["photo"]], is_es, "cc-gen-figure")}
          </div>"""
    else:
        inner = f"""{body_and_plate}
{egg}"""
    return f"""        <article class="cc-card" id="{a(card['id'])}" data-gen="{a(card['gen'])}">
          <header class="cc-card-head">
            <p class="cc-card-gen"><span>{t(card['gen'])}</span> <span class="cc-card-years">{t(card['years'])}</span></p>
            {bi("h3", card["move_en"], card["move_es"], "cc-card-move")}
          </header>
{inner}
        </article>"""


def render_north_america(is_es: bool) -> str:
    na = C.NORTH_AMERICA
    col, row = 'scope="col"', 'scope="row"'
    head = "".join(bi("th", en, es, "", col) for en, es in zip(na["head_en"], na["head_es"]))
    rows = "".join(
        "<tr>" + bi("th", r[0], r[1], "", row) + bi("td", r[2], r[3]) + bi("td", r[4], r[5]) + bi("td", r[6], r[7]) + "</tr>"
        for r in na["rows"]
    )
    return f"""          <aside class="cc-interlude" id="north-america-spec" aria-labelledby="cc-int-na">
            {bi("h3", na["title_en"], na["title_es"], "cc-int-h", 'id="cc-int-na"')}
            {bi("p", na["intro_en"], na["intro_es"])}
            <div class="cc-table-wrap"><table class="cc-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
            {bi("p", na["note_en"], na["note_es"], "cc-small")}
            {cite(na["src"])}
          </aside>"""


def render_interlude(kind: str, is_es: bool) -> str:
    by_id = _media_map()
    if kind == "ado15-details":
        d = C.ADO15_DETAILS
        items = "".join(f'<li>{bi("span", en, es)}</li>' for en, es in d["items"])
        photo_html = f'<div class="cc-inline-media">{render_media_figure(by_id[d["photo"]], is_es)}</div>' if d.get("photo") else ""
        return f"""          <aside class="cc-interlude" aria-labelledby="cc-int-ado15">
            {bi("h3", d["title_en"], d["title_es"], "cc-int-h", 'id="cc-int-ado15"')}
            <ul class="cc-ledger-list">{items}</ul>
            {cite(d["src"])}
            {photo_html}
          </aside>"""
    if kind == "induction":
        b = C.INDUCTION
        col, row = 'scope="col"', 'scope="row"'
        head = "".join(bi("th", en, es, "", col) for en, es in zip(b["head_en"], b["head_es"]))
        rows = "".join(
            "<tr>" + bi("th", r[0], r[1], "", row) + bi("td", r[2], r[3]) + bi("td", r[4], r[5]) + bi("td", r[6], r[7]) + "</tr>"
            for r in b["rows"]
        )
        return f"""          <aside class="cc-interlude" aria-labelledby="cc-int-ind">
            {bi("h3", b["title_en"], b["title_es"], "cc-int-h", 'id="cc-int-ind"')}
            <div class="cc-table-wrap"><table class="cc-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
            {bi("p", b["note_en"], b["note_es"], "cc-small")}
            {cite(b["src"])}
          </aside>"""
    if kind == "f56-anatomy":
        d = C.F56_ANATOMY
        rows = "".join(f'<div class="cc-anat-row">{bi("dt", r[0], r[1])}{bi("dd", r[2], r[3])}</div>' for r in d["items"])
        anat = f"""          <aside class="cc-interlude cc-anatomy" aria-labelledby="cc-int-anat">
            {bi("h3", d["title_en"], d["title_es"], "cc-int-h", 'id="cc-int-anat"')}
            <dl>{rows}</dl>
            {cite(d["src"])}
          </aside>"""
        return anat + "\n" + render_north_america(is_es)
    return ""


def render_part(part: dict, is_es: bool) -> str:
    cards = {c["id"]: c for c in C.CARDS}
    opener = []
    for i, p in enumerate(part["opener"]):
        cls = "cc-dropcap" if i == 0 else ""
        opener.append(f'          {bi("p", p["en"], p["es"], cls)}\n          {cite(p["src"])}')
        if i == 0:
            opener.append("          " + bi("p", part["pull_en"], part["pull_es"], "cc-pull"))
    body = "\n".join(render_card(cards[cid], is_es) for cid in part["cards"])
    extra = ""
    if part["id"] == "part-3":
        extra = render_load_section(is_es) + "\n" + render_brake_section(is_es)
    return f"""      <section class="cc-part" id="{a(part['id'])}" aria-labelledby="{a(part['id'])}-h">
        <header class="cc-part-head">
          <p class="cc-part-num" aria-hidden="true">{t(part['numeral'])}</p>
          <h2 class="cc-h2 cc-part-title" id="{a(part['id'])}-h"><span data-en="Part {a(part['numeral'])}" data-es="Parte {a(part['numeral'])}">Part {t(part['numeral'])}</span> · {bi("span", part["title_en"], part["title_es"])}</h2>
          <p class="cc-part-years">{t(part['years'])}</p>
        </header>
        <div class="cc-part-opener">
{chr(10).join(opener)}
        </div>
{body}
{render_interlude(part["interlude"], is_es)}
{extra}
      </section>"""


def _n(x: float) -> str:
    return f"{round(x):,} N"


def render_lab_section(is_es: bool) -> str:
    """Part V · Mechanics Lab: computed tables from cc03_mechanics (checked by skills/classics/cc03)."""
    L = C.LAB
    lm = M.LOAD_MODEL
    ay = lm["ay_start_g"]
    load_rows = []
    for key in ("tall", "f56", "kart"):
        en, es, h_cg, trk = lm["geometries"][key]
        r = M.axle_cornering(ay, key)
        load_rows.append(
            f'<tr data-load-mode="{key}">{bi("th", en, es, "", "scope=\"row\"")}'
            f'<td class="cc-num">{h_cg:.2f} m / {trk:.3f} m</td>'
            f'<td class="cc-num">{_n(r["dfz"])}</td>'
            f'<td class="cc-num">{_n(r["fz_in"])}</td>'
            f'<td class="cc-num">{_n(r["fz_out"])}</td>'
            f'<td class="cc-num">{_n(r["fy_total"])}</td>'
            f'<td class="cc-num cc-strong">{_n(r["grip_loss"])}</td></tr>'
        )
    lcols = [("Stance", "Postura"), ("h_cg / Track", "h_cg / Vía"), ("Transfer ΔF_z", "Transferencia ΔF_z"),
             ("Inside F_z", "Carga int."), ("Outside F_z", "Carga ext."), ("Axle grip F_y", "Agarre eje F_y"),
             ("Loss (DERIVED)", "Pérdida (DERIVADO)")]
    lhead = "".join(bi("th", en, es, "", 'scope="col"') for en, es in lcols)
    load_in_en = (f"Inputs: front-axle mass {round(lm['m_axle_kg'])} kg (MODEL), a_y {ay:.2f} g (MODEL), "
                  f"mu_0 {lm['mu_0']} (MODEL), load sensitivity k {lm['k_load']:.1e} N^-1 (MODEL), F56 track 1.485 m (BMW dimensions).")
    load_in_es = (f"Entradas: masa eje delantero {round(lm['m_axle_kg'])} kg (MODELO), a_y {ay:.2f} g (MODELO), "
                  f"mu_0 {lm['mu_0']} (MODELO), sensibilidad k {lm['k_load']:.1e} N^-1 (MODELO), vía F56 1.485 m (dimensiones BMW).")

    bm = M.BRAKE_MODEL
    v1 = bm["v1_start_kmh"]
    brake_rows = []
    for key in ("small", "mid", "brembo"):
        en, es, m_disc = bm["rotors"][key]
        r = M.brake_stop_rise(v1, key)
        brake_rows.append(
            f'<tr data-brake-mode="{key}">{bi("th", en, es, "", "scope=\"row\"")}'
            f'<td class="cc-num">{m_disc:.1f} kg</td>'
            f'<td class="cc-num">{r["e_disc_kj"]:.1f} kJ</td>'
            f'<td class="cc-num cc-strong">+{r["dt_c"]:.1f} °C</td>'
            f'<td class="cc-num">{r["t_peak_c"]:.1f} °C</td></tr>'
        )
    bcols = [("Front rotor class", "Clase de rotor delantero"), ("Disc mass", "Masa disco"),
             ("Energy / disc", "Energía / disco"), ("ΔT (DERIVED)", "ΔT (DERIVADO)"), ("Peak (25 °C base)", "Pico (base 25 °C)")]
    bhead = "".join(bi("th", en, es, "", 'scope="col"') for en, es in bcols)
    brake_in_en = (f"Inputs: car mass {round(bm['m_car_kg']):,} kg (F56 JCW auto), stop {v1:.0f} to {bm['v2_kmh']:.0f} km/h (MODEL), "
                   f"front braking share {bm['front_share']:.2f} (MODEL), cast-iron c_p {round(bm['cp_j_kgk'])} J/(kg·K) (MODEL).")
    brake_in_es = (f"Entradas: masa auto {round(bm['m_car_kg']):,} kg (F56 JCW auto), frenada {v1:.0f} a {bm['v2_kmh']:.0f} km/h (MODELO), "
                   f"reparto delantero {bm['front_share']:.2f} (MODELO), c_p hierro {round(bm['cp_j_kgk'])} J/(kg·K) (MODELO).")

    lap_rows = []
    for rid, era, car, year, ts, secs, _drv, _mph, cfg, _sk in C.LAPS:
        if not cfg:
            continue
        lap_rows.append(
            f'<tr data-lap-row="{a(rid)}"><td>{t(era)}</td><th scope="row">{t(car)}</th><td>{year}</td>'
            f'<td class="cc-num">{t(ts)}</td>'
            f'<td class="cc-num cc-strong" data-lap-kmh="{a(rid)}">{M.indy_speed_kmh(secs):.1f} km/h</td>'
            f'<td class="cc-num" data-lap-mph="{a(rid)}">{M.indy_speed_mph(secs):.2f} mph</td></tr>'
        )
    sp_cols = [("Era", "Época"), ("Class record", "Récord"), ("Year", "Año"), ("Lap", "Vuelta"),
               ("Average (DERIVED)", "Promedio (DERIVADO)"), ("mph (DERIVED)", "mph (DERIVADO)")]
    sp_head = "".join(bi("th", en, es, "", 'scope="col"') for en, es in sp_cols)

    pw = M.power_ratings()
    pcols = [("Standard", "Estándar"), ("Market sheets", "Fichas"), ("Power (from 170.0 kW)", "Potencia (desde 170.0 kW)"),
             ("F56 torque (320 Nm)", "Par F56 (320 Nm)"), ("F66 torque (380 Nm)", "Par F66 (380 Nm)")]
    phead = "".join(bi("th", en, es, "", 'scope="col"') for en, es in pcols)
    prows = (
        f'<tr>{bi("th", "SAE mechanical (745.70 W/hp)", "SAE mecánico (745.70 W/hp)", "", "scope=\"row\"")}'
        f'<td>US / North America</td>'
        f'<td class="cc-num cc-strong" data-unit-hp="{pw["hp_sae"]:.2f}">{pw["hp_sae"]:.2f} hp (228 hp)</td>'
        f'<td class="cc-num" data-unit-lbft-f56="{pw["lbft_f56"]:.1f}">{pw["lbft_f56"]:.1f} lb-ft (236 lb-ft)</td>'
        f'<td class="cc-num" data-unit-lbft-f66="{pw["lbft_f66"]:.1f}">{pw["lbft_f66"]:.1f} lb-ft (280 lb-ft)</td></tr>'
        f'<tr>{bi("th", "DIN metric PS (735.50 W/PS)", "Métrico DIN PS (735.50 W/PS)", "", "scope=\"row\"")}'
        f'<td>Mexico &amp; Europe</td>'
        f'<td class="cc-num cc-strong" data-unit-ps="{pw["ps_metric"]:.2f}">{pw["ps_metric"]:.2f} PS (231 PS)</td>'
        f'<td class="cc-num">320 Nm</td>'
        f'<td class="cc-num">380 Nm</td></tr>'
    )

    return f"""      <section class="cc-part cc-lab" id="part-5" aria-labelledby="part-5-h">
        <header class="cc-part-head">
          <p class="cc-part-num" aria-hidden="true">V</p>
          <h2 class="cc-h2 cc-part-title" id="part-5-h">{bi("span", "Part V", "Parte V")} · {bi("span", L["title_en"], L["title_es"])}</h2>
          <p class="cc-part-years" data-en="Model · Derived · Checked by script" data-es="Modelo · Derivado · Comprobado por script">Model · Derived · Checked by script</p>
        </header>
        {bi("p", L["intro_en"], L["intro_es"], "cc-lede cc-dropcap")}
        <article class="cc-lab-block" id="lab-load">
          {bi("h3", L["load_h_en"], L["load_h_es"])}
          {bi("p", L["load_p_en"], L["load_p_es"])}
          <p class="cc-eq"><code>ΔF_z = m_axle · g · a_y · h_cg / t_track</code><br><code>F_y,loss = 2 · F_y(F_z0) − (F_y(F_z0 − ΔF_z) + F_y(F_z0 + ΔF_z)) = 2 · k · (ΔF_z)²</code></p>
          <div class="cc-table-wrap"><table class="cc-table cc-lab-load"><thead><tr>{lhead}</tr></thead><tbody>{''.join(load_rows)}</tbody></table></div>
          {bi("p", load_in_en, load_in_es, "cc-small")}
          {cite(["ricco2020", "wiki-hatch"])}
        </article>
        <article class="cc-lab-block" id="lab-brake">
          {bi("h3", L["brake_h_en"], L["brake_h_es"])}
          {bi("p", L["brake_p_en"], L["brake_p_es"])}
          <p class="cc-eq"><code>E_disc = ½ · f_front · (½ · m_car · (v₁² − v₂²))</code><br><code>ΔT_adiabatic = E_disc / (m_disc · c_p)</code></p>
          <div class="cc-table-wrap"><table class="cc-table cc-lab-brake"><thead><tr>{bhead}</tr></thead><tbody>{''.join(brake_rows)}</tbody></table></div>
          {bi("p", brake_in_en, brake_in_es, "cc-small")}
          {cite(["adamowicz2011", "wiki-hatch"])}
        </article>
        <article class="cc-lab-block" id="lab-laps">
          {bi("h3", L["laps_h_en"], L["laps_h_es"])}
          {bi("p", L["laps_p_en"], L["laps_p_es"])}
          <p class="cc-eq"><code>L = 1.208 mi × 1,609.344 m/mi = 1,944.09 m · v̄ = L ÷ t_lap</code></p>
          <div class="cc-table-wrap"><table class="cc-table cc-lab-laps"><thead><tr>{sp_head}</tr></thead><tbody>{''.join(lap_rows)}</tbody></table></div>
          {cite(["mini7-records", "brands-hatch"])}
        </article>
        <article class="cc-lab-block" id="lab-power">
          {bi("h3", L["power_h_en"], L["power_h_es"])}
          {bi("p", L["power_p_en"], L["power_p_es"])}
          <p class="cc-eq"><code>hp_SAE = 170,000 W ÷ 745.70 W/hp · PS_DIN = 170,000 W ÷ 735.50 W/PS · lb-ft = N·m ÷ 1.3558</code></p>
          <div class="cc-table-wrap"><table class="cc-table cc-lab-power"><thead><tr>{phead}</tr></thead><tbody>{prows}</tbody></table></div>
          {cite(["wiki-hp", "miniusa-jcw", "bmw-jcw-2024"])}
        </article>
        <aside class="cc-interlude cc-verify-box" aria-labelledby="cc-verify-h">
          {bi("h3", L["verify_h_en"], L["verify_h_es"], "cc-int-h", 'id="cc-verify-h"')}
          {bi("p", L["verify_en"], L["verify_es"])}
          <p class="cc-eq"><code>python skills/classics/cc03/verify_cc03_mechanics.py</code><br><code>python skills/classics/cc03/verify_cc03_mechanics.py --planted-defect</code></p>
        </aside>
      </section>"""


def render_gen_rail(is_es: bool) -> str:
    chips = "".join(f'<a class="cc-gen-chip" href="#{a(c["id"])}" data-gen="{a(c["gen"])}">{t(c["gen"])}</a>' for c in C.CARDS)
    label = "Generaciones" if is_es else "Generations"
    return f'      <nav class="cc-gen-rail" aria-label="{label}">{chips}</nav>'


def render_visuals_section(is_es: bool) -> str:
    cards = "\n".join(render_media_figure(item, is_es, in_gallery=True) for item in C.MEDIA)
    return f"""      <section class="cc-visuals" id="visuals" aria-labelledby="cc-vis-h">
        {bi("h2", "Visual Archive (8 Plates)", "Archivo Visual (8 Láminas)", "cc-h2", 'id="cc-vis-h"')}
        {bi("p", "Every documentary photograph, drafting sketch and composite visual study on this page, with credits and full-screen inspection.", "Todas las fotografías documentales, bocetos de ingeniería y composiciones visuales de esta página, con créditos y vista ampliada.", "cc-small")}
        <div class="cc-visuals-grid">
{cards}
        </div>
      </section>"""


def render_lightbox(is_es: bool) -> str:
    prev_lbl = "Anterior" if is_es else "Previous"
    next_lbl = "Siguiente" if is_es else "Next"
    close_lbl = "Cerrar" if is_es else "Close"
    aria_lbl = "Visor de láminas a pantalla completa" if is_es else "Full-screen visual inspection dialog"
    return f"""  <dialog class="cc-lightbox" id="cc-lightbox" aria-label="{a(aria_lbl)}">
    <div class="cc-lightbox-bar">
      <span class="cc-media-badge" id="cc-lb-badge">1 / {len(C.MEDIA)}</span>
      <div class="cc-lightbox-actions">
        <button type="button" class="cc-btn cc-btn-quiet" data-cc-lb-prev data-en="Previous" data-es="Anterior">{t(prev_lbl)}</button>
        <button type="button" class="cc-btn cc-btn-quiet" data-cc-lb-next data-en="Next" data-es="Siguiente">{t(next_lbl)}</button>
        <button type="button" class="cc-btn cc-btn-quiet" data-cc-lb-close data-en="Close" data-es="Cerrar">{t(close_lbl)}</button>
      </div>
    </div>
    <div class="cc-lightbox-stage">
      <img id="cc-lb-img" alt="">
    </div>
    <p class="cc-lightbox-cap" id="cc-lb-cap"></p>
  </dialog>"""


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
    return f"""      <section class="cc-sources" id="sources" aria-labelledby="cc-src-h">
        {bi("h2", "Sources", "Fuentes", "cc-h2", 'id="cc-src-h"')}
        {bi("p", f"All read on {C.ACCESSED}. BMW/MINI marks official BMW Group &amp; MINI USA pages; Club/Track marks UK Mini 7 Racing Club, MINI CHALLENGE and circuit records; Record marks encyclopedic specification and regulatory tables; Paper marks peer-reviewed studies checked in Crossref and Scite on the same day (zero retractions; they explain general mechanics and did not test a Mini); Photo Archive marks Wikimedia Commons CC BY 2.0 / CC BY 4.0 photography.", f"Todas consultadas el {C.ACCESSED}. BMW/MINI marca páginas oficiales de BMW Group y MINI USA; Club/Pista, registros de Mini 7 Racing Club, MINI CHALLENGE y el circuito; Ficha, tablas de especificaciones y normas; Artículo, estudios revisados por pares verificados en Crossref y Scite el mismo día (cero retractaciones; explican mecánica general y no probaron un Mini); Archivo Fotográfico marca fotografías de Wikimedia Commons bajo CC BY 2.0 / CC BY 4.0.", "cc-small")}
        <ol class="cc-source-list">
{chr(10).join('          ' + i for i in items)}
        </ol>
      </section>"""


def render_page(catalog: dict, lang: str = "en") -> str:
    is_es = lang == "es"
    rel = "../.."
    t_en, d_en, t_es, d_es = C.SEO
    title = t_es if is_es else t_en
    desc = d_es if is_es else d_en
    canon = B.page_url(PATH, lang)
    image = "https://informatico.ai/plates/cc03.png"
    crumbs = [(BRAND, B.page_url("", lang)), ("Ingeniería" if is_es else "Engineering", B.page_url("engineering/", lang)), (C.CODE, canon)]
    ld = B._ld("ScholarlyArticle", title, desc, canon, lang, image=image, date_published=C.DATE,
               date_modified=C.DATE, crumbs=crumbs)
    head = B.render_head(f"{title} | {BRAND}", desc, PATH, "article", image, rel, rel, ld, lang)
    head = head.replace("</head>", f'  <link rel="stylesheet" href="{rel}/cult-classics.css">\n</head>')
    h = C.HERO
    ht = C.HERO_TRIBUTE
    frontispiece = _media_map()["plate-frontispiece"]
    pause_label = ("Pausar movimiento", "Reanudar movimiento") if is_es else ("Pause motion", "Resume motion")
    parts = "\n".join(render_part(p, is_es) for p in C.PARTS)
    opening = "\n".join(f'        {bi("p", p["en"], p["es"])}\n        {cite(p["src"])}' for p in C.OPENING)
    closing = "\n".join(f'        {bi("p", p["en"], p["es"])}' for p in C.CLOSING)
    jumps = [(f"#{p['id']}", f"{p['numeral']} · {p['title_en']}", f"{p['numeral']} · {p['title_es']}") for p in C.PARTS]
    jumps += [
        ("#north-america-spec", "US & Mexico", "EE. UU. y México"),
        ("#ghost-race", "Brands Hatch Indy", "Brands Hatch Indy"),
        ("#part-5", "V · Lab", "V · Laboratorio"),
        ("#visuals", "Visual Archive", "Archivo Visual"),
        ("#sources", "Sources", "Fuentes"),
    ]
    jump_html = " ".join(f'<a class="tp-essay-jump-pill" href="{jh}" data-en="{a(je)}" data-es="{a(js)}">{t(js if is_es else je)}</a>' for jh, je, js in jumps)
    aria_crumb = "Ruta de navegación" if is_es else "Breadcrumb"
    aria_jump = "Secciones" if is_es else "Sections"
    honor_roll = f"""        <aside class="cc-honor-roll" aria-label="{a(ht['kicker_es'] if is_es else ht['kicker_en'])}">
          <p class="tp-kicker">{bi("span", ht["kicker_en"], ht["kicker_es"])}</p>
          <dl class="cc-honor-dl">
            <div class="cc-honor-row">{bi("dt", ht["chassis_label_en"], ht["chassis_label_es"])}{bi("dd", ht["chassis_en"], ht["chassis_es"])}</div>
            <div class="cc-honor-row">{bi("dt", ht["sport_label_en"], ht["sport_label_es"])}{bi("dd", ht["sport_en"], ht["sport_es"])}</div>
            <div class="cc-honor-row">{bi("dt", ht["works_label_en"], ht["works_label_es"])}{bi("dd", ht["works_en"], ht["works_es"])}</div>
          </dl>
          {cite(ht["src"])}
        </aside>"""
    return f"""{head}
<body class="tp-body tp-page-folio cc-page cc-page-mini">
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
    <article class="cc-feature" data-folio-id="{a(C.CODE)}">
      <header class="cc-hero">
        <div class="cc-hero-grid">
          <div class="cc-hero-copy">
            <p class="tp-kicker">{bi("span", h["kicker_en"], h["kicker_es"])} · {bi("span", h["reading_en"], h["reading_es"])}</p>
            <h1 class="tp-h1 cc-h1" data-en="{a(h['title_en'])}" data-es="{a(h['title_es'])}">{t(h['title_en'])}</h1>
            {bi("p", h["dek_en"], h["dek_es"], "tp-standfirst")}
            <p class="cc-motion"><button type="button" class="cc-btn cc-btn-quiet" data-cc-pause aria-pressed="false" data-label-pause="{a(pause_label[0])}" data-label-resume="{a(pause_label[1])}">{t(pause_label[0])}</button></p>
            {bi("p", C.BRIEF_NOTE["en"], C.BRIEF_NOTE["es"], "cc-brief")}
          </div>
          {render_media_figure(frontispiece, is_es, "cc-hero-sketch")}
        </div>
{honor_roll}
      </header>
      <nav class="tp-essay-jump-bar" aria-label="{aria_jump}">{jump_html}</nav>
{render_gen_rail(is_es)}
      <section class="cc-opening" aria-label="{a('Inicio' if is_es else 'Opening')}">
{opening}
      </section>
{parts}
{render_laps_section(is_es)}
{render_lab_section(is_es)}
{render_silent(is_es)}
      <section class="cc-closing" aria-label="{a('Cierre' if is_es else 'Closing')}">
{closing}
      </section>
{render_visuals_section(is_es)}
{render_sources(is_es)}
      {bi("p", C.FOOTER_NOTE["en"], C.FOOTER_NOTE["es"], "cc-footnote")}
    </article>
{render_lightbox(is_es)}
{B.render_site_footer(rel)}
  </main>
  <script type="module" src="{rel}/modules/main.mjs"></script>
  <script type="module" src="{rel}/modules/cult-classics.mjs"></script>
</body>
</html>
"""


# ------------------------------------------------------------------------------------------------- plate ----------

def write_plate() -> None:
    """A 1200x630 share image: schematic 1959 -> R53 -> F56 MINI outlines, Chili Red + gold rules and chequered band."""
    import build_cross_scale_essays as E  # noqa: E402
    w, h = 1200, 630
    buf = E._make_canvas(w, h, (236, 238, 240))
    for ix in range(0, w, 40):
        for row_y, alt in ((530, 0), (566, 1), (602, 0)):
            if ((ix // 40) + alt) % 2 == 0:
                E._fill_rect(buf, w, h, ix, row_y, ix + 40, row_y + 34, (21, 53, 86), 0.14)
    E._fill_rect(buf, w, h, 80, 102, 560, 108, (176, 48, 30), 1.0)
    E._fill_rect(buf, w, h, 80, 114, 380, 119, (184, 137, 40), 1.0)
    for j, k in enumerate((0.0, 0.5, 1.0)):
        ox, oy = 140 + j * 330, 238 + j * 34
        nose_x = 56 - 16 * k
        cowl_x, cowl_y = 104 + 2 * k, 48 - 4 * k
        roof_front_x, roof_y = 122 + 4 * k, 22 - 4 * k
        roof_rear_x, tail_x = 216 + 14 * k, 236 + 12 * k
        pts = [
            (nose_x, 87), (nose_x - 2, 68 - 5 * k), (nose_x + 4, 59 - 4 * k),
            (cowl_x, cowl_y), (roof_front_x, roof_y), (roof_rear_x, roof_y + 1),
            (tail_x, 54 + 2 * k), (tail_x + 2, 87), (nose_x, 87),
        ]
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            E._draw_line(buf, w, h, ox + x0, oy + y0, ox + x1, oy + y1, 3, (17, 22, 28), 0.86)
        r = 11.5 + 6.0 * k
        for cx in (82, 206 + 10 * k):
            E._draw_ring(buf, w, h, ox + cx, oy + 80, r, 3, (184, 137, 40) if k == 1.0 else (17, 22, 28), 0.9)
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
    print(f"PASS: Built {C.CODE} ({len(written)} pages, EN + ES-MX), plate cc03.png ({digest}), sitemap.xml and llms.txt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
