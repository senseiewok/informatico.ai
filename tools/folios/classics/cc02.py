"""CC.02 · One Stone Forest, Eight Moves — La Sagrada Família as an Engineering Story (single source of truth).

Every factual claim on the page lives in this module beside the primary source it came from. Architectural and
historical accounts draw from the Basílica de la Sagrada Família official pages, Arup/Ingenia engineering dispatches,
and peer-reviewed architectural heritage, masonry limit analysis, and concrete papers checked in Crossref and Scite
on 2026-11-15.

- Model inputs for interactive benches live in tools/folios/classics/cc02_mechanics.py and are marked MODEL.
- General mechanics papers (Heyman 1966, Akbarzadeh et al. 2015, Eyring 1930) explain general mathematical and
  physical mechanisms and did not test the Sagrada Família; the page states this beside each reference.
- Anything a source does not state is labeled "not stated" and summarized in SILENT.
"""
from __future__ import annotations

SLUG = "sagrada-familia"
CODE = "CC.02"
DATE = "2026-11-15"
ACCESSED = "2026-11-15"

SEO = (
    "One Stone Forest, Eight Moves: La Sagrada Família",
    "Eight architectural moves across 144 years of the Sagrada Família: catenaries, ruled hyperboloids, double-twisted columns and tensioned stone.",
    "Un bosque de piedra, ocho jugadas: Sagrada Família",
    "Ocho jugadas arquitectónicas en 144 años de la Sagrada Família: catenarias, hiperboloides reglados, columnas de doble giro y piedra pretensada.",
)

# ---------------------------------------------------------------------------------------------------------------
# Sources. "kind": basilica (official Sagrada Familia pages), eng (engineering journal), paper (peer-reviewed DOI
# checked in Crossref and Scite on 2026-11-15; no retraction notice found).
# ---------------------------------------------------------------------------------------------------------------
SOURCES = {
    "sf-history": {
        "short": "Basílica history",
        "short_es": "Basílica historia",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “History of the Temple” (1882 foundation, crypt, facades, 1936 loss and 2026 centenary)",
        "url": "https://sagradafamilia.org/en/history-of-the-temple",
    },
    "sf-architecture": {
        "short": "Basílica architecture",
        "short_es": "Basílica arquitectura",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “Architecture” (ruled surfaces: hyperboloids, paraboloids, helicoids and conoids)",
        "url": "https://sagradafamilia.org/en/architecture",
    },
    "sf-columns": {
        "short": "Basílica columns",
        "short_es": "Basílica columnas",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “The Columns” (12/10/8/6-point star bases, double twist, 2n m height rule and 1:10 shaft ratio)",
        "url": "https://sagradafamilia.org/en/the-columns",
    },
    "sf-towers": {
        "short": "Basílica towers",
        "short_es": "Basílica torres",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “Towers” (18 parabolic-profile towers, 172.5 m Tower of Jesus Christ, 138 m Virgin Mary, 135 m Evangelists)",
        "url": "https://sagradafamilia.org/en/towers",
    },
    "sf-centenary": {
        "short": "Basílica 2026 cross",
        "short_es": "Basílica cruz 2026",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “Tower of Jesus Christ” (upper arm of the cross placed February 2026, 172.5 m total height, June 10, 2026 inauguration)",
        "url": "https://sagradafamilia.org/en/tower-of-jesus-christ",
    },
    "ingenia-arup": {
        "short": "Ingenia / Arup",
        "short_es": "Ingenia / Arup",
        "kind": "eng",
        "label": "Tristram Carfrae & Hugh Ferguson, “Completing the Sagrada Família”, Ingenia (Royal Academy of Engineering): prefabricated post-tensioned stone panels",
        "url": "https://www.ingenia.org.uk/articles/completing-the-sagrada-familia/",
    },
    "gomez2009": {
        "short": "Gómez-Serrano 2009",
        "kind": "paper",
        "label": "Gómez-Serrano, Espel, Grima, Burry & Aguado (2009). Evolution of the Formwork Used in the Temple of the Sagrada Família. International Journal of Architectural Heritage 3(2), 93–109",
        "url": "https://doi.org/10.1080/15583050802226470",
    },
    "grima2007": {
        "short": "Grima et al. 2007",
        "kind": "paper",
        "label": "Grima, Gómez Serrano & Aguado (2007). The Use of Concrete in Gaudi's Sagrada Familia. International Journal of Architectural Heritage 1(4), 366–379",
        "url": "https://doi.org/10.1080/15583050701476630",
    },
    "gomezramio2014": {
        "short": "Gómez-Ramió 2014",
        "kind": "paper",
        "label": "Gómez-Ramió, Cavalaro & Aguado (2014). The Trencadis Mosaic on the Pinnacles of the Sagrada Familia Cathedral. International Journal of Architectural Heritage 8(5), 760–782",
        "url": "https://doi.org/10.1080/15583058.2013.834089",
    },
    "rodriguez2017": {
        "short": "Rodríguez 2017",
        "kind": "paper",
        "label": "Rodríguez, Blanco, Pujadas & Aguado (2017). Self-Compacting Concrete in the Temple of Sagrada Familia. Journal of Architectural Engineering 23(3), 04017011",
        "url": "https://doi.org/10.1061/(asce)ae.1943-5568.0000249",
    },
    "cortes2019": {
        "short": "Cortés et al. 2019",
        "kind": "paper",
        "label": "Cortés, Samper & Herrera (2019). Determinación geométrica de los paraboloides hiperbólicos de las bóvedas del pórtico de acceso a la Cripta de la Colonia Güell. Informes de la Construcción 71(554), e295",
        "url": "https://doi.org/10.3989/ic.63691",
    },
    "heyman1966": {
        "short": "Heyman 1966",
        "kind": "paper",
        "label": "Heyman, J. (1966). The Stone Skeleton. International Journal of Solids and Structures 2(2), 249–279",
        "url": "https://doi.org/10.1016/0020-7683(66)90018-7",
    },
    "akbarzadeh2015": {
        "short": "Akbarzadeh 2015",
        "kind": "paper",
        "label": "Akbarzadeh, Van Mele & Block (2015). On the equilibrium of funicular polyhedral frames and convex polyhedral force diagrams. Computer-Aided Design 63, 118–128",
        "url": "https://doi.org/10.1016/j.cad.2015.01.006",
    },
    "dyakova2025": {
        "short": "Dyakova et al. 2025",
        "kind": "paper",
        "label": "Dyakova, Nordström & Benedict (2025). Image statistics substantiate Gaudí’s naturalistic design principles. Scientific Reports 15, 20015",
        "url": "https://doi.org/10.1038/s41598-025-06007-8",
    },
    "eyring1930": {
        "short": "Eyring 1930",
        "kind": "paper",
        "label": "Eyring, C. F. (1930). Reverberation Time in “Dead” Rooms. Journal of the Acoustical Society of America 1(2A), 217–241",
        "url": "https://doi.org/10.1121/1.1901884",
    },
}

