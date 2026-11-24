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
 'subtitle': 'Synthesizing Folios A.04, A.08, and A.10: an explanatory model—not a structural '
             'design method—pairing floating-compression tensegrity frameworks from Snelson, '
             'Fuller, Calladine, and Pellegrino with an untested exterior 8–13 μm radiative '
             'sky-cooling calculation.',
 'date_published': '2026-11-07',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'TENSEGRITY & SKY-COOL · REV 1.1',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'A t = f · K_T = K_E + K_G(t_0) ≻ 0 · q_net(T_a) = q_sky_net(T_a) − (1 − R_solar) I_sun',
 'colophon': {'identifier': 'A.12 · Tensegrity Frameworks & Exterior 8–13 μm Sky-Cooling Pairing',
              'kernels': 'Pellegrino–Calladine Equilibrium Subspaces (s ≥ 1, m ≥ 0) · Prestress Stiffness '
                         'K_G(t_0) · Exterior 8–13 μm Arithmetic',
              'benchmarks': 'Fixed illustrative values: t_0 = 185 kN · q_net(T_a) = 98.4 W/m² ⇒ ΔT ≈ −5.2 °C (assumed 128.4 W/m², 18.9 W/(m²·K))',
              'bridge': 'Synthesizes A.04/A.08/A.10 · Analogy: cellular tensegrity hypothesis (Ingber 1993) ↔ prestressed cable nets'},
 'sliders': [{'label': 'Cable Prestress Self-Stress Level',
              'min': 40.0,
              'max': 320.0,
              'step': 5.0,
              'value': 185.0,
              'unit': ' kN'},
             {'label': '8–13 μm Atmospheric Window Emissivity',
              'min': 0.7,
              'max': 0.99,
              'step': 0.01,
              'value': 0.96,
              'unit': 'ε = '}],
 'steps': ['Stage 1 (Snelson–Fuller Floating Compression): Isolated compression struts sit '
           'suspended without touching one another inside a continuous tensioned cable network '
           '(Calladine 1978, DOI 10.1016/0020-7683(78)90052-5).',
           'Stage 2 (Pellegrino–Calladine Equilibrium Matrix Subspaces): Row-echelon subspace '
           'analysis of equilibrium matrix A (Pellegrino & Calladine 1986, DOI '
           '10.1016/0020-7683(86)90014-4) separates s = dim ker(A) self-stress states from m = '
           'dim ker(Aᵀ) mechanisms.',
           'Stage 3 (Prestress Stiffening & Safety Boundary): In an idealized pin-jointed model, '
           'cable prestress t_0 makes K_G(t_0) positive on mechanism modes. Explanation only, not '
           'a design method; no figure here (185 kN, +42.8 kN/m, 12.4 kg/m² for 120 m) may be '
           'used on a real structure.',
           'Stage 4 (Separate Sky-Cooling Arithmetic, Continuing A.08): Assuming R_solar = 0.97 '
           'under I_sun = 1,000 W/m² (after Raman et al. 2014, DOI 10.1038/nature13883) absorbs '
           '30 W/m². With fixed lumped sky exchange 128.4 W/m² at air temperature and assumed '
           'h_comb = 18.9 W/(m²·K), q_net(T_a) = 98.4 W/m² and ΔT ≈ −5.2 °C.'],
 'readouts': [{'label': 'Tangent Stiffness λ_min(K_E + K_G)',
               'value': '+42.8 kN/m (Fixed Illustrative Text, No Solver)'},
              {'label': 'Structural Steel Aerial Mass',
               'value': '12.4 kg/m² for 120 m Span (Fixed Illustrative Text)'},
              {'label': 'Net Daytime Sky-Cooling Flux',
               'value': '98.4 W/m² at Air Temp · ΔT ≈ −5.2 °C (Fixed Text)'},
              {'label': 'A.12 Model Boundary',
               'value': 'EXPLANATORY MODEL · NOT A DESIGN METHOD'}],
 'spec_plate': {'division': 'EXPLANATORY PAIRING · CSI 05 16 00 / 13 31 23 (NOT A DESIGN SPEC)',
                'title': 'Illustrative Pairing: Prestressed Cable-Strut Canopy & Exterior 8–13 μm '
                         'Sky-Cooling Coating',
                'body': 'Explanatory pairing only, not a design method or tested assembly: a '
                        'prestressed cable-strut framework paired conceptually with an exterior '
                        'radiative-cooling coating (Raman et al. 2014 tested seven HfO₂/SiO₂ '
                        'layers on a silver mirror atop silicon; Mandal et al. 2018 tested porous '
                        'P(VdF-HFP) polymer films, distinct from architectural PTFE fabric). None '
                        'of these untested numbers may be used on a real structure; no COMPAS or '
                        'NREL/EnergyPlus model ran.',
                'meta': 'Pellegrino & Calladine 1986 (DOI 10.1016/0020-7683(86)90014-4) · Raman et '
                        'al. 2014 (DOI 10.1038/nature13883) · Mandal et al. 2018 (DOI '
                        "10.1126/science.aat9513) · ASCE 19 sets none of this folio's values"},
 'sidenote_1': {'kicker': 'SIDENOTE A.12-A · CROSS-FIELD ANALOGY · BICYCLE WHEELS, LIVING CELLS & '
                          'SAHARAN SILVER ANTS',
                'body': 'A bicycle wheel resists load because its thin spokes start in tension '
                        'inside a rigid rim. Donald Ingber proposed that living cells use a '
                        'tensegrity-like balance in their cytoskeleton (1993, DOI '
                        '10.1242/jcs.104.3.613). Separately, Saharan silver ants carry triangular '
                        'hairs that raise solar reflection and mid-infrared thermal emission (Shi '
                        'et al. 2015, DOI 10.1126/science.aab3564). Pairing tensegrity mechanics '
                        'with radiative-cooling coatings here is an untested conceptual synthesis.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.12-B · OPEN-SOURCE TOOLS & THERMAL SAFETY BOUNDARY',
                'body': 'Open tools such as compas-dev/compas (for framework equilibrium) and '
                        'NREL/EnergyPlus (for building heat balance) could test parts of this '
                        'pairing, though this folio ran neither. A cooler roof membrane is not a '
                        'heat-safety measure, does not replace mechanical cooling, and gives no '
                        'guidance for protecting people during heatwaves.'},
 'skill': {'filename': 'tensegrity-nullspace-skycooling-SKILL.md',
           'name': 'tensegrity-nullspace-skycooling',
           'description': 'Explanatory companion for Pellegrino-Calladine tensegrity equilibrium '
                          'matrix subspaces (s = dim ker(A), m = dim ker(A^T)), geometric '
                          'prestress stiffening K_G(t_0), and exterior 8-13 um sky-cooling '
                          'arithmetic. Explanation only, not a design method; no folio number may '
                          'be used on a real structure.',
           'rules': ['Explanation only, not a structural or thermal design method: none of this '
                     "folio's untested numbers (185 kN, +42.8 kN/m, 12.4 kg/m^2, 98.4 W/m^2, -5.2 "
                     'C) may be used on a real structure; analyze the four subspaces of '
                     'equilibrium matrix A (Pellegrino & Calladine 1986, DOI '
                     '10.1016/0020-7683(86)90014-4).',
                     'In an idealized pin-jointed frame, check u^T * K_G(t_0) * u > 0 on mechanism '
                     'modes u in ker(A^T); this omits strut buckling, cable slackening, wind '
                     'flutter, ponding, and support movement.',
                     'Separate radiative arithmetic from statics: in q_net(T_a) = q_sky_net(T_a) - '
                     '(1 - R_solar) * I_sun, state every assumed constant (R_solar = 0.97, I_sun = '
                     '1,000 W/m^2, sky exchange 128.4 W/m^2, h_comb = 18.9 W/(m^2*K)) as model '
                     'values.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The opening scene of '
                           'Snelson and Fuller was dramatized and is replaced by a plain account, '
                           'and the 2026 chronology entry that presented this canopy as a built '
                           'project is withdrawn. Unsourced figures (85% less steel, 80% of '
                           'capacity spent on self-weight, a bicycle wheel carrying 100 times its '
                           'weight, a World Economic Forum ranking) and public-health and '
                           'zero-energy claims are removed; the 98.4 W/m² and −5.2 °C values now '
                           'state the assumptions they follow from, and the stiffness and mass '
                           'readouts are labeled illustrative.',
                'opus': 'Review: references checked by DOI in Crossref and Scite; central claims '
                        'checked against the Scite index; arithmetic recomputed from the stated '
                        'balance.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-07',
                'summary': 'REV 1.0 (Published 2026-11-07): Volume VI Architecture synthesis '
                           'monograph pairing Pellegrino & Calladine tensegrity matrix mechanics '
                           '(DOI 10.1016/0020-7683(86)90014-4) with Raman et al. daytime radiative '
                           'sky cooling (DOI 10.1038/nature13883).',
                'opus': 'Initial arithmetic check of the Calladine count b - 3j + 6 = s - m and '
                        'prestress stiffness relation. Earlier "verified" wording for the radiative '
                        'balance was withdrawn in REV 1.1 because no Planck calculation ran and the '
                        'cooling figures are model values.'}],
 'volume': 6,
 'volume_code': 'VOL. 06',
 'reading_time': '19 MIN READ',
 'word_count': '4,300 WORDS',
 'scite': {'doi': '10.1126/science.aat9513',
           'fetched_on': '2026-11-21',
           'citing_publications': 2339,
           'supporting': 24,
           'mentioning': 1653,
           'contrasting': 4,
           'retracted': False,
           'summary': 'Scite index entry [observed: Scite ML citation classification, accessed '
                      '2026-11-21] for Mandal et al., Hierarchically porous polymer coatings for '
                      'highly efficient passive daytime radiative cooling (DOI '
                      '10.1126/science.aat9513): 2,339 citing publications (distinct from statement '
                      'tallies: 24 supporting, 1,653 mentioning, 4 contrasting) and no retraction '
                      "notice. Those counts describe that paper, not this folio's untested pairing."}}

