# -*- coding: utf-8 -*-
"""Time & Gravity · T.07 — The equation with no time.

Instrument: a Page–Wootters history state on a 16-level clock and a qubit; the global state is stationary, and
conditioning on the clock's reading recovers Schrödinger evolution. Knockout: read the clock in a different basis
(a different split) and there is no time in it. Planted defect: a clock whose generator does not match the constraint.
Verifier: skills/timegravity/t07/verify_t07_page_wootters.py (closed form, pure-Python Jacobi eigensolver).
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t07"
CODE = "T.07"

RABI = "T07-RABI1938"
RAMSEY = "T07-RAMSEY1950"
HAHN = "T07-HAHN1950"
DEWITT = "T07-DEWITT1967"
PW = "T07-PW1983"
MOREVA = "T07-MOREVA2014"
GIAC = "T07-GIAC2019"
STOICA = "T07-STOICA2026"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "date": "2026-11-09",
    "order_label_en": "Step 8 of 14",
    "order_label_es": "Paso 8 de 14",
    "kicker_en": "Time & Gravity · T.07 · Where the 'felt now' has no variable",
    "kicker_es": "Tiempo y Gravedad · T.07 · Donde el 'ahora sentido' no tiene variable",
    "title_en": "The Equation with No Time",
    "title_es": "La Ecuación sin Tiempo",
    "standfirst_en": (
        "Canonical quantum gravity hands physics an equation with no time in it: Ĥ|Ψ⟩⟩ = 0. Page and Wootters showed how a "
        "clock inside the state can still read time: condition the stationary whole on the clock, and the rest evolves exactly "
        "as Schrödinger says. This page builds that toy on two small subsystems, checks it against the closed form, and shows "
        "that a different choice of clock gives a different time, or none."
    ),
    "standfirst_es": (
        "La gravedad cuántica canónica le entrega a la física una ecuación sin tiempo: Ĥ|Ψ⟩⟩ = 0. Page y Wootters mostraron cómo "
        "un reloj dentro del estado aún puede leer el tiempo: condiciona el todo estacionario al reloj, y el resto evoluciona "
        "exactamente como dice Schrödinger. Esta página construye ese juguete con dos subsistemas pequeños, lo comprueba contra "
        "la forma cerrada, y muestra que otra elección de reloj da otro tiempo, o ninguno."
    ),
    "seo": (
        "The Equation with No Time: a Page-Wootters Toy",
        "How a stationary quantum state with a clock inside recovers Schrodinger evolution when conditioned on the clock, checked with a pure-Python eigensolver.",
        "La Ecuación sin Tiempo: un Juguete de Page y Wootters",
        "Cómo un estado cuántico estacionario con un reloj adentro recupera la evolución de Schrodinger al condicionar sobre el reloj, comprobado con un solver propio.",
    ),
    "reading_time_en": "14 min read",
    "reading_time_es": "14 min de lectura",
    "central_number_en": "‖Ĥ|Ψ⟩⟩‖ ≈ 1e-15 on a 32-dimensional space; P(+x | tₙ) = cos²(ε tₙ/2) within 1e-10; the Jacobi kernel holds the state (projection 1.000)",
    "central_number_es": "‖Ĥ|Ψ⟩⟩‖ ≈ 1e-15 en un espacio de 32 dimensiones; P(+x | tₙ) = cos²(ε tₙ/2) dentro de 1e-10; el núcleo de Jacobi contiene el estado (proyección 1.000)",
    "verifier": "skills/timegravity/t07/verify_t07_page_wootters.py",
    "generator": "skills/timegravity/t07/make_t07.py",
    "skill": "skills/timegravity/t07/SKILL.md",
    "skill_filename": "timegravity-t07-page-wootters.SKILL.md",
    "open_question_en": "Whose clock?",
    "open_question_es": "¿El reloj de quién?",
    "ledger_ids": [RABI, RAMSEY, HAHN, DEWITT, PW, MOREVA, GIAC, STOICA],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any measurement or derivation cited on this page. "
        "The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna medición o derivación citada en esta "
        "página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien mantiene el sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "pw",
        "title_en": "Instrument · A stationary whole, and a clock inside it that still reads time",
        "title_es": "Instrumento · Un todo estacionario, y un reloj adentro que aún lee el tiempo",
        "how_en": (
            "Left: the global state |Ψ⟩⟩ as a grid, one row per clock reading tₙ, two columns for the qubit's |+x⟩ and |−x⟩ parts; "
            "darker means more weight. Nothing in this grid changes: the state is stationary, Ĥ|Ψ⟩⟩ = 0, and the residual is shown "
            "in the readout. Right: what the qubit looks like given each clock reading, P(+x | tₙ), against the closed-form Schrödinger "
            "curve cos²(ε tₙ/2). The slider picks a reading. The knockout reads the clock in its energy basis instead: a different "
            "split of the same state, and the curve goes flat at 1/2, no time at all. The planted defect bends the clock's spectrum so "
            "its generator no longer matches the constraint; the residual leaves zero and the verifier rejects the run. Keyboard: Tab "
            "and arrows. With reduced motion on, nothing animates."
        ),
        "how_es": (
            "Izquierda: el estado global |Ψ⟩⟩ como una cuadrícula, una fila por lectura del reloj tₙ, dos columnas para las partes |+x⟩ "
            "y |−x⟩ del qubit; más oscuro significa más peso. Nada en esta cuadrícula cambia: el estado es estacionario, Ĥ|Ψ⟩⟩ = 0, y el "
            "residuo se muestra en la lectura. Derecha: cómo se ve el qubit dada cada lectura del reloj, P(+x | tₙ), frente a la curva "
            "cerrada de Schrödinger cos²(ε tₙ/2). El deslizador elige una lectura. El apagado lee el reloj en su base de energía: otra "
            "partición del mismo estado, y la curva queda plana en 1/2, sin tiempo alguno. El defecto plantado dobla el espectro del reloj "
            "para que su generador ya no coincida con la restricción; el residuo deja de ser cero y el verificador rechaza la corrida. "
            "Teclado: Tab y flechas. Con movimiento reducido, nada se anima."
        ),
    },
    "predict": {
        "q_en": "Before you press the knockout: if you read the clock in its energy basis instead of its time basis, what does the qubit do?",
        "q_es": "Antes de pulsar el apagado: si lees el reloj en su base de energía en vez de su base de tiempo, ¿qué hace el qubit?",
        "options": [("The same cos² motion", "El mismo movimiento cos²"), ("Nothing: a flat 1/2 for every reading", "Nada: un 1/2 plano para cada lectura"), ("It runs backward", "Corre hacia atrás")],
        "answer": 1,
        "reveal_en": "In the energy split every conditional state is an energy eigenstate: P(+x) = 1/2 for each reading. Same state, different clock, no time.",
        "reveal_es": "En la partición de energía cada estado condicional es un autoestado de energía: P(+x) = 1/2 para cada lectura. Mismo estado, otro reloj, ningún tiempo.",
    },
    "sections": [
        {"type": "h2", "id": "measured", "en": "I · What a two-level system does, measured since 1938", "es": "I · Lo que hace un sistema de dos niveles, medido desde 1938", "short_en": "I · Measured", "short_es": "I · Medido"},
        P(
            C("MEASURED", [RABI, RAMSEY, HAHN],
              "A two-level quantum system evolves in time as Schrödinger's equation says: the molecular-beam resonance of 1938 drove it "
              "at its Bohr frequency, the separated oscillatory fields of 1950 read the phase it accumulated between two interaction zones, "
              "and the spin echoes of the same year refocused its free precession with a single pulse.",
              "Un sistema cuántico de dos niveles evoluciona en el tiempo como dice la ecuación de Schrödinger: la resonancia de haz molecular "
              "de 1938 lo excitó a su frecuencia de Bohr, los campos oscilatorios separados de 1950 leyeron la fase que acumuló entre dos zonas "
              "de interacción, y los ecos de espín del mismo año reenfocaron su precesión libre con un solo pulso."),
            T(" Three collaborations, three methods, one equation of motion. Everything on this page that is DERIVED derives from this; "
              "the toy below must reproduce exactly that evolution or it is wrong.",
              " Tres colaboraciones, tres métodos, una ecuación de movimiento. Todo lo DERIVADO en esta página se deriva de esto; el "
              "juguete de abajo debe reproducir exactamente esa evolución o está mal."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("Imagine a photograph of a whole room, with a wall clock in it and a pendulum swinging. The photograph does not change. "
                 "Yet if you look at the part of the photograph where the clock says one o'clock, the pendulum is here; where the clock says "
                 "two, the pendulum is there. The photograph has no time in it, and still, relative to the clock, the pendulum moves. "
                 "That is the whole idea of this page.",
                 "Imagina una fotografía de todo un cuarto, con un reloj de pared y un péndulo oscilando. La fotografía no cambia. Y aun así, "
                 "si miras la parte de la fotografía donde el reloj marca la una, el péndulo está aquí; donde marca las dos, el péndulo está "
                 "allá. La fotografía no tiene tiempo adentro, y aun así, respecto al reloj, el péndulo se mueve. Esa es toda la idea de esta página.")),
             P(T("Now imagine you decided to use the pendulum as the clock and the wall clock as the thing being watched. The story is "
                 "different. And if you chose to read the wall clock by its color instead of its hands, nothing in the photograph would move at "
                 "all. Which part is the clock is a choice, and that choice is where the open question lives.",
                 "Ahora imagina que decides usar el péndulo como reloj y el reloj de pared como lo observado. La historia es distinta. Y si "
                 "eligieras leer el reloj de pared por su color en vez de por sus manecillas, nada en la fotografía se movería. Qué parte es el "
                 "reloj es una elección, y en esa elección vive la pregunta abierta.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: a long film strip laid flat on a table. Every frame is already there; the strip does not move. 'Time' "
                 "is the frame number printed in the corner. Pick a frame number and you see where the actors stand; walk along the strip and "
                 "they act out the story. Sort the frames by brightness instead of by number and the story is gone, though not one frame changed.",
                 "Analogía cotidiana: una tira de película extendida sobre una mesa. Cada fotograma ya está ahí; la tira no se mueve. El "
                 "'tiempo' es el número de fotograma impreso en la esquina. Elige un número y ves dónde están los actores; recorre la tira y "
                 "actúan la historia. Ordena los fotogramas por brillo en vez de por número y la historia desaparece, aunque ni un fotograma cambió.")),
             P(T("How the controls work in plain words: the slider is the frame number, the clock reading. The knockout sorts the frames by "
                 "a different label, the clock's energy, and the right-hand plot goes flat: no story. The planted defect prints the frame "
                 "numbers in the wrong order, so the strip no longer matches the rule that generated it; the residual readout catches that.",
                 "Cómo funcionan los controles en palabras sencillas: el deslizador es el número de fotograma, la lectura del reloj. El apagado "
                 "ordena los fotogramas por otra etiqueta, la energía del reloj, y la gráfica de la derecha queda plana: sin historia. El defecto "
                 "plantado imprime los números en el orden equivocado, así que la tira ya no obedece la regla que la generó; la lectura del residuo lo detecta.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "derived", "en": "II · From the constraint to a clock that reads time", "es": "II · De la restricción a un reloj que lee el tiempo", "short_en": "II · Derived", "short_es": "II · Derivado"},
        {"type": "equation", "text": "Ĥ|Ψ⟩⟩ = 0,   Ĥ = Ĥ_C ⊗ 1 + 1 ⊗ Ĥ_S,   |Ψ⟩⟩ = (1/√d) Σₙ |tₙ⟩ ⊗ e^{−iĤ_S tₙ}|ψ(0)⟩"},
        P(
            C("DERIVED", [DEWITT, RABI],
              "In the canonical formulation of general relativity the Hamiltonian is a constraint: physical states satisfy Ĥ|Ψ⟩⟩ = 0, "
              "so the state of the whole does not evolve and no external time parameter appears in the equation.",
              "En la formulación canónica de la relatividad general el hamiltoniano es una restricción: los estados físicos satisfacen "
              "Ĥ|Ψ⟩⟩ = 0, así que el estado del todo no evoluciona y ningún parámetro externo de tiempo aparece en la ecuación.",
              parent=RABI),
            T(" The toy on this page is not gravity; it keeps only that structure: a constraint, a whole with no outside, and two parts.",
              " El juguete de esta página no es gravedad; conserva solo esa estructura: una restricción, un todo sin afuera, y dos partes."),
        ),
        P(
            C("DERIVED", [PW, RABI],
              "Page and Wootters showed that if the whole contains a clock subsystem, conditioning the stationary state on the clock reading "
              "tₙ leaves the rest in e^{−iĤ_S tₙ}|ψ(0)⟩: ordinary Schrödinger evolution, recovered from a state that never changes; the "
              "verifier builds this on a 16-level cyclic clock and a qubit and finds P(+x | tₙ) = cos²(ε tₙ/2) to one part in 10¹⁰ while ‖Ĥ|Ψ⟩⟩‖ stays at 10⁻¹⁵.",
              "Page y Wootters mostraron que si el todo contiene un subsistema reloj, condicionar el estado estacionario a la lectura del "
              "reloj tₙ deja al resto en e^{−iĤ_S tₙ}|ψ(0)⟩: evolución ordinaria de Schrödinger, recuperada de un estado que nunca cambia; el "
              "verificador construye esto con un reloj cíclico de 16 niveles y un qubit y encuentra P(+x | tₙ) = cos²(ε tₙ/2) a una parte en 10¹⁰ mientras ‖Ĥ|Ψ⟩⟩‖ se queda en 10⁻¹⁵.",
              parent=RABI),
            T(" The check is against the closed form, not against a simulation of itself: the cos² is the two-level evolution the first "
              "claim on this page calls MEASURED.",
              " La comprobación es contra la forma cerrada, no contra una simulación de sí misma: el cos² es la evolución de dos niveles que la primera afirmación de esta página llama MEDIDA."),
        ),
        P(
            C("DERIVED", [GIAC, PW, RABI],
              "Which subsystem is the clock, and in which basis it is read, is a choice of reference frame: read the same state in the "
              "clock's energy basis and every conditional state is an energy eigenstate with P(+x) = 1/2, no evolution at all; quantum "
              "reference frames make this frame dependence explicit, with physical laws covariant under the change of frame.",
              "Qué subsistema es el reloj, y en qué base se lee, es una elección de marco de referencia: lee el mismo estado en la base de "
              "energía del reloj y cada estado condicional es un autoestado de energía con P(+x) = 1/2, sin evolución alguna; los marcos de "
              "referencia cuánticos hacen explícita esta dependencia del marco, con leyes físicas covariantes bajo el cambio de marco.",
              parent=RABI),
            T(" That is the knockout: a different split gives a different time, and this split gives none.",
              " Ese es el apagado: otra partición da otro tiempo, y esta partición no da ninguno."),
        ),
        P(
            C("SINGLE RESULT", [MOREVA],
              "In 2014 Moreva and colleagues illustrated the construction with photons: the polarisation of one photon served as the clock, "
              "and the second photon's conditional state showed evolution while the pair as a whole was stationary.",
              "En 2014 Moreva y colegas ilustraron la construcción con fotones: la polarización de un fotón sirvió de reloj, y el estado "
              "condicional del segundo fotón mostró evolución mientras el par como un todo era estacionario."),
            T(" This page knows of no later independent realisation, so the row is SINGLE RESULT; it is an illustration of the mathematics, not a test of quantum gravity.",
              " Esta página no conoce una realización independiente posterior, así que la fila es RESULTADO ÚNICO; es una ilustración de la matemática, no una prueba de gravedad cuántica."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "open", "en": "III · What this page does not say", "es": "III · Lo que esta página no dice", "short_en": "III · Not said", "short_es": "III · No dicho"},
        P(
            C("PROPOSED", [STOICA],
              "A 2026 preprint argues that the conditional construction still carries a preferred-time problem: the choice of clock and "
              "basis that makes the recovered evolution look like ordinary physics is not fixed by the constraint itself.",
              "Una prepublicación de 2026 sostiene que la construcción condicional aún arrastra un problema de tiempo preferido: la elección "
              "de reloj y de base que hace que la evolución recuperada parezca física ordinaria no la fija la restricción misma."),
            T(" A preprint cannot rise above PROPOSED here, whatever its merits; the ledger row carries a review date for when peer review lands.",
              " Una prepublicación no puede subir de PROPUESTO aquí, sean cuales sean sus méritos; la fila del libro de registro lleva una fecha de revisión para cuando llegue la revisión por pares."),
        ),
        P(
            C("OPEN", [GIAC, PW],
              "Whose clock the universe keeps, if any subsystem's, is not settled: the construction recovers a time for every choice of "
              "clock, and nothing in the constraint picks one.",
              "Qué reloj lleva el universo, si es el de algún subsistema, no está resuelto: la construcción recupera un tiempo para cada "
              "elección de reloj, y nada en la restricción escoge uno."),
            T(" The 'felt now' that the hub stated as a question is absent here too: the toy has readings, not a present. That absence is the "
              "page's honest result, and the next page asks what happens when acceleration or gravity turns the split between clock and rest into a causal horizon.",
              " El 'ahora sentido' que el punto de partida planteó como pregunta también está ausente aquí: el juguete tiene lecturas, no un "
              "presente. Esa ausencia es el resultado honesto de la página, y la siguiente pregunta qué pasa cuando la aceleración o la gravedad convierte la partición entre el reloj y el resto en un horizonte causal."),
        ),
        {"type": "change_box",
         "items": [
             ("A second independent realisation of a Page–Wootters clock would raise the 2014 row from SINGLE RESULT to MEASURED.",
              "Una segunda realización independiente de un reloj de Page y Wootters subiría la fila de 2014 de RESULTADO ÚNICO a MEDIDO."),
             ("Peer-reviewed publication of the 2026 preferred-time argument would move its row to peer-reviewed and let the OPEN claim name it as a reviewed objection.",
              "La publicación revisada por pares del argumento de 2026 sobre el tiempo preferido movería su fila a revisada por pares y permitiría que la afirmación ABIERTA la nombre como objeción revisada."),
             ("If the toy's conditional probabilities ever differed from cos²(εt/2) by more than 1e-10 after a code change, the verifier fails and the page does not build.",
              "Si las probabilidades condicionales del juguete llegaran a diferir de cos²(εt/2) por más de 1e-10 tras un cambio de código, el verificador falla y la página no se construye."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · The constraint", "Etapa 1 · La restricción",
         "Ĥ = Ĥ_C ⊗ 1 + 1 ⊗ Ĥ_S on a 16-level clock and a qubit, 32 dimensions in all. Clock energies Eₘ = 2πm/d, m = −8…7; qubit Ĥ_S = (ε/2)σ_z with ε/2 = 2π/d, so both qubit energies sit on the clock lattice and a zero-energy state can exist.",
         "Ĥ = Ĥ_C ⊗ 1 + 1 ⊗ Ĥ_S en un reloj de 16 niveles y un qubit, 32 dimensiones en total. Energías del reloj Eₘ = 2πm/d, m = −8…7; qubit Ĥ_S = (ε/2)σ_z con ε/2 = 2π/d, así que ambas energías del qubit caen en la red del reloj y puede existir un estado de energía cero."),
        ("Stage 2 · The history state", "Etapa 2 · El estado historia",
         "|Ψ⟩⟩ = (1/√d) Σₙ |tₙ⟩ ⊗ e^{−iĤ_S tₙ}|+x⟩ with Pegg–Barnett time states |tₙ⟩ = (1/√d) Σₘ e^{−iEₘtₙ}|Eₘ⟩. Each clock-energy component pairs with the qubit energy that cancels it, so Ĥ|Ψ⟩⟩ = 0 exactly; the verifier reports the residual.",
         "|Ψ⟩⟩ = (1/√d) Σₙ |tₙ⟩ ⊗ e^{−iĤ_S tₙ}|+x⟩ con estados de tiempo de Pegg y Barnett |tₙ⟩ = (1/√d) Σₘ e^{−iEₘtₙ}|Eₘ⟩. Cada componente de energía del reloj se empareja con la energía del qubit que la cancela, así que Ĥ|Ψ⟩⟩ = 0 exactamente; el verificador reporta el residuo."),
        ("Stage 3 · Conditioning and the other split", "Etapa 3 · Condicionar y la otra partición",
         "Project onto |tₙ⟩ and normalise: the qubit is in e^{−iĤ_S tₙ}|+x⟩ and P(+x | tₙ) = cos²(ε tₙ/2), the closed form. Project onto |Eₘ⟩ instead and the qubit is an energy eigenstate: P(+x) = 1/2 for every m, no evolution.",
         "Proyecta sobre |tₙ⟩ y normaliza: el qubit está en e^{−iĤ_S tₙ}|+x⟩ y P(+x | tₙ) = cos²(ε tₙ/2), la forma cerrada. Proyecta sobre |Eₘ⟩ y el qubit es un autoestado de energía: P(+x) = 1/2 para cada m, sin evolución."),
        ("Stage 4 · Eigensolver and defect", "Etapa 4 · Solver de autovalores y defecto",
         "Ĥ is written in the time ⊗ σ_x basis, a dense 32×32 Hermitian matrix, embedded as a real symmetric 64×64 matrix and diagonalised with a cyclic Jacobi sweep in pure Python. The zero-eigenvalue subspace has dimension 2 and holds the state with projection 1. The planted defect bends the clock spectrum to m·|m|; the residual rises to about 13 and the check fails, as it must.",
         "Ĥ se escribe en la base tiempo ⊗ σ_x, una matriz hermítica densa de 32×32, se incrusta como matriz real simétrica de 64×64 y se diagonaliza con barridos cíclicos de Jacobi en Python puro. El subespacio de autovalor cero tiene dimensión 2 y contiene al estado con proyección 1. El defecto plantado dobla el espectro del reloj a m·|m|; el residuo sube a unos 13 y la prueba falla, como debe."),
    ],
    "sidenotes": [
        ("SIDENOTE T.07-A · WHY THE CLOSED FORM, NOT A SIMULATION", "NOTA T.07-A · POR QUÉ LA FORMA CERRADA, NO UNA SIMULACIÓN",
         "A verifier that compares a simulation with another run of itself proves only that the code is deterministic. cos²(εt/2) is what the 1938 and 1950 experiments measured for a two-level system; matching it is the only check that means something.",
         "Un verificador que compara una simulación con otra corrida de sí misma demuestra solo que el código es determinista. cos²(εt/2) es lo que los experimentos de 1938 y 1950 midieron para un sistema de dos niveles; coincidir con eso es la única comprobación que significa algo."),
        ("SIDENOTE T.07-B · WHAT THE TOY IS NOT", "NOTA T.07-B · LO QUE EL JUGUETE NO ES",
         "Two subsystems and a constraint. No metric, no gravity, no horizon. It shows how a timeless equation can hold a clock, and that which clock is a choice. Everything beyond that on this subject is labelled OPEN.",
         "Dos subsistemas y una restricción. Sin métrica, sin gravedad, sin horizonte. Muestra cómo una ecuación sin tiempo puede contener un reloj, y que qué reloj es una elección. Todo lo demás sobre este tema lleva la etiqueta ABIERTO."),
    ],
    "sources": [
        ("Rabi, I. I., Zacharias, J. R., Millman, S., & Kusch, P. (1938). A new method of measuring nuclear magnetic moment. Physical Review, 53(4), 318.", "10.1103/PhysRev.53.318"),
        ("Ramsey, N. F. (1950). A molecular beam resonance method with separated oscillating fields. Physical Review, 78(6), 695–699.", "10.1103/PhysRev.78.695"),
        ("Hahn, E. L. (1950). Spin echoes. Physical Review, 80(4), 580–594.", "10.1103/PhysRev.80.580"),
        ("DeWitt, B. S. (1967). Quantum theory of gravity. I. The canonical theory. Physical Review, 160(5), 1113–1148.", "10.1103/PhysRev.160.1113"),
        ("Page, D. N., & Wootters, W. K. (1983). Evolution without evolution: Dynamics described by stationary observables. Physical Review D, 27(12), 2885–2892.", "10.1103/PhysRevD.27.2885"),
        ("Moreva, E., Brida, G., Gramegna, M., Giovannetti, V., Maccone, L., & Genovese, M. (2014). Time from quantum entanglement: An experimental illustration. Physical Review A, 89(5), 052122.", "10.1103/PhysRevA.89.052122"),
        ("Giacomini, F., Castro-Ruiz, E., & Brukner, Č. (2019). Quantum mechanics and the covariance of physical laws in quantum reference frames. Nature Communications, 10, 494.", "10.1038/s41467-018-08155-0"),
        ("Stoica, O. C. (2026). The preferred-time problem in the conditional interpretation of time. arXiv preprint (not peer reviewed).", "10.48550/arXiv.2608.16732"),
    ],
}
