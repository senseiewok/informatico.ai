# -*- coding: utf-8 -*-
"""Time & Gravity · T.09 — A horizon rings like a bell.

Instrument: Kerr horizon geometry, Smarr's identity, and Leaver's (1985) coupled angular + radial 3-term continued-fraction
solver for the l=m=2, n=0 fundamental and n=1 first-overtone quasinormal modes across spin chi in [0, 0.90].
Knockout / planted defect: flipping the spin sign under the radical (or locking to a spin-blind Schwarzschild horizon)
violates Smarr's identity and Leaver's radial continued fraction.
Verifier: skills/timegravity/t09/verify_t09_kerr_ringdown.py.
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t09"
CODE = "T.09"

ABBOTT = "T10-ABBOTT2016"
ABBOTT_GR = "T09-ABBOTT2016B"
ISI21 = "T10-ISI2021"
KERR = "T09-KERR1963"
H71 = "T10-HAWKING1971"
SMARR = "T09-SMARR1973"
TEUK = "T09-TEUKOLSKY1973"
LEAVER = "T09-LEAVER1985"
ISI19 = "T09-ISI2019"
COTESTA = "T09-COTESTA2022"
LVK25 = "T10-LVK2025"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "date": "2026-11-10",
    "order_label_en": "Step 10 of 14",
    "order_label_es": "Paso 10 de 14",
    "kicker_en": "Time & Gravity · T.09 · Where a newly merged horizon rings at frequencies fixed by mass and spin alone",
    "kicker_es": "Tiempo y Gravedad · T.09 · Donde un horizonte recién fusionado resuena a frecuencias fijadas solo por masa y espín",
    "title_en": "A Horizon Rings Like a Bell",
    "title_es": "Un Horizonte Resuena Como una Campana",
    "standfirst_en": (
        "Hawking radiation is sixty nanokelvin for a solar-mass black hole, far below the cosmic microwave sky. Yet the classical "
        "Kerr horizon geometry that underpins Bekenstein–Hawking thermodynamics is tested directly whenever two black holes merge: "
        "the remnant settles by radiating damped gravitational waves—quasinormal modes—whose frequencies and damping times depend "
        "only on its final mass M and dimensionless spin χ. This page solves Leaver's continued fractions for those modes, checks "
        "Smarr's horizon identity, and separates what gravitational-wave detectors have measured from what remains disputed."
    ),
    "standfirst_es": (
        "La radiación de Hawking es de sesenta nanokelvin para un agujero negro de una masa solar, muy por debajo del cielo cósmico "
        "de microondas. Sin embargo, la geometría clásica del horizonte de Kerr que sostiene la termodinámica de Bekenstein y Hawking "
        "se pone a prueba directamente cada vez que dos agujeros negros se fusionan: el remanente se asienta radiando ondas gravitacionales "
        "amortiguadas —modos cuasinormales— cuyas frecuencias y tiempos de amortiguamiento dependen solo de su masa final M y su espín "
        "adimensional χ. Esta página resuelve las fracciones continuas de Leaver para esos modos, comprueba la identidad de horizonte de "
        "Smarr, y separa lo que los detectores de ondas gravitacionales han medido de lo que sigue en disputa."
    ),
    "seo": (
        "A Horizon Rings Like a Bell: Kerr Quasinormal Modes and Leaver's Continued Fractions",
        "How a spinning Kerr black hole rings down at frequencies fixed by mass and spin alone, solved from Leaver's continued fractions and checked against GW150914 and GW250114.",
        "Un Horizonte Resuena Como una Campana: Modos Cuasinormales de Kerr y Fracciones Continuas de Leaver",
        "Cómo un agujero negro de Kerr en rotación resuena a frecuencias fijadas solo por masa y espín, resueltas con las fracciones continuas de Leaver y confrontadas con GW150914 y GW250114.",
    ),
    "reading_time_en": "14 min read",
    "reading_time_es": "14 min de lectura",
    "central_number_en": "Leaver continued-fraction solver converges to < 2.8e-15 across χ ∈ [0, 0.90] (matching published tables to < 8.4e-9); at M = 62 M_☉, χ = 0.68: r_+ = 158.7 km, A = 365,125 km², f₂₂₀ = 273.1 Hz, τ₂₂₀ = 3.75 ms",
    "central_number_es": "El solver de fracciones continuas de Leaver converge a < 2.8e-15 en χ ∈ [0, 0.90] (coincidiendo con las tablas publicadas a < 8.4e-9); en M = 62 M_☉, χ = 0.68: r_+ = 158.7 km, A = 365,125 km², f₂₂₀ = 273.1 Hz, τ₂₂₀ = 3.75 ms",
    "verifier": "skills/timegravity/t09/verify_t09_kerr_ringdown.py",
    "generator": "skills/timegravity/t09/make_t09.py",
    "skill": "skills/timegravity/t09/SKILL.md",
    "skill_filename": "timegravity-t09-kerr-ringdown.SKILL.md",
    "open_question_en": "If the classical horizon has no hair and only grows, what happens to quantum information when the black hole evaporates?",
    "open_question_es": "Si el horizonte clásico no tiene pelo y solo crece, ¿qué pasa con la información cuántica cuando el agujero negro se evapora?",
    "ledger_ids": [ABBOTT, ABBOTT_GR, ISI21, KERR, H71, SMARR, TEUK, LEAVER, ISI19, COTESTA, LVK25],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any observation, theorem or derivation cited on this page. "
        "The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna observación, teorema o derivación citados en esta "
        "página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien mantiene el sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "kerr",
        "title_en": "Instrument · Kerr ringdown spectroscopy from Leaver's continued fractions",
        "title_es": "Instrumento · Espectroscopía de resonancia de Kerr desde las fracciones continuas de Leaver",
        "how_en": (
            "Left: the damped ringdown waveform h(t) of the fundamental (ℓ=m=2, n=0) mode and the faster-decaying first overtone "
            "(ℓ=m=2, n=1) for a Kerr remnant of mass M and dimensionless spin χ. Right: the Kerr trajectory in the frequency–damping "
            "plane (f₂₂₀, τ₂₂₀) and (f₂₂₁, τ₂₂₁) as spin rises from χ = 0 (Schwarzschild) to χ = 0.90, alongside the outer horizon "
            "radius r_+, horizon area A(M, χ), and Smarr balance. The sliders adjust M / M_☉ (20 to 100) and χ (0.00 to 0.90); the "
            "fiducial preset (62 M_☉, χ = 0.68) sits at f₂₂₀ = 273.1 Hz, τ₂₂₀ = 3.75 ms. The knockout corrupts the Kerr radical "
            "√(1 − χ²) (or locks to a spin-blind Schwarzschild formula): Smarr's identity and Leaver's radial continued fraction fail, "
            "and the verifier rejects the run. Keyboard: Tab and arrows. With reduced motion on, nothing animates."
        ),
        "how_es": (
            "Izquierda: la forma de onda amortiguada h(t) del modo fundamental (ℓ=m=2, n=0) y del primer sobretono de decaimiento más "
            "rápido (ℓ=m=2, n=1) para un remanente de Kerr de masa M y espín adimensional χ. Derecha: la trayectoria de Kerr en el plano "
            "frecuencia–amortiguamiento (f₂₂₀, τ₂₂₀) y (f₂₂₁, τ₂₂₁) conforme el espín sube de χ = 0 (Schwarzschild) a χ = 0.90, junto con "
            "el radio del horizonte exterior r_+, el área del horizonte A(M, χ) y el balance de Smarr. Los deslizadores ajustan M / M_☉ "
            "(20 a 100) y χ (0.00 a 0.90); el valor fiducial (62 M_☉, χ = 0.68) se sitúa en f₂₂₀ = 273.1 Hz, τ₂₂₀ = 3.75 ms. El apagado "
            "corrompe el radical de Kerr √(1 − χ²) (o fija una fórmula de Schwarzschild ciega al espín): la identidad de Smarr y la fracción "
            "continua radial de Leaver fallan, y el verificador rechaza la corrida. Teclado: Tab y flechas. Con movimiento reducido, nada se anima."
        ),
    },
    "predict": {
        "q_en": "Before you move the spin slider: if you hold a black hole's mass M fixed and spin it up from χ = 0 to χ = 0.90, what happens to its horizon area A and its fundamental ringdown pitch f₂₂₀?",
        "q_es": "Antes de mover el deslizador de espín: si mantienes fija la masa M de un agujero negro y aumentas su espín de χ = 0 a χ = 0.90, ¿qué pasa con el área de su horizonte A y su frecuencia fundamental de resonancia f₂₂₀?",
        "options": [
            ("Area grows and pitch drops", "El área crece y el tono baja"),
            ("Area shrinks and pitch rises (it rings faster and longer)", "El área se encoge y el tono sube (resuena más rápido y por más tiempo)"),
            ("Both stay unchanged because mass is fixed", "Ambos permanecen iguales porque la masa está fija"),
        ],
        "answer": 1,
        "reveal_en": "Area shrinks as 1 + √(1 − χ²) while the co-rotating (ℓ=m=2) frequency rises by 80 % from χ = 0 to χ = 0.90 and its quality factor more than doubles.",
        "reveal_es": "El área se encoge como 1 + √(1 − χ²) mientras la frecuencia corrotante (ℓ=m=2) sube un 80 % de χ = 0 a χ = 0.90 y su factor de calidad se multiplica por más de dos.",
    },
    "sections": [
        {"type": "h2", "id": "measured", "en": "I · What gravitational-wave detectors have measured", "es": "I · Lo que han medido los detectores de ondas gravitacionales", "short_en": "I · Measured", "short_es": "I · Medido"},
        P(
            C("MEASURED", [ABBOTT, ABBOTT_GR, ISI21],
              "When two black holes merge, the remnant settles through a damped sinusoidal ringdown whose fundamental frequency and damping "
              "time agree with the final Kerr mass and spin inferred from the inspiral: observed in 2015 by the LIGO and Virgo collaborations "
              "in GW150914 (remnant around 62 M_☉ and χ ≈ 0.68, ringing near 250–275 Hz with a 4 ms decay) and independently reanalysed in "
              "2021 to test Hawking's area law on the public strain data.",
              "Cuando dos agujeros negros se fusionan, el remanente se asienta mediante una resonancia sinusoidal amortiguada cuya frecuencia "
              "fundamental y tiempo de amortiguamiento concuerdan con la masa y el espín finales de Kerr inferidos de la fase espiral: observado "
              "en 2015 por las colaboraciones LIGO y Virgo en GW150914 (remanente de unas 62 M_☉ y χ ≈ 0.68, resonando cerca de 250–275 Hz con un "
              "decaimiento de 4 ms) y reanalizado de forma independiente en 2021 para poner a prueba la ley del área de Hawking en los datos públicos de deformación."),
            T(" Those measured merger waveforms anchor the Kerr horizon geometry and quasinormal-mode spectrum derived below.",
              " Esas formas de onda de fusión medidas anclan la geometría del horizonte de Kerr y el espectro de modos cuasinormales derivados abajo."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("Strike a bronze bell with a hammer and it rings with a clear pitch and fades away, plus a handful of higher overtones that "
                 "die out even faster. From the pitch and the fade time you can tell how heavy the bell is and how thick its rim is. "
                 "A newly merged black hole does the same thing, except the bell is made of empty curved spacetime and its rim is the event horizon.",
                 "Golpea una campana de bronce con un martillo y resonará con un tono claro antes de apagarse, más un puñado de sobretonos más agudos "
                 "que se extinguen aún más rápido. Por el tono y el tiempo de caída puedes saber qué tan pesada es la campana y qué tan grueso es su borde. "
                 "Un agujero negro recién fusionado hace lo mismo, salvo que la campana está hecha de espaciotiempo curvo vacío y su borde es el horizonte de sucesos.")),
             P(T("General relativity says a quiet black hole in vacuum is simpler than any bronze bell: it has no bumps, no chemical composition, "
                 "and no memory of what fell in—only a total mass M and a spin χ. Because of that, every single tone and decay time of its ringdown "
                 "is locked by M and χ alone. Measuring two tones at once tests whether the object is truly a hairless Kerr horizon.",
                 "La relatividad general dice que un agujero negro en reposo en el vacío es más simple que cualquier campana de bronce: no tiene "
                 "abolladuras, ni composición química, ni memoria de lo que cayó adentro; solo una masa total M y un espín χ. Por eso, cada tono y "
                 "cada tiempo de caída de su resonancia quedan fijados únicamente por M y χ. Medir dos tonos a la vez pone a prueba si el objeto es "
                 "verdaderamente un horizonte de Kerr sin pelo.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: a spinning top that is tapped on the side wobbles back to vertical. A heavier top wobbles more slowly; "
                 "a faster-spinning top wobbles at a higher pitch and takes more turns before settling.",
                 "Analogía cotidiana: un trompo en rotación al que se le da un golpecito lateral se tambalea hasta volver a la vertical. Un trompo "
                 "más pesado se tambalea más despacio; un trompo que gira más rápido vibra con un tono más agudo y da más vueltas antes de asentarse.")),
             P(T("How the controls work in plain words: the mass slider scales the size of the horizon, lowering the pitch Hz and lengthening the "
                 "decay time ms in exact proportion to M. The spin slider spins up the horizon from χ = 0 to χ = 0.90, shrinking the horizon area "
                 "while raising the fundamental tone f₂₂₀ and its first overtone f₂₂₁. The knockout corrupts the spin dependence under the square "
                 "root, breaking both Smarr's horizon balance and Leaver's wave equation.",
                 "Cómo funcionan los controles en palabras sencillas: el deslizador de masa escala el tamaño del horizonte, bajando la frecuencia en "
                 "Hz y alargando el tiempo de caída en ms en proporción exacta a M. El deslizador de espín acelera el giro del horizonte de χ = 0 a "
                 "χ = 0.90, encogiendo el área del horizonte mientras sube el tono fundamental f₂₂₀ y su primer sobretono f₂₂₁. El apagado corrompe "
                 "la dependencia del espín bajo la raíz cuadrada, rompiendo tanto el balance de horizonte de Smarr como la ecuación de onda de Leaver.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "derived", "en": "II · Kerr geometry, Smarr's formula, and Leaver's continued fractions", "es": "II · Geometría de Kerr, fórmula de Smarr y fracciones continuas de Leaver", "short_en": "II · Derived", "short_es": "II · Derivado"},
        {"type": "equation", "text": "r_+ = (GM/c²)(1 + √(1 − χ²)),   A = 8π (GM/c²)² (1 + √(1 − χ²)),   Mc² = (κc² / 4πG) A + 2 Ω_H J"},
        P(
            C("DERIVED", [KERR, H71, SMARR, ABBOTT],
              "Kerr's 1963 exact vacuum metric places the outer event horizon at r_+ = (GM/c²)(1 + √(1 − χ²)) with area "
              "A(M, χ) = 8π(GM/c²)²(1 + √(1 − χ²)), which Hawking's 1971 theorem proves cannot decrease in any classical merger; "
              "Smarr's 1973 identity Mc² = (κc² / 4πG) A + 2 Ω_H J and the differential first law d(Mc²) = (κc² / 8πG) dA + Ω_H dJ "
              "tie the horizon's area, surface gravity κ, and angular velocity Ω_H into an exact thermodynamic balance.",
              "La métrica exacta de vacío de Kerr de 1963 sitúa el horizonte de sucesos exterior en r_+ = (GM/c²)(1 + √(1 − χ²)) con área "
              "A(M, χ) = 8π(GM/c²)²(1 + √(1 − χ²)), la cual el teorema de Hawking de 1971 demuestra que no puede disminuir en ninguna fusión "
              "clásica; la identidad de Smarr de 1973 Mc² = (κc² / 4πG) A + 2 Ω_H J y la primera ley diferencial d(Mc²) = (κc² / 8πG) dA + Ω_H dJ "
              "atan el área del horizonte, la gravedad superficial κ y la velocidad angular Ω_H en un balance termodinámico exacto.",
              parent=ABBOTT),
            T(" Across χ ∈ (0.2, 0.5, 0.68, 0.9) the verifier checks Smarr's identity to 1.2×10⁻¹⁶ and the central-difference first law along "
              "independent mass and spin steps to 2.5×10⁻¹⁰.",
              " En χ ∈ (0.2, 0.5, 0.68, 0.9) el verificador comprueba la identidad de Smarr a 1.2×10⁻¹⁶ y la primera ley por diferencias centrales "
              "a lo largo de pasos independientes de masa y espín a 2.5×10⁻¹⁰."),
        ),
        {"type": "equation", "text": "β₀ − α₀γ₁ / (β₁ − α₁γ₂ / (β₂ − …)) = 0   ⇒   Mω_{220}(0.68) = 0.523975 − 0.081513 i"},
        P(
            C("DERIVED", [TEUK, LEAVER, ABBOTT],
              "Teukolsky showed in 1973 that gravitational perturbations (s = −2) of a Kerr black hole separate into coupled angular and radial "
              "master equations, and Leaver showed in 1985 that their quasinormal eigenvalues Mω_{ℓmn}(χ) are the roots of coupled three-term "
              "continued fractions determined solely by (M, χ).",
              "Teukolsky mostró en 1973 que las perturbaciones gravitacionales (s = −2) de un agujero negro de Kerr se separan en ecuaciones "
              "maestras angular y radial acopladas, y Leaver mostró en 1985 que sus autovalores cuasinormales Mω_{ℓmn}(χ) son las raíces de "
              "fracciones continuas acopladas de tres términos determinadas únicamente por (M, χ).",
              parent=ABBOTT),
            T(" Starting only from the Schwarzschild angular eigenvalue A₂₂(0) = 4 and rough WKB seeds, the verifier's homotopy solver tracks "
              "both the fundamental (2,2,0) mode and the first overtone (2,2,1, via Leaver's first inversion) across χ ∈ [0, 0.90] with "
              "continued-fraction residuals below 2.8×10⁻¹⁵, agreeing with published tables to 8.3×10⁻⁹. At the fiducial GW150914 remnant "
              "(M = 62 M_☉, χ = 0.68), the kernel gives r_+ = 158.68 km, A = 365,125 km², f₂₂₀ = 273.07 Hz, τ₂₂₀ = 3.747 ms, and first "
              "overtone f₂₂₁ = 266.80 Hz, τ₂₂₁ = 1.239 ms.",
              " Partiendo únicamente del autovalor angular de Schwarzschild A₂₂(0) = 4 y semillas WKB aproximadas, el solver por homotopía del "
              "verificador sigue tanto el modo fundamental (2,2,0) como el primer sobretono (2,2,1, mediante la primera inversión de Leaver) en "
              "χ ∈ [0, 0.90] con residuos de fracción continua por debajo de 2.8×10⁻¹⁵, coincidiendo con las tablas publicadas a 8.3×10⁻⁹. En el "
              "remanente fiducial de GW150914 (M = 62 M_☉, χ = 0.68), el kernel entrega r_+ = 158.68 km, A = 365,125 km², f₂₂₀ = 273.07 Hz, "
              "τ₂₂₀ = 3.747 ms, y primer sobretono f₂₂₁ = 266.80 Hz, τ₂₂₁ = 1.239 ms."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "open", "en": "III · Overtone disputes, GW250114, and what this page does not say", "es": "III · Disputas de sobretonos, GW250114 y lo que esta página no dice", "short_en": "III · Not said", "short_es": "III · No dicho"},
        P(
            C("PROPOSED", [ISI19],
              "In 2019 Isi, Giesler, Farr, Scheel and Teukolsky proposed testing the Kerr no-hair theorem right at the merger peak of GW150914 "
              "by fitting the n = 0 fundamental and n = 1 first overtone together, reporting evidence for at least one overtone at 3.6σ and a remnant mass and spin in agreement with the full-signal values, a no-hair test at the 10 percent level.",
              "En 2019 Isi, Giesler, Farr, Scheel y Teukolsky propusieron poner a prueba el teorema de ausencia de pelo de Kerr justo en el pico "
              "de fusión de GW150914 ajustando juntos el modo fundamental n = 0 y el primer sobretono n = 1, reportando evidencia de al menos un sobretono a 3.6σ y una masa y un espín del remanente acordes con los valores de la señal completa, una prueba de ausencia de pelo al nivel del 10 por ciento."),
            T(" ", " "),
            C("OPEN", [ISI19, COTESTA],
              "In 2022 Cotesta, Carullo, Berti and Cardoso reanalysed the same GW150914 ringdown window and argued that evidence for the n = 1 "
              "overtone near the peak is sensitive to the chosen start time t₀ and noise fluctuations, leaving whether the first overtone was "
              "cleanly resolved in GW150914 an open question.",
              "En 2022 Cotesta, Carullo, Berti y Cardoso reanalizaron la misma ventana de resonancia de GW150914 y sostuvieron que la evidencia "
              "a favor del sobretono n = 1 cerca del pico es sensible al tiempo de inicio elegido t₀ y a fluctuaciones de ruido, dejando como "
              "pregunta abierta si el primer sobretono se resolvió limpiamente en GW150914."),
        ),
        P(
            C("SINGLE RESULT", [LVK25],
              "In 2025 the LIGO, Virgo and KAGRA collaborations reported GW250114 at network signal-to-noise ratio 80, constraining the "
              "post-merger ringdown mode frequencies to within 30 percent of the Kerr prediction and finding the remnant horizon area larger "
              "than the sum of the initial areas to high credibility.",
              "En 2025 las colaboraciones LIGO, Virgo y KAGRA reportaron GW250114 con relación señal a ruido de red de 80, acotando las "
              "frecuencias de los modos de resonancia posteriores a la fusión dentro del 30 por ciento de la predicción de Kerr y encontrando el "
              "área del horizonte remanente mayor que la suma de las áreas iniciales con alta credibilidad."),
            T(" Under the track's 24-month rule this 2025 row is capped at SINGLE RESULT, and its area figure is quoted strictly as the "
              "collaboration's posterior result—never recomputed from median masses. That brings us to the final page of the track: if a "
              "horizon's area only grows in classical mergers and radiates thermally by Hawking's law, what happens to quantum information when the black hole evaporates?",
              " Bajo la regla de 24 meses de la serie esta fila de 2025 tiene como tope RESULTADO ÚNICO, y su cifra de área se cita estrictamente "
              "como el resultado posterior de la colaboración, nunca recalculada a partir de masas medianas. Eso nos lleva a la última página de la "
              "serie: si el área de un horizonte solo crece en fusiones clásicas y radia térmicamente según la ley de Hawking, ¿qué pasa con la información cuántica cuando el agujero negro se evapora?"),
        ),
        {"type": "change_box",
         "items": [
             ("An independent reanalysis of GW250114's public strain data by a second group after the 24-month window would raise the SNR-80 ringdown and area-law test from SINGLE RESULT to MEASURED.",
              "Un reanálisis independiente de los datos públicos de deformación de GW250114 por un segundo grupo tras la ventana de 24 meses subiría la prueba de resonancia y ley del área con SNR 80 de RESULTADO ÚNICO a MEDIDO."),
             ("Consensus across high-SNR detections on a start-time-independent overtone extraction after the merger peak would resolve the GW150914 overtone dispute (T09-ISI2019 vs T09-COTESTA2022).",
              "Un consenso en detecciones de alta SNR sobre una extracción de sobretonos independiente del tiempo de inicio tras el pico de fusión resolvería la disputa del sobretono en GW150914 (T09-ISI2019 frente a T09-COTESTA2022)."),
             ("If the Leaver continued-fraction solver ever missed published (2,2,0) or (2,2,1) eigenvalues by more than 1e-6 or violated Smarr's identity, the verifier fails and the page does not build.",
              "Si el solver de fracciones continuas de Leaver llegara a fallar los autovalores publicados (2,2,0) o (2,2,1) por más de 1e-6 o violara la identidad de Smarr, el verificador falla y la página no se construye."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · Kerr horizon & Smarr balance", "Etapa 1 · Horizonte de Kerr y balance de Smarr",
         "From (M, χ), compute r_+ = r_g(1 + √(1 − χ²)), A = 8πr_g²(1 + √(1 − χ²)), κ, and Ω_H. Verify Smarr's identity Mc² = (κc² / 4πG)A + 2Ω_H J to 1.2e-16 and the central-difference first law δ(Mc²) = (κc² / 8πG)δA + Ω_H δJ to 2.5e-10.",
         "A partir de (M, χ), calcula r_+ = r_g(1 + √(1 − χ²)), A = 8πr_g²(1 + √(1 − χ²)), κ y Ω_H. Verifica la identidad de Smarr Mc² = (κc² / 4πG)A + 2Ω_H J a 1.2e-16 y la primera ley por diferencias centrales δ(Mc²) = (κc² / 8πG)δA + Ω_H δJ a 2.5e-10."),
        ("Stage 2 · Coupled Teukolsky–Leaver continued fractions", "Etapa 2 · Fracciones continuas acopladas de Teukolsky y Leaver",
         "For s = −2, ℓ = m = 2, evaluate Leaver's 60-term angular continued fraction for A_{22}(χ, Mω) and 140-term radial continued fraction (with n = 0 direct and n = 1 first inversion) by backward Lentz/tail recurrence.",
         "Para s = −2, ℓ = m = 2, evalúa la fracción continua angular de 60 términos de Leaver para A_{22}(χ, Mω) y la fracción continua radial de 140 términos (con n = 0 directa y n = 1 primera inversión) por recurrencia regresiva."),
        ("Stage 3 · Homotopy continuation & benchmark check", "Etapa 3 · Continuación por homotopía y comprobación con tablas",
         "Step χ from 0.00 to 0.90 in increments of 0.02 with linear branch prediction and complex secant polishing. Residuals |R_rad|, |R_ang| < 2.8e-15; solved Mω_{220} and Mω_{221} match Leaver (1985) and Berti–Cardoso–Starinets (2009) within 8.3e-9.",
         "Avanza χ de 0.00 a 0.90 en pasos de 0.02 con predicción lineal de rama y pulido por secante compleja. Residuos |R_rad|, |R_ang| < 2.8e-15; los Mω_{220} y Mω_{221} resueltos coinciden con Leaver (1985) y Berti, Cardoso y Starinets (2009) dentro de 8.3e-9."),
        ("Stage 4 · Planted defect knockout", "Etapa 4 · Apagado por defecto plantado",
         "Flipping the spin sign under the radical √(1 + χ²) breaks the Kerr geometry: Smarr's identity fails by 69.1 %, the differential first law fails by 200 %, and Leaver's radial continued-fraction residual jumps to 2.14, rejecting the run.",
         "Invertir el signo del espín bajo el radical √(1 + χ²) rompe la geometría de Kerr: la identidad de Smarr falla un 69.1 %, la primera ley diferencial falla un 200 %, y el residuo de la fracción continua radial de Leaver salta a 2.14, rechazando la corrida."),
    ],
    "sidenotes": [
        ("SIDENOTE T.09-A · WHY OVERTONES USE LEAVER'S FIRST INVERSION", "NOTA T.09-A · POR QUÉ LOS SOBRETONOS USAN LA PRIMERA INVERSIÓN DE LEAVER",
         "The un-inverted radial continued fraction β₀ − α₀γ₁/(β₁ − …) = 0 is most sensitive to the n = 0 fundamental root. Leaver's Eq. 14 inverts the continued fraction at index n_inv = 1, β₁ − α₀γ₁/β₀ − α₁γ₂/(β₂ − …) = 0, locking onto the n = 1 overtone without branch-jumping.",
         "La fracción continua radial sin invertir β₀ − α₀γ₁/(β₁ − …) = 0 es más sensible a la raíz fundamental n = 0. La Ec. 14 de Leaver invierte la fracción continua en el índice n_inv = 1, β₁ − α₀γ₁/β₀ − α₁γ₂/(β₂ − …) = 0, fijando el sobretono n = 1 sin saltos de rama."),
        ("SIDENOTE T.09-B · WHY MEDIAN MASSES NEVER TEST THE AREA LAW", "NOTA T.09-B · POR QUÉ LAS MASAS MEDIANAS NUNCA PRUEBAN LA LEY DEL ÁREA",
         "Evaluating A(M, χ) at a paper's published median M₁, M₂, M_f is a formula check, not an observational test of δA ≥ 0: the pre- and post-merger parameters must be inferred independently on time-gated inspiral and ringdown data and integrated over their joint posteriors (Isi et al. 2021; LVK 2025).",
         "Evaluar A(M, χ) en las medianas publicadas M₁, M₂, M_f de un artículo es una comprobación de la fórmula, no una prueba observacional de δA ≥ 0: los parámetros previos y posteriores a la fusión deben inferirse de manera independiente en datos truncados en el tiempo e integrarse sobre sus posteriores conjuntas (Isi et al. 2021; LVK 2025)."),
    ],
    "sources": [
        ("Abbott, B. P., et al. (LIGO Scientific Collaboration and Virgo Collaboration) (2016). Observation of gravitational waves from a binary black hole merger. Physical Review Letters, 116(6), 061102.", "10.1103/PhysRevLett.116.061102"),
        ("Abbott, B. P., et al. (LIGO Scientific and Virgo Collaborations) (2016). Tests of general relativity with GW150914. Physical Review Letters, 116(22), 221101.", "10.1103/PhysRevLett.116.221101"),
        ("Isi, M., Farr, W. M., Giesler, M., Scheel, M. A., & Teukolsky, S. A. (2021). Testing the black-hole area law with GW150914. Physical Review Letters, 127(1), 011103.", "10.1103/PhysRevLett.127.011103"),
        ("Kerr, R. P. (1963). Gravitational field of a spinning mass as an example of algebraically special metrics. Physical Review Letters, 11(5), 237–238.", "10.1103/PhysRevLett.11.237"),
        ("Hawking, S. W. (1971). Gravitational radiation from colliding black holes. Physical Review Letters, 26(21), 1344–1346.", "10.1103/PhysRevLett.26.1344"),
        ("Smarr, L. (1973). Mass formula for Kerr black holes. Physical Review Letters, 30(2), 71–73.", "10.1103/PhysRevLett.30.71"),
        ("Teukolsky, S. A. (1973). Perturbations of a rotating black hole. I. Fundamental equations for gravitational, electromagnetic, and neutrino-field perturbations. The Astrophysical Journal, 185, 635–647.", "10.1086/152444"),
        ("Leaver, E. W. (1985). An analytic representation for the quasi-normal modes of Kerr black holes. Proceedings of the Royal Society of London A, 402(1823), 285–298.", "10.1098/rspa.1985.0119"),
        ("Isi, M., Giesler, M., Farr, W. M., Scheel, M. A., & Teukolsky, S. A. (2019). Testing the no-hair theorem with GW150914. Physical Review Letters, 123(11), 111102.", "10.1103/PhysRevLett.123.111102"),
        ("Cotesta, R., Carullo, G., Berti, E., & Cardoso, V. (2022). Analysis of ringdown overtones in GW150914. Physical Review Letters, 129(11), 111102.", "10.1103/PhysRevLett.129.111102"),
        ("Abac, A. G., et al. (LIGO Scientific, Virgo and KAGRA Collaborations) (2025). GW250114: Testing Hawking's area law and the Kerr nature of black holes. Physical Review Letters, 135, 111403.", "10.1103/kw5g-d732"),
    ],
}
