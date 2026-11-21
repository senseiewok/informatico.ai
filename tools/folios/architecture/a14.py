#!/usr/bin/env python3
"""Folio A.14 (ARCHITECTURE): Félix Candela's Hypar Ruled Shells: Straight-Line Formwork, Pucher Membrane Shear & Umbrella Limits."""
from __future__ import annotations

SLUG = 'a14'

PILLAR = 'architecture'

FOLIO = {
    'folio_id': 'A.14',
    'slug': 'a14',
    'pillar': 'architecture',
    'category_code': 'A',
    'parent_folios': ['A.01', 'A.13'],
    'lineage_mode': 'CONTINUATION · Continues A.01 Funicular Thrust Surfaces & A.13 Heinz Isler Thin Shells',
    'title': "Félix Candela's Hypar Ruled Shells: Hyperbolic Paraboloid Membrane Shear & Straight-Line Formwork",
    'subtitle': (
        "Continuing Folio A.01's funicular thrust surfaces and A.13's inverted-hanging concrete shells: a structural design study "
        "of how hyperbolic paraboloid (hypar) geometry uses straight timber plank rulings to form doubly curved 40 mm concrete "
        "umbrellas (12.0 m quadrant semi-span, 4.0 m rise), mapping Pucher's flat-projection membrane shear model (N_xy = 31.35 kN/m, "
        "σ_2 = -0.784 MPa) alongside cantilevered free-edge, valley-rib, and thin-shell buckling boundaries."
    ),
    'date_published': '2026-11-21',
    'date_redated': '2026-11-21',
    'current_edition': 'REV 1.0',
    'status_badge': 'CANDELA HYPAR SHELL · REV 1.0',
    'primary_kernel': 'skills/architecture/a14/verify_a14_candela_hypar.py',
    'governing_law': 'z = (h / (a b)) x y · N_xy = (q_0 a b) / (2 h) · σ_1 = +N_xy / t · σ_2 = -N_xy / t · M_x = M_y = 0',
    'colophon': {
        'identifier': 'A.14 · Félix Candela Hypar Ruled Shells & Pucher Membrane Shear · REV 1.0',
        'kernels': 'Doubly-Ruled Hypar Saddle · Pucher Flat-Projection Shear · 45-Degree Principal Arch-Tie Field',
        'benchmarks': (
            'Model values (not measurements): a = b = 12.0 m · h = 4.0 m · t = 40.0 mm · q_0 = 1.741 kN/m² · '
            'N_xy = 31.35 kN/m · σ_2 = -0.784 MPa · λ_comp = 20.1 · 80.0% shell-field thickness saving vs 200 mm slab · '
            'Q_storm = 8.0 L/s (576 m²)'
        ),
        'bridge': 'Continues A.01/A.13 · Idealized Pucher membrane shear vs. cantilevered free-edge & rib behavior',
    },
    'sliders': [
        {
            'label': 'Hypar Quadrant Semi-Span (a = b)',
            'min': 6.0,
            'max': 18.0,
            'step': 1.0,
            'value': 12.0,
            'unit': ' m',
        },
        {
            'label': 'Hypar Corner Rise (h)',
            'min': 1.0,
            'max': 6.0,
            'step': 0.5,
            'value': 4.0,
            'unit': ' m',
        },
    ],
    'steps': [
        (
            'Stage 1 (Doubly-Ruled Hypar Geometry & Unbent Timber Formwork): A hyperbolic paraboloid quadrant z(x, y) = (h / (a b)) x y '
            'has negative Gaussian curvature everywhere (an anticlastic saddle) yet contains two families of straight generating lines '
            'along constant x and constant y. Because every section parallel to the axes is a straight line, builders could assemble '
            'formwork from unbent straight timber planks without curved falsework (Cassinello et al. 2010, DOI 10.3989/ic.10.040; '
            'Garlock & Billington 2011, DOI 10.2749/101686611x13049248220564).'
        ),
        (
            'Stage 2 (Pucher Projected Membrane Equilibrium): Under uniform plan-projected gravity load q_0 = 1.741 kN/m² '
            '(40.0 mm concrete at ρ = 2,400 kg/m³ giving 0.941 kN/m² plus 0.80 kN/m² superimposed load), Pucher\'s 1934 projected '
            'equilibrium equation cancels normal membrane terms because ∂²z/∂x² = 0 and ∂²z/∂y² = 0 identically. In this idealized '
            'interior membrane model with supported edges, N_x = N_y = M_x = M_y = 0 and uniform shear becomes N_xy = (q_0 a b) / (2 h) = 31.35 kN/m.'
        ),
        (
            'Stage 3 (Diagonal Principal Arch-Tie Field & Thickness Ratio): Rotating 45 degrees onto the bisecting diagonals resolves pure '
            'shear into equal principal tension σ_1 = +N_xy / t = +0.784 MPa and principal compression σ_2 = -N_xy / t = -0.784 MPa. '
            'Against an allowable compressive threshold of 0.45 f_ck = 15.75 MPa (f_ck = 35 MPa), the model compressive ratio is '
            'λ_comp = 20.1, while the 40 mm shell field uses 80.0% less concrete volume than a 200 mm solid flat slab (excluding stem and ribs).'
        ),
        (
            'Stage 4 (Central Stormwater Funnel & Tier T2 Model Boundary): Grouping four quadrants into a 24.0 m by 24.0 m (576 m²) '
            'umbrella slopes rainwater inward toward a central hollow stem, collecting 8.0 L/s (28.8 m³/h) under 50 mm/h design rain. '
            'Hypothesis (Tier T2 analytical model): straight-ruled anticlastic curvature carries symmetric gravity load primarily in '
            'in-plane shear rather than bending. This flat-projection model is falsified for physical cantilevered umbrellas where slope-angle '
            'self-weight growth, free-edge boundary bending, valley-rib concentration, concrete creep, or thin-shell buckling '
            '(Ramm & Mehlhorn 1991, DOI 10.1016/0141-0296(91)90050-M; Wang et al. 2020, DOI 10.1016/j.engstruct.2020.111156) govern failure.'
        ),
    ],
    'readouts': [
        {
            'label': 'Membrane Shear Force (N_xy)',
            'value': '31.35 kN/m (Uniform in Model Quadrant)',
        },
        {
            'label': 'Principal Compressive Stress (σ_2)',
            'value': '-0.784 MPa (Quadrant Field, Model Service Load)',
        },
        {
            'label': 'Model Compressive Margin (λ_comp)',
            'value': 'λ_comp = 20.1 (80.0% Savings vs 200 mm)',
        },
        {
            'label': 'Stormwater Harvest Rate (50 mm/h)',
            'value': '8.0 L/s (28.8 m³/h, 576 m² Model Roof)',
        },
    ],
    'spec_plate': {
        'division': 'CSI MASTERFORMAT 03 31 00 / 03 38 00 · CONCRETE HYPAR DESIGN STUDY',
        'title': 'Doubly-Ruled Hyperbolic Paraboloid Umbrella Shell (40 mm Field Model)',
        'body': (
            'Analytical design study of an idealized 4-quadrant hyperbolic paraboloid umbrella (24.0 m by 24.0 m overall plan, '
            'a = b = 12.0 m quadrant semi-span, h = 4.0 m rise, 40.0 mm shell field thickness) using Pucher flat-projection '
            'membrane equilibrium. Model values only; omits slope-angle dead-weight amplification, cantilevered free-edge bending, '
            'valley ribs, reinforcement detailing, and creep buckling. Not an engineered structural drawing or construction plan.'
        ),
        'meta': (
            'References: Candela 1960 (DOI 10.14359/8024, 10.14359/8026) · Billington & Garlock 2010 (DOI 10.1061/(asce)st.1943-541x.0000144) · '
            'Wang et al. 2020 (DOI 10.1016/j.engstruct.2020.111156) · Model values, not measurements'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE A.14-A · OVER 800 THIN SHELLS IN MEXICO CITY & BEYOND',
        'body': (
            'Cassinello, Schlaich, and Torroja (2010, DOI 10.3989/ic.10.040) document how Spanish-born architect-engineer Félix '
            'Candela built more than 800 reinforced-concrete thin shells—chiefly in Mexico—pairing doubly curved strength with '
            'low-cost carpentry. Billington and Garlock (2010, DOI 10.1061/(asce)st.1943-541x.0000144) and Garlock and Billington '
            '(2011, DOI 10.2749/101686611x13049248220564) examine how Candela united economy, efficiency, and sculptural form.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE A.14-B · STRAIGHT RULINGS VS. CANTILEVER EDGE BENDING',
        'body': (
            'Because z = (h / (a b)) x y has zero second partial derivatives along the x and y axes, Pucher\'s 1934 projected '
            'membrane equation yields constant shear N_xy = q_0 a b / (2 h) when edges carry tangential shear. In physical cantilevered '
            'umbrellas (Candela 1960, DOI 10.14359/8026; Wang et al. 2020, DOI 10.1016/j.engstruct.2020.111156; Wang et al. 2022, '
            'DOI 10.1016/j.engstruct.2022.114577), free outer edges and central valley intersections alter shear flow and demand '
            'nonlinear ultimate-load analysis (Ramm & Mehlhorn 1991, DOI 10.1016/0141-0296(91)90050-M).'
        ),
    },
    'skill': {
        'filename': 'candela-hypar-membrane-shear-SKILL.md',
        'name': 'candela-hypar-membrane-shear',
        'description': (
            'AI-agnostic architectural and structural engineering skill for Félix Candela\'s doubly-ruled hyperbolic paraboloid '
            '(hypar) concrete shells, Pucher flat-projection membrane shear equilibrium, and idealized cantilever/rib bounds.'
        ),
        'rules': [
            'Define one quadrant of a hyperbolic paraboloid saddle as z(x, y) = (h / (a * b)) * x * y with twist parameter c = (a * b) / h.',
            'Compute Pucher flat-projection membrane shear resultant as N_xy = (q_0 * a * b) / (2 * h) under uniform projected gravity load q_0, noting omitted slope-angle weight amplification.',
            'Resolve 45-degree principal stresses as sigma_1 = +N_xy / t (tension) and sigma_2 = -N_xy / t (compression) in the idealized interior membrane model.',
            'Evaluate compressive margin lambda_comp = (0.45 * f_ck) / |sigma_2| alongside shell-field thickness savings relative to a 200 mm slab, and flag free-edge bending and buckling limits.',
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.0',
            'date': '2026-11-21',
            'summary': (
                'REV 1.0 (Published 2026-11-21): Volume VII Architecture monograph continuing Folios A.01 & A.13 via Félix '
                'Candela\'s doubly-ruled hyperbolic paraboloid shells (1960 ACI papers), Pucher projected membrane shear (1934), '
                'central umbrella stormwater drainage, and modern multi-sided umbrella evaluations (Wang et al. 2020, 2022).'
            ),
            'opus': (
                'Independent verification: all 7 new DOIs checked via Crossref API, anchor paper checked via Scite tallies API '
                '(16 citing publications, 0 retractions), and hypar equilibrium equations recomputed offline by '
                'skills/architecture/a14/verify_a14_candela_hypar.py (with --planted-defect).'
            ),
        },
    ],
    'volume': 7,
    'volume_code': 'VOL. 07',
    'reading_time': '22 MIN READ',
    'word_count': '4,820 WORDS',
    'scite': {
        'doi': '10.14359/8024',
        'fetched_on': '2026-11-21',
        'citing_publications': 16,
        'supporting': 0,
        'mentioning': 0,
        'contrasting': 0,
        'retracted': False,
        'summary': (
            'Scite Smart Citation index entry for Candela, General Formulas for Membrane Stresses in Hyperbolic Paraboloidical '
            'Shells (ACI Journal Proceedings, Vol. 57, 1960, DOI 10.14359/8024), checked 2026-11-21: 16 citing publications '
            '(0 supporting, 0 mentioning, 0 contrasting) and no retraction notice. Counts describe that paper, not this folio\'s model.'
        ),
    },
}

LONGFORM_DATA = {
    'reading_time': '22 MIN READ',
    'word_count': '4,820 WORDS',
    'parent_folios': ['A.01', 'A.13'],
    'lineage_mode': 'CONTINUATION · Continues A.01 Funicular Thrust Surfaces & A.13 Heinz Isler Thin Shells',
    'scite': FOLIO['scite'],
    'act1_title': 'Act I — Straight Boards, Saddle Roofs: How Negative Curvature Built Thin Concrete Shells in Mexico',
    'act1_dropcap': (
        "In post-war Mexico City, building a curved concrete roof usually meant building an expensive curved wooden scaffold first "
        "and throwing most of that timber away after the concrete hardened. Félix Candela—a Madrid-born architect who arrived in "
        "Mexico in 1939 and co-founded the shell contracting firm Cubiertas Ala—spotted a mathematical escape hatch inside one "
        "surface: the hyperbolic paraboloid, or hypar. Although a hypar looks deeply sculpted like a horse's saddle, every point "
        "on it lies at the intersection of two completely straight lines. Carpenters could nail ordinary straight pine boards onto "
        "simple tilted frames, cast concrete just 40 mm thick across the warped deck, and reuse the boards on the next market hall, "
        "factory, or church. This folio pairs Candela's straight-ruled construction insight with Adolf Pucher's 1934 membrane "
        "equilibrium formula and examines where the simple interior shear model stops holding near cantilevered edges."
    ),
    'act1_plain_bridge': (
        'Picture twisting a square wooden picture frame by lifting two opposite corners up and pulling the other two corners down. '
        'Now lay straight wooden pencils side by side from one edge to the opposite edge. Even though the whole surface curves like '
        'a saddle or a potato chip, every single pencil stays dead straight from end to end. That geometric trick let Candela\'s crews '
        'build dramatic curved concrete roofs using ordinary flat lumber instead of custom curved carpentry. Even better, once four '
        'of those twisted squares meet at a single central post like an inverted umbrella, the sloped grooves guide rainwater straight '
        'down the middle stem instead of pooling on a flat slab. The engineering catch is just as concrete: if you make the twisted '
        'square too shallow, or leave its outer corners hanging free without ribs, internal forces shoot upward and bending creeps '
        'back into the thin shell.'
    ),
    'act1_body': (
        "Cassinello, Schlaich, and Torroja (2010, DOI 10.3989/ic.10.040) chronicle how Candela delivered more than 800 thin "
        "reinforced-concrete shells across Mexico and abroad, earning praise from David Billington, Frei Otto, and Ove Arup as "
        "exemplars of structural art (Billington & Garlock 2010, DOI 10.1061/(asce)st.1943-541x.0000144; Garlock & Billington 2011, "
        "DOI 10.2749/101686611x13049248220564). In two companion 1960 ACI Journal papers—General Formulas for Membrane Stresses in "
        "Hyperbolic Paraboloidical Shells (DOI 10.14359/8024) and Hyperbolic Paraboloidal Umbrella Shells under Vertical Loads "
        "(DOI 10.14359/8026), Candela laid out closed-form equilibrium formulas grounded in Adolf Pucher's 1934 projected stress "
        "method. Whereas Folio A.13 traced Heinz Isler's synclastic hanging-cloth shells (curved the same way in both directions, "
        "requiring curved molds or pneumatic balloons), anticlastic hypars curve upward along one diagonal and downward along the "
        "other. Contemporary structural engineering studies continue to re-evaluate Candela's 8-sided and hexagonal umbrellas "
        "(Wang et al. 2020, DOI 10.1016/j.engstruct.2020.111156; Wang et al. 2022, DOI 10.1016/j.engstruct.2022.114577) using "
        "modern computational tools alongside nonlinear shell mechanics (Ramm & Mehlhorn 1991, DOI 10.1016/0141-0296(91)90050-M)."
    ),
    'act1_stakes': (
        'Flat reinforced-concrete roof slabs carry gravity loads by bending, which forces concrete near the bottom into tension where '
        'it cracks unless deep sections and dense steel bars carry the pull. A 200 mm solid flat slab spends a large share of its '
        'embodied cement simply holding up its own dead weight. Redirecting vertical gravity into in-plane membrane shear lets a '
        '40.0 mm shell field use 80.0% less concrete volume across the quadrant field than a 200 mm solid slab—before accounting for '
        'the central stem, valley ribs, and foundation. At the same time, industrial and civic buildings in heavy seasonal rain '
        'need roofs that shed water cleanly without ponding. Knowing both the power and the limits of Pucher\'s shear formula keeps '
        'material-frugal shell design honest.'
    ),
    'pullquote': (
        '"Twist a square frame along its corners and straight timber boards weave a doubly curved roof—sending gravity along 45-degree '
        'arches and rain down the central stem."'
    ),
    'chronology': [
        (
            '1934',
            'Austrian engineer Adolf Pucher publishes projected shell equilibrium equations in Beton und Eisen, mapping spatial shell forces onto a flat horizontal reference grid.'
        ),
        (
            '1950–1968',
            'Félix Candela and Cubiertas Ala construct more than 800 thin concrete shells across Mexico, showing straight-plank formwork practical for industrial umbrellas and civic landmarks (Cassinello et al. 2010, DOI 10.3989/ic.10.040).'
        ),
        (
            '1960',
            'Candela publishes General Formulas for Membrane Stresses in Hyperbolic Paraboloidical Shells (DOI 10.14359/8024) and Hyperbolic Paraboloidal Umbrella Shells under Vertical Loads (DOI 10.14359/8026) in ACI Journal Proceedings.'
        ),
        (
            '2010–2022',
            'Billington & Garlock (2010, DOI 10.1061/(asce)st.1943-541x.0000144) frame Candela\'s shells as structural art, while Wang et al. (2020, DOI 10.1016/j.engstruct.2020.111156; 2022, DOI 10.1016/j.engstruct.2022.114577) evaluate multi-sided umbrella shells.'
        ),
    ],
    'act2_title': 'Act II — Cross-Field Intuition: The Saddle Twist and 45-Degree Arch-Tie Paths',
    'act2_analogy': (
        'A hyperbolic paraboloid quadrant acts like a woven saddle stretched between diagonal arches and suspension cables: '
        'along one 45-degree diagonal it arches upward in compression like a stone vault, while along the perpendicular diagonal '
        'it sags downward in tension like a hanging rope, keeping the interior membrane balanced in pure shear.'
    ),
    'act2_plain_primer': (
        'Use the two interactive sliders below to test how geometry controls force inside this idealized 40.0 mm concrete hypar model. '
        'The first slider adjusts Hypar Quadrant Semi-Span (a = b) from 6.0 m to 18.0 m (tripling the full umbrella width from 12 m to '
        '36 m). Watch how membrane shear force climbs with the square of semi-span because both the twist distance and the roof area '
        'grow together. The second slider adjusts Hypar Corner Rise (h) from 1.0 m to 6.0 m. Making the shell flatter (smaller h) '
        'forces shear and principal stresses sharply upward, whereas raising the corners reduces membrane stress proportionally. All '
        'numbers displayed are idealized analytical model values, not field measurements or a structural code check.'
    ),
    'distill_diagram': {
        'analogy_title': 'The Twisted Saddle & 45-Degree Arch-Tie Network',
        'analogy_sub': 'Straight asymptotic rulings remove second-derivative curvature terms, leaving pure diagonal tension and compression',
        'force_a_title': 'Quadrant Semi-Span (a = b)',
        'force_a_sub': 'Scales umbrella roof area (4ab) and Pucher membrane shear quadratically under fixed rise',
        'force_b_title': 'Hypar Corner Rise (h)',
        'force_b_sub': 'Controls geometric twist c = ab/h; flattening the rise amplifies N_xy inversely',
        'threshold_title': 'Model Compressive Margin (λ_comp)',
        'threshold_pass': 'Model margin λ_comp >= 3.0 in idealized interior membrane (not a building code check)',
        'threshold_fail': 'Below target λ_comp < 3.0 in idealized model (excessive shallow-shell compression)',
    },
    'act2_intuition': (
        'Consider one quadrant of a symmetrical umbrella shell spanning x in [0, a] and y in [0, b] with a = b = 12.0 m and '
        'corner rise h = 4.0 m, giving an overall four-quadrant umbrella footprint of 24.0 m by 24.0 m (576 m²). The elevation '
        'surface z(x, y) = (h / (a b)) x y defines geometric twist parameter c = (a b) / h = 36.0 m. At shell field thickness '
        't = 40.0 mm and concrete density ρ = 2,400 kg/m³, dead weight is 0.941 kN/m²; adding 0.80 kN/m² superimposed live/roofing '
        'load produces total plan-projected service load q_0 = 1.741 kN/m². Notice the explicit modeling simplification: projecting '
        'self-weight uniformly onto the horizontal plan omits the slope factor √(1 + (h x / a b)² + (h y / a b)²) that slightly '
        'increases dead load near steep corners.'
    ),
    'act2_deepening': (
        'Differentiating z(x, y) = (h / (a b)) x y gives ∂²z/∂x² = 0, ∂²z/∂y² = 0, and mixed twist curvature ∂²z/∂x∂y = h / (a b) = 1 / c. '
        'In Adolf Pucher\'s 1934 projected membrane equilibrium equation for downward vertical load q_0—which equates '
        'N_x(∂²z/∂x²) + 2 N_xy(∂²z/∂x∂y) + N_y(∂²z/∂y²) = +q_0 when horizontal external loads vanish—both normal-curvature terms drop out. '
        'When boundary members absorb tangential edge shear, the interior membrane settles into N_x = N_y = 0, M_x = M_y = 0, and '
        'uniform shear N_xy = +(q_0 a b) / (2 h) = +31.35 kN/m. Along 45-degree bisectors, Mohr\'s circle converts pure shear '
        'into principal tension σ_1 = +N_xy / t = +0.784 MPa and principal compression σ_2 = -N_xy / t = -0.784 MPa. Against an '
        'illustrative allowable compressive bound of 0.45 f_ck = 15.75 MPa (for f_ck = 35 MPa), λ_comp = 20.1, while a 40 mm shell '
        'field saves 80.0% volume versus a 200 mm slab and funnels 50 mm/h rainfall at 8.0 L/s (28.8 m³/h) down the central column. '
        'Hypothesis (Tier T2 analytical model): straight-ruled saddle geometry keeps interior membrane compression far below crushing '
        'at 40 mm thickness; this model is falsified for a physical cantilevered umbrella where free-edge boundary conditions, '
        'valley-rib concentration, asymmetric wind/snow loads, concrete creep, or snap-through buckling '
        '(Ramm & Mehlhorn 1991, DOI 10.1016/0141-0296(91)90050-M; Wang et al. 2020, DOI 10.1016/j.engstruct.2020.111156) dominate.'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Quadratic Span Growth): Drag Hypar Quadrant Semi-Span (a = b) from 6.0 m to 18.0 m at h = 4.0 m. '
            'Notice membrane shear N_xy quadruples when semi-span doubles from 6.0 m to 12.0 m (7.84 kN/m to 31.35 kN/m), while '
            'stormwater catchment rises fourfold from 2.0 L/s to 8.0 L/s.'
        ),
        (
            'Experiment 2 (Inverse Corner-Rise Amplification): Lower Hypar Corner Rise (h) from 4.0 m down to 2.0 m at a = b = 12.0 m. '
            'Shear doubles cleanly to 62.69 kN/m and compressive margin λ_comp halves from 20.1 to 10.0.'
        ),
        (
            'Experiment 3 (High-Span Shallow Regime): Push Semi-Span to 18.0 m and drop Corner Rise to 1.0 m. Watch N_xy climb '
            'to 282.11 kN/m and σ_2 deepen to -7.053 MPa (λ_comp = 2.2 < 3.0), triggering the model alert state and illustrating why '
            'very flat hypars need deeper rise, thicker edges, or nonlinear buckling analysis.'
        ),
    ],
    'act4_title': 'Act IV — From Straight Timber Boards to Multi-Sided Umbrella Shells & Nonlinear Limits',
    'act4_human_ai': (
        'Candela\'s straight-board formwork trick made custom concrete shells economical when skilled labor was affordable and timber '
        'planks could be stripped and reused across dozens of repetitive umbrella bays (Tang 2015, DOI 10.1260/0266-3511.30.1.1; '
        'Garlock & Billington 2011, DOI 10.2749/101686611x13049248220564). Today, designers can pair straight-ruled parametric '
        'geometry scripts—for example in open-source COMPAS (https://github.com/compas-dev/compas, named as an available open tool, '
        'not run for this folio)—with reusable gridshell or modular scaffolding systems.'
    ),
    'act4_deepening': (
        'Where Pucher\'s hand formula gave Candela rapid preliminary sizing, modern finite-element evaluations of his 8-sided and '
        'hexagonal umbrellas (Wang et al. 2020, DOI 10.1016/j.engstruct.2020.111156; Wang et al. 2022, DOI '
        '10.1016/j.engstruct.2022.114577) alongside nonlinear concrete shell analysis (Ramm & Mehlhorn 1991, DOI '
        '10.1016/0141-0296(91)90050-M) examine realistic support ribs, cracking, creep, and cantilevered edge behavior that '
        'flat-projection membrane equations leave out. Open architectural engineering questions include how automated timber/steel '
        'ruled-surface falsework and recycled low-clinker concrete mixes can revive thin umbrella roofs for urban stormwater capture '
        'and shaded civic courtyards without sacrificing buckling or creep safety.'
    ),
    'cf_bridge': '',
    'sources': [
        'Candela, F. (1960). General Formulas for Membrane Stresses in Hyperbolic Paraboloidical Shells. ACI Journal Proceedings, 57. DOI: 10.14359/8024.',
        'Candela, F. (1960). Hyperbolic Paraboloidal Umbrella Shells under Vertical Loads. ACI Journal Proceedings, 57. DOI: 10.14359/8026.',
        'Billington, D. P., & Moreyra Garlock, M. E. (2010). Structural Art and the Example of Félix Candela. Journal of Structural Engineering, 136(4), 339–342. DOI: 10.1061/(asce)st.1943-541x.0000144.',
        'Garlock, M. E. M., & Billington, D. P. (2011). Eminent Structural Engineer: Félix Candela—Structural Artist of Thin Shell Concrete Forms. Structural Engineering International, 21(4), 520–523. DOI: 10.2749/101686611x13049248220564.',
        'Wang, S., Levine, A., Garlock, M., Contreras-Jiménez, J. A., & Jorquera-Lucerga, J. J. (2020). Structural evaluation of Félix Candela’s 8-sided hyperbolic paraboloidal umbrellas. Engineering Structures, 222, 111156. DOI: 10.1016/j.engstruct.2020.111156.',
        'Wang, S., Contreras-Jimenez, J. A., Jorquera-Lucerga, J. J., & Garlock, M. (2022). Structural analysis of Félix Candela’s hexagonal hyperbolic paraboloidal umbrellas. Engineering Structures, 266, 114577. DOI: 10.1016/j.engstruct.2022.114577.',
        'Cassinello, P., Schlaich, M., & Torroja, J. A. (2010). Félix Candela. En memoria (1910-1997). Del cascarón de hormigón a las estructuras ligeras del s. XXI. Informes de la Construcción, 62(519), 5–26. DOI: 10.3989/ic.10.040.',
        'Tang, G. (2015). An Overview of Historical and Contemporary Concrete Shells, Their Construction and Factors in Their General Disappearance. International Journal of Space Structures, 30(1), 1–12. DOI: 10.1260/0266-3511.30.1.1.',
        'Ramm, E., & Mehlhorn, G. (1991). On shape finding methods and ultimate load analyses of reinforced concrete shells. Engineering Structures, 13(2), 178–198. DOI: 10.1016/0141-0296(91)90050-M.',
        'Pucher, A. (1934). Über den Spannungszustand in gekrümmten Flächen. Beton und Eisen, 33(19), 298–304.',
        'Heyman, J. (1995). The Stone Skeleton: Structural Engineering of Masonry Architecture. Cambridge University Press. DOI: 10.1017/CBO9781107050310.',
        'Maxwell, J. C. (1864). On reciprocal figures and diagrams of forces. Philosophical Magazine, 27(182), 250–261. DOI: 10.1080/14786446408643663.',
        'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: 10.1162/qss_a_00146.',
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Ruled Hyperbolic Paraboloid Umbrella Section and Principal Membrane Stress">\n'
        '            <line x1="35" y1="186" x2="645" y2="186" stroke="currentColor" stroke-opacity="0.3"/>\n'
        '            <text x="44" y="24" font-size="10.5" font-weight="600" fill="currentColor">4-Quadrant Hypar Umbrella (Straight Rulings &amp; Stem Drain)</text>\n'
        '            <polygon id="tp-a14-umbrella-l" points="87,85 198,130 198,144 87,97" fill="var(--tp-prussian)" fill-opacity="0.18" stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '            <polygon id="tp-a14-umbrella-r" points="198,130 309,85 309,97 198,144" fill="var(--tp-verdigris)" fill-opacity="0.18" stroke="var(--tp-verdigris)" stroke-width="2"/>\n'
        '            <line id="tp-a14-rule-1" x1="109" y1="94" x2="198" y2="132" stroke="var(--tp-prussian)" stroke-width="1" stroke-dasharray="3,2"/>\n'
        '            <line id="tp-a14-rule-2" x1="287" y1="94" x2="198" y2="132" stroke="var(--tp-verdigris)" stroke-width="1" stroke-dasharray="3,2"/>\n'
        '            <rect x="191" y="138" width="14" height="48" fill="var(--tp-stone)" fill-opacity="0.5" stroke="currentColor" stroke-width="1.5"/>\n'
        '            <path id="tp-a14-rain" d="M 115 81 L 184 116" stroke="var(--tp-minium)" stroke-width="1.8" stroke-dasharray="4,3"/>\n'
        '            <text id="tp-a14-span-lbl" x="198" y="176" text-anchor="middle" font-size="9" fill="currentColor">2a = 24.0 m · h = 4.0 m · Q = 8.0 L/s</text>\n'
        '            <line x1="376" y1="24" x2="376" y2="192" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="394" y="24" font-size="10.5" font-weight="600" fill="currentColor">Pucher Principal Stress &amp; Shear Response</text>\n'
        '            <rect id="tp-a14-sig1-bar" x="412" y="91" width="52" height="9" rx="2" fill="var(--tp-minium)" fill-opacity="0.35" stroke="var(--tp-minium)" stroke-width="1.6"/>\n'
        '            <rect id="tp-a14-sig2-bar" x="494" y="100" width="52" height="9" rx="2" fill="var(--tp-prussian)" fill-opacity="0.32" stroke="var(--tp-prussian)" stroke-width="1.6"/>\n'
        '            <line x1="398" y1="100" x2="562" y2="100" stroke="currentColor" stroke-opacity="0.45" stroke-dasharray="3,2"/>\n'
        '            <circle id="tp-a14-nxy-dot" cx="604" cy="145" r="6" fill="var(--tp-verdigris)" stroke="currentColor" stroke-width="1.2"/>\n'
        '            <text id="tp-a14-sig1-lbl" x="438" y="83" text-anchor="middle" font-size="9" fill="var(--tp-minium)">+0.784 MPa</text>\n'
        '            <text id="tp-a14-sig2-lbl" x="520" y="123" text-anchor="middle" font-size="9" fill="var(--tp-prussian)">-0.784 MPa</text>\n'
        '            <text id="tp-a14-nxy-lbl" x="604" y="131" text-anchor="middle" font-size="9" fill="var(--tp-verdigris)">31.35 kN/m</text>\n'
        '            <text x="438" y="180" text-anchor="middle" font-size="8.5" fill="currentColor">σ_1 (Tie)</text>\n'
        '            <text x="520" y="180" text-anchor="middle" font-size="8.5" fill="currentColor">σ_2 (Arch)</text>\n'
        '            <text x="604" y="180" text-anchor="middle" font-size="8.5" fill="currentColor">N_xy</text>\n'
        '            <text x="44" y="206" font-size="10" fill="var(--tp-verdigris)">Idealized Pucher Membrane Model · Not a Structural Code Check</text>\n'
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Studio architectural photograph on a honed warm limestone workbench showing a matte pale-gray cast-concrete 4-quadrant '
        'inverted hyperbolic paraboloid umbrella scale model over a carved stone catch-basin on the right, beside an uncast '
        'straight-slat basswood saddle formwork cradle and ungraduated solid brass dividers on the left '
        '(physical studio scale-model study, not a full-scale measured building)'
    ),
    'caption': (
        'Studio Model Plate A.14-V · Physical scale-model study showing how unbent straight basswood slats assemble a doubly curved '
        'hyperbolic paraboloid saddle cradle (left) alongside a thin 4-quadrant inverted concrete umbrella draining to a central '
        'stem (right). Artistic studio model study; the numerical readouts on this page represent an idealized Pucher membrane model.'
    ),
}

