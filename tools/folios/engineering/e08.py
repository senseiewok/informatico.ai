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
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'CIVIL & GEOTECH TUNNELING · REV 1.1',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'S(y) = S_max exp(−y² / 2i²) · V_s = V_L (π D² / 4) · i = K (z_0 − z) · CSI 31 '
                  '71 19',
 'colophon': {'identifier': 'E.08 · EPB-TBM Tunneling & Peck–Mair Settlement · CSI 31 71 19',
              'kernels': 'Peck–Mair Gaussian Trough · Anagnostou–Kovári Face Equilibrium · GNN '
                         'Twin',
              'benchmarks': 'D = 9.8 m · z_0 = 24.0 m · V_L = 0.75% ⇒ S_max = 18.8 mm',
              'bridge': 'EPB Foam Yield-Stress Conditioning ↔ Yield-Stress Gel Flow (analogy only)'},
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
 'steps': ['Stage 1 (Chamber Pressure Balance, after Anagnostou & Kovári 1996): At depth z_0 = 24.0 m, the model EPB chamber pressure P_face = 210 kPa is taken to sit between the active (collapse) and passive (blowout) limits. The folio states no soil profile, so this is an assumed operating point, not a computed face-stability check.',
           'Stage 2 (Foam-Conditioned Muck Rheology): Surfactant-polymer foam injection turns excavated clay into a cohesive, low-permeability plastic paste that can pass the screw conveyor. The 120 mm slump is an illustrative target.',
           'Stage 3 (Peck Gaussian Trough): Volume loss V_L = 0.75% across D = 9.8 m gives V_s = 0.566 m³ per metre of tunnel; with inflection width i = K z_0 = 12.0 m the centerline settlement is S_max = V_s / (√(2π) i) = 18.8 mm.',
           'Stage 4 (Graph Neural Network Subsurface Digital Twin, a Proposal): Cutterhead torque and tail-void grout pressures could update a GNN model whose aim is to keep the trough slope β_max below 1/500 beneath masonry buildings. No such network was built for this folio.'],
 'readouts': [{'label': 'Trough Inflection Width (i = K z_0)',
               'value': '12.0 m (K = 0.50, z_0 = 24 m)'},
              {'label': 'Centerline Max Settlement (S_max)', 'value': '18.8 mm (at V_L = 0.75%)'},
              {'label': 'Max Trough Slope (β_max)', 'value': '1 / 1,050 (< 1/500 model limit)'},
              {'label': 'Geotechnical TBM Verdict', 'value': 'WITHIN MODEL WINDOW (ASSUMED FACE BALANCE)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 31 71 19 / PRECAST SEGMENTAL LINING',
                'title': '9.8 m Earth-Pressure-Balance TBM & Precast Fiber-Reinforced Segmental '
                         'Lining',
                'body': 'Pressurized EPB shield excavation with automated two-component tail-void '
                        'backfill grouting, EPDM elastomeric gasketed C60/75 precast concrete '
                        'tunnel rings, and real-time InSAR + GNN settlement monitoring. A design sketch, not a project specification.',
                'meta': 'Anchor: Mair, Taylor & Bracegirdle 1993, DOI 10.1680/geot.1993.43.2.315 · β ≤ 1/500 is the limit chosen for this model'},
 'sidenote_1': {'kicker': 'SIDENOTE E.08-A · CONSERVATION OF SOIL VOLUME IN PECK–MAIR TROUGHS',
                'body': 'Integrating S(y) = S_max exp(−y² / 2i²) from −∞ to +∞ yields V_s = √(2π) '
                        '· i · S_max. Equating V_s to V_L · (π D² / 4) shows that, with i = K z_0, S_max is '
                        'inversely proportional to depth z_0 while maximum slope occurs at y = '
                        '±i.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.08-B · SPECIFICATION PLATE · CSI 31 71 19 / GNN SUBSURFACE '
                          'TWIN',
                'body': 'A Graph Neural Network could represent borehole stratigraphy and tunnel rings as nodes of a message-passing graph, constrained by Mohr–Coulomb yield surfaces, to forecast the settlement trough some tens of metres ahead of the TBM face. This is a proposed architecture; the folio trained no network and reports no forecast accuracy.'},
 'skill': {'filename': 'epb-tbm-peck-settlement-SKILL.md',
           'name': 'epb-tbm-peck-settlement',
           'description': 'AI-agnostic geotechnical and tunneling civil engineering skill for '
                          'EPB-TBM face pressure equilibrium, Peck-Mair Gaussian settlement '
                          'troughs, and GNN subsurface digital twins.',
           'rules': ['Compute trough inflection distance i = K * (z_0 - z) (K about 0.5 for clays at the surface, lower for sands; treat constant K below the surface as a simplification) and tunnel cross-sectional area A_t = pi * D^2 / '
                     '4.',
                     'Calculate centerline maximum settlement S_max = (V_L * A_t) / (sqrt(2 * pi) '
                     '* i) and maximum transverse slope beta_max = 0.6065 * S_max / i at y = +/- '
                     'i.',
                     'Verify EPB face pressure P_face stays between active collapse pressure '
                     'sigma_h,active + u_0 and passive blowout pressure sigma_v0.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The Graph Neural Network digital twin is now described as a proposal: no network was built, and the claims of 50 m look-ahead forecasts, "GNN PASS" and a "Rankine pass" verdict are withdrawn. The 1/500 slope limit is labelled as the choice of this model, not a value taken from a named standard, and the page now says that a constant K below the surface is a simplification of what Mair, Taylor & Bracegirdle (1993) reported. The Brunel opening is cut back to the commonly told account, and the foam note is marked as an analogy.',
                'opus': 'Review: references checked by DOI in the Scite index on 2026-11-14; S_max = 18.8 mm and the slope 1/1,050 were recomputed by hand from the stated law.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-02',
                'summary': 'REV 1.0 (Published 2026-11-02): Inaugural Volume IV geotechnical & '
                           'underground tunneling monograph uniting Peck-Mair Gaussian settlement '
                           'troughs (DOI 10.1680/geot.1993.43.2.315) with EPB-TBM chamber '
                           'mechanics and GNN subsurface digital twins.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'exact Gaussian integral V_s = sqrt(2*pi)*i*S_max = 0.565 m^3/m and S_max '
                        '= 18.8 mm at V_L = 0.75%, D = 9.8 m, i = 12.0 m. This was an arithmetic check only; no other verification is claimed.'}],
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
           'summary': 'Scite index entry for Mair, Taylor & Bracegirdle 1993 (DOI 10.1680/geot.1993.43.2.315), fetched 2026-11-08: 575 citing publications (6 supporting, 183 mentioning, 0 contrasting) and no retraction notice. These counts describe that one paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1680/geot.1993.43.2.315',
           'fetched_on': '2026-11-08',
           'citing_publications': 575,
           'supporting': 6,
           'mentioning': 183,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Mair, Taylor & Bracegirdle 1993 (DOI 10.1680/geot.1993.43.2.315), fetched 2026-11-08: 575 citing publications (6 supporting, 183 mentioning, 0 contrasting) and no retraction notice. These counts describe that one paper, not this folio.'},
 'act1_title': "Act I — From Marc Brunel's Thames Shield to Earth-Pressure-Balance TBMs & "
               'Subsurface AI Digital Twins',
 'act1_dropcap': 'In 1818 the French-born engineer Marc Isambard Brunel patented a tunnelling shield. The account usually given is that the idea came from the shipworm, a marine mollusc that bores through submerged timber with the shell plates at its head and lines the burrow behind it with a hard calcareous layer. Brunel and his son Isambard Kingdom Brunel then used a shield to drive a tunnel beneath the River Thames. Work began in 1825 and, after floods and long stoppages, the tunnel opened in 1843. It showed that soft, waterlogged ground could be tunnelled, and it left a question that tunnel engineers still work on: how does removing soil deep underground reshape the surface of the city above?',
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
                      'pumping cement grout around the newly placed concrete rings. This folio also sketches how graph-based machine learning could help forecast ground movement from machine data. That part is a proposal, not a description of a system in service.',
 'act1_body': 'In 1969, Ralph B. Peck drew together field observations from soft-ground tunnels in his state-of-the-art report to the Mexico City soil mechanics conference, and showed that the surface settlement across a tunnel is well described by an inverted Gaussian bell curve. In 1993, Robert J. Mair, R. N. Taylor, and A. Bracegirdle (Géotechnique, DOI 10.1680/geot.1993.43.2.315) examined settlement profiles below the surface in clays. They found these too can be described by Gaussian curves, but that the troughs at depth are wider than a constant K in i = K (z_0 − z) would give. This folio keeps a constant K = 0.5 and works at the surface, where that value is a common choice for clays. Today, Earth-Pressure-Balance Tunnel Boring Machines (EPB-TBMs) of about ten metres diameter excavate beneath cities by pressurizing foam-conditioned muck in the chamber behind the cutterhead. This pressurized paste balances earth and pore-water pressure at the face (Anagnostou & Kovári 1996, DOI 10.1016/0886-7798(96)00017-X). The folio proposes that telemetry from thrust cylinders and tail-void grout pumps could feed a Graph Neural Network (GNN) model that forecasts the settlement trough ahead of the machine. No such model was built here, and no forecast distance or accuracy is claimed. CSI MasterFormat 31 71 19 is named only to classify the work.',
 'act1_stakes': 'The practical stakes of urban tunneling are measured in the preservation of '
                'ancient architecture and modern utility networks. When an earth pressure balance '
                'shield loses face pressure, even for a few minutes, saturated silt and gravel can '
                'wash into the cutterhead, triggering an active ground collapse that propagates '
                'upward as a sudden sinkhole. Conversely, applying excessive support pressure '
                'heaves the street upward, shearing underground gas mains and cracking water '
                'distribution pipes. The most subtle danger is differential settlement: when one '
                'corner of a masonry structure settles more than another, shear stresses '
                'accumulate in unreinforced mortar joints. A slope of about one in five hundred is a limit often quoted in foundation engineering for the onset of cracking in buildings; this folio adopts it as its model threshold and does not take it from a named standard. Avoiding damage requires continuous equilibrium between '
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
                 'Mair, Taylor & Bracegirdle publish subsurface settlement profiles above tunnels in clays in Géotechnique (DOI 10.1680/geot.1993.43.2.315).'),
                ('1996',
                 'Anagnostou & Kovári publish face stability conditions for earth-pressure-balanced shields (DOI 10.1016/0886-7798(96)00017-X).'),
                ('2026',
                 'This folio proposes, as a design study, a physics-constrained GNN subsurface digital twin fed by EPB-TBM telemetry.')],
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
                   'fraction V_L. Assuming the ground deforms at constant volume, as is usual for clays in the short term, the volume of the surface settlement trough V_s per unit tunnel advance equals V_L (pi D^2 / 4). Following Peck, this volume is distributed as an inverted Gaussian curve S(y) = S_max exp(-y^2 / [2 i^2]), where the inflection distance i = K (z_0 - z) sets the trough width. Centerline maximum settlement is S_max = V_s / (sqrt(2 pi) i). The maximum ground slope occurs at y = +-i and equals beta_max = 0.6065 S_max / i. With D = 9.8 m, V_L = 0.75%, K = 0.5 and z_0 = 24 m these give V_s = 0.566 m^3/m, i = 12.0 m, S_max = 18.8 mm and beta_max = 1/1,050. The model keeps beta_max below 1/500, a limit chosen for this folio. The face pressure slider is not tied to V_L by a stated law: the 210 kPa default is an assumed operating point.',
 'act2_deepening': 'At the microscopic scale, the behavior of excavated soil inside the '
                   'pressurized plenum depends on foam conditioning rheology. Dry or sticky clay '
                   'clumps into dense masses that jam the cutterhead and adhere to the screw '
                   'conveyor, causing erratic pressure spikes and uncontrolled volume loss. '
                   'Injecting surfactant-polymer foam transforms stiff cohesive soil into a '
                   'homogeneous, low-permeability plastic paste (the slump of 120 to '
                   '180 millimeters used here is illustrative). This conditioned paste acts as a continuous hydraulic '
                   'cushion, transmitting thrust evenly across the tunnel face. Meanwhile, behind '
                   'the shield, rapid injection of two-component cementitious grout into the '
                   'annular tail void prevents the surrounding soil from relaxing into the gap '
                   'left by the steel shell. A Graph Neural Network could model this three-dimensional interaction by representing borehole strata, cutterhead sensors and individual lining rings as connected nodes, trained on past geotechnical records and machine telemetry. That is the proposal of this folio; it has not been built or tested here.',
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
 'act4_human_ai': 'In subway and utility tunnelling, a GNN subsurface digital twin could take in TBM cutterhead torque, screw-conveyor mass flow and InSAR satellite interferometry, and suggest adjustments to foam injection and tail-void grout pressure ring by ring. A reader who wants to try this could stage an elastoplastic finite-element excavation in FEniCS/dolfinx (https://github.com/FEniCS/dolfinx, DOI 10.1145/3524456) and fit sparse models to settlement data with dynamicslab/pysindy (Brunton et al. 2016, DOI 10.1073/pnas.1517384113). Both tools are named as starting points; the folio ran neither.',
 'act4_deepening': 'Looking ahead, tunnelling engineers could work with machine-learning models to read complex urban geology. A boring machine could combine seismic look-ahead sensing with a digital twin that follows cutterhead torque, cutter wear and muck weight, and that suggests foam ratios and face pressure adjustments as the ground changes. This is a possible direction, not a description of machines in service. Important questions remain '
                   'active areas of study: accurately predicting three-dimensional ground response '
                   'around skewed tunnel intersections, managing pore-pressure dissipation over '
                   'decades to prevent long-term secondary consolidation settlement, and designing '
                   'circular precast segmental linings that incorporate fiber-optic sensors to '
                   'monitor ground pressures throughout their service lives. Empirical ground mechanics and data-driven models, used together and checked against field measurements, are one route to building underground transit beneath dense cities with less surface damage.',
 'cf_bridge': 'Standalone geotechnical folio, written for geotechnical and tunnelling engineers. A note on analogy for readers of the other folios: foam conditioning lowers the yield stress and stickiness of clay so that it flows through the screw conveyor, and yield-stress fluids are also the language used to describe gels in other fields. The resemblance is one of vocabulary and general fluid mechanics. This folio does not model any biological fluid, and nothing here bears on health or treatment.',
 'sources': ['Peck, R. B. (1969). Deep excavations and tunneling in soft ground. Proceedings of '
             'the 7th International Conference on Soil Mechanics and Foundation Engineering, '
             'Mexico City, State-of-the-Art Volume, 225–290.',
             'Mair, R. J., Taylor, R. N., & Bracegirdle, A. (1993). Subsurface settlement profiles '
             'above tunnels in clays. Géotechnique, 43(2), 315–320. DOI: '
             '10.1680/geot.1993.43.2.315.',
             'Anagnostou, G., & Kovári, K. (1996). Face stability conditions with '
             'earth-pressure-balanced shields. Tunnelling and Underground Space Technology, 11(2), '
             '165–173. DOI: 10.1016/0886-7798(96)00017-X.',
             'Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing equations from data by sparse identification of nonlinear dynamical systems (dynamicslab/pysindy, https://github.com/dynamicslab/pysindy). PNAS, 113(15), 3932–3937. DOI: 10.1073/pnas.1517384113.',
             'CSI MasterFormat 31 71 19, Tunnel Excavation by Tunnel Boring Machine (classification only; no threshold on this page is taken from it).',
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
        'Twin (proposed)</text>\n'
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
 'headline': 'Could Graph Neural Networks and Peck–Mair Gaussian Troughs Forecast Urban Settlement Ahead of the Cutterhead?',
 'body': "Building on Ralph Peck's (1969) Gaussian settlement trough and the subsurface profiles of Mair, Taylor & Bracegirdle (Géotechnique, DOI 10.1680/geot.1993.43.2.315), this folio proposes that cutterhead torque, chamber pressure and InSAR satellite radar from an Earth-Pressure-Balance Tunnel Boring Machine could feed a physics-constrained Graph Neural Network. In the folio's worked example the trough slope is 1/1,050. Nothing was trained or deployed."}

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
             'sufren daños. Las tuneladoras modernas reducen este riesgo inyectando espumas a presión controlada frente a la cabeza de corte y lechada alrededor de los anillos. Este folio plantea además, como propuesta, que modelos de aprendizaje automático basados en grafos podrían ayudar a pronosticar el movimiento del terreno; no describe un sistema en operación.',
 'deep_es': 'La estabilidad del frente de excavación depende del equilibrio entre dos presiones '
            'fundamentales: la presión de soporte en la cámara de la tuneladora y el empuje '
            'combinado del suelo y el agua subterránea. Si la presión de soporte desciende por '
            'debajo del límite activo de Rankine, el frente colapsa hacia la máquina, '
            'incrementando la pérdida volumétrica y profundizando la cubeta gaussiana en la '
            'superficie. Por el contrario, si la presión de la cámara es excesiva, el suelo se '
            'fractura y la calle se levanta. El modelo del folio mantiene la pendiente máxima de la cubeta por debajo de uno entre quinientos, un límite elegido para este modelo y no tomado de una norma. Con D = 9.8 m, V_L = 0.75 %, K = 0.5 y z_0 = 24 m, la ley de Peck da S_max = 18.8 mm y una pendiente de 1/1,050. En la práctica, el balance se busca acondicionando el suelo con espumas e inyectando lechada en el espacio anular del escudo. El folio propone que una red neuronal de grafos podría integrar la telemetría de avance para pronosticar asentamientos; esa red no se construyó ni se probó aquí.',
 'bridge_es': 'El acondicionamiento con espumas reduce el esfuerzo de fluencia de la arcilla para que fluya por el tornillo sinfín; los fluidos con esfuerzo de fluencia también se usan para describir geles en otros campos. Es solo una analogía: este folio no modela ningún fluido biológico ni trata de salud.'}
