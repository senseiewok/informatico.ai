#!/usr/bin/env python3
"""Folio A.03 (ARCHITECTURE): Double-Skin Facade Buoyancy Stack Ventilation, Cavity Plumes, and 1:5 Acoustic Damper Louvers."""
from __future__ import annotations

SLUG = 'a03'

PILLAR = 'architecture'

FOLIO = {
    'folio_id': 'A.03',
    'slug': 'a03',
    'pillar': 'architecture',
    'category_code': 'A',
    'title': 'Double-Skin Facade Buoyancy Stack Ventilation, Cavity Plumes, and 1:5 Acoustic Damper Louvers',
    'subtitle': (
        'An explanatory model—not a facade design method—of buoyancy stack draft and solar shading '
        'position inside multi-story ventilated glass cavities, and how such a cavity could carry heat away.'
    ),
    'date_published': '2026-10-30',
    'date_redated': '2026-11-14',
    'current_edition': 'REV 1.3',
    'status_badge': 'REDATED REV 1.3',
    'primary_kernel': 'tools/tectonic_verify.py',
    'governing_law': 'Δp_stack = ρ_0 g H (ΔT / T_ext) · g_tot = 0.11 (assumed)',
    'colophon': {
        'identifier': 'A.03 · Facade Thermodynamics',
        'kernels': '1:50 Multi-Story Shaft + 1:5 Damper Sill',
        'benchmarks': 'Model values: Δp = 3.92 Pa (ρ_0 = 1.2 kg/m³, H = 9.0 m, ΔT = 11.2 K, T_ext ≈ 303 K) · g_tot = 0.11 fixed text',
        'bridge': 'Buoyancy Convective Clearance',
    },
    'steps': [
        (
            'Stage 1 (Solar Shortwave Absorption): An assumed solar irradiance I_sol = 650 W/m² heats the ventilated '
            'blind positioned in the outer third of the 600 mm cavity.'
        ),
        (
            'Stage 2 (Hydrostatic Buoyancy Pressure Drive): Δp_stack = ρ_0 g H (ΔT / T_ext) = 1.2 × 9.81 × 9.0 × '
            '(11.2 / 303) = 3.92 Pa across a 9.0 m two-story shaft (ideal-gas β ≈ 1 / T_ext, T_ext ≈ 303 K, about 30 °C, assumed).'
        ),
        (
            'Stage 3 (Bernoulli Discharge & Damper Loss Balance): Setting Δp = ζ_tot ρ v² / 2 gives v = 0.84 m/s for '
            'an assumed total loss coefficient ζ_tot ≈ 9.3. The 142 m³/h per meter of facade assumes an opening of about 0.047 m² per meter.'
        ),
        (
            'Stage 4 (1:5 Acoustic Baffle Sill Node A-12): A proposed mineral-wool lined labyrinth damper with design '
            'targets of R_w = 46 dB and C_d = 0.62 (targets, not measured).'
        ),
    ],
    'readouts': [
        {'label': 'Buoyancy Stack Draft (Δp, Model)', 'value': '3.92 Pa'},
        {'label': 'Induced Cavity Velocity (Model)', 'value': '0.84 m/s (142 m³/h·m)'},
        {'label': 'Total Solar Factor (g_tot, Fixed Text)', 'value': '0.11 (assumed; EN ISO 52022-3 method)'},
        {'label': 'Rescaled ACH & Fixed Daylight (Illustrative)', 'value': '24.21 ACH · 285 EML (illustrative)'},
    ],
    'spec_plate': {
        'division': 'EXPLANATORY MODEL · CSI 08 44 13 / 08 91 00 (NOT A DESIGN SPEC)',
        'title': 'Illustrative Box-Window Curtain Wall & Acoustic Sill Concept (Node A-12)',
        'body': (
            'Explanatory proposal only, not a tested product or design specification: ventilated box-window cavity with '
            'motorized aluminum blinds and sound-attenuating intake sill (assumed/target values: U_cw = 0.68 W/(m²·K), '
            'g_tot = 0.11, R_w = 46 dB). None of these numbers may be used on a real building.'
        ),
        'meta': 'Explanatory proposal, not a product · EN 13830 is the curtain-walling product standard a real system would be tested to',
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE A.03-A · BLIND POSITIONING PARADOX',
        'body': (
            'A blind placed close to the inner glazing may pass more absorbed heat indoors; moving it toward the outer skin '
            'could let more heat leave with cavity air. Saelens, Roels, and Hens compare multiple-skin facade strategies '
            '(DOI 10.1016/j.buildenv.2006.06.024). The outer-third position here is an assumed parameter.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE A.03-B · ILLUSTRATIVE ASSEMBLY & SAFETY BOUNDARY',
        'body': (
            'This folio is an explanation, not a facade design method, and remains untested on hardware. Assumed '
            'envelope and acoustic target values on this page may not be used to design or size a real structure.'
        ),
    },
    'skill': {
        'filename': 'double-skin-facade-buoyancy-SKILL.md',
        'name': 'double-skin-facade-buoyancy',
        'description': (
            'Explanatory building-physics reference (not a facade design method) for double-skin curtain-wall buoyancy '
            'stack draft, EN ISO 52022-3 g_tot concepts, and acoustic intake dampers.'
        ),
        'rules': [
            'Explanatory, untested model only, not a facade design method: none of these numbers may be used to design or size a real building or curtain wall.',
            'Under stated assumptions, estimate hydrostatic stack draft delta_p_stack = rho_0 * g * H * (T_cav - T_ext) / T_ext (ideal-gas beta = 1 / T_ext; baseline assumes rho_0 = 1.2 kg/m^3, T_ext about 303 K, zeta_tot about 9.3, opening area A about 0.047 m^2/m), cavity speed v = sqrt(2 * delta_p_stack / (zeta_tot * rho_0)), and mass flow m_dot = rho_0 * A * v = A * sqrt(2 * rho_0 * delta_p_stack / zeta_tot).',
            'Calculate total solar energy transmittance g_tot with the EN ISO 52022-3 method; this folio uses an illustrative target g_tot <= 0.15 above 500 W/m^2 (not a requirement of the standard), and in the browser lab g_tot = 0.11 and 285 EML remain fixed text while 24.21 ACH rescales with velocity.',
            'This folio assumes a cavity depth D >= 500 mm for maintenance access (an assumed parameter, not a code requirement), or sealed dry-air Closed Cavity Facade (CCF) modules.',
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.3',
            'date': '2026-11-14',
            'summary': (
                'REV 1.3 (Redated 2026-11-14): Grounding revision. No design was certified and no pathogen clearance '
                'measured; earlier claims of protected sleep and immunity are withdrawn. Circadian light sentences cite '
                'Berson et al. (2002; DOI 10.1126/science.1067262) and Brown et al. (2022; DOI 10.1371/journal.pbio.3001571). '
                'Stack draft assumptions (T_ext ≈ 303 K, ζ_tot ≈ 9.3), browser readout rescaling versus fixed text, and '
                'the non-design-method boundary are stated explicitly.'
            ),
            'opus': (
                'Review: Crossref metadata checked for all six DOIs; Scite index checked for Nabil & Mardaljevic '
                '(2006; DOI 10.1016/j.enbuild.2006.03.013). Brown et al. (2022) recommends at least 250 lux melanopic '
                'EDI indoors during daytime for healthy adults.'
            ),
        },
        {
            'edition': 'REV 1.2',
            'date': '2026-11-02',
            'summary': (
                'REV 1.2 (Redated 2026-11-02): Added a double-skin facade cavity buoyancy model with illustrative '
                'air-change and solar factor values.'
            ),
            'opus': (
                "Cross-model check of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier 'verified' wording "
                '(and its Δp = 4.2 Pa, which the formula does not give) is withdrawn in REV 1.3.'
            ),
        },
        {
            'edition': 'REV 1.1',
            'date': '2026-11-01',
            'summary': (
                'REV 1.1 (Redated 2026-11-01): Added CSI 08 44 13 acoustic labyrinth sill detail and EnergyPlus BSDF '
                'optical matrix parameters.'
            ),
            'opus': (
                "Cross-model check of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier 'verified' ζ_tot = 6.85 "
                'is withdrawn in REV 1.3; v = 0.84 m/s needs ζ_tot ≈ 9.3.'
            ),
        },
        {
            'edition': 'REV 1.0',
            'date': '2026-10-30',
            'summary': 'REV 1.0 (Published 2026-10-30): Initial thermosiphon double-skin facade stack ventilation monograph.',
            'opus': "Cross-model check of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier 'verified' wording is withdrawn in REV 1.3.",
        },
    ],
    'reading_time': '22 MIN READ',
    'word_count': '4,650 WORDS',
    'scite': {
        'doi': '10.1016/j.enbuild.2006.03.013',
        'fetched_on': '2026-11-08',
        'citing_publications': 864,
        'supporting': 2,
        'mentioning': 334,
        'contrasting': 0,
        'retracted': False,
        'summary': (
            'Scite index entry for Nabil & Mardaljevic, Useful daylight illuminances (DOI 10.1016/j.enbuild.2006.03.013), '
            'checked 2026-11-08: 864 citing publications (2 supporting, 334 mentioning, 0 contrasting) and no retraction '
            "notice. The paper is about daylight metrics; it does not check this folio's stack-draft numbers or make circadian claims."
        ),
    },
    'volume': 2,
    'volume_code': 'VOL. 02',
    'sliders': [
        {
            'label': 'Double-Skin Cavity Stack Height (H)',
            'min': 3.5,
            'max': 18.0,
            'step': 0.5,
            'value': 9.0,
            'unit': ' m',
        },
        {
            'label': 'Solar Cavity Temperature Rise (ΔT_cav)',
            'min': 2.0,
            'max': 20.0,
            'step': 0.4,
            'value': 11.2,
            'unit': ' K',
        },
    ],
}

_ACT1_DROPCAP = (
    'Across the hot, dry cities of the Iranian plateau, builders in Yazd raised tall masonry windcatchers called '
    'badgirs above courtyard houses. When afternoon breezes dropped, solar warmth stored in the masonry walls could '
    'heat air inside the shaft and draw warm air upward out of the rooms below. In some houses, those shafts worked '
    'alongside underground water channels known as qanats. How old the earliest windcatchers might be remains '
    'uncertain, and this folio does not date them. Centuries later, architects such as Norman Foster at the '
    'Commerzbank headquarters in Frankfurt (1997) adapted passive stack ventilation to tall glazed office towers. '
    'Two layers of glass enclose an aired outer cavity holding adjustable solar blinds that may intercept sun before '
    'it enters the room. This folio presents an explanatory model of that buoyancy draft, not a facade design method.'
)

_ACT1_BODY = (
    'Double-skin facades try to balance admitting daylight against limiting solar heat gain. When shading sits inside '
    'the ventilated gap, rising cavity air could carry part of the absorbed solar heat away before it crosses the '
    'inner glazing; Saelens, Roels, and Hens compare multiple-skin facade energy strategies (Building and Environment, '
    'DOI 10.1016/j.buildenv.2006.06.024). Nabil and Mardaljevic proposed Useful Daylight Illuminance to measure how '
    'often indoor daylight falls within a useful range (Energy and Buildings, DOI 10.1016/j.enbuild.2006.03.013). '
    'Separately, Berson, Dunn, and Takao showed that intrinsically photosensitive retinal ganglion cells set the '
    'circadian clock (Science, DOI 10.1126/science.1067262), and Brown et al. (2022; PLOS Biology, DOI '
    '10.1371/journal.pbio.3001571) recommended at least 250 lux melanopic EDI at eye level indoors during daytime for '
    'healthy adults. A reader could simulate cavity convection with DedalusProject/dedalus '
    '(https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068); this folio did not.'
)

_ACT2_INTUITION = (
    'Under the ideal-gas Boussinesq approximation (beta ≈ 1 / T_ext), solar heat absorbed by intermediate blinds warms '
    'the cavity air column and creates hydrostatic stack pressure Delta P_stack = rho_0 * g * H * (Delta T / T_ext). '
    'Under stated assumptions (rho_0 = 1.2 kg/m^3, H = 9.0 m, Delta T = 11.2 K, T_ext = 303 K), the formula estimates '
    '3.92 Pa. Balancing that drive against an assumed total loss coefficient of about 9.3 across inlet and outlet '
    'louvers gives cavity speed 0.84 m/s (142 m^3/h per meter of width for an opening of about 0.047 m^2/m). A '
    'separate worked example in tectonic_verify.py sets H = 4.5 m, Delta T = 8 K, and T_0 = 293.15 K (20 °C), giving '
    'sqrt(2 g H Delta T / T_0) = 1.55 m/s and Q = 0.363 m^3/s across C_d A = 0.234 m^2: 24.21 air changes per hour in '
    'an assumed 54 m^3 room, or about 6.4 in an assumed 204 m^3 room. The browser readout mixes those two model setups '
    'by rescaling 24.21 ACH with v / 0.84, while g_tot = 0.11 (EN ISO 52022-3 method) and 285 EML stay fixed text. '
    'Separately, Raman et al. (2014; DOI 10.1038/nature13883) studied photonic sky cooling; this folio does not '
    'simulate that device or claim pathogen clearance.'
)

LONGFORM_DATA = {
    'reading_time': '22 MIN READ',
    'history_lead': _ACT1_DROPCAP,
    'history_body': _ACT1_BODY,
    'pullquote': (
        'Explanatory statement of this folio, not a finding: a shaded double-skin cavity is modeled here as a '
        'buoyancy-driven air path that could carry part of the absorbed solar heat away; none of its numbers may be '
        'used on a real building.'
    ),
    'pullquote_cite': 'Editorial Synthesis · From Persian Badgirs to an Explanatory Stack-Draft Model',
    'chronology': [
        (
            'Date uncertain',
            'Builders of the Iranian Plateau (e.g. Yazd)',
            'Use badgir windcatchers, in some houses paired with underground qanat channels.',
        ),
        (
            '2002',
            'David Berson et al.',
            'Show that intrinsically photosensitive retinal ganglion cells set the circadian clock (DOI 10.1126/science.1067262).',
        ),
        (
            '2014',
            'Raman & Fan (Stanford)',
            'Demonstrate passive radiative cooling below ambient air temperature under direct sunlight (DOI 10.1038/nature13883).',
        ),
        (
            '2026',
            'Informatico.ai Folio A.03',
            'Explanatory stack-draft model (Δp = 3.92 Pa) with rescaled ACH and fixed-text daylight readouts; not a design method.',
        ),
    ],
    'intuition_lead': _ACT2_INTUITION,
    'intuition_body': (
        'In the separate 4.5 m and 8 K example (T_0 = 293.15 K, C_d A = 0.234 m^2), Q = 0.363 m^3/s gives 24.21 air '
        'changes per hour in 54 m^3 (or about 6.4 in 204 m^3); R_w = 46 dB is an unverified sill target.'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Trace the 4 Stages): Click Stages 1 -> 4 below to follow blind heating, hydrostatic stack '
            'pressure, Bernoulli damper loss balance, and the proposed 1:5 acoustic sill.'
        ),
        (
            'Experiment 2 (Inspect the Solar Chimney Schematic): Review the SVG schematic below; its Q = 0.363 m³/s '
            'label comes from the separate 4.5 m worked example, and the sky-cooler bar is conceptual.'
        ),
        (
            'Experiment 3 (Read the Readout Strip): Stack draft, cavity speed, and m³/h·m flow follow the two sliders; '
            '24.21 ACH rescales linearly with speed from an illustrative baseline, while g_tot = 0.11 and 285 EML stay fixed text.'
        ),
    ],
    'human_ai_shift': (
        'A reader studying cavity convection alongside whole-building energy loads could pair an open spectral solver '
        'such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) '
        'with NREL/EnergyPlus. This folio names those tools as options; it simulated neither.'
    ),
    'sources': [
        'Berson, D. M., Dunn, F. A., & Takao, M. (2002). Phototransduction by retinal ganglion cells that set the circadian clock. Science, 295(5557), 1070–1073. DOI: 10.1126/science.1067262.',
        'Brown, T. M., et al. (2022). Recommendations for daytime, evening, and nighttime indoor light exposure to best support physiology, sleep, and wakefulness in healthy adults. PLOS Biology, 20(3), e3001571. DOI: 10.1371/journal.pbio.3001571.',
        'Raman, A. P., Anoma, M. A., Zhu, L., Rephaeli, E., & Fan, S. (2014). Passive radiative cooling below ambient air temperature under direct sunlight. Nature, 515, 540–544. DOI: 10.1038/nature13883.',
        'Saelens, D., Roels, S., & Hens, H. (2008). Strategies to improve the energy performance of multiple-skin facades. Building and Environment, 43(4), 638–650. DOI: 10.1016/j.buildenv.2006.06.024.',
        'Nabil, A., & Mardaljevic, J. (2006). Useful daylight illuminances: A replacement for daylight factors. Energy and Buildings, 38(7), 905–913. DOI: 10.1016/j.enbuild.2006.03.013.',
        'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). Dedalus: A flexible framework for numerical simulations with spectral methods (DedalusProject/dedalus, https://github.com/DedalusProject/dedalus). Physical Review Research, 2(2), 023068. DOI: 10.1103/PhysRevResearch.2.023068.',
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Double-skin solar chimney thermosiphon and 8-13 um radiative sky cooling">\n'
        '            <rect x="110" y="30" width="22" height="160" fill="none" stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '            <rect x="170" y="30" width="420" height="160" fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-width="2"/>\n'
        '            <line x1="150" y1="175" x2="150" y2="42" stroke="var(--tp-minium)" stroke-width="3" stroke-dasharray="5,3"/>\n'
        '            <path d="M 55 75 L 170 110 L 390 65" fill="none" stroke="var(--tp-prussian)" stroke-width="2.5"/>\n'
        '            <line x1="380" y1="30" x2="540" y2="30" stroke="var(--tp-verdigris)" stroke-width="5"/>\n'
        '            <text x="45" y="65" font-size="11" fill="var(--tp-prussian)">Daylight (285 EML, fixed text)</text>\n'
        '            <text x="68" y="205" font-size="11" fill="var(--tp-minium)">Solar Chimney ↑ Q = 0.363 m³/s (4.5 m worked example)</text>\n'
        '            <text x="370" y="20" font-size="11" fill="var(--tp-verdigris)">8–13 μm Radiative Sky Cooler (concept)</text>\n'
        '          </svg>'
    ),
    'scite': FOLIO['scite'],
    'word_count': '4,650 WORDS',
    'act1_dropcap': _ACT1_DROPCAP,
    'act1_plain_bridge': (
        'Summer sun turns a parked car into an oven. Clear glass welcomes daylight indoors, yet it traps solar warmth '
        'like a greenhouse and raises afternoon cooling loads. A double-skin facade adds an outer pane of glass in '
        'front of the main wall, leaving a ventilated corridor holding adjustable blinds. Sunlight warms those blinds '
        'first. The surrounding cavity air heats up, becomes lighter than outdoor air, and could rise out through top '
        'vents before warming the room. This page is an explanation, not a facade design method. None of its numbers '
        'may be used on a real building. Under stated assumptions, the algebraic formula estimates only upward stack '
        'pressure and cavity air speed, and does not simulate comfort, noise, or daylight. Airflow and daylight '
        'figures on the strip are illustrative, and their effects remain untested here.'
    ),
    'act1_body': _ACT1_BODY,
    'act1_stakes': (
        'Glazed curtain walls admit daylight while trapping solar heat, raising cooling demand in sealed buildings. '
        'Opening ordinary windows may admit street noise, wind gusts, and rain. Conversely, if a double-skin cavity '
        'is too narrow or its blinds sit too close to the inner pane, cavity air might overheat, raise thermal stress '
        'on the glass, and let warm air pass back indoors.'
    ),
    'act2_analogy': (
        'Everyday analogy: Picture a wood-burning stove on a cold winter morning. Its tall flue pulls smoke upward '
        'without an electric fan because warm air inside the pipe weighs less than cold outdoor air. A double-skin '
        'facade borrows that buoyancy lift inside a glazed wall shaft. Where the picture stops: a stove flue vents '
        'hot exhaust through an opaque pipe without wind gusts, glazing heat loss, or daylight glare, and this page '
        'estimates only idealized hydrostatic draft.'
    ),
    'act2_plain_primer': (
        'In the interactive laboratory below, two sliders adjust Double-Skin Cavity Stack Height and Solar Cavity '
        'Temperature Rise across the outer glazed shaft. Raising Double-Skin Cavity Stack Height lengthens the warm '
        'air column and scales upward stack pressure in direct proportion. Raising Solar Cavity Temperature Rise '
        'makes air inside the 600-millimeter cavity lighter, increasing both stack pressure and upward air speed. '
        'In the browser script, stack draft, cavity air speed, and hourly flow per meter update from those two '
        'sliders, air changes per hour rescale with air speed from a separate room example, and the solar factor and '
        'daylight readout stay fixed text.'
    ),
    'distill_diagram': {
        'analogy_title': 'Wood Stove Thermal Chimney Draft',
        'analogy_sub': 'Warm buoyant air column rises up the glazed outer shaft',
        'force_a_title': 'Cavity Stack Height (H)',
        'force_a_sub': 'Taller glazed shaft scales hydrostatic stack pressure linearly',
        'force_b_title': 'Cavity Temp Rise (ΔT_cav)',
        'force_b_sub': 'Warmer cavity air lowers density and drives upward flow',
        'threshold_title': 'Louver Friction & Solar Factor Balance',
        'threshold_pass': 'Thermosiphon draft balances assumed louver losses; steady cavity flow (model)',
        'threshold_fail': 'Higher damper resistance lowers cavity velocity for a given stack pressure',
    },
    'act2_intuition': _ACT2_INTUITION,
    'act2_deepening': (
        'Hydrostatic stack pressure grows linearly with height H and temperature rise Delta T, whereas volumetric '
        'flow Q = C_d * A * sqrt(2 * Delta P / rho) grows only with the square root of pressure. Faster upward flow '
        'could also shorten the contact time during which air absorbs heat from the blinds—a feedback loop this model '
        'does not simulate. Micro-perforated aluminum louvers are proposed only conceptually and are not simulated '
        'optically or thermally. At the proposed 1:5 acoustic sill node, lined baffles might attenuate street noise '
        '(46 dB is a design target, not verified by measurement), while their added flow resistance lowers cavity '
        'air velocity rather than hydrostatic stack pressure.'
    ),
    'act4_deepening': (
        'A proposal, not a description of current practice: weather forecasts could adjust louver angles and dampers '
        'ahead of solar peaks, while light sensors could help balance daylight against glare at desks. Whether '
        'closed-cavity facades with dry-air purging might limit interstitial condensation and dust in humid tropical '
        'climates remains untested here.'
    ),
    'act4_human_ai': (
        'A reader studying cavity convection alongside whole-building energy loads could pair an open spectral solver '
        'such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) '
        'with NREL/EnergyPlus. This folio names those tools as options; it simulated neither.'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining what a multi-story double-skin glass facade buoyancy stack shaft paired '
        'with circadian solar shading louvers and acoustic intake baffles would look like (artistic impression, not a measured structure)'
    ),
    'caption': (
        'Conceptual Vision Plate A.03-V (Imagining What It Would Look Like) · Artistic architectural cutaway '
        'imagining a multi-story ventilated double-skin curtain wall shaft driving thermosiphon buoyancy exhaust '
        '(Delta_p = 3.92 Pa) across circadian daylight shading louvers (g_tot = 0.11).'
    ),
}

