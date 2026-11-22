#!/usr/bin/env python3
"""Folio E.16 (ENGINEERING): Bridge Pier Local Scour, Shields Sediment Threshold & Flood-Duration Time-Scale Lag."""
from __future__ import annotations

SLUG = 'e16'

PILLAR = 'engineering'

_SCITE = {
    'doi': '10.1061/(ASCE)0733-9429(1999)125:1(59)',
    'fetched_on': '2026-11-21',
    'citing_publications': 851,
    'supporting': 26,
    'mentioning': 420,
    'contrasting': 0,
    'retracted': False,
    'summary': (
        'Scite Smart Citation Index entry for Melville & Chiew 1999, "Time Scale for Local Scour at Bridge Piers" '
        '(Journal of Hydraulic Engineering, DOI 10.1061/(ASCE)0733-9429(1999)125:1(59)), fetched 2026-11-21: '
        '851 citing records (26 supporting, 420 mentioning, 0 contrasting) and no retraction notice. '
        'These counts describe that foundational paper, not this folio.'
    ),
}

FOLIO = {
    'folio_id': 'E.16',
    'slug': 'e16',
    'pillar': 'engineering',
    'category_code': 'E',
    'parent_folios': ['E.05', 'E.07', 'E.14'],
    'lineage_mode': 'CONTINUATION · Continues E.05 Deep Piling, E.07 Bridge Dynamics & E.14 Rainfall Slope Mechanics',
    'title': 'Bridge Pier Local Scour, Shields Sediment Threshold & Flood-Duration Time-Scale Lag',
    'subtitle': (
        "Continuing Folio E.05's deep piling, E.07's bridge dynamics, and E.14's rainfall slope mechanics: an illustrative "
        'hydraulic-engineering study coupling Shields incipient sediment motion, Sheppard and Melville equilibrium '
        'horseshoe-vortex scour, Federal Highway Administration Froude envelopes, and Melville and Chiew flood-duration '
        'lag around circular river bridge piers.'
    ),
    'date_published': '2026-11-21',
    'date_redated': '2026-11-21',
    'current_edition': 'REV 1.0',
    'status_badge': 'HYDRAULIC SCOUR · REV 1.0',
    'primary_kernel': 'skills/engineering/e16/verify_e16_pier_scour_timescale.py',
    'governing_law': (
        'y_s,SM = 2.5 a* f_1 f_2 f_3 · y_s,CSU = 2.0 K_1 K_2 K_3 y_1 (a* / y_1)^0.65 Fr_1^0.43 · '
        'K_t(t_d) = exp(−0.03 |(V_c / V_1) ln((t_d / 24) / t_e)|^1.6) · y_s(t_d) = K_t(t_d) y_s,SM'
    ),
    'colophon': {
        'identifier': 'E.16 · Bridge Pier Scour & Flood Time-Scale Lag · REV 1.0',
        'kernels': 'Shields Threshold (1936) · Melville Pier Scour (1997) · Melville–Chiew Time Scale (1999) · Sheppard–Melville (2014)',
        'benchmarks': (
            'Model values (circular pier a* = 2.00 m, y_1 = 3.00 m, d_50 = 2.00 mm, V_1 / V_c = 0.85, t_d = 24.0 h): '
            'V_c = 0.860 m/s · y_s,SM,eq = 2.505 m · y_s,CSU,eq = 2.142 m · t_e = 42.09 days · K_t = 0.7254 · '
            'y_s(24 h) = 1.817 m (1.213 m at 2.0 h flash flood)'
        ),
        'bridge': 'Continues E.05/E.07/E.14',
    },
    'sliders': [
        {
            'label': 'Clear-Water Flow Intensity',
            'min': 0.45,
            'max': 1.00,
            'step': 0.05,
            'value': 0.85,
            'unit': 'V_1 / V_c = ',
        },
        {
            'label': 'Peak Flood Duration',
            'min': 2.0,
            'max': 240.0,
            'step': 2.0,
            'value': 24.0,
            'unit': ' h',
        },
    ],
    'steps': [
        (
            'Stage 1 (Shields Incipient Motion & Logarithmic Critical Velocity V_c): Forensic analysis of 503 United '
            'States bridge failures from 1989 to 2000 by Wardhana and Hadipriono (2003, DOI '
            '10.1061/(ASCE)0887-3828(2003)17:3(144)) attributed 266 collapses (52.88%) to hydraulic flood, scour, and '
            'debris forces. Under Shields incipient-motion mechanics (documented by Buffington 1999, DOI '
            '10.1061/(ASCE)0733-9429(1999)125:4(376)) and Melville (1997, DOI 10.1061/(ASCE)0733-9429(1997)123:2(125)), '
            'cohesionless quartz grains (specific gravity s = 2.65, d_50 = 2.00 mm, θ_c = 0.045) reach critical shear '
            'velocity u_*c = √(θ_c (s − 1) g d_50) = 0.03817 m/s and depth-averaged threshold velocity '
            'V_c = 5.75 u_*c log_10(5.53 y_1 / d_50) = 0.860 m/s at approach depth y_1 = 3.00 m.'
        ),
        (
            'Stage 2 (Sheppard–Melville Equilibrium Scour vs. Froude-Only HEC-18 CSU): Sheppard, Melville, and Demir '
            '(2014, DOI 10.1061/(ASCE)HY.1943-7900.0000800) evaluated 23 pier-scour formulas across 569 laboratory and '
            '928 field records (filtered to 441 laboratory and 791 field datasets), merging clear-water factors into '
            'y_s,SM = 2.5 a* f_1 f_2 f_3 with f_1 = tanh((y_1 / a*)^0.4), f_2 = max(0, 1 − 1.2 [ln(V_1 / V_c)]^2), and '
            'f_3 = (a* / d_50) / [0.4 (a* / d_50)^1.2 + 10.6 (a* / d_50)^(−0.13)]. For a* = 2.00 m (f_1 = 0.8262, '
            'f_3 = 0.6263), near-threshold flow V_1 / V_c = 0.45 gives y_s,SM,eq = 0.608 m versus Froude-based CSU '
            'y_s,CSU,eq = 1.629 m (2.682× higher because CSU omits V_c), whereas near the clear-water peak V_1 / V_c = '
            '0.85 gives y_s,SM,eq = 2.505 m versus y_s,CSU,eq = 2.142 m.'
        ),
        (
            'Stage 3 (Melville & Chiew Equilibrium Time Scale t_e and Transient Factor K_t): Melville and Chiew (1999, '
            'DOI 10.1061/(ASCE)0733-9429(1999)125:1(59)) showed that clear-water horseshoe-vortex scour approaches '
            'equilibrium over time scale t_e (days) = 30.89 (a* / V_1) (V_1 / V_c − 0.4) (y_1 / a*)^0.25 for y_1 / a* '
            '<= 6.0 (where empirical constant 30.89 = 2.669 × 10^6 / 86,400 days·s^(−1) converts dimensionless '
            't* = V_1 t_e,sec / a* with a* in m and V_1 in m/s), with temporal fraction K_t(t_d) = exp(−0.03 |(V_c / V_1) '
            'ln((t_d / 24) / t_e)|^1.6) for t_d / 24 < t_e (clamped to 1.0 once t_d / 24 >= t_e). At V_1 / V_c = 0.85 '
            '(V_1 = 0.731 m/s), t_e = 42.09 days (1,010.1 h): a 2.0 h flash flood reaches K_t = 0.4841 (y_s = 1.213 m), '
            'and a 24.0 h storm reaches K_t = 0.7254 (y_s = 1.817 m).'
        ),
        (
            'Stage 4 (Open Hypothesis, Tier T1–T2, and Falsification Conditions): Hypothesis (Tier T1–T2): in uniform '
            'cohesionless sand or fine gravel around an unskewed circular pier under single-peak clear-water flow '
            '(0.45 <= V_1 / V_c <= 1.00), transient scour depth follows y_s(t_d) = K_t(t_d) y_s,SM,eq, excavating '
            'roughly half of equilibrium depth within two hours yet remaining below steady-state equilibrium across '
            '24-hour floods (1.817 m vs. 2.505 m S/M and 2.142 m CSU). This hypothesis is falsified under live-bed '
            'sediment transport (V_1 / V_c > 1.0), in graded armored riverbeds where horseshoe vortices breach surface '
            'armor into finer sub-layers ("armor-break" scour, Kabiri-Samani, Fathi & Farooq 2026, DOI '
            '10.2478/johh-2026-0004), across multi-flood deposition-erosion sequences (Link et al. 2020, DOI '
            '10.1061/(ASCE)HY.1943-7900.0001696), or when woody debris rafts widen the effective pier obstruction.'
        ),
    ],
    'readouts': [
        {'label': 'Transient & S/M Eq. Scour', 'value': 'y_s(t_d) = 1.817 m · y_s,SM = 2.505 m (model)'},
        {'label': 'HEC-18 CSU & Time Factor', 'value': 'y_s,CSU = 2.142 m · K_t = 0.7254 (model)'},
        {'label': 'Threshold V_c & Eq. Time t_e', 'value': 'V_c = 0.860 m/s · t_e = 42.09 d (model)'},
        {'label': 'Clear-Water Scour Regime', 'value': 'TRANSIENT HYDROGRAPH LAG (0.65 <= K_t < 0.90, model)'},
    ],
    'spec_plate': {
        'division': 'HYDRAULIC SCOUR / FHWA HEC-18 SCREENING (FILING LABEL · DESIGN STUDY)',
        'title': 'Circular Bridge Pier Clear-Water Horseshoe-Vortex Scour & Flood Time-Scale Screening Envelope',
        'body': (
            'Illustrative closed-form hydraulic screening study, not a bridge foundation design check (AASHTO LRFD / '
            'FHWA HEC-18) or site geotechnical evaluation: models a single unskewed circular concrete pier (a* = 2.00 m, '
            'K_1 = 1.0, K_2 = 1.0, K_3 = 1.1) in approach depth y_1 = 3.00 m over uniform cohesionless quartz sand-gravel '
            '(d_50 = 2.00 mm, s = 2.65, θ_c = 0.045, u_*c = 0.03817 m/s, V_c = 0.860 m/s, f_1 = 0.8262, f_3 = 0.6263) '
            'across clear-water intensities V_1 / V_c ∈ [0.45, 1.00] and flood durations t_d ∈ [2, 240] h. Contraction '
            'scour, abutment scour, live-bed dune passage, cohesive clays, graded armor breach, pile-cap exposure, and '
            'debris accumulation fall outside this reduced 2-slider curve.'
        ),
        'meta': (
            'Primary anchors: Buffington 1999 (DOI 10.1061/(ASCE)0733-9429(1999)125:4(376)) · '
            'Melville 1997 (DOI 10.1061/(ASCE)0733-9429(1997)123:2(125)) · '
            'Melville & Chiew 1999 (DOI 10.1061/(ASCE)0733-9429(1999)125:1(59)) · '
            'Sheppard, Melville & Demir 2014 (DOI 10.1061/(ASCE)HY.1943-7900.0000800) · Model values, not field survey data'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE E.16-A · DIMENSIONLESS TIME t* VS. EMPIRICAL DAY-SECOND CONSTANT IN t_e',
        'body': (
            'Melville and Chiew (1999, DOI 10.1061/(ASCE)0733-9429(1999)125:1(59)) define dimensionless equilibrium '
            'time scale t* = V_1 t_e,sec / a*. Dividing t* (a* / V_1) in seconds by 86,400 s/day produces the standard '
            'published dimensional prefactors 30.89 days·s^(−1) (= 2.669 × 10^6 / 86,400 for shallow flow y_1 / a* <= 6) '
            'and 48.26 days·s^(−1) (= 4.170 × 10^6 / 86,400 for deep flow y_1 / a* > 6), requiring a* in meters and '
            'V_1 in m/s, with a small 0.18% empirical fit step at y_1 / a* = 6 (30.89 × 6^0.25 = 48.35 vs. 48.26).'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE E.16-B · POST-EQUILIBRIUM CLAMP & ZERO-CROSSING GUARD ON f_2',
        'body': (
            'Two boundary conditions govern numerical evaluation of clear-water scour: first, f_2 = 1 − 1.2 [ln(V_1 / '
            'V_c)]^2 crosses zero at V_1 / V_c = exp(−1 / √1.2) ≈ 0.4014, so clear-water sweeps enforce V_1 / V_c >= '
            '0.45 (where f_2 >= 0.2349). Second, at low intensity V_1 / V_c = 0.45, t_e drops to 8.83 days (212.0 h); '
            'when peak duration t_d reaches 240.0 h, t_d / 24 exceeds t_e and K_t must clamp at 1.0 rather than '
            'evaluating |ln((t_d / 24) / t_e)| past maturity.'
        ),
    },
    'skill': {
        'filename': 'bridge-pier-scour-timescale-SKILL.md',
        'name': 'bridge-pier-scour-timescale',
        'description': (
            'AI-agnostic hydraulic engineering skill for Shields critical velocity V_c, Sheppard-Melville and HEC-18 '
            'CSU circular pier scour, and Melville-Chiew clear-water flood-duration time-scale factor K_t.'
        ),
        'rules': [
            (
                'Enforce finite positive pier diameter a*, approach depth y_1, median grain size d_50, gravity g, '
                'sediment specific gravity s > 1.0, relative roughness 5.53 y_1 / d_50 > 1.0, and clear-water '
                'intensity ratio V_1 / V_c in [0.405, 1.00].'
            ),
            (
                'Evaluate Sheppard-Melville clear-water equilibrium scour y_s,SM = 2.5 a* f_1 f_2 f_3 alongside '
                'Froude-capped HEC-18 CSU y_s,CSU, keeping grain-coarseness attenuation f_3 active rather than setting '
                'f_3 = 1.'
            ),
            (
                'Convert dimensionless time scale t* = V_1 t_e,sec / a* using explicit SI inputs (a* in m, V_1 in m/s, '
                'empirical factor 30.89 days*s^-1 for y_1 / a* <= 6 or 48.26 days*s^-1 for y_1 / a* > 6) and clamp '
                'K_t(t_d) = 1.0 whenever flood duration t_d / 24 >= t_e.'
            ),
            (
                'Label transient clear-water scour y_s(t_d) = K_t(t_d) y_s,SM as a Tier T1-T2 hydraulic screening '
                'hypothesis falsified by live-bed transport (V_1 / V_c > 1), graded armor-layer breach, multi-flood '
                'deposition-erosion cycles, cohesive soils, or debris rafts.'
            ),
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.0',
            'date': '2026-11-21',
            'summary': (
                'REV 1.0 (Published 2026-11-21): Volume VII Civil & Hydraulic Engineering monograph continuing Folios '
                'E.05, E.07 & E.14 via Shields incipient motion (1936/1999), Melville pier-scour synthesis (1997), '
                'Melville–Chiew clear-water time scale (1999), Wardhana–Hadipriono U.S. bridge failure forensics '
                '(2003), Sheppard–Melville–Demir equation benchmark (2014), flood hydrograph memory (2020), and '
                'armored-bed clear-water scour experiments (2026).'
            ),
            'opus': (
                'Verification note: all seven primary DOIs in this folio were checked against Crossref and Scite on '
                '2026-11-21 with zero retraction notices; all numerical outputs are recomputed offline by '
                'skills/engineering/e16/verify_e16_pier_scour_timescale.py and represent illustrative closed-form '
                'hydraulic screening model values rather than site-specific field survey data.'
            ),
        }
    ],
    'volume': 7,
    'volume_code': 'VOL. 07',
    'reading_time': '22 MIN READ',
    'word_count': '4,750 WORDS',
    'scite': dict(_SCITE),
}

LONGFORM_DATA = {
    'reading_time': '22 MIN READ',
    'word_count': '4,750 WORDS',
    'parent_folios': ['E.05', 'E.07', 'E.14'],
    'lineage_mode': 'CONTINUATION · Continues E.05 Deep Piling, E.07 Bridge Dynamics & E.14 Rainfall Slope Mechanics',
    'scite': dict(_SCITE),
    'act1_title': 'Act I — Cool Fact & Human Story: Why River Currents Topple More Bridges Than Earthquakes and Wind',
    'act1_dropcap': (
        'On the morning of April 5, 1987, spring snowmelt from the Catskill Mountains surged down Schoharie Creek in '
        'upstate New York and tore beneath a concrete bridge pier. Two highway spans collapsed into the swollen river. '
        'Across the United States, moving water has brought down more highway bridges than wind, earthquakes, and '
        'structural overload combined. Long before a steel girder bends or a concrete deck cracks, the river attacks '
        'the hidden bed below. Fast current strikes the rounded nose of a pier, dives toward the bottom, and rolls '
        'into a swirling horseshoe vortex that scoops sand and gravel from around the footing. Yet classic design '
        'formulas often treat a three-hour mountain flash flood as if the river ran steady for six weeks. Understanding '
        'how sediment threshold and flood duration govern that crater separates flash-flood lag from steady-state erosion.'
    ),
    'act1_plain_bridge': (
        'In plain words, a bridge pier standing in a river forces oncoming water to brake against its front face. '
        'That stalled water plunges straight down toward the riverbed. At the bottom, the downward jet curls around '
        'both flanks like a horseshoe and sweeps loose sand grains out of the hole. In mild currents below the '
        'threshold that moves open riverbed sand, the vortex carves a clean pit without fresh sand washing in from '
        'upstream. Digging that pit to its deepest possible level takes many days of steady flow. Real rainstorms '
        'rarely hold peak speed that long. Roughly half of the final pit depth forms during the opening hours, then '
        'excavation slows sharply as the crater widens. Older formulas that ignore grain size or storm duration can '
        'therefore overestimate shallow flash floods while missing near-threshold clear-water peaks. Pairing sediment '
        'threshold rules with flood duration tracks how deep the pit grows before the storm recedes.'
    ),
    'act1_body': (
        'Forensic engineering placed river hydraulics at the center of structural safety when Kumalasari Wardhana and '
        'Fabian Hadipriono analyzed 503 bridge failures across the United States from 1989 to 2000 (Journal of '
        'Performance of Constructed Facilities, 2003, DOI 10.1061/(ASCE)0887-3828(2003)17:3(144)) and found that 266 '
        'collapses, or 52.88 percent, stemmed from hydraulic flood, scour, and drift action. Predicting that hazard '
        'rests on three historical advances: Albert Shields framed dimensionless bed-shear incipient motion in Berlin '
        'in 1936 (recounted by John Buffington in 1999, DOI 10.1061/(ASCE)0733-9429(1999)125:4(376)); Bruce Melville '
        '(1997, DOI 10.1061/(ASCE)0733-9429(1997)123:2(125)) and Max Sheppard, Melville, and Huseyin Demir (2014, DOI '
        '10.1061/(ASCE)HY.1943-7900.0000800) unified shallow-flow, flow-intensity, and grain-size multipliers across '
        'hundreds of flume and river records; and Melville and Yee-Meng Chiew (1999, DOI '
        '10.1061/(ASCE)0733-9429(1999)125:1(59)) quantified the multi-day time scale required for clear-water scour '
        'pits to reach equilibrium.'
    ),
    'act1_stakes': (
        'Treating pier scour as instantaneous or independent of sediment threshold skews engineering judgment in two '
        'opposite directions. In our illustrative reference model for a 2.00 m circular pier in 3.00 m of water over '
        '2.00 mm quartz sand and gravel, mild flow at 0.45 of critical velocity yields 0.608 m of Sheppard and '
        'Melville equilibrium scour, whereas the threshold-blind Colorado State University Froude formula predicts '
        '1.629 m, or 2.682 times deeper. Conversely, near the clear-water peak at 0.85 of critical velocity, '
        'equilibrium scour reaches 2.505 m over 42.09 days, yet a 2.0 hour flash flood carves 1.213 m and a 24.0 hour '
        'flood carves 1.817 m. Omitting both grain-size attenuation and flood-duration lag inflates modeled short-flood '
        'scour to 4.000 m, more than triple the 2.0 hour model value.'
    ),
    'pullquote': (
        '"A bridge pier vortex excavates half its clear-water crater in hours, yet reaching full equilibrium in sand '
        'can demand weeks of steady floodwater that a passing mountain storm does not supply."'
    ),
    'chronology': [
        (
            '1936',
            'Albert Shields formulates the dimensionless bed-shear threshold for incipient grain motion in Berlin, '
            'later documented from archival records by John Buffington (1999, DOI 10.1061/(ASCE)0733-9429(1999)125:4(376)).'
        ),
        (
            '1997',
            'Bruce Melville synthesizes pier and abutment scour multipliers separating flow depth, flow intensity, '
            'sediment coarseness, shape, and alignment (Journal of Hydraulic Engineering, DOI '
            '10.1061/(ASCE)0733-9429(1997)123:2(125)).'
        ),
        (
            '1999',
            'Bruce Melville and Yee-Meng Chiew formulate the clear-water equilibrium time scale and exponential '
            'temporal scour curve for circular bridge piers (Journal of Hydraulic Engineering, DOI '
            '10.1061/(ASCE)0733-9429(1999)125:1(59)).'
        ),
        (
            '2003',
            'Kumalasari Wardhana and Fabian Hadipriono survey 503 United States bridge failures from 1989 to 2000, '
            'attributing 52.88 percent to hydraulic flood and scour causes (DOI 10.1061/(ASCE)0887-3828(2003)17:3(144)).'
        ),
        (
            '2014',
            'Max Sheppard, Bruce Melville, and Huseyin Demir benchmark 23 local pier-scour equations against 569 '
            'laboratory and 928 field records (Journal of Hydraulic Engineering, DOI 10.1061/(ASCE)HY.1943-7900.0000800).'
        ),
        (
            '2026',
            'Abdorreza Kabiri-Samani, Amir Fathi, and Rashid Farooq test clear-water scour in armored beds under '
            'steady and unsteady hydrographs (Journal of Hydrology and Hydromechanics, DOI 10.2478/johh-2026-0004).'
        ),
    ],
    'act2_title': 'Act II — Cross-Field Intuition: Beach Fence Posts, Horseshoe Eddies & Flood Time Lag',
    'act2_analogy': (
        'Plant a round wooden fence post upright in wet beach sand as a shallow wave glides shoreward. Water piles '
        'up slightly against the front of the timber, plunges down its face, and wraps around both sides in a '
        'spinning U-shaped eddy that scoops a neat crescent moat ahead of the post while leaving a small sand ridge '
        'behind it. Within two seconds the moat jumps into view, yet as the pocket deepens the swirling eddy weakens '
        'against the wider walls and stops digging before the wave drains back. This beach analogy stops where ocean '
        'swash reverses direction every few seconds in ankle-deep water, whereas a river flood drives a sustained '
        'unidirectional horseshoe vortex for hours or days around meters-wide concrete piers.'
    ),
    'act2_plain_primer': (
        'Our interactive hydraulic laboratory exposes two storm controls for a two-meter circular pier in three '
        'meters of water. The first slider is Clear-Water Flow Intensity, running from 0.45 to 1.00 of the critical '
        'velocity needed to move two-millimeter riverbed sand. Dragging Clear-Water Flow Intensity upward strengthens '
        'the plunging horseshoe vortex and raises both equilibrium scour depth and the days needed for full maturity. '
        'The second slider is Peak Flood Duration, from 2.0 to 240.0 hours. Sweep it rightward to watch fast early '
        'excavation slow down.'
    ),
    'distill_diagram': {
        'analogy_title': 'Horseshoe Vortex Excavation vs. Storm Clock',
        'analogy_sub': 'Downward pier-nose flow carves a crescent pit rapidly at first, then slows as the hole deepens',
        'force_a_title': 'Clear-Water Flow Intensity',
        'force_a_sub': 'Approaching sediment threshold strengthens horseshoe-vortex shear and deepens equilibrium scour',
        'force_b_title': 'Peak Flood Duration',
        'force_b_sub': 'Short mountain flash floods end long before weeks-long clear-water equilibrium is reached',
        'threshold_title': 'Incipient Live-Bed Boundary and Maturity Ratio',
        'threshold_pass': 'Transient lag regime: short floods hold pit depth below multi-week equilibrium envelopes',
        'threshold_fail': 'Peak threshold or armor breach: sustained flow near critical speed maximizes clear-water scour',
    },
    'act2_intuition': (
        'Once we step from plain intuition to formal hydraulics, four coupled relations govern clear-water pier scour. '
        'First, for uniform cohesionless quartz sediment of specific gravity s = ρ_s / ρ = 2.65, median diameter '
        'd_50 = 2.00 mm = 0.002 m, and critical Shields stress θ_c = 0.045 (Buffington 1999, DOI '
        '10.1061/(ASCE)0733-9429(1999)125:4(376)), critical bed shear velocity is u_*c = √(θ_c (s − 1) g d_50) = '
        '0.03817 m/s. Integrating the rough-bed logarithmic velocity profile across approach depth y_1 = 3.00 m '
        '(Melville 1997, DOI 10.1061/(ASCE)0733-9429(1997)123:2(125)) yields critical depth-averaged velocity '
        'V_c = 5.75 u_*c log_10(5.53 y_1 / d_50) = 0.860 m/s. Clear-water scour holds while upstream approach '
        'velocity V_1 stays at or below V_c (flow intensity V_1 / V_c <= 1.00), so upstream bedload does not refill '
        'the horseshoe pit. In the Sheppard–Melville (S/M) synthesis (Sheppard, Melville & Demir 2014, DOI '
        '10.1061/(ASCE)HY.1943-7900.0000800), equilibrium scour around effective diameter a* = 2.00 m factors into '
        'y_s,SM = 2.5 a* f_1 f_2 f_3, combining shallowness f_1 = tanh((y_1 / a*)^0.4) = 0.8262, intensity '
        'f_2 = max(0, 1 − 1.2 [ln(V_1 / V_c)]^2), and grain-coarseness f_3 = (a* / d_50) / [0.4 (a* / d_50)^1.2 + '
        '10.6 (a* / d_50)^(−0.13)] = 0.6263 at a* / d_50 = 1,000.'
    ),
    'act2_deepening': (
        'Comparing Sheppard–Melville against the Federal Highway Administration HEC-18 Colorado State University (CSU) '
        'equation y_s,CSU = 2.0 K_1 K_2 K_3 y_1 (a* / y_1)^0.65 Fr_1^0.43 (capped at 2.4 a* for Fr_1 <= 0.8, with '
        'Fr_1 = V_1 / √(g y_1) and K_1 = 1.0, K_2 = 1.0, K_3 = 1.1) exposes a revealing physical crossover. At mild '
        'flow V_1 / V_c = 0.45 (V_1 = 0.387 m/s, Fr_1 = 0.0713), CSU omits the sediment mobility threshold V_c and '
        'predicts y_s,CSU = 1.629 m, whereas S/M attenuates f_2 to 0.2349 and predicts 0.608 m (2.682× lower). Near '
        'the clear-water peak V_1 / V_c = 0.85 (V_1 = 0.731 m/s, Fr_1 = 0.1348, f_2 = 0.9683), S/M equilibrium rises '
        'to 2.505 m above CSU\'s 2.142 m—yet Melville and Chiew (1999, DOI 10.1061/(ASCE)0733-9429(1999)125:1(59)) '
        'showed that reaching equilibrium takes t_e = 30.89 (a* / V_1) (V_1 / V_c − 0.4) (y_1 / a*)^0.25 = 42.09 days '
        '(1,010.1 hours). Applying K_t(t_d) = exp(−0.03 |(V_c / V_1) ln((t_d / 24) / t_e)|^1.6) reduces modeled scour '
        'to 1.213 m (K_t = 0.4841) in a 2.0 h flash flood and 1.817 m (K_t = 0.7254) in a 24.0 h flood, whereas '
        'setting f_3 = 1 and K_t = 1 in our planted-defect check inflates depth to 4.000 m.'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Flash Flood vs. Multi-Day Storm at V_1 / V_c = 0.85): Keep Clear-Water Flow Intensity at '
            '0.85 (V_1 = 0.731 m/s, t_e = 42.09 days) and sweep Peak Flood Duration from 2.0 h through 24.0 h up to '
            '120.0 h. Watch time factor K_t climb from 0.4841 (y_s = 1.213 m) to 0.7254 (y_s = 1.817 m) and 0.8777 '
            '(y_s = 2.199 m), passing the static CSU line (2.142 m) around five days while still trailing S/M '
            'equilibrium (2.505 m).'
        ),
        (
            'Experiment 2 (Near-Threshold Crossover at V_1 / V_c = 0.45): Drag Clear-Water Flow Intensity down to '
            '0.45 and sweep Peak Flood Duration to 240.0 h. Because equilibrium time shrinks to t_e = 8.83 days '
            '(212.0 h), K_t clamps cleanly at 1.0000 for t_d = 240.0 h, holding y_s = y_s,SM,eq = 0.608 m while '
            'threshold-blind HEC-18 CSU sits 2.682× higher at 1.629 m.'
        ),
        (
            'Experiment 3 (Incipient Live-Bed Peak at V_1 / V_c = 1.00 & 4-Lens Observatory): Raise Clear-Water Flow '
            'Intensity to 1.00 (V_1 = V_c = 0.860 m/s, f_2 = 1.0000) at 24.0 h to inspect the clear-water equilibrium '
            'ceiling (y_s,SM,eq = 2.587 m, t_e = 47.70 days, K_t = 0.7703, y_s = 1.993 m), then switch across the '
            '4-Lens Observatory (3D Surface, Phase Portraits, Kirchhoff Ribbon, Polar Radar).'
        ),
    ],
    'act4_title': 'Act IV — Sustaining Infrastructure Under Unsteady Floods: Hydrograph Memory & Armored Beds',
    'act4_human_ai': (
        'Climate-intensified convective storms increasingly subject aging river bridges—many supported on shallow '
        'spread footings or short piles—to steep, short-duration flood hydrographs and sequential storm trains. '
        'Combining closed-form equilibrium bounds (Sheppard, Melville & Demir 2014, DOI '
        '10.1061/(ASCE)HY.1943-7900.0000800) with flood-scale erosion-deposition tracking (Link et al. 2020, DOI '
        '10.1061/(ASCE)HY.1943-7900.0001696) and unsteady armored-bed testing (Kabiri-Samani, Fathi & Farooq 2026, '
        'DOI 10.2478/johh-2026-0004) helps hydraulic engineers interpret sonar and fiber-optic pier monitors without '
        'confusing 2-hour flash-flood lag for long-term foundation capacity.'
    ),
    'act4_deepening': (
        'Under the Tier T1–T2 hypothesis examined here, clear-water scour depth around an unskewed circular pier in '
        'uniform cohesionless sand follows y_s(t_d) = K_t(t_d) y_s,SM,eq over 0.45 <= V_1 / V_c <= 1.00, capturing '
        'both near-threshold attenuation relative to Froude-only CSU and sub-equilibrium lag when storm duration t_d '
        'is far shorter than t_e. Four field mechanisms falsify this reduced single-storm model: (1) live-bed floods '
        '(V_1 / V_c > 1.0), where upstream bedload rapidly cycles scour and dune trough fluctuations; (2) graded '
        'gravel armor layers over fine sand (Kabiri-Samani et al. 2026, DOI 10.2478/johh-2026-0004), where horseshoe '
        'vortices breach the surface armor and excavate deeper "armor-break" craters than uniform-grain formulas '
        'predict; (3) multi-peak flood sequences with incomplete infilling between storms (Link et al. 2020, DOI '
        '10.1061/(ASCE)HY.1943-7900.0001696); and (4) floating log jams or skewed pier walls that amplify downflow '
        'width beyond a*. Keeping f_3 = 1, K_t = 1 as a failing planted defect inside '
        'verify_e16_pier_scour_timescale.py guards automated screening against unattenuated steady-state shortcuts.'
    ),
    'cf_bridge': 'Continues E.05/E.07/E.14',
    'sources': [
        (
            'Buffington, J. M. (1999). The Legend of A. F. Shields. Journal of Hydraulic Engineering, 125(4), '
            '376–387. DOI: 10.1061/(ASCE)0733-9429(1999)125:4(376).'
        ),
        (
            'Melville, B. W. (1997). Pier and Abutment Scour: Integrated Approach. Journal of Hydraulic Engineering, '
            '123(2), 125–136. DOI: 10.1061/(ASCE)0733-9429(1997)123:2(125).'
        ),
        (
            'Melville, B. W., & Chiew, Y.-M. (1999). Time Scale for Local Scour at Bridge Piers. Journal of Hydraulic '
            'Engineering, 125(1), 59–65. DOI: 10.1061/(ASCE)0733-9429(1999)125:1(59).'
        ),
        (
            'Wardhana, K., & Hadipriono, F. C. (2003). Analysis of Recent Bridge Failures in the United States. '
            'Journal of Performance of Constructed Facilities, 17(3), 144–150. '
            'DOI: 10.1061/(ASCE)0887-3828(2003)17:3(144).'
        ),
        (
            'Sheppard, D. M., Melville, B., & Demir, H. (2014). Evaluation of Existing Equations for Local Scour at '
            'Bridge Piers. Journal of Hydraulic Engineering, 140(1), 14–23. '
            'DOI: 10.1061/(ASCE)HY.1943-7900.0000800.'
        ),
        (
            'Link, O., García, M., Pizarro, A., Alcayaga, H., & Palma, S. (2020). Local Scour and Sediment Deposition '
            'at Bridge Piers during Floods. Journal of Hydraulic Engineering, 146(3), 04020003. '
            'DOI: 10.1061/(ASCE)HY.1943-7900.0001696.'
        ),
        (
            'Kabiri-Samani, A., Fathi, A., & Farooq, R. (2026). Does an Armor Layer Control Clear-Water Scour at '
            'Cylindrical Bridge Piers? A Comprehensive Experimental Assessment under Steady and Unsteady Flow '
            'Conditions. Journal of Hydrology and Hydromechanics, 74(1). DOI: 10.2478/johh-2026-0004.'
        ),
        (
            'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and '
            'classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
            '882–898. DOI: 10.1162/qss_a_00146.'
        ),
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Melville-Chiew transient pier scour depth '
        'evolution versus flood duration compared against Sheppard-Melville and HEC-18 CSU equilibrium bounds">\n'
        '            <line x1="48" y1="184" x2="352" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <line x1="48" y1="30" x2="48" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <text x="54" y="22" font-size="10.5" font-weight="600" fill="currentColor">Scour Depth y_s(t_d) vs. Flood Duration (2–240 h)</text>\n'
        '            <line id="tp-e16-sm-eq-line" x1="52" y1="55.8" x2="348" y2="55.8" stroke="var(--tp-minium)" stroke-width="1.5" stroke-dasharray="5,3"/>\n'
        '            <line id="tp-e16-csu-eq-line" x1="52" y1="73.2" x2="348" y2="73.2" stroke="var(--tp-slate)" stroke-width="1.4" stroke-dasharray="3,3"/>\n'
        '            <path id="tp-e16-scour-curve" data-custom-curve="1" d="M 52.0 117.8 L 70.5 114.5 L 89.0 111.1 L 107.5 107.7 L 126.0 104.2 L 144.5 100.6 L 163.0 97.1 L 181.5 93.5 L 200.0 89.9 L 218.5 86.3 L 237.0 82.8 L 255.5 79.3 L 274.0 75.9 L 292.5 72.7 L 311.0 69.5 L 329.5 66.6 L 348.0 63.8" fill="none" stroke="var(--tp-prussian)" stroke-width="2.5"/>\n'
        '            <circle id="tp-svg-eng-point" cx="206" cy="89" r="6" fill="var(--tp-verdigris)"/>\n'
        '            <text id="tp-e16-sm-label" x="56" y="49" font-size="8.8" fill="var(--tp-minium)">S/M eq. y_s,SM = 2.505 m (t_e = 42.1 d)</text>\n'
        '            <text id="tp-e16-csu-label" x="184" y="84" font-size="8.6" fill="var(--tp-slate)">HEC-18 CSU = 2.142 m</text>\n'
        '            <line x1="372" y1="24" x2="372" y2="192" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="386" y="22" font-size="10.2" font-weight="600" fill="currentColor">Pier Scour Benchmarks (a* = 2 m, V_1/V_c = 0.85)</text>\n'
        '            <rect x="386" y="38" width="256" height="62" rx="6" fill="var(--tp-stone)" fill-opacity="0.28" stroke="var(--tp-prussian)" stroke-width="1.6"/>\n'
        '            <text x="398" y="59" font-size="9.5" font-weight="600" fill="var(--tp-prussian)">2.0 h flash → y_s = 1.213 m (48.4%)</text>\n'
        '            <text x="398" y="81" font-size="9" fill="var(--tp-verdigris)">24 h storm → 1.817 m (72.5%)</text>\n'
        '            <rect x="386" y="112" width="256" height="58" rx="6" fill="var(--tp-verdigris)" fill-opacity="0.12" stroke="var(--tp-verdigris)" stroke-width="1.4"/>\n'
        '            <text x="398" y="134" font-size="9.5" font-weight="600" fill="var(--tp-prussian)">V_1/V_c = 0.45 → S/M 0.608 vs CSU 1.629 m</text>\n'
        '            <text x="398" y="154" font-size="9" fill="var(--tp-minium)">Defect (f_3=1, K_t=1): 4.000 m at 0.85</text>\n'
        '            <text x="48" y="206" font-size="10" fill="var(--tp-verdigris)">Sheppard–Melville + Melville–Chiew model · verify_e16_pier_scour_timescale.py</text>\n'
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining what a weathered two-meter circular concrete highway bridge pier in a '
        'shallow gravel-and-sand river at low-water inspection with an upstream crescent-shaped horseshoe scour pit '
        'and downstream wake ripples would look like (artistic impression, not a measured field structure or '
        'specification; governing equations and specifications are kept intact in deterministic Plate E.16-A below)'
    ),
    'caption': (
        'Conceptual Vision Plate E.16-V (Imagining What It Would Look Like) · Artistic field impression imagining a '
        'circular concrete river bridge pier at low water revealing its upstream crescent horseshoe scour crater in '
        'graded gravel and sand. Governing equations and specifications are kept intact in deterministic Plate E.16-A '
        'and the offline verifier below.'
    ),
}

