#!/usr/bin/env python3
"""Folio M.15 (MATH): Diagonal Ramsey Numbers, Paley P(17), Erdos Random Floors & Book Bounds."""
from __future__ import annotations

SLUG = 'm15'

PILLAR = 'math'

_SCITE = {
    'doi': '10.1112/plms/s2-30.1.264',
    'fetched_on': '2026-11-21',
    'citing_publications': 2255,
    'supporting': 4,
    'mentioning': 845,
    'contrasting': 0,
    'retracted': False,
    'summary': (
        'Scite Smart Citation Index entry for Ramsey 1930, "On a Problem of Formal Logic" '
        '(Proceedings of the London Mathematical Society, DOI 10.1112/plms/s2-30.1.264), fetched 2026-11-21: '
        '2,255 citing publications (4 supporting, 845 mentioning, 0 contrasting) and no retraction notice. '
        'These counts describe that foundational paper, not this folio.'
    ),
}

FOLIO = {
    'folio_id': 'M.15',
    'slug': 'm15',
    'pillar': 'math',
    'category_code': 'M',
    'parent_folios': ['M.03', 'M.13'],
    'lineage_mode': 'CONTINUATION · Extends M.03 Extremal Combinatorics & M.13 Graph Packing Bounds',
    'title': 'Diagonal Ramsey Numbers: Paley Colorings, Erdős Random Floors, the Book Algorithm & Open Gaps',
    'subtitle': (
        'How Frank Ramsey uncovered unavoidable order inside colored graphs, how Paul Erdős launched probabilistic '
        'combinatorics in three pages, why seventeen quadratic residues settle four-cliques while five-cliques sit '
        'between forty-three and forty-six, and how an asymmetric book algorithm broke the base-four ceiling.'
    ),
    'date_published': '2026-11-21',
    'date_redated': '2026-11-21',
    'current_edition': 'REV 1.0',
    'status_badge': 'RAMSEY EXTREMAL BOUNDS · REV 1.0',
    'primary_kernel': 'skills/math/m15/verify_m15_ramsey_bounds.py',
    'governing_law': (
        'E[X_k(n, p)] = C(n, k)[p^C(k,2) + (1 − p)^C(k,2)] · '
        '√2 ≤ lim inf R(k,k)^(1/k) ≤ lim sup R(k,k)^(1/k) ≤ 4 − ε'
    ),
    'colophon': {
        'identifier': 'M.15 · Diagonal Ramsey Numbers & Book Bounds · REV 1.0',
        'kernels': 'Goodman K_6 Multiplicity · Paley P(17) over F_17 · Rational First-Moment Union Bound',
        'benchmarks': (
            'R(3, 3) = 6 (1,760 extremal K_6 colorings at 2 triangles) · R(4, 4) = 18 via P(17) · '
            '43 ≤ R(5, 5) ≤ 46 (OPEN) · n_1(5, 0.50) = 11 vs C(8, 4) = 70'
        ),
        'bridge': 'Extends M.03/M.13 · Probabilistic existence, algebraic pseudorandomness and asymmetric density boosting',
    },
    'sliders': [
        {
            'label': 'Clique Target Size (k)',
            'min': 3,
            'max': 10,
            'step': 1,
            'value': 5,
            'unit': 'k = ',
        },
        {
            'label': 'Red Edge Density (p)',
            'min': 0.20,
            'max': 0.80,
            'step': 0.05,
            'value': 0.50,
            'unit': 'p = ',
        },
    ],
    'steps': [
        (
            'Stage 1 (Small Settled Thresholds and Goodman Multiplicity, 1930–1959): Frank Ramsey '
            '(1930, DOI 10.1112/plms/s2-30.1.264) showed that every two-coloring of a large enough complete graph '
            'contains a monochromatic k-clique. On five vertices, a red pentagon C_5 and its blue pentagram complement avoid '
            'monochromatic triangles, whereas on K_6 Goodman’s degree identity (1959, DOI 10.1080/00029890.1959.11989408) '
            'gives T_mono = 20 − (1/2)∑ d_r(v)(5 − d_r(v)) ≥ 2 across all 32,768 colorings (attained 1,760 times), '
            'pinning R(3, 3) = 6. On eight vertices, the circulant step set {1, 4, 7} avoids red K_3 and blue K_4, while '
            'forced 3-regularity on K_9 gives odd degree sum 9 × 3 = 27, pinning R(3, 4) = 9.'
        ),
        (
            'Stage 2 (Quadratic Residues on F_17 and the Open Five-Clique Window, 1955–2026): Greenwood and Gleason '
            '(1955, DOI 10.4153/CJM-1955-001-4) colored K_17 by connecting u and v in red whenever (v − u) mod 17 lies '
            'in the quadratic residue set {1, 2, 4, 8, 9, 13, 15, 16}. Multiplication by non-residue 3 mod 17 swaps red '
            'and blue edges, yielding strongly regular Paley graph P(17) = SRG(17, 8, 3, 4) with zero monochromatic K_4 '
            'across all 2,380 four-subsets; combining with R(4, 4) ≤ R(3, 4) + R(4, 3) = 18 settles R(4, 4) = 18. By '
            'contrast, R(5, 5) stays open between 43 (Exoo 1989, DOI 10.1002/jgt.3190130113) and 46 (Angeltveit & McKay '
            '2026, DOI 10.1002/jgt.70029).'
        ),
        (
            'Stage 3 (Erdős First-Moment Floor, Convexity at p = 1/2, and Spencer’s Local Lemma, 1947–1975): Paul Erdős '
            '(1947, DOI 10.1090/S0002-9904-1947-08785-1) counted colorings at p = 1/2; this folio extends the same count to a general red probability p, giving '
            'expected monochromatic k-cliques E[X_k(n, p)] = C(n, k)[p^C(k,2) + (1 − p)^C(k,2)]. Whenever E[X_k(n, p)] < 1, '
            'at least one coloring avoids monochromatic K_k, so R(k, k) ≥ n_1(k, p) + 1. Convexity of p^m + (1 − p)^m '
            'minimizes E[X_k] at p = 0.50, yielding asymptotic base √2 ≈ 1.414214; Joel Spencer (1975, '
            'DOI 10.1016/0097-3165(75)90071-0) doubled the prefactor to (1 + o(1)) (√2/e) k 2^(k/2) via the Lovász Local Lemma.'
        ),
        (
            'Stage 4 (Asymmetric Book Algorithm, Tier T0–T1 Hypothesis, and Falsification Conditions, 1988–2026): '
            'Thomason (1988, DOI 10.1002/jgt.3190120406), Conlon (2009, DOI 10.4007/annals.2009.170.941), and Sah (2023, '
            'DOI 10.1215/00127094-2022-0048) shaved sub-exponential factors off Erdős–Szekeres C(2k − 2, k − 1) < 4^k. '
            'Campos, Griffiths, Morris, and Sahasrabudhe (2026, DOI 10.4007/annals.2026.203.3.4) achieved an exponential '
            'reduction R(k, k) ≤ (4 − ε)^k for a constant ε > 0 via an asymmetric book algorithm. Hypothesis (Tier T0–T1): '
            'skewing p off 0.50 drops n_1(k, p) for every k ≥ 5 (from 100 at p = 0.50 to 71 at p = 0.45 and 17 at p = 0.20 '
            'when k = 10), yet finite algebraic colorings beat n_1 + 1 at k = 3, 4, 5 while leaving both R(5, 5) ∈ [43, 46] '
            'and whether lim R(k, k)^(1/k) exists inside [√2, 4 − ε] open. Any 43-vertex (K_5, K_5)-free coloring refutes '
            'R(5, 5) = 43; any family exceeding base √2 narrows the asymptotic gap from below.'
        ),
    ],
    'readouts': [
        {'label': 'First-Moment Floor n_1(k, p) + 1', 'value': 'R(5, 5) ≥ 12 (n_1 = 11, E = 0.902344)'},
        {'label': 'Binomial Ceiling & LLL Scale', 'value': 'C(8, 4) = 70 · Spencer LLL scale 14.72'},
        {'label': 'Published Finite / Book Bracket', 'value': '43 ≤ R(5, 5) ≤ 46 (Exoo 1989; Angeltveit–McKay 2026)'},
        {'label': 'Threshold Status & Open Horizon', 'value': 'OPEN FINITE WINDOW [43, 46] · BASE [√2, 4 − ε]'},
    ],
    'spec_plate': {
        'division': 'EXTREMAL & PROBABILISTIC COMBINATORICS / RAMSEY MULTIPLICITY & DENSITY',
        'title': 'Exhaustive K_6 Goodman Check, Paley P(17) over F_17 & Rational First-Moment Thresholds',
        'body': (
            'Scope boundary: verify_m15_ramsey_bounds.py recomputes offline from scratch all 32,768 two-colorings of K_6 '
            '(minimum 2 monochromatic triangles across 1,760 colorings), the Z_8 circulant {1, 4, 7} witness for R(3, 4) > 8, all 2,380 four-subsets of Paley P(17) for R(4, 4) > 17 (the matching upper bounds are the classical degree arguments, restated and not machine-checked), and rational Fraction union '
            'bounds across k ∈ [3..10] and p ∈ [0.20..0.80]. The computer-assisted bounds R(5, 5) ≥ 43 (Exoo 1989), '
            'R(5, 5) ≤ 46 (Angeltveit & McKay 2026), and R(k, k) ≤ (4 − ε)^k (Campos et al. 2026) are reported from '
            'those published papers and are not re-derived by this script.'
        ),
        'meta': (
            'Primary anchors: Ramsey 1930 (DOI 10.1112/plms/s2-30.1.264) · Erdős 1947 '
            '(DOI 10.1090/S0002-9904-1947-08785-1) · Greenwood & Gleason 1955 (DOI 10.4153/CJM-1955-001-4) · '
            'Campos, Griffiths, Morris & Sahasrabudhe 2026 (DOI 10.4007/annals.2026.203.3.4) · '
            'Angeltveit & McKay 2026 (DOI 10.1002/jgt.70029)'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE M.15-A · WHY INTEGER PLATEAUS APPEAR AT k = 3 AND k = 4',
        'body': (
            'Although the continuous expectation E[X_k(n, p)] = C(n, k)[p^m + (1 − p)^m] attains a strict minimum at '
            'p = 0.50 for every k ≥ 3 and n ≥ k, its integer cutoff n_1(k, p) = max{n : E[X_k(n, p)] < 1} rounds down '
            'to whole vertices. At k = 3, E[X_3(4, 0.50)] = 4 × (1/8 + 1/8) = 1, so strict inequality < 1 holds only up '
            'to n_1 = 3 across the entire slider interval [0.20, 0.80]; at k = 4, n_1 = 6 stays flat across [0.40, 0.60]. '
            'From k = 5 through k = 10, the 0.05 step grid resolves a single peak at p = 0.50.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE M.15-B · PALEY QUADRATIC RESIDUES STOP AT FOUR-CLIQUES',
        'body': (
            'Paley graphs P(q) on prime powers q ≡ 1 (mod 4) look statistically random in edge density and eigenvalue '
            'spread, and P(17) reaches the sharp threshold 17 = R(4, 4) − 1. Yet Paley constructions do not settle '
            'R(5, 5): on prime q = 37, P(37) avoids monochromatic 5-cliques yet falls below Exoo’s 42-vertex coloring '
            '(1989, DOI 10.1002/jgt.3190130113), while on prime q = 41, P(41) already contains monochromatic 5-cliques, '
            'illustrating how subtle local correlations separate explicit algebraic graphs from uniform random colorings.'
        ),
    },
    'skill': {
        'filename': 'diagonal-ramsey-paley-book-bounds-SKILL.md',
        'name': 'diagonal-ramsey-paley-book-bounds',
        'description': (
            'AI-agnostic extremal and probabilistic combinatorics skill for diagonal Ramsey numbers R(k, k), Goodman '
            'triangle multiplicity, Paley P(17), rational Erdos first-moment floors, and asymmetric book bounds.'
        ),
        'rules': [
            (
                'Require strict inequality E[X_k(n, p)] = C(n, k) * (p^C(k,2) + (1 - p)^C(k,2)) < 1 in rational '
                'arithmetic when computing the first-moment witness n_1(k, p), since E = 1 (as at k = 3, n = 4, p = 0.50) '
                'permits constant-1 random variables with zero clique-free colorings.'
            ),
            (
                'Distinguish continuous expectation minimization at p = 0.50 from integer quantization plateaus of '
                'n_1(k, p) at k = 3 (n_1 = 3 across [0.20, 0.80]) and k = 4 (n_1 = 6 across [0.40, 0.60]).'
            ),
            (
                'Verify R(3, 3) = 6, R(3, 4) = 9, and R(4, 4) = 18 via explicit witnesses (C_5, Z_8 circulant {1, 4, 7}, '
                'and self-complementary Paley P(17) over F_17) paired with Goodman multiplicity and degree-sum parity.'
            ),
            (
                'Keep R(5, 5) explicitly labeled OPEN inside [43, 46] (Exoo 1989; Angeltveit & McKay 2026) and state the '
                'asymptotic root bracket as lim inf >= sqrt(2) and lim sup <= 4 - epsilon (Campos et al. 2026) without '
                'assuming the limit exists or inventing a numerical value for epsilon.'
            ),
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.0',
            'date': '2026-11-21',
            'summary': (
                'REV 1.0 (Published 2026-11-21): Volume VII Mathematics monograph continuing Folios M.03 & M.13 across '
                'Ramsey (1930), Erdős–Szekeres (1935), Erdős (1947), Greenwood–Gleason (1955), Goodman (1959), Spencer '
                '(1975), Thomason (1988), Exoo (1989), McKay–Radziszowski (1995), Conlon (2009), Sah (2023), '
                'Campos–Griffiths–Morris–Sahasrabudhe (2026), and Angeltveit–McKay (2026).'
            ),
            'opus': (
                'Verification note: twelve primary journal DOIs were checked against Crossref and Scite on 2026-11-21 '
                'with zero retraction notices; skills/math/m15/verify_m15_ramsey_bounds.py recomputes all 32,768 K_6 '
                'colorings, the Z_8 witness and K_9 parity bound for R(3, 4) = 9, all 2,380 four-subsets of Paley P(17) '
                'for R(4, 4) = 18, and rational Fraction union bounds across k = 3..10 and p = 0.20..0.80.'
            ),
        }
    ],
    'volume': 7,
    'volume_code': 'VOL. 07',
    'reading_time': '23 MIN READ',
    'word_count': '4,900 WORDS',
    'scite': dict(_SCITE),
}

LONGFORM_DATA = {
    'reading_time': '23 MIN READ',
    'word_count': '4,900 WORDS',
    'parent_folios': ['M.03', 'M.13'],
    'lineage_mode': 'CONTINUATION · Extends M.03 Extremal Combinatorics & M.13 Graph Packing Bounds',
    'scite': dict(_SCITE),
    'act1_title': 'Act I — Cool Fact & Human Story: Seventeen Brass Pins, Coin Flips, and an Eighty-Eight-Year Ceiling',
    'act1_dropcap': (
        'Seventeen brass pins stand in a circle on an ash pegboard, linked across every pair by taut crimson or indigo '
        'silk threads. Inspect all two thousand three hundred eighty quartets of pins and not one quartet shares a '
        'single thread color. Add an eighteenth pin, however, and every possible lacing contains at least one solid '
        'crimson quartet or one solid indigo quartet. Young Cambridge logician Frank Plumpton Ramsey uncovered this law '
        'of unavoidable order shortly before his death at age twenty-six in nineteen thirty. Yet finding the threshold '
        'for five pins has defeated exhaustive search for decades. Today mathematicians know only that the five-pin '
        'threshold sits at forty-three, forty-four, forty-five, or forty-six. Stranger still, Paul Erdős showed in '
        'nineteen forty-seven that tossing a fair coin for each thread beats every constructive recipe known in high '
        'dimensions.'
    ),
    'act1_plain_bridge': (
        'In plain words, gather six strangers in a room. Either three of them have all met before, or three of them '
        'are mutual strangers. Chaos has a size limit: paint every link between enough dots in red or blue, and a '
        'single-color cluster of your chosen size will appear. The puzzle is how big the room can grow before that '
        'cluster becomes unavoidable. For clusters of three dots, six is the tipping point. For clusters of four dots, '
        'seventeen dots can dodge every four-dot group, while eighteen dots force one. For clusters of five dots, all '
        'modern computers have narrowed the tipping point to four whole numbers between forty-three and forty-six. At '
        'large cluster sizes, nobody knows the growth rate, though a twenty twenty-three book method recently pushed '
        'the eighty-eight-year upper ceiling downward by an exponential step.'
    ),
    'act1_body': (
        'Ramsey introduced his theorem in Proceedings of the London Mathematical Society while studying decision '
        'procedures in formal logic (1930, DOI 10.1112/plms/s2-30.1.264). Five years later, Paul Erdős and George '
        'Szekeres rediscovered the finite graph version in Budapest to show that large point sets in the plane contain '
        'convex polygons. By picking one pivot vertex and splitting its neighbors into red neighbors and blue neighbors, '
        'they bounded each threshold by the sum of two smaller thresholds, yielding a central binomial ceiling that '
        'grows near powers of four. Twelve years after that, Erdős (1947, DOI 10.1090/S0002-9904-1947-08785-1) flipped '
        'the problem upside down: instead of building a clever coloring by hand, he colored every edge independently by '
        'a fair coin toss and summed the average count of monochromatic cliques. Whenever that average stays below one, '
        'a valid coloring exists even if nobody can point to it.'
    ),
    'act1_stakes': (
        'For small cliques, algebraic symmetry outran random coin tosses. Robert Greenwood and Andrew Gleason (1955, '
        'DOI 10.4153/CJM-1955-001-4) built a seventeen-vertex coloring from quadratic residues modulo seventeen that '
        'settled the four-clique number at eighteen, while Adolph Goodman (1959, DOI 10.1080/00029890.1959.11989408) '
        'counted monochromatic triangles directly from vertex degrees. Brendan McKay and Stanisław Radziszowski (1995, '
        'DOI 10.1002/jgt.3190190304) settled the mixed four-versus-five threshold at twenty-five. On symmetric '
        'five-cliques, Geoffrey Exoo (1989, DOI 10.1002/jgt.3190130113) found a forty-two-vertex coloring and Vigleik '
        'Angeltveit and Brendan McKay (2026, DOI 10.1002/jgt.70029) lowered the upper ceiling to forty-six via linear '
        'programming and independent computer checks. Asymptotically, Joel Spencer (1975, DOI 10.1016/0097-3165(75)90071-0) '
        'doubled Erdős’s random floor, while Andrew Thomason (1988, DOI 10.1002/jgt.3190120406), David Conlon (2009, '
        'DOI 10.4007/annals.2009.170.941), and Ashwin Sah (2023, DOI 10.1215/00127094-2022-0048) shaved sub-exponential '
        'factors off powers of four before Marcelo Campos, Simon Griffiths, Robert Morris, and Julian Sahasrabudhe '
        '(2026, DOI 10.4007/annals.2026.203.3.4) lowered the exponential base itself below four.'
    ),
    'pullquote': (
        '"Tossing a fair coin for every edge builds clique-free graphs that no human algebraist has yet matched at '
        'large scale—while seventeen brass pins modulo seventeen settle four-cliques by pure quadratic symmetry."'
    ),
    'chronology': [
        (
            '1930',
            'Frank P. Ramsey publishes his finite and infinite partition theorems in formal logic '
            '(Proceedings of the London Mathematical Society, DOI 10.1112/plms/s2-30.1.264).'
        ),
        (
            '1935 & 1947',
            'Paul Erdős and George Szekeres derive the neighborhood pigeonhole recursion in Compositio Mathematica; '
            'Erdős introduces the probabilistic first-moment floor (Bulletin of the AMS, DOI 10.1090/S0002-9904-1947-08785-1).'
        ),
        (
            '1955 & 1959',
            'Robert Greenwood and Andrew Gleason settle the four-clique threshold at eighteen using quadratic residues '
            'modulo seventeen (DOI 10.4153/CJM-1955-001-4); Adolph Goodman derives the degree formula for monochromatic '
            'triangles (DOI 10.1080/00029890.1959.11989408).'
        ),
        (
            '1975–1995',
            'Joel Spencer doubles the probabilistic floor via the Lovász Local Lemma (DOI 10.1016/0097-3165(75)90071-0); '
            'Andrew Thomason obtains a polynomial upper factor (DOI 10.1002/jgt.3190120406); Geoffrey Exoo lifts the '
            'five-clique floor to forty-three (DOI 10.1002/jgt.3190130113); Brendan McKay and Stanisław Radziszowski '
            'settle four-versus-five at twenty-five (DOI 10.1002/jgt.3190190304).'
        ),
        (
            '2009–2023',
            'David Conlon (Annals of Mathematics, DOI 10.4007/annals.2009.170.941) and Ashwin Sah (Duke Mathematical '
            'Journal, DOI 10.1215/00127094-2022-0048) push quasirandomness upper factors to quasi-polynomial decay '
            'while keeping exponential base four.'
        ),
        (
            '2026',
            'Marcelo Campos, Simon Griffiths, Robert Morris, and Julian Sahasrabudhe publish the exponential upper '
            'improvement below base four in Annals of Mathematics (DOI 10.4007/annals.2026.203.3.4, preprint '
            'arXiv:2303.09521), and Vigleik Angeltveit and Brendan McKay narrow the five-clique ceiling to forty-six '
            '(Journal of Graph Theory, DOI 10.1002/jgt.70029, preprint arXiv:2409.15709).'
        ),
    ],
    'act2_title': 'Act II — Cross-Field Intuition: Switchboard Patch Cords, Convex Coin Bias & Book Subgraphs',
    'act2_analogy': (
        'Everyday analogy: Consider an old telephone switchboard where every pair of jacks is linked by either a '
        'crimson patch cord or an indigo patch cord. An operator scanning for a tangled group of five mutually '
        'cross-patched jacks pulls one master jack and sorts its remaining cords into a crimson bundle and an indigo '
        'bundle; whichever bundle holds at least half the board becomes the next search pool. A newer strategy instead builds, one jack at a time, a small group of mutually crimson jacks (the spine) that all share one large crimson neighborhood (the pages): a combinatorial book. Where the '
        'analogy stops: physical patch cords sit on a small fixed panel, whereas graph neighborhoods lose half their '
        'vertices at each balanced step and shift edge density dynamically across dozens of recursive stages.'
    ),
    'act2_plain_primer': (
        'Our interactive Ramsey workbench has two controls and mirrors, in the browser, the arithmetic of our rational Python verifier. The first '
        'slider sets Clique Target Size from three up to ten vertices, stepping from the settled three-clique and '
        'four-clique numbers through the open five-clique window and into asymptotic territory where only exponential '
        'bounds are known. The second slider adjusts Red Edge Density between twenty percent and eighty percent in '
        'five-percent steps, showing how biasing a random coloring away from fifty-fifty balance accelerates majority '
        'cliques and shrinks the largest graph size whose expected monochromatic clique count stays below one.'
    ),
    'distill_diagram': {
        'analogy_title': 'Two-Color Switchboard Bundles & Spine Books',
        'analogy_sub': 'Pigeonhole halving splits balanced boards; book spines harvest skewed red-dense pools',
        'force_a_title': 'Erdős First-Moment Union Floor n_1(k, p) + 1',
        'force_a_sub': 'Convexity of p^m + (1 − p)^m minimizes expected cliques at balanced p = 0.50 (base √2)',
        'force_b_title': 'Pigeonhole & Asymmetric Book Ceiling',
        'force_b_sub': 'Erdős–Szekeres C(2k − 2, k − 1) compressed exponentially to (4 − ε)^k by Campos et al. (2026)',
        'threshold_title': 'Settled Small Values vs Open Ramsey Regimes',
        'threshold_pass': 'Settled k = 3, 4: R(3, 3) = 6 (Goodman K_6) and R(4, 4) = 18 (Paley P(17) over F_17)',
        'threshold_fail': 'Open k ≥ 5: 43 ≤ R(5, 5) ≤ 46 and asymptotic root interval [√2, 4 − ε]',
    },
    'act2_intuition': (
        'Let K_n denote the complete graph on n vertices with C(n, 2) edges, each colored red with probability p and '
        'blue with probability 1 − p independently. A fixed k-vertex subset spans m = C(k, 2) = k(k − 1)/2 edges, so '
        'it forms a red K_k with probability p^m and a blue K_k with probability (1 − p)^m. By linearity of expectation '
        '—which holds even though overlapping k-subsets share edges—the expected number of monochromatic k-cliques is '
        'E[X_k(n, p)] = C(n, k)[p^m + (1 − p)^m]. Because X_k takes non-negative integer values, strict inequality '
        'E[X_k(n, p)] < 1 forces Pr(X_k = 0) > 0, meaning at least one red-blue coloring of K_n has zero monochromatic '
        'K_k and hence R(k, k) ≥ n + 1. Note why strict inequality < 1 is essential: at k = 3, n = 4, and p = 0.50, '
        'E[X_3(4, 0.50)] = 4 × (1/8 + 1/8) = 1, which still permits a coloring of K_4 with zero monochromatic triangles '
        '(such as a red 4-cycle C_4 with blue diagonals), yet E ≤ 1 by itself cannot rule out a constant-one distribution '
        'without inspecting higher moments or exhibiting an explicit witness.'
    ),
    'act2_deepening': (
        'Differentiating φ_m(p) = p^m + (1 − p)^m twice gives φ_m″(p) = m(m − 1)[p^(m−2) + (1 − p)^(m−2)] > 0 for '
        'm = C(k, 2) ≥ 3, so φ_m is strictly convex on [0, 1] with unique minimum 2^(1−m) at p = 1/2. Using Stirling’s '
        'bound C(n, k) ≤ n^k / k! < (1 / √(2πk)) (en/k)^k, setting p = 1/2 gives E[X_k(n, 1/2)] < 2 / √(2πk) < 1 for '
        'all k ≥ 3 whenever n ≤ (1/(e√2)) k 2^(k/2), anchoring Erdős’s 1947 base √2 ≈ 1.414214; Spencer (1975) applied '
        'the symmetric Lovász Local Lemma to '
        'weakly dependent k-subsets sharing at least two vertices, doubling the lower prefactor to (√2/e) k 2^(k/2). '
        'On the upper side, Erdős–Szekeres steps one vertex at a time, halving the surviving pool at worst and '
        'producing C(2k − 2, k − 1) < 4^(k−1). Campos, Griffiths, Morris, and Sahasrabudhe (2026) introduced a book algorithm that, without using quasirandomness, builds a large monochromatic book (a clique joined in one color to a common set of vertices) one step at a time through red, big-blue, and density-boost steps, giving R(k, k) ≤ (4 − ε)^k for a positive constant ε > 0.'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Settled Small Thresholds k = 3 and k = 4 vs. Random Floors): Slide Clique Target Size k '
            'down to 3 and 4 at balanced Red Edge Density p = 0.50. At k = 3, the strict union floor gives R(3, 3) ≥ 4 '
            '(n_1 = 3) while C_5 and Goodman’s K_6 identity pin R(3, 3) = 6; at k = 4, the union floor gives R(4, 4) ≥ 7 '
            '(n_1 = 6) while Paley P(17) over F_17 and R(3, 4) + R(4, 3) = 18 settle R(4, 4) = 18.'
        ),
        (
            'Experiment 2 (The Open Five-Clique Window and Density Skew at k = 5): Return Clique Target Size to k = 5 '
            'and sweep Red Edge Density p from 0.50 toward 0.20 or 0.80. Watch n_1(5, p) peak at 11 when p = 0.50 '
            '(E = 462/512 = 0.902344, floor ≥ 12) and drop symmetrically to 10 at p = 0.45/0.55 and 6 at p = 0.20/0.80, '
            'while the published bracket highlights the four-integer open window 43 ≤ R(5, 5) ≤ 46.'
        ),
        (
            'Experiment 3 (High-k Exponential Chasm and Sharp Density Sensitivity at k = 10): Raise Clique Target Size '
            'to k = 10. At balanced p = 0.50, the rational union floor yields existence of a 100-vertex clique-free '
            'coloring (R(10, 10) ≥ 101, Spencer LLL scale 166.48) against C(18, 9) = 48,620; nudging p by just 0.05 to '
            '0.45 or 0.55 drops n_1 from 100 to 71, and p = 0.20 drops it to 17.'
        ),
    ],
    'act4_title': 'Act IV — Imagining Humanity’s Future: Quasirandomness, LP/Computer Bounds & Open Ramsey Horizons',
    'act4_human_ai': (
        'Ramsey theory forged two tools that now sit across theoretical computer science, coding theory, and '
        'combinatorial optimization: the probabilistic method (Folio M.03) and algebraic pseudorandomness. Graphs that '
        'mimic coin flips—such as Paley quadratic-residue graphs—inspire explicit expanders, low-discrepancy samplers, '
        'and communication networks resilient to localized edge failures, while linear programming and large computer case checks drive modern bounds on finite Ramsey instances, such as Angeltveit and McKay’s 2026 upper bound R(5, 5) ≤ 46.'
    ),
    'act4_deepening': (
        'Under the Tier T0–T1 evidence discipline of this monograph, three layers stay strictly separated. First, '
        'our pure-Python script skills/math/m15/verify_m15_ramsey_bounds.py recomputes R(3, 3) = 6 (all 32,768 K_6 colorings) and the lower-bound witnesses for R(3, 4) > 8 (Z_8 circulant {1, 4, 7}) and R(4, 4) > 17 (all 2,380 four-subsets of Paley P(17)); it restates, but does not machine-check, the matching upper-bound arguments (K_9 odd degree sum 27, and 9 + 9 = 18); and it computes rational Fraction union bounds n_1(k, p) across k ∈ [3..10] and '
        'p ∈ [0.20..0.80], failing deterministically under --planted-defect when C_5, Z_8, P(17), or strict < 1 are '
        'corrupted. Second, the bounds 43 ≤ R(5, 5) ≤ 46 (Exoo 1989; Angeltveit & McKay 2026) and R(k, k) ≤ (4 − ε)^k '
        '(Campos, Griffiths, Morris & Sahasrabudhe 2026) are cited from peer-reviewed publications with ε > 0 kept '
        'symbolic as in the Annals abstract. Third, both the integer value of R(5, 5) ∈ {43, 44, 45, 46} and whether '
        'lim_{k→∞} R(k, k)^(1/k) exists inside [√2, 4 − ε] remain OPEN: exhibiting a 43-vertex (K_5, K_5)-free '
        'coloring would refute R(5, 5) = 43, whereas an explicit graph family exceeding exponential base √2 would '
        'falsify tightness of Erdős’s random lower base.'
    ),
    'cf_bridge': 'Extends M.03/M.13 · Probabilistic existence, algebraic pseudorandomness and asymmetric density boosting',
    'sources': [
        (
            'Ramsey, F. P. (1930). On a Problem of Formal Logic. Proceedings of the London Mathematical Society, '
            's2-30(1), 264–286. DOI: 10.1112/plms/s2-30.1.264.'
        ),
        (
            'Erdős, P., & Szekeres, G. (1935). A combinatorial problem in geometry. Compositio Mathematica, 2, 463–470.'
        ),
        (
            'Erdős, P. (1947). Some remarks on the theory of graphs. Bulletin of the American Mathematical Society, '
            '53(4), 292–294. DOI: 10.1090/S0002-9904-1947-08785-1.'
        ),
        (
            'Greenwood, R. E., & Gleason, A. M. (1955). Combinatorial Relations and Chromatic Graphs. Canadian Journal '
            'of Mathematics, 7, 1–7. DOI: 10.4153/CJM-1955-001-4.'
        ),
        (
            'Goodman, A. W. (1959). On Sets of Acquaintances and Strangers at any Party. The American Mathematical '
            'Monthly, 66(9), 778–783. DOI: 10.1080/00029890.1959.11989408.'
        ),
        (
            'Spencer, J. (1975). Ramsey’s theorem—A new lower bound. Journal of Combinatorial Theory, Series A, 18(1), '
            '108–115. DOI: 10.1016/0097-3165(75)90071-0.'
        ),
        (
            'Thomason, A. (1988). An upper bound for some Ramsey numbers. Journal of Graph Theory, 12(4), 509–517. '
            'DOI: 10.1002/jgt.3190120406.'
        ),
        (
            'Exoo, G. (1989). A lower bound for R(5, 5). Journal of Graph Theory, 13(1), 97–98. '
            'DOI: 10.1002/jgt.3190130113.'
        ),
        (
            'McKay, B. D., & Radziszowski, S. P. (1995). R(4, 5) = 25. Journal of Graph Theory, 19(3), 309–322. '
            'DOI: 10.1002/jgt.3190190304.'
        ),
        (
            'Conlon, D. (2009). A new upper bound for diagonal Ramsey numbers. Annals of Mathematics, 170(2), '
            '941–960. DOI: 10.4007/annals.2009.170.941.'
        ),
        (
            'Sah, A. (2023). Diagonal Ramsey via effective quasirandomness. Duke Mathematical Journal, 172(3), '
            '545–567. DOI: 10.1215/00127094-2022-0048.'
        ),
        (
            'Campos, M., Griffiths, S., Morris, R., & Sahasrabudhe, J. (2026). An exponential improvement for diagonal '
            'Ramsey. Annals of Mathematics, 203(3), 869–932 (preprint arXiv:2303.09521). DOI: 10.4007/annals.2026.203.3.4.'
        ),
        (
            'Angeltveit, V., & McKay, B. D. (2026). R(5, 5) ≤ 46. Journal of Graph Theory (preprint arXiv:2409.15709). '
            'DOI: 10.1002/jgt.70029.'
        ),
        (
            'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and '
            'classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
            '882–898. DOI: 10.1162/qss_a_00146.'
        ),
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Diagonal Ramsey log-scale bounds '
        'comparing Erdos random floor, settled Paley P(17) at k = 4, open R(5, 5) in [43, 46], and C(2k-2, k-1) ceiling">\n'
        '            <line x1="48" y1="184" x2="352" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <line x1="48" y1="28" x2="48" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <text x="54" y="20" font-size="10.2" font-weight="600" fill="currentColor">Log₁₀ Bounds: Erdős Floor vs. Binomial / Book Ceiling</text>\n'
        '            <path id="tp-m15-ceil-curve" data-custom-curve="1" d="M 60 159 L 98 142 L 136 124 L 174 106 L 212 88 L 250 69 L 288 51 L 326 32" fill="none" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="5,3"/>\n'
        '            <path id="tp-m15-floor-curve" data-custom-curve="1" d="M 60 164 L 98 157 L 136 149 L 174 143 L 212 137 L 250 131 L 288 125 L 326 119" fill="none" stroke="var(--tp-verdigris)" stroke-width="2.3"/>\n'
        '            <rect id="tp-m15-floor-bar" x="126" y="149" width="16" height="35" rx="2" fill="var(--tp-verdigris)" fill-opacity="0.45"/>\n'
        '            <rect id="tp-m15-ceil-bar" x="145" y="124" width="16" height="60" rx="2" fill="var(--tp-minium)" fill-opacity="0.32"/>\n'
        '            <circle id="tp-m15-point" cx="136" cy="149" r="5.5" fill="var(--tp-prussian)"/>\n'
        '            <text x="56" y="42" font-size="8.8" fill="var(--tp-minium)">Ceiling C(2k−2, k−1) · Book (4−ε)^k</text>\n'
        '            <text x="156" y="176" font-size="8.8" fill="var(--tp-verdigris)">Floor n_1(k, p) + 1</text>\n'
        '            <line x1="366" y1="24" x2="366" y2="192" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="378" y="20" font-size="10.2" font-weight="600" fill="currentColor">Small Witnesses &amp; Open R(5, 5)</text>\n'
        '            <rect x="378" y="36" width="194" height="62" rx="6" fill="var(--tp-stone)" fill-opacity="0.28" stroke="var(--tp-prussian)" stroke-width="1.6"/>\n'
        '            <text id="tp-m15-status-lbl" x="388" y="58" font-size="8.6" font-weight="600" fill="var(--tp-prussian)">k = 5, p = 0.50: floor ≥ 12 · C(8,4) = 70</text>\n'
        '            <text x="388" y="78" font-size="8.6" fill="var(--tp-verdigris)">Paley P(17): SRG(17,8,3,4) → R(4,4) = 18</text>\n'
        '            <rect x="378" y="112" width="194" height="58" rx="6" fill="var(--tp-verdigris)" fill-opacity="0.12" stroke="var(--tp-verdigris)" stroke-width="1.4"/>\n'
        '            <text x="388" y="134" font-size="8.8" font-weight="600" fill="var(--tp-prussian)">Open R(5, 5) ∈ [43, 46] · K_6 min K_3 = 2</text>\n'
        '            <text x="388" y="154" font-size="8.6" fill="var(--tp-minium)">Root base: √2 ≤ lim inf ≤ lim sup ≤ 4 − ε</text>\n'
        '            <text x="48" y="206" font-size="10" fill="var(--tp-verdigris)">Rational Fraction &amp; 32,768 K_6 checks · Recomputed offline by verify_m15_ramsey_bounds.py</text>\n'
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining what a seventeen-pin circular ash-wood pegboard for two-color Ramsey '
        'graph theory would look like: seventeen turned solid-brass pins laced with taut crimson-terracotta and '
        'Prussian-indigo silk threads beside two wooden thread spools and antique brass dividers on cream archival '
        'vellum over dark slate (artistic impression, not a measured physical specimen; exact structure and '
        'specifications are kept strictly intact in the deterministic Plate below)'
    ),
    'caption': (
        'Conceptual Vision Plate M.15-V (Imagining What It Would Look Like) · Conceptual visualization imagining '
        'what a seventeen-pin circular pegboard laced with crimson and Prussian-indigo silk threads would look like '
        '(artistic impression, not a measured structure or specification; exact structure and specifications are kept '
        'strictly intact in the deterministic Plate M.15-A and verify_m15_ramsey_bounds.py below).'
    ),
}

