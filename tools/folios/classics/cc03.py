"""CC.03 · Wheels at the Corners — from 1959 Classic Mini to the F56 John Cooper Works Hot Chili (single source of truth).

Every factual claim on the page sits beside a source read on 2026-11-15:
- BMW Group Newsroom release (13 Nov 2024) & MINI USA JCW specification page (live HTTP 200).
- Official MINI CHALLENGE UK & Mini 7 Racing Club pages and lap-record tables (Brands Hatch Indy).
- Wikipedia articles for Classic Mini, Mini Hatch (R53/R56/F56/F66/J01), John Cooper Works, Alec Issigonis,
  John Cooper, Frank Stephenson, BMW B48, FMVSS 108, Horsepower (SAE vs DIN PS), and Brands Hatch.
- Five Wikimedia Commons archival photographs (CC BY 2.0 / CC BY 4.0 only — zero ShareAlike conflicts), resized
  and stripped of all EXIF/XMP/ICC/GPS metadata.
- Six peer-reviewed engineering papers verified in Crossref and Scite on 2026-11-15 (zero retractions); none of them
  tested a Mini, and the page says so beside every paper stamp.

Model inputs for the interactive benches live in tools/folios/classics/cc03_mechanics.py and are marked MODEL. Anything a
source does not state is written "not stated" and listed in SILENT.
"""
from __future__ import annotations

SLUG = "mini-jcw"
CODE = "CC.03"
DATE = "2026-11-15"
ACCESSED = "2026-11-15"

SEO = (
    "Wheels at the Corners: MINI to F56 John Cooper Works Hot Chili",
    "Five eras from the 1959 Mini to the F56 JCW Hot Chili and North America vs. Mexico/EU specs: "
    "transverse packaging, forced induction, Brands Hatch Indy records, and brake thermal mass.",
    "Ruedas en las esquinas: del Mini de 1959 al F56 JCW Hot Chili",
    "Cinco etapas del Mini de 1959 al F56 JCW Hot Chili y su equivalencia Norteamérica vs. México/UE: "
    "motor transversal, sobrealimentación, récords en Brands Hatch Indy y masa térmica de frenos.",
)

# ---------------------------------------------------------------------------------------------------------------
# Sources (29 total). "kind": mini (BMW/MINI Group & MINI USA), club (racing clubs / circuit),
# ref (encyclopedic / regulatory / biography), paper (Crossref + Scite verified 2026-11-15, zero retractions),
# photo (Wikimedia Commons CC BY 2.0 / CC BY 4.0).
# ---------------------------------------------------------------------------------------------------------------
SOURCES = {
    "wiki-mini": {
        "short": "Classic Mini record",
        "short_es": "Ficha Mini clásico",
        "kind": "ref",
        "label": "Wikipedia, “Mini” (1959–2000 ADO15 dimensions, Moulton rubber cones & Hydrolastic, Cooper 997 cc, Cooper S 970/1,071/1,275 cc, North America Austin/Morris 850, 5.38 million built)",
        "url": "https://en.wikipedia.org/wiki/Mini",
    },
    "wiki-hatch": {
        "short": "MINI Hatch record",
        "short_es": "Ficha MINI Hatch",
        "kind": "ref",
        "label": "Wikipedia, “Mini Hatch” (R50/R53, R56, F56, J01/F66 specifications, dimensions, US vs. EU lighting/lineup differences, LCI Union Jack rear lights, and GP editions)",
        "url": "https://en.wikipedia.org/wiki/Mini_Hatch",
    },
    "wiki-jcw": {
        "short": "JCW archive summary",
        "short_es": "Resumen JCW",
        "kind": "ref",
        "label": "Wikipedia, “John Cooper Works” (2002 founding by Michael Cooper, R53 200/210 bhp kits, R56 factory 155 kW JCW with 316 mm Brembo brakes, GP2 218 hp / 214 hp US & 8:23 lap)",
        "url": "https://en.wikipedia.org/wiki/John_Cooper_Works",
    },
    "bmw-jcw-2024": {
        "short": "BMW Group 2024",
        "short_es": "BMW Group 2024",
        "kind": "mini",
        "label": "BMW Group Newsroom, “Even more performance - even more choice: The new MINI John Cooper Works model family” (13 Nov 2024: F66 170 kW / 231 hp / 380 Nm DCT; J01 190 kW / 258 hp / 350 Nm)",
        "url": "https://newsroom.bmwgroup.com/emea/even-more-performance---even-more-choice-the-new-mini-john-cooper-works-model-family/",
    },
    "miniusa-jcw": {
        "short": "MINI USA JCW",
        "short_es": "MINI USA JCW",
        "kind": "mini",
        "label": "MINI USA, “The John Cooper Works Family” (US JCW 2 Door 228 hp / 280 lb-ft / 0–60 mph 5.9 s / 7-speed DCT; Pat Moss 1962 Tulip Rally; Luis A. Perocarpi 2008 LAP Motorsports MINI JCW Team)",
        "url": "https://www.miniusa.com/model/john-cooper-works.html",
    },
    "wiki-issigonis": {
        "short": "Alec Issigonis bio",
        "short_es": "Biografía Issigonis",
        "kind": "ref",
        "label": "Wikipedia, “Alec Issigonis” (1906–1988, 1956 Suez crisis XC/9003 -> ADO15 rapid engineering, 1969 Knight Bachelor)",
        "url": "https://en.wikipedia.org/wiki/Alec_Issigonis",
    },
    "wiki-cooper": {
        "short": "John Cooper bio",
        "short_es": "Biografía John Cooper",
        "kind": "ref",
        "label": "Wikipedia, “John Cooper (car maker)” (1923–2000, Cooper Car Company 1946 with Charles Cooper, Mini Cooper homologation)",
        "url": "https://en.wikipedia.org/wiki/John_Cooper_(car_maker)",
    },
    "wiki-stephenson": {
        "short": "Frank Stephenson bio",
        "short_es": "Biografía Stephenson",
        "kind": "ref",
        "label": "Wikipedia, “Frank Stephenson” (1959–, lead exterior designer of the 2001 R50/R53 MINI Hatch rebirth)",
        "url": "https://en.wikipedia.org/wiki/Frank_Stephenson",
    },
    "wiki-b48": {
        "short": "BMW B48 / B46",
        "short_es": "Motor BMW B48 / B46",
        "kind": "ref",
        "label": "Wikipedia, “BMW B48” (170 kW B48A20 JCW tune and US SULEV B46 emissions variant)",
        "url": "https://en.wikipedia.org/wiki/BMW_B48",
    },
    "wiki-fmvss108": {
        "short": "FMVSS 108 lighting",
        "short_es": "Norma FMVSS 108",
        "kind": "ref",
        "label": "Wikipedia, “Federal Motor Vehicle Safety Standard 108” (49 CFR 571.108 US lighting and side-marker rules from 1968 vs. UNECE type approval)",
        "url": "https://en.wikipedia.org/wiki/Federal_Motor_Vehicle_Safety_Standard_108",
    },
    "wiki-hp": {
        "short": "SAE hp vs DIN PS",
        "short_es": "hp SAE vs PS DIN",
        "kind": "ref",
        "label": "Wikipedia, “Horsepower” (mechanical/SAE 745.7 W vs. DIN 66036 metric PS 735.49875 W, explaining 170 kW -> 228 hp US vs. 231 PS metric)",
        "url": "https://en.wikipedia.org/wiki/Horsepower",
    },
    "mini7-club": {
        "short": "Mini 7 Racing Club",
        "short_es": "Mini 7 Racing Club",
        "kind": "club",
        "label": "Mini 7 Racing Club, class overview (1966 Brands Hatch Se7en debut, Se7en 998 cc, S-Class 1,293 cc, Miglia 1,293 cc slicks, Libre)",
        "url": "https://www.mini7.co.uk/",
    },
    "mini7-records": {
        "short": "Mini 7 lap records",
        "short_es": "Récords Mini 7",
        "kind": "club",
        "label": "Mini 7 Racing Club, “Lap Records” (Brands Hatch Indy 1.208 miles: Se7en S-Class, Se7en, Miglia, Libre)",
        "url": "https://www.mini7.co.uk/lap-records",
    },
    "mc-cooper-class": {
        "short": "MINI CHALLENGE Trophy",
        "short_es": "MINI CHALLENGE Trophy",
        "kind": "club",
        "label": "MINI CHALLENGE UK, “Trophy Class” specification (1.6 L naturally aspirated 130 bhp, 6-speed manual, ~1,110 kg)",
        "url": "https://www.minichallenge.co.uk/the-mini-challenge/cooper-class/",
    },
    "mc-cooper-records": {
        "short": "MC Cooper records",
        "short_es": "Récords MC Cooper",
        "kind": "club",
        "label": "MINI CHALLENGE Stats, “Cooper Lap Records” (Brands Hatch Indy qualifying 56.221 s and race 56.507 s)",
        "url": "https://www.minichallengestats.co.uk/lap-records/cooper/",
    },
    "mc-jcw-class": {
        "short": "MINI CHALLENGE JCW",
        "short_es": "MINI CHALLENGE JCW",
        "kind": "club",
        "label": "MINI CHALLENGE UK, “JCW Class” specification (Gen 3 F56 hatch, 2.0 L turbo 240–265 bhp, Quaife sequential/LSD, Alcon brakes, ~1,180 kg)",
        "url": "https://www.minichallenge.co.uk/the-mini-challenge/jcw-class/",
    },
    "mc-jcw-records": {
        "short": "MC JCW records",
        "short_es": "Récords MC JCW",
        "kind": "club",
        "label": "MINI CHALLENGE Stats, “JCW Lap Records” (Brands Hatch Indy qualifying 50.175 s and race 50.502 s)",
        "url": "https://www.minichallengestats.co.uk/lap-records/jcw/",
    },
    "brands-hatch": {
        "short": "Brands Hatch",
        "short_es": "Brands Hatch",
        "kind": "club",
        "label": "Wikipedia, “Brands Hatch” (Kent, England; 1.208 mi / 1.944 km Indy circuit opened 1950)",
        "url": "https://en.wikipedia.org/wiki/Brands_Hatch",
    },
    "hu2016": {
        "short": "Hu et al. 2016",
        "kind": "paper",
        "label": "Hu, Akehurst & Brace (2016). Novel approaches to improve the gas exchange process of downsized turbocharged spark-ignition engines: A review. International Journal of Engine Research 17(6), 595–618",
        "url": "https://doi.org/10.1177/1468087415599866",
    },
    "hu2017": {
        "short": "Hu et al. 2017",
        "kind": "paper",
        "label": "Hu, Turner, Akehurst, Brace & Copeland (2017). Observations on and potential trends for mechanically supercharging a downsized passenger car engine: a review. Proc. IMechE Part D 231(4), 435–456",
        "url": "https://doi.org/10.1177/0954407016636971",
    },
    "chiong2016": {
        "short": "Chiong et al. 2016",
        "kind": "paper",
        "label": "Chiong, Rajoo, Romagnoli, Costall & Martinez-Botas (2016). One-dimensional pulse-flow modeling of a twin-scroll turbine. Energy 115, 1291–1304",
        "url": "https://doi.org/10.1016/j.energy.2016.09.041",
    },
    "kakalis2008": {
        "short": "Kakalis et al. 2008",
        "kind": "paper",
        "label": "Kakalis, Zorzutti, Cheli & Travaglio (2008). Brake Based Torque Vectoring for Sport Vehicle Performance Improvement. SAE Int. J. Passeng. Cars – Mech. Syst. 1(1), 514–525",
        "url": "https://doi.org/10.4271/2008-01-0596",
    },
    "adamowicz2011": {
        "short": "Adamowicz & Grzes 2011",
        "kind": "paper",
        "label": "Adamowicz & Grzes (2011). Influence of convective cooling on a disc brake temperature distribution during repetitive braking. Applied Thermal Engineering 31(14–15), 2177–2185",
        "url": "https://doi.org/10.1016/j.applthermaleng.2011.05.016",
    },
    "ricco2020": {
        "short": "Ricco et al. 2020",
        "kind": "paper",
        "label": "Ricco, Zanchetta, Rizzo, Tavernini, Sorniotti & Chatzikomis (2020). On the Design of Yaw Rate Control via Variable Front-to-Total Anti-Roll Moment Distribution. IEEE Trans. Veh. Technol. 69(2), 1388–1403",
        "url": "https://doi.org/10.1109/tvt.2019.2955902",
    },
    "commons-1959-mini": {
        "short": "1959 Mini photo",
        "short_es": "Foto Mini 1959",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Morris Mini Minor (1959).jpg” (andreboeni, 10 Nov 2017; Creative Commons CC BY 2.0)",
        "url": "https://commons.wikimedia.org/wiki/File:Morris_Mini_Minor_(1959).jpg",
    },
    "commons-1964-33ejb": {
        "short": "1964 Monte Carlo 33 EJB",
        "short_es": "Montecarlo 1964 33 EJB",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:1963 Morris Mini Cooper S 1964 Monte Carlo Rally winner.jpg” (Tony Hisgett, 2 May 2018; Creative Commons CC BY 2.0)",
        "url": "https://commons.wikimedia.org/wiki/File:1963_Morris_Mini_Cooper_S_1964_Monte_Carlo_Rally_winner.jpg",
    },
    "commons-r53-usa": {
        "short": "US R53 Cooper S photo",
        "short_es": "Foto R53 EE. UU.",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Mini Cooper S (R53) Washington DC Metro Area, USA.jpg” (OWS Photography, 18 Jan 2025; Creative Commons CC BY 4.0)",
        "url": "https://commons.wikimedia.org/wiki/File:Mini_Cooper_S_(R53)_Washington_DC_Metro_Area,_USA.jpg",
    },
    "commons-r56-usa": {
        "short": "US R56 JCW photo",
        "short_es": "Foto R56 JCW EE. UU.",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Mini Cooper Hatch JCW (R56) Washington DC Metro Area, USA.jpg” (OWS Photography, 18 Jan 2025; Creative Commons CC BY 4.0)",
        "url": "https://commons.wikimedia.org/wiki/File:Mini_Cooper_Hatch_JCW_(R56)_Washington_DC_Metro_Area,_USA.jpg",
    },
    "commons-2022-brands": {
        "short": "Brands Hatch JCW photo",
        "short_es": "Foto JCW Brands Hatch",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Mini Challenge UK Cars Brands Hatch 2022.jpg” (BWard 1997, 9 Oct 2022; Creative Commons CC BY 4.0)",
        "url": "https://commons.wikimedia.org/wiki/File:Mini_Challenge_UK_Cars_Brands_Hatch_2022.jpg",
    },
}

