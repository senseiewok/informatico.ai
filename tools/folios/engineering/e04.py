#!/usr/bin/env python3
"""Folio E.04 (ENGINEERING): Counter-Current Enthalpy Recovery Exchangers: Effectiveness–NTU, Membrane Sorption, and Frost Limits."""
from __future__ import annotations

SLUG = 'e04'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.04',
 'slug': 'e04',
 'pillar': 'engineering',
 'category_code': 'E',
 'title': 'Counter-Current Enthalpy Recovery Exchangers: Effectiveness–NTU, Membrane Sorption, and '
          'Frost Limits',
 'subtitle': 'Coupled sensible heat and latent water-vapor transfer across selective polymer '
             'membranes, with model values of 88.2% sensible and 79.4% latent effectiveness at '
             'the default settings and a simple frost-limit estimate.',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.2',
 'status_badge': 'CIVIL & HVAC · REV 1.2',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'ε = NTU / (1 + NTU) · Bi_m = h_m δ_m / D_w · CSI 23 72 23',
 'colophon': {'identifier': 'E.04 · Coupled Heat & Mass Transfer · CSI 23 72 23',
              'kernels': 'ε = NTU / (1 + NTU) (Balanced Counter-Current)',
              'benchmarks': 'Model values: ε_s = 7.5/8.5 = 88.2% · ε_l = 3.85/4.85 = 79.4%',
              'bridge': 'Counter-Current Exchange ↔ How the Nose Warms and Humidifies Air (an '
                        'analogy)'},
 'sliders': [{'label': 'Sensible Transfer Units (NTU_s)',
              'min': 1.0,
              'max': 12.0,
              'step': 0.1,
              'value': 7.5,
              'unit': 'NTU = '},
             {'label': 'Membrane Moisture NTU (NTU_m)',
              'min': 0.5,
              'max': 8.0,
              'step': 0.05,
              'value': 3.85,
              'unit': 'NTU_m = '}],
 'steps': ['Stage 1 (Balanced Counter-Current Flow, C_r = 1.0): At NTU = 7.5, sensible '
           'effectiveness reaches ε_s = NTU / (1 + NTU) = 7.5 / 8.5 = 88.2%.',
           'Stage 2 (Membrane Vapor Permeation): Water vapor dissolves into and diffuses across '
           'a dense hydrophilic membrane. The page assumes a 25 μm membrane with Bi_m = 0.26, '
           'illustrative values; how well a real membrane holds back other gases depends on the '
           'product and was not modelled.',
           'Stage 3 (Frost Threshold): Moving moisture across the membrane lowers the dew point '
           'of the exhaust stream, so frost starts at colder outdoor temperatures. The page '
           'uses a simple linear estimate, T_frost = −3.0 − 9.5 (ε_l / 79.4%) °C, which gives '
           '−12.5 °C at the defaults; it is an illustration, not a psychrometric calculation.',
           'Stage 4 (Channel Geometry): Fully developed laminar flow between wide parallel '
           'plates has Nu ≈ 7.54 at constant wall temperature. The core pressure drop of 118 Pa '
           'at 2.1 m/s is a fixed illustrative value.'],
 'readouts': [{'label': 'Sensible Effectiveness (ε_s)', 'value': '88.2% (NTU = 7.5)'},
              {'label': 'Latent Moisture Recovery (ε_l)', 'value': '79.4% (NTU_m = 3.85)'},
              {'label': 'Frost-Free Outdoor Limit', 'value': '-12.5 °C (illustrative linear estimate; -3.0 °C sensible-only)'},
              {'label': 'Model Status', 'value': 'MODEL VALUES · BALANCED FLOW (C_r = 1)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 23 72 23 / 23 41 33',
                'title': 'Counter-Current Polymer-Membrane Enthalpy Core & HEPA H14 Clean-Air '
                         'Module',
                'body': 'Illustrative design sketch, not a certified product: a counter-current '
                        'enthalpy recovery core with a vapor-selective membrane and a separate '
                        'HEPA filter stage. A low exhaust air transfer ratio (EATR) would be a '
                        'design target to be measured; no value was measured for this page.',
                'meta': 'Design sketch · no Passive House or Eurovent certification and no EN '
                        '308 test stand behind this plate'},
 'sidenote_1': {'kicker': 'SIDENOTE E.04-A · AN ANALOGY: THE NOSE AS A HEAT AND MOISTURE '
                          'EXCHANGER',
                'body': 'The nose warms and humidifies inhaled air and recovers some heat and '
                        'water when we breathe out. That resembles an enthalpy exchanger, but it '
                        'works by alternating flow over the same moist lining rather than by two '
                        'streams on either side of a membrane. The comparison is an analogy '
                        'offered by this folio.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.04-B · SPECIFICATION PLATE · CSI 23 72 23 / 23 41 33',
                'body': 'Design sketch of a counter-current polymer-membrane enthalpy core with a '
                        'separate HEPA filter stage. Leakage and filtration figures would have to '
                        'be measured; none are claimed here.'},
 'skill': {'filename': 'counter-current-enthalpy-exchanger-SKILL.md',
           'name': 'counter-current-enthalpy-exchanger',
           'description': 'AI-agnostic thermal and psychrometric engineering skill for '
                          'counter-current heat and enthalpy recovery exchangers (epsilon-NTU), '
                          'membrane moisture sorption, and frost-limit psychrometrics.',
           'rules': ['For balanced counter-current flow (C_min / C_max = 1), compute effectiveness '
                     'epsilon = NTU / (1 + NTU).',
                     'Evaluate membrane latent NTU_m = A_tot * U_m / m_dot_da where 1/U_m = 2/h_m '
                     '+ delta_m / D_eff_membrane.',
                     'Check exhaust plate surface temperature T_plate_cold > '
                     'T_frost(omega_exhaust) to avoid ice blockage.']},
 'revisions': [{'edition': 'REV 1.2',
                'date': '2026-11-14',
                'summary': 'REV 1.2 (Redated 2026-11-14): Grounding revision. Unverified compliance '
                           'claims on the specification plate (Passive House, Eurovent, EN 308), '
                           'the "zero pathogen crossover" and ">99.6% aerosol" claims '
                           'were withdrawn as unsourced. A '
                           'chronology entry that dated the 1960 Journal of Applied Mechanics '
                           'record to 1986 was corrected, the invented 1915 and 1955 scenes were '
                           'replaced with plain dates, and the frost limit is now labelled as an '
                           'illustrative linear estimate.',
                'opus': 'Review: every DOI in the folio was checked in Crossref and the Scite '
                        'index on 2026-11-14, and the repository names with the GitHub API. No '
                        'simulation or test was run for this folio; the effectiveness values '
                        'follow from epsilon = NTU / (1 + NTU).'},
               {'edition': 'REV 1.1',
                'date': '2026-11-02',
                'summary': 'REV 1.1 (Redated 2026-11-02): Verified Kays & London counter-current '
                           'enthalpy recovery (epsilon = NTU / (1 + NTU), CSI 23 72 23) and '
                           'selective vapor permeation across polymer membranes with 4-Seat '
                           'Multi-Lineage Council review.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): checked that '
                        'epsilon_s = 88.2% (NTU = 7.5) and epsilon_l = 79.4% follow from the page '
                        'formula. The word "Verified" in this note and the note below is '
                        'withdrawn in REV 1.2, and the -12.5 °C frost limit is an illustrative '
                        'estimate, not a verified result.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-01',
                'summary': 'REV 1.0 (Published 2026-11-01): Initial publication of counter-current '
                           'membrane enthalpy recovery and frost-limit psychrometrics.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'balanced counter-current limit lim_{C_r -> 1} ε(NTU, C_r) = NTU / (1 + '
                        'NTU) = 88.24%.'}],
 'volume': 2,
 'volume_code': 'VOL. 02',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1115/1.3644004',
           'fetched_on': '2026-11-08',
           'citing_publications': 2942,
           'supporting': 19,
           'mentioning': 1078,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for the Compact Heat Exchangers record by Kays (DOI '
                      '10.1115/1.3644004), as recorded 2026-11-08: 2,942 citing publications (19 '
                      'supporting, 1,078 mentioning, 0 contrasting) and no retraction notice. '
                      'These counts describe that one record, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1115/1.3644004',
           'fetched_on': '2026-11-08',
           'citing_publications': 2942,
           'supporting': 19,
           'mentioning': 1078,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for the Compact Heat Exchangers record by Kays (DOI '
                      '10.1115/1.3644004), as recorded 2026-11-08: 2,942 citing publications (19 '
                      'supporting, 1,078 mentioning, 0 contrasting) and no retraction notice. '
                      'These counts describe that one record, not this folio.'},
 'act1_title': "Act I — Wilhelm Nusselt, Kays & London's NTU Method, and Counter-Current Enthalpy "
               'Recovery',
 'act1_dropcap': 'In 1915 the German engineer Wilhelm Nusselt published a paper that applied '
                 'similarity (dimensionless) analysis to convective heat transfer; the Nusselt '
                 'number is named after him, and the same kind of analysis was later carried '
                 'over to mass transfer. In 1955 William Kays and Alexander London of Stanford '
                 'University published the first edition of Compact Heat Exchangers, a book of '
                 'design data that made the effectiveness–NTU method a standard tool. That method '
                 'shows a simple fact: with two streams of equal heat capacity, a parallel-flow '
                 'exchanger can never recover more than half of the available heat, while a '
                 'counter-flow exchanger approaches full recovery as it is made larger.',
 'act1_plain_bridge': 'Imagine two long trains traveling on adjacent tracks in opposite directions '
                      'during a freezing winter day. One train is warm and bustling with '
                      'passengers, while the other train is cold and empty. If passengers on the '
                      'warm train hand thermoses of hot coffee across the windows to the cold '
                      'train as they pass, a wonderful exchange happens. Because the two trains '
                      'move past each other from head to tail, the coldest incoming cars meet the '
                      'coolest departing cars first, while the warmest cars meet at the very end. '
                      'By the time they separate, the cold train has gathered almost all the '
                      'warmth and humidity from the departing train. Modern buildings use this '
                      'counter-flow trick inside their ventilation systems. Stale, warm indoor air '
                      'leaving the building warms and humidifies fresh, chilly outdoor air '
                      'entering the rooms through thin membrane sheets. The two air streams never '
                      'touch, yet heat and fresh moisture glide right through.',
 'act1_body': 'Noses do something similar: the nasal lining warms and humidifies inhaled air '
              'and takes back some heat and water on the way out, though by alternating flow '
              'rather than two separate streams. Building energy recovery ventilators use '
              'vapor-permeable polymer membranes to exchange heat and moisture between outgoing '
              'and incoming air. Building upon William Kays and Alexander '
              "London's Effectiveness–NTU formalism (Compact Heat Exchangers, DOI "
              "10.1115/1.3644004) and Wilhelm Nusselt's fully developed laminar duct heat transfer "
              'asymptotes, contemporary enthalpy recovery cores interleave microscopic hygroscopic '
              'membranes that simultaneously transfer sensible heat and latent water-vapor '
              'enthalpy. In these dense membrane blocks, exhaust air flows opposite to incoming '
              'outdoor air across sub-micron channels. Sensible energy conducts across the polymer '
              'skin while moisture dissolves into hydrophilic domains and diffuses down the '
              'vapor pressure gradient. Dense membranes are meant to keep the two air streams '
              'apart; how much air, odour or contaminant still crosses is a property of each '
              'product and has to be measured. Recovering heat and moisture this way can reduce '
              'heating and cooling loads.',
 'act1_stakes': 'Designing an energy recovery ventilator with sensible-only equations misses '
                'what happens to water. In freezing weather, warm exhaust air can cool below its '
                'dew point inside the core, and the condensate can freeze and block channels, '
                'which is why exchangers need defrost strategies. Moisture-permeable membrane '
                'cores move some of that water to the incoming air before it condenses, which '
                'the literature reports can reduce condensation and frost compared with plain '
                'plate exchangers (for example Van Vu & Dvořák 2017, DOI '
                '10.1051/epjconf/201714302080). In humid weather, the coupled moisture transfer '
                'also matters for indoor humidity. Engineers handle these cases by combining '
                'effectiveness–NTU models with membrane sorption data; this page shows a '
                'simplified version.',
 'pullquote': '"With two equal streams, parallel flow can recover at most half the heat; counter '
              'flow approaches all of it as the exchanger grows."',
 'chronology': [('1915',
                 'Wilhelm Nusselt applies similarity analysis to convective heat transfer.'),
                ('1955',
                 'William Kays & Alexander London publish the first edition of Compact Heat '
                 'Exchangers, built on the effectiveness–NTU design method.'),
                ('1960',
                 'A Journal of Applied Mechanics record of Compact Heat Exchangers (DOI '
                 '10.1115/1.3644004) documents the book in the engineering literature.'),
                ('1984',
                 'Kays & London publish the third edition of Compact Heat Exchangers.')],
 'act2_title': 'Act II — How It Actually Works: Sensible Conduction + Solution-Diffusion Vapor '
               'Transport',
 'act2_analogy': 'Think of two commuter trains passing each other in opposite directions on a '
                 'snowy afternoon. If passengers on the heated departing train reach across the '
                 'windows to hand warm mugs of tea to passengers on the incoming chilly train, '
                 'heat transfers along the entire length of the tracks. The arriving passengers '
                 'step off nearly as warm as the ones leaving, all without a single passenger ever '
                 'switching train cars or mixing their personal belongings.',
 'act2_plain_primer': 'To see how this energy recovery core functions in practice, our model '
                      'features two primary adjustments that govern the transfer process. The '
                      'first adjustment is the Sensible Transfer Units dial, which represents the '
                      'effective surface area and thermal conductivity available for swapping dry '
                      'heat. Turning this dial up is like lengthening the train platforms and '
                      'adding more passenger windows, allowing thermal energy to glide '
                      'effortlessly across the thin membrane dividers until the two streams nearly '
                      'match temperatures. The second adjustment is the Membrane Moisture NTU '
                      'dial, which represents the chemical capacity of the specialized membrane to '
                      'absorb and transport water vapor. Raising this moisture control allows '
                      'humidity to dissolve into microscopic pores and diffuse across the barrier '
                      'into the dry supply stream. Balancing both dials ensures that fresh '
                      'incoming air receives both the warmth and the gentle humidity needed for '
                      'healthy indoor spaces, without letting liquid water freeze into damaging '
                      'ice.',
 'distill_diagram': {'analogy_title': 'Two Passing Trains & Thermos Exchange',
                     'analogy_sub': 'Opposing streams transfer warmth and moisture without mixing.',
                     'force_a_title': 'Sensible Heat NTU (NTU_s)',
                     'force_a_sub': 'Drives thermal conduction across polymer membrane channels.',
                     'force_b_title': 'Moisture Latent NTU (NTU_m)',
                     'force_b_sub': 'Governs water-vapor sorption and solution-diffusion flux.',
                     'threshold_title': 'Frost Limit & Freezing Boundary',
                     'threshold_pass': 'High Recovery: Continuous enthalpy transfer without icing.',
                     'threshold_fail': 'Frost Blockage: Condensate freezes, sealing core '
                                       'passages.'},
 'act2_intuition': 'In a balanced counter-current membrane enthalpy exchanger, warm humid exhaust '
                   'air flows opposite to cold dry outdoor air across dense, non-porous '
                   'hydrophilic block-copolymer membranes. Sensible heat crosses the thin plastic '
                   'boundary by pure thermal conduction, governed by the sensible transfer number '
                   'NTU_s = U A / C_min. Simultaneously, water vapor molecules dissolve into '
                   'sulfonated nano-domains and diffuse down chemical potential gradients toward '
                   'the dry supply stream, governed by the latent transfer number NTU_m. Because '
                   'counter-current geometry maintains a nearly constant thermodynamic driving '
                   'gradient along the entire channel length L, its effectiveness epsilon = NTU / '
                   '(1 + NTU) under balanced heat capacity rates (C_r = 1) asymptotically '
                   'approaches unity as surface area expands. In contrast, parallel-flow '
                   'exchangers remain thermodynamically constrained below fifty percent efficiency '
                   'regardless of membrane size. Channel shape and membrane sorptivity set how '
                   'many transfer units a real core reaches; in this model, the default NTU = 7.5 '
                   'gives 88.2% sensible effectiveness. Real cores report lower or higher figures '
                   'depending on airflow and design, and their frost behaviour must be tested.',
 'act2_deepening': 'The coupled transfer of sensible heat and water vapor involves intricate '
                   'conjugate boundary layer mechanics on either side of the selective membrane. '
                   'Within the narrow flow channels, developing velocity and thermal boundary '
                   'layers determine local convective resistance according to Graetz–Nusselt '
                   'solutions. As moisture permeates the membrane via solution-diffusion, it '
                   'releases or absorbs latent heat of vaporization, dynamically shifting the '
                   'local membrane temperature. This thermal-latent coupling creates a localized '
                   'feedback loop: higher temperature increases the saturation vapor pressure at '
                   'the membrane interface, which modifies the local mass transfer driving force. '
                   'Furthermore, if outdoor temperatures plunge below freezing, the exhaust '
                   'channel wall can drop below the dew point and the freezing point '
                   'simultaneously. If the local moisture removal rate governed by NTU_m is too '
                   'slow to desorb water vapor before this freezing line, liquid condensate forms '
                   'and crystallizes into frost. Advanced multi-scale modeling resolves these '
                   'conjugate gradients, allowing engineers to tailor membrane thickness and '
                   'channel spacing to prevent frost inception.',
 'walkthrough': ['Experiment 1 (Counter-Current vs. Parallel Flow): Check that at NTU_s = 4.2 and '
                 'C_r = 1.0, counter-current effectiveness is 4.2 / 5.2 = 80.8%, whereas parallel '
                 'flow plateaus at (1 - e^-8.4)/2 = 50.0%.',
                 'Experiment 2 (Latent Moisture Balance): Observe how NTU_m = 2.83 yields '
                 'epsilon_l = 2.83 / 3.83 = 73.9%, and how the illustrative frost estimate moves '
                 'with it.',
                 'Experiment 3 (4-Stage Stepper): Follow the stepper from balanced counter-flow '
                 'to membrane permeation, the frost estimate and the channel geometry.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification '
               'Bridge',
 'act4_human_ai': 'A proposal, not a description of installed systems: a controller could '
                  'combine weather forecasts and occupancy sensors with effectiveness–NTU models '
                  'and membrane sorption isotherms (for example the '
                  'Guggenheim–Anderson–de Boer form) to manage humidity and frost risk. Readers '
                  'who want to explore this could use open tools such as the Dedalus spectral '
                  'solver (DedalusProject/dedalus, https://github.com/DedalusProject/dedalus, DOI '
                  '10.1103/PhysRevResearch.2.023068) or symbolic regression with PySR '
                  '(MilesCranmer/PySR, DOI 10.48550/arXiv.2305.01582). Neither was run for this '
                  'folio. Ventilation rates are set by standards such as ASHRAE 62.1, which this '
                  'page does not apply. References were checked in the Scite index (DOI '
                  '10.1162/qss_a_00146).',
 'act4_deepening': 'A possible next step for building energy recovery, offered as a research '
                   'direction: building management systems could link temperature and humidity '
                   'sensors with physics-informed surrogate models running locally. Such '
                   'algorithms would predict indoor moisture accumulation, outdoor weather '
                   'shifts, and internal frost risk in real time, dynamically modulating bypass '
                   'damper positions and variable-speed fan velocities to maximize heat recovery '
                   'while avoiding defrost penalty cycles. Human mechanical engineers define '
                   'health guidelines, ventilation rates, and indoor air quality standards while '
                   'reviewing automated fault detection reports. Open research frontiers '
                   'investigate novel metal-organic framework coatings and biomimetic membrane '
                   'channels that transport water vapor while holding back other gases and '
                   'volatile organic compounds as well as possible. Better ventilation and lower '
                   'energy use are the goals; this folio makes no claim about health outcomes.',
 'sources': ['Kays, W. M., & London, A. L. (1984). Compact Heat Exchangers (3rd ed.). McGraw-Hill.',
             'Zhang, L. Z. (2012). Conjugate Heat and Mass Transfer in Heat Mass Exchanger Ducts. '
             'Academic Press.',
             'Kays, W. M. (1960). Compact Heat Exchangers [record of the Kays & London book]. '
             'Journal of Applied Mechanics, 27(2), 377. DOI: 10.1115/1.3644004.',
             'Van Vu, N., & Dvořák, V. (2017). Evaluating the moisture transfer of membranes for '
             'total heat exchanger. EPJ Web of Conferences, 143, 02080. DOI: '
             '10.1051/epjconf/201714302080.',
             'ASHRAE (2021). ASHRAE Handbook — Fundamentals: Psychrometrics and Air-to-Air Energy '
             'Recovery.',
             'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). '
             'Dedalus: A flexible framework for numerical simulations with spectral methods '
             '(DedalusProject/dedalus, https://github.com/DedalusProject/dedalus). Physical Review '
             'Research, 2(2), 023068. DOI: 10.1103/PhysRevResearch.2.023068.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Counter-current '
        'epsilon-NTU effectiveness curve vs parallel flow plateau">\n'
        '            <line x1="60" y1="185" x2="620" y2="185" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <line x1="60" y1="25" x2="60" y2="185" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <path d="M 60 185 Q 210 65 590 42" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="3"/>\n'
        '            <path d="M 60 185 Q 210 75 590 68" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="2.5"/>\n'
        '            <path d="M 60 185 Q 180 108 590 105" fill="none" stroke="var(--tp-minium)" '
        'stroke-width="2" stroke-dasharray="5,4"/>\n'
        '            <circle cx="460" cy="52" r="6" fill="var(--tp-verdigris)"/>\n'
        '            <circle cx="460" cy="74" r="6" fill="var(--tp-prussian)"/>\n'
        '            <text x="315" y="34" font-size="11" fill="var(--tp-verdigris)">Sensible '
        'Counter-Current ε_s = 80.8% (NTU_s = 4.2)</text>\n'
        '            <text x="315" y="92" font-size="11" fill="var(--tp-prussian)">Latent Membrane '
        'Recovery ε_l = 73.9% (NTU_l = 2.83)</text>\n'
        '            <text x="370" y="122" font-size="11" fill="var(--tp-minium)">Parallel-Flow '
        'Limit (ε_max = 50.0%)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a laser-welded stainless-steel counter-current '
        'enthalpy recovery heat exchanger core would look like (artistic impression, not a '
        'measured structure)',
 'caption': 'Conceptual Vision Plate E.04-V (Imagining What It Would Look Like) · Artistic '
            'mechanical cutaway imagining a laser-welded 316L stainless-steel counter-current '
            'enthalpy recovery core with alternating micro-corrugated plates and vapor-selective '
            'membranes.'}

DISPATCH = {'kicker': 'FRONTIER THERMODYNAMICS DISPATCH · SELECTIVE IONOMER MEMBRANES',
 'headline': 'Membrane Enthalpy Cores Move Water Vapor as Well as Heat',
 'body': "Extending Kays & London's ε-NTU compact heat exchanger method (record: DOI "
         '10.1115/1.3644004), membrane enthalpy cores move water vapor by solution-diffusion as '
         'well as heat, which can reduce condensation and frost in cold weather (Van Vu & '
         'Dvořák 2017, DOI 10.1051/epjconf/201714302080). At the default settings this page '
         'models 79.4% latent effectiveness; its frost limit of −12.5 °C is an illustrative '
         'estimate.'}

META_3D = ('Cross-Corrugated Chevron Enthalpy Exchanger',
 'X: Supply Air Channel · Z: Exhaust Counter-Flow · Y: Psychrometric Enthalpy Transfer Surface')

ES_TRANSLATION = {'title_es': 'Intercambiadores de Recuperación de Entalpía a Contracorriente: Efectividad–NTU, '
             'Sorción en Membrana y Límites de Escarcha',
 'subtitle_es': 'Transferencia acoplada de calor sensible y vapor de agua latente a través de '
                'membranas poliméricas selectivas, con valores de modelo de 88.2% de efectividad '
                'sensible y 79.4% latente en la configuración inicial, y una estimación sencilla '
                'del límite de escarcha.',
 'why_es': 'Como dos trenes que se cruzan en sentido opuesto intercambiando termos calientes '
           'ventana por ventana, el flujo a contracorriente recupera casi toda la energía térmica '
           'y la humedad sin mezclar el aire viciado con el aire limpio.',
 'plain_es': 'En 1915, el ingeniero alemán Wilhelm Nusselt publicó un análisis de semejanza '
             '(adimensional) de la transferencia de calor por convección. En 1955, William Kays y '
             'Alexander London, de la Universidad de Stanford, publicaron la primera edición de '
             'Compact Heat Exchangers, que difundió el método de efectividad–NTU. Ese método '
             'muestra que, con dos corrientes iguales, el flujo paralelo nunca recupera más de la '
             'mitad del calor, mientras que el flujo a contracorriente se acerca a recuperarlo '
             'todo. Para entenderlo de manera sencilla, imaginen dos trenes que avanzan '
             'en direcciones contrarias durante una tarde helada: si los pasajeros comparten '
             'termos de café caliente a través de las ventanillas, el tren frío absorbe casi todo '
             'el calor del tren cálido antes de separarse. En las edificaciones modernas, los '
             'sistemas de ventilación emplean este principio mediante paneles con membranas '
             'especiales. El aire viciado que sale transfiere su calor y humedad al aire fresco '
             'que entra del exterior, sin que las corrientes se mezclen en ningún momento.',
 'deep_es': 'La recuperación total de entalpía se fundamenta en el equilibrio acoplado entre la '
            'conducción de calor sensible y la difusión de humedad latente a través de membranas '
            'poliméricas selectivas. La configuración a contracorriente mantiene una diferencia de '
            'temperatura y presión de vapor casi uniforme a lo largo de los canales, permitiendo '
            'eficiencias térmicas superiores al ochenta y cinco por ciento. No obstante, en climas '
            'extremadamente fríos surge un umbral crítico: si el aire húmedo de extracción se '
            'enfría por debajo de su punto de rocío y de congelación, el agua condensada se '
            'convierte en escarcha sólida, bloqueando el paso del aire. En la ingeniería civil '
            'contemporánea, los especialistas usan modelos numéricos para calcular el número de '
            'unidades de transferencia térmica y de humedad, y diseñar estrategias de '
            'descongelamiento. En esta página, el límite de escarcha de −12.5 °C es una '
            'estimación ilustrativa, no un resultado de prueba.'}
