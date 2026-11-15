#!/usr/bin/env python3
"""Folio A.07 (ARCHITECTURE): Luis Barragán's Chromatic Tectonics, Kubelka–Munk Pigment Radiosity & Emotional Spatial Wavefields."""
from __future__ import annotations

SLUG = 'a07'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.07',
 'slug': 'a07',
 'pillar': 'architecture',
 'category_code': 'A',
 'title': "Luis Barragán's Chromatic Tectonics, Kubelka–Munk Pigment Radiosity & Emotional Spatial "
          'Wavefields',
 'subtitle': 'How Luis Barragán, with his friend Chucho Reyes Ferreira, worked with saturated '
             'color (Rosa Mexicano, cobalt blue, ochre) and Mexican sunlight, and how Josef Albers '
             'taught color relativity—read here through a simple model of pigment scattering and '
             'inter-reflection.',
 'date_published': '2026-11-02',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'CHROMATIC ARCHITECTURE · REV 1.1',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'K/S = (1 − R_∞)² / (2 R_∞) · B(x,λ) = E(x,λ) + ρ(x,λ) ∫ B(y,λ) F(x,y) dA_y · '
                  'CSI 09 24 00',
 'colophon': {'identifier': 'A.07 · Barragán Chromatic Tectonics & Radiosity · CSI 09 24 00',
              'kernels': 'Kubelka–Munk Two-Flux Pigment Law · Fredholm Spectral Radiosity',
              'benchmarks': 'Model values: R_∞ = 0.389 at K/S = 0.48 · +31.1% bounce gain at F_12 = 0.61 (illustrative)',
              'bridge': 'Barragán Mineral Stucco Radiosity ↔ P.08 Thin-Film Car Paint & M.08 Color '
                        'Geodesics'},
 'sliders': [{'label': 'Incident Solar Elevation (θ_sun)',
              'min': 15.0,
              'max': 75.0,
              'step': 1.0,
              'value': 42.0,
              'unit': '°'},
             {'label': 'Kubelka–Munk Pigment Ratio (K/S)',
              'min': 0.05,
              'max': 2.5,
              'step': 0.01,
              'value': 0.48,
              'unit': 'K/S = '}],
 'steps': ['Stage 1 (Golden Corridor Spectral Filtering, λ ≈ 582 nm): Sunlight entering Casa '
           "Gilardi's yellow-glazed corridor loses much of its short-wave blue light, warming the "
           'light that reaches the room (582 nm is an illustrative dominant wavelength).',
           'Stage 2 (Kubelka–Munk Lime Scattering): For an assumed K/S = 0.48, the infinite-thickness '
           'diffuse reflectance is R_∞ = 1 + K/S − √((K/S)² + 2 K/S) = 1.48 − 1.091 = 0.389; the '
           'surface is assumed matte (Lambertian).',
           'Stage 3 (Wall-to-Water Inter-Reflection): In a simplified one-bounce-series model, the '
           'gain 1 / (1 − R_∞ F_12) = 1 / (1 − 0.389 × 0.61) gives +31.1% for an assumed view factor F_12 = 0.61; '
           'it is an illustrative model value, not a measured change in color.',
           'Stage 4 (Torres de Satélite Highway Parallax & Albers Contrast): The towers, the tallest '
           'about 52 m high, were designed to be seen from cars on the highway, so their silhouettes '
           'shift as viewers move.'],
 'readouts': [{'label': 'Kubelka–Munk Reflectance (R_∞, Model)', 'value': '0.389 (at K/S = 0.48)'},
              {'label': 'Inter-Reflection Gain (Illustrative)', 'value': '+31.1% (assumed F_12 = 0.61)'},
              {'label': 'Dominant Wavelength Pair (Illustrative)', 'value': '615 nm Rosa · 465 nm Cobalt'},
              {'label': 'Surface Assumption (Model)', 'value': 'LAMBERTIAN SURFACES ASSUMED'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 09 24 00 / 09 91 00',
                'title': 'Artisanal Volcanic-Sand Slaked Lime Stucco & Mineral Oxide / Cochineal '
                         'Wash',
                'body': 'Three-coat hand-troweled slaked calcium-hydroxide lime plaster (Ca(OH)2 '
                        'carbonating to calcite CaCO3) with coarse volcanic tezontle/basalt '
                        'aggregate and UV-stable inorganic mineral oxide & ultramarine pigments.',
                'meta': 'Design proposal · K/S = 0.48 and 85° gloss < 2 GU are targets, not '
                        'measurements'},
 'sidenote_1': {'kicker': 'SIDENOTE A.07-A · BARRAGÁN, CHUCHO REYES & THE AUTOMOBILE AT TORRES DE '
                          'SATÉLITE',
                'body': "The painter and collector Jesús 'Chucho' Reyes Ferreira was a close friend of "
                        'Luis Barragán and is often credited with influencing his use of color. Torres '
                        'de Satélite (1957–58), designed by Barragán and Mathias Goeritz, stands '
                        'beside a highway and was meant to be seen from moving cars; the tallest '
                        'tower is about 52 meters.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.07-B · SPECIFICATION PLATE · CSI 09 24 00 / KUBELKA–MUNK '
                          'OPTICS',
                'body': 'Unlike synthetic acrylic film paints that form a specular plastic skin, '
                        'carbonated limewash traps pigment grains inside a porous calcite crystal '
                        'lattice—scattering light waves isotropically via Kubelka–Munk radiative '
                        'transfer.'},
 'skill': {'filename': 'barragan-kubelka-munk-radiosity-SKILL.md',
           'name': 'barragan-kubelka-munk-radiosity',
           'description': 'AI-agnostic architectural daylighting and color-physics skill for Luis '
                          'Barragan chromatic tectonics, Kubelka-Munk pigment reflectance, and '
                          'Fredholm spectral radiosity.',
           'rules': ['Compute infinite-thickness Kubelka-Munk diffuse reflectance R_inf = 1 + '
                     '(K/S) - sqrt((K/S)^2 + 2*(K/S)) from absorption K and scattering S.',
                     'Solve wavelength-resolved enclosure radiosity B_i(lambda) = E_i(lambda) + '
                     'rho_i(lambda) * sum_j F_ij * B_j(lambda) across 380-780 nm.',
                     'Maintain matte mineral surface roughness (85-degree specular gloss < 2 GU) '
                     'so diffuse chromatic bounce dominates over specular glare.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The Kubelka–Munk '
                           'reflectance at K/S = 0.48 is corrected from 0.391 to 0.389 (and 0.21 to '
                           '0.22 at K/S = 1.40), and the chroma gain (+31.1% at F_12 = 0.61) is now labelled an '
                           'illustrative value with its assumed view factor. Claims that tuned color '
                           'regulates melanopsin pathways and calms patients, the PASS verdict, '
                           'unsourced anecdotes (gouache tests, 80 km/h) and an invented-looking '
                           'quotation are withdrawn; two uncited sources were removed.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; Scite '
                        'found no paper supporting a saturation gain from inter-reflection, so it is '
                        'labelled the folio\'s own model.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-02',
                'summary': 'REV 1.0 (Published 2026-11-02): Inaugural Volume IV architectural '
                           "color monograph uniting Luis Barragan's Casa Gilardi & Torres de "
                           "Satelite, Josef Albers's Interaction of Color, and Paul Kubelka's "
                           'radiative scattering law (DOI 10.1364/JOSA.38.000448).',
                'opus': 'Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its '
                        "earlier 'verified' wording is withdrawn in REV 1.1: R_inf at K/S = 0.48 is "
                        '0.389, not 0.3912, and the cavity amplification was not computed.'}],
 'volume': 4,
 'volume_code': 'VOL. 04',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1364/JOSA.38.000448',
           'fetched_on': '2026-11-08',
           'citing_publications': 2781,
           'supporting': 15,
           'mentioning': 1206,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Kubelka, New contributions to the optics of intensely light-scattering materials, Part I (DOI 10.1364/JOSA.38.000448), checked 2026-11-08: 2,781 citing publications (15 supporting, 1,206 mentioning, 0 contrasting) and no retraction notice. The paper is about scattering layers; it says nothing about architecture or this folio\'s numbers.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1364/JOSA.38.000448',
           'fetched_on': '2026-11-08',
           'citing_publications': 2781,
           'supporting': 15,
           'mentioning': 1206,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Kubelka, New contributions to the optics of intensely light-scattering materials, Part I (DOI 10.1364/JOSA.38.000448), checked 2026-11-08: 2,781 citing publications (15 supporting, 1,206 mentioning, 0 contrasting) and no retraction notice. The paper is about scattering layers; it says nothing about architecture or this folio\'s numbers.'},
 'act1_title': "Act I — Luis Barragán's Emotional Architecture, Chucho Reyes, Josef Albers & the "
               'Wave Radiosity of Color',
 'act1_dropcap': 'In Casa Gilardi in Tacubaya, Mexico City (completed 1976), a corridor lit through '
                 'yellow glass leads to an indoor pool where a freestanding red wall rises from '
                 'the water against blue walls. Luis Barragán trained as an engineer in '
                 'Guadalajara and became known for walls of saturated color and quiet enclosed '
                 'gardens. He received the Pritzker Architecture Prize in 1980, and his acceptance '
                 'speech spoke of beauty, silence and serenity. His friend the painter Jesús '
                 "'Chucho' Reyes Ferreira and the sculptor Mathias Goeritz, who in 1953 wrote a "
                 "manifesto of 'emotional architecture', were close collaborators and influences.",
 'act1_plain_bridge': 'In plain words, think about what happens when light hits a painted wall in '
                      'your home. Shiny modern latex paint acts like a mirror, bouncing harsh '
                      'glare straight into your eyes and washing out the color. Luis Barragán did '
                      'the opposite. He mixed mineral pigments directly into rough, porous plaster '
                      'made from local volcanic sand and slaked lime. When strong sunlight strikes '
                      'this textured surface, the light dives deep inside millions of tiny '
                      'microscopic crystals before bouncing back out. Instead of a single harsh '
                      'reflection, the wall scatters gentle, velvety color in every direction at '
                      'once. When two of these textured walls face each other across a courtyard '
                      'or a pool of water, the colored light bounces back and forth like echoes '
                      'between canyon walls. The red wall warms the blue pool, the blue water '
                      'softens the red, and the air between them fills with a soft glow.',
 'act1_body': 'In his house and studio in Mexico City (1948), the highway monument Torres de '
              'Satélite (1957–58, with Goeritz, meant to be seen from moving cars), the horse '
              'pools of Cuadra San Cristóbal (1966–68), and Casa Gilardi (1976), Barragán used '
              'large planes of saturated color—a magenta-pink often called Rosa Mexicano, deep '
              'blues and warm yellows. The dominant wavelengths this folio assigns them (about '
              '615 nm, 465 nm and 582 nm) are illustrative, not measurements of the buildings. '
              'Separately, at Black Mountain College and Yale, Josef Albers (Interaction of '
              'Color, 1963) showed through classroom exercises that the same color looks '
              'different depending on the colors around it. Physically, the folio models the '
              'pool room as follows: when zenith daylight enters '
              "Casa Gilardi's yellow-glazed corridor and strikes the freestanding crimson column "
              'rising from the cobalt pool, multiple diffuse bounces obey Paul Kubelka and Franz '
              "Munk's two-flux radiative transfer law K/S = (1 - R_inf)^2 / (2 R_inf) (DOI "
              '10.1364/JOSA.38.000448) coupled with the Fredholm radiosity integral equation B(x, '
              'lambda) = E(x, lambda) + rho(x, lambda) int B(y, lambda) F(x, y) dA_y.',
 'act1_stakes': 'For centuries, master builders in the Mediterranean, North Africa, and colonial '
                'Mexico used lime washes tinted with earth oxides to temper blinding desert glare. '
                'Lime plasters are vapor-permeable, so a well-made lime wall lets moisture escape '
                'rather than trapping it behind a film. '
                'But during the mid-twentieth century, the construction industry abandoned slaked '
                'lime in favor of quick-drying acrylic latex paints and planar glass curtain '
                'walls. Smooth glossy films can produce specular glare at glancing angles, and on '
                'damp masonry a less permeable paint layer can blister. '
                'When architects rely on generic color swatches under artificial fluorescent '
                'lighting, the colors look dead and artificial under natural daylight. Without '
                'understanding diffuse scattering and mutual radiosity, modern interiors either '
                'feel sterile and washed out or degenerate into cavernous spaces plagued by visual '
                'fatigue and harsh contrast.',
 'pullquote': "Editorial note: in Casa Gilardi the freestanding red wall does not merely sit in "
              'the blue pool—light bounced from it tints the water and the walls around it.',
 'chronology': [('1931',
                 'Paul Kubelka & Franz Munk formulate the two-flux absorption-to-scattering '
                 'differential theory of pigmented coatings (K/S = (1 - R_inf)^2 / 2 R_inf).'),
                ('1957–58',
                 'Luis Barragán & Mathias Goeritz build Torres de Satélite beside a highway in the '
                 'Mexico City area, five colored concrete towers up to about 52 meters tall, meant to '
                 'be seen from moving cars.'),
                ('1963',
                 'Josef Albers publishes Interaction of Color at Yale University Press, codifying '
                 'simultaneous contrast and chromatic relativity.'),
                ('1976',
                 'Luis Barragán completes Casa Gilardi in Tacubaya, Mexico City, uniting solar '
                 'corridor filtering, cobalt water reflection, and Rosa Mexicano radiosity.')],
 'act2_title': 'Act II — How It Actually Works: Kubelka–Munk Pigment Scattering + Spectral '
               'Radiosity Inter-Reflection',
 'act2_analogy': 'Hold a bright yellow buttercup flower beneath your chin on a sunny afternoon, '
                 'and your skin instantly lights up with a warm golden glow. The flower petals do '
                 'not generate light on their own; instead, sunlight dives into the translucent '
                 'cellular layers of the petal, picks up its intense yellow hue, and bounces onto '
                 'your jaw. Luis Barragán scaled that exact childhood playground phenomenon up to '
                 'the size of a building, turning textured masonry walls and quiet pools into '
                 'giant glowing petals that illuminate each other.',
 'act2_plain_primer': 'To bring this playground buttercup effect into architecture, you only need '
                      'to adjust two physical knobs. The first knob controls the angle of the sun '
                      'in the sky as the day progresses from morning to noon. When the sun is low '
                      'in the early morning, its rays strike the textured plaster walls at a '
                      'shallow angle, casting long micro-shadows across the rough volcanic sand '
                      'and creating deep, intimate tones. As the sun climbs toward its midday '
                      'peak, direct light penetrates straight down into the space, illuminating '
                      'the water and launching powerful reflections upward. The second knob sets '
                      'the concentration of mineral pigment mixed into the wet lime plaster. If '
                      'you add only a tiny pinch of pigment, the wall behaves like chalk, bouncing '
                      'white sunlight everywhere with almost no tint. If you overload the plaster '
                      'with heavy pigment, the surface turns dark and muddy, absorbing the light '
                      'instead of sharing it. The sweet spot creates radiant, velvety color.',
 'distill_diagram': {'analogy_title': 'The Buttercup Glow Cavity',
                     'analogy_sub': 'Bounced light between textured surfaces dyes the surrounding '
                                    'air',
                     'force_a_title': 'Solar Angle Knob (θ_sun)',
                     'force_a_sub': 'Drives beam depth, penetration angle, and water caustics '
                                    'movement',
                     'force_b_title': 'Pigment Ratio Knob (K/S)',
                     'force_b_sub': 'Balances wavelength absorption against crystal lattice '
                                    'scattering',
                     'threshold_title': 'Chosen Pigment Ratio (K/S = 0.48, design value)',
                     'threshold_pass': 'Matte diffuse color with about +31% bounce gain '
                                       '(illustrative)',
                     'threshold_fail': 'Specular glare below 0.1 or dark muddy absorption above '
                                       '2.0'},
 'act2_intuition': "Why does a mineral lime-wash wall in Barragán's Casa Gilardi feel velvety and "
                   'luminous, whereas an acrylic latex wall of the same RGB hex value feels flat '
                   'and plastic? In a rough mineral lime plaster (CSI 09 24 00 / 09 91 00), '
                   'calcite micro-crystals scatter incident electromagnetic waves across visible '
                   'wavelengths internally with scattering coefficient S, while iron-oxide, '
                   'ultramarine, or cochineal pigments absorb complementary wavelengths with '
                   'absorption coefficient K. In the two-flux theory of Paul Kubelka and Franz '
                   'Munk, an opaque layer has diffuse reflectance R_inf = 1 + (K/S) - '
                   'sqrt((K/S)^2 + 2(K/S)) (Kubelka 1948, DOI 10.1364/JOSA.38.000448); at K/S = '
                   '0.48 this gives 0.389. When sunlight at elevation angle theta_sun strikes '
                   'Wall 1 with reflectance spectrum rho_1(lambda) facing Wall 2 with '
                   'rho_2(lambda), and the view factors between them are F_12 and F_21, the '
                   'geometric series of mutual bounces multiplies the light in each band by '
                   '(1 - rho_1(lambda) * rho_2(lambda) * F_12 * F_21)^(-1). Bands the walls '
                   'reflect strongly gain most, which is the folio\'s simplified account of why '
                   'the bounced light looks more strongly colored; it is a model, not a '
                   'measurement of these rooms. '
                   'Simultaneously, Fresnel reflection off the interior water pool '
                   'R_water(theta_sun) redirects incident solar rays onto the ceiling, forming '
                   'dynamic caustics that dance across the textured stucco and heighten spatial '
                   'depth throughout the afternoon.',
 'act2_deepening': 'The nonlinear magic of this architectural cavity lies in the spectral coupling '
                   'between the solar angle knob and the pigment ratio knob. When the sun is high '
                   'at midday, the incident solar vector directs an intense beam onto the cobalt '
                   'pool, where Fresnel reflectance generates upward secondary illumination with '
                   'high short-wavelength energy. This blue-weighted flux hits the ceiling and '
                   'spills onto the upper half of the freestanding Rosa Mexicano wall. Because the '
                   "pigment's absorption coefficient K is low for red wavelengths but high for "
                   'blue, the wall absorbs the short waves while backscattering long red '
                   'wavelengths across the room. In the model, each successive reflection removes '
                   'more of the weakly reflected bands, so the bounced light becomes more strongly '
                   'colored even as it grows dimmer; raising K/S makes each wall darker overall but '
                   'its color purer. This is the folio\'s qualitative reading of the formula, not a '
                   'measured result.',
 'walkthrough': ['Experiment 1 (Solar Shaft & Casa Gilardi Pool): Sweep Incident Solar Elevation '
                 'theta_sun from 18 deg (low golden afternoon sun) to 68 deg (high Mexican '
                 'zenith). Watch the sunlight shaft move across the Rosa Mexicano wall into the '
                 'cobalt water plane.',
                 'Experiment 2 (Kubelka–Munk Pigment Ratio K/S): Adjust Pigment '
                 'Absorption-to-Scattering Ratio K/S from 0.12 (chalky pastel lime wash, R_inf = '
                 '0.62) to 1.40 (saturated mineral wash, R_inf = 0.22) and inspect the model '
                 'multi-bounce spectrum.',
                 'Experiment 3 (Barragán & Albers 4-Stage Chromatic Sequence): Click Stages 1 to 4 '
                 'to trace golden corridor spectral pre-filtering, Kubelka–Munk subsurface pigment '
                 'scattering, Fredholm wall-to-water radiosity coupling, and Torres de Satélite '
                 'kinetic parallax.'],
 'act4_title': 'Act IV — Chromatic Tectonics, Automotive Sculpture & Upstream Discovery Threads',
 'act4_human_ai': 'Spectral renderers can solve the radiosity equation band by band, for example '
                  'in 81 bands from 380 to 780 nm in 5 nm steps, instead of three RGB channels. '
                  'That keeps more of the difference between pigments under changing skies; this '
                  'folio describes the approach and did not run such a renderer.',
 'act4_deepening': 'A proposal, not a description of current practice: designers could pair '
                   'wavelength-resolved radiosity solvers with optimization tools to explore window '
                   'openings, ceiling geometry and pigment choices together, checking glare and '
                   'overheating as they go. Open questions remain in materials science: can '
                   'bio-based mineral binders match the self-healing behavior reported for '
                   'historic lime plasters while meeting modern low-carbon schedules? This folio '
                   'makes no claim about how colored rooms affect health or recovery.',
 'cf_bridge': 'This folio has no Cystic Fibrosis bridge. It is a standalone architecture folio '
              'and a thread across pillars on color as an electromagnetic wave: Architecture '
              '(Luis Barragán and Josef Albers), Physics (Folio P.08 on thin-film interference in '
              "car finishes, in contrast to Barragán's matte lime) and Mathematics (Folio M.08 on "
              'color geometry). It makes no health claim.',
 'sources': ['Barragán, L. (1980). Pritzker Architecture Prize acceptance speech. The Pritzker '
             'Architecture Prize.',
             'Kubelka, P. (1948). New contributions to the optics of intensely light-scattering '
             'materials. Part I. Journal of the Optical Society of America, 38(5), 448–457. DOI: '
             '10.1364/JOSA.38.000448.',
             'Albers, J. (1963). Interaction of Color. Yale University Press, New Haven.',
             'Zanco, F. (Ed.). (2001). Luis Barragán: The Quiet Revolution. Barragan Foundation / '
             'Vitra Design Museum.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Luis Barragan Casa '
        'Gilardi chromatic radiosity section showing golden corridor light, Rosa Mexicano wall, '
        'and cobalt pool">\n'
        '            <rect x="45" y="24" width="110" height="162" fill="#f3c64d" '
        'fill-opacity="0.28" stroke="currentColor" stroke-width="1.5"/>\n'
        '            <rect x="155" y="24" width="245" height="118" fill="var(--tp-stone)" '
        'stroke="currentColor" stroke-width="1.5"/>\n'
        '            <rect x="155" y="142" width="245" height="44" fill="#1b4d89" '
        'fill-opacity="0.82" stroke="var(--tp-prussian)" stroke-width="1.5"/>\n'
        '            <rect id="tp-a07-rosa-wall" x="285" y="42" width="26" height="128" '
        'fill="#d6336c" stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '            <polygon id="tp-a07-sun-shaft" points="185,24 235,24 311,142 255,142" '
        'fill="#ffd43b" fill-opacity="0.38" stroke="#f59f00" stroke-width="1.5" '
        'stroke-dasharray="4,3"/>\n'
        '            <path id="tp-a07-radiosity-arc" d="M 285 105 Q 225 118 210 142" fill="none" '
        'stroke="#d6336c" stroke-width="2.2" stroke-dasharray="3,3"/>\n'
        '            <text x="54" y="44" font-size="10" font-weight="600" '
        'fill="currentColor">Ochre Hall (582 nm)</text>\n'
        '            <text x="168" y="44" font-size="10" font-weight="600" '
        'fill="currentColor">Casa Gilardi Pool Court</text>\n'
        '            <text x="168" y="168" font-size="10" fill="#ffffff">Cobalt Water Plane (465 '
        'nm)</text>\n'
        '            <text id="tp-a07-wall-label" x="168" y="204" font-size="10.5" '
        'fill="var(--tp-prussian)">Kubelka–Munk R_∞ = 0.389 · Bounce Gain ≈ +31% '
        '(model)</text>\n'
        '            <line x1="420" y1="24" x2="420" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="435" y="34" font-size="11" font-weight="600" '
        'fill="currentColor">Spectral Reflectance R(λ) · 380–780 nm Waves</text>\n'
        '            <path d="M 435 165 Q 485 62 535 152 Q 585 168 635 72" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="2.2" stroke-dasharray="4,3"/>\n'
        '            <path id="tp-a07-km-curve" d="M 435 158 Q 515 162 565 110 Q 605 55 645 48" '
        'fill="none" stroke="var(--tp-minium)" stroke-width="2.8"/>\n'
        '            <text x="438" y="182" font-size="9.5" fill="var(--tp-prussian)">465 nm Cobalt '
        'Peak</text>\n'
        '            <text x="545" y="182" font-size="9.5" fill="var(--tp-minium)">615 nm Rosa '
        'Mexicano Wave</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a Luis Barragan inspired architectural courtyard '
        'with a Rosa Mexicano mineral stucco wall, golden corridor sunlight shaft, and cobalt-blue '
        'reflecting pool would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.07-V (Imagining What It Would Look Like) · Artistic '
            "architectural homage imagining Luis Barragán's chromatic tectonics: a shaft of "
            'Mexican sunlight striking a matte Rosa Mexicano lime-stucco pier rising from a '
            'tranquil cobalt-ultramarine indoor pool.'}

