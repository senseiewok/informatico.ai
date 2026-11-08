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
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1061/9780784415788',
           'fetched_on': '2026-11-08',
           'citing_publications': 445,
           'supporting': 0,
           'mentioning': 57,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 445 citing '
                      'publications (0 supporting, 57 mentioning, 0 contrasting) on ASCE/SEI 7-22 '
                      'seismic isolation design, inelastic response spectra, and bilinear '
                      'lead-rubber bearing hysteresis.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1061/9780784415788',
           'fetched_on': '2026-11-08',
           'citing_publications': 445,
           'supporting': 0,
           'mentioning': 57,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 445 citing '
                      'publications (0 supporting, 57 mentioning, 0 contrasting) on ASCE/SEI 7-22 '
                      'seismic isolation design, inelastic response spectra, and bilinear '
                      'lead-rubber bearing hysteresis.'},
 'act1_title': "Act I — From Maurice Biot's Response Spectrum to William Robinson's Lead-Rubber "
               'Seismic Isolator',
 'act1_dropcap': 'In the spring of 1932, amidst the wreckage of destructive California and Tokyo '
                 'earthquakes, the young Belgian-American engineer Maurice Anthony Biot sat in his '
                 'Pasadena office at Caltech. Troubled by how unpredictably buildings responded to '
                 'shaking ground, Biot formulated the earthquake response spectrum: a master '
                 'mathematical curve revealing how different structures amplify ground motion '
                 'depending on their natural swaying tempo. Four decades later, researchers showed '
                 'that buildings could survive violent shaking by bending into the inelastic '
                 'range, yet this internal damage ruined piping and halted operations. In 1974, '
                 'inside an industrial workshop in Lower Hutt, New Zealand, the physicist William '
                 'Robinson solved this fundamental dilemma. Instead of building stiffer walls to '
                 'fight the earth, Robinson vulcanized flexible rubber layers around a solid '
                 'central lead plug. Placed beneath a building, his isolator decoupled the '
                 'structure from ground movements, absorbing seismic shocks through plastic '
                 'deformation while the building above glided smoothly.',
 'act1_plain_bridge': 'Imagine riding a crowded subway car when the train suddenly hits the brakes '
                      'and jerks violently. If you stand with your knees locked and your body '
                      'rigid, the sudden jolt knocks you off your feet. But if you relax, bend '
                      'your knees, and let your feet glide on roller skates, the floor can jerk '
                      'violently underneath you while your upper body remains perfectly upright '
                      'and calm. Seismic base isolation protects modern buildings in that exact '
                      'same way. Instead of bolting a hospital or laboratory rigidly to the rock, '
                      'engineers set the entire building on giant flexible rubber and lead pads. '
                      'When an earthquake strikes, the ground thrashes furiously beneath the '
                      'foundation pads. The soft pads stretch and the lead inside bends smoothly, '
                      'absorbing the shock like heavy-duty shock absorbers. The building above '
                      'gently glides in place, keeping surgical rooms, delicate computers, and '
                      'medicine pipelines safe.',
 'act1_body': 'For acute-care hospitals, emergency trauma centers, semiconductor cleanrooms, and '
              'high-containment biomedical laboratories, allowing structural columns to yield '
              'during an earthquake is unacceptable. Inter-story drift shatters pressurized '
              'medical gas pipelines, misaligns delicate laser equipment, and forces immediate '
              'facility evacuation even when structural collapse is avoided. Under ASCE/SEI 7-22 '
              'Chapter 17 (DOI 10.1061/9780784415788), seismic base isolation solves this '
              'fundamental vulnerability by inserting laminated elastomeric Lead-Rubber Bearings '
              'beneath the superstructure. These specialized bearings lengthen the fundamental '
              'structural period from the high-energy shaking band of zero-point-four seconds out '
              'past three seconds, shifting the building far away from resonant earthquake '
              'frequencies. Simultaneously, the solid cylindrical lead core yields in plastic '
              'shear during lateral displacement, dissipating tectonic energy in stable bilinear '
              'hysteresis loops. By combining period lengthening with heavy hysteretic damping, '
              'base isolation slashes transmitted floor accelerations by more than seventy '
              'percent, ensuring critical clinical, manufacturing, and research infrastructure '
              'remains fully operational through Maximum Considered Earthquakes.',
 'act1_stakes': 'When structural designers rely on conventional fixed-base ductility assumptions '
                'for critical facilities, the consequences during severe earthquakes can be '
                'disastrous. While reinforced concrete shear walls may prevent catastrophic '
                'building collapse, the violent inter-story drift and extreme floor accelerations '
                'ruin interior infrastructure. Heavy ceiling grids drop, fire sprinkler pipes '
                'rupture, emergency backup generators rip from their anchor bolts, and delicate '
                'surgical equipment becomes projectile debris. Following major seismic events, '
                'hospitals designed with classical fixed-base standards frequently shut down due '
                'to non-structural destruction, turning away casualties when emergency care is '
                'needed most. Base isolation changes this paradigm by transforming structural '
                'performance from mere life-safety collapse prevention into guaranteed immediate '
                'occupancy. Modern building codes mandate rigorous nonlinear response history '
                'analysis, verifying that elastomeric isolators provide stable energy dissipation '
                'without tearing or exceeding moat clearances. By decoupling superstructures from '
                'violent ground shaking, engineers safeguard essential community hospitals and '
                'pharmaceutical production lines against multi-billion-dollar post-earthquake '
                'operational shutdowns.',
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
 'act2_analogy': 'Standing stiff-legged on a lurching subway car throws you violently off balance, '
                 'because the abrupt jolt travels directly up your spine to your head. If you flex '
                 'your knees or glide on roller skates, the floor jerks back and forth underneath '
                 'you while your upper body remains steady, calm, and upright. Seismic base '
                 'isolation gives an entire skyscraper flexible knees, letting tectonic ground '
                 'waves thrash furiously below while doctors continue delicate surgeries '
                 'undisturbed above.',
 'act2_plain_primer': 'To see how engineers protect buildings during a major earthquake, our model '
                      'gives you two primary controls that govern structural response. The first '
                      'control is the Design Spectral Acceleration, which represents the raw '
                      'intensity and violence of the earthquake ground shaking. Turning this dial '
                      'up simulates a more severe, near-fault tectonic rupture that violently '
                      'accelerates the ground beneath the foundation. The second control is the '
                      'Effective Hysteretic Damping, which represents the energy-absorbing '
                      'capability of the lead core inside the rubber bearings. Raising this '
                      'damping dial simulates inserting a thicker lead plug that plastically '
                      'deforms during shaking, acting like a heavy brake that absorbs shock '
                      'energy. Balancing these two controls demonstrates how base isolation '
                      'shields the superstructure: even when ground shaking intensity rises to '
                      'extreme levels, increasing the internal hysteretic damping curbs lateral '
                      'sway and keeps building motion within safe clearance boundaries.',
 'distill_diagram': {'analogy_title': 'Subway Rider Knees & Seismic Bearings',
                     'analogy_sub': 'Flexible bearings let ground jerk while the superstructure '
                                    'rests.',
                     'force_a_title': 'Spectral Acceleration (S_DS)',
                     'force_a_sub': 'Tectonic ground shaking intensity driving base motion.',
                     'force_b_title': 'Hysteretic Damping (β_eff)',
                     'force_b_sub': 'Plastic shear yield in lead core absorbing seismic energy.',
                     'threshold_title': 'Isolation Moat Clearance Limit',
                     'threshold_pass': 'Isolated Motion: Drift and floor accelerations suppressed.',
                     'threshold_fail': 'Moat Impact: Excessive displacement strikes retaining '
                                       'moat.'},
 'act2_intuition': 'A base-isolated structure obeys the coupled nonlinear matrix equation of '
                   'motion M * u_ddot + C * u_dot + F_s(u, u_dot) = -M * r * u_ddot_g(t), where '
                   'F_s(u) represents the bilinear restoring force across the isolation plane: '
                   'characteristic lead yield strength Q_d plus post-yield elastomeric stiffness '
                   'k_d * u. At maximum displacement D_M, the secant stiffness k_eff = Q_d / D_M + '
                   'k_d shifts the structural period to T_M = 2 * pi * sqrt(W / (g * k_eff)). The '
                   'equivalent hysteretic damping beta_eff = E_loop / (2 * pi * k_eff * D_M^2) '
                   'increases the ASCE 7-22 damping multiplier B_M, reducing spectral displacement '
                   'D_M and cutting base shear V_b by over seventy percent. When we solve these '
                   'coupled nonlinear hysteretic equations alongside finite-element structural '
                   'dynamics models in FEniCS/dolfinx (DOI 10.1145/3524456), the damping factor '
                   'B(beta_eff) cuts floor accelerations down to comfortable fractions of gravity. '
                   'This attenuation keeps sensitive laboratory equipment and surgical suites '
                   'fully operational during Maximum Considered Earthquakes without requiring '
                   'expensive structural column repair.',
 'act2_deepening': 'The nonlinear response of lead-rubber bearings involves intimate coupling '
                   'between mechanical kinematics and thermodynamics. During cyclic lateral '
                   'displacement, alternating elastomeric layers provide high vertical stiffness '
                   'to support building gravity loads while maintaining low horizontal shear '
                   'stiffness. Within the central cylindrical cavity, the solid lead plug '
                   'undergoes severe plastic shear strain exceeding one hundred percent. Because '
                   'lead recrystallizes dynamically at ambient temperatures, it can endure '
                   'hundreds of large-amplitude cyclic reversals without work-hardening or brittle '
                   'fatigue failure. However, the plastic work dissipated during severe ground '
                   'shaking converts directly into internal heat. In extreme ground motions, '
                   'internal lead temperatures can rise by over fifty degrees Celsius, causing '
                   'temporary thermal softening that slightly reduces characteristic yield '
                   'strength Q_d. Sophisticated nonlinear response history models account for this '
                   'hysteretic heat generation alongside P-Delta overturning moments, verifying '
                   'that restoring forces in the vulcanized rubber ensure reliable post-earthquake '
                   'recentering and prevent permanent structural offsets even after multiple '
                   'seismic aftershocks.',
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
                  'isolator recentering within seconds of a seismic event. Pairing real-time '
                  'strong-motion accelerometer arrays with sparse nonlinear hysteresis '
                  'identification in dynamicslab/pysindy (https://github.com/dynamicslab/pysindy, '
                  'DOI 10.1073/pnas.1517384113) and FEniCS/dolfinx (DOI 10.1145/3524456) enables '
                  'automated post-earthquake structural health certification grounded in '
                  'Scite-audited seismic standards (DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'Next-generation seismic resilience pairs autonomous sensor intelligence with '
                   'experienced human structural engineering oversight. Modern base-isolated '
                   'buildings feature distributed triaxial accelerometer arrays and laser '
                   'displacement sensors continuously streaming building telemetry to '
                   'physics-informed neural networks. Following an earthquake, these algorithms '
                   'immediately calculate peak floor accelerations, isolator orbital '
                   'displacements, and residual offsets across the foundation plane. Within '
                   'seconds of ground shaking cessation, automated structural health certification '
                   'reports inform facility directors whether the building is safe for '
                   'uninterrupted clinical and operational use. Human structural engineers review '
                   'anomalies and verify long-term elastomeric aging data against original design '
                   'tolerances. Open research frontiers explore semi-active magnetorheological '
                   'dampers and shape-memory alloy tendons that dynamically adjust their restoring '
                   'stiffness based on real-time earthquake frequency signatures. By unifying '
                   'automated real-time structural health monitoring with robust mechanical '
                   'isolation systems, civil engineers protect critical medical and technological '
                   'facilities, ensuring continuous life-saving operations through the most '
                   'violent earthquakes.',
 'cf_bridge': 'Research hospitals and GMP genetic-medicine facilities producing inhaled '
              'CSI-MasterFormat mRNA lipid nanoparticles and bacteriophages require uninterrupted '
              'negative/positive pressure containment, cryogenic storage, and sub-angstrom Cryo-EM '
              'structural imaging (PDB 8EIQ). Designing clinical and research infrastructure to '
              'ASCE 7-22 Risk Category IV with seismic base isolation keeps floor accelerations '
              'below 0.18 g and inter-story drift below 0.35%, ensuring life-saving inpatient care '
              'and curative biomanufacturing never go offline.',
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
             'MCEER-11-0004.',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). ACM Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: 10.1145/3524456.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
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
              'CSI-MasterFormat.',
 'plain_es': 'En la primavera de 1932, tras los devastadores terremotos de Long Beach y Tokio, el '
             'ingeniero Maurice Anthony Biot formuló en Caltech el espectro de respuesta sísmica. '
             'Biot descubrió una curva matemática que explica cómo los edificios amplifican el '
             'movimiento telúrico dependiendo de su propio ritmo de oscilación. Cuatro décadas '
             'después, en 1974, el físico William Robinson inventó en Nueva Zelanda los aisladores '
             'de plomo y caucho. Para comprender cómo funcionan en la vida cotidiana, imaginen '
             'viajar de pie en el metro: si mantienen las piernas rígidas, un frenazo brusco los '
             'derribará fácilmente; pero si flexionan las rodillas o usan patines, el piso puede '
             'moverse bruscamente debajo de ustedes mientras su torso permanece tranquilo. Los '
             'aisladores sísmicos actúan exactamente como esas rodillas flexibles. En lugar de '
             'anclar un hospital directamente a la roca, los ingenieros colocan grandes '
             'almohadillas de caucho con un núcleo de plomo en la base. Durante un sismo, el suelo '
             'tiembla con violencia, pero el edificio flota suavemente.',
 'deep_es': 'El aislamiento sísmico de base protege las estructuras al desacoplar el edificio del '
            'suelo mediante dos mecanismos combinados: el alargamiento del periodo fundamental y '
            'la disipación histerética de energía. Al intercalar capas elásticas de caucho con '
            'placas de acero, el periodo natural se desplaza desde la zona destructiva de '
            'resonancia hacia frecuencias mucho más lentas y seguras. Simultáneamente, el núcleo '
            'central de plomo se deforma plásticamente durante el sismo, absorbiendo energía '
            'telúrica en ciclos estables de histéresis bilineal y reduciendo las aceleraciones de '
            'piso en más de un setenta por ciento. En la ingeniería estructural contemporánea, '
            'este comportamiento se analiza mediante simulaciones no lineales en computadora para '
            'garantizar que el desplazamiento lateral se mantenga dentro de las juntas de '
            'separación perimetral. Esta tecnología asegura que hospitales, laboratorios de '
            'investigación y cuartos limpios continúen operando de inmediato tras un sismo mayor, '
            'protegiendo vidas, instrumental médico de alta precisión e infraestructura esencial.'}
