"""CC.01 · One Brief, Eight Answers — the Golf GTI as an engineering story (single source of truth).

Every factual claim on the page lives in this module next to its verified primary source:
- Volkswagen statements are attributed to Volkswagen ("VW says"); they are company statements, not independent tests.
- 15 peer-reviewed papers (checked in Crossref and Scite on 2026-11-15 with zero retractions) explain mechanical and
  vehicle-dynamics principles in general; none of them tested a Golf GTI, and the page states that beside every study.
- 9 Wikimedia Commons photographs (Public Domain / CC0 / CC BY — zero BY-SA) document the actual generations and cabin.
- 2 maintainer track/hood-up photographs in images/classics/ remain untouched under the 2026-11-15 caption contract.
- Retail pages and forum posts are never sources here. Anything a source does not state is written "not stated".
"""
from __future__ import annotations

SLUG = "golf-gti"
CODE = "CC.01"
DATE = "2026-11-15"
ACCESSED = "2026-11-15"

SEO = (
    "One Brief, Eight Answers: The Golf GTI as an Engineering Story",
    "Eight generations of the Golf GTI, one engineering move each: injection, sixteen valves, turbo, two clutches, "
    "brake-based and clutch-pack differentials, software. Sourced and interactive.",
    "Un reto, ocho respuestas: el Golf GTI como historia de ingeniería",
    "Ocho generaciones del Golf GTI, una decisión de ingeniería cada una: inyección, dieciséis válvulas, turbo, dos "
    "embragues, diferenciales por freno y por embrague, software. Con fuentes e interactivo.",
)

# ---------------------------------------------------------------------------------------------------------------
# Sources (37 total). "kind": vw (company statement), press (independent coverage), paper (peer-reviewed DOI checked
# in Crossref and Scite on 2026-11-15 with zero retractions), photo (Wikimedia Commons PD / CC0 / CC BY).
# ---------------------------------------------------------------------------------------------------------------
SOURCES = {
    "vw-history": {
        "short": "VW history",
        "short_es": "VW historia",
        "kind": "vw",
        "label": "Volkswagen Newsroom, “The history of the Golf GTI in detail”",
        "url": "https://www.volkswagen-newsroom.com/en/the-new-golf-gti-edition-50-international-media-drive-20143/the-history-of-the-golf-gti-in-detail-20156",
    },
    "vw-mk1": {
        "short": "VW Mk1 archive",
        "short_es": "VW archivo Mk1",
        "kind": "vw",
        "label": "Volkswagen Newsroom, “Golf I GTI (1976–1983)” archive entry",
        "url": "https://volkswagen-newsroom.com/en/golf-1-gti-19761983-19498",
    },
    "vw-mk1-story": {
        "short": "VW Mk1 story",
        "short_es": "VW relato Mk1",
        "kind": "vw",
        "label": "Volkswagen Newsroom, “Golf GTI Mk1” (history of the new Golf GTI: Anton Konrad, Hermann Hablitzel, Toni Schmücker, Herbert Schäfer, development order EA195)",
        "url": "https://www.volkswagen-newsroom.com/en/the-new-golf-gti-6025/golf-gti-history-6034",
    },
    "vw-mk5": {
        "short": "VW Mk5 archive",
        "short_es": "VW archivo Mk5",
        "kind": "vw",
        "label": "Volkswagen Newsroom, “Golf V GTI (2004–2008)” archive entry",
        "url": "https://www.volkswagen-newsroom.com/en/golf-5-gti-20042008-19511",
    },
    "vw-mk7-chassis": {
        "short": "VW 2013 chassis",
        "short_es": "VW chasis 2013",
        "kind": "vw",
        "label": "Volkswagen Newsroom, “New Golf GTI: running gear, layout and electronics” (2013)",
        "url": "https://www.volkswagen-newsroom.com/en/new-golf-gti-international-press-presentation-2976/new-golf-gti-running-gear-layout-and-electronics-2988",
    },
    "vw-mk7": {
        "short": "VW Mk7 archive",
        "short_es": "VW archivo Mk7",
        "kind": "vw",
        "label": "Volkswagen Newsroom, “Golf VII GTI (2013–2019)” archive entry",
        "url": "https://www.volkswagen-newsroom.com/en/golf-7-gti-20132019-20031",
    },
    "vw-us-2018": {
        "short": "VW US 2018 press kit",
        "short_es": "VW EE. UU. kit de prensa 2018",
        "kind": "vw",
        "label": "Volkswagen of America Media, “2018 Golf GTI press kit” (220 hp at 4,700 rpm, 258 lb-ft, all trims)",
        "url": "https://www.media.vw.com/en-us/press-kits/2018-golf-gti-press-kit",
    },
    "vw-cs-s": {
        "short": "VW Clubsport S",
        "kind": "vw",
        "label": "Volkswagen Newsroom, “Ten key facts: the Golf GTI Clubsport S”",
        "url": "https://volkswagen-newsroom.com/en/international-driving-presentation-the-new-golf-gti-clubsport-s-2776",
    },
    "hu2015": {
        "short": "Hu et al. 2015",
        "kind": "paper",
        "label": "Hu, Akehurst & Brace (2015). Novel approaches to improve the gas exchange process of downsized turbocharged spark-ignition engines: A review. International Journal of Engine Research 17(6), 595–618",
        "url": "https://doi.org/10.1177/1468087415599866",
    },
    "hu2016": {
        "short": "Hu et al. 2016",
        "kind": "paper",
        "label": "Hu, Turner, Akehurst et al. (2016). Observations on and potential trends for mechanically supercharging a downsized passenger car engine: a review. Proc. IMechE Part D 231(4), 435–456",
        "url": "https://doi.org/10.1177/0954407016636971",
    },
    "wiki-nords": {
        "short": "sport auto via Wikipedia",
        "short_es": "sport auto vía Wikipedia",
        "kind": "press",
        "label": "Wikipedia, “List of Nürburgring Nordschleife lap times” (rows citing sport auto Supertests 01/2002, 11/2005, 09/2011, 08/2013, 07/2016, 12/2019, 11/2021); raw text read 2026-11-15",
        "url": "https://en.wikipedia.org/wiki/List_of_N%C3%BCrburgring_Nordschleife_lap_times",
    },
    "scamarcio2023": {
        "short": "Scamarcio et al. 2023",
        "kind": "paper",
        "label": "Scamarcio, Caponio, Mihalkov et al. (2023). Predictive Anti-Jerk and Traction Control for V2X Connected Electric Vehicles With Central Motor and Open Differential. IEEE Transactions on Vehicular Technology 72(6), 7221–7239",
        "url": "https://doi.org/10.1109/tvt.2022.3143497",
    },
    "micromachines2026": {
        "short": "Micromachines 2026",
        "kind": "paper",
        "label": "Electromechanical Modeling and Dimensionless Optimization of a Multilayer PZT-5H Energy Harvester for Vehicle Suspension Systems (2026). Micromachines 17(10), 1111",
        "url": "https://doi.org/10.3390/mi17101111",
    },
    "ahmadian2000": {
        "short": "Ahmadian & Pare 2000",
        "kind": "paper",
        "label": "Ahmadian & Pare (2000). A Quarter-Car Experimental Analysis of Alternative Semiactive Control Methods. Journal of Intelligent Material Systems and Structures 11(8), 604–612",
        "url": "https://doi.org/10.1106/mr3w-5d8w-0lpl-wguq",
    },
    "press-cs-s": {
        "short": "CarAdvice 2016",
        "kind": "press",
        "label": "CarAdvice, “Volkswagen Golf GTI Clubsport S breaks front-drive Nürburgring lap record” (2016)",
        "url": "https://www.caradvice.com.au/news/2017-volkswagen-golf-gti-clubsport-s-breaks-front-drive-nurburgring-lap-record/",
    },
    "galvagno2011": {
        "short": "Galvagno 2011",
        "kind": "paper",
        "label": "Galvagno, Velardocchia & Vigliani (2011). Dynamic and kinematic model of a dual clutch transmission. Mechanism and Machine Theory 46(6), 794–805",
        "url": "https://doi.org/10.1016/j.mechmachtheory.2011.01.013",
    },
    "brancati2023": {
        "short": "Brancati 2023",
        "kind": "paper",
        "label": "Brancati, Pagano, Rocca et al. (2023). Dynamic Behaviour of an Automotive Dual Clutch Transmission during Gear Shift Maneuvers. Applied Sciences 13(8), 4828",
        "url": "https://doi.org/10.3390/app13084828",
    },
    "kakalis2008": {
        "short": "Kakalis 2008",
        "kind": "paper",
        "label": "Kakalis, Zorzutti, Cheli et al. (2008). Brake Based Torque Vectoring for Sport Vehicle Performance Improvement. SAE Int. J. Passenger Cars – Mechanical Systems 1(1), 514–525",
        "url": "https://doi.org/10.4271/2008-01-0596",
    },
    "woo2021": {
        "short": "Woo & Shin 2021",
        "kind": "paper",
        "label": "Woo & Shin (2021). A Double Sky-Hook Algorithm for Improving Road-Holding Property in Semi-Active Suspension Systems for Application to In-Wheel Motor. Applied Sciences 11(19), 8912",
        "url": "https://doi.org/10.3390/app11198912",
    },
    "karnopp1974": {
        "short": "Karnopp et al. 1974",
        "kind": "paper",
        "label": "Karnopp, Crosby & Harwood (1974). Vibration Control Using Semi-Active Force Generators. Journal of Engineering for Industry 96(2), 619–626",
        "url": "https://doi.org/10.1115/1.3438373",
    },
    "cronin1981": {
        "short": "Cronin 1981",
        "kind": "paper",
        "label": "Cronin, D. L. (1981). MacPherson strut kinematics. Mechanism and Machine Theory 16(6), 631–644",
        "url": "https://doi.org/10.1016/0094-114x(81)90069-0",
    },
    "pacejka1992": {
        "short": "Pacejka & Bakker 1992",
        "kind": "paper",
        "label": "Pacejka, H. B. & Bakker, E. (1992). The Magic Formula Tyre Model. Vehicle System Dynamics 21(S1), 1–18",
        "url": "https://doi.org/10.1080/00423119208969994",
    },
    "hac1992": {
        "short": "Hać & Youn 1992",
        "kind": "paper",
        "label": "Hać, A. & Youn, I. (1992). Optimal Semi-Active Suspension with Preview Based on a Quarter Car Model. Journal of Vibration and Acoustics 114(1), 84–92",
        "url": "https://doi.org/10.1115/1.2930239",
    },
    "zhao1999": {
        "short": "Zhao et al. 1999",
        "kind": "paper",
        "label": "Zhao, F., Lai, M.-C. & Harrington, D. L. (1999). Automotive spark-ignited direct-injection gasoline engines. Progress in Energy and Combustion Science 25(5), 437–562",
        "url": "https://doi.org/10.1016/s0360-1285(99)00004-0",
    },
    "abe2001": {
        "short": "Abe et al. 2001",
        "kind": "paper",
        "label": "Abe, M., Kano, Y., Suzuki, K., Shibahata, Y. & Furukawa, Y. (2001). Side-slip control to stabilize vehicle lateral motion by direct yaw moment. JSAE Review 22(4), 413–419",
        "url": "https://doi.org/10.1016/s0389-4304(01)00124-2",
    },
    "fichera2004": {
        "short": "Fichera et al. 2004",
        "kind": "paper",
        "label": "Fichera, G., Lacagnina, M. & Petrone, F. (2004). Modelling of Torsion Beam Rear Suspension by Using Multibody Method. Multibody System Dynamics 12(4), 303–316",
        "url": "https://doi.org/10.1007/s11044-004-2516-1",
    },
    "trachtler2004": {
        "short": "Trächtler 2004",
        "kind": "paper",
        "label": "Trächtler, A. (2004). Integrated vehicle dynamics control using active brake, steering and suspension systems. International Journal of Vehicle Design 36(1), 1–12",
        "url": "https://doi.org/10.1504/ijvd.2004.005316",
    },
    "rubin2015": {
        "short": "Rubin & Arogeti 2015",
        "kind": "paper",
        "label": "Rubin, D. & Arogeti, S. A. (2015). Vehicle yaw stability control using active limited-slip differential via model predictive control methods. Vehicle System Dynamics 53(9), 1315–1330",
        "url": "https://doi.org/10.1080/00423114.2015.1046461",
    },
    "commons-mk1": {
        "short": "Mk1 1982 photo",
        "short_es": "Foto Mk1 1982",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:1982 Volkswagen Golf GTi (Mk1) (14072934454).jpg” (Riley, Christchurch NZ; Creative Commons CC BY 2.0; registration plate obscured)",
        "url": "https://commons.wikimedia.org/wiki/File:1982_Volkswagen_Golf_GTi_(Mk1)_(14072934454).jpg",
    },
    "commons-mk7-interior": {
        "short": "GTI tartan interior photo",
        "short_es": "Foto interior escocés",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Volkswagen Golf GTI interior.jpg” (TTTNIS; Public Domain)",
        "url": "https://commons.wikimedia.org/wiki/File:Volkswagen_Golf_GTI_interior.jpg",
    },
    "commons-mk2": {
        "short": "Mk2 GTI photo",
        "short_es": "Foto Mk2 GTI",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:VW Golf II GTI (40516249732).jpg” (Guillaume Vachey; Creative Commons CC0 1.0 Public Domain Dedication; registration plate obscured)",
        "url": "https://commons.wikimedia.org/wiki/File:VW_Golf_II_GTI_(40516249732).jpg",
    },
    "commons-mk3": {
        "short": "Mk3 1996 photo",
        "short_es": "Foto Mk3 1996",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Volkswagen Golf III GTI (1996) (55082249962).jpg” (Charles; Creative Commons CC0 1.0 Public Domain Dedication)",
        "url": "https://commons.wikimedia.org/wiki/File:Volkswagen_Golf_III_GTI_(1996)_(55082249962).jpg",
    },
    "commons-mk4": {
        "short": "Mk4 2002 photo",
        "short_es": "Foto Mk4 2002",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Volkswagen Golf IV GTI (2002) (55083147451).jpg” (Charles; Creative Commons CC0 1.0 Public Domain Dedication)",
        "url": "https://commons.wikimedia.org/wiki/File:Volkswagen_Golf_IV_GTI_(2002)_(55083147451).jpg",
    },
    "commons-mk5": {
        "short": "Mk5 front photo",
        "short_es": "Foto frente Mk5",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Volkswagen GOLF V GTI front.JPG” (Tokumeigakarinoaoshima; Creative Commons CC0 1.0 Public Domain Dedication)",
        "url": "https://commons.wikimedia.org/wiki/File:Volkswagen_GOLF_V_GTI_front.JPG",
    },
    "commons-mk6": {
        "short": "Mk6 GTI photo",
        "short_es": "Foto Mk6 GTI",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Volkswagen Golf GTI (Mk VI) Washington DC Metro Area, USA.jpg” (OWS Photography; Creative Commons CC BY 4.0; registration plate obscured)",
        "url": "https://commons.wikimedia.org/wiki/File:Volkswagen_Golf_GTI_(Mk_VI)_Washington_DC_Metro_Area,_USA.jpg",
    },
    "commons-clubsport-s": {
        "short": "Clubsport S photo",
        "short_es": "Foto Clubsport S",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Volkswagen Golf GTI Clubsport S (31059402673).jpg” (Adam Court; Creative Commons CC BY 2.0; registration plate obscured)",
        "url": "https://commons.wikimedia.org/wiki/File:Volkswagen_Golf_GTI_Clubsport_S_(31059402673).jpg",
    },
    "commons-mk8": {
        "short": "Mk8 GTI photo",
        "short_es": "Foto Mk8 GTI",
        "kind": "photo",
        "label": "Wikimedia Commons, “File:Volkswagen Golf GTI (Mk VIII) Washington DC Metro Area, USA (1).jpg” (OWS Photography; Creative Commons CC BY 4.0)",
        "url": "https://commons.wikimedia.org/wiki/File:Volkswagen_Golf_GTI_(Mk_VIII)_Washington_DC_Metro_Area,_USA_(1).jpg",
    },
}

KIND_LABEL = {
    "vw": ("VW", "VW"),
    "press": ("Press", "Prensa"),
    "paper": ("Paper", "Artículo"),
    "photo": ("Photo Archive", "Archivo Fotográfico"),
}

HERO = {
    "kicker_en": "Cult Classics · CC.01 · Chassis Engineering & Powertrain",
    "kicker_es": "Clásicos de Culto · CC.01 · Ingeniería de Chasis y Tren Motriz",
    "title_en": "One Brief, Eight Answers",
    "title_es": "Un reto, ocho respuestas",
    "dek_en": "Fifty years of the Golf GTI (1976–2026), told one mechanical engineering move at a time.",
    "dek_es": "Cincuenta años del Golf GTI (1976–2026), contados decisión de ingeniería por decisión de ingeniería.",
    "reading_en": "22 min read",
    "reading_es": "24 min de lectura",
}

