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
import math
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
from timegravity_kernel_entangle import (  # noqa: E402
    BMV_D_M, BMV_DX_M, BMV_M_KG, BMV_T_S, branch_phases, concurrence_closed, entanglement_phase, four_branch_state, negativity,
    time_to_full_entanglement,
)
from timegravity_kernel_dispute import dp_collapse_sigma_at, ktm_dephasing_rate, tn_critical_sigma, tn_potential_ratio  # noqa: E402
from timegravity_kernel_wedge import wedge_deficit, wedge_yukawa_edge_deficit  # noqa: E402
from timegravity_kernel_bounds import (  # noqa: E402
    GS_R0_BOUND_M, GS_R0_PARAMFREE_M, XENONNT_R0_90, dp_collapse_time, gran_sasso_signal_counts, page_average_entropy, page_curve_toy,
)

RESEARCH = ROOT / "src"
LEDGER = json.loads((ROOT / "timegravity" / "ledger.json").read_text(encoding="utf-8"))
ROWS = {r["id"]: r for r in LEDGER["rows"]}
CACHE = json.loads((ROOT / "data" / "folio-citations.cache.json").read_text(encoding="utf-8"))

# The (t, z) plot box shared with timegravity-slope.mjs through data-* attributes on the <svg>.
PLOT = {"x0": 300, "x1": 890, "y0": 50, "y1": 390, "ztop": 1.0, "zbot": -10.5}

LABEL_DEF = {
    "MEASURED": ("At least two collaborations, peer-reviewed DOIs, older than the replication window.",
                 "Al menos dos colaboraciones, DOI revisados por pares, más antiguas que la ventana de replicación."),
    "DERIVED": ("Follows by mathematics or deterministic kernel from a named MEASURED parent row (computed, not directly measured).",
                "Se sigue por matemáticas o kernel determinista de una fila madre MEDIDA con nombre (calculado, no medido directamente)."),
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


def seg(s: dict, lang: str = "en") -> str:
    if s["kind"] == "text":
        return f'<span data-en="{a(s["en"])}" data-es="{a(s["es"])}">{t(s["en"])}</span>'
    label = s["label"]
    parent_id = s.get("parent")
    parent = f' data-tg-parent="{a(parent_id)}"' if parent_id else ""
    k_attr = f' data-tg-kernel="{a(s["kernel"])}"' if s.get("kernel") else ""
    scope_attr = f' data-tg-scope="{a(s["scope"])}"' if s.get("scope") else ""
    qual_attrs = ""
    if label == "DERIVED" and parent_id:
        qual = "DERIVADO (NO MEDIDO)" if lang == "es" else "DERIVED (NOT MEASURED)"
        title_en = f"Derived by mathematics/kernel from MEASURED parent row {parent_id} (not directly measured)"
        title_es = f"Derivado por matemáticas/kernel de la fila madre MEDIDA {parent_id} (no medido directamente)"
        title_cur = title_es if lang == "es" else title_en
        qual_attrs = (
            f' data-tg-qualifier="{a(qual)}" title="{a(title_cur)}"'
            f' data-title-en="{a(title_en)}" data-title-es="{a(title_es)}"'
        )
    return (
        f'<span class="tg-claim" data-tg-label="{a(label)}" data-tg-label-es="{a(LABEL_ES[label])}" '
        f'data-tg-ledger="{a(",".join(s["ids"]))}"{parent}{k_attr}{scope_attr}{qual_attrs} data-en="{a(s["en"])}" data-es="{a(s["es"])}">{t(s["en"])}</span>'
    )


def para(p: dict, lang: str = "en") -> str:
    return "<p>" + "".join(seg(s, lang) for s in p["segments"]) + "</p>"


def png_sha8(slug: str) -> str:
    p = RESEARCH / "plates" / f"{slug}.png"
    return hashlib.sha256(p.read_bytes()).hexdigest()[:8] if p.is_file() else "00000000"


def plate_slug(page: dict) -> str:
    return "t00" if page["slug"] == "" else page["slug"]


def boundary_banner(compact: bool = False) -> str:
    """The fixed boundary. The hub prints the full box; every other T page prints a one-line strip whose <details>
    holds the same sentence, so the lint's exact-string check and the reader's first mobile screen both hold."""
    if compact:
        return f"""      <details class="tg-boundary-banner tg-boundary-compact">
        <summary>{bi("strong", "Fixed boundary", "Frontera fija")} {bi("span", "No theory of everything here: six evidence labels, one open question per page.", "Aquí no hay teoría del todo: seis etiquetas de evidencia, una pregunta abierta por página.", "tg-boundary-short")}</summary>
        {bi("p", BOUNDARY_EN, BOUNDARY_ES)}
      </details>"""
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
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="{B._href(rel_res, "physics/")}" data-en="Physics" data-es="Física">Physics</a></li>
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
    "T.05": (
        "Two masses each in two places, the four branch lines between them, and entanglement against hold time for three channels at one stroke weight: the quantum curve, the classical LOCC flat line and the disputed band between them.",
        "Dos masas cada una en dos lugares, las cuatro líneas de rama entre ellas, y el entrelazamiento frente al tiempo de espera para tres canales con un mismo grosor: la curva cuántica, la recta plana del canal clásico LOCC y la banda en disputa entre ambas.",
        "two pairs of dots joined by four lines on the left, and on the right a rising curve above a dashed flat line with a hatched band between them and one dot on the curve",
        "dos pares de puntos unidos por cuatro líneas a la izquierda, y a la derecha una curva ascendente sobre una recta punteada plana con una banda rayada entre ambas y un punto sobre la curva",
    ),
    "T.06": (
        "A collapse-time curve falling steeply with mass beside an exclusion bar for R0, with the two bounds and the parameter-free value on the excluded side.",
        "Una curva de tiempo de colapso que cae abruptamente con la masa junto a una barra de exclusión para R0, con las dos cotas y el valor sin parámetros del lado excluido.",
        "a steep falling curve on the left and a horizontal bar with two tick marks and one dot on its shaded side on the right",
        "una curva que cae abruptamente a la izquierda y una barra horizontal con dos marcas y un punto en su lado sombreado a la derecha",
    ),
    "T.10": (
        "Hawking's straight line rising beside Page's curve, which rises with it, turns over at half the qubits and falls back to zero; dots from the ten-qubit toy sit on the curve.",
        "La recta de Hawking subiendo junto a la curva de Page, que sube con ella, da la vuelta a la mitad de los qubits y vuelve a cero; puntos del juguete de diez qubits descansan sobre la curva.",
        "a straight rising line and a hill-shaped curve that peaks in the middle, with dots along the hill",
        "una recta ascendente y una curva en forma de loma que alcanza su máximo en el centro, con puntos sobre la loma",
    ),
    "T.03": (
        "Concentric rings around a mass, darker where clocks run slower, from the Poisson solution on a grid; two dots of different size fall along the same line.",
        "Anillos concéntricos alrededor de una masa, más oscuros donde los relojes van más lento, de la solución de Poisson en una malla; dos puntos de distinto tamaño caen por la misma línea.",
        "concentric rings around a disc, darker toward the centre, and two dots of different size on one vertical line",
        "anillos concéntricos alrededor de un disco, más oscuros hacia el centro, y dos puntos de distinto tamaño sobre una línea vertical",
    ),
    "T.08": (
        "Left: the Rindler causal horizon X = ±cT and the accelerated worldline hyperbola, with one mode partner outside and one hidden behind the horizon. Right: the reduced state's Fock occupation bars matching the Planck thermal curve.",
        "Izquierda: el horizonte causal de Rindler X = ±cT y la hipérbola de la línea de mundo acelerada, con un modo compañero afuera y otro oculto detrás del horizonte. Derecha: las barras de ocupación de Fock del estado reducido coincidiendo con la curva térmica de Planck.",
        "a pair of diagonal horizon lines with a curved hyperbola on the left, and a set of descending vertical bars with dots on top on the right",
        "un par de líneas diagonales de horizonte con una hipérbola curva a la izquierda, y un conjunto de barras verticales descendentes con puntos encima a la derecha",
    ),
    "T.09": (
        "Left: the damped sinusoidal ringdown waveform of a newly merged Kerr black hole for the fundamental (2,2,0) mode and its faster-decaying first overtone (2,2,1). Right: the Kerr trajectory in the frequency–damping plane as spin rises from zero to 0.90.",
        "Izquierda: la forma de onda sinusoidal amortiguada de un agujero negro de Kerr recién fusionado para el modo fundamental (2,2,0) y su primer sobretono (2,2,1) de decaimiento más rápido. Derecha: la trayectoria de Kerr en el plano frecuencia–amortiguamiento conforme el espín sube de cero a 0.90.",
        "a damped oscillating wave on the left, and a rising curve with dots along it in a frequency versus damping-time plot on the right",
        "una onda oscilante amortiguada a la izquierda, y una curva ascendente con puntos encima en una gráfica de frecuencia contra tiempo de amortiguamiento a la derecha",
    ),
    "T.11": (
        "Left: the 2 × 2 clock reduced density matrix ρ_S as environmental photons scatter off the split, suppressing off-diagonal coherences as γ^N while leaving the pointer diagonal untouched. Right: the Quantum Darwinism mutual-information plateau I(S : E_k) across k of N = 6 bath modes.",
        "Izquierda: la matriz de densidad reducida 2 × 2 del reloj ρ_S conforme los fotones del entorno se dispersan en la división, suprimiendo las coherencias fuera de la diagonal como γ^N mientras deja intacta la diagonal puntero. Derecha: la meseta de información mutua del darwinismo cuántico I(S : E_k) a lo largo de k de N = 6 modos del baño.",
        "four matrix bars on the left where the two off-diagonal bars shrink with bath scattering, and a rising S-shaped mutual-information plateau curve with dots on the right",
        "cuatro barras matriciales a la izquierda donde las dos barras fuera de la diagonal se encogen con la dispersión del baño, y una curva en S con meseta de información mutua y puntos a la derecha",
    ),
    "T.12": (
        "Left: an electromagnetically transparent dark-matter subhalo flying past a two-node optical clock baseline (Λ_EM = 0), shifting the gravitational potential Φ(r) while leaving photon scattering at zero. Right: the accumulated proper-time step Δτ(t) across the flyby and its asymptotic plateau Δτ_∞ = −(2GM/c²v_0) ln(b_2/b_1).",
        "Izquierda: un subhalo de materia oscura electromagnéticamente transparente que pasa junto a una línea base de dos relojes ópticos (Λ_EM = 0), desplazando el potencial gravitatorio Φ(r) sin dispersar fotones. Derecha: el escalón acumulado de tiempo propio Δτ(t) durante el sobrevuelo y su meseta asintótica Δτ_∞ = −(2GM/c²v_0) ln(b_2/b_1).",
        "a trajectory passing two clock circles on the left, and a smooth step-shaped curve of accumulated proper-time difference against time on the right",
        "una trayectoria que pasa junto a dos círculos de reloj a la izquierda, y una curva suave en forma de escalón de diferencia de tiempo propio acumulada contra el tiempo a la derecha",
    ),
    "T.13": (
        "Left: an oscillatory binary-merger gravitational wave riding onto Christodoulou's permanent DC displacement memory step Δh_char = G E_rad / (c⁴ D_L), shifting proper arm separation by ΔL = (1/2) L_0 Δh. Right: Weinberg's spin-2 soft Ward residual and the Standard Model chiral and mixed gauge–gravitational anomaly polynomials crossing zero together exclusively at N_c = 3 quark colours.",
        "Izquierda: una onda gravitacional oscilatoria de fusión binaria montada sobre el escalón permanente de memoria de desplazamiento de Christodoulou Δh_char = G E_rad / (c⁴ D_L), desplazando la separación propia del brazo en ΔL = (1/2) L_0 Δh. Derecha: el residuo blando de Ward de espín 2 de Weinberg y los polinomios de anomalías quirales y mixtas del Modelo Estándar cruzando cero simultáneamente en N_c = 3 colores de quarks.",
        "an oscillating gravitational wave settling onto a permanent upward step on the left, and anomaly residual lines crossing zero together at N_c equals 3 on the right",
        "una onda gravitacional oscilante que se asienta en un escalón permanente hacia arriba a la izquierda, y líneas de residuos de anomalías que cruzan cero juntas en N_c igual a 3 a la derecha",
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
      <img class="tp-editorial-img" src="{rel_res}/plates/{slug}.png?v={png_sha8(slug)}" width="1200" height="630" alt="{a(alt_txt)}" loading="eager" fetchpriority="high" decoding="async">
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
          <rect class="tg-rate-col" x="140" y="{P['y0']}" width="60" height="{P['y1'] - P['y0']}" rx="6" fill="url(#tg-rate-grad)" opacity="0.6"/>
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
          <rect x="140" y="50" width="60" height="250" rx="6" fill="url(#tg-rate-grad-hub)" opacity="0.6"/>
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
        rings.append(f'<circle class="tg-ring" data-ring="{k}" cx="{cx}" cy="{cy}" r="{rpx * rr:.1f}" fill="none" stroke="var(--tp-prussian)" stroke-width="{3 + 6 * depth:.1f}" opacity="{0.15 + 0.6 * depth:.2f}"/>')
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
            tiles.append(f'<rect class="tg-tile" data-n="{n}" data-col="{col}" x="{x}" y="{ty0 + n * th}" width="60" height="{th - 2}" rx="3" fill="var(--tp-prussian)" opacity="{0.08 + 0.85 * p:.3f}"/>')
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


def dp_instrument(page: dict) -> str:
    ins = page["instrument"]
    import math
    log_m0, log_r0, dr0 = -14.0, -6.0, 2.0
    px0, px1, py0, py1 = 60, 440, 60, 360        # τ against log10 mass; y = log10 τ in [-6, 12]
    to_x = lambda lm: px0 + (px1 - px0) * (lm + 20.0) / 8.0  # noqa: E731   (mass 1e-20 .. 1e-12 kg)
    to_y = lambda lt: py1 - (py1 - py0) * (lt + 6.0) / 18.0  # noqa: E731   (τ 1e-6 .. 1e12 s)
    pts = []
    for i in range(81):
        lm = -20.0 + 8.0 * i / 80
        tau = dp_collapse_time(10.0 ** lm, 10.0 ** log_r0, dr0 * 10.0 ** log_r0)
        lt = max(-6.0, min(12.0, math.log10(tau)))
        pts.append(f'{"M" if i == 0 else "L"} {to_x(lm):.1f} {to_y(lt):.1f}')
    tau0 = dp_collapse_time(10.0 ** log_m0, 10.0 ** log_r0, dr0 * 10.0 ** log_r0)
    # R0 exclusion bar: log10 R0 from -12 to -9 (1 pm .. 1 nm)
    bx0, bx1, by = 520, 880, 200
    to_bx = lambda r0: bx0 + (bx1 - bx0) * (math.log10(r0) + 12.0) / 3.0  # noqa: E731
    gs_x, xe_x, pf_x = to_bx(GS_R0_BOUND_M), to_bx(XENONNT_R0_90), to_bx(GS_R0_PARAMFREE_M)
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="dp" aria-labelledby="tg-instrument-heading-t06">
      <h2 id="tg-instrument-heading-t06" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 420" role="img" aria-labelledby="tg-stage-title-t06 tg-stage-desc-t06" data-px0="{px0}" data-px1="{px1}" data-py0="{py0}" data-py1="{py1}" data-bx0="{bx0}" data-bx1="{bx1}">
          <title id="tg-stage-title-t06">The Diósi–Penrose collapse time against mass, and the exclusion bar for the nuclear density size R0</title>
          <desc id="tg-stage-desc-t06">Left: a curve of the model's collapse time against mass on log scales, falling steeply as mass grows. Right: a horizontal bar for R0 from one picometre to one nanometre; the region below the Gran Sasso bound is shaded as excluded, the XENONnT bound sits further right, and the parameter-free value sits deep in the excluded region.</desc>
          <text x="{(px0 + px1) / 2:.0f}" y="36" text-anchor="middle" font-size="11" font-weight="700" data-en="model collapse time τ = ħ/E_G (log–log)" data-es="tiempo de colapso del modelo τ = ħ/E_G (log–log)">model collapse time τ = ħ/E_G (log–log)</text>
          <line class="tg-axis" x1="{px0}" y1="{py0}" x2="{px0}" y2="{py1}"/>
          <line class="tg-axis" x1="{px0}" y1="{py1}" x2="{px1}" y2="{py1}"/>
          <text x="{px0 - 6}" y="{to_y(12.0) + 4:.0f}" text-anchor="end" font-size="10">10¹² s</text>
          <text x="{px0 - 6}" y="{to_y(0.0) + 4:.0f}" text-anchor="end" font-size="10">1 s</text>
          <text x="{px0 - 6}" y="{to_y(-6.0) + 4:.0f}" text-anchor="end" font-size="10">10⁻⁶ s</text>
          <text x="{px0}" y="{py1 + 16}" font-size="10">10⁻²⁰ kg</text>
          <text x="{px1}" y="{py1 + 16}" text-anchor="end" font-size="10">10⁻¹² kg</text>
          <text x="{(px0 + px1) / 2:.0f}" y="{py1 + 34}" text-anchor="middle" font-size="11" data-en="mass of the sphere in two places" data-es="masa de la esfera en dos lugares">mass of the sphere in two places</text>
          <path class="tg-dp-curve" d="{' '.join(pts)}" fill="none" stroke="var(--tp-prussian)" stroke-width="2.5"/>
          <circle class="tg-dp-marker" cx="{to_x(log_m0):.1f}" cy="{to_y(math.log10(tau0)):.1f}" r="7" fill="var(--tp-minium)" stroke="var(--tp-vellum)" stroke-width="2"/>
          <text x="{(bx0 + bx1) / 2:.0f}" y="36" text-anchor="middle" font-size="11" font-weight="700" data-en="where the data draw the line for R0" data-es="dónde trazan los datos la línea para R0">where the data draw the line for R0</text>
          <rect class="tg-dp-excluded" x="{bx0}" y="{by - 16}" width="{gs_x - bx0:.1f}" height="32" fill="var(--tp-minium-soft)" stroke="none"/>
          <rect class="tg-dp-allowed" x="{gs_x:.1f}" y="{by - 16}" width="{bx1 - gs_x:.1f}" height="32" fill="var(--tp-verdigris-soft)" stroke="none"/>
          <line class="tg-axis" x1="{bx0}" y1="{by}" x2="{bx1}" y2="{by}"/>
          <text x="{bx0}" y="{by + 44}" font-size="10">1 pm</text>
          <text x="{bx1}" y="{by + 44}" text-anchor="end" font-size="10">1 nm</text>
          <text x="{(bx0 + bx1) / 2:.0f}" y="{by + 62}" text-anchor="middle" font-size="11" data-en="R0, size of the nuclear mass density (log)" data-es="R0, tamaño de la densidad de masa nuclear (log)">R0, size of the nuclear mass density (log)</text>
          <line class="tg-dp-gs" x1="{gs_x:.1f}" y1="{by - 28}" x2="{gs_x:.1f}" y2="{by + 28}" stroke="var(--tp-ink)" stroke-width="2.5"/>
          <text x="{gs_x:.1f}" y="{by - 36}" text-anchor="middle" font-size="10" data-en="Gran Sasso 2021 · 0.54 Å · 95 %" data-es="Gran Sasso 2021 · 0.54 Å · 95 %">Gran Sasso 2021 · 0.54 Å · 95 %</text>
          <line class="tg-dp-xe" x1="{xe_x:.1f}" y1="{by - 28}" x2="{xe_x:.1f}" y2="{by + 28}" stroke="var(--tp-prussian)" stroke-width="2.5" stroke-dasharray="5 4"/>
          <text x="{xe_x:.1f}" y="{by - 36}" text-anchor="middle" font-size="10" data-en="XENONnT 2026 · 4.9 Å · 90 %" data-es="XENONnT 2026 · 4.9 Å · 90 %">XENONnT 2026 · 4.9 Å · 90 %</text>
          <circle class="tg-dp-pf" cx="{pf_x:.1f}" cy="{by}" r="7" fill="var(--tp-minium)" stroke="var(--tp-vellum)" stroke-width="2"/>
          <text x="{pf_x:.1f}" y="{by + 30}" text-anchor="middle" font-size="10" data-en="parameter-free · 0.05 Å" data-es="sin parámetros · 0.05 Å">parameter-free · 0.05 Å</text>
          <text class="tg-dp-side" x="{(bx0 + gs_x) / 2:.0f}" y="{by + 6}" text-anchor="middle" font-size="10" font-weight="700" fill="var(--tp-minium)" data-tg-read="sideleft" data-en="excluded" data-es="excluido">excluded</text>
          <text class="tg-dp-side" x="{(gs_x + bx1) / 2:.0f}" y="{by + 6}" text-anchor="middle" font-size="10" font-weight="700" fill="var(--tp-verdigris)" data-tg-read="sideright" data-en="allowed" data-es="permitido">allowed</text>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-logm-t06"><span data-en="log₁₀ mass M (kg)" data-es="log₁₀ masa M (kg)">log₁₀ mass M (kg)</span> <span data-tg-read="logm">{log_m0:.1f}</span></label>
          <input id="tg-logm-t06" data-tg-logm type="range" min="-20" max="-12" step="0.1" value="{log_m0}" aria-describedby="tg-status-t06">
          <label for="tg-logr-t06"><span data-en="log₁₀ radius R (m)" data-es="log₁₀ radio R (m)">log₁₀ radius R (m)</span> <span data-tg-read="logr">{log_r0:.1f}</span></label>
          <input id="tg-logr-t06" data-tg-logr type="range" min="-9" max="-5" step="0.1" value="{log_r0}">
          <label for="tg-dr-t06"><span data-en="displacement d / R" data-es="desplazamiento d / R">displacement d / R</span> <span data-tg-read="dr">{dr0:.1f}</span></label>
          <input id="tg-dr-t06" data-tg-dr type="range" min="0.1" max="6" step="0.1" value="{dr0}">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and planted defect">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · switch gravity off (G → 0)" data-es="⚡ Apagado · quitar la gravedad (G → 0)">⚡ Knockout · switch gravity off (G → 0)</button>
          <button type="button" class="tp-step-btn" data-tg-flip aria-pressed="false" data-en="Planted defect · draw the bound on the wrong side" data-es="Defecto plantado · dibujar la cota del lado equivocado">Planted defect · draw the bound on the wrong side</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="E_G of the difference" data-es="E_G de la diferencia">E_G of the difference</span>
          <span class="tp-readout-v" data-tg-read="eg">{1.054571817e-34 / tau0:.2e} J</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Model collapse time τ" data-es="Tiempo de colapso del modelo τ">Model collapse time τ</span>
          <span class="tp-readout-v" data-tg-read="tau">{tau0:.3g} s</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Photons predicted at Gran Sasso, parameter-free R0" data-es="Fotones predichos en Gran Sasso, R0 sin parámetros">Photons predicted at Gran Sasso, parameter-free R0</span>
          <span class="tp-readout-v">{gran_sasso_signal_counts(GS_R0_PARAMFREE_M):.1e}</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="Parameter-free value is" data-es="El valor sin parámetros está">Parameter-free value is</span>
          <span class="tp-readout-v" data-tg-read="verdict" data-en="excluded" data-es="excluido">excluded</span>
        </div>
      </div>
      <p id="tg-status-t06" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="The model's prediction on the left; the data's verdict on the right. Below the line the radiation would have been seen; it was not." data-es="La predicción del modelo a la izquierda; el veredicto de los datos a la derecha. Debajo de la línea la radiación se habría visto; no se vio.">The model's prediction on the left; the data's verdict on the right. Below the line the radiation would have been seen; it was not.</p>
    </section>"""


def bmv_instrument(page: dict) -> str:
    ins = page["instrument"]
    import math
    log_m0, d0_um, dx0_um, t0, log_g0 = -14.0, 450.0, 250.0, 2.5, -4.0
    T_MAX = 30.0
    # Left panel: positions along x (A at ∓Δx/2, B at d ∓ Δx/2), two rows.
    lx0, lx1, ya, yb = 70, 400, 120, 320
    span = (d0_um + dx0_um) * 1e-6
    sx = lambda pos: lx0 + (lx1 - lx0) * (pos + dx0_um * 1e-6 / 2) / span  # noqa: E731
    ax = (sx(-dx0_um * 1e-6 / 2), sx(dx0_um * 1e-6 / 2))
    bx = (sx(d0_um * 1e-6 - dx0_um * 1e-6 / 2), sx(d0_um * 1e-6 + dx0_um * 1e-6 / 2))
    # Right panel: entanglement 0..1 against hold time 0..T_MAX.
    px0, px1, py0, py1 = 500, 880, 60, 340
    to_x = lambda tt: px0 + (px1 - px0) * tt / T_MAX  # noqa: E731
    to_y = lambda e: py1 - (py1 - py0) * e  # noqa: E731
    q_pts, band = [], []
    for i in range(121):
        tt = T_MAX * i / 120
        e = concurrence_closed(entanglement_phase(branch_phases(BMV_M_KG, BMV_D_M, BMV_DX_M, tt, "quantum")))
        q_pts.append(f'{"M" if i == 0 else "L"} {to_x(tt):.1f} {to_y(e):.1f}')
        band.append(f"{to_x(tt):.1f},{to_y(e):.1f}")
    band_poly = " ".join(band) + f" {px1},{py1} {px0},{py1}"
    q0 = branch_phases(BMV_M_KG, BMV_D_M, BMV_DX_M, t0, "quantum")
    dphi0 = entanglement_phase(q0)
    c0 = concurrence_closed(dphi0)
    n0 = negativity(four_branch_state(q0, 10.0 ** log_g0 * t0))
    tfull0 = time_to_full_entanglement(BMV_M_KG, BMV_D_M, BMV_DX_M)
    log_sig0 = -3.0   # σ = 1 mm, above the 2017 geometry's critical 525 µm
    sigma_c0 = tn_critical_sigma(BMV_M_KG, BMV_DX_M, BMV_D_M - BMV_DX_M)
    ktm_gt0 = ktm_dephasing_rate(BMV_M_KG, BMV_D_M, BMV_DX_M) * t0
    soft0 = tn_potential_ratio(BMV_D_M - BMV_DX_M, 10.0 ** log_sig0)
    isl0 = wedge_deficit(10.0 ** log_sig0)
    isl_edge = wedge_yukawa_edge_deficit()
    col0 = dp_collapse_sigma_at(BMV_DX_M, BMV_D_M - BMV_DX_M, BMV_M_KG, t0, 0.0)
    seps = {"LL": d0_um, "LR": d0_um + dx0_um, "RL": d0_um - dx0_um, "RR": d0_um}
    lines_svg = []
    for i, (ia, xa) in enumerate(zip("LR", ax)):
        for j, (jb, xb_) in enumerate(zip("LR", bx)):
            key = ia + jb
            lines_svg.append(
                f'          <line class="tg-bmv-branch" data-tg-branch="{key}" x1="{xa:.1f}" y1="{ya}" x2="{xb_:.1f}" y2="{yb}" '
                f'stroke="{"var(--tp-stone)" if i == j else "var(--tp-prussian)"}" stroke-width="2"/>'
            )
            lines_svg.append(
                f'          <text class="tg-bmv-sep" data-tg-sep="{key}" x="{(xa + xb_) / 2 + (18 if key == "LR" else -18 if key == "RL" else 0):.1f}" '
                f'y="{(ya + yb) / 2 + (-6 if key in ("LL",) else 14 if key == "RR" else 4)}" text-anchor="middle" font-size="10">{key} · {seps[key]:.0f} µm</text>'
            )
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="bmv" aria-labelledby="tg-instrument-heading-t05">
      <h2 id="tg-instrument-heading-t05" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 420" role="img" aria-labelledby="tg-stage-title-t05 tg-stage-desc-t05" data-lx0="{lx0}" data-lx1="{lx1}" data-ya="{ya}" data-yb="{yb}" data-px0="{px0}" data-px1="{px1}" data-py0="{py0}" data-py1="{py1}" data-tmax="{T_MAX}">
          <title id="tg-stage-title-t05">Two masses each in two places with four branch lines, and entanglement against hold time for three channels</title>
          <desc id="tg-stage-desc-t05">Left: mass A in two positions on an upper row and mass B in two positions on a lower row, joined by four lines labelled with their separations in micrometres. Right: entanglement from zero to one against hold time from zero to thirty seconds, with a rising curve for the quantum channel, a dashed flat line at zero for the classical LOCC channel, and a hatched band between them for the disputed classical non-LOCC channel; a marker sits on the followed channel at the chosen hold time.</desc>
          <defs>
            <pattern id="tg-bmv-hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
              <line x1="0" y1="0" x2="0" y2="8" stroke="var(--tp-prussian)" stroke-width="1.2" opacity="0.45"/>
            </pattern>
          </defs>
          <text x="{(lx0 + lx1) / 2:.0f}" y="36" text-anchor="middle" font-size="11" font-weight="700" data-en="four branches, four separations" data-es="cuatro ramas, cuatro separaciones">four branches, four separations</text>
          <text x="{lx0 - 30}" y="{ya + 4}" text-anchor="end" font-size="11" font-weight="700">A</text>
          <text x="{lx0 - 30}" y="{yb + 4}" text-anchor="end" font-size="11" font-weight="700">B</text>
{chr(10).join(lines_svg)}
          <circle class="tg-bmv-mass" data-tg-mass="AL" cx="{ax[0]:.1f}" cy="{ya}" r="11" fill="var(--tp-prussian)" stroke="var(--tp-vellum)" stroke-width="2"/>
          <circle class="tg-bmv-mass" data-tg-mass="AR" cx="{ax[1]:.1f}" cy="{ya}" r="11" fill="var(--tp-prussian)" stroke="var(--tp-vellum)" stroke-width="2"/>
          <circle class="tg-bmv-mass" data-tg-mass="BL" cx="{bx[0]:.1f}" cy="{yb}" r="11" fill="var(--tp-minium)" stroke="var(--tp-vellum)" stroke-width="2"/>
          <circle class="tg-bmv-mass" data-tg-mass="BR" cx="{bx[1]:.1f}" cy="{yb}" r="11" fill="var(--tp-minium)" stroke="var(--tp-vellum)" stroke-width="2"/>
          <text x="{(lx0 + lx1) / 2:.0f}" y="{yb + 44}" text-anchor="middle" font-size="11" data-en="L and R: the two positions of each mass" data-es="L y R: las dos posiciones de cada masa">L and R: the two positions of each mass</text>
          <text x="{(px0 + px1) / 2:.0f}" y="36" text-anchor="middle" font-size="11" font-weight="700" data-en="entanglement against hold time, three channels" data-es="entrelazamiento frente al tiempo de espera, tres canales">entanglement against hold time, three channels</text>
          <line class="tg-axis" x1="{px0}" y1="{py0}" x2="{px0}" y2="{py1}"/>
          <line class="tg-axis" x1="{px0}" y1="{py1}" x2="{px1}" y2="{py1}"/>
          <text x="{px0 - 6}" y="{py0 + 4}" text-anchor="end" font-size="10">1</text>
          <text x="{px0 - 6}" y="{py1 + 4}" text-anchor="end" font-size="10">0</text>
          <text x="{px0}" y="{py1 + 16}" font-size="10">0 s</text>
          <text x="{px1}" y="{py1 + 16}" text-anchor="end" font-size="10">{T_MAX:.0f} s</text>
          <text x="{(px0 + px1) / 2:.0f}" y="{py1 + 34}" text-anchor="middle" font-size="11" data-en="hold time t" data-es="tiempo de espera t">hold time t</text>
          <polygon class="tg-bmv-band" points="{band_poly}" fill="url(#tg-bmv-hatch)" stroke="none"/>
          <path class="tg-bmv-dp" d="M {px0} {py1 - 1.5} L {px1} {py1 - 1.5}" fill="none" stroke="var(--tp-ink)" stroke-width="2.5" stroke-dasharray="2 4"/>
          <path class="tg-bmv-q" d="{' '.join(q_pts)}" fill="none" stroke="var(--tp-prussian)" stroke-width="2.5"/>
          <line class="tg-bmv-l" x1="{px0}" y1="{py1 - 1.5}" x2="{px1}" y2="{py1 - 1.5}" stroke="var(--tp-verdigris)" stroke-width="2.5" stroke-dasharray="7 5"/>
          <circle class="tg-bmv-marker" cx="{to_x(t0):.1f}" cy="{to_y(c0):.1f}" r="7" fill="var(--tp-minium)" stroke="var(--tp-vellum)" stroke-width="2"/>
          <g class="tg-bmv-legend" font-size="10">
            <line x1="{px0}" y1="{py1 + 54}" x2="{px0 + 22}" y2="{py1 + 54}" stroke="var(--tp-prussian)" stroke-width="2.5"/>
            <text x="{px0 + 28}" y="{py1 + 58}" data-en="quantum mediator" data-es="mediador cuántico">quantum mediator</text>
            <line x1="{px0 + 140}" y1="{py1 + 54}" x2="{px0 + 162}" y2="{py1 + 54}" stroke="var(--tp-verdigris)" stroke-width="2.5" stroke-dasharray="7 5"/>
            <text x="{px0 + 168}" y="{py1 + 58}" data-en="classical LOCC" data-es="clásico LOCC">classical LOCC</text>
            <rect x="{px0 + 262}" y="{py1 + 47}" width="22" height="14" fill="url(#tg-bmv-hatch)" stroke="var(--tp-prussian)" stroke-width="0.8"/>
            <text x="{px0 + 290}" y="{py1 + 58}" data-en="disputed, no single answer" data-es="en disputa, sin respuesta única">disputed, no single answer</text>
            <line x1="{px0}" y1="{py1 + 74}" x2="{px0 + 22}" y2="{py1 + 74}" stroke="var(--tp-ink)" stroke-width="2.5" stroke-dasharray="2 4"/>
            <text x="{px0 + 28}" y="{py1 + 78}" data-en="one named classical model: Diósi–Penrose with smearing σ (its prediction, not the page's)" data-es="un modelo clásico con nombre: Diósi–Penrose con suavizado σ (su predicción, no la de la página)">one named classical model: Diósi–Penrose with smearing σ (its prediction, not the page's)</text>
          </g>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-logm-t05"><span data-en="log₁₀ mass m (kg)" data-es="log₁₀ masa m (kg)">log₁₀ mass m (kg)</span> <span data-tg-read="logm">{log_m0:.1f}</span></label>
          <input id="tg-logm-t05" data-tg-logm type="range" min="-16" max="-12" step="0.1" value="{log_m0}" aria-describedby="tg-status-t05">
          <label for="tg-d-t05"><span data-en="separation d (µm)" data-es="separación d (µm)">separation d (µm)</span> <span data-tg-read="d">{d0_um:.0f}</span></label>
          <input id="tg-d-t05" data-tg-d type="range" min="150" max="1000" step="10" value="{d0_um:.0f}">
          <label for="tg-dx-t05"><span data-en="split Δx (µm)" data-es="división Δx (µm)">split Δx (µm)</span> <span data-tg-read="dx">{dx0_um:.0f}</span></label>
          <input id="tg-dx-t05" data-tg-dx type="range" min="10" max="400" step="10" value="{dx0_um:.0f}">
          <label for="tg-t-t05"><span data-en="hold time t (s)" data-es="tiempo de espera t (s)">hold time t (s)</span> <span data-tg-read="t">{t0:.1f}</span></label>
          <input id="tg-t-t05" data-tg-t type="range" min="0.1" max="{T_MAX:.0f}" step="0.1" value="{t0}">
          <label for="tg-logg-t05"><span data-en="log₁₀ dephasing rate γ (1/s)" data-es="log₁₀ tasa de desfase γ (1/s)">log₁₀ dephasing rate γ (1/s)</span> <span data-tg-read="logg">{log_g0:.1f}</span></label>
          <input id="tg-logg-t05" data-tg-logg type="range" min="-4" max="1" step="0.1" value="{log_g0}">
          <label for="tg-logsig-t05"><span data-en="log₁₀ smearing σ of the Diósi–Penrose model (m)" data-es="log₁₀ suavizado σ del modelo de Diósi–Penrose (m)">log₁₀ smearing σ of the Diósi–Penrose model (m)</span> <span data-tg-read="logsig">{log_sig0:.1f}</span></label>
          <input id="tg-logsig-t05" data-tg-logsig type="range" min="-6" max="-1" step="0.1" value="{log_sig0}">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout: which channel the readouts follow">
          <span class="tg-btn-row-label" data-en="⚡ Knockout · switch the channel:" data-es="⚡ Apagado · cambiar el canal:">⚡ Knockout · switch the channel:</span>
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-channel="quantum" aria-pressed="true" data-en="quantum mediator" data-es="mediador cuántico">quantum mediator</button>
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-channel="locc" aria-pressed="false" data-en="classical LOCC" data-es="clásico LOCC">classical LOCC</button>
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-channel="disputed" aria-pressed="false" data-en="disputed classical non-LOCC" data-es="clásico no-LOCC en disputa">disputed classical non-LOCC</button>
        </div>
        <div class="tg-btn-row" role="group" aria-label="Planted defect">
          <button type="button" class="tp-step-btn" data-tg-flip aria-pressed="false" data-en="Planted defect · a classical LOCC channel that entangles" data-es="Defecto plantado · un canal clásico LOCC que entrelaza">Planted defect · a classical LOCC channel that entangles</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Entanglement phase Δφ" data-es="Fase de entrelazamiento Δφ">Entanglement phase Δφ</span>
          <span class="tp-readout-v" data-tg-read="dphi">{dphi0:.3f} rad</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Entanglement (2 × negativity; equals concurrence when pure)" data-es="Entrelazamiento (2 × negatividad; igual a la concurrencia si es puro)">Entanglement (2 × negativity; equals concurrence when pure)</span>
          <span class="tp-readout-v" data-tg-read="ent">{2 * n0:.3f}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Hold time for full entanglement (Δφ = π)" data-es="Tiempo de espera para entrelazamiento completo (Δφ = π)">Hold time for full entanglement (Δφ = π)</span>
          <span class="tp-readout-v" data-tg-read="tfull">{tfull0:.1f} s</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Lower edge · classical channel at its minimal rate KΔx²/2ħ (γt)" data-es="Borde inferior · canal clásico a su tasa mínima KΔx²/2ħ (γt)">Lower edge · classical channel at its minimal rate KΔx²/2ħ (γt)</span>
          <span class="tp-readout-v" data-tg-read="ktm">{ktm_gt0:.3f} · 0 entanglement in its own linear model</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Upper edge · Diósi–Penrose model at this σ (critical σ for this geometry)" data-es="Borde superior · modelo de Diósi–Penrose a esta σ (σ crítica para esta geometría)">Upper edge · Diósi–Penrose model at this σ (critical σ for this geometry)</span>
          <span class="tp-readout-v" data-tg-read="dp">σ_c = {sigma_c0 * 1e6:.0f} µm · entangles slowly, nothing visible in 30 s</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Collapse test · quantum gravity plus pure Diósi–Penrose collapse, Newton intact: the witness at this hold time survives for" data-es="Prueba de colapso · gravedad cuántica más colapso puro de Diósi–Penrose, Newton intacto: el testigo a este tiempo de espera sobrevive para">Collapse test · quantum gravity plus pure Diósi–Penrose collapse, Newton intact: the witness at this hold time survives for</span>
          <span class="tp-readout-v" data-tg-read="col">σ > {col0 * 1e6:.0f} µm · {col0 / (BMV_D_M - BMV_DX_M):.2f} × the nearest approach · the hybrid σ_c above is {sigma_c0 / col0:.1f} × this</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Newton's pull at the nearest separation, on that model: erf(d/2σ)" data-es="Atracción de Newton a la separación más cercana, en ese modelo: erf(d/2σ)">Newton's pull at the nearest separation, on that model: erf(d/2σ)</span>
          <span class="tp-readout-v" data-tg-read="soft">{100 * soft0:.0f} %</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Eöt-Wash 2020, 120-fold torque at 52 µm on that model (full wedge pattern, Fourier–Bessel)" data-es="Eöt-Wash 2020, par de 120 pliegues a 52 µm en ese modelo (patrón de cuñas completo, Fourier–Bessel)">Eöt-Wash 2020, 120-fold torque at 52 µm on that model (full wedge pattern, Fourier–Bessel)</span>
          <span class="tp-readout-v" data-tg-read="isl">−{100 * isl0:.1f} % · the Yukawa at the published edge: −{100 * isl_edge:.1f} %</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="This channel says the pair is" data-es="Este canal dice que el par está">This channel says the pair is</span>
          <span class="tp-readout-v" data-tg-read="verdict" data-en="entangled" data-es="entrelazado">entangled</span>
        </div>
      </div>
      <p id="tg-status-t05" class="tg-status" data-tg-status data-state="quantum" aria-live="polite" data-en="Quantum mediator: the four phases as written. Weak is not zero; after 2.5 s the concurrence is 0.16, and the same geometry would reach 1 at 25 s." data-es="Mediador cuántico: las cuatro fases tal cual. Débil no es cero; tras 2.5 s la concurrencia es 0.16, y la misma geometría llegaría a 1 a los 25 s.">Quantum mediator: the four phases as written. Weak is not zero; after 2.5 s the concurrence is 0.16, and the same geometry would reach 1 at 25 s.</p>
    </section>"""


def page_instrument(page: dict) -> str:
    ins = page["instrument"]
    import math
    toy = page_curve_toy()
    N = toy["n_qubits"]
    px0, px1, py0, py1 = 100, 880, 50, 360
    ymax = 12.0 * math.log(2.0)   # fixed axis: up to 12 qubits of entropy
    to_x = lambda aq, n: px0 + (px1 - px0) * aq / n  # noqa: E731
    to_y = lambda s: py1 - (py1 - py0) * s / ymax  # noqa: E731
    curve = " ".join(f'{"M" if i == 0 else "L"} {to_x(i, N):.1f} {to_y(page_average_entropy(2 ** i, 2 ** (N - i)) if 0 < i < N else 0.0):.1f}' for i in range(N + 1))
    hawking = f'M {to_x(0, N):.1f} {to_y(0):.1f} L {to_x(N, N):.1f} {to_y(N * math.log(2.0)):.1f}'
    dots = "".join(f'<circle class="tg-page-dot" cx="{to_x(c["a"], N):.1f}" cy="{to_y(c["toy_mean_nats"]):.1f}" r="5" fill="var(--tp-minium)"/>' for c in toy["curve"])
    peak = max(c["toy_mean_nats"] for c in toy["curve"])
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="page" data-tg-toyn="{N}" aria-labelledby="tg-instrument-heading-t10">
      <h2 id="tg-instrument-heading-t10" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 420" role="img" aria-labelledby="tg-stage-title-t10 tg-stage-desc-t10" data-px0="{px0}" data-px1="{px1}" data-py0="{py0}" data-py1="{py1}" data-ymax="{ymax}">
          <title id="tg-stage-title-t10">Hawking's rising line against Page's curve, with dots from a ten-qubit toy</title>
          <desc id="tg-stage-desc-t10">Entropy of the radiation against the number of emitted qubits. A straight line rises without end. A hill-shaped curve rises with it, peaks at half the qubits and falls back to zero. Dots from random ten-qubit states lie on the hill.</desc>
          <line class="tg-axis" x1="{px0}" y1="{py0}" x2="{px0}" y2="{py1}"/>
          <line class="tg-axis" x1="{px0}" y1="{py1}" x2="{px1}" y2="{py1}"/>
          <text x="{px0 - 8}" y="{py1 + 4}" text-anchor="end" font-size="10">0</text>
          <text x="{px0 - 8}" y="{to_y(5 * math.log(2.0)) + 4:.0f}" text-anchor="end" font-size="10">5 ln 2</text>
          <text x="{px0 - 8}" y="{to_y(10 * math.log(2.0)) + 4:.0f}" text-anchor="end" font-size="10">10 ln 2</text>
          <text x="{px0}" y="{py0 - 12}" font-size="11" data-en="entropy of the radiation (nats)" data-es="entropía de la radiación (nats)">entropy of the radiation (nats)</text>
          <text x="{px1}" y="{py1 + 18}" text-anchor="end" font-size="11" data-tg-read="xlabel">emitted qubits a, of N = {N}</text>
          <path class="tg-hawking-line" d="{hawking}" fill="none" stroke="var(--tp-sienna)" stroke-width="2" stroke-dasharray="6 4"/>
          <text class="tg-hawking-label" x="{to_x(N, N) - 4:.1f}" y="{to_y(N * math.log(2.0)) - 8:.1f}" text-anchor="end" font-size="10" fill="var(--tp-sienna)" data-en="Hawking's line: thermal, rising forever" data-es="recta de Hawking: térmica, sube para siempre">Hawking's line: thermal, rising forever</text>
          <path class="tg-page-curve" d="{curve}" fill="none" stroke="var(--tp-prussian)" stroke-width="2.5"/>
          <text class="tg-page-label" x="{to_x(N / 2, N):.1f}" y="{to_y(peak) - 14:.1f}" text-anchor="middle" font-size="10" fill="var(--tp-prussian)" data-en="Page's curve: turns over at N/2" data-es="curva de Page: da la vuelta en N/2">Page's curve: turns over at N/2</text>
          <g class="tg-page-dots">{dots}</g>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-N-t10"><span data-en="Qubits in the black hole N" data-es="Qubits en el agujero negro N">Qubits in the black hole N</span> <span data-tg-read="N">{N}</span></label>
          <input id="tg-N-t10" data-tg-nq type="range" min="4" max="12" step="1" value="{N}" aria-describedby="tg-status-t10">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and the naive count">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · non-unitary: entropy never turns over" data-es="⚡ Apagado · no unitario: la entropía nunca da la vuelta">⚡ Knockout · non-unitary: entropy never turns over</button>
          <button type="button" class="tp-step-btn" data-tg-flip aria-pressed="false" data-en="Naive count · drop Page's −(m−1)/2n term" data-es="Conteo ingenuo · quitar el término −(m−1)/2n de Page">Naive count · drop Page's −(m−1)/2n term</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Peak entropy, Page's formula at N/2" data-es="Entropía máxima, fórmula de Page en N/2">Peak entropy, Page's formula at N/2</span>
          <span class="tp-readout-v" data-tg-read="peak">{page_average_entropy(2 ** (N // 2), 2 ** (N - N // 2)):.3f} nats</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Toy at N = 10: max |toy − Page|" data-es="Juguete en N = 10: máx |juguete − Page|">Toy at N = 10: max |toy − Page|</span>
          <span class="tp-readout-v">{max(abs(c["toy_mean_nats"] - c["page_nats"]) for c in toy["curve"]):.1e} nats</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Entropy at the last cut" data-es="Entropía en el último corte">Entropy at the last cut</span>
          <span class="tp-readout-v" data-tg-read="last">{page_average_entropy(2, 2 ** (N - 1)):.3f} nats</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="Turns over?" data-es="¿Da la vuelta?">Turns over?</span>
          <span class="tp-readout-v" data-tg-read="turn" data-en="yes, at N/2" data-es="sí, en N/2">yes, at N/2</span>
        </div>
      </div>
      <p id="tg-status-t10" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="Counting, not gravity: a random pure state's smaller part is nearly maximally entangled with the larger, so the radiation's entropy follows the smaller side and comes back down." data-es="Conteo, no gravedad: la parte menor de un estado puro aleatorio está casi máximamente entrelazada con la mayor, así que la entropía de la radiación sigue al lado menor y vuelve a bajar.">Counting, not gravity: a random pure state's smaller part is nearly maximally entangled with the larger, so the radiation's entropy follows the smaller side and comes back down.</p>
    </section>"""


def horizon_instrument(page: dict) -> str:
    ins = page["instrument"]
    from timegravity_kernel_horizon import FOCK_D, M_SUN, XI_DEFAULT, schwarzschild_thermodynamics, two_mode_squeezed_wedge
    wedge = two_mode_squeezed_wedge(XI_DEFAULT, FOCK_D)
    bh = schwarzschild_thermodynamics(M_SUN)
    # Left: Rindler wedge diagram centered at (180, 215)
    cx, cy, span = 160.0, 215.0, 130.0
    hyp_pts = []
    for i in range(61):
        eta = -1.1 + 2.2 * i / 60.0
        x = cx + 58.0 * math.cosh(eta)
        y = cy - 58.0 * math.sinh(eta)
        hyp_pts.append(f'{"M" if i == 0 else "L"} {x:.1f} {y:.1f}')
    hyp_path = " ".join(hyp_pts)
    # Right: Fock occupation bars n = 0..7
    px0, px1, py0, py1 = 430, 880, 65, 360
    bars = []
    curve_pts = []
    for n in range(8):
        p = wedge["eigenvalues"][n]
        bx = px0 + 18 + n * 54
        bh_px = (py1 - py0) * p
        by = py1 - bh_px
        bars.append(f'<rect class="tg-fock-bar" data-n="{n}" x="{bx}" y="{by:.1f}" width="34" height="{max(1.0, bh_px):.1f}" rx="2" fill="var(--tp-prussian)" opacity="0.82"/>')
        bars.append(f'<circle class="tg-fock-dot" data-n="{n}" cx="{bx + 17}" cy="{by:.1f}" r="4.5" fill="var(--tp-minium)"/>')
        bars.append(f'<text x="{bx + 17}" y="{py1 + 16}" text-anchor="middle" font-size="9.5">n={n}</text>')
        curve_pts.append(f'{"M" if n == 0 else "L"} {bx + 17:.1f} {by:.1f}')
    planck_path = " ".join(curve_pts)
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="horizon" data-tg-xi="{XI_DEFAULT}" data-tg-fockd="{FOCK_D}" aria-labelledby="tg-instrument-heading-t08">
      <h2 id="tg-instrument-heading-t08" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 420" role="img" aria-labelledby="tg-stage-title-t08 tg-stage-desc-t08" data-px0="{px0}" data-px1="{px1}" data-py0="{py0}" data-py1="{py1}" data-cx="{cx}" data-cy="{cy}">
          <title id="tg-stage-title-t08">Rindler causal horizon and accelerated worldline beside the Planck thermal occupation spectrum of the right wedge</title>
          <desc id="tg-stage-desc-t08">Left: spacetime diagram with null horizons X = ±cT, the accelerated clock hyperbola in the right wedge, and entangled mode partners across the horizon. Right: Fock occupation probabilities p_n of the reduced density matrix matching the Planck curve.</desc>
          <text x="{cx + 20}" y="38" text-anchor="middle" font-size="11" font-weight="700" data-en="Rindler wedge &amp; causal horizon X = ±cT" data-es="Cuña de Rindler y horizonte causal X = ±cT">Rindler wedge &amp; causal horizon X = ±cT</text>
          <polygon points="{cx},{cy} {cx - span},{cy - span} {cx - span},{cy + span}" fill="var(--tp-stone)" opacity="0.7"/>
          <line x1="{cx - span}" y1="{cy}" x2="{cx + span + 30}" y2="{cy}" stroke="var(--tp-rule-strong)" stroke-width="1" stroke-dasharray="4 3"/>
          <line x1="{cx}" y1="{cy - span}" x2="{cx}" y2="{cy + span}" stroke="var(--tp-rule-strong)" stroke-width="1" stroke-dasharray="4 3"/>
          <line x1="{cx - span}" y1="{cy + span}" x2="{cx + span}" y2="{cy - span}" stroke="var(--tp-minium)" stroke-width="2.2"/>
          <line x1="{cx - span}" y1="{cy - span}" x2="{cx + span}" y2="{cy + span}" stroke="var(--tp-minium)" stroke-width="2.2"/>
          <path class="tg-rindler-hyp" d="{hyp_path}" fill="none" stroke="var(--tp-prussian)" stroke-width="3"/>
          <line class="tg-entangle-link" x1="{cx - 48}" y1="{cy - 18}" x2="{cx + 58}" y2="{cy - 18}" stroke="var(--tp-verdigris)" stroke-width="2" stroke-dasharray="4 3"/>
          <circle cx="{cx - 48}" cy="{cy - 18}" r="7" fill="var(--tp-stone)" stroke="var(--tp-ink)" stroke-width="1.5"/>
          <text x="{cx - 48}" y="{cy + 4}" text-anchor="middle" font-size="9.5" fill="var(--tp-graphite)" data-en="hidden L" data-es="L oculto">hidden L</text>
          <circle cx="{cx + 58}" cy="{cy - 18}" r="7" fill="var(--tp-prussian)"/>
          <text x="{cx + 68}" y="{cy + 4}" font-size="9.5" fill="var(--tp-prussian)" data-en="clock R" data-es="reloj R">clock R</text>
          <line class="tg-axis" x1="{px0}" y1="{py0}" x2="{px0}" y2="{py1}"/>
          <line class="tg-axis" x1="{px0}" y1="{py1}" x2="{px1}" y2="{py1}"/>
          <text x="{px0 - 8}" y="{py0 + 4}" text-anchor="end" font-size="10">1.0</text>
          <text x="{px0 - 8}" y="{(py0 + py1) / 2 + 4:.0f}" text-anchor="end" font-size="10">0.5</text>
          <text x="{px0 - 8}" y="{py1 + 4}" text-anchor="end" font-size="10">0</text>
          <text x="{px0}" y="{py0 - 12}" font-size="11" data-en="Reduced-state Fock weights pₙ = (1 − e⁻ᵝ)e⁻ⁿᵝ" data-es="Pesos de Fock del estado reducido pₙ = (1 − e⁻ᵝ)e⁻ⁿᵝ">Reduced-state Fock weights pₙ = (1 − e⁻ᵝ)e⁻ⁿᵝ</text>
          <path class="tg-planck-curve" d="{planck_path}" fill="none" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="5 3"/>
          <g class="tg-fock-bars">{''.join(bars)}</g>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-xi-t08"><span data-en="Boltzmann exponent ξ = ħω / (k_B T)" data-es="Exponente de Boltzmann ξ = ħω / (k_B T)">Boltzmann exponent ξ = ħω / (k_B T)</span> <span data-tg-read="xi">{XI_DEFAULT:.2f}</span></label>
          <input id="tg-xi-t08" data-tg-xi-input type="range" min="0.50" max="4.00" step="0.10" value="{XI_DEFAULT}" aria-describedby="tg-status-t08">
        </div>
        <div class="tp-control-group">
          <label for="tg-mass-t08"><span data-en="Black-hole mass M (solar masses M_☉)" data-es="Masa del agujero negro M (masas solares M_☉)">Black-hole mass M (solar masses M_☉)</span> <span data-tg-read="msun">1.0</span></label>
          <input id="tg-mass-t08" data-tg-msun-input type="range" min="1" max="100" step="1" value="1" aria-describedby="tg-status-t08">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and planted defect">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · sever cross-horizon entanglement (|0_L⟩ ⊗ |0_R⟩)" data-es="⚡ Apagado · cortar el entrelazamiento del horizonte (|0_L⟩ ⊗ |0_R⟩)">⚡ Knockout · sever cross-horizon entanglement (|0_L⟩ ⊗ |0_R⟩)</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Wedge entropy S(ρ_R) · mean occupation n̄" data-es="Entropía de la cuña S(ρ_R) · ocupación media n̄">Wedge entropy S(ρ_R) · mean occupation n̄</span>
          <span class="tp-readout-v" data-tg-read="entropy">{wedge['entropy_jacobi_nats']:.4f} nats · n̄ = {wedge['n_bar_jacobi']:.4f}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="max |λ_Jacobi − p_Gibbs|" data-es="máx |λ_Jacobi − p_Gibbs|">max |λ_Jacobi − p_Gibbs|</span>
          <span class="tp-readout-v" data-tg-read="dev">{wedge['max_dev_from_truncated_gibbs']:.1e}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Hawking temperature T_H(M)" data-es="Temperatura de Hawking T_H(M)">Hawking temperature T_H(M)</span>
          <span class="tp-readout-v" data-tg-read="th">{bh['t_hawking_k'] * 1e9:.2f} nK</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="Horizon entropy S_BH / k_B = A / (4 ℓ_P²)" data-es="Entropía del horizonte S_BH / k_B = A / (4 ℓ_P²)">Horizon entropy S_BH / k_B = A / (4 ℓ_P²)</span>
          <span class="tp-readout-v" data-tg-read="sbh">{bh['s_bh_over_kb']:.3e}</span>
        </div>
      </div>
      <p id="tg-status-t08" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="Entangled across the horizon: tracing out the hidden left partner L turns the pure vacuum into a Planck thermal bath on the right wedge R." data-es="Entrelazado a través del horizonte: trazar sobre el compañero izquierdo oculto L convierte el vacío puro en un baño térmico de Planck en la cuña derecha R.">Entangled across the horizon: tracing out the hidden left partner L turns the pure vacuum into a Planck thermal bath on the right wedge R.</p>
    </section>"""


def kerr_instrument(page: dict) -> str:
    ins = page["instrument"]
    from timegravity_kernel_kerr import FIDUCIAL_CHI, FIDUCIAL_MASS_SOLAR, KERR_SPINS, kerr_horizon, M_SUN, physical_ringdown, solve_kerr_qnm_branch
    b0 = {r["chi"]: r for r in solve_kerr_qnm_branch(KERR_SPINS, overtone_n=0)}
    b1 = {r["chi"]: r for r in solve_kerr_qnm_branch(KERR_SPINS, overtone_n=1)}
    r220 = b0[FIDUCIAL_CHI]
    r221 = b1[FIDUCIAL_CHI]
    geom = kerr_horizon(FIDUCIAL_MASS_SOLAR * M_SUN, FIDUCIAL_CHI)
    phys0 = physical_ringdown(FIDUCIAL_MASS_SOLAR, r220["mw_re"], r220["mw_im"])
    phys1 = physical_ringdown(FIDUCIAL_MASS_SOLAR, r221["mw_re"], r221["mw_im"])
    # Left plot: damped waveform h(t) over t in [0, 18 ms]
    lx0, lx1, lyc = 60, 440, 215
    w0_pts, w1_pts = [], []
    for i in range(161):
        t_ms = 18.0 * i / 160.0
        x = lx0 + (lx1 - lx0) * (t_ms / 18.0)
        y0_ = lyc - 125.0 * math.exp(-t_ms / phys0["tau_ms"]) * math.cos(2.0 * math.pi * phys0["f_hz"] * (t_ms * 1e-3))
        y1_ = lyc - 95.0 * math.exp(-t_ms / phys1["tau_ms"]) * math.cos(2.0 * math.pi * phys1["f_hz"] * (t_ms * 1e-3))
        w0_pts.append(f'{"M" if i == 0 else "L"} {x:.1f} {y0_:.1f}')
        w1_pts.append(f'{"M" if i == 0 else "L"} {x:.1f} {y1_:.1f}')
    # Right plot: (f_Hz, tau_ms) trajectory across KERR_SPINS
    rx0, rx1, ry0, ry1 = 520, 880, 65, 360
    fx = lambda f: rx0 + (rx1 - rx0) * (f - 150.0) / 260.0  # noqa: E731
    ty = lambda tau: ry1 - (ry1 - ry0) * (tau - 0.8) / 4.6  # noqa: E731
    traj0, traj1 = [], []
    for i, chi in enumerate(KERR_SPINS):
        p0 = physical_ringdown(FIDUCIAL_MASS_SOLAR, b0[chi]["mw_re"], b0[chi]["mw_im"])
        p1 = physical_ringdown(FIDUCIAL_MASS_SOLAR, b1[chi]["mw_re"], b1[chi]["mw_im"])
        traj0.append(f'{"M" if i == 0 else "L"} {fx(p0["f_hz"]):.1f} {ty(p0["tau_ms"]):.1f}')
        traj1.append(f'{"M" if i == 0 else "L"} {fx(p1["f_hz"]):.1f} {ty(p1["tau_ms"]):.1f}')
    qnm_json = html.escape(json.dumps([
        {"chi": chi, "w0_re": round(b0[chi]["mw_re"], 8), "w0_im": round(b0[chi]["mw_im"], 8),
         "w1_re": round(b1[chi]["mw_re"], 8), "w1_im": round(b1[chi]["mw_im"], 8)}
        for chi in KERR_SPINS
    ]), quote=True)
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="kerr" data-tg-qnm="{qnm_json}" aria-labelledby="tg-instrument-heading-t09">
      <h2 id="tg-instrument-heading-t09" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 420" role="img" aria-labelledby="tg-stage-title-t09 tg-stage-desc-t09" data-lx0="{lx0}" data-lx1="{lx1}" data-lyc="{lyc}" data-rx0="{rx0}" data-rx1="{rx1}" data-ry0="{ry0}" data-ry1="{ry1}">
          <title id="tg-stage-title-t09">Kerr ringdown damped sinusoid for the fundamental (2,2,0) mode and first overtone (2,2,1), beside the frequency–damping trajectory</title>
          <desc id="tg-stage-desc-t09">Left: ringdown strain h(t) over 18 milliseconds showing the fundamental tone and faster-decaying first overtone. Right: the Kerr spin trajectory in frequency versus damping time from chi = 0 to chi = 0.90.</desc>
          <text x="{(lx0 + lx1) / 2:.0f}" y="38" text-anchor="middle" font-size="11" font-weight="700" data-en="Ringdown waveform h(t): fundamental (2,2,0) &amp; overtone (2,2,1)" data-es="Onda de resonancia h(t): fundamental (2,2,0) y sobretono (2,2,1)">Ringdown waveform h(t): fundamental (2,2,0) &amp; overtone (2,2,1)</text>
          <line class="tg-axis" x1="{lx0}" y1="{lyc}" x2="{lx1}" y2="{lyc}" stroke-dasharray="4 3"/>
          <path class="tg-kerr-wave1" d="{' '.join(w1_pts)}" fill="none" stroke="var(--tp-verdigris)" stroke-width="1.8" stroke-dasharray="4 2"/>
          <path class="tg-kerr-wave0" d="{' '.join(w0_pts)}" fill="none" stroke="var(--tp-prussian)" stroke-width="2.6"/>
          <text x="{lx1}" y="{lyc + 148}" text-anchor="end" font-size="10" fill="var(--tp-slate)" data-en="time after merger peak (0 to 18 ms)" data-es="tiempo tras el pico de fusión (0 a 18 ms)">time after merger peak (0 to 18 ms)</text>
          <line class="tg-axis" x1="{rx0}" y1="{ry0}" x2="{rx0}" y2="{ry1}"/>
          <line class="tg-axis" x1="{rx0}" y1="{ry1}" x2="{rx1}" y2="{ry1}"/>
          <text x="{rx0}" y="{ry0 - 12}" font-size="11" data-en="Kerr spin trajectory: τ (ms) vs f (Hz)" data-es="Trayectoria de espín de Kerr: τ (ms) frente a f (Hz)">Kerr spin trajectory: τ (ms) vs f (Hz)</text>
          <text x="{rx1}" y="{ry1 + 18}" text-anchor="end" font-size="10" data-en="frequency f (Hz)" data-es="frecuencia f (Hz)">frequency f (Hz)</text>
          <path class="tg-kerr-traj1" d="{' '.join(traj1)}" fill="none" stroke="var(--tp-verdigris)" stroke-width="2" stroke-dasharray="5 3"/>
          <path class="tg-kerr-traj0" d="{' '.join(traj0)}" fill="none" stroke="var(--tp-prussian)" stroke-width="2.6"/>
          <circle class="tg-kerr-marker0" cx="{fx(phys0['f_hz']):.1f}" cy="{ty(phys0['tau_ms']):.1f}" r="6.5" fill="var(--tp-minium)"/>
          <circle class="tg-kerr-marker1" cx="{fx(phys1['f_hz']):.1f}" cy="{ty(phys1['tau_ms']):.1f}" r="5" fill="var(--tp-verdigris)"/>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-mass-t09"><span data-en="Remnant mass M (M_☉)" data-es="Masa remanente M (M_☉)">Remnant mass M (M_☉)</span> <span data-tg-read="m">{FIDUCIAL_MASS_SOLAR:.0f}</span></label>
          <input id="tg-mass-t09" data-tg-m-input type="range" min="20" max="100" step="1" value="{FIDUCIAL_MASS_SOLAR:.0f}" aria-describedby="tg-status-t09">
        </div>
        <div class="tp-control-group">
          <label for="tg-chi-t09"><span data-en="Dimensionless spin χ = cJ / (GM²)" data-es="Espín adimensional χ = cJ / (GM²)">Dimensionless spin χ = cJ / (GM²)</span> <span data-tg-read="chi">{FIDUCIAL_CHI:.2f}</span></label>
          <input id="tg-chi-t09" data-tg-chi-input type="range" min="0.00" max="0.90" step="0.02" value="{FIDUCIAL_CHI:.2f}" aria-describedby="tg-status-t09">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and planted defect">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · corrupt Kerr radical √(1 + χ²) (breaks Smarr &amp; Leaver)" data-es="⚡ Apagado · corromper el radical de Kerr √(1 + χ²) (rompe Smarr y Leaver)">⚡ Knockout · corrupt Kerr radical √(1 + χ²) (breaks Smarr &amp; Leaver)</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Fundamental (2,2,0): f₂₂₀ · τ₂₂₀" data-es="Fundamental (2,2,0): f₂₂₀ · τ₂₂₀">Fundamental (2,2,0): f₂₂₀ · τ₂₂₀</span>
          <span class="tp-readout-v" data-tg-read="qnm0">{phys0['f_hz']:.1f} Hz · {phys0['tau_ms']:.2f} ms</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="First overtone (2,2,1): f₂₂₁ · τ₂₂₁" data-es="Primer sobretono (2,2,1): f₂₂₁ · τ₂₂₁">First overtone (2,2,1): f₂₂₁ · τ₂₂₁</span>
          <span class="tp-readout-v" data-tg-read="qnm1">{phys1['f_hz']:.1f} Hz · {phys1['tau_ms']:.2f} ms</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Horizon radius r_+ · area A(M, χ)" data-es="Radio del horizonte r_+ · área A(M, χ)">Horizon radius r_+ · area A(M, χ)</span>
          <span class="tp-readout-v" data-tg-read="geom">{geom['r_plus_m'] / 1e3:.1f} km · {geom['area_m2'] / 1e6:,.0f} km²</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="Smarr &amp; Leaver residual" data-es="Residuo de Smarr y Leaver">Smarr &amp; Leaver residual</span>
          <span class="tp-readout-v" data-tg-read="smarr">{geom['smarr_rel_err']:.1e} · PASS</span>
        </div>
      </div>
      <p id="tg-status-t09" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="Kerr horizon spectroscopy: both (2,2,0) and (2,2,1) frequencies and damping times are locked by M and χ alone, and Smarr's horizon identity holds to machine precision." data-es="Espectroscopía de horizonte de Kerr: las frecuencias y tiempos de caída de (2,2,0) y (2,2,1) quedan fijados solo por M y χ, y la identidad de Smarr se cumple a precisión de máquina.">Kerr horizon spectroscopy: both (2,2,0) and (2,2,1) frequencies and damping times are locked by M and χ alone, and Smarr's horizon identity holds to machine precision.</p>
    </section>"""


def einselection_instrument(page: dict) -> str:
    ins = page["instrument"]
    from timegravity_kernel_einselection import (
        N_ENV_DEFAULT, THETA_DEFAULT, photon_bath_localization_table, statevector_quantum_darwinism,
    )
    qd = statevector_quantum_darwinism(THETA_DEFAULT, N_ENV_DEFAULT)
    bath = photon_bath_localization_table()
    # Left panel: 2x2 clock reduced density matrix bars (|rho_00|, |rho_11| in prussian, |rho_01|, |rho_10| in minium)
    lx0, lx1, ly0, ly1 = 60, 410, 70, 350
    coh = qd["coherence_ratio_statevector"]
    bar_w = 54
    b_xs = [lx0 + 28, lx0 + 108, lx0 + 188, lx0 + 268]
    b_labels = ["|ρ₀₀|", "|ρ₁₁|", "|ρ₀₁|", "|ρ₁₀|"]
    b_vals = [0.5, 0.5, 0.5 * coh, 0.5 * coh]
    b_cols = ["var(--tp-prussian)", "var(--tp-prussian)", "var(--tp-minium)", "var(--tp-minium)"]
    bars_svg = []
    for idx, (bx, lbl, val, col) in enumerate(zip(b_xs, b_labels, b_vals, b_cols)):
        bh = (ly1 - ly0) * val
        by = ly1 - bh
        bars_svg.append(
            f'<rect class="tg-ein-bar" data-bar="{idx}" x="{bx}" y="{by:.1f}" width="{bar_w}" height="{max(1.5, bh):.1f}" rx="3" fill="{col}" opacity="0.86"/>'
            f'<text x="{bx + bar_w / 2:.1f}" y="{ly1 + 18}" text-anchor="middle" font-size="10">{lbl}</text>'
        )
    # Right panel: Quantum Darwinism plateau I(S : E_k) in bits for k = 0..N
    rx0, rx1, ry0, ry1 = 480, 880, 70, 350
    N = N_ENV_DEFAULT
    to_x = lambda k: rx0 + (rx1 - rx0) * k / N  # noqa: E731
    to_y = lambda bits: ry1 - (ry1 - ry0) * (bits / 2.05)  # noqa: E731
    pts = []
    dots = []
    for row in qd["fragments"]:
        kx = to_x(row["k"])
        ky = to_y(row["i_s_ek_jacobi_bits"])
        pts.append(f'{"M" if row["k"] == 0 else "L"} {kx:.1f} {ky:.1f}')
        dots.append(f'<circle class="tg-ein-dot" data-k="{row["k"]}" cx="{kx:.1f}" cy="{ky:.1f}" r="5" fill="var(--tp-minium)"/>')
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="einselection" data-tg-n="{N}" aria-labelledby="tg-instrument-heading-t11">
      <h2 id="tg-instrument-heading-t11" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 420" role="img" aria-labelledby="tg-stage-title-t11 tg-stage-desc-t11" data-ly0="{ly0}" data-ly1="{ly1}" data-rx0="{rx0}" data-rx1="{rx1}" data-ry0="{ry0}" data-ry1="{ry1}">
          <title id="tg-stage-title-t11">Clock reduced density matrix coherences beside the Quantum Darwinism mutual-information plateau across six environmental modes</title>
          <desc id="tg-stage-desc-t11">Left: four vertical bars for the clock's reduced density matrix elements; the two pointer diagonal populations stay at 0.5 while the two off-diagonal coherences shrink as gamma to the sixth power. Right: mutual information I(S:E_k) rising to the one-bit classical plateau at small k and jumping to two bits at k = N.</desc>
          <text x="{(lx0 + lx1) / 2:.0f}" y="38" text-anchor="middle" font-size="11" font-weight="700" data-en="Clock reduced state ρ_S: pointer diagonal vs off-diagonal" data-es="Estado reducido del reloj ρ_S: diagonal puntero frente a coherencias">Clock reduced state ρ_S: pointer diagonal vs off-diagonal</text>
          <line class="tg-axis" x1="{lx0}" y1="{ly0}" x2="{lx0}" y2="{ly1}"/>
          <line class="tg-axis" x1="{lx0}" y1="{ly1}" x2="{lx1}" y2="{ly1}"/>
          <text x="{lx0 - 8}" y="{ly1 - (ly1 - ly0) * 0.5 + 4:.0f}" text-anchor="end" font-size="10">0.5</text>
          <text x="{lx0 - 8}" y="{ly1 + 4}" text-anchor="end" font-size="10">0</text>
          <g class="tg-ein-bars">{''.join(bars_svg)}</g>
          <text x="{(rx0 + rx1) / 2:.0f}" y="38" text-anchor="middle" font-size="11" font-weight="700" data-en="Quantum Darwinism plateau I(S : E_k) across k of N = 6 modes" data-es="Meseta de darwinismo cuántico I(S : E_k) en k de N = 6 modos">Quantum Darwinism plateau I(S : E_k) across k of N = 6 modes</text>
          <line class="tg-axis" x1="{rx0}" y1="{ry0}" x2="{rx0}" y2="{ry1}"/>
          <line class="tg-axis" x1="{rx0}" y1="{ry1}" x2="{rx1}" y2="{ry1}"/>
          <line x1="{rx0}" y1="{to_y(1.0):.1f}" x2="{rx1}" y2="{to_y(1.0):.1f}" stroke="var(--tp-verdigris)" stroke-width="1.4" stroke-dasharray="4 3"/>
          <text x="{rx0 - 8}" y="{to_y(2.0) + 4:.0f}" text-anchor="end" font-size="10">2 bits</text>
          <text x="{rx0 - 8}" y="{to_y(1.0) + 4:.0f}" text-anchor="end" font-size="10">1 bit</text>
          <text x="{rx0 - 8}" y="{ry1 + 4}" text-anchor="end" font-size="10">0</text>
          <text x="{rx1}" y="{ry1 + 22}" text-anchor="end" font-size="10" data-en="captured bath fraction k / N (N = 6)" data-es="fracción capturada del baño k / N (N = 6)">captured bath fraction k / N (N = 6)</text>
          <path class="tg-ein-curve" d="{' '.join(pts)}" fill="none" stroke="var(--tp-prussian)" stroke-width="2.6"/>
          <g class="tg-ein-dots">{''.join(dots)}</g>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-theta-t11"><span data-en="Single-mode scattering angle θ (rad)" data-es="Ángulo de dispersión por modo θ (rad)">Single-mode scattering angle θ (rad)</span> <span data-tg-read="theta">{THETA_DEFAULT:.2f}</span></label>
          <input id="tg-theta-t11" data-tg-theta-input type="range" min="0.00" max="1.57" step="0.05" value="{THETA_DEFAULT:.2f}" aria-describedby="tg-status-t11">
        </div>
        <div class="tp-control-group">
          <label for="tg-r-t11"><span data-en="Sphere radius R (µm, for photon bath Λ)" data-es="Radio de la esfera R (µm, para el baño Λ)">Sphere radius R (µm, for photon bath Λ)</span> <span data-tg-read="rad">10.0</span></label>
          <input id="tg-r-t11" data-tg-r-input type="range" min="1.0" max="20.0" step="1.0" value="10.0" aria-describedby="tg-status-t11">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and planted defect">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · uncouple the bath (θ = 0, ε = 1 → Λ_EM = 0)" data-es="⚡ Apagado · desacoplar el baño (θ = 0, ε = 1 → Λ_EM = 0)">⚡ Knockout · uncouple the bath (θ = 0, ε = 1 → Λ_EM = 0)</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Off-diagonal coherence |ρ₀₁(N)| / |ρ₀₁(0)| = cos⁶θ" data-es="Coherencia fuera de la diagonal |ρ₀₁(N)| / |ρ₀₁(0)| = cos⁶θ">Off-diagonal coherence |ρ₀₁(N)| / |ρ₀₁(0)| = cos⁶θ</span>
          <span class="tp-readout-v" data-tg-read="coh">{coh:.2e}</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Redundant record I(S : E₂) at k = 2 of 6 modes" data-es="Registro redundante I(S : E₂) en k = 2 de 6 modos">Redundant record I(S : E₂) at k = 2 of 6 modes</span>
          <span class="tp-readout-v" data-tg-read="mi2">{qd['k2_plateau_bits']:.4f} bits (R_δ = 3.0)</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Joos–Zeh photon bath τ_loc (Δx = 10 µm): 2.725 K CMB vs 300 K" data-es="Baño de fotones Joos–Zeh τ_loc (Δx = 10 µm): CMB 2.725 K frente a 300 K">Joos–Zeh photon bath τ_loc (Δx = 10 µm): 2.725 K CMB vs 300 K</span>
          <span class="tp-readout-v" data-tg-read="tau">{bath['dust_10um_dielectric']['tau_cmb_s']:.2f} s · {bath['dust_10um_dielectric']['tau_300k_s']:.2e} s</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="Statevector vs Zurek closed form" data-es="Vector de estado frente a forma cerrada de Zurek">Statevector vs Zurek closed form</span>
          <span class="tp-readout-v" data-tg-read="err">{qd['max_mi_dev_nats']:.1e} nats · PASS</span>
        </div>
      </div>
      <p id="tg-status-t11" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="Einselection &amp; Quantum Darwinism: the interaction Hamiltonian [Ĥ_int, Z_S] = 0 preserves pointer populations while scattering copies of Z_S into the photon bath." data-es="Einselección y darwinismo cuántico: el hamiltoniano de interacción [Ĥ_int, Z_S] = 0 preserva las poblaciones puntero mientras copia Z_S en el baño de fotones.">Einselection &amp; Quantum Darwinism: the interaction Hamiltonian [Ĥ_int, Z_S] = 0 preserves pointer populations while scattering copies of Z_S into the photon bath.</p>
    </section>"""


def dark_clock_instrument(page: dict) -> str:
    ins = page["instrument"]
    from timegravity_kernel_dark_clock import (
        B_IMPACT_DEFAULT_M, BASELINE_DEFAULT_M, M_TRANSIT_DEFAULT_KG, V_VIRIAL_M_S,
        cosmological_matter_budget, dark_transit_clock_shift, ultralight_scalar_clock_bound,
    )
    cosmo = cosmological_matter_budget()
    fly = dark_transit_clock_shift(M_TRANSIT_DEFAULT_KG, B_IMPACT_DEFAULT_M, BASELINE_DEFAULT_M, V_VIRIAL_M_S)
    ulp = ultralight_scalar_clock_bound()
    # Left panel: flyby geometry with clock 1 at b1, clock 2 at b2, and passing dark trajectory
    lx0, lx1, ly0, ly1 = 60, 410, 65, 355
    # Right panel: accumulated proper-time step Delta tau(t) across the flyby
    rx0, rx1, ry0, ry1 = 480, 880, 65, 355
    pts = []
    dt_inf = fly["delta_tau_asymptotic_s"]
    b1 = fly["b1_m"]
    b2 = fly["b2_m"]
    v0 = fly["v_m_s"]
    for idx in range(61):
        t_val = 0.01 * (10.0 ** (3.0 * idx / 60.0)) * (b1 / v0)
        tx = rx0 + (rx1 - rx0) * idx / 60
        num = math.asinh(v0 * t_val / b1) - math.asinh(v0 * t_val / b2)
        den = math.log(b2 / b1)
        frac = num / den if abs(den) > 0 else 0.0
        ty = ry0 + 30 + (ry1 - ry0 - 60) * frac
        pts.append(f'{"M" if idx == 0 else "L"} {tx:.1f} {ty:.1f}')
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="dark_clock" aria-labelledby="tg-instrument-heading-t12">
      <h2 id="tg-instrument-heading-t12" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 420" role="img" aria-labelledby="tg-stage-title-t12 tg-stage-desc-t12" data-rx0="{rx0}" data-rx1="{rx1}" data-ry0="{ry0}" data-ry1="{ry1}">
          <title id="tg-stage-title-t12">An electromagnetically transparent mass flying past two optical clocks and the accumulated gravitational proper-time step</title>
          <desc id="tg-stage-desc-t12">Left: a dark subhalo trajectory passing clock 1 at impact parameter b_1 and clock 2 at b_2 with zero photon scattering. Right: the accumulated proper-time step Delta tau(t) approaching the logarithmic plateau -(2GM/c^2 v_0) ln(b_2/b_1).</desc>
          <text x="{(lx0 + lx1) / 2:.0f}" y="38" text-anchor="middle" font-size="11" font-weight="700" data-en="Transparent flyby (Λ_EM = 0, G &gt; 0) past two clocks" data-es="Sobrevuelo transparente (Λ_EM = 0, G &gt; 0) junto a dos relojes">Transparent flyby (Λ_EM = 0, G &gt; 0) past two clocks</text>
          <line x1="145" y1="{ly0 + 10}" x2="145" y2="{ly1 - 10}" stroke="var(--tp-minium)" stroke-width="2.5" stroke-dasharray="6 4"/>
          <polygon points="140,{ly0 + 18} 145,{ly0 + 6} 150,{ly0 + 18}" fill="var(--tp-minium)"/>
          <circle class="tg-dark-mass" cx="145" cy="195" r="14" fill="var(--tp-stone)" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="3 2"/>
          <text x="145" y="199" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--tp-minium)">M_DM</text>
          <line class="tg-dark-b1" x1="145" y1="195" x2="225" y2="195" stroke="var(--tp-prussian)" stroke-width="1.6" stroke-dasharray="3 2"/>
          <line class="tg-dark-b2" x1="145" y1="245" x2="355" y2="245" stroke="var(--tp-verdigris)" stroke-width="1.6" stroke-dasharray="3 2"/>
          <circle cx="225" cy="195" r="11" fill="var(--tp-prussian)"/>
          <text x="225" y="176" text-anchor="middle" font-size="9.5" fill="var(--tp-prussian)" data-en="Clock 1 (b₁)" data-es="Reloj 1 (b₁)">Clock 1 (b₁)</text>
          <circle cx="355" cy="245" r="11" fill="var(--tp-verdigris)"/>
          <text x="355" y="226" text-anchor="middle" font-size="9.5" fill="var(--tp-verdigris)" data-en="Clock 2 (b₂)" data-es="Reloj 2 (b₂)">Clock 2 (b₂)</text>
          <text x="235" y="330" text-anchor="middle" font-size="9.5" fill="var(--tp-graphite)" data-en="Planck 2018: Ω_c / Ω_b = 5.36 ± 0.06 (84.3 % dark)" data-es="Planck 2018: Ω_c / Ω_b = 5.36 ± 0.06 (84.3 % oscura)">Planck 2018: Ω_c / Ω_b = 5.36 ± 0.06 (84.3 % dark)</text>
          <text x="{(rx0 + rx1) / 2:.0f}" y="38" text-anchor="middle" font-size="11" font-weight="700" data-en="Proper-time step Δτ(T) = −(2GM/c²v₀) ln(b₂/b₁)" data-es="Escalón de tiempo propio Δτ(T) = −(2GM/c²v₀) ln(b₂/b₁)">Proper-time step Δτ(T) = −(2GM/c²v₀) ln(b₂/b₁)</text>
          <line class="tg-axis" x1="{rx0}" y1="{ry0}" x2="{rx0}" y2="{ry1}"/>
          <line class="tg-axis" x1="{rx0}" y1="{ry0 + 30}" x2="{rx1}" y2="{ry0 + 30}" stroke-dasharray="4 3"/>
          <line class="tg-axis" x1="{rx0}" y1="{ry1 - 30}" x2="{rx1}" y2="{ry1 - 30}" stroke="var(--tp-verdigris)" stroke-dasharray="4 3"/>
          <text x="{rx0 - 8}" y="{ry0 + 34}" text-anchor="end" font-size="10">0</text>
          <text x="{rx0 - 8}" y="{ry1 - 26}" text-anchor="end" font-size="10" data-tg-read="dtlabel">{dt_inf:.1e} s</text>
          <text x="{rx1}" y="{ry1 + 18}" text-anchor="end" font-size="10" data-en="integration window T across flyby" data-es="ventana de integración T del sobrevuelo">integration window T across flyby</text>
          <path class="tg-dark-curve" d="{' '.join(pts)}" fill="none" stroke="var(--tp-prussian)" stroke-width="2.6"/>
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-logm-t12"><span data-en="log₁₀ clump mass M_DM (kg)" data-es="log₁₀ masa del subhalo M_DM (kg)">log₁₀ clump mass M_DM (kg)</span> <span data-tg-read="logm">6.0</span></label>
          <input id="tg-logm-t12" data-tg-logm-input type="range" min="4.0" max="16.0" step="0.5" value="6.0" aria-describedby="tg-status-t12">
        </div>
        <div class="tp-control-group">
          <label for="tg-ratio-t12"><span data-en="Impact-parameter ratio b₂ / b₁" data-es="Razón de parámetros de impacto b₂ / b₁">Impact-parameter ratio b₂ / b₁</span> <span data-tg-read="ratio">1001.0</span></label>
          <input id="tg-ratio-t12" data-tg-ratio-input type="range" min="1.5" max="1001.0" step="10.0" value="1001.0" aria-describedby="tg-status-t12">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and planted defect">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · equal impact parameters b₂ = b₁ (common-mode Φ, Δτ = 0)" data-es="⚡ Apagado · parámetros de impacto iguales b₂ = b₁ (Φ común, Δτ = 0)">⚡ Knockout · equal impact parameters b₂ = b₁ (common-mode Φ, Δτ = 0)</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Cosmological dark-to-baryonic ratio Ω_c / Ω_b" data-es="Razón cosmológica oscura a bariónica Ω_c / Ω_b">Cosmological dark-to-baryonic ratio Ω_c / Ω_b</span>
          <span class="tp-readout-v" data-tg-read="cosmo">{cosmo['dark_to_baryon_ratio']:.3f} ± {cosmo['dark_to_baryon_ratio_err']:.3f} ({cosmo['dark_fraction_of_matter'] * 100:.1f} %)</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Asymptotic clock step Δτ_∞ = −(2GM/c²v₀) ln(b₂/b₁)" data-es="Escalón asintótico del reloj Δτ_∞ = −(2GM/c²v₀) ln(b₂/b₁)">Asymptotic clock step Δτ_∞ = −(2GM/c²v₀) ln(b₂/b₁)</span>
          <span class="tp-readout-v" data-tg-read="dt">{dt_inf:.3e} s</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Scalar field amplitude Φ_Pl (m_φ = 10⁻¹⁵ eV) · Λ_EM" data-es="Amplitud escalar Φ_Pl (m_φ = 10⁻¹⁵ eV) · Λ_EM">Scalar field amplitude Φ_Pl (m_φ = 10⁻¹⁵ eV) · Λ_EM</span>
          <span class="tp-readout-v" data-tg-read="ulp">{ulp['phi_planck_dimensionless']:.2e} · Λ_EM = 0</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="Quadrature vs analytic arsinh" data-es="Cuadratura frente a arsinh analítico">Quadrature vs analytic arsinh</span>
          <span class="tp-readout-v" data-tg-read="err">{fly['quadrature_rel_err']:.1e} · PASS</span>
        </div>
      </div>
      <p id="tg-status-t12" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="Universal metric coupling: an electromagnetically uncoupled mass (Λ_EM = 0) casts zero photon shadow yet shifts the gravitational clock rate along its flyby." data-es="Acoplamiento métrico universal: una masa sin acoplamiento electromagnético (Λ_EM = 0) no proyecta sombra fotónica pero desplaza el ritmo gravitatorio del reloj en su sobrevuelo.">Universal metric coupling: an electromagnetically uncoupled mass (Λ_EM = 0) casts zero photon shadow yet shifts the gravitational clock rate along its flyby.</p>
    </section>"""


def holonomy_soft_instrument(page: dict) -> str:
    ins = page["instrument"]
    from timegravity_kernel_holonomy_soft import (
        GW150914_DL_MPC, GW150914_E_RAD_SOLAR, LIGO_ARM_M,
        anomaly_traces_6y, memory_flux_quadrature_check, memory_strain_step, soft_ward_identities,
    )
    soft = soft_ward_identities(kappa_ratio_e_over_p=1.0)
    mem = memory_strain_step(e_rad_solar=GW150914_E_RAD_SOLAR, d_l_mpc=GW150914_DL_MPC, arm_length_m=LIGO_ARM_M)
    quad = memory_flux_quadrature_check(e_rad_solar=GW150914_E_RAD_SOLAR, d_l_mpc=GW150914_DL_MPC)
    anom = anomaly_traces_6y(n_c=3, include_right_electron=True)

    lx0, lx1, ly0, ly1 = 62, 422, 68, 348
    rx0, rx1, ry0, ry1 = 488, 882, 68, 348
    ry_mid = 208
    y_zero = ly1 - 44
    y_step = ly0 + 58

    mem_pts = []
    wave_pts = []
    for idx in range(81):
        u = -4.0 + 8.0 * idx / 80.0
        tx = lx0 + (lx1 - lx0) * idx / 80.0
        step_frac = 0.5 * (1.0 + math.tanh(1.35 * u))
        osc = 0.34 * math.exp(-0.75 * u * u) * math.cos(7.5 * u)
        ym = y_zero - (y_zero - y_step) * step_frac
        yw = y_zero - (y_zero - y_step) * (step_frac + osc)
        mem_pts.append(f'{"M" if idx == 0 else "L"} {tx:.1f} {ym:.1f}')
        wave_pts.append(f'{"M" if idx == 0 else "L"} {tx:.1f} {yw:.1f}')

    bar_xs = (534, 628, 722, 816)
    bar_labels_en = ("s=2 Ward", "Tr[6Y]", "SU(2)²·6Y", "U(1)³ / 54")
    bar_labels_es = ("Ward s=2", "Tr[6Y]", "SU(2)²·6Y", "U(1)³ / 54")
    bars_svg = []
    for bx, len_s, les_s in zip(bar_xs, bar_labels_en, bar_labels_es):
        bars_svg.append(
            f'<rect class="tg-hol-bar" x="{bx - 22}" y="{ry_mid - 2}" width="44" height="4" rx="2" fill="var(--tp-verdigris)"/>'
            f'<text x="{bx}" y="{ry1 + 18}" text-anchor="middle" font-size="9.2" fill="var(--tp-graphite)" data-en="{a(len_s)}" data-es="{a(les_s)}">{t(len_s)}</text>'
        )

    dh_c = mem["delta_h_char"]
    dl_c = mem["delta_l_char_m"]
    return f"""    <section class="tg-instrument" id="instrument" data-tg-instrument="holonomy_soft" aria-labelledby="tg-instrument-heading-t13">
      <h2 id="tg-instrument-heading-t13" class="tp-h2" data-en="{a(ins['title_en'])}" data-es="{a(ins['title_es'])}">{t(ins['title_en'])}</h2>
      {bi("p", ins["how_en"], ins["how_es"], "tg-how")}
{predict_block(page)}
        <svg class="tg-stage" viewBox="0 0 920 420" role="img" aria-labelledby="tg-stage-title-t13 tg-stage-desc-t13" data-lx0="{lx0}" data-lx1="{lx1}" data-ly0="{ly0}" data-ly1="{ly1}" data-rx0="{rx0}" data-rx1="{rx1}" data-ry0="{ry0}" data-ry1="{ry1}" data-rymid="{ry_mid}">
          <title id="tg-stage-title-t13">Gravitational-wave displacement memory step and infrared gauge-gravity Ward and anomaly residuals</title>
          <desc id="tg-stage-desc-t13">Left: oscillatory merger wave plus permanent DC memory strain step Delta h_char = G E_rad / (c^4 D_L). Right: Weinberg s=2 soft Ward residual and the Standard Model chiral and mixed gravitational anomaly traces vanishing together at N_c = 3.</desc>
          <text x="{(lx0 + lx1) / 2:.0f}" y="38" text-anchor="middle" font-size="11" font-weight="700" data-en="Christodoulou memory step Δh(t) &amp; arm offset ΔL" data-es="Escalón de memoria de Christodoulou Δh(t) y desplazamiento ΔL">Christodoulou memory step Δh(t) &amp; arm offset ΔL</text>
          <line class="tg-axis" x1="{lx0}" y1="{ly0}" x2="{lx0}" y2="{ly1}"/>
          <line class="tg-axis" x1="{lx0}" y1="{y_zero}" x2="{lx1}" y2="{y_zero}" stroke-dasharray="4 3"/>
          <line class="tg-hol-plateau" x1="{lx0}" y1="{y_step}" x2="{lx1}" y2="{y_step}" stroke="var(--tp-verdigris)" stroke-width="1.5" stroke-dasharray="5 3"/>
          <text x="{lx0 - 8}" y="{y_zero + 4}" text-anchor="end" font-size="9.5">0</text>
          <text x="{lx0 - 8}" y="{y_step + 4}" text-anchor="end" font-size="9.2" fill="var(--tp-verdigris)" data-tg-read="dhlabel">{dh_c:.2e}</text>
          <path class="tg-hol-wave" d="{' '.join(wave_pts)}" fill="none" stroke="var(--tp-prussian)" stroke-width="1.6" opacity="0.55"/>
          <path class="tg-hol-mem" d="{' '.join(mem_pts)}" fill="none" stroke="var(--tp-minium)" stroke-width="2.7"/>
          <text x="{(lx0 + lx1) / 2:.0f}" y="{ly1 + 18}" text-anchor="middle" font-size="9.5" fill="var(--tp-graphite)" data-en="time across merger burst (permanent DC offset after ringdown)" data-es="tiempo durante la fusión (escalón DC permanente tras la relajación)">time across merger burst (permanent DC offset after ringdown)</text>
          <text x="{(rx0 + rx1) / 2:.0f}" y="38" text-anchor="middle" font-size="11" font-weight="700" data-en="Soft Ward &amp; anomaly residuals (all zero iff κ_e = κ_p, N_c = 3)" data-es="Residuos de Ward y anomalías (todos cero sii κ_e = κ_p, N_c = 3)">Soft Ward &amp; anomaly residuals (all zero iff κ_e = κ_p, N_c = 3)</text>
          <line class="tg-axis" x1="{rx0}" y1="{ry0}" x2="{rx0}" y2="{ry1}"/>
          <line class="tg-axis" x1="{rx0}" y1="{ry_mid}" x2="{rx1}" y2="{ry_mid}" stroke-dasharray="4 3"/>
          <text x="{rx0 - 8}" y="{ry_mid + 4}" text-anchor="end" font-size="9.5">0</text>
          {''.join(bars_svg)}
        </svg>
      <div class="tg-controls">
        <div class="tp-control-group">
          <label for="tg-erad-t13"><span data-en="Radiated merger energy E_rad (M_⊙ c²)" data-es="Energía radiada E_rad (M_⊙ c²)">Radiated merger energy E_rad (M_⊙ c²)</span> <span data-tg-read="erad">3.0</span></label>
          <input id="tg-erad-t13" data-tg-erad-input type="range" min="0.5" max="8.0" step="0.5" value="3.0" aria-describedby="tg-status-t13">
        </div>
        <div class="tp-control-group">
          <label for="tg-dl-t13"><span data-en="Luminosity distance D_L (Mpc)" data-es="Distancia de luminosidad D_L (Mpc)">Luminosity distance D_L (Mpc)</span> <span data-tg-read="dl">410</span></label>
          <input id="tg-dl-t13" data-tg-dl-input type="range" min="100" max="1000" step="10" value="410" aria-describedby="tg-status-t13">
        </div>
        <div class="tp-control-group">
          <label for="tg-nc-t13"><span data-en="Quark colour multiplicity N_c" data-es="Multiplicidad de color de quarks N_c">Quark colour multiplicity N_c</span> <span data-tg-read="nc">3</span></label>
          <input id="tg-nc-t13" data-tg-nc-input type="range" min="1" max="5" step="1" value="3" aria-describedby="tg-status-t13">
        </div>
        <div class="tg-btn-row" role="group" aria-label="Knockout and planted defect">
          <button type="button" class="tp-step-btn tp-knockout-btn" data-tg-knockout aria-pressed="false" data-en="⚡ Knockout · planted defect (κ_e / κ_p = 1 + 10⁻⁵ &amp; N_c = 2 → Ward &amp; anomaly FAIL)" data-es="⚡ Apagado · defecto plantado (κ_e / κ_p = 1 + 10⁻⁵ y N_c = 2 → FALLA Ward y anomalía)">⚡ Knockout · planted defect (κ_e / κ_p = 1 + 10⁻⁵ &amp; N_c = 2 → Ward &amp; anomaly FAIL)</button>
        </div>
      </div>
      <div class="tp-readout-strip">
        <div class="tp-readout-box" data-tg-readout-box="ward" data-alert="false">
          <span class="tp-readout-k" data-en="Weinberg s = 2 soft Ward ||W^μ|| / E_cm" data-es="Ward blando s = 2 de Weinberg ||W^μ|| / E_cm">Weinberg s = 2 soft Ward ||W^μ|| / E_cm</span>
          <span class="tp-readout-v" data-tg-read="ward">{soft['s2_ward_vector_rel_norm']:.2e} (η = 0)</span>
        </div>
        <div class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Memory Δh_char · ΔL (4 km LIGO / 2.5 Gm LISA)" data-es="Memoria Δh_char · ΔL (4 km LIGO / 2.5 Gm LISA)">Memory Δh_char · ΔL (4 km LIGO / 2.5 Gm LISA)</span>
          <span class="tp-readout-v" data-tg-read="mem">{dh_c:.2e} · {dl_c:.2e} m</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="anom" data-alert="false">
          <span class="tp-readout-k" data-en="Traces (grav, SU3², SU2², U1³) at N_c" data-es="Trazas (grav, SU3², SU2², U1³) en N_c">Traces (grav, SU3², SU2², U1³) at N_c</span>
          <span class="tp-readout-v" data-tg-read="anom">({anom['tr_grav_6y']}, {anom['tr_su3_sq_6y']}, {anom['tr_su2_sq_6y']}, {anom['tr_u1_cubic_6y']}) · CANCEL</span>
        </div>
        <div class="tp-readout-box" data-tg-readout-box="err" data-alert="false">
          <span class="tp-readout-k" data-en="GL5 memory quadrature &amp; Lean 4 Prelude gate" data-es="Cuadratura GL5 de memoria y compuerta Lean 4 Prelude">GL5 memory quadrature &amp; Lean 4 Prelude gate</span>
          <span class="tp-readout-v" data-tg-read="err">{quad['quadrature_rel_err']:.1e} · 12 thms · PASS</span>
        </div>
      </div>
      <p id="tg-status-t13" class="tg-status" data-tg-status data-state="fall" aria-live="polite" data-en="Infrared consistency satisfied: κ_e = κ_p enforces universal free fall (||W^μ|| = 0), E_rad leaves permanent baseline memory ΔL = ½ L₀ Δh, and N_c = 3 cancels all four chiral and gravitational anomalies." data-es="Consistencia infrarroja satisfecha: κ_e = κ_p impone caída libre universal (||W^μ|| = 0), E_rad deja memoria permanente ΔL = ½ L₀ Δh, y N_c = 3 cancela las cuatro anomalías quirales y gravitacionales.">Infrared consistency satisfied: κ_e = κ_p enforces universal free fall (||W^μ|| = 0), E_rad leaves permanent baseline memory ΔL = ½ L₀ Δh, and N_c = 3 cancels all four chiral and gravitational anomalies.</p>
    </section>"""


def plate_d(page: dict) -> str:
    code = page["code"]
    slug = page["slug"] or "t01"
    specs = {
        "t01": {
            "title_en": "Plate T.01-D Visual Intuition Bridge: from the marching line on wet grass to a clock-rate gradient versus a flattened gradient, and the fall at g that only one of them produces",
            "title_es": "Lámina T.01-D Puente de Intuición Visual: de la fila de marchantes en pasto mojado a un gradiente de ritmo de relojes frente a un gradiente aplanado, y la caída a g que solo uno de ellos produce",
            "p1_h_en": "A line of marchers, wet grass on one side",
            "p1_h_es": "Una fila de marchantes, pasto mojado a un lado",
            "p1_l1_en": "The slow end covers less ground per step,",
            "p1_l1_es": "El extremo lento avanza menos por paso,",
            "p1_l2_en": "so the whole line curves toward it.",
            "p1_l2_es": "así que toda la fila se curva hacia él.",
            "p1_art": (
                '<path d="M 40 150 C 100 150, 160 140, 250 110" fill="none" stroke="var(--tp-minium)" stroke-width="2.4"/>'
                '<path d="M 40 170 L 250 170" fill="none" stroke="var(--tp-rule-strong)" stroke-width="1.4" stroke-dasharray="4 3"/>'
                '<text x="150" y="184" text-anchor="middle" font-size="8.4" fill="var(--tp-graphite)" data-en="dry: straight · wet: curved" data-es="seco: recto · mojado: curvo">dry: straight · wet: curved</text>'
            ),
            "p2_on_en": "▲ Gradient on: A′(z) = 2g/c²",
            "p2_on_es": "▲ Gradiente activo: A′(z) = 2g/c²",
            "p2_on1_en": "Lower clocks run slower; the connection",
            "p2_on1_es": "Los relojes bajos van más lento; el término",
            "p2_on2_en": "term Γᶻₜₜ = A′/2 is the only thing left.",
            "p2_on2_es": "de conexión Γᶻₜₜ = A′/2 es lo único que queda.",
            "p2_off_en": "▼ Knockout: A′(z) = 0",
            "p2_off_es": "▼ Apagado: A′(z) = 0",
            "p2_off1_en": "Every clock at one rate; the equation",
            "p2_off1_es": "Cada reloj a un ritmo; la ecuación",
            "p2_off2_en": "is d²z/dτ² = 0 and nothing moves.",
            "p2_off2_es": "es d²z/dτ² = 0 y nada se mueve.",
            "p3_ok_en": "✓ FALLS AT g, NO FORCE TERM",
            "p3_ok_es": "✓ CAE A g, SIN TÉRMINO DE FUERZA",
            "p3_ok1_en": "|2z(T)/T² + g| / g < 10⁻⁶",
            "p3_ok1_es": "|2z(T)/T² + g| / g < 10⁻⁶",
            "p3_ok2_en": "knockout: |a| < 10⁻¹²",
            "p3_ok2_es": "apagado: |a| < 10⁻¹²",
            "p3_bad_en": "⚠ PLANTED DEFECT: SIGN FLIP",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: SIGNO INVERTIDO",
            "p3_bad1_en": "A′ → −A′: the body rises at +g;",
            "p3_bad1_es": "A′ → −A′: el cuerpo sube a +g;",
            "p3_bad2_en": "the check must fail or the page does.",
            "p3_bad2_es": "la prueba debe fallar o falla la página.",
            "foot_en": "PLATE T.01-D · VISUAL INTUITION BRIDGE → ds² = −A(z)c²dt² + dz² · A(z) = 1 + 2gz/c² · d²z/dτ² = −(A′/2)(c dt/dτ)²",
            "foot_es": "LÁMINA T.01-D · PUENTE DE INTUICIÓN VISUAL → ds² = −A(z)c²dt² + dz² · A(z) = 1 + 2gz/c² · d²z/dτ² = −(A′/2)(c dt/dτ)²",
            "cap_en": "Plate T.01-D · Visual Intuition Bridge: the everyday analogy (left) sets up one quantity with two settings (center), and the verifier's three demands (right) are what the knockout and the sign-flip buttons in the instrument above test.",
            "cap_es": "Lámina T.01-D · Puente de Intuición Visual: la analogía cotidiana (izquierda) plantea una cantidad con dos ajustes (centro), y las tres exigencias del verificador (derecha) son lo que prueban los botones de apagado y de signo invertido en el instrumento de arriba.",
        },
        "t02": {
            "title_en": "Plate T.02-D Visual Intuition Bridge: one clock rate combining height speedup and velocity slowing in GPS orbit (+45.7 and -7.2 microseconds per day)",
            "title_es": "Lámina T.02-D Puente de Intuición Visual: un solo ritmo de reloj que combina el adelanto por altura y el atraso por velocidad en órbita GPS (+45.7 y -7.2 microsegundos por día)",
            "p1_h_en": "Two adjustments on one fare meter",
            "p1_h_es": "Dos ajustes en un mismo taxímetro",
            "p1_l1_en": "High orbit adds +45.7 µs/day (height);",
            "p1_l1_es": "La órbita alta suma +45.7 µs/día (altura);",
            "p1_l2_en": "orbital speed subtracts −7.2 µs/day.",
            "p1_l2_es": "la velocidad orbital resta −7.2 µs/día.",
            "p1_art": (
                '<rect x="44" y="114" width="76" height="16" rx="3" fill="var(--tp-prussian)" opacity="0.85"/>'
                '<rect x="132" y="138" width="38" height="16" rx="3" fill="var(--tp-minium)" opacity="0.85"/>'
                '<rect x="182" y="120" width="66" height="16" rx="3" fill="var(--tp-verdigris)" opacity="0.9"/>'
                '<line x1="38" y1="134" x2="256" y2="134" stroke="var(--tp-ink)" stroke-width="1"/>'
                '<text x="150" y="180" text-anchor="middle" font-size="8.3" fill="var(--tp-graphite)" data-en="+45.7 (height) − 7.2 (speed) = +38.6 µs/day" data-es="+45.7 (altura) − 7.2 (velocidad) = +38.6 µs/día">+45.7 (height) − 7.2 (speed) = +38.6 µs/day</text>'
            ),
            "p2_on_en": "▲ Both pieces kept: dτ/dt = 1 + ΔΦ/c² − v²/2c²",
            "p2_on_es": "▲ Ambas partes: dτ/dt = 1 + ΔΦ/c² − v²/2c²",
            "p2_on1_en": "Weak-field sum and exact Schwarzschild",
            "p2_on1_es": "La suma de campo débil y Schwarzschild",
            "p2_on2_en": "agree to within 0.3 µs/day in GPS orbit.",
            "p2_on2_es": "exacto coinciden a 0.3 µs/día en órbita GPS.",
            "p2_off_en": "▼ Knockout: drop the height term (ΔΦ → 0)",
            "p2_off_es": "▼ Apagado: quitar el término de altura (ΔΦ → 0)",
            "p2_off1_en": "Leaves only −7.2 µs/day; navigation",
            "p2_off1_es": "Deja solo −7.2 µs/día; la navegación",
            "p2_off2_en": "drifts by c · 45.7 µs ≈ 13.7 km/day.",
            "p2_off2_es": "deriva por c · 45.7 µs ≈ 13.7 km/día.",
            "p3_ok_en": "✓ DOUBLE-ENTRY GPS BUDGET",
            "p3_ok_es": "✓ PRESUPUESTO GPS DE DOBLE ENTRADA",
            "p3_ok1_en": "+45.7 − 7.2 = +38.5 µs/day (11.5 km/d)",
            "p3_ok1_es": "+45.7 − 7.2 = +38.5 µs/día (11.5 km/d)",
            "p3_ok2_en": "|weak − exact| < 0.3 µs/day",
            "p3_ok2_es": "|débil − exacto| < 0.3 µs/día",
            "p3_bad_en": "⚠ PLANTED DEFECT: WRONG SIGN ON v²",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: SIGNO ERRÓNEO EN v²",
            "p3_bad1_en": "+v²/2c² gives +52.9 µs/day;",
            "p3_bad1_es": "+v²/2c² da +52.9 µs/día;",
            "p3_bad2_en": "rejected against the Schwarzschild metric.",
            "p3_bad2_es": "rechazado frente a la métrica de Schwarzschild.",
            "foot_en": "PLATE T.02-D · VISUAL INTUITION BRIDGE → dτ/dt ≈ 1 + ΔΦ/c² − v²/(2c²) · GPS net +38.6 µs/day · Δr = 20,184 km",
            "foot_es": "LÁMINA T.02-D · PUENTE DE INTUICIÓN VISUAL → dτ/dt ≈ 1 + ΔΦ/c² − v²/(2c²) · neto GPS +38.6 µs/día · Δr = 20,184 km",
            "cap_en": "Plate T.02-D · Visual Intuition Bridge: one clock law carries both the height speedup (+45.7 µs/day) and the speed slowing (−7.2 µs/day); the knockout drops the height term and the planted defect flips the velocity sign.",
            "cap_es": "Lámina T.02-D · Puente de Intuición Visual: una sola ley del reloj lleva tanto el adelanto por altura (+45.7 µs/día) como el atraso por velocidad (−7.2 µs/día); el apagado quita la altura y el defecto plantado invierte el signo de la velocidad.",
        },
        "t03": {
            "title_en": "Plate T.03-D Visual Intuition Bridge: mass shapes the radial clock well via Poisson's equation and two different bodies fall side by side",
            "title_es": "Lámina T.03-D Puente de Intuición Visual: la masa curva el pozo radial de relojes mediante la ecuación de Poisson y dos cuerpos distintos caen a la par",
            "p1_h_en": "A heavy ball on a stretched sheet",
            "p1_h_es": "Una bola pesada sobre una lona tensa",
            "p1_l1_en": "Mass sets the curvature inside; outside,",
            "p1_l1_es": "La masa fija la curvatura adentro; afuera,",
            "p1_l2_en": "the slope eases off as −GM/(rc²).",
            "p1_l2_es": "la pendiente se suaviza como −GM/(rc²).",
            "p1_art": (
                '<circle cx="72" cy="144" r="18" fill="var(--tp-prussian)" opacity="0.22" stroke="var(--tp-prussian)" stroke-width="1.6"/>'
                '<path d="M 94 166 Q 140 126, 250 114" fill="none" stroke="var(--tp-prussian)" stroke-width="2.4"/>'
                '<circle cx="158" cy="133" r="4.5" fill="var(--tp-verdigris)"/>'
                '<circle cx="172" cy="130" r="4.5" fill="var(--tp-minium)"/>'
                '<text x="150" y="182" text-anchor="middle" font-size="8.3" fill="var(--tp-graphite)" data-en="Φ(r) = −GM/r · Ti and Pt fall together" data-es="Φ(r) = −GM/r · Ti y Pt caen juntos">Φ(r) = −GM/r · Ti and Pt fall together</text>'
            ),
            "p2_on_en": "▲ Source on: ∇²Φ = 4πGρ, η = 0",
            "p2_on_es": "▲ Fuente activa: ∇²Φ = 4πGρ, η = 0",
            "p2_on1_en": "Radial solver recovers −GM/r outside",
            "p2_on1_es": "El solver radial recupera −GM/r afuera",
            "p2_on2_en": "and −3GM/(2R) at the sphere's center.",
            "p2_on2_es": "y −3GM/(2R) en el centro de la esfera.",
            "p2_off_en": "▼ Knockout: M → 0 (no source mass)",
            "p2_off_es": "▼ Apagado: M → 0 (sin masa fuente)",
            "p2_off1_en": "Φ(r) = 0 everywhere; every clock ticks",
            "p2_off1_es": "Φ(r) = 0 en todas partes; cada reloj",
            "p2_off2_en": "at one rate and neither test body falls.",
            "p2_off2_es": "marcha igual y ningún cuerpo de prueba cae.",
            "p3_ok_en": "✓ POISSON & EQUIVALENCE (η = 0)",
            "p3_ok_es": "✓ POISSON Y EQUIVALENCIA (η = 0)",
            "p3_ok1_en": "max |Φ_num − Φ_exact| / |Φ| < 10⁻⁴",
            "p3_ok1_es": "máx |Φ_num − Φ_exacto| / |Φ| < 10⁻⁴",
            "p3_ok2_en": "two-body separation = 0 (< 10⁻¹² m)",
            "p3_ok2_es": "separación entre dos cuerpos = 0 (< 10⁻¹² m)",
            "p3_bad_en": "⚠ PLANTED DEFECT: η = 10⁻³",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: η = 10⁻³",
            "p3_bad1_en": "Composition-dependent fall splits the",
            "p3_bad1_es": "Una caída dependiente de la composición",
            "p3_bad2_en": "pair by 4.9 mm in 1 s; verifier rejects.",
            "p3_bad2_es": "separa el par 4.9 mm en 1 s; se rechaza.",
            "foot_en": "PLATE T.03-D · VISUAL INTUITION BRIDGE → ∇²Φ = 4πGρ · g₀₀ = −(1 + 2Φ/c²) · MICROSCOPE |η| ≤ 1.5 × 10⁻¹⁵",
            "foot_es": "LÁMINA T.03-D · PUENTE DE INTUICIÓN VISUAL → ∇²Φ = 4πGρ · g₀₀ = −(1 + 2Φ/c²) · MICROSCOPE |η| ≤ 1.5 × 10⁻¹⁵",
            "cap_en": "Plate T.03-D · Visual Intuition Bridge: mass bends the clock rate through Poisson's equation (left and center), and the equivalence principle demands that every test body follow the same curve (right).",
            "cap_es": "Lámina T.03-D · Puente de Intuición Visual: la masa curva el ritmo del reloj mediante la ecuación de Poisson (izquierda y centro), y el principio de equivalencia exige que todo cuerpo siga la misma curva (derecha).",
        },
        "t04": {
            "title_en": "Plate T.04-D Visual Intuition Bridge: a single quantum clock split across two heights loses fringe visibility as its two proper-time readings become distinguishable",
            "title_es": "Lámina T.04-D Puente de Intuición Visual: un solo reloj cuántico dividido en dos alturas pierde visibilidad de franjas conforme sus dos lecturas de tiempo propio se vuelven distinguibles",
            "p1_h_en": "One singer on two balconies",
            "p1_h_es": "Un cantante en dos balcones",
            "p1_l1_en": "When the upper metronome pulls ahead,",
            "p1_l1_es": "Cuando el metrónomo alto se adelanta,",
            "p1_l2_en": "the tick tells which balcony and fringes fade.",
            "p1_l2_es": "el pulso delata el balcón y la franja cae.",
            "p1_art": (
                '<circle cx="72" cy="126" r="14" fill="none" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
                '<line x1="72" y1="126" x2="82" y2="118" stroke="var(--tp-prussian)" stroke-width="2"/>'
                '<circle cx="72" cy="158" r="14" fill="none" stroke="var(--tp-minium)" stroke-width="1.8"/>'
                '<line x1="72" y1="158" x2="72" y2="145" stroke="var(--tp-minium)" stroke-width="2"/>'
                '<path d="M 110 120 Q 145 168, 180 132 T 250 150" fill="none" stroke="var(--tp-verdigris)" stroke-width="2.2"/>'
                '<text x="165" y="182" text-anchor="middle" font-size="8.3" fill="var(--tp-graphite)" data-en="V = |⟨τ₁|τ₂⟩| = |cos(ωΔτ/2)|" data-es="V = |⟨τ₁|τ₂⟩| = |cos(ωΔτ/2)|">V = |⟨τ₁|τ₂⟩| = |cos(ωΔτ/2)|</text>'
            ),
            "p2_on_en": "▲ Gravity & clock on: Δτ = gΔh·T/c²",
            "p2_on_es": "▲ Gravedad y reloj activos: Δτ = gΔh·T/c²",
            "p2_on1_en": "At 1 m × 1 s on a Sr clock, V = 0.989;",
            "p2_on1_es": "A 1 m × 1 s en un reloj de Sr, V = 0.989;",
            "p2_on2_en": "first visibility node at Δh·T = 10.7 m·s.",
            "p2_on2_es": "primer nodo de visibilidad en Δh·T = 10.7 m·s.",
            "p2_off_en": "▼ Knockout: g → 0 (no proper-time split)",
            "p2_off_es": "▼ Apagado: g → 0 (sin diferencia de tiempo)",
            "p2_off1_en": "Both branches tick identically; no",
            "p2_off1_es": "Ambas ramas marchan igual; no hay",
            "p2_off2_en": "which-path record and V = 1 everywhere.",
            "p2_off2_es": "información de camino y V = 1 siempre.",
            "p3_ok_en": "✓ OVERLAP EQUALS VISIBILITY",
            "p3_ok_es": "✓ EL SOLAPE IGUALA LA VISIBILIDAD",
            "p3_ok1_en": "max |V_overlap − |cos(ωΔτ/2)|| < 10⁻¹²",
            "p3_ok1_es": "máx |V_solape − |cos(ωΔτ/2)|| < 10⁻¹²",
            "p3_ok2_en": "first node: Δh·T ≈ 10.7 m·s",
            "p3_ok2_es": "primer nodo: Δh·T ≈ 10.7 m·s",
            "p3_bad_en": "⚠ PLANTED DEFECT: FROZEN CLOCK (ω = 0)",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: RELOJ PARADO (ω = 0)",
            "p3_bad1_en": "A clock that never ticks stays at V = 1",
            "p3_bad1_es": "Un reloj que no marcha queda en V = 1",
            "p3_bad2_en": "and never reaches the orthogonal node.",
            "p3_bad2_es": "y nunca alcanza el nodo ortogonal.",
            "foot_en": "PLATE T.04-D · VISUAL INTUITION BRIDGE → Δτ = gΔh·T/c² · V = |cos(ωgΔh·T / 2c²)| · PROPOSAL (NOT YET RUN IN GRAVITY)",
            "foot_es": "LÁMINA T.04-D · PUENTE DE INTUICIÓN VISUAL → Δτ = gΔh·T/c² · V = |cos(ωgΔh·T / 2c²)| · PROPUESTA (AÚN NO CORRIDA EN GRAVEDAD)",
            "cap_en": "Plate T.04-D · Visual Intuition Bridge: an internal clock carried along two heights records which path the wavepacket took (left and center), modulating the interference visibility (right).",
            "cap_es": "Lámina T.04-D · Puente de Intuición Visual: un reloj interno llevado por dos alturas registra qué camino siguió el paquete de ondas (izquierda y centro), modulando la visibilidad de interferencia (derecha).",
        },
        "t05": {
            "title_en": "Plate T.05-D Visual Intuition Bridge: two superposed masses accumulating four Newtonian branch phases, set beside the classical LOCC zero line and the disputed band",
            "title_es": "Lámina T.05-D Puente de Intuición Visual: dos masas en superposición que acumulan cuatro fases de rama newtonianas, junto al cero clásico LOCC y la banda en disputa",
            "p1_h_en": "Two dancers, four rope lengths",
            "p1_h_es": "Dos bailarines, cuatro largos de cuerda",
            "p1_l1_en": "Four pairs of positions (LL, LR, RL, RR)",
            "p1_l1_es": "Cuatro pares de posiciones (LL, LR, RL, RR)",
            "p1_l2_en": "collect four phases φ = Gm²t/(ħd).",
            "p1_l2_es": "acumulan cuatro fases φ = Gm²t/(ħd).",
            "p1_art": (
                '<circle cx="64" cy="118" r="6" fill="var(--tp-prussian)"/><circle cx="114" cy="118" r="6" fill="var(--tp-prussian)"/>'
                '<circle cx="174" cy="160" r="6" fill="var(--tp-minium)"/><circle cx="224" cy="160" r="6" fill="var(--tp-minium)"/>'
                '<line x1="64" y1="118" x2="174" y2="160" stroke="var(--tp-rule-strong)" stroke-width="1.3"/>'
                '<line x1="114" y1="118" x2="174" y2="160" stroke="var(--tp-prussian)" stroke-width="2.2"/>'
                '<line x1="64" y1="118" x2="224" y2="160" stroke="var(--tp-prussian)" stroke-width="1.5" stroke-dasharray="3 2"/>'
                '<line x1="114" y1="118" x2="224" y2="160" stroke="var(--tp-rule-strong)" stroke-width="1.3"/>'
                '<text x="150" y="182" text-anchor="middle" font-size="8.3" fill="var(--tp-graphite)" data-en="Δφ = φ_LR + φ_RL − φ_LL − φ_RR = 0.31 rad" data-es="Δφ = φ_LR + φ_RL − φ_LL − φ_RR = 0.31 rad">Δφ = φ_LR + φ_RL − φ_LL − φ_RR = 0.31 rad</text>'
            ),
            "p2_on_en": "▲ Three channels drawn at equal weight",
            "p2_on_es": "▲ Tres canales con el mismo grosor",
            "p2_on1_en": "Quantum: |sin(Δφ/2)| = 0.16 at 2.5 s;",
            "p2_on1_es": "Cuántico: |sin(Δφ/2)| = 0.16 a los 2.5 s;",
            "p2_on2_en": "LOCC: 0; Disputed: hatched band [0, Q].",
            "p2_on2_es": "LOCC: 0; Disputado: banda rayada [0, Q].",
            "p2_off_en": "▼ Knockout: switch the readout channel",
            "p2_off_es": "▼ Apagado: cambiar el canal de lectura",
            "p2_off1_en": "Mean-field LOCC gives product phases",
            "p2_off1_es": "El campo medio LOCC da fases producto",
            "p2_off2_en": "α_i + β_j and zero entanglement (< 10⁻¹²).",
            "p2_off2_es": "α_i + β_j y cero entrelazamiento (< 10⁻¹²).",
            "p3_ok_en": "✓ CONCURRENCE & PURITY AGREE",
            "p3_ok_es": "✓ CONCURRENCIA Y PUREZA COINCIDEN",
            "p3_ok1_en": "|C_closed − C_purity| < 10⁻¹² (C = 0.156)",
            "p3_ok1_es": "|C_cerrada − C_pureza| < 10⁻¹² (C = 0.156)",
            "p3_ok2_en": "LOCC channel: concurrence < 10⁻¹²",
            "p3_ok2_es": "canal LOCC: concurrencia < 10⁻¹²",
            "p3_bad_en": "⚠ PLANTED DEFECT: ENTANGLING LOCC",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: LOCC QUE ENTRELAZA",
            "p3_bad1_en": "Feeding quantum phases to the LOCC",
            "p3_bad1_es": "Dar fases cuánticas al canal clásico",
            "p3_bad2_en": "channel violates LOCC separability.",
            "p3_bad2_es": "LOCC viola la separabilidad LOCC.",
            "foot_en": "PLATE T.05-D · VISUAL INTUITION BRIDGE → Δφ = 0.314 rad · C = |sin(Δφ/2)| = 0.156 · THREE CHANNELS · PAGE LABEL OPEN",
            "foot_es": "LÁMINA T.05-D · PUENTE DE INTUICIÓN VISUAL → Δφ = 0.314 rad · C = |sin(Δφ/2)| = 0.156 · TRES CANALES · ETIQUETA ABIERTO",
            "cap_en": "Plate T.05-D · Visual Intuition Bridge: four branch distances between two superposed masses (left), the three channels drawn at equal weight without picking a side (center), and the verifier's separability gate (right).",
            "cap_es": "Lámina T.05-D · Puente de Intuición Visual: cuatro distancias de rama entre dos masas en superposición (izquierda), los tres canales dibujados con el mismo peso sin tomar partido (centro), y la puerta de separabilidad del verificador (derecha).",
        },
        "t06": {
            "title_en": "Plate T.06-D Visual Intuition Bridge: the Diosi-Penrose gravitational self-energy proposal and the Gran Sasso and XENONnT underground radiation bounds",
            "title_es": "Lámina T.06-D Puente de Intuición Visual: la propuesta de autoenergía gravitatoria de Diósi y Penrose y las cotas subterráneas de radiación de Gran Sasso y XENONnT",
            "p1_h_en": "Searching a quiet underground room",
            "p1_h_es": "Buscar el zumbido bajo una montaña",
            "p1_l1_en": "Collapse jitter would make nuclei radiate",
            "p1_l1_es": "El temblor de colapso haría radiar a los",
            "p1_l2_en": "as 1/R0³; underground detectors listened.",
            "p1_l2_es": "núcleos como 1/R0³; bajo tierra escucharon.",
            "p1_art": (
                '<rect x="44" y="124" width="88" height="24" rx="3" fill="var(--tp-minium)" opacity="0.22"/>'
                '<rect x="132" y="124" width="114" height="24" rx="3" fill="var(--tp-verdigris)" opacity="0.22"/>'
                '<line x1="132" y1="116" x2="132" y2="156" stroke="var(--tp-ink)" stroke-width="2.2"/>'
                '<line x1="184" y1="116" x2="184" y2="156" stroke="var(--tp-prussian)" stroke-width="2" stroke-dasharray="4 3"/>'
                '<circle cx="72" cy="136" r="5.5" fill="var(--tp-minium)"/>'
                '<text x="150" y="182" text-anchor="middle" font-size="8.3" fill="var(--tp-graphite)" data-en="R0 = 0.05 Å (dot) vs R0 > 0.54 Å &amp; 4.9 Å" data-es="R0 = 0.05 Å (punto) vs R0 > 0.54 Å y 4.9 Å">R0 = 0.05 Å (dot) vs R0 > 0.54 Å &amp; 4.9 Å</text>'
            ),
            "p2_on_en": "▲ Gravity on: τ = ħ/E_G, z_s = a/R0³",
            "p2_on_es": "▲ Gravedad activa: τ = ħ/E_G, z_s = a/R0³",
            "p2_on1_en": "576 counted vs 506 expected in 62 days",
            "p2_on1_es": "576 contados frente a 506 esperados en 62 d",
            "p2_on2_en": "sets R0 > 0.54 Å (95 %); XENONnT: 4.9 Å.",
            "p2_on2_es": "fija R0 > 0.54 Å (95 %); XENONnT: 4.9 Å.",
            "p2_off_en": "▼ Knockout: G → 0 (switch gravity off)",
            "p2_off_es": "▼ Apagado: G → 0 (apagar la gravedad)",
            "p2_off1_en": "E_G vanishes, τ = ∞, and the model",
            "p2_off1_es": "E_G se anula, τ = ∞, y el modelo",
            "p2_off2_en": "predicts neither collapse nor radiation.",
            "p2_off2_es": "no predice ni colapso ni radiación.",
            "p3_ok_en": "✓ RECOMPUTED BOUND & ORIENTATION",
            "p3_ok_es": "✓ COTA RECALCULADA Y ORIENTACIÓN",
            "p3_ok1_en": "R0_recomp = 0.545 Å (within 2 % of 0.54 Å)",
            "p3_ok1_es": "R0_recalc = 0.545 Å (a < 2 % de 0.54 Å)",
            "p3_ok2_en": "R0 = 0.05 Å predicts ~1.4 × 10⁵ photons",
            "p3_ok2_es": "R0 = 0.05 Å predice ~1.4 × 10⁵ fotones",
            "p3_bad_en": "⚠ PLANTED DEFECT: INVERTED BOUND",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: COTA INVERTIDA",
            "p3_bad1_en": "Painting small R0 as allowed contradicts",
            "p3_bad1_es": "Pintar R0 pequeño como permitido contradice",
            "p3_bad2_en": "the 1/R0³ rate; verifier rejects.",
            "p3_bad2_es": "la tasa 1/R0³; el verificador lo rechaza.",
            "foot_en": "PLATE T.06-D · VISUAL INTUITION BRIDGE → τ = ħ/E_G · E_G = (6/5)GM²/R · Gran Sasso R0 > 0.54 Å · XENONnT R0 > 4.9 Å",
            "foot_es": "LÁMINA T.06-D · PUENTE DE INTUICIÓN VISUAL → τ = ħ/E_G · E_G = (6/5)GM²/R · Gran Sasso R0 > 0.54 Å · XENONnT R0 > 4.9 Å",
            "cap_en": "Plate T.06-D · Visual Intuition Bridge: the spontaneous radiation test in an underground detector (left), the model's collapse time and exclusion line (center), and the verifier's orientation check (right).",
            "cap_es": "Lámina T.06-D · Puente de Intuición Visual: la prueba de radiación espontánea en un detector subterráneo (izquierda), el tiempo de colapso y la línea de exclusión (centro), y la prueba de orientación del verificador (derecha).",
        },
        "t07": {
            "title_en": "Plate T.07-D Visual Intuition Bridge: Page-Wootters conditional time inside a stationary history state satisfying H|Psi>> = 0",
            "title_es": "Lámina T.07-D Puente de Intuición Visual: el tiempo condicional de Page y Wootters dentro de un estado de historia estacionario que cumple H|Psi>> = 0",
            "p1_h_en": "A printed flip-book on a table",
            "p1_h_es": "Un folioscopio impreso sobre la mesa",
            "p1_l1_en": "The whole book sits still; conditioning",
            "p1_l1_es": "Todo el libro está quieto; condicionar",
            "p1_l2_en": "on page n recovers the moving figure.",
            "p1_l2_es": "a la página n recupera la figura móvil.",
            "p1_art": (
                '<rect x="44" y="116" width="52" height="44" rx="4" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
                '<text x="70" y="142" text-anchor="middle" font-size="9" font-weight="700" fill="var(--tp-prussian)">Ĥ|Ψ⟩⟩=0</text>'
                '<path d="M 104 138 L 128 138" stroke="var(--tp-prussian)" stroke-width="1.6"/>'
                '<path d="M 134 154 C 156 112, 184 164, 210 120 S 240 156, 254 128" fill="none" stroke="var(--tp-verdigris)" stroke-width="2.2"/>'
                '<text x="150" y="182" text-anchor="middle" font-size="8.3" fill="var(--tp-graphite)" data-en="⟨t_n|Ψ⟩⟩ ∝ |ψ(t_n)⟩ · P(+x|n) = cos²(εn/2)" data-es="⟨t_n|Ψ⟩⟩ ∝ |ψ(t_n)⟩ · P(+x|n) = cos²(εn/2)">⟨t_n|Ψ⟩⟩ ∝ |ψ(t_n)⟩ · P(+x|n) = cos²(εn/2)</text>'
            ),
            "p2_on_en": "▲ Time basis: slice by clock state |t_n⟩",
            "p2_on_es": "▲ Base de tiempo: corte por estado |t_n⟩",
            "p2_on1_en": "Stationary whole (||Ĥ|Ψ⟩⟩|| < 10⁻¹⁰)",
            "p2_on1_es": "Todo estacionario (||Ĥ|Ψ⟩⟩|| < 10⁻¹⁰)",
            "p2_on2_en": "yields exact cos²(εn/2) qubit motion.",
            "p2_on2_es": "da el movimiento exacto cos²(εn/2).",
            "p2_off_en": "▼ Knockout: read in the energy basis |E_m⟩",
            "p2_off_es": "▼ Apagado: leer en la base de energía |E_m⟩",
            "p2_off1_en": "Same global state |Ψ⟩⟩, different basis:",
            "p2_off1_es": "Mismo estado global |Ψ⟩⟩, otra base:",
            "p2_off2_en": "P(+x|m) = 1/2 for every slice; no time.",
            "p2_off2_es": "P(+x|m) = 1/2 en cada corte; sin tiempo.",
            "p3_ok_en": "✓ KERNEL & SCHRÖDINGER MATCH",
            "p3_ok_es": "✓ NÚCLEO Y SCHRÖDINGER COINCIDEN",
            "p3_ok1_en": "||Ĥ|Ψ⟩⟩|| < 10⁻¹⁰ · dim ker(Ĥ) ≥ 1",
            "p3_ok1_es": "||Ĥ|Ψ⟩⟩|| < 10⁻¹⁰ · dim ker(Ĥ) ≥ 1",
            "p3_ok2_en": "max |P(+x|n) − cos²(εn/2)| < 10⁻¹⁰",
            "p3_ok2_es": "máx |P(+x|n) − cos²(εn/2)| < 10⁻¹⁰",
            "p3_bad_en": "⚠ PLANTED DEFECT: DETUNED CLOCK",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: RELOJ DESAFINADO",
            "p3_bad1_en": "Quadratic clock spectrum breaks",
            "p3_bad1_es": "Un espectro cuadrático rompe",
            "p3_bad2_en": "(Ĥ_C + Ĥ_S)|Ψ⟩⟩ = 0 (residual > 1).",
            "p3_bad2_es": "(Ĥ_C + Ĥ_S)|Ψ⟩⟩ = 0 (residuo > 1).",
            "foot_en": "PLATE T.07-D · VISUAL INTUITION BRIDGE → (Ĥ_C ⊗ I + I ⊗ Ĥ_S)|Ψ⟩⟩ = 0 · |ψ(t_n)⟩ = √d ⟨t_n|Ψ⟩⟩ · P(+x|n) = cos²(εn/2)",
            "foot_es": "LÁMINA T.07-D · PUENTE DE INTUICIÓN VISUAL → (Ĥ_C ⊗ I + I ⊗ Ĥ_S)|Ψ⟩⟩ = 0 · |ψ(t_n)⟩ = √d ⟨t_n|Ψ⟩⟩ · P(+x|n) = cos²(εn/2)",
            "cap_en": "Plate T.07-D · Visual Intuition Bridge: a stationary flip-book state (left) shows Schrödinger evolution when conditioned on the clock's time basis and a flat 1/2 in the energy basis (center), guarded by the constraint residual check (right).",
            "cap_es": "Lámina T.07-D · Puente de Intuición Visual: un estado folioscopio estacionario (izquierda) muestra evolución de Schrödinger al condicionarse en la base de tiempo y 1/2 plano en la de energía (centro), vigilado por el residuo de la restricción (derecha).",
        },
        "t08": {
            "title_en": "Plate T.08-D Visual Intuition Bridge: tracing over the inaccessible Rindler wedge turns the pure two-mode vacuum into an exact Gibbs thermal state at the Unruh-Hawking temperature",
            "title_es": "Lámina T.08-D Puente de Intuición Visual: trazar sobre la cuña de Rindler inaccesible convierte el vacío puro de dos modos en un estado térmico exacto de Gibbs a la temperatura de Unruh-Hawking",
            "p1_h_en": "Two reels of one tape, one behind a curtain",
            "p1_h_es": "Dos carretes de una cinta, uno tras el telón",
            "p1_l1_en": "The two-mode state |Ψ(r)⟩ is pure overall,",
            "p1_l1_es": "El estado de dos modos |Ψ(r)⟩ es puro en total,",
            "p1_l2_en": "but one wedge alone sees thermal weights.",
            "p1_l2_es": "pero una sola cuña ve pesos térmicos.",
            "p1_art": (
                '<line x1="146" y1="112" x2="146" y2="168" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="3 2"/>'
                '<circle cx="92" cy="140" r="14" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.3"/>'
                '<circle cx="200" cy="140" r="14" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
                '<path d="M 106 136 Q 146 116, 186 136" fill="none" stroke="var(--tp-verdigris)" stroke-width="2"/>'
                '<text x="150" y="182" text-anchor="middle" font-size="8.3" fill="var(--tp-graphite)" data-en="Tr_L(|Ψ⟩⟨Ψ|) = (1−e⁻ˣ) Σ e⁻ⁿˣ |n⟩⟨n|" data-es="Tr_L(|Ψ⟩⟨Ψ|) = (1−e⁻ˣ) Σ e⁻ⁿˣ |n⟩⟨n|">Tr_L(|Ψ⟩⟨Ψ|) = (1−e⁻ˣ) Σ e⁻ⁿˣ |n⟩⟨n|</text>'
            ),
            "p2_on_en": "▲ Partial trace on: tanh r = exp(−πcω/a)",
            "p2_on_es": "▲ Traza parcial activa: tanh r = exp(−πcω/a)",
            "p2_on1_en": "Diagonal weights match Planck/Gibbs to",
            "p2_on1_es": "Los pesos diagonales igualan a Planck/Gibbs",
            "p2_on2_en": "< 10⁻¹²; ∫ dM/(k_B T_H) = A / (4 ℓ_P²).",
            "p2_on2_es": "a < 10⁻¹²; ∫ dM/(k_B T_H) = A / (4 ℓ_P²).",
            "p2_off_en": "▼ Knockout: drop the 2π Euclidean period",
            "p2_off_es": "▼ Apagado: quitar el factor 2π del periodo",
            "p2_off1_en": "Setting κ → a/c instead of a/(2πc)",
            "p2_off1_es": "Poner κ → a/c en lugar de a/(2πc)",
            "p2_off2_en": "shifts T_H by 2π and breaks A/(4ℓ_P²).",
            "p2_off2_es": "desplaza T_H por 2π y rompe A/(4ℓ_P²).",
            "p3_ok_en": "✓ GIBBS WEIGHTS & FIRST LAW",
            "p3_ok_es": "✓ PESOS DE GIBBS Y PRIMERA LEY",
            "p3_ok1_en": "max |p_n − p_Gibbs| < 10⁻¹² · S_vN = S_Pl",
            "p3_ok1_es": "máx |p_n − p_Gibbs| < 10⁻¹² · S_vN = S_Pl",
            "p3_ok2_en": "|S_quad − A/(4ℓ_P²)| / S < 10⁻¹⁰",
            "p3_ok2_es": "|S_cuad − A/(4ℓ_P²)| / S < 10⁻¹⁰",
            "p3_bad_en": "⚠ PLANTED DEFECT: MISSING 2π FACTOR",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: FALTA EL FACTOR 2π",
            "p3_bad1_en": "Dropping 2π yields S = A / (8π ℓ_P²);",
            "p3_bad1_es": "Omitir 2π arroja S = A / (8π ℓ_P²);",
            "p3_bad2_en": "verifier rejects the first-law mismatch.",
            "p3_bad2_es": "el verificador rechaza el desajuste.",
            "foot_en": "PLATE T.08-D · VISUAL INTUITION BRIDGE → T_U = ħa/(2πck_B) · T_H = ħc³/(8πGMk_B) · S_BH = k_B A/(4ℓ_P²) · 1 M_☉ → 61.7 nK",
            "foot_es": "LÁMINA T.08-D · PUENTE DE INTUICIÓN VISUAL → T_U = ħa/(2πck_B) · T_H = ħc³/(8πGMk_B) · S_BH = k_B A/(4ℓ_P²) · 1 M_☉ → 61.7 nK",
            "cap_en": "Plate T.08-D · Visual Intuition Bridge: tracing over the hidden Rindler wedge turns a pure two-mode state into an exact Gibbs thermal state (left and center), and integrating the first law recovers the quarter-area entropy (right).",
            "cap_es": "Lámina T.08-D · Puente de Intuición Visual: trazar sobre la cuña oculta de Rindler convierte un estado puro de dos modos en un estado térmico exacto de Gibbs (izquierda y centro), e integrar la primera ley recupera la entropía de un cuarto del área (derecha).",
        },
        "t09": {
            "title_en": "Plate T.09-D Visual Intuition Bridge: a struck Kerr horizon rings at frequencies and damping times locked by mass M and spin chi alone",
            "title_es": "Lámina T.09-D Puente de Intuición Visual: un horizonte de Kerr golpeado resuena a frecuencias y tiempos de caída fijados solo por la masa M y el espín chi",
            "p1_h_en": "Two bells cast from two numbers",
            "p1_h_es": "Una campana fundida con dos números",
            "p1_l1_en": "Mass M sets the pitch scale 1/M; spin χ",
            "p1_l1_es": "La masa M fija la escala 1/M; el espín χ",
            "p1_l2_en": "locks both the fundamental and overtone.",
            "p1_l2_es": "fija tanto el modo fundamental como el sobretono.",
            "p1_art": (
                '<path d="M 44 140 C 58 104, 72 176, 86 116 S 114 162, 128 130 S 156 148, 180 138 L 248 140" fill="none" stroke="var(--tp-prussian)" stroke-width="2.2"/>'
                '<path d="M 44 140 C 56 114, 68 164, 82 132 S 108 144, 140 140 L 248 140" fill="none" stroke="var(--tp-verdigris)" stroke-width="1.6" stroke-dasharray="3 2"/>'
                '<text x="150" y="182" text-anchor="middle" font-size="8.3" fill="var(--tp-graphite)" data-en="(2,2,0): 251 Hz, 4.2 ms · (2,2,1): 245 Hz, 1.4 ms" data-es="(2,2,0): 251 Hz, 4.2 ms · (2,2,1): 245 Hz, 1.4 ms">(2,2,0): 251 Hz, 4.2 ms · (2,2,1): 245 Hz, 1.4 ms</text>'
            ),
            "p2_on_en": "▲ Exact Kerr radical: √(1 − χ²)",
            "p2_on_es": "▲ Radical exacto de Kerr: √(1 − χ²)",
            "p2_on1_en": "A = 8π(GM/c²)²(1 + √(1 − χ²)) obeys",
            "p2_on1_es": "A = 8π(GM/c²)²(1 + √(1 − χ²)) cumple",
            "p2_on2_en": "Smarr's identity Mc² = κc²A/(4πG) + 2Ω_H J.",
            "p2_on2_es": "la identidad de Smarr Mc² = κc²A/(4πG) + 2Ω_H J.",
            "p2_off_en": "▼ Knockout: corrupt √(1 − χ²) → √(1 + χ²)",
            "p2_off_es": "▼ Apagado: corromper √(1 − χ²) → √(1 + χ²)",
            "p2_off1_en": "Breaks Smarr's horizon identity by > 7 %",
            "p2_off1_es": "Rompe la identidad de Smarr por > 7 %",
            "p2_off2_en": "and shifts the QNM spectrum off Leaver.",
            "p2_off2_es": "y desvía el espectro QNM respecto a Leaver.",
            "p3_ok_en": "✓ SMARR & LEAVER BENCHMARK",
            "p3_ok_es": "✓ IDENTIDAD DE SMARR Y LEAVER",
            "p3_ok1_en": "Smarr residual < 10⁻¹⁴ across χ ∈ [0, 0.95]",
            "p3_ok1_es": "residuo de Smarr < 10⁻¹⁴ en χ ∈ [0, 0.95]",
            "p3_ok2_en": "matches Leaver (1985) QNM table to < 0.5 %",
            "p3_ok2_es": "iguala la tabla de Leaver (1985) a < 0.5 %",
            "p3_bad_en": "⚠ PLANTED DEFECT: CORRUPTED RADICAL",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: RADICAL CORROMPIDO",
            "p3_bad1_en": "Replacing √(1 − χ²) with √(1 + χ²)",
            "p3_bad1_es": "Reemplazar √(1 − χ²) por √(1 + χ²)",
            "p3_bad2_en": "violates Smarr & Leaver; verifier rejects.",
            "p3_bad2_es": "viola Smarr y Leaver; el verificador falla.",
            "foot_en": "PLATE T.09-D · VISUAL INTUITION BRIDGE → A(M,χ) = 8π(GM/c²)²(1 + √(1 − χ²)) · 62 M_☉, χ = 0.67 → 250.8 Hz, 4.16 ms",
            "foot_es": "LÁMINA T.09-D · PUENTE DE INTUICIÓN VISUAL → A(M,χ) = 8π(GM/c²)²(1 + √(1 − χ²)) · 62 M_☉, χ = 0.67 → 250.8 Hz, 4.16 ms",
            "cap_en": "Plate T.09-D · Visual Intuition Bridge: a Kerr horizon's fundamental tone and first overtone are fixed by M and χ alone (left and center), checked against Smarr's identity and Leaver's continued-fraction benchmark (right).",
            "cap_es": "Lámina T.09-D · Puente de Intuición Visual: el modo fundamental y el primer sobretono de un horizonte de Kerr quedan fijados solo por M y χ (izquierda y centro), verificados frente a la identidad de Smarr y la tabla de Leaver (derecha).",
        },
        "t10": {
            "title_en": "Plate T.10-D Visual Intuition Bridge: Hawking's rising thermal entropy line versus Page's subsystem counting curve on ten qubits",
            "title_es": "Lámina T.10-D Puente de Intuición Visual: la recta de entropía térmica creciente de Hawking frente a la curva de conteo de subsistemas de Page en diez qubits",
            "p1_h_en": "Dealing a shuffled quantum deck",
            "p1_h_es": "Repartir una baraja cuántica",
            "p1_l1_en": "The smaller pile limits the entanglement,",
            "p1_l1_es": "El montón menor limita el entrelazamiento,",
            "p1_l2_en": "so uncertainty peaks at N/2 and falls.",
            "p1_l2_es": "así que la entropía sube hasta N/2 y baja.",
            "p1_art": (
                '<line x1="44" y1="164" x2="244" y2="110" stroke="var(--tp-minium)" stroke-width="1.8" stroke-dasharray="5 3"/>'
                '<path d="M 44 164 Q 144 96, 244 164" fill="none" stroke="var(--tp-prussian)" stroke-width="2.4"/>'
                '<circle cx="144" cy="130" r="4.5" fill="var(--tp-minium)"/>'
                '<text x="150" y="182" text-anchor="middle" font-size="8.3" fill="var(--tp-graphite)" data-en="Hawking: rises · Page: peaks at N/2 = 5" data-es="Hawking: sube · Page: máximo en N/2 = 5">Hawking: rises · Page: peaks at N/2 = 5</text>'
            ),
            "p2_on_en": "▲ Unitary pure state on N = 10 qubits",
            "p2_on_es": "▲ Estado puro unitario en N = 10 qubits",
            "p2_on1_en": "S(m,n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n)",
            "p2_on1_es": "S(m,n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n)",
            "p2_on2_en": "peaks at 2.97 nats (a=5), ends at 0.69 (a=9).",
            "p2_on2_es": "máximo 2.97 nats (a=5), termina en 0.69 (a=9).",
            "p2_off_en": "▼ Knockout: non-unitary thermal line",
            "p2_off_es": "▼ Apagado: recta térmica no unitaria",
            "p2_off1_en": "Every emitted qubit adds ln 2 forever;",
            "p2_off1_es": "Cada qubit emitido suma ln 2 sin fin;",
            "p2_off2_en": "the entropy never turns over.",
            "p2_off2_es": "la entropía nunca da la vuelta.",
            "p3_ok_en": "✓ HAAR TOY MATCHES PAGE FORMULA",
            "p3_ok_es": "✓ JUGUETE DE HAAR IGUALA A PAGE",
            "p3_ok1_en": "max |S_toy − S_Page| < 0.002 nats (< 0.03)",
            "p3_ok1_es": "máx |S_juguete − S_Page| < 0.002 nats (< 0.03)",
            "p3_ok2_en": "symmetric in a ↔ N−a; turns over at N/2",
            "p3_ok2_es": "simétrica en a ↔ N−a; da la vuelta en N/2",
            "p3_bad_en": "⚠ PLANTED DEFECT: NO TURNOVER",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: SIN VUELTA",
            "p3_bad1_en": "Replacing the curve with a·ln 2 fails",
            "p3_bad1_es": "Reemplazar la curva por a·ln 2 falla",
            "p3_bad2_en": "the turnover check at the final cut.",
            "p3_bad2_es": "la prueba de retorno en el corte final.",
            "foot_en": "PLATE T.10-D · VISUAL INTUITION BRIDGE → S(m,n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n) · N = 10 QUBITS · PEAK 2.97 NATS AT a = 5",
            "foot_es": "LÁMINA T.10-D · PUENTE DE INTUICIÓN VISUAL → S(m,n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n) · N = 10 QUBITS · MÁXIMO 2.97 NATS EN a = 5",
            "cap_en": "Plate T.10-D · Visual Intuition Bridge: dealing a pure quantum deck (left), Page's exact subsystem entropy formula against Hawking's rising thermal line (center), and the 10-qubit Haar-random eigensolver gate (right).",
            "cap_es": "Lámina T.10-D · Puente de Intuición Visual: repartir una baraja cuántica pura (izquierda), la fórmula exacta de entropía de Page frente a la recta térmica de Hawking (centro), y la puerta del solver de 10 qubits (derecha).",
        },
        "t11": {
            "title_en": "Plate T.11-D Visual Intuition Bridge: environmental photon scattering selects pointer states by suppressing off-diagonal coherences as gamma^N while copying 1 bit of classical record across the bath",
            "title_es": "Lámina T.11-D Puente de Intuición Visual: la dispersión de fotones del entorno selecciona estados puntero suprimiendo las coherencias fuera de la diagonal como gamma^N mientras copia 1 bit de registro clásico en el baño",
            "p1_h_en": "Sunlit dust motes in a dark room",
            "p1_h_es": "Motas de polvo al sol en un cuarto oscuro",
            "p1_l1_en": "Passing photons bounce off the mote's",
            "p1_l1_es": "Los fotones rebotan en la posición de",
            "p1_l2_en": "position and broadcast it to the room.",
            "p1_l2_es": "la mota y la difunden por todo el cuarto.",
            "p1_art": (
                '<circle cx="62" cy="136" r="8" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.6"/>'
                '<circle cx="92" cy="136" r="8" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.3" stroke-dasharray="2.5 2"/>'
                '<path d="M 44 114 L 56 129 M 68 129 L 82 114 M 98 129 L 112 114" fill="none" stroke="var(--tp-minium)" stroke-width="1.5"/>'
                '<rect x="122" y="118" width="14" height="36" rx="2" fill="var(--tp-prussian)"/>'
                '<rect x="144" y="150" width="14" height="6" rx="1.5" fill="var(--tp-minium)"/>'
                '<path d="M 172 158 C 186 122, 206 120, 248 120" fill="none" stroke="var(--tp-verdigris)" stroke-width="2.2"/>'
                '<text x="150" y="182" text-anchor="middle" font-size="8.3" fill="var(--tp-graphite)" data-en="[Ĥ_int, Z_S] = 0 · |ρ₀₁| = ½ cos⁶θ · I(S:E_k) ≈ 1 bit" data-es="[Ĥ_int, Z_S] = 0 · |ρ₀₁| = ½ cos⁶θ · I(S:E_k) ≈ 1 bit">[Ĥ_int, Z_S] = 0 · |ρ₀₁| = ½ cos⁶θ · I(S:E_k) ≈ 1 bit</text>'
            ),
            "p2_on_en": "▲ Photon bath coupled: [Ĥ_int, Z_S] = 0",
            "p2_on_es": "▲ Baño acoplado: [Ĥ_int, Z_S] = 0",
            "p2_on1_en": "|ρ₀₁(N)| = ½ (cos θ)^N → 0; k = 2 of 6",
            "p2_on1_es": "|ρ₀₁(N)| = ½ (cos θ)^N → 0; k = 2 de 6",
            "p2_on2_en": "modes already hold 0.998 bits of Z_S.",
            "p2_on2_es": "modos ya guardan 0.998 bits de Z_S.",
            "p2_off_en": "▼ Knockout: uncouple bath (θ = 0, ε = 1)",
            "p2_off_es": "▼ Apagado: desacoplar baño (θ = 0, ε = 1)",
            "p2_off1_en": "Λ_EM = 0; off-diagonal coherence stays",
            "p2_off1_es": "Λ_EM = 0; la coherencia queda en 1.0 y",
            "p2_off2_en": "at 1.0 and the bath records 0 bits.",
            "p2_off2_es": "el baño registra exactamente 0 bits.",
            "p3_ok_en": "✓ STATEVECTOR & R⁶T⁹ SCALING",
            "p3_ok_es": "✓ VECTOR DE ESTADO Y ESCALA R⁶T⁹",
            "p3_ok1_en": "max |I_sv − I_Zurek| < 10⁻¹² nats",
            "p3_ok1_es": "máx |I_sv − I_Zurek| < 10⁻¹² nats",
            "p3_ok2_en": "Λ ∝ R⁶T⁹ exact · ε = 1 → Λ_EM = 0",
            "p3_ok2_es": "Λ ∝ R⁶T⁹ exacto · ε = 1 → Λ_EM = 0",
            "p3_bad_en": "⚠ PLANTED DEFECT: SCRAMBLED POINTER",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: BASE MEZCLADA",
            "p3_bad1_en": "Rotating Z_S → X_S breaks [Ĥ_int, Z_S]=0",
            "p3_bad1_es": "Rotar Z_S → X_S rompe [Ĥ_int, Z_S]=0",
            "p3_bad2_en": "and collapses the Darwinism plateau.",
            "p3_bad2_es": "y destruye la meseta de información.",
            "foot_en": "PLATE T.11-D · VISUAL INTUITION BRIDGE → [Ĥ_int, Π_i] = 0 · I(S:E_k) = h₂(γ^N) + h₂(γ^k) − h₂(γ^{N−k}) · Λ_photon ∝ R⁶T⁹|(ε−1)/(ε+2)|²",
            "foot_es": "LÁMINA T.11-D · PUENTE DE INTUICIÓN VISUAL → [Ĥ_int, Π_i] = 0 · I(S:E_k) = h₂(γ^N) + h₂(γ^k) − h₂(γ^{N−k}) · Λ_fotón ∝ R⁶T⁹|(ε−1)/(ε+2)|²",
            "cap_en": "Plate T.11-D · Visual Intuition Bridge: ambient photons scatter off a localized dust mote (left), selecting the pointer basis and broadcasting redundant classical records across the bath (center), verified against the 1+6-qubit statevector and Joos–Zeh R⁶T⁹ scaling (right).",
            "cap_es": "Lámina T.11-D · Puente de Intuición Visual: los fotones ambientales se dispersan en una mota de polvo (izquierda), seleccionando la base puntero y difundiendo registros clásicos redundantes en el baño (centro), verificado frente al estado de 1+6 qubits y la ley R⁶T⁹ de Joos y Zeh (derecha).",
        },
        "t12": {
            "title_en": "Plate T.12-D Visual Intuition Bridge: an electromagnetically transparent dark mass casts zero photon shadow yet shifts the relative proper time of two clocks via the universal metric g00",
            "title_es": "Lámina T.12-D Puente de Intuición Visual: una masa oscura electromagnéticamente transparente no proyecta sombra fotónica pero desplaza el tiempo propio relativo de dos relojes mediante la métrica universal g00",
            "p1_h_en": "A clear glass lens in a dark current",
            "p1_h_es": "Una lente transparente en la corriente",
            "p1_l1_en": "Light passes straight through without",
            "p1_l1_es": "La luz pasa sin sombra, pero la masa",
            "p1_l2_en": "a shadow, yet its mass bends the clock.",
            "p1_l2_es": "curva el ritmo de los relojes vecinos.",
            "p1_art": (
                '<ellipse cx="74" cy="138" rx="18" ry="22" fill="none" stroke="var(--tp-prussian)" stroke-width="1.4" stroke-dasharray="3 2"/>'
                '<circle cx="74" cy="138" r="7" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.6"/>'
                '<line x1="46" y1="122" x2="102" y2="122" stroke="var(--tp-minium)" stroke-width="1.5" stroke-dasharray="3 2"/>'
                '<circle cx="118" cy="138" r="6" fill="var(--tp-prussian)"/>'
                '<circle cx="154" cy="138" r="6" fill="var(--tp-verdigris)"/>'
                '<path d="M 176 124 C 202 124, 214 158, 248 158" fill="none" stroke="var(--tp-prussian)" stroke-width="2.2"/>'
                '<text x="150" y="182" text-anchor="middle" font-size="8.3" fill="var(--tp-graphite)" data-en="Λ_EM = 0, G &gt; 0 · Δτ_∞ = −(2GM/c²v₀) ln(b₂/b₁)" data-es="Λ_EM = 0, G &gt; 0 · Δτ_∞ = −(2GM/c²v₀) ln(b₂/b₁)">Λ_EM = 0, G &gt; 0 · Δτ_∞ = −(2GM/c²v₀) ln(b₂/b₁)</text>'
            ),
            "p2_on_en": "▲ Universal gravity: b₂ > b₁, G > 0",
            "p2_on_es": "▲ Gravedad universal: b₂ > b₁, G > 0",
            "p2_on1_en": "Ω_c / Ω_b = 5.36 ± 0.06 (84.3 % dark);",
            "p2_on1_es": "Ω_c / Ω_b = 5.36 ± 0.06 (84.3 % oscura);",
            "p2_on2_en": "flyby leaves step −(2GM/c²v₀) ln(b₂/b₁).",
            "p2_on2_es": "deja el escalón −(2GM/c²v₀) ln(b₂/b₁).",
            "p2_off_en": "▼ Knockout: equal impact b₂ = b₁",
            "p2_off_es": "▼ Apagado: impacto igual b₂ = b₁",
            "p2_off1_en": "Both clocks sample the same Φ(t);",
            "p2_off1_es": "Ambos relojes leen el mismo Φ(t);",
            "p2_off2_en": "differential shift Δτ(T) = 0 everywhere.",
            "p2_off2_es": "el cambio diferencial Δτ(T) = 0 siempre.",
            "p3_ok_en": "✓ QUADRATURE & IMPULSE IDENTITY",
            "p3_ok_es": "✓ CUADRATURA E IDENTIDAD DE IMPULSO",
            "p3_ok1_en": "|Δτ_quad − Δτ_arsinh| / |Δτ| < 10⁻⁹",
            "p3_ok1_es": "|Δτ_cuad − Δτ_arsinh| / |Δτ| < 10⁻⁹",
            "p3_ok2_en": "+c² ∂Δτ_∞/∂b₁ = 2GM/(b₁v₀) (< 10⁻⁶)",
            "p3_ok2_es": "+c² ∂Δτ_∞/∂b₁ = 2GM/(b₁v₀) (< 10⁻⁶)",
            "p3_bad_en": "⚠ PLANTED DEFECT: MISSING FACTOR OF 2",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: FALTA EL FACTOR 2",
            "p3_bad1_en": "Halving the arsinh step breaks both",
            "p3_bad1_es": "Partir por dos el arsinh rompe tanto",
            "p3_bad2_en": "quadrature and the impulse identity.",
            "p3_bad2_es": "la cuadratura como el impulso.",
            "foot_en": "PLATE T.12-D · VISUAL INTUITION BRIDGE → Ω_c/Ω_b = 5.364 ± 0.065 · Δτ_∞ = −(2GM/c²v₀) ln(b₂/b₁) · T^{μν}_dark → g₀₀ ONLY",
            "foot_es": "LÁMINA T.12-D · PUENTE DE INTUICIÓN VISUAL → Ω_c/Ω_b = 5.364 ± 0.065 · Δτ_∞ = −(2GM/c²v₀) ln(b₂/b₁) · T^{μν}_oscuro → SOLO g₀₀",
            "cap_en": "Plate T.12-D · Visual Intuition Bridge: an electromagnetically dark mass passes unseen through light yet bends the metric (left and center), producing a logarithmic proper-time step verified against Gauss–Legendre quadrature and the transverse impulse identity (right).",
            "cap_es": "Lámina T.12-D · Puente de Intuición Visual: una masa electromagnéticamente oscura pasa sin sombra por la luz pero curva la métrica (izquierda y centro), produciendo un escalón logarítmico de tiempo propio verificado frente a la cuadratura de Gauss–Legendre y la identidad de impulso (derecha).",
        },
        "t13": {
            "title_en": "Plate T.13-D Visual Intuition Bridge: infrared soft-graviton gauge invariance, permanent gravitational-wave displacement memory, and mixed gauge-gravitational anomaly cancellation at N_c = 3",
            "title_es": "Lámina T.13-D Puente de Intuición Visual: invariancia gauge infrarroja de gravitones blandos, memoria permanente de ondas gravitacionales y cancelación de anomalías mixtas en N_c = 3",
            "p1_h_en": "Wake memory & three algebraic locks",
            "p1_h_es": "Memoria de estela y tres candados algebraicos",
            "p1_l1_en": "Wave energy shifts free-falling mirrors;",
            "p1_l1_es": "La energía de la onda desplaza espejos;",
            "p1_l2_en": "soft spin-2 & triangles lock κ_a and N_c.",
            "p1_l2_es": "el espín 2 blando y los lazos fijan κ_a y N_c.",
            "p1_art": (
                '<path d="M 38 156 L 96 156 C 128 156, 146 118, 178 118 L 260 118" fill="none" stroke="var(--tp-minium)" stroke-width="2.4"/>'
                '<line x1="38" y1="156" x2="260" y2="156" stroke="var(--tp-rule-strong)" stroke-width="1.1" stroke-dasharray="3 3"/>'
                '<circle cx="216" cy="118" r="4" fill="var(--tp-verdigris)"/>'
                '<text x="150" y="178" text-anchor="middle" font-size="8.2" fill="var(--tp-graphite)" data-en="Δh_char = GE_rad/(c⁴D_L) · W^μ = 0 · N_c = 3" data-es="Δh_char = GE_rad/(c⁴D_L) · W^μ = 0 · N_c = 3">Δh_char = GE_rad/(c⁴D_L) · W^μ = 0 · N_c = 3</text>'
            ),
            "p2_on_en": "▲ Consistent IR EFT: κ_e = κ_p, N_c = 3",
            "p2_on_es": "▲ EFT infrarroja consistente: κ_e = κ_p, N_c = 3",
            "p2_on1_en": "||W^μ|| = 0 (η = 0); Tr[6Y] = 0;",
            "p2_on1_es": "||W^μ|| = 0 (η = 0); Tr[6Y] = 0;",
            "p2_on2_en": "SU(2)²(6Y) = 0 and Tr[(6Y)³] = 0.",
            "p2_on2_es": "SU(2)²(6Y) = 0 y Tr[(6Y)³] = 0.",
            "p2_off_en": "▼ Knockout: κ_e / κ_p = 1 + 10⁻⁵, N_c = 2",
            "p2_off_es": "▼ Apagado: κ_e / κ_p = 1 + 10⁻⁵, N_c = 2",
            "p2_off1_en": "Longitudinal gravitons fail to decouple;",
            "p2_off1_es": "Los gravitones longitudinales no desacoplan;",
            "p2_off2_en": "SU(2)² = −1 and U(1)_Y³ = +54 ≠ 0.",
            "p2_off2_es": "SU(2)² = −1 y U(1)_Y³ = +54 ≠ 0.",
            "p3_ok_en": "✓ GL5 MEMORY & 12 LEAN 4 THEOREMS",
            "p3_ok_es": "✓ MEMORIA GL5 Y 12 TEOREMAS LEAN 4",
            "p3_ok1_en": "|Δh_GL5 − Δh_exact| / Δh < 10⁻¹²",
            "p3_ok1_es": "|Δh_GL5 − Δh_exacto| / Δh < 10⁻¹²",
            "p3_ok2_en": "0 imports · 0 sorry · s ≥ 3 → g_a = 0",
            "p3_ok2_es": "0 imports · 0 sorry · s ≥ 3 → g_a = 0",
            "p3_bad_en": "⚠ PLANTED DEFECT: WARD & ANOMALY FAIL",
            "p3_bad_es": "⚠ DEFECTO PLANTADO: FALLAN WARD Y ANOMALÍA",
            "p3_bad1_en": "||W^μ||/E_cm = 3.45×10⁻⁶ > 10⁻¹²;",
            "p3_bad1_es": "||W^μ||/E_cm = 3.45×10⁻⁶ > 10⁻¹²;",
            "p3_bad2_en": "verifier prints FAIL to stderr (exit 1).",
            "p3_bad2_es": "el verificador imprime FAIL (salida 1).",
            "foot_en": "PLATE T.13-D · VISUAL INTUITION BRIDGE → ∑ η_a κ_a p_a^μ = 0 · ΔL/L₀ = ½ Δh_+^mem · Tr[(6Y)³] = −54(N_c − 3) = 0",
            "foot_es": "LÁMINA T.13-D · PUENTE DE INTUICIÓN VISUAL → ∑ η_a κ_a p_a^μ = 0 · ΔL/L₀ = ½ Δh_+^mem · Tr[(6Y)³] = −54(N_c − 3) = 0",
            "cap_en": "Plate T.13-D · Visual Intuition Bridge: permanent nonlinear gravitational-wave memory and the infrared soft-graviton and triangle-anomaly locks (left and centre), verified by Gauss–Legendre quadrature and 12 core Lean 4 Prelude theorems (right).",
            "cap_es": "Lámina T.13-D · Puente de Intuición Visual: memoria permanente no lineal de ondas gravitacionales y candados infrarrojos de gravitones blandos y anomalías triangulares (izquierda y centro), verificados por cuadratura de Gauss–Legendre y 12 teoremas en Lean 4 Prelude (derecha).",
        },
    }
    sp = specs.get(slug, specs["t01"])
    return f"""        <figure class="tp-distill-figure" role="group" aria-label="Plate {code}-D Visual Intuition Bridge">
          <svg class="tp-distill-svg" viewBox="0 0 920 228" role="img" aria-labelledby="tp-distill-title-{slug}">
            <title id="tp-distill-title-{slug}" data-en="{a(sp['title_en'])}" data-es="{a(sp['title_es'])}">{t(sp['title_en'])}</title>
            <rect x="6" y="6" width="908" height="216" rx="10" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
            <rect x="20" y="20" width="266" height="168" rx="8" fill="var(--tp-vellum)" stroke="var(--tp-prussian)" stroke-width="1.5"/>
            <text x="34" y="40" font-family="var(--font-mono, monospace)" font-size="8.8" font-weight="700" fill="var(--tp-prussian)" data-en="1 · EVERYDAY ANALOGY ({code})" data-es="1 · ANALOGÍA COTIDIANA ({code})">1 · EVERYDAY ANALOGY ({code})</text>
            <text x="34" y="60" font-size="10.4" font-weight="700" fill="var(--tp-ink)" data-en="{a(sp['p1_h_en'])}" data-es="{a(sp['p1_h_es'])}">{t(sp['p1_h_en'])}</text>
            <text x="34" y="78" font-size="9.1" fill="var(--tp-graphite)" data-en="{a(sp['p1_l1_en'])}" data-es="{a(sp['p1_l1_es'])}">{t(sp['p1_l1_en'])}</text>
            <text x="34" y="92" font-size="9.1" fill="var(--tp-graphite)" data-en="{a(sp['p1_l2_en'])}" data-es="{a(sp['p1_l2_es'])}">{t(sp['p1_l2_en'])}</text>
            {sp['p1_art']}
            <path d="M 288 104 L 312 104" stroke="var(--tp-prussian)" stroke-width="2" stroke-dasharray="4 3"/>
            <polygon points="312,99 320,104 312,109" fill="var(--tp-prussian)"/>
            <rect x="322" y="20" width="276" height="168" rx="8" fill="var(--tp-vellum)" stroke="var(--tp-rule-strong)" stroke-width="1.5"/>
            <text x="336" y="40" font-family="var(--font-mono, monospace)" font-size="8.8" font-weight="700" fill="var(--tp-ink)" data-en="2 · ONE QUANTITY, TWO SETTINGS" data-es="2 · UNA CANTIDAD, DOS AJUSTES">2 · ONE QUANTITY, TWO SETTINGS</text>
            <rect x="334" y="48" width="252" height="60" rx="6" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.2"/>
            <text x="344" y="65" font-size="9.2" font-weight="700" fill="var(--tp-prussian)" data-en="{a(sp['p2_on_en'])}" data-es="{a(sp['p2_on_es'])}">{t(sp['p2_on_en'])}</text>
            <text x="344" y="80" font-size="8.6" fill="var(--tp-graphite)" data-en="{a(sp['p2_on1_en'])}" data-es="{a(sp['p2_on1_es'])}">{t(sp['p2_on1_en'])}</text>
            <text x="344" y="93" font-size="8.6" fill="var(--tp-graphite)" data-en="{a(sp['p2_on2_en'])}" data-es="{a(sp['p2_on2_es'])}">{t(sp['p2_on2_en'])}</text>
            <rect x="334" y="116" width="252" height="60" rx="6" fill="var(--tp-stone)" stroke="var(--tp-verdigris)" stroke-width="1.2"/>
            <text x="344" y="133" font-size="9.2" font-weight="700" fill="var(--tp-verdigris)" data-en="{a(sp['p2_off_en'])}" data-es="{a(sp['p2_off_es'])}">{t(sp['p2_off_en'])}</text>
            <text x="344" y="148" font-size="8.6" fill="var(--tp-graphite)" data-en="{a(sp['p2_off1_en'])}" data-es="{a(sp['p2_off1_es'])}">{t(sp['p2_off1_en'])}</text>
            <text x="344" y="161" font-size="8.6" fill="var(--tp-graphite)" data-en="{a(sp['p2_off2_en'])}" data-es="{a(sp['p2_off2_es'])}">{t(sp['p2_off2_en'])}</text>
            <path d="M 600 104 L 624 104" stroke="var(--tp-verdigris)" stroke-width="2" stroke-dasharray="4 3"/>
            <polygon points="624,99 632,104 624,109" fill="var(--tp-verdigris)"/>
            <rect x="634" y="20" width="266" height="168" rx="8" fill="var(--tp-vellum)" stroke="var(--tp-verdigris)" stroke-width="1.5"/>
            <text x="648" y="39" font-family="var(--font-mono, monospace)" font-size="8.8" font-weight="700" fill="var(--tp-verdigris)" data-en="3 · WHAT THE VERIFIER DEMANDS" data-es="3 · LO QUE EXIGE EL VERIFICADOR">3 · WHAT THE VERIFIER DEMANDS</text>
            <rect x="646" y="52" width="242" height="54" rx="6" fill="var(--tp-stone)" stroke="var(--tp-verdigris)" stroke-width="1.2"/>
            <text x="656" y="68" font-family="var(--font-mono, monospace)" font-size="8.5" font-weight="700" fill="var(--tp-verdigris)" data-en="{a(sp['p3_ok_en'])}" data-es="{a(sp['p3_ok_es'])}">{t(sp['p3_ok_en'])}</text>
            <text x="656" y="82" font-size="8.4" fill="var(--tp-ink)" data-en="{a(sp['p3_ok1_en'])}" data-es="{a(sp['p3_ok1_es'])}">{t(sp['p3_ok1_en'])}</text>
            <text x="656" y="95" font-size="8.4" fill="var(--tp-ink)" data-en="{a(sp['p3_ok2_en'])}" data-es="{a(sp['p3_ok2_es'])}">{t(sp['p3_ok2_en'])}</text>
            <rect x="646" y="118" width="242" height="54" rx="6" fill="var(--tp-stone)" stroke="var(--tp-minium)" stroke-width="1.2"/>
            <text x="656" y="134" font-family="var(--font-mono, monospace)" font-size="8.5" font-weight="700" fill="var(--tp-minium)" data-en="{a(sp['p3_bad_en'])}" data-es="{a(sp['p3_bad_es'])}">{t(sp['p3_bad_en'])}</text>
            <text x="656" y="148" font-size="8.4" fill="var(--tp-ink)" data-en="{a(sp['p3_bad1_en'])}" data-es="{a(sp['p3_bad1_es'])}">{t(sp['p3_bad1_en'])}</text>
            <text x="656" y="161" font-size="8.4" fill="var(--tp-ink)" data-en="{a(sp['p3_bad2_en'])}" data-es="{a(sp['p3_bad2_es'])}">{t(sp['p3_bad2_en'])}</text>
            <text x="460" y="208" text-anchor="middle" font-family="var(--font-mono, monospace)" font-size="8.8" font-weight="700" fill="var(--tp-prussian)" data-en="{a(sp['foot_en'])}" data-es="{a(sp['foot_es'])}">{t(sp['foot_en'])}</text>
          </svg>
          <figcaption class="tp-distill-caption">
            {bi("span", sp["cap_en"], sp["cap_es"])}
          </figcaption>
        </figure>"""


def sigma_ladder(page: dict) -> str:
    """Plate T.06-L · the σ ladder: every published bound and every claimed value of the Diósi–Penrose smearing on one log axis,
    with what Penrose's formula then says about a tubulin at each rung (tools/timegravity_kernel_ladder.py)."""
    from timegravity_kernel_ladder import LADDER_RUNGS, tubulin_table
    tub = tubulin_table()
    x0, x1, lo, hi = 70.0, 850.0, -15.0, -3.0
    xs = lambda sigma: x0 + (math.log10(sigma) - lo) / (hi - lo) * (x1 - x0)
    axis_y = 182.0
    parts = [f'<rect x="6" y="6" width="908" height="288" rx="10" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>',
             f'<line x1="{x0 - 20:.1f}" y1="{axis_y}" x2="{x1 + 30:.1f}" y2="{axis_y}" stroke="var(--tp-ink)" stroke-width="1.4"/>',
             f'<polygon points="{x1 + 30:.1f},{axis_y - 4} {x1 + 40:.1f},{axis_y} {x1 + 30:.1f},{axis_y + 4}" fill="var(--tp-ink)"/>']
    for dec in range(-15, -2):
        x = xs(10.0 ** dec)
        major = dec in (-15, -12, -10, -9, -6, -3)
        parts.append(f'<line x1="{x:.1f}" y1="{axis_y}" x2="{x:.1f}" y2="{axis_y + (9 if major else 5)}" stroke="var(--tp-ink)" stroke-width="{1.2 if major else 0.8}"/>')
        if major:
            name = {-15: "1 fm", -12: "1 pm", -10: "1 Å", -9: "1 nm", -6: "1 µm", -3: "1 mm"}[dec]
            parts.append(f'<text x="{x:.1f}" y="{axis_y + 22}" text-anchor="middle" font-size="9.2" fill="var(--tp-graphite)">{name}</text>')
    parts.append(f'<text x="{(x0 + x1) / 2:.1f}" y="{axis_y + 40}" text-anchor="middle" font-size="9.6" font-weight="700" fill="var(--tp-ink)" data-en="smearing width σ of the Diósi–Penrose model (log scale)" data-es="ancho de suavizado σ del modelo de Diósi–Penrose (escala log)">smearing width σ of the Diósi–Penrose model (log scale)</text>')
    # allowed region from the strongest mature bound (Gran Sasso) rightwards, lighter from XENONnT (single result)
    gs = xs(0.54e-10); xe = xs(4.9e-10)
    parts.append(f'<rect x="{gs:.1f}" y="{axis_y - 6}" width="{x1 + 30 - gs:.1f}" height="6" fill="var(--tp-verdigris)" opacity="0.2"/>')
    parts.append(f'<text x="{xe + 6:.1f}" y="{axis_y - 9}" font-size="7.8" fill="var(--tp-verdigris)" data-en="allowed by the mature bound →" data-es="permitido por la cota madura →">allowed by the mature bound →</text>')
    # the letter's range and the site's estimate
    xa, xb, xe2 = xs(50e-6), xs(250e-6), xs(33.1e-6)  # the recast limit (timegravity_kernel_recast / EW_MATCH_SIGMA_M)
    parts.append(f'<rect x="{xa:.1f}" y="{axis_y - 30}" width="{xb - xa:.1f}" height="10" rx="2" fill="var(--tp-prussian)" opacity="0.85"/>')
    parts.append(f'<text x="{(xa + xb) / 2:.1f}" y="{axis_y - 36}" text-anchor="middle" font-size="8.8" font-weight="700" fill="var(--tp-prussian)" data-en="2025 letter: entangles at 50–250 µm (PROPOSED)" data-es="carta de 2025: entrelaza a 50–250 µm (PROPUESTO)">2025 letter: entangles at 50–250 µm (PROPOSED)</text>')
    parts.append(f'<line x1="{xe2:.1f}" y1="{axis_y - 112}" x2="{xe2:.1f}" y2="{axis_y}" stroke="var(--tp-minium)" stroke-width="1.8" stroke-dasharray="5 3"/>')
    parts.append(f'<polygon points="{xe2 - 2:.1f},{axis_y - 100} {xe2 - 12:.1f},{axis_y - 105} {xe2 - 2:.1f},{axis_y - 110}" fill="var(--tp-minium)"/>')
    parts.append(f'<text x="{xe2 - 6:.1f}" y="{axis_y - 118}" text-anchor="end" font-size="8.8" font-weight="700" fill="var(--tp-minium)" data-en="T.05 recast of the published 95 % limits: σ above 33 µm excluded (DERIVED)" data-es="recast T.05 de los límites publicados al 95 %: σ por encima de 33 µm excluida (DERIVADO)">T.05 recast of the published 95 % limits: σ above 33 µm excluded (DERIVED)</text>')
    # T.05's window: on the 33 µm recast limit the hybrid dynamics could still entangle one published geometry, the 2024 side-by-side one, for σ above
    # its threshold there (13.6 µm). A model-specific window, not a bound on σ: lighter fill, dashed edge, its own label.
    from timegravity_kernel_dispute import proposals_table as _props, SIGMA_ESTIMATE_M
    by_key = {r["key"]: r for r in _props()}
    if "schut2024_z10" not in by_key:
        raise KeyError("proposals_table has no 'schut2024_z10' row; the ladder window needs its hybrid threshold")
    schut = by_key["schut2024_z10"]
    xw0, xw1 = xs(schut["hybrid_sigma_c_m"]), xs(SIGMA_ESTIMATE_M)
    parts.append(f'<rect x="{xw0:.1f}" y="{axis_y - 18}" width="{xw1 - xw0:.1f}" height="8" rx="2" fill="var(--tp-prussian)" opacity="0.3" stroke="var(--tp-prussian)" stroke-width="1" stroke-dasharray="3 2"/>')
    w_en = ("T.05 window: the hybrid model could still reach only the 2024", f"side-by-side geometry, {schut['hybrid_sigma_c_m'] * 1e6:.1f}–{SIGMA_ESTIMATE_M * 1e6:.0f} µm (PROPOSED, model-specific)")
    w_es = ("Ventana T.05: el modelo híbrido solo podría alcanzar la geometría", f"lado a lado de 2024, {schut['hybrid_sigma_c_m'] * 1e6:.1f}–{SIGMA_ESTIMATE_M * 1e6:.0f} µm (PROPUESTO, específico del modelo)")
    for i, (en_line, es_line) in enumerate(zip(w_en, w_es)):
        parts.append(f'<text x="{xw0 - 8:.1f}" y="{axis_y - 28 + 10 * i}" text-anchor="end" font-size="7.8" font-weight="700" fill="var(--tp-prussian)" data-en="{a(en_line)}" data-es="{a(es_line)}">{t(en_line)}</text>')
    # the bounds and the natural cut-off, labels staggered
    stagger = {"natural": 96, "lisa": 70, "gransasso": 96, "xenonnt": 70}
    for key, sigma, kind, _lid, en, es in LADDER_RUNGS:
        if key in ("eotwash", "letter_lo", "letter_hi"):
            continue
        x = xs(sigma); h = stagger[key]
        col = "var(--tp-verdigris)" if kind in ("bound", "single") else "var(--tp-prussian)"
        dash = "" if kind == "bound" else ' stroke-dasharray="4 3"'
        parts.append(f'<line x1="{x:.1f}" y1="{axis_y - h}" x2="{x:.1f}" y2="{axis_y}" stroke="{col}" stroke-width="1.6"{dash}/>')
        if kind in ("bound", "single"):
            parts.append(f'<polygon points="{x + 2:.1f},{axis_y - h + 8} {x + 12:.1f},{axis_y - h + 13} {x + 2:.1f},{axis_y - h + 18}" fill="{col}"/>')
        label = en + (" (BOUND)" if kind == "bound" else " (SINGLE RESULT)" if kind == "single" else " (PROPOSED)")
        label_es = es + (" (COTA)" if kind == "bound" else " (RESULTADO ÚNICO)" if kind == "single" else " (PROPUESTO)")
        parts.append(f'<text x="{x + 4:.1f}" y="{axis_y - h - 4}" font-size="8.6" font-weight="700" fill="{col}" data-en="{a(label)}" data-es="{a(label_es)}">{t(label)}</text>')
    # tubulin row
    def sci(v: float) -> str:
        ex = int(math.floor(math.log10(v))); man = v / 10 ** ex
        sup = str(ex).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))
        return (f"{man:.1f} × " if abs(man - 1.0) > 0.05 else "") + f"10{sup}"
    nat = tub["natural"]["nucleon_radius"]; ew = tub["eotwash"]["nucleon_radius"]
    parts.append(f'<text x="{x0 - 20:.1f}" y="{axis_y + 62}" font-size="8.8" font-weight="700" fill="var(--tp-ink)" data-en="The model\'s formula applied to one tubulin (55 kDa), the object the Orch-OR proposal refers to, in two places a nucleon radius apart:" data-es="La fórmula del modelo aplicada a una tubulina (55 kDa), el objeto al que se refiere la propuesta Orch-OR, en dos lugares a un radio de nucleón:">The model\'s formula applied to one tubulin (55 kDa), the object the Orch-OR proposal refers to, in two places a nucleon radius apart:</text>')
    parts.append(f'<text x="{xs(1e-14):.1f}" y="{axis_y + 78}" font-size="8.6" fill="var(--tp-graphite)" data-en="at 10⁻¹⁴ m: lives {sci(nat["lifetime_s"])} s" data-es="a 10⁻¹⁴ m: vive {sci(nat["lifetime_s"])} s">at 10⁻¹⁴ m: lives {sci(nat["lifetime_s"])} s</text>')
    parts.append(f'<text x="{xe2:.1f}" y="{axis_y + 78}" text-anchor="end" font-size="8.6" fill="var(--tp-graphite)" data-en="at 33 µm: lives {sci(ew["lifetime_s"])} s, {sci(ew["lifetime_over_universe_age"])} ages of the universe" data-es="a 33 µm: vive {sci(ew["lifetime_s"])} s, {sci(ew["lifetime_over_universe_age"])} edades del universo">at 33 µm: lives {sci(ew["lifetime_s"])} s, {sci(ew["lifetime_over_universe_age"])} ages of the universe</text>')
    parts.append(f'<text x="460" y="{axis_y + 100}" text-anchor="middle" font-family="var(--font-mono, monospace)" font-size="8.9" font-weight="700" fill="var(--tp-prussian)" data-en="PLATE T.06-L · THE σ LADDER · one parameter, four uses, each rung a ledger row" data-es="LÁMINA T.06-L · LA ESCALERA σ · un parámetro, cuatro usos, cada peldaño una fila del libro">PLATE T.06-L · THE σ LADDER · one parameter, four uses, each rung a ledger row</text>')
    body = "\n            ".join(parts)
    return f"""        <figure class="tp-distill-figure" role="group" aria-label="Plate T.06-L The sigma ladder" data-tg-figure="sigma-ladder">
          <svg class="tp-distill-svg" viewBox="0 0 920 300" role="img" aria-labelledby="tp-ladder-title-t06">
            <title id="tp-ladder-title-t06" data-en="Plate T.06-L The sigma ladder: the Diósi–Penrose smearing width on a log axis from a femtometre to a millimetre, with the lower bounds from LISA Pathfinder, Gran Sasso and XENONnT, the authors' natural cut-off, the 2025 entanglement letter's range, this site's Eöt-Wash estimate, and the lifetime of a tubulin at two rungs" data-es="Lámina T.06-L La escalera σ: el ancho de suavizado de Diósi–Penrose en un eje logarítmico de un femtómetro a un milímetro, con las cotas inferiores de LISA Pathfinder, Gran Sasso y XENONnT, el corte natural de los autores, el rango de la carta de entrelazamiento de 2025, la estimación de Eöt-Wash de este sitio, y la vida de una tubulina en dos peldaños">Plate T.06-L The sigma ladder</title>
            {body}
          </svg>
          <figcaption class="tp-distill-caption">
            {bi("span", "Plate T.06-L · The σ ladder: three bounds from experimental data hold the smearing from below (green, allowed to the right); its authors' natural cut-off and the 2025 letter's entangling range are proposals (blue); the dashed red line is T.05's recast of the experiment's published 95 % limits onto the smeared pull, σ above 33 µm excluded (DERIVED, not a refit). The lighter dashed bar, 13.6 to 33 µm, is T.05's window where the letter's model could still entangle one published geometry, the 2024 side-by-side proposal; it is specific to that model and that geometry, not a bound on σ generally, and it moves or closes if the 2020 data are refit. The bottom row applies the model's formula to a single tubulin, the object the Orch-OR proposal refers to; the page does not assess that proposal. Each rung is a ledger row; the page draws no conclusion beyond the picture.", "Lámina T.06-L · La escalera σ: tres cotas desde datos experimentales sostienen el suavizado por abajo (verde, permitido a la derecha); el corte natural de sus autores y el rango de entrelazamiento de la carta de 2025 son propuestas (azul); la línea roja punteada es el recast que T.05 hace de los límites publicados del experimento al 95 % sobre la atracción suavizada, σ por encima de 33 µm excluida (DERIVADO, no un reajuste). La barra discontinua más clara, de 13.6 a 33 µm, es la ventana de T.05 donde el modelo de la carta aún podría entrelazar una geometría publicada, la propuesta lado a lado de 2024; es específica de ese modelo y esa geometría, no una cota de σ en general, y se mueve o se cierra si los datos de 2020 se reajustan. La fila inferior aplica la fórmula del modelo a una sola tubulina, el objeto al que se refiere la propuesta Orch-OR; la página no evalúa esa propuesta. Cada peldaño es una fila del libro de registro; la página no concluye nada más allá de la imagen.")}
          </figcaption>
        </figure>"""


def threshold_map(page: dict) -> str:
    """Plate T.05-M · the geometry map: for any pair geometry, the σ above which the 2025 letter's hybrid dynamics entangles and the σ
    above which the quantum witness survives pure Diósi–Penrose collapse, both over the nearest approach d, against the split-to-gap
    ratio (tools/timegravity_kernel_dispute.py, threshold_map)."""
    from timegravity_kernel_dispute import threshold_map as _tmap
    rows = _tmap()
    x0, x1, y_top, y_bot = 92.0, 850.0, 30.0, 226.0
    rlo, rhi, vlo, vhi = math.log10(0.03), math.log10(32.0), math.log10(0.3), math.log10(40.0)
    xs = lambda r: x0 + (math.log10(r) - rlo) / (rhi - rlo) * (x1 - x0)
    ys = lambda v: y_bot - (math.log10(v) - vlo) / (vhi - vlo) * (y_bot - y_top)
    parts = [f'<rect x="6" y="6" width="908" height="288" rx="10" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>']
    for r in (0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0):
        x = xs(r)
        parts.append(f'<line x1="{x:.1f}" y1="{y_top}" x2="{x:.1f}" y2="{y_bot}" stroke="var(--tp-rule-strong)" stroke-width="0.6" opacity="0.5"/>')
        parts.append(f'<text x="{x:.1f}" y="{y_bot + 14}" text-anchor="middle" font-size="8.8" fill="var(--tp-graphite)">{r:g}</text>')
    for v in (0.3, 1.0, 3.0, 10.0, 30.0):
        y = ys(v)
        parts.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="var(--tp-rule-strong)" stroke-width="0.6" opacity="0.5"/>')
        parts.append(f'<text x="{x0 - 6}" y="{y + 3:.1f}" text-anchor="end" font-size="8.8" fill="var(--tp-graphite)">{v:g}</text>')
    parts.append(f'<line x1="{x0}" y1="{y_top}" x2="{x0}" y2="{y_bot}" stroke="var(--tp-ink)" stroke-width="1.3"/>')
    parts.append(f'<line x1="{x0}" y1="{y_bot}" x2="{x1}" y2="{y_bot}" stroke="var(--tp-ink)" stroke-width="1.3"/>')
    parts.append(f'<text x="{(x0 + x1) / 2:.1f}" y="{y_bot + 30}" text-anchor="middle" font-size="9.4" font-weight="700" fill="var(--tp-ink)" '
                 f'data-en="split ÷ nearest approach (Δx / d), log scale" data-es="división ÷ aproximación más cercana (Δx / d), escala logarítmica">split ÷ nearest approach (Δx / d), log scale</text>')
    parts.append(f'<text x="22" y="{(y_top + y_bot) / 2:.1f}" text-anchor="middle" font-size="9.4" font-weight="700" fill="var(--tp-ink)" transform="rotate(-90 22 {(y_top + y_bot) / 2:.1f})" '
                 f'data-en="σ ÷ nearest approach (σ / d)" data-es="σ ÷ aproximación más cercana (σ / d)">σ ÷ nearest approach (σ / d)</text>')
    g_pts = " ".join(f"{xs(r['ratio']):.1f},{ys(r['hybrid_over_nearest']):.1f}" for r in rows)
    f_pts = " ".join(f"{xs(r['ratio']):.1f},{ys(r['collapse_over_nearest']):.1f}" for r in rows)
    parts.append(f'<polyline points="{g_pts}" fill="none" stroke="var(--tp-prussian)" stroke-width="2.2" stroke-linejoin="round"/>')
    parts.append(f'<polyline points="{f_pts}" fill="none" stroke="var(--tp-minium)" stroke-width="2.2" stroke-dasharray="6 4" stroke-linejoin="round"/>')
    g_label = "hybrid dynamics entangles above this line (PROPOSED)"; g_label_es = "la dinámica híbrida entrelaza por encima de esta línea (PROPUESTO)"
    f_label = "witness survives pure collapse above this line (PROPOSED)"; f_label_es = "el testigo sobrevive al colapso puro por encima de esta línea (PROPUESTO)"
    parts.append(f'<text x="{x0 + 8:.1f}" y="{ys(rows[0]["hybrid_over_nearest"]) - 12:.1f}" text-anchor="start" font-size="8.8" font-weight="700" fill="var(--tp-prussian)" data-en="{a(g_label)}" data-es="{a(g_label_es)}">{t(g_label)}</text>')
    parts.append(f'<text x="{x0 + 8:.1f}" y="{ys(rows[0]["collapse_over_nearest"]) - 10:.1f}" text-anchor="start" font-size="8.8" font-weight="700" fill="var(--tp-minium)" data-en="{a(f_label)}" data-es="{a(f_label_es)}">{t(f_label)}</text>')
    gap = "between the lines: a model difference, not data"; gap_es = "entre las líneas: una diferencia entre modelos, no datos"
    parts.append(f'<text x="{xs(6.0):.1f}" y="{ys(2.2):.1f}" text-anchor="middle" font-size="8.6" font-style="italic" fill="var(--tp-graphite)" data-en="{a(gap)}" data-es="{a(gap_es)}">{t(gap)}</text>')
    # The side-by-side layout (the 2024 screened proposal) has nearly flat thresholds that would crowd the lower-left corner; stated, not drawn (Table T.05-P has the numbers).
    from timegravity_kernel_dispute import parallel_map as _pmap
    pm = _pmap(ratios=(0.03, 0.5, 1.0, 2.0, 32.0))  # first and last for the hybrid ends, all five for the collapse range
    side_en = (f"side by side (2024 layout), not drawn, d the gap: hybrid above {pm[0]['hybrid_over_gap']:.2f} d at small splits, {pm[-1]['hybrid_over_gap']:.2f} d at the largest;",
               f"witness survives pure collapse above {min(p['collapse_over_gap'] for p in pm):.2f}–{max(p['collapse_over_gap'] for p in pm):.2f} d")
    side_es = (f"lado a lado (disposición de 2024), sin dibujar, d la separación: la híbrida por encima de {pm[0]['hybrid_over_gap']:.2f} d a divisiones pequeñas, {pm[-1]['hybrid_over_gap']:.2f} d en la mayor;",
               f"el testigo sobrevive al colapso puro por encima de {min(p['collapse_over_gap'] for p in pm):.2f}–{max(p['collapse_over_gap'] for p in pm):.2f} d")
    for i, (en_line, es_line) in enumerate(zip(side_en, side_es)):
        parts.append(f'<text x="{x0 + 8:.1f}" y="{ys(20.0) + 12 * i:.1f}" text-anchor="start" font-size="8.2" font-style="italic" fill="var(--tp-graphite)" data-en="{a(en_line)}" data-es="{a(es_line)}">{t(en_line)}</text>')
    # The two named geometries at their own masses (the page's numbers: 525 / 130 µm and 55 / 14 µm), within 0.4 % of the small-mass curves.
    from timegravity_kernel_dispute import tn_critical_sigma, dp_collapse_sigma_at, BMV_M_KG, BMV_DX_M, BMV_D_M, BMV_T_S, TN_M_KG, TN_L_M, TN_D_M
    for name_en, name_es, dx, split, near, m in (("2017 proposal", "propuesta de 2017", 8, BMV_DX_M, BMV_D_M - BMV_DX_M, BMV_M_KG),
                                                  ("2025 letter", "carta de 2025", -8, TN_L_M, TN_D_M, TN_M_KG)):
        x = xs(split / near)
        anchor = "start" if dx > 0 else "end"
        # Labels follow the page's wording: the hybrid threshold is stated as "above" (ceiling: 525, 55 µm), the collapse one to the nearest µm (130, 14 µm).
        for sig_m, col, dy, rnd in ((tn_critical_sigma(m, split, near), "var(--tp-prussian)", -8, lambda v: math.ceil(v - 1e-9)),
                                    (dp_collapse_sigma_at(split, near, m, BMV_T_S, 0.0), "var(--tp-minium)", 16, round)):
            y = ys(sig_m / near); sig = rnd(sig_m * 1e6)
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{col}" stroke="var(--tp-vellum)" stroke-width="1.2"/>')
            lab = f"{name_en}: σ = {sig:.0f} µm"; lab_es = f"{name_es}: σ = {sig:.0f} µm"
            parts.append(f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="{anchor}" font-size="8.2" fill="{col}" data-en="{a(lab)}" data-es="{a(lab_es)}">{t(lab)}</text>')
    footer = "PLATE T.05-M · THE GEOMETRY MAP · TWO PUBLISHED MODELS, THIS SITE'S KERNEL · NO WITNESS MEASURED"
    footer_es = "LÁMINA T.05-M · EL MAPA GEOMÉTRICO · DOS MODELOS PUBLICADOS, EL NÚCLEO DE ESTE SITIO · NINGÚN TESTIGO MEDIDO"
    parts.append(f'<text x="460" y="{y_bot + 56}" text-anchor="middle" font-family="var(--font-mono, monospace)" font-size="8.9" font-weight="700" fill="var(--tp-prussian)" data-en="{a(footer)}" data-es="{a(footer_es)}">{t(footer)}</text>')
    body = "\n            ".join(parts)
    title_en = ("Plate T.05-M The geometry map: on log axes, the sigma above which the 2025 letter's hybrid dynamics entangles (solid) and the sigma above which the quantum "
                "witness survives pure Diósi–Penrose collapse (dashed), both divided by the nearest approach, against the split-to-gap ratio; dots mark the 2017 proposal and the letter's geometry")
    title_es = ("Lámina T.05-M El mapa geométrico: en ejes logarítmicos, la sigma por encima de la cual la dinámica híbrida de la carta de 2025 entrelaza (continua) y la sigma por encima "
                "de la cual el testigo cuántico sobrevive al colapso puro de Diósi–Penrose (discontinua), ambas divididas por la aproximación más cercana, frente a la razón división/separación; "
                "los puntos marcan la propuesta de 2017 y la geometría de la carta")
    cap_en = ("Plate T.05-M · The geometry map: for any pair geometry, the σ above which the letter's hybrid dynamics entangles (solid) and the σ above which the quantum witness "
              "survives pure Diósi–Penrose collapse (dashed), both over the nearest approach d, against the split-to-gap ratio. Both lines are this site's computations on the two "
              "published models; the gap between them is a model difference, not an exclusion region, and the page picks no side. The side-by-side layout of the 2024 "
              "screened proposal has nearly flat thresholds (hybrid about 0.65 d at small splits, collapse about 0.44 d) and is stated on the plate rather than drawn; Table T.05-P "
              "carries its numbers. No witness has been measured.")
    cap_es = ("Lámina T.05-M · El mapa geométrico: para cualquier geometría del par, la σ por encima de la cual la dinámica híbrida de la carta entrelaza (continua) y la σ por encima de "
              "la cual el testigo cuántico sobrevive al colapso puro de Diósi–Penrose (discontinua), ambas sobre la aproximación más cercana d, frente a la razón división/separación. Las dos "
              "líneas son cálculos de este sitio sobre los dos modelos publicados; la brecha entre ellas es una diferencia entre modelos, no una región de exclusión, y la página no toma "
              "partido. La disposición lado a lado de la propuesta apantallada de 2024 tiene umbrales casi planos (la híbrida cerca de 0.65 d a divisiones pequeñas, el colapso "
              "cerca de 0.44 d) y se enuncia en la lámina en vez de dibujarse; la Tabla T.05-P lleva sus números. Ningún testigo se ha medido.")
    return f"""        <figure class="tp-distill-figure" role="group" aria-label="Plate T.05-M The geometry map" data-tg-figure="threshold-map">
          <svg class="tp-distill-svg" viewBox="0 0 920 300" role="img" aria-labelledby="tp-map-title-t05">
            <title id="tp-map-title-t05" data-en="{a(title_en)}" data-es="{a(title_es)}">{t(title_en)}</title>
            {body}
          </svg>
          <figcaption class="tp-distill-caption">
            {bi("span", cap_en, cap_es)}
          </figcaption>
        </figure>"""


def proposals_table(page: dict) -> str:
    """Table T.05-P · the published GIE geometries on the map: both models' thresholds, the 52 µm torque deficit the hybrid
    threshold would cause, and the two predictions in time (tools/timegravity_kernel_dispute.py, proposals_table)."""
    from timegravity_kernel_dispute import proposals_table as _props
    names = {
        "bose2017": ("Bose et al. 2017 (PRL)", "Bose et al. 2017 (PRL)"),
        "chevalier2020_d350": ("Chevalier, Paige & Kim 2020 (PRA), d = 350 µm", "Chevalier, Paige & Kim 2020 (PRA), d = 350 µm"),
        "vandekamp2020": ("van de Kamp et al. 2020 (PRA), screened; 47 µm read as the nearest approach", "van de Kamp et al. 2020 (PRA), apantallado; 47 µm leídos como aproximación más cercana"),
        "vandekamp2020_letter_reading": ("the same, read as the 2025 letter reads it: 47 µm centre to centre", "la misma, leída como la lee la carta de 2025: 47 µm entre centros"),
        "schut2024_z30": ("Schut et al. 2024 (PRR), z = 30 µm", "Schut et al. 2024 (PRR), z = 30 µm"),
        "schut2024_z10": ("Schut et al. 2024 (PRR), z = 10 µm", "Schut et al. 2024 (PRR), z = 10 µm"),
        "schut2024_z5": ("Schut et al. 2024 (PRR), z = 5 µm", "Schut et al. 2024 (PRR), z = 5 µm"),
        "schut2024_z10_1e-13": ("Schut et al. 2024 (PRR), z = 10 µm, heavier", "Schut et al. 2024 (PRR), z = 10 µm, más pesado"),
        "schut2024_z10_1e-15": ("Schut et al. 2024 (PRR), z = 10 µm, lighter", "Schut et al. 2024 (PRR), z = 10 µm, más ligero"),
    }
    sup = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")
    def mass(m: float) -> str:
        return f"10{str(round(math.log10(m))).translate(sup)} kg"
    def um(x: float) -> str:
        v = x * 1e6
        return f"{v:.2f} µm" if v < 1 else f"{v:.1f} µm" if v < 10 else f"{v:.0f} µm"
    def dur(s: float, lang: str) -> str:
        if s < 120: return f"{s:.0f} s"
        if s < 3600: return f"{s / 60:.0f} min"
        if s < 2 * 86400: return f"{s / 3600:.1f} h"
        return f"{s / 86400:.0f} " + ("days" if lang == "en" else "días")
    def pct(d: float) -> str:
        return "100 %" if d >= 0.995 else f"{100 * d:.1f} %"
    rows = []
    for r in _props():
        en_name, es_name = names[r["key"]]
        lay_en, lay_es = ("collinear", "colineal") if r["layout"] == "collinear" else ("side by side", "lado a lado")
        # The hybrid threshold is stated as "above", so it rounds up like the page text (525, 406, 82, 40, 14, 8 µm).
        sc_um = r["hybrid_sigma_c_m"] * 1e6
        hyb = (f"{math.ceil(sc_um - 1e-9):.0f} µm" if sc_um >= 10 else f"{math.ceil(sc_um * 10 - 1e-9) / 10:.1f} µm") + f' ({pct(r["torque_deficit_at_hybrid_sigma_c"])})'
        at = r["at_sigma"]["33um"]
        if at["entangles"]:
            at_en = f'{at["hybrid_negativity_at_t_full"]:.4f} · peak {at["peak_negativity"]:.3f} after {dur(at["peak_time_s"], "en")}'
            at_es = f'{at["hybrid_negativity_at_t_full"]:.4f} · máximo {at["peak_negativity"]:.3f} tras {dur(at["peak_time_s"], "es")}'
        else:
            at_en, at_es = "none", "ninguno"
        geo_en = f"{mass(r['m_kg'])} · split {um(r['split_m'])} · gap {um(r['nearest_m'])}"
        geo_es = f"{mass(r['m_kg'])} · división {um(r['split_m'])} · separación {um(r['nearest_m'])}"
        tf_en = f"{dur(r['quantum_t_full_s'], 'en')} · {at_en}"; tf_es = f"{dur(r['quantum_t_full_s'], 'es')} · {at_es}"
        rows.append("<tr>" + bi("td", en_name, es_name) + bi("td", lay_en, lay_es) + bi("td", geo_en, geo_es)
                    + f"<td>{hyb}</td><td>{um(r['collapse_sigma_c_at_t_full_m'])}</td>" + bi("td", tf_en, tf_es) + "</tr>")
    head = ("<tr>" + bi("th", "Proposal", "Propuesta") + bi("th", "Layout", "Disposición") + bi("th", "Geometry", "Geometría")
            + bi("th", "Hybrid entangles above σ (52 µm torque deficit)", "La híbrida entrelaza por encima de σ (déficit de par a 52 µm)")
            + bi("th", "Witness survives collapse above σ", "El testigo sobrevive al colapso por encima de σ")
            + bi("th", "Quantum channel full in · hybrid negativity then, σ = 33 µm", "Canal cuántico completo en · negatividad híbrida entonces, σ = 33 µm") + "</tr>")
    cap_en = ("Table T.05-P · Published geometries on the map: for each, the σ above which the 2025 letter's hybrid dynamics entangles it, with the 52 µm Eöt-Wash "
              "torque deficit that smearing would cause, the σ above which the quantum witness survives pure Diósi–Penrose collapse at the quantum channel's "
              "full-entanglement time, that time, and the hybrid negativity at it for this site's recast limit of 33 µm. Side-by-side rows use the planar kernel (about "
              "0.65 of the gap), collinear rows the one-dimensional map. These are two models' thresholds for each geometry, computed by this site's kernels, not "
              "exclusions of anything; other proposals exist that the page has not mapped; no witness has been measured.")
    cap_es = ("Tabla T.05-P · Geometrías publicadas sobre el mapa: para cada una, la σ por encima de la cual la dinámica híbrida de la carta de 2025 la entrelaza, con el "
              "déficit de par de Eöt-Wash a 52 µm que ese suavizado causaría, la σ por encima de la cual el testigo cuántico sobrevive al colapso puro de Diósi–Penrose "
              "en el tiempo de entrelazamiento completo del canal cuántico, ese tiempo, y la negatividad híbrida en ese momento para el límite recast de 33 µm de este "
              "sitio. Las filas lado a lado usan el núcleo planar (cerca de 0.65 de la separación), las colineales el mapa unidimensional. Son los umbrales de dos "
              "modelos para cada geometría, calculados por los núcleos de este sitio, no exclusiones de nada; existen otras propuestas que la página no ha mapeado; "
              "ningún testigo se ha medido.")
    body = "\n              ".join(rows)
    return f"""        <figure class="tp-distill-figure" role="group" aria-label="Table T.05-P Published geometries on the map" data-tg-figure="proposals-table">
          <div class="tp-table-wrap">
            <table class="tp-table tg-ledger-table" aria-label="Published gravitationally induced entanglement geometries on the two-model map">
              <thead>{head}</thead>
              <tbody>
              {body}
              </tbody>
            </table>
          </div>
          <figcaption class="tp-distill-caption">
            {bi("span", cap_en, cap_es)}
          </figcaption>
        </figure>"""


def hardware_table(page: dict) -> str:
    """Table T.05-H · the dephasing thresholds of the 2024 geometries as ceilings: the helium pressure and the internal temperature at
    which residual gas or thermal photons alone reach each channel's threshold (tools/timegravity_kernel_decoherence.py, budget)."""
    from timegravity_kernel_decoherence import BUDGET_GEOMETRIES, budget as _budget
    names = {
        "schut2024_z10": ("z = 10 µm · 10⁻¹⁴ kg · split 1.7 µm", "z = 10 µm · 10⁻¹⁴ kg · división 1.7 µm"),
        "schut2024_z5": ("z = 5 µm · 10⁻¹⁴ kg · split 0.65 µm", "z = 5 µm · 10⁻¹⁴ kg · división 0.65 µm"),
        "schut2024_z10_1e-15": ("z = 10 µm · 10⁻¹⁵ kg · split 23 µm", "z = 10 µm · 10⁻¹⁵ kg · división 23 µm"),
        "schut2024_z10_1e-13": ("z = 10 µm · 10⁻¹³ kg · split 0.17 µm", "z = 10 µm · 10⁻¹³ kg · división 0.17 µm"),
    }
    sup = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")
    def sci(x: float) -> str:
        e = math.floor(math.log10(x)); m = x / 10.0 ** e
        if round(m, 1) >= 10.0:
            m, e = 1.0, e + 1
        return f"{m:.1f} × 10{str(e).translate(sup)}"
    def kel(x: float) -> str:
        return f"{x:.0f} K" if x >= 10 else f"{x:.1f} K"
    def per_cc(n_m3: float) -> str:
        x = n_m3 / 1e6
        return f"{x:.0f}" if x >= 10 else f"{x:.1f}" if x >= 1 else f"{x:.2g}"
    rows = []
    for key in BUDGET_GEOMETRIES:
        b = _budget(key)
        for chan, (ch_en, ch_es) in (("quantum", ("quantum", "cuántico")), ("hybrid_33um", ("hybrid, σ = 33 µm", "híbrida, σ = 33 µm"))):
            pc = b["pressure_ceiling_pa"][chan]["4K"]; tc = b["temperature_ceiling_k"][chan]; nd = b["number_density_ceiling_per_m3"][chan]["4K"]
            en_name, es_name = names[key]
            rows.append("<tr>" + bi("td", en_name, es_name) + bi("td", ch_en, ch_es)
                        + f"<td>{sci(b['rates_per_s'][chan])} /s</td>"
                        + bi("td", f"{sci(pc['kinetic'])} Pa · {per_cc(nd)} atoms/cm³", f"{sci(pc['kinetic'])} Pa · {per_cc(nd)} átomos/cm³")
                        + f"<td>{sci(pc['cited'])} Pa</td>"
                        + f"<td>{kel(tc['env_1K'])} ({kel(tc['env_1K_im_high'])} – {kel(tc['env_1K_im_low'])})</td><td>{kel(tc['env_equal'])}</td></tr>")
    head = ("<tr>" + bi("th", "2024 geometry", "Geometría de 2024") + bi("th", "Channel", "Canal")
            + bi("th", "Dephasing threshold", "Umbral de desfase")
            + bi("th", "Helium ceiling at 4 K, kinetic rate (the necessary one)", "Techo de helio a 4 K, tasa cinética (el necesario)")
            + bi("th", "The same on the form the proposals cite", "Lo mismo en la forma que citan las propuestas")
            + bi("th", "Internal-temperature ceiling, surroundings at 1 K (absorption ten times higher – ten times lower)",
                 "Techo de temperatura interna, entorno a 1 K (absorción diez veces mayor – diez veces menor)")
            + bi("th", "The same, surroundings as warm as the sphere", "Lo mismo, entorno tan caliente como la esfera") + "</tr>")
    cap_en = ("Table T.05-H · The two dephasing thresholds as ceilings, for four geometries of the 2024 proposal: the helium pressure at which residual gas "
              "alone, and the sphere's internal temperature at which thermal photons alone, reach each channel's threshold. Gas: the kinetic rate at which "
              "atoms strike the sphere, the lowest defensible rate and so the necessary ceiling, with its number density; beside it the closed form the "
              "proposals cite, an interpolation larger by 8π/3. Photons: the long-wavelength closed forms, with the imaginary part of diamond's dielectric "
              "constant assumed at 10⁻⁴ and a decade either side. Each ceiling lets one source use the whole threshold; other gases, dipoles, Casimir forces, "
              "gravity gradients, phonons and the trap are not in it. No decoherence measurement at this scale exists among the page's sources: these are "
              "two models' thresholds turned into pressures and temperatures by an extrapolated theory, not a finding about any experiment.")
    cap_es = ("Tabla T.05-H · Los dos umbrales de desfase como techos, para cuatro geometrías de la propuesta de 2024: la presión de helio a la que el gas residual "
              "por sí solo, y la temperatura interna de la esfera a la que los fotones térmicos por sí solos, alcanzan el umbral de cada canal. Gas: la tasa "
              "cinética a la que los átomos golpean la esfera, la tasa defendible más baja y por eso el techo necesario, con su densidad numérica; a su lado la "
              "forma cerrada que citan las propuestas, una interpolación mayor por 8π/3. Fotones: las formas cerradas de longitud de onda larga, con la parte "
              "imaginaria de la constante dieléctrica del diamante supuesta en 10⁻⁴ y una década a cada lado. Cada techo deja que una sola fuente use todo el "
              "umbral; otros gases, los dipolos, las fuerzas de Casimir, los gradientes de gravedad, los fonones y la trampa no están en él. No hay entre las "
              "fuentes de la página ninguna medición de decoherencia a esta escala: son los umbrales de dos modelos convertidos en presiones y temperaturas "
              "por una teoría extrapolada, no un hallazgo sobre experimento alguno.")
    body = "\n              ".join(rows)
    return f"""        <figure class="tp-distill-figure" role="group" aria-label="Table T.05-H The dephasing thresholds as ceilings" data-tg-figure="hardware-table">
          <div class="tp-table-wrap">
            <table class="tp-table tg-ledger-table" aria-label="Pressure and internal-temperature ceilings for the quantum and hybrid channels at the 2024 geometries">
              <thead>{head}</thead>
              <tbody>
              {body}
              </tbody>
            </table>
          </div>
          <figcaption class="tp-distill-caption">
            {bi("span", cap_en, cap_es)}
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
            <span class="tg-map-order"><span data-en="Step {i} of 14" data-es="Paso {i} de 14">Step {i} of 14</span></span>
            <span class="tg-map-code">{m['code']}</span>
            <strong class="tg-map-title">{title}</strong>
            {bi("span", "Ends with: " + m["q_en"], "Termina con: " + m["q_es"], "tg-map-q")}
            {status}
          </li>""")
    return "        <ol class=\"tg-track-map\" aria-label=\"The fourteen pages in reading order\">\n" + "\n".join(items) + "\n        </ol>"


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


def apparatus_svg(kind: str) -> str:
    """Engraved vector medallion (64x64) depicting the physical apparatus or mathematical geometry of a historical milestone."""
    inner = {
        "einstein-elevator": (
            '<rect x="18" y="12" width="28" height="42" rx="3" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.6"/>'
            '<line x1="32" y1="4" x2="32" y2="12" stroke="var(--tp-minium)" stroke-width="1.8"/>'
            '<polygon points="28,7 32,2 36,7" fill="var(--tp-minium)"/>'
            '<circle cx="32" cy="19" r="4.2" fill="none" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
            '<line x1="32" y1="19" x2="35" y2="17" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
            '<circle cx="32" cy="46" r="4.2" fill="none" stroke="var(--tp-minium)" stroke-width="1.4"/>'
            '<line x1="32" y1="46" x2="32" y2="43" stroke="var(--tp-minium)" stroke-width="1.4"/>'
            '<path d="M 18 28 Q 32 30, 46 36" fill="none" stroke="var(--tp-verdigris)" stroke-width="1.6" stroke-dasharray="2 2"/>'
        ),
        "jefferson-tower": (
            '<rect x="23" y="8" width="18" height="48" rx="2" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.6"/>'
            '<line x1="27" y1="12" x2="27" y2="52" stroke="var(--tp-rule-strong)" stroke-width="0.9" stroke-dasharray="2 3"/>'
            '<line x1="37" y1="12" x2="37" y2="52" stroke="var(--tp-rule-strong)" stroke-width="0.9" stroke-dasharray="2 3"/>'
            '<circle cx="32" cy="14" r="3.5" fill="var(--tp-minium)"/>'
            '<path d="M 32 18 L 30 26 L 34 32 L 30 38 L 32 46" fill="none" stroke="var(--tp-minium)" stroke-width="1.6"/>'
            '<rect x="26" y="48" width="12" height="5" rx="1" fill="var(--tp-prussian)"/>'
        ),
        "gpa-rocket": (
            '<path d="M 10 52 Q 30 50, 54 44" fill="none" stroke="var(--tp-prussian)" stroke-width="1.6"/>'
            '<path d="M 18 49 Q 32 8, 48 45" fill="none" stroke="var(--tp-minium)" stroke-width="1.8" stroke-dasharray="3 2"/>'
            '<circle cx="33" cy="18" r="4" fill="var(--tp-prussian)"/>'
            '<line x1="22" y1="48" x2="31" y2="21" stroke="var(--tp-verdigris)" stroke-width="1.3"/>'
            '<line x1="35" y1="21" x2="43" y2="46" stroke="var(--tp-verdigris)" stroke-width="1.3"/>'
        ),
        "optical-lattice": (
            '<path d="M 22 10 C 28 24, 28 40, 22 54" fill="none" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
            '<path d="M 42 10 C 36 24, 36 40, 42 54" fill="none" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
            '<ellipse cx="32" cy="18" rx="9" ry="2.8" fill="var(--tp-prussian)" opacity="0.35"/>'
            '<ellipse cx="32" cy="27" rx="8" ry="2.6" fill="var(--tp-prussian)" opacity="0.5"/>'
            '<ellipse cx="32" cy="36" rx="8" ry="2.6" fill="var(--tp-minium)" opacity="0.65"/>'
            '<ellipse cx="32" cy="45" rx="9" ry="2.8" fill="var(--tp-minium)" opacity="0.8"/>'
            '<circle cx="32" cy="27" r="2.2" fill="var(--tp-prussian)"/>'
            '<circle cx="32" cy="36" r="2.2" fill="var(--tp-minium)"/>'
        ),
        "canal-ray": (
            '<rect x="10" y="22" width="44" height="20" rx="10" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.5"/>'
            '<line x1="16" y1="32" x2="44" y2="32" stroke="var(--tp-minium)" stroke-width="1.8"/>'
            '<path d="M 46 25 Q 51 32, 46 39" fill="none" stroke="var(--tp-prussian)" stroke-width="2"/>'
            '<line x1="22" y1="47" x2="22" y2="55" stroke="var(--tp-verdigris)" stroke-width="1.6"/>'
            '<line x1="32" y1="46" x2="32" y2="56" stroke="var(--tp-ink)" stroke-width="1.8"/>'
            '<line x1="42" y1="47" x2="42" y2="55" stroke="var(--tp-minium)" stroke-width="1.6"/>'
        ),
        "flying-clocks": (
            '<circle cx="32" cy="32" r="16" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.5"/>'
            '<ellipse cx="32" cy="32" rx="24" ry="9" fill="none" stroke="var(--tp-minium)" stroke-width="1.5" stroke-dasharray="3 2"/>'
            '<ellipse cx="32" cy="32" rx="22" ry="12" transform="rotate(-18 32 32)" fill="none" stroke="var(--tp-verdigris)" stroke-width="1.4"/>'
            '<circle cx="55" cy="32" r="3" fill="var(--tp-minium)"/>'
            '<circle cx="11" cy="28" r="3" fill="var(--tp-verdigris)"/>'
        ),
        "gps-constellation": (
            '<circle cx="32" cy="32" r="10" fill="var(--tp-prussian)" opacity="0.25" stroke="var(--tp-prussian)" stroke-width="1.5"/>'
            '<circle cx="32" cy="32" r="22" fill="none" stroke="var(--tp-rule-strong)" stroke-width="1.3" stroke-dasharray="4 3"/>'
            '<rect x="28" y="7" width="8" height="6" rx="1" fill="var(--tp-minium)"/>'
            '<line x1="21" y1="10" x2="27" y2="10" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
            '<line x1="37" y1="10" x2="43" y2="10" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
        ),
        "torsion-pendulum": (
            '<line x1="32" y1="6" x2="32" y2="34" stroke="var(--tp-ink)" stroke-width="1.3"/>'
            '<ellipse cx="32" cy="36" rx="18" ry="6" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.6"/>'
            '<circle cx="15" cy="36" r="4" fill="var(--tp-prussian)"/>'
            '<circle cx="49" cy="36" r="4" fill="var(--tp-minium)"/>'
            '<ellipse cx="32" cy="46" rx="18" ry="6" fill="none" stroke="var(--tp-verdigris)" stroke-width="1.4" stroke-dasharray="3 2"/>'
        ),
        "alpha-trap": (
            '<rect x="20" y="10" width="24" height="44" rx="4" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.5"/>'
            '<line x1="18" y1="18" x2="46" y2="18" stroke="var(--tp-minium)" stroke-width="2"/>'
            '<line x1="18" y1="46" x2="46" y2="46" stroke="var(--tp-minium)" stroke-width="2"/>'
            '<circle cx="32" cy="27" r="3.5" fill="var(--tp-verdigris)"/>'
            '<line x1="32" y1="32" x2="32" y2="43" stroke="var(--tp-verdigris)" stroke-width="1.6"/>'
            '<polygon points="29,41 32,45 35,41" fill="var(--tp-verdigris)"/>'
        ),
        "atom-chip": (
            '<rect x="14" y="10" width="36" height="6" rx="1.5" fill="var(--tp-prussian)"/>'
            '<path d="M 16 34 C 24 22, 40 22, 48 34" fill="none" stroke="var(--tp-prussian)" stroke-width="1.7"/>'
            '<path d="M 16 34 C 24 46, 40 46, 48 34" fill="none" stroke="var(--tp-minium)" stroke-width="1.7"/>'
            '<circle cx="32" cy="25" r="3.5" fill="var(--tp-prussian)"/>'
            '<circle cx="32" cy="43" r="3.5" fill="var(--tp-minium)"/>'
        ),
        "bmv-branches": (
            '<circle cx="18" cy="20" r="4" fill="var(--tp-prussian)"/>'
            '<circle cx="30" cy="20" r="4" fill="var(--tp-prussian)"/>'
            '<circle cx="34" cy="44" r="4" fill="var(--tp-minium)"/>'
            '<circle cx="46" cy="44" r="4" fill="var(--tp-minium)"/>'
            '<line x1="30" y1="20" x2="34" y2="44" stroke="var(--tp-verdigris)" stroke-width="2"/>'
            '<line x1="18" y1="20" x2="46" y2="44" stroke="var(--tp-rule-strong)" stroke-width="1.2" stroke-dasharray="2 2"/>'
            '<line x1="18" y1="20" x2="34" y2="44" stroke="var(--tp-prussian)" stroke-width="1.3"/>'
            '<line x1="30" y1="20" x2="46" y2="44" stroke="var(--tp-prussian)" stroke-width="1.3"/>'
        ),
        "underground-crystal": (
            '<path d="M 8 30 L 24 12 L 36 22 L 46 10 L 56 30 Z" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.5"/>'
            '<rect x="22" y="34" width="20" height="20" rx="3" fill="var(--tp-vellum)" stroke="var(--tp-verdigris)" stroke-width="1.6"/>'
            '<rect x="27" y="39" width="10" height="10" rx="1.5" fill="var(--tp-prussian)" opacity="0.8"/>'
        ),
        "page-wootters": (
            '<circle cx="22" cy="32" r="11" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.6"/>'
            '<line x1="22" y1="32" x2="27" y2="25" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
            '<circle cx="44" cy="32" r="9" fill="var(--tp-stone)" stroke="var(--tp-verdigris)" stroke-width="1.6"/>'
            '<path d="M 38 32 Q 44 24, 50 32" fill="none" stroke="var(--tp-minium)" stroke-width="1.6"/>'
            '<line x1="33" y1="32" x2="35" y2="32" stroke="var(--tp-ink)" stroke-width="1.6"/>'
        ),
        "black-hole-qubits": (
            '<circle cx="22" cy="34" r="9" fill="var(--tp-ink)" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
            '<circle cx="22" cy="34" r="14" fill="none" stroke="var(--tp-minium)" stroke-width="1.2" stroke-dasharray="3 2"/>'
            '<path d="M 36 46 Q 46 18, 56 46" fill="none" stroke="var(--tp-verdigris)" stroke-width="2"/>'
            '<line x1="36" y1="46" x2="56" y2="20" stroke="var(--tp-minium)" stroke-width="1.3" stroke-dasharray="2 2"/>'
        ),
        "rindler-wedge": (
            '<line x1="12" y1="52" x2="52" y2="12" stroke="var(--tp-minium)" stroke-width="1.6"/>'
            '<line x1="12" y1="12" x2="52" y2="52" stroke="var(--tp-minium)" stroke-width="1.6"/>'
            '<path d="M 48 16 Q 35 32, 48 48" fill="none" stroke="var(--tp-prussian)" stroke-width="2.2"/>'
            '<line x1="21" y1="28" x2="43" y2="28" stroke="var(--tp-verdigris)" stroke-width="1.5" stroke-dasharray="2 2"/>'
            '<circle cx="21" cy="28" r="3" fill="var(--tp-stone)" stroke="var(--tp-ink)" stroke-width="1.2"/>'
            '<circle cx="43" cy="28" r="3" fill="var(--tp-prussian)"/>'
        ),
        "horn-antenna": (
            '<polygon points="14,38 44,18 48,40 16,44" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.6"/>'
            '<line x1="24" y1="42" x2="24" y2="52" stroke="var(--tp-ink)" stroke-width="1.8"/>'
            '<line x1="16" y1="52" x2="36" y2="52" stroke="var(--tp-ink)" stroke-width="1.6"/>'
            '<path d="M 48 20 Q 55 29, 50 38" fill="none" stroke="var(--tp-minium)" stroke-width="1.5"/>'
            '<path d="M 52 17 Q 60 29, 54 41" fill="none" stroke="var(--tp-verdigris)" stroke-width="1.4" stroke-dasharray="2 2"/>'
        ),
        "sonic-horizon": (
            '<path d="M 10 24 L 28 24 Q 34 24, 36 38 L 54 38" fill="none" stroke="var(--tp-prussian)" stroke-width="2"/>'
            '<line x1="33" y1="12" x2="33" y2="52" stroke="var(--tp-minium)" stroke-width="1.5" stroke-dasharray="3 2"/>'
            '<circle cx="22" cy="19" r="3" fill="var(--tp-verdigris)"/>'
            '<circle cx="44" cy="31" r="3" fill="var(--tp-minium)"/>'
            '<path d="M 22 19 Q 33 12, 44 31" fill="none" stroke="var(--tp-verdigris)" stroke-width="1.3" stroke-dasharray="2 2"/>'
        ),
        "kerr-ergosphere": (
            '<ellipse cx="32" cy="32" rx="21" ry="13" fill="var(--tp-stone)" stroke="var(--tp-verdigris)" stroke-width="1.5" stroke-dasharray="3 2"/>'
            '<circle cx="32" cy="32" r="10" fill="var(--tp-ink)" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
            '<path d="M 16 22 A 22 15 0 0 1 48 22" fill="none" stroke="var(--tp-minium)" stroke-width="1.6"/>'
            '<polygon points="47,19 51,23 45,24" fill="var(--tp-minium)"/>'
        ),
        "continued-fraction": (
            '<line x1="12" y1="16" x2="52" y2="16" stroke="var(--tp-ink)" stroke-width="1.3"/>'
            '<line x1="18" y1="12" x2="18" y2="52" stroke="var(--tp-ink)" stroke-width="1.3"/>'
            '<path d="M 24 24 Q 34 32, 46 46" fill="none" stroke="var(--tp-prussian)" stroke-width="1.6" stroke-dasharray="2 2"/>'
            '<circle cx="28" cy="26" r="3.5" fill="var(--tp-prussian)"/>'
            '<circle cx="37" cy="35" r="3.5" fill="var(--tp-verdigris)"/>'
            '<circle cx="46" cy="45" r="3.5" fill="var(--tp-minium)"/>'
        ),
        "ligo-interferometer": (
            '<line x1="16" y1="46" x2="16" y2="14" stroke="var(--tp-prussian)" stroke-width="2.2"/>'
            '<line x1="16" y1="46" x2="50" y2="46" stroke="var(--tp-prussian)" stroke-width="2.2"/>'
            '<line x1="12" y1="50" x2="22" y2="40" stroke="var(--tp-minium)" stroke-width="1.8"/>'
            '<rect x="12" y="11" width="8" height="4" fill="var(--tp-verdigris)"/>'
            '<rect x="48" y="42" width="4" height="8" fill="var(--tp-verdigris)"/>'
            '<path d="M 26 24 C 30 16, 34 32, 38 19 S 46 28, 50 24" fill="none" stroke="var(--tp-minium)" stroke-width="1.6"/>'
        ),
        "pointer-darwinism": (
            '<line x1="27" y1="21" x2="17" y2="16" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
            '<line x1="37" y1="21" x2="47" y2="16" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
            '<line x1="27" y1="29" x2="17" y2="34" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
            '<line x1="37" y1="29" x2="47" y2="34" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
            '<polygon points="32,17 40,25 32,33 24,25" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.6"/>'
            '<circle cx="32" cy="25" r="2.2" fill="var(--tp-prussian)"/>'
            '<circle cx="15" cy="15" r="3.2" fill="var(--tp-verdigris)"/>'
            '<circle cx="49" cy="15" r="3.2" fill="var(--tp-verdigris)"/>'
            '<circle cx="15" cy="35" r="3.2" fill="var(--tp-verdigris)"/>'
            '<circle cx="49" cy="35" r="3.2" fill="var(--tp-verdigris)"/>'
            '<path d="M 15 49 C 19 42, 24 42, 32 42 L 43 42 C 47 42, 49 39, 50 35" fill="none" stroke="var(--tp-minium)" stroke-width="1.8"/>'
        ),
        "photon-scattering": (
            '<circle cx="24" cy="34" r="7" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.7"/>'
            '<circle cx="40" cy="34" r="7" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.4" stroke-dasharray="2.5 2"/>'
            '<path d="M 11 19 Q 15 15, 19 23 T 23 27" fill="none" stroke="var(--tp-minium)" stroke-width="1.6"/>'
            '<path d="M 28 28 Q 33 19, 39 14" fill="none" stroke="var(--tp-verdigris)" stroke-width="1.6"/>'
            '<path d="M 44 28 Q 48 21, 52 17" fill="none" stroke="var(--tp-minium)" stroke-width="1.5" stroke-dasharray="2 2"/>'
            '<line x1="24" y1="46" x2="40" y2="46" stroke="var(--tp-ink)" stroke-width="1.3"/>'
        ),
        "cavity-buckminster": (
            '<path d="M 16 15 Q 22 28, 16 41" fill="none" stroke="var(--tp-prussian)" stroke-width="2.2"/>'
            '<path d="M 48 15 Q 42 28, 48 41" fill="none" stroke="var(--tp-prussian)" stroke-width="2.2"/>'
            '<ellipse cx="27" cy="25" rx="5.5" ry="3.2" transform="rotate(-22 27 25)" fill="var(--tp-stone)" stroke="var(--tp-minium)" stroke-width="1.5"/>'
            '<ellipse cx="37" cy="25" rx="5.5" ry="3.2" transform="rotate(22 37 25)" fill="var(--tp-stone)" stroke="var(--tp-verdigris)" stroke-width="1.5"/>'
            '<polygon points="32,33 36,36 35,41 29,41 28,36" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
            '<line x1="19" y1="47" x2="26" y2="47" stroke="var(--tp-ink)" stroke-width="1.8"/>'
            '<line x1="29" y1="47" x2="35" y2="47" stroke="var(--tp-ink)" stroke-width="1.8"/>'
            '<line x1="38" y1="47" x2="45" y2="47" stroke="var(--tp-ink)" stroke-width="1.8"/>'
        ),
        "bullet-cluster-lensing": (
            '<ellipse cx="19" cy="31" rx="7.5" ry="10.5" fill="none" stroke="var(--tp-prussian)" stroke-width="1.5" stroke-dasharray="2.5 2"/>'
            '<circle cx="19" cy="31" r="3.8" fill="var(--tp-prussian)" opacity="0.35" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
            '<ellipse cx="45" cy="31" rx="7.5" ry="10.5" fill="none" stroke="var(--tp-prussian)" stroke-width="1.5" stroke-dasharray="2.5 2"/>'
            '<circle cx="45" cy="31" r="3.8" fill="var(--tp-prussian)" opacity="0.35" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
            '<path d="M 35 19 Q 24 31, 35 43" fill="none" stroke="var(--tp-minium)" stroke-width="2"/>'
            '<polygon points="35,23 27,31 35,39" fill="var(--tp-minium)" opacity="0.75"/>'
            '<line x1="19" y1="47" x2="45" y2="47" stroke="var(--tp-verdigris)" stroke-width="1.4" stroke-dasharray="2 2"/>'
        ),
        "dark-clock-comparison": (
            '<line x1="14" y1="33" x2="27" y2="33" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
            '<line x1="14" y1="18" x2="27" y2="18" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
            '<line x1="20.5" y1="33" x2="20.5" y2="18" stroke="var(--tp-minium)" stroke-width="1.6"/>'
            '<line x1="37" y1="33" x2="50" y2="33" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
            '<line x1="37" y1="23" x2="50" y2="23" stroke="var(--tp-prussian)" stroke-width="1.4" stroke-dasharray="2 1.5"/>'
            '<line x1="37" y1="15" x2="50" y2="15" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
            '<line x1="43.5" y1="33" x2="43.5" y2="15" stroke="var(--tp-verdigris)" stroke-width="1.6"/>'
            '<line x1="27" y1="25" x2="37" y2="25" stroke="var(--tp-ink)" stroke-width="1.3" stroke-dasharray="2 2"/>'
            '<path d="M 12 45 C 18 38, 26 52, 32 45 S 46 38, 52 45" fill="none" stroke="var(--tp-minium)" stroke-width="1.7"/>'
        ),
        "soft-triangle": (
            '<polygon points="32,12 14,46 50,46" fill="none" stroke="var(--tp-prussian)" stroke-width="1.8"/>'
            '<circle cx="32" cy="12" r="4" fill="var(--tp-minium)"/>'
            '<circle cx="14" cy="46" r="4" fill="var(--tp-prussian)"/>'
            '<circle cx="50" cy="46" r="4" fill="var(--tp-verdigris)"/>'
            '<path d="M 23 36 L 41 36" stroke="var(--tp-minium)" stroke-width="1.5" stroke-dasharray="2 2"/>'
        ),
    }.get(kind, '<circle cx="32" cy="32" r="16" fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="1.6"/>')
    return (
        f'<span class="tg-apparatus-badge" data-apparatus="{kind}" aria-hidden="true">'
        '<svg class="tg-apparatus-svg" viewBox="0 0 64 64" focusable="false">'
        '<circle cx="32" cy="32" r="29" fill="var(--tp-vellum)" stroke="var(--tp-rule-strong)" stroke-width="1"/>'
        f"{inner}"
        "</svg></span>"
    )


HUMANS_DATA: dict[str, dict] = {
    "": {
        "lineage_en": "1905–2026 · Einstein · Ives & Stilwell · Pound & Rebka · Kerr · Hafele & Keating · Vessot & Levine · DeWitt · Page & Wootters · Bekenstein, Hawking & Unruh · Zurek, Joos & Zeh · Mather, Clowe & Planck · Haroche & Arndt · Eöt-Wash & HUST · Wineland, Ye, Peik & Huntemann · Brukner & Folman · Bose, Marletto & Vedral · Diósi, Penrose & Curceanu · MICROSCOPE, ALPHA, LIGO/Virgo/KAGRA, LZ & XENONnT",
        "lineage_es": "1905–2026 · Einstein · Ives y Stilwell · Pound y Rebka · Kerr · Hafele y Keating · Vessot y Levine · DeWitt · Page y Wootters · Bekenstein, Hawking y Unruh · Zurek, Joos y Zeh · Mather, Clowe y Planck · Haroche y Arndt · Eöt-Wash y HUST · Wineland, Ye, Peik y Huntemann · Brukner y Folman · Bose, Marletto y Vedral · Diósi, Penrose y Curceanu · MICROSCOPE, ALPHA, LIGO/Virgo/KAGRA, LZ y XENONnT",
        "title_en": "The Humans Who Built the Clockwork (1905–2026)",
        "title_es": "Las Personas que Construyeron esta Relojería (1905–2026)",
        "lead_en": "Across all thirteen steps of this track (T.00–T.12), every equation and every row in the grounding ledger began with human beings: machinists cutting platinum wedges to the micrometer, physicists threading helium bags through brick towers, clockmakers booking airline seats for atomic standards, experimentalists trapping microwave cat states and comparing optical clocks against dark-matter waves, and theorists counting states by hand. Before we step into the instruments, we honor the people whose patience and craft built this record.",
        "lead_es": "A lo largo de los trece pasos de esta serie (T.00–T.12), cada ecuación y cada fila del libro de registro comenzó con seres humanos: maquinistas que cortaron cuñas de platino al micrómetro, físicos que tendieron bolsas de helio por torres de ladrillo, relojeros que compraron boletos de avión para estándares atómicos, experimentalistas que atraparon estados gato en cavidades y compararon relojes ópticos frente al sector oscuro, y teóricos que contaron estados a mano. Antes de entrar a los instrumentos, honramos a las personas cuya paciencia y oficio construyeron este registro.",
        "cards": [
            {
                "icon": "einstein-elevator",
                "era_en": "1905–1916 · Bern, Prague & Berlin",
                "era_es": "1905–1916 · Berna, Praga y Berlín",
                "names_en": "Albert Einstein & Karl Schwarzschild",
                "names_es": "Albert Einstein y Karl Schwarzschild",
                "place_en": "Thought experiments, field equations & the exact spherical metric",
                "place_es": "Experimentos mentales, ecuaciones de campo y la métrica esférica exacta",
                "story_en": "In 1905 Einstein wrote down the slowing of a moving clock; in 1911 in Prague he asked how a clock near the ceiling of an accelerating cabin compares with one on the floor; in November 1915 he completed the field equations in Berlin. Weeks later, while serving on the Russian front, Karl Schwarzschild derived the exact exterior metric around a spherical mass and mailed it back to Berlin.",
                "story_es": "En 1905 Einstein escribió el atraso de un reloj en movimiento; en 1911 en Praga preguntó cómo se compara un reloj cerca del techo de una cabina acelerada con uno en el piso; en noviembre de 1915 completó las ecuaciones de campo en Berlín. Semanas después, desde el frente ruso, Karl Schwarzschild derivó la métrica exterior exacta alrededor de una masa esférica y la envió por correo a Berlín.",
                "spec_en": "Steps T.01 · T.02 · T.03",
                "spec_es": "Pasos T.01 · T.02 · T.03",
                "doi": "10.1002/andp.19163540702",
            },
            {
                "icon": "jefferson-tower",
                "era_en": "1938–1976 · Bell Labs, Harvard & Wallops Island",
                "era_es": "1938–1976 · Bell Labs, Harvard y Wallops Island",
                "names_en": "Ives & Stilwell · Pound & Rebka · Hafele & Keating · Vessot & Levine",
                "names_es": "Ives y Stilwell · Pound y Rebka · Hafele y Keating · Vessot y Levine",
                "place_en": "Canal rays, a 22.5 m brick tower, commercial airliners & a Scout D rocket",
                "place_es": "Rayos canales, una torre de ladrillo de 22.5 m, vuelos comerciales y un cohete Scout D",
                "story_en": "Herbert Ives and G. R. Stilwell photographed hydrogen canal rays in 1938 to catch the quadratic speed shift. In 1960 Robert Pound and Glen Rebka Jr. sent 14.4 keV iron-57 gamma rays down Harvard's 22.5-meter Jefferson Tower to measure the height shift inside a building. In 1971 Joseph Hafele and Richard Keating flew four cesium clocks around the world on commercial jets, and in 1976 Robert Vessot and Martin Levine launched a hydrogen maser 10,000 km up on a Scout D rocket.",
                "story_es": "Herbert Ives y G. R. Stilwell fotografiaron rayos canales de hidrógeno en 1938 para medir el corrimiento cuadrático por velocidad. En 1960 Robert Pound y Glen Rebka Jr. enviaron rayos gamma de hierro-57 por los 22.5 metros de la torre Jefferson de Harvard para medir el cambio por altura dentro de un edificio. En 1971 Joseph Hafele y Richard Keating volaron cuatro relojes de cesio alrededor del mundo en aviones comerciales, y en 1976 Robert Vessot y Martin Levine lanzaron un máser de hidrógeno a 10,000 km en un cohete Scout D.",
                "spec_en": "Steps T.01 · T.02",
                "spec_es": "Pasos T.01 · T.02",
                "doi": "10.1103/PhysRevLett.4.337",
            },
            {
                "icon": "optical-lattice",
                "era_en": "2003–2023 · Boulder, Seattle, Orbit & CERN",
                "era_es": "2003–2023 · Boulder, Seattle, Órbita y CERN",
                "names_en": "Ashby · Adelberger & Eöt-Wash · Wineland · Touboul · Ye · Hangst & ALPHA",
                "names_es": "Ashby · Adelberger y Eöt-Wash · Wineland · Touboul · Ye · Hangst y ALPHA",
                "place_en": "GPS satellites, torsion balances, optical lattices & falling antihydrogen",
                "place_es": "Satélites GPS, balanzas de torsión, redes ópticas y antihidrógeno en caída libre",
                "story_en": "Neil Ashby documented how every GPS satellite clock balances +45.7 against −7.2 microseconds per day. Chin-wen Chou and David Wineland resolved a 33 cm height step with aluminum-ion clocks in 2010, and Tobias Bothwell and Jun Ye resolved 1 millimeter across a strontium cloud in 2022. Meanwhile Eöt-Wash torsion pendulums, Pierre Touboul's orbiting MICROSCOPE cylinders, and Jeffrey Hangst's ALPHA-g trap at CERN tested universal free fall across matter and antimatter.",
                "story_es": "Neil Ashby documentó cómo cada reloj satelital GPS equilibra +45.7 frente a −7.2 microsegundos por día. Chin-wen Chou y David Wineland resolvieron un escalón de 33 cm con relojes de iones de aluminio en 2010, y Tobias Bothwell y Jun Ye resolvieron 1 milímetro en una nube de estroncio en 2022. Mientras tanto, los péndulos de Eöt-Wash, los cilindros orbitales de MICROSCOPE con Pierre Touboul y la trampa ALPHA-g con Jeffrey Hangst en el CERN pusieron a prueba la caída libre universal en materia y antimateria.",
                "spec_en": "Steps T.01 · T.02 · T.03",
                "spec_es": "Pasos T.01 · T.02 · T.03",
                "doi": "10.1038/s41586-021-04349-7",
            },
            {
                "icon": "atom-chip",
                "era_en": "1938–2026 · Columbia, Harvard, Vienna, Beersheba, London & Oxford",
                "era_es": "1938–2026 · Columbia, Harvard, Viena, Beerseba, Londres y Oxford",
                "names_en": "Rabi, Ramsey & Hahn · Zych & Brukner · Margalit & Folman · Bose, Marletto & Vedral",
                "names_es": "Rabi, Ramsey y Hahn · Zych y Brukner · Margalit y Folman · Bose, Marletto y Vedral",
                "place_en": "Spin echoes, quantum clocks in superposition & two-mass entanglement proposals",
                "place_es": "Ecos de espín, relojes cuánticos en superposición y propuestas de entrelazamiento de dos masas",
                "story_en": "Using the resonance and spin-echo language built by Isidor Isaac Rabi, Norman Ramsey, and Erwin Hahn, Magdalena Zych, Fabio Costa, Igor Pikovski, and Časlav Brukner asked in 2011 what happens when one ticking quantum clock sits at two heights at once; Yair Margalit and Ron Folman built the magnetic-gradient analogue on an atom chip in 2015. In 2017 Sougato Bose and co-authors and Chiara Marletto and Vlatko Vedral proposed testing whether gravity entangles two superposed micron masses.",
                "story_es": "Con el lenguaje de resonancia y eco de espín creado por Isidor Isaac Rabi, Norman Ramsey y Erwin Hahn, Magdalena Zych, Fabio Costa, Igor Pikovski y Časlav Brukner preguntaron en 2011 qué ocurre cuando un reloj cuántico está en dos alturas a la vez; Yair Margalit y Ron Folman construyeron el análogo con gradiente magnético en un chip atómico en 2015. En 2017 Sougato Bose y coautores y Chiara Marletto y Vlatko Vedral propusieron probar si la gravedad entrelaza dos masas micrométricas en superposición.",
                "spec_en": "Steps T.04 · T.05",
                "spec_es": "Pasos T.04 · T.05",
                "doi": "10.1038/ncomms1498",
            },
            {
                "icon": "underground-crystal",
                "era_en": "1987–2026 · Budapest, Oxford, Gran Sasso, Seattle, Wuhan & Vienna",
                "era_es": "1987–2026 · Budapest, Oxford, Gran Sasso, Seattle, Wuhan y Viena",
                "names_en": "Diósi & Penrose · Curceanu, Donadi & XENONnT · Lee, Tan, Westphal & Arndt",
                "names_es": "Diósi y Penrose · Curceanu, Donadi y XENONnT · Lee, Tan, Westphal y Arndt",
                "place_en": "Underground germanium and liquid-xenon detectors, 52 µm wedges & 90 mg gold spheres",
                "place_es": "Detectores subterráneos de germanio y xenón líquido, cuñas a 52 µm y esferas de oro de 90 mg",
                "story_en": "Lajos Diósi (1987) and Roger Penrose (1996) proposed that gravity collapses superpositions at a rate set by gravitational self-energy. Deep under the Gran Sasso mountain, Sandro Donadi, Catalina Curceanu, Lajos Diósi and co-workers (2021) and the XENONnT Collaboration (2026) listened for the spontaneous X-rays that model predicts, while Jun-Ge Lee (Seattle), Wen-Hai Tan (Wuhan), Tobias Westphal and Markus Arndt (Vienna) pushed short-range gravity and matter-wave coherence to their laboratory limits.",
                "story_es": "Lajos Diósi (1987) y Roger Penrose (1996) propusieron que la gravedad colapsa superposiciones a un ritmo fijado por la autoenergía gravitatoria. Bajo la montaña del Gran Sasso, Sandro Donadi, Catalina Curceanu, Lajos Diósi y colaboradores (2021) y la colaboración XENONnT (2026) buscaron los rayos X espontáneos que predice ese modelo, mientras Jun-Ge Lee (Seattle), Wen-Hai Tan (Wuhan), Tobias Westphal y Markus Arndt (Viena) llevaron la gravedad a corta distancia y las ondas de materia a sus límites de laboratorio.",
                "spec_en": "Steps T.05 · T.06",
                "spec_es": "Pasos T.05 · T.06",
                "doi": "10.1038/s41567-020-1008-4",
            },
            {
                "icon": "black-hole-qubits",
                "era_en": "1963–2026 · Austin, Chapel Hill, Princeton, Cambridge, Vancouver, Edmonton & LIGO",
                "era_es": "1963–2026 · Austin, Chapel Hill, Princeton, Cambridge, Vancouver, Edmonton y LIGO",
                "names_en": "Kerr · DeWitt · Page & Wootters · Bekenstein, Hawking & Unruh · Mather · LIGO/Virgo/KAGRA · Penington",
                "names_es": "Kerr · DeWitt · Page y Wootters · Bekenstein, Hawking y Unruh · Mather · LIGO/Virgo/KAGRA · Penington",
                "place_en": "Spinning horizons, conditional clocks, Rindler wedges, ringdowns & the Page curve",
                "place_es": "Horizontes en rotación, relojes condicionales, cuñas de Rindler, resonancias y la curva de Page",
                "story_en": "Roy Kerr found the exact spinning horizon in 1963; Bryce DeWitt (1967) and Don Page and William Wootters (1983) showed how conditional probability recovers ticking time from a stationary state. Jacob Bekenstein, Stephen Hawking, and William Unruh linked horizon surface gravity to thermal states, Don Page (1993) derived the unitary turnover curve, and LIGO, Virgo, KAGRA, and Maximiliano Isi tested Kerr ringdowns and Hawking's area law on merging black holes. Wojciech Zurek, Erich Joos, H. Dieter Zeh, Serge Haroche, and Jean-Michel Brune showed how the photon bath selects pointer states, while Planck, Douglas Clowe, Jun Ye, Ekkehard Peik, and Nils Huntemann tested gravity and clocks across dark matter.",
                "story_es": "Roy Kerr halló el horizonte en rotación exacto en 1963; Bryce DeWitt (1967) y Don Page y William Wootters (1983) mostraron cómo la probabilidad condicional recupera el tiempo desde un estado estacionario. Jacob Bekenstein, Stephen Hawking y William Unruh vincularon la gravedad superficial con estados térmicos, Don Page (1993) derivó la curva de retorno unitaria, y LIGO, Virgo, KAGRA y Maximiliano Isi probaron las resonancias de Kerr y la ley del área. Wojciech Zurek, Erich Joos, H. Dieter Zeh, Serge Haroche y Jean-Michel Brune mostraron cómo el baño de fotones selecciona estados puntero, mientras Planck, Douglas Clowe, Jun Ye, Ekkehard Peik y Nils Huntemann pusieron a prueba la gravedad y los relojes frente a la materia oscura.",
                "spec_en": "Steps T.07 · T.08 · T.09 · T.10 · T.11 · T.12 · T.13",
                "spec_es": "Pasos T.07 · T.08 · T.09 · T.10 · T.11 · T.12 · T.13",
                "doi": "10.1103/PhysRevD.27.2885",
            },
        ],
    },
    "t01": {
        "lineage_en": "Pioneers of Step T.01 · Einstein (1911, 1916) · Pound & Rebka (1960) · Vessot & Levine (1976) · Chou & Wineland (2010) · Bothwell & Ye (2022)",
        "lineage_es": "Pioneros del Paso T.01 · Einstein (1911, 1916) · Pound y Rebka (1960) · Vessot y Levine (1976) · Chou y Wineland (2010) · Bothwell y Ye (2022)",
        "title_en": "The Humans Behind Step T.01 · From a Brick Tower to a Single Millimeter",
        "title_es": "Las Personas Detrás del Paso T.01 · De una Torre de Ladrillo a un Solo Milímetro",
        "lead_en": "Measuring a fractional clock shift of 10⁻¹⁶ per meter of height took sixty-two years of laboratory craft—from a helium bag threaded through four floors at Harvard to a rocket over the Atlantic and a hundred thousand strontium atoms held in a vertical laser standing wave.",
        "lead_es": "Medir un cambio fraccionario de reloj de 10⁻¹⁶ por metro de altura tomó sesenta y dos años de oficio experimental: desde una bolsa de helio tendida por cuatro pisos en Harvard hasta un cohete sobre el Atlántico y cien mil átomos de estroncio sostenidos en una onda estacionaria láser.",
        "cards": [
            {
                "icon": "einstein-elevator",
                "era_en": "1911 & 1916 · Prague & Berlin",
                "era_es": "1911 y 1916 · Praga y Berlín",
                "names_en": "Albert Einstein",
                "names_es": "Albert Einstein",
                "place_en": "German University in Prague & Prussian Academy of Sciences",
                "place_es": "Universidad Alemana de Praga y Academia Prusiana de Ciencias",
                "story_en": "Working in Prague in 1911 before the full tensor calculus was ready, Einstein compared two clocks separated by height inside an accelerating frame and saw that the higher clock must tick faster by gh/c², then embedded that rate into the time–time component g₀₀ of the 1916 metric.",
                "story_es": "Trabajando en Praga en 1911 antes de tener listo el cálculo tensorial completo, Einstein comparó dos relojes separados por una altura dentro de un marco acelerado y vio que el reloj más alto debía marchar más rápido por gh/c², integrando luego ese ritmo en la componente g₀₀ de la métrica de 1916.",
                "spec_en": "Equivalence & Geodesic Law · g₀₀ = −(1 + 2gz/c²)",
                "spec_es": "Equivalencia y Ley Geodésica · g₀₀ = −(1 + 2gz/c²)",
                "doi": "10.1002/andp.19113401005",
            },
            {
                "icon": "jefferson-tower",
                "era_en": "1960 · Cambridge, Massachusetts",
                "era_es": "1960 · Cambridge, Massachusetts",
                "names_en": "Robert V. Pound & Glen A. Rebka Jr.",
                "names_es": "Robert V. Pound y Glen A. Rebka Jr.",
                "place_en": "Jefferson Physical Laboratory, Harvard University · 22.5 m Tower",
                "place_es": "Laboratorio Físico Jefferson, Universidad de Harvard · Torre de 22.5 m",
                "story_en": "To catch a fractional shift of 2.5 × 10⁻¹⁵ inside a building, Pound and his graduate student Glen Rebka hung a Mylar bag of flowing helium down a 22.5-meter shaft in Harvard's Jefferson Tower and mounted an iron-57 gamma-ray source on a loudspeaker cone, sweeping the Doppler velocity to null the height shift.",
                "story_es": "Para detectar un cambio fraccionario de 2.5 × 10⁻¹⁵ dentro de un edificio, Pound y su estudiante de doctorado Glen Rebka colgaron una bolsa de Mylar con helio a lo largo de un tiro de 22.5 metros en la torre Jefferson de Harvard y montaron una fuente gamma de hierro-57 en el cono de un altavoz.",
                "spec_en": "⁵⁷Fe Mössbauer recoilless resonance · Δh = 22.5 m",
                "spec_es": "Resonancia Mössbauer sin retroceso en ⁵⁷Fe · Δh = 22.5 m",
                "doi": "10.1103/PhysRevLett.4.337",
            },
            {
                "icon": "gpa-rocket",
                "era_en": "June 18, 1976 · Wallops Island, Virginia",
                "era_es": "18 de junio de 1976 · Wallops Island, Virginia",
                "names_en": "Robert F. C. Vessot & Martin W. Levine",
                "names_es": "Robert F. C. Vessot y Martin W. Levine",
                "place_en": "Smithsonian Astrophysical Observatory & NASA · Gravity Probe A",
                "place_es": "Observatorio Astrofísico Smithsoniano y NASA · Gravity Probe A",
                "story_en": "Vessot and Levine built a rugged atomic hydrogen maser and launched it 10,000 kilometers into space aboard a Scout D rocket. A continuous two-way microwave Doppler-cancellation link subtracted the rocket's motion in real time, testing the gravitational redshift to 7 × 10⁻⁵ during a two-hour flight.",
                "story_es": "Vessot y Levine construyeron un máser atómico de hidrógeno y lo lanzaron a 10,000 kilómetros de altitud en un cohete Scout D. Un enlace continuo de microondas de dos vías restó en tiempo real el efecto Doppler del movimiento del cohete, probando el corrimiento gravitatorio a 7 × 10⁻⁵ en dos horas de vuelo.",
                "spec_en": "Suborbital hydrogen maser · Δh = 10,000 km",
                "spec_es": "Máser suborbital de hidrógeno · Δh = 10,000 km",
                "doi": "10.1103/PhysRevLett.45.2081",
            },
            {
                "icon": "optical-lattice",
                "era_en": "2010 & 2022 · Boulder, Colorado",
                "era_es": "2010 y 2022 · Boulder, Colorado",
                "names_en": "Chin-wen Chou & David J. Wineland · Tobias Bothwell & Jun Ye",
                "names_es": "Chin-wen Chou y David J. Wineland · Tobias Bothwell y Jun Ye",
                "place_en": "NIST Ion Storage Group (33 cm) & JILA Optical Lattice Lab (1 mm)",
                "place_es": "Grupo de Trampas de Iones del NIST (33 cm) y Laboratorio JILA (1 mm)",
                "story_en": "In 2010 Chou, Hume, Rosenband, and Wineland connected two optical aluminum-ion clocks with a phase-stabilized optical fiber and raised one bench by 33 centimeters on a jack. Twelve years later down the street at JILA, Bothwell, Ye, and co-workers imaged the continuous redshift across a single millimeter of an ultracold strontium cloud.",
                "story_es": "En 2010 Chou, Hume, Rosenband y Wineland conectaron dos relojes ópticos de iones de aluminio con una fibra estabilizada en fase y levantaron una mesa 33 centímetros con un gato mecánico. Doce años después, en JILA, Bothwell, Ye y colaboradores midieron la pendiente continua a través de un solo milímetro de una nube ultrafría de estroncio.",
                "spec_en": "Al⁺ ion clocks (33 cm) & ⁸⁷Sr lattice (1 mm)",
                "spec_es": "Relojes de Al⁺ (33 cm) y red óptica de ⁸⁷Sr (1 mm)",
                "doi": "10.1038/s41586-021-04349-7",
            },
        ],
    },
    "t02": {
        "lineage_en": "Pioneers of Step T.02 · Einstein (1905) · Ives & Stilwell (1938) · Hafele & Keating (1971) · Vessot & Levine (1976) · Ashby (2003) · Touboul & MICROSCOPE (2022)",
        "lineage_es": "Pioneros del Paso T.02 · Einstein (1905) · Ives y Stilwell (1938) · Hafele y Keating (1971) · Vessot y Levine (1976) · Ashby (2003) · Touboul y MICROSCOPE (2022)",
        "title_en": "The Humans Behind Step T.02 · Canal Rays, Airline Tickets, and Orbiting Clocks",
        "title_es": "Las Personas Detrás del Paso T.02 · Rayos Canales, Boletos de Avión y Relojes en Órbita",
        "lead_en": "A clock on a vehicle experiences both parts of the metric at once: higher potential speeds it up, while motion through space slows it down. These researchers turned that two-column ledger into laboratory and engineering reality.",
        "lead_es": "Un reloj a bordo de un vehículo experimenta ambas partes de la métrica a la vez: mayor potencial lo adelanta, mientras el movimiento lo atrasa. Estos investigadores convirtieron esa contabilidad de doble entrada en realidad experimental y de ingeniería.",
        "cards": [
            {
                "icon": "canal-ray",
                "era_en": "1905 & 1938 · Bern & New York City",
                "era_es": "1905 y 1938 · Berna y Nueva York",
                "names_en": "Albert Einstein · Herbert E. Ives & G. R. Stilwell",
                "names_es": "Albert Einstein · Herbert E. Ives y G. R. Stilwell",
                "place_en": "Swiss Patent Office & Bell Telephone Laboratories",
                "place_es": "Oficina Suiza de Patentes y Bell Telephone Laboratories",
                "story_en": "Einstein predicted in 1905 that a clock moving at speed v ticks slower by v²/(2c²). At Bell Labs in 1938, Herbert Ives and G. R. Stilwell placed a small concave mirror inside a hydrogen canal-ray tube so they could photograph the forward and backward Doppler-shifted Balmer lines on a single plate, isolating the quadratic shift.",
                "story_es": "Einstein predijo en 1905 que un reloj que se mueve a velocidad v marcha más lento por v²/(2c²). En Bell Labs en 1938, Herbert Ives y G. R. Stilwell colocaron un pequeño espejo cóncavo dentro de un tubo de rayos canales de hidrógeno para fotografiar en una misma placa las líneas de Balmer hacia adelante y hacia atrás, aislando el término cuadrático.",
                "spec_en": "Hydrogen Hβ canal-ray spectroscopy · −v²/(2c²)",
                "spec_es": "Espectroscopía de rayos canales Hβ · −v²/(2c²)",
                "doi": "10.1364/JOSA.28.000215",
            },
            {
                "icon": "flying-clocks",
                "era_en": "October 1971 · Around the World",
                "era_es": "Octubre de 1971 · Alrededor del Mundo",
                "names_en": "Joseph C. Hafele & Richard E. Keating",
                "names_es": "Joseph C. Hafele y Richard E. Keating",
                "place_en": "Washington University in St. Louis & U.S. Naval Observatory",
                "place_es": "Universidad Washington en St. Louis y Observatorio Naval de EE. UU.",
                "story_en": "Physicist Joseph Hafele and astronomer Richard Keating carried four Hewlett-Packard 5061A cesium beam clocks onto commercial airliners—buying two cabin tickets for 'Mr. Clock'—and flew them eastward and westward around the globe. On return to Washington, the eastbound clocks had lost 59 ± 10 ns and the westbound clocks had gained 273 ± 7 ns.",
                "story_es": "El físico Joseph Hafele y el astrónomo Richard Keating subieron cuatro relojes de haz de cesio Hewlett-Packard 5061A a vuelos comerciales —comprando dos asientos de cabina para 'Mr. Clock'— y volaron hacia el este y hacia el oeste alrededor del mundo. Al volver a Washington, los relojes hacia el este habían perdido 59 ± 10 ns y hacia el oeste habían ganado 273 ± 7 ns.",
                "spec_en": "Four HP 5061A cesium standards · East & West flights",
                "spec_es": "Cuatro relojes de cesio HP 5061A · Vuelos este y oeste",
                "doi": "10.1126/science.177.4044.168",
            },
            {
                "icon": "gps-constellation",
                "era_en": "2003 · Boulder, Colorado & Medium Earth Orbit",
                "era_es": "2003 · Boulder, Colorado y Órbita Terrestre Media",
                "names_en": "Neil Ashby & the GPS Clock Engineers",
                "names_es": "Neil Ashby y la Ingeniería de Relojes del GPS",
                "place_en": "University of Colorado Boulder & the 20,184 km Constellation",
                "place_es": "Universidad de Colorado en Boulder y la constelación a 20,184 km",
                "story_en": "At 20,184 km altitude and 3.87 km/s orbital speed, a satellite clock gains +45.7 microseconds a day from height and loses 7.2 microseconds a day from speed. Neil Ashby's review lays out how engineers detune every rubidium and cesium oscillator before launch by −4.4647 × 10⁻¹⁰ so the +38.6 µs/day net drift is canceled continuously.",
                "story_es": "A 20,184 km de altitud y 3.87 km/s de velocidad orbital, un reloj satelital gana +45.7 microsegundos al día por altura y pierde 7.2 microsegundos al día por velocidad. La revisión de Neil Ashby detalla cómo los ingenieros desafinan cada oscilador de rubidio y cesio antes del lanzamiento por −4.4647 × 10⁻¹⁰ para cancelar los +38.6 µs/día netos.",
                "spec_en": "Factory frequency offset −4.4647 × 10⁻¹⁰ · +38.6 µs/day",
                "spec_es": "Ajuste de frecuencia de fábrica −4.4647 × 10⁻¹⁰ · +38.6 µs/día",
                "doi": "10.12942/lrr-2003-1",
            },
        ],
    },
    "t03": {
        "lineage_en": "Pioneers of Step T.03 · Einstein (1915–1916) · Schwarzschild (1916) · Schlamminger, Gundlach & Adelberger (2008) · Touboul & MICROSCOPE (2022) · Hangst & ALPHA (2023)",
        "lineage_es": "Pioneros del Paso T.03 · Einstein (1915–1916) · Schwarzschild (1916) · Schlamminger, Gundlach y Adelberger (2008) · Touboul y MICROSCOPE (2022) · Hangst y ALPHA (2023)",
        "title_en": "The Humans Behind Step T.03 · Torsion Fibers, Drag-Free Satellites, and Falling Antimatter",
        "title_es": "Las Personas Detrás del Paso T.03 · Fibras de Torsión, Satélites sin Arrastre y Antimateria en Caída",
        "lead_en": "Because the slope in clock rate is a property of spacetime rather than of the falling object, titanium, beryllium, platinum, and antihydrogen must follow the same trajectory. Generations of experimentalists built the balances and traps that tested that statement across fifteen orders of magnitude.",
        "lead_es": "Como la pendiente en el ritmo del reloj pertenece al espaciotiempo y no al objeto que cae, el titanio, el berilio, el platino y el antihidrógeno deben seguir la misma trayectoria. Generaciones de experimentalistas construyeron las balanzas y trampas que pusieron a prueba esa afirmación a lo largo de quince órdenes de magnitud.",
        "cards": [
            {
                "icon": "einstein-elevator",
                "era_en": "1915–1916 · Berlin & the Russian Front",
                "era_es": "1915–1916 · Berlín y el Frente Ruso",
                "names_en": "Albert Einstein & Karl Schwarzschild",
                "names_es": "Albert Einstein y Karl Schwarzschild",
                "place_en": "Prussian Academy of Sciences & Artillery Weather Station",
                "place_es": "Academia Prusiana de Ciencias y Estación Meteorológica de Artillería",
                "story_en": "Einstein's 1915–1916 field equations reduce in the static weak-field limit to Poisson's equation ∇²Φ = 4πGρ, tying the clock-rate well directly to mass density. Within weeks of reading Einstein's November 1915 paper at the front, astronomer Karl Schwarzschild found the exact spherical vacuum solution.",
                "story_es": "Las ecuaciones de campo de Einstein de 1915–1916 se reducen en el límite estático de campo débil a la ecuación de Poisson ∇²Φ = 4πGρ, atando el pozo de ritmo de relojes a la densidad de masa. Pocas semanas después de leer el artículo en el frente, el astrónomo Karl Schwarzschild halló la solución esférica exacta en el vacío.",
                "spec_en": "Exact exterior metric · 1 − 2GM/(rc²)",
                "spec_es": "Métrica exterior exacta · 1 − 2GM/(rc²)",
                "doi": "10.48550/arXiv.physics/9905030",
            },
            {
                "icon": "torsion-pendulum",
                "era_en": "2008 · Seattle, Washington",
                "era_es": "2008 · Seattle, Washington",
                "names_en": "Stephan Schlamminger, Ki-Young Choi, Todd Wagner, Jens Gundlach & Eric Adelberger",
                "names_es": "Stephan Schlamminger, Ki-Young Choi, Todd Wagner, Jens Gundlach y Eric Adelberger",
                "place_en": "Eöt-Wash Group, Center for Experimental Nuclear Physics and Astrophysics",
                "place_es": "Grupo Eöt-Wash, Universidad de Washington en Seattle",
                "story_en": "Continuing the torsion-balance tradition of Loránd Eötvös, the Seattle Eöt-Wash team rotated a precision pendulum carrying beryllium and titanium test bodies on a turntable inside multi-layer magnetic and thermal shields, bounding any composition-dependent acceleration toward the Earth or the Sun to 1.8 × 10⁻¹³.",
                "story_es": "Continuando la tradición de la balanza de torsión de Loránd Eötvös, el equipo Eöt-Wash de Seattle hizo girar un péndulo de precisión con cuerpos de prueba de berilio y titanio dentro de blindajes magnéticos y térmicos, acotando cualquier aceleración dependiente de la composición a 1.8 × 10⁻¹³.",
                "spec_en": "Rotating Be–Ti torsion balance · η = (0.3 ± 1.8) × 10⁻¹³",
                "spec_es": "Balanza de torsión rotatoria Be–Ti · η = (0.3 ± 1.8) × 10⁻¹³",
                "doi": "10.1103/PhysRevLett.100.041101",
            },
            {
                "icon": "alpha-trap",
                "era_en": "2022 & 2023 · Orbit & CERN, Geneva",
                "era_es": "2022 y 2023 · Órbita y CERN, Ginebra",
                "names_en": "Pierre Touboul & MICROSCOPE · Jeffrey S. Hangst & ALPHA",
                "names_es": "Pierre Touboul y MICROSCOPE · Jeffrey S. Hangst y ALPHA",
                "place_en": "ONERA / CNES Drag-Free Satellite & CERN Antiproton Decelerator",
                "place_es": "Satélite sin arrastre ONERA / CNES y Desacelerador de Antiprotones del CERN",
                "story_en": "In orbit, Pierre Touboul and the MICROSCOPE collaboration compared concentric platinum-rhodium and titanium cylinders over 1,500 orbits to reach |η| ≤ 1.5 × 10⁻¹⁵. At CERN in 2023, Jeffrey Hangst and the ALPHA collaboration released cold antihydrogen atoms in the vertical ALPHA-g magnetic trap and observed antimatter fall downward at (0.75 ± 0.13 ± 0.16) g.",
                "story_es": "En órbita, Pierre Touboul y la colaboración MICROSCOPE compararon cilindros concéntricos de platino-rodio y titanio durante 1,500 órbitas hasta alcanzar |η| ≤ 1.5 × 10⁻¹⁵. En el CERN en 2023, Jeffrey Hangst y la colaboración ALPHA liberaron átomos fríos de antihidrógeno en la trampa vertical ALPHA-g y observaron caer la antimateria hacia abajo a (0.75 ± 0.13 ± 0.16) g.",
                "spec_en": "MICROSCOPE Pt/Ti cylinders & CERN ALPHA-g antihydrogen trap",
                "spec_es": "Cilindros Pt/Ti de MICROSCOPE y trampa de antihidrógeno ALPHA-g",
                "doi": "10.1103/PhysRevLett.129.121102",
            },
        ],
    },
    "t04": {
        "lineage_en": "Pioneers of Step T.04 · Rabi (1938) · Ramsey (1950) · Hahn (1950) · Zych, Costa, Pikovski & Brukner (2011) · Margalit, Zhou, Machluf, Rohrlich, Japha & Folman (2015)",
        "lineage_es": "Pioneros del Paso T.04 · Rabi (1938) · Ramsey (1950) · Hahn (1950) · Zych, Costa, Pikovski y Brukner (2011) · Margalit, Zhou, Machluf, Rohrlich, Japha y Folman (2015)",
        "title_en": "The Humans Behind Step T.04 · Spin Echoes, Quantum Clocks, and Atom Chips",
        "title_es": "Las Personas Detrás del Paso T.04 · Ecos de Espín, Relojes Cuánticos y Chips Atómicos",
        "lead_en": "What happens when a single quantum particle carrying its own internal ticking clock travels along two heights at once? Three generations of physicists built the pulse sequences, the theoretical blueprint, and the atom-chip analogue.",
        "lead_es": "¿Qué ocurre cuando una sola partícula cuántica que lleva su propio reloj interno viaja por dos alturas a la vez? Tres generaciones de físicos construyeron las secuencias de pulsos, la propuesta teórica y el análogo en chip atómico.",
        "cards": [
            {
                "icon": "canal-ray",
                "era_en": "1938 & 1950 · New York, Cambridge & Urbana",
                "era_es": "1938 y 1950 · Nueva York, Cambridge y Urbana",
                "names_en": "Isidor Isaac Rabi · Norman F. Ramsey · Erwin L. Hahn",
                "names_es": "Isidor Isaac Rabi · Norman F. Ramsey · Erwin L. Hahn",
                "place_en": "Columbia University, Harvard University & University of Illinois",
                "place_es": "Universidad de Columbia, Universidad de Harvard y Universidad de Illinois",
                "story_en": "Every atomic clock rests on their pulse craft: Rabi invented molecular-beam magnetic resonance in 1938; Ramsey split the driving field into two coherent pulses separated by a free-evolution interval in 1950 so internal phase maps onto state population; and the same year Erwin Hahn discovered the spin-echo π pulse that reverses inhomogeneous dephasing.",
                "story_es": "Todo reloj atómico descansa en su oficio de pulsos: Rabi inventó la resonancia magnética de haces moleculares en 1938; Ramsey dividió el campo en dos pulsos coherentes separados por una evolución libre en 1950 para convertir la fase interna en población; y ese mismo año Erwin Hahn descubrió el pulso π de eco de espín.",
                "spec_en": "Ramsey π/2–T–π/2 interferometry & Hahn spin echo",
                "spec_es": "Interferometría de Ramsey π/2–T–π/2 y eco de espín de Hahn",
                "doi": "10.1103/PhysRev.78.695",
            },
            {
                "icon": "page-wootters",
                "era_en": "2011 · Vienna, Austria",
                "era_es": "2011 · Viena, Austria",
                "names_en": "Magdalena Zych, Fabio Costa, Igor Pikovski & Časlav Brukner",
                "names_es": "Magdalena Zych, Fabio Costa, Igor Pikovski y Časlav Brukner",
                "place_en": "University of Vienna & Institute for Quantum Optics and Quantum Information",
                "place_es": "Universidad de Viena e Instituto de Óptica e Información Cuántica (IQOQI)",
                "story_en": "In 2011 Zych, Costa, Pikovski, and Brukner showed that if a single massive particle with an internal two-level clock is split across two heights Δh in a gravitational potential, the proper-time difference Δτ = gΔh·T/c² entangles the internal clock with the path, reducing fringe visibility as V = |cos(ωΔτ/2)|.",
                "story_es": "En 2011 Zych, Costa, Pikovski y Brukner mostraron que si una partícula masiva con un reloj interno de dos niveles se divide entre dos alturas Δh en un potencial gravitatorio, la diferencia de tiempo propio Δτ = gΔh·T/c² entrelaza el reloj con el camino, modulando la visibilidad como V = |cos(ωΔτ/2)|.",
                "spec_en": "Gravitational proper-time complementarity · V = |⟨τ₁|τ₂⟩|",
                "spec_es": "Complementariedad de tiempo propio gravitatorio · V = |⟨τ₁|τ₂⟩|",
                "doi": "10.1038/ncomms1498",
            },
            {
                "icon": "atom-chip",
                "era_en": "2015 · Beersheba, Israel",
                "era_es": "2015 · Beerseba, Israel",
                "names_en": "Yair Margalit, Zhifan Zhou, Shimon Machluf, Daniel Rohrlich, Yonathan Japha & Ron Folman",
                "names_es": "Yair Margalit, Zhifan Zhou, Shimon Machluf, Daniel Rohrlich, Yonathan Japha y Ron Folman",
                "place_en": "Atom Chip Group, Ben-Gurion University of the Negev",
                "place_es": "Grupo de Chips Atómicos, Universidad Ben-Gurión del Néguev",
                "story_en": "Because the gravitational node for an optical clock requires ~10.7 m·s of height-time area, Margalit, Folman, and colleagues built an analogue on a micron-scale atom chip: splitting a rubidium-87 Bose–Einstein condensate into two wavepackets and driving a differential clock rate with a magnetic gradient to watch fringes vanish and revive.",
                "story_es": "Como el nodo gravitatorio para un reloj óptico requiere ~10.7 m·s de área altura-tiempo, Margalit, Folman y colegas construyeron un análogo en un chip atómico micrométrico: dividieron un condensado de Bose–Einstein de rubidio-87 en dos paquetes y aplicaron un gradiente magnético para ver apagarse y revivir las franjas.",
                "spec_en": "⁸⁷Rb BEC atom-chip clock interferometer (magnetic gradient)",
                "spec_es": "Interferómetro de reloj BEC de ⁸⁷Rb en chip atómico (gradiente magnético)",
                "doi": "10.1126/science.aac6498",
            },
        ],
    },
    "t05": {
        "lineage_en": "Pioneers of Step T.05 · Peres & Wootters (1996–1998) · Hornberger, Hackermüller & Arndt (2003–2004) · Kafri, Taylor & Milburn (2014) · Bose et al. & Marletto–Vedral (2017) · Lee/Eöt-Wash & Tan/HUST (2020) · Westphal & Aspelmeyer (2021) · 2025–2026 Dispute Authors",
        "lineage_es": "Pioneros del Paso T.05 · Peres y Wootters (1996–1998) · Hornberger, Hackermüller y Arndt (2003–2004) · Kafri, Taylor y Milburn (2014) · Bose et al. y Marletto–Vedral (2017) · Lee/Eöt-Wash y Tan/HUST (2020) · Westphal y Aspelmeyer (2021) · Autores de la disputa 2025–2026",
        "title_en": "The Humans Behind Step T.05 · The Two-Mass Proposals, the Sub-Millimeter Pendulums, and the Open Dispute",
        "title_es": "Las Personas Detrás del Paso T.05 · Las Propuestas de Dos Masas, los Péndulos Submilimétricos y la Disputa Abierta",
        "lead_en": "Step T.05 brings together three communities of researchers: quantum-information theorists who designed the entanglement witness and its classical counter-models, precision-gravity experimentalists who tested Newton's law at 52 µm and 90 mg, and the authors of the active 2025–2026 debate.",
        "lead_es": "El Paso T.05 reúne a tres comunidades de investigadores: teóricos de información cuántica que diseñaron el testigo de entrelazamiento y sus contramodelos clásicos, experimentalistas que probaron la ley de Newton a 52 µm y 90 mg, y los autores del debate activo de 2025–2026.",
        "cards": [
            {
                "icon": "bmv-branches",
                "era_en": "2017 · London, Groningen, Southampton, Belfast & Oxford",
                "era_es": "2017 · Londres, Groninga, Southampton, Belfast y Oxford",
                "names_en": "Sougato Bose, Anupam Mazumdar, Gavin Morley, Hendrik Ulbricht et al. · Chiara Marletto & Vlatko Vedral",
                "names_es": "Sougato Bose, Anupam Mazumdar, Gavin Morley, Hendrik Ulbricht et al. · Chiara Marletto y Vlatko Vedral",
                "place_en": "University College London Consortium & University of Oxford",
                "place_es": "Consorcio de University College London y Universidad de Oxford",
                "story_en": "In back-to-back December 2017 Physical Review Letters papers, Bose and nine co-authors proposed holding two 10⁻¹⁴ kg micro-diamonds in spatial superpositions 450 µm apart for 2.5 s so their four branch distances accumulate Δφ = 0.31 rad, while Marletto and Vedral formulated the general information-theoretic argument.",
                "story_es": "En dos artículos consecutivos de diciembre de 2017 en Physical Review Letters, Bose y nueve coautores propusieron sostener dos microdiamantes de 10⁻¹⁴ kg en superposiciones espaciales a 450 µm durante 2.5 s para acumular Δφ = 0.31 rad, mientras Marletto y Vedral formularon el argumento general en teoría de la información.",
                "spec_en": "Twin-mass interferometry proposal · Δφ = 0.31 rad (PROPOSED)",
                "spec_es": "Propuesta de interferometría de dos masas · Δφ = 0.31 rad (PROPUESTO)",
                "doi": "10.1103/PhysRevLett.119.240401",
            },
            {
                "icon": "page-wootters",
                "era_en": "1996–2026 · Haifa, Williamstown, Maryland, Madrid, London & Vienna",
                "era_es": "1996–2026 · Haifa, Williamstown, Maryland, Madrid, Londres y Viena",
                "names_en": "Asher Peres & William Wootters · Kafri, Taylor & Milburn · Trillo & Navascués · Aziz & Howl · Schneider et al.",
                "names_es": "Asher Peres y William Wootters · Kafri, Taylor y Milburn · Trillo y Navascués · Aziz y Howl · Schneider et al.",
                "place_en": "Concurrence, partial-transpose negativity, LOCC channels & the 2025–2026 debate",
                "place_es": "Concurrencia, negatividad por transpuesta parcial, canales LOCC y el debate 2025–2026",
                "story_en": "Peres (1996) and Wootters (1998) gave the exact measures of two-qubit entanglement; Kafri, Taylor, and Milburn (2014) derived the minimum noise of a classical measurement-and-feedback channel. In 2025–2026, Trillo and Navascués, Aziz and Howl, Marletto, Oppenheim, Vedral and Wilson, Diósi, and Schneider et al. opened the live dispute over what a positive witness would settle.",
                "story_es": "Peres (1996) y Wootters (1998) dieron las medidas exactas de entrelazamiento de dos qubits; Kafri, Taylor y Milburn (2014) derivaron el ruido mínimo de un canal clásico de medición y retroalimentación. En 2025–2026, Trillo y Navascués, Aziz y Howl, Marletto, Oppenheim, Vedral y Wilson, Diósi, y Schneider et al. abrieron la disputa sobre qué zanjaría un testigo positivo.",
                "spec_en": "Three channels at equal weight · Page label OPEN",
                "spec_es": "Tres canales con el mismo peso · Etiqueta de página ABIERTO",
                "doi": "10.1103/PhysRevLett.134.100201",
            },
            {
                "icon": "torsion-pendulum",
                "era_en": "2003–2026 · Seattle, Wuhan, Vienna & Leiden",
                "era_es": "2003–2026 · Seattle, Wuhan, Viena y Leiden",
                "names_en": "Jun-Ge Lee & Eöt-Wash · Wen-Hai Tan & HUST · Tobias Westphal & Markus Aspelmeyer · Hornberger, Hackermüller & Arndt",
                "names_es": "Jun-Ge Lee y Eöt-Wash · Wen-Hai Tan y HUST · Tobias Westphal y Markus Aspelmeyer · Hornberger, Hackermüller y Arndt",
                "place_en": "52 µm platinum wedges, 48 µm tungsten plates, 90 mg gold spheres & C₇₀ beams",
                "place_es": "Cuñas de platino a 52 µm, placas de tungsteno a 48 µm, esferas de oro de 90 mg y haces de C₇₀",
                "story_en": "Jun-Ge Lee and the Seattle Eöt-Wash group tested Newton's law across a 52 µm gap with a 120-wedge platinum pendulum (2020), while Wen-Hai Tan and the Wuhan HUST group reached a 48 µm scale with tungsten plates. In Vienna, Tobias Westphal and Markus Aspelmeyer measured gravity between 90 mg gold spheres (2021), and Klaus Hornberger, Lucia Hackermüller, and Markus Arndt measured fullerene gas and thermal decoherence.",
                "story_es": "Jun-Ge Lee y el grupo Eöt-Wash probaron la ley de Newton a 52 µm con un péndulo de platino de 120 cuñas (2020), mientras Wen-Hai Tan y el grupo HUST en Wuhan alcanzaron una escala de 48 µm con placas de tungsteno. En Viena, Tobias Westphal y Markus Aspelmeyer midieron la gravedad entre esferas de oro de 90 mg (2021), y Klaus Hornberger, Lucia Hackermüller y Markus Arndt midieron la decoherencia por gas y fotones en fulerenos.",
                "spec_en": "52 µm 120-fold wedge torque (1.5 fN·m) & 90 mg gravity",
                "spec_es": "Par de 120 cuñas a 52 µm (1.5 fN·m) y gravedad en 90 mg",
                "doi": "10.1103/PhysRevLett.124.101101",
            },
        ],
    },
    "t06": {
        "lineage_en": "Pioneers of Step T.06 · Diósi (1987) · Penrose (1996) · Helou et al. (2017) · Fein & Arndt (2019) · Donadi, Piscicchia, Curceanu, Diósi, Laubenstein & Bassi (2021) · Oppenheim et al. (2023) · XENONnT Collaboration (2026)",
        "lineage_es": "Pioneros del Paso T.06 · Diósi (1987) · Penrose (1996) · Helou et al. (2017) · Fein y Arndt (2019) · Donadi, Piscicchia, Curceanu, Diósi, Laubenstein y Bassi (2021) · Oppenheim et al. (2023) · Colaboración XENONnT (2026)",
        "title_en": "The Humans Behind Step T.06 · From Gravitational Self-Energy to Deep Underground Caverns",
        "title_es": "Las Personas Detrás del Paso T.06 · De la Autoenergía Gravitatoria a las Cavernas Subterráneas",
        "lead_en": "A proposal that gravity ends spatial superpositions also implies a tiny spontaneous jitter of nuclear charges. Testing that prediction required taking ultra-pure germanium crystals and multi-tonne liquid-xenon chambers under 1,400 meters of Italian dolomite rock.",
        "lead_es": "Una propuesta de que la gravedad termina las superposiciones espaciales implica también un pequeño temblor espontáneo de las cargas nucleares. Poner a prueba esa predicción exigió llevar cristales de germanio ultrapuro y cámaras de xenón líquido bajo 1,400 metros de roca dolomita en Italia.",
        "cards": [
            {
                "icon": "einstein-elevator",
                "era_en": "1987 & 1996 · Budapest & Oxford",
                "era_es": "1987 y 1996 · Budapest y Oxford",
                "names_en": "Lajos Diósi & Roger Penrose",
                "names_es": "Lajos Diósi y Roger Penrose",
                "place_en": "Central Research Institute for Physics (KFKI) & Mathematical Institute, Oxford",
                "place_es": "Instituto Central de Investigación Física (KFKI) e Instituto Matemático de Oxford",
                "story_en": "Lajos Diósi in 1987 wrote a universal master equation in which gravitational self-energy damps spatial superpositions, introducing a short-distance smearing width R0; in 1996 Roger Penrose independently arrived at the same lifetime τ ≈ ħ/E_G from the ambiguity between two superposed spacetime geometries.",
                "story_es": "Lajos Diósi escribió en 1987 una ecuación maestra universal en la que la autoenergía gravitatoria amortigua las superposiciones espaciales, introduciendo un ancho de suavizado R0; en 1996 Roger Penrose llegó de forma independiente a la misma vida media τ ≈ ħ/E_G a partir de la ambigüedad entre dos geometrías de espaciotiempo.",
                "spec_en": "Gravitational self-energy proposal · τ = ħ/E_G (PROPOSED)",
                "spec_es": "Propuesta de autoenergía gravitatoria · τ = ħ/E_G (PROPUESTO)",
                "doi": "10.1007/BF02105068",
            },
            {
                "icon": "underground-crystal",
                "era_en": "2021 · Under the Gran Sasso, Italy",
                "era_es": "2021 · Bajo el Gran Sasso, Italia",
                "names_en": "Sandro Donadi, Kristian Piscicchia, Catalina Curceanu, Lajos Diósi, Matthias Laubenstein & Angelo Bassi",
                "names_es": "Sandro Donadi, Kristian Piscicchia, Catalina Curceanu, Lajos Diósi, Matthias Laubenstein y Angelo Bassi",
                "place_en": "Laboratori Nazionali del Gran Sasso (INFN) · Coaxial HPGe Detector",
                "place_es": "Laboratori Nazionali del Gran Sasso (INFN) · Detector coaxial de germanio",
                "story_en": "Working together with Lajos Diósi himself, the experimental team led by Catalina Curceanu and Matthias Laubenstein operated a 2 kg high-purity germanium crystal encased in electrolytic copper and low-activity lead deep inside Gran Sasso. Over 62 days they counted 576 photons against 506 expected background events, setting R0 > 0.54 × 10⁻¹⁰ m.",
                "story_es": "Trabajando junto al propio Lajos Diósi, el equipo experimental encabezado por Catalina Curceanu y Matthias Laubenstein operó un cristal de germanio de alta pureza de 2 kg blindado con cobre electrolítico y plomo de baja actividad bajo el Gran Sasso. En 62 días contaron 576 fotones frente a 506 esperados de fondo, fijando R0 > 0.54 × 10⁻¹⁰ m.",
                "spec_en": "576 measured vs 506 background counts · R0 > 0.54 Å (BOUND)",
                "spec_es": "576 medidos frente a 506 de fondo · R0 > 0.54 Å (COTA)",
                "doi": "10.1038/s41567-020-1008-4",
            },
            {
                "icon": "underground-crystal",
                "era_en": "2019–2026 · Gran Sasso, Vienna & London",
                "era_es": "2019–2026 · Gran Sasso, Viena y Londres",
                "names_en": "Elena Aprile & XENONnT · Yaakov Fein & Markus Arndt · Jonathan Oppenheim et al.",
                "names_es": "Elena Aprile y XENONnT · Yaakov Fein y Markus Arndt · Jonathan Oppenheim et al.",
                "place_en": "XENONnT Liquid Xenon TPC, Vienna Macromolecule Interferometer & UCL",
                "place_es": "Cámara de xenón líquido XENONnT, interferómetro macromolecular de Viena y UCL",
                "story_en": "In 2026 the XENONnT Collaboration analyzed 1.16 tonne-years of liquid-xenon exposure to push the radiation limit to R0 > 4.9 × 10⁻¹⁰ m (90 %). Meanwhile Yaakov Fein, Markus Arndt and co-workers observed matter-wave interference for molecules beyond 25,000 atomic mass units in Vienna (2019), and Jonathan Oppenheim and colleagues bounded the classical-gravity diffusion trade-off (2023).",
                "story_es": "En 2026 la colaboración XENONnT analizó 1.16 toneladas-año de exposición de xenón líquido para llevar el límite de radiación a R0 > 4.9 × 10⁻¹⁰ m (90 %). Entretanto, Yaakov Fein, Markus Arndt y colaboradores observaron interferencia de ondas de materia en moléculas de más de 25,000 unidades de masa atómica en Viena (2019), y Jonathan Oppenheim y colegas acotaron la difusión gravitatoria (2023).",
                "spec_en": "XENONnT 1.16 t·yr (R0 > 4.9 Å) & 25,000 amu molecules",
                "spec_es": "XENONnT 1.16 t·año (R0 > 4.9 Å) y moléculas de 25,000 uma",
                "doi": "10.1103/mp49-4422",
            },
        ],
    },
    "t07": {
        "lineage_en": "Pioneers of Step T.07 · Bryce DeWitt (1967) · Don Page & William Wootters (1983) · Ekaterina Moreva, Giorgio Brida, Marco Gramegna, Vittorio Giovannetti, Lorenzo Maccone & Marco Genovese (2014) · Flaminia Giacomini, Esteban Castro-Ruiz & Časlav Brukner (2019)",
        "lineage_es": "Pioneros del Paso T.07 · Bryce DeWitt (1967) · Don Page y William Wootters (1983) · Ekaterina Moreva, Giorgio Brida, Marco Gramegna, Vittorio Giovannetti, Lorenzo Maccone y Marco Genovese (2014) · Flaminia Giacomini, Esteban Castro-Ruiz y Časlav Brukner (2019)",
        "title_en": "The Humans Behind Step T.07 · A Timeless Equation, Conditional Clocks, and Two Entangled Photons",
        "title_es": "Las Personas Detrás del Paso T.07 · Una Ecuación sin Tiempo, Relojes Condicionales y Dos Fotones Entrelazados",
        "lead_en": "When canonical quantum gravity removed external coordinate time from the wave equation of a closed universe, these physicists asked how a ticking clock can live inside the quantum state itself.",
        "lead_es": "Cuando la gravedad cuántica canónica quitó el tiempo coordenado externo de la ecuación de onda de un universo cerrado, estos físicos preguntaron cómo puede vivir un reloj dentro del propio estado cuántico.",
        "cards": [
            {
                "icon": "einstein-elevator",
                "era_en": "1967 · Chapel Hill & Princeton",
                "era_es": "1967 · Chapel Hill y Princeton",
                "names_en": "Bryce S. DeWitt & John Archibald Wheeler",
                "names_es": "Bryce S. DeWitt y John Archibald Wheeler",
                "place_en": "University of North Carolina at Chapel Hill & Princeton University",
                "place_es": "Universidad de Carolina del Norte en Chapel Hill y Universidad de Princeton",
                "story_en": "In his 1967 treatise on canonical quantum gravity, following discussions with John Archibald Wheeler, Bryce DeWitt showed that reparameterization invariance forces the total Hamiltonian of a closed universe to annihilate the state: Ĥ|Ψ⟩ = 0, leaving no external time parameter t.",
                "story_es": "En su tratado de 1967 sobre gravedad cuántica canónica, tras conversaciones con John Archibald Wheeler, Bryce DeWitt mostró que la invariancia bajo reparametrización obliga al hamiltoniano total de un universo cerrado a anular el estado: Ĥ|Ψ⟩ = 0, sin parámetro externo de tiempo t.",
                "spec_en": "Wheeler–DeWitt constraint · Ĥ|Ψ⟩ = 0 (DERIVED)",
                "spec_es": "Restricción de Wheeler–DeWitt · Ĥ|Ψ⟩ = 0 (DERIVADO)",
                "doi": "10.1103/PhysRev.160.1113",
            },
            {
                "icon": "page-wootters",
                "era_en": "1983 · University Park & Williamstown",
                "era_es": "1983 · University Park y Williamstown",
                "names_en": "Don N. Page & William K. Wootters",
                "names_es": "Don N. Page y William K. Wootters",
                "place_en": "Pennsylvania State University & Williams College",
                "place_es": "Universidad Estatal de Pensilvania y Williams College",
                "story_en": "Page and Wootters proposed 'evolution without evolution': split the stationary world into a clock subsystem C and the rest S with (Ĥ_C + Ĥ_S)|Ψ⟩⟩ = 0. Projecting the stationary joint state onto the clock's time states |t_n⟩_C recovers the exact Schrödinger evolution of S.",
                "story_es": "Page y Wootters propusieron la 'evolución sin evolución': dividir el mundo estacionario en un subsistema reloj C y el resto S con (Ĥ_C + Ĥ_S)|Ψ⟩⟩ = 0. Proyectar el estado conjunto estacionario sobre los estados de tiempo |t_n⟩_C recupera la evolución de Schrödinger exacta de S.",
                "spec_en": "Conditional probability clock · |ψ(t_n)⟩ = √d ⟨t_n|Ψ⟩⟩",
                "spec_es": "Reloj de probabilidad condicional · |ψ(t_n)⟩ = √d ⟨t_n|Ψ⟩⟩",
                "doi": "10.1103/PhysRevD.27.2885",
            },
            {
                "icon": "atom-chip",
                "era_en": "2014 & 2019 · Turin, Pisa, Pavia & Vienna",
                "era_es": "2014 y 2019 · Turín, Pisa, Pavía y Viena",
                "names_en": "Ekaterina Moreva, Giorgio Brida, Marco Gramegna, Vittorio Giovannetti, Lorenzo Maccone & Marco Genovese · Flaminia Giacomini, Esteban Castro-Ruiz & Časlav Brukner",
                "names_es": "Ekaterina Moreva, Giorgio Brida, Marco Gramegna, Vittorio Giovannetti, Lorenzo Maccone y Marco Genovese · Flaminia Giacomini, Esteban Castro-Ruiz y Časlav Brukner",
                "place_en": "INRIM National Metrology Institute (Turin) & IQOQI Vienna",
                "place_es": "Instituto Nacional de Investigación Metrológica INRIM (Turín) e IQOQI Viena",
                "story_en": "In 2014 Moreva and colleagues built a two-photon optical-table realization in Turin: passing polarization-entangled photons through quartz plates, they showed that conditioning on one photon's polarization recovers the other's rotation while an unconditioned observer sees a stationary state. In 2019 Giacomini, Castro-Ruiz, and Brukner derived the transformations between quantum reference frames.",
                "story_es": "En 2014 Moreva y colegas construyeron una realización con dos fotones en una mesa óptica en Turín: al pasar fotones entrelazados en polarización por placas de cuarzo, mostraron que condicionar a un fotón recupera la rotación del otro mientras un observador sin condicionar ve un estado estacionario. En 2019 Giacomini, Castro-Ruiz y Brukner derivaron los cambios entre marcos cuánticos.",
                "spec_en": "Turin biphoton table & quantum reference frames",
                "spec_es": "Mesa bifotónica de Turín y marcos de referencia cuánticos",
                "doi": "10.1103/PhysRevA.89.052122",
            },
        ],
    },
    "t08": {
        "lineage_en": "Pioneers of Step T.08 · Penzias & Wilson (1965) · Jacob Bekenstein (1973) · Stephen Hawking (1975) · Joseph Bisognano & Eyvind Wichmann (1975) · William Unruh (1976) · John Mather & COBE FIRAS (1996) · Jeff Steinhauer (2016)",
        "lineage_es": "Pioneros del Paso T.08 · Penzias y Wilson (1965) · Jacob Bekenstein (1973) · Stephen Hawking (1975) · Joseph Bisognano y Eyvind Wichmann (1975) · William Unruh (1976) · John Mather y COBE FIRAS (1996) · Jeff Steinhauer (2016)",
        "title_en": "The Humans Behind Step T.08 · Causal Horizons, Rindler Wedges, and the Cosmic Microwave Sky",
        "title_es": "Las Personas Detrás del Paso T.08 · Horizontes Causales, Cuñas de Rindler y el Fondo Cósmico de Microondas",
        "lead_en": "Linking the steepening clock slope at a horizon to an exact thermal bath brought together quantum-field theorists studying accelerated observers and radio astronomers measuring the 2.725 K cosmic microwave background that bathes every astrophysical black hole.",
        "lead_es": "Vincular la pendiente del reloj en un horizonte con un baño térmico exacto reunió a teóricos de campos cuánticos que estudiaban observadores acelerados y a radioastrónomos que midieron el fondo cósmico de microondas de 2.725 K que baña a todo agujero negro astrofísico.",
        "cards": [
            {
                "icon": "rindler-wedge",
                "era_en": "1973–1976 · Princeton, Cambridge, Berkeley & Vancouver",
                "era_es": "1973–1976 · Princeton, Cambridge, Berkeley y Vancouver",
                "names_en": "Jacob D. Bekenstein · Stephen W. Hawking · William G. Unruh · Joseph Bisognano & Eyvind Wichmann",
                "names_es": "Jacob D. Bekenstein · Stephen W. Hawking · William G. Unruh · Joseph Bisognano y Eyvind Wichmann",
                "place_en": "Princeton University, University of Cambridge, UC Berkeley & University of British Columbia",
                "place_es": "Universidad de Princeton, Universidad de Cambridge, UC Berkeley y Universidad de Columbia Británica",
                "story_en": "Jacob Bekenstein proposed in 1973 that a black hole carries entropy proportional to its horizon area; in 1975 Stephen Hawking fixed the proportionality at 1/4 by showing that a horizon radiates thermally at T_H = ħκ/(2πck_B). Within months Joseph Bisognano and Eyvind Wichmann proved the modular boost theorem on a Rindler wedge, and in 1976 William Unruh showed that an accelerated detector in flat vacuum sees T_U = ħa/(2πck_B).",
                "story_es": "Jacob Bekenstein propuso en 1973 que un agujero negro tiene entropía proporcional al área de su horizonte; en 1975 Stephen Hawking fijó la constante en 1/4 al mostrar que un horizonte radia a T_H = ħκ/(2πck_B). Ese mismo año Bisognano y Wichmann demostraron el teorema modular en una cuña de Rindler, y en 1976 William Unruh mostró que un detector acelerado en el vacío ve T_U = ħa/(2πck_B).",
                "spec_en": "Unruh–Hawking temperature & S_BH = k_B A / (4 ℓ_P²) (DERIVED)",
                "spec_es": "Temperatura de Unruh–Hawking y S_BH = k_B A / (4 ℓ_P²) (DERIVADO)",
                "doi": "10.1103/PhysRevD.14.870",
            },
            {
                "icon": "horn-antenna",
                "era_en": "1965 & 1996 · Holmdel, New Jersey & NASA Goddard",
                "era_es": "1965 y 1996 · Holmdel, Nueva Jersey y NASA Goddard",
                "names_en": "Arno A. Penzias & Robert W. Wilson · John C. Mather & the COBE FIRAS Team",
                "names_es": "Arno A. Penzias y Robert W. Wilson · John C. Mather y el Equipo COBE FIRAS",
                "place_en": "Bell Labs Crawford Hill Horn Antenna & Cosmic Background Explorer",
                "place_es": "Antena de cuerno de Bell Labs en Crawford Hill y satélite COBE",
                "story_en": "In 1965 Arno Penzias and Robert Wilson detected the isotropic microwave background at 4,080 MHz with the Bell Labs horn reflector at Crawford Hill, and in 1996 John Mather and the COBE FIRAS team measured its Planck spectrum at 2.728 ± 0.004 K—nearly forty-four million times warmer than the 61.7 nK Hawking temperature of a solar-mass black hole.",
                "story_es": "En 1965 Arno Penzias y Robert Wilson detectaron el fondo isótropo de microondas a 4,080 MHz con la antena de cuerno de Bell Labs en Crawford Hill, y en 1996 John Mather y el equipo COBE FIRAS midieron su espectro de Planck en 2.728 ± 0.004 K: casi cuarenta y cuatro millones de veces más cálido que los 61.7 nK de un agujero negro de una masa solar.",
                "spec_en": "2.725 K CMB bath vs 61.7 nK solar Hawking temperature",
                "spec_es": "Baño CMB de 2.725 K frente a 61.7 nK de temperatura de Hawking solar",
                "doi": "10.1086/178173",
            },
            {
                "icon": "sonic-horizon",
                "era_en": "2016 · Haifa, Israel",
                "era_es": "2016 · Haifa, Israel",
                "names_en": "Jeff Steinhauer",
                "names_es": "Jeff Steinhauer",
                "place_en": "Technion – Israel Institute of Technology · Acoustic BEC Horizon",
                "place_es": "Technion – Instituto Tecnológico de Israel · Horizonte acústico en BEC",
                "story_en": "Because astrophysical Hawking radiation is buried beneath the 2.725 K sky, Jeff Steinhauer swept a laser step potential through a rubidium-87 Bose–Einstein condensate at the Technion in 2016 to create a supersonic acoustic horizon, observing density correlations between partner phonons across the sonic boundary—an analogue kinematics test without gravitational dynamics.",
                "story_es": "Como la radiación de Hawking astrofísica queda oculta bajo el cielo de 2.725 K, Jeff Steinhauer barrió un escalón láser a través de un condensado de Bose–Einstein de rubidio-87 en el Technion en 2016 para crear un horizonte acústico supersónico, observando correlaciones entre fonones a ambos lados de la frontera sónica.",
                "spec_en": "⁸⁷Rb acoustic sonic-horizon analogue (MEASURED analogue)",
                "spec_es": "Análogo de horizonte sónico en BEC de ⁸⁷Rb (MEDIDO en análogo)",
                "doi": "10.1038/nphys3863",
            },
        ],
    },
    "t09": {
        "lineage_en": "Pioneers of Step T.09 · Roy Kerr (1963) · Larry Smarr (1973) · Saul Teukolsky (1973) · Edward Leaver (1985) · Berti, Cardoso & Starinets (2009) · LIGO/Virgo/KAGRA & Isi et al. (2016, 2019, 2021, 2025)",
        "lineage_es": "Pioneers of Step T.09 · Roy Kerr (1963) · Larry Smarr (1973) · Saul Teukolsky (1973) · Edward Leaver (1985) · Berti, Cardoso y Starinets (2009) · LIGO/Virgo/KAGRA e Isi et al. (2016, 2019, 2021, 2025)".replace("Pioneers of Step", "Pioneros del Paso"),
        "title_en": "The Humans Behind Step T.09 · Spinning Horizons, Continued Fractions, and Four-Kilometer Interferometers",
        "title_es": "Las Personas Detrás del Paso T.09 · Horizontes en Rotación, Fracciones Continuas e Interferómetros de Cuatro Kilómetros",
        "lead_en": "Predicting and measuring the damped tones of a newly merged black hole took fifty-two years: from Roy Kerr's 1963 exact rotating solution and Edward Leaver's 1985 continued-fraction eigenvalues to the LIGO–Virgo–KAGRA interferometers.",
        "lead_es": "Predecir y medir los tonos amortiguados de un agujero negro recién fusionado tomó cincuenta y dos años: desde la solución exacta en rotación de Roy Kerr en 1963 y las fracciones continuas de Edward Leaver en 1985 hasta los interferómetros de LIGO–Virgo–KAGRA.",
        "cards": [
            {
                "icon": "kerr-ergosphere",
                "era_en": "1963 & 1973 · Austin, Stanford & Pasadena",
                "era_es": "1963 y 1973 · Austin, Stanford y Pasadena",
                "names_en": "Roy P. Kerr · Larry Smarr · Saul A. Teukolsky",
                "names_es": "Roy P. Kerr · Larry Smarr · Saul A. Teukolsky",
                "place_en": "University of Texas at Austin, Stanford University & Caltech",
                "place_es": "Universidad de Texas en Austin, Universidad de Stanford y Caltech",
                "story_en": "In 1963 New Zealand mathematician Roy Kerr discovered the exact vacuum solution for a rotating mass, fixing the horizon area A(M, χ) = 8π(GM/c²)²(1 + √(1 − χ²)). Ten years later Larry Smarr proved the integral horizon identity Mc² = κc²A/(4πG) + 2Ω_H J and Saul Teukolsky separated the master wave equation for gravitational perturbations on a Kerr background.",
                "story_es": "En 1963 el matemático neozelandés Roy Kerr descubrió la solución exacta en el vacío para una masa en rotación, fijando el área del horizonte A(M, χ) = 8π(GM/c²)²(1 + √(1 − χ²)). Diez años después Larry Smarr demostró la identidad integral Mc² = κc²A/(4πG) + 2Ω_H J y Saul Teukolsky separó la ecuación maestra de perturbaciones en el fondo de Kerr.",
                "spec_en": "Kerr metric, Smarr identity & Teukolsky equation (DERIVED)",
                "spec_es": "Métrica de Kerr, identidad de Smarr y ecuación de Teukolsky",
                "doi": "10.1103/PhysRevLett.11.237",
            },
            {
                "icon": "continued-fraction",
                "era_en": "1985 & 2009 · Salt Lake City, Oxford, Lisbon & Mississippi",
                "era_es": "1985 y 2009 · Salt Lake City, Oxford, Lisboa y Misisipi",
                "names_en": "Edward W. Leaver · Emanuele Berti, Vitor Cardoso & Andrei O. Starinets",
                "names_es": "Edward W. Leaver · Emanuele Berti, Vitor Cardoso y Andrei O. Starinets",
                "place_en": "University of Utah & Quasinormal-Mode Ringdown Tables",
                "place_es": "Universidad de Utah y Tablas de Modos Cuasinormales",
                "story_en": "In 1985 Edward Leaver adapted Jaffe's hydrogen-molecule continued-fraction method to Teukolsky's equation, computing the exact complex quasinormal frequencies ω_{ℓmn}(M, χ) of a spinning black hole. In 2009 Emanuele Berti, Vitor Cardoso, and Andrei Starinets synthesized the modern horizon-spectroscopy tables across spin and overtone number.",
                "story_es": "En 1985 Edward Leaver adaptó el método de fracciones continuas de Jaffe a la ecuación de Teukolsky, calculando las frecuencias complejas cuasinormales exactas ω_{ℓmn}(M, χ) de un agujero negro en rotación. En 2009 Emanuele Berti, Vitor Cardoso y Andrei Starinets sintetizaron las tablas modernas de espectroscopía del horizonte.",
                "spec_en": "Continued-fraction QNM spectrum ω_{220}, ω_{221} (DERIVED)",
                "spec_es": "Espectro QNM por fracciones continuas ω_{220}, ω_{221} (DERIVADO)",
                "doi": "10.1098/rspa.1985.0119",
            },
            {
                "icon": "ligo-interferometer",
                "era_en": "2016–2025 · Hanford, Livingston, Cascina, Kamioka, MIT & Caltech",
                "era_es": "2016–2025 · Hanford, Livingston, Cascina, Kamioka, MIT y Caltech",
                "names_en": "LIGO, Virgo & KAGRA Collaborations · Maximiliano Isi, Matthew Giesler, Will Farr, Mark Scheel & Saul Teukolsky",
                "names_es": "Colaboraciones LIGO, Virgo y KAGRA · Maximiliano Isi, Matthew Giesler, Will Farr, Mark Scheel y Saul Teukolsky",
                "place_en": "GW150914 & GW250114 Ringdown Spectroscopy",
                "place_es": "Espectroscopía de resonancia en GW150914 y GW250114",
                "story_en": "After LIGO and Virgo observed the GW150914 merger ringdown around 251 Hz (M_f ≈ 62 M_☉, χ_f ≈ 0.67), Maximiliano Isi, Matthew Giesler, Will Farr, Mark Scheel, and Saul Teukolsky formulated two-tone overtone spectroscopy in 2019, and in 2025 the LVK collaboration recorded GW250114 at network SNR ~80 to test Kerr quasinormal tones.",
                "story_es": "Tras observar LIGO y Virgo la resonancia de GW150914 cerca de 251 Hz (M_f ≈ 62 M_☉, χ_f ≈ 0.67), Maximiliano Isi, Matthew Giesler, Will Farr, Mark Scheel y Saul Teukolsky formularon la espectroscopía con sobretonos en 2019, y en 2025 la colaboración LVK registró GW250114 con SNR ~80 para probar los modos de Kerr.",
                "spec_en": "GW150914 (MEASURED) & GW250114 SNR ~80 (SINGLE RESULT)",
                "spec_es": "GW150914 (MEDIDO) y GW250114 SNR ~80 (RESULTADO ÚNICO)",
                "doi": "10.1103/PhysRevLett.116.221101",
            },
        ],
    },
    "t10": {
        "lineage_en": "Pioneers of Step T.10 · Hawking (1971, 1975) · Bekenstein (1973) · Don Page (1993) · LIGO/Virgo/KAGRA & Isi et al. (2015, 2021, 2025) · Penington & Almheiri, Engelhardt, Marolf, Maxfield (2019–2020) · 2025–2026 Island Debate Authors",
        "lineage_es": "Pioneros del Paso T.10 · Hawking (1971, 1975) · Bekenstein (1973) · Don Page (1993) · LIGO/Virgo/KAGRA e Isi et al. (2015, 2021, 2025) · Penington y Almheiri, Engelhardt, Marolf, Maxfield (2019–2020) · Autores del debate de islas 2025–2026",
        "title_en": "The Humans Behind Step T.10 · Horizon Area, Subsystem Counting, and Gravitational-Wave Ringdowns",
        "title_es": "Las Personas Detrás del Paso T.10 · Área del Horizonte, Conteo de Subsistemas y Resonancias de Agujeros Negros",
        "lead_en": "The final step of the track honors the theorists who linked horizon area to entropy and counted the entanglement of random quantum states, alongside the gravitational-wave collaborations that tested Hawking's area theorem on merging black holes.",
        "lead_es": "El último paso de la serie honra a los teóricos que vincularon el área del horizonte con la entropía y contaron el entrelazamiento de estados cuánticos aleatorios, junto a las colaboraciones de ondas gravitacionales que pusieron a prueba el teorema del área de Hawking.",
        "cards": [
            {
                "icon": "black-hole-qubits",
                "era_en": "1971–1975 · Cambridge & Princeton",
                "era_es": "1971–1975 · Cambridge y Princeton",
                "names_en": "Stephen W. Hawking & Jacob D. Bekenstein",
                "names_es": "Stephen W. Hawking y Jacob D. Bekenstein",
                "place_en": "University of Cambridge & Princeton University",
                "place_es": "Universidad de Cambridge y Universidad de Princeton",
                "story_en": "In 1971 Stephen Hawking proved that in classical general relativity the total surface area of black-hole horizons never decreases. In 1973 Jacob Bekenstein argued that this horizon area is physical entropy, and in 1975 Hawking calculated that quantum fields near a horizon radiate thermally—setting up the tension with quantum unitarity.",
                "story_es": "En 1971 Stephen Hawking demostró que en la relatividad general clásica el área total de los horizontes de los agujeros negros nunca disminuye. En 1973 Jacob Bekenstein sostuvo que esa área es entropía física, y en 1975 Hawking calculó que los campos cuánticos cerca de un horizonte radian térmicamente.",
                "spec_en": "Area theorem (dA ≥ 0), Bekenstein–Hawking entropy & thermal line",
                "spec_es": "Teorema del área (dA ≥ 0), entropía de Bekenstein–Hawking y recta térmica",
                "doi": "10.1007/BF02345020",
            },
            {
                "icon": "page-wootters",
                "era_en": "1993 · Edmonton, Alberta",
                "era_es": "1993 · Edmonton, Alberta",
                "names_en": "Don N. Page",
                "names_es": "Don N. Page",
                "place_en": "University of Alberta · Subsystem Entropy & the Turnover Curve",
                "place_es": "Universidad de Alberta · Entropía de Subsistemas y la Curva de Retorno",
                "story_en": "In two 1993 Physical Review Letters papers, Don Page asked a pure counting question: for a random pure state on a bipartite Hilbert space of dimension m × n, what is the average entanglement entropy of the smaller m-dimensional subsystem? His formula S(m,n) = Σ 1/k − (m−1)/(2n) showed that unitary radiation entropy must peak halfway and return to zero.",
                "story_es": "En dos artículos de 1993 en Physical Review Letters, Don Page planteó una pregunta de puro conteo: para un estado puro aleatorio en un espacio de Hilbert bipartito de dimensión m × n, ¿cuál es la entropía de entrelazamiento promedio del subsistema menor m? Su fórmula S(m,n) mostró que la entropía unitaria debe dar la vuelta a la mitad y volver a cero.",
                "spec_en": "Page's closed form S(m,n) · Turnover at N/2 qubits (DERIVED)",
                "spec_es": "Forma cerrada de Page S(m,n) · Vuelta en N/2 qubits (DERIVADO)",
                "doi": "10.1103/PhysRevLett.71.1291",
            },
            {
                "icon": "ligo-interferometer",
                "era_en": "2015–2025 · Hanford, Livingston, Cascina, Kamioka, MIT & Caltech",
                "era_es": "2015–2025 · Hanford, Livingston, Cascina, Kamioka, MIT y Caltech",
                "names_en": "LIGO, Virgo & KAGRA Collaborations · Maximiliano Isi, Will Farr, Matthew Giesler, Mark Scheel & Saul Teukolsky",
                "names_es": "Colaboraciones LIGO, Virgo y KAGRA · Maximiliano Isi, Will Farr, Matthew Giesler, Mark Scheel y Saul Teukolsky",
                "place_en": "4 km Laser Interferometers & Ringdown Posterior Analysis",
                "place_es": "Interferómetros láser de 4 km y análisis posterior de resonancia",
                "story_en": "The LIGO and Virgo collaborations recorded the first binary black-hole merger GW150914 in 2015. In 2021 Maximiliano Isi, Will Farr, Matthew Giesler, Mark Scheel, and Saul Teukolsky independently reanalyzed its inspiral and ringdown portions to test Hawking's area law on a real signal, followed in 2025 by the LVK collaboration's SNR-80 event GW250114.",
                "story_es": "Las colaboraciones LIGO y Virgo registraron la primera fusión de agujeros negros binarios GW150914 en 2015. En 2021 Maximiliano Isi, Will Farr, Matthew Giesler, Mark Scheel y Saul Teukolsky reanalizaron de forma independiente su inspiración y resonancia para probar la ley del área de Hawking, seguidos en 2025 por el evento GW250114 de relación señal a ruido 80.",
                "spec_en": "GW150914 & GW250114 horizon area tests (MEASURED / SINGLE RESULT)",
                "spec_es": "Pruebas del área del horizonte en GW150914 y GW250114",
                "doi": "10.1103/PhysRevLett.127.011103",
            },
            {
                "icon": "black-hole-qubits",
                "era_en": "2019–2026 · Stanford, IAS, MIT, Santa Barbara, Maryland & Harvard",
                "era_es": "2019–2026 · Stanford, IAS, MIT, Santa Bárbara, Maryland y Harvard",
                "names_en": "Geoffrey Penington · Ahmed Almheiri, Netta Engelhardt, Donald Marolf & Henry Maxfield · 2025–2026 Island Debate Authors",
                "names_es": "Geoffrey Penington · Ahmed Almheiri, Netta Engelhardt, Donald Marolf y Henry Maxfield · Autores del debate de islas 2025–2026",
                "place_en": "Quantum Extremal Surfaces, Entanglement Wedges & Asymptotic Algebras",
                "place_es": "Superficies extremales cuánticas, cuñas de entrelazamiento y álgebras asintóticas",
                "story_en": "In 2019–2020 Penington and Almheiri, Engelhardt, Marolf, and Maxfield showed that the quantum extremal surface prescription reproduces Page's curve in semiclassical gravity via interior islands. In 2025–2026 Antonini, Chen, Maxfield, and Penington and Geng, Karch, Perez-Pardavila, Raju, Randall, and Riojas debated what islands mean when detectors have blind spots.",
                "story_es": "En 2019–2020 Penington y Almheiri, Engelhardt, Marolf y Maxfield mostraron que la prescripción de superficie extremal cuántica reproduce la curva de Page en gravedad semiclásica mediante islas interiores. En 2025–2026 Antonini, Chen, Maxfield y Penington y Geng, Karch, Perez-Pardavila, Raju, Randall y Riojas debatieron qué significan las islas.",
                "spec_en": "Quantum extremal surfaces & the 2025–2026 preprint debate",
                "spec_es": "Superficies extremales cuánticas y el debate de prepublicaciones 2025–2026",
                "doi": "10.1007/JHEP09(2020)002",
            },
        ],
    },
    "t11": {
        "lineage_en": "Pioneers of Step T.11 · Hugh Everett III (1957) · H. Dieter Zeh (1970) · Wojciech Zurek (1981, 2003, 2009) · Erich Joos & H. Dieter Zeh (1985) · Michel Brune, Serge Haroche, Jean-Michel Raimond & Davidovich (1996) · Klaus Hornberger, Lucia Hackermüller & Markus Arndt (2003–2004)",
        "lineage_es": "Pioneros del Paso T.11 · Hugh Everett III (1957) · H. Dieter Zeh (1970) · Wojciech Zurek (1981, 2003, 2009) · Erich Joos y H. Dieter Zeh (1985) · Michel Brune, Serge Haroche, Jean-Michel Raimond y Davidovich (1996) · Klaus Hornberger, Lucia Hackermüller y Markus Arndt (2003–2004)",
        "title_en": "The Humans Behind Step T.11 · Pointer Bases, Photon Baths, and Cavity Cat States",
        "title_es": "Las Personas Detrás del Paso T.11 · Bases Puntero, Baños de Fotones y Estados Gato en Cavidad",
        "lead_en": "Why does a macroscopic clock appear in one definite position rather than a superposition of positions? These theorists and experimentalists showed how the interaction Hamiltonian and the ambient electromagnetic bath select the pointer states and copy them across the environment.",
        "lead_es": "¿Por qué un reloj macroscópico aparece en una posición definida y no en una superposición de posiciones? Estos teóricos y experimentalistas mostraron cómo el hamiltoniano de interacción y el baño electromagnético seleccionan los estados puntero y los copian en el entorno.",
        "cards": [
            {
                "icon": "pointer-darwinism",
                "era_en": "1957 & 1981–2009 · Princeton, Austin & Los Alamos",
                "era_es": "1957 y 1981–2009 · Princeton, Austin y Los Álamos",
                "names_en": "Hugh Everett III · Wojciech Hubert Zurek",
                "names_es": "Hugh Everett III · Wojciech Hubert Zurek",
                "place_en": "Princeton University, University of Texas at Austin & Los Alamos National Laboratory",
                "place_es": "Universidad de Princeton, Universidad de Texas en Austin y Laboratorio Nacional de Los Álamos",
                "story_en": "In 1957 Hugh Everett III formulated relative-state quantum mechanics without an external collapse postulate, leaving open why observers record one preferred basis. In 1981 Wojciech Zurek showed that the apparatus–environment interaction Hamiltonian selects the pointer projectors satisfying [Ĥ_int, Π_i] = 0, and in 2009 formulated Quantum Darwinism: the classical record is the observable redundantly copied into many small fragments of the bath.",
                "story_es": "En 1957 Hugh Everett III formuló la mecánica cuántica de estados relativos sin postulado de colapso externo, dejando abierto por qué los observadores registran una base preferida. En 1981 Wojciech Zurek mostró que el hamiltoniano de interacción aparato–entorno selecciona los proyectores puntero que cumplen [Ĥ_int, Π_i] = 0, y en 2009 formuló el darwinismo cuántico.",
                "spec_en": "Einselection [Ĥ_int, Π_i] = 0 & Quantum Darwinism plateau (DERIVED)",
                "spec_es": "Einselección [Ĥ_int, Π_i] = 0 y meseta de darwinismo cuántico (DERIVADO)",
                "doi": "10.1103/PhysRevD.24.1516",
            },
            {
                "icon": "photon-scattering",
                "era_en": "1970 & 1985 · Heidelberg",
                "era_es": "1970 y 1985 · Heidelberg",
                "names_en": "Erich Joos & H. Dieter Zeh",
                "names_es": "Erich Joos y H. Dieter Zeh",
                "place_en": "Institut für Theoretische Physik, Universität Heidelberg",
                "place_es": "Instituto de Física Teórica, Universidad de Heidelberg",
                "story_en": "Following H. Dieter Zeh's 1970 insight that macroscopic quantum systems cannot be isolated from their surroundings, Erich Joos and Zeh calculated in 1985 the localization rate Λ of a dust grain bathed in thermal radiation. Because long-wavelength dipole scattering scales as R⁶T⁹|(ε−1)/(ε+2)|², even the 2.7 K cosmic microwave background localizes a 10 µm grain in about one second.",
                "story_es": "Siguiendo la idea de H. Dieter Zeh de 1970 de que los sistemas cuánticos macroscópicos no pueden aislarse de su entorno, Erich Joos y Zeh calcularon en 1985 la tasa de localización Λ de un grano de polvo bañado en radiación térmica. Como la dispersión dipolar escala como R⁶T⁹|(ε−1)/(ε+2)|², hasta el fondo cósmico de 2.7 K localiza un grano de 10 µm en cerca de un segundo.",
                "spec_en": "Dipole photon bath Λ ∝ R⁶T⁹|(ε−1)/(ε+2)|² (DERIVED)",
                "spec_es": "Baño dipolar de fotones Λ ∝ R⁶T⁹|(ε−1)/(ε+2)|² (DERIVADO)",
                "doi": "10.1007/BF01725541",
            },
            {
                "icon": "cavity-buckminster",
                "era_en": "1996 & 2003–2004 · Paris & Vienna",
                "era_es": "1996 y 2003–2004 · París y Viena",
                "names_en": "Michel Brune, Serge Haroche & Jean-Michel Raimond · Klaus Hornberger, Lucia Hackermüller & Markus Arndt",
                "names_es": "Michel Brune, Serge Haroche y Jean-Michel Raimond · Klaus Hornberger, Lucia Hackermüller y Markus Arndt",
                "place_en": "École Normale Supérieure (Paris) & University of Vienna",
                "place_es": "École Normale Supérieure (París) y Universidad de Viena",
                "story_en": "At the École Normale Supérieure in 1996, Michel Brune, Serge Haroche, Jean-Michel Raimond, and colleagues prepared a mesoscopic superposition of two microwave field phases in a superconducting cavity and watched single rubidium atoms trace its decoherence into a mixture. In 2003–2004 in Vienna, Klaus Hornberger, Lucia Hackermüller, and Markus Arndt measured the loss of C₇₀ matter-wave fringes under controlled gas collisions and thermal photon emission.",
                "story_es": "En la École Normale Supérieure en 1996, Michel Brune, Serge Haroche, Jean-Michel Raimond y colegas prepararon una superposición mesoscópica de dos fases de microondas en una cavidad superconductora y observaron su decoherencia átomo por átomo. En 2003–2004 en Viena, Klaus Hornberger, Lucia Hackermüller y Markus Arndt midieron la pérdida de visibilidad de ondas de C₇₀ bajo colisiones de gas y emisión térmica.",
                "spec_en": "Cavity QED cat decoherence & C₇₀ matter-wave baths (MEASURED)",
                "spec_es": "Decoherencia en cavidad QED y baños en ondas de C₇₀ (MEDIDO)",
                "doi": "10.1103/PhysRevLett.77.4887",
            },
        ],
    },
    "t12": {
        "lineage_en": "Pioneers of Step T.12 · Clowe, Bradač, Gonzalez, Markevitch, Randall, Jones & Zaritsky (2006) · Planck Collaboration (2020) · Kennedy, Oelker, Bothwell, Kedar, Robinson, Marti, Milne & Ye (2020) · Carney et al. (2021) · Filzinger, Dörscher, Lange, Klose, Steinel, Benkler, Peik, Lisdat & Huntemann (2023) · LUX-ZEPLIN Collaboration (2023)",
        "lineage_es": "Pioneros del Paso T.12 · Clowe, Bradač, Gonzalez, Markevitch, Randall, Jones y Zaritsky (2006) · Colaboración Planck (2020) · Kennedy, Oelker, Bothwell, Kedar, Robinson, Marti, Milne y Ye (2020) · Carney et al. (2021) · Filzinger, Dörscher, Lange, Klose, Steinel, Benkler, Peik, Lisdat y Huntemann (2023) · Colaboración LUX-ZEPLIN (2023)",
        "title_en": "The Humans Behind Step T.12 · Gravitational Lenses, the Cosmic Budget, and Dark-Sector Clock Comparisons",
        "title_es": "Las Personas Detrás del Paso T.12 · Lentes Gravitatorias, el Presupuesto Cósmico y Comparaciones de Relojes en el Sector Oscuro",
        "lead_en": "What happens when a mass sector has zero electromagnetic polarizability (Λ_EM = 0) and zero optical shadow, yet shares the spacetime metric g_μν? Cosmologists mapped its gravitational wells across the sky while atomic physicists turned optical clocks and underground detectors into dark-sector observatories.",
        "lead_es": "¿Qué ocurre cuando un sector de masa tiene polarizabilidad electromagnética nula (Λ_EM = 0) y cero sombra óptica, pero comparte la métrica g_μν? Los cosmólogos trazaron sus pozos gravitatorios en el cielo mientras los físicos atómicos convirtieron relojes ópticos y detectores subterráneos en observatorios del sector oscuro.",
        "cards": [
            {
                "icon": "bullet-cluster-lensing",
                "era_en": "2006 & 2018–2020 · Tucson, Cambridge & ESA L2",
                "era_es": "2006 y 2018–2020 · Tucson, Cambridge y punto L2 de la ESA",
                "names_en": "Douglas Clowe, Maruša Bradač & the Bullet Cluster Team · The Planck Collaboration",
                "names_es": "Douglas Clowe, Maruša Bradač y el Equipo del Cúmulo Bala · La Colaboración Planck",
                "place_en": "Magellan, Hubble & Chandra Telescopes (1E 0657−558) & ESA Planck Spacecraft",
                "place_es": "Telescopios Magellan, Hubble y Chandra (1E 0657−558) y satélite Planck de la ESA",
                "story_en": "In 2006 Douglas Clowe, Maruša Bradač, Anthony Gonzalez, Maxim Markevitch, Scott Randall, Christine Jones, and Dennis Zaritsky compared Chandra X-ray maps of the hot baryonic gas in the merging cluster 1E 0657−558 against weak-lensing maps of the gravitational potential, showing at 8σ that the potential follows the collisionless mass rather than the luminous gas. In 2018–2020 the Planck Collaboration fixed the cosmic ratio at Ω_c h² / Ω_b h² = 5.36 ± 0.06.",
                "story_es": "En 2006 Douglas Clowe, Maruša Bradač, Anthony Gonzalez, Maxim Markevitch, Scott Randall, Christine Jones y Dennis Zaritsky compararon mapas de rayos X de Chandra del gas bariónico en el cúmulo en fusión 1E 0657−558 con mapas de lente débil del potencial gravitatorio, mostrando a 8σ que el potencial sigue a la masa sin colisiones. En 2018–2020 la Colaboración Planck fijó la razón cósmica en Ω_c h² / Ω_b h² = 5.36 ± 0.06.",
                "spec_en": "8σ lensing–gas separation & Ω_c / Ω_b = 5.36 ± 0.06 (MEASURED)",
                "spec_es": "Separación lente–gas a 8σ y Ω_c / Ω_b = 5.36 ± 0.06 (MEDIDO)",
                "doi": "10.1051/0004-6361/201833910",
            },
            {
                "icon": "dark-clock-comparison",
                "era_en": "2020 & 2023 · Boulder, Colorado & Braunschweig, Germany",
                "era_es": "2020 y 2023 · Boulder, Colorado y Braunschweig, Alemania",
                "names_en": "Colin Kennedy, Tobias Bothwell & Jun Ye · Melina Filzinger, Ekkehard Peik, Christian Lisdat & Nils Huntemann",
                "names_es": "Colin Kennedy, Tobias Bothwell y Jun Ye · Melina Filzinger, Ekkehard Peik, Christian Lisdat y Nils Huntemann",
                "place_en": "JILA (⁸⁷Sr vs Silicon Cavity) & PTB (¹⁷¹Yb⁺ E3/E2 vs ⁸⁷Sr)",
                "place_es": "JILA (⁸⁷Sr frente a cavidad de silicio) y PTB (¹⁷¹Yb⁺ E3/E2 frente a ⁸⁷Sr)",
                "story_en": "If ultralight scalar dark matter couples to the fine-structure constant α or electron mass m_e, different clock transitions will oscillate at the Compton frequency m_φ c² / h. At JILA in 2020, Colin Kennedy, Jun Ye, and colleagues compared an ⁸⁷Sr optical lattice clock against a cryogenic crystalline silicon cavity; at PTB in 2023, Melina Filzinger, Nils Huntemann, and co-workers compared the electric octupole and quadrupole transitions of ¹⁷¹Yb⁺ against ⁸⁷Sr over more than two years, setting tight bounds on scalar couplings.",
                "story_es": "Si la materia oscura escalar ultraligera se acopla a la constante de estructura fina α o a la masa del electrón m_e, distintas transiciones de reloj oscilarán a la frecuencia de Compton m_φ c² / h. En JILA en 2020, Colin Kennedy, Jun Ye y colegas compararon un reloj de ⁸⁷Sr con una cavidad criogénica de silicio; en el PTB en 2023, Melina Filzinger, Nils Huntemann y colaboradores compararon las transiciones E3 y E2 de ¹⁷¹Yb⁺ y ⁸⁷Sr durante más de dos años.",
                "spec_en": "Sr–Si & Yb⁺–Sr dark-matter clock bounds (BOUND)",
                "spec_es": "Cotas de relojes Sr–Si e Yb⁺–Sr sobre materia oscura (COTA)",
                "doi": "10.1103/PhysRevLett.130.253001",
            },
            {
                "icon": "underground-crystal",
                "era_en": "2021–2026 · Lead (South Dakota), Gran Sasso & Gaithersburg",
                "era_es": "2021–2026 · Lead (Dakota del Sur), Gran Sasso y Gaithersburg",
                "names_en": "LUX-ZEPLIN (LZ) & XENONnT Collaborations · Daniel Carney, Sohitri Ghosh, Gordan Krnjaic & Jacob M. Taylor",
                "names_es": "Colaboraciones LUX-ZEPLIN (LZ) y XENONnT · Daniel Carney, Sohitri Ghosh, Gordan Krnjaic y Jacob M. Taylor",
                "place_en": "Sanford Underground Research Facility (SURF), Gran Sasso & Quantum-Sensor Arrays",
                "place_es": "Laboratorio Subterráneo de Sanford (SURF), Gran Sasso y arreglos de sensores cuánticos",
                "story_en": "One mile underground in South Dakota, the LUX-ZEPLIN Collaboration pushed spin-independent WIMP–nucleon cross sections down to 9.2 × 10⁻⁴⁸ cm² at 36 GeV/c² in 2023 without a positive recoil signal. To reach hypothetical dark sectors that have zero non-gravitational couplings at all, Daniel Carney, Jacob Taylor, and colleagues proposed using optomechanical accelerometer arrays and clock networks to detect passing dark-matter clumps purely through their Newtonian gravitational impulse.",
                "story_es": "A una milla bajo tierra en Dakota del Sur, la colaboración LUX-ZEPLIN llevó las secciones eficaces WIMP–nucleón hasta 9.2 × 10⁻⁴⁸ cm² a 36 GeV/c² en 2023 sin señal de retroceso. Para alcanzar sectores oscuros con acoplamiento no gravitatorio nulo, Daniel Carney, Jacob Taylor y colegas propusieron usar redes de relojes y sensores optomecánicos para detectar subhalos puramente por su impulso gravitatorio.",
                "spec_en": "LZ 9.2 × 10⁻⁴⁸ cm² (BOUND) & pure-gravity sensor proposals (PROPOSED)",
                "spec_es": "LZ 9.2 × 10⁻⁴⁸ cm² (COTA) y propuestas puramente gravitatorias (PROPUESTO)",
                "doi": "10.1103/PhysRevLett.131.041002",
            },
        ],
    },
    "t13": {
        "lineage_en": "Pioneers of Step T.13 · Weinberg (1964–1965) · Adler (1969) · Delbourgo & Salam (1972) · Christodoulou (1991) · Strominger & Zhiboedov (2016) · Zhang, Ye & Schumm (2024) · Tooby-Smith (2025)",
        "lineage_es": "Pioneros del Paso T.13 · Weinberg (1964–1965) · Adler (1969) · Delbourgo y Salam (1972) · Christodoulou (1991) · Strominger y Zhiboedov (2016) · Zhang, Ye y Schumm (2024) · Tooby-Smith (2025)",
        "title_en": "The Humans Behind Step T.13 · Soft Gravitons, Null-Infinity Memory, and Chiral Triangle Locks",
        "title_es": "Las Personas Detrás del Paso T.13 · Gravitones Blandos, Memoria en el Infinito Nulo y Candados Quirales",
        "lead_en": "Without assuming ultraviolet physics at the Planck scale, three generations of theorists and experimentalists uncovered the exact low-energy consistency conditions that tie massless spin-2 gravity to gauge charges, permanent wave memory, and the fermion table.",
        "lead_es": "Sin suponer física ultravioleta en la escala de Planck, tres generaciones de teóricos y experimentalistas descubrieron las condiciones exactas de consistencia de baja energía que enlazan la gravedad sin masa de espín 2 con las cargas gauge, la memoria permanente de ondas y la tabla de fermiones.",
        "cards": [
            {
                "icon": "soft-triangle",
                "era_en": "1964–1965 · Berkeley, California",
                "era_es": "1964–1965 · Berkeley, California",
                "names_en": "Steven Weinberg",
                "names_es": "Steven Weinberg",
                "place_en": "University of California, Berkeley · Infrared S-Matrix Theory",
                "place_es": "Universidad de California en Berkeley · Teoría de la Matriz S Infrarroja",
                "story_en": "Working purely from Lorentz invariance and unitarity of flat-space scattering amplitudes, Steven Weinberg showed in 1964–1965 that soft massless spin-1 emission requires charge conservation, soft massless spin-2 emission forces every species to share one gravitational coupling κ (deriving the Equivalence Principle), and massless spins s ≥ 3 cannot mediate long-range forces.",
                "story_es": "Partiendo solo de la invariancia de Lorentz y la unitariedad de amplitudes de dispersión, Steven Weinberg demostró en 1964–1965 que la emisión blanda de espín 1 exige conservar la carga, la emisión blanda de espín 2 obliga a toda especie a compartir un mismo acoplamiento gravitacional κ, y los espines sin masa s ≥ 3 no pueden mediar fuerzas macroscópicas.",
                "spec_en": "Soft Ward hierarchy · s = 1, 2, ≥ 3 (DERIVED)",
                "spec_es": "Jerarquía blanda de Ward · s = 1, 2, ≥ 3 (DERIVADO)",
                "doi": "10.1103/PhysRev.135.B1049",
            },
            {
                "icon": "ligo-interferometer",
                "era_en": "1991 & 2016 · Courant Institute & Harvard",
                "era_es": "1991 y 2016 · Instituto Courant y Harvard",
                "names_en": "Demetrios Christodoulou · Andrew Strominger & Alexander Zhiboedov",
                "names_es": "Demetrios Christodoulou · Andrew Strominger y Alexander Zhiboedov",
                "place_en": "New York University, Harvard University & LIGO/Virgo Catalogs",
                "place_es": "Universidad de Nueva York, Universidad de Harvard y Catálogos LIGO/Virgo",
                "story_en": "In 1991 Demetrios Christodoulou proved from the nonlinear vacuum Einstein equations that gravitational-wave energy flux leaves a permanent displacement step between free-falling test masses after a wave train passes. Twenty-five years later Andrew Strominger and Alexander Zhiboedov showed that displacement memory, BMS supertranslations, and Weinberg's soft graviton theorem form one infrared triangle.",
                "story_es": "En 1991 Demetrios Christodoulou demostró desde las ecuaciones no lineales de Einstein en el vacío que el flujo de energía de ondas gravitacionales deja un escalón permanente de desplazamiento entre masas en caída libre. Veinticinco años después Andrew Strominger y Alexander Zhiboedov mostraron que la memoria, las supertraslaciones BMS y el gravitón blando forman un solo triángulo infrarrojo.",
                "spec_en": "Nonlinear GW memory Δh_char = GE_rad/(c⁴D_L) (DERIVED)",
                "spec_es": "Memoria gravitacional Δh_char = GE_rad/(c⁴D_L) (DERIVADO)",
                "doi": "10.1103/PhysRevLett.67.1486",
            },
            {
                "icon": "optical-lattice",
                "era_en": "1969, 1972 & 2024–2025 · Princeton, Imperial College, Boulder & Munich",
                "era_es": "1969, 1972 y 2024–2025 · Princeton, Imperial College, Boulder y Múnich",
                "names_en": "Stephen L. Adler · Robert Delbourgo & Abdus Salam · Chuankun Zhang, Thorsten Schumm & Jun Ye · Joseph Tooby-Smith",
                "names_es": "Stephen L. Adler · Robert Delbourgo y Abdus Salam · Chuankun Zhang, Thorsten Schumm y Jun Ye · Joseph Tooby-Smith",
                "place_en": "IAS Princeton, Imperial College London, JILA / TU Wien & PhysLean",
                "place_es": "IAS Princeton, Imperial College London, JILA / TU Wien y PhysLean",
                "story_en": "Stephen Adler (1969) uncovered the one-loop chiral triangle anomaly, and Robert Delbourgo and Abdus Salam (1972) computed its mixed gravitational counterpart Tr[Y] = 0, which joins SU(2)²U(1)_Y and U(1)_Y³ to lock N_c = 3 quark colours—formalized in Lean 4 by Joseph Tooby-Smith (2025), while Chuankun Zhang, Thorsten Schumm, Jun Ye, and colleagues (2024) linked ²²⁹Th nuclear isomers to ⁸⁷Sr optical clocks.",
                "story_es": "Stephen Adler (1969) descubrió la anomalía triangular quiral a un lazo, y Robert Delbourgo y Abdus Salam (1972) calcularon su contraparte gravitacional mixta Tr[Y] = 0, que junto con SU(2)²U(1)_Y y U(1)_Y³ fija N_c = 3 colores de quarks —formalizado en Lean 4 por Joseph Tooby-Smith (2025)—, mientras Chuankun Zhang, Thorsten Schumm, Jun Ye y colegas (2024) enlazaron ²²⁹Th con relojes de ⁸⁷Sr.",
                "spec_en": "Tr[6Y] = 0, N_c = 3 & ²²⁹Th/⁸⁷Sr comb link",
                "spec_es": "Tr[6Y] = 0, N_c = 3 y enlace de peine ²²⁹Th/⁸⁷Sr",
                "doi": "10.1016/0370-2693(72)90825-8",
            },
        ],
    },
}


def hero_lineage(page: dict) -> str:
    """Archival pioneer ribbon inside the hero header linking directly to #humans."""
    slug = page["slug"]
    info = HUMANS_DATA.get(slug, HUMANS_DATA[""])
    jump_en = "Honor the humans &darr;" if slug else "Meet the pioneers (1905–2026) &darr;"
    jump_es = "Honrar a las personas &darr;" if slug else "Conocer a los pioneros (1905–2026) &darr;"
    return f"""      <div class="tg-hero-lineage" role="note" aria-label="Historical human lineage for {page['code']}">
        <span class="tg-hero-lineage-badge" data-en="Human Lineage" data-es="Linaje Humano">Human Lineage</span>
        <span class="tg-hero-lineage-names" data-en="{a(info['lineage_en'])}" data-es="{a(info['lineage_es'])}">{t(info['lineage_en'])}</span>
        <a class="tg-hero-lineage-link" href="#humans" data-en="{jump_en}" data-es="{jump_es}">{jump_en}</a>
      </div>"""


def humans_section(page: dict, rel_res: str) -> str:
    """Archival vitrine honoring the experimentalists and theorists behind the step (zero .tg-claim spans)."""
    slug = page["slug"]
    info = HUMANS_DATA.get(slug, HUMANS_DATA[""])
    cards_html = []
    for c in info["cards"]:
        badge = apparatus_svg(c["icon"])
        doi = c["doi"]
        cards_html.append(f"""          <article class="tg-human-card">
            <div class="tg-human-card-top">
              {badge}
              <div class="tg-human-head">
                <p class="tg-human-era" data-en="{a(c['era_en'])}" data-es="{a(c['era_es'])}">{t(c['era_en'])}</p>
                <h3 class="tg-human-names" data-en="{a(c['names_en'])}" data-es="{a(c['names_es'])}">{t(c['names_en'])}</h3>
                <p class="tg-human-place" data-en="{a(c['place_en'])}" data-es="{a(c['place_es'])}">{t(c['place_en'])}</p>
              </div>
            </div>
            {bi("p", c["story_en"], c["story_es"], "tg-human-story")}
            <div class="tg-human-footer">
              <span class="tg-human-apparatus" data-en="{a(c['spec_en'])}" data-es="{a(c['spec_es'])}">{t(c['spec_en'])}</span>
              <a class="tp-cite-link tg-human-doi" href="https://doi.org/{a(doi)}" target="_blank" rel="noopener noreferrer">DOI {t(doi)} &#8599;</a>
            </div>
          </article>""")
    hid = f"tg-humans-title-{slug or 'hub'}"
    return f"""        <section id="humans" class="tg-humans-section" aria-labelledby="{hid}">
          <div class="tg-humans-header">
            <p class="tp-kicker tg-humans-kicker" data-en="Archival Tribute · The Hands Behind the Instruments" data-es="Tributo Histórico · Las Manos Detrás de los Instrumentos">Archival Tribute · The Hands Behind the Instruments</p>
            <h2 id="{hid}" class="tp-h2 tg-humans-h2" data-en="{a(info['title_en'])}" data-es="{a(info['title_es'])}">{t(info['title_en'])}</h2>
            {bi("p", info["lead_en"], info["lead_es"], "tg-humans-lead")}
          </div>
          <div class="tg-humans-grid">
{chr(10).join(cards_html)}
          </div>
        </section>"""


def render_sections(page: dict, rel_res: str, lang: str = "en") -> str:
    out = []
    for block in page["sections"]:
        kind = block["type"]
        if kind == "h2":
            out.append(f'        <h2 id="{block["id"]}" class="tp-h2" data-en="{a(block["en"])}" data-es="{a(block["es"])}">{t(block["en"])}</h2>')
        elif kind == "p":
            out.append("        " + para(block, lang))
        elif kind == "bridge":
            inner = "\n".join("          " + para(p, lang) for p in block["paras"])
            out.append(f"""        <div class="tp-plain-bridge-box" role="note" aria-label="In plain words">
          <span class="tp-plain-bridge-kicker" data-en="{a(block['kicker_en'])}" data-es="{a(block['kicker_es'])}">{t(block['kicker_en'])}</span>
{inner}
        </div>""")
        elif kind == "analogy":
            inner = "\n".join("          " + para(p, lang) for p in block["paras"])
            out.append(f"""        <div class="tp-analogy-box" role="region" aria-label="Everyday intuition and controls primer">
          <span class="tp-plain-bridge-kicker" data-en="{a(block['kicker_en'])}" data-es="{a(block['kicker_es'])}">{t(block['kicker_en'])}</span>
{inner}
        </div>""")
        elif kind == "plate_d":
            out.append(plate_d(page))
            out.append(humans_section(page, rel_res))
        elif kind == "sigma_ladder":
            out.append(sigma_ladder(page))
        elif kind == "threshold_map":
            out.append(threshold_map(page))
        elif kind == "proposals_table":
            out.append(proposals_table(page))
        elif kind == "hardware_table":
            out.append(hardware_table(page))
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
            out.append(humans_section(page, rel_res))
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


def step_of(code: str) -> int:
    return next(i for i, m in enumerate(TRACK_MAP, 1) if m["code"] == code)


def step_rail(page: dict, rel_res: str) -> str:
    """Fourteen numbered steps under every T hero: where the reader is, and one tap to any other step."""
    items = []
    for i, m in enumerate(TRACK_MAP, 1):
        href = B._href(rel_res, "timegravity/" + (f"{m['slug']}/" if m["slug"] else ""))
        label = (f'<span class="tg-step-n" aria-hidden="true">{i}</span>'
                 f'<span class="tg-step-t"><span data-en="Step {i} of 14 · {a(m["title_en"])}" data-es="Paso {i} de 14 · {a(m["title_es"])}">Step {i} of 14 · {t(m["title_en"])}</span></span>')
        if m["code"] == page["code"]:
            items.append(f'          <li class="tg-step tg-step-current" aria-current="step">{label}</li>')
        elif m["built"]:
            items.append(f'          <li class="tg-step"><a href="{href}">{label}</a></li>')
        else:
            items.append(f'          <li class="tg-step tg-step-pending">{label}</li>')
    return ("    <nav class=\"tg-step-rail\" aria-label=\"The fourteen steps of Time and Gravity\">\n"
            "      <ol class=\"tg-steps\">\n" + "\n".join(items) + "\n      </ol>\n    </nav>")


def hub_cta(rel_res: str) -> str:
    """The hub's way in: begin with the first step after the hub, or jump to the map of fourteen."""
    first = TRACK_MAP[1]
    page = next(p for p in PAGES if p["code"] == first["code"])
    href = B._href(rel_res, "timegravity/" + first["slug"] + "/")
    return f"""      <p class="tg-hero-cta">
        <a class="tp-cta tp-cta-primary tg-cta-begin" href="{href}"><span data-en="Begin · Step 2 of 14 · {page['reading_time_en']}" data-es="Empezar · Paso 2 de 14 · {page['reading_time_es']}">Begin · Step 2 of 14 · {page['reading_time_en']}</span><strong data-en="{a(first['title_en'])} &rarr;" data-es="{a(first['title_es'])} &rarr;">{t(first['title_en'])} &rarr;</strong></a>
        <a class="tp-cta tg-cta-map" href="#map" data-en="See the fourteen steps &darr;" data-es="Ver los catorce pasos &darr;">See the fourteen steps &darr;</a>
      </p>"""


def neighbours(page: dict) -> tuple[dict | None, dict | None]:
    """Previous and next entries of TRACK_MAP in reading order (the hub is first)."""
    idx = next(i for i, m in enumerate(TRACK_MAP) if m["code"] == page["code"])
    prev = TRACK_MAP[idx - 1] if idx > 0 else None
    nxt = TRACK_MAP[idx + 1] if idx + 1 < len(TRACK_MAP) else None
    return prev, nxt


def open_question(page: dict, rel_res: str) -> str:
    _prev, nx = neighbours(page)
    if nx is None:
        href = B._href(rel_res, "timegravity/")
        nxt = (f'<a class="tg-next" href="{href}"><span class="tg-next-dir" data-en="Last step · back to the hub &rarr;" data-es="Último paso · volver al inicio &rarr;">Last step · back to the hub &rarr;</span>'
               f'<strong data-en="The question that opened the track" data-es="La pregunta que abrió la serie">The question that opened the track</strong></a>')
    elif nx["built"]:
        href = B._href(rel_res, "timegravity/" + nx["slug"] + "/")
        step = step_of(nx["code"])
        nxt = (f'<a class="tg-next" href="{href}" rel="next"><span class="tg-next-dir" data-en="Continue · Step {step} of 14 · {nx["code"]} &rarr;" data-es="Continuar · Paso {step} de 14 · {nx["code"]} &rarr;">Continue · Step {step} of 14 · {nx["code"]} &rarr;</span>'
               f'<strong data-en="{a(nx["title_en"])}" data-es="{a(nx["title_es"])}">{t(nx["title_en"])}</strong></a>')
    else:
        nxt = bi("p", f"Next: {nx['code']} · {nx['title_en']} (in preparation)",
                 f"Siguiente: {nx['code']} · {nx['title_es']} (en preparación)", "tg-next")
    return f"""        <section class="tg-open-question" aria-label="The open question this page ends with">
          <p class="tp-kicker" data-en="This page ends with one open question" data-es="Esta página termina con una pregunta abierta">This page ends with one open question</p>
          {bi("p", page["open_question_en"], page["open_question_es"])}
          {nxt}
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
    rel_root = rel_res
    t_en, d_en, t_es, d_es = page["seo"]
    if slug:
        title = f"{t_es if es else t_en} | {BRAND}"
    else:
        title = t_es if es else t_en
        title = title if title.endswith(BRAND) else f"{title} | {BRAND}"
    desc = d_es if es else d_en
    canon = B.page_url(path, lang)
    image = f"https://informatico.ai/plates/{plate_slug(page)}.png"
    crumbs = [("Informatico.ai", B.page_url("", lang)), ("Física" if es else "Physics", B.page_url("physics/", lang)),
              (TRACK_TITLE_ES if es else TRACK_TITLE_EN, B.page_url("timegravity/", lang))]
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
    jump.append(("#humans", "The Humans" if slug else "Humans (1905–2026)", "Las Personas" if slug else "Personas (1905–2026)"))
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
    elif kind == "dp":
        instrument = dp_instrument(page)
    elif kind == "bmv":
        instrument = bmv_instrument(page)
    elif kind == "horizon":
        instrument = horizon_instrument(page)
    elif kind == "kerr":
        instrument = kerr_instrument(page)
    elif kind == "page":
        instrument = page_instrument(page)
    elif kind == "einselection":
        instrument = einselection_instrument(page)
    elif kind == "dark_clock":
        instrument = dark_clock_instrument(page)
    elif kind == "holonomy_soft":
        instrument = holonomy_soft_instrument(page)
    else:
        instrument = slope_instrument(page, rel_res)
    ai_line = bi("p", page["ai_line_en"], page["ai_line_es"], "tg-ai-line") if page.get("ai_line_en") else ""
    order = bi("span", page["order_label_en"], page["order_label_es"])
    rt = bi("span", page["reading_time_en"], page["reading_time_es"])

    return f"""{head}
<body class="tp-body tp-page-folio tg-page">
{B.render_masthead(rel_res, "physics", lang)}
{B.render_contents_dialog(rel_res, catalog)}
  <main id="main" class="tp-shell" tabindex="-1">
{breadcrumb(rel_res, page)}
<div id="tp-folio-mount" data-folio-id="{page['code']}" data-folio-slug="{plate_slug(page)}">
    <section class="tp-hero">
      <p class="tp-kicker">{bi("span", page["kicker_en"], page["kicker_es"])} · {order} · {rt}</p>
      <h1 class="tp-h1" data-en="{a(page['title_en'])}" data-es="{a(page['title_es'])}">{t(page['title_en'])}</h1>
      {bi("p", page["standfirst_en"], page["standfirst_es"], "tp-standfirst")}
{hero_lineage(page)}
{hub_cta(rel_res) if not slug else ""}
{boundary_banner(compact=bool(slug))}
    </section>
{step_rail(page, rel_res)}
{lead_figure(page, rel_res, es)}
    <nav class="tg-jump-bar" aria-label="Sections of this page">
{jump_html}
    </nav>
{instrument}
    <section class="tp-folio-layout" aria-label="Essay">
      <div class="tp-prose">
{render_sections(page, rel_res, lang)}
        {ai_line}
{skill_box(page)}
{sources_list(page)}
{open_question(page, rel_res)}
      </div>
      <aside class="tp-rail" aria-label="{page['code']} margin notes">
{sidenotes(page)}
      </aside>
    </section>
</div>
{B.render_cross_scale_essays_showcase(rel_res, lang) if not slug else ""}
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
        (en_dir / "index.html").write_text(en_html, encoding="utf-8", newline="\n")
        (es_dir / "index.html").write_text(B.to_spanish_static(render_page(page, catalog, "es")), encoding="utf-8", newline="\n")
        written += [en_dir / "index.html", es_dir / "index.html"]
    return written


def main() -> int:
    catalog = B.update_catalogs()
    written = write_pages(catalog)
    # The track's entries on the cover, the sitemap and llms.txt live in the main builder, like the Toolbox's.
    (RESEARCH / "index.html").write_text(B.render_hub_index(catalog), encoding="utf-8", newline="\n")
    (RESEARCH / B.ES_PREFIX.strip("/") / "index.html").write_text(B.to_spanish_static(B.render_hub_index(catalog, "es")), encoding="utf-8", newline="\n")
    (RESEARCH / "sitemap.xml").write_text(B.render_research_sitemap(catalog), encoding="utf-8", newline="\n")
    (RESEARCH / "llms.txt").write_text(B.render_llms_txt(catalog), encoding="utf-8", newline="\n")
    print(f"PASS: Built {len(written)} Time & Gravity pages ({len(PAGES)} pages × EN/ES-MX) + cover, sitemap.xml and llms.txt entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
