#!/usr/bin/env python3
"""Folio E.05 (ENGINEERING): Terzaghi Soil Mechanics, CFA Augercast Deep Foundation Piling & Excess Pore Pressure."""
from __future__ import annotations

SLUG = 'e05'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.05',
 'slug': 'e05',
 'pillar': 'engineering',
 'category_code': 'E',
 'title': 'Terzaghi Soil Mechanics, CFA Augercast Deep Foundation Piling & Excess Pore Pressure',
 'subtitle': "How Karl Terzaghi's effective stress principle σ'_v = σ_v − u, hydrodynamic "
             'consolidation ∂u/∂t = c_v ∂²u/∂z², and Continuous Flight Auger (CFA) deep '
             'foundations relate to structural settlement and excess pore pressure.',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.2',
 'status_badge': 'CIVIL & GEOTECHNICAL · REV 1.2',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': "∂u/∂t = c_v ∂²u/∂z² · Q_ult = Q_skin + Q_toe · r_u = Δu / σ'_{v0}",
 'colophon': {'identifier': 'E.05 · Geotechnical & Deep Foundations · CSI 31 63 23',
              'kernels': "σ'_v = σ_v − u · ∂u/∂t = c_v ∂²u/∂z² · CFA Bearing",
              'benchmarks': 'Model values at defaults: T_v = 0.320 · U_avg = 63.2% (H_dr = 6 m, t = '
                            '3.6 yr)',
              'bridge': 'Terzaghi Consolidation ↔ Gel-on-Brush Airway Model (an analogy)'},
 'sliders': [{'label': 'Foundation Surcharge Load (Δq)',
              'min': 40.0,
              'max': 260.0,
              'step': 5.0,
              'value': 120.0,
              'unit': ' kPa'},
             {'label': 'Consolidation Coefficient (c_v)',
              'min': 0.5,
              'max': 8.0,
              'step': 0.1,
              'value': 3.2,
              'unit': ' m²/yr'}],
 'steps': ['Stage 1 (Undrained Surcharge Application, t = 0⁺): Structural surcharge Δq = 120 kPa '
           'transfers initially 100% into excess pore-water pressure Δu(z, 0) = Δq.',
           'Stage 2 (Terzaghi Hydrodynamic Dissipation): Pore water drains toward permeable sand '
           'boundaries via ∂u/∂t = c_v ∂²u/∂z². The page assumes a drainage path H_dr = 6 m and '
           'an elapsed time t = 3.6 years, so T_v = 3.2 × 3.6 / 6² = 0.320 and U_avg = 1 − '
           '(8/π²) exp(−π² T_v / 4) = 63.2%.',
           'Stage 3 (CFA Augercast Shaft + Toe Mobilization): A 750 mm diameter, 24 m deep CFA '
           'pile carries load by shaft friction and toe bearing. The page uses fixed '
           'illustrative capacities of 2,380 kN (shaft) and 1,980 kN (toe), and the folio assumes '
           'that residual pore pressure reduces them by factors of 0.65 r_u (shaft) and 0.35 r_u '
           '(toe): Q_ult = 2,380 × (1 − 0.65 r_u) + 1,980 × (1 − 0.35 r_u). With r_u = 0.221 '
           '(Stage 4, unrounded) this gives Q_ult = 3,865 kN against an assumed design load of '
           '1,400 kN + 1.25 kN per kPa of surcharge (FS = 2.49). The 0.65 and 0.35 factors are '
           "this folio's own assumptions, not code values.",
           "Stage 4 (Pore-Pressure Ratio, r_u = Δu / σ'_{v0}): The residual excess pore pressure "
           "after consolidation, Δu = Δq (1 − U_avg) = 44.2 kPa, over an assumed σ'_{v0} = 200 kPa "
           "gives r_u = 0.22. This is a consolidation ratio, not a seismic liquefaction analysis; "
           'r_u = 1 would mean zero effective stress, and the page flags r_u ≥ 0.70 as its own '
           'screening choice.'],
 'readouts': [{'label': 'Average Consolidation U_avg', 'value': '63.2% (S_c = 42.2 mm, model)'},
              {'label': 'CFA Ultimate Pile Capacity', 'value': '3,865 kN (FS = 2.49, model)'},
              {'label': 'Pore-Pressure Ratio r_u', 'value': "0.22 (σ'_v = 156 kPa)"},
              {'label': 'Geotechnical Verdict', 'value': 'MODEL FS ≥ 2.0 · ILLUSTRATIVE, NOT A SITE DESIGN'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 31 63 23 / FHWA GEC-8',
                'title': 'Continuous Flight Auger (CFA) Augercast Deep Foundation Piles',
                'body': 'Illustrative design sketch, not a project specification: CFA piles (D = '
                        "750 mm, L = 24 m, f'_c = 40 MPa grout) installed with automated "
                        'monitoring of depth, torque and pumped grout volume. The grout-volume '
                        'target of more than 115% of theoretical volume is a design assumption '
                        'of this page; check the current FHWA guidance for the actual criteria.',
                'meta': 'Design sketch · FHWA GEC No. 8 is the FHWA design and construction '
                        'manual for CFA piles; no site data stand behind this plate'},
 'sidenote_1': {'kicker': 'SIDENOTE E.05-A · TERZAGHI EFFECTIVE STRESS & TIME FACTOR T_v',
                'body': 'Consolidation settlement depends on the dimensionless time factor T_v = '
                        'c_v t / H_dr². A clay layer drained at top and bottom (H_dr = H/2) '
                        'reaches a given degree of consolidation 4× faster than the same layer '
                        'drained on one side only.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.05-B · SPECIFICATION PLATE · CSI 31 63 23 (CFA PILES)',
                'body': "Design sketch of continuous flight auger (augercast) piles (D = 750 mm, L "
                        "= 24 m, f'_c = 40 MPa grout, design target of more than 115% "
                        'theoretical grout volume) with automated rig monitoring.'},
 'skill': {'filename': 'terzaghi-cfa-geotechnical-piling-SKILL.md',
           'name': 'terzaghi-cfa-geotechnical-piling',
           'description': 'AI-agnostic civil geotechnical engineering skill for Terzaghi 1D '
                          "consolidation (du/dt = c_v d^2u/dz^2), effective stress sigma'_v = "
                          'sigma_v - u, CFA deep foundation capacity, and excess pore-pressure r_u '
                          'screening.',
           'rules': ['Compute Terzaghi dimensionless time factor T_v = (c_v * t) / H_dr^2 and '
                     'degree of consolidation U_avg = sqrt(4*T_v/pi) for T_v <= 0.286 or U_avg = 1 '
                     '- (8/pi^2)*exp(-pi^2 * T_v / 4) for T_v > 0.286.',
                     'Evaluate axial CFA pile ultimate capacity Q_ult = Q_skin + Q_toe using '
                     "effective overburden stress sigma'_v(z) = sigma_v(z) - u(z); this folio assumes the "
                     'shaft term is scaled by (1 - 0.65 r_u) and the toe term by (1 - 0.35 r_u), '
                     'its own illustrative factors.',
                     'Flag the design for review whenever excess pore-pressure ratio r_u = '
                     "Delta_u / sigma'_v0 >= 0.70 or factor of safety FS = Q_ult / P_design < 2.0 "
                     "(both are this folio's screening choices, not code values); a real "
                     'liquefaction assessment needs a site-specific cyclic analysis.']},
 'revisions': [{'edition': 'REV 1.2',
                'date': '2026-11-14',
                'summary': 'REV 1.2 (Redated 2026-11-14): Grounding revision. The claim that '
                           "Terzaghi's equation is \"mathematically identical\" to airway "
                           'physics, the 3.5 kPa periciliary figure and the treatment language '
                           'were withdrawn; the gel-on-brush link to Button et al. (2012) is now '
                           'an analogy with their own figures. The source entry for DOI '
                           '10.1061/(ASCE)GT.1943-5606.0000073 was corrected to Gavin, Cadogan & '
                           'Casey, the readouts were recomputed from the page model (U_avg = '
                           '63.2%, Q_ult = 3,865 kN, r_u = 0.22), and the invented 1925 workshop '
                           'scene and an unsourced 4.2 mm settlement result were removed. A '
                           'later review corrected the page further: the pore-pressure ratio r_u '
                           'is now described as a consolidation quantity, not a liquefaction '
                           'result, the 0.65 and 0.35 capacity-reduction factors behind '
                           '3,865 kN are stated, and unsourced liquefaction and drainage claims '
                           'were removed.',
                'opus': 'Review: every DOI in the folio was checked in Crossref and the Scite '
                        'index on 2026-11-14, and the repository names with the GitHub API. No '
                        'finite-element analysis or site data stand behind this folio; its '
                        'numbers come from the closed-form model and the stated assumptions.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-02',
                'summary': 'REV 1.1 (Redated 2026-11-02): Verified Karl Terzaghi effective stress '
                           "(sigma'_v = sigma_v - u) & 1D consolidation (du/dt = c_v d^2u/dz^2), "
                           'CFA deep foundation shaft + toe bearing (Q_ult = Q_skin + Q_toe), and '
                           "Seed-Idriss liquefaction surcharge (r_u = Delta_u / sigma'_v0, CSI 31 "
                           '63 23, FHWA GEC-8).',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): reviewed '
                        'the consolidation formulas. The word "Verified" in this note and the note '
                        'below is withdrawn in REV 1.2; the earlier readouts (64.2%, 4,180 kN, '
                        'r_u = 0.28) did not follow from the page model.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-01',
                'summary': 'REV 1.0 (Published 2026-11-01): Initial 5-Act civil geotechnical '
                           'monograph on Terzaghi effective stress consolidation, CSI 31 63 23 CFA '
                           'deep piling, and Seed-Idriss liquefaction surcharge.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Fourier series consolidation isochrones, T_v = c_v t / H_dr² scaling, and '
                        'effective-stress CFA shaft capacity.'}],
 'volume': 3,
 'volume_code': 'VOL. 03',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1061/(ASCE)GT.1943-5606.0000073',
           'fetched_on': '2026-11-08',
           'citing_publications': 39,
           'supporting': 0,
           'mentioning': 3,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Gavin, Cadogan & Casey 2009, Shaft Capacity of '
                      'Continuous Flight Auger Piles in Sand (DOI '
                      '10.1061/(ASCE)GT.1943-5606.0000073), as recorded 2026-11-08: 39 citing '
                      'publications (0 supporting, 3 mentioning, 0 contrasting) and no '
                      'retraction notice. These counts describe that one paper, not this '
                      'folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1061/(ASCE)GT.1943-5606.0000073',
           'fetched_on': '2026-11-08',
           'citing_publications': 39,
           'supporting': 0,
           'mentioning': 3,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Gavin, Cadogan & Casey 2009, Shaft Capacity of '
                      'Continuous Flight Auger Piles in Sand (DOI '
                      '10.1061/(ASCE)GT.1943-5606.0000073), as recorded 2026-11-08: 39 citing '
                      'publications (0 supporting, 3 mentioning, 0 contrasting) and no '
                      'retraction notice. These counts describe that one paper, not this '
                      'folio.'},
 'act1_title': "Act I — Karl Terzaghi's Effective Stress Revolution and Continuous Flight Auger "
               '(CFA) Deep Piling',
 'act1_dropcap': 'In 1925 the Austrian engineer Karl Terzaghi, then teaching at Robert College '
                 'in Constantinople (Istanbul), published Erdbaumechanik, the book usually taken '
                 'as the start of modern soil mechanics. Builders had long seen structures on '
                 'clay settle unevenly, sometimes for years. Terzaghi treated saturated ground as '
                 'two phases, mineral grains and pore water, and set out two ideas that are still '
                 'taught: the principle of effective stress, which says the grains carry only the '
                 'total stress minus the pore-water pressure, and a theory of one-dimensional '
                 'consolidation, in which a new load is first carried by the water and passes to '
                 'the grains only as water drains away.',
 'act1_plain_bridge': 'Think of stepping your foot onto a waterlogged kitchen sponge resting on a '
                      'kitchen counter. The instant your shoe presses down, you do not compress '
                      'the foam fibers right away. Instead, you pressurize the water trapped '
                      'inside the tiny pores, sending water squirting out across the sides. Only '
                      'after that trapped water drains away do the rubbery sponge fibers finally '
                      'compress and flatten out. Saturated soil beneath a skyscraper acts in the '
                      'exact same manner. When a heavy concrete tower is constructed, the trapped '
                      'groundwater initially carries the weight. Over months and years, water '
                      'slowly seeps out through tiny underground passages, allowing the sand and '
                      'clay grains to lock together and support the building. Earthquake shaking of '
                      'loose wet sand is a different problem: water pressure can rise and push '
                      'the grains apart, which engineers assess separately. Deep concrete piles '
                      'that carry load to firmer layers are one tool for that, not a guarantee.',
 'act1_body': 'Because water is virtually incompressible, any sudden foundation surcharge applied '
              'to saturated, low-permeability clay is initially borne entirely by excess '
              "pore-water pressure. Only as pore water slowly drains according to Terzaghi's "
              'one-dimensional diffusion equation does load transfer to the mineral skeleton, '
              'generating primary consolidation settlement. To bypass soft, compressible alluvial '
              'soils and avoid decades of destructive differential settlement, modern heavy civil '
              'projects utilize Continuous Flight Auger deep foundation piles. A hollow-stem auger '
              'drills into competent load-bearing strata at depth, pumping high-strength cement '
              'grout under pressure as the tooling is withdrawn. This continuous installation '
              'mobilizes both cylindrical shaft friction and toe bearing capacity without casing '
              'vibration. Field tests show how shaft resistance develops on CFA piles in sand '
              '(Gavin, Cadogan & Casey 2009, DOI 10.1061/(ASCE)GT.1943-5606.0000073). '
              'Separately, prefabricated vertical drains can be installed in soft clay to shorten '
              'drainage paths so consolidation happens faster; how much faster depends on drain '
              'spacing and soil properties, and no design can guarantee serviceability without '
              'site investigation and monitoring.',
 'act1_stakes': 'When geotechnical engineers ignore excess pore-water pressure and assume '
                'instantaneous soil settlement, the consequences for civil infrastructure are '
                'severe. In heavy building construction, failing to account for low consolidation '
                'rates causes structures to experience severe differential settlement decades '
                'after ribbon-cutting ceremonies, cracking structural load-bearing walls, warping '
                'elevator shafts, and rupturing buried utility mains. Under dynamic cyclic '
                'loading, such as earthquake ground motions, pore pressure can also build up in '
                'loose saturated sand. That is a different process from consolidation under a '
                'steady surcharge, and it needs its own site-specific assessment. Engineers reduce these risks with site '
                'investigation, liquefaction assessment, ground improvement and, where suitable, '
                'deep foundations that carry load down into denser layers below the liquefiable '
                'zone. Deep piles in liquefiable ground still need design for lost shaft support '
                'and downdrag; they are one tool, not a guarantee.',
 'pullquote': '"Soil grains do not know the total weight of the skyscraper above them; they feel '
              "only the Terzaghi effective stress sigma'_v = sigma_v - u remaining after "
              'pore-water pressure is subtracted."',
 'chronology': [('1925',
                 'Karl Terzaghi publishes Erdbaumechanik, establishing the principle of effective '
                 "stress sigma'_v = sigma_v - u and 1D consolidation."),
                ('1948',
                 'Terzaghi & Ralph Peck publish Soil Mechanics in Engineering Practice, a '
                 'standard text on bearing capacity and settlement design.'),
                ('1971',
                 'H. Bolton Seed & I. M. Idriss publish their simplified procedure for evaluating '
                 'soil liquefaction potential (DOI 10.1061/JSFEAQ.0001662).'),
                ('2007',
                 'FHWA Geotechnical Engineering Circular No. 8 (Brown et al.) gives design and '
                 'construction guidance for Continuous Flight Auger (CFA) piles.')],
 'act2_title': 'Act II — How It Actually Works: Pore-Water Isochrones, CFA Pile Bearing & '
               'Excess Pore-Pressure Ratio r_u',
 'act2_analogy': 'Stepping onto a soaking wet kitchen sponge first pressurizes the water trapped '
                 'in its pores; the foam skeleton only compresses as that water escapes. '
                 'Terzaghi consolidation is the slow squeezing out of that trapped water. The '
                 'ratio r_u on this page tracks how much of the load the water is still '
                 'carrying: the higher it is, the lower the effective stress between the grains.',
 'act2_plain_primer': 'To see how geotechnical engineers design stable foundations, our simulation '
                      'gives you two fundamental dials that control ground behavior. The first '
                      'dial is the Foundation Surcharge Load, which represents the immense weight '
                      'of the building or bridge pushing down on the earth. Increasing this dial '
                      'places greater stress on the subterranean soil, demanding that both the '
                      'trapped water and the mineral grains carry more burden. The second dial is '
                      'the Consolidation Coefficient, which dictates how quickly water can squeeze '
                      'out through microscopic soil pores. If you set this drainage dial high, '
                      'trapped water escapes faster and the ground settles sooner. If you turn it '
                      'down, as in a dense, slow-draining clay, the water remains under pressure '
                      'for years. The dial runs from 0.5 to 8 m²/yr, a clay range; a clean sand '
                      'would drain much faster than anything on this scale. Tuning both knobs '
                      'shows how excess pore pressure builds up under heavy loading, and why '
                      'engineers sometimes turn to deep foundation piles when surface soils drain '
                      'too slowly.',
 'distill_diagram': {'analogy_title': 'Waterlogged Sponge & Excess Pore Pressure',
                     'analogy_sub': 'Trapped water bears load until slow pore drainage settles '
                                    'skeleton.',
                     'force_a_title': 'Foundation Surcharge (Δq)',
                     'force_a_sub': 'Total downward building weight pressurizing soil pore water.',
                     'force_b_title': 'Consolidation Speed (c_v)',
                     'force_b_sub': 'Rate of hydrodynamic pore-water dissipation through strata.',
                     'threshold_title': "Excess Pore-Pressure Ratio (r_u = Δu / σ'_v0)",
                     'threshold_pass': 'Low r_u: Effective stress stays positive, grains and '
                                       'piles carry the load.',
                     'threshold_fail': 'High r_u: Excess pore pressure carries more of the load, '
                                       'effective stress falls.'},
 'act2_intuition': 'Under an applied surface surcharge Delta_q, the dimensionless time factor T_v '
                   '= (c_v * t) / H_dr^2 dictates the transient degree of consolidation: for T_v '
                   '<= 0.286, average settlement follows U_avg = sqrt(4 * T_v / pi). '
                   'Simultaneously, a Continuous Flight Auger pile of diameter D = 0.75 m and '
                   'length L = 24.0 m transfers axial load through combined shaft skin friction '
                   "Q_skin = integral(beta * sigma'_v(z) * pi * D dz) and end-bearing toe "
                   'resistance Q_toe = q_b * A_toe. However, if seismic shaking or rapid undrained '
                   'loading raises excess pore-water pressure Delta_u such that the pore-pressure '
                   "ratio r_u = Delta_u / sigma'_v0 approaches unity, effective stress falls "
                   'toward zero. Where effective stress is zero, intergranular friction '
                   'vanishes and that layer stops contributing shaft support (a real '
                   'liquefaction assessment needs a site-specific cyclic analysis, which this '
                   'page does not do). '
                   "A coupled analysis based on Biot's poroelasticity, which a reader could build "
                   'with a finite-element library such as FEniCS/dolfinx '
                   '(https://github.com/FEniCS/dolfinx; one of its method papers: DOI '
                   '10.1145/3524456), would show how axial load sheds down the shaft into deeper '
                   'bearing layers when upper layers soften. No such analysis was run for this '
                   'folio. On this page, settlement is a simple scaling (66.7 mm at full '
                   'consolidation under 120 kPa, times U_avg) and capacity uses fixed '
                   'illustrative values.',
 'act2_deepening': 'The micro-mechanical interplay between pore-water dissipation and soil '
                   'skeleton stiffness governs the nonlinear rate of consolidation settlement. In '
                   'cohesive clay formations, hydraulic permeability is not constant; as excess '
                   'water drains, the void ratio decreases, compressing pore throats and reducing '
                   'permeability. This permeability reduction '
                   'creates an evolving nonlinear consolidation front where drainage slows '
                   'progressively over time. Concurrently, load transfer along a deep augercast '
                   'pile shaft engages non-uniform shear stress distributions. In the upper '
                   'strata, high soil compressibility requires larger downward displacement to '
                   'mobilize ultimate skin friction, while the stiffer basal sands develop '
                   'immediate end-bearing resistance. If sudden cyclic earthquake shearing occurs, '
                   'contractive tendencies in loose granular layers induce positive excess pore '
                   'pressures that degrade shaft resistance from the ground surface downward. '
                   'Finite-element models can represent this progressive load transfer; none was '
                   'run for this folio.',
 'walkthrough': ['Experiment 1 (Foundation Surcharge & Settlement): Increase Foundation Surcharge '
                 'Delta_q from 60 kPa to 220 kPa. Watch primary consolidation settlement S_c rise '
                 'while the parabolic pore-pressure isochrone bulges rightward.',
                 'Experiment 2 (Consolidation Coefficient & Pore-Pressure Check): Lower '
                 'Consolidation Coefficient c_v toward 0.8 m^2/yr under high surcharge to observe '
                 'undrained excess pore-pressure buildup (r_u > 0.65) and reduced CFA factor of '
                 'safety.',
                 'Experiment 3 (4-Stage Geotechnical Stepper): Click Stages 1 to 4 to trace '
                 'undrained surcharge loading, Terzaghi hydrodynamic dissipation, CFA shaft + toe '
                 'mobilization, and excess pore-pressure screening.'],
 'act4_title': 'Act IV — Automated Geotechnical Rig Telemetry & the Structural & Civil Engineering '
               'Specification Bridge',
 'act4_human_ai': 'CFA rigs are commonly instrumented to record depth, torque, penetration '
                  'rate and pumped grout volume. As a proposal, not something this folio has '
                  'done, those records could be combined with effective-stress models to flag '
                  'piles for review. A reader could explore this with a finite-element library '
                  'such as FEniCS/dolfinx (one of its method papers: DOI 10.1145/3524456) or with '
                  'sparse identification of settlement trends from piezometer data '
                  '(dynamicslab/pysindy, DOI 10.1073/pnas.1517384113). Neither was run here, and '
                  'no model makes a foundation guaranteed-safe. References were checked in the '
                  'Scite index (DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'Looking ahead, and offered as a research direction: machine-learning '
                   'models could read drilling records from instrumented CFA rigs and flag piles '
                   'where the auger may not have reached the intended bearing layer or met '
                   'unexpected soft pockets. Engineers would still interpret the results, judge '
                   'pile integrity and decide on acceptance under the applicable codes. Open frontier '
                   'questions focus on predicting multi-decade creep settlement under variable '
                   'sea-level rise and modeling microbially induced calcite precipitation to '
                   'reinforce liquefiable sands in situ. Combining instrument records with '
                   'sound soil mechanics can make foundations more resilient, though no method '
                   'removes earthquake risk.',
 'cf_bridge': 'An analogy, not a shared equation: Button et al. (Science 2012, DOI '
              '10.1126/science.1223012) proposed a gel-on-brush model of the airway surface, in '
              'which a mucus layer sits on a periciliary brush. In their account, when the '
              'osmotic modulus of the mucus layer rises above that of the brush, the brush and '
              'cilia are compressed and clearance slows or stops, as seen in Cystic Fibrosis. Water moving out of a compressed gel resembles water '
              "draining from a loaded clay in Terzaghi's theory, but the paper does not use "
              "Terzaghi's equation. This page makes no claim about any treatment and is not "
              'medical advice.',
 'sources': ['Gavin, K. G., Cadogan, D., & Casey, P. (2009). Shaft Capacity of Continuous Flight '
             'Auger Piles in Sand. Journal of Geotechnical and Geoenvironmental Engineering, '
             '135(6), 790–798. DOI: 10.1061/(ASCE)GT.1943-5606.0000073.',
             'Button, B., et al. (2012). A Periciliary Brush Promotes the Lung Health by '
             'Separating the Mucus Layer from Airway Epithelia. Science, 337(6097), 937–941. '
             'DOI: 10.1126/science.1223012.',
             'Terzaghi, K., Peck, R. B., & Mesri, G. (1996). Soil Mechanics in Engineering '
             'Practice (3rd ed.). Wiley.',
             'Seed, H. B., & Idriss, I. M. (1971). Simplified procedure for evaluating soil '
             'liquefaction potential. Journal of the Soil Mechanics and Foundations Division, '
             'ASCE, 97(9), 1249–1273. DOI: 10.1061/JSFEAQ.0001662.',
             'Brown, D. A., Dapp, S. D., Thompson, W. R., & Lazarte, C. A. (2007). Design and '
             'Construction of Continuous Flight Auger (CFA) Piles (FHWA GEC No. 8). Federal '
             'Highway Administration.',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). ACM Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: 10.1145/3524456.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Terzaghi 1D '
        'consolidation pore-pressure isochrones and 24-meter CFA augercast deep foundation pile">\n'
        '            <rect x="45" y="30" width="250" height="55" fill="var(--tp-ochre)" '
        'fill-opacity="0.16" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <rect x="45" y="85" width="250" height="75" fill="var(--tp-prussian)" '
        'fill-opacity="0.14" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <rect x="45" y="160" width="250" height="35" fill="var(--tp-verdigris)" '
        'fill-opacity="0.22" stroke="currentColor" stroke-opacity="0.45"/>\n'
        '            <rect id="tp-e05-svg-pile" x="152" y="24" width="36" height="156" '
        'fill="var(--tp-graphite)" stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '            <text x="54" y="52" font-size="10" fill="currentColor">Holocene Fill &amp; '
        'Loose Sand (0–6 m)</text>\n'
        '            <text x="54" y="122" font-size="10" fill="currentColor">Compressible Marine '
        'Clay (6–18 m)</text>\n'
        '            <text x="54" y="182" font-size="10" fill="var(--tp-verdigris)">Dense Bearing '
        'Stratum (18–24 m · Q_toe)</text>\n'
        '            <text x="52" y="20" font-size="11" font-weight="600" '
        'fill="currentColor">1:200 Soil Profile &amp; CFA Pile (D = 750 mm)</text>\n'
        '            <line x1="360" y1="30" x2="360" y2="195" stroke="currentColor" '
        'stroke-opacity="0.45" stroke-width="1.8"/>\n'
        '            <line x1="360" y1="195" x2="635" y2="195" stroke="currentColor" '
        'stroke-opacity="0.45" stroke-width="1.8"/>\n'
        '            <path id="tp-e05-svg-isochrone" d="M 360 30 Q 535 112 360 195" '
        'fill="var(--tp-minium)" fill-opacity="0.16" stroke="var(--tp-minium)" '
        'stroke-width="2.8"/>\n'
        '            <path d="M 360 30 Q 445 112 360 195" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="2" stroke-dasharray="5,4"/>\n'
        '            <text x="365" y="20" font-size="11" font-weight="600" '
        'fill="currentColor">Terzaghi Excess Pore Pressure Isochrone Δu(z, t)</text>\n'
        '            <text id="tp-e05-svg-label" x="455" y="108" font-size="10.5" '
        'fill="var(--tp-minium)">U_avg = 63.2% · Q_ult = 3,865 kN</text>\n'
        '            <text x="415" y="212" font-size="10" fill="currentColor">Excess Pore Pressure '
        'Δu (kPa) · Drainage Boundaries z = 0, 2H_dr</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what Continuous Flight Auger deep foundation piles and '
        'Terzaghi consolidation strata would look like in cutaway (artistic impression, not a '
        'measured structure)',
 'caption': 'Conceptual Vision Plate E.05-V (Imagining What It Would Look Like) · Artistic '
            'geotechnical cutaway imagining Continuous Flight Auger (CFA) deep foundation piles '
            'drilled through stratified clay and sand into granite bedrock.'}