DISPATCH = {
    'kicker': 'FRONTIER HYDRAULIC DISPATCH · BRIDGE PIER SCOUR & HYDROGRAPH TIME LAG',
    'headline': 'Shields Sediment Threshold, Sheppard–Melville Pier Scour & Flash-Flood Time-Scale Lag',
    'body': (
        'Why has moving river water caused 52.88% of modern U.S. bridge failures (Wardhana & Hadipriono 2003), yet '
        'steady-state formulas misread short mountain floods? Coupling Sheppard–Melville equilibrium scour (2014) '
        'with Melville–Chiew time lag (1999, DOI 10.1061/(ASCE)0733-9429(1999)125:1(59)) tracks y_s from 1.213 m at '
        '2.0 h and 1.817 m at 24.0 h toward 2.505 m over t_e = 42.09 days.'
    ),
}

META_3D = (
    'Clear-Water Pier Scour & Flood-Duration Lag Surface',
    'X: Clear-Water Flow Intensity V_1 / V_c · Z: Flood Duration t_d (h) · Y: Normalized Scour Depth y_s(t_d) / a*',
)

ES_TRANSLATION = {
    'title_es': 'Socavación Local en Pilas de Puente, Umbral de Shields y Retardo Temporal en Avenidas',
    'subtitle_es': (
        'Continuación de los Folios E.05, E.07 y E.14: estudio ilustrativo de ingeniería hidráulica que acopla el '
        'inicio de movimiento de Shields, la socavación de equilibrio de Sheppard y Melville y el factor temporal de '
        'Melville y Chiew en pilas circulares de puente.'
    ),
    'why_es': (
        'Igual que un poste redondo clavado en arena húmeda forma una fosa en herradura cuando una ola choca contra '
        'su frente, una pila de puente concentra un vórtice descendente cuya profundidad depende del umbral del grano '
        'y de la duración de la avenida.'
    ),
    'plain_es': (
        'En palabras sencillas, una pila de concreto dentro de un río frena el agua que choca contra su cara frontal. '
        'Esa columna de agua baja hacia el lecho, gira alrededor de ambos costados como una herradura y arrastra la '
        'arena suelta fuera del hueco. Cuando la corriente queda por debajo del umbral que mueve el resto del cauce, '
        'el vórtice excava sin que entre arena nueva desde aguas arriba. Alcanzar la profundidad máxima de equilibrio '
        'toma semanas de flujo constante, mientras que una tormenta real dura pocas horas o días. Combinar el umbral '
        'de sedimento con la duración de la avenida permite estimar cuánto crece la fosa antes de que baje el río.'
    ),
    'deep_es': (
        'En el modelo de Melville y Chiew (1999, DOI 10.1061/(ASCE)0733-9429(1999)125:1(59)) y Sheppard, Melville y '
        'Demir (2014, DOI 10.1061/(ASCE)HY.1943-7900.0000800), para una pila circular a* = 2.00 m en tirante y_1 = '
        '3.00 m sobre arena cuarzosa d_50 = 2.00 mm (s = 2.65, θ_c = 0.045, u_*c = 0.03817 m/s, V_c = 0.860 m/s), la '
        'socavación de equilibrio en agua clara sigue y_s,SM = 2.5 a* f_1 f_2 f_3 con f_1 = 0.8262 y f_3 = 0.6263. '
        'En flujo moderado V_1 / V_c = 0.45, S/M predice 0.608 m frente a 1.629 m de la ecuación HEC-18 CSU (2.682× '
        'mayor por omitir V_c). En V_1 / V_c = 0.85, el equilibrio S/M sube a 2.505 m con escala temporal t_e = 42.09 '
        'días (constante empírica 30.89 días·s^(−1) con a* en m y V_1 en m/s): una avenida relámpago de 2.0 h alcanza '
        'K_t = 0.4841 (y_s = 1.213 m) y una tormenta de 24.0 h llega a K_t = 0.7254 (y_s = 1.817 m), frente a 4.000 m '
        'con el defecto f_3 = 1, K_t = 1. Esta hipótesis de nivel T1–T2 se refuta en lecho móvil (V_1 / V_c > 1.0), '
        'ruptura de coraza gruesa sobre arena fina (Kabiri-Samani et al. 2026, DOI 10.2478/johh-2026-0004), trenes de '
        'avenidas sucesivas (Link et al. 2020, DOI 10.1061/(ASCE)HY.1943-7900.0001696) o palizadas.'
    ),
    'bridge_es': (
        'Acoplar y_s(t_d) = K_t(t_d) y_s,SM distingue el retardo en avenidas cortas del equilibrio de semanas en '
        'arena uniforme (estudio hidráulico ilustrativo, no un cálculo de cimentación).'
    ),
}
