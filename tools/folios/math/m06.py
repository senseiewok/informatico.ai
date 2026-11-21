#!/usr/bin/env python3
"""Folio M.06 (MATH): Sub-Cubic Fine-Grained Reductions (3SUM → APSP) and Step-Level Process Supervision (PRM800K)."""
from __future__ import annotations

SLUG = 'm06'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.06',
 'slug': 'm06',
 'pillar': 'math',
 'category_code': 'M',
 'title': 'Sub-Cubic Fine-Grained Reductions (3SUM → APSP) and Step-Level Process Supervision '
          '(PRM800K)',
 'subtitle': "Ryan Williams's circuit-complexity algorithm for All-Pairs Shortest Paths, a "
             "repository README's statement of a polynomial improvement for APSP and 3SUM, and "
             "OpenAI's step-level process-supervision paper. Comparisons with proof search or "
             "genomics are this folio's own analogies.",
 'date_published': '2026-11-01',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.2',
 'status_badge': 'REDATED REV 1.2',
 'primary_kernel': 'tools/discovery/formal_proof_thermodynamic_landscape.py',
 'colophon': {'identifier': 'M.06 · Fine-Grained Complexity & PRM',
              'kernels': 'Williams APSP · 3SUM · Step-Level PRM',
              'benchmarks': 'SIAM 10.1137/15M1024524 · PRM800K (arXiv:2305.20050)',
              'bridge': 'Search pruning ↔ screening many candidates (analogy only)'},
 'sliders': [{'label': 'Polynomial Block Degree Parameter (d_poly)',
              'min': 2,
              'max': 11,
              'step': 1,
              'value': 5,
              'unit': 'd_poly = '},
             {'label': 'Constraint Clause Density (α = m / n)',
              'min': 2.5,
              'max': 6.0,
              'step': 0.02,
              'value': 4.26,
              'unit': 'α = '}],
 'steps': ['Stage 1 (Min-Plus Distance Product): Formulates All-Pairs Shortest Paths as (A ⋆ '
           'B)_{ij} = min_k (A_{ik} + B_{kj}) over n = 4,096 vertices.',
           'Stage 2 (Razborov-Smolensky Polynomial Batching): Williams uses Razborov-Smolensky '
           'polynomials over F_2 to reduce a min-plus product to a relatively small number of '
           'rectangular matrix products (SIAM J. Comput. 2018, abstract).',
           'Stage 3 (Step-Level Scoring): A process reward model scores each step of a solution. '
           'Lightman et al. report that process supervision significantly outperformed outcome '
           'supervision on problems from the MATH dataset (arXiv:2305.20050).',
           'Stage 4 (Illustrative Numbers): The figures on this page are illustrative. A cubic '
           'count at n = 4,096 is 4,096³ = 6.87 × 10^10 operations; 14.8 is an assumed divisor '
           'that no theorem implies. A 20-step chain whose validity is the product of per-step '
           'probabilities gives 0.9566^20 ≈ 41.2% and 0.99723^20 ≈ 94.6%. None of these is a '
           'measured result.'],
 'readouts': [{'label': 'Assumed Speedup Divisor', 'value': '14.8× at n = 4,096 (assumed, illustrative)'},
              {'label': '20-Step Chain Validity (model)', 'value': '94.6% vs 41.2% (from assumed per-step probabilities 0.99723 and 0.9566)'},
              {'label': 'ETH Status (see M.01)', 'value': 'formal-math eth README states it refutes ETH (not checked here)'},
              {'label': 'Verification Status', 'value': 'nothing verified by this site'}],
 'sidenote_1': {'kicker': 'SIDENOTE M.06-A · SIAM DOI 10.1137/15M1024524',
                'body': "Williams's abstract describes a randomized algorithm that computes the "
                        'min-plus product, and so APSP, in time n^3/2^(Ω(log n)^(1/2)) on the real '
                        'RAM, where earlier algorithms took O(n^3/log^c n) for c ≤ 2. It uses '
                        'Razborov-Smolensky polynomials to reduce the product to rectangular '
                        'matrix products over F_2; a deterministic version runs in n^3/2^(log^δ n) '
                        'for some δ > 0.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.06-B · A LOOSE ANALOGY',
                'body': 'The folio compares pruning a search early with screening many candidate '
                        'sequences. This is an analogy only. Nothing here was run on a genome, and '
                        'nothing here is a method for designing guide RNAs.'},
 'skill': {'filename': 'fine-grained-prm-SKILL.md',
           'name': 'fine-grained-prm',
           'description': 'AI-agnostic skill for fine-grained complexity reductions (3SUM/APSP/OV) '
                          'and step-level process reward verification.',
           'rules': ['Do not present the n^3/2^(Ω(√log n)) APSP bound as a practical speedup: it is an '
                     'asymptotic result with an unspecified constant, and no speedup at a given n '
                     'follows from it.',
                     'Check each intermediate reasoning step with an exact checker where one '
                     'exists, and say when a step score is only a model estimate.',
                     'State fine-grained hypotheses (3SUM, APSP, SETH, ETH) as conjectures, and '
                     'report a claim that refutes one as the claim of its source, not as '
                     'established.']},
 'revisions': [{'edition': 'REV 1.2',
                'date': '2026-11-14',
                'summary': 'REV 1.2 (Redated 2026-11-14): Grounding revision. The speedup of '
                           '14.8x at n = 4,096, the validity figures 41.2% and 94.6%, and the '
                           'bound 2^(0.385 n) were presented as results; none follows from the '
                           'cited papers. The first two are now labeled as illustrative, with the '
                           'per-step probabilities that produce the validity figures stated, and '
                           'the third is removed. Williams (2018) is described as its abstract '
                           'does, as a randomized algorithm that uses rectangular matrix products '
                           '(the earlier text said it needs no fast matrix multiplication). The '
                           'opening scene of two researchers in Berkeley and Stanford, the '
                           "'QED verified' labels, the wrong DOI attached to an antisense "
                           'oligonucleotide, and the claim that the method prunes genome-wide '
                           'off-target edits in seconds are removed; the Cystic Fibrosis section '
                           'is shortened to a labeled analogy. The Alman and Vassilevska Williams '
                           'result is reported as a statement of the repository README and of '
                           'the preprint, which this site has not checked.',
                'opus': 'Review: DOIs checked in Crossref and the Scite index on 2026-11-14; the '
                        'Williams abstract and the Lightman et al. arXiv abstract were read, and '
                        'the Vassilevska Williams-Williams subcubic equivalences were checked '
                        'with Scite check_claim. Vassilevska Williams & Williams (DOI '
                        '10.1145/3186893), Gajentaan & Overmars (DOI '
                        '10.1016/0925-7721(95)00022-2) and Lightman et al. (arXiv:2305.20050) were '
                        'added to the source list.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-02',
                'summary': 'REV 1.1 (Redated 2026-11-02): Williams sub-cubic APSP '
                           'circuit polynomials and step-level PRM800K process reward supervision '
                           'with 4-Seat Frontier Council review. (REV 1.2: "certified" wording '
                           'withdrawn.)',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'exp(c √log n) sub-cubic divisor and step-level survival probability '
                        'prod_{k=1}^L p_k. (REV 1.2: "verified" wording withdrawn; the product '
                        'formula is a model, and the divisor has no stated constant.)'},
               {'edition': 'REV 1.0',
                'date': '2026-11-01',
                'summary': 'REV 1.0 (Published 2026-11-01): Initial 5-Act monograph uniting '
                           'Williams sub-cubic APSP circuit polynomials with step-level Process '
                           'Reward verification.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'exp(c √log n) sub-cubic divisor and step-level survival probability '
                        'prod_{k=1}^L p_k. (REV 1.2: "verified" wording withdrawn.)'}],
 'governing_law': 'O(n³ / 2^(Ω(√log n))) APSP (randomized) · Step-Level PRM',
 'volume': 3,
 'volume_code': 'VOL. 03',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1137/15M1024524',
           'fetched_on': '2026-11-08',
           'citing_publications': 148,
           'supporting': 0,
           'mentioning': 100,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Williams 2018 (DOI 10.1137/15M1024524), checked '
                      '2026-11-08: 148 citing publications (0 supporting, 100 mentioning, 0 '
                      'contrasting) and no retraction notice. These counts describe that one '
                      'paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1137/15M1024524',
           'fetched_on': '2026-11-08',
           'citing_publications': 148,
           'supporting': 0,
           'mentioning': 100,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Williams 2018 (DOI 10.1137/15M1024524), checked '
                      '2026-11-08: 148 citing publications (0 supporting, 100 mentioning, 0 '
                      'contrasting) and no retraction notice. These counts describe that one '
                      'paper, not this folio.'},
 'act1_title': 'Act I — The Quadratic Wall in Polynomial Time and the Rise of Fine-Grained '
               'Complexity',
 'act1_dropcap': 'In the early 1970s Stephen Cook and Richard Karp showed how to separate problems that can be solved in polynomial time from NP-complete ones, which are believed to need far more. Polynomial time is not always fast enough: an algorithm that takes cubic time on a graph with n nodes needs about n^3 steps. Fine-grained complexity asks which polynomial exponents can be improved. Its central conjectures concern 3SUM, All-Pairs Shortest Paths (APSP) and the Strong Exponential Time Hypothesis. In 2010 Virginia Vassilevska Williams and Ryan Williams showed that APSP is subcubic-equivalent to several other problems (published in the Journal of the ACM, 2018, DOI 10.1145/3186893), and in 2018 Ryan Williams published an algorithm that takes a factor 2^(Ω(√log n)) off the cubic running time for APSP.',
 'act1_plain_bridge': 'In plain words, this research is about the shortest route between every pair of towns in a large road network. Checking every possible connection one by one takes a number of steps that grows roughly with the cube of the number of towns, which becomes a problem for big networks. For a long time nobody knew how to do substantially better than a modest saving. Williams showed how to save a factor that grows slowly with the size of the network, and a recent repository README states a much larger polynomial improvement, which this site has not checked. This folio makes no claim about navigation apps, logistics or genetics.',
 'act1_body': "Ryan Williams's paper in the SIAM Journal on Computing (2018, DOI 10.1137/15M1024524) gives a randomized algorithm for the min-plus product, and so for APSP, that runs in time n^3/2^(Ω(√log n)) on the real RAM, where earlier algorithms took O(n^3/log^c n) for c ≤ 2. It applies Razborov-Smolensky polynomials to reduce the min-plus product to a relatively small number of rectangular matrix products over F_2, each computed by a method due to Coppersmith. The README of the repository anthropics/formal-math lists a 3sum-apsp project whose stated result, due to Alman and Vassilevska Williams (arXiv:2610.06783), is that 3SUM can be solved in O(n^1.9992) steps and APSP in O(n^2.99942) steps on integers of polynomial size; a later preprint by Chan (arXiv:2610.42012) refers to this result as announced by those authors. Both are reported statements: this site has not built the project or checked the proofs. Separately, Lightman et al. (arXiv:2305.20050) compare outcome supervision, which rewards only a final answer, with process supervision, which rewards each step, for models solving problems from the MATH dataset.",
 'act1_stakes': 'Fine-grained complexity ties the exact exponent of many problems to a few conjectures. Vassilevska Williams and Williams showed that APSP is subcubic-equivalent to several other problems (DOI 10.1145/3186893), and Gajentaan and Overmars showed that many problems in computational geometry are 3SUM-hard, meaning a truly subquadratic algorithm for any of them would give one for 3SUM (DOI 10.1016/0925-7721(95)00022-2). A statement that refutes one of these hypotheses is a very large claim and needs independent expert review. The folio sets this beside process supervision only as an analogy: in both cases a long chain is only as good as its steps.',
 'pullquote': 'A long chain is only as reliable as its steps: if each of 20 steps is valid with '
              'probability p, the whole chain is valid with probability p^20, which is why '
              'step-level scoring is attractive.',
 'chronology': [('1995',
                 'Gajentaan & Overmars introduce 3SUM-hardness in computational geometry '
                 '(DOI 10.1016/0925-7721(95)00022-2).'),
                ('2010',
                 'Virginia Vassilevska Williams & Ryan Williams show sub-cubic equivalences '
                 'around APSP and triangle detection (journal version DOI 10.1145/3186893).'),
                ('2018',
                 'Ryan Williams gives a randomized O(n^3 / 2^{Omega(sqrt(log n))}) algorithm for '
                 'APSP using Razborov–Smolensky polynomials (DOI 10.1137/15M1024524).'),
                ('2023',
                 'Lightman et al. report that process supervision significantly outperforms '
                 'outcome supervision on MATH problems (arXiv:2305.20050).'),
                ('2026',
                 'Alman & Vassilevska Williams, as listed in the formal-math README, state '
                 'O(n^1.9992) for 3SUM and O(n^2.99942) for APSP (arXiv:2610.06783); not checked '
                 'by this site.')],
 'act2_title': 'Act II — How It Actually Works: Razborov–Smolensky Polynomials + Step-Level PRM',
 'act2_analogy': 'Everyday analogy: Imagine planning connecting flights across four thousand regional airports during a holiday storm. If you inspect every single layover combination one by one, you must evaluate billions of possibilities, and your computer freezes. Instead, an experienced travel coordinator groups neighboring airports into regional hubs. By checking weather patterns across whole regional corridors at once, you rule out thousands of delayed connecting routes in a single pass, finding the fastest itinerary without getting overwhelmed.',
 'act2_plain_primer': 'To see how this batching shortcut works in practice, you can explore two intuitive control knobs. The first knob controls the grouping size, deciding how many regional cities or logical steps are bundled into each algebraic package. If you keep the grouping parameter at zero, the computer checks each connection individually, forcing the calculation into a slow, grinding crawl. But as you dial the grouping knob higher, the computer translates multiple comparisons into algebraic polynomials, evaluating hundreds of routes in parallel. The second knob measures constraint density, tracking how many overlapping rules or scheduling limits crowd into the network. When constraints are sparse, paths remain open and flexible. However, as constraint crowding approaches the critical boundary, conflict points multiply rapidly. The two knobs drive an illustration with assumed numbers; they are not measurements of any algorithm.',
 'distill_diagram': {'analogy_title': 'Regional Airport Hub Routing', 'analogy_sub': 'Batching regional hubs eliminates dominated layovers in one pass', 'force_a_title': 'Polynomial Block Degree (d_poly)', 'force_a_sub': 'Compresses comparison blocks into low-degree polynomial systems', 'force_b_title': 'Constraint Clause Density (alpha)', 'force_b_sub': 'Clause crowding ratio driving fine-grained hardness transitions', 'threshold_title': 'Sub-Cubic Circuit Complexity Barrier', 'threshold_pass': 'Illustrative: an assumed 14.8x divisor at n = 4,096; modeled 20-step validity 94.6%', 'threshold_fail': 'Naive cubic search needs 4,096^3 = 6.87e10 operations'},
 'act2_intuition': 'The classical Floyd–Warshall algorithm evaluates the min-plus distance product (A * B)_{ij} = min_k (A_{ik} + B_{kj}) across n vertices, using about n^3 comparisons. Ryan Williams applied Razborov–Smolensky polynomials to reduce the min-plus product to a relatively small number of rectangular matrix products over F_2 (SIAM Journal on Computing, DOI 10.1137/15M1024524), which gives a running time of n^3/2^(Ω(√log n)). That is an asymptotic statement with an unspecified constant, so it does not say what the speedup is at n = 4,096; the divisor 14.8 on this page is an assumed illustrative value. Separately, multi-step reasoning has an analogous issue: if each of 20 steps is valid independently with probability p, the whole chain is valid with probability p^20. With p = 0.9566 that is about 41.2%, and with p = 0.99723 about 94.6%. These are the two numbers the page shows; they come from the assumed per-step probabilities and are not measurements of any outcome-supervised or process-supervised model.',
 'act2_deepening': 'Fine-grained reductions tie together three conjectures: the 3SUM hypothesis, the All-Pairs Shortest Paths conjecture and the Strong Exponential Time Hypothesis. Under those conjectures, computing the min-plus matrix product was believed to need about n^3 operations up to sub-polynomial factors. Williams does not contradict that belief, since his saving is a factor of 2^(Ω(√log n)), which is smaller than any polynomial in n. The README of the 3sum-apsp project states a polynomial saving for APSP, which would contradict the APSP conjecture; this site has not checked that claim. The page\'s sliders are illustrative controls: they are not parameters of Williams\'s algorithm and they do not model the satisfiability threshold.',
 'walkthrough': ["Experiment 1 (Illustrative Divisor): With the assumed divisor 14.8, 6.87 × 10^10 "
                 'naive cubic operations at n = 4,096 become about 4.6 × 10^9. The divisor is not '
                 "implied by Williams's bound.",
                 'Experiment 2 (Chain Validity): With assumed per-step probabilities 0.9566 and '
                 '0.99723, a 20-step chain is valid with probability about 41.2% and 94.6% '
                 'respectively. These are model values, not measurements.',
                 'Experiment 3 (Sliders): Drag the complexity slider alpha to see the '
                 'illustration change; it is not a measurement of any algorithm.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification '
               'Bridge',
 'act4_human_ai': 'Models that propose proof steps can be scored step by step, and a proof assistant such as Lean 4 checks the steps it is given. The folio did not run either, and it does not claim that step-level scoring prevents errors in practice; Lightman et al. report an improvement on a math benchmark, nothing more. Mathlib (DOI 10.1145/3372885.3373824) is the community library Lean projects build on, and the anthropics/formal-math README lists a 3sum-apsp project whose statement this site has not checked.',
 'act4_deepening': 'In systems that combine a language model with a proof assistant, one could score the model\'s intermediate deductions before expanding the search. That is a possibility, not a description of a system the folio has tested. If experts verified the README statement of a polynomial saving for APSP, it would be a major result; that is not something this site can assess.',
 'cf_bridge': 'This bridge is an analogy the folio draws and nothing more. A study of prime '
              'editing for CF-causing CFTR variants in human organoids and airway cells exists '
              '(Cell Reports Medicine, DOI 10.1016/j.xcrm.2024.101544). The folio only borrows '
              'the general picture of screening many candidates and pruning early. It makes no '
              'claim about how guides are designed or about any speed, and nothing here is '
              'medical advice.',
 'sources': ['Williams, R. (2018). Faster All-Pairs Shortest Paths via Circuit Complexity. SIAM '
             'Journal on Computing, 47(5), 1965–1985. DOI: 10.1137/15M1024524.',
             'Williams, V. V., & Williams, R. R. (2018). Subcubic equivalences between '
             'path, matrix, and triangle problems. Journal of the ACM, 65(5). DOI: '
             '10.1145/3186893.',
             'Gajentaan, A., & Overmars, M. H. (1995). On a class of O(n²) problems in '
             'computational geometry. Computational Geometry, 5(3), 165–185. DOI: '
             '10.1016/0925-7721(95)00022-2.',
             'Alman, J., & Vassilevska Williams, V. (2026). Truly subquadratic 3SUM and truly '
             'subcubic APSP via triangles in sparse lopsided graphs. arXiv:2610.06783. Listed as '
             'the 3sum-apsp project in anthropics/formal-math '
             '(https://github.com/anthropics/formal-math); README read 2026-11-14. Not built or '
             'checked by this site. Referred to by Chan et al., arXiv:2610.42012.',
             "Lightman, H., et al. (2023). Let's verify step by step (PRM800K). arXiv:2305.20050.",
             'The mathlib Community (2020). The Lean mathematical library (CPP 2020), '
             '367–381. DOI: 10.1145/3372885.3373824.',
             'Bulcaen, M., et al. (2024). Prime editing functionally corrects cystic '
             'fibrosis-causing CFTR mutations in human organoids and airway epithelial cells. '
             'Cell Reports Medicine, 5(5), 101544. DOI: 10.1016/j.xcrm.2024.101544.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Sub-cubic APSP '
        'circuit reduction and step-level PRM tree pruning">\n'
        '            <line x1="60" y1="185" x2="620" y2="185" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <line x1="60" y1="25" x2="60" y2="185" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <path d="M 60 185 Q 240 165 440 28" fill="none" stroke="var(--tp-minium)" '
        'stroke-width="2.5" stroke-dasharray="5,4"/>\n'
        '            <path d="M 60 185 Q 280 172 580 92" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="3"/>\n'
        '            <circle cx="480" cy="116" r="6" fill="var(--tp-verdigris)"/>\n'
        '            <text x="275" y="42" font-size="11" fill="var(--tp-minium)">Naive '
        'Floyd-Warshall O(n^3) + Outcome-Only Search</text>\n'
        '            <text x="315" y="84" font-size="11" fill="var(--tp-verdigris)">Williams '
        'Sub-Cubic APSP + Step-Level PRM (assumed 14.8x, illustrative)</text>\n'
        '            <text x="210" y="204" font-size="11" fill="currentColor">Graph / Proof '
        'Horizon n (up to 4,096 Nodes · 94.6% modeled)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a pruned polynomial circuit tree revealing an '
        'illuminated shortest-path trajectory would look like (artistic impression, not a formal '
        'circuit diagram)',
 'caption': 'Conceptual Vision Plate M.06-V (Imagining What It Would Look Like) · Artistic '
            'geometric visualization imagining a hierarchical circuit tree where unverified '
            'branches are pruned away to leave a verified shortest path.'}

DISPATCH = {'kicker': 'FINE-GRAINED COMPLEXITY & PROCESS SUPERVISION · WILLIAMS APSP, A REPOSITORY STATEMENT, '
           'AND PRM800K · REPORTED, NOT CHECKED HERE',
 'headline': "Williams's APSP Algorithm, a Repository's Statement on 3SUM and APSP, and Step-Level "
             'Process Supervision',
 'body': "Ryan Williams's randomized All-Pairs Shortest Paths algorithm runs in time "
         "n^3 / 2^(Ω(√log n)) (SIAM J. Comput. DOI 10.1137/15M1024524). The README of "
         'anthropics/formal-math lists a 3sum-apsp project whose stated result, by Alman and '
         'Vassilevska Williams (arXiv:2610.06783), is a polynomial saving for 3SUM and APSP. '
         "Lightman et al. (PRM800K, arXiv:2305.20050) report that step-level process supervision "
         'outperformed outcome supervision on MATH problems. This site reports these results and '
         'has not checked the repository or the preprint.'}

META_3D = ('Williams (min,+) Tropical Matrix Shortcut Trough',
 'X: Source Vertex Index i · Z: Target Vertex Index j · Y: Sub-Cubic Shortest-Path Potential')

ES_TRANSLATION = {'title_es': 'Reducciones Subcúbicas de Grano Fino (3SUM → APSP) y Supervisión de Procesos Paso a '
             'Paso (PRM800K)',
 'subtitle_es': 'El algoritmo de Ryan Williams, basado en complejidad de circuitos, para Caminos '
                'Más Cortos entre Todos los Pares (APSP), lo que afirma el README de un '
                'repositorio sobre una mejora polinomial para APSP y 3SUM, y el artículo de '
                'supervisión por pasos de OpenAI. Las comparaciones con la búsqueda de pruebas o '
                'la genómica son analogías de este folio.',
 'why_es': 'En vez de verificar uno por uno todos los vuelos de conexión entre 4,000 aeropuertos '
           '(O(n³)), agrupas los centros regionales en paquetes algebraicos y descartas rutas '
           'dominadas en bloque.',
 'bridge_es': 'Es solo una analogía de este folio: existe un estudio de edición prime para '
              'variantes de CFTR que causan fibrosis quística en organoides humanos y células de '
              'las vías respiratorias (Cell Reports Medicine, DOI 10.1016/j.xcrm.2024.101544). '
              'El folio toma prestada únicamente la imagen general de examinar muchos candidatos '
              'y podar pronto. No afirma nada sobre cómo se diseñan las guías ni sobre ninguna '
              'velocidad, y nada de esto es consejo médico.',
 'plain_es': 'En palabras sencillas, esta investigación trata de la ruta más corta entre cada par de ciudades en una red grande de caminos. Revisar cada conexión posible una por una toma un número de pasos que crece aproximadamente con el cubo del número de ciudades, y eso se vuelve un problema en redes grandes. Durante mucho tiempo nadie supo cómo hacerlo sustancialmente mejor que con un ahorro modesto. Williams mostró cómo ahorrar un factor que crece lentamente con el tamaño de la red, y el README de un repositorio reciente afirma una mejora polinomial mucho mayor, que este sitio no ha revisado. Este folio no afirma nada sobre aplicaciones de navegación, logística ni genética.',
 'deep_es': 'La idea se comprende con dos ejemplos ilustrativos. El algoritmo aleatorizado de Ryan Williams para APSP corre en tiempo n^3 / 2^(Ω(√log n)); es un enunciado asintótico con una constante no especificada, así que no dice cuál es la aceleración con n = 4,096: el divisor 14.8 de esta página es un valor supuesto e ilustrativo. Por otro lado, si cada uno de 20 pasos es válido con probabilidad p, la cadena completa es válida con probabilidad p^20: con p = 0.9566 resulta cerca de 41.2 %, y con p = 0.99723, cerca de 94.6 %. Son valores del modelo, no mediciones. El README del proyecto 3sum-apsp afirma un ahorro polinomial para APSP, lo que contradiría la conjetura de APSP; este sitio no ha revisado esa afirmación. Los deslizadores son controles ilustrativos y no parámetros del algoritmo de Williams.'}
