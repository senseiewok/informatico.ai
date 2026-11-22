"""Plain-language bilingual (EN-US & ES-MX) interpretations for every Informatico.ai governing law.

Each entry restates what the symbolic equation in ``governing_law`` relates or balances in everyday
scientific language so both inline page readers and spoken audio listeners grasp the physical or
mathematical meaning without losing the symbolic notation on screen.

All glosses are descriptive only and avoid overclaim language.
"""
from __future__ import annotations

LAW_GLOSSES: dict[str, dict[str, str]] = {
    # Engineering (E.01 - E.16)
    "e01": {
        "en": "viscous shear and porous drag balance the pressure gradient, while percolation marks the pore fraction where flow connects across the medium",
        "es": "el esfuerzo viscoso y el arrastre poroso equilibran el gradiente de presión, mientras la percolación marca la fracción de poros donde el flujo conecta el medio",
    },
    "e02": {
        "en": "concrete stays rigid below its yield stress and flows above it, setting the un-sheared plug radius and pumping pressure drop along the pipe",
        "es": "el concreto permanece rígido bajo su esfuerzo de fluencia y fluye al superarlo, fijando el radio del tapón central y la caída de presión en la tubería",
    },
    "e03": {
        "en": "viscous boundary-layer thickness sets acoustic damping inside the resonator, reaching near-total absorption when surface impedance matches air",
        "es": "el espesor de la capa límite viscosa fija la amortiguación acústica del resonador y logra absorción casi total cuando la impedancia iguala a la del aire",
    },
    "e04": {
        "en": "heat and moisture recovery rises with the number of transfer units while the membrane Biot number compares surface transfer against internal diffusion",
        "es": "la recuperación de calor y humedad crece con las unidades de transferencia mientras el número de Biot compara la transferencia superficial con la difusión interna",
    },
    "e05": {
        "en": "excess pore-water pressure diffuses out of soil over time, while total pile capacity sums shaft friction and tip bearing relative to effective vertical stress",
        "es": "el exceso de presión intersticial se difunde en el suelo con el tiempo, mientras la capacidad del pilote suma fricción lateral y resistencia de punta frente al esfuerzo efectivo",
    },
    "e06": {
        "en": "inertia, damping, and nonlinear restoring force balance ground acceleration, linking base shear and ductility demand to peak roof displacement",
        "es": "la inercia, la amortiguación y la fuerza restauradora no lineal equilibran la aceleración del suelo, ligando el cortante basal y la ductilidad al desplazamiento máximo",
    },
    "e07": {
        "en": "net bridge damping equals structural damping minus aerodynamic flutter excitation, while the neural surrogate combines measurement error with physics residuals",
        "es": "la amortiguación neta del puente resta la excitación aeroelástica a la amortiguación estructural, mientras el modelo neuronal combina el error medido con el residuo físico",
    },
    "e08": {
        "en": "ground settlement above a bored tunnel follows a bell-shaped trough whose volume matches the tunnel ground-loss fraction and whose width scales with cover depth",
        "es": "el asentamiento sobre un túnel sigue una cubeta gaussiana cuyo volumen iguala la pérdida de terreno y cuyo ancho escala con la profundidad de cobertura",
    },
    "e09": {
        "en": "capillary water advances with the square root of time into concrete cracks while reactant diffusion and enzymatic calcite precipitation compete to seal the void",
        "es": "el agua capilar avanza con la raíz cuadrada del tiempo dentro de las grietas mientras la difusión y la precipitación enzimática de calcita compiten por sellar el vacío",
    },
    "e10": {
        "en": "printed concrete builds yield strength linearly with resting time, setting the maximum plastic wall height before the fresh filament yields under its own weight",
        "es": "el concreto impreso gana esfuerzo de fluencia linealmente con el reposo, fijando la altura máxima de muro antes de que el filamento fresco ceda por su propio peso",
    },
    "e11": {
        "en": "topology optimization minimizes structural compliance by penalizing intermediate element densities, while an inerter adds reaction force proportional to relative acceleration",
        "es": "la optimización topológica minimiza la flexibilidad estructural penalizando densidades intermedias, mientras un inerter aporta una fuerza proporcional a la aceleración relativa",
    },
    "e12": {
        "en": "a control barrier keeps grid states inside a safe boundary while generator inertia and damping govern how frequency responds to power imbalance",
        "es": "una barrera de control mantiene el estado de la red dentro de un límite seguro mientras la inercia y el amortiguamiento rigen la respuesta de frecuencia ante desbalances",
    },
    "e13": {
        "en": "fluid pressure shares mean stress through the Biot and Skempton couplings, keeping a fault stable while shear stress stays below effective normal friction",
        "es": "la presión de fluido comparte el esfuerzo medio mediante los acoplamientos de Biot y Skempton, manteniendo la falla estable mientras el corte no supere la fricción efectiva",
    },
    "e14": {
        "en": "soil moisture retention maps matric suction into an effective suction stress that adds apparent cohesion to an infinite slope's factor of safety",
        "es": "la retención de humedad convierte la succión mátrica en un esfuerzo de succión efectivo que aporta cohesión aparente al factor de seguridad de un talud",
    },
    "e15": {
        "en": "nominal concrete tensile strength declines with member size relative to a transition scale set by fracture energy and the finite fracture process zone",
        "es": "la resistencia nominal a tracción del concreto disminuye con el tamaño del elemento respecto a una escala de transición fijada por la energía y la zona de fractura",
    },
    "e16": {
        "en": "equilibrium bridge-pier scour depth scales with pier width and flow Froude number, then reduces by a time-lag factor when flood duration is shorter than equilibrium",
        "es": "la socavación en equilibrio escala con el ancho de la pila y el número de Froude, y se reduce mediante un factor temporal cuando la crecida dura menos que el equilibrio",
    },
    # Architecture (A.01 - A.14)
    "a01": {
        "en": "horizontal arch thrust grows with load and span squared over rise, and masonry stays in pure compression when the thrust line stays within the middle third",
        "es": "el empuje horizontal del arco crece con la carga y el claro al cuadrado sobre la flecha, y la mampostería trabaja en compresión pura dentro del tercio medio",
    },
    "a02": {
        "en": "eccentric timber lap joints carry bending moment proportional to shear force and lever offset while shear stress stays below factored timber capacity",
        "es": "los empalmes recíprocos de madera resisten un momento proporcional al cortante y su excentricidad mientras el esfuerzo cortante se mantiene bajo la capacidad admisible",
    },
    "a03": {
        "en": "buoyancy stack pressure drives airflow upward in proportion to cavity height and temperature difference while solar louvers limit total heat gain",
        "es": "la presión por efecto chimenea impulsa el aire en proporción a la altura de la cámara y la diferencia térmica mientras las celosías limitan la ganancia solar",
    },
    "a04": {
        "en": "cantilever tie tension scales with the lever-arm ratio, Maxwell's rule counts frame indeterminacy against mechanisms, and replaceable pods turn over faster than the primary frame",
        "es": "la tensión del tirante escala con la relación de brazos de palanca, la regla de Maxwell cuenta hiperestaticidad frente a mecanismos y las cápsulas se renuevan más rápido que el marco",
    },
    "a05": {
        "en": "room reverberation time scales with volume divided by logarithmic surface absorption, targeting clear speech intelligibility across the hall",
        "es": "el tiempo de reverberación escala con el volumen dividido por la absorción logarítmica de las superficies para sostener una inteligibilidad clara de la voz",
    },
    "a06": {
        "en": "wetland effluent concentration decays exponentially toward background levels with hydraulic residence time before ultraviolet disinfection reduces residual pathogens",
        "es": "la concentración del humedal decae exponencialmente hacia el nivel base con el tiempo de residencia antes de que la desinfección ultravioleta reduzca patógenos residuales",
    },
    "a07": {
        "en": "pigment absorption-to-scattering ratio sets surface reflectance, while inter-reflected radiosity integrates light bouncing between colored walls",
        "es": "la relación entre absorción y dispersión del pigmento fija la reflectancia superficial, mientras la radiosidad integra la luz que rebota entre los muros de color",
    },
    "a08": {
        "en": "net daytime sky-cooling subtracts atmospheric, solar, and convective heat gains from infrared radiation, while phase-change melting fronts advance with the square root of time",
        "es": "el enfriamiento radiativo diurno resta las ganancias atmosféricas, solares y convectivas a la emisión infrarroja, mientras el frente de cambio de fase avanza con la raíz del tiempo",
    },
    "a09": {
        "en": "bilayer timber curvature bends in proportion to moisture change and differential swelling, weighted by the thickness and stiffness ratio of the two wood layers",
        "es": "la curvatura de una madera bicapa se flexiona en proporción al cambio de humedad y expansión diferencial, ponderada por el espesor y la rigidez de ambas capas",
    },
    "a10": {
        "en": "Miura-ori fold angles couple geometrically to produce a negative Poisson ratio that expands laterally when stretched, while opposite crease angles sum to a straight angle",
        "es": "los ángulos de plegado Miura-ori se acoplan geométricamente generando un coeficiente de Poisson negativo que se expande al estirarse, mientras los ángulos opuestos suman ciento ochenta grados",
    },
    "a11": {
        "en": "a concave Airy stress surface maps second derivatives to compression-only forces, and in three dimensions each bar force scales with the area of its dual polyhedral face",
        "es": "una superficie de Airy cóncava traduce segundas derivadas en fuerzas de compresión pura, y en tres dimensiones cada barra escala con el área de su cara poliédrica dual",
    },
    "a12": {
        "en": "tensegrity equilibrium balances member forces against loads while prestress adds geometric stiffness, paired with net radiative heat rejection to the sky",
        "es": "el equilibrio de tensegridad balancea fuerzas con cargas mientras el pretensado aporta rigidez geométrica, combinado con el rechazo radiativo neto de calor hacia el cielo",
    },
    "a13": {
        "en": "spherical dome radius and membrane stress follow span, rise, and thickness, while practical buckling capacity applies an imperfection knockdown to the classical shell threshold",
        "es": "el radio y el esfuerzo de membrana de la cúpula siguen claro, flecha y espesor, mientras el pandeo real aplica un factor de reducción por imperfecciones al límite clásico",
    },
    "a14": {
        "en": "a hyperbolic paraboloid saddle carries uniform vertical load as constant in-plane membrane shear, resolving into equal principal tension and compression with minimal bending",
        "es": "un paraboloide hiperbólico transmite carga uniforme como cortante constante de membrana, resuelto en tensiones principales iguales de tracción y compresión con flexión mínima",
    },
    # Physics (P.01 - P.12)
    "p01": {
        "en": "equilibrium fluctuation covariance tracks entropy curvature, while chemical affinity equals thermal energy times the log ratio of forward to reverse transition rates",
        "es": "la covarianza de fluctuaciones sigue la curvatura de la entropía, mientras la afinidad química equivale a la energía térmica por el logaritmo de tasas directas e inversas",
    },
    "p02": {
        "en": "coupled oscillators advance at their natural beat frequency shifted by phase-lagged neighbor interactions, driving a metachronal wave at wavelength times beat frequency",
        "es": "los osciladores acoplados avanzan a su frecuencia natural modulada por vecinos desfasados, impulsando una onda metacrónica cuya velocidad es longitud de onda por frecuencia",
    },
    "p03": {
        "en": "mucus viscosity thins smoothly with shear rate between high and low plateaus, while polymer mesh spacing shrinks as a power law of concentration",
        "es": "la viscosidad del moco disminuye suavemente con la velocidad de corte entre dos mesetas, mientras el tamaño de malla polimérica se reduce como ley de potencias de la concentración",
    },
    "p04": {
        "en": "ion flux combines diffusion with electrical drift, while periciliary fluid height changes with hydraulic permeability times the balance of osmotic and hydrostatic pressures",
        "es": "el flujo iónico combina difusión con arrastre eléctrico, mientras la altura del líquido periciliar cambia según la permeabilidad hidráulica por el balance osmótico e hidrostático",
    },
    "p05": {
        "en": "quantum tunneling probability drops exponentially with barrier width and height, producing a measurable kinetic isotope ratio between hydrogen and deuterium transfer",
        "es": "la probabilidad de tunelamiento cuántico cae exponencialmente con el ancho y la altura de la barrera, generando una relación isotópica medible entre hidrógeno y deuterio",
    },
    "p06": {
        "en": "long polymer chains escape their entangled tubes in a disengagement time growing with chain length cubed, so reptation diffusivity drops with length squared",
        "es": "las cadenas poliméricas largas escapan de su tubo enredado en un tiempo que crece al cubo de su longitud, por lo que su difusión cae con el cuadrado de la longitud",
    },
    "p07": {
        "en": "underfloor suction tracks local speed squared, vortex circulation seals the floor edge, and vertical suspension oscillation couples ride height to aerodynamic downforce",
        "es": "la succión del piso sigue el cuadrado de la velocidad local, la circulación de vórtices sella el borde y la oscilación vertical acopla la altura de marcha con la carga aerodinámica",
    },
    "p08": {
        "en": "thin-film color peaks when optical path difference matches whole wavelengths, while microfacet reflectance blends diffuse pigment scatter with angle-dependent specular sheen",
        "es": "el color de película delgada destaca cuando la diferencia de camino óptico iguala longitudes de onda enteras, mientras la reflectancia combina difusión y brillo especular",
    },
    "p09": {
        "en": "electrostatic pull balances surface tension at the 49.3-degree Taylor cone angle, while the Rayleigh charge limit and flow scaling set droplet fission and diameter",
        "es": "la atracción electrostática equilibra la tensión superficial en el cono de Taylor de 49.3 grados, mientras el límite de Rayleigh y el caudal fijan la fisión y el diámetro de gota",
    },
    "p10": {
        "en": "integrating Berry curvature over the Brillouin zone yields an integer Chern number, turning on a one-way chiral edge mode when time-reversal breaking outweighs parity breaking",
        "es": "integrar la curvatura de Berry en la zona de Brillouin da un número de Chern entero, activando un modo de borde unidireccional cuando domina la ruptura temporal sobre la de paridad",
    },
    "p11": {
        "en": "surface-code logical error drops exponentially with code distance below threshold while commuting stabilizers protect qubits, alongside the ground-state energy problem for nitrogenase catalysis",
        "es": "el error lógico del código de superficie cae exponencialmente con la distancia bajo el umbral mientras los estabilizadores conmutan, junto al problema de energía basal en catálisis",
    },
    "p12": {
        "en": "the thermodynamic uncertainty relation bounds current precision by entropy production, while small Knudsen numbers bridge Boltzmann particle kinetics to viscous fluid dissipation",
        "es": "la relación de incertidumbre termodinámica acota la precisión del flujo mediante la producción de entropía, mientras números de Knudsen pequeños conectan la cinética de Boltzmann con la viscosidad",
    },
    # Math (M.01 - M.15)
    "m01": {
        "en": "modularity lifting equates deformation rings with Hecke algebras to connect elliptic curves and modular forms, alongside sparsification bounds for counting satisfiability",
        "es": "el levantamiento de modularidad identifica anillos de deformación con álgebras de Hecke para unir curvas elípticas y formas modulares, junto a cotas de dispersión en conteo booleano",
    },
    "m02": {
        "en": "large-sieve inequalities bound how many zeta zeros can lie off the critical line in a given strip, framing the published zero-density estimates",
        "es": "las desigualdades de gran criba acotan cuántos ceros de zeta pueden quedar fuera de la recta crítica en una franja dada, enmarcando las estimaciones de densidad",
    },
    "m03": {
        "en": "cap-set bounds limit three-term-progression-free subsets in ternary spaces, paired with low-rank tensor decompositions for fast matrix multiplication",
        "es": "las cotas de conjuntos gorra limitan subconjuntos sin progresiones de tres términos en espacios ternarios, junto a descomposiciones tensoriales de bajo rango para multiplicar matrices",
    },
    "m04": {
        "en": "entropy calculus bounds how closely a set with small doubling sits inside a subgroup, alongside automated equational deduction across millions of magma-law pairs",
        "es": "el cálculo de entropía acota cuán cerca queda un conjunto de duplicación pequeña de un subgrupo, junto a deducción ecuacional automatizada sobre millones de pares de magmas",
    },
    "m05": {
        "en": "deductive closure with algebraic rules searches geometric constructions while a vanishing Cayley–Menger determinant checks whether five distances embed in three-dimensional space",
        "es": "el cierre deductivo con reglas algebraicas busca construcciones geométricas mientras el determinante de Cayley–Menger verifica si cinco distancias encajan en tres dimensiones",
    },
    "m06": {
        "en": "fine-grained reductions link sub-cubic shortest-path algorithms to 3SUM hardness, paired with step-level process reward models that score intermediate reasoning",
        "es": "las reducciones de grano fino enlazan algoritmos subcúbicos de caminos mínimos con la dificultad de 3SUM, junto a modelos de recompensa paso a paso para el razonamiento",
    },
    "m07": {
        "en": "Pontryagin's Hamiltonian trades lap time against electrical battery draw along the circuit, while a Fourier neural operator approximates the flow in frequency space",
        "es": "el hamiltoniano de Pontryagin intercambia tiempo de vuelta frente al consumo eléctrico de batería en el circuito, mientras un operador neuronal de Fourier aproxima la dinámica en frecuencia",
    },
    "m08": {
        "en": "cone-response projection maps light spectra into three-dimensional color space, where a Riemannian metric tensor defines perceptual distance and shortest geodesic curves",
        "es": "la proyección de conos mapea espectros de luz a un espacio de color tridimensional, donde un tensor métrico riemanniano define distancias perceptuales y curvas geodésicas",
    },
    "m09": {
        "en": "Wasserstein-2 optimal transport finds the least-kinetic-energy fluid path moving one probability density into another under mass conservation and Hamilton–Jacobi flow",
        "es": "el transporte óptimo de Wasserstein-2 busca el flujo de mínima energía cinética que lleva una densidad de probabilidad a otra bajo conservación de masa y dinámica de Hamilton–Jacobi",
    },
    "m10": {
        "en": "the boundary of a boundary vanishes, Betti numbers count holes persisting across scales, and bottleneck distance between barcodes stays bounded by input perturbation",
        "es": "la frontera de una frontera se anula, los números de Betti cuentan agujeros persistentes entre escalas y la distancia entre códigos de barras queda acotada por la perturbación",
    },
    "m11": {
        "en": "the Wang–Zahl preprint addresses full three-dimensional dimension for Kakeya needle sets, alongside the Guth–Maynard zero-density bound for Riemann zeta zeros",
        "es": "el preimpreso de Wang y Zahl aborda la dimensión completa tres para conjuntos de Kakeya, junto a la cota de densidad de ceros de Guth y Maynard para la función zeta",
    },
    "m12": {
        "en": "module learning-with-errors hides a secret vector behind modular matrix multiplication plus small noise at prime modulus 3329 and dimension 256 in NIST FIPS 203",
        "es": "el aprendizaje con errores sobre módulos oculta un vector secreto mediante multiplicación matricial modular más ruido pequeño con módulo primo 3329 y dimensión 256 en NIST FIPS 203",
    },
    "m13": {
        "en": "the Lovász theta number sandwiches Shannon's zero-error graph capacity between independence number and fractional covering, evaluating in closed form on odd cycles",
        "es": "el número theta de Lovász acota la capacidad de error cero de Shannon entre el número de independencia y el recubrimiento fraccional, con expresión cerrada en ciclos impares",
    },
    "m14": {
        "en": "Cohn–Elkies auxiliary functions with controlled sign and Fourier transform upper-bound sphere packing density, matching the optimal E8 and Leech lattices in dimensions 8 and 24",
        "es": "las funciones auxiliares de Cohn y Elkies con signo y transformada de Fourier acotan la densidad de empaquetamiento de esferas, coincidiendo con las redes óptimas en dimensiones 8 y 24",
    },
    "m15": {
        "en": "expected monochromatic cliques set the probabilistic lower floor for diagonal Ramsey numbers, framing the exponential growth rate between root two and below four",
        "es": "el número esperado de cliques monocromáticos fija el piso probabilístico para los números de Ramsey diagonales, enmarcando su tasa exponencial entre raíz de dos y menos de cuatro",
    },
    # Bounties (B.01 - B.06)
    "b01": {
        "en": "a Sidon set has all pairwise sums distinct, limiting how many elements can fit inside an interval up to roughly the square root of its size",
        "es": "un conjunto de Sidon mantiene todas sus sumas por pares distintas, limitando cuántos elementos caben en un intervalo a cerca de la raíz cuadrada de su tamaño",
    },
    "b02": {
        "en": "logical error rate falls rapidly with surface-code distance below physical error threshold while physical qubit count scales quadratically with distance",
        "es": "la tasa de error lógico cae rápidamente con la distancia del código de superficie bajo el umbral físico mientras el conteo de cúbits físicos crece cuadráticamente con la distancia",
    },
    "b03": {
        "en": "net embodied carbon equals scaled baseline emissions minus mineralized carbon uptake, balanced against a nonlinear cost-premium curve as material volume drops",
        "es": "el carbono incorporado neto resta el carbono mineralizado a las emisiones escaladas del volumen, equilibrado frente a una curva no lineal de costo al reducir material",
    },
    "b04": {
        "en": "closed force polyhedra keep a masonry vault in equilibrium without steel rebar, paired with net sky-cooling heat flux balancing infrared emission against solar and atmospheric gain",
        "es": "los poliedros de fuerzas cerrados mantienen una bóveda en equilibrio sin acero de refuerzo, junto al flujo neto de enfriamiento radiativo que equilibra emisión infrarroja y ganancia solar",
    },
    "b05": {
        "en": "sparse thresholding recovers a Burgers-type transport equation from noisy fields while minimum description length balances data fit against expression complexity",
        "es": "el umbralizado disperso recupera una ecuación de transporte tipo Burgers desde datos ruidosos mientras la longitud mínima de descripción equilibra ajuste y complejidad",
    },
    "b06": {
        "en": "gauge-anomaly traces vanish for consistent hypercharge assignments, while entanglement entropy in a critical spin chain grows logarithmically within the tensor-network bond budget",
        "es": "las trazas de anomalía de norma se anulan para asignaciones consistentes de hipercarga, mientras la entropía de entrelazamiento en una cadena crítica crece logarítmicamente bajo el presupuesto tensorial",
    },
    # Toolchain (X.01 - X.07)
    "x01": {
        "en": "signed tetrahedron volumes sum to total closed-mesh volume, Euler's formula links vertices, edges, and faces to genus, and watertight triangle meshes satisfy three faces equal two edges",
        "es": "los volúmenes signados de tetraedros suman el volumen cerrado, la fórmula de Euler liga vértices, aristas y caras al género y una malla triangular cerrada cumple tres caras por dos aristas",
    },
    "x02": {
        "en": "chordal sagitta error shrinks as circle tessellation increases, while solid volume sums flange and boss within a tight relative tolerance across CAD export formats",
        "es": "el error de sagita disminuye al refinar la teselación circular, mientras el volumen sólido suma brida y saliente con tolerancia estrecha entre formatos de exportación CAD",
    },
    "x03": {
        "en": "arch thrust and middle-third eccentricity check masonry equilibrium, Euler count tracks timber mesh topology, and infrared sky-cooling flux targets clear-sky heat rejection",
        "es": "el empuje del arco y la excentricidad del tercio medio revisan el equilibrio, el conteo de Euler verifica la topología y el flujo infrarrojo estima el rechazo térmico al cielo",
    },
    "x04": {
        "en": "alternating crease angles sum to zero for flat-foldable origami, mountain-valley counts differ by two at each vertex, and solid volume equals projected area times thickness",
        "es": "los ángulos alternados de pliegue suman cero en origami plegable en plano, los pliegues monte y valle difieren en dos por vértice y el volumen iguala el área por espesor",
    },
    "x05": {
        "en": "frustum slice volumes sum to total strut volume while face-normal inclination checks that every printable wall overhang stays within the 45-degree build-plate angle limit",
        "es": "los volúmenes de troncos suman el volumen total del puntal mientras la inclinación normal de cada cara verifica que ningún voladizo supere el límite de 45 grados en impresión",
    },
    "x06": {
        "en": "Euler characteristic zero marks a genus-one toroidal unit cell with two independent loops, while outer-minus-inner volume sets the acoustic fill fraction",
        "es": "la característica de Euler cero marca una celda unitaria toroidal de género uno con dos ciclos independientes, mientras la diferencia de volúmenes fija la fracción de relleno acústico",
    },
    "x07": {
        "en": "angle defects across all mesh vertices sum to two pi times the Euler characteristic, and non-negative cotangent weights check well-shaped Delaunay-like triangles",
        "es": "los defectos angulares en todos los vértices suman dos pi por la característica de Euler, y pesos cotangentes no negativos verifican triángulos bien condicionados",
    },
}


def resolve_law_gloss(folio_or_slug: dict | str, lang: str = "en") -> str:
    """Return the plain-language gloss for a folio dict or slug in 'en' or 'es', or '' if unset."""
    key = "es" if str(lang).lower().startswith("es") else "en"
    if isinstance(folio_or_slug, dict):
        direct = str(folio_or_slug.get(f"law_gloss_{key}", "") or "").strip()
        if direct:
            return direct
        slug = str(folio_or_slug.get("slug", "") or "").strip().lower()
    else:
        slug = str(folio_or_slug or "").strip().lower()
    return LAW_GLOSSES.get(slug, {}).get(key, "")
