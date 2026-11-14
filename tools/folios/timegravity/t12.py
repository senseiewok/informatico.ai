# -*- coding: utf-8 -*-
"""Time & Gravity · T.12 — Two clocks that only meet in gravity.

Instrument: a two-clock gravitational-redshift network (baseline d_c, impact parameter b_1) recording the proper-time
step Δτ(T) = -(2 G M_DM / c² v_0) [arsinh(v_0 T / b_1) - arsinh(v_0 T / b_2)] of an electromagnetically transparent
mass (α_EM = 0, Λ_EM = 0), checked by composite 5-point Gauss-Legendre quadrature within 3.7e-16, alongside the
Planck 2018 dark-to-baryonic matter budget (Ω_c / Ω_b = 5.364) and co-located optical-clock portal bounds (d_e).
Knockout / planted defect: setting G_dark = 0 for the electromagnetically transparent mass violates the Equivalence
Principle and fails the trajectory quadrature check.
Verifier: skills/timegravity/t12/verify_t12_dark_clock.py.
"""
from __future__ import annotations

from ._model import C, P, T

SLUG = "t12"
CODE = "T.12"

PLANCK = "T12-PLANCK2020"
CLOWE = "T12-CLOWE2006"
MICRO = "T03-MICRO2022"
PR60 = "T01-PR1960"
CHOU = "T01-CHOU2010"
EIN16 = "T03-EIN1916"
JOOS = "T11-JOOS1985"
KEN20 = "T12-KENNEDY2020"
FIL23 = "T12-FILZINGER2023"
LZ23 = "T12-LZ2023"
CAR21 = "T12-CARNEY2020"