BRIEF_NOTE = {
    "en": "The “brief” in the title is our framing, not Volkswagen’s: make a sensible family hatchback properly quick "
          "without making it any less sensible. Across fifty years, engines, gearboxes, front differentials, and control "
          "software all changed—while the practical envelope stayed put.",
    "es": "El “reto” del título es una lectura nuestra, no de Volkswagen: hacer que un hatchback familiar y sensato "
          "sea rápido de verdad sin que deje de ser sensato. En cincuenta años cambiaron motores, cajas, diferenciales "
          "y software de control, mientras el envase práctico permaneció intacto.",
}

HERO_TRIBUTE = {
    "kicker_en": "In Honor of the Engineers, Designers & Drivers · EA195 to 2026",
    "kicker_es": "En honor a los ingenieros, diseñadores y pilotos · De EA195 a 2026",
    "architects_label_en": "1974–1976 EA195 Initiators & Leaders",
    "architects_label_es": "Iniciadores y Líderes EA195 (1974–1976)",
    "architects_en": "Anton Konrad (Press officer & secret-project co-founder) · Hermann Hablitzel (Board Member for Technology) · Toni Schmücker (Board Chairman, 1975 approval) · Herbert Schäfer (Chief Designer, golf-ball gear knob)",
    "architects_es": "Anton Konrad (jefe de prensa y cofundador del proyecto secreto) · Hermann Hablitzel (consejero de Tecnología) · Toni Schmücker (presidente, aprobación 1975) · Herbert Schäfer (jefe de Diseño, pomo tipo pelota de golf)",
    "makers_label_en": "Chassis Tuners, Powertrain & Testers",
    "makers_label_es": "Chasis, Motores y Pilotos de Prueba",
    "makers_en": "Wolfsburg development & MQB suspension engineers · Hans-Joachim Stuck (Mk6 chassis tuning) · sport auto Nordschleife test drivers Horst von Saurma & Christian Gebhardt · Clubsport S & EDITION 50 teams",
    "makers_es": "Equipos de desarrollo y chasis MQB en Wolfsburgo · Hans-Joachim Stuck (puesta a punto Mk6) · pilotos de prueba de sport auto en Nordschleife Horst von Saurma y Christian Gebhardt · equipos Clubsport S y EDITION 50",
    "src": ["vw-mk1-story", "vw-history", "wiki-nords"],
}

OPENING = [
    {
        "en": "Volkswagen’s own newsroom tells the beginning plainly. In 1974 about half a dozen people inside the company, "
              "among them the chief press officer of the day, Anton Konrad, started work on a sporty Golf that nobody had "
              "asked them for. Hermann Hablitzel, Board Member for Technology, kept the unofficial project alive and presented "
              "it to Board Chairman Toni Schmücker in March 1975 under development order EA195; chief designer Herbert Schäfer "
              "added the dimpled golf-ball gear knob before its September 1975 IAA debut and June 1976 German launch at 110 PS.",
        "es": "La sala de prensa de Volkswagen cuenta el comienzo sin adornos. En 1974, alrededor de media docena de personas "
              "dentro de la empresa, entre ellas el entonces jefe de prensa, Anton Konrad, empezaron a trabajar en un Golf "
              "deportivo que nadie les había pedido. Hermann Hablitzel, consejero de Tecnología, sostuvo el proyecto hasta "
              "presentarlo al presidente Toni Schmücker en marzo de 1975 como orden EA195; el jefe de diseño Herbert Schäfer "
              "sumó la perilla de pelota de golf antes del estreno en septiembre de 1975 y el lanzamiento alemán en junio de 1976 con 110 PS.",
        "src": ["vw-mk1-story", "vw-history"],
    },
    {
        "en": "The plan was modest: about 5,000 cars to recover tooling costs. Volkswagen’s history page puts the final count "
              "of the first generation at 461,690. Everything that follows—from inline historical photographs to a 3D WebGL2 "
              "MacPherson/VAQ transaxle bench and 15 Scite-checked vehicle-dynamics papers—traces how eight generations solved "
              "the same physics limits of power, grip, mass, and stability on a front-wheel-drive compact platform.",
        "es": "El plan era modesto: unos 5,000 autos para amortizar el herramental. La página de historia de Volkswagen cifra la "
              "producción final de la primera generación en 461,690. Todo lo que sigue —desde fotografías históricas en línea hasta "
              "un banco 3D en WebGL2 y 15 artículos de dinámica vehicular verificados en Scite— traza cómo ocho generaciones resolvieron "
              "los mismos límites físicos de potencia, agarre, masa y estabilidad en un compacto de tracción delantera.",
        "src": ["vw-history", "cronin1981"],
    },
]

# ---------------------------------------------------------------------------------------------------------------
# Five-Era Interactive Engineering Relay
# ---------------------------------------------------------------------------------------------------------------
RELAY_TEXT = {
    "kicker_en": "Five Engineering Eras · 1974–2026 Continuity Observatory",
    "kicker_es": "Cinco Eras de Ingeniería · Observatorio de Continuidad 1974–2026",
    "title_en": "How Fifty Years Evolved From 810 kg Restraint to Software Coordination",
    "title_es": "Cómo cincuenta años evolucionaron de 810 kg de ligereza a la coordinación por software",
    "intro_en": "Select each era from the 1974 EA195 side project to 2026 software integration: see the engineering constraint that defined the decade, the mechanical answer adopted, and how earlier cabin craftsmanship endured beside modern electronics.",
    "intro_es": "Selecciona cada etapa desde el proyecto EA195 de 1974 hasta la integración electrónica de 2026: explora la restricción física dominante, la respuesta mecánica adoptada y cómo la identidad del habitáculo convivió con la evolución del chasis.",
}

GENERATIONS_RELAY = [
    {
        "id": "era-1",
        "era": "1974–1983",
        "name_en": "1 · Lightness & Injection",
        "name_es": "1 · Ligereza e Inyección",
        "lead_en": "Anton Konrad, Hermann Hablitzel, Herbert Schäfer (EA195)",
        "lead_es": "Anton Konrad, Hermann Hablitzel, Herbert Schäfer (EA195)",
        "challenge_en": "Deliver genuine highway pace out of an upright three-door economy shell without luxury-sedan engine displacement or weight.",
        "challenge_es": "Lograr ritmo real de carretera en una carrocería compacta de tres puertas sin cilindrada ni masa de sedán grande.",
        "gift_en": "Keep base mass at 810 kg, fit an Audi-sourced 1.6 L 110 PS fuel-injected engine, drop springs 10 mm front / 20 mm rear with anti-roll bars, and sign it with tartan upholstery and the golf-ball knob.",
        "gift_es": "Mantener el peso base en 810 kg, montar el motor Audi 1.6 L de inyección con 110 PS, rebajar 10 mm adelante / 20 mm atrás con estabilizadoras, y firmarlo con tapicería escocesa y pomo de pelota de golf.",
        "src": ["vw-mk1-story", "vw-mk1"],
        "media_id": "photo-mk7-interior",
    },
    {
        "id": "era-2",
        "era": "1984–1997",
        "name_en": "2 · Breathing & Safety",
        "name_es": "2 · Respiración y Seguridad",
        "lead_en": "Mk2 (16V & G60) → Mk3 (2.0 L, 16V & TDI)",
        "lead_es": "Mk2 (16V y G60) → Mk3 (2.0 L, 16V y TDI)",
        "challenge_en": "Regulated three-way catalytic converters shaved top-end breathing (139 PS down to 129 PS on Mk2 16V), while heavier crash structures demanded low-end punch.",
        "challenge_es": "Los convertidores catalíticos regulados restaron potencia alta (de 139 PS a 129 PS en Mk2 16V), mientras las estructuras de seguridad más pesadas exigían mejor llenado.",
        "gift_en": "Moved from two-valve heads to four-valve pent-roof heads (16V), briefly tested belt-driven G-Lader scroll compression (160 PS G60), and introduced ABS brakes alongside heavier Mk3 safety shells.",
        "gift_es": "Paso de dos a cuatro válvulas por cilindro (16V), ensayo breve con compresor espiral G-Lader por banda (160 PS en G60) y llegada de ABS en la plataforma Mk3.",
        "src": ["vw-history", "hu2016"],
    },
    {
        "id": "era-3",
        "era": "1998–2008",
        "name_en": "3 · Boost & Dual Clutches",
        "name_es": "3 · Turbo y Doble Embrague",
        "lead_en": "Mk4 1.8T / VR5 → Mk5 2.0 TFSI & 6-speed DSG",
        "lead_es": "Mk4 1.8T / VR5 → Mk5 2.0 TFSI y DSG de 6 vels.",
        "challenge_en": "Engine downsizing needed exhaust-driven boost and direct injection for efficiency, yet manual upshifts still interrupted front-wheel traction and dumped boost pressure.",
        "challenge_es": "El downsizing requería sobrealimentación por escape e inyección directa para eficiencia, pero los cambios manuales interrumpían la tracción delantera.",
        "gift_en": "Adopted turbocharged 1.8 L and 2.0 L 200 PS petrol powerplants plus coaxial 6-speed DSG wet dual clutches (cutting VW’s 0–100 km/h figure from 7.2 s manual to 6.9 s DSG).",
        "gift_es": "Adopción de motores gasolina turbo de 1.8 L y 2.0 L con 200 PS junto a la caja coaxial DSG de 6 velocidades en baño de aceite (reduciendo el 0–100 km/h declarado por VW de 7.2 s manual a 6.9 s DSG).",
        "src": ["vw-history", "vw-mk5", "galvagno2011", "zhao1999"],
    },
    {
        "id": "era-4",
        "era": "2009–2019",
        "name_en": "4 · Front-Axle Torque Vectoring",
        "name_es": "4 · Vectorización en Eje Delantero",
        "lead_en": "Mk6 XDS (Hans-Joachim Stuck tuning) → Mk7 MQB, VAQ & Clubsport S",
        "lead_es": "Mk6 XDS (puesta a punto Stuck) → Mk7 MQB, VAQ y Clubsport S",
        "challenge_en": "Above 200 PS at the front tyres, cornering weight transfer unloads the inside front tyre so an open differential wastes drive into inside wheelspin.",
        "challenge_es": "Por encima de 200 PS al eje delantero, la transferencia lateral descarga la rueda interior y un diferencial abierto pierde tracción en patinaje interno.",
        "gift_en": "Progressed from brake-based inside-wheel clamping (XDS) to an electro-hydraulic multi-plate front differential lock (up to 1,600 Nm), MQB weight cuts up to 42 kg, progressive 2.1-turn steering, and Clubsport S aluminium unsprung reductions (7:49.21 VW record / 7:57 sport auto).",
        "gift_es": "Evolución de frenado interior (XDS) a bloqueo electrohidráulico multidisco (hasta 1,600 Nm), reducción MQB de hasta 42 kg, dirección progresiva de 2.1 vueltas y aligeramiento de aluminio del Clubsport S (7:49.21 récord VW / 7:57 sport auto).",
        "src": ["vw-mk7-chassis", "vw-cs-s", "kakalis2008", "wiki-nords"],
    },
    {
        "id": "era-5",
        "era": "2020–2026",
        "name_en": "5 · Software Fusion & Edition 50",
        "name_es": "5 · Fusión por Software y Edition 50",
        "lead_en": "Mk8 Vehicle Dynamics Manager (245 → 265 PS → 325 PS Edition 50)",
        "lead_es": "Mk8 Gestor de Dinámica Vehicular (245 → 265 PS → 325 PS Edition 50)",
        "challenge_en": "By 2020 the brake-based lock, clutch-pack e-diff, and adaptive dampers already existed independently—running on separate silos that could fight each other near the limit.",
        "challenge_es": "En 2020 ya existían por separado XDS+, el diferencial de embragues y los amortiguadores DCC, pero operaban como subsistemas aislados cerca del límite.",
        "gift_en": "A unified Vehicle Dynamics Manager coordinates XDS+, the front lock, and DCC dampers in real time, rising to 265 PS standard (2024) and the 325 PS GTI EDITION 50 announced for 2026.",
        "gift_es": "Un Gestor de Dinámica Vehicular unificado coordina XDS+, el bloqueo delantero y DCC en tiempo real, escalando a 265 PS de serie en 2024 y al GTI EDITION 50 de 325 PS anunciado para 2026.",
        "src": ["vw-history", "trachtler2004", "rubin2015"],
    },
]