KIND_LABEL = {
    "basilica": ("Basílica", "Basílica"),
    "eng": ("Engineering", "Ingeniería"),
    "paper": ("Paper", "Artículo"),
}

HERO = {
    "kicker_en": "Cult Classics · CC.02 · Architecture & Stereotomy",
    "kicker_es": "Clásicos de Culto · CC.02 · Arquitectura y Estereotomía",
    "title_en": "One Stone Forest, Eight Moves",
    "title_es": "Un bosque de piedra, ocho jugadas",
    "dek_en": "La Sagrada Família (1882–2026), told one structural and geometric move at a time.",
    "dek_es": "La Sagrada Família (1882–2026), contada jugada estructural y geométrica por jugada.",
    "reading_en": "18 min read",
    "reading_es": "20 min de lectura",
}

BRIEF_NOTE = {
    "en": "The structural problem behind Antoni Gaudí’s church: carry a 172.5 m crown of stone towers and sunlit vaults without external flying buttresses, using shapes a stonecutter can generate with straight lines. Each move below tracks how one generation of builders solved the next boundary of that problem.",
    "es": "El problema estructural detrás de la basílica de Antoni Gaudí: sostener una corona de torres de 172.5 m y bóvedas iluminadas sin arbotantes exteriores, usando superficies que un cantero puede trazar con líneas rectas. Cada jugada abajo muestra cómo una generación de constructores resolvió el siguiente tramo del problema.",
}

OPENING = [
    {
        "en": "In February 2026, cranes above Eixample lifted the upper arm of a 17 m ceramic-and-glass cross onto the central lantern of the Basílica de la Sagrada Família, bringing the Tower of Jesus Christ to 172.5 m—the height of the temple completed on June 10, 2026, a century to the day after Antoni Gaudí’s death. About 5.2 m shy of Montjuïc hill (177.7 m), the central spire rests on foundations first laid in 1882.",
        "es": "En febrero de 2026, las grúas sobre el Eixample izaron el brazo superior de una cruz de cerámica y vidrio de 17 m sobre el cimborrio central de la Basílica de la Sagrada Família, llevando la torre de Jesucristo a 172.5 m: la altura final inaugurada el 10 de junio de 2026, justo cien años después de la muerte de Antoni Gaudí. Unos 5.2 m por debajo de la montaña de Montjuïc (177.7 m), la aguja central se apoya sobre cimientos iniciados en 1882.",
        "src": ["sf-history", "sf-towers", "sf-centenary"],
    },
    {
        "en": "Between the Neo-Gothic crypt started by Francisco de Paula del Villar in 1882 and the pre-tensioned stone panels hoisted 144 years later sits one unbroken thread: turning gravity and geometry into each other’s keeper. Instead of propping vertical nave walls from outside with Gothic buttresses, Gaudí leaned columns inward along the inverted catenary thrust, twisted star polygons upward in four kinds of stone, and ruled the vaults with straight lines so plasterers, masons, and eventually five-axis CNC saws could cut curved stone along flat strings.",
        "es": "Entre la cripta neogótica iniciada por Francisco de Paula del Villar en 1882 y los paneles de piedra pretensada izados 144 años después corre un mismo hilo: hacer que la gravedad y la geometría se custodien mutuamente. En lugar de apuntalar muros verticales desde afuera con arbotantes góticos, Gaudí inclinó las columnas hacia adentro siguiendo el empuje catenario invertido, giró polígonos estrellados en cuatro tipos de piedra y regló las bóvedas con rectas para que yeseros, canteros y, más tarde, sierras CNC de cinco ejes cortaran piedra curva siguiendo cuerdas rectas.",
        "src": ["sf-architecture", "sf-columns", "ingenia-arup"],
    },
]