KIND_LABEL = {
    "mini": ("BMW/MINI", "BMW/MINI"),
    "club": ("Club/Track", "Club/Pista"),
    "ref": ("Record", "Ficha"),
    "paper": ("Paper", "Artículo"),
    "photo": ("Photo Archive", "Archivo Fotográfico"),
}

HERO = {
    "kicker_en": "Cult Classics · CC.03 · Applied Mechanics",
    "kicker_es": "Clásicos de culto · CC.03 · Mecánica aplicada",
    "title_en": "Wheels at the Corners",
    "title_es": "Ruedas en las esquinas",
    "dek_en": "From the 1959 transverse blueprint to the F56 John Cooper Works Hot Chili and North American lineup, told one engineering move at a time.",
    "dek_es": "Del plano transversal de 1959 al F56 John Cooper Works Hot Chili y su llegada a Norteamérica, contado paso de ingeniería por paso.",
    "reading_en": "16 min read",
    "reading_es": "18 min de lectura",
}

BRIEF_NOTE = {
    "en": "The thesis in the title comes from Sir Alec Issigonis’s 1959 packaging constraint: push a wheel to each corner and "
          "mount the four-cylinder sideways over its own gearbox. Every era since—and both sides of the US–Mexico North American "
          "market—adapted that compact front-drive stance to stricter emissions, crash rules, and track heat.",
    "es": "La tesis del título nace de una restricción geométrica de 1959 ideada por sir Alec Issigonis: empujar una rueda a cada "
          "esquina y montar el cuatro cilindros transversal sobre su propia caja. Cada etapa posterior—y ambos lados del mercado "
          "norteamericano entre Estados Unidos y México—adaptó esa postura delantera a nuevas normas de emisiones, choque y calor en pista.",
}

HERO_TRIBUTE = {
    "kicker_en": "In Honor of the Engineers, Designers, Drivers & Builders (1959–2026)",
    "kicker_es": "En honor a quienes lo diseñaron, armaron y llevaron a pista (1959–2026)",
    "chassis_label_en": "Chassis & Design Pioneers",
    "chassis_label_es": "Pioneros de chasis y diseño",
    "chassis_en": "Sir Alec Issigonis (ADO15 packaging & transverse powertrain, 1957–1959), Alex Moulton (rubber-cone and Hydrolastic suspension), Longbridge drawing-office & prototype crews, and Frank Stephenson (2001 R50/R53 MINI Hatch exterior rebirth).",
    "chassis_es": "Sir Alec Issigonis (empaque ADO15 y tren motriz transversal, 1957–1959), Alex Moulton (suspensión por conos de hule e Hydrolastic), el taller de prototipos de Longbridge y Frank Stephenson (renacimiento exterior del MINI R50/R53 en 2001).",
    "sport_label_en": "Cooper, Rally & Track Crew",
    "sport_label_es": "Cooper, rally y equipos de pista",
    "sport_en": "Charles & John Cooper (Cooper Car Company, 1946; 1961 Mini Cooper homologation), Michael Cooper (John Cooper Works founder, 2002), Stuart Turner (BMC Abingdon competitions), Pat Moss & Ann Wisdom (1962 Tulip Rally first international Mini win), Paddy Hopkirk, Timo Mäkinen & Rauno Aaltonen (1964/1965/1967 Monte Carlo winners), and Luis A. Perocarpi (LAP Motorsports North American MINI JCW Team).",
    "sport_es": "Charles y John Cooper (Cooper Car Company, 1946; homologación Mini Cooper 1961), Michael Cooper (fundador de John Cooper Works, 2002), Stuart Turner (BMC Abingdon), Pat Moss y Ann Wisdom (primera victoria internacional del Mini en el Tulip Rally 1962), Paddy Hopkirk, Timo Mäkinen y Rauno Aaltonen (Montecarlo 1964/1965/1967) y Luis A. Perocarpi (equipo MINI JCW Team Norteamérica).",
    "works_label_en": "Plant & Club Lineage",
    "works_label_es": "Plantas y clubes de pista",
    "works_en": "Craftspeople across Longbridge, Plant Oxford (Cowley), and VDL Nedcar (Born), plus grassroots competitors of the Mini 7 Racing Club (since 1966) and MINI CHALLENGE.",
    "works_es": "Los equipos de ensamble en Longbridge, Planta Oxford (Cowley) y VDL Nedcar (Born), junto a los competidores del Mini 7 Racing Club (desde 1966) y MINI CHALLENGE.",
    "src": ["wiki-issigonis", "wiki-cooper", "wiki-mini", "wiki-stephenson", "wiki-jcw", "miniusa-jcw", "mini7-club", "mc-jcw-class"],
}

OPENING = [
    {
        "en": "In 1959 the British Motor Corporation launched a 3.05-meter saloon engineered by Alec Issigonis and Alex Moulton with a "
              "transverse engine sitting directly over an integrated-sump transmission. That layout left 80% of the floorpan area "
              "free for four adults and luggage. Formula One constructor John Cooper saw something else in the 2,036 mm wheelbase "
              "and 580–686 kg shell: a chassis with minimal body roll that kept momentum through tight bends.",
        "es": "En 1959 la British Motor Corporation presentó un sedán de 3.05 metros diseñado por Alec Issigonis y Alex Moulton con el "
              "motor transversal montado directamente sobre una transmisión en el mismo cárter. Ese arreglo dejó 80 % del piso para "
              "cuatro adultos y equipaje. El constructor de Fórmula 1 John Cooper vio otra ventaja en la batalla de 2,036 mm "
              "y los 580–686 kg: un chasis con mínima inclinación que conservaba velocidad en curvas cerradas.",
        "src": ["wiki-mini", "wiki-issigonis", "wiki-cooper"],
    },
    {
        "en": "Cooper pressed BMC management to commission 1,000 homologation units of a tuned 997 cc car in 1961, adding "
              "twin SU carburetors and front disc brakes when small saloons still ran drums. Between 1959 and 2000 roughly "
              "5.38 million classic Minis left the line, and when BMW took the marque forward at Plant Oxford in 2001, the "
              "John Cooper Works name grew from a dealer pulley kit into the factory F56 B48 flagship featured under "
              "the clamshell bonnet below.",
        "es": "Cooper convenció a la directiva de BMC de aprobar 1,000 unidades de homologación de un 997 cc preparado en "
              "1961, sumando dos carburadores SU y frenos delanteros de disco cuando los compactos aún llevaban tambor. "
              "Entre 1959 y 2000 se fabricaron unos 5.38 millones de Mini clásicos, y cuando BMW retomó la marca en la "
              "planta de Oxford en 2001, el nombre John Cooper Works pasó de un kit de polea en agencia al modelo de "
              "fábrica F56 B48 que vive bajo el cofre de almeja de esta página.",
        "src": ["wiki-mini", "wiki-jcw"],
    },
]