# ---------------------------------------------------------------------------------------------------------------
# Archival Wikimedia Commons Photographs (9 items: PD / CC0 / CC BY — ZERO ShareAlike)
# ---------------------------------------------------------------------------------------------------------------
PHOTOS = [
    {
        "id": "photo-mk1",
        "kind": "photo",
        "era": "1976–1983 · Mk1",
        "era_es": "1976–1983 · Mk1",
        "license": "CC BY 2.0 · Riley (plate obscured)",
        "image": "images/golf-gti/photo-mk1-gti.jpg",
        "width": 1280,
        "height": 960,
        "alt_en": "Silver 1982 Mk1 Volkswagen Golf GTI three-door hatchback seen in right three-quarter profile showing the red grille surround, twin headlamps, front spoiler lip, black wheel-arch extensions, and flat beltline.",
        "alt_es": "Volkswagen Golf GTI Mk1 plateado de 1982 en tres puertas mostrando el marco rojo de parrilla, faros dobles, spoiler delantero, pasos de rueda negros y cintura rectilínea.",
        "caption_en": "Generation 1 photograph (1982 Mk1): Giugiaro’s upright three-door silhouette fitted with the GTI’s black wheel-arch extensions, front chin spoiler, and red grille border (Riley, CC BY 2.0; plate obscured).",
        "caption_es": "Fotografía Generación 1 (Mk1 1982): silueta rectilínea de tres puertas con molduras negras en arcos, spoiler delantero y filo rojo en parrilla (Riley, CC BY 2.0; placa difuminada).",
        "src": ["commons-mk1", "vw-mk1"],
    },
    {
        "id": "photo-mk7-interior",
        "kind": "photo",
        "era": "Cabin Lineage · Plaid & Drivers Cockpit",
        "era_es": "Linaje de Cabina · Tela Escocesa y Mandos",
        "license": "Public Domain · TTTNIS",
        "image": "images/golf-gti/photo-mk7-interior.jpg",
        "width": 1280,
        "height": 747,
        "alt_en": "Modern Golf GTI cabin photograph showing tartan woven sports seats with red stitching beside a flat-bottom perforated leather steering wheel and alloy pedals.",
        "alt_es": "Fotografía del habitáculo del Golf GTI mostrando asientos deportivos de tela escocesa con costuras rojas junto al volante plano y pedales metálicos.",
        "caption_en": "Interior craft continuity: five decades after the 1976 launch specification, check-patterned woven cloth bolsters and red seam accents remain hallmarks of the driver-focused cockpit (TTTNIS, Public Domain).",
        "caption_es": "Continuidad del oficio interior: décadas después de la especificación de 1976, los asientos con tejido escocés y costuras rojas permanecen en el puesto de conducción (TTTNIS, Dominio público).",
        "src": ["commons-mk7-interior", "vw-mk1"],
    },
    {
        "id": "photo-mk2",
        "kind": "photo",
        "era": "1984–1991 · Mk2",
        "era_es": "1984–1991 · Mk2",
        "license": "CC0 1.0 · Guillaume Vachey (plate obscured)",
        "image": "images/golf-gti/photo-mk2-gti.jpg",
        "width": 1280,
        "height": 928,
        "alt_en": "Red three-door Mk2 Volkswagen Golf GTI showing twin auxiliary inner driving lamps inside the red-framed grille, black wheel-arch trims, and ventilated steel-look rims.",
        "alt_es": "Volkswagen Golf GTI Mk2 rojo de tres puertas mostrando los cuatro faros frontales dentro del marco rojo, arcos negros y proporciones ensanchadas.",
        "caption_en": "Generation 2 photograph (Mk2): larger body with twin auxiliary grille lamps and familiar black fender trim, housing the 16V pent-roof head and later 160 PS G60 scroll compressor (Guillaume Vachey, CC0; plate obscured).",
        "caption_es": "Fotografía Generación 2 (Mk2): carrocería ampliada con doble faro en parrilla que recibió la culata 16V y el compresor espiral G60 de 160 PS (Guillaume Vachey, CC0; placa difuminada).",
        "src": ["commons-mk2", "vw-history"],
    },
    {
        "id": "photo-mk3",
        "kind": "photo",
        "era": "1991–1997 · Mk3",
        "era_es": "1991–1997 · Mk3",
        "license": "CC0 1.0 · Charles",
        "image": "images/golf-gti/photo-mk3-gti.jpg",
        "width": 1280,
        "height": 840,
        "alt_en": "Exhibition-hall photograph of a 1996 Mk3 Volkswagen Golf GTI in deep violet-black metallic with twin tailpipes, multi-spoke alloy wheels, and a GOLF III GTI show plate.",
        "alt_es": "Fotografía de exposición de un Volkswagen Golf GTI Mk3 de 1996 con doble escape, rines multirradio y placa de exhibición GOLF III GTI.",
        "caption_en": "Generation 3 exhibition photograph (1996 Mk3): softer aerodynamic corners, crash-structure stiffness, twin exhaust tips, and the first 20-year GTI anniversary era (Charles, CC0 1.0).",
        "caption_es": "Fotografía de exhibición Generación 3 (Mk3 1996): formas redondeadas, mayor rigidez estructural, doble salida de escape y primer modelo de aniversario 20 años (Charles, CC0 1.0).",
        "src": ["commons-mk3", "vw-history"],
    },
    {
        "id": "photo-mk4",
        "kind": "photo",
        "era": "1998–2003 · Mk4",
        "era_es": "1998–2003 · Mk4",
        "license": "CC0 1.0 · Charles",
        "image": "images/golf-gti/photo-mk4-gti.jpg",
        "width": 1280,
        "height": 811,
        "alt_en": "Exhibition-hall photograph of a dark indigo 2002 Mk4 Volkswagen Golf GTI viewed from the rear three-quarter angle with sculpted C-pillars, twin tailpipes, and a GOLF IV GTI show plate.",
        "alt_es": "Fotografía de exposición de un Volkswagen Golf GTI Mk4 de 2002 azul oscuro desde tres cuartos trasero con pilar C ancho y placa GOLF IV GTI.",
        "caption_en": "Generation 4 exhibition photograph (2002 Mk4): thick C-pillar silhouette housing the 150–180 PS 1.8 L turbocharged inline-four that anchored forced induction (Charles, CC0 1.0).",
        "caption_es": "Fotografía de exhibición Generación 4 (Mk4 2002): silueta de pilar C sólido que albergó el bloque turbo 1.8 L de 150 a 180 PS con el que arrancó la era turbo (Charles, CC0 1.0).",
        "src": ["commons-mk4", "vw-history"],
    },
    {
        "id": "photo-mk5",
        "kind": "photo",
        "era": "2004–2008 · Mk5",
        "era_es": "2004–2008 · Mk5",
        "license": "CC0 1.0 · Tokumeigakarinoaoshima",
        "image": "images/golf-gti/photo-mk5-gti.jpg",
        "width": 1280,
        "height": 941,
        "alt_en": "Front three-quarter photograph of a white Mk5 Volkswagen Golf GTI showing the signature black honeycomb center mask framed by a thin red trim pinstripe.",
        "alt_es": "Fotografía tres cuartos delantera de un Volkswagen Golf GTI Mk5 blanco mostrando la máscara central en panal negro enmarcada por el filo rojo.",
        "caption_en": "Generation 5 photograph (Mk5): glossy black honeycomb front grille reviving the red surround above the 200 PS 2.0 TFSI and optional 6-speed DSG dual-clutch transmission (Tokumeigakarinoaoshima, CC0 1.0).",
        "caption_es": "Fotografía Generación 5 (Mk5): parrilla en panal negro con ribete rojo sobre el motor 2.0 TFSI de 200 PS y la caja DSG de 6 velocidades opcional (Tokumeigakarinoaoshima, CC0 1.0).",
        "src": ["commons-mk5", "vw-mk5"],
    },
    {
        "id": "photo-mk6",
        "kind": "photo",
        "era": "2009–2012 · Mk6",
        "era_es": "2009–2012 · Mk6",
        "license": "CC BY 4.0 · OWS Photography (plate obscured)",
        "image": "images/golf-gti/photo-mk6-gti.jpg",
        "width": 1280,
        "height": 1024,
        "alt_en": "Elevated front view photograph of a black Mk6 Volkswagen Golf GTI turning on city asphalt with twin horizontal red grille bars and LED daytime headlamps.",
        "alt_es": "Fotografía cenital delantera de un Volkswagen Golf GTI Mk6 negro girando sobre asfalto con doble línea roja en parrilla y ópticas diurnas.",
        "caption_en": "Generation 6 photograph (Mk6): twin red grille ribs and 210 PS output paired with standard XDS electronic brake-based torque vectoring tuned with Hans-Joachim Stuck (OWS Photography, CC BY 4.0; plate obscured).",
        "caption_es": "Fotografía Generación 6 (Mk6): doble filete rojo en parrilla y 210 PS con bloqueo electrónico por freno XDS de serie afinado con Hans-Joachim Stuck (OWS Photography, CC BY 4.0; placa difuminada).",
        "src": ["commons-mk6", "vw-history"],
    },
    {
        "id": "photo-clubsport-s",
        "kind": "photo",
        "era": "2013–2019 · Mk7 Clubsport S",
        "era_es": "2013–2019 · Mk7 Clubsport S",
        "license": "CC BY 2.0 · Adam Court (plate obscured)",
        "image": "images/golf-gti/photo-mk7-clubsport-s.jpg",
        "width": 1280,
        "height": 853,
        "alt_en": "Three-door black Mk7 Volkswagen Golf GTI Clubsport S at circuit paddock showing red brake calipers, multi-spoke lightweight wheels, and split rear roof spoiler.",
        "alt_es": "Volkswagen Golf GTI Clubsport S Mk7 de tres puertas negro en paddock mostrando pinzas rojas de freno, rines multirradio ligeros y alerón trasero bipartido.",
        "caption_en": "Generation 7 photograph (Mk7 Clubsport S): lightweight three-door MQB specification combining a manual box, aluminium front subframe and brake bells, 310 PS, and the electro-hydraulic front lock for 7:49.21 on the Nordschleife per VW (Adam Court, CC BY 2.0; plate obscured).",
        "caption_es": "Fotografía Generación 7 (Mk7 Clubsport S): versión aligerada MQB de tres puertas con caja manual, subchasis y portafrenos de aluminio, 310 PS y bloqueo delantero electrohidráulico para 7:49.21 según VW (Adam Court, CC BY 2.0; placa difuminada).",
        "src": ["commons-clubsport-s", "vw-cs-s", "vw-mk7-chassis"],
    },
    {
        "id": "photo-mk8",
        "kind": "photo",
        "era": "2020–2026 · Mk8",
        "era_es": "2020–2026 · Mk8",
        "license": "CC BY 4.0 · OWS Photography",
        "image": "images/golf-gti/photo-mk8-gti.jpg",
        "width": 1280,
        "height": 853,
        "alt_en": "Wet-track panning photograph of a Moonstone Grey Mk8 Volkswagen Golf GTI loaded onto its outside front tyre showing the full-width illuminated grille light bar and red brake caliper.",
        "alt_es": "Fotografía en pista mojada de un Volkswagen Golf GTI Mk8 gris apoyado en el neumático delantero exterior con franja iluminada frontal y pinza roja.",
        "caption_en": "Generation 8 wet-pad photograph (Mk8): loaded outside front tyre under lateral cornering while the Vehicle Dynamics Manager coordinates XDS+, the front lock, and optional adaptive dampers—scaling from 245 PS to 265 PS (2024) and 325 PS in the Edition 50 (OWS Photography, CC BY 4.0).",
        "caption_es": "Fotografía en pista húmeda Generación 8 (Mk8): neumático delantero exterior en apoyo mientras el Gestor de Dinámica Vehicular coordina XDS+, el bloqueo delantero y DCC desde 245 PS hasta 265 PS (2024) y 325 PS en Edition 50 (OWS Photography, CC BY 4.0).",
        "src": ["commons-mk8", "vw-history"],
    },
]

# ---------------------------------------------------------------------------------------------------------------
# Conceptual AI-Assisted Engineering Studio Plates & Frontispiece (5 items: zero EXIF, zero baked-in text)
# Explicit Law 8 disclosure in BOTH alt and caption (EN + ES-MX).
# ---------------------------------------------------------------------------------------------------------------
PLATES = [
    {
        "id": "plate-1974-sketch",
        "kind": "render",
        "era": "Frontispiece Tribute · 1974 EA195",
        "era_es": "Lámina Frontal · Proyecto EA195 (1974)",
        "image": "images/golf-gti/gti-1974-wolfsburg-ink-sketch.jpg",
        "width": 1280,
        "height": 714,
        "alt_en": "Conceptual visualization in 1970s sepia ink and graphite drafting-board style imagining orthogonal three-door hatchback silhouettes beside brass dividers, red tartan fabric, a golf-ball shift knob, and calipers (artistic tribute, not an archival VW drawing).",
        "alt_es": "Visualización conceptual en tinta sepia y grafito que imagina alzados de un hatchback tres puertas de 1974 junto a un compás de latón, tela escocesa roja, perilla de pelota de golf y calibrador vernier (homenaje artístico, no es un plano original de VW).",
        "caption_en": "Conceptual visualization: hand-sketched frontispiece tribute honoring the 1974 Wolfsburg EA195 initiators (Konrad, Hablitzel, Schmücker, Schäfer), orthographic packaging, tartan wool, and golf-ball shifter (artistic tribute, not an archival blueprint).",
        "caption_es": "Visualización conceptual: lámina frontal a pluma en homenaje a los iniciadores del proyecto EA195 de 1974 en Wolfsburgo (Konrad, Hablitzel, Schmücker, Schäfer), su proporción en alzado, la tela escocesa y la perilla esférica (homenaje artístico, no es plano de archivo).",
        "src": ["vw-mk1-story", "vw-mk1"],
    },
    {
        "id": "plate-turbo-gdi",
        "kind": "render",
        "era": "Engine Cutaway · GDI + Turbo",
        "era_es": "Corte de Motor · Inyección Directa y Turbo",
        "image": "images/golf-gti/gti-plate-turbo-gdi-cutaway.jpg",
        "width": 1280,
        "height": 714,
        "alt_en": "Conceptual visualization of a studio cutaway inline-four cylinder head showing an optical spray chamber for direct fuel atomization beside a sectioned turbocharger turbine/compressor scroll and intercooler fin core (illustrative cutaway, not a VW OEM CAD drawing).",
        "alt_es": "Visualización conceptual de un corte de laboratorio de una culata de cuatro cilindros con cámara óptica de inyección directa junto a un turbocompresor seccionado y núcleo de intercooler (corte ilustrativo, no es CAD oficial de VW).",
        "caption_en": "Conceptual visualization imagining gasoline direct-injection evaporative charge cooling inside the cylinder beside an exhaust-driven turbine and intercooler core studied in Zhao et al. (1999) and Hu et al. (2015) (illustrative studio model, not an OEM Golf teardown).",
        "caption_es": "Visualización conceptual que imagina el enfriamiento evaporativo por inyección directa de gasolina junto a la turbina de escape y el intercooler analizados en Zhao et al. (1999) y Hu et al. (2015) (modelo ilustrativo de estudio, no es despiece de fábrica).",
        "src": ["zhao1999", "hu2015"],
    },
    {
        "id": "plate-dsg-cutaway",
        "kind": "render",
        "era": "Transaxle Cutaway · Coaxial Dual Clutch",
        "era_es": "Corte de Caja · Doble Embrague Coaxial",
        "image": "images/golf-gti/gti-plate-dsg-coaxial-cutaway.jpg",
        "width": 1280,
        "height": 714,
        "alt_en": "Conceptual visualization of a sectioned coaxial dual-clutch gearbox on dark stone showing nested inner and outer input shafts, wet multi-plate friction clutches, helical gears, and brass synchronizers (artistic studio cutaway, not a VW workshop manual diagram).",
        "alt_es": "Visualización conceptual de una caja de doble embrague coaxial seccionada mostrando flechas concéntricas interior y exterior, paquetes húmedos multidisco, engranes helicoidales y sincronizadores de bronce (corte ilustrativo, no es manual de taller de VW).",
        "caption_en": "Conceptual visualization imagining a sectioned coaxial dual-clutch transaxle—solid odd-gear shaft inside a hollow even-gear shaft with interleaved wet clutches modeled in Galvagno et al. (2011) and Brancati et al. (2023) (illustrative cutaway, not a measured VW DSG drawing).",
        "caption_es": "Visualización conceptual que imagina una caja de doble embrague coaxial seccionada: flecha interior para nones dentro de una flecha hueca para pares con embragues húmedos analizados en Galvagno et al. (2011) y Brancati et al. (2023) (corte ilustrativo, no es plano VW).",
        "src": ["galvagno2011", "brancati2023", "vw-mk5"],
    },
    {
        "id": "plate-vaq-corner",
        "kind": "render",
        "era": "Front Axle · MacPherson + VAQ Lock",
        "era_es": "Eje Delantero · MacPherson y Bloqueo VAQ",
        "image": "images/golf-gti/gti-plate-vaq-front-corner.jpg",
        "width": 1280,
        "height": 714,
        "alt_en": "Conceptual visualization of a studio cutaway pairing a MacPherson coil-over strut, lower aluminum wishbone, CV driveshaft, and red caliper with a sectioned bevel differential and multi-plate clutch pack (illustrative studio plate, not an OEM service manual).",
        "alt_es": "Visualización conceptual de corte en banco reuniendo un puntal MacPherson con resorte helicoidal, horquilla de aluminio, flecha homocinética y pinza roja junto a un diferencial de engranes cónicos y paquete multidisco (lámina ilustrativa, no es manual de servicio).",
        "caption_en": "Conceptual visualization pairing a MacPherson strut corner and vented brake disc with a sectioned multi-plate differential clutch pack whose 1,600 Nm max lock transfers drive torque to the heavily loaded outside front wheel (illustrative plate; exact MODEL torque math lives in Part VI).",
        "caption_es": "Visualización conceptual que reúne un puntal MacPherson y disco ventilado junto a un paquete de embragues multidisco cuyo par de bloqueo máximo de 1,600 Nm traslada tracción a la rueda exterior cargada (lámina ilustrativa; el cálculo MODELO exacto vive en la Parte VI).",
        "src": ["cronin1981", "kakalis2008", "vw-mk7-chassis"],
    },
    {
        "id": "plate-vdm-apex",
        "kind": "render",
        "era": "Chassis Dynamics · Apex Equilibrium",
        "era_es": "Dinámica de Chasis · Equilibrio en Ápice",
        "image": "images/golf-gti/gti-plate-vdm-chassis-dynamics.jpg",
        "width": 1280,
        "height": 714,
        "alt_en": "Conceptual visualization imagining an unbadged white-silver five-door compact hatchback compressing its outside front tyre onto red-and-white circuit curbing at dusk with a glowing vented front brake disc (artistic impression, not a telemetry frame).",
        "alt_es": "Visualización conceptual que imagina un hatchback compacto de cinco puertas sin emblemas cargando su neumático delantero exterior sobre el piano rojo y blanco de un circuito al atardecer con disco delantero incandescente (impresión artística, no es telemetría).",
        "caption_en": "Conceptual visualization imagining coupled lateral weight transfer, front tyre traction ellipse utilization, and coordinated brake/e-diff yaw stabilization near an apex curb (artistic impression, not an instrumented lap trace).",
        "caption_es": "Visualización conceptual que imagina la transferencia lateral de carga, el círculo de fricción del neumático delantero y la estabilización coordinada de guiñada sobre un ápice de circuito (impresión artística, no es registro de telemetría).",
        "src": ["pacejka1992", "abe2001", "trachtler2004"],
    },
]

VISUAL_GALLERY_TEXT = {
    "kicker_en": "Complete Visual Archive · 9 Commons Photos + 5 Studio Cutaways",
    "kicker_es": "Archivo Visual Completo · 9 Fotos de Commons + 5 Láminas de Banco",
    "title_en": "Inspect Every Generation Photograph & Mechanical Cutaway Fullscreen",
    "title_es": "Explora cada fotografía generacional y lámina de corte a pantalla completa",
    "intro_en": "Filter between nine verified Wikimedia Commons photographs (PD / CC0 / CC BY; private street plates obscured) across Mk1–Mk8 plus five clearly labeled conceptual studio illustrations, or open any frame inside the zero-jump fullscreen plate viewer.",
    "intro_es": "Filtra entre nueve fotografías verificadas de Wikimedia Commons (PD / CC0 / CC BY; placas particulares difuminadas) desde Mk1 hasta Mk8 más cinco visualizaciones conceptuales debidamente rotuladas, o abre cualquier lámina en el visor a pantalla completa.",
    "all_en": "All 14 Media",
    "all_es": "Las 14 vistas",
    "photos_en": "Archival & Track Photos (9)",
    "photos_es": "Fotos de Archivo y Pista (9)",
    "renders_en": "Conceptual Cutaways (5)",
    "renders_es": "Láminas Conceptuales (5)",
    "badge_photo_en": "COMMONS PHOTO",
    "badge_photo_es": "FOTO ARCHIVO",
    "badge_render_en": "CONCEPTUAL RENDER · AI-ASSISTED",
    "badge_render_es": "VISUALIZACIÓN CONCEPTUAL · IA",
}

