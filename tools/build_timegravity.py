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
from timegravity_kernel import G0, integrate  # noqa: E402

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


def lead_figure(page: dict, rel_res: str) -> str:
    slug = plate_slug(page)
    code = page["code"]
    alt_en = (f"Diagram for {code}: a worldline drawn across a shaded column that shows how fast a clock runs at each height, "
              "darker meaning slower. Drawn by a script from the page's own numbers; no text, no photograph.")
    if code == "T.01":
        cap_en = ("Plate T.01-V · The worldline the kernel integrates: a body released at rest drifts toward the slower clocks, "
                  "faster and faster, with no force term in the equation. Drawn by timegravity/make_plates.py from tools/timegravity_kernel.py.")
        cap_es = ("Lámina T.01-V · La línea de mundo que integra el núcleo: un cuerpo soltado en reposo deriva hacia los relojes más lentos, "
                  "cada vez más rápido, sin término de fuerza en la ecuación. Dibujada por timegravity/make_plates.py desde tools/timegravity_kernel.py.")
    else:
        cap_en = ("Plate T.00-V · A worldline across a clock-rate gradient, with a marker for the 'now' the intuition imagines. "
                  "General relativity has the line and the shading; it has no marker. Drawn by timegravity/make_plates.py.")
        cap_es = ("Lámina T.00-V · Una línea de mundo sobre un gradiente de ritmo de relojes, con un marcador para el 'ahora' que la intuición imagina. "
                  "La relatividad general tiene la línea y el sombreado; no tiene marcador. Dibujada por timegravity/make_plates.py.")
    return f"""    <figure class="tp-editorial-figure" data-lead-figure role="group" aria-label="Lead diagram for {code}">
      <img class="tp-editorial-img" src="{rel_res}/plates/{slug}.png?v={png_sha8(slug)}" width="1280" height="720" alt="{a(alt_en)}" loading="eager" fetchpriority="high" decoding="async">
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
    to_x = lambda tt: P["x0"] + (P["x1"] - P["x0"]) * tt  # noqa: E731
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
          <title id="tg-stage-title-t01">Worldline of a body released at rest in a metric where only the rate of time varies with height</title>
          <desc id="tg-stage-desc-t01">Left, a shaded column: clocks lower down run slower. Right, height against coordinate time: the body starts at height zero and falls 4.9 metres in one second, a parabola with no force term in the equation.</desc>
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
          <title id="tg-stage-title-t00">A worldline across a clock-rate gradient with a movable marker</title>
          <desc id="tg-stage-desc-t00">Height against coordinate time. A shaded column shows clocks lower down running slower. One curve, the worldline, and one dot on it, the imagined now, which the slider moves. The physics has the curve and the shading; it has no dot.</desc>
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


def plate_d(page: dict) -> str:
    code = page["code"]
    return f"""        <figure class="tp-distill-figure" role="group" aria-label="Plate {code}-D Visual Intuition Bridge">
          <svg class="tp-distill-svg" viewBox="0 0 920 228" role="img" aria-labelledby="tp-distill-title-t01">
            <title id="tp-distill-title-t01">Plate T.01-D Visual Intuition Bridge: from the marching line on wet grass to a clock-rate gradient versus a flattened gradient, and the fall at g that only one of them produces</title>
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
    for rid in page["ledger_ids"]:
        r = ROWS[rid]
        rec = CACHE.get("doi:" + r["doi"].lower(), {})
        src = f"{rec.get('first_author', '')} ({r['year']}), {rec.get('journal', '')}"
        rows.append(
            f'            <tr><td><code>{rid}</code></td><td><span class="tg-label-chip tg-claim-look" data-tg-label="{r["label"]}" data-tg-label-es="{a(LABEL_ES[r["label"]])}"></span></td>'
            f'<td>{t(src)}</td><td><a class="tp-cite-link" href="https://doi.org/{a(r["doi"])}" target="_blank" rel="noopener noreferrer">{t(r["doi"])}</a></td>'
            f'<td>{t(r["collaboration"])}</td><td>{r["kind"]}</td><td>{r["review_by"]}</td></tr>'
        )
    return f"""        <h3 id="ledger" data-en="Grounding ledger rows cited on this page" data-es="Filas del libro de registro citadas en esta página">Grounding ledger rows cited on this page</h3>
        {bi("p", "Every row below resolves in the site's offline Crossref cache. The lint derives what each set of rows can carry; a person decided the label on each claim above. Rows pass a review date and the build fails until someone rereads the source.", "Cada fila de abajo resuelve en la caché Crossref sin conexión del sitio. El lint deriva lo que cada conjunto de filas puede sostener; una persona decidió la etiqueta de cada afirmación de arriba. Las filas tienen fecha de revisión y la construcción falla hasta que alguien relea la fuente.")}
        <div class="tp-table-wrap">
          <table class="tp-table tg-ledger-table" aria-label="Ledger rows for {page['code']}">
            <thead><tr>
              {bi("th", "Row", "Fila")}{bi("th", "Row label", "Etiqueta de la fila")}{bi("th", "Source", "Fuente")}<th>DOI</th>{bi("th", "Collaboration", "Colaboración")}{bi("th", "Kind", "Tipo")}{bi("th", "Review by", "Revisar antes de")}
            </tr></thead>
            <tbody>
{chr(10).join(rows)}
            </tbody>
          </table>
        </div>"""


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
    skill_fn = "timegravity-t01-time-slope-geodesic.SKILL.md"
    py_fn = Path(page["verifier"]).name
    return f"""        <section class="tp-skill-box" aria-label="Downloadable SKILL.md companion and Python verifier">
          <div class="tp-skill-header">
            <span class="tp-skill-kicker">SKILL.md companion &amp; Python verifier · {page['code']}</span>
            <span class="tp-skill-compat">Works with Claude Code · Copilot · Cursor · Antigravity · Codex · Ollama · Python 3</span>
          </div>
          {bi("p", f"Rebuild this instrument locally and run the verifier as the acceptance gate: python {page['generator']} then python {page['verifier']} (and --planted-defect, which must fail). Then python tools/check_timegravity_labels.py.", f"Reconstruye este instrumento localmente y corre el verificador como puerta de aceptación: python {page['generator']} y luego python {page['verifier']} (y --planted-defect, que debe fallar). Después python tools/check_timegravity_labels.py.", "tp-skill-desc")}
          <div class="tp-skill-actions">
            <button class="tp-skill-btn" type="button" data-skill-download="{skill_fn}">Download SKILL.md ({skill_fn})</button>
            <button class="tp-skill-btn tp-skill-btn-secondary" type="button" data-skill-copy="true">Copy SKILL.md</button>
            <button class="tp-skill-btn tp-skill-btn-secondary" type="button" data-py-download="{py_fn}">Download Python Verifier ({py_fn})</button>
          </div>
          <details class="tp-skill-source-details">
            <summary class="tp-skill-source-summary">Show the <code>SKILL.md</code> source</summary>
            <pre class="tp-skill-pre"><code data-skill-source>{t(skill_md)}</code></pre>
          </details>
          <details class="tp-skill-source-details">
            <summary class="tp-skill-source-summary">Show the verifier <code>{py_fn}</code></summary>
            <pre class="tp-skill-pre"><code data-py-source>{t(verify_src)}</code></pre>
          </details>
        </section>"""


