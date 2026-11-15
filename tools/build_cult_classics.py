#!/usr/bin/env python3
"""Build CC.01, the Golf GTI cult-classic feature (/classics/golf-gti/ and /es-mx/classics/golf-gti/).

Content lives in tools/folios/classics/cc01.py. This module only lays it out: the page shell comes from
build_longform_folios (head, masthead, contents dialog, footer), the drawings are generated SVG, and the behaviour is
in src/modules/cult-classics.mjs (no inline script or style: the site's CSP forbids both).

Run on its own: python tools/build_cult_classics.py   (also called from build_longform_folios.main)
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


# --------------------------------------------------------------------------------------------- drawings ----------

def hatch_path(k: float) -> str:
    """Schematic hatchback side profile in a 300×110 box; k=0 boxy (Mk1) … k=1 crisp (Mk8). Freehand proportions."""
    ground = 92
    roof_y = 24 + 5 * k
    nose_top = 62 - 2 * k
    ws_base_x = 104 - 10 * k          # windscreen base
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
    return (f'<g class="cc-wheel"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"/>'
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r * 0.55:.1f}"/>{spokes}</g>')


def silhouette(k: float, gen: str, extra_cls: str = "") -> str:
    r = 15 + 3 * k
    return (f'<svg class="cc-car {extra_cls}" data-gen="{a(gen)}" viewBox="0 0 300 110" width="300" height="110" '
            f'focusable="false" aria-hidden="true"><path class="cc-car-body" d="{hatch_path(k)}"/>'
            f'<line class="cc-car-red" x1="12" y1="{70 - 2 * k:.1f}" x2="40" y2="{70 - 2 * k:.1f}"/>'
            f'{wheel(62, 92 - r + 6, r)}{wheel(232, 92 - r + 6, r)}</svg>')


def render_parade() -> str:
    cars = []
    for i, card in enumerate(C.CARDS):
        k = i / (len(C.CARDS) - 1)
        extra = "cc-car-tint" if card.get("egg") else ""
        cars.append(f'    <div class="cc-lane cc-lane-{i + 1}">{silhouette(k, card["gen"], extra)}</div>')
    return render_track_layers() + '\n  <div class="cc-parade" aria-hidden="true">\n' + "\n".join(cars) + "\n  </div>"


def render_track_layers() -> str:
    """Fixed, decorative parallax racetrack: far hills, the track ribbon with a centre line, near kerbs.
    Each layer is drawn twice (y and y+1000) so the scroll offset can wrap seamlessly."""
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


LOOP = "M 80 60 L 420 60 C 520 60 540 140 480 180 L 360 250 C 320 274 320 300 360 300 L 520 300 C 600 300 600 400 520 400 L 80 400 C 20 400 20 60 80 60 Z"


def render_laps_section(is_es: bool) -> str:
    x = C.LAPS_TEXT
    fastest = min(lap[5] for lap in C.LAPS)
    dots, legend, rows = [], [], []
    for i, (gen, car, year, ps, ts, secs, driver, tyres, cfg) in enumerate(C.LAPS):
        hue = ("cc-dot-a", "cc-dot-b", "cc-dot-c", "cc-dot-d", "cc-dot-e", "cc-dot-f", "cc-dot-g", "cc-dot-h")[i]
        dots.append(f'<g class="cc-ghost {hue}" data-secs="{secs}"><circle r="9" cx="80" cy="60"/>'
                    f'<text x="80" y="64" text-anchor="middle">{i + 1}</text></g>')
        legend.append(f'<li class="{hue}"><span class="cc-ghost-key" aria-hidden="true">{i + 1}</span> {t(gen)} · {t(car)} ({year})</li>')
        cfg_cell = cfg if cfg else ("en blanco" if is_es else "blank")
        tyres_cell = tyres if tyres != "not stated" else ("no se indica" if is_es else "not stated")
        rows.append(f'<tr><td>{i + 1}</td><td>{t(gen)}</td><th scope="row">{t(car)}</th><td>{year}</td><td>{ps} PS</td>'
                    f'<td class="cc-num">{t(ts)}</td><td>{t(driver)}</td><td>{t(tyres_cell)}</td><td>{t(cfg_cell)}</td></tr>')
    cols = [("#", "#"), ("Gen", "Gen"), ("Car, as listed", "Auto, como aparece"), ("Year", "Año"), ("Output", "Potencia"),
            ("Lap", "Vuelta"), ("Driver", "Piloto"), ("Tyres", "Llantas"), ("Configuration", "Configuración")]
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


def render_gen_rail(is_es: bool) -> str:
    chips = "".join(f'<a class="cc-gen-chip" href="#{a(c["id"])}" data-gen="{a(c["gen"])}">{t(c["gen"])}</a>' for c in C.CARDS)
    label = "Generaciones" if is_es else "Generations"
    return f'      <nav class="cc-gen-rail" aria-label="{label}">{chips}</nav>'


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
        return (f'<g class="cc-gear" data-gear="{n}"><circle cx="{x}" cy="{y}" r="17"/>'
                f'<text x="{x}" y="{y + 5}" text-anchor="middle">{n}</text></g>')
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
    for i, (en, es, kg) in enumerate(C.WEIGHT_LEDGER):
        w = kg * 40  # proportional: bar length is to scale
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
        return (f'<g class="cc-steer {cls}" transform="rotate(0 {cx} 60)"><circle cx="{cx}" cy="60" r="40"/>'
                f'<circle cx="{cx}" cy="60" r="9"/><line x1="{cx - 38}" y1="60" x2="{cx - 9}" y2="60"/>'
                f'<line x1="{cx + 9}" y1="60" x2="{cx + 38}" y2="60"/><line x1="{cx}" y1="69" x2="{cx}" y2="98"/>'
                f'<line class="cc-steer-mark" x1="{cx}" y1="20" x2="{cx}" y2="30"/></g>')
    return f"""<svg class="cc-steer-svg" viewBox="0 0 320 140" width="320" height="140" role="img" aria-labelledby="cc-steer-title">
          <title id="cc-steer-title">Two steering wheels turned to the same road-wheel angle: the progressive rack needs less rotation</title>
          {sw(80, "cc-steer-prog")}{sw(240, "cc-steer-std")}
          <text class="cc-svg-label" x="80" y="132" text-anchor="middle" data-en="GTI, progressive" data-es="GTI, progresiva">GTI, progressive</text>
          <text class="cc-svg-label" x="240" y="132" text-anchor="middle" data-en="lesser Golf" data-es="Golf menos potente">lesser Golf</text>
        </svg>"""


# -------------------------------------------------------------------------------------------------- page ----------

def cite(keys: list[str]) -> str:
    if not keys:
        return ""
    return f'<p class="cc-cite">{" ".join(stamp(k) for k in keys)}</p>'


def stamp(key: str) -> str:
    s = C.SOURCES[key]
    return bi("a", s["short"], s.get("short_es", s["short"]), f"cc-stamp cc-stamp-{s['kind']}", f'href="#src-{a(key)}"')


def render_card(card: dict, is_es: bool) -> str:
    rows = []
    for en, es, value, key in card["plate"]:
        s = C.SOURCES[key]
        rows.append(
            f'<div class="cc-plate-row">{bi("dt", en, es)}<dd>{bi("span", value, C.VALUE_ES.get(value, value), "cc-plate-val")} '
            f'{stamp(key)}</dd></div>'
        )
    keys = sorted({r[3] for r in card["plate"]}, key=list(C.SOURCES).index)
    egg = ""
    if card.get("egg"):
        egg = render_egg(is_es)
    extra = ""
    if card["id"] == "mk7":
        extra = render_mk7_extras(is_es)
    return f"""        <article class="cc-card" id="{a(card['id'])}" data-gen="{a(card['gen'])}">
          <header class="cc-card-head">
            <p class="cc-card-gen"><span>{t(card['gen'])}</span> <span class="cc-card-years">{t(card['years'])}</span></p>
            {bi("h3", card["move_en"], card["move_es"], "cc-card-move")}
          </header>
          {bi("p", card["body_en"], card["body_es"], "cc-card-body")}
          <div class="cc-plate" role="group" aria-label="{a('Placa de especificaciones' if is_es else 'Spec plate')} {a(card['gen'])}">
            <dl>{''.join(rows)}</dl>
            <p class="cc-plate-foot" data-en="Read {a(C.ACCESSED)}" data-es="Consultado {a(C.ACCESSED)}">Read {t(C.ACCESSED)}</p>
          </div>
{extra}{egg}
        </article>"""


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


def egg_caption(is_es: bool) -> str:
    """The caption with the wheel maker linked (built per language: a link cannot sit inside a data-en/data-es swap)."""
    e = C.EGG
    text = e["caption_es"] if is_es else e["caption_en"]
    label = e["link_label"]
    before, _sep, after = text.partition(label)
    return f'{t(before)}<a href="{a(e["link_url"])}" rel="noopener noreferrer">{t(label)}</a>{t(after)}'


def render_egg(is_es: bool) -> str:
    e = C.EGG
    return f"""          <div class="cc-egg">
            <button type="button" class="cc-egg-btn" aria-expanded="false" aria-controls="cc-egg-panel" data-label-open="{a(e['button_es'] if is_es else e['button_en'])}" data-label-close="{a(e['close_es'] if is_es else e['close_en'])}" data-en="{a(e['button_en'])}" data-es="{a(e['button_es'])}">{t(e['button_en'])}</button>
            <figure class="cc-egg-panel" id="cc-egg-panel" hidden>
              <img src="../../{e['image']}" width="{e['width']}" height="{e['height']}" loading="lazy" decoding="async" alt="{a(e['alt_es'] if is_es else e['alt_en'])}">
              <figcaption>{egg_caption(is_es)}</figcaption>
            </figure>
          </div>
