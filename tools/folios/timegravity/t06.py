# -*- coding: utf-8 -*-
"""Time & Gravity · T.06 — Does gravity collapse the wave?

The Diósi–Penrose proposal (collapse time τ = ħ/E_G) and the two experiments that bound it through the
spontaneous radiation it predicts: Gran Sasso (2021) and XENONnT (2026). Scoped to the non-dissipative,
parameter-free model; CSL is not a gravity model and stays out. Knockout: switch gravity off and no collapse.
Planted defect: the bound drawn on the wrong side. Page label BOUND.
Verifier: skills/timegravity/t06/verify_t06_collapse_bound.py.
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t06"
CODE = "T.06"

DIOSI = "T06-DIOSI1987"
PENROSE = "T06-PENROSE1996"
DONADI = "T06-DONADI2021"
XENON = "T06-XENONNT2026"
FEIN = "T06-FEIN2019"
HELOU = "T06-HELOU2017"
HAMEROFF = "T06-HAMEROFF2014"
OPPENHEIM = "T06-OPPENHEIM2023"
PICCIONE = "T06-PICCIONE2025"
TILLOY = "T05-TILLOY2016"
TRILLO = "T05-TRILLO2025"
LEE = "T05-LEE2020"
LEE21 = "T05-LEE2021"
GERACI = "T06-GERACI2008"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "date": "2026-11-09",
    "order_label_en": "Step 7 of 13",
    "order_label_es": "Paso 7 de 13",
    "kicker_en": "Time & Gravity · T.06 · A proposal and the two experiments that bound it",
    "kicker_es": "Tiempo y Gravedad · T.06 · Una propuesta y los dos experimentos que la acotan",
    "title_en": "Does Gravity Collapse the Wave?",
    "title_es": "¿La Gravedad Colapsa la Onda?",
    "standfirst_en": (
        "One proposal says gravity itself ends a superposition: a mass in two places pays an energy E_G for the difference "
        "between its two gravitational fields, and the superposition decays in about ħ/E_G. The same proposal predicts that "
        "charged matter should emit a faint spontaneous radiation with no external cause. Two underground detectors looked for that glow and did not see it. "
        "This page computes the model, recomputes the bound from the raw counts, and draws the line on the side the data put it."
    ),
    "standfirst_es": (
        "Una propuesta dice que la gravedad misma termina una superposición: una masa en dos lugares paga una energía E_G por la "
        "diferencia entre sus dos campos gravitatorios, y la superposición decae en unos ħ/E_G. La misma propuesta predice que la "
        "materia cargada debería emitir una radiación espontánea débil sin causa externa. Dos detectores subterráneos buscaron ese brillo y no lo vieron. "
        "Esta página calcula el modelo, recalcula la cota desde los conteos crudos, y dibuja la línea del lado en que los datos la pusieron."
    ),
    "seo": (
        "Does Gravity Collapse the Wave? The Bound",
        "The Diosi-Penrose collapse proposal, its predicted spontaneous radiation, and the Gran Sasso and XENONnT bounds recomputed from the published counts.",
        "¿La Gravedad Colapsa la Onda? La Cota",
        "La propuesta de colapso de Diosi y Penrose, la radiación espontánea que predice, y las cotas de Gran Sasso y XENONnT recalculadas de los conteos publicados.",
    ),
    "reading_time_en": "13 min read",
    "reading_time_es": "13 min de lectura",
    "central_number_en": "From 576 measured against 506 background counts in 62 days: R0 > 0.54 × 10⁻¹⁰ m at 95 %, recomputed within 2 % of the published bound; the parameter-free R0 = 0.05 × 10⁻¹⁰ m would have given about 1.4 × 10⁵ photons",
    "central_number_es": "De 576 conteos medidos frente a 506 de fondo en 62 días: R0 > 0.54 × 10⁻¹⁰ m al 95 %, recalculado dentro del 2 % de la cota publicada; el R0 = 0.05 × 10⁻¹⁰ m sin parámetros habría dado unos 1.4 × 10⁵ fotones",
    "verifier": "skills/timegravity/t06/verify_t06_collapse_bound.py",
    "generator": "skills/timegravity/t06/make_t06.py",
    "skill": "skills/timegravity/t06/SKILL.md",
    "skill_filename": "timegravity-t06-collapse-bound.SKILL.md",
    "open_question_en": "If gravity neither collapses nor is shown to entangle, what is a superposition of slopes?",
    "open_question_es": "Si la gravedad ni colapsa ni se muestra que entrelaza, ¿qué es una superposición de pendientes?",
    "ledger_ids": [DIOSI, PENROSE, DONADI, XENON, FEIN, HELOU, HAMEROFF, OPPENHEIM, PICCIONE, TILLOY, TRILLO, LEE, LEE21],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any proposal, measurement or bound cited on this page. "
        "The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna propuesta, medición o cota citada en esta "
        "página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien mantiene el sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "dp",
        "title_en": "Instrument · The model's collapse time, and where the data draw the line",
        "title_es": "Instrumento · El tiempo de colapso del modelo, y dónde trazan la línea los datos",
        "how_en": (
            "Left: the Diósi–Penrose collapse time τ = ħ/E_G for a uniform sphere of mass M and radius R displaced by d, with E_G the "
            "gravitational self-energy of the difference between the two mass distributions; sliders set log₁₀ M, log₁₀ R and d/R, and the "
            "curve shows τ against mass at the chosen R and d. Right: the exclusion line for R0, the size of the nuclear mass density the "
            "model's radiation depends on: the Gran Sasso bound (95 %), the XENONnT bound (90 %), and the parameter-free value the model "
            "would prefer, drawn on the excluded side. The knockout switches gravity off (G → 0): E_G vanishes, τ is infinite, the model "
            "predicts nothing. The planted defect draws the bound on the wrong side, as if small R0 were allowed; the verifier rejects that "
            "orientation. Keyboard: Tab and arrows. With reduced motion on, nothing animates."
        ),
        "how_es": (
            "Izquierda: el tiempo de colapso de Diósi y Penrose τ = ħ/E_G para una esfera uniforme de masa M y radio R desplazada d, con E_G la "
            "autoenergía gravitatoria de la diferencia entre las dos distribuciones de masa; los deslizadores fijan log₁₀ M, log₁₀ R y d/R, y la "
            "curva muestra τ frente a la masa para la R y la d elegidas. Derecha: la línea de exclusión para R0, el tamaño de la densidad de masa "
            "nuclear del que depende la radiación del modelo: la cota de Gran Sasso (95 %), la cota de XENONnT (90 %) y el valor sin parámetros "
            "que el modelo preferiría, dibujado del lado excluido. El apagado quita la gravedad (G → 0): E_G se anula, τ es infinito, el modelo "
            "no predice nada. El defecto plantado dibuja la cota del lado equivocado, como si los R0 pequeños estuvieran permitidos; el "
            "verificador rechaza esa orientación. Teclado: Tab y flechas. Con movimiento reducido, nada se anima."
        ),
    },
    "predict": {
        "q_en": "Before you look at the right-hand panel: with the model's own parameter-free value R0 = 0.05 × 10⁻¹⁰ m, how many spontaneous photons should Gran Sasso have counted above background in 62 days?",
        "q_es": "Antes de mirar el panel derecho: con el valor sin parámetros del propio modelo, R0 = 0.05 × 10⁻¹⁰ m, ¿cuántos fotones espontáneos debió contar Gran Sasso por encima del fondo en 62 días?",
        "options": [("About 70", "Unos 70"), ("About a thousand", "Como mil"), ("About 140,000", "Unos 140,000")],
        "answer": 2,
        "reveal_en": "About 1.4 × 10⁵. The detector saw 576 counts against 506 expected, an excess of 70 ± 24. That is why the parameter-free model is excluded, by three orders of magnitude.",
        "reveal_es": "Unos 1.4 × 10⁵. El detector vio 576 conteos frente a 506 esperados, un exceso de 70 ± 24. Por eso el modelo sin parámetros queda excluido, por tres órdenes de magnitud.",
    },
    "sections": [
        {"type": "h2", "id": "proposal", "en": "I · The proposal", "es": "I · La propuesta", "short_en": "I · Proposal", "short_es": "I · Propuesta"},
        P(
            C("PROPOSED", [DIOSI, PENROSE],
              "Diósi in 1987 and Penrose in 1996 proposed that a quantum superposition of two mass distributions is unstable, with a "
              "lifetime of order ħ/E_G, where E_G is the gravitational self-energy of the difference between the two distributions; for a "
              "uniform sphere of mass M and radius R displaced far from itself, E_G = (6/5) G M²/R.",
              "Diósi en 1987 y Penrose en 1996 propusieron que una superposición cuántica de dos distribuciones de masa es inestable, con una "
              "vida media del orden de ħ/E_G, donde E_G es la autoenergía gravitatoria de la diferencia entre las dos distribuciones; para una "
              "esfera uniforme de masa M y radio R desplazada lejos de sí misma, E_G = (6/5) G M²/R."),
            T(" This is a proposal, and the label says so. The instrument evaluates E_G in closed form and by direct numerical integration, "
              "which agree to better than one part in a thousand, so that whatever the model's fate, its arithmetic on this page is right.",
              " Es una propuesta, y la etiqueta lo dice. El instrumento evalúa E_G en forma cerrada y por integración numérica directa, que "
              "coinciden a mejor que una parte en mil, para que, sea cual sea la suerte del modelo, su aritmética en esta página esté bien."),
        ),
        P(
            T("For a sphere of a hundredth of a nanogram and a micrometre across, displaced by its own diameter, the model's collapse time is "
              "a few hundredths of a second. For a molecule of 25,000 atomic mass units treated as a sphere a nanometre across it is tens of "
              "thousands of years. Matter-wave interferometry, which is where superpositions are built, is nowhere near the first number yet; "
              "the test came from somewhere else.",
              "Para una esfera de una centésima de nanogramo y un micrómetro de ancho, desplazada su propio diámetro, el tiempo de colapso del "
              "modelo es de unas centésimas de segundo. Para una molécula de 25,000 unidades de masa atómica tratada como esfera de un nanómetro "
              "es de decenas de miles de años. La interferometría de ondas de materia, donde se construyen las superposiciones, todavía no está "
              "cerca del primer número; la prueba llegó de otro lado."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("If a thing is in two places at once, its gravity is too. The proposal says nature dislikes that and resolves it, faster the "
                 "heavier the thing. Nobody has caught a superposition collapsing that way. But the same proposal has a side effect: the jitter "
                 "that keeps collapsing a particle's position would make charged particles radiate, always, a little. That is a prediction you "
                 "can test in a quiet room with a detector and patience.",
                 "Si algo está en dos lugares a la vez, su gravedad también. La propuesta dice que a la naturaleza no le gusta eso y lo resuelve, "
                 "más rápido cuanto más pesada la cosa. Nadie ha atrapado una superposición colapsando así. Pero la misma propuesta tiene un "
                 "efecto secundario: el temblor que colapsa la posición de una partícula haría que las partículas cargadas radiaran, siempre, un "
                 "poco. Esa es una predicción que puedes probar en un cuarto silencioso con un detector y paciencia.")),
             P(T("Two groups did, deep underground where cosmic rays cannot reach. They counted the photons they expected from ordinary "
                 "radioactivity, and almost nothing more. The model in its simplest form would have produced thousands of times that. So that "
                 "form is out, and the page says what is left.",
                 "Dos grupos lo hicieron, bajo tierra, donde los rayos cósmicos no llegan. Contaron los fotones que esperaban de la radiactividad "
                 "ordinaria, y casi nada más. El modelo en su forma más simple habría producido miles de veces eso. Así que esa forma queda fuera, "
                 "y la página dice qué queda.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: a suspect claims to be in two cities at once. You cannot catch the moment he picks one. But a person who "
                 "is constantly being yanked between two cities would leave a trail: receipts, footprints, a hum. You search the quietest room "
                 "in the country for the hum. You find the usual noise and nothing else. The story that he is being yanked, in its plainest "
                 "version, is no longer tenable.",
                 "Analogía cotidiana: un sospechoso dice estar en dos ciudades a la vez. No puedes atrapar el momento en que elige una. Pero a "
                 "alguien que es jalado constantemente entre dos ciudades se le notaría un rastro: recibos, huellas, un zumbido. Buscas el zumbido "
                 "en el cuarto más silencioso del país. Encuentras el ruido de siempre y nada más. La historia de que lo jalan, en su versión más "
                 "simple, ya no se sostiene.")),
             P(T("How the controls work in plain words: the mass and size sliders choose the thing in two places; the model's clock on the left "
                 "shows how fast it would be forced to choose. The right panel is the hum search: the line is how quiet the room was, and the "
                 "model's preferred setting sits on the loud side of it. The knockout removes gravity, so the model predicts nothing at all. The "
                 "planted defect paints the loud side green, which the verifier refuses.",
                 "Cómo funcionan los controles en palabras sencillas: los deslizadores de masa y tamaño eligen la cosa en dos lugares; el reloj "
                 "del modelo a la izquierda muestra qué tan rápido se vería forzada a elegir. El panel derecho es la búsqueda del zumbido: la línea "
                 "es qué tan silencioso estaba el cuarto, y el ajuste preferido del modelo queda del lado ruidoso. El apagado quita la gravedad, así "
                 "que el modelo no predice nada. El defecto plantado pinta de verde el lado ruidoso, lo que el verificador rechaza.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "bound", "en": "II · The bound, recomputed from the counts", "es": "II · La cota, recalculada desde los conteos", "short_en": "II · Bound", "short_es": "II · Cota"},
        {"type": "equation", "text": "dΓ/dω = (2/3) G e² N² N_a / (π^{3/2} ε₀ c³ R0³ ω)    ⇒    z_s(R0) = a / R0³,  a ≈ 1.8 × 10⁻²⁹ m³"},
        P(
            C("BOUND", [DONADI],
              "In a germanium detector at Gran Sasso, 576 photons were counted in the 1,000 to 3,800 keV window over about 62 days against 506 "
              "expected from background, and the predicted spontaneous emission, which scales as 1/R0³ with R0 the size of the nuclear mass "
              "density, sets R0 > 0.54 × 10⁻¹⁰ m with probability 0.95; the parameter-free version of the model, which fixes R0 at the width of "
              "the nuclear wave function in the crystal, 0.05 × 10⁻¹⁰ m, is excluded.",
              "En un detector de germanio en Gran Sasso se contaron 576 fotones en la ventana de 1,000 a 3,800 keV durante unos 62 días frente a "
              "506 esperados del fondo, y la emisión espontánea predicha, que escala como 1/R0³ con R0 el tamaño de la densidad de masa nuclear, "
              "fija R0 > 0.54 × 10⁻¹⁰ m con probabilidad 0.95; la versión sin parámetros del modelo, que fija R0 en el ancho de la función de onda "
              "nuclear en el cristal, 0.05 × 10⁻¹⁰ m, queda excluida."),
            T(" The verifier takes the counts and the paper's rate constant, computes a classical 95 % upper limit on the excess (about 111 "
              "photons) and inverts z_s = a/R0³: it finds R0 > 0.545 × 10⁻¹⁰ m, within 2 % of the published bound. At the parameter-free value "
              "the same formula gives about 1.4 × 10⁵ photons, three orders of magnitude above what was seen.",
              " El verificador toma los conteos y la constante de tasa del artículo, calcula un límite superior clásico al 95 % para el exceso "
              "(unos 111 fotones) e invierte z_s = a/R0³: encuentra R0 > 0.545 × 10⁻¹⁰ m, dentro del 2 % de la cota publicada. En el valor sin "
              "parámetros la misma fórmula da unos 1.4 × 10⁵ fotones, tres órdenes de magnitud por encima de lo visto."),
        ),
        P(
            C("SINGLE RESULT", [XENON],
              "In 2026 the XENONnT collaboration searched its first science run, 1.16 tonne-years of liquid xenon exposure in the 1 to 140 keV "
              "electronic-recoil range, for the same spontaneous radiation and set R0 > 4.9 × 10⁻¹⁰ m at 90 % confidence (4.5 × 10⁻¹⁰ m at 95 %), "
              "about a factor of five beyond the previous world-leading limit.",
              "En 2026 la colaboración XENONnT buscó en su primera corrida científica, 1.16 toneladas-año de exposición de xenón líquido en el "
              "rango de retroceso electrónico de 1 a 140 keV, la misma radiación espontánea y fijó R0 > 4.9 × 10⁻¹⁰ m al 90 % de confianza "
              "(4.5 × 10⁻¹⁰ m al 95 %), alrededor de un factor cinco más allá del límite mundial previo."),
            T(" It is the strongest bound and, inside the ledger's replication window, a SINGLE RESULT; the row will read BOUND once it is two "
              "years old or another detector reaches it. The same paper constrains an unrelated collapse model, CSL, by two orders of magnitude; "
              "CSL is not a gravity model and is outside this page.",
              " Es la cota más fuerte y, dentro de la ventana de replicación del libro de registro, un RESULTADO ÚNICO; la fila dirá COTA cuando "
              "cumpla dos años u otro detector la alcance. El mismo artículo acota un modelo de colapso no relacionado, CSL, por dos órdenes de "
              "magnitud; CSL no es un modelo de gravedad y queda fuera de esta página."),
        ),
        P(
            C("SINGLE RESULT", [FEIN],
              "Matter-wave interference has been observed for molecules beyond 25,000 atomic mass units, the heaviest superpositions built so far.",
              "Se ha observado interferencia de ondas de materia para moléculas de más de 25,000 unidades de masa atómica, las superposiciones más pesadas construidas hasta ahora."),
            T(" In the model, such a molecule treated as a nanometre-sized sphere would take tens of thousands of years to collapse, so "
              "interferometry does not yet test the proposal directly; the radiation does, and that is why the bound comes from an underground "
              "detector rather than a beam.",
              " En el modelo, tal molécula tratada como esfera de un nanómetro tardaría decenas de miles de años en colapsar, así que la "
              "interferometría todavía no prueba la propuesta directamente; la radiación sí, y por eso la cota viene de un detector subterráneo y no de un haz."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "open", "en": "III · What this page does not say", "es": "III · Lo que esta página no dice", "short_en": "III · Not said", "short_es": "III · No dicho"},
        P(
            T("The bound applies to the non-dissipative, parameter-free form of the model, the form Penrose proposed. Variants with dissipation, "
              "or with R0 left as a free parameter above the bound, are not excluded by these experiments, and this page does not assess them. "
              "The page also does not say that superpositions never collapse; it says that gravity, in this one proposed way, does not do it at the rate its parameter-free form predicts.",
              "La cota aplica a la forma no disipativa y sin parámetros del modelo, la forma que propuso Penrose. Las variantes con disipación, o "
              "con R0 dejado como parámetro libre por encima de la cota, no quedan excluidas por estos experimentos, y esta página no las evalúa. "
              "La página tampoco dice que las superposiciones nunca colapsan; dice que la gravedad, de esta manera propuesta, no lo hace al ritmo que predice su forma sin parámetros."),
        ),
        P(
            C("OPEN", [PENROSE, DONADI],
              "What a superposition of two gravitational fields is, if it neither collapses at the proposed rate nor has been shown to "
              "entangle, is not a question these bounds answer; they close one road and leave the destination open.",
              "Qué es una superposición de dos campos gravitatorios, si ni colapsa al ritmo propuesto ni se ha mostrado que entrelaza, no es una "
              "pregunta que estas cotas respondan; cierran un camino y dejan el destino abierto."),
            T(" The next page takes up the strangest version of that question: an equation for the whole with no time in it at all.",
              " La siguiente página retoma la versión más extraña de esa pregunta: una ecuación para el todo sin tiempo alguno."),
        ),
        {"type": "h2", "id": "ladder", "en": "IV · Where the smearing may live", "es": "IV · Dónde puede vivir el suavizado", "short_en": "IV · Ladder", "short_es": "IV · Escalera"},
        {"type": "sigma_ladder"},
        P(
            C("BOUND", [HELOU, DONADI, XENON],
              "The model has one free length, the width σ over which each mass is smeared, and the radiation it predicts has bounded that "
              "length from below three times: analysis of LISA Pathfinder data put it above 40 fm in 2017, the Gran Sasso germanium "
              "detector above 0.54 Å in 2021, and XENONnT above 4.9 Å in 2026.",
              "El modelo tiene una longitud libre, el ancho σ sobre el que se suaviza cada masa, y la radiación que predice ha acotado esa "
              "longitud por abajo tres veces: el análisis de los datos de LISA Pathfinder la puso por encima de 40 fm en 2017, el "
              "detector de germanio de Gran Sasso por encima de 0.54 Å en 2021, y XENONnT por encima de 4.9 Å en 2026."),
            T(" The ladder draws them as the left edge of the allowed region. Everything else on it is a use of the same parameter, and the "
              "uses disagree.",
              " La escalera las dibuja como el borde izquierdo de la región permitida. Todo lo demás en ella es un uso del mismo parámetro, y "
              "los usos no coinciden."),
        ),
        P(
            C("PROPOSED", [TILLOY, HAMEROFF, PENROSE],
              "Two very different uses want σ small. The authors of the hybrid form that the 2025 entanglement letter builds on called it "
              "'the natural cutoff σ ∼ 10⁻¹² cm', a hundredth of a picometre. The one biological use of the model, Orch-OR, holds that "
              "consciousness-related collapse follows 'the specific Diósi-Penrose scheme'; on Penrose's formula the kernel finds that a "
              "single tubulin, 55 kDa, in two places a nucleon radius apart lives 6.5 × 10⁸ s at σ = 10⁻¹⁴ m and about 10³⁷ s at the "
              "laboratory rungs near 33 µm, some 5 × 10¹⁹ ages of the universe: nearly twenty-nine orders of magnitude between the two uses of one number.",
              "Dos usos muy distintos quieren σ pequeña. Los autores de la forma híbrida sobre la que se construye la carta de entrelazamiento "
              "de 2025 la llamaron 'el corte natural σ ∼ 10⁻¹² cm', una centésima de picómetro. El único uso biológico del modelo, Orch-OR, "
              "sostiene que el colapso ligado a la conciencia sigue 'el esquema específico de Diósi-Penrose'; con la fórmula de Penrose el núcleo "
              "encuentra que una sola tubulina, 55 kDa, en dos lugares a un radio de nucleón vive 6.5 × 10⁸ s a σ = 10⁻¹⁴ m y unos 10³⁷ s en "
              "los peldaños de laboratorio cerca de 33 µm, unas 5 × 10¹⁹ edades del universo: casi veintinueve órdenes de magnitud entre los dos usos de un mismo número."),
            T(" The page does not assess Orch-OR; it reports what the model's own formula gives at each rung. Its planted defect for this "
              "kernel drops the small-displacement series, so the direct difference returns rounding noise six orders of magnitude off and "
              "breaks the σ³ law between the top rungs, which the verifier rejects.",
              " La página no evalúa Orch-OR; reporta lo que la fórmula propia del modelo da en cada peldaño. Su defecto plantado para este "
              "núcleo quita la serie de desplazamiento pequeño, así que la diferencia directa devuelve ruido de redondeo seis órdenes de "
              "magnitud fuera y rompe la ley σ³ entre los peldaños superiores, lo que el verificador rechaza."),
        ),
        P(
            C("PROPOSED", [TRILLO, LEE, LEE21, PICCIONE],
              "At the top of the ladder sits the 2025 letter's 50 to 250 µm, the range in which the model entangles two masses in a "
              "laboratory; well below it, at 33 µm, sits T.05's recast of the experiment's published 95 % limits onto the model's softened pull. On that "
              "recast the inverse-square tests leave room only below that line, and the entanglement letter needs the range above it. A 2025 preprint on the smearing profiles of these models notes that for "
              "this parameter 'upper bounds can be put by observing no deviations from Newton's law of gravitation'; it works none out and names no "
              "experiment. The 33 µm rung is this site's own recast of the published limits on T.05, not the preprint's and not a refit of the data; it superseded an earlier 44 µm edge match. Below the rung the balance loses reach quickly: at σ = 25 µm the smeared pull mimics a Yukawa of "
              "11 µm range about seven times too weak for the published limit there, at 18 µm a 7 µm range about 140 times too weak, and at 13.6 µm the "
              "mimic falls to the shortest tabulated range, 5 µm, some five thousand times too weak; the room below 33 µm is there because no "
              "experiment reaches near-gravitational strength at ranges of 5 to 10 µm, not because of a gap in the data. T.05 adds a rung of another kind: if gravity is quantum and pure collapse exists besides, a positive witness at the 2017 geometry would put σ above 130 µm within this pure-collapse model. The ladder also carries a window of another kind, 13.6 to 33 µm: on this site's estimate the letter's model could still entangle one published geometry there, the 2024 side-by-side proposal, without contradicting the 2020 inverse-square data; it is a window for that one model and that one geometry, not a bound on σ, and it moves or closes if the 2020 data are refit.",
              "En lo alto de la escalera están los 50 a 250 µm de la carta de 2025, el rango en que el modelo entrelaza dos masas en un "
              "laboratorio; bastante más abajo, a 33 µm, está el recast que T.05 hace de los límites publicados del experimento al 95 % sobre la atracción "
              "suavizada del modelo. En ese recast las pruebas del inverso del cuadrado dejan sitio solo por debajo de esa línea, y la carta de "
              "entrelazamiento necesita el rango por encima. Una prepublicación de 2025 sobre los "
              "perfiles de suavizado de estos modelos anota que para este parámetro 'se pueden poner cotas superiores observando que no hay desviaciones "
              "de la ley de gravitación de Newton'; no calcula ninguna ni nombra experimento alguno. El peldaño de 33 µm es el recast propio de este sitio "
              "de los límites publicados en T.05, no el de la prepublicación ni un reajuste de los datos; sustituyó a un ajuste de borde anterior de 44 µm. Por debajo del peldaño la balanza pierde alcance deprisa: a σ = 25 µm la atracción "
              "suavizada imita un Yukawa de 13 µm de alcance unas siete veces más débil que el límite publicado allí, a 18 µm uno de 7 µm unas 140 veces "
              "más débil, y a 13.6 µm la imitación cae al alcance tabulado más corto, 5 µm, unas cinco mil veces más débil; el sitio por debajo de "
              "33 µm existe porque ningún experimento alcanza intensidad casi gravitatoria a alcances de 5 a 10 µm, no por un hueco en los datos. T.05 añade un peldaño de otra clase: si la gravedad es "
              "cuántica y además existe el colapso puro, un testigo positivo en la geometría de 2017 pondría σ por encima de 130 µm dentro de este modelo de colapso puro. La escalera lleva además una ventana de otra clase, de 13.6 a 33 µm: en la estimación de este sitio el modelo de la carta aún podría entrelazar allí una geometría publicada, la propuesta lado a lado de 2024, sin contradecir los datos de 2020 del inverso del cuadrado; es una ventana para ese único modelo y esa única geometría, no una cota de σ, y se mueve o se cierra si los datos de 2020 se reajustan."),
            C("BOUND", [GERACI, LEE],
              " One experiment has worked at a smaller separation than the balance's 52 µm: a micro-cantilever about 25 µm from its source mass, "
              "whose published 95 % limits exclude strengths above 14,000 at a range of 10 µm. Set beside the balance's own tabulated limits on the "
              "magnitude, the balance is the stronger at ranges from 10 to 66 µm (3,100 at 10 µm) and the cantilever at 6 µm (460,000 against "
              "730,000), where its limit is still about two thousand times the strength the smeared pull would need. Neither table reaches the "
              "room below the rung.",
              " Un experimento ha trabajado a una separación menor que los 52 µm de la balanza: un microvoladizo a unos 25 µm de su masa fuente, "
              "cuyos límites publicados al 95 % excluyen intensidades por encima de 14,000 a un alcance de 10 µm. Puestos junto a los límites "
              "tabulados de la propia balanza sobre la magnitud, la balanza es la más fuerte en alcances de 10 a 66 µm (3,100 a 10 µm) y el "
              "microvoladizo a 6 µm (460,000 frente a 730,000), donde su límite sigue siendo unas dos mil veces la intensidad que la atracción "
              "suavizada necesitaría. Ninguna de las dos tablas alcanza el sitio por debajo del peldaño."),
            T(" ", " "),
            C("BOUND", [OPPENHEIM],
              "The same torsion balances enter a second squeeze: in 2023 Oppenheim and co-workers showed that any consistent theory with "
              "classical gravity and quantum matter must trade decoherence of the matter against diffusion of the field, bounded that "
              "diffusion with Cavendish-type and rotating-attractor measurements at D₂ ≤ 10⁻⁴¹ kg² s m⁻³, and named the Diósi–Penrose kernel "
              "as a member of the class.",
              "Las mismas balanzas de torsión entran en un segundo apretón: en 2023 Oppenheim y colaboradores mostraron que toda teoría "
              "consistente con gravedad clásica y materia cuántica debe intercambiar decoherencia de la materia por difusión del campo, "
              "acotaron esa difusión con mediciones tipo Cavendish y de atractor giratorio en D₂ ≤ 10⁻⁴¹ kg² s m⁻³, y nombraron al núcleo de "
              "Diósi–Penrose como miembro de la clase."),
            T(" At the laboratory rungs the model is quiet: its own decoherence falls as σ⁻³ for separations well inside the smearing, by the "
              "letter's expansion, and the radiation the three detectors bounded scales as 1/R0³, which is why their bounds run from below and sit "
              "a hundred thousand times or more under the entangling range. The handles built on the model's noise or coherence go slack as σ "
              "grows; the deficit in the mean pull grows instead, which is why the inverse-square tests are where this site's T.05 estimate is set "
              "against the model.",
              " En los peldaños de laboratorio el modelo es silencioso: su propia decoherencia cae como σ⁻³ para separaciones bien dentro del "
              "suavizado, por la expansión de la carta, y la radiación que acotaron los tres detectores escala como 1/R0³, por lo que sus cotas "
              "corren desde abajo y quedan cien mil veces o más por debajo del rango que entrelaza. Las asas construidas sobre el ruido o la "
              "coherencia del modelo se aflojan al crecer σ; el déficit en la atracción media crece en cambio, y por eso las pruebas del inverso "
              "del cuadrado son donde la estimación T.05 de este sitio se confronta con el modelo."),
            C("PROPOSED", [OPPENHEIM, LEE],
              "The same torque residuals could be read into the 2023 trade-off itself. Its authors bound the field diffusion of the Diósi–Penrose-kernel "
              "class from the variance of the time-averaged force on a composite body, a sum over its nuclei of incoherent kicks, so that the ceiling "
              "grows with the number of atoms N and with the nuclear radius cubed, and they fed it Cavendish-class numbers, a 10⁻⁷ m/s² scatter over "
              "100 s on a kilogram, for a ceiling of 10⁻⁹ kg² s m⁻¹ against an interferometry floor of 10⁻⁴⁰, a squeeze they call extremely "
              "conservative. Read with the 2020 torques instead, a residual of 0.005 fN·m on a 2 g platinum foil at an 18 mm lever arm over an averaging "
              "time of 10³ to 10⁴ s, their formula gives a ceiling between 10⁻²⁶ and 10⁻²², thirteen to sixteen orders lower, and the gap above the "
              "interferometry floor would shrink from thirty-one orders to between fourteen and eighteen.",
              "Los mismos residuos de par podrían leerse dentro del propio intercambio de 2023. Sus autores acotan la difusión del campo de la clase "
              "de núcleo de Diósi–Penrose desde la varianza de la fuerza promediada en el tiempo sobre un cuerpo compuesto, una suma sobre sus núcleos "
              "de golpes incoherentes, de modo que el techo crece con el número de átomos N y con el cubo del radio nuclear, y la alimentaron con "
              "números de clase Cavendish, una dispersión de 10⁻⁷ m/s² en 100 s sobre un kilogramo, para un techo de 10⁻⁹ kg² s m⁻¹ frente a un piso "
              "de interferometría de 10⁻⁴⁰, un apretón que ellos llaman extremadamente conservador. Leída con los pares de 2020, un residuo de "
              "0.005 fN·m sobre una lámina de platino de 2 g a un brazo de 18 mm en un tiempo de promediado de 10³ a 10⁴ s, su fórmula da un techo "
              "entre 10⁻²⁶ y 10⁻²², de trece a dieciséis órdenes más bajo, y la brecha sobre el piso de interferometría se encogería de treinta y un órdenes a entre catorce y dieciocho."),
            T(" That is their estimate with better inputs, not a bound: the step from a torque residual to an acceleration is a heuristic at the level "
              "of their own Cavendish step, the averaging time is this page's assumption and enters linearly, and the number says nothing about the "
              "smeared model of T.05, whose granularity is σ rather than a nucleus and whose ceiling would sit (σ/r_N)³ higher.",
              " Esa es su estimación con mejores entradas, no una cota: el paso de un residuo de par a una aceleración es una heurística al nivel de su "
              "propio paso Cavendish, el tiempo de promediado es una suposición de esta página y entra linealmente, y el número no dice nada del modelo "
              "suavizado de T.05, cuya granularidad es σ y no un núcleo y cuyo techo quedaría (σ/r_N)³ más alto."),
        ),
        P(
            C("OPEN", [TRILLO, HAMEROFF, HELOU, LEE],
              "No single σ serves every use on the ladder: the bounds want it above 5 Å, the biological use needs the bottom of the ladder, "
              "the entanglement letter needs the top, and the inverse-square tests, on this site's recast of their published limits, leave room only under 33 µm. The ladder "
              "shows that and the page draws no conclusion beyond it; which rung gives way is for the experiments to decide.",
              "Ninguna σ sirve a todos los usos de la escalera: las cotas la quieren por encima de 5 Å, el uso biológico necesita el fondo "
              "de la escalera, la carta de entrelazamiento necesita la cima, y las pruebas del inverso del cuadrado, en el recast que este sitio hace de sus límites publicados, dejan sitio "
              "solo por debajo de 33 µm. La escalera muestra eso y la página no concluye nada más allá; qué peldaño cede lo decidirán los experimentos."),
        ),
        {"type": "change_box",
         "items": [
             ("A measured excess of spontaneous radiation with the predicted 1/R0³ spectrum, seen by two detectors, would turn the BOUND into a measurement of R0 and the page would be rewritten.",
              "Un exceso medido de radiación espontánea con el espectro 1/R0³ predicho, visto por dos detectores, convertiría la COTA en una medición de R0 y la página se reescribiría."),
             ("The XENONnT row leaves the replication window in 2028 or when a second detector reaches its bound; either moves its claim from SINGLE RESULT to BOUND.",
              "La fila de XENONnT sale de la ventana de replicación en 2028 o cuando un segundo detector alcance su cota; cualquiera de las dos mueve su afirmación de RESULTADO ÚNICO a COTA."),
             ("A refit of the Eöt-Wash data for the smeared potential, published by its collaboration, would turn the ladder's 33 µm rung from this site's recast of the published limits into a BOUND, in either direction. Until November 2026 the rung stood at 44 µm, a match to the gravitational-strength edge at one separation; the recast superseded it.",
              "Un reajuste de los datos de Eöt-Wash para el potencial suavizado, publicado por su colaboración, convertiría el peldaño de 33 µm de la escalera, recast propio de este sitio de los límites publicados, en una COTA, en cualquier dirección. Hasta noviembre de 2026 el peldaño estuvo en 44 µm, un ajuste al borde de intensidad gravitatoria a una sola separación; el recast lo sustituyó."),
             ("If the recomputed bound ever drifted more than 20 % from the published 0.54 × 10⁻¹⁰ m after a constants change, the verifier fails and the page does not build.",
              "Si la cota recalculada llegara a desviarse más del 20 % de los 0.54 × 10⁻¹⁰ m publicados tras un cambio de constantes, el verificador falla y la página no se construye."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · E_G two ways", "Etapa 1 · E_G de dos maneras",
         "E_G(d) = 2 U_self − U_int(d) with U_self = (3/5) G M²/R and U_int the interaction energy of two uniform spheres (G M²/d beyond contact, a quintic polynomial in d/2R when they overlap, 2 U_self when they coincide). The verifier integrates the potential of one sphere over the volume of the other on a grid and requires agreement with the closed form within 10⁻³; E_G → (6/5) G M²/R at large d and → 0 at d = 0.",
         "E_G(d) = 2 U_propia − U_int(d) con U_propia = (3/5) G M²/R y U_int la energía de interacción de dos esferas uniformes (G M²/d más allá del contacto, un polinomio quíntico en d/2R cuando se traslapan, 2 U_propia cuando coinciden). El verificador integra el potencial de una esfera sobre el volumen de la otra en una malla y exige coincidencia con la forma cerrada dentro de 10⁻³; E_G → (6/5) G M²/R a d grande y → 0 en d = 0."),
        ("Stage 2 · The predicted radiation", "Etapa 2 · La radiación predicha",
         "Donadi et al. Eq. 4: dΓ/dω = (2/3) G e² N² N_a / (π^{3/2} ε₀ c³ R0³ ω), with N the atomic number and N_a the number of atoms. Integrated over the 1,000 to 3,800 keV window and 62 days this is z_s = a/R0³ with a ≈ 1.8 × 10⁻²⁹ m³ (the paper's value, which includes the detector's efficiency). The verifier recomputes a without efficiency and gets about 1.0 × 10⁻²⁸ m³, within a factor of ten.",
         "Donadi et al., Ec. 4: dΓ/dω = (2/3) G e² N² N_a / (π^{3/2} ε₀ c³ R0³ ω), con N el número atómico y N_a el número de átomos. Integrada sobre la ventana de 1,000 a 3,800 keV y 62 días es z_s = a/R0³ con a ≈ 1.8 × 10⁻²⁹ m³ (el valor del artículo, que incluye la eficiencia del detector). El verificador recalcula a sin eficiencia y obtiene cerca de 1.0 × 10⁻²⁸ m³, dentro de un factor de diez."),
        ("Stage 3 · From counts to a bound", "Etapa 3 · De conteos a cota",
         "576 counted, 506 expected: a classical 95 % upper limit on a Poisson signal over known background gives about 111 photons. Setting a/R0³ ≤ 111 gives R0 > 0.545 × 10⁻¹⁰ m, against the paper's 0.54 × 10⁻¹⁰ m (the paper uses a Bayesian treatment; the verifier accepts agreement within 20 %).",
         "576 contados, 506 esperados: un límite superior clásico al 95 % para una señal de Poisson sobre fondo conocido da unos 111 fotones. Imponer a/R0³ ≤ 111 da R0 > 0.545 × 10⁻¹⁰ m, frente a los 0.54 × 10⁻¹⁰ m del artículo (el artículo usa un tratamiento bayesiano; el verificador acepta coincidencia dentro del 20 %)."),
        ("Stage 4 · The side of the line", "Etapa 4 · El lado de la línea",
         "Allowed: R0 at or above the bound. Excluded: below it, including the parameter-free 0.05 × 10⁻¹⁰ m (about 1.4 × 10⁵ predicted photons). The planted defect inverts the orientation and would call the parameter-free value allowed; the verifier fails, as it must. XENONnT's 4.9 × 10⁻¹⁰ m lies on the allowed side and tightens it.",
         "Permitido: R0 en la cota o por encima. Excluido: por debajo, incluido el 0.05 × 10⁻¹⁰ m sin parámetros (unos 1.4 × 10⁵ fotones predichos). El defecto plantado invierte la orientación y llamaría permitido al valor sin parámetros; el verificador falla, como debe. Los 4.9 × 10⁻¹⁰ m de XENONnT quedan del lado permitido y lo estrechan."),
    ],
    "sidenotes": [
        ("SIDENOTE T.06-A · WHY THE RADIATION, NOT THE COLLAPSE", "NOTA T.06-A · POR QUÉ LA RADIACIÓN, NO EL COLAPSO",
         "Catching a collapse needs a superposition heavy enough to collapse fast and isolated enough to show it; nobody has one. The radiation the model implies needs only matter and a quiet detector. The weaker-looking test is the one that could be done.",
         "Atrapar un colapso necesita una superposición lo bastante pesada para colapsar rápido y lo bastante aislada para mostrarlo; nadie tiene una. La radiación que el modelo implica necesita solo materia y un detector silencioso. La prueba que parece más débil es la que se pudo hacer."),
        ("SIDENOTE T.06-B · WHAT BOUND MEANS", "NOTA T.06-B · QUÉ SIGNIFICA COTA",
         "A BOUND is a measurement of what is not there. It does not confirm the model; it tells the model where it may not live. The label is deliberately separate from MEASURED and from PROPOSED.",
         "Una COTA es una medición de lo que no está. No confirma el modelo; le dice al modelo dónde no puede vivir. La etiqueta es deliberadamente distinta de MEDIDO y de PROPUESTO."),
    ],
    "sources": [
        ("Diósi, L. (1987). A universal master equation for the gravitational violation of quantum mechanics. Physics Letters A, 120(8), 377–381.", "10.1016/0375-9601(87)90681-5"),
        ("Penrose, R. (1996). On gravity's role in quantum state reduction. General Relativity and Gravitation, 28(5), 581–600.", "10.1007/BF02105068"),
        ("Donadi, S., Piscicchia, K., Curceanu, C., Diósi, L., Laubenstein, M., & Bassi, A. (2021). Underground test of gravity-related wave function collapse. Nature Physics, 17, 74–78.", "10.1038/s41567-020-1008-4"),
        ("Aprile, E., et al. (XENONnT Collaboration) (2026). Challenging spontaneous quantum collapse with XENONnT. Physical Review Letters, 136, 120201.", "10.1103/2jm3-4976"),
        ("Fein, Y. Y., Geyer, P., Zwick, P., Kiałka, F., Pedalino, S., Mayor, M., Gerlich, S., & Arndt, M. (2019). Quantum superposition of molecules beyond 25 kDa. Nature Physics, 15, 1242–1245.", "10.1038/s41567-019-0663-9"),
        ("Helou, B., Slagmolen, B. J. J., McClelland, D. E., & Chen, Y. (2017). LISA pathfinder appreciably constrains collapse models. Physical Review D, 95, 084054.", "10.1103/PhysRevD.95.084054"),
        ("Hameroff, S., & Penrose, R. (2014). Consciousness in the universe: A review of the 'Orch OR' theory. Physics of Life Reviews, 11(1), 39–78.", "10.1016/j.plrev.2013.08.002"),
        ("Oppenheim, J., Sparaciari, C., Šoda, B., & Weller-Davies, Z. (2023). Gravitationally induced decoherence vs space-time diffusion: testing the quantum nature of gravity. Nature Communications, 14, 7910.", "10.1038/s41467-023-43348-2"),
        ("Tilloy, A., & Diósi, L. (2016). Sourcing semiclassical gravity from spontaneously localized quantum matter. Physical Review D, 93, 024026.", "10.1103/PhysRevD.93.024026"),
        ("Trillo, D., & Navascués, M. (2025). The Diósi-Penrose model of classical gravity predicts gravitationally induced entanglement. Physical Review D, 111, L121101.", "10.1103/PhysRevD.111.L121101"),
        ("Lee, J. G., Adelberger, E. G., Cook, T. S., Fleischer, S. M., & Heckel, B. R. (2020). New test of the gravitational 1/r² law at separations down to 52 µm. Physical Review Letters, 124, 101101.", "10.1103/PhysRevLett.124.101101"),
        ("Piccione, N. (2025). Diffusion minimization via optimal smearing in collapse and hybrid classical-quantum gravitational models. arXiv:2511.00644.", "10.48550/arXiv.2511.00644"),
        ("Lee, J. G., Adelberger, E. G., Marcoline, F. V., Terrano, W. A., & Heckel, B. R. (2021). The Fourier–Bessel expansion: application to experimental probes of gravity and feeble short-range interactions. Classical and Quantum Gravity, 38, 085020.", "10.1088/1361-6382/abebf2"),
    ],
}
