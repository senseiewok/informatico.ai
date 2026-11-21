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
        "How viscous shear and Darcy drag balance over the Brinkman screening length in porous limestone and mortars, with a lattice percolation model.",
        "Flujo de Stokes–Brinkman en Materiales Porosos",
        "Cómo se equilibran el cortante viscoso y el arrastre de Darcy sobre la longitud de Brinkman en caliza porosa y morteros, con un modelo de percolación.",
    ),
    "e02": (
        "Herschel–Bulkley Rheology of Pumped Concrete",
        "How the yield-stress rheology of Bingham, Herschel and Bulkley describes pipe pressure, a central plug core and the risk of blockage when pumping concrete.",
        "Reología de Herschel–Bulkley del Concreto Bombeado",
        "Cómo la reología con esfuerzo de fluencia de Bingham, Herschel y Bulkley describe la presión en la tubería, el tapón central y el riesgo de bloqueo.",
    ),
    "e03": (
        "Acoustic Metamaterials: Helmholtz Sound Absorbers",
        "How coiled resonators and viscothermal boundary layers could absorb low-frequency sound in a panel about 1/19 of a wavelength thick, as a design target.",
        "Metamateriales Acústicos: Absorbedores de Helmholtz",
        "Cómo resonadores enrollados y capas límite viscotérmicas podrían absorber sonido grave en un panel de 1/19 de longitud de onda, como meta de diseño.",
    ),
    "e04": (
        "Counter-Current Enthalpy Recovery Exchangers",
        "How membrane exchangers move heat and water vapor between exhaust and supply air, with model values of 88.2% sensible and 79.4% latent effectiveness.",
        "Recuperadores de Entalpía a Contracorriente",
        "Cómo los intercambiadores de membrana mueven calor y vapor entre el aire de extracción y el de suministro, con valores de modelo de 88.2% y 79.4%.",
    ),
    "e05": (
        "Terzaghi Soil Mechanics and CFA Deep Foundations",
        "How Karl Terzaghi's effective stress principle and consolidation theory, with continuous flight auger piles, relate to settlement and excess pore pressure.",
        "Mecánica de Suelos de Terzaghi y Pilas CFA",
        "Cómo el esfuerzo efectivo y la consolidación de Karl Terzaghi, junto con las pilas CFA, se relacionan con el asentamiento y la presión de poro.",
    ),
    "e06": (
        "Nonlinear Structural Dynamics and Seismic Isolation",
        "How Biot's earthquake spectra, Newmark–Hall ductility and Robinson's lead-rubber bearings are meant to decouple hospitals and laboratories from ground motion.",
        "Dinámica Estructural No Lineal y Aislamiento Sísmico",
        "Cómo los espectros sísmicos de Biot, la ductilidad de Newmark–Hall y los aisladores de Robinson buscan separar hospitales y laboratorios del sismo.",
    ),
    "e07": (
        "Suspension Bridge Flutter and Scanlan Derivatives",
        "How Robert Scanlan's flutter derivatives describe wind forces on bridge decks, and how physics-informed neural networks might read stresses from few sensors.",
        "Flameo de Puentes Colgantes y Derivadas de Scanlan",
        "Cómo las derivadas de flameo de Robert Scanlan describen el viento sobre tableros de puentes, y cómo redes PINN podrían leer esfuerzos con pocos sensores.",
    ),
    "e08": (
        "EPB Tunnel Boring Machines and Settlement Troughs",
        "How the Peck–Mair Gaussian settlement trough describes ground movement above city tunnels, and how a graph network twin of the subsurface might be tried.",
        "Tuneladoras EPB y Cubetas de Asentamiento",
        "Cómo la cubeta gaussiana de Peck y Mair describe el movimiento del suelo sobre túneles urbanos, y cómo podría probarse un gemelo con redes de grafos.",
    ),
    "e09": (
        "Self-Healing Concrete: Bacterial and Crystalline",
        "How Bacillus pseudofirmus spores and crystalline admixtures can seal microcracks with calcium carbonate, in an illustrative model with coda-wave monitoring.",
        "Concreto Autocurativo Bacteriano y Cristalino",
        "Cómo las esporas de Bacillus pseudofirmus y los aditivos cristalinos pueden sellar microfisuras con carbonato de calcio, en un modelo ilustrativo.",
    ),
    "e10": (
        "3D Concrete Printing: Extrusion and Buildability",
        "How Nicolas Roussel's thixotropic structuration and Suiker's buckling analysis bear on whether a printed concrete wall can stand without formwork.",
        "Impresión 3D de Concreto: Extrusión e Imprimibilidad",
        "Cómo la estructuración tixotrópica de Nicolas Roussel y el pandeo de Suiker se relacionan con que un muro de concreto impreso se sostenga sin cimbra.",
    ),
    "e11": (
        "SIMP Topology Optimization and Inerter Damping",
        "How Bendsøe and Sigmund's SIMP topology optimization, Michell trusses and flywheel inerters could lighten floor slabs, as a design study.",
        "Optimización Topológica SIMP y Amortiguador Inerter",
        "Cómo la optimización SIMP de Bendsøe y Sigmund, las armaduras de Michell y los inerters de volante podrían aligerar losas, en un estudio de diseño.",
    ),
    "e12": (
        "RISC-V Silicon and Firefly Grid Control Barriers",
        "How Control Barrier Functions and firefly-style phase-locking can steady renewable grids, and what a machine-checked RISC-V chip would add beneath.",
        "Silicio RISC-V y Barreras de Control en la Red",
        "Cómo las funciones de barrera y la sincronización tipo luciérnaga pueden estabilizar la red renovable, y qué sumaría un chip RISC-V comprobado por máquina.",
    ),
    "e13": (
        "Biot 3D Poroelasticity and Fault Slip Margin",
        "How Biot consolidation, Skempton pore-pressure coupling and Mohr-Coulomb friction frame fault slip risk during geologic carbon dioxide storage, in a model.",
        "Poroelasticidad de Biot y Deslizamiento de Fallas",
        "Cómo la consolidación de Biot, el acoplamiento de Skempton y la fricción de Mohr-Coulomb acotan el deslizamiento de fallas al inyectar CO2, en un modelo.",
    ),
    "e14": (
        "Unsaturated Suction Stress and Slope Instability",
        "How van Genuchten retention, Mualem permeability and Lu-Godt-Wu suction stress model rainfall-induced slope collapse in silty loam and sand.",
        "Succión en Suelos No Saturados y Laderas",
        "Cómo la retención de van Genuchten, la permeabilidad de Mualem y el esfuerzo de succión de Lu-Godt-Wu modelan fallas de ladera por lluvia.",
    ),
    "e15": (
        "Quasi-Brittle Concrete Size Effect Scaling",
        "How Hillerborg's process zone and Bazant's Size Effect Law explain why deep concrete girders carry less nominal stress than small test beams.",
        "Efecto de Tamaño y Fractura en Concreto",
        "Cómo la zona de proceso de Hillerborg y la ley de Bažant explican por qué vigas profundas de concreto fallan a menor esfuerzo que probetas chicas.",
    ),
    # ---- Pillar II: Architecture
    "a01": (
        "Funicular Thrust Surfaces in Stone and Timber Shells",
        "How a compression-only stone vault stands when its thrust line stays inside the masonry, with a middle-third check and a modeled springer node.",
        "Superficies Funiculares de Empuje en Bóvedas",
        "Cómo se sostiene una bóveda de piedra a compresión pura cuando su línea de empuje queda dentro de la mampostería, con revisión del tercio medio.",
    ),
    "a02": (
        "Reciprocal Timber Gridshells (Nexorades)",
        "How bolt-free reciprocal timber frames, where each beam rests on its neighbor, turn shell thrust into local bending and span large roofs with short pieces.",
        "Retículas Recíprocas de Madera (Nexorades)",
        "Cómo los entramados recíprocos de madera sin herrajes, donde cada viga descansa sobre su vecina, cubren grandes claros con piezas cortas.",
    ),
    "a03": (
        "Double-Skin Facades and Buoyancy Stack Ventilation",
        "How the thermosiphon stack effect and solar shading inside multi-story ventilated glass cavities could reduce cooling loads, in a stack-draft model.",
        "Fachadas de Doble Piel y Ventilación por Flotabilidad",
        "Cómo el efecto chimenea por termosifón y el control solar en cavidades acristaladas ventiladas podrían reducir cargas de enfriamiento, en un modelo de tiro.",
    ),
    "a04": (
        "From Archigram to British High-Tech Architecture",
        "How Archigram's 1960s plug-in drawings are widely seen as an influence on Rogers, Piano, Rice and Foster, with a lever model of the cast-steel gerberette.",
        "De Archigram a la Arquitectura High-Tech Británica",
        "Cómo los dibujos enchufables de Archigram suelen verse como influencia en Rogers, Piano, Rice y Foster, con un modelo de palanca de la gerberette.",
    ),
    "a05": (
        "Room Acoustics: Sabine–Eyring Reverberation",
        "How Sabine's reverberation law, Eyring's absorption formula and Manfred Schroeder's prime-sequence coffers can help design rooms where speech is clearer.",
        "Acústica de Salas: Reverberación de Sabine–Eyring",
        "Cómo la ley de Sabine, la absorción de Eyring y los casetones de números primos de Manfred Schroeder ayudan a diseñar salas donde la voz se entienda mejor.",
    ),
    "a06": (
        "Net-Zero Water and Greywater Constructed Wetlands",
        "How a modelled reed bed removes about 95% of greywater BOD, while 60 °C recirculation and UV-C are design targets meant to limit bacteria growth indoors.",
        "Agua Neta Cero y Humedales Construidos",
        "Cómo un lecho de carrizo modelado elimina cerca del 95% de la DBO del agua gris, y cómo 60 °C y UV-C son metas de diseño para limitar bacterias.",
    ),
    "a07": (
        "Luis Barragán's Chromatic Tectonics",
        "How Luis Barragán, with Chucho Reyes Ferreira, worked with saturated color and Mexican sunlight, and how Josef Albers taught color relativity.",
        "Tectónica Cromática de Luis Barragán",
        "Cómo Luis Barragán, con Chucho Reyes Ferreira, trabajó con color saturado y luz de México, y cómo Josef Albers enseñó la relatividad del color.",
    ),
    "a08": (
        "Radiative Sky-Cooling Roofs and Phase-Change Walls",
        "How a roof could send building heat through the 8–13 μm atmospheric window into cold space even under midday sun, in a design model.",
        "Techos de Enfriamiento Radiativo y Cambio de Fase",
        "Cómo una cubierta podría enviar el calor del edificio por la ventana atmosférica de 8–13 μm hacia el espacio frío a pleno sol, en un modelo de diseño.",
    ),
    "a09": (
        "Hygroscopic Programmable Timber Skins",
        "How Timoshenko's bilayer curvature formula describes wood skins that bend with humidity, the idea behind motor-free facades studied at ICD/ITKE Stuttgart.",
        "Pieles Programables de Madera Higroscópica",
        "Cómo la fórmula de curvatura bicapa de Timoshenko describe pieles de madera que se curvan con la humedad, idea de fachadas sin motores del ICD/ITKE.",
    ),
    "a10": (
        "Miura-Ori Origami Deployable Facades",
        "How Koryo Miura's fold and the folded metamaterials of Schenk and Guest drive adaptive, deployable solar facades inspired by the mashrabiya screen.",
        "Fachadas Desplegables de Origami Miura-Ori",
        "Cómo el pliegue de Koryo Miura y los metamateriales plegados de Schenk y Guest podrían mover celosías solares adaptativas inspiradas en la mashrabiya.",
    ),
    "a11": (
        "3D Polyhedral Graphic Statics and Stone Vaults",
        "How James Clerk Maxwell's reciprocal figures and polyhedral graphic statics, with tools like COMPAS, shape compression-only vaults, as a design study.",
        "Estática Gráfica Poliédrica 3D y Bóvedas de Piedra",
        "Cómo las figuras recíprocas de James Clerk Maxwell y la estática gráfica poliédrica, con herramientas como COMPAS, dan forma a bóvedas a compresión pura.",
    ),
    "a12": (
        "Tensegrity Cable Domes and Sky-Cooling Canopies",
        "A design study of how the floating-compression tensegrity of Snelson and Fuller could carry an 8–13 μm radiative sky-cooling membrane over a civic canopy.",
        "Domos de Tensegridad y Cubiertas de Enfriamiento",
        "Un estudio de diseño sobre cómo la tensegridad de Snelson y Fuller podría sostener una membrana de enfriamiento radiativo de 8–13 μm sobre una plaza.",
    ),
    "a13": (
        "Heinz Isler's Thin-Shell Domes and Buckling",
        "How inverted hanging cloth shapes compression-only concrete shells, and why inward dimples govern elastic buckling below Zoelly's classical limit.",
        "Domos Delgados de Heinz Isler y Pandeo Elástico",
        "Cómo una tela colgada invertida da forma a cáscaras de concreto en compresión, y por qué las abolladuras reducen el pandeo frente al límite clásico.",
    ),
    "a14": (
        "Felix Candela's Hypar Shells and Membrane Shear",
        "How straight timber boards form doubly curved hyperbolic paraboloid concrete umbrellas, and where Pucher's pure-shear model reaches its edge limits.",
        "Cascarones Reglados de Félix Candela y Cortante",
        "Cómo tablas rectas cimbran paraguas de concreto en paraboloide hiperbólico, y dónde el modelo de cortante de Pucher encuentra su límite de borde.",
    ),
    # ---- Pillar III: Physics
    "p01": (
        "Fluctuation–Dissipation and Allosteric Gating Energy",
        "How Keizer's fluctuation theory, Harada–Sasa dissipation and Hill cycle diagrams quantify the energy efficiency of ABC-transporter gating cycles.",
        "Fluctuación–Disipación y Energética Alostérica",
        "Cómo la teoría de fluctuaciones de Keizer, la disipación de Harada–Sasa y los diagramas de Hill cuantifican la eficiencia de los transportadores ABC.",
    ),
    "p02": (
        "Active Matter: Ciliary Metachronal Waves",
        "How low-Reynolds-number hydrodynamics and Kuramoto phase-lag synchronization make carpets of airway cilia beat in waves that move fluid together.",
        "Materia Activa: Ondas Metacrónicas Ciliares",
        "Cómo la hidrodinámica a bajo número de Reynolds y la sincronización de Kuramoto hacen que los cilios de las vías respiratorias latan en ondas coordinadas.",
    ),
    "p03": (
        "Mucin Hydrogel Rheology and Anomalous Subdiffusion",
        "How Carreau–Yasuda shear-thinning, reptation and anomalous subdiffusion describe the way gene-delivery nanoparticles move through the airway mucus mesh.",
        "Reología de Hidrogeles de Mucina y Subdifusión",
        "Cómo el adelgazamiento por corte de Carreau–Yasuda, la reptación y la subdifusión anómala describen a las nanopartículas en la malla de moco bronquial.",
    ),
    "p04": (
        "Electrokinetics of Airway Surface Hydration",
        "How Nernst–Planck electrodiffusion, Donnan swelling pressure and liquid flux across the epithelium enter a model of airway surface hydration.",
        "Electrocinética de la Hidratación de Vías Aéreas",
        "Cómo la electrodifusión de Nernst–Planck, la presión de Donnan y el flujo líquido transepitelial entran en un modelo de la hidratación de las vías aéreas.",
    ),
    "p05": (
        "Quantum Tunneling: WKB Barrier Penetration",
        "How Gamow's WKB tunneling integral, Marcus reorganization energy and kinetic isotope effects bear on the chemistry of adenine base editing.",
        "Tunelamiento Cuántico: Barreras WKB",
        "Cómo la integral WKB de Gamow, la energía de reorganización de Marcus y los efectos isotópicos cinéticos se relacionan con la edición de bases de adenina.",
    ),
    "p06": (
        "de Gennes Polymer Reptation in Entangled Gels",
        "How Pierre-Gilles de Gennes's tube model and Doi–Edwards relaxation describe the way long chains, such as a 4.5 kb mRNA, slither through entangled gels.",
        "Reptación de Polímeros de de Gennes en Geles",
        "Cómo el modelo de tubo de de Gennes y la relajación de Doi–Edwards describen el avance reptante de cadenas largas, como un ARNm de 4.5 kb, en geles.",
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
        "How Sir Geoffrey Taylor's 49.3° equilibrium cone and the Rayleigh charge limit govern electrospray, a way to turn a liquid into a fine aerosol.",
        "Conos de Taylor Electrohidrodinámicos y Aerosoles",
        "Cómo el cono de equilibrio de 49.3° de Sir Geoffrey Taylor y el límite de carga de Rayleigh gobiernan el electrospray para generar aerosoles finos.",
    ),
    "p10": (
        "Topological Photonics and Chern Numbers",
        "How Haldane and Raghu's Berry curvature and integer Chern numbers can route light around sharp defects with no backscatter, in an illustrative model.",
        "Fotónica Topológica y Números de Chern",
        "Cómo la curvatura de Berry de Haldane y Raghu y los números de Chern pueden guiar la luz alrededor de defectos sin retrodispersión, en un modelo ilustrativo.",
    ),
    "p11": (
        "Surface-Code Quantum Computing and FeMoCo",
        "How surface-code parity checks in Stim and PySCF quantum simulation could one day inform the search for ambient-temperature nitrogen fertilizer.",
        "Códigos de Superficie Cuánticos y FeMoCo",
        "Cómo los chequeos de paridad del código de superficie en Stim y la simulación en PySCF podrían informar la búsqueda de fertilizante a temperatura ambiente.",
    ),
    "p12": (
        "Hilbert's Sixth Problem: Atoms to Navier–Stokes",
        "How Yu Deng, Zaher Hani and Xiao Ma report, in preprints, a derivation of the incompressible Navier–Stokes equations from colliding Newtonian spheres.",
        "El Sexto Problema de Hilbert: Átomos a Navier–Stokes",
        "Cómo Yu Deng, Zaher Hani y Xiao Ma reportan, en preprints, una derivación de las ecuaciones de Navier–Stokes incompresibles a partir de esferas newtonianas.",
    ),
    # ---- Pillar IV: Mathematics
    "m01": (
        "Fermat's Last Theorem and a Public Lean 4 Repository",
        "A reading of the Taylor–Wiles patching argument behind Fermat's Last Theorem and of a public Lean 4 repository whose README says it formalises the proof.",
        "Último Teorema de Fermat y un Repositorio en Lean 4",
        "Una lectura del parchado de Taylor–Wiles detrás del Último Teorema de Fermat y de un repositorio público en Lean 4 que, según su README, formaliza la prueba.",
    ),
    "m02": (
        "Riemann Zeta Zero-Density Estimates",
        "Classical zero-density estimates for the Riemann zeta function, and what a public Lean 4 repository README states about a recent critical-line result.",
        "Densidad de Ceros de la Función Zeta de Riemann",
        "Estimaciones clásicas de densidad de ceros de la función zeta de Riemann y lo que afirma el README de un repositorio en Lean 4 sobre un resultado reciente.",
    ),
    "m03": (
        "Cap Sets, FunSearch and AlphaEvolve",
        "What Google DeepMind's FunSearch and AlphaEvolve papers report: a 512-point cap set in eight dimensions and 48 products for 4×4 complex matrices.",
        "Conjuntos Cap, FunSearch y AlphaEvolve",
        "Lo que reportan FunSearch y AlphaEvolve de Google DeepMind: un conjunto cap de 512 puntos en ocho dimensiones y 48 productos para matrices complejas 4×4.",
    ),
    "m04": (
        "Polynomial Freiman–Ruzsa and the Magma Graph",
        "How Gowers, Green, Manners and Tao settled PFR in characteristic 2 by entropy, with public Lean 4 projects around it and 4,694 magma laws.",
        "Freiman–Ruzsa Polinomial y el Grafo de Magmas",
        "Cómo Gowers, Green, Manners y Tao resolvieron PFR en característica 2 con entropía, con proyectos públicos en Lean 4 a su alrededor y 4,694 leyes de magmas.",
    ),
    "m05": (
        "AlphaGeometry 2: Neuro-Symbolic Deductive Search",
        "How AlphaGeometry pairs a symbolic deduction engine with a neural model that proposes auxiliary points, as reported in Nature and in an AlphaGeometry2 report.",
        "AlphaGeometry 2: Búsqueda Deductiva Neuro-Simbólica",
        "Cómo AlphaGeometry une un motor deductivo simbólico con un modelo neuronal que propone puntos auxiliares, según Nature y un informe sobre AlphaGeometry2.",
    ),
    "m06": (
        "Fine-Grained Complexity and Process Supervision",
        "Ryan Williams's circuit-complexity algorithm for all-pairs shortest paths, a repository's statement on 3SUM and APSP, and step-level process supervision.",
        "Complejidad de Grano Fino y Supervisión de Procesos",
        "El algoritmo de Ryan Williams para caminos más cortos entre todos los pares, lo que afirma un repositorio sobre 3SUM y APSP, y la supervisión por pasos.",
    ),
    "m07": (
        "F1 Energy Control with Pontryagin's Maximum Principle",
        "A design study of how Pontryagin's Maximum Principle could schedule a 350 kW hybrid boost without flattening the battery, with neural surrogates proposed.",
        "Control Óptimo de Energía en F1: Pontryagin",
        "Un estudio de diseño de cómo el Principio del Máximo de Pontryagin podría programar un impulso híbrido de 350 kW sin agotar la batería.",
    ),
    "m08": (
        "The Riemannian Geometry of Color Perception",
        "How Grassmann's linear color matching creates metamers, and how a curved metric of the kind Schrödinger proposed in 1920 defines hue paths, in a model.",
        "Geometría Riemanniana de la Percepción del Color",
        "Cómo la mezcla lineal de colores de Grassmann crea metámeros, y cómo una métrica curva como la de Schrödinger (1920) traza caminos entre tonos, en un modelo.",
    ),
    "m09": (
        "Monge–Kantorovich Optimal Transport",
        "How Benamou and Brenier recast Wasserstein-2 optimal transport as a fluid flow of least kinetic energy, with Sinkhorn scaling in an illustrative model.",
        "Transporte Óptimo de Monge–Kantorovich",
        "Cómo Benamou y Brenier replantearon el transporte óptimo Wasserstein-2 como un flujo de mínima energía cinética, con Sinkhorn en un modelo ilustrativo.",
    ),
    "m10": (
        "Persistent Homology and Percolating Pores",
        "How persistent homology of Edelsbrunner, Letscher and Zomorodian tracks pores and tunnels across scales, shown on a synthetic model, not real samples.",
        "Homología Persistente y Poros Percolantes",
        "Cómo la homología persistente de Edelsbrunner, Letscher y Zomorodian sigue poros y túneles entre escalas, en un modelo sintético y no en muestras reales.",
    ),
    "m11": (
        "The 3D Kakeya Conjecture and Riemann Zero Bounds",
        "Hong Wang and Joshua Zahl's preprint on 3D Kakeya sets and Guth and Maynard's zero-density estimate, two separate results read side by side.",
        "La Conjetura de Kakeya 3D y los Ceros de Riemann",
        "El preprint de Hong Wang y Joshua Zahl sobre Kakeya en 3D y la estimación de densidad de ceros de Guth y Maynard, dos resultados independientes.",
    ),
    "m12": (
        "Public Lean 4 Repositories and Post-Quantum ML-KEM",
        "What the README of the public Lean 4 repository anthropics/formal-math says it contains, beside the NIST FIPS 203 lattice standard; none checked here.",
        "Repositorios Lean 4 Públicos y ML-KEM Post-Cuántico",
        "Lo que dice el README del repositorio público anthropics/formal-math que contiene, junto al estándar de retículos NIST FIPS 203; nada comprobado aquí.",
    ),
    "m13": (
        "Shannon Zero-Error Graph Capacity and Lovász Theta",
        "How Shannon zero-error block codes, Lovász's theta umbrella and Haemers's rank bound meet on odd cycles, with the seven-cycle limit still open.",
        "Capacidad de Error Cero de Shannon y Theta de Lovász",
        "Cómo los códigos sin error de Shannon, el paraguas de Lovász y el rango de Haemers se cruzan en ciclos impares, con la brecha del ciclo de siete abierta.",
    ),
}

