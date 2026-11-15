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
 'governing_law': 'H(x, u, λ) = 1/v + λ_v f_v(v, P_k, δ) − λ_E P_k/(η v) · u_θ = F⁻¹(R_φ · F(a))',
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
 'steps': ['Stage 1 (Fourier Neural Operator Surrogate, proposed): An FNO layer u_{t+1} = σ(W u_t + '
           'F⁻¹(R_φ · F u_t)) could be trained to map wing angle δ_wing and ride height h_ride to '
           'drag and downforce coefficients. No such surrogate was trained for this folio.',
           'Stage 2 (Distance-Domain Pontryagin Hamiltonian H): Formulates minimum-time lap '
           'control with ds/dt = v. While the battery stays inside its limits, the battery '
           'co-state λ_E* is constant; the folio calibrates it to an assumed 4.0 MJ-per-lap '
           'energy budget.',
           'Stage 3 (Bang–Singular–Bang Taper vs. Clipping): Above a switching speed the model '
           'tapers P_k*(s) instead of deploying full power until the battery clips. The 298 km/h '
           'switching speed and the 0.42 s saving are illustrative model values.',
           'Stage 4 (Regenerative Braking Harvest): Under braking the MGU-K recovers energy so '
           'that the periodic boundary condition E_batt(L) = E_batt(0) closes the lap.'],
 'readouts': [{'label': 'Straight-Line Lap Gain (Δt_lap, model)',
               'value': '−0.42 s vs. naive clipping (illustrative)'},
              {'label': 'Optimal Taper Velocity (v_switch, model)',
               'value': '298.4 km/h (illustrative)'},
              {'label': 'FNO Operator Error (k_max = 32, model)',
               'value': '0.82% (illustrative; no surrogate trained here)'},
              {'label': 'Pontryagin Model Outcome',
               'value': 'Taper avoids clipping in the model (not a race result)'}],
 'spec_plate': {'division': 'FIA 2026 ARTICLE 5 / SCIENTIFIC ML & OPTIMAL CONTROL',
                'title': '2026 Formula 1 350 kW MGU-K Energy Store & Real-Time FNO-Pontryagin Lap '
                         'Optimizer',
                'body': 'Design study: a 350 kW kinetic motor-generator unit governed by a '
                        'distance-domain Pontryagin co-state controller that could query a 32-mode '
                        'Fourier Neural Operator aerodynamic surrogate. Nothing here was built or '
                        'run on a car.',
                'meta': 'Method sources cited, not reproduced: Limebeer, Perantoni & Rao 2014 (DOI '
                        '10.1080/00207179.2014.900705) · Li et al. FNO (arXiv:2010.08895)'},
 'sidenote_1': {'kicker': 'SIDENOTE M.07-A · WHY THE BATTERY CO-STATE λ_E IS CONSTANT ACROSS THE '
                          'LAP',
                'body': "By Pontryagin's co-state equation dλ_E/ds = −∂H/∂E_batt, whenever the "
                        'battery state of charge E_batt(s) stays strictly inside its [E_min, '
                        'E_max] corridor, ∂H/∂E_batt = 0—meaning a single scalar shadow price λ_E* '
                        'governs every straight and corner on the circuit!'},
 'sidenote_2': {'kicker': 'SIDENOTE M.07-B · SPECIFICATION PLATE · FOURIER NEURAL OPERATOR '
                          'ZERO-SHOT SUPER-RESOLUTION',
                'body': 'Because R_φ acts directly on the lowest k_max Fourier modes, the '
                        'operator can be evaluated on a finer grid than it was trained on; Li et '
                        'al. (arXiv:2010.08895) report this zero-shot super-resolution on their '
                        'benchmark flows. Whether it holds for race-car aerodynamics is untested '
                        'here.'},
 'skill': {'filename': 'f1-pontryagin-fno-control-SKILL.md',
           'name': 'f1-pontryagin-fno-control',
           'description': 'AI-agnostic applied mathematics and operator-learning skill for Formula '
                          '1 350 kW MGU-K Pontryagin optimal energy management, HJB lap-time '
                          'minimization, and Fourier Neural Operator PDE surrogates.',
           'rules': ['Formulate distance-domain Pontryagin Hamiltonian H = (1/v) + lambda_v * '
                     'a_net(v, P_k, delta_wing) / v - lambda_E * P_k / (eta_k * v).',
                     'Determine the MGU-K switching velocity v_switch from the switching function '
                     'dH/dP_k = lambda_v / (m * v^2) - lambda_E / (eta_k * v), which vanishes '
                     'where lambda_v / (m * v) = lambda_E / eta_k, to prevent straight-end '
                     'clipping.',
                     'Evaluate spectral neural operator layer u_{l+1}(x) = sigma(W * u_l(x) + '
                     'F^{-1}(R_phi * F(u_l))(x)) truncated at k_max Fourier modes.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The lap-time gain, '
                           'switching speed, FNO error and speedup are now labelled as '
                           'illustrative model values; no surrogate was trained and no lap was '
                           'simulated. The 2014 Limebeer, Perantoni & Rao paper is no longer '
                           'cited for the 2026 rules it predates, the switching condition is '
                           'corrected to lambda_v/(m v) = lambda_E/eta, the invented opening scene '
                           'is replaced by a plain account, and the nebulizer and Cystic Fibrosis '
                           'dosing bridge is withdrawn.',
                'opus': 'Review: DOIs checked in Crossref and arXiv:2010.08895 checked on '
                        '2026-11-14. No DOIs added.'},
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
           'fetched_on': '2026-11-08',
           'citing_publications': 87,
           'supporting': 0,
           'mentioning': 52,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 87 citing '
                      'publications (0 supporting, 52 mentioning, 0 contrasting) on David '
                      "Limebeer, Giacomo Perantoni & Anil Rao's optimal control of Formula One "
                      'hybrid energy recovery systems.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1080/00207179.2014.900705',
           'fetched_on': '2026-11-08',
           'citing_publications': 87,
           'supporting': 0,
           'mentioning': 52,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 87 citing '
                      'publications (0 supporting, 52 mentioning, 0 contrasting) on David '
                      "Limebeer, Giacomo Perantoni & Anil Rao's optimal control of Formula One "
                      'hybrid energy recovery systems.'},
 'act1_title': "Act I — From Lev Pontryagin's Maximum Principle to 2026 Formula 1 350 kW Hybrid "
               'Control & Neural PDE Operators',
 'act1_dropcap': 'Lev Semenovich Pontryagin, blind from an accident at the age of fourteen, led '
                 'a group at the Steklov Mathematical Institute in Moscow with Vladimir '
                 'Boltyanskii, Revaz Gamkrelidze and Evgenii Mishchenko. Their maximum principle, '
                 'first announced in the mid-1950s and set out in their 1962 book The '
                 'Mathematical Theory of Optimal Processes, handles a problem the classical '
                 'calculus of variations of Euler and Lagrange did not: controls that have hard '
                 'limits. Real engines face such limits: valves hit stops, motors overheat, and '
                 'batteries drain. The principle attaches to each state a shadow price, the '
                 'co-state, which tracks the future value of a unit of that resource and tells '
                 'the controller when to use full power, when to hold back, and when to brake.',
 'act1_plain_bridge': 'Think about driving an electric hybrid car down a long desert highway with '
                      'only one small battery pack and no charging stations for fifty miles. If '
                      'you stomp on the accelerator pedal the moment you leave the stoplight, the '
                      'sudden burst of speed feels thrilling, but your battery will run completely '
                      'dry halfway down the road. Once that charge disappears, your car bogs down, '
                      'leaving you crawling along at a sluggish pace while more patient drivers '
                      'glide effortlessly past you. The mathematical question behind optimal '
                      'control is simple: how do you spend a finite budget of energy so that you '
                      'finish the entire trip in the absolute shortest time? Instead of guessing '
                      'with human reflexes, modern racing engineers and autonomous systems '
                      'calculate an exact exchange rate for every watt-hour. By easing off the '
                      'electric boost at high speeds where wind resistance pushes back hardest, a '
                      'vehicle saves precious energy for the moments where acceleration counts '
                      'most.',
 'act1_body': 'Optimal control has been applied to hybrid race cars for more than a decade. In '
              '2014 Limebeer, Perantoni and Rao published an optimal-control study of the energy '
              'recovery systems of a Formula One car (International Journal of Control, DOI '
              '10.1080/00207179.2014.900705), written for the rules of that era, when the kinetic '
              'motor-generator was limited to 120 kilowatts. The 2026 rules, as widely reported, '
              'raise that limit to 350 kilowatts; this folio has not checked the regulation text, '
              'and its 4.0 megajoule per-lap energy budget is a model assumption. In the model, '
              'if the motor deploys full boost too early on a straight, the battery reaches its '
              'limit before the braking zone and the car loses time. Computing drag and downforce '
              'for many wing angles and ride heights with conventional flow solvers is slow. The '
              'Fourier Neural Operator (Li et al., arXiv:2010.08895) learns the solution operator '
              'of a PDE by parameterising an integral kernel in Fourier space; its authors report '
              'speedups of up to three orders of magnitude over conventional solvers on their '
              'benchmark equations. Using such a surrogate inside a Pontryagin controller for a '
              "race car is this folio's proposal, not something shown here.",
 'act1_stakes': 'The stakes of this mathematical convergence extend far beyond qualifying laps and '
                'checkered flags. For decades, optimal control and partial differential equation '
                'modeling lived on opposite sides of a vast computational canyon. Classical '
                'control theorists knew how to write down exact optimality equations for simple '
                'spring-mass systems, but the moment a problem involved turbulent airflow, '
                'swirling thermal boundaries, or complex physical media, the equations became too '
                'heavy to evaluate in real time. Engineers had to rely on clumsy lookup tables, '
                'pre-baked approximations, or conservative safety margins that left dramatic '
                "amounts of performance on the table. Pairing Pontryagin's Hamiltonian "
                'formulation with learned neural operators is one proposed way to close that gap '
                'between continuum physics and fast decisions; it remains a research direction. '
                'The maximum principle on its own is long established, for example in '
                'spacecraft trajectory optimisation.',
 'pullquote': '"In the model, a single shadow price, the co-state lambda_E, decides where on '
              'the straight to ease off the electric boost so the battery lasts the lap."',
 'chronology': [('1956',
                 'Boltyanskii, Gamkrelidze & Pontryagin announce the maximum principle for '
                 'optimal control with bounded controls (book with Mishchenko, 1962).'),
                ('1957',
                 'Richard Bellman formulates Dynamic Programming and the Hamilton–Jacobi–Bellman '
                 '(HJB) partial differential equation.'),
                ('2014',
                 'David Limebeer, Giacomo Perantoni & Anil V. Rao solve minimum-lap-time optimal '
                 'control for Formula 1 hybrid energy recovery (DOI '
                 '10.1080/00207179.2014.900705).'),
                ('2020–2021',
                 'Li, Kovachki, Azizzadenesheli et al. introduce the Fourier Neural Operator for '
                 'parametric PDEs (arXiv:2010.08895; ICLR 2021).')],
 'act2_title': 'Act II — How It Actually Works: Pontryagin Co-State Switching + Fourier Neural '
               'Operator Spectral Convolutions',
 'act2_intuition': 'To minimize total lap time along track distance s, we formulate the '
                   'distance-domain Hamiltonian H(v, E_batt, P_k, delta_wing, lambda_v, lambda_E) '
                   '= (1 / v) + lambda_v * (F_ice + P_k / v - 0.5 * rho * v^2 * A * C_D - F_brake) '
                   '/ (m * v) - lambda_E * P_k / (eta_k * v). Because battery state of charge '
                   "E_batt does not appear explicitly in the velocity dynamics, Pontryagin's "
                   'adjoint equation d(lambda_E)/ds = -dH/dE_batt = 0 means the battery co-state '
                   'lambda_E* stays constant along arcs where the battery limits are not active. '
                   'In this model that one shadow price governs the whole lap. Because H is '
                   'linear in P_k, the switching function is dH/dP_k = lambda_v / (m * v^2) - '
                   'lambda_E* / (eta_k * v); full boost is used while it favours deployment, and '
                   'a singular tapering arc begins where it vanishes, that is where lambda_v / (m '
                   '* v) = lambda_E* / eta_k. Separately, a Fourier Neural Operator could '
                   'approximate the flow solution with layers F^(-1)(R_phi * F(u_t)) truncated at '
                   'k_max modes and supply differentiable drag gradients dC_D / d(delta_wing) to '
                   'the optimiser; that coupling is proposed here, not demonstrated.',
 'act2_deepening': 'The deeper variational beauty lies in how the Fourier Neural Operator and the '
                   'Pontryagin Hamiltonian couple across physical dimensions. Traditional control '
                   'algorithms treat aerodynamic drag as a static polynomial curve fit to wind '
                   'tunnel data. In reality, vehicle ride height, pitch angle, and active '
                   'aerodynamic flap deflections warp the airflow dynamically, changing boundary '
                   'layer separation points down the chassis. Truncating the Fourier Neural '
                   'Operator at k_max modes acts as a spectral filter: low wavenumbers '
                   'capture large recirculating vortices behind the rear wing, while higher '
                   'wavenumbers resolve localized turbulent eddies shedding from the front wing '
                   'endplates. As the simulated car accelerates past 290 kilometers per hour, the '
                   'thrust gained per kilowatt falls (thrust is power divided by speed) while '
                   'aerodynamic drag grows with the square of speed. The Pontryagin co-state '
                   'controller in the model recognizes that continuing to '
                   'dump 350 kilowatts into the teeth of that aerodynamic wall yields diminishing '
                   'returns. It initiates a singular arc that gently bleeds motor power into '
                   'low-drag active aero, preserving battery voltage for high-traction exits.',
 'act2_analogy': 'Everyday analogy: Imagine running a grueling trail marathon through rolling '
                 'mountains with only a single twenty-ounce water flask. If you drink greedily on '
                 'the early flat path because you feel thirsty, your flask runs empty on the sunny '
                 'ridge, leaving you dehydrated and staggering before the summit. But if you horde '
                 'the water too stingily, you finish the race fatigued with ounces to spare. '
                 "Pontryagin's shadow price acts like an internal coach, calculating the exact "
                 'value of each sip so you hydrate precisely on steep ascents where energy yields '
                 'the greatest speed.',
 'act2_plain_primer': 'To see how this works in practice, imagine having two interactive dials on '
                      'the dashboard of your racing simulator. The first dial governs the maximum '
                      'electrical punch delivered by the hybrid motor, scaling from a conservative '
                      '120 kilowatts up to a thunderous 350 kilowatts. When you dial this power '
                      'up, the car launches down the asphalt with astonishing thrust, but your '
                      'energy reservoir drains at nearly triple the speed, threatening to cut '
                      'power abruptly before the next corner. The second dial controls the visual '
                      'and mathematical clarity of the airflow simulator, increasing the number of '
                      'wave frequencies used to map the air rushing over the car from a blurry '
                      'eight modes up to a razor-sharp sixty-four modes. With too few wave modes, '
                      'the computer misjudges wind resistance and gives bad advice. But as you '
                      'turn both dials in harmony, you watch the virtual coach find the exact '
                      'sweet spot: delivering maximum electric acceleration off slow bends, then '
                      'smoothly tapering off the boost at blistering speeds where aerodynamic drag '
                      'makes further electric expenditure wasteful.',
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
 'walkthrough': ['Experiment 1 (350 kW MGU-K Deployment vs. Clipping): Drag MGU-K Electric Power '
                 'P_k from 120 kW (2022–2025 regulations) up to 350 kW (2026 regulations). Compare '
                 'naive early deployment (which clips battery mid-straight) against the Pontryagin '
                 'co-state optimal taper.',
                 'Experiment 2 (Fourier Neural Operator Spectral Resolution): Increase Fourier '
                 'Spectral Modes k_max from 8 modes to 32–64 modes. Watch the illustrative '
                 'operator-error readout fall; the curve is a fixed teaching model, not a trained '
                 'network, and no speedup over CFD was measured.',
                 'Experiment 3 (Coupled PMP + FNO 4-Stage Loop): Step through Stages 1 to 4 to '
                 'inspect FNO spectral convolution in wavenumber space, Pontryagin Hamiltonian '
                 'co-state calibration, X/Z-mode active aero switching, and regenerative braking '
                 'harvest.'],
 'act4_title': 'Act IV — Applied Mathematics, Operator Learning & Upstream Discovery Threads',
 'act4_human_ai': 'If neural operators (FNO / DeepONet) can stand in for slow finite-element '
                  'and finite-volume solvers inside Pontryagin and HJB optimal control solvers, '
                  'race engineers and physicists could explore trade-offs between energy and '
                  'aerodynamic strategy much faster. That is a proposal, not a reported result.',
 'act4_deepening': 'Looking toward the horizon of autonomous engineering, embedding Fourier Neural '
                   'Operators inside Hamilton–Jacobi–Bellman PDE solvers creates a new paradigm of '
                   'human-machine scientific collaboration. Instead of spending hours running '
                   'detached offline simulations, race strategists and control theorists interact '
                   'with real-time Pareto frontiers. In principle, software could sweep many '
                   'weather shifts, tire wear regimes, and active aero configurations during a '
                   'session and propose candidate energy allocation policies, though their '
                   'optimality would only be as good as the surrogate behind them. The human '
                   'engineer retains the critical architectural role: '
                   'defining the invariant cost functionals, monitoring non-convex boundary '
                   'hazards, and evaluating thermal stress limits on experimental silicon-carbide '
                   'inverters. Open mathematical frontiers remain: how do we prove rigorous error '
                   'bounds when neural operators extrapolate outside their training distributions '
                   'during violent vehicle spins, and can Banach-space operator learning guarantee '
                   'Lyapunov stability when physical control actuators saturate? Resolving these '
                   'questions bridges high-speed motorsport control with the safety-critical '
                   'autonomy required for civil aviation, humanoid robotics, and resilient power '
                   'grid networks.',
 'cf_bridge': 'Standalone Applied Mathematics & AI Flagship & Upstream Mathematical Thread: '
              'Engineered for control theorists, applied mathematicians, motorsport strategists, '
              'and scientific machine-learning researchers. This folio makes no health or '
              'Cystic Fibrosis claim. Bang–singular–bang switching laws of the kind used here '
              'appear in many resource-limited control problems; any comparison with medical '
              'devices would be a loose analogy and is not offered as advice.',
 'sources': ['Limebeer, D. J. N., Perantoni, G., & Rao, A. V. (2014). Optimal control of Formula '
             'One car energy recovery systems. International Journal of Control, 87(10), '
             '2065–2080. DOI: 10.1080/00207179.2014.900705.',
             'Li, Z., Kovachki, N., Azizzadenesheli, K., Liu, B., Bhattacharya, K., Stuart, A., & '
             'Anandkumar, A. (2021). Fourier Neural Operator for Parametric Partial Differential '
             'Equations. ICLR 2021. arXiv:2010.08895.',
             'Pontryagin, L. S., Boltyanskii, V. G., Gamkrelidze, R. V., & Mishchenko, E. F. '
             '(1962). The Mathematical Theory of Optimal Processes. Interscience / Wiley.',
             'Kovachki, N., Li, Z., Liu, B., Azizzadenesheli, K., Bhattacharya, K., Stuart, A., & '
             'Anandkumar, A. (2023). Neural Operator: Learning Maps Between Function Spaces. '
             'Journal of Machine Learning Research, 24(89), 1–97.',
             'Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing '
             'equations from data by sparse identification of nonlinear dynamical systems '
             '(dynamicslab/pysindy, https://github.com/dynamicslab/pysindy). PNAS, 113(15), '
             '3932–3937. DOI: 10.1073/pnas.1517384113.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Pontryagin 350 kW '
        'MGU-K optimal deployment profile vs naive battery clipping and Fourier Neural Operator '
        'spectral architecture">\n'
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
        'fill="currentColor">Pontryagin 350 kW MGU-K Velocity Profile v(s)</text>\n'
        '            <text id="tp-m07-pk-text" x="62" y="64" font-size="10" '
        'fill="var(--tp-verdigris)">PMP Optimal Boost (P_k = 350 kW → Singular Taper)</text>\n'
        '            <text x="165" y="134" font-size="9.5" fill="var(--tp-minium)">Naive Early '
        'Clipping (≈0.42 s, illustrative)</text>\n'
        '            <text x="55" y="200" font-size="10" fill="currentColor">Straight Arc-Length s '
        '(0 → 1,150 m) · Co-State λ_E* Calibrated</text>\n'
        '            <line x1="385" y1="22" x2="385" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="402" y="24" font-size="11" font-weight="600" '
        'fill="currentColor">Fourier Neural Operator: u_θ = F⁻¹(R_φ · F(a))</text>\n'
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
        '            <text x="415" y="96" font-size="9.5" fill="currentColor">FFT F(u)</text>\n'
        '            <text x="506" y="88" font-size="9.5" font-weight="600" '
        'fill="var(--tp-verdigris)">R_φ · k_max</text>\n'
        '            <text id="tp-m07-modes-text" x="506" y="106" font-size="9" '
        'fill="currentColor">32 Modes</text>\n'
        '            <text x="603" y="96" font-size="9.5" fill="currentColor">IFFT F⁻¹</text>\n'
        '            <text id="tp-m07-err-text" x="405" y="168" font-size="10" '
        'fill="var(--tp-prussian)">Illustrative Operator Error: 0.82% · Speedup Not Measured</text>\n'
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
 'X: Track Lap Distance s · Z: Co-State λ_soc · Y: Optimal MGU-K Power P_k*(s) & Lap Time Δt')