# ---------------------------------------------------------------------------------------------------------------
# Generation cards (one card per generation with inline archival photo + factory/published spec plate)
# ---------------------------------------------------------------------------------------------------------------
CARDS = [
    {
        "id": "mk1", "gen": "Mk1", "years": "1976–1983",
        "move_en": "Light car, injected engine, firm chassis",
        "move_es": "Auto ligero, motor de inyección, chasis firme",
        "body_en": "VW’s archive describes a 1.6-litre injection engine borrowed from Audi, a base weight of 810 kg, and a "
                   "chassis set 10 mm lower at the front and 20 mm lower at the rear, with anti-roll bars at both ends. "
                   "The details that became shorthand for the badge are in the same entry: a red surround on the grille, "
                   "tartan sports seats and a golf-ball gear knob. The archive also notes, with a wink, that the "
                   "car’s 175/70 HR 13 tyres carried a speed rating implying more than 180 km/h. That is a tyre rating, "
                   "not a measured top speed.",
        "body_es": "El archivo de VW describe un motor de inyección de 1.6 litros tomado de Audi, un peso base de 810 kg y "
                   "un chasis 10 mm más bajo adelante y 20 mm atrás, con barras estabilizadoras en ambos ejes. Los "
                   "detalles que se volvieron sinónimo del emblema están en la misma ficha: un marco rojo en la parrilla, "
                   "asientos deportivos de tela escocesa y una palanca de cambios con forma de pelota de golf. El archivo "
                   "también apunta, con un guiño, que las llantas 175/70 HR 13 tenían un índice de velocidad que "
                   "implicaba más de 180 km/h. Es un índice de la llanta, no una prueba independiente.",
        "inline_media": "photo-mk1",
        "plate": [
            ("Engine", "Motor", "1.6 L injection, from Audi", "vw-mk1"),
            ("Output at launch", "Potencia inicial", "110 PS", "vw-history"),
            ("Base weight", "Peso base", "810 kg", "vw-mk1"),
            ("Lowered", "Altura reducida", "10 mm front / 20 mm rear", "vw-mk1"),
        ],
    },
    {
        "id": "mk2", "gen": "Mk2", "years": "1984–1991",
        "move_en": "Breathing: sixteen valves, then a supercharger",
        "move_es": "Respirar mejor: dieciséis válvulas y luego un compresor",
        "body_en": "The second generation started at 112 PS. In 1986 a 16-valve engine arrived: VW lists 139 PS without a "
                   "regulated catalytic converter and 129 PS with one, a small, honest record of what emissions hardware "
                   "cost in that era. In 1990 the G60 added a scroll-type “G-Lader” supercharger for 160 PS. VW’s history "
                   "page also notes that ABS was offered as an option for the first time.",
        "body_es": "La segunda generación arrancó con 112 PS. En 1986 llegó un motor de 16 válvulas: VW indica 139 PS sin "
                   "catalizador regulado y 129 PS con él, un registro pequeño y honesto de lo que costaba entonces el "
                   "control de emisiones. En 1990 el G60 sumó un compresor de tipo espiral “G-Lader” para 160 PS. La "
                   "página de historia de VW también señala que el ABS se ofreció como opción por primera vez.",
        "inline_media": "photo-mk2",
        "plate": [
            ("Output at launch", "Potencia inicial", "112 PS", "vw-history"),
            ("16V (1986)", "16V (1986)", "139 PS · 129 PS with catalyst", "vw-history"),
            ("G60 (1990)", "G60 (1990)", "Scroll supercharger, 160 PS", "vw-history"),
        ],
    },
    {
        "id": "mk3", "gen": "Mk3", "years": "1991–1997",
        "move_en": "Heavier, safer, and a diesel with the badge",
        "move_es": "Más pesado, más seguro y un diésel con el emblema",
        "body_en": "The third generation opened with a 2.0-litre two-valve engine at 115 PS, and a 16-valve version followed "
                   "at 150 PS (VW pages give 1992 and 1993 for it, so we print neither). In 1996 the badge went onto a "
                   "110 PS turbodiesel, and the “20 Years of GTI” edition became, in VW’s words, the first anniversary "
                   "model in GTI history.",
        "body_es": "La tercera generación abrió con un motor de 2.0 litros y dos válvulas por cilindro de 115 PS, y después "
                   "llegó una versión de 16 válvulas con 150 PS (las páginas de VW dan 1992 y 1993, así que no imprimimos "
                   "ninguna fecha). En 1996 el emblema llegó a un turbodiésel de 110 PS, y la edición “20 años de GTI” "
                   "fue, según VW, el primer modelo de aniversario en la historia del GTI.",
        "inline_media": "photo-mk3",
        "plate": [
            ("Output at launch", "Potencia inicial", "2.0 L 8V, 115 PS", "vw-history"),
            ("16V", "16V", "150 PS", "vw-history"),
            ("Turbodiesel (1996)", "Turbodiésel (1996)", "110 PS", "vw-history"),
        ],
    },
    {
        "id": "mk4", "gen": "Mk4", "years": "1998–2003",
        "move_en": "The turbo era starts",
        "move_es": "Empieza la era turbo",
        "body_en": "VW lists a 1.8-litre turbocharged petrol engine at 150 PS for the fourth generation, beside a 2.3-litre "
                   "five-cylinder, also at 150 PS, that rose to 170 PS in 2000, and turbodiesels from 110 PS to 150 PS. "
                   "Model names varied by market, so read that list as VW’s, not as one country’s price sheet. The "
                   "2001 “25 Years of the GTI” edition used a 180 PS turbocharged engine.",
        "body_es": "VW enumera para la cuarta generación un motor de gasolina turbo de 1.8 litros con 150 PS, junto a un "
                   "cinco cilindros de 2.3 litros, también de 150 PS, que subió a 170 PS en 2000, y turbodiésel de 110 PS a "
                   "150 PS. Los nombres de versión cambiaban según el mercado, así que esa lista es la de VW, no la de "
                   "un solo país. La edición “25 años del GTI” de 2001 usó un motor turbo de 180 PS.",
        "inline_media": "photo-mk4",
        "plate": [
            ("Turbo petrol", "Gasolina turbo", "1.8 L, 150 PS", "vw-history"),
            ("Five-cylinder", "Cinco cilindros", "2.3 L, 150 → 170 PS", "vw-history"),
            ("25 Years (2001)", "25 años (2001)", "180 PS turbo", "vw-history"),
        ],
    },
    {
        "id": "mk5", "gen": "Mk5", "years": "2004–2008",
        "move_en": "Two clutches",
        "move_es": "Dos embragues",
        "body_en": "Shown at the Paris Motor Show in September 2004, the fifth generation used a 2.0-litre turbocharged "
                   "engine at 200 PS. VW offered an optional 6-speed direct-shift gearbox (DSG) and quotes 0–100 km/h in "
                   "6.9 s with it against 7.2 s with the manual. The gearbox bench and 3D cutaway below show why two "
                   "coaxial clutches keep wheel torque continuous across upshifts.",
        "body_es": "Presentada en el Salón de París en septiembre de 2004, la quinta generación usó un motor turbo de 2.0 "
                   "litros con 200 PS. VW ofreció como opción una caja de doble embrague de 6 velocidades (DSG) y cita "
                   "0–100 km/h en 6.9 s con ella frente a 7.2 s con la manual. El banco y el modelo 3D de abajo muestran "
                   "cómo dos embragues coaxiales mantienen continuo el par al neumático durante cada cambio.",
        "inline_media": "photo-mk5",
        "plate": [
            ("Engine", "Motor", "2.0 L turbo, 200 PS", "vw-history"),
            ("Gearbox option", "Caja opcional", "6-speed DSG", "vw-mk5"),
            ("0–100 km/h (VW)", "0–100 km/h (VW)", "7.2 s manual · 6.9 s DSG", "vw-history"),
        ],
    },
    {
        "id": "mk6", "gen": "Mk6", "years": "2009–2012",
        "move_en": "Brakes as a differential",
        "move_es": "Los frenos como diferencial",
        "body_en": "The sixth generation made 210 PS. VW says it was the first GTI with the XDS electronic differential lock "
                   "as standard, and that Hans-Joachim Stuck had a hand in the chassis tuning. XDS does not lock "
                   "anything mechanically: it brakes the inside front wheel so the open differential’s equal halves allow "
                   "the loaded outside tyre to hold more drive.",
        "body_es": "La sexta generación tenía 210 PS. VW dice que fue el primer GTI con el bloqueo electrónico de "
                   "diferencial XDS de serie, y que Hans-Joachim Stuck participó en la puesta a punto del chasis. El XDS "
                   "no bloquea nada mecánicamente: frena la rueda delantera interior para que la rueda exterior cargada "
                   "pueda transmitir mayor par útil.",
        "inline_media": "photo-mk6",
        "plate": [
            ("Output", "Potencia", "210 PS", "vw-history"),
            ("New as standard", "Nuevo de serie", "XDS (brake-based)", "vw-history"),
        ],
    },
    {
        "id": "mk7", "gen": "Mk7", "years": "2013–2019 · Mk7.5 (2017)",
        "move_en": "A platform, and a clutch pack at the front axle",
        "move_es": "Una plataforma y un paquete de embragues en el eje delantero",
        "body_en": "The seventh generation sat on Volkswagen’s MQB platform, and VW says the GTI was up to 42 kg lighter "
                   "than its predecessor. It started at 220 PS, with a GTI Performance at 230 PS. The Performance model "
                   "added what VW calls a front differential lock: a multi-plate clutch between the right driveshaft and "
                   "the differential case, squeezed by a piston pump driven by an electric motor, with locking torque up "
                   "to 1,600 Nm proportional to pump pressure. The standard car used XDS+, which brakes the inside wheels. "
                   "VW also lists progressive steering (2.1 turns vs 2.75 turns) and a body 15 mm lower than lesser Golfs. "
                   "The 2017 Mk7.5 facelift brought 230 PS and 245 PS in Europe; in the US it arrived as the 2018 model "
                   "year at 220 hp.",
        "body_es": "La séptima generación usó la plataforma MQB de Volkswagen, y VW dice que el GTI era hasta 42 kg más "
                   "ligero que su antecesor. Empezó con 220 PS, con un GTI Performance de 230 PS. El Performance sumó lo "
                   "que VW llama bloqueo del diferencial delantero: un embrague multidisco entre la flecha derecha y la "
                   "caja del diferencial, apretado por una bomba de pistón movida por motor eléctrico, con un par de "
                   "bloqueo de hasta 1,600 Nm proporcional a la presión. El auto estándar usaba XDS+. VW también menciona "
                   "dirección progresiva (2.1 vueltas frente a 2.75 vueltas) y carrocería 15 mm más baja. La actualización Mk7.5 "
                   "de 2017 trajo 230 PS y 245 PS en Europa; en EE. UU. llegó como modelo 2018 con 220 hp.",
        "inline_media": "photo-clubsport-s",
        "plate": [
            ("Platform", "Plataforma", "MQB", "vw-mk7"),
            ("Weight vs Mk6 (VW)", "Peso vs Mk6 (VW)", "up to 42 kg lighter", "vw-mk7"),
            ("Front lock (Performance)", "Bloqueo delantero (Performance)", "Multi-plate, pump-pressurised", "vw-mk7-chassis"),
            ("Steering", "Dirección", "2.1 turns lock to lock (2.75 on lesser Golfs)", "vw-mk7-chassis"),
            ("Facelift (Mk7.5)", "Actualización (Mk7.5)", "2017 in Europe", "vw-mk7"),
            ("US model year", "Año modelo en EE. UU.", "2018, 220 hp", "vw-us-2018"),
        ],
        "egg": True,
    },
    {
        "id": "mk8", "gen": "Mk8", "years": "2020–2026",
        "move_en": "Software as chassis",
        "move_es": "El software como chasis",
        "body_en": "The eighth generation launched with a 2.0-litre turbo at 245 PS and 370 Nm and a seven-speed DSG. VW "
                   "describes a new vehicle dynamics manager, used in a GTI for the first time, that coordinates the XDS+ "
                   "brake-based lock, the optional DCC adaptive dampers and the front differential lock. In 2024 the "
                   "standard car rose to 265 PS, with the front lock standard on every model, and VW announced the GTI "
                   "EDITION 50 at 325 PS for a 2026 launch, which it calls the most powerful Golf GTI to date.",
        "body_es": "La octava generación salió con un turbo de 2.0 litros de 245 PS y 370 Nm y una DSG de siete "
                   "velocidades. VW describe un nuevo gestor de dinámica del vehículo, usado por primera vez en un GTI, "
                   "que coordina el bloqueo por freno XDS+, los amortiguadores adaptativos DCC opcionales y el bloqueo "
                   "del diferencial delantero. En 2024 el auto estándar subió a 265 PS, con el bloqueo delantero de serie "
                   "en todos los modelos, y VW anunció el GTI EDITION 50 con 325 PS para 2026, que llama el Golf GTI más "
                   "potente hasta la fecha.",
        "inline_media": "photo-mk8",
        "plate": [
            ("Output at launch", "Potencia inicial", "245 PS · 370 Nm", "vw-history"),
            ("Gearbox", "Caja", "7-speed DSG", "vw-history"),
            ("2024 update", "Actualización 2024", "265 PS", "vw-history"),
            ("Announced 2026 milestone", "Hito anunciado 2026", "EDITION 50 · 325 PS", "vw-history"),
        ],
    },
]

# Spanish for spec-plate values that are not language-neutral.
VALUE_ES = {
    "1.6 L injection, from Audi": "1.6 L de inyección, de Audi",
    "10 mm front / 20 mm rear": "10 mm adelante / 20 mm atrás",
    "139 PS · 129 PS with catalyst": "139 PS · 129 PS con catalizador",
    "Scroll supercharger, 160 PS": "Compresor espiral, 160 PS",
    "6-speed DSG": "DSG de 6 velocidades",
    "XDS (brake-based)": "XDS (por freno)",
    "up to 42 kg lighter": "hasta 42 kg más ligero",
    "Multi-plate, pump-pressurised": "Multidisco, presión por bomba",
    "2.1 turns lock to lock (2.75 on lesser Golfs)": "2.1 vueltas de tope a tope (2.75 en Golf menos potentes)",
    "7-speed DSG": "DSG de 7 velocidades",
    "2017 in Europe": "2017 en Europa",
    "2018, 220 hp": "2018, 220 hp",
    "EDITION 50 · 325 PS": "EDITION 50 · 325 PS",
}

CLUBSPORT_S = {
    "en": "In 2016 the Golf GTI Clubsport S lapped the Nürburgring Nordschleife in 7:49.21, which Volkswagen announced as "
          "the front-wheel-drive production car record at the time; the previous mark reported in the press was the "
          "Honda Civic Type R’s 7:50.63. The engineering was about mass in the right places: 310 PS, a manual gearbox "
          "to save mass rather than all-wheel drive, and an aluminium front subframe and aluminium brake carriers to trim "
          "unsprung mass. VW also says stability control was retuned to intervene later.",
    "es": "En 2016 el Golf GTI Clubsport S dio la vuelta al Nordschleife de Nürburgring en 7:49.21, que Volkswagen anunció "
          "como récord para autos de producción con tracción delantera en ese momento; la marca anterior citada por la "
          "prensa era el 7:50.63 del Honda Civic Type R. La ingeniería puso la masa en el lugar correcto: 310 PS, caja "
          "manual en lugar de tracción integral, subchasis delantero y soportes de freno de aluminio para reducir masa "
          "no suspendida. VW también indica intervención más tardía del control de estabilidad.",
    "src": ["vw-cs-s", "press-cs-s", "vw-history"],
}

WEIGHT_LEDGER = [
    ("Front suspension links and bearings", "Brazos y baleros de la suspensión delantera", 1.6),
    ("Aluminium front pivot bearing", "Muñón delantero de aluminio", 2.8),
    ("Rear suspension", "Suspensión trasera", 4.0),
]

DIFF_TEXT = {
    "intro_en": "Under power in a tight corner, a front-wheel-drive car shifts weight off its inside front tyre. With an "
                "ordinary open differential, that light wheel spins and the engine’s torque goes nowhere useful. Pick a "
                "strategy and press the throttle.",
    "intro_es": "Al acelerar en una curva cerrada, un auto de tracción delantera le quita peso a la llanta delantera "
                "interior. Con un diferencial abierto común, esa rueda ligera patina y el par del motor no llega a donde "
                "sirve. Elige una estrategia y pisa el acelerador.",
    "science_en": "Why the clutch pack sends torque outward: a 2008 SAE paper on brake-based torque vectoring explains "
                  "that a clutch-type (semi-active) differential can only move torque from the faster wheel to the slower "
                  "one, and that brakes can create a yaw moment even with a free differential. When the inside wheel "
                  "starts to spin, it is the faster one, so the clutch pack moves torque to the outside wheel, which "
                  "matches Volkswagen’s description of shifting torque from the wheel with less grip to the one with more. "
                  "The paper studied a rear-drive sports car, not a Golf.",
    "science_es": "Por qué el paquete de embragues manda el par hacia afuera: un artículo de SAE de 2008 sobre vectorización "
                  "de par con frenos explica que un diferencial de embrague (semiactivo) solo puede mover par de la rueda "
                  "más rápida a la más lenta, y que los frenos pueden crear un momento de guiñada incluso con un "
                  "diferencial libre. Cuando la rueda interior empieza a patinar es la más rápida, así que el paquete de "
                  "embragues manda el par a la rueda exterior, lo que coincide con la descripción de Volkswagen: pasar el "
                  "par de la rueda con menos agarre a la que tiene más. El artículo estudió un deportivo de tracción "
                  "trasera, no un Golf.",
    "caption_en": "Computed, not measured: arrow lengths follow the Mechanics Lab model in Part VI, whose inputs are "
                  "MODEL values except Volkswagen’s 1,600 Nm locking torque.",
    "caption_es": "Calculado, no medido: el largo de las flechas sigue el modelo del Laboratorio de mecánica de la Parte "
                  "VI, cuyas entradas son valores de MODELO, salvo el par de bloqueo de 1,600 Nm de Volkswagen.",
}

