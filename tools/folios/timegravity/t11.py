# -*- coding: utf-8 -*-
"""Time & Gravity · T.11 — What selects the world a clock sees?

Instrument: a 1+6 qubit pure-dephasing pointer-state and Quantum Darwinism statevector model (dim = 128) whose
Jacobi-diagonalised partial traces match Zurek's closed-form mutual-information curve I(S : E_k) = h_2(γ^N) +
h_2(γ^k) - h_2(γ^{N-k}) within 1.7e-14 nats, paired with the Joos-Zeh / Romero-Isart R^6 T^9 thermal photon
scattering localization table from the 2.725 K CMB to 300 K (and Λ_EM = 0 for an electromagnetically uncoupled sector).
Knockout / planted defect: turning off pointer-commuting bath imprinting (θ = 0, γ = 1) collapses the classical
redundancy plateau I(S : E_k) to zero and fails the verifier.
Verifier: skills/timegravity/t11/verify_t11_einselection.py.
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t11"
CODE = "T.11"

BRUNE = "T11-BRUNE1996"
HORN = "T05-HORNBERGER2003"
HACK = "T05-HACKERMULLER2004"
MATHER = "T08-MATHER1994"
Z81 = "T11-ZUREK1981"
JOOS = "T11-JOOS1985"
Z09 = "T11-ZUREK2009"
EV57 = "T11-EVERETT1957"
DIOSI = "T06-DIOSI1987"
PEN96 = "T06-PENROSE1996"
DONADI = "T06-DONADI2021"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "date": "2026-11-10",
    "order_label_en": "Step 12 of 13",
    "order_label_es": "Paso 12 de 13",
    "kicker_en": "Time & Gravity · T.11 · How the photon bath selects pointer states and broadcasts a classical record",
    "kicker_es": "Tiempo y Gravedad · T.11 · Cómo el baño de fotones selecciona estados puntero y difunde un registro clásico",
    "title_en": "What Selects the World a Clock Sees?",
    "title_es": "¿Qué Selecciona el Mundo que Ve un Reloj?",
    "standfirst_en": (
        "On T.10 unitarity kept the full quantum state pure while an observer holding only a subsystem saw entropy rise and turn over. "
        "Why, then, does a laboratory clock always display one definite position rather than a superposition of pointers? "
        "Because electromagnetic scattering commutes with position: the ambient photon bath diagonalises the clock in the position basis "
        "and copies that eigenvalue across millions of scattered photons—while anything that does not couple to the bath leaves no optical record at all."
    ),
    "standfirst_es": (
        "En T.10 la unitariedad mantuvo puro el estado cuántico total mientras un observador que solo tenía un subsistema veía subir y dar la vuelta a la entropía. "
        "¿Por qué, entonces, un reloj de laboratorio muestra siempre una posición definida y no una superposición de agujas? "
        "Porque la dispersión electromagnética conmuta con la posición: el baño ambiental de fotones diagonaliza el reloj en la base de posición "
        "y copia ese autovalor en millones de fotones dispersados, mientras que cualquier sector que no se acople al baño no deja registro óptico alguno."
    ),
    "seo": (
        "What Selects the World a Clock Sees? Einselection and Quantum Darwinism",
        "How pointer-commuting photon scattering suppresses spatial superpositions and broadcasts redundant classical records in the electromagnetic bath.",
        "¿Qué Selecciona el Mundo que Ve un Reloj? Einselección y Darwinismo Cuántico",
        "Cómo la dispersión de fotones que conmuta con la posición suprime superposiciones espaciales y difunde registros clásicos redundantes.",
    ),
    "reading_time_en": "14 min read",
    "reading_time_es": "14 min de lectura",
    "central_number_en": "1+6 qubit statevector partial trace matches Zurek's I(S:E_k) within 1.7e-14 nats, reaching 0.998 bits at k=2 modes (θ=1.35 rad); R=10 µm dust grain at Δx=10 µm has τ_CMB = 1.63 s vs τ_300K = 6.89e-19 s (and Λ_EM = 0 at ε = 1)",
    "central_number_es": "La traza parcial del vector de estado de 1+6 qubits coincide con I(S:E_k) de Zurek dentro de 1.7e-14 nats, alcanzando 0.998 bits en k=2 modos (θ=1.35 rad); un grano de R=10 µm a Δx=10 µm tiene τ_CMB = 1.63 s frente a τ_300K = 6.89e-19 s (y Λ_EM = 0 en ε = 1)",
    "verifier": "skills/timegravity/t11/verify_t11_einselection.py",
    "generator": "skills/timegravity/t11/make_t11.py",
    "skill": "skills/timegravity/t11/SKILL.md",
    "skill_filename": "timegravity-t11-einselection.SKILL.md",
    "open_question_en": "If the electromagnetic bath only records and decoheres what couples to photons, how could our clocks ever detect a sector of matter that never scatters light at all?",
    "open_question_es": "Si el baño electromagnético solo registra y decohera lo que se acopla a los fotones, ¿cómo podrían nuestros relojes detectar un sector de materia que jamás dispersa la luz?",
    "ledger_ids": [BRUNE, HORN, HACK, MATHER, Z81, JOOS, Z09, EV57, DIOSI, PEN96, DONADI],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any measurement or derivation cited on this page. "
        "The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna medición o derivación citada en esta "
        "página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien mantiene el sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "einselection",
        "title_en": "Instrument · Pointer-state decoherence and the Quantum Darwinism redundancy plateau",
        "title_es": "Instrumento · Decoherencia de estados puntero y la meseta de redundancia del darwinismo cuántico",
        "how_en": (
            "Left: the mutual information I(S : E_k) (in bits) between a superposed pointer qubit S and a captured fragment E_k of k out of "
            "N = 6 environment photon modes, plotted alongside the decaying off-diagonal coherence |ρ_{S,01}(k)| / |ρ_{S,01}(0)| = cos^k(θ). "
            "Right: the Joos–Zeh / Romero-Isart thermal photon dipole localization time τ_sc = 1 / (Λ_sc Δx²) at Δx = 10 µm from the 2.725 K "
            "cosmic microwave background to 300 K for a 10 µm dust grain, a 1 µm microsphere (10⁶ times slower by R⁶), and an electromagnetically "
            "uncoupled mass (ε = 1, Λ_EM = 0). The sliders set the photon scattering angle θ per mode and the ambient temperature T_e. "
            "The knockout sets θ = 0 (no pointer-commuting bath imprinting): off-diagonal coherence stays at 1, the redundancy plateau "
            "collapses to 0 bits, and the verifier rejects the run. Keyboard: Tab and arrows. With reduced motion on, nothing animates."
        ),
        "how_es": (
            "Izquierda: la información mutua I(S : E_k) (en bits) entre un qubit puntero en superposición S y un fragmento capturado E_k de k "
            "entre N = 6 modos fotónicos del entorno, graficada junto a la coherencia fuera de la diagonal |ρ_{S,01}(k)| / |ρ_{S,01}(0)| = cos^k(θ). "
            "Derecha: el tiempo de localización dipolar por fotones térmicos de Joos–Zeh y Romero-Isart τ_sc = 1 / (Λ_sc Δx²) en Δx = 10 µm "
            "desde el fondo cósmico de microondas de 2.725 K hasta 300 K para un grano de polvo de 10 µm, una microesfera de 1 µm (10⁶ veces "
            "más lenta por R⁶) y una masa sin acoplamiento electromagnético (ε = 1, Λ_EM = 0). Los deslizadores fijan el ángulo de dispersión θ "
            "por modo y la temperatura ambiental T_e. El apagado fija θ = 0 (sin impresión en el baño que conmute con el puntero): la coherencia "
            "permanece en 1, la meseta de redundancia cae a 0 bits y el verificador rechaza la corrida. Teclado: Tab y flechas. Con movimiento reducido, nada se anima."
        ),
    },
    "predict": {
        "q_en": "Before you move the slider: at strong photon scattering (θ = 1.35 rad across N = 6 environment modes), how many modes must an observer intercept to learn over 99% of the pointer's 1 bit of classical position information?",
        "q_es": "Antes de mover el deslizador: con dispersión fotónica fuerte (θ = 1.35 rad en N = 6 modos del entorno), ¿cuántos modos debe interceptar un observador para conocer más del 99% del bit clásico de posición del puntero?",
        "options": [
            ("All 6 modes: without the entire bath, no position information is available", "Los 6 modos: sin todo el baño, no hay información de posición disponible"),
            ("Just 2 modes (k = 2): redundant copies form a plateau at 0.998 bits", "Solo 2 modos (k = 2): las copias redundantes forman una meseta en 0.998 bits"),
            ("Exactly 0 modes: decoherence erases information without recording it anywhere", "Exactamente 0 modos: la decoherencia borra la información sin registrarla en ningún lado"),
        ],
        "answer": 1,
        "reveal_en": "Just 2 out of 6 modes already carry 0.9983 bits: each scattered photon mode records the pointer eigenvalue independently, so many observers can read the same classical position from small, non-overlapping fractions of the light field.",
        "reveal_es": "Solo 2 de los 6 modos ya portan 0.9983 bits: cada modo fotónico dispersado registra de manera independiente el autovalor del puntero, de modo que muchos observadores pueden leer la misma posición clásica a partir de fracciones pequeñas y disjuntas del campo de luz.",
    },
    "sections": [
        {"type": "h2", "id": "measured", "en": "I · Measured decoherence in cavities and molecular beams", "es": "I · Decoherencia medida en cavidades y haces moleculares", "short_en": "I · Measured", "short_es": "I · Medido"},
        P(
            C("MEASURED", [BRUNE, HORN, HACK],
              "Environmental decoherence is not a philosophical postulate; its rate has been measured step by step as individual photons and "
              "gas molecules carry away which-path information: in 1996 Brune, Haroche and collaborators prepared a mesoscopic superposition of "
              "coherent microwave fields in a superconducting cavity and watched its interference fringes decay as photons leaked out, and in "
              "2003 and 2004 the Vienna fullerene interferometers measured quantitative visibility loss of C₇₀ molecules from single background-gas "
              "collisions and from thermal blackbody photons emitted by the heated molecules themselves.",
              "La decoherencia ambiental no es un postulado filosófico; su tasa se ha medido paso a paso conforme fotones individuales y moléculas de "
              "gas se llevan la información de trayectoria: en 1996 Brune, Haroche y colaboradores prepararon una superposición mesoscópica de campos "
              "coherentes de microondas en una cavidad superconductora y observaron decaer sus franjas de interferencia conforme escapaban fotones, y en "
              "2003 y 2004 los interferómetros de fulerenos en Viena midieron la pérdida cuantitativa de visibilidad de moléculas C₇₀ por colisiones "
              "individuales con gas residual y por fotones térmicos de cuerpo negro emitidos por las propias moléculas calientes."),
            T(" Every time a photon or gas atom resolves whether a mass took the left path or the right path, the two environment states become "
              "more orthogonal and the interference term between the paths shrinks by their inner product.",
              " Cada vez que un fotón o átomo de gas distingue si una masa tomó el camino izquierdo o el derecho, los dos estados del entorno se "
              "vuelven más ortogonales y el término de interferencia entre los caminos se reduce según su producto interno."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("Think of wet ink on a printing press. If a sheet of paper touches the plate without smudging it sideways, the raised letters "
                 "stay sharp while sheet after sheet carries away an identical copy of the words. Anyone in the room only needs to catch one "
                 "sheet of paper to know what is written on the press, without ever touching the metal plate itself.",
                 "Piensa en tinta fresca sobre una imprenta. Si una hoja de papel toca la placa sin correrla de lado, las letras en relieve se "
                 "mantienen nítidas mientras hoja tras hoja se lleva una copia idéntica de las palabras. Cualquiera en la sala solo necesita "
                 "atrapar una hoja para saber qué dice la prensa, sin tocar jamás la placa metálica.")),
             P(T("For ordinary matter, the ambient electromagnetic field is that stream of paper. Because electric charges and dipoles scatter "
                 "photons according to where they sit in space, position is the 'raised letter' that survives the contact. Superpositions of "
                 "different positions are rapidly diagonalised, while the surviving position is copied into millions of scattered photons—what "
                 "physicists call environment-induced superselection (einselection) and Quantum Darwinism.",
                 "Para la materia ordinaria, el campo electromagnético ambiental es ese flujo de papel. Como las cargas y los dipolos eléctricos "
                 "dispersan fotones según dónde están en el espacio, la posición es la 'letra en relieve' que sobrevive al contacto. Las "
                 "superposiciones de distintas posiciones se diagonalizan rápidamente, mientras la posición sobreviviente se copia en millones de "
                 "fotones dispersados: lo que la física llama superselección inducida por el entorno (einselección) y darwinismo cuántico.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: a lighthouse beam sweeping through fog. A ship that reflects light scatters droplets of glare in every "
                 "direction, so twenty watchers on different cliffs all agree on the ship's bearing after catching a tiny fraction of the scattered "
                 "light. Something completely transparent to light leaves the fog undisturbed—not because it is in another universe, but because "
                 "photons pass straight through it without taking an imprint.",
                 "Analogía cotidiana: el haz de un faro atravesando la niebla. Un barco que refleja la luz dispersa destellos en todas direcciones, "
                 "así que veinte observadores en distintos acantilados coinciden en la posición del barco tras captar una fracción mínima de la luz "
                 "dispersada. Algo completamente transparente a la luz deja la niebla intacta: no porque esté en otro universo, sino porque los "
                 "fotones lo atraviesan sin llevarse una huella.")),
             P(T("How the controls work in plain words: the first slider sets θ, how strongly each scattered photon mode distinguishes left from "
                 "right. As θ grows, the orange coherence curve cos^k(θ) drops toward zero while the blue mutual-information curve I(S : E_k) rises "
                 "into a flat plateau near 1 bit. The second slider changes the ambient photon temperature from the 2.725 K cosmic microwave "
                 "background to 300 K room temperature, scaling the dipole scattering rate as T⁹. The knockout sets θ = 0 (an electromagnetically "
                 "transparent coupling): coherence stays at 1 and the classical plateau vanishes.",
                 "Cómo funcionan los controles en palabras sencillas: el primer deslizador fija θ, qué tanto distingue cada modo fotónico dispersado "
                 "la izquierda de la derecha. Al crecer θ, la curva naranja de coherencia cos^k(θ) cae hacia cero mientras la curva azul de "
                 "información mutua I(S : E_k) sube hasta una meseta plana cercana a 1 bit. El segundo deslizador cambia la temperatura ambiental de "
                 "fotones desde los 2.725 K del fondo cósmico hasta 300 K, escalando la tasa dipolar como T⁹. El apagado fija θ = 0 (un acoplamiento "
                 "transparente a la luz): la coherencia permanece en 1 y la meseta clásica desaparece.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "derived", "en": "II · Pointer states, the redundancy plateau, and the R⁶ T⁹ photon bath", "es": "II · Estados puntero, la meseta de redundancia y el baño fotónico R⁶ T⁹", "short_en": "II · Derived", "short_es": "II · Derivado"},
        {"type": "equation", "text": "[Ĥ_int, Π̂] = 0   ⇒   |ρ_{S,01}(N)| / |ρ_{S,01}(0)| = γ^N,   I(S : E_k) = h₂(γ^N) + h₂(γ^k) − h₂(γ^{N−k})"},
        P(
            C("DERIVED", [Z81, JOOS, BRUNE],
              "Zurek showed in 1981 and 1982 that when a quantum system S couples to an environment E through an interaction Hamiltonian Ĥ_int, "
              "the eigenstates of the observable Π̂ that commutes with Ĥ_int ([Ĥ_int, Π̂] = 0) are dynamically stable pointer states: each "
              "environment mode E_j rotates conditionally on the pointer eigenvalue without flipping it, suppressing off-diagonal superpositions "
              "by the product of mode overlaps γ^N = |⟨E^{(0)}|E^{(1)}⟩|^N.",
              "Zurek mostró en 1981 y 1982 que cuando un sistema cuántico S se acopla a un entorno E mediante un hamiltoniano de interacción Ĥ_int, "
              "los autoestados del observable Π̂ que conmuta con Ĥ_int ([Ĥ_int, Π̂] = 0) son estados puntero dinámicamente estables: cada modo "
              "ambiental E_j rota condicionalmente según el autovalor del puntero sin invertirlo, suprimiendo las superposiciones fuera de la "
              "diagonal por el producto de traslapes γ^N = |⟨E^{(0)}|E^{(1)}⟩|^N.",
              parent=BRUNE),
            T(" Because the Coulomb and dipole couplings of light to matter depend on position x̂, the interaction term Ĥ_int commutes with x̂ "
              "(whereas the free kinetic term p̂²/2m does not), singling out localized position states as the pointer basis of macroscopic clocks.",
              " Como los acoplamientos de Coulomb y dipolares de la luz con la materia dependen de la posición x̂, el término de interacción Ĥ_int "
              "conmuta con x̂ (mientras que el término cinético libre p̂²/2m no lo hace), seleccionando estados localizados de posición como la base "
              "puntero de los relojes macroscópicos."),
        ),
        P(
            C("DERIVED", [Z09, Z81, BRUNE],
              "In 2009 Zurek showed that pure pointer-state dephasing also explains why independent observers agree on the same classical readout "
              "(Quantum Darwinism): for a symmetric pointer superposition coupled to N modes with overlap γ = |cos θ|, the mutual information "
              "between S and a fragment E_k of k modes is I(S : E_k) = h₂(γ^N) + h₂(γ^k) − h₂(γ^{N−k}), which rises rapidly to a classical "
              "redundancy plateau at S(ρ_S) ≈ ln 2 and satisfies the exact midpoint identity I(S : E_{N/2}) = S(ρ_S).",
              "En 2009 Zurek mostró que el desfasamiento puro en la base puntero también explica por qué observadores independientes coinciden en la "
              "misma lectura clásica (darwinismo cuántico): para una superposición simétrica del puntero acoplada a N modos con traslape γ = |cos θ|, "
              "la información mutua entre S y un fragmento E_k de k modos es I(S : E_k) = h₂(γ^N) + h₂(γ^k) − h₂(γ^{N−k}), que sube rápidamente hasta "
              "una meseta clásica de redundancia en S(ρ_S) ≈ ln 2 y cumple la identidad exacta de punto medio I(S : E_{N/2}) = S(ρ_S).",
              parent=BRUNE),
            T(" On 1 + 6 qubits (statevector dimension 128) at θ = 1.35 rad, the verifier computes every reduced density matrix ρ_S, ρ_{E_k} and "
              "ρ_{S E_k} by explicit partial trace, rotates each into a dense matrix via DCT-II, diagonalises it with the track's pure-Python "
              "Jacobi solver, and matches the closed-form binary entropy curve within 1.7×10⁻¹⁴ nats across all k = 0 … 6: capturing just k = 2 "
              "modes already yields 0.9983 bits while off-diagonal coherence on S has fallen to 1.1×10⁻⁴.",
              " En 1 + 6 qubits (dimensión 128 del vector de estado) en θ = 1.35 rad, el verificador calcula cada matriz de densidad reducida ρ_S, "
              "ρ_{E_k} y ρ_{S E_k} por traza parcial explícita, rota cada una en una matriz densa mediante DCT-II, la diagonaliza con el solver de "
              "Jacobi en Python puro de la serie, y coincide con la curva cerrada de entropía binaria dentro de 1.7×10⁻¹⁴ nats en todo k = 0 … 6: "
              "capturar apenas k = 2 modos ya entrega 0.9983 bits mientras la coherencia fuera de la diagonal en S ha caído a 1.1×10⁻⁴."),
        ),
        {"type": "equation", "text": "Λ_sc(R, T_e, ε) = (8! · 8 ζ(9) c R⁶ / 9π) (k_B T_e / ħc)⁹ Re[(ε − 1)/(ε + 2)]²,   Γ_sc = Λ_sc Δx²"},
        P(
            C("DERIVED", [JOOS, MATHER, HACK],
              "Joos and Zeh derived in 1985 the long-wavelength dipole Rayleigh scattering rate of thermal photons off a dielectric sphere of "
              "radius R and permittivity ε: the localization parameter Λ_sc scales as R⁶ T_e⁹ Re[(ε − 1)/(ε + 2)]², so even the 2.725 K cosmic "
              "microwave background localizes a R = 10 µm dust grain across Δx = 10 µm on a one-second timescale (τ_CMB = 1.63 s for ε = 5.7, or "
              "0.61 s in the conducting limit Λ_CMB = 1.64×10⁶ cm⁻² s⁻¹), whereas 300 K room-temperature photons localize the same split in "
              "6.89×10⁻¹⁹ s.",
              "Joos y Zeh derivaron en 1985 la tasa de dispersión dipolar de Rayleigh de longitud de onda larga de fotones térmicos sobre una esfera "
              "dieléctrica de radio R y permitividad ε: el parámetro de localización Λ_sc escala como R⁶ T_e⁹ Re[(ε − 1)/(ε + 2)]², de modo que "
              "incluso el fondo cósmico de microondas de 2.725 K localiza un grano de polvo de R = 10 µm a través de Δx = 10 µm en una escala de un "
              "segundo (τ_CMB = 1.63 s para ε = 5.7, o 0.61 s en el límite conductor Λ_CMB = 1.64×10⁶ cm⁻² s⁻¹), mientras que los fotones a 300 K "
              "localizan la misma separación en 6.89×10⁻¹⁹ s.",
              parent=MATHER),
            T(" Because of the sixth power in radius R⁶, shrinking the sphere tenfold from a 10 µm dust grain to the 1 µm diamond microsphere of "
              "T.05 reduces Λ_sc by exactly 10⁶ (lengthening τ_CMB to 1.63×10⁶ s and τ_300K to 0.69 ps). And for an electromagnetically uncoupled "
              "test mass (ε = 1, zero electric charge and dipole moment), Re[(ε − 1)/(ε + 2)] = 0 and Λ_sc = 0 at every temperature: the photon "
              "bath neither decoheres it nor records its position.",
              " Debido a la sexta potencia en el radio R⁶, reducir diez veces la esfera desde un grano de polvo de 10 µm hasta la microesfera de "
              "diamante de 1 µm de T.05 reduce Λ_sc exactamente por 10⁶ (alargando τ_CMB a 1.63×10⁶ s y τ_300K a 0.69 ps). Y para una masa de prueba "
              "sin acoplamiento electromagnético (ε = 1, carga eléctrica y momento dipolar nulos), Re[(ε − 1)/(ε + 2)] = 0 y Λ_sc = 0 a cualquier "
              "temperatura: el baño de fotones ni la decohera ni registra su posición."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "open", "en": "III · Three distinct concepts: pointer records, decohered branches, and dark sectors", "es": "III · Tres conceptos distintos: registros puntero, ramas decoheridas y sectores oscuros", "short_en": "III · Not said", "short_es": "III · No dicho"},
        P(
            C("PROPOSED", [EV57, DIOSI, PEN96],
              "Once environmental scattering drives the overlap ⟨E^{(0)}|E^{(1)}⟩ = γ^N toward zero, what happens to the unselected branch is "
              "the subject of competing proposals: Everett's 1957 relative-state formulation keeps the global state unitary so both orthogonal "
              "branches persist in Hilbert space without being able to interfere locally, whereas objective-reduction models such as Diósi (1987) "
              "and Penrose (1996) modify Schrödinger's equation so gravitational self-energy collapses superpositions at a physical rate.",
              "Una vez que la dispersión ambiental lleva el traslape ⟨E^{(0)}|E^{(1)}⟩ = γ^N hacia cero, qué ocurre con la rama no seleccionada es "
              "objeto de propuestas en competencia: la formulación de estados relativos de Everett de 1957 mantiene unitario el estado global de modo "
              "que ambas ramas ortogonales persisten en el espacio de Hilbert sin poder interferir localmente, mientras que los modelos de reducción "
              "objetiva como Diósi (1987) y Penrose (1996) modifican la ecuación de Schrödinger para que la autoenergía gravitacional colapse las "
              "superposiciones a una tasa física."),
            T(" ", " "),
            C("BOUND", [DONADI],
              "As examined on T.06, underground X-ray searches such as VIP-2 bound the parameter-free Diósi–Penrose cutoff to r₀ > 0.54×10⁻¹⁰ m "
              "while leaving softer smearing scales open.",
              "Como se examinó en T.06, las búsquedas subterráneas de rayos X como VIP-2 acotan el corte libre de parámetros de Diósi y Penrose a "
              "r₀ > 0.54×10⁻¹⁰ m dejando abiertas escalas de suavizado mayores."),
        ),
        P(
            C("OPEN", [EV57, Z09],
              "Whether decohered branches of ordinary matter persist physically after photon scattering makes their environment records orthogonal "
              "or are eliminated by an objective collapse mechanism is not settled by any experiment to date: einselection and Quantum Darwinism "
              "derive why each branch sees a stable classical pointer, not why one branch is experienced rather than another.",
              "Si las ramas decoheridas de la materia ordinaria persisten físicamente después de que la dispersión fotónica vuelve ortogonales sus "
              "registros ambientales o si son eliminadas por un mecanismo de colapso objetivo no está resuelto por ningún experimento hasta la fecha: "
              "la einselección y el darwinismo cuántico derivan por qué cada rama ve un puntero clásico estable, no por qué se experimenta una rama y no otra."),
            T(" Crucially, this page keeps a strict three-way fence: (1) electromagnetic pointer selection (DERIVED from MEASURED cavity and "
              "molecular decoherence), (2) unselected decohered branches in Hilbert space (whose ontological status is OPEN), and (3) matter in "
              "our same four-dimensional spacetime that has zero tree-level electromagnetic coupling (ε = 1, α_EM = 0). Decohered branches and "
              "electromagnetically uncoupled dark sectors are completely different physical concepts—and the next page asks how two clocks can "
              "meet through gravity alone when the electromagnetic bath is completely silent.",
              " De manera crucial, esta página mantiene una frontera estricta entre tres conceptos: (1) la selección electromagnética de estados "
              "puntero (DERIVADA de la decoherencia MEDIDA en cavidades y haces moleculares), (2) las ramas decoheridas en el espacio de Hilbert "
              "(cuyo estatus ontológico permanece ABIERTO), y (3) la materia en nuestro mismo espaciotiempo cuadridimensional con acoplamiento "
              "electromagnético nulo a nivel árbol (ε = 1, α_EM = 0). Las ramas decoheridas y los sectores oscuros sin acoplamiento electromagnético "
              "son conceptos físicos completamente distintos, y la siguiente página pregunta cómo dos relojes pueden encontrarse solo por gravedad "
              "cuando el baño electromagnético guarda silencio total."),
        ),
        {"type": "change_box",
         "items": [
             ("Direct tomography of multi-fragment mutual information I(S : E_k) across controlled photon baths in additional independent platforms would strengthen the experimental backing of Quantum Darwinism redundancy plateaus.",
              "La tomografía directa de la información mutua multifragmento I(S : E_k) en baños fotónicos controlados en plataformas independientes adicionales fortalecería el respaldo experimental de las mesetas de redundancia del darwinismo cuántico."),
             ("A decisive macroscopic superposition test in the regime where gravitational collapse models predict visibility loss beyond thermal photon and gas decoherence (T.05–T.06) would test whether unitary branching breaks down at large mass.",
              "Una prueba decisiva de superposición macroscópica en el régimen donde los modelos de colapso gravitacional predicen pérdida de visibilidad más allá de la decoherencia por fotones térmicos y gas (T.05–T.06) pondría a prueba si la ramificación unitaria se rompe a gran masa."),
             ("If the 1+6 qubit statevector partial trace ever differed from Zurek's closed-form binary entropy curve by more than 1e-12 nats, or if the R⁶ T⁹ photon scattering scaling failed, the verifier fails and the page does not build.",
              "Si la traza parcial del vector de estado de 1+6 qubits llegara a diferir de la curva cerrada de entropía binaria de Zurek por más de 1e-12 nats, o si fallara el escalamiento R⁶ T⁹ de dispersión fotónica, el verificador falla y la página no se construye."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · 1+6 qubit pointer-dephasing statevector", "Etapa 1 · Vector de estado de desfasamiento puntero de 1+6 qubits",
         "|Ψ_{SE}(θ)⟩ = (|0⟩_S ⊗ |0⟩^{⊗6} + |1⟩_S ⊗ (cos θ |0⟩ + sin θ |1⟩)^{⊗6}) / √2 in 2⁷ = 128 dimensions. Tracing out all 6 modes leaves off-diagonal coherence |ρ_{S,01}| / (1/2) = cos⁶(θ), checked against explicit partial trace to < 1e-15.",
         "|Ψ_{SE}(θ)⟩ = (|0⟩_S ⊗ |0⟩^{⊗6} + |1⟩_S ⊗ (cos θ |0⟩ + sin θ |1⟩)^{⊗6}) / √2 en 2⁷ = 128 dimensiones. Trazar sobre los 6 modos deja la coherencia fuera de la diagonal |ρ_{S,01}| / (1/2) = cos⁶(θ), comprobada contra la traza parcial explícita a < 1e-15."),
        ("Stage 2 · Partial-trace Jacobi diagonalisation across k = 0 … 6", "Etapa 2 · Diagonalización de Jacobi por traza parcial en k = 0 … 6",
         "For every fragment size k ∈ {0 … 6}, the kernel forms ρ_{E_k} (2^k × 2^k) and ρ_{S E_k} (2^{k+1} × 2^{k+1}) by explicit partial trace, rotates each by an orthogonal DCT-II matrix into a dense symmetric matrix, and diagonalises with cyclic Jacobi to obtain I(S : E_k).",
         "Para cada tamaño de fragmento k ∈ {0 … 6}, el kernel construye ρ_{E_k} (2^k × 2^k) y ρ_{S E_k} (2^{k+1} × 2^{k+1}) por traza parcial explícita, rota cada una mediante una matriz ortogonal DCT-II en una matriz simétrica densa y la diagonaliza con Jacobi cíclico para obtener I(S : E_k)."),
        ("Stage 3 · Redundancy plateau & R⁶ T⁹ photon localization", "Etapa 3 · Meseta de redundancia y localización fotónica R⁶ T⁹",
         "Jacobi mutual information matches h₂(γ^N) + h₂(γ^k) − h₂(γ^{N−k}) within 1.7e-14 nats across all k and θ, reaching 0.9983 bits at k = 2 (θ = 1.35 rad) and obeying I(S : E_3) = S(ρ_S) to 2.4e-15. Dipole photon scattering verifies Λ(10 µm)/Λ(1 µm) = 10⁶ and Λ(300 K)/Λ(T_CMB) = (300/T_CMB)⁹ to < 1e-15.",
         "La información mutua de Jacobi coincide con h₂(γ^N) + h₂(γ^k) − h₂(γ^{N−k}) dentro de 1.7e-14 nats en todo k y θ, alcanzando 0.9983 bits en k = 2 (θ = 1.35 rad) y cumpliendo I(S : E_3) = S(ρ_S) a 2.4e-15. La dispersión dipolar fotónica verifica Λ(10 µm)/Λ(1 µm) = 10⁶ y Λ(300 K)/Λ(T_CMB) = (300/T_CMB)⁹ a < 1e-15."),
        ("Stage 4 · Planted defect knockout", "Etapa 4 · Apagado por defecto plantado",
         "Setting θ = 0 removes pointer-commuting bath imprinting: off-diagonal coherence remains 1.0 and the k = 2 mutual information collapses to 0 bits, failing the plateau gate and rejecting the run.",
         "Fijar θ = 0 elimina la impresión en el baño que conmuta con el puntero: la coherencia fuera de la diagonal permanece en 1.0 y la información mutua en k = 2 colapsa a 0 bits, fallando la compuerta de meseta y rechazando la corrida."),
    ],
    "sidenotes": [
        ("SIDENOTE T.11-A · WHY [Ĥ_INT, x̂] = 0 SELECTS POSITION DESPITE FREE KINETIC SPREADING", "NOTA T.11-A · POR QUÉ [Ĥ_INT, x̂] = 0 SELECCIONA LA POSICIÓN PESE A LA DISPERSIÓN CINÉTICA LIBRE",
         "A free particle's kinetic Hamiltonian p̂²/(2m) commutes with momentum, not position. For a macroscopic grain of mass m in a thermal photon bath, however, environmental scattering operates on a timescale τ_sc many orders of magnitude faster than free wave-packet spreading, so the interaction term Ĥ_int(x̂) dominates the pointer selection.",
         "El hamiltoniano cinético libre p̂²/(2m) conmuta con el momento, no con la posición. Sin embargo, para un grano macroscópico de masa m en un baño de fotones térmicos, la dispersión ambiental opera en una escala temporal τ_sc muchos órdenes de magnitud más rápida que el ensanchamiento libre del paquete de ondas, de modo que el término de interacción Ĥ_int(x̂) domina la selección del puntero."),
        ("SIDENOTE T.11-B · HILBERT-SPACE ORTHOGONALITY VS SPACETIME TRANSPARENCY", "NOTA T.11-B · ORTOGONALIDAD EN EL ESPACIO DE HILBERT FRENTE A TRANSPARENCIA EN EL ESPACIOTIEMPO",
         "Two decohered branches |0⟩_S ⊗ |E^{(0)}⟩ and |1⟩_S ⊗ |E^{(1)}⟩ of an ordinary mass are unseen to each other because their photon records are orthogonal in Hilbert space (⟨E^{(0)}|E^{(1)}⟩ → 0) after strong electromagnetic scattering. A dark-matter particle with α_EM = 0 (T.12) is unseen to photons for the opposite reason: it never couples to the electromagnetic field in the first place (θ = 0, γ = 1).",
         "Dos ramas decoheridas |0⟩_S ⊗ |E^{(0)}⟩ y |1⟩_S ⊗ |E^{(1)}⟩ de una masa ordinaria son invisibles entre sí porque sus registros fotónicos son ortogonales en el espacio de Hilbert (⟨E^{(0)}|E^{(1)}⟩ → 0) tras una fuerte dispersión electromagnética. Una partícula de materia oscura con α_EM = 0 (T.12) es invisible a los fotones por la razón opuesta: nunca se acopla al campo electromagnético (θ = 0, γ = 1)."),
    ],
    "sources": [
        ("Brune, M., Hagley, E., Dreyer, J., Maître, X., Maali, A., Wunderlich, C., Raimond, J. M., & Haroche, S. (1996). Observing the progressive decoherence of the 'meter' in a quantum measurement. Physical Review Letters, 77(24), 4887–4890.", "10.1103/PhysRevLett.77.4887"),
        ("Hornberger, K., Uttenthaler, S., Brezger, B., Hackermüller, L., Arndt, M., & Zeilinger, A. (2003). Collisional decoherence observed in matter wave interferometry. Physical Review Letters, 90(16), 160401.", "10.1103/PhysRevLett.90.160401"),
        ("Hackermüller, L., Hornberger, K., Brezger, B., Zeilinger, A., & Arndt, M. (2004). Decoherence of matter waves by thermal emission of radiation. Nature, 427, 711–714.", "10.1038/nature02276"),
        ("Mather, J. C., et al. (1994). Measurement of the cosmic microwave background spectrum by the COBE FIRAS instrument. The Astrophysical Journal, 420, 439–444.", "10.1086/173574"),
        ("Zurek, W. H. (1981). Pointer basis of quantum apparatus: Into what mixture does the wave packet collapse? Physical Review D, 24(6), 1516–1525.", "10.1103/PhysRevD.24.1516"),
        ("Joos, E., & Zeh, H. D. (1985). The emergence of classical properties through interaction with the environment. Zeitschrift für Physik B Condensed Matter, 59(2), 223–243.", "10.1007/BF01725541"),
        ("Zurek, W. H. (2009). Quantum Darwinism. Nature Physics, 5, 181–188.", "10.1038/nphys1202"),
        ("Everett, H. (1957). 'Relative state' formulation of quantum mechanics. Reviews of Modern Physics, 29(3), 454–462.", "10.1103/RevModPhys.29.454"),
        ("Diósi, L. (1987). A universal master equation for the gravitational violation of quantum mechanics. Physics Letters A, 120(8), 377–381.", "10.1016/0375-9601(87)90681-5"),
        ("Penrose, R. (1996). On gravity's role in quantum state reduction. General Relativity and Gravitation, 28(5), 581–600.", "10.1007/BF02105068"),
        ("Donadi, S., Piscicchia, K., Curceanu, C., Diósi, L., Laubenstein, M., & Bassi, A. (2020). Underground test of gravity-related wave function collapse. Nature Physics, 17, 74–78.", "10.1038/s41567-020-1008-4"),
    ],
}