LONGFORM_DATA = {'reading_time': '19 MIN READ',
 'word_count': '4,300 WORDS',
 'parent_folios': ['A.04', 'A.08', 'A.10'],
 'lineage_mode': 'SYNTHESIS · Synthesizes A.04 Lightweight Exoskeletons, A.08 Radiative '
                 'Sky-Cooling & A.10 Deployable Skins',
 'scite': {'doi': '10.1126/science.aat9513',
           'fetched_on': '2026-11-21',
           'citing_publications': 2339,
           'supporting': 24,
           'mentioning': 1653,
           'contrasting': 4,
           'retracted': False,
           'summary': 'Scite index entry [observed: Scite ML citation classification, accessed '
                      '2026-11-21] for Mandal et al., Hierarchically porous polymer coatings for '
                      'highly efficient passive daytime radiative cooling (DOI '
                      '10.1126/science.aat9513): 2,339 citing publications (distinct from statement '
                      'tallies: 24 supporting, 1,653 mentioning, 4 contrasting) and no retraction '
                      "notice. Those counts describe that paper, not this folio's untested pairing."},
 'act1_title': 'Act I — Floating Struts in a Net of Cable, and a Skin That Radiates to the Sky',
 'act1_dropcap': 'In the late 1940s, the art student Kenneth Snelson met Buckminster Fuller at '
                 'Black Mountain College in North Carolina. Snelson built small sculptures in '
                 'which wooden struts hung apart from one another inside a taut web of cords. '
                 'Fuller called the principle tensegrity, blending tension and integrity to '
                 'describe isolated compression bars held inside continuous tension. On paper, '
                 'pin-jointed frames of that kind can look loose and unstable. At Cambridge in '
                 '1978 and 1986, Christopher Calladine and Sergio Pellegrino showed how to count '
                 'both their internal states of self-stress and their small motions. They also '
                 'showed when initial cable pull stiffens a frame that would otherwise sway. '
                 'This folio pairs that structural idea with a separate roof-coating calculation '
                 'as an explanation, not a design method, and none of its numbers may be used on '
                 'a real structure.',
 'act1_plain_bridge': 'In plain words, a long beam spanning an open hall bends under its own '
                      'weight. Its top edge squeezes while its bottom edge stretches. Thin steel '
                      'cables cannot resist squeezing at all, yet they carry heavy pull for their '
                      'weight. In a prestressed cable canopy, short compression struts push '
                      'outward against a continuous net of taut cables anchored at a perimeter '
                      'ring. Pulling the cables tight before weather loads arrive helps hold the '
                      'joint geometry steady in an idealized model. Separately, physics groups '
                      'have tested bright polymer and multilayer films that reflect sunlight while '
                      'shedding heat upward through a clear infrared band of the sky. Putting '
                      'such a film on a cable roof is an untested concept, and passive surface '
                      'cooling does not replace building ventilation or heatwave safety. This '
                      'folio is an explanation, not a design method, and none of its numbers may '
                      'be used on a real structure.',
 'act1_body': 'In 1978, Cambridge engineer C. R. Calladine (DOI 10.1016/0020-7683(78)90052-5) '
              "generalized James Clerk Maxwell's 1864 frame-counting rule by accounting for both "
              'states of self-stress and infinitesimal mechanisms, explaining why tensegrity '
              'frames stiffen when cables are pretensioned. Eight years later, Sergio Pellegrino '
              'and Calladine (1986, International Journal of Solids and Structures, DOI '
              '10.1016/0020-7683(86)90014-4) formulated matrix subspaces from the equilibrium '
              'operator to separate internal cable self-stress from kinematic mechanism modes and '
              'to test first-order geometric stiffening. Separately, Raman et al. (2014, DOI '
              '10.1038/nature13883) reported daytime sub-ambient radiative cooling with seven '
              'hafnia and silica layers on a silver mirror atop a silicon wafer, and Mandal et al. (2018, DOI '
              '10.1126/science.aat9513) reported porous P(VdF-HFP) polymer coatings under direct '
              "sunlight. The phrase 'zero-energy cooling' in this folio's title refers only to "
              'passive surface heat emission without a compressor in those material experiments, '
              'not to whole-building cooling. Open tools such as compas-dev/compas '
              '(https://github.com/compas-dev/compas) and NREL/EnergyPlus '
              '(https://github.com/NREL/EnergyPlus) are named for context; this folio ran no '
              'simulation. This folio is an explanation, not a design method, and none of its '
              'untested numbers may be used on a real structure.',
 'act1_stakes': 'Long-span roofs must carry their own dead weight alongside wind uplift, rain '
                'ponding, and asymmetric live loads. Tensioned cable-strut roofs carry tensile '
                'load paths along steel cables while confining compression to shorter struts, '
                'trading bending depth for high perimeter ring forces and anchorage demands. '
                'Meanwhile, sunlit roofs absorb solar irradiance and warm up. Combining a '
                'prestressed cable-strut canopy with a high-reflectance radiative-cooling skin is '
                'an untested research question that mixes two distinct published methods. This '
                'folio compares no measured steel weights, designs no real canopy, and claims no '
                'air-conditioning or outdoor plaza temperature reduction.',
 'pullquote': '"In an idealized pin-jointed model, cable prestress adds geometric stiffness on '
              'mechanism modes; in separate material tests, selective 8–13 μm emitters cool '
              'below ambient air. Pairing them here is an explanation, not a structural design."',
 'chronology': [('1948–1962',
                 "Kenneth Snelson's floating-strut sculptures and R. Buckminster Fuller's term "
                 "'tensegrity' (tensional integrity): isolated compression struts held inside "
                 'continuous tension nets.'),
                ('1978–1986',
                 'C. R. Calladine (DOI 10.1016/0020-7683(78)90052-5) and Sergio Pellegrino (DOI '
                 '10.1016/0020-7683(86)90014-4) formulate the generalized Maxwell count, matrix '
                 'subspaces, and geometric prestress stiffening.'),
                ('2014',
                 'Aaswath Raman and colleagues report daytime sub-ambient radiative cooling on a '
                 'multilayer photonic surface via the 8–13 μm atmospheric window (DOI '
                 '10.1038/nature13883).'),
                ('2018',
                 'Mandal et al. report porous P(VdF-HFP) polymer coatings cooling about 6 °C below '
                 'ambient under direct sunlight (DOI 10.1126/science.aat9513); pairing such a film '
                 'with a cable canopy here remains unbuilt and unsimulated.')],
 'act2_title': 'Act II — Cross-Field Intuition: Prestress Stiffening & Selective 8–13 μm '
               'Emission',
 'act2_analogy': 'Picture a spoked bicycle wheel. One loose wire spoke bends under two fingers, '
                 'yet tightening every spoke inside a rigid outer rim lets the wheel carry a '
                 'rider because downward load slightly relieves existing tension instead of '
                 'pushing wires into compression. Where the analogy stops: a bicycle wheel relies '
                 'on a stiff circular rim and predictable hub loads, whereas an architectural '
                 'cable-strut roof faces wind uplift, rain ponding, cable creep, strut buckling, '
                 'and support movement that spoke intuition does not check.',
 'act2_plain_primer': 'Below, the laboratory lists two conceptual parameters before any symbols. '
                      'The Cable Prestress Self-Stress Level slider represents initial tension '
                      'pulled into the cable net during assembly: in an idealized pin-jointed '
                      'model, higher initial tension raises geometric resistance to small '
                      'mechanism sway. The 8–13 μm Atmospheric Window Emissivity slider represents '
                      'how strongly an exposed top coating emits thermal infrared radiation through '
                      'the clear sky band. On this page, dragging either slider updates only its '
                      'displayed label and generic visual wave preview; all four readout cards '
                      '(including +42.8 kN/m, 12.4 kg/m² for a 120 m span, 98.4 W/m², and −5.2 °C) '
                      'stay fixed illustrative text and no solver runs.',
 'distill_diagram': {'analogy_title': 'Spoked Bicycle Wheel (Analogy)',
                     'analogy_sub': 'Pretensioned spokes carry load by relieving tension inside a '
                                    'stiff rim',
                     'force_a_title': 'Cable Prestress Self-Stress Level',
                     'force_a_sub': 'Conceptual cable pretension; slider updates label only',
                     'force_b_title': '8–13 μm Atmospheric Window Emissivity',
                     'force_b_sub': 'Conceptual infrared emission; slider updates label only',
                     'threshold_title': 'Idealized Prestress Stiffening: K_T = K_E + K_G(t_0) ≻ 0',
                     'threshold_pass': 'Positive model stiffness on mechanism modes; fixed −5.2 °C '
                                       'surface example',
                     'threshold_fail': 'Slack cables lose geometric stiffness; real buckling/wind '
                                       'not modeled'},
 'act2_intuition': "Calladine (1978, DOI 10.1016/0020-7683(78)90052-5) extended Maxwell's 1864 "
                   'bar-and-joint count to three dimensions as b − 3j + 6 = s − m, linking bar '
                   'count b and joint count j to self-stress count s and infinitesimal mechanism '
                   'count m. In the matrix formulation of Pellegrino and Calladine (1986, DOI '
                   '10.1016/0020-7683(86)90014-4), the equilibrium matrix A maps internal member '
                   'force vector t to external nodal load vector f through A t = f, and '
                   'row-echelon reduction extracts its fundamental subspaces: the nullspace '
                   'ker(A) of dimension s (internal tension states t_0 in equilibrium at zero '
                   'external load) and the left nullspace ker(Aᵀ) of dimension m (inextensional '
                   'mechanism displacements u where linear elastic stiffness vanishes, K_E u = 0; '
                   'later tensegrity software can compute the same bases via singular value '
                   'decomposition). Adding initial cable prestress t_0 introduces geometric '
                   'stiffness matrix K_G(t_0); when quadratic form uᵀ K_G(t_0) u > 0 holds for '
                   'every mechanism mode u, total tangent stiffness K_T = K_E + K_G(t_0) is '
                   'positive-definite in the idealized model. The readout +42.8 kN/m at t_0 = '
                   '185 kN is fixed illustrative text, not the eigenvalue of a solved dome matrix.',
 'act2_deepening': 'Separately from statics, q_net(T_a) = q_sky_net(T_a) − (1 − R_solar) I_sun '
                   'mixes published coating data with assumed constants. Citing R_solar = 0.97 from '
                   'Raman et al. (2014, DOI 10.1038/nature13883, seven HfO₂/SiO₂ layers on a '
                   'silver mirror atop silicon) under assumed I_sun = 1,000 W/m² absorbs 30 W/m². '
                   'Assigning fixed illustrative sky exchange q_sky_net(T_a) = 128.4 W/m² at air '
                   'temperature (not a Planck integral, and omitting ground radiation) gives '
                   'q_net(T_a) = 98.4 W/m²; dividing by assumed h_comb = 18.9 W/(m²·K) estimates '
                   'ΔT ≈ −5.2 °C. Raman et al. (2014) measured 4.9 °C below ambient and Mandal et '
                   'al. (2018, DOI 10.1126/science.aat9513) measured about 6 °C on porous '
                   'P(VdF-HFP) films. None of these figures may be used on a real structure.',
 'walkthrough': ['Experiment 1 (Cable Prestress Self-Stress Level): Drag Cable Prestress '
                 'Self-Stress Level from 40 to 320 kN. On this page the slider updates only its '
                 'displayed kN label and generic SVG wave preview; +42.8 kN/m and 12.4 kg/m² stay '
                 'fixed illustrative text with no matrix solver.',
                 'Experiment 2 (8–13 μm Atmospheric Window Emissivity): Drag 8–13 μm Atmospheric '
                 'Window Emissivity from 0.70 to 0.99. Only the ε label and SVG preview update; '
                 '98.4 W/m² and −5.2 °C remain fixed text from Stage 4.',
                 'Experiment 3 (4-Stage Stepper & 3D Preview): Click Stage buttons 1 through 4 '
                 'above the plate to review Snelson–Fuller tensegrity, Pellegrino–Calladine '
                 'subspaces, safety boundaries, and the sky-cooling arithmetic, or orbit the 3D '
                 'preview.'],
 'act4_title': 'Act IV — Open Research Questions: Open-Source Form-Finding & Weathering Limits',
 'act4_human_ai': 'Open tools such as compas-dev/compas (https://github.com/compas-dev/compas) and '
                  'NREL/EnergyPlus (https://github.com/NREL/EnergyPlus) let researchers study '
                  'equilibrium matrices and envelope heat balances separately. Pairing prestressed '
                  'cable nets with porous radiative-cooling coatings (Mandal et al. 2018, DOI '
                  '10.1126/science.aat9513) remains untested: this folio ran neither tool, and '
                  '−5.2 °C describes a modeled top surface, not cooler air in a plaza below.',
 'act4_deepening': 'Any real prototype would require checking nonlinear cable slackening, strut '
                   'buckling, wind flutter, rain ponding, ring anchorage, and upward thermal '
                   'radiation from warm pavement. While Raman et al. (2014, DOI '
                   '10.1038/nature13883) and Mandal et al. (2018, DOI 10.1126/science.aat9513) '
                   'tested photonic and porous polymer coolers, how any radiative coating holds up '
                   'under ultraviolet light, tensile membrane strain, humidity, and airborne dust '
                   'on a flexible cable roof remains open. No number here may be used in design.',
 'cf_bridge': 'Explanatory Architecture Monograph (A.04 + A.08 + A.10 → A.12): Introduces '
              'Pellegrino–Calladine equilibrium subspaces alongside a separate exterior '
              'sky-cooling arithmetic example; explanation only, not a structural design method.',
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
             'Ingber, D. E. (1993). Cellular tensegrity: defining new rules of biological design '
             'that govern the cytoskeleton. Journal of Cell Science, 104(3), 613–627. DOI: '
             '10.1242/jcs.104.3.613.',
             'Shi, N. N., Tsai, C.-C., Camino, F., Bernard, G. D., Yu, N., & Wehner, R. (2015). '
             'Keeping cool: Enhanced optical reflection and radiative heat dissipation in Saharan '
             'silver ants. Science, 349(6245), 298–301. DOI: 10.1126/science.aab3564.',
             'Open-Source Context: NREL/EnergyPlus (https://github.com/NREL/EnergyPlus) & '
             'compas-dev/compas (https://github.com/compas-dev/compas). Named as tools a reader '
             'could inspect; neither was run for this folio.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Tensegrity '
        'Floating-Compression Cable Framework and Separate 8-13 Micrometer Exterior Sky-Cooling '
        'Arithmetic Schematic">\n'
        '            <line x1="35" y1="188" x2="645" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <text x="44" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">Idealized Tensegrity Frame: K_T = K_E + K_G(t_0) ≻ 0</text>\n'
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
        '            <text x="52" y="178" font-size="9.5" fill="var(--tp-prussian)">Isolated '
        'Compression Struts (Blue) in Continuous Cable Net (Red)</text>\n'
        '            <line x1="376" y1="24" x2="376" y2="192" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="394" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">Separate 8–13 μm Exterior Sky-Cooling Arithmetic</text>\n'
        '            <path d="M 398 148 Q 515 112 632 148" fill="var(--tp-stone)" '
        'fill-opacity="0.35" stroke="var(--tp-verdigris)" stroke-width="3"/>\n'
        '            <line x1="445" y1="42" x2="465" y2="126" stroke="var(--tp-minium)" '
        'stroke-width="2"/>\n'
        '            <line x1="465" y1="126" x2="488" y2="42" stroke="var(--tp-minium)" '
        'stroke-width="2" stroke-dasharray="4,3"/>\n'
        '            <line x1="555" y1="124" x2="555" y2="38" stroke="var(--tp-verdigris)" '
        'stroke-width="2.8"/>\n'
        '            <text x="396" y="62" font-size="9" fill="var(--tp-minium)">Assumed R_solar = '
        '0.97</text>\n'
        '            <text x="548" y="62" font-size="9" fill="var(--tp-verdigris)">8–13 μm '
        'Window</text>\n'
        '            <text x="396" y="178" font-size="9.5" fill="var(--tp-verdigris)">Fixed Text: '
        'q_net(T_a) = 98.4 W/m² · ΔT ≈ −5.2 °C</text>\n'
        '            <text x="44" y="206" font-size="10" fill="var(--tp-verdigris)">Explanatory '
        'Model · Fixed Values · Not a Design Method</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a long-span floating-compression tensegrity '
        'cable-strut canopy paired with a white radiative-cooling roof membrane over a civic '
        'plaza would look like (artistic impression, not a measured structure or specification)',
 'caption': 'Conceptual Vision Plate A.12-V (Imagining What It Would Look Like) · Artistic '
            'architectural visualization (synthesizing Folios A.04, A.08 & A.10) imagining a '
            '120-meter cable-strut canopy paired with an exterior 8–13 μm radiative-cooling '
            'membrane.'}

