#!/usr/bin/env python3
"""Folio E.08 (ENGINEERING): Earth-Pressure-Balance Tunnel Boring Machines (EPB-TBM), Peck–Mair Gaussian Settlement Troughs & GNN Subsurface Digital Twins."""
from __future__ import annotations

SLUG = 'e08'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.08',
 'slug': 'e08',
 'pillar': 'engineering',
 'category_code': 'E',
 'title': 'Earth-Pressure-Balance Tunnel Boring Machines (EPB-TBM), Peck–Mair Gaussian Settlement '
          'Troughs & GNN Subsurface Digital Twins',
 'subtitle': "How Ralph Peck and Robert Mair's conservation-of-volume Gaussian settlement trough "
             'S(y) = S_max exp(−y² / 2i²) governs urban underground tunneling, coupled with Graph '
             'Neural Network subsurface digital twins.',
 'date_published': '2026-11-02',
 'date_redated': '2026-11-02',
 'current_edition': 'REV 1.0',
 'status_badge': 'CIVIL & GEOTECH TUNNELING · REV 1.0',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'S(y) = S_max exp(−y² / 2i²) · V_s = V_L (π D² / 4) · i = K (z_0 − z) · CSI 31 '
                  '71 19',
 'colophon': {'identifier': 'E.08 · EPB-TBM Tunneling & Peck–Mair Settlement · CSI 31 71 19',
              'kernels': 'Peck–Mair Gaussian Trough · Anagnostou–Kovári Face Equilibrium · GNN '
                         'Twin',
              'benchmarks': 'D = 9.8 m · z_0 = 24.0 m · V_L = 0.75% ⇒ S_max = 18.8 mm',
              'bridge': 'EPB Foam Yield-Stress Conditioning ↔ Two-Phase Viscoelastic Gel '
                        'Mobilization'},
 'sliders': [{'label': 'TBM Face Support Pressure (P_face)',
              'min': 80.0,
              'max': 360.0,
              'step': 5.0,
              'value': 210.0,
              'unit': ' kPa'},
             {'label': 'Geotechnical Volume Loss Ratio (V_L)',
              'min': 0.2,
              'max': 2.5,
              'step': 0.05,
              'value': 0.75,
              'unit': '%'}],
 'steps': ['Stage 1 (Anagnostou–Kovári Chamber Pressure Balance): At depth z_0 = 24.0 m, EPB '
           'chamber pressure P_face = 210 kPa balances lateral earth + pore water pressure without '
           'passive blowout.',
           'Stage 2 (Foam-Conditioned Muck Rheology): Surfactant-polymer foam injection transforms '
           'excavated clay into a cohesive, low-permeability plastic paste (slump 120 mm) across '
           'the screw conveyor.',
           'Stage 3 (Peck–Mair Subsurface Gaussian Propagation): Volume loss V_L = 0.75% across D '
           '= 9.8 m creates a trough of inflection width i = K z_0 = 12.0 m and centerline S_max = '
           '18.8 mm.',
           'Stage 4 (Graph Neural Network Subsurface Digital Twin): Real-time cutterhead torque '
           'and tail-void grout pressures update the GNN mesh to hold angular distortion β_max < '
           '1/500 beneath historic masonry.'],
 'readouts': [{'label': 'Trough Inflection Width (i = K z_0)',
               'value': '12.0 m (K = 0.50, z_0 = 24 m)'},
              {'label': 'Centerline Max Settlement (S_max)', 'value': '18.8 mm (at V_L = 0.75%)'},
              {'label': 'Max Angular Distortion (β_max)', 'value': '1 / 1,050 (< 1/500 Limit)'},
              {'label': 'Geotechnical TBM Verdict', 'value': 'FACE STABLE · RANKINE PASS'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 31 71 19 / ACI 533',
                'title': '9.8 m Earth-Pressure-Balance TBM & Precast Fiber-Reinforced Segmental '
                         'Lining',
                'body': 'Pressurized EPB shield excavation with automated two-component tail-void '
                        'backfill grouting, EPDM elastomeric gasketed C60/75 precast concrete '
                        'tunnel rings, and real-time InSAR + GNN settlement monitoring.',
                'meta': 'Mair-Taylor-Bracegirdle (1993) verified · Max building distortion β ≤ '
                        '1/500'},
 'sidenote_1': {'kicker': 'SIDENOTE E.08-A · CONSERVATION OF SOIL VOLUME IN PECK–MAIR TROUGHS',
                'body': 'Integrating S(y) = S_max exp(−y² / 2i²) from −∞ to +∞ yields V_s = √(2π) '
                        '· i · S_max. Equating V_s to V_L · (π D² / 4) proves that S_max is '
                        'inversely proportional to depth z_0 while maximum slope occurs at y = '
                        '±i.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.08-B · SPECIFICATION PLATE · CSI 31 71 19 / GNN SUBSURFACE '
                          'TWIN',
                'body': 'Graph Neural Networks represent borehole stratigraphy and tunnel ring '
                        'nodes as a message-passing graph constrained by Mohr–Coulomb yield '
                        'surfaces, predicting settlement troughs 50 m ahead of the TBM face.'},
 'skill': {'filename': 'epb-tbm-peck-settlement-SKILL.md',
           'name': 'epb-tbm-peck-settlement',
           'description': 'AI-agnostic geotechnical and tunneling civil engineering skill for '
                          'EPB-TBM face pressure equilibrium, Peck-Mair Gaussian settlement '
                          'troughs, and GNN subsurface digital twins.',
           'rules': ['Compute trough inflection distance i = K * (z_0 - z) (with K = 0.50 for '
                     'clays, 0.25-0.35 for sands) and tunnel cross-sectional area A_t = pi * D^2 / '
                     '4.',
                     'Calculate centerline maximum settlement S_max = (V_L * A_t) / (sqrt(2 * pi) '
                     '* i) and maximum transverse slope beta_max = 0.6065 * S_max / i at y = +/- '
                     'i.',
                     'Verify EPB face pressure P_face stays between active collapse pressure '
                     'sigma_h,active + u_0 and passive blowout pressure sigma_v0.']},
 'revisions': [{'edition': 'REV 1.0',
                'date': '2026-11-02',
                'summary': 'REV 1.0 (Published 2026-11-02): Inaugural Volume IV geotechnical & '
                           'underground tunneling monograph uniting Peck-Mair Gaussian settlement '
                           'troughs (DOI 10.1680/geot.1993.43.2.315) with EPB-TBM chamber '
                           'mechanics and GNN subsurface digital twins.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'exact Gaussian integral V_s = sqrt(2*pi)*i*S_max = 0.565 m^3/m and S_max '
                        '= 18.8 mm at V_L = 0.75%, D = 9.8 m, i = 12.0 m.'}],
 'volume': 4,
 'volume_code': 'VOL. 04',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1680/geot.1993.43.2.315',
           'fetched_on': '2026-11-08',
           'citing_publications': 575,
           'supporting': 6,
           'mentioning': 183,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 575 citing '
                      'publications (6 supporting, 183 mentioning, 0 contrasting) on subsurface '
                      'and surface Peck-Mair Gaussian settlement troughs above bored tunnels in '
                      'soft ground.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1680/geot.1993.43.2.315',
           'fetched_on': '2026-11-08',
           'citing_publications': 575,
           'supporting': 6,
           'mentioning': 183,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 575 citing '
                      'publications (6 supporting, 183 mentioning, 0 contrasting) on subsurface '
                      'and surface Peck-Mair Gaussian settlement troughs above bored tunnels in '
                      'soft ground.'},
 'act1_title': "Act I — From Marc Brunel's Thames Shield to Earth-Pressure-Balance TBMs & "
               'Subsurface AI Digital Twins',
 'act1_dropcap': 'In the damp chill of Chatham Dockyard in 1818, the French-born engineer Marc '
                 'Isambard Brunel peered through a magnifying glass at a soft-bodied marine '
                 'mollusk called the shipworm. He watched in fascination as the creature used tiny '
                 'shell plates on its head to grind through submerged oak timbers, immediately '
                 'lining its newly excavated burrow with a smooth, protective calcium coating to '
                 "prevent collapse. Inspired by the creature's elegant subterranean rhythm, Brunel "
                 "patented the world's first tunneling shield and embarked on excavating beneath "
                 'the tidal currents of the River Thames. For eighteen years, miners faced '
                 'quicksand blowouts, noxious gases, and sudden riverbed fractures before '
                 'completing the historic bore. Brunel proved that soft ground could be conquered, '
                 'but he left behind an enduring geotechnical mystery: how does the removal of '
                 'soil deep underground inevitably reshape the surface of the city above?',
 'act1_plain_bridge': 'In plain words, digging a giant subway tunnel beneath an active city is '
                      'like scooping sand from the bottom of an hourglass. When a massive boring '
                      'machine cuts through waterlogged clay twenty meters below ground, it '
                      'temporarily relieves the pressure supporting the earth. Even if the machine '
                      'slips by just a few millimeters, the surrounding soil creeps into the tiny '
                      'void left behind. Because earth cannot simply vanish, this underground '
                      'movement travels upward through the soil layers like a slow-motion wave, '
                      'eventually forming a gentle, bowl-shaped dip on the street above. If that '
                      'dip sinks unevenly beneath a historic cathedral or brick building, walls '
                      'crack and foundations tilt. To prevent damage, modern tunneling machines '
                      'pressurize conditioned soil paste directly against the cutting face while '
                      'pumping cement grout around the newly placed concrete rings. Geotechnical '
                      'engineers use graph-based artificial intelligence to monitor ground motion '
                      'continuously, keeping street settlement so small that city life above '
                      'continues undisturbed.',
 'act1_body': 'In 1969, Ralph B. Peck synthesized field observations from major subway excavations '
              'worldwide at the Mexico City soil mechanics conference, demonstrating that surface '
              'settlement above a circular tunnel follows an inverted Gaussian bell curve. Two '
              'decades later, Robert J. Mair, R. N. Taylor, and A. Bracegirdle (Géotechnique, DOI '
              '10.1680/geot.1993.43.2.315) proved that this Gaussian profile extends through '
              'subsurface horizons at every depth, establishing that the trough inflection width '
              'scales directly with remaining soil overburden. Today, ten-meter-diameter '
              'Earth-Pressure-Balance Tunnel Boring Machines (EPB-TBMs, CSI 31 71 19, ACI 533) '
              'excavate beneath dense metropolitan centers by pressurizing foam-conditioned muck '
              'inside the cutterhead plenum. This pressurized paste balances lateral earth and '
              'pore-water pressure, preventing face collapse. By coupling real-time telemetry from '
              'cutterhead thrust cylinders and tail-void grout pumps with Graph Neural Network '
              '(GNN) subsurface digital twins, geotechnical engineers forecast settlement troughs '
              'fifty meters ahead of the machine, ensuring angular distortion remains well within '
              'safe historical building tolerances.',
 'act1_stakes': 'The practical stakes of urban tunneling are measured in the preservation of '
                'ancient architecture and modern utility networks. When an earth pressure balance '
                'shield loses face pressure, even for a few minutes, saturated silt and gravel can '
                'wash into the cutterhead, triggering an active ground collapse that propagates '
                'upward as a sudden sinkhole. Conversely, applying excessive support pressure '
                'heaves the street upward, shearing underground gas mains and cracking water '
                'distribution pipes. The most subtle danger is differential settlement: when one '
                'corner of a masonry structure settles more than another, shear stresses '
                'accumulate in unreinforced mortar joints. Once angular distortion exceeds one '
                'unit in five hundred, plaster cracks, door frames jam, and structural brickwork '
                'begins to detach. Avoiding these failures requires continuous equilibrium between '
                'excavation rate and support pressure, turning geotechnical tunneling into a '
                'delicate balance of material rheology, ground mechanics, and predictive '
                'subsurface modeling.',
 'pullquote': '"Every fraction of a percent of volume loss V_L at the TBM cutterhead propagates '
              'upward through the soil continuum as a conservation-of-volume Gaussian settlement '
              'trough at the city street above."',
 'chronology': [('1825',
                 'Marc & Isambard Kingdom Brunel drive the Thames Tunnel using the first '
                 'compartmentalized cast-iron tunneling shield.'),
                ('1969',
                 'Ralph B. Peck establishes the empirical Gaussian surface settlement trough S(y) '
                 '= S_max exp(-y^2 / 2i^2) and volume loss V_L.'),
                ('1993',
                 'Mair, Taylor & Bracegirdle prove subsurface Gaussian scaling and centrifugal '
                 'face-collapse bounds in Géotechnique (DOI 10.1680/geot.1993.43.2.315).'),
                ('2026',
                 'Physics-constrained GNN subsurface digital twins integrate EPB-TBM cutterhead '
                 'telemetry for real-time urban settlement control.')],
 'act2_title': 'Act II — How It Actually Works: EPB Chamber Pressure Balance + Peck–Mair Gaussian '
               'Troughs',
 'act2_analogy': 'Everyday analogy: Imagine slicing a spoon through a bowl of moist chocolate '
                 'pudding. If you pull the pudding out too fast, the surface above dips into a '
                 'smooth, curved hollow; if you press forward too aggressively, the surface bulges '
                 'upward. Tunneling through saturated urban ground works the exact same way. The '
                 "machine's pressurized front must support the soil with the exact firmness needed "
                 'to keep the street above completely flat.',
 'act2_plain_primer': 'To visualize subsurface settlement dynamics, our interactive laboratory '
                      'provides two essential knobs. The first control is TBM Face Support '
                      'Pressure, which sets the pressure maintained by the pressurized soil paste '
                      'inside the cutting chamber. Lowering this pressure below ambient soil and '
                      'water levels causes the tunnel face to yield inward, increasing ground loss '
                      'and deepening the settlement bowl at the surface. Raising it too high '
                      'pushes the ground upward, creating an unwanted heave. The second control is '
                      'the Geotechnical Volume Loss Ratio, representing the fraction of the '
                      'excavated tunnel volume that is lost as surrounding soil creeps into tiny '
                      'voids around the shield. As this percentage rises, more soil volume is '
                      'drawn down, causing the surface settlement curve to sink deeper across the '
                      'entire neighborhood. Tuning these two parameters reveals how balancing '
                      'chamber pressure keeps surface settlement within millimeters, protecting '
                      'street pavements and adjacent foundations.',
 'distill_diagram': {'analogy_title': 'Spoon Slicing Moist Pudding',
                     'analogy_sub': 'Underground voids propagate upward as smooth surface dips',
                     'force_a_title': 'Chamber Face Pressure (P_face)',
                     'force_a_sub': 'Balances earth and pore-water pressure to prevent ground '
                                    'collapse',
                     'force_b_title': 'Volume Loss Ratio (V_L)',
                     'force_b_sub': 'Quantifies lost ground propagating into surface settlement',
                     'threshold_title': 'Active Collapse vs. Passive Heave Window',
                     'threshold_pass': 'Stable: Ground loss stays under 1% and distortion under '
                                       '1/500',
                     'threshold_fail': 'Failure: Face collapse creates surface sinkhole or street '
                                       'heave'},
 'act2_intuition': 'When an Earth-Pressure-Balance TBM of diameter D advances at depth z_0 through '
                   'saturated ground, the cutterhead chamber pressure P_face must maintain '
                   'equilibrium with in-situ horizontal effective stress and pore water pressure '
                   "sigma_h0 = K_0 sigma'_v + u_0. If chamber pressure drops below active Rankine "
                   'limit equilibrium, soil slumps into the cutterhead, producing a volume loss '
                   'fraction V_L. By soil mass conservation, the total volume of the surface '
                   'settlement trough V_s per unit tunnel advance equals V_L (pi D^2 / 4). Ralph '
                   'Peck and Robert Mair demonstrated that this volume distributes into an '
                   'inverted Gaussian curve S(y) = S_max exp(-y^2 / [2 i^2]), where the inflection '
                   'distance i = K (z_0 - z) governs the trough width. Centerline maximum '
                   'settlement is S_max = V_s / (sqrt(2 pi) i). The maximum ground slope occurs '
                   'precisely at y = +-i, producing an angular distortion beta_max = 0.6065 S_max '
                   '/ i that must remain below 1/500 to protect surface structures, historical '
                   'buildings, and sensitive subsurface utility conduits from shear distortion.',
 'act2_deepening': 'At the microscopic scale, the behavior of excavated soil inside the '
                   'pressurized plenum depends on foam conditioning rheology. Dry or sticky clay '
                   'clumps into dense masses that jam the cutterhead and adhere to the screw '
                   'conveyor, causing erratic pressure spikes and uncontrolled volume loss. '
                   'Injecting surfactant-polymer foam transforms stiff cohesive soil into a '
                   'homogeneous, low-permeability plastic paste with an engineered slump of 120 to '
                   '180 millimeters. This conditioned paste acts as a continuous hydraulic '
                   'cushion, transmitting thrust evenly across the tunnel face. Meanwhile, behind '
                   'the shield, rapid injection of two-component cementitious grout into the '
                   'annular tail void prevents the surrounding soil from relaxing into the gap '
                   'left by the steel shell. Graph Neural Networks model this three-dimensional '
                   'interaction by representing geological borehole strata, cutterhead sensors, '
                   'and individual segmental lining rings as connected nodes. By training on '
                   'historical geotechnical records and real-time machine telemetry, the network '
                   'predicts settlement bowl evolution as ground conditions change.',
 'walkthrough': ['Experiment 1 (Chamber Pressure vs. Face Stability): Drag TBM Face Support '
                 'Pressure P_face from 240 kPa down toward 110 kPa. Watch face stability ratio '
                 'N_face climb and induce higher Volume Loss V_L.',
                 'Experiment 2 (Peck–Mair Settlement Trough): Adjust Volume Loss Ratio V_L (%) '
                 'from 0.40% to 1.80% and watch the inverted Gaussian settlement profile S(y) '
                 'deepen across the +-36 m urban building footprint.',
                 'Experiment 3 (Precast Segmental Ring & GNN Forecast): Step through Stages 1 to 4 '
                 'to inspect foam-conditioned muck rheology, Anagnostou–Kovári wedge equilibrium, '
                 'tail-void grouting, and GNN digital-twin settlement prediction.'],
 'act4_title': 'Act IV — Geotechnical Tunneling Telemetry, Lab Sustainability & Upstream Discovery '
               'Threads',
 'act4_human_ai': 'In metropolitan subway and deep utility tunneling, GNN subsurface digital twins '
                  'ingest real-time TBM cutterhead torque, screw-conveyor mass flow, and InSAR '
                  'satellite interferometry to adjust bentonite/polymer foam injection and '
                  'tail-void grout pressure ring by ring. Coupling 3D elastoplastic finite-element '
                  'excavation staging in FEniCS/dolfinx (https://github.com/FEniCS/dolfinx, DOI '
                  '10.1145/3524456) with sparse settlement-trough identification in '
                  'dynamicslab/pysindy (DOI 10.1073/pnas.1517384113) lets tunnel engineers '
                  'continuously tune EPB chamber pressure and tail-void grouting under '
                  'Scite-verified geotechnical benchmarks (DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'In the modern era of subterranean infrastructure, human tunneling engineers '
                   'work alongside autonomous artificial intelligence to navigate complex urban '
                   'geology. Next-generation boring machines combine downhole seismic look-ahead '
                   'sensors with real-time digital twins that analyze cutterhead torque, disc '
                   'cutter wear rates, and muck weight hundreds of times per second. When the '
                   'machine approaches an unmapped geological fault or soft clay pocket, the AI '
                   'model recommends optimal foam injection ratios and face pressure adjustments '
                   'before the cutting wheels make contact. Important frontier questions remain '
                   'active areas of study: accurately predicting three-dimensional ground response '
                   'around skewed tunnel intersections, managing pore-pressure dissipation over '
                   'decades to prevent long-term secondary consolidation settlement, and designing '
                   'circular precast segmental linings that incorporate fiber-optic sensors to '
                   'monitor ground pressures throughout their century-long service lives. By '
                   'combining empirical ground mechanics with machine-checked digital models, '
                   'engineers construct resilient underground transit networks beneath the densest '
                   'cities on Earth.',
 'cf_bridge': 'Standalone Geotechnical Civil Engineering Flagship & Upstream Thread to Follow: '
              'Written for geotechnical, tunneling, and underground civil engineers designing '
              'urban TBM infrastructure (CSI 31 71 19, ACI 318 precast segmental linings). '
              'Upstream physical thread for the lab: the surfactant/polymer foam conditioning of '
              'cohesive clays inside an EPB-TBM plenum (lowering yield stress tau_0 and '
              'interfacial adhesion so muck flows through the screw conveyor without clogging) '
              'obeys the same two-phase yield-stress dispersion laws as polymeric hydrogel '
              'mobilization in biological ducts.',
 'sources': ['Peck, R. B. (1969). Deep excavations and tunneling in soft ground. Proceedings of '
             'the 7th International Conference on Soil Mechanics and Foundation Engineering, '
             'Mexico City, State-of-the-Art Volume, 225–290.',
             'Mair, R. J., Taylor, R. N., & Bracegirdle, A. (1993). Subsurface settlement profiles '
             'above tunnels in clays. Géotechnique, 43(2), 315–320. DOI: '
             '10.1680/geot.1993.43.2.315.',
             'Anagnostou, G., & Kovári, K. (1996). Face stability conditions with '
             'earth-pressure-balanced shields. Tunnelling and Underground Space Technology, 11(2), '
             '165–173.',
             'ACI Committee 533 / ACI 318 & CSI MasterFormat 31 71 19 Excavation by Tunnel Boring '
             'Machine.',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). ACM Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: 10.1145/3524456.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Peck-Mair Gaussian '
        'surface settlement trough S(y) above an Earth-Pressure-Balance Tunnel Boring Machine">\n'
        '            <line x1="40" y1="42" x2="640" y2="42" stroke="currentColor" '
        'stroke-opacity="0.35" stroke-dasharray="4,3"/>\n'
        '            <path id="tp-e08-trough-path" d="M 60 42 Q 210 43 265 62 Q 340 88 415 62 Q '
        '470 43 620 42" fill="var(--tp-minium-soft)" stroke="var(--tp-minium)" stroke-width="3"/>\n'
        '            <line x1="340" y1="42" x2="340" y2="188" stroke="currentColor" '
        'stroke-opacity="0.25" stroke-dasharray="3,3"/>\n'
        '            <line x1="250" y1="36" x2="250" y2="68" stroke="var(--tp-prussian)" '
        'stroke-width="1.5"/>\n'
        '            <line x1="430" y1="36" x2="430" y2="68" stroke="var(--tp-prussian)" '
        'stroke-width="1.5"/>\n'
        '            <circle id="tp-e08-tbm-shield" cx="340" cy="148" r="34" '
        'fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="3"/>\n'
        '            <circle cx="340" cy="148" r="26" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="1.8" stroke-dasharray="5,3"/>\n'
        '            <text x="52" y="18" font-size="10.5" font-weight="600" '
        'fill="currentColor">Peck–Mair Gaussian Settlement Trough S(y) = S_max exp(−y² / '
        '2i²)</text>\n'
        '            <text id="tp-e08-smax-text" x="352" y="88" font-size="10.5" font-weight="600" '
        'fill="var(--tp-minium)">S_max = 18.8 mm (V_L = 0.75% · i = 12.0 m)</text>\n'
        '            <text x="195" y="35" font-size="9.5" fill="var(--tp-prussian)">−i = −12.0 '
        'm</text>\n'
        '            <text x="436" y="35" font-size="9.5" fill="var(--tp-prussian)">+i = +12.0 '
        'm</text>\n'
        '            <text id="tp-e08-tbm-text" x="195" y="204" font-size="10.5" '
        'fill="var(--tp-verdigris)">EPB-TBM (D = 9.8 m · z_0 = 24.0 m) · P_face = 210 kPa · GNN '
        'Twin PASS</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a 10-meter Earth-Pressure-Balance Tunnel Boring '
        'Machine excavating beneath historic urban foundations with a translucent Peck-Mair '
        'Gaussian settlement trough above would look like (artistic impression, not a measured '
        'structure)',
 'caption': 'Conceptual Vision Plate E.08-V (Imagining What It Would Look Like) · Artistic '
            'geotechnical cross-section imagining an Earth-Pressure-Balance Tunnel Boring Machine '
            '(EPB-TBM) boring through saturated clay beneath a city street while a Graph Neural '
            'Network digital twin monitors the Peck–Mair Gaussian settlement trough.'}

