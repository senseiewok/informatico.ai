#!/usr/bin/env python3
"""Folio M.10 (MATH): Persistent Homology, Vietoris–Rips Simplicial Filtrations, Betti Barcodes & Topological Percolation Thresholds in Disordered Media."""
from __future__ import annotations

SLUG = 'm10'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.10',
 'slug': 'm10',
 'pillar': 'math',
 'category_code': 'M',
 'parent_folios': ['E.01', 'P.03', 'M.05'],
 'lineage_mode': 'TRIAD_SYNTHESIS · Completes the Circle to E.01 Percolation, P.03 Mucin Meshes & '
                 'M.05 Simplicial Geometry',
 'title': 'Persistent Homology, Vietoris–Rips Simplicial Filtrations, Betti Barcodes & Topological '
          'Percolation Thresholds in Disordered Media',
 'subtitle': "Closing the 40-Folio circle back to Folio E.01's porous percolation and P.03's mucin "
             "hydrogels: how Edelsbrunner, Letscher & Zomorodian's persistent homology tracks "
             'pores and tunnels across scales. The barcodes shown come from a synthetic teaching '
             'model, not from real samples.',
 'date_published': '2026-11-03',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'PERSISTENT HOMOLOGY · REV 1.1',
 'primary_kernel': 'tools/discovery/frontier_ai_math_catalog.py',
 'governing_law': '∂_{k−1} ∘ ∂_k = 0 · β_k^{i,j} = rank(H_k(K_i) → H_k(K_j)) · d_B(D(f), D(g)) ≤ '
                  '||f − g||_∞',
 'colophon': {'identifier': 'M.10 · Persistent Homology & Topological Percolation Barcodes',
              'kernels': 'Vietoris–Rips Filtration · Z_2 Boundary Reduction ∂_k · Bottleneck '
                         'Stability',
              'benchmarks': 'Synthetic model: ε = 65 nm · β_0 = 1, β_1 = 3, χ = −2 · longest H_1 bar '
                            'ends at 116 nm (illustrative)',
              'bridge': 'Completes E.01/P.03/M.05 · a proposed pore-size analysis, not a measured '
                        'result'},
 'sliders': [{'label': 'Simplicial Filtration Scale (ε)',
              'min': 15.0,
              'max': 140.0,
              'step': 5.0,
              'value': 65.0,
              'unit': ' nm'},
             {'label': 'Point-Cloud Perturbation Noise (σ_noise)',
              'min': 0.02,
              'max': 0.35,
              'step': 0.01,
              'value': 0.08,
              'unit': 'σ = '}],
 'steps': ['Stage 1 (Vietoris–Rips Simplicial Filtration K_ε, Continuing M.05): Grows balls of '
           'radius ε around 3D pore/mucin nodes, adding edges, triangles, and tetrahedra as '
           'pairwise distances cross 2ε.',
           'Stage 2 (Chain Complex & Z_2 Boundary Reduction ∂_{k−1} ∘ ∂_k = 0, DOI '
           '10.1007/s00454-002-2885-2): Reduces boundary matrices to pair each k-cycle birth b_i '
           'with its bounding (k+1)-simplex death d_i.',
           'Stage 3 (Cohen-Steiner Bottleneck Stability): By the stability theorem of '
           'Cohen-Steiner, Edelsbrunner & Harer, a perturbation moves persistence points by at '
           'most d_B ≤ ||f − g||_∞, so short bars near the diagonal can be read as noise and long '
           'bars as structure. σ_noise = 0.08 is the model setting.',
           'Stage 4 (Pore-Throat Reading, Completing E.01 & P.03): In the synthetic model the '
           'longest H_1 interval is [38 nm, 116 nm]. Robins et al. (2016) relate persistence '
           'features of this kind to percolating length scales in micro-CT images of porous '
           'materials. Whether a given particle passes through a real mesh also depends on '
           'chemistry and binding, which topology alone does not settle.'],
 'readouts': [{'label': 'Betti Numbers (β_0, β_1, β_2, model)', 'value': 'β₀ = 1 · β₁ = 3 · β₂ = 0'},
              {'label': 'Euler–Poincaré Invariant (χ)', 'value': 'χ = β₀ − β₁ + β₂ = −2'},
              {'label': 'Longest H_1 Bar Death Scale (model)',
               'value': '116 nm (synthetic point cloud)'},
              {'label': 'Model Reading', 'value': 'Long bar stands out from noise (not a measurement)'}],
 'spec_plate': {'division': 'ALGEBRAIC TOPOLOGY & 3D POROUS TOMOGRAPHY / TDA',
                'title': 'Vietoris–Rips & Alpha-Complex Persistent Homology Pore Analyzer (Design '
                         'Study)',
                'body': 'Design study: a Z_2 sparse boundary-matrix reducer and '
                        'Wasserstein/Bottleneck persistence diagram analyzer that could be applied '
                        'to 3D micro-CT images of concrete cores (E.01/E.09) or to imaged mucin '
                        'hydrogels (P.03). No such images were analyzed here.',
                'meta': 'Method source cited, not reproduced: Edelsbrunner, Letscher & Zomorodian '
                        '(2002) DOI 10.1007/s00454-002-2885-2'},
 'sidenote_1': {'kicker': 'SIDENOTE M.10-A · CLOSING THE 40-FOLIO LOOP FROM E.01 TO M.10',
                'body': 'Folio E.01 introduced percolation (the square-lattice site threshold p_c '
                        '≈ 0.5927) and Helmholtz–Hodge decomposition; Folio M.10 adds persistent '
                        'homology, a way to track connected pieces and loops in 3D point clouds '
                        'across scales.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.10-B · BOTTLENECK STABILITY AND NOISY IMAGES',
                'body': 'Noisy tomograms make single-threshold segmentation fragile. The '
                        'Bottleneck Stability Theorem bounds how far noise can move persistence '
                        'points, which is why persistence is attractive for noisy images; how '
                        'well it sizes pores in a particular biological sample would have to be '
                        'tested.'},
 'skill': {'filename': 'persistent-homology-betti-percolation-SKILL.md',
           'name': 'persistent-homology-betti-percolation',
           'description': 'AI-agnostic algebraic-topology and porous-media skill for '
                          'Vietoris-Rips/Alpha simplicial filtrations, boundary matrix reduction '
                          '(partial_{k-1} o partial_k = 0), Betti persistence barcodes, and '
                          'percolation throat sizing.',
           'rules': ['Verify the fundamental chain-complex identity partial_{k-1} * partial_k = 0 '
                     'and Euler-Poincare invariant chi = sum_k (-1)^k |K^(k)| = sum_k (-1)^k '
                     'beta_k.',
                     'Filter out topological noise features with persistence lifetime (d_i - b_i) '
                     '<= 2 * sigma_noise under the Cohen-Steiner Bottleneck Stability bound.',
                     'Compare the birth/death scale of the dominant H_1 / H_2 cycle with a '
                     'particle diameter only as a first geometric screen, and state that '
                     'transport also depends on chemistry and binding.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The Betti numbers '
                           'and the 38–116 nm bar are now labelled as values from a synthetic '
                           "teaching model, and the 'certifies 65 nm LNP passage' and 'BOTTLENECK "
                           "PASS' wording is withdrawn. The invented before-and-after pore radii "
                           'for CF sputum under therapy (42 nm to 118 nm) are removed; the bridge '
                           'now describes a proposed analysis with no clinical claim. E.01\'s '
                           '0.5927 is identified as the square-lattice site threshold.',
                'opus': 'Review: all DOIs checked in Crossref and the Scite index on 2026-11-14. '
                        'Added DOIs for Cohen-Steiner, Edelsbrunner & Harer (10.1007/s00454-006-1276-5), '
                        'Carlsson (10.1090/S0273-0979-09-01249-X) and Robins et al. '
                        '(10.1002/2015WR017937).'},
               {'edition': 'REV 1.0',
                'date': '2026-11-03',
                'summary': 'REV 1.0 (Published 2026-11-03): Crowning 40th Folio of Informatico.ai '
                           'Volume V, completing the circle back to Folio E.01 & P.03 via '
                           "Edelsbrunner, Letscher & Zomorodian's persistent homology (DOI "
                           '10.1007/s00454-002-2885-2).',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'chain complex exactness partial^2 = 0, Euler-Poincare alternation chi = '
                        'beta_0 - beta_1 + beta_2, and H_1 throat percolation threshold. (REV '
                        "1.1: this 'verified' wording is withdrawn for the throat threshold, "
                        'which is a synthetic model value.)'}],
 'volume': 5,
 'volume_code': 'VOL. 05',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1007/s00454-002-2885-2',
           'fetched_on': '2026-11-08',
           'citing_publications': 2416,
           'supporting': 8,
           'mentioning': 2230,
           'contrasting': 1,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 2,416 '
                      'citing publications (8 supporting, 2,230 mentioning, 1 contrasting) on '
                      "Edelsbrunner, Letscher & Zomorodian's foundational paper on topological "
                      'persistence and simplicial filtration barcodes.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['E.01', 'P.03', 'M.05'],
 'lineage_mode': 'TRIAD_SYNTHESIS · Completes the Circle to E.01 Percolation, P.03 Mucin Meshes & '
                 'M.05 Simplicial Geometry',
 'scite': {'doi': '10.1007/s00454-002-2885-2',
           'fetched_on': '2026-11-08',
           'citing_publications': 2416,
           'supporting': 8,
           'mentioning': 2230,
           'contrasting': 1,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 2,416 '
                      'citing publications (8 supporting, 2,230 mentioning, 1 contrasting) on '
                      "Edelsbrunner, Letscher & Zomorodian's foundational paper on topological "
                      'persistence and simplicial filtration barcodes.'},
 'act1_title': 'Act I — Completing the Circle Back to Folio E.01: How Algebraic Topology Sees the '
               'Exact Birth of a Percolating Pore',
 'act1_dropcap': 'In 1895, French polymath Henri Poincaré published Analysis Situs, laying the '
                 'bedrock of modern algebraic topology by asking what properties of a geometric '
                 'object survive when it is stretched, twisted, or crumpled like a sheet of '
                 'rubber. Poincaré understood that while metric distances and exact angles change '
                 'under deformation, fundamental topological traits—such as whether a shape is a '
                 'single connected piece, hollow like a basketball, or pierced by a tunnel like a '
                 'donut—remain stubbornly invariant. Yet for more than a century, algebraic '
                 'topology was considered too abstract for messy real-world data. If scientists '
                 'gathered a three-dimensional cloud of laser scanner points from a porous rock or '
                 'a delicate biological matrix, choosing how closely to connect the dots was an '
                 'difficult choice. In 2002, computer scientists Herbert Edelsbrunner, David '
                 'Letscher, and Afra Zomorodian published a way around it: instead of choosing a '
                 'single threshold, watch shapes form across expanding scales and record how long '
                 'each feature persists.',
 'act1_plain_bridge': 'Have you ever looked closely at a dry kitchen sponge and wondered whether a '
                      'tiny drop of water can travel all the way through from one side to the '
                      'other? If you look through a powerful microscope, you see a tangled jungle '
                      'of pores, pockets, and fibrous tunnels of every imaginable size. If an '
                      'engineer tries to measure the holes by picking one arbitrary cutoff size, '
                      'they run into a frustrating trap: set the ruler too small, and every single '
                      'atom looks like an isolated dust particle; set the ruler too large, and the '
                      'entire sponge turns into a solid, impenetrable block. Persistent homology '
                      'solves this puzzle by filming a continuous movie rather than taking a '
                      'single snapshot. Imagine slowly blowing soap bubbles around every pore in '
                      'the sponge. Small, irrelevant surface fuzz merges and vanishes almost '
                      'instantly, while genuine tunnels that allow fluids to flow through survive '
                      'across broad scales, standing out like tall trees in a low meadow.',
 'act1_body': 'In their landmark 2002 paper in Discrete & Computational Geometry (DOI '
              '10.1007/s00454-002-2885-2), Herbert Edelsbrunner, David Letscher, and Afra '
              'Zomorodian established the mathematical foundations of Persistent Homology. By '
              'growing spheres of radius epsilon around three-dimensional data points to construct '
              'a nested Vietoris–Rips or Alpha simplicial complex filtration, they tracked how '
              'topological cycles are born and eventually filled in. Using column reductions over '
              'binary field coefficients, each topological feature receives an exact birth scale '
              'and death scale, plotted as horizontal lines in a persistence barcode. In 2007, '
              'David Cohen-Steiner, Herbert Edelsbrunner, and John Harer proved the Bottleneck '
              'Stability Theorem, establishing that persistence diagrams are mathematically stable '
              'against experimental measurement noise. By connecting combinatorial matrix '
              'reductions directly to coordinate-free topological invariants, their algorithm '
              'opened multi-scale structural analysis to computation. In porous materials, Robins '
              'et al. (2016, Water Resources Research, DOI 10.1002/2015WR017937) related '
              'persistence features to percolating length scales in micro-CT images. Applying '
              'the same reading to biological meshes is a direction this folio proposes.',
 'act1_stakes': 'The development of persistent homology transformed algebraic topology from a '
                'purely theoretical branch of pure mathematics into an indispensable computational '
                'tool for twenty-first-century engineering. For generations, materials scientists '
                'and civil engineers analyzing three-dimensional tomography scans faced a '
                'crippling bottleneck: separating genuine fluid-carrying channels from image noise '
                'required subjective manual thresholding that varied from one technician to '
                'another. A minor tweak in contrast could falsely indicate that a cracked '
                'foundation was watertight or that a drug-delivery pathway was blocked. By '
                'grounding shape analysis in boundary operators where the boundary of a boundary '
                'is identically zero, persistent homology replaced human guesswork with '
                'mathematical invariants. Topological data analysis has since been explored in '
                'many fields, from materials to neuroscience (see Carlsson 2009 for an early '
                'survey). Topology gives a qualitative description on which quantitative '
                'physical models can build.',
 'pullquote': '"Persistent homology turns a static threshold guess into a movie of growing '
              'simplicial complexes: noise flickers in and out near the diagonal, while the true '
              'pore channel stands out as a long bar across scales."',
 'chronology': [('1895',
                 'Henri Poincaré publishes Analysis Situs, introducing simplicial complexes, '
                 'boundary operators partial_k, and homology groups H_k.'),
                ('2002',
                 'Edelsbrunner, Letscher & Zomorodian establish Persistent Homology and filtration '
                 'pairing in Discrete & Computational Geometry (DOI 10.1007/s00454-002-2885-2).'),
                ('2007',
                 'Cohen-Steiner, Edelsbrunner & Harer prove the Bottleneck Stability Theorem '
                 'd_B(D(f), D(g)) <= ||f - g||_inf for persistence diagrams.'),
                ('2016',
                 'Robins, Saadatfar, Delgado-Friedrichs & Sheppard relate persistence to '
                 'percolating length scales in micro-CT images of porous materials (DOI '
                 '10.1002/2015WR017937).')],
 'act2_title': 'Act II — How It Actually Works: Vietoris–Rips Boundary Reduction ∂_{k-1} ∘ ∂_k = 0 '
               '+ Betti Persistence Barcodes',
 'act2_intuition': 'Let X = {x_1, ..., x_n} be a discrete point cloud in three-dimensional '
                   'Euclidean space. At filtration radius epsilon, the Vietoris–Rips simplicial '
                   'complex VR(X, epsilon) includes a k-simplex whenever all pairwise distances '
                   'between its vertices satisfy ||x_a - x_b|| <= 2 * epsilon. Because boundary '
                   'operators satisfy the fundamental nilpotency identity partial_{k-1} o '
                   'partial_k = 0, the k-th homology group H_k = ker(partial_k) / '
                   'im(partial_{k+1}) isolates independent k-dimensional topological holes. The '
                   'Betti numbers count connected components (beta_0), one-dimensional loops and '
                   'tunnels (beta_1), and enclosed voids (beta_2), satisfying the alternating '
                   'Euler–Poincaré formula chi = beta_0 - beta_1 + beta_2. Standard Gaussian '
                   'column reduction transforms the boundary matrix into a paired list where each '
                   'simplex that births a cycle at radius b_i is paired with the simplex that '
                   'seals it at death radius d_i. In porous media, the persistence interval [b*, '
                   'd*] of the dominant beta_1 bar gives a geometric length scale for the '
                   'bottleneck: in this synthetic model the bar dies at 116 nm, larger than a 65 '
                   'nm particle. That is a geometric screen, not proof that a particle passes.',
 'act2_deepening': 'The deeper algebraic power of persistent homology rests upon the '
                   'Cohen-Steiner, Edelsbrunner, and Harer Bottleneck Stability Theorem, which '
                   'establishes that d_B(D(f), D(g)) <= ||f - g||_infinity. When spatial '
                   'perturbation noise sigma_noise is injected into the point cloud, each '
                   'birth-death coordinate in the persistence diagram can shift by at most the '
                   'supremum norm of the perturbation. Consequently, short-lived topological '
                   'artifacts generated by localized clustering remain tightly confined within a '
                   'narrow band along the main diagonal line b = d. In contrast, genuine '
                   'percolating cycles possess large persistence lifetimes (d_i - b_i) that '
                   'project far into the upper-left quadrant of the diagram. When analyzing porous '
                   'geomaterials or biopolymer meshes, the birth of a long-lived beta_1 cycle '
                   'marks the scale at which separate pockets join into loops. Moving the scale '
                   'slider and the noise slider together shows, in the model, that such a long '
                   'bar survives small perturbations, as the stability theorem predicts.',
 'act2_analogy': 'Everyday analogy: Imagine slowly flooding a mountainous landscape with rising '
                 'floodwaters. At first, you see countless isolated puddles forming in shallow '
                 'dips in the soil; as the water rises slightly higher, these puddles merge and '
                 'disappear quickly into the background. But when the water level reaches deep '
                 'mountain passes, it suddenly connects massive river valleys together, creating '
                 'major waterways that persist for miles. The short-lived puddles represent '
                 'geometric noise, while the long-lived valleys represent the enduring topological '
                 'features recorded in a persistence barcode.',
 'act2_plain_primer': 'To understand how persistent homology discovers hidden passages, imagine '
                      'adjusting two controls on a virtual microscope. The first control gradually '
                      'expands the detection bubble around every point in your material from a '
                      'tiny radius of fifteen nanometers up to a generous one hundred forty '
                      'nanometers. At small bubble sizes, the system registers only isolated '
                      'specks. As you dial the bubble size outward, triangles and '
                      'three-dimensional tetrahedra snap into place between neighboring points, '
                      'revealing hollow loops and tunnels before eventually merging into a single '
                      'solid cluster. The second control adds realistic measurement jitter to '
                      'simulate noisy laboratory scans. As you increase the noise dial, short, '
                      'flickering bars flutter along the baseline of the chart, but the primary '
                      'horizontal bar corresponding to the genuine, percolating pore throat '
                      'remains remarkably steady. Moving these dials together shows the scale '
                      'at which an open channel forms in the model, a first geometric hint of '
                      'whether a particle of a given size might fit.',
 'distill_diagram': {'analogy_title': 'The Flooding Mountain Pass',
                     'analogy_sub': 'Rising waters drown shallow puddles while connecting deep '
                                    'valleys',
                     'force_a_title': 'Filtration Radius Scale ε',
                     'force_a_sub': 'Expands simplicial balls to detect cycle births and deaths',
                     'force_b_title': 'Point Perturbation Noise σ',
                     'force_b_sub': 'Injects spatial jitter bounded by Bottleneck Stability '
                                    'guarantees',
                     'threshold_title': 'Critical Throat Percolation Bound',
                     'threshold_pass': 'Model: long H_1 bar is wider than a 65 nm particle',
                     'threshold_fail': 'Model: a bottleneck below the particle size would block '
                                       'it geometrically'},
 'walkthrough': ['Experiment 1 (Filtration Scale Radius epsilon): Drag Simplicial Filtration '
                 'Radius epsilon from 15 nm up to 140 nm. Watch isolated beta_0 components merge '
                 'into a connected complex while 1D percolating tunnels (beta_1) are born and '
                 'eventually sealed.',
                 'Experiment 2 (Measurement Noise & Bottleneck Stability): Adjust Point-Cloud '
                 'Perturbation Noise sigma_noise from 0.02 to 0.35. Observe how short noise bars '
                 'hover near the b = d diagonal while the dominant percolating beta_1 bar remains '
                 'rock-solid under the Bottleneck Stability bound.',
                 'Experiment 3 (From Poincaré Homology to E.01/P.03 Percolation): Step through '
                 'Stages 1 to 4 to inspect Vietoris–Rips simplex birth, Z_2 boundary matrix '
                 'reduction, Betti barcode lifetimes, and the model pore-throat reading.'],
 'act4_title': 'Act IV — Topological Data Analysis in Porous Media, Archive Closure & CF '
               'Mucus Mesh Tomography',
 'act4_human_ai': "Pairing Folio E.01's Darcy–Brinkman continuum solvers and Folio E.09's "
                  'concrete micro-CT scans with persistent homology could let materials '
                  'scientists read pore-throat scales from 3D X-ray tomograms with less '
                  'hand-tuned segmentation, along the lines of Robins et al. (2016).',
 'act4_deepening': 'As automated laboratory instruments generate massive three-dimensional image '
                   'datasets, combining persistent homology with deep neural representations '
                   'could support co-design workflows. Human researchers would set the physical '
                   'questions and boundary constraints, while topological pipelines extract '
                   'persistence summaries from large micro-CT scans and tomograms. Feeding Betti '
                   'curve summaries into learning models to predict permeability or failure '
                   'without full finite-element meshing is a research idea, not an established '
                   'practice described here. Major open '
                   'mathematical questions remain on the horizon: how can we efficiently compute '
                   'multi-parameter persistent homology when systems depend simultaneously on '
                   'temperature, pore pressure, and filtration scale, given that commutative '
                   'algebra forbids simple barcode decompositions over multi-graded polynomial '
                   'rings? Progress on multi-parameter persistence could give civil engineers, '
                   'hydrologists, and materials researchers better topological summaries for '
                   'questions such as groundwater transport and geothermal extraction.',
 'cf_bridge': 'Crowning Volume V Triad Synthesis (E.01 + P.03 + M.05 -> M.10): This 40th Folio '
              'closes the architectural loop back to Folio E.01. A proposed analysis, not a '
              'result: mucus and sputum form disordered 3D networks (Folio P.03), and persistent '
              'homology of an imaged network could, in principle, give a geometric pore-size '
              'scale to compare with particle sizes such as those discussed in Folio P.09. No '
              'images were analyzed for this folio, no pore sizes for any patient sample are '
              'reported, and nothing here is clinical or treatment guidance.',
 'sources': ['Edelsbrunner, H., Letscher, D., & Zomorodian, A. (2002). Topological persistence and '
             'simplification. Discrete & Computational Geometry, 28(4), 511–533. DOI: '
             '10.1007/s00454-002-2885-2.',
             'Cohen-Steiner, D., Edelsbrunner, H., & Harer, J. (2007). Stability of persistence '
             'diagrams. Discrete & Computational Geometry, 37(1), 103–120. DOI: '
             '10.1007/s00454-006-1276-5.',
             'Carlsson, G. (2009). Topology and data. Bulletin of the American Mathematical '
             'Society, 46(2), 255–308. DOI: 10.1090/S0273-0979-09-01249-X.',
             'Robins, V., Saadatfar, M., Delgado-Friedrichs, O., & Sheppard, A. P. (2016). '
             'Percolating length scales from topological persistence analysis of micro-CT images '
             'of porous materials. Water Resources Research, 52(1), 315–329. DOI: '
             '10.1002/2015WR017937.',
             'Peyré, G., & Cuturi, M. (2019). Computational Optimal Transport with Applications '
             'to Data Sciences (PythonOT/POT, https://github.com/PythonOT/POT). Foundations and '
             'Trends in Machine Learning, 11(5–6), 355–607. DOI: 10.1561/2200000073.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Vietoris-Rips '
        'simplicial filtration complex and H0/H1 Persistent Homology Betti barcode diagram">\n'
        '            <line x1="40" y1="188" x2="640" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <g id="tp-m10-simplicial-complex" transform="translate(175, 112)">\n'
        '              <polygon points="-75,-38 0,-58 68,-18" fill="var(--tp-prussian)" '
        'fill-opacity="0.2" stroke="var(--tp-prussian)" stroke-width="1.8"/>\n'
        '              <polygon points="-75,-38 -52,44 18,48 68,-18 0,-58" fill="none" '
        'stroke="var(--tp-minium)" stroke-width="2.5"/>\n'
        '              <circle cx="-75" cy="-38" r="5" fill="var(--tp-prussian)"/>\n'
        '              <circle cx="0" cy="-58" r="5" fill="var(--tp-prussian)"/>\n'
        '              <circle cx="68" cy="-18" r="5" fill="var(--tp-prussian)"/>\n'
        '              <circle cx="18" cy="48" r="5" fill="var(--tp-verdigris)"/>\n'
        '              <circle cx="-52" cy="44" r="5" fill="var(--tp-verdigris)"/>\n'
        '            </g>\n'
        '            <text x="52" y="26" font-size="10.5" font-weight="600" '
        'fill="currentColor">Vietoris–Rips Simplicial Filtration K_ε (∂_{k-1}∘∂_k = 0)</text>\n'
        '            <text id="tp-m10-svg-betti-text" x="52" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Betti Invariants: β₀ = 1 · β₁ = 3 Tunnels · χ = −2</text>\n'
        '            <line x1="350" y1="24" x2="350" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="368" y="26" font-size="10" font-weight="600" '
        'fill="currentColor">Persistence Barcode (H₀ Components &amp; H₁ Pore Tunnels)</text>\n'
        '            <line x1="380" y1="58" x2="625" y2="58" stroke="var(--tp-prussian)" '
        'stroke-width="4"/>\n'
        '            <line x1="380" y1="76" x2="465" y2="76" stroke="var(--tp-prussian)" '
        'stroke-width="4"/>\n'
        '            <line id="tp-m10-h1-bar-main" x1="425" y1="112" x2="598" y2="112" '
        'stroke="var(--tp-verdigris)" stroke-width="5"/>\n'
        '            <line x1="448" y1="132" x2="552" y2="132" stroke="var(--tp-verdigris)" '
        'stroke-width="4"/>\n'
        '            <line x1="485" y1="152" x2="512" y2="152" stroke="var(--tp-minium)" '
        'stroke-width="3"/>\n'
        '            <line id="tp-m10-eps-scan" x1="495" y1="42" x2="495" y2="176" '
        'stroke="var(--tp-minium)" stroke-width="1.8" stroke-dasharray="4,3"/>\n'
        '            <text x="380" y="102" font-size="9.5" fill="var(--tp-verdigris)">Longest H₁ '
        'Bar (Model) [b*, d*] = [38, 116 nm]</text>\n'
        '            <text id="tp-m10-stab-text" x="380" y="206" font-size="10" '
        'fill="var(--tp-prussian)">Bottleneck Stability d_B ≤ ||f − g||_∞ · Synthetic '
        'Model</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a 3D Vietoris-Rips simplicial complex filtration '
        'inside a porous hydrogel network alongside glowing H0/H1/H2 persistent homology Betti '
        'barcodes identifying a percolating pore channel would look like (artistic impression, not '
        'a formal plot)',
 'caption': 'Conceptual Vision Plate M.10-V (Imagining What It Would Look Like) · Artistic '
            'algebraic-topology visualization (completing the 40-Folio circle back to Folios E.01 '
            '& P.03) imagining a Vietoris–Rips simplicial filtration and Edelsbrunner–Zomorodian '
            'Betti persistence barcodes isolating a percolating pore throat.'}