DISPATCH = {'kicker': 'FRONTIER TENSEGRITY & RADIATIVE COOLING DISPATCH · A.12 · REV 1.1',
 'headline': 'Explanatory Model: Pellegrino–Calladine Tensegrity Frameworks & Exterior 8–13 μm '
             'Sky-Cooling Coatings',
 'body': "This folio explains Sergio Pellegrino and C. R. Calladine's equilibrium-matrix "
         'subspaces for prestressed frameworks (DOI 10.1016/0020-7683(86)90014-4) alongside a '
         'separate exterior roof-cooling arithmetic example citing Raman et al. (DOI '
         '10.1038/nature13883) and Mandal et al. (DOI 10.1126/science.aat9513). Under stated '
         'assumptions (128.4 W/m² sky exchange at air temperature, h_comb = 18.9 W/(m²·K)), the '
         'example gives 98.4 W/m² and about −5.2 °C on the membrane surface. Explanatory model '
         'only, not a design method; nothing was built or simulated.'}

META_3D = ('Pellegrino Tensegrity Geometric Stiffness & 8–13 μm Sky-Cooling Surface',
 'X: Cable Prestress t_0 · Z: LWIR Emissivity ε_LWIR · Y: Conceptual Stiffness & Cooling Surface')

ES_TRANSLATION = {'title_es': 'Domos de Tensegridad Cable-Puntal y Envolventes de Enfriamiento Radiativo: '
             'Subespacios Nulos de Pellegrino y Enfriamiento sin Energía',
 'subtitle_es': 'Sintetizando los Folios A.04, A.08 y A.10: un modelo explicativo —no un método '
                'de diseño estructural— que combina marcos de tensegridad con un cálculo '
                'hipotético de enfriamiento radiativo exterior de 8–13 μm.',
 'why_es': 'Como una rueda de bicicleta cuyos rayos tensados sostienen carga dentro de un rin '
           'rígido, una red pretensada mantiene puntales aislados en equilibrio en el modelo '
           'idealizado. Dónde termina la analogía: una cubierta real enfrenta viento, '
           'encharcamiento, pandeo y fluencia que una rueda no representa.',
 'bridge_es': 'Modelo explicativo (no un método de diseño): en esta página los dos deslizadores '
              'solo actualizan sus etiquetas y las cuatro tarjetas muestran texto ilustrativo fijo.',
 'plain_es': 'En palabras sencillas, una viga larga sobre un salón amplio se flexiona bajo su '
             'propio peso. Su borde superior se comprime y el inferior se estira. Los cables '
             'delgados de acero no resisten compresión, pero soportan gran tracción con poco '
             'peso. En una cubierta pretensada de cables y puntales, barras cortas empujan '
             'contra una red continua de cables anclada en un anillo perimetral. Tensar los '
             'cables desde el montaje aporta rigidez geométrica en el modelo idealizado. Aparte, '
             'grupos de física han probado películas poliméricas y multicapa que reflejan el sol '
             'y emiten calor por la banda infrarroja del cielo. Unir esa película con una red de '
             'cables es una idea no probada, y enfriar una superficie no sustituye la '
             'ventilación ni protege durante olas de calor. Este folio es una explicación, no un '
             'método de diseño, y ninguno de sus números puede usarse en una estructura real.',
 'deep_es': 'En la parte estructural, C. R. Calladine (1978, DOI 10.1016/0020-7683(78)90052-5) y '
            'Sergio Pellegrino con Calladine (1986, DOI 10.1016/0020-7683(86)90014-4) obtuvieron '
            'mediante reducción por renglones los subespacios fundamentales de la matriz de '
            'equilibrio para separar autoesfuerzos t_0 y mecanismos. En esta página los controles '
            'solo actualizan etiquetas y las cuatro lecturas (+42.8 kN/m, 12.4 kg/m² para 120 m, '
            '98.4 W/m² y −5.2 °C) son texto fijo sin solucionador. Citando a Raman et al. (2014, '
            'DOI 10.1038/nature13883, siete capas de HfO₂/SiO₂ sobre espejo de plata) y Mandal '
            'et al. (2018, DOI 10.1126/science.aat9513), con R_solar = 0.97 bajo 1,000 W/m² de '
            'sol, intercambio fijo de 128.4 W/m² y h_comb supuesto de 18.9 W/(m²·K), el ejemplo '
            'da 98.4 W/m² y −5.2 °C; COMPAS y EnergyPlus no se ejecutaron aquí.'}