# One card per generation. "plate" rows are (label_en, label_es, value, source key).
CARDS = [
    {
        "id": "ado15", "gen": "ADO15", "years": "1959–2000 · Cooper & S",
        "move_en": "Transverse sump packaging, rubber cones, front discs",
        "move_es": "Motor transversal sobre el cárter, conos de hule y discos delanteros",
        "body_en": "Every millimeter of the classic Mini obeyed packaging geometry: 3,054 mm overall length, 2,036 mm wheelbase, "
                   "1,410 mm width and 10-inch wheels so arches never stole cabin footwell. Pat Moss and Ann Wisdom scored "
                   "the car’s first international rally victory at the 1962 Tulip Rally before the 1963 Cooper S brought nitrided "
                   "crankshafts in 1,071 cc, 970 cc and 1,275 cc forms for 1964, 1965 and 1967 Monte Carlo wins; early exports "
                   "reached the US and Canada as the Austin and Morris 850.",
        "body_es": "Cada milímetro del Mini clásico obedecía a la geometría del empaque: 3,054 mm de largo total, "
                   "2,036 mm de distancia entre ejes, 1,410 mm de ancho y rines de 10 pulgadas para no robar espacio a los "
                   "pies. Pat Moss y Ann Wisdom lograron su primera victoria internacional en el Tulip Rally de 1962 antes "
                   "de que el Cooper S sumara cigüeñal nitrurado en 1,071 cc, 970 cc y 1,275 cc para ganar Montecarlo en "
                   "1964, 1965 y 1967; las primeras exportaciones llegaron a Estados Unidos como Austin y Morris 850.",
        "plate": [
            ("Footprint", "Huella", "3,054 mm length · 2,036 mm wheelbase", "wiki-mini"),
            ("Kerb weight range", "Peso en vacío", "580–686 kg", "wiki-mini"),
            ("1961 Mini Cooper", "Mini Cooper 1961", "997 cc, 55 bhp, front discs", "wiki-mini"),
            ("Cooper S bores", "Cilindradas Cooper S", "970 · 1,071 · 1,275 cc", "wiki-mini"),
        ],
        "photo": "photo-1959-mini",
    },
    {
        "id": "r53", "gen": "R53", "years": "2001–2006 · Supercharged",
        "move_en": "Oxford rebirth, crank-driven supercharger, JCW pulley kits",
        "move_es": "Renacer en Oxford, supercargador al cigüeñal y kits de polea JCW",
        "body_en": "BMW moved assembly to Plant Oxford and built Frank Stephenson’s 2001 Cooper S (R53) around a 1.6-liter Tritec "
                   "engine with a Roots supercharger, six-speed Getrag manual and central exhaust—pushing the battery under the "
                   "boot floor. In North America (both the US and Mexico), the supercharged Hardtop 2 Door set the core "
                   "JCW dealer-kit template: an 11% smaller pulley and head work to 200 bhp in 2003, 210 bhp with 380 cc/min "
                   "injectors in 2004, and 444 US-bound cars among the 2,000-unit 2006 GP Kit (218 PS, −40 kg).",
        "body_es": "BMW trasladó el ensamble a Planta Oxford y construyó el Cooper S (R53) dibujado por Frank Stephenson "
                   "con un 1.6 litros Tritec supercargado, caja Getrag manual de seis cambios y escape central, enviando la "
                   "batería bajo la cajuela. Tanto en Estados Unidos como en México, el modelo fijó la receta inicial de JCW: "
                   "polea 11 % menor para dar 200 bhp en 2003, 210 bhp con inyectores de 380 cc/min en 2004 y 444 unidades "
                   "norteamericanas dentro de las 2,000 del GP Kit 2006 (218 PS, −40 kg).",
        "plate": [
            ("Dimensions", "Dimensiones", "3,655 mm Cooper S · 2,466 mm wheelbase", "wiki-hatch"),
            ("JCW 200 / 210 kits", "Kits JCW 200 / 210", "11% smaller pulley · 380 cc/min injectors", "wiki-jcw"),
            ("2006 JCW GP Kit", "JCW GP Kit 2006", "218 PS · 250 Nm · ~40 kg lighter (2,000 built)", "wiki-hatch"),
        ],
        "photo": "photo-r53-usa",
    },
    {
        "id": "r56", "gen": "R56", "years": "2006–2013 · Twin-scroll",
        "move_en": "Exhaust-pulse turbocharging, fixed headlamps, factory JCW",
        "move_es": "Turbo twin-scroll, faros fijos en salpicadera y JCW de fábrica",
        "body_en": "Pedestrian-impact rules and efficiency shifted the second generation (R56) onto a 1.6-liter turbo engine "
                   "with fixed headlamps mounted inside the wings rather than rising inside the clamshell bonnet. In mid-2008 "
                   "BMW brought John Cooper Works in-house as a full factory build: 155 kW (208 bhp), 260 Nm (280 Nm on "
                   "overboost), 316 × 22 mm perforated front discs under red four-piston Brembo calipers, Dynamic Traction "
                   "Control and brake-based EDLC. The 2013 GP2 made 218 hp (214 hp US spec) and lapped the Nürburgring in 8:23.",
        "body_es": "Las normas de impacto peatonal y eficiencia llevaron la segunda generación (R56) a un 1.6 litros turbo "
                   "con faros fijos en salpicaderas en vez de integrarse al cofre móvil. En 2008, BMW integró John Cooper Works "
                   "como modelo completo de fábrica: 155 kW (208 bhp), 260 Nm (280 Nm en overboost), discos ventilados de "
                   "316 × 22 mm con cáliper Brembo de cuatro pistones, DTC y EDLC por freno. El GP2 de 2013 entregó 218 hp "
                   "(214 hp en especificación estadounidense) y giró en 8:23 en Nürburgring.",
        "plate": [
            ("Factory JCW (2008)", "JCW de fábrica (2008)", "1.6 L turbo · 155 kW (208 bhp) · 260/280 Nm", "wiki-jcw"),
            ("Factory JCW brakes", "Frenos JCW de fábrica", "316 × 22 mm front · 4-piston Brembo", "wiki-jcw"),
            ("2013 JCW GP2", "JCW GP2 2013", "218 hp (214 hp US) · 8:23 Nordschleife (2,000 built)", "wiki-jcw"),
        ],
        "photo": "photo-r56-usa",
    },
    {
        "id": "f56", "gen": "F56", "years": "2014–2024 · JCW Hot Chili",
        "move_en": "2.0 L B48 four-cylinder, widened track, cooling over fog lamps",
        "move_es": "Cuatro cilindros 2.0 L B48, vías más anchas y ductos en lugar de niebla",
        "body_en": "Riding on BMW’s UKL front-drive platform, the F56 grew 98 mm in length, 28 mm in wheelbase "
                   "(2,495 mm) and +42 mm in front track (+34 mm rear) over the R56. Its 1,998 cc B48A20 TwinPower Turbo engine "
                   "delivers the same 170 kW in North America and Europe—printed as 228 hp / 236 lb-ft in US sheets and "
                   "231 PS / 320 Nm in Mexican and European sheets—paired with four-piston red calipers and front cooling ducts "
                   "replacing fog lamps. In Mexico, the top-tier Hot Chili package carries LCI Union Jack tail lamps without US "
                   "arch reflectors; in 2020 the GP3 rose to 225 kW (306 PS) and 450 Nm.",
        "body_es": "Sobre la plataforma UKL de tracción delantera, el F56 creció 98 mm de largo, 28 mm de batalla (2,495 mm) "
                   "y +42 mm de vía delantera (+34 mm atrás) frente al R56. Su motor B48A20 de 1,998 cc entrega exactamente los "
                   "mismos 170 kW en Norteamérica y Europa—publicados como 228 hp / 236 lb-ft en EE. UU. y 231 PS / 320 Nm en "
                   "México y Europa—con cáliper rojos de cuatro pistones y ductos de aire en vez de niebla. En México, la "
                   "especificación tope Hot Chili suma calaveras Union Jack sin reflejantes laterales de arco; en 2020 el GP3 "
                   "subió a 225 kW (306 PS) y 450 Nm.",
        "plate": [
            ("Platform & stance", "Plataforma y vías", "BMW UKL · 2,495 mm wheelbase · +42/+34 mm track", "wiki-hatch"),
            ("F56 JCW (B48A20)", "F56 JCW (B48A20)", "1,998 cc · 170 kW (228 hp US / 231 PS) · 320 Nm (236 lb-ft)", "wiki-b48"),
            ("0–100 km/h & weight", "0–100 km/h y peso", "6.3 s manual / 6.1 s auto · 1,205 / 1,220 kg", "wiki-hatch"),
            ("LCI-1 & LCI-2 updates", "Actualizaciones LCI-1 y LCI-2", "2018 8-speed auto · Union Jack rear lights", "wiki-hatch"),
            ("2020 JCW GP3", "JCW GP3 2020", "225 kW (306 PS) · 450 Nm · 5.2 s (3,000 built)", "wiki-hatch"),
        ],
        "egg": True,
    },
    {
        "id": "f66", "gen": "F66/J01", "years": "2024– · Two paths",
        "move_en": "380 Nm petrol dual-clutch alongside 258 hp electric torque",
        "move_es": "Doble embrague de gasolina con 380 Nm junto a 258 hp eléctricos",
        "body_en": "In November 2024, MINI split the fourth generation across two factories and regulations. The Oxford-built F66 "
                   "petrol JCW (sold across Europe, Mexico, and MINI USA at 228 hp / 280 lb-ft, 0–60 mph in 5.9 s and 155 mph) "
                   "raises B48 torque to 380 Nm through a 7-speed DCT (no manual), reaching 0–100 km/h in 6.1 s and 250 km/h. "
                   "Alongside it in Mexico and Europe sits the China-built J01 JCW Electric (190 kW / 258 hp, 350 Nm, 5.9 s), "
                   "which is not imported by MINI USA.",
        "body_es": "En noviembre de 2024, MINI dividió la cuarta generación entre dos plantas y mercados. El F66 JCW de gasolina "
                   "armado en Oxford (comercializado en Europa, México y MINI USA con 228 hp / 280 lb-ft, 0–60 mph en 5.9 s y "
                   "155 mph) eleva el par del B48 a 380 Nm con doble embrague de 7 velocidades (sin caja manual) y logra 0–100 km/h "
                   "en 6.1 s y 250 km/h. Junto a él en México y Europa vive el J01 JCW eléctrico armado en China (190 kW / "
                   "258 hp, 350 Nm, 5.9 s), ausente del catálogo de MINI USA.",
        "plate": [
            ("F66 petrol JCW", "F66 JCW gasolina", "2.0 L turbo · 170 kW (228 hp US / 231 PS) · 380 Nm (280 lb-ft) · DCT", "bmw-jcw-2024"),
            ("F66 NA & metric sprint", "F66 sprint y máxima", "0–60 mph 5.9 s (US) · 0–100 km/h 6.1 s · 250 km/h", "miniusa-jcw"),
            ("J01 JCW Electric (MX/EU)", "J01 JCW Eléctrico (MX/UE)", "190 kW (258 hp) · 350 Nm · 5.9 s · 54.2 kWh", "bmw-jcw-2024"),
        ],
    },
]

