#!/usr/bin/env python3
"""Folio M.07 (MATH): Formula 1 350 kW MGU-K Pontryagin Optimal Energy Control, Hamilton–Jacobi–Bellman Lap Time Minimization & Fourier Neural Operator Surrogates."""
from __future__ import annotations

SLUG = 'm07'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.07',
 'slug': 'm07',
 'pillar': 'math',
 'category_code': 'M',
 'title': 'Formula 1 350 kW MGU-K Pontryagin Optimal Energy Control, Hamilton–Jacobi–Bellman Lap '
          'Time Minimization & Fourier Neural Operator Surrogates',
 'subtitle': "A design study: how Lev Pontryagin's Maximum Principle could schedule a hybrid race "
             "car's electric boost (350 kW under the 2026 Formula 1 rules as reported) without "
             'running the battery flat mid-straight, and how Fourier Neural Operators might stand in '
             'for slow flow solvers. The numbers are illustrative model values.',
 'date_published': '2026-11-02',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'F1 OPTIMAL CONTROL & AI · REV 1.1',
 'primary_kernel': 'tools/discovery/formal_proof_thermodynamic_landscape.py',
 'governing_law': 'H(x, u, λ) = 1/v + λ_v f_v(v, P_k, δ) − λ_E P_batt(P_k)/v ; u_{l+1} = σ(W u_l + F⁻¹(R_φ · F(u_l)))',
 'colophon': {'identifier': 'M.07 · F1 Pontryagin Control & FNO Surrogates · FIA 2026 Art. 5',
              'kernels': 'Pontryagin Maximum Principle (PMP) · HJB PDE · Fourier Neural Operator',
              'benchmarks': 'Model values: P_k,max = 350 kW · ΔE_lap = 4.0 MJ (assumed budget) · '
                            'FNO error 0.82% (illustrative, not measured)',
              'bridge': 'F1 350 kW Co-State Switching ↔ P.07 Active Aero (analogy only)'},
 'sliders': [{'label': 'MGU-K Peak Electric Power (P_k)',
              'min': 120.0,
              'max': 350.0,
              'step': 10.0,
              'value': 350.0,
              'unit': ' kW'},
             {'label': 'Fourier Spectral Modes (k_max)',
              'min': 8,
              'max': 64,
              'step': 4,
              'value': 32,
              'unit': ' modes'}],
 'steps': ['Stage 1 (Fourier Neural Operator Surrogate, proposed): An FNO layer u_{l+1} = σ(W u_l + '
           'F⁻¹(R_φ · F(u_l))) could map wing angle δ_wing and ride height h_ride to aerodynamic '
           'coefficients; no surrogate was trained here.',
           'Stage 2 (Distance-Domain Pontryagin Hamiltonian H): Rewrites minimum-time control in '
           'track distance ds/dt = v; on interior battery arcs, co-state λ_E* is constant across '
           'an assumed 4.0 MJ budget.',
           'Stage 3 (Convex-Loss Taper vs. Clipping): Above a switching speed, convex electrical '
           'losses taper P_k*(s) instead of clipping mid-straight (298.4 km/h and 0.42 s are '
           'illustrative).',
           'Stage 4 (Regenerative Braking Harvest): Under braking (P_k < 0), piecewise efficiency '
           'η_regen recovers kinetic energy so E_batt(L) = E_batt(0) closes the lap.'],
 'readouts': [{'label': 'Straight-Line Lap Gain (Δt_lap, model)',
               'value': '−0.42 s vs. naive clipping (illustrative)'},
              {'label': 'Optimal Taper Velocity (v_switch, model)',
               'value': '298.4 km/h (illustrative)'},
              {'label': 'FNO Operator Error (k_max = 32, model)',
               'value': '0.82% (illustrative; no surrogate trained here)'},
              {'label': 'Pontryagin Model Outcome',
               'value': 'Taper avoids clipping in the model (not a race result)'}],
 'spec_plate': {'division': 'APPLIED OPTIMAL CONTROL & OPERATOR LEARNING · DESIGN STUDY',
                'title': 'Hybrid 350 kW MGU-K Energy Store & Proposed FNO-Pontryagin Lap '
                         'Controller',
                'body': 'Design study: a 350 kW kinetic motor-generator unit scheduled by a '
                        'distance-domain Pontryagin co-state controller that could query a 32-mode '
                        'Fourier Neural Operator flow surrogate. Nothing here was built or run on '
                        'a car.',
                'meta': 'Method sources cited, not reproduced: Limebeer, Perantoni & Rao 2014 (DOI '
                        '10.1080/00207179.2014.900705) · Li et al. 2020 (arXiv:2010.08895)'},
 'sidenote_1': {'kicker': 'SIDENOTE M.07-A · WHY THE BATTERY CO-STATE λ_E IS CONSTANT ACROSS THE '
                          'LAP',
                'body': "By Pontryagin's adjoint equation dλ_E/ds = −∂H/∂E_batt, whenever battery "
                        'energy E_batt(s) stays inside [E_min, E_max] and losses omit state of '
                        'charge, ∂H/∂E_batt = 0, so one constant shadow price λ_E* governs the '
                        'lap.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.07-B · SPECIFICATION PLATE · FOURIER NEURAL OPERATOR '
                          'ZERO-SHOT SUPER-RESOLUTION',
                'body': 'Because R_φ acts on the lowest k_max Fourier modes, an FNO layer could be '
                        'evaluated on finer grids than its training mesh (Li et al. 2020, '
                        'arXiv:2010.08895); race-car aerodynamics remains untested here.'},
 'skill': {'filename': 'f1-pontryagin-fno-control-SKILL.md',
           'name': 'f1-pontryagin-fno-control',
           'description': 'AI-agnostic applied mathematics and operator-learning skill for Formula '
                          '1 350 kW MGU-K Pontryagin optimal energy management, HJB lap-time '
                          'minimization, and Fourier Neural Operator PDE surrogates.',
           'rules': ['Formulate the minimum-Hamiltonian H = (1/v) + lambda_v * a_net(v, P_k, '
                     'delta_wing) / v - lambda_E * P_batt(P_k) / v along arc-length s, with P_batt '
                     '= P_k / eta_k for motoring (P_k >= 0) and eta_regen * P_k under braking.',
                     'Evaluate the motoring optimality condition dH/dP_k = lambda_v / (m * v^2) '
                     '- lambda_E * (dP_batt/dP_k) / v = 0 (lambda_v, lambda_E < 0 under min_u '
                     'H): affine losses (dP_batt/dP_k = 1/eta_k) switch at lambda_v / (m * v) = '
                     'lambda_E / eta_k, whereas strictly convex losses P_batt(P_k) initiate '
                     'smooth tapering below P_k,max where lambda_v / (m * v) = lambda_E * '
                     'dP_batt/dP_k(P_k,max).',
                     'Evaluate spectral neural operator layer u_{l+1}(x) = sigma(W * u_l(x) + '
                     'F^{-1}(R_phi * F(u_l))(x)) truncated at k_max Fourier modes.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The lap-time gain, '
                           'switching speed, FNO error and speedup are now labeled as '
                           'illustrative model values; no surrogate was trained and no lap was '
                           'simulated. The 2014 Limebeer, Perantoni & Rao paper is no longer '
                           'cited for the 2026 rules it predates, the switching condition is '
                           'corrected to lambda_v/(m v) = lambda_E/eta, the invented opening scene '
                           'is replaced by a plain account, and the nebulizer and Cystic Fibrosis '
                           'dosing bridge is withdrawn.',
                'opus': 'Review: DOIs checked in Crossref and arXiv:2010.08895 checked on '
                        '2026-11-14; 2026-11-21 grounding pass verified and added Bellman 1954, '
                        'Crandall & Lions 1983, Perantoni & Limebeer 2014, Salazar et al. 2017, '
                        'Duhr et al. 2021, and Lu et al. 2021.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-02',
                'summary': 'REV 1.0 (Published 2026-11-02): Inaugural Volume IV Formula 1 applied '
                           'mathematics & AI monograph uniting Limebeer-Perantoni-Rao optimal '
                           'hybrid control (DOI 10.1080/00207179.2014.900705) with Fourier Neural '
                           'Operators (arXiv:2010.08895).',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'constant co-state d(lambda_E)/ds = 0 interior invariance, -0.42 s '
                        'straight-line clipping avoidance, and 0.82% FNO spectral convergence. '
                        "(REV 1.1: this 'verified' wording is withdrawn; the -0.42 s and 0.82% "
                        'figures are illustrative and were not computed by any run.)'}],
 'volume': 4,
 'volume_code': 'VOL. 04',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1080/00207179.2014.900705',
           'fetched_on': '2026-11-21',
           'citing_publications': 87,
           'supporting': 0,
           'mentioning': 52,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index [observed: Scite ML citation classification, '
                      'accessed 2026-11-21]: 0 retractions; 87 citing publications (0 supporting, '
                      '52 mentioning, 0 contrasting) on David Limebeer, Giacomo Perantoni & Anil '
                      "Rao's optimal control of Formula One hybrid energy recovery systems."}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1080/00207179.2014.900705',
           'fetched_on': '2026-11-21',
           'citing_publications': 87,
           'supporting': 0,
           'mentioning': 52,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index [observed: Scite ML citation classification, '
                      'accessed 2026-11-21]: 0 retractions; 87 citing publications (0 supporting, '
                      '52 mentioning, 0 contrasting) on David Limebeer, Giacomo Perantoni & Anil '
                      "Rao's optimal control of Formula One hybrid energy recovery systems."},
 'act1_title': "Act I — From Lev Pontryagin's Maximum Principle to 2026 Formula 1 350 kW Hybrid "
               'Control & Neural PDE Operators',
 'act1_dropcap': 'Lev Semenovich Pontryagin, blind from an accident at the age of fourteen, led '
                 'a control seminar at the Steklov Mathematical Institute in Moscow on engines, '
                 'valves, and steering rudders. Working with Vladimir Boltyanskii, Revaz '
                 'Gamkrelidze, and Evgenii Mishchenko, he asked how to guide a machine in minimum '
                 'time when controls hit hard limits. Euler and Lagrange had assumed smooth '
                 'interior adjustments. Real hardware defies that assumption: valves hit stops, '
                 'motors overheat, and batteries drain. Announced in the mid-1950s and set out in '
                 'their 1962 book The Mathematical Theory of Optimal Processes, their principle '
                 'attaches a shadow price called the co-state to each state. That co-state tracks '
                 'the future time value of stored energy, telling the controller when to use full '
                 'power, hold back, or brake. One marginal price coordinates every straight and '
                 'corner.',
 'act1_plain_bridge': 'Picture driving an electric hybrid car about fifty miles across a desert '
                      'highway on one small battery pack. No charging stations sit along the '
                      'route. Stomping on the accelerator pedal at the stoplight feels fast, yet '
                      'the battery runs dry halfway down the road. Once that charge disappears, '
                      'the car slows while steadier drivers pass. Optimal control asks a practical '
                      'question: how might a driver spend a finite budget of energy to finish in '
                      'the shortest time? Instead of guessing by reflex, race engineers compute a '
                      'marginal exchange rate for every watt-hour. At high speeds, wind resistance '
                      'pushes back hard and extra electric boost buys very little acceleration. '
                      'Easing off the boost early on a long straight saves charge for low-speed '
                      'corner exits. Braking into the next turn then feeds kinetic energy back '
                      'into the battery. Pacing beats draining the pack early.',
 'act1_body': 'Minimum-lap-time control for Formula One cars was cast in curvilinear track '
              'coordinates by Perantoni and Limebeer (2014, DOI 10.1080/00423114.2014.889315) and '
              'extended to hybrid recovery by Limebeer, Perantoni, and Rao (2014, DOI '
              '10.1080/00207179.2014.900705), when the motor-generator was limited to 120 '
              'kilowatts. Analytical Pontryagin policies for hybrid race cars were derived by '
              'Salazar et al. (2017, DOI 10.1109/TCST.2016.2642830). The 2026 rules, as reported, '
              'raise that limit to 350 kilowatts (not verified against the FIA text here), and '
              'the 4.0 megajoule per-lap energy budget is an assumed value. Separately, the '
              'Fourier Neural Operator (Li et al., 2020, arXiv:2010.08895, DOI '
              '10.48550/arXiv.2010.08895) parameterizes PDE kernels in Fourier space; pairing it '
              'with a race-car controller is proposed here and not yet tested.',
 'act1_stakes': 'Optimal control and continuum fluid mechanics long sat on opposite sides of a '
                'computational divide. Dynamic programming, introduced by Richard Bellman (1954, '
                'DOI 10.1090/S0002-9904-1954-09848-8), characterizes minimum-time trajectories '
                'via the Hamilton–Jacobi–Bellman equation, whose non-smooth value functions '
                'across switching surfaces are defined by the viscosity solutions of Crandall and '
                'Lions (1983, DOI 10.1090/S0002-9947-1983-0690039-8). Point-mass equations solve '
                'quickly, yet three-dimensional turbulent wakes remain too costly to evaluate '
                'online. Teams therefore fit polynomial wind-tunnel maps offline with conservative '
                'margins. Coupling Pontryagin co-state trajectory optimization with neural '
                'surrogates could narrow that gap, alongside classical spacecraft trajectory '
                'optimization.',
 'pullquote': '"In the model, a single shadow price, the co-state lambda_E, decides where on '
              'the straight to ease off the electric boost so the battery lasts the lap."',
 'chronology': [('1954–1957',
                 'Richard Bellman formulates Dynamic Programming and the Hamilton–Jacobi–Bellman '
                 '(HJB) equation (DOI 10.1090/S0002-9904-1954-09848-8).'),
                ('1956–1983',
                 'Pontryagin et al. publish the bounded-control maximum principle (1962); '
                 'Crandall & Lions define HJB viscosity solutions (DOI '
                 '10.1090/S0002-9947-1983-0690039-8).'),
                ('2014–2017',
                 'Limebeer, Perantoni & Rao model F1 hybrid recovery (DOI '
                 '10.1080/00207179.2014.900705); Salazar et al. derive PMP race policies (DOI '
                 '10.1109/TCST.2016.2642830).'),
                ('2020–2021',
                 'Li et al. introduce Fourier Neural Operators (arXiv:2010.08895) and Lu et al. '
                 'introduce DeepONet (DOI 10.1038/s42256-021-00302-5).')],
 'act2_title': 'Act II — How It Actually Works: Pontryagin Co-State Switching + Fourier Neural '
               'Operator Spectral Convolutions',
 'act2_intuition': 'In track arc-length s (ds/dt = v), time minimization uses the '
                   'minimum-Hamiltonian H = (1/v) + lambda_v * (F_ice + P_k/v - 0.5*rho*v^2*A*C_D '
                   '- F_brake)/(m*v) - lambda_E * P_batt(P_k)/v. Under min_u H with cost +1/v, '
                   'lambda_v and lambda_E are negative; motoring (P_k >= 0) draws P_batt = '
                   'P_k/eta_k while braking (P_k < 0) harvests P_batt = eta_regen * P_k. Inside '
                   '[E_min, E_max], d(lambda_E)/ds = -dH/dE_batt = 0 keeps lambda_E* constant. '
                   'With affine losses, dH/dP_k = lambda_v/(m*v^2) - lambda_E*/(eta_k*v) favors '
                   'full boost until lambda_v/(m*v) = lambda_E*/eta_k, where d(dH/dP_k)/ds = 0 '
                   'gives a constant-speed singular cruise; smooth tapering during acceleration '
                   'requires strictly convex losses P_batt(P_k) (Salazar et al. 2017). An FNO '
                   'layer u_{l+1} = sigma(W u_l + F^(-1)(R_phi * F(u_l))) truncated at k_max '
                   'modes could supply drag gradients dC_D/d(delta_wing) to the optimizer '
                   '(proposed, untested).',
 'act2_deepening': 'Race-strategy simulations typically tabulate drag and downforce as polynomial '
                   'fits to wind-tunnel data (Perantoni & Limebeer 2014). On track, pitch and '
                   'active flap motion shift floor separation points. Truncating a Fourier Neural '
                   'Operator at k_max modes acts on PDE benchmarks as a spectral filter: low '
                   'wavenumbers capture large-scale pressure fields while higher wavenumbers '
                   'resolve finer shear layers. As the simulated car accelerates past 290 '
                   'kilometers per hour, thrust per kilowatt falls as 1/v while drag grows as '
                   'v^2. In hybrid models with convex internal-resistance and inverter losses '
                   '(Duhr et al. 2021, DOI 10.1016/j.apenergy.2020.115980), continuing to dump '
                   '350 kilowatts into quadratic aerodynamic drag carries a steep marginal cost, '
                   'so the co-state policy tapers power before straight-end clipping.',
 'act2_analogy': 'A trail runner carrying one twenty-ounce water flask across mountain ridges '
                 'faces the same pacing dilemma. Drinking greedily on the flat valley floor '
                 'empties the flask before the sunny climb, leaving the runner dehydrated and '
                 'staggering below the summit. Hoarding water too stingily leaves unused ounces '
                 "at the finish line. Pontryagin's shadow price estimates the marginal time saved "
                 'per sip on steep grades. Where the analogy stops: a runner cannot refill a '
                 'flask on descents, whereas regenerative braking recharges the battery entering '
                 'corners.',
 'act2_plain_primer': 'Two controls sit on the simulator panel below. The first slider, MGU-K '
                      'Peak Electric Power, sets the motor ceiling from 120 kilowatts up to 350 '
                      'kilowatts. Raising it trades launch thrust against faster battery drain. '
                      'The second slider, Fourier Spectral Modes, adjusts the wavenumber cutoff '
                      'from eight modes to sixty-four modes in the proposed airflow simulator. '
                      'Dragging either slider updates its unit label and the live stage vector '
                      'overlay, while the four readout cards keep the stated illustrative '
                      'reference values.',
 'distill_diagram': {'analogy_title': 'The Marathon Runner Flask',
                     'analogy_sub': 'Spending finite energy sips on climbs without early '
                                    'dehydration',
                     'force_a_title': 'Peak Electric Power P_k',
                     'force_a_sub': 'Drives rapid acceleration but exhausts limited battery '
                                    'reserves',
                     'force_b_title': 'Fourier Spectral Modes k_max',
                     'force_b_sub': 'Resolves aerodynamic drag fields across non-local wavenumber '
                                    'space',
                     'threshold_title': 'Switching Velocity Taper vs. Clipping',
                     'threshold_pass': 'Model: singular taper saves about 0.42 s without battery '
                                       'clipping (illustrative)',
                     'threshold_fail': 'Model: early boost depletion clips power mid-straight '
                                       '(illustrative loss)'},
 'walkthrough': ['Experiment 1 (MGU-K Peak Electric Power): Drag MGU-K Peak Electric Power (P_k) '
                 'from 120 kW (2014 limit) to 350 kW (reported 2026 limit) to update the power '
                 'label and stage vector overlay beside the illustrative curves.',
                 'Experiment 2 (Fourier Spectral Modes): Adjust Fourier Spectral Modes (k_max) '
                 'from 8 to 64 modes to update the mode label and harmonic wave; the 0.82% card '
                 'remains the fixed k_max = 32 illustrative reference.',
                 'Experiment 3 (Four-Stage Stepper): Step through Stages 1 to 4 to inspect the '
                 'proposed FNO layer, distance-domain Hamiltonian H and constant λ_E*, convex-loss '
                 'tapering vs. clipping, and regenerative braking harvest.'],
 'act4_title': 'Act IV — Applied Mathematics, Operator Learning & Upstream Discovery Threads',
 'act4_human_ai': 'Neural operators such as FNO and DeepONet (Lu et al. 2021, DOI '
                  '10.1038/s42256-021-00302-5) learn mappings between function spaces. If '
                  'surrogates could approximate flow gradients inside Pontryagin or HJB solvers, '
                  'engineers might explore energy and aero trade-offs faster than offline CFD '
                  'simulations; that coupling remains untested.',
 'act4_deepening': 'Coupling Banach-space neural operators (Kovachki et al. 2023) with HJB '
                   'viscosity formulations (Crandall & Lions 1983) suggests a clear split between '
                   'learned surrogates and human engineers. Offline simulations could sweep wing '
                   'angles and wind conditions, yet any candidate energy policy carries a strict '
                   'caveat: its optimality is bounded by surrogate error under stated assumptions. '
                   'Engineers still define state constraints, battery thermal limits, and '
                   'saturation guards (Duhr et al. 2021). Two open questions remain: how may a '
                   'posteriori spectral residuals flag out-of-distribution stall or wake regimes, '
                   'and what Lipschitz bounds on surrogate gradients preserve stability when '
                   'actuators saturate?',
 'cf_bridge': 'Standalone Applied Mathematics & AI Monograph: Written for control theorists, '
              'applied mathematicians, motorsport engineers, and operator-learning researchers. '
              'This folio makes no health or Cystic Fibrosis claim; any comparison between '
              'bang–singular switching laws and medical devices would be a loose analogy and is '
              'not advice.',
 'sources': ['Limebeer, D. J. N., Perantoni, G., & Rao, A. V. (2014). Optimal control of Formula '
             'One car energy recovery systems. International Journal of Control, 87(10), '
             '2065–2080. DOI: 10.1080/00207179.2014.900705.',
             'Perantoni, G., & Limebeer, D. J. N. (2014). Optimal control for a Formula One car '
             'with variable parameters. Vehicle System Dynamics, 52(5), 653–678. DOI: '
             '10.1080/00423114.2014.889315.',
             'Salazar, M., Elbert, P., Ebbesen, S., Bussi, C., & Onder, C. H. (2017). '
             'Time-optimal control policy for a hybrid electric race car. IEEE Transactions on '
             'Control Systems Technology, 25(6), 1921–1934. DOI: 10.1109/TCST.2016.2642830.',
             'Duhr, P., Christodoulou, G., Balerna, C., Salazar, M., Cerofolini, A., & Onder, '
             'C. H. (2021). Time-optimal gearshift and energy management strategies for a hybrid '
             'electric race car. Applied Energy, 282, 115980. DOI: '
             '10.1016/j.apenergy.2020.115980.',
             'Pontryagin, L. S., Boltyanskii, V. G., Gamkrelidze, R. V., & Mishchenko, E. F. '
             '(1962). The Mathematical Theory of Optimal Processes. Interscience / Wiley.',
             'Bellman, R. (1954). The theory of dynamic programming. Bulletin of the American '
             'Mathematical Society, 60(6), 503–515. DOI: 10.1090/S0002-9904-1954-09848-8.',
             'Crandall, M. G., & Lions, P.-L. (1983). Viscosity solutions of Hamilton-Jacobi '
             'equations. Transactions of the American Mathematical Society, 277(1), 1–42. DOI: '
             '10.1090/S0002-9947-1983-0690039-8.',
             'Li, Z., Kovachki, N., Azizzadenesheli, K., Liu, B., Bhattacharya, K., Stuart, A., & '
             'Anandkumar, A. (2020). Fourier Neural Operator for Parametric Partial Differential '
             'Equations. arXiv:2010.08895. DOI: 10.48550/arXiv.2010.08895.',
             'Lu, L., Jin, P., Pang, G., Zhang, Z., & Karniadakis, G. E. (2021). Learning '
             'nonlinear operators via DeepONet based on the universal approximation theorem of '
             'operators. Nature Machine Intelligence, 3(3), 218–229. DOI: '
             '10.1038/s42256-021-00302-5.',
             'Kovachki, N., Li, Z., Liu, B., Azizzadenesheli, K., Bhattacharya, K., Stuart, A., & '
             'Anandkumar, A. (2023). Neural Operator: Learning Maps Between Function Spaces. '
             'Journal of Machine Learning Research, 24(89), 1–97.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Illustrative '
        'Pontryagin 350 kW MGU-K boost taper schematic vs naive battery clipping and Fourier '
        'Neural Operator spectral layer">\n'
        '            <line x1="50" y1="180" x2="365" y2="180" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <line x1="50" y1="28" x2="50" y2="180" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <path d="M 55 155 L 115 45 L 235 45 L 245 142 L 355 142" fill="none" '
        'stroke="var(--tp-minium)" stroke-width="2.2" stroke-dasharray="4,3"/>\n'
        '            <path id="tp-m07-pmp-curve" d="M 55 155 Q 135 38 225 44 Q 285 52 335 72 L 355 '
        '170" fill="none" stroke="var(--tp-verdigris)" stroke-width="3"/>\n'
        '            <circle id="tp-m07-switch-dot" cx="245" cy="48" r="5.5" '
        'fill="var(--tp-prussian)"/>\n'
        '            <text x="55" y="24" font-size="11" font-weight="600" '
        'fill="currentColor">Illustrative 350 kW MGU-K Boost &amp; Taper Schematic</text>\n'
        '            <text id="tp-m07-pk-text" x="62" y="64" font-size="10" '
        'fill="var(--tp-verdigris)">PMP Co-State Taper (P_k = 350 kW → Convex-Loss Arc)</text>\n'
        '            <text x="165" y="134" font-size="9.5" fill="var(--tp-minium)">Naive Early '
        'Clipping (≈0.42 s, illustrative)</text>\n'
        '            <text x="55" y="200" font-size="10" fill="currentColor">Straight Arc-Length s '
        '(0 → 1,150 m) · Co-State λ_E* Calibrated</text>\n'
        '            <line x1="385" y1="22" x2="385" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="402" y="24" font-size="11" font-weight="600" '
        'fill="currentColor">FNO Layer: u_{l+1} = σ(W u_l + F⁻¹(R_φ · F(u_l)))</text>\n'
        '            <rect x="405" y="46" width="64" height="92" rx="3" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="1.8"/>\n'
        '            <rect x="498" y="46" width="68" height="92" rx="3" fill="var(--tp-verdigris)" '
        'fill-opacity="0.14" stroke="var(--tp-verdigris)" stroke-width="2"/>\n'
        '            <rect x="595" y="46" width="64" height="92" rx="3" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="1.8"/>\n'
        '            <line x1="469" y1="92" x2="498" y2="92" stroke="currentColor" '
        'stroke-width="2"/>\n'
        '            <line x1="566" y1="92" x2="595" y2="92" stroke="currentColor" '
        'stroke-width="2"/>\n'
        '            <text x="415" y="96" font-size="9.5" fill="currentColor">FFT F(u_l)</text>\n'
        '            <text x="506" y="88" font-size="9.5" font-weight="600" '
        'fill="var(--tp-verdigris)">R_φ · k_max</text>\n'
        '            <text id="tp-m07-modes-text" x="506" y="106" font-size="9" '
        'fill="currentColor">32 Modes</text>\n'
        '            <text x="603" y="96" font-size="9.5" fill="currentColor">IFFT F⁻¹</text>\n'
        '            <text id="tp-m07-err-text" x="405" y="168" font-size="10" '
        'fill="var(--tp-prussian)">Illustrative Reference Error: 0.82% (k_max = 32)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a Pontryagin optimal control phase portrait and '
        '3D Fourier Neural Operator spectral lattice governing a 2026 Formula 1 350 kW MGU-K '
        'hybrid powertrain would look like (artistic impression, not a formal plot)',
 'caption': 'Conceptual Vision Plate M.07-V (Imagining What It Would Look Like) · Artistic '
            'mathematical visualization imagining a Fourier Neural Operator spectral lattice '
            'feeding real-time aerodynamic manifolds into a Pontryagin Maximum Principle 350 kW '
            'MGU-K optimal energy trajectory.'}