"""


def render_diff_section(is_es: bool) -> str:
    modes = [("open", "Open differential", "Diferencial abierto"),
             ("xds", "XDS+ · brake the inside wheel", "XDS+ · frenar la rueda interior"),
             ("lock", "Clutch-pack lock", "Bloqueo por embragues")]
    radios = "".join(
        f'<label class="cc-mode"><input type="radio" name="cc-diff-mode" value="{m}"{" checked" if m == "open" else ""}> {bi("span", en, es)}</label>'
        for m, en, es in modes
    )
    legend = "Estrategia" if is_es else "Strategy"
    thr = "Acelerador" if is_es else "Throttle"
    return f"""      <section class="cc-observatory" id="differential" aria-labelledby="cc-diff-h">
        {bi("h2", "The differential bench", "El banco de diferenciales", "cc-h2", 'id="cc-diff-h"')}
        {bi("p", C.DIFF_TEXT["intro_en"], C.DIFF_TEXT["intro_es"], "cc-lede")}
        <div class="cc-bench" data-cc-diff>
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
      </section>"""


def render_sources(is_es: bool) -> str:
    items = []
    for key, s in C.SOURCES.items():
        en, es = C.KIND_LABEL[s["kind"]]
        items.append(
            f'<li id="src-{a(key)}"><span class="cc-stamp cc-stamp-{s["kind"]}" data-en="{a(en)}" data-es="{a(es)}">{t(en)}</span> '
            f'<a href="{a(s["url"])}" rel="noopener noreferrer">{t(s["label"])}</a></li>'
        )
    return f"""      <section class="cc-sources" id="sources" aria-labelledby="cc-src-h">
        {bi("h2", "Sources", "Fuentes", "cc-h2", 'id="cc-src-h"')}
        {bi("p", f"All read on {C.ACCESSED}. VW marks a Volkswagen statement; Press marks independent coverage; Paper marks a peer-reviewed article checked in Scite for retractions and concerns on the same day. The papers explain mechanisms in general and did not test these cars.", f"Todas consultadas el {C.ACCESSED}. VW marca una declaración de Volkswagen; Prensa, cobertura independiente; Artículo, un texto revisado por pares que verificamos en Scite ese mismo día (sin retractaciones ni alertas). Los artículos explican mecanismos en general y no probaron estos autos.", "cc-small")}
        <ol class="cc-source-list">
{chr(10).join('          ' + i for i in items)}
        </ol>
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
        extra = render_dct_section(is_es)
    elif part["id"] == "part-4":
        extra = render_diff_section(is_es)
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


