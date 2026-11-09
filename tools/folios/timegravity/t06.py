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

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "date": "2026-11-09",
    "order_label_en": "Reading order 7 of 9",
    "order_label_es": "Orden de lectura 7 de 9",
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
        "La propuesta de colapso de Diosi y Penrose, la radiación espontánea que predice, y las cotas de Gran Sasso y XENONnT recalculadas a partir de los conteos publicados.",
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
    "ledger_ids": [DIOSI, PENROSE, DONADI, XENON, FEIN],
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
        {"type": "change_box",
         "items": [
             ("A measured excess of spontaneous radiation with the predicted 1/R0³ spectrum, seen by two detectors, would turn the BOUND into a measurement of R0 and the page would be rewritten.",
              "Un exceso medido de radiación espontánea con el espectro 1/R0³ predicho, visto por dos detectores, convertiría la COTA en una medición de R0 y la página se reescribiría."),
             ("The XENONnT row leaves the replication window in 2028 or when a second detector reaches its bound; either moves its claim from SINGLE RESULT to BOUND.",
              "La fila de XENONnT sale de la ventana de replicación en 2028 o cuando un segundo detector alcance su cota; cualquiera de las dos mueve su afirmación de RESULTADO ÚNICO a COTA."),
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
    ],
}
