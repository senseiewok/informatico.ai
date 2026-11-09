# -*- coding: utf-8 -*-
"""Time & Gravity · T.00 — The hub.

Poses the intuition once, in the third person, as a question; maps the nine pages; carries no claims.
tools/check_timegravity_labels.py asserts that this page has zero claim spans.
"""
from __future__ import annotations

from ._model import P, T

SLUG = ""
CODE = "T.00"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "order_label_en": "Step 1 of 9",
    "order_label_es": "Paso 1 de 9",
    "kicker_en": "Time & Gravity · A track where the open problem is the subject",
    "kicker_es": "Tiempo y Gravedad · Una serie donde el problema abierto es el tema",
    "title_en": "Time & Gravity",
    "title_es": "Tiempo y Gravedad",
    "standfirst_en": (
        "A common intuition is that experience slides along a worldline and that gravity is a slope in the rate of time. "
        "Is any of that physics? Half of it is, and it is among the best-measured facts we have. The other half has no "
        "variable in any equation. These nine pages walk from the measured half to the open half without inventing a step."
    ),
    "standfirst_es": (
        "Una intuición común es que la experiencia se desliza por una línea de mundo y que la gravedad es una pendiente en el "
        "ritmo del tiempo. ¿Algo de eso es física? La mitad sí, y está entre los hechos mejor medidos que tenemos. La otra mitad "
        "no tiene variable en ninguna ecuación. Estas nueve páginas caminan de la mitad medida a la mitad abierta sin inventar un paso."
    ),
    "seo": (
        "Time & Gravity · Nine Pages on an Open Problem",
        "A reading track from the measured slope in the rate of time to the open problem of time in quantum gravity, with instruments, verifiers and a ledger.",
        "Tiempo y Gravedad · Un Problema Abierto en 9 Páginas",
        "Una serie que va de la pendiente medida en el ritmo del tiempo al problema abierto del tiempo en la gravedad cuántica, con instrumentos y verificadores.",
    ),
    "reading_time_en": "6 min read",
    "reading_time_es": "6 min de lectura",
    "open_question_en": "Is any of this physics?",
    "open_question_es": "¿Algo de esto es física?",
    "next_code": "T.02",
    "next_title_en": "Everyone moves at one rate",
    "next_title_es": "Todos avanzamos a un mismo ritmo",
    "next_built": False,
    "ledger_ids": [],
    "worldline": {
        "title_en": "The question, drawn once",
        "title_es": "La pregunta, dibujada una vez",
        "how_en": (
            "A picture of the question, not a result. The horizontal axis is coordinate time, the vertical axis is height, and the "
            "shading is how fast a clock runs at each height, darker meaning slower. The marker is 'now' as the intuition imagines it, "
            "a point sliding along the worldline; move it with the slider or the arrow keys. General relativity has the worldline and "
            "the shading. It has no marker. Which pages carry that difference is what the map below is for."
        ),
        "how_es": (
            "Un dibujo de la pregunta, no un resultado. El eje horizontal es el tiempo coordenado, el vertical es la altura, y el "
            "sombreado es qué tan rápido avanza un reloj a cada altura, más oscuro significa más lento. El marcador es el 'ahora' tal como "
            "lo imagina la intuición, un punto que se desliza por la línea de mundo; muévelo con el deslizador o las flechas del teclado. "
            "La relatividad general tiene la línea de mundo y el sombreado. No tiene marcador. Para qué páginas cargan esa diferencia "
            "está el mapa de abajo."
        ),
    },
    "sections": [
        {"type": "h2", "id": "map", "en": "The nine steps, in reading order", "es": "Los nueve pasos, en orden de lectura", "short_en": "Map", "short_es": "Mapa"},
        {"type": "track_map"},
        {"type": "h2", "id": "contract", "en": "How to read a T page", "es": "Cómo leer una página T", "short_en": "Labels", "short_es": "Etiquetas"},
        P(
            T("Every page in this track ships six things, and the build refuses a page that lacks one: a hand-written instrument whose "
              "knockout is the argument; a standard-library verifier that recomputes the page's central number and fails on a planted "
              "defect; a grounding ledger whose every DOI resolves in the site's offline Crossref cache; a label on every claim, derived "
              "from the ledger by a lint and decided by a person; a SKILL.md so any agent can rebuild the toy; and a Mexican Spanish twin "
              "in the same commit.",
              "Cada página de esta serie entrega seis cosas, y la construcción rechaza una página a la que le falte una: un instrumento "
              "escrito a mano cuyo apagado es el argumento; un verificador de biblioteca estándar que recalcula el número central de la "
              "página y falla ante un defecto plantado; un libro de registro cuyos DOI resuelven todos en la caché Crossref sin conexión "
              "del sitio; una etiqueta en cada afirmación, derivada del libro de registro por un lint y decidida por una persona; un "
              "SKILL.md para que cualquier agente reconstruya el juguete; y una gemela en español mexicano en el mismo commit."),
        ),
        {"type": "labels"},
        P(
            T("The labels describe evidence, not confidence. MEASURED needs at least two collaborations with peer-reviewed results. "
              "BOUND is an exclusion limit. DERIVED follows by mathematics from a named MEASURED parent. SINGLE RESULT is one "
              "collaboration, or anything published inside the last twenty-four months. PROPOSED is a proposal, and a preprint can never "
              "be more. OPEN is a question the field has not closed. A lint checks the mechanics: rows, dates, collaborations, DOIs, the "
              "same label sequence in both languages. A human checklist decides the label itself.",
              "Las etiquetas describen evidencia, no confianza. MEDIDO necesita al menos dos colaboraciones con resultados revisados por "
              "pares. COTA es un límite de exclusión. DERIVADO se sigue por matemáticas de una fila madre MEDIDA con nombre. RESULTADO "
              "ÚNICO es una sola colaboración, o cualquier cosa publicada en los últimos veinticuatro meses. PROPUESTO es una propuesta, y "
              "una prepublicación nunca puede ser más. ABIERTO es una pregunta que el campo no ha cerrado. Un lint revisa la mecánica: "
              "filas, fechas, colaboraciones, DOI, la misma secuencia de etiquetas en ambos idiomas. Una lista de verificación humana decide "
              "la etiqueta en sí."),
        ),
        P(
            T("This hub carries no claims at all, and the lint asserts that. It states the intuition once, above, as a question in the "
              "third person, and that sentence is banned on every other page of the track.",
              "Este punto de partida no lleva ninguna afirmación, y el lint lo comprueba. Enuncia la intuición una vez, arriba, como "
              "pregunta en tercera persona, y esa oración está prohibida en todas las demás páginas de la serie."),
        ),
        {"type": "h2", "id": "change", "en": "What would change this page", "es": "Qué cambiaría esta página", "short_en": "What would change", "short_es": "Qué cambiaría"},
        {"type": "change_box",
         "items": [
             ("A measurement that found a felt 'now' as a variable in a physical law would turn the open half into a claim with a label; nothing of the kind exists today.",
              "Una medición que encontrara un 'ahora' sentido como variable en una ley física convertiría la mitad abierta en una afirmación con etiqueta; hoy no existe nada parecido."),
             ("A page in this track labelled above what its ledger rows support fails the build, and the track does not ship until the label or the ledger is fixed.",
              "Una página de esta serie etiquetada por encima de lo que sus filas del libro de registro sostienen hace fallar la construcción, y la serie no se publica hasta corregir la etiqueta o el libro."),
             ("Every step in the map above is live. The map keeps each page's open question beside its title so the order of reading stays fixed, and a new page joins the track only through the same ledger and lint.",
              "Cada paso del mapa de arriba está publicado. El mapa conserva la pregunta abierta de cada página junto a su título para que el orden de lectura quede fijo, y una página nueva entra a la serie sólo por el mismo libro de registro y el mismo lint."),
         ]},
    ],
    "sources": [],
}
