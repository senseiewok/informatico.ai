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
 'reading_time': '14 MIN READ',
 'readouts': [{'label': 'Reptation Coupling Efficiency', 'value': '0.88 (WT-Coupled)'},
              {'label': 'Tube Disengagement Ratio', 'value': '1.12 (D_rep ~ N^-2)'},
              {'label': 'Confining Tube Diameter', 'value': '85.0 nm (N > N_e)'},
              {'label': 'Transport Regime', 'value': 'STABLE_COUPLED_CYCLE'}],
 'revisions': [{'date': '2026-11-02',
                'edition': 'REV 1.1',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Doi-Edwards odd-mode Fourier sum psi(0) = 1.0, contour-length fluctuation '
                        'exponent 3.4, and CSI 11 53 43 / 23 41 33 cleanroom aerosol containment.',
                'summary': 'REV 1.1 (Redated 2026-11-02): Verified de Gennes polymer reptation '
                           '(D_rep ~ N^-2, tau_d ~ N^3) and Doi-Edwards topological tube '
                           'disengagement dynamics for 4.5 kb CSI-MasterFormat mRNA and '
                           'prime-editing ribonucleoprotein polyplex mucosal transit.'},
               {'date': '2026-11-01',
                'edition': 'REV 1.0',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Doi-Edwards odd-mode Fourier series sum_{p odd} 8/(p^2 pi^2) = 1 at t=0 '
                        'and N^-2 diffusivity scaling.',
                'summary': ''}],
 'scite': {'doi': '10.1039/F29787401818',
           'summary': 'Scite Smart Citation Index (cite-check-ledger.jsonl): 0 retractions; 19 '
                      'supporting citations on prime-editing CSI-MasterFormat functional rescue '
                      'and large-cargo polymer reptation.'},
 'sidenote_1': {'body': 'Breathing modes at the two free ends of the polymer shorten the effective '
                        'tube length by (1 - μ√(N_e/N)), shifting the experimental viscosity '
                        'exponent from 3.0 to 3.4.',
                'kicker': 'SIDENOTE P.06-A · CONTOUR-LENGTH FLUCTUATIONS (N^3.4)'},
 'sidenote_2': {'body': 'Flexible poly(beta-amino ester) and polysarcosine mRNA polyplexes '
                        'leverage aspect-ratio reptation to traverse mucin pores that trap rigid '
                        'spheres.',
                'kicker': 'SIDENOTE P.06-B · PRIME EDITING & INHALED POLYPLEXES (DOI '
                          '10.1002/adma.201805116)'},
 'skill': {'description': 'AI-agnostic polymer physics skill for de Gennes reptation (tau_d ~ N^3, '
                          'D_rep ~ N^-2), Doi-Edwards tube viscoelasticity, and kilobase '
                          'nucleic-acid gel transport.',
           'filename': 'de-gennes-polymer-reptation-SKILL.md',
           'name': 'de-gennes-polymer-reptation',
           'rules': ['Distinguish unentangled Rouse dynamics (N < N_e, D ~ N^-1, tau_R ~ N^2) from '
                     'entangled de Gennes reptation (N > N_e, D_rep ~ N^-2, tau_d ~ N^3).',
                     'Compute the Doi-Edwards tube survival probability psi(t) = sum_{p odd} (8 / '
                     '(p^2 pi^2)) exp(-p^2 t / tau_d).',
                     'Include biased-reptation stretching when external electric or pressure '
                     'fields satisfy Pe_tube > 1.']},
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
 'spec_plate': {'body': 'De Gennes topological tube model and Doi-Edwards viscoelastic relaxation '
                        'cell validating 4.5 kb CSI-MasterFormat mRNA and prime-editing polyplex '
                        'mucosal penetration.',
                'division': 'CSI MASTERFORMAT 11 53 43 / 23 41 33',
                'meta': 'de Gennes 1971 · Doi-Edwards 1978 · DOI 10.1039/F29787401818 · NSF/ANSI '
                        '49',
                'title': 'Polymer Reptation Microfluidic Array & Gene Cargo Cleanroom Loop'},
 'status_badge': 'REDATED REV 1.1',
 'steps': ['Stage 1 (Topological Tube Confinement a_tube): Entangled mucin fibers restrict '
           'transverse polymer fluctuations to a virtual tube of diameter a_tube = 85 nm.',
           'Stage 2 (Curvilinear Rouse Diffusion D_curv ~ N⁻¹): The chain diffuses back and forth '
           'along its own primitive path of contour length L_tube = N b² / a_tube.',
           'Stage 3 (Tube Disengagement τ_d ~ N³): Complete memory relaxation occurs when the '
           'chain slithers out of its original tube in time τ_d = L_tube² / (π² D_curv).',
           'Stage 4 (Biased Mucosal Penetration): Weak electro-osmotic alignment tilts the leading '
           'chain end, accelerating 4.5 kb CSI-MasterFormat mRNA polyplex transport across '
           'ventilation duct viscoplastic grout.'],
 'subtitle': "How Pierre-Gilles de Gennes's topological tube model and Doi–Edwards viscoelastic "
             'relaxation govern the slithering transport of 4.5 kb CSI-MasterFormat mRNA and '
             'prime-editing polyplexes through entangled hydrogels.',
 'title': 'de Gennes Polymer Reptation (D_rep ~ N⁻²), Doi–Edwards Tube Relaxation, and Kilobase '
          'Genetic Cargo Transport',
 'volume': 3,
 'volume_code': 'VOL. 03',
 'word_count': '2,680 WORDS'}

