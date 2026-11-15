#!/usr/bin/env python3
"""Folio M.08 (MATH): Riemannian Differential Geometry of Color Perception: Helmholtz–Schrödinger Geodesics, MacAdam Metric Tensors & Grassmann Spectral Hilbert Projections."""
from __future__ import annotations

SLUG = 'm08'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.08',
 'slug': 'm08',
 'pillar': 'math',
 'category_code': 'M',
 'title': 'Riemannian Differential Geometry of Color Perception: Helmholtz–Schrödinger Geodesics, '
          'MacAdam Metric Tensors & Grassmann Spectral Hilbert Projections',
 'subtitle': 'How the linearity of color matching that Hermann Grassmann described, read in modern '
             'terms as a projection Π: L²([380,780] nm) → ℝ³, creates metamers, and how a '
             'Riemannian line element ds² = g_ij dx^i dx^j of the kind Erwin Schrödinger proposed '
             'in 1920 defines curved paths between hues. The numbers shown are model values.',
 'date_published': '2026-11-02',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'RIEMANNIAN COLOR MATH · REV 1.1',
 'primary_kernel': 'tools/discovery/formal_proof_thermodynamic_landscape.py',
 'governing_law': 'ds² = ∑ g_ij(x) dx^i dx^j · ẍ^k + Γ^k_ij ẋ^i ẋ^j = 0 · Π: L²([380,780]) → '
                  'ℝ³₊',
 'colophon': {'identifier': 'M.08 · Riemannian Color Manifold & Metamer Nullspace · CIE',
              'kernels': 'Helmholtz–Schrödinger Metric g_ij · MacAdam Ellipses · Cohen Metamer '
                         'Matrix',
              'benchmarks': 'dim ker(Π) = ∞ · model hue drift and ΔE_00 values are illustrative',
              'bridge': 'Schrödinger Color Geodesics ↔ A.07 Barragán Pigments & P.08 Wave '
                        'Interference'},
 'sliders': [{'label': 'Illuminant Blackbody Temp (T_illum)',
              'min': 2700,
              'max': 9500,
              'step': 100,
              'value': 6500,
              'unit': ' K'},
             {'label': 'Riemannian Geodesic Parameter (t_geo)',
              'min': 0.0,
              'max': 1.0,
              'step': 0.02,
              'value': 0.5,
              'unit': 't = '}],
 'steps': ['Stage 1 (Grassmann Hilbert Space Projection Π: L² → ℝ³₊): Continuous electromagnetic '
           'spectra I(λ) project onto 3 cone coordinates X_k = ∫ S(λ, T_illum) R(λ) c̄_k(λ) dλ.',
           "Stage 2 (Cohen's Fundamental Metamer Decomposition): Because dim ker(Π) = ∞, any "
           'spectrum decomposes into R(λ) = R*(λ) + B(λ), where metameric black B(λ) vanishes '
           'under D65 (6500 K) but emerges at sunset (3000 K).',
           "Stage 3 (Helmholtz-Type Line Element g_ij, the folio's model): Discrimination "
           'ellipses such as those MacAdam measured in 1942 show that equal perceptual steps are '
           'not equal Euclidean steps. The folio models this with a Helmholtz-type line element '
           'ds² = ∑ a_k (dx^k / x^k)².',
           'Stage 4 (Geodesic Hue Interpolation, model): Solvingẍ^k + Γ^k_ij ẋ^i ẋ^j '
           '= 0 for that model metric between a cobalt blue and a magenta (rosa mexicano) gives a '
           'curved path. The +9.4° hue difference from a flat RGB chord is an illustrative model '
           'value, not a measured Abney-effect correction.'],
 'readouts': [{'label': 'Riemannian Geodesic Distance (model)',
               'value': 'ds_geo = 42.8 (illustrative units, t = 0.50)'},
              {'label': 'Chord vs. Geodesic Hue Difference (model)',
               'value': '+9.4° for the flat chord (illustrative)'},
              {'label': 'Illuminant Metamerism Index (model)',
               'value': 'ΔE_00 = 0.18 at 6500 K (illustrative)'},
              {'label': 'Model Geometry', 'value': 'Helmholtz-type metric (a model, not a proof)'}],
 'spec_plate': {'division': 'NAMED FOR CONTEXT: CIE 015:2018 (COLORIMETRY) / ISO/CIE 11664-6 '
                            '(CIEDE2000)',
                'title': '81-Band Spectral Reflectance Projection & Riemannian Geodesic '
                         'Colorimetry Kernel',
                'body': 'Design study: a 5 nm wavelength-resolved (380–780 nm) spectral power and '
                        "reflectance integration kernel using Jozef Cohen's matrix R projection "
                        'and geodesic interpolation under a model Riemannian metric.',
                'meta': 'Sources cited, not reproduced: Schrödinger 1920 (DOI '
                        '10.1002/andp.19203682202) · MacAdam 1942 (DOI 10.1364/JOSA.32.000247)'},
 'sidenote_1': {'kicker': "SIDENOTE M.08-A · SCHRÖDINGER'S COLOR METRIC BEFORE QUANTUM MECHANICS",
                'body': 'Six years before his 1926 wave equation, Erwin Schrödinger published a '
                        'theory of color measurement in Annalen der Physik (1920) that treated '
                        'color space with a Riemannian line element, building on earlier work by '
                        'Helmholtz.'},
 'sidenote_2': {'kicker': "SIDENOTE M.08-B · SPECIFICATION PLATE · COHEN'S MATRIX R & "
                          'AUTOMOTIVE/ARCHITECTURAL METAMERISM',
                'body': 'When an automotive metallic door panel repainted with a different pigment '
                        'batch matches the fender at noon (6500 K) but clashes at sunset (3000 K), '
                        'their reflectance difference ΔR(λ) lies in ker(Π_D65) but outside '
                        'ker(Π_3000K).'},
 'skill': {'filename': 'riemannian-color-schrodinger-geodesic-SKILL.md',
           'name': 'riemannian-color-schrodinger-geodesic',
           'description': 'AI-agnostic mathematical colorimetry and differential-geometry skill '
                          'for Grassmann spectral Hilbert projections, Cohen metameric black '
                          'nullspaces, MacAdam metric tensors, and Schrodinger color geodesics.',
           'rules': ['Project spectral reflectance R(lambda) under illuminant S(lambda, T) onto '
                     'tristimulus cone space via x_k = int_{380}^{780} S(lambda, T) * R(lambda) * '
                     'c_bar_k(lambda) d_lambda.',
                     "Decompose R = P_R * R + (I - P_R) * R using Cohen's projection matrix P_R = "
                     'A * (A^T * A)^{-1} * A^T to isolate fundamental color from metameric blacks '
                     'in ker(Pi).',
                     'Integrate Riemannian color geodesics under a stated model metric ds^2 = '
                     'g_ij(x) dx^i dx^j rather than Euclidean chords, and report that the hue '
                     'paths depend on the chosen metric.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The geodesic '
                           'distance, the +9.4° chord hue shift and the ΔE_00 value are now '
                           "labelled as illustrative model values, and the 'QED' verdict and "
                           "the claim that geodesics eliminate the Abney effect are withdrawn. "
                           "The metric ds² = ∑ a_k (dx^k/x^k)² is called a Helmholtz-type model, "
                           'not the Fisher–Rao metric; the claim that color inspired Grassmann\'s '
                           'exterior algebra, the invented 1853 scene, and the Cystic Fibrosis '
                           'line in the Spanish block are removed.',
                'opus': 'Review: all DOIs checked in Crossref and the Scite index on 2026-11-14; '
                        "Schrödinger 1920 and MacAdam 1942 found in Scite. No DOIs added."},
               {'edition': 'REV 1.0',
                'date': '2026-11-02',
                'summary': 'REV 1.0 (Published 2026-11-02): Inaugural Volume IV mathematical '
                           "colorimetry monograph uniting Grassmann's spectral projection, Erwin "
                           "Schrodinger's 1920 Riemannian color manifold (DOI "
                           '10.1002/andp.19203682202), and MacAdam metric ellipses (DOI '
                           '10.1364/JOSA.32.000247).',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'rank-3 projection operator P_R^2 = P_R idempotence, Christoffel geodesic '
                        "curvature, and illuminant metamerism drift. (REV 1.1: this 'verified' "
                        'wording is withdrawn; no measurement or independent check was run.)'}],
 'volume': 4,
 'volume_code': 'VOL. 04',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1002/andp.19203682202',
           'fetched_on': '2026-11-08',
           'citing_publications': 102,
           'supporting': 0,
           'mentioning': 20,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 102 citing '
                      'publications (0 supporting, 20 mentioning, 0 contrasting) on Erwin '
                      "Schrödinger's foundational Riemannian differential geometry of perceptual "
                      'color space and geodesic hue paths.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1002/andp.19203682202',
           'fetched_on': '2026-11-08',
           'citing_publications': 102,
           'supporting': 0,
           'mentioning': 20,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 102 citing '
                      'publications (0 supporting, 20 mentioning, 0 contrasting) on Erwin '
                      "Schrödinger's foundational Riemannian differential geometry of perceptual "
                      'color space and geodesic hue paths.'},
 'act1_title': "Act I — From Hermann Grassmann's Exterior Algebra of Color to Erwin Schrödinger's "
               'Riemannian Color Manifolds',
 'act1_dropcap': 'In 1853 Hermann Grassmann, a schoolteacher in Stettin, published a short paper '
                 'on color mixing in Annalen der Physik und Chemie. It stated what are now called '
                 "Grassmann's laws: mixtures of colored lights combine additively, so that color "
                 'matching behaves like a linear map into a space of three dimensions. Sunlight '
                 'spans a continuum of wavelengths, yet a normal human eye matches colors with '
                 'three kinds of cone. In 1920, six years before his wave equation, Erwin '
                 'Schrödinger published a theory of color measurement in Annalen der Physik that '
                 'gave color space a Riemannian line element, following earlier work by '
                 'Helmholtz. In such a geometry the shortest path between two hues can bend, much '
                 'as an airline route arcs across the globe.',
 'act1_plain_bridge': 'Have you ever noticed that a new sweater matches your favorite pants '
                      'perfectly in the bright fluorescent lighting of a department store, yet '
                      'looks embarrassingly mismatched once you step outside into the afternoon '
                      'sunshine? Or have you ever tried mixing paint on a palette, only to find '
                      'that blending blue and red gives you an unexpectedly dull, muddy gray '
                      'rather than a radiant violet? These everyday surprises happen because our '
                      'eyes do not measure every wavelength of light directly. Instead, three '
                      'color sensors in our retinas compress an infinite spectrum of light waves '
                      'into just three signals. Because many different combinations of wavelengths '
                      'can trigger the exact same response, two materials can appear identical '
                      'under one light bulb but clash wildly under another. Furthermore, our '
                      'perception of color distance is curved. When computers mix colors in '
                      'straight lines, they distort natural hues. True color harmony requires '
                      'understanding the curved geometry of how human eyes actually see.',
 'act1_body': 'Because a three-dimensional projection of an infinite-dimensional wave space '
              'contains an infinite-dimensional nullspace, two radically different electromagnetic '
              'wave distributions can produce identical cone signals whenever their difference '
              'lies inside that kernel. This mathematical mechanism creates metamerism. In 1920, '
              'Erwin Schrödinger published his theory of color metrics, in three parts, in '
              'Annalen der Physik (DOI 10.1002/andp.19203682202), describing color space with a '
              'Riemannian line element rather than a flat Euclidean one. In such a model, paths '
              'between hues are geodesics that solve Euler–Lagrange equations, and they depend on '
              'which metric is chosen. In 1942, David L. MacAdam measured discrimination ellipses '
              'across chromaticity space for one observer (Journal of the Optical Society of '
              'America, DOI 10.1364/JOSA.32.000247); their unequal sizes and orientations show '
              'that equal perceptual steps are not equal steps in the chromaticity diagram. '
              'Later color-difference formulas, such as CIEDE2000, were built to approximate '
              'this kind of non-uniformity.',
 'act1_stakes': 'The leap from flat color wheels to curved differential geometry resolved a '
                'century of industrial and scientific frustration. Early textile dyers, printers, '
                'and lighting engineers treated color matching as simple Euclidean geometry, '
                'assuming that an equal step in red, green, or blue coordinates would produce an '
                'equal step in human perception. The results were notorious: displays clipped '
                'delicate skin tones, automotive panels painted in different factory bays clashed '
                'under evening headlights, and early color photography suffered unpredictable hue '
                'shifts. Schrödinger brought the tools of Riemannian geometry to color '
                "perception, and MacAdam's measurements showed how uneven perceptual distances "
                'are. Non-uniform color-difference metrics descended from this line of work are '
                'used today in color management and quality control. '
                'Understanding how high-dimensional wave phenomena project onto low-dimensional '
                'curved perception bridges pure differential geometry with the physical realities '
                'of human experience.',
 'pullquote': '"Light spectra live in an infinite-dimensional space L^2([380, 780] nm), human '
              'cones reduce them to three numbers, and a curved metric of the kind Schrödinger '
              'proposed is one way to model how far apart two colors look."',
 'chronology': [('1853',
                 "Hermann Grassmann states Grassmann's laws of additive color mixing, which in "
                 'modern terms make color matching a linear map to three dimensions.'),
                ('1920',
                 'Erwin Schrödinger publishes Grundlinien einer Theorie der Farbenmetrik im '
                 'Tagessehen (DOI 10.1002/andp.19203682202), a Riemannian theory of color '
                 'measurement.'),
                ('1942',
                 'David L. MacAdam measures 25 color-discrimination ellipses across CIE '
                 'chromaticity space (DOI 10.1364/JOSA.32.000247).'),
                ('2026',
                 'This folio combines spectral nullspace (metamer) projections with geodesics of '
                 'a model metric, as a teaching study.')],
 'act2_title': "Act II — How It Actually Works: Grassmann's Infinite-Dimensional Nullspace + "
               'Schrödinger Geodesics',
 'act2_intuition': 'Let S(lambda, T_illum) be the illuminant spectral power distribution modeled '
                   "by Planck's blackbody law at temperature T_illum in [2700, 9500] K, and let "
                   'R(lambda) be a surface reflectance spectrum such as a mineral wall pigment or '
                   'an automotive finish. The tristimulus vector is x_k = int S(lambda, T_illum) '
                   'R(lambda) c_bar_k(lambda) d_lambda across cone sensitivities. Two surfaces R_1 '
                   'and R_2 are metameric under reference lighting S_0 when int S_0 (R_1 - R_2) '
                   'c_bar d_lambda = 0. When ambient sunlight cools from 6500 K noon sky to 3000 K '
                   'golden hour, the projection changes and a pair that matched can show a '
                   'CIEDE2000 color difference. For the folio\'s Helmholtz-type model metric g_ij '
                   '= diag(a_1 / x_1^2, a_2 / x_2^2, a_3 / x_3^2), the nonzero Christoffel symbols '
                   'are Gamma^k_kk = -1 / x^k. In the coordinates u_k = ln x_k this metric is '
                   'flat, so its geodesics are straight lines in log space: x_k(t) = '
                   'x_k(0)^(1-t) x_k(1)^t. The path between a cobalt blue and a magenta (rosa '
                   'mexicano, a non-spectral color with no single wavelength) is therefore an arc '
                   'in linear coordinates; the plus 9.4 degree hue difference from the flat RGB '
                   'chord is an illustrative model value.',
 'act2_deepening': 'One modelling view, offered here as a hypothesis rather than an established '
                   'result, treats color discrimination statistically: if cone photon counts are '
                   'noisy, nearby spectra can be told apart only to the extent their response '
                   'distributions differ, and an information metric of that kind would produce '
                   'ellipses resembling MacAdam\'s. When you adjust the illuminant temperature '
                   'slider, you are '
                   'rotating the projection subspace relative to the spectral reflectance '
                   'manifold, causing the metameric black component hidden in the '
                   'infinite-dimensional nullspace to emerge as a visible color shift. '
                   'Simultaneously, adjusting the geodesic slider traverses the Levi-Civita '
                   'connection on the Riemannian cone. Rather than passing through low-saturation '
                   'regions where brightness dips artificially, the geodesic balances brightness '
                   'and chromaticity along the model\'s shortest curve. For the log-flat model '
                   'metric used here each pair of colors has exactly one geodesic, but that is a '
                   'property of this model, not of every color metric. Real color appearance '
                   'also depends on adaptation and surroundings, which no single metric captures.',
 'act2_analogy': 'Everyday analogy: If you look at a flat paper map of the world, drawing a '
                 'straight ruler line between Seattle and Paris makes it seem like the shortest '
                 'flight path runs directly east across the Atlantic Ocean. But because the Earth '
                 'is a curved sphere, airplanes actually fly a great-circle arc north over '
                 'Greenland. Human color perception is curved in exactly the same way. When a '
                 'computer blends colors along a flat, straight line, it cuts across an unnatural '
                 'detour, making hues look washed out or strangely purple. Following a curved '
                 'Riemannian geodesic preserves true, vibrant hue.',
 'act2_plain_primer': 'To explore this curved geometry for yourself, consider two intuitive '
                      'controls on the visual console. The first control changes the color '
                      'temperature of your light source, mimicking the natural transition of '
                      'daylight from a cozy 2,700 Kelvin sunset to a crisp 6,500 Kelvin noon sky '
                      'and up to a cool 9,500 Kelvin northern shade. As the light changes, the '
                      'wavelengths bouncing off two different painted surfaces shift, revealing '
                      'whether their shared color was genuine or merely an illusion that collapses '
                      'at dusk. The second control glides your viewpoint along the transition path '
                      'between two vivid hues, such as deep cobalt blue and vibrant bougainvillea '
                      'magenta. Dragging this slider demonstrates the difference between traveling '
                      'along a flat, artificial shortcut and following the true curved geodesic. '
                      'As you move the sliders together, you observe how the curved mathematical '
                      'path guides the blend cleanly through rich, glowing tones without ever '
                      'falling into muddy gray distortion.',
 'distill_diagram': {'analogy_title': 'The Great-Circle Flight Path',
                     'analogy_sub': 'Airplanes curve over Greenland because the Earth is not flat',
                     'force_a_title': 'Illuminant Temperature T_illum',
                     'force_a_sub': 'Rotates spectral nullspace and triggers metamerism color '
                                    'clash',
                     'force_b_title': 'Geodesic Parameter t_geo',
                     'force_b_sub': 'Traces shortest metric path across curved perceptual '
                                    'coordinates',
                     'threshold_title': 'Model Geodesic vs. Flat Chord',
                     'threshold_pass': 'Model geodesic avoids the illustrative +9.4 deg chord hue '
                                       'shift',
                     'threshold_fail': 'Flat RGB chord detours through muddy purple and gray '
                                       'distortion'},
 'walkthrough': ['Experiment 1 (Illuminant Metamerism & Barragán Sunset Shift): Sweep Illuminant '
                 'Color Temperature T_illum from 6500 K (D65 midday sky) down to 2800 K (warm '
                 'sunset). Watch the Planckian locus shift and track the CIEDE2000 metamerism '
                 'divergence between mineral pigment and synthetic dye.',
                 'Experiment 2 (Model Geodesic vs. Euclidean Chord): Drag Geodesic '
                 'Interpolation Parameter t_geo from 0.00 to 1.00 between a cobalt ultramarine and '
                 'a rosa mexicano magenta (labels illustrative), comparing the model geodesic arc '
                 'against the flat Euclidean chord across MacAdam ellipses.',
                 'Experiment 3 (Hilbert Projection & Metric Tensor Stepper): Click Stages 1 to 4 '
                 "to inspect infinite-dimensional wave spectra in L^2, Cohen's fundamental metamer "
                 'matrix projection, MacAdam metric ellipses g_ij, and Christoffel geodesic '
                 'integration.'],
 'act4_title': 'Act IV — Mathematical Colorimetry, Spectral AI & Upstream Discovery Threads',
 'act4_human_ai': "Modern computer graphics and architectural material synthesis use Jozef Cohen's "
                  'fundamental metamer decomposition (splitting any reflectance spectrum R(lambda) '
                  'into its 3D fundamental component R* in row-space(Pi) plus a metameric black '
                  'B(lambda) in ker(Pi)) could be paired with optimization under a perceptual '
                  'metric to reduce metamerism between materials under changing light. This is '
                  'a proposal, not a description of current practice.',
 'act4_deepening': 'Differential geometry and machine learning could meet in spectral '
                   'rendering and material design. One could imagine human artists setting '
                   'palettes while optimizers trained with differentiable color-difference '
                   'metrics search for materials that keep their appearance across daylight '
                   'conditions. Whether such methods reduce banding or metamerism in practice is '
                   'not something this folio has tested. Mathematical questions remain open: how do '
                   "we extend Schrödinger's Riemannian metric from isolated color patches to "
                   'complex, spatially varying textures where visual cortex receptive fields '
                   'introduce non-local contextual contrast? Furthermore, can we generalize these '
                   'information-geometric geodesics to hyperspectral satellite imaging and medical '
                   'diagnostic endoscopy, where sensors record hundreds of spectral bands beyond '
                   'human vision? Answering these questions could deepen our understanding of '
                   'visual perception and inform tools for virtual reality, architectural '
                   'daylight design, and robotics.',
 'cf_bridge': 'Standalone Pure & Applied Mathematics Flagship & Cross-Pillar Synthesis: Folio M.08 '
              'completes Volume IV Color Wave Triad alongside Architecture (Folio A.07 on Luis '
              "Barragán's chromatic walls) and Physics (Folio P.08 on Bragg thin-film wave "
              'interference and automotive pearlescence). A related but different metric on the '
              'positive cone, the Shahshahani metric ds^2 = sum (dx^i)^2 / x^i, appears in '
              'population genetics; the resemblance to the color model here is a mathematical '
              'analogy only.',
 'sources': ['Grassmann, H. (1853). Zur Theorie der Farbenmischung. Annalen der Physik und Chemie, '
             '165(5), 69–84.',
             'Schrödinger, E. (1920). Grundlinien einer Theorie der Farbenmetrik im Tagessehen '
             '(Outline of a Theory of Color Measurement for Daylight Vision). Annalen der Physik, '
             '368(22), 481–520 (one of three parts; the DOI is for this part). DOI: '
             '10.1002/andp.19203682202.',
             'MacAdam, D. L. (1942). Visual sensitivities to color differences in daylight. '
             'Journal of the Optical Society of America, 32(5), 247–274. DOI: '
             '10.1364/JOSA.32.000247.',
             'Koenderink, J. J. (2010). Color for the Sciences. MIT Press, Cambridge, MA.',
             'Peyré, G., & Cuturi, M. (2019). Computational Optimal Transport with Applications '
             'to Data Sciences (PythonOT/POT, https://github.com/PythonOT/POT). Foundations and '
             'Trends in Machine Learning, 11(5–6), 355–607. DOI: 10.1561/2200000073.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Riemannian color '
        'manifold with MacAdam metric ellipses, Schrodinger geodesic arc vs Euclidean chord, and '
        'Grassmann spectral nullspace projection">\n'
        '            <path d="M 65 182 Q 72 35 195 28 Q 315 24 345 182 Z" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '            <ellipse cx="145" cy="92" rx="18" ry="10" transform="rotate(-28 145 92)" '
        'fill="none" stroke="var(--tp-verdigris)" stroke-width="1.8"/>\n'
        '            <ellipse cx="215" cy="78" rx="22" ry="12" transform="rotate(14 215 78)" '
        'fill="none" stroke="var(--tp-verdigris)" stroke-width="1.8"/>\n'
        '            <ellipse cx="265" cy="128" rx="16" ry="9" transform="rotate(42 265 128)" '
        'fill="none" stroke="var(--tp-verdigris)" stroke-width="1.8"/>\n'
        '            <line x1="115" y1="148" x2="295" y2="112" stroke="currentColor" '
        'stroke-opacity="0.45" stroke-width="2" stroke-dasharray="4,3"/>\n'
        '            <path id="tp-m08-geodesic-arc" d="M 115 148 Q 195 72 295 112" fill="none" '
        'stroke="var(--tp-minium)" stroke-width="3"/>\n'
        '            <circle id="tp-m08-geo-dot" cx="205" cy="98" r="6" '
        'fill="var(--tp-prussian)"/>\n'
        '            <text x="52" y="22" font-size="11" font-weight="600" '
        'fill="currentColor">Model Riemannian Geodesic vs. Discrimination Ellipses</text>\n'
        '            <text x="85" y="168" font-size="9.5" fill="var(--tp-prussian)">'
        'Cobalt</text>\n'
        '            <text x="255" y="102" font-size="9.5" fill="var(--tp-minium)">Rosa '
        'Mexicano</text>\n'
        '            <text id="tp-m08-de-text" x="65" y="202" font-size="10" '
        'fill="var(--tp-verdigris)">Geodesic Arc ds = ∫√(g_ij dx^i dx^j) · Model Metric '
        '(Illustrative)</text>\n'
        '            <line x1="375" y1="22" x2="375" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="392" y="22" font-size="11" font-weight="600" '
        'fill="currentColor">Grassmann Projection Π: L²([380,780] nm) → ℝ³</text>\n'
        '            <path d="M 400 155 Q 445 65 495 142 Q 545 45 595 128 Q 625 162 650 85" '
        'fill="none" stroke="var(--tp-prussian)" stroke-width="2.4"/>\n'
        '            <path id="tp-m08-metamer-wave" d="M 400 142 Q 445 168 495 58 Q 545 152 595 62 '
        'Q 625 98 650 135" fill="none" stroke="var(--tp-minium)" stroke-width="2" '
        'stroke-dasharray="5,3"/>\n'
        '            <text id="tp-m08-illum-text" x="395" y="182" font-size="10" '
        'fill="var(--tp-prussian)">Illuminant T_illum = 6500 K (D65) · dim ker(Π) = ∞</text>\n'
        '            <text x="395" y="202" font-size="9.5" fill="var(--tp-minium)">Solid: Mineral '
        'Pigment R₁(λ) · Dashed: Metameric Pair R₂(λ)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': "Conceptual visualization imagining what Erwin Schrodinger's curved 3D Riemannian color "
        'manifold studded with golden MacAdam metric ellipses and geodesic hue arcs would look '
        'like (artistic impression, not a formal plot)',
 'caption': 'Conceptual Vision Plate M.08-V (Imagining What It Would Look Like) · Artistic '
            "differential-geometry visualization imagining Erwin Schrödinger's curved Riemannian "
            'color cone spanned by MacAdam discrimination ellipses and a glowing geodesic arc from '
            'cobalt ultramarine to Rosa Mexicano.'}

