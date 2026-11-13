# -*- coding: utf-8 -*-
"""Time & Gravity · T.08 — A horizon has a temperature.

Instrument: a two-mode Rindler thermofield double on 16 Fock levels; tracing out the behind-the-horizon mode L
leaves the right wedge R in a Planck thermal state at the Unruh/Hawking temperature, checked with a pure-Python
Jacobi eigensolver, alongside Gauss-Legendre integration of dS = c^2 dM / T_H(M) = k_B A / (4 l_P^2).
Knockout / planted defect: severing cross-horizon entanglement (product state |0>_L x |0>_R) collapses the wedge
entropy to zero and fails the Planck spectrum check.
Verifier: skills/timegravity/t08/verify_t08_horizon_thermodynamics.py.
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t08"
CODE = "T.08"

PR60 = "T01-PR1960"
GPA80 = "T01-GPA1980"
PENZIAS = "T08-PENZIAS1965"
MATHER = "T08-MATHER1994"
BCH = "T08-BCH1973"
BEK = "T10-BEKENSTEIN1973"
H75 = "T10-HAWKING1975"
BW = "T08-BW1975"
UNRUH = "T08-UNRUH1976"
MUNOZ = "T08-MUNOZ2019"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "date": "2026-11-10",
    "order_label_en": "Step 9 of 14",
    "order_label_es": "Paso 9 de 14",
    "kicker_en": "Time & Gravity · T.08 · Where a causal boundary turns a pure vacuum into a thermal bath",
    "kicker_es": "Tiempo y Gravedad · T.08 · Donde una frontera causal convierte un vacío puro en un baño térmico",
    "title_en": "A Horizon Has a Temperature",
    "title_es": "Un Horizonte Tiene Temperatura",
    "standfirst_en": (
        "On T.07 a choice of clock split a stationary quantum state into an observer and a system. When acceleration or "
        "gravity makes that split geometric, a causal horizon hides half the vacuum modes from any clock that stays outside. "
        "Tracing out the hidden partner turns the pure vacuum into a Planck thermal state at the Unruh or Hawking temperature, "
        "and integrating the first law of black-hole mechanics fixes the horizon entropy at one quarter of its area in Planck units."
    ),
    "standfirst_es": (
        "En T.07 la elección de un reloj dividió un estado cuántico estacionario entre un observador y un sistema. Cuando la aceleración "
        "o la gravedad vuelve geométrica esa partición, un horizonte causal oculta la mitad de los modos del vacío a cualquier reloj que "
        "permanezca afuera. Trazar sobre el compañero oculto convierte el vacío puro en un estado térmico de Planck a la temperatura de Unruh "
        "o de Hawking, e integrar la primera ley de la mecánica de agujeros negros fija la entropía del horizonte en un cuarto de su área en unidades de Planck."
    ),
    "seo": (
        "A Horizon Has a Temperature: Rindler Wedges and Hawking's Quarter",
        "How tracing over modes behind a causal horizon turns a pure vacuum state into a Planck thermal bath and fixes black-hole entropy at A/4.",
        "Un Horizonte Tiene Temperatura: Cuñas de Rindler y el Cuarto de Hawking",
        "Cómo trazar sobre los modos detrás de un horizonte causal convierte un vacío puro en un baño térmico de Planck y fija la entropía en A/4.",
    ),
    "reading_time_en": "14 min read",
    "reading_time_es": "14 min de lectura",
    "central_number_en": "16-level Rindler wedge trace matches Planck weights within 1.7e-15 at ξ = 2.5; ∫ c² dM / T_H(M) matches k_B A / (4 ℓ_P²) within 2.5e-16; 1 M_☉ gives T_H = 61.7 nK and S_BH / k_B = 1.05e77",
    "central_number_es": "La traza de la cuña de Rindler de 16 niveles coincide con los pesos de Planck dentro de 1.7e-15 en ξ = 2.5; ∫ c² dM / T_H(M) coincide con k_B A / (4 ℓ_P²) dentro de 2.5e-16; 1 M_☉ da T_H = 61.7 nK y S_BH / k_B = 1.05e77",
    "verifier": "skills/timegravity/t08/verify_t08_horizon_thermodynamics.py",
    "generator": "skills/timegravity/t08/make_t08.py",
    "skill": "skills/timegravity/t08/SKILL.md",
    "skill_filename": "timegravity-t08-horizon-thermodynamics.SKILL.md",
    "open_question_en": "Does a real horizon have the hairless geometry that this thermodynamic law assumes?",
    "open_question_es": "¿Tiene un horizonte real la geometría sin pelo que esta ley termodinámica supone?",
    "ledger_ids": [PR60, GPA80, PENZIAS, MATHER, BCH, BEK, H75, BW, UNRUH, MUNOZ],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any measurement or derivation cited on this page. "
        "The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna medición o derivación citada en esta "
        "página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien mantiene el sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "horizon",
        "title_en": "Instrument · Tracing out the hidden wedge turns a pure vacuum into a Planck bath",
        "title_es": "Instrumento · Trazar sobre la cuña oculta convierte un vacío puro en un baño de Planck",
        "how_en": (
            "Left: the Rindler spacetime wedge (cT against X), with the causal horizon X = ±cT, the accelerated clock's hyperbola "
            "X² − c²T² = (c²/a)², and the paired mode partners straddling the horizon. Right: the occupation probabilities pₙ of the "
            "reduced state ρ_R = Tr_L(|Ψ⟩⟨Ψ|) on a 16-level Fock space against the Planck curve (1 − e^{−ξ})e^{−nξ}, alongside the "
            "Hawking temperature T_H and Bekenstein–Hawking entropy S_BH / k_B = A / (4 ℓ_P²) for the selected black-hole mass. "
            "The sliders set the Boltzmann exponent ξ = βħω and the black-hole mass M / M_☉. The knockout severs entanglement across "
            "the horizon (setting the squeezing to zero, |0_L⟩ ⊗ |0_R⟩): the thermal tail vanishes, S(ρ_R) drops to zero, and the "
            "verifier rejects the run. Keyboard: Tab and arrows. With reduced motion on, nothing animates."
        ),
        "how_es": (
            "Izquierda: la cuña espaciotemporal de Rindler (cT frente a X), con el horizonte causal X = ±cT, la hipérbola del reloj acelerado "
            "X² − c²T² = (c²/a)², y los modos emparejados a ambos lados del horizonte. Derecha: las probabilidades de ocupación pₙ del "
            "estado reducido ρ_R = Tr_L(|Ψ⟩⟨Ψ|) en un espacio de Fock de 16 niveles frente a la curva de Planck (1 − e^{−ξ})e^{−nξ}, junto "
            "con la temperatura de Hawking T_H y la entropía de Bekenstein y Hawking S_BH / k_B = A / (4 ℓ_P²) para la masa de agujero negro elegida. "
            "Los deslizadores fijan el exponente de Boltzmann ξ = βħω y la masa M / M_☉. El apagado corta el entrelazamiento a través del "
            "horizonte (poniendo el parámetro de compresión en cero, |0_L⟩ ⊗ |0_R⟩): la cola térmica desaparece, S(ρ_R) cae a cero y el "
            "verificador rechaza la corrida. Teclado: Tab y flechas. Con movimiento reducido, nada se anima."
        ),
    },
    "predict": {
        "q_en": "Before you check the readout: how does the Hawking temperature of a one-solar-mass black hole compare with the 2.725 K cosmic microwave background?",
        "q_es": "Antes de mirar la lectura: ¿cómo se compara la temperatura de Hawking de un agujero negro de una masa solar con el fondo cósmico de microondas de 2.725 K?",
        "options": [
            ("Much hotter, thousands of kelvin", "Mucho más caliente, miles de kelvin"),
            ("About the same, a few kelvin", "Más o menos igual, unos cuantos kelvin"),
            ("Forty million times colder, about 62 nanokelvin", "Cuarenta millones de veces más frío, unos 62 nanokelvin"),
        ],
        "answer": 2,
        "reveal_en": "About 61.7 nanokelvin: forty-four million times colder than the 2.725 K sky, so a stellar black hole absorbs far more radiation than it emits.",
        "reveal_es": "Unos 61.7 nanokelvin: cuarenta y cuatro millones de veces más frío que el cielo a 2.725 K, así que un agujero negro estelar absorbe mucha más radiación de la que emite.",
    },
    "sections": [
        {"type": "h2", "id": "measured", "en": "I · Two measured anchors: redshifted clocks and a Planck sky", "es": "I · Dos anclas medidas: relojes desplazados al rojo y un cielo de Planck", "short_en": "I · Measured", "short_es": "I · Medido"},
        P(
            C("MEASURED", [PR60, GPA80],
              "Clocks at different heights or accelerations tick at different rates, with fractional shift Δf/f = g Δz / c²: "
              "the 22.5-metre tower measurement of 1960 and the 10,000-kilometre suborbital hydrogen-maser flight of 1980 "
              "confirmed Einstein's gravitational redshift, to 10 percent in the tower and to 7×10⁻⁵ in the maser flight.",
              "Los relojes a distintas alturas o aceleraciones marcan el paso a ritmos distintos, con desplazamiento fraccionario Δf/f = g Δz / c²: "
              "la medición en la torre de 22.5 metros en 1960 y el vuelo suborbital del máser de hidrógeno a 10,000 kilómetros en 1980 "
              "confirmaron el corrimiento al rojo gravitacional de Einstein, al 10 por ciento en la torre y a 7×10⁻⁵ en el vuelo del máser."),
            T(" ", " "),
            C("MEASURED", [PENZIAS, MATHER],
              "And a thermal radiation bath follows Planck's Bose–Einstein occupation law n̄(ω) = 1/(e^{ħω/k_B T} − 1): "
              "discovered as an isotropic microwave background in 1965 and measured by COBE FIRAS in 1994 to match a 2.726 K "
              "Planck blackbody within 0.03 percent of peak brightness.",
              "Y un baño de radiación térmica sigue la ley de ocupación de Bose y Einstein de Planck n̄(ω) = 1/(e^{ħω/k_B T} − 1): "
              "descubierto como un fondo isótropo de microondas en 1965 y medido por COBE FIRAS en 1994 coincidiendo con un cuerpo negro "
              "de Planck a 2.726 K dentro del 0.03 por ciento del brillo máximo."),
            T(" What follows on this page is DERIVED from these two pieces of physics—proper-time redshift and quantum field theory—pushed to a causal horizon.",
              " Lo que sigue en esta página es DERIVADO a partir de estas dos piezas de la física —el corrimiento del tiempo propio y la teoría cuántica de campos— llevadas hasta un horizonte causal."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("Imagine two dancers holding hands across a curtain. Together they are completely still and orderly: if you see both, "
                 "there is zero randomness in their pose. Now draw the curtain so you are forbidden, by the speed of light itself, from ever "
                 "seeing the dancer on the left. Watching only the dancer on the right, every shared motion looks like random thermal jiggling.",
                 "Imagina a dos bailarines tomados de la mano a través de una cortina. Juntos están en perfecto orden: si ves a los dos, "
                 "hay cero aleatoriedad en su postura. Ahora cierra la cortina de modo que la velocidad de la luz misma te prohíba ver jamás "
                 "al bailarín de la izquierda. Mirando solo al bailarín de la derecha, cada movimiento compartido parece una agitación térmica aleatoria.")),
             P(T("A horizon is that curtain. A quantum vacuum is not empty; its field modes are entangled across every boundary in space. "
                 "When a rocket accelerates forever, or when a black hole forms, a horizon hides the inside partner of every pair. "
                 "To any clock outside, the half it can still see is a warm bath with a precise Planck temperature set by the steepness of the horizon.",
                 "Un horizonte es esa cortina. Un vacío cuántico no está vacío; sus modos de campo están entrelazados a través de cada frontera espacial. "
                 "Cuando un cohete acelera sin pausa, o cuando se forma un agujero negro, un horizonte oculta al compañero interior de cada par. "
                 "Para cualquier reloj afuera, la mitad que aún puede ver es un baño tibio con una temperatura de Planck precisa fijada por la pendiente del horizonte.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: a stereo recording where the left channel cancels the hiss of the right channel when heard together. "
                 "Unplug the left speaker and you hear pure thermal static from the right speaker alone, even though the master tape holds "
                 "a clean, noiseless signal.",
                 "Analogía cotidiana: una grabación estéreo donde el canal izquierdo cancela el siseo del canal derecho cuando se escuchan juntos. "
                 "Desconecta la bocina izquierda y oirás estática térmica pura en la bocina derecha sola, aunque la cinta maestra guarde una señal limpia y sin ruido.")),
             P(T("How the controls work in plain words: the first slider changes ξ = ħω / (k_B T), the ratio of mode energy to horizon temperature; "
                 "smaller ξ means a hotter horizon and a longer thermal tail across the Fock bars. The second slider sets a black hole's mass in solar "
                 "masses and updates its Hawking temperature and area entropy. The knockout unplugs the cross-horizon entanglement: both halves sit in "
                 "their separate ground states, the thermal bars collapse into n = 0, and the entropy drops to zero.",
                 "Cómo funcionan los controles en palabras sencillas: el primer deslizador cambia ξ = ħω / (k_B T), la razón entre la energía del modo "
                 "y la temperatura del horizonte; un ξ menor significa un horizonte más caliente y una cola térmica más larga en las barras de Fock. "
                 "El segundo deslizador fija la masa de un agujero negro en masas solares y actualiza su temperatura de Hawking y su entropía de área. "
                 "El apagado desconecta el entrelazamiento a través del horizonte: ambas mitades quedan en su estado base separado, las barras térmicas colapsan en n = 0 y la entropía cae a cero.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "derived", "en": "II · From Rindler wedges to Hawking's quarter", "es": "II · De las cuñas de Rindler al cuarto de Hawking", "short_en": "II · Derived", "short_es": "II · Derivado"},
        {"type": "equation", "text": "T_U = ħa / (2π k_B c),   T_H = ħc³ / (8π G M k_B),   S_BH = k_B c³ A / (4 G ħ) = k_B A / (4 ℓ_P²)"},
        P(
            C("DERIVED", [BW, UNRUH, PR60, MATHER],
              "A clock with uniform proper acceleration a follows the hyperbola X² − c²T² = (c²/a)², bounded by a causal horizon at X = ±cT "
              "where its proper-time rate dτ = (aξ/c²) dt vanishes; Bisognano and Wichmann proved in 1975 that the Minkowski vacuum restricted "
              "to the right Rindler wedge is a thermal state with respect to Lorentz boosts, and Unruh showed in 1976 that an accelerated detector "
              "responds as if immersed in a Planck bath at T_U = ħa / (2π k_B c).",
              "Un reloj con aceleración propia uniforme a sigue la hipérbola X² − c²T² = (c²/a)², acotada por un horizonte causal en X = ±cT "
              "donde su ritmo de tiempo propio dτ = (aξ/c²) dt se anula; Bisognano y Wichmann demostraron en 1975 que el vacío de Minkowski "
              "restringido a la cuña derecha de Rindler es un estado térmico respecto a los impulsos de Lorentz, y Unruh mostró en 1976 que un "
              "detector acelerado responde como si estuviera sumergido en un baño de Planck a T_U = ħa / (2π k_B c).",
              parent=PR60),
            T(" At 1g the Unruh temperature is 4.0×10⁻²⁰ K; reaching 1 K requires 2.5×10²⁰ m/s². On a 16-level Fock space per wedge at ξ = 2.5, "
              "the verifier embeds the partial trace ρ_R = Tr_L(|Ψ⟩⟨Ψ|) into a dense symmetric matrix, diagonalises it with the track's pure-Python "
              "Jacobi solver, and matches the Planck weights (1 − e^{−ξ})e^{−nξ} within 1.7×10⁻¹⁵.",
              " A 1g la temperatura de Unruh es 4.0×10⁻²⁰ K; alcanzar 1 K requiere 2.5×10²⁰ m/s². En un espacio de Fock de 16 niveles por cuña en ξ = 2.5, "
              "el verificador incrusta la traza parcial ρ_R = Tr_L(|Ψ⟩⟨Ψ|) en una matriz simétrica densa, la diagonaliza con el solver de Jacobi en Python "
              "puro de la serie, y coincide con los pesos de Planck (1 − e^{−ξ})e^{−nξ} dentro de 1.7×10⁻¹⁵."),
        ),
        P(
            C("DERIVED", [BCH, BEK, H75, MATHER],
              "Near a Schwarzschild horizon of radius r_s = 2GM/c² and area A = 4πr_s², the redshifted surface gravity κ = c⁴/(4GM) plays the role "
              "of proper acceleration: Hawking showed in 1975 that quantum fields on that geometry radiate thermally at T_H = ħκ / (2π k_B c) = "
              "ħc³ / (8π G M k_B), which combined with the 1973 Bardeen–Carter–Hawking first law d(Mc²) = (κc² / 8πG) dA fixes Bekenstein's "
              "horizon entropy coefficient at S_BH = k_B A / (4 ℓ_P²).",
              "Cerca de un horizonte de Schwarzschild de radio r_s = 2GM/c² y área A = 4πr_s², la gravedad superficial desplazada al rojo κ = c⁴/(4GM) "
              "desempeña el papel de la aceleración propia: Hawking mostró en 1975 que los campos cuánticos en esa geometría radian térmicamente a "
              "T_H = ħκ / (2π k_B c) = ħc³ / (8π G M k_B), lo cual combinado con la primera ley de Bardeen, Carter y Hawking de 1973 "
              "d(Mc²) = (κc² / 8πG) dA fija el coeficiente de la entropía de horizonte de Bekenstein en S_BH = k_B A / (4 ℓ_P²).",
              parent=MATHER),
            T(" Integrating d(S/k_B) = c² dM / (k_B T_H(M)) by Gauss–Legendre quadrature from 0 to 1 M_☉ reproduces A / (4 ℓ_P²) = 1.049×10⁷⁷ to "
              "2.5×10⁻¹⁶, with T_H = 61.7 nK.",
              " Integrar d(S/k_B) = c² dM / (k_B T_H(M)) por cuadratura de Gauss y Legendre de 0 a 1 M_☉ reproduce A / (4 ℓ_P²) = 1.049×10⁷⁷ con una "
              "precisión de 2.5×10⁻¹⁶, con T_H = 61.7 nK."),
        ),
        P(
            C("SINGLE RESULT", [MUNOZ],
              "In 2019 Muñoz de Nova, Golubkov, Kolobov and Steinhauer reported a thermal spectrum of spontaneous phonon pairs emitted across a "
              "sonic horizon in a rubidium Bose–Einstein condensate, at a temperature matching the acoustic surface gravity.",
              "En 2019 Muñoz de Nova, Golubkov, Kolobov y Steinhauer reportaron un espectro térmico de pares espontáneos de fonones emitidos a través "
              "de un horizonte sónico en un condensado de Bose y Einstein de rubidio, a una temperatura que coincide con la gravedad superficial acústica."),
            T(" This is a fluid-mechanics analogue, not a gravitational horizon: it tests Bogoliubov mode mixing across a sonic flow boundary, not "
              "Einstein's field equations or Bekenstein–Hawking area entropy, and stays SINGLE RESULT.",
              " Este es un análogo de mecánica de fluidos, no un horizonte gravitacional: pone a prueba la mezcla de modos de Bogoliubov a través de "
              "una frontera de flujo sónico, no las ecuaciones de campo de Einstein ni la entropía de área de Bekenstein y Hawking, y se mantiene como RESULTADO ÚNICO."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "open", "en": "III · What this page does not say", "es": "III · Lo que esta página no dice", "short_en": "III · Not said", "short_es": "III · No dicho"},
        P(
            C("OPEN", [H75, UNRUH],
              "Neither Hawking radiation from a gravitational black hole nor the thermal Unruh bath on a macroscopic accelerated thermometer has "
              "been directly measured: at one solar mass T_H ≈ 61.7 nK sits 4.4×10⁷ times below the 2.725 K cosmic microwave background, and "
              "what microstates of spacetime geometry are counted by A / (4 ℓ_P²) remains an open question.",
              "Ni la radiación de Hawking de un agujero negro gravitacional ni el baño térmico de Unruh en un termómetro macroscópico acelerado se "
              "han medido directamente: a una masa solar T_H ≈ 61.7 nK queda 4.4×10⁷ veces por debajo del fondo cósmico de microondas de 2.725 K, y "
              "qué microestados de la geometría del espaciotiempo cuenta A / (4 ℓ_P²) sigue siendo una pregunta abierta."),
            T(" While the radiation itself is far too cold to see in the sky, the classical horizon geometry and area law behind T_H and S_BH can be "
              "tested directly when two black holes collide and ring down—the subject of the next page.",
              " Aunque la radiación misma es demasiado fría para verse en el cielo, la geometría clásica del horizonte y la ley del área detrás de T_H "
              "y S_BH pueden ponerse a prueba directamente cuando dos agujeros negros chocan y resuenan, el tema de la siguiente página."),
        ),
        {"type": "change_box",
         "items": [
             ("An independent laboratory confirmation of spontaneous thermal emission across a horizon analogue in a second collaboration and platform would raise the analogue-kinematics claim from SINGLE RESULT to MEASURED, still fenced as fluid kinematics.",
              "Una confirmación de laboratorio independiente de emisión térmica espontánea a través de un horizonte análogo en una segunda colaboración y plataforma subiría la afirmación de cinemática análoga de RESULTADO ÚNICO a MEDIDO, aún acotada como cinemática de fluidos."),
             ("A direct measurement of the Unruh thermal response on an accelerated quantum detector with peer-reviewed replication would promote the detector response from DERIVED to MEASURED.",
              "Una medición directa de la respuesta térmica de Unruh en un detector cuántico acelerado con replicación revisada por pares promovería la respuesta del detector de DERIVADO a MEDIDO."),
             ("If the Jacobi eigenvalues of the reduced Rindler state ever differed from the truncated Gibbs weights by more than 1e-12, or if the Gauss–Legendre first-law integral missed A / (4 ℓ_P²), the verifier fails and the page does not build.",
              "Si los autovalores de Jacobi del estado reducido de Rindler llegaran a diferir de los pesos de Gibbs truncados por más de 1e-12, o si la integral de Gauss y Legendre de la primera ley fallara A / (4 ℓ_P²), el verificador falla y la página no se construye."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · Rindler hyperbola & redshift", "Etapa 1 · Hipérbola de Rindler y corrimiento al rojo",
         "A clock at constant proper acceleration a follows X(τ) = (c²/a) cosh(aτ/c), cT(τ) = (c²/a) sinh(aτ/c). Across 81 rapidity steps the kernel checks X² − c²T² = (c²/a)² and four-velocity normalisation to < 1e-15.",
         "Un reloj con aceleración propia constante a sigue X(τ) = (c²/a) cosh(aτ/c), cT(τ) = (c²/a) sinh(aτ/c). A lo largo de 81 pasos de rapidez el kernel comprueba X² − c²T² = (c²/a)² y la normalización de la cuadrivelocidad a < 1e-15."),
        ("Stage 2 · Two-mode squeezed state & partial trace", "Etapa 2 · Estado comprimido de dos modos y traza parcial",
         "|Ψ(ξ)⟩ = Z_d(ξ)^{−1/2} Σ_{n=0}^{15} e^{−nξ/2} |n_L⟩ ⊗ |n_R⟩ on 16×16 = 256 Fock states. Tracing out L gives ρ_R, which is rotated by an orthogonal DCT-II matrix into a dense 16×16 symmetric matrix and diagonalised with cyclic Jacobi.",
         "|Ψ(ξ)⟩ = Z_d(ξ)^{−1/2} Σ_{n=0}^{15} e^{−nξ/2} |n_L⟩ ⊗ |n_R⟩ en 16×16 = 256 estados de Fock. Trazar sobre L da ρ_R, que se rota mediante una matriz ortogonal DCT-II en una matriz simétrica densa de 16×16 y se diagonaliza con Jacobi cíclico."),
        ("Stage 3 · Planck check & first-law quadrature", "Etapa 3 · Comprobación de Planck y cuadratura de la primera ley",
         "At ξ = 2.5 (where truncation leakage e^{−16ξ} = 4.25e-18), Jacobi eigenvalues match (1 − e^{−ξ})e^{−nξ} within 1.7e-15; across ξ ∈ [0.5, 4.0] they match the exact truncated Gibbs weights within 4.1e-15. Five-point Gauss–Legendre quadrature of ∫ c² dM / T_H(M) matches k_B A / (4 ℓ_P²) within 2.5e-16.",
         "En ξ = 2.5 (donde la fuga por truncamiento es e^{−16ξ} = 4.25e-18), los autovalores de Jacobi coinciden con (1 − e^{−ξ})e^{−nξ} dentro de 1.7e-15; en ξ ∈ [0.5, 4.0] coinciden con los pesos de Gibbs truncados exactos dentro de 4.1e-15. La cuadratura de Gauss y Legendre de cinco puntos de ∫ c² dM / T_H(M) coincide con k_B A / (4 ℓ_P²) dentro de 2.5e-16."),
        ("Stage 4 · Planted defect knockout", "Etapa 4 · Apagado por defecto plantado",
         "Setting cross-horizon squeezing to zero replaces |Ψ(ξ)⟩ with the product state |0_L⟩ ⊗ |0_R⟩: S(ρ_R) collapses to 0 and the Planck spectrum check fails with deviation 0.082, rejecting the run.",
         "Poner en cero la compresión a través del horizonte reemplaza |Ψ(ξ)⟩ por el estado producto |0_L⟩ ⊗ |0_R⟩: S(ρ_R) colapsa a 0 y la comprobación del espectro de Planck falla con desviación 0.082, rechazando la corrida."),
    ],
    "sidenotes": [
        ("SIDENOTE T.08-A · FINITE FOCK CUTOFF VS INFINITE PLANCK TAIL", "NOTA T.08-A · CORTE FINITO DE FOCK FRENTE A LA COLA INFINITA DE PLANCK",
         "On d = 16 Fock levels, the truncated partition function differs from 1/(1 − e^{−ξ}) by e^{−dξ}. At ξ = 2.5 that tail is e^{−40} ≈ 4.25×10⁻¹⁸, well below double-precision tolerance; at hotter temperatures (ξ = 0.5) the verifier checks exact agreement with the truncated Gibbs distribution e^{−nξ}/Z_d(ξ).",
         "En d = 16 niveles de Fock, la función de partición truncada difiere de 1/(1 − e^{−ξ}) por e^{−dξ}. En ξ = 2.5 esa cola es e^{−40} ≈ 4.25×10⁻¹⁸, muy por debajo de la tolerancia de doble precisión; a temperaturas mayores (ξ = 0.5) el verificador comprueba el acuerdo exacto con la distribución de Gibbs truncada e^{−nξ}/Z_d(ξ)."),
        ("SIDENOTE T.08-B · WHY SONIC HORIZONS ARE AN ANALOGUE, NOT GRAVITY", "NOTA T.08-B · POR QUÉ LOS HORIZONTES SÓNICOS SON UN ANÁLOGO, NO GRAVEDAD",
         "A Bose–Einstein condensate where fluid flow exceeds the speed of sound traps phonons behind a sonic horizon and exhibits Bogoliubov mode mixing. That tests the kinematics of linear wave equations on a curved effective metric, not Einstein's equations or the Bekenstein–Hawking area law.",
         "Un condensado de Bose y Einstein donde el flujo del fluido supera la velocidad del sonido atrapa fonones detrás de un horizonte sónico y muestra mezcla de modos de Bogoliubov. Eso pone a prueba la cinemática de ecuaciones de onda lineales en una métrica efectiva curva, no las ecuaciones de Einstein ni la ley del área de Bekenstein y Hawking."),
    ],
    "sources": [
        ("Pound, R. V., & Rebka, G. A. (1960). Apparent weight of photons. Physical Review Letters, 4(7), 337–341.", "10.1103/PhysRevLett.4.337"),
        ("Vessot, R. F. C., et al. (1980). Test of relativistic gravitation with a space-borne hydrogen maser. Physical Review Letters, 45(26), 2081–2084.", "10.1103/PhysRevLett.45.2081"),
        ("Penzias, A. A., & Wilson, R. W. (1965). A measurement of excess antenna temperature at 4080 Mc/s. The Astrophysical Journal, 142, 419–421.", "10.1086/148307"),
        ("Mather, J. C., et al. (1994). Measurement of the cosmic microwave background spectrum by the COBE FIRAS instrument. The Astrophysical Journal, 420, 439–444.", "10.1086/173574"),
        ("Bardeen, J. M., Carter, B., & Hawking, S. W. (1973). The four laws of black hole mechanics. Communications in Mathematical Physics, 31(2), 161–170.", "10.1007/BF01645742"),
        ("Bekenstein, J. D. (1973). Black holes and entropy. Physical Review D, 7(8), 2333–2346.", "10.1103/PhysRevD.7.2333"),
        ("Hawking, S. W. (1975). Particle creation by black holes. Communications in Mathematical Physics, 43(3), 199–220.", "10.1007/BF02345020"),
        ("Bisognano, J. J., & Wichmann, E. H. (1975). On the duality condition for a Hermitian scalar field. Journal of Mathematical Physics, 16(4), 985–1007.", "10.1063/1.522605"),
        ("Unruh, W. G. (1976). Notes on black-hole evaporation. Physical Review D, 14(4), 870–892.", "10.1103/PhysRevD.14.870"),
        ("Muñoz de Nova, J. R., Golubkov, K., Kolobov, V. I., & Steinhauer, J. (2019). Observation of thermal Hawking radiation and its temperature in an analogue black hole. Nature, 569, 688–691.", "10.1038/s41586-019-1241-0"),
    ],
}