DISPATCH = {'kicker': 'FRONTIER ALGEBRAIC TOPOLOGY DISPATCH · COMPLETING E.01, P.03 & M.05 · PERSISTENT '
           'HOMOLOGY',
 'headline': 'Persistent Homology & Betti Barcodes as a Way to Read Pore Scales in 3D Porous Media',
 'body': "Closing the 40-Folio arc back to Folio E.01's continuum percolation and Folio P.03's "
         "mucin hydrogels, Edelsbrunner, Letscher & Zomorodian's persistent homology (Discrete "
         'Comput. Geom. DOI 10.1007/s00454-002-2885-2) tracks Vietoris–Rips H_0/H_1/H_2 Betti '
         'barcodes across filtration scales; this folio shows the idea on a synthetic model.'}

META_3D = ('Vietoris–Rips Filtration & Betti Percolation Landscape',
 'X: Filtration Scale ε (nm) · Z: Cycle Homology Class · Y: Persistence Lifetime (d_i − b_i)')

ES_TRANSLATION = {'title_es': 'Homología Persistente, Filtraciones Simpliciales de Vietoris–Rips, Códigos de Barras '
             'de Betti y Umbrales Topológicos de Percolación en Medios Desordenados',
 'subtitle_es': 'Cerrando el círculo de 40 Folios hacia E.01 y P.03: cómo la homología persistente '
                'de Edelsbrunner, Letscher y Zomorodian sigue poros y túneles a través de las '
                'escalas. Los códigos de barras que se muestran vienen de un modelo sintético de '
                'enseñanza, no de muestras reales.',
 'why_es': 'Imagina inundar lentamente una cordillera: los charcos pequeños aparecen y desaparecen '
           'rápido (barras cortas de ruido), mientras que los pasos de montaña profundos que '
           'conectan valles enteros destacan como barras largas e indestructibles.',
 'plain_es': 'En 1895, el matemático francés Henri Poincaré fundó la topología algebraica para '
             'estudiar aquellas propiedades geométricas que no cambian cuando un objeto se estira '
             'o se deforma sin romperse. Durante más de un siglo, estas ideas parecían demasiado '
             'abstractas para aplicarse a datos experimentales reales. Imaginen que ustedes '
             'observan una esponja de cocina bajo un microscopio potente para saber si una gota de '
             'agua puede atravesarla de lado a lado. Si intentan medir el tamaño de los orificios '
             'eligiendo una regla fija, cometerán errores graves: si la medida es muy pequeña, '
             'cada partícula parecerá aislada; si es muy grande, la esponja parecerá un bloque '
             'impenetrable. En 2002, Herbert Edelsbrunner, David Letscher y Afra Zomorodian '
             'publicaron una salida a este dilema: la homología persistente. En lugar de tomar una sola fotografía fija, '
             'el método graba una película continua donde las burbujas crecen sobre los datos: el '
             'ruido desaparece rápidamente, mientras que los verdaderos canales abiertos '
             'sobreviven y destacan con total claridad.',
 'deep_es': 'El principio matemático de la homología persistente construye una filtración '
            'simplicial de Vietoris–Rips haciendo crecer esferas de radio épsilon alrededor de '
            'cada punto de la muestra tridimensional. Mediante operaciones de álgebra lineal sobre '
            'matrices de frontera, el algoritmo empareja el momento de nacimiento de cada ciclo '
            'topológico con su escala de desaparición, generando un código de barras de Betti. Los '
            'dos parámetros del sistema permiten explorar la escala de filtración y el nivel de '
            'ruido en los datos. El Teorema de Estabilidad del Cuello de Botella garantiza que las '
            'perturbaciones experimentales solo muevan los puntos cerca de la diagonal, '
            'manteniendo inalterables las barras largas que representan estructuras físicas '
            'genuinas. En el modelo sintético, la barra de dimensión uno más duradera termina en '
            '116 nanómetros, más que el tamaño de una partícula de 65 nanómetros. Es una primera '
            'señal geométrica, no una prueba de que la partícula pase; Robins y colaboradores '
            '(2016) relacionaron este tipo de rasgos con escalas de percolación en microtomografías '
            'de materiales porosos.',
 'bridge_es': 'Un análisis propuesto, no un resultado: la homología persistente de una red de '
              'moco o esputo obtenida por imagen podría, en principio, dar una escala geométrica '
              'de poro para compararla con el tamaño de partículas como las del Folio P.09. No se '
              'analizaron imágenes para este folio, no se reportan tamaños de poro de ninguna '
              'muestra de pacientes y nada aquí es una guía clínica ni de tratamiento.'}
