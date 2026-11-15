#!/usr/bin/env python3
"""Folio A.03 (ARCHITECTURE): Double-Skin Facade Buoyancy Stack Ventilation, Cavity Plumes, and 1:5 Acoustic Damper Louvers."""
from __future__ import annotations

SLUG = 'a03'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.03',
 'slug': 'a03',
 'pillar': 'architecture',
 'category_code': 'A',
 'title': 'Double-Skin Facade Buoyancy Stack Ventilation, Cavity Plumes, and 1:5 Acoustic Damper Louvers',
 'subtitle': 'A model of thermosiphon stack draft Δp_stack = ρ_0 g H β ΔT and solar shading position inside '
             'multi-story ventilated glass cavities, and how such a facade could reduce cooling loads.',
 'date_published': '2026-10-30',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.3',
 'status_badge': 'REDATED REV 1.3',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'Δp_stack = ρ_0 g H (ΔT / T_ext) · g_tot = 0.11',
 'colophon': {'identifier': 'A.03 · Facade Thermodynamics',
              'kernels': '1:50 Multi-Story Shaft + 1:5 Damper Sill',
              'benchmarks': 'Model values: Δp = 3.92 Pa (ρ_0 = 1.2 kg/m³, H = 9.0 m, ΔT = 11.2 K, T_ext ≈ 303 K) · g_tot = 0.11 assumed',
              'bridge': 'Buoyancy Convective Clearance ↔ Airway Mucociliary Escalator (analogy only)'},
 'steps': ['Stage 1 (Solar Shortwave Absorption): An assumed solar irradiance I_sol = 650 W/m² heats the ventilated '
           'blind positioned in the outer third of the 600 mm cavity.',
           'Stage 2 (Hydrostatic Buoyancy Pressure Drive): Δp_stack = ρ_0 g H (ΔT / T_ext) = 1.2 × 9.81 × 9.0 × '
           '(11.2 / 303) = 3.92 Pa across a 9.0 m two-story shaft (T_ext ≈ 303 K, about 30 °C, assumed).',
           'Stage 3 (Bernoulli Discharge & Damper Loss Balance): Setting Δp = ζ_tot ρ v² / 2 gives v = 0.84 m/s for an '
           'assumed total loss coefficient ζ_tot ≈ 9.3 (inlet, outlet louvers and friction). The 142 m³/h per metre of '
           'facade assumes an effective free opening of about 0.047 m² per metre.',
           'Stage 4 (1:5 Acoustic Baffle Sill Node A-12): A proposed mineral-wool lined labyrinth damper with a design '
           'target of R_w = 46 dB and C_d = 0.62 (targets, not measured).'],
 'readouts': [{'label': 'Buoyancy Stack Draft (Δp, Model)', 'value': '3.92 Pa'},
              {'label': 'Induced Cavity Velocity (Model)', 'value': '0.84 m/s (142 m³/h·m)'},
              {'label': 'Total Solar Factor (g_tot)', 'value': '0.11 (assumed; EN ISO 52022-3 method)'},
              {'label': 'Air Changes & Daylight (Illustrative)', 'value': '24.21 ACH · 285 EML (illustrative)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 08 44 13 / 08 91 00',
                'title': 'Thermally Broken Double-Skin Curtain Wall & Acoustic Labyrinth Vent (Node A-12)',
                'body': 'Naturally ventilated box-window facade assembly with motorized micro-perforated aluminum '
                        'venetian blinds and sound-attenuating intake sill (U_cw = 0.68 W/(m²·K), g_tot = 0.11, R_w = '
                        '46 dB).',
                'meta': 'Design proposal, not a product · EN 13830 is the curtain walling product standard a real system would be tested to'},
 'sidenote_1': {'kicker': 'SIDENOTE A.03 · BLIND POSITIONING PARADOX',
                'body': 'A blind placed close to the inner glazing tends to pass more of its absorbed heat indoors; '
                        'moving it toward the outer skin lets more of that heat leave with the cavity air. Saelens, '
                        'Roels and Hens compare strategies for multiple-skin facades (DOI 10.1016/j.buildenv.2006.06.024). '
                        'The outer-third position here is a design assumption.'},
 'skill': {'filename': 'double-skin-facade-buoyancy-SKILL.md',
           'name': 'double-skin-facade-buoyancy',
           'description': 'AI-agnostic facade engineering and building physics skill for double-skin curtain wall '
                          'buoyancy stack ventilation, EN ISO 52022-3 g_tot solar factors, and acoustic intake '
                          'dampers.',
           'rules': ['Compute buoyancy stack pressure delta_p_stack = rho_0 * g * H * (T_cav - T_ext) / T_ext and mass '
                     'flow m_dot = rho * A_eff * sqrt(2 * delta_p / zeta_tot).',
                     'Calculate total solar energy transmittance g_tot with the EN ISO 52022-3 method; this folio uses '
                     'its own design target g_tot <= 0.15 when exterior irradiance exceeds 500 W/m^2 (a folio target, '
                     'not a requirement of the standard).',
                     'This folio assumes a cavity depth D >= 500 mm for maintenance access (the folio\'s own assumption, not a '
                     'code requirement), or sealed dry-air Closed Cavity Facade (CCF) modules.']},
 'revisions': [{'edition': 'REV 1.3',
                'date': '2026-11-14',
                'summary': 'REV 1.3 (Redated 2026-11-14): Grounding revision. Claims of pathogen clearance, '
                           'protected sleep and immunity, a certified design and a PASS verdict are withdrawn: nothing '
                           'was measured. The circadian sentences had cited a radiative-cooling paper (DOI '
                           '10.1038/nature13883); they now cite Berson et al. 2002 (DOI 10.1126/science.1067262) and '
                           'Brown et al. 2022 (DOI 10.1371/journal.pbio.3001571). The stack draft now states its '
                           'assumptions (T_ext ≈ 303 K, ζ_tot ≈ 9.3), and the opening scene is replaced by a plain '
                           'account. A later review withdrew the "lung" '
                           'pullquote, the unsourced claims about mid-century glazing and the Paimio sanatorium source, '
                           'and softened outcome statements in the plain-language text and the Spanish text.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; Scite confirmed the '
                        '250 lux melanopic EDI daytime recommendation in Brown et al. 2022.'},
               {'edition': 'REV 1.2',
                'date': '2026-11-02',
                'summary': 'REV 1.2 (Redated 2026-11-02): Added a double-skin facade cavity buoyancy model with '
                           'illustrative air-change and solar factor values.',
                'opus': 'Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'wording (and its Δp = 4.2 Pa, which the formula does not give) is withdrawn in REV 1.3.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-01',
                'summary': 'REV 1.1 (Redated 2026-11-01): Added CSI 08 44 13 acoustic labyrinth sill detail and '
                           'EnergyPlus BSDF optical matrix parameters.',
                'opus': 'Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'ζ_tot = 6.85 is withdrawn in REV 1.3; v = 0.84 m/s needs ζ_tot ≈ 9.3.'},
               {'edition': 'REV 1.0',
                'date': '2026-10-30',
                'summary': 'REV 1.0 (Published 2026-10-30): Initial thermosiphon double-skin facade stack ventilation '
                           'monograph.',
                'opus': 'Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'wording is withdrawn in REV 1.3.'}],
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/j.enbuild.2006.03.013',
           'fetched_on': '2026-11-08',
           'citing_publications': 864,
           'supporting': 2,
           'mentioning': 334,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Nabil & Mardaljevic, Useful daylight illuminances (DOI 10.1016/j.enbuild.2006.03.013), checked 2026-11-08: 864 citing publications (2 supporting, 334 mentioning, 0 contrasting) and no retraction notice. The paper is about daylight metrics; it does not check this folio\'s stack-draft numbers or make circadian claims.'},
 'volume': 2,
 'volume_code': 'VOL. 02',
 'sliders': [{'label': 'Double-Skin Cavity Stack Height (H)',
              'min': 3.5,
              'max': 18.0,
              'step': 0.5,
              'value': 9.0,
              'unit': ' m'},
             {'label': 'Solar Cavity Temperature Rise (ΔT_cav)',
              'min': 2.0,
              'max': 20.0,
              'step': 0.4,
              'value': 11.2,
              'unit': ' K'}]}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'history_lead': 'In the hot, dry cities of the Iranian plateau, such as Yazd, builders have long used windcatchers '
                 '(badgirs): tall masonry towers that catch the breeze and, when the wind drops, use the warmth of the '
                 'tower itself to draw air upward and out of the rooms below. In some houses they were paired with '
                 'underground water channels (qanats). How old the oldest ones are is uncertain, and this folio does '
                 'not date them. The folio\'s own framing: a double-skin facade uses the same buoyancy principle, in glass.',
 'history_body': "Double-skin facades try to resolve the tension between letting daylight in and keeping solar heat out. Norman Foster's Commerzbank headquarters in Frankfurt (1997) is a well-known tall building with a double-skin facade. When shading sits inside the cavity, the cavity air can carry part of the absorbed solar heat away before it reaches the room; Saelens, Roels and Hens compare strategies for improving the energy performance of multiple-skin facades (Building and Environment, DOI 10.1016/j.buildenv.2006.06.024). Nabil and Mardaljevic proposed Useful Daylight Illuminance, a metric for how often daylight in a room falls in a useful range (Energy and Buildings, DOI 10.1016/j.enbuild.2006.03.013). Separately, Berson and colleagues showed that some retinal ganglion cells are themselves light-sensitive and set the circadian clock (Science, DOI 10.1126/science.1067262), and an expert consensus has recommended indoor daytime light of at least 250 lux melanopic EDI at eye level for healthy adults (Brown et al. 2022, DOI 10.1371/journal.pbio.3001571). A reader could model cavity convection with an open spectral solver such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068); this folio did not, and its numbers come from the stack formula shown.",
 'pullquote': 'Design statement of this folio, not a finding: a shaded double-skin cavity is modelled here as a '
              'buoyancy-driven air path that could carry part of the absorbed solar heat out of the building; the folio '
              'makes no other claim about the envelope.',
 'pullquote_cite': 'Editorial Synthesis · From Persian Badgirs to a Stack-Draft Model',
 'chronology': [('Date uncertain',
                 'Builders of the Iranian Plateau (e.g. Yazd)',
                 'Use badgir windcatchers, in some houses paired with underground qanat channels.'),
                ('2002',
                 'David Berson et al.',
                 'Show that some retinal ganglion cells are intrinsically light-sensitive and set the circadian clock '
                 '(DOI 10.1126/science.1067262).'),
                ('2014',
                 'Raman & Fan (Stanford)',
                 'Demonstrate passive radiative cooling below ambient air temperature under direct sunlight (DOI '
                 '10.1038/nature13883).'),
                ('2026',
                 'Informatico.ai Folio A.03',
                 'A teaching model of facade stack draft (Δp = 3.92 Pa) with illustrative daylight and air-change '
                 'values.')],
 'intuition_lead': 'The fluid mechanics of a double-skin facade operate on the Boussinesq buoyancy principle: solar '
                   'heat absorbed by intermediate motorized louvers warms the air column, creating a hydrostatic '
                   'pressure differential Delta P_stack = rho_0 * g * H * (Delta T / T_ext). With rho_0 = 1.2 kg/m^3, '
                   'H = 9.0 m, Delta T = 11.2 K and an assumed outdoor temperature T_ext = 303 K, the formula gives '
                   '3.92 Pa. Balancing that drive against an assumed total loss coefficient of about 9.3 for the inlet '
                   'and outlet louvers gives a cavity velocity of 0.84 m/s. The blind position in the outer third of the '
                   '600 mm cavity and the total solar factor g_tot = 0.11 are design assumptions; EN ISO 52022-3 gives a '
                   'method for calculating g_tot, and Saelens, Roels and Hens (DOI 10.1016/j.buildenv.2006.06.024) '
                   'compare facade strategies. The 24.2 air changes per hour and 285 EML on the readout strip are '
                   'illustrative values, not computed here, and the folio makes no claim about clearing aerosols or '
                   'pathogens. The 46 dB sound reduction is a design target for the proposed sill.',
 'intuition_body': 'A second, separate worked example using the folio\'s formula: a 4.5 m cavity warmed by Delta T = 8 K, '
                   'with T_0 = 293 K, gives sqrt(2 g H Delta T / T_0) = 1.55 m/s. Multiplying by an assumed effective '
                   'opening C_d A = 0.234 m^2 gives Q = 0.363 m^3/s, which is 6.4 air changes per hour only for an '
                   'assumed room volume of about 204 m^3. These are illustrative numbers. Separately, Raman and '
                   'colleagues demonstrated a roof-scale photonic emitter cooling below ambient air temperature under '
                   'direct sunlight (DOI 10.1038/nature13883); the folio does not model that device.',
 'walkthrough': ['Experiment 1 (Trace the 4 Stages): Click Stages 1 -> 4 above to follow the solar heating of the blind, '
                 'the stack pressure, the loss balance and the proposed acoustic sill.',
                 'Experiment 2 (Inspect the Double-Skin Solar Chimney Section): Study the SVG section below showing '
                 'how warm exhaust air rises up the 600 mm outer cavity while daylight reaches the ceiling plane.',
                 'Experiment 3 (Read the Readout Strip): The stack draft and velocity follow from the formula and stated '
                 'assumptions; the air-change rate and EML values are illustrative and are not health targets.'],
 'human_ai_shift': 'Daylight and airflow are usually simulated separately. A designer, with or without an AI assistant, '
                   'could pair a spectral solver such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, '
                   'DOI 10.1103/PhysRevResearch.2.023068) for cavity convection with a whole-building energy tool such as '
                   'NREL/EnergyPlus, and explore louver and damper settings together. This folio names those tools as '
                   'options a reader could use; it did not run them.',
 'cf_bridge': 'People with Cystic Fibrosis often spend time each day on inhaled therapies, and some are treated in '
              'hospital. Infection-prevention practice for CF care is set out in clinical guidance '
              '(Saiman et al. 2014, DOI 10.1086/676882); this folio does not address it. '
              'Daylight recommendations for healthy adults exist (Brown et al. 2022, DOI 10.1371/journal.pbio.3001571), '
              'but this folio reports no clinical, sleep or infection outcome. It is a facade physics study and is not '
              'medical or infection-control advice; people with CF should follow their care team.',
 'sources': ['Berson, D. M., Dunn, F. A., & Takao, M. (2002). Phototransduction by retinal ganglion cells that set the '
             'circadian clock. Science, 295(5557), 1070–1073. DOI: 10.1126/science.1067262.',
             'Brown, T. M., et al. (2022). Recommendations for daytime, evening, and nighttime indoor light exposure to '
             'best support physiology, sleep, and wakefulness in healthy adults. PLOS Biology, 20(3), e3001571. DOI: '
             '10.1371/journal.pbio.3001571.',
             'Saiman, L., et al. (2014). Infection Prevention and Control Guideline for Cystic Fibrosis: 2013 Update. '
             'Infection Control & Hospital Epidemiology, 35(S1), S1–S67. DOI: 10.1086/676882.',
             'Raman, A. P., Anoma, M. A., Zhu, L., Rephaeli, E., & Fan, S. (2014). Passive radiative cooling below '
             'ambient air temperature under direct sunlight. Nature, 515, 540–544. DOI: 10.1038/nature13883.',
             'Saelens, D., Roels, S., & Hens, H. (2008). Strategies to improve the energy performance of multiple-skin '
             'facades. Building and Environment, 43(4), 638–650. DOI: 10.1016/j.buildenv.2006.06.024.',
             'Nabil, A., & Mardaljevic, J. (2006). Useful daylight illuminances: A replacement for daylight factors. '
             'Energy and Buildings, 38(7), 905–913. DOI: 10.1016/j.enbuild.2006.03.013.',
             'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). Dedalus: A flexible '
             'framework for numerical simulations with spectral methods (DedalusProject/dedalus, '
             'https://github.com/DedalusProject/dedalus). Physical Review Research, 2(2), 023068. DOI: '
             '10.1103/PhysRevResearch.2.023068.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Double-skin solar chimney thermosiphon '
        'and 8-13 um radiative sky cooling">\n'
        '            <rect x="110" y="30" width="22" height="160" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="2"/>\n'
        '            <rect x="170" y="30" width="420" height="160" fill="none" stroke="currentColor" '
        'stroke-opacity="0.35" stroke-width="2"/>\n'
        '            <line x1="150" y1="175" x2="150" y2="42" stroke="var(--tp-minium)" stroke-width="3" '
        'stroke-dasharray="5,3"/>\n'
        '            <path d="M 55 75 L 170 110 L 390 65" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="2.5"/>\n'
        '            <line x1="380" y1="30" x2="540" y2="30" stroke="var(--tp-verdigris)" stroke-width="5"/>\n'
        '            <text x="45" y="65" font-size="11" fill="var(--tp-prussian)">Daylight (285 EML, illustrative)</text>\n'
        '            <text x="68" y="205" font-size="11" fill="var(--tp-minium)">Solar Chimney ↑ Q = 0.363 m³/s (worked '
        'example)</text>\n'
        '            <text x="370" y="20" font-size="11" fill="var(--tp-verdigris)">8–13 μm Radiative Sky Cooler '
        '(concept)</text>\n'
        '          </svg>',
 'scite': {'doi': '10.1016/j.enbuild.2006.03.013',
           'fetched_on': '2026-11-08',
           'citing_publications': 864,
           'supporting': 2,
           'mentioning': 334,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Nabil & Mardaljevic, Useful daylight illuminances (DOI 10.1016/j.enbuild.2006.03.013), checked 2026-11-08: 864 citing publications (2 supporting, 334 mentioning, 0 contrasting) and no retraction notice. The paper is about daylight metrics; it does not check this folio\'s stack-draft numbers or make circadian claims.'},
 'word_count': '4,650 WORDS',
 'act1_dropcap': 'In the hot, dry cities of the Iranian plateau, such as Yazd, builders have long used windcatchers '
                 '(badgirs): tall masonry towers that catch the breeze and, when the wind drops, use the warmth of the '
                 'tower itself to draw air upward and out of the rooms below. In some houses they were paired with '
                 'underground water channels (qanats). How old the oldest ones are is uncertain, and this folio does '
                 'not date them. The folio\'s own framing: a double-skin facade uses the same buoyancy principle, in glass.',
 'act1_plain_bridge': 'We have all stepped into a car parked in the hot summer sun and felt that stifling blast of '
                      'trapped heat. Glass is fantastic at letting bright sunshine stream indoors, but it traps that '
                      'solar warmth like a greenhouse. In a modern office tower or hospital, baking inside a sealed '
                      'glass box forces giant air-conditioning units to burn enormous amounts of electrical energy all '
                      'day long. A double-skin facade is one design that aims to ease this problem by giving the building two layers of glass '
                      'with an open walkway in between, like wearing a light windbreaker over a sweater. When sunlight '
                      'hits adjustable blinds inside that middle corridor, the trapped air warms up, becomes lighter, '
                      'and rushes up the chimney to escape out the roof. That rising plume of air could draw fresh '
                      'outdoor air through the building, which is what the design aims for: lower cooling loads and '
                      'daylit rooms. This folio models only the stack draft; it does not measure comfort, noise or light.',
 'act1_body': "Double-skin facades try to resolve the tension between letting daylight in and keeping solar heat out. Norman Foster's Commerzbank headquarters in Frankfurt (1997) is a well-known tall building with a double-skin facade. When shading sits inside the cavity, the cavity air can carry part of the absorbed solar heat away before it reaches the room; Saelens, Roels and Hens compare strategies for improving the energy performance of multiple-skin facades (Building and Environment, DOI 10.1016/j.buildenv.2006.06.024). Nabil and Mardaljevic proposed Useful Daylight Illuminance, a metric for how often daylight in a room falls in a useful range (Energy and Buildings, DOI 10.1016/j.enbuild.2006.03.013). Separately, Berson and colleagues showed that some retinal ganglion cells are themselves light-sensitive and set the circadian clock (Science, DOI 10.1126/science.1067262), and an expert consensus has recommended indoor daytime light of at least 250 lux melanopic EDI at eye level for healthy adults (Brown et al. 2022, DOI 10.1371/journal.pbio.3001571). A reader could model cavity convection with an open spectral solver such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068); this folio did not, and its numbers come from the stack formula shown.",
 'act1_stakes': 'Sealed, curtain-walled glass towers became common in the mid-twentieth century. Glass admits daylight '
                'but also traps solar heat, so a sealed glass building needs cooling. Ventilating such spaces with '
                'simple operable windows can let outside traffic noise, wind gusts, and rain intrude on interior '
                'offices. Conversely, if a double-skin facade is sized with flawed rules of thumb—such as building a '
                'cavity that is too narrow or placing shading blinds too close to the inner pane—the cavity can become '
                'a thermal trap: it may overheat, the glass sees larger thermal stresses, and a weak stack effect can let '
                'warm cavity air find its way back indoors.',
 'act2_analogy': 'Everyday analogy: Picture a wood-burning stove on a chilly winter morning. The tall, narrow chimney '
                 'pipe does not need an electric fan to pull smoke upward; the hot air inside is less dense than the '
                 'cold outside air, creating an upward draft that drinks fresh air through the bottom air intake. A '
                 'double-skin facade is simply an architectural glass chimney wrapped around the building, using '
                 'absorbed solar heat to draw warm air upward and away.',
 'act2_plain_primer': 'In the interactive laboratory below, you command the two primary thermodynamic levers that '
                      'drive natural chimney ventilation across a glass curtain wall. The first lever controls the '
                      'vertical stack height of the glazed cavity, spanning from a single floor up to a multi-story '
                      'atrium shaft. As you extend the chimney taller, the weight difference between the warm air '
                      'column inside the glass and the cooler outdoor air grows larger, creating stronger upward '
                      'suction that draws fresh air across interior rooms. The second lever adjusts the temperature '
                      'rise inside the cavity, representing how much solar heat the motorized aluminum louvers absorb. '
                      'On bright sunny afternoons, this temperature rise increases, heating the air parcel and '
                      'accelerating the upward exhaust velocity. By harmonizing chimney height with shading louver '
                      'angles, the model facade keeps a steady upward flow in the cavity while the proposed sill aims '
                      'to cut street noise.',
 'distill_diagram': {'analogy_title': 'Wood Stove Thermal Chimney Draft',
                     'analogy_sub': 'Warm buoyant air column pulls fresh breezes through intake',
                     'force_a_title': 'Cavity Stack Height (H)',
                     'force_a_sub': 'Taller glazed shaft increases hydrostatic buoyancy suction',
                     'force_b_title': 'Cavity Temp Rise (ΔT_cav)',
                     'force_b_sub': 'Absorbed solar heat decreases air density, powering draft',
                     'threshold_title': 'Louver Friction & Solar Factor Balance',
                     'threshold_pass': 'Thermosiphon draft exceeds louver losses; steady cavity flow (model)',
                     'threshold_fail': 'Excessive damper resistance; thermal plume stalls and overheats'},
 'act2_intuition': 'The fluid mechanics of a double-skin facade operate on the Boussinesq buoyancy principle: solar '
                   'heat absorbed by intermediate motorized louvers warms the air column, creating a hydrostatic '
                   'pressure differential Delta P_stack = rho_0 * g * H * (Delta T / T_ext). With rho_0 = 1.2 kg/m^3, '
                   'H = 9.0 m, Delta T = 11.2 K and an assumed outdoor temperature T_ext = 303 K, the formula gives '
                   '3.92 Pa. Balancing that drive against an assumed total loss coefficient of about 9.3 for the inlet '
                   'and outlet louvers gives a cavity velocity of 0.84 m/s. The blind position in the outer third of the '
                   '600 mm cavity and the total solar factor g_tot = 0.11 are design assumptions; EN ISO 52022-3 gives a '
                   'method for calculating g_tot, and Saelens, Roels and Hens (DOI 10.1016/j.buildenv.2006.06.024) '
                   'compare facade strategies. The 24.2 air changes per hour and 285 EML on the readout strip are '
                   'illustrative values, not computed here, and the folio makes no claim about clearing aerosols or '
                   'pathogens. The 46 dB sound reduction is a design target for the proposed sill.',
 'act2_deepening': 'The coupled thermodynamics between stack height H and temperature rise Delta T reveals why facade '
                   'tuning demands strict nonlinear optimization. Buoyancy draft scales linearly with the product of '
                   'height and temperature differential, but volumetric airflow Q = C_d * A * sqrt(2 * Delta P / rho) '
                   'exhibits a square-root dependence on that pressure drive. If the cavity height is doubled, the '
                   'buoyancy force increases, drawing higher mass flow through the intake dampers. However, this '
                   'faster air velocity sweeps through the cavity in less time, reducing the contact duration during '
                   'which the air parcel absorbs heat from the solar blinds. In the model, this negative feedback loop '
                   'tends to limit how far the cavity temperature rises; the folio does not simulate it. Micro-perforated '
                   'aluminum louvers are proposed in this design to scatter some shortwave light toward the ceiling; the folio '
                   'does not model their optical or thermal behavior. At the 1:5 acoustic sill node, '
                   'sound-absorbing baffles are proposed to force incoming air through a serpentine path to reduce street '
                   'noise; the 46 dB figure is a design target, not a measurement, and the added flow resistance would '
                   'reduce the draft.',
 'act4_deepening': 'A proposal, not a description of current practice: instead of fixed seasonal damper schedules, '
                   'a facade controller could use weather forecasts to adjust louver angles and exhaust dampers ahead '
                   'of solar peaks, and light sensors could help balance daylight against glare at desks. An open '
                   'question explores '
                   'closed-cavity facades with dry-air purging: can automated desiccant-loop agents reduce '
                   'interstitial condensation and dust accumulation in such cavities over long lifecycles? Whether that '
                   'would make passive buoyancy ventilation workable in humid tropical climates is untested.',
 'act4_human_ai': 'Daylight and airflow are usually simulated separately. A designer, with or without an AI assistant, '
                  'could pair a spectral solver such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, '
                  'DOI 10.1103/PhysRevResearch.2.023068) for cavity convection with a whole-building energy tool such as '
                  'NREL/EnergyPlus, and explore louver and damper settings together. This folio names those tools as '
                  'options a reader could use; it did not run them.'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a multi-story double-skin glass facade buoyancy stack shaft paired '
        'with circadian solar shading louvers and acoustic intake baffles would look like (artistic impression, not a '
        'measured structure)',
 'caption': 'Conceptual Vision Plate A.03-V (Imagining What It Would Look Like) · Artistic architectural cutaway '
            'imagining a multi-story ventilated double-skin curtain wall shaft driving thermosiphon buoyancy exhaust '
            '(Delta_p = 3.92 Pa) across circadian daylight shading louvers (g_tot = 0.11).'}

DISPATCH = {'kicker': 'FRONTIER FACADE & PHOTOBIOLOGY DISPATCH · BUOYANCY STACKS & CIRCADIAN DAYLIGHTING',
 'headline': 'Double-Skin Curtain Wall Buoyancy: A Stack-Draft Model Beside Daylight Metrics',
 'body': "Drawing on Saelens, Roels & Hens's comparison of multiple-skin facade strategies (Building and Environment "
         "DOI 10.1016/j.buildenv.2006.06.024), Nabil & Mardaljevic's Useful Daylight Illuminance (DOI "
         '10.1016/j.enbuild.2006.03.013) and the daytime light recommendation of Brown et al. (DOI '
         '10.1371/journal.pbio.3001571), this folio models a 9.0 m cavity with a stack draft of 3.92 Pa under stated '
         'assumptions. Its air-change and daylight figures are illustrative, and it makes no health claim.'}

META_3D = ('Double-Skin Facade Buoyancy Plume Canyon',
 'X: Glazed Cavity Depth · Z: Stack Elevation H · Y: Solar Thermosiphon Velocity & ACH Plume')

ES_TRANSLATION = {'title_es': 'Ventilación por Tiro de Flotabilidad en Fachadas de Doble Piel, Plumas en la Cavidad y Rejillas Acústicas '
             'Amortiguadoras 1:5',
 'subtitle_es': 'Un modelo del tiro por termosifón Δp_stack = ρ_0 g H β ΔT y de la posición de la protección solar '
                'en cavidades acristaladas ventiladas de varios niveles, y de cómo una fachada así podría reducir las '
                'cargas de enfriamiento.',
 'why_es': 'Una chimenea solar acristalada usa el propio calor del sol para hacer subir el aire caliente de la '
           'cavidad, mientras deja pasar la luz del día.',
 'bridge_es': 'Las prácticas de prevención de infecciones en la atención de la Fibrosis Quística están descritas en '
              'guías clínicas (Saiman et al. 2014, DOI 10.1086/676882); esta ficha no las aborda. Es un estudio de física '
              'de fachadas, no reporta resultados clínicos y no es consejo médico ni de control de infecciones; las '
              'personas con Fibrosis Quística deben seguir las indicaciones de su equipo de atención.',
 'plain_es': 'Todos hemos entrado a un automóvil estacionado bajo el sol del mediodía y sentido ese golpe sofocante de '
             'aire atrapado. El vidrio convencional deja pasar la hermosa luz solar, pero retiene el calor infrarrojo '
             'como un invernadero. En edificios de oficinas y hospitales, este sobrecalentamiento obliga a los '
             'sistemas de aire acondicionado a consumir enormes cantidades de energía eléctrica todo el día. Una '
             'fachada de doble piel es un diseño que busca aliviar este problema: da al edificio dos capas de cristal '
             'con un pasillo abierto entre ellas. Cuando los rayos del sol calientan las persianas colocadas dentro de este '
             'espacio intermedio, el aire se vuelve más ligero y asciende hacia el techo, saliendo al '
             'exterior como en una chimenea. Esa corriente ascendente podría jalar aire fresco del exterior a través '
             'del edificio, que es lo que busca el diseño: menores cargas de enfriamiento y cuartos con luz natural. '
             'Este folio solo modela el tiro por flotabilidad; no mide confort, ruido ni luz.',
 'deep_es': 'La ventilación natural en fachadas de doble piel opera mediante el principio de termosifón, donde la '
            'altura del tiro vertical y la elevación de temperatura en la cavidad generan una presión de flotabilidad '
            'positiva. Una persiana colocada cerca del vidrio interior tiende a ceder más de su calor absorbido al interior; al '
            'ubicarla en el tercio exterior del espacio acristalado (un supuesto de diseño), una parte mayor de ese calor '
            'tiende a salir con el aire de la cavidad. El factor solar total g_tot = 0.11 es un supuesto, no un resultado. '
            'La diferencia de densidad genera una corriente ascendente en la cavidad, según la fórmula del modelo. Con ρ_0 = 1.2 kg/m³, H = 9.0 m, ΔT = 11.2 K y '
            'una temperatura exterior supuesta de 303 K, la fórmula da 3.92 Pa, y con un coeficiente de pérdidas '
            'supuesto de 9.3 la velocidad en la cavidad es de 0.84 m/s. Las 24.2 renovaciones por hora y los 285 EML '
            'son valores ilustrativos, no metas de salud, y los 46 dB del antepecho acústico son una meta de diseño.'}