# ---------------------------------------------------------------------------------------------------------------
# Eight tectonic moves across five chronological Parts
# ---------------------------------------------------------------------------------------------------------------
CARDS = [
    {
        "id": "m1",
        "era": "1882",
        "move_en": "1882 · The Neo-Gothic Crypt",
        "move_es": "1882 · La cripta neogótica",
        "years": "1882–1883",
        "title_en": "Inheriting a stone footprint",
        "title_es": "Heredar una huella de piedra",
        "body_en": "Francisco de Paula del Villar laid the first stone on March 19, 1882, in traditional Neo-Gothic form before stepping down the next year. When the 31-year-old Antoni Gaudí took over in 1883, the crypt piers and radial footprint were already rising out of Barcelona clay—fixing the ground plan that every upper tower would later have to respect.",
        "body_es": "Francisco de Paula del Villar colocó la primera piedra el 19 de marzo de 1882 en clave neogótica tradicional antes de renunciar al año siguiente. Cuando Antoni Gaudí asumió la dirección en 1883, a los 31 años, los pilares y el trazado radial de la cripta ya emergían del terreno, fijando la huella en planta que todas las torres superiores tendrían que respetar.",
        "plate": [
            ("First stone", "Primera piedra", "1882-03-19", "sf-history"),
            ("Initial architect", "Arquitecto inicial", "F. de Paula del Villar", "sf-history"),
            ("Gaudí takes over", "Gaudí asume la obra", "1883", "sf-history"),
            ("Structural constraint", "Límite estructural", "Fixed 19th-century crypt plan", "ingenia-arup"),
        ],
        "egg": False,
    },
    {
        "id": "m2",
        "era": "1884–1914",
        "move_en": "1884–1914 · Hanging Cords & Nativity",
        "move_es": "1884–1914 · Catenarias y Fachada del Nacimiento",
        "years": "1884–1914",
        "title_en": "Inverting gravity before cutting stone",
        "title_es": "Invertir la gravedad antes de labrar piedra",
        "body_en": "Across the Nativity facade and especially in the parallel Colònia Güell study (1898–1908), Gaudí hung fine cords and little shot bags upside down. Under self-weight, tension chains choose the path with zero bending moment; mirrored vertically, stone piers slanted along that line carry the load in pure compression without external flying buttresses.",
        "body_es": "Mientras alzaba la fachada del Nacimiento y en paralelo en su estudio para la Colònia Güell (1898–1908), Gaudí colgó cordeles finos con saquitos de perdigones boca abajo. Bajo su propio peso, la cadena en tensión adopta la curva de momento flector nulo; invertida en vertical, la columna inclinada sobre esa línea conduce la carga en compresión pura sin arbotantes exteriores.",
        "plate": [
            ("Governing curve", "Curva rectora", "y = a·cosh(x/a) (MODEL)", "heyman1966"),
            ("External buttresses", "Arbotantes exteriores", "Omitted via inclined columns", "sf-architecture"),
            ("Nativity tower range", "Rango torres Nacimiento", "~98.4 m to ~107 m", "sf-towers"),
            ("Early concrete use", "Primeros hormigones", "Non-structural pinnacles & cores", "grima2007"),
        ],
        "egg": False,
    },
    {
        "id": "m3",
        "era": "1914–1926",
        "move_en": "1914–1926 · Ruled Surfaces & The Stone Forest",
        "move_es": "1914–1926 · Superficies regladas y bosque de piedra",
        "years": "1914–1926",
        "title_en": "Curved stone built from straight lines",
        "title_es": "Piedra curva generada con líneas rectas",
        "body_en": "After 1914 Gaudí devoted himself wholly to the temple, codifying a geometry of four ruled families: one-sheet hyperboloids for skylights and vaults, hyperbolic paraboloids as saddle transitions, helicoids for double-twisted columns and spiral stairs, and conoids for the Schools roof. Four column stone tiers—12-point red porphyry, 10-point basalt, 8-point gray granite, and 6-point Montjuïc sandstone—scale in total height as 2n meters with a 1:10 inner-diameter-to-shaft rule.",
        "body_es": "Desde 1914 Gaudí se dedicó por entero al templo y codificó una geometría de cuatro familias regladas: hiperboloides de una hoja en óculos y bóvedas, paraboloides hiperbólicos como sillas de transición, helicoides en columnas de doble giro y escaleras, y conoides en la cubierta de las Escuelas. Cuatro rangos de piedra —pórfido rojo de 12 puntas, basalto de 10, granito gris de 8 y arenisca de Montjuïc de 6— escalan su altura total a 2n metros con relación 1:10 entre diámetro interior y fuste.",
        "plate": [
            ("Ruled families", "Familias regladas", "Hyperboloid, paraboloid, helicoid, conoid", "sf-architecture"),
            ("Crossing pillars (4)", "Pilares crucero (4)", "12-pt red porphyry · 24 m total", "sf-columns"),
            ("Shaft-to-diameter rule", "Regla fuste-diámetro", "1:10 (H_shaft = 10·D_in)", "sf-columns"),
            ("Column tree branching", "Ramificación arbórea", "Naturalistic 2025 image study", "dyakova2025"),
        ],
        "egg": False,
    },
    {
        "id": "m4",
        "era": "1936–1952",
        "move_en": "1936–1952 · Plaster Shards & Parametric Rules",
        "move_es": "1936–1952 · Fragmentos de yeso y reglas paramétricas",
        "years": "1936–1952",
        "title_en": "Reassembling geometry from fragments",
        "title_es": "Reconstruir la geometría desde fragmentos",
        "body_en": "When fire swept Gaudí’s studio in July 1936, drawings burned and 1:10 and 1:25 plaster models shattered. Disciples Francesc Quintana, Isidre Puig-Boada, and Lluís Bonet i Garí gathered the gypsum shards; because ruled quadrics are governed by ratios rather than freehand arcs, surviving fragments preserved the slope parameters needed to reconstruct the nave bays.",
        "body_es": "Cuando el incendio de julio de 1936 arrasó el obrador de Gaudí, los planos ardieron y las maquetas de yeso a escalas 1:10 y 1:25 quedaron hechas añicos. Sus discípulos Francesc Quintana, Isidre Puig-Boada y Lluís Bonet i Garí reunieron los fragmentos; como las cuádricas regladas obedecen proporciones y no arcos arbitrarios, las piezas sobrevivientes conservaron los parámetros para reconstruir las naves.",
        "plate": [
            ("Studio fire", "Incendio del obrador", "July 1936", "sf-history"),
            ("Model scales", "Escalas de maqueta", "1:10 and 1:25 plaster casts", "sf-history"),
            ("Formwork evolution", "Evolución de encofrados", "Timber strings to precast", "gomez2009"),
            ("Natural stone vs concrete", "Piedra y hormigón", "Structural formwork shells", "grima2007"),
        ],
        "egg": True,
    },
    {
        "id": "m5",
        "era": "1954–1986",
        "move_en": "1954–1986 · Passion Facade & Taut Bones",
        "move_es": "1954–1986 · Fachada de la Pasión y huesos tensos",
        "years": "1954–1986",
        "title_en": "Reading the compression diagram in the open",
        "title_es": "Dejar a la vista el diagrama de compresión",
        "body_en": "Excavations for the Passion facade began in 1954, exposing six colossal inclined stone ribs angled like taut tendons along the thrust line—Gaudí’s structural bare bones laid outside the glass. Higher up, self-compacting concrete entered the complex ruled vaults while Catalan trencadís ceramic mosaic waterproofed the pinnacles above Barcelona.",
        "body_es": "Las excavaciones de la fachada de la Pasión comenzaron en 1954 y dejaron al descubierto seis monumentales pilares inclinados como tendones tensos sobre la línea de empuje: el esqueleto estructural expuesto fuera del vitral. En altura, el hormigón autocompactante llenó las bóvedas regladas mientras el trencadís cerámico impermeabilizaba los pináculos.",
        "plate": [
            ("Passion work begins", "Inicio fachada Pasión", "1954", "sf-history"),
            ("Passion tower range", "Rango torres Pasión", "~107.4 m to ~112.2 m", "sf-towers"),
            ("Pinnacle trencadís", "Trencadís en pináculos", "Glazed ceramic weather shell", "gomezramio2014"),
            ("Self-compacting mixes", "Hormigón autocompactante", "Tight hyperboloid rebar pours", "rodriguez2017"),
        ],
        "egg": False,
    },
    {
        "id": "m6",
        "era": "1979–2010",
        "move_en": "1979–2010 · CAD, Stereotomy & The Sunlit Nave",
        "move_es": "1979–2010 · CAD, estereotomía y la nave iluminada",
        "years": "1979–2010",
        "title_en": "Translating plaster rulings into five-axis stone",
        "title_es": "Traducir el yeso reglado a corte en cinco ejes",
        "body_en": "Starting in 1979, architect Mark Burry and the Barcelona team translated Gaudí’s second-order ruled equations into parametric CAD scripts originally borrowed from aeronautical and automotive surfacing. Five-axis diamond wire saws sliced straight rulings across blocks to close the 45 m central nave vaults, dedicated as a minor basilica in 2010.",
        "body_es": "Desde 1979, el arquitecto Mark Burry y el equipo de Barcelona tradujeron las ecuaciones regladas de segundo orden a guiones CAD paramétricos adaptados del diseño aeronáutico. Sierras de hilo diamantado de cinco ejes cortaron rectas sobre bloques de piedra para cerrar las bóvedas de la nave central (45 m), dedicada como basílica menor en 2010.",
        "plate": [
            ("Parametric CAD shift", "Salto a CAD paramétrico", "From 1979 onward", "gomez2009"),
            ("Formwork method", "Método constructivo", "Straight wire-cut rules on stone", "gomez2009"),
            ("Nave vault dedication", "Dedicación de la nave", "2010", "sf-history"),
            ("Vault acoustic theory", "Teoría acústica de bóvedas", "Eyring 1930 absorption model", "eyring1930"),
        ],
        "egg": False,
    },
    {
        "id": "m7",
        "era": "2016–2026",
        "move_en": "2016–2026 · Tensioned Stone & The 172.5 m Crown",
        "move_es": "2016–2026 · Piedra pretensada y la corona de 172.5 m",
        "years": "2016–2026",
        "title_en": "Halving tower mass to save the 1882 crypt",
        "title_es": "Reducir a la mitad la masa de las torres sobre 1882",
        "body_en": "Building six central lanterns above the 19th-century crossing piers risked overloading historic foundations with conventional solid masonry or concrete cores. Working with Arup, the Basílica engineers developed prefabricated stone panels threaded with stainless post-tensioning bars: squeezing stone under pre-compression keeps windward mortar joints shut without excess weight, completing the Virgin Mary tower (138 m), the four Evangelists (135 m), and the 172.5 m Tower of Jesus Christ topped in February 2026 and inaugurated June 10, 2026.",
        "body_es": "Alzar los seis cimborrios centrales sobre los pilares del siglo XIX arriesgaba sobrecargar la cimentación histórica si se usaba mampostería maciza o núcleo pesado de hormigón. Con Arup, los ingenieros desarrollaron paneles prefabricados de piedra atravesados por barras de acero inoxidable pretensado: comprimir la piedra mantiene cerradas las juntas bajo el viento con la mitad de peso, completando María (138 m), los cuatro Evangelistas (135 m) y la torre de Jesucristo (172.5 m), coronada en febrero de 2026 e inaugurada el 10 de junio de 2026.",
        "plate": [
            ("Virgin Mary · Evangelists", "Virgen María · Evangelistas", "138 m · 135 m", "sf-towers"),
            ("Tower of Jesus Christ", "Torre de Jesucristo", "172.5 m (5.2 m below Montjuïc)", "sf-centenary"),
            ("Structural system", "Sistema estructural", "Prefabricated post-tensioned stone", "ingenia-arup"),
            ("Cross dimensions", "Dimensiones de la cruz", "17 m tall · 13.5 m wide", "sf-centenary"),
        ],
        "egg": False,
    },
    {
        "id": "m8",
        "era": "2026+",
        "move_en": "2026+ · The Glory Facade Horizon",
        "move_es": "2026+ · El horizonte de la Fachada de la Gloria",
        "years": "2026+",
        "title_en": "The unfinished south elevation and urban bridge",
        "title_es": "El alzado sur pendiente y el puente urbano",
        "body_en": "Even with the central cross glowing 172.5 m above Barcelona, the temple is not finished. On the south side along Carrer de Mallorca stands the Glory facade: planned as the monumental main entrance with four final apostle towers, dramatic lantern arches, and a contested grand staircase that awaits municipal resolution.",
        "body_es": "Incluso con la cruz central brillando a 172.5 m sobre Barcelona, el templo no ha concluido. Al sur, frente a la calle de Mallorca, aguarda la fachada de la Gloria: proyectada como entrada principal monumental con cuatro últimas torres de los apóstoles, arcos en celosía y una escalinata cuya solución urbanística municipal sigue abierta.",
        "plate": [
            ("Total tower ensemble", "Conjunto de torres", "18 towers planned", "sf-towers"),
            ("Primary open phase", "Fase principal abierta", "Glory facade (Carrer de Mallorca)", "sf-history"),
            ("Polyhedral statics bridge", "Puente de estática 3D", "Akbarzadeh et al. 2015 model theory", "akbarzadeh2015"),
            ("Hypar geometry link", "Vínculo geométrico paraboloides", "Colònia Güell benchmark", "cortes2019"),
        ],
        "egg": False,
    },
]

