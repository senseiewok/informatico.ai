"""CC.02 · One Stone Forest, Eight Moves — La Sagrada Família as an Engineering & Human Story (single source of truth).

Every factual claim on the page sits beside a primary source verified on 2026-11-15: official Basílica de la Sagrada
Família pages (live HTTP 200), Ingenia / Royal Academy of Engineering reporting, and 15 peer-reviewed articles checked in
Crossref and Scite on 2026-11-15 (zero retractions).

- Model inputs for interactive benches live in tools/folios/classics/cc02_mechanics.py and are marked MODEL.
- General mechanics and acoustics papers (Heyman 1966, Akbarzadeh et al. 2015, Eyring 1930) explain general principles
  and did not test the Sagrada Família; the page states this beside each reference.
- Anything a source does not state is labeled "not stated" and summarized in SILENT.
"""
from __future__ import annotations

SLUG = "sagrada-familia"
CODE = "CC.02"
DATE = "2026-11-15"
ACCESSED = "2026-11-15"

SEO = (
    "One Stone Forest, Eight Moves: La Sagrada Família",
    "Five generations across 144 years of the Sagrada Família: catenaries, ruled hyperboloids, 1936 plaster shards, and tensioned stone.",
    "Un bosque de piedra, ocho jugadas: Sagrada Família",
    "Cinco generaciones en 144 años de la Sagrada Família: catenarias, hiperboloides reglados, yesos de 1936 y piedra pretensada.",
)

