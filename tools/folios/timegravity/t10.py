# -*- coding: utf-8 -*-
"""Time & Gravity · T.10 — Page's counting argument.

Hawking's rising line against Page's average-entropy curve from a Haar-random toy on 10 qubits, checked against
Page's closed form with a pure-Python eigensolver; islands described in prose as OPEN; the GW250114 area figure
shown as the paper's own claim, never as a recomputed test. Knockout: non-unitary evaporation, the entropy never
turns over (also the verifier's planted defect). Page labels DERIVED and OPEN.
Verifier: skills/timegravity/t10/verify_t10_page_curve.py.
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t10"
CODE = "T.10"

H71 = "T10-HAWKING1971"
BEK = "T10-BEKENSTEIN1973"
H75 = "T10-HAWKING1975"
PAGEA = "T10-PAGE1993A"
PAGEB = "T10-PAGE1993B"
ABBOTT = "T10-ABBOTT2016"
ISI = "T10-ISI2021"
LVK = "T10-LVK2025"
PEN = "T10-PENINGTON2020"
AEMM = "T10-ALMHEIRI2019"
APOL = "T10-APOLOGIA2025"
BLIND = "T10-BLINDERS2026"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "date": "2026-11-09",
    "order_label_en": "Reading order 9 of 9",
    "order_label_es": "Orden de lectura 9 de 9",
    "kicker_en": "Time & Gravity · T.10 · Where a clock can be seen to lose information, and the counting that says it should not",
    "kicker_es": "Tiempo y Gravedad · T.10 · Donde un reloj puede verse perdiendo información, y el conteo que dice que no debería",
    "title_en": "Page's Counting Argument",
    "title_es": "El Argumento de Conteo de Page",
    "standfirst_en": (
        "A black hole's horizon only grows, its entropy is its area, and it radiates. Hawking's calculation says the radiation carries "
        "no information and its entropy rises forever. Page's counting argument says that if the whole process is quantum mechanics, "
        "the radiation's entropy must turn over halfway and fall back to zero. This page builds the counting argument on ten qubits, "
        "checks it against Page's formula, and says plainly what in this story is measured, derived, and still open."
    ),
    "standfirst_es": (
        "El horizonte de un agujero negro solo crece, su entropía es su área, y radia. El cálculo de Hawking dice que la radiación no lleva "
        "información y su entropía sube para siempre. El argumento de conteo de Page dice que si todo el proceso es mecánica cuántica, la "
        "entropía de la radiación debe dar la vuelta a la mitad y volver a cero. Esta página construye el argumento de conteo con diez qubits, "
        "lo comprueba contra la fórmula de Page, y dice llanamente qué de esta historia está medido, derivado y todavía abierto."
    ),
    "seo": (
        "Page's Counting Argument: the Curve on Ten Qubits",
        "Hawking's rising entropy against Page's curve, built from random states on ten qubits and checked against Page's formula, with the area theorem's two tests.",
        "Argumento de Conteo de Page: la Curva en Diez Qubits",
        "La entropía creciente de Hawking frente a la curva de Page, construida con diez qubits y comprobada contra su fórmula, con dos pruebas del teorema del área.",
    ),
    "reading_time_en": "14 min read",
    "reading_time_es": "14 min de lectura",
    "central_number_en": "Haar-random toy on 10 qubits: radiation entropy matches Page's S(m,n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/2n within 0.002 nats at every cut (tolerance 0.03), peaks at 5 qubits (2.97 nats) and falls to 0.69 nats at 9",
    "central_number_es": "Juguete aleatorio de Haar con 10 qubits: la entropía de la radiación coincide con la S(m,n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/2n de Page dentro de 0.002 nats en cada corte (tolerancia 0.03), alcanza su máximo en 5 qubits (2.97 nats) y cae a 0.69 nats en 9",
    "verifier": "skills/timegravity/t10/verify_t10_page_curve.py",
    "generator": "skills/timegravity/t10/make_t10.py",
    "skill": "skills/timegravity/t10/SKILL.md",
    "skill_filename": "timegravity-t10-page-curve.SKILL.md",
    "open_question_en": "Where does the information go, in our universe?",
    "open_question_es": "¿A dónde va la información, en nuestro universo?",
    "ledger_ids": [ABBOTT, ISI, LVK, H71, BEK, H75, PAGEA, PAGEB, PEN, AEMM, APOL, BLIND],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any observation, theorem or derivation cited on this page. "
        "The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna observación, teorema o derivación citados en esta "
        "página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien mantiene el sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "page",
        "title_en": "Instrument · Hawking's line against Page's curve",
        "title_es": "Instrumento · La línea de Hawking frente a la curva de Page",
        "how_en": (
            "The plot shows the entropy of the radiation against the number of qubits that have left the black hole, out of N in all. The "
            "straight line is Hawking's: every emitted qubit is thermal, entropy rises by ln 2 each time, forever. The curve is Page's "
            "closed form for a random pure state of N qubits: it rises almost along Hawking's line, turns over at N/2, and falls back to zero "
            "when the last qubit leaves. The dots are a toy: random states on 10 qubits, each cut's entropy computed from the eigenvalues of the "
            "reduced state with the same pure-Python eigensolver the verifier uses. The N slider redraws the line and the curve. The knockout "
            "removes unitarity: the radiation is thermal all the way and the entropy never turns over, which is also the verifier's planted "
            "defect. The second button drops Page's correction term −(m−1)/2n to show how far the naive count misses. Keyboard: Tab and arrows. "
            "With reduced motion on, nothing animates."
        ),
        "how_es": (
            "La gráfica muestra la entropía de la radiación frente al número de qubits que han salido del agujero negro, de N en total. La recta "
            "es la de Hawking: cada qubit emitido es térmico, la entropía sube ln 2 cada vez, para siempre. La curva es la forma cerrada de Page "
            "para un estado puro aleatorio de N qubits: sube casi por la recta de Hawking, da la vuelta en N/2, y vuelve a cero cuando sale el "
            "último qubit. Los puntos son un juguete: estados aleatorios de 10 qubits, la entropía de cada corte calculada con los autovalores del "
            "estado reducido con el mismo solver en Python puro que usa el verificador. El deslizador N redibuja la recta y la curva. El apagado "
            "quita la unitariedad: la radiación es térmica todo el camino y la entropía nunca da la vuelta, que es también el defecto plantado del "
            "verificador. El segundo botón quita el término de corrección de Page −(m−1)/2n para mostrar cuánto falla el conteo ingenuo. Teclado: "
            "Tab y flechas. Con movimiento reducido, nada se anima."
        ),
    },
    "predict": {
        "q_en": "Before you move the slider: for a black hole made of N qubits that evaporates as ordinary quantum mechanics, when does the radiation's entropy peak?",
        "q_es": "Antes de mover el deslizador: para un agujero negro hecho de N qubits que se evapora como mecánica cuántica ordinaria, ¿cuándo alcanza su máximo la entropía de la radiación?",
        "options": [("After a quarter of the qubits", "Tras un cuarto de los qubits"), ("Halfway, at N/2", "A la mitad, en N/2"), ("Only at the very end", "Solo al final")],
        "answer": 1,
        "reveal_en": "Halfway. Page's counting says the smaller half of a random pure state is almost maximally entangled with the larger, so the entropy tracks the smaller side and peaks when the two halves are equal.",
        "reveal_es": "A la mitad. El conteo de Page dice que la mitad más pequeña de un estado puro aleatorio está casi máximamente entrelazada con la mayor, así que la entropía sigue al lado pequeño y alcanza su máximo cuando las dos mitades son iguales.",
    },
    "sections": [
        {"type": "h2", "id": "measured", "en": "I · What has been observed", "es": "I · Lo que se ha observado", "short_en": "I · Observed", "short_es": "I · Observado"},
        P(
            C("MEASURED", [ABBOTT, ISI],
              "Pairs of black holes merge, and the signals, including the remnant's ringdown, are consistent with general relativity: the first gravitational-wave "
              "signal, GW150914, was observed in 2015 by the LIGO and Virgo collaborations, and the same public data were reanalysed "
              "independently in 2021 to test the area theorem.",
              "Pares de agujeros negros se fusionan, y las señales, incluida la resonancia del remanente, son consistentes con la relatividad general: la primera señal de "
              "ondas gravitacionales, GW150914, fue observada en 2015 por las colaboraciones LIGO y Virgo, y los mismos datos públicos fueron "
              "reanalizados de forma independiente en 2021 para poner a prueba el teorema del área."),
            T(" Those two rows are what every DERIVED statement on this page is about: the black holes we have actually seen.",
              " Esas dos filas son de lo que trata cada afirmación DERIVADA de esta página: los agujeros negros que realmente hemos visto."),
        ),
        P(
            C("SINGLE RESULT", [ISI],
              "The 2021 reanalysis of GW150914 found the remnant's horizon area larger than the sum of the two initial areas, the first test "
              "of Hawking's area theorem on a real signal.",
              "El reanálisis de 2021 de GW150914 encontró el área del horizonte del remanente mayor que la suma de las dos áreas iniciales, la "
              "primera prueba del teorema del área de Hawking en una señal real."),
            T(" ", " "),
            C("SINGLE RESULT", [LVK],
              "In 2025 the LIGO, Virgo and KAGRA collaborations reported GW250114, a binary black hole signal with a network signal-to-noise "
              "ratio of 80, and stated that the remnant area is larger than the sum of the initial areas to high credibility, with the ringdown "
              "mode frequencies constrained to within 30 percent of the Kerr spectrum.",
              "En 2025 las colaboraciones LIGO, Virgo y KAGRA reportaron GW250114, una señal de agujeros negros binarios con una relación señal a "
              "ruido de red de 80, y afirmaron que el área del remanente es mayor que la suma de las áreas iniciales con alta credibilidad, con las "
              "frecuencias de los modos de resonancia acotadas dentro del 30 por ciento del espectro de Kerr."),
            T(" The figure is quoted as the paper's own claim; this page does not recompute it. Plugging published median masses into the area "
              "formula would look like a test and would not be one, because the result comes from posterior sampling, not from medians.",
              " La cifra se cita como afirmación propia del artículo; esta página no la recalcula. Sustituir masas medianas publicadas en la "
              "fórmula del área parecería una prueba y no lo sería, porque el resultado viene de muestreo posterior, no de medianas."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("Burn a book and the smoke looks random, but in principle every letter is still in the smoke, scrambled. Hawking's 1975 "
                 "calculation said a black hole is different: its smoke is truly random, and the book is gone. Page's argument says: if a black "
                 "hole is a quantum system like any other, then after half of it has turned to smoke, the smoke must start carrying the book, "
                 "and by the end the smoke holds everything. Draw the amount of randomness in the smoke over time and you get a hill, not a slope.",
                 "Quema un libro y el humo se ve aleatorio, pero en principio cada letra sigue en el humo, revuelta. El cálculo de Hawking de 1975 "
                 "decía que un agujero negro es distinto: su humo es verdaderamente aleatorio, y el libro desaparece. El argumento de Page dice: si "
                 "un agujero negro es un sistema cuántico como cualquier otro, entonces después de que la mitad se ha vuelto humo, el humo debe "
                 "empezar a cargar el libro, y al final el humo lo guarda todo. Dibuja la cantidad de aleatoriedad del humo en el tiempo y obtienes una loma, no una pendiente.")),
             P(T("The hill is not a theory of black holes. It is counting: what a random quantum state of N parts must look like from any one "
                 "part. The open question is how gravity manages to make the real smoke follow the hill, and whether it does.",
                 "La loma no es una teoría de agujeros negros. Es conteo: cómo debe verse un estado cuántico aleatorio de N partes desde cualquiera "
                 "de ellas. La pregunta abierta es cómo logra la gravedad que el humo real siga la loma, y si lo hace.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: a shuffled deck is dealt one card at a time. Early on, knowing the dealt cards tells you almost nothing "
                 "about the rest. Past the halfway point, every new card is mostly predictable from what is already on the table. The "
                 "uncertainty in the dealt pile rises, peaks at the middle, and falls to nothing when the last card lands. Page's curve is "
                 "that, for quantum cards.",
                 "Analogía cotidiana: una baraja revuelta se reparte una carta a la vez. Al principio, conocer las cartas repartidas te dice casi "
                 "nada del resto. Pasada la mitad, cada carta nueva es casi predecible a partir de lo que ya está en la mesa. La incertidumbre en el "
                 "montón repartido sube, alcanza su máximo a la mitad, y cae a nada cuando aterriza la última carta. La curva de Page es eso, para cartas cuánticas.")),
             P(T("How the controls work in plain words: the N slider is the size of the deck. The straight line is a dealer who burns each card "
                 "after showing it, so the pile's uncertainty only grows; that is the knockout, and nothing on the table ever lets you predict a "
                 "card. The second button uses a slightly wrong counting rule to show that the exact hill needs Page's small correction.",
                 "Cómo funcionan los controles en palabras sencillas: el deslizador N es el tamaño de la baraja. La recta es un repartidor que quema "
                 "cada carta después de mostrarla, así que la incertidumbre del montón solo crece; ese es el apagado, y nada en la mesa te deja "
                 "predecir una carta. El segundo botón usa una regla de conteo ligeramente equivocada para mostrar que la loma exacta necesita la pequeña corrección de Page.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "derived", "en": "II · Area, entropy, radiation, and the counting", "es": "II · Área, entropía, radiación y el conteo", "short_en": "II · Derived", "short_es": "II · Derivado"},
        P(
            C("DERIVED", [H71, ABBOTT],
              "In classical general relativity the total horizon area of black holes never decreases: Hawking's 1971 area theorem, which "
              "is the statement the two gravitational-wave tests above examine.",
              "En la relatividad general clásica el área total de los horizontes de los agujeros negros nunca disminuye: el teorema del área de "
              "Hawking de 1971, que es el enunciado que examinan las dos pruebas de ondas gravitacionales de arriba.",
              parent=ABBOTT),
            T(" ", " "),
            C("DERIVED", [BEK, H75, ABBOTT],
              "Bekenstein argued in 1973 that a black hole carries an entropy proportional to its horizon area, and Hawking showed in 1975 "
              "that a black hole radiates thermally at a temperature fixed by its mass, so that it loses mass and, in that calculation, "
              "returns no information about what fell in.",
              "Bekenstein sostuvo en 1973 que un agujero negro lleva una entropía proporcional al área de su horizonte, y Hawking mostró en 1975 "
              "que un agujero negro radia térmicamente a una temperatura fijada por su masa, de modo que pierde masa y, en ese cálculo, no "
              "devuelve información sobre lo que cayó.",
              parent=ABBOTT),
            T(" That is the straight line in the instrument: thermal radiation whose entropy rises by one bit per emitted qubit without end.",
              " Esa es la recta del instrumento: radiación térmica cuya entropía sube un bit por qubit emitido sin fin."),
        ),
        {"type": "equation", "text": "S(m, n) = Σ_{k=n+1}^{mn} 1/k − (m − 1)/(2n),   m ≤ n   (Page 1993)"},
        P(
            C("DERIVED", [PAGEA, PAGEB, ABBOTT],
              "Page showed in 1993 that for a random pure state on a Hilbert space of dimension mn the average entanglement entropy of the "
              "m-dimensional part is S(m, n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n), only slightly below the maximum ln m, and applied it to an "
              "evaporating black hole: if the hole and its radiation together are in a pure state, the radiation's entropy rises almost "
              "thermally, turns over when half the degrees of freedom have been emitted, and returns to zero.",
              "Page mostró en 1993 que para un estado puro aleatorio en un espacio de Hilbert de dimensión mn la entropía de entrelazamiento "
              "promedio de la parte de dimensión m es S(m, n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n), solo un poco por debajo del máximo ln m, y lo "
              "aplicó a un agujero negro en evaporación: si el agujero y su radiación están juntos en un estado puro, la entropía de la radiación "
              "sube casi térmicamente, da la vuelta cuando se ha emitido la mitad de los grados de libertad, y vuelve a cero.",
              parent=ABBOTT),
            T(" The verifier draws eight random pure states on ten qubits, computes the entropy of every cut from the eigenvalues of the reduced "
              "state with a pure-Python Jacobi solver, and finds the average within 0.002 nats of Page's formula at every cut, peaking at five "
              "qubits with 2.97 nats and ending at 0.69 nats. The check is against the formula; the random numbers are only the sample.",
              " El verificador toma ocho estados puros aleatorios de diez qubits, calcula la entropía de cada corte con los autovalores del estado "
              "reducido mediante un solver de Jacobi en Python puro, y encuentra el promedio dentro de 0.002 nats de la fórmula de Page en cada corte, "
              "con máximo en cinco qubits con 2.97 nats y final en 0.69 nats. La comprobación es contra la fórmula; los números aleatorios son solo la muestra."),
        ),
        P(
            C("DERIVED", [PEN, AEMM, ABBOTT],
              "In 2019 and 2020 two groups showed that within semiclassical gravity the entropy of the radiation, computed with the quantum "
              "extremal surface prescription, follows Page's curve: after the halfway point a region inside the black hole, an island, "
              "belongs to the radiation's entanglement wedge.",
              "En 2019 y 2020 dos grupos mostraron que dentro de la gravedad semiclásica la entropía de la radiación, calculada con la prescripción "
              "de superficie extremal cuántica, sigue la curva de Page: después de la mitad una región dentro del agujero negro, una isla, "
              "pertenece a la cuña de entrelazamiento de la radiación.",
              parent=ABBOTT),
            T(" That is a derivation inside a framework, not a mechanism anyone has observed, and the toy on this page contains no island; it "
              "contains only the counting.",
              " Eso es una derivación dentro de un marco, no un mecanismo que alguien haya observado, y el juguete de esta página no contiene "
              "ninguna isla; contiene solo el conteo."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "open", "en": "III · What this page does not say", "es": "III · Lo que esta página no dice", "short_en": "III · Not said", "short_es": "III · No dicho"},
        P(
            C("PROPOSED", [APOL, BLIND],
              "Two 2025 and 2026 preprints take opposite sides on what the island calculation means: one argues for islands as the mechanism "
              "behind the curve, the other argues that islands only redistribute information when a detector has a blind spot and that the "
              "asymptotic algebra is already complete.",
              "Dos prepublicaciones de 2025 y 2026 toman lados opuestos sobre lo que significa el cálculo de islas: una argumenta a favor de las islas como el "
              "mecanismo detrás de la curva, la otra sostiene que las islas solo redistribuyen información cuando un detector tiene un punto ciego y "
              "que el álgebra asintótica ya está completa."),
            T(" Both are preprints and neither can rise above PROPOSED here. Unitarity is near consensus; the mechanism is not.",
              " Ambas son prepublicaciones y ninguna puede subir de PROPUESTO aquí. La unitariedad es casi consenso; el mecanismo no."),
        ),
        P(
            C("OPEN", [PAGEB, PEN],
              "Where the information goes in our universe, with its positive cosmological constant and no asymptotic boundary to hold the "
              "radiation, is not settled: the curve is a counting result, and the derivations that reproduce it live in frameworks whose "
              "application to our spacetime is itself open.",
              "A dónde va la información en nuestro universo, con su constante cosmológica positiva y sin frontera asintótica que contenga la "
              "radiación, no está resuelto: la curva es un resultado de conteo, y las derivaciones que la reproducen viven en marcos cuya "
              "aplicación a nuestro espaciotiempo es en sí misma abierta."),
            T(" This is the last page of the track, and it ends where the hub began: with a question. The slope in the rate of time is measured "
              "to a part in 10¹⁵; what happens to a clock's record when the slope becomes a horizon is counted, derived in pieces, and not yet seen.",
              " Esta es la última página de la serie, y termina donde empezó el punto de partida: con una pregunta. La pendiente en el ritmo del "
              "tiempo está medida a una parte en 10¹⁵; qué pasa con el registro de un reloj cuando la pendiente se vuelve un horizonte está contado, "
              "derivado por partes, y todavía no visto."),
        ),
        {"type": "change_box",
         "items": [
             ("A second independent analysis confirming the GW250114 area result would raise that row from SINGLE RESULT to MEASURED alongside the GW150914 test.",
              "Un segundo análisis independiente que confirmara el resultado de área de GW250114 subiría esa fila de RESULTADO ÚNICO a MEDIDO junto a la prueba de GW150914."),
             ("Peer-reviewed publication of either 2025 or 2026 preprint would move its row from PROPOSED to DERIVED, and the dispute would be stated as a reviewed one.",
              "La publicación revisada por pares de cualquiera de las prepublicaciones de 2025 o 2026 movería su fila de PROPUESTO a DERIVADO, y la disputa se enunciaría como revisada."),
             ("If the toy's averaged entropies ever missed Page's formula by more than 0.03 nats at any cut, the verifier fails and the page does not build.",
              "Si las entropías promediadas del juguete llegaran a fallar la fórmula de Page por más de 0.03 nats en algún corte, el verificador falla y la página no se construye."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · The counting", "Etapa 1 · El conteo",
         "A pure state on N qubits, split into a emitted qubits (dimension m = 2ᵃ) and N − a remaining (n = 2^{N−a}). For a Haar-random state the average entropy of the smaller part is Page's S(m, n); entropy is the same seen from either side.",
         "Un estado puro de N qubits, dividido en a qubits emitidos (dimensión m = 2ᵃ) y N − a restantes (n = 2^{N−a}). Para un estado aleatorio de Haar la entropía promedio de la parte menor es la S(m, n) de Page; la entropía es la misma vista desde cualquier lado."),
        ("Stage 2 · The toy", "Etapa 2 · El juguete",
         "Eight random complex vectors on 2¹⁰ dimensions (Gaussian components, normalised; fixed seed so the artefact regenerates byte for byte). For each cut the reduced density matrix of the smaller side (at most 32×32) is embedded as a real symmetric 64×64 matrix and diagonalised with cyclic Jacobi; S = −Σ λ ln λ.",
         "Ocho vectores complejos aleatorios en 2¹⁰ dimensiones (componentes gaussianas, normalizadas; semilla fija para que el artefacto se regenere byte por byte). Para cada corte la matriz de densidad reducida del lado menor (a lo más 32×32) se incrusta como matriz real simétrica de 64×64 y se diagonaliza con Jacobi cíclico; S = −Σ λ ln λ."),
        ("Stage 3 · The assertion", "Etapa 3 · La aserción",
         "The sample mean at every cut must lie within 0.03 nats of Page's closed form (it lies within 0.002), the curve must be symmetric about N/2 and must fall to less than half its peak at the last cut. The assertion is against the formula, never against the random numbers themselves.",
         "La media muestral en cada corte debe quedar dentro de 0.03 nats de la forma cerrada de Page (queda dentro de 0.002), la curva debe ser simétrica respecto a N/2 y debe caer a menos de la mitad de su máximo en el último corte. La aserción es contra la fórmula, nunca contra los números aleatorios mismos."),
        ("Stage 4 · The defect", "Etapa 4 · El defecto",
         "The planted defect replaces the toy's entropies by Hawking's line a·ln 2, a non-unitary model that never turns over; the 'falls to less than half its peak' check fails, as it must, and the page does not build.",
         "El defecto plantado reemplaza las entropías del juguete por la recta de Hawking a·ln 2, un modelo no unitario que nunca da la vuelta; la prueba de 'cae a menos de la mitad de su máximo' falla, como debe, y la página no se construye."),
    ],
    "sidenotes": [
        ("SIDENOTE T.10-A · WHY NOT RECOMPUTE THE AREA TEST", "NOTA T.10-A · POR QUÉ NO RECALCULAR LA PRUEBA DEL ÁREA",
         "The GW250114 result comes from sampling the full posterior over masses and spins, before and after the merger. Feeding published medians into the area formula would produce a number that looks like a test and tests nothing. The page quotes the paper and stops.",
         "El resultado de GW250114 viene de muestrear la posterior completa sobre masas y espines, antes y después de la fusión. Alimentar medianas publicadas a la fórmula del área produciría un número que parece una prueba y no prueba nada. La página cita el artículo y se detiene."),
        ("SIDENOTE T.10-B · WHAT THE TOY LACKS", "NOTA T.10-B · LO QUE LE FALTA AL JUGUETE",
         "No gravity, no horizon, no island. Ten qubits and a random state. It shows what any quantum system must do; it says nothing about how a black hole does it.",
         "Sin gravedad, sin horizonte, sin isla. Diez qubits y un estado aleatorio. Muestra lo que cualquier sistema cuántico debe hacer; no dice nada de cómo lo hace un agujero negro."),
    ],
    "sources": [
        ("Abbott, B. P., et al. (LIGO Scientific Collaboration and Virgo Collaboration) (2016). Observation of gravitational waves from a binary black hole merger. Physical Review Letters, 116(6), 061102.", "10.1103/PhysRevLett.116.061102"),
        ("Isi, M., Farr, W. M., Giesler, M., Scheel, M. A., & Teukolsky, S. A. (2021). Testing the black-hole area law with GW150914. Physical Review Letters, 127(1), 011103.", "10.1103/PhysRevLett.127.011103"),
        ("Abac, A. G., et al. (LIGO Scientific, Virgo and KAGRA Collaborations) (2025). GW250114: Testing Hawking's area law and the Kerr nature of black holes. Physical Review Letters, 135, 111403.", "10.1103/kw5g-d732"),
        ("Hawking, S. W. (1971). Gravitational radiation from colliding black holes. Physical Review Letters, 26(21), 1344–1346.", "10.1103/PhysRevLett.26.1344"),
        ("Bekenstein, J. D. (1973). Black holes and entropy. Physical Review D, 7(8), 2333–2346.", "10.1103/PhysRevD.7.2333"),
        ("Hawking, S. W. (1975). Particle creation by black holes. Communications in Mathematical Physics, 43(3), 199–220.", "10.1007/BF02345020"),
        ("Page, D. N. (1993). Average entropy of a subsystem. Physical Review Letters, 71(9), 1291–1294.", "10.1103/PhysRevLett.71.1291"),
        ("Page, D. N. (1993). Information in black hole radiation. Physical Review Letters, 71(23), 3743–3746.", "10.1103/PhysRevLett.71.3743"),
        ("Penington, G. (2020). Entanglement wedge reconstruction and the information paradox. Journal of High Energy Physics, 2020(9), 2.", "10.1007/JHEP09(2020)002"),
        ("Almheiri, A., Engelhardt, N., Marolf, D., & Maxfield, H. (2019). The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole. Journal of High Energy Physics, 2019(12), 63.", "10.1007/JHEP12(2019)063"),
        ("Antonini, S., Chen, Y., Maxfield, H., & Penington, G. (2025). An apologia for islands. arXiv preprint (not peer reviewed).", "10.48550/arXiv.2506.04311"),
        ("Geng, H., Karch, A., Perez-Pardavila, C., Raju, S., Randall, L., & Riojas, M. (2026). Seeing Page curves and islands with blinders on. arXiv preprint (not peer reviewed).", "10.48550/arXiv.2602.06543"),
    ],
}
