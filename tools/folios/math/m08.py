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
 'subtitle': 'How Hermann Grassmann’s color-mixing laws compress spectra into three cone signals '
             'and create metamers, and how Riemannian line elements from Helmholtz, Schrödinger, '
             'and Stiles model curved hue paths while overestimating large intervals. Numbers '
             'shown are illustrative.',
 'date_published': '2026-11-02',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'RIEMANNIAN COLOR MATH · REV 1.1',
 'primary_kernel': 'tools/discovery/formal_proof_thermodynamic_landscape.py',
 'governing_law': 'Π_T: L²([380,780]) → ℝ³ · ds² = ∑ g_ij(x) dx^i dx^j (x ∈ ℝ³₊) · ẍ^k + Γ^k_ij '
                  'ẋ^i ẋ^j = 0',
 'colophon': {'identifier': 'M.08 · Riemannian Color Manifold & Metamer Nullspace · CIE',
              'kernels': 'Weber–Fechner Metric · MacAdam Ellipses · Cohen–Kappauf Projector',
              'benchmarks': 'dim ker(Π_T) = ∞ · illustrative Δs_geo = 42.8, +9.4°, ΔE_00 = 0.18',
              'bridge': 'Schrödinger Geodesics ↔ A.07 Pigments & P.08 Thin-Film Optics'},
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
 'steps': ['Stage 1 (Grassmann Projection Π_T: L² → ℝ³): Positive reflectance ρ(λ) ∈ (0, 1] maps '
           'to cone signals x_k = ∫ S(λ, T_illum) ρ(λ) c̄_k(λ) dλ in ℝ³₊ (Grassmann 1853).',
           'Stage 2 (Reflectance Projector): Weighted P_{A_T} = A_T (A_Tᵀ A_T)⁻¹ A_Tᵀ splits '
           'discrete reflectances ρ into a 3D fundamental component and metameric black (adapting '
           'Cohen & Kappauf 1982).',
           'Stage 3 (Weber–Fechner Model Metric): Combining zero self-light offsets (c_k = 0 in '
           'Helmholtz 1891–1892) with Stiles’s (1946) Fechner weights yields model ds² = ∑ a_k '
           '(dx^k / x^k)².',
           'Stage 4 (Log-Geodesics & Scale Caveat): Solving ẍ^k + Γ^k_ij ẋ^i ẋ^j = 0 gives '
           'x^k(t) = x^k(0)^(1−t) x^k(1)^t (+9.4° illustrative); Bujack et al. (2022) show '
           'diminishing returns at large steps.'],
 'readouts': [{'label': 'Geodesic Arc Length (model)',
               'value': 'Δs_geo = 42.8 at t = 0.50 (fixed illustrative)'},
              {'label': 'Chord vs. Geodesic Hue Shift (model)',
               'value': '+9.4° for the flat chord (fixed illustrative)'},
              {'label': 'Near-Metamer Index (model)',
               'value': 'ΔE_00 = 0.18 at 6500 K (fixed illustrative)'},
              {'label': 'Model Geometry',
               'value': 'c_k = 0 Weber–Fechner metric (model, not a proof)'}],
 'spec_plate': {'division': 'MATHEMATICAL COLORIMETRY & DIFFERENTIAL GEOMETRY · TEACHING STUDY',
                'title': 'Spectral Nullspace Projection & Weber–Fechner Geodesic Study',
                'body': 'Teaching study pairing Grassmann projection and Cohen–Kappauf metamer '
                        'decomposition with closed-form geodesics under stated assumptions (c_k = '
                        '0). No spectral grid solver runs here; readouts are fixed illustrative '
                        'text.',
                'meta': 'Cited, not reproduced: Schrödinger 1920 (DOI 10.1002/andp.19203682202) · '
                        'MacAdam 1942 (DOI 10.1364/JOSA.32.000247) · Bujack et al. 2022 (DOI '
                        '10.1073/pnas.2119753119)'},
 'sidenote_1': {'kicker': 'SIDENOTE M.08-A · HELMHOLTZ (1891–1892) & SCHRÖDINGER (1920)',
                'body': 'Helmholtz proposed a 3D Riemannian color line element in 1891–1892 '
                        '(Peruzzi & Roberti 2023, DOI 10.1007/s00407-023-00304-2). Schrödinger '
                        'revived it in 1920, separating affine color matching from Riemannian '
                        'threshold distance (Roberti & Peruzzi 2023, DOI '
                        '10.1007/s00407-023-00317-x).'},
 'sidenote_2': {'kicker': 'SIDENOTE M.08-B · COHEN–KAPPAUF PROJECTOR & METAMERISM',
                'body': 'Cohen & Kappauf (1982, DOI 10.2307/1422186) premultiply a radiant '
                        'stimulus by A(AᵀA)⁻¹Aᵀ to isolate its 3D fundamental metamer from '
                        'metameric blacks. Weighting A into A_T applies orthogonal projection '
                        'P_{A_T} to discrete reflectances, where shifting 6500 K to 3000 K may '
                        'expose differences.'},
 'skill': {'filename': 'riemannian-color-schrodinger-geodesic-SKILL.md',
           'name': 'riemannian-color-schrodinger-geodesic',
           'description': 'AI-agnostic colorimetry and differential-geometry skill for Grassmann '
                          'projections, Cohen-Kappauf metamer projectors, MacAdam ellipses, '
                          'Weber-Fechner geodesics, and non-Riemannian large-difference limits.',
           'rules': ['Map reflectance rho(lambda) in [0, 1] to x_k = int S(lambda, T) rho(lambda) '
                     'c_bar_k(lambda) d_lambda in R^3_{>=0} (strictly positive rho(lambda) in (0, '
                     '1] lands in R^3_+), keeping linear codomain R^3 distinct from R^3_+.',
                     'Use Cohen and Kappauf (1982) projector A(A^T A)^{-1}A^T on radiant stimuli, '
                     'or weighted P_{A_T} = A_T (A_T^T A_T)^{-1} A_T^T on discrete reflectances '
                     'rho, to separate 3D fundamentals from metameric blacks.',
                     'Distinguish Helmholtz (1891-1892) self-light offsets c_k from Stiles (1946) '
                     'unequal Fechner weights in model ds^2 = sum a_k (dx^k / x^k)^2, and note '
                     'Bujack et al. (2022) diminishing returns at large color intervals.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The geodesic '
                           'distance, the +9.4° chord hue shift and the ΔE_00 value are now '
                           "labelled as illustrative model values, and the 'QED' verdict and the "
                           'claim that geodesics eliminate the Abney effect are withdrawn. The '
                           'metric ds² = ∑ a_k (dx^k/x^k)² is called a Helmholtz-type model, not '
                           "the Fisher–Rao metric; the claim that color inspired Grassmann's "
                           'exterior algebra, the invented 1853 scene, and the Cystic Fibrosis '
                           'line in the Spanish block are removed.',
                'opus': 'Review: all DOIs checked in Crossref and the Scite index on 2026-11-14; '
                        'Schrödinger 1920 and MacAdam 1942 found in Scite. No DOIs added.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-02',
                'summary': 'REV 1.0 (Published 2026-11-02): Inaugural Volume IV mathematical '
                           "colorimetry monograph uniting Grassmann's spectral projection, Erwin "
                           "Schrodinger's 1920 Riemannian color manifold (DOI "
                           '10.1002/andp.19203682202), and MacAdam metric ellipses (DOI '
                           '10.1364/JOSA.32.000247).',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'rank-3 projection operator P_R^2 = P_R idempotence, Christoffel geodesic '
                        "curvature, and illuminant metamerism drift. (REV 1.1: this 'verified' "
                        'wording is withdrawn; no measurement or independent check was run.)'}],
 'volume': 4,
 'volume_code': 'VOL. 04',
 'reading_time': '19 MIN READ',
 'word_count': '4,300 WORDS',
 'scite': {'doi': '10.1002/andp.19203682202',
           'fetched_on': '2026-11-21',
           'citing_publications': 103,
           'supporting': 0,
           'mentioning': 20,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index [observed: Scite ML citation classification, accessed '
                      '2026-11-21]: 0 retractions; 103 citing publications (0 supporting, 20 '
                      'mentioning, 0 contrasting) for Schrödinger 1920 (DOI '
                      '10.1002/andp.19203682202). Counts describe that paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '19 MIN READ',
 'word_count': '4,300 WORDS',
 'scite': {'doi': '10.1002/andp.19203682202',
           'fetched_on': '2026-11-21',
           'citing_publications': 103,
           'supporting': 0,
           'mentioning': 20,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index [observed: Scite ML citation classification, accessed '
                      '2026-11-21]: 0 retractions; 103 citing publications (0 supporting, 20 '
                      'mentioning, 0 contrasting) for Schrödinger 1920 (DOI '
                      '10.1002/andp.19203682202). Counts describe that paper, not this folio.'},
 'act1_title': "Act I — From Hermann Grassmann's Laws of Color Mixing to Erwin Schrödinger's "
               'Riemannian Color Metrics',
 'act1_dropcap': 'In 1853 Hermann Grassmann, a teacher in Stettin, published a study on color '
                 'mixing in Annalen der Physik und Chemie responding to optical experiments by '
                 'Hermann von Helmholtz. Grassmann separated every color impression into three '
                 'mathematical moments: brightness, hue, and colorless admixture. Additive light '
                 'matching therefore behaves like a linear map into three coordinates. Sunlight '
                 'spans a continuous rainbow of wavelengths, yet human daylight vision compares '
                 'lights through only three cone classes. Between 1891 and 1892, Helmholtz '
                 'proposed a three-dimensional differential line element to convert small matching '
                 'thresholds into geometric distances. After three decades of neglect, Erwin '
                 'Schrödinger revived that geometric program in three 1920 memoirs in Annalen der '
                 'Physik. He separated lower affine color matching from a higher Riemannian metric '
                 'where shortest paths between hues may curve like routes across a globe.',
 'act1_plain_bridge': 'Have you noticed a sweater match a pair of pants under bright store lamps, '
                      'yet clash outdoors in afternoon sunlight? Or mixed blue and red paint on a '
                      'palette, hoping for violet, and gotten a dull gray instead? Those surprises '
                      'start in the retina. Our eyes do not record each wavelength of light on its '
                      'own. Three cone classes compress an infinite-dimensional light spectrum '
                      'into three signals. Many distinct wavelength mixtures can trigger identical '
                      'cone totals under one lamp while separating under another. Perceptual '
                      'spacing across colors is uneven as well. Equal steps in digital red, green, '
                      'and blue values do not look equally spaced to a human observer, and '
                      'straight digital blends might drift in hue. Curved threshold models suggest '
                      'why local steps bend, with one important caveat at large intervals.',
 'act1_body': 'Projecting an infinite-dimensional wave space onto three signals leaves an '
              'infinite-dimensional nullspace, so distinct spectra match whenever their difference '
              'lies in that kernel (Grassmann 1853, DOI 10.1002/andp.18531650505). In 1920, '
              'Schrödinger distinguished affine matching ("lower color metric") from a Riemannian '
              'line element ("higher color metric") anchored in just-noticeable steps (DOI '
              '10.1002/andp.19203682202; Roberti & Peruzzi 2023, DOI 10.1007/s00407-023-00317-x). '
              'In 1942, David L. MacAdam recorded over 25,000 trials for one observer at 15 '
              'millilamberts, plotting 25 ellipses that no projective map of the 1931 diagram '
              'turns into equal circles (DOI 10.1364/JOSA.32.000247).',
 'act1_stakes': 'W. S. Stiles (1946, DOI 10.1088/0959-5309/58/1/305) modified Helmholtz’s line '
                'element (Peruzzi & Roberti 2023, DOI 10.1007/s00407-023-00304-2) using limiting '
                "Fechner fractions, noting remaining gaps against MacAdam's data. Industrial "
                'colorimetry later adopted CIEDE2000 on CIELAB with lightness, chroma, hue, and '
                'blue-rotation weights (Luo, Cui & Rigg 2001, DOI 10.1002/col.1049). Yet Bujack et '
                'al. (2022, DOI 10.1073/pnas.2119753119) showed that Riemannian metrics '
                'overestimate large color intervals because perceived differences show diminishing '
                'returns below summed small steps.',
 'pullquote': '"Spectra live in L²([380, 780] nm), cones project them to ℝ³, and Riemannian '
              'metrics approximate local ellipses while overestimating large color intervals."',
 'chronology': [('1853',
                 'Grassmann states additive color-mixing laws across three moments (DOI '
                 '10.1002/andp.18531650505).'),
                ('1891–1920',
                 'Helmholtz proposes a 3D line element (DOI 10.1007/s00407-023-00304-2); '
                 'Schrödinger separates affine and Riemannian metrics (DOI '
                 '10.1002/andp.19203682202).'),
                ('1942–1946',
                 'MacAdam measures 25 ellipses (DOI 10.1364/JOSA.32.000247); Stiles weights '
                 'Helmholtz’s element by Fechner fractions (DOI 10.1088/0959-5309/58/1/305).'),
                ('1982–2022',
                 'Cohen & Kappauf introduce projector A(AᵀA)⁻¹Aᵀ (DOI 10.2307/1422186); Luo et al. '
                 'publish CIEDE2000 (DOI 10.1002/col.1049); Bujack et al. show diminishing returns '
                 '(DOI 10.1073/pnas.2119753119).')],
 'act2_title': 'Act II — How It Works: Grassmann Nullspaces, Cohen–Kappauf Projection & '
               'Weber–Fechner Geodesics',
 'act2_intuition': 'For blackbody spectrum S(λ, T_illum) at T_illum ∈ [2700, 9500] K, linear map '
                   'Π_T: L²([380, 780] nm) → ℝ³ sends ρ(λ) ∈ [0, 1] into ℝ³_≥0 and strictly '
                   'positive ρ(λ) ∈ (0, 1] into ℝ³₊ via x_k = ∫ S(λ, T_illum) ρ(λ) c̄_k(λ) dλ; '
                   'nonzero metameric blacks b ∈ ker(Π_T) change sign across λ. With discrete '
                   'matrix (A_T)_{nk} = S(λ_n, T_illum) c̄_k(λ_n) Δλ, adapting Cohen and Kappauf’s '
                   '(1982, DOI 10.2307/1422186) stimulus projector yields P_{A_T} = A_T (A_Tᵀ '
                   'A_T)⁻¹ A_Tᵀ, splitting reflectance ρ into col(A_T) and an orthogonal metameric '
                   'black. Under the stated assumptions (zero self-light offsets c_k = 0 in '
                   'Helmholtz’s 1891–1892 element, DOI 10.1007/s00407-023-00304-2, with Fechner '
                   'weights a_k inspired by Stiles 1946, DOI 10.1088/0959-5309/58/1/305), model '
                   'metric g_ij = diag(a_1/(x^1)², a_2/(x^2)², a_3/(x^3)²) has Γ^k_kk = −1/x^k and '
                   'log-geodesics x^k(t) = x^k(0)^(1−t) x^k(1)^t. For illustrative endpoints x(0) '
                   '= (0.19, 0.20, 0.64) and x(1) = (0.63, 0.09, 0.52) at ω = 0.017 (a_k = 1/ω²), '
                   'half-path length is Δs_geo(0.50) = 42.8 and the chord midpoint (t = 0.50) '
                   'shifts chromaticity angle in (x^1, x^2)/∑x^j by about +9.4° around (1/3, 1/3).',
 'act2_deepening': 'One modeling hypothesis suggests photon-count noise may link local threshold '
                   'ellipses to information metrics, though that remains untested here. Shifting '
                   'T_illum rotates the column space of A_T, so a near-metameric pair at 6500 K '
                   '(illustrative ΔE_00 = 0.18) might diverge at 3000 K. In coordinates u^k = √a_k '
                   'ln x^k, this c_k = 0 metric is flat, giving one geodesic per pair as a model '
                   'property rather than a general law. Crucially, a caveat applies beyond local '
                   'thresholds: Bujack et al. (2022, DOI 10.1073/pnas.2119753119) reported '
                   'diminishing returns across large differences, inconsistent with global '
                   'Riemannian additivity, and adaptation and surround contrast also shift '
                   'appearance.',
 'act2_analogy': 'Everyday analogy: On a flat world map, a ruler line from Seattle to Paris heads '
                 'due east, whereas aircraft fly a curved arc north over Greenland. Straight '
                 'digital color blends can likewise cut across duller coordinates than a curved '
                 'model path. Where the analogy stops: unlike Earth’s curved sphere, this '
                 'zero-offset logarithmic metric has zero intrinsic curvature, and human '
                 'perception also shifts with adaptation, surroundings, and diminishing returns.',
 'act2_plain_primer': 'Two sliders sit below. Illuminant Blackbody Temp sweeps from 2,700 K warm '
                      'light through 6,500 K daylight to 9,500 K shade. Riemannian Geodesic '
                      'Parameter sweeps t from 0.00 to 1.00 along the illustrative '
                      'cobalt-to-magenta arc. Dragging either slider updates its unit label and '
                      'the simulated stage vector overlay, while the four readout cards keep their '
                      'fixed illustrative values (approximately Δs_geo = 42.8, +9.4°, and ΔE_00 = '
                      '0.18).',
 'distill_diagram': {'analogy_title': 'The Great-Circle Flight Path',
                     'analogy_sub': 'Coordinate arcs bend on a flat chart; log-cone model is '
                                    'intrinsically flat',
                     'force_a_title': 'Illuminant Temperature T_illum',
                     'force_a_sub': 'Rotates matching subspace col(A_T) and exposes metameric '
                                    'black components',
                     'force_b_title': 'Geodesic Parameter t_geo',
                     'force_b_sub': 'Indexes model path x^k(t) = x^k(0)^(1−t) x^k(1)^t in cone '
                                    'space',
                     'threshold_title': 'Model Geodesic vs. Flat Chord',
                     'threshold_pass': 'Model log-geodesic avoids the illustrative +9.4 deg chord '
                                       'hue shift',
                     'threshold_fail': 'Flat chord shifts angle; large steps show diminishing '
                                       'returns'},
 'walkthrough': ['Experiment 1 (Illuminant Slider): Sweep T_illum across 2700–9500 K to update the '
                 'Kelvin label and stage overlay; ΔE_00 = 0.18 stays fixed as an illustrative 6500 '
                 'K near-metamer value.',
                 'Experiment 2 (Geodesic Slider): Drag t_geo from 0.00 to 1.00 to update the '
                 'parameter label beside the illustrative arc (Δs_geo = 42.8 and +9.4° stay '
                 'fixed).',
                 'Experiment 3 (Four-Stage Stepper): Step through Stages 1–4 for Grassmann '
                 'projection, Cohen–Kappauf P_{A_T}, Stiles Fechner weights, and Bujack et al. '
                 '(2022) limits.'],
 'act4_title': 'Act IV — Mathematical Colorimetry, Empirical Limits & Open Questions',
 'act4_human_ai': 'In a proposed pigment-design workflow, Cohen and Kappauf’s (1982, DOI '
                  '10.2307/1422186) projector could be paired with perceptual optimization so '
                  'candidate coatings stay consistent with daylight matches. Practical solvers '
                  'must mind formula caveats: Luo, Cui, and Rigg (2001, DOI 10.1002/col.1049) fit '
                  'CIEDE2000 to object-color datasets, and Sharma, Wu, and Dalal (2005, DOI '
                  '10.1002/col.20070) noted small mathematical discontinuities in it. This '
                  'workflow is untested and not verified here.',
 'act4_deepening': 'Because Bujack et al. (2022, DOI 10.1073/pnas.2119753119) showed diminishing '
                   'returns relative to summed threshold steps, no single Riemannian metric spans '
                   'both local thresholds and large intervals. Open questions remain: what '
                   'non-Riemannian scaling laws could reconcile local MacAdam ellipses (DOI '
                   '10.1364/JOSA.32.000247) with global sub-additivity, and how might spectral '
                   'nullspace models include chromatic adaptation?',
 'cf_bridge': 'Standalone Mathematics Monograph: Completes the Volume IV Color Triad with '
              'Architecture A.07 and Physics P.08. The Shahshahani metric ds² = ∑ (dx^i)² / x^i on '
              'the positive orthant is a formal mathematical analogy only; nothing here is a '
              'biological or clinical claim.',
 'sources': ['Grassmann, H. (1853). Zur Theorie der Farbenmischung. Annalen der Physik und Chemie, '
             '165(5), 69–84. DOI: 10.1002/andp.18531650505.',
             'Schrödinger, E. (1920). Grundlinien einer Theorie der Farbenmetrik im Tagessehen. '
             'Annalen der Physik, 368(22), 481–520 (II. Teil). DOI: 10.1002/andp.19203682202.',
             'Peruzzi, G., & Roberti, V. (2023). Helmholtz and the geometry of color space: '
             'gestation and development of Helmholtz’s line element. Arch. Hist. Exact Sci., '
             '77(2), 201–220. DOI: 10.1007/s00407-023-00304-2.',
             'Roberti, V., & Peruzzi, G. (2023). The Helmholtz legacy in color metrics: '
             'Schrödinger’s color theory. Arch. Hist. Exact Sci., 77(6), 615–635. DOI: '
             '10.1007/s00407-023-00317-x.',
             'MacAdam, D. L. (1942). Visual sensitivities to color differences in daylight. J. '
             'Opt. Soc. Am., 32(5), 247–274. DOI: 10.1364/JOSA.32.000247.',
             'Stiles, W. S. (1946). A modified Helmholtz line-element in brightness-colour space. '
             'Proc. Phys. Soc., 58(1), 41–65. DOI: 10.1088/0959-5309/58/1/305.',
             'Cohen, J. B., & Kappauf, W. E. (1982). Metameric color stimuli, fundamental '
             "metamers, and Wyszecki's metameric blacks. Am. J. Psychol., 95(4), 537–564. DOI: "
             '10.2307/1422186.',
             'Luo, M. R., Cui, G., & Rigg, B. (2001). The development of the CIE 2000 '
             'colour-difference formula: CIEDE2000. Color Res. Appl., 26(5), 340–350. DOI: '
             '10.1002/col.1049.',
             'Sharma, G., Wu, W., & Dalal, E. N. (2005). The CIEDE2000 color-difference formula: '
             'Implementation notes, supplementary test data, and mathematical observations. Color '
             'Res. Appl., 30(1), 21–30. DOI: 10.1002/col.20070.',
             'Bujack, R., Teti, E., Miller, J., Caffrey, E., & Turton, T. L. (2022). The '
             'non-Riemannian nature of perceptual color space. PNAS, 119(18), e2119753119. DOI: '
             '10.1073/pnas.2119753119.',
             'Koenderink, J. J. (2010). Color for the Sciences. MIT Press, Cambridge, MA.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning. Quant. Sci. '
             'Stud., 2(3), 882–898. DOI: 10.1162/qss_a_00146.'],
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
        '            <text x="85" y="168" font-size="9.5" fill="var(--tp-prussian)">Cobalt</text>\n'
        '            <text x="255" y="102" font-size="9.5" fill="var(--tp-minium)">Rosa '
        'Mexicano</text>\n'
        '            <text id="tp-m08-de-text" x="65" y="202" font-size="10" '
        'fill="var(--tp-verdigris)">Geodesic Arc Δs_geo = ∫√(g_ij dx^i dx^j) · Model Metric '
        '(Illustrative)</text>\n'
        '            <line x1="375" y1="22" x2="375" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="392" y="22" font-size="11" font-weight="600" '
        'fill="currentColor">Grassmann Projection Π_T: L²([380,780] nm) → ℝ³</text>\n'
        '            <path d="M 400 155 Q 445 65 495 142 Q 545 45 595 128 Q 625 162 650 85" '
        'fill="none" stroke="var(--tp-prussian)" stroke-width="2.4"/>\n'
        '            <path id="tp-m08-metamer-wave" d="M 400 142 Q 445 168 495 58 Q 545 152 595 62 '
        'Q 625 98 650 135" fill="none" stroke="var(--tp-minium)" stroke-width="2" '
        'stroke-dasharray="5,3"/>\n'
        '            <text id="tp-m08-illum-text" x="395" y="182" font-size="10" '
        'fill="var(--tp-prussian)">Reference T_illum = 6500 K (D65) · dim ker(Π_T) = ∞</text>\n'
        '            <text x="395" y="202" font-size="9.5" fill="var(--tp-minium)">Solid: Mineral '
        'Pigment ρ₁(λ) · Dashed: Near-Metamer ρ₂(λ)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': "Conceptual visualization imagining what Erwin Schrodinger's curved 3D Riemannian color "
        'manifold studded with golden MacAdam metric ellipses and geodesic hue arcs would look '
        'like (artistic impression, not a formal plot)',
 'caption': 'Conceptual Vision Plate M.08-V (Imagining What It Would Look Like) · Artistic '
            "visualization imagining Schrödinger's Riemannian color cone, MacAdam ellipses, and a "
            'model geodesic arc from cobalt to Rosa Mexicano.'}

DISPATCH = {'kicker': 'COLORIMETRY DISPATCH · SCHRÖDINGER METRICS, METAMERS & SCALE LIMITS',
 'headline': "Schrödinger's 1920 Color Metric, Cohen–Kappauf Metamers & Non-Riemannian Limits",
 'body': "Links Grassmann's 1853 laws (DOI 10.1002/andp.18531650505) and Cohen & Kappauf's "
         'projector (DOI 10.2307/1422186) with Schrödinger–Stiles line elements (DOI '
         '10.1002/andp.19203682202; DOI 10.1088/0959-5309/58/1/305), MacAdam ellipses (DOI '
         '10.1364/JOSA.32.000247), and Bujack et al. (2022, DOI 10.1073/pnas.2119753119). Values '
         'shown are illustrative.'}

META_3D = ('Schrödinger Riemannian Color Manifold & MacAdam Geodesics',
 'X/Z: CIE Chromaticity Plane (x, y) · Y: Model Metric ds² = g_ij dx^i dx^j & Geodesic Arc')

ES_TRANSLATION = {'title_es': 'Geometría Diferencial Riemanniana de la Percepción del Color: Geodésicas de '
             'Helmholtz–Schrödinger, Tensores Métricos de MacAdam y Proyecciones de Grassmann',
 'subtitle_es': 'Cómo las leyes de mezcla de Hermann Grassmann comprimen espectros en tres señales '
                'de conos y producen metámeros, y cómo los elementos de línea de Helmholtz, '
                'Schrödinger y Stiles modelan trayectorias curvas pero sobreestiman intervalos '
                'grandes. Cifras ilustrativas.',
 'why_es': 'En un mapa plano la ruta aérea a París parece recta, pero en el globo se arquea al '
           'norte; este modelo logarítmico curva la mezcla en coordenadas de conos con curvatura '
           'intrínseca nula.',
 'plain_es': '¿Les ha pasado que un suéter combina con sus pantalones bajo las lámparas de una '
             'tienda, pero desentona al salir al sol? ¿O que al mezclar pintura azul y roja en una '
             'paleta obtienen gris apagado en vez de violeta? Nuestros ojos no registran cada '
             'longitud de onda por separado: tres clases de conos comprimen el espectro en tres '
             'señales. Distintas mezclas dan igual suma bajo un foco y se separan bajo otro. '
             'Además, pasos iguales en rojo, verde y azul en una computadora no lucen iguales y '
             'las mezclas rectas desvían el matiz. Los modelos curvos aclaran los umbrales locales '
             'y sus límites.',
 'deep_es': 'La proyección Π_T envía reflectancias positivas ρ(λ) ∈ (0, 1] a tres señales en ℝ³₊ '
            '(Grassmann 1853, DOI 10.1002/andp.18531650505), y P_{A_T} = A_T(A_TᵀA_T)⁻¹A_Tᵀ '
            '(adaptando Cohen y Kappauf 1982, DOI 10.2307/1422186) descompone reflectancias '
            'discretas entre 2,700 K y 9,500 K. Combinando desplazamientos nulos c_k = 0 en '
            'Helmholtz (1891–1892, DOI 10.1007/s00407-023-00304-2) con pesos de Fechner de Stiles '
            '(1946, DOI 10.1088/0959-5309/58/1/305; Schrödinger 1920, DOI '
            '10.1002/andp.19203682202), ds² = ∑ a_k (dx^k/x^k)² produce x^k(t) = x^k(0)^(1−t) '
            'x^k(1)^t (Δs_geo = 42.8, +9.4° en t = 0.50 y ΔE_00 = 0.18 fijos e ilustrativos; Luo '
            'et al. 2001, DOI 10.1002/col.1049). Bujack et al. (2022, DOI 10.1073/pnas.2119753119) '
            'mostraron rendimientos decrecientes en diferencias grandes.',
 'bridge_es': 'Completa la tríada del color del Volumen IV con A.07 y P.08. El parecido con la '
              'métrica de Shahshahani en el ortante positivo es solo una analogía matemática, sin '
              'afirmaciones biológicas ni clínicas.'}
