#!/usr/bin/env python3
"""Folio A.13 (ARCHITECTURE): Heinz Isler's Funicular Thin-Shell Domes: Inverted-Hanging Form-Finding, Zoelly Buckling & Imperfection Knockdowns."""
from __future__ import annotations

SLUG = 'a13'

PILLAR = 'architecture'

FOLIO = {
    'folio_id': 'A.13',
    'slug': 'a13',
    'pillar': 'architecture',
    'category_code': 'A',
    'parent_folios': ['A.01', 'A.11'],
    'lineage_mode': 'CONTINUATION · Continues A.01 Funicular Thrust Surfaces & A.11 3D Polyhedral Graphic Statics',
    'title': "Heinz Isler's Funicular Thin-Shell Domes: Inverted-Hanging Form-Finding, Zoelly Buckling & Imperfection Knockdowns",
    'subtitle': (
        "Continuing Folio A.01's 2D catenary thrust lines and A.11's 3D polyhedral force diagrams: a structural design study of "
        "Heinz Isler's physical form-finding—inverted hanging cloth, pneumatic membranes, and sculpted hills—coupled to an idealized "
        "spherical-cap model (31.6 m span, 4.2 m rise, 90 mm thickness) comparing Zoelly classical buckling against an illustrative "
        "imperfection-sensitivity knockdown curve."
    ),
    'date_published': '2026-11-20',
    'date_redated': '2026-11-20',
    'current_edition': 'REV 1.0',
    'status_badge': 'ISLER SHELL BUCKLING · REV 1.0',
    'primary_kernel': 'skills/architecture/a13/verify_a13_isler_buckling.py',
    'governing_law': 'R = (L² + 4f²)/(8f) · σ_mem = q R / (2t) · p_cr^cl = 2E / √(3(1−ν²)) · (t/R)² · p_cr^act = γ_kd · p_cr^cl',
    'colophon': {
        'identifier': 'A.13 · Heinz Isler Funicular Thin-Shell Domes & Imperfection Knockdowns · REV 1.0',
        'kernels': 'Inverted-Hanging Membrane Analogy · Zoelly Classical Shell Buckling · Imperfection Knockdown Curve',
        'benchmarks': 'Idealized spherical-cap model: L = 31.6 m · f = 4.2 m · R = 31.82 m · t = 90.0 mm · σ_mem = 0.587 MPa · p_cr^cl = 282.9 kN/m² · γ_kd = 0.189 · p_cr^act = 53.4 kN/m² · λ_b = 16.1',
        'bridge': 'Continues A.01/A.11 · Idealized spherical-cap stability model vs. free-edge shell form-finding',
    },
    'sliders': [
        {
            'label': 'Shell Crown Thickness (t)',
            'min': 40.0,
            'max': 140.0,
            'step': 5.0,
            'value': 90.0,
            'unit': ' mm',
        },
        {
            'label': 'Concrete Elastic Modulus (E_c)',
            'min': 15.0,
            'max': 45.0,
            'step': 1.0,
            'value': 30.0,
            'unit': ' GPa',
        },
    ],
    'steps': [
        (
            'Stage 1 (Inverted-Hanging Cloth & Pneumatic Form-Finding): In his 1959 IASS Madrid lecture (published 1961), '
            'Swiss engineer Heinz Isler grouped thin concrete shell form-finding into three physical experiments: freely shaped '
            'hills, inflated pneumatic membranes, and hanging textiles stiffened with plaster or frozen in winter air and inverted. '
            'Because a hanging sheet carries gravity load in pure membrane tension, its inverted rigid geometry channels uniform '
            'dead load along compression-only trajectories with minimal bending.'
        ),
        (
            'Stage 2 (Idealized Spherical-Cap Geometry & Uniform-Projection Membrane Stress): As a tractable analytical reference—distinct '
            'from Deitingen Süd\'s three-point free-edge wing shells, which share only the 90 mm double-rebar-cover thickness—the model '
            'evaluates a spherical cap of span L = 31.6 m and rise f = 4.2 m (curvature radius R = 31.82 m, rim half-angle φ_0 = 29.8°). '
            'At t = 90.0 mm (ρ = 2,400 kg/m³) plus 1.20 kN/m² superimposed load, uniform plan-projected gravity load is q = 3.318 kN/m² '
            '(neglecting the sec φ_0 = 1.152 slope factor at the rim and boundary haunches), giving crown compressive stress σ_mem = 0.587 MPa.'
        ),
        (
            'Stage 3 (Zoelly Classical Elastic Buckling & Post-Buckling Sensitivity): Because σ_mem = 0.587 MPa is under 2% of an '
            'assumed 35 MPa concrete compressive strength, crushing does not govern this model. Instead, thin doubly curved shells face '
            'elastic snap-through buckling. R. Zoelly\'s 1915 linear-elastic formula for an ideal uniform sphere under normal pressure '
            'gives p_cr^cl = 282.9 kN/m² at E = 30.0 GPa and ν = 0.20—an idealized upper bound that omits concrete creep, cracking '
            '(Ramm & Mehlhorn 1991, DOI 10.1016/0141-0296(91)90050-M), asymmetric snow, and edge bending.'
        ),
        (
            'Stage 4 (Illustrative Knockdown Curve & Tier T2 Hypothesis): Hutchinson (1967, DOI 10.1115/1.3607667), Gerasimidis et al. '
            '(2018, DOI 10.1115/1.4040455), and Abbasi, Derveni, and Reis (2023, DOI 10.1115/1.4056801) analyzed why tiny inward dimples '
            'sharply cut spherical shell buckling capacity below Zoelly\'s line. Applying an illustrative empirical-style knockdown function '
            'γ_kd = 0.14 + 0.32 exp(−0.1 √(R/t)) (NASA SP-8007 and Dulácska inspired, not a design code formula) at R/t = 353.5 yields '
            'γ_kd = 0.189, p_cr^act = 53.4 kN/m², and buckling ratio λ_b = 16.1. Hypothesis (Tier T2 model): elastic snap-through under '
            'inward dimples governs reserve rather than crushing; falsified for a physical shell if creep, cracking, asymmetric snow, '
            'or deeper inward dimples (δ_0 / t > 0.5) push collapse below λ_b = 3.0 or induce edge bending.'
        ),
    ],
    'readouts': [
        {
            'label': 'Membrane Compressive Stress',
            'value': '0.587 MPa (Crown, Model Service Load)',
        },
        {
            'label': 'Zoelly Classical Buckling Pressure',
            'value': '282.9 kN/m² (Idealized Linear Elastic)',
        },
        {
            'label': 'Illustrative Knockdown Pressure',
            'value': 'γ_kd = 0.189 ⇒ p_cr = 53.4 kN/m² (Model)',
        },
        {
            'label': 'Model Buckling Ratio (λ_b)',
            'value': '16.1 (Model Value · Not a Structural Check)',
        },
    ],
    'spec_plate': {
        'division': 'CSI MASTERFORMAT 03 31 00 / 03 38 00 / ACI 334R CONCRETE SHELL DESIGN STUDY',
        'title': 'Idealized Funicular Spherical-Cap Shell Model (90 mm Crown Reference)',
        'body': (
            'Analytical design study of an idealized spherical cap (L = 31.6 m, f = 4.2 m, R = 31.82 m, t = 90.0 mm) '
            'comparing Zoelly classical elastic buckling against an illustrative imperfection knockdown curve. Inspired by '
            'Heinz Isler\'s 90 mm double-rebar-cover Deitingen Süd shells, whose three-point free-edge geometry is more complex '
            'than a spherical cap. Model values only; not an engineered structural drawing or construction specification.'
        ),
        'meta': (
            'References: Ramm & Mehlhorn 1991 (DOI 10.1016/0141-0296(91)90050-M) · Hutchinson 1967 (DOI 10.1115/1.3607667) · '
            'Abbasi et al. 2023 (DOI 10.1115/1.4056801) · Tang 2015 (DOI 10.1260/0266-3511.30.1.1) · Model values, not measurements'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE A.13-A · DEITINGEN SÜD (1968) & THE 90 MM COVER DETAIL',
        'body': (
            'Heinz Isler\'s Deitingen Süd motorway canopies in Switzerland (1968) span 31.6 m across triangular wing shells '
            'supported on three points without edge beams (Tang 2015, DOI 10.1260/0266-3511.30.1.1). Their 90 mm thickness '
            'was set largely by construction durability—providing 20 mm concrete cover around double-layer reinforcement—rather '
            'than compressive crushing limits. Unlike our simplified spherical-cap benchmark, those free-edge wings rely on '
            'three-dimensional hanging-cloth curvature and upturned edge stiffening.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE A.13-B · INWARD DIMPLES VS. OUTWARD BUMPS (ABBASI ET AL. 2023)',
        'body': (
            'Flat plates hold post-buckling reserve after initial wrinkling, whereas doubly curved compression shells can '
            'snap inward suddenly when localized defects seed a dimple. Hutchinson (1967, DOI 10.1115/1.3607667) quantified '
            'this steep imperfection sensitivity, Gerasimidis et al. (2018, DOI 10.1115/1.4040455) examined localized dimples '
            'versus lateral probes, and Abbasi, Derveni, and Reis (2023, DOI 10.1115/1.4056801) showed that inward dimples '
            'cut spherical buckling strength more sharply than outward bumps of matching size.'
        ),
    },
    'skill': {
        'filename': 'isler-thin-shell-buckling-SKILL.md',
        'name': 'isler-thin-shell-buckling',
        'description': (
            'AI-agnostic architectural engineering skill for idealized thin spherical-cap membrane stress, '
            'Zoelly (1915) classical elastic buckling, and illustrative imperfection-sensitivity knockdown bounds.'
        ),
        'rules': [
            'Compute spherical-cap curvature radius R = (L^2 + 4 * f^2) / (8 * f) and uniform-projection crown membrane stress sigma_mem = (q * R) / (2 * t); record the rim slope factor sec(phi_0) omitted by uniform plan projection.',
            'Compute Zoelly (1915) classical elastic buckling pressure p_cr^cl = (2 * E / sqrt(3 * (1 - nu^2))) * (t / R)^2 and verify quadratic (t/R)^2 scaling when thickness doubles.',
            'Apply an explicit empirical-style knockdown function gamma_kd(R/t) = 0.14 + 0.32 * exp(-0.1 * sqrt(R / t)) as an illustrative bound (not a code rule) and check that thin 15 mm caps drop below lambda_b = 3.0.',
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.0',
            'date': '2026-11-20',
            'summary': (
                'REV 1.0 (Published 2026-11-20): Volume VII Architecture monograph continuing Folios A.01 & A.11 via '
                'Heinz Isler\'s physical form-finding, Zoelly (1915) classical spherical shell buckling, Hutchinson (1967) '
                'imperfection sensitivity, Ramm & Mehlhorn (1991) nonlinear concrete shell analysis, and Abbasi et al. (2023) '
                'inward-dimple vs. outward-bump knockdown mechanics.'
            ),
            'opus': (
                'Independent verification: all 6 new DOIs checked via Crossref API, anchor paper checked via Scite tallies API '
                '(51 citing publications, 0 retractions), and spherical-cap equations recomputed offline by '
                'skills/architecture/a13/verify_a13_isler_buckling.py (with --planted-defect).'
            ),
        },
    ],
    'volume': 7,
    'volume_code': 'VOL. 07',
    'reading_time': '22 MIN READ',
    'word_count': '4,780 WORDS',
    'scite': {
        'doi': '10.1016/0141-0296(91)90050-M',
        'fetched_on': '2026-11-20',
        'citing_publications': 51,
        'supporting': 0,
        'mentioning': 12,
        'contrasting': 0,
        'retracted': False,
        'summary': (
            'Scite Smart Citation index entry for Ramm & Mehlhorn, On shape finding methods and ultimate load analyses of '
            'reinforced concrete shells (Engineering Structures, 1991, DOI 10.1016/0141-0296(91)90050-M), checked 2026-11-20: '
            '51 citing publications (0 supporting, 12 mentioning, 0 contrasting) and no retraction notice. The counts describe '
            'that paper, not this folio\'s idealized spherical-cap model.'
        ),
    },
}

LONGFORM_DATA = {
    'reading_time': '22 MIN READ',
    'word_count': '4,780 WORDS',
    'parent_folios': ['A.01', 'A.11'],
    'lineage_mode': 'CONTINUATION · Continues A.01 Funicular Thrust Surfaces & A.11 3D Polyhedral Graphic Statics',
    'scite': FOLIO['scite'],
    'act1_title': 'Act I — Hanging Cloth in Winter Air: How Physical Models Found Shapes That Equations Missed',
    'act1_dropcap': (
        "In September 1959, at the first International Association for Shell Structures congress in Madrid, a young Swiss "
        "engineer named Heinz Isler stepped up with a brief lecture titled 'New Shapes for Shells' (published in the IASS "
        "Bulletin in 1961). While senior builders debated cylindrical barrels and circular domes derived from textbook formulas, "
        "Isler argued that gravity and surface tension could solve three-dimensional shell equilibrium without a single "
        "closed-form equation. He showed three physical ways to find forms: molding hills of earth or plaster, inflating "
        "rubber membranes or expansion foam, and hanging wet cloth or latex sheets from fixed anchor points until they settled "
        "under self-weight, stiffening them—sometimes by letting wet fabric freeze outdoors in Swiss winter air—and turning "
        "the resulting pouch upside down. This folio pairs Isler's experimental lineage with the classical elastic buckling "
        "theory of spherical shells and modern imperfection-sensitivity research."
    ),
    'act1_plain_bridge': (
        'In plain words, imagine holding a wet bedsheet by four corners. Gravity pulls the fabric into a smooth curved hammock '
        'where every single thread is stretched tight in tension, with zero wrinkles of compression. Now imagine freezing that '
        'hammock solid and flipping it upside down so it arches upward like a tent roof. Every path that used to pull in tension '
        'now pushes in compression, funneling the weight cleanly down to the four corners without bending. That is Heinz Isler\'s '
        'trick for concrete canopies. Yet making a shell paper-thin—like an eggshell scaled up to thirty meters—introduces a subtle '
        'trap. A thin concrete dome rarely crushes under its own weight; instead, like an aluminum soda can pressed from the top, '
        'a tiny inward dent can make the whole dome suddenly snap inward long before the concrete itself is stressed.'
    ),
    'act1_body': (
        "Isler's Madrid paper closed with a grid of thirty-nine freeform shell sketches followed by 'etc.', signaling that "
        "physical equilibrium opened an unbounded family of structural forms (Tang 2015, DOI 10.1260/0266-3511.30.1.1). Over "
        "the next four decades in Burgdorf, Isler engineered more than a thousand thin-shell canopies across Europe, including "
        "the iconic Deitingen Süd motorway service station (1968), whose two triangular concrete wings span 31.6 m while resting "
        "on just three supports each. As Gabriel Tang (2015, DOI 10.1260/0266-3511.30.1.1) documents, Deitingen's 90 mm thickness "
        "was governed primarily by placing 20 mm of protective concrete cover over two layers of steel reinforcement rather than "
        "by raw compressive strength. Later computational mechanics—reviewed by Ekkehard Ramm and Gerhard Mehlhorn (1991, DOI "
        "10.1016/0141-0296(91)90050-M) bridged physical hanging models to finite-element shape optimization and nonlinear "
        "ultimate-load analysis tracking concrete cracking, creep, and large deformations. More recently, Tang and Pedreschi "
        "(2020, DOI 10.1061/(ASCE)AE.1943-5568.0000430) explored pairing curved timber gridshells as reusable formwork for thin "
        "concrete shells to lower labor and falsework barriers."
    ),
    'act1_stakes': (
        'Conventional flat concrete slabs carry floor and roof loads through bending, placing half the cross-section in tension '
        'and requiring deep slabs and heavy steel reinforcement. Doubling the span of a flat beam raises bending moments by a '
        'factor of four, so long-span slabs spend most of their capacity carrying their own dead weight. Curved funicular shells '
        'redirect vertical loads into in-plane membrane compression, allowing a 90 mm concrete shell thickness (an illustrative 80% '
        'thickness ratio relative to a 450 mm solid flat slab, before counting edge beams or supports) to bridge wide spans. '
        'Understanding when thin shells fail by elastic snap-through buckling rather than crushing is therefore central to '
        'designing light, material-frugal roofs safely.'
    ),
    'pullquote': (
        '"A hanging cloth finds compression paths by gravity; yet an eggshell thin enough to avoid crushing still lives or fails '
        'by whether a millimeter-scale dimple can trigger elastic snap-through."'
    ),
    'chronology': [
        (
            '1915',
            'R. Zoelly (ETH Zürich doctoral thesis) derives the classical linear-elastic buckling pressure p_cr^cl for a perfect uniform spherical shell under external pressure.'
        ),
        (
            '1959–1968',
            'Heinz Isler presents "New Shapes for Shells" at the 1959 IASS Madrid congress (published 1961) and builds the 31.6 m three-point Deitingen Süd wing shells with 90 mm double-mesh cover (Tang 2015, DOI 10.1260/0266-3511.30.1.1).'
        ),
        (
            '1967–1968',
            'John W. Hutchinson (1967, DOI 10.1115/1.3607667) formulates spherical-shell post-buckling imperfection sensitivity, alongside NASA SP-8007 empirical buckling knockdown curves.'
        ),
        (
            '1991–2023',
            'Ramm & Mehlhorn (1991, DOI 10.1016/0141-0296(91)90050-M) unite computational form-finding and nonlinear concrete shell ultimate-load analysis; Gerasimidis et al. (2018, DOI 10.1115/1.4040455) and Abbasi, Derveni & Reis (2023, DOI 10.1115/1.4056801) quantify how inward dimple defects govern buckling knockdowns.'
        ),
    ],
    'act2_title': 'Act II — Cross-Field Intuition: The Inverted Hammock and the Soda-Can Dimple',
    'act2_analogy': (
        'An Isler thin shell combines two everyday intuitions: an upside-down hammock that guides weight strictly along '
        'compression paths, and a chicken eggshell or aluminum soda can that feels strong when squeezed evenly yet buckles '
        'abruptly if one small inward dimple disturbs its curvature.'
    ),
    'act2_plain_primer': (
        'Use the two interactive sliders below to explore this idealized spherical-cap model. The first slider adjusts Shell '
        'Crown Thickness (t) between 40 mm and 140 mm. Notice how thickening the concrete increases self-weight linearly, yet '
        'Zoelly classical buckling pressure climbs with the square of thickness—so cutting thickness in half cuts buckling '
        'resistance to roughly one quarter. The second slider adjusts the Concrete Elastic Modulus (E_c) between 15 GPa and '
        '45 GPa, illustrating how stiffness—including long-term concrete creep that lowers effective E_c—scales the critical '
        'buckling pressure proportionally. All readouts are idealized analytical model values, not field measurements or a '
        'structural code check.'
    ),
    'distill_diagram': {
        'analogy_title': 'The Inverted Hammock & The Eggshell Dimple',
        'analogy_sub': 'Funicular curvature keeps membrane compression tiny, leaving elastic snap-through as the governing model limit',
        'force_a_title': 'Shell Crown Thickness (t)',
        'force_a_sub': 'Governs quadratic Zoelly buckling scaling (t/R)^2 and imperfection sensitivity R/t',
        'force_b_title': 'Concrete Elastic Modulus (E_c)',
        'force_b_sub': 'Scales elastic buckling pressure linearly; creep lowers long-term effective E_c',
        'threshold_title': 'Model Buckling Reserve Ratio (λ_b)',
        'threshold_pass': 'Model ratio λ_b >= 3.0 in idealized elastic cap (not a building code check)',
        'threshold_fail': 'Below target λ_b < 3.0 in idealized model (thin-shell snap-through risk)',
    },
    'act2_intuition': (
        'Consider an idealized spherical cap spanning L = 31.6 m with crown rise f = 4.2 m—chosen to match the span scale of '
        'Deitingen Süd while keeping closed-form analytical tractability, since Deitingen\'s three-point free-edge wings are '
        'not spherical caps. Geometry gives radius of curvature R = (L^2 + 4 f^2)/(8 f) = 31.82 m and rim half-angle φ_0 = 29.8° '
        '(sec φ_0 = 1.152). Under uniform plan-projected self-weight q_sw = ρ g t = 2.118 kN/m² (at t = 90.0 mm, ρ = 2,400 kg/m³; '
        'this uniform-projection approximation neglects the 15.2% steeper shell slope near the rim and edge haunches) plus '
        '1.20 kN/m² superimposed load, total model load is q = 3.318 kN/m². Laplace-Young membrane equilibrium gives crown '
        'compressive stress σ_mem = q R / (2 t) = 0.587 MPa, far below an assumed 35 MPa concrete compressive strength.'
    ),
    'act2_deepening': (
        'Why can a shell fail when its compressive stress is under 2% of crushing strength? In 1915, R. Zoelly derived the '
        'classical linear-elastic buckling pressure of a complete uniform sphere under radial pressure: p_cr^cl = (2 E / '
        '√(3(1 − ν^2))) (t/R)^2 = 282.9 kN/m² for E = 30.0 GPa and ν = 0.20. Real shells buckle far below Zoelly\'s line. '
        'John W. Hutchinson (1967, DOI 10.1115/1.3607667) showed that spherical shells possess an unstable post-buckling branch '
        'where small geometric deviations produce steep load drops, and empirical aerospace curves (such as NASA SP-8007 for '
        'cylinders and Dulácska\'s concrete shell studies) introduced imperfection knockdown factors γ_kd(R/t). More recently, '
        'Gerasimidis et al. (2018, DOI 10.1115/1.4040455) and Abbasi, Derveni, and Reis (2023, DOI 10.1115/1.4056801) '
        'isolated how localized inward dimples lower buckling pressure much more severely than outward bumps of equal depth. '
        'Here we evaluate an illustrative empirical-style knockdown function γ_kd = 0.14 + 0.32 exp(−0.1 √(R/t))—explicitly '
        'a NASA SP-8007/Dulácska-inspired model trend rather than a design code formula—giving γ_kd = 0.189, p_cr^act = 53.4 kN/m², '
        'and λ_b = 16.1 at 90 mm. Hypothesis (Tier T2 model): elastic snap-through under inward dimples governs reserve rather '
        'than crushing; this elastic spherical-cap model is falsified for a physical concrete shell if long-term creep '
        '(E_eff = E / (1 + φ)), cracking (Ramm & Mehlhorn 1991, DOI 10.1016/0141-0296(91)90050-M), asymmetric snow drift, '
        'or deeper inward dimples (δ_0 / t > 0.5) pull collapse below λ_b = 3.0 or induce edge bending.'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Quadratic Thickness Scaling): Drag Shell Crown Thickness (t) from 40 mm to 140 mm. Watch '
            'Zoelly classical pressure climb quadratically with (t/R)^2 while membrane compressive stress falls.'
        ),
        (
            'Experiment 2 (Concrete Modulus & Creep Sensitivity): Lower Concrete Elastic Modulus (E_c) from 30 GPa toward '
            '15 GPa to model long-term creep softening (E_eff = E/(1 + φ)). Notice buckling ratio λ_b drops by half.'
        ),
        (
            'Experiment 3 (Thin-Shell Snap-Through Boundary): Slide thickness down to 40 mm and modulus to 15 GPa to inspect '
            'how R/t = 795 shrinks the illustrative knockdown factor γ_kd toward its lower asymptote.'
        ),
    ],
    'act4_title': 'Act IV — From Hanging Cloth to Gridshell Formwork & Imperfection-Aware Design',
    'act4_human_ai': (
        'Isler\'s hanging-cloth method fell out of widespread commercial use partly because custom curved timber falsework '
        'became expensive relative to standardized flat formwork (Tang 2015, DOI 10.1260/0266-3511.30.1.1). Modern digital '
        'form-finding—using open-source geometry tools such as COMPAS (https://github.com/compas-dev/compas, named as a tool '
        'a reader could use; not run for this folio)—combined with reusable timber or steel gridshell falsework (Tang & '
        'Pedreschi 2020, DOI 10.1061/(ASCE)AE.1943-5568.0000430) reopens thin concrete shells for low-material roofs.'
    ),
    'act4_deepening': (
        'Pairing computational form-finding with nonlinear ultimate-load analysis (Ramm & Mehlhorn 1991, DOI '
        '10.1016/0141-0296(91)90050-M) and localized dimple-sensitivity bounds (Gerasimidis et al. 2018, DOI '
        '10.1115/1.4040455; Abbasi et al. 2023, DOI 10.1115/1.4056801) turns shell stability from an empirical guess into an '
        'auditable design loop. Key open engineering questions include: how laser-scanned as-built concrete shell surfaces '
        'can feed localized dimple amplitude maps directly into nonlinear finite-element buckling checks before decentering, '
        'and how reusable gridshell falsework can keep curved casting economical without sacrificial timber waste.'
    ),
    'cf_bridge': '',
    'sources': [
        'Ramm, E., & Mehlhorn, G. (1991). On shape finding methods and ultimate load analyses of reinforced concrete shells. Engineering Structures, 13(2), 178–198. DOI: 10.1016/0141-0296(91)90050-M.',
        'Hutchinson, J. W. (1967). Imperfection Sensitivity of Externally Pressurized Spherical Shells. Journal of Applied Mechanics, 34(1), 49–55. DOI: 10.1115/1.3607667.',
        'Gerasimidis, S., Virot, E., Hutchinson, J. W., & Rubinstein, S. M. (2018). On Establishing Buckling Knockdowns for Imperfection-Sensitive Shell Structures. Journal of Applied Mechanics, 85(9), 091010. DOI: 10.1115/1.4040455.',
        'Abbasi, A., Derveni, F., & Reis, P. M. (2023). Comparing the Buckling Strength of Spherical Shells With Dimpled Versus Bumpy Defects. Journal of Applied Mechanics, 90(6), 061007. DOI: 10.1115/1.4056801.',
        'Tang, G. (2015). An Overview of Historical and Contemporary Concrete Shells, Their Construction and Factors in Their General Disappearance. International Journal of Space Structures, 30(1), 1–12. DOI: 10.1260/0266-3511.30.1.1.',
        'Tang, G., & Pedreschi, R. (2020). Gridshell as Formwork: Proof of Concept for a New Technique for Constructing Thin Concrete Shells Supported by Gridshell as Formwork. Journal of Architectural Engineering, 26(4), 04020037. DOI: 10.1061/(ASCE)AE.1943-5568.0000430.',
        'Isler, H. (1961). New Shapes for Shells (presented at 1st IASS Congress, Madrid, Sept 1959). Bulletin of the International Association for Shell Structures, 8.',
        'Zoelly, R. (1915). Ueber ein Knickungsproblem an der Kugelschale. Doctoral Thesis, ETH Zürich.',
        'Heyman, J. (1995). The Stone Skeleton: Structural Engineering of Masonry Architecture. Cambridge University Press. DOI: 10.1017/CBO9781107050310.',
        'Maxwell, J. C. (1864). On reciprocal figures and diagrams of forces. Philosophical Magazine, 27(182), 250–261. DOI: 10.1080/14786446408643663.',
        'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: 10.1162/qss_a_00146.',
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Inverted-Hanging Cloth Form-Finding and Zoelly Spherical Shell Buckling Knockdown">\n'
        '            <line x1="35" y1="186" x2="645" y2="186" stroke="currentColor" stroke-opacity="0.3"/>\n'
        '            <text x="44" y="24" font-size="10.5" font-weight="600" fill="currentColor">Inverted-Hanging Funicular Cap (L = 31.6 m, f = 4.2 m)</text>\n'
        '            <path d="M 54 152 Q 198 228 342 152" fill="none" stroke="var(--tp-stone)" stroke-width="2" stroke-dasharray="5,4"/>\n'
        '            <path id="tp-a13-shell-curve" d="M 54 152 Q 198 62 342 152" fill="none" stroke="var(--tp-prussian)" stroke-width="4.5"/>\n'
        '            <path d="M 164 98 Q 198 112 232 98" fill="none" stroke="var(--tp-minium)" stroke-width="2.2" stroke-dasharray="3,2"/>\n'
        '            <circle cx="54" cy="152" r="4" fill="var(--tp-prussian)"/>\n'
        '            <circle cx="342" cy="152" r="4" fill="var(--tp-prussian)"/>\n'
        '            <text x="58" y="176" font-size="9" fill="currentColor">Dashed below: hanging cloth tension · Solid above: inverted compression</text>\n'
        '            <line x1="376" y1="24" x2="376" y2="192" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="394" y="24" font-size="10.5" font-weight="600" fill="currentColor">Zoelly Classical vs. Knockdown Pressure</text>\n'
        '            <rect x="408" y="46" width="54" height="122" rx="3" fill="var(--tp-prussian)" fill-opacity="0.22" stroke="var(--tp-prussian)" stroke-width="1.5"/>\n'
        '            <rect id="tp-a13-act-bar" x="492" y="128" width="54" height="40" rx="3" fill="var(--tp-verdigris)" fill-opacity="0.35" stroke="var(--tp-verdigris)" stroke-width="1.8"/>\n'
        '            <rect x="576" y="158" width="54" height="10" rx="2" fill="var(--tp-minium)" fill-opacity="0.45" stroke="var(--tp-minium)" stroke-width="1.5"/>\n'
        '            <text id="tp-a13-pcl-lbl" x="435" y="40" text-anchor="middle" font-size="9" fill="var(--tp-prussian)">282.9 kPa</text>\n'
        '            <text id="tp-a13-pact-lbl" x="519" y="122" text-anchor="middle" font-size="9" fill="var(--tp-verdigris)">53.4 kPa</text>\n'
        '            <text id="tp-a13-q-lbl" x="603" y="152" text-anchor="middle" font-size="9" fill="var(--tp-minium)">3.32 kPa</text>\n'
        '            <text x="435" y="180" text-anchor="middle" font-size="8.5" fill="currentColor">Zoelly</text>\n'
        '            <text x="519" y="180" text-anchor="middle" font-size="8.5" fill="currentColor">γ_kd Model</text>\n'
        '            <text x="603" y="180" text-anchor="middle" font-size="8.5" fill="currentColor">Load q</text>\n'
        '            <text x="44" y="206" font-size="10" fill="var(--tp-verdigris)">Idealized Spherical-Cap Model · Not a Structural Code Check</text>\n'
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Studio architectural photograph of a plaster-stiffened cotton catenary hanging cloth clamped in a timber frame '
        'beside a thin cast-concrete wing-shell canopy scale model resting on three steel point supports on a beechwood workbench '
        '(physical studio model study, not a full-scale measured structure)'
    ),
    'caption': (
        'Studio Model Plate A.13-V · Tactile physical scale study illustrating Heinz Isler\'s inverted-hanging cloth form-finding '
        '(left) alongside a thin cast-concrete wing-shell canopy on three supports (right). Artistic studio model study; the '
        'mathematical model on this page evaluates an idealized spherical cap, not this wing geometry.'
    ),
}

