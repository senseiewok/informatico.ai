#!/usr/bin/env python3
"""Folio E.01 (ENGINEERING): Stokes–Brinkman Porous Continuum, Helmholtz–Hodge Decomposition, and Percolation."""
from __future__ import annotations

SLUG = 'e01'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.01',
 'slug': 'e01',
 'pillar': 'engineering',
 'category_code': 'E',
 'title': 'Stokes–Brinkman Porous Continuum, Helmholtz–Hodge Decomposition, and Percolation',
 'subtitle': 'How viscous shear and Darcy drag balance over the Brinkman screening length √κ '
             'across porous limestone, capillary-active mortars, and consolidated geotechnical '
             'strata.',
 'date_published': '2026-10-22',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.4',
 'status_badge': 'CIVIL & CONTINUUM · REV 1.4',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'μ ∇²u − (μ/κ)u = ∇p · φ_c = 0.5927 · u = −∇Φ + ∇×Ψ',
 'colophon': {'identifier': 'E.01 · Brinkman & Percolation · CSI 03 30 00 / 07 16 00',
              'kernels': 'μ ∇²u − (μ/κ)u = ∇p · Discrete Helmholtz-Hodge',
              'benchmarks': 'Model values: φ_c = 0.5927 (square-lattice site threshold) · √κ = 13.09 nm at defaults',
              'bridge': 'Porous Stone & Mortar ↔ Capillary Pore Network Percolation'},
 'sliders': [{'label': 'Void Porosity Fraction (φ vs φ_c = 0.5927)',
              'min': 0.45,
              'max': 0.92,
              'step': 0.005,
              'value': 0.72,
              'unit': 'φ = '},
             {'label': 'Capillary / Pore Throat Radius Scale (a_f)',
              'min': 4.0,
              'max': 25.0,
              'step': 0.5,
              'value': 12.0,
              'unit': 'a_f = '}],
 'steps': ['Stage 1 (Supercritical Open Matrix, φ = 0.72): In the lattice model, connected pore '
           'channels span the domain; with a_f = 12 nm the Brinkman screening length is √κ = '
           'a_f φ^(3/2) / (2(1 − φ)) = 13.09 nm.',
           'Stage 2 (Critical Percolation Backbone, φ → 0.5927): Tortuous dead-end branches '
           'multiply; transport restricts to a fractal spanning cluster. The value 0.5927 is the '
           'site-percolation threshold of the two-dimensional square lattice, used here as the '
           "model's threshold.",
           'Stage 3 (Subcritical Arrest, φ < 0.5927): In the lattice model the open sites no '
           'longer connect across the domain, so its macroscopic conductivity is zero. Real '
           'three-dimensional pore networks stay connected at much lower porosity.',
           'Stage 4 (Discrete Helmholtz-Hodge Decomposition): Separates velocity into curl-free '
           'pressure drive (−∇Φ) and divergence-free pore eddies (∇×Ψ).'],
 'readouts': [{'label': 'Brinkman Screening (√κ)', 'value': '13.09 nm'},
              {'label': 'Effective Conductivity', 'value': '0.220 D_0'},
              {'label': 'Percolation Phase Regime', 'value': 'SUPERCRITICAL (φ > 0.5927, model)'},
              {'label': 'Helmholtz-Hodge Split', 'value': 'ORTHOGONAL BY DEFINITION · not computed here'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 03 30 00 / 07 16 00',
                'title': 'Capillary-Active Mineral Lime Mortar & Breathable Silicate Coating',
                'body': 'Illustrative design sketch, not a tested product: a mortar and coating '
                        'with an open, connected pore structure, intended to dry by capillary '
                        'transport and so reduce the risk of salt-crystallization damage in '
                        'masonry. The values φ = 0.68 and μ-value ≤ 8 are design targets chosen '
                        "to sit above this page's model threshold; they were not measured.",
                'meta': 'Design sketch · a hygrothermal simulation to EN 15026 would be the next '
                        'step; none was run'},
 'sidenote_1': {'kicker': 'SIDENOTE E.01-A · AN ANALOGY FROM BIOLOGY',
                'body': 'Airway mucus is also a porous network: a mesh of mucin polymers with '
                        'water-filled gaps. Whether a small particle can cross such a gel '
                        'depends, as in stone, on the size of the gaps and on whether they '
                        'connect. That resemblance is an analogy offered by this folio. The '
                        'lattice threshold on this page was not measured in mucus, and nothing '
                        'here is a statement about any treatment.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.01-B · SPECIFICATION PLATE · CSI 03 30 00 / 07 16 00',
                'body': 'Design sketch of a capillary-active mineral lime mortar and breathable '
                        'silicate coating (design targets φ = 0.68, μ ≤ 8). Real lime mortars '
                        'usually have total porosities well below 0.5; the high value follows '
                        "from the page's two-dimensional lattice model, not from a mix design."},
 'skill': {'filename': 'porous-brinkman-percolation-SKILL.md',
           'name': 'porous-brinkman-percolation',
           'description': 'AI-agnostic continuum and porous-media engineering skill for '
                          'Darcy-Brinkman momentum screening, Helmholtz-Hodge decomposition, and '
                          'continuum percolation (phi_c = 0.5927).',
           'rules': ['Brinkman Screening Length: sqrt(kappa) = a_f * phi^(3/2) / (2 * (1 - phi)) '
                     'from mu * nabla^2(u) - (mu/kappa)*u = nabla(p).',
                     'Lattice Percolation Threshold (model): compare porosity phi with phi_c = '
                     '0.5927, the site threshold of the 2D square lattice; the model scales '
                     'effective diffusivity as ((phi - phi_c) / (1 - phi_c))^1.30. State that '
                     'this is a lattice idealization; a real material needs its own measured '
                     'threshold.',
                     'Discrete Helmholtz-Hodge Decomposition: Separate face-centered flux into '
                     'L2-orthogonal curl-free potential gradient and divergence-free '
                     'recirculation.']},
 'revisions': [{'edition': 'REV 1.4',
                'date': '2026-11-14',
                'summary': 'REV 1.4 (Redated 2026-11-14): Grounding revision. A chronology entry '
                           'that credited a 2009 work to Brinkman and Bear was removed: the DOI '
                           'it carried (10.1007/BF02120313) is Brinkman\'s own 1949 paper. A claim '
                           'that optimal-transport software had shown a result about '
                           'percolation was withdrawn, as were the unsourced figures about Cystic '
                           'Fibrosis sputum and inhaled nanoparticles; the mucus link is now '
                           'stated as an analogy. The threshold 0.5927 is identified as the '
                           'square-lattice site value, and the walkthrough numbers were '
                           'recomputed from the stated formula (8.73 nm and 19.64 nm).',
                'opus': 'Review: every DOI in the folio was checked in Crossref and the Scite '
                        'index on 2026-11-14, and the repository names with the GitHub API. No '
                        'simulation was run for this folio; the numbers are outputs of the '
                        'closed-form model on the page.'},
               {'edition': 'REV 1.3',
                'date': '2026-11-02',
                'summary': 'REV 1.3 (Redated 2026-11-02): Verified Stokes-Brinkman porous '
                           'continuum (sqrt(kappa)), discrete Helmholtz-Hodge decomposition, and '
                           'Broadbent-Hammersley percolation (phi_c = 0.5927, CSI 03 30 00 / 07 16 '
                           '00) with multi-model peer review.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): checked that '
                        'sqrt(kappa) = 13.09 nm follows from the page formula. The word '
                        '"Verified" in this note and in the notes below, and the claim of '
                        'parity with CSI specifications, are withdrawn in REV 1.4: CSI section '
                        'numbers classify work and contain no such values.'},
               {'edition': 'REV 1.2',
                'date': '2026-11-01',
                'summary': 'REV 1.2 (Redated 2026-11-01): Coupled civil capillary-active mineral '
                           'lime mortar physics to capillary pore network percolation in mineral '
                           'lime mortars and porous stone.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        '√κ = 13.09 nm static and dynamic parity.'},
               {'edition': 'REV 1.1',
                'date': '2026-10-28',
                'summary': 'REV 1.1 (Redated 2026-10-28): Added discrete Helmholtz-Hodge flux '
                           'decomposition.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified L2 '
                        'orthogonality on finite-volume cell faces.'},
               {'edition': 'REV 1.0',
                'date': '2026-10-22',
                'summary': 'REV 1.0 (Published 2026-10-22): Initial Darcy-Brinkman momentum '
                           'balance monograph.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'subcritical arrest below φ_c = 0.5927.'}],
 'volume': 1,
 'volume_code': 'VOL. 01',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1007/BF02120313',
           'fetched_on': '2026-11-08',
           'citing_publications': 3126,
           'supporting': 18,
           'mentioning': 1456,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Brinkman 1949 (DOI 10.1007/BF02120313), as recorded '
                      '2026-11-08: 3,126 citing publications (18 supporting, 1,456 mentioning, '
                      '0 contrasting) and no retraction notice. These counts describe that one '
                      'paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1007/BF02120313',
           'fetched_on': '2026-11-08',
           'citing_publications': 3126,
           'supporting': 18,
           'mentioning': 1456,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Brinkman 1949 (DOI 10.1007/BF02120313), as recorded '
                      '2026-11-08: 3,126 citing publications (18 supporting, 1,456 mentioning, '
                      '0 contrasting) and no retraction notice. These counts describe that one '
                      'paper, not this folio.'},
 'act1_title': 'Act I — From the Fountains of Dijon to the Nanoporous Gels of the Human Lung',
 'act1_dropcap': 'In 1856 the French engineer Henry Darcy published Les Fontaines Publiques de la Ville de Dijon, his report on the public water supply of Dijon. An appendix describes experiments with vertical columns of sand, from which he concluded that the flow of water through the bed is proportional to the loss of head across it and inversely proportional to its thickness. That rule is now called Darcy\'s law. Almost a century later Hendrik Brinkman added a viscous shear term to Darcy\'s drag, so that one equation could describe both open channels and a dense swarm of particles (DOI 10.1007/BF02120313; the journal volume is often cited as 1947, and Crossref dates the paper 1949). In 1957 Simon Broadbent and John Hammersley introduced percolation processes (DOI 10.1017/S0305004100032680): a way to ask whether the open paths through a random medium connect from one side to the other. On a lattice the answer changes abruptly at a critical fraction of open sites.',
 'act1_plain_bridge': 'Think of how water seeps through a kitchen sponge, a sandy garden bed, or '
                      'an antique limestone brick after heavy rain. If the holes inside the '
                      'material are wide and connect to one another, water glides through without '
                      'much trouble. But if you pack the grains tighter and tighter, something '
                      'surprising happens. The water does not just slow down a little bit. Once '
                      'the open space drops below a specific tipping point, the open pathways '
                      'vanish completely. Pores that once formed a continuous highway turn into '
                      'isolated pockets and dead ends. Moisture gets trapped, and movement grinds '
                      'to an absolute halt. Engineers care about this transition because it '
                      'decides whether protective sealants breathe, whether historic stone walls '
                      'survive freezing winters without crumbling, and whether water filters catch '
                      'contaminants or choke under pressure. By understanding how fluid clings to '
                      'microscopic surfaces while trying to squeeze through tiny gaps, we can '
                      'design porous materials that let good things pass while keeping damage out.',
 'act1_body': 'Together these three ideas underlie much of the modelling of fluid transport in disordered porous media. The same continuum mathematics is used in groundwater hydrology, membrane design, battery separators and breathable restoration mortars for historic masonry. This page joins Brinkman\'s viscous screening equation to a Carman–Kozeny-type permeability, k(phi) = d_f^2 phi^3 / [16 c_K (1 - phi)^2], with the Kozeny constant c_K set to 1 and d_f = 2 a_f, which gives sqrt(k) = a_f phi^(3/2) / (2 (1 - phi)). That choice of constant is the folio\'s simplification. When pore diameters approach the scale of the moving particles, Darcy drag by itself cannot describe the shearing layers that develop near the solid walls; the Brinkman term does, over the length delta_B = sqrt(mu_eff k / mu). A reader who wants velocity profiles in a real geometry could discretize the mixed velocity-pressure Darcy–Brinkman form with an open-source finite-element library such as FEniCS/dolfinx (Scroggs et al. 2022, DOI 10.1145/3524456, describes part of its element machinery). No such simulation was run for this folio.',
 'act1_stakes': 'Why this matters in buildings and ground: water that cannot leave a porous wall stays there. In masonry, trapped moisture that freezes, or that carries salts which crystallize as it dries, can generate pressures larger than the tensile strength of stone and mortar, and the surface spalls. In drainage layers and filters, fine sediment that settles into the pores narrows and disconnects the flow paths, and a layer that was meant to drain can begin to hold water back. Both problems come down to the two questions this folio studies: how much drag do the pore walls exert, and do the pores still connect? The model on this page is a teaching idealization of those questions. It is not a substitute for measured permeability or for a hygrothermal assessment of a real wall.',
 'pullquote': '"In the lattice model on this page, below the critical open fraction phi_c = 0.5927 the network does not merely slow '
              'a diffusing particle down: every open path it can reach is a finite cul-de-sac."',
 'chronology': [('1856',
                 'Henry Darcy publishes Les Fontaines Publiques de la Ville de Dijon, with the '
                 'sand-column experiments behind what is now called Darcy\'s law.'),
                ('1947–1949',
                 'Hendrik Brinkman adds a viscous shear term to Darcy drag, giving the '
                 'screening length sqrt(kappa) (DOI 10.1007/BF02120313; volume often cited as '
                 '1947, Crossref date 1949).'),
                ('1957',
                 'Simon Broadbent & John Hammersley introduce percolation processes (DOI '
                 '10.1017/S0305004100032680).')],
 'act2_title': 'Act II — How It Actually Works: Viscous Screening vs. Topological Trapping',
 'act2_analogy': 'Imagine trying to bicycle across a dense, untamed forest. Brinkman screening '
                 'represents the drag of the underbrush and tree branches whipping against your '
                 'pedals, slowing you down with viscous friction even when open air exists between '
                 'the trunks. Percolation represents whether a continuous dirt trail actually '
                 'connects one side of the woods to the other. Even if you have the stamina to '
                 'overcome the thickest branch friction, you remain trapped if fallen logs seal '
                 'off the last open gap, forcing you into a dead end.',
 'act2_plain_primer': 'Before looking at any technical symbols, picture the two controls in our '
                      'interactive model as two physical dials on a forest trail. The first dial '
                      'is the Void Porosity Fraction, which controls how much open space exists '
                      'between the obstacles. If you turn this dial down, you are packing more '
                      'trees and debris into the woods. Above a specific threshold, enough clear '
                      'pathways link together to let you cross from one side to the other. Slip '
                      'below that threshold, and the spanning trail suddenly breaks into '
                      'disconnected islands. The second dial is the Capillary Throat Radius, which '
                      'controls the width of the gaps between the obstacles. Widening these '
                      'openings gives you more breathing room, which pushes back the friction from '
                      'surrounding branches and lets fluids glide freely through the center. '
                      'Turning both dials together shows how open space and gap width team up: you '
                      'need enough connected trails to pass through, and wide enough openings so '
                      'friction does not choke the flow.',
 'distill_diagram': {'analogy_title': 'The Forest Trail & Underbrush Drag',
                     'analogy_sub': 'Friction slows motion while trail connectivity dictates '
                                    'passage.',
                     'force_a_title': 'Void Fraction (φ vs φ_c)',
                     'force_a_sub': 'Controls total open volume and spanning trail connectivity.',
                     'force_b_title': 'Pore Throat Radius (a_f)',
                     'force_b_sub': 'Determines viscous boundary-layer screening distance √κ.',
                     'threshold_title': 'Percolation Threshold (φ_c = 0.5927)',
                     'threshold_pass': 'Supercritical: Connected pore channels span entire matrix.',
                     'threshold_fail': 'Subcritical: Pathways pinch off into isolated dead ends.'},
 'act2_intuition': 'Two independent physical barriers govern whether a fluid or suspended particle '
                   'can traverse a porous medium. The first barrier is hydrodynamic drag: solid '
                   'matrix fibers of radius a_f exert viscous shear on moving fluid over the '
                   'Brinkman screening distance sqrt(kappa). This length scale defines the '
                   'boundary zone where fluid transitions from creeping Darcy seepage to free '
                   'Stokes flow. The second barrier is geometric topology. This page models it '
                   'with site percolation on a two-dimensional square lattice, whose threshold is '
                   'phi_c = 0.5927: below that open fraction no path crosses the lattice, and '
                   'just above it the conductivity grows as (phi - phi_c)^1.30, the '
                   'two-dimensional conductivity exponent. The lattice is a stand-in. '
                   'Three-dimensional networks have lower thresholds (0.3116 for site '
                   'percolation on the simple cubic lattice), and a real stone or mortar has '
                   'its own, which must be measured. The laboratory multiplies the two effects: '
                   'it reports the Brinkman length from the formula above and an effective '
                   'conductivity D_eff / D_0 = ((phi - phi_c) / (1 - phi_c))^1.30. A '
                   'Helmholtz–Hodge decomposition, which splits a velocity field into a '
                   'curl-free part driven by pressure and a divergence-free part that '
                   'recirculates, is described here as a tool for reading such flows; the page '
                   'does not compute one.',
 'act2_deepening': 'At the microscopic scale, the interaction between the void fraction and the '
                   'pore throat radius creates a strongly nonlinear transport regime. As porosity '
                   'approaches the percolation threshold from above, the geometry of the flow '
                   'field undergoes dramatic restructuring. Rather than distributing evenly across '
                   'all available pores, streamlines concentrate into a tenuous fractal backbone '
                   'while dead-end pores hold stagnant fluid. Within the conducting channels, the '
                   'Brinkman screening length dictates how deeply shear stresses penetrate from '
                   'pore walls into the core fluid stream. When the throat radius is small '
                   'relative to the screening length, viscous boundary layers from opposite walls '
                   'overlap, creating an elevated apparent viscosity that severely restricts '
                   'throughput. Conversely, widening the pore throat pushes the screening zone '
                   'toward the perimeter, forming a low-resistance central core where '
                   'convective velocity surges. Discrete Helmholtz–Hodge decomposition separates '
                   'this coupled field into curl-free potential flow driven by macroscale pressure '
                   'gradients and divergence-free rotational eddies trapped within pore crevices, '
                   'which shows how local micro-geometry shapes drainage as a whole.',
 'walkthrough': ['Experiment 1 (Crossing the Model Threshold): Drag Void Porosity phi '
                 'from 0.720 down to 0.540. The effective conductivity falls from 0.220 D_0 to '
                 'zero as phi passes the lattice threshold phi_c = 0.593.',
                 'Experiment 2 (Throat Radius): Increase the radius scale a_f from 8 nm to 18 nm at '
                 'constant porosity phi = 0.72 and observe the Brinkman screening length '
                 'sqrt(kappa) widen from 8.73 nm to 19.64 nm, in proportion to a_f.',
                 'Experiment 3 (Equation-to-Diagram Chip): Hover over the Brinkman Screening chip '
                 'to highlight the exponential velocity boundary layer in the SVG plate.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification '
               'Bridge',
 'act4_human_ai': 'What follows is a proposal, not a report of work done. A closed-form check like the one on this page could sit inside a design loop: a person or a model proposes a pore structure, and the Brinkman length and a connectivity test screen it before any expensive simulation. The tools named here are ones a reader could use. FEniCS/dolfinx (https://github.com/FEniCS/dolfinx, DOI 10.1145/3524456) can solve the Darcy–Brinkman equations on a scanned pore geometry, and PySR (Cranmer 2023, DOI 10.48550/arXiv.2305.01582) can search for compact formulas that fit the results. This folio ran neither. Citation counts shown on the page come from the Scite index (DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'The paragraph below describes a possible future workflow, not current practice. One frontier of porous media engineering could be closed-loop '
                   'co-design where human engineers and artificial intelligence algorithms '
                   'collaborate on microstructural topology. Using micro-computed tomography scans '
                   'of natural limestones and pozzolanic mortars, neural networks propose '
                   'synthetic pore networks optimized for tailored hydraulic conductivity and '
                   'chemical durability. High-performance finite-element solvers then subject '
                   'these candidate geometries to rigorous Stokes–Brinkman continuum verification, '
                   'ensuring that candidate microstructures maintain void fractions comfortably '
                   'above the percolation threshold while maximizing mechanical compressive '
                   'strength. Human engineers set the boundary constraints, specifying maximum '
                   'allowable hygroscopic expansion, target vapor permeability, and freeze-thaw '
                   'durability indices for specific climatic zones. Open research questions focus '
                   'on how dynamic crack propagation during seismic or thermal loading alters the '
                   'percolation threshold over decadal timescales. By continuously fusing physical '
                   'sensor data from restoring structures with physics-informed surrogate models, '
                   'engineering teams can forecast progressive pore clogging and schedule targeted '
                   'breathable consolidation treatments before irreversible structural spalling '
                   'begins.',
 'cf_bridge': 'An analogy, not a clinical statement: airway mucus is a hydrated polymer mesh, and in Cystic Fibrosis it is more concentrated than in health. Whether a particle can move through any mesh depends on the two things this folio models in stone, the size of the gaps and whether they connect. The lattice threshold phi_c = 0.5927 and the nanometre values on this page are model values; none was measured in mucus, and this folio makes no claim about any inhaled therapy or about care.',
 'sources': ['Darcy, H. (1856). Les Fontaines Publiques de la Ville de Dijon. Victor Dalmont, '
             'Paris.',
             'Broadbent, S. R., & Hammersley, J. M. (1957). Percolation processes: I. Crystals and '
             'mazes. Mathematical Proceedings of the Cambridge Philosophical Society, 53(3), '
             '629–641. DOI: 10.1017/S0305004100032680.',
             'Brinkman, H. C. (1949). A calculation of the viscous force exerted by a flowing '
             'fluid on a dense swarm of particles. Applied Scientific Research, 1(1), 27–34 '
             '(volume often cited as 1947). DOI: 10.1007/BF02120313.',
             'Cranmer, M. (2023). Interpretable Machine Learning for Science with PySR and '
             'SymbolicRegression.jl. arXiv:2305.01582. DOI: 10.48550/arXiv.2305.01582.',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). ACM Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: 10.1145/3524456.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.']}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what Darcy-Brinkman porous percolation streamlines '
        'through mineral lime mortar pore throats would look like (artistic impression, not a '
        'measured structure)',
 'caption': 'Conceptual Vision Plate E.01-V (Imagining What It Would Look Like) · Artistic macro '
            'visualization imagining Stokes-Brinkman fluid streamlines weaving through percolating '
            'crystalline pore throats (phi > phi_c = 0.5927) in a pozzolanic mineral mortar '
            'matrix.'}

DISPATCH = {'kicker': 'DISPATCH · POROUS MEDIA: DRAG AND CONNECTIVITY',
 'headline': 'Two Questions for Any Porous Material: How Much Drag, and Do the Pores Connect?',
 'body': 'This folio joins Darcy (1856), Brinkman (1949, DOI 10.1007/BF02120313) and the '
         'percolation processes of Broadbent & Hammersley (1957, DOI 10.1017/S0305004100032680) '
         'in one small model. Its threshold φ_c = 0.5927 is the site value for a square lattice, '
         'an idealization: the page does not show that any real mortar, stone or gel has that '
         'threshold.'}

META_3D = ('Darcy–Brinkman Percolation Throat Lattice',
 'X: Pore Throat Coordinate · Z: Transverse Span · Y: Hydraulic Potential & Percolation Saddle')

ES_TRANSLATION = {'title_es': 'Continuo Poroso de Stokes–Brinkman, Descomposición de Helmholtz–Hodge y Percolación',
 'subtitle_es': 'Cómo se equilibran el esfuerzo cortante viscoso y el arrastre de Darcy sobre la '
                'longitud de apantallamiento de Brinkman √κ en caliza porosa, morteros capilares y '
                'estratos geotécnicos consolidados.',
 'why_es': 'Imagina pedalear en bicicleta a través de un bosque: el apantallamiento de Brinkman es '
           'la resistencia combinada del aire y las ramas que rozas, mientras que la percolación '
           'determina si existe un sendero continuo para cruzar de un extremo a otro.',
 'bridge_es': 'Una analogía, no una afirmación clínica: el moco de las vías respiratorias es una malla de polímeros hidratada, y en la Fibrosis Quística está más concentrado. Que una partícula pueda atravesar una malla depende del tamaño de los huecos y de que estén conectados, las mismas dos preguntas que este folio modela en piedra. Los valores de la página son del modelo; ninguno se midió en moco y el folio no afirma nada sobre terapias ni cuidados.',
 'plain_es': 'En 1856, el ingeniero francés Henry Darcy publicó su informe sobre las fuentes '
             'públicas de la ciudad de Dijon. '
             'Al medir el paso del agua a través de columnas de arena, concluyó que el '
             'caudal es proporcional a la pérdida de carga e inversamente proporcional al espesor '
             'de la capa de arena. Para entenderlo de manera sencilla en nuestra vida diaria, piensen en '
             'cómo se mueve el agua dentro de una esponja de cocina o en un ladrillo de barro '
             'después de una lluvia intensa. Si los poros microscópicos están conectados entre sí, '
             'el líquido avanza con libertad. No obstante, cuando el espacio vacío disminuye y '
             'cruza un límite crítico, los caminos continuos se rompen por completo y el agua '
             'queda atrapada en rincones aislados. Este fenómeno, conocido como percolación, '
             'explica por qué algunos materiales de construcción respiran adecuadamente mientras '
             'que otros acumulan humedad y se fracturan durante el invierno.',
 'deep_es': 'El transporte en medios porosos se rige por la competencia entre dos fenómenos '
            'físicos fundamentales: el arrastre viscoso de Brinkman sobre las paredes sólidas y la '
            'conectividad geométrica del espacio poroso. La longitud de apantallamiento de '
            'Brinkman define el espesor de la capa límite donde la fricción viscosa frena el '
            'fluido cerca de las fibras. Por otro lado, la fracción de vacíos determina si existe '
            'una red continua de transporte. En el modelo de esta página, una red cuadrada en dos '
            'dimensiones, cuando la fracción abierta desciende por debajo del umbral de '
            'percolación de 0.5927 la conductividad del modelo cae a cero, sin importar la presión '
            'que apliquemos. Los materiales reales, en tres dimensiones, siguen conectados con '
            'porosidades mucho menores, y su umbral debe medirse. Este balance puede calcularse '
            'con simulaciones de elementos finitos; para este folio no se corrió ninguna. '
            'Entender la transición ayuda a pensar por qué algunos muros secan bien y otros '
            'retienen humedad y sales. Los números de la página son resultados del modelo.'}
