#!/usr/bin/env python3
"""Folio M.02 (MATH): Riemann Zeta Zero-Density Estimates and Large Sieve Inequalities."""
from __future__ import annotations

SLUG = 'm02'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.02',
 'slug': 'm02',
 'pillar': 'math',
 'category_code': 'M',
 'title': 'Riemann Zeta Zero-Density Estimates and Large Sieve Inequalities',
 'subtitle': 'Classical zero-density estimates for the Riemann zeta function, and what a public '
             'Lean 4 repository README states about a recent critical-line result. The comparison '
             "with Markov-chain relaxation is this folio's own analogy.",
 'date_published': '2026-10-24',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.4',
 'status_badge': 'REDATED REV 1.4',
 'primary_kernel': 'tools/discovery/formal_proof_thermodynamic_landscape.py',
 'colophon': {'identifier': 'M.02 · Analytic Number Theory',
              'kernels': 'Zero-density estimates · Large Sieve · Zeta23 (README statement)',
              'benchmarks': 'Ingham-Huxley Zero-Density N(σ, T) ≪ T^(c(1-σ)+ε), total exponent 3/5 at σ = 3/4',
              'bridge': 'Spectral gap ↔ Markov-chain relaxation (analogy only)'},
 'sliders': [{'label': 'Real Part Threshold σ in Critical Strip (1/2 ≤ σ ≤ 1)',
              'min': 0.52,
              'max': 0.98,
              'step': 0.01,
              'value': 0.75,
              'unit': 'σ = '},
             {'label': 'Dirichlet Polynomial Length Parameter (log T)',
              'min': 4.0,
              'max': 20.0,
              'step': 0.5,
              'value': 10.0,
              'unit': 'log T = '}],
 'steps': ['Stage 1 (Dirichlet Polynomial Mollification): A mollifier M(s) is a short Dirichlet '
           'polynomial chosen so that ζ(s)M(s) stays close to 1 away from zeros; it is a standard '
           'tool for studying zeros near the critical line Re(s) = 1/2.',
           'Stage 2 (Montgomery-Halász Large Sieve): Bounds mean-value L² norms of Dirichlet '
           'polynomials over well-spaced frequencies t_r ∈ [0, T].',
           'Stage 3 (Zero-Detectors & Huxley-Ingham Exponent): Combines zero-detecting polynomials '
           'with fourth-power moment bounds on Re(s) = 1/2.',
           'Stage 4 (The Resulting Bound): Zero-density estimates of the form N(σ, T) ≪ '
           'T^(c(1-σ)+ε) limit how many zeros can lie off the critical line. Ingham gives '
           'c = 3/(2-σ) and Huxley gives c = 12/5; at σ = 3/4 both give c = 12/5 and the total '
           "exponent c(1-σ) = 3/5. Comparing this with a spectral gap is the folio's own "
           'analogy.'],
 'readouts': [{'label': 'Total Zero-Density Exponent c(σ)(1-σ)', 'value': '0.600 (at σ = 0.75, Ingham and Huxley agree)'},
              {'label': 'Spectral Gap Ratio (λ_2 / λ_max)', 'value': '0.418 (fixed illustrative value)'},
              {'label': 'Zeta23 Statement in formal-math', 'value': 'stated by its README (not built or checked here)'},
              {'label': 'Cheeger Inequality Bound', 'value': 'h_G² / 2 ≤ λ_2 ≤ 2 h_G (classical)'}],
 'sidenote_1': {'kicker': 'SIDENOTE M.02-A · WHAT THE REPOSITORY STATES',
                'body': 'The README of anthropics/formal-math lists a Zeta23 project whose statement '
                        'is that more than two thirds of the zeros of the Riemann zeta function are '
                        'simple and on the critical line (Alpöge–Furman, arXiv:2608.13637). This '
                        'site has not built it and does not check the mathematics. The same project contains zeta23/Challenge/XiPrime.lean, whose header describes it as a challenge about the zeros of ξ′ (the derivative of the completed zeta function); this folio does not use it, and its proof status was not checked here.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.02-B · A LOOSE ANALOGY WITH MARKOV CHAINS',
                'body': 'For a reversible continuous-time Markov chain, the relaxation time is the '
                        'reciprocal of the spectral gap, τ = 1/λ_2. The folio places this picture '
                        'beside zero-density bounds only as an analogy: no mathematics passes '
                        'between the zeros of zeta and the gating of an ion channel.'},
 'skill': {'filename': 'zeta-spectral-zero-density-SKILL.md',
           'name': 'zeta-spectral-zero-density',
           'description': 'AI-agnostic analytic number theory and spectral gap skill for Riemann '
                          'zeta zero-density bounds N(sigma, T), large sieve inequalities, and '
                          'Cheeger-Fiedler mixing times.',
           'rules': ['Quote zero-density exponents N(sigma, T) <= T^(c(1-sigma) + eps) with their sources: '
                     'Ingham c = 3/(2-sigma) and Huxley c = 12/5 (both give total exponent 3/5 at '
                     'sigma = 3/4), and Guth-Maynard c = 30/13.',
                     'State the Cheeger-Fiedler inequalities h_G^2 / 2 <= lambda_2 <= 2 h_G as '
                     'classical results, and say when a Markov-chain picture is only an analogy.',
                     'When citing a Lean 4 repository, report what its README states and whether '
                     'you built it; do not assert that it is free of sorry unless you checked.']},
 'revisions': [{'edition': 'REV 1.4',
                'date': '2026-11-14',
                'summary': 'REV 1.4 (Redated 2026-11-14): Grounding revision. Earlier editions '
                           "said in the site's own voice that a Lean 4 file Challenge/XiPrime.lean "
                           "had 'zero sorryAx', and attributed zero-density estimates to the Zeta23 "
                           'project. That file (zeta23/Challenge/XiPrime.lean) concerns the zeros of ξ′, not zero-density estimates, and its sorry status was not checked here; the README describes Zeta23 as a statement about zeros that are simple '
                           'and on the critical line (Alpöge–Furman, arXiv:2608.13637), which this '
                           'site reports without checking. The Ingham reference now has its correct '
                           'DOI and pages, the unrelated DOIs attached to the Montgomery-Odlyzko '
                           'sentence and to the Cheeger-Fiedler comparison are removed, and the '
                           'Cystic Fibrosis section is shortened to a labelled analogy. The opening '
                           'scene and the encryption claims are replaced by a plain account of '
                           'Riemann (1859).',
                'opus': 'Review: DOIs checked in Crossref and the Scite index on 2026-11-14 '
                        '(Huxley, Conrey, Guth-Maynard, mathlib); the Guth-Maynard 30/13 exponent, '
                        "the Huxley exponent and Ingham's exponent were checked with Scite "
                        'check_claim. Guth-Maynard (DOI 10.4007/annals.2026.203.2.6) and the '
                        'correct Ingham DOI were added to the source list.'},
               {'edition': 'REV 1.3',
                'date': '2026-11-06',
                'summary': 'REV 1.3 (Redated 2026-11-06): Added the Guth-Maynard (30/13)(1-sigma) '
                           'zero-density bound (total exponent 15/26 = 0.5769 at sigma = 3/4, below '
                           "0.600) and a reference to OpenAI's openai/math repository. (REV 1.4: "
                           "the '1.0400x Markovian spectral relaxation speedup' and the '722 -> 719 "
                           "sign-parity' account have no source and are withdrawn.)",
                'opus': 'Cross-model check (Gemini 4 Argon + Gemma 4 31B + Ornith 1.5 '
                        '35B): Verified Guth-Maynard 30/13 exponent at sigma = 3/4. (REV 1.4: the '
                        "'quarantine of 3 sign-flip lemmas' wording is withdrawn; it has no "
                        'source.)'},
               {'edition': 'REV 1.2',
                'date': '2026-11-02',
                'summary': 'REV 1.2 (Redated 2026-11-02): Re-verified Ingham-Huxley zero-density '
                           'crossover (sigma = 3/4, c = 0.600), Conrey critical-line mollifier (> '
                           '2/5 zeros on Re(s) = 1/2, DOI 10.1515/crll.1989.399.1), and '
                           'Challenge/XiPrime.lean spectral bounds with 4-Seat Frontier Council '
                           'review.',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Ingham-Huxley crossover at sigma = 3/4 (c = 0.600) and zero sorryAx '
                        'contamination in Challenge/XiPrime.lean. (REV 1.4: the \'zero sorryAx\' wording is withdrawn; the file exists as zeta23/Challenge/XiPrime.lean, but this site ran no such check.)'},
               {'edition': 'REV 1.1',
                'date': '2026-11-01',
                'summary': 'REV 1.1 (Redated 2026-11-01): Added Challenge/XiPrime.lean spectral '
                           'barrier trace and Cheeger-Fiedler Markovian mixing bridge. (REV 1.4: withdrawn as a zero-density trace; XiPrime.lean concerns the zeros of ξ′.)',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Ingham-Huxley crossover at σ = 3/4 where both exponents equal 6/5 · (1 - '
                        'σ). (REV 1.4: the exponents at that point are 12/5 · (1 - σ) and '
                        '3/(2-σ) · (1 - σ), both 3/5 at σ = 3/4; the 6/5 wording was wrong.)'},
               {'edition': 'REV 1.0',
                'date': '2026-10-24',
                'summary': 'REV 1.0 (Published 2026-10-24): Initial formal-math Zeta23 '
                           'zero-density monograph.',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Montgomery-Halász large sieve orthogonality constants. (REV 1.4: this '
                        "'verified' wording is withdrawn.)"}],
 'governing_law': 'Zero-density estimates · Large Sieve · Zeta23 (README statement)',
 'governing_law_latex': r"N(\sigma, T) \ll T^{c(1-\sigma)+\varepsilon}, \\ c_{\mathrm{Huxley}} = \frac{12}{5}, \quad c_{\mathrm{GM}} = \frac{30}{13}",
 'volume': 1,
 'volume_code': 'VOL. 01',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1515/crll.1989.399.1',
           'fetched_on': '2026-11-08',
           'citing_publications': 230,
           'supporting': 1,
           'mentioning': 12,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Conrey 1989 (DOI 10.1515/crll.1989.399.1), checked '
                      '2026-11-08: 230 citing publications (1 supporting, 12 mentioning, 0 '
                      'contrasting) and no retraction notice. These counts describe that one '
                      'paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'act1_dropcap': 'In 1859, on his election as a corresponding member of the Berlin Academy of Sciences, Bernhard Riemann submitted an eight-page paper, "Über die Anzahl der Primzahlen unter einer gegebenen Grösse" (On the number of primes less than a given magnitude). It studies the zeta function as a function of a complex variable and ties the distribution of the primes to the places where that function is zero. In it Riemann remarked that it is very likely that all the non-trivial zeros lie on the vertical line Re(s) = 1/2. That statement is now called the Riemann Hypothesis, and it has not been proved.',
 'act1_plain_bridge': 'In plain words, Riemann asked how the primes are spread along the number line. Primes such as two, three, five and seven are the building blocks of whole numbers, since every whole number is a product of them. They look scattered at random, yet counting them is closely tied to where the zeta function vanishes. The Riemann Hypothesis says that all the non-trivial zeros sit on one line; it remains an open conjecture. Prime numbers are also used in public-key cryptography, but this folio makes no claim that any result discussed here makes a code safe or unsafe.',
 'act1_body': 'While the Riemann Hypothesis remains unproved, number theorists including Albert Ingham, Hugh Montgomery and Martin Huxley established zero-density estimates: bounds on how many zeros can lie off the critical line, of the form N(sigma, T) <= T^(c(1-sigma) + eps) (Ingham 1940, DOI 10.1093/qmath/os-11.1.201; Huxley 1972, DOI 10.1007/BF01418933). Conrey showed that more than two-fifths of the zeros lie on the critical line (DOI 10.1515/crll.1989.399.1). More recently Guth and Maynard established new large value estimates for Dirichlet polynomials, which give the smaller exponent 30/13 in place of 12/5 (arXiv:2405.20552, DOI 10.4007/annals.2026.203.2.6; the folio does not state the range of sigma where it applies). The README of the repository anthropics/formal-math lists a Lean 4 project, zeta23, whose stated result is that more than two thirds of the zeros are simple and on the critical line (Alpöge and Furman, arXiv:2608.13637). This site has not built that project and does not check the mathematics.',
 'act1_stakes': 'Analytic number theory proofs can run to dozens of dense pages, and a slip in an exponent or a remainder term can be hard to spot. A proof assistant such as Lean 4 checks each step against a small trusted kernel, which is why formalization is attractive for this kind of argument. Whether a particular repository delivers that depends on what is actually built and checked, and this site reports what repository READMEs state without having built them. A formalization also only shows that a statement follows from its assumptions; the statement itself still has to be read and judged by people.',
 'pullquote': 'Even without proving that off-line zeros cannot exist, bounding how many there can '
              'be is enough for many results about the primes.',
 'pullquote_cite': 'Editorial Synthesis · Zero-Density Estimates from Ingham (1940) to '
                   'Guth–Maynard (2024)',
 'chronology': [('1859',
                 'Bernhard Riemann',
                 'Connects prime distribution pi(x) to the complex zeros of the analytic '
                 'continuation of zeta(s).'),
                ('1940',
                 'Albert E. Ingham',
                 'Establishes the zero-density bound N(sigma, T) <= T^(3(1-sigma)/(2-sigma) + eps) '
                 '(DOI 10.1093/qmath/os-11.1.201).'),
                ('1971–1972',
                 'Martin Huxley',
                 'Establishes N(sigma, T) <= T^(12(1-sigma)/5 + eps), the bound that is smaller than '
                 "Ingham's for sigma > 3/4 (DOI 10.1007/BF01418933)."),
                ('2024',
                 'Guth & Maynard',
                 'Derive new large value estimates for Dirichlet polynomials and, as a '
                 'consequence, N(sigma, T) <= T^(30(1-sigma)/13 + o(1)) (arXiv:2405.20552).'),
                ('2026',
                 'anthropics/formal-math README',
                 'Lists a Lean 4 project, zeta23, for the Alpöge–Furman critical-line result '
                 '(arXiv:2608.13637); not built or checked by this site.')],
 'act2_analogy': 'Everyday analogy: Imagine tuning a sensitive radio receiver in a crowded auditorium where hundreds of people are humming different musical pitches. If the singers hum randomly, their voices cancel out into a soft, harmless murmur. For a deafening feedback squeal to occur, hundreds of independent singers must suddenly synchronize their breath and hit the exact same note simultaneously. The Large Sieve shows that acoustic energy is strictly finite, meaning massive feedback spikes can happen only in rare, isolated bursts.',
 'act2_plain_primer': 'To see how this acoustic balance works in practice, you can explore two intuitive control knobs. The first knob acts like an acoustic threshold dial, moving from the safe centerline out toward the dangerous edge of the concert hall. Near the center, almost all frequencies cancel out naturally, so no runaway signals can take hold. But as you dial this threshold knob toward the outer boundary, you are checking whether any rogue waves manage to survive. The second knob sets the listening window, stretching the duration over which you monitor the crowd. At short time scales, random fluctuations might occasionally seem loud. However, as you expand the observation window, the total energy of the room enforces strict limits: singers who waste energy shouting at one pitch cannot sustain noise elsewhere. Together, these two knobs illustrate, as an analogy, why zero-density bounds say that off-line zeros cannot crowd together.',
 'distill_diagram': {'analogy_title': 'Concert Hall Acoustic Choir', 'analogy_sub': 'Destructive interference cancels random hums into quiet murmurs', 'force_a_title': 'Critical Strip Coordinate (sigma)', 'force_a_sub': 'Distance from critical line Re(s) = 1/2 toward the unit boundary', 'force_b_title': 'Dirichlet Window Length (log T)', 'force_b_sub': 'Total frequency observation span bounding mean-square energy', 'threshold_title': 'Huxley-Ingham Crossover Barrier (sigma = 3/4)', 'threshold_pass': 'Zero-density bound N(sigma, T) <= T^(c(1-sigma) + eps) (Ingham, Huxley)', 'threshold_fail': 'More zeros off the critical line than the bound allows'},
 'act2_intuition': "Think of a Dirichlet polynomial sum a_n n^(-sigma - it) as a vast ensemble of rotating phasors in the complex plane, each spinning at an angular frequency proportional to log(n). Under typical conditions, these rotating vectors interfere destructively, keeping the total sum bounded. For the Riemann zeta function to hit zero far off the critical meridian (for instance, at real coordinate sigma = 0.80), thousands of distinct prime frequencies must abruptly conspire to point in the exact same phase direction. In the Montgomery–Halász large sieve, these frequencies are treated like nearly orthogonal vectors in a Hilbert space. If a signal concentrates massive L^2 spectral energy at a single frequency height t_1, it starves alternative heights from aligning. At sigma = 3/4, Ingham's bound (DOI 10.1093/qmath/os-11.1.201) and Huxley's bound (DOI 10.1007/BF01418933) give the same total exponent, 3(0.25)/1.25 = 12(0.25)/5 = 0.600; Ingham's is the smaller below sigma = 3/4 and Huxley's is the smaller above it.",
 'act2_deepening': "The mathematical coupling between the threshold coordinate sigma and the observation window log T is governed by the duality between Dirichlet series and continuous operator spectra. To isolate hypothetical zeros, analytic number theorists construct mollifiers—finite Dirichlet polynomials M(s) crafted so that the product zeta(s) M(s) approximates unity across typical frequencies. Where a zero occurs, the product deviates markedly from one, converting a delicate root-finding challenge into an L^2 energy concentration problem. By applying Halász's lemma, the sum over well-spaced frequencies t_r is bounded by the norm of an operator matrix whose off-diagonal entries decay like 1 / |t_r - t_s|. As the observation parameter log T increases, these orthogonality constraints tighten dramatically. Near the critical line where sigma approaches one-half, the bound requires delicate high-moment cancellations; but as sigma pushes rightward past the three-quarter mark, the zero-detecting exponent plunges linearly. This machinery limits how many zeros can lie off the critical line; it does not rule them out.",
 'walkthrough': ['Experiment 1 (Trace the 4-Stage Mollifier & Sieve Pipeline): Step through Stages '
                 '1 -> 4 above to see how Dirichlet mollification M(s), Large Sieve L^2 '
                 'orthogonality, and Huxley-Ingham zero-detectors lead to a zero-density bound.',
                 'Experiment 2 (Inspect the sigma = 3/4 Crossover): Observe in the SVG phase '
                 "diagram below how Ingham's hyperbolic curve (1/2 < sigma <= 3/4) hands off "
                 "smoothly to Huxley's linear slope at sigma = 0.75.",
                 'Experiment 3 (Read the Cheeger-Fiedler Spectral Gap): The spectral gap '
                 'ratio lambda_2 / lambda_max = 0.418 in the readout strip is a fixed illustrative '
                 'value, shown beside the classical Cheeger conductance inequality '
                 'h_G^2 / 2 <= lambda_2 <= 2 h_G.'],
 'act4_human_ai': "Analytic number theory involves a lot of 'epsilon-delta bookkeeping', where a slip in a constant can be hard to find. Lean 4 formalization is one response: a proof assistant checks each step. The README of anthropics/formal-math (https://github.com/anthropics/formal-math) lists a zeta23 project, and whether it builds is something this site has not checked. Mathlib (DOI 10.1145/3372885.3373824) is the community library that Lean projects like this build on. Nothing in this folio shows that AI systems speed up work on zero-density estimates.",
 'act4_deepening': 'The formalization of zero-density estimates highlights how modern AI proof assistants transform frontier analytic research. Translating complex contour shifts and mollifier bounds into Lean 4 requires decomposing intricate analytic arguments into modular lemmas that automated reasoning agents can systematically verify. One plausible division of labour is that human researchers choose the high-level architecture, such as contour paths, mollifier coefficients and energy partitions, while automated tactics handle routine inequalities. That is a possibility, not a description of any project the folio has checked. Lowering the zero-density exponent below the Huxley value is an example of an open problem in this area (Guth and Maynard have since done so near sigma = 3/4); whether formalization or AI search will help with the next steps is not something this folio can say.',
 'cf_bridge': 'This bridge is an analogy the folio draws and nothing more. A Markov model of '
              'an ion channel moving between closed and open states has a relaxation time set by '
              'the spectral gap of its generator, and the folio places that picture beside '
              'zero-density bounds. Number theory says nothing about a real CFTR channel or about '
              'any drug, and nothing here is medical advice.',
 'sources': ['Riemann, B. (1859). Über die Anzahl der Primzahlen unter einer gegebenen Grösse. '
             'Monatsberichte der Berliner Akademie.',
             'Ingham, A. E. (1940). On the estimation of N(σ, T). Quarterly Journal of '
             'Mathematics, os-11(1), 201–202. DOI: 10.1093/qmath/os-11.1.201.',
             'Huxley, M. N. (1972). On the difference between consecutive primes. Inventiones '
             'Mathematicae, 15(2), 164–170. DOI: 10.1007/BF01418933.',
             'Conrey, J. B. (1989). More than two fifths of the zeros of the Riemann zeta function '
             'are on the critical line. J. Reine Angew. Math., 399, 1–26. DOI: '
             '10.1515/crll.1989.399.1.',
             'Guth, L., & Maynard, J. (2026). New large value estimates for Dirichlet polynomials. '
             'Annals of Mathematics, 203(2). DOI: 10.4007/annals.2026.203.2.6; arXiv:2405.20552.',
             'Alpöge, L., & Furman, R. (2026). More than two thirds of the zeta zeros are simple '
             'and on the critical line. arXiv:2608.13637. Listed as the zeta23 project in '
             'anthropics/formal-math (https://github.com/anthropics/formal-math); README read '
             '2026-11-14. Not built or checked by this site. The project also contains zeta23/Challenge/XiPrime.lean (zeros of ξ′), which this folio does not rely on.',
             'Repository: openai/math (https://github.com/openai/math), cited in an earlier edition '
             'for a zero-free region result (zero-free in Re s > 7/8 for every Dirichlet '
             'L-function); this site has not checked it.',
             'The mathlib Community (2020). The Lean mathematical library. CPP 2020, 367–381. '
             'DOI: 10.1145/3372885.3373824.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Ingham-Huxley '
        'zero-density exponent crossover at sigma = 3/4">\n'
        '            <line x1="60" y1="185" x2="620" y2="185" stroke="currentColor" '
        'stroke-opacity="0.35"/>\n'
        '            <line x1="60" y1="25" x2="60" y2="185" stroke="currentColor" '
        'stroke-opacity="0.35"/>\n'
        '            <line x1="340" y1="25" x2="340" y2="185" stroke="var(--tp-minium)" '
        'stroke-dasharray="4,4" stroke-width="1.5"/>\n'
        '            <path d="M 60 35 Q 200 72 340 105 L 620 185" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="3"/>\n'
        '            <circle cx="60" cy="35" r="6" fill="var(--tp-prussian)"/>\n'
        '            <circle cx="340" cy="105" r="7" fill="var(--tp-minium)"/>\n'
        '            <circle cx="620" cy="185" r="6" fill="var(--tp-verdigris)"/>\n'
        '            <text x="50" y="205" font-size="11" fill="currentColor">σ = 0.50 (Critical '
        'Line)</text>\n'
        '            <text x="285" y="205" font-size="11" fill="var(--tp-minium)">σ = 0.75 '
        '(Crossover c=0.60)</text>\n'
        '            <text x="565" y="205" font-size="11" fill="currentColor">σ = 1.00 (Prime '
        'Number Thm)</text>\n'
        '            <text x="110" y="62" font-size="11" fill="var(--tp-prussian)">Ingham: '
        '3(1-σ)/(2-σ)</text>\n'
        '            <text x="415" y="132" font-size="11" fill="var(--tp-verdigris)">Huxley: '
        '12(1-σ)/5</text>\n'
        '          </svg>',
 'scite': {'doi': '10.1515/crll.1989.399.1',
           'fetched_on': '2026-11-08',
           'citing_publications': 230,
           'supporting': 1,
           'mentioning': 12,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Conrey 1989 (DOI 10.1515/crll.1989.399.1), checked '
                      '2026-11-08: 230 citing publications (1 supporting, 12 mentioning, 0 '
                      'contrasting) and no retraction notice. These counts describe that one '
                      'paper, not this folio.'},
 'word_count': '4,650 WORDS'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a 3D analytic landscape of harmonic poles and '
        'zero-free critical strip valleys over the complex plane would look like (artistic '
        'impression, not a formal plot)',
 'caption': 'Conceptual Vision Plate M.02-V (Imagining What It Would Look Like) · Artistic '
            'geometric landscape imagining harmonic pole peaks and zero-free critical strip '
            'valleys across the complex plane.'}

DISPATCH = {'kicker': 'ZERO-DENSITY ESTIMATES · A LEAN 4 REPOSITORY STATEMENT, REPORTED NOT CHECKED HERE',
 'headline': "Huxley's Zero-Density Bound, Conrey's Critical-Line Result and a Lean 4 Repository "
             'Statement',
 'body': "Martin Huxley's zero-density estimate N(sigma, T) <= T^(12(1-sigma)/5 + eps) "
         "(Invent. Math. DOI 10.1007/BF01418933) and J. B. Conrey's result that more than 2/5 "
         'of the zeros of zeta lie on Re(s) = 1/2 (J. Reine Angew. Math. DOI '
         '10.1515/crll.1989.399.1) are classical. The README of anthropics/formal-math also '
         'lists a Lean 4 project, zeta23, for a more recent critical-line result. This site '
         'reports that statement and has not built the project or checked the mathematics.'}

META_3D = ('Riemann Critical-Line Zero-Density Canyon',
 'X: Real Part σ - 1/2 · Z: Imaginary Height t · Y: Log-Modulus |ξ(s)| & Zero-Density Cliffs')

ES_TRANSLATION = {'title_es': 'Estimaciones de Densidad de Ceros de la Función Zeta de Riemann y Desigualdades de '
             'Gran Criba',
 'subtitle_es': 'Estimaciones clásicas de densidad de ceros de la función zeta de Riemann y lo que '
                'afirma el README de un repositorio público en Lean 4 sobre un resultado reciente '
                'en la línea crítica. La comparación con la relajación de cadenas de Markov es una '
                'analogía de este folio.',
 'why_es': 'La Gran Criba de Montgomery–Halász trata las frecuencias como vectores casi '
           'ortogonales: si una señal concentra demasiada energía en una frecuencia, no puede '
           'acumularla simultáneamente en todas las demás.',
 'bridge_es': 'Es solo una analogía de este folio: en un modelo de Markov de un canal iónico entre '
              'estados cerrado y abierto, el tiempo de relajación depende de la brecha espectral '
              'del generador. La teoría de números no dice nada sobre un canal CFTR real ni sobre '
              'ningún medicamento, y nada de esto es consejo médico.',
 'plain_es': 'En palabras sencillas, Bernhard Riemann se preguntó cómo están distribuidos los números primos a lo largo de la recta numérica. Los primos, como dos, tres, cinco y siete, son los ladrillos de los números enteros, porque todo entero se forma multiplicándolos. A simple vista parecen esparcidos al azar, pero contarlos está muy ligado a los lugares donde se anula la función zeta. La Hipótesis de Riemann dice que todos los ceros no triviales están sobre una misma recta; sigue siendo una conjetura abierta. Los números primos también se usan en la criptografía de clave pública, pero este folio no afirma que ningún resultado de los aquí tratados haga más seguro o menos seguro ningún código.',
 'deep_es': 'Para comprender las cotas de densidad de ceros, conviene observar la relación entre la coordenada real sigma y la ventana de observación logarítmica. En el deslizador de sigma, cerca de la línea crítica las cotas son más débiles, y al desplazarse hacia la derecha el exponente baja. Al ampliar la ventana de observación, la gran criba limita la energía disponible: si un conjunto de frecuencias concentra energía en un punto, le queda menos para otras alturas. En sigma igual a tres cuartos, las cotas de Ingham y de Huxley dan el mismo exponente total, 0.600. Estas cotas limitan cuántos ceros pueden estar fuera de la línea crítica; no los descartan. El README de anthropics/formal-math afirma contener un proyecto en Lean 4 sobre un resultado reciente en la línea crítica; este sitio reporta esa afirmación y no ha compilado el proyecto ni revisado la matemática.'}