# Spanish for spec-plate values that are not language-neutral.
VALUE_ES = {
    "3,054 mm length · 2,036 mm wheelbase": "3,054 mm de largo · 2,036 mm de batalla",
    "997 cc, 55 bhp, front discs": "997 cc, 55 bhp, discos delanteros",
    "3,655 mm Cooper S · 2,466 mm wheelbase": "3,655 mm Cooper S · 2,466 mm de batalla",
    "11% smaller pulley · 380 cc/min injectors": "polea 11 % menor · inyectores 380 cc/min",
    "218 PS · 250 Nm · ~40 kg lighter (2,000 built)": "218 PS · 250 Nm · ~40 kg menos (2,000 uds.)",
    "1.6 L turbo · 155 kW (208 bhp) · 260/280 Nm": "1.6 L turbo · 155 kW (208 bhp) · 260/280 Nm",
    "316 × 22 mm front · 4-piston Brembo": "316 × 22 mm adelante · Brembo 4 pistones",
    "218 hp (214 hp US) · 8:23 Nordschleife (2,000 built)": "218 hp (214 hp EE. UU.) · 8:23 Nordschleife (2,000 uds.)",
    "BMW UKL · 2,495 mm wheelbase · +42/+34 mm track": "BMW UKL · batalla 2,495 mm · vía +42/+34 mm",
    "1,998 cc · 170 kW (228 hp US / 231 PS) · 320 Nm (236 lb-ft)": "1,998 cc · 170 kW (228 hp EE. UU. / 231 PS) · 320 Nm (236 lb-ft)",
    "6.3 s manual / 6.1 s auto · 1,205 / 1,220 kg": "6.3 s manual / 6.1 s auto · 1,205 / 1,220 kg",
    "2018 8-speed auto · Union Jack rear lights": "2018 auto 8 vel. · calaveras Union Jack",
    "225 kW (306 PS) · 450 Nm · 5.2 s (3,000 built)": "225 kW (306 PS) · 450 Nm · 5.2 s (3,000 uds.)",
    "2.0 L turbo · 170 kW (228 hp US / 231 PS) · 380 Nm (280 lb-ft) · DCT": "2.0 L turbo · 170 kW (228 hp EE. UU. / 231 PS) · 380 Nm (280 lb-ft) · DCT",
    "0–60 mph 5.9 s (US) · 0–100 km/h 6.1 s · 250 km/h": "0–60 mph 5.9 s (EE. UU.) · 0–100 km/h 6.1 s · 250 km/h",
}

PARTS = [
    {
        "id": "part-1", "numeral": "I", "years": "1959–2000",
        "title_en": "Packaging", "title_es": "Empaquetado",
        "opener": [
            {
                "en": "The classic Mini solved a dimension constraint before anyone spoke about handling. Turning the A-series "
                      "four-cylinder sideways over its sump transmission cut the engine bay down enough to place a 2,036 mm "
                      "wheelbase inside a 3,054 mm body—two-thirds of the car sitting between the axles.",
                "es": "El Mini clásico resolvió primero una restricción geométrica. Girar el motor A-series de cuatro cilindros "
                      "en sentido transversal sobre una caja alojada en el cárter acortó el cofre lo suficiente para meter "
                      "2,036 mm de batalla en 3,054 mm de largo total: dos terceras partes del auto quedaban entre los ejes.",
                "src": ["wiki-mini"],
            },
            {
                "en": "When John Cooper pushed BMC to homologate the 1961 Mini Cooper, he paired that wide wheelbase-to-length "
                      "stance with front disc brakes and a longer-stroke 997 cc engine. In the Brands Hatch section below, a "
                      "modern 998 cc Mini Se7en built to that classic silhouette still posts laps inside 59 seconds around "
                      "Paddock Hill Bend.",
                "es": "Cuando John Cooper impulsó la homologación del Mini Cooper de 1961, sumó frenos delanteros de disco "
                      "y un motor 997 cc a esa relación entre batalla y longitud. En la sección de Brands Hatch más abajo, un "
                      "Mini Se7en de 998 cc de esa silueta clásica sigue marcando vueltas por debajo de 59 segundos pasando "
                      "Paddock Hill Bend.",
                "src": ["wiki-mini", "mini7-club", "mini7-records"],
            },
        ],
        "pull_en": "Two-thirds of the car’s length sat between its axles—the layout came first, the cornering followed.",
        "pull_es": "Dos terceras partes del largo total vivían entre ejes: primero nació el arreglo, luego el paso por curva.",
        "cards": ["ado15"],
        "interlude": "ado15-details",
    },
    {
        "id": "part-2", "numeral": "II", "years": "2001–2013",
        "title_en": "Forced Induction", "title_es": "Sobrealimentación",
        "opener": [
            {
                "en": "Across two generations in twelve years, BMW-built MINIs ran both halves of the forced-induction textbook. "
                      "The R53 Cooper S bolted a crank-driven Roots supercharger onto a 1.6-liter Tritec block, forcing the "
                      "battery under the boot floor; six years later the R56 switched to a twin-scroll exhaust turbocharger.",
                "es": "En dos generaciones y doce años, los MINI de la era BMW recorrieron las dos mitades del libro de "
                      "sobrealimentación. El R53 Cooper S montó un supercargador Roots arrastrado por el cigüeñal en el 1.6 "
                      "Tritec—obligando a mandar la batería bajo la cajuela—; seis años después, el R56 pasó a un turbo "
                      "twin-scroll movido por el escape.",
                "src": ["wiki-hatch", "wiki-jcw"],
            },
            {
                "en": "Why swap a supercharger for a twin-scroll turbo? Two independent engine studies explain the trade in "
                      "general spark-ignition engines (neither tested a Mini): mechanical supercharging tracks the crankshaft "
                      "without delay but consumes shaft work at part load, while twin-scroll turbines pair cylinders whose exhaust "
                      "blowdown pulses stay separated by 360 crank degrees, preserving pulse energy and spooling faster than a "
                      "single-entry volute.",
                "es": "¿Por qué cambiar un supercargador por un turbo twin-scroll? Dos estudios independientes de motores de "
                      "encendido por chispa explican el compromiso general (ninguno probó un Mini): el compresor mecánico "
                      "responde directo al cigüeñal sin demora pero consume trabajo del eje en carga parcial, mientras que la "
                      "turbina de doble entrada separa en dos ductos los pulsos de escape desfasados 360 grados de cigüeñal, "
                      "evitando interferencias y acelerando el giro del rotor respecto a una caracola simple.",
                "src": ["hu2016", "hu2017", "chiong2016"],
            },
        ],
        "pull_en": "Crank-driven immediacy on the R53 gave way to separated exhaust pulses on the R56.",
        "pull_es": "La respuesta directa del cigüeñal en el R53 cedió el paso a los pulsos separados del R56.",
        "cards": ["r53", "r56"],
        "interlude": "induction",
    },
    {
        "id": "part-3", "numeral": "III", "years": "2014–2024",
        "title_en": "Track, Displacement & North America", "title_es": "Ancho de vía, cilindrada y Norteamérica",
        "opener": [
            {
                "en": "Moving the third-generation F56 onto BMW’s UKL front-drive architecture broke the 1.6-liter ceiling and "
                      "widened the footprint: +42 mm front track, +34 mm rear track and a 2,495 mm wheelbase. For the John "
                      "Cooper Works flagship, the 1,998 cc B48A20 delivered 170 kW (231 PS / 228 hp SAE) and 320 Nm (236 lb-ft), "
                      "combining broader low-rev torque with physical room for larger front brake rotors.",
                "es": "Pasar la tercera generación F56 a la arquitectura UKL de tracción delantera rompió el techo de 1.6 litros "
                      "y ensanchó la pisada: +42 mm adelante, +34 mm atrás y 2,495 mm de batalla. En el John Cooper Works, "
                      "el B48A20 de 1,998 cc entregó 170 kW (231 PS / 228 hp SAE) y 320 Nm (236 lb-ft), ampliando el par desde "
                      "bajas rpm y abriendo espacio físico para rotores delanteros más grandes.",
                "src": ["wiki-hatch", "wiki-b48"],
            },
            {
                "en": "Extra nose cooling matters on a short circuit like Brands Hatch Indy, and North America adds its own "
                      "engineering twist: US and Mexican F56 JCW hatches usually share the same Oxford mechanicals, yet lighting "
                      "laws (FMVSS 108 vs. UNECE), unit conventions (228 hp vs. 231 PS), top trim names (Iconic vs. Hot Chili), "
                      "and 2024 J01 availability set them cleanly apart.",
                "es": "Ese flujo frontal importa en un circuito corto como Brands Hatch Indy, y Norteamérica suma su propio "
                      "matiz técnico: en EE. UU. y México los F56 JCW suelen compartir mecánica de Oxford, pero normas de luces "
                      "(FMVSS 108 vs. UNECE), unidades (228 hp vs. 231 PS), nombres de versión (Iconic vs. Hot Chili) y la oferta "
                      "2024 del eléctrico J01 los distinguen con claridad.",
                "src": ["wiki-hatch", "mc-jcw-class", "wiki-fmvss108", "wiki-hp"],
            },
        ],
        "pull_en": "Same 170 kW engine across continents—printed as 228 hp US or 231 PS in Mexico depending on test unit.",
        "pull_es": "Mismo motor de 170 kW en ambos lados: se publica como 228 hp en EE. UU. o 231 PS en México según la unidad.",
        "cards": ["f56"],
        "interlude": "f56-anatomy",
    },
    {
        "id": "part-4", "numeral": "IV", "years": "2024–",
        "title_en": "Two Architectures", "title_es": "Dos arquitecturas",
        "opener": [
            {
                "en": "Rather than force electric batteries and a two-liter turbo onto one floorpan, MINI split the fourth "
                      "generation in November 2024. The Oxford-built petrol F66 JCW pushes B48 torque from 320 Nm to 380 Nm "
                      "(280 lb-ft in US sheets) through a dual-clutch transmission, while the J01 JCW Electric pairs 190 kW "
                      "(258 hp) and 350 Nm of instant pull with a 20 kW boost function—available in Mexico and Europe but not the US.",
                "es": "En lugar de forzar baterías y un dos litros turbo sobre un mismo piso, MINI dividió la cuarta "
                      "generación en noviembre de 2024. El F66 JCW de gasolina ensamblado en Oxford sube el par de 320 Nm a "
                      "380 Nm (280 lb-ft en ficha EE. UU.) con doble embrague, mientras que el J01 JCW eléctrico entrega 190 kW "
                      "(258 hp) y 350 Nm con impulso extra de 20 kW—disponible en México y Europa pero no en Estados Unidos.",
                "src": ["bmw-jcw-2024", "miniusa-jcw", "wiki-hatch"],
            },
            {
                "en": "Both architectures still share the front-drive cornering limit born in 1959: two front tires asked "
                      "to steer and pull simultaneously, governed by axle lateral load transfer and brake-based yaw "
                      "stabilization.",
                "es": "Ambas arquitecturas siguen compartiendo el límite frontal nacido en 1959: dos llantas delanteras "
                      "encargadas de girar y traccionar a la vez, gobernadas por la transferencia lateral de carga y la "
                      "estabilización de guiñada con los frenos.",
                "src": ["bmw-jcw-2024", "kakalis2008"],
            },
        ],
        "pull_en": "Same front-drive physics from 1959—answered now by 380 Nm combustion and 258 hp electric drive.",
        "pull_es": "La misma física frontal desde 1959—respondida hoy por 380 Nm a combustión y 258 hp eléctricos.",
        "cards": ["f66"],
        "interlude": "",
    },
]

