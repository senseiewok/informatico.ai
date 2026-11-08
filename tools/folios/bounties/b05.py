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
             'SymbolicRegression.jl. arXiv:2305.01582']}