VALUE_ES = {
    "Fixed 19th-century crypt plan": "Planta fija de cripta del siglo XIX",
    "Omitted via inclined columns": "Omitidos mediante columnas inclinadas",
    "Non-structural pinnacles & cores": "Pináculos y núcleos no portantes",
    "Hyperboloid, paraboloid, helicoid, conoid": "Hiperboloide, paraboloide, helicoide, conoide",
    "12-pt red porphyry · 24 m total": "Pórfido rojo 12 puntas · 24 m totales",
    "Naturalistic 2025 image study": "Estudio estadístico naturalista 2025",
    "July 1936": "Julio de 1936",
    "1:10 and 1:25 plaster casts": "Maquetas de yeso 1:10 y 1:25",
    "Timber strings to precast": "De cuerdas en madera a prefabricados",
    "Structural formwork shells": "Cáscaras de encofrado resistente",
    "Glazed ceramic weather shell": "Piel cerámica vidriada protectora",
    "Tight hyperboloid rebar pours": "Vaciado en armado denso hiperboloide",
    "From 1979 onward": "Desde 1979 en adelante",
    "Straight wire-cut rules on stone": "Corte recto con hilo sobre piedra",
    "Eyring 1930 absorption model": "Modelo de absorción de Eyring 1930",
    "Prefabricated post-tensioned stone": "Piedra prefabricada pretensada",
    "17 m tall · 13.5 m wide": "17 m de alto · 13.5 m de ancho",
    "18 towers planned": "18 torres proyectadas",
    "Glory facade (Carrer de Mallorca)": "Fachada de la Gloria (C/ Mallorca)",
    "Akbarzadeh et al. 2015 model theory": "Teoría de modelo Akbarzadeh et al. 2015",
    "Colònia Güell benchmark": "Referencia Colònia Güell",
}