# pillar -> (title_en, description_en, title_es, description_es); titles are complete (brand included).
PILLAR_SEO: dict[str, tuple[str, str, str, str]] = {
    "engineering": (
        "Civil Engineering & Construction Essays | Informatico.ai",
        "Fourteen interactive essays on civil engineering and construction: concrete pumping, 3D printing, bridges, tunnel boring machines and geomechanics.",
        "Ensayos de Ingeniería Civil y Construcción | Informatico.ai",
        "Catorce ensayos interactivos de ingeniería civil y construcción: bombeo e impresión 3D de concreto, puentes, tuneladoras, concreto y geomecánica.",
    ),
    "architecture": (
        "Architecture Essays: Vaults, Color & Facades | Informatico.ai",
        "Fourteen interactive essays on architecture: stone vaults, timber gridshells, thin concrete shells, Barragán's color and radiative sky-cooling roofs.",
        "Ensayos de Arquitectura: Bóvedas, Color y Fachadas | Informatico.ai",
        "Catorce ensayos interactivos de arquitectura: bóvedas de piedra, retículas, cascarones delgados, color de Barragán y techos de enfriamiento pasivo.",
    ),
    "physics": (
        "Physics Essays: F1 Aero, Color & Waves | Informatico.ai",
        "Twelve interactive essays on physics: Formula 1 aerodynamics, the wave physics of color, cilia and mucus, Taylor-cone aerosols and topological photonics.",
        "Ensayos de Física: Aerodinámica F1, Color y Ondas | Informatico.ai",
        "Doce ensayos interactivos de física: aerodinámica de Fórmula 1, la física ondulatoria del color, cilios y moco, conos de Taylor y fotónica topológica.",
    ),
    "math": (
        "Mathematics Essays: Lean 4 Repositories & More | Informatico.ai",
        "Thirteen interactive essays on mathematics: Fermat's Last Theorem, zero-error graph capacity, F1 optimal control, color geometry and optimal transport.",
        "Ensayos de Matemáticas: Repositorios Lean 4 y Más | Informatico.ai",
        "Trece ensayos interactivos de matemáticas: el Último Teorema de Fermat, capacidad de grafos sin error, control óptimo, color y transporte óptimo.",
    ),
    "bounties": (
        "Grand Challenges & Open Problems Crucible | Informatico.ai",
        "Six interactive folios with worked-example Python scripts and AI skills on Erdős Problem #30 and closed prize themes; independent studies, not entries.",
        "Crisol de Grandes Retos y Problemas Abiertos | Informatico.ai",
        "Seis folios interactivos con scripts en Python y habilidades de IA sobre Erdős #30 y grandes retos pasados; estudios independientes, sin participar.",
    ),
    "toolchain": (
        "Tech & Tools · The 3D CAD & Open Toolbox | Informatico.ai",
        "Seven interactive 3D CAD and open-tool folios with downloadable STEP, 3MF, GLB and DXF files, Python byte-level verifiers, and skills for small studios.",
        "Tecnología y Herramientas · Caja 3D y CAD | Informatico.ai",
        "Siete folios interactivos de herramientas 3D y CAD abierto con archivos STEP, 3MF, GLB y DXF, verificadores en Python y habilidades para estudios.",
    ),
    # Time & Gravity hub (/timegravity/): the track pages' own copy lives in tools/folios/timegravity/<slug>.py ("seo").
    "timegravity": (
        "Time & Gravity · Thirteen Pages on an Open Problem | Informatico.ai",
        "A reading track from the measured slope in the rate of time to the open problem of time in quantum gravity, with instruments, verifiers and a ledger.",
        "Tiempo y Gravedad · Un Problema Abierto en 13 Páginas | Informatico.ai",
        "Una serie que va de la pendiente medida en el ritmo del tiempo al problema abierto del tiempo en la gravedad cuántica, con instrumentos y verificadores.",
    ),
    "about": (
        "About Informatico & the Verification Engine | Informatico.ai",
        "How an independent open-source lab builds interactive engineering essays and checks their model values by script, in the open.",
        "Acerca de Informatico y el Motor de Verificación | Informatico.ai",
        "Cómo un laboratorio independiente de código abierto crea ensayos interactivos y comprueba sus valores de modelo con scripts, en público.",
    ),
    "essays": (
        "Cross-Scale Essays · Shared Laws & Verification | Informatico.ai",
        "Eleven long-form essays where quantum decoherence, formal verification and porous-media thermodynamics connect falling clocks, stone and living systems.",
        "Ensayos entre Escalas · Leyes y Verificación | Informatico.ai",
        "Once ensayos donde la decoherencia cuántica, la verificación formal y la termodinámica conectan relojes ópticos, medios porosos y sistemas biológicos.",
    ),
}

