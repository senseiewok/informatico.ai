# -*- coding: utf-8 -*-
"""Time & Gravity · T.04 — A clock in two places.

An experiment description, not a result: the Zych–Brukner clock interferometer. A clock in a superposition of two
heights loses interferometric visibility as its two proper times decohere; the instrument plots visibility against
height difference and clock frequency. Knockout: switch gravity off and the curve is flat. Planted defect: a clock
that never decoheres. No gravitational version has run; the page label is PROPOSED.
Verifier: skills/timegravity/t04/verify_t04_clock_visibility.py.
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t04"
CODE = "T.04"

ZYCH = "T04-ZYCH2011"
PR = "T01-PR1960"
MARG = "T04-MARGALIT2015"
PACZOS = "T04-PACZOS2025"
SORCI = "T04-SORCI2026"
GIAC = "T07-GIAC2019"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "date": "2026-11-09",
    "order_label_en": "Step 5 of 9",
    "order_label_es": "Paso 5 de 9",
    "kicker_en": "Time & Gravity · T.04 · An experiment description, page label PROPOSED",
    "kicker_es": "Tiempo y Gravedad · T.04 · La descripción de un experimento, etiqueta de página PROPUESTO",
    "title_en": "A Clock in Two Places",
    "title_es": "Un Reloj en Dos Lugares",
    "standfirst_en": (
        "Put a clock into a superposition of two heights and let it tick. The lower copy ages less. When the two copies are "
        "brought back together, the clock itself remembers which path it took, and the interference fades by exactly the overlap of "
        "its two readings. This is a proposal from 2011 that no laboratory has yet run with gravity; this page describes the "
        "experiment, computes the fade, and says what has and has not been done."
    ),
    "standfirst_es": (
        "Pon un reloj en una superposición de dos alturas y déjalo marchar. La copia de abajo envejece menos. Cuando las dos copias "
        "se vuelven a juntar, el reloj mismo recuerda qué camino tomó, y la interferencia se desvanece exactamente por el solape de sus "
        "dos lecturas. Es una propuesta de 2011 que ningún laboratorio ha corrido todavía con gravedad; esta página describe el "
        "experimento, calcula el desvanecimiento, y dice qué se ha hecho y qué no."
    ),
    "seo": (
        "A Clock in Two Places: the Clock Interferometer",
        "An experiment description: a clock in superposition of two heights loses interference visibility as its proper times decohere, with the formula recomputed live.",
        "Un Reloj en Dos Lugares: el Interferómetro de Reloj",
        "Descripción de un experimento: un reloj en superposición de dos alturas pierde visibilidad al decoherer sus tiempos propios, con la fórmula en vivo.",
    ),
    "reading_time_en": "12 min read",
    "reading_time_es": "12 min de lectura",
    "central_number_en": "V = |cos(ω Δτ/2)| with Δτ = g Δh T/c²: closed form equals the state overlap within 1e-12; a Sr clock 1 m apart for 1 s keeps V = 0.989; first zero at Δh·T = 10.7 m·s",
    "central_number_es": "V = |cos(ω Δτ/2)| con Δτ = g Δh T/c²: la forma cerrada iguala el solape de estados dentro de 1e-12; un reloj de Sr a 1 m durante 1 s conserva V = 0.989; primer cero en Δh·T = 10.7 m·s",
    "verifier": "skills/timegravity/t04/verify_t04_clock_visibility.py",
    "generator": "skills/timegravity/t04/make_t04.py",
    "skill": "skills/timegravity/t04/SKILL.md",
    "skill_filename": "timegravity-t04-clock-visibility.SKILL.md",
    "open_question_en": "Which time does the clock read?",
    "open_question_es": "¿Qué tiempo marca el reloj?",
    "ledger_ids": [ZYCH, PR, MARG, PACZOS, SORCI, GIAC],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any proposal, measurement or derivation cited on this page. "
        "The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna propuesta, medición o derivación citada en "
        "esta página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien mantiene el sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "zych",
        "title_en": "Instrument · Visibility of a clock in superposition of two heights",
        "title_es": "Instrumento · Visibilidad de un reloj en superposición de dos alturas",
        "how_en": (
            "Left: the two arms of the interferometer, one above the other by Δh, each with a clock face; the lower clock accumulates "
            "less proper time over the hold time T. Right: the interferometric visibility V = |cos(ω Δτ/2)| against Δh for the chosen T "
            "and clock frequency ω; the marker is the current setting. Sliders set Δh, T and log₁₀(ω/2π). The knockout switches gravity "
            "off (g → 0): no proper-time difference, no which-path information, V = 1 everywhere. The planted defect is a clock that never "
            "ticks (ω → 0), also V = 1 everywhere, which is why the verifier insists that the visibility reach zero for a real clock. "
            "Keyboard: Tab and arrows. With reduced motion on, nothing animates."
        ),
        "how_es": (
            "Izquierda: los dos brazos del interferómetro, uno sobre el otro a Δh, cada uno con una carátula de reloj; el reloj de abajo "
            "acumula menos tiempo propio durante el tiempo de espera T. Derecha: la visibilidad interferométrica V = |cos(ω Δτ/2)| frente a "
            "Δh para la T y la frecuencia de reloj ω elegidas; el marcador es el ajuste actual. Los deslizadores fijan Δh, T y log₁₀(ω/2π). El "
            "apagado quita la gravedad (g → 0): sin diferencia de tiempo propio, sin información de camino, V = 1 en todas partes. El defecto "
            "plantado es un reloj que nunca marcha (ω → 0), también V = 1 en todas partes, por eso el verificador insiste en que la "
            "visibilidad llegue a cero para un reloj real. Teclado: Tab y flechas. Con movimiento reducido, nada se anima."
        ),
    },
    "predict": {
        "q_en": "Before you move the sliders: an optical clock held 1 m above its other copy for 1 s. How much interference visibility is lost?",
        "q_es": "Antes de mover los deslizadores: un reloj óptico sostenido 1 m arriba de su otra copia durante 1 s. ¿Cuánta visibilidad de interferencia se pierde?",
        "options": [("About 1 percent", "Alrededor de 1 por ciento"), ("About half", "Alrededor de la mitad"), ("None at all", "Nada en absoluto")],
        "answer": 0,
        "reveal_en": "V = 0.989: about 1.1 percent, from a proper-time difference of 1.1 × 10⁻¹⁶ s read by a clock ticking at 429 THz. Ten metre-seconds kills it completely.",
        "reveal_es": "V = 0.989: alrededor de 1.1 por ciento, por una diferencia de tiempo propio de 1.1 × 10⁻¹⁶ s leída por un reloj que marcha a 429 THz. Diez metro-segundos la eliminan por completo.",
    },
    "sections": [
        {"type": "h2", "id": "proposal", "en": "I · The proposal, and the number it predicts", "es": "I · La propuesta, y el número que predice", "short_en": "I · Proposal", "short_es": "I · Propuesta"},
        P(
            C("DERIVED", [ZYCH, PR],
              "For a clock prepared in an equal superposition of its two internal levels and sent along two arms whose proper times differ "
              "by Δτ, the interferometric visibility is V = |cos(ω Δτ/2)|, where ω is the clock's transition frequency; in the weak field "
              "near Earth Δτ = g Δh T/c² for arms Δh apart held for a time T, the same clock-rate difference the redshift experiments measured.",
              "Para un reloj preparado en una superposición igual de sus dos niveles internos y enviado por dos brazos cuyos tiempos propios "
              "difieren en Δτ, la visibilidad interferométrica es V = |cos(ω Δτ/2)|, donde ω es la frecuencia de transición del reloj; en el "
              "campo débil cerca de la Tierra Δτ = g Δh T/c² para brazos separados Δh durante un tiempo T, la misma diferencia de ritmo de reloj que midieron los experimentos de corrimiento al rojo.",
              parent=PR),
            T(" The label is DERIVED: the formula follows from quantum mechanics plus the measured clock-rate gradient, and its parent "
              "MEASURED row is Pound and Rebka. What has not been measured is the visibility itself.",
              " La etiqueta es DERIVADO: la fórmula se sigue de la mecánica cuántica más el gradiente medido del ritmo de los relojes, y su fila madre MEDIDA es Pound y Rebka. Lo que no se ha medido es la visibilidad misma."),
        ),
        P(
            C("DERIVED", [ZYCH, PR],
              "For a strontium optical clock, ω/2π ≈ 429 THz, two arms 1 m apart held for 1 s differ in proper time by 1.1 × 10⁻¹⁶ s and the "
              "visibility drops to 0.989; the visibility first vanishes when Δh·T reaches π c²/(g ω) ≈ 10.7 m·s, for instance 1 m for 10.7 s.",
              "Para un reloj óptico de estroncio, ω/2π ≈ 429 THz, dos brazos separados 1 m durante 1 s difieren en tiempo propio por 1.1 × 10⁻¹⁶ s "
              "y la visibilidad baja a 0.989; la visibilidad se anula por primera vez cuando Δh·T llega a π c²/(g ω) ≈ 10.7 m·s, por ejemplo 1 m durante 10.7 s.",
              parent=PR),
            T(" The verifier computes the visibility twice, from the closed form and from the explicit overlap of the two clock states, and "
              "requires them to agree to one part in 10¹²; the instrument above uses the same two formulas.",
              " El verificador calcula la visibilidad dos veces, desde la forma cerrada y desde el solape explícito de los dos estados del reloj, "
              "y exige que coincidan a una parte en 10¹²; el instrumento de arriba usa las mismas dos fórmulas."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("Interference happens when two paths cannot be told apart. If something on one path marks it, even a little, the "
                 "interference weakens. A clock marks its own path: the copy that went higher ticked a little more. Bring the copies "
                 "together and the clock's own hands tell, faintly, which way it went. The fainter the difference, the stronger the "
                 "interference; the formula on this page is just that sentence written out.",
                 "La interferencia ocurre cuando dos caminos no pueden distinguirse. Si algo en un camino lo marca, aunque sea un poco, la "
                 "interferencia se debilita. Un reloj marca su propio camino: la copia que subió más marcó un poco más. Junta las copias y las "
                 "manecillas del reloj dicen, débilmente, por dónde fue. Mientras más débil la diferencia, más fuerte la interferencia; la "
                 "fórmula de esta página es solo esa frase escrita.")),
             P(T("Nobody has yet done this with gravity. The differences are tiny and the clocks that could read them are large and cold. "
                 "That is why the page carries the label PROPOSED, and why it describes an experiment instead of reporting one.",
                 "Nadie lo ha hecho todavía con gravedad. Las diferencias son diminutas y los relojes que podrían leerlas son grandes y fríos. "
                 "Por eso la página lleva la etiqueta PROPUESTO, y por eso describe un experimento en vez de reportar uno.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: two identical choirs walk around a building by different streets and meet at the back to sing the "
                 "same note. If one street is slightly longer, they arrive a beat apart and the chord blurs. Here the two streets are the "
                 "same length; what differs is how fast time passes on each, and the choir is one clock in two places.",
                 "Analogía cotidiana: dos coros idénticos rodean un edificio por calles distintas y se encuentran atrás para cantar la misma "
                 "nota. Si una calle es un poco más larga, llegan con un compás de diferencia y el acorde se emborrona. Aquí las dos calles miden "
                 "lo mismo; lo que difiere es qué tan rápido pasa el tiempo en cada una, y el coro es un solo reloj en dos lugares.")),
             P(T("How the controls work in plain words: the height slider separates the streets vertically; the hold-time slider makes the "
                 "walk longer; the frequency slider makes the choir sing a higher note, which blurs sooner. The knockout removes gravity, so "
                 "both streets keep the same time and the chord is perfect. The planted defect silences the choir, which also looks perfect, "
                 "and is why the verifier demands that a singing choir must be able to blur to nothing.",
                 "Cómo funcionan los controles en palabras sencillas: el deslizador de altura separa las calles verticalmente; el de tiempo de "
                 "espera alarga la caminata; el de frecuencia hace que el coro cante una nota más aguda, que se emborrona antes. El apagado quita "
                 "la gravedad, así que ambas calles llevan el mismo tiempo y el acorde es perfecto. El defecto plantado silencia al coro, lo que "
                 "también se ve perfecto, y por eso el verificador exige que un coro que canta pueda emborronarse hasta la nada.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "done", "en": "II · What has run, and what has only been proposed", "es": "II · Qué se ha corrido, y qué solo se ha propuesto", "short_en": "II · Done", "short_es": "II · Hecho"},
        P(
            C("SINGLE RESULT", [MARG],
              "In 2015 Margalit and colleagues ran a self-interfering clock: an atom in a superposition of two paths whose internal clock "
              "ticked at different rates on the two paths, with the rate difference produced by a magnetic field gradient, not by gravity; "
              "the interference visibility fell as the clock's which-path information grew and returned when the readings were realigned.",
              "En 2015 Margalit y colegas corrieron un reloj autointerferente: un átomo en superposición de dos caminos cuyo reloj interno marchaba "
              "a ritmos distintos en los dos caminos, con la diferencia de ritmo producida por un gradiente de campo magnético, no por gravedad; "
              "la visibilidad de interferencia cayó conforme creció la información de camino del reloj y regresó cuando las lecturas se realinearon."),
            T(" It is the mechanism of this page, demonstrated once, with a different cause for the rate difference; the row is SINGLE RESULT and the page says plainly that it was not gravity.",
              " Es el mecanismo de esta página, demostrado una vez, con otra causa para la diferencia de ritmo; la fila es RESULTADO ÚNICO y la página dice llanamente que no fue gravedad."),
        ),
        P(
            C("PROPOSED", [PACZOS, SORCI],
              "Two recent proposals aim at the gravitational version with the clocks that now exist: trapped-atom interferometers in which "
              "the clock's internal energy witnesses mass–energy equivalence through a visibility modulation and a resonance shift (2025), and "
              "'proper time interferometry' in optical ion clocks, where time dilation entangles the ion's motion with its clock state (2026).",
              "Dos propuestas recientes apuntan a la versión gravitatoria con los relojes que ya existen: interferómetros de átomos atrapados en "
              "los que la energía interna del reloj atestigua la equivalencia masa-energía mediante una modulación de visibilidad y un corrimiento "
              "de resonancia (2025), e 'interferometría de tiempo propio' en relojes ópticos de iones, donde la dilatación del tiempo entrelaza el "
              "movimiento del ion con su estado de reloj (2026)."),
            T(" Both are peer-reviewed proposals and neither has been realised; both rows are PROPOSED and both carry a review date inside the replication window.",
              " Ambas son propuestas revisadas por pares y ninguna se ha realizado; ambas filas son PROPUESTO y ambas llevan fecha de revisión dentro de la ventana de replicación."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "open", "en": "III · What this page does not say", "es": "III · Lo que esta página no dice", "short_en": "III · Not said", "short_es": "III · No dicho"},
        P(
            C("OPEN", [GIAC, ZYCH],
              "Which time the clock reads while it is in two places is not a question the formula answers: it gives the overlap of two "
              "readings, not a reading, and the frame in which a superposed clock has a time of its own is a live question in quantum reference frames.",
              "Qué tiempo marca el reloj mientras está en dos lugares no es una pregunta que la fórmula responda: da el solape de dos lecturas, no una "
              "lectura, y el marco en el que un reloj superpuesto tiene un tiempo propio es una pregunta viva en los marcos de referencia cuánticos."),
            T(" The page does not say the experiment will work, or that it would test quantum gravity if it did; it would test the overlap of "
              "quantum mechanics and the measured clock-rate gradient, nothing more and nothing less.",
              " La página no dice que el experimento funcionará, ni que probaría la gravedad cuántica si lo hiciera; probaría el solape de la mecánica cuántica y el gradiente medido del ritmo de los relojes, nada más y nada menos."),
        ),
        {"type": "change_box",
         "items": [
             ("A gravitational clock interferometer that measured the visibility fade would turn the page's DERIVED claims into measured ones and the page label from PROPOSED to SINGLE RESULT, then MEASURED after a second collaboration.",
              "Un interferómetro de reloj gravitatorio que midiera el desvanecimiento de la visibilidad convertiría las afirmaciones DERIVADAS de la página en medidas y la etiqueta de página de PROPUESTO a RESULTADO ÚNICO, y luego MEDIDO tras una segunda colaboración."),
             ("A measured visibility that did not follow |cos(ω Δτ/2)| would mean the clock, the proper-time difference or quantum mechanics behaves differently from this page; the page would be rewritten, not relabelled.",
              "Una visibilidad medida que no siguiera |cos(ω Δτ/2)| significaría que el reloj, la diferencia de tiempo propio o la mecánica cuántica se comportan distinto de esta página; la página se reescribiría, no se reetiquetaría."),
             ("Either 2025 or 2026 proposal being realised would move its row from PROPOSED to SINGLE RESULT.",
              "Que se realizara cualquiera de las propuestas de 2025 o 2026 movería su fila de PROPUESTO a RESULTADO ÚNICO."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · The proper-time difference", "Etapa 1 · La diferencia de tiempo propio",
         "Δτ = g Δh T/c² to first order in the weak field: the clock-rate gradient of T.01 integrated over the hold time T across a height difference Δh. For 1 m and 1 s this is 1.09 × 10⁻¹⁶ s.",
         "Δτ = g Δh T/c² a primer orden en el campo débil: el gradiente de ritmo de relojes de T.01 integrado sobre el tiempo de espera T a través de una diferencia de altura Δh. Para 1 m y 1 s esto es 1.09 × 10⁻¹⁶ s."),
        ("Stage 2 · The clock state on each arm", "Etapa 2 · El estado del reloj en cada brazo",
         "|ψ(τ)⟩ = (e^{−iωτ/2}|0⟩ + e^{+iωτ/2}|1⟩)/√2. The arms return the clock in |ψ(τ₁)⟩ and |ψ(τ₂)⟩ with τ₂ − τ₁ = Δτ.",
         "|ψ(τ)⟩ = (e^{−iωτ/2}|0⟩ + e^{+iωτ/2}|1⟩)/√2. Los brazos devuelven el reloj en |ψ(τ₁)⟩ y |ψ(τ₂)⟩ con τ₂ − τ₁ = Δτ."),
        ("Stage 3 · Visibility as overlap", "Etapa 3 · La visibilidad como solape",
         "V = |⟨ψ(τ₁)|ψ(τ₂)⟩| = |cos(ω Δτ/2)|. The verifier evaluates both sides on a grid of Δh and T and requires agreement within 1e-12; V(Δh = 0) = 1 exactly.",
         "V = |⟨ψ(τ₁)|ψ(τ₂)⟩| = |cos(ω Δτ/2)|. El verificador evalúa ambos lados en una malla de Δh y T y exige coincidencia dentro de 1e-12; V(Δh = 0) = 1 exactamente."),
        ("Stage 4 · The zero and the defect", "Etapa 4 · El cero y el defecto",
         "The first zero sits at ω g Δh T/c² = π, i.e. Δh·T = π c²/(g ω) ≈ 10.7 m·s for a Sr clock; the verifier requires V < 1e-6 there. The planted defect sets ω = 0: V ≡ 1, the zero never comes, and the check fails, as it must.",
         "El primer cero está en ω g Δh T/c² = π, es decir Δh·T = π c²/(g ω) ≈ 10.7 m·s para un reloj de Sr; el verificador exige V < 1e-6 ahí. El defecto plantado fija ω = 0: V ≡ 1, el cero nunca llega, y la prueba falla, como debe."),
    ],
    "sidenotes": [
        ("SIDENOTE T.04-A · WHY THE LABEL IS PROPOSED", "NOTA T.04-A · POR QUÉ LA ETIQUETA ES PROPUESTO",
         "The formula is derived and the ingredients are measured, but the visibility fade of a clock in a gravitational superposition has never been observed. A page that reports an experiment nobody has run is an experiment description, and the label says so.",
         "La fórmula está derivada y los ingredientes están medidos, pero el desvanecimiento de la visibilidad de un reloj en superposición gravitatoria nunca se ha observado. Una página que reporta un experimento que nadie ha corrido es la descripción de un experimento, y la etiqueta lo dice."),
        ("SIDENOTE T.04-B · TEN METRE-SECONDS", "NOTA T.04-B · DIEZ METRO-SEGUNDOS",
         "Δh·T is the whole budget: 10 m for 1 s or 1 m for 10 s give the same fade. Today's atom interferometers hold superpositions of metres for seconds, but not yet with an optical clock running inside them. That gap is the experiment.",
         "Δh·T es todo el presupuesto: 10 m durante 1 s o 1 m durante 10 s dan el mismo desvanecimiento. Los interferómetros atómicos de hoy sostienen superposiciones de metros durante segundos, pero todavía no con un reloj óptico marchando adentro. Esa brecha es el experimento."),
    ],
    "sources": [
        ("Zych, M., Costa, F., Pikovski, I., & Brukner, Č. (2011). Quantum interferometric visibility as a witness of general relativistic proper time. Nature Communications, 2, 505.", "10.1038/ncomms1498"),
        ("Pound, R. V., & Rebka, G. A. (1960). Apparent weight of photons. Physical Review Letters, 4(7), 337–341.", "10.1103/PhysRevLett.4.337"),
        ("Margalit, Y., et al. (2015). A self-interfering clock as a \"which path\" witness. Science, 349(6253), 1205–1208.", "10.1126/science.aac6498"),
        ("Paczos, J., Foo, J., & Zych, M. (2025). Witnessing mass-energy equivalence with trapped atom interferometers. Quantum, 9, 1827.", "10.22331/q-2025-08-08-1827"),
        ("Sorci, M., Foo, J., Leibfried, D., Sanner, C., & Pikovski, I. (2026). Quantum signatures of proper time in optical ion clocks. Physical Review Letters, 136, 163602.", "10.1103/qhj9-pc2b"),
        ("Giacomini, F., Castro-Ruiz, E., & Brukner, Č. (2019). Quantum mechanics and the covariance of physical laws in quantum reference frames. Nature Communications, 10, 494.", "10.1038/s41467-018-08155-0"),
    ],
}