PARTS = [
    {
        "id": "part-1",
        "numeral": "I",
        "title_en": "Stone and Inverted Gravity",
        "title_es": "Piedra y gravedad invertida",
        "years": "1882–1914",
        "pull_en": "What hangs in pure tension can stand in pure compression, if the masonry follows the chain upside down.",
        "pull_es": "Lo que cuelga en tensión pura puede sostenerse en compresión pura si la piedra sigue la cadena invertida.",
        "opener": [
            {
                "en": "Every medieval cathedral fights a horizontal push. Round arches and pointed ribs press outward at the tops of high nave walls; without stone flying buttresses bracing the masonry from outside, those walls would bow and crack open.",
                "es": "Toda catedral medieval libra una batalla contra el empuje horizontal. Los arcos de medio punto y los arcos ojivales empujan hacia afuera en lo alto de los muros; sin arbotantes exteriores de piedra que apunten el muro desde afuera, las paredes se abrirían.",
                "src": ["heyman1966"],
            },
            {
                "en": "Gaudí called flying buttresses architectural crutches. Inheriting Villar’s 1882 crypt footprint, he used hanging weighted-cord models to locate the three-dimensional line of thrust, inclining columns so the vertical gravity reaction V and horizontal vault push H combine straight down the stone axis.",
                "es": "Gaudí llamaba muletas arquitectónicas a los arbotantes. Al heredar la planta de la cripta de Villar de 1882, usó maquetas funiculares de cordeles cargados para hallar la línea tridimensional de empuje, inclinando las columnas de modo que la reacción vertical V y el empuje horizontal H se unan justo a lo largo del eje pétreo.",
                "src": ["sf-history", "sf-architecture"],
            },
        ],
        "cards": ["m1", "m2"],
        "interlude": "ruled-comparison",
    },
    {
        "id": "part-2",
        "numeral": "II",
        "title_en": "Ruled Geometry & The Stone Forest",
        "title_es": "Geometría reglada y el bosque de piedra",
        "years": "1914–1926",
        "pull_en": "A surface curved in space can still be ruled entirely by straight lines—so a mason’s taut string builds the vault.",
        "pull_es": "Una superficie curva en el espacio puede estar tejida enteramente por líneas rectas: una cuerda tensa basta para trazar la bóveda.",
        "opener": [
            {
                "en": "A dome built from general double-curved blocks requires unique custom carving at every joint. After 1914, Gaudí anchored the nave in ruled quadrics: surfaces swept out by a moving straight line.",
                "es": "Una cúpula tallada con dobles curvaturas arbitrarias exige plantillas únicas para cada sillar. Después de 1914, Gaudí basó la nave en cuádricas regladas: superficies barridas por una recta en movimiento.",
                "src": ["sf-architecture"],
            },
            {
                "en": "The nave columns rise as double-twisted intersections of two star prisms turning in opposite directions—passing smoothly from 6, 8, 10, or 12 points up to twice as many flutes before branching like eucalyptus boughs. A 2025 statistical study of nave photographs found scale-invariant visual spectra resembling forest canopies.",
                "es": "Las columnas nacen de la intersección de dos prismas estrellados que giran en sentidos opuestos, pasando de 6, 8, 10 o 12 puntas al doble de estrías antes de ramificarse como ramas de eucalipto. Un estudio estadístico de imágenes de 2025 observó espectros espaciales invariantes de escala semejantes a copas de bosque.",
                "src": ["sf-columns", "dyakova2025"],
            },
        ],
        "cards": ["m3"],
        "interlude": "quadrics",
    },
    {
        "id": "part-3",
        "numeral": "III",
        "title_en": "Fire, Shards & Taut Ribs",
        "title_es": "Fuego, yesos y costillas tensas",
        "years": "1936–1986",
        "pull_en": "Because each surface followed a geometric rule, broken pieces of plaster still carried the whole temple inside their angles.",
        "pull_es": "Como cada superficie seguía una regla geométrica, los fragmentos rotos de yeso aún guardaban en sus ángulos la ley completa del templo.",
        "opener": [
            {
                "en": "In 1936, fire in Gaudí’s workshop destroyed drawings and shattered the fragile plaster casts. Had the nave been a freehand sculpture, continuity would have vanished with the ashes.",
                "es": "En 1936, el incendio del obrador destruyó planos y redujo a fragmentos las maquetas de yeso. Si la nave hubiera sido una escultura libre, la continuidad habría desaparecido con las cenizas.",
                "src": ["sf-history"],
            },
            {
                "en": "Instead, surviving shards preserved the ruled slope axes and throat ratios. Post-war builders rebuilt the models, exposed the compression diagram on the Passion facade, and gradually replaced traditional timber ribs with high-precision precast and self-compacting concrete vault elements.",
                "es": "En cambio, los fragmentos rescatados conservaron los ejes de recta reglada y las gargantas hiperbólicas. Tras la guerra se recompusieron las maquetas, se desnudó el diagrama de compresión en la Pasión y el encofrado artesanal cedió paso a prefabricados y hormigón autocompactante.",
                "src": ["gomez2009", "rodriguez2017"],
            },
        ],
        "cards": ["m4", "m5"],
        "interlude": "stone-hierarchy",
    },
    {
        "id": "part-4",
        "numeral": "IV",
        "title_en": "CAD, Wire Saws & Tensioned Stone",
        "title_es": "CAD, hilo de diamante y piedra pretensada",
        "years": "1979–2026+",
        "pull_en": "Putting stone in pre-compression lets a 172.5 m tower halve its weight above 1882 foundations.",
        "pull_es": "Precomprimir la piedra permite que una torre de 172.5 m reduzca su peso a la mitad sobre cimientos de 1882.",
        "opener": [
            {
                "en": "By the late twentieth century, three-dimensional parametric modeling unlocked Gaudí’s second-order equations at industrial speed: five-axis diamond wire saws followed the mathematical rulings directly through stone blocks to close the 45 m nave vaults by 2010.",
                "es": "Hacia finales del siglo XX, el modelado paramétrico tridimensional tradujo las ecuaciones de segundo orden de Gaudí a velocidad industrial: sierras de hilo diamantado de cinco ejes siguieron las rectas matemáticas sobre la piedra para cerrar las bóvedas de 45 m en 2010.",
                "src": ["gomez2009", "sf-history"],
            },
            {
                "en": "When work shifted to the six monumental crossing towers, solid masonry would have overstressed the 19th-century crypt footings. Prefabricated stone panels tensioned internally with stainless steel tendons closed the joints against Barcelona gusts—culminating in February 2026 with the 172.5 m cross and the June 10 centenary.",
                "es": "Al iniciar los seis cimborrios centrales, la mampostería maciza habría sobrecargado la cimentación decimonónica. Paneles prefabricados de piedra pretensados internamente con barras de acero inoxidable mantuvieron cerradas las juntas ante el viento, culminando en febrero de 2026 con la cruz de 172.5 m y el centenario del 10 de junio.",
                "src": ["ingenia-arup", "sf-centenary"],
            },
        ],
        "cards": ["m6", "m7", "m8"],
        "interlude": "towers-ledger",
    },
]

# ---------------------------------------------------------------------------------------------------------------
# Conceptual plate drawer (Law 8: explicit conceptual disclosure in both alt and visible caption; zero metadata)
# ---------------------------------------------------------------------------------------------------------------
EGG_BUTTON = {
    "hint_en": "Open the plaster-shard workshop drawer.",
    "hint_es": "Abrir el cajón de fragmentos de yeso.",
    "button_en": "Inspect the architectural workshop plates (2 views)",
    "button_es": "Ver las láminas del obrador arquitectónico (2 vistas)",
    "close_en": "Fold the workshop drawer shut",
    "close_es": "Cerrar el cajón del obrador",
}

