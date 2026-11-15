#!/usr/bin/env python3
"""Folio M.11 (MATH): The 3D Kakeya Preprint of Wang and Zahl and the Guth–Maynard Zero-Density Estimate."""
from __future__ import annotations

SLUG = 'm11'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.11',
 'slug': 'm11',
 'pillar': 'math',
 'category_code': 'M',
 'parent_folios': ['M.02', 'P.08'],
 'lineage_mode': 'CONTINUATION · Continues M.02 Riemann Zeta Zero-Density in Lean 4 & P.08 Wave '
                 'Interference',
 'title': 'The 3D Kakeya Preprint of Wang and Zahl and the Guth–Maynard Zero-Density Estimate',
 'subtitle': "Continuing Folios M.02 and P.08: Hong Wang and Joshua Zahl's preprint "
             '(arXiv:2502.17655), which states a proof that every Kakeya set in ℝ³ has Hausdorff dimension 3, '
             'and Larry Guth and James Maynard (Annals of Mathematics, 2026; arXiv:2405.20552) '
             'improving the zero-density exponent to 30/13, past the long-standing bound at σ = '
             '3/4 that goes back to Ingham in 1940. The two results are separate; the links drawn '
             'between them here are analogies.',
 'date_published': '2026-11-07',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': '3D KAKEYA & 30/13 · REV 1.1',
 'primary_kernel': 'tools/formal_verifier.py',
 'governing_law': 'dim_H(K) = dim_M(K) = 3 for Kakeya K ⊂ ℝ³ (as stated in the Wang–Zahl '
                  'preprint) · N(σ, T) ≤ T^(30(1−σ)/13+o(1)) (Guth–Maynard)',
 'colophon': {'identifier': 'M.11 · 3D Kakeya Conjecture (arXiv:2502.17655) & Guth–Maynard 30/13 '
                            '(arXiv:2405.20552)',
              'kernels': 'Wang–Zahl volume estimates for unions of tubes · Guth–Maynard large '
                         'values of Dirichlet polynomials',
              'benchmarks': 'dim_H(K_3D) = 3 (Wang–Zahl preprint) · zero-density exponent 30/13 ≈ 2.3077 < 12/5 = 2.400 '
                            '· primes in short intervals of length x^(17/30+o(1))',
              'bridge': 'Continues M.02/P.08 · Turning a needle in 3D space ↔ wave packets (an '
                        'analogy)'},
 'sliders': [{'label': 'Dirichlet Tube Separation Width (δ_tube)',
              'min': 0.005,
              'max': 0.1,
              'step': 0.005,
              'value': 0.02,
              'unit': 'δ = '},
             {'label': 'Critical Strip Abscissa (σ_zeta)',
              'min': 0.52,
              'max': 0.98,
              'step': 0.01,
              'value': 0.75,
              'unit': 'σ = '}],
 'steps': ["Stage 1 (Besicovitch's 1919 Needle Paradox & The 3D Kakeya Conjecture): A unit needle "
           'can be rotated 360° inside a set of arbitrarily tiny volume (measure zero), yet the '
           'Kakeya Conjecture asserts its fractal Hausdorff dimension in ℝ³ must still be the full '
           '3.000.',
           'Stage 2 (Wang–Zahl 2025, arXiv:2502.17655): In a preprint, Hong Wang and Joshua Zahl '
           'study sets of δ-tubes in ℝ³ in which not too many tubes lie inside a common convex '
           'set, and state a proof that the union of such tubes has almost maximal volume, from '
           'which they deduce that every Kakeya set in ℝ³ has Minkowski and Hausdorff dimension 3.',
           'Stage 3 (Guth–Maynard, arXiv:2405.20552; Annals 2026): New bounds on how often '
           'Dirichlet polynomials take large values give the zero-density estimate N(σ, T) ≤ '
           "T^(30(1−σ)/13+o(1)), improving on the uniform exponent 12/5 = 2.40 of Huxley (DOI "
           '10.1007/BF01418933) and on the bound at σ = 3/4 going back to Ingham (1940).',
           'Stage 4 (Consequence and formal context): Guth and Maynard also deduce asymptotics '
           'for primes in short intervals of length x^(17/30+o(1)). Neither result is listed in '
           'the README of anthropics/formal-math read on 2026-11-14; that README lists Lean 4 '
           'projects on other theorems (see Act IV).'],
 'readouts': [{'label': '3D Kakeya Hausdorff Dimension',
               'value': 'dim_H(K) = 3 (Wang–Zahl preprint)'},
              {'label': 'Zero-Density Exponent (Guth–Maynard)', 'value': '30/13 ≈ 2.3077 (< 12/5 = 2.400)'},
              {'label': 'Short-Interval Prime Asymptotics',
               'value': 'intervals of length x^(17/30+o(1)); 17/30 ≈ 0.5667'},
              {'label': 'Lean 4 Status',
               'value': 'Not listed in the formal-math README (read 2026-11-14)'}],
 'spec_plate': {'division': 'HARMONIC ANALYSIS / ANALYTIC NUMBER THEORY / LEAN 4 FORMALIZATION',
                'title': 'Wang–Zahl 3D Kakeya Tube Multiplicity & Guth–Maynard 30/13 Riemann '
                         'Zero-Density Bound',
                'body': 'Volume estimates for unions of δ-tubes, from which a preprint states a '
                        'proof of the 3D Kakeya conjecture (arXiv:2502.17655), and large-value estimates for Dirichlet polynomials '
                        'giving the 30/13 zero-density exponent (Guth & Maynard, DOI '
                        '10.4007/annals.2026.203.2.6), set against Huxley (DOI '
                        '10.1007/BF01418933) and Conrey (DOI 10.1515/crll.1989.399.1).',
                'meta': 'Sources checked against Crossref and arXiv abstracts on 2026-11-14; the '
                        'proofs themselves were not checked here'},
 'sidenote_1': {'kicker': 'SIDENOTE M.11-A · CROSS-FIELD ANALOGY · TURNING A NEEDLE IN 3D',
                'body': 'How much room do you need to point a needle in every 3D direction? Very '
                        'little volume, but a preprint by Wang and Zahl states a proof that the '
                        'set must still have dimension 3. Harmonic analysts care because wave packets behave like thin tubes, '
                        'and Kakeya-type estimates are linked to restriction problems in Fourier '
                        'analysis. Claims that this result governs MRI scanners have no source '
                        'and are not made here.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.11-B · WHAT THE FORMAL-MATH README LISTS',
                'body': 'The README of https://github.com/anthropics/formal-math, read on '
                        '2026-11-14, describes its zeta23 project as a machine-checked Lean 4 '
                        'formalisation of the Alpöge–Furman result that more than two thirds of '
                        'zeta zeros are simple and on the critical line (arXiv:2608.13637); the '
                        "project's file tree read the same day also holds Challenge/XiPrime.lean, "
                        'on the zeros of ξ′. That README does not list Guth–Maynard or Wang–Zahl. '
                        'https://github.com/openai/math is a separate repository whose contents '
                        'were not reviewed for this folio. This site has not built either.'},
 'skill': {'filename': 'kakeya-3d-guth-maynard-zero-density-SKILL.md',
           'name': 'kakeya-3d-guth-maynard-zero-density',
           'description': 'AI-agnostic harmonic analysis and analytic number theory skill for the '
                          'Wang-Zahl 3D Kakeya preprint (dim_H(K) = 3 as stated there), the '
                          'Guth-Maynard 30/13 Riemann zero-density estimate, and reading Lean 4 '
                          'repository READMEs such as anthropics/formal-math (zeta23).',
           'rules': ['Bound the union volume of direction-separated delta-tubes in R^3 via |union '
                     'T_i| >= C_eps * delta^eps * sum |T_i| to enforce dim_H(K) = dim_M(K) = 3.',
                     'Evaluate the Guth-Maynard zero-density bound N(sigma, T) <= T^(30(1 - '
                     "sigma)/13 + o(1)) as stated in its abstract, compared with Huxley's 12/5 = "
                     '2.40; 30/13 = 2.3077.',
                     'Before citing a Lean repository as a formalisation of a theorem, read its '
                     'README to confirm which theorem it covers, and report what the README said '
                     'with the date you read it (the anthropics/formal-math README read on '
                     '2026-11-14 lists zeta23 as Alpöge–Furman and does not list '
                     'Guth–Maynard).']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. Earlier editions '
                           'said anthropics/formal-math formalised or verified these results; its '
                           'README, read on 2026-11-14, instead describes its zeta23 project as a '
                           'formalisation of the Alpöge–Furman critical-line theorem, so those '
                           'statements are withdrawn. The claims that '
                           'Guth–Maynard bound prime gaps by p^(17/30) and use sixth-order '
                           'decoupling, that the Kakeya theorem governs MRI and cuts scan times, '
                           'and the invented 1917 Petrograd scene are removed. The 30/13 result '
                           'now cites its Annals of Mathematics DOI. A second review the same day '
                           'retitled the folio, attributed the Kakeya result to the Wang–Zahl '
                           'preprint rather than stating it as settled, and phrased every '
                           'statement about a GitHub repository as what its README or file tree '
                           'showed on 2026-11-14.',
                'opus': 'Review: all DOIs checked in Crossref and the Scite index, both arXiv '
                        'abstracts and the zeta23 README read on 2026-11-14. Added Guth & Maynard '
                        '2026 (DOI 10.4007/annals.2026.203.2.6).'},
               {'edition': 'REV 1.0',
                'date': '2026-11-07',
                'summary': 'REV 1.0 (Published 2026-11-07): Volume VI Mathematics flagship '
                           'continuing Folio M.02 (Huxley DOI 10.1007/BF01418933, Conrey DOI '
                           "10.1515/crll.1989.399.1) via Wang–Zahl's 3D Kakeya proof "
                           '(arXiv:2502.17655), Guth–Maynard 30/13 (arXiv:2405.20552), and '
                           'anthropics/formal-math.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B + Gemma 4 31B): '
                        'Verified 3D Kakeya tube overlap exponent, Guth-Maynard 30/13 vs. Huxley '
                        "12/5, and prime gap exponent 17/30. (REV 1.1: this 'verified' wording is "
                        'withdrawn; 17/30 is a short-interval exponent, not a prime-gap bound, '
                        'and no proof was checked here.)'}],
 'volume': 6,
 'volume_code': 'VOL. 06',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.4007/annals.2015.182.1.9',
           'fetched_on': '2026-11-08',
           'citing_publications': 555,
           'supporting': 13,
           'mentioning': 914,
           'contrasting': 2,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (fetched 2026-11-08): 0 retractions; 555 citing '
                      'publications (13 supporting, 914 mentioning, 2 contrasting) for Bourgain & '
                      'Demeter, The proof of the l^2 Decoupling Conjecture (2015), a harmonic '
                      'analysis background paper. It is not the source of the Guth–Maynard or '
                      'Wang–Zahl results.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['M.02', 'P.08'],
 'lineage_mode': 'CONTINUATION · Continues M.02 Riemann Zeta Zero-Density in Lean 4 & P.08 Wave '
                 'Interference',
 'scite': {'doi': '10.4007/annals.2015.182.1.9',
           'fetched_on': '2026-11-08',
           'citing_publications': 555,
           'supporting': 13,
           'mentioning': 914,
           'contrasting': 2,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (fetched 2026-11-08): 0 retractions; 555 citing '
                      'publications (13 supporting, 914 mentioning, 2 contrasting) for Bourgain & '
                      'Demeter, The proof of the l^2 Decoupling Conjecture (2015), a harmonic '
                      'analysis background paper. It is not the source of the Guth–Maynard or '
                      'Wang–Zahl results.'},
 'act1_title': 'Act I — Cool Fact & Human Story: Turning a Needle in Almost No Area, and Two '
               'Separate Breakthroughs',
 'act1_dropcap': "Sōichi Kakeya asked in 1917 how small a region can be in which a needle can be "
                 'turned completely around. Abram Besicovitch showed, in work published around '
                 'that time and in the 1920s, that the area can be made arbitrarily small, and '
                 'that a set containing a unit segment in every direction can have measure zero. '
                 'Pushing this paradox into three dimensions gives the Kakeya '
                 'Conjecture: even if a shape has zero volume while containing a needle pointing '
                 'in every direction, can its intricate fractal dimension also shrink, or must it '
                 'stubbornly fill all three dimensions?',
 'act1_plain_bridge': 'To picture this mystery, imagine trying to parallel park a long, thin car '
                      'in an impossibly narrow alleyway. By making thousands of microscopic '
                      'forward and backward maneuvers, could you turn your car all the way around '
                      'without ever leaving a patch of pavement smaller than a postage stamp? In '
                      'three dimensions, this question asks how tightly you can pack lines '
                      'pointing in every conceivable direction. You might wonder why anyone '
                      'besides a pure mathematician would care. One reason is that in harmonic '
                      'analysis, high-frequency waves concentrated in a direction behave like '
                      'thin tubes, so questions about how tubes overlap are linked to questions '
                      'about how waves add up. That link is mathematical; this folio does not '
                      'claim any direct effect on medical scanners or on the distribution of '
                      'primes.',
 'act1_body': 'Two separate results appeared between May 2024 and February 2025. First, Larry '
              'Guth and James Maynard posted new large-value estimates for Dirichlet polynomials '
              '(arXiv:2405.20552; published in Annals of Mathematics in 2026, DOI '
              '10.4007/annals.2026.203.2.6). As a consequence they obtain the zero-density '
              'estimate N(σ, T) ≤ T^(30(1−σ)/13+o(1)), improving the uniform exponent 12/5 = 2.40 '
              'usually credited to Martin Huxley (Inventiones Mathematicae, DOI '
              '10.1007/BF01418933) and the bound at σ = 3/4 that goes back to Albert Ingham in '
              '1940, and asymptotics for primes in short intervals of length x^(17/30+o(1)). In '
              'February 2025 Hong Wang and Joshua Zahl posted a preprint (arXiv:2502.17655) '
              'stating a proof that every Kakeya set in three dimensions has Minkowski and '
              'Hausdorff dimension three. Neither result is listed in the README of '
              'https://github.com/anthropics/formal-math read on 2026-11-14; that README describes '
              'its zeta23 project as a formalisation of a different theorem, by Alpöge and '
              'Furman, on simple '
              "zeros on the critical line, which strengthens the line of results that includes "
              "Brian Conrey's 1989 two-fifths theorem (DOI 10.1515/crll.1989.399.1).",
 'act1_stakes': 'Both results address a question of concentration. Number theorists bounding '
                'zeros of the Riemann zeta function off the critical line need to know how often '
                'Dirichlet polynomials can be large; harmonic analysts need to know how much thin '
                'tubes pointing in different directions can overlap. The obstacles are different '
                'in detail, and the folio\'s pairing of them is a thematic one. The Wang–Zahl '
                'preprint states that in three dimensions tubes cannot pile up enough to lower '
                'the dimension. Formal proof assistants such as Lean can, in principle, check '
                'long arguments of this kind line by line, but neither result is listed in the '
                'anthropics/formal-math README read on 2026-11-14.',
 'pullquote': '"Packing needles in space (Wang–Zahl) and bounding how often Dirichlet '
              'polynomials are large (Guth–Maynard) are different problems that share a theme: '
              'things pointing in many directions cannot pile up too much."',
 'chronology': [('1917–1940',
                 'Kakeya poses the needle problem; Besicovitch constructs measure-zero needle '
                 'sets; Albert Ingham proves a zero-density estimate that stood at σ = 3/4.'),
                ('1971–1989',
                 'Martin Huxley proves the 12/5 = 2.40 zero-density exponent (DOI '
                 '10.1007/BF01418933); Brian Conrey proves > 2/5 of zeros lie on σ = 1/2 (DOI '
                 '10.1515/crll.1989.399.1).'),
                ('2024',
                 'Larry Guth and James Maynard (arXiv:2405.20552) post the 30/13 ≈ 2.3077 '
                 'zero-density exponent (Annals of Mathematics, 2026).'),
                ('2025',
                 'Hong Wang and Joshua Zahl post a preprint stating a proof of the 3D Kakeya set '
                 'conjecture (arXiv:2502.17655).')],
 'act2_title': 'Act II — Cross-Field Intuition: Overlapping Tubes and Large Values',
 'act2_intuition': 'In harmonic analysis, a wave packet with a well-defined direction is '
                   'concentrated, roughly, in a tube of width delta pointing that way. Kakeya '
                   'questions ask how much such tubes can overlap. In their preprint, Wang and '
                   'Zahl study sets of delta-tubes in R^3 with the property that not too many lie '
                   'inside a common convex set, and state a proof that their union has almost '
                   'maximal volume, roughly |union T_i| >~ delta^epsilon * sum |T_i|, from which '
                   'they deduce that every Kakeya set in R^3 has dimension 3. Guth and Maynard work on a different question: how '
                   'often a Dirichlet polynomial sum_{n <= N} a_n n^(-it) can take values close '
                   'to N^(3/4), which their abstract calls the critical situation for several '
                   'estimates connected to primes and the zeta function. Their new bound gives '
                   'N(sigma, T) <= T^(30(1 - sigma)/13 + o(1)) and asymptotics for primes in '
                   'short intervals of length x^(17/30+o(1)). The comparison between the two is '
                   "this folio's analogy; the second result does not rest on the first.",
 'act2_deepening': 'A useful way to read both results is as limits on concentration. For '
                   'Dirichlet polynomials, the question is how many well-separated points t can '
                   'carry a large value; for tubes, how many can crowd into a small volume. '
                   'Guth and Maynard describe their contribution in terms of large-value '
                   'estimates for Dirichlet polynomials; Wang and Zahl describe theirs in terms of '
                   'volume estimates for unions of convex sets. For the actual mechanisms, read '
                   'the papers: this folio does not reconstruct either proof, and earlier '
                   'editions overstated how the two arguments interlock. A zero-density estimate '
                   'limits how many zeros of the zeta function can lie far from the critical '
                   'line; it does not by itself settle the Riemann Hypothesis.',
 'act2_analogy': 'Everyday analogy: Imagine shining thousands of thin, pencil-like laser pointers '
                 'from every possible direction into a smoky auditorium. Common sense might '
                 'suggest that with clever aiming, you could arrange the beams so they all pass '
                 'through a flat sheet of glass without spilling into the rest of the room. The '
                 'Wang–Zahl preprint states that, in the idealized mathematical version, beams '
                 'pointing in every direction cannot crowd into a set of lower dimension.',
 'act2_plain_primer': 'To compare two separate results, one about needles and one about the '
                      'zeros behind the distribution of prime numbers, our interactive console provides two mathematical knobs. The first knob '
                      'controls the microscopic thickness of the directional tubes, zooming from a '
                      'broad width of one-tenth down to a delicate sliver of five-thousandths. As '
                      'you narrow the tubes, you watch a dense bush of intersecting needles '
                      'proliferate on your screen; the drawing illustrates, but cannot prove, '
                      'that the dimension stays three. The second knob adjusts your '
                      'position across the critical strip where potential exceptions to the '
                      'Riemann Hypothesis might lurk, moving from the central balance line of '
                      'one-half up toward one. As you sweep this slider, you compare the modern '
                      'Guth–Maynard exponent against the older 12/5 exponent and the 1940 bound '
                      'of Ingham, and see how the allowed count of zeros off the critical line '
                      'shrinks. The curves are drawn from the exponents, with the o(1) terms '
                      'ignored.',
 'distill_diagram': {'analogy_title': 'The Smoky Laser Auditorium',
                     'analogy_sub': 'Directional beams cannot collapse into a sheet without volume',
                     'force_a_title': 'Dirichlet Tube Width δ_tube',
                     'force_a_sub': 'Bounds multi-scale needle overlap across directional tubes',
                     'force_b_title': 'Critical Abscissa σ_zeta',
                     'force_b_sub': 'Counts possible zeta zeros off the critical line Re(s)=1/2',
                     'threshold_title': 'Wang-Zahl 3D Bound & 30/13 Exponent',
                     'threshold_pass': 'Kakeya dimension 3 (Wang–Zahl preprint) and 30/13 '
                                       'zero-density '
                                       'exponent (Guth–Maynard)',
                     'threshold_fail': 'Older exponent 12/5; the two results are independent'},
 'walkthrough': ['Experiment 1 (Dirichlet Tube Width δ_tube): Drag Tube Width δ from 0.100 down to '
                 '0.005. Watch the 3D Kakeya bush of intersecting needles fill volumetric space '
                 "(an illustration of the preprint's statement dim_H(K) = 3, not a computation "
                 'of it).',
                 'Experiment 2 (Critical Strip Abscissa σ_zeta): Sweep Abscissa σ from 0.52 to '
                 "0.98. Compare Guth–Maynard's green 30/13 curve against Huxley's 12/5 and "
                 "Ingham's 1940 barrier.",
                 'Experiment 3 (Counterfactual ⚡): Click [⚡ Counterfactual] to replace the '
                 'Guth–Maynard exponent with the older 12/5 exponent and compare the curves.'],
 'act4_title': "Act IV — Imagining Humanity's Future: AI + Lean 4 Formal Blueprints",
 'act4_human_ai': 'Neither Wang–Zahl (arXiv:2502.17655) nor Guth–Maynard (arXiv:2405.20552) is '
                  'listed in the anthropics/formal-math README read on 2026-11-14. Read the same '
                  'day, the README of https://github.com/anthropics/formal-math describes its '
                  'zeta23 project as a sorry-free formalisation of the Alpöge–Furman '
                  'critical-line theorem, the README of https://github.com/teorth/pfr describes '
                  'a Lean 4 formalisation of the polynomial Freiman–Ruzsa conjecture, and the '
                  'README of https://github.com/deepseek-ai/DeepSeek-Prover-V2 describes a '
                  'language model for formal theorem proving in Lean 4. They suggest what such '
                  'work could look like for long harmonic-analysis arguments.',
 'act4_deepening': 'Turning long harmonic-analysis papers into formal proofs would be a large '
                   'project. Researchers could outline dependency blueprints while automated '
                   'tools help fill in lemmas in Lean 4, as the READMEs of anthropics/formal-math '
                   'and teorth/pfr, read on 2026-11-14, describe for other theorems. Any benefit to '
                   'applied fields such as signal processing would come through the ordinary, '
                   'slower route of new algorithms built and tested on their own terms; this '
                   'folio makes no claim about scanners or scan times. Mathematical frontiers remain: '
                   'can the Wang–Zahl techniques be generalized to resolve the Kakeya '
                   'Conjecture in four and higher dimensions, where algebraic varieties exhibit '
                   'far richer singularity structures? And how much further can the zero-density '
                   'exponent fall toward 2, the value predicted by the density hypothesis? Human '
                   'insight, and perhaps machine checking, will both have a part in the answers.',
 'cf_bridge': 'Standalone Harmonic Analysis, Analytic Number Theory & Lean 4 Flagship (M.02 + P.08 '
              '-> M.11): Engineered for mathematicians, formal-verification researchers, and '
              'signal-processing engineers.',
 'sources': ['Bourgain, J., & Demeter, C. (2015). The proof of the l^2 Decoupling Conjecture. '
             'Annals of Mathematics, 182(1), 351–389. DOI: 10.4007/annals.2015.182.1.9.',
             'Wang, H., & Zahl, J. (2025). Volume estimates for unions of convex sets, and the '
             'Kakeya set conjecture in three dimensions. arXiv:2502.17655.',
             'Guth, L., & Maynard, J. (2026). New large value estimates for Dirichlet polynomials. '
             'Annals of Mathematics, 203(2), 623–675. DOI: 10.4007/annals.2026.203.2.6. '
             '(Preprint arXiv:2405.20552, 2024.)',
             'Huxley, M. N. (1971). On the difference between consecutive primes. Inventiones '
             'Mathematicae, 15(2), 164–170. DOI: 10.1007/BF01418933.',
             'Conrey, J. B. (1989). More than two fifths of the zeros of the Riemann zeta function '
             'are on the critical line. Journal für die reine und angewandte Mathematik, 399, '
             '1–26. DOI: 10.1515/crll.1989.399.1.',
             'anthropics/formal-math, zeta23 project README (read 2026-11-14): a Lean 4 '
             'formalisation of Alpöge & Furman, "More than two thirds of the zeta zeros are simple '
             'and on the critical line" (arXiv:2608.13637), with Challenge/XiPrime.lean on the '
             'zeros of ξ′. https://github.com/anthropics/formal-math. Repository statements; '
             'not built by this site.',
             'The mathlib Community (2020). The Lean mathematical library '
             '(leanprover-community/mathlib4). CPP 2020, 367–381. DOI: '
             '10.1145/3372885.3373824.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Wang-Zahl 3D '
        'Kakeya Needle Tube Bush and Guth-Maynard 30/13 Riemann Zero-Density Bound vs Huxley '
        '12/5">\n'
        '            <line x1="35" y1="188" x2="645" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <text x="44" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">3D Kakeya δ-Tube Bush: dim_H(K) = 3 (Wang–Zahl Preprint)</text>\n'
        '            <g transform="translate(185, 112)">\n'
        '              <line x1="-95" y1="-48" x2="95" y2="48" stroke="var(--tp-prussian)" '
        'stroke-width="3.2" stroke-opacity="0.8"/>\n'
        '              <line x1="-95" y1="48" x2="95" y2="-48" stroke="var(--tp-verdigris)" '
        'stroke-width="3.2" stroke-opacity="0.8"/>\n'
        '              <line x1="-35" y1="-60" x2="35" y2="60" stroke="var(--tp-minium)" '
        'stroke-width="3" stroke-opacity="0.8"/>\n'
        '              <line x1="-105" y1="0" x2="105" y2="0" stroke="var(--tp-prussian)" '
        'stroke-width="2.6" stroke-opacity="0.7"/>\n'
        '              <line x1="0" y1="-62" x2="0" y2="62" stroke="var(--tp-verdigris)" '
        'stroke-width="2.6" stroke-opacity="0.7"/>\n'
        '              <circle cx="0" cy="0" r="14" fill="none" stroke="var(--tp-minium)" '
        'stroke-width="1.8" stroke-dasharray="3,2"/>\n'
        '            </g>\n'
        '            <text x="44" y="176" font-size="9.5" fill="var(--tp-verdigris)">Volume '
        'Estimates for Unions of Tubes (arXiv:2502.17655)</text>\n'
        '            <line x1="348" y1="24" x2="348" y2="192" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="366" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">Guth–Maynard 30/13 vs. Huxley 12/5 Zero-Density</text>\n'
        '            <path d="M 372 162 Q 495 72 628 44" fill="none" stroke="var(--tp-minium)" '
        'stroke-width="2.2" stroke-dasharray="5,3"/>\n'
        '            <path d="M 372 162 Q 495 104 628 72" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="3.2"/>\n'
        '            <circle cx="500" cy="102" r="5.5" fill="var(--tp-verdigris)"/>\n'
        '            <text x="374" y="56" font-size="9" fill="var(--tp-minium)">Huxley '
        '12/5 = 2.400</text>\n'
        '            <text x="374" y="132" font-size="9.5" fill="var(--tp-verdigris)">Guth–Maynard '
        '30/13 ≈ 2.3077 (arXiv:2405.20552)</text>\n'
        '            <text x="366" y="176" font-size="9.5" fill="var(--tp-prussian)">Primes in '
        'Short Intervals: Length x^(17/30+o(1))</text>\n'
        '            <text x="44" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Illustration · Results From the Cited Papers, Not Checked '
        'Here</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a three-dimensional Kakeya crystal of '
        'intersecting directional light tubes coupled to the critical-line landscape of the '
        'Riemann zeta function would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate M.11-V (Imagining What It Would Look Like) · Artistic '
            'mathematical visualization (continuing Folios M.02 & P.08) imagining the Wang–Zahl 3D '
            "Kakeya directional tube bush and Guth–Maynard's 30/13 Riemann zero-density "
            'exponent.'}

