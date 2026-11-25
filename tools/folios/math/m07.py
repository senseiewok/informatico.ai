#!/usr/bin/env python3
"""Folio M.07 (MATH): Formula 1 350 kW MGU-K Pontryagin Optimal Energy Control, Hamilton–Jacobi–Bellman Lap Time Minimization & Fourier Neural Operator Surrogates."""
from __future__ import annotations

SLUG = 'm07'

PILLAR = 'math'

FOLIO = {
    'folio_id': 'M.07',
    'slug': 'm07',
    'pillar': 'math',
    'category_code': 'M',
    'title': (
        'Formula 1 350 kW MGU-K Pontryagin Optimal Energy Control, Hamilton–Jacobi–Bellman Lap '
        'Time Minimization & Fourier Neural Operator Surrogates'
    ),
    'subtitle': (
        "An applied-mathematics explanation, not a vehicle design method. Pontryagin's Maximum "
        'Principle models hybrid boost pacing (up to the reported 2026 350 kW ceiling) on a '
        'finite battery, with Fourier Neural Operators proposed as flow surrogates. All figures '
        'are illustrative; none belong on a real vehicle, battery, or controller.'
    ),
    'date_published': '2026-11-02',
    'date_redated': '2026-11-14',
    'current_edition': 'REV 1.1',
    'status_badge': 'F1 OPTIMAL CONTROL & AI · REV 1.1',
    'primary_kernel': 'tools/folios/math/m07.py',
    'kernel_verdict': 'Not independently verified',
    'kernel_verdict_es': 'Sin verificación independiente',
    'governing_law': (
        'H(x, u, λ) = 1/v + λ_v a_net(v, P_k, δ)/v − λ_E P_batt(P_k)/v ; '
        'u_{l+1} = σ(W u_l + F⁻¹(R_φ · F(u_l)))'
    ),
    'colophon': {
        'identifier': 'M.07 · Hybrid Pontryagin Control & FNO Surrogates (Teaching Model)',
        'kernels': 'Pontryagin Maximum Principle (PMP) · HJB PDE · Fourier Neural Operator',
        'benchmarks': (
            'Illustrative constants: P_k,max = 350 kW · ΔE_lap = 4.0 MJ (assumed) · '
            'FNO error 0.82% (untrained)'
        ),
        'bridge': 'Hybrid Co-State Switching ↔ P.07 Active Aero (conceptual analogy only)',
    },
    'sliders': [
        {
            'label': 'MGU-K Peak Electric Power (P_k)',
            'min': 120.0,
            'max': 350.0,
            'step': 10.0,
            'value': 350.0,
            'unit': ' kW',
        },
        {
            'label': 'Fourier Spectral Modes (k_max)',
            'min': 8,
            'max': 64,
            'step': 4,
            'value': 32,
            'unit': ' modes',
        },
    ],
    'steps': [
        (
            'Stage 1 (Proposed FNO Surrogate): Layer u_{l+1} = σ(W u_l + F⁻¹(R_φ · F(u_l))) '
            'could map wing angle and ride height to flow fields (Li et al. 2020); untrained here.'
        ),
        (
            'Stage 2 (Distance-Domain Hamiltonian H): Rewrites minimum-time control in ds/dt = v; '
            'on interior battery arcs, constant λ_E* < 0 allocates an assumed 4.0 MJ budget.'
        ),
        (
            'Stage 3 (Convex-Loss Motoring Taper): For P_k ≥ 0, assumed draw '
            'P_batt(P_k) = P_k/η_k + α P_k² (α > 0) tapers P_k*(s) on (v_switch, v_zero) '
            '(298.4 km/h and −0.42 s are fixed illustrative figures).'
        ),
        (
            'Stage 4 (Corner Braking & Harvest): On braking arcs (F_brake > 0, λ_v > 0, P_k < 0), '
            'P_batt = η_regen P_k recovers kinetic energy toward E_batt(L) = E_batt(0).'
        ),
    ],
    'readouts': [
        {
            'label': 'Straight-Line Lap Gain (Δt_lap, model)',
            'value': '−0.42 s vs. naive clipping (fixed illustrative)',
        },
        {
            'label': 'Optimal Taper Velocity (v_switch, model)',
            'value': '298.4 km/h (fixed illustrative)',
        },
        {
            'label': 'FNO Operator Error (k_max = 32, model)',
            'value': '0.82% (fixed illustrative; no surrogate trained)',
        },
        {
            'label': 'Pontryagin Model Outcome',
            'value': 'Taper avoids clipping in the model (not a vehicle design)',
        },
    ],
    'spec_plate': {
        'division': 'APPLIED OPTIMAL CONTROL & OPERATOR LEARNING · TEACHING MODEL',
        'title': 'Hybrid 350 kW MGU-K Energy Store & Proposed FNO-Pontryagin Teaching Model',
        'body': (
            'Teaching model: a 350 kW motor-generator schedule framed via Pontryagin co-states '
            'and a proposed 32-mode Fourier Neural Operator. Not a vehicle design method; nothing '
            'ran on a car and no figure belongs on hardware.'
        ),
        'meta': (
            'Cited, not reproduced: Limebeer, Perantoni & Rao 2014 (DOI '
            '10.1080/00207179.2014.900705) · Li et al. 2020 (arXiv:2010.08895)'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE M.07-A · CONSTANT INTERIOR BATTERY CO-STATE λ_E*',
        'body': (
            "By Pontryagin's adjoint equation dλ_E/ds = −∂H/∂E_batt, when E_batt(s) stays inside "
            '(E_min, E_max) and losses omit state of charge, ∂H/∂E_batt = 0 keeps λ_E* < 0 constant.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE M.07-B · FNO ZERO-SHOT SUPER-RESOLUTION',
        'body': (
            'Because R_φ acts on the lowest k_max Fourier modes, Li et al. (2020, '
            'arXiv:2010.08895) report zero-shot super-resolution on Navier–Stokes benchmarks; '
            'race-car aerodynamics remains untested here.'
        ),
    },
    'skill': {
        'filename': 'f1-pontryagin-fno-control-SKILL.md',
        'name': 'f1-pontryagin-fno-control',
        'description': (
            'AI-agnostic applied-mathematics teaching skill for hybrid Pontryagin energy pacing, '
            'Hamilton-Jacobi-Bellman formulations, and proposed Fourier Neural Operator PDE '
            'surrogates (not a vehicle or controller design method).'
        ),
        'rules': [
            (
                'Treat this skill strictly as an educational explanation, not as a vehicle, '
                'battery, or powertrain controller design method; none of its assumed or '
                'untested illustrative figures (-0.42 s, 298.4 km/h, 4.0 MJ, 0.82%, not verified) '
                'may be applied to real hardware, under the stated assumptions of '
                'H = (1/v) + lambda_v * a_net / v - lambda_E * P_batt(P_k) / v with interior '
                'd(lambda_E)/ds = 0 (lambda_E* < 0).'
            ),
            (
                'Separate motoring arcs (lambda_v < 0, F_brake = 0, P_k >= 0), the subgradient '
                'coasting deadband (P_k* = 0 when lambda_E* / eta_k <= lambda_v / (m * v) <= '
                'lambda_E* * eta_regen), lift-and-coast regen (lambda_E* * eta_regen < '
                'lambda_v / (m * v) < 0, F_brake = 0, P_k < 0), and corner friction braking '
                '(lambda_v > 0, F_brake > 0, P_k < 0, P_batt = eta_regen * P_k): under the '
                'stated assumptions, quadratic draw P_k / eta_k + alpha * P_k^2 (alpha > 0) '
                'could taper P_k*(s) = (lambda_v / (lambda_E* * m * v) - 1/eta_k) / (2α) on '
                '(v_switch, v_zero) with v_switch = lambda_v / (lambda_E* * m * (1/eta_k + '
                '2α P_{k,max})) and v_zero = lambda_v * eta_k / (lambda_E* * m).'
            ),
            (
                'Write the Fourier Neural Operator layer u_{l+1}(x) = sigma(W * u_l(x) + '
                'F^{-1}(R_phi * F(u_l))(x)) truncated at k_max modes (Li et al. 2020, '
                'arXiv:2010.08895), noting the caveat that race-car aerodynamic simulation '
                'coupling is not yet tested and remains untested here.'
            ),
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.1',
            'date': '2026-11-14',
            'summary': (
                'REV 1.1 (Redated 2026-11-14): Grounding revision. Lap-time, switching-speed, and '
                'FNO figures are labeled fixed illustrative values (no surrogate trained, no lap '
                'simulated); citations follow primary abstracts and titles, motoring vs. braking '
                'co-state sign domains are separated, and the non-design-method vehicle boundary '
                'is stated.'
            ),
            'opus': (
                'Bibliographic scope: DOIs in Crossref and arXiv:2010.08895 matched to abstracts '
                'for Limebeer et al. (2014), Perantoni & Limebeer (2014), Salazar et al. (2017), '
                'Duhr et al. (2021), Bellman (1954), Crandall & Lions (1983), Li et al. (2020), '
                'Kovachki et al. (2023), and title-level DeepONet in Lu et al. (2021).'
            ),
        },
        {
            'edition': 'REV 1.0',
            'date': '2026-11-02',
            'summary': (
                'REV 1.0 (Published 2026-11-02): Inaugural Volume IV Formula 1 applied '
                'mathematics & AI monograph uniting Limebeer-Perantoni-Rao optimal hybrid control '
                '(DOI 10.1080/00207179.2014.900705) with Fourier Neural Operators '
                '(arXiv:2010.08895).'
            ),
            'opus': (
                'Initial edition note: constant interior co-state d(lambda_E)/ds = 0 alongside '
                '-0.42 s and 0.82% illustrative figures (REV 1.1: earlier verification wording is '
                'withdrawn; -0.42 s and 0.82% were not computed by any run).'
            ),
        },
    ],
    'volume': 4,
    'volume_code': 'VOL. 04',
    'reading_time': '19 MIN READ',
    'word_count': '4,350 WORDS',
    'scite': {
        'doi': '10.1080/00207179.2014.900705',
        'fetched_on': '2026-11-25',
        'citing_publications': 87,
        'supporting': 0,
        'mentioning': 52,
        'contrasting': 0,
        'retracted': False,
        'summary': (
            'Scite Smart Citation Index [observed: Scite ML citation classification, accessed '
            '2026-11-25]: 0 retractions; 87 citing publications (0 supporting, 52 mentioning, '
            '0 contrasting citation statements) for Limebeer, Perantoni & Rao (2014, DOI '
            '10.1080/00207179.2014.900705). Counts describe that paper, not this folio.'
        ),
    },
}

LONGFORM_DATA = {
    'reading_time': '19 MIN READ',
    'word_count': '4,350 WORDS',
    'scite': FOLIO['scite'],
    'act1_title': (
        "Act I — From Lev Pontryagin's Maximum Principle to Hybrid Race-Car Pacing "
        '& Neural PDE Operators'
    ),
    'act1_dropcap': (
        'Lev Pontryagin, Vladimir Boltyanskii, Revaz Gamkrelidze, and Evgenii Mishchenko studied '
        'how to steer a machine when control levers hit stops. Classical calculus of variations, '
        'developed from Leonhard Euler and Joseph-Louis Lagrange onward, looks for smooth interior '
        'variations where small nudges stay open. Real machines hit limits. Valves reach mechanical '
        'stops, traction motors reach power ceilings, and battery packs hold finite stored energy. '
        'In their 1962 book The Mathematical Theory of Optimal Processes, Pontryagin and his '
        'coauthors paired each state variable with an adjoint co-state. In plain terms, that '
        'co-state acts like an exchange rate on stored energy across a trip. It weighs immediate '
        'thrust against charge needed later, deciding where full power gives way to restraint or '
        'braking. This page is an explanation, not a vehicle design method, and none of its '
        'numbers belong on a real car.'
    ),
    'act1_plain_bridge': (
        'Picture driving a hybrid car fifty miles across a flat desert highway on one small '
        'battery pack. No charging stations sit along the route. Flooring the pedal at the start '
        'feels brisk, yet the battery empties halfway down the road. Once that charge vanishes, '
        'the car slows while steadier drivers hold pace and pass. Optimal control asks a direct '
        'question: how might finite energy be spent to finish in least time? Rather than guessing '
        'by reflex, a mathematical model assigns each stored watt-hour a time value. At high '
        'speed, air drag pushes back hard and extra electric boost buys very little acceleration. '
        'Easing off boost early on a long straight saves charge for slower corner exits, and '
        'braking into turns recovers energy. Nothing here is a powertrain or controller design '
        'method, and none of these illustrative numbers belong on a vehicle or battery.'
    ),
    'act1_body': (
        'Perantoni and Limebeer (2014, DOI 10.1080/00423114.2014.889315) solved minimum-lap-time '
        'Formula One control by direct transcription on a curvilinear track. Limebeer, Perantoni, '
        'and Rao (2014, DOI 10.1080/00207179.2014.900705) applied orthogonal collocation to '
        'kinetic and hybrid thermal energy recovery systems. Salazar et al. (2017, DOI '
        '10.1109/TCST.2016.2642830) derived an analytical minimum-lap-time power-split policy, and '
        'Duhr et al. (2021, DOI 10.1016/j.apenergy.2020.115980) combined a convex powertrain and '
        "gearbox model with convex optimization, dynamic programming, and Pontryagin's minimum "
        'principle. The slider spans 120 to 350 kilowatts (350 kilowatts reported for 2026, FIA '
        'text unverified here) on an assumed 4.0 megajoule budget. Pairing Fourier Neural '
        'Operators (Li et al. 2020, arXiv:2010.08895, DOI 10.48550/arXiv.2010.08895) with hybrid '
        'control is untested.'
    ),
    'act1_stakes': (
        'Optimal control and fluid mechanics sit across a wide computational gap. Richard Bellman '
        'gave an expository address on dynamic programming in 1954 (DOI '
        '10.1090/S0002-9904-1954-09848-8). Crandall and Lions (1983, DOI '
        '10.1090/S0002-9947-1983-0690039-8) formulated uniqueness, stability, and existence '
        'theorems for viscosity solutions of Hamilton–Jacobi equations. Point-mass equations solve '
        'fast, whereas three-dimensional Navier–Stokes simulations remain costly online; whether '
        'operator surrogates could supply aerodynamic gradients inside trajectory solvers is not '
        'yet tested.'
    ),
    'pullquote': (
        '"In the model, a constant interior co-state lambda_E* prices stored battery energy across '
        'the lap, trading straight-end boost against low-speed exit thrust."'
    ),
    'chronology': [
        (
            '1954',
            'Richard Bellman delivers an expository address on dynamic programming (DOI '
            '10.1090/S0002-9904-1954-09848-8).',
        ),
        (
            '1962–1983',
            'Pontryagin et al. publish the bounded-control maximum principle (1962); Crandall & '
            'Lions introduce Hamilton–Jacobi viscosity solutions (1983, DOI '
            '10.1090/S0002-9947-1983-0690039-8).',
        ),
        (
            '2014–2021',
            'Limebeer, Perantoni & Rao model F1 recovery (DOI 10.1080/00207179.2014.900705); '
            'Salazar et al. derive power-split policies (DOI 10.1109/TCST.2016.2642830); Duhr et '
            'al. combine convex models, DP, and PMP (DOI 10.1016/j.apenergy.2020.115980).',
        ),
        (
            '2020–2023',
            'Li et al. introduce Fourier Neural Operators (arXiv:2010.08895), Lu et al. introduce '
            'DeepONet (DOI 10.1038/s42256-021-00302-5), and Kovachki et al. analyze '
            'function-space neural operators (2023).',
        ),
    ],
    'act2_title': (
        'Act II — How the Model Is Written: Pontryagin Co-State Switching + Fourier Neural '
        'Operator Spectral Convolutions'
    ),
    'act2_intuition': (
        'The display pairs two separate formulations—a distance-domain Pontryagin minimum '
        'Hamiltonian and a standalone Fourier Neural Operator layer—with an assumed 4.0 MJ budget, '
        'unspecified vehicle parameters (m, rho, A, C_D, F_ice, eta_k, eta_regen, alpha), and fixed '
        'illustrative figures (−0.42 s, 298.4 km/h, 0.82%). Along track arc-length s (ds/dt = v), '
        'H = (1/v) + lambda_v * (F_ice + P_k/v - 0.5*rho*v^2*A*C_D - F_brake)/(m*v) - '
        'lambda_E * P_batt(P_k)/v. Inside (E_min, E_max), d(lambda_E)/ds = 0 keeps lambda_E* < 0 '
        'constant. Motoring arcs (F_brake = 0, P_k >= 0) carry lambda_v < 0; a coasting deadband '
        'P_k* = 0 holds when lambda_E* / eta_k <= lambda_v / (m * v) <= lambda_E* * eta_regen, '
        'lift-and-coast regen (F_brake = 0, P_k < 0) enters on lambda_E* * eta_regen < '
        'lambda_v / (m * v) < 0, and corner friction braking (F_brake > 0, P_k < 0, '
        'P_batt = eta_regen * P_k) requires lambda_v > 0. For P_k >= 0, affine draw P_k/eta_k '
        'switches at lambda_v/(m*v) = lambda_E*/eta_k, whereas assumed quadratic losses '
        'P_k/eta_k + alpha*P_k^2 (alpha > 0, folio algebra) could taper '
        'P_k*(s) = (lambda_v / (lambda_E* * m * v) - 1/eta_k) / (2α) on (v_switch, v_zero) '
        'between v_switch = lambda_v / (lambda_E* * m * (1/eta_k + 2α P_{k,max})) and '
        'v_zero = lambda_v * eta_k / (lambda_E* * m).'
    ),
    'act2_deepening': (
        'Point-mass formulations evaluate drag from precomputed aero maps. Truncating a Fourier '
        'Neural Operator at k_max modes parameterizes kernels in Fourier space (Li et al. 2020). '
        'Duhr et al. (2021, DOI 10.1016/j.apenergy.2020.115980) combined a convex powertrain and '
        "gearbox model with convex optimization, dynamic programming, and Pontryagin's minimum "
        'principle. Because thrust per kilowatt falls as 1/v while drag grows as v^2, strictly '
        'convex losses taper 350 kW boost on (v_switch, v_zero) before depletion.'
    ),
    'act2_analogy': (
        'A trail runner carrying one twenty-ounce water flask across mountain ridges faces a '
        'related pacing trade-off. Drinking greedily on the flat valley floor empties the flask '
        'before the steep climb, leaving the runner dehydrated below the ridge. Hoarding water too '
        'cautiously leaves unused ounces at the finish. An optimal shadow price weighs time saved '
        'per sip on steep grades. Where the analogy stops: a runner cannot refill a flask on '
        'descents, whereas regenerative braking recharges the battery entering corners.'
    ),
    'act2_plain_primer': (
        'Two sliders sit below. Before any acronym, an MGU-K is a kinetic motor-generator unit on '
        'the drivetrain. MGU-K Peak Electric Power updates the power label from 120.0 to 350.0 '
        'kilowatts, and Fourier Spectral Modes updates the wavenumber label from eight to '
        'sixty-four modes while driving the generic stage overlay and 3D view. Neither slider runs '
        'a trajectory or flow solver; both schematic curves and the four readout cards stay fixed '
        'illustrative items.'
    ),
    'distill_diagram': {
        'analogy_title': "The Trail Runner's Water Flask",
        'analogy_sub': 'Pacing finite stored reserves across flat ground and steep climbs',
        'force_a_title': 'Peak Electric Power P_k',
        'force_a_sub': 'Raises launch thrust while drawing down finite battery energy',
        'force_b_title': 'Fourier Spectral Modes k_max',
        'force_b_sub': 'Sets wavenumber cutoff in the proposed operator surrogate',
        'threshold_title': 'Switching Velocity Taper vs. Clipping',
        'threshold_pass': 'Model: convex-loss taper (−0.42 s fixed illustrative figure)',
        'threshold_fail': 'Model: early boost depletion clips power mid-straight (illustrative)',
    },
    'walkthrough': [
        (
            'Experiment 1 (MGU-K Peak Electric Power): Drag P_k between 120 kW and 350 kW to '
            'update the power label and schematic caption beside the fixed curves.'
        ),
        (
            'Experiment 2 (Fourier Spectral Modes): Adjust k_max from 8 to 64 modes to update the '
            'mode label; the 0.82% card stays a fixed k_max = 32 illustrative figure.'
        ),
        (
            'Experiment 3 (Four-Stage Stepper): Step through Stages 1 to 4 to inspect the '
            'proposed FNO layer, distance Hamiltonian H, convex-loss taper, and braking harvest.'
        ),
    ],
    'act4_title': 'Act IV — Applied Mathematics, Operator Learning & Open Questions',
    'act4_human_ai': (
        'Neural operators parameterize PDE integral kernels in Fourier space (Li et al. 2020, '
        'arXiv:2010.08895) or learn nonlinear operators via DeepONet based on the universal '
        'approximation theorem of operators (Lu et al. 2021, DOI 10.1038/s42256-021-00302-5). '
        'Such models map between infinite-dimensional function spaces (Kovachki et al. 2023); '
        'using them inside Pontryagin or HJB solvers remains untested here.'
    ),
    'act4_deepening': (
        'Pairing function-space neural operators (Kovachki et al. 2023) with Hamilton–Jacobi '
        'viscosity theory (Crandall & Lions 1983) highlights a strict boundary: policies optimized '
        'against a surrogate inherit its errors, so engineers must enforce state, thermal, and '
        'actuator limits—and nothing here is a controller design method. Open questions include '
        'spectral out-of-distribution indicators and surrogate gradient Lipschitz bounds.'
    ),
    'cf_bridge': (
        'Standalone Applied Mathematics & AI Monograph: Written as an educational explanation, '
        'not a vehicle or clinical design method, and offering no engineering or medical advice.'
    ),
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
        '            <path data-custom-curve="1" d="M 55 155 L 115 45 L 235 45 L 245 142 L 355 '
        '142" fill="none" stroke="var(--tp-minium)" stroke-width="2.2" '
        'stroke-dasharray="4,3"/>\n'
        '            <path id="tp-m07-pmp-curve" data-custom-curve="1" d="M 55 155 Q 135 38 225 44 '
        'Q 285 52 335 72 L 355 170" fill="none" stroke="var(--tp-verdigris)" stroke-width="3"/>\n'
        '            <circle id="tp-m07-switch-dot" cx="245" cy="48" r="5.5" '
        'fill="var(--tp-prussian)"/>\n'
        '            <text x="55" y="24" font-size="11" font-weight="600" '
        'fill="currentColor">Illustrative 350 kW MGU-K Boost &amp; Taper Schematic</text>\n'
        '            <text id="tp-m07-pk-text" x="62" y="64" font-size="10" '
        'fill="var(--tp-verdigris)">PMP Co-State Taper (P_k = 350.0 kW → Convex-Loss Arc)</text>\n'
        '            <text x="165" y="134" font-size="9.5" fill="var(--tp-minium)">Naive Early '
        'Clipping (+0.42 s slower, illustrative)</text>\n'
        '            <text x="55" y="200" font-size="10" fill="currentColor">Illustrative Straight '
        'Arc-Length s · Interior Co-State λ_E* Constant</text>\n'
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

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining a Pontryagin phase portrait and 3D Fourier Neural '
        'Operator lattice for a 350 kW hybrid teaching model (artistic impression, not a plot)'
    ),
    'caption': (
        'Conceptual Vision Plate M.07-V (Imagining What It Would Look Like) · Artistic '
        'visualization imagining a Fourier Neural Operator lattice paired conceptually with a '
        'Pontryagin 350 kW MGU-K teaching trajectory.'
    ),
}

DISPATCH = {
    'kicker': (
        'FRONTIER OPTIMAL CONTROL & AI DISPATCH · HYBRID PONTRYAGIN CONTROL & FOURIER NEURAL '
        'OPERATORS'
    ),
    'headline': (
        'Pontryagin Energy Control & Proposed Neural Surrogates for a 350 kW Hybrid Teaching Model'
    ),
    'body': (
        "Pairs Limebeer, Perantoni & Rao's optimal control of Formula One energy recovery (DOI "
        "10.1080/00207179.2014.900705) with Li et al.'s Fourier Neural Operator (arXiv:2010.08895) "
        'as a teaching explanation under the reported 2026 350 kW ceiling—not a vehicle design '
        'method, with illustrative figures.'
    ),
}

META_3D = (
    'Formula 1 350 kW Pontryagin & FNO Teaching Manifold',
    'X: Track Lap Distance s · Z: Battery Co-State λ_E · Y: Illustrative Power P_k*(s)',
)

ES_TRANSLATION = {
    'title_es': (
        'Control Óptimo de Energía de Pontryagin para MGU-K de 350 kW en Fórmula 1, '
        'Minimización de Tiempo de Vuelta HJB y Operadores Neuronales de Fourier'
    ),
    'subtitle_es': (
        'Una explicación matemática, no un método de diseño vehicular: cómo el Principio del '
        'Máximo de Pontryagin modela el reparto del impulso híbrido (hasta el techo de 350 kW '
        'reportado para 2026) con batería finita, con Operadores Neuronales de Fourier '
        'propuestos. Todas las cifras son ilustrativas; ninguna aplica a un vehículo, batería o '
        'controlador real.'
    ),
    'why_es': (
        'Un corredor de sendero con una cantimplora dosifica cada sorbo según el tiempo ahorrado '
        'en subida; el co-estado λ_E* cumple ese papel en el modelo, aunque el frenado '
        'regenerativo recarga la batería.'
    ),
    'plain_es': (
        'Imaginen manejar un auto híbrido ochenta kilómetros por una carretera plana del desierto '
        'con una batería pequeña. No hay estaciones de carga en la ruta. Pisar el acelerador a '
        'fondo al salir vacía la batería a mitad del camino. Agotada esa carga, el auto pierde '
        'ritmo frente a conductores constantes. El control óptimo pregunta cómo repartir energía '
        'finita para llegar en el menor tiempo. En vez de decidir por reflejo, el modelo '
        'matemático asigna un valor temporal a cada watt-hora. A alta velocidad el arrastre del '
        'aire crece y el impulso extra compra poca aceleración. Moderar el apoyo eléctrico en '
        'recta conserva carga para curvas lentas, y frenar recupera energía. Esta página es una '
        'explicación, no un método de diseño vehicular, y ninguna cifra aplica a un vehículo, '
        'batería o controlador real.'
    ),
    'deep_es': (
        'Esta exposición combina dos formulaciones distintas—un hamiltoniano mínimo de Pontryagin '
        'en ds/dt = v y una capa independiente de Operador Neuronal de Fourier—con 4.0 MJ '
        'supuestos, parámetros vehiculares no fijados y cifras ilustrativas fijas (−0.42 s, '
        '298.4 km/h, 0.82%); no es un método de diseño vehicular. En (E_min, E_max), λ_E* < 0 '
        'queda constante: la tracción usa λ_v < 0, una banda de planeo P_k* = 0 rige cuando '
        'λ_E* / η_k ≤ λ_v / (m · v) ≤ λ_E* · η_regen, el frenado en curva exige λ_v > 0, y '
        'pérdidas cuadráticas supuestas P_k/η_k + α P_k² atenúan P_k*(s) en (v_switch, v_zero). '
        'Perantoni y Limebeer (2014, DOI 10.1080/00423114.2014.889315) usaron transcripción '
        'directa, Limebeer, Perantoni y Rao (2014, DOI 10.1080/00207179.2014.900705) colocación '
        'ortogonal, Salazar et al. (2017, DOI 10.1109/TCST.2016.2642830) reparto analítico, y '
        'Duhr et al. (2021, DOI 10.1016/j.apenergy.2020.115980) modelos convexos con DP y '
        'Pontryagin; Bellman (1954, DOI 10.1090/S0002-9904-1954-09848-8) y Crandall y Lions '
        '(1983, DOI 10.1090/S0002-9947-1983-0690039-8) fundamentan HJB, y acoplar FNO (Li et al. '
        '2020), DeepONet (Lu et al. 2021) u operadores (Kovachki et al. 2023) sigue sin probarse.'
    ),
    'bridge_es': (
        'Monografía educativa independiente, no un método de diseño vehicular ni clínico, sin '
        'asesoramiento médico ni de ingeniería.'
    ),
}