PLATES = [
    {
        "image": "images/sagrada-familia/sagrada-nave-forest.jpg",
        "width": 1280,
        "height": 720,
        "alt_en": "Conceptual visualization imagining looking upward inside a Sagrada Família-inspired stone nave: fluted branching columns, star hyperboloid oculi, and emerald-to-amber stained-glass light (artistic impression, not a measured drawing or blueprint).",
        "alt_es": "Visualización conceptual que imagina la vista ascendente dentro de una nave pétrea inspirada en la Sagrada Família: columnas estriadas ramificadas, óculos en estrella hiperboloide y luz de vitrales esmeralda a ámbar (impresión artística, no es un plano medido).",
        "caption_en": "Conceptual visualization imagining what the sunlit branching porphyry and granite stone forest beneath star hyperboloid vaults looks like (artistic impression, not a measured structure; stated geometric equations and dimensions remain intact in the interactive benches below).",
        "caption_es": "Visualización conceptual que imagina cómo se percibe el bosque de columnas de pórfido y granito bajo bóvedas hiperboloides iluminadas (impresión artística, no es un plano medido; las ecuaciones y proporciones planteadas permanecen intactas en los bancos interactivos de abajo).",
        "src": ["sf-columns", "sf-architecture"],
    },
    {
        "image": "images/sagrada-familia/sagrada-stereotomy-atelier.jpg",
        "width": 1280,
        "height": 720,
        "alt_en": "Conceptual visualization imagining Gaudí’s stonecutting and plaster-model workbench: brass-strung plaster hyperboloid and saddle paraboloid beside hanging chains and a star-cut granite block (artistic impression, not an archival photograph).",
        "alt_es": "Visualización conceptual que imagina la mesa del obrador de estereotomía: hiperboloide y paraboloide de yeso tensados con hilos de latón junto a cadenas colgantes y un bloque de granito estrellado (impresión artística, no es fotografía de archivo).",
        "caption_en": "Conceptual visualization imagining what the Barcelona plaster-and-chain stereotomy workbench looks like, pairing a doubly-ruled one-sheet hyperboloid, hyperbolic paraboloid saddle, hanging catenary frame, and fluted granite star section (artistic impression, not an archival photograph).",
        "caption_es": "Visualización conceptual que imagina cómo luce la mesa del obrador de yeso y cadenas en Barcelona, reuniendo un hiperboloide doblemente reglado, un paraboloide hiperbólico en silla, un marco de catenarias y una sección estrellada en granito (impresión artística, no es fotografía de archivo).",
        "src": ["sf-history", "gomez2009"],
    },
]

# ---------------------------------------------------------------------------------------------------------------
# Interactive Benches Copy (EN + ES-MX)
# ---------------------------------------------------------------------------------------------------------------
ATELIER_TEXT = {
    "kicker_en": "Coupled 2D ↔ 3D Observatory · El Croquis Stereotomy Plate",
    "kicker_es": "Observatorio Acoplado 2D ↔ 3D · Lámina de Estereotomía",
    "title_en": "From Hanging Catenary to 3D Ruled Stone (Live GLB & DXF Export)",
    "title_es": "De la cadena colgante a la piedra reglada en 3D (Exportación GLB y DXF)",
    "intro_en": "Adjust the central lantern load or vault shape on the left: the 2D funicular arch immediately recomputes horizontal thrust H, vertical reaction V, and the computed column inclination θ = arctan(H/V) measured from vertical—and steers the 3D WebGL2 column on the right in real time. Switch 3D modes to inspect straight-line wire rulings on the hyperboloid, saddle paraboloid, and conoid, then export a watertight .glb mesh or .dxf stonecutting template directly from your browser.",
    "intro_es": "Ajusta la carga concentrada del cimborrio o la altura de la bóveda a la izquierda: el arco funicular 2D recalcula al instante el empuje horizontal H, la reacción vertical V y la inclinación θ = arctan(H/V) medida desde la vertical, orientando en vivo la columna 3D en WebGL2 a la derecha. Cambia de superficie para ver las rectas regladas en el hiperboloide, paraboloide y conoide, y exporta un sólido .glb o plantilla .dxf directamente desde el navegador.",
    "science_en": "Heyman’s 1966 plastic limit framework shows in general that a compression-only masonry structure stands when a thrust line in equilibrium lies inside the masonry section; Akbarzadeh et al. (2015) extend graphic statics to 3D polyhedral cells. Neither paper tested the Sagrada Família directly; the values computed here come from the MODEL parameters stated in Part VI.",
    "science_es": "El marco plástico de Heyman (1966) muestra en general que una estructura de mampostería sin tracción se sostiene cuando existe una línea de empuje en equilibrio dentro de su espesor; Akbarzadeh et al. (2015) extienden la estática gráfica a poliedros 3D. Ninguno de estos artículos ensayó directamente la Sagrada Família; los valores calculados aquí provienen de los parámetros de MODELO indicados en la Parte VI.",
}

COL_BENCH_TEXT = {
    "kicker_en": "Boolean Stone Hierarchy · 6, 8, 10 & 12 Points",
    "kicker_es": "Jerarquía Pétrea Booleana · 6, 8, 10 y 12 Puntas",
    "title_en": "Counter-Rotating Star Columns & Material Tiers",
    "title_es": "Columnas estrelladas de doble giro y rangos de piedra",
    "intro_en": "Select a Basilica stone tier and scrub height fraction z / H_shaft from base (0.00) to capital neck (1.00): two identical star polygons twist by +θ and −θ in opposite senses. Where they overlap, n outer ridges split smoothly into 2n facets with zero pinch.",
    "intro_es": "Elige un rango de piedra de la Basílica y desliza la fracción de altura z / H_fuste desde la base (0.00) hasta el capitel (1.00): dos polígonos estrellados idénticos giran +θ y −θ en sentidos opuestos. En su intersección, n aristas iniciales se duplican suavemente en 2n facetas sin estrangulamiento.",
}

TOWER_BENCH_TEXT = {
    "kicker_en": "18 Towers & Post-Tensioned Stone Decompression",
    "kicker_es": "18 Torres y Descompresión en Piedra Pretensada",
    "title_en": "Barcelona Skyline Datum (172.5 m vs 177.7 m) & Tensioned Panel Stress",
    "title_es": "Cota urbana (172.5 m vs 177.7 m) y esfuerzo en paneles pretensados",
    "intro_en": "Compare the 18 Basilica spires against Ulm Minster (161.5 m) and Montjuïc Hill (177.7 m), then test why Arup and the Basilica engineers pre-compress prefabricated stone panels with stainless steel bars: keep the windward edge stress σ_min ≥ 0 so mortar and epoxy joints do not pull open under gust moment M_wind.",
    "intro_es": "Compara las 18 torres frente a la Catedral de Ulm (161.5 m) y Montjuïc (177.7 m), y prueba por qué Arup y los ingenieros de la Basílica precomprimen paneles prefabricados de piedra con barras de acero inoxidable: mantener σ_min ≥ 0 en el borde a barlovento evita que las juntas se abran por tracción bajo el momento de viento M_viento.",
}

LIGHT_BENCH_TEXT = {
    "kicker_en": "Solar Azimuth & Stone Vault Acoustics",
    "kicker_es": "Acimut Solar y Acústica de Bóvedas Pétreas",
    "title_en": "East-to-West Stained-Glass Chromatics & Eyring Reverberation",
    "title_es": "Cromatismo solar de oriente a poniente y reverberación de Eyring",
    "intro_en": "Scrub the solar hour from dawn to sunset across the nave section: morning sunlight enters the eastern Nativity glass in cool blues and greens, noon light drops straight down through hyperboloid ceiling oculi, and late afternoon warms the western Passion glass in amber and crimson.",
    "intro_es": "Desliza la hora solar del alba al ocaso sobre la sección de la nave: el sol de mañana entra por los vitrales del Nacimiento en tonos azules y verdes, el mediodía desciende vertical por los óculos hiperboloides y la tarde tiñe los vitrales de la Pasión en ámbar y carmesí.",
}