DISPATCH = {
    'kicker': 'FRONTIER EXTREMAL COMBINATORICS DISPATCH · RAMSEY NUMBERS & BOOK ALGORITHMS',
    'headline': 'Breaking the Eighty-Eight-Year Base-Four Ceiling While R(5, 5) Narrows to [43, 46]',
    'body': (
        'For eighty-eight years after Erdős and Szekeres (1935), upper bounds on diagonal Ramsey numbers R(k, k) '
        'remained at base 4 − o(1). Campos, Griffiths, Morris, and Sahasrabudhe (2026, Annals of Mathematics, '
        'DOI 10.4007/annals.2026.203.3.4) lowered the exponential base to 4 − ε, giving R(k, k) ≤ (4 − ε)^k via an '
        'asymmetric book algorithm, while Angeltveit and McKay (2026, DOI 10.1002/jgt.70029) compressed R(5, 5) into [43, 46].'
    ),
}

META_3D = (
    'Diagonal Ramsey First-Moment Convexity & Exponential Growth Envelope',
    'X: Clique Target Size k · Z: Red Edge Density p · Y: Log₁₀ Clique-Free Threshold vs Ceiling',
)

ES_TRANSLATION = {
    'title_es': (
        'Números de Ramsey Diagonales: Grafos de Paley, Cotas Aleatorias de Erdős, el Algoritmo del Libro y Brechas Abiertas'
    ),
    'subtitle_es': (
        'Cómo Frank Ramsey halló orden inevitable en grafos coloreados, cómo Paul Erdős fundó el método '
        'probabilístico en tres páginas, por qué diecisiete residuos cuadráticos cierran las camarillas de cuatro '
        'mientras las de cinco quedan entre cuarenta y tres y cuarenta y seis, y cómo el algoritmo del libro bajó '
        'la base exponencial debajo de cuatro.'
    ),
    'why_es': (
        'Reunir a seis personas en una sala obliga a que tres se conozcan entre sí o a que tres sean desconocidas; '
        'sin embargo, para grupos de cinco personas el umbral sigue abierto entre cuarenta y tres y cuarenta y seis.'
    ),
    'plain_es': (
        'En palabras sencillas, reúnan a seis desconocidos en una sala. O bien tres ya se habían tratado antes, o '
        'bien tres no se conocen entre sí. El desorden tiene un tamaño máximo: si pintan de rojo o azul cada enlace '
        'entre suficientes puntos, aparecerá un grupo de un solo color del tamaño elegido. La pregunta es cuánto '
        'puede crecer la red antes de que ese grupo sea inevitable. Para grupos de tres puntos, seis es el umbral. '
        'Para grupos de cuatro puntos, diecisiete puntos logran esquivar cada cuarteto monocromático, pero dieciocho '
        'puntos fuerzan uno. Para grupos de cinco puntos, las computadoras actuales han acotado el umbral a cuatro '
        'enteros entre cuarenta y tres y cuarenta y seis. En tamaños grandes nadie conoce la tasa de crecimiento, '
        'aunque en dos mil veintitrés el método del libro redujo exponencialmente un techo de ochenta y ocho años.'
    ),
    'deep_es': (
        'En el argumento probabilístico de Erdős (1947, DOI 10.1090/S0002-9904-1947-08785-1), que da una cota inferior para los números de Ramsey (1930, DOI 10.1112/plms/s2-30.1.264), colorear cada arista de K_n en rojo con probabilidad p produce un '
        'conteo esperado E[X_k(n, p)] = C(n, k)[p^C(k,2) + (1 − p)^C(k,2)]. Cuando E[X_k(n, p)] < 1 en aritmética '
        'racional, existe al menos una coloración sin K_k monocromático, dando R(k, k) ≥ n_1(k, p) + 1 y base '
        'asintótica √2 ≈ 1.414214 (Spencer 1975, DOI 10.1016/0097-3165(75)90071-0, duplicó la constante del prefactor, no la base). '
        'Nuestro script fuera de línea comprueba las 32,768 coloraciones de K_6 con mínimo de 2 triángulos en 1,760 '
        'casos (Goodman 1959, DOI 10.1080/00029890.1959.11989408), el grafo circulante en Z_8 y la paridad 9 × 3 = 27 '
        'para R(3, 4) = 9, y los 2,380 subconjuntos de cuatro vértices del grafo de Paley P(17) sobre F_17 para '
        'R(4, 4) = 18 (Greenwood & Gleason 1955, DOI 10.4153/CJM-1955-001-4). Para k = 5 permanece abierta la '
        'ventana 43 ≤ R(5, 5) ≤ 46 (Exoo 1989, DOI 10.1002/jgt.3190130113; Angeltveit & McKay 2026, '
        'DOI 10.1002/jgt.70029), mientras Campos, Griffiths, Morris y Sahasrabudhe (2026, '
        'DOI 10.4007/annals.2026.203.3.4) obtuvieron R(k, k) ≤ (4 − ε)^k con ε > 0 constante. Tanto el entero '
        'R(5, 5) como la existencia de lim R(k, k)^(1/k) en [√2, 4 − ε] siguen abiertos.'
    ),
    'bridge_es': (
        'Extiende M.03 y M.13 a números de Ramsey diagonales: comprueba R(3, 3) = 6 y R(4, 4) = 18 mediante P(17), '
        'evalúa pisos racionales de Erdős y acota las brechas abiertas en R(5, 5) y en [√2, 4 − ε].'
    ),
}
