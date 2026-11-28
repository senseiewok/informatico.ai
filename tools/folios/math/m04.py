#!/usr/bin/env python3
"""Folio M.04 (MATH): Polynomial Freiman–Ruzsa (PFR) Entropy Calculus and the 22-Million Equational Magma Graph."""
from __future__ import annotations

SLUG = 'm04'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.04',
 'slug': 'm04',
 'pillar': 'math',
 'category_code': 'M',
 'title': 'Polynomial Freiman–Ruzsa (PFR) Entropy Calculus and the 22-Million Equational Magma '
          'Graph',
 'subtitle': 'A reading of the entropy proof of the Polynomial Freiman–Ruzsa conjecture in '
             'characteristic 2 (Gowers, Green, Manners and Tao), the public Lean 4 project whose '
             "README says it formalizes that proof, and the Equational Theories project's "
             '4,694 magma laws and 22,028,942 ordered pairs. The comparison with genetics is an '
             'analogy.',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.2',
 'status_badge': 'REDATED REV 1.2',
 'primary_kernel': 'tools/discovery/frontier_ai_math_catalog.py',
 'colophon': {'identifier': 'M.04 · Additive Combinatorics & Algebra',
              'kernels': 'PFR entropy proof · Lean 4 project (README) · 22,028,942 magma-law pairs',
              'benchmarks': 'Doubling |A + A| ≤ K|A| ⇒ covered by ≤ 2K^12 cosets (as stated in the project README)',
              'bridge': 'Ruzsa entropic distance ↔ grouping variant profiles (analogy only)'},
 'sliders': [{'label': 'Additive Doubling Constant K (|A + A| / |A|)',
              'min': 1.2,
              'max': 8.0,
              'step': 0.2,
              'value': 2.4,
              'unit': 'K = '},
             {'label': 'Ruzsa Entropic Distance d_R(X, Y)',
              'min': 0.1,
              'max': 3.0,
              'step': 0.05,
              'value': 0.85,
              'unit': 'd_R = '}],
 'steps': ['Stage 1 (Small Doubling Hypothesis): A subset A ⊂ F_2^n satisfies |A + A| ≤ K|A|, '
           'indicating hidden approximate subgroup structure.',
           'Stage 2 (Ruzsa Entropic Triangle Inequality): Defines entropic distance d(X, Y) = H(X '
           "- Y') - (H(X) + H(Y'))/2, where Y' is an independent copy of Y.",
           'Stage 3 (Tau-Minimizer): The proof studies a minimizer of an entropic functional τ and '
           'uses it to show that d(X, U_H) is small for the uniform distribution U_H on a '
           "subgroup H. This page's slider is a simplified picture of that step, not the "
           "paper's argument.",
           'Stage 4 (Polynomial Coset Covering): The theorem, as stated in the README of the '
           'Lean project, says A is covered by at most 2·K^12 cosets of a subspace H of size at '
           'most |A|. Separately, the Equational Theories project concerns 4,694 × 4,693 = '
           '22,028,942 ordered pairs of magma laws.'],
 'readouts': [{'label': 'Polynomial Coset Bound', 'value': '≤ 2 · K^12 Cosets (per project README)'},
              {'label': 'Equational Theories Pairs', 'value': '22,028,942 ordered pairs (4694 × 4693; progress not checked here)'},
              {'label': 'Lean 4 Project Status', 'value': 'README: main proof formalized (not built here)'},
              {'label': 'Entropic Contraction Picture', 'value': 'simplified illustration, not the paper\'s argument'}],
 'sidenote_1': {'kicker': 'SIDENOTE M.04-A · WHAT THE PROJECT README STATES',
                'body': 'The README of teorth/pfr describes a Lean 4 formalization of the proof, '
                        'with a human-written blueprint. It states that the main purpose was '
                        'completed, and that a second stage, which developed consequences and an '
                        'argument of Jyun-Jie Liao reducing the exponent 12 to 11, has also been '
                        'completed. How long this took is not stated there, and no duration is '
                        'claimed here.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.04-B · A LOOSE ANALOGY',
                'body': 'The folio compares measuring how far a distribution is from a clean '
                        'structure with grouping measured profiles of related variants. This is '
                        'an analogy only. It claims no use for CFTR data, and nothing here is '
                        'medical advice.'},
 'skill': {'filename': 'pfr-entropic-combinatorics-SKILL.md',
           'name': 'pfr-entropic-combinatorics',
           'description': 'AI-agnostic additive combinatorics and universal algebra skill for '
                          'Ruzsa entropic distance, Polynomial Freiman-Ruzsa coset bounds, and '
                          'equational magma implication graphs.',
           'rules': ["Compute Ruzsa entropic distance d(X, Y) = H(X - Y') - 0.5*(H(X) + H(Y')) for "
                     "independent copies X, Y' on abelian groups.",
                     'State the Ruzsa triangle inequality d(X, Z) <= d(X, Y) + d(Y, Z) and the PFR '
                     'covering bound <= 2 * K^12 as results of the cited paper and project README.',
                     'Treat an implication between magma laws as established only when a Lean proof or a '
                     'finite counterexample is cited, and say when you have not checked it.']},
 'revisions': [{'edition': 'REV 1.2',
                'date': '2026-11-14',
                'summary': 'REV 1.2 (Redated 2026-11-14): Grounding revision. The opening scene of '
                           'Marton in a Budapest office in 1998, the claim that the Lean '
                           'formalization took 21 days, and the claim that all 22,028,942 magma '
                           'law pairs are resolved in a machine-checked graph are removed: the '
                           'project READMEs do not say these things. The page now reports what the '
                           'two READMEs state and that this site did not check them. The number '
                           '22,028,942 is stated correctly as 4,694 × 4,693 ordered pairs (not '
                           '4,694²). The links to data compression and encryption, the reference to '
                           'anthropics/formal-math as part of these projects, and the AAV and '
                           'lipid-nanoparticle passage are removed; the Cystic Fibrosis comparison '
                           'is a labeled analogy.',
                'opus': 'Review: DOIs checked in Crossref and the Scite index on 2026-11-14; both '
                        'repository READMEs read on that date (teorth/pfr states the 2K^12 '
                        'covering and the completed formalization; teorth/equational_theories '
                        'states the 4,694 laws, 22,028,942 pairs and the 25 September 2024 launch). '
                        'The Annals abstract was checked with Scite and states the result in '
                        'characteristic 2.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-02',
                'summary': 'REV 1.1 (Redated 2026-11-02): Re-verified Polynomial Freiman-Ruzsa '
                           "(PFR) entropic doubling, Marton's conjecture bounds, and "
                           '22,028,942-edge magma implication graph with 4-Seat Frontier Council '
                           'review.',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Ruzsa entropic triangle inequality submodularity and polynomial coset '
                        'covering bound <= 2 * K^12. (REV 1.2: this "verified" wording is '
                        'withdrawn; the bound is as stated in the project README.)'},
               {'edition': 'REV 1.0',
                'date': '2026-11-01',
                'summary': 'REV 1.0 (Published 2026-11-01): Initial publication of the PFR '
                           'Entropic Calculus and 22,028,942-edge Equational Magma Graph '
                           'monograph.',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Ruzsa entropic triangle inequality and 4,694² = 22,033,636 total magma '
                        'law pairs (22,028,942 off-diagonal implications). (REV 1.2: the '
                        'arithmetic is right, since 4,694 × 4,693 = 22,028,942; the "verified" '
                        'wording is withdrawn.)'}],
 'governing_law': 'PFR entropy proof · Lean 4 project (README) · 22,028,942 magma-law pairs',
 'volume': 2,
 'volume_code': 'VOL. 02',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.4007/annals.2025.201.2.5',
           'fetched_on': '2026-11-08',
           'citing_publications': 25,
           'supporting': 0,
           'mentioning': 14,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Gowers, Green, Manners & Tao 2025 (DOI '
                      '10.4007/annals.2025.201.2.5), checked 2026-11-08: 25 citing publications '
                      '(0 supporting, 14 mentioning, 0 contrasting) and no retraction notice. '
                      'These counts describe that one paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'act1_dropcap': "In additive combinatorics, a set A in F_2^n has small doubling if |A + A| <= K|A| for a modest constant K. The Polynomial Freiman–Ruzsa conjecture, attributed to Katalin Marton and widely known under that name, asks whether such a set must be covered by a number of cosets of a subspace that is only polynomial in K. In November 2023, Timothy Gowers, Ben Green, Freddie Manners and Terence Tao posted a proof in characteristic 2 (arXiv:2311.05762; Annals of Mathematics 2025, DOI 10.4007/annals.2025.201.2.5).",
 'act1_plain_bridge': 'In plain words, this puzzle asks how closely a messy collection of points must resemble a tidy, organized grid. Imagine tossing a handful of coins onto a blanket. If adding their positions together produces very few new positions, the coins must secretly share a hidden alignment. The conjecture says that such a set can be covered by a modest number of tidy frames, where "modest" means a polynomial in the doubling constant. This folio makes no claim about data compression, streaming or encryption.',
 'act1_body': "Gowers, Green, Manners and Tao establish the conjecture in characteristic 2 using Shannon entropy and an entropic version of Ruzsa distance (Annals of Mathematics 2025, DOI 10.4007/annals.2025.201.2.5). The repository https://github.com/teorth/pfr holds a Lean 4 formalization project whose README states that its main purpose, formalizing the proof, was completed, followed by a second stage developing consequences. The Equational Theories project (https://github.com/teorth/equational_theories), launched on 25 September 2024 according to its README, concerns the implications among 4,694 magma laws, that is 4,694 × 4,693 = 22,028,942 ordered pairs. Its README says that accepted implications are verified in Lean and that other claims are tracked as conjectured. This site has not built either project and has not checked how far the second one has progressed.",
 'act1_stakes': "A blueprint splits a proof into small lemmas that different people can formalize independently, with a dependency graph showing what remains. The README of the PFR project links its blueprint and describes the formalization as completed. Whether this way of working carries over to other proofs is not something the folio assesses. A formalization also needs a reader to judge that the formal statement matches the statement intended.",
 'pullquote': 'By translating sumset size |A + A| <= K|A| into Shannon entropy distances d(X, Y), '
              'the proof of PFR in characteristic 2 turns a counting problem into one about '
              'entropy.',
 'pullquote_cite': 'Editorial Synthesis · Gowers, Green, Manners & Tao (2023)',
 'chronology': [('1960s–1990s',
                 'Freiman & Ruzsa',
                 'Develop the structure theory of sets with small doubling |A + A| <= K|A| '
                 '(see Ruzsa 1999, Astérisque 258).'),
                ('Date not stated here',
                 'Katalin Marton',
                 'The Polynomial Freiman-Ruzsa conjecture is attributed to her in the abstract of '
                 'Gowers, Green, Manners & Tao.'),
                ('Nov 2023',
                 'Gowers, Green, Manners & Tao',
                 'Establish PFR in F_2^n (covering A by <= 2 K^12 cosets, per the project README) '
                 '(arXiv:2311.05762).'),
                ('After Nov 2023',
                 'teorth/pfr project',
                 'README: formalization of the proof completed, then a second stage including an '
                 'exponent reduction from 12 to 11 by Jyun-Jie Liao.'),
                ('From Sep 2024',
                 'Equational Theories Project',
                 'Launched 25 September 2024 (README); concerns 22,028,942 ordered pairs of '
                 '4,694 magma laws.')],
 'act2_analogy': 'Everyday analogy: smoothing a wrinkled bedsheet. Tugging one wrinkle at a time tends to push the fold somewhere else; working across the whole sheet at once flattens it. The analogy is loose: it pictures trading point-by-point counting for one quantity, entropy, that describes the whole set at once.',
 'act2_plain_primer': 'To see how informational smoothing works, you can explore two intuitive control knobs. The first knob measures the expansion rate, tracking how many new combinations appear when you add a set of points to itself. When this doubling knob is low, points stay bundled together in a tight cluster; but as you dial it higher, the points spread out across the space. The second knob measures informational distance, tracking how far our messy arrangement sits from a perfectly uniform grid. When this distance knob is high, the points are scattered like wrinkles on the bedsheet; as you lower it, the picture flattens. Together, these two knobs are a picture, not the paper\'s argument: they suggest that when the expansion rate is bounded, the informational distance can be made small.',
 'distill_diagram': {'analogy_title': 'Wrinkled Bedsheet Steam Ironing', 'analogy_sub': 'Working on the whole sheet at once, not one wrinkle at a time', 'force_a_title': 'Doubling Constant K (|A+A|/|A|)', 'force_a_sub': 'Controls subset expansion under pairwise vector addition', 'force_b_title': 'Ruzsa Entropic Distance d_R', 'force_b_sub': 'Measures deviation from a uniform distribution on a coset of a subgroup', 'threshold_title': 'Marton Coset Covering Horizon', 'threshold_pass': 'Covered by at most 2 K^12 cosets (as stated in the project README)', 'threshold_fail': 'No polynomial covering bound'},
 'act2_intuition': "Why might trading counting for Shannon entropy help? This is the folio's own reading, not a claim taken from the paper: entropy H(X) = -sum p(x) log p(x) obeys inequalities, such as submodularity, that can be chained step by step, which may be harder to do with the sizes of sumsets directly. Gowers, Green, Manners and Tao work with an entropic Ruzsa distance d_R(X, Y) = H(X - Y') - 0.5 [H(X) + H(Y')], where Y' is an independent copy of Y; it is zero when X and Y are uniform on cosets of the same subgroup. The theorem, as stated in the README of the Lean 4 project teorth/pfr, is that any subset A of F_2^n with small doubling |A + A| <= K |A| is covered by at most 2 K^12 cosets of a subspace H of size at most |A|; the paper's argument is in the Annals (DOI 10.4007/annals.2025.201.2.5) and is not reproduced here.",
 'act2_deepening': "Here is how doubling and entropic distance meet. Let X and Y' be independent and uniform on a set A in F_2^n with |A + A| <= K |A|. Then H(X) = H(Y') = log |A|, and since subtraction is addition in F_2^n, X - Y' takes at most |A + A| values, so H(X - Y') <= log K + log |A|. Hence d_R(X, X) <= log K. If d_R(X, X) = 0, X is uniform on a coset of a subgroup. The proof then works with a minimizer of an entropic functional to show that the distance to such a uniform distribution must be small, and a covering argument turns that into the bound of at most 2 K^12 cosets. The page's contraction slider is a simplified picture of this, not the paper's argument; read the paper for the details.",
 'walkthrough': ['Experiment 1 (Follow the 4-Stage Entropic Descent): Click through Stages 1 -> 4 '
                 'above to trace how small doubling |A+A| <= K|A| maps to Ruzsa entropic distance '
                 'd(X, Y), tau-minimizer descent, and the 2 K^12 coset covering bound.',
                 'Experiment 2 (Explore the 22-Million Magma Implication Graph): Inspect the '
                 'right-hand panel of the SVG schematic, a sketch of the 4,694 equational laws and the '
                 '22,028,942 ordered pairs the project studies; it does not show verified '
                 'results.',
                 'Experiment 3 (Apply Blueprint Decomposition): Use the portable SKILL.md below to '
                 'structure complex engineering or proof tasks as human-readable DAG blueprints '
                 'with independent machine-verifiable nodes.'],
 'act4_human_ai': "The READMEs of the PFR and Equational Theories projects describe open collaborations around Lean 4 proofs and, in the second case, a dashboard of verified and conjectured implications. Lean's kernel rejects a step that does not follow, so, barring a bug in Lean itself, a false statement cannot be proved; an unproved step has to appear as sorry or an added axiom, and #print axioms on the final theorem lists both. Lean cannot check that a formal statement says what its authors meant. This folio cannot say how many contributors were human or AI, or how the work compares with unassisted work. The anthropics/formal-math repository is not part of either project, and the folio draws no link to it. Mathlib (DOI 10.1145/3372885.3373824) is the library such projects build on.",
 'act4_deepening': 'Splitting a large proof or a large list of questions into small pieces that different people, or programs, can take on is one way to organize formalization. The Equational Theories README describes this for 4,694 magma laws; this folio has not checked how far the project got or which tools settled which pairs. Whether similar entropy methods work over other groups is a question for mathematicians and is not addressed here.',
 'cf_bridge': 'This bridge is an analogy the folio draws and nothing more. The folio compares '
              'measuring how far a probability distribution is from a clean structure with '
              'grouping measured profiles of related variants. It describes no gene-delivery '
              'design, no sequence, and no result about CFTR, and nothing here is medical advice.',
 'sources': ['Gowers, W. T., Green, B., Manners, F., & Tao, T. (2025). On a conjecture of Marton. '
             'Annals of Mathematics, 201(2), 515–549. DOI: 10.4007/annals.2025.201.2.5; '
             'arXiv:2311.05762.',
             'Repository: teorth/pfr, The Polynomial Freiman-Ruzsa Conjecture '
             '(https://github.com/teorth/pfr). README read 2026-11-14; it states the 2K^12 '
             'covering and that the formalization and a second stage were completed. Not built '
             'or checked by this site.',
             'Repository: teorth/equational_theories, Equational theories project '
             '(https://github.com/teorth/equational_theories). README read 2026-11-14; it states '
             '4,694 laws, 4,694 × 4,693 = 22,028,942 implications to be decided or refuted, '
             'and that verified ones are checked in Lean. Progress not checked by this site.',
             "Ruzsa, I. Z. (1999). An analog of Freiman's theorem in groups. Astérisque, 258, "
             '323–326.',
             'The mathlib Community (2020). The Lean mathematical library. Proceedings of the '
             '9th ACM SIGPLAN CPP Conference (CPP '
             '2020), 367–381. DOI: 10.1145/3372885.3373824.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Ruzsa entropic '
        'descent and the 22,028,942 ordered pairs of distinct magma laws">\n'
        '            <path d="M 70 50 C 180 55, 240 155, 360 165" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="3"/>\n'
        '            <circle cx="70" cy="50" r="6" fill="var(--tp-minium)"/>\n'
        '            <circle cx="215" cy="108" r="6" fill="var(--tp-prussian)"/>\n'
        '            <circle cx="360" cy="165" r="7" fill="var(--tp-verdigris)"/>\n'
        '            <text x="60" y="38" font-size="11" fill="var(--tp-minium)">Initial Set A: '
        '|A+A| ≤ K|A|</text>\n'
        '            <text x="165" y="95" font-size="11" fill="var(--tp-prussian)">τ-Minimizer '
        'Descent d(X,Y)</text>\n'
        '            <text x="260" y="190" font-size="11" fill="var(--tp-verdigris)">Subgroup '
        'Coset Cover ≤ 2·K^12 (d=0)</text>\n'
        '            <rect x="430" y="40" width="210" height="145" fill="none" '
        'stroke="currentColor" stroke-opacity="0.3"/>\n'
        '            <circle cx="480" cy="80" r="8" fill="var(--tp-prussian)"/><circle cx="580" '
        'cy="80" r="8" fill="var(--tp-prussian)"/>\n'
        '            <circle cx="530" cy="145" r="9" fill="var(--tp-verdigris)"/>\n'
        '            <line x1="486" y1="86" x2="524" y2="138" stroke="currentColor" '
        'stroke-width="1.8"/>\n'
        '            <line x1="574" y1="86" x2="536" y2="138" stroke="currentColor" '
        'stroke-width="1.8"/>\n'
        '            <text x="448" y="60" font-size="11" fill="currentColor">4,694 × 4,693 = 22,028,942 '
        'pairs</text>\n'
        '            <text x="455" y="172" font-size="11" fill="var(--tp-verdigris)">Progress: see '
        'project dashboard</text>\n'
        '          </svg>',
 'scite': {'doi': '10.4007/annals.2025.201.2.5',
           'fetched_on': '2026-11-08',
           'citing_publications': 25,
           'supporting': 0,
           'mentioning': 14,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Gowers, Green, Manners & Tao 2025 (DOI '
                      '10.4007/annals.2025.201.2.5), checked 2026-11-08: 25 citing publications '
                      '(0 supporting, 14 mentioning, 0 contrasting) and no retraction notice. '
                      'These counts describe that one paper, not this folio.'},
 'word_count': '4,650 WORDS'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a Polynomial Freiman-Ruzsa entropic coset '
        'covering lattice and the 22,028,942 ordered pairs of distinct magma laws would look like '
        '(artistic impression, not a formal plot)',
 'caption': 'Conceptual Vision Plate M.04-V (Imagining What It Would Look Like) · Artistic '
            'mathematical visualization imagining Ruzsa entropic distance contracting an '
            'approximate set A into <= 2 K^12 cosets of one subgroup, alongside the 22,028,942 '
            'ordered pairs of distinct magma laws (each pair asks whether one law implies the other; '
            'this folio reports, not checks, the project\'s answers).'}

DISPATCH = {'kicker': 'POLYNOMIAL FREIMAN–RUZSA (PFR) · A LEAN 4 PROJECT README AND THE EQUATIONAL THEORIES '
           'PROJECT, REPORTED NOT CHECKED HERE',
 'headline': "Gowers, Green, Manners & Tao's Shannon-Entropy Proof of PFR, and Two Public Lean 4 "
             'Projects',
 'body': 'Published in Annals of Mathematics (Gowers, Green, Manners & Tao 2025, DOI '
         '10.4007/annals.2025.201.2.5), the proof covers a set A in F_2^n with |A + A| <= K|A| by '
         'at most 2 K^12 cosets, as stated in the README of teorth/pfr, which also states that '
         'its Lean 4 formalization was completed. The Equational Theories project concerns '
         '4,694 magma laws and 22,028,942 ordered pairs. This site reports those statements and '
         'has not built either project.'}

META_3D = ('Polynomial Freiman–Ruzsa Entropic Gaussian Dome',
 'X/Z: Doubling Set Coset Coordinates · Y: Ruzsa Entropic Convolution Density')

ES_TRANSLATION = {'title_es': 'Cálculo de Entropía Polinomial de Freiman–Ruzsa (PFR) y el Grafo Ecuacional de 22 '
             'Millones de Leyes de Magmas',
 'subtitle_es': 'Una lectura de la demostración entrópica de la conjetura polinomial de '
                'Freiman–Ruzsa en característica 2 (Gowers, Green, Manners y Tao), del proyecto '
                'público en Lean 4 que, según su README, la formaliza, y de las 4,694 leyes de '
                'magmas y 22,028,942 pares ordenados del proyecto de Teorías Ecuacionales. La '
                'comparación con la genética es una analogía.',
 'why_es': 'La distancia entrópica de Ruzsa mide cuánto se parece una nube desordenada de datos a '
           'una estructura algebraica limpia: si al sumar el conjunto consigo mismo apenas crece, '
           'queda cubierto por un número de clases laterales de un mismo subespacio que crece solo '
           'de forma polinomial con la constante de duplicación.',
 'bridge_es': 'Es solo una analogía de este folio: se compara medir qué tan lejos está una '
              'distribución de probabilidad de una estructura limpia con agrupar perfiles medidos '
              'de variantes relacionadas. No describe ningún diseño de entrega génica, ninguna '
              'secuencia ni ningún resultado sobre CFTR, y nada de esto es consejo médico.',
 'plain_es': 'En palabras sencillas, este acertijo pregunta qué tanto debe parecerse una colección desordenada de puntos a una cuadrícula ordenada. Imaginen que arrojan un puñado de monedas sobre una manta. Si al sumar sus posiciones casi no aparecen posiciones nuevas, las monedas comparten una alineación secreta. La conjetura dice que un conjunto así se puede cubrir con un número modesto de marcos ordenados, donde "modesto" significa un polinomio en la constante de duplicación. Este folio no afirma nada sobre compresión de datos, transmisión ni cifrado.',
 'deep_es': 'El núcleo de esta demostración se comprende a través de la relación entre la tasa de duplicación del conjunto y la distancia entrópica de Ruzsa. En el deslizador de duplicación, valores pequeños indican que el conjunto apenas crece al sumarse consigo mismo. Por su parte, la distancia entrópica de Ruzsa mide qué tan lejos se encuentra una distribución de probabilidades respecto a una distribución uniforme sobre una clase lateral de un subgrupo. Gowers, Green, Manners y Tao sustituyen el conteo de puntos por la entropía de Shannon. El deslizador de contracción es solo una imagen simplificada, no el argumento del artículo. El README del proyecto teorth/pfr afirma que la formalización en Lean 4 de la demostración se completó, y el de Equational Theories describe 4,694 leyes y 22,028,942 pares ordenados; este sitio reporta esas afirmaciones y no ha compilado ni revisado ninguno de los dos proyectos.'}
