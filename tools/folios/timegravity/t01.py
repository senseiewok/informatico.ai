# -*- coding: utf-8 -*-
"""Time & Gravity · T.01 — Gravity as a slope in the rate of time.

Instrument: a 1+1 geodesic integrator in which only the time-time metric component varies with height.
The particle falls at g with no force term; flatten the gradient (knockout) and nothing falls.
Verifier: skills/timegravity/t01/verify_t01_time_slope_geodesic.py recomputes a = g within 1e-6 relative
and fails on a sign flip (planted defect).
"""
from __future__ import annotations

from ._model import C, H3, P, T

SLUG = "t01"
CODE = "T.01"

# Ledger rows this page cites (timegravity/ledger.json).
PR = "T01-PR1960"
HKP = "T01-HK1972P"
HKO = "T01-HK1972O"
GPA = "T01-GPA1980"
CHOU = "T01-CHOU2010"
BOTH = "T01-BOTH2022"
EIN = "T01-EIN1911"
WILL = "T01-WILL2014"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "order_label_en": "Step 3 of 14",
    "order_label_es": "Paso 3 de 14",
    "kicker_en": "Time & Gravity · T.01 · The best-measured half of the intuition",
    "kicker_es": "Tiempo y Gravedad · T.01 · La mitad mejor medida de la intuición",
    "title_en": "Gravity as a Slope in the Rate of Time",
    "title_es": "La Gravedad como Pendiente en el Ritmo del Tiempo",
    "standfirst_en": (
        "Clocks lower in a gravity well run slower than clocks above them. For a slow body, that one measured fact "
        "is enough to make it fall: integrate a worldline through a metric whose only varying piece is the rate of "
        "time, and the body accelerates downward at g with no force written anywhere. Flatten the gradient and nothing falls."
    ),
    "standfirst_es": (
        "Los relojes más abajo en un pozo gravitatorio avanzan más lento que los relojes arriba. Para un cuerpo lento, "
        "ese único hecho medido basta para hacerlo caer: integra una línea de mundo en una métrica cuya única pieza "
        "variable es el ritmo del tiempo, y el cuerpo acelera hacia abajo a g sin que haya una fuerza escrita en ningún "
        "lado. Aplana el gradiente y nada cae."
    ),
    "seo": (
        "Gravity as a Slope in the Rate of Time",
        "How measured clock-rate differences between heights make a slow body fall at g with no force term, with a live geodesic instrument and a Python verifier.",
        "La Gravedad como Pendiente en el Ritmo del Tiempo",
        "Cómo las diferencias medidas en el ritmo de relojes a distintas alturas hacen caer un cuerpo a g sin término de fuerza, con instrumento y verificador.",
    ),
    "reading_time_en": "14 min read",
    "reading_time_es": "14 min de lectura",
    "central_number_en": "a = −9.80665 m/s² recomputed from the clock-rate gradient alone, within 1e-6 relative",
    "central_number_es": "a = −9.80665 m/s² recalculada solo desde el gradiente del ritmo de los relojes, dentro de 1e-6 relativo",
    "verifier": "skills/timegravity/t01/verify_t01_time_slope_geodesic.py",
    "generator": "skills/timegravity/t01/make_t01.py",
    "skill": "skills/timegravity/t01/SKILL.md",
    "open_question_en": "What sets the slope?",
    "open_question_es": "¿Qué fija la pendiente?",
    "next_code": "T.03",
    "next_title_en": "What sets the slope",
    "next_title_es": "Qué fija la pendiente",
    "next_built": False,
    "prev_code": "T.00",
    "prev_title_en": "The hub",
    "prev_title_es": "El punto de partida",
    "ledger_ids": [PR, HKP, HKO, GPA, CHOU, BOTH, EIN, WILL],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any measurement or derivation cited on "
        "this page. The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer "
        "against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna medición o derivación "
        "citada en esta página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien "
        "mantiene el sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "title_en": "Instrument · A worldline falls through a slope in the rate of time",
        "title_es": "Instrumento · Una línea de mundo cae por una pendiente en el ritmo del tiempo",
        "how_en": (
            "Left: the rate of a clock at each height, drawn as a shaded column; darker means slower. Right: the worldline "
            "of a body released at rest, integrated step by step through a metric in which only the time-time component "
            "varies with height. The gradient slider scales the slope relative to Earth's surface value. The knockout flattens "
            "the gradient to zero: every clock then ticks at the same rate and the body stays where it was released. The sign "
            "flip is the verifier's planted defect: a slope the wrong way makes the body rise. Keyboard: Tab to a control, "
            "arrows to change it. With reduced motion on, the trajectory is drawn at once instead of animated."
        ),
        "how_es": (
            "Izquierda: el ritmo de un reloj a cada altura, dibujado como una columna sombreada; más oscuro significa más lento. "
            "Derecha: la línea de mundo de un cuerpo soltado en reposo, integrada paso a paso en una métrica donde solo la "
            "componente tiempo-tiempo varía con la altura. El deslizador de gradiente escala la pendiente respecto al valor en la "
            "superficie terrestre. El apagado aplana el gradiente a cero: todos los relojes marchan al mismo ritmo y el cuerpo se "
            "queda donde se soltó. El cambio de signo es el defecto plantado del verificador: una pendiente al revés hace subir al "
            "cuerpo. Teclado: Tab hasta un control y flechas para cambiarlo. Con movimiento reducido, la trayectoria se dibuja de "
            "una vez en lugar de animarse."
        ),
    },
    "sections": [
        {"type": "h2", "id": "measured", "en": "I · What was measured, and how well", "es": "I · Qué se midió, y con qué precisión", "short_en": "I · Measured", "short_es": "I · Medido"},
        P(
            C("MEASURED", [PR, HKP, HKO, GPA, CHOU],
              "A clock lower in Earth's gravitational field runs slower than an identical clock above it, and in the weak field "
              "the fractional rate difference between two heights separated by h is gh/c².",
              "Un reloj más abajo en el campo gravitatorio terrestre avanza más lento que un reloj idéntico arriba de él, y en el "
              "campo débil la diferencia fraccional de ritmo entre dos alturas separadas por h es gh/c²."),
            T(" That sentence carries the label MEASURED because at least two independent collaborations measured it with "
              "peer-reviewed results decades apart, from a 22.5 metre tower to a rocket.",
              " Esa oración lleva la etiqueta MEDIDO porque al menos dos colaboraciones independientes la midieron con resultados "
              "revisados por pares, con décadas de diferencia, desde una torre de 22.5 metros hasta un cohete."),
        ),
        P(
            C("MEASURED", [PR, CHOU],
              "In 1960 Pound and Rebka sent gamma rays up and down a 22.5 metre tower at Harvard and used the Mössbauer effect to "
              "resolve the frequency shift; the difference between the two directions came out at (5.13 ± 0.51) × 10⁻¹⁵ against a "
              "predicted 4.92 × 10⁻¹⁵, a ratio of 1.05 ± 0.10.",
              "En 1960 Pound y Rebka enviaron rayos gamma hacia arriba y hacia abajo por una torre de 22.5 metros en Harvard y usaron "
              "el efecto Mössbauer para resolver el corrimiento de frecuencia; la diferencia entre ambas direcciones resultó "
              "(5.13 ± 0.51) × 10⁻¹⁵ frente a un valor predicho de 4.92 × 10⁻¹⁵, una razón de 1.05 ± 0.10."),
            T(" The number that matters for this page is not the precision but the sign: the photon climbing out lost frequency, "
              "exactly as a clock at the bottom would be seen to run slow from the top. Each experiment below carries MEASURED because the "
              "ledger pairs its row with an independent measurement of the same gh/c² at another height; one row alone would read SINGLE RESULT.",
              " El número que importa para esta página no es la precisión sino el signo: el fotón que subía perdió frecuencia, "
              "exactamente como un reloj en la base se vería lento desde arriba. Cada experimento de abajo lleva MEDIDO porque el libro de "
              "registro empareja su fila con una medición independiente del mismo gh/c² a otra altura; una sola fila se leería RESULTADO ÚNICO."),
        ),
        P(
            C("MEASURED", [HKP, HKO, GPA],
              "In 1971 Hafele and Keating flew caesium clocks around the world on commercial flights, eastward and westward, and "
              "compared them with clocks left at the United States Naval Observatory; the gravitational part of the predicted gain "
              "came from the aircraft's altitude, and the observed totals, −59 ± 10 ns eastward and 273 ± 7 ns westward, agreed with "
              "the predictions of −40 ± 23 ns and 275 ± 21 ns.",
              "En 1971 Hafele y Keating volaron relojes de cesio alrededor del mundo en vuelos comerciales, hacia el este y hacia el "
              "oeste, y los compararon con relojes que se quedaron en el Observatorio Naval de Estados Unidos; la parte gravitatoria "
              "de la ganancia predicha venía de la altitud del avión, y los totales observados, −59 ± 10 ns hacia el este y 273 ± 7 ns "
              "hacia el oeste, coincidieron con las predicciones de −40 ± 23 ns y 275 ± 21 ns."),
            T(" Two papers, one predicting and one reporting, are two rows in the ledger below; together with Pound and Rebka they are "
              "why the first claim on this page may say MEASURED.",
              " Dos artículos, uno que predice y otro que reporta, son dos filas en el libro de registro de abajo; junto con Pound y "
              "Rebka son la razón por la que la primera afirmación de esta página puede decir MEDIDO."),
        ),
        P(
            C("MEASURED", [GPA, PR],
              "In 1976 Gravity Probe A carried a hydrogen maser on a rocket to about 10,000 km and compared its rate with a maser on "
              "the ground throughout the flight; the 1980 report found agreement with the predicted gravitational frequency shift to "
              "about 70 parts per million.",
              "En 1976 Gravity Probe A llevó un máser de hidrógeno en un cohete hasta unos 10,000 km y comparó su ritmo con un máser en "
              "tierra durante todo el vuelo; el reporte de 1980 encontró acuerdo con el corrimiento gravitatorio de frecuencia predicho "
              "a unas 70 partes por millón."),
            T(" ", " "),
            C("MEASURED", [CHOU, PR],
              "In 2010 Chou and colleagues at NIST compared two aluminium-ion optical clocks and raised one by 33 cm; the measured "
              "fractional shift was (4.1 ± 1.6) × 10⁻¹⁷, against a predicted 3.6 × 10⁻¹⁷.",
              "En 2010 Chou y colegas en el NIST compararon dos relojes ópticos de ion de aluminio y elevaron uno 33 cm; el corrimiento "
              "fraccional medido fue (4.1 ± 1.6) × 10⁻¹⁷, frente a un valor predicho de 3.6 × 10⁻¹⁷."),
            T(" A tower, an airliner, a rocket and a laboratory bench: the slope in the rate of time has the same sign and the same "
              "size, gh/c², at every one of them.",
              " Una torre, un avión de línea, un cohete y una mesa de laboratorio: la pendiente en el ritmo del tiempo tiene el mismo "
              "signo y el mismo tamaño, gh/c², en todos ellos."),
        ),
        P(
            C("SINGLE RESULT", [BOTH],
              "In 2022 Bothwell and colleagues at JILA resolved the gravitational redshift across a single millimetre inside one "
              "cloud of strontium atoms, consistent with general relativity at the 10⁻¹⁹ level.",
              "En 2022 Bothwell y colegas en JILA resolvieron el corrimiento gravitatorio al rojo a lo largo de un solo milímetro "
              "dentro de una misma nube de átomos de estroncio, consistente con la relatividad general al nivel de 10⁻¹⁹."),
            T(" That row is labelled SINGLE RESULT, not MEASURED: it is one experiment from a single collaboration at that millimetre "
              "scale, and the label will rise only when a second collaboration resolves the same gradient. The label is "
              "a statement about the evidence, not a doubt about the team.",
              " Esa fila lleva la etiqueta RESULTADO ÚNICO, no MEDIDO: es un solo experimento de una sola colaboración a esa escala "
              "milimétrica, y la etiqueta subirá solo cuando una segunda colaboración resuelva el mismo "
              "gradiente. La etiqueta habla de la evidencia, no duda del equipo."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("Imagine two identical clocks. Put one on the floor and one on a shelf. Wait a very long time and compare them. "
                 "The clock on the floor is behind, by an amount so small that only atomic clocks can see it, but it is behind every time, "
                 "in every laboratory that has ever tried. Nothing on this page asks you to believe more than that.",
                 "Imagina dos relojes idénticos. Pon uno en el piso y otro en una repisa. Espera muchísimo tiempo y compáralos. El reloj "
                 "del piso va atrasado, por una cantidad tan pequeña que solo los relojes atómicos la ven, pero va atrasado cada vez, en "
                 "cada laboratorio que lo ha intentado. Nada en esta página te pide creer más que eso.")),
             P(T("Now ask what a thing does if the lower part of it lives in slightly slower time than the upper part. The answer the "
                 "instrument shows is that it drifts toward the slow side, faster and faster, at exactly the rate we call falling. No push "
                 "is needed. The slope in the rate of time is enough.",
                 "Ahora pregúntate qué hace un objeto si su parte baja vive en un tiempo ligeramente más lento que su parte alta. La "
                 "respuesta que muestra el instrumento es que deriva hacia el lado lento, cada vez más rápido, exactamente al ritmo que "
                 "llamamos caer. No hace falta ningún empujón. La pendiente en el ritmo del tiempo basta.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: a line of marchers walks straight across a field, arm in arm. The grass on the left is wet and "
                 "slows the left end of the line a little. Nobody turns on purpose, yet the whole line curves toward the slow side, because "
                 "the left end covers less ground per step. A worldline through a slope in the rate of time curves the same way, toward where "
                 "time runs slower, which is downward.",
                 "Analogía cotidiana: una fila de personas camina en línea recta por un campo, tomadas del brazo. El pasto de la "
                 "izquierda está mojado y frena un poco el extremo izquierdo de la fila. Nadie gira a propósito, pero toda la fila se curva "
                 "hacia el lado lento, porque el extremo izquierdo avanza menos por paso. Una línea de mundo que cruza una pendiente en el "
                 "ritmo del tiempo se curva igual, hacia donde el tiempo corre más lento, que es hacia abajo.")),
             P(T("How the controls work in plain words: the gradient slider makes the wet grass wetter or drier, so the line curves "
                 "more or less. The knockout dries the whole field, so the line walks straight and the body never moves. The sign flip "
                 "wets the right side instead, so the line curves the other way and the body rises. The readouts report the slope, the "
                 "acceleration the instrument measures from the trajectory, and how far that is from g.",
                 "Cómo funcionan los controles en palabras sencillas: el deslizador de gradiente moja o seca el pasto, así que la fila "
                 "se curva más o menos. El apagado seca todo el campo, la fila camina recto y el cuerpo nunca se mueve. El cambio de signo "
                 "moja el lado derecho, la fila se curva al revés y el cuerpo sube. Las lecturas reportan la pendiente, la aceleración que "
                 "el instrumento mide en la trayectoria y qué tan lejos está de g.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "derived", "en": "II · From a clock-rate gradient to a fall, with no force term", "es": "II · De un gradiente en el ritmo de los relojes a una caída, sin término de fuerza", "short_en": "II · Derived", "short_es": "II · Derivado"},
        P(
            T("Write the line element of a 1+1 spacetime in which only the time-time component depends on height z:",
              "Escribe el elemento de línea de un espaciotiempo 1+1 donde solo la componente tiempo-tiempo depende de la altura z:"),
        ),
        {"type": "equation", "text": "ds² = −A(z) c² dt² + dz²,   A(z) = 1 + 2 g z / c²"},
        P(
            C("DERIVED", [EIN, PR],
              "In the weak field the Newtonian potential sits in the time-time component, A(z) ≈ 1 + 2Φ(z)/c², and the measured "
              "clock-rate ratio between two heights is √A(z₂)/√A(z₁) ≈ 1 + g(z₂ − z₁)/c², the same gh/c² that the experiments above report.",
              "En el campo débil el potencial newtoniano vive en la componente tiempo-tiempo, A(z) ≈ 1 + 2Φ(z)/c², y la razón medida de "
              "ritmos de reloj entre dos alturas es √A(z₂)/√A(z₁) ≈ 1 + g(z₂ − z₁)/c², el mismo gh/c² que reportan los experimentos de arriba.",
              parent=PR),
            T(" This carries the label DERIVED: it names its parent MEASURED row, and it follows from the metric by algebra, not by a "
              "new measurement.",
              " Esto lleva la etiqueta DERIVADO: nombra su fila MEDIDA madre y se sigue de la métrica por álgebra, no por una medición nueva."),
        ),
        P(
            C("DERIVED", [EIN, PR],
              "The geodesic equation for a body released at rest in that metric has a single surviving connection term, "
              "Γᶻₜₜ = A′(z)/2 in units where x⁰ = ct, so d²z/dτ² = −(A′/2)(c dt/dτ)², and for a slow body (dt/dτ ≈ 1) this is "
              "d²z/dt² ≈ −(c²/2) A′(z) = −g: the body falls at g, and no force appears anywhere in the equation.",
              "La ecuación geodésica para un cuerpo soltado en reposo en esa métrica tiene un solo término de conexión que sobrevive, "
              "Γᶻₜₜ = A′(z)/2 en unidades con x⁰ = ct, así que d²z/dτ² = −(A′/2)(c dt/dτ)², y para un cuerpo lento (dt/dτ ≈ 1) esto es "
              "d²z/dt² ≈ −(c²/2) A′(z) = −g: el cuerpo cae a g, y ninguna fuerza aparece en la ecuación.",
              parent=PR),
            T(" The instrument above integrates exactly this system with a fourth-order Runge–Kutta step, and the verifier beside the "
              "page recomputes the acceleration from the trajectory and demands |a + g|/g < 10⁻⁶.",
              " El instrumento de arriba integra exactamente este sistema con un paso de Runge–Kutta de cuarto orden, y el verificador "
              "junto a la página recalcula la aceleración desde la trayectoria y exige |a + g|/g < 10⁻⁶."),
        ),
        P(
            T("The knockout is the argument. Set A′(z) = 0 and the connection term vanishes: every clock ticks at the same rate, the "
              "worldline is a straight vertical line in the diagram, and the body never leaves the height where it was released. Flip the "
              "sign of A′ and the body rises, which is the verifier's planted defect; a page whose verifier accepts that trajectory does not ship.",
              "El apagado es el argumento. Pon A′(z) = 0 y el término de conexión desaparece: cada reloj marcha al mismo ritmo, la línea de "
              "mundo es una vertical recta en el diagrama y el cuerpo nunca deja la altura donde se soltó. Invierte el signo de A′ y el "
              "cuerpo sube, que es el defecto plantado del verificador; una página cuyo verificador acepte esa trayectoria no se publica."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "open", "en": "III · What this page does not say", "es": "III · Lo que esta página no dice", "short_en": "III · Not said", "short_es": "III · No dicho"},
        P(
            C("OPEN", [WILL],
              "Whether the rate of time is the more basic quantity, with the pull a derived appearance, or the reverse, is not a question "
              "the measurements decide: in general relativity the two descriptions are one description, and every experiment reviewed in "
              "the field's standard survey agrees with it.",
              "Si el ritmo del tiempo es la cantidad más básica, con la atracción como apariencia derivada, o al revés, no es una pregunta "
              "que las mediciones decidan: en la relatividad general las dos descripciones son una sola, y cada experimento revisado en el "
              "panorama estándar del campo concuerda con ella."),
            T(" That is why the statement in the hub is a question and not a claim, and why this page is labelled on the measured half only.",
              " Por eso la frase del punto de partida es una pregunta y no una afirmación, y por eso esta página solo lleva etiquetas en la mitad medida."),
        ),
        P(
            T("The page also does not say what sets the slope. In the metric above, g is a number we put in by hand. Where it comes from, "
              "and why every kind of matter responds to it in the same way, is the next page's question.",
              "La página tampoco dice qué fija la pendiente. En la métrica de arriba, g es un número que pusimos a mano. De dónde sale, y por "
              "qué cada tipo de materia responde a ella de la misma manera, es la pregunta de la página siguiente."),
        ),
        {"type": "change_box",
         "items": [
             ("A second collaboration resolving the redshift across a millimetre would raise the 2022 row from SINGLE RESULT to MEASURED.",
              "Una segunda colaboración que resuelva el corrimiento al rojo a lo largo de un milímetro subiría la fila de 2022 de RESULTADO ÚNICO a MEDIDO."),
             ("A measured clock-rate gradient that did not match gh/c² at any height would make the first MEASURED claim false and the page would be withdrawn, not relabelled.",
              "Un gradiente medido en el ritmo de los relojes que no coincidiera con gh/c² a alguna altura haría falsa la primera afirmación MEDIDA y la página se retiraría, no se reetiquetaría."),
             ("A ledger row passing its review date fails the build until a maintainer rereads the source and renews it.",
              "Una fila del libro de registro que pase su fecha de revisión hace fallar la construcción hasta que quien mantiene el sitio relea la fuente y la renueve."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · The metric", "Etapa 1 · La métrica",
         "ds² = −A(z)c²dt² + dz² with A(z) = 1 + 2gz/c². Only the time-time component varies; space is flat. This is the weak-field, slow-body limit of the Schwarzschild metric near a surface, and it is the only place the number g enters.",
         "ds² = −A(z)c²dt² + dz² con A(z) = 1 + 2gz/c². Solo la componente tiempo-tiempo varía; el espacio es plano. Es el límite de campo débil y cuerpo lento de la métrica de Schwarzschild cerca de una superficie, y es el único lugar donde entra el número g."),
        ("Stage 2 · The connection", "Etapa 2 · La conexión",
         "With x⁰ = ct the non-zero Christoffel symbols are Γᶻ₀₀ = A′/2 and Γ⁰₀ᶻ = Γ⁰ᶻ₀ = A′/(2A). Nothing else survives because nothing else depends on position.",
         "Con x⁰ = ct los símbolos de Christoffel distintos de cero son Γᶻ₀₀ = A′/2 y Γ⁰₀ᶻ = Γ⁰ᶻ₀ = A′/(2A). Nada más sobrevive porque nada más depende de la posición."),
        ("Stage 3 · The geodesic", "Etapa 3 · La geodésica",
         "d²z/dτ² = −(A′/2)(c dt/dτ)² and d²t/dτ² = −(A′/A)(dt/dτ)(dz/dτ). The verifier integrates both with RK4 from rest, dt/dτ = 1/√A(0), for one second of proper time in 20,000 steps.",
         "d²z/dτ² = −(A′/2)(c dt/dτ)² y d²t/dτ² = −(A′/A)(dt/dτ)(dz/dτ). El verificador integra ambas con RK4 desde el reposo, dt/dτ = 1/√A(0), durante un segundo de tiempo propio en 20,000 pasos."),
        ("Stage 4 · The number and the defect", "Etapa 4 · El número y el defecto",
         "From z(T) the verifier reads a = 2z/T² and requires |a + g|/g < 10⁻⁶. It then flattens A′ to zero and requires |a| < 10⁻¹², and flips the sign of A′ and requires the check to fail. If the flipped run passes, the verifier exits non-zero and the page does not build.",
         "Desde z(T) el verificador lee a = 2z/T² y exige |a + g|/g < 10⁻⁶. Luego aplana A′ a cero y exige |a| < 10⁻¹², e invierte el signo de A′ y exige que la prueba falle. Si la corrida invertida pasa, el verificador sale con código distinto de cero y la página no se construye."),
    ],
    "sidenotes": [
        ("SIDENOTE T.01-A · WHY THERE IS NO FORCE TERM", "NOTA T.01-A · POR QUÉ NO HAY TÉRMINO DE FUERZA",
         "The geodesic equation has no right-hand side. Everything that looks like gravity on this page is the connection term built from A′(z), which is the gradient in the rate of time. Remove the gradient and the equation is d²z/dτ² = 0.",
         "La ecuación geodésica no tiene lado derecho. Todo lo que parece gravedad en esta página es el término de conexión construido con A′(z), que es el gradiente en el ritmo del tiempo. Quita el gradiente y la ecuación es d²z/dτ² = 0."),
        ("SIDENOTE T.01-B · WHAT THE LABELS COST", "NOTA T.01-B · LO QUE CUESTAN LAS ETIQUETAS",
         "MEASURED needs two collaborations with peer-reviewed DOIs. The 2022 millimetre result is one collaboration, so it stays SINGLE RESULT however good it is. The lint cannot read physics; it can count rows, check dates and resolve DOIs, and a person decides the rest.",
         "MEDIDO exige dos colaboraciones con DOI revisados por pares. El resultado del milímetro de 2022 es una colaboración, así que sigue siendo RESULTADO ÚNICO por bueno que sea. El lint no lee física; cuenta filas, revisa fechas y resuelve DOI, y una persona decide lo demás."),
    ],
    "sources": [
        ("Pound, R. V., & Rebka, G. A. (1960). Apparent weight of photons. Physical Review Letters, 4(7), 337–341.", "10.1103/PhysRevLett.4.337"),
        ("Hafele, J. C., & Keating, R. E. (1972). Around-the-world atomic clocks: Predicted relativistic time gains. Science, 177(4044), 166–168.", "10.1126/science.177.4044.166"),
        ("Hafele, J. C., & Keating, R. E. (1972). Around-the-world atomic clocks: Observed relativistic time gains. Science, 177(4044), 168–170.", "10.1126/science.177.4044.168"),
        ("Vessot, R. F. C., et al. (1980). Test of relativistic gravitation with a space-borne hydrogen maser. Physical Review Letters, 45(26), 2081–2084.", "10.1103/PhysRevLett.45.2081"),
        ("Chou, C. W., Hume, D. B., Rosenband, T., & Wineland, D. J. (2010). Optical clocks and relativity. Science, 329(5999), 1630–1633.", "10.1126/science.1192720"),
        ("Bothwell, T., et al. (2022). Resolving the gravitational redshift across a millimetre-scale atomic sample. Nature, 602, 420–424.", "10.1038/s41586-021-04349-7"),
        ("Einstein, A. (1911). Über den Einfluß der Schwerkraft auf die Ausbreitung des Lichtes. Annalen der Physik, 340(10), 898–908.", "10.1002/andp.19113401005"),
        ("Will, C. M. (2014). The confrontation between general relativity and experiment. Living Reviews in Relativity, 17, 4.", "10.12942/lrr-2014-4"),
    ],
}