ADO15_DETAILS = {
    "title_en": "The 1959–1967 architectural ledger",
    "title_es": "El registro de arquitectura 1959–1967",
    "items": [
        ("Transverse A-series I4 mounted above an integrated gearbox sharing engine oil.", "Motor A-series transversal de 4 cilindros montado sobre una caja integrada al mismo aceite."),
        ("Wheelbase 2,036 mm inside 3,054 mm overall length (66.7% of total length).", "Distancia entre ejes de 2,036 mm dentro de 3,054 mm totales (66.7 % del largo)."),
        ("1961 Mini Cooper: 1,000 Group 2 homologation units, 997 cc, twin SU carburetors, front discs.", "Mini Cooper 1961: 1,000 unidades de homologación Grupo 2, 997 cc, doble SU y discos delanteros."),
        ("1963 Cooper S: nitrided steel crankshaft in 1,071 cc (4,030 built), 970 cc (963 built) and 1,275 cc.", "Cooper S 1963: cigüeñal nitrurado en 1,071 cc (4,030 uds.), 970 cc (963 uds.) y 1,275 cc."),
        ("International rally breakthroughs: 1962 Tulip Rally (Pat Moss / Ann Wisdom) and overall Monte Carlo victories in 1964 (Paddy Hopkirk), 1965 (Timo Mäkinen) and 1967 (Rauno Aaltonen).", "Hitos internacionales en rally: Tulip Rally 1962 (Pat Moss / Ann Wisdom) y victorias absolutas en Montecarlo en 1964 (Paddy Hopkirk), 1965 (Timo Mäkinen) y 1967 (Rauno Aaltonen)."),
    ],
    "photo": "photo-1964-33ejb",
    "src": ["wiki-mini", "miniusa-jcw"],
}

INDUCTION = {
    "title_en": "Three ways to pack air into a small front bay",
    "title_es": "Tres formas de meter más aire en un cofre compacto",
    "head_en": ("", "Supercharger (R53)", "Twin-scroll turbo (R56)", "2.0 L Twin-scroll B48 (F56/F66)"),
    "head_es": ("", "Supercargador (R53)", "Turbo twin-scroll (R56)", "2.0 L Twin-scroll B48 (F56/F66)"),
    "rows": [
        ("Driven by", "Movido por", "crankshaft belt", "banda al cigüeñal", "paired exhaust pulses", "pulsos de escape en dos ductos", "paired exhaust pulses + direct injection", "pulsos separados + inyección directa"),
        ("Throttle character", "Respuesta al pedal", "immediate mechanical boost", "empuje mecánico inmediato", "pulse energy cuts lag vs mono-scroll", "pulsos reducen retraso vs caracola simple", "peak torque from 1,250–1,450 rpm", "par máximo desde 1,250–1,450 rpm"),
        ("Packaging & cost", "Costo y empaque", "consumes shaft power; battery moved to boot", "consume trabajo del eje; batería en cajuela", "exhaust heat load in tight nose", "carga térmica en escape compacto", "larger displacement needs dedicated cooling ducts", "mayor cilindrada exige ductos frontales dedicados"),
        ("In MINI JCW history", "En el linaje JCW", "200 / 210 bhp kits; 2006 GP 218 PS", "Kits 200 / 210 bhp; GP 2006 218 PS", "2008 factory JCW 208 bhp; 2013 GP2 218 hp", "JCW fábrica 2008 208 bhp; GP2 2013 218 hp", "F56 231 PS / 320 Nm; GP3 306 PS; F66 380 Nm", "F56 231 PS / 320 Nm; GP3 306 PS; F66 380 Nm"),
    ],
    "note_en": "Mechanisms summarized from three peer-reviewed engine studies (Hu et al. 2016; Hu et al. 2017; Chiong et al. 2016). None of those papers tested a Mini.",
    "note_es": "Mecanismos resumidos de tres estudios arbitrados sobre motores (Hu et al. 2016; Hu et al. 2017; Chiong et al. 2016). Ninguno probó un Mini.",
    "src": ["hu2016", "hu2017", "chiong2016", "wiki-hatch", "wiki-jcw", "bmw-jcw-2024"],
}

F56_ANATOMY = {
    "title_en": "From road Hot Chili to MINI CHALLENGE UK F56 JCW",
    "title_es": "Del Hot Chili de calle al F56 JCW de la MINI CHALLENGE británica",
    "items": [
        ("Road engine (F56 JCW)", "Motor de calle (F56 JCW)",
         "BMW B48A20 1,998 cc inline-four TwinPower Turbo: 170 kW (231 PS / 228 hp SAE) and 320 Nm (236 lb-ft); 6-speed manual or 8-speed Steptronic auto from 2018 LCI.",
         "BMW B48A20 de 1,998 cc TwinPower Turbo: 170 kW (231 PS / 228 hp SAE) y 320 Nm (236 lb-ft); manual de 6 vel. o Steptronic de 8 vel. desde LCI 2018."),
        ("Track-spec JCW Class engine", "Motor categoría JCW de pista",
         "Same Gen 3 F56 2.0-liter platform tuned with Owen Developments turbo and championship ECU to 240–265 bhp.",
         "Misma base Gen 3 F56 2.0 litros con turbo especificación Owen Developments y ECU controlada de 240–265 bhp."),
        ("Gearbox & differential", "Caja y diferencial",
         "Road F56 uses brake-based electronic torque control; JCW race class fits a Quaife sequential gearbox and plated limited-slip differential.",
         "El F56 de calle usa control electrónico por freno; el de pista monta caja secuencial Quaife y diferencial autoblocante de placas."),
        ("Brakes & unsprung hardware", "Frenos y masa no suspendida",
         "Road JCW fits red four-piston calipers with fog-lamp cooling apertures; JCW race class runs Alcon floating rotors, Nitron 3-way dampers and 17-inch wheels at ~1,180 kg with driver.",
         "El JCW de calle equipa cáliper rojos de cuatro pistones sin niebla para ductos; el de pista usa discos flotantes Alcon, amortiguadores Nitron de 3 vías y rines de 17 pulgadas (~1,180 kg con piloto)."),
        ("Mexican Hot Chili nomenclature", "Versión Hot Chili en México",
         "Top-tier trim pairing the 231 PS / 320 Nm mechanical specification, four-piston calipers, MINI Driving Modes and LCI Union Jack tail lamps.",
         "Acabado tope de equipamiento que combina la base mecánica de 231 PS / 320 Nm, cáliper de cuatro pistones, modos de manejo y calaveras Union Jack del LCI."),
    ],
    "src": ["wiki-hatch", "mc-jcw-class"],
}

NORTH_AMERICA = {
    "title_en": "North America desk: Mexico & the US—mostly identical, with four real splits",
    "title_es": "Cuadro Norteamérica: México y Estados Unidos—casi idénticos, con cuatro diferencias reales",
    "intro_en": "In practice, MINI Hardtop / 3-Door shipments to the United States and Mexico start from the same left-hand-drive "
                "Oxford build platform and follow North American model years—yet safety regulations, horsepower conventions, "
                "trim labels, and tariffs create four distinct differences you can spot on the curb and on the spec sheet.",
    "intro_es": "En la práctica, los MINI de 3 puertas enviados a Estados Unidos y México parten de la misma plataforma con "
                "volante a la izquierda armada en Oxford y comparten años modelo norteamericanos; aun así, las normas de "
                "iluminación, las unidades de potencia, los nombres de paquete y los aranceles crean cuatro diferencias concretas.",
    "head_en": ("Aspect", "United States (US)", "Mexico (MX)", "Europe / UK baseline"),
    "head_es": ("Aspecto", "Estados Unidos (EE. UU.)", "México (MX)", "Referencia Europa / R. Unido"),
    "rows": [
        ("Wheel-arch side markers & rules", "Reflejantes y norma de luces",
         "FMVSS 108 manufacturer compliance: recessed amber front + red rear arch markers (visible in DC R53/R56 photos)", "Norma FMVSS 108 ante NHTSA: reflejantes ámbar adelante y rojos atrás en los arcos",
         "UNECE lighting type approval: clean black wheel-arch trim with no side markers", "Homologación UNECE: arcos negros limpios sin reflejantes laterales",
         "UNECE Regulation 48 / clean arches", "Reglamento UNECE / arcos limpios"),
        ("F56 & F66 JCW 170 kW rating", "Cifra de 170 kW en F56 y F66 JCW",
         "228 hp SAE (745.7 W/hp) · 236 lb-ft (F56) / 280 lb-ft (F66)", "228 hp SAE (745.7 W/hp) · 236 lb-ft (F56) / 280 lb-ft (F66)",
         "231 PS metric (735.5 W/PS) · 320 Nm (F56) / 380 Nm (F66)", "231 PS métricos (735.5 W/PS) · 320 Nm (F56) / 380 Nm (F66)",
         "231 PS (170 kW) · 320 Nm / 380 Nm", "231 PS (170 kW) · 320 Nm / 380 Nm"),
        ("Top equipment tier naming", "Nombre del acabado tope",
         "Iconic trim (F56/F66) above Classic & Signature tiers", "Acabado Iconic (F56/F66) sobre niveles Classic y Signature",
         "Hot Chili (top performance + tech package in Mexico)", "Hot Chili (paquete tope de equipamiento en México)",
         "Level / Trim packages (I–III / Sport)", "Niveles / paquetes regionales"),
        ("2024– F66 Petrol vs. J01 Electric", "F66 gasolina vs. J01 eléctrico (2024–)",
         "Oxford-built F66 JCW 2 Door (228 hp / 280 lb-ft, 7-DCT, 5.9 s); no China-built J01 imported", "F66 JCW de Oxford (228 hp / 280 lb-ft, 7-DCT, 5.9 s); sin J01 armado en China",
         "Both Oxford F66 petrol JCW and J01 Electric (190 kW / 258 hp)", "Tanto F66 gasolina de Oxford como J01 eléctrico (190 kW / 258 hp)",
         "Both Oxford F66 and J01 JCW Electric", "Tanto F66 de Oxford como J01 JCW eléctrico"),
        ("Emissions & Classic ADO15 era", "Emisiones y época clásica ADO15",
         "SULEV B46 sibling variant; Austin/Morris 850 ended before 1968 FMVSS 108 rules", "Variante hermana SULEV B46; Austin/Morris 850 cesó ante FMVSS 108 de 1968",
         "B48 calibration; local CKD/classic era history diverged from US cutoff", "Calibración B48; historia de importación distinta al corte de 1968 en EE. UU.",
         "Euro 6 / WLTP OPF particulate filter", "Euro 6 / filtro de partículas OPF WLTP"),
    ],
    "note_en": "Model unit conversions verified in Part V Model 4; regulatory lighting and lineup facts cited directly from MINI USA, BMW Group Newsroom, and Wikipedia records read on 2026-11-15.",
    "note_es": "Conversiones de unidades verificadas en el Modelo 4 de la Parte V; normas de luces y catálogo citados directo de MINI USA, BMW Group y fichas consultadas el 2026-11-15.",
    "src": ["miniusa-jcw", "bmw-jcw-2024", "wiki-fmvss108", "wiki-hp", "wiki-b48", "wiki-hatch", "wiki-mini"],
}