DISPATCH = {'kicker': 'FRONTIER OPTIMAL CONTROL & AI DISPATCH · F1 350 KW PONTRYAGIN CONTROL & FOURIER NEURAL '
           'OPERATORS',
 'headline': 'A Design Study: Pontryagin Energy Control for a 350 kW Hybrid Race Car, With Neural '
             'Operator Surrogates',
 'body': "This folio pairs Limebeer, Perantoni & Rao's optimal control of Formula One energy "
         'recovery (Int. J. Control DOI 10.1080/00207179.2014.900705) with Li et al.\'s Fourier '
         'Neural Operator (arXiv:2010.08895) as a proposal for faster co-state switching under '
         'the reported 2026 350 kW limit. Its lap-time and error figures are illustrative.'}

META_3D = ('Formula 1 350 kW Pontryagin & FNO Optimal Lap Manifold',
 'X: Track Lap Distance s · Z: Battery Co-State λ_E · Y: Optimal MGU-K Power P_k*(s) & Lap Time Δt')

ES_TRANSLATION = {'title_es': 'Control Óptimo de Energía de Pontryagin para MGU-K de 350 kW en Fórmula 1, '
             'Minimización de Tiempo de Vuelta HJB y Operadores Neuronales de Fourier',
 'subtitle_es': 'Un estudio de diseño: cómo el Principio del Máximo de Lev Pontryagin podría '
                'programar el impulso eléctrico de un auto híbrido de carreras (350 kW según las '
                'reglas de la Fórmula 1 2026, tal como se han reportado) sin agotar la batería a '
                'media recta, y cómo los Operadores Neuronales de Fourier podrían sustituir a '
                'simuladores de flujo lentos. Las cifras son valores ilustrativos del modelo.',
 'why_es': 'Un corredor de montaña con una cantimplora dosifica cada sorbo según el tiempo que '
           'ahorra en subida; el co-estado λ_E cumple ese papel en pista, aunque a diferencia de '
           'la cantimplora el frenado regenerativo recarga la batería.',
 'plain_es': 'En 1956, Lev Pontryagin y sus colegas Boltyanskii, Gamkrelidze y Mishchenko '
             'estudiaron en Moscú cómo guiar máquinas sujetas a topes físicos (libro de 1962). '
             'Piensen en manejar un auto híbrido ochenta kilómetros por el desierto con una '
             'batería pequeña y sin estaciones de carga. Pisar a fondo al salir vacía la carga a '
             'mitad de ruta. Con la batería agotada, el auto pierde ritmo frente a conductores con '
             'reserva. El control óptimo pregunta cómo repartir energía finita para terminar en el '
             'menor tiempo posible. En vez de decidir por reflejo, se calcula un precio sombra por '
             'watt-hora almacenado. A alta velocidad la resistencia del aire crece y cada kilowatt '
             'extra aporta poca aceleración. Moderar el apoyo eléctrico en recta conserva carga '
             'para salir de curvas lentas. Después, el frenado regenerativo recupera energía al '
             'entrar a la curva.',
 'deep_es': 'El control de tiempo mínimo en coordenadas curvilíneas ds/dt = v para Fórmula 1 fue '
            'formulado por Perantoni y Limebeer (2014, DOI 10.1080/00423114.2014.889315) y '
            'extendido a recuperación híbrida bajo el tope de 120 kilowatts por Limebeer, '
            'Perantoni y Rao (2014, DOI 10.1080/00207179.2014.900705). La programación dinámica '
            'de Bellman (1954, DOI 10.1090/S0002-9904-1954-09848-8) conduce a la ecuación HJB, '
            'interpretada mediante soluciones de viscosidad (Crandall y Lions 1983, DOI '
            '10.1090/S0002-9947-1983-0690039-8). Este estudio usa el techo reportado de 350 '
            'kilowatts para 2026 (sin verificar el reglamento FIA) y asume 4.0 MJ por vuelta. '
            'Con pérdidas convexas (Salazar et al. 2017, DOI 10.1109/TCST.2016.2642830; Duhr et '
            'al. 2021, DOI 10.1016/j.apenergy.2020.115980), λ_E* atenúa la potencia antes del '
            'corte; 298.4 km/h, −0.42 s y 0.82% (k_max = 32) son ilustrativos y no se entrenó '
            'ningún FNO (Li et al. 2020) ni DeepONet (Lu et al. 2021).',
 'bridge_es': 'Monografía para especialistas en control óptimo, matemática aplicada, automovilismo '
              'y operadores neuronales. Este folio no hace ninguna afirmación de salud ni sobre la '
              'Fibrosis Quística; cualquier comparación con dispositivos médicos sería una analogía '
              'vaga y no es un consejo.'}