DISPATCH = {'kicker': 'FRONTIER GEOTECHNICAL DISPATCH · AUTOMATED CFA RIG TELEMETRY & POROELASTIC GELS',
 'headline': 'A Century After Erdbaumechanik: Instrumented CFA Piles and Effective Stress',
 'body': "One century after Karl Terzaghi's Erdbaumechanik (1925), continuous flight auger (CFA) "
         'piles are installed with rigs that record depth, torque and grout volume (FHWA GEC No. '
         '8), and field tests show how their shaft resistance develops in sand (Gavin, Cadogan & '
         'Casey 2009, DOI 10.1061/(ASCE)GT.1943-5606.0000073). In a different field, Button and '
         'colleagues (Science 2012, DOI 10.1126/science.1223012) described osmotic compression '
         'of the airway periciliary brush, an idea this folio offers only as an analogy.'}

META_3D = ('Terzaghi Consolidation Dish & 4-Pile Bearing Cones',
 'X/Z: Foundation Mat Footprint · Y: Effective Stress Consolidation & CFA Pile Capacity')

ES_TRANSLATION = {'title_es': 'Mecánica de Suelos de Terzaghi, Pilotes Profundos CFA y Presión de Poro en Exceso',
 'subtitle_es': 'Cómo el principio de esfuerzo efectivo de Karl Terzaghi σ′_v = σ_v − u, la '
                'consolidación hidrodinámica ∂u/∂t = c_v ∂²u/∂z² y las cimentaciones profundas CFA '
                'se relacionan con el asentamiento y la presión de poro en exceso.',
 'why_es': 'Al pisar una esponja empapada, primero se presuriza el agua atrapada; el esqueleto de '
           'la esponja sólo se comprime a medida que el agua escapa lentamente por los poros '
           '(consolidación de Terzaghi).',
 'bridge_es': 'Una analogía, no una ecuación compartida: en el modelo de gel sobre cepillo '
              'de Button y colegas (2012), cuando la capa de moco tiene un módulo osmótico '
              'mayor que el del cepillo periciliar, lo comprime y la depuración se frena, como en '
              'la Fibrosis Quística. Esta página no habla de tratamientos ni es consejo médico.',
 'plain_es': 'En 1925, el ingeniero austriaco Karl Terzaghi, entonces profesor en el Robert '
             'College de Constantinopla (Estambul), publicó Erdbaumechanik, el libro con el que '
             'suele fecharse el inicio de la mecánica de suelos moderna. Desde hacía mucho, las '
             'construcciones sobre arcilla se asentaban de forma desigual. Terzaghi explicó que '
             'el suelo saturado actúa como una esponja compuesta por granos minerales y agua '
             'atrapada. Cuando construyen un edificio pesado, el peso inicial lo '
             'sostiene la presión del agua subterránea. Solo a medida que esa agua escurre '
             'lentamente por los diminutos poros del subsuelo, los granos sólidos se juntan para '
             'cargar la estructura. Para entenderlo, piensen en una esponja empapada: al pisarla, '
             'el agua sale disparada primero, y solo después la goma se comprime. Un sismo que '
             'sacude arena suelta y húmeda es otro problema: la presión del agua puede subir y '
             'separar los granos, y los ingenieros lo evalúan por separado. Los pilotes '
             'profundos de concreto que llevan la carga a capas más firmes son una herramienta '
             'para eso, no una garantía.',
 'deep_es': 'El principio de esfuerzo efectivo de Terzaghi establece que la resistencia del suelo '
            'depende del esfuerzo neto sobre los granos minerales una vez restada la presión de '
            'poro. Cuando una sobrecarga actúa sobre arcillas saturadas, la disipación '
            'hidrodinámica del agua sigue una ecuación diferencial de difusión, transfiriendo '
            'carga gradualmente al esqueleto sólido. Si ocurre un terremoto, las vibraciones '
            'rápidas pueden incrementar la presión de poro en arena suelta saturada, un proceso '
            'distinto de la consolidación bajo una sobrecarga constante que requiere su propia '
            'evaluación en sitio. Para proteger grandes estructuras, la ingeniería '
            'geotécnica puede usar, entre otras herramientas, pilotes profundos de barrena '
            'continua que transfieren las cargas hacia estratos más firmes. Las perforadoras '
            'suelen registrar la profundidad, el torque y el volumen de concreto bombeado, '
            'datos que ayudan a los ingenieros a revisar cada pilote. Los valores de esta página '
            'son ilustrativos y ningún método elimina el riesgo sísmico.'}
