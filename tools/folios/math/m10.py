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
 'lineage_mode': 'TRIAD_SYNTHESIS · Completes the Circle to E.01 Percolation, P.03 Mucin '
                 'Meshes & M.05 Simplicial Geometry',
 'title': 'Persistent Homology, Vietoris–Rips Simplicial Filtrations, Betti Barcodes & '
          'Topological Percolation Thresholds in Disordered Media',
 'subtitle': 'Synthesizing Folios E.01, P.03, and M.05: an explanatory model—not a structural, '
             'hydrological, or clinical design method—of how persistent homology pairs '
             'topological cycle births and deaths across filtration scales. Numerical readouts '
             'shown here are fixed illustrative text.',
 'date_published': '2026-11-03',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'PERSISTENT HOMOLOGY · REV 1.1',
 'primary_kernel': 'tools/discovery/frontier_ai_math_catalog.py',
 'governing_law': '∂_{k−1} ∘ ∂_k = 0 · β_k^{i,j} = rank(H_k(K_i) → H_k(K_j)) · d_B(D(f), D(g)) '
                  '≤ ||f − g||_∞',
 'colophon': {'identifier': 'M.10 · Persistent Homology & Topological Persistence Barcodes',
              'kernels': 'Alpha & Vietoris–Rips Filtrations · Z_2 Boundary Reduction ∂_k · '
                         'Bottleneck Stability',
              'benchmarks': 'Abstract 7-vertex flag 2-skeleton (|V|=7, |E|=10, |F|=1): '
                            'β_0=1, β_1=3, χ=−2 · H_1 [38, 116] nm (fixed illustrative)',
              'bridge': 'Synthesizes E.01/P.03/M.05 · micro-CT persistence (Robins et al. '
                        '2016) as a method reference'},
 'sliders': [{'label': 'Simplicial Filtration Scale',
              'min': 15.0,
              'max': 140.0,
              'step': 5.0,
              'value': 65.0,
              'unit': ' nm'},
             {'label': 'Point-Cloud Perturbation Noise',
              'min': 0.02,
              'max': 0.35,
              'step': 0.01,
              'value': 0.08,
              'unit': 'σ = '}],
 'steps': ['Stage 1 (Alpha & Vietoris–Rips Filtrations): 3D alpha filtrations (Edelsbrunner, '
           'Letscher & Zomorodian 2002, DOI 10.1007/s00454-002-2885-2) and Vietoris–Rips '
           'cliques (indexed by diameter ||x_a − x_b|| ≤ t in Carlsson 2009, DOI '
           '10.1090/S0273-0979-09-01249-X and Bauer 2021, DOI 10.1007/s41468-021-00071-5, so '
           't = 2ε under ball radius ε) build nested complexes.',
           'Stage 2 (Chain Nilpotency & Z_2 Pairing, DOI 10.1007/s00454-002-2885-2): ∂_{k−1} ∘ '
           '∂_k = 0 gives H_k = ker(∂_k)/im(∂_{k+1}) and pairs cycle births b_i with bounding '
           'deaths d_i. Explanation only, not a structural or clinical design method.',
           'Stage 3 (Bottleneck Stability, DOI 10.1007/s00454-006-1276-5): Cohen-Steiner, '
           'Edelsbrunner & Harer bound d_B(D(f), D(g)) ≤ ||f − g||_∞ for tame functions; '
           'under uniform bound δ in matching units, bars with d_i − b_i > 2δ stay off b = d '
           '(σ = 0.08 is a dimensionless slider setting).',
           'Stage 4 (Micro-CT Persistence Reference, DOI 10.1002/2015WR017937): Robins et al. '
           '(2016) relate persistence on bead, sand, sandstone, and limestone micro-CT images '
           'to pore-size distributions and percolating sphere radius ([38, 116] nm is fixed '
           'illustrative text; chemistry and binding also affect transport).'],
 'readouts': [{'label': 'Betti Numbers (β_0, β_1, β_2, model)',
               'value': 'β₀ = 1 · β₁ = 3 · β₂ = 0 (Fixed 7-Vertex 2-Skeleton)'},
              {'label': 'Euler–Poincaré Invariant (χ, model)',
               'value': 'χ = 7 − 10 + 1 = −2 (Fixed Illustrative Text)'},
              {'label': 'Longest H_1 Bar Death Scale (model)',
               'value': '116 nm on [38, 116] nm (Fixed Illustrative Text)'},
              {'label': 'M.10 Model Boundary',
               'value': 'EXPLANATORY MODEL · NOT A DESIGN METHOD'}],
 'spec_plate': {'division': 'ALGEBRAIC TOPOLOGY & POROUS TOMOGRAPHY · EXPLANATORY MODEL (NOT A DESIGN SPEC)',
                'title': 'Illustrative Study: Alpha & Vietoris–Rips Persistent Homology in '
                         'Porous Media',
                'body': 'Explanatory model only, not a structural, hydrological, or clinical '
                        'design method: none of these illustrative numbers (65 nm, β₀ = 1, '
                        'β₁ = 3, χ = −2, 38–116 nm) may be used on a real structure, '
                        'foundation, or patient sample. No boundary-matrix reducer runs in the '
                        'browser, no micro-CT or hydrogel images were analyzed here, and the '
                        'four readout cards stay fixed text.',
                'meta': 'Method sources cited, not reproduced: Edelsbrunner, Letscher & '
                        'Zomorodian 2002 (DOI 10.1007/s00454-002-2885-2) · Cohen-Steiner, '
                        'Edelsbrunner & Harer 2007 (DOI 10.1007/s00454-006-1276-5) · Robins et '
                        'al. 2016 (DOI 10.1002/2015WR017937)'},
 'sidenote_1': {'kicker': 'SIDENOTE M.10-A · ALPHA FILTRATIONS, VIETORIS–RIPS CLIQUES & RIPSER',
                'body': 'Folio E.01 used square-lattice percolation (p_c ≈ 0.5927). '
                        'Edelsbrunner, Letscher & Zomorodian (2002, DOI '
                        '10.1007/s00454-002-2885-2) defined persistence on 3D alpha-complex '
                        'filtrations, while Ripser (Bauer 2021, DOI '
                        '10.1007/s41468-021-00071-5) computes Vietoris–Rips barcodes using '
                        'implicit coboundaries and apparent pairs.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.10-B · BOTTLENECK STABILITY VS. DIMENSIONLESS SLIDER JITTER',
                'body': 'Cohen-Steiner, Edelsbrunner & Harer (2007, DOI '
                        '10.1007/s00454-006-1276-5) bound d_B(D(f), D(g)) ≤ ||f − g||_∞ under a '
                        'supremum norm in matching units. Unbounded random noise lacks a finite '
                        'supremum bound unless truncated, and the σ = 0.08 slider here is a '
                        'normalized dimensionless display control.'},
 'skill': {'filename': 'persistent-homology-betti-percolation-SKILL.md',
           'name': 'persistent-homology-betti-percolation',
           'description': 'Explanatory algebraic-topology companion for Alpha and Vietoris-Rips '
                          'simplicial filtrations, Z_2 boundary reduction, persistence '
                          'barcodes, bottleneck stability, and micro-CT pore-scale '
                          'persistence. Explanation only, not a structural, hydrological, or '
                          'clinical design method; no folio number may be used on a real '
                          'structure or patient sample.',
           'rules': ['Explanation only, not a structural, hydrological, or clinical design '
                     "method: none of this folio's illustrative numbers (65 nm, beta_0 = 1, "
                     'beta_1 = 3, chi = -2, 38-116 nm) may be used on a real structure, '
                     'foundation, or patient sample; check chain nilpotency partial_{k-1} o '
                     'partial_k = 0 and truncate chi = sum_{k>=0} (-1)^k |K^(k)| = sum_{k>=0} '
                     '(-1)^k beta_k to beta_0 - beta_1 + beta_2 only if beta_k = 0 for k >= 3 '
                     '(DOI 10.1007/s00454-002-2885-2).',
                     'Apply diagonal separation d_i - b_i > 2*delta under tame bottleneck '
                     'stability d_B(D(f), D(g)) <= ||f - g||_inf <= delta only in matching '
                     'units (DOI 10.1007/s00454-006-1276-5), account for diameter t = 2*epsilon '
                     'vs. ball-radius epsilon conventions in Vietoris-Rips software (DOI '
                     '10.1090/S0273-0979-09-01249-X; DOI 10.1007/s41468-021-00071-5), and do '
                     'not equate a dimensionless slider (sigma = 0.08) to a nanometer bound.',
                     'Distinguish Robins et al. (2016, DOI 10.1002/2015WR017937) persistence '
                     'on bead, sand, sandstone, and limestone micro-CT images from untested '
                     'biological gel proposals, note that charge and binding could also block '
                     'particles, and state when readouts are fixed illustrative text.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The Betti '
                           'numbers and the 38–116 nm bar are now labeled as values from a '
                           'synthetic teaching model, and the earlier 65 nm LNP passage claim '
                           "and 'BOTTLENECK PASS' wording are withdrawn. The invented "
                           'before-and-after pore radii for CF sputum under therapy (42 nm to '
                           '118 nm) are removed; the bridge now describes a proposed analysis '
                           "with no clinical claim. E.01's 0.5927 is identified as the "
                           'square-lattice site threshold.',
                'opus': 'Review: all DOIs checked in Crossref and the Scite index on '
                        '2026-11-14. Added DOIs for Cohen-Steiner, Edelsbrunner & Harer '
                        '(10.1007/s00454-006-1276-5), Carlsson (10.1090/S0273-0979-09-01249-X) '
                        'and Robins et al. (10.1002/2015WR017937).'},
               {'edition': 'REV 1.0',
                'date': '2026-11-03',
                'summary': 'REV 1.0 (Published 2026-11-03): Crowning 40th Folio of '
                           'Informatico.ai Volume V, completing the circle back to Folio E.01 '
                           "& P.03 via Edelsbrunner, Letscher & Zomorodian's persistent "
                           'homology (DOI 10.1007/s00454-002-2885-2).',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Checked chain '
                        'boundary nilpotency partial^2 = 0 (earlier printed as "exactness"), '
                        'Euler-Poincare alternation chi = beta_0 - beta_1 + beta_2, and H_1 '
                        'throat threshold. (REV 1.1: earlier "Verified" wording is withdrawn '
                        'across all three items because no verifier script ran here and the '
                        'throat threshold is a synthetic model value.)'}],
 'volume': 5,
 'volume_code': 'VOL. 05',
 'reading_time': '19 MIN READ',
 'word_count': '4,400 WORDS',
 'scite': {'doi': '10.1007/s00454-002-2885-2',
           'fetched_on': '2026-11-24',
           'citing_publications': 2459,
           'supporting': 8,
           'mentioning': 2256,
           'contrasting': 1,
           'retracted': False,
           'summary': 'Scite Smart Citation Index [observed: Scite ML citation classification, '
                      'accessed 2026-11-24]: 0 retractions; 2,459 citing publications (8 '
                      'supporting, 2,256 mentioning, 1 contrasting citation statements) for '
                      'Edelsbrunner, Letscher & Zomorodian 2002 (DOI '
                      '10.1007/s00454-002-2885-2). Counts describe that paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '19 MIN READ',
 'word_count': '4,400 WORDS',
 'parent_folios': ['E.01', 'P.03', 'M.05'],
 'lineage_mode': 'TRIAD_SYNTHESIS · Completes the Circle to E.01 Percolation, P.03 Mucin '
                 'Meshes & M.05 Simplicial Geometry',
 'scite': {'doi': '10.1007/s00454-002-2885-2',
           'fetched_on': '2026-11-24',
           'citing_publications': 2459,
           'supporting': 8,
           'mentioning': 2256,
           'contrasting': 1,
           'retracted': False,
           'summary': 'Scite Smart Citation Index [observed: Scite ML citation classification, '
                      'accessed 2026-11-24]: 0 retractions; 2,459 citing publications (8 '
                      'supporting, 2,256 mentioning, 1 contrasting citation statements) for '
                      'Edelsbrunner, Letscher & Zomorodian 2002 (DOI '
                      '10.1007/s00454-002-2885-2). Counts describe that paper, not this folio.'},
 'act1_title': "Act I — Completing the Circle Back to Folio E.01: From Henri Poincaré's "
               'Analysis Situs to Multi-Scale Persistence Barcodes',
 'act1_dropcap': "Henri Poincaré's 1895 memoir Analysis Situs asked a plain question about "
                 'geometry: what stays unchanged as a rubber sheet stretches or twists? '
                 'Lengths and angles shift under deformation, yet connected pieces, hollow '
                 'cavities, and open tunnels remain invariant unless the sheet tears or glues. '
                 'For a century, noisy three-dimensional point clouds from physical scans '
                 'resisted that clean theory. Choosing one fixed cutoff distance was fragile. '
                 'A tiny ruler left isolated specks, whereas a wide ruler fused the sample '
                 'into one solid block. In 2002, Herbert Edelsbrunner, David Letscher, and '
                 "Afra Zomorodian swept across scales instead, pairing each cycle's birth with "
                 'the scale that fills it. Brief flickers mark local clutter, while long-lived '
                 'features trace enduring passages across rock and sand. This folio offers a '
                 'mathematical explanation, not a structural, hydrological, or clinical design '
                 'method, and none of its numbers apply to real structures.',
 'act1_plain_bridge': 'Hold a dry sponge toward light. Can water cross from side to side? '
                      'Under strong microscope magnification, tiny surface pockets, narrow '
                      'necks, and wider channels sit tangled together inside the porous block. '
                      'Measuring those openings with one fixed ruler fails if scanner readings '
                      'carry small position jitter across the sample. Persistent homology '
                      'instead grows a sphere around each point stepwise. Shallow dents fill '
                      'fast, leaving short bars. Wider passages remain open across many steps '
                      'and stand out as much longer horizontal bars beside the short clutter. '
                      'Researchers use such summaries to study pore scales in '
                      'three-dimensional tomography scans of sand, bead packs, and stone. '
                      'Surface charge and chemical binding could also block particles in wet '
                      'gels. On this page every numerical readout is fixed illustrative text, '
                      'and nothing serves as a structural design check or clinical guide.',
 'act1_body': 'Edelsbrunner, Letscher, and Zomorodian (2002, DOI 10.1007/s00454-002-2885-2) '
              'introduced topological persistence on three-dimensional alpha-complex '
              'filtrations via modulo-two boundary reduction, pairing each cycle birth with '
              'its filling simplex. Gunnar Carlsson (2009, DOI 10.1090/S0273-0979-09-01249-X) '
              'surveyed Vietoris–Rips and Čech point-cloud persistence barcodes. '
              'Cohen-Steiner, Edelsbrunner, and Harer (2007, DOI 10.1007/s00454-006-1276-5) '
              'bounded persistence-diagram shifts under continuous tame perturbations by the '
              'supremum norm. In porous media, Robins et al. (2016, DOI 10.1002/2015WR017937) '
              'used micro-CT images of spherical bead packings, unconsolidated sand, '
              'sandstones, and a limestone to relate persistence summaries to pore-size '
              'distributions, connectivity numbers, and percolating sphere radius.',
 'act1_stakes': 'Explicit boundary matrices for dense Vietoris–Rips clique filtrations can '
                'exhaust memory. Ulrich Bauer (2021, DOI 10.1007/s41468-021-00071-5) improved '
                'time and memory in Ripser by using implicit coboundary representations and '
                'apparent-pair discrete gradients without storing the full coboundary matrix. '
                'This folio explains those mathematical constructions; it is not a design '
                'method for foundations, rock engineering, hydrology, or clinical care, and '
                'none of its illustrative values may be used on a real structure or patient '
                'sample.',
 'pullquote': '"Persistent homology replaces a single fragile threshold choice with a nested '
              "simplicial filtration, pairing each topological cycle's birth scale with the "
              'scale where a bounding chain fills it."',
 'chronology': [('1895–1900',
                 'Henri Poincaré publishes Analysis Situs and its early complements, studying '
                 'manifold homologies, Betti numbers, and polyhedral subdivisions.'),
                ('2002',
                 'Edelsbrunner, Letscher & Zomorodian formulate alpha-complex topological '
                 'persistence and modulo-two filtration pairing (DOI '
                 '10.1007/s00454-002-2885-2).'),
                ('2007–2009',
                 'Cohen-Steiner, Edelsbrunner & Harer show bottleneck stability for tame '
                 'functions (DOI 10.1007/s00454-006-1276-5); Carlsson surveys point-cloud '
                 'persistence barcodes (DOI 10.1090/S0273-0979-09-01249-X).'),
                ('2016–2021',
                 'Robins et al. relate micro-CT persistence to percolating sphere radii in '
                 'bead, sand, and rock scans (DOI 10.1002/2015WR017937); Bauer publishes '
                 'Ripser for Vietoris–Rips barcodes (DOI 10.1007/s41468-021-00071-5).')],
 'act2_title': 'Act II — How It Works: Alpha & Vietoris–Rips Filtrations, Z_2 Boundary '
               'Reduction & Bottleneck Stability',
 'act2_intuition': 'For a finite point cloud X in ℝ^d, Carlsson (2009, DOI '
                   '10.1090/S0273-0979-09-01249-X) and Ripser (Bauer 2021, DOI '
                   '10.1007/s41468-021-00071-5) index Vietoris–Rips cliques by diameter t '
                   '(||x_a − x_b|| ≤ t), which equals t = 2ε under ball radius ε (||x_a − '
                   'x_b|| ≤ 2ε), whereas 3D alpha filtrations restrict to Delaunay '
                   'subcomplexes (Edelsbrunner et al. 2002, DOI 10.1007/s00454-002-2885-2). '
                   'Over Z_2, boundary nilpotency ∂_{k−1} ∘ ∂_k = 0 defines homology H_k = '
                   'ker(∂_k)/im(∂_{k+1}) of rank β_k, and Euler characteristic χ = ∑_{k≥0} '
                   '(−1)^k |K^(k)| = ∑_{k≥0} (−1)^k β_k reduces to β_0 − β_1 + β_2 if β_k = '
                   '0 for k ≥ 3. In Plate M.10-A, the abstract combinatorial 7-vertex flag '
                   '2-skeleton (planar sketch, not drawn to 2D 2ε scale: |V| = 7, |E| = 10, '
                   '|F| = 1 filled triangle plus three chordless 4-cycles) yields β_0 = 1, '
                   'β_1 = 3, β_2 = 0, χ = −2, and fixed illustrative H_1 bar [38, 116] nm.',
 'act2_deepening': 'Cohen-Steiner, Edelsbrunner, and Harer (2007, DOI '
                   '10.1007/s00454-006-1276-5) showed bottleneck stability d_B(D(f), '
                   'D(g)) ≤ ||f − g||_∞ for tame functions. Each point (b_i, d_i) sits at L_∞ '
                   'distance (d_i − b_i)/2 from the diagonal b = d. Under a uniform bound δ in '
                   'matching units, intervals with d_i − b_i > 2δ remain separated from b = d, '
                   'whereas unbounded random jitter has no finite supremum without truncation. '
                   'Here Point-Cloud Perturbation Noise is a dimensionless control, and no '
                   'matrix reduction runs.',
 'act2_analogy': 'Spring snowmelt rising slowly across a mountain basin separates shallow dips '
                 'from deep valley passes. Small hollows fill within centimeters of water '
                 'rise. Deep passes linking neighboring valleys stay distinct across many '
                 'meters before the rising water joins them. Where the analogy stops: rising '
                 'water sweeps one height across a two-dimensional surface. By contrast, a '
                 'three-dimensional filtration builds simplices from point distances and can '
                 'enclose cavities with no terrain counterpart.',
 'act2_plain_primer': 'Two controls sit below. Simplicial Filtration Scale sweeps the ball '
                      'radius from 15.0 to 140.0 nanometers around a 65.0 nanometer reference '
                      'setting. Point-Cloud Perturbation Noise sweeps a dimensionless jitter '
                      'index from 0.02 to 0.35 around 0.08. Dragging either slider updates its '
                      'unit label, the generic stage vector overlay, and the three-dimensional '
                      'surface view in the browser. No boundary matrix is reduced here: the '
                      'seven-vertex sketch, schematic barcode bars, and four readout cards '
                      'keep their fixed illustrative text.',
 'distill_diagram': {'analogy_title': 'The Flooding Mountain Pass',
                     'analogy_sub': 'Rising water merges shallow hollows fast; 3D clique '
                                    'filtrations differ',
                     'force_a_title': 'Simplicial Filtration Scale',
                     'force_a_sub': 'Indexes ball radius ε as simplices enter and bound cycles',
                     'force_b_title': 'Uniform Perturbation Bound δ',
                     'force_b_sub': 'Tame stability bounds diagram shift by d_B ≤ ||f − g||_∞',
                     'threshold_title': 'Diagonal Separation vs. Collapse',
                     'threshold_pass': 'Model: bars with d_i − b_i > 2δ stay off the b = d '
                                       'diagonal',
                     'threshold_fail': 'Model: bars with d_i − b_i ≤ 2δ can shift onto b = d'},
 'walkthrough': ['Experiment 1 (Simplicial Filtration Scale): Sweep Simplicial Filtration '
                 'Scale across 15.0–140.0 nm to update its nm label, the stage vector overlay, '
                 'and the 3D surface; β₀ = 1, β₁ = 3, χ = −2, and [38, 116] nm stay fixed.',
                 'Experiment 2 (Point-Cloud Perturbation Noise): Sweep Point-Cloud '
                 'Perturbation Noise across 0.02–0.35 to update the σ label, overlay, and 3D '
                 'view; schematic barcode bars and readout cards stay fixed text.',
                 'Experiment 3 (Four-Stage Stepper): Step through Stages 1–4 for Alpha and '
                 'Vietoris–Rips filtrations, Z_2 boundary pairing, bottleneck stability, and '
                 'micro-CT persistence references.'],
 'act4_title': 'Act IV — Micro-CT Porous Tomography, Implicit Coboundary Solvers & Open '
               'Frontiers',
 'act4_human_ai': 'Robins et al. (2016, DOI 10.1002/2015WR017937) related topological '
                  'persistence in micro-CT images of spherical bead packings, sand, '
                  'sandstones, and a limestone to pore-size distributions, connectivity '
                  'numbers, and percolating sphere radius. Such summaries could complement '
                  'continuum scans in Folios E.01 and E.09, while Ripser (Bauer 2021, DOI '
                  '10.1007/s41468-021-00071-5) lowers Vietoris–Rips memory via implicit '
                  'coboundaries and apparent pairs.',
 'act4_deepening': 'Combining micro-CT persistence (DOI 10.1002/2015WR017937) with flow '
                   'solvers could suggest porous descriptors, though voxel resolution, '
                   'segmentation, and wetting might alter permeability and were not tested '
                   'here. Multi-parameter persistence—tracking filtration scale alongside '
                   'pressure or temperature—remains an active mathematical research problem '
                   '(Carlsson 2009, DOI 10.1090/S0273-0979-09-01249-X) rather than a settled '
                   'engineering design method.',
 'cf_bridge': 'Triad Synthesis Note (E.01 + P.03 + M.05 -> M.10): Button et al. (2012, DOI '
              '10.1126/science.1223012) proposed the airway gel-on-brush model in which '
              'tethered mucins and mucopolysaccharides in the periciliary layer separate the '
              'mucus layer from airway epithelia. Whether persistence methods like Robins et '
              'al. (2016, DOI 10.1002/2015WR017937) could help summarize imaged biopolymer '
              'networks is an untested question, and charge or binding could still block '
              'particles; no biological samples were analyzed and nothing here is clinical '
              'guidance.',
 'sources': ['Edelsbrunner, H., Letscher, D., & Zomorodian, A. (2002). Topological persistence '
             'and simplification. Discrete & Computational Geometry, 28(4), 511–533. DOI: '
             '10.1007/s00454-002-2885-2.',
             'Cohen-Steiner, D., Edelsbrunner, H., & Harer, J. (2007). Stability of '
             'persistence diagrams. Discrete & Computational Geometry, 37(1), 103–120. DOI: '
             '10.1007/s00454-006-1276-5.',
             'Carlsson, G. (2009). Topology and data. Bulletin of the American Mathematical '
             'Society, 46(2), 255–308. DOI: 10.1090/S0273-0979-09-01249-X.',
             'Button, B., Cai, L.-H., Ehre, C., Kesimer, M., Hill, D. B., Sheehan, J. K., '
             'Boucher, R. C., & Rubinstein, M. (2012). A periciliary brush promotes the lung '
             'health by separating the mucus layer from airway epithelia. Science, 337(6097), '
             '937–941. DOI: 10.1126/science.1223012.',
             'Robins, V., Saadatfar, M., Delgado-Friedrichs, O., & Sheppard, A. P. (2016). '
             'Percolating length scales from topological persistence analysis of micro-CT '
             'images of porous materials. Water Resources Research, 52(1), 315–329. DOI: '
             '10.1002/2015WR017937.',
             'Bauer, U. (2021). Ripser: efficient computation of Vietoris–Rips persistence '
             'barcodes. Journal of Applied and Computational Topology, 5(3), 391–423. DOI: '
             '10.1007/s41468-021-00071-5.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Abstract '
        'combinatorial 7-vertex flag 2-skeleton (|V|=7, |E|=10, |F|=1, beta_0=1, beta_1=3, '
        'chi=-2) and schematic H0/H1 persistence barcode diagram">\n'
        '            <line x1="40" y1="188" x2="640" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <g id="tp-m10-simplicial-complex" transform="translate(172, 112)">\n'
        '              <polygon points="-28,-16 28,-16 0,26" fill="var(--tp-prussian)" '
        'fill-opacity="0.22" stroke="var(--tp-prussian)" stroke-width="1.8"/>\n'
        '              <line x1="-28" y1="-16" x2="0" y2="-60" stroke="var(--tp-minium)" '
        'stroke-width="2.2"/>\n'
        '              <line x1="0" y1="-60" x2="76" y2="-8" stroke="var(--tp-minium)" '
        'stroke-width="2.2"/>\n'
        '              <line x1="76" y1="-8" x2="28" y2="-16" stroke="var(--tp-minium)" '
        'stroke-width="2.2"/>\n'
        '              <line x1="76" y1="-8" x2="38" y2="52" stroke="var(--tp-minium)" '
        'stroke-width="2.2"/>\n'
        '              <line x1="38" y1="52" x2="0" y2="26" stroke="var(--tp-minium)" '
        'stroke-width="2.2"/>\n'
        '              <line x1="38" y1="52" x2="-68" y2="20" stroke="var(--tp-minium)" '
        'stroke-width="2.2"/>\n'
        '              <line x1="-68" y1="20" x2="-28" y2="-16" stroke="var(--tp-minium)" '
        'stroke-width="2.2"/>\n'
        '              <circle cx="-28" cy="-16" r="4.8" fill="var(--tp-prussian)"/>\n'
        '              <circle cx="28" cy="-16" r="4.8" fill="var(--tp-prussian)"/>\n'
        '              <circle cx="0" cy="26" r="4.8" fill="var(--tp-prussian)"/>\n'
        '              <circle cx="0" cy="-60" r="4.8" fill="var(--tp-verdigris)"/>\n'
        '              <circle cx="76" cy="-8" r="4.8" fill="var(--tp-verdigris)"/>\n'
        '              <circle cx="38" cy="52" r="4.8" fill="var(--tp-verdigris)"/>\n'
        '              <circle cx="-68" cy="20" r="4.8" fill="var(--tp-verdigris)"/>\n'
        '            </g>\n'
        '            <text x="48" y="26" font-size="9.8" font-weight="600" '
        'fill="currentColor">Abstract 7-Vertex Flag 2-Skeleton (|V|=7, |E|=10, |F|=1)</text>\n'
        '            <text id="tp-m10-svg-betti-text" x="48" y="203" font-size="9.8" '
        'fill="var(--tp-verdigris)">Fixed Invariants: β₀ = 1 · β₁ = 3 Loops · χ = −2</text>\n'
        '            <line x1="350" y1="24" x2="350" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="366" y="26" font-size="9.8" font-weight="600" '
        'fill="currentColor">Schematic Barcode (Selected H₀ &amp; 3 H₁ Bars)</text>\n'
        '            <line x1="380" y1="56" x2="625" y2="56" stroke="var(--tp-prussian)" '
        'stroke-width="4"/>\n'
        '            <line x1="380" y1="74" x2="465" y2="74" stroke="var(--tp-prussian)" '
        'stroke-width="4"/>\n'
        '            <line id="tp-m10-h1-bar-main" x1="425" y1="114" x2="598" y2="114" '
        'stroke="var(--tp-verdigris)" stroke-width="5"/>\n'
        '            <line x1="448" y1="134" x2="552" y2="134" stroke="var(--tp-verdigris)" '
        'stroke-width="4"/>\n'
        '            <line x1="485" y1="154" x2="512" y2="154" stroke="var(--tp-minium)" '
        'stroke-width="3"/>\n'
        '            <line id="tp-m10-eps-scan" x1="495" y1="42" x2="495" y2="174" '
        'stroke="var(--tp-minium)" stroke-width="1.8" stroke-dasharray="4,3"/>\n'
        '            <text x="502" y="103" font-size="9" fill="var(--tp-verdigris)">H₁ bar: '
        '[38, 116] nm (fixed)</text>\n'
        '            <text id="tp-m10-stab-text" x="366" y="203" font-size="9.8" '
        'fill="var(--tp-prussian)">d_B ≤ ||f − g||_∞ · Fixed Teaching Sketch</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a 3D simplicial filtration inside a porous '
        'network alongside H0 and H1 persistent homology Betti barcodes would look like '
        '(artistic impression, not a measured structure or specification; exact structure and '
        'specifications are kept strictly intact in deterministic Plate M.10-A and Plate '
        'M.10-B below)',
 'caption': 'Conceptual Vision Plate M.10-V (Imagining What It Would Look Like) · Artistic '
            'impression of a simplicial filtration and persistence barcode; governing '
            'equations and fixed model specifications live in deterministic Plates M.10-A and '
            'M.10-B below.'}

DISPATCH = {'kicker': 'ALGEBRAIC TOPOLOGY & POROUS TOMOGRAPHY · SYNTHESIZING E.01, P.03 & M.05 · '
           'PERSISTENT HOMOLOGY',
 'headline': 'Persistent Homology, Bottleneck Stability & Percolating Sphere Scales in '
             'Micro-CT Porous Media',
 'body': "Synthesizing Folios E.01, P.03, and M.05, Edelsbrunner, Letscher, and Zomorodian's "
         'alpha-complex persistence (DOI 10.1007/s00454-002-2885-2) pairs cycle births and '
         'deaths across scales, while Robins et al. (2016, DOI 10.1002/2015WR017937) relate '
         'micro-CT persistence in bead, sand, and rock scans to percolating sphere radii.'}

META_3D = ('Vietoris–Rips Filtration & Betti Persistence Landscape',
 'X: Filtration Scale ε (nm) · Z: Cycle Homology Class · Y: Persistence Lifetime (d_i − b_i)')

ES_TRANSLATION = {'title_es': 'Homología Persistente, Filtraciones Simpliciales de Vietoris–Rips, Códigos de '
             'Barras de Betti y Umbrales Topológicos de Percolación en Medios Desordenados',
 'subtitle_es': 'Sintetizando los Folios E.01, P.03 y M.05: un modelo explicativo—no un método '
                'de diseño estructural, hidrológico ni clínico—sobre cómo la homología '
                'persistente empareja nacimientos y cierres de ciclos a través de las escalas. '
                'Las lecturas numéricas son texto ilustrativo fijo.',
 'why_es': 'El deshielo lento en una cuenca separa pronto las pozas someras de los pasos '
           'profundos entre valles. Dónde termina la analogía: el agua barre una sola altura '
           'en una superficie bidimensional, mientras una filtración tridimensional construye '
           'símplices por distancias y puede encerrar cavidades sin equivalente en un terreno.',
 'plain_es': 'Sostengan ustedes una esponja de cocina seca frente a una lámpara de escritorio. '
             '¿Puede cruzar el agua de un lado al otro? Bajo aumento fuerte aparecen huecos '
             'diminutos, cuellos estrechos y conductos amplios entrelazados. Medir esas '
             'aberturas con una sola regla fija falla si las lecturas del escáner traen '
             'pequeños desvíos de posición. La homología persistente hace crecer paso a paso '
             'una esfera alrededor de cada punto muestreado. Las muescas superficiales se '
             'llenan rápido y dejan barras cortas en la gráfica. Los conductos amplios siguen '
             'abiertos durante muchos pasos y destacan como barras horizontales más largas '
             'junto al ruido corto. Esos resúmenes ayudan a estudiar escalas de poro en '
             'tomografías tridimensionales de arena, esferas empacadas y roca. La carga '
             'eléctrica y la adhesión química también podrían frenar partículas en geles '
             'húmedos. Aquí cada cifra es texto ilustrativo fijo, no una guía estructural ni '
             'clínica.',
 'deep_es': 'Edelsbrunner, Letscher y Zomorodian (2002, DOI 10.1007/s00454-002-2885-2) '
            'formularon la persistencia sobre filtraciones alfa tridimensionales mediante '
            'reducción módulo dos, mientras Carlsson (2009, DOI 10.1090/S0273-0979-09-01249-X) '
            'y Ripser (Bauer 2021, DOI 10.1007/s41468-021-00071-5) indexan cliques de '
            'Vietoris–Rips por diámetro t = 2ε. En la Lámina M.10-A, el 2-esqueleto bandera '
            'abstracto de siete vértices (|V| = 7, |E| = 10, |F| = 1) produce β_0 = 1, '
            'β_1 = 3, β_2 = 0, χ = −2 y la barra ilustrativa fija [38, 116] nm. '
            'Cohen-Steiner, Edelsbrunner y Harer (2007, DOI 10.1007/s00454-006-1276-5) acotan '
            'd_B(D(f), D(g)) ≤ ||f − g||_∞ para funciones continuas dóciles en unidades '
            'compatibles (σ = 0.08 aquí es un control adimensional). En el navegador no corre '
            'ningún reductor matricial: los deslizadores actualizan etiquetas, superposición y '
            'vista 3D, mientras el boceto, las barras y las cuatro tarjetas quedan fijos.',
 'bridge_es': 'Nota conceptual, no un resultado: Button et al. (2012, DOI '
              '10.1126/science.1223012) propusieron el modelo de gel sobre cepillo periciliar '
              'en la vía aérea, y Robins et al. (2016, DOI 10.1002/2015WR017937) relacionaron '
              'persistencia en micro-CT de esferas, arena y roca con radios de percolación. '
              'Explorar resúmenes similares en geles biológicos es una pregunta no probada y '
              'la carga o unión química podría frenar partículas; no se analizaron muestras de '
              'pacientes ni nada aquí es consejo médico o de diseño.'}