# Dedicated Tech & Tools · The Toolbox Folios (x01..x07) under /toolchain/<slug>/ and /es-mx/toolchain/<slug>/
TOOLCHAIN_SEO: dict[str, tuple[str, str, str, str]] = {
    "x01": (
        "Zero-Build WebGL2 GLB Viewer and Manifold Validator",
        "How a zero-dependency WebGL2 loader parses binary glTF 2.0 files while a Python stdlib verifier checks watertight topology and signed mesh volume.",
        "Visor WebGL2 GLB y Validador de Mallas Herméticas",
        "Cómo un cargador WebGL2 sin dependencias analiza archivos glTF 2.0 binarios mientras un verificador en Python comprueba la topología y el volumen.",
    ),
    "x02": (
        "Code-First Parametric Solids: STEP, 3MF and GLB",
        "How independent engineers generate parametric B-rep solids in Python and audit what survives across STEP AP242, 3MF and GLB with chordal tolerances.",
        "Sólidos Paramétricos en Código: STEP, 3MF y GLB",
        "Cómo los ingenieros independientes generan sólidos B-rep en Python y auditan qué se conserva entre STEP AP242, 3MF y GLB con tolerancias cordales.",
    ),
    "x03": (
        "Small Architect's Vault, Timber and Open BIM Kit",
        "How small architecture studios generate compression-only stone and timber voussoir arches in Python and export STEP, 3MF, DXF and GLB files checked by script.",
        "Kit de Bóvedas y Madera para Estudios de Arquitectura",
        "Cómo los pequeños estudios de arquitectura generan arcos funiculares de piedra y madera en Python y exportan archivos STEP, 3MF, DXF y GLB.",
    ),
    "x04": (
        "Miura-Ori Kinetic Screens: 3D GLB to Laser-Cut DXF",
        "How small studios and makers generate deployable Miura-ori facade shells in 3D GLB and 3MF alongside layered 2D laser-cutter DXF crease patterns.",
        "Pantallas Cinéticas Miura-Ori: GLB 3D a Corte DXF",
        "Cómo estudios y talleres generan envolventes plegables Miura-ori en GLB y 3MF junto con patrones planos DXF por capas para corte láser.",
    ),
    "x05": (
        "SIMP Structural Lattices to Watertight 3MF Meshes",
        "How variable-taper SIMP structural struts are synthesized as watertight 2-manifold 3MF, GLB and STEP meshes with frustum volume and overhang checks.",
        "Retículas Estructurales SIMP a Mallas 3MF Herméticas",
        "Cómo se sintetizan puntales estructurales SIMP ahusados como mallas 3MF, GLB y STEP herméticas con verificación de volumen y ángulo de voladizo.",
    ),
    "x06": (
        "Topological Metamaterial Cells and Betti Verifier",
        "How pierced genus-one acoustic metamaterial unit cells are exported to GLB, 3MF and STEP while a Python verifier checks Euler and Betti invariants.",
        "Celdas de Metamateriales Topológicos y Betti 3D",
        "Cómo se exportan celdas unitarias de metamateriales acústicos de género uno a GLB, 3MF y STEP verificando sus invariantes de Euler y Betti en Python.",
    ),
    "x07": (
        "Gauss–Bonnet Curvature & Cotangent Mesh Audit",
        "How pure Python checks discrete Gauss–Bonnet closure, Meyer mixed Voronoi areas, and cotangent edge weights across GLB, 3MF, and STEP.",
        "Curvatura Gauss–Bonnet y Auditoría Cotangente",
        "Cómo Python comprueba el cierre de Gauss–Bonnet, las áreas mixtas de Meyer y los pesos cotangentes en archivos GLB, 3MF y STEP.",
    ),
}