# ---------------------------------------------------------------------------------------------------------------
# Cross-generation track times on Brands Hatch Indy (Kent, UK).
# Rows from Mini 7 Racing Club explicitly list Length = 1.208 miles; rows from MINI CHALLENGE Stats omit length.
# (row_id, era, class_name, year, time_str, seconds, driver, listed_mph, config_str, src_key)
# ---------------------------------------------------------------------------------------------------------------
LAPS = [
    ("se7en-s", "ADO15", "Mini Se7en S-Class (1,293 cc mild)", 2024, "0:58.822", 58.822, "Frazer Hack", "73.92 mph", "1.208 mi", "mini7-records"),
    ("se7en", "ADO15", "Mini Se7en (998 cc A-series)", 2023, "0:58.247", 58.247, "Mike Jordan", "74.65 mph", "1.208 mi", "mini7-records"),
    ("cooper-race", "R50", "MINI CHALLENGE Cooper (Race)", 2025, "0:56.507", 56.507, "Jenson Mason", "not stated", "", "mc-cooper-records"),
    ("cooper-qual", "R50", "MINI CHALLENGE Cooper (Qual.)", 2025, "0:56.221", 56.221, "Gabe Fairbrother", "not stated", "", "mc-cooper-records"),
    ("libre", "ADO15", "Mini Libre (up to 1,380 cc)", 2018, "0:54.800", 54.800, "David Franks", "79.35 mph", "1.208 mi", "mini7-records"),
    ("miglia", "ADO15", "Mini Miglia (1,293 cc slicks)", 2024, "0:53.979", 53.979, "Rupert Deeth (listed Rupery Deeth)", "80.56 mph", "1.208 mi", "mini7-records"),
    ("jcw-race", "F56", "MINI CHALLENGE JCW (Race)", 2022, "0:50.502", 50.502, "Sam Weller", "not stated", "", "mc-jcw-records"),
    ("jcw-qual", "F56", "MINI CHALLENGE JCW (Qual.)", 2022, "0:50.175", 50.175, "Jack Mitchell", "not stated", "", "mc-jcw-records"),
]

LAPS_TEXT = {
    "title_en": "Ghost race: Brands Hatch Indy (Kent, UK)",
    "title_es": "Carrera fantasma: Brands Hatch Indy (Kent, Reino Unido)",
    "intro_en": "Few circuits belong to the Mini like Brands Hatch Indy—1.208 miles (1,944 m) through Paddock Hill Bend, "
                "Druids, Graham Hill, Cooper Straight and Clearways, where Formula Mini Se7en first raced in 1966. "
                "Below sit eight official class lap records from the Mini 7 Racing Club and MINI CHALLENGE UK. Press start "
                "and all eight run together at 10× speed.",
    "intro_es": "Pocos circuitos pertenecen al Mini como Brands Hatch Indy—1.208 millas (1,944 m) pasando por Paddock Hill "
                "Bend, Druids, Graham Hill, la recta Cooper Straight y Clearways, donde la Fórmula Mini Se7en debutó en "
                "1966. Abajo corren ocho récords oficiales del Mini 7 Racing Club y la MINI CHALLENGE británica. Presiona "
                "iniciar y los ocho arrancan juntos a velocidad 10×.",
    "read_en": "What the arithmetic shows: across those eight official class records, the F56-based JCW qualifying lap "
               "(50.175 s) is 8.65 seconds faster per 50-second lap than the entry Classic S-Class record (58.822 s). "
               "Among classic A-series entries, Goodyear slicks and full Miglia tune shave 4.27 seconds off "
               "the 998 cc cross-ply Se7en.",
    "read_es": "Lo que muestra la aritmética: entre los ocho récords de categoría, la vuelta de calificación del JCW "
               "basado en F56 (50.175 s) es 8.65 segundos más rápida por giro que la referencia S-Class clásico "
               "(58.822 s). Entre los clásicos de bloque A-series, los slicks y la preparación Miglia recortan "
               "4.27 segundos frente al Se7en de 998 cc en llanta diagonal.",
    "caveat_en": "Same circuit, not the same day or class rules: classic Se7en and Miglia cars carry 998–1,380 cc A-series "
                 "engines on 10-inch or small race wheels; MINI CHALLENGE Trophy/Cooper cars run 130 bhp 1.6 L engines "
                 "(~1,110 kg); JCW Class cars run Gen 3 F56 2.0 L turbo hardware (240–265 bhp, ~1,180 kg). The Mini 7 "
                 "table states the 1.208 mi length and mph; MINI CHALLENGE Stats prints time only, so those four speed "
                 "columns stay hollow.",
    "caveat_es": "Mismo circuito, no mismo día ni mismo reglamento: los Se7en y Miglia clásicos corren con motores A-series "
                 "de 998–1,380 cc; los Cooper/Trophy de la MINI CHALLENGE usan 1.6 L atmosférico de 130 bhp (~1,110 kg); "
                 "la clase JCW corre sobre plataforma Gen 3 F56 2.0 L turbo (240–265 bhp, ~1,180 kg). La tabla del club "
                 "Mini 7 indica 1.208 mi y mph; MINI CHALLENGE Stats solo publica el tiempo, por eso esas cuatro filas "
                 "quedan con punto hueco.",
    "loop_en": "Schematic Indy contour showing Paddock Hill, Druids, Cooper Straight and Clearways. Each dot moves at the "
               "constant average speed its lap time implies at 10× speed; real laps brake hard into Paddock Hill and Druids. "
               "Hollow dots mark rows where the source table leaves distance blank.",
    "loop_es": "Contorno esquemático de Brands Hatch Indy con Paddock Hill, Druids, Cooper Straight y Clearways. Cada punto "
               "avanza a la velocidad promedio constante que implica su vuelta a 10×; las vueltas reales frenan fuerte en "
               "Paddock Hill y Druids. Los puntos huecos marcan filas donde la fuente omite la longitud.",
}

# ---------------------------------------------------------------------------------------------------------------
# Interactive Mechanics Lab & Papers
# ---------------------------------------------------------------------------------------------------------------
LOAD_SCIENCE = {
    "intro_en": "“Wheels at the corners” is not a slogan; it is lever-arm arithmetic. As cornering g rises, weight shifts from "
                "the inside tire to the outside tire by ΔF_z = m_axle · g · a_y · h_cg / t_track. Because a tire loses "
                "peak grip slightly faster on the overloaded side than it gains on the unloaded side, total axle grip drops.",
    "intro_es": "“Ruedas en las esquinas” no es un lema; es aritmética de palancas. Al aumentar la aceleración lateral en curva, "
                "se transfiere peso de la llanta interior a la exterior según ΔF_z = m_axle · g · a_y · h_cg / t_track. Como "
                "el neumático pierde eficiencia más rápido en el lado sobrecargado de lo que gana en el descargado, el "
                "agarre total del eje cae.",
    "science_en": "Why track width and anti-roll split govern yaw balance: Ricco and colleagues (2020) model how varying the "
                  "front-to-total anti-roll moment distribution controls steady-state cornering and yaw rate through "
                  "differential lateral load transfer across front and rear axles. That paper studied an electric AWD test "
                  "platform, not a Mini, but the load-transfer geometry is the same physics.",
    "science_es": "Por qué el ancho de vía y el reparto antibalanceo gobiernan el giro: Ricco y colegas (2020) modelan cómo "
                  "variar la distribución del momento antibalanceo controla la guiñada mediante la transferencia lateral de "
                  "carga en cada eje. Ese artículo estudió un prototipo eléctrico de tracción total, no un Mini, pero la "
                  "geometría de transferencia de carga es la misma física.",
    "caption_en": "Computed, not measured: F56 1,485 mm track width comes from BMW dimensions; all other inputs (axle mass, "
                  "h_cg and tire load sensitivity k_load) are MODEL values.",
    "caption_es": "Calculado, no medido: el ancho de vía de 1,485 mm del F56 viene de dimensiones oficiales; el resto de las "
                  "entradas (masa del eje, altura h_cg y sensibilidad de llanta k_load) son valores de MODELO.",
}

BRAKE_SCIENCE = {
    "intro_en": "Into Paddock Hill Bend at Brands Hatch, braking from high speed turns kinetic energy ½·m·(v₁² − v₂²) into "
                "rotor heat. Larger ventilated discs carry more iron thermal mass so each stop raises disc temperature less "
                "before airflow has to carry that heat away.",
    "intro_es": "Al entrar a Paddock Hill Bend en Brands Hatch, frenar desde alta velocidad convierte energía cinética "
                "½·m·(v₁² − v₂²) en calor dentro del disco. Los rotores ventilados más grandes aportan mayor masa térmica "
                "de hierro, reduciendo el pico de temperatura de una frenada antes de que el flujo de aire lo disipe.",
    "science_en": "Why front cooling ducts replace fog lamps on the F56 JCW: Adamowicz & Grzes (2011) solve 3D transient heat "
                  "conduction and convective cooling on solid automotive brake discs, showing how repeated braking relies on "
                  "convective heat transfer between stops to hold peak surface temperature down. Their model examined general "
                  "automotive discs, not a Mini.",
    "science_es": "Por qué los ductos de enfriamiento reemplazan los faros de niebla en el F56 JCW: Adamowicz y Grzes (2011) "
                  "resuelven la conducción térmica transitoria y la convección en discos de freno durante frenadas repetidas, "
                  "mostrando cómo el flujo de aire entre curvas limita la temperatura superficial. Ese trabajo estudió discos "
                  "automotrices generales, no un Mini.",
    "caption_en": "Adiabatic single-stop upper bound (neglecting pad/hub conduction and airflow convection): 1,220 kg F56 JCW "
                  "kerb weight from Wikipedia Hatch table; rotor masses, front bias and heat capacity are MODEL values.",
    "caption_es": "Cota superior adiabática en una sola frenada (sin conducción hacia pastilla/maza ni convección): peso de "
                  "1,220 kg del F56 JCW de la ficha; masas de disco, reparto y calor específico son valores de MODELO.",
}

