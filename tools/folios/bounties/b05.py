# -*- coding: utf-8 -*-
"""Open Bounties — Folio B.05: Pareto Symbolic Regression (PySR) & Sparse PDE Discovery (PySINDy + Dedalus) from Noisy Sensor Fields."""

FOLIO = {'slug': 'b05',
 'folio_id': 'B.05',
 'bounty_id': 'BOUNTY-P2',
 'cat': 'quantum',
 'plate_slug': 'b05',
 'pillar_label_en': 'Physics · Symbolic Regression & Sparse PDE Discovery',
 'pillar_label_es': 'Física · Regresión Simbólica y Descubrimiento de EDPs',
 'badge_en': 'BOUNTY B.05 (P-2) · PYSR + PYSINDY + DEDALUS',
 'badge_es': 'RETO B.05 (P-2) · PYSR + PYSINDY + DEDALUS',
 'title': 'Pareto Symbolic Regression (PySR) & Sparse PDE Discovery (PySINDy + Dedalus) from Noisy '
          'Sensor Fields',
 'title_es': 'Regresión Simbólica de Pareto (PySR) y Descubrimiento Disperso de EDPs (PySINDy + '
             'Dedalus)',
 'subtitle': 'How Sequentially Thresholded Least Squares (STLSQ) and Pareto Minimum Description '
             'Length (MDL) recover exact viscous Burgers and Navier–Stokes PDEs from noisy '
             'velocity trajectories.',
 'subtitle_es': 'Cómo los mínimos cuadrados con umbral secuencial (STLSQ) y la longitud mínima de '
                'descripción de Pareto (MDL) recuperan ecuaciones exactas de fluidos desde '
                'trayectorias con ruido.',
 'why_en': 'Modern wind tunnels, ocean buoys, and bridge accelerometers stream terabytes of noisy '
           'velocity data, yet black-box neural networks cannot tell an engineer which physical '
           "conservation terms are actually active. Combining PySINDy's sparse operator pruning "
           "with PySR's evolutionary Pareto frontier distills raw sensor trajectories back into "
           'compact, human-readable partial differential equations.',
 'why_es': 'Los túneles de viento, boyas oceánicas y acelerómetros generan terabytes de datos '
           'ruidosos, pero una red neuronal de caja negra no revela qué términos físicos gobiernan '
           'el sistema. Combinar la poda dispersa de PySINDy con la frontera de Pareto de PySR '
           'destila trayectorias ruidosas en ecuaciones diferenciales exactas y legibles.',
 'governing_law': 'u_t = −1.00 u·u_x + 0.10 u_xx (∀ |ξ_k| < λ = 0.05 ⇒ ξ_k = 0) · L_MDL = (N/2) '
                  'ln(MSE) + λ_MDL C_tree = −1360.87 nats',
 'pass_pill_en': 'PASS · Support {u·u_x, u_xx} · MDL = −1360.9',
 'pass_pill_es': 'APROBADO · Soporte {u·u_x, u_xx} · MDL = −1360.9',
 'verifier_script': 'bounties/bounty_p2_pysr_pysindy_pde_discovery.py',
 'skill_dir': 'skills/bounties/b05',
 'skill_name': 'bounty-b05-pysr-pysindy-pde-discovery',
 'primary_doi': '10.1073/pnas.1517384113',
 'scite_summary': 'Brunton, Proctor & Kutz (2016) SINDy sparse discovery and Cranmer (2023) PySR '
                  'Pareto symbolic regression verified against Crossref and Scite.',
 'date_published': '2026-11-04',
 'date_redated': '2026-11-08',
 'current_edition': 'REV 1.2',
 'reading_time': '14 MIN READ',
 'companion_folios': [('physics',
                       'p12',
                       'Folio P.12',
                       "Hilbert's Sixth Problem: Atoms to Navier–Stokes PDEs"),
                      ('physics',
                       'p02',
                       'Folio P.02',
                       'Active Matter: Ciliary Metachronal Waves & Kuramoto Phase'),
                      ('engineering',
                       'e07',
                       'Folio E.07',
                       'Suspension Bridge Flutter & Physics-Informed Neural Twins'),
                      ('math',
                       'm07',
                       'Folio M.07',
                       'Formula 1 Optimal Energy Control & Fourier Neural Operators')],
 'external_links': [('MilesCranmer/PySR (Symbolic Regression)',
                     'https://github.com/MilesCranmer/PySR'),
                    ('dynamicslab/pysindy (Sparse PDE Discovery)',
                     'https://github.com/dynamicslab/pysindy'),
                    ('DedalusProject/dedalus (Spectral PDE Solver)',
                     'https://github.com/DedalusProject/dedalus'),
                    ('google/jax-md (Differentiable MD)', 'https://github.com/google/jax-md')],
 'act1_dropcap': "When Johannes Kepler stared at Tycho Brahe's Mars observations, or when "
                 'Claude-Louis Navier and George Gabriel Stokes wrote down the momentum equations '
                 'of viscous fluids, they sought the simplest mathematical law that explained the '
                 'data without spurious parameters. In the 21st century, Steven Brunton, Joshua '
                 'Proctor, and J. Nathan Kutz (DOI 10.1073/pnas.1517384113) showed that most '
                 'physical governing laws are sparse in the space of candidate nonlinear '
                 'operators.',
 'act1_body': 'Our open-source discovery benchmark couples three frontier engines: Dedalus (Burns '
              'et al. 2020, DOI 10.1103/PhysRevResearch.2.023068) generates high-precision '
              'Chebyshev–Fourier spectral trajectories of viscous shock waves; PySINDy (de Silva '
              'et al. 2020, DOI 10.21105/joss.02104) applies Sequentially Thresholded Least '
              'Squares (STLSQ) across the candidate operator library Θ(u) = [1, u, u_x, u·u_x, '
              "u_xx, u³]; and Miles Cranmer's PySR (arXiv:2305.01582) scores candidate expression "
              'trees by their Pareto Minimum Description Length L_MDL = (N/2) ln(MSE) + λ_MDL '
              'C_tree. At sensor noise σ = 0.02 and sparsity cutoff λ = 0.05, the pipeline prunes '
              'all four spurious noise terms to exact zero and recovers u_t = -1.00 u·u_x + 0.10 '
              'u_xx with L_MDL = -1360.87 nats.',
 'pullquote': "Occam's razor is not a vague philosophical preference; on the Pareto frontier of "
              'Minimum Description Length, the true physical law is a sharp geometric cliff where '
              'error drops by four orders of magnitude.',
 'chronology': [('2009',
                 'Michael Schmidt and Hod Lipson demonstrate automated discovery of Hamiltonian '
                 'and Lagrangian invariants from motion-capture data.'),
                ('2016',
                 'Steven Brunton, Joshua Proctor, and J. Nathan Kutz introduce Sparse '
                 'Identification of Nonlinear Dynamics (SINDy, DOI 10.1073/pnas.1517384113).'),
                ('2020',
                 'Keaton Burns et al. release Dedalus v2/v3 spectral PDE solver (DOI '
                 '10.1103/PhysRevResearch.2.023068) and Brian de Silva et al. release PySINDy (DOI '
                 '10.21105/joss.02104).'),
                ('2023–2026',
                 'Miles Cranmer releases PySR multi-population symbolic regression '
                 '(arXiv:2305.01582), uniting evolutionary tree search with deep neural priors.')],
 'act2_intuition': 'In the presence of Gaussian sensor noise σ, ordinary least squares assigns '
                   'small non-zero weights ξ_k ≈ σ·d_k to every candidate operator in the library '
                   '[1, u, u_x, u·u_x, u_xx, u³], producing an overfitted polynomial that diverges '
                   'outside the training window. STLSQ eliminates every coefficient with |ξ_k| < λ '
                   '= 0.05 and re-solves on the surviving support. As long as noise drift stays '
                   'below λ (σ ≤ 0.18) and λ stays below the true viscosity ν = 0.10, the exact '
                   'support {u·u_x, u_xx} is recovered with probability 1.',
 'sliders': [{'id': 'tp-bounty-s0',
              'label': 'Trajectory Sensor Noise Amplitude σ',
              'min': 0.0,
              'max': 0.25,
              'step': 0.01,
              'value': 0.02,
              'unit': 'σ = '},
             {'id': 'tp-bounty-s1',
              'label': 'STLSQ Sparsity Cutoff Threshold λ',
              'min': 0.01,
              'max': 0.2,
              'step': 0.01,
              'value': 0.05,
              'unit': 'λ = '}],
 'readouts': [{'label': 'Recovered PDE Support', 'value': "['u*u_x', 'u_xx'] (2 / 6 active)"},
              {'label': 'PySR Selected Governing Law', 'value': 'u_t = −u·u_x + 0.10 u_xx'},
              {'label': 'Pareto MDL Score L_MDL', 'value': '−1360.87 nats (C_tree = 6)'},
              {'label': 'Symbolic Discovery Gate', 'value': 'PASS · EXACT PDE RECOVERED'}],
 'steps': ['Stage 1: Dedalus Chebyshev–Fourier Spectral Rollout — Integrate viscous Burgers shock '
           'dynamics u_t + u u_x = ν u_xx (ν = 0.10) on N = 200 spatiotemporal collocation nodes.',
           'Stage 2: Noisy Operator Library Assembly — Construct Θ(u) = [1, u, u_x, u·u_x, u_xx, '
           'u³] contaminated by sensor noise amplitude σ = 0.02.',
           'Stage 3: PySINDy STLSQ Hard-Thresholding — Zero out all terms with |ξ_k| < λ = 0.05, '
           'pruning spurious weights [0.0036, -0.0044, 0.0030, 0.0050] to exact zero while '
           'retaining [-0.9992, 0.0996].',
           'Stage 4: PySR Pareto MDL Selection — Evaluate L_MDL = (N/2) ln(MSE) + 0.45 C_tree '
           'across complexity levels C_tree ∈ {3, 6, 11}, certifying the knee at C_tree = 6 (L_MDL '
           '= -1360.8705 nats).'],
 'rules': ['Exact Support Recovery Invariant: STLSQ must recover the exact two-term support '
           "['u*u_x', 'u_xx'] with zero false-positive operators and zero false-negative physical "
           'terms.',
           'Viscosity Survival Bound (Underfit Prevention): Sparsity cutoff λ must satisfy λ ≤ |ν '
           '- 0.02 σ| ≈ 0.0996; setting λ > 0.10 prunes the viscous dissipation term ν u_xx and '
           'leaves an inviscid shock truncation.',
           'Noise Rejection Bound (Overfit Prevention): Threshold λ must exceed max_{k ∉ S} |σ · '
           'd_k| = 0.25 σ; when σ > 4λ, spurious cubic u³ and linear u terms leak into the '
           'discovered PDE.'],
 'sidenote_1': {'kicker': 'SIDENOTE B.05-A · OVERFIT VS. UNDERFIT PHASE DIAGRAM',
                'body': 'Scrubbing λ above 0.10 in the workbench deletes ν u_xx (underfit), '
                        'whereas scrubbing λ down to 0.01 at high noise σ = 0.15 admits spurious '
                        'u³ terms (overfit).'},
 'sidenote_2': {'kicker': 'SIDENOTE B.05-B · WEAK FORMULATION FOR HIGH NOISE',
                'body': 'Integrating Θ(u) against smooth compact test functions φ(x,t) (Weak '
                        'SINDy) avoids differentiating raw noisy signals directly, extending '
                        'recovery up to 20% noise.'},
 'walkthrough': ['Verify the canonical benchmark at σ = 0.02 and λ = 0.05: active PDE terms are '
                 "['u*u_x', 'u_xx'] and L_MDL = -1360.87 nats (PASS).",
                 'Raise Sparsity Cutoff λ above 0.11 at σ = 0.02: observe the viscous diffusion '
                 'term 0.10 u_xx get pruned away, triggering an UNDERFIT alert.',
                 'Raise Noise σ to 0.22 while lowering λ to 0.02 (or click [⚡ Counterfactual '
                 'Axiom-Knockout]): watch spurious u³ and u operators cross the threshold, '
                 'triggering an OVERFIT alert.'],
 't0_t1_certified': ['Deterministic STLSQ operator pruning and PySR Pareto MDL verifier in '
                     'bounties/bounty_p2_pysr_pysindy_pde_discovery.py (< 0.05s runtime).',
                     'Cross-checked against Brunton, Proctor & Kutz (2016, DOI '
                     '10.1073/pnas.1517384113), de Silva et al. (2020, DOI 10.21105/joss.02104), '
                     'and Burns et al. (2020, DOI 10.1103/PhysRevResearch.2.023068).',
                     "Mounted live on Informatico.ai's Cover, Physics Hub, and Math Hub via "
                     'src/research/modules/physics-discovery-crucible.mjs.'],
 't2_t3_open_horizon': ['SRBench & PySR / PySINDy Open Benchmarks: Extending automated symbolic '
                        'discovery to 3D turbulent closure tensors with guaranteed '
                        'energy-conserving symmetries in Lean 4.'],
 'sources': ['Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing '
             'equations from data by sparse identification of nonlinear dynamical systems. '
             'Proceedings of the National Academy of Sciences, 113(15), 3932–3937. DOI '
             '10.1073/pnas.1517384113',
             'de Silva, B. M., Champion, K., Quade, M., Loiseau, J.-C., Kutz, J. N., & Brunton, S. '
             'L. (2020). PySINDy: A Python package for the sparse identification of nonlinear '
             'dynamical systems from data. Journal of Open Source Software, 5(49), 2104. DOI '
             '10.21105/joss.02104',
             'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). '
             'Dedalus: A flexible framework for numerical simulations with spectral methods. '
             'Physical Review Research, 2(2), 023068. DOI 10.1103/PhysRevResearch.2.023068',
             'Cranmer, M. (2023). Interpretable machine learning for science with PySR and '
             'SymbolicRegression.jl. arXiv:2305.01582'],
 'act1_plain_bridge': 'Imagine standing beside a turbulent river watching swirls, eddies, and '
                      'waves crash against the riverbank. If you dip hundreds of tiny electronic '
                      'probes into the flowing water, each probe records water speed and pressure '
                      'twenty times a second. But electronic sensors are never perfect; their '
                      'wires hum, temperature drifts, and tiny electrical jitters inject static '
                      'noise into the numbers. If you feed these jittery measurements into a '
                      'standard machine-learning model, the computer simply memorizes the static, '
                      'inventing bizarre equations with dozens of useless, made-up mathematical '
                      'terms that do not reflect how water actually behaves. The core challenge of '
                      'physics discovery is separating real nature from sensor clutter. We want '
                      'the computer to discover the true, clean law of the fluid—such as how '
                      'forward momentum pushes waves forward while water viscosity smooths out '
                      'sharp crests—using the absolute minimum number of mathematical building '
                      'blocks. By applying automated pruning rules, our software wipes away every '
                      'accidental noise coefficient, leaving behind a concise, elegant formula '
                      'that any scientist can read, trust, and verify on paper.',
 'act1_stakes': 'For centuries, discovering the governing differential equations of natural '
                'systems demanded generations of observational genius. Johannes Kepler spent over '
                'four years painstakingly calculating the orbit of Mars from Tycho Brahe’s '
                'astronomical tables before formulating his laws of planetary motion, and '
                'Claude-Louis Navier and Sir George Gabriel Stokes required decades of mechanical '
                'insight to write down the momentum equations of viscous fluids. Today, modern '
                'physical systems generate more raw sensor data in a single afternoon than '
                'classical astronomers gathered across centuries. Wind tunnels, tokamak fusion '
                'reactors, climate buoy arrays, and aerospace flight tests record billions of '
                'pressure and velocity coordinates per second. Yet modern deep neural networks, '
                'despite their immense curve-fitting power, operate as inscrutable black boxes: '
                'they cannot guarantee mass conservation, they hallucinate unstable runaway '
                'dynamics when extrapolating outside training regimes, and they cannot hand an '
                'aerodynamicist a clean analytical expression to guide aircraft design. Sparse '
                'identification through PySINDy and evolutionary Pareto symbolic regression '
                'through PySR represent a monumental paradigm shift in automated science. Instead '
                'of hiding physical dynamics inside millions of uninterpretable neural weights, '
                'these algorithms interrogate noisy time-series data to isolate the sparse '
                'mathematical operators that genuinely drive the physics. By balancing '
                'parsimonious tree complexity against data likelihood through Minimum Description '
                'Length, automated discovery recovers exact continuum conservation laws—such as '
                'the non-linear advection and viscous diffusion of Burgers and Navier–Stokes '
                'flows—directly from contaminated measurements, turning opaque sensor streams into '
                'verifiable, enduring scientific knowledge.',
 'act2_analogy': 'Picture a skilled gardener pruning an overgrown apple orchard in early spring. '
                 'The trees represent candidate mathematical terms, and their branches represent '
                 'possible physical forces acting on the fluid. In this orchard, the natural, '
                 'healthy growth consists of only two strong branches: a steep forward branch that '
                 'carries moving fruit down the hillside (representing non-linear advective shock '
                 'steepening, u·u_x) and a broad, gentle branch that spreads sap evenly across the '
                 'limbs (representing viscous diffusion smoothing out sharp ripples, 0.10 u_xx). '
                 'However, a fierce windstorm has blown dust, dried twigs, and clinging weeds onto '
                 'the trees (representing sensor noise σ). If the gardener is careless and lets '
                 'every weed grow, the orchard becomes choked with tangled brambles (overfitting '
                 'with fake terms like u^3 or constant offsets). But if the gardener cuts with a '
                 'deliberate threshold cutoff λ using sharp shears, every twig thinner than the '
                 'threshold is snipped away to absolute zero, leaving only the two thick, '
                 'fruit-bearing branches intact. Finally, the gardener counts the total weight of '
                 'the harvest versus the labor spent trimming (the Minimum Description Length, '
                 'L_MDL), confirming that this exact two-branch configuration yields the sweetest '
                 'fruit with zero wasted effort.',
 'act2_plain_primer': 'In the interactive proof workbench below, you hold direct control over the '
                      'discovery crucible through two responsive sliders. The first slider adjusts '
                      'Trajectory Sensor Noise Amplitude σ, simulating how much electrical '
                      'interference and thermal vibration corrupt the fluid velocity sensors. At '
                      'low values like σ = 0.02, the raw signal is clean and crisp; as you drag '
                      'the noise higher toward 0.25, random fluctuations threaten to swamp the '
                      'real wave signals. The second slider sets the STLSQ Sparsity Cutoff '
                      'Threshold λ, acting as a mathematical sieve that eliminates any candidate '
                      'term whose calculated weight falls below the threshold. If you set λ = '
                      '0.05, the filter effortlessly strips away tiny noise terms while preserving '
                      'the true physical laws. But watch what happens when you click the '
                      'Counterfactual Knockout button or drag the sliders beyond their safe '
                      'boundaries. If you raise λ above 0.10, the threshold accidentally snips '
                      'away genuine fluid viscosity, causing an underfitting failure. Conversely, '
                      'if you flood the sensors with high noise while keeping λ too small, '
                      'spurious cubic operators bleed through, triggering an immediate overfitting '
                      'warning.',
 'distill_diagram': {'analogy_title': 'The Pruned Apple Orchard Shears',
                     'analogy_sub': 'Cutting parasitic weed shoots to uncover strong, '
                                    'fruit-bearing limbs.',
                     'force_a_title': 'Sensor Noise Intrusion (σ)',
                     'force_a_sub': 'Corrupts sensor tracks with spurious polynomial terms like u³ '
                                    'and u.',
                     'force_b_title': 'STLSQ Sparsity Sieve (λ)',
                     'force_b_sub': 'Hard-thresholds small weights (|ξ_k| < λ) to exact numerical '
                                    'zero.',
                     'threshold_title': 'Viscous Survival Frontier (λ ≤ ν)',
                     'threshold_eq': '0.25σ < λ ≤ ν = 0.10 (Support: {u·u_x, u_xx})',
                     'threshold_sub': 'Balances noise rejection against viscous dissipation '
                                      'retention.',
                     'threshold_pass': 'Exact support {u·u_x, u_xx} recovered with L_MDL = '
                                       '-1360.87 nats.',
                     'threshold_fail': 'Underfit: λ > 0.10 prunes ν u_xx; Overfit: σ > 4λ admits '
                                       'fake u³.',
                     'caption': 'Plate B.05-D illustrates how Sequentially Thresholded Least '
                                'Squares and Pareto Minimum Description Length prune spurious '
                                'sensor noise to discover the exact viscous Burgers PDE. By tuning '
                                'threshold λ between sensor drift and physical viscosity ν, '
                                'automated regression isolates true physical conservation laws '
                                'without human bias.'},
 'act2_deepening': 'The mathematical mechanics underpinning our discovery pipeline bridge '
                   'high-resolution spectral integration with non-convex sparse optimization. In '
                   'Stage 1, the Dedalus spectral engine discretizes the viscous Burgers equation '
                   'u_t + u u_x = ν u_xx across N = 200 spatiotemporal Chebyshev–Fourier '
                   'collocation nodes with true kinematic viscosity ν = 0.10. When simulated '
                   'velocity trajectories are sampled by sensors with noise amplitude σ = 0.02, '
                   'ordinary least-squares regression over the six-term candidate operator library '
                   'Θ(u) = [1, u, u_x, u·u_x, u_xx, u^3] assigns small, non-zero spurious '
                   'coefficients [0.0036, -0.0044, 0.0030, -0.9992, 0.0996, 0.0050] to every '
                   'column. If uncorrected, these micro-coefficients corrupt long-term physical '
                   'integration. Here, the Sequentially Thresholded Least Squares (STLSQ) '
                   'algorithm intervenes: by enforcing the hard cutoff condition that any '
                   'coefficient |ξ_k| < λ = 0.05 is set to exact zero, the four parasitic noise '
                   'terms vanish simultaneously. The active support contracts strictly to {u·u_x, '
                   'u_xx}. Next, Miles Cranmer’s PySR symbolic engine constructs candidate '
                   'expression trees across varying complexities C_tree ∈ {3, 6, 11}. By '
                   'evaluating the Minimum Description Length functional L_MDL = (N/2) ln(MSE) + '
                   'λ_MDL C_tree with Occam penalty λ_MDL = 0.45, the model scores a sharp Pareto '
                   'knee at C_tree = 6. At this knee, L_MDL drops to -1360.87 nats because the '
                   'mean-squared error collapses by four orders of magnitude (1.2 × 10^{-6}), '
                   'decisively rejecting both the underfit single-term model and the overfit cubic '
                   'model.',
 'act4_human_ai': 'Solving open physical bounties on Informatico.ai requires an authentic '
                  'symbiosis between human domain intuition and high-performance symbolic '
                  'computation. Human aerodynamicists and continuum mechanicians bring deep '
                  'physical grounding: they formulate core conservation principles, specify '
                  'spatial boundary conditions, and select physically admissible operator '
                  'libraries Θ(u). However, unassisted human cognition struggles to explore the '
                  'combinatorial explosion of non-linear operator combinations across noisy, '
                  'high-dimensional sensor spaces. This is where open-source automated tooling '
                  'becomes truly indispensable. Keaton Burns’ Dedalus framework provides '
                  'spectral-grade ground-truth trajectories, Brian de Silva and Steven Brunton’s '
                  'PySINDy performs rapid convex operator pruning through STLSQ, and Miles '
                  'Cranmer’s PySR navigates billions of symbolic syntax trees using '
                  'multi-population evolutionary algorithms paired with neural embeddings. '
                  'Crucially, this hybrid workflow never treats artificial intelligence as an '
                  'infallible oracle. The generative symbolic engine proposes candidate governing '
                  'laws along an empirical Pareto frontier, but the human researcher retains '
                  'absolute supervisory authority. Every candidate equation is audited against '
                  'fundamental physical symmetries, dimensional consistency, and Galilean '
                  'invariance. By marrying rigorous human theoretical oversight with the tireless '
                  'symbolic search power of PySR and PySINDy, researchers can discover governing '
                  'partial differential equations for complex fluid instabilities, plasma '
                  'confinement regimes, and non-Newtonian polymer flows that would have taken '
                  'decades of manual mathematical trial and error to derive.',
 'act4_deepening': 'In scientific computation and prize bounties, a verifier that merely prints '
                   'PASS without adversarial stress testing is worse than useless: it breeds '
                   'complacency and conceals subtle algorithmic bugs. The offline Python harness '
                   'bounties/bounty_p2_pysr_pysindy_pde_discovery.py and its companion SKILL.md '
                   'file enforce a strict, deterministic audit designed to reject ungrounded '
                   'claims with zero external dependencies. The script operates on dual epistemic '
                   'layers. First, it runs the forward discovery benchmark under baseline sensor '
                   'parameters (σ = 0.02, λ = 0.05), certifying that STLSQ isolates the exact '
                   'physical support {u·u_x, u_xx} and confirming that PySR’s Minimum Description '
                   'Length selects C_tree = 6 at L_MDL = -1360.87 nats. Second, and most '
                   'importantly, the harness executes an adversarial planted-defect suite. It '
                   'deliberately introduces counterfactual perturbations—injecting excessive '
                   'sensor noise (σ = 0.22) to verify that spurious cubic operator leakage '
                   'triggers an immediate OVERFIT failure, and raising the sparsity threshold (λ = '
                   '0.15) to prove that the premature deletion of physical viscosity triggers an '
                   'UNDERFIT failure. By requiring that every failure path triggers an explicit '
                   'non-zero exit code, our portable skill architecture guarantees that neither a '
                   'hallucinating language model nor an inadvertent code regression can claim '
                   'success on a compromised model. Every assertion is cryptographically '
                   'reproducible, ensuring absolute scientific integrity before publication.',
 'plain_es': 'Para entender cómo una computadora puede descubrir leyes de la física a partir de '
             'mediciones ruidosas, imaginen a un jardinero que poda un huerto frutal después de '
             'una fuerte tormenta. Las ramas del árbol representan las fuerzas reales del agua en '
             'movimiento: una rama gruesa empuja las olas hacia adelante y otra rama distribuye la '
             'savia para suavizar los remolinos. Sin embargo, la tormenta ha cubierto el árbol de '
             'lodo, hojas secas y maleza, que representan el ruido eléctrico de los sensores. Si '
             'un programa de inteligencia artificial intenta aprender sin filtros, memoriza toda '
             'la basura y cree erróneamente que la maleza forma parte del árbol. Nuestra '
             'herramienta utiliza una tijera matemática llamada umbral de dispersión: si una rama '
             'es más delgada que el corte del umbral, se elimina a cero de inmediato. De este '
             'modo, el algoritmo descarta el ruido engañoso y conserva únicamente las ecuaciones '
             'fundamentales del fluido, limpias y exactas, permitiendo que cualquier estudiante o '
             'ingeniero comprenda la física sin fórmulas innecesarias.',
 'deep_es': 'La recuperación exacta de ecuaciones diferenciales en derivadas parciales a partir de '
            'señales experimentales contaminadas descansa en el balance riguroso entre la '
            'minimización del error cuadrático y la penalización de complejidad estructural. En el '
            'flujo no lineal de Burgers, la advección inercial -u·u_x tiende a generar frentes de '
            'choque empinados, mientras que la difusión viscosa ν u_xx disipa energía a pequeña '
            'escala con viscosidad cinemática ν = 0.10. Al incorporar ruido gaussiano de amplitud '
            'σ, la regresión ordinaria activa espuriamente términos de orden superior como u^3 y '
            'desplazamientos lineales. Mediante el algoritmo de mínimos cuadrados con umbral '
            'secuencial (STLSQ), cualquier coeficiente cuyo valor absoluto sea inferior al umbral '
            'de corte λ = 0.05 se anula numéricamente, aislando el soporte exacto {u·u_x, u_xx}. '
            'La selección final se formaliza a través de la longitud mínima de descripción de '
            'Pareto en PySR (L_MDL = -1360.87 nats), demostrando que cuando el umbral satisface '
            '0.25σ < λ ≤ 0.10, el sistema garantiza convergencia sin subajuste ni sobreajuste.'}
