#!/usr/bin/env python3
"""Folio E.15 (ENGINEERING): Quasi-Brittle Concrete Fracture, Bažant Size Effect Law & Hillerborg Process-Zone Scaling."""
from __future__ import annotations

SLUG = 'e15'

PILLAR = 'engineering'

_SCITE = {
    'doi': '10.1061/(ASCE)0733-9399(1984)110:4(518)',
    'fetched_on': '2026-11-21',
    'citing_publications': 1772,
    'supporting': 35,
    'mentioning': 707,
    'contrasting': 1,
    'retracted': False,
    'summary': (
        'Scite Smart Citation Index entry for Bažant 1984, "Size Effect in Blunt Fracture: Concrete, Rock, Metal" '
        '(Journal of Engineering Mechanics, DOI 10.1061/(ASCE)0733-9399(1984)110:4(518)), fetched 2026-11-21: '
        '1,772 citing records (35 supporting, 707 mentioning, 1 contrasting) and no retraction notice. '
        'These counts describe that foundational paper, not this folio.'
    ),
}

FOLIO = {
    'folio_id': 'E.15',
    'slug': 'e15',
    'pillar': 'engineering',
    'category_code': 'E',
    'parent_folios': ['E.02', 'E.09', 'E.11'],
    'lineage_mode': 'CONTINUATION · Continues E.02 Concrete Rheology, E.09 Self-Healing & E.11 Compliance',
    'title': 'Quasi-Brittle Concrete Fracture, Bažant Size Effect Law & Hillerborg Process-Zone Scaling',
    'subtitle': (
        "Continuing Folio E.02's concrete placement, E.09's crack healing, and E.11's continuum stiffness: an "
        'illustrative fracture-mechanics study coupling Hillerborg\'s fictitious crack model, Bažant\'s Type II '
        'Size Effect Law, and Bažant–Kazemi regression for initial fracture energy and process-zone length across '
        'laboratory beams and deep concrete girders.'
    ),
    'date_published': '2026-11-21',
    'date_redated': '2026-11-21',
    'current_edition': 'REV 1.0',
    'status_badge': 'FRACTURE MECHANICS · REV 1.0',
    'primary_kernel': 'skills/engineering/e15/verify_e15_bazant_size_effect.py',
    'governing_law': "σ_N(D) = B f'_t / √(1 + D / D_0) · β_B = D / D_0 · G_f = (B f'_t)² D_0 g(α_0) / E' · c_f = D_0 g(α_0) / g'(α_0)",
    'colophon': {
        'identifier': 'E.15 · Bažant Size Effect & Concrete Fracture · REV 1.0',
        'kernels': 'Griffith LEFM (1921) · Hillerborg Fictitious Crack (1976) · Bažant Size Effect Law (1984, 1990)',
        'benchmarks': (
            'Model values (notched beam D = 400.0 mm, D_0 = 220.0 mm): β_B = 1.818 · σ_N = 2.502 MPa (59.6% of B f\'_t) · '
            's = −0.323 · G_f = 127.84 N/m · c_f = 64.84 mm (drops to σ_N = 1.322 MPa at D = 2000 mm)'
        ),
        'bridge': 'Continues E.02/E.09/E.11',
    },
    'sliders': [
        {
            'label': 'Structural Depth (D)',
            'min': 50.0,
            'max': 2400.0,
            'step': 50.0,
            'value': 400.0,
            'unit': ' mm',
        },
        {
            'label': 'Transitional Size (D_0)',
            'min': 80.0,
            'max': 500.0,
            'step': 10.0,
            'value': 220.0,
            'unit': ' mm',
        },
    ],
    'steps': [
        (
            'Stage 1 (From Griffith LEFM to Hillerborg\'s Fictitious Crack Zone): Griffith (1921, DOI '
            '10.1098/rsta.1921.0006) showed that a sharp crack in a brittle solid grows when stored elastic energy release '
            'matches surface energy, scaling nominal strength as D^(−1/2). Concrete is not ideally brittle: ahead of a '
            'visible notch, microcracking and aggregate bridging form a finite Fracture Process Zone (FPZ). Hillerborg, '
            'Modéer, and Petersson (1976, DOI 10.1016/0008-8846(76)90007-7) modeled this softening zone via tensile '
            'strength f\'_t, initial fracture energy G_f, and characteristic length l_ch = E\' G_f / (f\'_t)^2 (424.5 mm '
            'at E\' = 34.0 GPa, f\'_t = 3.20 MPa, G_f = 127.84 N/m).'
        ),
        (
            'Stage 2 (Bažant Type II Size Effect Law & Brittleness Number β_B): For geometrically similar notched '
            'members (notch ratio α_0 = a_0 / D > 0), Bažant (1984, DOI 10.1061/(ASCE)0733-9399(1984)110:4(518)) matched '
            'plastic yield at small D against LEFM at large D via σ_N(D) = B f\'_t / √(1 + β_B), with brittleness number '
            'β_B = D / D_0. Using illustrative calibration B f\'_t = 4.20 MPa and D_0 = 220.0 mm, a 100 mm laboratory beam '
            'reaches σ_N = 3.482 MPa (82.9% of B f\'_t, β_B = 0.455), while a 400 mm beam drops to 2.502 MPa (59.6%, '
            'β_B = 1.818) and log–log slope s = −β_B / [2(1 + β_B)] steepens from −0.156 to −0.323.'
        ),
        (
            'Stage 3 (Bažant–Kazemi Regression for G_f and Process-Zone Length c_f): Bažant and Kazemi (1990, DOI '
            '10.1007/BF00047063) inverted the size-effect curve into a linear relation Y = 1 / σ_N^2 = C D + A, where '
            'G_f = (B f\'_t)^2 D_0 g(α_0) / E\' and effective FPZ length c_f = D_0 g(α_0) / g\'(α_0). With LEFM geometry '
            'factors g(α_0) = 1.12 and g\'(α_0) = 3.80 at D_0 = 220.0 mm, the model yields G_f = 127.84 N/m and c_f = '
            '64.84 mm. Doubling D_0 to 440.0 mm (a tougher aggregate mix at fixed B f\'_t) raises G_f to 255.68 N/m, '
            'c_f to 129.68 mm, and 400 mm beam nominal strength to 3.040 MPa.'
        ),
        (
            'Stage 4 (Open Hypothesis, Tier T1–T2, and Falsification Condition): Hypothesis (Tier T1–T2): in '
            'geometrically similar notched concrete beams without distributed shear reinforcement, nominal failure stress '
            'declines along σ_N = B f\'_t (1 + D / D_0)^(−1/2) toward Griffith D^(−1/2) scaling as structural depth '
            'grows; at D = 2000 mm (D_0 = 220 mm, β_B = 9.091), modeled σ_N falls to 1.322 MPa (31.5%, slope −0.450), '
            'whereas ignoring (1 + D / D_0) overpredicts capacity by 3.177× at 4.20 MPa. This Type II hypothesis is '
            'falsified in unnotched Type I beams governed by Weibull boundary-layer strength (Bažant & Yu 2009, DOI '
            '10.1061/(ASCE)0733-9399(2009)135:2(78)), in heavily stirrup-confined or steel-fiber members that arrest '
            'localization, or where aggregate size d_a is comparable to D.'
        ),
    ],
    'readouts': [
        {'label': 'Brittleness & Fracture Energy', 'value': 'β_B = 1.818 · G_f = 127.84 N/m (model)'},
        {'label': 'Nominal Strength & Retention', 'value': "σ_N = 2.502 MPa (59.6% of B f'_t, model)"},
        {'label': 'Log–Log Slope & FPZ Length', 'value': 's = −0.323 · c_f = 64.84 mm (model)'},
        {'label': 'Size-Effect Fracture Regime', 'value': 'QUASI-BRITTLE TRANSITION (0.15 < β_B <= 10, model)'},
    ],
    'spec_plate': {
        'division': 'CONCRETE FRACTURE / CSI 03 30 00 (FILING LABEL · DESIGN STUDY)',
        'title': 'Bažant Type II Notched Concrete Fracture & Brittleness Scaling Screening Envelope',
        'body': (
            'Illustrative closed-form fracture-scaling study, not a structural code check (ACI 318 / fib Model Code) or '
            'member design: tracks Type II geometrically similar notched specimens (notch ratio α_0 > 0, LEFM shape '
            'factors g(α_0) = 1.12 and g\'(α_0) = 3.80, E\' = 34.0 GPa, B f\'_t = 4.20 MPa, f\'_t = 3.20 MPa). '
            'Holding B f\'_t, E\', g(α_0), and g\'(α_0) constant while sweeping transitional size D_0 scales initial '
            'fracture energy G_f, process-zone length c_f, and Hillerborg l_ch linearly with D_0, comparing tougher '
            'versus more brittle mixes at constant small-scale plastic strength. Unnotched Type I members, stirrup '
            'reinforcement, and full-scale testing fall outside this reduced 2-slider curve.'
        ),
        'meta': (
            'Primary anchors: Griffith 1921 (DOI 10.1098/rsta.1921.0006) · '
            'Hillerborg et al. 1976 (DOI 10.1016/0008-8846(76)90007-7) · '
            'Bažant 1984 (DOI 10.1061/(ASCE)0733-9399(1984)110:4(518)) · '
            'Bažant & Kazemi 1990 (DOI 10.1007/BF00047063) · Model values, not laboratory test data'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE E.15-A · INITIAL FRACTURE ENERGY G_f VS. TOTAL WORK OF FRACTURE G_F',
        'body': (
            'Bažant and Kazemi (1990, DOI 10.1007/BF00047063) distinguish the initial fracture energy G_f—governed by '
            'the steep initial tangent of the cohesive softening curve and extracted from size-effect peak loads—from the '
            'larger total work of fracture G_F integrated under the entire softening tail. Peak-load structural size '
            'effect depends primarily on G_f and effective process-zone length c_f, whereas post-peak tail energy G_F '
            'governs late crack opening.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE E.15-B · TYPE II NOTCHED BOUNDARIES & CONSTANT-B f\'_t PARAMETERIZATION',
        'body': (
            'This reduced 2-slider sweep holds B f\'_t = 4.20 MPa, E\' = 34.0 GPa, f\'_t = 3.20 MPa, g(α_0) = 1.12, and '
            'g\'(α_0) = 3.80 constant across D_0 ∈ [80, 500] mm, so G_f = (B f\'_t)^2 D_0 g(α_0) / E\', c_f, and l_ch '
            'all scale linearly with D_0 (comparing tougher versus more brittle mixes). The curve applies to notched '
            'Type II members (α_0 > 0); unnotched Type I beams retain a finite large-size asymptotic stress under '
            'Universal Size Effect Law (Bažant & Yu 2009, DOI 10.1061/(ASCE)0733-9399(2009)135:2(78)).'
        ),
    },
    'skill': {
        'filename': 'bazant-size-effect-SKILL.md',
        'name': 'bazant-size-effect',
        'description': (
            'AI-agnostic civil structural fracture skill for Bazant Type II Size Effect Law, Hillerborg fictitious crack '
            'length l_ch, and Bazant-Kazemi extraction of fracture energy G_f and process-zone length c_f.'
        ),
        'rules': [
            (
                'Enforce strictly positive finite parameters D, D_0, B*f_t, E\', f_t, g(alpha_0), and g\'(alpha_0) inside '
                'geometrically similar notched Type II members (alpha_0 = a_0 / D > 0).'
            ),
            (
                'Compute nominal strength via Bazant Type II Size Effect Law sigma_N = B*f_t / sqrt(1 + D/D_0) with '
                'brittleness number beta_B = D / D_0 and log-log slope s = -beta_B / (2*(1 + beta_B)), avoiding '
                'scale-invariant plastic extrapolation.'
            ),
            (
                'Check unit identity (MPa^2 * mm / GPa = N/m) when evaluating initial Mode I fracture energy '
                'G_f = (B*f_t)^2 * D_0 * g(alpha_0) / E\', effective FPZ length c_f = D_0 * g(alpha_0) / g\'(alpha_0), '
                'and Hillerborg characteristic length l_ch = E\' * G_f / f_t^2 (mm).'
            ),
            (
                'Frame Type II size-effect scaling as a Tier T1-T2 structural screening hypothesis that stops at '
                'unnotched Type I beams, stirrup-confined or fiber-reinforced shear members, and code design checks.'
            ),
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.0',
            'date': '2026-11-21',
            'summary': (
                'REV 1.0 (Published 2026-11-21): Volume VII Civil & Structural Engineering monograph continuing Folios '
                'E.02, E.09 & E.11 via Griffith energy balance (1921), Hillerborg fictitious crack softening (1976), '
                'Bažant Type II Size Effect Law (1984), Bažant–Kazemi G_f/c_f regression (1990), Universal Size Effect '
                'Law (2009), and dam-concrete mesoscale fracture experiments (2024).'
            ),
            'opus': (
                'Verification note: all six primary DOIs in this folio were checked against Crossref and Scite on '
                '2026-11-21 with zero retraction notices; all numerical outputs are recomputed offline by '
                'skills/engineering/e15/verify_e15_bazant_size_effect.py and represent illustrative closed-form '
                'fracture-scaling model values rather than laboratory test data.'
            ),
        }
    ],
    'volume': 7,
    'volume_code': 'VOL. 07',
    'reading_time': '22 MIN READ',
    'word_count': '4,700 WORDS',
    'scite': dict(_SCITE),
}

LONGFORM_DATA = {
    'reading_time': '22 MIN READ',
    'word_count': '4,700 WORDS',
    'parent_folios': ['E.02', 'E.09', 'E.11'],
    'lineage_mode': 'CONTINUATION · Continues E.02 Concrete Rheology, E.09 Self-Healing & E.11 Compliance',
    'scite': dict(_SCITE),
    'act1_title': 'Act I — Cool Fact & Human Story: Why Small Concrete Beams Test Stronger Than Deep Bridge Girders',
    'act1_dropcap': (
        'In 1976, Swedish structural engineer Arne Hillerborg stood before a puzzling gap in how concrete breaks. '
        'A small notched concrete beam cast for a university laboratory bench routinely carried higher nominal stress '
        'than a geometrically identical beam poured ten times deeper for a bridge pier or dam spillway. Classical '
        'plastic strength rules treated material strength as a fixed number independent of member height, while '
        'classical brittle fracture predicted a steep drop in strength as beam depth grew. Neither picture matched '
        'real concrete structures. Hillerborg and his colleagues Mikael Modéer and Per-Erik Petersson proposed that '
        'concrete ahead of a crack tip does not snap cleanly like window glass. Instead, microcracks and rough stone '
        'aggregates share tensile stress across a finite softening zone before splitting apart. Explaining how that '
        'process zone sets structural brittleness governs safe scaling from laboratory test benches to full civil spans.'
    ),
    'act1_plain_bridge': (
        'In plain words, concrete carries a hidden cushion ahead of a growing crack. Before a notch opens all the '
        'way, rough stones and tiny microcracks bridge the gap and hold part of the load. In a small bench beam, '
        'that bridged zone spans most of the height. The whole cross section shares the pull and fails near its '
        'plastic strength. In a deep bridge girder or dam wall, the bridged zone stays about the same size while '
        'the girder grows much taller. Now the cushion sits in a thin strip near the notch tip. Elastic energy '
        'concentrates right ahead of the crack. Standard small cylinders miss this drop in resistance. As a result, '
        'a two-meter girder splits at a lower average stress than a small beam from the same batch, even with '
        'matching notch proportions.'
    ),
    'act1_body': (
        'In 1984, Zdeněk P. Bažant united those two limits—small-scale plastic strength and large-scale Linear Elastic '
        'Fracture Mechanics (LEFM, introduced by Alan Arnold Griffith in 1921, DOI 10.1098/rsta.1921.0006) in a single '
        'asymptotic matching law known as the Type II Size Effect Law (Journal of Engineering Mechanics, DOI '
        '10.1061/(ASCE)0733-9399(1984)110:4(518)). Bažant scaled nominal failure stress using structural depth D, '
        'transitional size D_0, and small-scale plastic intercept B f\'_t so that small members approach plastic yield '
        'while deep members approach square-root fracture scaling. Six years later, Bažant and Mohammad T. Kazemi '
        '(1990, DOI 10.1007/BF00047063) showed that plotting inverse squared strength against depth turns the curve '
        'into a line whose slope and intercept extract initial Mode I fracture energy G_f and effective fracture '
        'process zone (FPZ) length c_f directly from peak loads of notched beams.'
    ),
    'act1_stakes': (
        'Ignoring size scaling when moving from laboratory specimens to deep civil members introduces substantial '
        'unconservative error in unreinforced or lightly reinforced shear zones. Under our illustrative calibration '
        '(B f\'_t = 4.20 MPa, transitional size D_0 = 220.0 mm, effective modulus E\' = 34.0 GPa, g(α_0) = 1.12, '
        'g\'(α_0) = 3.80), a 100 mm laboratory beam carries σ_N = 3.482 MPa (82.9% of B f\'_t), a 400 mm beam drops to '
        '2.502 MPa (59.6%), and a 2,000 mm full-scale girder falls to 1.322 MPa (31.5% of B f\'_t, brittleness number '
        'β_B = 9.091). Extrapolating the small-scale plastic limit 4.20 MPa directly to D = 2,000 mm overestimates '
        'nominal fracture capacity by a factor of 3.177× in the model.'
    ),
    'pullquote': (
        '"The aggregate-bridged fracture process zone does not grow with the bridge: as structural depth D outpaces '
        'transitional size D_0, nominal strength crosses smoothly from plastic yield toward Griffith D^(−1/2) brittleness."'
    ),
    'chronology': [
        (
            '1921',
            'Alan Arnold Griffith derives the brittle energy-balance fracture criterion in solids, predicting nominal '
            'strength proportional to D^(−1/2) (Phil. Trans. R. Soc. Lond. A, DOI 10.1098/rsta.1921.0006).'
        ),
        (
            '1976',
            'Arne Hillerborg, Mikael Modéer, and Per-Erik Petersson introduce the fictitious crack model with cohesive '
            'softening and characteristic length l_ch = E\' G_f / (f\'_t)^2 (Cement and Concrete Research, DOI '
            '10.1016/0008-8846(76)90007-7).'
        ),
        (
            '1984',
            'Zdeněk P. Bažant derives the Type II Size Effect Law σ_N = B f\'_t / √(1 + D / D_0) by asymptotic matching '
            'of crack-band energy release and plastic limit (Journal of Engineering Mechanics, DOI '
            '10.1061/(ASCE)0733-9399(1984)110:4(518)).'
        ),
        (
            '1990',
            'Bažant and Mohammad T. Kazemi formulate linear regression of 1 / σ_N^2 vs. D to extract initial fracture '
            'energy G_f, FPZ length c_f, and brittleness number β_B (International Journal of Fracture, DOI '
            '10.1007/BF00047063).'
        ),
        (
            '2009',
            'Bažant and Qiang Yu generalize the Universal Size Effect Law across Type II notched and Type I unnotched '
            'quasi-brittle structures (Journal of Engineering Mechanics, DOI 10.1061/(ASCE)0733-9399(2009)135:2(78)).'
        ),
        (
            '2024',
            'Qin, Lin, and Guo combine large-scale dam-concrete fracture tests with mesoscale aggregate simulation to '
            'examine aggregate-size effects on size-effect transition (Theoretical and Applied Fracture Mechanics, DOI '
            '10.1016/j.tafmec.2024.104649).'
        ),
    ],
    'act2_title': 'Act II — Cross-Field Intuition: Perforated Paper, Aggregate Bridges & the Brittleness Number',
    'act2_analogy': (
        'Everyday analogy: Compare tearing a small notched strip of heavy woven cardboard against tearing a wide '
        'poster board made of the same card stock. Along the notch tip, loose paper fibers fray and bridge across a '
        'finger-width zone about 20 mm wide. On a 30 mm narrow strip, that frayed zone spans nearly the whole remaining '
        'ligament, so you feel the strip pull evenly before parting. On a 1,000 mm wide sheet, the same 20 mm frayed '
        'zone sits like a tiny pinprick at the notch tip while elastic tension across the broad sheet concentrates '
        'energy right into that tip, unzipping the sheet at far lower average stress. This analogy stops where '
        'three-dimensional coarse-aggregate interlock and compressive shear friction replace pure tensile fiber tearing.'
    ),
    'act2_plain_primer': (
        'Our interactive fracture laboratory controls two geometric and material scales from the Bažant–Kazemi model. '
        'The first slider is Structural Depth (D, from 50 to 2,400 mm), representing the height of a notched concrete '
        'beam tested in geometric proportion. Dragging D upward moves the specimen rightward along the size-effect '
        'curve, driving brittleness number β_B upward and dropping nominal strength σ_N toward the −1/2 elastic '
        'fracture slope. The second slider is Transitional Size (D_0, from 80 to 500 mm), which reflects how large '
        'the aggregate-bridged fracture process zone is relative to specimen geometry; raising D_0 expands fracture '
        'energy G_f and process-zone length c_f, lifting nominal strength across medium depths.'
    ),
    'distill_diagram': {
        'analogy_title': 'Frayed Process Zone vs. Structural Depth',
        'analogy_sub': 'Fixed process-zone length c_f shrinks relative to girder depth D as structures scale up',
        'force_a_title': 'Structural Depth (D)',
        'force_a_sub': 'Raising D increases elastic energy stored per unit advance, lowering nominal stress σ_N',
        'force_b_title': 'Transitional Size (D_0)',
        'force_b_sub': 'Larger D_0 reflects wider aggregate bridging c_f and higher initial fracture energy G_f',
        'threshold_title': 'Brittleness Transition (β_B = D / D_0)',
        'threshold_pass': 'Quasi-plastic small scale: β_B <= 0.15 keeps σ_N close to plastic intercept B f\'_t',
        'threshold_fail': 'LEFM brittle regime: β_B > 10 approaches D^(−1/2) slope −0.5 (caution on scale-up)',
    },
    'act2_intuition': (
        'In Bažant\'s (1984) energy-release balance, advancing a notch through a quasi-brittle beam releases strain '
        'energy from a band of width proportional to aggregate-controlled FPZ length c_f as well as from the outer '
        'elastic volume proportional to D. Combining both terms yields σ_N(D) = B f\'_t / √(1 + D / D_0), where '
        'brittleness number β_B = D / D_0 measures structural size relative to the material-geometry crossover scale D_0. '
        'Taking the log–log derivative gives local slope s = d ln σ_N / d ln D = −β_B / [2(1 + β_B)], moving smoothly '
        'from 0 in the plastic limit (β_B → 0) to −0.5 in Griffith LEFM (β_B → ∞). Notice the calibration boundary: '
        'holding B f\'_t = 4.20 MPa, E\' = 34.0 GPa, f\'_t = 3.20 MPa, g(α_0) = 1.12, and g\'(α_0) = 3.80 fixed while '
        'varying D_0 scales initial fracture energy G_f = (B f\'_t)^2 D_0 g(α_0) / E\', process-zone length '
        'c_f = D_0 g(α_0) / g\'(α_0), and Hillerborg characteristic length l_ch = E\' G_f / (f\'_t)^2 linearly with D_0.'
    ),
    'act2_deepening': (
        'Bažant and Kazemi (1990) turned this scaling relation into a direct laboratory extraction method. Squaring and '
        'inverting σ_N(D) gives Y = 1 / σ_N^2 = C D + A, where A = 1 / (B f\'_t)^2 and C = 1 / [(B f\'_t)^2 D_0]. '
        'Fitting five notched beams across D ∈ {100, 200, 400, 800, 1600} mm recovers B f\'_t = 4.20 MPa and '
        'D_0 = 220.0 mm directly from regression slope C and intercept A, yielding initial fracture energy '
        'G_f = 127.84 N/m (note unit identity: MPa^2 · mm / GPa = N/m), effective FPZ length c_f = 64.84 mm, and '
        'Hillerborg l_ch = 424.5 mm. By contrast, replacing (1 + D / D_0) with 1 assumes scale-invariant plastic '
        'strength, leaving slope s = 0 and inflating a D = 2,000 mm girder\'s modeled capacity from 1.322 MPa to '
        '4.200 MPa (a 3.177× unconservative defect).'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Lab Beam vs. Full-Scale Girder at D_0 = 220 mm): Hold Transitional Size D_0 = 220 mm and '
            'sweep Structural Depth D from 100 mm up to 2,000 mm. Watch brittleness β_B climb from 0.455 to 9.091 while '
            'nominal strength σ_N falls from 3.482 MPa (82.9% of B f\'_t) through 2.502 MPa at D = 400 mm down to '
            '1.322 MPa (31.5% retention), with log–log slope steepening from −0.156 to −0.450.'
        ),
        (
            'Experiment 2 (Aggregate Toughness & Crossover D_0): Hold Structural Depth D = 400 mm and increase '
            'Transitional Size D_0 from 220 mm to 440 mm. Watch initial fracture energy G_f double from 127.84 N/m to '
            '255.68 N/m and FPZ length c_f double from 64.84 mm to 129.68 mm, lifting modeled strength from 2.502 MPa '
            '(59.6%) to 3.040 MPa (72.4%) as the beam shifts back toward the ductile crossover.'
        ),
        (
            'Experiment 3 (Asymptotic Slope & 4-Lens Observatory): Drag D toward 2,400 mm at D_0 = 80 mm (β_B = 30.0) '
            'to inspect the LEFM brittle asymptote (σ_N = 0.754 MPa, slope s = −0.484 close to −0.500), and explore '
            'the 4-Lens Observatory tabs (3D Surface, Phase Portraits, Kirchhoff Ribbon, Polar Radar).'
        ),
    ],
    'act4_title': 'Act IV — Imagining Humanity\'s Future: Dam Safety, Mesoscale Digital Twins & Falsifiable Scaling',
    'act4_human_ai': (
        'Large concrete dams, deep transfer girders, and nuclear containment shells sit well above the laboratory beam '
        'scale where standard cube and cylinder strengths are measured. Coupling closed-form Type II size-effect scaling '
        'with mesoscale aggregate experiments (Qin, Lin & Guo 2024, DOI 10.1016/j.tafmec.2024.104649) and offline '
        'regression verifiers allows structural engineers to keep size-dependent brittleness transparent alongside '
        'code provisions rather than extrapolating small-specimen stress linearly.'
    ),
    'act4_deepening': (
        'Under the Tier T1–T2 hypothesis stated here, geometrically similar notched concrete members without distributed '
        'shear reinforcement follow σ_N(D) = B f\'_t (1 + D / D_0)^(−1/2), transitioning from plastic yield toward '
        'Griffith D^(−1/2) fracture as β_B = D / D_0 exceeds unity. This Type II hypothesis is explicitly falsified in '
        'unnotched Type I modulus-of-rupture beams where boundary-layer randomness yields a finite large-size asymptote '
        '(Bažant & Yu 2009, DOI 10.1061/(ASCE)0733-9399(2009)135:2(78)), in heavily stirrup-confined or fiber-bridged '
        'beams that prevent single-crack localization, or at miniature sizes D comparable to coarse-aggregate diameter '
        'd_a. Keeping a scale-invariant χ_size = 0 planted defect inside the verifier keeps plastic-extrapolation errors '
        'from passing automated screening.'
    ),
    'cf_bridge': 'Continues E.02/E.09/E.11',
    'sources': [
        (
            'Griffith, A. A. (1921). VI. The phenomena of rupture and flow in solids. Philosophical Transactions of the '
            'Royal Society of London. Series A, 221, 163–198. DOI: 10.1098/rsta.1921.0006.'
        ),
        (
            'Hillerborg, A., Modéer, M., & Petersson, P.-E. (1976). Analysis of crack formation and crack growth in '
            'concrete by means of fracture mechanics and finite elements. Cement and Concrete Research, 6(6), 773–781. '
            'DOI: 10.1016/0008-8846(76)90007-7.'
        ),
        (
            'Bažant, Z. P. (1984). Size Effect in Blunt Fracture: Concrete, Rock, Metal. Journal of Engineering '
            'Mechanics, 110(4), 518–535. DOI: 10.1061/(ASCE)0733-9399(1984)110:4(518).'
        ),
        (
            'Bažant, Z. P., & Kazemi, M. T. (1990). Determination of fracture energy, process zone length and '
            'brittleness number from size effect, with application to rock and concrete. International Journal of '
            'Fracture, 44(2), 111–131. DOI: 10.1007/BF00047063.'
        ),
        (
            'Bažant, Z. P., & Yu, Q. (2009). Universal Size Effect Law and Effect of Crack Depth on Quasi-Brittle '
            'Structure Strength. Journal of Engineering Mechanics, 135(2), 78–84. '
            'DOI: 10.1061/(ASCE)0733-9399(2009)135:2(78).'
        ),
        (
            'Qin, J., Lin, C., & Guo, J. (2024). Syncretic investigation on size effect in fracture behavior of dam '
            'concrete with physical experiment and mesoscale simulation. Theoretical and Applied Fracture Mechanics, '
            '133, 104649. DOI: 10.1016/j.tafmec.2024.104649.'
        ),
        (
            'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and '
            'classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
            '882–898. DOI: 10.1162/qss_a_00146.'
        ),
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Bazant Type II Size Effect Law log-log curve '
        'from plastic limit to Griffith LEFM asymptote with small lab beam and full-scale girder benchmarks">\n'
        '            <line x1="48" y1="184" x2="352" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <line x1="48" y1="30" x2="48" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <text x="54" y="22" font-size="10.5" font-weight="600" fill="currentColor">Log–Log Strength σ_N vs. Depth D / D_0</text>\n'
        '            <line x1="52" y1="52.4" x2="210" y2="52.4" stroke="var(--tp-minium)" stroke-width="1.4" stroke-dasharray="4,3"/>\n'
        '            <line id="tp-e15-lefm-line" x1="165.3" y1="52.4" x2="348" y2="128.3" stroke="var(--tp-slate)" stroke-width="1.4" stroke-dasharray="4,3"/>\n'
        '            <path id="tp-e15-sel-curve" data-custom-curve="1" d="M 52 57.5 L 110 64.5 L 165.3 71.7 L 211.0 85.0 L 280 107.0 L 348 130.8" fill="none" stroke="var(--tp-prussian)" stroke-width="2.5"/>\n'
        '            <circle id="tp-svg-eng-point" cx="211" cy="85" r="6" fill="var(--tp-verdigris)"/>\n'
        '            <text x="56" y="42" font-size="9" fill="var(--tp-minium)">Plastic limit B f\'_t = 4.20 MPa</text>\n'
        '            <text x="234" y="150" font-size="9" fill="var(--tp-prussian)">LEFM slope −1/2</text>\n'
        '            <line x1="372" y1="24" x2="372" y2="192" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="386" y="22" font-size="10.5" font-weight="600" fill="currentColor">Scale Benchmarks (D_0 = 220 mm)</text>\n'
        '            <rect x="386" y="38" width="256" height="62" rx="6" fill="var(--tp-stone)" fill-opacity="0.28" stroke="var(--tp-prussian)" stroke-width="1.6"/>\n'
        '            <text x="398" y="59" font-size="9.5" font-weight="600" fill="var(--tp-prussian)">D = 100 mm lab → σ_N = 3.482 MPa</text>\n'
        '            <text x="398" y="81" font-size="9" fill="var(--tp-verdigris)">D = 400 mm → 2.502 MPa (β_B = 1.818)</text>\n'
        '            <rect x="386" y="112" width="256" height="58" rx="6" fill="var(--tp-verdigris)" fill-opacity="0.12" stroke="var(--tp-verdigris)" stroke-width="1.4"/>\n'
        '            <text x="398" y="134" font-size="9.5" font-weight="600" fill="var(--tp-prussian)">D = 2000 mm → 1.322 MPa (31.5%)</text>\n'
        '            <text x="398" y="154" font-size="9" fill="var(--tp-minium)">Defect: plastic 4.20 MPa (3.177× high)</text>\n'
        '            <text x="48" y="206" font-size="10" fill="var(--tp-verdigris)">Bažant Type II SEL model · Recomputed by verify_e15_bazant_size_effect.py</text>\n'
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining what three geometrically similar notched concrete three-point bending '
        'beams at small laboratory, medium, and deep girder scales on steel cylindrical rollers under an overhead '
        'brass-and-steel hydraulic actuator with aggregate-bridged notch-tip microcracking would look like (artistic '
        'impression, not a measured test specimen)'
    ),
    'caption': (
        'Conceptual Vision Plate E.15-V (Imagining What It Would Look Like) · Artistic laboratory view imagining '
        'geometrically similar notched concrete beams across three structural depths. Governing equations and '
        'strength-scaling bounds are kept intact in deterministic Plate E.15-A and the offline verifier below.'
    ),
}