PAGE: dict = {
    "slug": SLUG,
    "code": CODE,
    "date": "2026-11-10",
    "order_label_en": "Step 13 of 14",
    "order_label_es": "Paso 13 de 14",
    "kicker_en": "Time & Gravity · T.12 · When the electromagnetic bath is silent, proper time still couples to every stress-energy tensor",
    "kicker_es": "Tiempo y Gravedad · T.12 · Cuando el baño electromagnético guarda silencio, el tiempo propio aún se acopla a todo tensor de energía-momento",
    "title_en": "Two Clocks That Only Meet in Gravity",
    "title_es": "Dos Relojes que Solo se Encuentran en la Gravedad",
    "standfirst_en": (
        "On T.11 the photon bath rendered a classical world by scattering off electric charges and dipoles, leaving anything with zero "
        "electromagnetic coupling unrecorded in light. Yet five-sixths of the gravitating matter in our universe is non-luminous. "
        "Because Einstein's metric couples universally to every stress-energy tensor, a sector that never scatters a photon still tilts the "
        "rate of proper time—requiring two spatially separated clocks to sense a purely gravitational transit, or co-located clocks of different "
        "atomic species to bound any non-gravitational portal."
    ),
    "standfirst_es": (
        "En T.11 el baño de fotones produjo un registro clásico al dispersarse sobre cargas y dipolos eléctricos, dejando sin huella óptica a todo "
        "lo que tenga acoplamiento electromagnético nulo. Sin embargo, cinco sextas partes de la materia gravitante de nuestro universo no son luminosas. "
        "Como la métrica de Einstein se acopla universalmente a todo tensor de energía-momento, un sector que jamás dispersa un fotón aún inclina el "
        "ritmo del tiempo propio, requiriendo dos relojes separados en el espacio para detectar un tránsito puramente gravitacional, o relojes "
        "colocalizados de distintas especies atómicas para acotar cualquier portal no gravitacional."
    ),
    "seo": (
        "Two Clocks That Only Meet in Gravity: Dark Sectors and Clock Networks",
        "How universal metric coupling lets spatially separated clocks sense electromagnetically transparent matter while co-located optical clocks bound scalar portals.",
        "Dos Relojes que Solo se Encuentran en la Gravedad: Sectores Oscuros y Redes de Relojes",
        "Cómo el acoplamiento métrico universal permite a relojes separados sentir materia transparente a la luz mientras relojes ópticos acotan portales escalares.",
    ),
    "reading_time_en": "15 min read",
    "reading_time_es": "15 min de lectura",
    "central_number_en": "Planck 2018 gives Ω_c / Ω_b = 5.364 (84.3% of matter); GL5 quadrature of Δτ(T) for an EM-transparent transit matches -(2GM/c²v)[arsinh(vT/b₁) - arsinh(vT/b₂)] within 3.7e-16, with Δτ = 0 at zero baseline d_c = 0",
    "central_number_es": "Planck 2018 da Ω_c / Ω_b = 5.364 (84.3% de la materia); la cuadratura GL5 de Δτ(T) para un tránsito transparente a la luz coincide con -(2GM/c²v)[arsinh(vT/b₁) - arsinh(vT/b₂)] dentro de 3.7e-16, con Δτ = 0 en línea base nula d_c = 0",
    "verifier": "skills/timegravity/t12/verify_t12_dark_clock.py",
    "generator": "skills/timegravity/t12/make_t12.py",
    "skill": "skills/timegravity/t12/SKILL.md",
    "skill_filename": "timegravity-t12-dark-clock.SKILL.md",
    "open_question_en": "Does the 84.3% of matter that leaves no electromagnetic record couple to our clocks only through the curvature of proper time, or through a portal just below today's optical-clock bounds?",
    "open_question_es": "¿El 84.3% de la materia que no deja registro electromagnético se acopla a nuestros relojes solo mediante la curvatura del tiempo propio, o mediante un portal justo por debajo de las cotas actuales de los relojes ópticos?",
    "ledger_ids": [PLANCK, CLOWE, MICRO, PR60, CHOU, EIN16, JOOS, KEN20, FIL23, LZ23, CAR21],
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any measurement or derivation cited on this page. "
        "The page text, instrument and verifier were drafted with AI assistance and checked by the site maintainer against the primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna medición o derivación citada en esta "
        "página. El texto, el instrumento y el verificador se redactaron con asistencia de IA y los revisó quien mantiene el sitio contra las fuentes primarias listadas abajo."
    ),
    "instrument": {
        "kind": "dark_clock",
        "title_en": "Instrument · Proper-time step of an electromagnetically transparent transit across a two-clock network",
        "title_es": "Instrumento · Escalón de tiempo propio de un tránsito transparente a la luz en una red de dos relojes",
        "how_en": (
            "Left: the differential gravitational redshift Δν(t)/ν = (Φ₁(t) − Φ₂(t))/c² across two clocks separated by baseline d_c as an "
            "electromagnetically transparent mass M_DM (α_EM = 0, Λ_EM = 0) flies past Clock 1 at impact parameter b₁ with galactic speed "
            "v₀ = 220 km/s. Right: the integrated proper-time step |Δτ_∞| = (2 G M_DM / c² v₀) ln(1 + d_c / b₁) as a function of network "
            "baseline d_c, alongside the ultralight scalar portal modulation δ(ν_A/ν_B)/(ν_A/ν_B) = ΔK_α d_e Φ_Pl for co-located clocks. "
            "The sliders set the clock baseline d_c / b₁ and the scalar portal coupling d_e. The knockout severs universal gravitational "
            "coupling (G_dark = 0): the proper-time step collapses to zero and the verifier rejects the run. Keyboard: Tab and arrows. "
            "With reduced motion on, nothing animates."
        ),
        "how_es": (
            "Izquierda: el corrimiento al rojo gravitacional diferencial Δν(t)/ν = (Φ₁(t) − Φ₂(t))/c² entre dos relojes separados por una línea "
            "base d_c conforme una masa transparente a la luz M_DM (α_EM = 0, Λ_EM = 0) pasa frente al Reloj 1 con parámetro de impacto b₁ a "
            "velocidad galáctica v₀ = 220 km/s. Derecha: el escalón integrado de tiempo propio |Δτ_∞| = (2 G M_DM / c² v₀) ln(1 + d_c / b₁) en "
            "función de la línea base d_c, junto a la modulación por portal escalar ultraligero δ(ν_A/ν_B)/(ν_A/ν_B) = ΔK_α d_e Φ_Pl para relojes "
            "colocalizados. Los deslizadores fijan la razón de línea base d_c / b₁ y el acoplamiento escalar d_e. El apagado corta el acoplamiento "
            "gravitacional universal (G_dark = 0): el escalón de tiempo propio cae a cero y el verificador rechaza la corrida. Teclado: Tab y flechas. "
            "Con movimiento reducido, nada se anima."
        ),
    },
    "predict": {
        "q_en": "Before you check the readout: if a passing dark-matter mass couples only through Einstein's metric (zero scalar portal coupling, d_e = 0), what differential frequency shift do two co-located clocks at the exact same position (baseline d_c = 0) record?",
        "q_es": "Antes de mirar la lectura: si una masa de materia oscura en tránsito se acopla solo mediante la métrica de Einstein (acoplamiento escalar nulo, d_e = 0), ¿qué corrimiento diferencial de frecuencia registran dos relojes colocalizados exactamente en el mismo punto (línea base d_c = 0)?",
        "options": [
            ("A large shift proportional to the atomic number Z of each clock", "Un gran corrimiento proporcional al número atómico Z de cada reloj"),
            ("Exactly zero: by the Equivalence Principle, pure gravity shifts co-located clocks identically, so a spatial baseline d_c > 0 is required", "Exactamente cero: por el Principio de Equivalencia, la gravedad pura desplaza igual a dos relojes colocalizados, por lo que se requiere una línea base d_c > 0"),
            ("An infinite shift at closest approach", "Un corrimiento infinito en el punto de máximo acercamiento"),
        ],
        "answer": 1,
        "reveal_en": "Exactly zero at d_c = 0: pure gravity curves proper time universally (dτ = (1 + Φ/c²) dt), so two clocks at the same point tick together; sensing a purely gravitational transit requires comparing clocks across a spatial baseline d_c > 0 where ΔΦ ≠ 0.",
        "reveal_es": "Exactamente cero en d_c = 0: la gravedad pura curva el tiempo propio de manera universal (dτ = (1 + Φ/c²) dt), así que dos relojes en el mismo punto marcan el mismo paso; detectar un tránsito puramente gravitacional exige comparar relojes a través de una línea base espacial d_c > 0 donde ΔΦ ≠ 0.",
    },
    "sections": [
        {"type": "h2", "id": "measured", "en": "I · Five-sixths of gravitating matter is unseen in light, and gravity is universal", "es": "I · Cinco sextas partes de la materia gravitante no se ven en luz, y la gravedad es universal", "short_en": "I · Measured", "short_es": "I · Medido"},
        P(
            C("MEASURED", [PLANCK, CLOWE],
              "Across cosmological and cluster scales, most gravitating mass neither emits nor scatters light: the Planck 2018 cosmic microwave "
              "background power spectra measure a physical cold dark matter density Ω_c h² = 0.1200 ± 0.0012 beside baryon density Ω_b h² = "
              "0.02237 ± 0.00015—a dark-to-baryonic ratio of 5.364 ± 0.065, or 84.29% of non-relativistic matter—and weak gravitational lensing "
              "of the merging Bullet Cluster 1E 0657-558 shows the gravitational potential peaks separated at 8σ from the X-ray-emitting plasma "
              "that holds most of the normal baryonic gas.",
              "En escalas cosmológicas y de cúmulos, la mayor parte de la masa gravitante ni emite ni dispersa luz: los espectros de potencia del "
              "fondo cósmico de microondas de Planck 2018 miden una densidad física de materia oscura fría Ω_c h² = 0.1200 ± 0.0012 junto a una "
              "densidad bariónica Ω_b h² = 0.02237 ± 0.00015 —una razón de 5.364 ± 0.065, o el 84.29% de la materia no relativista— y el lente "
              "gravitacional débil del Cúmulo Bala 1E 0657-558 muestra los picos del potencial gravitacional separados a 8σ del plasma emisor de "
              "rayos X que contiene la mayor parte del gas bariónico ordinario."),
            T(" ", " "),
            C("MEASURED", [MICRO, PR60, CHOU],
              "Meanwhile, laboratory and space tests confirm that gravitational proper-time redshift Δf/f = ΔΦ/c² is measured down to a 33 cm "
              "height difference in optical aluminium-ion clocks and that the Weak Equivalence Principle holds to η = (−1.5 ± 2.7)×10⁻¹⁵ in "
              "MICROSCOPE.",
              "Mientras tanto, las pruebas de laboratorio y espaciales confirman que el corrimiento al rojo gravitacional del tiempo propio "
              "Δf/f = ΔΦ/c² se mide hasta en una diferencia de altura de 33 cm en relojes ópticos de iones de aluminio y que el Principio de "
              "Equivalencia Débil se cumple hasta η = (−1.5 ± 2.7)×10⁻¹⁵ en MICROSCOPE."),
        ),
        {"type": "bridge",
         "kicker_en": "In Plain Words · Extra-Easy Explanation",
         "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
         "paras": [
             P(T("Imagine an invisible bowling ball rolling across a stretched rubber sheet in a pitch-dark room. Flashlights shine right through "
                 "the ball without casting a shadow or bouncing a single gleam back to your eyes—in the language of T.11, the ball is unrendered "
                 "in the photon bath. Yet the sheet still dips wherever the ball rolls.",
                 "Imagina una bola de boliche invisible rodando sobre una lona tensa en un cuarto oscuro. Las linternas atraviesan la bola sin "
                 "proyectar sombra ni devolver un solo destello a tus ojos: en el lenguaje de T.11, la bola no se registra en el baño de fotones. "
                 "Sin embargo, la lona se sigue hundiendo por donde pasa la bola.")),
             P(T("If you place two precision clocks at different spots on the sheet, the clock closer to the passing ball sits slightly deeper in "
                 "the gravitational dip and ticks a fraction slower while the ball goes by. Even if two sectors of matter never exchange a photon, "
                 "they still share the same spacetime geometry and meet through the rate of time.",
                 "Si colocas dos relojes de precisión en puntos distintos de la lona, el reloj más cercano a la bola en tránsito queda un poco más "
                 "abajo en el pozo gravitacional y marca el paso una fracción más lento mientras la bola pasa. Incluso si dos sectores de materia "
                 "jamás intercambian un fotón, comparten la misma geometría espaciotemporal y se encuentran a través del ritmo del tiempo.")),
         ]},
        {"type": "analogy",
         "kicker_en": "Everyday Analogy & Controls Primer",
         "kicker_es": "Analogía Cotidiana y Guía de Controles",
         "paras": [
             P(T("Everyday analogy: two tide gauges anchored a kilometre apart in a harbour at night. A submerged submarine with all lights off "
                 "reflects no radar and shines no lamp above the water, yet its hull displaces water as it passes near the first pier: comparing "
                 "the two gauges reveals the transit from the difference in water level alone, whereas two gauges bolted to the exact same post "
                 "rise and fall together and see zero difference.",
                 "Analogía cotidiana: dos mareógrafos anclados a un kilómetro de distancia en un puerto de noche. Un submarino sumergido con todas "
                 "las luces apagadas no refleja radar ni enciende lámparas sobre el agua, pero su casco desplaza agua al pasar cerca del primer "
                 "muelle: comparar los dos mareógrafos revela el paso solo por la diferencia de nivel, mientras que dos medidores atornillados al "
                 "mismo poste suben y bajan juntos y ven diferencia cero.")),
             P(T("How the controls work in plain words: the first slider changes the spatial baseline d_c between Clock 1 and Clock 2; setting "
                 "d_c = 0 puts both clocks at the same point, where the pure-gravity proper-time difference vanishes. The second slider sets a "
                 "hypothetical non-gravitational scalar coupling d_e to the electromagnetic fine-structure constant, which optical clock pairs "
                 "test even at zero baseline. The knockout sets G_dark = 0: the gravitational dip vanishes and the verifier rejects the run.",
                 "Cómo funcionan los controles en palabras sencillas: el primer deslizador cambia la línea base espacial d_c entre el Reloj 1 y el "
                 "Reloj 2; poner d_c = 0 coloca ambos relojes en el mismo punto, donde la diferencia de tiempo propio por gravedad pura se anula. "
                 "El segundo deslizador fija un acoplamiento escalar no gravitacional hipotético d_e con la constante de estructura fina, que los "
                 "pares de relojes ópticos ponen a prueba incluso con línea base cero. El apagado fija G_dark = 0: el pozo gravitacional desaparece "
                 "y el verificador rechaza la corrida.")),
         ]},
        {"type": "plate_d"},
        {"type": "h2", "id": "derived", "en": "II · Gravitational proper-time steps and optical-clock portal bounds", "es": "II · Escalones gravitacionales de tiempo propio y cotas de relojes ópticos", "short_en": "II · Derived", "short_es": "II · Derivado"},
        {"type": "equation", "text": "Δτ(T) = −(2 G M_DM / c² v₀) [arsinh(v₀ T / b₁) − arsinh(v₀ T / b₂)]  →  −(2 G M_DM / c² v₀) ln(b₂ / b₁)"},
        P(
            C("DERIVED", [EIN16, JOOS, MICRO],
              "In general relativity the metric g_{μν} couples universally to the total stress-energy tensor T_{μν} regardless of electromagnetic "
              "charge: a compact mass M_DM with α_EM = 0 has zero dipole photon-scattering localization rate (Λ_EM = 0 on T.11) yet produces the "
              "Newtonian potential Φ(r) = −G M_DM / r, shifting the proper-time rate between two clocks at impact parameters b₁ and b₂ = b₁ + d_c "
              "along a flyby at speed v₀ by the integrated step Δτ(T) = −(2 G M_DM / c² v₀) [arsinh(v₀ T / b₁) − arsinh(v₀ T / b₂)], whose spatial "
              "gradient +c² ∂(Δτ_∞)/∂b₁ = 2 G M_DM / (b₁ v₀) equals the transverse gravitational velocity impulse Δv_⊥.",
              "En la relatividad general la métrica g_{μν} se acopla universalmente al tensor total de energía-momento T_{μν} sin importar la carga "
              "electromagnética: una masa compacta M_DM con α_EM = 0 tiene tasa nula de localización por dispersión fotónica dipolar (Λ_EM = 0 en T.11) "
              "pero produce el potencial newtoniano Φ(r) = −G M_DM / r, desplazando el ritmo de tiempo propio entre dos relojes con parámetros de "
              "impacto b₁ y b₂ = b₁ + d_c durante un sobrevuelo a velocidad v₀ por el escalón integrado Δτ(T) = −(2 G M_DM / c² v₀) [arsinh(v₀ T / b₁) − "
              "arsinh(v₀ T / b₂)], cuyo gradiente espacial +c² ∂(Δτ_∞)/∂b₁ = 2 G M_DM / (b₁ v₀) iguala el impulso transversal de velocidad Δv_⊥.",
              parent=MICRO),
            T(" Across baselines d_c ∈ {1, 10, 100, 1000} m (with b₁ = 1 m, v₀ = 220 km/s, M_DM = 10⁶ kg), the verifier integrates "
              "∫ (Φ₁(t) − Φ₂(t))/c² dt by composite 5-point Gauss–Legendre quadrature anchored at the flyby timescale b₁/v₀ = 4.55 µs and matches "
              "the closed-form arsinh expression within 6.1×10⁻¹⁶ (3.7×10⁻¹⁶ at d_c = 1 km, where Δτ = −4.664×10⁻²⁶ s). At zero baseline "
              "(d_c = 0, co-located clocks), b₁ = b₂ and Δτ = 0 identically.",
              " A lo largo de líneas base d_c ∈ {1, 10, 100, 1000} m (con b₁ = 1 m, v₀ = 220 km/s, M_DM = 10⁶ kg), el verificador integra "
              "∫ (Φ₁(t) − Φ₂(t))/c² dt por cuadratura compuesta de Gauss y Legendre de 5 puntos anclada en la escala temporal b₁/v₀ = 4.55 µs y "
              "coincide con la expresión cerrada arsinh dentro de 6.1×10⁻¹⁶ (3.7×10⁻¹⁶ en d_c = 1 km, donde Δτ = −4.664×10⁻²⁶ s). Con línea base "
              "nula (d_c = 0, relojes colocalizados), b₁ = b₂ y Δτ = 0 de manera idéntica."),
        ),
        {"type": "equation", "text": "δ(ν_A / ν_B) / (ν_A / ν_B) = ΔK_α d_e Φ_Pl cos(ω_φ t),   Φ_Pl = ħ √(8π G ρ_DM) / (m_φ c³)"},
        P(
            C("BOUND", [KEN20, FIL23, LZ23],
              "Because pure gravity shifts co-located clocks identically, comparing two co-located optical clocks of different electronic sensitivity "
              "ΔK_α tests whether dark matter also carries a non-gravitational portal coupling d_e to the electromagnetic fine-structure constant α: "
              "JILA comparisons of ⁸⁷Sr against a cryogenic silicon cavity (2020) and PTB multi-year comparisons of the ¹⁷¹Yb⁺ electric-octupole (E3) "
              "and electric-quadrupole (E2) transitions (2023) set upper bounds on |d_e| for ultralight scalar masses (10⁻²¹ eV to 10⁻¹⁶ eV in the JILA comparison), "
              "while underground liquid-xenon recoil searches such as LUX-ZEPLIN (2023) bound spin-independent WIMP–nucleon cross-sections down to "
              "9.2×10⁻⁴⁸ cm² at 36 GeV/c².",
              "Como la gravedad pura desplaza por igual a los relojes colocalizados, comparar dos relojes ópticos colocalizados con distinta "
              "sensibilidad electrónica ΔK_α pone a prueba si la materia oscura porta además un acoplamiento escalar no gravitacional d_e con la "
              "constante de estructura fina α: las comparaciones en JILA de ⁸⁷Sr contra una cavidad criogénica de silicio (2020) y las comparaciones "
              "multianuales en PTB de las transiciones octupolar eléctrica (E3) y cuadrupolar eléctrica (E2) de ¹⁷¹Yb⁺ (2023) fijan cotas superiores "
              "sobre |d_e| para masas escalares ultraligeras (de 10⁻²¹ eV a 10⁻¹⁶ eV en la comparación de JILA), mientras que búsquedas subterráneas en xenón líquido como "
              "LUX-ZEPLIN (2023) acotan la sección eficaz espín-independiente WIMP–nucleón hasta 9.2×10⁻⁴⁸ cm² a 36 GeV/c²."),
            T(" At the local galactic dark-matter density ρ_DM = 0.4 GeV/cm³ and m_φ c² = 10⁻¹⁵ eV (Compton frequency 0.242 Hz), the dimensionless "
              "Planck-normalised field amplitude is Φ_Pl = 7.20×10⁻¹⁶; if d_e = 0 (purely gravitational coupling), the co-located clock ratio modulation "
              "is identically zero.",
              " A la densidad local galáctica de materia oscura ρ_DM = 0.4 GeV/cm³ y m_φ c² = 10⁻¹⁵ eV (frecuencia de Compton 0.242 Hz), la amplitud "
              "adimensional normalizada a la escala de Planck es Φ_Pl = 7.20×10⁻¹⁶; si d_e = 0 (acoplamiento puramente gravitacional), la modulación "
              "de la razón entre relojes colocalizados es idénticamente cero."),
        ),
        P(
            C("PROPOSED", [CAR21],
              "In 2020 Carney, Ghosh, Krnjaic and Taylor proposed that an array of quantum-limited mechanical impulse sensors could detect "
              "a passing dark-matter particle through its gravitational pull alone, without assuming any electromagnetic or nuclear "
              "portal coupling.",
              "En 2020 Carney, Ghosh, Krnjaic y Taylor propusieron que un arreglo de sensores mecánicos de impulso limitados cuánticamente podría "
              "detectar una partícula de materia oscura que pasa solo mediante su atracción gravitacional, sin suponer ningún "
              "acoplamiento electromagnético ni nuclear."),
            T(" The paper's own target is Planck-scale dark matter, with a large number of gram-scale sensors in a metre-scale array with sufficiently low quantum noise; "
              "it is a proposal about impulse sensors, not clocks, and stays PROPOSED.",
              " El objetivo del propio artículo es materia oscura a la escala de Planck, con un gran número de sensores a escala de gramos en un arreglo "
              "a escala de metros con ruido cuántico suficientemente bajo; es una propuesta sobre sensores de impulso, no sobre relojes, y se mantiene como PROPUESTO."),
        ),
        {"type": "spine"},
        {"type": "h2", "id": "open", "en": "III · From dark-sector clocks to the infrared gauge–gravity bridge", "es": "III · De los relojes del sector oscuro al puente infrarrojo entre gravedad y campos gauge", "short_en": "III · Not said", "short_es": "III · No dicho"},
        P(
            C("OPEN", [PLANCK, CAR21],
              "What particles or fields make up the 84.3% of non-relativistic matter measured by gravitational lensing and the cosmic microwave "
              "background—and whether that sector ever meets ordinary matter through anything other than the curvature of spacetime g_{μν}—remains "
              "an open question.",
              "Qué partículas o campos componen el 84.3% de la materia no relativista medida por lente gravitacional y por el fondo cósmico de "
              "microondas —y si ese sector se encuentra alguna vez con la materia ordinaria mediante algo distinto de la curvatura del espaciotiempo "
              "g_{μν}— sigue siendo una pregunta abierta."),
            T(" This penultimate step of the fourteen-step track hands off to T.13 (Where Infrared Gravity Meets Gauge Theory) while holding to the "
              "hub's single thread: a clock measures proper time along its worldline, the electromagnetic bath selects and broadcasts the pointer "
              "states of everything that scatters light, and gravity tilts the rate of proper time for everything that carries energy—seen or unseen.",
              " Este penúltimo paso de la serie de catorce pasos da paso a T.13 (Donde la Gravedad Infrarroja Toca las Teorías Gauge) manteniendo el "
              "hilo conductor del punto de partida: un reloj mide el tiempo propio a lo largo de su línea de mundo, el baño electromagnético selecciona "
              "y difunde los estados puntero de todo lo que dispersa la luz, y la gravedad inclina el ritmo del tiempo propio para todo lo que porta "
              "energía, visible o invisible."),
        ),
        {"type": "change_box",
         "items": [
             ("A replicated detection of a coherent oscillating or transient frequency-ratio shift across independent optical-clock networks at JILA, PTB, NIST and SYRTE would move ultralight dark-matter clock coupling from BOUND to MEASURED.",
              "Una detección replicada de una modulación coherente o transitoria en la razón de frecuencias entre redes independientes de relojes ópticos en JILA, PTB, NIST y SYRTE movería el acoplamiento de materia oscura ultraligera con relojes de COTA a MEDIDO."),
             ("Demonstrating gravitational impulse detection of calibrated sub-milligram test transits in an optomechanical sensor array would advance gravitational-only transit sensing from PROPOSED toward laboratory calibration.",
              "Demostrar la detección por impulso gravitacional de tránsitos de prueba submiligramo calibrados en un arreglo de sensores optomecánicos haría avanzar la detección puramente gravitacional de PROPUESTO hacia una calibración de laboratorio."),
             ("If the composite Gauss–Legendre quadrature of Δτ(T) ever differed from the closed-form arsinh expression by more than 1e-11, or if a zero-baseline pure-gravity run returned a non-zero shift, the verifier fails and the page does not build.",
              "Si la cuadratura compuesta de Gauss y Legendre de Δτ(T) llegara a diferir de la expresión cerrada arsinh por más de 1e-11, o si una corrida de gravedad pura con línea base cero devolviera un corrimiento no nulo, el verificador falla y la página no se construye."),
         ]},
        {"type": "ledger_table"},
    ],
    "stages": [
        ("Stage 1 · Cosmological dark-to-baryonic budget", "Etapa 1 · Presupuesto cosmológico de materia oscura a bariónica",
         "From Planck 2018 Table 2 (Ω_c h² = 0.1200 ± 0.0012, Ω_b h² = 0.02237 ± 0.00015), the kernel computes Ω_c / Ω_b = 5.3643 ± 0.0646 and f_dark = 84.29%, checking analytic error propagation against central finite differences to 1.6e-10.",
         "A partir de la Tabla 2 de Planck 2018 (Ω_c h² = 0.1200 ± 0.0012, Ω_b h² = 0.02237 ± 0.00015), el kernel calcula Ω_c / Ω_b = 5.3643 ± 0.0646 y f_dark = 84.29%, comprobando la propagación analítica de errores contra diferencias finitas centradas a 1.6e-10."),
        ("Stage 2 · Closed-form arsinh vs composite GL5 quadrature", "Etapa 2 · Forma cerrada arsinh frente a cuadratura compuesta GL5",
         "For a flyby along r_DM(t) = (b₁, v₀ t, 0) past clocks at b₁ and b₂ = b₁ + d_c, the kernel integrates ∫ (Φ₁ − Φ₂)/c² dt over [-T, +T] using composite 5-point Gauss–Legendre quadrature anchored at b₁/v₀, matching -(2GM/c²v₀)[arsinh(v₀T/b₁) − arsinh(v₀T/b₂)] within 6.1e-16.",
         "Para un sobrevuelo a lo largo de r_DM(t) = (b₁, v₀ t, 0) frente a relojes en b₁ y b₂ = b₁ + d_c, el kernel integra ∫ (Φ₁ − Φ₂)/c² dt en [-T, +T] mediante cuadratura compuesta de Gauss y Legendre de 5 puntos anclada en b₁/v₀, coincidiendo con -(2GM/c²v₀)[arsinh(v₀T/b₁) − arsinh(v₀T/b₂)] dentro de 6.1e-16."),
        ("Stage 3 · Transverse impulse & equivalence-principle baseline check", "Etapa 3 · Impulso transversal y comprobación de línea base del principio de equivalencia",
         "Central differences verify +c² ∂(Δτ_∞)/∂b₁ = 2 G M_DM / (b₁ v₀) = Δv_⊥ within 5.6e-11. At d_c = 0 and d_e = 0, both Δτ and δ(ν_A/ν_B) vanish identically, while the ULDM energy-density round-trip (c²/8πG) ω_φ² Φ_Pl² = ρ_DM holds to 2.1e-16.",
         "Las diferencias finitas centradas verifican +c² ∂(Δτ_∞)/∂b₁ = 2 G M_DM / (b₁ v₀) = Δv_⊥ dentro de 5.6e-11. En d_c = 0 y d_e = 0, tanto Δτ como δ(ν_A/ν_B) se anulan idénticamente, mientras la identidad de densidad de energía ULDM (c²/8πG) ω_φ² Φ_Pl² = ρ_DM se cumple a 2.1e-16."),
        ("Stage 4 · Planted defect knockout", "Etapa 4 · Apagado por defecto plantado",
         "Setting G_dark = 0 for the electromagnetically transparent mass gives Δτ = 0 across non-zero baselines d_c > 0, failing the trajectory quadrature gate with relative error 1.0 and rejecting the run.",
         "Fijar G_dark = 0 para la masa transparente a la luz da Δτ = 0 en líneas base no nulas d_c > 0, fallando la compuerta de cuadratura de trayectoria con error relativo 1.0 y rechazando la corrida."),
    ],
    "sidenotes": [
        ("SIDENOTE T.12-A · WHY CO-LOCATED CLOCKS NEED A PORTAL (d_e ≠ 0) WHILE NETWORKS SENSE PURE GRAVITY", "NOTA T.12-A · POR QUÉ LOS RELOJES COLOCALIZADOS REQUIEREN UN PORTAL (d_e ≠ 0) MIENTRAS LAS REDES SIENTEN GRAVEDAD PURA",
         "By the Weak Equivalence Principle (T.01–T.03), a gravitational potential Φ(x, t) shifts the tick rate of every clock at the same point x by the same fractional amount Φ/c², regardless of atomic transition. Two co-located clocks (d_c = 0) therefore cancel pure gravity in their ratio ν_A/ν_B and isolate non-gravitational portal couplings d_e; sensing pure gravity requires a spatial baseline d_c > 0.",
         "Por el Principio de Equivalencia Débil (T.01–T.03), un potencial gravitacional Φ(x, t) desplaza el ritmo de todo reloj en el mismo punto x por la misma fracción Φ/c², sin importar la transición atómica. Dos relojes colocalizados (d_c = 0) cancelan por tanto la gravedad pura en su razón ν_A/ν_B y aíslan acoplamientos no gravitacionales d_e; detectar gravedad pura exige una línea base espacial d_c > 0."),
        ("SIDENOTE T.12-B · LOGARITHMIC BASELINE SCALING OF GRAVITATIONAL TRANSITS", "NOTA T.12-B · ESCALAMIENTO LOGARÍTMICO DE LÍNEA BASE EN TRÁNSITOS GRAVITACIONALES",
         "Because the 1/r Newtonian potential integrates along a straight trajectory to 2 arsinh(v₀ T / b), the asymptotic differential proper-time step between impact parameters b₁ and b₂ = b₁ + d_c grows logarithmically as (2 G M_DM / c² v₀) ln(1 + d_c / b₁).",
         "Como el potencial newtoniano 1/r se integra a lo largo de una trayectoria recta como 2 arsinh(v₀ T / b), el escalón diferencial asintótico de tiempo propio entre parámetros de impacto b₁ y b₂ = b₁ + d_c crece logarítmicamente como (2 G M_DM / c² v₀) ln(1 + d_c / b₁)."),
    ],
    "sources": [
        ("Planck Collaboration (Aghanim, N., et al.). (2020). Planck 2018 results. VI. Cosmological parameters. Astronomy & Astrophysics, 641, A6.", "10.1051/0004-6361/201833910"),
        ("Clowe, D., Bradač, M., Gonzalez, A. H., Markevitch, M., Randall, S. W., Jones, C., & Zaritsky, D. (2006). A direct empirical proof of the existence of dark matter. The Astrophysical Journal Letters, 648(2), L109–L113.", "10.1086/508162"),
        ("Touboul, P., et al. (MICROSCOPE Collaboration). (2022). MICROSCOPE mission: Final results of the test of the equivalence principle. Physical Review Letters, 129(12), 121102.", "10.1103/PhysRevLett.129.121102"),
        ("Pound, R. V., & Rebka, G. A. (1960). Apparent weight of photons. Physical Review Letters, 4(7), 337–341.", "10.1103/PhysRevLett.4.337"),
        ("Chou, C. W., Hume, D. B., Rosenband, T., & Wineland, D. J. (2010). Optical clocks and relativity. Science, 329(5999), 1630–1633.", "10.1126/science.1192720"),
        ("Einstein, A. (1916). Die Grundlage der allgemeinen Relativitätstheorie. Annalen der Physik, 354(7), 769–822.", "10.1002/andp.19163540702"),
        ("Joos, E., & Zeh, H. D. (1985). The emergence of classical properties through interaction with the environment. Zeitschrift für Physik B Condensed Matter, 59(2), 223–243.", "10.1007/BF01725541"),
        ("Kennedy, C. J., Oelker, E., Robinson, J. M., Bothwell, T., Kedar, D., Milner, W. R., Marti, G. E., Derevianko, A., & Ye, J. (2020). Precision metrology meets cosmology: Improved constraints on ultralight dark matter from atom-cavity frequency comparisons. Physical Review Letters, 125(20), 201302.", "10.1103/PhysRevLett.125.201302"),
        ("Filzinger, M., Döring, S., Steinel, M., Huntemann, N., et al. (2023). Improved limits on the coupling of ultralight bosonic dark matter to photons from optical atomic clock comparisons. Physical Review Letters, 130(25), 253001.", "10.1103/PhysRevLett.130.253001"),
        ("Aalbers, J., et al. (LUX-ZEPLIN Collaboration). (2023). First dark matter search results from the LUX-ZEPLIN (LZ) experiment. Physical Review Letters, 131(4), 041002.", "10.1103/PhysRevLett.131.041002"),
        ("Carney, D., Ghosh, S., Krnjaic, G., & Taylor, J. M. (2020). Proposal for gravitational direct detection of dark matter. Physical Review D, 102(7), 072003.", "10.1103/PhysRevD.102.072003"),
    ],
}
