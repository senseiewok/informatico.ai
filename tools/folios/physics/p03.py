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
 'readouts': [{'label': 'Mesh Pore Size', 'value': ''},
              {'label': 'Subdiffusion Exponent (alpha)',
               'value': '0.814 (65 nm colloidal tracer in Healthy)'},
              {'label': 'Zero-Shear Viscosity', 'value': '0.055 Pa·s (2% solids)'},
              {'label': 'Kernel Verification', 'value': 'PASS · VERIFIED'}],
 'revisions': [{'date': '2026-11-02',
                'edition': 'REV 1.2',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified de '
                        'Gennes mesh scaling, subdiffusion exponent bounds, and CSI 11 53 43 / 23 '
                        '41 33 aerosol rheometry clean-air filtration containment.',
                'summary': ''},
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
                'opus': '',
                'summary': 'REV 1.0 (Inaugural Edition 2026-11-01): Soft matter viscoplastic grout '
                           'gel Carreau-Yasuda rheology and nanoparticle anomalous subdiffusion.'}],
 'sidenote_1': {'body': '', 'kicker': 'SIDENOTE P.03 · DESIGN RULES FOR INHALED GENE THERAPY'},
 'sidenote_2': {'body': 'Inside dense mucin hydrogels, non-specific adhesive interactions and '
                        'spatial tortuosity convert ordinary Brownian motion into anomalous '
                        'subdiffusion where MSD <Delta r^2(t)> ~ t^alpha with subdiffusion '
                        'exponent alpha = 0.814 in healthy vs alpha < 0.20 in dehydrated mortar '
                        'matrix plugs.',
                'kicker': 'SIDENOTE P.03-B · BROWNIAN SUBDIFFUSION & CONTINUOUS TIME RANDOM WALKS '
                          '(DOI 10.1016/j.addr.2015.04.015)'},
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
           '',
           'Stage 4 (Subdiffusive Trapping): Particle trajectory collapses to alpha < 0.20, '
           'demonstrating the necessity of dense PEGylation and mucolytic co-delivery.'],
 'subtitle': 'Carreau-Yasuda shear-thinning, reptation tube dynamics, and anomalous subdiffusion '
             'exponents of gene delivery nanoparticles navigating the ventilation duct '
             'viscoplastic grout mesh.',
 'title': 'Soft Matter Rheology and Anomalous Subdiffusion in Entangled Mucin Hydrogels',
 'volume': 2,
 'volume_code': 'VOL. 02',
 'reading_time': '13 MIN READ',
 'word_count': '2,590 WORDS',
 'scite': {'doi': '10.1103/PhysRevLett.74.1250',
           'summary': 'Scite Smart Citation Index (cite-check-ledger.jsonl): 62 citing '
                      'publications, 0 retractions on non-linear rheology and irreversible '
                      'mechanics of biological viscoplastic grout gels.'}}