DISPATCH = {
    'kicker': 'FRONTIER STRUCTURAL DISPATCH · QUASI-BRITTLE CONCRETE & SIZE EFFECT',
    'headline': 'Bažant Size Effect Law, Hillerborg Process Zones & Deep Concrete Girder Scaling',
    'body': (
        'Why do small notched concrete test beams sustain higher nominal stress than two-meter bridge girders of the '
        'same batch? Coupling Hillerborg\'s fictitious crack model (1976) with Bažant\'s Type II Size Effect Law '
        '(1984, DOI 10.1061/(ASCE)0733-9399(1984)110:4(518)) tracks the shift from 3.482 MPa at D = 100 mm to '
        '1.322 MPa at D = 2,000 mm (D_0 = 220 mm, G_f = 127.84 N/m).'
    ),
}

META_3D = (
    'Bažant Type II Size Effect & Fracture Energy Surface',
    'X: Structural Depth D (mm) · Z: Transitional Size D_0 (mm) · Y: Nominal Strength Retention σ_N / (B f\'_t)',
)

ES_TRANSLATION = {
    'title_es': 'Fractura Cuasi-Frágil en Concreto, Ley de Efecto de Tamaño de Bažant y Zona de Proceso',
    'subtitle_es': (
        'Continuación de los Folios E.02, E.09 y E.11: estudio ilustrativo de mecánica de fractura que acopla la grieta '
        'ficticia de Hillerborg, la ley de tamaño Tipo II de Bažant σ_N = B f\'_t / √(1 + D / D_0) y la regresión de '
        'Bažant–Kazemi para G_f y c_f.'
    ),
    'why_es': (
        'Igual que una muesca en cartón ancho concentra la tensión en una franja pequeña de fibras sueltas, una viga '
        'profunda de concreto falla a menor esfuerzo nominal que una probeta pequeña del mismo colado.'
    ),
    'plain_es': (
        'En palabras sencillas, el concreto guarda un colchón de resistencia justo delante de la punta de una grieta. '
        'Antes de partirse del todo, piedras ásperas y microfisuras puentean el corte y cargan parte del tirón. En una '
        'viga pequeña de laboratorio, esa zona puenteada abarca casi todo el peralte y la sección trabaja cerca de su '
        'límite plástico. En una trabe profunda de puente o presa, la zona puenteada conserva casi el mismo espesor '
        'físico mientras la pieza crece mucho, concentrando la energía elástica en la muesca.'
    ),
    'deep_es': (
        'En el modelo de Bažant (1984, DOI 10.1061/(ASCE)0733-9399(1984)110:4(518)) y Hillerborg et al. (1976, '
        'DOI 10.1016/0008-8846(76)90007-7), la resistencia nominal de vigas entalladas Tipo II sigue σ_N(D) = '
        'B f\'_t / √(1 + D / D_0) con número de fragilidad β_B = D / D_0 y pendiente s = −β_B / [2(1 + β_B)]. Con la '
        'calibración ilustrativa B f\'_t = 4.20 MPa, D_0 = 220.0 mm, E\' = 34.0 GPa, f\'_t = 3.20 MPa, g(α_0) = 1.12 y '
        'g\'(α_0) = 3.80, una viga de 100 mm alcanza σ_N = 3.482 MPa (82.9%), una de 400 mm baja a 2.502 MPa (59.6%, '
        'β_B = 1.818, s = −0.323) y una trabe de 2,000 mm desciende a 1.322 MPa (31.5%, s = −0.450), frente a 4.20 MPa '
        'con el defecto plástico (3.177× mayor). La regresión de Bažant–Kazemi (1990, DOI 10.1007/BF00047063) recupera '
        'G_f = 127.84 N/m, c_f = 64.84 mm y l_ch = 424.5 mm. Esta hipótesis de nivel T1–T2 se refuta en vigas sin '
        'entalla Tipo I (Bažant y Yu 2009, DOI 10.1061/(ASCE)0733-9399(2009)135:2(78)), elementos con estribos o fibras '
        'densas o piezas donde D se aproxima al tamaño del agregado (Qin et al. 2024, DOI 10.1016/j.tafmec.2024.104649).'
    ),
    'bridge_es': (
        'Escalar con σ_N = B f\'_t / √(1 + D / D_0) separa la respuesta dúctil de laboratorio del comportamiento '
        'cuasi-frágil en trabes profundas (modelo ilustrativo Tipo II, no un cálculo normativo).'
    ),
}