DCT_TEXT = {
    "intro_en": "A dual-clutch gearbox is two gearboxes sharing one output: odd gears on one shaft, even gears on the "
                "other, each with its own clutch. Press “Shift up” and watch which clutch carries the drive.",
    "intro_es": "Una caja de doble embrague son dos cajas que comparten una salida: velocidades nones en una flecha, pares "
                "en la otra, cada una con su propio embrague. Presiona “Subir velocidad” y observa qué embrague lleva "
                "la tracción.",
    "science_en": "What the papers say: Galvagno and colleagues (2011) describe the shift as one clutch letting go while "
                  "the other engages, so torque keeps flowing to the wheels during the change, after which a synchroniser "
                  "pre-selects the next gear on the idle shaft. Brancati and colleagues (2023) add a detail worth listening "
                  "for: with many unloaded gears turning, a dual-clutch box is prone to gear rattle during "
                  "shifts, and the oil between the teeth damps it. Neither paper tested a Volkswagen gearbox.",
    "science_es": "Lo que dicen los artículos: Galvagno y colegas (2011) describen el cambio como un embrague que suelta "
                  "mientras el otro acopla, de modo que el par sigue llegando a las ruedas durante el cambio; después, un "
                  "sincronizador preselecciona la siguiente velocidad en la flecha libre. Brancati y colegas (2023) suman "
                  "un detalle que vale la pena escuchar: con muchos engranes girando sin carga, una caja de doble "
                  "embrague tiende a cascabelear durante los cambios, y el aceite entre los dientes lo amortigua. Ninguno "
                  "de los dos artículos probó una caja de Volkswagen.",
}

UNSPRUNG_TEXT = {
    "en": "Why chase a few kilograms at the wheels? Unsprung mass is everything the springs do not carry: wheels, tyres, "
          "brakes, hubs, part of the links. A 2021 study of in-wheel motors names added unsprung mass as their main "
          "drawback because it worsens road holding. That paper is about electric hubs, not hot hatches, but the "
          "physics is the same reason Volkswagen itemised these savings.",
    "es": "¿Por qué perseguir unos kilos en las ruedas? La masa no suspendida es todo lo que los resortes no cargan: rines, "
          "llantas, frenos, mazas, parte de los brazos. Un estudio de 2021 sobre motores en las ruedas señala la masa no "
          "suspendida adicional como su principal desventaja porque empeora el agarre al camino. Ese artículo trata de "
          "mazas eléctricas, no de hot hatches, pero la física es la misma razón por la que Volkswagen detalló estos "
          "ahorros.",
}

# ---------------------------------------------------------------------------------------------------------------
# Coupled 2D <-> 3D Atelier, Dual-Scale 1:20 <-> 1:5 Axle Anatomy Loupe, Torque Sankey & 6-Axis Radar
# ---------------------------------------------------------------------------------------------------------------
AXLE_LOUPE_TEXT = {
    "kicker_en": "Dual-Scale Chassis Plate · 1:20 Front Bay ↔ 1:5 Detail Loupe",
    "kicker_es": "Lámina Dual de Chasis · Escala 1:20 Eje Delantero ↔ Lupa 1:5",
    "title_en": "Inspect the Front-Wheel-Drive Hardware Across Four Spatial Nodes",
    "title_es": "Inspecciona el eje delantero en cuatro nudos mecánicos a escala 1:20 y 1:5",
    "intro_en": "Front-wheel-drive performance lives inside one crowded transverse front bay sharing steering, suspension, drive torque, and braking. Pick any node on the 1:20 schematic to inspect its 1:5 engineering detail.",
    "intro_es": "El comportamiento de un tracción delantera nace en un solo vano delantero donde conviven dirección, suspensión, par motor y frenado. Toca cualquier nodo del esquema 1:20 para inspeccionar su detalle 1:5.",
}

LOUPE_NODES = [
    {
        "id": "strut",
        "short_en": "1 · MacPherson Tower",
        "short_es": "1 · Torre MacPherson",
        "title_en": "MacPherson Strut & Camber Geometry (1:20 ↔ 1:5)",
        "title_es": "Puntal MacPherson y geometría de caída (1:20 ↔ 1:5)",
        "summary_en": "The damper tube doubles as the upper steering pivot axis between lower ball joint and top strut bearing; kingpin inclination keeps scrub radius small during simultaneous braking and cornering (Cronin 1981; general mechanism, did not test a Golf).",
        "summary_es": "El tubo amortiguador actúa a la vez como eje superior de giro entre la rótula inferior y la copela superior; la inclinación de pivote controla el radio de pivotamiento bajo frenada y giro (Cronin 1981; mecanismo general, no probó un Golf).",
        "src": ["cronin1981", "vw-mk7-chassis"],
    },
    {
        "id": "vaq",
        "short_en": "2 · VAQ Clutch Pack",
        "short_es": "2 · Embrague VAQ",
        "title_en": "Right-Halfshaft Electro-Hydraulic Clutch Pack (Up to 1,600 Nm)",
        "title_es": "Paquete multidisco electrohidráulico derecho (Hasta 1,600 Nm)",
        "summary_en": "Seated on the right driveshaft outside the open differential carrier, pump pressure squeezes multi-plate discs to shift torque up to 1,600 Nm toward the loaded outside front wheel without burning service brake pads.",
        "summary_es": "Situado entre la flecha derecha y la caja del diferencial, una bomba eléctrica comprime discos múltiples para enviar hasta 1,600 Nm hacia el neumático exterior apoyado sin calentar las balatas.",
        "src": ["vw-mk7-chassis", "rubin2015"],
    },
    {
        "id": "dsg",
        "short_en": "3 · Coaxial DSG Shafts",
        "short_es": "3 · Flechas Coaxiales DSG",
        "title_en": "Coaxial Odd/Even Input Shafts & Wet Clutches (6-Speed / 7-Speed)",
        "title_es": "Flechas concéntricas nones/pares y embragues húmedos",
        "summary_en": "Odd gears spin on the inner solid shaft via Clutch 1 while even gears run on the coaxial outer hollow sleeve via Clutch 2—allowing synchronous handover shifts with uninterrupted wheel thrust.",
        "summary_es": "Las velocidades nones giran en la flecha interior sólida (embrague 1) mientras las pares giran sobre la funda hueca concéntrica (embrague 2), permitiendo traslapar la transferencia de par sin vacío de empuje.",
        "src": ["galvagno2011", "brancati2023", "vw-mk5"],
    },
    {
        "id": "unsprung",
        "short_en": "4 · Rotor & Alloy Hub",
        "short_es": "4 · Disco y Portafreno",
        "title_en": "340 × 30 mm Ventilated Disc, Aluminium Carrier & Steering Rack",
        "title_es": "Disco ventilado de 340 × 30 mm, muñón ligero y cremallera",
        "summary_en": "Shaving 1.6 kg in front links and 2.8 kg at aluminium pivot bearings lifts the tyre wheel-hop natural frequency above body bounce so rubber holds rough tarmac; progressive variable teeth tighten the rack to 2.1 turns.",
        "summary_es": "Ahorrar 1.6 kg en brazos delanteros y 2.8 kg en portamanguetas de aluminio despega la frecuencia de salto de rueda del rebote de carrocería; el dentado variable acorta el volante a 2.1 vueltas.",
        "src": ["vw-mk7-chassis", "woo2021", "ahmadian2000"],
    },
]

ATELIER_TEXT = {
    "kicker_en": "Coupled 2D ↔ 3D Observatory · Chassis & Transaxle Workbench",
    "kicker_es": "Observatorio Acoplado 2D ↔ 3D · Banco de Chasis y Transmisión",
    "title_en": "From Lateral Weight Transfer to 3D Hardware (Live GLB & DXF Export)",
    "title_es": "De la transferencia lateral al hardware 3D (Exportación GLB y DXF)",
    "intro_en": "Adjust lateral cornering acceleration (0.00 g to 0.90 g) and axle torque demand on the left: the 2D traction-ellipse schematic recomputes inside/outside front wheel load shift N_in / N_out, available tyre grip μ·N·r, and net direct yaw moment M_z—steering the 3D WebGL2 front assembly on the right live. Switch between all 4 hardware views (MacPherson Strut, VAQ Clutch Differential, Coaxial Dual-Clutch Shafts, and Twist-Beam vs. Multi-Link Corner) and export valid binary .glb or R2000 .dxf geometry directly.",
    "intro_es": "Ajusta la aceleración lateral en curva (0.00 g a 0.90 g) y el par pedido al eje a la izquierda: el esquema 2D recalcula la descarga interior N_in / N_out, los límites de agarre μ·N·r y el momento directo de guiñada M_z, orientando en vivo el modelo 3D WebGL2 a la derecha. Alterna entre las 4 vistas mecánicas (Puntal MacPherson, Diferencial VAQ, Doble Embrague Coaxial y Eje Trasero / Cuarto de Auto) y exporta archivos .glb o .dxf.",
    "science_en": "Tire force saturation follows the nonlinear Pacejka slip-load framework (1992), differential torque vectoring yaw stabilization is formalized in Abe et al. (2001) and Rubin & Arogeti (2015), and integrated brake/e-diff/damper coordination in Trächtler (2004). None of those studies measured a Golf GTI; numeric bench readouts reflect the MODEL parameters in Part VI.",
    "science_es": "La saturación de agarre sigue el marco no lineal de Pacejka y Bakker (1992), la estabilización de guiñada mediante diferencial activo se formaliza en Abe et al. (2001) y Rubin y Arogeti (2015), y la coordinación freno/suspensión/eje en Trächtler (2004). Ninguno midió un Golf GTI; las cifras del banco siguen el MODELO de la Parte VI.",
}

SANKEY_TEXT = {
    "kicker_en": "Alluvial Torque-Conservation Ribbon · 3,000 Nm Demand Corner Split (MODEL)",
    "kicker_es": "Diagrama Aluvial · Reparto de 3,000 Nm en Curva (MODELO)",
    "title_en": "Where Does the Engine’s Torque Go Under Cornering Unloading?",
    "title_es": "¿A dónde va el par motor cuando descarga la rueda interior?",
    "intro_en": "Compare the exact Part VI 3,000 Nm axle demand across the unloaded left-hander (inside tyre holds 832 Nm, outside holds 1,728 Nm MODEL limits): an open differential caps road tractive torque at 1,664 Nm (1,336 Nm wasted in inside spin), whereas the 1,600 Nm VAQ clutch pack delivers 2,560 Nm directly to the tarmac with zero brake heat.",
    "intro_es": "Compara la demanda exacta de 3,000 Nm de la Parte VI en plena curva (límite MODELO interior de 832 Nm y exterior de 1,728 Nm): un diferencial abierto topa en 1,664 Nm al camino (1,336 Nm perdidos en patinaje), mientras el paquete VAQ de 1,600 Nm entrega 2,560 Nm útiles sin calentar los frenos.",
    "readout_lock_en": "MODEL Flow (VAQ 1,600 Nm Clutch Pack): 3,000 Nm demand -> 832 Nm inside road + 1,728 Nm outside road = 2,560 Nm net drive (440 Nm excess held at engine limit) · Brake heat = 0 Nm",
    "readout_lock_es": "MODELO Flujo (Embrague VAQ 1,600 Nm): 3,000 Nm pedidos -> 832 Nm rueda interior + 1,728 Nm rueda exterior = 2,560 Nm al asfalto (440 Nm limitados por par motor) · Freno = 0 Nm",
    "readout_xds_en": "MODEL Flow (XDS+ Brake Vectoring): 3,000 Nm demand -> 832 Nm inside + 1,332 Nm outside = 2,164 Nm to the road + 500 Nm inside brake heat + 336 Nm unapplied",
    "readout_xds_es": "MODELO Flujo (Vectorización XDS+): 3,000 Nm pedidos -> 832 Nm interior + 1,332 Nm exterior = 2,164 Nm al camino + 500 Nm calor de freno + 336 Nm sin aplicar",
    "readout_open_en": "MODEL Flow (Open Differential): 3,000 Nm demand -> 832 Nm inside + 832 Nm outside = 1,664 Nm to the road + 1,336 Nm wasted in inside-wheel slip",
    "readout_open_es": "MODELO Flujo (Diferencial Abierto): 3,000 Nm pedidos -> 832 Nm interior + 832 Nm exterior = 1,664 Nm al camino + 1,336 Nm disipados en patinaje interno",
    "src": ["scamarcio2023", "kakalis2008", "vw-mk7-chassis"],
}

RADAR_TEXT = {
    "kicker_en": "6-Axis Vehicle-Dynamics Envelope · MODEL Comparative Index (0–100)",
    "kicker_es": "Envolvente Polar de 6 Ejes · Índice Comparativo MODELO (0–100)",
    "title_en": "How Five Eras Expanded Traction Without Abandoning Compact Packaging",
    "title_es": "Cómo cinco eras ampliaron la tracción sin perder el envase compacto",
    "intro_en": "Toggle across GTI engineering eras on this illustrative 0–100 MODEL comparative index (reflecting published subsystem evolution, not independent instrumented lap telemetry): Mk1 maximized low-mass feedback, Mk5 bridged shift-torque gaps, and Mk7/Mk8 unlocked corner-exit front traction via MQB stiffness and e-diff control.",
    "intro_es": "Alterna entre eras técnicas en este índice comparativo MODELO 0–100 (resume la evolución de subsistemas publicada, no telemetría instrumental propia): Mk1 priorizó ligereza pura, Mk5 eliminó vacíos entre cambios con DSG y Mk7/Mk8 desbloquearon tracción en salida mediante rigidez MQB y bloqueo electrónico.",
    "axes_en": ["Lightness Response", "Corner-Exit Traction", "Shift Continuity", "Braking & Yaw Stability", "Thermal Endurance", "System Coordination"],
    "axes_es": ["Ligereza de respuesta", "Tracción en salida", "Continuidad en cambio", "Frenada y guiñada", "Resistencia térmica", "Coordinación integrada"],
    "src": ["vw-history", "vw-mk7-chassis", "trachtler2004"],
}

RADAR_ERAS = [
    {
        "id": "mk1",
        "label_en": "1976 · Mk1 (810 kg · 110 PS)",
        "label_es": "1976 · Mk1 (810 kg · 110 PS)",
        "scores": [96, 52, 48, 56, 58, 28],
        "note_en": "Unassisted direct steering feel and 810 kg curb mass; open differential and narrow 175 mm rubber set traction ceiling.",
        "note_es": "Dirección pura y 810 kg de ligereza; diferencial abierto y llantas de 175 mm fijan el techo de tracción.",
    },
    {
        "id": "mk4",
        "label_en": "1998–2005 · Mk4–Mk5 (Turbo + 6-spd DSG)",
        "label_es": "1998–2005 · Mk4–Mk5 (Turbo + DSG 6)",
        "scores": [64, 62, 92, 72, 74, 58],
        "note_en": "Turbo torque plateau (200 PS) and coaxial dual-clutch upshifts cut longitudinal shift gaps; still reliant on open differential.",
        "note_es": "Par turbo (200 PS) y doble embrague coaxial cierran interrupciones al subir de marcha; mantiene diferencial abierto.",
    },
    {
        "id": "mk7",
        "label_en": "2013–2019 · Mk7 MQB + VAQ + Clubsport S",
        "label_es": "2013–2019 · Mk7 MQB + VAQ + Clubsport S",
        "scores": [84, 92, 94, 90, 91, 82],
        "note_en": "42 kg MQB weight savings, aluminium front carriers, progressive steering, and up to 1,600 Nm multi-plate front lock.",
        "note_es": "Ahorro de hasta 42 kg sobre MQB, muñones ligeros de aluminio, dirección de 2.1 vueltas y bloqueo delantero hasta 1,600 Nm.",
    },
    {
        "id": "mk8",
        "label_en": "2020–2026 · Mk8 VDM (245–325 PS)",
        "label_es": "2020–2026 · Mk8 Gestor VDM (245–325 PS)",
        "scores": [80, 96, 97, 96, 93, 98],
        "note_en": "Vehicle Dynamics Manager fuses XDS+, front differential lock, and adaptive DCC dampers ahead of the 325 PS EDITION 50.",
        "note_es": "El Gestor de Dinámica Vehicular coordina XDS+, bloqueo delantero y DCC rumbo al EDITION 50 de 325 PS.",
    },
]

