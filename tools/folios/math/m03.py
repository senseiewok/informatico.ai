#!/usr/bin/env python3
"""Folio M.03 (MATH): Extremal Cap Sets in F_3^n, Polynomial Method Upper Bounds, and Rank-48 Matrix Tensors."""
from __future__ import annotations

SLUG = 'm03'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.03',
 'slug': 'm03',
 'pillar': 'math',
 'category_code': 'M',
 'title': 'Extremal Cap Sets in F_3^n, Polynomial Method Upper Bounds, and Rank-48 Matrix Tensors',
 'subtitle': 'What two published Google DeepMind systems report about large cap sets in F_3^8 '
             '(FunSearch: a set of 512 points) and about multiplying 4×4 complex matrices with 48 '
             'scalar multiplications (AlphaEvolve). Any link to biology is an analogy.',
 'date_published': '2026-10-29',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.4',
 'status_badge': 'REDATED REV 1.4',
 'primary_kernel': 'tools/discovery/frontier_ai_math_catalog.py',
 'colophon': {'identifier': 'M.03 · Extremal Combinatorics & Tensors',
              'kernels': 'FunSearch Cap Set (512 in F_3^8) · AlphaEvolve 48 products',
              'benchmarks': 'Ellenberg-Gijswijt o(2.756^n) · 512^(1/8) = 2.1810 (products)',
              'bridge': 'Line-free sets ↔ constrained sequence design (analogy only)'},
 'sliders': [{'label': 'Affine Dimension n in F_3^n (3 ≤ n ≤ 8)',
              'min': 3,
              'max': 8,
              'step': 1,
              'value': 8,
              'unit': 'n = '},
             {'label': 'Tensor Border Rank Target (4×4 Matrix Multiplication)',
              'min': 46,
              'max': 49,
              'step': 1,
              'value': 48,
              'unit': 'rank = '}],
 'steps': ['Stage 1 (Affine Line-Free Constraint): A subset S ⊂ F_3^n is a Cap Set if no three '
           'distinct vectors x, y, z ∈ S satisfy x + y + z = 0 (mod 3).',
           'Stage 2 (Croot-Lev-Pach & Ellenberg-Gijswijt Polynomial Method): The polynomial '
           'method bounds the size of a cap set in F_3^n by o(2.756^n) (Ellenberg-Gijswijt, '
           'Corollary 5).',
           'Stage 3 (FunSearch Priority-Function Discovery): Romera-Paredes et al. report an '
           'evolutionary search over Python priority functions that found a 512-point cap set '
           'in F_3^8.',
           "Stage 4 (AlphaEvolve 48-Product Procedure): The AlphaEvolve white paper reports a "
           "procedure for 4×4 complex matrices with 48 scalar multiplications, against the 49 "
           "that Strassen's 1969 method gives when applied twice (7² = 49)."],
 'readouts': [{'label': 'F_3^8 Cap Set Size', 'value': '512 vectors (reported by FunSearch paper)'},
              {'label': 'Ellenberg-Gijswijt Base', 'value': 'o(2.756^n) upper bound (Corollary 5)'},
              {'label': '4×4 Matrix Multiplication Products', 'value': '48 < 49 (reported by AlphaEvolve, complex field)'},
              {'label': 'Exponent if used recursively', 'value': 'log_4(48) = 2.7925 (vs log_2(7) = 2.8074)'}],
 'sidenote_1': {'kicker': 'SIDENOTE M.03-A · NATURE DOI 10.1038/s41586-023-06924-6',
                'body': 'The Nature paper reports that FunSearch searches for programs that '
                        'describe how to build a solution rather than for the solution itself, '
                        'and that such programs tend to be more interpretable than raw solutions. '
                        'Its Figure 4b shows the priority function that yields a cap set of 512 '
                        'points in dimension 8.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.03-B · A LOOSE ANALOGY',
                'body': 'Choosing a sequence that avoids forbidden patterns can be compared in '
                        'spirit with building a cap set, which avoids a forbidden pattern of '
                        'three points. The folio draws that comparison only as an analogy. It '
                        'names no real design method, and nothing here is medical advice.'},
 'skill': {'filename': 'extremal-capset-tensor-rank-SKILL.md',
           'name': 'extremal-capset-tensor-rank',
           'description': 'AI-agnostic extremal combinatorics and algebraic complexity skill for '
                          'F_3^n Cap Sets, slice-rank polynomial upper bounds, and bilinear matrix '
                          'multiplication tensor decompositions.',
           'rules': ['Check cap set three-term progression avoidance exactly: for all distinct x, y, z in '
                     'S subset F_3^n, x + y + z != 0 (mod 3).',
                     'Quote the Ellenberg-Gijswijt bound as |S| = o(2.756^n) (their Corollary 5); '
                     'the constant is the minimum over 0 < x < 1 of (1 + x + x^2)/x^(2/3), about '
                     '2.7551. Report the FunSearch F_3^8 size, 512, as the paper reports it.',
                     'Verify bilinear tensor decomposition sum_{r=1}^R (u_r . A)(v_r . B) w_r = A '
                     'B exactly satisfies all n^6 Brent equations.']},
 'revisions': [{'edition': 'REV 1.4',
                'date': '2026-11-14',
                'summary': 'REV 1.4 (Redated 2026-11-14): Grounding revision. The bound on cap '
                           "sets is now quoted as the paper states it, o(2.756^n) (Ellenberg and "
                           "Gijswijt, Corollary 5), instead of '3 · (2.755104)^n', and the "
                           'formula for the constant is corrected. The opening scene about the '
                           'invention of the card game SET is replaced by the fact that the 81 '
                           'cards are the points of F_3^4, with Pellegrino 1970 for the maximum of '
                           '20. The 2.1810^n figure is labelled as what products of the 512-point '
                           'set give, not as a proved floor, and the configuration count is '
                           'corrected to about 10^779. The AlphaEvolve result is cited to its '
                           'white paper (arXiv:2506.13131) and reported as a reported result. The '
                           'claim that these methods inform CFTR mRNA design, and the reference to '
                           'Lean files in anthropics/formal-math, are removed; the Cystic Fibrosis '
                           'link is now a labelled analogy.',
                'opus': 'Review: DOIs checked in Crossref and the Scite index on 2026-11-14; the '
                        'Ellenberg-Gijswijt statement and the 512-point FunSearch result were read '
                        'in the papers through Scite full-text excerpts, and the AlphaEvolve '
                        'abstract was read on arXiv. Pellegrino (1970) and Croot, Lev & Pach (2017) '
                        'were added to the source list.'},
               {'edition': 'REV 1.3',
                'date': '2026-11-06',
                'summary': 'REV 1.3 (Redated 2026-11-06): Expanded extremal combinatorics '
                           'benchmark with a pure O-sequence h-vector log-concavity check (h_k^2 >= h_{k-1}*h_{k+1} up to degree d = 7; earlier editions credited a DeepMind \'AlphaProof Nexus\' Science paper for which no resolvable source was found), Gemini Deep Think IMO 2025 Gold (35/42), and FirstProof '
                           '(10/10 research problems). (REV 1.4: the log-concavity check and the '
                           'IMO 2025 and FirstProof figures have no source in this folio and are '
                           'withdrawn.)',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Gemma 4 31B + Ornith 1.5 '
                        '35B): Verified small-case pure O-sequence log-concavity circuit breaker '
                        '(d <= 7), FunSearch 512-cap invariant, and AlphaEvolve Rank-48 tensor '
                        'exponent. (REV 1.4: this "verified" wording is withdrawn.)'},
               {'edition': 'REV 1.2',
                'date': '2026-11-02',
                'summary': 'REV 1.2 (Redated 2026-11-02): Re-verified Ellenberg-Gijswijt '
                           'slice-rank cap set upper bound (2.7551^n, DOI '
                           '10.4007/annals.2017.185.1.8), FunSearch F_3^8 lower bound (>= 512, DOI '
                           '10.1038/s41586-023-06924-6), and AlphaEvolve Rank-48 4x4 matrix tensor '
                           'decomposition with 4-Seat Frontier Council review.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'slice-rank base 2.755104, F_3^8 512-cap line-free invariant, and '
                        'log_4(48) = 2.7925 tensor exponent. (REV 1.4: "verified" wording '
                        'withdrawn; the base 2.7551 is a number the folio computed, and the paper '
                        'states o(2.756^n).)'},
               {'edition': 'REV 1.1',
                'date': '2026-11-01',
                'summary': 'REV 1.1 (Redated 2026-11-01): Added AlphaEvolve rank-48 4×4 matrix '
                           'tensor verification alongside FunSearch F_3^8 cap set bounds.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'log_4(48) = 2.79248 < log_2(7) = 2.80735 asymptotic exponent '
                        'improvement. (REV 1.4: arithmetic confirmed; "verified" wording '
                        'withdrawn.)'},
               {'edition': 'REV 1.0',
                'date': '2026-10-29',
                'summary': 'REV 1.0 (Published 2026-10-29): Initial publication of F_3^8 Cap Set '
                           'and Ellenberg-Gijswijt slice-rank monograph.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'exact known cap set sizes for n=3 (9), n=4 (20), n=5 (45), n=6 (112). '
                        '(REV 1.4: "verified" wording withdrawn; only n = 4 (20) is cited in this '
                        'edition.)'}],
 'governing_law': 'FunSearch Cap Set (512 in F_3^8) · AlphaEvolve 48 products',
 'volume': 2,
 'volume_code': 'VOL. 02',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1038/s41586-023-06924-6',
           'fetched_on': '2026-11-08',
           'citing_publications': 797,
           'supporting': 0,
           'mentioning': 349,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Romera-Paredes et al. 2023 (DOI '
                      '10.1038/s41586-023-06924-6), checked 2026-11-08: 797 citing publications '
                      '(0 supporting, 349 mentioning, 0 contrasting) and no retraction notice. '
                      'These counts describe that one paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'act1_dropcap': 'The cap set problem asks for the largest set of points in F_3^n, the n-fold product of the integers modulo 3, that contains no three distinct points x, y, z with x + y + z = 0, which in this space means no line. In four dimensions the 81 points correspond to the cards of the game SET, and the largest cap there has 20 points, a result of Giuseppe Pellegrino (1970). How large a cap can be as the dimension grows stayed open for decades and is one of the well-known questions of additive combinatorics.',
 'act1_plain_bridge': 'In plain words, the cap set problem asks how many items you can put together before an unwanted pattern becomes unavoidable. Imagine choosing cards from the game SET so that no three of them form a matching trio; the more cards you choose, the harder it is to avoid one. Mathematicians wanted to know how fast that crowding effect grows as the number of dimensions increases. Questions of this kind are studied in additive combinatorics and are related to coding theory, but this folio does not claim that the results discussed here improve any real communication system.',
 'act1_body': "In 2016, Ernie Croot, Vsevolod Lev and Péter Pál Pach introduced a polynomial method that bounds progression-free sets in (Z/4Z)^n (DOI 10.4007/annals.2017.185.1.7), and Jordan Ellenberg and Dion Gijswijt extended it to F_q^n, showing in particular that a cap set in F_3^n has size o(2.756^n) (Annals of Mathematics, DOI 10.4007/annals.2017.185.1.8). In December 2023, Romera-Paredes and colleagues at Google DeepMind reported FunSearch in Nature (DOI 10.1038/s41586-023-06924-6): a procedure that pairs a pretrained large language model with an evaluator, searches for programs rather than for solutions, and in dimension 8 found a cap set of 512 points, larger than the one previously known. The AlphaEvolve white paper from the same group (arXiv:2506.13131) reports a procedure for multiplying two 4×4 complex-valued matrices with 48 scalar multiplications, which it describes as the first improvement in 56 years over Strassen's algorithm in that setting.",
 'act1_stakes': 'FunSearch and AlphaEvolve are examples of combining a language model that proposes programs with an automatic evaluator that checks them. In the cap set case the evaluator can test exactly whether a proposed set contains a line, so an invalid candidate is rejected whatever the model says. The FunSearch paper also reports that the programs it finds tend to be more interpretable than raw solutions, which lets people study them. The folio does not claim that this approach carries over to other problems; that is an empirical question each case answers for itself.',
 'pullquote': 'FunSearch searches for the program that builds a cap set rather than for the set '
              'itself, and its authors report that such programs tend to be easier to interpret '
              'than raw solutions.',
 'pullquote_cite': 'Editorial Synthesis · Romera-Paredes et al., Nature (2023) & AlphaEvolve '
                   '(2025)',
 'chronology': [('1969',
                 'Volker Strassen',
                 'Discovers 2x2 matrix multiplication in 7 scalar multiplications (49 for 4x4 via '
                 '2-level recursion).'),
                ('1970',
                 'Giuseppe Pellegrino',
                 'Shows the maximum cap in F_3^4 (the game SET) has exactly 20 points.'),
                ('2016',
                 'Croot-Lev-Pach & Ellenberg-Gijswijt',
                 'Polynomial method: a cap set in F_3^n has size o(2.756^n) (Ellenberg-Gijswijt, '
                 'Corollary 5).'),
                ('2023',
                 'Google DeepMind FunSearch',
                 'Romera-Paredes et al. (2023) report a 512-point cap set in F_3^8 (DOI: '
                 '10.1038/s41586-023-06924-6) found by evolving Python priority functions.'),
                ('2025',
                 'Google DeepMind AlphaEvolve',
                 'Reports a procedure for 4x4 complex matrix multiplication with 48 scalar '
                 'multiplications (48 < 49) (arXiv:2506.13131).')],
 'act2_analogy': 'Everyday analogy: Imagine planting a grove of young apple trees in an orchard so that no three trees ever form a straight line, no matter which direction you look. If you place saplings haphazardly, you quickly find that almost every open spot lines up with two existing trees. Instead of wandering randomly with a shovel, you invent a clever rule of thumb—like placing trees near curved stone mounds—that systematically deflects lines of sight and leaves the orchard open and sunlit.',
 'act2_plain_primer': 'To see how algorithmic search conquers this orchard puzzle, you can adjust two intuitive control knobs. The first knob controls the dimension of the orchard, expanding the playing field from a modest garden patch to an eight-dimensional grid containing thousands of possible planting spots. As the dimension grows, the total number of locations multiplies rapidly, creating a dizzying maze where accidental lines threaten to form in every direction. The second knob sets the target efficiency for matrix operations, challenging the computer to multiply complex arrays using fewer elementary calculations than traditional textbooks require. Strassen showed in 1969 that fewer multiplications than the textbook method are possible. The two sliders are independent; they do not drive each other. A search like FunSearch tests many candidate priority recipes and keeps only those that assemble large collections of points without forming a line, which illustrates how a heuristic search can get around an exhaustive one.',
 'distill_diagram': {'analogy_title': 'Orchard Non-Collinear Saplings', 'analogy_sub': 'Planting saplings so no three ever align into a straight sightline', 'force_a_title': 'Affine Dimension in F_3^n (n)', 'force_a_sub': 'Expands finite vector space from 27 points up to 6,561 locations', 'force_b_title': 'Tensor Multiplication Target', 'force_b_sub': 'Reduces bilinear multiplications below Strassen recursive rank', 'threshold_title': 'Slice-Rank vs Greedy Frontier', 'threshold_pass': 'FunSearch 512-cap in F_3^8 and AlphaEvolve 48 products, as reported', 'threshold_fail': 'Exhaustive coordinate search faces about 10^779 candidate sets'},
 'act2_intuition': 'Why is searching directly for a 512-point cap set inside the eight-dimensional space F_3^8 completely impossible with brute force? Because the number of candidate subsets of size 512 among the 6,561 points is the binomial coefficient C(6561, 512), about 10^779—a quantity dwarfing the 10^80 elementary particles in the observable universe. Any raw coordinate permutation search drowns instantly in combinatorial noise. FunSearch resolved this barrier by shifting search from raw coordinates into the space of executable programs (Nature, DOI 10.1038/s41586-023-06924-6). The language model evolves compact Python priority functions that evaluate each vector, while a deterministic greedy kernel selects candidate points only if they never complete an arithmetic progression x + y + z = 0 (mod 3). Separately, Ellenberg and Gijswijt established an upper ceiling via the polynomial method, proving |S| = o(2.756^n) (Annals of Mathematics, DOI 10.4007/annals.2017.185.1.8). Their paper also quotes a best known lower bound of around 2.2^n for the growth rate, from before FunSearch. For comparison, the 512-point set alone gives, by taking products of copies of it, a growth rate of at least 512^(1/8) ≈ 2.181 per dimension; this is the folio\'s own arithmetic and not a figure from the paper.',
 'act2_deepening': "Classical arithmetic needs 64 scalar multiplications for a product of two four-by-four matrices. Strassen's 1969 method uses seven multiplications for two-by-two blocks, so applying it twice gives 7 × 7 = 49 products. The AlphaEvolve white paper reports a procedure with 48 products over the complex numbers. Writing matrix multiplication as a three-dimensional tensor, such a procedure is a decomposition of that tensor into 48 rank-one terms, described by factor matrices U, V and W. The two sliders on this page are independent: the cap set dimension and the tensor target do not drive one another, and any link between cap sets and tensor decompositions is the folio's loose comparison, not a result.",
 'walkthrough': ['Experiment 1 (Compare Upper & Lower Figures): Step through Stages 1 -> 4 to see '
                 'the polynomial-method ceiling o(2.756^n) beside the 512-point set; products of '
                 'that set give a growth rate of at least 512^(1/8) = 2.1810 per dimension, which '
                 'is the folio\'s own arithmetic.',
                 'Experiment 2 (Inspect the 48-Product Procedure): Examine the SVG '
                 'comparison plate below showing 4x4 multiplication with 64 products (textbook) '
                 '-> 49 (Strassen 1969, applied twice) -> 48 (AlphaEvolve, complex field). If such '
                 'a procedure could be applied recursively, the exponent would be '
                 'log_4(48) = 2.7925.',
                 'Experiment 3 (Download the Combinatorial Search Skill): Copy the AI-agnostic '
                 'SKILL.md below to enforce program-space priority search and polynomial '
                 'slice-rank bounds in your own coding agents.'],
 'act4_human_ai': 'A program is easier to read than a table of 512 vectors. The FunSearch paper reports that the programs it discovers tend to be more interpretable than raw solutions, and that this lets domain experts give feedback. This folio did not run FunSearch, AlphaEvolve, PySR or any formal verification; PySR (arXiv:2305.01582) and Mathlib (DOI 10.1145/3372885.3373824) are listed as tools a reader might look at.',
 'act4_deepening': "A workflow one could try: a language model proposes scoring programs, an exact checker rejects invalid sets, and people read the best programs for structure. That describes the method the FunSearch paper reports; it is not a claim that the method works on other problems. Open questions in this area, such as the best growth rate of cap sets, remain open.",
 'cf_bridge': 'This bridge is an analogy the folio draws and nothing more. Choosing a sequence '
              'that avoids certain forbidden patterns can be compared in spirit with building a '
              'cap set, which avoids a forbidden pattern of three points. The comparison is '
              'loose: it is not an isomorphism, it names no real design method, and nothing '
              'here is medical advice.',
 'sources': ['Ellenberg, J. S., & Gijswijt, D. (2017). On large subsets of F_q^n with no '
             'three-term arithmetic progression. Annals of Mathematics, 185(1), 339–343. DOI: '
             '10.4007/annals.2017.185.1.8.',
             'Croot, E., Lev, V. F., & Pach, P. P. (2017). Progression-free sets in Z_4^n are '
             'exponentially small. Annals of Mathematics, 185(1), 331–337. DOI: '
             '10.4007/annals.2017.185.1.7.',
             'Romera-Paredes, B., et al. (2023). Mathematical discoveries from program search with '
             'large language models (FunSearch). Nature, 625, 468–475. DOI: '
             '10.1038/s41586-023-06924-6.',
             'Strassen, V. (1969). Gaussian elimination is not optimal. Numerische Mathematik, '
             '13(4), 354–356. DOI: 10.1007/BF02165411.',
             'Pellegrino, G. (1970). Sul massimo ordine delle calotte in S_{4,3}. Le Matematiche '
             '(Catania), 25. No DOI; cited as [Pel70] for the maximum cap of 20 points in AG(4,3) '
             'in Kable & Mills, arXiv:2604.26989, found through Scite on 2026-11-14.',
             'Novikov, A., et al. (2025). AlphaEvolve: A coding agent for scientific and '
             'algorithmic discovery. arXiv:2506.13131. Earlier editions also cited an AlphaProof '
             'item and Lean files (CrystalSystem, CayleyDickson, Bki, PrimeOrder) in '
             'anthropics/formal-math; none were found in the repository README and the '
             'reference is withdrawn.',
             'Cranmer, M. (2023). Interpretable machine learning for science with PySR and '
             'SymbolicRegression.jl (MilesCranmer/PySR, https://github.com/MilesCranmer/PySR). '
             'DOI: 10.48550/arXiv.2305.01582.',
             'The mathlib Community (2020). The Lean mathematical library. Proceedings of the '
             '9th ACM SIGPLAN International Conference on Certified Programs and Proofs (CPP '
             '2020), 367–381. DOI: 10.1145/3372885.3373824.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Cap Set asymptotic '
        'corridor and AlphaEvolve Rank-48 tensor bound">\n'
        '            <rect x="60" y="38" width="250" height="145" fill="none" '
        'stroke="currentColor" stroke-opacity="0.3"/>\n'
        '            <line x1="80" y1="160" x2="290" y2="62" stroke="var(--tp-minium)" '
        'stroke-width="2.5" stroke-dasharray="5,4"/>\n'
        '            <line x1="80" y1="160" x2="290" y2="108" stroke="var(--tp-verdigris)" '
        'stroke-width="3"/>\n'
        '            <text x="75" y="56" font-size="11" fill="var(--tp-minium)">Ellenberg-Gijswijt '
        'Upper: o(2.756^n)</text>\n'
        '            <text x="75" y="146" font-size="11" fill="var(--tp-verdigris)">FunSearch '
        'n = 8: 512 (products: 2.1810^n)</text>\n'
        '            <rect x="360" y="38" width="270" height="145" fill="none" '
        'stroke="currentColor" stroke-opacity="0.3"/>\n'
        '            <rect x="390" y="65" width="48" height="100" fill="currentColor" '
        'fill-opacity="0.2"/>\n'
        '            <rect x="470" y="88" width="48" height="77" fill="var(--tp-prussian)" '
        'fill-opacity="0.65"/>\n'
        '            <rect x="550" y="91" width="48" height="74" fill="var(--tp-verdigris)"/>\n'
        '            <text x="386" y="60" font-size="11" fill="currentColor">Naive: 64</text>\n'
        '            <text x="460" y="82" font-size="11" fill="var(--tp-prussian)">Strassen: '
        '49</text>\n'
        '            <text x="535" y="84" font-size="11" fill="var(--tp-verdigris)">AlphaEvolve: '
        '48</text>\n'
        '          </svg>',
 'scite': {'doi': '10.1038/s41586-023-06924-6',
           'fetched_on': '2026-11-08',
           'citing_publications': 797,
           'supporting': 0,
           'mentioning': 349,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Romera-Paredes et al. 2023 (DOI '
                      '10.1038/s41586-023-06924-6), checked 2026-11-08: 797 citing publications '
                      '(0 supporting, 349 mentioning, 0 contrasting) and no retraction notice. '
                      'These counts describe that one paper, not this folio.'},
 'word_count': '4,650 WORDS'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what an extremal line-free F_3^n Cap Set affine '
        'lattice paired with a 4x4 Rank-48 bilinear matrix multiplication tensor cube would look '
        'like (artistic impression, not a formal plot)',
 'caption': 'Conceptual Vision Plate M.03-V (Imagining What It Would Look Like) · Artistic '
            'geometric visualization imagining an extremal non-collinear Cap Set lattice in F_3^n '
            '(|S| >= 512) beside an AlphaEvolve Rank-48 bilinear matrix tensor decomposition cube.'}

DISPATCH = {'kicker': 'REPORTED RESULTS · DEEPMIND FUNSEARCH CAP SETS & ALPHAEVOLVE 48-PRODUCT MATRIX '
           'MULTIPLICATION',
 'headline': 'FunSearch Reports a 512-Point Cap Set in F_3^8; AlphaEvolve Reports 48 Products for '
             '4x4 Complex Matrices',
 'body': "In Nature (Romera-Paredes et al. DOI 10.1038/s41586-023-06924-6), DeepMind's FunSearch "
         'paired an LLM with an evaluator and reports a cap set of 512 points in F_3^8. '
         'Ellenberg and Gijswijt (Annals of Math. DOI 10.4007/annals.2017.185.1.8) bound cap sets '
         'in F_3^n by o(2.756^n). The AlphaEvolve white paper (arXiv:2506.13131) reports a '
         'procedure for 4x4 complex matrix multiplication with 48 scalar multiplications. This '
         'site reports these results and did not reproduce them.'}

META_3D = ('FunSearch Cap-Set F_3^n Combinatorial Plateaus',
 'X/Z: Affine Finite-Field Hyperplane Grid · Y: Non-Collinear Cap-Set Indicator & Tensor Rank')

ES_TRANSLATION = {'title_es': 'Conjuntos Cap Extremales en F_3^n, Cotas del Método Polinomial y Tensores '
             'Matriciales de Rango 48',
 'subtitle_es': 'Lo que reportan dos sistemas publicados de Google DeepMind sobre conjuntos cap '
                'grandes en F_3^8 (FunSearch: un conjunto de 512 puntos) y sobre la '
                'multiplicación de matrices complejas 4×4 con 48 productos escalares '
                '(AlphaEvolve). Cualquier vínculo con la biología es una analogía.',
 'why_es': 'En lugar de buscar a ciegas entre billones de puntos sueltos, FunSearch evoluciona '
           'pequeños programas en Python que califican qué puntos elegir, y un verificador exacto '
           'conserva sólo las construcciones válidas.',
 'bridge_es': 'Es solo una analogía de este folio: elegir una secuencia que evite ciertos patrones '
              'prohibidos se puede comparar, en espíritu, con construir un conjunto cap, que evita '
              'un patrón prohibido de tres puntos. La comparación es vaga, no nombra ningún método '
              'de diseño real y nada de esto es consejo médico.',
 'plain_es': 'En palabras sencillas, el problema del conjunto cap plantea un reto muy intuitivo: ¿cuántos objetos podemos reunir sin que un patrón no deseado se vuelva inevitable? Imaginen que eligen cartas del juego SET de modo que ningún trío forme una combinación válida; entre más cartas eligen, más difícil es evitarla. Los matemáticos querían saber con qué rapidez crece ese efecto de aglomeración al aumentar el número de dimensiones. Las preguntas de este tipo se estudian en la combinatoria aditiva y se relacionan con la teoría de códigos, pero este folio no afirma que los resultados aquí tratados mejoren ningún sistema de comunicación real.',
 'deep_es': 'Para analizar este tema, conviene observar que los dos deslizadores son independientes: la dimensión del espacio afín y la meta de multiplicaciones para matrices de cuatro por cuatro no se influyen entre sí. Al elevar la dimensión hacia ocho, el número de subconjuntos de 512 puntos entre los 6,561 puntos es del orden de 10^779, mucho mayor que el número de átomos del universo observable, así que una búsqueda exhaustiva no es viable. El artículo de FunSearch reporta que, en lugar de buscar el conjunto directamente, se busca un programa que lo construya, y que esos programas suelen ser más interpretables. Ellenberg y Gijswijt acotan los conjuntos cap en F_3^n por o(2.756^n). Para matrices de cuatro por cuatro, el método de Strassen de 1969, aplicado dos veces, usa 49 productos; el documento técnico de AlphaEvolve reporta un procedimiento con 48 productos sobre los números complejos. Este sitio reporta esos resultados y no los reprodujo.'}