DISPATCH = {
    'kicker': 'FRONTIER SHELL STABILITY DISPATCH · ZOELLY 1915, HUTCHINSON 1967 & ABBASI ET AL. 2023',
    'headline': 'Inward Dimples, Imperfection Knockdowns, and the Buckling Limit of Thin Funicular Concrete Shells',
    'body': (
        'Pairing Ramm and Mehlhorn\'s nonlinear concrete shell analysis (DOI 10.1016/0141-0296(91)90050-M) with spherical '
        'imperfection sensitivity from Hutchinson (1967, DOI 10.1115/1.3607667) and Abbasi, Derveni, and Reis (2023, DOI '
        '10.1115/1.4056801), this folio evaluates an idealized 90 mm spherical cap (R = 31.82 m) where crown compression is '
        '0.587 MPa and an illustrative knockdown curve yields λ_b = 16.1. Model values only, not field measurements.'
    ),
}

META_3D = (
    'Isler Spherical-Cap Membrane Stress & Imperfection Knockdown Surface',
    'X: Crown Thickness t · Z: Concrete Modulus E_c · Y: Zoelly vs. Knockdown Buckling Pressure',
)

ES_TRANSLATION = {
    'title_es': (
        'Domos Funiculares de Cáscara Delgada de Heinz Isler: Telas Colgantes, Pandeo de Zoelly y Factores de Reducción'
    ),
    'subtitle_es': (
        'Continuando las líneas de empuje de A.01 y los poliedros recíprocos de A.11: un estudio de diseño sobre los modelos '
        'físicos de Heinz Isler y un modelo analítico de casquete esférico idealizado (31.6 m de claro, 4.2 m de flecha, '
        '90 mm de espesor) que compara el pandeo clásico de Zoelly frente a una curva ilustrativa de sensibilidad a imperfecciones.'
    ),
    'why_es': (
        'Una tela colgada encuentra por gravedad la geometría que, al invertirse, trabaja en compresión; pero una cáscara '
        'delgada rara vez falla por aplastamiento, sino por pandeo elástico súbito si una pequeña abolladura altera su curvatura.'
    ),
    'bridge_es': (
        'Continúa A.01 y A.11: modelo analítico de estabilidad en casquete esférico idealizado frente a modelos físicos de cáscaras.'
    ),
    'plain_es': (
        'En palabras sencillas, imaginen sostener una sábana húmeda por sus cuatro esquinas. La gravedad la curva en una hamaca '
        'suave donde cada hilo está estirado en tracción. Si esa forma se endurece y se voltea boca arriba, las trayectorias que '
        'estaban en tracción pasan a trabajar en compresión limpia hacia los apoyos. Así buscó Heinz Isler la geometría de sus '
        'cubiertas delgadas de concreto. No obstante, al hacer un techo tan esbelto como el cascarón de un huevo a gran escala, '
        'el riesgo principal no es que el concreto se aplaste bajo su propio peso, sino que una pequeña hendidura hacia adentro '
        'provoque un pandeo repentino mucho antes de agotar la resistencia del material.'
    ),
    'deep_es': (
        'A nivel analítico, este folio evalúa un casquete esférico idealizado de claro L = 31.6 m y flecha f = 4.2 m '
        '(radio R = 31.82 m, ángulo de borde φ_0 = 29.8°, sec φ_0 = 1.152) con espesor de referencia t = 90.0 mm—inspirado en '
        'el recubrimiento doble de Deitingen Süd (1968), aunque Deitingen es una lámina triangular de tres apoyos con bordes libres '
        'y no un casquete esférico. Bajo carga proyectada uniforme q = 3.318 kN/m² (sin incluir el aumento por pendiente sec φ_0 ni '
        'engrosamientos de borde), el esfuerzo de membrana es 0.587 MPa, mientras la fórmula lineal elástica de Zoelly (1915) da '
        '282.9 kN/m² (E = 30.0 GPa, ν = 0.20), omitiendo fluencia lenta, fisuración (Ramm y Mehlhorn, 1991), nieve asimétrica y '
        'flexión de borde. Aplicando una curva ilustrativa inspirada en NASA SP-8007 y Dulácska (γ_kd = 0.189, no una norma de '
        'diseño), la presión crítica del modelo baja a 53.4 kN/m² (razón λ_b = 16.1). Hipótesis (modelo de nivel T2): el pandeo '
        'elástico por abolladuras hacia adentro (Hutchinson, 1967; Abbasi et al., 2023) gobierna la reserva estructural; se '
        'refuta para una obra real si la fluencia, el agrietamiento o abolladuras profundas reducen la capacidad por debajo de 3.0.'
    ),
}