ES_TRANSLATION = {'title_es': 'Control Óptimo de Energía de Pontryagin para MGU-K de 350 kW en Fórmula 1, '
             'Minimización de Tiempo de Vuelta HJB y Operadores Neuronales de Fourier',
 'subtitle_es': 'Un estudio de diseño: cómo el Principio del Máximo de Lev Pontryagin podría '
                'programar el impulso eléctrico de un auto híbrido de carreras (350 kW según las '
                'reglas de la Fórmula 1 2026, tal como se han reportado) sin agotar la batería a '
                'media recta, y cómo los Operadores Neuronales de Fourier podrían sustituir a '
                'simuladores de flujo lentos. Las cifras son valores ilustrativos del modelo.',
 'why_es': 'Al correr un maratón con una cantimplora pequeña, el co-estado de Pontryagin λ_E es el '
           "'precio exacto por sorbo' que indica en qué tramo de la pista cada watt ahorra más "
           'milisegundos.',
 'plain_es': 'En 1956, el matemático Lev Pontryagin y su equipo en Moscú resolvieron un problema '
             'fundamental para la ingeniería moderna: cómo guiar un vehículo o cohete con la '
             'máxima rapidez cuando los motores y combustibles tienen límites mecánicos estrictos. '
             'Imaginen que ustedes manejan un automóvil híbrido en una autopista larga con una '
             'batería pequeña y sin estaciones de recarga cercanas. Si pisan el acelerador a fondo '
             'desde el primer segundo, el arranque se siente impresionante, pero la batería se '
             'descargará por completo antes de llegar a la mitad del trayecto, obligándolos a '
             'avanzar lentamente el resto del camino. El Principio del Máximo de Pontryagin '
             'calcula una especie de tipo de cambio invisible o precio sombra para cada unidad de '
             'energía. En lugar de acelerar a ciegas, el sistema matemático determina el momento '
             'exacto en que conviene empujar con toda la potencia eléctrica, cuándo reducir '
             'suavemente el consumo en rectas de alta velocidad donde el viento frena con más '
             'fuerza, y cuándo regenerar energía al frenar para completar toda la vuelta en el '
             'menor tiempo posible.',
 'deep_es': 'La optimización matemática de este sistema acopla dos parámetros fundamentales: la '
            'potencia máxima del motor eléctrico de 350 kilovatios y los modos espectrales del '
            'Operador Neuronal de Fourier que resuelven los campos de turbulencia aerodinámica. '
            'A alta velocidad, la resistencia del aire crece con el cuadrado de la velocidad y el '
            'empuje por kilovatio disminuye, así que seguir inyectando energía eléctrica a máxima '
            'capacidad rinde cada vez menos. En el modelo, si el motor mantiene el empuje al '
            'límite sin contemplar el costo marginal, la batería se agota a mitad de la recta y '
            'se pierde tiempo. En contraste, el regulador de co-estado de Pontryagin identifica '
            'el umbral: pasa de la potencia máxima a un arco singular que modula la descarga. La '
            'velocidad de cambio de 298 km/h y la ganancia de 0.42 s son valores ilustrativos. '
            'Combinar esta formulación con operadores neuronales que aproximen el flujo es una '
            'propuesta de este folio; sus autores reportan aceleraciones de hasta tres órdenes '
            'de magnitud en sus propios problemas de prueba, no en autos de carreras.',
 'bridge_es': 'Este folio no hace ninguna afirmación de salud ni sobre la Fibrosis Quística. Las '
              'leyes de conmutación bang-singular aparecen en muchos problemas de control con '
              'recursos limitados; cualquier comparación con dispositivos médicos sería una '
              'analogía vaga y no es un consejo.'}