DISPATCH = {'kicker': 'FRONTIER HARMONIC ANALYSIS & LEAN 4 DISPATCH · 3D KAKEYA (ARXIV:2502.17655) & '
           'GUTH–MAYNARD 30/13',
 'headline': 'Wang–Zahl on the 3D Kakeya Conjecture & Guth–Maynard on Zero Density',
 'body': 'A preprint by Hong Wang and Joshua Zahl (arXiv:2502.17655) states a proof that every '
         'Kakeya set in R^3 has dimension 3, and Larry Guth and James Maynard (Annals of Mathematics, DOI '
         '10.4007/annals.2026.203.2.6) lower the zero-density exponent to 30/13 from the 12/5 of '
         'Huxley (DOI 10.1007/BF01418933). Two separate results, read side by side.'}

META_3D = ('Wang–Zahl 3D Kakeya Tube Overlap & Guth–Maynard 30/13 Surface',
 'X: Tube Scale −log10(δ) · Z: Critical Strip σ · Y: Zero-Density Exponent & Tube Multiplicity')

ES_TRANSLATION = {'title_es': 'El preprint de Wang y Zahl sobre Kakeya en 3D y la estimación de densidad '
             'de ceros de Guth y Maynard',
 'subtitle_es': 'Continuando los Folios M.02 y P.08: el preprint de Hong Wang y Joshua Zahl '
                '(arXiv:2502.17655), que afirma demostrar que todo conjunto de Kakeya en ℝ³ tiene '
                'dimensión de Hausdorff 3, y el trabajo de Larry Guth y James Maynard (Annals of '
                'Mathematics, 2026; arXiv:2405.20552) que mejora el exponente de densidad de '
                'ceros a 30/13, superando la cota en σ = 3/4 que venía de Ingham en 1940. Son '
                'resultados independientes; los vínculos entre ellos aquí son analogías.',
 'why_es': 'Apuntar una aguja en todas las direcciones del espacio puede hacerse en un volumen '
           'casi nulo, pero un preprint de Wang y Zahl afirma demostrar que el conjunto debe '
           'tener dimensión 3. Este '
           'folio no afirma ningún efecto sobre resonancias magnéticas.',
 'plain_es': 'En 1917, Sōichi Kakeya preguntó qué tan pequeña puede ser una región donde se '
             'pueda girar una aguja por completo, y Abram Besicovitch mostró algo asombroso: es '
             'posible diseñar maniobras tan ingeniosas que el área total tocada sea tan pequeña '
             'como se quiera. Desde entonces, los matemáticos se '
             'preguntaron si en tres dimensiones este conjunto de agujas apuntando en todas '
             'direcciones podía encogerse en una superficie plana, o si obligatoriamente debía '
             'ocupar las tres dimensiones completas. En febrero de 2025, Hong Wang y Joshua Zahl '
             'publicaron un preprint que afirma demostrar que la dimensión debe ser exactamente '
             'tres. En '
             'análisis armónico, las ondas con una dirección definida se comportan como tubos '
             'delgados, así que la pregunta sobre cómo se enciman los tubos está ligada a cómo se '
             'suman las ondas. Ese vínculo es matemático; este folio no afirma ningún efecto '
             'directo sobre escáneres médicos ni sobre los números primos.',
 'deep_es': 'Este folio pone lado a lado dos resultados independientes: el preprint de Wang y '
            'Zahl que afirma demostrar la conjetura de Kakeya en 3D y el nuevo exponente de densidad de ceros '
            '30/13 de Guth y Maynard. El sistema interactivo vincula el grosor de los tubos '
            'direccionales con la abscisa de la franja crítica de la función zeta de Riemann. '
            'Wang y Zahl afirman que la unión de tubos que no se concentran demasiado en un '
            'mismo conjunto convexo tiene un volumen casi máximo. Guth y Maynard acotan con qué '
            'frecuencia los polinomios de Dirichlet toman valores grandes, lo que mejora el '
            'exponente 12/5 de Huxley y la cota en σ = 3/4 que venía de Ingham en 1940, y da '
            'asintóticas para primos en intervalos cortos de longitud x elevado a 17/30 más o(1). '
            'Ninguno de los dos resultados aparece en el README de anthropics/formal-math '
            'consultado el 14 de noviembre de 2026; ese README describe su proyecto zeta23 como '
            'la formalización de otro teorema, de Alpöge y Furman.',
 'bridge_es': 'Los grandes valores de polinomios de Dirichlet de Guth–Maynard reducen el '
              'exponente de densidad de ceros de 12/5 a 30/13. Ninguno de los dos resultados '
              'aparece en el README de anthropics/formal-math consultado el 14 de noviembre de '
              '2026.'}
