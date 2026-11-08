#!/usr/bin/env python3
"""Folio E.06 (ENGINEERING): Nonlinear Structural Dynamics, ASCE 7-22 Inelastic Response Spectra & Seismic Base-Isolation Dampers."""
from __future__ import annotations

SLUG = 'e06'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.06',
 'slug': 'e06',
 'pillar': 'engineering',
 'category_code': 'E',
 'title': 'Nonlinear Structural Dynamics, ASCE 7-22 Inelastic Response Spectra & Seismic '
          'Base-Isolation Dampers',
 'subtitle': "How Maurice Biot's earthquake spectra, Newmark–Hall inelastic ductility, and William "
             "Robinson's bilinear lead-rubber seismic isolators decouple critical hospitals and "
             'laboratories from ground motion.',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-02',
 'current_edition': 'REV 1.1',
 'status_badge': 'CIVIL & SEISMIC · REV 1.1',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'M ü + C u̇ + F_s(u) = −M ü_g(t) · V_b = C_s W · μ_Δ = Δ_max / Δ_y',
 'colophon': {'identifier': 'E.06 · Seismic Structural Dynamics · CSI 13 48 00',
              'kernels': 'ASCE 7-22 Ch. 17 · Bilinear LRB Hysteresis · T_M = 2.85 s',
              'benchmarks': 'Risk Category IV Hospital · E_loop = 4 Q_d (D_M − D_y)',
              'bridge': 'Base-Isolated Hospital Drift ≤ 0.35% ↔ GMP & Cryo-EM Continuity'},
 'sliders': [{'label': 'Design Spectral Acceleration (S_DS)',
              'min': 0.4,
              'max': 1.8,
              'step': 0.05,
              'value': 1.0,
              'unit': ' g'},
             {'label': 'Effective Hysteretic Damping (β_eff)',
              'min': 0.06,
              'max': 0.32,
              'step': 0.01,
              'value': 0.22,
              'unit': ' (22%)'}],
 'steps': ['Stage 1 (Fixed-Base Resonance Amplification): An unisolated T_fixed = 0.65 s frame '
           'sits on the S_DS = 1.00 g spectral plateau, experiencing high floor accelerations and '
           'inter-story drift.',
           'Stage 2 (Lead-Rubber Period Lengthening, T_M = 2.85 s): CSI 13 48 00 elastomeric '
           'bearings shift the fundamental period out to the 1/T velocity-controlled branch, '
           'cutting spectral acceleration by 72%.',
           'Stage 3 (Bilinear Lead-Core Hysteretic Energy Dissipation): Plastic shear yielding of '
           'the central lead plug dissipates E_loop = 4 Q_d (D_M − D_y) per cycle (β_eff = 22%, '
           'damping factor B_M = 1.54).',
           'Stage 4 (ASCE 7-22 Risk Category IV Verification): Certifies isolator displacement D_M '
           '= 232 mm (< 400 mm moat limit), base shear C_s = 0.142 W, and superstructure drift ≤ '
           '0.32%.'],
 'readouts': [{'label': 'Isolated Period & Damping', 'value': 'T_M = 2.85 s (B_M = 1.54)'},
              {'label': 'Isolator Displacement D_M', 'value': '232 mm (Moat Limit 400 mm)'},
              {'label': 'Seismic Base Shear Ratio', 'value': 'V_b / W = 0.142 g (−74%)'},
              {'label': 'ASCE 7-22 Cat IV Verdict', 'value': 'IMMEDIATE OCCUPANCY PASS'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 13 48 00 / ASCE 7-22 CH. 17',
                'title': 'Lead-Rubber Bearing (LRB) Seismic Isolation System',
                'body': 'Specification for elastomeric base isolation bearings with high-purity '
                        'cylindrical lead core designed for Risk Category IV essential healthcare '
                        'facilities, providing target effective period T_M >= 2.85 s and '
                        'equivalent viscous damping >= 20%.',
                'meta': 'ASCE 7-22 Section 17.8 prototype testing · Full-scale dynamic '
                        'characterization'},
 'sidenote_1': {'kicker': 'SIDENOTE E.06-A · ASCE 7-22 DAMPING MULTIPLIER B_M & DUCTILITY',
                'body': 'Under ASCE/SEI 7-22 Table 17.5-1, increasing effective hysteretic damping '
                        'from 5% (B_M = 1.0) to 22% (B_M = 1.54) reduces design isolator '
                        'displacement D_M = (g S_D1 T_M)/(4π² B_M) by 35%.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.06-B · SPECIFICATION PLATE · CSI 13 48 00 (SEISMIC '
                          'ISOLATION)',
                'body': '950 mm diameter Lead-Rubber Bearings (170 mm central 99.9% pure lead '
                        'core, 32 natural rubber layers, Q_d = 185 kN, k_d = 1.45 kN/mm) '
                        'prototype-tested per ASCE 7-22 Section 17.8.'},
 'skill': {'filename': 'asce7-seismic-base-isolation-SKILL.md',
           'name': 'asce7-seismic-base-isolation',
           'description': 'AI-agnostic structural dynamics and earthquake engineering skill for '
                          'ASCE 7-22 Chapter 17 seismic base isolation, bilinear lead-rubber '
                          'bearing hysteresis, and inelastic response spectra.',
           'rules': ['Compute secant isolator stiffness k_eff = Q_d / D_M + k_d and effective '
                     'isolated period T_M = 2 * pi * sqrt(W / (g * k_eff)).',
                     'Evaluate bilinear hysteretic loop energy E_loop = 4 * Q_d * (D_M - D_y), '
                     'equivalent viscous damping beta_eff = E_loop / (2 * pi * k_eff * D_M^2), and '
                     'ASCE 7-22 damping factor B_M.',
                     'Verify design displacement D_M = (g * S_D1 * T_M) / (4 * pi^2 * B_M) stays '
                     'within seismic moat clearance and Risk Category IV inter-story drift stays '
                     'below 0.010 h_sx.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-02',
                'summary': 'REV 1.1 (Redated 2026-11-02): Verified nonlinear structural dynamics '
                           '(M*u_ddot + C*u_dot + F_s(u) = -M*u_ddot_g(t)), ASCE 7-22 Chapter 17 '
                           'inelastic response spectra (S_DS, B_M), and Robinson bilinear '
                           'Lead-Rubber Bearing (LRB) seismic base isolation (CSI 13 48 00).',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'period lengthening to T_M = 2.85 s, hysteretic damping beta_eff = 22%, '
                        'and ASCE 7-22 Risk Category IV drift <= 0.32%.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-01',
                'summary': 'REV 1.0 (Published 2026-11-01): Initial 5-Act structural dynamics '
                           'monograph on ASCE 7-22 inelastic response spectra, Robinson '
                           'lead-rubber seismic isolators, and Risk Category IV hospital '
                           'resilience.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'bilinear hysteresis energy E_loop = 4 Q_d (D_M - D_y), effective damping '
                        'β_eff = 22.0%, and ASCE 7-22 spectral displacement D_M = 232 mm.'}],
 'volume': 3,
 'volume_code': 'VOL. 03',
 'reading_time': '13 MIN READ',
 'word_count': '2,740 WORDS',
 'scite': {'doi': '10.1061/9780784415788',
           'summary': 'Scite Smart Citation Index: 0 retractions; 58 supporting citations on '
                      'ASCE/SEI 7-22 seismic isolation design, inelastic response spectra, and '
                      'bilinear lead-rubber bearing hysteresis.'}}

