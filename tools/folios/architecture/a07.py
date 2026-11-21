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
 'subtitle': 'How Luis Barragán and Jesús \'Chucho\' Reyes Ferreira worked with saturated color '
             '(Rosa Mexicano, cobalt blue, ochre) and Mexican daylight (Zanco 2001), alongside '
             "Josef Albers's color relativity (1963)—modeled here via Kubelka–Munk scattering "
             '(DOI 10.1364/JOSA.38.000448) and diffuse radiosity (Goral et al. 1984, DOI '
             '10.1145/800031.808601).',
 'date_published': '2026-11-02',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'CHROMATIC ARCHITECTURE · REV 1.1',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'K/S = (1 − R_∞)² / (2 R_∞) · B(x,λ) = E(x,λ) + ρ(x,λ) ∫ B(y,λ) F(x,y) dA_y · '
                  'CSI 09 24 00',
 'colophon': {'identifier': 'A.07 · Barragán Chromatic Tectonics & Radiosity · CSI 09 24 00',
              'kernels': 'Kubelka–Munk Two-Flux Law · Fredholm Diffuse Radiosity',
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
 'steps': ['Stage 1 (Corridor Spectral Filtering, λ ≈ 582 nm): In Casa Gilardi (1976; Coelho 2015, '
           'DOI 10.4000/ambiances.606), daylight passing yellow glazing loses short-wave blue light; '
           'about 582 nm is an illustrative dominant wavelength.',
           'Stage 2 (Kubelka–Munk Scattering): For K/S = 0.48, Kubelka\'s infinite-thickness equation '
           '(1948, DOI 10.1364/JOSA.38.000448) gives R_∞ = 1 + K/S − √((K/S)² + 2 K/S) = 0.389, '
           'assuming a matte Lambertian layer.',
           'Stage 3 (Enclosure Inter-Reflection): Following the diffuse radiosity balance (Goral et al. '
           '1984, DOI 10.1145/800031.808601), a one-parameter enclosure series with effective return '
           'factor F_12 = 0.61 gives gain 1 / (1 − R_∞ F_12) − 1 ≈ +31.1% (multiplier 1.311) at '
           'R_∞ = 0.389—an illustrative model value, not a measured color shift.',
           'Stage 4 (Torres de Satélite Parallax & Albers Contrast): Built by Barragán and Mathias '
           'Goeritz (1957–58; Pelletier 2008, DOI 10.1111/j.1531-314X.2008.00234.x), the towers—the '
           'tallest about 52 m—shift silhouette from moving cars while juxtaposed planes illustrate '
           'relational contrast (Albers 1963).'],
 'readouts': [{'label': 'Kubelka–Munk Reflectance (R_∞, Model)', 'value': '0.389 (at K/S = 0.48)'},
              {'label': 'Inter-Reflection Gain (Illustrative)', 'value': '+31.1% (assumed F_12 = 0.61)'},
              {'label': 'Dominant Wavelength Pair (Illustrative)', 'value': '615 nm Rosa · 465 nm Cobalt'},
              {'label': 'Surface Assumption (Model)', 'value': 'LAMBERTIAN SURFACES ASSUMED'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 09 24 00 / 09 91 00',
                'title': 'Slaked Lime Stucco & Mineral Pigment Wash (Design Proposal)',
                'body': 'Three-coat slaked calcium-hydroxide lime plaster (Ca(OH)2 carbonating to CaCO3 '
                        'calcite; Cultrone et al. 2005, DOI 10.1016/j.cemconres.2004.12.012) with '
                        'porous vapor permeability (Parra-Fernández & Varas-Muriel 2025, DOI '
                        '10.3989/mc.2025.379124; hydraulic lime permeability in Isebaert et al. '
                        '2016, DOI 10.1617/s11527-016-0829-1) and mineral oxide pigments.',
                'meta': 'Design proposal · K/S = 0.48 and 85° gloss < 2 GU are targets, not '
                        'measurements'},
 'sidenote_1': {'kicker': 'SIDENOTE A.07-A · BARRAGÁN, CHUCHO REYES & TORRES DE SATÉLITE',
                'body': "Painter and collector Jesús 'Chucho' Reyes Ferreira influenced Luis Barragán's "
                        'palette (Zanco 2001). Torres de Satélite (1957–58), by Barragán and Mathias '
                        'Goeritz, stands beside a highway for moving viewers; the tallest tower rises '
                        'about 52 m (Pelletier 2008, DOI 10.1111/j.1531-314X.2008.00234.x).'},
 'sidenote_2': {'kicker': 'SIDENOTE A.07-B · SPECIFICATION PLATE · CSI 09 24 00 / CARBONATED LIME',
                'body': 'Unlike film-forming acrylic paints, carbonated lime plaster builds a porous '
                        'CaCO3 calcite network (Cultrone et al. 2005, DOI '
                        '10.1016/j.cemconres.2004.12.012) that transmits water vapor '
                        '(Parra-Fernández & Varas-Muriel 2025, DOI 10.3989/mc.2025.379124) and '
                        'scatters light isotropically via Kubelka–Munk transfer (DOI '
                        '10.1364/JOSA.38.000448).'},
 'skill': {'filename': 'barragan-kubelka-munk-radiosity-SKILL.md',
           'name': 'barragan-kubelka-munk-radiosity',
           'description': 'AI-agnostic architectural daylighting and color-physics skill for Luis '
                          'Barragan chromatic tectonics, Kubelka-Munk pigment reflectance, and '
                          'Fredholm diffuse radiosity.',
           'rules': ['Compute infinite-thickness Kubelka-Munk diffuse reflectance R_inf = 1 + '
                     '(K/S) - sqrt((K/S)^2 + 2*(K/S)) from absorption K and scattering S '
                     '(Kubelka 1948, DOI 10.1364/JOSA.38.000448).',
                     'Solve wavelength-resolved diffuse radiosity B_i(lambda) = E_i(lambda) + '
                     'rho_i(lambda) * sum_j F_ij * B_j(lambda) across 380-780 nm (Goral et al. '
                     '1984, DOI 10.1145/800031.808601; Ruppertsberg & Bloj 2008, DOI '
                     '10.3758/BRM.40.1.304).',
                     'Specify matte, vapor-permeable lime plaster (Cultrone et al. 2005, DOI '
                     '10.1016/j.cemconres.2004.12.012; Parra-Fernández & Varas-Muriel 2025, DOI '
                     '10.3989/mc.2025.379124) with an unmeasured 85-degree gloss < 2 GU target so '
                     'diffuse bounce dominates over specular glare.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The Kubelka–Munk '
                           'reflectance at K/S = 0.48 is corrected from 0.391 to 0.389 (and 0.21 to '
                           '0.22 at K/S = 1.40), and the chroma gain (+31.1% at F_12 = 0.61) is now '
                           'labeled an illustrative value with its assumed view factor. Claims that '
                           'tuned color regulates melanopsin pathways and calms patients, the PASS '
                           'verdict, unsourced anecdotes (gouache tests, 80 km/h) and an '
                           'invented-looking quotation are withdrawn; two uncited sources were removed.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; Scite '
                        'found no paper supporting a saturation gain from inter-reflection, so it is '
                        'labeled the folio\'s own model.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-02',
                'summary': 'REV 1.0 (Published 2026-11-02): Inaugural Volume IV architectural '
                           "color monograph uniting Luis Barragan's Casa Gilardi & Torres de "
                           "Satelite, Josef Albers's Interaction of Color, and Paul Kubelka's "
                           'radiative scattering law (DOI 10.1364/JOSA.38.000448).',
                'opus': 'Initial model review (2026-11-02; Gemini 4 Argon + Qwen 3.8 27B). Its '
                        "earlier 'verified' wording is withdrawn in REV 1.1: R_inf at K/S = 0.48 is "
                        '0.389, not 0.3912, and the cavity amplification was not computed.'}],
 'volume': 4,
 'volume_code': 'VOL. 04',
 'reading_time': '20 MIN READ',
 'word_count': '4,410 WORDS',
 'scite': {'doi': '10.1364/JOSA.38.000448',
           'fetched_on': '2026-11-21',
           'citing_publications': 2805,
           'supporting': 15,
           'mentioning': 1209,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Kubelka, New contributions to the optics of intensely light-scattering materials, Part I (DOI 10.1364/JOSA.38.000448), checked 2026-11-21: 2,805 citing publications (15 supporting, 1,209 mentioning, 0 contrasting) and no retraction notice. The paper is about scattering layers; it says nothing about architecture or this folio\'s numbers.'}}

LONGFORM_DATA = {'reading_time': '20 MIN READ',
 'word_count': '4,330 WORDS',
 'scite': {'doi': '10.1364/JOSA.38.000448',
           'fetched_on': '2026-11-21',
           'citing_publications': 2805,
           'supporting': 15,
           'mentioning': 1209,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Kubelka, New contributions to the optics of intensely light-scattering materials, Part I (DOI 10.1364/JOSA.38.000448), checked 2026-11-21: 2,805 citing publications (15 supporting, 1,209 mentioning, 0 contrasting) and no retraction notice. The paper is about scattering layers; it says nothing about architecture or this folio\'s numbers.'},
 'act1_title': "Act I — Luis Barragán's Chromatic Architecture, Chucho Reyes, Josef Albers & "
               'Diffuse Radiosity',
 'act1_dropcap': 'In Casa Gilardi in Tacubaya, Mexico City (1976), a yellow-glazed corridor leads to '
                 'an indoor pool where a freestanding red wall rises from the water against blue '
                 'walls (Zanco 2001; Coelho 2015, DOI 10.4000/ambiances.606). Trained as an '
                 'engineer in Guadalajara, Luis Barragán worked with saturated mineral walls and '
                 'enclosed gardens (Zanco 2001), receiving the 1980 Pritzker Architecture Prize '
                 'with an acceptance speech on beauty, silence, and serenity (Barragán 1980). '
                 "Painter Jesús 'Chucho' Reyes Ferreira and sculptor Mathias Goeritz—whose 1953 "
                 "manifesto framed 'emotional architecture'—shaped his palette and spatial work "
                 '(Zanco 2001; Pelletier 2008, DOI 10.1111/j.1531-314X.2008.00234.x).',
 'act1_plain_bridge': 'Everyday picture: shiny acrylic paint behaves like a shallow mirror, throwing '
                      'glare off a flat plastic film. In the design model here, rough lime plaster '
                      'carbonates into a porous calcite crystal network (Cultrone et al. 2005, DOI '
                      '10.1016/j.cemconres.2004.12.012) that scatters daylight across interior '
                      'grains (Kubelka 1948, DOI 10.1364/JOSA.38.000448). When two matte colored '
                      'walls face each other across a courtyard or pool (Zanco 2001; Coelho 2015, '
                      'DOI 10.4000/ambiances.606), mutual diffuse reflection could transfer color '
                      'between surfaces (Goral et al. 1984, DOI 10.1145/800031.808601).',
 'act1_body': 'Across Casa Estudio (1948), Torres de Satélite (1957–58, with Goeritz; Pelletier '
              '2008, DOI 10.1111/j.1531-314X.2008.00234.x), Cuadra San Cristóbal (1966–68), and '
              'Casa Gilardi (1976; Coelho 2015, DOI 10.4000/ambiances.606), Barragán paired large '
              'Rosa Mexicano, cobalt, and ochre planes (Zanco 2001). The dominant wavelengths '
              'assigned here (about 615 nm, 465 nm, and 582 nm) are illustrative model choices, not '
              'yet measured in the buildings. At Black Mountain College and Yale, Josef Albers '
              '(1963) showed through classroom exercises that apparent hue and lightness depend on '
              'surrounding surfaces. In physical rendering, diffuse inter-reflection follows '
              'Kubelka–Munk two-flux scattering (Kubelka 1948, DOI 10.1364/JOSA.38.000448; Kubelka '
              '1954, DOI 10.1364/JOSA.44.000330) coupled to the Fredholm radiosity integral '
              'B(x, λ) = E(x, λ) + ρ(x, λ) ∫ B(y, λ) F(x, y) dA_y (Goral et al. 1984, DOI '
              '10.1145/800031.808601; Cohen & Greenberg 1985, DOI 10.1145/325165.325171).',
 'act1_stakes': 'Traditional aerial and hydraulic lime mortars carbonate into porous calcite '
                '(Cultrone et al. 2005, DOI 10.1016/j.cemconres.2004.12.012) with high water-vapor '
                'permeability that lets masonry dry (Isebaert et al. 2016, DOI '
                '10.1617/s11527-016-0829-1; Parra-Fernández & Varas-Muriel 2025, DOI '
                '10.3989/mc.2025.379124). By contrast, dense film-forming coatings restrict vapor '
                'transfer and may create specular highlights, while standard three-channel RGB '
                'workflows miss wavelength-dependent metamerism and color bleed (Goral et al. 1984, '
                'DOI 10.1145/800031.808601; Ruppertsberg & Bloj 2008, DOI '
                '10.3758/BRM.40.1.304).',
 'pullquote': 'Editorial note: in Casa Gilardi, light reflected between the freestanding red wall and '
              'the blue pool models mutual diffuse radiosity (Coelho 2015, DOI '
              '10.4000/ambiances.606; Goral et al. 1984, DOI 10.1145/800031.808601).',
 'chronology': [('1931 / 1948',
                 'Paul Kubelka & Franz Munk (1931) and Kubelka (1948, DOI '
                 '10.1364/JOSA.38.000448) derive two-flux diffuse reflectance for scattering '
                 'coatings, extended to nonhomogeneous layers in 1954 (DOI '
                 '10.1364/JOSA.44.000330).'),
                ('1957–58',
                 'Luis Barragán & Mathias Goeritz build Torres de Satélite beside a highway near '
                 'Mexico City, concrete towers up to about 52 m tall for moving observers '
                 '(Pelletier 2008, DOI 10.1111/j.1531-314X.2008.00234.x).'),
                ('1963',
                 'Josef Albers publishes Interaction of Color at Yale University Press, '
                 'documenting simultaneous contrast and chromatic relativity (Albers 1963).'),
                ('1976 / 1984',
                 'Barragán completes Casa Gilardi (Coelho 2015, DOI 10.4000/ambiances.606); '
                 'Goral et al. (1984, DOI 10.1145/800031.808601) formulate diffuse radiosity for '
                 'architectural color bleed.')],
 'act2_title': 'Act II — How It Works: Kubelka–Munk Scattering + Diffuse Radiosity Inter-Reflection',
 'act2_analogy': 'Hold a yellow flower beneath your chin in sunlight and bounced light warms your '
                 'skin: the petals absorb short-wave blue light and scatter yellow toward nearby '
                 'surfaces. This folio models matte lime walls by Kubelka–Munk scattering (1948, '
                 'DOI 10.1364/JOSA.38.000448) and models mutual bounce across an enclosure—where '
                 'still water reflects specularly in reality and is idealized as Lambertian here—by '
                 'diffuse radiosity (Goral et al. 1984, DOI 10.1145/800031.808601).',
 'act2_plain_primer': 'Two model controls shape the courtyard balance below. Solar elevation θ_sun '
                      'rotates the incoming beam onto the wall and pool, shifting where direct '
                      'illumination lands. Pigment ratio K/S sets absorption relative to scattering '
                      'in Kubelka\'s equation (1948, DOI 10.1364/JOSA.38.000448): very low K/S '
                      'approaches chalky white reflectance, whereas large K/S darkens the wall by '
                      'absorbing light before it can bounce to neighbors.',
 'distill_diagram': {'analogy_title': 'Mutual Diffuse Radiosity Cavity',
                     'analogy_sub': 'Matte mineral surfaces exchange wavelength-filtered bounces',
                     'force_a_title': 'Solar Angle Knob (θ_sun)',
                     'force_a_sub': 'Sets beam strike angle on wall and water plane',
                     'force_b_title': 'Pigment Ratio Knob (K/S)',
                     'force_b_sub': 'Balances pigment absorption K against lime scattering S',
                     'threshold_title': 'Chosen Pigment Ratio (K/S = 0.48, design value)',
                     'threshold_pass': 'Matte diffuse color with about +31% bounce gain '
                                       '(illustrative)',
                     'threshold_fail': 'Chalky low-K/S washout below 0.1 or dark absorption above '
                                       '2.0'},
 'act2_intuition': 'In a carbonated lime plaster (CSI 09 24 00 / 09 91 00; Cultrone et al. 2005, '
                   'DOI 10.1016/j.cemconres.2004.12.012), calcite micro-crystals scatter visible '
                   'light with coefficient S while mineral pigments absorb complementary bands with '
                   'coefficient K. For an optically thick matte layer, Kubelka (1948, DOI '
                   '10.1364/JOSA.38.000448) gives R_inf = 1 + (K/S) − sqrt((K/S)^2 + 2(K/S)), and '
                   'Kubelka (1954, DOI 10.1364/JOSA.44.000330) treats stacked or nonhomogeneous '
                   'layers; under the stated assumptions at K/S = 0.48, R_inf = 0.389. In a full '
                   'two-surface radiosity balance (Goral et al. 1984, DOI '
                   '10.1145/800031.808601; Cohen & Greenberg 1985, DOI 10.1145/325165.325171), '
                   'round-trip attenuation scales as ρ_1 ρ_2 F_12 F_21; collapsing the second '
                   'surface\'s effective return factor ρ_2 F_21 into a single enclosure parameter '
                   'F_12 = 0.61 (idealizing the water as Lambertian) gives multiplier '
                   '1 / (1 − R_inf · F_12) ≈ 1.311, or a bounce gain of about +31.1% above direct '
                   'illumination. That scalar factor is an illustrative enclosure model, not yet a '
                   'measurement of Casa Gilardi.',
 'act2_deepening': 'Both knobs interact spectrally across visible wavelengths (380–780 nm; '
                   'Ruppertsberg & Bloj 2008, DOI 10.3758/BRM.40.1.304). Changing θ_sun shifts '
                   'how much direct flux reaches the pool relative to the vertical stucco wall, '
                   'while changing K/S alters the per-bounce reflectance ρ(λ). In the model '
                   'series, bands with higher reflectance retain a larger share after each bounce, '
                   'which may shift the spectral balance of inter-reflected light even as total '
                   'radiosity falls; raising K/S lowers overall brightness. This is a qualitative '
                   'reading of the simplified equation, not a field photometric survey.',
 'walkthrough': ['Experiment 1 (Solar Elevation θ_sun): Sweep θ_sun from 18° to 68° to trace the '
                 'beam angle across the Rosa Mexicano wall and cobalt pool.',
                 'Experiment 2 (Kubelka–Munk Ratio K/S): Vary K/S from 0.12 (R_inf = 0.62) to '
                 '1.40 (R_inf = 0.22) using Kubelka (1948, DOI 10.1364/JOSA.38.000448) and '
                 'inspect the simulated bounce spectrum.',
                 'Experiment 3 (Four-Stage Sequence): Step through corridor filtering (Coelho '
                 '2015, DOI 10.4000/ambiances.606), Kubelka–Munk scattering, radiosity bounce '
                 '(Goral et al. 1984, DOI 10.1145/800031.808601), and Torres de Satélite '
                 'parallax (Pelletier 2008, DOI 10.1111/j.1531-314X.2008.00234.x).'],
 'act4_title': 'Act IV — Spectral Rendering, Lime Carbonation & Upstream Discovery Threads',
 'act4_human_ai': 'Physically based renderers such as RADIANCE can sample visible spectra across '
                  '380–780 nm (for example, in 5 nm steps) rather than three RGB channels '
                  '(Ruppertsberg & Bloj 2008, DOI 10.3758/BRM.40.1.304), alongside hemi-cube '
                  'form-factor solvers (Cohen & Greenberg 1985, DOI 10.1145/325165.325171). This '
                  'folio describes those methods and did not simulate a room with them.',
 'act4_deepening': 'Design proposal: architects could pair diffuse radiosity solvers (Goral et al. '
                   '1984, DOI 10.1145/800031.808601; Cohen & Greenberg 1985, DOI '
                   '10.1145/325165.325171) or spectral ray-tracing tools such as RADIANCE '
                   '(Ruppertsberg & Bloj 2008, DOI 10.3758/BRM.40.1.304) with vapor-permeable lime '
                   'mortar specifications (Cultrone et al. 2005, DOI '
                   '10.1016/j.cemconres.2004.12.012; Isebaert et al. 2016, DOI '
                   '10.1617/s11527-016-0829-1; Parra-Fernández & Varas-Muriel 2025, DOI '
                   '10.3989/mc.2025.379124) to estimate daylight color shifts alongside moisture '
                   'durability; any assembly remains untested. This folio makes no claim about how '
                   'colored rooms affect health or clinical outcomes.',
 'cf_bridge': 'A standalone architecture folio linking electromagnetic color across pillars: '
              'Architecture (Barragán 1980; Albers 1963; Coelho 2015, DOI '
              '10.4000/ambiances.606), Physics (Folio P.08 on thin-film interference), and '
              'Mathematics (Folio M.08 on David MacAdam\'s daylight ellipses, DOI '
              '10.1364/JOSA.32.000247, and Scite citation indexing, Nicholson et al. 2021, DOI '
              '10.1162/qss_a_00146). It makes no health claim.',
 'sources': ['Barragán, L. (1980). Pritzker Architecture Prize acceptance speech. The Pritzker '
             'Architecture Prize.',
             'Kubelka, P. (1948). New Contributions to the Optics of Intensely Light-Scattering '
             'Materials Part I. Journal of the Optical Society of America, 38(5), 448–457. DOI: '
             '10.1364/JOSA.38.000448.',
             'Kubelka, P. (1954). New Contributions to the Optics of Intensely Light-Scattering '
             'Materials Part II: Nonhomogeneous Layers. Journal of the Optical Society of America. '
             'DOI: 10.1364/JOSA.44.000330.',
             'Albers, J. (1963). Interaction of Color. Yale University Press, New Haven.',
             'Zanco, F. (Ed.). (2001). Luis Barragán: The Quiet Revolution. Barragan Foundation / '
             'Vitra Design Museum.',
             'Goral, C. M., Torrance, K. E., Greenberg, D. P., & Battaile, B. (1984). Modeling the '
             'interaction of light between diffuse surfaces. Proceedings of the 11th annual '
             'conference on Computer graphics and interactive techniques. DOI: '
             '10.1145/800031.808601.',
             'Cohen, M. F., & Greenberg, D. P. (1985). The hemi-cube. ACM SIGGRAPH Computer '
             'Graphics. DOI: 10.1145/325165.325171.',
             'Cultrone, G., Sebastián, E., & Ortega Huertas, M. (2005). Forced and natural '
             'carbonation of lime-based mortars with and without additives: Mineralogical and '
             'textural changes. Cement and Concrete Research. DOI: '
             '10.1016/j.cemconres.2004.12.012.',
             'Ruppertsberg, A. I., & Bloj, M. (2008). Creating physically accurate visual stimuli '
             'for free: Spectral rendering with RADIANCE. Behavior Research Methods. DOI: '
             '10.3758/BRM.40.1.304.',
             'Pelletier, L. (2008). Modeling the Void. Journal of Architectural Education. DOI: '
             '10.1111/j.1531-314X.2008.00234.x.',
             'Coelho, A. (2015). The Living Experience as a design content: from concept to '
             'appropriation. Ambiances. DOI: 10.4000/ambiances.606.',
             'Isebaert, A., De Boever, W., & Cnudde, V. (2016). An empirical method for the '
             'estimation of permeability in natural hydraulic lime mortars. Materials and '
             'Structures. DOI: 10.1617/s11527-016-0829-1.',
             'Parra-Fernández, S., & Varas-Muriel, M. J. (2025). Petrographic and petrophysical '
             'characterization of the main aerial and hydraulic mortars used in the construction '
             'and rehabilitation sectors. Materiales de Construcción. DOI: '
             '10.3989/mc.2025.379124.',
             'MacAdam, D. L. (1942). Visual Sensitivities to Color Differences in Daylight. '
             'Journal of the Optical Society of America, 32(5), 247–274. DOI: '
             '10.1364/JOSA.32.000247.',
             'Nicholson, J. M., Mordaunt, M., Lopez, P., et al. (2021). scite: A smart citation '
             'index that displays the context of citations and classifies their intent using deep '
             'learning. Quantitative Science Studies, 2(3), 882–898. DOI: 10.1162/qss_a_00146.'],
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

DISPATCH = {'kicker': 'FRONTIER CHROMATIC ARCHITECTURE DISPATCH · LUIS BARRAGÁN, JOSEF ALBERS & DIFFUSE '
           'RADIOSITY',
 'headline': "A Kubelka–Munk and Radiosity Reading of Luis Barragán's Architecture of "
             'Color',
 'body': "Combining Paul Kubelka's two-flux scattering law (1948, DOI 10.1364/JOSA.38.000448), "
         'diffuse radiosity (Goral et al. 1984, DOI 10.1145/800031.808601), and Josef '
         "Albers's Interaction of Color (1963), this folio models how matte walls in rooms such "
         'as Casa Gilardi (Coelho 2015, DOI 10.4000/ambiances.606) inter-reflect light: '
         'R_∞ = 0.389 at K/S = 0.48 and an illustrative +31.1% bounce gain at F_12 = 0.61. '
         'No building was measured.'}

META_3D = ('Luis Barragán Kubelka–Munk Chromatic Radiosity Basin',
 'X: Pigmented Stucco K/S Ratio · Z: Courtyard Bounces · Y: Spectral Reflectance & Hue Shift')

ES_TRANSLATION = {'title_es': 'Tectónica Cromática de Luis Barragán, Radiosidad de Pigmentos de Kubelka–Munk y '
             'Campos de Onda Espaciales',
 'subtitle_es': 'Cómo Luis Barragán y Chucho Reyes Ferreira trabajaron con color intenso y luz natural '
                '(Zanco 2001), junto con la relatividad cromática de Josef Albers (1963), modelados '
                'mediante Kubelka–Munk (DOI 10.1364/JOSA.38.000448) y radiosidad difusa (Goral et '
                'al. 1984, DOI 10.1145/800031.808601).',
 'why_es': 'Una flor amarilla bajo la barbilla refleja luz filtrada hacia la piel. Este modelo '
           'representa muros mate de cal con Kubelka–Munk (1948, DOI 10.1364/JOSA.38.000448) e '
           'intercambio entre muros y un espejo de agua idealizado como lambertiano mediante '
           'radiosidad difusa (Goral et al. 1984, DOI 10.1145/800031.808601).',
 'plain_es': 'En el modelo de esta ficha, la pintura acrílica brillante genera reflejos especulares, '
             'mientras que un aplanado mate de cal apagada carbonata en cristales porosos de '
             'calcita (Cultrone et al. 2005, DOI 10.1016/j.cemconres.2004.12.012) que dispersan '
             'la luz (Kubelka 1948, DOI 10.1364/JOSA.38.000448). Cuando dos muros mate se '
             'enfrentan en un patio o alberca como la Casa Gilardi (Zanco 2001; Coelho 2015, DOI '
             '10.4000/ambiances.606), la reflexión difusa mutua podría transferir color entre '
             'superficies (Goral et al. 1984, DOI 10.1145/800031.808601).',
 'deep_es': 'El modelo acopla la dispersión de Kubelka–Munk (1948, DOI 10.1364/JOSA.38.000448; '
            '1954, DOI 10.1364/JOSA.44.000330) con la radiosidad difusa entre superficies (Goral '
            'et al. 1984, DOI 10.1145/800031.808601; Cohen y Greenberg 1985, DOI '
            '10.1145/325165.325171). Bajo los supuestos indicados con K/S = 0.48, la reflectancia '
            'es R_∞ = 0.389, y con un factor de vista supuesto F_12 = 0.61 la serie geométrica da '
            'una ganancia ilustrativa cercana a +31.1 por ciento; no es una medición en obra. Un '
            'diseñador puede simular el espectro en 380–780 nm (Ruppertsberg y Bloj 2008, DOI '
            '10.3758/BRM.40.1.304) junto con morteros de cal (Parra-Fernández y Varas-Muriel 2025, '
            'DOI 10.3989/mc.2025.379124). Esta ficha no afirma efectos del color sobre la salud.'}
