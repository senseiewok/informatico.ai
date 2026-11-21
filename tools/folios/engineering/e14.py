#!/usr/bin/env python3
"""Folio E.14 (ENGINEERING): Unsaturated Soil Suction Stress, van Genuchten-Mualem Water Retention & Rainfall-Induced Infinite-Slope Instability."""
from __future__ import annotations

SLUG = 'e14'

PILLAR = 'engineering'

_SCITE = {
    'doi': '10.2136/sssaj1980.03615995004400050002x',
    'fetched_on': '2026-11-21',
    'citing_publications': 27857,
    'supporting': 105,
    'mentioning': 12669,
    'contrasting': 4,
    'retracted': False,
    'summary': (
        'Scite Smart Citation Index entry for van Genuchten 1980, "A Closed-form Equation for Predicting the Hydraulic '
        'Conductivity of Unsaturated Soils" (Soil Science Society of America Journal, DOI 10.2136/sssaj1980.03615995004400050002x), '
        'fetched 2026-11-21: 27,857 citing records (105 supporting, 12,669 mentioning, 4 contrasting) and no retraction notice. '
        'These counts describe that foundational paper, not this folio.'
    ),
}

FOLIO = {
    'folio_id': 'E.14',
    'slug': 'e14',
    'pillar': 'engineering',
    'category_code': 'E',
    'parent_folios': ['E.05', 'E.13'],
    'lineage_mode': 'CONTINUATION · Continues E.05 Terzaghi Effective Stress & E.13 Biot Poroelasticity',
    'title': 'Unsaturated Soil Suction Stress, van Genuchten–Mualem Water Retention & Rainfall-Induced Infinite-Slope Instability',
    'subtitle': (
        "Continuing Folio E.05's saturated Terzaghi effective stress and E.13's poroelastic fault margin: an illustrative "
        'geotechnical screening study coupling van Genuchten–Mualem retention S_e(ψ) and K_r(S_e), Lu–Godt–Wu closed-form '
        'suction stress σ^s = −S_e ψ, and infinite-slope limit equilibrium FS across wetting hillslopes and dry sands.'
    ),
    'date_published': '2026-11-21',
    'date_redated': '2026-11-21',
    'current_edition': 'REV 1.0',
    'status_badge': 'VADOSE GEOMECHANICS · REV 1.0',
    'primary_kernel': 'skills/engineering/e14/verify_e14_unsaturated_suction.py',
    'governing_law': "S_e = [1 + (α_vG ψ)^n]^(−m) · σ^s = −S_e ψ · FS = tan φ' / tan β + (c' − σ^s tan φ') / (γ z sin β cos β)",
    'colophon': {
        'identifier': 'E.14 · Unsaturated Suction Stress & Slope Margin · REV 1.0',
        'kernels': 'van Genuchten SWCC (1980) · Mualem K_r (1976) · Lu–Godt–Wu Suction Stress (2010)',
        'benchmarks': (
            'Model values (silty loam ψ = 24.0 kPa, β = 34.0°): S_e = 0.904 · K_r = 0.1662 · '
            "σ^s = −21.69 kPa · FS = 1.557 (collapses to 0.962 at ψ = 2.0 kPa)"
        ),
        'bridge': 'Continues E.05/E.13',
    },
    'sliders': [
        {
            'label': 'Matric Suction at Slip Plane (ψ = u_a − u_w)',
            'min': 0.0,
            'max': 120.0,
            'step': 2.0,
            'value': 24.0,
            'unit': ' kPa',
        },
        {
            'label': 'Slope Inclination (β)',
            'min': 20.0,
            'max': 45.0,
            'step': 0.5,
            'value': 34.0,
            'unit': '°',
        },
    ],
    'steps': [
        (
            'Stage 1 (van Genuchten–Mualem Water Retention, Continuing E.05): Above the water table (ψ = u_a − u_w ≥ 0 kPa), '
            'soil pores hold both air and capillary water. van Genuchten (1980, DOI 10.2136/sssaj1980.03615995004400050002x) '
            'parameterizes effective saturation as S_e(ψ) = [1 + (α_vG ψ)^n]^(−m) with m = 1 − 1/n (requiring n > 1), '
            'and Mualem (1976, DOI 10.1029/WR012i003p00513) gives K_r(S_e) = S_e^(1/2) [1 − (1 − S_e^(1/m))^m]^2. '
            'In silty loam (α_vG = 0.02 kPa^−1, n = 1.60, m = 0.375) at ψ = 24.0 kPa, S_e = 0.904 and K_r = 0.1662.'
        ),
        (
            'Stage 2 (Lu–Godt–Wu Suction Stress σ^s and Pore-Exponent Split): Lu, Godt & Wu (2010, DOI 10.1029/2009WR008646) '
            'unify Bishop effective stress σ\' = (σ − u_a) − σ^s via closed-form suction stress σ^s(ψ) = −S_e(ψ) ψ ≤ 0 '
            '(compression-positive convention, so negative σ^s pulls grains together). For silty loam (1 < n ≤ 2), |σ^s| rises '
            'monotonically (−21.69 kPa at ψ = 24.0 kPa; −65.34 kPa at ψ = 120.0 kPa). For clean sand (n = 2.68 > 2, '
            'α_vG = 0.145 kPa^−1), |σ^s| peaks at ψ_peak = 7.964 kPa (−4.52 kPa) and declines to −2.08 kPa by ψ = 40.0 kPa.'
        ),
        (
            'Stage 3 (Infinite-Slope Wetting Collapse While Still Unsaturated): Following Lu & Godt (2008, '
            'DOI 10.1029/2008WR006976) with steady uniform suction at z = 2.0 m, γ = 19.0 kN/m^3, c\' = 2.0 kPa, and '
            'φ\' = 28.0°, a steep silty-loam slope at β = 34.0° (> φ\') stands at FS = 1.557 when ψ = 24.0 kPa. '
            'Rain wetting to ψ = 2.0 kPa drops FS to 0.962 (< 1.0) even before pore-water pressure turns positive, '
            'and saturation (ψ = 0 kPa, K_r = 1.0) drops FS to 0.902.'
        ),
        (
            'Stage 4 (Open Hypothesis, Tier T1–T2, and Falsification Condition): Hypothesis (Tier T1–T2): in shallow '
            'unsaturated hillslopes steeper than their drained friction angle (β > φ\'), storm-triggered collapse below '
            'FS = 1.0 tracks the loss of S_e ψ during wetting rather than waiting for positive u_w, whereas setting Bishop '
            'χ = 1.0 on dry clean sand (ψ = 40.0 kPa, γ = 18.0 kN/m^3, c\' = 0, φ\' = 32°, β = 36°) falsely inflates FS '
            'from 0.936 to 2.320. This 1D steady-suction hypothesis is falsified where 3D topographic flow convergence, '
            'macropore bypass (Iverson 2000, DOI 10.1029/2000WR900090), wetting-branch hysteresis, or root cohesion '
            'governs field failure.'
        ),
    ],
    'readouts': [
        {'label': 'Effective Saturation & Conductivity', 'value': 'S_e = 0.904 · K_r = 0.1662 (model)'},
        {'label': 'Lu–Godt–Wu Suction Stress (σ^s)', 'value': '−21.69 kPa (σ\'_n = 47.81 kPa, model)'},
        {'label': 'Infinite-Slope Factor of Safety (FS)', 'value': 'FS = 1.557 (τ = 17.62 kPa, model)'},
        {'label': 'Mohr–Coulomb Suction Regime', 'value': 'ABOVE LIMIT EQUILIBRIUM (FS >= 1.2, model)'},
    ],
    'spec_plate': {
        'division': 'VADOSE GEOTECHNICS / CSI 31 32 00 (FILING LABEL · DESIGN STUDY)',
        'title': 'Unsaturated Silty-Loam & Clean-Sand Hillslope Suction-Stress Screening Envelope',
        'body': (
            'Illustrative closed-form screening study, not a site geotechnical investigation or slope-stability design: '
            'prescribes steady uniform matric suction ψ ≥ 0 kPa at slip-plane depth z = 2.0 m with constant unit weight '
            'γ = 19.0 kN/m^3 (silty loam) or 18.0 kN/m^3 (clean sand), α_vG expressed in kPa^−1 (1 kPa ≈ 10.194 cm H2O), '
            'and atmospheric pore-air pressure u_a = 0. Below the water table (u_w > u_a, ψ < 0), behavior transitions '
            'to saturated Terzaghi effective stress. Transient Richards infiltration, wetting-drying hysteresis, and '
            'field tensiometry are required for any real slope assessment.'
        ),
        'meta': (
            'Primary anchors: van Genuchten 1980 (DOI 10.2136/sssaj1980.03615995004400050002x) · '
            'Mualem 1976 (DOI 10.1029/WR012i003p00513) · Lu, Godt & Wu 2010 (DOI 10.1029/2009WR008646) · '
            'Iverson 2000 (DOI 10.1029/2000WR900090) · Model values, not field measurements'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE E.14-A · FINE SILTY LOAM (n ≤ 2) VS. CLEAN SAND (n > 2) SUCTION PEAK',
        'body': (
            'Differentiating |σ^s(ψ)| = ψ [1 + (α_vG ψ)^n]^(−(n−1)/n) shows that d|σ^s|/dψ flips sign only when n > 2. '
            'In fine silty loam (n = 1.60 ≤ 2), adsorptive films and broad pore-size distributions sustain a monotonically '
            'growing tensile suction stress across the modeled suction range. In uniform clean sand (n = 2.68 > 2, '
            'α_vG = 0.145 kPa^−1), pendular capillary bridges break down past ψ_peak = 7.964 kPa (|σ^s| = 4.52 kPa), '
            'reducing |σ^s| to 2.08 kPa at ψ = 40.0 kPa and leaving dry sand at FS = 0.936 when β = 36° > φ\' = 32°.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE E.14-B · STEADY PRESCRIBED ψ, CONSTANT γ & α_vG UNIT CONVENTION',
        'body': (
            'This reduced 2-slider model prescribes steady uniform ψ at z = 2.0 m and constant γ rather than integrating '
            'coupled transient Richards diffusion (Iverson 2000, DOI 10.1029/2000WR900090) or moisture-dependent unit '
            'weight γ(θ) (Lu & Godt 2008, DOI 10.1029/2008WR006976). Also check parameter units carefully: α_vG here '
            'uses kPa^−1 (matching ψ in kPa), whereas Carsel & Parrish soil tables report α in cm^−1 of water head '
            '(1 kPa ≈ 10.194 cm H2O). Below the water table (ψ < 0), saturated Terzaghi pore pressure applies.'
        ),
    },
    'skill': {
        'filename': 'unsaturated-suction-slope-SKILL.md',
        'name': 'unsaturated-suction-slope',
        'description': (
            'AI-agnostic civil geotechnical skill for van Genuchten-Mualem unsaturated soil water retention, '
            'Lu-Godt-Wu closed-form suction stress sigma_s = -S_e * psi, and rainfall-induced infinite-slope Factor of Safety.'
        ),
        'rules': [
            (
                'Enforce the physical domain psi = u_a - u_w >= 0 kPa, alpha_vg > 0 kPa^-1, and n > 1.0 (m = 1 - 1/n in (0, 1)) '
                'for van Genuchten effective saturation S_e(psi) = [1 + (alpha_vg * psi)^n]^(-m) and Mualem relative '
                'hydraulic conductivity K_r(S_e).'
            ),
            (
                'Compute Lu-Godt-Wu closed-form suction stress as sigma_s(psi) = -S_e(psi) * psi <= 0 (with sigma_s = 0 at '
                'psi = 0), keeping effective weighting chi = S_e rather than extrapolating Terzaghi chi = 1.0 into '
                'unsaturated soil.'
            ),
            (
                'Distinguish fine-grained monotonic retention (1 < n <= 2, silty loam where |sigma_s| grows monotonically '
                'with suction) from coarse-grained non-monotonic retention (n > 2, clean sand where |sigma_s| peaks near '
                'air-entry and declines toward zero upon drying).'
            ),
            (
                'Frame infinite-slope stability as a steady-suction, constant-gamma Tier T1-T2 screening hypothesis that '
                'requires 3D seepage, wetting-drying hysteresis, and field tensiometry before any site-level slope evaluation.'
            ),
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.0',
            'date': '2026-11-21',
            'summary': (
                'REV 1.0 (Published 2026-11-21): Volume VII Civil & Geotechnical Engineering monograph continuing Folios '
                'E.05 & E.13 via Mualem relative permeability (1976), Fredlund–Morgenstern–Widger unsaturated shear '
                'strength (1978), van Genuchten retention (1980), Iverson infiltration triggers (2000), and Lu–Godt–Wu '
                'closed-form suction stress (2008, 2010).'
            ),
            'opus': (
                'Verification note: all six primary DOIs in this folio were checked against Crossref on 2026-11-21 with '
                'zero retraction notices; all numerical outputs are recomputed offline by '
                'skills/engineering/e14/verify_e14_unsaturated_suction.py and represent illustrative closed-form '
                'steady-suction model outputs rather than field measurements.'
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
    'parent_folios': ['E.05', 'E.13'],
    'lineage_mode': 'CONTINUATION · Continues E.05 Terzaghi Effective Stress & E.13 Biot Poroelasticity',
    'scite': dict(_SCITE),
    'act1_title': 'Act I — Cool Fact & Human Story: Why Damp Sand Castles Stand and Steep Hills Slip Before Flooding',
    'act1_dropcap': (
        'Anyone who has built a sand castle at low tide has watched an apparent geotechnical paradox up close: dry sand '
        'pours out into a flat cone near 32°, completely submerged sand slumps flat under water, yet damp sand stands in '
        'vertical walls. The hidden clamp holding those grains together is capillary water under tension—negative gauge '
        'pore pressure above the water table, called matric suction ψ = u_a − u_w. In 1976, Yechezkel Mualem linked '
        'pore-size distribution to unsaturated hydraulic conductivity (Water Resources Research, DOI 10.1029/WR012i003p00513), '
        'and in 1980 Martinus van Genuchten turned that integral into a smooth closed-form Soil–Water Characteristic Curve '
        '(Soil Science Society of America Journal, DOI 10.2136/sssaj1980.03615995004400050002x). Meanwhile, Fredlund, '
        'Morgenstern, and Widger (1978, Canadian Geotechnical Journal, DOI 10.1139/t78-029) formalized shear strength in '
        'unsaturated soils using net normal stress and matric suction as two independent stress-state variables. Today, '
        'understanding when capillary suction holds a hillside above its friction angle—and how rapidly storm rainfall erases '
        'that suction—sits at the center of rainfall-induced landslide forecasting.'
    ),
    'act1_plain_bridge': (
        'In plain words, soil above the groundwater table is neither bone-dry nor completely flooded. Tiny curved water bridges '
        'cling between soil grains and pull them inward, acting like millions of microscopic rubber bands. As long as the '
        'soil stays damp but not saturated, those capillary bridges supply extra clamping force—called suction stress—that '
        'can hold a hillside steeper than loose sand or silt could otherwise stand. During heavy rain, water soaking down '
        'from the surface fills the air spaces, relaxes those curved menisci, and drops the clamping force even before free '
        'groundwater pressure rises above zero. If the slope is steeper than its drained friction angle, losing that suction '
        'can trigger a sudden shallow slide.'
    ),
    'act1_body': (
        'In 2000, Richard M. Iverson coupled transient infiltration physics with infinite-slope stability to show how storm '
        'intensity, hydraulic diffusivity, and antecedent moisture control the timing of shallow landslides (Water Resources '
        'Research, DOI 10.1029/2000WR900090). Eight years later, Ning Lu and Jonathan W. Godt (2008, DOI 10.1029/2008WR006976) '
        'and Lu, Godt, and Wu (2010, DOI 10.1029/2009WR008646) bridged Bishop\'s empirical effective-stress weighting χ with '
        'van Genuchten\'s retention parameters via a single closed-form suction stress: σ^s(ψ) = −S_e(ψ) ψ. In a silty-loam '
        'colluvium (α_vG = 0.02 kPa^−1, n = 1.60, γ = 19.0 kN/m^3, c\' = 2.0 kPa, φ\' = 28.0°, slip-plane depth z = 2.0 m) '
        'on a 34.0° slope, a moderate matric suction of ψ = 24.0 kPa maintains effective saturation S_e = 0.904, suction '
        'stress σ^s = −21.69 kPa, and an infinite-slope Factor of Safety FS = 1.557. Wetting the soil down to ψ = 2.0 kPa—still '
        'under negative pore-water pressure—drops σ^s to −2.00 kPa and sends FS down to 0.962, below limit equilibrium.'
    ),
    'act1_stakes': (
        'Distinguishing true effective suction stress −S_e ψ from naive linear Terzaghi extrapolation −ψ matters directly for '
        'hazard screening on roads, levees, and mountain catchments. In coarse clean sand (α_vG = 0.145 kPa^−1, n = 2.68, '
        'γ = 18.0 kN/m^3, c\' = 0 kPa, φ\' = 32.0°, β = 36.0°), capillary menisci break apart once suction exceeds the '
        'air-entry peak at ψ_peak = 7.964 kPa (σ^s = −4.52 kPa, FS = 1.025). By ψ = 40.0 kPa, effective saturation drops '
        'to S_e = 0.052, suction stress shrinks to −2.08 kPa, and real FS falls to 0.936 (< 1.0). Multiplying full ψ by '
        'χ = 1.0 instead of S_e would predict −40.0 kPa of fictitious clamping and FS = 2.320, masking why dry or overly '
        'coarse slopes fail above their friction angle.'
    ),
    'pullquote': (
        '"Damp soil does not wait for positive floodwater pressure to fail: once rainwater softens effective saturation S_e, '
        'the capillary clamping term σ^s = −S_e ψ fades and a steep slope can slip while still unsaturated."'
    ),
    'chronology': [
        (
            '1976',
            'Yechezkel Mualem derives a predictive integral relation connecting the soil-water retention curve to unsaturated '
            'relative hydraulic conductivity K_r(S_e) (Water Resources Research, DOI 10.1029/WR012i003p00513).'
        ),
        (
            '1978',
            'Delwyn G. Fredlund, Norbert R. Morgenstern, and R. A. Widger formulate unsaturated soil shear strength in terms '
            'of net normal stress (σ − u_a) and matric suction (u_a − u_w) (Canadian Geotechnical Journal, DOI 10.1139/t78-029).'
        ),
        (
            '1980',
            'Martinus Th. van Genuchten introduces the closed-form S_e(ψ) = [1 + (α_vG ψ)^n]^(−m) retention curve that pairs '
            'analytically with Mualem\'s conductivity model (Soil Sci. Soc. Am. J., DOI 10.2136/sssaj1980.03615995004400050002x).'
        ),
        (
            '2000',
            'Richard M. Iverson analyzes transient rainfall pore-pressure diffusion and infinite-slope landslide triggering '
            '(Water Resources Research, DOI 10.1029/2000WR900090).'
        ),
        (
            '2008',
            'Ning Lu and Jonathan W. Godt incorporate unsaturated suction stress profiles into steady infinite-slope stability '
            'analysis (Water Resources Research, DOI 10.1029/2008WR006976).'
        ),
        (
            '2010',
            'Lu, Godt, and D. T. Wu derive the closed-form suction stress characteristic equation σ^s = −S_e ψ and map its '
            'monotonic (1 < n ≤ 2) versus non-monotonic (n > 2) soil regimes (Water Resources Research, DOI 10.1029/2009WR008646).'
        ),
    ],
    'act2_title': 'Act II — Cross-Field Intuition: Sand-Castle Bridges, Exponent n & Suction Collapse',
    'act2_analogy': (
        'Everyday analogy: Imagine stacking damp glass marbles on a tilted wooden tray. When just enough water coats each '
        'contact point, surface-tension necks pull adjacent marbles together so the pile resists sliding even tilted past '
        'its dry repose angle. Flood the tray with a hose, and the water necks merge into bulk water with zero inward pull, '
        'letting the marbles slide; bake the marbles bone-dry, and the water necks snap so they roll away again. Only in the '
        'intermediate unsaturated window—controlled by pore-size uniformity n—do the water bridges stay active.'
    ),
    'act2_plain_primer': (
        'Our interactive geotechnical laboratory exposes two primary parameters from the closed-form screening model. The '
        'first slider is Matric Suction at the Slip Plane (ψ = u_a − u_w, from 0.0 to 120.0 kPa), representing capillary '
        'tension at depth z = 2.0 m inside the silty-loam slope. Dragging ψ toward 0.0 kPa simulates storm wetting: relative '
        'permeability K_r surges from 0.1662 toward 1.0000 while suction stress |σ^s| collapses toward 0.00 kPa and FS crosses '
        'below 1.0 near ψ = 3.27 kPa. The second slider is Slope Inclination (β, from 20.0° to 45.0°), showing how slopes '
        'gentler than φ\' = 28.0° remain above limit equilibrium even saturated, whereas steeper slopes rely on suction.'
    ),
    'distill_diagram': {
        'analogy_title': 'Capillary Menisci Between Unsaturated Grains',
        'analogy_sub': 'Water necks pull grains together via σ^s = −S_e ψ while open pores still drain air',
        'force_a_title': 'Matric Suction (ψ = u_a − u_w)',
        'force_a_sub': 'Rainfall wetting lowers ψ toward 0, raising K_r toward 1 and erasing capillary clamping',
        'force_b_title': 'Slope Inclination (β vs. φ\')',
        'force_b_sub': 'Slopes steeper than φ\' = 28° require c\' and −σ^s tan φ\' to hold FS ≥ 1.0',
        'threshold_title': 'Infinite-Slope Limit Equilibrium',
        'threshold_pass': 'Model above threshold: FS ≥ 1.0 under steady uniform ψ (not transient flow)',
        'threshold_fail': 'Below equilibrium: FS < 1.0 before positive u_w (β > φ\' and ψ < 3.27 kPa at 34°)',
    },
    'act2_intuition': (
        'In van Genuchten (1980) with Mualem constraint m = 1 − 1/n (n > 1), effective saturation S_e(ψ) = '
        '[1 + (α_vG ψ)^n]^(−m) drops smoothly from 1 at ψ = 0 toward 0 at high suction. Multiplying S_e by ψ yields the '
        'Lu–Godt–Wu suction stress σ^s(ψ) = −S_e(ψ) ψ ≤ 0, so effective normal stress on a plane at depth z becomes '
        'σ\'_n = γ z cos²β − σ^s = γ z cos²β + S_e ψ. Differentiating |σ^s(ψ)| yields a critical exponent split at n = 2: '
        'for 1 < n ≤ 2 (silty loam, n = 1.60), d|σ^s|/dψ remains positive for all ψ ≥ 0; for n > 2 (clean sand, n = 2.68), '
        'd|σ^s|/dψ flips negative past ψ_peak = [α_vG (n − 2)^(1/n)]^(−1) = 7.964 kPa. Notice the modeling boundaries: α_vG is '
        'in kPa^−1, γ is held constant rather than varying as γ(θ), and ψ is prescribed uniformly at z = 2.0 m.'
    ),
    'act2_deepening': (
        'Keeping Bishop\'s effective-stress weighting equal to S_e rather than 1.0 resolves both ends of unsaturated failure. '
        'In saturated soil (ψ = 0), S_e = 1 and σ^s = 0 recover Terzaghi\'s equation directly; below the water table (ψ < 0, '
        'u_w > u_a), positive pore-water pressure reduces σ\'_n = σ_n − u_w. Conversely, applying χ = 1.0 across dry sand at '
        'ψ = 40.0 kPa ignores that only 5.2% of the effective pore space still holds water (S_e = 0.052), fabricating 40.0 kPa '
        'of tensile strength instead of 2.08 kPa and turning an unstable 36° sand slope (FS = 0.936) into a misleading '
        'FS = 2.320. Note also that Mualem\'s K_r(S_e) exhibits a steep slope dK_r/dψ → −∞ near ψ → 0+ when 1 < n < 2, '
        'requiring careful numerical clamping near saturation.'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Storm Wetting Collapse While Still Unsaturated): Keep Slope Inclination β = 34.0° and drag Matric '
            'Suction ψ downward from 24.0 kPa toward 2.0 kPa. Watch K_r surge from 0.1662 to 0.7308 while σ^s weakens from '
            '−21.69 kPa to −2.00 kPa and FS drops from 1.557 to 0.962 (< 1.0) while pore water is still in tension.'
        ),
        (
            'Experiment 2 (Full Saturation Limit ψ = 0 kPa & Drained Angle β ≤ 28°): Set ψ = 0.0 kPa to verify the saturated '
            'limit (S_e = 1.000, K_r = 1.0000, σ^s = 0.00 kPa, FS = 0.902 at β = 34°). Now drag β down below φ\' = 28.0° '
            'toward 24.0° and watch FS stay above 1.2 even at zero suction.'
        ),
        (
            'Experiment 3 (Exponent n > 2 Non-Monotonic Sand & 4-Lens Observatory): Compare silty loam (n = 1.60, monotonic '
            '|σ^s|) with the clean-sand benchmark (n = 2.68, peak |σ^s| = 4.52 kPa at ψ = 7.964 kPa, dropping to 2.08 kPa at '
            'ψ = 40.0 kPa), and inspect the 4-Lens Observatory tabs (3D Surface, Phase Portraits, Kirchhoff Ribbon, Polar Radar).'
        ),
    ],
    'act4_title': 'Act IV — Imagining Humanity\'s Future: Falsifiable Hillslope Warning & Open Geotechnics',
    'act4_human_ai': (
        'Shallow landslides triggered by intense storms threaten hillside neighborhoods, mountain highways, and earthen '
        'embankments worldwide. Making vadose-zone suction math inspectable—separating pore-retention shape (S_e), '
        'hydraulic conductivity amplification during wetting (K_r), and capillary clamping (σ^s = −S_e ψ)—lets civil engineers, '
        'hydrologists, and automated verification scripts test boundary assumptions openly rather than treating hillslopes '
        'as black boxes. This folio states an explicit Tier T1–T2 screening hypothesis with clear physical limits.'
    ),
    'act4_deepening': (
        'Under the Tier T1–T2 hypothesis framed here, shallow unsaturated hillslopes with β > φ\' depend on S_e ψ to remain '
        'above FS = 1.0 and lose equilibrium as wetting raises S_e toward the air-entry zone before positive pore pressure '
        'develops, whereas clean sands (n > 2) lose capillary strength on drying as well. This 1D steady-suction hypothesis '
        'is explicitly falsified in any catchment where 3D topographic convergence, preferential macropore or root-pipe flow '
        '(Iverson 2000, DOI 10.1029/2000WR900090), wetting-versus-drying SWCC hysteresis, bedrock artesian exfiltration, or '
        'woody-root mechanical cohesion controls slip timing. Pairing deterministic Python verifiers with a χ = 1.0 planted '
        'defect keeps dry-soil stability illusions from passing automated checks.'
    ),
    'cf_bridge': 'Continues E.05/E.13',
    'sources': [
        (
            'Mualem, Y. (1976). A new model for predicting the hydraulic conductivity of unsaturated porous media. '
            'Water Resources Research, 12(3), 513–522. DOI: 10.1029/WR012i003p00513.'
        ),
        (
            'Fredlund, D. G., Morgenstern, N. R., & Widger, R. A. (1978). The shear strength of unsaturated soils. '
            'Canadian Geotechnical Journal, 15(3), 313–321. DOI: 10.1139/t78-029.'
        ),
        (
            'van Genuchten, M. Th. (1980). A Closed-form Equation for Predicting the Hydraulic Conductivity of Unsaturated Soils. '
            'Soil Science Society of America Journal, 44(5), 892–898. DOI: 10.2136/sssaj1980.03615995004400050002x.'
        ),
        (
            'Iverson, R. M. (2000). Landslide triggering by rain infiltration. Water Resources Research, 36(7), 1897–1910. '
            'DOI: 10.1029/2000WR900090.'
        ),
        (
            'Lu, N., & Godt, J. W. (2008). Infinite slope stability under steady unsaturated seepage conditions. '
            'Water Resources Research, 44(11), W11404. DOI: 10.1029/2008WR006976.'
        ),
        (
            'Lu, N., Godt, J. W., & Wu, D. T. (2010). A closed-form equation for effective stress in unsaturated soil. '
            'Water Resources Research, 46(5), W05515. DOI: 10.1029/2009WR008646.'
        ),
        (
            'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and '
            'classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
            '882–898. DOI: 10.1162/qss_a_00146.'
        ),
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Lu-Godt-Wu suction stress curves comparing '
        'monotonic silty loam (n = 1.60) and non-monotonic clean sand (n = 2.68) with infinite-slope stability marker">\n'
        '            <line x1="48" y1="184" x2="352" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <line x1="48" y1="30" x2="48" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <text x="54" y="22" font-size="10.5" font-weight="600" fill="currentColor">Suction Stress |σ^s| vs. Matric Suction ψ</text>\n'
        '            <path d="M 48 184 Q 130 140 210 104 T 348 44" fill="none" stroke="var(--tp-prussian)" stroke-width="2.4"/>\n'
        '            <path d="M 48 184 Q 68 148 86 154 T 190 176 L 348 181" fill="none" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="5,3"/>\n'
        '            <circle id="tp-svg-eng-point" cx="108" cy="139" r="6" fill="var(--tp-verdigris)"/>\n'
        '            <text x="190" y="64" font-size="9" fill="var(--tp-prussian)">Silty Loam (n = 1.60, monotonic)</text>\n'
        '            <text x="122" y="168" font-size="9" fill="var(--tp-minium)">Clean Sand (n = 2.68, peak 7.96 kPa)</text>\n'
        '            <line x1="372" y1="24" x2="372" y2="192" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="388" y="22" font-size="10.5" font-weight="600" fill="currentColor">Wetting vs. Dry Sand Benchmarks</text>\n'
        '            <rect x="388" y="42" width="256" height="58" rx="6" fill="var(--tp-stone)" fill-opacity="0.28" stroke="var(--tp-prussian)" stroke-width="1.6"/>\n'
        '            <text x="400" y="64" font-size="9.5" font-weight="600" fill="var(--tp-prussian)">Loam ψ = 24 kPa, β = 34° → FS = 1.557</text>\n'
        '            <text x="400" y="84" font-size="9" fill="var(--tp-verdigris)">Wetting ψ = 2 kPa → FS = 0.962 (&lt; 1.0)</text>\n'
        '            <rect x="388" y="114" width="256" height="56" rx="6" fill="var(--tp-verdigris)" fill-opacity="0.12" stroke="var(--tp-verdigris)" stroke-width="1.4"/>\n'
        '            <text x="400" y="136" font-size="9.5" font-weight="600" fill="var(--tp-prussian)">Sand ψ = 40 kPa → S_e = 0.052, FS = 0.936</text>\n'
        '            <text x="400" y="156" font-size="9" fill="var(--tp-minium)">Defect χ = 1.0 inflates FS to 2.320</text>\n'
        '            <text x="48" y="206" font-size="10" fill="var(--tp-verdigris)">Steady-suction infinite-slope model · Recomputed by verify_e14_unsaturated_suction.py</text>\n'
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining what a laboratory unsaturated silty-loam rainfall infiltration flume with '
        'overhead brass misting nozzles, a Prussian-slate wetting front, verdigris capillary sheen above a basal '
        'drainage screen, tensiometer probes, and a companion quartz-sand column would look like (artistic impression, '
        'not a measured field profile)'
    ),
    'caption': (
        'Conceptual Vision Plate E.14-V (Imagining What It Would Look Like) · Artistic laboratory view imagining a tilted '
        'silty-loam rainfall-infiltration flume and companion clean-sand column. Governing equations and factor-of-safety '
        'bounds are kept intact in deterministic Plate E.14-A and the offline verifier below.'
    ),
}

DISPATCH = {
    'kicker': 'FRONTIER GEOTECHNICAL DISPATCH · VADOSE SUCTION & RAINFALL LANDSLIDES',
    'headline': 'Lu–Godt–Wu Suction Stress, van Genuchten Exponent n & Unsaturated Slope Collapse',
    'body': (
        'Why do steep unsaturated hillslopes fail before pore water turns positive, while dry clean sands lose capillary '
        'cohesion? Coupling van Genuchten–Mualem retention (1976, 1980) with Lu, Godt & Wu suction stress (2010, '
        'DOI 10.1029/2009WR008646) separates monotonic silty loam (n = 1.60; FS drops from 1.557 at ψ = 24 kPa to 0.962 '
        'at ψ = 2 kPa) from non-monotonic clean sand (n = 2.68; FS = 0.936 at ψ = 40 kPa).'
    ),
}

META_3D = (
    'Unsaturated Suction Stress & Infinite-Slope Stability Surface',
    'X: Matric Suction ψ (kPa) · Z: Slope Angle β (°) · Y: Factor of Safety Margin FS − 1',
)

ES_TRANSLATION = {
    'title_es': 'Esfuerzo de Succión en Suelos No Saturados, Retención de van Genuchten–Mualem e Inestabilidad de Laderas',
    'subtitle_es': (
        'Continuación de los Folios E.05 y E.13: estudio geotécnico ilustrativo que acopla la retención de van Genuchten–Mualem '
        'S_e(ψ) y K_r(S_e), el esfuerzo de succión cerrado de Lu–Godt–Wu σ^s = −S_e ψ y el factor de seguridad FS en ladera infinita.'
    ),
    'why_es': (
        'Como los puentes de agua que sostienen un castillo de arena húmeda, la succión mátrica sujeta las partículas del suelo '
        'por encima del nivel freático; cuando la lluvia satura los poros, ese agarre capilar cae incluso antes de haber presión positiva.'
    ),
    'plain_es': (
        'En palabras sencillas, el suelo sobre el manto freático no está seco ni inundado: conserva diminutos meniscos de agua '
        'entre los granos que tiran hacia adentro como ligas microscópicas. Ese tirón capilar aporta resistencia adicional que '
        'puede sostener una ladera más empinada que su ángulo de fricción drenado. Al infiltrarse agua de lluvia intensa, los '
        'poros se llenan, los meniscos pierden curvatura y el factor de seguridad cae por debajo de 1.0 incluso cuando el agua '
        'de poro sigue en tensión.'
    ),
    'deep_es': (
        'En el modelo de van Genuchten (1980, DOI 10.2136/sssaj1980.03615995004400050002x) y Mualem (1976, '
        'DOI 10.1029/WR012i003p00513), la saturación efectiva es S_e(ψ) = [1 + (α_vG ψ)^n]^(−m) con m = 1 − 1/n (n > 1). '
        'Lu, Godt y Wu (2010, DOI 10.1029/2009WR008646) definen el esfuerzo de succión σ^s = −S_e ψ ≤ 0: en suelo franco limoso '
        '(n = 1.60 ≤ 2, α_vG = 0.02 kPa^−1, γ = 19.0 kN/m^3, c\' = 2.0 kPa, φ\' = 28.0°, z = 2.0 m, β = 34.0°), ψ = 24.0 kPa '
        'da S_e = 0.904, K_r = 0.1662, σ^s = −21.69 kPa y FS = 1.557, bajando a FS = 0.962 en ψ = 2.0 kPa (Lu y Godt 2008, '
        'DOI 10.1029/2008WR006976). En arena limpia (n = 2.68 > 2, α_vG = 0.145 kPa^−1, γ = 18.0 kN/m^3), |σ^s| alcanza un pico '
        'de 4.52 kPa en ψ = 7.964 kPa y cae a 2.08 kPa en ψ = 40.0 kPa (FS = 0.936 a β = 36°, frente a 2.320 con el defecto χ = 1.0). '
        'El modelo fija ψ uniforme y γ constante en el plano de falla. Esta hipótesis de nivel T1–T2 queda falsada donde el flujo '
        'topográfico 3D, macroporos (Iverson 2000, DOI 10.1029/2000WR900090), histéresis o cohesión de raíces controlen el deslizamiento.'
    ),
    'bridge_es': (
        'Ponderar la succión mátrica con S_e (σ^s = −S_e ψ) separa la falla por humedecimiento en limos de la pérdida de puentes '
        'capilares al secarse una arena limpia (modelo ilustrativo de succión estacionaria).'
    ),
}
