#!/usr/bin/env python3
"""Folio M.13 (MATH): Shannon Zero-Error Graph Capacity, Lovasz Theta Sandwich & the Open C7 Gap."""
from __future__ import annotations

SLUG = 'm13'

PILLAR = 'math'

_SCITE = {
    'doi': '10.1109/TIT.1979.1055985',
    'fetched_on': '2026-11-21',
    'citing_publications': 1779,
    'supporting': 15,
    'mentioning': 1482,
    'contrasting': 0,
    'retracted': False,
    'summary': (
        'Scite Smart Citation Index entry for Lovasz 1979, "On the Shannon capacity of a graph" '
        '(IEEE Transactions on Information Theory, DOI 10.1109/TIT.1979.1055985), fetched 2026-11-21: '
        '1,779 citing publications (15 supporting, 1,482 mentioning, 0 contrasting) and zero retraction notices. '
        'These counts describe that foundational paper, not this folio.'
    ),
}

FOLIO = {
    'folio_id': 'M.13',
    'slug': 'm13',
    'pillar': 'math',
    'category_code': 'M',
    'parent_folios': ['M.03', 'M.06'],
    'lineage_mode': 'CONTINUATION · Extends M.03 Combinatorial Packing & M.06 Graph Complexity Bounds',
    'title': 'Shannon Zero-Error Graph Capacity, Lovász Theta Sandwich & the Open Seven-Cycle Gap',
    'subtitle': (
        'How Claude Shannon turned error-free messaging into packing squares on cyclic graphs, how László Lovász '
        'settled the five-cycle with a three-dimensional umbrella, why Willem Haemers separated geometric cones '
        'from capacity on twenty-seven lines, and why the seven-cycle limit stays open.'
    ),
    'date_published': '2026-11-21',
    'date_redated': '2026-11-21',
    'current_edition': 'REV 1.0',
    'status_badge': 'GRAPH CAPACITY · REV 1.0',
    'primary_kernel': 'skills/math/m13/verify_m13_shannon_capacity.py',
    'governing_law': 'α(G) ≤ Θ(G) ≤ ϑ(G) ≤ α*(G) ≤ χ̄(G) · ϑ(C_n) = n cos(π/n) / [1 + cos(π/n)]',
    'governing_law_latex': r"\alpha(G) \le \Theta(G) \le \vartheta(G) \le \alpha^*(G) \le \bar{\chi}(G), \\ \vartheta(C_n) = \frac{n \cos(\pi/n)}{1 + \cos(\pi/n)}",
    'colophon': {
        'identifier': 'M.13 · Zero-Error Capacity & Lovász Theta Sandwich · REV 1.0',
        'kernels': 'Shannon Strong Product G^k · Lovász Umbrella ϑ(G) · Haemers Minrank(S_bar) = 7',
        'benchmarks': (
            'C_5 (k = 2): α = 2 · Θ(C_5) = ϑ(C_5) = √5 ≈ 2.236068 · '
            'C_7 (k = 5): 367^(1/5) ≈ 3.257866 ≤ Θ(C_7) ≤ ϑ(C_7) ≈ 3.317667 (OPEN)'
        ),
        'bridge': 'Extends M.03/M.06 · Information-theoretic packing and spectral duality',
    },
    'sliders': [
        {
            'label': 'Odd Cycle Length (n)',
            'min': 5,
            'max': 13,
            'step': 2,
            'value': 5,
            'unit': 'n = ',
        },
        {
            'label': 'Codeword Block Length (k)',
            'min': 1,
            'max': 5,
            'step': 1,
            'value': 2,
            'unit': 'k = ',
        },
    ],
    'steps': [
        (
            'Stage 1 (Confusability Graphs and Strong Products, Shannon 1956): Claude Shannon '
            '(DOI 10.1109/TIT.1956.1056798) modeled a noisy discrete channel as a graph G whose vertices are '
            'input letters and whose edges connect pairs that can produce the same output. Zero-error words of '
            'length k form an independent set in the k-fold strong product G^k, yielding Θ(G) = sup_k α(G^k)^(1/k). '
            'For C_5, α(C_5) = 2, whereas the five pairs (i, 2i mod 5) form an independent set in C_5^2, giving Θ(C_5) ≥ √5.'
        ),
        (
            'Stage 2 (Lovász Orthonormal Umbrellas and Sandwich Inequality, 1979): László Lovász '
            '(DOI 10.1109/TIT.1979.1055985) defined ϑ(G) by placing unit vectors u_i in Euclidean space so '
            'non-adjacent vertices are orthogonal, minimizing max_i 1/(c · u_i)^2 over unit handles c. '
            'Because ϑ is multiplicative under strong products, α(G) ≤ Θ(G) ≤ ϑ(G) ≤ α*(G) ≤ χ̄(G). On odd cycles, '
            'ϑ(C_n) = n cos(π/n) / [1 + cos(π/n)], pinning Θ(C_5) = √5 ≈ 2.236068 via the 3D umbrella cos²φ = 1/√5.'
        ),
        (
            'Stage 3 (Haemers Minrank Separation on the Schläfli Complement, 1979): Willem Haemers '
            '(DOI 10.1109/TIT.1979.1056027) bounded Θ(G) above by the minimum rank of any matrix fitting G over a '
            'field. On the 27-line cubic-surface intersection graph S_bar = SRG(27, 10, 1, 5), spectrum {10^1, 1^20, (-5)^6} '
            'gives ϑ(S_bar) = 9, whereas A(S_bar) − I fits S_bar with exact rational rank 7. Thus Θ(S_bar) ≤ 7 < 9, '
            'and the diagonal in S ⊠ S_bar shows Θ(S ⊠ S_bar) ≥ 27 > 3 × 7 ≥ Θ(S) Θ(S_bar).'
        ),
        (
            'Stage 4 (Open Hypothesis on C_7, Tier T0–T1 Bounds, and Falsification Condition): For the seven-cycle '
            'C_7, Polak & Schrijver (2019, DOI 10.1016/j.ipl.2018.11.006) found 367 independent vertices in C_7^5, '
            'establishing Tier T0/T1 bounds 367^(1/5) ≈ 3.257866 ≤ Θ(C_7) ≤ ϑ(C_7) ≈ 3.317667. Whether Θ(C_7) equals '
            'ϑ(C_7) or stays strictly below it remains OPEN. Any strict algebraic upper bound below 3.317667 refutes '
            'equality Θ(C_7) = ϑ(C_7), while any block code with α(C_7^k)^(1/k) > 3.257866 tightens the lower floor.'
        ),
    ],
    'readouts': [
        {'label': 'Lovász Theta Upper Bound ϑ(C_n)', 'value': '2.236068 (closed Θ(C_5) = √5)'},
        {'label': 'Best Block-k Rate α(C_n^k)^(1/k)', 'value': '2.236068 at n = 5, k = 2'},
        {'label': 'Sandwich: α · ϑ · α* · χ̄', 'value': '2 ≤ 2.2361 ≤ 2.500 ≤ 3'},
        {'label': 'Open Capacity Gap ϑ − Rate', 'value': '0.000000 (CLOSED ON C_5)'},
    ],
    'spec_plate': {
        'division': 'COMBINATORIAL INFORMATION THEORY / SEMIDEFINITE BOUNDS',
        'title': 'Odd-Cycle Zero-Error Packing Envelope, Lovász Orthonormal Umbrella & Haemers Rank Bound',
        'body': (
            'Exact discrete mathematics verification over odd cycles C_5 through C_13, strong products C_5^2 and C_7^2, '
            'and the 27-vertex Schläfli complement SRG(27, 10, 1, 5). Lower bounds for C_7^5 (367 codewords) are cited '
            'from Polak & Schrijver (2019); all C_5^2, C_7^2, Gram PSD eigenvalues, and exact rational Gaussian-elimination '
            'rank-7 checks are recomputed from scratch by verify_m13_shannon_capacity.py.'
        ),
        'meta': (
            'Primary anchors: Shannon 1956 (DOI 10.1109/TIT.1956.1056798) · Lovász 1979 '
            '(DOI 10.1109/TIT.1979.1055985) · Haemers 1979 (DOI 10.1109/TIT.1979.1056027) · '
            'Polak & Schrijver 2019 (DOI 10.1016/j.ipl.2018.11.006)'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE M.13-A · POLYNOMIAL-TIME SDP VS. NP-HARD ALPHA',
        'body': (
            'Grötschel, Lovász & Schrijver (1981, DOI 10.1007/BF02579273) showed via the ellipsoid method that '
            'ϑ(G) can be approximated to arbitrary rational precision in polynomial time, even though both α(G) and χ̄(G) '
            'are NP-hard. Whenever α(G) = χ̄(G) (perfect graphs), the sandwich collapses to equality and yields both '
            'quantities in polynomial time.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE M.13-B · NON-ADDITIVITY UNDER DISJOINT UNION (ALON 1998)',
        'body': (
            'Shannon asked in 1956 whether the capacity of a disjoint union equals the sum Θ(G ⊔ H) = Θ(G) + Θ(H). '
            'Noga Alon (1998, DOI 10.1007/PL00009824) constructed graphs G and H for which Θ(G) and Θ(H) are '
            'bounded while Θ(G ⊔ H) grows far larger, demonstrating that block-coding across two separate channels '
            'can mix codewords more efficiently than either channel separately.'
        ),
    },
    'skill': {
        'filename': 'shannon-capacity-lovasz-theta-SKILL.md',
        'name': 'shannon-capacity-lovasz-theta',
        'description': (
            'AI-agnostic combinatorial information theory skill for Shannon zero-error graph capacity, '
            'the Lovasz theta sandwich alpha(G) <= Theta(G) <= vartheta(G) <= chi_bar(G), and Haemers minrank separation.'
        ),
        'rules': [
            (
                'Model zero-error k-symbol block codes as independent sets in the strong product G^{\boxtimes k}, '
                'never the Cartesian box product, so symbol confusability across simultaneous coordinates is captured.'
            ),
            (
                'Enforce the Lovasz sandwich alpha(G) <= Theta(G) <= vartheta(G) <= alpha*(G) <= chi_bar(G) and compute '
                'odd-cycle theta values via n * cos(pi/n) / (1 + cos(pi/n)).'
            ),
            (
                'Never treat vartheta(G) as equal to Theta(G) in general: check algebraic minrank bounds such as '
                'Haemers rank(A(S_bar) - I) = 7 < 9 = vartheta(S_bar) on the 27-vertex Schlafli complement.'
            ),
            (
                'Keep Theta(C_7) explicitly labeled OPEN between the verified lower floor 367^(1/5) (~3.257866) and '
                'the Lovasz upper bound vartheta(C_7) (~3.317667).'
            ),
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.0',
            'date': '2026-11-21',
            'summary': (
                'REV 1.0 (Published 2026-11-21): Volume VII Mathematics monograph continuing Folios M.03 & M.06 '
                'across Shannon (1956), Lovász (1979), Haemers (1979), Grötschel–Lovász–Schrijver (1981), Alon (1998), '
                'Bohman–Holzman (2003), and Polak–Schrijver (2019).'
            ),
            'opus': (
                'Verification note: all seven primary DOIs were checked against Crossref on 2026-11-21 with zero '
                'retraction notices; skills/math/m13/verify_m13_shannon_capacity.py recomputes odd-cycle bounds, '
                'the 3D C_5 umbrella, the 10-word C_7^2 packing, Gram PSD spectra, and exact rational rank 7 on the '
                '27-vertex Schläfli complement.'
            ),
        }
    ],
    'volume': 7,
    'volume_code': 'VOL. 07',
    'reading_time': '22 MIN READ',
    'word_count': '4,800 WORDS',
    'scite': dict(_SCITE),
}

LONGFORM_DATA = {
    'reading_time': '22 MIN READ',
    'word_count': '4,800 WORDS',
    'parent_folios': ['M.03', 'M.06'],
    'lineage_mode': 'CONTINUATION · Extends M.03 Combinatorial Packing & M.06 Graph Complexity Bounds',
    'scite': dict(_SCITE),
    'act1_title': 'Act I — Cool Fact & Human Story: Five Confusable Letters on a Pentagon Dial',
    'act1_dropcap': (
        'In autumn 1956, at Bell Laboratories in Murray Hill, Claude Shannon sketched a puzzle around a simple '
        'five-letter telegraph dial. Suppose five symbols sit in a ring, and transmission blurs each letter into '
        'its two nearest neighbors. If you send one letter at a time, at most two symbols remain completely safe from '
        'confusion. Pairing two letters might seem able to double those safe choices from two to '
        'four. Yet Shannon noticed five two-letter pairs that stay mutually distinct even under neighbor blur. That '
        'single extra message raised the zero-error rate above two per use. For twenty-three years, nobody knew '
        'whether longer blocks could beat the square root of five, or how to place an upper ceiling on the ring. '
        'Today that same gap still blocks mathematicians on a seven-letter dial, where the true limit remains unsolved.'
    ),
    'act1_plain_bridge': (
        'In plain words, imagine a noisy channel where each sent letter can arrive slightly shifted to the letter '
        'next door. When you want zero mistakes, you must skip neighbors and pick letters that do not overlap at '
        'the receiver. On a five-letter circle, picking single letters gives only two safe choices. Pairing two '
        'letters into short words opens diagonal corners on a twenty-five-cell grid. Five coded pairs stay cleanly '
        'separated instead of four. That extra fifth pair raises the average safe rate per letter above two. In '
        '1979, mathematician László Lovász built a geometric cone of vectors that placed a firm upper ceiling on '
        'error-free word packing. His cone matched the five-pair code and settled the five-letter ring. Yet on a '
        'seven-letter ring, a narrow gap remains between the best computer-found codebooks and that upper ceiling.'
    ),
    'act1_body': (
        'Shannon formalized this packing problem in his 1956 paper on zero-error capacity '
        '(DOI 10.1109/TIT.1956.1056798). Two input symbols share an edge in the confusability graph whenever a '
        'channel can turn both into the same received output. Sending blocks of length k without error means '
        'picking vertices in the k-fold strong product graph so that no two chosen words differ only by confusable '
        'neighbors in every slot. On the five-cycle, pairing two slots lifts the maximum safe set from two to five '
        'words. Two decades later, László Lovász (1979, DOI 10.1109/TIT.1979.1055985) constructed an orthonormal '
        'cone representation in Euclidean space that squeezed the five-cycle capacity between the five-pair code '
        'and an identical geometric ceiling.'
    ),
    'act1_stakes': (
        'That geometric ceiling looked so clean that Lovász wondered whether his theta function might equal zero-error '
        'capacity on every graph, and whether capacity always multiplied across separate graphs. Months later, '
        'Willem Haemers (1979, DOI 10.1109/TIT.1979.1056027) answered both questions negatively using an algebraic '
        'matrix rank bound on twenty-seven lines of a cubic surface. Grötschel, Lovász, and Schrijver (1981, '
        'DOI 10.1007/BF02579273) later showed that Lovász theta can be computed in polynomial time by the ellipsoid '
        'method, even while exact independence and capacity stay computationally intractable. Meanwhile, Bohman and '
        'Holzman (2003, DOI 10.1109/TIT.2002.808128) raised lower bounds on the complements of odd cycles, while '
        'Vesel and Žerovnik (2002, DOI 10.1016/S0020-0190(01)00229-0) and Polak and Schrijver (2019, '
        'DOI 10.1016/j.ipl.2018.11.006) pushed up the lower bound on the seven-cycle without reaching Lovász theta.'
    ),
    'pullquote': (
        '"Pairing two blurred letters turns a five-point ring into five clear pairs—yet on a seven-point ring, '
        'sixty-plus years of combinatorics have not closed the gap between known codes and Lovász\'s cone."'
    ),
    'chronology': [
        (
            '1956',
            'Claude Shannon defines zero-error channel capacity via strong graph products and exhibits the five-word '
            'two-letter code on the five-cycle (DOI 10.1109/TIT.1956.1056798).'
        ),
        (
            '1979',
            'László Lovász introduces the semidefinite theta function to establish the exact capacity of the five-cycle '
            '(DOI 10.1109/TIT.1979.1055985); Willem Haemers separates capacity from theta on the twenty-seven-vertex '
            'Schläfli complement using matrix rank (DOI 10.1109/TIT.1979.1056027).'
        ),
        (
            '1981',
            'Martin Grötschel, László Lovász, and Alexander Schrijver show that Lovász theta is computable in '
            'polynomial time via the ellipsoid method (DOI 10.1007/BF02579273).'
        ),
        (
            '1998',
            'Noga Alon demonstrates that zero-error capacity is not additive under disjoint union of graphs '
            '(DOI 10.1007/PL00009824).'
        ),
        (
            '2002–2003',
            'Aleksander Vesel and Janez Žerovnik find thirty-three independent words in the third power and one '
            'hundred eight in the fourth power of the seven-cycle (DOI 10.1016/S0020-0190(01)00229-0); Tom Bohman and '
            'Ron Holzman establish nontrivial lower bounds for odd-cycle complements (DOI 10.1109/TIT.2002.808128).'
        ),
        (
            '2019',
            'Sven Polak and Alexander Schrijver locate an independent set of three hundred sixty-seven codewords in the '
            'fifth strong power of the seven-cycle (DOI 10.1016/j.ipl.2018.11.006).'
        ),
    ],
    'act2_title': 'Act II — Cross-Field Intuition: The Round Dinner Table, the Umbrella Cone & Matrix Rank',
    'act2_analogy': (
        'Everyday analogy: Picture five dinner guests seated around a circular table where anyone speaking drowns '
        'out their left and right neighbors. On a single round, at most two guests sitting across the table can speak '
        'at once. Now imagine holding two simultaneous rounds where every pair of guests sends a joint signal: by '
        'diagonalizing who speaks in round one and round two, five distinct pairs can transmit without ever placing '
        'neighbors together in both rounds. Where the picture stops: discrete table seating lives on finite integer '
        'grids that explode exponentially with block length, whereas Lovász\'s umbrella spreads vectors in continuous '
        'Euclidean space and Haemers\'s bound counts linear dependencies over a field.'
    ),
    'act2_plain_primer': (
        'Our interactive combinatorics workbench exposes two discrete parameters of Shannon\'s odd-cycle problem. '
        'The first slider selects Odd Cycle Length from five to thirteen vertices, letting you step from the solved '
        'five-cycle onto the open seven-cycle and longer rings. Moving it updates the single-letter independence '
        'floor, the fractional packing ceiling, the clique cover, and Lovász\'s spectral bound simultaneously. The '
        'second slider chooses Codeword Block Length from one to five symbols, tracking how pairing and blocking '
        'codewords push the achievable zero-error rate per symbol upward toward the geometric cone ceiling.'
    ),
    'distill_diagram': {
        'analogy_title': 'Five Guests on Two Simultaneous Rounds',
        'analogy_sub': 'Diagonalizing pairs escapes single-round neighbor collisions (2 per round vs 5 per pair)',
        'force_a_title': 'Strong-Product Packing α(G^k)^(1/k)',
        'force_a_sub': 'Combinatorial lower bound climbing via multi-letter block codes (367 on C_7^5)',
        'force_b_title': 'Lovász Umbrella & Haemers Rank',
        'force_b_sub': 'Continuous semidefinite cone ceiling vs discrete finite-field matrix rank ceiling',
        'threshold_title': 'Capacity Sandwich Closure vs Open Gap',
        'threshold_pass': 'C_5 closed: √5 lower code matches ϑ(C_5) cone at 2.236068',
        'threshold_fail': 'C_7 open: 3.257866 lower code stays strictly below 3.317667 cone ceiling',
    },
    'act2_intuition': (
        'To build Lovász\'s sandwich α(G) ≤ Θ(G) ≤ ϑ(G) ≤ α*(G) ≤ χ̄(G), assign each vertex i a unit vector '
        'u_i ∈ ℝ^d such that u_i · u_j = 0 whenever i and j are non-adjacent in G. Choose a unit handle vector c '
        'and define ϑ(G) = min_{c, {u_i}} max_i 1 / (c · u_i)². Because orthogonal vectors in any independent set S '
        'satisfy ∑_{i ∈ S} (c · u_i)² ≤ ‖c‖² = 1, the maximum term is at least 1/|S|, forcing ϑ(G) ≥ α(G). Moreover, '
        'taking tensor products u_i ⊗ v_j preserves orthogonality on non-edges of G ⊠ H, making ϑ multiplicative: '
        'ϑ(G ⊠ H) = ϑ(G) ϑ(H), so α(G^k)^(1/k) ≤ ϑ(G) for every block length k. On C_5, tilting five vectors into '
        'ℝ³ at cos²φ = 1/√5 makes non-neighbors orthogonal and locks ϑ(C_5) = √5 ≈ 2.236068.'
    ),
    'act2_deepening': (
        'For general odd cycles C_n (n ≥ 5), Lovász (1979, Theorem 9) evaluated the spectral bound directly from '
        'the eigenvalues λ_m = 2 cos(2πm/n) of the adjacency matrix A(C_n). Since λ_min = −2 cos(π/n) on a k = 2 '
        'regular edge-transitive cycle, ϑ(C_n) = −n λ_min / (2 − λ_min) = n cos(π/n) / [1 + cos(π/n)]. Equivalently, '
        'the circulant matrix M = I + A(C_n) / [2 cos(π/n)] has unit diagonal, vanishes on all non-edges, and has '
        'non-negative eigenvalues 1 + cos(2πm/n) / cos(π/n) ≥ 0, giving an explicit positive-semidefinite Gram '
        'factorization. Yet Haemers (1979) showed ϑ(G) is not tight everywhere: on the 27-vertex intersection graph '
        'S_bar = SRG(27, 10, 1, 5) of the 27 lines on a smooth cubic surface, eigenvalues {10¹, 1²⁰, (−5)⁶} give '
        'ϑ(S_bar) = 9, while B = A(S_bar) − I fits S_bar with diagonal −1 and exact rational rank 27 − 20 = 7, '
        'forcing Θ(S_bar) ≤ 7 < 9 and Θ(S ⊠ S_bar) ≥ 27 > 3 × 7 ≥ Θ(S) Θ(S_bar).'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Closure on the Five-Cycle C_5): Set Odd Cycle Length n = 5 and move Block Length k from '
            'k = 1 to k = 2. Watch the achievable rate jump from α(C_5) = 2.000000 to √5 = 2.236068, collapsing the '
            'open gap against ϑ(C_5) = 2.236068 to zero.'
        ),
        (
            'Experiment 2 (The Open Seven-Cycle Gap on C_7): Switch Odd Cycle Length to n = 7 and raise Block Length '
            'from k = 1 (rate 3.000000) through k = 2 (√10 ≈ 3.162278) up to k = 5 (367^(1/5) ≈ 3.257866 from Polak & '
            'Schrijver 2019). Observe the remaining 0.059801 gap below ϑ(C_7) = 3.317667.'
        ),
        (
            'Experiment 3 (Asymptotic Sandwich on Higher Odd Cycles): Step n to 9, 11, and 13 to compare α = (n−1)/2, '
            'our verified square-power packings (18 on C_9^2, 26 on C_11^2, 38 on C_13^2), ϑ(C_n), and α* = n/2, '
            'alongside the explicit rank-7 Haemers separation on the 27-vertex Schläfli complement checked offline by '
            'verify_m13_shannon_capacity.py.'
        ),
    ],
    'act4_title': 'Act IV — Imagining Humanity\'s Future: Error-Free Coding, Semidefinite Relaxations & Open Frontiers',
    'act4_human_ai': (
        'Zero-error capacity sits at the quiet crossroads of information theory, semidefinite optimization, and '
        'extremal combinatorics. Lovász\'s umbrella relaxation turned a hopelessly exponential block-packing limit '
        'into a convex geometry problem solvable in polynomial time, inspiring modern semidefinite hierarchies in '
        'combinatorial optimization and quantum nonlocality. Yet Haemers\'s 27-vertex rank barrier and Alon\'s '
        'non-additivity theorem remind researchers that no single relaxation captures every algebraic obstruction '
        'inside finite-block discrete codes.'
    ),
    'act4_deepening': (
        'Under the Tier T0–T1 evidence framing of this folio, the inequalities α(C_5) < ϑ(C_5) = Θ(C_5) = √5, '
        '367^(1/5) ≈ 3.257866 ≤ Θ(C_7) ≤ ϑ(C_7) ≈ 3.317667, and Θ(S_bar) ≤ 7 < 9 = ϑ(S_bar) rest on published '
        'theorems and deterministic rational/floating-point verification. The exact asymptotic value of Θ(C_7) '
        'remains an explicit OPEN mathematical problem. Any future proof exhibiting an algebraic or sum-of-squares '
        'upper bound strictly below 3.317667 would refute Θ(C_7) = ϑ(C_7), while any larger independent set in a '
        'strong power C_7^k exceeding rate 3.257866 would narrow the interval from below. The offline verifier '
        'enforces a planted-defect shift (i, i) in C_5^2 and an edge flip in S_bar so broken packings or spectra '
        'always fail.'
    ),
    'cf_bridge': 'Extends M.03/M.06 · Information-theoretic packing and spectral duality',
    'sources': [
        (
            'Shannon, C. E. (1956). The zero error capacity of a noisy channel. '
            'IRE Transactions on Information Theory, 2(3), 8–19. DOI: 10.1109/TIT.1956.1056798.'
        ),
        (
            'Lovász, L. (1979). On the Shannon capacity of a graph. '
            'IEEE Transactions on Information Theory, 25(1), 1–7. DOI: 10.1109/TIT.1979.1055985.'
        ),
        (
            'Haemers, W. (1979). On some problems of Lovász concerning the Shannon capacity of a graph. '
            'IEEE Transactions on Information Theory, 25(2), 231–232. DOI: 10.1109/TIT.1979.1056027.'
        ),
        (
            'Grötschel, M., Lovász, L., & Schrijver, A. (1981). The ellipsoid method and its consequences in '
            'combinatorial optimization. Combinatorica, 1(2), 169–197. DOI: 10.1007/BF02579273.'
        ),
        (
            'Alon, N. (1998). The Shannon capacity of a union. '
            'Combinatorica, 18(3), 301–310. DOI: 10.1007/PL00009824.'
        ),
        (
            'Vesel, A., & Žerovnik, J. (2002). Improved lower bound on the Shannon capacity of C7. '
            'Information Processing Letters, 81(5), 277–282. DOI: 10.1016/S0020-0190(01)00229-0.'
        ),
        (
            'Bohman, T., & Holzman, R. (2003). A nontrivial lower bound on the Shannon capacities of the complements '
            'of odd cycles. IEEE Transactions on Information Theory, 49(3), 721–722. DOI: 10.1109/TIT.2002.808128.'
        ),
        (
            'Polak, S. C., & Schrijver, A. (2019). New lower bound on the Shannon capacity of C7 from circular graphs. '
            'Information Processing Letters, 143, 37–40. DOI: 10.1016/j.ipl.2018.11.006.'
        ),
        (
            'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and '
            'classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
            '882–898. DOI: 10.1162/qss_a_00146.'
        ),
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Shannon capacity sandwich comparing '
        'odd cycles C_5 through C_13, the closed C_5 root-5 intersection, and the open C_7 gap">\n'
        '            <line x1="48" y1="184" x2="352" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <line x1="48" y1="30" x2="48" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <text x="54" y="22" font-size="10.5" font-weight="600" fill="currentColor">Odd-Cycle Sandwich α(C_n) ≤ Θ ≤ ϑ(C_n)</text>\n'
        '            <path d="M 62 152 L 136 126 L 210 98 L 284 72 L 344 50" fill="none" stroke="var(--tp-prussian)" stroke-width="2.4"/>\n'
        '            <path d="M 62 152 L 136 128 L 210 105 L 284 82 L 344 62" fill="none" stroke="var(--tp-verdigris)" stroke-width="2" stroke-dasharray="5,3"/>\n'
        '            <circle id="tp-svg-math-point" cx="62" cy="152" r="6" fill="var(--tp-verdigris)"/>\n'
        '            <text x="72" y="168" font-size="9" fill="var(--tp-prussian)">C_5 closed at √5 ≈ 2.2361</text>\n'
        '            <text x="152" y="138" font-size="9" fill="var(--tp-minium)">C_7 open gap [3.2579, 3.3177]</text>\n'
        '            <line x1="372" y1="24" x2="372" y2="192" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="388" y="22" font-size="10.5" font-weight="600" fill="currentColor">Verified Bounds &amp; Separations</text>\n'
        '            <rect x="388" y="42" width="256" height="58" rx="6" fill="var(--tp-stone)" fill-opacity="0.28" stroke="var(--tp-prussian)" stroke-width="1.6"/>\n'
        '            <text x="400" y="64" font-size="9.5" font-weight="600" fill="var(--tp-prussian)">C_5^2 Packing: 5 words → Θ(C_5) = √5</text>\n'
        '            <text x="400" y="84" font-size="9" fill="var(--tp-verdigris)">C_7^5 Packing: 367 → ≥ 3.2579 (&lt; 3.3177)</text>\n'
        '            <rect x="388" y="114" width="256" height="56" rx="6" fill="var(--tp-verdigris)" fill-opacity="0.12" stroke="var(--tp-verdigris)" stroke-width="1.4"/>\n'
        '            <text x="400" y="136" font-size="9.5" font-weight="600" fill="var(--tp-prussian)">Schläfli S_bar: ϑ = 9, rank(A−I) = 7</text>\n'
        '            <text x="400" y="156" font-size="9" fill="var(--tp-minium)">Θ(S ⊠ S_bar) ≥ 27 &gt; 3 × 7 (Haemers 1979)</text>\n'
        '            <text x="48" y="206" font-size="10" fill="var(--tp-verdigris)">Recomputed offline by verify_m13_shannon_capacity.py</text>\n'
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining a brushed-brass pentagon ring with five turned ivory pegs resting on '
        'cream vellum beside an upward-radiating brass geometric umbrella-rib apparatus on a bronze bearing handle '
        'over dark slate (artistic impression, not a measured physical apparatus)'
    ),
    'caption': (
        'Conceptual Vision Plate M.13-V (Imagining What It Would Look Like) · Artistic tabletop view imagining '
        'Shannon\'s five-vertex confusability pentagon beside Lovász\'s geometric umbrella cone. Exact sandwich bounds '
        'and the 27-vertex Schläfli rank check are kept in Plate M.13-A and verify_m13_shannon_capacity.py below.'
    ),
}

