#!/usr/bin/env python3
"""Folio M.09 (MATH): Monge–Kantorovich Optimal Transport, Benamou–Brenier Wasserstein-2 Geodesic Fluid Dynamics, Sinkhorn Entropic Regularization & Flow Matching."""
from __future__ import annotations

SLUG = 'm09'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.09',
 'slug': 'm09',
 'pillar': 'math',
 'category_code': 'M',
 'parent_folios': ['M.04', 'M.07', 'M.08'],
 'lineage_mode': 'TRIAD_SYNTHESIS · Synthesizes M.04 PFR Entropic Distance, M.07 Pontryagin '
                 'Control & M.08 Riemannian Geodesics',
 'title': 'Monge–Kantorovich Optimal Transport, Benamou–Brenier Wasserstein-2 Geodesic Fluid '
          'Dynamics, Sinkhorn Entropic Regularization & Flow Matching',
 'subtitle': 'Synthesizing Folios M.04, M.07, and M.08: how Jean-David Benamou and Yann Brenier '
             'recast quadratic Wasserstein-2 optimal transport as a pressureless fluid flow of '
             'least kinetic energy. Numerical readouts shown here are fixed illustrative model '
             'values.',
 'date_published': '2026-11-03',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'OPTIMAL TRANSPORT · REV 1.1',
 'primary_kernel': 'tools/discovery/frontier_ai_math_catalog.py',
 'governing_law': 'W_2²(μ_0, μ_1) = inf ∫_0^1 ∫ ρ|v|² dx dt · ∂_t ρ + ∇·(ρ∇ψ) = 0 · ∂_t ψ + ½|∇ψ|² '
                  '= 0',
 'colophon': {'identifier': 'M.09 · Benamou–Brenier Wasserstein-2 Optimal Transport',
              'kernels': 'Benamou–Brenier Continuity & HJB · Brenier Convex Potential ∇Φ · '
                         'Sinkhorn Scaling',
              'benchmarks': 'Illustrative 1D Gaussians: W_2² = 4.82 · t = 0.50 (σ = 1.15) · ε = '
                            '0.05 (18 steps)',
              'bridge': 'Synthesizes M.04/M.07/M.08 · Waddington-OT trajectory inference '
                        '(Schiebinger et al. 2019) as a method reference'},
 'sliders': [{'label': 'McCann Geodesic Transport Time (t_geo)',
              'min': 0.0,
              'max': 1.0,
              'step': 0.05,
              'value': 0.5,
              'unit': 't = '},
             {'label': 'Sinkhorn Entropic Regularization (eps_reg)',
              'min': 0.01,
              'max': 0.5,
              'step': 0.01,
              'value': 0.05,
              'unit': 'ε = '}],
 'steps': ['Stage 1 (Kantorovich Couplings): Relaxes Monge maps T_# μ_0 = μ_1 into a linear '
           'program over couplings π ∈ Π(μ_0, μ_1) when discrete mass splits (DOI '
           '10.1561/2200000073).',
           'Stage 2 (Brenier Polar Factorization, DOI 10.1002/cpa.3160440402): When μ_0, μ_1 ∈ '
           'P_2(ℝ^d) and μ_0 vanishes on Lebesgue-null sets, T(x) = ∇Φ(x) = x + ∇ψ_0(x) for convex '
           'Φ.',
           'Stage 3 (Benamou–Brenier Geodesic, DOI 10.1007/s002110050002): Minimizing ½∬ ρ|v|² dx '
           'dt = ½W_2² under ∂_t ρ + ∇·(ρv) = 0 gives v = ∇ψ and ∂_t ψ + ½|∇ψ|² = 0 (DOI '
           '10.1006/aima.1997.1634).',
           'Stage 4 (Sinkhorn Scaling, arXiv:1306.0895): Penalty ε KL(π || μ_0⊗μ_1) gives π_ij = '
           'u_i K_ij v_j with K_ij = exp(−||x_i − y_j||² / ε) and O(ε) bias (18 steps fixed '
           'illustrative).'],
 'readouts': [{'label': 'Squared Wasserstein Distance (W_2², model)',
               'value': '4.82 (fixed illustrative Gaussian pair)'},
              {'label': 'Midpoint Mean & Spread (t = 0.50, model)',
               'value': 'μ_0.5 = 0.00 · σ_0.5 = 1.15 (fixed illustrative)'},
              {'label': 'Sinkhorn Scaling Step Count (model)',
               'value': '18 steps at ε = 0.05 (fixed illustrative)'},
              {'label': 'Model Geometry',
               'value': 'Benamou–Brenier geodesic (teaching model, not a solver)'}],
 'spec_plate': {'division': 'APPLIED MATHEMATICS & OPTIMAL TRANSPORT · TEACHING STUDY',
                'title': 'Benamou–Brenier Fluid Geodesic & Entropic Sinkhorn Study',
                'body': 'Teaching study pairing Monge–Kantorovich couplings, Benamou–Brenier '
                        'continuity and Hamilton–Jacobi equations, 1D Gaussian displacement '
                        'interpolation, and Sinkhorn scaling under stated assumptions. No solver '
                        'runs here; readouts are fixed illustrative text.',
                'meta': 'Cited, not reproduced: Brenier 1991 (DOI 10.1002/cpa.3160440402) · '
                        'Benamou & Brenier 2000 (DOI 10.1007/s002110050002) · Peyré & Cuturi 2019 '
                        '(DOI 10.1561/2200000073)'},
 'sidenote_1': {'kicker': 'SIDENOTE M.09-A · OTTO CALCULUS (2001) & MONGE–AMPÈRE CAVEAT',
                'body': 'Felix Otto (2001, DOI 10.1081/PDE-100002243) introduced a formal '
                        'Riemannian calculus on probability densities for porous-medium gradient '
                        'flows. For smooth positive densities f and g with g ∘ ∇Φ > 0, det(D²Φ) = '
                        'f / (g ∘ ∇Φ) holds classically, and in a weak Aleksandrov sense '
                        'otherwise.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.09-B · SNAPSHOT TRAJECTORY INFERENCE (WADDINGTON-OT)',
                'body': 'Because single-cell RNA sequencing destroys cells at each timepoint, '
                        'Schiebinger et al. (2019, DOI 10.1016/j.cell.2019.01.006; erratum DOI '
                        '10.1016/j.cell.2019.02.026) used optimal transport across 315,000 '
                        'profiles over 18 days to estimate ancestor-descendant couplings.'},
 'skill': {'filename': 'wasserstein-optimal-transport-benamou-brenier-SKILL.md',
           'name': 'wasserstein-optimal-transport-benamou-brenier',
           'description': 'AI-agnostic optimal-transport skill for Monge-Kantorovich couplings, '
                          'Brenier polar factorization, Benamou-Brenier Wasserstein-2 fluid '
                          'geodesics, Bures-Wasserstein Gaussian displacement interpolation, and '
                          'entropic Sinkhorn scaling.',
           'rules': ['Relate W_2^2(mu_0, mu_1) = inf int_0^1 int rho |v|^2 dx dt under d_t rho + '
                     'nabla.(rho v) = 0 to kinetic saddle point (1/2) W_2^2 = inf int_0^1 int '
                     '(1/2) rho |v|^2 dx dt, giving v = nabla psi and d_t psi + (1/2)|nabla psi|^2 '
                     '= 0 (DOI 10.1007/s002110050002).',
                     'Check that mu_0 vanishes on Lebesgue-null sets before asserting T = nabla '
                     'Phi (DOI 10.1002/cpa.3160440402), and interpolate both mean m_t = (1-t)m_0 + '
                     't m_1 and covariance along McCann paths (DOI 10.1006/aima.1997.1634; DOI '
                     '10.1016/j.exmath.2018.01.002).',
                     'Stabilize Sinkhorn scaling pi_ij = u_i exp(-c_ij / epsilon) v_j in the log '
                     'domain for small epsilon > 0, note its O(epsilon) bias (arXiv:1306.0895), '
                     'and state when readouts are fixed illustrative values.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. W_2² = 4.82, σ_t = '
                           '1.15 and the 18 Sinkhorn steps are now labeled as illustrative values '
                           "(the Gaussian parameters behind them are not stated), and the 'QED "
                           "PASS' verdict is withdrawn. The claims that optimal transport has "
                           'reconstructed basal-to-ionocyte trajectories and that flow matching '
                           'designs lipid nanoparticles are withdrawn; the bridge now describes a '
                           'possible analysis, sourced to Schiebinger et al. 2019 and the 2018 '
                           'ionocyte papers. The invented 1781 scene is trimmed.',
                'opus': 'Review: all DOIs checked in Crossref and the Scite index on 2026-11-14. '
                        'Added Schiebinger et al. 2019 (DOI 10.1016/j.cell.2019.01.006), Montoro '
                        'et al. 2018 (DOI 10.1038/s41586-018-0393-7) and Plasschaert et al. 2018 '
                        '(DOI 10.1038/s41586-018-0394-6).'},
               {'edition': 'REV 1.0',
                'date': '2026-11-03',
                'summary': 'REV 1.0 (Published 2026-11-03): Volume V mathematical monograph '
                           "synthesizing Folios M.04, M.07 & M.08 via Benamou & Brenier's dynamic "
                           'fluid formulation of Wasserstein-2 optimal transport (DOI '
                           '10.1007/s002110050002).',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Bures-Wasserstein closed-form metric, HJB optimality d_t psi + 0.5|nabla '
                        "psi|^2 = 0, and log-Sinkhorn convergence. (REV 1.1: this 'verified' "
                        'wording is withdrawn; no independent check was run.)'}],
 'volume': 5,
 'volume_code': 'VOL. 05',
 'reading_time': '19 MIN READ',
 'word_count': '4,550 WORDS',
 'scite': {'doi': '10.1007/s002110050002',
           'fetched_on': '2026-11-22',
           'citing_publications': 2137,
           'supporting': 19,
           'mentioning': 2121,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index [observed: Scite ML citation classification, accessed '
                      '2026-11-22]: 0 retractions; 2,137 citing publications (19 supporting, 2,121 '
                      'mentioning, 0 contrasting citation statements) for Benamou & Brenier 2000 '
                      '(DOI 10.1007/s002110050002). Counts describe that paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '19 MIN READ',
 'word_count': '4,550 WORDS',
 'parent_folios': ['M.04', 'M.07', 'M.08'],
 'lineage_mode': 'TRIAD_SYNTHESIS · Synthesizes M.04 PFR Entropic Distance, M.07 Pontryagin '
                 'Control & M.08 Riemannian Geodesics',
 'scite': {'doi': '10.1007/s002110050002',
           'fetched_on': '2026-11-22',
           'citing_publications': 2137,
           'supporting': 19,
           'mentioning': 2121,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index [observed: Scite ML citation classification, accessed '
                      '2026-11-22]: 0 retractions; 2,137 citing publications (19 supporting, 2,121 '
                      'mentioning, 0 contrasting citation statements) for Benamou & Brenier 2000 '
                      '(DOI 10.1007/s002110050002). Counts describe that paper, not this folio.'},
 'act1_title': 'Act I — Uniting M.04 Entropy, M.07 Optimal Control & M.08 Riemannian Geodesics: '
               "From Gaspard Monge's Earthworks to Wasserstein-2 Fluid Dynamics",
 'act1_dropcap': 'In 1781 the French mathematician Gaspard Monge presented a famous memoir in '
                 'Paris on cuts and fills for moving excavated soil into distant trenches. Workers '
                 'had to haul every single shovelful with minimal total labor. Crossing cart paths '
                 'wasted effort, while splitting one load across separate pits broke the '
                 'assumption of a strict one-to-one assignment. For two centuries, large grids '
                 'stalled combinatorial searches and early linear programs. In 1942 Leonid '
                 'Kantorovich relaxed rigid maps into joint couplings that minimize expected '
                 'transport cost, and in 1991 Yann Brenier linked quadratic maps to convex '
                 'potentials. In 2000 Jean-David Benamou and Yann Brenier recast quadratic optimal '
                 'transport as the smooth flow of a pressureless fluid carrying mass with least '
                 'kinetic energy. That fluid picture turned an old earthwork problem into a clear '
                 'geometry of moving densities.',
 'act1_plain_bridge': 'Have you ever watched a video editor fade one portrait out while fading '
                      'another portrait in at the same time? Halfway through, two ghostly faces '
                      'overlap on screen like a double exposure. Plain averaging blends pixel '
                      'values in place without moving any visual feature across the frame. Optimal '
                      'transport instead treats brightness or probability weight like fine sand '
                      'and slides each grain along a straight path. A single shape travels intact '
                      'instead of splitting apart. Adding a small smoothing penalty lets modern '
                      'computers approximate that transport plan rapidly through alternating row '
                      'and column matrix scalings. Similar tools may help in freight routing, '
                      'computer graphics, generative flow models, and time-course studies of '
                      'changing cell populations. Under the stated assumptions on this page, every '
                      'numerical readout is a fixed illustrative figure rather than a live '
                      'calculation.',
 'act1_body': "Monge's one-to-one map might fail to exist when a discrete source atom splits "
              'across two targets, which led Leonid Kantorovich in 1942 to relax transport into a '
              'linear program over joint couplings (Peyré & Cuturi 2019, DOI 10.1561/2200000073). '
              'In 1991 Yann Brenier gave a polar factorization for nondegenerate vector fields on '
              'probability spaces, linking quadratic transport to convex gradients and the '
              'Monge–Ampère equation (DOI 10.1002/cpa.3160440402). Robert J. McCann (1997, DOI '
              '10.1006/aima.1997.1634) introduced displacement interpolation on Euclidean '
              'probability measures, showing displacement convexity for interacting gas energies. '
              'In 2000 Jean-David Benamou and Yann Brenier reset quadratic mass transfer in fluid '
              'mechanics and solved it numerically by an augmented Lagrangian method (DOI '
              '10.1007/s002110050002).',
 'act1_stakes': 'Linear-programming solvers grow costly once discrete histograms pass a few '
                'hundred bins. Marco Cuturi (2013, arXiv:1306.0895) smoothed classical transport '
                'with an entropic penalty solved by Sinkhorn–Knopp matrix scaling orders of '
                'magnitude faster than general solvers, with an entropic bias caveat. Lipman et '
                'al. (2023, arXiv:2210.02747) introduced simulation-free Flow Matching for '
                'continuous normalizing flows, reporting faster training and sampling along '
                'optimal-transport displacement paths than diffusion paths on ImageNet. '
                'Separately, Schiebinger et al. (2019, DOI 10.1016/j.cell.2019.01.006) used '
                'optimal transport on 315,000 single-cell profiles across 18 days to estimate '
                'reprogramming trajectories; how far such models help in other tissues is untested '
                'and not verified here.',
 'pullquote': '"Benamou and Brenier recast quadratic Wasserstein-2 mass transfer as a pressureless '
              'fluid flow whose particles move along straight characteristics guided by a '
              'Hamilton–Jacobi potential."',
 'chronology': [('1781',
                 'Gaspard Monge formulates the cut-and-fill earthwork transport problem (déblais '
                 'et remblais).'),
                ('1942–1991',
                 'Kantorovich relaxes transport to linear programming over couplings; Brenier '
                 'characterizes quadratic maps via convex gradients (DOI 10.1002/cpa.3160440402).'),
                ('1997–2001',
                 'McCann introduces displacement interpolation (DOI 10.1006/aima.1997.1634); '
                 'Benamou & Brenier publish the fluid formulation (DOI 10.1007/s002110050002); '
                 'Otto develops formal Riemannian gradient-flow calculus (DOI '
                 '10.1081/PDE-100002243).'),
                ('2013–2023',
                 'Cuturi introduces entropic Sinkhorn distances (arXiv:1306.0895; DOI '
                 '10.1561/2200000073); Lipman et al. pair displacement paths with Flow Matching '
                 '(arXiv:2210.02747).')],
 'act2_title': 'Act II — How It Works: Benamou–Brenier Continuity, Bures–Wasserstein Geodesics & '
               'Sinkhorn Scaling',
 'act2_intuition': 'Felix Otto (2001, DOI 10.1081/PDE-100002243) introduced a formal Riemannian '
                   'calculus on probability densities where tangent vectors take the potential '
                   'form v = ∇ψ. For positive definite matrices Σ_0 and Σ_1, Bhatia, Jain, and Lim '
                   '(2019, DOI 10.1016/j.exmath.2018.01.002) study the Bures–Wasserstein metric '
                   'd_BW(Σ_0, Σ_1) = [Tr Σ_0 + Tr Σ_1 − 2 Tr(Σ_0^(1/2) Σ_1 '
                   'Σ_0^(1/2))^(1/2)]^(1/2); for Gaussians N(m_0, Σ_0) and N(m_1, Σ_1), W_2² = '
                   '||m_0 − m_1||² + d_BW(Σ_0, Σ_1)². In 1D, McCann’s displacement interpolation '
                   '(1997, DOI 10.1006/aima.1997.1634) keeps ρ_t Gaussian with m_t = (1 − t)m_0 + '
                   't m_1 and σ_t = (1 − t)σ_0 + t σ_1 rather than a bimodal mixture. Under the '
                   'stated assumptions for N(−1.05, 0.83²) and N(1.05, 1.47²), W_2² = (2.10)² + '
                   '(0.64)² = 4.8196, approximately 4.82, with midpoint m_0.5 = 0.00 and σ_0.5 = '
                   '1.15.',
 'act2_deepening': 'In Benamou and Brenier’s formulation (2000, DOI 10.1007/s002110050002), '
                   'W_2²(μ_0, μ_1) = inf ∫_0^1 ∫ ρ|v|² dx dt under continuity ∂_t ρ + ∇·(ρv) = 0. '
                   'Writing kinetic action ½ W_2² = inf ∫_0^1 ∫ ½ ρ|v|² dx dt dual to ½|x − y|², '
                   'optimality gives v = ∇ψ and ∂_t ψ + ½|∇ψ|² = 0. Interior rays ẋ = ∇ψ move at '
                   'constant velocity ∇ψ_0(x), so T(x) = x + ∇ψ_0(x) = ∇(½|x|² + ψ_0(x)) = ∇Φ(x) '
                   'when μ_0 vanishes on Lebesgue-null sets (Brenier 1991, DOI '
                   '10.1002/cpa.3160440402); for smooth positive densities with g ∘ ∇Φ > 0, '
                   'det(D²Φ) = f / (g ∘ ∇Φ). Cuturi’s penalty ε KL(π || μ_0⊗μ_1) (arXiv:1306.0895) '
                   'yields π_ij = u_i K_ij v_j with K_ij = exp(−||x_i − y_j||² / ε), suggesting '
                   'faster matrix scaling at the cost of O(ε) smoothing.',
 'act2_analogy': 'Everyday analogy: Raking fallen leaves across a yard into a compost bin near the '
                 'fence shows the difference between scattered motion and coordinated transport. A '
                 'leaf blower scatters dry leaves into swirling clouds. When a line of rakes '
                 'advances together, each leaf travels along a straight lane to the bin with '
                 'minimal wasted effort. Where the analogy stops: yard leaves are discrete rigid '
                 'solids pushed by hand, whereas Benamou–Brenier transport evolves a continuous '
                 'density under zero pressure and Sinkhorn regularization blurs mass across '
                 'neighboring targets.',
 'act2_plain_primer': 'Two sliders sit below. McCann Geodesic Transport Time sweeps transport time '
                      'from 0.00 to 1.00. Sinkhorn Entropic Regularization sweeps the smoothing '
                      'parameter from 0.01 to 0.50. Dragging either slider updates its unit label '
                      'and the simulated stage vector overlay, while the four readout cards keep '
                      'fixed illustrative values (approximately 4.82 for squared distance, '
                      'midpoint 0.00 and 1.15 halfway along the path, and 18 steps at smoothing '
                      '0.05).',
 'distill_diagram': {'analogy_title': 'The Synchronized Leaf Rake',
                     'analogy_sub': 'Coordinated lanes carry mass cleanly; discrete leaves stop '
                                    'short of fluid blur',
                     'force_a_title': 'McCann Geodesic Time t_geo',
                     'force_a_sub': 'Indexes displacement path ρ_t along straight Hamilton–Jacobi '
                                    'characteristics',
                     'force_b_title': 'Sinkhorn Entropic Blur eps_reg',
                     'force_b_sub': 'Smooths couplings π_ij = u_i K_ij v_j for matrix scaling with '
                                    'O(ε) bias',
                     'threshold_title': 'Displacement Geodesic vs. Ghosting',
                     'threshold_pass': '1D Gaussian displacement path keeps a single unimodal '
                                       'density bump',
                     'threshold_fail': 'Linear Euclidean mixture ½μ_0 + ½μ_1 splits into bimodal '
                                       'double exposures'},
 'walkthrough': ['Experiment 1 (Transport Time Slider): Sweep t_geo across 0.00–1.00 to update the '
                 't label and simulated overlay; W_2² = 4.82 and midpoint (0.00, 1.15) stay fixed.',
                 'Experiment 2 (Entropic Regularization Slider): Vary eps_reg across 0.01–0.50 to '
                 'update the ε label; the 18-step figure at ε = 0.05 stays fixed text.',
                 'Experiment 3 (Four-Stage Stepper): Step through Stages 1–4 for Kantorovich '
                 'couplings, Brenier maps, Benamou–Brenier geodesics, and Sinkhorn scaling.'],
 'act4_title': 'Act IV — Flow Matching, Snapshot Biology & Open High-Dimensional Questions',
 'act4_human_ai': 'Lipman et al. (2023, arXiv:2210.02747) connect displacement interpolation to '
                  'simulation-free Flow Matching for continuous normalizing flows. In civil '
                  'engineering, Monge’s 1781 cut-and-fill problem motivated computational '
                  'transport (Peyré & Cuturi 2019, DOI 10.1561/2200000073), though real grading '
                  'also involves soil swell and haul-grade caveats that could shift costs and are '
                  'not modeled here.',
 'act4_deepening': 'Because single-cell RNA sequencing destroys cells at each timepoint, '
                   'Schiebinger et al. (2019, DOI 10.1016/j.cell.2019.01.006) used Waddington-OT '
                   'to couple reprogramming snapshots across 18 days. Open questions remain: '
                   'unregularized Wasserstein estimation faces steep high-dimensional sample '
                   'bounds, and extending dynamic transport to curved groups such as SE(3) might '
                   'require new regularizers not yet settled in practice.',
 'cf_bridge': 'Standalone Mathematical Monograph (M.04 + M.07 + M.08 -> M.09): Montoro et al. '
              '(2018, DOI 10.1038/s41586-018-0393-7) and Plasschaert et al. (2018, DOI '
              '10.1038/s41586-018-0394-6) identified rare FOXI1-positive airway ionocytes '
              'replenished by basal progenitors as a major source of CFTR transcripts. In '
              'principle, Waddington-OT trajectory estimation could be explored on airway '
              'time-course data, but that idea is untested and not verified here, and nothing on '
              'this page is clinical advice.',
 'sources': ['Brenier, Y. (1991). Polar factorization and monotone rearrangement of vector-valued '
             'functions. Comm. Pure Appl. Math., 44(4), 375–417. DOI: 10.1002/cpa.3160440402.',
             'McCann, R. J. (1997). A convexity principle for interacting gases. Advances in '
             'Mathematics, 128(1), 153–179. DOI: 10.1006/aima.1997.1634.',
             'Benamou, J.-D., & Brenier, Y. (2000). A computational fluid mechanics solution to '
             'the Monge-Kantorovich mass transfer problem. Numerische Mathematik, 84(3), 375–393. '
             'DOI: 10.1007/s002110050002.',
             'Otto, F. (2001). The geometry of dissipative evolution equations: The porous medium '
             'equation. Comm. Partial Differential Equations, 26(1–2), 101–174. DOI: '
             '10.1081/PDE-100002243.',
             'Cuturi, M. (2013). Sinkhorn distances: Lightspeed computation of optimal transport. '
             'NeurIPS, 26, 2292–2300. arXiv:1306.0895.',
             'Bhatia, R., Jain, T., & Lim, Y. (2019). On the Bures–Wasserstein distance between '
             'positive definite matrices. Expositiones Mathematicae, 37(2), 165–191. DOI: '
             '10.1016/j.exmath.2018.01.002.',
             'Peyré, G., & Cuturi, M. (2019). Computational optimal transport: With applications '
             'to data sciences. Found. Trends Mach. Learn., 11(5–6), 355–607. DOI: '
             '10.1561/2200000073.',
             'Lipman, Y., et al. (2023). Flow matching for generative modeling. ICLR 2023. '
             'arXiv:2210.02747.',
             'Schiebinger, G., et al. (2019). Optimal-transport analysis of single-cell gene '
             'expression identifies developmental trajectories in reprogramming. Cell, 176(4), '
             '928–943.e22. DOI: 10.1016/j.cell.2019.01.006.',
             'Montoro, D. T., et al. (2018). A revised airway epithelial hierarchy includes '
             'CFTR-expressing ionocytes. Nature, 560(7718), 319–324. DOI: '
             '10.1038/s41586-018-0393-7.',
             'Plasschaert, L. W., et al. (2018). A single-cell atlas of the airway epithelium '
             'reveals the CFTR-rich pulmonary ionocyte. Nature, 560(7718), 377–381. DOI: '
             '10.1038/s41586-018-0394-6.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning. Quant. Sci. '
             'Stud., 2(3), 882–898. DOI: 10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Benamou-Brenier '
        'Wasserstein-2 optimal transport geodesic wave packet interpolation and Sinkhorn entropic '
        'coupling diagram">\n'
        '            <line x1="40" y1="185" x2="640" y2="185" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <path d="M 55 185 Q 95 65 135 185" fill="var(--tp-prussian)" '
        'fill-opacity="0.18" stroke="var(--tp-prussian)" stroke-width="2" '
        'stroke-dasharray="4,3"/>\n'
        '            <path d="M 255 185 Q 295 55 335 185" fill="var(--tp-verdigris)" '
        'fill-opacity="0.18" stroke="var(--tp-verdigris)" stroke-width="2" '
        'stroke-dasharray="4,3"/>\n'
        '            <path id="tp-m09-geodesic-packet" d="M 155 185 Q 195 60 235 185" '
        'fill="var(--tp-minium)" fill-opacity="0.32" stroke="var(--tp-minium)" '
        'stroke-width="2.8"/>\n'
        '            <line x1="95" y1="95" x2="295" y2="90" stroke="var(--tp-minium)" '
        'stroke-width="1.6" stroke-dasharray="5,3"/>\n'
        '            <text x="52" y="26" font-size="10.5" font-weight="600" '
        'fill="currentColor">Benamou–Brenier W₂ Geodesic ρ(t, x) (∂_t ρ + ∇·(ρ ∇ψ) = 0)</text>\n'
        '            <text id="tp-m09-svg-w2-text" x="52" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Fixed Illustrative Pair: W₂² = 4.82 · Midpoint t = 0.50 (σ = '
        '1.15)</text>\n'
        '            <line x1="365" y1="24" x2="365" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="382" y="26" font-size="10" font-weight="600" '
        'fill="currentColor">Brenier Convex Map T(x) = x + ∇ψ₀(x) = ∇Φ(x)</text>\n'
        '            <path id="tp-m09-map-curve" d="M 390 172 Q 505 118 625 52" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="2.8"/>\n'
        '            <circle id="tp-m09-op-dot" cx="505" cy="114" r="6" fill="var(--tp-minium)"/>\n'
        '            <text x="390" y="68" font-size="9.5" fill="var(--tp-prussian)">HJB '
        'Optimality: ∂_t ψ + ½|∇ψ|² = 0</text>\n'
        '            <text id="tp-m09-sinkhorn-text" x="390" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Fixed Illustrative Sinkhorn: ε = 0.05 · 18 Steps</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a Benamou-Brenier Wasserstein-2 transport bridge '
        'morphing one probability density into another along straight streamlines would look like '
        '(artistic impression, not a formal plot)',
 'caption': 'Conceptual Vision Plate M.09-V (Imagining What It Would Look Like) · Artistic '
            'visualization imagining Jean-David Benamou and Yann Brenier’s Wasserstein-2 fluid '
            'geodesic carrying mass along straight streamlines.'}

DISPATCH = {'kicker': 'OPTIMAL TRANSPORT DISPATCH · BRENIER MAPS, FLUID GEODESICS & SINKHORN SCALING',
 'headline': 'Benamou–Brenier Dynamic Optimal Transport, McCann Geodesics & Entropic Scaling',
 'body': 'Links Brenier’s polar factorization (DOI 10.1002/cpa.3160440402) and McCann’s '
         'displacement interpolation (DOI 10.1006/aima.1997.1634) with Benamou & Brenier’s fluid '
         'formulation (DOI 10.1007/s002110050002), Otto’s calculus (DOI 10.1081/PDE-100002243), '
         'and Sinkhorn scaling (arXiv:1306.0895; DOI 10.1561/2200000073). Values shown are '
         'illustrative.'}

META_3D = ('Benamou–Brenier Wasserstein-2 Geodesic Transport Bridge',
 'X: Spatial Domain x · Z: Geodesic Time t ∈ [0,1] · Y: Optimal Transport Density ρ(t, x)')

ES_TRANSLATION = {'title_es': 'Transporte Óptimo de Monge–Kantorovich, Dinámica de Fluidos Geodésica Wasserstein-2 '
             'de Benamou–Brenier, Regularización Entrópica de Sinkhorn y Flow Matching',
 'subtitle_es': 'Sintetizando los Folios M.04, M.07 y M.08: cómo Jean-David Benamou y Yann Brenier '
                'replantearon el transporte óptimo Wasserstein-2 como un flujo sin presión de '
                'mínima energía cinética. Las lecturas numéricas son valores ilustrativos fijos.',
 'why_es': 'Fundir dos retratos en el mismo sitio produce una doble exposición borrosa; el '
           'transporte óptimo desliza cada porción de masa por carriles rectos como una fila '
           'coordinada de rastrillos.',
 'plain_es': 'En 1781 en París, Gaspard Monge estudió cortes y rellenos para mover tierra hacia '
             'zanjas con el menor esfuerzo total. ¿Han notado que al fundir dos retratos en un '
             'editor de video aparecen dos rostros superpuestos a mitad de la transición? '
             'Promediar píxeles en su sitio mezcla brillos sin desplazar formas. El transporte '
             'óptimo trata el peso de cada imagen como arena fina y desliza cada grano en línea '
             'recta. Así una figura viaja entera sin partirse en dos fantasmas. Una penalización '
             'suave permite aproximar ese plan en computadora escalando filas y columnas de una '
             'matriz. Estas ideas se estudian en logística, gráficas, modelos generativos y '
             'biología celular. En esta página las lecturas numéricas son valores ilustrativos '
             'fijos.',
 'deep_es': 'Kantorovich relajó el problema de Monge a un programa lineal de costo cuadrático '
            'sobre acoplamientos como una malla de pesos entre nodos (DOI 10.1561/2200000073), y '
            'Brenier (1991, DOI 10.1002/cpa.3160440402) caracterizó el mapa óptimo mediante '
            'gradientes convexos cuando la medida inicial se anula en conjuntos nulos de Lebesgue. '
            'En mecánica de fluidos, Benamou y Brenier (2000, DOI 10.1007/s002110050002) '
            'minimizaron la energía cinética de un flujo de fluido sin presión cuya masa sigue la '
            'ecuación de continuidad y la condición de Hamilton–Jacobi sobre trayectorias de '
            'McCann (DOI 10.1006/aima.1997.1634; Otto 2001, DOI 10.1081/PDE-100002243). Bajo la '
            'métrica de Bures–Wasserstein en covarianzas (Bhatia et al. 2019, DOI '
            '10.1016/j.exmath.2018.01.002), en las gaussianas ilustrativas de este folio N(−1.05, '
            '0.83²) y N(1.05, 1.47²) resulta W_2² ≈ 4.82 y punto medio con desviación 1.15 sin '
            'mezclas bimodales; Sinkhorn (arXiv:1306.0895) introduce sesgo O(ε), mientras los '
            'controles solo actualizan etiquetas y las cuatro tarjetas quedan fijas.',
 'bridge_es': 'Pregunta hipotética, no un resultado: Montoro et al. (2018, DOI '
              '10.1038/s41586-018-0393-7) y Plasschaert et al. (2018, DOI '
              '10.1038/s41586-018-0394-6) describieron ionocitos ricos en CFTR, y métodos como '
              'Waddington-OT (DOI 10.1016/j.cell.2019.01.006) podrían explorarse en series '
              'temporales aéreas. Este folio no analizó datos biológicos ni ofrece orientación '
              'clínica.'}
