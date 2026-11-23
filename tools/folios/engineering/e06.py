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
             "Robinson's bilinear lead-rubber seismic isolators help decouple hospitals and "
             'laboratories from ground motion.',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.2',
 'status_badge': 'CIVIL & SEISMIC · REV 1.2',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'M ü + C u̇ + F_s(u) = −M ü_g(t) · V_b = C_s W · μ_Δ = Δ_max / Δ_y',
 'colophon': {'identifier': 'E.06 · Seismic Structural Dynamics · CSI 13 48 00',
              'kernels': 'ASCE 7-22 Ch. 17 · Bilinear LRB Hysteresis · T_M = 2.85 s',
              'benchmarks': 'Model values: D_M = 276 mm and C_s = 0.137 at S_DS = 1.00 g, S_D1 = '
                            '0.60 g, B_M = 1.54',
              'bridge': 'Base-Isolated Buildings ↔ Laboratories and Medicine Facilities (context)'},
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
 'steps': ['Stage 1 (Fixed-Base Response): The page assumes S_D1 = 0.60 S_DS, so at S_DS = '
           '1.00 g the spectral plateau ends at T_s = 0.60 s. An unisolated frame with T_fixed '
           '= 0.65 s sits just past it, at S_a = 0.60/0.65 = 0.92 g.',
           'Stage 2 (Lead-Rubber Period Lengthening, T_M = 2.85 s): Lengthening the period to '
           '2.85 s moves the building onto the 1/T branch, S_a = 0.60/2.85 = 0.21 g, about 77% '
           'below the fixed-base value before any damping is counted.',
           'Stage 3 (Bilinear Lead-Core Hysteretic Energy Dissipation): Plastic shear yielding of '
           'the central lead plug dissipates E_loop = 4 Q_d (D_M − D_y) per cycle. The page '
           'takes β_eff = 22% from the slider rather than computing it from the bearing '
           'properties, and B_M = 1.54 by interpolating 1.5 (20%) and 1.7 (30%).',
           'Stage 4 (Model Check, Not a Code Check): With D_M = g S_D1 T_M / (4π² B_M) the model '
           'gives D_M = 276 mm, inside the assumed 400 mm moat, and C_s = S_D1 / (T_M B_M) = '
           '0.137. Drift, floor acceleration and a full ASCE/SEI 7-22 Chapter 17 design were not '
           'checked.'],
 'readouts': [{'label': 'Isolated Period & Damping', 'value': 'T_M = 2.85 s (B_M = 1.54)'},
              {'label': 'Isolator Displacement D_M', 'value': '276 mm (assumed moat 400 mm)'},
              {'label': 'Seismic Base Shear Ratio', 'value': 'V_b / W = 0.137 (−86% vs S_DS)'},
              {'label': 'Model Verdict', 'value': 'WITHIN ASSUMED MOAT · NOT A CODE CHECK'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 13 48 00 / ASCE 7-22 CH. 17',
                'title': 'Lead-Rubber Bearing (LRB) Seismic Isolation System',
                'body': 'Illustrative design sketch, not a project specification: elastomeric '
                        'base isolation bearings with a cylindrical lead core for an essential '
                        'healthcare building, with design targets T_M ≈ 2.85 s and equivalent '
                        'viscous damping of about 20% or more.',
                'meta': 'Design sketch · ASCE/SEI 7-22 Chapter 17 requires prototype testing of '
                        'isolators; none was done for this page'},
 'sidenote_1': {'kicker': 'SIDENOTE E.06-A · DAMPING FACTOR B_M & DISPLACEMENT',
                'body': 'In the damping-factor table used for isolated structures, B_M = 1.0 at '
                        '5% damping, 1.5 at 20% and 1.7 at 30%; interpolating gives B_M ≈ 1.54 at '
                        '22%. In the displacement formula D_M = (g S T_M)/(4π² B_M), that cuts '
                        'displacement by 1 − 1/1.54 ≈ 35%. Check the current edition of the '
                        'standard for the exact table and which spectral value it uses.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.06-B · SPECIFICATION PLATE · CSI 13 48 00 (SEISMIC '
                          'ISOLATION)',
                'body': 'Design sketch of a 950 mm diameter lead-rubber bearing (170 mm lead '
                        'core, 32 natural rubber layers, Q_d = 185 kN, k_d = 1.45 kN/mm). These '
                        'are illustrative values; no bearing was built or tested.'},
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
                     'Check that the design displacement D_M = (g * S * T_M) / (4 * pi^2 * B_M) '
                     'stays within the moat clearance and that story drift meets the limits of '
                     'the governing code; take the spectral value S, the B_M table and the drift '
                     'limits from the current edition of the standard, not from this skill.']},
 'revisions': [{'edition': 'REV 1.2',
                'date': '2026-11-14',
                'summary': 'REV 1.2 (Redated 2026-11-14): Grounding revision. The readouts were '
                           'recomputed from the stated formula with S_D1 = 0.60 S_DS and B_M = '
                           '1.54 (D_M = 276 mm, not 232 mm; C_s = 0.137, not 0.142), and the '
                           '"immediate occupancy pass", compliance and prototype-testing '
                           'claims were withdrawn because no code check or test was done. The '
                           'claims that isolation keeps facilities "never offline", the '
                           '"curative biomanufacturing" wording were withdrawn, and the invented 1932 '
                           'scene was replaced with plain dates.',
                'opus': 'Review: every DOI in the folio was checked in Crossref and the Scite '
                        'index on 2026-11-14, and the repository names with the GitHub API. No '
                        'response-history or finite-element analysis was run for this folio.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-02',
                'summary': 'REV 1.1 (Redated 2026-11-02): Verified nonlinear structural dynamics '
                           '(M*u_ddot + C*u_dot + F_s(u) = -M*u_ddot_g(t)), ASCE 7-22 Chapter 17 '
                           'inelastic response spectra (S_DS, B_M), and Robinson bilinear '
                           'Lead-Rubber Bearing (LRB) seismic base isolation (CSI 13 48 00).',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): reviewed '
                        'the period-lengthening formulas. The word "Verified" in this note and '
                        'the note below is withdrawn in REV 1.2, as are the drift figure 0.32% '
                        'and the displacement D_M = 232 mm, which did not follow from the page '
                        'formula.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-01',
                'summary': 'REV 1.0 (Published 2026-11-01): Initial 5-Act structural dynamics '
                           'monograph on ASCE 7-22 inelastic response spectra, Robinson '
                           'lead-rubber seismic isolators, and Risk Category IV hospital '
                           'resilience.',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
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
           'summary': 'Scite index entry for ASCE/SEI 7-22 (DOI 10.1061/9780784415788), as '
                      'recorded 2026-11-08: 445 citing publications (0 supporting, 57 '
                      'mentioning, 0 contrasting) and no retraction notice. These counts '
                      'describe that one standard, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1061/9780784415788',
           'fetched_on': '2026-11-08',
           'citing_publications': 445,
           'supporting': 0,
           'mentioning': 57,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for ASCE/SEI 7-22 (DOI 10.1061/9780784415788), as '
                      'recorded 2026-11-08: 445 citing publications (0 supporting, 57 '
                      'mentioning, 0 contrasting) and no retraction notice. These counts '
                      'describe that one standard, not this folio.'},
 'act1_title': "Act I — From Maurice Biot's Response Spectrum to William Robinson's Lead-Rubber "
               'Seismic Isolator',
 'act1_dropcap': 'In his 1932 doctoral work at Caltech, the Belgian-born engineer Maurice '
                 'Anthony Biot introduced the idea behind the earthquake response spectrum: a '
                 'curve showing how strongly simple structures with different natural periods '
                 'respond to a given ground motion. Later work, including Newmark and Hall\'s, '
                 'built design spectra that allow buildings to survive strong shaking by yielding '
                 'into the inelastic range, which protects lives but can leave the building and '
                 'its contents badly damaged. In New Zealand in the 1970s the physicist William '
                 'Robinson developed the lead-rubber bearing: layers of rubber and steel around a '
                 'central lead core, which he described in a 1982 paper (DOI '
                 '10.1002/eqe.4290100408). Placed beneath a building, such bearings lengthen its '
                 'period and dissipate energy as the lead yields.',
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
              'beneath the superstructure. These bearings lengthen the fundamental period from '
              'a fraction of a second to a few seconds (2.85 s on this page), moving the '
              'building away from the periods where typical ground motions are strongest. At the '
              'same time, the lead core yields in shear and dissipates energy in bilinear '
              'hysteresis loops. In this page\'s model, those two effects lower the design base '
              'shear coefficient from 0.92 to 0.137, about 85%. How much a real building\'s '
              'floor accelerations drop depends on the building and the earthquake, and staying '
              'operational also depends on non-structural design.',
 'act1_stakes': 'When structural designers rely on conventional fixed-base ductility assumptions '
                'for critical facilities, the consequences during severe earthquakes can be '
                'disastrous. While reinforced concrete shear walls may prevent catastrophic '
                'building collapse, the violent inter-story drift and extreme floor accelerations '
                'ruin interior infrastructure. Heavy ceiling grids drop, fire sprinkler pipes '
                'rupture, emergency backup generators rip from their anchor bolts, and delicate '
                'surgical equipment can be thrown about. Hospitals can be forced to close after '
                'an earthquake because of non-structural damage even when the structure stands. '
                'Base isolation aims higher than collapse prevention: it seeks to keep the '
                'building usable, though no design guarantees that. Codes for isolated '
                'buildings require the isolators to be tested and the design to show that '
                'displacements stay within the moat clearance. By reducing the shaking passed '
                'to the building, isolation lowers the risk of costly shutdowns for hospitals '
                'and production facilities.',
 'pullquote': '"Instead of fighting the earthquake with brute-force stiffness that amplifies floor '
              'accelerations, seismic base isolation decouples the superstructure from the ground '
              'and shifts the building out of harm\'s resonant frequency band."',
 'chronology': [('1932',
                 'Maurice Biot introduces the mechanical earthquake response spectrum at Caltech.'),
                ('1982',
                 'William H. Robinson publishes the lead-rubber bearing, developed in New Zealand '
                 'in the 1970s (DOI 10.1002/eqe.4290100408).'),
                ('1982',
                 'Nathan Newmark & William Hall codify inelastic design response spectra and '
                 'equal-displacement ductility rules.'),
                ('2022',
                 'ASCE/SEI 7-22 is published; its Chapter 17 sets requirements for seismically '
                 'isolated structures.')],
 'act2_title': 'Act II — How It Actually Works: Equation of Motion, Effective Period T_M & '
               'Bilinear Hysteresis',
 'act2_analogy': 'Standing stiff-legged on a lurching subway car throws you violently off balance, '
                 'because the abrupt jolt travels directly up your spine to your head. If you flex '
                 'your knees or glide on roller skates, the floor jerks back and forth underneath '
                 'you while your upper body remains steady, calm, and upright. Seismic base '
                 'isolation gives a building flexible knees, letting the ground move a great '
                 'deal below while the floors above move much less.',
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
                   'D_M. With the page assumptions (S_D1 = 0.60 g, T_M = 2.85 s, B_M = 1.54), D_M = '
                   '9.81 × 0.60 × 2.85 / (4π² × 1.54) m = 276 mm and C_s = 0.60 / (2.85 × 1.54) = '
                   '0.137. These are equivalent-linear estimates; a real design would also run '
                   'nonlinear response-history analyses, which a reader could set up with a '
                   'structural or finite-element package such as FEniCS/dolfinx (one of its '
                   'method papers: DOI 10.1145/3524456). None was run for this folio.',
 'act2_deepening': 'The nonlinear response of lead-rubber bearings involves intimate coupling '
                   'between mechanical kinematics and thermodynamics. During cyclic lateral '
                   'displacement, alternating elastomeric layers provide high vertical stiffness '
                   'to support building gravity loads while maintaining low horizontal shear '
                   'stiffness. Within the central cylindrical cavity, the solid lead plug '
                   'undergoes severe plastic shear strain exceeding one hundred percent. Because '
                   'lead recrystallizes dynamically at ambient temperatures, it can endure '
                   'hundreds of large-amplitude cyclic reversals without work-hardening or brittle '
                   'fatigue failure. However, the plastic work dissipated during severe ground '
                   'shaking converts directly into internal heat. Under repeated large cycles the '
                   'lead core heats up, which lowers its characteristic strength Q_d and the '
                   'energy dissipated per cycle; tests reported in the literature have recorded '
                   'core temperatures well above 100 °C (reviewed by Yang et al. 2026, Polymers, '
                   'DOI 10.3390/polym18111306). Nonlinear response-history models can include '
                   'this heating along with P-Delta effects, and designers check that the rubber '
                   'provides enough restoring force for the building to recenter, limiting '
                   'permanent offsets.',
 'walkthrough': ['Experiment 1 (Spectral Acceleration Demand): Increase Design Spectral '
                 'Acceleration S_DS from 0.60 g to 1.60 g. Watch isolator displacement D_M and '
                 'base shear ratio V_b/W update live while the bilinear hysteresis loop expands.',
                 'Experiment 2 (Supplemental Hysteretic Damping): Increase Effective Damping Ratio '
                 'beta_eff from 8% to 28%. Observe the ASCE 7-22 damping factor B_M climb, '
                 'suppressing isolator drift D_M within the 400 mm moat clearance.',
                 'Experiment 3 (4-Stage Dynamic Stepper): Click Stages 1 to 4 to trace fixed-base '
                 'resonance amplification, LRB period lengthening, lead-core plastic hysteresis, '
                 'and the model displacement and base-shear check (not a code check).'],
 'act4_title': 'Act IV — Real-Time Structural Health Monitoring & the Structural & Civil '
               'Engineering Specification Bridge',
 'act4_human_ai': 'A proposal, not a description of deployed systems: accelerometers above and '
                  'below the isolation plane could feed a Bouc–Wen hysteresis model to estimate '
                  'isolator displacement and recentering after an earthquake, giving engineers a '
                  'quick first look before inspection. A reader could explore this with sparse '
                  'identification (dynamicslab/pysindy, https://github.com/dynamicslab/pysindy, '
                  'DOI 10.1073/pnas.1517384113) or the FEniCS/dolfinx finite-element library (one '
                  'of its method papers: DOI 10.1145/3524456). Neither was run for this folio, '
                  'and safety decisions after an earthquake belong to qualified engineers. '
                  'References were checked in the Scite index (DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'Looking ahead, and offered as a research direction: base-isolated buildings '
                   'can be instrumented with accelerometers and displacement sensors, and '
                   'algorithms could estimate peak floor accelerations, isolator displacements '
                   'and residual offsets soon after shaking stops. Such estimates could help '
                   'engineers decide where to inspect first; they would not replace inspection '
                   'or a decision by a qualified engineer about whether a building is safe to '
                   'use. Engineers also review long-term rubber aging against design '
                   'tolerances. Open research frontiers explore semi-active magnetorheological '
                   'dampers and shape-memory alloy tendons that dynamically adjust their restoring '
                   'stiffness based on real-time earthquake frequency signatures. By unifying '
                   'automated real-time structural health monitoring with robust mechanical '
                   'isolation systems, civil engineers aim to help medical and technological '
                   'facilities keep working after strong earthquakes, while accepting that no '
                   'system removes the risk.',
 'sources': ['ASCE/SEI 7-22 (2022). Minimum Design Loads and Associated Criteria for Buildings and '
             'Other Structures, Chapter 17: Seismic Design Requirements for Seismically Isolated '
             'Structures. American Society of Civil Engineers. DOI: 10.1061/9780784415788.',
             'Robinson, W. H. (1982). Lead-rubber hysteretic bearings suitable for protecting '
             'structures during earthquakes. Earthquake Engineering & Structural Dynamics, 10(4), '
             '593–604. DOI: 10.1002/eqe.4290100408.',
             'Yang, F., Zhang, L., Pang, H., & Jiang, T. (2026). Influence of Temperature on the '
             'Mechanical Behavior of Lead/Rubber Bearings. Polymers, 18(11), 1306. DOI: '
             '10.3390/polym18111306.',
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
        '(T=0.65 s · 0.92g)</text>\n'
        '            <text x="165" y="142" font-size="9.5" fill="var(--tp-verdigris)">Isolated T_M '
        '= 2.85 s (C_s = 0.137)</text>\n'
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
 'body': "Building on Maurice Biot's 1932 response spectrum and William Robinson's lead-rubber "
         'bearing (1982, DOI 10.1002/eqe.4290100408), ASCE/SEI 7-22 (DOI 10.1061/9780784415788) '
         'sets requirements for seismically isolated structures in its Chapter 17. In this '
         "page's equivalent-linear model, isolating a building at T_M = 2.85 s with 22% damping "
         'lowers the base shear coefficient from 0.92 to 0.137.'}

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
 'plain_es': 'En su trabajo doctoral de 1932 en Caltech, el ingeniero de origen belga Maurice '
             'Anthony Biot introdujo la idea del espectro de respuesta sísmica: una curva que '
             'muestra cuánto responden estructuras sencillas con distintos periodos naturales a '
             'un mismo movimiento del suelo. En la década de 1970, el físico William Robinson '
             'desarrolló en Nueva Zelanda los aisladores de plomo y caucho, que describió en un '
             'artículo de 1982. Para comprender cómo funcionan en la vida cotidiana, imaginen '
             'viajar de pie en el metro: si mantienen las piernas rígidas, un frenazo brusco los '
             'derribará fácilmente; pero si flexionan las rodillas o usan patines, el piso puede '
             'moverse bruscamente debajo de ustedes mientras su torso permanece tranquilo. Los '
             'aisladores sísmicos actúan exactamente como esas rodillas flexibles. En lugar de '
             'anclar un hospital directamente a la roca, los ingenieros colocan grandes '
             'almohadillas de caucho con un núcleo de plomo en la base. Durante un sismo, el suelo '
             'tiembla con violencia, pero el edificio se mueve mucho menos.',
 'deep_es': 'El aislamiento sísmico de base protege las estructuras al desacoplar el edificio del '
            'suelo mediante dos mecanismos combinados: el alargamiento del periodo fundamental y '
            'la disipación histerética de energía. Al intercalar capas elásticas de caucho con '
            'placas de acero, el periodo natural se desplaza desde la zona destructiva de '
            'resonancia hacia frecuencias mucho más lentas y seguras. Simultáneamente, el núcleo '
            'central de plomo se deforma plásticamente durante el sismo, absorbiendo energía '
            'telúrica en ciclos de histéresis bilineal. En el modelo equivalente lineal de esta '
            'página, el coeficiente de cortante basal baja de 0.92 a 0.137 y el desplazamiento '
            'del aislador es de 276 mm. En la ingeniería estructural, este comportamiento se '
            'analiza además con simulaciones no lineales para comprobar que el desplazamiento se '
            'mantenga dentro de la junta perimetral. El aislamiento ayuda a que hospitales y '
            'laboratorios sigan funcionando tras un sismo fuerte, aunque ningún sistema elimina '
            'el riesgo.'}