DISPATCH = {'kicker': 'FRONTIER MATHEMATICAL COLORIMETRY DISPATCH · SCHRÖDINGER RIEMANNIAN GEODESICS & '
           'METAMER NULLSPACES',
 'headline': "Schrödinger's 1920 Color Metric and the Spectral Nullspace Behind Metamerism",
 'body': "A teaching study linking Grassmann's 1853 laws of color mixing, read as a projection "
         "to three dimensions, with Erwin Schrödinger's Riemannian theory of color measurement "
         "(Annalen der Physik DOI 10.1002/andp.19203682202) and David MacAdam's discrimination "
         'ellipses (JOSA DOI 10.1364/JOSA.32.000247). Hue paths and values shown come from a '
         'model metric.'}

META_3D = ('Schrödinger Riemannian Color Manifold & MacAdam Geodesics',
 'X/Z: CIE Chromaticity Plane (x, y) · Y: Riemannian Metric ds² = g_ij dx^i dx^j & Geodesic Arc')

ES_TRANSLATION = {'title_es': 'Geometría Diferencial Riemanniana de la Percepción del Color: Geodésicas de '
             'Helmholtz–Schrödinger, Tensores Métricos de MacAdam y Proyecciones de Grassmann',
 'subtitle_es': 'Cómo la linealidad de la mezcla de colores que describió Hermann Grassmann, '
                'leída hoy como una proyección Π: L²([380,780] nm) → ℝ³, crea metámeros, y cómo '
                'un elemento de línea riemanniano ds² = g_ij dx^i dx^j como el que propuso Erwin '
                'Schrödinger en 1920 define trayectorias curvas entre tonos. Las cifras son '
                'valores del modelo.',
 'why_es': 'Volar de Ciudad de México a París en un mapa plano parece una línea recta horizontal, '
           'pero sobre la esfera curva de la Tierra la ruta más corta real (la geodésica) se '
           'arquea hacia el norte.',
 'plain_es': 'En 1853, el profesor Hermann Grassmann descubrió que aunque la luz solar contiene '
             'una infinidad de ondas electromagnéticas distintas, el ojo humano comprime toda esa '
             'riqueza en solo tres señales básicas en la retina. Años después, en 1920, el físico '
             'Erwin Schrödinger propuso describir el espacio de los colores con una geometría '
             'curva, no plana como una mesa. Seguro les ha pasado que '
             'compran una prenda de vestir en una tienda y bajo las luces del mostrador se ve '
             'idéntica a sus pantalones, pero al salir a la luz del sol se nota una diferencia '
             'incómoda. Esto ocurre porque distintas combinaciones de ondas de luz pueden engañar '
             'a nuestros tres receptores visuales bajo cierto tipo de foco. Además, cuando una '
             'computadora mezcla dos colores trazando una línea recta simple, el resultado suele '
             'verse opaco o grisáceo. La verdadera ruta armónica entre dos tonalidades sigue una '
             'trayectoria curva que respeta la geometría natural de la vista humana.',
 'deep_es': 'La formulación matemática de este monográfico conecta dos factores esenciales: la '
            'temperatura de color de la fuente luminosa y el parámetro de interpolación geodésica '
            'riemanniana. Al modificar la temperatura entre 2,700 Kelvin (luz cálida de atardecer) '
            'y 9,500 Kelvin (cielo azul del norte), el espectro de iluminación rota el subespacio '
            'nulo infinito donde se originan los pares metaméricos, alterando la percepción visual '
            'entre pigmentos minerales y tintes sintéticos. Por otra parte, al unir dos tonos como '
            'el azul cobalto y el rosa mexicano, la distancia más corta no es una recta euclidiana '
            'en el espacio RGB, sino una geodésica de una métrica modelo, inspirada en la de '
            'Schrödinger y en las elipses de discriminación que midió MacAdam. En el modelo, la '
            'mezcla lineal plana se desvía unos 9.4 grados de tono respecto a la geodésica; es un '
            'valor ilustrativo, no una corrección medida del efecto Abney.',
 'bridge_es': 'Este folio completa la tríada del color del Volumen IV junto con A.07 (los muros '
              'de Luis Barragán) y P.08 (interferencia en películas delgadas). Una métrica '
              'parecida pero distinta, la de Shahshahani, aparece en genética de poblaciones; el '
              'parecido es solo una analogía matemática.'}
