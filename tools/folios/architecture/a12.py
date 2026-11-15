#!/usr/bin/env python3
"""Folio A.12 (ARCHITECTURE): Tensegrity Cable-Strut Domes & Radiative Sky-Cooling Envelopes: Pellegrino Equilibrium Nullspaces, Prestress Stiffening & Zero-Energy Cooling."""
from __future__ import annotations

SLUG = 'a12'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.12',
 'slug': 'a12',
 'pillar': 'architecture',
 'category_code': 'A',
 'parent_folios': ['A.04', 'A.08', 'A.10'],
 'lineage_mode': 'SYNTHESIS · Synthesizes A.04 Lightweight Exoskeletons, A.08 Radiative '
                 'Sky-Cooling & A.10 Deployable Skins',
 'title': 'Tensegrity Cable-Strut Domes & Radiative Sky-Cooling Envelopes: Pellegrino Equilibrium '
          'Nullspaces, Prestress Stiffening & Zero-Energy Cooling',
 'subtitle': "Synthesizing Folio A.04's lightweight megastructures, A.08's 8–13 μm radiative sky "
             "cooling, and A.10's deployable skins: a design study of how the floating-compression tensegrity of Kenneth Snelson and Buckminster Fuller could carry a radiative sky-cooling membrane over a civic canopy.",
 'date_published': '2026-11-07',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'TENSEGRITY & SKY-COOL · REV 1.1',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'A t = f · K_T = K_E + K_G(t_0) ≻ 0 · P_cool = P_rad(T_s) − P_atm(T_amb) − P_sun',
 'colophon': {'identifier': 'A.12 · Tensegrity Cable-Strut Domes & 8–13 μm Sky-Cooling Canopies · '
                            'ASCE 19',
              'kernels': 'Pellegrino–Calladine SVD Nullspace (s ≥ 1, m ≥ 0) · Geometric Stiffness '
                         'K_G(t_0) · Raman 8–13 μm',
              'benchmarks': 'Model values: t_0 = 185 kN · q_net = 98.4 W/m² at air temperature ⇒ ΔT ≈ −5.2 °C for an assumed 18.9 W/(m²·K)',
              'bridge': 'Synthesizes A.04/A.08/A.10 · Analogy: cellular tensegrity hypothesis (Ingber 1993) ↔ prestressed cable domes'},
 'sliders': [{'label': 'Cable Prestress Self-Stress Level (t_0)',
              'min': 40.0,
              'max': 320.0,
              'step': 5.0,
              'value': 185.0,
              'unit': ' kN'},
             {'label': '8–13 μm Atmospheric Window Emissivity (ε_LWIR)',
              'min': 0.7,
              'max': 0.99,
              'step': 0.01,
              'value': 0.96,
              'unit': 'ε = '}],
 'steps': ['Stage 1 (Snelson–Fuller Islands of Compression in an Ocean of Tension): Isolated steel '
           'compression struts float without touching one another, suspended inside a continuous '
           'prestressed cable net (Calladine 1978, DOI 10.1016/0020-7683(78)90052-5).',
           'Stage 2 (Pellegrino–Calladine Equilibrium Matrix SVD): Singular Value Decomposition of '
           'the equilibrium matrix A (Pellegrino & Calladine 1986, DOI '
           '10.1016/0020-7683(86)90014-4) identifies s = dim ker(A) self-stress states and m = dim '
           'ker(Aᵀ) infinitesimal mechanisms.',
           'Stage 3 (Geometric Prestress Stiffening K_G(t_0) ≻ 0): Just as tightening a guitar '
           'string raises its pitch, cable prestress t_0 makes the geometric stiffness matrix '
           'K_G(t_0) positive on the mechanism modes, so the prestressed structure is stiff in the model. The structural mass figure of 12.4 kg/m² shown on this page is illustrative, not a design result.',
           "Stage 4 (Daytime Radiative Sky-Cooling Membrane Canopy, Continuing A.08): The membrane is assumed to reflect 97% of an assumed 1,000 W/m² of sunlight, as the photonic surface of Raman et al. did (2014, DOI 10.1038/nature13883), so it absorbs 30 W/m². The model assigns a net radiative exchange with the sky of 128.4 W/m² at air temperature, a fixed illustrative value, so q_net = 128.4 − 30 = 98.4 W/m². Divided by an assumed combined heat-exchange coefficient of about 18.9 W/(m²·K), that gives a membrane surface about 5.2 °C below the air in the model."],
 'readouts': [{'label': 'Tangent Stiffness λ_min(K_E + K_G)',
               'value': '+42.8 kN/m (Illustrative, Positive in Model)'},
              {'label': 'Structural Steel Aerial Mass', 'value': '12.4 kg/m² (Illustrative, 120 m Span)'},
              {'label': 'Net Daytime Sky-Cooling Flux', 'value': '98.4 W/m² (Model, at Air Temperature)'},
              {'label': 'Sub-Ambient Canopy Drop (ΔT)', 'value': '−5.2 °C Membrane Surface (Model)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 05 16 00 / 13 31 23 / ASCE 19 STRUCTURAL CABLES',
                'title': 'Geiger–Levy Cable-Strut Tensegrity Domes with Photonic Radiative '
                         'Sky-Cooling PTFE Cladding',
                'body': 'Design proposal: a Geiger-type circular cable dome, prestressed so that its geometric stiffness K_G(t_0) is positive on its mechanism modes, clad in a microporous radiative sky-cooling membrane. Not an engineered or tested assembly; NREL/EnergyPlus is named as a tool a reader could use, and this folio ran no simulation.',
                'meta': 'References: Pellegrino & Calladine (1986) DOI 10.1016/0020-7683(86)90014-4 · Raman et al. (2014) DOI 10.1038/nature13883 · ASCE 19 is the standard for structural applications of steel cables; it sets none of this folio\'s values'},
 'sidenote_1': {'kicker': 'SIDENOTE A.12-A · CROSS-FIELD ANALOGY · BICYCLE WHEELS, LIVING CELLS & '
                          'THE SAHARAN SILVER ANT',
                'body': 'A bicycle wheel is stiff because its thin spokes are pretensioned, so they never have to carry compression. Donald Ingber proposed that living cells use a similar tensegrity principle in their cytoskeleton (1993, DOI 10.1242/jcs.104.3.613). Saharan silver ants are covered in hairs that raise their near-infrared reflection and help them shed heat by thermal radiation (Shi et al. 2015, DOI 10.1126/science.aab3564). Joining a tensegrity dome to a radiative-cooling skin is this folio\'s design idea.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.12-B · OPEN-SOURCE BUILDING PHYSICS · NREL/ENERGYPLUS & '
                          'COMPAS',
                'body': 'Open tools such as compas-dev/compas (for equilibrium matrices and form finding) and NREL/EnergyPlus (for whole-building energy) could be used to test a canopy like this one. This folio ran neither. A cooler membrane is not a heat-safety measure, and nothing here is guidance on protecting people during heatwaves.'},
 'skill': {'filename': 'tensegrity-nullspace-skycooling-SKILL.md',
           'name': 'tensegrity-nullspace-skycooling',
           'description': 'AI-agnostic architectural engineering skill for Pellegrino-Calladine '
                          'tensegrity equilibrium matrix SVD (s = dim ker(A), m = dim ker(A^T)), '
                          'geometric prestress stiffening K_G(t_0), and 8-13 um radiative '
                          'sky-cooling membranes.',
           'rules': ['Compute Singular Value Decomposition of equilibrium matrix A to extract '
                     'self-stress vector t_0 in ker(A) with strictly positive tension in all '
                     'cables.',
                     'Verify first-order prestress stability by checking u^T * K_G(t_0) * u > 0 '
                     'for all inextensional mechanism modes u in ker(A^T).',
                     'Evaluate net daytime radiative cooling flux q_net = P_rad(T_s) - '
                     'P_atm(T_amb) - (1 - R_solar) * I_sun across the 8-13 um atmospheric '
                     'window.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The opening scene of Snelson and Fuller was dramatized and is replaced by a plain account, and the 2026 chronology entry that presented this folio\'s canopy as a built project is withdrawn. Unsourced figures (85% less steel, 80% of capacity spent on self-weight, a bicycle wheel carrying 100 times its weight, a World Economic Forum ranking) and public-health and zero-energy claims are removed; the 98.4 W/m² and −5.2 °C values now state the assumptions they follow from, and the stiffness and mass readouts are labelled illustrative.',
                'opus': 'Review: references checked by DOI in Crossref and Scite; central claims checked against the Scite index; arithmetic recomputed from the stated balance.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-07',
                'summary': 'REV 1.0 (Published 2026-11-07): Volume VI Architecture synthesis '
                           'monograph uniting Pellegrino & Calladine tensegrity matrix mechanics '
                           '(DOI 10.1016/0020-7683(86)90014-4) with Raman daytime radiative sky '
                           'cooling (DOI 10.1038/nature13883).',
                'opus': "Council review (Gemini 4 Argon + Qwen 3.8 27B + Gemma 4 31B) of the Maxwell-Calladine rule b - 3j + 6 = s - m and the stiffness formulation. Its 'verified' wording for the radiative balance is withdrawn in REV 1.1: no Planck calculation was run, and the cooling figures are model values."}],
 'volume': 6,
 'volume_code': 'VOL. 06',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1126/science.aat9513',
           'fetched_on': '2026-11-08',
           'citing_publications': 2317,
           'supporting': 23,
           'mentioning': 1629,
           'contrasting': 4,
           'retracted': False,
           'summary': "Scite index entry for Mandal et al., Hierarchically porous polymer coatings for highly efficient passive daytime radiative cooling (DOI 10.1126/science.aat9513), checked 2026-11-08: 2,317 citing publications (23 supporting, 1,629 mentioning, 4 contrasting) and no retraction notice. The counts describe that paper, not this folio's model."}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['A.04', 'A.08', 'A.10'],
 'lineage_mode': 'SYNTHESIS · Synthesizes A.04 Lightweight Exoskeletons, A.08 Radiative '
                 'Sky-Cooling & A.10 Deployable Skins',
 'scite': {'doi': '10.1126/science.aat9513',
           'fetched_on': '2026-11-08',
           'citing_publications': 2317,
           'supporting': 23,
           'mentioning': 1629,
           'contrasting': 4,
           'retracted': False,
           'summary': "Scite index entry for Mandal et al., Hierarchically porous polymer coatings for highly efficient passive daytime radiative cooling (DOI 10.1126/science.aat9513), checked 2026-11-08: 2,317 citing publications (23 supporting, 1,629 mentioning, 4 contrasting) and no retraction notice. The counts describe that paper, not this folio's model."},
 'act1_title': 'Act I — Floating Struts in a Net of Cable, and a Skin That Radiates to the Sky',
 'act1_dropcap': "In the late 1940s the art student Kenneth Snelson, who had met Buckminster Fuller at Black Mountain College in North Carolina, made small sculptures in which wooden struts were held apart, without touching one another, by taut cords. Fuller named the principle tensegrity, from tension and integrity: islands of compression inside a continuous network of tension. Such frameworks can look floppy on paper. C. R. Calladine (1978, DOI 10.1016/0020-7683(78)90052-5) and Sergio Pellegrino with Calladine (1986, DOI 10.1016/0020-7683(86)90014-4) at Cambridge showed how to count their mechanisms and states of self-stress, and how prestress in the cables can stiffen mechanisms that would otherwise move freely, much as tuning a slack string stiffens it. This folio is a design study that pairs a prestressed cable dome with a daytime radiative sky-cooling membrane.",
 'act1_plain_bridge': 'In plain words, think of how a bicycle wheel works. A bicycle wheel has '
                      'thin wire spokes that would bend and buckle if you pressed on them with '
                      'your thumb. Yet when you tighten every spoke inside the outer metal rim, '
                      'the wheel can easily support the weight of an adult riding over rough '
                      'cobblestones. The secret is pretension: because every wire is pulled tight '
                      'from the start, downward weight simply relaxes the tension slightly without '
                      'allowing the wire to bend. A tensegrity cable dome works on this exact same '
                      'principle across a giant scale. Instead of building massive steel trusses '
                      'that weigh down a stadium roof, engineers float isolated steel posts inside '
                      'a taut web of high-strength cables, creating a light canopy. If that canopy is covered with a white membrane that reflects most of the noon sun and radiates heat through the infrared window toward space, the membrane itself can stay a few degrees below the air temperature, according to this folio\'s model. How much cooler the air in the plaza beneath would be is not modeled here.',
 'act1_body': 'In 1978 and 1986, Cambridge engineers C. R. Calladine (DOI '
              '10.1016/0020-7683(78)90052-5) and Sergio Pellegrino (International Journal of '
              'Solids and Structures, DOI 10.1016/0020-7683(86)90014-4) resolved the tensegrity '
              'paradox using the Singular Value Decomposition of the equilibrium matrix A. While '
              "Maxwell's classical rule b - 3j + 6 = s - m only counts structural members and "
              'joints, SVD reveals two fundamental vector subspaces: the nullspace ker(A) of '
              'dimension s (states of self-stress where internal cable tension exists without '
              'external loads) and the left nullspace ker(A^T) of dimension m (infinitesimal '
              'kinematic mechanisms). When prestress tension t_0 is introduced into the cable '
              'network, the structural tangent stiffness matrix K_T = K_E + K_G(t_0) acquires '
              'positive-definite geometric stiffness, locking floppy mechanism modes into rigid '
              "equilibrium. This folio pairs such a cable-strut skeleton with daytime radiative sky-cooling physics (Raman et al. 2014, DOI 10.1038/nature13883; Mandal et al. 2018, DOI 10.1126/science.aat9513). In its model the membrane is assumed to reflect 97% of sunlight and the canopy surface gives 98.4 W/m² of net cooling at air temperature. Open tools such as NREL/EnergyPlus (https://github.com/NREL/EnergyPlus) are named as tools a reader could use to test the idea; the folio ran no simulation.",
 'act1_stakes': 'Long-span civic roofs over stadiums, transit hubs and exhibition halls have often been built as heavy steel trusses, and much of a long-span roof\'s capacity goes into carrying its own weight. Cable domes of the Geiger and Levy types are a lighter alternative that carries load mainly in tension. A sunlit roof also heats up and adds to the cooling load of the building beneath it. The idea here is to combine a light prestressed structure with a skin that stays below air temperature in sunlight. It is a design hypothesis: this folio does not compare steel weights and does not claim that such a canopy would replace mechanical cooling.',
 'pullquote': '"A prestressed cable dome can be light because its cables only ever pull; '
              'a radiative skin can stay below air temperature because the 8–13 μm window lets it lose heat to the sky. This folio asks what happens if one structure does both."',
 'chronology': [('1948–1962',
                 "Kenneth Snelson's floating-strut sculptures and R. Buckminster Fuller's term 'tensegrity' (tensional "
                 'integrity): isolated compression struts held inside continuous tension '
                 'nets.'),
                ('1978–1986',
                 'C. R. Calladine (DOI 10.1016/0020-7683(78)90052-5) and Sergio Pellegrino (DOI '
                 '10.1016/0020-7683(86)90014-4) formulate the SVD equilibrium matrix and geometric '
                 'prestress stiffness theory.'),
                ('2014',
                 'Aaswath Raman and Shanhui Fan demonstrate daytime sub-ambient radiative sky '
                 'cooling through the 8–13 μm atmospheric window (DOI 10.1038/nature13883).'),
                ('2018',
                 'Mandal et al. report porous P(VdF-HFP) coatings that stay about 6 °C below ambient in sunlight (DOI 10.1126/science.aat9513). This folio (2026) proposes, but has not built or simulated, a cable dome clad in such a membrane.')],
 'act2_title': 'Act II — Cross-Field Intuition: Guitar-String Prestress + The 8–13 μm Window to '
               'Outer Space',
 'act2_analogy': 'A tensegrity sky-cooling canopy operates like a bicycle wheel cross-bred with a '
                 'guitar string: tightening the tension spokes makes a floppy wire web rock-solid '
                 'without adding heavy metal beams. Meanwhile, its outer white skin functions like '
                 'the microscopic silver fur of the Saharan ant: it bounces harsh desert sunlight '
                 'away like a mirror while opening a clear infrared window that radiates internal '
                 'urban heat straight into the freezing void of deep space.',
 'act2_plain_primer': 'To design this floating, passively cooled canopy, engineers would tune '
                      'two physical knobs. The first knob controls the mechanical pretension '
                      'jacked into the steel cables during erection. When this knob is at a low '
                      'setting, the cables hang slack and the suspended steel struts wobble like '
                      'an untuned instrument. As technicians crank the tension up toward its '
                      'design level, geometric stiffness locks into place across the entire dome: '
                      'the structure snaps into rigid equilibrium, capable of supporting heavy '
                      'wind gusts and maintenance crews while staying light (the twelve kilograms per square meter shown here is an illustrative figure). The second knob sets the thermal emissivity of '
                      'the white roof membrane within the atmospheric infrared window. Dialing '
                      'this knob upward opens the sky window, allowing the canopy to radiate its '
                      'stored heat directly toward the cold depths of outer space. When both knobs '
                      'are properly adjusted, the model dome is stiff and its membrane stays below the air temperature. The readouts are model values, not measurements, and the air temperature in the plaza is not modeled.',
 'distill_diagram': {'analogy_title': 'The Bicycle-Wheel Guitar String',
                     'analogy_sub': 'Cable tension locks floating struts while photonic skin cools '
                                    'plaza',
                     'force_a_title': 'Cable Prestress Level (t_0)',
                     'force_a_sub': 'Jacks positive-definite geometric stiffness to eliminate '
                                    'mechanism',
                     'force_b_title': 'Sky-Window Emissivity (ε_LWIR)',
                     'force_b_sub': 'Beams 8–13 μm thermal infrared waves into 3 K deep outer '
                                    'space',
                     'threshold_title': 'Tangent Stiffness Stability (K_T ≻ 0)',
                     'threshold_pass': 'Stiff prestressed canopy in the model; membrane surface about 5.2 °C below air in the model',
                     'threshold_fail': 'Slack cables cause floppy mechanism or low emissivity '
                                       'traps heat'},
 'act2_intuition': 'Why does a bicycle wheel easily carry a heavy rider when a single loose spoke '
                   'would buckle under the gentle push of a finger? Because the outer rim holds '
                   'every spoke in high initial tension t_0, so an applied downward load merely '
                   'relaxes tension slightly in upper spokes without ever pushing any wire into '
                   'compressive buckling. In a three-dimensional tensegrity dome governed by '
                   "equilibrium matrix equation A t = f, Sergio Pellegrino's Singular Value "
                   'Decomposition extracts the precise self-stress state vector t_0 residing in '
                   'the nullspace ker(A) that ensures every cable remains taut while isolated '
                   'compression struts float in pure compression. For any infinitesimal floppy '
                   'mechanism mode u in the left nullspace ker(A^T) where linear elastic stiffness '
                   'vanishes (K_E u = 0), the second-order geometric work u^T K_G(t_0) u > 0 '
                   'increases linearly with cable pretension t_0; when it is positive for every mechanism mode, the total tangent '
                   'stiffness is positive-definite. The stretched membrane is assumed to reflect 97% of solar '
                   'radiation across 0.3–2.5 micrometers while emitting strongly through '
                   'the 8–13 micrometer atmospheric window, where it can lose heat toward the cold sky.',
 'act2_deepening': "In a Geiger or Levy cable dome, raising the cable pretension t_0 raises the lowest eigenvalue of the tangent stiffness matrix K_T on the mechanism modes, and it also keeps the cladding membrane taut; a slack membrane can flutter in wind or pond water. Thermally, the folio's balance is q_net = P_rad(T_s) - P_atm(T_amb) - (1 - R_solar) I_sun. With R_solar = 0.97 and an assumed I_sun = 1,000 W/m^2, the membrane absorbs 30 W/m^2. The model assigns a net radiative exchange with the sky of 128.4 W/m^2 at air temperature (a fixed illustrative value), so q_net = 98.4 W/m^2. At equilibrium that cooling is balanced by heat gained from the air; with an assumed combined heat-exchange coefficient of about 18.9 W/(m^2 K), the surface settles about 5.2 C below the air. Stronger wind would raise that coefficient and shrink the drop. For comparison, Raman et al. (2014) measured 4.9 C below ambient and Mandal et al. (2018) about 6 C. These are model values, not measurements.",
 'walkthrough': ['Experiment 1 (Cable Self-Stress Prestress t_0): Drag Cable Prestress t_0 from 40 '
                 'kN up to 320 kN. Watch minimum tangent stiffness λ_min(K_E + K_G) climb as '
                 'geometric prestress locks the floating struts.',
                 'Experiment 2 (8–13 μm Sky-Window Emissivity ε_LWIR): Increase LWIR Emissivity '
                 'from 0.70 to 0.96. In the model, net daytime cooling reaches 98.4 W/m² at the default and the membrane surface settles about 5.2 °C below the air.',
                 'Experiment 3 (Counterfactual Knockout ⚡): Click [⚡ Counterfactual] to slacken '
                 'the self-stress nullspace state t_0 -> 0 and watch the tensegrity mechanism '
                 'soften.'],
 'act4_title': "Act IV — Imagining Humanity's Future: Zero-Compressor Cooling Canopies for "
               'Extreme-Heat Cities',
 'act4_human_ai': 'Hot cities need shade and cooler surfaces. Combining open-source structural form-finding (https://github.com/compas-dev/compas) with open-source building energy modeling (https://github.com/NREL/EnergyPlus) and inverse photonic design, designers in hot cities could study light cable canopies with radiative-cooling membranes over schoolyards, transit stops and markets. That is a proposal: this folio ran neither tool, and its −5.2 °C is a model value for the membrane surface, not a cooler plaza.',
 'act4_deepening': 'Computational designers could plan such canopies by coupling structural equilibrium solvers in compas-dev/compas with building physics models in NREL/EnergyPlus and optimizing cable sizes, prestress and membrane coatings together. During construction, jacks with load cells could tension the cable net, and sensors could track cable forces over the seasons. These are proposals, not a description of current practice. Important open '
                   'questions define the frontier of tensegrity engineering: How can active '
                   'shape-memory alloy tendons dynamically retension cable nets during extreme '
                   'hurricane wind loads to prevent fatigue failure? How can self-cleaning '
                   'superhydrophobic coatings preserve ninety-seven percent solar reflectance over '
                   'decades of urban dust and pollution without manual washing? Those questions decide whether the idea is practical.',
 'cf_bridge': 'Standalone Lightweight Tensegrity & Passive-Cooling Envelope Design Study (A.04 + A.08 + '
              'A.10 -> A.12): Engineered for structural cable-net, architectural envelope, and '
              'urban microclimate designers.',
 'sources': ['Mandal, J., Fu, Y., Overvig, A. C., Jia, M., Sun, K., Shi, N. N., Zhou, H., Xiao, '
             'X., Yu, N., & Yang, Y. (2018). Hierarchically porous polymer coatings for highly '
             'efficient passive daytime radiative cooling. Science, 362(6412), 315–319. DOI: '
             '10.1126/science.aat9513.',
             'Pellegrino, S., & Calladine, C. R. (1986). Matrix analysis of statically and '
             'kinematically indeterminate frameworks. International Journal of Solids and '
             'Structures, 22(4), 409–428. DOI: 10.1016/0020-7683(86)90014-4.',
             "Calladine, C. R. (1978). Buckminster Fuller's 'Tensegrity' structures and Clerk "
             "Maxwell's rules for the construction of stiff frames. International Journal of "
             'Solids and Structures, 14(2), 161–172. DOI: 10.1016/0020-7683(78)90052-5.',
             'Raman, A. P., Anoma, M. A., Zhu, L., Rephaeli, E., & Fan, S. (2014). Passive '
             'radiative cooling below ambient air temperature under direct sunlight. Nature, 515, '
             '540–544. DOI: 10.1038/nature13883.',
             'Open-Source Stack: NREL/EnergyPlus (https://github.com/NREL/EnergyPlus) + '
             'compas-dev/compas (https://github.com/compas-dev/compas). Named as tools a reader could use; not run for this folio.',
             'Ingber, D. E. (1993). Cellular tensegrity: defining new rules of biological design that govern the cytoskeleton. Journal of Cell Science, 104(3), 613–627. DOI: 10.1242/jcs.104.3.613.',
             'Shi, N. N., Tsai, C.-C., Camino, F., Bernard, G. D., Yu, N., & Wehner, R. (2015). Keeping cool: Enhanced optical reflection and radiative heat dissipation in Saharan silver ants. Science, 349(6245), 298–301. DOI: 10.1126/science.aab3564.',
             'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). '
             'Dedalus: A flexible framework for numerical simulations with spectral methods '
             '(DedalusProject/dedalus, https://github.com/DedalusProject/dedalus). Physical Review '
             'Research, 2(2), 023068. DOI: 10.1103/PhysRevResearch.2.023068.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Tensegrity '
        'Floating-Compression Cable Dome and 8-13 Micrometer Daytime Radiative Sky-Cooling '
        'Membrane">\n'
        '            <line x1="35" y1="188" x2="645" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <text x="44" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">Tensegrity Cable-Strut Dome: K_T = K_E + K_G(t_0) ≻ 0</text>\n'
        '            <path d="M 48 164 Q 198 46 348 164" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="2.4" stroke-dasharray="6,3"/>\n'
        '            <line x1="112" y1="96" x2="146" y2="152" stroke="var(--tp-prussian)" '
        'stroke-width="4"/>\n'
        '            <line x1="198" y1="72" x2="198" y2="138" stroke="var(--tp-prussian)" '
        'stroke-width="4"/>\n'
        '            <line x1="284" y1="96" x2="250" y2="152" stroke="var(--tp-prussian)" '
        'stroke-width="4"/>\n'
        '            <line x1="48" y1="164" x2="146" y2="152" stroke="var(--tp-minium)" '
        'stroke-width="1.6"/>\n'
        '            <line x1="146" y1="152" x2="198" y2="138" stroke="var(--tp-minium)" '
        'stroke-width="1.6"/>\n'
        '            <line x1="198" y1="138" x2="250" y2="152" stroke="var(--tp-minium)" '
        'stroke-width="1.6"/>\n'
        '            <line x1="250" y1="152" x2="348" y2="164" stroke="var(--tp-minium)" '
        'stroke-width="1.6"/>\n'
        '            <text x="52" y="178" font-size="9.5" fill="var(--tp-prussian)">Floating '
        'Compression Struts (Blue) in Continuous Cable Net (Red)</text>\n'
        '            <line x1="376" y1="24" x2="376" y2="192" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="394" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">8–13 μm Radiative Sky-Cooling Canopy (3 K Space)</text>\n'
        '            <path d="M 398 148 Q 515 112 632 148" fill="var(--tp-stone)" '
        'fill-opacity="0.35" stroke="var(--tp-verdigris)" stroke-width="3"/>\n'
        '            <line x1="445" y1="42" x2="465" y2="126" stroke="var(--tp-minium)" '
        'stroke-width="2"/>\n'
        '            <line x1="465" y1="126" x2="488" y2="42" stroke="var(--tp-minium)" '
        'stroke-width="2" stroke-dasharray="4,3"/>\n'
        '            <line x1="555" y1="124" x2="555" y2="38" stroke="var(--tp-verdigris)" '
        'stroke-width="2.8"/>\n'
        '            <text x="396" y="62" font-size="9" fill="var(--tp-minium)">97% Solar '
        'Reflected</text>\n'
        '            <text x="565" y="62" font-size="9" fill="var(--tp-verdigris)">8–13 μm LWIR to '
        '3 K Space</text>\n'
        '            <text x="396" y="178" font-size="9.5" fill="var(--tp-verdigris)">Model: q_net = 98.4 '
        'W/m² · ΔT ≈ −5.2 °C Surface</text>\n'
        '            <text x="44" y="206" font-size="10" fill="var(--tp-verdigris)">Design Study · Model Values · Not Measured</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a long-span floating-compression tensegrity '
        'cable-strut canopy clad in a luminous radiative sky-cooling membrane over a sunlit civic '
        'plaza would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.12-V (Imagining What It Would Look Like) · Artistic '
            'architectural visualization (synthesizing Folios A.04, A.08 & A.10) imagining a '
            '120-meter tensegrity dome whose photonic membrane beams urban heat through the 8–13 '
            'μm window into outer space.'}