DISPATCH = {
    'kicker': 'FRONTIER FACADE & PHOTOBIOLOGY DISPATCH · BUOYANCY STACKS & CIRCADIAN DAYLIGHTING',
    'headline': 'Double-Skin Curtain Wall Buoyancy: An Explanatory Stack-Draft Model Beside Daylight Metrics',
    'body': (
        "Drawing on Saelens, Roels, and Hens's comparison of multiple-skin facade strategies (Building and Environment "
        "DOI 10.1016/j.buildenv.2006.06.024), Nabil and Mardaljevic's Useful Daylight Illuminance (DOI "
        '10.1016/j.enbuild.2006.03.013), and the daytime light recommendation of Brown et al. (DOI '
        '10.1371/journal.pbio.3001571), this folio models a 9.0 m cavity with an estimated stack draft of 3.92 Pa '
        'under stated assumptions. Its air-change and daylight readouts are illustrative, and it makes no health claim.'
    ),
}

META_3D = (
    'Double-Skin Facade Buoyancy Plume Canyon',
    'X: Glazed Cavity Depth · Z: Stack Elevation H · Y: Solar Thermosiphon Velocity & ACH Plume',
)

ES_TRANSLATION = {
    'title_es': (
        'Ventilación por Tiro de Flotabilidad en Fachadas de Doble Piel, Plumas en la Cavidad y Rejillas Acústicas '
        'Amortiguadoras 1:5'
    ),
    'subtitle_es': (
        'Un modelo explicativo—no un método de diseño de fachadas—del tiro por flotabilidad y la posición de la '
        'protección solar en cavidades acristaladas ventiladas de varios niveles.'
    ),
    'why_es': (
        'Una chimenea solar acristalada usa el calor absorbido en las persianas para elevar el aire caliente de la '
        'cavidad en un modelo algebraico simplificado.'
    ),
    'plain_es': (
        'El sol de verano convierte un automóvil estacionado en un horno. El vidrio transparente deja pasar la luz '
        'del día, pero retiene el calor solar como un invernadero y eleva la carga de enfriamiento. Una fachada de '
        'doble piel añade una lámina exterior de vidrio frente al muro principal, dejando un corredor ventilado con '
        'persianas ajustables. El sol calienta primero esas persianas. El aire cercano en la cavidad se calienta, se '
        'vuelve más ligero que el aire exterior y puede subir hacia las rejillas superiores antes de calentar el '
        'cuarto. Este folio es una explicación, no un método de diseño de fachadas. Ninguno de sus números debe '
        'usarse en un edificio real. Bajo supuestos explícitos, la fórmula estima solo la presión ascendente y la '
        'velocidad del aire en la cavidad, sin medir confort, ruido ni luz.'
    ),
    'deep_es': (
        'Este folio es una explicación, no un método de diseño de fachadas, y ninguno de sus números debe usarse en '
        'una estructura real. Bajo la aproximación de gas ideal (β ≈ 1 / T_ext), la altura H y la elevación de '
        'temperatura ΔT producen una presión hidrostática Δp_stack = ρ_0 g H (ΔT / T_ext). Con supuestos ρ_0 = 1.2 '
        'kg/m³, H = 9.0 m, ΔT = 11.2 K y T_ext = 303 K, la fórmula da 3.92 Pa, y con pérdidas supuestas de 9.3 la '
        'velocidad es 0.84 m/s (142 m³/h por metro para 0.047 m²/m). En el navegador, 24.21 renovaciones por hora '
        '(de un ejemplo aparte con H = 4.5 m, ΔT = 8 K, T_0 = 293.15 K y 54 m³, o cerca de 6.4 en 204 m³) se reescalan '
        'con v / 0.84, mientras g_tot = 0.11 y 285 EML quedan como texto fijo, y 46 dB es una meta no medida. Aparte, '
        'Berson y colaboradores estudiaron células que ajustan el reloj circadiano, Brown et al. recomendaron al menos '
        '250 lux melanópicos EDI de día para adultos sanos, y el folio imagina ajustar celosías con pronósticos del '
        'tiempo y sensores de luz.'
    ),
}