# Dedicated Bounty Folios (b01..b06) under /bounties/<slug>/ and /es-mx/bounties/<slug>/
BOUNTY_SEO: dict[str, tuple[str, str, str, str]] = {
    "b01": (
        "Erdős Sidon Sets and Lean 4 Formalization Bounties",
        "How Mian–Chowla greedy sequences, the Erdős–Turán upper bound and Lean 4 blueprints bear on Sidon sets, with a Python worked example of the check.",
        "Conjuntos de Sidon de Erdős y Pruebas en Lean 4",
        "Cómo la sucesión voraz de Mian–Chowla, la cota de Erdős–Turán y los planos en Lean 4 se relacionan con los conjuntos de Sidon, con un ejemplo en Python.",
    ),
    "b02": (
        "Surface Codes and FeMoCo: XPRIZE Quantum Context",
        "A worked example of how surface-code stabilizers in Stim and PySCF active-space models give a qubit-count estimate for nitrogen fixation; not a prize entry.",
        "Códigos de Superficie y FeMoCo: Contexto XPRIZE",
        "Un ejemplo resuelto de cómo estabilizadores de código de superficie en Stim y modelos de PySCF dan una estimación de qubits; no es participación en un premio.",
    ),
    "b03": (
        "SIMP Floor Slab Study: XPRIZE Carbon Context",
        "A design study of how SIMP topology optimization in FEniCS and carbonated mineral curing could cut slab embodied carbon below 45 kg per square meter.",
        "Losas SIMP: Contexto XPRIZE Carbon",
        "Un estudio de diseño de cómo la optimización SIMP en FEniCS y el curado carbonatado podrían dejar una losa bajo 45 kg de carbono por metro cuadrado.",
    ),
    "b04": (
        "Zero-Rebar Vaults and Sky-Cooling: Prize Context",
        "A design study of Maxwell polyhedral graphic statics in COMPAS and 8–13 μm sky-cooling roofs for zero-rebar vaults, with model values only and no prize entry.",
        "Bóvedas sin Acero y Enfriamiento: Contexto de Premios",
        "Un estudio de diseño de estática gráfica poliédrica en COMPAS y cubiertas de enfriamiento de 8–13 μm para bóvedas sin acero; solo valores de modelo.",
    ),
    "b05": (
        "PySR Symbolic Regression and PySINDy PDE Discovery",
        "How PySINDy sparse thresholding, Dedalus spectral solvers and PySR symbolic regression recover the viscous Burgers equation from noisy data in an example.",
        "Regresión Simbólica PySR y Descubrimiento PySINDy",
        "Cómo la poda dispersa de PySINDy, los solucionadores Dedalus y la regresión simbólica PySR recuperan la ecuación de Burgers viscosa desde datos ruidosos.",
    ),
    "b06": (
        "PhysLean Gauge Anomaly & ITensors.jl Entanglement",
        "How HEPLean/PhysLean treats Standard Model gauge anomaly cancellation in Lean 4, with ITensors.jl and NetKet entanglement bounds, in a worked Python example.",
        "Anomalía Gauge en PhysLean y Redes en ITensors.jl",
        "Cómo HEPLean/PhysLean trata en Lean 4 la cancelación de anomalías gauge del Modelo Estándar, con cotas de entrelazamiento de ITensors.jl y NetKet.",
    ),
}

# The cover page; "{total}" is replaced with the number of essays.
HUB_SEO: tuple[str, str, str, str] = (
    "Informatico.ai — {total} interactive essays on how the built world works",
    "{total} interactive long-form essays on civil engineering, architecture, physics and mathematics, in English and Spanish, each with a live model to explore.",
    "Informatico.ai — {total} ensayos sobre cómo funciona el mundo construido",
    "{total} ensayos interactivos de largo aliento sobre ingeniería civil, arquitectura, física y matemáticas, en español e inglés, cada uno con un modelo vivo.",
)
