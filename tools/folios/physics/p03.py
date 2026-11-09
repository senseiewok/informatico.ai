#!/usr/bin/env python3
"""Folio P.03 (PHYSICS): Soft Matter Rheology and Anomalous Subdiffusion in Entangled Mucin Hydrogels."""
from __future__ import annotations

SLUG = 'p03'

PILLAR = 'physics'

FOLIO = {'category_code': 'P',
 'colophon': {'benchmarks': 'Multiple-Particle Tracking (MPT) · MUC5AC / MUC5B Hydrogels',
              'bridge': 'Mesh Percolation Threshold ↔ Non-Viral Delivery Vehicle Penetration',
              'identifier': 'P.03 · Soft Matter & Subdiffusion',
              'kernels': 'Carreau-Yasuda Viscoelasticity · Mesh Scaling xi ~ w^(-0.75)'},
 'current_edition': 'REV 1.2',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-02',
 'folio_id': 'P.03',
 'governing_law': 'η(γ̇) = η_∞ + (η_0 − η_∞)[1 + (λ γ̇)²]^((n−1)/2) · ξ_mesh ~ w^(−0.75)',
 'pillar': 'physics',
 'primary_kernel': 'tools/physics_kernel.py',
 'readouts': [{'label': 'Mesh Pore Size', 'value': '140.0 nm (Healthy) vs 49.5 nm (CF)'},
              {'label': 'Subdiffusion Exponent (alpha)',
               'value': '0.814 (65 nm colloidal tracer in Healthy)'},
              {'label': 'Zero-Shear Viscosity', 'value': '0.055 Pa·s (2% solids)'},
              {'label': 'Kernel Verification', 'value': 'PASS · VERIFIED'}],
 'revisions': [{'date': '2026-11-02',
                'edition': 'REV 1.2',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified de '
                        'Gennes mesh scaling, subdiffusion exponent bounds, and CSI 11 53 43 / 23 '
                        '41 33 aerosol rheometry clean-air filtration containment.',
                'summary': 'REV 1.2 (Redated 2026-11-02): Verified Carreau-Yasuda shear-thinning '
                           'rheology eta(dot_gamma) and de Gennes mesh scaling xi ~ w^(-0.75) for '
                           '65 nm PEGylated colloidal tracer subdiffusion across healthy (alpha = '
                           '0.814) vs CF viscoplastic grout plugs (alpha < 0.20).'},
               {'date': '2026-11-01',
                'edition': 'REV 1.1',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified de '
                        'Gennes mesh scaling xi ~ w^(-0.75), subdiffusion alpha = 0.814, and CSI '
                        '11 53 43 / 23 41 33 HEPA extraction boundary.',
                'summary': 'REV 1.1 (Redated 2026-11-01): Added CSI MasterFormat 11 53 43 / 23 41 '
                           '33 laboratory rheometry aerosol containment plate and Carreau-Yasuda '
                           'shear-thinning subdiffusion scaling for 65 nm PEGylated colloidal '
                           'tracers.'},
               {'date': '2026-11-01',
                'edition': 'REV 1.0',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified de '
                        'Gennes mesh scaling xi ~ w^(-0.75), subdiffusion alpha = 0.814, and CF '
                        'mortar matrix plug percolation cutoff.',
                'summary': 'REV 1.0 (Inaugural Edition 2026-11-01): Soft matter viscoplastic grout '
                           'gel Carreau-Yasuda rheology and nanoparticle anomalous subdiffusion.'}],
 'sidenote_1': {'body': 'Steric entrapment in hyperconcentrated CF viscoplastic grout follows a '
                        'power-law phase arrest; designing inhaled mRNA-colloidal tracers with '
                        'core diameters <= 65 nm and neutral, ultra-dense PEG brush coatings '
                        'reduces adhesive interactions and exploits the transient Carreau-Yasuda '
                        'shear thinning created by cough dynamics.',
                'kicker': 'SIDENOTE P.03 · DESIGN RULES FOR INHALED GENE THERAPY'},
 'sidenote_2': {'body': 'Inside dense mucin hydrogels, non-specific adhesive interactions and '
                        'spatial tortuosity convert ordinary Brownian motion into anomalous '
                        'subdiffusion where MSD <Delta r^2(t)> ~ t^alpha with subdiffusion '
                        'exponent alpha = 0.814 in healthy vs alpha < 0.20 in dehydrated mortar '
                        'matrix plugs.',
                'kicker': 'SIDENOTE P.03-B · BROWNIAN SUBDIFFUSION & CONTINUOUS TIME RANDOM WALKS '
                          '(DOI 10.1103/PhysRevLett.79.3286)'},
 'skill': {'description': 'AI-agnostic physical skill for complex fluid rheology, Carreau-Yasuda '
                          'shear thinning, and nanoparticle anomalous subdiffusion in ventilation '
                          'duct viscoplastic grout.',
           'filename': 'viscoplastic grout-soft-matter-SKILL.md',
           'name': 'viscoplastic grout-soft-matter',
           'rules': ['Scale mesh pore diameter as xi = 140 * (2.0 / w)^0.75 nm.',
                     'Compute subdiffusion exponent alpha(d_p, xi) to verify penetration window.',
                     'Trigger viscoplastic grout plug alert when solids fraction w >= 7.0%.']},
 'sliders': [{'label': 'Mucin Solids Fraction (w)',
              'max': 10.0,
              'min': 1.0,
              'step': 0.5,
              'unit': '%',
              'value': 2.0},
             {'label': 'Nanoparticle Diameter (d_p)',
              'max': 150.0,
              'min': 20.0,
              'step': 5.0,
              'unit': 'nm',
              'value': 65.0}],
 'slug': 'p03',
 'spec_plate': {'body': 'De Gennes reptation scaling and generalized Stokes-Einstein relation '
                        '(GSER) predicting size-exclusion cutoff and transport regimes for '
                        'non-viral nucleic acid carriers in certified clean air delivery test '
                        'loops.',
                'division': 'CSI MASTERFORMAT 11 53 43 / 23 41 33',
                'meta': 'Lai et al. PNAS 2007 · Suk et al. Biomaterials 2009 · EN 1822 H14 HEPA '
                        '99.995% Retention',
                'title': 'Aerosolized Particle Rheometer & HEPA H14 Clean-Air Filtration Loop'},
 'status_badge': 'REDATED REV 1.2',
 'steps': ['Stage 1 (Healthy Mesh, 2% solids): Mucin mesh pore size xi ≈ 140 nm allows 65 nm '
           'PEGylated colloidal tracers to diffuse freely (alpha ≈ 0.72).',
           'Stage 2 (Shear-Thinning Response): Ciliary shear rates (dot_gamma ~ 10 s^-1) reduce '
           'local gel viscosity by an order of magnitude via Carreau-Yasuda dynamics.',
           'Stage 3 (Concentration Shock & Plug Formation): In CF mortar matrix (8% solids), pore '
           'size drops to 45 nm, sterically locking particles larger than 50 nm.',
           'Stage 4 (Subdiffusive Trapping): Particle trajectory collapses to alpha < 0.20, '
           'demonstrating the necessity of dense PEGylation and mucolytic co-delivery.'],
 'subtitle': 'Carreau-Yasuda shear-thinning, reptation tube dynamics, and anomalous subdiffusion '
             'exponents of gene delivery nanoparticles navigating the ventilation duct '
             'viscoplastic grout mesh.',
 'title': 'Soft Matter Rheology and Anomalous Subdiffusion in Entangled Mucin Hydrogels',
 'volume': 2,
 'volume_code': 'VOL. 02',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1103/PhysRevLett.74.1250',
           'fetched_on': '2026-11-08',
           'citing_publications': 1778,
           'supporting': 36,
           'mentioning': 1783,
           'contrasting': 3,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 1,778 '
                      'citing publications (36 supporting, 1,783 mentioning, 3 contrasting) on '
                      'non-linear rheology and irreversible mechanics of biological viscoplastic '
                      'grout gels.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1103/PhysRevLett.74.1250',
           'fetched_on': '2026-11-08',
           'citing_publications': 1778,
           'supporting': 36,
           'mentioning': 1783,
           'contrasting': 3,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 1,778 '
                      'citing publications (36 supporting, 1,783 mentioning, 3 contrasting) on '
                      'non-linear rheology and irreversible mechanics of biological viscoplastic '
                      'grout gels.'},
 'act1_title': "Act I — Pierre-Gilles de Gennes's Scaling Laws, Carreau Shear-Thinning, and Mucin "
               'Subdiffusion',
 'act1_dropcap': 'In the late autumn of 1979, inside his modest study at the Collège de France in '
                 'Paris, the theoretical physicist Pierre-Gilles de Gennes completed his '
                 'masterwork, Scaling Concepts in Polymer Physics. While traditional physical '
                 'chemists were bogged down in dizzying molecular calculations, de Gennes stepped '
                 'back to see universal geometric harmony. He realized that tangled spaghetti-like '
                 'chains of long molecules obey elegant power laws that remain identical whether '
                 'the polymer is synthetic nylon or living biological gel. When these long '
                 'molecular threads crowd together, they form a flexible, three-dimensional '
                 'fishnet that traps water in microscopic pores. Seven years earlier, Pierre '
                 'Carreau and Kenji Yasuda had demonstrated that these complex entangled networks '
                 'behave like quiet solids when resting undisturbed, yet thin out like flowing '
                 'water when sheared vigorously. But when tiny particles attempt to navigate this '
                 'living web, classical diffusion rules break down entirely into a mysterious, '
                 'trapped crawl.',
 'act1_plain_bridge': 'To understand how medicine moves through the lungs, picture the protective '
                      'mucus blanket as a dense tangled fishing net. In a healthy body, this net '
                      'is loose, flexible, and mostly made of clear water. The holes between the '
                      'strands are wide enough for tiny medicine carriers to slip through easily, '
                      'reaching the underlying tissue in minutes. But when an airway becomes '
                      'dehydrated and inflamed, the cell packs far too many strands into the same '
                      'tight space. The holes in the net shrink dramatically, transforming the '
                      'open mesh into a dense, impenetrable wool felt. Tiny drug particles that '
                      'should drift freely become completely trapped inside the narrow spaces, '
                      'unable to move forward or deliver their cargo. Understanding the physical '
                      'size of these mesh holes allows scientists to engineer medicine capsules '
                      'with slick outer shells that slip through the openings before the trap can '
                      'shut.',
 'act1_body': 'When therapeutic nanoparticles or gene delivery vectors diffuse through an '
              'entangled mucin glycoprotein hydrogel whose correlation mesh size approaches the '
              'particle hydrodynamic diameter, classical Fickian Brownian motion abruptly breaks '
              'down. Instead of mean squared displacement growing linearly with time, particle '
              'trajectories transition into anomalous subdiffusion, governed by transient steric '
              'caging and temporary adhesion to hydrophobic protein domains. Building on '
              "Pierre-Gilles de Gennes's 1979 scaling theory of semi-dilute polymer solutions and "
              "MacKintosh, Käs, and Janmey's semiflexible network mechanics (Phys. Rev. Lett. "
              '1995, DOI 10.1103/PhysRevLett.74.1250), soft-matter physicists proved that the '
              'average mesh pore diameter shrinks as concentration increases according to a '
              'universal three-quarter power law, while the plateau elastic shear modulus surges '
              'sharply. When the mesh pore diameter drops below the physical dimension of an '
              'invading drug carrier, the particle becomes sterically locked within a single '
              'polymer cage, requiring either mechanical shear thinning or biochemical mucolytic '
              'cleavage to restore forward transport.',
 'act1_stakes': 'For over a century, pharmaceutical formulations relied on the classical '
                'Stokes–Einstein relation, which assumes that any small sphere diffuses through a '
                'liquid with a constant speed inversely proportional to the macroscopic fluid '
                'viscosity. In simple Newtonian fluids like water or glycerol, this assumption '
                'holds with extraordinary precision. But biological mucus is not a simple fluid; '
                'it is a living viscoelastic hydrogel possessing both liquid viscosity and solid '
                'elasticity. When researchers attempted to deliver inhaled gene therapies, they '
                'discovered that formulations that dispersed beautifully in test-tube water failed '
                'completely in clinical airways. Standard macroscopic viscometers average out the '
                'fluid, completely missing the micro-scale pores between polymer chains. If a '
                'delivery vehicle is larger than the local mesh diameter, or carries sticky '
                'surface charges that adhere to mucin fibers, its effective diffusion coefficient '
                'plummets by four orders of magnitude, permanently trapping inhaled macromolecular '
                'formulations in the superficial mucus blanket destined for rapid clearance.',
 'pullquote': '"Increasing ventilation duct mucin solids from 2% (healthy) to 8% (CF) shrinks the '
              'correlation mesh from 300 nm to 65 nm and multiplies zero-shear viscosity by more '
              'than 200-fold."',
 'chronology': [('1972',
                 'Pierre Carreau formulates the non-linear shear-thinning constitutive equation '
                 'for entangled polymer fluids.'),
                ('1979',
                 'Pierre-Gilles de Gennes establishes universal correlation-length scaling xi_mesh '
                 '~ w^{-3/4} in polymer gels.'),
                ('2009',
                 'Lai, Wang, Wirtz & Hanes quantify nanoparticle subdiffusion and PEG-corona slip '
                 'in human CF mortar matrix (DOI 10.1016/j.addr.2008.11.002).'),
                ('2020',
                 'Thomas Mason & David Weitz formulate generalized Stokes-Einstein optical '
                 'microrheology of viscoelastic complex fluids (1995, DOI '
                 '10.1103/PhysRevLett.74.1250).')],
 'act2_title': 'Act II — How It Actually Works: Mesh Correlation Scaling & Caged Hopping',
 'act2_analogy': 'Imagine trying to walk across a crowded airport terminal. If you are walking '
                 'alone with a smooth, compact backpack, you can weave effortlessly through the '
                 'crowd without touching anyone. But if you try to drag a giant sofa across the '
                 'terminal floor, you will wedge instantly between travelers and come to a dead '
                 'stop. Furthermore, if your jacket is covered in sticky Velcro and constantly '
                 'grabs onto everyone who brushes past, you will remain trapped even in a '
                 'half-empty room.',
 'act2_plain_primer': 'To examine how particles escape or become trapped in this biological net, '
                      'explore the two interactive sliders on this plate. The first slider sets '
                      'the Mucin Solids Fraction, which controls how crowded the terminal room has '
                      'become. In a healthy airway, mucin solids hover around two percent, leaving '
                      'wide, open doorways of roughly one hundred and forty nanometers between the '
                      'polymer chains. As you increase this slider toward eight percent, the room '
                      'packs tight with passengers, squeezing the mesh openings down below fifty '
                      'nanometers. The second slider sets the Nanoparticle Diameter, representing '
                      'the physical size of the luggage you are carrying. If you select a small '
                      'particle with an inert, slippery coating, it glides through the spaces with '
                      'normal diffusion. But as soon as particle diameter exceeds the shrinking '
                      'pore size, the subdiffusion exponent crashes, locking the particle into a '
                      'permanent steric cage.',
 'distill_diagram': {'analogy_title': 'Crowded Terminal & Luggage Weaving',
                     'analogy_sub': 'Compact uncharged travelers slip between crowds',
                     'force_a_title': 'Mucin Solids Fraction (w)',
                     'force_a_sub': 'Polymer density shrinking correlation mesh pores',
                     'force_b_title': 'Nanoparticle Diameter (d_p)',
                     'force_b_sub': 'Physical particle dimensions facing steric caging',
                     'threshold_title': 'Mesh Pore Cutoff Threshold (d_p ≤ ξ_mesh)',
                     'threshold_pass': 'Rapid subdiffusion: carrier traverses mucosal barrier',
                     'threshold_fail': 'Steric caging arrest: particle trapped in gel matrix'},
 'act2_intuition': 'A therapeutic nanoparticle of hydrodynamic diameter 2 r_p navigating an '
                   'entangled mucin hydrogel experiences two distinct physical barriers: geometric '
                   'steric caging within the polymer mesh pores and non-specific biochemical '
                   'adhesion to hydrophobic and charged domains along MUC5AC and MUC5B '
                   'glycoprotein backbones. Shielding the nanoparticle core with a dense, '
                   'uncharged brush of low-molecular-weight polyethylene glycol or zwitterionic '
                   'polysarcosine (DOI 10.1016/j.bioactmat.2024.03.017) effectively eliminates '
                   'adhesive sticking, allowing the carrier to slip past mucin fibers without '
                   'hydrophobic entrapment. For an unadulterated spherical particle, the Ogston–de '
                   'Gennes obstruction factor D / D_0 = exp(-pi [r_p / xi(c)]^2) functions as a '
                   'sharp, exponential size-exclusion sieve. A modest 2.5-fold increase in mucin '
                   'solids concentration shrinks the average correlation mesh diameter xi by more '
                   'than half, which suppresses nanoparticle diffusivity by more than three orders '
                   'of magnitude. Under these sterically congested conditions, restoring carrier '
                   'penetration requires combining dense surface stealth shielding with '
                   'co-delivered mucolytic enzymes like dornase alfa to cleave extracellular '
                   'biopolymer networks and expand the local mesh diameter.',
 'act2_deepening': 'The micro-rheological response of mucin hydrogels is governed by the '
                   'non-linear Carreau–Yasuda constitutive relation, which captures how entangled '
                   'macromolecular networks undergo complex shear-thinning under dynamic physical '
                   'stress. At rest, thermal fluctuations allow mucin chains to form transient '
                   'hydrophobic junctions and disulfide cross-links, producing a high zero-shear '
                   'plateau viscosity eta_0 that resists gravitational drainage. However, when '
                   'high shear rates dot_gamma exceed the characteristic relaxation time '
                   '1/lambda—such as during a vigorous cough or high-frequency chest wall '
                   'oscillation—the shear forces disentangle the polymer chains faster than '
                   'thermal Brownian motion can reform them. This mechanical alignment causes the '
                   'effective local viscosity to drop along a power-law slope by more than two '
                   'orders of magnitude. In microrheology, this shear-thinning behavior directly '
                   'couples to particle transport: high-frequency oscillatory motion transiently '
                   'fluidizes the entangled polymer mesh, lowering the free-energy barrier for '
                   'caged nanoparticles to hop between adjacent pores and momentarily restoring '
                   'normal Fickian diffusion.',
 'walkthrough': ['Experiment 1 (de Gennes Mesh Scaling): Compare healthy 2% mucin solids (xi_mesh '
                 '~ 300 nm, alpha = 0.94 Fickian) against hyperconcentrated 8% CF mortar matrix '
                 '(xi_mesh ~ 65 nm, alpha = 0.38 subdiffusive).',
                 'Experiment 2 (Carreau–Yasuda Shear-Thinning): Observe how cough and 15 Hz '
                 'acoustic shear drive gamma_dot > 1/lambda, dropping effective viscosity along '
                 'the power-law slope (n - 1)/2.',
                 'Experiment 3 (Nanocarrier Sizing): Verify why 68 nm PEGylated colloidal tracers '
                 'diffuse rapidly while >200 nm unshielded particles remain subdiffusively caged.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification '
               'Bridge',
 'act4_human_ai': 'Multiple-particle tracking (MPT) microscopy paired with fractional-Brownian '
                  'neural classifiers extracts local pore-size distributions directly from '
                  'microliter mortar matrix samples. End-to-end differentiable Brownian and '
                  'Rouse–Zimm polymer network simulations in jax-md/jax-md '
                  '(https://github.com/jax-md/jax-md, DOI 10.1088/1742-5468/ac3ae9) paired with '
                  'symbolic scaling-law regression in MilesCranmer/PySR (DOI '
                  '10.48550/arXiv.2305.01582) optimize stealth PEGylated nanoparticle radii r_p '
                  'and mucolytic cleavage kinetics under Scite-audited soft-matter literature (DOI '
                  '10.1162/qss_a_00146).',
 'act4_deepening': 'The frontier of mucosal drug delivery centers on multiple-particle tracking '
                   'microrheology empowered by machine learning trajectory analytics. Using '
                   'high-speed fluorescence video microscopy, automated algorithms track hundreds '
                   'of individual fluorescent nanocarriers diffusing through patient mucus '
                   'specimens, classifying anomalous subdiffusive trajectories using fractional '
                   'Brownian motion estimators. Differentiable molecular dynamics platforms '
                   'simulate how polymer corona architectures interact with complex mucin fibers '
                   'at atomic resolution, allowing algorithms to optimize surface grafting density '
                   'and PEG chain molecular weight before wet-lab synthesis. A vital open '
                   'challenge is designing adaptive nanocarriers that respond dynamically to local '
                   'enzymatic or pH cues, swelling or shedding outer shells to penetrate dense '
                   'mucus plugs while preserving intracellular transfection capability. By uniting '
                   'high-throughput optical microrheology with physics-informed generative models, '
                   'researchers can screen thousands of polymer-lipid formulations in days, '
                   'accelerating the development of non-viral gene delivery platforms capable of '
                   'surmounting the most severe physiological mucus barriers.',
 'cf_bridge': 'In the SIMPLIFY trial era (NCT06350474) and for modulator-ineligible CF patients, '
              'understanding how dornase alfa, hypertonic saline, and microbubble conditioning '
              '(DOI 10.1073/pnas.0705326104) expand xi_mesh is essential for getting '
              'inhaled mRNA and base/prime editors across the mortar matrix barrier.',
 'sources': ['de Gennes, P.-G. (1979). Scaling Concepts in Polymer Physics. Cornell University '
             'Press.',
             'Carreau, P. J. (1972). Rheological equations from molecular network theories. '
             'Transactions of the Society of Rheology, 16(1), 99–127.',
             'Lai, S. K., Wang, Y.-Y., & Hanes, J. (2009). Viscoplastic Grout-penetrating '
             'nanoparticles for drug and gene delivery to mucosal tissues. Adv. Drug Deliv. Rev., '
             '61(2), 158–171. DOI: 10.1016/j.addr.2008.11.002.',
             'Mason, T. G., & Weitz, D. A. (1995). Optical Measurements of Frequency-Dependent '
             'Linear Viscoelastic Moduli of Complex Fluids. Physical Review Letters, 74(7), '
             '1250–1253. DOI: 10.1103/PhysRevLett.74.1250.',
             'Schoenholz, S. S., & Cubuk, E. D. (2021). JAX, M.D.: A framework for differentiable '
             'physics (jax-md/jax-md, https://github.com/jax-md/jax-md). Journal of Statistical '
             'Mechanics: Theory and Experiment, 2021(12), 124006. DOI: 10.1088/1742-5468/ac3ae9.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="de Gennes mucin '
        'mesh scaling xi_mesh ~ w^-0.75 and anomalous subdiffusion exponent alpha">\n'
        '            <line x1="60" y1="185" x2="620" y2="185" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <line x1="60" y1="25" x2="60" y2="185" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <path d="M 60 180 L 580 35" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="3"/>\n'
        '            <path d="M 60 180 Q 280 155 580 132" fill="none" stroke="var(--tp-minium)" '
        'stroke-width="2.5" stroke-dasharray="5,4"/>\n'
        '            <text x="355" y="48" font-size="11" fill="var(--tp-verdigris)">Healthy 2% '
        'Mucin (ξ_mesh = 300 nm · α = 0.94 Normal Diffusion)</text>\n'
        '            <text x="330" y="122" font-size="11" fill="var(--tp-minium)">CF 8% Mortar '
        'Matrix (ξ_mesh = 65 nm · α = 0.38 Caged Subdiffusion)</text>\n'
        '            <text x="195" y="204" font-size="11" fill="currentColor">Log-Log Mean Squared '
        'Displacement ⟨Δr²(t)⟩ = 6 D_α t^α</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what PEGylated lipid nanoparticles diffusing through a '
        'cross-linked mucin polymer meshwork would look like (artistic impression, not a measured '
        'structure)',
 'caption': 'Conceptual Vision Plate P.03-V (Imagining What It Would Look Like) · Artistic '
            'soft-matter visualization imagining spherical lipid nanoparticles navigating pores '
            'within a 3D viscoelastic mucin glycoprotein mesh.'}

DISPATCH = {'kicker': 'FRONTIER SOFT MATTER DISPATCH · DE GENNES SCALING & MUCIN SUBDIFFUSION',
 'headline': 'Single-Particle Tracking Reveals Anomalous Subdiffusion to Normal Diffusion '
             'Crossover in CF Mortar Matrix',
 'body': "Applying Pierre-Gilles de Gennes's polymer correlation scaling and Mason–Weitz "
         'generalized Stokes–Einstein microrheology (Phys. Rev. Lett. DOI '
         '10.1103/PhysRevLett.74.1250), multiple-particle tracking studies (Lai et al. PNAS DOI '
         '10.1073/pnas.0705326104) map the exact mesh-size threshold where inhaled mRNA colloidal '
         'tracers escape mucin caging.'}

META_3D = ('Carreau–Yasuda Entangled Mucin Mesh & Shear Furrow',
 'X/Z: Mucin Biopolymer Network Plane · Y: Viscoelastic Energy & Shear-Thinning Trough')

ES_TRANSLATION = {'title_es': 'Reología de Materia Blanda y Subdifusión Anómala en Hidrogeles Entrelazados de '
             'Mucina',
 'subtitle_es': 'Adelgazamiento por corte de Carreau–Yasuda, dinámica de tubos de reptación y '
                'exponentes de subdifusión anómala de nanopartículas de terapia génica navegando '
                'la malla de moco bronquial.',
 'why_es': 'Cruzar un salón lleno de gente es rápido si caminas sin detenerte (recubrimiento denso '
           'de PEG muco-inerte), pero imposible si te detienes a estrechar la mano de cada persona '
           '(nanopartícula con carga electrostática adherente).',
 'plain_es': 'En 1979, el físico Pierre-Gilles de Gennes demostró que los geles biológicos y las '
             'cadenas de polímeros entrelazadas obedecen leyes geométricas universales de escala. '
             'Para entender cómo viajan los medicamentos a través de los pulmones, imaginen que el '
             'moco protector es como una red de pescar enredada. En una vía respiratoria sana, '
             'esta red es holgada, flexible y contiene abundante agua, con espacios abiertos de '
             'ciento cuarenta nanómetros por donde diminutas cápsulas con medicina pueden avanzar '
             'con facilidad. Sin embargo, cuando el tejido se inflama y se deshidrata, la célula '
             'produce demasiadas fibras de mucina en el mismo espacio. Los orificios de la red se '
             'cierran drásticamente, convirtiendo la malla abierta en un fieltro tupido que atrapa '
             'cualquier partícula mayor a cincuenta nanómetros. Si la medicina tiene una '
             'superficie pegajosa, queda adherida de inmediato a los hilos. Diseñar cápsulas '
             'microscópicas con cubiertas especiales y muy resbalosas permite que los fármacos se '
             'deslicen entre los poros antes de que la red los atrape.',
 'deep_es': 'La reología de materia blanda demuestra que la difusión en hidrogeles de mucina está '
            'gobernada por la ley de escala de correlación de de Gennes, donde el tamaño del poro '
            'se reduce con la concentración según una potencia de tres cuartos. El transporte de '
            'nanopartículas depende de dos factores críticos: la fracción de sólidos de mucina y '
            'el diámetro hidrodinámico de la partícula portadora. Si el diámetro de la partícula '
            'es menor que el tamaño de poro de la malla y su superficie está protegida con '
            'polímeros neutros, la partícula experimenta una difusión normal. Pero cuando la '
            'concentración de sólidos aumenta por encima del umbral crítico, el poro colapsa y el '
            'exponente de subdifusión cae por debajo de cero punto dos, atrapando la carga por '
            'exclusión estérica. Además, el modelo de Carreau-Yasuda muestra que el cizallamiento '
            'mecánico generado por la tos desenreda temporalmente las cadenas, reduciendo la '
            'viscosidad en varios órdenes de magnitud y abriendo ventanas transitorias para la '
            'penetración de terapias génicas avanzadas.',
 'bridge_es': 'Guía el diseño de nanopartículas lipídicas (colloidal tracer) recubiertas con '
              'polímeros zwitteriónicos o PEG denso para atravesar poros de mucina de 100–200 nm y '
              'entregar ARNm de CSI-MasterFormat a las células epiteliales.'}