LAB = {
    "title_en": "Mechanics Lab: the physics, worked",
    "title_es": "Laboratorio de mecánica: la física, resuelta",
    "intro_en": "The history above traces how five Mini eras changed proportions, boost, regional regulations and rotors. Below are "
                "four computed models you can inspect. Any input without a listed source is marked MODEL: an illustrative value "
                "to expose the mechanism, not a measurement of any Mini. A verifier in the repository recomputes every number.",
    "intro_es": "La crónica de arriba muestra cómo cinco épocas del Mini cambiaron proporciones, sobrealimentación, normas "
                "regionales y frenos. Abajo hay cuatro modelos calculados. Toda entrada sin fuente publicada lleva la etiqueta "
                "MODELO: un valor ilustrativo para mostrar el mecanismo, no una medición de un Mini. Un verificador en el "
                "repositorio recalcula cada cifra.",
    "load_h_en": "1 · Lateral load transfer & tire load sensitivity",
    "load_h_es": "1 · Transferencia lateral de carga y sensibilidad del neumático",
    "load_p_en": "Because peak lateral force per unit vertical load falls slightly with load (μ₀ − k·F_z), shifting ΔF_z from "
                 "inside to outside removes 2·k·(ΔF_z)² of total axle grip even before the inside wheel lifts. Widening "
                 "the track from 1.36 m to 1.485 m and lowering h_cg drops that loss sharply.",
    "load_p_es": "Como la fuerza lateral por unidad de carga vertical cae levemente al sobrecargarse (μ₀ − k·F_z), mover ΔF_z "
                 "de la rueda interior a la exterior resta 2·k·(ΔF_z)² de agarre total del eje incluso antes de despegar la "
                 "rueda interna. Ensanchar la vía de 1.36 m a 1.485 m y bajar h_cg recorta fuerte esa pérdida.",
    "brake_h_en": "2 · Single-stop brake rotor thermal rise",
    "brake_h_es": "2 · Aumento térmico adiabático por frenada en rotor delantero",
    "brake_p_en": "Decelerating a 1,220 kg car from 160 km/h to 80 km/h sheds 903.7 kJ of kinetic energy; at a 72% front "
                  "braking split, each front disc absorbs 325.3 kJ. In an adiabatic single-stop upper bound, tripling rotor "
                  "thermal mass cuts temperature rise by two-thirds.",
    "brake_p_es": "Frenar un auto de 1,220 kg de 160 km/h a 80 km/h disipa 903.7 kJ de energía cinética; con un reparto "
                  "delantero de 72 %, cada disco frontal absorbe 325.3 kJ. Como cota superior adiabática, triplicar la masa "
                  "térmica del disco reduce dos terceras partes la subida de temperatura.",
    "laps_h_en": "3 · Brands Hatch Indy lap speeds (1.208 miles)",
    "laps_h_es": "3 · Velocidades promedio en Brands Hatch Indy (1.208 millas)",
    "laps_p_en": "Dividing 1,944.09 m (1.208 × 1,609.344 m) by lap time yields average speed—computed ONLY for the four Mini 7 "
                 "Racing Club rows that print 1.208 mi. The four MINI CHALLENGE rows stay blank rather than "
                 "borrowing distance across tables.",
    "laps_p_es": "Dividir 1,944.09 m (1.208 × 1,609.344 m) entre el tiempo de vuelta da la velocidad promedio—calculada SOLO "
                 "para las cuatro filas del Mini 7 Racing Club que imprimen 1.208 mi. Las cuatro filas "
                 "de MINI CHALLENGE quedan en blanco sin tomar prestada distancia de otra tabla.",
    "power_h_en": "4 · US 228 hp vs. Mexico/EU 231 PS conversion (identical 170 kW engine)",
    "power_h_es": "4 · Conversión 228 hp EE. UU. vs. 231 PS México/UE (mismo motor de 170 kW)",
    "power_p_en": "Why an identical 170.0 kW shaft rating prints as 228 hp in US sheets and 231 PS (or 231 hp metric) in Mexico "
                  "and Europe: SAE J1349 mechanical horsepower defines 1 hp as 745.70 W (170,000 / 745.70 = 227.97 hp -> 228 hp), "
                  "whereas DIN 66036 metric horsepower defines 1 PS as 735.50 W (170,000 / 735.50 = 231.14 PS -> 231 PS). "
                  "Likewise, 320 Nm converts to 236 lb-ft and F66’s 380 Nm converts to 280 lb-ft.",
    "power_p_es": "Por qué un mismo eje de 170.0 kW aparece como 228 hp en fichas de EE. UU. y 231 PS (o 231 hp métricos) en "
                  "México y Europa: 1 hp mecánico SAE J1349 equivale a 745.70 W (170,000 / 745.70 = 227.97 hp -> 228 hp), "
                  "mientras 1 PS métrico DIN 66036 equivale a 735.50 W (170,000 / 735.50 = 231.14 PS -> 231 PS). Del mismo "
                  "modo, 320 Nm equivalen a 236 lb-ft y los 380 Nm del F66 a 280 lb-ft.",
    "verify_h_en": "Run it yourself",
    "verify_h_es": "Córrelo tú",
    "verify_en": "The verifier lives at skills/classics/cc03/verify_cc03_mechanics.py, paired with SKILL.md. Using only Python’s "
                 "standard library, it checks the SHA-256 data pin, re-derives lateral grip loss both directly and via "
                 "2·k·(ΔF_z)², numerically integrates braking power, checks all four stated-length Indy speeds plus the "
                 "SAE vs. metric unit conversions, and fails under five planted physics defects.",
    "verify_es": "El verificador vive en skills/classics/cc03/verify_cc03_mechanics.py junto a su SKILL.md. Usando solo la "
                 "biblioteca estándar de Python, revisa la firma SHA-256 de datos, recalcula la pérdida de agarre directo y "
                 "por 2·k·(ΔF_z)², integra numéricamente la potencia de frenado, revisa las cuatro velocidades de pista y las "
                 "conversiones SAE vs. métrica, y falla bajo cinco defectos plantados.",
}

SILENT = [
    {
        "q_en": "What rotor diameter did the 2024 F66 JCW launch sheet print?",
        "q_es": "¿Qué diámetro de disco delantero imprimió el comunicado 2024 del F66 JCW?",
        "a_en": "BMW Group’s 13 November 2024 release lists power, torque and sprint metrics without printing rotor diameters: not stated.",
        "a_es": "El comunicado de BMW Group del 13 de noviembre de 2024 da potencia, par y aceleración sin indicar diámetro de discos: no se indica.",
    },
    {
        "q_en": "Do published F56 specifications separate OEM rotor mass in kilograms?",
        "q_es": "¿Las fichas publicadas del F56 desglosan el peso del rotor de freno en kilogramos?",
        "a_en": "Only curb weights and R56 disc dimensions appear in our read sources; rotor masses (3.2 / 7.4 / 9.8 kg) in Part V are explicitly labeled MODEL.",
        "a_es": "Solo aparecen pesos totales y medidas del R56 en las fuentes leídas; las masas de disco (3.2 / 7.4 / 9.8 kg) en la Parte V se etiquetan como MODELO.",
    },
    {
        "q_en": "Which model years changed every minor line item inside Mexico’s “Hot Chili” or MINI USA’s “Iconic” option bundle?",
        "q_es": "¿Qué años cambiaron cada detalle menor dentro del paquete “Hot Chili” de México o “Iconic” en EE. UU.?",
        "a_en": "Year-by-year option-sheet line codes were not archived across regional brochures, so only verified structural, powertrain, lighting and trim-tier names are stated here.",
        "a_es": "Los códigos menores año por año no quedaron archivados de forma completa en folletos regionales; aquí solo se afirman datos verificados de chasis, tren motriz, iluminación y nivel de acabado.",
    },
    {
        "q_en": "Why do the MINI CHALLENGE Stats lap tables leave track mileage blank?",
        "q_es": "¿Por qué las tablas de MINI CHALLENGE Stats omiten el kilometraje de pista?",
        "a_en": "Those club result tables print circuit, driver, team, lap and year without distance; we leave their derived speeds blank rather than borrowing 1.208 mi from Mini 7.",
        "a_es": "Esas tablas solo publican circuito, piloto, equipo, tiempo y año sin distancia; dejamos sus velocidades derivadas en blanco en vez de copiar 1.208 mi de Mini 7.",
    },
]

CLOSING = [
    {
        "en": "Sixty-five years after a 3.05-meter commuter squeezed its four cylinders sideways to keep a wheel in each corner, "
              "the proportions still explain the drive: wide stance, short overhangs, front rotors sized for repeat stops, and "
              "an unbroken human relay from Longbridge drafting tables and Brands Hatch bends to North American tarmac.",
        "es": "Sesenta y cinco años después de que un compacto de 3.05 metros girara sus cuatro cilindros de lado para empujar "
              "una rueda a cada esquina, las proporciones siguen explicando la física: vía ancha, voladizos cortos, discos "
              "frontales dimensionados para frenadas repetidas y una estafeta humana viva desde los restiradores de Longbridge "
              "y las curvas de Brands Hatch hasta los caminos de Norteamérica.",
        "src": [],
    },
]

# Enthusiast 2-photo clamshell Easter egg (privacy-scrubbed, zero metadata, zero owner words, zero power ratings)
EGG = {
    "id": "egg-front",
    "kind": "photo",
    "license": "Metadata-scrubbed photo",
    "era": "F56 · Hot Chili",
    "button_en": "Pop the clamshell bonnet",
    "button_es": "Abrir el cofre de almeja",
    "close_en": "Shut the bonnet",
    "close_es": "Cerrar el cofre",
    "caption_en": "MINI F56 John Cooper Works Hot Chili in Midnight Black Metallic with gold cross-spoke alloy wheels, red four-piston front Brembo calipers, gold grille bar and clean UNECE black wheel arches (no US FMVSS 108 amber side markers).",
    "caption_es": "MINI F56 John Cooper Works Hot Chili en Midnight Black Metallic con rines dorados de brazos cruzados, cáliper delanteros Brembo rojos de cuatro pistones, barra dorada frontal y arcos negros limpios norma UNECE (sin reflejantes laterales de EE. UU.).",
    "alt_en": "Front three-quarter view of a black F56 MINI John Cooper Works Hot Chili with gold cross-spoke wheels, red front brake calipers and clean black UNECE arches parked beside an open road.",
    "alt_es": "Vista frontal tres cuartos de un MINI F56 John Cooper Works Hot Chili negro con rines dorados, cáliper rojos y arcos negros sin reflejantes laterales junto a la carretera.",
    "links": [("Brembo", "https://www.brembo.com/")],
    "image": "images/mini-jcw/mini-jcw-front-three-quarter.jpg",
    "width": 1024,
    "height": 768,
    "src": ["wiki-hatch", "wiki-fmvss108"],
}

