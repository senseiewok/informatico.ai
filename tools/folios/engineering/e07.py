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
 'steps': ['Stage 1 (Coupled Heave-Torsion Modal Kinematics): A model 2,100 m suspension span with deck width B = 36 m oscillates in vertical bending h(x,t) (f_h = 0.095 Hz) and torsion α(x,t) (f_α = 0.235 Hz). These are illustrative values, not a surveyed bridge.',
           'Stage 2 (Scanlan Aeroelastic Flutter Derivatives): Motion-induced pitching moment M_ae scales with A_2*(K) at reduced velocity U / (f_α B); in the folio model the vented twin-box girder keeps A_2*(K) < 0 up to U_crit = 76.4 m/s, a fixed illustrative value.',
           'Stage 3 (Physics-Informed Neural Network Virtual Sensing): Embedding the coupled Euler–Bernoulli + Saint-Venant PDE residual R_pde into L_total is the proposed way to reconstruct full-span bending stress from 8 accelerometers. No network was trained for this folio.',
           'Stage 4 (Orthotropic Steel Deck Fatigue Check, a Proposal): Stress histories from such a digital twin could be compared with the fatigue provisions of a design code such as the AASHTO LRFD Bridge Design Specifications at rib-to-deck welds. The folio performs no code check.'],
 'readouts': [{'label': 'Reduced Wind Velocity U/(f_α B)', 'value': '6.15 (U = 52.0 m/s, B = 36 m)'},
              {'label': 'Net Torsional Damping (ζ_net)', 'value': '+2.84% (illustrative; U_crit = 76.4 m/s)'},
              {'label': 'PINN Virtual Stress Error', 'value': '1.42% (illustrative; λ_pde = 1.00)'},
              {'label': 'Bridge Aeroelastic Verdict', 'value': 'STABLE IN MODEL (ζ_net > 0)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 05 12 00 / AASHTO LRFD',
                'title': 'Streamlined Twin-Box Orthotropic Steel Bridge Girder & Fiber-Bragg PINN '
                         'Digital Twin',
                'body': 'Aerodynamically vented twin-box structural steel deck girder with central '
                        '6.0 m wind slot, nose fairings, and 8-node tri-axial accelerometer / FBG '
                        'optical strain array feeding an edge Physics-Informed Neural Network '
                        'virtual stress monitor.',
                'meta': 'Design study · U_crit = 76.4 m/s is a model value, not a wind-tunnel result · no code compliance is claimed'},
 'sidenote_1': {'kicker': 'SIDENOTE E.07-A · WHY TACOMA NARROWS WAS FLUTTER, NOT SIMPLE VORTEX '
                          'RESONANCE',
                'body': 'Kármán vortex shedding occurs at a Strouhal frequency f_s = St · U / D (about 1 Hz at 19 m/s), whereas Tacoma Narrows twisted at about 0.2 Hz. Billah & Scanlan (1991, DOI 10.1119/1.16590) use this mismatch to argue that the failure was not vortex resonance but self-excited single-degree-of-freedom torsional flutter, in which motion-dependent aerodynamic damping turns negative (A_2*(K) > 0).'},
 'sidenote_2': {'kicker': 'SIDENOTE E.07-B · SPECIFICATION PLATE · CSI 05 12 00 / PINN VIRTUAL '
                          'SENSING',
                'body': 'By regularizing neural network weights with the fourth-order '
                        'Euler–Bernoulli operator E I ∂⁴h/∂x⁴ + m ∂²h/∂t² = q_aero(x,t), PINN '
                        'digital twins are meant to damp unphysical stress oscillations between sparse '
                        'bridge sensors.'},
 'skill': {'filename': 'bridge-flutter-pinn-twin-SKILL.md',
           'name': 'bridge-flutter-pinn-twin',
           'description': 'AI-agnostic structural and wind civil engineering skill for Scanlan '
                          'bridge aeroelastic flutter derivatives, critical wind speed U_crit, and '
                          'Physics-Informed Neural Network (PINN) virtual stress sensing.',
           'rules': ['Compute dimensionless reduced velocity U_red = U / (f_alpha * B) and reduced '
                     'frequency K = B * omega / U = 2 * pi / U_red.',
                     'Evaluate net torsional aeroelastic damping zeta_net = zeta_struct - (rho * '
                     'B^4 / (2 * I_alpha)) * A_2*(K); instability (flutter) occurs when zeta_net '
                     '<= 0.',
                     'Balance PINN composite loss L_total = L_data + lambda_pde * ||E*I*u_xxxx + '
                     'm*u_tt - f_aero||^2 so sparse sensor noise does not violate Euler-Bernoulli '
                     'equilibrium.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. U_crit = 76.4 m/s, net damping +2.84% and the 1.42% PINN error are now labelled as illustrative model values: no wind-tunnel test was run and no network was trained, and the claims of wind-tunnel verification and AASHTO LRFD compliance are withdrawn. The Tacoma Narrows account is cut back to the documented record and cites Scanlan & Tomko 1971 (DOI 10.1061/JMCEA3.0001526) and Billah & Scanlan 1991 (DOI 10.1119/1.16590). Statements that such digital twins are deployed are now written as proposals.',
                'opus': 'Review: references checked by DOI in the Scite index on 2026-11-14; the reduced velocity was recomputed by hand (B = 36 m is now stated).'},
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
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/j.jcp.2018.10.045',
           'fetched_on': '2026-11-08',
           'citing_publications': 24941,
           'supporting': 65,
           'mentioning': 12640,
           'contrasting': 4,
           'retracted': False,
           'summary': 'Scite index entry for Raissi, Perdikaris & Karniadakis 2019 (DOI 10.1016/j.jcp.2018.10.045), fetched 2026-11-08: 24,941 citing publications (65 supporting, 12,640 mentioning, 4 contrasting) and no retraction notice. These counts describe that one paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/j.jcp.2018.10.045',
           'fetched_on': '2026-11-08',
           'citing_publications': 24941,
           'supporting': 65,
           'mentioning': 12640,
           'contrasting': 4,
           'retracted': False,
           'summary': 'Scite index entry for Raissi, Perdikaris & Karniadakis 2019 (DOI 10.1016/j.jcp.2018.10.045), fetched 2026-11-08: 24,941 citing publications (65 supporting, 12,640 mentioning, 4 contrasting) and no retraction notice. These counts describe that one paper, not this folio.'},
 'act1_title': 'Act I — From Tacoma Narrows to Multi-Kilometer Suspension Spans & Physics-Informed '
               'Bridge Digital Twins',
 'act1_dropcap': 'On November 7, 1940, four months after it opened, the first Tacoma Narrows Bridge twisted itself apart in a wind of about 19 metres per second (42 miles per hour). The deck had gone into a torsional oscillation at about 0.2 cycles per second, one edge of the roadway rising as the other fell, and after roughly an hour of this the main span broke up and fell into Puget Sound. Leonard Coatsworth, a newspaper editor, left his car on the span and got off on foot; the collapse was filmed, and the film has been shown in physics classrooms ever since. For decades many textbooks described the failure as simple resonance, a steady wind shedding vortices in time with the bridge. In 1971 Robert Scanlan and John Tomko published measured flutter derivatives for bridge decks (DOI 10.1061/JMCEA3.0001526), and in 1991 Billah and Scanlan set out why the resonance account does not fit (DOI 10.1119/1.16590): the bridge was driven by self-excited aeroelastic flutter, in which the moving deck changes the air forces on itself so that they feed its motion.',
 'act1_plain_bridge': 'In plain words, a suspension bridge is not just a heavy road hung from '
                      'cables; it is a giant wing tethered above water. When wind flows past any '
                      'roadway deck, the air splits into swirling currents that push and twist the '
                      'structure. Normally, a bridge absorbs these gusts and settles down, like a '
                      'stiff diving board after a single jump. But at certain high wind speeds, a '
                      'dangerous tipping point occurs. Instead of slowing the motion, the rushing '
                      "air begins pushing in perfect rhythm with the bridge's natural twist, "
                      'pumping fresh energy into each cycle. The oscillations grow larger with '
                      'every second until structural steel bends beyond repair. Today, long-span decks are shaped, and sometimes slotted, so that the wind passes with less of this feedback. This folio also sketches how physics-guided machine learning could estimate stress along a span from only a handful of vibration sensors. That part is a design study: no bridge was instrumented and no network was trained for this page.',
 'act1_body': 'Long suspension crossings today often use streamlined box girders, and some of the longest use twin boxes separated by a central slot. Monitoring cable tension, wind buffeting and metal fatigue across a span of a kilometre or more runs into a practical limit: strain gauges and accelerometers can be fixed at only a few accessible points, which leaves long stretches of steel unmeasured. In 2019 Maziar Raissi, Paris Perdikaris and George Em Karniadakis published Physics-Informed Neural Networks (PINNs, DOI 10.1016/j.jcp.2018.10.045), a general method for forward and inverse problems governed by partial differential equations. A physics-informed network adds the residual of the governing equations to its loss function, so that its fit to sparse data must also respect those equations. Their paper is not about bridges. This folio proposes applying the idea to the beam and torsion equations of a deck, so that a digital twin could estimate bending moments and stresses between sensors. Whether such a twin is accurate enough for fatigue assessment on a real bridge is an open question that this page does not answer. CSI MasterFormat 05 12 00 (Structural Steel Framing) and the AASHTO LRFD Bridge Design Specifications are named only to place the subject; no compliance with either is claimed.',
 'act1_stakes': 'The real-world stakes of aeroelastic modeling become apparent whenever classical '
                'approximations fail under storm conditions. For decades, engineers treated wind '
                'loads as static horizontal pressures, multiplying mean velocity by an empirical '
                'drag coefficient. That simplified approach ignores how a flexing structure alters '
                'the very aerodynamic flow around it. When unexpected wind shear or localized '
                'vortex shedding develops during a tropical cyclone, a bridge designed purely for '
                'static pressure can suddenly slip into torsional flutter. Even when motions do '
                'not reach catastrophic collapse, chronic unobserved vibrations accumulate '
                'millions of low-amplitude stress cycles, nucleating invisible fatigue cracks at '
                'welded rib-to-deck joints. Replacing hanger cables or cracked orthotropic deck plates on a working sea crossing is costly and disruptive. The hope behind pairing wind-tunnel flutter derivatives with physics-informed digital twins is to notice local degradation earlier. That is a research aim, not an established result.',
 'pullquote': '"When aerodynamic torsional damping A_2*(K) crosses from negative to positive, the '
              'wind stops resisting deck twist and begins feeding energy into every oscillation '
              'cycle."',
 'chronology': [('1940',
                 'The first Tacoma Narrows Bridge collapses in a wind of about 19 m/s after sustained torsional oscillation.'),
                ('1971',
                 'Robert H. Scanlan & John J. Tomko publish measured flutter derivatives H_i* and A_i* for airfoils and bridge decks in the ASCE Journal of the Engineering Mechanics Division (DOI 10.1061/JMCEA3.0001526).'),
                ('1991',
                 'Billah & Scanlan explain why simple resonance does not account for the Tacoma Narrows failure (American Journal of Physics, DOI 10.1119/1.16590).'),
                ('2019',
                 'Raissi, Perdikaris & Karniadakis publish Physics-Informed Neural Networks '
                 '(PINNs) in Journal of Computational Physics (DOI 10.1016/j.jcp.2018.10.045).'),
                ('2026',
                 'This folio proposes, as a design study, PINN digital twins fed by sparse accelerometers for virtual stress sensing on long-span bridges.')],
 'act2_title': 'Act II — How It Actually Works: Scanlan Aeroelastic Flutter + PINN Virtual Sensing',
 'act2_analogy': 'Everyday analogy: Picture holding your palm flat out the window of a car '
                 'speeding down a highway. If you tilt your hand up even slightly, the rushing '
                 'wind catches the underside, forcing your wrist upward and twisting your palm '
                 'open even further. That sudden upward jerk is aeroelastic flutter in action. '
                 'Aerodynamic twin-box bridge decks add a central open slot that lets air bleed '
                 'through cleanly, canceling that lifting twist before it can build into an '
                 'uncontrolled oscillation.',
 'act2_plain_primer': 'To explore this aeroelastic behavior, our interactive laboratory provides '
                      'two primary controls. The first control is Mean Wind Velocity, which sets '
                      'the speed of the storm pushing against the suspended bridge deck. At gentle '
                      'breezes, structural stiffness and natural material damping absorb every '
                      'gust, keeping deck motion small and stable. As you slide the wind speed '
                      'higher toward storm levels, the rushing airflow begins feeding rotational '
                      'energy back into the deck, driving net damping toward zero. The second '
                      'control is the Physics Loss Weight in our digital twin neural network. When '
                      'this knob is set near zero, the artificial intelligence behaves like a '
                      'naive pattern matcher, producing erratic, noisy stress guesses between the '
                      'sparse vibration sensors. Turning this knob up forces the model to respect '
                      "Newton's laws of motion and beam elasticity, smoothly reconstructing "
                      'internal bending stresses across every unmeasured meter of the span.',
 'distill_diagram': {'analogy_title': 'Hand Out a Speeding Car Window',
                     'analogy_sub': 'Tilting your palm catches wind and forces your wrist to twist '
                                    'upward',
                     'force_a_title': 'Mean Wind Speed (U_wind)',
                     'force_a_sub': 'Pumps aeroelastic energy into deck pitch and vertical heave '
                                    'motions',
                     'force_b_title': 'PINN Physics Loss (lambda_pde)',
                     'force_b_sub': 'Enforces beam mechanics to eliminate sensor noise and wild '
                                    'guesses',
                     'threshold_title': 'Critical Flutter Velocity Tipping Point',
                     'threshold_pass': 'Stable: Natural damping dissipates aerodynamic wind energy',
                     'threshold_fail': 'Flutter: Negative damping causes self-amplifying deck '
                                       'twist'},
 'act2_intuition': 'A long-span suspension bridge deck of width B subjected to mean horizontal wind velocity U oscillates in coupled vertical heave h(x,t) and torsional pitch alpha(x,t). In 1971, Scanlan and Tomko wrote the motion-induced aerodynamic lift and pitching moment as linear functions of the deck motion, with dimensionless flutter derivatives H_i*(K) and A_i*(K) measured in a wind tunnel, where K = B omega / U is the reduced frequency. Their paper used three derivatives for lift and three for moment; later work extended the set to H_1* through H_4* and A_1* through A_4*, and to eighteen once lateral motion is included. Bluff plate girders can show positive values of the torsional derivative A_2*(K), which acts as negative aerodynamic damping. In the single-mode form used here, once wind velocity exceeds the critical value U_crit, net damping zeta_net = zeta_struct - (rho B^4 / [2 I_alpha]) A_2*(K) drops below zero and torsional flutter grows. The laboratory on this page takes B = 36 m and f_alpha = 0.235 Hz, so the reduced velocity at U = 52 m/s is 52 / (0.235 x 36) = 6.15. It does not state zeta_struct, I_alpha or an A_2* curve, so the readouts zeta_net = +2.84% and U_crit = 76.4 m/s are fixed illustrative values for a vented twin-box deck, not results computed from the law above or measured in a wind tunnel. The second half of the model is a physics-informed neural network that would penalize the Euler–Bernoulli beam residual R_pde = E I d^4h/dx^4 + m d^2h/dt^2 - L_aero in its composite loss function. The stress-error curve shown for it (18.4% falling to 1.42% as lambda_pde rises) is likewise illustrative: no network was trained for this folio.',
 'act2_deepening': 'At deeper multi-scale levels, bridge aeroelasticity couples three-dimensional '
                   'boundary-layer aerodynamics with structural dynamics. As air shears over the '
                   'leading windward nose fairing, thin boundary layers detach and form '
                   'alternating vortex sheets. In a conventional bluff girder, these detached '
                   'vortices roll across the deck surface and lock into the structural natural '
                   'frequency, generating suction peaks that lag behind the twisting motion. This '
                   'phase lag is precisely what transforms aerodynamic drag into an '
                   'energy-injecting torque. In vented twin-box decks, the central aerodynamic '
                   'slot acts as a pressure-relief bypass: the vortex shed from the leading box is '
                   'diffused before it can strike the trailing box. This is a qualitative picture, not a simulation run for this folio. On the sensing side, a physics-informed network uses automatic differentiation to take spatial derivatives of its displacement field, so curvature and shear can be read from the network without finite differencing. Whether that resolves strain concentrations at the weld toes of an orthotropic deck is untested here.',
 'walkthrough': ['Experiment 1 (Critical Flutter Boundary): Drag Wind Velocity U_wind from 35 m/s '
                 'up to 78 m/s. Watch Reduced Velocity U/(f_a B) climb and track the net '
                 'aeroelastic damping margin zeta_net as it approaches the Scanlan flutter '
                 'threshold.',
                 'Experiment 2 (PINN Physics Loss Regularization): Adjust PINN Physics Weight '
                 'lambda_pde from 0.10 (data-only black box prone to overfitting sparse sensors) '
                 'to 1.00–2.00 (strict Euler–Bernoulli + Scanlan PDE enforcement). The illustrative mid-span stress error falls from 18.4% to 1.42%; the page draws a curve and trains no network.',
                 'Experiment 3 (Twin-Box Slotted Deck vs. Bluff Girder): Step through Stages 1 to '
                 '4 to compare bluff vortex lock-in, Scanlan coupled flutter derivatives, vented '
                 'twin-box aerodynamic stabilization, and PINN virtual strain reconstruction.'],
 'act4_title': 'Act IV — Civil Structural Digital Twins, Lab Sustainability & Upstream Discovery '
               'Threads',
 'act4_human_ai': 'A bridge owner could combine sparse fiber-Bragg-grating (FBG) strain gauges and drone photogrammetry with a Physics-Informed Neural Network, so that inspection effort goes to the Orthotropic Steel Deck (OSD) weld details where the model estimates the highest stress ranges. This is a proposal; the folio reports no deployment.',
 'act4_deepening': 'Looking ahead, structural engineers and physics-informed machine learning could work together on how large bridges are designed and looked after. Instead of relying only on periodic manual inspection, a maintenance authority could run a digital twin that takes in data from fiber-optic sensors and uncrewed aerial vehicles and, during a storm, estimates where strain and fatigue damage are accumulating. None of this is claimed here as current practice. Open research questions remain: linking turbulence at small scales to the dynamics of a whole span, and keeping a neural surrogate trustworthy during an extreme event unlike anything in its training data. Grounding machine learning in continuum mechanics is one way to approach both, in the service of longer lives for existing spans and lighter new ones.',
 'cf_bridge': 'Standalone civil engineering folio, written for structural, wind and bridge engineers.',
 'sources': ['Scanlan, R. H., & Tomko, J. J. (1971). Airfoil and Bridge Deck Flutter Derivatives. '
             'Journal of the Engineering Mechanics Division (ASCE), 97(6), 1717–1737. DOI: 10.1061/JMCEA3.0001526.',
             'Billah, K. Y., & Scanlan, R. H. (1991). Resonance, Tacoma Narrows bridge failure, and undergraduate physics textbooks. American Journal of Physics, 59(2), 118–124. DOI: 10.1119/1.16590.',
             'Raissi, M., Perdikaris, P., & Karniadakis, G. E. (2019). Physics-informed neural '
             'networks: A deep learning framework for solving forward and inverse problems '
             'involving nonlinear partial differential equations. Journal of Computational '
             'Physics, 378, 686–707. DOI: 10.1016/j.jcp.2018.10.045.',
             'Simiu, E., & Scanlan, R. H. (1996). Wind Effects on Structures: Fundamentals and '
             'Applications to Design (3rd ed.). Wiley.',
             'AASHTO (2024). AASHTO LRFD Bridge Design Specifications (10th ed.) & CSI '
             'MasterFormat 05 12 00 Structural Steel Framing.',
             'Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing '
             'equations from data by sparse identification of nonlinear dynamical systems '
             '(dynamicslab/pysindy, https://github.com/dynamicslab/pysindy). PNAS, 113(15), '
             '3932–3937. DOI: 10.1073/pnas.1517384113.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
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
        'fill="currentColor">Scanlan Damping ζ_net(U) &amp; PINN Field Reconstruction</text>\n'
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
            'civil-engineering visualization imagining a long-span vented twin-box suspension '
            'bridge deflecting coastal storm winds while a Physics-Informed Neural Network (PINN) '
            'digital twin reconstructs internal stress fields.'}

DISPATCH = {'kicker': 'FRONTIER CIVIL ENGINEERING DISPATCH · PINN BRIDGE DIGITAL TWINS & SCANLAN FLUTTER',
 'headline': 'Could Physics-Informed Neural Networks Turn Sparse Bridge Accelerometers Into Full-Span Stress Estimates?',
 'body': "This folio pairs Robert Scanlan's aeroelastic flutter derivatives (Scanlan & Tomko 1971, DOI 10.1061/JMCEA3.0001526) with the Physics-Informed Neural Networks of Raissi, Perdikaris & Karniadakis (J. Comput. Phys., DOI 10.1016/j.jcp.2018.10.045). It proposes that a bridge digital twin could embed Euler–Bernoulli and torsional PDEs in its loss function to estimate stress and flutter margin along a 2,000 m span from about 8 accelerometer stations. It is a design study: nothing was trained or deployed."}

META_3D = ('Scanlan Suspension Bridge Aeroelastic Flutter Surface',
 'X: Deck Spanwise Coordinate · Z: Wind Speed U/U_crit · Y: Coupled Heave–Torsion Flutter Energy')

ES_TRANSLATION = {'title_es': 'Flameo Aeroelástico de Puentes Colgantes de Gran Claro, Derivadas de Scanlan y '
             'Gemelos Digitales PINN',
 'subtitle_es': 'Cómo las derivadas aeroelásticas de Robert Scanlan describen la estabilidad de un tablero de doble cajón bajo viento fuerte, junto con un estudio de diseño de gemelos digitales de Redes Neuronales Informadas por la Física (PINN) a partir de pocos acelerómetros.',
 'why_es': 'Sacar la mano plana por la ventanilla de un auto en movimiento con un ligero ángulo '
           'hace que el viento la empuje hacia arriba y tuerza la muñeca, inyectando energía en '
           'una oscilación autoexcitada.',
 'plain_es': 'En palabras sencillas, un puente colgante de gran claro funciona como una inmensa '
             'ala extendida sobre el agua. Cuando el viento sopla a través del estrecho, el aire '
             'empuja la estructura y genera pequeñas oscilaciones que la rigidez del acero '
             'normalmente disipa. Pero al alcanzar una velocidad crítica de viento, ocurre '
             'un fenómeno peligroso llamado flameo aeroelástico: el aire comienza a empujar en '
             'sincronía con la torsión del tablero, inyectando energía en cada ciclo hasta que el '
             'puente se retuerce de manera descontrolada, tal como ocurrió en el famoso colapso de '
             'Tacoma Narrows en 1940. Para reducir ese riesgo, algunos puentes modernos dividen el tablero en dos cajones de acero con una ranura central que deja pasar el viento. Este folio también plantea, como estudio de diseño, gemelos digitales basados en redes neuronales informadas por la física que podrían estimar los esfuerzos internos a partir de unos pocos acelerómetros. No se instrumentó ningún puente ni se entrenó ninguna red para esta página.',
 'deep_es': 'El comportamiento del puente está gobernado por dos fuerzas opuestas: la '
            'amortiguación estructural del acero y el momento aerodinámico inducido por el viento. '
            'A velocidades moderadas, la amortiguación natural disipa la energía cinética de las '
            'ráfagas. No obstante, a medida que la velocidad del viento se aproxima al umbral '
            'crítico, las fuerzas aerodinámicas superan la capacidad disipativa de la estructura, '
            'haciendo que la amortiguación neta se vuelva negativa. En este punto de inflexión, el '
            'tablero absorbe energía del flujo de aire y experimenta oscilaciones autoexcitadas de '
            'flexión y torsión acopladas. Los ingenieros modelan estas fuerzas con las derivadas aeroelásticas de Scanlan (Scanlan y Tomko 1971, DOI 10.1061/JMCEA3.0001526). El folio propone además usar redes neuronales informadas por la física (Raissi et al. 2019, DOI 10.1016/j.jcp.2018.10.045), que penalizan el residuo de las ecuaciones de Euler–Bernoulli, para estimar esfuerzos entre sensores dispersos. Los valores de la página (U_crit = 76.4 m/s, amortiguamiento neto de +2.84 %, error de 1.42 %) son valores ilustrativos del modelo: no provienen de un túnel de viento ni de una red entrenada.'}
