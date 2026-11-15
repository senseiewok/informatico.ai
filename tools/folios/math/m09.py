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
 'subtitle': 'Synthesizing Folios M.04, M.07, and M.08: how Jean-David Benamou & Yann Brenier '
             'recast quadratic Wasserstein-2 optimal transport as a fluid-mechanics problem of '
             'least kinetic energy, with a pressureless flow guided by a Hamilton–Jacobi '
             'potential. The numbers shown are illustrative model values.',
 'date_published': '2026-11-03',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'OPTIMAL TRANSPORT · REV 1.1',
 'primary_kernel': 'tools/discovery/frontier_ai_math_catalog.py',
 'governing_law': 'W_2²(μ_0, μ_1) = inf ∫_0^1 ∫ ρ|v|² dx dt · ∂_t ρ + ∇·(ρ∇ψ) = 0 · ∂_t ψ + ½|∇ψ|² '
                  '= 0',
 'colophon': {'identifier': 'M.09 · Benamou–Brenier Wasserstein-2 Optimal Transport',
              'kernels': 'Benamou–Brenier Fluid Geodesic · Brenier Convex Potential ∇Φ · Sinkhorn '
                         'KL',
              'benchmarks': 'Illustrative model values: W_2²(μ_0, μ_1) = 4.82 · t = 0.50 · ε = 0.05 '
                            '(18 Sinkhorn steps)',
              'bridge': 'Synthesizes M.04/M.07/M.08 · Waddington-OT trajectory inference '
                        '(Schiebinger et al. 2019) as a method reference'},
 'sliders': [{'label': 'McCann Geodesic Transport Time (t)',
              'min': 0.0,
              'max': 1.0,
              'step': 0.05,
              'value': 0.5,
              'unit': 't = '},
             {'label': 'Sinkhorn Entropic Regularization (ε)',
              'min': 0.01,
              'max': 0.5,
              'step': 0.01,
              'value': 0.05,
              'unit': 'ε = '}],
 'steps': ["Stage 1 (Monge–Kantorovich Convex Duality): Relaxes Monge's transport map T_# μ_0 = "
           "μ_1 into Kantorovich's linear program over couplings π ∈ Π(μ_0, μ_1).",
           'Stage 2 (Brenier Polar Factorization Theorem): Proves the unique L²-optimal transport '
           'map is the gradient of a convex potential T(x) = ∇Φ(x) = x + ∇ψ_0(x).',
           'Stage 3 (Benamou–Brenier Dynamic Fluid Geodesic, DOI 10.1007/s002110050002): Evolves '
           'density ρ_t along constant-velocity geodesics ∂_t ρ + ∇·(ρ∇ψ) = 0 with HJB optimality '
           '∂_t ψ + ½|∇ψ|² = 0.',
           'Stage 4 (Cuturi Sinkhorn Scaling, Continuing M.04/M.07): The entropic penalty ε KL(π '
           '|| μ_0⊗μ_1) turns the problem into alternating matrix scalings. The 18-step count '
           'shown is an illustrative value; the real count depends on ε and the stopping '
           'tolerance.'],
 'readouts': [{'label': 'Squared Wasserstein Distance (W_2², model)',
               'value': '4.82 (illustrative Gaussian pair)'},
              {'label': 'Geodesic Mean & Std. Dev. (t=0.5, model)',
               'value': 'μ_t = 0.00 · σ_t = 1.15 (illustrative)'},
              {'label': 'Sinkhorn Scaling Convergence (model)',
               'value': '18 iterations at ε = 0.05 (illustrative)'},
              {'label': 'Model Geometry', 'value': 'Benamou–Brenier geodesic (teaching model)'}],
 'spec_plate': {'division': 'COMPUTATIONAL MATHEMATICS & GENERATIVE AI / OT-FLOW',
                'title': 'Benamou–Brenier Dynamic Optimal Transport & Sinkhorn Flow-Matching '
                         'Solver',
                'body': 'Design study: a Bures–Wasserstein geodesic integrator and a log-domain '
                        'stabilized Sinkhorn–Knopp matrix scaling routine, of the kind used for '
                        'trajectory inference and mass-haul planning. Nothing here was run on '
                        'real data.',
                'meta': 'Sources cited, not reproduced: Benamou & Brenier (2000) DOI '
                        '10.1007/s002110050002 · Cuturi (2013)'},
 'sidenote_1': {'kicker': 'SIDENOTE M.09-A · UNITING M.04 ENTROPY, M.07 HJB & M.08 RIEMANNIAN '
                          'METRICS',
                'body': "In Felix Otto's formal Riemannian calculus on probability space P_2(R^d), "
                        'Benamou–Brenier paths are geodesics. As ε -> 0, entropic transport plans '
                        'approach the unregularized optimal plan, whose Brenier map solves the '
                        'Monge–Ampère equation det(D²Φ) = f / (g ∘ ∇Φ).'},
 'sidenote_2': {'kicker': 'SIDENOTE M.09-B · WADDINGTON-OT AND A POSSIBLE AIRWAY QUESTION',
                'body': 'Because scRNA-seq destroys cells at each measurement timepoint t_k, '
                        'Schiebinger et al. (2019, DOI 10.1016/j.cell.2019.01.006) used optimal '
                        'transport to infer developmental trajectories during reprogramming. The '
                        'same method could in principle be asked how airway basal cells give rise '
                        'to ionocytes, a CFTR-rich cell type described in 2018 (Montoro et al., '
                        'DOI 10.1038/s41586-018-0393-7; Plasschaert et al., DOI '
                        '10.1038/s41586-018-0394-6). This folio has not done that analysis.'},
 'skill': {'filename': 'wasserstein-optimal-transport-benamou-brenier-SKILL.md',
           'name': 'wasserstein-optimal-transport-benamou-brenier',
           'description': 'AI-agnostic mathematical and generative-AI skill for Monge-Kantorovich '
                          'optimal transport, Benamou-Brenier Wasserstein-2 dynamic fluid '
                          'geodesics, Bures-Wasserstein Gaussian closed forms, and Sinkhorn '
                          'entropic scaling.',
           'rules': ['Compute dynamic Wasserstein-2 distance via Benamou-Brenier action '
                     'minimization W_2^2(mu_0, mu_1) = inf int_0^1 int rho(t,x) |v(t,x)|^2 dx dt '
                     'subject to d_t rho + nabla.(rho v) = 0.',
                     'Interpolate Gaussian measures N(m_0, Sigma_0) and N(m_1, Sigma_1) along '
                     "McCann's geodesic m_t = (1-t)m_0 + t m_1 rather than Euclidean mixture "
                     'averaging.',
                     'Stabilize Sinkhorn-Knopp scaling in the log domain for small entropic '
                     'regularization epsilon to prevent numerical underflow in exp(-C_ij / '
                     'epsilon).']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. W_2² = 4.82, σ_t = '
                           '1.15 and the 18 Sinkhorn steps are now labelled as illustrative '
                           "values (the Gaussian parameters behind them are not stated), and the "
                           "'QED PASS' verdict is withdrawn. The claims that optimal transport "
                           'has reconstructed basal-to-ionocyte trajectories and that flow '
                           'matching designs lipid nanoparticles are withdrawn; the bridge now '
                           'describes a possible analysis, sourced to Schiebinger et al. 2019 and '
                           'the 2018 ionocyte papers. The invented 1781 scene is trimmed.',
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
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1007/s002110050002',
           'fetched_on': '2026-11-08',
           'citing_publications': 2109,
           'supporting': 19,
           'mentioning': 2106,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 2,109 '
                      'citing publications (19 supporting, 2,106 mentioning, 0 contrasting) on '
                      "Jean-David Benamou & Yann Brenier's computational fluid mechanics "
                      'formulation of the Monge-Kantorovich L2 Wasserstein optimal transport '
                      'problem.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['M.04', 'M.07', 'M.08'],
 'lineage_mode': 'TRIAD_SYNTHESIS · Synthesizes M.04 PFR Entropic Distance, M.07 Pontryagin '
                 'Control & M.08 Riemannian Geodesics',
 'scite': {'doi': '10.1007/s002110050002',
           'fetched_on': '2026-11-08',
           'citing_publications': 2109,
           'supporting': 19,
           'mentioning': 2106,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 2,109 '
                      'citing publications (19 supporting, 2,106 mentioning, 0 contrasting) on '
                      "Jean-David Benamou & Yann Brenier's computational fluid mechanics "
                      'formulation of the Monge-Kantorovich L2 Wasserstein optimal transport '
                      'problem.'},
 'act1_title': 'Act I — Uniting M.04 Entropy, M.07 Optimal Control & M.08 Riemannian Geodesics: '
               "From Gaspard Monge's Earthworks to Wasserstein-2 Fluid Dynamics",
 'act1_dropcap': 'In 1781 the French mathematician Gaspard Monge published a memoir with the '
                 'Royal Academy of Sciences in Paris on cuts and fills (déblais et remblais), the '
                 'moving of earth. It asked a humble yet mathematically stubborn question: '
                 'given a sprawling mound of excavated dirt and a distant trench that must be '
                 'filled, how should workers shovel and haul every clod of earth so that the total '
                 'labor expended is the smallest possible? Shovels could not cross paths '
                 'chaotically without wasting time, and throwing earth into random piles created '
                 "expensive bottlenecks. Monge's problem stayed hard for a long time. In 2000 the "
                 'French applied mathematicians Jean-David Benamou and Yann Brenier showed that, '
                 'for quadratic cost, moving mass with least effort can be computed as the '
                 'smooth flow of a pressureless fluid that minimizes kinetic energy.',
 'act1_plain_bridge': 'Imagine you are creating a digital animation that morphs one photograph '
                      'into another, like transforming a photo of a kitten into a photo of a lion. '
                      'A naive video editor simply fades out the kitten while fading in the lion '
                      'at the same time. During the middle of that transition, you see an awkward, '
                      'ghostly double image where two transparent faces awkwardly overlap. That '
                      'unnatural ghosting happens because standard averaging merely blends pixel '
                      'colors without moving shapes. Optimal transport solves this problem by '
                      "treating every bit of the kitten's image like a tiny grain of sand on a "
                      'beach. Instead of fading, the algorithm picks up each grain and slides it '
                      'along the smoothest, shortest path until it settles into its new home in '
                      "the lion's mane. The same mathematics is used in logistics, in some "
                      'machine-learning image generators, and in research that infers how cells '
                      'change over time from snapshots.',
 'act1_body': 'In 1942, Soviet mathematician Leonid Kantorovich made the critical breakthrough of '
              "relaxing Monge's rigid point-to-point mapping into a convex linear program over "
              'joint probability couplings, earning the 1975 Nobel Prize in Economics. Then in '
              '2000, Jean-David Benamou and Yann Brenier published their seminal discovery in '
              'Numerische Mathematik (DOI 10.1007/s002110050002), showing that quadratic '
              'Wasserstein-2 optimal transport can be reformulated as a dynamic continuum fluid '
              'problem. Instead of solving a static combinatorial matching grid, one tracks the '
              'density and velocity fields of a pressureless fluid evolving along '
              'action-minimizing geodesics governed by Hamilton–Jacobi potential theory. By '
              'framing probability transport as kinetic energy minimization, their partial '
              'differential equations bridged the historical divide between pure variational '
              'analysis and large-scale industrial computation. When Marco Cuturi subsequently '
              'introduced Sinkhorn entropic regularization, the intractable optimal transport '
              'bottleneck transformed into rapid matrix-vector scalings perfectly suited for '
              'parallel graphics processing hardware. Optimal transport ideas now appear in '
              'generative modelling, and Schiebinger et al. (2019, Cell, DOI '
              '10.1016/j.cell.2019.01.006) used optimal transport to infer developmental '
              'trajectories from single-cell snapshots of cellular reprogramming.',
 'act1_stakes': "The journey from Monge's military trenches to modern generative artificial "
                'intelligence represents one of the greatest unifications in applied mathematics. '
                'For centuries, engineers treating optimal transport struggled against an '
                'exponential computational wall: comparing two probability distributions with '
                'thousands of discrete data points required solving massive linear programs that '
                'ground early computers to a halt. As a result, machine learning relied on crude '
                'divergence metrics that failed whenever distributions had non-overlapping '
                'support, causing generative models to collapse into blurry averages. By recasting '
                'optimal transport through the twin lenses of fluid mechanics and '
                'entropy-regularized convex optimization, researchers converted a fragile '
                'combinatorial puzzle into a smooth, differentiable geometry known as the '
                'Otto–Wasserstein manifold. This geometry is now studied in generative '
                'modelling, image registration and logistics; how far it helps in each '
                'application is a question for the specialist literature, not something this '
                'folio measures.',
 'pullquote': '"Benamou and Brenier showed that morphing one probability distribution into '
              'another with minimum effort can be computed as a pressureless fluid flow whose '
              'particles travel along straight lines, guided by a Hamilton–Jacobi potential."',
 'chronology': [('1781',
                 'Gaspard Monge formulates the optimal earthwork excavation and embankment '
                 'transport problem (déblais et remblais).'),
                ('1942',
                 'Leonid Kantorovich introduces dual linear programming couplings pi in Pi(mu_0, '
                 'mu_1) for optimal resource allocation.'),
                ('2000',
                 'Jean-David Benamou & Yann Brenier publish the dynamic fluid-mechanics formulation '
                 'of W_2^2 optimal transport in Numerische Mathematik (DOI '
                 '10.1007/s002110050002).'),
                ('2013',
                 'Marco Cuturi introduces Sinkhorn distances, computing entropy-regularized '
                 'optimal transport by fast matrix scaling.')],
 'act2_title': 'Act II — How It Actually Works: Benamou–Brenier Geodesic Continuity + Sinkhorn '
               'Entropic Scaling',
 'act2_intuition': 'Connecting optimal control with Riemannian geometry, Felix Otto demonstrated '
                   'that the space of probability distributions P_2(R^d) endowed with the '
                   'Wasserstein-2 metric is an infinite-dimensional Riemannian manifold. The '
                   'tangent vectors correspond to potential velocity fields v = nabla psi. For two '
                   'Gaussian measures N(m_0, Sigma_0) and N(m_1, Sigma_1), the exact '
                   'Bures–Wasserstein geodesic distance has the closed-form expression W_2^2 = '
                   '||m_0 - m_1||^2 + Tr(Sigma_0 + Sigma_1 - 2 * (Sigma_0^(1/2) Sigma_1 '
                   "Sigma_0^(1/2))^(1/2)). Along this manifold, McCann's displacement "
                   'interpolation rho_t = ((1 - t) id + t nabla Phi)_# mu_0 moves mass along '
                   'constant-velocity geodesics without creating the artificial bimodal fading '
                   "typical of Euclidean mixtures. When we introduce Marco Cuturi's entropic "
                   'penalty epsilon * KL(pi || mu_0 x mu_1), the Kantorovich problem turns into an '
                   'entropic Schrödinger bridge. The optimal coupling matrix factors into diagonal '
                   'scalings u and v around a Gibbs kernel K_{ij} = exp(-||x_i - y_j||^2 / '
                   'epsilon), found by alternating matrix-vector scalings; in this teaching '
                   'model the illustrative run stops after eighteen of them. The entropic plan '
                   'is a smoothed approximation to the optimal one.',
 'act2_deepening': 'The deeper variational mechanism uncovered by Benamou and Brenier is that '
                   'minimizing kinetic energy across a compressible density path transforms a '
                   'static spatial permutation into a time-dependent continuity equation d_t rho + '
                   'nabla . (rho v) = 0 coupled to the Hamilton–Jacobi equation d_t psi + 0.5 '
                   '|nabla psi|^2 = 0. In this fluid formulation, individual probability particles '
                   'never cross trajectories; their paths follow the gradient of a convex '
                   'potential Phi whose Hessian determinant satisfies the Monge–Ampère partial '
                   'differential equation det(D^2 Phi) = f / (g o nabla Phi). When the entropic '
                   'parameter epsilon approaches zero, the diffusive Brownian motion of the '
                   'Schrödinger bridge freezes into the deterministic Monge transport map. '
                   'Conversely, setting epsilon higher introduces controlled thermal dispersion, '
                   'converting a stiff combinatorial matching into a strongly convex optimization '
                   'problem with guaranteed linear convergence rates. This interplay between fluid '
                   'geodesics and entropic regularization explains why generative flow matching '
                   'models can train neural velocity fields to follow straight, non-colliding '
                   'paths between ambient noise and structured physical data.',
 'act2_analogy': 'Everyday analogy: Imagine raking a sprawling pile of autumn leaves from the '
                 'center of your lawn into a neat composting bin near the fence. If you try to '
                 'blow them with a leaf blower all at once, leaves scatter randomly in turbulent '
                 'swirls, creating a messy cloud. But if a team of rake handlers marches in a '
                 'synchronized wave, each leaf moves along a straight, parallel path directly to '
                 'its final spot without colliding. Optimal transport is that synchronized rake '
                 'line, moving mass with minimum effort and zero chaotic turbulence.',
 'act2_plain_primer': 'To see optimal transport in action, consider two intuitive controls on our '
                      'interactive demonstration. The first control is a master time slider that '
                      'sweeps your view from the starting pile of mass at time zero to the final '
                      'target shape at time one. As you move this slider, you watch the '
                      'distribution glide smoothly across the screen like a coherent water '
                      'droplet, preserving its shape without ever splitting into an unnatural '
                      'ghost image. The second control adjusts the entropic fuzziness or '
                      'smoothness of the transport plan, moving from an ultra-crisp, deterministic '
                      'physical path up to a slightly warm, diffusive cloud. When this '
                      'regularization setting is very small, the algorithm calculates an exact, '
                      'razor-sharp mechanical path, but requires more computational steps. As you '
                      'increase the smoothness dial, the calculations converge in a fraction of a '
                      'second while retaining the overall geometric flow, illustrating the '
                      'practical trade-off used inside real-world generative models.',
 'distill_diagram': {'analogy_title': 'The Synchronized Leaf Rake',
                     'analogy_sub': 'Moving autumn leaves along parallel paths without chaotic '
                                    'swirls',
                     'force_a_title': 'McCann Geodesic Time t',
                     'force_a_sub': 'Advances fluid density along straight Hamilton-Jacobi '
                                    'streamlines',
                     'force_b_title': 'Sinkhorn Entropic Blur ε',
                     'force_b_sub': 'Accelerates matrix scaling by smoothing transport coupling '
                                    'paths',
                     'threshold_title': 'Coherent Fluid Flow vs. Ghosting',
                     'threshold_pass': 'For Gaussians, the Wasserstein geodesic stays a single '
                                       'bump',
                     'threshold_fail': 'Linear Euclidean blending creates washed-out double '
                                       'exposures'},
 'walkthrough': ['Experiment 1 (McCann Geodesic Interpolation Time t in [0, 1]): Drag Geodesic '
                 'Transport Time t from 0.00 (source distribution mu_0) to 1.00 (target '
                 'distribution mu_1). Compare how the Wasserstein-2 geodesic preserves coherent '
                 'wave packet shape while Euclidean linear mixing splits into two ghosts.',
                 'Experiment 2 (Sinkhorn Entropic Regularization epsilon): Vary Entropic '
                 'Regularization epsilon from 0.01 (sharp Monge–Brenier deterministic map) to 0.50 '
                 '(diffusive Schrödinger bridge coupling) and watch Sinkhorn convergence '
                 'iterations drop.',
                 'Experiment 3 (From Monge Earthworks to Flow Matching AI): Step through Stages 1 '
                 'to 4 to inspect Monge–Kantorovich duality, Benamou–Brenier continuity + HJB '
                 'optimality, Bures–Wasserstein geodesics, and generative Flow Matching.'],
 'act4_title': 'Act IV — Generative Flow Matching, Civil Earthworks & Single-Cell CF Trajectory '
               'Inference',
 'act4_human_ai': "Monge's original question was about cut-and-fill earthworks; Sinkhorn solvers "
                  'could be applied to mass-haul balancing, and machine-learning researchers '
                  'train continuous normalizing flows toward straight transport-like velocity '
                  'fields. These are directions the folio describes, not projects it ran.',
 'act4_deepening': 'Optimal transport links generative modelling with experimental biology and '
                   'engineering. When biologists analyze single-cell RNA sequencing data, the '
                   'measurement destroys the cells at each timestamp, leaving only disconnected '
                   'snapshots of cellular populations. Schiebinger et al. (2019) used optimal '
                   'transport to connect such snapshots and infer trajectories during '
                   'reprogramming. In civil infrastructure, Sinkhorn solvers could be coupled '
                   'with geographic information systems to plan mass-haul during highway '
                   'grading; this folio did not test that. Open '
                   'mathematical frontiers beckon: how do we scale dynamic optimal transport to '
                   'high-dimensional non-Euclidean manifolds like SE(3) for protein docking '
                   'without incurring the curse of dimensionality? Stable entropy-regularized '
                   'estimators on curved spaces would be useful for molecular modelling and '
                   'logistics, if they can be built.',
 'cf_bridge': 'Standalone Mathematical Flagship & Triad Synthesis (M.04 + M.07 + M.08 -> M.09): '
              'Written for applied mathematicians, optimal-control theorists, and AI researchers. '
              'A possible biology question, not a result: optimal-transport trajectory inference '
              'of the Waddington-OT kind (Schiebinger et al. 2019, DOI '
              '10.1016/j.cell.2019.01.006) could be applied to airway single-cell data to study '
              'how basal cells give rise to ionocytes, the CFTR-rich cells described by Montoro '
              'et al. and Plasschaert et al. in 2018. This folio has not run such an analysis '
              'and makes no clinical claim.',
 'sources': ['Benamou, J.-D., & Brenier, Y. (2000). A computational fluid mechanics solution to '
             'the Monge-Kantorovich mass transfer problem. Numerische Mathematik, 84(3), 375–393. '
             'DOI: 10.1007/s002110050002.',
             'Villani, C. (2009). Optimal Transport: Old and New (Grundlehren der mathematischen '
             'Wissenschaften, Vol. 338). Springer.',
             'Cuturi, M. (2013). Sinkhorn distances: Lightspeed computation of optimal transport. '
             'Advances in Neural Information Processing Systems (NeurIPS), 26, 2292–2300.',
             'Schiebinger, G., et al. (2019). Optimal-transport analysis of single-cell gene '
             'expression identifies developmental trajectories in reprogramming. Cell, 176(4), '
             '928–943.e22. DOI: 10.1016/j.cell.2019.01.006.',
             'Montoro, D. T., et al. (2018). A revised airway epithelial hierarchy includes '
             'CFTR-expressing ionocytes. Nature, 560(7718), 319–324. DOI: '
             '10.1038/s41586-018-0393-7.',
             'Plasschaert, L. W., et al. (2018). A single-cell atlas of the airway epithelium '
             'reveals the CFTR-rich pulmonary ionocyte. Nature, 560(7718), 377–381. DOI: '
             '10.1038/s41586-018-0394-6.',
             'Open-source tools a reader could use (not run for this folio): POT Python Optimal '
             'Transport (https://github.com/PythonOT/POT) and the FEniCSx PDE solver '
             '(https://github.com/FEniCS/dolfinx).',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). ACM Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: 10.1145/3524456.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
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
        'fill="var(--tp-verdigris)">W₂²(μ₀, μ₁) = 4.82 (Illustrative) · Geodesic Step t = '
        '0.50</text>\n'
        '            <line x1="365" y1="24" x2="365" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="382" y="26" font-size="10" font-weight="600" '
        'fill="currentColor">Monge–Brenier Transport Map T(x) = x + ∇ψ(x)</text>\n'
        '            <path id="tp-m09-map-curve" d="M 390 172 Q 505 118 625 52" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="2.8"/>\n'
        '            <circle id="tp-m09-op-dot" cx="505" cy="114" r="6" fill="var(--tp-minium)"/>\n'
        '            <text x="390" y="68" font-size="9.5" fill="var(--tp-prussian)">HJB '
        'Optimality: ∂_t ψ + ½|∇ψ|² = 0</text>\n'
        '            <text id="tp-m09-sinkhorn-text" x="390" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Sinkhorn Regularization ε = 0.05 · 18 Iterations (Illustrative)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a Benamou-Brenier Wasserstein-2 optimal transport '
        'geodesic fluid bridge morphing a Prussian-blue probability distribution into an emerald '
        'target manifold along golden Hamilton-Jacobi streamlines would look like (artistic '
        'impression, not a formal plot)',
 'caption': 'Conceptual Vision Plate M.09-V (Imagining What It Would Look Like) · Artistic '
            'mathematical visualization (synthesizing Folios M.04, M.07 & M.08) imagining '
            "Jean-David Benamou & Yann Brenier's dynamic Wasserstein-2 geodesic transporting "
            'probability mass along non-crossing Hamilton–Jacobi fluid streamlines.'}

