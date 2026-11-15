#!/usr/bin/env python3
"""Folio A.08 (ARCHITECTURE): AI-Designed Daytime Radiative Sky-Cooling Photonic Roofs (8–13 μm Window) & Stefan Phase-Change Envelopes."""
from __future__ import annotations

SLUG = 'a08'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.08',
 'slug': 'a08',
 'pillar': 'architecture',
 'category_code': 'A',
 'title': 'AI-Designed Daytime Radiative Sky-Cooling Photonic Roofs (8–13 μm Window) & Stefan '
          'Phase-Change Envelopes',
 'subtitle': 'Extending architectural wave optics from visible color (0.38–0.78 μm) to the 8–13 μm '
             'atmospheric infrared window—beaming building heat straight into 3 K deep space under '
             'peak midday sun.',
 'date_published': '2026-11-02',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'PHOTONIC ENVELOPES · REV 1.1',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'P_net = P_rad(T) − P_atm(T_a) − (1 − R_sol)I_sol − h_c(T_a − T) · s(t) = '
                  '2λ_s√(α t) · CSI 07 54 00',
 'colophon': {'identifier': 'A.08 · Photonic Sky-Cooling & Stefan PCM · CSI 07 54 00',
              'kernels': 'Planck 8–13 μm Sky Window · Stefan Moving-Boundary PCM Storage',
              'benchmarks': 'Model values: R_solar = 97.0% · ε_LWIR = 95.0% · P_net = +86.4 W/m² (−6.2 °C)',
              'bridge': 'Passive Sub-Ambient Sky Cooling ↔ Cooler Storage Rooms (Open Question, Not Medical Cold Storage)'},
 'sliders': [{'label': 'Solar Waveband Reflectance (R_solar)',
              'min': 0.85,
              'max': 0.99,
              'step': 0.005,
              'value': 0.97,
              'unit': 'R = '},
             {'label': '8–13 μm Sky-Window Emissivity (ε_LWIR)',
              'min': 0.65,
              'max': 0.99,
              'step': 0.01,
              'value': 0.95,
              'unit': 'ε = '}],
 'steps': ['Stage 1 (Solar Reflection, 0.3–2.5 μm): In the model the roof reflects 97.0% of an assumed 1,000 W/m² of midday sunlight, so it absorbs (1 − 0.97) × 1,000 = 30 W/m².',
           'Stage 2 (Emission in the 8–13 μm Window): The model assigns the roof a net radiative exchange with the sky of 116.4 W/m² at air temperature (emission minus absorbed atmospheric radiation). This is a fixed illustrative value, not a measurement.',
           'Stage 3 (Sub-Ambient Equilibrium Below Air Temperature): Net cooling power P_net = 116.4 − 30 = +86.4 W/m². Divided by an assumed combined heat-exchange coefficient of about 13.9 W/(m²·K), that gives a roof surface about 6.2 °C below outdoor air in the model.',
           'Stage 4 (Stefan Phase-Change Thermal Ceiling Buffer): A proposed 21 °C PCM ceiling panel would absorb indoor heat along a moving melting front s(t) = 2λ_s√(α t). The panel is a design proposal and was not sized or tested here.'],
 'readouts': [{'label': 'Absorbed Solar Flux (P_sun)', 'value': '30.0 W/m² (R_sol = 97.0%)'},
              {'label': 'Net Sky Cooling Power (P_net, Model)', 'value': '+86.4 W/m² (Noon Sun, Model)'},
              {'label': 'Sub-Ambient Temp Drop (ΔT_sub, Model)', 'value': '−6.2 °C Below Ambient (Model)'},
              {'label': 'Model Check', 'value': 'NET COOLING IN MODEL (P_net > 0)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 07 54 00 / 07 21 00',
                'title': 'Microporous PVDF-HFP Radiative Sky-Cooling Membrane & Bio-PCM Thermal '
                         'Ceiling',
                'body': 'Design proposal: a hierarchically porous poly(vinylidene fluoride-co-hexafluoropropylene) cool-roof coating of the kind reported by Mandal et al. (2018, DOI 10.1126/science.aat9513), with assumed R_solar = 0.97 and ε_8-13um = 0.95, coupled to 21 °C PCM ceiling cassettes. Not a tested assembly.',
                'meta': 'Reference: Raman et al. 2014, DOI 10.1038/nature13883 · Model values, not measurements · ASTM E1980 is the practice for calculating a solar reflectance index; none was calculated here'},
 'sidenote_1': {'kicker': 'SIDENOTE A.08-A · VISIBLE STRUCTURAL COLOR WITHOUT SOLAR HEATING',
                'body': 'A white roof can glare. One proposed answer is a thin-film coating that reflects a narrow band of visible color (terracotta, slate blue, ochre) and still reflects most of the invisible near-infrared part of sunlight. A colored surface absorbs more sunlight than a white one, so it would cool less. This folio does not model colored roofs.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.08-B · SPECIFICATION PLATE · CSI 07 54 00 / STEFAN NUMBER',
                'body': 'Illustrative storage figure: about 7.2 kg/m² of PCM with latent heat L_f = 210 kJ/kg stores 7.2 × 210 = 1,512 kJ/m², which is 420 Wh/m². In an 18 mm panel that means the panel is roughly half PCM by volume (an assumption). The Stefan number Ste = c_p ΔT / L_f = 0.085 is also an assumed value. The folio makes no claim about chiller demand.'},
 'skill': {'filename': 'radiative-sky-cooling-stefan-pcm-SKILL.md',
           'name': 'radiative-sky-cooling-stefan-pcm',
           'description': 'AI-agnostic building-physics and photonic-envelope skill for daytime '
                          'radiative sky cooling across the 8-13 um atmospheric window and Stefan '
                          'phase-change thermal storage.',
           'rules': ['Evaluate net radiative cooling flux P_net(T) = epsilon_LWIR * sigma * T^4 - '
                     'P_atm(T_amb) - (1 - R_solar) * I_solar - h_c * (T_amb - T).',
                     'Treat R_solar >= 0.94 across 0.3-2.5 um and epsilon_LWIR >= 0.90 across 8-13 um as this folio\'s own design targets under I_solar = 1000 W/m^2; report P_net and Delta T as model values, never as measured results.',
                     'Compute Stefan phase-change melting front depth s(t) = 2 * lambda_s * '
                     'sqrt(alpha_th * t) where lambda_s * exp(lambda_s^2) * erf(lambda_s) = Ste / '
                     'sqrt(pi).']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The opening rooftop scene was not sourced and is replaced by what Raman et al. (2014) report: 4.9 °C below ambient and 40.1 W/m². Earlier editions showed a zero-energy PASS verdict and a cold-chain claim for medicines; nothing here was measured and a roof a few degrees below air temperature is not medical cold storage, so both are withdrawn. The −6.2 °C figure now states the combined heat-exchange coefficient it assumes, and walkthrough numbers that did not follow from the formula are corrected.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; arithmetic recomputed from the stated formula.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-02',
                'summary': 'REV 1.0 (Published 2026-11-02): First edition, pairing the daytime radiative cooling result of Raman et al. (DOI 10.1038/nature13883) with a proposed structural-color membrane and Stefan PCM storage.',
                'opus': 'Council review of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' wording is withdrawn in REV 1.1: nothing was measured, and −6.2 K does not follow from h_c = 6.9 W/(m^2 K) alone.'}],
 'volume': 4,
 'volume_code': 'VOL. 04',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1038/nature13883',
           'fetched_on': '2026-11-08',
           'citing_publications': 3769,
           'supporting': 15,
           'mentioning': 2634,
           'contrasting': 1,
           'retracted': False,
           'summary': 'Scite index entry for Raman et al., Passive radiative cooling below ambient air temperature under direct sunlight (DOI 10.1038/nature13883), checked 2026-11-08: 3,769 citing publications (15 supporting, 2,634 mentioning, 1 contrasting) and no retraction notice. The counts describe that paper, not this folio\'s model.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1038/nature13883',
           'fetched_on': '2026-11-08',
           'citing_publications': 3769,
           'supporting': 15,
           'mentioning': 2634,
           'contrasting': 1,
           'retracted': False,
           'summary': 'Scite index entry for Raman et al., Passive radiative cooling below ambient air temperature under direct sunlight (DOI 10.1038/nature13883), checked 2026-11-08: 3,769 citing publications (15 supporting, 2,634 mentioning, 1 contrasting) and no retraction notice. The counts describe that paper, not this folio\'s model.'},
 'act1_title': 'Act I — From Ancient Persian Yakhchāl Ice Domes to Photonic Sky-Cooling Roofs & AI '
               'Thermal Meta-Emitters',
 'act1_dropcap': 'In 2014 Aaswath Raman, Shanhui Fan and colleagues at Stanford University reported in Nature a small multilayer surface that stayed colder than the surrounding air while sitting in direct sunlight (DOI 10.1038/nature13883). Tested on a rooftop under more than 850 watts per square meter of sunlight, it cooled to 4.9 degrees Celsius below the air temperature, with no electricity. Cooling a surface by letting it radiate to a clear night sky is an old practice; the yakhchāl ice houses of Iran are the example usually given, though this folio cites no source for their history. Doing the same thing in daylight is harder, because the sun delivers far more energy than a surface at ordinary temperatures can radiate away. This folio explains the energy balance behind the 2014 result and uses it in a simple design model of a roof.',
 'act1_plain_bridge': 'To understand how a roof can stay cooler than the air in full sun, think about how our planet '
                      'cools off. Everything in our world radiates invisible infrared heat waves '
                      'into the air around it. Usually, our thick atmosphere acts like a thermal '
                      'blanket, absorbing those heat waves and bouncing them back toward the '
                      'ground. However, there is a natural gap in that blanket. For a specific '
                      'band of invisible heat waves, the air is almost completely transparent. '
                      'Outer space, sitting just beyond our atmosphere, is unimaginably cold at '
                      'three degrees above absolute zero. If you can make a roof coating that '
                      'reflects ninety-seven percent of incoming sunlight while simultaneously '
                      'radiating heat waves through that clear gap in the air, the roof sends part of its heat out toward space. '
                      'When the roof radiates away more heat than it absorbs from the sun and the air, its surface settles below the outdoor air temperature, with no electric compressor involved.',
 'act1_body': 'Radiative cooling was long a night-time effect. Midday sunlight delivers roughly one thousand watts per square meter across wavelengths from 0.3 to 2.5 micrometers, so a surface that absorbs even a tenth of it takes in about as much heat as it can radiate through the sky window. In 2014, Aaswath P. Raman, Shanhui Fan, and their co-authors reported in Nature (DOI 10.1038/nature13883) a photonic cooler made of seven layers of hafnia and silica on a silver mirror. It reflected 97 percent of incident sunlight while emitting strongly in the 8–13 micrometer atmospheric window, cooled to 4.9 degrees Celsius below ambient air, and showed a cooling power of 40.1 watts per square meter at air temperature. In 2018, Mandal and colleagues reported a porous polymer coating, applied like paint, with a solar reflectance of about 0.96 and a long-wave emittance of about 0.97 (DOI 10.1126/science.aat9513); they measured sub-ambient drops of about 6 degrees Celsius and cooling powers of about 96 watts per square meter. This folio proposes pairing such a roof (CSI 07 54 00 is the roofing section it would be specified under) with phase-change ceiling cassettes that absorb daytime heat as they melt. The pairing is a design study. It could reduce the cooling a building needs from machines; the folio does not show by how much.',
 'act1_stakes': 'Historically, master builders in scorching climates fought heat through sheer '
                'thermal mass, thick adobe masonry, evaporative courtyard fountains, and white '
                'lime paint. While whitewashed plaster reflects visible light reasonably well, '
                'standard white coatings still absorb approximately ten to fifteen percent of '
                'invisible near-infrared solar energy. Under intense midday insolation of one '
                'thousand watts per square meter, that absorbed fraction puts one hundred to one hundred and fifty '
                'watts of heat into each square meter of roof, about as much as the roof can radiate through the sky window, so an ordinary white roof in full sun usually runs warmer than the air. Most cooling in cities comes from '
                'mechanical vapor-compression chillers, which use grid '
                'electricity and reject heat into the streets around them. When a heatwave and a power cut arrive together, a sealed building that depends on those machines can become dangerously hot. '
                'That is the case for adding passive cooling to a building. Passive cooling of this kind lowers a roof by a few degrees; it does not replace mechanical cooling.',
 'pullquote': '"The clear sky can serve as a heat sink in daylight, provided a '
              'building envelope reflects about 97% of sunlight while emitting strongly '
              'across the 8–13 micrometer infrared window."',
 'chronology': [('Antiquity',
                 'Night-time cooling toward a clear sky is used in ice making; the yakhchāl ice houses of Iran are the usual example (no source cited here).'),
                ('1900',
                 'Max Planck formulates the spectral law of blackbody radiation. It explains why sunlight peaks near 0.5 um while objects at room temperature emit mostly around 10 um.'),
                ('2014',
                 'Raman, Anoma, Zhu, Rephaeli & Fan demonstrate daytime sub-ambient radiative '
                 'cooling under direct sunlight in Nature (DOI 10.1038/nature13883).'),
                ('2018',
                 'Mandal et al. report hierarchically porous polymer coatings for daytime radiative cooling in Science (DOI 10.1126/science.aat9513).')],
 'act2_title': 'Act II — How It Actually Works: Spectral Selectivity (0.3–2.5 um vs. 8–13 um) + '
               'Stefan Phase-Change Storage',
 'act2_analogy': 'Wearing a standard white cotton shirt under the desert sun protects you from '
                 'getting sunburned because it reflects visible light, but your body heat remains '
                 'trapped beneath the fabric like a miniature sauna. A daytime radiative '
                 'sky-cooling roof acts like a high-tech survival suit that combines a '
                 'mirror-bright sun umbrella with an open chimney straight to outer space: it '
                 "bounces away the sun's scorching rays while giving your internal heat waves a "
                 'frictionless, direct highway to escape into the freezing cosmos.',
 'act2_plain_primer': 'To make this passive outer-space air conditioner work on a building, '
                      'engineers balance two opposing physical knobs. The first knob controls '
                      'solar reflectance across the entire daytime spectrum, from visible colors '
                      'into the invisible near-infrared. If you dial this knob down even slightly, '
                      'the roof absorbs too much raw sunlight, and heat builds up inside the '
                      'structure faster than it can escape. You must keep this first knob dialed '
                      'above ninety-five percent so the roof deck acts as an almost flawless '
                      'sunlight reflector. The second knob controls thermal emissivity inside the '
                      'narrow infrared sky window where our atmosphere is transparent. Dialing '
                      "this second knob up opens the thermal escape hatch, allowing the roof's "
                      'molecules to vibrate and shed their warmth directly into the three-Kelvin '
                      'vacuum of outer space. When both knobs are set well, the outgoing '
                      'infrared stream exceeds the sunlight the roof absorbs, and the model roof surface settles '
                      'below the temperature of the surrounding air. The readouts are outputs of a simple model, not measurements of a roof.',
 'distill_diagram': {'analogy_title': 'The Cosmic Thermal Chimney',
                     'analogy_sub': 'Reflects daytime sunlight while venting infrared into deep '
                                    'space',
                     'force_a_title': 'Solar Reflectance Knob (R_sol)',
                     'force_a_sub': 'Blocks 0.3–2.5 μm visible & near-infrared heat gain from noon '
                                    'sun',
                     'force_b_title': 'Sky-Window Emissivity (ε_LWIR)',
                     'force_b_sub': 'Beams 8–13 μm thermal infrared waves straight into 3 K deep '
                                    'space',
                     'threshold_title': 'Sub-Ambient Tipping Point (P_net > 0 W/m²)',
                     'threshold_pass': 'Model roof surface about 6.2 °C below outdoor air, no compressor',
                     'threshold_fail': 'Absorbed solar heat overwhelms emission, heating the '
                                       'building'},
 'act2_intuition': 'Net daytime radiative cooling flux is governed by the four-term thermodynamic '
                   'energy balance P_net(T) = P_rad(T) - P_atm(T_amb) - P_sun - h_c (T_amb - T). '
                   'Positive net cooling under midday sun of one thousand watts per square meter asks two different things of the roof in two wavebands. First, the solar reflectance R_solar must be high across 0.3 to 2.5 micrometers. In this folio\'s model the absorbed solar heating is P_sun = (1 - R_solar) I_solar, which is 30 W/m² at R_solar = 0.97. Second, the emissivity epsilon_LWIR should be high inside the 8–13 micrometer atmospheric window, where the roof can radiate to space with little coming back from the atmosphere, P_atm(T_amb). The model assigns the default roof a net radiative exchange of 116.4 W/m² at air temperature, a fixed illustrative value, so P_net = 116.4 - 30 = 86.4 W/m², and the model breaks even near R_solar = 0.88. The folio\'s own design targets, R_solar of at least 0.96 and epsilon_LWIR of at least 0.94, leave a margin above that. The temperature drop of 6.2 degrees Celsius comes from dividing 86.4 W/m² by an assumed combined heat-exchange coefficient of about 13.9 W/(m²·K); with a convective coefficient of 6.9 W/(m²·K) alone the same balance would give about 12.5 degrees, so the figure depends strongly on that assumption. For comparison, Raman et al. (2014, DOI 10.1038/nature13883) measured 4.9 degrees and Mandal et al. (2018, DOI 10.1126/science.aat9513) about 6 degrees. A proposed paraffin or salt-hydrate Phase-Change Material ceiling cassette (latent heat of fusion L_f = 210 kJ/kg, Stefan number Ste = c_p DeltaT / L_f) would store cooling along an advancing solid-liquid boundary s(t) = 2 * lambda_s * sqrt(alpha_th * t). Wind raises the convective term h_c (T_amb - T) and reduces the drop; published experiments often use a wind cover for that reason.',
 'act2_deepening': 'The physical coupling between solar reflectance and long-wave infrared '
                   'emissivity is intrinsically nonlinear because incoming solar energy is almost '
                   'an order of magnitude more concentrated than outgoing radiative cooling. '
                   'Midday sunlight delivers roughly one thousand watts per square meter, whereas '
                   'an ideal blackbody at room temperature radiates only about one hundred to one '
                   'hundred and fifty watts per square meter through the 8–13 micrometer '
                   'atmospheric window. Consequently, a tiny two-percent drop in solar reflectance '
                   'absorbs twenty additional watts of heat, which instantly wipes out more than '
                   "twenty percent of the roof's entire net cooling power. Parasitic convective "
                   'heat transfer governed by the heat transfer coefficient h_c creates a second '
                   'critical coupling: as the roof drops further below ambient air temperature, '
                   'the surrounding warm air reheats it. Porous polymer coatings scatter sunlight from their air voids and emit in the infrared through the vibrations of their chemical bonds (Mandal et al. 2018, DOI 10.1126/science.aat9513). In this folio\'s model the roof sits about six degrees Celsius below the air for the assumed heat-exchange coefficient; stronger wind would make that smaller.',
 'walkthrough': ['Experiment 1 (Solar Reflectance Threshold): Drag Solar Reflectance R_solar from 0.88 up to 0.97. In the folio\'s balance, P_net = 116.4 - (1 - R_solar) * 1000, the midday net cooling power rises from about -4 W/m^2 (slight heating) to +86.4 W/m^2.',
                 'Experiment 2 (8–13 um Sky Window Emissivity): Adjust Sky-Window Emissivity epsilon_LWIR from 0.70 to 0.96 and watch the model temperature drop grow; at the default 0.95 it is about 6.2 K below outdoor air.',
                 'Experiment 3 (Photonic Waveband & Stefan PCM Stepper): Step through Stages 1 to '
                 '4 to inspect Bragg/Mie solar backscattering, 8–13 um Si-O-Si phonon emission, '
                 'non-radiative wind convection shielding, and Stefan PCM latent thermal '
                 'buffering.'],
 'act4_title': 'Act IV — AI-Designed Photonic Envelopes, Lab Sustainability & Upstream Discovery '
               'Threads',
 'act4_human_ai': 'Inverse-design methods, including adjoint electromagnetic solvers and machine-learning surrogates, could be used to search for coatings that show a chosen color and still emit strongly at 8–13 um. That is a proposal; this folio designed no coating. Open tools such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) for the air flow over a roof and NREL/EnergyPlus for whole-building energy are named as tools a reader could use to test the idea; the folio ran neither. Its own model value is P_net = 86.4 W/m^2 at the default settings. Citation counts on this page come from the Scite index (DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'Engineers and machine-learning models could co-design building envelopes by solving the electromagnetic equations in reverse: the architect names a color, such as warm terracotta or forest green, and the algorithm searches for a multilayer stack that shows that color and reflects most of the invisible near-infrared part of sunlight. Building-energy models such as NREL/EnergyPlus could then estimate how fast phase-change ceiling cassettes absorb office heat by day and give it back through the roof at night. None of this was run for this folio; it is a description of a possible workflow. '
                   'Key frontier questions remain open: How can scalable roll-to-roll '
                   'manufacturing maintain sub-micron pore distributions across millions of square '
                   'meters of roofing membrane without degradation from ultraviolet weathering and '
                   'atmospheric soot? How will municipal building codes and LEED rating systems '
                   'evolve to credit passive sub-ambient cooling against mandatory HVAC equipment '
                   'sizing? Those questions decide whether the idea is useful at the scale of a city.',
 'cf_bridge': 'This is a building-physics folio for envelope architects, facade physicists, and HVAC designers (CSI 07 54 00 is the roofing section; ASHRAE Standard 90.1 is the energy standard for buildings). It has no Cystic Fibrosis content. One open question it leaves for later: a room that stays a few degrees cooler without grid power could be useful for storage in places with unreliable electricity. A roof about 6 °C below outdoor air is not refrigeration, and it cannot hold the 2–8 °C range that many medicines need. Nothing here is guidance on storing medicines.',
 'sources': ['Raman, A. P., Anoma, M. A., Zhu, L., Rephaeli, E., & Fan, S. (2014). Passive '
             'radiative cooling below ambient air temperature under direct sunlight. Nature, '
             '515(7528), 540–544. DOI: 10.1038/nature13883.',
             'Mandal, J., Fu, Y., Overvig, A. C., Jia, M., Sun, K., Shi, N. N., Zhou, H., Xiao, X., Yu, N., & Yang, Y. (2018). Hierarchically porous polymer coatings for highly '
             'efficient passive daytime radiative cooling. Science, 362(6412), 315–319. DOI: 10.1126/science.aat9513.',
             'Carslaw, H. S., & Jaeger, J. C. (1959). Conduction of Heat in Solids (2nd ed., '
             'Chapter XI: Change of State / Stefan Problem). Oxford University Press.',
             'CSI MasterFormat 07 54 00 Thermoplastic Membrane Roofing; ASHRAE Standard 90.1, Energy Standard for Buildings Except Low-Rise Residential Buildings. Named for context; neither sets this folio\'s targets.',
             'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). '
             'Dedalus: A flexible framework for numerical simulations with spectral methods '
             '(DedalusProject/dedalus, https://github.com/DedalusProject/dedalus). Physical Review '
             'Research, 2(2), 023068. DOI: 10.1103/PhysRevResearch.2.023068.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Dual-waveband '
        'photonic radiative sky-cooling spectrum showing 97% solar reflection and 95% 8-13 um '
        'atmospheric window emission">\n'
        '            <line x1="55" y1="180" x2="635" y2="180" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <line x1="55" y1="26" x2="55" y2="180" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <rect x="75" y="34" width="210" height="146" fill="var(--tp-stone)" '
        'stroke="none"/>\n'
        '            <rect x="355" y="34" width="245" height="146" fill="var(--tp-verdigris)" '
        'fill-opacity="0.12" stroke="none"/>\n'
        '            <path d="M 75 178 Q 145 38 225 162 L 285 178" fill="var(--tp-minium-soft)" '
        'stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="4,3"/>\n'
        '            <path id="tp-a08-emissivity-curve" d="M 75 174 L 295 174 L 355 44 L 585 44 L '
        '625 168" fill="none" stroke="var(--tp-verdigris)" stroke-width="3"/>\n'
        '            <text x="85" y="52" font-size="10.5" font-weight="600" '
        'fill="var(--tp-minium)">Solar Waveband (0.3–2.5 μm)</text>\n'
        '            <text id="tp-a08-rsolar-text" x="85" y="70" font-size="10" '
        'fill="currentColor">Reflectance R_solar = 97.0% (Abs = 3.0%)</text>\n'
        '            <text x="368" y="52" font-size="10.5" font-weight="600" '
        'fill="var(--tp-verdigris)">Atmospheric Sky Window (8–13 μm)</text>\n'
        '            <text id="tp-a08-pnet-text" x="368" y="70" font-size="10" '
        'fill="var(--tp-prussian)">ε_LWIR = 95.0% · Model P_net = +86.4 W/m²</text>\n'
        '            <text x="195" y="202" font-size="10.5" fill="currentColor">Electromagnetic '
        'Wavelength λ (μm) · Model ΔT_sub = −6.2 °C Below Noon Air</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a photonic radiative sky-cooling roof pavilion '
        'beaming 8-13 micrometer infrared thermal waves through the atmosphere into deep space '
        'under midday sunlight would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.08-V (Imagining What It Would Look Like) · Artistic '
            'architectural-physics visualization imagining an AI-designed microporous photonic '
            'roof reflecting midday sunlight while radiating 8–13 μm infrared heat waves directly '
            'into the 3 K sky sink above a Stefan phase-change ceiling.'}

DISPATCH = {'kicker': 'FRONTIER BUILDING PHYSICS DISPATCH · AI PHOTONIC SKY-COOLING & STEFAN PHASE-CHANGE '
           'ENVELOPES',
 'headline': 'How a Roof Can Radiate Building Heat Through the 8–13 μm Sky Window in Daylight: A Design Model',
 'body': 'Raman, Anoma, Zhu, Rephaeli & Fan measured a surface 4.9 °C below air temperature in direct sunlight (Nature, DOI 10.1038/nature13883), and Mandal et al. reported a porous polymer coating with similar behavior (Science, DOI 10.1126/science.aat9513). This folio models a roof with 97% solar reflectance and 95% sky-window emissivity: 86.4 W/m² of midday cooling in the model, paired with a proposed PCM ceiling. Model values, not measurements.'}

META_3D = ('Photonic Sky-Cooling 8–13 μm Radiative & PCM Envelope',
 'X: Wavelength λ (0.3–20 μm) · Z: Solar Flux · Y: Net Sub-Ambient Radiative Cooling P_net')

ES_TRANSLATION = {'title_es': 'Cubiertas Fotónicas de Enfriamiento Radiativo Diurno al Cielo (Ventana de 8–13 μm) y '
             'Envolventes de Cambio de Fase de Stefan',
 'subtitle_es': 'Extendiendo la óptica ondulatoria arquitectónica del color visible (0.38–0.78 μm) '
                'a la ventana infrarroja atmosférica de 8–13 μm para irradiar el calor del '
                'edificio directamente al espacio profundo a 3 K bajo pleno sol.',
 'why_es': 'Un techo blanco común refleja la luz visible pero atrapa el calor infrarrojo; una '
           'cubierta fotónica actúa como un espejo selectivo que además abre una ventana térmica '
           'directa hacia el frío del espacio exterior.',
 'bridge_es': 'Este folio es de física de edificios y no tiene contenido sobre Fibrosis Quística. Deja una pregunta abierta: un cuarto que se mantiene unos grados más fresco sin red eléctrica podría servir para almacenamiento donde la electricidad falla. Un techo unos 6 °C por debajo del aire exterior no es refrigeración ni alcanza el intervalo de 2 a 8 °C que requieren muchos medicamentos. Nada de esto es una indicación sobre cómo guardar medicamentos.',
 'plain_es': 'En palabras sencillas, imaginen que el techo de un edificio pudiera mantenerse más fresco que el aire bajo el rayo del sol sin usar electricidad. Todos los '
             'objetos emiten calor en forma de ondas infrarrojas invisibles. Normalmente, la '
             'atmósfera de la Tierra atrapa ese calor como si fuera una cobija térmica. Sin '
             'embargo, existe una ventana natural en el aire por donde ciertas ondas de calor '
             'pueden salir sin ningún obstáculo hacia el espacio exterior, el cual se encuentra a '
             'temperaturas cercanas al cero absoluto. En 2014 un equipo de Stanford midió una superficie que se mantuvo 4.9 °C por debajo del aire a pleno sol (Raman et al., DOI 10.1038/nature13883), y en 2018 otro grupo reportó un recubrimiento de polímero poroso con un comportamiento parecido (Mandal et al., DOI 10.1126/science.aat9513). Estas superficies hacen dos cosas a la vez: reflejan alrededor del 96 o 97 por ciento de la luz solar para no calentarse y emiten calor hacia el espacio a través de esa ventana en la atmósfera. El resultado es una superficie que se '
             'mantiene unos grados más fresca que el aire exterior a pleno mediodía.',
 'deep_es': 'El modelo de este folio es un balance entre lo que el techo absorbe del sol y lo que emite en la ventana atmosférica de 8 a 13 micrómetros. Con mil watts por metro cuadrado de sol a mediodía y una reflectancia solar de 0.97, el techo absorbe 30 W/m². El modelo le asigna un intercambio radiativo neto con el cielo de 116.4 W/m², un valor ilustrativo fijo, de modo que la potencia neta de enfriamiento es 116.4 − 30 = 86.4 W/m²; en el modelo el balance se vuelve cero cerca de una reflectancia de 0.88. Las metas de diseño del propio folio (reflectancia de al menos 0.96 y emisividad de al menos 0.94) dejan un margen sobre ese punto. La caída de 6.2 °C supone un coeficiente combinado de intercambio de calor de unos 13.9 W/(m²·K) y cambia mucho con esa suposición. Como referencia, Raman et al. midieron 4.9 °C y Mandal et al. alrededor de 6 °C. El folio propone combinar el techo con plafones de materiales de cambio de fase que absorban calor durante el día y lo liberen de noche; es una propuesta de diseño que no se construyó ni se probó. Son valores de modelo, no mediciones, y un techo unos grados más fresco que el aire no sustituye a la refrigeración.'}