def render_page(catalog: dict, lang: str = "en") -> str:
    is_es = lang == "es"
    rel = "../.."
    t_en, d_en, t_es, d_es = C.SEO
    title = t_es if is_es else t_en
    desc = d_es if is_es else d_en
    canon = B.page_url(PATH, lang)
    image = "https://informatico.ai/plates/cc01.png"
    crumbs = [(BRAND, B.page_url("", lang)), (C.CODE, canon)]
    ld = B._ld("ScholarlyArticle", title, desc, canon, lang, image=image, date_published=C.DATE,
               date_modified=C.DATE, crumbs=crumbs)
    head = B.render_head(f"{title} | {BRAND}", desc, PATH, "article", image, rel, rel, ld, lang)
    head = head.replace("</head>", f'  <link rel="stylesheet" href="{rel}/cult-classics.css">\n</head>')
    h = C.HERO
    pause_label = ("Pausar movimiento", "Reanudar movimiento") if is_es else ("Pause motion", "Resume motion")
    parts = "\n".join(render_part(p, is_es) for p in C.PARTS)
    opening = "\n".join(f'        {bi("p", p["en"], p["es"])}\n        {cite(p["src"])}' for p in C.OPENING)
    closing = "\n".join(f'        {bi("p", p["en"], p["es"])}' for p in C.CLOSING)
    jumps = [(f"#{p['id']}", f"{p['numeral']} · {p['title_en']}", f"{p['numeral']} · {p['title_es']}") for p in C.PARTS]
    jumps += [("#ghost-race", "Ghost race", "Carrera fantasma"), ("#sources", "Sources", "Fuentes")]
    jump_html = " ".join(f'<a class="tp-essay-jump-pill" href="{jh}" data-en="{a(je)}" data-es="{a(js)}">{t(je)}</a>' for jh, je, js in jumps)
    aria_crumb = "Ruta de navegación" if is_es else "Breadcrumb"
    aria_jump = "Secciones" if is_es else "Sections"
    return f"""{head}
<body class="tp-body tp-page-folio cc-page">
{B.render_masthead(rel, "", lang)}
{B.render_contents_dialog(rel, catalog, C.SLUG)}
{render_parade()}
  <main id="main" class="tp-shell cc-shell" tabindex="-1">
    <nav class="tp-breadcrumb-bar" aria-label="{aria_crumb}">
      <ol class="tp-breadcrumb-list">
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="../../">Informatico.ai</a></li>
        <li class="tp-crumb-item" aria-current="page"><span>{t(C.CODE)}</span></li>
      </ol>
    </nav>
    <article class="cc-feature" data-folio-id="{a(C.CODE)}">
      <header class="cc-hero">
        <p class="tp-kicker">{bi("span", h["kicker_en"], h["kicker_es"])} · {bi("span", h["reading_en"], h["reading_es"])}</p>
        <h1 class="tp-h1 cc-h1" data-en="{a(h['title_en'])}" data-es="{a(h['title_es'])}">{t(h['title_en'])}</h1>
        {bi("p", h["dek_en"], h["dek_es"], "tp-standfirst")}
        <p class="cc-motion"><button type="button" class="cc-btn cc-btn-quiet" data-cc-pause aria-pressed="false" data-label-pause="{a(pause_label[0])}" data-label-resume="{a(pause_label[1])}">{t(pause_label[0])}</button></p>
        {bi("p", C.BRIEF_NOTE["en"], C.BRIEF_NOTE["es"], "cc-brief")}
      </header>
      <nav class="tp-essay-jump-bar" aria-label="{aria_jump}">{jump_html}</nav>
{render_gen_rail(is_es)}
      <section class="cc-opening" aria-label="{a('Inicio' if is_es else 'Opening')}">
{opening}
      </section>
{parts}
{render_laps_section(is_es)}
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


# ------------------------------------------------------------------------------------------------- plate ----------

def write_plate() -> None:
    """A 1200×630 share image: schematic silhouettes, a red rule and a tartan band. No photograph, no logo."""
    import build_cross_scale_essays as E  # noqa: E402  (PNG helpers)
    w, h = 1200, 630
    buf = E._make_canvas(w, h, (236, 238, 240))
    for i in range(0, w, 60):  # tartan band
        E._fill_rect(buf, w, h, i, 520, i + 30, 630, (21, 53, 86), 0.18)
        E._fill_rect(buf, w, h, 0, 540 + (i // 60 % 3) * 24, w, 548 + (i // 60 % 3) * 24, (176, 48, 30), 0.06)
    E._fill_rect(buf, w, h, 80, 110, 560, 116, (176, 48, 30), 1.0)
    for j, k in enumerate((0.0, 0.5, 1.0)):
        ox, oy, s = 140 + j * 330, 250 + j * 40, 1.0
        pts = [(10, 82), (8, 66), (20, 61), (104 - 10 * k, 52 - 4 * k), (132 - 6 * k, 24 + 5 * k),
               (222 + 6 * k, 26 + 7 * k), (280, 50 + 6 * k), (290, 58 + 6 * k), (290, 82), (10, 82)]
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            E._draw_line(buf, w, h, ox + x0 * s, oy + y0 * s, ox + x1 * s, oy + y1 * s, 3, (17, 22, 28), 0.85)
        for cx in (62, 232):
            E._draw_ring(buf, w, h, ox + cx * s, oy + 80 * s, 16, 3, (17, 22, 28), 0.85)
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
