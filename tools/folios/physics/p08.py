#!/usr/bin/env python3
"""Folio P.08 (PHYSICS): Electromagnetic Color Wave Physics: Bragg Thin-Film Interference, Gonioapparent Automotive Pearlescence & Barragán Stucco Optics."""
from __future__ import annotations

SLUG = 'p08'

PILLAR = 'physics'

FOLIO = {'category_code': 'P',
 'colophon': {'benchmarks': 'n_f = 2.45 (TiO₂) · d = 240 nm, m = 2 ⇒ λ_peak = 588 nm · Flop Δλ = −10.9 nm at 28°',
              'bridge': 'Automotive Gonioapparent Flop ↔ A.07 Barragán Stucco & M.08 Color '
                        'Geodesics',
              'identifier': 'P.08 · Electromagnetic Color Waves & BRDF · Optics',
              'kernels': 'Bragg–Snell Thin-Film Interference · Cook–Torrance Microfacet BRDF'},
 'current_edition': 'REV 1.1',
 'date_published': '2026-11-02',
 'date_redated': '2026-11-14',
 'folio_id': 'P.08',
 'governing_law': 'Δ_OPD = 2 d √(n_f² − sin²θ_i) = m λ · f_r = k_d(ρ/π) + k_s(D F G) / '
                  '[4(n·l)(n·v)]',
 'governing_law_latex': r"\Delta_{\mathrm{OPD}} = 2 d \sqrt{n_f^2 - \sin^2\theta_i} = m\lambda, \\ f_r = k_d \frac{\rho}{\pi} + k_s \frac{D F G}{4(n\cdot l)(n\cdot v)}",
 'kernel_verdict': 'Partial: 2 of 4 readouts recomputed',
 'kernel_verdict_es': 'Parcial: 2 de 4 lecturas recalculadas',
 'pillar': 'physics',
 'primary_kernel': 'tools/physics_kernel.py',
 'reading_time': '22 MIN READ',
 'readouts': [{'label': 'Constructive Peak Wavelength', 'value': 'λ_peak = 588 nm at 0° (m = 2)'},
              {'label': 'Angular Color-Flop Blue Shift', 'value': 'Δλ = −10.9 nm (at θ_i = 28°)'},
              {'label': 'Fresnel–Cook Specular Gain', 'value': 'F ≈ 0.18 (fixed illustrative value) · GGX α_r = 0.04'},
              {'label': 'Wave Interference Verdict', 'value': 'PEAK IN VISIBLE BAND (MODEL)'}],
 'revisions': [{'date': '2026-11-14',
                'edition': 'REV 1.1',
                'opus': 'Review: numbers recomputed by hand from the stated law by an independent reviewer.',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The numbers printed in REV 1.0 did '
                           'not follow from the folio law: 245 nm gives 600 nm, not 588 nm, and the shift at 28° is '
                           '−10.9 nm, not −24.2 nm. The film is now 240 nm read in second order, the colour '
                           'descriptions match the computed wavelengths, and the page says that the law neglects '
                           'the half-wave phase shift on reflection. The interactive lab had its two sliders '
                           'swapped and is fixed.'},
               {'date': '2026-11-02',
                'edition': 'REV 1.0',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'exact Snell-Bragg cos(theta_t) = sqrt(1 - sin^2(theta_i)/n_f^2) '
                        'blue-shift trajectory across 0-75 deg.',
                'summary': 'REV 1.0 (Published 2026-11-02): Inaugural Volume IV electromagnetic '
                           'color wave monograph uniting Bragg thin-film interference, '
                           'Cook-Torrance microfacet BRDFs (DOI 10.1145/357290.357293), automotive '
                           'pearlescence, and Barragan matte stucco.'}],
 'scite': {'doi': '10.1145/357290.357293',
           'fetched_on': '2026-11-08',
           'citing_publications': 1524,
           'supporting': 4,
           'mentioning': 405,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 1,524 '
                      'citing publications (4 supporting, 405 mentioning, 0 contrasting) on Robert '
                      "Cook & Kenneth Torrance's physical microfacet reflectance model for "
                      'wavelength-dependent Fresnel and interference color shifts.'},
 'sidenote_1': {'body': "A sports car's compound-curved fender sweeps surface normals n(x) through "
                        "90° in a single glance, turning the sin²θ_i term of the interference condition into a living sculpture of shifting wavelengths."
                        ' A flat 12-meter wall by Luis Barragán '
                        'has constant surface normal—so it relies on Kubelka–Munk diffuse cavity '
                        'bounces instead.',
                'kicker': 'SIDENOTE P.08-A · WHY CURVED CAR BODIES LOVE GONIOAPPARENT FLOP WHILE '
                          'WALLS LOVE MATTE'},
 'sidenote_2': {'body': 'The exact same Bragg–Snell equation Δ_OPD = 2 d √(n² − sin²θ) used to design pearlescent automotive pigments is the kind of relation that thin-film interferometry uses to estimate the thickness of thin transparent layers such as the tear film.',
                'kicker': 'SIDENOTE P.08-B · SPECIFICATION PLATE · THIN-FILM INTERFEROMETRY IN '
                          'BIOPHYSICS'},
 'skill': {'description': 'AI-agnostic wave-optics and surface-physics skill for Bragg thin-film '
                          'interference, gonioapparent automotive pearlescent color flop, and '
                          'Cook-Torrance vs. Lambertian BRDF modeling.',
           'filename': 'color-wave-bragg-brdf-SKILL.md',
           'name': 'color-wave-bragg-brdf',
           'rules': ['Calculate thin-film optical path difference Delta_OPD = 2 * d_film * '
                     'sqrt(n_f^2 - sin^2(theta_i)) and constructive interference peak wavelength '
                     'lambda_peak(theta_i).',
                     'Compute angular color-flop blue shift Delta_lambda(theta_i) = '
                     'lambda_peak(theta_i) - lambda_peak(0) as viewing angle theta_i increases '
                     'from normal (0 deg) to grazing.',
                     'Decompose surface reflectance via Cook-Torrance BRDF f_r = k_d*(rho/pi) + '
                     'k_s*(D_GGX * F_Schlick * G_Smith) / (4*(n.l)*(n.v)) to contrast specular '
                     'metallic coats with matte mineral plaster.']},
 'sliders': [{'label': 'Incident Viewing Angle (θ_i)',
              'max': 75.0,
              'min': 0.0,
              'step': 1.0,
              'unit': '°',
              'value': 28.0},
             {'label': 'TiO₂ Nano-Oxide Film Thickness (d_film)',
              'max': 360.0,
              'min': 140.0,
              'step': 5.0,
              'unit': ' nm',
              'value': 240.0}],
 'slug': 'p08',
 'spec_plate': {'body': 'Three-stage OEM/motorsport basecoat-pearlescent-clearcoat system '
                        '(synthetic fluorophlogopite mica platelets encapsulated in 240 nm rutile TiO2) benchmarked at 15°, 45°, and 110° aspecular angles per ASTM E2539.',
                'division': 'ASTM E2539 / AUTOMOTIVE & ARCHITECTURAL SPECTROPHOTOMETRY',
                'meta': 'Cook-Torrance BRDF (DOI 10.1145/357290.357293) · simplified thin-film condition (model)',
                'title': 'Multi-Angle (15° / 45° / 110°) Gonioapparent Pearlescent Clearcoat vs. '
                         'Mineral Matte Standard'},
 'status_badge': 'COLOR WAVE PHYSICS · REV 1.1',
 'steps': ['Stage 1 (Maxwell Transverse Electromagnetic Wave Packet): Incident white daylight '
           'carries continuous spectral modes λ ∈ [380, 780] nm across the clearcoat dielectric '
           'boundary.',
           'Stage 2 (Bragg–Snell Thin-Film Phase Addition): Inside a 240 nm TiO₂ nanolayer (n_f = 2.45) on mica platelets, optical path difference Δ_OPD = 2 d √(n_f² − sin²θ_i) = m λ selects, in second order (m = 2) at normal incidence, λ_peak = 588 nm.',
           'Stage 3 (Gonioapparent Automotive Blue-Shift Color Flop): Sweeping viewing angle θ_i '
           'from 0° to 65° along a curved car fender shrinks √(n_f² − sin²θ_i), shifting λ_peak blueward by about −42 nm for the 240 nm film.',
           'Stage 4 (Cook–Torrance Specular vs. Barragán Lambertian Limit): Low microfacet '
           "roughness (α_r = 0.04) concentrates metallic car highlights, while Barragán's calcite "
           'stucco (α_r = 0.88) scatters hue uniformly.'],
 'subtitle': 'How transverse electromagnetic waves (λ ∈ [380, 780] nm) produce angle-dependent '
             'color flop in TiO₂-mica automotive pearlescent finishes via Bragg interference vs. '
             "angle-invariant serenity in Luis Barragán's mineral lime walls.",
 'title': 'Electromagnetic Color Wave Physics: Bragg Thin-Film Interference, Gonioapparent '
          'Automotive Pearlescence & Barragán Stucco Optics',
 'volume': 4,
 'volume_code': 'VOL. 04',
 'word_count': '4,650 WORDS'}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1145/357290.357293',
           'fetched_on': '2026-11-08',
           'citing_publications': 1524,
           'supporting': 4,
           'mentioning': 405,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 1,524 '
                      'citing publications (4 supporting, 405 mentioning, 0 contrasting) on Robert '
                      "Cook & Kenneth Torrance's physical microfacet reflectance model for "
                      'wavelength-dependent Fresnel and interference color shifts.'},
 'act1_title': 'Act I — Color Is an Electromagnetic Wave: From Thomas Young & Bragg Interference '
               'to Automotive Pearlescent Lacquers & Barragán Stucco',
 'act1_dropcap': 'In the first years of the nineteenth century the English physician and polymath Thomas Young argued before the Royal Society of London that light is a wave. Isaac Newton had favored tiny corpuscles; Young proposed that color is a periodic vibration, and he used interference, including measurements of the colored rings seen in thin films, to estimate the wavelengths of visible light. Violet was a rapid flutter scarcely four hundred nanometers from '
                 'crest to crest, while deep red stretched out toward seven hundred nanometers. '
                 'Six decades later, James Clerk Maxwell showed that these luminous undulations '
                 'were oscillating electric and magnetic fields traveling across space, setting '
                 'the stage for how modern coatings manipulate light.',
 'act1_body': 'Consider two iconic masterpieces of human color craft that sit at opposite poles of '
              'electromagnetic wave physics: an Italian pearlescent race-car silhouette and a '
              'sun-drenched Rosa Mexicano lime-stucco wall by Luis Barragán (Folio A.07). In a '
              'modern multi-layer automotive pearlescent coat, synthetic mica platelets coated '
              'with a nanometric layer of high-index titanium dioxide (TiO2, refractive index n_f '
              '= 2.45, thickness d_film ~ 180–320 nm) are suspended parallel to the curved '
              "carbon-fiber bodywork. By the thin-film interference condition (Young, Fresnel),"
              ' the optical path difference between waves reflecting '
              'from the top and bottom of the TiO2 nanolayer is Delta_OPD = 2 d_film sqrt(n_f^2 - '
              'sin^2(theta_i)). As a viewer walks past a curved car fender or watches an F1 car '
              'corner, the incidence angle theta_i sweeps from 0 deg (normal) to 70 deg (grazing), '
              'shifting the constructive interference peak lambda_peak toward shorter wavelengths '
              "('blue-shift color flop') and coupling with Cook & Torrance's microfacet "
              'Bidirectional Reflectance Distribution Function (BRDF, DOI 10.1145/357290.357293). '
              "Conversely, Barragán's coarse volcanic-lime plaster intentionally destroys specular "
              'coherence via random Mie/Kubelka–Munk cavity scattering, holding dominant hue '
              'invariant across every viewing angle.',
 'pullquote': '"Walk around a pearlescent sports car and its curved bodywork shifts from yellow-gold toward green because oblique viewing shrinks the Bragg optical path '
              'difference; walk past a Luis Barragán stucco wall and its hue stands still like a '
              'monument."',
 'chronology': [('1801',
                 'Thomas Young presents his wave theory of light to the Royal Society and estimates the wavelengths of colors from interference in thin films; his double-slit demonstration follows a few years later.'),
                ('1865',
                 'James Clerk Maxwell shows light and color are transverse electromagnetic waves '
                 'governed by dielectric permittivity epsilon(omega).'),
                ('1913',
                 'William Henry Bragg & William Lawrence Bragg derive the crystal diffraction law 2 d sin(theta) = m lambda; its thin-film analogue with refraction, 2 d sqrt(n^2 - sin^2 theta) = m lambda, is the form this folio uses.'),
                ('1982',
                 'Robert L. Cook & Kenneth E. Torrance formulate the physical microfacet BRDF (DOI '
                 '10.1145/357290.357293) governing metallic automotive and architectural '
                 'rendering.')],
 'act2_title': 'Act II — How It Actually Works: Bragg–Fresnel Thin-Film Wave Interference vs. '
               'Microfacet BRDF',
 'act2_intuition': 'For a dielectric TiO2-coated mica flake of thickness d_film and refractive '
                   'index n_f = 2.45 embedded in clearcoat, this folio uses the simplified condition lambda_peak(theta_i) = (2 / m) * d_film * sqrt(n_f^2 - sin^2(theta_i)), read in second order (m = 2). It neglects the half-wave phase shift on reflection at the high-index boundary; including it would replace m by m - 1/2 and move every peak, so the wavelengths here are model values, not a pigment specification. Increasing the viewing angle theta_i '
                   'from 0 deg to 65 deg decreases cos(theta_t), shifting lambda_peak blueward by about 42 nm for the 240 nm film (\'gonioapparent flop\').'
                   " Meanwhile, the Cook–Torrance "
                   'BRDF f_r = k_d (rho / pi) + k_s (D_GGX * F_Fresnel * G_Smith) / (4 (n.l)(n.v)) '
                   "separates the angle-invariant Lambertian pigment lobe (dominant in Barragán's "
                   'mineral stucco, roughness alpha_r = 0.88) from the sharp specular microfacet '
                   'lobe (dominant in automotive clearcoats, alpha_r = 0.04). In the Cook–Torrance model the microfacet slope distribution sets the directional sharpness of specular highlights and the geometric term limits reflectance at grazing angles. Open spectral solvers such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) are general PDE tools, and the folio\'s references were checked in the Scite citation index (DOI 10.1162/qss_a_00146).',
 'act2_analogy': 'Everyday analogy: Think of a swirling soap bubble floating in the sun or the '
                 'iridescent throat feathers of a hummingbird. Neither has a single drop of '
                 'colorful ink inside them. Their brilliant, shifting colors come purely from '
                 'light waves bouncing off the front and back of an ultra-thin transparent skin. '
                 'When the two reflections overlap with their wave crests in lockstep, they '
                 'amplify one vivid color while canceling out all others—shifting hue whenever you '
                 'tilt your head.',
 'walkthrough': ['Experiment 1 (Automotive Gonioapparent Color Flop): Sweep Viewing Angle theta_i '
                 'from 0 deg (face-on normal view) to 68 deg (grazing fender horizon). Watch the '
                 'Bragg constructive interference wavelength lambda_peak shift blueward while '
                 'Fresnel specular reflectance surges.',
                 'Experiment 2 (TiO2 Nano-Coating Thickness Tuning): Drag Dielectric Oxide '
                 'Thickness d_film from 160 nm (model peak near 392 nm, violet) to 310 nm (model peak near 760 nm, deep red) and inspect the reflected electromagnetic wave '
                 'packet.',
                 'Experiment 3 (Automotive Pearl vs. Barragán Stucco BRDF): Click Stages 1 to 4 to '
                 'compare coherent Bragg thin-film phase addition, Cook–Torrance GGX microfacet '
                 "specular lobes, Mie subsurface pigment absorption, and Barragán's isotropic "
                 'Lambertian scatter.'],
 'act4_title': 'Act IV — Wave Optics in Design, AI Inverse Rendering & Upstream Discovery Threads',
 'act4_human_ai': 'Neural radiance fields and differentiable wave-optics shaders now embed exact '
                  'Bragg transfer-matrix interference and Cook–Torrance microfacet BRDFs so '
                  'automotive and architectural designers can inspect gonioapparent paint and '
                  'mineral facade samples under real sky domes before mixing a single gram of '
                  'pigment.',
 'cf_bridge': 'Standalone Wave Physics Flagship & Cross-Pillar Thread: Folio P.08 bridges Folio '
              "A.07 (Barragán's architectural pigment radiosity) and Folio M.08 (Riemannian "
              'differential geometry of color space). Upstream optical-physics case study: '
              'the exact Bragg–Snell thin-film interference law Delta_OPD = 2 d sqrt(n^2 - sin^2 '
              'theta) that creates color flop on a pearlescent car fender is the same physics that thin-film interferometry relies on when it estimates the thickness of thin transparent layers such as the tear film. No measurement of that kind is made or cited in this folio.',
 'sources': ['Young, T. (1802). On the theory of light and colours (Bakerian Lecture). '
             'Philosophical Transactions of the Royal Society of London, 92, 12–48.',
             'Cook, R. L., & Torrance, K. E. (1982). A reflectance model for computer graphics. '
             'ACM Transactions on Graphics, 1(1), 7–24. DOI: 10.1145/357290.357293.',
             'Maile, F. J., Pfaff, G., & Reynders, P. (2005). Effect pigments—new concepts, new '
             'technologies. Progress in Organic Coatings, 54(3), 150–163.',
             'Born, M., & Wolf, E. (1999). Principles of Optics: Electromagnetic Theory of '
             'Propagation, Interference and Diffraction of Light (7th ed.). Cambridge University '
             'Press.',
             'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). '
             'Dedalus: A flexible framework for numerical simulations with spectral methods '
             '(DedalusProject/dedalus, https://github.com/DedalusProject/dedalus). Physical Review '
             'Research, 2(2), 023068. DOI: 10.1103/PhysRevResearch.2.023068.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Bragg thin-film '
        'wave interference on an automotive TiO2-mica pearlescent flake vs Cook-Torrance and '
        'Barragan Lambertian BRDF lobes">\n'
        '            <rect x="45" y="95" width="295" height="32" fill="#2b50aa" '
        'fill-opacity="0.22" stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '            <rect x="45" y="127" width="295" height="22" fill="var(--tp-stone)" '
        'stroke="currentColor" stroke-width="1.5"/>\n'
        '            <line id="tp-p08-ray-in" x1="85" y1="32" x2="155" y2="95" stroke="#f59f00" '
        'stroke-width="2.5"/>\n'
        '            <line id="tp-p08-ray-ref1" x1="155" y1="95" x2="235" y2="32" '
        'stroke="var(--tp-verdigris)" stroke-width="2.5"/>\n'
        '            <line x1="155" y1="95" x2="188" y2="127" stroke="#f59f00" stroke-width="2" '
        'stroke-dasharray="3,2"/>\n'
        '            <line x1="188" y1="127" x2="221" y2="95" stroke="var(--tp-minium)" '
        'stroke-width="2" stroke-dasharray="3,2"/>\n'
        '            <line id="tp-p08-ray-ref2" x1="221" y1="95" x2="301" y2="32" '
        'stroke="var(--tp-minium)" stroke-width="2.5"/>\n'
        '            <text x="50" y="24" font-size="11" font-weight="600" '
        'fill="currentColor">Bragg Thin-Film Interference (Automotive TiO₂ Mica)</text>\n'
        '            <text x="55" y="115" font-size="10" fill="var(--tp-prussian)">TiO₂ Dielectric '
        'Layer (n_f = 2.45 · d_film = 240 nm)</text>\n'
        '            <text x="55" y="142" font-size="9.5" fill="currentColor">Mica / Aluminum '
        'Flake Substrate</text>\n'
        '            <text id="tp-p08-lambda-text" x="50" y="176" font-size="10.5" '
        'font-weight="600" fill="var(--tp-verdigris)">Constructive Peak λ_peak = 588 nm (m = 2) · Flop Shift Δλ = −10.9 nm at 28°</text>\n'
        '            <text x="50" y="196" font-size="9.5" fill="currentColor">Δ_OPD = 2 d √(n_f² − '
        'sin²θ_i) = m λ</text>\n'
        '            <line x1="365" y1="22" x2="365" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="385" y="24" font-size="11" font-weight="600" '
        'fill="currentColor">BRDF Polar Lobes: Automotive vs. Barragán Stucco</text>\n'
        '            <line x1="400" y1="168" x2="645" y2="168" stroke="currentColor" '
        'stroke-width="2"/>\n'
        '            <path d="M 435 168 A 85 85 0 0 1 605 168" fill="none" '
        'stroke="var(--tp-minium)" stroke-width="2.2" stroke-dasharray="4,3"/>\n'
        '            <path id="tp-p08-specular-lobe" d="M 520 168 Q 555 85 618 42 Q 585 125 520 '
        '168" fill="var(--tp-verdigris)" fill-opacity="0.24" stroke="var(--tp-verdigris)" '
        'stroke-width="2.5"/>\n'
        '            <text x="412" y="96" font-size="9.5" fill="var(--tp-minium)">Barragán Matte '
        'Lime (Lambertian)</text>\n'
        '            <text x="535" y="54" font-size="9.5" fill="var(--tp-verdigris)">Cook–Torrance '
        'Metallic Lobe</text>\n'
        '          </svg>',
 'act1_plain_bridge': 'In plain words, think of light not as a steady beam, but as millions of '
                      'tiny ripples moving across a pond. When white sunlight hits an object, '
                      'waves of every color strike its surface together. Most objects have dyes or '
                      'pigments that soak up certain colors and bounce back the rest. But nature '
                      'and human craft have a far cleverer trick: structural color without any '
                      'chemical dye. If you coat a microscopic mineral flake with an ultra-thin '
                      'transparent glass-like film, light waves bounce off both the front face and '
                      'the back face. When those two reflected ripples line up crest-to-crest, '
                      'they boost each other into a dazzling pure color. Because the distance '
                      'through that thin film changes depending on the angle you look from, the '
                      'color shifts as you walk past. That is why a sports car fender ripples from gold toward green under the sun.',
 'act1_stakes': "From Newton's colorful glass rings to modern dielectric mirrors, understanding "
                'thin-film interference transformed our mastery of optics. Early classical optics '
                'treated surfaces as flat geometric planes that simply reflected light according '
                'to ray tracing. But when surface features shrink down to the scale of visible '
                'wavelengths, ray optics fails completely. If a microscopic flake has non-uniform '
                'thickness or excessive roughness, phase coherence across the wave packet '
                'collapses into a dull gray haze. Modern automotive paints and architectural '
                'coatings must navigate the knife-edge boundary between specular wave coherence '
                'and diffuse scattering. If dielectric layer thickness drifts by fifteen nanometers, the model\'s second-order peak moves by about 37 nanometers, from gold toward yellow-green. Classical reflection models '
                'cannot capture these subtle chromatic shifts without tracking phase addition '
                'across multi-layer dielectric stacks. Mastering nanometer film tolerances and '
                'microfacet angle distributions is therefore essential for both photorealistic '
                'computer rendering and advanced optical manufacturing.',
 'act2_plain_primer': 'Let us examine how our two adjustment knobs shape this shimmering wave '
                      'behavior. The first knob is the Incident Viewing Angle. When you look at '
                      'the coated surface straight on, light passes deeply through the film before '
                      'bouncing back, producing a warm baseline tone like rich gold or amber. As '
                      'you tilt your perspective toward a steep glancing angle along a car fender, '
                      'the path through the film shortens geometrically, shifting the amplified color toward shorter, cooler wavelengths, from gold toward green. '
                      'The second knob is the Nano-Oxide Film Thickness. Making the transparent '
                      'oxide layer thicker increases the physical round-trip distance inside the '
                      'film, moving the starting peak from the ultraviolet, through the whole visible band, into the infrared across the slider\'s range. Together, these two controls determine whether a painted surface '
                      'glows with dramatic metallic flop or scatters light evenly into a soft '
                      'matte finish.',
 'distill_diagram': {'analogy_title': 'Sunlight on an Iridescent Soap Bubble',
                     'analogy_sub': 'Bouncing wave crests align into vivid color without any dye',
                     'force_a_title': 'Viewing Angle θ_i',
                     'force_a_sub': 'Shortens optical path and drives blue-shift color flop',
                     'force_b_title': 'Oxide Film Thickness d_film',
                     'force_b_sub': 'Sets baseline constructive resonance wavelength across film',
                     'threshold_title': 'Specular Wave Coherence vs. Diffuse Scattering',
                     'threshold_pass': 'Phase-matched constructive interference with sharp '
                                       'metallic flop',
                     'threshold_fail': 'Random microfacet phase cancellation yielding isotropic '
                                       'matte'},
 'act2_deepening': 'Diving deeper into electromagnetic boundary conditions, the reflection of '
                   'light across stratified dielectric media is governed by the Fresnel '
                   'coefficients and the transfer-matrix method. When an electromagnetic wave '
                   'encounters the interface between the clearcoat resin (refractive index n = '
                   '1.50) and the titanium dioxide platelet (refractive index n = 2.45), the externally reflected wave picks up a 180-degree phase jump. The internally reflected wave travels through the high-index nanolayer twice, accumulating an optical path phase delay. A full treatment adds that jump to the path delay, which turns the integer condition into a half-integer one; the folio\'s interactive model leaves it out for simplicity. Furthermore, the Cook–Torrance microfacet '
                   'distribution function D_GGX governs how many microscopic mirror facets are '
                   "tilted toward the half-vector between incoming sunlight and the observer's "
                   'eye. Geometric shadow-masking factors prevent microfacets from blocking each '
                   'other at oblique grazing angles. On a compound-curved automotive fender, the '
                   'surface normal sweeps continuously through space, turning the nonlinear '
                   'trigonometric term sqrt(n_f^2 - sin^2(theta_i)) into a dynamic, living '
                   'gradient of interference colors.',
 'act4_deepening': 'In contemporary computer vision and materials science, researchers are pairing '
                   'differentiable wave-optics renderers with neural radiance fields to solve '
                   'inverse optical design problems. Instead of guessing pigment formulations '
                   'through laborious trial and error, algorithms invert the Cook–Torrance BRDF '
                   'and Bragg transfer matrix directly from multi-angle camera captures. Neural '
                   'networks predict the exact platelet thickness distribution and orientation '
                   "statistics required to match an artist's custom iridescent color target under "
                   'arbitrary sky illumination. The frontier question in computational optics is '
                   'whether synthetic multi-layer metamaterial films can be designed to produce '
                   'non-monotonic, multi-band color flop—shifting from amber to violet and back to '
                   'emerald at specific angles—without relying on heavy toxic metals or pigment '
                   "degradation. By embedding Maxwell's wave equations directly into graphics "
                   'pipelines, designers and architects can optimize sustainable mineral finishes '
                   'and solar-reflective automotive coatings before mixing a single gram of '
                   'physical material.'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what electromagnetic light waves interfering inside a '
        'gonioapparent pearlescent sports car fender beside a matte Rosa Mexicano and cobalt '
        'architectural stucco wall would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate P.08-V (Imagining What It Would Look Like) · Artistic '
            'wave-optics visualization imagining Bragg thin-film interference across a curved '
            "pearlescent automotive fender ('color flop') juxtaposed against the serene isotropic "
            'Lambertian scatter of a Luis Barragán mineral lime wall.'}

