"""Search titles and descriptions for every Informatico.ai page, in English and Mexican Spanish.

Written by hand, one entry per essay, so search results show a whole idea instead of a fragment
cut at a fixed width (council SEO review, 2026-11-04). Each entry restates the essay's own title and
subtitle in plain words: no new claims, numbers only where the essay states them, no formulas.

Budgets, checked by tests/test_informatico_seo.py:
  - title: at most 53 characters, so "<title> | Informatico.ai" stays within 70;
  - description: 110 to 158 characters, one or two whole sentences ending with a period.
"""

from __future__ import annotations

BRAND = "Informatico.ai"

# slug -> (title_en, description_en, title_es, description_es)
FOLIO_SEO: dict[str, tuple[str, str, str, str]] = {
    # ---- Pillar I: Civil Engineering & Construction
    "e01": (
        "Stokes–Brinkman Flow in Porous Materials",
        "How viscous shear and Darcy drag balance inside porous limestone, capillary mortars and biological hydrogels, with an interactive percolation model.",
        "Flujo de Stokes–Brinkman en Materiales Porosos",
        "Cómo se equilibran el cortante viscoso y el arrastre de Darcy en caliza porosa, morteros capilares e hidrogeles, con un modelo interactivo de percolación.",
    ),
    "e02": (
        "Herschel–Bulkley Rheology of Pumped Concrete",
        "How the yield-stress rheology of Bingham, Herschel and Bulkley sets pipe pressure, forms a solid plug core and keeps concrete pumping free of blockages.",
        "Reología de Herschel–Bulkley del Concreto Bombeado",
        "Cómo la reología con esfuerzo de fluencia de Bingham, Herschel y Bulkley fija la presión en la tubería, forma un tapón central y evita bloqueos al bombear.",
    ),
    "e03": (
        "Acoustic Metamaterials: Helmholtz Sound Absorbers",
        "How coiled quarter-wave resonators and micro-slit boundary layers absorb nearly all low-frequency sound in a panel 1/19th of a wavelength thick.",
        "Metamateriales Acústicos: Absorbedores de Helmholtz",
        "Cómo los resonadores de cuarto de onda enrollados y las capas límite en microranuras absorben casi todo el sonido grave en 1/19 de la longitud de onda.",
    ),
    "e04": (
        "Counter-Current Enthalpy Recovery Exchangers",
        "How membrane exchangers pass heat and water vapor from exhaust to supply air, recovering 88.2% sensible and 79.4% latent energy without frost.",
        "Recuperadores de Entalpía a Contracorriente",
        "Cómo los intercambiadores de membrana pasan calor y vapor de agua del aire de extracción al de suministro, con 88.2% de recuperación y sin escarcha.",
    ),
    "e05": (
        "Terzaghi Soil Mechanics and CFA Deep Foundations",
        "How Karl Terzaghi's effective stress principle and consolidation theory, with continuous flight auger piles, govern building settlement and liquefaction.",
        "Mecánica de Suelos de Terzaghi y Pilas CFA",
        "Cómo el principio de esfuerzo efectivo y la teoría de consolidación de Karl Terzaghi, junto con las pilas CFA, gobiernan el asentamiento y la licuefacción.",
    ),
    "e06": (
        "Nonlinear Structural Dynamics and Seismic Isolation",
        "How Biot's earthquake spectra, Newmark–Hall ductility and Robinson's lead-rubber bearings decouple hospitals and laboratories from ground motion.",
        "Dinámica Estructural No Lineal y Aislamiento Sísmico",
        "Cómo los espectros sísmicos de Biot, la ductilidad de Newmark–Hall y los aisladores de plomo-caucho de Robinson separan hospitales y laboratorios del sismo.",
    ),
    "e07": (
        "Suspension Bridge Flutter and Scanlan Derivatives",
        "How Robert Scanlan's flutter derivatives govern twin-box bridge decks in extreme wind, and how physics-informed neural networks read them from few sensors.",
        "Flameo de Puentes Colgantes y Derivadas de Scanlan",
        "Cómo las derivadas aeroelásticas de Robert Scanlan gobiernan los tableros de puentes bajo viento extremo, con gemelos digitales de redes neuronales PINN.",
    ),
    "e08": (
        "EPB Tunnel Boring Machines and Settlement Troughs",
        "How the Peck–Mair Gaussian settlement trough predicts ground movement above city tunnels, paired with graph neural network twins of the subsurface.",
        "Tuneladoras EPB y Cubetas de Asentamiento",
        "Cómo la cubeta gaussiana de Peck y Mair predice el movimiento del suelo sobre túneles urbanos, con gemelos digitales de redes neuronales de grafos.",
    ),
    "e09": (
        "Self-Healing Concrete: Bacterial and Crystalline",
        "How Bacillus pseudofirmus spores and crystalline admixtures seal microcracks in concrete by growing calcium carbonate, tracked with ultrasonic coda waves.",
        "Concreto Autocurativo Bacteriano y Cristalino",
        "Cómo las esporas de Bacillus pseudofirmus y los aditivos cristalinos sellan microfisuras del concreto con carbonato de calcio, verificado con ondas coda.",
    ),
    "e10": (
        "3D Concrete Printing: Extrusion and Buildability",
        "How Nicolas Roussel's thixotropic structuration and Suiker's buckling laws decide whether a robot-printed concrete wall stands without formwork.",
        "Impresión 3D de Concreto: Extrusión e Imprimibilidad",
        "Cómo la estructuración tixotrópica de Nicolas Roussel y las leyes de pandeo de Suiker deciden si un muro de concreto impreso sin cimbra se sostiene.",
    ),
    "e11": (
        "SIMP Topology Optimization and Inerter Damping",
        "How Bendsøe and Sigmund's bone-like topology optimization and Formula 1 flywheel inerters cut floor concrete by 65% while calming wind sway in towers.",
        "Optimización Topológica SIMP y Amortiguador Inerter",
        "Cómo la optimización topológica tipo hueso de Bendsøe y Sigmund y los volantes de inercia de Fórmula 1 reducen 65% el concreto y frenan el viento.",
    ),
    "e12": (
        "Verified RISC-V Silicon and Firefly Grid Control",
        "How Anthropic's 180-million-line Rocq proof for RISC-V chips, Control Barrier Functions and firefly phase-locking stabilize renewable power grids.",
        "Silicio RISC-V Verificado y Control de Red Renovable",
        "Cómo la prueba de 180 millones de líneas en Rocq para RISC-V, las funciones de barrera y la sincronización de luciérnagas estabilizan la red eléctrica.",
    ),
    # ---- Pillar II: Architecture
    "a01": (
        "Funicular Thrust Surfaces in Stone and Timber Shells",
        "How compression-only stone vaults and cross-laminated timber shells stand under Heyman's middle-third rule, with a condensation-free springer detail.",
        "Superficies Funiculares de Empuje en Bóvedas",
        "Cómo las bóvedas de piedra a compresión y las cáscaras de madera contralaminada se sostienen con la regla del tercio medio de Heyman, sin condensación.",
    ),
    "a02": (
        "Reciprocal Timber Gridshells (Nexorades)",
        "How bolt-free reciprocal timber frames, where each beam rests on its neighbor, turn shell thrust into local bending and span large roofs with short pieces.",
        "Retículas Recíprocas de Madera (Nexorades)",
        "Cómo los entramados recíprocos de madera sin herrajes, donde cada viga descansa sobre su vecina, cubren grandes claros con piezas cortas.",
    ),
    "a03": (
        "Double-Skin Facades and Buoyancy Stack Ventilation",
        "How the thermosiphon stack effect and solar shading inside multi-story ventilated glass cavities cut mechanical cooling loads without overheating.",
        "Fachadas de Doble Piel y Ventilación por Flotabilidad",
        "Cómo el efecto chimenea por termosifón y el control solar en cavidades acristaladas ventiladas reducen el enfriamiento mecánico sin sobrecalentar.",
    ),
    "a04": (
        "From Archigram to British High-Tech Architecture",
        "How Archigram's 1960s Plug-In City manifestos shaped Rogers, Piano, Rice and Foster: cast-steel exoskeletons, open floors and crane-replaceable modules.",
        "De Archigram a la Arquitectura High-Tech Británica",
        "Cómo los manifiestos utópicos de Archigram inspiraron a Rogers, Piano, Rice y Foster: exoesqueletos de acero fundido, plantas libres y módulos reemplazables.",
    ),
    "a05": (
        "Room Acoustics: Sabine–Eyring Reverberation",
        "How Wallace Sabine's decay law, Carl Eyring's absorption formula and Manfred Schroeder's prime-sequence coffers shape reverberation and noise fatigue.",
        "Acústica de Salas: Reverberación de Sabine–Eyring",
        "Cómo la ley de decaimiento de Wallace Sabine, la absorción de Carl Eyring y los casetones de números primos de Manfred Schroeder controlan la reverberación.",
    ),
    "a06": (
        "Net-Zero Water and Greywater Constructed Wetlands",
        "How Kadlec–Knight reed beds recycle 95% of building greywater, while 60 °C hot-water loops and UV-C reactors keep Legionella and Pseudomonas out.",
        "Agua Neta Cero y Humedales Construidos",
        "Cómo los lechos de carrizo de Kadlec–Knight reciclan el 95% de las aguas grises, mientras la recirculación a 60 °C y la luz UV-C controlan Legionella.",
    ),
    "a07": (
        "Luis Barragán's Chromatic Tectonics",
        "How Luis Barragán, Chucho Reyes Ferreira and Josef Albers turned mineral pigments like Rosa Mexicano and Mexican sunlight into architecture of color.",
        "Tectónica Cromática de Luis Barragán",
        "Cómo Luis Barragán, Chucho Reyes Ferreira y Josef Albers convirtieron pigmentos minerales como el Rosa Mexicano y la luz de México en arquitectura de color.",
    ),
    "a08": (
        "Radiative Sky-Cooling Roofs and Phase-Change Walls",
        "How photonic roofs send building heat through the 8–13 μm atmospheric window into cold space, even under midday sun, paired with phase-change walls.",
        "Techos de Enfriamiento Radiativo y Cambio de Fase",
        "Cómo las cubiertas fotónicas envían el calor del edificio por la ventana atmosférica de 8–13 μm hacia el espacio frío, incluso a pleno sol.",
    ),
    "a09": (
        "Hygroscopic Programmable Timber Skins",
        "How Timoshenko's bilayer curvature theory and Achim Menges's beech skins let building facades open and close with humidity, using no motors at all.",
        "Pieles Programables de Madera Higroscópica",
        "Cómo la teoría de curvatura bicapa de Timoshenko y las láminas de haya de Achim Menges abren y cierran fachadas con la humedad, sin motores eléctricos.",
    ),
    "a10": (
        "Miura-Ori Origami Deployable Facades",
        "How Koryo Miura's fold and the folded metamaterials of Schenk and Guest drive adaptive, deployable solar facades inspired by the mashrabiya screen.",
        "Fachadas Desplegables de Origami Miura-Ori",
        "Cómo el pliegue de Koryo Miura y los metamateriales plegados de Schenk y Guest impulsan fachadas solares adaptativas con razón de Poisson negativa.",
    ),
    "a11": (
        "3D Polyhedral Graphic Statics and Stone Vaults",
        "How James Clerk Maxwell's reciprocal force polyhedra and open-source COMPAS software design thin, unreinforced vaulted floors with 72% less concrete.",
        "Estática Gráfica Poliédrica 3D y Bóvedas de Piedra",
        "Cómo los poliedros recíprocos de fuerza de James Clerk Maxwell y el software abierto COMPAS diseñan pisos abovedados sin acero con 72% menos concreto.",
    ),
    "a12": (
        "Tensegrity Cable Domes and Sky-Cooling Canopies",
        "How Sergio Pellegrino's prestressed tensegrity domes and 8–13 μm radiative sky-cooling membranes shade and cool civic plazas using zero electricity.",
        "Domos de Tensegridad y Cubiertas de Enfriamiento",
        "Cómo los domos de tensegridad preesforzados de Sergio Pellegrino y las membranas radiativas de 8–13 μm enfrían plazas urbanas sin usar electricidad.",
    ),
    # ---- Pillar III: Physics
    "p01": (
        "Fluctuation–Dissipation and Allosteric Gating Energy",
        "How Keizer's fluctuation theory, Harada–Sasa dissipation and Hill cycle diagrams measure the energy efficiency of ABC-transporter gating cycles.",
        "Fluctuación–Disipación y Energética Alostérica",
        "Cómo la teoría de fluctuaciones de Keizer, la disipación de Harada–Sasa y los diagramas de Hill miden la eficiencia energética de los transportadores ABC.",
    ),
    "p02": (
        "Active Matter: Ciliary Metachronal Waves",
        "How low-Reynolds-number hydrodynamics and Kuramoto phase-lag synchronization make carpets of airway cilia beat in waves that move fluid together.",
        "Materia Activa: Ondas Metacrónicas Ciliares",
        "Cómo la hidrodinámica a bajo número de Reynolds y la sincronización de Kuramoto hacen que los cilios de las vías respiratorias latan en ondas coordinadas.",
    ),
    "p03": (
        "Mucin Hydrogel Rheology and Anomalous Subdiffusion",
        "How Carreau–Yasuda shear-thinning, reptation and anomalous subdiffusion decide how fast gene-delivery nanoparticles can cross the airway mucus mesh.",
        "Reología de Hidrogeles de Mucina y Subdifusión",
        "Cómo el adelgazamiento por corte de Carreau–Yasuda, la reptación y la subdifusión anómala deciden si las nanopartículas cruzan la malla de moco bronquial.",
    ),
    "p04": (
        "Electrokinetics of Airway Surface Hydration",
        "How Nernst–Planck electrodiffusion, Donnan swelling pressure and liquid flux across the epithelium set the critical hydration threshold of airway surfaces.",
        "Electrocinética de la Hidratación de Vías Aéreas",
        "Cómo la electrodifusión de Nernst–Planck, la presión de Donnan y el flujo líquido transepitelial fijan el umbral crítico de hidratación del pulmón.",
    ),
    "p05": (
        "Quantum Tunneling: WKB Barrier Penetration",
        "How Gamow's WKB tunneling integral, Marcus reorganization energy and kinetic isotope effects shape the chemistry of base editing of nonsense mutations.",
        "Tunelamiento Cuántico: Barreras WKB",
        "Cómo la integral de tunelamiento WKB de Gamow, la energía de reorganización de Marcus y el efecto isotópico cinético moldean la edición de bases.",
    ),
    "p06": (
        "de Gennes Polymer Reptation in Entangled Gels",
        "How Pierre-Gilles de Gennes's tube model and Doi–Edwards relaxation govern how 4.5 kb mRNA and gene-editing polyplexes slither through entangled gels.",
        "Reptación de Polímeros de de Gennes en Geles",
        "Cómo el modelo de tubo de Pierre-Gilles de Gennes y la relajación de Doi–Edwards gobiernan el avance reptante del ARNm de 4.5 kb a través de hidrogeles.",
    ),
    "p07": (
        "Formula 1 Ground-Effect Venturi Aerodynamics",
        "How underfloor Venturi tunnels, edge vortices and the 2026 FIA active aerodynamics rules balance downforce against porpoising in Formula 1 cars.",
        "Aerodinámica Venturi de Efecto Suelo en Fórmula 1",
        "Cómo los túneles Venturi bajo el piso, los vórtices de borde y la aerodinámica activa FIA 2026 equilibran la carga aerodinámica frente al porpoising.",
    ),
    "p08": (
        "The Wave Physics of Color",
        "How light waves between 380 and 780 nm make pearlescent car paint shift color with angle, while Luis Barragán's lime walls keep a calm, steady hue.",
        "La Física Ondulatoria del Color",
        "Cómo las ondas de luz entre 380 y 780 nm hacen que la pintura perlada cambie de color con el ángulo, mientras los muros de cal de Barragán mantienen su tono.",
    ),
    "p09": (
        "Electrohydrodynamic Taylor Cones and Aerosols",
        "How Sir Geoffrey Taylor's 49.3° equilibrium cone and the Rayleigh charge limit govern electrospray, a precise way to turn a liquid into a fine aerosol.",
        "Conos de Taylor Electrohidrodinámicos y Aerosoles",
        "Cómo el cono de equilibrio de 49.3° de Sir Geoffrey Taylor y el límite de carga de Rayleigh gobiernan el electrospray para generar aerosoles finos.",
    ),
    "p10": (
        "Topological Photonics and Chern Numbers",
        "How Haldane and Raghu's Berry curvature and integer Chern numbers let light and sound flow around sharp defects with zero reflection.",
        "Fotónica Topológica y Números de Chern",
        "Cómo la curvatura de Berry de Haldane y Raghu y los números enteros de Chern guían la luz y el sonido alrededor de defectos sin ninguna reflexión.",
    ),
    "p11": (
        "Surface-Code Quantum Computing and Clean Nitrogen",
        "How Kitaev's topological surface-code stabilizers in Stim and PySCF quantum phase estimation decode room-temperature nitrogen fertilizer catalysis.",
        "Códigos de Superficie Cuánticos y Nitrógeno Limpio",
        "Cómo los estabilizadores topológicos de Kitaev en Stim y la estimación de fase cuántica en PySCF descifran la catálisis limpia de fertilizantes.",
    ),
    "p12": (
        "Hilbert's Sixth Problem: Atoms to Navier–Stokes",
        "How Yu Deng, Zaher Hani and Xiao Ma derived the incompressible Navier–Stokes fluid equations from colliding Newtonian spheres over long times.",
        "El Sexto Problema de Hilbert: Átomos a Navier–Stokes",
        "Cómo Yu Deng, Zaher Hani y Xiao Ma derivaron las ecuaciones de fluidos de Navier–Stokes a partir de esferas newtonianas para tiempos largos.",
    ),
    # ---- Pillar IV: Mathematics
    "m01": (
        "Fermat's Last Theorem in Lean 4: Modularity Lifting",
        "How the Lean 4 formalization of Fermat's Last Theorem and Taylor–Wiles patching work, and how their stepwise proofs mirror energy landscapes.",
        "Último Teorema de Fermat en Lean 4",
        "Cómo funcionan la formalización en Lean 4 del Último Teorema de Fermat y el parchado de Taylor–Wiles, y cómo sus pasos reflejan paisajes de energía.",
    ),
    "m02": (
        "Riemann Zeta Zero-Density Estimates in Lean 4",
        "Inside the Zeta23 and XiPrime Lean 4 proofs: how mathematicians bound exceptions to the Riemann critical line and what spectral gaps describe.",
        "Densidad de Ceros de la Función Zeta de Riemann",
        "Dentro de las pruebas Zeta23 y XiPrime en Lean 4: cómo se acotan las excepciones a la línea crítica de Riemann y qué describen las brechas espectrales.",
    ),
    "m03": (
        "Cap Sets, FunSearch and AlphaEvolve",
        "How Google DeepMind's FunSearch found larger cap sets and AlphaEvolve multiplied 4×4 complex matrices with 48 products, reshaping extremal combinatorics.",
        "Conjuntos Cap, FunSearch y AlphaEvolve",
        "Cómo FunSearch de Google DeepMind halló conjuntos cap más grandes y AlphaEvolve multiplicó matrices complejas 4×4 con 48 multiplicaciones.",
    ),
    "m04": (
        "Polynomial Freiman–Ruzsa and the Magma Graph",
        "How Terence Tao and the Lean community formalized Marton's conjecture with entropy methods and mapped all 4,694 × 4,694 pairs of magma laws.",
        "Freiman–Ruzsa Polinomial y el Grafo de Magmas",
        "Cómo Terence Tao y la comunidad de Lean 4 formalizaron la conjetura de Marton con métodos de entropía y clasificaron 4,694 × 4,694 pares de leyes de magmas.",
    ),
    "m05": (
        "AlphaGeometry 2: Neuro-Symbolic Deductive Search",
        "How pairing a symbolic deduction engine with neural auxiliary-point generation solves Olympiad geometry, and how the same idea locates 3D binding sites.",
        "AlphaGeometry 2: Búsqueda Deductiva Neuro-Simbólica",
        "Cómo unir un motor deductivo simbólico con la generación neuronal de puntos auxiliares resuelve geometría de Olimpiada y ubica sitios de unión en 3D.",
    ),
    "m06": (
        "Fine-Grained Complexity and Process Supervision",
        "How Ryan Williams's APSP speedup and step-level process reward models prune errors in formal proof search and in genomic off-target scans.",
        "Complejidad de Grano Fino y Supervisión de Procesos",
        "Cómo la aceleración de Ryan Williams para caminos más cortos (APSP) y los modelos de recompensa por pasos podan errores en pruebas formales y en genómica.",
    ),
    "m07": (
        "F1 Energy Control with Pontryagin's Maximum Principle",
        "How Pontryagin's Maximum Principle schedules the 350 kW electric boost of 2026 Formula 1 cars without clipping the battery, sped up by neural operators.",
        "Control Óptimo de Energía en F1: Pontryagin",
        "Cómo el Principio del Máximo de Pontryagin programa los 350 kW eléctricos de la Fórmula 1 2026 sin agotar la batería, acelerado con operadores neuronales.",
    ),
    "m08": (
        "The Riemannian Geometry of Color Perception",
        "How Grassmann's projection creates metamers, colors that look the same but differ in light, and how Schrödinger's curved metric defines true hue paths.",
        "Geometría Riemanniana de la Percepción del Color",
        "Cómo la proyección de Grassmann crea metámeros, colores iguales a la vista con luz distinta, y cómo la métrica curva de Schrödinger traza el color.",
    ),
    "m09": (
        "Monge–Kantorovich Optimal Transport",
        "How Jean-David Benamou and Yann Brenier showed that Wasserstein-2 optimal transport is a fluid flow along geodesics, governed by Hamilton–Jacobi.",
        "Transporte Óptimo de Monge–Kantorovich",
        "Cómo Jean-David Benamou y Yann Brenier demostraron que el transporte óptimo Wasserstein-2 es un flujo geodésico gobernado por Hamilton–Jacobi.",
    ),
    "m10": (
        "Persistent Homology and Percolating Pores",
        "How Edelsbrunner, Letscher and Zomorodian's persistent homology finds the pore throats that let fluid percolate through materials at every scale.",
        "Homología Persistente y Poros Percolantes",
        "Cómo la homología persistente de Edelsbrunner, Letscher y Zomorodian identifica las gargantas de poro que permiten la percolación, con códigos de Betti.",
    ),
    "m11": (
        "The 3D Kakeya Conjecture and Riemann Zero Bounds",
        "How Hong Wang and Joshua Zahl solved the 3D Kakeya needle conjecture, paired with Guth and Maynard's 30/13 Riemann zero-density breakthrough.",
        "La Conjetura de Kakeya 3D y los Ceros de Riemann",
        "Cómo Hong Wang y Joshua Zahl resolvieron la conjetura de agujas de Kakeya en 3D, junto con el avance 30/13 de Guth y Maynard sobre ceros de Riemann.",
    ),
    "m12": (
        "Anthropic Lean 4 Complexity and Post-Quantum Locks",
        "How Anthropic's machine-checked Lean 4 complexity proofs pair with NIST FIPS 203 crystal lattices to protect digital trust against quantum attacks.",
        "Complejidad en Lean 4 y Criptografía Post-Cuántica",
        "Cómo las pruebas de complejidad en Lean 4 de Anthropic se unen a los retículos cristalinos NIST FIPS 203 para proteger la privacidad ante ataques cuánticos.",
    ),
}

