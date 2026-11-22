#!/usr/bin/env python3
"""Folio E.07 (ENGINEERING): Long-Span Suspension Bridge Aeroelastic Flutter, Scanlan Derivatives & Physics-Informed Neural Network (PINN) Digital Twins."""
from __future__ import annotations

SLUG = 'e07'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.07',
 'slug': 'e07',
 'pillar': 'engineering',
 'category_code': 'E',
 'title': 'Long-Span Suspension Bridge Aeroelastic Flutter, Scanlan Derivatives & Physics-Informed '
          'Neural Network (PINN) Digital Twins',
 'subtitle': "How Robert Scanlan's motion-dependent flutter derivatives describe the stability of a twin-box bridge girder in strong wind, paired with a design study of Physics-Informed Neural Network virtual sensing from sparse accelerometers.",
 'date_published': '2026-11-02',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'CIVIL & BRIDGE WIND · REV 1.1',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'ζ_net = ζ_s − (ρ B⁴ / 2 I_α) A_2*(K) · L_total = L_data + λ_pde ‖R_pde‖² · CSI '
                  '05 12 00',
 'colophon': {'identifier': 'E.07 · Bridge Aeroelastic Flutter & PINN SHM · CSI 05 12 00',
              'kernels': 'Scanlan Flutter Derivatives A_2*(K), H_1*(K) · Euler–Bernoulli PINN Loss',
              'benchmarks': 'Illustrative model values: U_crit = 76.4 m/s · PINN stress error 1.42% (8 sensors; no network trained)',
              'bridge': 'Sparse Bridge Accelerometer PINNs'},
 'sliders': [{'label': 'Mean Wind Velocity (U_wind)',
              'min': 20.0,
              'max': 85.0,
              'step': 1.0,
              'value': 52.0,
              'unit': ' m/s'},
             {'label': 'PINN Physics Loss Weight (λ_pde)',
              'min': 0.1,
              'max': 2.0,
              'step': 0.05,
              'value': 1.0,
              'unit': 'λ = '}],
 'steps': ['Stage 1 (Modal Kinematics): Model 2,100 m span (B = 36 m) with heave h(x,t) (f_h = 0.095 Hz) and torsion α(x,t) (f_α = 0.235 Hz); illustrative values, not a surveyed bridge.',
           'Stage 2 (Scanlan Derivatives): Under 1971 2B² moment scaling with per-span I_α, A_2*(K) < 0 keeps the vented twin-box model stable up to an illustrative U_crit = 76.4 m/s.',
           'Stage 3 (Proposed PINN Residual): Penalizing non-dimensionalized beam and Saint-Venant PDE residuals R_pde could aid 8-sensor stress estimation; untested, no network trained.',
           'Stage 4 (Proposed Weld Fatigue Check): Estimated rib-to-deck weld stress ranges could be compared against AASHTO LRFD fatigue provisions; no code check is run.'],
 'readouts': [{'label': 'Reduced Wind Velocity U/(f_α B)', 'value': '6.15 (U = 52.0 m/s, B = 36 m)'},
              {'label': 'Net Torsional Damping (ζ_net)', 'value': '+2.84% (illustrative; U_crit = 76.4 m/s)'},
              {'label': 'PINN Virtual Stress Error', 'value': '1.42% (illustrative; λ_pde = 1.00)'},
              {'label': 'Bridge Aeroelastic Verdict', 'value': 'STABLE IN MODEL (ζ_net > 0)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 05 12 00 / AASHTO LRFD',
                'title': 'Streamlined Twin-Box Orthotropic Steel Bridge Girder & Fiber-Bragg PINN '
                         'Digital Twin',
                'body': 'Design study: vented twin-box steel girder with a 6.0 m central slot, '
                        'fairings, and an 8-station accelerometer and fiber-Bragg-grating array '
                        'paired with a proposed PINN monitor.',
                'meta': 'Design study · U_crit = 76.4 m/s is a model value, not a wind-tunnel result · no code compliance is claimed'},
 'sidenote_1': {'kicker': 'SIDENOTE E.07-A · WHY TACOMA NARROWS WAS FLUTTER, NOT SIMPLE VORTEX '
                          'RESONANCE',
                'body': 'Vortex shedding occurs near f_s = St · U / D (about 1 Hz at 19 m/s), whereas Tacoma Narrows twisted near 0.2 Hz. Billah & Scanlan (1991, DOI 10.1119/1.16590) attribute the collapse to self-excited torsional flutter (A_2*(K) > 0).'},
 'sidenote_2': {'kicker': 'SIDENOTE E.07-B · SPECIFICATION PLATE · CSI 05 12 00 / PINN VIRTUAL '
                          'SENSING',
                'body': 'Penalizing bending E I ∂⁴h/∂x⁴ − H_w ∂²h/∂x² + m ∂²h/∂t² − L_aero(x,t) and torsion I_α ∂²α/∂t² − G J ∂²α/∂x² − M_ae(x,t) might curb unphysical curvature spikes between sparse sensors if wind loads are estimated.'},
 'skill': {'filename': 'bridge-flutter-pinn-twin-SKILL.md',
           'name': 'bridge-flutter-pinn-twin',
           'description': 'AI-agnostic structural and wind civil engineering skill for Scanlan '
                          'bridge aeroelastic flutter derivatives, critical wind speed U_crit, and '
                          'Physics-Informed Neural Network (PINN) virtual stress sensing.',
           'rules': ['Compute U_red = U / (f_alpha * B) and K = B * omega / U = 2 * pi / U_red.',
                     'Under Scanlan 1971 2B^2 moment scaling (per-span I_alpha in kg*m^2/m), '
                     'evaluate zeta_net = zeta_s - (rho * B^4 / (2 * I_alpha)) * A_2*^(1971)(K) = '
                     'zeta_s - (rho * B^4 / (4 * I_alpha)) * A_2*^(1996)(K) with A_2*^(1996) = 2 * '
                     'A_2*^(1971); flutter starts at zeta_net <= 0.',
                     'Weight non-dimensionalized bending (E I ∂⁴h/∂x⁴ − H_w ∂²h/∂x² + m ∂²h/∂t² − '
                     'L_aero) and torsion (I_α ∂²α/∂t² − G J ∂²α/∂x² − M_ae) residuals in L_total = '
                     'L_data + λ_pde ‖R_pde‖²; unmeasured wind makes sparse inversion ill-posed.',
                     'State that these are explanatory single-mode relations with illustrative constants: '
                     'not a design or assessment method, and no value here applies to a real bridge.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. U_crit = 76.4 m/s, net damping +2.84% and the 1.42% PINN error are now labeled as illustrative model values: no wind-tunnel test was run and no network was trained, and the claims of wind-tunnel verification and AASHTO LRFD compliance are withdrawn. The Tacoma Narrows account is cut back to the documented record and cites Scanlan & Tomko 1971 (DOI 10.1061/JMCEA3.0001526) and Billah & Scanlan 1991 (DOI 10.1119/1.16590). Statements that such digital twins are deployed are now written as proposals. A grounding pass on 2026-11-21 added six references (Sarkar et al. 1994, Jain et al. 1996, Chan et al. 2006, Ya et al. 2011, Yang et al. 2015, Al-Adly & Kripakaran 2024), stated the two moment-scaling conventions, and said which readouts are fixed.',
                'opus': 'Review: DOIs checked in Crossref and Scite (2026-11-14; expanded 2026-11-21), with Scanlan 2B² moment scaling and slider readouts stated.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-02',
                'summary': 'REV 1.0 (Published 2026-11-02): Inaugural Volume IV civil structural & '
                           'wind engineering monograph uniting Scanlan aeroelastic flutter '
                           'derivatives with Raissi-Perdikaris-Karniadakis PINN bridge digital '
                           'twins (DOI 10.1016/j.jcp.2018.10.045).',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'U_crit = 76.4 m/s twin-box flutter boundary and 1.42% PINN virtual '
                        'sensing error at lambda_pde = 1.00. The word "Verified" is withdrawn in REV 1.1: both figures are illustrative model values.'}],
 'volume': 4,
 'volume_code': 'VOL. 04',
 'reading_time': '22 MIN READ',
 'word_count': '5,250 WORDS',
 'scite': {'doi': '10.1016/j.jcp.2018.10.045',
           'fetched_on': '2026-11-21',
           'citing_publications': 25907,
           'supporting': 65,
           'mentioning': 13014,
           'contrasting': 4,
           'retracted': False,
           'summary': 'Scite index entry for Raissi, Perdikaris & Karniadakis 2019 (DOI 10.1016/j.jcp.2018.10.045), fetched 2026-11-21: 25,907 citing publications (65 supporting, 13,014 mentioning, 4 contrasting) and no retraction notice. These counts describe that one paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '5,250 WORDS',
 'scite': {'doi': '10.1016/j.jcp.2018.10.045',
           'fetched_on': '2026-11-21',
           'citing_publications': 25907,
           'supporting': 65,
           'mentioning': 13014,
           'contrasting': 4,
           'retracted': False,
           'summary': 'Scite index entry for Raissi, Perdikaris & Karniadakis 2019 (DOI 10.1016/j.jcp.2018.10.045), fetched 2026-11-21: 25,907 citing publications (65 supporting, 13,014 mentioning, 4 contrasting) and no retraction notice. These counts describe that one paper, not this folio.'},
 'act1_title': 'Act I — From Tacoma Narrows to Multi-Kilometer Suspension Spans & Physics-Informed '
               'Bridge Digital Twins',
 'act1_dropcap': 'On November 7, 1940, four months after it opened, the first Tacoma Narrows '
                 'Bridge twisted apart in a wind of about 19 meters per second, or 42 miles per '
                 'hour. Newspaper editor Leonard Coatsworth left his car on the pitching span and '
                 'got off on foot before the roadway broke up and fell into Puget Sound. For '
                 'roughly an hour, the deck had gone into a torsional oscillation at about 0.2 '
                 'cycles per second, one edge of the roadway rising as the other fell. Film of '
                 'that collapse has been shown in physics classrooms ever since, where many '
                 'textbooks blamed simple resonance. In 1971, Robert Scanlan and John Tomko '
                 'published measured flutter derivatives for bridge decks. In 1991, Yusuf Billah '
                 'and Scanlan set out why resonance does not fit: self-excited aeroelastic flutter '
                 'made the moving deck feed its own motion.',
 'act1_plain_bridge': 'A long suspension bridge acts less like a static road and more like a '
                      'tethered wing above water. Everyday gusts push and twist the suspended '
                      'steel deck, and structural damping normally settles that motion like a '
                      'stiff diving board. Above a critical wind speed, that margin may vanish. '
                      'Swirling air starts pushing in rhythm with the natural twist of the deck, '
                      'adding energy on every cycle. Oscillations can grow until girders or '
                      'hangers fail. Modern long-span crossings streamline the deck or open a '
                      'central slot so wind passes with less feedback. Engineers also seek ways to '
                      'estimate weld fatigue between sparse sensors along multi-kilometer spans. '
                      'This folio pairs bridge flutter mechanics with an untested design study of '
                      'physics-guided machine learning; no bridge was instrumented and no neural network was trained for this page. This page explains the idea; it is not a design or assessment method, and none of its numbers apply to a real bridge.',
 'act1_body': 'Scanlan and Tomko (1971, DOI 10.1061/JMCEA3.0001526) measured flutter derivatives '
              'on wind-tunnel deck models, and Billah and Scanlan explained why resonance failed '
              '(1991, DOI 10.1119/1.16590): self-excited torsional flutter drove the span. Some long crossings use streamlined box girders, or twin boxes separated by a central '
              'slot (Yang et al. 2015, DOI 10.1061/(ASCE)BE.1943-5592.0000645). Monitoring '
              'buffeting and fatigue across a kilometer or more hits a practical limit because '
              'optical strain gauges and accelerometers sit at discrete stations (Chan et al. '
              '2006, DOI 10.1016/j.engstruct.2005.09.018). In 2019, Raissi, Perdikaris, and '
              'Karniadakis introduced Physics-Informed Neural Networks (PINNs, DOI '
              '10.1016/j.jcp.2018.10.045), adding equation residuals to network loss; later work '
              'tested PINNs on plate monitoring (Al-Adly & Kripakaran 2024, DOI '
              '10.1017/dce.2024.4). Whether sparse gauges could estimate weld-toe stress on a '
              'real bridge is not yet verified. CSI MasterFormat 05 12 00 and AASHTO LRFD name '
              'the subject scope only.',
 'act1_stakes': 'Quasi-static wind rules treat gusts as steady horizontal drag, ignoring how a '
                'flexing girder alters its own wake. Under strong wind, a deck may enter torsional or coupled flutter (Jain, Jones & Scanlan 1996, DOI '
                '10.1061/(ASCE)0733-9445(1996)122:7(716)). Below flutter onset, storm buffeting '
                'adds spanwise stress cycles, while wheel loads drive local root and toe fatigue '
                'cracks in welded rib-to-deck joints of orthotropic steel decks (Ya, Yamada & '
                'Ishikawa 2011, DOI 10.1061/(ASCE)BE.1943-5592.0000181). Replacing hangers or '
                'cracked deck plates on a working crossing is costly. Pairing wind-tunnel '
                'derivatives with physics-guided models might help focus inspection earlier, '
                'under stated assumptions; that remains an untested research aim.',
 'pullquote': '"When aerodynamic torsional damping A_2*(K) crosses from negative to positive, the '
              'wind stops resisting deck twist and begins feeding energy into every oscillation '
              'cycle."',
 'chronology': [('1940',
                 'First Tacoma Narrows Bridge fails near 19 meters per second under torsional '
                 'oscillation.'),
                ('1971',
                 'Scanlan & Tomko publish measured lift and pitching-moment flutter derivatives '
                 'for bridge decks.'),
                ('1991–1996',
                 'Billah & Scanlan clarify Tacoma Narrows; Sarkar et al. (1994) identify aeroelastic parameters of flexible bridges; Jain et al. (1996) treat coupled flutter and buffeting.'),
                ('2006–2015',
                 'Chan et al. (2006) monitor Tsing Ma with fiber-Bragg sensors; Ya et al. (2011) '
                 'test weld fatigue; Yang et al. (2015) study slotted twin boxes.'),
                ('2019–2026',
                 'Raissi et al. (2019) introduce PINNs, tested on plates by Al-Adly & Kripakaran '
                 '(2024); this folio sketches a bridge proposal.')],
 'act2_title': 'Act II — How It Actually Works: Scanlan Aeroelastic Flutter + PINN Virtual Sensing',
 'act2_analogy': 'Hold your palm flat out a car window at highway speed. Tilt the front edge up '
                 'slightly, and rushing air pushes your wrist upward, twisting your hand further; '
                 'slotted twin-box decks bleed air between boxes to weaken that twist. The '
                 'analogy stops at support restraint: an arm pivots at one shoulder, whereas '
                 'continuous cables couple bounce and twist.',
 'act2_plain_primer': 'Our interactive plate has two sliders, and we separate what the browser '
                      'computes from fixed reference cards. Mean Wind Velocity sets wind speed '
                      'from 20 to 85 meters per second on a 36-meter model deck (about 6.15 '
                      'reduced velocity at default wind). Dragging it updates Reduced Wind '
                      'Velocity and switches Bridge Aeroelastic Verdict at 76.4 meters per '
                      'second, while Net Torsional Damping stays at its illustrative +2.84 '
                      'percent reference. PINN Physics Loss Weight adjusts the equation weight '
                      'from 0.10 to 2.00; moving it updates the slider label and shared '
                      'stage-overlay vectors, while PINN Virtual Stress Error stays at its '
                      'untested 1.42 percent reference because no neural simulation runs here.',
 'distill_diagram': {'analogy_title': 'Hand Out a Speeding Car Window',
                     'analogy_sub': 'Tilting your palm catches wind and forces your wrist to twist '
                                    'upward',
                     'force_a_title': 'Mean Wind Speed (U_wind)',
                     'force_a_sub': 'Raises reduced velocity U/(f_α B) toward the model flutter '
                                    'limit',
                     'force_b_title': 'PINN Physics Loss (lambda_pde)',
                     'force_b_sub': 'Penalizes beam residuals to curb unphysical fits between '
                                    'sensors',
                     'threshold_title': 'Critical Flutter Velocity Tipping Point',
                     'threshold_pass': 'Stable: Natural damping dissipates aerodynamic wind energy',
                     'threshold_fail': 'Flutter: Negative damping causes self-amplifying deck '
                                       'twist'},
 'act2_intuition': 'A deck of width B in wind U oscillates in heave h(x,t) and torsion α(x,t). '
                   'Scanlan and Tomko (1971, DOI 10.1061/JMCEA3.0001526) linearized lift L_aero '
                   '(scaled by (1/2) ρ U² (2 B), N/m) and pitching moment M_ae (scaled by (1/2) ρ '
                   'U² (2 B²), N) via flutter derivatives H_i*(K) and A_i*(K) at K = B ω / U. '
                   'Sarkar, Jones, and Scanlan (1994, DOI '
                   '10.1061/(ASCE)0733-9399(1994)120:8(1718)) and Jain, Jones, and Scanlan (1996, '
                   'DOI 10.1061/(ASCE)0733-9445(1996)122:7(716)) used eight and eighteen '
                   'derivatives with (1/2) ρ U² B for lift or drag and (1/2) ρ U² B² for moment, '
                   'where A_2*^(1996) = 2 A_2*^(1971) shifts the torsional denominator from 2 I_α '
                   'to 4 I_α. With per-span inertia I_α (kg·m²/m, making ρ B⁴ / I_α '
                   'dimensionless), uncoupled 1971 torsional damping is ζ_net = ζ_s − (ρ B⁴ / '
                   '[2 I_α]) A_2*(K). At U = 52.0 m/s, B = 36 m, and f_α = 0.235 Hz, U_red = 6.15 '
                   '(K = 1.02); +2.84% and U_crit = 76.4 m/s are fixed illustrative values, not computed from this law and not wind-tunnel data. A coupled PINN loss L_total = L_data + λ_pde ‖R_pde‖² '
                   'would non-dimensionalize bending E I ∂⁴h/∂x⁴ − H_w ∂²h/∂x² + m ∂²h/∂t² − '
                   'L_aero(x,t) and torsion I_α ∂²α/∂t² − G J ∂²α/∂x² − M_ae(x,t); 1.42% is an '
                   'untested reference.',
 'act2_deepening': 'As a qualitative picture, flow separating at the leading edge of a bluff girder can act in phase with pitch velocity; when A_2*(K) turns positive, the wind injects torsional energy (Billah & Scanlan 1991, DOI 10.1119/1.16590). Wind-tunnel tests on '
                   'twin-box decks suggest a central slot modifies gap venting and surface-pressure '
                   'phase between windward and leeward boxes, raising critical flutter speed when the slot suits the section (Yang et al. 2015, DOI '
                   '10.1061/(ASCE)BE.1943-5592.0000645). For sensing, automatic differentiation '
                   'evaluates fourth-order bending derivatives without grid-difference noise '
                   '(Raissi et al. 2019, DOI 10.1016/j.jcp.2018.10.045; Al-Adly & Kripakaran '
                   '2024, DOI 10.1017/dce.2024.4). Still, storm gusts apply unmeasured loads '
                   'L_aero(x,t) and M_ae(x,t), so 8-sensor stress recovery remains ill-posed '
                   'without wind-load estimation.',
 'walkthrough': ['Experiment 1 (Reduced Velocity & Threshold): Drag Mean Wind Velocity U_wind '
                 'from 35.0 to 78.0 m/s. U/(f_α B) climbs from 4.14 to 9.22 and the verdict '
                 'flips at U_crit = 76.4 m/s, while +2.84% stays a fixed reference.',
                 'Experiment 2 (PINN Loss Weight Label): Move PINN Physics Loss Weight λ_pde '
                 'from 0.10 to 2.00; the browser updates λ = … and shared stage-overlay vectors '
                 'while 1.42% remains a fixed placeholder value.',
                 'Experiment 3 (4-Stage Stepper): Step Stages 1 to 4 across modal kinematics, '
                 'Scanlan 2B² moment scaling, coupled PDE residuals, and proposed weld-fatigue '
                 'checks.'],
 'act4_title': 'Act IV — Civil Structural Digital Twins, Lab Sustainability & Upstream Discovery '
               'Threads',
 'act4_human_ai': 'Fiber-Bragg-grating (FBG) strain sensors were trialed on the Tsing Ma Bridge (Chan et al. 2006, DOI 10.1016/j.engstruct.2005.09.018). As an untested proposal, '
                  'sparse FBG and accelerometer data might pair with PINNs (Al-Adly & Kripakaran '
                  '2024, DOI 10.1017/dce.2024.4) or SINDy sparse regression (Brunton et al. 2016, DOI 10.1073/pnas.1517384113) to '
                  'prioritize Orthotropic Steel Deck (OSD) weld inspection (Ya et al. 2011, DOI '
                  '10.1061/(ASCE)BE.1943-5592.0000181). Citation tallies were checked in Scite '
                  '(DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'Optical gauges record strain at discrete stations (Chan et al. 2006, DOI '
                   '10.1016/j.engstruct.2005.09.018), whereas traffic wheel loads nucleate local '
                   'fatigue cracks at welded U-rib-to-deck joints (Ya, Yamada & Ishikawa 2011, '
                   'DOI 10.1061/(ASCE)BE.1943-5592.0000181) alongside spanwise wind buffeting. '
                   'Two caveats limit any proposed PINN twin: global beam equations cannot '
                   'resolve local weld-toe notches without submodeling, and surrogates may '
                   'miscalibrate in extreme storms outside training data. Separating measured '
                   'wind-tunnel derivatives from fixed illustrative values keeps tests honest.',
 'cf_bridge': 'Standalone civil engineering folio, written for structural, wind and bridge engineers.',
 'sources': ['Scanlan, R. H., & Tomko, J. J. (1971). Airfoil and Bridge Deck Flutter Derivatives. '
             'J. Eng. Mech. Div. (ASCE), 97(6), 1717–1737. DOI: 10.1061/JMCEA3.0001526.',
             'Billah, K. Y., & Scanlan, R. H. (1991). Resonance, Tacoma Narrows bridge failure, and undergraduate physics textbooks. Am. J. Phys., 59(2), 118–124. DOI: 10.1119/1.16590.',
             'Sarkar, P. P., Jones, N. P., & Scanlan, R. H. (1994). Identification of Aeroelastic Parameters of Flexible Bridges. J. Eng. Mech., 120(8), 1718–1742. DOI: 10.1061/(ASCE)0733-9399(1994)120:8(1718).',
             'Jain, A., Jones, N. P., & Scanlan, R. H. (1996). Coupled Flutter and Buffeting Analysis of Long-Span Bridges. J. Struct. Eng., 122(7), 716–725. DOI: 10.1061/(ASCE)0733-9445(1996)122:7(716).',
             'Simiu, E., & Scanlan, R. H. (1996). Wind Effects on Structures: Fundamentals and Applications to Design (3rd ed.). Wiley.',
             'Chan, T. H. T., Yu, L., Tam, H. Y., Ni, Y. Q., Liu, S. Y., Chung, W. H., & Cheng, L. K. (2006). Fiber Bragg grating sensors for structural health monitoring of Tsing Ma bridge: Background and experimental observation. Eng. Struct., 28(5), 648–659. DOI: 10.1016/j.engstruct.2005.09.018.',
             'Ya, S., Yamada, K., & Ishikawa, T. (2011). Fatigue Evaluation of Rib-to-Deck Welded Joints of Orthotropic Steel Bridge Deck. J. Bridge Eng., 16(4), 492–499. DOI: 10.1061/(ASCE)BE.1943-5592.0000181.',
             'Yang, Y., Wu, T., Ge, Y., & Kareem, A. (2015). Aerodynamic Stabilization Mechanism of a Twin Box Girder with Various Slot Widths. J. Bridge Eng., 20(3), 04014067. DOI: 10.1061/(ASCE)BE.1943-5592.0000645.',
             'Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing equations from data by sparse identification of nonlinear dynamical systems. PNAS, 113(15), 3932–3937. DOI: 10.1073/pnas.1517384113.',
             'Raissi, M., Perdikaris, P., & Karniadakis, G. E. (2019). Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. J. Comput. Phys., 378, 686–707. DOI: 10.1016/j.jcp.2018.10.045.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and classifies their intent using deep learning. Quant. Sci. Stud., 2(3), 882–898. DOI: 10.1162/qss_a_00146.',
             'Al-Adly, A. I. F., & Kripakaran, P. (2024). Physics-informed neural networks for structural health monitoring: a case study for Kirchhoff-Love plates. Data-Centric Eng., 5, e6. DOI: 10.1017/dce.2024.4.',
             'AASHTO (2024). AASHTO LRFD Bridge Design Specifications (10th ed.) & CSI 05 12 00.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Long-span twin-box '
        'suspension bridge cross-section with Scanlan flutter derivatives and PINN virtual sensor '
        'nodes">\n'
        '            <line x1="40" y1="185" x2="640" y2="185" stroke="currentColor" '
        'stroke-opacity="0.35"/>\n'
        '            <path d="M 55 45 Q 200 155 345 45" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="2.5"/>\n'
        '            <line x1="115" y1="88" x2="115" y2="132" stroke="currentColor" '
        'stroke-width="1.2" stroke-dasharray="3,2"/>\n'
        '            <line x1="200" y1="100" x2="200" y2="132" stroke="currentColor" '
        'stroke-width="1.2" stroke-dasharray="3,2"/>\n'
        '            <line x1="285" y1="88" x2="285" y2="132" stroke="currentColor" '
        'stroke-width="1.2" stroke-dasharray="3,2"/>\n'
        '            <g id="tp-e07-deck-group" transform="translate(200, 134) rotate(-3.2)">\n'
        '              <polygon points="-115,-8 -14,-8 -22,8 -98,8" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '              <polygon points="14,-8 115,-8 98,8 22,8" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '              <circle cx="-65" cy="0" r="4.5" fill="var(--tp-verdigris)"/>\n'
        '              <circle cx="65" cy="0" r="4.5" fill="var(--tp-verdigris)"/>\n'
        '              <circle cx="0" cy="0" r="5" fill="var(--tp-minium)"/>\n'
        '            </g>\n'
        '            <path id="tp-e07-wind-stream" d="M 35 134 Q 140 118 200 134 T 365 130" '
        'fill="none" stroke="var(--tp-verdigris)" stroke-width="2" stroke-dasharray="6,4"/>\n'
        '            <line x1="385" y1="22" x2="385" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="55" y="26" font-size="11" font-weight="600" '
        'fill="currentColor">Twin-Box Vented Girder &amp; PINN Virtual Nodes</text>\n'
        '            <text id="tp-e07-svg-flutter-text" x="55" y="172" font-size="10.5" '
        'fill="var(--tp-verdigris)">U_crit = 76.4 m/s · Net Damping ζ_net = +2.84% '
        '(MODEL)</text>\n'
        '            <text x="394" y="26" font-size="9.5" font-weight="600" '
        'fill="currentColor">Scanlan Damping ζ_net(U) Schematic &amp; PINN Reference</text>\n'
        '            <path id="tp-e07-damping-curve" d="M 410 145 Q 505 110 565 135 Q 605 155 635 '
        '182" fill="none" stroke="var(--tp-prussian)" stroke-width="2.6"/>\n'
        '            <line x1="405" y1="160" x2="640" y2="160" stroke="var(--tp-minium)" '
        'stroke-width="1.5" stroke-dasharray="4,3"/>\n'
        '            <circle id="tp-e07-op-dot" cx="525" cy="126" r="6" '
        'fill="var(--tp-verdigris)"/>\n'
        '            <text x="410" y="154" font-size="9.5" fill="var(--tp-minium)">Flutter '
        'Threshold ζ_net = 0 (A_2* Crossover)</text>\n'
        '            <text id="tp-e07-pinn-text" x="410" y="178" font-size="10" '
        'fill="var(--tp-prussian)">PINN Virtual Stress Error: 1.42% (λ_pde = 1.00)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a multi-kilometer twin-box suspension bridge in a '
        'coastal gale instrumented with glowing Physics-Informed Neural Network virtual sensing '
        'nodes and aeroelastic wind streamlines would look like (artistic impression, not a '
        'measured structure)',
 'caption': 'Conceptual Vision Plate E.07-V (Imagining What It Would Look Like) · Artistic '
            'impression of a vented twin-box bridge in storm wind with a proposed PINN monitor.'}

DISPATCH = {'kicker': 'FRONTIER CIVIL ENGINEERING DISPATCH · PINN BRIDGE DIGITAL TWINS & SCANLAN FLUTTER',
 'headline': 'Could Physics-Informed Neural Networks Turn Sparse Bridge Accelerometers Into Full-Span Stress Estimates?',
 'body': "Pairs Scanlan's flutter derivatives (DOI 10.1061/JMCEA3.0001526; Jain et al. 1996, DOI 10.1061/(ASCE)0733-9445(1996)122:7(716)) and twin-box slot mechanics (Yang et al. 2015, DOI 10.1061/(ASCE)BE.1943-5592.0000645) with PINNs (Raissi et al. 2019, DOI 10.1016/j.jcp.2018.10.045; Al-Adly & Kripakaran 2024, DOI 10.1017/dce.2024.4) for sparse bridge sensing; untested proposal."}

META_3D = ('Scanlan Suspension Bridge Aeroelastic Flutter Surface',
 'X: Deck Spanwise Coordinate · Z: Wind Speed U/U_crit · Y: Coupled Heave–Torsion Flutter Energy')

ES_TRANSLATION = {'title_es': 'Flameo Aeroelástico de Puentes Colgantes de Gran Claro, Derivadas de Scanlan y '
             'Gemelos Digitales PINN',
 'subtitle_es': 'Cómo las derivadas aeroelásticas de Robert Scanlan describen la estabilidad de un tablero de doble cajón bajo viento fuerte, junto con un estudio de diseño de gemelos digitales de Redes Neuronales Informadas por la Física (PINN) a partir de pocos acelerómetros.',
 'why_es': 'Sacar la palma plana por la ventanilla de un auto e inclinarla hace que el viento '
           'empuje y tuerza más la muñeca; un doble cajón ranurado atenúa ese giro. La analogía '
           'termina en el apoyo: el brazo gira en un hombro, mientras los cables acoplan flexión '
           'y torsión.',
 'plain_es': 'Un puente colgante actúa menos como calzada fija y más como un ala sujeta sobre el '
             'agua. Las ráfagas cotidianas tuercen el tablero y el amortiguamiento del acero '
             'suele apagarlas. Sobre una velocidad crítica ese margen puede perderse. El aire '
             'empuja en fase con la torsión y mete energía en cada ciclo, como en Tacoma Narrows '
             'en 1940. Las oscilaciones pueden crecer hasta dañar péndolas o vigas. Los cruces modernos '
             'perfilan el cajón o abren una ranura central para reducir esa retroalimentación. '
             'También se busca estimar fatiga en soldaduras entre pocos sensores. Este folio une '
             'esa física con una propuesta no probada de redes guiadas por ecuaciones, sin puente instrumentado ni red entrenada. Esta página explica la idea; no es un método de diseño ni de evaluación, y ninguno de sus números aplica a un puente real.',
 'deep_es': 'Bajo el escalamiento de momento 2B² de Scanlan y Tomko (1971, DOI '
            '10.1061/JMCEA3.0001526) con inercia por metro I_α (kg·m²/m), el amortiguamiento '
            'torsional neto es ζ_net = ζ_s − (ρ B⁴ / [2 I_α]) A_2*^(1971)(K) = ζ_s − (ρ B⁴ / '
            '[4 I_α]) A_2*^(1996)(K), donde la convención B² de Sarkar et al. (1994, DOI '
            '10.1061/(ASCE)0733-9399(1994)120:8(1718)) y Jain et al. (1996, DOI '
            '10.1061/(ASCE)0733-9445(1996)122:7(716)) cumple A_2*^(1996) = 2 A_2*^(1971). La '
            'ranura central de un doble cajón modifica la fase de presiones (Yang et al. 2015, '
            'DOI 10.1061/(ASCE)BE.1943-5592.0000645). Se propone evaluar sensores ópticos (Chan '
            'et al. 2006, DOI 10.1016/j.engstruct.2005.09.018) y residuos acoplados de las ecuaciones de flexión y torsión en PINNs (Raissi et al. 2019, DOI 10.1016/j.jcp.2018.10.045; '
            'Al-Adly y Kripakaran 2024, DOI 10.1017/dce.2024.4) frente a fatiga por cargas '
            'rodantes en uniones costilla-tablero (Ya et al. 2011, DOI '
            '10.1061/(ASCE)BE.1943-5592.0000181). El control de viento actualiza U/(f_α B) y el veredicto en 76.4 m/s; 76.4 m/s, +2.84 % y 1.42 % son valores ilustrativos fijos: no provienen de un túnel de viento ni de una red entrenada.'}