# ---------------------------------------------------------------------------------------------------------------
# Interlude Reference Tables
# ---------------------------------------------------------------------------------------------------------------
RULED_COMPARE = {
    "title_en": "Hanging chain (catenary) vs. parabola: why slope matters",
    "title_es": "Cadena colgante (catenaria) frente a parábola: por qué importa la pendiente",
    "head_en": ("Property", "Loaded horizontally (Parabola)", "Self-weight along arc (Catenary)"),
    "head_es": ("Propiedad", "Carga horizontal uniforme (Parábola)", "Peso propio sobre el arco (Catenaria)"),
    "rows": [
        ("Load distribution", "Distribución de carga", "Constant per horizontal meter", "Constante por metro horizontal", "Constant per meter of curved stone arc", "Constante por metro de arco pétreo"),
        ("Equation", "Ecuación", "y = f·(1 − 4x²/L²)", "y = f·(1 − 4x²/L²)", "y = a·[cosh(L/2a) − cosh(x/a)]", "y = a·[cosh(L/2a) − cosh(x/a)]"),
        ("Slope at steeper haunches", "Pendiente en riñones", "More arch weight missed", "Subestima el peso de tramos inclinados", "Carries full arc length near springing", "Integra toda la longitud de arco en arranques"),
        ("Concentrated crown load", "Carga puntual en clave", "Sharp angle change", "Cambio brusco de pendiente", "Explicit crown slope kink Δy′ = W_top / H", "Quiebre de pendiente Δy′ = W_top / H"),
    ],
    "note_en": "Equilibrium identity verified against Heyman (1966) masonry limit rules; the Colònia Güell portal hyperboloids are documented geometrically in Cortés et al. (2019). Neither source asserts a single closed-form span for the entire nave.",
    "note_es": "Identidad de equilibrio comprobada frente a las reglas de límite de mampostería de Heyman (1966); los paraboloides del pórtico de la Colònia Güell se documentan en Cortés et al. (2019). Ninguna fuente fija un solo claro cerrado para toda la nave.",
    "src": ["heyman1966", "cortes2019"],
}

QUADRICS_LEDGER = {
    "title_en": "The four ruled families of the Sagrada Família",
    "title_es": "Las cuatro familias de superficies regladas en la Sagrada Família",
    "items": [
        ("One-sheet hyperboloid", "Hiperboloide de una hoja",
         "Generated by two families of straight lines sweeping around an elliptical or circular throat; distributes daylight through vaulted oculi while remaining formable with straight slats.",
         "Generado por dos familias de rectas alrededor de una garganta elíptica o circular; difunde luz solar por óculos de bóveda y permite cimbra con listones rectos."),
        ("Hyperbolic paraboloid (Hypar)", "Paraboloide hiperbólico",
         "Doubly-ruled saddle surface forming smooth stone transitions between columns, vaults, and tower openings.",
         "Superficie en silla doblemente reglada que resuelve transiciones continuas entre columnas, bóvedas y vanos de torre."),
        ("Helicoid", "Helicoide",
         "Generated by rotating and translating a line along a central axis; shapes the double-twist arborescent shafts and spiral tower stairs.",
         "Generado al rotar y trasladar una recta a lo largo de un eje; da forma a fustes arbóreos de doble giro y escaleras helicoidales."),
        ("Conoid", "Conoide",
         "Generated by straight lines joining a horizontal apex line to a sinusoidal curve along the eaves of the Sagrada Família Schools roof.",
         "Generado por rectas que unen una cumbrera horizontal con una curva sinusoidal en los aleros de las Escuelas."),
    ],
    "src": ["sf-architecture", "gomez2009"],
}

# ---------------------------------------------------------------------------------------------------------------
# Part VI · Stereotomy & Structural Mechanics Lab (recomputed by skills/classics/cc02/verify_cc02_sagrada.py)
# ---------------------------------------------------------------------------------------------------------------
LAB = {
    "title_en": "Stereotomy & Mechanics Lab: the geometry, worked",
    "title_es": "Laboratorio de Estereotomía y Mecánica: las fórmulas, resueltas",
    "intro_en": "The eight moves above tell the architectural story. This lab puts numbers to four underlying mechanisms: doubly-ruled hyperboloid straightness, catenary vs. parabolic arch equilibrium, counter-rotating star column cross-sections, and post-tensioned stone joint decompression. Any input not taken from a primary source is marked MODEL; an independent standard-library script in the repository recomputes every cell below and fails if a defect is planted.",
    "intro_es": "Las ocho jugadas anteriores cuentan la historia arquitectónica. Este laboratorio pone números a cuatro mecanismos clave: la rectitud del hiperboloide reglado, el equilibrio catenario frente a la parábola, la sección de columnas estrelladas de doble giro y la descompresión en piedra pretensada. Toda entrada que no proviene de una fuente primaria está marcada como MODELO; un script independiente en el repositorio recalcula cada cifra y falla si se le planta un defecto.",
    "hyp_h_en": "1 · Doubly-ruled one-sheet hyperboloid without curved formwork",
    "hyp_h_es": "1 · Hiperboloide de una hoja doblemente reglado sin cimbra curva",
    "hyp_en": "For fixed parameter u and family sign s in {+1, −1}, the point r(u, v) = (a(cos u − s·v·sin u), b(sin u + s·v·cos u), v·c) traces a straight line as v varies—yet satisfies (x/a)² + (y/b)² − (z/c)² = 1 everywhere on the surface. Straight saw cuts or taut strings therefore sweep out a doubly curved stone funnel. Dimensions below are MODEL throat parameters.",
    "hyp_es": "Para u fijo y signo de familia s en {+1, −1}, el punto r(u, v) = (a(cos u − s·v·sen u), b(sen u + s·v·cos u), v·c) traza una línea recta al variar v y satisface (x/a)² + (y/b)² − (z/c)² = 1 en toda la superficie. Así, cortes rectos de sierra o cuerdas tensas engendran un embudo pétreo de doble curvatura. Las dimensiones de abajo son parámetros de garganta MODELO.",
    "fun_h_en": "2 · Hanging catenary vs. parabola & column thrust angle",
    "fun_h_es": "2 · Catenaria colgante vs. parábola e inclinación de columna",
    "fun_en": "A cord carrying uniform weight per horizontal meter forms a parabola; a masonry vault carrying uniform self-weight per meter of arc forms a catenary. Adding a concentrated crown lantern load W_top introduces slope offset alpha_0 = arcsinh(W_top / (2H)), tilting the resultant support angle from vertical by θ = arctan(H / V). Setting W_top to zero shows how much an unloaded catenary rises above an equal-span, equal-rise parabola on the haunches.",
    "fun_es": "Un cable con peso uniforme por metro horizontal forma una parábola; una bóveda de piedra con peso propio por metro de arco forma una catenaria. Añadir una carga puntual de linterna W_top en la clave introduce el parámetro alpha_0 = arcsenh(W_top / (2H)) e inclina la resultante respecto a la vertical en θ = arctan(H / V). Al fijar W_top en cero se mide cuánto se eleva la catenaria sobre la parábola equivalente en los riñones.",
    "col_h_en": "3 · Double-twisted star columns: height rule, Boolean area & net stress",
    "col_h_es": "3 · Columnas estrelladas de doble giro: altura, área booleana y esfuerzo neto",
    "col_en": "Gaudí’s Basílica columns obey two documented ratios: total height equals double the star-point count in meters (H_total = 2n m), and shaft height equals ten times inner diameter (H_shaft = 10·D_in). Intersecting two counter-rotating n-star prisms over twist ±π/(2n) splits n points cleanly into 2n facets with positive net area A_net (after subtracting a MODEL central conduit void). Axial loads N below are MODEL illustrations matching the stone tier order.",
    "col_es": "Las columnas de la Basílica siguen dos razones documentadas: la altura total en metros duplica el número de puntas de la estrella (H_total = 2n m), y el fuste mide diez veces el diámetro interior (H_fuste = 10·D_int). Intersectar dos prismas estrellados que giran ±π/(2n) transforma n aristas en 2n facetas con área neta positiva A_net (descontando un ducto central MODELO). Las cargas axiales N de abajo son valores MODELO acordes con la jerarquía pétrea.",
    "pt_h_en": "4 · Post-tensioned stone tower panels under Barcelona wind",
    "pt_h_es": "4 · Paneles de piedra pretensada bajo viento en las torres",
    "pt_en": "Masonry joints carry compression well and resist minimal tension. Threading unbonded stainless steel bars down prefabricated hollow stone panels adds concentric pre-compression F_pt so that minimum windward edge stress σ_min = (F_pt + N_dead)/A_net − M_wind/Z_net stays non-negative under characteristic wind overturning moment M_wind. All panel dimensions and wind loads below are MODEL parameters illustrating the Arup/Basílica mechanism.",
    "pt_es": "Las juntas de mampostería trabajan bien a compresión y resisten tracción mínima. Pasar barras de acero inoxidable por paneles huecos de piedra añade precompresión F_pt para que el esfuerzo mínimo de borde a barlovento σ_min = (F_pt + N_dead)/A_net − M_viento/Z_net permanezca positivo o nulo bajo el momento de volteo del viento M_viento. Todas las dimensiones y cargas de abajo son parámetros MODELO que ilustran el mecanismo.",
    "verify_h_en": "Run the independent verifier yourself",
    "verify_h_es": "Ejecuta el verificador independiente",
    "verify_en": "The repository script skills/classics/cc02/verify_cc02_sagrada.py (with SKILL.md beside it) uses only the Python standard library. It recomputes the hyperboloid quadric and straight-ruling identity, integrates catenary arc length via Simpson quadrature, evaluates counter-rotating Boolean column cross-sections and panel wind decompression, checks every number on both language pages, and exits non-zero under four planted defects.",
    "verify_es": "El script skills/classics/cc02/verify_cc02_sagrada.py (junto con su SKILL.md) usa solo la biblioteca estándar de Python. Recalcula la identidad cuádrica y rectilínea del hiperboloide, integra la longitud catenaria por cuadratura de Simpson, evalúa las secciones de columna de doble giro y la descompresión bajo viento, coteja cada cifra en inglés y español y falla ante cuatro defectos plantados.",
}

