# -*- coding: utf-8 -*-
"""Time & Gravity · T.02 — Everyone moves at one rate.

Instrument: a light clock whose tick stretches by the Lorentz factor as it moves, and the GPS daily clock
correction computed live from GM, the orbit radius and c. Knockout: let the satellite clock "opt out" (leave it
uncorrected) and the pseudorange error grows by about 11.5 km per day. Planted defect: a sign flip.
Verifier: skills/timegravity/t02/verify_t02_gps_one_rate.py (two calculation paths must agree; GUM-style budget).
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t02"
CODE = "T.02"

EIN05 = "T02-EIN1905"
IS = "T02-IS1938"
BOT = "T02-BOT2014"
ASHBY = "T02-ASHBY2003"
LHAASO = "T02-LHAASO2024"
HKP = "T01-HK1972P"
HKO = "T01-HK1972O"
GPA = "T01-GPA1980"
CHOU = "T01-CHOU2010"
PR = "T01-PR1960"
WILL = "T01-WILL2014"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "order_label_en": "Step 2 of 11",
    "order_label_es": "Paso 2 de 11",
    "kicker_en": "Time & Gravity · T.02 · The 'slide' made into a measured identity",
    "kicker_es": "Tiempo y Gravedad · T.02 · El 'deslizarse' convertido en una identidad medida",
    "title_en": "Everyone Moves at One Rate",
    "title_es": "Todos Avanzamos a un Mismo Ritmo",
    "standfirst_en": (
        "A clock that moves ticks slower, by exactly the Lorentz factor, and no clock can opt out: the four-velocity of "
        "every body has the same norm, c. The GPS constellation is that identity run as infrastructure. This page recomputes "
        "the satellite clock correction from three constants, two different ways, and shows what one uncorrected day would cost."
    ),
    "standfirst_es": (
        "Un reloj que se mueve avanza más lento, exactamente por el factor de Lorentz, y ningún reloj puede quedarse fuera: la "
        "cuatrivelocidad de todo cuerpo tiene la misma norma, c. La constelación GPS es esa identidad convertida en "
        "infraestructura. Esta página recalcula la corrección del reloj satelital a partir de tres constantes, de dos maneras "
        "distintas, y muestra lo que costaría un día sin corregir."
    ),
    "seo": (
        "Everyone Moves at One Rate: Clocks, GPS and c",
        "How moving clocks tick slower by the Lorentz factor, measured from 1938 to 2014, and how the GPS clock correction follows from GM, the orbit radius and c.",
        "Todos Avanzamos a un Mismo Ritmo: Relojes, GPS y c",
        "Cómo los relojes en movimiento avanzan más lento por el factor de Lorentz, medido de 1938 a 2014, y cómo la corrección del GPS sale de GM, el radio orbital y c.",
    ),
    "reading_time_en": "13 min read",
    "reading_time_es": "13 min de lectura",
    "central_number_en": "GPS satellite clock: +45.7 µs/day gravitational, −7.2 µs/day velocity, +38.4 µs/day net, recomputed two ways within 0.3 µs/day",
    "central_number_es": "Reloj satelital GPS: +45.7 µs/día gravitatorio, −7.2 µs/día por velocidad, +38.4 µs/día neto, recalculado de dos maneras dentro de 0.3 µs/día",
    "verifier": "skills/timegravity/t02/verify_t02_gps_one_rate.py",
    "generator": "skills/timegravity/t02/make_t02.py",
    "skill": "skills/timegravity/t02/SKILL.md",
    "skill_filename": "timegravity-t02-gps-one-rate.SKILL.md",
    "open_question_en": "Why can nothing opt out?",
    "open_question_es": "¿Por qué nada puede quedarse fuera?",
    "ledger_ids": [IS, HKP, HKO, CHOU, BOT, EIN05, ASHBY, GPA, PR, LHAASO, WILL],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any measurement or derivation cited on this "
        "page. The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer against "
        "the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna medición o derivación citada "
        "en esta página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien mantiene el "
        "sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "gps",
        "title_en": "Instrument · A light clock in motion, and the GPS correction from three constants",
        "title_es": "Instrumento · Un reloj de luz en movimiento, y la corrección GPS a partir de tres constantes",
        "how_en": (
            "Left: a light clock, a photon bouncing between two mirrors. At rest it ticks straight up and down. In motion the "
            "photon's path is a longer zigzag at the same speed c, so the tick takes γ = 1/√(1 − v²/c²) times longer; the speed "
            "slider sets v/c. Right: the GPS clock budget computed live from GM, the orbit radius and c: the weaker potential makes "
            "the satellite clock run fast, its speed makes it run slow, and the net is what the ground must correct. The orbit "
            "slider moves the satellite; the knockout leaves its clock uncorrected and the bar shows the pseudorange error after one "
            "day; the sign flip corrects it the wrong way. Keyboard: Tab to a control, arrows to change it. With reduced motion on, "
            "the photon is drawn as a path instead of animated."
        ),
        "how_es": (
            "Izquierda: un reloj de luz, un fotón que rebota entre dos espejos. En reposo marca recto arriba y abajo. En movimiento la "
            "trayectoria del fotón es un zigzag más largo a la misma rapidez c, así que el tic tarda γ = 1/√(1 − v²/c²) veces más; el "
            "deslizador de rapidez fija v/c. Derecha: el presupuesto del reloj GPS calculado en vivo a partir de GM, el radio orbital y "
            "c: el potencial más débil hace que el reloj satelital adelante, su rapidez hace que atrase, y el neto es lo que el suelo "
            "debe corregir. El deslizador de órbita mueve el satélite; el apagado deja el reloj sin corregir y la barra muestra el error "
            "de pseudodistancia tras un día; el cambio de signo lo corrige al revés. Teclado: Tab hasta un control y flechas para "
            "cambiarlo. Con movimiento reducido, el fotón se dibuja como trayectoria en lugar de animarse."
        ),
    },
    "predict": {
        "q_en": "Before you press the knockout: if the satellite clock is left uncorrected for one day, how far off will a position fix drift?",
        "q_es": "Antes de pulsar el apagado: si el reloj satelital se deja sin corregir un día, ¿cuánto se desviará una posición?",
        "options": [("About 11 metres", "Unos 11 metros"), ("About 11 kilometres", "Unos 11 kilómetros"), ("Nothing: the receiver cancels it", "Nada: el receptor lo cancela")],
        "answer": 1,
        "reveal_en": "The instrument shows about 11.5 km per day: 38.4 µs of clock offset multiplied by c.",
        "reveal_es": "El instrumento muestra unos 11.5 km por día: 38.4 µs de desfase de reloj multiplicados por c.",
    },
    "sections": [
        {"type": "h2", "id": "measured", "en": "I · Moving clocks tick slower, and it has been measured for ninety years", "es": "I · Los relojes en movimiento avanzan más lento, y se ha medido durante noventa años", "short_en": "I · Measured", "short_es": "I · Medido"},
        P(
            C("MEASURED", [IS, HKO, CHOU, BOT],
              "A clock moving relative to an observer ticks slower by the Lorentz factor γ = 1/√(1 − v²/c²); this has been measured "
              "from the second-order Doppler shift of hydrogen canal rays in 1938, through caesium clocks on airliners in 1971 and "
              "lithium ions circulating at a third of the speed of light in 2014, down to an aluminium-ion clock moving at a few metres per second in 2010.",
              "Un reloj que se mueve respecto a un observador avanza más lento por el factor de Lorentz γ = 1/√(1 − v²/c²); se ha "
              "medido desde el corrimiento Doppler de segundo orden de rayos canales de hidrógeno en 1938, pasando por relojes de cesio "
              "en aviones de línea en 1971 e iones de litio circulando a un tercio de la rapidez de la luz en 2014, hasta un reloj de ion "
              "de aluminio moviéndose a unos metros por segundo en 2010."),
            T(" Four collaborations, four technologies, one factor. That is what lets the first claim on this page say MEASURED.",
              " Cuatro colaboraciones, cuatro tecnologías, un solo factor. Eso es lo que permite que la primera afirmación de esta página diga MEDIDO."),
        ),
        P(
            C("MEASURED", [HKP, HKO, CHOU],
              "Hafele and Keating separated the two effects in their prediction: for the eastward flight the aircraft's speed cost "
              "the clocks −184 ± 18 ns while the altitude gained them 144 ± 14 ns, net −40 ± 23 ns; westward the speed term was "
              "+96 ± 10 ns and the altitude term 179 ± 18 ns, net 275 ± 21 ns; the observed totals were −59 ± 10 ns and 273 ± 7 ns.",
              "Hafele y Keating separaron los dos efectos en su predicción: en el vuelo hacia el este la rapidez del avión costó a los "
              "relojes −184 ± 18 ns mientras la altitud les dio 144 ± 14 ns, neto −40 ± 23 ns; hacia el oeste el término de rapidez fue "
              "+96 ± 10 ns y el de altitud 179 ± 18 ns, neto 275 ± 21 ns; los totales observados fueron −59 ± 10 ns y 273 ± 7 ns."),
            T(" The same two terms, speed and potential, are the whole GPS budget below; the aircraft experiment is the GPS experiment "
              "at a lower altitude and a slower speed.",
              " Los mismos dos términos, rapidez y potencial, son todo el presupuesto GPS de abajo; el experimento del avión es el "
              "experimento GPS a menor altitud y menor rapidez."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("Picture a clock as a ball bouncing between the floor and the ceiling of a train car. When the train stands still, "
                 "the ball goes straight up and down. When the train moves, someone on the platform sees the ball trace a zigzag: it "
                 "covers more distance between bounces. If the ball always travels at the same speed, each bounce must take longer. "
                 "Light is that ball, and its speed is the same for everyone. So a moving clock ticks slower, and the amount is fixed by geometry.",
                 "Imagina un reloj como una pelota que rebota entre el piso y el techo de un vagón. Cuando el tren está quieto, la pelota "
                 "sube y baja en línea recta. Cuando el tren se mueve, alguien en el andén ve que la pelota traza un zigzag: recorre más "
                 "distancia entre rebotes. Si la pelota siempre viaja a la misma rapidez, cada rebote debe tardar más. La luz es esa "
                 "pelota, y su rapidez es la misma para todos. Así que un reloj en movimiento avanza más lento, y la cantidad la fija la geometría.")),
             P(T("That is also why nothing can opt out. Not because of a rule imposed on clocks, but because every clock is made of "
                 "things that move at or below the speed of light, and the geometry applies to all of them equally.",
                 "Por eso tampoco nada puede quedarse fuera. No por una regla impuesta a los relojes, sino porque todo reloj está hecho "
                 "de cosas que se mueven a la rapidez de la luz o por debajo, y la geometría se aplica a todas por igual.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: everyone walks at the same total speed through a city where streets run 'through space' and "
                 "avenues run 'through time'. Standing still, all your speed goes along the avenue, which is why your watch runs fastest "
                 "when you do not move. Walk along a street and some of that fixed total is spent on space, so less is left for time: "
                 "your watch slows. You cannot walk faster than the total, and you cannot refuse to spend it.",
                 "Analogía cotidiana: todos caminan a la misma rapidez total por una ciudad donde las calles van 'por el espacio' y las "
                 "avenidas van 'por el tiempo'. Quieto, toda tu rapidez va por la avenida, por eso tu reloj corre más rápido cuando no te "
                 "mueves. Camina por una calle y parte de ese total fijo se gasta en espacio, así que queda menos para el tiempo: tu "
                 "reloj se frena. No puedes caminar más rápido que el total, y no puedes negarte a gastarlo.")),
             P(T("How the controls work in plain words: the speed slider is how fast the light clock walks along the street; the γ "
                 "readout is how much slower its ticks become. The orbit slider lifts or lowers the satellite; higher means a weaker "
                 "potential (clock runs faster) and a slower orbit (clock runs less slow). The knockout leaves the satellite clock "
                 "uncorrected, and the bar shows the ranging error that piles up in a day. The sign flip is the mistake a careless "
                 "engineer might make: correcting in the wrong direction, which doubles the error.",
                 "Cómo funcionan los controles en palabras sencillas: el deslizador de rapidez es qué tan rápido camina el reloj de luz por "
                 "la calle; la lectura γ es cuánto más lentos se vuelven sus tics. El deslizador de órbita sube o baja el satélite; más "
                 "alto significa potencial más débil (el reloj adelanta) y órbita más lenta (el reloj atrasa menos). El apagado deja el "
                 "reloj satelital sin corregir, y la barra muestra el error de distancia que se acumula en un día. El cambio de signo es "
                 "el error de un ingeniero descuidado: corregir en la dirección equivocada, lo que duplica el error.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "derived", "en": "II · One rate for everyone, and the GPS budget two ways", "es": "II · Un mismo ritmo para todos, y el presupuesto GPS de dos maneras", "short_en": "II · Derived", "short_es": "II · Derivado"},
        P(
            C("DERIVED", [EIN05, HKO],
              "In special relativity the four-velocity of any body has the fixed norm c: c²(dt/dτ)² − (dx/dτ)² = c², so the rate of "
              "proper time against coordinate time is dτ/dt = √(1 − v²/c²), the inverse Lorentz factor; the statement 'everyone moves "
              "through spacetime at one rate' is this identity restated, and it is why no clock can opt out of time dilation.",
              "En relatividad especial la cuatrivelocidad de cualquier cuerpo tiene la norma fija c: c²(dt/dτ)² − (dx/dτ)² = c², así que "
              "el ritmo del tiempo propio respecto al tiempo coordenado es dτ/dt = √(1 − v²/c²), el inverso del factor de Lorentz; la "
              "frase 'todos avanzamos por el espaciotiempo a un mismo ritmo' es esta identidad dicha de otro modo, y es la razón por la "
              "que ningún reloj puede quedarse fuera de la dilatación del tiempo.",
              parent=HKO),
            T(" This is labelled DERIVED: it follows from the 1905 kinematics by algebra, and its parent MEASURED row is the clock "
              "transport experiment that measured the factor directly.",
              " Lleva la etiqueta DERIVADO: se sigue de la cinemática de 1905 por álgebra, y su fila madre MEDIDA es el experimento de "
              "transporte de relojes que midió el factor directamente."),
        ),
        {"type": "equation", "text": "Δf/f ≈ (GM/c²)(1/R − 1/a)  −  GM/(2 a c²)      →   +45.7 µs/day − 7.2 µs/day = +38.4 µs/day"},
        P(
            C("DERIVED", [ASHBY, GPA, HKO],
              "For a GPS satellite at a = 26,562 km the weaker potential makes its clock run fast by about 45.7 µs per day and its orbital "
              "speed makes it run slow by about 7.2 µs per day, net about 38.4 µs per day fast relative to a clock on the ground; the "
              "verifier beside this page recomputes those three numbers from GM, a and c and requires them within 0.6, 0.2 and 0.7 µs per day of the reference values.",
              "Para un satélite GPS en a = 26,562 km el potencial más débil hace que su reloj adelante unos 45.7 µs por día y su rapidez "
              "orbital hace que atrase unos 7.2 µs por día, neto unos 38.4 µs por día adelantado respecto a un reloj en tierra; el "
              "verificador junto a esta página recalcula esos tres números a partir de GM, a y c y los exige dentro de 0.6, 0.2 y 0.7 µs por día de los valores de referencia.",
              parent=GPA),
            T(" The parent MEASURED row is Gravity Probe A, which measured the potential term for a clock on a rocket; the derivation row is Ashby's review.",
              " La fila madre MEDIDA es Gravity Probe A, que midió el término de potencial para un reloj en un cohete; la fila de derivación es la revisión de Ashby."),
        ),
        P(
            C("DERIVED", [ASHBY, GPA],
              "Double entry: the same net gain computed a second way, from the Schwarzschild rate ratio dτ/dt of each clock, "
              "√(1 − 3GM/ac²) for the circular orbit against √(1 − 2GM/Rc² − Ω²R²/c²) for a clock on the rotating equator, agrees with the "
              "first-order sum within 0.3 µs per day; the difference is the ground clock's own rotation, which the first-order sum leaves out.",
              "Doble entrada: la misma ganancia neta calculada de una segunda manera, a partir de la razón de ritmos de Schwarzschild dτ/dt de "
              "cada reloj, √(1 − 3GM/ac²) para la órbita circular frente a √(1 − 2GM/Rc² − Ω²R²/c²) para un reloj en el ecuador en rotación, "
              "coincide con la suma de primer orden dentro de 0.3 µs por día; la diferencia es la rotación propia del reloj en tierra, que la suma de primer orden omite.",
              parent=GPA),
            T(" Two paths to one number is an accounting habit, not a physics one, and it is the cheapest guard against a formula that is plausible and wrong.",
              " Dos caminos hacia un número es un hábito contable, no de física, y es la guardia más barata contra una fórmula plausible y equivocada."),
        ),
        {"type": "budget_table"},
        P(
            C("DERIVED", [ASHBY, GPA],
              "Left uncorrected, a 38.4 µs per day clock offset multiplied by c is a pseudorange error that grows by about 11.5 km per day, "
              "which is why the satellite clocks are set before launch to run slow by the net amount, so that from the ground they appear to tick at their nominal 10.23 MHz.",
              "Sin corregir, un desfase de reloj de 38.4 µs por día multiplicado por c es un error de pseudodistancia que crece unos 11.5 km por "
              "día, y por eso los relojes satelitales se ajustan antes del lanzamiento para atrasar la cantidad neta, de modo que desde tierra "
              "parecen marcar sus 10.23 MHz nominales.",
              parent=GPA),
            T(" The knockout in the instrument is exactly that uncorrected day. A receiver would in practice fail in other ways first; the number is the size of the term, not a prediction of what a phone would show.",
              " El apagado del instrumento es exactamente ese día sin corregir. En la práctica un receptor fallaría antes de otras maneras; el número es el tamaño del término, no una predicción de lo que mostraría un teléfono."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "bound", "en": "III · A bound, and what this page does not say", "es": "III · Una cota, y lo que esta página no dice", "short_en": "III · Bound", "short_es": "III · Cota"},
        P(
            C("BOUND", [LHAASO],
              "If the one rate had a tiny energy dependence, the highest-energy photons from a gamma-ray burst would arrive out of step; "
              "LHAASO's observation of GRB 221009A found none and set the scale of any linear Lorentz-invariance violation above 10 Planck "
              "energies and of any quadratic one above 6 × 10⁻⁸ Planck energies, at 95% confidence.",
              "Si el ritmo único tuviera una pequeña dependencia de la energía, los fotones de mayor energía de un estallido de rayos gamma "
              "llegarían desfasados; la observación de LHAASO del GRB 221009A no encontró ninguno y fijó la escala de cualquier violación "
              "lineal de la invariancia de Lorentz por encima de 10 energías de Planck y de cualquier violación cuadrática por encima de "
              "6 × 10⁻⁸ energías de Planck, al 95% de confianza."),
            T(" BOUND means a measurement of what is excluded, not of what exists; the label is deliberately separate from MEASURED.",
              " COTA significa una medición de lo que queda excluido, no de lo que existe; la etiqueta es deliberadamente distinta de MEDIDO."),
        ),
        P(
            C("OPEN", [WILL],
              "Why there is a universal speed and a single rate is not something the measurements answer; they fix the structure, in "
              "every test the field's standard survey lists, and leave the reason as a question.",
              "Por qué hay una rapidez universal y un ritmo único no es algo que las mediciones respondan; fijan la estructura, en cada "
              "prueba que lista el panorama estándar del campo, y dejan la razón como pregunta."),
            T(" The speed is kinematic. What bends the one rate between heights, and why the bend is the same for every kind of matter, is the next question, and the next page.",
              " La rapidez es cinemática. Qué dobla el ritmo único entre alturas, y por qué el doblez es el mismo para toda clase de materia, es la siguiente pregunta, y la siguiente página."),
        ),
        {"type": "change_box",
         "items": [
             ("A measured time-dilation factor that differed from 1/√(1 − v²/c²) at any speed would make the first MEASURED claim false and the page would be withdrawn, not relabelled.",
              "Un factor de dilatación del tiempo medido que difiriera de 1/√(1 − v²/c²) a cualquier rapidez haría falsa la primera afirmación MEDIDA y la página se retiraría, no se reetiquetaría."),
             ("An energy-dependent photon delay confirmed by a second observatory would turn the BOUND row into a measured violation and reopen every DERIVED claim here.",
              "Un retraso de fotones dependiente de la energía confirmado por un segundo observatorio convertiría la fila COTA en una violación medida y reabriría cada afirmación DERIVADA de aquí."),
             ("If the two calculation paths of the GPS number ever disagree by more than 0.3 µs per day after a constants update, the verifier fails and the page does not build until the derivation is rechecked.",
              "Si los dos caminos de cálculo del número GPS llegaran a diferir por más de 0.3 µs por día tras actualizar las constantes, el verificador falla y la página no se construye hasta revisar la derivación."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · The identity", "Etapa 1 · La identidad",
         "u·u = −c² for every timelike worldline. Written out, c²(dt/dτ)² − v²(dt/dτ)² = c², so dτ/dt = √(1 − v²/c²). The light clock is this identity drawn: a longer zigzag at the same speed c.",
         "u·u = −c² para toda línea de mundo temporal. Desarrollado, c²(dt/dτ)² − v²(dt/dτ)² = c², así que dτ/dt = √(1 − v²/c²). El reloj de luz es esta identidad dibujada: un zigzag más largo a la misma rapidez c."),
        ("Stage 2 · Two first-order terms", "Etapa 2 · Dos términos de primer orden",
         "Gravitational: Δf/f = (GM/c²)(1/R − 1/a), positive (satellite fast). Velocity: −v²/2c² with v² = GM/a, negative (satellite slow). The verifier evaluates both with GM = 3.986004418e14 m³/s², a = 26,561.75 km, R = 6,378.137 km.",
         "Gravitatorio: Δf/f = (GM/c²)(1/R − 1/a), positivo (satélite adelanta). De velocidad: −v²/2c² con v² = GM/a, negativo (satélite atrasa). El verificador evalúa ambos con GM = 3.986004418e14 m³/s², a = 26,561.75 km, R = 6,378.137 km."),
        ("Stage 3 · Double entry", "Etapa 3 · Doble entrada",
         "The Schwarzschild rate ratio: dτ/dt = √(1 − 3GM/ac²) in circular orbit, √(1 − 2GM/Rc² − Ω²R²/c²) on the rotating ground. Their ratio minus one, per day, must match Stage 2 within 0.3 µs; the residual is the ground clock's rotation.",
         "La razón de ritmos de Schwarzschild: dτ/dt = √(1 − 3GM/ac²) en órbita circular, √(1 − 2GM/Rc² − Ω²R²/c²) en el suelo en rotación. Su cociente menos uno, por día, debe coincidir con la Etapa 2 dentro de 0.3 µs; el residuo es la rotación del reloj en tierra."),
        ("Stage 4 · Budget and defect", "Etapa 4 · Presupuesto y defecto",
         "A GUM-style budget propagates the stated uncertainties of GM, a and the ground radius to the net term and combines them in quadrature; c is exact. The planted defect flips the sign of the gravitational term; the check must reject it or the page does not build.",
         "Un presupuesto al estilo GUM propaga las incertidumbres declaradas de GM, a y el radio en tierra al término neto y las combina en cuadratura; c es exacta. El defecto plantado invierte el signo del término gravitatorio; la prueba debe rechazarlo o la página no se construye."),
    ],
    "sidenotes": [
        ("SIDENOTE T.02-A · WHY TWO CALCULATION PATHS", "NOTA T.02-A · POR QUÉ DOS CAMINOS DE CÁLCULO",
         "Accountants reconcile two ledgers because one plausible wrong entry is easy to miss. The first-order sum and the Schwarzschild ratio share no code; when they agree within 0.3 µs per day, a sign slip or a dropped factor of 2 cannot be hiding in either.",
         "Los contadores concilian dos libros porque una entrada plausible y equivocada es fácil de pasar por alto. La suma de primer orden y la razón de Schwarzschild no comparten código; cuando coinciden dentro de 0.3 µs por día, un desliz de signo o un factor de 2 perdido no puede esconderse en ninguna."),
        ("SIDENOTE T.02-B · WHAT THE BUDGET LEAVES OUT", "NOTA T.02-B · LO QUE EL PRESUPUESTO OMITE",
         "Orbital eccentricity adds a periodic term with zero mean that receivers correct separately, and the real ground reference is the geoid, not the equator. Both are why the acceptance window is ±0.7 µs per day and not ±0.1.",
         "La excentricidad orbital agrega un término periódico de media cero que los receptores corrigen por separado, y la referencia real en tierra es el geoide, no el ecuador. Ambas cosas son la razón de que la ventana de aceptación sea ±0.7 µs por día y no ±0.1."),
    ],
    "sources": [
        ("Ives, H. E., & Stilwell, G. R. (1938). An experimental study of the rate of a moving atomic clock. Journal of the Optical Society of America, 28(7), 215–226.", "10.1364/JOSA.28.000215"),
        ("Hafele, J. C., & Keating, R. E. (1972). Around-the-world atomic clocks: Predicted relativistic time gains. Science, 177(4044), 166–168.", "10.1126/science.177.4044.166"),
        ("Hafele, J. C., & Keating, R. E. (1972). Around-the-world atomic clocks: Observed relativistic time gains. Science, 177(4044), 168–170.", "10.1126/science.177.4044.168"),
        ("Chou, C. W., Hume, D. B., Rosenband, T., & Wineland, D. J. (2010). Optical clocks and relativity. Science, 329(5999), 1630–1633.", "10.1126/science.1192720"),
        ("Botermann, B., et al. (2014). Test of time dilation using stored Li+ ions as clocks at relativistic speed. Physical Review Letters, 113(12), 120405.", "10.1103/PhysRevLett.113.120405"),
        ("Einstein, A. (1905). Zur Elektrodynamik bewegter Körper. Annalen der Physik, 322(10), 891–921.", "10.1002/andp.19053221004"),
        ("Ashby, N. (2003). Relativity in the Global Positioning System. Living Reviews in Relativity, 6, 1.", "10.12942/lrr-2003-1"),
        ("Vessot, R. F. C., et al. (1980). Test of relativistic gravitation with a space-borne hydrogen maser. Physical Review Letters, 45(26), 2081–2084.", "10.1103/PhysRevLett.45.2081"),
        ("Pound, R. V., & Rebka, G. A. (1960). Apparent weight of photons. Physical Review Letters, 4(7), 337–341.", "10.1103/PhysRevLett.4.337"),
        ("LHAASO Collaboration (Cao, Z., et al.) (2024). Stringent tests of Lorentz invariance violation from LHAASO observations of GRB 221009A. Physical Review Letters, 133(7), 071501.", "10.1103/PhysRevLett.133.071501"),
        ("Will, C. M. (2014). The confrontation between general relativity and experiment. Living Reviews in Relativity, 17, 4.", "10.12942/lrr-2014-4"),
    ],
}