# ---------------------------------------------------------------------------------------------------------------
# Sources (23 total). "kind": basilica (live HTTP 200 sagradafamilia.org pages), eng (Ingenia / RAE),
# paper (15 peer-reviewed DOIs checked in Crossref and Scite on 2026-11-15; zero retractions).
# ---------------------------------------------------------------------------------------------------------------
SOURCES = {
    "sf-history": {
        "short": "Basílica history",
        "short_es": "Basílica historia",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “History of the Temple” (1882 foundation, five generations, 1925 St. Barnabas, 1936 fire, 1939 Quintana, 2010 consecration, 138 m Virgin Mary tower)",
        "url": "https://sagradafamilia.org/en/history-of-the-temple",
    },
    "sf-gaudi": {
        "short": "Basílica Gaudí bio",
        "short_es": "Basílica biografía",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “Antoni Gaudí” (1852 Reus birth, coppersmith father’s workshop from 1860, artisan trades, site scale models, 1914–1926 exclusive dedication)",
        "url": "https://sagradafamilia.org/en/antoni-gaudi",
    },
    "sf-humanism": {
        "short": "Basílica humanism",
        "short_es": "Basílica humanismo",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “Antoni Gaudí: Humanism and Spirituality” (observation of nature, workshop tree, care for workers and families)",
        "url": "https://sagradafamilia.org/en/antoni-gaudi-humanism-and-spirituality",
    },
    "sf-booklets": {
        "short": "Basílica booklets",
        "short_es": "Basílica cuadernos",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “The Booklets” (9 technical and architectural booklets covering workshop followers, columns, interior, and lanterns)",
        "url": "https://sagradafamilia.org/en/the-booklets",
    },
    "sf-evangelists": {
        "short": "Basílica Evangelists",
        "short_es": "Basílica Evangelistas",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “Towers of the Evangelists” (four 135 m central towers crowned with winged tetramorph sculptures by Xavier Medina-Campeny)",
        "url": "https://sagradafamilia.org/en/-/actes-de-commemoracio-per-la-finalitzacio-del-conjunt-dels-evangelistes",
    },
    "sf-cross-2026": {
        "short": "Basílica 2026 cross",
        "short_es": "Basílica cruz 2026",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “Cross lands in sky above Barcelona” (20 Feb 2026 placement of 17 m × 13.5 m cross completing 172.5 m 12-faced Tower of Jesus Christ, 12 tensioned-stone panel levels from 85 m to 142.5 m)",
        "url": "https://sagradafamilia.org/en/-/una-creu-que-arriba-al-cel-de-barcelona",
    },
    "sf-inauguration-2026": {
        "short": "Basílica 2026 inauguration",
        "short_es": "Basílica centenario 2026",
        "kind": "basilica",
        "label": "Basílica de la Sagrada Família, “Blessing and Inauguration of the Tower of Jesus Christ” (10 June 2026 centenary milestone honoring five generations)",
        "url": "https://sagradafamilia.org/en/-/benediccio-i-inauguracio-de-la-torre-de-jesucrist",
    },
    "ingenia-arup": {
        "short": "Ingenia / Arup",
        "short_es": "Ingenia / Arup",
        "kind": "eng",
        "label": "Tristram Carfrae & Hugh Ferguson, “Completing the Sagrada Família”, Ingenia (Royal Academy of Engineering): post-tensioned stone panels and global stone quarries",
        "url": "https://www.ingenia.org.uk/articles/completing-the-sagrada-familia/",
    },
    "huerta2006": {
        "short": "Huerta 2006",
        "kind": "paper",
        "label": "Huerta, S. (2006). Structural Design in the Work of Gaudí. Architectural Science Review 49(4), 324–339",
        "url": "https://doi.org/10.3763/asre.2006.4943",
    },
    "burry1996": {
        "short": "Burry 1996",
        "kind": "paper",
        "label": "Burry, M. (1996). Parametric design and the Sagrada Familia. Architectural Research Quarterly 1(4), 70–81",
        "url": "https://doi.org/10.1017/s1359135500003092",
    },
    "barrios2006": {
        "short": "Barrios Hernandez 2006",
        "kind": "paper",
        "label": "Barrios Hernandez, C. R. (2006). Thinking parametric design: introducing parametric Gaudi. Design Studies 27(3), 309–324",
        "url": "https://doi.org/10.1016/j.destud.2005.11.006",
    },
    "adell2005": {
        "short": "Adell & García Santos 2005",
        "kind": "paper",
        "label": "Adell, J. M. & García Santos, A. (2005). Gaudí y las bóvedas de las escuelas de la Sagrada Familia. Informes de la Construcción 56(496), 31–45",
        "url": "https://doi.org/10.3989/ic.2005.v57.i496.461",
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
        "label": "Grima, Gómez Serrano & Aguado (2007). The Use of Concrete in Gaudí’s Sagrada Familia. International Journal of Architectural Heritage 1(4), 366–379",
        "url": "https://doi.org/10.1080/15583050701476630",
    },
    "gomezramio2014": {
        "short": "Gómez-Ramió 2014",
        "kind": "paper",
        "label": "Gómez-Ramió, Cavalaro & Aguado (2014). The Trencadís Mosaic on the Pinnacles of the Sagrada Familia Cathedral. International Journal of Architectural Heritage 8(5), 760–782",
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
    "zhaoburry2024": {
        "short": "Zhao & Burry 2024",
        "kind": "paper",
        "label": "Zhao, S. & Burry, M. (2024). Architectural acoustics of the Sagrada Família Basílica. The Routledge Companion to the Sound of Space, 68–86",
        "url": "https://doi.org/10.4324/9781003347149-7",
    },
    "yoshikawa2004": {
        "short": "Yoshikawa & Narita 2004",
        "kind": "paper",
        "label": "Yoshikawa, S. & Narita, T. (2004). The Sagrada Familia Cathedral where Gaudí envisaged his bell music. Journal of the Acoustical Society of America 115(5), 2529",
        "url": "https://doi.org/10.1121/1.4783380",
    },
    "eyring1930": {
        "short": "Eyring 1930",
        "kind": "paper",
        "label": "Eyring, C. F. (1930). Reverberation Time in “Dead” Rooms. Journal of the Acoustical Society of America 1(2A), 217–241",
        "url": "https://doi.org/10.1121/1.1901884",
    },
    "commons-escoles-1909": {
        "short": "1909 Schools photo",
        "short_es": "Foto Escuelas 1909",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Escuelas Sagrada Familia.jpg” (1909 photograph via Maria Antonietta Crippa 2007; Public Domain Mark 1.0)",
        "url": "https://commons.wikimedia.org/wiki/File:Escuelas_Sagrada_Familia.jpg",
    },
    "commons-catenary-model": {
        "short": "Chain model photo",
        "short_es": "Foto maqueta funicular",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:GaudiCatenaryModel.jpg” (Etan J. Tal, 14 Dec 2009; Creative Commons CC BY 3.0)",
        "url": "https://commons.wikimedia.org/wiki/File:GaudiCatenaryModel.jpg",
    },
    "commons-nativity": {
        "short": "Nativity photo",
        "short_es": "Foto Nacimiento",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Sagrada Familia, Nativity facade (26) (30489118703).jpg” (Richard Mortel, 12 Nov 2016; Creative Commons CC BY 2.0)",
        "url": "https://commons.wikimedia.org/wiki/File:Sagrada_Familia,_Nativity_facade_(26)_(30489118703).jpg",
    },
    "commons-1988": {
        "short": "1988 site photo",
        "short_es": "Foto obra 1988",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Sagrada Familia Construction 1988.jpg” (J Dykstra, Spring 1988; Public Domain)",
        "url": "https://commons.wikimedia.org/wiki/File:Sagrada_Familia_Construction_1988.jpg",
    },
    "commons-nave-interior": {
        "short": "Nave columns photo",
        "short_es": "Foto columnas nave",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Sagrada Familia Multiple Columns (5839245513).jpg” (Tony Hisgett; Creative Commons CC BY 2.0)",
        "url": "https://commons.wikimedia.org/wiki/File:Sagrada_Familia_Multiple_Columns_(5839245513).jpg",
    },
    "commons-2026-cross": {
        "short": "2026 cross photo",
        "short_es": "Foto cruz 2026",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:View of Sagrada Familia 2026 corrected.jpg” (Hokky / ほっきー, 9 Aug 2026; Creative Commons CC0 1.0)",
        "url": "https://commons.wikimedia.org/wiki/File:View_of_Sagrada_Familia_2026_corrected.jpg",
    },
}

KIND_LABEL = {
    "basilica": ("Basílica", "Basílica"),
    "eng": ("Engineering", "Ingeniería"),
    "paper": ("Paper", "Artículo"),
    "photo": ("Photo Archive", "Archivo Fotográfico"),
}

HERO = {
    "kicker_en": "Cult Classics · CC.02 · Architecture, Craft & Stereotomy",
    "kicker_es": "Clásicos de Culto · CC.02 · Arquitectura, Oficio y Estereotomía",
    "title_en": "One Stone Forest, Eight Moves",
    "title_es": "Un bosque de piedra, ocho jugadas",
    "dek_en": "Five generations across 144 years of the Sagrada Família (1882–2026), told one structural and human move at a time.",
    "dek_es": "Cinco generaciones en 144 años de la Sagrada Família (1882–2026), contadas jugada estructural y humana por jugada.",
    "reading_en": "22 min read",
    "reading_es": "24 min de lectura",
}

BRIEF_NOTE = {
    "en": "How does one human workshop carry an unfinished vision across 144 years of war, fire, lost drawings, depleted quarries, and changing materials? By replacing private whim with open geometric law—so builders separated by a century can still pick up each other’s straight lines.",
    "es": "¿Cómo logra un taller humano sostener una obra inconclusa durante 144 años de guerras, incendios, planos perdidos y canteras agotadas? Sustituyendo el capricho privado por una ley geométrica compartida, para que constructores separados por un siglo retomen las mismas líneas rectas.",
}

OPENING = [
    {
        "en": "On February 20, 2026, cranes high above Barcelona’s Eixample set the final 4.5 m × 4.5 m × 4.9 m upper arm onto a 17 m ceramic-and-glass cross atop the Tower of Jesus Christ, completing its exterior silhouette at 172.5 m ahead of the June 10, 2026 centenary inauguration—one hundred years to the day after Antoni Gaudí died, roughly 5.2 m below Montjuïc hill (177.7 m).",
        "es": "El 20 de febrero de 2026, las grúas sobre el Eixample de Barcelona colocaron el brazo superior de 4.5 m × 4.5 m × 4.9 m en una cruz de cerámica y vidrio de 17 m sobre la torre de Jesucristo, cerrando su perfil exterior a 172.5 m rumbo a la inauguración centenaria del 10 de junio de 2026: a cien años de la muerte de Antoni Gaudí, unos 5.2 m por debajo de Montjuïc (177.7 m).",
        "src": ["sf-history", "sf-cross-2026", "sf-inauguration-2026"],
    },
    {
        "en": "The real wonder of those 144 years is human continuity. Gaudí grew up learning sheet-metal geometry at eight years old in his coppersmith father’s workshop in Reus, studied the tree outside his Barcelona studio window, and left behind a grammar of hanging chains and straight-line quadrics. Five generations of disciples, plasterers, stonecutters, stained-glass masters, acousticians, and structural engineers kept reading that shared grammar across century-wide gaps—turning math into a bridge between people who missed each other in time.",
        "es": "La verdadera maravilla de esos 144 años es la continuidad humana. Gaudí aprendió geometría del volumen a los ocho años en el taller de calderero de su padre en Reus, estudió el árbol junto a su estudio en Barcelona y legó una gramática de cadenas colgantes y cuádricas regladas. Cinco generaciones de discípulos, yeseros, canteros, vitralistas, acústicos e ingenieros estructurales leyeron esa gramática a través de brechas de un siglo, convirtiendo las matemáticas en un puente entre personas que no llegaron a conocerse.",
        "src": ["sf-gaudi", "sf-booklets", "ingenia-arup"],
    },
]

# ---------------------------------------------------------------------------------------------------------------
# Interactive Five-Generation Relay Data
# ---------------------------------------------------------------------------------------------------------------
GENERATIONS_RELAY = [
    {
        "id": "g1",
        "years": "1882–1926",
        "span_label": "Gen 1 · 1882–1926",
        "span_label_es": "Gen 1 · 1882–1926",
        "title_en": "First Generation · Antoni Gaudí & Craft Foundations",
        "title_es": "Primera Generación · Antoni Gaudí y los oficios",
        "hands_en": "Antoni Gaudí (taking over from Francisco de Paula del Villar in 1883), site blacksmiths, plasterers, carvers, and Domènec Sugrañes.",
        "hands_es": "Antoni Gaudí (relevando a Francisco de Paula del Villar en 1883), herreros, yeseros, escultores y Domènec Sugrañes.",
        "challenge_en": "Working within an already rising 1882 Neo-Gothic crypt plan while suffering childhood rheumatism and inventing an architecture free of external flying buttresses.",
        "challenge_es": "Trabajar sobre la cripta neogótica iniciada en 1882 mientras creaba una arquitectura sin arbotantes exteriores tras haber observado la naturaleza desde su niñez con reumatismo.",
        "gift_en": "Replaced private sketches with 3D polyfunicular string models, ruled surfaces, the 1909 workers’ Schools, and the completed Saint Barnabas tower (1925) as a built physical key for successors.",
        "gift_es": "Sustituyó los croquis privados por maquetas funiculares de cordeles, superficies regladas, las Escuelas de 1909 para los hijos de los obreros y la torre de San Bernabé (1925) como clave física para sus sucesores.",
        "elevation": "Crypt 0 m → St. Barnabas ~100 m",
        "src": ["sf-history", "sf-gaudi", "sf-humanism", "adell2005"],
    },
    {
        "id": "g2",
        "years": "1926–1952",
        "span_label": "Gen 2 · 1926–1952",
        "span_label_es": "Gen 2 · 1926–1952",
        "title_en": "Second Generation · Guardians of the 1936 Shards",
        "title_es": "Segunda Generación · Guardianes de los fragmentos de 1936",
        "hands_en": "Domènec Sugrañes (head 1926–1936) and Francesc de Paula Quintana (site director from 1939), alongside surviving disciples and workshop plasterers.",
        "hands_es": "Domènec Sugrañes (director 1926–1936) y Francesc de Paula Quintana (director de obra desde 1939), junto a discípulos y modelistas.",
        "challenge_en": "When the July 1936 Civil War fire destroyed drawings and photographs and smashed the 1:10 and 1:25 plaster models, public debate questioned whether the temple could continue.",
        "challenge_es": "Cuando el incendio de julio de 1936 destruyó planos y fotografías y rompió las maquetas de yeso 1:10 y 1:25, se dudó si la obra podría seguir.",
        "gift_en": "Rescued the broken gypsum pieces from the ashes and painstakingly matched straight-line rulings and photos—showing how ruled geometry preserved the whole temple inside palm-sized fragments.",
        "gift_es": "Rescataron los fragmentos de yeso entre las cenizas y recompusieron sus ejes reglados y fotografías, mostrando que la geometría reglada conservaba el templo entero en piezas pequeñas.",
        "elevation": "Workshop reconstruction → Passion foundations",
        "src": ["sf-history", "gomez2009", "burry1996"],
    },
    {
        "id": "g3",
        "years": "1954–1985",
        "span_label": "Gen 3 · 1954–1985",
        "span_label_es": "Gen 3 · 1954–1985",
        "title_en": "Third Generation · Passion Ribs & Ceramic Pinnacles",
        "title_es": "Tercera Generación · Huesos de la Pasión y trencadís",
        "hands_en": "Isidre Puig i Boada and Lluís Bonet i Garí (joint leaders from 1966), Francesc Cardoner (1983), and Catalan mosaic and stone artisans.",
        "hands_es": "Isidre Puig i Boada y Lluís Bonet i Garí (codirectores desde 1966), Francesc Cardoner (1983) y maestros canteros y ceramistas.",
        "challenge_en": "Erecting the Passion facade towers (completed 1976) and museum documentation where traditional timber formwork struggled against double-curved junctions.",
        "challenge_es": "Levantar las torres de la Pasión (culminadas en 1976) y documentar las soluciones constructivas cuando el encofrado artesanal de madera no bastaba en encuentros complejos.",
        "gift_en": "Built the taut bone-like Passion compression colonnade, founded the site museum in 1961 so visitors could study the engineering openly, and launched the nave foundations.",
        "gift_es": "Alzaron los pilares tensos de la Pasión, abrieron el museo en 1961 para enseñar al público la ingeniería de la obra y prepararon la cimentación de la nave.",
        "elevation": "Passion towers 107.4–112.2 m · Vault prep",
        "src": ["sf-history", "gomezramio2014", "rodriguez2017"],
    },
    {
        "id": "g4",
        "years": "1979–2012",
        "span_label": "Gen 4 · 1979–2012",
        "span_label_es": "Gen 4 · 1979–2012",
        "title_en": "Fourth Generation · Aerospace CAD, Light & Sound",
        "title_es": "Cuarta Generación · CAD aeroespacial, luz y acústica",
        "hands_en": "Head architect Jordi Bonet i Armengol (from 1985), parametric pioneer Mark Burry (from 1979), sculptors Josep Maria Subirachs & Etsuro Sotoo, stained-glass master Joan Vila-Grau, and Blancafort organ builders.",
        "hands_es": "Director Jordi Bonet i Armengol (desde 1985), pionero paramétrico Mark Burry (desde 1979), escultores Subirachs y Etsuro Sotoo, vitralista Joan Vila-Grau y organeros Blancafort.",
        "challenge_en": "Translating Gaudí’s second-order intersecting hyperboloids and double-twisted star columns cleanly enough to close the 45 m nave vaults for consecration in 2010.",
        "challenge_es": "Traducir intersecciones de hiperboloides y columnas de doble giro con precisión industrial para cerrar las bóvedas de 45 m rumbo a la consagración de 2010.",
        "gift_en": "Paired 5-axis diamond-wire stone cutting with Vila-Grau’s seasonal solar stained glass and the 1,492-pipe Blancafort organ—turning stone mathematics into light and music.",
        "gift_es": "Combinaron corte de piedra con hilo diamantado de 5 ejes, los vitrales solares de Vila-Grau y el órgano Blancafort de 1,492 tubos, transformando la geometría en luz y música.",
        "elevation": "Nave vaults 45 m (Consecrated 2010)",
        "src": ["sf-history", "burry1996", "gomez2009", "zhaoburry2024", "yoshikawa2004"],
    },
    {
        "id": "g5",
        "years": "2012–2026+",
        "span_label": "Gen 5 · 2012–2026+",
        "span_label_es": "Gen 5 · 2012–2026+",
        "title_en": "Fifth Generation · Tensioned Stone & Centenary Cross",
        "title_es": "Quinta Generación · Piedra pretensada y cruz del centenario",
        "hands_en": "Head architect Jordi Faulí (from 2012), Arup engineer Tristram Carfrae, sculptor Xavier Medina-Campeny, European glass/ceramic workshops, and global stone quarries including Brinscall (UK).",
        "hands_es": "Director Jordi Faulí (desde 2012), ingeniero Tristram Carfrae (Arup), escultor Xavier Medina-Campeny, talleres cerámicos europeos y canteras internacionales como Brinscall.",
        "challenge_en": "Raising six central lanterns up to 172.5 m above delicate 19th-century crypt foundations in a living city with high crane wind exposure.",
        "challenge_es": "Elevar seis cimborrios centrales hasta 172.5 m sobre cimientos decimonónicos en plena ciudad expuesta al viento.",
        "gift_en": "Pre-compressed hollow stone panels off-site to cut weight dramatically, lighting the 138 m Virgin Mary star (2021), 135 m Evangelists (2023), and crowning the 172.5 m cross in 2026.",
        "gift_es": "Precomprimieron paneles huecos de piedra para aligerar el peso, encendiendo la estrella de María (138 m, 2021), los Evangelistas (135 m, 2023) y coronando la cruz de 172.5 m en 2026.",
        "elevation": "Mary 138 m · Evangelists 135 m · Jesus Christ 172.5 m",
        "src": ["sf-cross-2026", "sf-inauguration-2026", "sf-evangelists", "ingenia-arup"],
    },
]

# ---------------------------------------------------------------------------------------------------------------
# Eight tectonic moves across four chronological Parts
# ---------------------------------------------------------------------------------------------------------------
CARDS = [
    {
        "id": "m1",
        "era": "1882",
        "move_en": "1882 · The Neo-Gothic Crypt & The Coppersmith’s Eye",
        "move_es": "1882 · La cripta neogótica y la mirada del calderero",
        "years": "1882–1883",
        "title_en": "Inheriting a stone footprint with spatial eyes trained in metal",
        "title_es": "Heredar una huella de piedra con ojos educados en metal",
        "body_en": "Diocesan architect Francisco de Paula del Villar laid the cornerstone on March 19, 1882, in classic Neo-Gothic style before technical disagreements led to his departure. When 31-year-old Antoni Gaudí took direction in 1883, the crypt piers were already rising—fixing a footprint he could not erase. Born in Reus in 1852, Gaudí had spent his boyhood cutting copper sheet into 3D vessels beside his smith father from 1860 onward, while bouts of rheumatism kept him observing plants and light at the family farmhouse rather than running with other children.",
        "body_es": "El arquitecto diocesano Francisco de Paula del Villar colocó la primera piedra el 19 de marzo de 1882 en clave neogótica antes de dejar la obra por diferencias técnicas. Cuando Antoni Gaudí asumió el proyecto en 1883 a los 31 años, la cripta ya emergía del suelo y fijaba la huella del templo. Nacido en Reus en 1852, Gaudí aprendió desde 1860 a doblar láminas planas en volúmenes 3D en el taller de su padre calderero mientras períodos de reumatismo lo mantenían observando formas vivas y luz en el campo familiar.",
        "plate": [
            ("First cornerstone laid", "Primera piedra colocada", "1882-03-19 (Bishop Urquinaona)", "sf-history"),
            ("Gaudí takes over", "Gaudí asume la dirección", "1883 (age 31)", "sf-gaudi"),
            ("Early spatial craft", "Oficio espacial temprano", "Coppersmithing from 1860", "sf-gaudi"),
            ("Guiding nature rule", "Principio de naturaleza", "Workshop tree as teacher", "sf-humanism"),
        ],
        "egg": False,
    },
    {
        "id": "m2",
        "era": "1884–1914",
        "move_en": "1884–1914 · Hanging Cords & The St. Barnabas Benchmark",
        "move_es": "1884–1914 · Catenarias y la torre de San Bernabé",
        "years": "1884–1914",
        "title_en": "Letting gravity draw the structure upside down",
        "title_es": "Dejar que la gravedad dibuje la estructura boca abajo",
        "body_en": "On the Nativity facade and in his parallel 1:10 polyfunicular model (over 4 m tall) for Colònia Güell, Gaudí suspended silk cords weighed with lead-shot bags calibrated to ~1:10,000 of full structural load. Because a loose cord carries zero bending moment, flipping its reflection upward turns pure tension into compression arches—omitting external flying buttresses. Before Gaudí’s death in 1926, only one bell tower stood complete: Saint Barnabas (1925), leaving his disciples a full-scale built key for pinnacle mosaic and structural geometry.",
        "body_es": "Mientras alzaba la fachada del Nacimiento y su maqueta polifunicular paralela a escala 1:10 (más de 4 m de altura) para la Colònia Güell, Gaudí colgó cordeles con saquitos de perdigones calibrados a ~1:10,000 de las cargas reales. Como un hilo flexible no resiste flexión, invertir su reflejo convierte la tensión pura en compresión pura y elimina arbotantes externos. Antes de morir en 1926, solo vio terminada una torre —San Bernabé (1925)—, dejando una clave construida para sus discípulos.",
        "plate": [
            ("Funicular test scale", "Escala del ensayo funicular", "1:10 chords · ~1:10,000 weights", "huerta2006"),
            ("Governing curve", "Curva rectora", "y = a·cosh(x/a) (MODEL)", "heyman1966"),
            ("First completed spire", "Primera aguja culminada", "Saint Barnabas (1925)", "sf-history"),
            ("Early concrete use", "Primeros hormigones", "Non-structural pinnacles & cores", "grima2007"),
        ],
        "egg": False,
    },
    {
        "id": "m3",
        "era": "1909–1926",
        "move_en": "1909–1926 · Workers’ Schools, Ruled Stone & Double Twists",
        "move_es": "1909–1926 · Escuelas obreras, piedra reglada y doble giro",
        "years": "1909–1926",
        "title_en": "A sinusoidal conoid schoolhouse and a canopy of twisted columns",
        "title_es": "Una escuela de conoide sinusoide y un bosque de doble giro",
        "body_en": "From 1914 Gaudí declined every external commission to give his final twelve years solely to the temple. Already in 1909 he had built the modest Parish Schools on site for the builders’ children—roofing brick classrooms with thin-brick sinusoidal conoids whose straight generating lines stiffened humble Catalan vaults. Inside the Basílica nave, he unified four ruled families (hyperboloids, hyperbolic paraboloids, helicoids, conoids) and organized double-twisted star columns in four stone tiers (6, 8, 10, and 12 points; total height 2n m; shaft height 10·D_in).",
        "body_es": "Desde 1914 Gaudí rechazó todo encargo externo para consagrar sus últimos doce años solo al templo. Ya en 1909 había levantado las Escuelas Parroquiales para los hijos de los albañiles, cubriendo el aula con conoides sinusoidales de ladrillo fino cuya regla recta rigidizaba la bóveda catalana. En la nave unificó cuatro familias regladas e ideó columnas estrelladas de doble giro en cuatro rangos pétreos (6, 8, 10 y 12 puntas; altura 2n m y fuste 10·D_int).",
        "plate": [
            ("Workers’ children school", "Escuelas para hijos de obreros", "1909 thin-brick conoid", "adell2005"),
            ("Four ruled families", "Cuatro familias regladas", "Hyperboloid, hypar, helicoid, conoid", "sf-booklets"),
            ("Column rule & tree", "Regla de columna y giro", "H_total = 2n m · 1:10 ratio", "barrios2006"),
            ("Naturalistic canopies", "Óptica de bosque", "Scale-invariant nave spectra", "dyakova2025"),
        ],
        "egg": False,
    },
    {
        "id": "m4",
        "era": "1936–1952",
        "move_en": "1936–1952 · Fire, Ashes & The Rescue of Ruled Law",
        "move_es": "1936–1952 · Fuego, cenizas y rescate de la ley reglada",
        "years": "1936–1952",
        "title_en": "Reassembling a century’s geometry from shattered gypsum",
        "title_es": "Reconstruir la geometría de un siglo desde yeso roto",
        "body_en": "During the July 1936 Civil War vandalism, workshop drawings and archival glass plates burned while the 1:10 and 1:25 plaster models were smashed across the floor. From 1939, site director Francesc de Paula Quintana and collaborators gathered every retrievable plaster shard alongside surviving published photographs. Because Gaudí had built vaults from quadrics governed by r²(z) = a² + (a²/c²)z² rather than freehand arcs, even a small broken fragment preserved the throat axis and slope ratios needed to reconstruct entire bays.",
        "body_es": "Durante el vandalismo de julio de 1936 ardieron planos y placas fotográficas mientras las maquetas de yeso 1:10 y 1:25 acababan destrozadas. Desde 1939, el director Francesc de Paula Quintana y sus colaboradores recogieron cada fragmento posible junto a fotografías publicadas. Como Gaudí trazó bóvedas con cuádricas regladas r²(z) = a² + (a²/c²)z² y no con arcos arbitrarios, hasta un fragmento roto conservaba las razones de garganta necesarias para reconstruir bóvedas completas.",
        "plate": [
            ("Workshop destruction", "Destrucción del obrador", "July 1936 fire & shattered casts", "sf-history"),
            ("Reconstruction lead", "Director de reconstrucción", "Francesc de Paula Quintana (1939)", "sf-history"),
            ("Shard parametric key", "Clave paramétrica del yeso", "Small fragments encode (a, c)", "burry1996"),
            ("Formwork evolution", "Evolución de cimbras", "Timber strings to precast", "gomez2009"),
        ],
        "egg": True,
    },
    {
        "id": "m5",
        "era": "1954–1985",
        "move_en": "1954–1985 · Passion Facade & Taut Stone Ribs",
        "move_es": "1954–1985 · Fachada de la Pasión y costillas tensas",
        "years": "1954–1985",
        "title_en": "Exposing the structural skeleton and opening the studio to all",
        "title_es": "Exponer el esqueleto estructural y abrir el taller al público",
        "body_en": "Work began on the western Passion facade foundations in 1954, exposing six bone-like slanted stone struts following the outer thrust resultant outside the stained-glass envelope—with the museum opening in 1961 to share the technical logic with visitors. Joint directors Isidre Puig i Boada and Lluís Bonet i Garí completed the Passion bell towers in 1976 while research into dense self-compacting concrete and trencadís ceramic glazing sealed the intricate ruled ribs and pinnacles.",
        "body_es": "En 1954 comenzaron los cimientos de la fachada de la Pasión, exponiendo seis contrafuertes óseos inclinados sobre la línea de empuje, mientras el museo abría en 1961 para divulgar la lógica técnica al público. Los codirectores Isidre Puig i Boada y Lluís Bonet i Garí completaron las torres de la Pasión en 1976, mientras el hormigón autocompactante y el trencadís cerámico resolvían armados densos y coronamientos impermeables.",
        "plate": [
            ("Passion foundations", "Cimientos de la Pasión", "1954 (towers finished 1976)", "sf-history"),
            ("Public learning", "Divulgación técnica", "Site Museum founded 1961", "sf-history"),
            ("Trencadís glaze", "Vidriado en pináculos", "Ceramic weather armor", "gomezramio2014"),
            ("High-flow concrete", "Hormigón autocompactante", "Tight hyperboloid rebar pours", "rodriguez2017"),
        ],
        "egg": False,
    },
    {
        "id": "m6",
        "era": "1979–2010",
        "move_en": "1979–2010 · Aerospace CAD, Stained Glass & An Organ Forest",
        "move_es": "1979–2010 · CAD aeroespacial, vitrales y bosque sonoro",
        "years": "1979–2010",
        "title_en": "Turning Boolean intersections into stone light and reverberant song",
        "title_es": "Convertir intersecciones booleanas en luz y música resonante",
        "body_en": "In 1979 Cambridge graduate Mark Burry joined Barcelona’s elderly disciples to examine the 1936 shards, later working under head architect Jordi Bonet i Armengol (named 1985) to deploy parametric aerospace surfacing software and 5-axis diamond-wire saws. Closing the 45 m nave vaults for consecration on November 7, 2010 awakened Joan Vila-Grau’s seasonal stained-glass palette—cool blue-green east toward the Nativity morning sun, glowing amber-crimson west at Passion sunset—alongside Blancafort’s 1,492-pipe presbytery organ and acoustic designs informed by Gaudí’s tubular bell studies.",
        "body_es": "En 1979 el arquitecto Mark Burry trabajó junto a los discípulos mayores examinando los yesos de 1936 y, bajo la dirección de Jordi Bonet i Armengol (1985), adaptó software paramétrico aeroespacial y sierras de hilo diamantado de 5 ejes. Cerrar las bóvedas de 45 m en la consagración del 7 de noviembre de 2010 despertó la paleta solar de vitrales de Joan Vila-Grau —verde y azul al alba en el Nacimiento, ámbar y rojo al poniente en la Pasión— junto al órgano Blancafort de 1,492 tubos y estudios acústicos.",
        "plate": [
            ("Parametric reconstruction", "Reconstrucción paramétrica", "Burry 1979 · Bonet 1985", "burry1996"),
            ("Nave vault consecration", "Consagración de la nave", "2010-11-07 (Benedict XVI)", "sf-history"),
            ("Distributed sound", "Acústica distribuida", "Vaults & Blancafort organ", "zhaoburry2024"),
            ("Bell music studies", "Campanas tubulares", "Tower acoustic propagation", "yoshikawa2004"),
        ],
        "egg": False,
    },
    {
        "id": "m7",
        "era": "2016–2026",
        "move_en": "2016–2026 · Post-Tensioned Stone & Global Quarries",
        "move_es": "2016–2026 · Piedra pretensada y canteras globales",
        "years": "2016–2026",
        "title_en": "Lightweight stone panels uniting quarries worldwide over 1882 footings",
        "title_es": "Paneles ligeros de piedra de todo el mundo sobre cimientos de 1882",
        "body_en": "Raising six central lanterns up to 172.5 m over 19th-century crypt footings precluded heavy solid masonry cores. Working under head architect Jordi Faulí (from 2012) with Arup engineer Tristram Carfrae, teams sourced color-matched stone from depleted historical beds to quarries as far afield as Brinscall (Lancashire, UK), CNC-milled hollow panels off-site, and threaded stainless post-tensioning bars through the stone joints. The 138 m Virgin Mary star shone in 2021, Xavier Medina-Campeny’s 135 m Evangelist tetramorphs completed in 2023 amidst city castellers, and 12 tensioned-stone levels topped with a German-fabricated 17 m × 13.5 m cross reached 172.5 m on February 20, 2026.",
        "body_es": "Alzar seis cimborrios hasta 172.5 m sobre cimientos del siglo XIX impedía usar núcleos macizos pesados. Bajo la dirección de Jordi Faulí (desde 2012) e ingeniería de Tristram Carfrae en Arup, se seleccionaron piedras equivalentes hasta canteras como Brinscall (Reino Unido), se fresaron paneles huecos en taller y se comprimieron sus juntas con acero inoxidable pretensado. La estrella de María (138 m) brilló en 2021, los Evangelistas (135 m) en 2023 entre castellers, y 12 niveles coronados por la cruz de 17 m × 13.5 m llegaron a 172.5 m el 20 de febrero de 2026.",
        "plate": [
            ("Virgin Mary · Evangelists", "Virgen María · Evangelistas", "138 m (2021) · 135 m (2023)", "sf-evangelists"),
            ("Tower of Jesus Christ", "Torre de Jesucristo", "172.5 m (12 stone panel levels)", "sf-cross-2026"),
            ("Structural innovation", "Innovación estructural", "Prefabricated post-tensioned stone", "ingenia-arup"),
            ("2026 cross ceremony", "Ceremonia del centenario", "2026-02-20 cross · 2026-06-10 blessing", "sf-inauguration-2026"),
        ],
        "egg": False,
    },
    {
        "id": "m8",
        "era": "2026+",
        "move_en": "2026+ · The Glory Facade & The Craft Ahead",
        "move_es": "2026+ · La Fachada de la Gloria y la obra futura",
        "years": "2026+",
        "title_en": "Leaving the last doors open to the next builders",
        "title_es": "Dejar las últimas puertas abiertas a los siguientes constructores",
        "body_en": "While February 20, 2026 closed the exterior skyline of the Tower of Jesus Christ and June 10, 2026 marks its centenary blessing, the Basílica itself notes that interior cross work continues into 2027–2028 alongside artist Andrea Mastrovito’s Agnus Dei sculpture inside the glazed upper arm, while the southern Glory facade along Carrer de Mallorca and its grand staircase still remain to be built—passing an unbroken geometric grammar onward to a sixth generation.",
        "body_es": "Aunque el 20 de febrero de 2026 cerró la silueta exterior de la torre de Jesucristo y el 10 de junio de 2026 celebra su bendición centenaria, la Basílica detalla que los trabajos interiores de la cruz continúan en 2027–2028 junto a la escultura del Agnus Dei de Andrea Mastrovito, mientras aguardan la fachada sur de la Gloria y su escalinata sobre la calle de Mallorca: pasando una gramática viva a una sexta generación.",
        "plate": [
            ("2027–2028 cross work", "Interior de la cruz", "Upper-arm interior & Agnus Dei", "sf-cross-2026"),
            ("Centenary dedication", "Homenaje centenario", "Celebrates 5 generations", "sf-inauguration-2026"),
            ("3D graphic statics link", "Estática gráfica 3D", "Akbarzadeh et al. 2015 theory", "akbarzadeh2015"),
            ("Colònia Güell benchmark", "Referencia Colònia Güell", "Cortés et al. 2019 hypar survey", "cortes2019"),
        ],
        "egg": False,
    },
]

VALUE_ES = {
    "1882-03-19 (Bishop Urquinaona)": "1882-03-19 (Obispo Urquinaona)",
    "1883 (age 31)": "1883 (31 años)",
    "Coppersmithing from 1860": "Calderería desde 1860",
    "Workshop tree as teacher": "El árbol del taller como maestro",
    "1:10 chords · ~1:10,000 weights": "Escala 1:10 · pesos ~1:10,000",
    "Saint Barnabas (1925)": "San Bernabé (1925)",
    "Non-structural pinnacles & cores": "Pináculos y núcleos no portantes",
    "1909 thin-brick conoid": "Conoide en ladrillo fino de 1909",
    "Hyperboloid, hypar, helicoid, conoid": "Hiperboloide, paraboloide, helicoide, conoide",
    "H_total = 2n m · 1:10 ratio": "H_total = 2n m · razón 1:10",
    "Scale-invariant nave spectra": "Espectros invariantes en la nave",
    "July 1936 fire & shattered casts": "Incendio de julio 1936 y yesos rotos",
    "Francesc de Paula Quintana (1939)": "Francesc de Paula Quintana (1939)",
    "Small fragments encode (a, c)": "Pequeños fragmentos codifican (a, c)",
    "Timber strings to precast": "De cuerdas en madera a prefabricados",
    "1954 (towers finished 1976)": "1954 (torres culminadas en 1976)",
    "Site Museum founded 1961": "Museo de obra fundado en 1961",
    "Ceramic weather armor": "Coraza cerámica vidriada",
    "Tight hyperboloid rebar pours": "Vaciado en armado denso hiperboloide",
    "Burry 1979 · Bonet 1985": "Burry 1979 · Bonet 1985",
    "2010-11-07 (Benedict XVI)": "2010-11-07 (Benedicto XVI)",
    "Vaults & Blancafort organ": "Bóvedas y órgano Blancafort",
    "Tower acoustic propagation": "Propagación acústica de torres",
    "138 m (2021) · 135 m (2023)": "138 m (2021) · 135 m (2023)",
    "172.5 m (12 stone panel levels)": "172.5 m (12 niveles pretensados)",
    "Prefabricated post-tensioned stone": "Piedra prefabricada pretensada",
    "2026-02-20 cross · 2026-06-10 blessing": "Cruz 2026-02-20 · bendición 2026-06-10",
    "Upper-arm interior & Agnus Dei": "Brazo superior y Agnus Dei",
    "Celebrates 5 generations": "Celebra a 5 generaciones",
    "Akbarzadeh et al. 2015 theory": "Teoría Akbarzadeh et al. 2015",
    "Cortés et al. 2019 hypar survey": "Estudio Cortés et al. 2019",
}

PARTS = [
    {
        "id": "part-1",
        "numeral": "I",
        "title_en": "Stone, Copper & Inverted Gravity",
        "title_es": "Piedra, cobre y gravedad invertida",
        "years": "1882–1914",
        "pull_en": "What hangs in pure tension stands in pure compression—giving builders without computers an analog physics engine in silk and shot.",
        "pull_es": "Lo que cuelga en tensión pura se sostiene en compresión pura: dando a constructores sin computadoras un motor físico analógico en hilo y plomo.",
        "opener": [
            {
                "en": "Every medieval cathedral fights a horizontal push where vaults lean outward on high stone walls. Gaudí refused external flying buttresses as structural crutches; shaped by metalwork geometry from his father’s forge in Reus and patient hours studying trees during childhood illness, he built upside-down string-and-shot models to watch gravity select compression lines.",
                "es": "Toda catedral medieval libra una batalla contra el empuje horizontal de sus bóvedas. Gaudí rechazó los arbotantes exteriores como muletas; formado en el volumen metálico de la forja paterna en Reus y en horas de estudio ante los árboles durante su niñez enferma, colgó maquetas invertidas de cordeles y perdigones para que la gravedad eligiera las líneas de compresión.",
                "src": ["heyman1966", "sf-gaudi"],
            },
            {
                "en": "On the Nativity facade and in the parallel 1:10 Colònia Güell hanging model (calibrated near 1:10,000 weight scale), tilting columns to follow the vector sum of vertical load V and horizontal thrust H kept loads centered in compression. Before his death in 1926, Saint Barnabas (1925) stood as a full-scale stone beacon for everyone coming next.",
                "es": "En el Nacimiento y en la maqueta paralela 1:10 de la Colònia Güell (calibrada cerca de 1:10,000 en pesos), inclinar las columnas según la resultante entre carga vertical V y empuje H mantuvo el esfuerzo en compresión centrada. Antes de morir en 1926, San Bernabé (1925) quedó erigida como guía real para quienes lo sucedieran.",
                "src": ["sf-history", "huerta2006"],
            },
        ],
        "cards": ["m1", "m2"],
        "interlude": "ruled-comparison",
    },
    {
        "id": "part-2",
        "numeral": "II",
        "title_en": "Ruled Geometry & The Living Canopy",
        "title_es": "Geometría reglada y el bosque vivo",
        "years": "1909–1926",
        "pull_en": "A surface curved in three dimensions can still be swept cleanly by a straight wooden rule—joining sublime form to a mason’s hand tool.",
        "pull_es": "Una superficie curva en el espacio puede engendrarse enteramente con una regla recta de madera, uniendo la forma sublime al oficio manual del cantero.",
        "opener": [
            {
                "en": "Arbitrary double-curved stone shells require unique templates for every block. Already in 1909 when building the small Parish Schools for the site workers’ children, Gaudí roofed humble brick classrooms with sinusoidal conoids swept by straight lines. After 1914 he devoted every waking year solely to the Basílica’s four ruled families.",
                "es": "Las cáscaras de doble curvatura arbitraria exigen plantillas únicas por sillar. Ya en 1909, al levantar las modestas Escuelas Parroquiales para los hijos de los trabajadores, Gaudí techó las aulas de ladrillo con conoides sinusoidales barridos por rectas. Desde 1914 consagró todos sus días exclusivamente a las cuatro familias regladas del templo.",
                "src": ["sf-booklets", "adell2005"],
            },
            {
                "en": "Each nave pier twists two star prisms in opposite directions—passing cleanly from n = 6, 8, 10, or 12 points up to 2n flutes across a shaft 10·D_in tall and a total height of 2n meters. In 2025, computational vision measurements of nave photographs revealed scale-invariant spatial frequency spectra closely matching natural forest canopies.",
                "es": "Cada pilar gira dos prismas estrellados en sentidos opuestos —pasando de n = 6, 8, 10 o 12 puntas al doble de estrías a lo largo de un fuste de 10·D_int y altura total 2n metros—. En 2025, un análisis estadístico de imágenes de la nave detectó espectros espaciales invariantes de escala semejantes a copas de bosque.",
                "src": ["barrios2006", "dyakova2025"],
            },
        ],
        "cards": ["m3"],
        "interlude": "quadrics",
    },
    {
        "id": "part-3",
        "numeral": "III",
        "title_en": "Ashes, Shards & Stubborn Fidelity",
        "title_es": "Cenizas, yesos y fidelidad tenaz",
        "years": "1936–1985",
        "pull_en": "Because every plaster shell obeyed a ruled quadratic formula, broken shards carried the equation of the whole cathedral inside a handful of gypsum.",
        "pull_es": "Como cada bóveda obedecía una ley cuádrica reglada, hasta los añicos de yeso conservaron la ecuación entera de la catedral dentro de un puñado de polvo.",
        "opener": [
            {
                "en": "In July 1936, fire gutted Gaudí’s studio and left his plaster scale models in fragments across the floor. From 1939 onward, site director Francesc de Paula Quintana led disciples, artisans, and later joint leaders Isidre Puig i Boada and Lluís Bonet i Garí to sift the debris and rebuild the models—choosing patient faithfulness over abandoning a century-long promise.",
                "es": "En julio de 1936, el fuego arrasó el obrador y dejó hechas añicos las maquetas de yeso. Desde 1939, Francesc de Paula Quintana encabezó a discípulos y modelistas —seguidos después por Isidre Puig i Boada y Lluís Bonet i Garí— para rescatar fragmentos entre los escombros y recomponer las maquetas.",
                "src": ["sf-history", "burry1996"],
            },
            {
                "en": "On the western Passion facade begun in 1954, builders laid the inclined compression struts bare outside the glass and opened the site museum in 1961 so citizens could inspect the geometry directly. As construction scaled past manual wood strings, high-flow self-compacting concrete and trencadís ceramic mosaics allowed dense reinforced hyperboloids and weatherproof pinnacles.",
                "es": "En la fachada de la Pasión iniciada en 1954 expusieron los tirantes pétreos inclinados fuera del vitral y abrieron el museo en 1961 para enseñar la geometría a la ciudad. Al crecer la escala, el hormigón autocompactante y el trencadís cerámico resolvieron armados densos y pináculos duraderos.",
                "src": ["gomez2009", "rodriguez2017"],
            },
        ],
        "cards": ["m4", "m5"],
        "interlude": "stone-hierarchy",
    },
    {
        "id": "part-4",
        "numeral": "IV",
        "title_en": "Algorithms, Light, Music & 172.5 Meters",
        "title_es": "Algoritmos, luz, música y 172.5 metros",
        "years": "1979–2026+",
        "pull_en": "From five-axis stone cutters and stained-glass chromatic light to tensioned stone reaching 172.5 m: technology became the servant of shared human stewardship.",
        "pull_es": "Desde sierras de cinco ejes y luz de vitrales hasta piedra pretensada a 172.5 m: la tecnología sirvió al relevo humano compartido.",
        "opener": [
            {
                "en": "Arriving in 1979 as a young architect, Mark Burry worked beside Gaudí’s elderly disciples to parameterize the plaster shard rulings under head architect Jordi Bonet i Armengol (1985), guiding five-axis diamond-wire stone cutters to close the 45 m nave vaults for consecration on November 7, 2010. Artist Joan Vila-Grau bathed those white columns in directional sunrise blue-greens and sunset reds, while Blancafort’s 1,492-pipe organ realized reverberant music rooted in Gaudí’s bell studies.",
                "es": "Llegado en 1979 siendo un joven arquitecto, Mark Burry colaboró con los discípulos ancianos para parametrizar las reglas de los fragmentos bajo el director Jordi Bonet i Armengol (1985), guiando sierras CNC de cinco ejes hasta consagrar las bóvedas de 45 m el 7 de noviembre de 2010. Joan Vila-Grau bañó esas columnas en luz direccional y el órgano Blancafort de 1,492 tubos encarnó los estudios acústicos del templo.",
                "src": ["burry1996", "gomez2009", "zhaoburry2024"],
            },
            {
                "en": "To erect six central spires up to 172.5 m without crushing 1882 footings under solid masonry weight, head architect Jordi Faulí (from 2012) and Arup engineer Tristram Carfrae joined Catalan ceramicists and quarries like Brinscall (UK) to assemble hollow post-tensioned stone panels—pre-assembled 54 m above the nave floor, lit with the 138 m Virgin Mary star (2021), 135 m Evangelists (2023), and crowned February 20, 2026 for the June 10 centenary.",
                "es": "Para alzar seis cimborrios hasta 172.5 m sin sobrecargar cimientos de 1882, el director Jordi Faulí (desde 2012) y Tristram Carfrae (Arup) unieron canteras como Brinscall y ceramistas catalanes en paneles huecos de piedra pretensada —preensamblados a 54 m sobre el suelo—, encendiendo la estrella de María (138 m, 2021), los Evangelistas (135 m, 2023) y coronando la cruz el 20 de febrero de 2026 rumbo al centenario.",
                "src": ["ingenia-arup", "sf-cross-2026", "sf-inauguration-2026"],
            },
        ],
        "cards": ["m6", "m7", "m8"],
        "interlude": "towers-ledger",
    },
]

# ---------------------------------------------------------------------------------------------------------------
# Conceptual plate drawer (explicit disclosure in both alt and caption; zero metadata)
# ---------------------------------------------------------------------------------------------------------------
EGG_BUTTON = {
    "hint_en": "Open the 1936 plaster-shard workshop drawer.",
    "hint_es": "Abrir el cajón de fragmentos de yeso de 1936.",
    "button_en": "Compare 1988 construction site vs. 1936 plaster atelier",
    "button_es": "Comparar obra de 1988 y obrador de yesos de 1936",
    "close_en": "Fold the workshop drawer shut",
    "close_es": "Cerrar el cajón del obrador",
}

PHOTOS = [
    {
        "id": "photo-1909-escoles",
        "kind": "photo",
        "era": "1909",
        "license": "Public Domain (PDM 1.0)",
        "author": "Archival 1909 photograph (Wikimedia Commons)",
        "image": "images/sagrada-familia/photo-1909-escoles-conoid.jpg",
        "width": 880,
        "height": 685,
        "alt_en": "1909 archival black-and-white photograph of Gaudí’s Parish Schools with its undulating sinusoidal conoid brick roof in the foreground and the rising Nativity bell towers behind.",
        "alt_es": "Fotografía histórica de 1909 en blanco y negro de las Escuelas de la Sagrada Família con su cubierta ondulada de conoides de ladrillo delante de los campanarios del Nacimiento.",
        "caption_en": "Archival site photograph (1909): the thin-brick sinusoidal conoid roof of the workers’ Parish Schools standing before the rising Nativity towers (Public Domain, Wikimedia Commons).",
        "caption_es": "Fotografía histórica de 1909: cubierta delgada de ladrillo en conoide sinusoide de las Escuelas obreras frente a las torres del Nacimiento en construcción (Dominio público, Wikimedia Commons).",
        "src": ["commons-escoles-1909", "adell2005"],
    },
    {
        "id": "photo-catenary-model",
        "kind": "photo",
        "era": "1898–1908 / 2009",
        "license": "CC BY 3.0 · Etan J. Tal",
        "author": "Etan J. Tal (2009)",
        "image": "images/sagrada-familia/photo-gaudi-catenary-model.jpg",
        "width": 1280,
        "height": 841,
        "alt_en": "Photograph of Gaudí’s suspended chain funicular model hanging upside down beside warm terracotta masonry arches illuminated inside the exhibition vault.",
        "alt_es": "Fotografía de una maqueta colgante de cadenas funiculares de Gaudí invertida junto a arcos de ladrillo cálido.",
        "caption_en": "Site reconstruction photograph: Gaudí’s polyfunicular hanging-chain statics model casting catenary curves in tension before inversion into stone compression (Etan J. Tal, CC BY 3.0).",
        "caption_es": "Fotografía documental: maqueta polifunicular colgante de Gaudí dibujando catenarias en tracción antes de invertirse en piedra a compresión (Etan J. Tal, CC BY 3.0).",
        "src": ["commons-catenary-model", "huerta2006"],
    },
    {
        "id": "photo-nativity-facade",
        "kind": "photo",
        "era": "1893–1930 / 2016",
        "license": "CC BY 2.0 · Richard Mortel",
        "author": "Richard Mortel (2016)",
        "image": "images/sagrada-familia/photo-nativity-facade.jpg",
        "width": 1280,
        "height": 853,
        "alt_en": "Photograph looking up the eastern Nativity facade of the Sagrada Família with sculpted stone portals, central cypress pinnacle, and four parabolic bell towers.",
        "alt_es": "Fotografía desde abajo de la fachada oriental del Nacimiento de la Sagrada Família con portales esculpidos, ciprés central y cuatro campanarios parabólicos.",
        "caption_en": "Site photograph: the eastern Nativity facade and its four 100 m parabolic bell towers, begun in Gaudí’s lifetime and crowned after the Saint Barnabas prototype of 1925 (Richard Mortel, CC BY 2.0).",
        "caption_es": "Fotografía del templo: fachada del Nacimiento y sus cuatro campanarios parabólicos tras el prototipo de San Bernabé en 1925 (Richard Mortel, CC BY 2.0).",
        "src": ["commons-nativity", "sf-history"],
    },
    {
        "id": "photo-1988-site",
        "kind": "photo",
        "era": "Spring 1988",
        "license": "Public Domain · J Dykstra",
        "author": "J Dykstra (1988)",
        "image": "images/sagrada-familia/photo-1988-construction.jpg",
        "width": 1280,
        "height": 849,
        "alt_en": "1988 construction photograph looking down into the unroofed Sagrada Família nave floor stacked with numbered cut stones and a yellow tower crane between unfinished columns.",
        "alt_es": "Fotografía de obra de 1988 desde altura sobre la nave sin cubrir de la Sagrada Família, con bloques numerados de piedra y una grúa torre amarilla.",
        "caption_en": "Spring 1988 archival construction photograph: pre-roof nave piers, stacked numbered masonry blocks, and tower cranes bridging Generation 3 precast work to CAD stereotomy (J Dykstra, Public Domain).",
        "caption_es": "Fotografía de obra en primavera de 1988: pilares de la nave aún descubierta, sillares numerados y grúas conectando el prefabricado con el CAD (J Dykstra, Dominio público).",
        "src": ["commons-1988", "gomez2009"],
    },
    {
        "id": "photo-nave-columns",
        "kind": "photo",
        "era": "2011",
        "license": "CC BY 2.0 · Tony Hisgett",
        "author": "Tony Hisgett",
        "image": "images/sagrada-familia/photo-nave-branching-vaults.jpg",
        "width": 1280,
        "height": 1920,
        "alt_en": "Interior upward photograph of the Sagrada Família nave showing cream sandstone, gray granite, dark basalt, and red porphyry star columns branching into star hyperboloid ceiling vaults.",
        "alt_es": "Fotografía interior ascendente de la nave de la Sagrada Família con columnas de arenisca clara, granito gris, basalto oscuro y pórfido rojo ramificándose hacia bóvedas estrelladas hiperboloides.",
        "caption_en": "Interior photograph showing all four hierarchical stone tiers (Montjuïc sandstone, granite, basalt, and red porphyry) branching upward to support pierced star hyperboloid ceiling vaults (Tony Hisgett, CC BY 2.0).",
        "caption_es": "Fotografía interior mostrando los cuatro rangos de piedra (arenisca de Montjuïc, granito, basalto y pórfido rojo) ramificados hacia bóvedas de óculos hiperboloides (Tony Hisgett, CC BY 2.0).",
        "src": ["commons-nave-interior", "sf-booklets"],
    },
    {
        "id": "photo-2026-cross",
        "kind": "photo",
        "era": "August 2026",
        "license": "CC0 1.0 Public Domain · Hokky",
        "author": "Hokky / ほっきー (2026)",
        "image": "images/sagrada-familia/photo-2026-completed-cross.jpg",
        "width": 1280,
        "height": 1855,
        "alt_en": "Photograph from August 2026 reflecting the Basílica across water, showing the central 172.5 m Tower of Jesus Christ topped with its gleaming white 17 m ceramic-and-glass cross beside the 138 m star and Evangelist towers.",
        "alt_es": "Fotografía de agosto de 2026 reflejada en el estanque mostrando la torre central de Jesucristo de 172.5 m coronada por su cruz blanca de 17 m junto a la estrella de 138 m y las torres de los Evangelistas.",
        "caption_en": "August 2026 photograph reflected in Plaça de Gaudí: the 172.5 m Tower of Jesus Christ topped with its white 17 m ceramic-and-glass cross, flanking the 135 m Evangelists and 138 m Virgin Mary star (Hokky, CC0 1.0).",
        "caption_es": "Fotografía de agosto de 2026 reflejada en la plaza de Gaudí: la torre de Jesucristo de 172.5 m con su cruz blanca de 17 m junto a los Evangelistas (135 m) y la estrella de María (138 m) (Hokky, CC0 1.0).",
        "src": ["commons-2026-cross", "sf-cross-2026"],
    },
]

PLATES = [
    {
        "id": "plate-reus-forge",
        "kind": "render",
        "era": "c. 1860",
        "image": "images/sagrada-familia/sagrada-reus-coppersmith-forge.jpg",
        "width": 1280,
        "height": 720,
        "alt_en": "Conceptual visualization imagining a 19th-century Catalonian coppersmith bench in Reus: flat copper sheet, conical and hyperboloid vessels, calipers, and an olive tree outside the stone window (artistic impression, not an archival photograph).",
        "alt_es": "Visualización conceptual que imagina un banco de calderero catalán en Reus en el siglo XIX: láminas de cobre, embudos hiperboloides y cónicos, compases y un olivo tras la ventana de piedra (impresión artística, no es fotografía histórica).",
        "caption_en": "Conceptual visualization imagining Gaudí’s boyhood coppersmith bench in Reus (from 1860): turning flat hammered sheet copper into 3D ruled cones and vessels beside natural foliage outside (artistic impression, not an archival photograph).",
        "caption_es": "Visualización conceptual que imagina el taller infantil de calderería en Reus (desde 1860): convertir chapa plana de cobre en conos y vasijas regladas en 3D junto a árboles vivos fuera de la ventana (impresión artística, no es fotografía histórica).",
        "src": ["sf-gaudi", "sf-humanism"],
    },
    {
        "id": "plate-nave-forest",
        "kind": "render",
        "era": "Interior Vision",
        "image": "images/sagrada-familia/sagrada-nave-forest.jpg",
        "width": 1280,
        "height": 720,
        "alt_en": "Conceptual visualization imagining looking upward inside a Sagrada Família-inspired stone nave: fluted branching columns, star hyperboloid oculi, and emerald-to-amber stained-glass light (artistic impression, not a measured drawing or blueprint).",
        "alt_es": "Visualización conceptual que imagina la vista ascendente dentro de una nave pétrea inspirada en la Sagrada Família: columnas estriadas ramificadas, óculos en estrella hiperboloide y luz de vitrales esmeralda a ámbar (impresión artística, no es un plano medido).",
        "caption_en": "Conceptual visualization imagining what the sunlit branching porphyry and granite stone forest beneath star hyperboloid vaults looks like (artistic impression, not a measured structure; stated geometric equations and dimensions remain intact in the interactive benches below).",
        "caption_es": "Visualización conceptual que imagina cómo se percibe el bosque de columnas de pórfido y granito bajo bóvedas hiperboloides iluminadas (impresión artística, no es un plano medido; las ecuaciones y proporciones planteadas permanecen intactas en los bancos interactivos de abajo).",
        "src": ["sf-booklets", "barrios2006"],
    },
    {
        "id": "plate-stereotomy-atelier",
        "kind": "render",
        "era": "1936–1985 Studio",
        "image": "images/sagrada-familia/sagrada-stereotomy-atelier.jpg",
        "width": 1280,
        "height": 720,
        "alt_en": "Conceptual visualization imagining Gaudí’s stonecutting and plaster-model workbench: brass-strung plaster hyperboloid and saddle paraboloid beside hanging chains and a star-cut granite block (artistic impression, not an archival photograph).",
        "alt_es": "Visualización conceptual que imagina la mesa del obrador de estereotomía: hiperboloide y paraboloide de yeso tensados con hilos de latón junto a cadenas colgantes y un bloque de granito estrellado (impresión artística, no es fotografía de archivo).",
        "caption_en": "Conceptual visualization imagining what the Barcelona plaster-and-chain stereotomy workbench looks like, pairing a doubly-ruled one-sheet hyperboloid, hyperbolic paraboloid saddle, hanging catenary frame, and fluted granite star section (artistic impression, not an archival photograph).",
        "caption_es": "Visualización conceptual que imagina cómo luce la mesa del obrador de yeso y cadenas en Barcelona, reuniendo un hiperboloide doblemente reglado, un paraboloide hiperbólico en silla, un marco de catenarias y una sección estrellada en granito (impresión artística, no es fotografía de archivo).",
        "src": ["sf-history", "gomez2009"],
    },
    {
        "id": "plate-tensioned-crown",
        "kind": "render",
        "era": "2016–2026 Stone Panels",
        "image": "images/sagrada-familia/sagrada-post-tensioned-crown.jpg",
        "width": 1280,
        "height": 720,
        "alt_en": "Conceptual visualization imagining a hollow prefabricated Montjuïc sandstone and light granite tower panel cut along straight ruled planes with vertical stainless post-tensioning rods and white trencadís inset above morning Barcelona (artistic impression, not a construction drawing).",
        "alt_es": "Visualización conceptual que imagina un panel hueco prefabricado de arenisca de Montjuïc y granito cortado en planos reglados con barras verticales de acero inoxidable y trencadís blanco sobre la Barcelona matinal (impresión artística, no es un plano de obra).",
        "caption_en": "Conceptual visualization imagining prefabricated hollow stone masonry panels cut with straight wire-cut bevels and threaded stainless tensioning rods above morning clouds (artistic impression, not an engineering blueprint; wind-stress equations live in Part VI below).",
        "caption_es": "Visualización conceptual que imagina los paneles huecos prefabricados de piedra cortados en planos rectos y comprimidos con acero inoxidable sobre el cielo matinal (impresión artística, no es plano constructivo; el modelo de esfuerzo eólico vive en la Parte VI).",
        "src": ["ingenia-arup", "sf-cross-2026"],
    },
]

# ---------------------------------------------------------------------------------------------------------------
# New Visual Observatory Specs: 1:500 <-> 1:10 Tectonic Loupe, Alluvial Gravity Sankey, 6-Axis Polar Radar & Gallery
# ---------------------------------------------------------------------------------------------------------------
TECTONIC_LOUPE_TEXT = {
    "kicker_en": "Dual-Scale Tectonic Plate · 1:500 Section ↔ 1:10 Stereotomy Loupe",
    "kicker_es": "Lámina Tectónica Dual · Sección 1:500 ↔ Lupa 1:10",
    "title_en": "Inspect the Temple Across Four Vertical Scales",
    "title_es": "Inspecciona el templo en cuatro escalas verticales",
    "intro_en": "Select any structural zone on the 1:500 elevation from crypt footings to the 172.5 m lantern cross to inspect how material choice, joint compression, and ruled stone geometry shift at 1:10 nodal detail.",
    "intro_es": "Elige cualquier zona estructural del alzado 1:500 desde los cimientos de la cripta hasta la cruz a 172.5 m para observar cómo cambian la piedra, el pretensado y la geometría reglada al detalle nodal 1:10.",
}

LOUPE_NODES = [
    {
        "id": "footing",
        "short_en": "0 m · 1882 Footing",
        "short_es": "0 m · Cimiento 1882",
        "elev": "-5 m to 0 m",
        "title_en": "Crypt Footings & Porphyry Anchors (0 m)",
        "title_es": "Cimientos de la cripta y anclaje en pórfido (0 m)",
        "summary_en": "Crossing piers drop through 19th-century crypt foundations; keeping central lanterns light upstream protects soil bearing limits below.",
        "summary_es": "Los pilares del crucero apoyan sobre cimientos del siglo XIX; aligerar los cimborrios superiores protege la capacidad portante del terreno.",
        "src": ["sf-history", "ingenia-arup"],
    },
    {
        "id": "knot",
        "short_en": "24 m · Branching Knot",
        "short_es": "24 m · Nudo ramificado",
        "elev": "21 m – 30 m",
        "title_en": "Ellipsoid Capital Knot & Diagonal Shoots (1:10)",
        "title_es": "Nudo elipsoidal y ramas inclinadas (1:10)",
        "summary_en": "At 10·D_in shaft height, double-twisted 12-point red porphyry shafts bloom into multi-branch granite stems aimed right into ceiling oculus rings.",
        "summary_es": "A la altura 10·D_int del fuste, las columnas de pórfido rojo de 12 puntas se bifurcan en ramas de granito alineadas con los anillos de bóveda.",
        "src": ["sf-booklets", "barrios2006"],
    },
    {
        "id": "oculus",
        "short_en": "45–60 m · Star Oculus",
        "short_es": "45–60 m · Óculo estrellado",
        "elev": "45 m nave · 60 m crossing",
        "title_en": "Hyperboloid Sunlight Diffuser Ring (45–60 m)",
        "title_es": "Anillo difusor hiperboloide de bóveda (45–60 m)",
        "summary_en": "Straight tangents of a one-sheet hyperboloid carve a golden oculus funnel between adjacent hyperbolic paraboloids, washing glare into soft daylight.",
        "summary_es": "Las tangentes rectas de un hiperboloide tallan el embudo dorado entre paraboloides adyacentes, transformando el sol directo en luz difusa.",
        "src": ["burry1996", "gomez2009"],
    },
    {
        "id": "crown",
        "short_en": "142–172.5 m · Tensioned Cross",
        "short_es": "142–172.5 m · Cruz pretensada",
        "elev": "85 m – 172.5 m",
        "title_en": "Post-Tensioned Hollow Stone & 17 m Cross Crown",
        "title_es": "Piedra hueca pretensada y cruz terminal de 17 m",
        "summary_en": "Twelve CNC-milled hollow levels locked with unbonded stainless steel bars carry the glazed white trencadís and ceramic-glass cross cleanly under Barcelona coastal wind.",
        "summary_es": "Doce niveles huecos fresados y postensados con acero inoxidable sostienen la cruz blanca de 17 m × 13.5 m ante el viento costero de Barcelona.",
        "src": ["ingenia-arup", "sf-cross-2026"],
    },
]

SANKEY_TEXT = {
    "kicker_en": "Alluvial Conservation Ribbon · Gravity Thrust Split (MODEL Illustration)",
    "kicker_es": "Diagrama Aluvial de Flujo · Reparto de Empujes (Ilustración MODELO)",
    "title_en": "Gaudí’s Branched Tree Flow vs. Classical Flying-Buttress Split",
    "title_es": "Árbol ramificado de Gaudí frente al arbotante gótico clásico",
    "intro_en": "Compare a notional 360 kN canopy gravity flux across two topologies: Gothic pointed ribs split sideways thrust through external stone crutches outside the glass, whereas angled branching trunks channel 360 kN internally down to 0 kN external crutches.",
    "intro_es": "Compara un flujo hipotético de 360 kN de cubierta entre dos topologías: las bóvedas góticas derivan empuje lateral hacia arbotantes externos, mientras los fustes inclinados canalizan los 360 kN internamente hasta el cimiento con 0 kN en arbotantes externos.",
    "readout_gaudi_en": "MODEL Flow (Branched Canopy): 360 kN canopy -> 180 kN primary piers + 180 kN aisle ring -> 360 kN internal base · External flying buttresses = 0 kN",
    "readout_gaudi_es": "MODELO Flujo (Bosque Ramificado): 360 kN cubierta -> 180 kN pilares centrales + 180 kN anillo lateral -> 360 kN cimiento interno · Arbotantes externos = 0 kN",
    "readout_gothic_en": "MODEL Flow (Classical Gothic): 360 kN vault -> 240 kN nave piers + 120 kN lateral thrust bypassed externally through masonry flying buttresses",
    "readout_gothic_es": "MODELO Flujo (Gótico Clásico): 360 kN bóveda -> 240 kN pilares de nave + 120 kN empuje lateral desviado por arbotantes exteriores",
    "src": ["heyman1966", "huerta2006", "akbarzadeh2015"],
}

RADAR_TEXT = {
    "kicker_en": "6-Axis Structural & Acoustic Performance Envelope · MODEL Comparative Index (0–100)",
    "kicker_es": "Envolvente Polar de 6 Ejes · Índice Comparativo MODELO (0–100)",
    "title_en": "How Five Generations Expanded Elevation, Daylight & Wind Margin",
    "title_es": "Cómo cinco generaciones ampliaron altura, luz natural y margen eólico",
    "intro_en": "Toggle across structural eras to see the conceptual 6-axis tradeoff (normalized 0–100 MODEL comparative index illustrating structural literature trends, not measured site instrumentation): transitioning to CAD and post-tensioned stone panels unlocks 172.5 m height with lower dead weight per meter.",
    "intro_es": "Cambia entre etapas constructivas en este índice comparativo MODELO normalizado 0–100 (ilustra tendencias de la literatura técnica, no telemetría de sensores en obra): pasar al CAD y a paneles huecos pretensados permite alcanzar 172.5 m reduciendo la masa muerta por metro.",
    "axes_en": ["Elevation Reach", "Wind Uplift Margin", "Ruled Repeatability", "Mass Efficiency", "Zenith Daylight", "Acoustic Diffusion"],
    "axes_es": ["Altura alcanzada", "Margen ante viento", "Repetitividad reglada", "Ligereza de masa", "Luz cenital", "Difusión acústica"],
    "src": ["ingenia-arup", "zhaoburry2024", "burry1996"],
}

RADAR_ERAS = [
    {
        "id": "gothic",
        "label_en": "Classical Gothic Baseline",
        "label_es": "Referencia gótica clásica",
        "scores": [42, 46, 30, 34, 48, 52],
        "note_en": "Pointed masonry vaults aided by external buttresses; heavy timber scaffolding and lower roof daylight penetration.",
        "note_es": "Bóvedas apuntadas asistidas por arbotantes externos; cimbras pesadas y menor entrada cenital de luz.",
    },
    {
        "id": "gaudi1926",
        "label_en": "1882–1926 · Hanging Chain & Parabolic Spires",
        "label_es": "1882–1926 · Catenaria y torres parabólicas",
        "scores": [62, 60, 74, 52, 68, 72],
        "note_en": "Funicular inversion aligns piers inside compression cones; Nativity towers sculpted in solid blockwork.",
        "note_es": "La inversión funicular alinea los pilares; las torres del Nacimiento se labran en sillería pesada.",
    },
    {
        "id": "cad2010",
        "label_en": "1979–2012 · Aerospace CAD & Nave Vaults",
        "label_es": "1979–2012 · CAD y bóvedas de nave (45 m)",
        "scores": [78, 74, 96, 66, 94, 92],
        "note_en": "Parametric hyperboloids and 5-axis diamond-wire cutting complete the 45 m starry canopy and Vila-Grau solar spectrum.",
        "note_es": "Los hiperboloides paramétricos y el corte por hilo diamantado cierran la nave de 45 m con vitrales de Vila-Grau.",
    },
    {
        "id": "fauli2026",
        "label_en": "2012–2026 · Post-Tensioned Stone Panels (172.5 m)",
        "label_es": "2012–2026 · Paneles pretensados (172.5 m)",
        "scores": [98, 95, 97, 94, 92, 88],
        "note_en": "Prefabricated hollow stone panels tensioned with stainless bars keep joints compressed while cutting central tower mass.",
        "note_es": "Paneles huecos prefabricados pretensados con acero inoxidable comprimen juntas reduciendo el peso sobre cimientos antiguos.",
    },
]

VISUAL_GALLERY_TEXT = {
    "kicker_en": "All Media Archive · 6 Verified Photos + 4 Conceptual Atelier Plates",
    "kicker_es": "Archivo Visual Completo · 6 Fotos Documentales + 4 Láminas Conceptuales",
    "title_en": "Inspect Every Photograph & Conceptual Visualization Fullscreen",
    "title_es": "Explora cada fotografía documental y lámina conceptual a pantalla completa",
    "intro_en": "Filter between real historical and modern Wikimedia Commons site photographs (PD / CC0 / CC BY) and explicitly labeled AI-assisted conceptual visualizations, or open any card inside the accessible fullscreen plate viewer.",
    "intro_es": "Filtra entre fotografías históricas y modernas reales de Wikimedia Commons (PD / CC0 / CC BY) y visualizaciones conceptuales asistidas por IA debidamente rotuladas, o abre cualquiera en el visor accesible.",
    "all_en": "All 10 Media",
    "all_es": "Las 10 vistas",
    "photos_en": "Site & Archival Photos (6)",
    "photos_es": "Fotos de archivo y obra (6)",
    "renders_en": "Conceptual Plates (4)",
    "renders_es": "Láminas conceptuales (4)",
    "badge_photo_en": "SITE / ARCHIVAL PHOTO",
    "badge_photo_es": "FOTO DE OBRA / ARCHIVO",
    "badge_render_en": "CONCEPTUAL RENDER · AI-ASSISTED",
    "badge_render_es": "VISUALIZACIÓN CONCEPTUAL · IA",
}

PLATES_ES_SAFE = True

# ---------------------------------------------------------------------------------------------------------------
# Interactive Benches Copy (EN + ES-MX)
# ---------------------------------------------------------------------------------------------------------------
RELAY_TEXT = {
    "kicker_en": "Five Generations · 1882–2026+ Human Continuity Observatory",
    "kicker_es": "Cinco Generaciones · Observatorio de Continuidad Humana 1882–2026+",
    "title_en": "How Five Generations Carried One Work Across 144 Years",
    "title_es": "Cómo cinco generaciones sostuvieron una obra durante 144 años",
    "intro_en": "Seldom in human history do grandparents lay foundations knowing neither they nor their grandchildren will see the cross installed. Select each generation (1882–2026+) to trace who held the site, what historical break threatened to end it, and what geometric or structural gift they left for builders yet unborn.",
    "intro_es": "Pocas veces en la historia una generación coloca cimientos sabiendo que ni sus nietos verán coronar la aguja. Selecciona cada generación (1882–2026+) para explorar quién cuidó la obra, qué ruptura histórica amenazó con detenerla y qué legado geométrico dejó a quienes vendrían después.",
}

ATELIER_TEXT = {
    "kicker_en": "Coupled 2D ↔ 3D Observatory · Stereotomy Plate",
    "kicker_es": "Observatorio Acoplado 2D ↔ 3D · Lámina de Estereotomía",
    "title_en": "From Hanging Catenary to 3D Ruled Stone (Live GLB & DXF Export)",
    "title_es": "De la cadena colgante a la piedra reglada en 3D (Exportación GLB y DXF)",
    "intro_en": "Adjust the central lantern load or vault shape on the left: the 2D funicular arch recomputes horizontal thrust H, vertical reaction V, and the computed column inclination θ = arctan(H/V) measured from vertical—and steers the 3D WebGL2 column on the right live. Switch 3D modes to inspect straight-line wire rulings on the hyperboloid, saddle paraboloid, and Schools conoid, then export a watertight .glb mesh or .dxf stonecutting template directly from your browser.",
    "intro_es": "Ajusta la carga concentrada del cimborrio o la altura de la bóveda a la izquierda: el arco funicular 2D recalcula el empuje horizontal H, la reacción vertical V y la inclinación θ = arctan(H/V) medida desde la vertical, orientando en vivo la columna 3D en WebGL2 a la derecha. Cambia de superficie para ver las rectas regladas en el hiperboloide, paraboloide y conoide de las Escuelas, y exporta un sólido .glb o plantilla .dxf desde tu navegador.",
    "science_en": "Heyman’s 1966 plastic limit framework explains in general why compression masonry stands when a thrust line lies inside the stone section; Huerta (2006) documents how Gaudí’s 1:10 hanging models enacted that statics physically; Akbarzadeh et al. (2015) extend graphic statics to 3D polyhedral frames. Heyman (1966) and Akbarzadeh (2015) did not test the Basílica; numerical bench outputs come from the MODEL parameters in Part VI.",
    "science_es": "El marco límite de Heyman (1966) explica en general por qué la mampostería sin tracción trabaja cuando la línea de empuje permanece dentro del espesor pétreo; Huerta (2006) documenta cómo las maquetas 1:10 de Gaudí materializaron esa estática; Akbarzadeh et al. (2015) la extienden a poliedros 3D. Ni Heyman ni Akbarzadeh ensayaron la Basílica; los valores mostrados provienen del MODELO en la Parte VI.",
}

COL_BENCH_TEXT = {
    "kicker_en": "Boolean Stone Hierarchy · 6, 8, 10 & 12 Points",
    "kicker_es": "Jerarquía Pétrea Booleana · 6, 8, 10 y 12 Puntas",
    "title_en": "Counter-Rotating Star Columns & Material Tiers",
    "title_es": "Columnas estrelladas de doble giro y rangos de piedra",
    "intro_en": "Select a Basílica stone tier and scrub height fraction z / H_shaft from base (0.00) to capital neck (1.00): two identical star polygons twist by +θ and −θ in opposite senses. Where they overlap, n outer ridges split smoothly into 2n facets with zero pinch.",
    "intro_es": "Elige un rango de piedra de la Basílica y desliza la fracción de altura z / H_fuste desde la base (0.00) hasta el capitel (1.00): dos polígonos estrellados idénticos giran +θ y −θ en sentidos opuestos. En su intersección, n aristas iniciales se duplican suavemente en 2n facetas sin estrangulamiento.",
}

SHARD_BENCH_TEXT = {
    "kicker_en": "1936 Workshop Rescue · Why Ruled Surfaces Survive Fire",
    "kicker_es": "Rescate del Obradoiro de 1936 · Por Qué Sobrevive lo Reglado",
    "title_en": "Recovering an Entire 3 m Vault from a 35 cm Plaster Shard",
    "title_es": "Recuperar una bóveda de 3 m desde un fragmento de yeso de 35 cm",
    "intro_en": "When Francesc Quintana and later Mark Burry measured broken gypsum slivers from the July 1936 fire, why could a palm-sized 0.35 m piece rebuild the upper vault? Scrub the caliper perturbation δr (0 to 2.0 mm): because a one-sheet hyperboloid obeys r²(z) = a² + (a²/c²)·z², two chord measurements lock onto global parameters (a, c), whereas local freeform curve fitting drifts by 311.6 mm at the rim.",
    "intro_es": "Cuando Francesc Quintana y después Mark Burry midieron restos rotos de yeso tras el incendio de 1936, ¿por qué bastaba una pieza de 0.35 m para reconstruir la bóveda superior? Desliza el error de calibrador δr (0 a 2.0 mm): como el hiperboloide obedece r²(z) = a² + (a²/c²)·z², dos cuerdas determinan (a, c) globalmente, mientras una extrapolación libre se desvía 311.6 mm en la corona.",
}

TOWER_BENCH_TEXT = {
    "kicker_en": "18 Towers & Post-Tensioned Stone Decompression",
    "kicker_es": "18 Torres y Descompresión en Piedra Pretensada",
    "title_en": "Barcelona Skyline Datum (172.5 m vs 177.7 m) & Tensioned Panel Stress",
    "title_es": "Cota urbana (172.5 m vs 177.7 m) y esfuerzo en paneles pretensados",
    "intro_en": "Compare the Basílica tower ensemble (crowned February 20, 2026) against Ulm Minster (161.5 m) and Montjuïc Hill (177.7 m), then test why Arup and the Basílica engineers pre-compress prefabricated stone panels with stainless steel bars: keep windward edge stress σ_min ≥ 0 so mortar and epoxy joints remain shut under wind overturning moment M_wind.",
    "intro_es": "Compara el conjunto de torres (coronado el 20 de febrero de 2026) frente a la Catedral de Ulm (161.5 m) y Montjuïc (177.7 m), y comprueba por qué Arup y los ingenieros de la Basílica precomprimen paneles prefabricados de piedra con barras de acero inoxidable: mantener σ_min ≥ 0 en barlovento evita que las juntas se abran bajo el momento de viento M_viento.",
}

LIGHT_BENCH_TEXT = {
    "kicker_en": "Solar Azimuth, Stained Glass & Organ Acoustics",
    "kicker_es": "Acimut Solar, Vitrales y Acústica del Órgano",
    "title_en": "East-to-West Stained-Glass Chromatics & Eyring Reverberation",
    "title_es": "Cromatismo solar de oriente a poniente y reverberación de Eyring",
    "intro_en": "Scrub the solar hour from dawn to sunset across the nave section: morning sunlight enters the eastern Nativity glass in cool blues and greens conceived with glassmaster Joan Vila-Grau, noon light drops down through hyperboloid ceiling oculi, and sunset warms the western Passion glass in amber and crimson—resonating beside the 1,492-pipe Blancafort organ and tubular bell concepts.",
    "intro_es": "Desliza la hora solar del alba al ocaso sobre la nave: el sol de mañana entra por los vitrales del Nacimiento en tonos azules y verdes diseñados con Joan Vila-Grau, el mediodía desciende por óculos hiperboloides y la tarde tiñe los vitrales de la Pasión en ámbar y carmesí, resonando junto al órgano Blancafort de 1,492 tubos.",
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
    "note_en": "Equilibrium identity checked against Heyman (1966) masonry rules; Huerta (2006) reviews Gaudí’s hanging models; Colònia Güell portico hyperboloids are surveyed in Cortés et al. (2019). Neither paper states one uniform nave span.",
    "note_es": "Identidad de equilibrio comprobada frente a Heyman (1966); Huerta (2006) analiza las maquetas funiculares de Gaudí; los paraboloides de la Colònia Güell se estudian en Cortés et al. (2019). Ninguna fuente fija un solo claro único para toda la nave.",
    "src": ["heyman1966", "huerta2006", "cortes2019"],
}

QUADRICS_LEDGER = {
    "title_en": "The four ruled families of the Sagrada Família & 1909 Schools",
    "title_es": "Las cuatro familias regladas de la Sagrada Família y las Escuelas de 1909",
    "items": [
        ("One-sheet hyperboloid", "Hiperboloide de una hoja",
         "Generated by two families of straight lines sweeping around an elliptical or circular throat; distributes sunlight through nave oculi while remaining formable with straight slats.",
         "Generado por dos familias de rectas alrededor de una garganta elíptica o circular; difunde luz por óculos de bóveda y permite cimbra con listones rectos."),
        ("Hyperbolic paraboloid (Hypar)", "Paraboloide hiperbólico",
         "Doubly-ruled saddle surface forming smooth stone transitions between columns, vaults, and tower openings.",
         "Superficie en silla doblemente reglada que resuelve transiciones continuas entre columnas, bóvedas y vanos de torre."),
        ("Helicoid", "Helicoide",
         "Generated by rotating and translating a line along an axis; shapes the double-twist arborescent columns and spiral stairs.",
         "Generado al rotar y trasladar una recta a lo largo de un eje; da forma a fustes arbóreos de doble giro y escaleras helicoidales."),
        ("Sinusoidal conoid (1909 Schools)", "Conoide sinusoide (Escuelas 1909)",
         "Generated by straight lines connecting a straight ridge girder to a wavy sinusoidal eave, giving a thin-brick school roof for workers’ children surprising stiffness against wind.",
         "Generado por rectas que unen una viga recta central con un alero sinusoide, rigidizando la cubierta de ladrillo de la escuela obrera de 1909."),
    ],
    "src": ["sf-booklets", "adell2005", "gomez2009"],
}

# ---------------------------------------------------------------------------------------------------------------
# Part VI · Stereotomy & Structural Mechanics Lab (5 models recomputed by skills/classics/cc02/verify_cc02_sagrada.py)
# ---------------------------------------------------------------------------------------------------------------
LAB = {
    "title_en": "Stereotomy & Mechanics Lab: five models, worked in the open",
    "title_es": "Laboratorio de Estereotomía y Mecánica: cinco modelos resueltos",
    "intro_en": "The eight moves and five-generation relay above tell the human story. This lab puts numbers to five mechanisms behind that continuity: doubly-ruled hyperboloid straightness, catenary vs. parabolic equilibrium, counter-rotating star columns, post-tensioned stone decompression, and algebraic recovery from 1936 plaster shards. Every non-sourced input is labeled MODEL; the repository verifier recomputes every cell independently and fails under five planted defects.",
    "intro_es": "Las ocho jugadas y el relevo de cinco generaciones cuentan la historia humana. Este laboratorio cifra cinco mecanismos detrás de esa continuidad: la rectitud del hiperboloide reglado, el equilibrio catenario frente a la parábola, las columnas de doble giro, la piedra pretensada y la recuperación algebraica de fragmentos de yeso de 1936. Toda entrada no tomada de fuentes primarias se etiqueta MODELO; el verificador recalcula cada celda y falla ante cinco defectos plantados.",
    "hyp_h_en": "1 · Doubly-ruled one-sheet hyperboloid without curved formwork",
    "hyp_h_es": "1 · Hiperboloide de una hoja doblemente reglado sin cimbra curva",
    "hyp_en": "For fixed parameter u and family sign s in {+1, −1}, r(u, v) = (a(cos u − s·v·sin u), b(sin u + s·v·cos u), v·c) traces a straight line as v varies—yet satisfies (x/a)² + (y/b)² − (z/c)² = 1 across the funnel. Straight saw cuts or taut timber strings thus sweep out doubly curved stone openings. Dimensions below are MODEL throat parameters.",
    "hyp_es": "Para u fijo y s en {+1, −1}, r(u, v) = (a(cos u − s·v·sen u), b(sin u + s·v·cos u), v·c) traza una recta al variar v y satisface (x/a)² + (y/b)² − (z/c)² = 1 en toda la garganta. Cortes rectos o cuerdas tensas engendran así embudos de doble curvatura. Las dimensiones son parámetros MODELO.",
    "fun_h_en": "2 · Hanging catenary vs. parabola & column thrust angle",
    "fun_h_es": "2 · Catenaria colgante vs. parábola e inclinación de columna",
    "fun_en": "A cord carrying uniform weight per horizontal meter forms a parabola; a masonry arch carrying uniform self-weight per meter of curved arc forms a catenary. Adding concentrated lantern load W_top introduces slope offset α₀ = arcsinh(W_top / (2H)), tilting the support angle from vertical by θ = arctan(H / V). Setting W_top to zero shows how much an unloaded catenary rises above an equal-span, equal-rise parabola on the haunches.",
    "fun_es": "Un cable con carga uniforme por metro horizontal dibuja una parábola; un arco pétreo con peso propio uniforme por metro de arco describe una catenaria. Añadir carga de linterna W_top introduce α₀ = arcsenh(W_top / (2H)) e inclina la resultante en θ = arctan(H / V). Con W_top nulo se observa cuánto supera la catenaria a la parábola equivalente en los riñones.",
    "col_h_en": "3 · Double-twisted star columns: height rule, Boolean area & net stress",
    "col_h_es": "3 · Columnas estrelladas de doble giro: altura, área booleana y esfuerzo neto",
    "col_en": "Gaudí’s Basílica columns obey two published ratios: total height in meters equals double the star-point count (H_total = 2n m), and shaft height equals ten times inner diameter (H_shaft = 10·D_in). Intersecting two counter-rotating n-star prisms over ±π/(2n) transforms n ridges into 2n facets with positive net area A_net (minus a MODEL central duct void). Axial loads N below are MODEL illustrations by tier.",
    "col_es": "Las columnas siguen dos razones documentadas: la altura total en metros duplica las puntas (H_total = 2n m), y el fuste mide diez diámetros interiores (H_fuste = 10·D_int). Intersectar dos prismas estrellados girados ±π/(2n) transforma n aristas en 2n facetas con área neta A_neta (descontando un ducto MODELO). Las cargas axiales N son valores MODELO.",
    "pt_h_en": "4 · Post-tensioned stone tower panels under Barcelona wind",
    "pt_h_es": "4 · Paneles de piedra pretensada bajo viento en las torres",
    "pt_en": "Masonry joints carry compression well and resist minimal tension. Threading unbonded stainless steel bars through prefabricated hollow stone panels adds concentric pre-compression F_pt so windward extreme fiber stress σ_min = (F_pt + N_dead)/A_net − M_wind/Z_net remains non-negative under characteristic wind overturning moment M_wind. All panel dimensions and wind loads below are MODEL parameters illustrating the Arup/Basílica mechanism.",
    "pt_es": "Las juntas de mampostería trabajan bien a compresión y resisten tracción mínima. Pasar barras de acero inoxidable por paneles huecos añade precompresión F_pt para que el esfuerzo mínimo de borde a barlovento σ_min = (F_pt + N_dead)/A_net − M_viento/Z_net permanezca positivo o nulo bajo el momento de volteo del viento M_viento. Todas las dimensiones y cargas son parámetros MODELO.",
    "shard_h_en": "5 · 1936 plaster-shard algebraic recovery vs. freeform drift",
    "shard_h_es": "5 · Recuperación algebraica desde fragmentos de 1936 vs. deriva libre",
    "shard_en": "On a MODEL circular one-sheet hyperboloid (a = 1.80 m, c = 2.40 m), imagine only a 0.35 m height band survives from the 1936 studio fire (between z₁ = 0.20 m and z₂ = 0.55 m). Solving r²(z) = a² + (a²/c²)·z² from two measured shard chords reconstructs the full 3.00 m vault rim cleanly; even under ±1.0 mm opposite-sign caliper error, the ruled reconstruction stays bounded near 43 mm, whereas unruled local quadratic Taylor extrapolation from the same fragment drifts by 311.6 mm at the top.",
    "shard_es": "En un hiperboloide circular MODELO (a = 1.80 m, c = 2.40 m), imagina que solo sobrevive una franja de 0.35 m del yeso tras el incendio de 1936 (z₁ = 0.20 m y z₂ = 0.55 m). Resolver r²(z) = a² + (a²/c²)·z² desde dos mediciones locales reconstruye la corona completa a 3.00 m; incluso con error opuesto de ±1.0 mm de calibrador, la ley reglada acota el desvío a ~43 mm frente a 311.6 mm en una curva libre de Taylor.",
    "verify_h_en": "Run the independent verifier yourself",
    "verify_h_es": "Ejecuta el verificador independiente",
    "verify_en": "The repository script skills/classics/cc02/verify_cc02_sagrada.py (beside SKILL.md) uses only the Python standard library. It independently recomputes hyperboloid rulings, Simpson catenary arc integrals, Boolean column cross-sections, PT wind decompression, and 1936 shard algebraic recovery—checking every value in EN and ES-MX HTML and failing across all five planted defects.",
    "verify_es": "El script skills/classics/cc02/verify_cc02_sagrada.py (junto a SKILL.md) usa solo la biblioteca estándar de Python. Recalcula de modo independiente rectas regladas, longitud de arco catenaria por Simpson, secciones estrelladas, descompresión por viento y recuperación algebraica desde fragmentos de 1936, verificando ambos idiomas y fallando ante cinco defectos plantados.",
}

SILENT = [
    {
        "q_en": "Did Antoni Gaudí leave complete signed engineering blueprints for every upper tower?",
        "q_es": "¿Dejó Antoni Gaudí planos de ingeniería completos y firmados para todas las torres superiores?",
        "a_en": "Not stated as complete blueprints: Gaudí relied far more on 3D scale models than floor plans, and the July 1936 Civil War fire destroyed drawings and photographs while smashing plaster casts; post-war directors reconstructed the geometry from surviving shards, published photos, and the ruled rules.",
        "a_es": "No existen planos completos: Gaudí confiaba más en maquetas espaciales 3D que en planos en planta, y el incendio de julio de 1936 destruyó dibujos y fotos rompiendo los yesos; sus sucesores reconstruyeron la geometría desde fragmentos sobrevivientes, fotografías publicadas y leyes regladas.",
    },
    {
        "q_en": "Are tendon forces, caliper errors, and column loads in Part VI measurements from the Basílica?",
        "q_es": "¿Son mediciones reales de obra las fuerzas de pretensado, errores de calibrador y cargas de la Parte VI?",
        "a_en": "No: detailed project calculations for specific post-tensioned joints, individual pier loads, and historical 1936 shard caliper logs are not published as full raw engineering tables in our cited sources, so every non-sourced input in Part VI is labeled MODEL.",
        "a_es": "No: las tablas de cálculo detallado por junta, carga axial específica o mediciones originales de cada fragmento de 1936 no se publican completas en las fuentes consultadas, por lo que toda entrada sin fuente en la Parte VI lleva la etiqueta MODELO.",
    },
    {
        "q_en": "Does the June 10, 2026 centenary inauguration finish the entire temple?",
        "q_es": "¿Concluye el templo entero tras la bendición del centenario el 10 de junio de 2026?",
        "a_en": "No: February 20, 2026 completed the exterior of the 172.5 m Tower of Jesus Christ and June 10 marks its blessing, while interior work on the upper cross continues in 2027–2028 and the southern Glory facade and grand staircase remain to be built.",
        "a_es": "No: el 20 de febrero de 2026 concluyó el exterior de la torre de Jesucristo (172.5 m) y el 10 de junio marca su bendición, pero el trabajo interior de la cruz sigue en 2027–2028 y la fachada sur de la Gloria con su escalinata aún queda pendiente.",
    },
]

CLOSING = [
    {
        "en": "Stand beneath the 45 m stone vaults on a clear morning when green light from the eastern windows touches red porphyry shafts, and look up 172.5 m past the Crossing Room bridges: you are looking at what ordinary human hands can accomplish across five generations when pride yields to shared geometry, humility before nature’s laws, and care for those who arrive a century later.",
        "es": "Ponte bajo las bóvedas de 45 m en una mañana despejada cuando la luz verde del oriente baña el pórfido rojo, y mira hacia lo alto hasta los 172.5 m: contemplas lo que manos humanas ordinarias alcanzan a lo largo de cinco generaciones cuando el orgullo cede ante una geometría compartida, la humildad frente a las leyes de la naturaleza y el cuidado por quienes llegarán un siglo después.",
    },
]

FOOTER_NOTE = {
    "en": "Independent educational monograph. Basílica dates, heights, and succession milestones are attributed to Basílica de la Sagrada Família; post-tensioned stone panel systems are attributed to Ingenia / Arup; all 15 peer-reviewed articles were checked in Crossref and Scite on 2026-11-15 with zero retractions. Values labeled MODEL illustrate mechanisms only and are not engineering calculations for construction.",
    "es": "Monografía educativa independiente. Fechas, alturas y relevos se atribuyen a Basílica de la Sagrada Família; la ingeniería de paneles pretensados a Ingenia / Arup; los 15 artículos arbitrados se verificaron en Crossref y Scite el 2026-11-15 sin retractaciones. Los valores marcados MODELO ilustran mecanismos únicamente y no constituyen cálculo ni dictamen de obra.",
}

BANNED = [
    "ordenador", "fichero", "vosotros", "miracle", "milagro", "unbreakable", "tallest possible",
]