DISPATCH = {
    'kicker': 'MEMBRANE SHELL DISPATCH · CANDELA 1960 & MULTI-SIDED UMBRELLA STUDIES (WANG ET AL. 2020, 2022)',
    'headline': 'Straight-Board Rulings, Pucher Shear Flow, and the Edge Boundaries of Thin Hypar Umbrellas',
    'body': (
        'Pairing Félix Candela\'s 1960 ACI shell formulations (DOI 10.14359/8024, 10.14359/8026) with contemporary structural '
        'evaluations of 8-sided and hexagonal umbrellas (Wang et al. 2020, DOI 10.1016/j.engstruct.2020.111156; 2022, DOI '
        '10.1016/j.engstruct.2022.114577), this folio inspects a 40 mm hypar quadrant (a = b = 12.0 m, h = 4.0 m) where model shear '
        'is 31.35 kN/m (σ_2 = -0.784 MPa, λ_comp = 20.1). Model values only, not field measurements.'
    ),
}

META_3D = (
    'Candela Hyperbolic Paraboloid Saddle Surface & Pucher Membrane Shear',
    'X: Quadrant Semi-Span a = b · Z: Corner Rise h · Y: Principal Membrane Stress & N_xy',
)

ES_TRANSLATION = {
    'title_es': (
        'Cascarones Reglados de Félix Candela: Cortante de Membrana de Pucher y Cimbra de Duelas Rectas'
    ),
    'subtitle_es': (
        'Continuando las superficies funiculares de A.01 y las cáscaras de A.13: estudio de diseño estructural sobre cómo el '
        'paraboloide hiperbólico permite colar paraguas de concreto de 40 mm (semiclaro 12.0 m, flecha 4.0 m) sobre tablas rectas, '
        'acoplando el modelo plano de Pucher (N_xy = 31.35 kN/m, σ_2 = -0.784 MPa) con sus límites de borde libre y pandeo.'
    ),
    'why_es': (
        'Un paraboloide hiperbólico luce doblemente curvado como silla de montar, pero está tejido por dos familias de rectas: '
        'tablas de madera sin doblar forman un techo delgado que canaliza el peso por cortante puro y la lluvia por el fuste central.'
    ),
    'bridge_es': (
        'Continúa A.01 y A.13: equilibrio idealizado de membrana de Pucher frente a flexión de borde libre y nervaduras reales.'
    ),
    'plain_es': (
        'Imaginen torcer un marco cuadrado levantando dos esquinas opuestas y bajando las otras dos. Aunque la superficie se curva '
        'como una silla de montar, si apoyan lápices rectos de un borde al opuesto, cada lápiz toca toda la superficie sin doblarse. '
        'Ese principio geométrico permitió que las cuadrillas de Félix Candela en México armaran cimbras con tablas comunes de pino '
        'rectas para colar cascarones de concreto de apenas 40 mm de espesor. Al reunir cuatro cuadrantes en un paraguas invertido '
        'sobre una sola columna hueca, el agua de lluvia escurre por gravedad hacia el bajante central.'
    ),
    'deep_es': (
        'En el plano analítico, este folio evalúa un cuadrante de paraboloide hiperbólico z(x, y) = (h / (a b)) x y con a = b = 12.0 m, '
        'flecha de esquina h = 4.0 m (parámetro de alabeo c = 36.0 m) y espesor de campo t = 40.0 mm. Bajo carga proyectada uniforme '
        'q_0 = 1.741 kN/m² (peso propio de 0.941 kN/m² más 0.80 kN/m² de sobrecarga, omitiendo el factor de pendiente hacia las esquinas), '
        'las derivadas segundas ∂²z/∂x² y ∂²z/∂y² se anulan y la ecuación proyectada de Pucher (1934) arroja cortante uniforme '
        'N_xy = 31.35 kN/m con N_x = N_y = M_x = M_y = 0 en el interior idealizado. A 45 grados surgen esfuerzos principales '
        'σ_1 = +0.784 MPa (tracción) y σ_2 = -0.784 MPa (compresión), con razón de margen λ_comp = 20.1 respecto a 0.45 f_ck (f_ck = 35 MPa), '
        'un ahorro de 80.0% en el espesor del campo frente a una losa maciza de 200 mm y una captación pluvial de 8.0 L/s (28.8 m³/h) '
        'sobre 576 m² a 50 mm/h. Hipótesis (modelo de nivel T2): la curvatura reglada sostiene carga simétrica en régimen de cortante '
        'con compresión reducida; el modelo se refuta en paraguas reales en voladizo si la flexión de borde libre, las nervaduras en '
        'los valles, la fluencia lenta o el pandeo delgado (Ramm y Mehlhorn, 1991; Wang et al., 2020, 2022) dominan la respuesta.'
    ),
}