DISPATCH = {'kicker': 'FRONTIER WAVE OPTICS DISPATCH · BRAGG THIN-FILM PEARLESCENCE VS. BARRAGÁN LAMBERTIAN '
           'STUCCO',
 'headline': 'Electromagnetic Interference & Cook–Torrance Microfacet BRDFs Unite Automotive Paint '
             'Flop and Architectural Pigments',
 'body': "Coupling Bragg–Snell thin-film optical path interference with Cook & Torrance's physical "
         'microfacet BRDF (ACM Trans. Graph. DOI 10.1145/357290.357293) explains why TiO2-coated '
         'mica nanoplatelets in curved sports-car finishes shift the model peak by about −42 nm between 0° and 65° (\'color flop\')'
         ", whereas Luis Barragán's porous calcite lime walls hold "
         'hue invariant across every angle.'}

META_3D = ('Bragg Thin-Film Interference & Pearlescent Goniochromism',
 'X: Viewing Angle θ_1 (0°–65°) · Z: Mica TiO₂ d_film · Y: Constructive Wavelength λ_max & Flip')

ES_TRANSLATION = {'title_es': 'Física de Ondas Electromagnéticas del Color: Interferencia de Bragg en Película '
             'Delgada, Perlado Automotriz y Óptica de Estuco de Barragán',
 'subtitle_es': 'Cómo las ondas electromagnéticas transversales (λ ∈ [380, 780] nm) producen '
                'cambio de color angular en pinturas automotrices de mica-TiO₂ frente a la '
                'serenidad invariante de los muros de cal de Luis Barragán.',
 'why_es': 'Una pompa de jabón o la pluma de un colibrí no contienen tintes: sus colores '
           'iridiscentes nacen cuando las ondas de luz rebotan en las caras superior e inferior de '
           'una nanolámina transparente y suman sus crestas.',
 'bridge_es': 'La misma física de interferencia en película delgada es la que usa la interferometría para estimar el espesor de capas transparentes delgadas, como la película lagrimal. Este folio no realiza ni cita mediciones de ese tipo.',
 'plain_es': 'En palabras sencillas, la luz no viaja como un rayo rígido, sino como diminutas olas '
             'que avanzan por un estanque. La luz blanca del sol contiene olas de todos los '
             'colores vibrando al mismo tiempo. La mayoría de los objetos que vemos a diario '
             'tienen tintes o pigmentos químicos que absorben ciertos colores y rebotan el resto '
             'hacia nuestros ojos. Sin embargo, la física del color estructural utiliza un truco '
             'mucho más elegante: no necesita una sola gota de tinte. Al recubrir pequeñas '
             'laminillas minerales transparentes con una capa nanométrica de óxido de titanio, las '
             'ondas de luz rebotan tanto en la cara frontal como en la cara trasera de la '
             'película. Si ambas ondas reflejadas coinciden cresta con cresta, se suman y crean un '
             'color puro y brillante. Como el trayecto a través de esa película cambia según el '
             'ángulo desde donde mires, el tono se transforma mágicamente al caminar junto al '
             'auto, pasando de un dorado cálido hacia el verde.',
 'deep_es': 'La física profunda del color electromagnético se basa en el equilibrio entre dos '
            'fenómenos: la interferencia constructiva de ondas en películas delgadas de Bragg y la '
            'dispersión difusa en microfacetas rugosas. El primer control ajusta el ángulo de '
            'visión respecto a la superficie; al mirar de reojo a lo largo de la salpicadera curva '
            'de un auto deportivo, la trayectoria óptica dentro de la película se acorta y la '
            'longitud de onda se desplaza hacia el azul. El segundo control regula el espesor '
            'nanométrico de la capa de óxido de titanio, determinando el color base de resonancia. '
            'El umbral crítico separa la coherencia especular del acabado perlado frente a la '
            'dispersión difusa e isotrópica del estuco de cal de Luis Barragán. Mientras que el '
            'esmalte automotriz alinea las laminillas para concentrar el brillo en un ángulo '
            'exacto, la rugosidad mineral del muro destruye la fase de las ondas, manteniendo un '
            'color constante y sereno bajo el sol.'}
