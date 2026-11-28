# -*- coding: utf-8 -*-
"""Open Bounties — Folio B.06: Machine-Checked Gauge Physics in PhysLean & Tensor-Network Quantum Criticality (ITensors.jl + NetKet)."""


FOLIO = {'slug': 'b06',
 'folio_id': 'B.06',
 'bounty_id': 'BOUNTY-M2',
 'cat': 'math',
 'plate_slug': 'b06',
 'pillar_label_en': 'Math & Quantum · Lean 4 Gauge Physics & Tensor Networks',
 'pillar_label_es': 'Matemáticas y Cuántica · Física Gauge en Lean 4 y Redes Tensoriales',
 'badge_en': 'GRAND CHALLENGE B.06 (M-2) · PHYSLEAN (ACTIVE PRs) + ITENSORS + NETKET',
 'badge_es': 'GRAN RETO B.06 (M-2) · PHYSLEAN (PRs ACTIVOS) + ITENSORS + NETKET',
 'title': 'Machine-Checked Gauge Physics in PhysLean & Tensor-Network Quantum Criticality '
          '(ITensors.jl + NetKet)',
 'title_es': 'Física Gauge Verificada en PhysLean y Criticidad Cuántica con Redes Tensoriales '
             '(ITensors.jl + NetKet)',
 'subtitle': 'What the HEPLean/PhysLean repository states about formalizing Standard Model '
             'U(1)_Y × SU(2)_L × SU(3)_C chiral anomaly cancellation in Lean 4, beside the critical '
             'entanglement-entropy bounds that tools such as ITensors.jl and NetKet are used to study.',
 'subtitle_es': 'Lo que el repositorio HEPLean/PhysLean afirma sobre la formalización en Lean 4 '
                'de la cancelación de anomalías quirales U(1)_Y × SU(2)_L × SU(3)_C del Modelo Estándar, junto a las cotas de '
                'entropía de entrelazamiento crítico que se estudian con herramientas como '
                'ITensors.jl y NetKet.',
 'why_en': 'Why does the electric charge of a proton balance the charge of an electron, even '
           'though quarks carry fractional charges of +2/3 and -1/3? In the Standard Model, quantum '
           'gauge invariance requires four anomaly traces—including the cubic hypercharge sum '
           '∑ d_f Y_f³—to vanish, an algebraic identity encoded in Lean 4 via PhysLean '
           '(Tooby-Smith, 2025, DOI 10.1016/j.cpc.2024.109457).',
 'why_es': '¿Por qué la carga eléctrica del protón compensa la del electrón aunque los quarks '
           'tengan cargas fraccionarias +2/3 y -1/3? En el Modelo Estándar, la invariancia gauge '
           'cuántica exige que cuatro trazas de anomalía—incluida la suma cúbica ∑ d_f Y_f³—se '
           'anulen, una identidad algebraica codificada en Lean 4 mediante PhysLean (Tooby-Smith, '
           '2025, DOI 10.1016/j.cpc.2024.109457).',
 'governing_law': 'Tr[Y] = Tr[Y³] = Tr[τ²Y] = Tr[λ²Y] = 0 · S_vN(L) = (c/6) ln(L) + s_1 = 0.8828 ≤ '
                  'ln(χ = 64) = 4.1589',
 'pass_pill_en': 'PASS · Tr[Y³] = 0 · S_vN = 0.883 ≤ ln(64)',
 'pass_pill_es': 'APROBADO · Tr[Y³] = 0 · S_vN = 0.883 ≤ ln(64)',
 'verifier_script': 'bounties/bounty_m2_physlean_itensor_quantum_gauge.py',
 'skill_dir': 'skills/bounties/b06',
 'skill_name': 'bounty-b06-physlean-itensor-quantum-gauge',
 'primary_doi': '10.1016/j.cpc.2024.109457',
 'scite_summary': 'Tooby-Smith (2025) HepLean/PhysLean formalization in Lean 4 and Fishman, White '
                  '& Stoudenmire (2022) ITensors.jl checked against Crossref and Scite.',
 'date_published': '2026-11-04',
 'date_redated': '2026-11-15',
 'current_edition': 'REV 1.3',
 'reading_time': '15 MIN READ',
 'companion_folios': [('math',
                       'm01',
                       'Folio M.01',
                       "Fermat's Last Theorem in Lean 4 & Modularity Lifting"),
                      ('physics',
                       'p11',
                       'Folio P.11',
                       'Surface-Code Quantum Error Correction & FeMoCo Catalysis'),
                      ('math',
                       'm11',
                       'Folio M.11',
                       '3D Kakeya Conjecture & Guth–Maynard 30/13 Zero Bounds'),
                      ('math',
                       'm12',
                       'Folio M.12',
                       'Anthropic Lean 4 Complexity & Post-Quantum Lattices')],
 'external_links': [('HEPLean/PhysLean (Lean 4 Physics)', 'https://github.com/HEPLean/PhysLean'),
                    ('itensor/ITensors.jl (MPS / DMRG)', 'https://github.com/itensor/ITensors.jl'),
                    ('netket/netket (Neural Quantum States)', 'https://github.com/netket/netket'),
                    ('qutip/qutip (Open Quantum Systems)', 'https://github.com/qutip/qutip')],
 'act1_dropcap': 'In quantum field theory, a symmetry of the classical Lagrangian does not '
                 'automatically survive quantization: one-loop triangle diagrams coupling '
                 'three chiral gauge currents can break gauge invariance unless the fermion '
                 'hypercharges satisfy four algebraic trace identities. In a single generation of '
                 'the Standard Model, fifteen Weyl multiplets—left-handed quark doublets Q_L '
                 '(3, 2, 1/6), right-handed up and down singlets u_R^c (3̄, 1, -2/3) and d_R^c '
                 '(3̄, 1, 1/3), left-handed lepton doublets L_L (1, 2, -1/2), and right-handed '
                 'positrons e_R^c (1, 1, 1)—make the gravitational, mixed non-Abelian, and cubic '
                 'hypercharge traces vanish.',
 'act1_body': "Joseph Tooby-Smith's HEPLean / PhysLean library (2025, DOI 10.1016/j.cpc.2024.109457) "
              'formalizes Standard Model anomaly cancellation, Lorentz groups, Maxwell '
              "electrodynamics, and Wick's theorem in Lean 4 (as described by its author). "
              "Paired with Matthew Fishman, Steven White, and Miles Stoudenmire's ITensors.jl "
              '(2022, DOI 10.21468/SciPostPhysCodeb.4) and Giuseppe Carleo and Filippo '
              "Vicentini's NetKet (2022, DOI 10.21468/SciPostPhysCodeb.7), this folio's Python "
              'harness evaluates those four anomaly traces and the Calabrese–Cardy scaling '
              'relation S_vN(L) = (c/6) ln(L) + s_1 ≤ ln(χ) for the 1D critical Transverse-Field '
              'Ising Model (c = 1/2, E₀/N = -4/π = -1.27323954).',
 'pullquote': '6(1/6)³ + 3(-2/3)³ + 3(1/3)³ + 2(-1/2)³ + 1(1)³ = 0: one line of rational '
              'arithmetic in Lean 4 matches electric charge neutrality in atoms.',
 'chronology': [('1969',
                 'Stephen Adler, John Bell, and Roman Jackiw identify chiral triangle anomalies in '
                 'quantum electrodynamics.'),
                ('1970',
                 'Pierre Pfeuty solves the 1D Transverse-Field Quantum Ising Model, giving '
                 'critical ground-state energy density E₀/N = -4/π.'),
                ('1992–2004',
                 'Steven White introduces DMRG; Pasquale Calabrese and John Cardy derive CFT '
                 'entanglement scaling S_vN(L) = (c/6) ln(L) + s_1 (DOI '
                 '10.1088/1742-5468/2004/06/P06002).'),
                ('2022–2026',
                 'ITensors.jl (DOI 10.21468/SciPostPhysCodeb.4), NetKet 3 (DOI '
                 '10.21468/SciPostPhysCodeb.7), and HEPLean/PhysLean in Lean 4 (Tooby-Smith, '
                 '2025, DOI 10.1016/j.cpc.2024.109457) connect tensor networks with formal proof '
                 'assistants.')],
 'act2_intuition': 'Why do Matrix Product States (MPS) in ITensors.jl represent 1D critical chains '
                   'compactly? A bond of dimension χ between two halves of a chain carries at '
                   'most ln(χ) nats of von Neumann entanglement entropy. At c = 1/2, length L = '
                   '128, and illustrative offset s_1 = 0.4785, S_vN(128) = (0.5/6) ln(128) + '
                   '0.4785 = 0.8828 nats—captured by χ = 64 (ln 64 = 4.1589 nats), whereas a '
                   'product state (χ = 1, ln 1 = 0) captures no entanglement.',
 'sliders': [{'id': 'tp-bounty-s0',
              'label': 'MPS Bond Dimension χ (ITensors.jl)',
              'min': 1,
              'max': 128,
              'step': 1,
              'value': 64,
              'unit': 'χ = '},
             {'id': 'tp-bounty-s1',
              'label': 'Hypercharge Perturbation δY (PhysLean)',
              'min': 0.0,
              'max': 0.2,
              'step': 0.01,
              'value': 0.0,
              'unit': 'δY = '}],
 'readouts': [{'label': 'PhysLean Cubic Trace Tr[Y³]', 'value': '0.000000000000 (Anomaly-Free)'},
              {'label': 'Critical TFIM Energy E₀ / N', 'value': '−1.27323954 (−4 / π exact)'},
              {'label': 'CFT Entanglement S_vN(128)', 'value': '0.8828 nats ≤ ln(χ) = 4.1589'},
              {'label': 'Verifier Verdict (Worked Example)', 'value': 'PASS · ANOMALY-FREE & AREA-LAW'}],
 'steps': ['Stage 1 (Multiplet Table in Harness): Encode the five SU(3)_C × SU(2)_L × U(1)_Y '
           'Weyl multiplets per generation (PhysLean, DOI 10.1016/j.cpc.2024.109457): '
           'Q_L(3,2,1/6), u_R^c(3,1,-2/3), d_R^c(3,1,1/3), L_L(1,2,-1/2), e_R^c(1,1,1).',
           'Stage 2 (Four-Trace Anomaly Sum in Harness): Evaluate Tr[Y], Tr[Y³], Tr[τ²Y], and '
           'Tr[λ²Y] in Python floating-point arithmetic (< 10⁻¹² tolerance; PhysLean reports the '
           'rational check over ℚ in Lean 4).',
           'Stage 3 (Pfeuty & Calabrese–Cardy Formulas in Harness): Evaluate E₀/N = -4/π = '
           '-1.27323954 and S_vN(L=128) = (0.5/6) ln(128) + 0.4785 = 0.882836 nats (illustrative '
           's_1 = 0.4785).',
           'Stage 4 (MPS Bond-Capacity Check): Check that MPS bond capacity ln(χ) = ln(64) = '
           '4.158883 nats bounds S_vN(128) = 0.882836 nats.'],
 'rules': ['Standard Model Gauge Anomaly Cancellation: All four chiral trace invariants '
           '(gravitational Tr[Y], cubic U(1)_Y³ Tr[Y³], weak mixed Tr[τ²Y], and color mixed '
           'Tr[λ²Y]) must vanish identically (|Tr| < 10⁻¹²); any hypercharge drift δY ≠ 0 breaks '
           'quantum gauge invariance.',
           'Calabrese–Cardy Entanglement Bound: To faithfully represent the critical Ising ground '
           'state at chain length L = 128 (c = 0.5, S_vN = 0.882836 nats), the MPS bond dimension '
           'must satisfy ln(χ) ≥ S_vN(L), i.e., χ ≥ 3.',
           'Pfeuty Ground-State Energy Invariant: Critical TFIM energy per site at g = J = 1 must '
           'equal -4/π = -1.27323954.'],
 'sidenote_1': {'kicker': 'SIDENOTE B.06-A · KNOCKING OUT COLOR N_c = 3',
                'body': 'If quarks did not come in N_c = 3 colors, the weak mixed trace 2 N_c(1/6) '
                        '+ 2(-1/2) = (N_c - 3)/3 would fail to vanish: with the hypercharges held at their observed values, lepton-quark anomaly cancellation requires three colors.'},
 'sidenote_2': {'kicker': 'SIDENOTE B.06-B · AREA LAW VS. VOLUME LAW',
                'body': 'Gapped 1D ground states obey an area law S_vN = O(1), while 1D conformal '
                        'critical points grow only logarithmically as (c/6) ln(L), allowing '
                        'polynomial-time DMRG compression.'},
 'walkthrough': ['Verify the canonical benchmark at χ = 64 and δY = 0.00: Tr[Y³] = 0.0, E₀/N = '
                 '-1.273240, and S_vN(128) = 0.8828 ≤ ln(64) = 4.1589 (PASS).',
                 'Perturb Hypercharge δY away from 0.00 (or click [⚡ Counterfactual '
                 'Axiom-Knockout]): watch the cubic gauge anomaly Tr[Y³] become non-zero, breaking '
                 'U(1)_Y quantum consistency.',
                 'Drag MPS Bond Dimension χ down to 1 or 2: observe ln(χ) drop below S_vN(128) = '
                 '0.8828 nats, triggering a bond-dimension truncation failure.'],
 't0_t1_certified': ['Algebraic Standard Model four-trace anomaly and 1D critical TFIM scaling '
                     'harness in bounties/bounty_m2_physlean_itensor_quantum_gauge.py (< 0.05s '
                     'runtime; no Lean 4 execution or planted-defect mode yet).',
                     'Primary references checked: Tooby-Smith (2025, DOI '
                     '10.1016/j.cpc.2024.109457), Fishman et al. (2022, DOI '
                     '10.21468/SciPostPhysCodeb.4), and Vicentini et al. (2022, DOI '
                     '10.21468/SciPostPhysCodeb.7).'],
 't2_t3_open_horizon': ['HEPLean / PhysLean active open-source formalization (pull requests welcome; '
                        'no cash prize): submitting Lean 4 pull requests formalizing '
                        'renormalization group flows, lattice gauge bounds, or BSM anomaly '
                        'classification directly to HEPLean/PhysLean.'],
 'sources': ['Tooby-Smith, J. (2025). HepLean: Digitalising high energy physics. Computer Physics '
             'Communications, 308, 109457. DOI 10.1016/j.cpc.2024.109457',
             'Fishman, M., White, S. R., & Stoudenmire, E. M. (2022). The ITensor Software Library '
             'for Tensor Network Calculations. SciPost Physics Codebases, 4. DOI '
             '10.21468/SciPostPhysCodeb.4',
             'Vicentini, F., et al. (2022). NetKet 3: Machine Learning Toolbox for Many-Body '
             'Quantum Systems. SciPost Physics Codebases, 7. DOI 10.21468/SciPostPhysCodeb.7',
             'Calabrese, P., & Cardy, J. (2004). Entanglement entropy and quantum field theory. '
             'Journal of Statistical Mechanics: Theory and Experiment, 2004(06), P06002. DOI '
             '10.1088/1742-5468/2004/06/P06002'],
 'act1_plain_bridge': 'A proton inside an atomic nucleus contains three quarks carrying '
                      'fractional electric charges of +2/3 or -1/3, while an electron orbits outside '
                      'with negative unit charge. Yet the proton and electron charges are equal and '
                      'opposite. In the Standard Model, that cancellation is tied to mathematical '
                      'consistency: if fermion hypercharges did not sum to zero across four '
                      'algebraic trace equations, one-loop quantum corrections could break gauge '
                      'invariance. Separately, when many quantum spins interact along a chain, '
                      'storing all states grows exponentially with system size. Tensor networks '
                      'like Matrix Product States organize the chain with a fixed bond capacity so '
                      'critical 1D entanglement fits within manageable memory.',
 'act1_stakes': 'In 1969, Stephen Adler, John Bell, and Roman Jackiw showed that one-loop '
                'triangle diagrams may break classical chiral symmetries in quantum '
                'electrodynamics. In the Standard Model, fifteen Weyl fermion multiplets per '
                'generation make four anomaly traces—including the cubic hypercharge sum ∑ d_f '
                'Y_f^3—vanish; holding the observed hypercharges fixed, lepton-quark '
                'cancellation requires N_c = 3 quark colors. Joseph Tooby-Smith’s HEPLean / '
                'PhysLean library (2025, DOI 10.1016/j.cpc.2024.109457) encodes these anomaly '
                'identities in Lean 4 (as described by its author; not verified here). In '
                'parallel, simulating N interacting spins faces an exponential 2^N Hilbert space; '
                'Steven White’s DMRG, ITensors.jl (DOI 10.21468/SciPostPhysCodeb.4), and NetKet '
                '(DOI 10.21468/SciPostPhysCodeb.7) use Matrix Product States along 1D chains '
                'where Calabrese–Cardy entanglement grows logarithmically with chain length.',
 'act2_analogy': 'Picture a delicate suspension bridge suspended between two sheer canyon walls. '
                 'To keep the road completely level without snapping cables, the bridge relies on '
                 'two distinct structural principles. First, the vertical suspension cables must '
                 'achieve perfect mechanical counterbalancing. Every heavy truck and steel girder '
                 'on the left side of the bridge must be matched by an exact counterweight on the '
                 'right side across four distinct balance scales: total linear weight (Tr[Y]), '
                 'twisting torque (Tr[Y^3]), torsional cable pull (Tr[τ^2 Y]), and crossbeam sway '
                 '(Tr[λ^2 Y]). If even a tiny weight perturbation δY shifts by a single gram, '
                 'twisting torque unbalances the deck and tears the suspension apart. Second, '
                 'consider the communication network running along the bridge deck, connecting '
                 'hundreds of sensors. Instead of running a separate, thick cable from every '
                 'single sensor to every other sensor (which would create an impossibly heavy, '
                 'tangled mess of wires), engineers install a neat digital data pipeline with a '
                 'fixed channel bandwidth χ. The total volume of information flowing across the '
                 'center of the bridge represents the quantum entanglement entropy S_vN. As long '
                 'as the digital pipeline capacity ln(χ) exceeds the message traffic S_vN, signals '
                 'transmit instantly with zero loss, keeping the bridge stable and fully '
                 'monitored.',
 'act2_plain_primer': 'The interactive workbench places two controls in your hands. The first slider '
                      'sets MPS Bond Dimension χ (1 to 128); at χ = 64, ln(64) is approximately '
                      '4.16 nats, above the 0.8828 nats of the L = 128 model. The second slider '
                      'sets Hypercharge Perturbation δY (0.0 to 0.2), shifting the quark doublet '
                      'Q_L hypercharge. At δY = 0.00, all four chiral anomaly traces vanish to '
                      'machine precision. Pushing δY above zero makes Tr[Y^3] nonzero and triggers '
                      'an anomaly alert; dropping χ to 1 or 2 lowers ln(χ) below 0.8828 nats and '
                      'triggers a truncation alert.',
 'distill_diagram': {'analogy_title': 'Suspension Bridge Cable Balance',
                     'analogy_sub': 'Balanced weights preserve bridge equilibrium while data '
                                    'channels carry traffic.',
                     'force_a_title': 'Hypercharge Trace Drift (δY)',
                     'force_a_sub': 'Shifts fermion hypercharge, breaking cubic gauge anomaly '
                                    'cancellation.',
                     'force_b_title': 'MPS Bond Capacity (ln χ)',
                     'force_b_sub': 'Bounds quantum entanglement entropy across critical 1D '
                                    'chains.',
                     'threshold_title': 'Area-Law Capacity (ln χ ≥ S_vN)',
                     'threshold_eq': 'Tr[Y³] = 0 · S_vN(128) = 0.8828 ≤ ln(χ) = 4.1589',
                     'threshold_sub': 'Tracks anomaly-free gauge traces and bounded tensor '
                                      'capacity.',
                     'threshold_pass': 'Tr[Y³] = 0 (anomaly-free) & S_vN(128) = 0.883 ≤ ln(64) = '
                                       '4.159 nats.',
                     'threshold_fail': 'Anomaly: δY > 0 breaks Tr[Y³] = 0; Truncation: χ < 3 fails '
                                       'S_vN bound.',
                     'caption': 'Plate B.06-D diagrams the two halves of the folio model: '
                                'algebraic cancellation of chiral gauge anomalies and '
                                'logarithmic area-law entanglement bounds in MPS representations.'},
 'act2_deepening': 'Folio B.06 pairs rational gauge-anomaly algebra with 1D critical entanglement '
                   'bounds. For each Standard Model generation, fifteen Weyl fields transform '
                   'under SU(3)_C × SU(2)_L × U(1)_Y: Q_L(3,2,1/6), u_R^c(3̄,1,-2/3), '
                   'd_R^c(3̄,1,1/3), L_L(1,2,-1/2), and e_R^c(1,1,1). In Tooby-Smith’s PhysLean '
                   'library (2025, DOI 10.1016/j.cpc.2024.109457), anomaly cancellation is '
                   'encoded over ℚ; this folio checks the four traces in Python: Tr[Y] = 0, '
                   'Tr[τ^2 Y] = 0, Tr[λ^2 Y] = 0, and Tr[Y^3] = 6(1/6)^3 + 3(-2/3)^3 + 3(1/3)^3 + '
                   '2(-1/2)^3 + 1(1)^3 = 0. Holding observed hypercharges fixed, N_c ≠ 3 would '
                   'yield (N_c - 3)/3 ≠ 0. In the many-body sector, Pfeuty’s solution of the 1D '
                   'critical Transverse-Field Ising Model (g = J = 1) gives E_0 / N = -4/π = '
                   '-1.27323954, and Calabrese–Cardy scaling (c = 1/2, DOI '
                   '10.1088/1742-5468/2004/06/P06002) with illustrative offset s_1 = 0.4785 gives '
                   'S_vN(128) = (0.5/6) ln(128) + 0.4785 = 0.8828 nats, below the χ = 64 MPS '
                   'bond capacity ln(64) = 4.1589 nats.',
 'act4_human_ai': 'Lean 4 libraries such as HEPLean / PhysLean (Tooby-Smith, 2025, DOI '
                  '10.1016/j.cpc.2024.109457) let physicists check rational hypercharge identities '
                  'with tactics like norm_num and ring, while ITensors.jl (DOI '
                  '10.21468/SciPostPhysCodeb.4) and NetKet (DOI 10.21468/SciPostPhysCodeb.7) '
                  'optimize Matrix Product States and neural quantum states numerically. Human '
                  'researchers still choose the gauge groups, symmetry assumptions, and physical '
                  'interpretations, while proof assistants and tensor libraries may catch '
                  'algebraic sign slips and bond-capacity overflows.',
 'act4_deepening': 'The standalone script bounties/bounty_m2_physlean_itensor_quantum_gauge.py '
                   'runs in under 0.05 seconds using only the Python standard library. Under the '
                   'stated assumptions, it encodes the five Standard Model Weyl multiplets per '
                   'generation, evaluates the four chiral traces in floating-point arithmetic (< '
                   '10^{-12} tolerance), and checks Pfeuty’s E_0 / N = -4/π and S_vN(128) = '
                   '0.882836 ≤ ln(64) = 4.158883 nats. It does not execute Lean 4 or ITensors.jl '
                   'directly and does not yet implement a --planted-defect CLI mode; counterfactual '
                   'perturbations (δY > 0 and χ < 3) are explored live in the Act III interactive '
                   'workbench above.',
 'plain_es': 'Un protón en el núcleo atómico contiene tres quarks con cargas fraccionarias de '
             '+2/3 o -1/3, mientras que un electrón orbita con carga -1, y ambas cargas se '
             'compensan con igual magnitud y signo opuesto. En el Modelo Estándar, ese balance '
             'corresponde a cuatro ecuaciones algebraicas de hipercarga cuya suma se anula para '
             'evitar anomalías cuánticas. Por otro lado, al simular cadenas de muchos espines '
             'cuánticos, los estados totales crecen exponencialmente; las redes tensoriales '
             'como los Estados de Producto Matricial (MPS) acotan el enlace entre mitades de la '
             'cadena para capturar el entrelazamiento crítico en memoria polinomial.',
 'deep_es': 'En cada generación del Modelo Estándar, quince campos quirales de Weyl bajo SU(3)_C '
            '× SU(2)_L × U(1)_Y anulan las cuatro trazas de anomalía Tr[Y], Tr[τ^2 Y], Tr[λ^2 Y] '
            'y Tr[Y^3] = 0; con las hipercargas observadas fijas, esa cancelación requiere N_c = '
            '3 colores (PhysLean, DOI 10.1016/j.cpc.2024.109457). En paralelo, la cadena '
            'crítica de Ising 1D (c = 1/2, E₀/N = -4/π) sigue la ley de Calabrese–Cardy '
            'S_vN(128) = 0.8828 nats (con desplazamiento ilustrativo s_1 = 0.4785), acotada '
            'por la capacidad de enlace ln(64) = 4.1589 nats de un estado MPS (ITensors.jl, DOI '
            '10.21468/SciPostPhysCodeb.4).',
 'easy_history_title_en': 'How Human Pioneers Reached This Frontier: From 1969 Triangle Anomalies '
                          '& DMRG Chains to PhysLean in Lean 4',
 'easy_history_title_es': 'Cómo los Pioneros Humanos Llegaron a Esta Frontera: De las Anomalías '
                          'Triangulares de 1969 y DMRG a PhysLean en Lean 4',
 'easy_history_en': 'In 1969, Stephen Adler, John Bell, and Roman Jackiw identified a trap in '
                    'quantum field theory: virtual fermion triangle loops can break classical '
                    'gauge symmetries and spoil unitarity unless anomaly sums vanish. In the '
                    'Standard Model, each generation has 15 chiral fermion fields with hypercharges '
                    '+1/6, −2/3, +1/3, −1/2, and +1; when quarks come in three colors, the cubed '
                    'sum vanishes: 6(1/6)³ + 3(−2/3)³ + 3(1/3)³ + 2(−1/2)³ + 1(1)³ = 0, matching '
                    'proton–electron charge balance.\n'
                    '\n'
                    'In condensed-matter physics, simulating N entangled spins needs 2^N numbers, '
                    'which outgrows memory past small N. In 1992, Steven White introduced DMRG, and '
                    'in 2004 Pasquale Calabrese and John Cardy derived logarithmic entanglement '
                    'scaling S_vN(L) = (c/6) ln(L) + s₁ for critical 1D chains (DOI '
                    '10.1088/1742-5468/2004/06/P06002). Joseph Tooby-Smith’s HEPLean / PhysLean '
                    'library (2025, DOI 10.1016/j.cpc.2024.109457) encodes Standard Model anomaly '
                    'cancellation in Lean 4 (as its author describes it; not re-checked here), '
                    'while ITensors.jl (DOI 10.21468/SciPostPhysCodeb.4) and NetKet (DOI '
                    '10.21468/SciPostPhysCodeb.7) model critical chains with tensor networks.',
 'easy_history_es': 'En 1969, Stephen Adler, John Bell y Roman Jackiw identificaron una trampa en '
                    'la teoría cuántica de campos: los lazos triangulares de fermiones pueden '
                    'romper simetrías clásicas de norma si las sumas de anomalía no se anulan. En '
                    'el Modelo Estándar, cada generación contiene 15 campos de fermiones quirales '
                    'con hipercargas +1/6, −2/3, +1/3, −1/2 y +1; con tres colores de quark, la '
                    'suma cúbica se anula: 6(1/6)³ + 3(−2/3)³ + 3(1/3)³ + 2(−1/2)³ + 1(1)³ = 0, en '
                    'concordancia con el equilibrio de carga entre protón y electrón.\n'
                    '\n'
                    'En física de muchos cuerpos, simular N espines requiere 2^N amplitudes. En '
                    '1992, Steven White introdujo DMRG, y en 2004 Pasquale Calabrese y John Cardy '
                    'derivaron el escalamiento logarítmico S_vN(L) = (c/6) ln(L) + s₁ en puntos '
                    'críticos 1D (DOI 10.1088/1742-5468/2004/06/P06002). La biblioteca HEPLean / '
                    'PhysLean de Joseph Tooby-Smith (2025, DOI 10.1016/j.cpc.2024.109457) '
                    'codifica la cancelación de anomalías del Modelo Estándar en Lean 4 (según la '
                    'describe su autor; no se revisó aquí), mientras ITensors.jl (DOI '
                    '10.21468/SciPostPhysCodeb.4) y NetKet (DOI 10.21468/SciPostPhysCodeb.7) '
                    'modelan cadenas críticas con redes tensoriales.',
 'history_milestones': [{'year': '1969',
                         'who_en': 'Stephen Adler, John Bell & Roman Jackiw',
                         'who_es': 'Stephen Adler, John Bell y Roman Jackiw',
                         'title_en': 'Chiral Triangle Gauge Anomalies (ABJ)',
                         'title_es': 'Anomalías Quirales Triangulares (ABJ)',
                         'summary_en': 'Discovers that one-loop chiral fermion triangle diagrams '
                                       'break gauge invariance unless trace sums vanish '
                                       'identically.',
                         'summary_es': 'Descubre que los diagramas triangulares de fermiones '
                                       'quirales rompen la invariancia gauge salvo que sus trazas '
                                       'se anulen.',
                         'roadblock_en': 'Any non-zero trace in U(1)_Y × SU(2)_L × SU(3)_C '
                                         'destroys unitarity and renormalizability.',
                         'roadblock_es': 'Cualquier traza distinta de cero en U(1)_Y × SU(2)_L × '
                                         'SU(3)_C destruye la unitariedad de la teoría.'},
                        {'year': '1970–1972',
                         'who_en': 'Pierre Pfeuty, Claude Bouchiat, John Iliopoulos & Philippe '
                                   'Meyer',
                         'who_es': 'Pierre Pfeuty, Claude Bouchiat, John Iliopoulos y Philippe '
                                   'Meyer',
                         'title_en': 'Exact Ising Criticality & Quark-Lepton Cancellation',
                         'title_es': 'Criticidad Exacta de Ising y Cancelación Quark-Leptón',
                         'summary_en': 'Pfeuty solves the 1D critical Ising model (E₀/N = −4/π); '
                                       'Bouchiat–Iliopoulos–Meyer show N_c = 3 quarks cancel '
                                       'lepton anomalies.',
                         'summary_es': 'Pfeuty resuelve el modelo crítico de Ising 1D (E₀/N = '
                                       '−4/π); Bouchiat–Iliopoulos–Meyer muestran que N_c = 3 '
                                       'colores cancelan las anomalías.',
                         'roadblock_en': 'Checking anomaly cancellation in larger gauge extensions '
                                         'by hand risks algebraic sign mistakes.',
                         'roadblock_es': 'Verificar a mano la cancelación de anomalías en '
                                         'extensiones gauge mayores es propenso a errores de '
                                         'signo.'},
                        {'year': '1992',
                         'who_en': 'Steven R. White',
                         'who_es': 'Steven R. White',
                         'title_en': 'Density Matrix Renormalization Group (DMRG)',
                         'title_es': 'Grupo de Renormalización de la Matriz de Densidad (DMRG)',
                         'summary_en': 'Compresses 2^N quantum spin chains into Matrix Product '
                                       'States (MPS) truncated at bond dimension χ.',
                         'summary_es': 'Comprime cadenas cuánticas de 2^N estados en Estados de '
                                       'Producto Matricial (MPS) con dimensión de enlace χ.',
                         'roadblock_en': 'Why DMRG works even at gapless quantum critical points '
                                         'requires a conformal entanglement scaling law.',
                         'roadblock_es': 'Explicar por qué DMRG funciona incluso en puntos '
                                         'críticos sin brecha requiere una ley conforme de '
                                         'entrelazamiento.'},
                        {'year': '2004',
                         'who_en': 'Pasquale Calabrese & John Cardy',
                         'who_es': 'Pasquale Calabrese y John Cardy',
                         'title_en': 'Conformal Entanglement Entropy Scaling S_vN(L)',
                         'title_es': 'Escalamiento Conforme de la Entropía de Entrelazamiento '
                                     'S_vN(L)',
                         'summary_en': 'Derives logarithmic 1D critical entanglement scaling '
                                       'S_vN(L) = (c/6) ln(L) + s₁, bounded by MPS capacity '
                                       'ln(χ).',
                         'summary_es': 'Deriva que el entrelazamiento crítico 1D crece como '
                                       'S_vN(L) = (c/6) ln(L) + s₁, acotado por la capacidad MPS '
                                       'ln(χ).',
                         'roadblock_en': 'Separates formal mathematical physics proofs from '
                                         'numerical tensor-network codebases.',
                         'roadblock_es': 'Mantiene separadas las demostraciones formales de física '
                                         'matemática y las bibliotecas numéricas de redes '
                                         'tensoriales.'},
                        {'year': '2022–2026',
                         'who_en': 'Joseph Tooby-Smith (PhysLean), ITensors.jl & NetKet',
                         'who_es': 'Joseph Tooby-Smith (PhysLean), ITensors.jl y NetKet',
                         'title_en': 'Lean 4 Gauge Anomaly Checks & Tensor Networks',
                         'title_es': 'Verificación Gauge en Lean 4 y Redes Tensoriales',
                         'summary_en': 'PhysLean encodes Tr[Y] = Tr[Y³] = Tr[τ²Y] = Tr[λ²Y] = 0 '
                                       'over ℚ in Lean 4; this folio checks the four traces and '
                                       'S_vN(128) = 0.8828 ≤ ln(64) = 4.1589.',
                         'summary_es': 'PhysLean codifica Tr[Y] = Tr[Y³] = Tr[τ²Y] = Tr[λ²Y] = 0 '
                                       'sobre ℚ en Lean 4; este folio comprueba las trazas y '
                                       'S_vN(128) = 0.8828 ≤ ln(64) = 4.1589.',
                         'roadblock_en': 'Formalizing full non-perturbative lattice gauge bounds '
                                         'and renormalization flows in PhysLean.',
                         'roadblock_es': 'Formalizar cotas no perturbativas de teorías gauge en el '
                                         'retículo y flujos de renormalización en PhysLean.'}],
 'toy_model_title_en': 'Try It in Your Head in 20 Seconds: Adding 15 Cubed Fractions to Zero & '
                       'Checking a Tensor Pipe',
 'toy_model_title_es': 'Pruébalo en tu Cabeza en 20 Segundos: Sumar 15 Fracciones al Cubo a Cero y '
                       'Probar un Canal Tensorial',
 'toy_model_en': "Check 1 (Why Atoms Are Neutral): Multiply each fermion family's count by its "
                 'cubed hypercharge Y³: 6 left-quarks at (1/6)³ = 6/216 = 1/36; 3 up-quarks at '
                 '(−2/3)³ = 3(−8/27) = −8/9 = −32/36; 3 down-quarks at (1/3)³ = 3(1/27) = +1/9 = '
                 '+4/36. Sum the quarks: (1 − 32 + 4)/36 = −27/36 = −3/4. Now add the leptons: 2 '
                 'left-leptons at (−1/2)³ = 2(−1/8) = −1/4, plus 1 positron at (+1)³ = +1. Sum the '
                 'leptons: −1/4 + 1 = +3/4. Quarks (−3/4) + Leptons (+3/4) = 0 exactly! Check 2 '
                 '(Tensor Pipe): A 128-spin critical Ising chain needs S_vN = 0.883 nats of '
                 'entanglement. With bond dimension χ = 64, our pipe holds ln(64) = 4.159 nats '
                 '(PASS!). Shrink χ to 2, and ln(2) = 0.693 < 0.883 overflows!',
 'toy_model_es': 'Prueba 1 (Por qué los átomos son neutros): Multiplica la multiplicidad de cada '
                 'fermión por su hipercarga al cubo Y³: 6 quarks izquierdos con (1/6)³ = 6/216 = '
                 '1/36; 3 quarks up con (−2/3)³ = 3(−8/27) = −32/36; 3 quarks down con (1/3)³ = '
                 '3(1/27) = +4/36. Suma los quarks: (1 − 32 + 4)/36 = −27/36 = −3/4. Ahora suma '
                 'los leptones: 2 leptones izquierdos con (−1/2)³ = 2(−1/8) = −1/4, más 1 positrón '
                 'con (+1)³ = +1. Suma de leptones: −1/4 + 1 = +3/4. ¡Quarks (−3/4) + Leptones '
                 '(+3/4) = 0 exacto! Prueba 2 (Canal Tensorial): Una cadena crítica de Ising de '
                 '128 espines requiere S_vN = 0.883 nats de entrelazamiento. Con χ = 64, el canal '
                 'soporta ln(64) = 4.159 nats (¡APROBADO!); si bajas χ a 2, ln(2) = 0.693 < 0.883 '
                 'colapsa.',
 'act1_dropcap_es': 'En la teoría cuántica de campos, una simetría del lagrangiano clásico no '
                    'sobrevive automáticamente a la cuantización: los diagramas triangulares de un '
                    'lazo que acoplan tres corrientes gauge quirales pueden romper la invariancia '
                    'gauge salvo que las hipercargas fermiónicas satisfagan cuatro identidades '
                    'algebraicas de traza. En una sola generación del Modelo Estándar, quince '
                    'multipletes de Weyl—dobletes de quarks izquierdos Q_L (3, 2, 1/6), singletes '
                    'derechos up y down u_R^c (3̄, 1, -2/3) y d_R^c (3̄, 1, 1/3), dobletes de '
                    'leptones izquierdos L_L (1, 2, -1/2) y positrones derechos e_R^c (1, 1, '
                    '1)—anulan las trazas gravitacional, mixtas no abelianas y cúbica de '
                    'hipercarga.',
 'act1_body_es': 'La biblioteca HEPLean / PhysLean de Joseph Tooby-Smith (2025, DOI '
                 '10.1016/j.cpc.2024.109457) lleva la teoría de tipos de Lean 4 a la física '
                 'teórica, codificando la cancelación de anomalías del Modelo Estándar, grupos de '
                 'Lorentz, electrodinámica de Maxwell y el teorema de Wick (según la describe su '
                 'autor). En combinación con ITensors.jl (Fishman et al., 2022, DOI '
                 '10.21468/SciPostPhysCodeb.4) y NetKet (Vicentini et al., 2022, DOI '
                 '10.21468/SciPostPhysCodeb.7), el script de este folio evalúa las cuatro trazas '
                 'de anomalía y la relación de Calabrese–Cardy S_vN(L) = (c/6) ln(L) + s_1 ≤ '
                 'ln(χ) para la cadena crítica de Ising 1D (c = 1/2, E₀/N = -4/π = -1.27323954).',
 'act1_stakes_es': 'En 1969, Stephen Adler, John Bell y Roman Jackiw mostraron que los diagramas '
                   'triangulares de un lazo pueden romper simetrías quirales clásicas en la '
                   'electrodinámica cuántica. En el Modelo Estándar, quince multipletes de Weyl '
                   'por generación hacen que cuatro trazas de anomalía—incluida la suma cúbica '
                   '∑ d_f Y_f³—se anulen; con las hipercargas observadas fijas, esa cancelación '
                   'exige N_c = 3 colores de quark. La biblioteca PhysLean de Tooby-Smith (2025, '
                   'DOI 10.1016/j.cpc.2024.109457) codifica estas condiciones en Lean 4 (según la '
                   'describe su autor; no se verificó aquí).\n'
                   '\n'
                   'En física de muchos cuerpos, simular N espines en 2^N estados enfrenta una '
                   'escala exponencial; el método DMRG de Steven White, ITensors.jl (DOI '
                   '10.21468/SciPostPhysCodeb.4) y NetKet (DOI 10.21468/SciPostPhysCodeb.7) '
                   'emplean Estados de Producto Matricial (MPS) sobre cadenas 1D donde el '
                   'entrelazamiento de Calabrese–Cardy crece solo logarítmicamente.',
 'pullquote_es': '6(1/6)³ + 3(-2/3)³ + 3(1/3)³ + 2(-1/2)³ + 1(1)³ = 0: una sola línea de '
                 'aritmética racional en Lean 4 concuerda con la neutralidad eléctrica de los '
                 'átomos.',
 'act2_intuition_es': '¿Por qué los Estados de Producto Matricial (MPS) en ITensors.jl representan '
                      'cadenas críticas 1D de forma compacta? Un enlace de dimensión χ entre dos '
                      'mitades de la cadena transporta como máximo ln(χ) nats de entropía de '
                      'entrelazamiento de von Neumann. Con carga central c = 1/2, longitud L = 128 '
                      'y desplazamiento ilustrativo s_1 = 0.4785, S_vN(128) = (0.5/6) ln(128) + '
                      '0.4785 = 0.8828 nats—capturada por χ = 64 (ln 64 = 4.1589 nats), mientras '
                      'que un estado producto (χ = 1, ln 1 = 0) no captura entrelazamiento.',
 'act2_analogy_es': 'Imagina un puente colgante suspendido entre dos paredes de cañón. Para '
                    'mantener el tablero perfectamente nivelado sin romper los cables, el puente '
                    'depende de dos principios distintos. Primero, los tirantes verticales deben '
                    'lograr un contrapeso mecánico exacto en cuatro básculas simultáneas: peso '
                    'lineal (Tr[Y]), par de torsión cúbico (Tr[Y³]), tensión débil (Tr[τ²Y]) y '
                    'balance de color (Tr[λ²Y]); si una sola hipercarga se desvía por δY ≠ 0, el '
                    'puente pierde su equilibrio. Segundo, la red de fibra óptica que conecta los '
                    'sensores a lo largo del puente tiene un ancho de banda fijo ln(χ). Mientras '
                    'la capacidad del canal ln(χ) supere el tráfico de entrelazamiento cuántico '
                    'S_vN que cruza la mitad del puente, toda la información cuántica se transmite '
                    'sin pérdidas.',
 'act2_plain_primer_es': 'El banco interactivo del Folio B.06 ofrece dos controles. El primero ajusta la '
                         'Dimensión de Enlace MPS χ (de 1 a 128); en χ = 64, ln(64) ≈ 4.16 nats '
                         'supera los 0.8828 nats del modelo de L = 128 sitios. El segundo ajusta la '
                         'Perturbación de Hipercarga δY (de 0.00 a 0.20) sobre el doblete Q_L. En '
                         'δY = 0.00, las cuatro trazas quirales se anulan a precisión de máquina; '
                         'si mueves δY por encima de cero, Tr[Y³] se vuelve distinto de cero y '
                         'activa una alerta de anomalía, y si bajas χ a 1 o 2, ln(χ) cae bajo '
                         '0.8828 nats y dispara un fallo de truncamiento.',
 'act2_deepening_es': 'El Folio B.06 enlaza álgebra de anomalías gauge con cotas de entrelazamiento '
                      'crítico 1D. Para los quince campos de Weyl bajo SU(3)_C × SU(2)_L × U(1)_Y '
                      'por generación, PhysLean (Tooby-Smith, 2025, DOI '
                      '10.1016/j.cpc.2024.109457) codifica la cancelación sobre ℚ; este folio '
                      'evalúa en Python Tr[Y] = 0, Tr[τ²Y] = 0, Tr[λ²Y] = 0 y Tr[Y³] = 6(1/6)³ + '
                      '3(-2/3)³ + 3(1/3)³ + 2(-1/2)³ + 1(1)³ = 0. Con las hipercargas observadas '
                      'fijas, N_c ≠ 3 daría (N_c - 3)/3 ≠ 0. Con la solución de Pfeuty para Ising '
                      '1D crítico (E₀/N = -4/π = -1.27323954) y el escalamiento de Calabrese–Cardy '
                      '(c = 1/2, DOI 10.1088/1742-5468/2004/06/P06002) con desplazamiento '
                      'ilustrativo s_1 = 0.4785, S_vN(128) = 0.8828 nats cabe en la capacidad MPS '
                      'ln(64) = 4.1589 nats.',
 'act4_human_ai_es': 'Bibliotecas en Lean 4 como HEPLean / PhysLean (Tooby-Smith, 2025, DOI '
                     '10.1016/j.cpc.2024.109457) permiten comprobar identidades racionales de '
                     'hipercarga con tácticas como norm_num y ring, mientras ITensors.jl y NetKet '
                     'optimizan estados MPS y estados cuánticos neuronales. La persona '
                     'investigadora define los grupos gauge, hipótesis de simetría e '
                     'interpretación física, y las herramientas detectan errores de signo y '
                     'desbordes de capacidad.',
 'act4_deepening_es': 'El script bounties/bounty_m2_physlean_itensor_quantum_gauge.py se ejecuta '
                      'en menos de 0.05 s con la biblioteca estándar de Python. Evalúa las '
                      'cuatro trazas quirales en punto flotante (< 10⁻¹²), E₀/N = -4/π y '
                      'S_vN(128) = 0.882836 ≤ ln(64) = 4.158883 nats. No ejecuta Lean 4 ni '
                      'ITensors.jl directamente ni implementa aún un modo CLI --planted-defect; '
                      'las perturbaciones contrafactuales (δY > 0 y χ < 3) se prueban en vivo en '
                      'el laboratorio interactivo del Acto III.',
 'sidenote_1_es': {'kicker': 'NOTA AL MARGEN B.06-A · QUÉ PASA SI N_c ≠ 3 COLORES',
                   'body': 'Si los quarks no vinieran en N_c = 3 colores, la traza débil mixta 2 '
                           'N_c(1/6) + 2(-1/2) = (N_c - 3)/3 no se anularía: con las hipercargas fijas en sus valores observados, la cancelación de anomalías quark-leptón exige tres colores.'},
 'sidenote_2_es': {'kicker': 'NOTA AL MARGEN B.06-B · LEY DE ÁREA VS. LEY DE VOLUMEN',
                   'body': 'Los estados base 1D con brecha de energía obedecen una ley de área '
                           'S_vN = O(1), mientras que los puntos críticos conformes 1D crecen solo '
                           'logarítmicamente como (c/6) ln(L), permitiendo la compresión DMRG en '
                           'tiempo polinomial.'},
 'walkthrough_es': ['Verifica el punto de referencia canónico en χ = 64 y δY = 0.00: Tr[Y³] = 0.0, '
                    'E₀/N = -1.273240 y S_vN(128) = 0.8828 ≤ ln(64) = 4.1589 (APROBADO).',
                    'Perturba la Hipercarga δY fuera de 0.00 (o pulsa [⚡ Counterfactual '
                    'Axiom-Knockout]): observa cómo la anomalía cúbica Tr[Y³] deja de ser cero, '
                    'rompiendo la consistencia cuántica de U(1)_Y.',
                    'Arrastra la Dimensión de Enlace MPS χ hacia abajo hasta 1 o 2: observa cómo '
                    'ln(χ) cae por debajo de S_vN(128) = 0.8828 nats, disparando un fallo por '
                    'truncamiento de entrelazamiento.'],
 'steps_es': ['Etapa 1 (Tabla de Multipletes en el Arnés): Codifica los cinco multipletes de '
              'Weyl SU(3)_C × SU(2)_L × U(1)_Y por generación (PhysLean, DOI '
              '10.1016/j.cpc.2024.109457): Q_L(3,2,1/6), u_R^c(3,1,-2/3), d_R^c(3,1,1/3), '
              'L_L(1,2,-1/2), e_R^c(1,1,1).',
              'Etapa 2 (Suma de Cuatro Trazas en el Arnés): Evalúa Tr[Y], Tr[Y³], Tr[τ²Y] y '
              'Tr[λ²Y] en punto flotante de Python (< 10⁻¹²; PhysLean reporta la verificación '
              'racional sobre ℚ en Lean 4).',
              'Etapa 3 (Fórmulas de Pfeuty y Calabrese–Cardy en el Arnés): Evalúa E₀/N = -4/π = '
              '-1.27323954 y S_vN(L=128) = (0.5/6) ln(128) + 0.4785 = 0.882836 nats (s_1 = 0.4785 '
              'ilustrativo).',
              'Etapa 4 (Control de Capacidad de Enlace MPS): Verifica que la capacidad '
              'logarítmica ln(χ) = ln(64) = 4.158883 nats acota S_vN(128) = 0.882836 nats.'],
 'rules_es': ['Cancelación de Anomalías Gauge del Modelo Estándar: Los cuatro invariantes de traza '
              'quiral (gravitacional Tr[Y], cúbico U(1)_Y³ Tr[Y³], mixto débil Tr[τ²Y] y mixto de '
              'color Tr[λ²Y]) deben anularse idénticamente (|Tr| < 10⁻¹²); cualquier deriva δY ≠ 0 '
              'rompe la invariancia gauge cuántica.',
              'Cota de Entrelazamiento de Calabrese–Cardy: Para representar fielmente el estado '
              'base crítico de Ising en L = 128 (c = 0.5, S_vN = 0.882836 nats), la dimensión de '
              'enlace MPS debe satisfacer ln(χ) ≥ S_vN(L), es decir, χ ≥ 3.',
              'Invariante de Energía del Estado Base de Pfeuty: La energía crítica por sitio en g '
              '= J = 1 debe ser igual a -4/π = -1.27323954.'],
 't0_t1_certified_es': ['Arnés algebraico de anomalías de cuatro trazas del Modelo Estándar y '
                        'escalamiento TFIM 1D en '
                        'bounties/bounty_m2_physlean_itensor_quantum_gauge.py (tiempo < 0.05 s; sin '
                        'ejecución de Lean 4 ni modo de defecto sembrado aún).',
                        'Referencias primarias revisadas: Tooby-Smith (2025, DOI '
                        '10.1016/j.cpc.2024.109457), Fishman et al. (2022, DOI '
                        '10.21468/SciPostPhysCodeb.4) y Vicentini et al. (2022, DOI '
                        '10.21468/SciPostPhysCodeb.7).'],
 't2_t3_open_horizon_es': ['Formalización abierta en HEPLean / PhysLean (pull requests bienvenidos, '
                           'sin premio monetario): envío de pull requests en Lean 4 sobre flujos del '
                           'grupo de renormalización, cotas gauge en retículo o clasificación de '
                           'anomalías BSM directamente en HEPLean/PhysLean.']}
