# -*- coding: utf-8 -*-
"""Time & Gravity · T.05 — Does gravity entangle, and would that settle it?

A proposal, a dispute, and no result: the Bose–Marletto–Vedral experiment. Two masses, each in two places, interact
only through gravity; if the mediator is quantum the pair ends up entangled, with a phase the instrument recomputes live.
Three channels are drawn at equal weight (quantum, classical LOCC, disputed classical non-LOCC). Knockout: switch the
channel. Planted defect: a LOCC channel that entangles. Page label OPEN; T.05 ships last by council decision.
Verifier: skills/timegravity/t05/verify_t05_entanglement_channels.py.
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t05"
CODE = "T.05"

BOSE = "T05-BOSE2017"
MV = "T05-MARLETTO2017"
WEST = "T05-WESTPHAL2021"
FUCHS = "T05-FUCHS2024"
AGAF = "T05-AGAFONOVA2026"
TROY = "T05-TROYER2026"
KTM = "T05-KTM2014"
PERES = "T05-PERES1996"
WOOT = "T05-WOOTTERS1998"
AZIZ = "T05-AZIZ2025"
TRILLO = "T05-TRILLO2025"
SCHN = "T05-SCHNEIDER2026"
MV25 = "T05-MARLETTO2025"
DIOSI25 = "T05-DIOSI2025"
TOBAR = "T05-TOBAR2026"
TILLOY = "T05-TILLOY2016"
VDK = "T05-VANDEKAMP2020"
LEE = "T05-LEE2020"
TAN = "T05-TAN2020"
LEE21 = "T05-LEE2021"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "date": "2026-11-09",
    "order_label_en": "Reading order 6 of 9",
    "order_label_es": "Orden de lectura 6 de 9",
    "kicker_en": "Time & Gravity · T.05 · A proposal, a dispute and no result yet; page label OPEN",
    "kicker_es": "Tiempo y Gravedad · T.05 · Una propuesta, una disputa y todavía ningún resultado; etiqueta de página ABIERTO",
    "title_en": "Does Gravity Entangle, and Would That Settle It?",
    "title_es": "¿La Gravedad Entrelaza, y Eso Bastaría?",
    "standfirst_en": (
        "Put two small masses each into two places at once and let them pull on each other through gravity alone. If the pull is "
        "carried by something quantum, the pair comes back entangled, by a phase this page recomputes from G, the masses, the distances "
        "and the time. Nobody has run the experiment. And since 2025, into 2026, the literature disputes what a positive result would prove. This page "
        "draws the three answers at equal weight and labels the whole question OPEN."
    ),
    "standfirst_es": (
        "Pon dos masas pequeñas, cada una en dos lugares a la vez, y deja que se atraigan solo por gravedad. Si la atracción la lleva "
        "algo cuántico, el par regresa entrelazado, por una fase que esta página recalcula desde G, las masas, las distancias y el tiempo. "
        "Nadie ha corrido el experimento. Y desde 2025, ya en 2026, la literatura disputa qué probaría un resultado positivo. Esta página dibuja las "
        "tres respuestas con el mismo peso y etiqueta toda la pregunta como ABIERTA."
    ),
    "seo": (
        "Does Gravity Entangle? Three Channels, One Question",
        "Bose-Marletto-Vedral recomputed: the entanglement phase of two masses, a classical channel that entangles nothing, and the 2025 dispute, at equal weight.",
        "¿La Gravedad Entrelaza? Tres Canales, Una Pregunta",
        "Bose, Marletto y Vedral recalculados: la fase de entrelazamiento de dos masas, un canal clásico que no entrelaza nada, y la disputa de 2025, con el mismo peso.",
    ),
    "reading_time_en": "14 min read",
    "reading_time_es": "14 min de lectura",
    "central_number_en": "For the 2017 proposal's own geometry (10⁻¹⁴ kg, 450 µm apart, each split by 250 µm, held 2.5 s): entanglement phase Δφ = 0.31 rad, concurrence |sin(Δφ/2)| = 0.16 recomputed two ways within 1e-12; full entanglement at 25.0 s; a classical mean-field channel entangles nothing (< 1e-12); the band's edges computed: the classical-channel rate KΔx²/2ħ is this page's dephasing threshold (ratio 1.000 in the small-split limit), and the Diósi–Penrose model predicts entanglement only below 0.8508σ (the 2025 letter: 0.8501σ); on the 2020 Eöt-Wash wedge pattern that model's smeared pull removes 17 % of the 120-fold torque at 52 µm for σ = 75 µm, where the Yukawa at the published edge removes 2.5 %",
    "central_number_es": "Para la geometría de la propuesta de 2017 (10⁻¹⁴ kg, a 450 µm, cada una dividida 250 µm, sostenidas 2.5 s): fase de entrelazamiento Δφ = 0.31 rad, concurrencia |sin(Δφ/2)| = 0.16 recalculada de dos maneras dentro de 1e-12; entrelazamiento completo a 25.0 s; un canal clásico de campo medio no entrelaza nada (< 1e-12); los bordes de la banda calculados: la tasa del canal clásico KΔx²/2ħ es el umbral de desfase de esta página (razón 1.000 en el límite de división pequeña), y el modelo de Diósi–Penrose predice entrelazamiento solo por debajo de 0.8508σ (la carta de 2025: 0.8501σ); en el patrón de cuñas de Eöt-Wash de 2020 la atracción suavizada de ese modelo quita 17 % del par de 120 pliegues a 52 µm para σ = 75 µm, donde el Yukawa del borde publicado quita 2.5 %",
    "verifier": "skills/timegravity/t05/verify_t05_entanglement_channels.py",
    "generator": "skills/timegravity/t05/make_t05.py",
    "skill": "skills/timegravity/t05/SKILL.md",
    "skill_filename": "timegravity-t05-entanglement-channels.SKILL.md",
    "open_question_en": "If a classical slope can entangle, what would count as quantum gravity?",
    "open_question_es": "Si una pendiente clásica puede entrelazar, ¿qué contaría como gravedad cuántica?",
    "ledger_ids": [BOSE, MV, WEST, FUCHS, AGAF, TROY, KTM, PERES, WOOT, AZIZ, TRILLO, SCHN, MV25, DIOSI25, TOBAR, TILLOY, VDK, LEE, TAN, LEE21],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any proposal, measurement, derivation or rebuttal cited on this page. "
        "The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna propuesta, medición, derivación o réplica citada en "
        "esta página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien mantiene el sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "bmv",
        "title_en": "Instrument · Two masses in two places, three channels at equal weight",
        "title_es": "Instrumento · Dos masas en dos lugares, tres canales con el mismo peso",
        "how_en": (
            "Left: mass A and mass B, each in a superposition of a left and a right position; the four lines are the four branches, each "
            "with its own separation and its own phase G m² t/(ħ d). Right: entanglement against hold time, drawn for all three channels at "
            "once and at the same stroke weight: the quantum channel's curve |sin(Δφ/2)|, the classical LOCC channel's flat zero, and the "
            "disputed classical non-LOCC channel as a hatched band between them, because the literature gives two answers and this page "
            "picks neither; inside the band a dotted curve is what one named classical model, the Diósi–Penrose model with its smearing σ, "
            "predicts for the chosen σ, and the readouts give the band's two computed edges and what the smeared pull would do to the 120-fold torque of the 2020 Eöt-Wash plates at 52 µm. Sliders set the mass, the separation, the split, "
            "the hold time, a local dephasing rate and the model's σ. The knockout switches "
            "which channel the readouts follow. The planted defect is a classical LOCC channel that entangles, which the verifier rejects. "
            "Keyboard: Tab and arrows. With reduced motion on, nothing animates."
        ),
        "how_es": (
            "Izquierda: la masa A y la masa B, cada una en superposición de una posición izquierda y una derecha; las cuatro líneas son las "
            "cuatro ramas, cada una con su propia separación y su propia fase G m² t/(ħ d). Derecha: entrelazamiento frente al tiempo de "
            "espera, dibujado para los tres canales a la vez y con el mismo grosor de trazo: la curva |sin(Δφ/2)| del canal cuántico, el cero "
            "plano del canal clásico LOCC, y el canal clásico no-LOCC en disputa como una banda rayada entre ambos, porque la literatura da dos "
            "respuestas y esta página no elige ninguna; dentro de la banda una curva punteada es lo que un modelo clásico con nombre, el modelo de "
            "Diósi–Penrose con su suavizado σ, predice para la σ elegida, y las lecturas dan los dos bordes calculados de la banda y lo que la atracción suavizada haría al par de 120 pliegues de las placas de Eöt-Wash de 2020 a 52 µm. Los deslizadores "
            "fijan la masa, la separación, la división, el tiempo de espera, una tasa local de desfase y la σ del modelo. El apagado cambia qué canal siguen las lecturas. El defecto plantado es un canal clásico LOCC que entrelaza, "
            "que el verificador rechaza. Teclado: Tab y flechas. Con movimiento reducido, nada se anima."
        ),
    },
    "predict": {
        "q_en": "Before you move the sliders: the 2017 geometry, held for 2.5 s, if the mediator is quantum. How entangled are the two masses, on a scale where 0 is none and 1 is maximal?",
        "q_es": "Antes de mover los deslizadores: la geometría de 2017, sostenida 2.5 s, si el mediador es cuántico. ¿Qué tan entrelazadas quedan las dos masas, en una escala donde 0 es nada y 1 es máximo?",
        "options": [("About 0.16", "Alrededor de 0.16"), ("About 0.9", "Alrededor de 0.9"), ("Exactly zero: gravity is too weak", "Exactamente cero: la gravedad es demasiado débil")],
        "answer": 0,
        "reveal_en": "Concurrence 0.16, from an entanglement phase of 0.31 rad. The same geometry held for 25 s would reach 1. Weak is not zero; what the proposal needs is isolation, not strength.",
        "reveal_es": "Concurrencia 0.16, por una fase de entrelazamiento de 0.31 rad. La misma geometría sostenida 25 s llegaría a 1. Débil no es cero; lo que la propuesta necesita es aislamiento, no fuerza.",
    },
    "sections": [
        {"type": "h2", "id": "proposal", "en": "I · The proposal, and the phase it predicts", "es": "I · La propuesta, y la fase que predice", "short_en": "I · Proposal", "short_es": "I · Propuesta"},
        P(
            C("PROPOSED", [BOSE, MV],
              "In 2017 two papers proposed the same test: hold two micron-size masses, each in a superposition of two positions, close enough "
              "to pull on each other through gravity and far enough that Casimir–Polder forces stay a tenth of the gravitational pull; if the two masses "
              "come back entangled, the field that connected them is, on the papers' argument, a quantum entity.",
              "En 2017 dos artículos propusieron la misma prueba: sostener dos masas de tamaño micrométrico, cada una en superposición de dos "
              "posiciones, lo bastante cerca para atraerse por gravedad y lo bastante lejos para que las fuerzas de Casimir-Polder queden en un décimo "
              "de la atracción gravitatoria; si las dos masas regresan entrelazadas, el campo que las conectó es, según el argumento de los artículos, "
              "una entidad cuántica."),
            T(" The first paper gives a geometry: masses of 10⁻¹⁴ kg, traps 450 µm apart, each mass split by 250 µm, a hold of 2.5 s, "
              "a pressure of 10⁻¹⁵ Pa and an internal temperature of 0.15 K. The second gives the general argument for why entanglement would be "
              "sufficient evidence. Both are proposals, and both rows are labelled so.",
              " El primer artículo da una geometría: masas de 10⁻¹⁴ kg, trampas a 450 µm, cada masa dividida 250 µm, una espera de 2.5 s, una "
              "presión de 10⁻¹⁵ Pa y una temperatura interna de 0.15 K. El segundo da el argumento general de por qué el entrelazamiento sería "
              "evidencia suficiente. Ambos son propuestas, y ambas filas están etiquetadas así."),
        ),
        P(
            C("DERIVED", [WOOT, WEST, BOSE],
              "Each of the four branches (left–left, left–right, right–left, right–right) accumulates the Newtonian phase φ = G m² t/(ħ d) for its own "
              "separation d; the two-mass state is a product exactly when Δφ = φ_LR + φ_RL − φ_LL − φ_RR is a multiple of 2π, and otherwise its "
              "concurrence is |sin(Δφ/2)|.",
              "Cada una de las cuatro ramas (izquierda-izquierda, izquierda-derecha, derecha-izquierda, derecha-derecha) acumula la fase newtoniana "
              "φ = G m² t/(ħ d) para su propia separación d; el estado de las dos masas es un producto exactamente cuando Δφ = φ_LR + φ_RL − φ_LL − φ_RR "
              "es un múltiplo de 2π, y de otro modo su concurrencia es |sin(Δφ/2)|.",
              parent=WEST),
            T(" The label is DERIVED: the concurrence formula is Wootters's for a pure two-qubit state, and the potential it is fed is the "
              "Newtonian one, the law the parent MEASURED row confirmed between millimetre gold spheres at a surface distance of 400 µm. For the 2017 geometry the kernel finds "
              "the RL and LR branch phases to exceed the LL phase by 0.44 rad and −0.13 rad (the paper's order-of-magnitude 0.7 and −0.2), an entanglement phase of 0.31 rad and "
              "a concurrence of 0.16; the verifier recomputes the concurrence from the reduced state's purity and requires agreement to one part in 10¹².",
              " La etiqueta es DERIVADO: la fórmula de la concurrencia es la de Wootters para un estado puro de dos qubits, y el potencial que se "
              "le da es el newtoniano, la ley que la fila madre MEDIDA confirmó entre esferas de oro milimétricas a una distancia entre superficies de 400 µm. Para la geometría de 2017 el núcleo encuentra "
              "que las fases de las ramas RL y LR exceden la fase LL por 0.44 rad y −0.13 rad (los 0.7 y −0.2 de orden de magnitud del artículo), una fase de entrelazamiento de 0.31 rad "
              "y una concurrencia de 0.16; el verificador recalcula la concurrencia desde la pureza del estado reducido y exige coincidencia a una parte en 10¹²."),
        ),
        P(
            C("DERIVED", [PERES, WEST, WOOT],
              "A local dephasing rate γ on each mass shrinks the off-diagonal terms by e^{−γt}; the Peres negativity of the resulting mixed state, "
              "computed from the partial transpose, equals half the concurrence when γ = 0 and reaches zero for the 2017 geometry at γt = 0.16, so "
              "the entanglement survives only while the dephasing phase budget stays below the entanglement phase's own order.",
              "Una tasa local de desfase γ en cada masa encoge los términos fuera de la diagonal por e^{−γt}; la negatividad de Peres del estado "
              "mixto resultante, calculada desde la transpuesta parcial, iguala la mitad de la concurrencia cuando γ = 0 y llega a cero para la geometría "
              "de 2017 en γt = 0.16, así que el entrelazamiento sobrevive solo mientras el presupuesto de fase del desfase se queda por debajo del orden "
              "de la propia fase de entrelazamiento.",
              parent=WEST),
            T(" The paper's own requirement reads the same way: at 10⁻¹⁵ Pa and 0.15 K it estimates a collisional decoherence time of the order "
              "of the 3.5 s the masses spend falling, and a witness value of about 1.16 against a threshold of 1. This page's dephasing model "
              "is a single rate, not a laboratory budget; the paper's witness and the kernel's negativity are different measures of the same state.",
              " El requisito del propio artículo se lee igual: a 10⁻¹⁵ Pa y 0.15 K estima un tiempo de decoherencia por colisiones del orden de los "
              "3.5 s que las masas pasan cayendo, y un valor del testigo de alrededor de 1.16 frente a un umbral de 1. El modelo de desfase de esta "
              "página es una sola tasa, no un presupuesto de laboratorio; el testigo del artículo y la negatividad del núcleo son medidas distintas del mismo estado."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("Two things are entangled when neither has a state of its own, only the pair does. Gravity is a pull that depends on distance. "
                 "If each mass is in two places, there are four distances, and each pair of positions collects a slightly different amount of "
                 "'gravitational time'. Those four amounts do not add up to something each mass could carry alone; the leftover is the "
                 "entanglement phase. On this page it is 0.31 radians after 2.5 seconds, and the dial would read 1 after 25 seconds.",
                 "Dos cosas están entrelazadas cuando ninguna tiene un estado propio, solo el par lo tiene. La gravedad es una atracción que "
                 "depende de la distancia. Si cada masa está en dos lugares, hay cuatro distancias, y cada par de posiciones acumula una cantidad "
                 "ligeramente distinta de 'tiempo gravitatorio'. Esas cuatro cantidades no se reparten en algo que cada masa pudiera llevar sola; "
                 "el sobrante es la fase de entrelazamiento. En esta página es 0.31 radianes tras 2.5 segundos, y el dial marcaría 1 tras 25 segundos.")),
             P(T("The hard part is not the pull, which is there. The hard part is keeping two specks of matter in two places for seconds without a "
                 "single gas molecule or a single photon noticing where they are. Nobody has done it yet. And a second hard part appeared in 2025: "
                 "physicists disagree about whether seeing the entanglement would prove gravity is quantum. So the page says OPEN, twice.",
                 "Lo difícil no es la atracción, que está ahí. Lo difícil es mantener dos motas de materia en dos lugares durante segundos sin que "
                 "una sola molécula de gas o un solo fotón note dónde están. Nadie lo ha hecho todavía. Y en 2025 apareció una segunda dificultad: "
                 "los físicos no concuerdan en si ver el entrelazamiento probaría que la gravedad es cuántica. Por eso la página dice ABIERTO, dos veces.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: two dancers each step left or right, and a rope between them tightens by an amount that depends on how far "
                 "apart they land. If the rope is a real rope, the four possible tightenings leave a trace that neither dancer could have made alone, "
                 "and the two are coupled. If a stagehand only watches each dancer and tugs the other by hand according to the average, the dancers "
                 "feel a pull, but no trace of the pair survives. The third case, a rope nobody agrees is real, is what the 2025 papers argue about.",
                 "Analogía cotidiana: dos bailarines dan cada uno un paso a la izquierda o a la derecha, y una cuerda entre ambos se tensa según qué "
                 "tan lejos caigan. Si la cuerda es una cuerda real, las cuatro tensiones posibles dejan una huella que ninguno de los dos pudo hacer "
                 "solo, y los dos quedan acoplados. Si un tramoyista solo observa a cada bailarín y jala al otro a mano según el promedio, los bailarines "
                 "sienten un tirón, pero ninguna huella del par sobrevive. El tercer caso, una cuerda que nadie concuerda en si es real, es lo que discuten "
                 "los artículos de 2025.")),
             P(T("How the controls work in plain words: the mass slider makes the rope stronger as the square of the mass; the separation slider "
                 "weakens it; the split slider makes the four distances more different, which is what entangles; the hold-time slider lets the phase "
                 "grow; the dephasing slider lets the room look. The channel buttons are the knockout: the same rope seen as quantum, as classical "
                 "LOCC, or as disputed. The planted defect lets the classical LOCC channel copy the quantum curve, which the verifier refuses.",
                 "Cómo funcionan los controles en palabras sencillas: el deslizador de masa hace la cuerda más fuerte con el cuadrado de la masa; el de "
                 "separación la debilita; el de división hace las cuatro distancias más distintas, que es lo que entrelaza; el de tiempo de espera deja "
                 "crecer la fase; el de desfase deja que el cuarto mire. Los botones de canal son el apagado: la misma cuerda vista como cuántica, como "
                 "clásica LOCC, o como disputada. El defecto plantado deja que el canal clásico LOCC copie la curva cuántica, lo que el verificador rechaza.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "channels", "en": "II · Three channels, equal weight", "es": "II · Tres canales, el mismo peso", "short_en": "II · Channels", "short_es": "II · Canales"},
        P(
            C("PROPOSED", [KTM, MV],
              "A classical channel can carry the force without carrying the entanglement: in the 2014 classical-channel model gravity acts as a "
              "continuous measurement of each mass's position fed back as a force on the other, which reproduces Newton's law on average, adds a "
              "minimum decoherence, and, being local operations with classical communication, can create no entanglement at all.",
              "Un canal clásico puede llevar la fuerza sin llevar el entrelazamiento: en el modelo de canal clásico de 2014 la gravedad actúa como "
              "una medición continua de la posición de cada masa retroalimentada como fuerza sobre la otra, lo que reproduce la ley de Newton en "
              "promedio, añade una decoherencia mínima y, siendo operaciones locales con comunicación clásica, no puede crear entrelazamiento alguno."),
            T(" That is the second channel of the instrument, drawn at the same stroke weight as the first. The kernel builds it as a mean field: "
              "each mass feels the average of the other's two positions, the four phases take the product form α_i + β_j, and the entanglement phase is "
              "zero to one part in 10¹² on a grid of twenty-seven geometries. In the 2017 argument this is the case a positive result would exclude.",
              " Ese es el segundo canal del instrumento, dibujado con el mismo grosor de trazo que el primero. El núcleo lo construye como campo "
              "medio: cada masa siente el promedio de las dos posiciones de la otra, las cuatro fases toman la forma producto α_i + β_j, y la fase de "
              "entrelazamiento es cero a una parte en 10¹² sobre una malla de veintisiete geometrías. En el argumento de 2017 este es el caso que un "
              "resultado positivo excluiría."),
        ),
        P(
            C("OPEN", [AZIZ, TRILLO, SCHN, MV25, DIOSI25],
              "Whether every classical account of gravity falls into that second channel is disputed: a 2025 paper argues that a classical gravitational "
              "interaction can transmit quantum information and generate entanglement through physically local processes when matter is treated by quantum "
              "field theory, and a 2025 letter finds that the Diósi–Penrose dynamics with classical gravity entangles two separate particles, so that "
              "'GIE detection is not enough to validate quantum gravity'; two preprints and a 2026 paper reply that classical gravity cannot mediate "
              "entanglement by local means and that the perturbative result is precluded by an exact derivation.",
              "Si toda descripción clásica de la gravedad cae en ese segundo canal está en disputa: un artículo de 2025 sostiene que una interacción "
              "gravitatoria clásica puede transmitir información cuántica y generar entrelazamiento mediante procesos físicamente locales cuando la "
              "materia se trata con teoría cuántica de campos, y una carta de 2025 encuentra que la dinámica de Diósi-Penrose con gravedad clásica "
              "entrelaza dos partículas separadas, de modo que 'detectar GIE no basta para validar la gravedad cuántica'; dos prepublicaciones y un "
              "artículo de 2026 responden que la gravedad clásica no puede mediar entrelazamiento por medios locales y que el resultado perturbativo "
              "queda excluido por una derivación exacta."),
            T(" This is the third channel. The kernel gives it no curve of its own, only the interval between the two published answers, no entanglement at all and "
              "as much as the quantum channel gives, drawn as a hatched band with neither edge marked as the expected one; the page does not pick a side, and the row labels say why: the papers are young, two are "
              "preprints, and none is a measurement.",
              " Este es el tercer canal. El núcleo no le da una curva propia, solo el intervalo entre las dos respuestas publicadas, ningún entrelazamiento y tanto como da el "
              "canal cuántico, dibujado como banda rayada sin marcar ningún borde como el esperado; la página no toma partido, y las etiquetas de las filas dicen por qué: los artículos son jóvenes, "
              "dos son prepublicaciones y ninguno es una medición."),
        ),
        P(
            C("PROPOSED", [TRILLO, TILLOY, VDK],
              "The band's upper edge can be computed. In the Diósi–Penrose model as the 2025 letter writes it, gravity is classical, matter is "
              "quantum, and the mass density is smeared over a width σ, the model's only free parameter and the same R0 that T.06 bounded from "
              "below; with the free motion switched off the model integrates in closed form, and the kernel reproduces the letter's result: the "
              "model predicts entanglement only when the masses' nearest separation is below 0.8508σ (the letter: 0.8501σ in its text, 0.850872σ in its appendix), "
              "that entanglement is transient, and for the letter's example geometry (10⁻¹⁵ kg, split 23 µm, 24 µm apart) nothing is entangled at "
              "σ = 50 µm while at σ = 75, 100 and 250 µm the negativity lasts about 5 hours, 16 hours and 20 days.",
              "El borde superior de la banda se puede calcular. En el modelo de Diósi–Penrose tal como lo escribe la carta de 2025, la gravedad es "
              "clásica, la materia es cuántica, y la densidad de masa se suaviza sobre un ancho σ, el único parámetro libre del modelo y el mismo R0 "
              "que T.06 acotó por abajo; con el movimiento libre apagado el modelo se integra en forma cerrada, y el núcleo reproduce el resultado de "
              "la carta: el modelo predice entrelazamiento solo cuando la separación más cercana de las masas queda por debajo de 0.8508σ (la carta: 0.8501σ en su texto, "
              "0.850872σ en su apéndice), el entrelazamiento es transitorio, y para la geometría de ejemplo de la carta (10⁻¹⁵ kg, división de 23 µm, a 24 µm) "
              "nada se entrelaza a σ = 50 µm mientras que a σ = 75, 100 y 250 µm la negatividad dura unas 5 horas, 16 horas y 20 días."),
            T(" On the same model the smearing softens gravity itself below about 2σ: at σ = 75 µm it puts the pull between those two masses at 24 µm at "
              "18 % of Newton's. For the 2017 geometry, with a split of 250 µm, the model entangles only for σ above 525 µm and shows less than one part in a "
              "thousand of negativity at 2.5 s, because its entanglement takes hours to build. The page's planted defect for this kernel drops the model's own "
              "decoherence and keeps its phases; the critical separation then disappears, and the verifier rejects it. All of this is one model's arithmetic; the label is PROPOSED.",
              " En el mismo modelo el suavizado ablanda la gravedad misma por debajo de unas 2σ: a σ = 75 µm pone la atracción entre esas dos masas a 24 µm "
              "en el 18 % de la de Newton. Para la geometría de 2017, con una división de 250 µm, el modelo entrelaza solo para σ por encima de 525 µm y "
              "muestra menos de una parte en mil de negatividad a 2.5 s, porque su entrelazamiento tarda horas en formarse. El defecto plantado de la página para este núcleo quita la "
              "decoherencia propia del modelo y conserva sus fases; la separación crítica entonces desaparece, y el verificador lo rechaza. Todo esto es "
              "la aritmética de un modelo; la etiqueta es PROPUESTO."),
        ),
        P(
            C("PROPOSED", [KTM, MV],
              "The band's lower edge is computed from the classical-channel rate: in the 2014 model the measurement-and-feedback channel reproduces the linearised "
              "gravitational spring K = 2Gm²/d³ and adds position decoherence at KΔx²/(2ħ) per mass, 'minimal in the sense that, if it were any "
              "smaller, evolution ... would immediately entangle'; the kernel finds that the dephasing threshold at which this page's negativity "
              "vanishes is exactly that rate in the small-split limit (ratio 1.000 at a 2 µm split, 1.43 at the 2017 split of 250 µm, where the "
              "linearisation is 30 % low on the phase).",
              "El borde inferior de la banda se calcula desde la tasa del canal clásico: en el modelo de 2014 el canal de medición y retroalimentación reproduce el "
              "resorte gravitatorio linealizado K = 2Gm²/d³ y añade decoherencia de posición a KΔx²/(2ħ) por masa, 'mínima en el sentido de que, si "
              "fuera un poco menor, la evolución ... entrelazaría de inmediato'; el núcleo encuentra que el umbral de desfase al que se anula la "
              "negatividad de esta página es exactamente esa tasa en el límite de división pequeña (razón 1.000 a una división de 2 µm, 1.43 a la "
              "división de 250 µm de 2017, donde la linealización se queda 30 % corta en la fase)."),
            T(" So the two edges are computed, not chosen: the lower one is the least noise a classical channel of that kind must add on its own "
              "model, the upper one is what one named classical model predicts, and between them the page still picks no side.",
              " Así que los dos bordes se calculan, no se eligen: el inferior es el ruido mínimo que debe añadir un canal clásico de ese tipo en su propio "
              "modelo, el superior es lo que predice un modelo clásico con nombre, y entre ambos la página sigue sin tomar partido."),
        ),
        P(
            C("MEASURED", [LEE, TAN],
              "Newton's inverse-square law has been tested in the laboratory at separations down to 52 µm, with any gravitational-strength Yukawa "
              "interaction limited to ranges below 38.6 µm at 95 % confidence, and shown by a second group to hold with |α| ≤ 1 down to a length "
              "scale of 48 µm.",
              "La ley del inverso del cuadrado de Newton se ha puesto a prueba en el laboratorio a separaciones de hasta 52 µm, con cualquier "
              "interacción de Yukawa de intensidad gravitatoria limitada a alcances por debajo de 38.6 µm al 95 % de confianza, y un segundo grupo "
              "mostró que se cumple con |α| ≤ 1 hasta una escala de longitud de 48 µm."),
            T(" The smearing that lets the model entangle softens its pull below about 2σ, and the same pull must act between the test bodies of these experiments.",
              " El suavizado que permite al modelo entrelazar ablanda su atracción por debajo de unas 2σ, y la misma atracción debe actuar entre los cuerpos de prueba de estos experimentos."),
        ),
        P(
            C("PROPOSED", [TRILLO, LEE, LEE21],
              "The kernel can redo the comparison with the experiment's own method. Between two patterned plates each in-plane mode of the mass "
              "pattern with wavenumber q contributes to the pull across a gap s in proportion to e^(−qs) under Newton, and to ½[erfc(qσ − s/2σ) + "
              "e^(2qs) erfc(qσ + s/2σ)] of that under the smeared potential, a closed form checked against direct quadrature; the 2020 test bodies are two concentric sets of glue-filled "
              "wedges cut from platinum foils, 120 wedges between 13.00 and 23.00 mm and 18 between 23.51 and 26.00 mm at 50 % duty, 54 and 99 µm thick, "
              "measured to the micrometre in the 2020 dissertation, and the Fourier–Bessel expansion the collaboration published in 2021 turns the torque at "
              "each harmonic into one integral over wavenumber. The kernel rebuilds that integral with its own Bessel functions, checked against their "
              "integral representation, and gets the Newtonian 120-fold torque at 1.5 fN·m at 72 µm, where the letter's magnetic subtraction of 0.0165 fN·m, "
              "'roughly 1 %' of the signal, implies by arithmetic about 1.6. On the same integral the smeared potential removes 17 % of the 120-fold torque at 52 µm for "
              "σ = 75 µm (4.3 % at 50 µm, 0.3 % at 30 µm, 6.3 % at 55 µm, the smallest σ at which that model entangles the letter's own geometry), 13 % at 72 µm, 3.8 % at "
              "150 µm and 0.1 % at 300 µm, while a Yukawa at the published 95 % edge, α = −1 at λ = 38.6 µm, removes 2.5 % at 52 µm.",
              "El núcleo puede rehacer la comparación con el método propio del experimento. Entre dos placas con patrón, cada modo en el plano del patrón "
              "de masa con número de onda q contribuye a la atracción a través de un hueco s en proporción a e^(−qs) según Newton, y a ½[erfc(qσ − s/2σ) + "
              "e^(2qs) erfc(qσ + s/2σ)] de eso con el potencial suavizado, una forma cerrada comprobada contra cuadratura directa; los cuerpos de prueba de 2020 son dos conjuntos "
              "concéntricos de cuñas rellenas de pegamento cortadas en láminas de platino, 120 cuñas entre 13.00 y 23.00 mm y 18 entre 23.51 y 26.00 mm con "
              "50 % de relleno, de 54 y 99 µm de espesor, medidas al micrómetro en la tesis doctoral de 2020, y la expansión de Fourier–Bessel que la "
              "colaboración publicó en 2021 convierte el par de cada armónico en una sola integral sobre el número de onda. El núcleo reconstruye esa "
              "integral con sus propias funciones de Bessel, comprobadas contra su representación integral, y obtiene el par newtoniano de 120 pliegues en "
              "1.5 fN·m a 72 µm, donde la resta magnética de la carta, 0.0165 fN·m, 'alrededor del 1 %' de la señal, implica por aritmética unos 1.6. Sobre la misma integral "
              "el potencial suavizado quita 17 % del par de 120 pliegues a 52 µm para σ = 75 µm (4.3 % a 50 µm, 0.3 % a 30 µm, 6.3 % a 55 µm, la σ más "
              "pequeña a la que ese modelo entrelaza la geometría propia de la carta), 13 % a 72 µm, 3.8 % a 150 µm y 0.1 % a 300 µm, mientras que un Yukawa en el borde "
              "publicado al 95 %, α = −1 con λ = 38.6 µm, quita 2.5 % a 52 µm."),
            T(" That sets two predicted signal sizes side by side; it is not a bound on σ, because the experiment's fit, with its floating offset, roughness "
              "correction and calibrated scale, is not recomputed here. A smearing of 44 µm in that model would remove as much torque as the Yukawa at the published edge does at the closest "
              "separation, close to the 44.4 µm a one-mode lower bound at the pattern's lowest wavenumber had given, and the Yukawa shape closest to the "
              "σ = 75 µm curve has a range near 49 µm and about three times gravity's strength, a curve match with no data behind it.",
              " Eso pone lado a lado dos tamaños de señal predichos; no es una cota sobre σ, porque el ajuste del experimento, con su desplazamiento libre, "
              "su corrección de rugosidad y su escala calibrada, no se recalcula aquí. Un suavizado de 44 µm en ese modelo quitaría tanto par como el Yukawa del borde publicado a la "
              "separación más cercana, cerca de los 44.4 µm que había dado una cota inferior de un modo al número de onda más bajo del patrón, y la forma de "
              "Yukawa más parecida a la curva de σ = 75 µm tiene un alcance cerca de 49 µm y unas tres veces la intensidad de la gravedad, un ajuste de "
              "curva sin datos detrás."),
            C("PROPOSED", [TRILLO, LEE],
              "Taken as a hypothesis, not as a bound, a smearing no larger than that 44 µm would leave the model predicting entanglement only for "
              "masses whose nearest separation is below 37 µm in the small-split limit and below 15 µm for the letter's 23 µm split, and not for the "
              "letter's own geometry 24 µm apart; the criterion does not depend on the mass, the time does, as 1/m², and at 10⁻¹⁵ kg the negativity would "
              "peak between about 0.02 and 0.05 after an hour to a few weeks depending on the split. One model's predictions at a measured geometry: the label is "
              "PROPOSED.",
              "Tomado como hipótesis, no como cota, un suavizado no mayor que esos 44 µm dejaría al modelo prediciendo entrelazamiento solo para "
              "masas cuya separación más cercana quede por debajo de 37 µm en el límite de división pequeña y por debajo de 15 µm para la división de "
              "23 µm de la carta, y no para la geometría propia de la carta a 24 µm; el criterio no depende de la masa, el tiempo sí, como 1/m², y a "
              "10⁻¹⁵ kg la negatividad alcanzaría su máximo entre unos 0.02 y 0.05 tras una hora a unas semanas según la división. Predicciones de "
              "un modelo en una geometría medida: la etiqueta es PROPUESTO."),
            C("OPEN", [TRILLO, LEE, TAN],
              "Whether the published analysis, run on its own data, would reject the smeared shape is for the experiment to say, and the second group's bound "
              "at 48 µm is stated as published because its geometry is not in the open text; the letter calls the entangling range of σ 'previously untested' "
              "and its main text does not mention these tests. The page notes the question and leaves it open.",
              "Si el análisis publicado, corrido sobre sus propios datos, rechazaría la forma suavizada es algo que debe decir el experimento, y la cota del "
              "segundo grupo a 48 µm se enuncia tal como se publicó porque su geometría no está en el texto abierto; la carta llama al rango de σ que "
              "entrelaza 'no probado antes' y su texto principal no menciona estas pruebas. La página anota la pregunta y la deja abierta."),
        ),
        {"type": "h2", "id": "labs", "en": "III · How far the laboratories are", "es": "III · Qué tan lejos están los laboratorios", "short_en": "III · Labs", "short_es": "III · Laboratorios"},
        P(
            C("MEASURED", [WEST, FUCHS],
              "Gravity has been measured on the table with milligram-scale masses by two groups: in 2021 between two gold spheres of about 1 mm "
              "radius and 90 mg, on a torsion pendulum at 12.7 mHz over 350 hours, down to a surface distance of 400 µm; and in 2024 by a levitated "
              "0.4 mg magnetic particle at 26.7 Hz with a force noise of 0.5 fN/√Hz, sensing kilogram source masses about half a metre away.",
              "La gravedad se ha medido en la mesa con masas de escala de miligramos por dos grupos: en 2021 entre dos esferas de oro de alrededor "
              "de 1 mm de radio y 90 mg, en un péndulo de torsión a 12.7 mHz durante 350 horas, hasta una distancia entre superficies de 400 µm; y en "
              "2024 por una partícula magnética levitada de 0.4 mg a 26.7 Hz con un ruido de fuerza de 0.5 fN/√Hz, sintiendo masas fuente de kilogramos "
              "a alrededor de medio metro."),
            T(" Both are classical measurements of a classical pull, by different collaborations, which is what MEASURED requires. Neither mass was "
              "in two places; the proposal's masses are between seven and ten orders of magnitude lighter still.",
              " Ambas son mediciones clásicas de una atracción clásica, por colaboraciones distintas, que es lo que MEDIDO exige. Ninguna masa estuvo "
              "en dos lugares; las masas de la propuesta son todavía entre siete y diez órdenes de magnitud más ligeras."),
        ),
        P(
            C("SINGLE RESULT", [AGAF],
              "In 2026 a one-milligram torsional pendulum at 18 Hz was laser-cooled from room temperature to 240 µK, more than twenty times colder than "
              "earlier oscillators from micrograms to kilograms; the paper presents it as a platform for the quantum–gravity interface, not as a measurement of gravity.",
              "En 2026 un péndulo de torsión de un miligramo a 18 Hz se enfrió con láser desde temperatura ambiente hasta 240 µK, más de veinte veces "
              "más frío que osciladores previos de microgramos a kilogramos; el artículo lo presenta como plataforma para la interfaz cuántico-gravitatoria, "
              "no como medición de la gravedad."),
            T(" ", " "),
            C("SINGLE RESULT", [TROY],
              "The same year two librational modes of a levitated silica nanorotor were cooled to occupation numbers of 0.21 ± 0.03 and 0.54 ± 0.32 one at a "
              "time, and 1.02 ± 0.08 and 0.73 ± 0.22 together, with the rotor aligned to better than 20 µrad.",
              "El mismo año dos modos libracionales de un nanorrotor de sílice levitado se enfriaron a números de ocupación de 0.21 ± 0.03 y 0.54 ± 0.32 "
              "uno a la vez, y 1.02 ± 0.08 y 0.73 ± 0.22 juntos, con el rotor alineado a mejor que 20 µrad."),
            T(" Both rows are young and each is one laboratory's result, so each carries SINGLE RESULT; neither put a mass in two places, and the "
              "proposal's mass sits between them. The page lists them as distance covered, not as the experiment.",
              " Ambas filas son jóvenes y cada una es el resultado de un laboratorio, así que cada una lleva RESULTADO ÚNICO; ninguna puso una masa en "
              "dos lugares, y la masa de la propuesta queda entre ambas. La página las lista como distancia recorrida, no como el experimento."),
        ),
        P(
            C("PROPOSED", [TOBAR, BOSE],
              "A 2026 preprint proposes to replace the second mass by an array of quantum clocks and ask whether a levitated particle's gravity entangles "
              "with them, noting that the quantised active gravitational mass has not been tested in any prior experiment.",
              "Una prepublicación de 2026 propone sustituir la segunda masa por un arreglo de relojes cuánticos y preguntar si la gravedad de una "
              "partícula levitada se entrelaza con ellos, señalando que la masa gravitatoria activa cuantizada no se ha probado en ningún experimento previo."),
            T(" A preprint stays PROPOSED whatever it proposes. The page records it because it ties this question back to T.04: the second mass becomes a clock.",
              " Una prepublicación se queda en PROPUESTO proponga lo que proponga. La página la registra porque devuelve esta pregunta a T.04: la segunda masa se vuelve un reloj."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "settle", "en": "IV · What would count, and what this page does not say", "es": "IV · Qué contaría, y qué no dice esta página", "short_en": "IV · Settle?", "short_es": "IV · ¿Bastaría?"},
        P(
            C("OPEN", [MV, SCHN, TRILLO],
              "What a positive result would settle depends on assumptions the dispute is about: the 2017 sufficiency argument needs the field to be a "
              "mediator acting locally, the 2026 paper grants both and concludes that an observed entanglement would then have to come from something "
              "other than classical gravity, and the 2025 letter answers that a specific classical model entangles anyway, so that the experiment would "
              "test that model rather than the quantum nature of gravity.",
              "Qué zanjaría un resultado positivo depende de supuestos sobre los que versa la disputa: el argumento de suficiencia de 2017 necesita que "
              "el campo sea un mediador que actúa localmente, el artículo de 2026 concede ambos y concluye que un entrelazamiento observado tendría entonces "
              "que venir de algo distinto de la gravedad clásica, y la carta de 2025 responde que un modelo clásico específico entrelaza de todos modos, "
              "de modo que el experimento pondría a prueba ese modelo más que la naturaleza cuántica de la gravedad."),
            T(" The page does not say gravity is quantum, or that it is not; it does not say the experiment will run, or what it will show. It says "
              "which published statement each channel rests on, and that no channel has a measurement behind it.",
              " La página no dice que la gravedad sea cuántica, ni que no lo sea; no dice que el experimento se correrá, ni qué mostrará. Dice en qué "
              "afirmación publicada descansa cada canal, y que ningún canal tiene una medición detrás."),
        ),
        {"type": "change_box",
         "items": [
             ("A performed experiment that witnessed entanglement would move the quantum channel's row from PROPOSED to SINGLE RESULT, then MEASURED after a second collaboration; the page label would stay OPEN until the dispute over what it proves is resolved in the peer-reviewed record.",
              "Un experimento realizado que atestiguara entrelazamiento movería la fila del canal cuántico de PROPUESTO a RESULTADO ÚNICO, y luego a MEDIDO tras una segunda colaboración; la etiqueta de página seguiría ABIERTO hasta que la disputa sobre qué prueba se resuelva en el registro revisado por pares."),
             ("A performed experiment that found no entanglement where the quantum channel predicts it would be reported as a BOUND on the mediator, and the page rewritten around it.",
              "Un experimento realizado que no encontrara entrelazamiento donde el canal cuántico lo predice se reportaría como una COTA sobre el mediador, y la página se reescribiría alrededor de ella."),
             ("A sub-millimetre test of Newton's law analysed by its own collaboration for the smeared potential erf(r/2σ)/r would turn the σ question from OPEN into a BOUND on the model, in either direction; the page's one-mode estimate is not that analysis.",
              "Una prueba submilimétrica de la ley de Newton analizada por su propia colaboración para el potencial suavizado erf(r/2σ)/r convertiría la pregunta sobre σ de ABIERTO en una COTA sobre el modelo, en cualquier dirección; la estimación de un modo de la página no es ese análisis."),
             ("Peer-reviewed resolution of the 2025 dispute in either direction would collapse the hatched band onto one of its edges and relabel the third channel.",
              "Una resolución revisada por pares de la disputa de 2025 en cualquier dirección colapsaría la banda rayada sobre uno de sus bordes y reetiquetaría el tercer canal."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · Four separations, four phases", "Etapa 1 · Cuatro separaciones, cuatro fases",
         "Mass A at ∓Δx/2, mass B at d ∓ Δx/2: d_LL = d_RR = d, d_LR = d + Δx, d_RL = d − Δx. Each branch accumulates φ = G m² t/(ħ d). For the 2017 geometry: 0.352, 0.226, 0.791 and 0.352 rad.",
         "Masa A en ∓Δx/2, masa B en d ∓ Δx/2: d_LL = d_RR = d, d_LR = d + Δx, d_RL = d − Δx. Cada rama acumula φ = G m² t/(ħ d). Para la geometría de 2017: 0.352, 0.226, 0.791 y 0.352 rad."),
        ("Stage 2 · The entanglement phase", "Etapa 2 · La fase de entrelazamiento",
         "Δφ = φ_LR + φ_RL − φ_LL − φ_RR = 0.314 rad. The state ½ Σ e^{iφ_ij}|ij⟩ factorises exactly when Δφ ≡ 0 (mod 2π); concurrence 2|ad − bc| = |sin(Δφ/2)| = 0.156; it reaches 1 at Δφ = π, t = 25.0 s.",
         "Δφ = φ_LR + φ_RL − φ_LL − φ_RR = 0.314 rad. El estado ½ Σ e^{iφ_ij}|ij⟩ se factoriza exactamente cuando Δφ ≡ 0 (mod 2π); concurrencia 2|ad − bc| = |sin(Δφ/2)| = 0.156; llega a 1 en Δφ = π, t = 25.0 s."),
        ("Stage 3 · Negativity under dephasing", "Etapa 3 · Negatividad bajo desfase",
         "Local dephasing multiplies off-diagonal terms by e^{−γt} per mass. The partial transpose is Hermitian; its eigenvalues come from the real 8×8 embedding and the track's Jacobi solver. N = C/2 = 0.078 at γ = 0; N = 0 at γt = 0.156.",
         "El desfase local multiplica los términos fuera de la diagonal por e^{−γt} por masa. La transpuesta parcial es hermitiana; sus valores propios salen de la inmersión real 8×8 y del solucionador de Jacobi de la serie. N = C/2 = 0.078 en γ = 0; N = 0 en γt = 0.156."),
        ("Stage 4 · The classical channel and the defect", "Etapa 4 · El canal clásico y el defecto",
         "Mean field: φ_ij = ½(α_i + β_j) with α_i the average of A's phases on branch i and β_j likewise for B. Δφ = 0 to 1e-12 over 27 geometries. The planted defect hands the LOCC channel the quantum phases: concurrence 0.156 where zero is required, and the verifier fails, as it must. A second kernel computes the band's edges: the Diósi–Penrose master equation ⟨x|ρ(t)|y⟩ = exp[(G/2ħ) g(x,y) t]⟨x|ρ(0)|y⟩ with the smeared kernel f̃(z) = erf(z/2σ)/z (critical separation 0.8508σ, its own planted defect drops the decoherence), and the classical-channel rate KΔx²/2ħ against this page's threshold.",
         "Campo medio: φ_ij = ½(α_i + β_j) con α_i el promedio de las fases de A en la rama i y β_j lo mismo para B. Δφ = 0 a 1e-12 sobre 27 geometrías. El defecto plantado le da al canal LOCC las fases cuánticas: concurrencia 0.156 donde se exige cero, y el verificador falla, como debe. Un segundo núcleo calcula los bordes de la banda: la ecuación maestra de Diósi–Penrose ⟨x|ρ(t)|y⟩ = exp[(G/2ħ) g(x,y) t]⟨x|ρ(0)|y⟩ con el núcleo suavizado f̃(z) = erf(z/2σ)/z (separación crítica 0.8508σ, su propio defecto plantado quita la decoherencia), y la tasa del canal clásico KΔx²/2ħ frente al umbral de esta página."),
    ],
    "sidenotes": [
        ("SIDENOTE T.05-A · WHY THE PAGE LABEL IS OPEN", "NOTA T.05-A · POR QUÉ LA ETIQUETA DE PÁGINA ES ABIERTO",
         "Two reasons, and the second would hold even if the first fell. No gravitationally induced entanglement has been measured. And the peer-reviewed record of 2025 and 2026 disagrees about what measuring it would prove. A page cannot carry a label higher than its weakest load-bearing claim, and the load-bearing claim here is the dispute.",
         "Dos razones, y la segunda se sostendría aunque cayera la primera. No se ha medido ningún entrelazamiento inducido por gravedad. Y el registro revisado por pares de 2025 y 2026 no concuerda en qué probaría medirlo. Una página no puede llevar una etiqueta más alta que su afirmación portante más débil, y la afirmación portante aquí es la disputa."),
        ("SIDENOTE T.05-B · WEAK IS NOT ZERO", "NOTA T.05-B · DÉBIL NO ES CERO",
         "The gravitational coupling is some forty-three orders of magnitude below the electromagnetic one, as the 2017 sufficiency paper notes, yet the phase after 2.5 s is a third of a radian. The experiment's problem is isolation: 10⁻¹⁵ Pa and 0.15 K, with no stray field, for seconds. That is why the page lists cooling records as distance covered.",
         "El acoplamiento gravitatorio está unos cuarenta y tres órdenes de magnitud por debajo del electromagnético, como señala el artículo de suficiencia de 2017, y aun así la fase tras 2.5 s es un tercio de radián. El problema del experimento es el aislamiento: 10⁻¹⁵ Pa y 0.15 K, sin campo parásito, durante segundos. Por eso la página lista los récords de enfriamiento como distancia recorrida."),
    ],
    "sources": [
        ("Bose, S., Mazumdar, A., Morley, G. W., Ulbricht, H., Toroš, M., Paternostro, M., Geraci, A. A., Barker, P. F., Kim, M. S., & Milburn, G. (2017). Spin entanglement witness for quantum gravity. Physical Review Letters, 119(24), 240401.", "10.1103/PhysRevLett.119.240401"),
        ("Marletto, C., & Vedral, V. (2017). Gravitationally induced entanglement between two massive particles is sufficient evidence of quantum effects in gravity. Physical Review Letters, 119(24), 240402.", "10.1103/PhysRevLett.119.240402"),
        ("Westphal, T., Hepach, H., Pfaff, J., & Aspelmeyer, M. (2021). Measurement of gravitational coupling between millimetre-sized masses. Nature, 591, 225–228.", "10.1038/s41586-021-03250-7"),
        ("Fuchs, T. M., Uitenbroek, D. G., Plugge, J., van Halteren, N., van Soest, J.-P., Vinante, A., Ulbricht, H., & Oosterkamp, T. H. (2024). Measuring gravity with milligram levitated masses. Science Advances, 10(8), eadk2949.", "10.1126/sciadv.adk2949"),
        ("Agafonova, S., Rossello, P., Mekonnen, M., & Hosten, O. (2026). One-milligram torsional pendulum toward experiments at the quantum-gravity interface. Communications Physics, 9, 80.", "10.1038/s42005-026-02514-w"),
        ("Troyer, S., Fechtel, F., Hummer, L., Rudolph, H., Stickler, B. A., Delić, U., & Arndt, M. (2026). Quantum ground-state cooling of two librational modes of a nanorotor. Nature Physics, 22, 584–590.", "10.1038/s41567-026-03219-1"),
        ("Kafri, D., Taylor, J. M., & Milburn, G. J. (2014). A classical channel model for gravitational decoherence. New Journal of Physics, 16, 065020.", "10.1088/1367-2630/16/6/065020"),
        ("Peres, A. (1996). Separability criterion for density matrices. Physical Review Letters, 77(8), 1413–1415.", "10.1103/PhysRevLett.77.1413"),
        ("Wootters, W. K. (1998). Entanglement of formation of an arbitrary state of two qubits. Physical Review Letters, 80(10), 2245–2248.", "10.1103/PhysRevLett.80.2245"),
        ("Aziz, J., & Howl, R. (2025). Classical theories of gravity produce entanglement. Nature, 646, 813–817.", "10.1038/s41586-025-09595-7"),
        ("Trillo, D., & Navascués, M. (2025). Diósi-Penrose model of classical gravity predicts gravitationally induced entanglement. Physical Review D, 111, L121101.", "10.1103/PhysRevD.111.L121101"),
        ("Schneider, M. D., Huggett, N., & Linnemann, N. (2026). A demonstration that classical gravity does not produce entanglement. Classical and Quantum Gravity, 43(17), 177001.", "10.1088/1361-6382/ae6f62"),
        ("Marletto, C., & Vedral, V. (2025). Classical gravity cannot mediate entanglement by local means. arXiv:2510.19969 (preprint).", "10.48550/arXiv.2510.19969"),
        ("Diósi, L. (2025). No, classical gravity does not entangle quantized matter fields. arXiv:2511.00852 (preprint).", "10.48550/arXiv.2511.00852"),
        ("Tobar, G., Aspelmeyer, M., & Zych, M. (2026). Testing gravitationally-induced-entanglement with massive particles and quantum clocks. arXiv:2611.08313 (preprint).", "10.48550/arXiv.2611.08313"),
        ("Tilloy, A., & Diósi, L. (2016). Sourcing semiclassical gravity from spontaneously localized quantum matter. Physical Review D, 93, 024026.", "10.1103/PhysRevD.93.024026"),
        ("van de Kamp, T. W., Marshman, R. J., Bose, S., & Mazumdar, A. (2020). Quantum gravity witness via entanglement of masses: Casimir screening. Physical Review A, 102, 062807.", "10.1103/PhysRevA.102.062807"),
        ("Lee, J. G., Adelberger, E. G., Cook, T. S., Fleischer, S. M., & Heckel, B. R. (2020). New test of the gravitational 1/r² law at separations down to 52 µm. Physical Review Letters, 124, 101101.", "10.1103/PhysRevLett.124.101101"),
        ("Tan, W.-H., et al. (2020). Improvement for testing the gravitational inverse-square law at the submillimeter range. Physical Review Letters, 124, 051301.", "10.1103/PhysRevLett.124.051301"),
    ],
}