# ---------------------------------------------------------------------------------------------------------------
# #engineers-study: Four Subsystem Archetypes, Constructive Grammar Table & 6-Station Vehicle-Dynamics Lineage
# ---------------------------------------------------------------------------------------------------------------
ENGINEERS_STUDY = {
    "kicker_en": "For Automotive & Chassis Engineers · Kinematic Grammar & Academic Lineage",
    "kicker_es": "Para Ingenieros Automotrices y de Chasis · Gramática Cinemática y Linaje Académico",
    "title_en": "How Chassis Engineers Study Front-Wheel-Drive Dynamics (1974–2026)",
    "title_es": "Cómo estudian los ingenieros la dinámica de tracción delantera (1974–2026)",
    "intro_en": "Why does a transverse front-engine hatchback feel balanced rather than nose-heavy? Automotive engineers dissect the layout across four coupled subsystems—paired below with a constructive specifications ledger and six landmark peer-reviewed papers (all checked in Crossref and Scite with zero retractions, explicitly distinguishing general dynamics theory from VW’s published factory specs).",
    "intro_es": "¿Por qué un hatchback transversal de motor delantero logra equilibrio en curva sin volverse torpe de trompa? La ingeniería automotriz descompone su arquitectura en cuatro subsistemas acoplados, acompañados abajo por una tabla constructiva y seis hitos bibliográficos arbitrados (verificados en Crossref y Scite sin retractaciones, separando claramente la teoría general de los datos publicados por VW).",
    "subsystems": [
        {
            "name_en": "MacPherson Strut & Steering Axis",
            "name_es": "Puntal MacPherson y Eje de Dirección",
            "rule_en": "Compact spring-damper pillar plus lower control arm saves transverse engine-bay width while tuning kingpin inclination and caster trail against torque steer.",
            "rule_es": "El pilar resorte-amortiguador y brazo inferior único libera ancho en el vano motor mientras sintoniza pivote e inclinación frente a tirones de dirección.",
            "where_en": "All 8 GTI generations; Mk7 progressive variable-pitch rack (2.1 turns)",
            "where_es": "Ocho generaciones; cremallera progresiva de 2.1 vueltas desde Mk7",
        },
        {
            "name_en": "GDI Evaporative Charge & Exhaust Boost",
            "name_es": "Inyección Directa y Sobrealimentación",
            "rule_en": "Spraying fuel inside the cylinder cools intake air via latent heat, raising knock-limited compression tolerance alongside high-efficiency exhaust turbines.",
            "rule_es": "Vaporizar combustible directo en cámara reduce temperatura de mezcla por calor latente, elevando margen antidetonante bajo turbina de escape.",
            "where_en": "2.0 L turbo petrol architecture (Mk5 200 PS → Mk8 265 PS / 325 PS)",
            "where_es": "Motores 2.0 L turbo de gasolina (Mk5 200 PS → Mk8 265 PS / 325 PS)",
        },
        {
            "name_en": "Coaxial Dual-Clutch & Electro-Hydraulic VAQ",
            "name_es": "Doble Embrague Coaxial y Bloqueo VAQ",
            "rule_en": "Odd and even shafts share one differential crown; multi-plate wet clutches swap shafts under overlap while VAQ routes up to 1,600 Nm outward in corners.",
            "rule_es": "Flechas nones y pares comparten corona de salida con traslape hidráulico, mientras el embrague VAQ deriva hasta 1,600 Nm hacia la rueda apoyada.",
            "where_en": "Mk5–Mk8 DSG + Mk7 Performance / Mk8 standard front lock",
            "where_es": "DSG en Mk5–Mk8 + bloqueo delantero en Mk7 Performance / Mk8",
        },
        {
            "name_en": "Modular Rear Compliance & Quarter-Car Mass",
            "name_es": "Eje Trasero y Masa No Suspendida",
            "rule_en": "Transitioning to multi-link rear kinematics separates toe control from vertical bumps while light aluminium hubs keep high-frequency wheel hop separated from body bounce.",
            "rule_es": "Los brazos independientes traseros separan convergencia del bacheo, y manguetas de aluminio despegan el salto de rueda del rebote de carrocería.",
            "where_en": "MQB modular multi-link rear & Clubsport S aluminium subframe/carriers",
            "where_es": "Trasera multibrazo MQB y subchasis/portamanguetas de aluminio en Clubsport S",
        },
    ],
    "grammar_head_en": ("Subsystem Ratio", "GTI / Published Value", "Engineering Rationale", "Source"),
    "grammar_head_es": ("Razón Constructiva", "Cifra GTI / Publicada", "Principio de Ingeniería", "Fuente"),
    "grammar_rows": [
        (
            "Launch lightness datum",
            "Referencia inicial de masa",
            "810 kg base · 110 PS",
            "810 kg base · 110 PS",
            "Restraining vehicle weight yields sharper transients than adding displacement alone.",
            "Contener masa total mejora respuesta transitoria más que sumar cilindrada.",
            "vw-mk1",
        ),
        (
            "Stance drop over standard Golf",
            "Altura rebajada respecto a Golf base",
            "10 mm front / 20 mm rear (Mk1) · 15 mm (Mk7)",
            "10 mm adelante / 20 mm atrás (Mk1) · 15 mm (Mk7)",
            "Lower roll center and shorter spring travel cut lateral load transfer ΔF_z.",
            "Bajar centro de gravedad y recorrido recorta transferencia lateral ΔF_z.",
            "vw-mk1",
        ),
        (
            "MQB structural mass delta",
            "Reducción estructural MQB",
            "up to 42 kg lighter (Mk7 vs Mk6)",
            "hasta 42 kg más ligero (Mk7 vs Mk6)",
            "Hot-formed steels recover torsional stiffness without paying weight penalty.",
            "Aceros conformados en caliente recuperan rigidez reduciendo masa bruta.",
            "vw-mk7",
        ),
        (
            "Variable progressive steering",
            "Cremallera de paso variable",
            "2.1 turns lock-to-lock vs 2.75 turns",
            "2.1 vueltas entre topes frente a 2.75 vueltas",
            "Calm center on highway merges smoothly into rapid lock-to-lock apex turn-in.",
            "Centro estable en autopista y giro rápido conforme crece el ángulo de volante.",
            "vw-mk7-chassis",
        ),
        (
            "Front differential lock limit",
            "Límite del bloqueo delantero",
            "1,600 Nm max multi-plate clutch torque",
            "1,600 Nm par máximo multidisco",
            "Transfers drive strictly from faster inside tyre toward loaded outside tyre.",
            "Transfiere par únicamente desde rueda interior rápida hacia la exterior cargada.",
            "vw-mk7-chassis",
        ),
        (
            "Itemized corner mass savings",
            "Ahorro en masa no suspendida",
            "1.6 kg + 2.8 kg + 4.0 kg = 8.4 kg",
            "1.6 kg + 2.8 kg + 4.0 kg = 8.4 kg",
            "Raises unsprung wheel-hop mode above body bounce for cleaner tarmac contact.",
            "Eleva frecuencia de salto de rueda por encima del rebote de carrocería.",
            "vw-mk7-chassis",
        ),
        (
            "Integrated dynamics supervision",
            "Coordinación de dinámica integrada",
            "XDS+ + front lock + DCC (245 → 325 PS)",
            "XDS+ + bloqueo delantero + DCC (245 → 325 PS)",
            "Prevents brake vectoring, e-diff, and damping actuators from counteracting each other.",
            "Evita que freno, diferencial y amortiguadores se opongan entre sí al límite.",
            "vw-history",
        ),
    ],
    "lineage_title_en": "Vehicle-Dynamics Scholarship Lineage (1974–2026) · Click Any Station",
    "lineage_title_es": "Linaje Académico en Dinámica Vehicular (1974–2026) · Selecciona cada hito",
    "lineage_intro_en": "Select each peer-reviewed station to inspect the governing physics inside engines, struts, tyres, dual clutches, active differentials, and global chassis controllers. Explicit scope tags mark general theory studies that did not test a Golf GTI.",
    "lineage_intro_es": "Selecciona cada artículo arbitrado para examinar la física detrás de motores, puntales MacPherson, neumáticos, doble embrague, diferenciales activos y control integrado. Cada ficha aclara su alcance porque ninguno ensayó un Golf GTI.",
    "lineage": [
        {
            "id": "lin-karnopp",
            "year": "1974 / 1992",
            "short_en": "Karnopp · Skyhook",
            "short_es": "Karnopp · Skyhook",
            "title_en": "Karnopp, Crosby & Harwood (1974) + Hać & Youn (1992) · Semi-Active Damping",
            "title_es": "Karnopp, Crosby y Harwood (1974) + Hać y Youn (1992) · Amortiguación Semiactiva",
            "who_en": "Karnopp et al. (ASME J. Eng. Ind. 1974) · Hać & Youn (J. Vib. Acoust. 1992)",
            "note_en": "Introduced the skyhook damping concept: switching damper orifice resistance faster than body heave periods reconciles isolating sprung-mass heave with restraining unsprung wheel hop—the exact mathematical ancestry behind modern millisecond-rate adaptive DCC dampers.",
            "note_es": "Introdujeron la lógica skyhook: variar en milisegundos la resistencia hidráulica del amortiguador concilia el aislamiento de la carrocería con el control de rebote de rueda, base directa de los amortiguadores DCC modernos.",
            "boundary_en": "Scope: General quarter-car semi-active vibration control studies; neither study tested a Golf GTI.",
            "boundary_es": "Alcance: teoría general en modelo de cuarto de auto; ninguno probó un Golf GTI.",
            "src": ["karnopp1974", "hac1992"],
        },
        {
            "id": "lin-cronin",
            "year": "1981",
            "short_en": "Cronin · Struts",
            "short_es": "Cronin · Puntales",
            "title_en": "D. L. Cronin (1981) · Exact 3D Kinematics of MacPherson Struts",
            "title_es": "D. L. Cronin (1981) · Cinemática 3D del Puntal MacPherson",
            "who_en": "D. L. Cronin (Mechanism and Machine Theory 1981)",
            "note_en": "Formulated exact nonlinear kinematic constraint equations for MacPherson front suspensions—quantifying camber curve changes, caster precession, track scrub, and anti-dive/lift vectors without resorting to small-angle approximations across full wheel travel.",
            "note_es": "Formuló ecuaciones cinemáticas tridimensionales exactas para suspensiones MacPherson, cuantificando caída, avance y barrido de vía en todo el recorrido de suspensión sin aproximaciones lineales pequeñas.",
            "boundary_en": "Scope: General multibody strut kinematics paper; did not analyze or test a Golf GTI.",
            "boundary_es": "Alcance: artículo cinemático general sobre puntales; no midió un Golf GTI.",
            "src": ["cronin1981"],
        },
        {
            "id": "lin-pacejka",
            "year": "1992",
            "short_en": "Pacejka · Tyre",
            "short_es": "Pacejka · Llanta",
            "title_en": "H. B. Pacejka & E. Bakker (1992) · The Magic Formula Tyre Model",
            "title_es": "H. B. Pacejka y E. Bakker (1992) · La Fórmula Mágica del Neumático",
            "who_en": "Pacejka & Bakker (Vehicle System Dynamics 1992)",
            "note_en": "Captured longitudinal traction, lateral cornering stiffness, self-aligning torque, and vertical-load sensitivity inside compact trigonometric curves—showing mathematically why loading an outside front tyre grows peak grip less than proportionally (load sensitivity), so splitting torque equitably maximizes total axle thrust.",
            "note_es": "Sintetizó agarre longitudinal, fuerza lateral, par de autoalineación y sensibilidad de carga en curvas trigonométricas compactas: explica por qué el agarre crece menos que la carga vertical (sensibilidad de carga) y por qué vectorizar hacia afuera aprovecha el pico real.",
            "boundary_en": "Scope: Semi-empirical tyre physics framework; did not publish VW Golf GTI tyre test coefficients.",
            "boundary_es": "Alcance: formulación física general del neumático; no reporta ensayos de llantas del Golf GTI.",
            "src": ["pacejka1992"],
        },
        {
            "id": "lin-zhao",
            "year": "1999 / 2015",
            "short_en": "Zhao · GDI",
            "short_es": "Zhao · GDI",
            "title_en": "Zhao, Lai & Harrington (1999) + Hu et al. (2015) · Direct Injection & Boost",
            "title_es": "Zhao, Lai y Harrington (1999) + Hu et al. (2015) · Inyección Directa y Turbo",
            "who_en": "Zhao et al. (Prog. Energy Combust. Sci. 1999) · Hu et al. (IJER 2015)",
            "note_en": "Explained why in-cylinder fuel vaporization draws heat directly out of compressed intake charge (charge cooling), raising knock threshold on boosted four-cylinder engines so higher cylinder pressures stay reliable at low engine speed.",
            "note_es": "Detallaron cómo la vaporización directa dentro del cilindro extrae calor del aire comprimido (enfriamiento de carga), elevando el límite contra detonación en motores turbo de baja cilindrada y cuatro cilindros.",
            "boundary_en": "Scope: General spark-ignition GDI and downsized-turbo engine reviews; neither tested a VW engine.",
            "boundary_es": "Alcance: revisiones generales de combustión GDI y sobrealimentación; ninguna probó motores VW.",
            "src": ["zhao1999", "hu2015"],
        },
        {
            "id": "lin-fichera",
            "year": "2004 / 2011",
            "short_en": "Rear · DSG",
            "short_es": "Trasera · DSG",
            "title_en": "Fichera et al. (2004) + Galvagno (2011) · Rear Torsion Beam & Coaxial Clutches",
            "title_es": "Fichera et al. (2004) + Galvagno (2011) · Eje Trasero y Embragues Coaxiales",
            "who_en": "Fichera, Lacagnina & Petrone (2004) · Galvagno et al. (2011)",
            "note_en": "Coupled multibody kinematics maps torsion-beam roll steer vs. independent links on compact hatches (explaining why higher-output trims moved from Mk1–Mk4 twist beams to Mk5–Mk8 multi-link), while Galvagno’s kinematic-dynamic equations model zero-torque-loss powershift clutch crossings.",
            "note_es": "La dinámica multicuerpo compara la deformación de barras torsionales frente a esquemas multibrazo independientes (contexto técnico del salto del eje Mk4 al multibrazo desde Mk5), mientras Galvagno formula la cinemática de cambios sin pérdida de tracción.",
            "boundary_en": "Scope: Generic torsion-beam and dual-clutch multibody papers; did not model VW Golf tolerances directly.",
            "boundary_es": "Alcance: modelos genéricos multicuerpo de suspensión trasera y caja DSG; no calibran piezas de fábrica VW.",
            "src": ["fichera2004", "galvagno2011"],
        },
        {
            "id": "lin-abe",
            "year": "2001–2015",
            "short_en": "Abe · VDM MPC",
            "short_es": "Abe · VDM MPC",
            "title_en": "Abe (2001), Trächtler (2004) & Rubin (2015) · Active Diffs & Vehicle Dynamics Control",
            "title_es": "Abe (2001), Trächtler (2004) y Rubin (2015) · Diferenciales Activos y Control VDM",
            "who_en": "Abe et al. (2001) · Trächtler (2004) · Rubin & Arogeti (2015)",
            "note_en": "Showed that generating a deliberate right-left longitudinal force couple produces a fast stabilizing yaw moment near peak lateral g—and why supervisory model-predictive coordinators (matching the philosophy of Mk8’s Vehicle Dynamics Manager) prevent brake clamping, clutch locking, and damping actuators from fighting each other.",
            "note_es": "Demostraron que crear una diferencia intencional de empuje izquierdo-derecho aporta un momento estabilizador de guiñada ágil cerca del límite lateral, y por qué un supervisor único (como la lógica del Gestor de Dinámica Mk8) evita conflictos entre frenos, bloqueo e hidráulica.",
            "boundary_en": "Scope: Control-theory and chassis integration articles outside VW; did not test any Golf GTI hardware.",
            "boundary_es": "Alcance: artículos generales de control vehicular integrador; no probaron unidades Golf GTI.",
            "src": ["abe2001", "trachtler2004", "rubin2015"],
        },
    ],
}