DISPATCH = {'kicker': 'FRONTIER GEOTECHNICAL DISPATCH · EPB-TBM TELEMETRY & GNN SUBSURFACE DIGITAL TWINS',
 'headline': 'Graph Neural Networks & Peck–Mair Gaussian Troughs Prevent Urban Settlement Ahead of '
             'the Cutterhead',
 'body': "Building on Ralph Peck's (1969) and Mair, Taylor & Bracegirdle's (Géotechnique DOI "
         '10.1680/geot.1993.43.2.315) Gaussian subsurface settlement theory, modern '
         'Earth-Pressure-Balance Tunnel Boring Machines fuse real-time cutterhead torque, chamber '
         'pressure, and InSAR satellite radar into physics-constrained Graph Neural Networks to '
         'hold urban building distortion below 1/1,000.'}

META_3D = ('EPB-TBM Peck–Mair Gaussian Settlement Trough',
 'X: Transverse Offset x / i · Z: Tunnel Face Advance · Y: Subsurface Volume-Loss Settlement S(x)')

ES_TRANSLATION = {'title_es': 'Tuneladoras de Equilibrio de Presión de Tierras (EPB-TBM), Cubetas Gaussianas de '
             'Peck–Mair y Gemelos Subterráneos GNN',
 'subtitle_es': 'Cómo la cubeta gaussiana de asentamiento por conservación de volumen de Peck y '
                'Mair S(y) = S_max exp(−y² / 2i²) gobierna la excavación urbana con TBM, acoplada '
                'con Redes Neuronales de Grafos (GNN).',
 'why_es': 'Pasar una cuchara bajo la arena húmeda deja en la superficie una depresión suave más '
           'ancha que la cuchara, cuyo volumen total iguala exactamente el volumen desplazado '
           'abajo.',
 'plain_es': 'En palabras sencillas, excavar un túnel de metro bajo una ciudad habitada es como '
             'retirar arena del fondo de un reloj de arena. Cuando una máquina tuneladora de diez '
             'metros de diámetro avanza veinte metros bajo tierra, corta el suelo arcilloso y '
             'alivia temporalmente la presión natural del terreno. Si la máquina permite que el '
             'suelo ceda aunque sea unos pocos milímetros, la tierra circundante se desplaza hacia '
             'ese hueco. Este movimiento subterráneo viaja hacia arriba a través de los estratos '
             'del suelo y crea una depresión suave en forma de cuenco sobre la calle, conocida '
             'como cubeta de asentamiento. Si ese hundimiento ocurre de forma dispareja bajo un '
             'edificio histórico o tuberías de agua, los muros se agrietan y las estructuras '
             'sufren daños. Las tuneladoras modernas evitan esto inyectando lodos y espumas a '
             'presión controlada frente a la cabeza de corte, mientras sistemas de inteligencia '
             'artificial monitorean el terreno en tiempo real.',
 'deep_es': 'La estabilidad del frente de excavación depende del equilibrio entre dos presiones '
            'fundamentales: la presión de soporte en la cámara de la tuneladora y el empuje '
            'combinado del suelo y el agua subterránea. Si la presión de soporte desciende por '
            'debajo del límite activo de Rankine, el frente colapsa hacia la máquina, '
            'incrementando la pérdida volumétrica y profundizando la cubeta gaussiana en la '
            'superficie. Por el contrario, si la presión de la cámara es excesiva, el suelo se '
            'fractura y la calle se levanta peligrosamente. El umbral crítico de diseño exige que '
            'la distorsión angular de la superficie no supere uno entre quinientos para proteger '
            'mamposterías y cimentaciones urbanas. En la práctica moderna de ingeniería '
            'geotécnica, este balance se logra acondicionando el suelo con espumas poliméricas e '
            'inyectando lechada en el espacio anular del escudo, mientras redes neuronales de '
            'grafos en computadora integran la telemetría de avance para predecir asentamientos '
            'con decenas de metros de anticipación.',
 'bridge_es': 'El acondicionamiento reológico de suelos con espumas tensoactivas en cámaras '
              'EPB-TBM comparte las leyes constitutivas de flujo bifásico con los surfactantes '
              'pulmonares y agentes mucolíticos.'}