def open_question(page: dict) -> str:
    nxt_en = f"Next: {page['next_code']} · {page['next_title_en']}" + ("" if page.get("next_built") else " (in preparation)")
    nxt_es = f"Siguiente: {page['next_code']} · {page['next_title_es']}" + ("" if page.get("next_built") else " (en preparación)")
    return f"""        <section class="tg-open-question" aria-label="The open question this page ends with">
          <p class="tp-kicker" data-en="This page ends with one open question" data-es="Esta página termina con una pregunta abierta">This page ends with one open question</p>
          {bi("p", page["open_question_en"], page["open_question_es"])}
          {bi("p", nxt_en, nxt_es, "tg-next")}
        </section>"""


def pager(page: dict, rel_res: str) -> str:
    if page["slug"] == "":
        prev = '<span class="tp-pager-link tp-pager-empty" aria-hidden="true"></span>'
    else:
        prev = (f'<a class="tp-pager-link tp-pager-prev" href="{B._href(rel_res, "timegravity/")}" rel="prev"><span class="tp-pager-dir">'
                f'<span data-en="&larr; Hub" data-es="&larr; Inicio">&larr; Hub</span> · {page["prev_code"]}</span>'
                f'<strong data-en="{a(page["prev_title_en"])}" data-es="{a(page["prev_title_es"])}">{t(page["prev_title_en"])}</strong></a>')
    if page.get("next_built"):
        nxt = (f'<a class="tp-pager-link tp-pager-next" href="{B._href(rel_res, "timegravity/" + page["next_slug"] + "/")}" rel="next"><span class="tp-pager-dir">'
               f'<span data-en="Next &rarr;" data-es="Siguiente &rarr;">Next &rarr;</span> · {page["next_code"]}</span>'
               f'<strong data-en="{a(page["next_title_en"])}" data-es="{a(page["next_title_es"])}">{t(page["next_title_en"])}</strong></a>')
    else:
        nxt = (f'<span class="tp-pager-link tp-pager-next" aria-disabled="true"><span class="tp-pager-dir">'
               f'<span data-en="Next (in preparation)" data-es="Siguiente (en preparación)">Next (in preparation)</span> · {page["next_code"]}</span>'
               f'<strong data-en="{a(page["next_title_en"])}" data-es="{a(page["next_title_es"])}">{t(page["next_title_en"])}</strong></span>')
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
                   date_published=TRACK_DATE, date_modified=TRACK_DATE, crumbs=crumbs)
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

    instrument = slope_instrument(page, rel_res) if slug else worldline_instrument(page)
    ai_line = bi("p", page["ai_line_en"], page["ai_line_es"], "tg-ai-line") if page.get("ai_line_en") else ""
    order = bi("span", page["order_label_en"], page["order_label_es"])
    rt = bi("span", page["reading_time_en"], page["reading_time_es"])

    return f"""{head}
<body class="tp-body tp-page-folio tg-page">
{B.render_masthead(rel_res, "", lang)}
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
{lead_figure(page, rel_res)}
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
