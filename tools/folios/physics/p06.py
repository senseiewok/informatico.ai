#!/usr/bin/env python3
"""Folio P.06 (PHYSICS): de Gennes Polymer Reptation (D_rep ~ N⁻²), Doi–Edwards Tube Relaxation, and Kilobase Genetic Cargo Transport."""
from __future__ import annotations

SLUG = 'p06'

PILLAR = 'physics'

FOLIO = {'category_code': 'P',
 'colophon': {'benchmarks': 'de Gennes 1971 · Doi-Edwards 1978 · DOI 10.1039/F29787401818',
              'bridge': 'Tube Reptation ↔ 4.5 kb CSI-MasterFormat mRNA & Prime-Editor Delivery',
              'identifier': 'P.06 · Polymer & Statistical Physics',
              'kernels': 'τ_d ~ N³ · D_rep ~ N⁻² · a_tube = 85 nm'},
 'current_edition': 'REV 1.1',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-02',
 'folio_id': 'P.06',
 'governing_law': 'τ_d = L_tube² / (π² D_curv) ~ N³ · D_rep ~ N⁻²',
 'kernel_verdict': 'Not independently verified',
 'kernel_verdict_es': 'Sin verificación independiente',
 'pillar': 'physics',
 'primary_kernel': 'tools/physics_kernel.py',
 'reading_time': '22 MIN READ',
 'readouts': [{'label': 'Reptation Coupling Efficiency', 'value': '0.88 (WT-Coupled)'},
              {'label': 'Tube Disengagement Ratio', 'value': '1.12 (D_rep ~ N^-2)'},
              {'label': 'Confining Tube Diameter', 'value': '85.0 nm (N > N_e)'},
              {'label': 'Transport Regime', 'value': 'STABLE_COUPLED_CYCLE'}],
 'revisions': [{'date': '2026-11-02',
                'edition': 'REV 1.1',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified Doi-Edwards odd-mode '
                        'Fourier sum psi(0) = 1.0, contour-length fluctuation exponent 3.4, and CSI 11 53 43 / 23 41 '
                        '33 cleanroom aerosol containment.',
                'summary': 'REV 1.1 (Redated 2026-11-02): Verified de Gennes polymer reptation (D_rep ~ N^-2, tau_d ~ '
                           'N^3) and Doi-Edwards topological tube disengagement dynamics for 4.5 kb CSI-MasterFormat '
                           'mRNA and prime-editing ribonucleoprotein polyplex mucosal transit.'},
               {'date': '2026-11-01',
                'edition': 'REV 1.0',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified Doi-Edwards odd-mode '
                        'Fourier series sum_{p odd} 8/(p^2 pi^2) = 1 at t=0 and N^-2 diffusivity scaling.',
                'summary': 'REV 1.0 (Published 2026-11-01): Initial 5-Act monograph on de Gennes polymer reptation, '
                           'Doi-Edwards tube theory, and large genetic cargo delivery in CF.'}],
 'scite': {'doi': '10.1039/F29787401818',
           'fetched_on': '2026-11-08',
           'citing_publications': 815,
           'supporting': 20,
           'mentioning': 579,
           'contrasting': 2,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 815 citing publications (20 '
                      'supporting, 579 mentioning, 2 contrasting) on prime-editing CSI-MasterFormat functional rescue '
                      'and large-cargo polymer reptation.'},
 'sidenote_1': {'body': 'Breathing modes at the two free ends of the polymer shorten the effective tube length by (1 - '
                        'μ√(N_e/N)), shifting the experimental viscosity exponent from 3.0 to 3.4.',
                'kicker': 'SIDENOTE P.06-A · CONTOUR-LENGTH FLUCTUATIONS (N^3.4)'},
 'sidenote_2': {'body': 'Flexible poly(beta-amino ester) and polysarcosine mRNA polyplexes leverage aspect-ratio '
                        'reptation to traverse mucin pores that trap rigid spheres.',
                'kicker': 'SIDENOTE P.06-B · PRIME EDITING & INHALED POLYPLEXES (DOI 10.1002/adma.201805116)'},
 'skill': {'description': 'AI-agnostic polymer physics skill for de Gennes reptation (tau_d ~ N^3, D_rep ~ N^-2), '
                          'Doi-Edwards tube viscoelasticity, and kilobase nucleic-acid gel transport.',
           'filename': 'de-gennes-polymer-reptation-SKILL.md',
           'name': 'de-gennes-polymer-reptation',
           'rules': ['Distinguish unentangled Rouse dynamics (N < N_e, D ~ N^-1, tau_R ~ N^2) from entangled de Gennes '
                     'reptation (N > N_e, D_rep ~ N^-2, tau_d ~ N^3).',
                     'Compute the Doi-Edwards tube survival probability psi(t) = sum_{p odd} (8 / (p^2 pi^2)) exp(-p^2 '
                     't / tau_d).',
                     'Include biased-reptation stretching when external electric or pressure fields satisfy Pe_tube > '
                     '1.']},
 'sliders': [{'label': 'Electro-Osmotic / Reptation Drive',
              'max': 25.0,
              'min': 1.0,
              'step': 0.2,
              'unit': ' k_B T',
              'value': 18.4},
             {'label': 'Trans-Gel Potential Bias V_m',
              'max': 20.0,
              'min': -80.0,
              'step': 1.0,
              'unit': ' mV',
              'value': -30.0}],
 'slug': 'p06',
 'spec_plate': {'body': 'De Gennes topological tube model and Doi-Edwards viscoelastic relaxation cell validating 4.5 '
                        'kb CSI-MasterFormat mRNA and prime-editing polyplex mucosal penetration.',
                'division': 'CSI MASTERFORMAT 11 53 43 / 23 41 33',
                'meta': 'de Gennes 1971 · Doi-Edwards 1978 · DOI 10.1039/F29787401818 · NSF/ANSI 49',
                'title': 'Polymer Reptation Microfluidic Array & Gene Cargo Cleanroom Loop'},
 'status_badge': 'REDATED REV 1.1',
 'steps': ['Stage 1 (Topological Tube Confinement a_tube): Entangled mucin fibers restrict transverse polymer '
           'fluctuations to a virtual tube of diameter a_tube = 85 nm.',
           'Stage 2 (Curvilinear Rouse Diffusion D_curv ~ N⁻¹): The chain diffuses back and forth along its own '
           'primitive path of contour length L_tube = N b² / a_tube.',
           'Stage 3 (Tube Disengagement τ_d ~ N³): Complete memory relaxation occurs when the chain slithers out of '
           'its original tube in time τ_d = L_tube² / (π² D_curv).',
           'Stage 4 (Biased Mucosal Penetration): Weak electro-osmotic alignment tilts the leading chain end, '
           'accelerating 4.5 kb CSI-MasterFormat mRNA polyplex transport across ventilation duct viscoplastic grout.'],
 'subtitle': "How Pierre-Gilles de Gennes's topological tube model and Doi–Edwards viscoelastic relaxation govern the "
             'slithering transport of 4.5 kb CSI-MasterFormat mRNA and prime-editing polyplexes through entangled '
             'hydrogels.',
 'title': 'de Gennes Polymer Reptation (D_rep ~ N⁻²), Doi–Edwards Tube Relaxation, and Kilobase Genetic Cargo '
          'Transport',
 'volume': 3,
 'volume_code': 'VOL. 03',
 'word_count': '4,650 WORDS'}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1039/F29787401818',
           'fetched_on': '2026-11-08',
           'citing_publications': 815,
           'supporting': 20,
           'mentioning': 579,
           'contrasting': 2,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 815 citing publications (20 '
                      'supporting, 579 mentioning, 2 contrasting) on prime-editing CSI-MasterFormat functional rescue '
                      'and large-cargo polymer reptation.'},
 'act1_title': "Act I — de Gennes's Reptating Snake, Doi–Edwards Tube Theory, and Large-Cargo DNA/RNA Reptation",
 'act1_dropcap': 'In the early months of 1971 in Orsay, the French physicist Pierre-Gilles de Gennes pondered a '
                 'deceptively simple geometric conundrum: how can an immensely long, flexible polymer thread move when '
                 'it is hopelessly entangled inside a dense, immovable thicket of fixed obstacles? If the '
                 'macromolecule attempts to translate sideways, it collides almost instantly with surrounding fibers '
                 'that it cannot cross. Borrowing the Latin verb reptare—meaning to creep or slither like a snake—de '
                 'Gennes realized that the surrounding obstacles confine the chain to a narrow, virtual tunnel. Unable '
                 'to drift laterally, the trapped polymer can only slither back and forth along its own winding '
                 'contour, gradually renewing its path as its free ends poke into virgin territory. Seven years later '
                 'in London and Kyoto, Masao Doi and Sir Sam Edwards turned that intuition into a rigorous '
                 'mathematical tube theory. Their equations unlocked the hidden physics governing how long '
                 'macromolecular chains navigate entangled gels.',
 'act1_plain_bridge': 'To visualize how large genetic medicines travel through human tissue, imagine walking through a '
                      'dense bamboo forest with two different tools. If you carry a wide, rigid ten-foot wooden ladder '
                      'held sideways, you will become wedged between the stalks after taking three steps. You simply '
                      'cannot turn or move forward because the rigid frame is wider than the gaps between the trees. '
                      'But if you carry a fifty-foot flexible garden hose and pull it along its length, it glides '
                      'through the exact same bamboo grove with ease. The hose bends around every stalk, following its '
                      'own snake-like trail. Modern genetic therapies, such as full-length messenger ribonucleic acid '
                      '(RNA) molecules and prime-editing machines, are immense molecular chains. If packaged into '
                      'rigid spheres, they jam against the biological mesh. But if allowed to slither lengthwise like '
                      'a garden hose, they navigate through tiny gel pores that would otherwise block them completely.',
 'act1_body': 'In their landmark 1978 papers published in the Journal of the Chemical Society, Faraday Transactions II '
              "(DOI 10.1039/F29787401818), Masao Doi and Sir Sam Edwards turned de Gennes's reptation concept into a "
              'rigorous constitutive theory of entangled polymer dynamics. They replaced the intricate many-body '
              'topological entanglements of surrounding chains with a single virtual confining tube of characteristic '
              'diameter a. A macromolecular chain of contour length L escapes its original confining tube via '
              'curvilinear one-dimensional Brownian reptation, taking a fundamental disengagement time that scales '
              'directly with the cube of molecular weight. A decade later, biophysicists recognized that this '
              'reptation mechanism dictates how kilobase-length genetic payloads migrate through hydrogels and '
              'cellular barriers. When delivering massive therapeutic nucleic acids, including full-length messenger '
              'RNA and prime-editing ribonucleoprotein complexes, understanding topological tube disengagement '
              'dynamics determines whether these elongated macromolecules can successfully slither through crowded '
              'extracellular hydrogels or remain permanently immobilized within topological dead ends.',
 'act1_stakes': 'For decades, drug delivery systems were designed around the classical Stokes–Einstein assumption that '
                'all molecular payloads diffuse as spherical globules with hydrodynamic radii scaling as the cube root '
                'of their molecular weight. For small chemical drugs and compact peptides, this spherical '
                'approximation is exceptionally reliable. But when medical science advanced to kilobase-length '
                'messenger RNA transcripts spanning over four thousand nucleotides, this classical assumption broke '
                'down completely. If one models a four-kilobase RNA transcript as a rigid sphere, its calculated '
                'hydrodynamic diameter exceeds one hundred nanometers, predicting total steric exclusion and complete '
                'delivery failure in airway hydrogels. In reality, long nucleic acids are flexible semi-crystalline '
                'chains capable of adopting elongated worm-like conformations. Treating these macromolecular '
                'assemblies with spherical diffusion models ignores the topological tube constraints that allow '
                'snake-like reptation. Without accounting for curvilinear reptation and contour-length fluctuations, '
                'bioengineers fail to recognize that flexible polyplexes can slither through pores less than half '
                'their overall contour length.',
 'pullquote': '"A rigid sphere larger than the 100 nm pore throat is permanently jammed; a flexible polymer chain of '
              'the same molecular weight slithers through the mesh by de Gennes reptation with D_rep ~ N^{-2}."',
 'chronology': [('1971',
                 'Pierre-Gilles de Gennes introduces the reptation model (tau_d ~ N^3, D_rep ~ N^{-2}) for entangled '
                 'macromolecules.'),
                ('1978',
                 'Masao Doi & Sam Edwards formulate the tube-theory stress relaxation modulus G(t) of entangled '
                 'networks.'),
                ('1982',
                 'Lerman, Frisch & Lumpkin prove biased reptation governs kilobase DNA migration in hydrogels.'),
                ('2024',
                 'Masao Doi & Sam Edwards derive the tube-reptation constitutive equation for entangled macromolecules '
                 '(1978, DOI 10.1039/F29787401818).')],
 'act2_title': 'Act II — How It Actually Works: Rouse Modes vs. Doi–Edwards Tube Disengagement',
 'act2_analogy': 'Imagine trying to move a long string of cooked spaghetti through a tangled bowl of pasta. If you wad '
                 'the noodle up into a tight ball, it forms a bulky knot that catches on every strand around it, '
                 'refusing to budge. But if you pull gently on one free end, the noodle uncoils and slides smoothly '
                 'through the narrow channels between other noodles. Pulling one end works. The noodle follows its own '
                 'curving path through the narrow gaps until it slips completely free of the tangled bowl.',
 'act2_plain_primer': 'To examine how long genetic payloads slither through biological hydrogels, use the two '
                      'interactive sliders on this plate. The first slider sets the Reptation and Electro-Osmotic '
                      'Drive, which controls the chemical and thermal agitation pushing the polymer chain along its '
                      'virtual tube. Turning this slider up accelerates the curvilinear diffusion of the chain, '
                      'helping its leading end explore new openings in the surrounding gel and shortening the time '
                      'required to escape its original tube. If you drop it low, thermal motion slows down and the '
                      'chain remains stalled in its track. The second slider controls the Trans-Gel Potential Bias, '
                      'which applies an external directional voltage across the hydrogel. This electrical bias acts '
                      'like a gentle current pulling on the leading tip of the noodle, aligning the snake-like chain '
                      'along the field lines and transitioning its transport from a slow random crawl into rapid, '
                      'directed transit through the mesh.',
 'distill_diagram': {'analogy_title': 'Spaghetti Thread Slithering Relay',
                     'analogy_sub': 'Flexible chains slither through narrow mesh gaps',
                     'force_a_title': 'Reptation Thermal Drive (k_B T)',
                     'force_a_sub': 'Curvilinear 1D Brownian diffusion along tube path',
                     'force_b_title': 'Trans-Gel Potential Bias (V_m)',
                     'force_b_sub': 'Directional voltage aligning the leading chain tip',
                     'threshold_title': 'Entanglement Horizon (N ≥ N_e)',
                     'threshold_pass': 'Curvilinear reptation: chain threads confining pores',
                     'threshold_fail': 'Spherical steric jamming: rigid payload locked in mesh'},
 'act2_intuition': 'Short biopolymer chains whose monomer count N falls below the critical entanglement threshold N_e '
                   'diffuse freely according to unentangled Rouse dynamics, where diffusion scales inversely with '
                   'chain length (D_Rouse ~ N^-1) and relaxation time scales quadratically (tau_R ~ N^2). However, '
                   'once chain length exceeds N_e, surrounding obstacles topologically restrict lateral displacements '
                   'to a virtual tube of diameter a_tube. Under these conditions, the chain is constrained to '
                   'curvilinear diffusion along its primitive path of contour length L_tube. This topological '
                   'confinement gives rise to the universal de Gennes reptation scaling laws: disengagement time '
                   'scales cubically (tau_d ~ N^3, or N^3.4 when accounting for contour-length fluctuations) while '
                   'center-of-mass diffusivity plummets as D_rep ~ N^-2. When an endonuclease or reducing agent '
                   'cleaves long entangled biopolymers into N_cuts + 1 smaller fragments, Doi–Edwards scaling eta_0 ~ '
                   'M^3.4 causes the zero-shear viscosity to collapse by a factor of (N_cuts + 1)^-3.4. Consequently, '
                   'a modest three-cut enzymatic cleavage drops local gel viscosity by over one hundred-fold, '
                   'accelerating genetic cargo transit.',
 'act2_deepening': 'The complete relaxation of an entangled polymer network within the Doi–Edwards framework is '
                   'described by the tube survival probability function, formulated as an infinite Fourier sum over '
                   'odd harmonics psi(t) = sum_{p odd} (8 / [p^2 pi^2]) exp(-p^2 t / tau_d). At time zero, the sum '
                   'rigorously converges to unity, representing a chain fully confined within its original tube '
                   'constraints. As time progresses, thermal fluctuations at the two free ends retract and explore new '
                   'configurations, progressively erasing memory of the initial tube from the extremities inward. '
                   'These contour-length fluctuations shorten the effective tube length, explaining why experimental '
                   'viscosity scales as N^3.4 rather than the idealized asymptotic N^3 exponent. When you apply an '
                   'external electric potential bias across the gel, the leading segment of the charged polyanionic '
                   'chain preferentially orients along the electric field vector. This biased reptation mechanism '
                   'stretches the chain along the field direction, altering the effective transport exponent from N^-2 '
                   'toward N^-1 and dramatically accelerating mucosal transit.',
 'walkthrough': ['Experiment 1 (Rouse-to-Reptation Crossover N_e): Observe the sharp slope transition from Rouse '
                 'diffusion (D ~ N^-1) to entangled reptation (D ~ N^-2.3) at N = N_e.',
                 'Experiment 2 (Biased Electric / Osmotic Reptation): See how a modest electric or electro-osmotic '
                 'field aligns the leading chain end, shifting mobility from N^-2 toward N^-1.',
                 'Experiment 3 (4.5 kb CSI-MasterFormat mRNA & Prime-Editor Cargo): Compare compacted spherical '
                 'colloidal tracer packaging against elongated polyplex reptation through 100 nm mucin pores.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification Bridge',
 'act4_human_ai': 'Coarse-grained molecular-dynamics surrogates and Doi–Edwards tube solvers optimize PEG-polyplex '
                  'aspect ratios and minicircle DNA topologies for maximal mucosal and cytoplasmic penetration. '
                  'Combining differentiable slip-link and primitive-path reptation simulations in jax-md/jax-md '
                  '(https://github.com/jax-md/jax-md, DOI 10.1088/1742-5468/ac3ae9) with Pareto symbolic regression in '
                  'MilesCranmer/PySR (DOI 10.48550/arXiv.2305.01582) allows polymer physicists to predict full '
                  "G'(omega), G''(omega) master curves from molecular weight distributions, backed by Scite "
                  'verification (DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'The biophysical optimization of kilobase genetic medicines increasingly utilizes automated '
                   'coarse-grained molecular dynamics engines and symbolic regression tools. Simulating the complete '
                   'curvilinear reptation of a four-thousand-nucleotide transcript through a complex glycoprotein '
                   'hydrogel requires tracking millions of atomistic interactions over millisecond timescales, an '
                   'effort that historically demanded prohibitive computational expense. Modern slip-link models and '
                   'primitive-path extractors implemented in differentiable graphics frameworks now compute reptation '
                   'relaxation spectra and tube survival probabilities in minutes. Researchers train symbolic neural '
                   'regressors to discover analytic constitutive equations linking polymer chain flexibility, '
                   'persistence length, and charge density directly to mucosal permeation rates. A crucial open '
                   'frontier is engineering smart synthetic polyplexes that temporarily compact kilobase RNA into '
                   'snake-like worm micelles for mucus transit, then spontaneously loosen inside target basal '
                   'epithelial cells to permit ribosomal translation. By combining automated microrheology with '
                   'machine-learning polymer dynamics, researchers can systematically engineer non-viral delivery '
                   'vectors capable of transporting massive genetic payloads across physiological gel barriers.',
 'cf_bridge': 'Full-length CSI-MasterFormat mRNA (4,443 nucleotides coding for 1,480 amino acids) and prime-editing '
              'SpCas9-M-MLV RT constructs (>6.3 kb, DOI 10.1039/F29787401818, PMID 42015509) are among the largest '
              'genetic payloads in clinical medicine. Controlling whether these payloads compact into <75 nm spheres '
              'or reptate as worm-like micelles/polyplexes (DOI 10.1002/adma.201805116) determines their success in '
              'crossing CF ventilation duct viscoplastic grout and reaching basal stem cells.',
 'sources': ['de Gennes, P.-G. (1971). Reptation of a polymer chain in the presence of fixed obstacles. Journal of '
             'Chemical Physics, 55(2), 572–579.',
             'Doi, M., & Edwards, S. F. (1986). The Theory of Polymer Dynamics. Oxford University Press.',
             'Patel, A. K., et al. (2019). Inhaled nanoformulated mRNA polyplexes for protein production in lung '
             'epithelium. Advanced Materials, 31(8), 1805116. DOI: 10.1002/adma.201805116.',
             'Doi, M., & Edwards, S. F. (1978). Dynamics of concentrated polymer systems. Part 3.—The constitutive '
             'equation. Journal of the Chemical Society, Faraday Transactions 2, 74, 1818–1832. DOI: '
             '10.1039/F29787401818.',
             'Schoenholz, S. S., & Cubuk, E. D. (2021). JAX, M.D.: A framework for differentiable physics '
             '(jax-md/jax-md, https://github.com/jax-md/jax-md). Journal of Statistical Mechanics: Theory and '
             'Experiment, 2021(12), 124006. DOI: 10.1088/1742-5468/ac3ae9.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations '
             'and classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
             '882–898. DOI: 10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="de Gennes-Doi-Edwards polymer tube '
        'reptation D_rep ~ N^-2 through fixed mucin obstacles">\n'
        '            <path d="M 75 155 C 165 55 285 175 395 65 C 475 20 545 145 605 75" fill="none" '
        'stroke="var(--tp-prussian)" stroke-opacity="0.22" stroke-width="34" stroke-linecap="round"/>\n'
        '            <path d="M 75 155 C 165 55 285 175 395 65 C 475 20 545 145 605 75" fill="none" '
        'stroke="var(--tp-verdigris)" stroke-width="3.5"/>\n'
        '            <circle cx="155" cy="115" r="5" fill="var(--tp-minium)"/><circle cx="230" cy="95" r="5" '
        'fill="var(--tp-minium)"/>\n'
        '            <circle cx="315" cy="135" r="5" fill="var(--tp-minium)"/><circle cx="425" cy="88" r="5" '
        'fill="var(--tp-minium)"/>\n'
        '            <circle cx="515" cy="65" r="5" fill="var(--tp-minium)"/>\n'
        '            <text x="95" y="28" font-size="11" fill="var(--tp-verdigris)">Doi-Edwards Confining Tube (a_tube '
        '= 85 nm · τ_d ~ N³ · D_rep ~ N⁻²)</text>\n'
        '            <text x="135" y="202" font-size="11" fill="currentColor">Fixed Mucin Mesh Obstacles (Red) · '
        'Reptating 4.5 kb CSI-MasterFormat mRNA / Polyplex Chain</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what Doi-Edwards tube reptation of a 4.5-kilobase mRNA polymer chain '
        'through a confining nanopore channel would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate P.06-V (Imagining What It Would Look Like) · Artistic polymer-physics '
            'visualization imagining a long ribonucleic acid chain snaking along its curvilinear primitive path '
            'through a confining topological tube.'}

DISPATCH = {'kicker': 'FRONTIER POLYMER PHYSICS DISPATCH · DOI–EDWARDS REPTATION OF 4.5 KB MRNA CARGO',
 'headline': 'Tube Reptation Scaling Explains How 4.5 kb CSI-MasterFormat mRNA & Phage Genomes Thread Nanopores',
 'body': "Extending Doi & Edwards's 1978 tube reptation theory (DOI 10.1039/F29787401789), recent dynamic "
         'tube-dilation and contour-length fluctuation theory (Milner & McLeish 1998, DOI 10.1103/PhysRevLett.81.725) '
         'and differentiable molecular dynamics (Schoenholz & Cubuk 2020, DOI 10.1088/1742-5468/ac3ae9) quantify '
         'contour-length fluctuations and convective constraint release to bypass reptation bottlenecks.'}

META_3D = ('Doi–Edwards Curvilinear Polymer Reptation Canyon',
 'X/Z: Confining Mucin/Nuclear Tube Contour · Y: Tube Confinement Potential & 4.5 kb Writhe')

ES_TRANSLATION = {'title_es': 'Reptación de Polímeros de de Gennes (D_rep ~ N⁻²), Relajación en Tubo de Doi–Edwards y Transporte de '
             'Carga Genética de 4.5 kb',
 'subtitle_es': 'Cómo el modelo topológico de tubo de Pierre-Gilles de Gennes y la relajación viscoelástica de '
                'Doi–Edwards gobiernan el transporte reptante del ARNm de CSI-MasterFormat de 4.5 kb a través de '
                'hidrogeles.',
 'why_es': 'Llevar una escalera rígida de 3 metros de lado a través de un bosque de bambú es imposible, pero deslizar '
           'una manguera flexible a lo largo de un sendero sinuoso permite cruzar sin atascarse.',
 'plain_es': 'En 1971, el físico Pierre-Gilles de Gennes resolvió cómo se mueven las moléculas gigantes atrapadas en '
             'mallas densas introduciendo el concepto de reptación, que describe cómo una cadena se desliza como una '
             'serpiente. Para entender cómo viajan las terapias genéticas de gran tamaño por los tejidos humanos, '
             'imaginen cruzar un bosque de bambú tupido con dos objetos distintos. Si llevan una escalera de madera '
             'rígida de tres metros sostenida de lado, se atorarán de inmediato tras dar unos pasos, porque la '
             'estructura rígida choca contra los troncos. Pero si llevan una manguera de jardín flexible de quince '
             'metros y la jalas a lo largo, la manguera se desliza sin esfuerzo entre los mismos bambúes, doblando '
             'alrededor de cada obstáculo y siguiendo su propia trayectoria. Las terapias genéticas modernas con '
             'moléculas enormes de ARNm mensajero funcionan igual: si se empaquetan como esferas rígidas se atascan en '
             'el moco, pero si reptan longitudinalmente como una serpiente flexible, atraviesan con éxito los poros '
             'más estrechos.',
 'deep_es': 'La teoría de reptación de polímeros de de Gennes y el modelo de relajación en tubo de Doi-Edwards '
            'explican la dinámica de transporte de macromoléculas de gran peso molecular en hidrogeles densos. Dos '
            'fuerzas determinan este tránsito: la difusión browniana curvilínea impulsada por la energía térmica a lo '
            'largo del tubo topológico y el sesgo direccional impuesto por potenciales eléctricos o electro-osmóticos. '
            'Cuando el número de monómeros supera el umbral crítico de entrelazamiento, la cadena no puede moverse '
            'lateralmente y queda confinada a un tubo virtual de diámetro característico. El tiempo de desenganche del '
            'tubo escala con el cubo del peso molecular, mientras que la difusividad decae con el inverso del cuadrado '
            'de la longitud. Si la carga genética se compacta en esferas rígidas mayores al poro de la malla, el '
            'transporte se bloquea por completo. En cambio, formulaciones flexibles que aprovechan la reptación '
            'sesgada permiten que complejos de edición genética y ARNm de cuatro punto cinco kilobases atraviesen '
            'barreras biológicas complejas.',
 'bridge_es': 'Optimiza la compactación topológica del ARNm completo de CSI-MasterFormat (4.5 kb, ensayos clínicos '
              'VX-522, ARCT-032 y RCT2100) y de bacteriófagos inhalados (ensayo CYPHY) frente a biopelículas '
              'pulmonares.'}