# ---------------------------------------------------------------------------------------------------------------
# Interludes & Long-form (magazine) five parts
# ---------------------------------------------------------------------------------------------------------------
PARTS = [
    {
        "id": "part-1", "numeral": "I", "years": "1976–1983",
        "title_en": "Lightness", "title_es": "Ligereza",
        "opener": [
            {
                "en": "Start with what the first car did not have. VW’s archive lists a base weight of 810 kg, a 1.6-litre "
                      "engine and 175-section tyres on 13-inch wheels. There was no turbocharger: the GTI was a Golf with a "
                      "stronger engine, a lower stance and anti-roll bars at both ends. In our reading, the engineering move was restraint.",
                "es": "Empecemos por lo que el primer auto no tenía. El archivo de VW indica un peso base de 810 kg, un motor "
                      "de 1.6 litros y llantas de sección 175 en rines de 13 pulgadas. No había turbo: el GTI era un "
                      "Golf con un motor más fuerte, una postura más baja y barras estabilizadoras en ambos ejes. En nuestra lectura, la decisión de ingeniería fue la contención.",
                "src": ["vw-mk1"],
            },
            {
                "en": "The archive also records how the car grew up during its run. In 1978 new bumpers with replaceable "
                      "plastic covers on a metal support made it almost 10 cm longer; right-hand drive arrived in 1979; a "
                      "redesigned dashboard and larger rear lights came in 1981, the same year a four-door body became "
                      "available.",
                "es": "El archivo también registra cómo maduró el auto durante su producción. En 1978, defensas nuevas con "
                      "cubiertas plásticas reemplazables sobre un soporte metálico lo alargaron casi 10 cm; el volante a la "
                      "derecha llegó en 1979; un tablero rediseñado y calaveras más grandes llegaron en 1981, el mismo año "
                      "en que se ofreció la carrocería de cuatro puertas.",
                "src": ["vw-mk1"],
            },
        ],
        "pull_en": "Our reading: the engineering move was restraint.",
        "pull_es": "Nuestra lectura: la decisión de ingeniería fue la contención.",
        "cards": ["mk1"],
        "interlude": "mk1-details",
    },
    {
        "id": "part-2", "numeral": "II", "years": "1984–1997",
        "title_en": "Breathing", "title_es": "Respirar",
        "opener": [
            {
                "en": "The second and third generations are the story of an engine learning to breathe under new rules. A "
                      "sixteen-valve head, four valves for each of four cylinders, arrived in 1986, and a catalytic-converter "
                      "version followed. Volkswagen lists both figures: 139 PS and 208 km/h without a "
                      "regulated catalyst, 129 PS and 200 km/h with one. Then, in 1990, came a different way to fill the "
                      "cylinders: the G60’s scroll-type supercharger, driven by the engine itself.",
                "es": "La segunda y la tercera generación son la historia de un motor que aprende a respirar con reglas "
                      "nuevas. Una cabeza de dieciséis válvulas, cuatro por cada uno de los cuatro cilindros, llegó en 1986, y después una "
                      "versión con convertidor catalítico. Volkswagen da las dos cifras: 139 PS y 208 km/h sin catalizador regulado, 129 PS y 200 km/h con él. Luego, en 1990, "
                      "llegó otra forma de llenar los cilindros: el compresor de tipo espiral del G60, movido por el propio "
                      "motor.",
                "src": ["vw-history"],
            },
            {
                "en": "The third generation carried more of everything: VW lists a 2.0-litre engine, a sports chassis with "
                      "a lowered body, and all the headlight functions in one housing. In 1996 it also carried the first "
                      "anniversary edition in GTI history and a 110 PS turbodiesel wearing the badge.",
                "es": "La tercera generación cargó más de todo: VW enumera un motor de 2.0 litros, un chasis deportivo con la "
                      "carrocería más baja y todas las funciones de los faros en una sola unidad. En 1996 también trajo la "
                      "primera edición de aniversario en la historia del GTI y un turbodiésel de 110 PS con el "
                      "emblema.",
                "src": ["vw-history"],
            },
        ],
        "pull_en": "139 PS without a regulated catalyst, 129 PS with one: VW’s own figures, side by side.",
        "pull_es": "139 PS sin catalizador regulado, 129 PS con él: las cifras de VW, lado a lado.",
        "cards": ["mk2", "mk3"],
        "interlude": "",
    },
    {
        "id": "part-3", "numeral": "III", "years": "1998–2008",
        "title_en": "Pressure", "title_es": "Presión",
        "opener": [
            {
                "en": "From the fourth generation on, turbocharged petrol engines become the GTI’s main line in VW’s "
                      "history page: a 1.8-litre turbo in the Mk4, beside a five-cylinder, then turbo engines in the Mk5, "
                      "Mk6 and Mk8. Why turbo, after the G60 had tried a supercharger? VW does not say; engine researchers summarise the general trade plainly. "
                      "A supercharger takes its power straight from the crankshaft, which helps the engine respond to the "
                      "throttle. A turbocharger is driven by the engine’s exhaust flow and is the more widely adopted "
                      "choice for fuel efficiency, paired with direct fuel injection charge cooling, though it needs a moment to build boost.",
                "es": "A partir de la cuarta generación, los motores turbo de gasolina se vuelven la línea principal del GTI "
                      "en la página de historia de VW: un 1.8 litros turbo en el Mk4, junto a un cinco cilindros, y luego "
                      "motores turbo en el Mk5, el Mk6 y el Mk8. ¿Por qué turbo, si el G60 ya había probado un compresor? VW no lo dice; la investigación sobre "
                      "motores resume el intercambio general sin rodeos. Un compresor toma su energía directo del cigüeñal, lo que ayuda a "
                      "que el motor responda al acelerador. Un turbo se mueve con el escape y es la opción más extendida en eficiencia, junto al enfriamiento por inyección directa, aunque toma un instante cargar presión.",
                "src": ["hu2015", "hu2016", "zhao1999"],
            },
            {
                "en": "The fifth generation added an optional dual-clutch gearbox, the DSG, that keeps "
                      "torque flowing during the shift. Its section below lets you run through the gears. VW marked the "
                      "car’s thirtieth year with the Edition 30 of 2006: 230 PS, 0–100 km/h in 6.8 s, 18-inch wheels, "
                      "tartan-checked seats and the golf-ball gear knob, and called it the fastest GTI to date.",
                "es": "La quinta generación sumó una caja de doble embrague opcional, la DSG, que mantiene "
                      "el par durante el cambio. Su sección, más abajo, te deja recorrer las velocidades. VW celebró los "
                      "treinta años del auto con la Edition 30 de 2006: 230 PS, 0–100 km/h en 6.8 s, rines de 18 pulgadas, "
                      "asientos a cuadros y la palanca con forma de pelota de golf, y la llamó el GTI más rápido hasta "
                      "entonces.",
                "src": ["vw-history"],
            },
        ],
        "pull_en": "A supercharger answers the throttle; a turbo answers the fuel bill.",
        "pull_es": "El compresor responde al acelerador; el turbo responde a la cuenta de gasolina.",
        "cards": ["mk4", "mk5"],
        "interlude": "boost",
    },
    {
        "id": "part-4", "numeral": "IV", "years": "2009–2019",
        "title_en": "Grip", "title_es": "Agarre",
        "opener": [
            {
                "en": "With power past 200 PS through the front wheels, the next problem was putting it down. The sixth "
                      "generation answered with the brakes: XDS, standard on a GTI for the first time, according to VW. The "
                      "seventh answered twice, with XDS+ on the standard car and a clutch-pack front differential lock up to "
                      "1,600 Nm on the Performance model. VW’s 2013 launch material is unusually detailed about the hardware, "
                      "and the anatomy and differential sections below walk through it.",
                "es": "Con más de 200 PS en las ruedas delanteras, el siguiente problema fue ponerlos en el piso. La sexta "
                      "generación respondió con los frenos: el XDS, de serie en un GTI por primera vez, según VW. La séptima "
                      "respondió dos veces, con XDS+ en el auto estándar y un bloqueo del diferencial delantero por "
                      "embragues de hasta 1,600 Nm en el Performance. El material de lanzamiento de VW de 2013 es inusualmente detallado "
                      "sobre el hardware, y las secciones de anatomía y diferenciales de abajo lo recorren.",
                "src": ["vw-history", "vw-mk7-chassis"],
            },
            {
                "en": "The era also produced the specials. VW lists the Edition 35 of 2011 at 235 PS, the first GTI cabriolet "
                      "in 2012, the 2016 Clubsport at 265 PS with a temporary boost to 290 PS that VW says was the first GTI "
                      "to break the six-second mark in its sprint figure, the Clubsport S at 310 PS, and the 2019 GTI TCR at 290 PS.",
                "es": "La época también trajo las ediciones especiales. VW enumera la Edition 35 de 2011 con 235 PS, el "
                      "primer GTI convertible en 2012, el Clubsport de 2016 con 265 PS y un aumento temporal a 290 PS que, según VW, "
                      "fue el primer GTI en bajar de seis segundos en su cifra de aceleración, el Clubsport S con 310 PS y el GTI TCR de 2019 con "
                      "290 PS.",
                "src": ["vw-history"],
            },
        ],
        "pull_en": "With 200 PS through the front wheels, the problem stopped being power.",
        "pull_es": "Con 200 PS en las ruedas delanteras, el problema dejó de ser la potencia.",
        "cards": ["mk6", "mk7"],
        "interlude": "anatomy",
    },
    {
        "id": "part-5", "numeral": "V", "years": "2020–2026",
        "title_en": "Software", "title_es": "Software",
        "opener": [
            {
                "en": "The eighth generation’s headline is a controller. VW describes a vehicle dynamics manager that "
                      "coordinates the brake-based XDS+, the optional adaptive dampers and the front differential lock as "
                      "one system. The hardware ideas are the ones earlier generations introduced one at a time; on VW’s "
                      "description, what is new is that software decides how they work together.",
                "es": "Lo más destacado de la octava generación es un controlador. VW describe un gestor de dinámica del "
                      "vehículo que coordina el XDS+ por freno, los amortiguadores adaptativos opcionales y el bloqueo del "
                      "diferencial delantero como un solo sistema. Las ideas de hardware son las que las generaciones "
                      "anteriores introdujeron una por una; según la descripción de VW, lo nuevo es que el software decide "
                      "cómo trabajan juntas.",
                "src": ["vw-history"],
            },
            {
                "en": "VW lists the Clubsport 45 of 2021 at 300 PS, a 2024 update that raised the standard car to 265 PS, and "
                      "the GTI EDITION 50, shown at the 2025 Nürburgring 24-hour race, at 325 PS for a 2026 launch.",
                "es": "VW enumera el Clubsport 45 de 2021 con 300 PS, una actualización de 2024 que subió el auto estándar a "
                      "265 PS, y el GTI EDITION 50, presentado en las 24 Horas de Nürburgring de 2025, con 325 PS para "
                      "salir en 2026.",
                "src": ["vw-history"],
            },
        ],
        "pull_en": "The hardware ideas are old; the new part is who decides.",
        "pull_es": "Las ideas de hardware son viejas; lo nuevo es quién decide.",
        "cards": ["mk8"],
        "interlude": "editions",
    },
]

MK1_DETAILS = {
    "title_en": "The details that became shorthand",
    "title_es": "Los detalles que se volvieron sinónimo",
    "items": [
        ("Launch colours: Diamond Silver Metallic and Mars Red.", "Colores de lanzamiento: Diamond Silver Metallic y Mars Red."),
        ("Chrome trim swapped for black parts, and a black headliner.", "Cromo cambiado por piezas negras y cielo negro."),
        ("A grille with the GTI badge and a red surround.", "Una parrilla con el emblema GTI y marco rojo."),
        ("An enlarged front spoiler and 175/70 HR 13 tyres.", "Un spoiler delantero más grande y llantas 175/70 HR 13."),
        ("Tartan sports seats and a golf-ball-shaped gear lever.", "Asientos deportivos de tela escocesa y palanca con forma de pelota de golf."),
        ("Of exports, per VW: 35% to France, 18% to Italy, 13% to Switzerland.", "De las exportaciones, según VW: 35 % a Francia, 18 % a Italia, 13 % a Suiza."),
        ("The 1983 Pirelli edition: 10,500 built, 185/60 HR 14 tyres on alloys, a four-spoke leather wheel.", "La edición Pirelli de 1983: 10,500 unidades, llantas 185/60 HR 14 en rines de aleación y volante de piel de cuatro rayos."),
    ],
    "src": ["vw-mk1"],
}

BOOST = {
    "title_en": "Two ways to push air",
    "title_es": "Dos formas de empujar aire",
    "rows": [
        ("Driven by", "Movido por", "the crankshaft", "el cigüeñal", "exhaust gas", "los gases de escape"),
        ("Strength", "Ventaja", "quick response to the throttle", "respuesta rápida al acelerador", "fuel efficiency", "eficiencia en combustible"),
        ("Cost", "Costo", "takes power from the engine to run", "le quita potencia al motor para funcionar", "needs time to build boost (turbo lag)", "necesita tiempo para generar presión (turbo lag)"),
        ("In the GTI story", "En la historia del GTI", "G60, 1990", "G60, 1990", "the Mk4 1.8 L, then the Mk5, Mk6 and Mk8 engines", "el 1.8 L del Mk4 y luego los motores del Mk5, Mk6 y Mk8"),
    ],
    "head_en": ("", "Supercharger", "Turbocharger"),
    "head_es": ("", "Compresor", "Turbo"),
    "note_en": "General engineering from two peer-reviewed reviews of boosted petrol engines; the last row is from VW’s history page. Neither review tested a Golf.",
    "note_es": "Ingeniería general de dos artículos de revisión arbitrados sobre motores de gasolina sobrealimentados; la última fila viene de la página de historia de VW. Ninguna revisión probó un Golf.",
    "src": ["hu2015", "hu2016", "vw-history"],
}

ANATOMY = {
    "title_en": "Anatomy of a front axle (Mk7, 2013)",
    "title_es": "Anatomía de un eje delantero (Mk7, 2013)",
    "items": [
        ("Front suspension", "Suspensión delantera",
         "MacPherson struts with a newly developed low wishbone, a centrally placed subframe built for transverse stiffness, and a fully tubular anti-roll bar with a GTI-specific rate.",
         "Puntales MacPherson con un brazo inferior de nuevo diseño, un subchasis central pensado para la rigidez transversal y una barra estabilizadora totalmente tubular con una dureza propia del GTI."),
        ("Rear suspension", "Suspensión trasera",
         "What VW calls a modular performance rear suspension: a trailing link, a spring link and an upper transverse link, with toe and camber set by eccentric bolts.",
         "Lo que VW llama suspensión trasera modular de alto desempeño: un brazo longitudinal, un brazo de resorte y un brazo transversal superior, con convergencia y caída ajustadas con tornillos excéntricos."),
        ("Ride height", "Altura", "15 mm lower than the less powerful Golfs.", "15 mm más baja que la de los Golf menos potentes."),
        ("Dampers (DCC, optional)", "Amortiguadores (DCC, opcional)",
         "Second-generation adaptive dampers with Comfort, Normal and Sport modes; rebound and compression can be varied independently.",
         "Amortiguadores adaptativos de segunda generación con modos Comfort, Normal y Sport; extensión y compresión se ajustan por separado."),
        ("Stability control", "Control de estabilidad",
         "A two-stage switch: a short press turns traction control off; holding it for more than three seconds puts ESC in a Sport mode that intervenes later.",
         "Un botón de dos etapas: al presionarlo brevemente se apaga el control de tracción; al mantenerlo más de tres segundos, pone el ESC en un modo Sport que interviene más tarde."),
        ("Brakes", "Frenos",
         "GTI: 314 × 30 mm ventilated front discs, 300 × 12 mm solid rear. GTI Performance: 340 × 30 mm front and 310 × 22 mm rear, ventilated all round.",
         "GTI: discos delanteros ventilados de 314 × 30 mm y traseros sólidos de 300 × 12 mm. GTI Performance: 340 × 30 mm adelante y 310 × 22 mm atrás, ventilados en las cuatro ruedas."),
    ],
    "src": ["vw-mk7-chassis"],
}

EDITIONS = [
    ("1983", "Pirelli GTI", "112 PS", "vw-history"),
    ("1996", "20 Years of GTI", "—", "vw-history"),
    ("2001", "25 Years of the GTI", "180 PS", "vw-history"),
    ("2006", "Edition 30", "230 PS", "vw-history"),
    ("2011", "Edition 35", "235 PS", "vw-history"),
    ("2016", "Clubsport", "265 PS (290 PS boost)", "vw-history"),
    ("2016", "Clubsport S", "310 PS", "vw-history"),
    ("2019", "GTI TCR", "290 PS", "vw-history"),
    ("2021", "Clubsport 45", "300 PS", "vw-history"),
    ("2025", "GTI EDITION 50 (shown; 2026 launch)", "325 PS", "vw-history"),
]
EDITIONS_TEXT = {
    "title_en": "The special editions, as VW lists them",
    "title_es": "Las ediciones especiales, según las enumera VW",
    "note_en": "Volkswagen’s PS figures from one page, so the units match. The 1996 edition’s output is not stated there.",
    "note_es": "Cifras en PS de Volkswagen tomadas de una sola página, para que las unidades coincidan. La potencia de la edición de 1996 no se indica ahí.",
}

# ---------------------------------------------------------------------------------------------------------------
# Cross-generation track times (pinned in skills/classics/cc01/verify_cc01_mechanics.py)
# ---------------------------------------------------------------------------------------------------------------
LAPS = [
    ("Mk4", "Golf IV GTI “25 Jahre GTI”", 2002, 180, "8:54", 534.0, "Horst von Saurma", "not stated", ""),
    ("Mk5", "Golf V GTI DSG", 2005, 200, "8:53", 533.0, "Horst von Saurma", "Michelin Pilot Exalto", ""),
    ("Mk6", "Golf VI GTI “35 Jahre GTI”", 2011, 235, "8:38", 518.0, "Horst von Saurma", "Dunlop Sport Maxx GT", ""),
    ("Mk7", "Golf VII GTI Performance", 2013, 230, "8:29", 509.0, "Horst von Saurma", "Bridgestone Potenza S001", ""),
    ("Mk7", "Golf VII GTI Clubsport", 2016, 265, "8:07", 487.0, "Christian Gebhardt", "Michelin Pilot Sport Cup", "20,600 m"),
    ("Mk7", "Golf VII GTI Clubsport S", 2016, 310, "7:57", 477.0, "Christian Gebhardt", "Michelin Pilot Sport Cup 2", "20,600 m"),
    ("Mk7", "Golf VII GTI TCR", 2019, 290, "8:04.92", 484.92, "Christian Gebhardt", "Michelin Pilot Sport Cup 2 N0", "20,600 m"),
    ("Mk8", "Golf VIII GTI Clubsport “45 Jahre GTI”", 2021, 300, "8:02.66", 482.66, "Christian Gebhardt", "Michelin Pilot Sport Cup 2 N0", "20,600 m"),
]