DISPATCH = {'kicker': 'FRONTIER TENSEGRITY & RADIATIVE COOLING DISPATCH · PELLEGRINO SVD & NREL/ENERGYPLUS',
 'headline': 'A Design Study: Prestressed Tensegrity Cable Domes Clad in 8–13 μm Radiative-Cooling Membranes',
 'body': "This folio pairs Sergio Pellegrino and C. R. Calladine's equilibrium-matrix analysis of prestressed frameworks (DOI 10.1016/0020-7683(86)90014-4) with daytime radiative sky cooling as reported by Raman et al. (DOI 10.1038/nature13883). In its model the membrane gives 98.4 W/m² of cooling at air temperature and sits about 5.2 °C below the air for an assumed heat-exchange coefficient. Model values, not measurements; nothing was built or simulated."}

META_3D = ('Pellegrino Tensegrity Geometric Stiffness & 8–13 μm Sky-Cooling Surface',
 'X: Cable Prestress t_0 · Z: LWIR Emissivity ε_LWIR · Y: Tangent Stiffness & Net Cooling Flux')

ES_TRANSLATION = {'title_es': 'Domos de Tensegridad Cable-Puntal y Envolventes de Enfriamiento Radiativo: '
             'Subespacios Nulos de Pellegrino y Enfriamiento sin Energía',
 'subtitle_es': 'Sintetizando los Folios A.04, A.08 y A.10: un estudio de diseño sobre cómo la tensegridad de compresión flotante de Snelson y Fuller podría sostener una membrana de enfriamiento radiativo de 8–13 μm sobre una cubierta pública.',
 'why_es': 'Un domo de tensegridad funciona como una rueda de bicicleta: sus cables tensados sostienen barras que no se tocan entre sí, con poco peso (12 kg/m² es una cifra ilustrativa), mientras su membrana blanca pierde calor hacia el cielo frío por la ventana de 8–13 μm.',
 'bridge_es': 'Analogía: Donald Ingber propuso que las células usan un principio de tensegridad en su citoesqueleto (1993). El análisis de Pellegrino y Calladine permite revisar si el preesfuerzo da rigidez geométrica K_G(t_0) positiva sobre los modos de mecanismo.',
 'plain_es': 'En palabras sencillas, imaginen cómo funciona una rueda de bicicleta. Sus rayos son '
             'alambres delgados que se doblarían fácilmente con las manos, pero al estar tensados '
             'firmemente entre el centro y el rin, la rueda soporta el peso de una persona sin '
             'doblarse. Un domo de tensegridad aplica este mismo principio a escala monumental. En '
             'lugar de levantar techos pesadísimos de acero que absorben calor como hornos, los '
             'ingenieros suspenden postes de acero flotantes dentro de una red de cables de alta '
             'resistencia tensados con gatos hidráulicos, y la estructura resulta ligera. Si encima '
             'se coloca una membrana blanca especial que refleja casi toda la luz del sol y pierde '
             'calor hacia el cielo a través de la ventana infrarroja de la atmósfera, en el modelo de '
             'este folio la membrana queda unos grados por debajo de la temperatura del aire. Cuánto '
             'se enfriaría el aire de la plaza no se calcula aquí, y nada de esto es una indicación '
             'para proteger a las personas durante olas de calor.',
 'deep_es': 'A nivel matemático y estructural, los domos de tensegridad se analizan mediante la '
            'descomposición en valores singulares (SVD) de la matriz de equilibrio formulada por '
            'Sergio Pellegrino y C. R. Calladine en la Universidad de Cambridge. Esta herramienta '
            'identifica los estados de autoesfuerzo en el espacio nulo que permiten tensar los '
            'cables sin cargas externas, aportando una rigidez geométrica positiva que bloquea '
            'los mecanismos cinemáticos flojos. Para la cubierta, el folio supone una membrana que '
            'refleja el 97 por ciento de la luz solar, como la superficie fotónica de Raman et al. (2014), '
            'y emite en la ventana infrarroja de 8 a 13 micrómetros. Con 1,000 W/m² de sol supuestos, '
            'absorbe 30 W/m²; el modelo le asigna un intercambio radiativo neto con el cielo de 128.4 W/m², '
            'un valor ilustrativo fijo, de modo que el enfriamiento neto a temperatura del aire es de 98.4 W/m². '
            'Con un coeficiente combinado de intercambio de calor supuesto de unos 18.9 W/(m²·K), la superficie '
            'queda unos 5.2 °C por debajo del aire. Herramientas abiertas como COMPAS y EnergyPlus podrían '
            'servir para probar la idea, pero este folio no corrió ninguna. Son valores de modelo, no mediciones.'}
