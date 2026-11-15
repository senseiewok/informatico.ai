"""CC.01 · One Brief, Eight Answers — the Golf GTI as an engineering story (single source of truth).

Every number on the page lives in this module next to the source it came from. Rules (proposal reviewed by a
two-seat council, 2026-11-15):

- Volkswagen statements are attributed to Volkswagen ("VW says"); they are company statements, not independent tests.
- Peer-reviewed papers explain the mechanisms in general terms; none of them tested a Golf GTI, and the page says so.
- Retail pages and forum posts are never sources here. Anything a source does not state is written "not stated".
- No car on the page is anyone's car: captions, alt text and code comments name no owner.

Silhouette note: the eight background profiles are schematic hatchback outlines drawn freehand from general
proportions (boxy to crisp) for this page on 2026-11-15. They were not traced from photographs, press images or
design drawings, and they make no dimensional claim.
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
    "Ocho generaciones del Golf GTI, una jugada de ingeniería cada una: inyección, dieciséis válvulas, turbo, dos "
    "embragues, diferenciales por freno y por embrague, software. Con fuentes e interactivo.",
)

# ---------------------------------------------------------------------------------------------------------------
# Sources. "kind": vw (company statement), press (independent coverage), paper (peer-reviewed, verified in Scite
# 2026-11-15: no retraction, no concern, no contrasting evidence flagged).
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
        "label": "Volkswagen Newsroom, “Golf GTI Mk1” (history of the new Golf GTI)",
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
}

KIND_LABEL = {
    "vw": ("VW", "VW"),
    "press": ("Press", "Prensa"),
    "paper": ("Paper", "Artículo"),
}

HERO = {
    "kicker_en": "Cult Classics · CC.01 · Engineering",
    "kicker_es": "Clásicos de culto · CC.01 · Ingeniería",
    "title_en": "One Brief, Eight Answers",
    "title_es": "Un reto, ocho respuestas",
    "dek_en": "The Golf GTI, told one engineering move at a time.",
    "dek_es": "El Golf GTI, contado jugada de ingeniería por jugada de ingeniería.",
    "reading_en": "13 min read",
    "reading_es": "15 min de lectura",
}

BRIEF_NOTE = {
    "en": "The “brief” in the title is our framing, not Volkswagen’s: make a sensible family hatchback properly quick "
          "without making it any less sensible. Each card below shows how one generation answered it.",
    "es": "El “reto” del título es una lectura nuestra, no de Volkswagen: hacer que un hatchback familiar y sensato "
          "sea rápido de verdad sin que deje de ser sensato. Cada tarjeta muestra cómo respondió una generación.",
}

OPENING = [
    {
        "en": "Volkswagen’s own newsroom tells the beginning plainly. In 1974 about half a dozen people inside the company, "
              "among them the chief press officer of the day, Anton Konrad, started work on a sporty Golf that nobody had "
              "asked them for. A prototype paced the field at the Nürburgring in the summer of 1975, and the car went on "
              "sale in Germany in June 1976.",
        "es": "La sala de prensa de Volkswagen cuenta el comienzo sin adornos. En 1974, alrededor de media docena de personas "
              "dentro de la empresa, entre ellas el entonces jefe de prensa, Anton Konrad, empezaron a trabajar en un Golf "
              "deportivo que nadie les había pedido. Un prototipo fue auto de seguridad en Nürburgring en el verano de 1975, "
              "y el auto salió a la venta en Alemania en junio de 1976.",
        "src": ["vw-mk1-story", "vw-history"],
    },
    {
        "en": "The plan was modest: about 5,000 cars. Volkswagen’s history page puts the final count of the first "
              "generation at 461,690. Everything that follows on this page is an attempt to explain, with sources, how "
              "a quiet side project kept answering the same question for fifty years.",
        "es": "El plan era modesto: unos 5,000 autos. La página de historia de Volkswagen cifra la producción final de la "
              "primera generación en 461,690. Todo lo que sigue en esta página intenta explicar, con fuentes, cómo un "
              "proyecto discreto siguió respondiendo la misma pregunta durante cincuenta años.",
        "src": ["vw-history"],
    },
]

# One card per generation. "plate" rows are (label_en, label_es, value, source key).
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
                   "implicaba más de 180 km/h. Es un índice de la llanta, no una velocidad máxima medida.",
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
                   "five-cylinder, also at 150 PS, that rose to 170 PS in 2000, and turbodiesels from 110 to 150 PS. "
                   "Model names varied by market, so read that list as VW’s, not as one country’s price sheet. The "
                   "2001 “25 Years of the GTI” edition used a 180 PS turbocharged engine.",
        "body_es": "VW enumera para la cuarta generación un motor de gasolina turbo de 1.8 litros con 150 PS, junto a un "
                   "cinco cilindros de 2.3 litros, también de 150 PS, que subió a 170 PS en 2000, y turbodiésel de 110 a "
                   "150 PS. Los nombres de versión cambiaban según el mercado, así que esa lista es la de VW, no la de "
                   "un solo país. La edición “25 años del GTI” de 2001 usó un motor turbo de 180 PS.",
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
                   "6.9 s with it against 7.2 s with the manual. The gearbox has its own section below, because how it "
                   "changes gear is the interesting part.",
        "body_es": "Presentada en el Salón de París en septiembre de 2004, la quinta generación usó un motor turbo de 2.0 "
                   "litros con 200 PS. VW ofreció como opción una caja de doble embrague de 6 velocidades (DSG) y cita "
                   "0–100 km/h en 6.9 s con ella frente a 7.2 s con la manual. La caja tiene su propia sección más abajo, "
                   "porque lo interesante es cómo cambia de velocidad.",
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
                   "anything mechanically: it brakes the inside front wheel. The differential bench below shows why that "
                   "works.",
        "body_es": "La sexta generación tenía 210 PS. VW dice que fue el primer GTI con el bloqueo electrónico de "
                   "diferencial XDS de serie, y que Hans-Joachim Stuck participó en la puesta a punto del chasis. El XDS "
                   "no bloquea nada mecánicamente: frena la rueda delantera interior. El banco de diferenciales de más "
                   "abajo muestra por qué funciona.",
        "plate": [
            ("Output", "Potencia", "210 PS", "vw-history"),
            ("New as standard", "Nuevo de serie", "XDS (brake-based)", "vw-history"),
        ],
    },
    {
        "id": "mk7", "gen": "Mk7", "years": "2013–2019",
        "move_en": "A platform, and a clutch pack at the front axle",
        "move_es": "Una plataforma y un paquete de embragues en el eje delantero",
        "body_en": "The seventh generation sat on Volkswagen’s MQB platform, and VW says the GTI was up to 42 kg lighter "
                   "than its predecessor. It started at 220 PS, with a GTI Performance at 230 PS. The Performance model "
                   "added what VW calls a front differential lock: a multi-plate clutch between the right driveshaft and "
                   "the differential case, squeezed by a piston pump driven by an electric motor, with the locking torque "
                   "proportional to the pump pressure. The standard car used XDS+, which brakes the inside wheels. VW "
                   "also lists progressive steering, a body 15 mm lower than lesser Golfs, and the 2017 update to 230 PS "
                   "and 245 PS.",
        "body_es": "La séptima generación usó la plataforma MQB de Volkswagen, y VW dice que el GTI era hasta 42 kg más "
                   "ligero que su antecesor. Empezó con 220 PS, con un GTI Performance de 230 PS. El Performance sumó lo "
                   "que VW llama bloqueo del diferencial delantero: un embrague multidisco entre la flecha derecha y la "
                   "caja del diferencial, apretado por una bomba de pistón movida por un motor eléctrico, con un par de "
                   "bloqueo proporcional a la presión de la bomba. El auto estándar usaba XDS+, que frena las ruedas "
                   "interiores. VW también menciona la dirección progresiva, una carrocería 15 mm más baja que la de los "
                   "Golf menos potentes y la actualización de 2017 a 230 PS y 245 PS.",
        "plate": [
            ("Platform", "Plataforma", "MQB", "vw-mk7"),
            ("Weight vs Mk6 (VW)", "Peso vs Mk6 (VW)", "up to 42 kg lighter", "vw-mk7"),
            ("Front lock (Performance)", "Bloqueo delantero (Performance)", "Multi-plate, pump-pressurised", "vw-mk7-chassis"),
            ("Steering", "Dirección", "2.1 turns lock to lock (2.75 on lesser Golfs)", "vw-mk7-chassis"),
        ],
        "egg": True,
    },
    {
        "id": "mk8", "gen": "Mk8", "years": "2020–",
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
        "plate": [
            ("Output at launch", "Potencia inicial", "245 PS · 370 Nm", "vw-history"),
            ("Gearbox", "Caja", "7-speed DSG", "vw-history"),
            ("2024 update", "Actualización 2024", "265 PS", "vw-history"),
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
}
CLUBSPORT_S = {
    "en": "In 2016 the Golf GTI Clubsport S lapped the Nürburgring Nordschleife in 7:49.21, which Volkswagen announced as "
          "the front-wheel-drive production car record at the time; the previous mark reported in the press was the "
          "Honda Civic Type R’s 7:50.63. The engineering was about mass in the right places. Volkswagen kept front-wheel "
          "drive rather than the Golf R’s all-wheel drive and fitted a manual to save weight, and used an aluminium front "
          "subframe and aluminium brake carriers, which cut unsprung mass. VW also says the stability control was retuned "
          "to intervene later.",
    "es": "En 2016 el Golf GTI Clubsport S dio la vuelta al Nordschleife de Nürburgring en 7:49.21, que Volkswagen anunció "
          "como récord para autos de producción con tracción delantera en ese momento; la marca anterior citada por la "
          "prensa era el 7:50.63 del Honda Civic Type R. La ingeniería se trató de poner la masa en el lugar correcto. "
          "Volkswagen mantuvo la tracción delantera en lugar de la tracción integral del Golf R y montó una caja manual "
          "para ahorrar peso, y usó un subchasis delantero y soportes de freno de aluminio, que reducen la masa no "
          "suspendida. VW también dice que el control de estabilidad se reajustó para intervenir más tarde.",
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
              "supercharger and then turbos, one clutch to two, an open differential to brakes and then a clutch pack, "
              "and finally a controller that coordinates all of it. The brief, as we have framed it, stayed put.",
        "es": "En cincuenta años las respuestas cambiaron casi por completo: de ocho válvulas a dieciséis, de aspiración "
              "natural a un compresor y luego a los turbos, de un embrague a dos, de un diferencial abierto a los frenos y "
              "luego a un paquete de embragues, y al final un controlador que coordina todo. El reto, tal como lo "
              "planteamos, se quedó en su lugar.",
        "src": [],
    },
]

EGG = {
    "button_en": "Lift the bonnet",
    "button_es": "Levantar el cofre",
    "close_en": "Close the bonnet",
    "close_es": "Cerrar el cofre",
    "caption_en": "A Mk7.5 Golf GTI in Dark Iron Blue Metallic, on BBS wheels.",
    "caption_es": "Un Golf GTI Mk7.5 en Dark Iron Blue Metallic, con rines BBS.",
    "alt_en": "A Mk7.5 Golf GTI with its bonnet up and the engine bay showing.",
    "alt_es": "Un Golf GTI Mk7.5 con el cofre levantado y el compartimento del motor a la vista.",
    # Maintainer decision 2026-11-15: the caption names the paint and the wheel maker; the owner is the source
    # for both (retail paint pages stay off the page). The BBS link points to the maker, not to a product claim.
    "link_label": "BBS",
    "link_url": "https://www.bbs.com/",
    "image": "images/classics/golf-gti-hood-up.jpg",
    "width": 1030,
    "height": 870,
}

# Second photo in the bonnet reveal (maintainer, 2026-11-15): the same car on track, people kept as shot, plate rebuilt.
EGG_SIDE = {
    "caption_en": "The same car on track.",
    "caption_es": "El mismo auto en pista.",
    "alt_en": "The same Mk7.5 Golf GTI at speed on a circuit, seen from the side, with two helmeted people inside.",
    "alt_es": "El mismo Golf GTI Mk7.5 a velocidad en un circuito, visto de lado, con dos personas con casco adentro.",
    "image": "images/classics/golf-gti-side-track.jpg",
    "width": 1024,
    "height": 682,
}

FOOTER_NOTE = {
    "en": "Not affiliated with or endorsed by Volkswagen AG. Volkswagen, Golf and GTI are trademarks of Volkswagen AG, "
          "used here only to identify the cars. All drawings are original schematics. For learning, not buying, tuning "
          "or driving advice.",
    "es": "Sin afiliación ni respaldo de Volkswagen AG. Volkswagen, Golf y GTI son marcas de Volkswagen AG, usadas aquí "
          "solo para identificar los autos. Todos los dibujos son esquemas originales. Para aprender; no es consejo de "
          "compra, de modificación ni de manejo.",
}

# ---------------------------------------------------------------------------------------------------------------
# Long-form (magazine) structure: five parts, each with an opener, its generation cards and an interlude.
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
                      "Golf con un motor más fuerte, una postura más baja y barras estabilizadoras en ambos ejes. En nuestra lectura, la jugada de ingeniería fue la contención.",
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
        "pull_es": "Nuestra lectura: la jugada de ingeniería fue la contención.",
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
                      "choice for fuel efficiency, but it needs a perceptible moment to build boost: the delay drivers "
                      "call turbo lag.",
                "es": "A partir de la cuarta generación, los motores turbo de gasolina se vuelven la línea principal del GTI "
                      "en la página de historia de VW: un 1.8 litros turbo en el Mk4, junto a un cinco cilindros, y luego "
                      "motores turbo en el Mk5, el Mk6 y el Mk8. ¿Por qué turbo, si el G60 ya había probado un compresor? VW no lo dice; la investigación sobre "
                      "motores resume el intercambio general sin rodeos. Un compresor toma su energía directo del cigüeñal, lo que ayuda a "
                      "que el motor responda al acelerador. Un turbo se mueve con el flujo de escape del motor y es la "
                      "opción más adoptada por su eficiencia en combustible, pero necesita un momento "
                      "perceptible para generar presión: el retraso que los conductores llaman turbo lag.",
                "src": ["hu2015", "hu2016"],
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
                      "seventh answered twice, with XDS+ on the standard car and a clutch-pack front differential lock on "
                      "the Performance model. VW’s 2013 launch material is unusually detailed about the hardware, and the "
                      "anatomy section below walks through it.",
                "es": "Con más de 200 PS en las ruedas delanteras, el siguiente problema fue ponerlos en el piso. La sexta "
                      "generación respondió con los frenos: el XDS, de serie en un GTI por primera vez, según VW. La séptima "
                      "respondió dos veces, con XDS+ en el auto estándar y un bloqueo del diferencial delantero por "
                      "embragues en el Performance. El material de lanzamiento de VW de 2013 es inusualmente detallado "
                      "sobre el hardware, y la sección de anatomía más abajo lo recorre.",
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
        "id": "part-5", "numeral": "V", "years": "2020–",
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
# Cross-generation track times: one magazine (sport auto), one circuit (Nordschleife), as compiled in Wikipedia's
# lap-time list (raw wikitext read 2026-11-15). Seconds are exact as listed; older rows are given to the second.
# (gen, car as listed, year, PS, time string, seconds, driver, tyres, config) — config "" where the row is blank.
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


# ---------------------------------------------------------------------------------------------------------------
# Part VI · Mechanics Lab (2026-11-15 council: magazine-first article plus a computed physics companion, a SKILL.md
# and a verifier). Numbers come from tools/folios/classics/cc01_mechanics.py; MODEL values are illustrative.
# ---------------------------------------------------------------------------------------------------------------
LAB = {
    "title_en": "Mechanics Lab: the physics, worked",
    "title_es": "Laboratorio de mecánica: la física, resuelta",
    "intro_en": "The story above describes what each generation did. This part shows why it works, with three small models "
                "you can run. Any number that is not from a source is marked MODEL: an illustrative value chosen to make "
                "the mechanism visible, not a measurement of a Golf. A verifier in the repository recomputes every number "
                "here and fails if one is wrong.",
    "intro_es": "La historia de arriba describe lo que hizo cada generación. Esta parte muestra por qué funciona, con tres "
                "modelos pequeños que puedes correr. Cualquier cifra que no venga de una fuente está marcada como MODELO: "
                "un valor ilustrativo elegido para que se vea el mecanismo, no una medición de un Golf. Un verificador en "
                "el repositorio recalcula cada número de aquí y falla si alguno está mal.",
    "diff_h_en": "1 · Why an open differential runs out of grip",
    "diff_h_es": "1 · Por qué un diferencial abierto se queda sin agarre",
    "diff_en": "An open differential gives each driven wheel half the axle torque. A wheel can only push the road as hard as "
               "its grip allows, roughly the friction coefficient times the load on it times the wheel radius. In a hard "
               "corner the inside front wheel carries less load, so its limit is lower, and because both halves must stay "
               "equal, the whole axle is capped at twice that smaller limit. Brake the inside wheel and the differential "
               "can hold more torque before that wheel spins, so the outside wheel gets more. A clutch pack instead moves "
               "torque directly from the faster, spinning wheel to the slower one, up to its locking torque. Volkswagen "
               "gives 1,600 Nm for the Mk7 GTI Performance front lock. The table runs the same three cases at the top of "
               "the throttle slider in the bench above.",
    "diff_es": "Un diferencial abierto le da a cada rueda motriz la mitad del par del eje. Una rueda solo puede empujar el "
               "camino tanto como su agarre lo permite, más o menos el coeficiente de fricción por la carga sobre ella por "
               "el radio de la rueda. En una curva cerrada, la rueda delantera interior lleva menos carga, así que su "
               "límite es más bajo, y como las dos mitades deben ser iguales, todo el eje queda limitado al doble de ese "
               "límite menor. Si se frena la rueda interior, el diferencial puede sostener más par antes de que esa rueda "
               "patine, y la rueda exterior recibe más. Un paquete de embragues, en cambio, pasa par directamente de la "
               "rueda más rápida, la que patina, a la más lenta, hasta su par de bloqueo. Volkswagen da 1,600 Nm para el "
               "bloqueo delantero del Mk7 GTI Performance. La tabla corre los mismos tres casos en el tope del acelerador "
               "del banco de arriba.",
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
    "verify_h_en": "Run it yourself",
    "verify_h_es": "Córrelo tú",
    "verify_en": "The verifier lives at skills/classics/cc01/verify_cc01_mechanics.py, with a SKILL.md beside it. It uses only "
                 "the Python standard library, recomputes the torque split, the lap speeds and the quarter-car frequencies "
                 "with its own code, checks them against this page in both languages, and must fail when a defect is "
                 "planted, for example a clutch pack that sends torque the wrong way.",
    "verify_es": "El verificador está en skills/classics/cc01/verify_cc01_mechanics.py, con un SKILL.md al lado. Usa solo la "
                 "biblioteca estándar de Python, recalcula el reparto de par, las velocidades por vuelta y las frecuencias "
                 "del cuarto de auto con su propio código, las compara con esta página en los dos idiomas y debe fallar "
                 "cuando se le planta un defecto, por ejemplo un paquete de embragues que manda el par al revés.",
}

# Phrases that may not appear anywhere on the page (tests/test_cult_classics.py).
BANNED = [
    "first hot hatch", "best hot hatch", "legendary", "iconic", "greatest", "my car", "our car", "owner's car",
    "primer hot hatch", "legendario", "icónico", "mi auto", "nuestro auto",
]
