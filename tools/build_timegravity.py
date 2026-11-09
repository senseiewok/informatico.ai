#!/usr/bin/env python3
"""Build the Time & Gravity track pages (/timegravity/ and /es-mx/timegravity/) from tools/folios/timegravity/.

Reuses the site's own head, masthead, contents dialog, footer and Spanish copier from build_longform_folios.py, so a
T page is a sibling of a Toolbox page: same shell, same language toggle, same static Spanish twin. Claims are spans
with a label and ledger ids; transitions and questions carry none. After the pages, it re-renders the cover,
sitemap.xml and llms.txt through the main builder so the track's entries live where the Toolbox's do.
"""
from __future__ import annotations

import hashlib
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_longform_folios as B  # noqa: E402
from folios.timegravity import (  # noqa: E402
    BOUNDARY_EN,
    BOUNDARY_ES,
    LABEL_ES,
    LABELS,
    PAGES,
    TRACK_DATE,
    TRACK_MAP,
    TRACK_TITLE_EN,
    TRACK_TITLE_ES,
)
from folios.seo_copy import BRAND, PILLAR_SEO  # noqa: E402
from timegravity_kernel import (  # noqa: E402
    A_GPS, G0, G_NEWTON, GM_EARTH, R_EARTH, fall_two_bodies, gps_position_error_per_day_m, gps_schwarzschild_net, gps_terms,
    gps_uncertainty_budget, integrate, light_clock_dilation, poisson_radial,
)

from timegravity_kernel_quantum import OMEGA_SR, pw_history_state, zych_first_zero, zych_visibility  # noqa: E402

RESEARCH = ROOT / "src" / "research"
LEDGER = json.loads((ROOT / "timegravity" / "ledger.json").read_text(encoding="utf-8"))
ROWS = {r["id"]: r for r in LEDGER["rows"]}
CACHE = json.loads((ROOT / "data" / "folio-citations.cache.json").read_text(encoding="utf-8"))

# The (t, z) plot box shared with timegravity-slope.mjs through data-* attributes on the <svg>.
PLOT = {"x0": 300, "x1": 890, "y0": 50, "y1": 390, "ztop": 1.0, "zbot": -10.5}

LABEL_DEF = {
    "MEASURED": ("At least two collaborations, peer-reviewed DOIs, older than the replication window.",
                 "Al menos dos colaboraciones, DOI revisados por pares, más antiguas que la ventana de replicación."),
    "DERIVED": ("Follows by mathematics from a named MEASURED parent row.",
                "Se sigue por matemáticas de una fila madre MEDIDA con nombre."),
    "BOUND": ("An exclusion limit: what the data rule out, not what they show.",
              "Un límite de exclusión: lo que los datos descartan, no lo que muestran."),
    "SINGLE RESULT": ("One collaboration, or anything inside the last twenty-four months.",
                      "Una sola colaboración, o cualquier cosa dentro de los últimos veinticuatro meses."),
    "PROPOSED": ("A proposal or a preprint; a preprint can never be more.",
                 "Una propuesta o una prepublicación; una prepublicación nunca puede ser más."),
    "OPEN": ("A question the field has not closed.", "Una pregunta que el campo no ha cerrado."),
}


def a(s: str) -> str:
    return html.escape(s, quote=True)


def t(s: str) -> str:
    return html.escape(s, quote=False)