# pillar -> (title_en, description_en, title_es, description_es); titles are complete (brand included).
PILLAR_SEO: dict[str, tuple[str, str, str, str]] = {
    "engineering": (
        "Civil Engineering & Construction Essays | Informatico.ai",
        "Twelve interactive essays on civil engineering and construction: concrete pumping, 3D printing, bridges, tunnel boring machines and self-healing concrete.",
        "Ensayos de Ingeniería Civil y Construcción | Informatico.ai",
        "Doce ensayos interactivos de ingeniería civil y construcción: bombeo e impresión 3D de concreto, puentes, tuneladoras y concreto autocurativo.",
    ),
    "architecture": (
        "Architecture Essays: Vaults, Color & Facades | Informatico.ai",
        "Twelve interactive essays on architecture: stone vaults, timber gridshells, Barragán's color, sky-cooling roofs and facades that move with humidity and sun.",
        "Ensayos de Arquitectura: Bóvedas, Color y Fachadas | Informatico.ai",
        "Doce ensayos interactivos de arquitectura: bóvedas de piedra, retículas de madera, el color de Barragán, techos que se enfrían y fachadas que se mueven.",
    ),
    "physics": (
        "Physics Essays: F1 Aero, Color & Waves | Informatico.ai",
        "Twelve interactive essays on physics: Formula 1 aerodynamics, the wave physics of color, cilia and mucus, Taylor-cone aerosols and topological photonics.",
        "Ensayos de Física: Aerodinámica F1, Color y Ondas | Informatico.ai",
        "Doce ensayos interactivos de física: aerodinámica de Fórmula 1, la física ondulatoria del color, cilios y moco, conos de Taylor y fotónica topológica.",
    ),
    "math": (
        "Mathematics Essays: Lean 4 Proofs & More | Informatico.ai",
        "Twelve interactive essays on mathematics: Fermat's Last Theorem in Lean 4, F1 optimal control, the geometry of color, optimal transport and topology.",
        "Ensayos de Matemáticas: Pruebas en Lean 4 y Más | Informatico.ai",
        "Doce ensayos interactivos de matemáticas: Fermat en Lean 4, control óptimo en la Fórmula 1, la geometría del color, transporte óptimo y topología.",
    ),
}

# The cover page; "{total}" is replaced with the number of essays.
HUB_SEO: tuple[str, str, str, str] = (
    "Informatico.ai — {total} interactive essays on how the built world works",
    "{total} interactive long-form essays on civil engineering, architecture, physics and mathematics, in English and Spanish, each with a live model to explore.",
    "Informatico.ai — {total} ensayos sobre cómo funciona el mundo construido",
    "{total} ensayos interactivos de largo aliento sobre ingeniería civil, arquitectura, física y matemáticas, en español e inglés, cada uno con un modelo vivo.",
)
