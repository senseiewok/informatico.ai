#!/usr/bin/env python3
"""Folio E.05 (ENGINEERING): Terzaghi Soil Mechanics, CFA Augercast Deep Foundation Piling & Excess Pore Pressure."""
from __future__ import annotations

SLUG = 'e05'

PILLAR = 'engineering'

_SCITE_RECORD = {
    'doi': '10.1061/(ASCE)GT.1943-5606.0000073',
    'fetched_on': '2026-11-08',
    'citing_publications': 39,
    'supporting': 0,
    'mentioning': 3,
    'contrasting': 0,
    'retracted': False,
    'summary': (
        'Scite index entry [observed: Scite ML citation classification, accessed 2026-11-08] for '
        'Gavin, Cadogan & Casey (2009), Shaft Capacity of Continuous Flight Auger Piles in Sand '
        '(DOI 10.1061/(ASCE)GT.1943-5606.0000073). It records 39 citing publications (distinct '
        'from statement tallies: 0 supporting, 3 mentioning, 0 contrasting) and no retraction '
        "notice. That paper reports sand tests, not this folio's assumed clay factors."
    ),
}

FOLIO = {
    'folio_id': 'E.05',
    'slug': 'e05',
    'pillar': 'engineering',
    'category_code': 'E',
    'title': 'Terzaghi Soil Mechanics, CFA Augercast Deep Foundation Piling & Excess Pore Pressure',
    'subtitle': (
        "An explanatory geotechnical model of Karl Terzaghi's effective stress, consolidation, "
        'and continuous flight auger piles under assumed parameters. It is not a foundation or '
        'structural design method, and no number here belongs on a real structure.'
    ),
    'date_published': '2026-11-01',
    'date_redated': '2026-11-14',
    'current_edition': 'REV 1.2',
    'status_badge': 'CIVIL & GEOTECHNICAL · REV 1.2',
    'primary_kernel': 'tools/folios/engineering/e05.py',
    'kernel_verdict': 'Not independently verified',
    'kernel_verdict_es': 'Sin verificación independiente',
    'governing_law': "∂u/∂t = c_v ∂²u/∂z² · Q_ult = Q_skin + Q_toe · r_u = Δu / σ'_{v0}",
    'colophon': {
        'identifier': 'E.05 · Geotechnical & Deep Foundations · Teaching Model',
        'kernels': "σ'_v = σ_v − u · ∂u/∂t = c_v ∂²u/∂z² · Assumed CFA Model",
        'benchmarks': 'Assumed defaults: T_v = 0.320 · U_avg = 63.2% · Q_ult = 3,865 kN',
        'bridge': 'Terzaghi Consolidation (Explanatory Model)',
    },
    'sliders': [
        {
            'label': 'Foundation Surcharge Load (kPa)',
            'min': 40.0,
            'max': 260.0,
            'step': 5.0,
            'value': 120.0,
            'unit': ' kPa',
        },
        {
            'label': 'Consolidation Coefficient (m²/yr)',
            'min': 0.5,
            'max': 8.0,
            'step': 0.1,
            'value': 3.2,
            'unit': ' m²/yr',
        },
    ],
    'steps': [
        (
            'Stage 1 (Undrained Surcharge Application, t = 0⁺): Assumed surcharge Δq = 120 kPa '
            'transfers initially into excess pore pressure Δu(z, 0) = Δq in saturated clay '
            '(Terzaghi 1925).'
        ),
        (
            'Stage 2 (Terzaghi Hydrodynamic Dissipation): With assumed H_dr = 6 m and t = 3.6 yr '
            'at c_v = 3.2 m²/yr, T_v = 0.320 gives U_avg = 63.2% and assumed settlement '
            'S_c = (Δq / 120) × 66.7 × U_avg = 42.2 mm.'
        ),
        (
            'Stage 3 (Assumed CFA Shaft + Toe Model): Illustrative 750 mm by 24 m CFA capacities '
            'follow Q_ult = 2,380 × (1 − 0.65 r_u) + 1,980 × (1 − 0.35 r_u) = 3,865 kN at '
            'unrounded r_u = 0.2208 against assumed P_design = 1,400 + 1.25 Δq = 1,550 kN '
            '(FS = 2.49; untested assumptions, not a design method).'
        ),
        (
            'Stage 4 (Consolidation Pore-Pressure Ratio): Residual Δu = Δq (1 − U_avg) = 44.2 kPa '
            "over assumed σ'_{v0} = 200 kPa gives r_u = 0.22 (σ'_v = 156 kPa), distinct from "
            'seismic liquefaction (Seed & Idriss 1971, DOI 10.1061/JSFEAQ.0001662); r_u ≥ 0.70 or '
            'FS < 2.0 is an illustrative alert.'
        ),
    ],
    'readouts': [
        {'label': 'Average Consolidation U_avg (Model)', 'value': '63.2% (S_c = 42.2 mm, model)'},
        {'label': 'CFA Pile Capacity (Illustrative)', 'value': '3,865 kN (FS = 2.49, model)'},
        {'label': 'Consolidation Ratio r_u (Assumed)', 'value': "0.22 (σ'_v = 156 kPa)"},
        {'label': 'Illustrative Model Check', 'value': 'MODEL FS ≥ 2.0 · ILLUSTRATIVE, NOT A SITE DESIGN'},
    ],
    'spec_plate': {
        'division': 'CONCEPT NOTE · CSI 31 63 23 FILING LABEL / FHWA GEC-8 (NOT A SPEC)',
        'title': 'Continuous Flight Auger (CFA) Deep Foundation Concept Note',
        'body': (
            'Untested explanatory note, not a specification or design method: illustrative CFA '
            "piles (D = 750 mm, L = 24 m, assumed f'_c = 40 MPa grout) monitored for depth, "
            'torque, and grout volume (Brown et al. 2007, FHWA GEC No. 8; CSI 31 63 23 is a '
            'filing label only). No number here belongs on a real foundation.'
        ),
        'meta': (
            'Explanatory note · FHWA GEC No. 8 provides agency guidance for CFA piles; '
            'no site data stand behind this folio'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE E.05-A · TERZAGHI EFFECTIVE STRESS & TIME FACTOR T_v',
        'body': (
            'Under Terzaghi (1925), T_v = c_v t / H_dr² governs 1D consolidation; double drainage '
            '(H_dr = H/2) divides consolidation time by four for uniform clay.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE E.05-B · CONCEPT NOTE · CSI 31 63 23 LABEL (NOT A SPEC)',
        'body': (
            'Untested note, not a specification: illustrative CFA geometry (D = 750 mm, L = 24 m) '
            'and rig logs (Brown et al. 2007); no number belongs on real work.'
        ),
    },
    'skill': {
        'filename': 'terzaghi-cfa-geotechnical-piling-SKILL.md',
        'name': 'terzaghi-cfa-geotechnical-piling',
        'description': (
            'Explanatory geotechnical reference (not a foundation or structural design method) '
            'for Terzaghi 1D consolidation, effective stress, and an illustrative continuous '
            'flight auger pile algebraic model; no number here may be used on a real structure.'
        ),
        'rules': [
            (
                'Explanatory model only, not a geotechnical or structural design method (no '
                'number here may be used on a real structure): with assumed H_dr = 6 m and '
                't = 3.6 yr, compute T_v = c_v * t / H_dr^2, piecewise U_avg(T_v), and assumed '
                'S_c = (Delta_q / 120) * 66.7 * U_avg.'
            ),
            (
                'Evaluate illustrative Q_ult = max(650, 2,380 * (1 - 0.65 * r_u) + 1,980 * '
                '(1 - 0.35 * r_u)) against assumed P_design = 1,400 + 1.25 * Delta_q using '
                'r_u = min(0.98, Delta_q * (1 - U_avg) / 200) (untested assumptions, not code '
                'values).'
            ),
            (
                'Treat r_u >= 0.70 or FS = Q_ult / P_design < 2.0 as an illustrative alert, not '
                'a code check; cyclic liquefaction (Seed & Idriss 1971, DOI '
                '10.1061/JSFEAQ.0001662) requires site testing.'
            ),
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.2',
            'date': '2026-11-14',
            'summary': (
                'REV 1.2 (Redated 2026-11-14): Grounding revision. Corrected DOI '
                '10.1061/(ASCE)GT.1943-5606.0000073 to Gavin, Cadogan & Casey (2009), recomputed '
                'closed-form readouts (U_avg = 63.2%, S_c = 42.2 mm, Q_ult = 3,865 kN, r_u = '
                '0.22), removed unsourced claims, aligned Experiment 2 and SVG curves with '
                'solvers.mjs, and set the non-design-method boundary.'
            ),
            'opus': (
                'Review: references checked in Crossref and Scite; no finite-element model or '
                'site data stand behind this folio.'
            ),
        },
        {
            'edition': 'REV 1.1',
            'date': '2026-11-02',
            'summary': (
                'REV 1.1 (Redated 2026-11-02): Revised Terzaghi effective stress, 1D '
                'consolidation, and CFA shaft + toe bearing discussion.'
            ),
            'opus': (
                'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B); earlier "Verified" wording '
                'and mismatched readouts (64.2%, 4,180 kN, r_u = 0.28) withdrawn in REV 1.2.'
            ),
        },
        {
            'edition': 'REV 1.0',
            'date': '2026-11-01',
            'summary': (
                'REV 1.0 (Published 2026-11-01): Initial 5-Act geotechnical monograph on Terzaghi '
                'consolidation and CFA deep piling.'
            ),
            'opus': (
                'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B); earlier "Verified" wording '
                'withdrawn in REV 1.2.'
            ),
        },
    ],
    'volume': 3,
    'volume_code': 'VOL. 03',
    'reading_time': '20 MIN READ',
    'word_count': '~4,450 WORDS',
    'scite': _SCITE_RECORD,
}

LONGFORM_DATA = {
    'reading_time': '20 MIN READ',
    'word_count': '~4,450 WORDS',
    'scite': _SCITE_RECORD,
    'act1_title': (
        "Act I — Karl Terzaghi's Effective Stress Principle and Continuous Flight Auger "
        '(CFA) Deep Piling'
    ),
    'act1_dropcap': (
        'In 1925 in Vienna, the Austrian civil engineer Karl Terzaghi published Erdbaumechanik, '
        'setting out a two-phase physical description of waterlogged ground. Builders had long '
        'watched heavy masonry structures on soft clay settle unevenly for years. Terzaghi '
        'separated saturated soil into solid mineral grains and pore water. Water barely '
        'compresses under ordinary building loads, whereas wet clay pores drain slowly. Under '
        'his principle of effective stress, the mineral skeleton carries only total overburden '
        'pressure minus water pressure inside the pores. Under one-dimensional consolidation, a '
        'sudden building load first pressurizes trapped water and shifts to the grains only as '
        'water drains. Decades later, foundation crews began drilling hollow-stem augers through '
        'compressible clay into firmer strata and pumping cement grout as the auger withdrew. '
        'Everything here is an explanatory model, not a geotechnical or structural design method, '
        'and no figure on this page belongs on a real structure.'
    ),
    'act1_plain_bridge': (
        'Imagine setting a heavy stone block onto soft river mud whose tiny spaces are brimming '
        'with groundwater. Water cannot compress out of the way in an instant. At first, trapped '
        'groundwater carries the added weight while microscopic clay passages slow its escape '
        'toward sandy layers. Over months or years, water seeps out and solid grains press closer '
        'together, lowering the ground surface. Earthquake shaking in loose wet sand is a '
        'separate hazard in which rapid vibration raises water pressure between grains. Where '
        'soft clay is thick, Continuous Flight Auger (CFA) piles bore down to denser layers and '
        'fill the shaft with pumped cement grout. Deep piles and vertical drains remain '
        'site-dependent tools rather than guarantees against settlement or earthquakes. This page '
        'offers a simplified classroom explanation rather than a foundation design method, so '
        'none of its numbers may be used on real work.'
    ),
    'act1_body': (
        "Under Terzaghi's consolidation theory, an undrained surcharge on saturated, "
        'low-permeability clay transfers first into excess pore-water pressure before diffusing '
        'toward permeable boundaries (Terzaghi 1925). Primary consolidation settlement develops '
        'as drainage transfers vertical stress onto the mineral skeleton (Terzaghi, Peck & Mesri '
        '1996). Where compressible clay overlies denser strata, Continuous Flight Auger (CFA) '
        'rigs drill a hollow-stem auger to depth and pump cement grout during withdrawal '
        '(Brown et al. 2007). Instrumented load tests in sand document how shaft resistance '
        'develops along augercast piles (Gavin, Cadogan & Casey 2009, DOI '
        '10.1061/(ASCE)GT.1943-5606.0000073). Citation tallies for cited papers were checked in '
        'Scite (Nicholson et al. 2021, DOI 10.1162/qss_a_00146). Prefabricated vertical drains '
        'can shorten clay drainage paths where site testing supports them, yet this untested '
        'folio is an explanation, not a foundation design method.'
    ),
    'act1_stakes': (
        'Ignoring slow pore-water drainage on compressible clay leads to long-term consolidation '
        'settlement (Terzaghi, Peck & Mesri 1996). Differential settlement and angular distortion '
        'can crack walls and frames (Boscardin & Cording 1989, DOI '
        '10.1061/(ASCE)0733-9410(1989)115:1(1)). Cyclic earthquake shearing in loose wet sand '
        'raises pore pressure through a separate mechanism needing site-specific liquefaction '
        'analysis (Seed & Idriss 1971, DOI 10.1061/JSFEAQ.0001662). Steady surcharge '
        'consolidation on this page does not model seismic liquefaction. In practice, engineers '
        'combine borings, lab testing, ground improvement, and piles checked for downdrag and '
        'lost lateral support; deep piles are one option, not a guarantee.'
    ),
    'pullquote': (
        "In Karl Terzaghi's two-phase soil model (Terzaghi 1925), mineral grains carry only the "
        'effective stress remaining after pore-water pressure is subtracted from total overburden '
        'stress.'
    ),
    'chronology': [
        (
            '1925',
            'Karl Terzaghi publishes Erdbaumechanik in Vienna, formulating the principle of '
            'effective stress and one-dimensional consolidation.',
        ),
        (
            '1941–1948',
            'Maurice Biot generalizes three-dimensional poroelastic consolidation (DOI '
            '10.1063/1.1712886), and Terzaghi & Ralph Peck publish Soil Mechanics in Engineering '
            'Practice.',
        ),
        (
            '1971',
            'H. Bolton Seed & I. M. Idriss publish a simplified cyclic procedure for evaluating '
            'earthquake soil liquefaction potential (DOI 10.1061/JSFEAQ.0001662).',
        ),
        (
            '2007–2009',
            'FHWA Circular No. 8 (Brown et al. 2007) documents CFA pile practice, and Gavin, '
            'Cadogan & Casey (2009, DOI 10.1061/(ASCE)GT.1943-5606.0000073) report sand shaft '
            'load tests.',
        ),
    ],
    'act2_title': (
        'Act II — How It Works: Pore-Water Isochrones, CFA Pile Bearing & Excess Pore-Pressure '
        'Ratio'
    ),
    'act2_analogy': (
        'Pressing a hand onto a soaked kitchen sponge first squeezes trapped water inside its '
        'pores; the foam skeleton compresses as water escapes. Terzaghi consolidation describes '
        'that gradual transfer of load from pore water to grains. The excess pore-pressure ratio '
        'on this page tracks what fraction of the assumed initial effective overburden pressure '
        'remains in water. Where the comparison stops: sponge foam rebounds elastically in '
        'seconds, whereas clay platelets rearrange plastically over years and a bored grout pile '
        'carries load into deeper strata.'
    ),
    'act2_plain_primer': (
        'Two sliders drive the closed-form algebraic model in Act III under fixed illustrative '
        'soil and pile assumptions. Foundation Surcharge Load sets the assumed uniform surface '
        'pressure from 40 to 260 kilopascals, raising both model settlement and residual water '
        'pressure. Consolidation Coefficient sets the assumed pore-water diffusion rate from 0.5 '
        'to 8.0 square meters per year across a fixed six-meter drainage path. Higher diffusion '
        'values drain excess water sooner at the fixed 3.6-year snapshot. Lower diffusion values '
        "combined with heavy surcharge leave higher residual water pressure, triggering the page's "
        'illustrative factor-of-safety alert.'
    ),
    'distill_diagram': {
        'analogy_title': 'Soaked Sponge & Pore Drainage',
        'analogy_sub': 'Trapped pore water carries load until slow drainage compresses skeleton.',
        'force_a_title': 'Foundation Surcharge (Δq)',
        'force_a_sub': 'Assumed surface pressure raising initial excess pore-water pressure.',
        'force_b_title': 'Consolidation Rate (c_v)',
        'force_b_sub': 'Assumed diffusion rate draining pore water toward sand boundaries.',
        'threshold_title': 'Illustrative Alert (r_u ≥ 0.70 or FS < 2.0)',
        'threshold_pass': 'Model FS ≥ 2.0 and r_u < 0.70 under assumed reference constants.',
        'threshold_fail': 'Model FS < 2.0 or r_u ≥ 0.70 (illustrative alert, not a site check).',
    },
    'act2_intuition': (
        'With assumed H_dr = 6.0 m and t = 3.6 yr, the time factor T_v = c_v t / H_dr² governs '
        'average consolidation (Terzaghi 1925). The browser model uses U_avg = sqrt(4 T_v / pi) '
        'for T_v <= 0.286 and U_avg = 1 − (8 / pi²) exp(−pi² T_v / 4) above 0.286, clamped to '
        '[0.05, 0.995]. At defaults Delta_q = 120 kPa and c_v = 3.2 m²/yr, T_v = 0.320 gives '
        'U_avg = 63.2%. Assumed settlement follows S_c = (Delta_q / 120) × 66.7 × U_avg = '
        '42.2 mm. Residual pressure Delta_u = Delta_q (1 − U_avg) = 44.2 kPa over assumed '
        "sigma'_v0 = 200 kPa yields r_u = 0.22 and sigma'_v = 156 kPa. The illustrative CFA "
        'formula scales 2,380 kN shaft and 1,980 kN toe terms to Q_ult = 3,865 kN against '
        'P_design = 1,550 kN (FS = 2.49). Readers could explore Biot poroelasticity (Biot 1941, '
        'DOI 10.1063/1.1712886) in FEniCS/dolfinx (https://github.com/FEniCS/dolfinx; Scroggs '
        'et al. 2022, DOI 10.1145/3524456); none was run here.'
    ),
    'act2_deepening': (
        "Terzaghi's linear diffusion equation treats the consolidation coefficient c_v as "
        'constant, whereas real soft clays lose void space and permeability as compression '
        'proceeds (Terzaghi, Peck & Mesri 1996). Variable compressibility and radial drainage '
        'around piles alter settlement rates in layered ground. Along real bored and augercast '
        'piles, shaft friction mobilizes at small relative slip whereas full base resistance '
        'requires larger downward movement (Brown et al. 2007; Gavin, Cadogan & Casey 2009, DOI '
        "10.1061/(ASCE)GT.1943-5606.0000073). This folio's algebraic formula omits slip "
        'compatibility, layered soils, negative skin friction, and cyclic earthquake '
        'pore-pressure generation (Seed & Idriss 1971, DOI 10.1061/JSFEAQ.0001662).'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Surcharge Sweep at Default Drainage): Hold Consolidation Coefficient '
            'at 3.2 m²/yr and raise Foundation Surcharge from 60 kPa to 220 kPa. Assumed S_c '
            'climbs from 21.1 mm to 77.3 mm while r_u rises from 0.11 to 0.40. Illustrative '
            'Q_ult drops from 4,113 kN (FS = 2.79) to 3,453 kN (FS = 2.06) as the isochrone '
            'bulge moves from x = 406 to x = 530.'
        ),
        (
            'Experiment 2 (Low Drainage & Illustrative Alert Threshold): Set Consolidation '
            'Coefficient to 0.8 m²/yr at 120 kPa to read T_v = 0.080, U_avg = 31.9%, r_u = 0.41, '
            'and FS = 2.22. Raise Foundation Surcharge to 220 kPa at 0.8 m²/yr so r_u hits 0.75 '
            'and Q_ult falls to 2,682 kN (FS = 1.60), triggering the illustrative alert.'
        ),
        (
            'Experiment 3 (Four-Stage Stepper & Companion Caveat Sheet): Click Stages 1 through '
            '4 above to inspect each assumed equation. Read terzaghi-cfa-geotechnical-piling '
            'SKILL.md below as an explanatory caveat sheet, not a foundation design method.'
        ),
    ],
    'act4_title': (
        'Act IV — Rig Drilling Telemetry & the Geotechnical Concept Note Bridge'
    ),
    'act4_human_ai': (
        'Automated monitoring systems on CFA rigs can record auger depth, torque, rotation rate, '
        'and pumped grout volume during installation (Brown et al. 2007). As an untested '
        'proposal, engineers might pair those installation logs with piezometer settlement '
        'records. Readers could prototype poroelastic finite-element models in FEniCS/dolfinx '
        '(Scroggs et al. 2022, DOI 10.1145/3524456) or data-driven system identification with '
        'dynamicslab/pysindy (Brunton, Proctor & Kutz 2016, DOI 10.1073/pnas.1517384113). '
        'Neither tool was run for this folio, citation counts come from Scite (DOI '
        '10.1162/qss_a_00146), and no software replaces licensed site engineering.'
    ),
    'act4_deepening': (
        'Offered strictly as an unverified research direction, statistical models trained on rig '
        'telemetry and cone-penetration borings might help flag anomalous grout-volume drops or '
        'soft lenses for inspection. Field load testing, core sampling, and licensed engineering '
        'review would remain mandatory under applicable codes. Coupling three-dimensional '
        'consolidation (Biot 1941, DOI 10.1063/1.1712886) with field CFA measurements (Gavin, '
        'Cadogan & Casey 2009, DOI 10.1061/(ASCE)GT.1943-5606.0000073) remains an open modeling '
        'problem, not a design substitute.'
    ),
    'sources': [
        'Terzaghi, K. (1925). Erdbaumechanik auf bodenphysikalischer Grundlage. Franz Deuticke, '
        'Vienna.',
        'Biot, M. A. (1941). General Theory of Three-Dimensional Consolidation. Journal of '
        'Applied Physics, 12(2), 155–164. DOI: 10.1063/1.1712886.',
        'Terzaghi, K., Peck, R. B., & Mesri, G. (1996; 1st ed. Terzaghi & Peck, 1948). Soil '
        'Mechanics in Engineering Practice (3rd ed.). Wiley.',
        'Seed, H. B., & Idriss, I. M. (1971). Simplified Procedure for Evaluating Soil '
        'Liquefaction Potential. Journal of the Soil Mechanics and Foundations Division, ASCE, '
        '97(9), 1249–1273. DOI: 10.1061/JSFEAQ.0001662.',
        'Boscardin, M. D., & Cording, E. J. (1989). Building Response to Excavation-Induced '
        'Settlement. Journal of Geotechnical Engineering, 115(1), 1–21. DOI: '
        '10.1061/(ASCE)0733-9410(1989)115:1(1).',
        'Brown, D. A., Dapp, S. D., Thompson, W. R., & Lazarte, C. A. (2007). Design and '
        'Construction of Continuous Flight Auger (CFA) Piles (FHWA GEC No. 8, FHWA-HIF-07-039). '
        'Federal Highway Administration.',
        'Gavin, K. G., Cadogan, D., & Casey, P. (2009). Shaft Capacity of Continuous Flight '
        'Auger Piles in Sand. Journal of Geotechnical and Geoenvironmental Engineering, 135(6), '
        '790–798. DOI: 10.1061/(ASCE)GT.1943-5606.0000073.',
        'Construction Specifications Institute (CSI). MasterFormat Section 31 63 23: Bored Piles '
        '(industry filing label only; this folio is not a project specification).',
        'Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing equations '
        'from data by sparse identification of nonlinear dynamical systems. Proceedings of the '
        'National Academy of Sciences, 113(15), 3932–3937. DOI: 10.1073/pnas.1517384113. '
        '(Cited for the SINDy method; dynamicslab/pysindy, https://github.com/dynamicslab/pysindy, '
        'is a separate open-source Python package.)',
        'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction '
        'of Arbitrary Order Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral '
        'Cell Meshes (FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). ACM Transactions on '
        'Mathematical Software, 48(2), 18:1–18:23. DOI: 10.1145/3524456.',
        'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
        'context of citations and classifies their intent using deep learning (https://scite.ai). '
        'Quantitative Science Studies, 2(3), 882–898. DOI: 10.1162/qss_a_00146.',
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Terzaghi 1D '
        'consolidation pore-pressure isochrones and 24-meter CFA augercast deep foundation pile">\n'
        '            <rect x="45" y="30" width="250" height="55" fill="var(--tp-ochre)" '
        'fill-opacity="0.16" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <rect x="45" y="85" width="250" height="75" fill="var(--tp-prussian)" '
        'fill-opacity="0.14" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <rect x="45" y="160" width="250" height="35" fill="var(--tp-verdigris)" '
        'fill-opacity="0.22" stroke="currentColor" stroke-opacity="0.45"/>\n'
        '            <rect id="tp-e05-svg-pile" x="152" y="24" width="36" height="156" '
        'fill="var(--tp-graphite)" stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '            <text x="54" y="52" font-size="10" fill="currentColor">Assumed Upper Sand &amp; '
        'Fill (0–6 m)</text>\n'
        '            <text x="54" y="122" font-size="10" fill="currentColor">Assumed Compressible '
        'Clay (6–18 m)</text>\n'
        '            <text x="54" y="182" font-size="10" fill="var(--tp-verdigris)">Assumed Bearing '
        'Stratum (18–24 m · Q_toe)</text>\n'
        '            <text x="52" y="20" font-size="11" font-weight="600" '
        'fill="currentColor">Illustrative Profile &amp; CFA Pile (D = 750 mm)</text>\n'
        '            <line x1="360" y1="30" x2="360" y2="195" stroke="currentColor" '
        'stroke-opacity="0.45" stroke-width="1.8"/>\n'
        '            <line x1="360" y1="195" x2="635" y2="195" stroke="currentColor" '
        'stroke-opacity="0.45" stroke-width="1.8"/>\n'
        '            <path id="tp-e05-svg-isochrone" data-custom-curve="1" d="M 360 30 Q 453 112 360 195" '
        'fill="var(--tp-minium)" fill-opacity="0.16" stroke="var(--tp-minium)" '
        'stroke-width="2.8"/>\n'
        '            <path data-custom-curve="1" d="M 360 30 Q 445 112 360 195" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="2" stroke-dasharray="5,4"/>\n'
        '            <text x="365" y="20" font-size="11" font-weight="600" '
        'fill="currentColor">Terzaghi Excess Pore Pressure Isochrone Δu(z, t)</text>\n'
        '            <text id="tp-e05-svg-label" x="455" y="108" font-size="10.5" '
        'fill="var(--tp-minium)">U_avg = 63.2% · Q_ult = 3,865 kN</text>\n'
        '            <text x="415" y="212" font-size="10" fill="currentColor">Excess Pore Pressure '
        'Δu (kPa) · Drainage Boundaries z = 0, 2H_dr</text>\n'
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining what Continuous Flight Auger deep foundation piles '
        'and Terzaghi consolidation strata would look like in cutaway (artistic impression, not '
        'a measured structure)'
    ),
    'caption': (
        'Conceptual Vision Plate E.05-V (Imagining What It Would Look Like). Artistic cutaway '
        'imagining CFA piles in clay and sand (untested impression, not an engineered '
        'foundation).'
    ),
}