SILENT = [
    {
        "q_en": "Did Antoni Gaudí leave complete signed engineering blueprints for the upper towers?",
        "q_es": "¿Dejó Antoni Gaudí planos de ingeniería completos y firmados para las torres superiores?",
        "a_en": "Not stated as complete blueprints: the 1936 fire destroyed studio drawings and shattered plaster models; later builders reconstructed the geometry from surviving 1:10 and 1:25 shards, photographs, and Gaudí’s ruled-surface proportions.",
        "a_es": "No existen planos completos: el incendio de 1936 destruyó dibujos y rompió maquetas; los constructores posteriores reconstruyeron la geometría desde fragmentos sobrevivientes a escalas 1:10 y 1:25, fotografías y las proporciones regladas de Gaudí.",
    },
    {
        "q_en": "Are the tendon prestress forces, wind pressures, and column loads in Part VI measurements from the Basílica?",
        "q_es": "¿Son mediciones reales de la Basílica las fuerzas de pretensado, presiones de viento y cargas de columna de la Parte VI?",
        "a_en": "No: detailed project calculations for the post-tensioned tower joints and specific column axial forces are not published as full raw engineering tables in our cited sources, so every non-sourced input in Part VI is labeled MODEL.",
        "a_es": "No: los cálculos detallados de pretensado de juntas ni las cargas axiales exactas por nivel se publican como tablas completas en las fuentes consultadas, por lo que toda entrada sin fuente en la Parte VI lleva la etiqueta MODELO.",
    },
    {
        "q_en": "Is every facade of the Sagrada Família finished after the June 10, 2026 centenary inauguration?",
        "q_es": "¿Quedó terminada toda la Sagrada Família tras la inauguración del centenario el 10 de junio de 2026?",
        "a_en": "No: the 2026 milestone marks the completion and inauguration of the 172.5 m Tower of Jesus Christ; work on the southern Glory facade, its four final apostle spires, and the municipal staircase across Carrer de Mallorca remains ahead.",
        "a_es": "No: el hito de 2026 marca la culminación e inauguración de la torre central de Jesucristo (172.5 m); la fachada sur de la Gloria, sus cuatro torres finales de los apóstoles y la escalinata sobre la calle de Mallorca siguen pendientes.",
    },
]

CLOSING = [
    {
        "en": "Walking under the 45 m nave vaults today, you see three centuries of structural thought compressed into one stone room: 19th-century crypt masonry, hanging catenary lines, early-20th-century ruled plasterwork, 1980s aerospace CAD scripts, and 21st-century post-tensioned stone panels standing 172.5 m above the street.",
        "es": "Caminar hoy bajo las bóvedas de 45 m de la nave reúne tres siglos de pensamiento estructural en un mismo recinto de piedra: mampostería decimonónica de cripta, curvas catenarias invertidas, yesos reglados de principios del siglo XX, guiones CAD aeroespaciales y paneles pretensados de piedra que alcanzan 172.5 m sobre la calle.",
    },
]

FOOTER_NOTE = {
    "en": "Independent educational monograph. Sourced Basilica figures are attributed to Basílica de la Sagrada Família; structural pre-tensioned panel engineering is attributed to Ingenia / Arup; peer-reviewed articles were checked in Crossref and Scite on 2026-11-15. Values labeled MODEL illustrate mechanisms only and are not structural approvals or engineering calculations for construction.",
    "es": "Monografía educativa independiente. Las cifras de la Basílica se atribuyen a Basílica de la Sagrada Família; la ingeniería de paneles pretensados a Ingenia / Arup; los artículos arbitrados se verificaron en Crossref y Scite el 2026-11-15. Los valores marcados MODELO ilustran mecanismos únicamente y no constituyen cálculo estructural ni dictamen de obra.",
}

# Forbidden hype / overclaim / leakage strings guarded by tests/test_sagrada_masterpiece.py
BANNED = [
    "ordenador", "fichero", "vosotros", "miracle", "milagro", "unbreakable", "tallest possible",
]