EGG_SKETCH = {
    "id": "egg-rear-sketch",
    "kind": "render",
    "license": "Conceptual track sketch",
    "era": "Brands Hatch · Woodland",
    "caption_en": "Conceptual visualization imagining the black-and-gold F56 JCW Hot Chili from its low rear three-quarter angle—showing LCI Union Jack tail lamps, two-piece roof wing, central dual exhaust and blank dark plate—alongside the wooded trackside bend of a circuit loop inspired by Brands Hatch as a single pen-and-ink and selective-wash studio sketch (original full-frame illustration, not a track photograph).",
    "caption_es": "Visualización conceptual que imagina al F56 JCW Hot Chili negro y dorado desde su ángulo trasero tres cuartos bajo—con calaveras Union Jack del LCI, alerón de dos piezas, escape doble central y placa trasera oscura en blanco—al borde de una curva arbolada inspirada en Brands Hatch como un solo boceto de estudio a tinta y acuarela selectiva (ilustración original completa, no fotografía real en pista).",
    "alt_en": "Conceptual visualization imagining the low rear three-quarter of a Midnight Black F56 MINI JCW Hot Chili on gold wheels alongside a wooded circuit bend inspired by Brands Hatch rendered entirely as a pen-and-ink and selective-wash sketch (original full-frame illustration, not a track photograph).",
    "alt_es": "Visualización conceptual que imagina la parte trasera tres cuartos baja de un MINI F56 JCW Hot Chili negro con rines dorados al lado de una curva de circuito entre árboles inspirada en Brands Hatch trazada por completo como boceto a tinta y acuarela selectiva (ilustración original completa, no fotografía real en pista).",
    "links": [],
    "image": "images/mini-jcw/mini-jcw-rear-sketched-track.jpg",
    "width": 1024,
    "height": 768,
    "src": ["brands-hatch", "wiki-hatch"],
}

# Full 8-plate visual archive (Frontispiece tribute + 5 archival Commons photos + 2 clamshell Easter-egg plates)
MEDIA = [
    {
        "id": "plate-frontispiece",
        "kind": "render",
        "license": "Conceptual tribute sketch",
        "era": "1959 · ADO15",
        "caption_en": "Conceptual visualization imagining a 1959 Longbridge drafting board tribute to Alec Issigonis and John Cooper: pen-and-ink linework of the sideways A-series engine, sump transmission, and pushed-out front corner wheel beside brass dividers and a mechanical stopwatch (original illustration, not a 1959 archive drawing).",
        "caption_es": "Visualización conceptual que imagina una mesa de dibujo de Longbridge en homenaje a Alec Issigonis y John Cooper: trazo a tinta del motor A-series transversal sobre su transmisión en el cárter y rueda delantera en la esquina, junto a compás de latón y cronómetro mecánico (ilustración original, no plano histórico de 1959).",
        "alt_en": "Conceptual visualization of an ink drafting-board tribute to 1959 compact transverse engineering showing a sideways four-cylinder front axle cutaway beside brass dividers and an unlabelled stopwatch.",
        "alt_es": "Visualización conceptual de un homenaje sobre restirador a tinta de la ingeniería transversal de 1959, mostrando un corte de eje delantero y motor transversal junto a compás de latón y cronómetro.",
        "links": [],
        "image": "images/mini-jcw/mini-frontispiece-tribute.jpg",
        "width": 1024,
        "height": 768,
        "src": ["wiki-issigonis", "wiki-cooper", "wiki-mini"],
    },
    {
        "id": "photo-1959-mini",
        "kind": "photo",
        "license": "CC BY 2.0",
        "era": "1959 · Classic ADO15",
        "caption_en": "1959 Morris Mini-Minor showing how tiny 10-inch outer wheels and flat boot floor packaging left room for four adults inside a 3.05-meter footprint (photo: andreboeni, CC BY 2.0).",
        "caption_es": "Morris Mini-Minor 1959 mostrando cómo las ruedas de 10 pulgadas en las esquinas y la cajuela plana liberaban espacio para cuatro adultos en apenas 3.05 metros de largo (foto: andreboeni, CC BY 2.0).",
        "alt_en": "Red 1959 Morris Mini-Minor hatchback with small ten-inch wheels and open rear luggage boot lid.",
        "alt_es": "Morris Mini-Minor 1959 rojo con rines pequeños de diez pulgadas y tapa de cajuela trasera abierta.",
        "links": [],
        "image": "images/mini-jcw/photo-1959-morris-mini-minor.jpg",
        "width": 1280,
        "height": 956,
        "src": ["commons-1959-mini", "wiki-mini"],
    },
    {
        "id": "photo-1964-33ejb",
        "kind": "photo",
        "license": "CC BY 2.0",
        "era": "1964 · 33 EJB",
        "caption_en": "1963 Morris Mini Cooper S #37 (33 EJB), driven by Paddy Hopkirk and Henry Liddon to overall victory in the 1964 Monte Carlo Rally (photo: Tony Hisgett, CC BY 2.0).",
        "caption_es": "Morris Mini Cooper S 1963 número 37 (33 EJB), con el que Paddy Hopkirk y Henry Liddon ganaron el Rally de Montecarlo de 1964 (foto: Tony Hisgett, CC BY 2.0).",
        "alt_en": "Red and white-roofed 1963 Morris Mini Cooper S #37 rally car (33 EJB) preserved on display.",
        "alt_es": "Morris Mini Cooper S 1963 rojo con techo blanco número 37 (33 EJB), ganador de Montecarlo 1964.",
        "links": [],
        "image": "images/mini-jcw/photo-1964-monte-carlo-33ejb.jpg",
        "width": 1280,
        "height": 862,
        "src": ["commons-1964-33ejb", "wiki-mini"],
    },
    {
        "id": "photo-r53-usa",
        "kind": "photo",
        "license": "CC BY 4.0",
        "era": "R53 · North America",
        "caption_en": "US-specification first-generation MINI Cooper S (R53) in Washington, D.C., displaying the supercharged bonnet scoop and recessed amber front wheel-arch marker required under FMVSS 108 (photo: OWS Photography, CC BY 4.0).",
        "caption_es": "MINI Cooper S (R53) especificación EE. UU. en Washington, D.C., mostrando la toma del intercooler en el cofre y el reflejante lateral ámbar en el arco exigido por FMVSS 108 (foto: OWS Photography, CC BY 4.0).",
        "alt_en": "White R53 MINI Cooper S hatchback photographed in Washington D.C., showing functional hood scoop and amber US side marker in the front wheel arch.",
        "alt_es": "MINI Cooper S R53 blanco fotografiado en Washington D.C., con toma de aire en el cofre y reflejante lateral ámbar en el arco delantero.",
        "links": [],
        "image": "images/mini-jcw/photo-r53-cooper-s-usa.jpg",
        "width": 1280,
        "height": 1024,
        "src": ["commons-r53-usa", "wiki-fmvss108", "wiki-stephenson"],
    },
    {
        "id": "photo-r56-usa",
        "kind": "photo",
        "license": "CC BY 4.0",
        "era": "R56 · North America",
        "caption_en": "US-specification R56 John Cooper Works hatch showing fixed front wing headlamps, factory red front brake caliper peeking behind black wheels, and FMVSS 108 amber/red arch reflectors (photo: OWS Photography, CC BY 4.0).",
        "caption_es": "MINI John Cooper Works R56 especificación EE. UU. con faros fijos en salpicadera, cáliper delantero rojo de fábrica y reflejantes laterales FMVSS 108 adelante y atrás (foto: OWS Photography, CC BY 4.0).",
        "alt_en": "Gray and black-roofed US-spec R56 MINI John Cooper Works hatchback showing red front brake caliper and amber/red side arch markers.",
        "alt_es": "MINI John Cooper Works R56 gris con techo negro especificación estadounidense, mostrando cáliper delantero rojo y reflejantes laterales de arco.",
        "links": [],
        "image": "images/mini-jcw/photo-r56-jcw-usa.jpg",
        "width": 1280,
        "height": 1024,
        "src": ["commons-r56-usa", "wiki-jcw", "wiki-fmvss108"],
    },
    {
        "id": "photo-2022-brands",
        "kind": "photo",
        "license": "CC BY 4.0",
        "era": "2022 · Brands Hatch",
        "caption_en": "Gen 3 F56 MINI CHALLENGE UK John Cooper Works race cars assembled at Brands Hatch in 2022—showing rear JCW wings, roof air scoops and full club-racing aerodynamic trim (photo: BWard 1997, CC BY 4.0).",
        "caption_es": "Autos de carrera Gen 3 F56 de la categoría MINI CHALLENGE británica reunidos en Brands Hatch en 2022, con alerón trasero y preparación completa de pista (foto: BWard 1997, CC BY 4.0).",
        "alt_en": "Row of F56 MINI CHALLENGE UK John Cooper Works race cars prepared in the paddock at Brands Hatch.",
        "alt_es": "Fila de autos F56 MINI CHALLENGE UK John Cooper Works preparados en el paddock de Brands Hatch.",
        "links": [],
        "image": "images/mini-jcw/photo-2022-brands-hatch-jcw.jpg",
        "width": 1280,
        "height": 720,
        "src": ["commons-2022-brands", "mc-jcw-class"],
    },
    EGG,
    EGG_SKETCH,
]

FOOTER_NOTE = {
    "en": "Not affiliated with or endorsed by BMW AG, MINI or John Cooper Works. MINI, Cooper and John Cooper Works are "
          "trademarks of BMW AG, used here only to identify the cars. All circuit schematics, drafting sketches and engineering plots are "
          "original or attributed work. For learning, not buying, tuning or track-driving advice.",
    "es": "Sin afiliación ni respaldo de BMW AG, MINI ni John Cooper Works. MINI, Cooper y John Cooper Works son marcas de "
          "BMW AG, usadas aquí solo para identificar los autos. Todos los trazos de circuito, bocetos y gráficas son obra original o con crédito. Para "
          "aprender; no es consejo de compra, modificación ni manejo en pista.",
}

# Phrases forbidden across visible prose, captions, and alt text (checked by tests/test_mini_jcw.py).
BANNED = [
    "legendary", "iconic hatch", "iconic mini", "greatest", "best hot hatch", "giant-killer", "my car", "our car", "owner's car",
    "legendario", "icónico", "mi auto", "nuestro auto", "jugada",
]