def bi(tag: str, en: str, es: str, cls: str = "", extra: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    x = f" {extra}" if extra else ""
    return f'<{tag}{c}{x} data-en="{a(en)}" data-es="{a(es)}">{t(en)}</{tag}>'


def seg(s: dict) -> str:
    if s["kind"] == "text":
        return f'<span data-en="{a(s["en"])}" data-es="{a(s["es"])}">{t(s["en"])}</span>'
    label = s["label"]
    parent = f' data-tg-parent="{a(s["parent"])}"' if s.get("parent") else ""
    return (
        f'<span class="tg-claim" data-tg-label="{a(label)}" data-tg-label-es="{a(LABEL_ES[label])}" '
        f'data-tg-ledger="{a(",".join(s["ids"]))}"{parent} data-en="{a(s["en"])}" data-es="{a(s["es"])}">{t(s["en"])}</span>'
    )


def para(p: dict) -> str:
    return "<p>" + "".join(seg(s) for s in p["segments"]) + "</p>"


def png_sha8(slug: str) -> str:
    p = RESEARCH / "plates" / f"{slug}.png"
    return hashlib.sha256(p.read_bytes()).hexdigest()[:8] if p.is_file() else "00000000"


def plate_slug(page: dict) -> str:
    return "t00" if page["slug"] == "" else page["slug"]


def boundary_banner() -> str:
    return f"""      <div class="tg-boundary-banner" role="note" aria-label="Fixed boundary of every Time and Gravity page">
        {bi("strong", "Fixed boundary · printed on every T page · asserted by the lint", "Frontera fija · impresa en cada página T · comprobada por el lint")}
        {bi("span", BOUNDARY_EN, BOUNDARY_ES)}
      </div>"""


def breadcrumb(rel_res: str, page: dict) -> str:
    if page["slug"] == "":
        tail = f'<li class="tp-crumb-item" aria-current="page">{bi("span", TRACK_TITLE_EN, TRACK_TITLE_ES)}</li>'
        mid = ""
    else:
        mid = (f'<li class="tp-crumb-item"><a class="tp-crumb-link" href="{B._href(rel_res, "timegravity/")}" '
               f'data-en="{a(TRACK_TITLE_EN)}" data-es="{a(TRACK_TITLE_ES)}">{t(TRACK_TITLE_EN)}</a></li>\n        ')
        tail = f'<li class="tp-crumb-item" aria-current="page">{page["code"]}</li>'
    return f"""  <nav class="tp-breadcrumb-bar" aria-label="Breadcrumb">
    <ol class="tp-breadcrumb-list">
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="{B._href(rel_res)}">Informatico.ai</a></li>
        {mid}{tail}
    </ol>
  </nav>"""


PLATE_CAPTIONS = {
    "T.00": (
        "A worldline across a clock-rate gradient, with a marker for the 'now' the intuition imagines. General relativity has the line and the shading; it has no marker.",
        "Una línea de mundo sobre un gradiente de ritmo de relojes, con un marcador para el 'ahora' que la intuición imagina. La relatividad general tiene la línea y el sombreado; no tiene marcador.",
        "a worldline drawn across a shaded column that shows how fast a clock runs at each height, darker meaning slower, with one marker on the line",
        "una línea de mundo trazada sobre una columna sombreada que muestra qué tan rápido avanza un reloj a cada altura, más oscuro significa más lento, con un marcador sobre la línea",
    ),
    "T.01": (
        "The worldline the kernel integrates: a body released at rest drifts toward the slower clocks, faster and faster, with no force term in the equation.",
        "La línea de mundo que integra el núcleo: un cuerpo soltado en reposo deriva hacia los relojes más lentos, cada vez más rápido, sin término de fuerza en la ecuación.",
        "a falling worldline drawn across a shaded column that shows how fast a clock runs at each height, darker meaning slower",
        "una línea de mundo que cae trazada sobre una columna sombreada que muestra qué tan rápido avanza un reloj a cada altura, más oscuro significa más lento",
    ),
    "T.02": (
        "A satellite on its orbit around the shaded Earth, and three bars for the clock budget: the gravitational gain, the velocity loss and the net, all computed from GM, the orbit radius and c.",
        "Un satélite en su órbita alrededor de la Tierra sombreada, y tres barras para el presupuesto del reloj: la ganancia gravitatoria, la pérdida por velocidad y el neto, todo calculado desde GM, el radio orbital y c.",
        "an orbit circle around a shaded disc with a satellite dot, and three horizontal bars of different lengths",
        "un círculo de órbita alrededor de un disco sombreado con un punto satélite, y tres barras horizontales de distinta longitud",
    ),
    "T.04": (
        "Two arms of an interferometer one above the other, each with a clock face, and the visibility curve that falls as the height difference grows.",
        "Dos brazos de un interferómetro uno sobre otro, cada uno con una carátula de reloj, y la curva de visibilidad que cae conforme crece la diferencia de altura.",
        "two horizontal arms at different heights with a clock face on each, and a curve that falls from left to right",
        "dos brazos horizontales a distintas alturas con una carátula de reloj en cada uno, y una curva que cae de izquierda a derecha",
    ),
    "T.07": (
        "A grid of tiles for a stationary global state, one row per clock reading, and the cosine-squared curve the conditional probabilities trace; nothing in the grid moves.",
        "Una cuadrícula de mosaicos para un estado global estacionario, una fila por lectura del reloj, y la curva coseno cuadrado que trazan las probabilidades condicionales; nada en la cuadrícula se mueve.",
        "a grid of shaded tiles beside a smooth cosine-squared curve with dots on it",
        "una cuadrícula de mosaicos sombreados junto a una curva suave de coseno cuadrado con puntos encima",
    ),
    "T.03": (
        "Concentric rings around a mass, darker where clocks run slower, from the Poisson solution on a grid; two dots of different size fall along the same line.",
        "Anillos concéntricos alrededor de una masa, más oscuros donde los relojes van más lento, de la solución de Poisson en una malla; dos puntos de distinto tamaño caen por la misma línea.",
        "concentric rings around a disc, darker toward the centre, and two dots of different size on one vertical line",
        "anillos concéntricos alrededor de un disco, más oscuros hacia el centro, y dos puntos de distinto tamaño sobre una línea vertical",
    ),
}


def lead_figure(page: dict, rel_res: str, es: bool = False) -> str:
    slug = plate_slug(page)
    code = page["code"]
    cap_en_body, cap_es_body, alt_body_en, alt_body_es = PLATE_CAPTIONS[code]
    alt_en = f"Diagram for {code}: {alt_body_en}. Drawn by a script from the page's own numbers; no text, no photograph."
    alt_es = f"Diagrama para {code}: {alt_body_es}. Dibujado por un script con los números de la página; sin texto ni fotografía."
    alt_txt = alt_es if es else alt_en
    fig_label = f"Diagrama principal de {code}" if es else f"Lead diagram for {code}"
    cap_en = f"Plate {code}-V · {cap_en_body} Drawn by timegravity/make_plates.py from tools/timegravity_kernel.py."
    cap_es = f"Lámina {code}-V · {cap_es_body} Dibujada por timegravity/make_plates.py desde tools/timegravity_kernel.py."
    return f"""    <figure class="tp-editorial-figure" data-lead-figure role="group" aria-label="{a(fig_label)}">
      <img class="tp-editorial-img" src="{rel_res}/plates/{slug}.png?v={png_sha8(slug)}" width="1280" height="720" alt="{a(alt_txt)}" loading="eager" fetchpriority="high" decoding="async">
      <figcaption class="tp-editorial-caption">
        {bi("span", cap_en, cap_es)}
        <details class="tp-plate-provenance-details">
          <summary class="tp-plate-provenance-summary" data-en="About this illustration" data-es="Sobre esta ilustración">About this illustration</summary>
          {bi("span", "This plate is a deterministic drawing, not an AI-generated image and not a photograph. The curve is the kernel's own trajectory; the shading exaggerates a clock-rate difference of about one part in 10^16 per metre so that it can be seen at all.", "Esta lámina es un dibujo determinista, no una imagen generada por IA ni una fotografía. La curva es la trayectoria del propio núcleo; el sombreado exagera una diferencia de ritmo de reloj de alrededor de una parte en 10^16 por metro para que se pueda ver.", "tp-drawn-note")}
        </details>
      </figcaption>
    </figure>"""


def clocks_svg(x: float, ys: list[float]) -> str:
    out = []
    for i, y in enumerate(ys):
        ang = -1.2 + 0.55 * i
        import math
        hx, hy = x + 9 * math.cos(ang), y + 9 * math.sin(ang)
        out.append(f'<circle class="tg-clock-face" cx="{x}" cy="{y}" r="12"/><line class="tg-clock-hand" x1="{x}" y1="{y}" x2="{hx:.1f}" y2="{hy:.1f}"/>')
    return "".join(out)


def slope_instrument(page: dict, rel_res: str) -> str:
    ins = page["instrument"]
    P = PLOT
    to_x = lambda tt: P["x0"] + (P["x1"] - P["x0"]) * min(1.0, max(0.0, tt))  # noqa: E731
    to_y = lambda z: P["y0"] + (P["y1"] - P["y0"]) * ((P["ztop"] - z) / (P["ztop"] - P["zbot"]))  # noqa: E731
    res = integrate(True, +1.0, sample_every=250)
    d = " ".join(f'{"M" if i == 0 else "L"} {to_x(tt):.2f} {to_y(max(P["zbot"], z)):.2f}' for i, (_tau, tt, z) in enumerate(res["samples"]))
    bx, by = to_x(res["samples"][-1][1]), to_y(res["samples"][-1][2])
    y_rel = to_y(0.0)
    ticks = "".join(
        f'<line class="tg-axis" x1="{P["x0"] - 5}" y1="{to_y(z):.1f}" x2="{P["x0"]}" y2="{to_y(z):.1f}"/>'
        f'<text x="{P["x0"] - 10}" y="{to_y(z) + 4:.1f}" text-anchor="end" font-size="11">{z:g} m</text>'
        for z in (0, -2, -4, -6, -8, -10)
    )
    tticks = "".join(
        f'<line class="tg-axis" x1="{to_x(tt):.1f}" y1="{P["y1"]}" x2="{to_x(tt):.1f}" y2="{P["y1"] + 5}"/>'
        f'<text x="{to_x(tt):.1f}" y="{P["y1"] + 18}" text-anchor="middle" font-size="11">{tt:g} s</text>'
        for tt in (0, 0.25, 0.5, 0.75, 1.0)
    )
    svg = f"""        <svg class="tg-stage" viewBox="0 0 920 420" role="img" aria-labelledby="tg-stage-title-t01 tg-stage-desc-t01" data-x0="{P['x0']}" data-x1="{P['x1']}" data-y0="{P['y0']}" data-y1="{P['y1']}" data-ztop="{P['ztop']}" data-zbot="{P['zbot']}">
          <title id="tg-stage-title-t01" data-en="Worldline of a body released at rest in a metric where only the rate of time varies with height" data-es="Línea de mundo de un cuerpo soltado en reposo en una métrica donde solo el ritmo del tiempo varía con la altura">Worldline of a body released at rest in a metric where only the rate of time varies with height</title>
          <desc id="tg-stage-desc-t01" data-en="Left, a shaded column: clocks lower down run slower. Right, height against coordinate time: the body starts at height zero and falls 4.9 metres in one second, a parabola with no force term in the equation." data-es="Izquierda, una columna sombreada: los relojes más abajo avanzan más lento. Derecha, altura contra tiempo coordenado: el cuerpo inicia en altura cero y cae 4.9 metros en un segundo, una parábola sin término de fuerza en la ecuación.">Left, a shaded column: clocks lower down run slower. Right, height against coordinate time: the body starts at height zero and falls 4.9 metres in one second, a parabola with no force term in the equation.</desc>
          <defs>
            <linearGradient id="tg-rate-grad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="var(--tp-vellum)"/>
              <stop offset="1" stop-color="var(--tp-prussian)"/>
            </linearGradient>
          </defs>
          <rect class="tg-rate-col" x="140" y="{P['y0']}" width="60" height="{P['y1'] - P['y0']}" rx="6" fill="url(#tg-rate-grad)" style="opacity:0.6"/>
          <text x="170" y="{P['y0'] - 12}" text-anchor="middle" font-size="11" data-en="rate of a clock" data-es="ritmo de un reloj">rate of a clock</text>
          <text x="170" y="{P['y0'] + 16}" text-anchor="middle" font-size="10" data-en="faster" data-es="más rápido">faster</text>
          <text x="170" y="{P['y1'] - 8}" text-anchor="middle" font-size="10" fill="var(--tp-vellum)" data-en="slower" data-es="más lento">slower</text>
          <text x="170" y="{P['y1'] + 18}" text-anchor="middle" font-size="9.5" data-en="(exaggerated ×10¹⁶)" data-es="(exagerado ×10¹⁶)">(exaggerated ×10¹⁶)</text>
          {clocks_svg(80, [to_y(0.0), to_y(-3.5), to_y(-7.0), to_y(-10.0)])}
          <line class="tg-axis" x1="{P['x0']}" y1="{P['y0']}" x2="{P['x0']}" y2="{P['y1']}"/>
          <line class="tg-axis" x1="{P['x0']}" y1="{P['y1']}" x2="{P['x1']}" y2="{P['y1']}"/>
          {ticks}{tticks}
          <text x="{P['x1']}" y="{P['y1'] + 36}" text-anchor="end" font-size="11" data-en="coordinate time t" data-es="tiempo coordenado t">coordinate time t</text>
          <text x="{P['x0'] - 10}" y="{P['y0'] - 12}" text-anchor="end" font-size="11" data-en="height z" data-es="altura z">height z</text>
          <line class="tg-release-line" x1="{P['x0']}" y1="{y_rel:.1f}" x2="{P['x1']}" y2="{y_rel:.1f}"/>
          <text x="{P['x1']}" y="{y_rel - 6:.1f}" text-anchor="end" font-size="10" data-en="released at rest here" data-es="soltado en reposo aquí">released at rest here</text>
          <path class="tg-worldline" data-state="fall" d="{d}"/>
          <circle class="tg-body" cx="{bx:.2f}" cy="{by:.2f}" r="7"/>
        </svg>"""
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="slope" data-tg-g="{G0}" aria-labelledby="tg-instrument-heading-t01">
      <h2 id="tg-instrument-heading-t01" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{svg}
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-grad-t01">
            <span data-en="Gradient (× Earth's surface slope)" data-es="Gradiente (× pendiente en la superficie terrestre)">Gradient (× Earth's surface slope)</span>
            <span data-tg-read="grad">1.00 ×</span>
          </label>
          <input id="tg-grad-t01" data-tg-grad type="range" min="0" max="2" step="0.05" value="1" aria-describedby="tg-status-t01">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and planted defect">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · flatten the gradient" data-es="⚡ Apagado · aplanar el gradiente">⚡ Knockout · flatten the gradient</button>
          <button type="button" class="tp-step-btn" data-tg-flip aria-pressed="false" data-en="Planted defect · flip the sign" data-es="Defecto plantado · invertir el signo">Planted defect · flip the sign</button>
          <button type="button" class="tp-step-btn" data-tg-replay data-en="Replay the fall" data-es="Repetir la caída">Replay the fall</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Slope A′(0) in the rate of time" data-es="Pendiente A′(0) en el ritmo del tiempo">Slope A′(0) in the rate of time</span>
          <span class="tp-readout-v" data-tg-read="slope">{res['slope_Ap']:.3e} 1/m</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Acceleration read from the worldline" data-es="Aceleración leída en la línea de mundo">Acceleration read from the worldline</span>
          <span class="tp-readout-v" data-tg-read="accel">{res['a_eff']:.5f} m/s²</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="|a + g·scale| / g" data-es="|a + g·escala| / g">|a + g·scale| / g</span>
          <span class="tp-readout-v" data-tg-read="err">{abs(res['a_eff'] + G0) / G0:.2e}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Force term in the equation" data-es="Término de fuerza en la ecuación">Force term in the equation</span>
          <span class="tp-readout-v">0</span>
        </div>
      </div>
      <p id="tg-status-t01" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="Falls at g: the clock-rate gradient alone produces the acceleration. No force term anywhere." data-es="Cae a g: el gradiente del ritmo de los relojes produce por sí solo la aceleración. Ninguna fuerza en ningún lado.">Falls at g: the clock-rate gradient alone produces the acceleration. No force term anywhere.</p>
    </section>"""


def worldline_instrument(page: dict) -> str:
    w = page["worldline"]
    pts = [(300 + 590 * s, 70 + 230 * (0.25 * s + 0.75 * s * s)) for s in [i / 40 for i in range(41)]]
    d = " ".join(f'{"M" if i == 0 else "L"} {x:.1f} {y:.1f}' for i, (x, y) in enumerate(pts))
    mx, my = pts[20]
    return f"""    <section class="tg-instrument" id="question" data-tg-instrument="worldline" aria-labelledby="tg-instrument-heading-t00">
      <h2 id="tg-instrument-heading-t00" class="tp-h2" data-en="{a(w['title_en'])}" data-es="{a(w['title_es'])}">{t(w['title_en'])}</h2>
      {bi("p", w["how_en"], w["how_es"], "tg-how")}
        <svg class="tg-stage" viewBox="0 0 920 340" role="img" aria-labelledby="tg-stage-title-t00 tg-stage-desc-t00">
          <title id="tg-stage-title-t00" data-en="A worldline across a clock-rate gradient with a movable marker" data-es="Una línea de mundo sobre un gradiente de ritmo de relojes con un marcador móvil">A worldline across a clock-rate gradient with a movable marker</title>
          <desc id="tg-stage-desc-t00" data-en="Height against coordinate time. A shaded column shows clocks lower down running slower. One curve, the worldline, and one dot on it, the imagined now, which the slider moves. The physics has the curve and the shading; it has no dot." data-es="Altura contra tiempo coordenado. Una columna sombreada muestra que los relojes más abajo avanzan más lento. Una curva, la línea de mundo, y un punto sobre ella, el ahora imaginado, que el deslizador mueve. La física tiene la curva y el sombreado; no tiene punto.">Height against coordinate time. A shaded column shows clocks lower down running slower. One curve, the worldline, and one dot on it, the imagined now, which the slider moves. The physics has the curve and the shading; it has no dot.</desc>
          <defs>
            <linearGradient id="tg-rate-grad-hub" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="var(--tp-vellum)"/>
              <stop offset="1" stop-color="var(--tp-prussian)"/>
            </linearGradient>
          </defs>
          <rect x="140" y="50" width="60" height="250" rx="6" fill="url(#tg-rate-grad-hub)" style="opacity:0.6"/>
          <text x="170" y="38" text-anchor="middle" font-size="11" data-en="rate of a clock" data-es="ritmo de un reloj">rate of a clock</text>
          <text x="170" y="66" text-anchor="middle" font-size="10" data-en="faster" data-es="más rápido">faster</text>
          <text x="170" y="292" text-anchor="middle" font-size="10" fill="var(--tp-vellum)" data-en="slower" data-es="más lento">slower</text>
          {clocks_svg(80, [80.0, 150.0, 220.0, 290.0])}
          <line class="tg-axis" x1="300" y1="50" x2="300" y2="300"/>
          <line class="tg-axis" x1="300" y1="300" x2="890" y2="300"/>
          <text x="890" y="322" text-anchor="end" font-size="11" data-en="coordinate time" data-es="tiempo coordenado">coordinate time</text>
          <text x="290" y="38" text-anchor="end" font-size="11" data-en="height" data-es="altura">height</text>
          <path class="tg-worldline" d="{d}"/>
          <circle class="tg-now-marker" cx="{mx:.1f}" cy="{my:.1f}" r="8"/>
          <text class="tg-now-label" x="{mx + 12:.1f}" y="{my - 10:.1f}" font-size="12" font-weight="700" data-en="now?" data-es="¿ahora?">now?</text>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-now-t00">
            <span data-en="Where the intuition puts 'now'" data-es="Dónde pone la intuición el 'ahora'">Where the intuition puts 'now'</span>
            <span aria-hidden="true">?</span>
          </label>
          <input id="tg-now-t00" data-tg-now type="range" min="0" max="100" step="1" value="50">
        </div>
        {bi("p", "The slider moves a picture, not a variable. No equation on the pages that follow has a term for it.", "El deslizador mueve un dibujo, no una variable. Ninguna ecuación en las páginas que siguen tiene un término para él.", "tg-status")}
      </div>
    </section>"""


def predict_block(page: dict) -> str:
    """Pedagogy: predict before reveal. A static question without scripts; with scripts, the chosen answer gets a verdict."""
    pr = page.get("predict")
    if not pr:
        return ""
    slug = plate_slug(page)
    opts = "\n".join(
        f'          <button type="button" class="tp-step-btn" data-tg-option="{i}" aria-pressed="false" data-en="{a(en)}" data-es="{a(es)}">{t(en)}</button>'
        for i, (en, es) in enumerate(pr["options"])
    )
    return f"""      <div class="tg-predict" data-tg-predict data-tg-answer="{pr['answer']}" role="group" aria-labelledby="tg-predict-q-{slug}">
        <p id="tg-predict-q-{slug}" class="tg-predict-q"><span class="tg-predict-kicker" data-en="Predict before you reveal" data-es="Predice antes de revelar">Predict before you reveal</span> {bi("span", pr["q_en"], pr["q_es"])}</p>
        <div class="tg-btn-row">
{opts}
        </div>
        <p class="tg-predict-verdict" data-tg-verdict hidden aria-live="polite" data-tg-reveal-en="{a(pr['reveal_en'])}" data-tg-reveal-es="{a(pr['reveal_es'])}"></p>
      </div>"""


def gps_instrument(page: dict) -> str:
    ins = page["instrument"]
    beta0 = 0.6
    gamma0 = light_clock_dilation(beta0)
    terms = gps_terms()
    poserr = gps_position_error_per_day_m(terms["net_us"])
    # Light clock: mirrors at y=90 and y=350 (L = 260 px); in motion the photon's path is a zigzag whose half-base is β·γ·L/2 per leg.
    L = 260.0
    half = beta0 * gamma0 * L / 2.0
    zig = f"M {180 - half:.1f} 350 L 180 90 L {180 + half:.1f} 350"
    # Orbit panel: Earth at (560, 250) r=58; orbit radius drawn on a compressed scale so the slider range fits.
    def orbit_px(a_m: float) -> float:
        return 72.0 + 150.0 * (a_m - R_EARTH) / (42164000.0 - R_EARTH)
    rpx = orbit_px(A_GPS)
    bar_scale = 3.2  # px per µs/day
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="gps" data-tg-gm="{GM_EARTH}" data-tg-rearth="{R_EARTH}" aria-labelledby="tg-instrument-heading-t02">
      <h2 id="tg-instrument-heading-t02" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 440" role="img" aria-labelledby="tg-stage-title-t02 tg-stage-desc-t02">
          <title id="tg-stage-title-t02">A light clock at rest and in motion, and the GPS clock budget computed from three constants</title>
          <desc id="tg-stage-desc-t02">Left: two mirrors with a photon bouncing between them; at rest the path is vertical, in motion it is a longer zigzag, so the tick takes longer by the Lorentz factor. Right: Earth, a satellite on its orbit, and three bars: the gravitational gain of the satellite clock, its velocity loss and the net, in microseconds per day; a fourth bar shows the pseudorange error after one uncorrected day.</desc>
          <defs>
            <radialGradient id="tg-earth-grad" cx="0.5" cy="0.5" r="0.5">
              <stop offset="0" stop-color="var(--tp-prussian)"/>
              <stop offset="1" stop-color="var(--tp-stone-deep)"/>
            </radialGradient>
          </defs>
          <text x="180" y="40" text-anchor="middle" font-size="11" font-weight="700" data-en="light clock · v/c = {beta0:.2f}" data-es="reloj de luz · v/c = {beta0:.2f}">light clock · v/c = {beta0:.2f}</text>
          <rect x="120" y="86" width="120" height="4" fill="var(--tp-ink)"/>
          <rect x="120" y="350" width="120" height="4" fill="var(--tp-ink)"/>
          <line class="tg-release-line" x1="180" y1="90" x2="180" y2="350"/>
          <text x="186" y="222" font-size="10" fill="var(--tp-slate)" data-en="at rest" data-es="en reposo">at rest</text>
          <path class="tg-worldline tg-zigzag" data-state="fall" d="{zig}"/>
          <circle class="tg-body tg-photon" cx="180" cy="90" r="6"/>
          <text x="180" y="376" text-anchor="middle" font-size="10" data-tg-read="gammalabel">tick × γ = {gamma0:.3f}</text>
          <text x="180" y="392" text-anchor="middle" font-size="9.5" fill="var(--tp-slate)" data-en="(same speed c, longer path)" data-es="(misma rapidez c, camino más largo)">(same speed c, longer path)</text>
          <circle cx="560" cy="250" r="58" fill="url(#tg-earth-grad)" stroke="var(--tp-ink)" stroke-width="1.2"/>
          <text x="560" y="254" text-anchor="middle" font-size="10" fill="var(--tp-vellum)" data-en="ground clock" data-es="reloj en tierra">ground clock</text>
          <circle class="tg-orbit" cx="560" cy="250" r="{rpx:.1f}" fill="none" stroke="var(--tp-rule-strong)" stroke-dasharray="4 4"/>
          <circle class="tg-satellite" cx="{560 + rpx:.1f}" cy="250" r="7" fill="var(--tp-minium)" stroke="var(--tp-vellum)" stroke-width="2"/>
          <text class="tg-sat-label" x="{560 + rpx + 12:.1f}" y="246" font-size="10" data-tg-read="alabel">a = {A_GPS / 1000:,.0f} km</text>
          <g class="tg-bars" transform="translate(380, 40)">
            <text x="0" y="0" font-size="10" font-weight="700" data-en="satellite clock, µs per day" data-es="reloj satelital, µs por día">satellite clock, µs per day</text>
            <rect class="tg-bar tg-bar-grav" x="0" y="10" width="{terms['grav_us'] * bar_scale:.1f}" height="12" fill="var(--tp-verdigris)"/>
            <text x="{terms['grav_us'] * bar_scale + 6:.1f}" y="20" font-size="10" data-tg-read="gravbar">+{terms['grav_us']:.1f} (potential)</text>
            <rect class="tg-bar tg-bar-vel" x="0" y="28" width="{abs(terms['vel_us']) * bar_scale:.1f}" height="12" fill="var(--tp-sienna)"/>
            <text x="{abs(terms['vel_us']) * bar_scale + 6:.1f}" y="38" font-size="10" data-tg-read="velbar">{terms['vel_us']:.1f} (speed)</text>
            <rect class="tg-bar tg-bar-net" x="0" y="46" width="{terms['net_us'] * bar_scale:.1f}" height="12" fill="var(--tp-prussian)"/>
            <text x="{terms['net_us'] * bar_scale + 6:.1f}" y="56" font-size="10" font-weight="700" data-tg-read="netbar">+{terms['net_us']:.1f} net</text>
          </g>
          <g class="tg-errbar" transform="translate(380, 392)">
            <text x="0" y="0" font-size="10" font-weight="700" data-en="pseudorange error after one uncorrected day" data-es="error de pseudodistancia tras un día sin corregir">pseudorange error after one uncorrected day</text>
            <rect x="0" y="8" width="480" height="10" fill="var(--tp-stone-deep)" stroke="var(--tp-rule)"/>
            <rect class="tg-bar tg-bar-err" x="0" y="8" width="0" height="10" fill="var(--tp-minium)"/>
            <text x="486" y="17" font-size="10" data-tg-read="errbar">0 km (corrected)</text>
          </g>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-beta-t02">
            <span data-en="Light-clock speed v/c" data-es="Rapidez del reloj de luz v/c">Light-clock speed v/c</span>
            <span data-tg-read="beta">{beta0:.2f}</span>
          </label>
          <input id="tg-beta-t02" data-tg-beta type="range" min="0" max="0.95" step="0.01" value="{beta0}">
          <label for="tg-orbit-t02">
            <span data-en="Orbit radius a (km)" data-es="Radio orbital a (km)">Orbit radius a (km)</span>
            <span data-tg-read="a">{A_GPS / 1000:,.0f}</span>
          </label>
          <input id="tg-orbit-t02" data-tg-orbit type="range" min="7000" max="42164" step="100" value="{round(A_GPS / 1000)}" aria-describedby="tg-status-t02">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and planted defect">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · leave the satellite clock uncorrected" data-es="⚡ Apagado · dejar el reloj satelital sin corregir">⚡ Knockout · leave the satellite clock uncorrected</button>
          <button type="button" class="tp-step-btn" data-tg-flip aria-pressed="false" data-en="Planted defect · correct it the wrong way" data-es="Defecto plantado · corregirlo al revés">Planted defect · correct it the wrong way</button>
          <button type="button" class="tp-step-btn" data-tg-replay data-en="Replay the tick" data-es="Repetir el tic">Replay the tick</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Lorentz factor γ of the light clock" data-es="Factor de Lorentz γ del reloj de luz">Lorentz factor γ of the light clock</span>
          <span class="tp-readout-v" data-tg-read="gamma">{gamma0:.4f}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Gravitational · velocity (µs/day)" data-es="Gravitatorio · velocidad (µs/día)">Gravitational · velocity (µs/day)</span>
          <span class="tp-readout-v" data-tg-read="terms">+{terms['grav_us']:.2f} · {terms['vel_us']:.2f}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Net, two ways (µs/day)" data-es="Neto, de dos maneras (µs/día)">Net, two ways (µs/day)</span>
          <span class="tp-readout-v" data-tg-read="net">+{terms['net_us']:.2f} · +{gps_schwarzschild_net():.2f}</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="Pseudorange error after one day" data-es="Error de pseudodistancia tras un día">Pseudorange error after one day</span>
          <span class="tp-readout-v" data-tg-read="poserr">0 km (corrected; {poserr / 1000:.1f} km if not)</span>
        </div>
      </div>
      <p id="tg-status-t02" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="Corrected: the satellite clock is pre-set to run slow by the net amount, so from the ground it keeps time with the ground clocks." data-es="Corregido: el reloj satelital se preajusta para atrasar la cantidad neta, así que desde tierra mantiene el tiempo con los relojes en tierra.">Corrected: the satellite clock is pre-set to run slow by the net amount, so from the ground it keeps time with the ground clocks.</p>
    </section>"""


def poisson_instrument(page: dict) -> str:
    ins = page["instrument"]
    mass = GM_EARTH / G_NEWTON
    sol = poisson_radial(mass, R_EARTH, 4.0 * R_EARTH, 400)
    cx, cy, rpx = 240.0, 230.0, 48.0
    rings = []
    for k in range(1, 8):
        rr = 1.0 + 0.4 * k  # in units of R, out to 3.8 R
        i = min(400, int(round(rr / 4.0 * 400)))
        depth = abs(sol["phi"][i]) / abs(sol["phi"][100])  # relative to the surface potential
        rings.append(f'<circle class="tg-ring" data-ring="{k}" cx="{cx}" cy="{cy}" r="{rpx * rr:.1f}" fill="none" stroke="var(--tp-prussian)" stroke-width="{3 + 6 * depth:.1f}" style="opacity:{0.15 + 0.6 * depth:.2f}"/>')
    pts = []
    for i in range(0, 401, 10):
        x = 30 + 420 * (sol["r"][i] / (4.0 * R_EARTH))
        y = 425 - 40 * (abs(sol["phi"][i]) / abs(sol["phi_center"]))
        pts.append(f'{"M" if i == 0 else "L"} {x:.1f} {y:.1f}')
    curve = " ".join(pts)
    fall0 = fall_two_bodies(0.0)
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="poisson" data-tg-gm="{GM_EARTH}" data-tg-rearth="{R_EARTH}" data-tg-gnewton="{G_NEWTON}" aria-labelledby="tg-instrument-heading-t03">
      <h2 id="tg-instrument-heading-t03" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 440" role="img" aria-labelledby="tg-stage-title-t03 tg-stage-desc-t03">
          <title id="tg-stage-title-t03">A mass and the clock-rate map around it from Poisson's equation, and two bodies of different composition falling together</title>
          <desc id="tg-stage-desc-t03">Left: a disc for the mass with concentric rings, darker and thicker where the potential is deeper and clocks run slower, and a small curve of the potential against radius below. Right: two bodies released from the same height above a ground line fall together; a readout gives their separation.</desc>
          <text x="{cx}" y="36" text-anchor="middle" font-size="11" font-weight="700" data-en="clock-rate map from ∇²Φ = 4πGρ" data-es="mapa de ritmo de relojes desde ∇²Φ = 4πGρ">clock-rate map from ∇²Φ = 4πGρ</text>
          <g class="tg-rings">{''.join(rings)}</g>
          <circle class="tg-mass" cx="{cx}" cy="{cy}" r="{rpx}" fill="var(--tp-ink)"/>
          <text class="tg-mass-label" x="{cx}" y="{cy + 4}" text-anchor="middle" font-size="10" fill="var(--tp-vellum)" data-tg-read="mlabel">M = 1.0 M⊕</text>
          <path class="tg-phi-curve" d="{curve}" fill="none" stroke="var(--tp-prussian)" stroke-width="2"/>
          <text x="30" y="436" font-size="9.5" fill="var(--tp-slate)" data-en="Φ(r) on the grid, centre to 4R" data-es="Φ(r) en la malla, del centro a 4R">Φ(r) on the grid, centre to 4R</text>
          <line class="tg-axis" x1="520" y1="400" x2="890" y2="400"/>
          <text x="890" y="418" text-anchor="end" font-size="10" data-en="surface" data-es="superficie">surface</text>
          <line class="tg-release-line" x1="520" y1="80" x2="890" y2="80"/>
          <text x="890" y="74" text-anchor="end" font-size="10" data-en="released together" data-es="soltados juntos">released together</text>
          <circle class="tg-body tg-body-a" cx="640" cy="80" r="9"/>
          <text x="640" y="62" text-anchor="middle" font-size="10">Ti</text>
          <circle class="tg-body tg-body-b" cx="770" cy="80" r="13"/>
          <text x="770" y="58" text-anchor="middle" font-size="10">Pt</text>
          <text x="705" y="436" text-anchor="middle" font-size="9.5" fill="var(--tp-slate)" data-tg-read="seplabel" data-en="separation drawn ×10⁴" data-es="separación dibujada ×10⁴">separation drawn ×10⁴</text>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-mass-t03">
            <span data-en="Source mass M (Earth masses)" data-es="Masa fuente M (masas terrestres)">Source mass M (Earth masses)</span>
            <span data-tg-read="m">1.0</span>
          </label>
          <input id="tg-mass-t03" data-tg-mass type="range" min="0.1" max="3" step="0.1" value="1" aria-describedby="tg-status-t03">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and planted defect">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · remove the source (M → 0)" data-es="⚡ Apagado · quitar la fuente (M → 0)">⚡ Knockout · remove the source (M → 0)</button>
          <button type="button" class="tp-step-btn" data-tg-flip aria-pressed="false" data-en="Planted defect · η = 10⁻³" data-es="Defecto plantado · η = 10⁻³">Planted defect · η = 10⁻³</button>
          <button type="button" class="tp-step-btn" data-tg-replay data-en="Replay the fall" data-es="Repetir la caída">Replay the fall</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Surface acceleration GM/R²" data-es="Aceleración en superficie GM/R²">Surface acceleration GM/R²</span>
          <span class="tp-readout-v" data-tg-read="gsurf">{G_NEWTON * mass / R_EARTH**2:.3f} m/s²</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Φ(0) / (GM/R), grid vs −1.5" data-es="Φ(0) / (GM/R), malla vs −1.5">Φ(0) / (GM/R), grid vs −1.5</span>
          <span class="tp-readout-v" data-tg-read="phi0">{sol['phi_center'] / (G_NEWTON * mass / R_EARTH):.4f}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Grid vs −GM/r outside, worst rel. error" data-es="Malla vs −GM/r afuera, peor error rel.">Grid vs −GM/r outside, worst rel. error</span>
          <span class="tp-readout-v" data-tg-read="griderr">{sol['worst_rel_err_exterior']:.1e}</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="Separation after 1 s (η)" data-es="Separación tras 1 s (η)">Separation after 1 s (η)</span>
          <span class="tp-readout-v" data-tg-read="sep">{fall0['separation_m']:.1e} m (η = 0)</span>
        </div>
      </div>
      <p id="tg-status-t03" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="Both bodies read the same map and fall as one: the geodesic equation has no term for what they are made of." data-es="Ambos cuerpos leen el mismo mapa y caen como uno: la ecuación geodésica no tiene término para lo que están hechos.">Both bodies read the same map and fall as one: the geodesic equation has no term for what they are made of.</p>
    </section>"""


def budget_table(page: dict) -> str:
    b = gps_uncertainty_budget()
    rows = "\n".join(
        f'            <tr><td>{t(r["input"])}</td><td><code>{r["value"]:.9g}</code></td><td><code>{r["sigma"]:.3g}</code></td><td><code>{r["contribution_us"]:.3f}</code></td></tr>'
        for r in b["rows"]
    )
    return f"""        <h3 id="budget" data-en="Uncertainty budget for the net term (metrology habit, GUM style)" data-es="Presupuesto de incertidumbre del término neto (hábito metrológico, estilo GUM)">Uncertainty budget for the net term (metrology habit, GUM style)</h3>
        {bi("p", "Each input's stated 1σ uncertainty is propagated numerically to the net term and the contributions are combined in quadrature. c is exact by definition. The ground clock's rotation, which the first-order sum leaves out and the Schwarzschild path includes, is listed for comparison.", "La incertidumbre 1σ declarada de cada entrada se propaga numéricamente al término neto y las contribuciones se combinan en cuadratura. c es exacta por definición. La rotación del reloj en tierra, que la suma de primer orden omite y el camino de Schwarzschild incluye, se lista para comparar.")}
        <div class="tp-table-wrap">
          <table class="tp-table tg-ledger-table" aria-label="Uncertainty budget for the GPS net clock term">
            <thead><tr>{bi("th", "Input", "Entrada")}{bi("th", "Value (SI)", "Valor (SI)")}{bi("th", "1σ", "1σ")}{bi("th", "Contribution to net (µs/day)", "Contribución al neto (µs/día)")}</tr></thead>
            <tbody>
{rows}
            <tr><td>{bi("strong", "Combined (quadrature)", "Combinada (cuadratura)")}</td><td></td><td></td><td><code>{b["combined_sigma_us"]:.3f}</code></td></tr>
            <tr><td>{bi("em", "Ground rotation, not in the first-order sum", "Rotación del suelo, no está en la suma de primer orden")}</td><td></td><td></td><td><code>{b["ground_rotation_effect_us"]:.3f}</code></td></tr>
            </tbody>
          </table>
        </div>
        {bi("p", b["note"], "c es exacta por definición; la excentricidad (periódica, de media cero) y el potencial geoide-frente-a-ecuador no están en el presupuesto y son la razón de la ventana de aceptación de ±0.7 µs/día.", "tg-how")}"""


def pw_instrument(page: dict) -> str:
    ins = page["instrument"]
    st = pw_history_state()
    d = st["d"]
    # Tiles: rows n = 0..d-1 (y), columns |+x>, |-x> ; opacity from the conditional probabilities weighted by the row weight
    tiles = []
    ty0, th = 60, 20
    for c in st["conditional"]:
        n = c["n"]
        for col, p in ((0, c["p_plus_x"]), (1, 1.0 - c["p_plus_x"])):
            x = 110 + col * 70
            tiles.append(f'<rect class="tg-tile" data-n="{n}" data-col="{col}" x="{x}" y="{ty0 + n * th}" width="60" height="{th - 2}" rx="3" fill="var(--tp-prussian)" style="opacity:{0.08 + 0.85 * p:.3f}"/>')
    # Plot: P(+x | t_n) dots and the cos^2 curve
    px0, px1, py0, py1 = 380, 880, 70, 370
    to_x = lambda n: px0 + (px1 - px0) * n / (d - 1)  # noqa: E731
    to_y = lambda p: py1 - (py1 - py0) * p  # noqa: E731
    curve = " ".join(f'{"M" if i == 0 else "L"} {to_x(i * (d - 1) / 200):.1f} {to_y(__import__("math").cos(st["eps"] * (i * (d - 1) / 200) / 2.0) ** 2):.1f}' for i in range(201))
    dots = "".join(f'<circle class="tg-pw-dot" data-n="{c["n"]}" cx="{to_x(c["n"]):.1f}" cy="{to_y(c["p_plus_x"]):.1f}" r="5" fill="var(--tp-minium)"/>' for c in st["conditional"])
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="pw" data-tg-d="{d}" data-tg-k="1" aria-labelledby="tg-instrument-heading-t07">
      <h2 id="tg-instrument-heading-t07" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 420" role="img" aria-labelledby="tg-stage-title-t07 tg-stage-desc-t07" data-px0="{px0}" data-px1="{px1}" data-py0="{py0}" data-py1="{py1}" data-ty0="{ty0}" data-th="{th}">
          <title id="tg-stage-title-t07">A stationary Page–Wootters state as a grid, and the Schrödinger curve its conditional probabilities trace</title>
          <desc id="tg-stage-desc-t07">Left: a grid with one row per clock reading and two columns for the qubit's plus-x and minus-x components; the shading does not change because the global state is stationary. Right: the probability of plus-x given each clock reading, dots on a cosine-squared curve. A different clock basis gives a flat line at one half.</desc>
          <text x="170" y="40" text-anchor="middle" font-size="11" font-weight="700" data-en="|Ψ⟩⟩ by clock reading (rows) and qubit part (columns)" data-es="|Ψ⟩⟩ por lectura del reloj (filas) y parte del qubit (columnas)">|Ψ⟩⟩ by clock reading (rows) and qubit part (columns)</text>
          <text x="140" y="56" text-anchor="middle" font-size="10">|+x⟩</text>
          <text x="210" y="56" text-anchor="middle" font-size="10">|−x⟩</text>
          <g class="tg-tiles">{''.join(tiles)}</g>
          <text class="tg-tile-label" x="60" y="{ty0 + 12}" font-size="10">t₀</text>
          <text class="tg-tile-label" x="60" y="{ty0 + (d - 1) * th + 12}" font-size="10">t₁₅</text>
          <rect class="tg-row-marker" x="104" y="{ty0 - 2}" width="142" height="{th + 2}" fill="none" stroke="var(--tp-minium)" stroke-width="2" rx="4"/>
          <line class="tg-axis" x1="{px0}" y1="{py0}" x2="{px0}" y2="{py1}"/>
          <line class="tg-axis" x1="{px0}" y1="{py1}" x2="{px1}" y2="{py1}"/>
          <text x="{px0 - 8}" y="{py0 + 4}" text-anchor="end" font-size="10">1</text>
          <text x="{px0 - 8}" y="{(py0 + py1) / 2 + 4:.0f}" text-anchor="end" font-size="10">½</text>
          <text x="{px0 - 8}" y="{py1 + 4}" text-anchor="end" font-size="10">0</text>
          <text x="{px1}" y="{py1 + 18}" text-anchor="end" font-size="11" data-en="clock reading tₙ" data-es="lectura del reloj tₙ">clock reading tₙ</text>
          <text x="{px0}" y="{py0 - 12}" font-size="11" data-tg-read="plotlabel" data-en="P(+x | tₙ) against cos²(ε tₙ/2)" data-es="P(+x | tₙ) frente a cos²(ε tₙ/2)">P(+x | tₙ) against cos²(ε tₙ/2)</text>
          <path class="tg-pw-curve" d="{curve}" fill="none" stroke="var(--tp-prussian)" stroke-width="2"/>
          <g class="tg-pw-dots">{dots}</g>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-n-t07">
            <span data-en="Clock reading n" data-es="Lectura del reloj n">Clock reading n</span>
            <span data-tg-read="n">0</span>
          </label>
          <input id="tg-n-t07" data-tg-n type="range" min="0" max="{d - 1}" step="1" value="0" aria-describedby="tg-status-t07">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and planted defect">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · read the clock in its energy basis" data-es="⚡ Apagado · leer el reloj en su base de energía">⚡ Knockout · read the clock in its energy basis</button>
          <button type="button" class="tp-step-btn" data-tg-flip aria-pressed="false" data-en="Planted defect · clock spectrum ignores the constraint" data-es="Defecto plantado · el espectro del reloj ignora la restricción">Planted defect · clock spectrum ignores the constraint</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="Constraint residual ‖Ĥ|Ψ⟩⟩‖" data-es="Residuo de la restricción ‖Ĥ|Ψ⟩⟩‖">Constraint residual ‖Ĥ|Ψ⟩⟩‖</span>
          <span class="tp-readout-v" data-tg-read="residual">{st['constraint_residual']:.1e}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="P(+x | tₙ) at the chosen reading" data-es="P(+x | tₙ) en la lectura elegida">P(+x | tₙ) at the chosen reading</span>
          <span class="tp-readout-v" data-tg-read="pn">{st['conditional'][0]['p_plus_x']:.4f}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="max |P − cos²(ε tₙ/2)|" data-es="máx |P − cos²(ε tₙ/2)|">max |P − cos²(ε tₙ/2)|</span>
          <span class="tp-readout-v" data-tg-read="dev">{st['max_dev_from_schroedinger']:.1e}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Time in this split" data-es="Tiempo en esta partición">Time in this split</span>
          <span class="tp-readout-v" data-tg-read="split" data-en="yes: cos² motion" data-es="sí: movimiento cos²">yes: cos² motion</span>
        </div>
      </div>
      <p id="tg-status-t07" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="Stationary whole, moving part: conditioning on the clock's time states recovers the Schrödinger curve exactly." data-es="Todo estacionario, parte en movimiento: condicionar a los estados de tiempo del reloj recupera la curva de Schrödinger exactamente.">Stationary whole, moving part: conditioning on the clock's time states recovers the Schrödinger curve exactly.</p>
    </section>"""


def zych_instrument(page: dict) -> str:
    ins = page["instrument"]
    T_hold, dh0 = 1.0, 1.0
    px0, px1, py0, py1 = 420, 880, 70, 360
    to_x = lambda dh: px0 + (px1 - px0) * dh / 10.0  # noqa: E731
    to_y = lambda v: py1 - (py1 - py0) * v  # noqa: E731
    curve = " ".join(f'{"M" if i == 0 else "L"} {to_x(i / 20):.1f} {to_y(zych_visibility(i / 20, T_hold, OMEGA_SR)):.1f}' for i in range(201))
    v0 = zych_visibility(dh0, T_hold, OMEGA_SR)
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="zych" data-tg-g="{G0}" aria-labelledby="tg-instrument-heading-t04">
      <h2 id="tg-instrument-heading-t04" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 420" role="img" aria-labelledby="tg-stage-title-t04 tg-stage-desc-t04" data-px0="{px0}" data-px1="{px1}" data-py0="{py0}" data-py1="{py1}">
          <title id="tg-stage-title-t04">Two interferometer arms at different heights with a clock on each, and the visibility against height difference</title>
          <desc id="tg-stage-desc-t04">Left: two horizontal arms one above the other, each with a clock face; the lower clock accumulates less proper time. Right: the interferometric visibility from one down to zero against the height difference from zero to ten metres, with a marker at the chosen setting.</desc>
          <text x="200" y="40" text-anchor="middle" font-size="11" font-weight="700" data-en="one clock, two heights" data-es="un reloj, dos alturas">one clock, two heights</text>
          <line class="tg-arm tg-arm-up" x1="60" y1="120" x2="340" y2="120" stroke="var(--tp-ink)" stroke-width="3"/>
          <line class="tg-arm tg-arm-down" x1="60" y1="300" x2="340" y2="300" stroke="var(--tp-ink)" stroke-width="3"/>
          <path d="M 40 210 L 60 120 M 40 210 L 60 300 M 340 120 L 360 210 M 340 300 L 360 210" fill="none" stroke="var(--tp-rule-strong)" stroke-dasharray="4 4"/>
          <circle class="tg-clock-face" cx="200" cy="120" r="22"/><line class="tg-clock-hand tg-hand-up" x1="200" y1="120" x2="200" y2="102"/>
          <circle class="tg-clock-face" cx="200" cy="300" r="22"/><line class="tg-clock-hand tg-hand-down" x1="200" y1="300" x2="200" y2="282"/>
          <line class="tg-release-line tg-dh-line" x1="380" y1="120" x2="380" y2="300"/>
          <text class="tg-dh-label" x="386" y="214" font-size="10" data-tg-read="dhlabel">Δh = {dh0:.1f} m</text>
          <text x="200" y="340" text-anchor="middle" font-size="10" fill="var(--tp-slate)" data-en="(clock hands exaggerated)" data-es="(manecillas exageradas)">(clock hands exaggerated)</text>
          <line class="tg-axis" x1="{px0}" y1="{py0}" x2="{px0}" y2="{py1}"/>
          <line class="tg-axis" x1="{px0}" y1="{py1}" x2="{px1}" y2="{py1}"/>
          <text x="{px0 - 8}" y="{py0 + 4}" text-anchor="end" font-size="10">1</text>
          <text x="{px0 - 8}" y="{py1 + 4}" text-anchor="end" font-size="10">0</text>
          <text x="{px1}" y="{py1 + 18}" text-anchor="end" font-size="11" data-en="height difference Δh (0 to 10 m)" data-es="diferencia de altura Δh (0 a 10 m)">height difference Δh (0 to 10 m)</text>
          <text x="{px0}" y="{py0 - 12}" font-size="11" data-en="visibility V = |cos(ω Δτ/2)|" data-es="visibilidad V = |cos(ω Δτ/2)|">visibility V = |cos(ω Δτ/2)|</text>
          <path class="tg-zych-curve" d="{curve}" fill="none" stroke="var(--tp-prussian)" stroke-width="2.5"/>
          <circle class="tg-zych-marker" cx="{to_x(dh0):.1f}" cy="{to_y(v0):.1f}" r="7" fill="var(--tp-minium)" stroke="var(--tp-vellum)" stroke-width="2"/>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-dh-t04"><span data-en="Height difference Δh (m)" data-es="Diferencia de altura Δh (m)">Height difference Δh (m)</span> <span data-tg-read="dh">{dh0:.1f}</span></label>
          <input id="tg-dh-t04" data-tg-dh type="range" min="0" max="10" step="0.1" value="{dh0}" aria-describedby="tg-status-t04">
          <label for="tg-T-t04"><span data-en="Hold time T (s)" data-es="Tiempo de espera T (s)">Hold time T (s)</span> <span data-tg-read="T">{T_hold:.1f}</span></label>
          <input id="tg-T-t04" data-tg-hold type="range" min="0.1" max="10" step="0.1" value="{T_hold}">
          <label for="tg-w-t04"><span data-en="Clock frequency log₁₀(ω/2π in Hz)" data-es="Frecuencia del reloj log₁₀(ω/2π en Hz)">Clock frequency log₁₀(ω/2π in Hz)</span> <span data-tg-read="logw">14.63</span></label>
          <input id="tg-w-t04" data-tg-logw type="range" min="13" max="16" step="0.01" value="14.63">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and planted defect">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · switch gravity off (g → 0)" data-es="⚡ Apagado · quitar la gravedad (g → 0)">⚡ Knockout · switch gravity off (g → 0)</button>
          <button type="button" class="tp-step-btn" data-tg-flip aria-pressed="false" data-en="Planted defect · a clock that never ticks (ω → 0)" data-es="Defecto plantado · un reloj que nunca marcha (ω → 0)">Planted defect · a clock that never ticks (ω → 0)</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Proper-time difference Δτ" data-es="Diferencia de tiempo propio Δτ">Proper-time difference Δτ</span>
          <span class="tp-readout-v" data-tg-read="dtau">{G0 * dh0 * T_hold / 299792458.0**2:.2e} s</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Phase ω Δτ / 2" data-es="Fase ω Δτ / 2">Phase ω Δτ / 2</span>
          <span class="tp-readout-v" data-tg-read="phase">{OMEGA_SR * G0 * dh0 * T_hold / 299792458.0**2 / 2:.3f} rad</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="Visibility V" data-es="Visibilidad V">Visibility V</span>
          <span class="tp-readout-v" data-tg-read="V">{v0:.4f}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="First zero: Δh·T" data-es="Primer cero: Δh·T">First zero: Δh·T</span>
          <span class="tp-readout-v" data-tg-read="zero">{zych_first_zero(OMEGA_SR):.1f} m·s</span>
        </div>
      </div>
      <p id="tg-status-t04" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="A proposal, not a result: the clock's two readings overlap less as Δh·T grows, and the interference fades by exactly that overlap." data-es="Una propuesta, no un resultado: las dos lecturas del reloj se solapan menos conforme crece Δh·T, y la interferencia se desvanece exactamente por ese solape.">A proposal, not a result: the clock's two readings overlap less as Δh·T grows, and the interference fades by exactly that overlap.</p>
    </section>"""


def plate_d(page: dict) -> str:
    code = page["code"]
    return f"""        <figure class="tp-distill-figure" role="group" aria-label="Plate {code}-D Visual Intuition Bridge">
          <svg class="tp-distill-svg" viewBox="0 0 920 228" role="img" aria-labelledby="tp-distill-title-t01">
            <title id="tp-distill-title-t01" data-en="Plate T.01-D Visual Intuition Bridge: from the marching line on wet grass to a clock-rate gradient versus a flattened gradient, and the fall at g that only one of them produces" data-es="Lámina T.01-D Puente de Intuición Visual: de la fila de marchantes en pasto mojado a un gradiente de ritmo de relojes frente a un gradiente aplanado, y la caída a g que solo uno de ellos produce">Plate T.01-D Visual Intuition Bridge: from the marching line on wet grass to a clock-rate gradient versus a flattened gradient, and the fall at g that only one of them produces</title>
            <rect x="6" y="6" width="908" height="216" rx="10" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
            <rect x="20" y="20" width="266" height="168" rx="8" fill="var(--tp-vellum)" stroke="var(--tp-prussian)" stroke-width="1.5"/>
            <text x="34" y="40" font-family="var(--font-mono, monospace)" font-size="8.8" font-weight="700" fill="var(--tp-prussian)" data-en="1 · EVERYDAY ANALOGY (T.01)" data-es="1 · ANALOGÍA COTIDIANA (T.01)">1 · EVERYDAY ANALOGY (T.01)</text>
            <text x="34" y="60" font-size="10.4" font-weight="700" fill="var(--tp-ink)" data-en="A line of marchers, wet grass on one side" data-es="Una fila de marchantes, pasto mojado a un lado">A line of marchers, wet grass on one side</text>
            <text x="34" y="78" font-size="9.1" fill="var(--tp-graphite)" data-en="The slow end covers less ground per step," data-es="El extremo lento avanza menos por paso,">The slow end covers less ground per step,</text>
            <text x="34" y="92" font-size="9.1" fill="var(--tp-graphite)" data-en="so the whole line curves toward it." data-es="así que toda la fila se curva hacia él.">so the whole line curves toward it.</text>
            <path d="M 40 150 C 100 150, 160 140, 250 110" fill="none" stroke="var(--tp-minium)" stroke-width="2.4"/>
            <path d="M 40 170 L 250 170" fill="none" stroke="var(--tp-rule-strong)" stroke-width="1.4" stroke-dasharray="4 3"/>
            <text x="150" y="184" text-anchor="middle" font-size="8.4" fill="var(--tp-graphite)" data-en="dry: straight · wet: curved" data-es="seco: recto · mojado: curvo">dry: straight · wet: curved</text>
            <path d="M 288 104 L 312 104" stroke="var(--tp-prussian)" stroke-width="2" stroke-dasharray="4 3"/>
            <polygon points="312,99 320,104 312,109" fill="var(--tp-prussian)"/>
            <rect x="322" y="20" width="276" height="168" rx="8" fill="var(--tp-vellum)" stroke="var(--tp-rule-strong)" stroke-width="1.5"/>
            <text x="336" y="40" font-family="var(--font-mono, monospace)" font-size="8.8" font-weight="700" fill="var(--tp-ink)" data-en="2 · ONE QUANTITY, TWO SETTINGS" data-es="2 · UNA CANTIDAD, DOS AJUSTES">2 · ONE QUANTITY, TWO SETTINGS</text>
            <rect x="334" y="48" width="252" height="60" rx="6" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.2"/>
            <text x="344" y="65" font-size="9.6" font-weight="700" fill="var(--tp-prussian)" data-en="▲ Gradient on: A′(z) = 2g/c²" data-es="▲ Gradiente activo: A′(z) = 2g/c²">▲ Gradient on: A′(z) = 2g/c²</text>
            <text x="344" y="80" font-size="8.7" fill="var(--tp-graphite)" data-en="Lower clocks run slower; the connection" data-es="Los relojes bajos van más lento; el término">Lower clocks run slower; the connection</text>
            <text x="344" y="93" font-size="8.7" fill="var(--tp-graphite)" data-en="term Γᶻₜₜ = A′/2 is the only thing left." data-es="de conexión Γᶻₜₜ = A′/2 es lo único que queda.">term Γᶻₜₜ = A′/2 is the only thing left.</text>
            <rect x="334" y="116" width="252" height="60" rx="6" fill="var(--tp-stone)" stroke="var(--tp-verdigris)" stroke-width="1.2"/>
            <text x="344" y="133" font-size="9.6" font-weight="700" fill="var(--tp-verdigris)" data-en="▼ Knockout: A′(z) = 0" data-es="▼ Apagado: A′(z) = 0">▼ Knockout: A′(z) = 0</text>
            <text x="344" y="148" font-size="8.7" fill="var(--tp-graphite)" data-en="Every clock at one rate; the equation" data-es="Cada reloj a un ritmo; la ecuación">Every clock at one rate; the equation</text>
            <text x="344" y="161" font-size="8.7" fill="var(--tp-graphite)" data-en="is d²z/dτ² = 0 and nothing moves." data-es="es d²z/dτ² = 0 y nada se mueve.">is d²z/dτ² = 0 and nothing moves.</text>
            <path d="M 600 104 L 624 104" stroke="var(--tp-verdigris)" stroke-width="2" stroke-dasharray="4 3"/>
            <polygon points="624,99 632,104 624,109" fill="var(--tp-verdigris)"/>
            <rect x="634" y="20" width="266" height="168" rx="8" fill="var(--tp-vellum)" stroke="var(--tp-verdigris)" stroke-width="1.5"/>
            <text x="648" y="39" font-family="var(--font-mono, monospace)" font-size="8.8" font-weight="700" fill="var(--tp-verdigris)" data-en="3 · WHAT THE VERIFIER DEMANDS" data-es="3 · LO QUE EXIGE EL VERIFICADOR">3 · WHAT THE VERIFIER DEMANDS</text>
            <rect x="646" y="52" width="242" height="54" rx="6" fill="var(--tp-stone)" stroke="var(--tp-verdigris)" stroke-width="1.2"/>
            <text x="656" y="68" font-family="var(--font-mono, monospace)" font-size="8.5" font-weight="700" fill="var(--tp-verdigris)" data-en="✓ FALLS AT g, NO FORCE TERM" data-es="✓ CAE A g, SIN TÉRMINO DE FUERZA">✓ FALLS AT g, NO FORCE TERM</text>
            <text x="656" y="82" font-size="8.5" fill="var(--tp-ink)">|2z(T)/T² + g| / g &lt; 10⁻⁶</text>
            <text x="656" y="95" font-size="8.5" fill="var(--tp-ink)" data-en="knockout: |a| &lt; 10⁻¹²" data-es="apagado: |a| &lt; 10⁻¹²">knockout: |a| &lt; 10⁻¹²</text>
            <rect x="646" y="118" width="242" height="54" rx="6" fill="var(--tp-stone)" stroke="var(--tp-minium)" stroke-width="1.2"/>
            <text x="656" y="134" font-family="var(--font-mono, monospace)" font-size="8.5" font-weight="700" fill="var(--tp-minium)" data-en="⚠ PLANTED DEFECT: SIGN FLIP" data-es="⚠ DEFECTO PLANTADO: SIGNO INVERTIDO">⚠ PLANTED DEFECT: SIGN FLIP</text>
            <text x="656" y="148" font-size="8.5" fill="var(--tp-ink)" data-en="A′ → −A′: the body rises at +g;" data-es="A′ → −A′: el cuerpo sube a +g;">A′ → −A′: the body rises at +g;</text>
            <text x="656" y="161" font-size="8.5" fill="var(--tp-ink)" data-en="the check must fail or the page does." data-es="la prueba debe fallar o falla la página.">the check must fail or the page does.</text>
            <text x="460" y="208" text-anchor="middle" font-family="var(--font-mono, monospace)" font-size="8.9" font-weight="700" fill="var(--tp-prussian)">PLATE T.01-D · VISUAL INTUITION BRIDGE → ds² = −A(z)c²dt² + dz² · A(z) = 1 + 2gz/c² · d²z/dτ² = −(A′/2)(c dt/dτ)²</text>
          </svg>
          <figcaption class="tp-distill-caption">
            {bi("span", "Plate T.01-D · Visual Intuition Bridge: the everyday analogy (left) sets up one quantity with two settings (centre), and the verifier's three demands (right) are what the knockout and the sign-flip buttons in the instrument above test.", "Lámina T.01-D · Puente de Intuición Visual: la analogía cotidiana (izquierda) plantea una cantidad con dos ajustes (centro), y las tres exigencias del verificador (derecha) son lo que prueban los botones de apagado y de signo invertido en el instrumento de arriba.")}
          </figcaption>
        </figure>"""


def spine(page: dict) -> str:
    blocks = []
    for i, (te, ts, be, bs) in enumerate(page["stages"], 1):
        blocks.append(f"""          <div class="tp-proof-stage-block">
            <h4>{bi("span", te, ts)}</h4>
            {bi("p", be, bs)}
          </div>""")
    return f"""        <section class="tp-proof-spine" aria-label="Formal derivation and verification spine">
          <article class="tp-proof-chapter" id="spine-t01">
            {bi("h3", "§ II.1 · The derivation the verifier runs, in four stages", "§ II.1 · La derivación que corre el verificador, en cuatro etapas")}
            <div class="tp-theorem-box" role="region" aria-label="Governing equations and verifier">
              <span class="tp-kicker" data-en="GEODESIC WITH NO FORCE TERM · TIME &amp; GRAVITY T.01" data-es="GEODÉSICA SIN TÉRMINO DE FUERZA · TIEMPO Y GRAVEDAD T.01">GEODESIC WITH NO FORCE TERM · TIME &amp; GRAVITY T.01</span>
              <p class="tp-theorem-eq"><code>d²z/dτ² = −(A′(z)/2)(c dt/dτ)²,  A(z) = 1 + 2gz/c²  ⇒  a = −g</code></p>
              <p class="tp-theorem-meta"><strong>Kernel:</strong> <code>tools/timegravity_kernel.py</code> · <strong>Verifier:</strong> <code>{page['verifier']}</code> · <strong>Generator:</strong> <code>{page['generator']}</code></p>
            </div>
{chr(10).join(blocks)}
          </article>
        </section>"""


def change_box(block: dict) -> str:
    items = "\n".join(f"            <li>{bi('span', en, es)}</li>" for en, es in block["items"])
    return f"""        <aside class="tg-change-box" role="note" aria-label="What would change this page">
          <span class="tp-plain-bridge-kicker" data-en="What would change this page" data-es="Qué cambiaría esta página">What would change this page</span>
          <ul>
{items}
          </ul>
        </aside>"""


def labels_legend() -> str:
    items = []
    for lab in LABELS:
        de, ds = LABEL_DEF[lab]
        # The legend's chips are decoration (class tg-claim-look, not tg-claim): no ledger id, no text, so the hub
        # keeps zero claim spans and the lint can assert that.
        items.append(
            f'            <li><span class="tg-label-chip tg-claim-look" data-tg-label="{lab}" data-tg-label-es="{a(LABEL_ES[lab])}" aria-hidden="true"></span> '
            f'{bi("span", de, ds)}</li>'
        )
    return "        <ul class=\"tg-label-legend\" aria-label=\"The six labels\">\n" + "\n".join(items) + "\n        </ul>"


def track_map(rel_res: str) -> str:
    items = []
    for i, m in enumerate(TRACK_MAP, 1):
        href = B._href(rel_res, "timegravity/" + (f"{m['slug']}/" if m["slug"] else ""))
        if m["built"]:
            title = f'<a href="{href}" data-en="{a(m["title_en"])}" data-es="{a(m["title_es"])}">{t(m["title_en"])}</a>'
            status = bi("span", "Live", "Publicada", "tg-map-status")
        else:
            title = bi("span", m["title_en"], m["title_es"])
            status = bi("span", "In preparation", "En preparación", "tg-map-status")
        items.append(f"""          <li data-built="{str(m['built']).lower()}">
            <span class="tg-map-order" aria-label="reading order">{i}/9</span>
            <span class="tg-map-code">{m['code']}</span>
            <strong class="tg-map-title">{title}</strong>
            {bi("span", "Ends with: " + m["q_en"], "Termina con: " + m["q_es"], "tg-map-q")}
            {status}
          </li>""")
    return "        <ol class=\"tg-track-map\" aria-label=\"The nine pages in reading order\">\n" + "\n".join(items) + "\n        </ol>"


def ledger_table(page: dict) -> str:
    rows = []
    fetched_dates = set()
    for rid in page["ledger_ids"]:
        r = ROWS[rid]
        rec = CACHE.get("doi:" + r["doi"].lower(), {})
        sc = CACHE.get("scite:" + r["doi"].lower(), {})
        src = f"{rec.get('first_author', '')} ({r['year']}), {rec.get('journal', '')}"
        if sc.get("found"):
            fetched_dates.add(str(sc.get("fetched", "")))
            scite = (f'<a class="tp-cite-link" href="https://scite.ai/reports/{a(r["doi"])}" target="_blank" rel="noopener noreferrer" '
                     f'title="Scite report for {a(r["doi"])}">{sc.get("supporting", 0)} · {sc.get("contrasting", 0)} · {sc.get("mentioning", 0)}</a> '
                     f'<span class="tg-scite-n">/ {sc.get("citing_publications", 0):,}</span>')
        else:
            scite = bi("span", "not fetched", "sin consultar")
        rows.append(
            f'            <tr><td><code>{rid}</code></td><td><span class="tg-label-chip tg-claim-look" data-tg-label="{r["label"]}" data-tg-label-es="{a(LABEL_ES[r["label"]])}"></span></td>'
            f'<td>{t(src)}</td><td><a class="tp-cite-link" href="https://doi.org/{a(r["doi"])}" target="_blank" rel="noopener noreferrer">{t(r["doi"])}</a></td>'
            f'<td>{t(r["collaboration"])}</td><td>{r["kind"]}</td><td>{scite}</td><td>{r["review_by"]}</td></tr>'
        )
    fetched = ", ".join(sorted(fetched_dates)) or "—"
    return f"""        <h3 id="ledger" data-en="Grounding ledger rows cited on this page" data-es="Filas del libro de registro citadas en esta página">Grounding ledger rows cited on this page</h3>
        {bi("p", "Every row below resolves in the site's offline Crossref cache. The lint derives what each set of rows can carry; a person decided the label on each claim above. Rows pass a review date and the build fails until someone rereads the source.", "Cada fila de abajo resuelve en la caché Crossref sin conexión del sitio. El lint deriva lo que cada conjunto de filas puede sostener; una persona decidió la etiqueta de cada afirmación de arriba. Las filas tienen fecha de revisión y la construcción falla hasta que alguien relea la fuente.")}
        <div class="tp-table-wrap">
          <table class="tp-table tg-ledger-table" aria-label="Ledger rows for {page['code']}">
            <thead><tr>
              {bi("th", "Row", "Fila")}{bi("th", "Row label", "Etiqueta de la fila")}{bi("th", "Source", "Fuente")}<th>DOI</th>{bi("th", "Collaboration", "Colaboración")}{bi("th", "Kind", "Tipo")}{bi("th", "Scite: supporting · contrasting · mentioning / citing", "Scite: apoyo · contraste · mención / citantes")}{bi("th", "Review by", "Revisar antes de")}
            </tr></thead>
            <tbody>
{chr(10).join(rows)}
            </tbody>
          </table>
        </div>
        {bi("p", f"Scite column: [observed: Scite ML citation classification, accessed {fetched}] via Scite's public tallies endpoint. The counts are a classifier's output over indexed citation statements, an evidence-synthesis habit borrowed from medicine; they never replace reading the source, and a row with more contrasting than supporting statements is flagged for a human re-read in the label checklist.", f"Columna Scite: [observado: clasificación de citas por aprendizaje automático de Scite, consultada {fetched}] mediante el punto público de conteos de Scite. Los conteos son la salida de un clasificador sobre enunciados de cita indexados, un hábito de síntesis de evidencia tomado de la medicina; nunca sustituyen leer la fuente, y una fila con más enunciados de contraste que de apoyo se marca para relectura humana en la lista de verificación de etiquetas.", "tg-how")}"""


def render_sections(page: dict, rel_res: str) -> str:
    out = []
    for block in page["sections"]:
        kind = block["type"]
        if kind == "h2":
            out.append(f'        <h2 id="{block["id"]}" class="tp-h2" data-en="{a(block["en"])}" data-es="{a(block["es"])}">{t(block["en"])}</h2>')
        elif kind == "p":
            out.append("        " + para(block))
        elif kind == "bridge":
            inner = "\n".join("          " + para(p) for p in block["paras"])
            out.append(f"""        <div class="tp-plain-bridge-box" role="note" aria-label="In plain words">
          <span class="tp-plain-bridge-kicker" data-en="{a(block['kicker_en'])}" data-es="{a(block['kicker_es'])}">{t(block['kicker_en'])}</span>
{inner}
        </div>""")
        elif kind == "analogy":
            inner = "\n".join("          " + para(p) for p in block["paras"])
            out.append(f"""        <div class="tp-analogy-box" role="region" aria-label="Everyday intuition and controls primer">
          <span class="tp-plain-bridge-kicker" data-en="{a(block['kicker_en'])}" data-es="{a(block['kicker_es'])}">{t(block['kicker_en'])}</span>
{inner}
        </div>""")
        elif kind == "plate_d":
            out.append(plate_d(page))
        elif kind == "equation":
            out.append(f'        <p class="tg-equation"><code>{t(block["text"])}</code></p>')
        elif kind == "spine":
            out.append(spine(page))
        elif kind == "change_box":
            out.append(change_box(block))
        elif kind == "ledger_table":
            out.append(ledger_table(page))
        elif kind == "budget_table":
            out.append(budget_table(page))
        elif kind == "labels":
            out.append(labels_legend())
        elif kind == "track_map":
            out.append(track_map(rel_res))
        else:
            raise ValueError(f"unknown block type {kind}")
    return "\n".join(out)


def sidenotes(page: dict) -> str:
    notes = []
    for ke, ks, be, bs in page.get("sidenotes", []):
        notes.append(f'        <div class="tp-sidenote"><span class="tp-sidenote-id" data-en="{a(ke)}" data-es="{a(ks)}">{t(ke)}</span>{bi("span", be, bs)}</div>')
    spec = ""
    if page.get("verifier"):
        spec = f"""        <div class="tp-spec-plate">
          <span class="tp-spec-tag" data-en="Central number &amp; verifier" data-es="Número central y verificador">Central number &amp; verifier</span>
          {bi("h3", page["central_number_en"], page["central_number_es"], "tp-spec-title")}
          <p class="tp-spec-meta"><code>{page['verifier']}</code> · PASS · <code>--planted-defect</code> → FAIL</p>
        </div>"""
    return "\n".join(notes + [spec])


def sources_list(page: dict) -> str:
    if not page.get("sources"):
        return ""
    items = []
    for text_, doi in page["sources"]:
        items.append(
            f'          <li>{t(text_)} DOI <a class="tp-cite-link" href="https://doi.org/{a(doi)}" target="_blank" rel="noopener noreferrer">DOI {t(doi)}</a> '
            f'<a class="tp-scite-badge-link" href="https://scite.ai/reports/{a(doi)}" target="_blank" rel="noopener noreferrer" title="Inspect Scite Smart Citation report for {a(doi)}">[Scite &#8599;]</a></li>'
        )
    return f"""        <h3 data-en="Primary sources" data-es="Fuentes primarias">Primary sources</h3>
        <ol class="tp-sources-list">
{chr(10).join(items)}
        </ol>"""


def skill_box(page: dict) -> str:
    if not page.get("skill"):
        return ""
    skill_md = (ROOT / page["skill"]).read_text(encoding="utf-8")
    verify_src = (ROOT / page["verifier"]).read_text(encoding="utf-8")
    skill_fn = page.get("skill_filename", "timegravity-t01-time-slope-geodesic.SKILL.md")
    py_fn = Path(page["verifier"]).name
    return f"""        <section class="tp-skill-box" aria-label="Downloadable SKILL.md companion and Python verifier">
          <div class="tp-skill-header">
            <span class="tp-skill-kicker" data-en="SKILL.md companion &amp; Python verifier · {page['code']}" data-es="Compañero SKILL.md y verificador en Python · {page['code']}">SKILL.md companion &amp; Python verifier · {page['code']}</span>
            <span class="tp-skill-compat" data-en="Works with Claude Code · Copilot · Cursor · Antigravity · Codex · Ollama · Python 3" data-es="Compatible con Claude Code · Copilot · Cursor · Antigravity · Codex · Ollama · Python 3">Works with Claude Code · Copilot · Cursor · Antigravity · Codex · Ollama · Python 3</span>
          </div>
          {bi("p", f"Rebuild this instrument locally and run the verifier as the acceptance gate: python {page['generator']} then python {page['verifier']} (and --planted-defect, which must fail). Then python tools/check_timegravity_labels.py.", f"Reconstruye este instrumento localmente y corre el verificador como puerta de aceptación: python {page['generator']} y luego python {page['verifier']} (y --planted-defect, que debe fallar). Después python tools/check_timegravity_labels.py.", "tp-skill-desc")}
          <div class="tp-skill-actions">
            <button class="tp-skill-btn" type="button" data-skill-download="{skill_fn}" data-en="Download SKILL.md ({skill_fn})" data-es="Descargar SKILL.md ({skill_fn})">Download SKILL.md ({skill_fn})</button>
            <button class="tp-skill-btn tp-skill-btn-secondary" type="button" data-skill-copy="true" data-en="Copy SKILL.md" data-es="Copiar SKILL.md">Copy SKILL.md</button>
            <button class="tp-skill-btn tp-skill-btn-secondary" type="button" data-py-download="{py_fn}" data-en="Download Python Verifier ({py_fn})" data-es="Descargar verificador en Python ({py_fn})">Download Python Verifier ({py_fn})</button>
          </div>
          <details class="tp-skill-source-details">
            <summary class="tp-skill-source-summary"><span data-en="Show the " data-es="Mostrar el código de ">Show the </span><code>SKILL.md</code><span data-en=" source" data-es=" fuente"> source</span></summary>
            <pre class="tp-skill-pre"><code data-skill-source>{t(skill_md)}</code></pre>
          </details>
          <details class="tp-skill-source-details">
            <summary class="tp-skill-source-summary"><span data-en="Show the verifier " data-es="Mostrar el verificador ">Show the verifier </span><code>{py_fn}</code></summary>
            <pre class="tp-skill-pre"><code data-py-source>{t(verify_src)}</code></pre>
          </details>
        </section>"""


def neighbours(page: dict) -> tuple[dict | None, dict | None]:
    """Previous and next entries of TRACK_MAP in reading order (the hub is first)."""
    idx = next(i for i, m in enumerate(TRACK_MAP) if m["code"] == page["code"])
    prev = TRACK_MAP[idx - 1] if idx > 0 else None
    nxt = TRACK_MAP[idx + 1] if idx + 1 < len(TRACK_MAP) else None
    return prev, nxt


def open_question(page: dict) -> str:
    _prev, nx = neighbours(page)
    nxt_en = f"Next: {nx['code']} · {nx['title_en']}" + ("" if nx["built"] else " (in preparation)")
    nxt_es = f"Siguiente: {nx['code']} · {nx['title_es']}" + ("" if nx["built"] else " (en preparación)")
    return f"""        <section class="tg-open-question" aria-label="The open question this page ends with">
          <p class="tp-kicker" data-en="This page ends with one open question" data-es="Esta página termina con una pregunta abierta">This page ends with one open question</p>
          {bi("p", page["open_question_en"], page["open_question_es"])}
          {bi("p", nxt_en, nxt_es, "tg-next")}
        </section>"""


def pager(page: dict, rel_res: str) -> str:
    pv, nx = neighbours(page)
    if pv is None:
        prev = '<span class="tp-pager-link tp-pager-empty" aria-hidden="true"></span>'
    else:
        prev_href = "timegravity/" + (f"{pv['slug']}/" if pv["slug"] else "")
        prev_lbl_en = "&larr; Hub" if not pv["slug"] else "&larr; Previous"
        prev_lbl_es = "&larr; Inicio" if not pv["slug"] else "&larr; Anterior"
        prev = (f'<a class="tp-pager-link tp-pager-prev" href="{B._href(rel_res, prev_href)}" rel="prev"><span class="tp-pager-dir">'
                f'<span data-en="{prev_lbl_en}" data-es="{prev_lbl_es}">{prev_lbl_en}</span> · {pv["code"]}</span>'
                f'<strong data-en="{a(pv["title_en"])}" data-es="{a(pv["title_es"])}">{t(pv["title_en"])}</strong></a>')
    next_live = None
    if nx is not None and not nx.get("built"):
        idx = next((i for i, m in enumerate(TRACK_MAP) if m["code"] == page["code"]), -1)
        for m in (TRACK_MAP[idx + 1:] if idx >= 0 else []):
            if m["built"] and m["slug"]:
                next_live = m
                break
    if nx is not None and nx.get("built"):
        nxt = (f'<a class="tp-pager-link tp-pager-next" href="{B._href(rel_res, "timegravity/" + nx["slug"] + "/")}" rel="next"><span class="tp-pager-dir">'
               f'<span data-en="Next &rarr;" data-es="Siguiente &rarr;">Next &rarr;</span> · {nx["code"]}</span>'
               f'<strong data-en="{a(nx["title_en"])}" data-es="{a(nx["title_es"])}">{t(nx["title_en"])}</strong></a>')
    elif next_live is not None and nx is not None:
        nxt = (f'<a class="tp-pager-link tp-pager-next" href="{B._href(rel_res, "timegravity/" + next_live["slug"] + "/")}" rel="next"><span class="tp-pager-dir">'
               f'<span data-en="Next live page &rarr; ({nx["code"]} in preparation)" data-es="Siguiente publicada &rarr; ({nx["code"]} en preparación)">Next live page &rarr; ({nx["code"]} in preparation)</span> · {next_live["code"]}</span>'
               f'<strong data-en="{a(next_live["title_en"])}" data-es="{a(next_live["title_es"])}">{t(next_live["title_en"])}</strong></a>')
    elif nx is not None:
        nxt = (f'<span class="tp-pager-link tp-pager-next" aria-disabled="true"><span class="tp-pager-dir">'
               f'<span data-en="Next (in preparation)" data-es="Siguiente (en preparación)">Next (in preparation)</span> · {nx["code"]}</span>'
               f'<strong data-en="{a(nx["title_en"])}" data-es="{a(nx["title_es"])}">{t(nx["title_en"])}</strong></span>')
    else:
        nxt = '<span class="tp-pager-link tp-pager-empty" aria-hidden="true"></span>'
    all_link = (f'<p class="tp-pager-all"><a href="{B._href(rel_res, "timegravity/")}" data-en="All Time &amp; Gravity pages &rarr;" '
                f'data-es="Todas las páginas de Tiempo y Gravedad &rarr;">All Time &amp; Gravity pages &rarr;</a></p>')
    return f"""    <nav class="tp-pager" aria-label="More in Time and Gravity">
      {prev}
      {nxt}
    </nav>
    {all_link}"""


def render_page(page: dict, catalog: dict, lang: str = "en") -> str:
    es = lang == "es"
    slug = page["slug"]
    path = "timegravity/" + (f"{slug}/" if slug else "")
    rel_res = "../.." if slug else ".."
    rel_root = rel_res + "/.."
    t_en, d_en, t_es, d_es = page["seo"]
    if slug:
        title = f"{t_es if es else t_en} | {BRAND}"
    else:
        title = t_es if es else t_en
        title = title if title.endswith(BRAND) else f"{title} | {BRAND}"
    desc = d_es if es else d_en
    canon = B.page_url(path, lang)
    image = f"https://informatico.ai/plates/{plate_slug(page)}.png"
    crumbs = [("Informatico.ai", B.page_url("", lang)), (TRACK_TITLE_ES if es else TRACK_TITLE_EN, B.page_url("timegravity/", lang))]
    if slug:
        crumbs.append((page["code"], canon))
        ld = B._ld("ScholarlyArticle", t_es if es else t_en, desc, canon, lang, image=image,
                   date_published=page.get("date", TRACK_DATE), date_modified=page.get("date", TRACK_DATE), crumbs=crumbs)
    else:
        ld = B._ld("CollectionPage", t_es if es else t_en, desc, canon, lang, image=image, crumbs=crumbs)
    head = B.render_head(title, desc, path, "article" if slug else "website", image, rel_root, rel_res, ld, lang)
    head = head.replace(
        '  <link rel="modulepreload"',
        f'  <link rel="stylesheet" href="{rel_res}/timegravity.css">\n  <link rel="modulepreload"',
        1,
    )

    jump = [("#instrument" if slug else "#question", "Instrument", "Instrumento")]
    for block in page["sections"]:
        if block["type"] == "h2":
            jump.append((f"#{block['id']}", block.get("short_en", block["en"]), block.get("short_es", block["es"])))
    # Own classes, not tp-act-pill: theme-plate.mjs relabels .tp-act-jump-bar pills with the Folio act names.
    jump_html = "\n".join(f'      <a class="tg-jump-pill" href="{h}" data-en="{a(e)}" data-es="{a(s)}">{t(e)}</a>' for h, e, s in jump)

    kind = (page.get("instrument") or {}).get("kind", "slope")
    if not slug:
        instrument = worldline_instrument(page)
    elif kind == "gps":
        instrument = gps_instrument(page)
    elif kind == "poisson":
        instrument = poisson_instrument(page)
    elif kind == "pw":
        instrument = pw_instrument(page)
    elif kind == "zych":
        instrument = zych_instrument(page)
    else:
        instrument = slope_instrument(page, rel_res)
    ai_line = bi("p", page["ai_line_en"], page["ai_line_es"], "tg-ai-line") if page.get("ai_line_en") else ""
    order = bi("span", page["order_label_en"], page["order_label_es"])
    rt = bi("span", page["reading_time_en"], page["reading_time_es"])

    return f"""{head}
<body class="tp-body tp-page-folio tg-page">
{B.render_masthead(rel_res, "timegravity", lang)}
{B.render_contents_dialog(rel_res, catalog)}
  <main id="main" class="tp-shell" tabindex="-1">
{breadcrumb(rel_res, page)}
<div id="tp-folio-mount" data-folio-id="{page['code']}" data-folio-slug="{plate_slug(page)}">
    <section class="tp-hero">
      <p class="tp-kicker">{bi("span", page["kicker_en"], page["kicker_es"])} · {page['code']} · {order} · {rt}</p>
      <h1 class="tp-h1" data-en="{a(page['title_en'])}" data-es="{a(page['title_es'])}">{t(page['title_en'])}</h1>
      {bi("p", page["standfirst_en"], page["standfirst_es"], "tp-standfirst")}
{boundary_banner()}
    </section>
{lead_figure(page, rel_res, es)}
    <nav class="tg-jump-bar" aria-label="Sections of this page">
{jump_html}
    </nav>
{instrument}
    <section class="tp-folio-layout" aria-label="Essay">
      <div class="tp-prose">
{render_sections(page, rel_res)}
        {ai_line}
{skill_box(page)}
{sources_list(page)}
{open_question(page)}
      </div>
      <aside class="tp-rail" aria-label="{page['code']} margin notes">
{sidenotes(page)}
      </aside>
    </section>
</div>
{pager(page, rel_res)}
{B.render_site_footer(rel_res)}
  </main>
  <script type="module" src="{rel_res}/modules/main.mjs"></script>
  <script type="module" src="{rel_res}/modules/timegravity-slope.mjs"></script>
</body>
</html>
"""


def write_pages(catalog: dict | None = None) -> list[Path]:
    catalog = catalog or B.update_catalogs()
    written = []
    for page in PAGES:
        slug = page["slug"]
        rel = Path("timegravity") / slug if slug else Path("timegravity")
        en_dir = RESEARCH / rel
        es_dir = RESEARCH / B.ES_PREFIX.strip("/") / rel
        en_dir.mkdir(parents=True, exist_ok=True)
        es_dir.mkdir(parents=True, exist_ok=True)
        en_html = render_page(page, catalog, "en")
        (en_dir / "index.html").write_text(en_html, encoding="utf-8")
        (es_dir / "index.html").write_text(B.to_spanish_static(render_page(page, catalog, "es")), encoding="utf-8")
        written += [en_dir / "index.html", es_dir / "index.html"]
    return written


def main() -> int:
    catalog = B.update_catalogs()
    written = write_pages(catalog)
    # The track's entries on the cover, the sitemap and llms.txt live in the main builder, like the Toolbox's.
    (RESEARCH / "index.html").write_text(B.render_hub_index(catalog), encoding="utf-8")
    (RESEARCH / B.ES_PREFIX.strip("/") / "index.html").write_text(B.to_spanish_static(B.render_hub_index(catalog, "es")), encoding="utf-8")
    (RESEARCH / "sitemap.xml").write_text(B.render_research_sitemap(catalog), encoding="utf-8")
    (RESEARCH / "llms.txt").write_text(B.render_llms_txt(catalog), encoding="utf-8")
    print(f"PASS: Built {len(written)} Time & Gravity pages ({len(PAGES)} pages × EN/ES-MX) + cover, sitemap.xml and llms.txt entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