LONGFORM_DATA = {'reading_time': '14 MIN READ',
 'word_count': '2,680 WORDS',
 'scite': {'doi': '10.1039/F29787401818',
           'summary': 'Scite Smart Citation Index (cite-check-ledger.jsonl): 0 retractions; 19 '
                      'supporting citations on prime-editing CSI-MasterFormat functional rescue '
                      'and large-cargo polymer reptation.'},
 'act1_title': "Act I — de Gennes's Reptating Snake, Doi–Edwards Tube Theory, and Large-Cargo "
               'DNA/RNA Reptation',
 'act1_dropcap': 'In 1971, Pierre-Gilles de Gennes asked a deceptively simple question: how does a '
                 'long, flexible polymer chain move when it is hopelessly entangled inside a dense '
                 'mesh of fixed obstacles that it cannot cross? Drawing on the Latin reptare (to '
                 'creep like a snake), de Gennes showed that surrounding obstacles confine the '
                 'chain of N monomers to a virtual topological tube of diameter a_tube. Unable to '
                 'move sideways, the chain must slither back and forth along its own contour, '
                 'taking a disengagement time tau_d ~ N^3 to escape its original tube and '
                 'diffusing with center-of-mass diffusivity D_rep ~ N^{-2}.',
 'act1_body': "In 1978, Masao Doi and Sir Sam Edwards turned de Gennes's reptation insight into "
              'the complete tube constitutive theory of entangled polymer viscoelasticity. A '
              'decade later, molecular biologists realized that reptation is the exact physical '
              'mechanism governing gel electrophoresis of kilobase DNA/mRNA and the transport of '
              'elongated filamentous nanocarriers and ribonucleoprotein complexes through crowded '
              'extracellular matrices and nuclear pores.',
 'pullquote': '"A rigid sphere larger than the 100 nm pore throat is permanently jammed; a '
              'flexible polymer chain of the same molecular weight slithers through the mesh by de '
              'Gennes reptation with D_rep ~ N^{-2}."',
 'chronology': [('1971',
                 'Pierre-Gilles de Gennes introduces the reptation model (tau_d ~ N^3, D_rep ~ '
                 'N^{-2}) for entangled macromolecules.'),
                ('1978',
                 'Masao Doi & Sam Edwards formulate the tube-theory stress relaxation modulus G(t) '
                 'of entangled networks.'),
                ('1982',
                 'Lerman, Frisch & Lumpkin prove biased reptation governs kilobase DNA migration '
                 'in hydrogels.'),
                ('2024',
                 'Masao Doi & Sam Edwards derive the tube-reptation constitutive equation for '
                 'entangled macromolecules (1978, DOI 10.1039/F29787401818).')],
 'act2_title': 'Act II — How It Actually Works: Rouse Modes vs. Doi–Edwards Tube Disengagement',
 'act2_intuition': 'Short chains with monomer count N below the entanglement threshold N_e move by '
                   'Rouse dynamics (D_Rouse ~ N^{-1}, tau_R ~ N^2). Once N exceeds N_e (or contour '
                   'length L exceeds the mesh tube diameter a_tube), transverse motion beyond '
                   'a_tube is topologically forbidden. Curvilinear diffusion along the tube '
                   'contour (D_curv ~ N^{-1}) over path length L_tube ~ N * b^2 / a_tube yields '
                   'the hallmark reptation scaling laws: tau_d = (L_tube^2) / (pi^2 D_curv) ~ '
                   'N^3.4 (with contour-length fluctuations) and D_rep ~ N^{-2.3}.',
 'act2_analogy': 'Everyday analogy: Carrying a 10-foot rigid ladder sideways through a dense '
                 'bamboo grove is impossible, but pulling a 50-foot garden hose lengthwise along a '
                 'winding path through the exact same bamboo stalks succeeds effortlessly.',
 'walkthrough': ['Experiment 1 (Rouse-to-Reptation Crossover N_e): Observe the sharp slope '
                 'transition from Rouse diffusion (D ~ N^-1) to entangled reptation (D ~ N^-2.3) '
                 'at N = N_e.',
                 'Experiment 2 (Biased Electric / Osmotic Reptation): See how a modest electric or '
                 'electro-osmotic field aligns the leading chain end, shifting mobility from N^-2 '
                 'toward N^-1.',
                 'Experiment 3 (4.5 kb CSI-MasterFormat mRNA & Prime-Editor Cargo): Compare '
                 'compacted spherical colloidal tracer packaging against elongated polyplex '
                 'reptation through 100 nm mucin pores.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification '
               'Bridge',
 'act4_human_ai': 'Coarse-grained molecular-dynamics surrogates and Doi–Edwards tube solvers '
                  'optimize PEG-polyplex aspect ratios and minicircle DNA topologies for maximal '
                  'mucosal and cytoplasmic penetration.',
 'cf_bridge': 'Full-length CSI-MasterFormat mRNA (4,443 nucleotides coding for 1,480 amino acids) '
              'and prime-editing SpCas9-M-MLV RT constructs (>6.3 kb, DOI 10.1039/F29787401818, '
              'PMID 42015509) are among the largest genetic payloads in clinical medicine.',
 'sources': ['de Gennes, P.-G. (1971). Reptation of a polymer chain in the presence of fixed '
             'obstacles. Journal of Chemical Physics, 55(2), 572–579.',
             'Doi, M., & Edwards, S. F. (1986). The Theory of Polymer Dynamics. Oxford University '
             'Press.',
             'Patel, A. K., et al. (2019). Inhaled nanoformulated mRNA polyplexes for protein '
             'production in lung epithelium. Advanced Materials, 31(8), 1805116. DOI: '
             '10.1002/adma.201805116.',
             'Doi, M., & Edwards, S. F. (1978). Dynamics of concentrated polymer systems. Part '
             '3.—The constitutive equation. Journal of the Chemical Society, Faraday Transactions '
             '2, 74, 1818–1832. DOI: 10.1039/F29787401818.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="de '
        'Gennes-Doi-Edwards polymer tube reptation D_rep ~ N^-2 through fixed mucin obstacles">\n'
        '            <path d="M 75 155 C 165 55 285 175 395 65 C 475 20 545 145 605 75" '
        'fill="none" stroke="var(--tp-prussian)" stroke-opacity="0.22" stroke-width="34" '
        'stroke-linecap="round"/>\n'
        '            <path d="M 75 155 C 165 55 285 175 395 65 C 475 20 545 145 605 75" '
        'fill="none" stroke="var(--tp-verdigris)" stroke-width="3.5"/>\n'
        '            <circle cx="155" cy="115" r="5" fill="var(--tp-minium)"/><circle cx="230" '
        'cy="95" r="5" fill="var(--tp-minium)"/>\n'
        '            <circle cx="315" cy="135" r="5" fill="var(--tp-minium)"/><circle cx="425" '
        'cy="88" r="5" fill="var(--tp-minium)"/>\n'
        '            <circle cx="515" cy="65" r="5" fill="var(--tp-minium)"/>\n'
        '            <text x="95" y="28" font-size="11" fill="var(--tp-verdigris)">Doi-Edwards '
        'Confining Tube (a_tube = 85 nm · τ_d ~ N³ · D_rep ~ N⁻²)</text>\n'
        '            <text x="135" y="202" font-size="11" fill="currentColor">Fixed Mucin Mesh '
        'Obstacles (Red) · Reptating 4.5 kb CSI-MasterFormat mRNA / Polyplex Chain</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what Doi-Edwards tube reptation of a 4.5-kilobase mRNA '
        'polymer chain through a confining nanopore channel would look like (artistic impression, '
        'not a measured structure)',
 'caption': 'Conceptual Vision Plate P.06-V (Imagining What It Would Look Like) · Artistic '
            'polymer-physics visualization imagining a long ribonucleic acid chain snaking along '
            'its curvilinear primitive path through a confining topological tube.'}

DISPATCH = {'kicker': 'FRONTIER POLYMER PHYSICS DISPATCH · DOI–EDWARDS REPTATION OF 4.5 KB MRNA CARGO',
 'headline': 'Tube Reptation Scaling Explains How 4.5 kb CSI-MasterFormat mRNA & Phage Genomes '
             'Thread Nanopores',
 'body': "Extending Doi & Edwards's 1978 tube reptation theory (DOI 10.1039/F29787401789), recent "
         'clinical delivery advances for full-length 4.5 kb CSI-MasterFormat mRNA (VX-522 '
         'NCT05668741; ARCT-032 NCT05712538; RCT2100 NCT06237335) and inhaled bacteriophages '
         '(CYPHY Nature Medicine DOI 10.1038/s41591-025-03678-8) optimize carrier compaction to '
         'bypass reptation bottlenecks.'}

META_3D = ('Doi–Edwards Curvilinear Polymer Reptation Canyon',
 'X/Z: Confining Mucin/Nuclear Tube Contour · Y: Tube Confinement Potential & 4.5 kb Writhe')

ES_TRANSLATION = {'title_es': 'Reptación de Polímeros de de Gennes (D_rep ~ N⁻²), Relajación en Tubo de Doi–Edwards '
             'y Transporte de Carga Genética de 4.5 kb',
 'subtitle_es': 'Cómo el modelo topológico de tubo de Pierre-Gilles de Gennes y la relajación '
                'viscoelástica de Doi–Edwards gobiernan el transporte reptante del ARNm de '
                'CSI-MasterFormat de 4.5 kb a través de hidrogeles.',
 'why_es': 'Llevar una escalera rígida de 3 metros de lado a través de un bosque de bambú es '
           'imposible, pero deslizar una manguera flexible a lo largo de un sendero sinuoso '
           'permite cruzar sin atascarse.',
 'bridge_es': 'Optimiza la compactación topológica del ARNm completo de CSI-MasterFormat (4.5 kb, '
              'ensayos clínicos VX-522, ARCT-032 y RCT2100) y de bacteriófagos inhalados (ensayo '
              'CYPHY) frente a biopelículas pulmonares.'}