DISPATCH = {'kicker': 'FRONTIER OPTIMAL TRANSPORT DISPATCH · SYNTHESIZING M.04, M.07 & M.08 · WASSERSTEIN-2 '
           'GEODESICS',
 'headline': 'Benamou–Brenier Dynamic Optimal Transport: Where Fluid Mechanics Meets Probability',
 'body': "Synthesizing Folio M.04's entropic distance, Folio M.07's Pontryagin/HJB optimal "
         "control, and Folio M.08's Riemannian geodesics, Jean-David Benamou & Yann Brenier "
         '(Numer. Math. DOI 10.1007/s002110050002) reformulated Monge–Kantorovich Wasserstein-2 '
         'transport as a pressureless Hamilton–Jacobi fluid geodesic.'}

META_3D = ('Benamou–Brenier Wasserstein-2 Geodesic Transport Bridge',
 'X: Spatial Domain x · Z: Geodesic Time t ∈ [0,1] · Y: Optimal Transport Density ρ(t, x)')

ES_TRANSLATION = {'title_es': 'Transporte Óptimo de Monge–Kantorovich, Dinámica de Fluidos Geodésica Wasserstein-2 '
             'de Benamou–Brenier, Regularización Entrópica de Sinkhorn y Flow Matching',
 'subtitle_es': 'Sintetizando los Folios M.04, M.07 y M.08: cómo Jean-David Benamou y Yann Brenier '
                'replantearon el transporte óptimo Wasserstein-2 como un problema de mecánica de '
                'fluidos de mínima energía cinética, con un flujo sin presión guiado por un '
                'potencial de Hamilton–Jacobi. Las cifras son valores ilustrativos del modelo.',
 'why_es': 'Mezclar dos fotografías disolviendo una en otra crea una imagen fantasma intermedia; '
           'el Transporte Óptimo desliza cada grano de arena desde su origen hasta su destino por '
           'la trayectoria geodésica más corta sin cruzarse.',
 'plain_es': 'En 1781 en París, el matemático e ingeniero civil Gaspard Monge planteó un dilema '
             'práctico para la construcción: cómo mover montículos de tierra hacia fosas de '
             'relleno realizando el menor esfuerzo físico posible. Durante más de dos siglos, este '
             'problema de acarreo de materiales parecía casi imposible de resolver en computadoras '
             'comunes debido a la enorme cantidad de combinaciones. Imaginen que ustedes quieren '
             'transformar una fotografía en otra dentro de un editor de video. Si simplemente '
             'desvanecen una imagen mientras aparece la otra, se produce un efecto fantasma '
             'desagradable donde ambas figuras se enciman. El transporte óptimo resuelve esto '
             'tratando cada parte de la imagen como si fuera un grano de arena que se desliza por '
             'el camino más corto y limpio hasta su destino final. Las mismas matemáticas se usan '
             'en logística, en algunos generadores de imágenes y en investigaciones que infieren '
             'cómo cambian las células a partir de instantáneas.',
 'deep_es': 'La solución moderna de Benamou y Brenier demostró que el transporte óptimo cuadrático '
            'de Wasserstein equivale a un flujo de fluido ideal sin presión que viaja a lo largo '
            'de geodésicas en el espacio de densidades. Este sistema acopla dos parámetros '
            'interactivos: el tiempo de transporte geodésico y el coeficiente de regularización '
            'entrópica de Sinkhorn. Al desplazar el tiempo entre cero y uno, la masa se traslada '
            'coherentemente conservando su estructura sin dividirse en imágenes fantasma '
            'biumbrales. Por otro lado, el parámetro entrópico suaviza el acoplamiento '
            'probabilístico mediante una penalización de Kullback–Leibler, lo que transforma un '
            'problema combinatorio pesado en multiplicaciones de matrices ultrarrápidas sobre '
            'tarjetas gráficas modernas. Cuando este valor tiende a cero, se recupera el mapa '
            'determinista exacto de Monge; al incrementarlo, el algoritmo converge en menos '
            'iteraciones (las dieciocho que se muestran son un valor ilustrativo). Este balance '
            'entre geodésicas continuas y regularización entrópica aparece en modelos generativos '
            'y en la inferencia de trayectorias celulares en biología experimental.',
 'bridge_es': 'Una posible pregunta biológica, no un resultado: la inferencia de trayectorias '
              'con transporte óptimo del tipo Waddington-OT (Schiebinger et al. 2019) podría '
              'aplicarse a datos de una sola célula de la vía aérea para estudiar cómo las '
              'células basales dan origen a los ionocitos, ricos en CFTR, descritos en 2018. Este '
              'folio no hizo ese análisis y no hace ninguna afirmación clínica.'}
