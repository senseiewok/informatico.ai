# -*- coding: utf-8 -*-
"""Time & Gravity · T.13 — Where infrared gravity meets gauge theory.

Instrument: an infrared consistency observatory combining Weinberg's s = 1, 2, >= 3 soft Ward residuals,
Christodoulou / Strominger-Zhiboedov gravitational-wave displacement memory and baseline holonomy
Delta h_char = G E_rad / (c^4 D_L), Delta L / L_0 = (1/2) Delta h_+^mem, and one-loop Standard Model chiral and
mixed gauge-gravitational anomaly traces (6Y integer scaling) across colour multiplicity N_c, paired with the pure
core Lean 4 Prelude formalization skills/timegravity/t13/HolonomySoftAnomaly.lean.
Knockout / planted defect: perturbing species gravitational coupling kappa_e / kappa_p = 1 + 1e-5 violates the
soft-graviton Ward identity and setting N_c = 2 != 3 breaks SU(2)_L^2 U(1)_Y and U(1)_Y^3 anomaly cancellation.
Verifier: skills/timegravity/t13/verify_t13_holonomy_soft.py.
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t13"
CODE = "T.13"

MICRO = "T03-MICRO2022"
EOT08 = "T03-EOTWASH2008"
ABB16 = "T10-ABBOTT2016"
ISI21 = "T10-ISI2021"
LVK25 = "T10-LVK2025"
LEE20 = "T05-LEE2020"
LEE21 = "T05-LEE2021"
TAN20 = "T05-TAN2020"
DIOSI87 = "T06-DIOSI1987"
PENROSE96 = "T06-PENROSE1996"
BOSE17 = "T05-BOSE2017"
SCH24 = "T05-SCHUT2024"

W64 = "T13-WEINBERG1964"
W65 = "T13-WEINBERG1965"
ADL69 = "T13-ADLER1969"
DEL72 = "T13-DELBOURGO1972"
AGW84 = "T13-AGW1984"
FAV09 = "T13-FAVATA2009"
CHR91 = "T13-CHRIST1991"
STR16 = "T13-STROM2016"
HUB20 = "T13-HUBNER2020"
ZH24 = "T13-ZHANG2024"
TOOBY25 = "T13-TOOBY2025"

EMP_SCOPE = "Scoped to published mass, energy, baseline, and confidence regimes in cited experiments"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "date": "2026-11-11",
    "order_label_en": "Step 14 of 14",
    "order_label_es": "Paso 14 de 14",
    "kicker_en": "Time & Gravity · T.13 · Soft gravitons, gravitational memory, and the gauge–gravity anomaly bridge",
    "kicker_es": "Tiempo y Gravedad · T.13 · Gravitones blandos, memoria gravitacional y el puente de anomalías entre gravedad y teorías gauge",
    "title_en": "Where Infrared Gravity Meets Gauge Theory",
    "title_es": "Donde la Gravedad Infrarroja Toca las Teorías Gauge",
    "standfirst_en": (
        "At Planckian energies the microscopic quantum structure of spacetime remains unknown, yet in the long-wavelength infrared limit "
        "Lorentz invariance and gauge consistency place exact algebraic locks across gravity and particle physics. Weinberg's soft theorems "
        "force every massless spin-2 field to couple universally to energy-momentum, Strominger and Zhiboedov's infrared triangle ties "
        "soft gravitons to permanent gravitational-wave memory across free-falling clocks and mirrors, and one-loop mixed gauge–gravitational "
        "anomaly cancellation joins chiral gauge traces to require N_c = 3 quark colours once the hypercharges take their observed values."
    ),
    "standfirst_es": (
        "A energías de la escala de Planck la estructura cuántica microscópica del espaciotiempo sigue sin conocerse, pero en el límite "
        "infrarrojo de gran longitud de onda la invariancia de Lorentz y la consistencia gauge imponen candados algebraicos exactos entre "
        "la gravedad y la física de partículas. Los teoremas blandos de Weinberg obligan a todo campo sin masa de espín 2 a acoplarse de "
        "forma universal a la energía-momento, el triángulo infrarrojo de Strominger y Zhiboedov enlaza los gravitones blandos con la "
        "memoria permanente de ondas gravitacionales en espejos y relojes en caída libre, y la cancelación de anomalías mixtas "
        "gauge-gravitacionales a un lazo se suma a las trazas quirales para exigir N_c = 3 colores de quarks una vez que las hipercargas toman sus valores observados."
    ),
    "seo": (
        "Where Infrared Gravity Meets Gauge Theory",
        "Soft gravitons, gravitational wave memory, and mixed anomaly cancellation link equivalence and quark colour while UV quantum gravity stays open.",
        "Donde la Gravedad Infrarroja Toca las Teorías Gauge",
        "Gravitones blandos, memoria gravitacional y cancelación de anomalías mixtas ligan equivalencia y color de quarks con la escala UV aún abierta.",
    ),
    "reading_time_en": "16 min read",
    "reading_time_es": "16 min de lectura",
    "central_number_en": "Weinberg s=2 Ward residual ||W^μ||/E_cm = 0 iff κ_e = κ_p (η = 0); GW150914 fiducial memory step Δh_char = 3.50×10⁻²² (ΔL_char = 7.00×10⁻¹⁹ m on 4 km, GL5 quadrature within 1.3e-16); all 4 SM chiral & mixed gravitational anomaly traces vanish iff N_c = 3 (12 Lean 4 Prelude theorems)",
    "central_number_es": "Residuo de Ward s=2 de Weinberg ||W^μ||/E_cm = 0 sii κ_e = κ_p (η = 0); escalón fiducial de memoria en GW150914 Δh_char = 3.50×10⁻²² (ΔL_char = 7.00×10⁻¹⁹ m en 4 km, cuadratura GL5 dentro de 1.3e-16); las 4 trazas de anomalías quirales y gravitacionales del Modelo Estándar se anulan sii N_c = 3 (12 teoremas en Lean 4 Prelude)",
    "verifier": "skills/timegravity/t13/verify_t13_holonomy_soft.py",
    "generator": "skills/timegravity/t13/make_t13.py",
    "skill": "skills/timegravity/t13/SKILL.md",
    "skill_filename": "timegravity-t13-holonomy-soft.SKILL.md",
    "open_question_en": "Infrared consistency fixes universal gravitational coupling, permanent wave memory, and chiral anomaly cancellation from below—what laboratory witness across sub-millimetre superpositions or optical–nuclear clock networks will first test where classical spacetime gives way above?",
    "open_question_es": "La consistencia infrarroja fija desde abajo el acoplamiento gravitacional universal, la memoria permanente de ondas y la cancelación de anomalías quirales: ¿qué testigo experimental en superposiciones submilimétricas o redes de relojes ópticos y nucleares pondrá a prueba primero dónde cede el espaciotiempo clásico por arriba?",
    "ledger_ids": [
        MICRO, EOT08, ABB16, ISI21, LVK25, LEE20, LEE21, TAN20, DIOSI87, PENROSE96, BOSE17, SCH24,
        W64, W65, ADL69, DEL72, AGW84, CHR91, FAV09, STR16, HUB20, ZH24, TOOBY25,
    ],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any measurement or theoretical derivation cited on this page; "
        "Tooby-Smith (2025) is an author-written Lean 4 formalization library (PhysLean / HepLean). The page text, interactive instrument, "
        "Lean 4 Prelude companion, and Python verifier were drafted with AI assistance and checked against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna medición o derivación teórica citada en "
        "esta página; Tooby-Smith (2025) es una biblioteca de formalización en Lean 4 escrita por su autor (PhysLean / HepLean). El texto, el "
        "instrumento interactivo, el archivo en Lean 4 Prelude y el verificador en Python se redactaron con asistencia de IA y se revisaron contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "holonomy_soft",
        "title_en": "Instrument · Soft-graviton Ward residual, gravitational-wave memory step & N_c anomaly bridge",
        "title_es": "Instrumento · Residuo de Ward de gravitón blando, escalón de memoria gravitacional y puente de anomalías en N_c",
        "how_en": (
            "Left: the Christodoulou / Strominger–Zhiboedov gravitational-wave displacement memory curve Δh(t) across merger burst flux "
            "dE_rad/dt, leaving a permanent baseline offset ΔL = (1/2) L₀ Δh_+^mem between free-falling mirrors or clocks after the oscillatory "
            "ringdown dies out. Right: the Weinberg s = 2 soft-graviton gauge Ward residual ||W^μ||/E_cm alongside the four Standard Model "
            "chiral and mixed gauge–gravitational anomaly traces (6Y scaling) across quark colour multiplicity N_c ∈ {1, 2, 3, 4, 5}. "
            "Sliders adjust radiated merger energy E_rad (in M_⊙ c²), luminosity distance D_L (in Mpc), and integer quark colour count N_c. "
            "The knockout injects the planted defect (κ_e / κ_p = 1 + 10⁻⁵ and N_c = 2): both Lorentz soft gauge invariance and chiral "
            "anomaly cancellation fail simultaneously, and the verifier exits 1. Keyboard: Tab and arrows. With reduced motion on, nothing animates."
        ),
        "how_es": (
            "Izquierda: la curva de memoria de desplazamiento de ondas gravitacionales Δh(t) de Christodoulou y Strominger–Zhiboedov a través "
            "del flujo de energía dE_rad/dt, dejando un corrimiento permanente ΔL = (1/2) L₀ Δh_+^mem entre espejos o relojes en caída libre "
            "cuando la oscilación se apaga. Derecha: el residuo gauge de Ward s = 2 de Weinberg ||W^μ||/E_cm junto con las cuatro trazas de "
            "anomalías quirales y mixtas gauge-gravitacionales del Modelo Estándar (escala 6Y) según el número de colores N_c ∈ {1, 2, 3, 4, 5}. "
            "Los deslizadores ajustan la energía radiada E_rad (en M_⊙ c²), la distancia de luminosidad D_L (en Mpc) y el entero de colores N_c. "
            "El apagado inyecta el defecto plantado (κ_e / κ_p = 1 + 10⁻⁵ y N_c = 2): fallan a la vez la invariancia gauge blanda de Lorentz y "
            "la cancelación de anomalías quirales, y el verificador sale con código 1. Teclado: Tab y flechas. Con movimiento reducido, nada se anima."
        ),
    },
    "predict": {
        "q_en": "Before you toggle the readout: in relativistic 2 → 2 electron–proton scattering, if the electron coupled to soft massless spin-2 gravitons by even 10 parts per million more strongly than the proton (κ_e / κ_p = 1 + 10⁻⁵) while 4-momentum is conserved, what happens to the scattering amplitude under a longitudinal graviton gauge shift?",
        "q_es": "Antes de activar la lectura: en una dispersión relativista 2 → 2 electrón-protón, si el electrón se acoplara a gravitones blandos sin masa de espín 2 apenas 10 partes por millón más fuerte que el protón (κ_e / κ_p = 1 + 10⁻⁵) conservando el cuadrimpulso, ¿qué le ocurre a la amplitud de dispersión bajo una transformación gauge longitudinal del gravitón?",
        "options": [
            ("Nothing changes: each particle species can pick its own gravitational constant without affecting Lorentz invariance", "No cambia nada: cada especie de partícula puede elegir su propia constante gravitacional sin afectar la invariancia de Lorentz"),
            ("The longitudinal Ward residual W^μ = (κ_p − κ_e)(p₁^μ − p₃^μ) becomes non-zero, so unphysical longitudinal graviton polarizations fail to decouple and violate Lorentz invariance", "El residuo longitudinal de Ward W^μ = (κ_p − κ_e)(p₁^μ − p₃^μ) deja de anularse, por lo que las polarizaciones longitudinales no físicas no se desacoplan y violan la invariancia de Lorentz"),
            ("Only spin-3 bosons are affected; spin-2 gravitons do not have gauge redundancy", "Solo se afectan los bosones de espín 3; los gravitones de espín 2 no tienen redundancia gauge"),
        ],
        "answer": 1,
        "reveal_en": "Because four-momentum conservation gives p₄^μ = p₁^μ + p₂^μ − p₃^μ, the soft-graviton gauge shift produces W^μ = (κ_p − κ_e)(p₁^μ − p₃^μ). For any non-forward scattering (p₁ ≠ p₃), W^μ vanishes if and only if κ_e = κ_p: Lorentz invariance of massless spin-2 particles forces universal free fall.",
        "reveal_es": "Como la conservación del cuadrimpulso fija p₄^μ = p₁^μ + p₂^μ − p₃^μ, la variación gauge del gravitón blando produce W^μ = (κ_p − κ_e)(p₁^μ − p₃^μ). Para cualquier dispersión no frontal (p₁ ≠ p₃), W^μ se anula si y solo si κ_e = κ_p: la invariancia de Lorentz para partículas sin masa de espín 2 exige la caída libre universal.",
    },
    "sections": [
        {"type": "h2", "id": "soft", "en": "I · Universal free fall from the infrared S-matrix", "es": "I · Caída libre universal desde la matriz S infrarroja", "short_en": "I · Soft Theorems", "short_es": "I · Teoremas Blandos"},
        P(
            C("MEASURED", [MICRO, EOT08],
              "From low Earth orbit to the laboratory bench, matter falls at one rate in a gravitational field: in low Earth orbit the "
              "MICROSCOPE drag-free differential accelerometer bounds the Eötvös ratio between platinum-rhodium and titanium cylinders to "
              "η = (−1.5 ± 2.7)×10⁻¹⁵, while rotating beryllium–titanium torsion pendulums in the Seattle Eöt-Wash laboratory bound "
              "composition-dependent accelerations toward Earth to η = (0.3 ± 1.8)×10⁻¹³.",
              "De la órbita terrestre baja a la mesa de laboratorio, la materia cae al mismo ritmo en un campo gravitacional: en órbita "
              "terrestre baja el acelerómetro diferencial sin arrastre MICROSCOPE acota la razón de Eötvös entre cilindros de platino-rodio y "
              "titanio en η = (−1.5 ± 2.7)×10⁻¹⁵, mientras que péndulos rotatorios de torsión de berilio y titanio en el laboratorio Eöt-Wash "
              "de Seattle acotan aceleraciones dependientes de la composición hacia la Tierra en η = (0.3 ± 1.8)×10⁻¹³.",
              scope=EMP_SCOPE),
            T(" On T.01 through T.03 Einstein treated that universality as the foundational postulate that turns gravity into proper-time geometry. "
              "Half a century later, Steven Weinberg asked the inverse question: if one starts not from curved geometry, but from Lorentz-invariant "
              "quantum scattering of massless particles in flat spacetime, what couplings are mathematically consistent as the boson frequency ω → 0?",
              " De T.01 a T.03 Einstein tomó esa universalidad como el postulado fundacional que convierte la gravedad en geometría del tiempo propio. "
              "Medio siglo después, Steven Weinberg planteó la pregunta inversa: si uno parte no de la geometría curva, sino de la dispersión cuántica "
              "invariante de Lorentz de partículas sin masa en espaciotiempo plano, ¿qué acoplamientos son matemáticamente consistentes cuando la frecuencia del bosón ω → 0?"),
        ),
        P(
            C("DERIVED", [W64, W65, MICRO],
              "In 1964 and 1965 Weinberg proved that when a soft massless boson of momentum q^μ → 0 is emitted from n external scattering legs "
              "(incoming sign η_a = −1, outgoing sign η_a = +1, conserved momenta ∑_a η_a p_a^μ = 0), decoupling unphysical longitudinal "
              "polarizations imposes a strict hierarchy by spin s: for spin s = 1 (ε_μ → ε_μ + q_μ), the Ward residual ∑_a η_a q_a = 0 enforces "
              "additive charge conservation; for spin s = 2 (ε_{μν} → ε_{μν} + q_{(μ} Λ_{ν)}), the vector Ward residual W^μ = ∑_a η_a κ_a p_a^μ = 0 "
              "has linear solution κ_a = κ = √(32π G / c⁴) because external 4-momenta share no linear relation beyond ∑_a η_a p_a^μ = 0, deriving "
              "η = 0 from infrared Lorentz invariance; and for massless higher spins s ≥ 3, symmetric products ∑_a η_a g_a p_a^{μ₁}⋯p_a^{μ_{s−1}} = 0 "
              "are linearly independent across generic scattering angles, forcing g_a = 0 and ruling out macroscopic 1/r² forces of spin 3 or higher.",
              "En 1964 y 1965 Weinberg demostró que cuando un bosón blando sin masa con momento q^μ → 0 se emite desde n patas externas de dispersión "
              "(signo entrante η_a = −1, signo saliente η_a = +1, momentos conservados ∑_a η_a p_a^μ = 0), desacoplar las polarizaciones longitudinales "
              "no físicas impone una jerarquía estricta según el espín s: para espín s = 1 (ε_μ → ε_μ + q_μ), el residuo de Ward ∑_a η_a q_a = 0 exige "
              "la conservación aditiva de la carga; para espín s = 2 (ε_{μν} → ε_{μν} + q_{(μ} Λ_{ν)}), el residuo vectorial de Ward W^μ = ∑_a η_a κ_a p_a^μ = 0 "
              "admite como solución lineal κ_a = κ = √(32π G / c⁴) porque los 4-momentos externos no guardan otra relación lineal más allá de "
              "∑_a η_a p_a^μ = 0, derivando η = 0 desde la invariancia infrarroja de Lorentz; y para espines sin masa s ≥ 3, los productos simétricos "
              "∑_a η_a g_a p_a^{μ₁}⋯p_a^{μ_{s−1}} = 0 son linealmente independientes en ángulos genéricos de dispersión, forzando g_a = 0 y descartando "
              "fuerzas macroscópicas 1/r² de espín 3 o superior.",
              parent=MICRO),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("Why are there long-range electric forces (spin 1) and gravitational forces (spin 2) in nature, yet no long-range spin-3 force—and why "
                 "can electricity have positive, negative, and neutral particles while gravity pulls every particle in proportion to its energy? "
                 "Because a massless particle moving at the speed of light has only two transverse polarization directions, while four-dimensional "
                 "spacetime vectors have four components.",
                 "¿Por qué existen en la naturaleza fuerzas eléctricas de largo alcance (espín 1) y fuerzas gravitacionales (espín 2), pero ninguna "
                 "fuerza macroscópica de espín 3, y por qué la electricidad admite partículas positivas, negativas y neutras mientras la gravedad tira "
                 "de cada partícula en proporción exacta a su energía? Porque una partícula sin masa que viaja a la velocidad de la luz solo tiene dos "
                 "polarizaciones transversales, mientras que los cuadrivectores del espaciotiempo tienen cuatro componentes.")),
             P(T("For physics to make the same predictions for every moving observer, the extra longitudinal components must cancel out of every "
                 "collision. For spin 1, they cancel whenever total electric charge before the collision equals total charge after. For spin 2, the "
                 "cancellation multiplies each particle's coupling by its momentum vector—and since total momentum is the conserved vector in a "
                 "collision, the math works if every particle shares the exact same gravitational coupling. For spin 3, it would require conserved "
                 "squares of momentum, which collisions do not conserve, so the coupling must be zero.",
                 "Para que la física dé las mismas predicciones a cualquier observador en movimiento, las componentes longitudinales sobrantes deben "
                 "cancelarse en toda colisión. Para espín 1, se cancelan siempre que la carga eléctrica total antes del choque iguale a la posterior. "
                 "Para espín 2, la cancelación multiplica el acoplamiento de cada partícula por su vector de momento, y como el momento total es el "
                 "vector conservado en un choque, la suma cierra si cada partícula comparte exactamente el mismo acoplamiento gravitacional. Para espín 3 "
                 "harían falta cuadrados de momento conservados, que los choques no conservan, así que el acoplamiento debe ser cero.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: two floating buoys on calm water after a heavy ship passes far offshore. While the wake rolls through, the buoys "
                 "bob back and forth; in an ordinary linear ripple they return to their starting separation, whereas in Einstein's nonlinear gravity "
                 "the energy carried by the wave packet itself permanently shifts the baseline between two free-falling mirrors—leaving a tiny step "
                 "stamped into proper distance after the ringing stops.",
                 "Analogía cotidiana: dos boyas flotando en aguas calmas tras el paso lejano de un barco pesado. Mientras cruza la estela, las boyas "
                 "oscilan de ida y vuelta; en una onda lineal ordinaria vuelven a su separación inicial, mientras que en la gravedad no lineal de "
                 "Einstein la propia energía transportada por el tren de ondas desplaza de forma permanente la línea base entre dos espejos en caída "
                 "libre, dejando un pequeño escalón grabado en la distancia propia cuando cesa la vibración.")),
             P(T("How the controls work in plain words: the first two sliders set the radiated merger energy E_rad (in solar-mass energy units M_⊙ c²) "
                 "and luminosity distance D_L (in megaparsecs), updating the permanent gravitational-wave memory strain Δh and arm shift ΔL on 4 km "
                 "LIGO and 2.5 million km LISA baselines. The third slider varies the integer number of quark colours N_c from 1 to 5 in the anomaly "
                 "ledger; at N_c = 3 all four gauge and gravitational traces hit 0. The knockout button activates κ_e ≠ κ_p and N_c = 2 simultaneously.",
                 "Cómo funcionan los controles en palabras sencillas: los dos primeros deslizadores fijan la energía radiada en la fusión E_rad (en "
                 "unidades de masa solar M_⊙ c²) y la distancia de luminosidad D_L (en megapársecs), actualizando el escalón permanente de memoria Δh "
                 "y el corrimiento ΔL en líneas base de 4 km (LIGO) y 2.5 millones de km (LISA). El tercer deslizador cambia el entero de colores de "
                 "quarks N_c de 1 a 5; en N_c = 3 las cuatro trazas gauge y gravitacionales caen en 0. El botón de apagado activa κ_e ≠ κ_p y N_c = 2.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "memory", "en": "II · Gravitational-wave memory and permanent baseline holonomy", "es": "II · Memoria de ondas gravitacionales y holonomía permanente de línea base", "short_en": "II · Memory Step", "short_es": "II · Escalón de Memoria"},
        {"type": "equation", "text": "Δh_char^mem = G E_rad / (c⁴ D_L),   Δh_+^mem(ι) = Δh_char^mem · sin²ι (17 + cos²ι) / 24,   ΔL / L₀ = (1/2) Δh_+^mem"},
        P(
            C("MEASURED", [ABB16, ISI21],
              "In September 2015 the twin 4000 m LIGO interferometers observed GW150914 from the inspiral and merger of two black holes at luminosity "
              "distance D_L ≈ 410 Mpc, radiating E_rad ≈ 3.0 M_⊙ c² into gravitational waves and settling into a 62 M_⊙ Kerr remnant whose pre- and "
              "post-merger horizon areas satisfy Hawking's area increase theorem in time-domain overtone analyses.",
              "En septiembre de 2015 los dos interferómetros gemelos de 4000 m de LIGO observaron GW150914 por la inspiración y fusión de dos agujeros "
              "negros a una distancia de luminosidad D_L ≈ 410 Mpc, radiando E_rad ≈ 3.0 M_⊙ c² en ondas gravitacionales y asentándose en un remanente "
              "de Kerr de 62 M_⊙ cuyas áreas de horizonte antes y después de la fusión cumplen el teorema del área de Hawking en análisis temporales.",
              scope=EMP_SCOPE),
            T(" ", " "),
            C("SINGLE RESULT", [LVK25],
              "A decade later, in GW250114, the LIGO–Virgo–KAGRA collaboration recorded a binary black hole merger at network signal-to-noise ratio 80 "
              "near D_L ≈ 400 Mpc, resolving two Kerr ringdown modes within 30% of the remnant frequency and damping predictions.",
              "Una década después, en GW250114, la colaboración LIGO–Virgo–KAGRA registró una fusión binaria de agujeros negros con relación señal a "
              "ruido de red de 80 cerca de D_L ≈ 400 Mpc, resolviendo dos modos de relajación de Kerr dentro del 30% de las predicciones del remanente.",
              scope=EMP_SCOPE),
        ),
        P(
            C("DERIVED", [CHR91, FAV09, STR16, ABB16],
              "Demetrios Christodoulou proved in 1991 from the exact asymptotically flat vacuum Einstein equations that the stress-energy carried to "
              "null infinity by gravitational waves themselves sources a permanent DC transverse-traceless strain offset Δh_+^mem; for a quasi-circular "
              "binary Favata's 2009 leading-quadrupole expression, written with the radiated energy, is Δh_+^mem = Δh_char sin²ι (17 + cos²ι) / 24 with "
              "Δh_char = G E_rad / (c⁴ D_L), shifting the proper separation of free-falling mirrors or optical clocks by ΔL / L₀ = (1/2) Δh_+^mem; "
              "in 2016 Andrew Strominger and Alexander Zhiboedov proved that this displacement memory step, Bondi–Metzner–Sachs (BMS) supertranslation "
              "conservation at null infinity, and Weinberg's soft-graviton pole are Fourier and Ward transforms of one infrared triangle.",
              "Demetrios Christodoulou demostró en 1991 a partir de las ecuaciones exactas de Einstein en el vacío asintóticamente plano que la "
              "energía-momento transportada al infinito nulo por las propias ondas gravitacionales genera un escalón permanente de deformación "
              "transversal sin traza Δh_+^mem; para una binaria cuasicircular la expresión cuadrupolar dominante de Favata (2009), escrita con la energía radiada, es Δh_+^mem = Δh_char sin²ι (17 + cos²ι) / 24 con Δh_char = G E_rad / (c⁴ D_L), desplazando la separación propia entre espejos "
              "o relojes en caída libre por ΔL / L₀ = (1/2) Δh_+^mem; en 2016 Andrew Strominger y Alexander Zhiboedov demostraron que este escalón de "
              "memoria, la conservación por supertraslaciones de Bondi–Metzner–Sachs (BMS) en el infinito nulo y el polo de gravitón blando de Weinberg "
              "son transformadas de Fourier y de Ward de un mismo triángulo infrarrojo.",
              parent=ABB16),
            T(" Evaluated on our kernel's fiducial GW150914 benchmark (E_rad = 3.0 M_⊙ c², D_L = 410 Mpc, L₀ = 4000 m), the characteristic step is "
              "Δh_char = 3.50×10⁻²² (ΔL_char = 7.00×10⁻¹⁹ m, or edge-on quadrupole Δh_+ = 2.48×10⁻²² and ΔL = 4.96×10⁻¹⁹ m), and on a fiducial "
              "400 Mpc GW250114-scale benchmark (at 3.0 M_⊙ c² fiducial radiated energy) Δh_char = 3.59×10⁻²² (ΔL_char = 7.18×10⁻¹⁹ m)—with "
              "5-point Gauss–Legendre quadrature of dE_rad/dt matching the closed-form hyperbolic-tangent step within 1.3×10⁻¹⁶.",
              " Evaluado en el punto fiducial de nuestro kernel para GW150914 (E_rad = 3.0 M_⊙ c², D_L = 410 Mpc, L₀ = 4000 m), el escalón característico "
              "es Δh_char = 3.50×10⁻²² (ΔL_char = 7.00×10⁻¹⁹ m, o cuadrupolar de canto Δh_+ = 2.48×10⁻²² y ΔL = 4.96×10⁻¹⁹ m), y en un punto fiducial "
              "de escala GW250114 a 400 Mpc (con 3.0 M_⊙ c² de energía radiada fiducial) Δh_char = 3.59×10⁻²² (ΔL_char = 7.18×10⁻¹⁹ m), coincidiendo "
              "la cuadratura de Gauss y Legendre de 5 puntos de dE_rad/dt con el escalón cerrado de tangente hiperbólica dentro de 1.3×10⁻¹⁶."),
        ),
        P(
            C("BOUND", [HUB20],
              "Because terrestrial test masses hang as pendulums restored below ~10 Hz while seismic and Newtonian gravity-gradient noise rise toward "
              "0 Hz, nonlinear displacement memory has not yet been isolated in a single event: LIGO/Virgo catalog searches by Hübner, Talbot, Lasky "
              "and Thrane (2020) place observational upper bounds on the memory signal and project coherent ensemble detection across roughly 2000 "
              "O3-class binary black hole detections.",
              "Como las masas de prueba terrestres cuelgan como péndulos restaurados por debajo de ~10 Hz mientras el ruido sísmico y newtoniano sube "
              "hacia 0 Hz, la memoria no lineal de desplazamiento aún no se ha aislado en un evento individual: las búsquedas en catálogos de LIGO y "
              "Virgo por Hübner, Talbot, Lasky y Thrane (2020) fijan cotas superiores observacionales sobre la señal de memoria y proyectan su "
              "detección coherente acumulando cerca de 2000 detecciones binarias de clase O3.",
              scope=EMP_SCOPE),
            T(" Across a space-borne 2.5×10⁹ m LISA baseline free of terrestrial seismic walls, that same 3.50×10⁻²² strain scale corresponds to a "
              "0.44 pm proper separation step.",
              " A través de una línea base espacial tipo LISA de 2.5×10⁹ m libre del muro sísmico terrestre, esa misma escala de deformación de "
              "3.50×10⁻²² equivale a un escalón de separación propia de 0.44 pm."),
        ),
        {"type": "h2", "id": "anomaly", "en": "III · Chiral and mixed gauge–gravitational anomaly cancellation", "es": "III · Cancelación de anomalías quirales y mixtas gauge-gravitacionales", "short_en": "III · Anomaly Bridge", "short_es": "III · Puente de Anomalías"},
        {"type": "equation", "text": "Tr[6Y] = 2N_c − 4N_c + 2N_c − 6 + 6 = 0,   2 Tr[T_{SU(2)}²(6Y)] = N_c − 3 = 0,   Tr[(6Y)³] = −54(N_c − 3) = 0"},
        P(
            C("DERIVED", [ADL69, DEL72, AGW84, MICRO],
              "Gravity enters consistent chiral quantum field theory a second time at one loop: Adler (1969) showed that fermion triangle diagrams can "
              "break classical chiral gauge symmetries, and Delbourgo and Salam (1972) computed the fermion triangle with one chiral current and two external gravitons; applied to hypercharge, "
              "as in Alvarez-Gaumé and Witten's 1984 treatment of gravitational anomalies, the U(1)_Y current stays conserved in a gravitational "
              "background only if the sum of left-handed Weyl hypercharges vanishes, Tr[Y] = 0. Parameterizing one Standard Model generation by integer hypercharges 6Y "
              "(Q_L: 2N_c at +1, u_R^c: N_c at −4, d_R^c: N_c at +2, L_L: 2 at −3, e_R^c: 1 at +6) gives Tr[6Y] = 0 and 2 Tr[T_{SU(3)}²(6Y)] = "
              "2(+1) − 4 + 2 = 0, while 2 Tr[T_{SU(2)}²(6Y)] = N_c − 3 and Tr[(6Y)³] = −54(N_c − 3) vanish, with the hypercharges held at these observed values, if and only if N_c = 3.",
              "La gravedad entra por segunda vez en la consistencia de las teorías cuánticas quirales a un lazo: Adler (1969) mostró que los diagramas "
              "triangulares de fermiones pueden romper simetrías gauge quirales clásicas, y Delbourgo y Salam (1972) calcularon el triángulo de fermiones con una corriente quiral y dos gravitones externos; aplicado a la hipercarga, "
              "como en el tratamiento de las anomalías gravitacionales de Alvarez-Gaumé y Witten (1984), la corriente U(1)_Y solo se conserva en un fondo "
              "gravitacional si se anula la suma de hipercargas de Weyl zurdas, Tr[Y] = 0. Parametrizar una generación del Modelo Estándar "
              "con hipercargas enteras 6Y (Q_L: 2N_c en +1, u_R^c: N_c en −4, d_R^c: N_c en +2, L_L: 2 en −3, e_R^c: 1 en +6) arroja Tr[6Y] = 0 y "
              "2 Tr[T_{SU(3)}²(6Y)] = 2(+1) − 4 + 2 = 0, mientras que 2 Tr[T_{SU(2)}²(6Y)] = N_c − 3 y Tr[(6Y)³] = −54(N_c − 3) se anulan, con las hipercargas fijas en estos valores observados, si y solo si N_c = 3.",
              parent=MICRO),
            T(" If the right-handed electron singlet e_R^c is omitted, the mixed gravitational trace jumps to Tr[6Y] = −6 ≠ 0; if quark colour "
              "multiplicity is perturbed to N_c = 2, SU(2)_L² × U(1)_Y fails at −1 and cubic U(1)_Y³ fails at +54.",
              " Si se omite el singlete electrónico diestro e_R^c, la traza mixta gravitacional salta a Tr[6Y] = −6 ≠ 0; si la multiplicidad de color "
              "de los quarks se perturba a N_c = 2, SU(2)_L² × U(1)_Y falla en −1 y la traza cúbica U(1)_Y³ falla en +54."),
        ),
        P(
            C("SINGLE RESULT", [TOOBY25],
              "In 2025 Joseph Tooby-Smith formalized the Standard Model rational and integer hypercharge anomaly equations in the Lean 4 theorem prover "
              "within PhysLean (HepLean).",
              "En 2025 Joseph Tooby-Smith formalizó las ecuaciones racionales y enteras de cancelación de anomalías de hipercarga del Modelo Estándar "
              "en el demostrador de teoremas Lean 4 dentro de PhysLean (HepLean).",
              scope=EMP_SCOPE),
            T(" Alongside our Python kernel, this step ships a self-contained pure core Lean 4 Prelude file (HolonomySoftAnomaly.lean, 0 external "
              "imports, 0 sorry axioms, 12 theorems) verifying SI dimensional exponents, Weinberg's 2 → 2 soft-photon, soft-graviton, and spin-3 "
              "identities, and the exact N_c = 3 anomaly equivalences.",
              " Junto con nuestro kernel en Python, este paso incluye un archivo autocontenido en Lean 4 Prelude puro (HolonomySoftAnomaly.lean, "
              "0 importaciones externas, 0 axiomas sorry, 12 teoremas) que verifica los exponentes dimensionales SI, las identidades blandas 2 → 2 "
              "de Weinberg para espines 1, 2 y 3, y las equivalencias exactas de anomalías en N_c = 3."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "open", "en": "IV · What infrared consistency settles, and what remains open at the Planck and tabletop scales", "es": "IV · Lo que zanja la consistencia infrarroja, y lo que sigue abierto en las escalas de Planck y de mesa", "short_en": "IV · Open Horizon", "short_es": "IV · Horizonte Abierto"},
        P(
            C("MEASURED", [LEE20, TAN20],
              "Walking back across the fourteen-step track shows both the reach and the strict boundary of infrared consistency: at sub-millimetre "
              "distances, precision torsion pendulums at Seattle Eöt-Wash (52 µm gap, 38.6 µm unit-strength Yukawa limit) and Wuhan HUST (48 µm scale) "
              "confirm Newton's inverse-square attraction without deviation down to tens of micrometres.",
              "Recorrer de vuelta los catorce pasos de la serie muestra tanto el alcance como la frontera estricta de la consistencia infrarroja: en "
              "distancias submilimétricas, los péndulos de torsión de precisión en Eöt-Wash de Seattle (brecha de 52 µm, límite de Yukawa de intensidad "
              "unitaria en 38.6 µm) y HUST en Wuhan (escala de 48 µm) confirman la atracción de inverso del cuadrado sin desviaciones hasta decenas de micrómetros.",
              scope=EMP_SCOPE),
            T(" ", " "),
            C("DERIVED", [LEE21, DIOSI87, PENROSE96, LEE20, SCH24],
              "Recasting those published 95% sub-millimetre limits onto smeared Diósi–Penrose potentials on T.05 excludes smearing widths above 33 µm, "
              "while mapping parallel side-by-side interferometers (crossing the 73.14 µm parallel hybrid reach down into a narrow 13.6 µm to 33 µm "
              "screened window) isolates the exact regime where coherent quantum phase and objective collapse make competing predictions.",
              "Proyectar esos límites submilimétricos publicados al 95% sobre potenciales suavizados de Diósi–Penrose en T.05 excluye anchos de "
              "suavizado por encima de 33 µm, mientras que el mapeo de interferómetros paralelos lado a lado (bajando desde el alcance híbrido paralelo "
              "de 73.14 µm hasta una estrecha ventana apantallada de 13.6 µm a 33 µm) aísla el régimen exacto donde la fase cuántica coherente y el "
              "colapso objetivo hacen predicciones contrapuestas.",
              parent=LEE20,
              kernel="parallel_hybrid_horizon_um"),
        ),
        P(
            C("PROPOSED", [BOSE17, SCH24],
              "Whether micron-scale masses held in spatial superposition generate bipartite or multipartite gravitational entanglement—as proposed in "
              "2017 and refined in 2024 screened diamond geometries—remains unmeasured in the laboratory.",
              "Si masas micrométricas sostenidas en superposición espacial generan entrelazamiento gravitacional bipartito o multipartito —como se "
              "propuso en 2017 y se refinó en las geometrías apantalladas de microdiamantes de 2024— sigue sin medirse en el laboratorio."),
            T(" ", " "),
            C("SINGLE RESULT", [ZH24],
              "Meanwhile, on the clock frontier, phase-coherent vacuum-ultraviolet frequency combs in 2024 linked the ²²⁹Th nuclear isomeric transition "
              "directly to an ⁸⁷Sr optical lattice clock, opening optical–nuclear clock networks sensitive to both proper-time curvature and nuclear "
              "binding couplings.",
              "Mientras tanto, en la frontera de los relojes, peines de frecuencia coherentes en el ultravioleta de vacío enlazaron en 2024 la "
              "transición isomérica nuclear de ²²⁹Th directamente con un reloj de red óptica de ⁸⁷Sr, abriendo redes de relojes ópticos y nucleares "
              "sensibles tanto a la curvatura del tiempo propio como a los acoplamientos nucleares.",
              scope=EMP_SCOPE),
            T(" Together with the Cross-Scale Synthesis Companions—ES.07 on the 73.14 µm parallel Diósi–Penrose hybrid horizon, ES.08 on the Modified "
              "Gram–Schmidt Fisher Schur-complement recast (σ_95 ≤ 33.08 µm under nuisance marginalization), and ES.09 on tripartite Mermin entanglement "
              "witnesses (⟨M_3⟩ = 3.6741 > 2√2) alongside ¹⁷³Yb, ⁸⁷Sr, and ²²⁹Th clock architectures—those calculations map the falsifiable laboratory "
              "corridor above the infrared theorems.",
              " Junto con los ensayos de síntesis transversal —ES.07 sobre el horizonte híbrido paralelo de Diósi–Penrose en 73.14 µm, ES.08 sobre la "
              "proyección de complemento de Schur de Fisher con Gram–Schmidt modificado (σ_95 ≤ 33.08 µm tras marginalizar parámetros de molestia) y "
              "ES.09 sobre testigos tripartitos de Mermin (⟨M_3⟩ = 3.6741 > 2√2) junto a relojes de ¹⁷³Yb, ⁸⁷Sr y ²²⁹Th—, esos cálculos trazan el "
              "corredor experimental falsable por encima de los teoremas infrarrojos."),
        ),
        P(
            C("OPEN", [W64, BOSE17],
              "Infrared S-matrix theorems, permanent gravitational-wave memory, and one-loop gauge–gravitational anomaly cancellation constrain every "
              "consistent low-energy effective theory from below, yet they do not select the ultraviolet completion of gravity near the Planck scale "
              "E ~ M_P c² or settle whether superposed masses entangle coherently in a tabletop interferometer—that ultraviolet and mesoscopic bridge "
              "remains open.",
              "Los teoremas infrarrojos de la matriz S, la memoria permanente de ondas gravitacionales y la cancelación a un lazo de anomalías mixtas "
              "restringen desde abajo toda teoría efectiva consistente de baja energía, pero no seleccionan la completitud ultravioleta de la gravedad "
              "cerca de la escala de Planck E ~ M_P c² ni deciden si masas en superposición se entrelazan coherentemente en un interferómetro de mesa: "
              "ese puente ultravioleta y mesoscópico permanece abierto."),
        ),
        {"type": "change_box",
         "items": [
             ("A statistically significant ensemble or single-event observation of permanent DC gravitational-wave displacement memory in LIGO–Virgo–KAGRA, Cosmic Explorer, Einstein Telescope, or LISA would move gravitational memory from DERIVED / BOUND to MEASURED.",
              "Una observación estadísticamente significativa, individual o en conjunto, de la memoria permanente de desplazamiento de ondas gravitacionales en LIGO–Virgo–KAGRA, Cosmic Explorer, Einstein Telescope o LISA movería la memoria gravitacional de DERIVADO / COTA a MEDIDO."),
             ("Discovering a fourth chiral fermion family with anomalous hypercharges or any composition-dependent violation of universal free fall (η ≠ 0) would force revision of the low-energy gauge–gravity effective theory.",
              "Descubrir una cuarta familia quiral de fermiones con hipercargas anómalas o cualquier violación dependiente de la composición en la caída libre universal (η ≠ 0) obligaría a revisar la teoría efectiva de baja energía entre campos gauge y gravedad."),
             ("If the planted-defect run (κ_e / κ_p = 1 + 10⁻⁵ and N_c = 2) ever passed the soft-graviton Ward gate or anomaly gate, or if Gauss–Legendre memory quadrature diverged from G E_rad / (c⁴ D_L) beyond 1e-12, the verifier exits 1 and halts the build.",
              "Si la corrida con defecto plantado (κ_e / κ_p = 1 + 10⁻⁵ y N_c = 2) pasara alguna vez la compuerta de Ward o de anomalías, o si la cuadratura de Gauss y Legendre divergiera de G E_rad / (c⁴ D_L) más allá de 1e-12, el verificador sale con código 1 y detiene la construcción."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · Weinberg s = 1, 2, 3 soft Ward solver", "Etapa 1 · Solucionador de identidades blandas de Ward s = 1, 2, 3",
         "On relativistic non-collinear e⁻ p⁺ → e⁻ p⁺ kinematics (E_cm = 5.17 GeV), the kernel verifies ||∑ η_a p_a^μ|| = 0, spin-1 charge residual 0, spin-2 Ward residual ||W^μ||/E_cm = 0 at κ_e = κ_p (Gram det = 464.4 > 0), and spin-3 rank-4 quadratic obstruction norm 0.367 > 0.",
         "Sobre cinemática relativista no colineal e⁻ p⁺ → e⁻ p⁺ (E_cm = 5.17 GeV), el kernel verifica ||∑ η_a p_a^μ|| = 0, residuo de carga de espín 1 igual a 0, residuo de Ward de espín 2 ||W^μ||/E_cm = 0 en κ_e = κ_p (det de Gram = 464.4 > 0) y norma de obstrucción cuadrática de espín 3 igual a 0.367 > 0."),
        ("Stage 2 · Christodoulou memory step vs GL5 quadrature", "Etapa 2 · Escalón de memoria de Christodoulou frente a cuadratura GL5",
         "Composite 5-point Gauss–Legendre integration of d(Δh)/dt = (G/c⁴D_L) dE_rad/dt across [-22τ_m, +22τ_m] matches the closed-form step Δh_char = 3.502×10⁻²² (ΔL_char = 7.003×10⁻¹⁹ m on 4 km) within 1.34×10⁻¹⁶.",
         "La integración compuesta de Gauss y Legendre de 5 puntos de d(Δh)/dt = (G/c⁴D_L) dE_rad/dt en [-22τ_m, +22τ_m] coincide con el escalón cerrado Δh_char = 3.502×10⁻²² (ΔL_char = 7.003×10⁻¹⁹ m en 4 km) dentro de 1.34×10⁻¹⁶."),
        ("Stage 3 · Chiral & mixed gravitational anomaly polynomials + Lean 4 Prelude", "Etapa 3 · Polinomios de anomalías quirales y gravitacionales + Lean 4 Prelude",
         "Evaluates Tr[6Y], 2Tr[T_{SU(3)}²(6Y)], 2Tr[T_{SU(2)}²(6Y)] = N_c − 3, and Tr[(6Y)³] = −54(N_c − 3) across N_c ∈ {1..5}, and audits HolonomySoftAnomaly.lean (0 imports, 0 sorry, 12 theorems).",
         "Evalúa Tr[6Y], 2Tr[T_{SU(3)}²(6Y)], 2Tr[T_{SU(2)}²(6Y)] = N_c − 3 y Tr[(6Y)³] = −54(N_c − 3) en N_c ∈ {1..5}, y audita HolonomySoftAnomaly.lean (0 importaciones, 0 sorry, 12 teoremas)."),
        ("Stage 4 · Dual planted-defect knockout", "Etapa 4 · Apagado doble por defecto plantado",
         "Setting κ_e / κ_p = 1 + 10⁻⁵ raises ||W^μ||/E_cm to 3.45×10⁻⁶ and setting N_c = 2 yields Tr[SU(2)²(6Y)] = −1 and Tr[(6Y)³] = +54; --planted-defect prints FAIL to stderr and exits 1.",
         "Fijar κ_e / κ_p = 1 + 10⁻⁵ eleva ||W^μ||/E_cm a 3.45×10⁻⁶ y fijar N_c = 2 arroja Tr[SU(2)²(6Y)] = −1 y Tr[(6Y)³] = +54; --planted-defect imprime FAIL en stderr y termina con código 1."),
    ],
    "sidenotes": [
        ("SIDENOTE T.13-A · STROMINGER'S INFRARED TRIANGLE (SOFT THEOREMS ↔ MEMORY ↔ BMS)", "NOTA T.13-A · EL TRIÁNGULO INFRARROJO DE STROMINGER (TEOREMAS BLANDOS ↔ MEMORIA ↔ BMS)",
         "At future null infinity I⁺, asymptotically flat spacetimes admit an infinite-dimensional group of angle-dependent Bondi–Metzner–Sachs (BMS) supertranslations. Strominger and Zhiboedov (2016) showed that BMS supertranslation charge conservation gives Christodoulou's displacement memory in the time domain and Weinberg's soft-graviton theorem under a Fourier transform.",
         "En el infinito nulo futuro I⁺, los espaciotiempos asintóticamente planos admiten un grupo infinito-dimensional de supertraslaciones de Bondi–Metzner–Sachs (BMS) dependientes del ángulo. Strominger y Zhiboedov (2016) mostraron que la conservación de la carga de supertraslación BMS produce la memoria de Christodoulou en el dominio temporal y el teorema blando de Weinberg bajo transformada de Fourier."),
        ("SIDENOTE T.13-B · WHY INFRARED CONSISTENCY IS NOT AN ULTRAVIOLET COMPLETION", "NOTA T.13-B · POR QUÉ LA CONSISTENCIA INFRARROJA NO ES UNA COMPLETITUD ULTRAVIOLETA",
         "Soft Ward identities and one-loop triangle anomalies depend only on massless spectrum and low-energy charges, remaining insensitive to Planck-suppressed higher-curvature operators (R², R_{μνρσ}² / M_P²). They act as exact necessary conditions from below without uniquely determining UV quantum gravity above.",
         "Las identidades blandas de Ward y las anomalías triangulares a un lazo dependen únicamente del espectro sin masa y de las cargas de baja energía, siendo insensibles a operadores de curvatura superior suprimidos por la escala de Planck (R², R_{μνρσ}² / M_P²). Actúan como condiciones necesarias exactas desde abajo sin determinar de forma única la gravedad cuántica UV por arriba."),
    ],
    "sources": [
        ("Weinberg, S. (1964). Photons and gravitons in S-matrix theory: Derivation of charge conservation and equality of gravitational and inertial mass. Physical Review, 135(4B), B1049–B1056.", "10.1103/PhysRev.135.B1049"),
        ("Weinberg, S. (1965). Infrared photons and gravitons. Physical Review, 140(2B), B516–B524.", "10.1103/PhysRev.140.B516"),
        ("Adler, S. L. (1969). Axial-vector vertex in spinor electrodynamics. Physical Review, 177(5), 2426–2438.", "10.1103/PhysRev.177.2426"),
        ("Delbourgo, R., & Salam, A. (1972). The gravitational correction to PCAC. Physics Letters B, 40(3), 381–382.", "10.1016/0370-2693(72)90825-8"),
        ("Alvarez-Gaumé, L., & Witten, E. (1984). Gravitational anomalies. Nuclear Physics B, 234(2), 269–330.", "10.1016/0550-3213(84)90066-X"),
        ("Favata, M. (2009). Nonlinear gravitational-wave memory from binary black hole mergers. The Astrophysical Journal Letters, 696(2), L159–L162.", "10.1088/0004-637X/696/2/L159"),
        ("Christodoulou, D. (1991). Nonlinear nature of gravitation and gravitational-wave experiments. Physical Review Letters, 67(12), 1486–1489.", "10.1103/PhysRevLett.67.1486"),
        ("Strominger, A., & Zhiboedov, A. (2016). Gravitational memory, BMS supertranslations and soft theorems. Journal of High Energy Physics, 2016(1), 086.", "10.1007/JHEP01(2016)086"),
        ("Hübner, M., Talbot, C., Lasky, P. D., & Thrane, E. (2020). Measuring gravitational-wave memory in the first LIGO/Virgo gravitational-wave transient catalog. Physical Review D, 101(2), 023011.", "10.1103/PhysRevD.101.023011"),
        ("Touboul, P., et al. (MICROSCOPE Collaboration). (2022). MICROSCOPE mission: Final results of the test of the equivalence principle. Physical Review Letters, 129(12), 121102.", "10.1103/PhysRevLett.129.121102"),
        ("Schlamminger, S., Choi, K.-Y., Wagner, T. A., Gundlach, J. H., & Adelberger, E. G. (2008). Test of the equivalence principle using a rotating torsion balance. Physical Review Letters, 100(4), 041101.", "10.1103/PhysRevLett.100.041101"),
        ("Abbott, B. P., et al. (LIGO Scientific Collaboration and Virgo Collaboration). (2016). Observation of gravitational waves from a binary black hole merger. Physical Review Letters, 116(6), 061102.", "10.1103/PhysRevLett.116.061102"),
        ("Isi, M., Farr, W. M., Giesler, M., Scheel, M. A., & Teukolsky, S. A. (2021). Testing the black-hole area law with GW150914. Physical Review Letters, 127(1), 011103.", "10.1103/PhysRevLett.127.011103"),
        ("LIGO Scientific, Virgo, and KAGRA Collaborations. (2025). GW250114: Testing Hawking's area law and the Kerr nature of black holes. Physical Review Letters.", "10.1103/kw5g-d732"),
        ("Lee, J. G., Adelberger, E. G., Cook, T. S., Fleischer, S. M., & Heckel, B. R. (2020). New test of the gravitational 1/r² law at separations down to 52 µm. Physical Review Letters, 124(10), 101101.", "10.1103/PhysRevLett.124.101101"),
        ("Lee, J. G., Adelberger, E. G., Marcoline, F. V., Terrano, W. A., & Heckel, B. R. (2021). The Fourier–Bessel expansion applied to experimental probes of gravity and feeble short-range interactions. Classical and Quantum Gravity, 38(8), 085020.", "10.1088/1361-6382/abebf2"),
        ("Tan, W.-H., et al. (2020). Improvement for testing the gravitational inverse-square law at the submillimeter range. Physical Review Letters, 124(5), 051301.", "10.1103/PhysRevLett.124.051301"),
        ("Bose, S., et al. (2017). Spin entanglement witness for quantum gravity. Physical Review Letters, 119(24), 240401.", "10.1103/PhysRevLett.119.240401"),
        ("Schut, M., Geraci, A., Bose, S., & Mazumdar, A. (2024). Micrometer-size spatial superpositions for the QGEM-protocol via screening and trapping. Physical Review Research, 6(1), 013199.", "10.1103/PhysRevResearch.6.013199"),
        ("Zhang, C., Ooi, T., Higgins, J. S., Doyle, J. F., von der Wense, L., Beeks, K., Leitner, A., Kazakov, G. A., Li, P., Thirolf, P. G., Schumm, T., & Ye, J. (2024). Frequency ratio of the ²²⁹ᵐTh nuclear isomeric transition and the ⁸⁷Sr atomic clock. Nature, 633, 63–70.", "10.1038/s41586-024-07839-6"),
        ("Tooby-Smith, J. (2025). HepLean: Digitalising high energy physics. Computer Physics Communications, 308, 109457.", "10.1016/j.cpc.2024.109457"),
    ],
}
