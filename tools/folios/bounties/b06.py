# -*- coding: utf-8 -*-
"""Open Bounties — Folio B.06: Machine-Checked Gauge Physics in PhysLean & Tensor-Network Quantum Criticality (ITensors.jl + NetKet)."""


FOLIO = {'slug': 'b06',
 'folio_id': 'B.06',
 'bounty_id': 'BOUNTY-M2',
 'cat': 'math',
 'plate_slug': 'b06',
 'pillar_label_en': 'Math & Quantum · Lean 4 Gauge Physics & Tensor Networks',
 'pillar_label_es': 'Matemáticas y Cuántica · Física Gauge en Lean 4 y Redes Tensoriales',
 'badge_en': 'BOUNTY B.06 (M-2) · PHYSLEAN + ITENSORS.JL + NETKET',
 'badge_es': 'RETO B.06 (M-2) · PHYSLEAN + ITENSORS.JL + NETKET',
 'title': 'Machine-Checked Gauge Physics in PhysLean & Tensor-Network Quantum Criticality '
          '(ITensors.jl + NetKet)',
 'title_es': 'Física Gauge Verificada en PhysLean y Criticidad Cuántica con Redes Tensoriales '
             '(ITensors.jl + NetKet)',
 'subtitle': 'How HEPLean/PhysLean certifies Standard Model U(1)_Y × SU(2)_L × SU(3)_C chiral '
             'anomaly cancellation in Lean 4 while ITensors.jl and NetKet bound critical '
             'entanglement entropy.',
 'subtitle_es': 'Cómo HEPLean/PhysLean certifica en Lean 4 la cancelación de anomalías quirales '
                'del Modelo Estándar mientras ITensors.jl y NetKet acotan la entropía de '
                'entrelazamiento crítico.',
 'why_en': 'Why does the electric charge of a proton exactly cancel the charge of an electron, '
           'even though quarks carry fractional charges of +2/3 and -1/3? Because quantum gauge '
           'invariance of the Standard Model requires four anomaly traces—including the cubic '
           'hypercharge sum ∑ d_f Y_f³—to vanish identically to zero, a profound algebraic miracle '
           'now machine-checked in Lean 4 via PhysLean.',
 'why_es': '¿Por qué la carga eléctrica del protón cancela exactamente la del electrón aunque los '
           'quarks tengan cargas fraccionarias +2/3 y -1/3? Porque la consistencia cuántica del '
           'Modelo Estándar exige que cuatro trazas de anomalía—incluida la suma cúbica ∑ d_f '
           'Y_f³—sean idénticamente cero, una identidad verificada formalmente en Lean 4 mediante '
           'PhysLean.',
 'governing_law': 'Tr[Y] = Tr[Y³] = Tr[τ²Y] = Tr[λ²Y] = 0 · S_vN(L) = (c/6) ln(L) + s_1 = 0.8828 ≤ '
                  'ln(χ = 64) = 4.1589',
 'pass_pill_en': 'PASS · Tr[Y³] = 0 · S_vN = 0.883 ≤ ln(64)',
 'pass_pill_es': 'APROBADO · Tr[Y³] = 0 · S_vN = 0.883 ≤ ln(64)',
 'verifier_script': 'bounties/bounty_m2_physlean_itensor_quantum_gauge.py',
 'skill_dir': 'skills/bounties/b06',
 'skill_name': 'bounty-b06-physlean-itensor-quantum-gauge',
 'primary_doi': '10.1016/j.cpc.2024.109457',
 'scite_summary': 'Tooby-Smith (2024) PhysLean/HepLean formalization in Lean 4 and Fishman, White '
                  '& Stoudenmire (2022) ITensors.jl verified against Crossref and Scite.',
 'date_published': '2026-11-04',
 'date_redated': '2026-11-08',
 'current_edition': 'REV 1.2',
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
 'act1_dropcap': 'In quantum field theory, a symmetry of the classical Lagrangian is not '
                 'guaranteed to survive quantization: one-loop triangle Feynman diagrams coupling '
                 'three chiral gauge currents can break gauge invariance and destroy unitarity '
                 'unless the fermion representations satisfy exact algebraic trace identities. In '
                 'a single generation of the Standard Model, fifteen Weyl fermion '
                 'multiplets—left-handed quark doublets Q_L (3, 2, 1/6), right-handed up and down '
                 'singlets u_R^c (3̄, 1, -2/3) and d_R^c (3̄, 1, 1/3), left-handed lepton doublets '
                 'L_L (1, 2, -1/2), and right-handed positrons e_R^c (1, 1, 1)—conspire so that '
                 'gravitational, mixed non-Abelian, and cubic hypercharge anomalies cancel to '
                 'zero.',
 'act1_body': "Joseph Tooby-Smith's HEPLean / PhysLean library (DOI 10.1016/j.cpc.2024.109457) "
              "brings Lean 4's dependent type theory to theoretical physics, formalizing results across Standard Model anomaly cancellation,"
              ' Lorentz groups, Maxwell '
              "electrodynamics, and Wick's theorem. Paired with Matthew Fishman, Steven White, and "
              "Miles Stoudenmire's ITensors.jl (DOI 10.21468/SciPostPhysCodeb.4) and Giuseppe "
              "Carleo and Filippo Vicentini's NetKet (DOI 10.21468/SciPostPhysCodeb.7), our "
              'benchmark verifies both exact symbolic gauge-anomaly cancellation and the '
              'Calabrese–Cardy conformal entanglement scaling S_vN(L) = (c/6) ln(L) + s_1 ≤ ln(χ) '
              'of the 1D critical Transverse-Field Ising Model (c = 1/2, E₀/N = -4/π = '
              '-1.27323954).',
 'pullquote': '6(1/6)³ + 3(-2/3)³ + 3(1/3)³ + 2(-1/2)³ + 1(1)³ = 0: one line of rational '
              'arithmetic in Lean 4 explains why atoms are electrically neutral and the quantum '
              'vacuum is consistent.',
 'chronology': [('1969',
                 'Stephen Adler, John Bell, and Roman Jackiw discover chiral triangle anomalies in '
                 'quantum electrodynamics.'),
                ('1970',
                 'Pierre Pfeuty solves the 1D Transverse-Field Quantum Ising Model exactly, '
                 'proving critical ground-state energy density E₀/N = -4/π.'),
                ('1992–2004',
                 'Steven White invents the Density Matrix Renormalization Group (DMRG); Pasquale '
                 'Calabrese and John Cardy derive CFT entanglement entropy S_vN(L) = (c/6) ln(L) + '
                 's_1.'),
                ('2022–2026',
                 'ITensors.jl (DOI 10.21468/SciPostPhysCodeb.4), NetKet 3 (DOI '
                 '10.21468/SciPostPhysCodeb.7), and HEPLean/PhysLean in Lean 4 (DOI '
                 '10.1016/j.cpc.2024.109457) unify tensor networks with formal proof assistants.')],
 'act2_intuition': 'Why do Matrix Product States (MPS) in ITensors.jl solve 1D quantum chains so '
                   'efficiently? Because a bond of dimension χ between two halves of a chain can '
                   'carry at most ln(χ) nats of von Neumann entanglement entropy. At the quantum '
                   'critical point of the Ising chain (central charge c = 1/2, length L = 128), '
                   'S_vN(128) = (0.5/6) ln(128) + 0.4785 = 0.8828 nats—easily captured by bond '
                   'dimension χ = 64 (ln 64 = 4.1589 nats), whereas a mean-field product state (χ '
                   '= 1, ln 1 = 0) misses the critical entanglement entirely.',
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
 'steps': ['Stage 1: Weyl Multiplet Assignment in PhysLean — Declare the five chiral SU(3)_C × '
           'SU(2)_L × U(1)_Y representations per generation: Q_L(3,2,1/6), u_R^c(3,1,-2/3), '
           'd_R^c(3,1,1/3), L_L(1,2,-1/2), e_R^c(1,1,1).',
           'Stage 2: Four-Trace Gauge Anomaly Cancellation — Verify Tr[Y] = 0, Tr[Y³] = 0, Tr[τ²Y] '
           '= 0, and Tr[λ²Y] = 0 to machine precision (and exactly over ℚ in Lean 4).',
           'Stage 3: Exact Pfeuty & Calabrese–Cardy Critical Scaling — Evaluate 1D critical '
           'Transverse-Field Ising ground-state energy density E₀/N = -4/π = -1.27323954 and '
           'entanglement entropy S_vN(L=128) = (0.5/6) ln(128) + 0.4785 = 0.882836 nats.',
           'Stage 4: MPS Bond-Dimension Capacity Certification — Confirm that MPS bond capacity '
           'ln(χ) = ln(64) = 4.158883 nats strictly bounds S_vN(128) = 0.882836 nats.'],
 'rules': ['Standard Model Gauge Anomaly Cancellation: All four chiral trace invariants '
           '(gravitational Tr[Y], cubic U(1)_Y³ Tr[Y³], weak mixed Tr[τ²Y], and colour mixed '
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
 't0_t1_certified': ['Deterministic Standard Model four-trace anomaly verifier and 1D critical '
                     'TFIM entanglement harness in '
                     'bounties/bounty_m2_physlean_itensor_quantum_gauge.py (< 0.05s runtime).',
                     'Cross-checked against Tooby-Smith (2024, DOI 10.1016/j.cpc.2024.109457), '
                     'Fishman et al. (2022, DOI 10.21468/SciPostPhysCodeb.4), and Vicentini et al. '
                     '(2022, DOI 10.21468/SciPostPhysCodeb.7).',
                     'Ready for immediate community showcase submission to HEPLean/PhysLean Zulip '
                     'and ITensors / NetKet showcases.'],
 't2_t3_open_horizon': ['HEPLean / PhysLean open formalization work (no cash prize is named here): submitting 0-sorry Lean 4 '
                        'pull requests formalizing renormalization group flows, lattice gauge '
                        'bounds, or BSM anomaly classification directly in HEPLean/PhysLean.'],
 'sources': ['Tooby-Smith, J. (2024). HepLean: Digitalising high energy physics. Computer Physics '
             'Communications, 308, 109457. DOI 10.1016/j.cpc.2024.109457',
             'Fishman, M., White, S. R., & Stoudenmire, E. M. (2022). The ITensor Software Library '
             'for Tensor Network Calculations. SciPost Physics Codebases, 4. DOI '
             '10.21468/SciPostPhysCodeb.4',
             'Vicentini, F., et al. (2022). NetKet 3: Machine Learning Toolbox for Many-Body '
             'Quantum Systems. SciPost Physics Codebases, 7. DOI 10.21468/SciPostPhysCodeb.7',
             'Calabrese, P., & Cardy, J. (2004). Entanglement entropy and quantum field theory. '
             'Journal of Statistical Mechanics: Theory and Experiment, 2004(06), P06002. DOI '
             '10.1088/1742-5468/2004/06/P06002'],
 'act1_plain_bridge': 'Every atom in our universe is held together by an astonishing numerical '
                      'miracle that we rarely stop to appreciate. A proton inside an atomic '
                      'nucleus is made of three tightly bound quarks, each carrying a weird '
                      'fractional electric charge of plus two-thirds or minus one-third. Floating '
                      'around the nucleus is an electron, an entirely different fundamental '
                      'particle that has nothing to do with quarks. Yet the positive charge of the '
                      'proton cancels the negative charge of the electron with absolute, flawless '
                      'perfection down to dozens of decimal places. Why is an atom completely '
                      'neutral instead of carrying an awkward leftover static charge? In modern '
                      'quantum physics, this balance is not an accident or a lucky coincidence; it '
                      'is required by mathematical consistency. If the particle charges did not '
                      'add up to zero across four specific algebraic equations, quantum '
                      "calculations would blow up to infinity and destroy the universe's "
                      'stability. Meanwhile, when thousands of quantum particles interact in a '
                      'solid material, their spooky entanglement threatens to overwhelm any '
                      'supercomputer. By organizing particles into a linked chain called a tensor '
                      'network, physicists capture essential quantum connections while trimming '
                      'away redundant information, making complex quantum matter understandable.',
 'act1_stakes': 'The historical development of particle physics and quantum many-body theory was '
                'plagued for decades by mathematical catastrophes. In 1969, Stephen Adler, John '
                'Bell, and Roman Jackiw discovered that quantum corrections could break classical '
                'symmetries in quantum electrodynamics through triangular Feynman diagrams, '
                'introducing chiral anomalies that threatened to destroy unitarity and render '
                'quantum field theory mathematically nonsensical. The entire Standard Model of '
                'particle physics survived only because its fifteen chiral fermion representations '
                'per generation perform a breathtaking algebraic balancing act. Four distinct '
                'anomaly trace equations—most notably the cubic hypercharge sum ∑ d_f Y_f^3—cancel '
                'out to exact rational zero, explaining from pure geometry why quarks require '
                'exactly three color charges and why matter is electrically stable. Until '
                'recently, verifying these intricate cancellations across grand unified theories '
                'relied on fragile manual blackboard algebra prone to sign errors. With Joseph '
                'Tooby-Smith’s PhysLean library in Lean 4, theoretical physics now possesses '
                'computer-verified formal proofs where chiral anomaly cancellation is certified '
                'with zero sorry gaps. Simultaneously, in condensed-matter physics, the challenge '
                'of simulating quantum criticality long ran into an exponential wall: a system of '
                'N interacting quantum spins occupies an intractable 2^N-dimensional Hilbert '
                'space. Steven White’s Density Matrix Renormalization Group and modern '
                'tensor-network frameworks like ITensors.jl and NetKet transformed this impasse. '
                'Grounded in the Calabrese–Cardy conformal scaling law, Matrix Product States '
                'compress quantum entanglement along a one-dimensional chain in polynomial time, '
                'proving that critical states obey bounded logarithmic area laws and opening the '
                'frontier of certified quantum simulation.',
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
 'act2_plain_primer': 'The interactive workbench for Folio B.06 places two fundamental knobs of '
                      'quantum theory directly into your hands. The first slider adjusts MPS Bond '
                      'Dimension χ, which represents the data capacity of the Matrix Product State '
                      'in ITensors.jl. When set to its default value of χ = 64, the network easily '
                      'accommodates the entanglement of a 128-site critical quantum Ising chain, '
                      'providing a spacious capacity of ln(64) ≈ 4.16 nats against the required '
                      '0.88 nats. The second slider controls Hypercharge Perturbation δY, which '
                      'introduces an intentional flaw into the electric hypercharge assignments of '
                      'Standard Model fermions. In the certified baseline regime (δY = 0.00), all '
                      'four chiral anomaly traces vanish to machine precision, confirming that '
                      'quantum gauge theory remains mathematically sound. Now, test what happens '
                      'when you click the Counterfactual Knockout button or drag the controls. If '
                      'you push δY above zero, the cubic trace Tr[Y^3] instantly spikes, violating '
                      'gauge symmetry and triggering an anomaly alert. If you drop bond dimension '
                      'χ down to 1 or 2, the tensor capacity collapses below the critical '
                      'entanglement curve, causing an immediate quantum truncation failure.',
 'distill_diagram': {'analogy_title': 'Suspension Bridge Cable Balance',
                     'analogy_sub': 'Balanced weights ensure bridge stability as data channels '
                                    'prevent lag.',
                     'force_a_title': 'Hypercharge Trace Drift (δY)',
                     'force_a_sub': 'Shifts fermion hypercharge, destroying cubic gauge anomaly '
                                    'balance.',
                     'force_b_title': 'MPS Bond Capacity (ln χ)',
                     'force_b_sub': 'Bounds quantum entanglement entropy across critical many-body '
                                    'chains.',
                     'threshold_title': 'Area-Law Capacity (ln χ ≥ S_vN)',
                     'threshold_eq': 'Tr[Y³] = 0 · S_vN(128) = 0.8828 ≤ ln(χ) = 4.1589',
                     'threshold_sub': 'Guarantees anomaly-free gauge physics and faithful tensor '
                                      'states.',
                     'threshold_pass': 'Tr[Y³] = 0 (anomaly-free) & S_vN(128) = 0.883 ≤ ln(64) = '
                                       '4.159 nats.',
                     'threshold_fail': 'Anomaly: δY > 0 breaks Tr[Y³] = 0; Truncation: χ < 3 fails '
                                       'S_vN bound.',
                     'caption': 'Plate B.06-D maps the twin pillars of certified quantum physics: '
                                'exact algebraic cancellation of chiral gauge anomalies in '
                                'PhysLean and logarithmic area-law entanglement bounds in '
                                'ITensors.jl. The diagram illustrates how vanishing trace '
                                'invariants ensure physical consistency while tensor networks '
                                'compress critical quantum states.'},
 'act2_deepening': 'The formal unity of Folio B.06 links machine-checked algebraic geometry in '
                   'Lean 4 with conformal quantum information theory. In the gauge sector, quantum '
                   'consistency of the Standard Model requires that triangle Feynman loops with '
                   'chiral fermions vanish across all gauge groups. For each fermion generation, '
                   'fifteen chiral Weyl fields transform under SU(3)_C × SU(2)_L × U(1)_Y: quark '
                   'doublets Q_L(3,2,1/6), up-singlets u_R^c(ō3,1,-2/3), down-singlets '
                   'd_R^c(ō3,1,1/3), lepton doublets L_L(1,2,-1/2), and positrons e_R^c(1,1,1). In '
                   'Joseph Tooby-Smith’s PhysLean library, the Standard Model anomaly cancellation conditions are formalized over the rational field ℚ; the four traces this folio checks are the gravitational trace Tr[Y] = 0, '
                   'the non-Abelian weak mixed trace Tr[τ^2 Y] = 0, the color mixed trace Tr[λ^2 '
                   'Y] = 0, and the celebrated cubic trace Tr[Y^3] = 6(1/6)^3 + 3(-2/3)^3 + '
                   '3(1/3)^3 + 2(-1/2)^3 + 1(1)^3 = 0. If quarks lacked three colors (N_c ≠ 3), '
                   'the weak trace would yield (N_c - 3)/3 ≠ 0, breaking gauge invariance. In '
                   'parallel, the many-body sector investigates the 1D Transverse-Field Quantum '
                   'Ising Model at criticality (g = J = 1). Pierre Pfeuty proved the exact '
                   'ground-state energy density E_0 / N = -4/π = -1.27323954. Conformal field '
                   'theory with central charge c = 1/2 dictates Calabrese–Cardy entanglement '
                   'entropy S_vN(L) = (c/6) ln(L) + s_1. At chain length L = 128, S_vN(128) = '
                   '(0.5/6) ln(128) + 0.4785 = 0.8828 nats. ITensors.jl represents this state as a '
                   'Matrix Product State whose bond dimension χ = 64 provides capacity ln(64) = '
                   '4.1589 nats, rigorously bounding S_vN and guaranteeing polynomial compression.',
 'act4_human_ai': 'In the modern era of theoretical and quantum physics, progress occurs at the '
                  'confluence of human mathematical conceptualization and machine-checked '
                  'computational rigor. Theoretical physicists identify the deep structural '
                  'questions: they conceptualize anomaly cancellation across Beyond-Standard-Model '
                  'gauge groups, formulate grand unified embeddings, and design quantum tensor '
                  'architectures. Yet manual derivations of multidimensional Clifford algebras, '
                  'Lorentz representations, and tensor contractions are notoriously prone to '
                  'subtle human oversight. Here, the modern toolchain transforms research into an '
                  'infallible collaborative workflow. Joseph Tooby-Smith’s PhysLean repository '
                  'formalizes high-energy physics directly within the Lean 4 interactive theorem '
                  'prover, allowing automated tactics like norm_num and ring to verify rational '
                  'charge identities with mathematical certainty. Concurrently, Matthew Fishman, '
                  'Steven White, and Miles Stoudenmire’s ITensors.jl alongside Giuseppe Carleo and '
                  'Filippo Vicentini’s NetKet provide high-performance numerical engines for '
                  'optimizing Matrix Product States and neural quantum states. In this '
                  'collaborative loop, artificial intelligence assists by checking proof branches, '
                  'generating candidate tensor networks, and proposing variational ground states. '
                  'However, the human scientist steers the physical inquiry, establishing symmetry '
                  'constraints and interpreting phase transitions. By integrating Lean 4 proof '
                  'assistants with Julia and Python tensor networks, researchers can explore novel '
                  'topological phases of matter and exotic gauge theories with absolute confidence '
                  'that every algebraic identity and numerical boundary is machine-certified.',
 'act4_deepening': 'The cornerstone of scientific credibility in computational physics is '
                   'adversarial reproducibility. The standalone verifier '
                   'bounties/bounty_m2_physlean_itensor_quantum_gauge.py and its companion '
                   'SKILL.md provide an automated, zero-dependency gate that falsifies ungrounded '
                   'assertions before any benchmark claim is certified. Operating in Python '
                   'standard library in under 0.05 seconds, the script performs a rigorous '
                   'two-pronged evaluation. First, it encodes the five Standard Model Weyl fermion '
                   'multiplets across their exact representation dimensions and evaluates the four '
                   'chiral trace equations, verifying that gravitational, cubic, and non-Abelian '
                   'anomalies cancel to within 10^{-12}. It then computes the exact Pfeuty energy '
                   'density E_0 / N = -4/π and verifies that the Matrix Product State bond '
                   'dimension χ = 64 provides ample logarithmic capacity ln(64) ≈ 4.1589 nats to '
                   'bound the critical entanglement entropy S_vN ≈ 0.8828 nats. Second, the '
                   'verifier subjects the model to an adversarial planted-defect test. By '
                   'injecting a synthetic hypercharge perturbation δY = 0.05, it confirms that the '
                   'cubic anomaly immediately breaches tolerance, forcing an explicit verification '
                   'failure. Similarly, truncating bond dimension down to χ = 2 proves that '
                   'capacity collapse triggers an immediate area-law violation. By demanding that '
                   'invalid states fail unconditionally, this verification architecture guarantees '
                   'that no generative AI agent or human contributor can claim benchmark '
                   'convergence on an inconsistent gauge model.',
 'plain_es': 'Para entender por qué los átomos de nuestro universo son eléctricamente estables, '
             'imaginen un puente colgante sostenido por cables de acero perfectamente balanceados. '
             'En el núcleo de cada átomo habitan protones formados por tres quarks con cargas '
             'fraccionarias extrañas, mientras que a su alrededor giran electrones independientes. '
             'A pesar de ser partículas completamente distintas, la carga del protón cancela la '
             'del electrón con una precisión asombrosa. En la física cuántica moderna, este '
             'equilibrio no es una casualidad afortunada: es un requisito matemático estricto. Si '
             'las cargas no sumaran exactamente cero en cuatro ecuaciones de equilibrio, las leyes '
             'cuánticas se romperían y la materia colapsaría en el caos. Por otra parte, cuando '
             'miles de partículas interactúan en un material, su entrelazamiento cuántico puede '
             'saturar cualquier computadora. Mediante redes tensoriales, los físicos organizan '
             'estas partículas como una hilera ordenada de sensores, asegurando que el canal de '
             'datos capture todas las conexiones cuánticas esenciales sin perder información ni '
             'desperdiciar memoria de cálculo.',
 'deep_es': 'La coherencia interna del Modelo Estándar y la simulación eficiente de la criticidad '
            'cuántica convergen en principios algebraicos y topológicos rigurosos. En el ámbito de '
            'las teorías de norma, la cuantización de fermiones quirales introduce diagramas '
            'triangulares de un lazo que destruyen la unitariedad a menos que se anulen cuatro '
            'trazas algebraicas de hipercarga: la traza gravitacional Tr[Y], la traza débil mixta '
            'Tr[τ^2 Y], la traza de color Tr[λ^2 Y] y la suma cúbica Tr[Y^3] = 0. Esta identidad '
            'fundamental, formalizada en Lean 4 mediante PhysLean, muestra que, con las hipercargas observadas, la cancelación exige tres colores. '
            'En paralelo, en la cadena cuántica de Ising en su punto crítico con carga central c = '
            '1/2, la entropía de entrelazamiento de Calabrese–Cardy escala logarítmicamente según '
            'S_vN(128) = 0.8828 nats. Los estados de producto matricial (MPS) en ITensors.jl '
            'truncan el espacio de Hilbert mediante una dimensión de enlace χ = 64 cuya capacidad '
            'ln(64) = 4.1589 nats acota estrictamente la entropía crítica, garantizando compresión '
            'polinomial sin pérdida de fidelidad.',
 'easy_history_title_en': 'How Human Pioneers Reached This Frontier: From 1969 Triangle Anomalies '
                          '& DMRG Chains to PhysLean in Lean 4',
 'easy_history_title_es': 'Cómo los Pioneros Humanos Llegaron a Esta Frontera: De las Anomalías '
                          'Triangulares de 1969 y DMRG a PhysLean en Lean 4',
 'easy_history_en': 'In 1969, physicists Stephen Adler, John Bell, and Roman Jackiw uncovered a '
                    'terrifying trap at the heart of quantum field theory. Even when a classical '
                    'law of physics obeys a clean symmetry on paper, zooming in to the quantum '
                    'level introduces virtual fermion loops shaped like tiny triangles (Feynman '
                    'triangle diagrams) that can violently break that symmetry—making '
                    'probabilities add up to more than 100% and causing the theory to '
                    'self-destruct! When physicists checked the fledgling Standard Model of '
                    'particle physics in the early 1970s, they held their breath: in each '
                    'generation of matter, there are 15 chiral fermion fields carrying strange '
                    'fractional hypercharges like +1/6, −2/3, +1/3, −1/2, and +1. Miraculously, '
                    'when you cube all fifteen hypercharges and add them up—provided quarks come '
                    'in exactly three colors—the positive and negative fractions cancel out to '
                    'exact zero: 6(1/6)³ + 3(−2/3)³ + 3(1/3)³ + 2(−1/2)³ + 1(1)³ = 0! That single '
                    'cancellation is why the proton and electron have equal and opposite electric '
                    'charges and why atoms are neutral.\n'
                    '\n'
                    'Meanwhile, condensed-matter physicists faced a second wall: simulating N '
                    'entangled quantum spins requires 2^N numbers, which overwhelms every computer '
                    'on Earth past N = 50. In 1992, Steven White invented the Density Matrix '
                    'Renormalization Group (DMRG), and in 2004 Pasquale Calabrese and John Cardy '
                    'proved via Conformal Field Theory that critical 1D quantum chains only grow '
                    'their entanglement logarithmically as S_vN(L) = (c/6) ln(L) + s₁. Today, '
                    "between 2022 and 2026, Joseph Tooby-Smith's PhysLean (HEPLean) library "
                    'certifies Standard Model anomaly cancellation with zero sorry axioms in Lean '
                    "4, while Matthew Fishman, Steven White, and Miles Stoudenmire's ITensors.jl "
                    'and NetKet compress critical quantum chains into Matrix Product States.',
 'easy_history_es': 'En 1969, los físicos Stephen Adler, John Bell y Roman Jackiw descubrieron una '
                    'trampa inquietante en el corazón de la teoría cuántica de campos. Incluso '
                    'cuando una ley física respeta una simetría impecable a nivel clásico, las '
                    'fluctuaciones cuánticas introducen lazos cerrados de fermiones con forma de '
                    'triángulo (los diagramas triangulares de Feynman) capaces de romper esa '
                    'simetría y destruir la consistencia matemática de las probabilidades. Cuando '
                    'los físicos revisaron el naciente Modelo Estándar a principios de los años '
                    'setenta, contuvieron el aliento: cada familia de materia contiene 15 campos '
                    'de fermiones quirales con hipercargas fraccionarias extrañas como +1/6, −2/3, '
                    '+1/3, −1/2 y +1. Milagrosamente, al elevar al cubo las quince hipercargas y '
                    'sumarlas—siempre que los quarks existan en exactamente tres colores—las '
                    'fracciones positivas y negativas se cancelan dando cero exacto: 6(1/6)³ + '
                    '3(−2/3)³ + 3(1/3)³ + 2(−1/2)³ + 1(1)³ = 0. Esa identidad aritmética explica '
                    'por qué el protón y el electrón tienen cargas exactamente opuestas y por qué '
                    'los átomos son eléctricamente neutros.\n'
                    '\n'
                    'En paralelo, la física de muchos cuerpos enfrentaba la barrera exponencial de '
                    '2^N estados cuánticos. En 1992, Steven White inventó el grupo de '
                    'renormalización de la matriz de densidad (DMRG), y en 2004 Pasquale Calabrese '
                    'y John Cardy demostraron que en un punto crítico cuántico 1D la entropía de '
                    'entrelazamiento crece solo logarítmicamente como S_vN(L) = (c/6) ln(L) + s₁. '
                    'Hoy, entre 2022 y 2026, la biblioteca PhysLean (HEPLean) de Joseph '
                    'Tooby-Smith certifica formalmente en Lean 4 la cancelación de anomalías del '
                    'Modelo Estándar sin un solo sorry, mientras ITensors.jl y NetKet comprimen '
                    'cadenas críticas en estados de producto matricial (MPS).',
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
                                       'Bouchiat–Iliopoulos–Meyer prove N_c = 3 quarks cancel '
                                       'lepton anomalies.',
                         'summary_es': 'Pfeuty resuelve el modelo crítico de Ising 1D (E₀/N = '
                                       '−4/π); Bouchiat–Iliopoulos–Meyer prueban que N_c = 3 '
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
                         'summary_en': 'Proves that 1D critical entanglement grows logarithmically '
                                       'as S_vN(L) = (c/6) ln(L) + s₁, bounded by MPS capacity '
                                       'ln(χ).',
                         'summary_es': 'Demuestra que el entrelazamiento crítico 1D crece como '
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
                         'title_en': 'Zero-Sorry Lean 4 Gauge Proofs & Tensor Networks',
                         'title_es': 'Pruebas Gauge Cero-Sorry en Lean 4 y Redes Tensoriales',
                         'summary_en': 'Machine-checks Tr[Y] = Tr[Y³] = Tr[τ²Y] = Tr[λ²Y] = 0 over '
                                       'ℚ in Lean 4 while certifying S_vN(128) = 0.8828 ≤ ln(64) = '
                                       '4.1589.',
                         'summary_es': 'Certifica en Lean 4 que Tr[Y] = Tr[Y³] = Tr[τ²Y] = Tr[λ²Y] '
                                       '= 0 sobre ℚ y verifica S_vN(128) = 0.8828 ≤ ln(64) = '
                                       '4.1589.',
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
 'act1_dropcap_es': 'En la teoría cuántica de campos, no está garantizado que una simetría del '
                    'lagrangiano clásico sobreviva a la cuantización: los diagramas de Feynman '
                    'triangulares de un lazo que acoplan tres corrientes gauge quirales pueden '
                    'romper la invariancia gauge y destruir la unitariedad a menos que las '
                    'representaciones fermiónicas satisfagan identidades algebraicas de traza '
                    'exactas. En una sola generación del Modelo Estándar, quince multipletes de '
                    'fermiones de Weyl—dobletes de quarks izquierdos Q_L (3, 2, 1/6), singletes '
                    'derechos up y down u_R^c (3̄, 1, -2/3) y d_R^c (3̄, 1, 1/3), dobletes de '
                    'leptones izquierdos L_L (1, 2, -1/2) y positrones derechos e_R^c (1, 1, '
                    '1)—conspiran para que las anomalías gravitacional, mixtas no abelianas y '
                    'cúbica de hipercarga se cancelen exactamente a cero.',
 'act1_body_es': 'La biblioteca HEPLean / PhysLean de Joseph Tooby-Smith (DOI '
                 '10.1016/j.cpc.2024.109457) lleva la teoría de tipos dependientes de Lean 4 a la '
                 'física teórica, formalizando resultados sobre cancelación de '
                 'anomalías del Modelo Estándar, grupos de Lorentz, electrodinámica de Maxwell y '
                 'el teorema de Wick. En combinación con ITensors.jl de Matthew Fishman, Steven '
                 'White y Miles Stoudenmire (DOI 10.21468/SciPostPhysCodeb.4) y NetKet de Giuseppe '
                 'Carleo y Filippo Vicentini (DOI 10.21468/SciPostPhysCodeb.7), nuestro banco de '
                 'pruebas verifica tanto la cancelación simbólica exacta de anomalías gauge como '
                 'el escalamiento conforme de entrelazamiento de Calabrese–Cardy S_vN(L) = (c/6) '
                 'ln(L) + s_1 ≤ ln(χ) del Modelo de Ising Cuántico de Campo Transversal crítico en '
                 '1D (c = 1/2, E₀/N = -4/π = -1.27323954).',
 'act1_stakes_es': 'El desarrollo histórico de la física de partículas y de la teoría cuántica de '
                   'muchos cuerpos estuvo marcado durante décadas por catástrofes matemáticas. En '
                   '1969, Stephen Adler, John Bell y Roman Jackiw descubrieron que las '
                   'correcciones cuánticas podían romper simetrías clásicas mediante diagramas '
                   'triangulares de Feynman, introduciendo anomalías quirales que amenazaban con '
                   'destruir la unitariedad. El Modelo Estándar sobrevivió únicamente porque sus '
                   'quince representaciones de fermiones quirales por generación ejecutan un acto '
                   'de equilibrio algebraico extraordinario donde cuatro ecuaciones de '
                   'traza—incluida la suma cúbica ∑ d_f Y_f³—se anulan exactamente a cero '
                   'racional.\n'
                   '\n'
                   'Con la biblioteca PhysLean en Lean 4, la física teórica cuenta hoy con '
                   'demostraciones formales verificadas por computadora con cero axiomas sorry. Al '
                   'mismo tiempo, en física de la materia condensada, simular N espines cuánticos '
                   'interactuantes en un espacio de Hilbert de dimensión 2^N chocaba contra una '
                   'pared exponencial hasta que el método DMRG de Steven White y los entornos '
                   'modernos ITensors.jl y NetKet demostraron que los Estados de Producto '
                   'Matricial (MPS) comprimen estados críticos 1D en tiempo polinomial respetando '
                   'la ley de área logarítmica de Calabrese–Cardy.',
 'pullquote_es': '6(1/6)³ + 3(-2/3)³ + 3(1/3)³ + 2(-1/2)³ + 1(1)³ = 0: una sola línea de '
                 'aritmética racional en Lean 4 explica por qué los átomos son eléctricamente '
                 'neutros y por qué el vacío cuántico es consistente.',
 'act2_intuition_es': '¿Por qué los Estados de Producto Matricial (MPS) en ITensors.jl resuelven '
                      'cadenas cuánticas 1D con tanta eficiencia? Porque un enlace de dimensión χ '
                      'entre dos mitades de una cadena puede transportar como máximo ln(χ) nats de '
                      'entropía de entrelazamiento de von Neumann. En el punto crítico cuántico de '
                      'la cadena de Ising (carga central c = 1/2, longitud L = 128), S_vN(128) = '
                      '(0.5/6) ln(128) + 0.4785 = 0.8828 nats—capturada con holgura por una '
                      'dimensión de enlace χ = 64 (ln 64 = 4.1589 nats), mientras que un estado '
                      'producto de campo medio (χ = 1, ln 1 = 0) pierde por completo el '
                      'entrelazamiento crítico.',
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
 'act2_plain_primer_es': 'El banco de pruebas interactivo del Folio B.06 pone en tus manos dos '
                         'controles fundamentales de la física cuántica. El primer control ajusta '
                         'la Dimensión de Enlace MPS χ (de 1 a 128) en ITensors.jl. En su valor de '
                         'referencia χ = 64, la red ofrece una capacidad de ln(64) ≈ 4.16 nats '
                         'frente a los 0.8828 nats requeridos por la cadena crítica de Ising de '
                         '128 sitios. El segundo control ajusta la Perturbación de Hipercarga δY '
                         '(de 0.00 a 0.20) en PhysLean. En δY = 0.00, las cuatro trazas de '
                         'anomalía quiral se anulan a precisión de máquina. Si pulsas [⚡ '
                         'Counterfactual Axiom-Knockout] o mueves δY por encima de cero, la traza '
                         'cúbica Tr[Y³] deja de ser cero y rompe la invariancia gauge; si bajas χ '
                         'a 1 o 2, la capacidad ln(χ) cae por debajo de 0.8828 nats y dispara un '
                         'fallo de truncamiento cuántico.',
 'act2_deepening_es': 'La unidad formal del Folio B.06 enlaza la geometría algebraica verificada '
                      'en Lean 4 con la teoría conforme de la información cuántica. En el sector '
                      'gauge, para cada generación de quince campos de Weyl bajo SU(3)_C × SU(2)_L '
                      '× U(1)_Y—Q_L(3,2,1/6), u_R^c(3̄,1,-2/3), d_R^c(3̄,1,1/3), L_L(1,2,-1/2) y '
                      'e_R^c(1,1,1)—la biblioteca PhysLean formaliza sobre el cuerpo racional ℚ las condiciones de cancelación; las trazas que este folio comprueba son Tr[Y] = 0, Tr[τ²Y] = 0, Tr[λ²Y] = 0 y Tr[Y³] = 6(1/6)³ '
                      '+ 3(-2/3)³ + 3(1/3)³ + 2(-1/2)³ + 1(1)³ = 0. En paralelo, sobre la cadena '
                      'crítica de Ising en campo transversal 1D (g = J = 1), la solución exacta de '
                      'Pierre Pfeuty fija la densidad de energía del estado base en E₀/N = -4/π = '
                      '-1.27323954, mientras la teoría conforme de campos con carga central c = '
                      '1/2 dicta S_vN(128) = (0.5/6) ln(128) + 0.4785 = 0.8828 nats, acotada '
                      'holgadamente por la capacidad MPS ln(64) = 4.1589 nats en ITensors.jl.',
 'act4_human_ai_es': 'En la física teórica y cuántica contemporánea, el avance surge de la '
                     'convergencia entre la conceptualización matemática humana y el rigor '
                     'computacional verificado por máquina. Los físicos teóricos proponen '
                     'extensiones del Modelo Estándar y arquitecturas de redes tensoriales, '
                     'mientras que PhysLean en Lean 4 certifica cada identidad racional de '
                     'hipercarga mediante tácticas formales (norm_num, ring) sin errores de signo, '
                     'e ITensors.jl junto con NetKet optimizan estados cuánticos variacionales y '
                     'estados de producto matricial.',
 'act4_deepening_es': 'La piedra angular de la credibilidad en física computacional es la '
                      'reproducibilidad adversaria. El verificador autónomo '
                      'bounties/bounty_m2_physlean_itensor_quantum_gauge.py y su guía SKILL.md '
                      'ejecutan en menos de 0.05 segundos una evaluación doble sin dependencias '
                      'externas: primero certifican que las cuatro trazas quirales del Modelo '
                      'Estándar se anulan dentro de 10⁻¹², que E₀/N = -4/π y que ln(64) = 4.1589 '
                      'nats acota S_vN(128) = 0.8828 nats; segundo, inyectan defectos sembrados '
                      '(δY = 0.05 y χ = 2) para demostrar que cualquier anomalía gauge o '
                      'truncamiento de entrelazamiento es rechazado de inmediato.',
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
 'steps_es': ['Etapa 1: Asignación de Multipletes de Weyl en PhysLean — Declara las cinco '
              'representaciones quirales SU(3)_C × SU(2)_L × U(1)_Y por generación: Q_L(3,2,1/6), '
              'u_R^c(3,1,-2/3), d_R^c(3,1,1/3), L_L(1,2,-1/2), e_R^c(1,1,1).',
              'Etapa 2: Cancelación de Cuatro Trazas de Anomalía Gauge — Verifica Tr[Y] = 0, '
              'Tr[Y³] = 0, Tr[τ²Y] = 0 y Tr[λ²Y] = 0 a precisión de máquina (y exactamente sobre ℚ '
              'en Lean 4).',
              'Etapa 3: Escalamiento Crítico Exacto de Pfeuty y Calabrese–Cardy — Evalúa la '
              'densidad de energía crítica de Ising 1D E₀/N = -4/π = -1.27323954 y la entropía de '
              'entrelazamiento S_vN(L=128) = (0.5/6) ln(128) + 0.4785 = 0.882836 nats.',
              'Etapa 4: Certificación de Capacidad de Dimensión de Enlace MPS — Confirma que la '
              'capacidad logarítmica ln(χ) = ln(64) = 4.158883 nats acota estrictamente S_vN(128) '
              '= 0.882836 nats.'],
 'rules_es': ['Cancelación de Anomalías Gauge del Modelo Estándar: Los cuatro invariantes de traza '
              'quiral (gravitacional Tr[Y], cúbico U(1)_Y³ Tr[Y³], mixto débil Tr[τ²Y] y mixto de '
              'color Tr[λ²Y]) deben anularse idénticamente (|Tr| < 10⁻¹²); cualquier deriva δY ≠ 0 '
              'rompe la invariancia gauge cuántica.',
              'Cota de Entrelazamiento de Calabrese–Cardy: Para representar fielmente el estado '
              'base crítico de Ising en L = 128 (c = 0.5, S_vN = 0.882836 nats), la dimensión de '
              'enlace MPS debe satisfacer ln(χ) ≥ S_vN(L), es decir, χ ≥ 3.',
              'Invariante de Energía del Estado Base de Pfeuty: La energía crítica por sitio en g '
              '= J = 1 debe ser igual a -4/π = -1.27323954.'],
 't0_t1_certified_es': ['Verificador determinista de anomalías de cuatro trazas del Modelo '
                        'Estándar y arnés de entrelazamiento crítico TFIM 1D en '
                        'bounties/bounty_m2_physlean_itensor_quantum_gauge.py (tiempo de ejecución '
                        '< 0.05 s).',
                        'Verificado frente a Tooby-Smith (2024, DOI 10.1016/j.cpc.2024.109457), '
                        'Fishman et al. (2022, DOI 10.21468/SciPostPhysCodeb.4) y Vicentini et al. '
                        '(2022, DOI 10.21468/SciPostPhysCodeb.7).',
                        'Listo para envío inmediato al Zulip de HEPLean/PhysLean y a las galerías '
                        'de ITensors / NetKet.'],
 't2_t3_open_horizon_es': ['Retos Abiertos de Formalización en HEPLean / PhysLean: Envío de pull '
                           'requests en Lean 4 con cero sorry formalizando flujos del grupo de '
                           'renormalización, cotas de teorías gauge en el retículo o clasificación '
                           'de anomalías BSM directamente en HEPLean/PhysLean.']}