DISPATCH = {
    'kicker': 'GEOTECHNICAL TEACHING DISPATCH · TERZAGHI CONSOLIDATION & CFA RIG MONITORING',
    'headline': 'A Century After Erdbaumechanik: Effective Stress, Consolidation, and Monitored CFA Piles',
    'body': (
        "Connecting Terzaghi's 1925 effective stress model with FHWA GEC No. 8 rig monitoring "
        '(Brown et al. 2007) and sand shaft tests (Gavin, Cadogan & Casey 2009, DOI '
        '10.1061/(ASCE)GT.1943-5606.0000073). This untested explanation estimates U_avg = 63.2% '
        'and Q_ult = 3,865 kN under assumed inputs; no figure belongs on a real structure.'
    ),
}

META_3D = (
    'Terzaghi Consolidation Dish & 4-Pile Bearing Cones',
    'X/Z: Foundation Mat Footprint · Y: Effective Stress Consolidation & Assumed CFA Capacity',
)

ES_TRANSLATION = {
    'title_es': 'Mecánica de Suelos de Terzaghi, Pilotes Profundos CFA y Presión de Poro en Exceso',
    'subtitle_es': (
        'Modelo geotécnico explicativo, no un método de diseño estructural ni de cimentaciones: '
        'cómo el esfuerzo efectivo y la consolidación de Karl Terzaghi se combinan con pilotes '
        'de barrena continua bajo supuestos ilustrativos; ninguna cifra aquí puede usarse en una '
        'obra real.'
    ),
    'why_es': (
        'Al presionar una esponja empapada, primero sube la presión del agua atrapada en los '
        'poros y el esqueleto sólo se comprime conforme el agua escapa (consolidación de '
        'Terzaghi). Donde termina la comparación: la espuma recupera su forma en segundos, '
        'mientras la arcilla se deforma de manera plástica durante años y un pilote perforado '
        'transmite carga a estratos profundos.'
    ),
    'plain_es': (
        'En 1925 en Viena, Karl Terzaghi publicó Erdbaumechanik y trató el suelo saturado como '
        'granos minerales sólidos y agua en los poros. Bajo una sobrecarga sobre arcilla '
        'saturada, el agua casi incompresible recibe primero el peso porque los poros frenan su '
        'salida; conforme drena, los granos se reacomodan y producen asentamiento. El sismo en '
        'arena suelta saturada es otro fenómeno que exige evaluación cíclica en sitio (Seed e '
        'Idriss 1971, DOI 10.1061/JSFEAQ.0001662). Los pilotes de barrena continua (CFA) '
        'perforan hasta estratos densos e inyectan lechada de cemento (Brown et al. 2007). Esta '
        'página es una explicación conceptual, no un método de diseño geotécnico ni estructural, '
        'y ninguna cifra debe usarse en una obra real.'
    ),
    'deep_es': (
        'Con H_dr = 6.0 m y t = 3.6 años supuestos, T_v = c_v t / H_dr² (Terzaghi 1925) da en '
        '120 kPa y 3.2 m²/año T_v = 0.320, U_avg = 63.2%, S_c = 42.2 mm y r_u = 0.22 sobre '
        "sigma'_v0 = 200 kPa supuesto. El modelo CFA ilustrativo (0.75 m por 24 m) escala "
        '2,380 kN y 1,980 kN supuestos a Q_ult = 3,865 kN frente a P_design = 1,550 kN '
        '(FS = 2.49), con alerta ilustrativa si r_u >= 0.70 o FS < 2.0 (en 220 kPa y 0.8 m²/año, '
        'r_u = 0.75 y Q_ult = 2,682 kN, FS = 1.60). Los sistemas de monitoreo en equipos CFA '
        'pueden registrar profundidad, par y lechada bombeada (Brown et al. 2007; Gavin, Cadogan '
        'y Casey 2009, DOI 10.1061/(ASCE)GT.1943-5606.0000073); esto no es un método de diseño.'
    ),
}