DISPATCH = {
    'kicker': 'FRONTIER COMBINATORIAL INFORMATION DISPATCH · SHANNON CAPACITY & SEMIDEFINITE BOUNDS',
    'headline': 'Lovász\'s Theta Sandwich, Haemers\'s Rank Barrier & the Open Seven-Cycle Capacity Gap',
    'body': (
        'Pairing two symbols lets five error-free codewords pack into a five-cycle, closing Θ(C_5) = √5 via Lovász\'s '
        '1979 orthonormal umbrella (DOI 10.1109/TIT.1979.1055985). Yet Haemers\'s rank-7 bound on the 27-vertex '
        'Schläfli complement (DOI 10.1109/TIT.1979.1056027) separates capacity from theta, and on C_7 the gap '
        '[3.257866, 3.317667] (Polak & Schrijver 2019, DOI 10.1016/j.ipl.2018.11.006) stays open.'
    ),
}

META_3D = (
    'Odd-Cycle Zero-Error Capacity & Lovász Theta Sandwich Manifold',
    'X: Odd Cycle Length n · Z: Block Length k · Y: Achievable Rate α(C_n^k)^(1/k) vs ϑ(C_n)',
)

ES_TRANSLATION = {
    'title_es': 'Capacidad de Error Cero de Shannon, Acotación Theta de Lovász y la Brecha Abierta en C_7',
    'subtitle_es': (
        'Cómo Claude Shannon convirtió la mensajería sin errores en empaquetamientos sobre grafos cíclicos, cómo '
        'László Lovász cerró el ciclo de cinco vértices con un paraguas tridimensional, por qué Willem Haemers '
        'separó el cono geométrico mediante rango matricial en veintisiete rectas y por qué el límite del ciclo de '
        'siete sigue abierto.'
    ),
    'why_es': (
        'Emparejar dos letras borrosas permite transmitir cinco palabras sin error sobre un anillo de cinco símbolos '
        'donde antes solo cabían dos; no obstante, en un anillo de siete símbolos la brecha exacta sigue abierta.'
    ),
    'plain_es': (
        'En palabras sencillas, imaginen un canal ruidoso donde cada letra enviada puede confundirse con sus letras '
        'vecinas. Si desean transmitir sin un solo error, deben evitar vecinos contiguos. En un círculo de cinco '
        'letras, elegir letras sueltas permite apenas dos señales seguras. Al enviar pares de letras como palabras '
        'cortas, aparecen esquinas diagonales en una cuadrícula de veinticinco casillas. Cinco pares codificados '
        'quedan bien separados en lugar de cuatro. Ese quinto par eleva la tasa segura promedio por letra arriba de '
        'dos. En 1979, el matemático László Lovász construyó un cono geométrico de vectores que fijó un techo '
        'superior para empaquetar palabras sin error. Su cono igualó el código de cinco pares y cerró el anillo de '
        'cinco letras. No obstante, en un anillo de siete letras persiste una pequeña brecha entre los mejores '
        'códigos hallados por computadora y ese techo superior.'
    ),
    'deep_es': (
        'En el modelo de Shannon (1956, DOI 10.1109/TIT.1956.1056798), las palabras de longitud k sin error forman '
        'un conjunto independiente en el producto fuerte G^k, definiendo Θ(G) = sup_k α(G^k)^(1/k). Lovász (1979, '
        'DOI 10.1109/TIT.1979.1055985) estableció el sándwich α(G) ≤ Θ(G) ≤ ϑ(G) ≤ α*(G) ≤ χ̄(G) y obtuvo para '
        'ciclos impares ϑ(C_n) = n cos(π/n) / [1 + cos(π/n)], cerrando Θ(C_5) = √5 ≈ 2.236068 mediante el conjunto '
        'de cinco pares {(i, 2i mod 5)} en C_5^2. En C_7, nuestro verificador comprueba diez palabras en C_7^2 '
        '(√10 ≈ 3.162278), mientras que Polak y Schrijver (2019, DOI 10.1016/j.ipl.2018.11.006) hallaron 367 '
        'palabras en C_7^5, fijando las cotas de nivel T0–T1 3.257866 ≤ Θ(C_7) ≤ 3.317667 (estado ABIERTO). '
        'Además, Haemers (1979, DOI 10.1109/TIT.1979.1056027) construyó el complemento del grafo de Schläfli '
        'SRG(27, 10, 1, 5) con ϑ(S_bar) = 9 pero rango racional exacto rank(A(S_bar) − I) = 7, refutando que '
        'Θ iguale siempre a ϑ y mostrando Θ(S ⊠ S_bar) ≥ 27 > 21 ≥ Θ(S) Θ(S_bar). Cualquier cota algebraica '
        'estrictamente menor que 3.317667 refutaría la igualdad Θ(C_7) = ϑ(C_7).'
    ),
    'bridge_es': (
        'Extiende M.03 y M.06 al límite de error cero de Shannon: cierra C_5 en √5, separa Schläfli mediante rango 7 '
        'y deja explícita la brecha abierta en C_7.'
    ),
}