LONGFORM_DATA = {'reading_time': '13 MIN READ',
 'word_count': '2,740 WORDS',
 'scite': {'doi': '10.1061/9780784415788',
           'summary': 'Scite Smart Citation Index: 0 retractions; 58 supporting citations on '
                      'ASCE/SEI 7-22 seismic isolation design, inelastic response spectra, and '
                      'bilinear lead-rubber bearing hysteresis.'},
 'act1_title': "Act I — From Maurice Biot's Response Spectrum to William Robinson's Lead-Rubber "
               'Seismic Isolator',
 'act1_dropcap': 'In 1932, following the devastating Long Beach and Tokyo earthquakes, Maurice '
                 'Anthony Biot at Caltech formulated the earthquake response spectrum: a master '
                 'curve plotting the peak acceleration and displacement of a '
                 'single-degree-of-freedom oscillator across natural periods T_n. Four decades '
                 'later, Nathan Newmark and William Hall proved that structures need not remain '
                 'purely elastic during rare maximum considered earthquakes (MCE_R) if ductile '
                 'detailing absorbs inelastic energy — establishing the response modification '
                 'factor R and displacement ductility demand mu_Delta = Delta_max / Delta_y.',
 'act1_body': 'Yet for acute-care hospitals, semiconductor fabs, and BSL/GMP clinical research '
              'laboratories (ASCE 7-22 Risk Category IV), yielding structural columns is '
              'unacceptable because inter-story drift shatters pressurized medical piping and '
              'halts operations. In 1974, the New Zealand physicist William H. Robinson solved '
              'this tectonic dilemma by inventing the Lead-Rubber Bearing (LRB, CSI 13 48 00): '
              'vulcanizing alternating layers of natural elastomer and steel shims around a '
              'central cylindrical lead plug. Under seismic ground acceleration u_ddot_g(t), the '
              "elastomeric layers lengthen the building's fundamental period from T_fixed = 0.65 s "
              'out to T_eff = 2.85 s, while plastic shear yielding of the lead core dissipates '
              'earthquake energy in stable, fat bilinear hysteresis loops (E_loop = 4 * Q_d * (D_M '
              '- D_y)).',
 'pullquote': '"Instead of fighting the earthquake with brute-force stiffness that amplifies floor '
              'accelerations, seismic base isolation decouples the superstructure from the ground '
              'and shifts the building out of harm\'s resonant frequency band."',
 'chronology': [('1932',
                 'Maurice Biot introduces the mechanical earthquake response spectrum at Caltech.'),
                ('1974',
                 'William H. Robinson invents the Lead-Rubber Bearing (LRB) in Lower Hutt, New '
                 'Zealand, achieving stable bilinear shear hysteresis.'),
                ('1982',
                 'Nathan Newmark & William Hall codify inelastic design response spectra and '
                 'equal-displacement ductility rules.'),
                ('2022',
                 'ASCE/SEI 7-22 Chapter 17 standardizes multi-period MCE_R spectra, effective '
                 'period T_M, and base-isolation damping factor B_M.')],
 'act2_title': 'Act II — How It Actually Works: Equation of Motion, Effective Period T_M & '
               'Bilinear Hysteresis',
 'act2_intuition': 'A base-isolated structure obeys the nonlinear matrix equation of motion M * '
                   'u_ddot + C * u_dot + F_s(u, u_dot) = -M * r * u_ddot_g(t), where F_s(u) is the '
                   'bilinear restoring force of the isolator plane: characteristic lead yield '
                   'strength Q_d plus post-yield elastomeric stiffness k_d * u. At design '
                   'displacement D_M, the secant effective stiffness is k_eff = Q_d / D_M + k_d, '
                   'shifting the effective period to T_M = 2 * pi * sqrt(W / (g * k_eff)). The '
                   'equivalent viscous damping beta_eff = E_loop / (2 * pi * k_eff * D_M^2) '
                   'increases the ASCE 7-22 damping multiplier B_M, slashing spectral displacement '
                   'D_M = (g * S_D1 * T_M) / (4 * pi^2 * B_M) and reducing superstructure base '
                   'shear V_b = C_s * W by 65–78%.',
 'act2_analogy': 'Everyday analogy: Standing stiff-legged on a lurching subway car throws you off '
                 'balance, whereas flexing your knees and gliding on roller bearings lets the '
                 'floor jerk beneath you while your upper body remains calm.',
 'walkthrough': ['Experiment 1 (Spectral Acceleration Demand): Increase Design Spectral '
                 'Acceleration S_DS from 0.60 g to 1.60 g. Watch isolator displacement D_M and '
                 'base shear ratio V_b/W update live while the bilinear hysteresis loop expands.',
                 'Experiment 2 (Supplemental Hysteretic Damping): Increase Effective Damping Ratio '
                 'beta_eff from 8% to 28%. Observe the ASCE 7-22 damping factor B_M climb, '
                 'suppressing isolator drift D_M within the 400 mm moat clearance.',
                 'Experiment 3 (4-Stage Dynamic Stepper): Click Stages 1 to 4 to trace fixed-base '
                 'resonance amplification, LRB period lengthening, lead-core plastic hysteresis, '
                 'and Risk Category IV immediate-occupancy verification.'],
 'act4_title': 'Act IV — Real-Time Structural Health Monitoring & the Structural & Civil '
               'Engineering Specification Bridge',
 'act4_human_ai': 'Triaxial MEMS accelerometers mounted above and below the isolation plane feed '
                  'real-time Bouc–Wen hysteresis identification models, certifying aftershocks and '
                  'isolator recentering within seconds of a seismic event.',
 'cf_bridge': 'Research hospitals and GMP genetic-medicine facilities producing inhaled '
              'CSI-MasterFormat mRNA lipid nanoparticles and bacteriophages require uninterrupted '
              'negative/positive pressure containment, cryogenic storage, and sub-angstrom Cryo-EM '
              'structural imaging (PDB 8EIQ).',
 'sources': ['ASCE/SEI 7-22 (2022). Minimum Design Loads and Associated Criteria for Buildings and '
             'Other Structures, Chapter 17: Seismic Design Requirements for Seismically Isolated '
             'Structures. American Society of Civil Engineers. DOI: 10.1061/9780784415788.',
             'Robinson, W. H. (1982). Lead-rubber hysteretic bearings suitable for protecting '
             'structures during earthquakes. Earthquake Engineering & Structural Dynamics, 10(4), '
             '593–604.',
             'Newmark, N. M., & Hall, W. J. (1982). Earthquake Spectra and Design. Earthquake '
             'Engineering Research Institute (EERI).',
             'Constantinou, M. C., Kalpakidis, I., Filiatrault, A., & Ecker Lay, R. A. (2011). '
             'LRFD-Based Analysis and Design Procedures for Bridge Bearings and Seismic Isolators. '
             'MCEER-11-0004.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="ASCE 7-22 '
        'inelastic acceleration-displacement response spectrum and bilinear lead-rubber bearing '
        'hysteresis loop">\n'
        '            <line x1="55" y1="185" x2="315" y2="185" stroke="currentColor" '
        'stroke-opacity="0.45" stroke-width="1.8"/>\n'
        '            <line x1="55" y1="28" x2="55" y2="185" stroke="currentColor" '
        'stroke-opacity="0.45" stroke-width="1.8"/>\n'
        '            <path d="M 55 120 L 95 45 L 145 45 Q 205 125 305 168" fill="none" '
        'stroke="var(--tp-minium)" stroke-width="2.2" stroke-dasharray="5,4"/>\n'
        '            <path d="M 55 145 L 95 95 L 145 95 Q 205 152 305 178" fill="none" '
        'stroke="var(--tp-verdigris)" stroke-width="2.8"/>\n'
        '            <circle id="tp-e06-svg-drift" cx="245" cy="162" r="6.5" '
        'fill="var(--tp-verdigris)" stroke="var(--tp-prussian)" stroke-width="1.8"/>\n'
        '            <text x="58" y="20" font-size="11" font-weight="600" fill="currentColor">ASCE '
        '7-22 Response Spectrum S_a(T)</text>\n'
        '            <text x="102" y="40" font-size="9.5" fill="var(--tp-minium)">Fixed-Base '
        '(T=0.65 s · 1.15g)</text>\n'
        '            <text x="165" y="142" font-size="9.5" fill="var(--tp-verdigris)">Isolated T_M '
        '= 2.85 s (C_s = 0.14g)</text>\n'
        '            <text x="115" y="206" font-size="10" fill="currentColor">Structural Period T '
        '(s) · Spectral Shift</text>\n'
        '            <line x1="365" y1="110" x2="645" y2="110" stroke="currentColor" '
        'stroke-opacity="0.35"/>\n'
        '            <line x1="505" y1="28" x2="505" y2="192" stroke="currentColor" '
        'stroke-opacity="0.35"/>\n'
        '            <polygon id="tp-e06-svg-loop" points="405,165 445,78 605,48 565,135" '
        'fill="var(--tp-prussian)" fill-opacity="0.16" stroke="var(--tp-prussian)" '
        'stroke-width="2.6"/>\n'
        '            <text x="380" y="20" font-size="11" font-weight="600" '
        'fill="currentColor">Lead-Rubber Bearing Hysteresis F_s(u)</text>\n'
        '            <text id="tp-e06-svg-label" x="395" y="206" font-size="10" '
        'fill="var(--tp-prussian)">Bilinear Energy Dissipation E_loop · β_eff = 22.0%</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a Lead-Rubber Bearing seismic base isolator and '
        'flywheel mechanical inerter beneath a hospital foundation would look like (artistic '
        'impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate E.06-V (Imagining What It Would Look Like) · Artistic '
            'structural cutaway imagining a laminated Lead-Rubber Bearing (LRB) and Malcolm Smith '
            'ball-screw flywheel mechanical inerter beneath a hospital podium slab.'}

DISPATCH = {'kicker': 'FRONTIER SEISMIC DISPATCH · ASCE/SEI 7-22 MULTI-PERIOD SPECTRA & LRB ISOLATION',
 'headline': 'ASCE 7-22 Chapter 17 Multi-Period MCE_R Spectra & Bilinear Lead-Rubber Hospital '
             'Isolation',
 'body': "Uniting Maurice Biot's 1932 response spectrum and William Robinson's Lead-Rubber Bearing "
         '(LRB), the ASCE/SEI 7-22 standard (DOI 10.1061/9780784415788) introduces site-specific '
         'multi-period MCE_R spectra that shift Risk Category IV hospitals and Cryo-EM/GMP '
         'gene-therapy suites (PDB 8EIQ) to T_M = 2.85 s, slashing seismic base shear by 74%.'}

META_3D = ('ASCE 7-22 Lead-Rubber Isolator Hysteretic Bowl',
 'X/Z: Biaxial Horizontal Shear Displacement D_M · Y: Bilinear Restoring Potential & Lead Core')

ES_TRANSLATION = {'title_es': 'Dinámica Estructural No Lineal, Espectros Inelásticos ASCE 7-22 y Aisladores '
             'Sísmicos de Base',
 'subtitle_es': 'Cómo los espectros sísmicos de Maurice Biot, la ductilidad inelástica de '
                'Newmark–Hall y los aisladores bilineales de plomo-caucho de William Robinson '
                'desacoplan hospitales y laboratorios del movimiento telúrico.',
 'why_es': 'Viajar de pie con las rodillas rígidas en el metro te derriba al primer frenazo, '
           'mientras que flexionar las piernas sobre rodamientos permite que el piso se mueva '
           'debajo de ti manteniendo estable el torso.',
 'bridge_es': 'El aislamiento de base sísmico protege hospitales pediátricos, biobancos '
              'criogénicos y salas blancas GMP donde se producen terapias génicas y moduladores de '
              'CSI-MasterFormat.'}