DISPATCH = {'kicker': 'FRONTIER CHROMATIC ARCHITECTURE DISPATCH · LUIS BARRAGÁN, JOSEF ALBERS & SPECTRAL '
           'RADIOSITY',
 'headline': "A Kubelka–Munk and Radiosity Reading of Luis Barragán's Architecture of "
             'Color',
 'body': "Using Paul Kubelka's two-flux pigment scattering theory (JOSA DOI "
         "10.1364/JOSA.38.000448) alongside Josef Albers's Interaction of Color (1963), this "
         "folio models how matte colored walls in rooms like Luis Barragán's Casa Gilardi "
         '(1976) reflect and inter-reflect light: R_∞ = 0.389 at K/S = 0.48, and an '
         'illustrative bounce gain of about +31% for an assumed view factor. It measured no '
         'building.'}

META_3D = ('Luis Barragán Kubelka–Munk Chromatic Radiosity Basin',
 'X: Pigmented Stucco K/S Ratio · Z: Courtyard Bounces · Y: Spectral Reflectance & Hue Shift')

ES_TRANSLATION = {'title_es': 'Tectónica Cromática de Luis Barragán, Radiosidad de Pigmentos de Kubelka–Munk y '
             'Campos de Onda Espaciales',
 'subtitle_es': 'Cómo Luis Barragán, junto con su amigo Chucho Reyes Ferreira, trabajó con colores '
                'intensos (rosa mexicano, azul cobalto, ocre) y la luz de México, y cómo Josef '
                'Albers enseñó la relatividad del color, leído aquí con un modelo sencillo de '
                'dispersión de pigmentos e interreflexión.',
 'why_es': 'Acercar una flor amarilla bajo la barbilla proyecta un resplandor dorado sobre la piel '
           'porque la luz rebota entre los pétalos; Barragán escaló ese fenómeno a muros de cal y '
           'espejos de agua que tiñen la luz del espacio.',
 'bridge_es': 'Esta ficha no tiene puente con la Fibrosis Quística: es una ficha de arquitectura '
              'que conecta con otras sobre el color como onda electromagnética, y no hace '
              'afirmaciones de salud.',
 'plain_es': 'En palabras sencillas, imaginen lo que sucede cuando la luz del sol entra a una '
             'habitación pintada. La pintura brillante moderna puede reflejar un destello '
             'que cansa la vista. Luis Barragán buscó lo contrario: muros mate de color '
             'intenso, como el rosa mexicano, el azul cobalto y el amarillo ocre. En el modelo de '
             'esta ficha, el color va mezclado en un aplanado rústico de cal apagada y arena '
             'volcánica. Al no tener barniz brillante, los rayos del sol penetran '
             'entre millones de cristales microscópicos de cal antes de rebotar suavemente en '
             'todas direcciones. Cuando dos muros con estas texturas se colocan frente a frente, '
             'como en la célebre alberca interior de la Casa Gilardi, la luz rebota una y otra vez '
             'entre el agua y los aplanados, llenando el espacio de un resplandor de color. En '
             'la obra de Barragán el color no es un simple adorno, sino parte de la arquitectura.',
 'deep_es': 'A nivel físico y matemático, esta atmósfera luminosa surge del acoplamiento entre dos '
            'fuerzas: la dispersión cristalina de la cal y la absorción espectral del pigmento '
            'mineral, descritas por la ecuación de transferencia radiativa de Kubelka–Munk. Si la '
            'proporción entre absorción y dispersión es demasiado baja, el muro luce blanquecino y '
            'sin vida; si es excesiva, la superficie se torna oscura y absorbe la luz en lugar de '
            'multiplicarla. Con una proporción de 0.48, la reflectancia del modelo es 0.389, y '
            'con un factor de vista supuesto de 0.61 los rebotes entre el muro y el agua aumentan '
            'la luz reflejada en cerca de 31 por ciento; es un valor ilustrativo del modelo, no '
            'una medición. Un proyectista podría combinar simulaciones de radiosidad espectral con '
            'aplanados artesanales de cal apagada. Esta ficha no afirma efectos del color sobre '
            'la salud.'}