LAPS_TEXT = {
    "title_en": "Ghost race: nineteen years on one circuit",
    "title_es": "Carrera fantasma: diecinueve años en un mismo circuito",
    "intro_en": "Lap-time lists usually mix manufacturers’ record runs, magazines and amateurs. This one does not. Every "
                "time below comes from one German magazine, sport auto, timing a Golf GTI on the Nürburgring "
                "Nordschleife for its Supertest, from the 2002 “25 Jahre GTI” to the 2021 Clubsport 45. Press start and "
                "all eight run at once.",
    "intro_es": "Las listas de tiempos por vuelta suelen mezclar récords de fábrica, revistas y aficionados. Esta no. Cada "
                "tiempo de abajo viene de una sola revista alemana, sport auto, cronometrando un Golf GTI en el "
                "Nordschleife de Nürburgring para su Supertest, desde el “25 Jahre GTI” de 2002 hasta el Clubsport 45 "
                "de 2021. Presiona iniciar y los ocho corren a la vez.",
    "read_en": "What the numbers say, in our arithmetic: the 2016 Clubsport S was 57 seconds quicker than the 2002 car on "
               "the same magazine’s lap, and the regular-production GTI improved by 25 seconds between the 2002 and 2013 "
               "tests. The specials of 2016 to 2021 sit within ten seconds of each other.",
    "read_es": "Lo que dicen los números, según nuestro cálculo: el Clubsport S de 2016 fue 57 segundos más rápido que el "
               "auto de 2002 en la vuelta de la misma revista, y el GTI de producción normal mejoró 25 segundos entre las "
               "pruebas de 2002 y 2013. Las ediciones especiales de 2016 a 2021 quedan a no más de diez segundos entre sí.",
    "caveat_en": "Same magazine and circuit, not the same day: tyres, drivers, weather and track surface changed over "
                 "nineteen years, and the older rows are listed to the second. sport auto uses a 20,600 m configuration, "
                 "about 200 m shorter than a full lap; the list states it for the 2016 to 2021 rows and leaves it blank "
                 "for the older ones. Volkswagen’s own 7:49.21 record run for the Clubsport S was a different, "
                 "manufacturer-run test and is not part of this comparison. No sport auto times for the Mk1, Mk2 or Mk3 "
                 "are in the list: not stated.",
    "caveat_es": "Misma revista y mismo circuito, no el mismo día: llantas, pilotos, clima y pavimento cambiaron en "
                 "diecinueve años, y las filas más antiguas están dadas al segundo. sport auto usa una configuración de "
                 "20,600 m, unos 200 m más corta que la vuelta completa; la lista la indica para las filas de 2016 a 2021 "
                 "y la deja en blanco para las anteriores. El récord de 7:49.21 que Volkswagen corrió con el Clubsport S "
                 "fue otra prueba, hecha por el fabricante, y no forma parte de esta comparación. En la lista no hay "
                 "tiempos de sport auto para el Mk1, Mk2 ni Mk3: no se indica.",
    "loop_en": "Schematic loop, not the Nordschleife’s shape. Each dot runs at the constant average speed its lap time "
               "implies; real laps speed up and slow down. Time is compressed 100 to 1. Hollow dots mark rows where the list leaves the "
               "track length blank.",
    "loop_es": "Circuito esquemático, no el trazado del Nordschleife. Cada punto corre a la velocidad promedio constante "
               "que implica su tiempo; las vueltas reales aceleran y frenan. El tiempo está comprimido 100 a 1. Los puntos huecos marcan las filas "
               "donde la lista deja en blanco la longitud del circuito.",
}

SILENT = [
    {
        "q_en": "Which fuel-injection system did the 1976 car use?",
        "q_es": "¿Qué sistema de inyección usaba el auto de 1976?",
        "a_en": "VW’s archive says “injection engine” and stops there. Not stated.",
        "a_es": "El archivo de VW dice “motor de inyección” y ahí se detiene. No se indica.",
    },
    {
        "q_en": "How much did each generation weigh?",
        "q_es": "¿Cuánto pesaba cada generación?",
        "a_en": "VW gives the Mk1’s 810 kg base weight and the Mk7’s saving of up to 42 kg. We found no like-for-like "
                "figure for every generation, so there is no weight chart here.",
        "a_es": "VW da el peso base de 810 kg del Mk1 y el ahorro de hasta 42 kg del Mk7. No encontramos una cifra "
                "comparable para cada generación, así que aquí no hay gráfica de pesos.",
    },
    {
        "q_en": "When exactly did the Mk3 16V arrive?",
        "q_es": "¿Cuándo llegó exactamente el Mk3 16V?",
        "a_en": "Two VW pages disagree (1992 and 1993). Not settled here.",
        "a_es": "Dos páginas de VW no coinciden (1992 y 1993). Aquí no se resuelve.",
    },
    {
        "q_en": "Which gearbox did the Mk5’s DSG option use internally?",
        "q_es": "¿Qué caja usaba por dentro la DSG opcional del Mk5?",
        "a_en": "VW says six speeds and dual clutch. The internal type code is not stated in the pages we read.",
        "a_es": "VW dice seis velocidades y doble embrague. El código interno no aparece en las páginas que leímos.",
    },
]

CLOSING = [
    {
        "en": "Across fifty years the answers changed almost completely: eight valves to sixteen, natural aspiration to a "
              "supercharger and then direct-injection turbos, one clutch to two, an open differential to brakes and then "
              "a 1,600 Nm clutch pack, and finally software coordinating all of it. The brief, as we framed it, stayed put.",
        "es": "En cincuenta años las respuestas cambiaron casi por completo: de ocho válvulas a dieciséis, de aspiración "
              "natural a un compresor y luego turbos de inyección directa, de un embrague a dos, de un diferencial abierto "
              "a los frenos y un paquete de embragues de 1,600 Nm, y al final un software que lo coordina todo. El reto, "
              "tal como lo planteamos, se quedó en su lugar.",
        "src": [],
    },
]

# Maintainer decision 2026-11-15: keep EGG and EGG_SIDE captions, links, and src/images/classics/ files untouched.
EGG = {
    "button_en": "Lift the bonnet",
    "button_es": "Levantar el cofre",
    "close_en": "Close the bonnet",
    "close_es": "Cerrar el cofre",
    "caption_en": "A 2018 Mk7.5 Golf GTI with a Cobb Stage 2 tune and BBS wheels, in Dark Iron Blue Metallic.",
    "caption_es": "Un Golf GTI Mk7.5 2018 con reprogramación Cobb Stage 2 y rines BBS, en Dark Iron Blue Metallic.",
    "alt_en": "A Mk7.5 Golf GTI with its bonnet up and the engine bay showing.",
    "alt_es": "Un Golf GTI Mk7.5 con el cofre levantado y el compartimento del motor a la vista.",
    "links": [("Cobb", "https://www.cobbtuning.com/"), ("BBS", "https://www.bbs.com/")],
    "image": "images/classics/golf-gti-hood-up.jpg",
    "width": 1030,
    "height": 870,
}

EGG_SIDE = {
    "caption_en": "The same car on track, on MOMO wheels.",
    "caption_es": "El mismo auto en pista, con rines MOMO.",
    "alt_en": "The same Mk7.5 Golf GTI at speed on a circuit, seen from the side, with two helmeted people inside.",
    "alt_es": "El mismo Golf GTI Mk7.5 a velocidad en un circuito, visto de lado, con dos personas con casco adentro.",
    "links": [("MOMO", "https://momo.com/")],
    "image": "images/classics/golf-gti-side-track.jpg",
    "width": 1024,
    "height": 682,
}

# ---------------------------------------------------------------------------------------------------------------
# Part VI · Mechanics Lab (models 1–3 checked by skills/classics/cc01/verify_cc01_mechanics.py; 4–5 added beside them)
# ---------------------------------------------------------------------------------------------------------------
LAB = {
    "title_en": "Mechanics Lab: five models, worked in the open",
    "title_es": "Laboratorio de mecánica: la física, resuelta en cinco modelos",
    "intro_en": "The story above describes what each generation did. This part puts equations to five mechanisms behind "
                "those moves: front differential torque split, Nordschleife lap average speeds, two-mass corner frequencies, "
                "lateral cornering load transfer with yaw couple, and coaxial dual-clutch powershift handover. Any input "
                "not from a primary source is marked MODEL; skills/classics/cc01/verify_cc01_mechanics.py recomputes and checks every figure.",
    "intro_es": "La historia de arriba describe lo que hizo cada generación. Esta parte pone ecuaciones a cinco mecanismos: "
                "reparto de par en el eje delantero, velocidades promedio por vuelta, frecuencias del cuarto de auto, "
                "transferencia lateral con par de guiñada y traslape coaxial de doble embrague. Toda entrada sin fuente "
                "primaria se marca MODELO; skills/classics/cc01/verify_cc01_mechanics.py recalcula y comprueba cada cifra.",
    "diff_h_en": "1 · Why an open differential runs out of grip",
    "diff_h_es": "1 · Por qué un diferencial abierto se queda sin agarre",
    "diff_en": "An open differential gives each driven wheel half the axle torque. A wheel can only push the road as hard as "
               "its grip allows, roughly the friction coefficient times the load on it times the wheel radius. In a hard "
               "corner the inside front wheel carries less load, so its limit is lower, and because both halves must stay "
               "equal, the whole axle is capped at twice that smaller limit. Brake the inside wheel and the differential "
               "can hold more torque before that wheel spins, so the outside wheel gets more. A clutch pack instead moves "
               "torque directly from the faster, spinning wheel to the slower one, up to its locking torque. Volkswagen "
               "gives 1,600 Nm for the Mk7 GTI Performance front lock. The table runs the same three cases at 3,000 Nm demand.",
    "diff_es": "Un diferencial abierto le da a cada rueda motriz la mitad del par del eje. Una rueda solo puede empujar el "
               "camino tanto como su agarre lo permite, más o menos el coeficiente de fricción por la carga sobre ella por "
               "el radio de la rueda. En una curva cerrada, la rueda delantera interior lleva menos carga, así que su "
               "límite es más bajo, y como las dos mitades deben ser iguales, todo el eje queda limitado al doble de ese "
               "límite menor. Si se frena la rueda interior, el diferencial puede sostener más par antes de que esa rueda "
               "patine, y la rueda exterior recibe más. Un paquete de embragues, en cambio, pasa par directamente de la "
               "rueda más rápida, la que patina, a la más lenta, hasta su par de bloqueo. Volkswagen da 1,600 Nm para el "
               "bloqueo delantero del Mk7 GTI Performance. La tabla corre los mismos tres casos al tope de 3,000 Nm.",
    "laps_h_en": "2 · Lap times as average speeds",
    "laps_h_es": "2 · Tiempos por vuelta como velocidades promedio",
    "laps_en": "Divide the lap length by the lap time and you get an average speed. The source gives the 20,600 m sport auto "
               "configuration only for the 2016 to 2021 rows, so only those four get a speed here; the older rows stay "
               "blank rather than borrow a length the list does not state. These are DERIVED values, our arithmetic, and "
               "an average hides every braking zone and straight.",
    "laps_es": "Divide la longitud de la vuelta entre el tiempo y obtienes una velocidad promedio. La fuente da la "
               "configuración de 20,600 m de sport auto solo para las filas de 2016 a 2021, así que solo esas cuatro "
               "tienen velocidad aquí; las filas anteriores quedan en blanco en lugar de tomar prestada una longitud que la "
               "lista no indica. Son valores DERIVADOS, nuestro cálculo, y un promedio esconde cada zona de frenado y cada "
               "recta.",
    "qc_h_en": "3 · Unsprung mass and the two ways a corner bounces",
    "qc_h_es": "3 · Masa no suspendida y las dos formas en que rebota una esquina",
    "qc_en": "Engineers model one corner of a car as two masses and two springs: the body on the suspension spring, and the "
             "wheel on the tyre. The model has two natural frequencies, a slow body bounce and a fast wheel hop, found "
             "from the masses and stiffnesses. Research on this model reports that unsprung mass mainly moves the wheel-hop "
             "mode, tyre stiffness mainly shapes it too, and suspension stiffness sets the bounce; less wheel hop means "
             "better road holding. Move the slider to change the unsprung mass and watch which frequency moves. The rates "
             "are MODEL values, not a Golf’s.",
    "qc_es": "Los ingenieros modelan una esquina del auto como dos masas y dos resortes: la carrocería sobre el resorte de "
             "la suspensión y la rueda sobre la llanta. El modelo tiene dos frecuencias naturales, un rebote lento de la "
             "carrocería y un salto rápido de la rueda, que salen de las masas y las rigideces. La investigación sobre este "
             "modelo reporta que la masa no suspendida mueve sobre todo el modo de salto de la rueda, que la rigidez de la "
             "llanta también lo define y que la rigidez de la suspensión fija el rebote; menos salto de rueda significa "
             "mejor agarre al camino. Mueve el control para cambiar la masa no suspendida y observa qué frecuencia se "
             "mueve. Las rigideces son valores de MODELO, no las de un Golf.",
    "yaw_h_en": "4 · Lateral weight transfer & direct yaw moment M_z",
    "yaw_h_es": "4 · Transferencia lateral de carga y momento de guiñada M_z",
    "yaw_en": "Across increasing lateral acceleration a_y from straight acceleration (0.00 g) to 0.70 g cornering, vertical "
              "load shifts linearly off the inside tyre onto the outside tyre. An open differential stays symmetric (0 kN·m "
              "yaw assist) while shifting torque asymmetrically with XDS+ (500 Nm brake limit) or the 1,600 Nm VAQ lock "
              "generates an outward tractive force difference (F_out − F_in) across a 1.54 m MODEL track width.",
    "yaw_es": "Al crecer la aceleración lateral a_y desde recta (0.00 g) hasta 0.70 g en curva, la carga vertical migra "
              "del neumático interior al exterior. Un diferencial abierto queda simétrico (0 kN·m de guiñada), mientras XDS+ "
              "(límite de freno 500 Nm) o el bloqueo VAQ de 1,600 Nm producen diferencia tractora (F_out − F_in) sobre un ancho "
              "de vía MODELO de 1.54 m.",
    "dct_h_en": "5 · Coaxial dual-clutch ratio spacing & handover kinematics",
    "dct_h_es": "5 · Escalones de relación coaxial y cinemática de traslape",
    "dct_en": "On a MODEL 6-speed gearbox shifting at 6,000 rpm under 280 Nm crankshaft torque across a 0.20 s clutch handover "
              "overlap, lower gears carry steeper step drops Δω that require larger friction dissipation in the wet "
              "clutch packs while output tractive torque remains unbroken across every upshift.",
    "dct_es": "En una caja MODELO de 6 velocidades cambiando a 6,000 rpm con 280 Nm en cigüeñal y 0.20 s de traslape, los "
              "cambios bajos absorben mayor salto de giro Δω en los embragues húmedos manteniendo continuo el par al camino.",
    "verify_h_en": "Run the independent verifier yourself",
    "verify_h_es": "Ejecuta el verificador independiente",
    "verify_en": "The verifier lives at skills/classics/cc01/verify_cc01_mechanics.py, with a SKILL.md beside it. It uses only "
                 "the Python standard library, recomputes torque split, lap speeds, and quarter-car frequencies "
                 "with its own code, checks them against this page in both languages, and fails when a defect is planted.",
    "verify_es": "El verificador está en skills/classics/cc01/verify_cc01_mechanics.py, con un SKILL.md al lado. Usa solo la "
                 "biblioteca estándar de Python, recalcula reparto de par, velocidades por vuelta y frecuencias "
                 "del cuarto de auto con su propio código, las compara con esta página en ambos idiomas y falla si se le planta un defecto.",
}

FOOTER_NOTE = {
    "en": "Not affiliated with or endorsed by Volkswagen AG. Volkswagen, Golf and GTI are trademarks of Volkswagen AG, "
          "used here only to identify the cars. Original schematics and 15 Crossref/Scite-checked peer-reviewed papers "
          "(zero retractions) explain mechanisms in general; numbers marked MODEL illustrate physics only. For learning, not buying, tuning or driving advice.",
    "es": "Sin afiliación ni respaldo de Volkswagen AG. Volkswagen, Golf y GTI son marcas de Volkswagen AG, usadas aquí "
          "solo para identificar los autos. Esquemas originales y 15 artículos arbitrados verificados en Crossref/Scite "
          "(sin retractaciones) explican mecanismos en general; las cifras marcadas MODELO ilustran física únicamente. Para aprender; no es consejo de compra, modificación ni manejo.",
}

# Phrases that may not appear anywhere on the page (tests/test_cult_classics.py).
BANNED = [
    "first hot hatch", "best hot hatch", "legendary", "iconic", "greatest", "my car", "our car", "owner's car",
    "primer hot hatch", "legendario", "icónico", "mi auto", "nuestro auto",
]
