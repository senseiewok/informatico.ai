# -*- coding: utf-8 -*-
"""Open Bounties — Folio B.03: After the $100M XPRIZE Carbon Removal: A Sub-45 kg CO₂e/m² SIMP Mineralized Slab Design Study."""


FOLIO = {'slug': 'b03',
 'folio_id': 'B.03',
 'bounty_id': 'BOUNTY-E1',
 'cat': 'aec',
 'plate_slug': 'b03',
 'pillar_label_en': 'Civil Engineering & Net-Zero Structures',
 'pillar_label_es': 'Ingeniería Civil y Estructuras Cero Neto',
 'badge_en': 'GRAND CHALLENGE B.03 (E-1) · XPRIZE CARBON (CLOSED 2025) + ISTRUCTE',
 'badge_es': 'GRAN RETO B.03 (E-1) · XPRIZE CARBON (CERRADO 2025) + ISTRUCTE',
 'title': 'After the $100M XPRIZE Carbon Removal: A Sub-45 kg CO₂e/m² SIMP Mineralized Slab Design Study',
 'title_es': 'Tras el XPRIZE Carbon Removal ($100M): Estudio de Diseño de Losas SIMP Bajo 45 kg CO₂e/m²',
 'subtitle': 'How Bendsøe–Sigmund SIMP topology optimization in FEniCS/dolfinx and carbonated '
             'mineral curing could cut structural floor embodied carbon by 73% in this folio\'s model while keeping stiffness within its compliance limit.',
 'subtitle_es': 'Cómo la optimización topológica SIMP de Bendsøe–Sigmund en FEniCS/dolfinx y el '
                'curado por mineralización de CO₂ podrían reducir 73% el carbono incorporado '
                'en el modelo de este folio manteniendo la rigidez dentro del límite.',
 'why_en': 'Flat reinforced-concrete floor slabs make up a large share of structural mass and '
           'embodied CO₂ in typical multi-story frames (this folio uses an illustrative solid-slab '
           'baseline of 148.0 kg CO₂e/m²), even though concrete near the neutral axis carries '
           'little bending stress. In this folio\'s model, carving stress-aligned ribs and '
           'mineralizing CO₂ lowers modeled net carbon below 40 kg CO₂e/m².',
 'why_es': 'Las losas planas de concreto armado aportan una gran parte de la masa estructural y '
           'del CO₂ incorporado en marcos de varios pisos (este folio toma como línea base '
           'ilustrativa 148.0 kg CO₂e/m²), aunque el concreto cercano al eje neutro soporta poco '
           'esfuerzo. En el modelo de este folio, esculpir nervaduras con SIMP y mineralizar CO₂ '
           'reduce la huella modelada bajo 40 kg CO₂e/m².',
 'governing_law': 'e_net = e_0 (V/V_0) − m_CO2 = 39.40 kg CO₂e/m² < 45.0 · c/c_0 = 1 + 0.40(1 − '
                  'V/V_0)^1.35 = 1.224 < 1.35',
 'pass_pill_en': 'PASS · 39.4 kg CO₂e/m² · c/c₀ = 1.224',
 'pass_pill_es': 'APROBADO · 39.4 kg CO₂e/m² · c/c₀ = 1.224',
 'verifier_script': 'bounties/bounty_e1_simp_carbon_slab.py',
 'skill_dir': 'skills/bounties/b03',
 'skill_name': 'bounty-b03-simp-carbon-slab',
 'primary_doi': '10.1007/s001580050176',
 'scite_summary': 'Sigmund (2001) and Bendsøe & Sigmund (1999) SIMP topology optimization references '
                  'checked against Crossref and Scite.',
 'date_published': '2026-11-04',
 'date_redated': '2026-11-15',
 'current_edition': 'REV 1.3',
 'reading_time': '14 MIN READ',
 'companion_folios': [('engineering',
                       'e11',
                       'Folio E.11',
                       'SIMP Topology Optimization & Formula 1 Inerter Damping'),
                      ('engineering',
                       'e12',
                       'Folio E.12',
                       'Control Barrier Functions, Firefly Renewable Grids & RISC-V Silicon'),
                      ('engineering',
                       'e09',
                       'Folio E.09',
                       'Bacterial & Crystalline Self-Healing Concrete'),
                      ('engineering',
                       'e10',
                       'Folio E.10',
                       '3D Concrete Printing Thixotropy & Suiker Buckling')],
 'external_links': [('XPRIZE Carbon Removal ($100M, Closed Apr 2025)',
                     'https://www.xprize.org/prizes/carbonremoval'),
                    ('IStructE Structural Awards (Commissioned Built Structures Only)',
                     'https://www.istructe.org/'),
                    ('FEniCS/dolfinx (Finite Element PDE)', 'https://github.com/FEniCS/dolfinx')],
 'act1_dropcap': 'Cement production is commonly estimated at up to about 8% of global carbon dioxide '
                 'emissions (an estimate not sourced in this folio), and in typical multi-story '
                 'frames, flat two-way floor slabs consume a large fraction of structural concrete '
                 '(Küpfer et al., 2025, DOI 10.1088/1755-1315/1554/1/012083). Because a solid slab '
                 'carries bending mainly near its top and bottom faces, material near the neutral '
                 'axis contributes little bending stiffness.',
 'act1_body': "Martin Bendsøe (1989, DOI 10.1007/bf01650949) and Ole Sigmund (2001, DOI "
              '10.1007/s001580050176) formulated Solid Isotropic Material with Penalization (SIMP), '
              'turning layout design into a finite-element optimization problem solvable in '
              'open-source libraries such as FEniCS/dolfinx (Scroggs et al., 2022, DOI '
              '10.1145/3524456). Penalizing intermediate densities E(ρ_e) = E_min + ρ_e^p (E_0 - '
              'E_min) with p = 3 and filtering sensitivities favors branching ribs aligned with '
              "Michell's (1904, DOI 10.1080/14786440409463229) principal stress trajectories. If "
              'printable concrete ribs (Roussel, 2018, DOI 10.1016/j.cemconres.2018.04.005; '
              'Folio E.10) are paired with carbonate mineralization (CaO + CO₂ → CaCO₃), modeled '
              'net embodied carbon moves from the illustrative 148.0 kg CO₂e/m² baseline to 39.40 '
              'kg CO₂e/m² in this folio\'s mass balance, below its 45.0 kg CO₂e/m² design target. '
              'That target is not an XPRIZE Carbon Removal criterion, and no slab has been built '
              'or tested.',
 'pullquote': 'Bone adapts density along load paths; SIMP topology optimization models concrete '
              'floor slabs with that same stress-aligned economy.',
 'chronology': [('1904',
                 'A. G. M. Michell formulates optimality criteria for minimum-weight funicular '
                 'trusses aligned with principal strain trajectories (DOI '
                 '10.1080/14786440409463229).'),
                ('1989–2001',
                 'Martin Bendsøe introduces the material-distribution method (DOI '
                 '10.1007/bf01650949) and Ole Sigmund publishes the 99-line SIMP topology '
                 'optimization code (DOI 10.1007/s001580050176).'),
                ('2018–2023',
                 'Printable concrete rheology (Roussel, 2018, DOI 10.1016/j.cemconres.2018.04.005) '
                 'and FEniCS/dolfinx (Scroggs et al., 2022, DOI 10.1145/3524456) support open '
                 'ribbed-slab modeling.'),
                ('2024–2026',
                 'The $100M XPRIZE Carbon Removal and IStructE SCORS highlight embodied and removed '
                 'carbon; the sub-45 kg CO₂e/m² line is this folio\'s own illustrative target.')],
 'act2_intuition': 'In this folio\'s simplified algebraic model, removing volume fraction V/V₀ from '
                   'the 148.0 kg CO₂e/m² baseline lowers carbon linearly as e_net = e₀(V/V₀) - '
                   'm_CO₂, while the compliance surrogate c/c₀ = 1 + 0.40(1 - V/V₀)^1.35 rises '
                   'gently. At the reference operating point V/V₀ = 0.35 (65% modeled slab volume '
                   'reduction) and m_CO₂ = 12.4 kg/m², c/c₀ = 1.224 (< 1.35) and e_net = 39.40 kg '
                   'CO₂e/m² (< 45.0).',
 'sliders': [{'id': 'tp-bounty-s0',
              'label': 'SIMP Volume Fraction V / V₀',
              'min': 0.2,
              'max': 0.7,
              'step': 0.01,
              'value': 0.35,
              'unit': 'V/V₀ = '},
             {'id': 'tp-bounty-s1',
              'label': 'Mineralized CO₂ Uptake (kg/m²)',
              'min': 0.0,
              'max': 20.0,
              'step': 0.4,
              'value': 12.4,
              'unit': 'm_CO₂ = '}],
 'readouts': [{'label': 'Net Embodied Carbon e_net', 'value': '39.40 kg CO₂e/m² (< 45.0 target)'},
              {'label': 'Normalized Compliance c / c₀',
               'value': '1.224 (< 1.35 L/250 deflection limit)'},
              {'label': 'Mass Reduction vs. Solid Slab', 'value': '65.0% concrete mass saved'},
              {'label': 'Verifier Verdict (Worked Example)', 'value': 'PASS · SUB-45 KG CO₂E/M²'}],
 'steps': ['Conceptual Stage 1 (SIMP Context, Not Run in Script): Linear elasticity assembly '
           'K(ρ) u = f on floor domain Ω (as in FEniCS/dolfinx, DOI 10.1145/3524456).',
           'Conceptual Stage 2 (SIMP Context, Not Run in Script): Power-law penalization E(ρ_e) '
           'with p = 3 and sensitivity filtering ∂c/∂ρ_e (Bendsøe 1989; Sigmund 2001, DOI '
           '10.1007/s001580050176).',
           'Conceptual Stage 3 & Surrogate Check: At reference fraction V/V₀ = 0.35, the surrogate '
           'compliance function gives c/c₀ = 1.0 + 0.40(1 - 0.35)^1.35 = 1.224 < 1.35.',
           'Stage 4 (Evaluated by Harness): Subtract illustrative mineralization parameter m_CO₂ = '
           '12.4 kg CO₂e/m² from 148.0 × 0.35 = 51.80 to get e_net = 39.40 kg CO₂e/m² < 45.0.'],
 'rules': ['Embodied Carbon Ceiling (folio design target): Net cradle-to-gate embodied carbon e_net '
           '= 148.0(V/V₀) - m_CO₂ must remain strictly below 45.0 kg CO₂e/m².',
           'Normalized Compliance Bound (model target): Normalized structural compliance surrogate '
           'c/c₀ = 1.0 + 0.40(1 - V/V₀)^1.35 must remain strictly below 1.35.',
           'Model Window on the Workbench: At m_CO₂ = 12.4 kg/m², keeping e_net < 45.0 kg CO₂e/m² '
           'requires V/V₀ < 0.3878 (at most 0.38 on the 0.01-step slider). Across the slider range '
           '[0.20, 0.70], c/c₀ is at most 1.296 (at V/V₀ = 0.20); in the algebraic surrogate '
           'curve, c/c₀ reaches 1.35 only below V/V₀ ≈ 0.0942.'],
 'sidenote_1': {'kicker': 'SIDENOTE B.03-A · WHY p = 3 PENALIZATION WORKS',
                'body': 'At p = 3, an intermediate density ρ = 0.5 provides only 12.5% of solid '
                        'stiffness for 50% of the mass, pushing the optimizer toward crisp 0/1 '
                        'ribs (Bendsøe & Sigmund, 1999, DOI 10.1007/s004190050248).'},
 'sidenote_2': {'kicker': 'SIDENOTE B.03-B · MINERALIZATION CHEMISTRY',
                'body': 'In this model, carbonation curing (Ca(OH)₂ + CO₂ → CaCO₃ + H₂O) represents '
                        'an illustrative uptake parameter m_CO₂ = 12.4 kg CO₂e/m²; actual strength '
                        'and uptake depend on mix and curing measurements.'},
 'walkthrough': ['Inspect the reference design point at V/V₀ = 0.35 and m_CO₂ = 12.4 kg/m²: net '
                 'carbon is 39.40 kg CO₂e/m² (< 45.0) and compliance ratio is 1.224 (< 1.35) '
                 '(PASS).',
                 'Drag Volume Fraction V/V₀ up to 0.50: watch modeled compliance drop to 1.157 '
                 'while net carbon jumps to 61.60 kg CO₂e/m², failing the 45.0 kg CO₂e/m² target.',
                 'Set Mineralized CO₂ Uptake m_CO₂ = 0.0 kg/m² (or click [⚡ Counterfactual '
                 'Axiom-Knockout]): see how un-mineralized Portland cement at V/V₀ = 0.35 reaches '
                 '51.80 kg CO₂e/m², illustrating why both terms are needed in the model.'],
 't0_t1_certified': ['Algebraic compliance-carbon model in '
                     'bounties/bounty_e1_simp_carbon_slab.py (< 0.05s runtime; no finite-element '
                     'solver or planted-defect mode yet).',
                     'References FEniCS/dolfinx (Scroggs et al., 2022, DOI 10.1145/3524456) and '
                     'Sigmund (2001, DOI 10.1007/s001580050176) for the SIMP formulation.'],
 't2_t3_open_horizon': ['XPRIZE Carbon Removal ($100M, concluded April 2025) & IStructE Structural '
                        'Awards (commissioned built structures only): any real claim about a slab '
                        'would require full-scale physical load testing (ACI 318 / EN 1992-1-1 '
                        'four-point bending to ultimate failure) and third-party ISO 14040/14044 '
                        'cradle-to-grave LCA review.'],
 'sources': ['Michell, A. G. M. (1904). The limits of economy of material in frame-structures. '
             'Philosophical Magazine, 8(47), 589–597. DOI 10.1080/14786440409463229',
             'Bendsøe, M. P. (1989). Optimal shape design as a material distribution problem. '
             'Structural Optimization, 1(4), 193–202. DOI 10.1007/bf01650949',
             'Bendsøe, M. P., & Sigmund, O. (1999). Material interpolation schemes in topology '
             'optimization. Archive of Applied Mechanics, 69(9–10), 635–654. DOI '
             '10.1007/s004190050248',
             'Sigmund, O. (2001). A 99 line topology optimization code written in Matlab. '
             'Structural and Multidisciplinary Optimization, 21(2), 120–127. DOI '
             '10.1007/s001580050176',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). '
             'Construction of arbitrary order finite element degree-of-freedom maps on polygonal '
             'and polyhedral cell meshes. ACM Transactions on Mathematical Software, 48(2), 1–23. '
             'DOI 10.1145/3524456',
             'Roussel, N. (2018). Rheological requirements for printable concretes. Cement and '
             'Concrete Research, 112, 76–85. DOI 10.1016/j.cemconres.2018.04.005',
             'Küpfer, C., et al. (2025). Concrete floors: multi-criteria analysis of conventional '
             'and novel solutions. IOP Conference Series: Earth and Environmental Science, '
             '1554(1), 012083. DOI 10.1088/1755-1315/1554/1/012083'],
 'act1_plain_bridge': 'Think about the floors in schools, offices, libraries, and apartment towers. '
                      'In most of them, the floor beneath your feet is a thick flat slab of solid '
                      'concrete. Concrete resists compression well, yet manufacturing cement carries '
                      'a heavy carbon cost. Inside a solid bending slab, concrete near the middle '
                      'carries little stress compared with the top and bottom faces. Inspired by '
                      'porous bone structure, topology optimization models carve away low-stress '
                      'middle material—up to 65% in this folio\'s example—leaving ribs where '
                      'forces travel. Pairing that geometry with CO₂ mineralization curing in the '
                      'model lowers net embodied carbon below 40 kg CO₂e/m² while keeping '
                      'modeled stiffness within the service limit.',
 'act1_stakes': 'Cement production is commonly estimated at roughly eight percent of global carbon '
                'dioxide emissions (an estimate not sourced in this folio). In multi-story '
                'buildings, flat reinforced concrete floor slabs form a major share of structural '
                'mass and embodied carbon (Küpfer et al., 2025, DOI 10.1088/1755-1315/1554/1/012083). '
                'Extra slab weight amplifies gravity loads on columns, walls, and foundations. '
                'Flat prismatic slabs became standard because flat wooden formwork was cheap, '
                'even though builders since Robert Maillart and Pier Luigi Nervi knew material '
                'near the neutral axis carries little stress. The Institution of Structural '
                'Engineers SCORS scale and the XPRIZE Carbon Removal competition highlighted '
                'embodied and removed carbon. This folio sets its own illustrative target of 45 '
                'kg CO₂e/m², well below the 148.0 kg CO₂e/m² its model assigns to a solid flat '
                'slab, by combining SIMP topology optimization with modeled carbonate '
                'mineralization.',
 'act2_analogy': 'Consider a solid wooden stump beside the frame of a racing bicycle. The solid '
                 'stump carries weight, yet much of the inner wood feels little bending stress; '
                 'the bicycle frame arranges slender tubes along load paths. In this folio\'s '
                 'model, the illustrative solid slab baseline is 148.0 kg CO₂e/m². The volume '
                 'fraction V/V₀ trims unused mass down to 0.35 (35%), while the modeled '
                 'compliance ratio rises slightly to 1.224, below the 1.35 limit. Finally, '
                 'carbonation curing models binding 12.4 kg CO₂e/m² as solid calcium carbonate '
                 'during curing, bringing modeled net emissions to 39.40 kg CO₂e/m².',
 'act2_plain_primer': 'Explore the two sliders in the Act III workbench to see how modeled geometry '
                      'and mineralization interact. The first slider sets the SIMP Volume Fraction '
                      'V/V₀ from 0.20 to 0.70. At our reference point of 0.35, 65% of modeled slab '
                      'volume is removed while stiffness stays within the limit (c/c₀ = 1.224). '
                      'Pulling the slider left toward 0.20 makes the model more flexible (c/c₀ '
                      'reaches 1.296); pushing it right toward 0.70 makes it stiffer but exceeds '
                      'the 45.0 kg CO₂e/m² target. The second slider sets Mineralized CO₂ Uptake '
                      'm_CO₂ (kg/m²). Clicking Counterfactual Knockout sets m_CO₂ to zero, raising '
                      'net embodied carbon from 39.40 to 51.80 kg CO₂e/m² and failing this folio\'s '
                      '45.0 kg CO₂e/m² threshold, showing why both terms matter in the model.',
 'distill_diagram': {'analogy_title': 'Trabecular Bone & Bicycle Truss',
                     'analogy_sub': 'Carving dead core concrete while mineralizing CO2 into stone '
                                    'matrix',
                     'force_a_title': 'SIMP Volume Fraction (V/V0)',
                     'force_a_sub': 'Carves dead core mass along Michell principal stress '
                                    'trajectories',
                     'force_b_title': 'Mineralized CO2 Uptake (m_CO2)',
                     'force_b_sub': 'Models binding gaseous CO2 into solid calcium carbonate '
                                    'matrix',
                     'threshold_title': 'Folio Design Target',
                     'threshold_eq': 'e_net < 45.0 kg CO2e/m2 and c/c0 < 1.35',
                     'threshold_sub': 'Net carbon below 45 kg CO2e/m2 while keeping modeled '
                                      'compliance below 1.35',
                     'threshold_pass': 'PASS: e_net = 39.4 kg CO2e/m2, c/c0 = 1.224 (<1.35 model '
                                       'bound)',
                     'threshold_fail': 'FAIL: Unmineralized or over-dense slab exceeds 45 kg '
                                       'CO2e/m2',
                     'caption': 'Visual intuition bridge connecting porous bone mechanics to '
                                'topology-optimized material removal and modeled carbonate '
                                'mineralization.'},
 'act2_deepening': 'SIMP topology optimization addresses the trade-off between removing mass and '
                   'controlling deflection. Over a floor domain Omega, finite elements receive a '
                   'relative density rho_e in [0, 1]. Martin Bendsøe (1989) and Ole Sigmund '
                   '(2001) showed that penalizing element stiffness via E(rho_e) = E_min + '
                   'rho_e^p (E_0 - E_min) with p = 3 makes intermediate densities inefficient: a '
                   'half-density element gives 12.5% stiffness for 50% mass. With a sensitivity '
                   'filter radius r_min to suppress checkerboarding, optimization favors binary '
                   'ribs aligned with principal stresses. On this folio\'s surrogate curve, '
                   'normalized compliance scales as c/c_0 = 1.0 + 0.40(1 - V/V_0)^1.35; at V/V_0 '
                   '= 0.35, c/c_0 = 1.224, below the 1.35 model limit. In the mass balance e_net '
                   '= e_0 (V/V_0) - m_CO2, starting from the illustrative 148.0 kg CO₂e/m² '
                   'baseline, keeping 35% gives 51.80 kg CO₂e/m², and subtracting m_CO2 = 12.4 '
                   'kg/m² yields 39.40 kg CO₂e/m².',
 'act4_human_ai': 'Developing low-carbon structural components requires an integrated design loop '
                  'between human engineers and transparent computational tools. The human '
                  'structural engineer sets project parameters: column grids, service '
                  'penetrations, boundary conditions, and design load combinations (1.2D + 1.6L). '
                  'Open-source finite-element libraries such as FEniCS/dolfinx assemble '
                  'variational forms and compute adjoint sensitivities for SIMP rib layouts, while '
                  'Python checks evaluate the carbon mass balance and deflection bounds. Rather '
                  'than relying on black-box neural networks, this open workflow pairs generative '
                  'topology exploration with inspectable algebraic and finite-element checks so '
                  'independent studios and academic labs can audit and extend the model.',
 'act4_deepening': 'Sustainable-construction claims are often blurred by unverified life-cycle '
                   'labels and small clinker adjustments presented without numbers. Folio B.03 '
                   'puts its two algebraic design checks inside an open Python script, '
                   'bounties/bounty_e1_simp_carbon_slab.py, running offline with no third-party '
                   'packages. The script evaluates net embodied carbon e_net = 148.0(V/V₀) - m_CO₂ '
                   'against the 45.0 kg CO₂e/m² ceiling and the compliance surrogate c/c₀ = 1.0 + '
                   '0.40(1 - V/V₀)^1.35 against 1.35. Leaving out mineralization curing (m_CO₂ = '
                   '0.0 at V/V₀ = 0.35) raises e_net to 51.80 kg CO₂e/m² and returns FAIL; raising '
                   'V/V₀ to 0.50 with m_CO₂ = 12.4 gives 61.60 kg CO₂e/m² and also returns FAIL. '
                   'The script computes only these two model inequalities and does not yet include '
                   'a planted-defect mode or finite-element stress check, so physical testing '
                   'remains essential before any built use.',
 'plain_es': 'En casi todos los edificios donde vivimos y trabajamos, los pisos están hechos de '
             'losas gruesas de concreto macizo. El concreto es muy resistente para soportar peso, '
             'pero fabricar cemento genera una enorme contaminación ambiental. No obstante, en una '
             'losa plana convencional, la mayor parte del material en el centro casi no realiza '
             'trabajo estructural: simplemente añade peso muerto que el edificio debe sostener día '
             'con día. Inspirándonos en la estructura porosa de los huesos humanos y las ramas de '
             'los árboles, podemos retirar mediante algoritmos computacionales hasta el sesenta y '
             'cinco por ciento de ese concreto innecesario, dejando nervaduras esbeltas que siguen '
             'con precisión las líneas de fuerza. Además, durante el proceso de curado en planta, '
             'inyectamos dióxido de carbono capturado para transformarlo en roca mineral de '
             'carbonato de calcio. Así logramos reducir la huella de carbono por debajo de '
             'cuarenta kilogramos por metro cuadrado en el modelo, manteniendo la flexibilidad '
             'dentro del límite de servicio.',
 'deep_es': 'La optimización modelada equilibra la reducción topológica SIMP con el secuestro '
            'mineralizado de carbono. Sobre la curva sustituta c/c₀ = 1 + 0.40(1 − V/V₀)^1.35, en '
            'V/V₀ = 0.35 se obtiene c/c₀ = 1.224 (< 1.35), mientras que e_net = e₀(V/V₀) − m_CO₂ '
            'baja de 148.0 a 51.80 kg CO₂e/m² y, al restar m_CO₂ = 12.4 kg/m², alcanza 39.40 kg '
            'CO₂e/m² por debajo de la meta de diseño de 45.0 kg CO₂e/m² de este folio.',
 'easy_history_title_en': 'How Human Pioneers Reached This Frontier: From 1904 Bone & Truss '
                          'Geometry to SIMP & Mineralized Concrete',
 'easy_history_title_es': 'Cómo los Pioneros Humanos Llegaron a Esta Frontera: De las Cerchas de '
                          '1904 a SIMP y el Concreto Mineralizado',
 'easy_history_en': 'In 1904, an Australian mechanical engineer named Anthony George Maldon '
                    'Michell asked a question that still haunts every structural engineer: what is '
                    'the lightest possible frame that can carry a given load between supports? '
                    'Working purely with calculus on paper, Michell showed that an ideal '
                    'minimum-weight structure uses curving, orthogonal fan-like ribs along the '
                    'paths of tension and compression—resembling the porous trabecular bone '
                    "inside a human femur or a bird's wing—rather than solid blocks. Half a "
                    'century later, Italian master builder Pier Luigi Nervi applied that '
                    'principle in poured concrete, sculpting ribbed ceilings for exhibition halls '
                    'in Turin and Rome that saved large amounts of material. Yet because crafting '
                    'custom curved wooden molds by hand took months of specialized carpentry, '
                    "twentieth-century construction abandoned Nervi's ribs in favor of cheap, "
                    'flat, solid concrete slabs—wasting up to two-thirds of every floor plate as '
                    'dead, inactive weight.\n'
                    '\n'
                    'The turning point arrived between 1989 and 2001 when Danish mathematicians '
                    'Martin Bendsøe and Ole Sigmund invented Solid Isotropic Material with '
                    'Penalization (SIMP) and published a 99-line computer code that allowed '
                    'finite-element solvers to carve solid blocks into rib layouts automatically. '
                    'In the 2020s, open-source PDE engines like FEniCS/dolfinx paired with '
                    'robotic 3D concrete extrusion reduced reliance on wooden molds, while '
                    'accelerated carbonate mineralization (injecting captured CO₂ gas during '
                    'curing so it reacts into solid calcium carbonate CaCO₃ inside the slab) '
                    'lowered modeled floor emissions—which is how this folio\'s model brings '
                    'floor emissions below its own 45 kg CO₂e/m² design target.',
 'easy_history_es': 'En 1904, el ingeniero australiano Anthony George Maldon Michell planteó una '
                    'pregunta que aún inspira a toda la ingeniería estructural: ¿cuál es la '
                    'estructura más ligera posible capaz de sostener una carga dada entre apoyos? '
                    'Con puro cálculo variacional en papel, Michell mostró que la estructura '
                    'óptima de peso mínimo teje nervaduras curvas ortogonales que siguen las líneas '
                    'de tensión y compresión, semejantes al hueso trabecular poroso del fémur '
                    'humano o del ala de un ave, en lugar de bloques macizos. Medio siglo después, '
                    'el maestro italiano Pier Luigi Nervi llevó la geometría de Michell al concreto '
                    'real, esculpiendo techos nervados en Turín y Roma con un ahorro notable de '
                    'material. No obstante, como fabricar cimbras curvas de madera a mano requería '
                    'meses de carpintería artesanal, la construcción del siglo XX abandonó las '
                    'nervaduras de Nervi en favor de losas planas macizas baratas de moldear, '
                    'desperdiciando hasta dos tercios de cada entrepiso como peso muerto inactivo.\n'
                    '\n'
                    'El punto de inflexión llegó entre 1989 y 2001 cuando Martin Bendsøe y Ole '
                    'Sigmund inventaron el método SIMP (Material Isotrópico Sólido con '
                    'Penalización) y publicaron su código de 99 líneas, permitiendo que '
                    'solucionadores de elementos finitos esculpieran bloques macizos en nervaduras '
                    'automáticamente. En la década de 2020, los motores abiertos de elementos '
                    'finitos como FEniCS/dolfinx unidos a la impresión 3D robótica redujeron la '
                    'dependencia de cimbras, mientras que la mineralización acelerada de carbonatos '
                    '(inyectar CO₂ capturado durante el curado para fijarlo como carbonato de '
                    'calcio CaCO₃) redujo las emisiones modeladas bajo la meta de diseño de 45 kg '
                    'CO₂e/m² de este folio.',
 'history_milestones': [{'year': '1904',
                         'who_en': 'A. G. M. Michell',
                         'who_es': 'A. G. M. Michell',
                         'title_en': 'Minimum-Weight Principal Stress Continua',
                         'title_es': 'Continuos de Peso Mínimo sobre Líneas Principales',
                         'summary_en': 'Derives optimality criteria for minimum-weight trusses '
                                       'aligning orthogonal tension and compression ribs along '
                                       'principal strain trajectories.',
                         'summary_es': 'Deriva criterios de optimalidad para estructuras de peso '
                                       'mínimo con nervaduras ortogonales alineadas con las '
                                       'trayectorias principales de deformación.',
                         'roadblock_en': 'Analytical solutions exist only for idealized point '
                                         'loads; arbitrary 3D building bays cannot be solved by '
                                         'hand.',
                         'roadblock_es': 'Las soluciones analíticas solo existen para cargas '
                                         'puntuales simples; las crujías 3D reales no pueden '
                                         'resolverse a mano.'},
                        {'year': '1951–1960',
                         'who_en': 'Pier Luigi Nervi',
                         'who_es': 'Pier Luigi Nervi',
                         'title_en': 'Isostatic Ribbed Ferrocement Floor Slabs',
                         'title_es': 'Losas Nervadas Isostáticas de Ferrocemento',
                         'summary_en': 'Builds the Gatti Wool Factory and Palazzetto dello Sport '
                                       'with curving floor ribs following bending stress lines.',
                         'summary_es': 'Construye la fábrica Gatti y el Palazzetto dello Sport con '
                                       'nervaduras curvas que siguen los momentos flectores.',
                         'roadblock_en': 'Hand-built plaster and timber formwork is too '
                                         'labor-intensive for everyday commercial buildings.',
                         'roadblock_es': 'Las cimbras artesanales de yeso y madera resultan '
                                         'demasiado costosas para edificios convencionales.'},
                        {'year': '1989–2001',
                         'who_en': 'Martin Bendsøe & Ole Sigmund',
                         'who_es': 'Martin Bendsøe y Ole Sigmund',
                         'title_en': 'SIMP Power-Law Topology Optimization',
                         'title_es': 'Optimización Topológica por Ley de Potencias SIMP',
                         'summary_en': 'Penalizes intermediate finite-element densities (E = ρ^p '
                                       'E₀, p = 3) with a Helmholtz filter to carve crisp 0/1 '
                                       'ribs.',
                         'summary_es': 'Penaliza densidades intermedias (E = ρ^p E₀, p = 3) con '
                                       'filtro de Helmholtz para esculpir nervaduras nítidas 0/1.',
                         'roadblock_en': 'Removing 65% of concrete mass alone still leaves ~51.8 '
                                         'kg CO₂e/m² from Portland clinker calcination.',
                         'roadblock_es': 'Retirar 65% de la masa por sí solo aún deja ~51.8 kg '
                                         'CO₂e/m² por la calcinación del clínker Portland.'},
                        {'year': '2018–2023',
                         'who_en': 'FEniCS/dolfinx & Printable Concrete Research',
                         'who_es': 'FEniCS/dolfinx e Investigación en Concreto Imprimible',
                         'title_en': 'Open PDE Solvers & Ribbed Floor Models',
                         'title_es': 'Solvers Abiertos de EDPs y Modelos de Losas Nervadas',
                         'summary_en': 'Open-source variational PDE solvers (DOI 10.1145/3524456) '
                                       'and printable concrete research (DOI '
                                       '10.1016/j.cemconres.2018.04.005) support ribbed-slab '
                                       'design; V/V₀ = 0.35 is this folio\'s reference parameter.',
                         'summary_es': 'Los solvers abiertos de EDPs (DOI 10.1145/3524456) y la '
                                       'investigación en concreto imprimible (DOI '
                                       '10.1016/j.cemconres.2018.04.005) respaldan el modelado de '
                                       'losas nervadas; V/V₀ = 0.35 es el parámetro de referencia '
                                       'de este folio.',
                         'roadblock_en': 'Removing 65% of concrete volume still leaves 51.80 kg '
                                         'CO₂e/m² in this model without mineralization.',
                         'roadblock_es': 'Retirar 65% del volumen aún deja 51.80 kg CO₂e/m² en este '
                                         'modelo sin mineralización.'},
                        {'year': '2024–2026',
                         'who_en': 'This folio\'s design study',
                         'who_es': 'Estudio de diseño de este folio',
                         'title_en': 'Sub-45 kg CO₂e/m² Mineralized Structural Slabs',
                         'title_es': 'Losas Mineralizadas Bajo 45 kg CO₂e/m²',
                         'summary_en': 'Combines V/V₀ = 0.35 SIMP ribs with 12.4 kg/m² carbonate '
                                       'mineralization (CaO + CO₂ → CaCO₃) to reach 39.40 kg '
                                       'CO₂e/m² and c/c₀ = 1.224 in this model.',
                         'summary_es': 'Une nervaduras SIMP (V/V₀ = 0.35) con 12.4 kg/m² de '
                                       'mineralización (CaO + CO₂ → CaCO₃) para lograr 39.40 kg '
                                       'CO₂e/m² y c/c₀ = 1.224 en este modelo.',
                         'roadblock_en': 'Full-scale ACI 318 / EN 1992 four-point destructive load '
                                         'testing and third-party ISO 14044 cradle-to-grave LCA '
                                         'review.',
                         'roadblock_es': 'Ensayos destructivos a escala real según ACI 318 / EN '
                                         '1992 y evaluación externa de ciclo de vida ISO 14044.'}],
 'toy_model_title_en': 'Try It in Your Head in 20 Seconds: Carving a 148 kg Floor Slab Under the '
                       '45 kg Target',
 'toy_model_title_es': 'Pruébalo en tu Cabeza en 20 Segundos: Esculpir una Losa de 148 kg Bajo la '
                       'Meta de 45 kg',
 'toy_model_en': 'Start with this folio\'s illustrative solid concrete slab: each square meter emits '
                 '148 kg of CO₂. This folio\'s design target is below 45 kg. Step 1 (Geometry): '
                 'Keep only 35% (V/V₀ = 0.35) in bone-like ribs. Multiply 148 kg × 0.35 = 51.80 kg '
                 'CO₂e/m². Geometry alone still exceeds the 45 kg target! Step 2 (Chemistry): '
                 'Model curing those ribs with 12.4 kg of CO₂ per square meter bound as calcium '
                 'carbonate. Subtract 51.80 − 12.40 = 39.40 kg CO₂e/m² (< 45 kg PASS!), while '
                 'modeled compliance rises to c/c₀ = 1.224 (< 1.35 limit).',
 'toy_model_es': 'Comienza con la losa maciza ilustrativa de este folio: cada metro cuadrado emite '
                 '148 kg de CO₂. La meta de diseño de este folio exige menos de 45 kg. Paso 1 '
                 '(Geometría): Conserva solo el 35% (V/V₀ = 0.35) en nervaduras tipo hueso. '
                 'Multiplica 148 kg × 0.35 = 51.80 kg CO₂e/m². ¡La geometría por sí sola aún rebasa '
                 'la meta de 45 kg! Paso 2 (Química): Modela el curado mineralizando 12.4 kg de '
                 'CO₂/m² como carbonato de calcio. Resta 51.80 − 12.40 = 39.40 kg CO₂e/m² (< 45 kg '
                 '¡APROBADO!), mientras la flexibilidad modelada es c/c₀ = 1.224 (< 1.35).',
 'act1_dropcap_es': 'La producción de cemento suele estimarse en hasta cerca del 8% de las emisiones '
                    'mundiales de dióxido de carbono (estimación sin fuente en este folio), y en '
                    'edificios de varios pisos las losas planas consumen gran parte del concreto '
                    'estructural (Küpfer et al., 2025, DOI 10.1088/1755-1315/1554/1/012083). Como '
                    'una losa maciza resiste la flexión cerca de sus caras superior e inferior, el '
                    'material cercano al eje neutro aporta poca rigidez.',
 'act1_body_es': 'Martin Bendsøe (1989, DOI 10.1007/bf01650949) y Ole Sigmund (2001, DOI '
                 '10.1007/s001580050176) formularon la optimización topológica SIMP, resoluble en '
                 'bibliotecas abiertas como FEniCS/dolfinx (Scroggs et al., 2022, DOI '
                 '10.1145/3524456). Penalizar densidades intermedias con p = 3 favorece nervaduras '
                 'alineadas con las trayectorias principales de Michell (1904, DOI '
                 '10.1080/14786440409463229). Si las nervaduras de concreto imprimible (Roussel, '
                 '2018, DOI 10.1016/j.cemconres.2018.04.005; Folio E.10) se combinan con '
                 'mineralización de carbonatos (CaO + CO₂ → CaCO₃), el carbono neto pasa en el '
                 'balance de masa de este folio de la línea base ilustrativa de 148.0 kg CO₂e/m² a '
                 '39.40 kg CO₂e/m², por debajo de su meta de diseño de 45.0 kg CO₂e/m². Esa meta no '
                 'es un criterio del XPRIZE Carbon Removal, y ninguna losa se ha construido ni '
                 'ensayado.',
 'act1_stakes_es': 'La fabricación de cemento suele estimarse cerca del ocho por ciento de las '
                   'emisiones globales de CO₂ (estimación sin fuente en este folio). En edificios '
                   'de varios niveles, las losas planas de concreto armado forman una gran parte de '
                   'la masa estructural y del carbono incorporado (Küpfer et al., 2025, DOI '
                   '10.1088/1755-1315/1554/1/012083). Cada tonelada adicional en un entrepiso '
                   'aumenta las cargas gravitacionales sobre columnas, muros y cimentaciones. Las '
                   'losas prismáticas se volvieron estándar por la sencillez de las cimbras planas, '
                   'aunque ingenieros desde Robert Maillart y Pier Luigi Nervi sabían que el '
                   'núcleo cercano al eje neutro soporta poco esfuerzo. La escala SCORS del '
                   'IStructE y el XPRIZE Carbon Removal pusieron el foco en el carbono incorporado y '
                   'removido; este folio fija su propia meta ilustrativa de 45 kg CO₂e/m², por '
                   'debajo de los 148.0 kg CO₂e/m² de su losa base, reduciendo un 65% la masa en el '
                   'modelo e incorporando mineralización de carbonatos.',
 'pullquote_es': 'El hueso adapta su densidad a las trayectorias de carga; la optimización '
                 'topológica SIMP modela losas de concreto con esa misma economía estructural.',
 'act2_intuition_es': 'En el modelo algebraico simplificado de este folio, retirar fracción '
                      'volumétrica V/V₀ respecto a la base de 148.0 kg CO₂e/m² reduce el carbono '
                      'como e_net = e₀(V/V₀) - m_CO₂, mientras la flexibilidad sustituta c/c₀ = 1 + '
                      '0.40(1 - V/V₀)^1.35 sube suavemente. En el punto de referencia V/V₀ = 0.35 '
                      '(65% menos volumen en la losa modelada) y m_CO₂ = 12.4 kg/m², c/c₀ = 1.224 '
                      '(< 1.35) y e_net = 39.40 kg CO₂e/m² (< 45.0).',
 'act2_analogy_es': 'Imagina un tronco macizo frente al cuadro de una bicicleta de carreras. El '
                    'tronco sostiene peso, pero gran parte de la madera interior siente poco '
                    'esfuerzo; la bicicleta canaliza cargas por tubos esbeltos. En el modelo de '
                    'este folio, la losa base ilustrativa emite 148.0 kg CO₂e/m². El parámetro '
                    'V/V₀ recorta volumen hasta dejar 0.35 (35%), mientras la flexibilidad '
                    'modelada sube a 1.224 (< 1.35). Por último, el curado por carbonatación modela '
                    'fijar 12.4 kg CO₂e/m² como carbonato de calcio sólido, bajando las emisiones '
                    'netas modeladas a 39.40 kg CO₂e/m².',
 'act2_plain_primer_es': 'Antes de revisar las ecuaciones de elementos finitos, explora los dos '
                         'controles interactivos de nuestro banco de pruebas en el Acto III para '
                         'ver cómo colaboran la geometría y la química. El primer control ajusta '
                         'la Fracción Volumétrica SIMP (V/V₀), permitiéndote elegir cuánto '
                         'concreto conservas desde el 70% hasta el 20%. En nuestro punto de '
                         'referencia de 35% (0.35), eliminas casi dos tercios de la masa total '
                         'conservando una rigidez adecuada en el modelo. Si arrastras este control '
                         'demasiado a la izquierda, la losa se vuelve más flexible; si lo '
                         'empujas a la derecha, se vuelve más rígida pero rebasa el presupuesto de '
                         'carbono. El segundo control regula la Absorción de CO₂ Mineralizado '
                         '(m_CO₂), fijando cuántos kilogramos de gas capturado se mineralizan en '
                         'calcita por metro cuadrado durante el curado. Finalmente, pulsa el '
                         'botón [⚡ Counterfactual Axiom-Knockout]: esto simula qué ocurre si la '
                         'planta de prefabricados omite la cámara de mineralización (m_CO₂ = 0). '
                         'De inmediato, el carbono neto salta de 39.40 a 51.80 kg CO₂e/m², '
                         'reprobando el umbral de 45 kg CO₂e/m² y mostrando por qué topología y '
                         'mineralización deben actuar juntas.',
 'act2_deepening_es': 'La formulación matemática de la optimización topológica SIMP aborda la '
                      'paradoja de retirar masa sin provocar deflexiones estructurales excesivas. '
                      'Sobre el dominio continuo del tablero de piso Ω, la distribución de '
                      'material se discretiza en elementos finitos, cada uno con una densidad '
                      'relativa continua ρ_e acotada entre cero y uno. Martin Bendsøe y Ole '
                      'Sigmund mostraron que penalizar el módulo de Young mediante la ley de '
                      'potencias E(ρ_e) = E_min + ρ_e^p (E_0 - E_min) con exponente p = 3 vuelve '
                      'ineficientes las densidades intermedias: un elemento a mitad de densidad '
                      'aporta apenas el 12.5% de la rigidez elástica para el 50% de la masa. '
                      'Impulsado por un solucionador adjunto de sensibilidades con filtro de '
                      'Helmholtz de radio r_min para suprimir el damero numérico, el algoritmo '
                      'converge hacia nervaduras binarias nítidas que siguen las líneas '
                      'principales de esfuerzo de Michell. Sobre esta curva sustituta, la '
                      'flexibilidad normalizada escala como c/c₀ = 1.0 + 0.40(1 - V/V₀)^1.35. En '
                      'V/V₀ = 0.35, la flexibilidad alcanza 1.224 (< 1.35). En el balance ambiental, '
                      'las emisiones siguen e_net = e₀(V/V₀) - m_CO₂: al partir de 148.0 kg '
                      'CO₂e/m², aligerar al 35% baja la huella a 51.80 kg CO₂e/m², y la '
                      'carbonatación en cámara (Ca(OH)₂ + CO₂ → CaCO₃ + H₂O) secuestra m_CO₂ = '
                      '12.4 kg/m² para alcanzar 39.40 kg CO₂e/m².',
 'act4_human_ai_es': 'El desarrollo de componentes estructurales de bajo carbono exige un ciclo de '
                     'codiseño entre ingenieros humanos y herramientas abiertas. El ingeniero '
                     'define claros entre columnas, pasos de instalaciones, condiciones de apoyo '
                     'y combinaciones de carga (1.2D + 1.6L). Bibliotecas abiertas como '
                     'FEniCS/dolfinx permiten ensamblar formas variacionales y sensibilidades '
                     'adjuntas para nervaduras SIMP, mientras scripts en Python auditan el balance '
                     'de carbono y la cota de flexibilidad sin depender de cajas negras '
                     'propietarias.',
 'act4_deepening_es': 'Las afirmaciones en construcción sostenible suelen carecer de cifras '
                      'auditables. El Folio B.03 coloca sus dos desigualdades modelo en un script '
                      'abierto de Python (bounties/bounty_e1_simp_carbon_slab.py) que se ejecuta '
                      'sin conexión ni dependencias. El arnés evalúa el carbono neto e_net = '
                      '148.0(V/V₀) - m_CO₂ frente a 45.0 kg CO₂e/m² y la flexibilidad sustituta '
                      'c/c₀ = 1.0 + 0.40(1 - V/V₀)^1.35 frente a 1.35. Omitir el curado '
                      'mineralizado (m_CO₂ = 0.0 con V/V₀ = 0.35) eleva e_net a 51.80 kg CO₂e/m² '
                      '(FAIL); subir V/V₀ a 0.50 con m_CO₂ = 12.4 da 61.60 kg CO₂e/m² (FAIL). El '
                      'script aún no tiene modo de defecto plantado ni análisis de elementos '
                      'finitos, por lo que cualquier obra real requeriría ensayos físicos.',
 'sidenote_1_es': {'kicker': 'NOTA AL MARGEN B.03-A · POR QUÉ FUNCIONA LA PENALIZACIÓN p = 3',
                   'body': 'Con p = 3, una densidad intermedia ρ = 0.5 proporciona solo el 12.5% '
                           'de la rigidez sólida por el 50% de la masa, empujando al optimizador a '
                           'esculpir nervaduras nítidas 0/1 (Bendsøe & Sigmund, 1999, DOI '
                           '10.1007/s004190050248).'},
 'sidenote_2_es': {'kicker': 'NOTA AL MARGEN B.03-B · QUÍMICA DE LA MINERALIZACIÓN',
                   'body': 'En este modelo, el curado por carbonatación (Ca(OH)₂ + CO₂ → CaCO₃ + '
                           'H₂O) representa un parámetro ilustrativo m_CO₂ = 12.4 kg CO₂e/m²; la '
                           'resistencia y absorción reales dependen de mediciones en mezcla.'},
 'walkthrough_es': ['Inspecciona el punto de referencia en V/V₀ = 0.35 y m_CO₂ = 12.4 kg/m²: el '
                    'carbono neto es 39.40 kg CO₂e/m² (< 45.0) y la razón de flexibilidad es 1.224 '
                    '(< 1.35) (APROBADO).',
                    'Arrastra la Fracción Volumétrica V/V₀ hasta 0.50: observa cómo baja la '
                    'flexibilidad modelada a 1.157 mientras el carbono neto salta a 61.60 kg '
                    'CO₂e/m², rebasando la meta de 45.0 kg CO₂e/m².',
                    'Ajusta la Absorción de CO₂ Mineralizado m_CO₂ = 0.0 kg/m² (o pulsa [⚡ '
                    'Counterfactual Axiom-Knockout]): observa cómo el cemento sin mineralizar en '
                    'V/V₀ = 0.35 llega a 51.80 kg CO₂e/m², mostrando por qué ambos términos son '
                    'necesarios en el modelo.'],
 'steps_es': ['Etapa Conceptual 1 (Contexto SIMP, no ejecutado en script): Ensamblaje de '
              'elasticidad lineal K(ρ) u = f en Ω (como en FEniCS/dolfinx, DOI 10.1145/3524456).',
              'Etapa Conceptual 2 (Contexto SIMP, no ejecutado en script): Penalización E(ρ_e) con '
              'p = 3 y filtro de sensibilidad ∂c/∂ρ_e (Bendsøe 1989; Sigmund 2001, DOI '
              '10.1007/s001580050176).',
              'Etapa Conceptual 3 y Cota Sustituta: En V/V₀ = 0.35, la curva sustituta da c/c₀ = '
              '1.0 + 0.40(1 - 0.35)^1.35 = 1.224 < 1.35.',
              'Etapa 4 (Evaluada por el Arnés): Resta el parámetro ilustrativo m_CO₂ = 12.4 kg '
              'CO₂e/m² de 148.0 × 0.35 = 51.80 para obtener e_net = 39.40 kg CO₂e/m² < 45.0.'],
 'rules_es': ['Techo de Carbono Incorporado (meta de diseño del folio): El carbono incorporado neto de '
              'cuna a puerta e_net = 148.0(V/V₀) - m_CO₂ debe mantenerse estrictamente por debajo '
              'de 45.0 kg CO₂e/m².',
              'Cota de Flexibilidad Normalizada (meta del modelo): La flexibilidad sustituta c/c₀ = '
              '1.0 + 0.40(1 - V/V₀)^1.35 debe mantenerse estrictamente por debajo de 1.35.',
              'Ventana del Modelo en el Banco de Pruebas: Con m_CO₂ = 12.4 kg/m², mantener e_net < '
              '45.0 kg CO₂e/m² exige V/V₀ < 0.3878 (hasta 0.38 en el deslizador de paso 0.01). En '
              'todo el rango [0.20, 0.70], c/c₀ es como máximo 1.296 (en V/V₀ = 0.20); en la curva '
              'algebraica sustituta, c/c₀ alcanza 1.35 solo por debajo de V/V₀ ≈ 0.0942.'],
 't0_t1_certified_es': ['Modelo algebraico de flexibilidad y carbono en '
                        'bounties/bounty_e1_simp_carbon_slab.py (tiempo de ejecución < 0.05 s; sin '
                        'solucionador de malla ni modo de defecto plantado aún).',
                        'Referencias de formulación SIMP: FEniCS/dolfinx (Scroggs et al., 2022, '
                        'DOI 10.1145/3524456) y Sigmund (2001, DOI 10.1007/s001580050176).'],
 't2_t3_open_horizon_es': ['XPRIZE Carbon Removal ($100M, concluido en abril de 2025) e IStructE '
                           'Structural Awards (solo obras construidas): cualquier afirmación real '
                           'sobre una losa requeriría ensayos físicos de carga a escala real hasta '
                           'la falla (flexión en cuatro puntos según ACI 318 / EN 1992-1-1) y '
                           'evaluación de análisis de ciclo de vida ISO 14040/14044 por terceros.']}
