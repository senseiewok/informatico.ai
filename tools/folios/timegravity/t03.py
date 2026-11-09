# -*- coding: utf-8 -*-
"""Time & Gravity · T.03 — What sets the slope.

Instrument: the weak-field Einstein equation reduced to Poisson's equation, solved on a radial grid; a mass slider
reshapes the clock-rate map; two bodies of different composition fall together. Knockout: remove the source and
the map flattens, nothing falls. Planted defect: a composition-dependent fall (η ≠ 0).
Verifier: skills/timegravity/t03/verify_t03_poisson_equivalence.py.
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t03"
CODE = "T.03"

EIN16 = "T03-EIN1916"
MICRO = "T03-MICRO2022"
EOT = "T03-EOTWASH2008"
LLR = "T03-LLR2004"
ALPHA = "T03-ALPHAG2023"
WILL = "T03-WILL2014"
PR = "T01-PR1960"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "order_label_en": "Reading order 4 of 9",
    "order_label_es": "Orden de lectura 4 de 9",
    "kicker_en": "Time & Gravity · T.03 · The source side of the slope",
    "kicker_es": "Tiempo y Gravedad · T.03 · El lado de la fuente de la pendiente",
    "title_en": "What Sets the Slope",
    "title_es": "Qué Fija la Pendiente",
    "standfirst_en": (
        "On the previous page the slope in the rate of time was a number put in by hand. Here it has a source: mass-energy. In the "
        "weak field the Einstein equation reduces to Poisson's equation, the instrument solves it on a grid, and every body, whatever "
        "it is made of, reads the same map. That sameness has been measured to a part in a thousand trillion, and antimatter has been seen to fall once."
    ),
    "standfirst_es": (
        "En la página anterior la pendiente en el ritmo del tiempo era un número puesto a mano. Aquí tiene una fuente: la masa-energía. "
        "En el campo débil la ecuación de Einstein se reduce a la ecuación de Poisson, el instrumento la resuelve en una malla, y todo "
        "cuerpo, esté hecho de lo que sea, lee el mismo mapa. Esa igualdad se ha medido a una parte en mil billones, y la antimateria se ha visto caer una vez."
    ),
    "seo": (
        "What Sets the Slope: Poisson and the Equivalence Principle",
        "How the weak-field Einstein equation reduces to Poisson's equation on a grid, and how torsion balances, lunar ranging and a satellite show every composition falls alike.",
        "Qué Fija la Pendiente: Poisson y el Principio de Equivalencia",
        "Cómo la ecuación de Einstein en campo débil se reduce a la de Poisson en una malla, y cómo balanzas de torsión, el láser lunar y un satélite muestran que todo cae igual.",
    ),
    "reading_time_en": "13 min read",
    "reading_time_es": "13 min de lectura",
    "central_number_en": "Poisson on a 2,000-point grid recovers Φ = −GM/r outside an Earth-mass sphere within 2e-3 and Φ(0) = −3GM/2R; two compositions released together separate by < 1e-12 m",
    "central_number_es": "Poisson en una malla de 2,000 puntos recupera Φ = −GM/r fuera de una esfera de masa terrestre dentro de 2e-3 y Φ(0) = −3GM/2R; dos composiciones soltadas juntas se separan < 1e-12 m",
    "verifier": "skills/timegravity/t03/verify_t03_poisson_equivalence.py",
    "generator": "skills/timegravity/t03/make_t03.py",
    "skill": "skills/timegravity/t03/SKILL.md",
    "skill_filename": "timegravity-t03-poisson-equivalence.SKILL.md",
    "open_question_en": "What if the mass is in two places?",
    "open_question_es": "¿Y si la masa está en dos lugares?",
    "ledger_ids": [MICRO, EOT, LLR, ALPHA, EIN16, PR, WILL],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any measurement or derivation cited on this page. "
        "The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna medición o derivación citada en esta "
        "página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien mantiene el sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "poisson",
        "title_en": "Instrument · A mass shapes the clock-rate map, and two compositions read it alike",
        "title_es": "Instrumento · Una masa da forma al mapa de ritmo de relojes, y dos composiciones lo leen igual",
        "how_en": (
            "Left: a sphere of mass M and the potential Φ(r) around it, solved live on a radial grid from ∇²Φ = 4πGρ and drawn as the "
            "clock-rate map it is: darker rings mean slower clocks. The mass slider reshapes the map; the grid solution is compared "
            "with −GM/r outside the body on every change. Right: two bodies of different composition released together above the "
            "surface; with η = 0 they fall as one. The knockout removes the source: the map flattens and nothing falls, as on the "
            "previous page. The planted defect sets η = 10⁻³, an exaggerated composition-dependent fall, and the bodies separate; the "
            "verifier rejects it. Keyboard: Tab to a control, arrows to change it. With reduced motion on, the fall is drawn at once."
        ),
        "how_es": (
            "Izquierda: una esfera de masa M y el potencial Φ(r) a su alrededor, resuelto en vivo en una malla radial a partir de ∇²Φ = 4πGρ "
            "y dibujado como el mapa de ritmo de relojes que es: anillos más oscuros significan relojes más lentos. El deslizador de masa "
            "cambia el mapa; la solución en malla se compara con −GM/r fuera del cuerpo en cada cambio. Derecha: dos cuerpos de distinta "
            "composición soltados juntos sobre la superficie; con η = 0 caen como uno. El apagado quita la fuente: el mapa se aplana y nada "
            "cae, como en la página anterior. El defecto plantado fija η = 10⁻³, una caída dependiente de la composición exagerada, y los "
            "cuerpos se separan; el verificador lo rechaza. Teclado: Tab hasta un control y flechas para cambiarlo. Con movimiento reducido, la caída se dibuja de una vez."
        ),
    },
    "predict": {
        "q_en": "Before you press the planted defect: in the best measurement so far, how different are the falls of titanium and platinum?",
        "q_es": "Antes de pulsar el defecto plantado: en la mejor medición hasta ahora, ¿qué tan distintas son las caídas de titanio y platino?",
        "options": [("About one part in a thousand", "Como una parte en mil"), ("About one part in a million", "Como una parte en un millón"), ("Indistinguishable to one part in 10¹⁵", "Indistinguibles a una parte en 10¹⁵")],
        "answer": 2,
        "reveal_en": "MICROSCOPE 2022: η(Ti, Pt) = (−1.5 ± 2.3 ± 1.5) × 10⁻¹⁵, consistent with zero. The instrument's η = 10⁻³ is a trillion times larger, so that you can see it.",
        "reveal_es": "MICROSCOPE 2022: η(Ti, Pt) = (−1.5 ± 2.3 ± 1.5) × 10⁻¹⁵, consistente con cero. El η = 10⁻³ del instrumento es un billón de veces mayor, para que puedas verlo.",
    },
    "sections": [
        {"type": "h2", "id": "measured", "en": "I · Every composition falls alike, to a part in 10¹⁵", "es": "I · Toda composición cae igual, a una parte en 10¹⁵", "short_en": "I · Measured", "short_es": "I · Medido"},
        P(
            C("MEASURED", [MICRO, EOT, LLR],
              "Bodies of different composition fall with the same acceleration: the MICROSCOPE satellite found η(Ti, Pt) = (−1.5 ± 2.3 "
              "statistical ± 1.5 systematic) × 10⁻¹⁵ for titanium against platinum in 2022; the Eöt-Wash rotating torsion balance found "
              "η(Be, Ti) = (0.3 ± 1.8) × 10⁻¹³ in 2008; and lunar laser ranging finds the Earth and the Moon, which differ in composition and "
              "in gravitational self-energy, falling toward the Sun alike at the 10⁻¹³ level.",
              "Cuerpos de distinta composición caen con la misma aceleración: el satélite MICROSCOPE encontró η(Ti, Pt) = (−1.5 ± 2.3 "
              "estadística ± 1.5 sistemática) × 10⁻¹⁵ para titanio frente a platino en 2022; la balanza de torsión rotatoria de Eöt-Wash "
              "encontró η(Be, Ti) = (0.3 ± 1.8) × 10⁻¹³ en 2008; y el láser lunar encuentra que la Tierra y la Luna, que difieren en "
              "composición y en autoenergía gravitatoria, caen hacia el Sol por igual al nivel de 10⁻¹³."),
            T(" Three collaborations, three methods, in orbit, on a bench and across 384,000 km: that is why the claim may say MEASURED.",
              " Tres colaboraciones, tres métodos, en órbita, en una mesa y a lo largo de 384,000 km: por eso la afirmación puede decir MEDIDO."),
        ),
        P(
            C("SINGLE RESULT", [ALPHA],
              "Antimatter falls down: in 2023 the ALPHA collaboration released antihydrogen atoms in a vertical trap at CERN and measured a "
              "downward acceleration of (0.75 ± 0.13 statistical and systematic ± 0.16 simulation) g.",
              "La antimateria cae hacia abajo: en 2023 la colaboración ALPHA soltó átomos de antihidrógeno en una trampa vertical en el CERN y "
              "midió una aceleración hacia abajo de (0.75 ± 0.13 estadística y sistemática ± 0.16 de simulación) g."),
            T(" One collaboration, one apparatus, a result consistent with g at about one sigma: the row is SINGLE RESULT, and a reported "
              "internal repeat in 2024 does not change that, because an internal repeat is not an independent replication.",
              " Una colaboración, un aparato, un resultado consistente con g a cerca de una sigma: la fila es RESULTADO ÚNICO, y una repetición "
              "interna reportada en 2024 no cambia eso, porque una repetición interna no es una replicación independiente."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("The last page said: where time runs slower below than above, things drift downward. This page asks what makes time run "
                 "slower below. The answer is: mass. Put a planet somewhere and the clocks around it slow down, more the closer they are. "
                 "The instrument computes that slowing from the planet's mass, with the same equation Newton would have used, because in "
                 "weak gravity Einstein's equation becomes Newton's.",
                 "La página anterior decía: donde el tiempo corre más lento abajo que arriba, las cosas derivan hacia abajo. Esta página "
                 "pregunta qué hace que el tiempo corra más lento abajo. La respuesta es: la masa. Pon un planeta en algún lugar y los relojes "
                 "a su alrededor se frenan, más cuanto más cerca están. El instrumento calcula ese frenado a partir de la masa del planeta, con "
                 "la misma ecuación que Newton habría usado, porque en gravedad débil la ecuación de Einstein se vuelve la de Newton.")),
             P(T("And because what falls is the clock rate, not the object, a feather, a hammer and an atom of antihydrogen all read the "
                 "same map. Experiments have checked that to fifteen decimal places. Nobody has found a material that reads a different map.",
                 "Y como lo que cae es el ritmo del reloj, no el objeto, una pluma, un martillo y un átomo de antihidrógeno leen el mismo "
                 "mapa. Los experimentos lo han comprobado hasta quince decimales. Nadie ha encontrado un material que lea un mapa distinto.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: a heavy sleeper lies down on a trampoline and the fabric dips around them; the dip is deepest right "
                 "beside them and fades with distance. The dip is the clock-rate map, the sleeper is the mass, and the equation that gives "
                 "the shape of the dip from the weight is Poisson's. Roll a marble and a bowling ball across the fabric from the same spot "
                 "and they curve toward the sleeper along the same path, because the fabric does not ask what they are made of.",
                 "Analogía cotidiana: alguien pesado se acuesta en un trampolín y la tela se hunde a su alrededor; el hundimiento es más "
                 "profundo justo a su lado y se desvanece con la distancia. El hundimiento es el mapa de ritmo de relojes, quien duerme es la "
                 "masa, y la ecuación que da la forma del hundimiento a partir del peso es la de Poisson. Haz rodar una canica y una bola de "
                 "boliche por la tela desde el mismo punto y se curvan hacia quien duerme por el mismo camino, porque la tela no pregunta de qué están hechas.")),
             P(T("How the controls work in plain words: the mass slider is how heavy the sleeper is; the rings redraw and the surface "
                 "acceleration readout changes. The knockout lifts the sleeper off the trampoline: flat fabric, nothing rolls. The planted "
                 "defect is a trampoline that treats the marble and the bowling ball differently, which no experiment has ever seen; the "
                 "readout shows the separation such a fabric would produce after one second.",
                 "Cómo funcionan los controles en palabras sencillas: el deslizador de masa es qué tan pesado es quien duerme; los anillos se "
                 "redibujan y la lectura de aceleración en superficie cambia. El apagado levanta a quien duerme del trampolín: tela plana, nada "
                 "rueda. El defecto plantado es un trampolín que trata distinto a la canica y a la bola de boliche, algo que ningún experimento "
                 "ha visto jamás; la lectura muestra la separación que esa tela produciría tras un segundo.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "derived", "en": "II · From the field equation to Poisson, and why composition cannot enter", "es": "II · De la ecuación de campo a Poisson, y por qué la composición no puede entrar", "short_en": "II · Derived", "short_es": "II · Derivado"},
        {"type": "equation", "text": "g₀₀ ≈ −(1 + 2Φ/c²),   G₀₀ = (8πG/c⁴) T₀₀,   T₀₀ ≈ ρc²   ⇒   ∇²Φ = 4πGρ"},
        P(
            C("DERIVED", [EIN16, PR],
              "In the weak-field, slow-motion, static limit of the 1916 field equation, the time-time component of the metric is "
              "g₀₀ ≈ −(1 + 2Φ/c²) and the 00 component of the field equation becomes Poisson's equation ∇²Φ = 4πGρ; the slope A′(z) = 2g/c² "
              "that the previous page put in by hand is 2∇Φ/c², and its source is the mass-energy density on the right-hand side.",
              "En el límite de campo débil, movimiento lento y estático de la ecuación de campo de 1916, la componente tiempo-tiempo de la "
              "métrica es g₀₀ ≈ −(1 + 2Φ/c²) y la componente 00 de la ecuación de campo se vuelve la ecuación de Poisson ∇²Φ = 4πGρ; la "
              "pendiente A′(z) = 2g/c² que la página anterior puso a mano es 2∇Φ/c², y su fuente es la densidad de masa-energía del lado derecho.",
              parent=PR),
            T(" The parent MEASURED row is the redshift measurement that fixed the g₀₀ dependence on the potential; the derivation row is Einstein's 1916 paper. "
              "The instrument solves the equation on a 2,000-point radial grid for a uniform sphere and checks the result against −GM/r outside the body.",
              " La fila madre MEDIDA es la medición del corrimiento al rojo que fijó la dependencia de g₀₀ con el potencial; la fila de derivación es el "
              "artículo de Einstein de 1916. El instrumento resuelve la ecuación en una malla radial de 2,000 puntos para una esfera uniforme y comprueba el resultado contra −GM/r fuera del cuerpo."),
        ),
        P(
            C("DERIVED", [EIN16, EOT],
              "The geodesic equation contains no property of the falling body, no mass, charge or composition, so once the map Φ is fixed "
              "every body reads it alike; a composition-dependent fall, η ≠ 0, would mean the geodesic picture is wrong, which is what the "
              "equivalence-principle experiments test and what the verifier's planted defect imitates.",
              "La ecuación geodésica no contiene ninguna propiedad del cuerpo que cae, ni masa, carga o composición, así que una vez fijado el "
              "mapa Φ todo cuerpo lo lee igual; una caída dependiente de la composición, η ≠ 0, significaría que la imagen geodésica es "
              "incorrecta, que es lo que prueban los experimentos del principio de equivalencia y lo que imita el defecto plantado del verificador.",
              parent=EOT),
            T(" This is the page's knockout turned inside out: the previous page removed the gradient and nothing fell; this one removes the source and the gradient goes with it.",
              " Es el apagado de la página vuelto del revés: la página anterior quitó el gradiente y nada cayó; esta quita la fuente y el gradiente se va con ella."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "open", "en": "III · What this page does not say", "es": "III · Lo que esta página no dice", "short_en": "III · Not said", "short_es": "III · No dicho"},
        P(
            C("OPEN", [WILL],
              "What fixes the value of G, and whether the equivalence principle holds exactly or only to the 10⁻¹⁵ reached so far, are not "
              "questions the measurements answer; the field's standard survey lists them among the open tests, and every proposed violation remains a proposal.",
              "Qué fija el valor de G, y si el principio de equivalencia se cumple exactamente o solo hasta el 10⁻¹⁵ alcanzado hasta ahora, no "
              "son preguntas que las mediciones respondan; el panorama estándar del campo las lista entre las pruebas abiertas, y toda violación propuesta sigue siendo una propuesta."),
            T(" A 2026 result on the equivalence principle for quantum phases is not in the ledger because no DOI for it resolved when this page was built; the ledger admits rows, not headlines.",
              " Un resultado de 2026 sobre el principio de equivalencia para fases cuánticas no está en el libro de registro porque ningún DOI suyo resolvió cuando se construyó esta página; el libro admite filas, no titulares."),
        ),
        P(
            T("The page also does not say what happens when the source itself is in a quantum superposition, in two places at once. Poisson's "
              "equation takes a density; it has nothing to say about a mass that has no single position. That is the next page's question.",
              "La página tampoco dice qué pasa cuando la fuente misma está en una superposición cuántica, en dos lugares a la vez. La ecuación de "
              "Poisson toma una densidad; no tiene nada que decir sobre una masa que no tiene una sola posición. Esa es la pregunta de la siguiente página."),
        ),
        {"type": "change_box",
         "items": [
             ("A composition-dependent fall confirmed by two independent collaborations would make the first MEASURED claim false and withdraw both DERIVED claims; the page would be rewritten, not relabelled.",
              "Una caída dependiente de la composición confirmada por dos colaboraciones independientes haría falsa la primera afirmación MEDIDA y retiraría ambas afirmaciones DERIVADAS; la página se reescribiría, no se reetiquetaría."),
             ("An independent replication of the antihydrogen fall would raise the 2023 row from SINGLE RESULT to MEASURED.",
              "Una replicación independiente de la caída del antihidrógeno subiría la fila de 2023 de RESULTADO ÚNICO a MEDIDO."),
             ("A resolving DOI for the 2026 quantum-phase equivalence result would admit it to the ledger as SINGLE RESULT, inside the replication window.",
              "Un DOI que resuelva para el resultado de 2026 sobre equivalencia de fases cuánticas lo admitiría al libro de registro como RESULTADO ÚNICO, dentro de la ventana de replicación."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · The limit", "Etapa 1 · El límite",
         "Weak field (|Φ| ≪ c²), slow motion (v ≪ c), static source. Then g₀₀ ≈ −(1 + 2Φ/c²), T₀₀ ≈ ρc², and G₀₀ ≈ (2/c²)∇²Φ, so the 00 equation reads ∇²Φ = 4πGρ.",
         "Campo débil (|Φ| ≪ c²), movimiento lento (v ≪ c), fuente estática. Entonces g₀₀ ≈ −(1 + 2Φ/c²), T₀₀ ≈ ρc² y G₀₀ ≈ (2/c²)∇²Φ, así que la ecuación 00 se lee ∇²Φ = 4πGρ."),
        ("Stage 2 · The grid", "Etapa 2 · La malla",
         "Spherical symmetry: (1/r²) d/dr (r² dΦ/dr) = 4πGρ(r), discretised in conservative form on 2,000 cells out to 4R, with dΦ/dr = 0 at the centre and Φ = −GM/r_max at the edge, solved by the Thomas algorithm. The surface cell takes the volume-weighted density so no half-cell of mass is invented.",
         "Simetría esférica: (1/r²) d/dr (r² dΦ/dr) = 4πGρ(r), discretizada en forma conservativa en 2,000 celdas hasta 4R, con dΦ/dr = 0 en el centro y Φ = −GM/r_max en el borde, resuelta por el algoritmo de Thomas. La celda de superficie toma la densidad ponderada por volumen para no inventar media celda de masa."),
        ("Stage 3 · The checks", "Etapa 3 · Las pruebas",
         "Outside the body Φ must equal −GM/r within 2e-3 everywhere and the surface acceleration must equal GM/R² within 2e-3; at the centre Φ(0) must equal −3GM/2R. Two bodies released together with η = 0 must separate by less than 1e-12 m after one second.",
         "Fuera del cuerpo Φ debe ser igual a −GM/r dentro de 2e-3 en todas partes y la aceleración en superficie igual a GM/R² dentro de 2e-3; en el centro Φ(0) debe ser igual a −3GM/2R. Dos cuerpos soltados juntos con η = 0 deben separarse menos de 1e-12 m tras un segundo."),
        ("Stage 4 · The defect", "Etapa 4 · El defecto",
         "The planted defect sets the Eötvös parameter η = 2(a₁ − a₂)/(a₁ + a₂) to 10⁻³. The bodies then separate by about 4.9 mm in one second and the equivalence check fails, as it must, or the page does not build.",
         "El defecto plantado fija el parámetro de Eötvös η = 2(a₁ − a₂)/(a₁ + a₂) en 10⁻³. Los cuerpos se separan entonces unos 4.9 mm en un segundo y la prueba de equivalencia falla, como debe, o la página no se construye."),
    ],
    "sidenotes": [
        ("SIDENOTE T.03-A · WHY A GRID AND NOT A FORMULA", "NOTA T.03-A · POR QUÉ UNA MALLA Y NO UNA FÓRMULA",
         "The formula −GM/r is the answer; solving the equation on a grid and recovering it is the check. A verifier that only prints the formula is vacuously true. The grid can be wrong, which is exactly what makes passing it mean something.",
         "La fórmula −GM/r es la respuesta; resolver la ecuación en una malla y recuperarla es la prueba. Un verificador que solo imprime la fórmula es vacuamente verdadero. La malla puede estar mal, que es exactamente lo que hace que pasarla signifique algo."),
        ("SIDENOTE T.03-B · WHAT η MEANS", "NOTA T.03-B · QUÉ SIGNIFICA η",
         "η = 2(a₁ − a₂)/(a₁ + a₂) is the fractional difference in acceleration between two test bodies. Zero is the equivalence principle. The best bound is fifteen orders of magnitude below the instrument's exaggerated setting.",
         "η = 2(a₁ − a₂)/(a₁ + a₂) es la diferencia fraccional de aceleración entre dos cuerpos de prueba. Cero es el principio de equivalencia. La mejor cota está quince órdenes de magnitud por debajo del ajuste exagerado del instrumento."),
    ],
    "sources": [
        ("Touboul, P., et al. (MICROSCOPE Collaboration) (2022). MICROSCOPE mission: Final results of the test of the equivalence principle. Physical Review Letters, 129(12), 121102.", "10.1103/PhysRevLett.129.121102"),
        ("Schlamminger, S., Choi, K.-Y., Wagner, T. A., Gundlach, J. H., & Adelberger, E. G. (2008). Test of the equivalence principle using a rotating torsion balance. Physical Review Letters, 100(4), 041101.", "10.1103/PhysRevLett.100.041101"),
        ("Williams, J. G., Turyshev, S. G., & Boggs, D. H. (2004). Progress in lunar laser ranging tests of relativistic gravity. Physical Review Letters, 93(26), 261101.", "10.1103/PhysRevLett.93.261101"),
        ("Anderson, E. K., et al. (ALPHA Collaboration) (2023). Observation of the effect of gravity on the motion of antimatter. Nature, 621, 716–722.", "10.1038/s41586-023-06527-1"),
        ("Einstein, A. (1916). Die Grundlage der allgemeinen Relativitätstheorie. Annalen der Physik, 354(7), 769–822.", "10.1002/andp.19163540702"),
        ("Pound, R. V., & Rebka, G. A. (1960). Apparent weight of photons. Physical Review Letters, 4(7), 337–341.", "10.1103/PhysRevLett.4.337"),
        ("Will, C. M. (2014). The confrontation between general relativity and experiment. Living Reviews in Relativity, 17, 4.", "10.12942/lrr-2014-4"),
    ],
}