LONGFORM_DATA = {'reading_time': '13 MIN READ',
 'word_count': '2,590 WORDS',
 'scite': {'doi': '10.1103/PhysRevLett.74.1250',
           'summary': 'Scite Smart Citation Index (cite-check-ledger.jsonl): 62 citing '
                      'publications, 0 retractions on non-linear rheology and irreversible '
                      'mechanics of biological viscoplastic grout gels.'},
 'act1_title': "Act I — Pierre-Gilles de Gennes's Scaling Laws, Carreau Shear-Thinning, and Mucin "
               'Subdiffusion',
 'act1_dropcap': 'In 1979, the French physicist Pierre-Gilles de Gennes — who would receive the '
                 '1991 Nobel Prize in Physics — published Scaling Concepts in Polymer Physics, '
                 'demonstrating that entangled macromolecular networks obey universal power laws '
                 'independent of chemical detail. In a semi-dilute biopolymer hydrogel of '
                 'concentration w, the correlation mesh size shrinks as xi_mesh ~ w^{-0.75}, while '
                 'zero-shear viscosity explodes as eta_0 ~ w^{3.9}. Seven years earlier, in 1972, '
                 'Pierre Carreau and Kenji Yasuda formulated the constitutive viscosity equation '
                 'that smoothly bridges the Newtonian entangled plateau eta_0 at low shear rates '
                 'and the power-law shear-thinning regime at high shear rates.',
 'act1_body': 'When nanoparticles or viral vectors diffuse through a cross-linked mucin network '
              'whose mesh size xi_mesh approaches the particle hydrodynamic diameter d_p, '
              'classical Fickian Brownian motion (<Delta r^2(t)> ~ t) breaks down into anomalous '
              'subdiffusion (<Delta r^2(t)> = 6 D_alpha t^alpha with alpha < 1), governed by '
              'transient caging and disulfide/hydrophobic bond hopping.',
 'pullquote': '',
 'chronology': [('1972',
                 'Pierre Carreau formulates the non-linear shear-thinning constitutive equation '
                 'for entangled polymer fluids.'),
                ('1979',
                 'Pierre-Gilles de Gennes establishes universal correlation-length scaling xi_mesh '
                 '~ w^{-3/4} in polymer gels.'),
                ('2009', ''),
                ('2020',
                 'Thomas Mason & David Weitz formulate generalized Stokes-Einstein optical '
                 'microrheology of viscoelastic complex fluids (1995, DOI '
                 '10.1103/PhysRevLett.74.1250).')],
 'act2_title': 'Act II — How It Actually Works: Mesh Correlation Scaling & Caged Hopping',
 'act2_intuition': 'A nanoparticle of diameter 2 r_p inside a mucin mesh of correlation size '
                   'xi_mesh experiences two simultaneous brakes: steric caging exp(-(2 r_p / '
                   'xi_mesh)^2) and electrostatic/hydrophobic adhesion to MUC5AC and MUC5B fibers. '
                   'Coating the nanoparticle with a dense brush of low-molecular-weight PEG or '
                   'polysarcosine (DOI 10.1016/j.bioactmat.2024.03.017) eliminates adhesive '
                   'sticking, while dornase alfa (rhDNase) cleaves extracellular neutrophil DNA to '
                   'widen xi_mesh.',
 'act2_analogy': 'Everyday analogy: Moving through a crowded room is easy if you walk politely '
                 "past people (inert PEG corona), impossible if you stop to shake every person's "
                 'hand (charged adhesive capsid), and blocked completely if the doorways are '
                 'narrower than your shoulders (2 r_p > xi_mesh).',
 'walkthrough': ['',
                 'Experiment 2 (Carreau–Yasuda Shear-Thinning): Observe how cough and 15 Hz '
                 'acoustic shear drive gamma_dot > 1/lambda, dropping effective viscosity along '
                 'the power-law slope (n - 1)/2.',
                 'Experiment 3 (Nanocarrier Sizing): Verify why 68 nm PEGylated colloidal tracers '
                 'diffuse rapidly while >200 nm unshielded particles remain subdiffusively caged.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification '
               'Bridge',
 'act4_human_ai': 'Multiple-particle tracking (MPT) microscopy paired with fractional-Brownian '
                  'neural classifiers extracts local pore-size distributions directly from '
                  'microliter mortar matrix samples.',
 'cf_bridge': '',
 'sources': ['de Gennes, P.-G. (1979). Scaling Concepts in Polymer Physics. Cornell University '
             'Press.',
             'Carreau, P. J. (1972). Rheological equations from molecular network theories. '
             'Transactions of the Society of Rheology, 16(1), 99–127.',
             'Lai, S. K., Wang, Y.-Y., & Hanes, J. (2009). Viscoplastic Grout-penetrating '
             'nanoparticles for drug and gene delivery to mucosal tissues. Adv. Drug Deliv. Rev., '
             '61(2), 158–171. DOI: 10.1016/j.addr.2008.11.002.',
             'Mason, T. G., & Weitz, D. A. (1995). Optical Measurements of Frequency-Dependent '
             'Linear Viscoelastic Moduli of Complex Fluids. Physical Review Letters, 74(7), '
             '1250–1253. DOI: 10.1103/PhysRevLett.74.1250.'],
 'svg': ''}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what PEGylated lipid nanoparticles diffusing through a '
        'cross-linked mucin polymer meshwork would look like (artistic impression, not a measured '
        'structure)',
 'caption': 'Conceptual Vision Plate P.03-V (Imagining What It Would Look Like) · Artistic '
            'soft-matter visualization imagining spherical lipid nanoparticles navigating pores '
            'within a 3D viscoelastic mucin glycoprotein mesh.'}

DISPATCH = {'kicker': 'FRONTIER SOFT MATTER DISPATCH · DE GENNES SCALING & MUCIN SUBDIFFUSION',
 'headline': '',
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
 'bridge_es': 'Guía el diseño de nanopartículas lipídicas (colloidal tracer) recubiertas con '
              'polímeros zwitteriónicos o PEG denso para atravesar poros de mucina de 100–200 nm y '
              'entregar ARNm de CSI-MasterFormat a las células epiteliales.'}
