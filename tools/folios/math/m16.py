#!/usr/bin/env python3
"""Folio M.16 (MATH): Three-Term Arithmetic Progressions, Behrend Spheres & Kelley-Meka Quasi-Polynomial Bounds."""
from __future__ import annotations

SLUG = 'm16'

PILLAR = 'math'

_SCITE = {
    'doi': '10.1112/jlms/s1-28.1.104',
    'fetched_on': '2026-11-24',
    'citing_publications': 666,
    'supporting': 4,
    'mentioning': 451,
    'contrasting': 0,
    'retracted': False,
    'summary': (
        'Scite Smart Citation Index entry for Roth 1953, "On Certain Sets of Integers" '
        '(Journal of the London Mathematical Society, DOI 10.1112/jlms/s1-28.1.104), fetched 2026-11-24 '
        '[observed: Scite ML citation classification, accessed 2026-11-24]: 666 citing publications, with '
        '4 supporting, 451 mentioning, and 0 contrasting classified citation statements, and no retraction notice. '
        'Citing publications and classified citation statements are distinct counts, and describe that foundational '
        'paper rather than this folio.'
    ),
}

FOLIO = {
    'folio_id': 'M.16',
    'slug': 'm16',
    'pillar': 'math',
    'category_code': 'M',
    'parent_folios': ['M.03', 'M.04', 'M.15'],
    'lineage_mode': 'CONTINUATION · Extends M.03 Cap Sets, M.04 Additive Entropy & M.15 Extremal Thresholds',
    'title': 'Three-Term Arithmetic Progressions: Behrend Spheres, Fourier Bias & Kelley–Meka Bounds',
    'subtitle': (
        'How Paul Erdős and Pál Turán asked whether positive density forces three equally spaced integers, how Felix '
        'Behrend hid dense progression-free sets on high-dimensional spheres, how Klaus Roth turned harmonic ripples '
        'into density increments, and how Zander Kelley and Raghu Meka reached quasi-polynomial decay.'
    ),
    'date_published': '2026-11-24',
    'date_redated': '2026-11-24',
    'current_edition': 'REV 1.0',
    'status_badge': 'ADDITIVE COMBINATORICS BOUNDS · REV 1.0',
    'primary_kernel': 'skills/math/m16/verify_m16_progression_bounds.py',
    'governing_law': (
        'For N ≥ 3: T(A) = (1/M) ∑_r Â(r)² conj(Â(2r mod M)) · '
        'N exp(−c √(log N)) ≤ r_3(N) ≤ N exp(−c′ (log N)^(1/9))'
    ),
    'colophon': {
        'identifier': 'M.16 · Three-Term Arithmetic Progressions & Behrend Spheres · REV 1.0',
        'kernels': 'Bitmask Branch-and-Bound r_3(N) · Base-(2d−1) Spherical Shell DP · Odd-Modulus Cyclic DFT',
        'benchmarks': (
            'r_3(9) = 5 > |C_3(9)| = 4 · r_3(20) = 9, r_3(24) = 10 · '
            '|B(5, 4)| = 30 on R*² = 18 in N = 6,561 · Open log exponent β ∈ [1/9, 1/2]'
        ),
        'bridge': 'Extends M.03/M.04/M.15 · Strict Euclidean convexity, carry-free radix projection and sifting increments',
    },
    'sliders': [
        {
            'label': 'Digit Bound (d)',
            'min': 2,
            'max': 8,
            'step': 1,
            'value': 5,
            'unit': 'd = ',
        },
        {
            'label': 'Shell Dimension (m)',
            'min': 2,
            'max': 6,
            'step': 1,
            'value': 4,
            'unit': 'm = ',
        },
    ],
    'steps': [
        (
            'Stage 1 (Small Extremal Thresholds and Ternary Cantor Departures, 1936): Paul Erdős and Pál Turán '
            '(1936, DOI 10.1112/jlms/s1-11.4.261) introduced r_3(N), the maximum size of a subset of {1, …, N} '
            'containing no three distinct terms in arithmetic progression x + z = 2y, and recorded the base-3 '
            '{0, 1} construction (credited there to G. Szekeres), written here as C_3(N) of scale N^(log_3 2) ≈ '
            'N^0.63093. Exhaustive search in verify_m16_progression_bounds.py recomputes r_3(1..24) and pinpoints '
            'where optimal sets outgrow C_3(N): at N = 9, witness {1, 2, 4, 8, 9} gives r_3(9) = 5 > |C_3(9)| = 4; '
            'at N = 14, r_3(14) = |C_3(14)| = 8; at N = 20, {1, 2, 6, 7, 9, 14, 15, 18, 20} gives r_3(20) = 9 > 8; '
            'and at N = 24, r_3(24) = 10 > 8.'
        ),
        (
            'Stage 2 (Behrend Spherical Shells and Carry-Free Base-(2d − 1) Projection, 1942–2011): Raphaël Salem '
            'and Donald Spencer (1942, DOI 10.1073/pnas.28.12.561) refuted sub-linear power-law ceilings O(N^(1 − ε)) '
            'on r_3(N), and Felix Behrend (1946, DOI 10.1073/pnas.32.12.331) intersected {0, …, d − 1}^m with '
            'quadratic shells ∑ x_i² = R², choosing modal shell R*² of size S_m(R*²) ≥ ⌈d^m / (m(d − 1)² + 1)⌉ and '
            'projecting via radix b = 2d − 1 into {1, …, (2d − 1)^m}. Because 0 ≤ x_i + z_i ≤ 2d − 2 < 2d − 1 blocks '
            'every base carry and strict Euclidean convexity forbids three distinct collinear sphere points, B(d, m) '
            'has zero nontrivial 3-APs; Michael Elkin (2011, DOI 10.1007/s11856-011-0061-1) and Ben Green with Julia '
            'Wolf (2010, DOI 10.1007/978-0-387-68361-4_9) thickened the sphere to a thin annulus, raising r_3(N) by a '
            'Θ(√(log N)) factor.'
        ),
        (
            'Stage 3 (Roth’s Circle Method and Our Odd-Modulus Z_{2N+1} Discretization, 1953–2011): Klaus Roth '
            '(1953, DOI 10.1112/jlms/s1-28.1.104) adapted the continuous Hardy–Littlewood circle method on [0, 1] to '
            'establish r_3(N) = O(N / log log N). To check finite sets exactly, this folio discretizes Roth’s '
            'orthogonality identity onto the odd cyclic group Z_M of order M = 2N + 1, preventing wrap-around since '
            '2 ≤ x + z ≤ 2N < M and giving T(A) = (1/M) ∑_{r=0}^{M−1} Â(r)² conj(Â(2r mod M)) with complex square '
            'Â(r)². When A is 3-AP-free, T(A) = |A|, yielding our finite linear bias floor max_{r≠0} |Â(r)| ≥ '
            '||A|² − M| / (M − |A|) alongside Parseval’s RMS floor √(|A|(M − |A|)/(M − 1)); Jean Bourgain (1999, '
            'DOI 10.1007/s000390050105) and Tom Sanders (2011, DOI 10.4007/annals.2011.174.1.20) refined Bohr-set '
            'and almost-periodicity increments.'
        ),
        (
            'Stage 4 (Kelley–Meka Physical-Space Sifting, Combined Display Note & Tier T0–T1 Falsification, 2020–2023): '
            'After Thomas Bloom and Olof Sisask crossed the logarithmic barrier in preprint arXiv:2007.03528, Zander '
            'Kelley and Raghu Meka (2023, DOI 10.1109/focs57990.2023.00059, arXiv:2302.05537) bypassed high-order '
            'Fourier inversions via Hölder decoupling, physical-space sifting, and spread subspaces to establish '
            'r_3(N) ≤ exp(−c (log N)^(1/12)) N (c > 0), expounded on integer intervals at β = 1/12 by Bloom and '
            'Sisask (2023, DOI 10.2140/ent.2023.2.15) and sharpened to β = 1/9 in preprint arXiv:2309.02353 (for '
            'N ≥ 3, combined in our governing header beside Behrend’s β = 1/2 lower bound and our Z_{2N+1} DFT '
            'identity). Hypothesis (Tier T0–T1): across d ∈ [2..8], m ∈ [2..6], radix-(2d − 1) overhead keeps '
            '|B(d, m)| < |C_3(N)| before asymptotic crossover, while valid log exponents in [1/9, 1/2] remain OPEN; '
            'any construction with β < 1/2 or upper bound with β > 1/9 narrows that open interval.'
        ),
    ],
    'readouts': [
        {
            'label': 'Modal Behrend Shell |B(d, m)|',
            'value': '|B(5, 4)| = 30 on R*² = 18 (in N = 6,561, base 9)',
        },
        {
            'label': 'Grid Pigeonhole & Ternary Baseline',
            'value': 'Pigeonhole ≥ 10 (625 / 65 shells) · Cantor C_3(6,561) = 256',
        },
        {
            'label': 'Small Exact r_3(N) & Fourier Peak (Fixed Reference)',
            'value': 'r_3(9) = 5, r_3(14) = 8, r_3(20) = 9, r_3(24) = 10 · max |Â(r)| = 5.15 at N = 20 (M = 41)',
        },
        {
            'label': 'Asymptotic Log-Exponent Window',
            'value': 'OPEN EXPONENT GAP β ∈ [1/9, 1/2] · FINITE CROSSOVER REGIME',
        },
    ],
    'spec_plate': {
        'division': 'ADDITIVE & EXTREMAL COMBINATORICS / PROGRESSION-FREE SHELLS & HARMONIC SIFTING',
        'title': 'Exhaustive r_3(1..24), Base-(2d−1) Behrend Spherical Shells & Odd-Modulus Cyclic DFT',
        'body': (
            'Scope boundary: verify_m16_progression_bounds.py recomputes offline from scratch exact r_3(N) for '
            'N = 1..24 via bitmask branch-and-bound (cross-checked against power-set enumeration for N = 1..14), '
            'explicit base-(2d − 1) Behrend sets B(d, m) for d ∈ [2..5], m ∈ [2..4] with zero nontrivial 3-APs, '
            'exact dynamic-programming shell histograms across d ∈ [2..8], m ∈ [2..6], and odd-modulus Z_{2N+1} DFT '
            '3-AP identities across N = 3..24 (max floating-point residual < 1.25e-14, asserted < 1e-12). Our '
            'governing header pairs that finite Z_{2N+1} identity with Behrend’s 1946 lower bound and the '
            'Kelley & Meka (2023, β = 1/12) / Bloom & Sisask (2023 ENT exposition; preprint arXiv:2309.02353, '
            'β = 1/9) upper bounds, which are reported from those papers and not re-derived by this script.'
        ),
        'meta': (
            'Primary anchors: Erdős & Turán 1936 (DOI 10.1112/jlms/s1-11.4.261) · Behrend 1946 '
            '(DOI 10.1073/pnas.32.12.331) · Roth 1953 (DOI 10.1112/jlms/s1-28.1.104) · '
            'Kelley & Meka 2023 (DOI 10.1109/focs57990.2023.00059) · '
            'Bloom & Sisask 2023 (DOI 10.2140/ent.2023.2.15; preprint arXiv:2309.02353)'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE M.16-A · WHY DROPPING BASE 2d − 1 TO d OR FLATTENING L² TO L¹ FAILS',
        'body': (
            'Two planted knockouts in verify_m16_progression_bounds.py isolate both halves of Behrend’s 1946 idea. '
            'First, keeping the true Euclidean shell ∑ x_i² = 5 at d = 3, m = 3 (six permutations of (2, 1, 0)) but '
            'encoding in base b = 3 instead of carry-free b = 2d − 1 = 5 produces {6, 8, 12, 16, 20, 22} ⊆ {1..27}, '
            'where base-3 carries create two nontrivial three-term progressions (8, 12, 16) and (12, 16, 20) of step 4. '
            'Second, keeping carry-free base b = 5 but replacing quadratic ∑ x_i² with the flat L¹ slice ∑ x_i = 3 '
            'admits collinear vectors (2, 1, 0), (1, 1, 1), and (0, 1, 2), mapping to (8, 32, 56) of step 24.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE M.16-B · FINITE CANTOR ADVANTAGE VS ASYMPTOTIC BEHREND CROSSOVER',
        'body': (
            'On our interactive grid d ∈ [2..8], m ∈ [2..6], the shifted ternary Cantor set C_3(N) stays larger than '
            'Behrend’s shell B(d, m): at d = 5, m = 4 (N = 6,561), |C_3| = 256 exceeds |B| = 30, and even at d = 8, '
            'm = 6 (N = 11,390,625), |C_3| = 32,768 exceeds |B| = 3,300. That finite lag comes from the factor '
            '(d / (2d − 1))^m ≈ 2^(−m) paid to prevent base carries across m coordinates. Once dimension m is scaled '
            'near √(2 log_2 N) with 2d − 1 = ⌊N^(1/m)⌋ for large N, however, exp(−2√(2 ln 2) √(ln N)) decays slower '
            'than any fixed negative power N^(log_3 2 − 1) ≈ N^(−0.36907), so spherical shells eventually overtake C_3(N).'
        ),
    },
    'skill': {
        'filename': 'progression-free-behrend-kelley-meka-bounds-SKILL.md',
        'name': 'progression-free-behrend-kelley-meka-bounds',
        'description': (
            'AI-agnostic additive and extremal combinatorics skill for three-term progression-free sets r_3(N), '
            'carry-free base-(2d-1) Behrend spherical shells, odd-modulus cyclic Fourier identities, and Kelley-Meka '
            'quasi-polynomial bounds.'
        ),
        'rules': [
            (
                'Encode Behrend shell vectors x in {0, ..., d - 1}^m using radix b = 2d - 1 (never b = d) and strict '
                'Euclidean norm sum(x_i^2) = R^2 (never L^1 sum), blocking carries in x_i + z_i = 2*y_i while strict '
                'sphere convexity forces x = y = z.'
            ),
            (
                'Distinguish Roth’s 1953 continuous circle-method bound O(N / log log N) from this folio’s finite '
                'odd-modulus cyclic discretization Z_M (M = 2N + 1), and retain the complex square A_hat(r)^2 (not '
                '|A_hat(r)|^2) in T(A) = (1/M) * sum_r A_hat(r)^2 * conj(A_hat(2r mod M)).'
            ),
            (
                'Separate finite-N behavior from asymptotic growth: C_3(N) matches r_3(N) at N = 14 (8) yet trails at '
                'N = 9 (4 vs 5), N = 20 (8 vs 9), and N = 24 (8 vs 10), and |C_3((2d - 1)^m)| exceeds |B(d, m)| across '
                'd in [2..8], m in [2..6] before Behrend’s exp(-c * sqrt(log N)) density overtakes N^(log_3 2) at large m.'
            ),
            (
                'Keep the upper-bound milestones distinct—Bloom-Sisask arXiv:2007.03528 logarithmic-barrier break, '
                'Kelley-Meka 2023 (DOI 10.1109/focs57990.2023.00059) explicit exp(-c * (log N)^(1/12)) * N bound, '
                'Bloom-Sisask 2023 Essential Number Theory (DOI 10.2140/ent.2023.2.15) 1/12 exposition, and preprint '
                'arXiv:2309.02353 exponent 1/9—and keep the log-exponent gap [1/9, 1/2] explicitly labeled OPEN.'
            ),
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.0',
            'date': '2026-11-24',
            'summary': (
                'REV 1.0 (Published 2026-11-24): Volume VII Mathematics monograph continuing Folios M.03, M.04 & M.15 '
                'across Erdős–Turán (1936), Salem–Spencer (1942), Behrend (1946), Roth (1953), Szemerédi (1975), '
                'Bourgain (1999), Green–Tao (2008), Green–Wolf (2010), Elkin (2011), Sanders (2011), Kelley–Meka '
                '(2023), and Bloom–Sisask (2020 preprint; 2023 Essential Number Theory; 2023 arXiv:2309.02353).'
            ),
            'opus': (
                'Verification note: twelve primary DOIs (10.1112/jlms/s1-11.4.261, 10.1073/pnas.28.12.561, '
                '10.1073/pnas.32.12.331, 10.1112/jlms/s1-28.1.104, 10.4064/aa-27-1-199-245, 10.1007/s000390050105, '
                '10.4007/annals.2008.167.481, 10.1007/978-0-387-68361-4_9, 10.1007/s11856-011-0061-1, '
                '10.4007/annals.2011.174.1.20, 10.1109/focs57990.2023.00059, 10.2140/ent.2023.2.15) were checked '
                'against Crossref, OpenAlex, and Scite on 2026-11-24 with zero retraction notices; '
                'skills/math/m16/verify_m16_progression_bounds.py recomputes r_3(1..24), Behrend shells, and '
                'Z_{2N+1} DFT identities.'
            ),
        }
    ],
    'volume': 7,
    'volume_code': 'VOL. 07',
    'reading_time': '24 MIN READ',
    'word_count': '5,100 WORDS',
    'scite': dict(_SCITE),
}

LONGFORM_DATA = {
    'reading_time': '24 MIN READ',
    'word_count': '5,100 WORDS',
    'parent_folios': ['M.03', 'M.04', 'M.15'],
    'lineage_mode': 'CONTINUATION · Extends M.03 Cap Sets, M.04 Additive Entropy & M.15 Extremal Thresholds',
    'scite': dict(_SCITE),
    'act1_title': 'Act I — Cool Fact & Human Story: Equally Spaced Footsteps, Curved Spheres, and a Seventy-Year Log Barrier',
    'act1_dropcap': (
        'Paul Erdős and Pál Turán asked in nineteen thirty-six how many integer pebbles can sit along a chalk '
        'number line without three landing an equal stride apart. Pick one, two, four, and five, and no pebble '
        'sits halfway between two others. Add three, six, seven, or eight, and an evenly spaced triplet appears at '
        'once. Erdős and Turán conjectured that any subset holding a fixed positive share of the whole numbers must '
        'eventually contain such a trio. Ten years later at Melbourne, Felix Behrend arranged progression-free sets '
        'along thin spherical shells in high dimensions. Because round curvature bends away from every straight '
        'chord, no three distinct points on one sphere can share a line. Klaus Roth settled the positive-density '
        'question in nineteen fifty-three through harmonic waves, and Zander Kelley with Raghu Meka reached '
        'quasi-polynomial upper bounds in twenty twenty-three.'
    ),
    'act1_plain_bridge': (
        'In plain words, three whole numbers form an evenly spaced trio whenever the middle number sits halfway '
        'between the outer two, like five, eight, and eleven. How many whole numbers from one up to a chosen '
        'ceiling can we keep without forming even a single evenly spaced trio? A classical base-three recipe drops '
        'every number whose ternary spelling uses the digit two, leaving a sparse fractal dust. Six years later, '
        'Raphaël Salem and Donald Spencer built much thicker progression-free sets. Four years after that, Felix '
        'Behrend placed multi-digit coordinates along the curved surface of a high-dimensional ball. A straight '
        'line pierces a sphere in at most two places, so three distinct shell points cannot line up. From above, '
        'Klaus Roth showed that dense sets contain trios, and modern computer-science tools narrowed the remaining gap.'
    ),
    'act1_body': (
        'Erdős and Turán opened this quantitative program in the Journal of the London Mathematical Society '
        '(1936, DOI 10.1112/jlms/s1-11.4.261), recording exact small values alongside the base-three zero-one '
        'construction attributed there to George Szekeres. Raphaël Salem and Donald Spencer (1942, DOI '
        '10.1073/pnas.28.12.561) refuted sub-linear power-law ceilings by constructing progression-free subsets '
        'growing faster than any fixed exponent below one. Four years later at the University of Melbourne, Felix '
        'Adalbert Behrend (1946, DOI 10.1073/pnas.32.12.331) replaced flat digit blocks with integer lattice '
        'points lying on a single Euclidean sphere. Projecting those coordinates through a wide radix silenced '
        'digit carries and yielded progression-free sets with sub-polynomial density loss.'
    ),
    'act1_stakes': (
        'Seven years after Behrend, Klaus Friedrich Roth (1953, DOI 10.1112/jlms/s1-28.1.104) adapted the Hardy and '
        'Littlewood circle method to obtain a reciprocal double-logarithmic upper density bound. '
        'Endre Szemerédi (1975, DOI 10.4064/aa-27-1-199-245) extended zero asymptotic density to progressions of '
        'every finite length. Decades later, Ben Green and Terence Tao (2008, DOI 10.4007/annals.2008.167.481; '
        'Scite records 909 citing publications and 6 supporting, 946 mentioning, and 1 contrasting classified '
        'citation statements, with zero retractions [observed: Scite ML citation classification, accessed '
        '2026-11-24]) found arbitrarily long progressions in the primes. Jean Bourgain (1999, DOI '
        '10.1007/s000390050105), Tom Sanders (2011, DOI 10.4007/annals.2011.174.1.20), and Thomas Bloom with Olof '
        'Sisask (2020, arXiv:2007.03528) sharpened the logarithmic denominator, before Zander Kelley and Raghu Meka '
        '(2023, DOI 10.1109/focs57990.2023.00059) obtained explicit quasi-polynomial decay at exponent one-twelfth, '
        'expounded by Bloom and Sisask (2023, DOI 10.2140/ent.2023.2.15) and refined to one-ninth in arXiv:2309.02353.'
    ),
    'pullquote': (
        '"A straight line pierces a round sphere in at most two points—and when an expanded radix silences digit '
        'carries, high-dimensional curvature hides dense sets with zero evenly spaced triples."'
    ),
    'chronology': [
        (
            '1936',
            'Paul Erdős and Pál Turán pose the density conjecture for arithmetic progressions and record Szekeres’s '
            'ternary zero-one baseline in the Journal of the London Mathematical Society (DOI 10.1112/jlms/s1-11.4.261).'
        ),
        (
            '1942 & 1946',
            'Raphaël Salem and Donald Spencer refute sub-linear power-law upper bounds (DOI 10.1073/pnas.28.12.561); '
            'Felix Behrend introduces carry-free spherical shells in Proceedings of the National Academy of Sciences '
            '(DOI 10.1073/pnas.32.12.331).'
        ),
        (
            '1953 & 1975',
            'Klaus Roth obtains a reciprocal double-logarithmic upper density bound via the continuous circle method '
            '(DOI 10.1112/jlms/s1-28.1.104); Endre Szemerédi settles general progression lengths combinatorially '
            '(DOI 10.4064/aa-27-1-199-245).'
        ),
        (
            '1999–2011',
            'Jean Bourgain introduces Bohr-set density increments (DOI 10.1007/s000390050105); Ben Green and Terence '
            'Tao find arbitrarily long progressions in the primes (DOI 10.4007/annals.2008.167.481); Michael '
            'Elkin (DOI 10.1007/s11856-011-0061-1) and Green with Julia Wolf (DOI 10.1007/978-0-387-68361-4_9) '
            'thicken Behrend’s shell; Tom Sanders nears the first-power logarithmic barrier (DOI 10.4007/annals.2011.174.1.20).'
        ),
        (
            '2020–2023',
            'Thomas Bloom and Olof Sisask cross the first-power logarithmic barrier in preprint arXiv:2007.03528; '
            'Zander Kelley and Raghu Meka obtain explicit one-twelfth quasi-polynomial bounds via physical-space '
            'sifting at FOCS (DOI 10.1109/focs57990.2023.00059, arXiv:2302.05537).'
        ),
        (
            '2023',
            'Bloom and Sisask publish a streamlined integer-interval exposition of Kelley–Meka’s one-twelfth bound '
            'in Essential Number Theory (DOI 10.2140/ent.2023.2.15) and post preprint arXiv:2309.02353 sharpening '
            'the upper log exponent to one-ninth.'
        ),
    ],
    'act2_title': 'Act II — Cross-Field Intuition: Porcelain Soup Bowls, Carry-Free Abacus Rods & Ripple Interference',
    'act2_analogy': (
        'Everyday analogy: Set glazed ceramic beads along a single horizontal water ring inside a round porcelain '
        'soup bowl. On a flat dinner plate, three beads easily line up because their midpoint stays flat on the '
        'plate. Inside the curved soup bowl, the straight chord joining any two distinct beads cuts through empty '
        'air rather than touching the porcelain wall. Next, record each bead’s coordinates on a wooden abacus '
        'whose rods hold nearly twice as many counters as you ever slide up. Adding two positions rod by rod then '
        'triggers zero carries into neighboring rods. Where the analogy stops: a kitchen bowl curves in three '
        'dimensions, whereas Behrend’s shells require growing dimension before overtaking the simpler base-three pattern.'
    ),
    'act2_plain_primer': (
        'Two integer sliders drive our workbench. Digit Bound runs from two up to eight, setting coordinate height '
        'and the expanded carry-free abacus radix. Shell Dimension sweeps two through six coordinates, carrying the '
        'interval past eleven million. Dragging either slider updates the first two readout cards, the shell curve, '
        'both comparison bars, the pigeonhole line, and the top status label, while the third and fourth readouts '
        'plus eight diagram captions stay fixed.'
    ),
    'distill_diagram': {
        'analogy_title': 'Curved Soup-Bowl Latitude Ring & Carry-Free Abacus',
        'analogy_sub': 'Chords between distinct ring beads pass inside the bowl; wide rods stop digit carries',
        'force_a_title': 'Behrend & Elkin Spherical Shell Floor',
        'force_a_sub': 'Modal shell S_m(R*²) in base 2d − 1 reaches sub-polynomial scale N exp(−c √(log N))',
        'force_b_title': 'Roth Circle Method & Kelley–Meka Sifting Ceiling',
        'force_b_sub': 'Harmonic density increments and Hölder physical-space sifting enforce N exp(−c′ (log N)^(1/9))',
        'threshold_title': 'Finite Cantor Regime vs Open Asymptotic Exponent Window',
        'threshold_pass': 'Exact small values: r_3(9) = 5, r_3(14) = 8, r_3(20) = 9, r_3(24) = 10; |B(5, 4)| = 30',
        'threshold_fail': 'Open asymptotic log-exponent gap β ∈ [1/9, 1/2] between upper sifting and lower spheres',
    },
    'act2_intuition': (
        'Let r_3(N) denote the largest cardinality |A| of a subset A ⊆ {1, …, N} containing no three distinct '
        'integers x, y, z with x + z = 2y. In the shifted ternary Cantor set C_3(N) = {1 + ∑_{i≥0} ε_i 3^i ≤ N : '
        'ε_i ∈ {0, 1}} (recorded from Szekeres in Erdős & Turán 1936), doubling y_i ∈ {0, 1} yields 2(y − 1) with '
        'digits restricted to {0, 2}, whereas (x − 1) + (z − 1) has digits in {0, 1, 2} that equal 0 only when '
        'x_i = z_i = 0 and equal 2 only when x_i = z_i = 1, forcing x = z = y without carries. That fractal '
        'benchmark gives |C_3(3^m)| = 2^m = N^(log_3 2) ≈ N^0.63093, yet small intervals already beat it: as '
        'recomputed by bitmask branch-and-bound in verify_m16_progression_bounds.py (and cross-checked by exhaustive '
        'power-set search through N = 14), C_3(N) matches r_3(N) at N = 1..8 and N = 10..19 (including r_3(14) = 8), '
        'but falls behind at N = 9 where {1, 2, 4, 8, 9} attains r_3(9) = 5 > |C_3(9)| = 4, and across N = 20..24 '
        'where {1, 2, 6, 7, 9, 14, 15, 18, 20} reaches r_3(20) = 9 > 8 and {1, 2, 5, 7, 11, 16, 18, 19, 23, 24} '
        'reaches r_3(24) = 10 > 8. Behrend (1946) generalized carry avoidance to m coordinates x ∈ {0, …, d − 1}^m '
        'encoded in base b = 2d − 1 via φ(x) = 1 + ∑_{i=0}^{m−1} x_i (2d − 1)^i ∈ {1, …, (2d − 1)^m}: because '
        '0 ≤ x_i + z_i ≤ 2d − 2 < b and 0 ≤ 2y_i ≤ 2d − 2 < b, integer equality φ(x) + φ(z) = 2φ(y) forces '
        'coordinatewise equality x + z = 2y in R^m. Restricting x to the modal Euclidean shell ‖x‖_2² = R*² among '
        'the m(d − 1)² + 1 possible radii 0, …, m(d − 1)² yields S_m(R*²) ≥ ⌈d^m / (m(d − 1)² + 1)⌉ points by '
        'pigeonhole, while the parallelogram identity ‖x‖_2² + ‖z‖_2² − 2‖(x + z)/2‖_2² = (1/2)‖x − z‖_2² > 0 for '
        'x ≠ z rules out every nontrivial midpoint y = (x + z)/2 on the same sphere.'
    ),
    'act2_deepening': (
        'In standard parameterizations of Behrend’s bound (our derivation following Behrend 1946), choosing '
        'm ≈ √(2 log_2 N) and 2d − 1 = ⌊N^(1/m)⌋ (so d ≈ (1/2) · 2^(√((1/2) log_2 N)) and (2d − 1)^m ≤ N) balances '
        'the carry penalty (d / (2d − 1))^m ≈ 2^(−m) against the quadratic-in-d shell divisor m(d − 1)² + 1, '
        'yielding r_3(N) ≥ N · 2^(−2√2 √(log_2 N) − O(log log N)); Elkin (2011, DOI 10.1007/s11856-011-0061-1) and '
        'Green with Wolf (2010, DOI 10.1007/978-0-387-68361-4_9) replaced a single sphere with a thin annulus to '
        'gain an extra Θ(√(log N)) factor while keeping exponent β = 1/2 inside exp(−c (log N)^β). Whereas Roth '
        '(1953, DOI 10.1112/jlms/s1-28.1.104) integrated continuous exponential sums on [0, 1] to bound r_3(N) = '
        'O(N / log log N), our verifier discretizes that orthogonality check onto the finite odd cyclic group Z_M '
        'of order M = 2N + 1: because 2 ≤ x + z ≤ 2N < M, congruence x + z ≡ 2y (mod M) coincides with integer '
        'equality x + z = 2y, and gcd(2, M) = 1 makes r ↦ 2r (mod M) a bijection. Writing Â(r) = ∑_{x∈A} '
        'e^(−2πi r x / M), character orthogonality yields T(A) = (1/M) ∑_{r=0}^{M−1} Â(r)² conj(Â(2r mod M)), '
        'where the complex square Â(r)² (never |Â(r)|², which counts x − z ≡ 2y) couples r to 2r. When A has no '
        'nontrivial 3-APs, T(A) = |A|; isolating r = 0 where Â(0) = |A| and applying Parseval ∑_{r=1}^{M−1} |Â(r)|² '
        '= |A|(M − |A|) gives our finite linear bias floor max_{r≠0} |Â(r)| ≥ ||A|² − M| / (M − |A|) alongside '
        'Parseval’s root-mean-square floor √(|A|(M − |A|)/(M − 1)). At N = 20 (M = 41, extremal |A| = 9), our '
        'script measures max_{r≠0} |Â(r)| = 5.146830 above both Parseval’s 2.683282 and the linear floor 1.250000 '
        '(the linear floor exceeds Parseval once (|A|² − M)² / (M − |A|)² > |A|(M − |A|) / (M − 1), at scale '
        '|A| ≫ M^(2/3)). '
        'After Bourgain (1999) and Sanders (2011) harvested multi-frequency Bohr sets, Kelley and Meka (2023, '
        'DOI 10.1109/focs57990.2023.00059) used Hölder decoupling, physical-space sifting, and spread subspaces to '
        'obtain exp(−c (log N)^(1/12)) N (c > 0), expounded at β = 1/12 by Bloom and Sisask (2023, DOI '
        '10.2140/ent.2023.2.15) and sharpened to β = 1/9 in preprint arXiv:2309.02353 (combined for N ≥ 3 with '
        'Behrend’s lower bound in our governing header).'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Ternary Coincidence at d = 2 and Carry Knockout at d = 3, m = 3): Slide Digit Bound to '
            'd = 2 and Shell Dimension to m = 3 (radix b = 3, ambient N = 27). Here B(2, 3) picks the unit-coordinate '
            'shell R*² = 1 of size 3 inside C_3(27) of size 8. Next step Digit Bound to d = 3 at m = 3 (b = 5, '
            'N = 125): the modal shell jumps to R*² = 5 with |B(3, 3)| = 6 permutation vectors {8, 12, 28, 36, 52, '
            '56} and zero nontrivial 3-APs—whereas our planted base-3 knockout collapses those same six vectors onto '
            '{6, 8, 12, 16, 20, 22}, creating two progressions of step 4.'
        ),
        (
            'Experiment 2 (Canonical Operating Point d = 5, m = 4 and Live vs. Fixed Readouts): Return to the '
            'canonical setting d = 5, m = 4 (radix b = 9, ambient N = 6,561). Dynamic programming updates Readouts '
            '1–2, the SVG shell curve (#tp-m16-shell-curve), modal and Cantor bars, pigeonhole line, dot, and top '
            'status line (#tp-m16-status-lbl), partitioning all 5^4 = 625 grid vectors across 65 radii R² ∈ [0, 64] '
            'with |B(5, 4)| = 30 on R*² = 18 versus pigeonhole floor 10; Readout 3 (small r_3 and N = 20 DFT peak '
            '5.15), Readout 4 (finite crossover status), and the eight reference SVG captions remain static.'
        ),
        (
            'Experiment 3 (High-Radix Scaling d = 8, m = 6 and the Finite-vs-Asymptotic Crossover): Push both '
            'sliders to their upper stops d = 8, m = 6 (radix b = 15, ambient N = 11,390,625). Across 295 shells '
            'partitioning 262,144 grid vectors, the modal sphere R*² = 103 holds |B(8, 6)| = 3,300 integers against '
            'pigeonhole floor 889 and ternary Cantor baseline |C_3(N)| = 32,768, illustrating why m must grow with '
            '√(log_2 N) before spherical curvature overtakes base-3 digit avoidance.'
        ),
    ],
    'act4_title': 'Act IV — Imagining Humanity’s Future: Physical-Space Decoupling, Finite Witnesses & Open Exponents',
    'act4_human_ai': (
        'Across additive combinatorics and theoretical computer science, Kelley and Meka’s 2023 physical-space '
        'argument connected pseudorandomness against low-depth communication protocols with classical number-theoretic '
        'density increments. Because their proof replaces delicate multi-dimensional Fourier inversion with '
        'elementary Hölder norm raising, convolution sifting, and subspace spreadness—expounded directly on integer '
        'intervals by Bloom and Sisask (2023, DOI 10.2140/ent.2023.2.15) alongside the additive-entropy tools of '
        'Polynomial Freiman–Ruzsa (Folio M.04) and cap-set polynomial methods (Folio M.03)—each algebraic reduction '
        'separates cleanly into checkable finite-group lemmas and explicit parameter schedules.'
    ),
    'act4_deepening': (
        'Under the Tier T0–T1 evidence discipline of this monograph, three epistemic layers remain strictly '
        'distinguished. First, our zero-dependency Python script skills/math/m16/verify_m16_progression_bounds.py '
        'recomputes exact r_3(1..24) (with independent power-set cross-checks through N = 14), materializes carry-free '
        'Behrend sets B(d, m) for d ∈ [2..5], m ∈ [2..4] to check zero nontrivial 3-APs directly, evaluates exact '
        'integer shell histograms across the full slider domain d ∈ [2..8], m ∈ [2..6], and checks the odd-modulus '
        'cyclic DFT identity T(A) = (1/M) ∑ Â(r)² conj(Â(2r mod M)) across N = 3..24 (max residual < 1.25 × 10⁻¹⁴, '
        'asserted < 10⁻¹²), failing deterministically under --planted-defect when base b = d, L¹ hyperplanes, '
        'conj(Â(r)), or step-1 omissions are injected. Second, the asymptotic bounds of Behrend (1946), Elkin '
        '(2011), Roth (1953), Bourgain (1999), Sanders (2011), Kelley & Meka (2023, exp(−c (log N)^(1/12)) N), and '
        'Bloom & Sisask (2023 Essential Number Theory β = 1/12 exposition; preprint arXiv:2309.02353 β = 1/9) are '
        'reported from their primary texts without re-deriving quasi-polynomial sifting in our finite script. Third, '
        'narrowing the gap between valid upper exponents (currently β = 1/9) and lower constructions (β = 1/2) '
        'inside exp(−c (log N)^β) N—and deciding whether spherical shells achieve the true asymptotic order—remains '
        'OPEN: any progression-free construction achieving exp(−c (log N)^β) N with β < 1/2 would beat spherical '
        'shells, while any density-increment bound with β > 1/9 narrows the frontier from above.'
    ),
    'cf_bridge': 'Extends M.03/M.04/M.15 · Strict Euclidean convexity, carry-free radix projection and sifting increments',
    'sources': [
        (
            'Erdös, P., & Turán, P. (1936). On Some Sequences of Integers. Journal of the London Mathematical '
            'Society, s1-11(4), 261–264. DOI: 10.1112/jlms/s1-11.4.261.'
        ),
        (
            'Salem, R., & Spencer, D. C. (1942). On Sets of Integers Which Contain No Three Terms in Arithmetical '
            'Progression. Proceedings of the National Academy of Sciences, 28(12), 561–563. '
            'DOI: 10.1073/pnas.28.12.561.'
        ),
        (
            'Behrend, F. A. (1946). On Sets of Integers Which Contain No Three Terms in Arithmetical Progression. '
            'Proceedings of the National Academy of Sciences, 32(12), 331–332. DOI: 10.1073/pnas.32.12.331.'
        ),
        (
            'Roth, K. F. (1953). On Certain Sets of Integers. Journal of the London Mathematical Society, s1-28(1), '
            '104–109. DOI: 10.1112/jlms/s1-28.1.104.'
        ),
        (
            'Szemerédi, E. (1975). On sets of integers containing k elements in arithmetic progression. Acta '
            'Arithmetica, 27, 199–245. DOI: 10.4064/aa-27-1-199-245.'
        ),
        (
            'Bourgain, J. (1999). On Triples in Arithmetic Progression. Geometric and Functional Analysis, 9(5), '
            '968–984. DOI: 10.1007/s000390050105.'
        ),
        (
            'Green, B., & Tao, T. (2008). The primes contain arbitrarily long arithmetic progressions. Annals of '
            'Mathematics, 167(2), 481–547. DOI: 10.4007/annals.2008.167.481.'
        ),
        (
            'Green, B., & Wolf, J. (2010). A Note on Elkin’s Improvement of Behrend’s Construction. In Additive '
            'Number Theory (pp. 141–144), Springer. DOI: 10.1007/978-0-387-68361-4_9.'
        ),
        (
            'Elkin, M. (2011). An improved construction of progression-free sets. Israel Journal of Mathematics, '
            '184, 93–128. DOI: 10.1007/s11856-011-0061-1.'
        ),
        (
            'Sanders, T. (2011). On Roth’s theorem on progressions. Annals of Mathematics, 174(1), 619–636. '
            'DOI: 10.4007/annals.2011.174.1.20.'
        ),
        (
            'Kelley, Z., & Meka, R. (2023). Strong Bounds for 3-Progressions. 2023 IEEE 64th Annual Symposium on '
            'Foundations of Computer Science (FOCS), 933–947 (preprint arXiv:2302.05537). '
            'DOI: 10.1109/focs57990.2023.00059.'
        ),
        (
            'Bloom, T. F., & Sisask, O. (2023). The Kelley–Meka bounds for sets free of three-term arithmetic '
            'progressions. Essential Number Theory, 2(1), 15–44 (see also preprints arXiv:2007.03528 and '
            'arXiv:2309.02353). DOI: 10.2140/ent.2023.2.15.'
        ),
        (
            'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations '
            'and classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
            '882–898. DOI: 10.1162/qss_a_00146.'
        ),
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Behrend spherical shell histogram '
        'in base 2d-1 compared against pigeonhole average, ternary Cantor baseline, and open log-exponent gap">\n'
        '            <line x1="48" y1="184" x2="352" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <line x1="48" y1="28" x2="48" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <text x="54" y="20" font-size="10.2" font-weight="600" fill="currentColor">Behrend Shell Histogram S_m(R²) vs. Cantor Baseline</text>\n'
        '            <path id="tp-m16-shell-curve" data-custom-curve="1" d="M 56 167 L 94 121 L 125 97 L 155 112 L 201 139 L 254 167 L 300 167" fill="none" stroke="var(--tp-verdigris)" stroke-width="2.3"/>\n'
        '            <line id="tp-m16-pigeon-line" x1="52" y1="124" x2="348" y2="124" stroke="var(--tp-minium)" stroke-width="1.6" stroke-dasharray="5,3"/>\n'
        '            <rect id="tp-m16-shell-bar" x="116" y="97" width="18" height="87" rx="2" fill="var(--tp-verdigris)" fill-opacity="0.45"/>\n'
        '            <rect id="tp-m16-cantor-bar" x="312" y="44" width="18" height="140" rx="2" fill="var(--tp-prussian)" fill-opacity="0.30"/>\n'
        '            <circle id="tp-m16-point" cx="125" cy="97" r="5.5" fill="var(--tp-prussian)"/>\n'
        '            <text x="56" y="40" font-size="8.8" fill="var(--tp-prussian)">Ternary C_3(N) (finite lead) vs. Modal B(d, m)</text>\n'
        '            <text x="56" y="55" font-size="8.6" fill="var(--tp-minium)">Dashed line: Pigeonhole floor ⌈d^m / #shells⌉</text>\n'
        '            <line x1="366" y1="24" x2="366" y2="192" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="378" y="20" font-size="10.2" font-weight="600" fill="currentColor">Odd-Modulus DFT &amp; Open β ∈ [1/9, 1/2]</text>\n'
        '            <rect x="378" y="34" width="286" height="44" rx="6" fill="var(--tp-stone)" fill-opacity="0.28" stroke="var(--tp-prussian)" stroke-width="1.6"/>\n'
        '            <text id="tp-m16-status-lbl" x="388" y="52" font-size="8.6" font-weight="600" fill="var(--tp-prussian)">d = 5, m = 4 (b = 9): |B| = 30 at R*² = 18 · C_3 = 256</text>\n'
        '            <text x="388" y="69" font-size="8.3" fill="var(--tp-verdigris)">Fixed ref: r_3(9)=5, r_3(14)=8, r_3(20)=9, r_3(24)=10</text>\n'
        '            <rect x="378" y="114" width="286" height="58" rx="6" fill="var(--tp-verdigris)" fill-opacity="0.12" stroke="var(--tp-verdigris)" stroke-width="1.4"/>\n'
        '            <text x="388" y="136" font-size="8.8" font-weight="600" fill="var(--tp-prussian)">Fixed Z_41 ref (N = 20): T(A) = 9 · max |Â(r)| = 5.15</text>\n'
        '            <text x="388" y="156" font-size="8.6" fill="var(--tp-minium)">Asymptotic gap: N exp(−c√log N) vs. N exp(−c′(log N)^(1/9))</text>\n'
        '            <text x="48" y="206" font-size="10" fill="var(--tp-verdigris)">Exact DP shells, r_3(1..24) &amp; cyclic Z_{2N+1} DFT · Recomputed offline by verify_m16_progression_bounds.py</text>\n'
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining what a tabletop optical and combinatorics bench for three-term '
        'progression-free sets would look like: a clear hemispherical borosilicate glass bowl in an unmarked '
        'brushed-brass ring holding cobalt-indigo and emerald-verdigris glass spheres along one horizontal latitude '
        'ring, beside an unnumbered five-rod walnut abacus with boxwood beads and a two-rod water ripple tank with '
        'interference fringes on cream vellum (artistic impression, not a measured physical apparatus; exact '
        'structure and specifications are kept strictly intact in the deterministic Plate below)'
    ),
    'caption': (
        'Conceptual Vision Plate M.16-V (Imagining What It Would Look Like) · Conceptual visualization imagining '
        'what a curved glass bowl holding latitude-ring spheres beside an unnumbered carry-free walnut abacus and '
        'a two-source ripple tank would look like (artistic impression, not a measured structure or specification; '
        'exact structure and specifications are kept strictly intact in the deterministic Plate below).'
    ),
}

DISPATCH = {
    'kicker': 'FRONTIER ADDITIVE COMBINATORICS DISPATCH · BEHREND SPHERES & KELLEY–MEKA SIFTING',
    'headline': 'Closing Seventy Years Between Roth’s Circle Method and Quasi-Polynomial 3-AP Bounds',
    'body': (
        'Seventy years after Klaus Roth (1953, DOI 10.1112/jlms/s1-28.1.104) established r_3(N) = O(N / log log N), '
        'Zander Kelley and Raghu Meka (2023, DOI 10.1109/focs57990.2023.00059, arXiv:2302.05537) bypassed high-order '
        'Fourier inversion via physical-space Hölder decoupling and sifting to establish r_3(N) ≤ '
        'exp(−c (log N)^(1/12)) N, expounded by Thomas Bloom and Olof Sisask (2023, DOI 10.2140/ent.2023.2.15) and '
        'sharpened to exponent 1/9 in preprint arXiv:2309.02353 toward Behrend’s 1946 spherical-shell exponent β = 1/2.'
    ),
}

META_3D = (
    'Behrend Spherical-Shell Concentration & Odd-Modulus Cyclic Fourier Ripple Landscape',
    'X: Digit Bound d & Radix 2d − 1 · Z: Shell Radius Offset R² − R*² · Y: Log₁₀ Shell Density & Harmonic Mode',
)

ES_TRANSLATION = {
    'title_es': (
        'Progresiones Aritméticas de Tres Términos: Esferas de Behrend, Sesgo de Fourier y Cotas de Kelley–Meka'
    ),
    'subtitle_es': (
        'Cómo Paul Erdős y Pál Turán preguntaron si la densidad positiva fuerza tres enteros equiespaciados, cómo '
        'Felix Behrend ocultó conjuntos densos en esferas de alta dimensión, cómo Klaus Roth usó ondas armónicas y '
        'cómo Zander Kelley y Raghu Meka alcanzaron cotas cuasi-polinomiales.'
    ),
    'why_es': (
        'Una recta corta una esfera en a lo más dos puntos: al codificar coordenadas esféricas en una base amplia '
        'sin acarreos, emergen conjuntos sorprendentemente densos sin ningún trío equiespaciado.'
    ),
    'plain_es': (
        'En palabras sencillas, tres enteros forman un trío equiespaciado cuando el número central queda justo a '
        'mitad de camino entre los extremos, como cinco, ocho y once. ¿Cuántos números desde uno hasta un tope '
        'elegido podemos conservar sin formar ni un solo trío equiespaciado? Una receta clásica en base tres '
        'descarta todo número cuya escritura ternaria use el dígito dos, dejando un polvo fractal disperso. Seis '
        'años después, Raphaël Salem y Donald Spencer construyeron conjuntos libres de progresiones más densos. '
        'Cuatro años más tarde, Felix Behrend colocó coordenadas de varios dígitos sobre un cascarón esférico de '
        'alta dimensión. Una recta corta una esfera en a lo más dos sitios, así que tres puntos distintos del '
        'cascarón jamás quedan alineados. Desde arriba, Klaus Roth mostró que los conjuntos densos contienen tríos, '
        'y herramientas recientes de ciencias de la computación estrecharon la brecha restante.'
    ),
    'deep_es': (
        'Para subconjuntos A ⊆ {1, …, N} sin progresiones no triviales x + z = 2y, Erdős y Turán (1936, '
        'DOI 10.1112/jlms/s1-11.4.261) introdujeron r_3(N) y registraron el conjunto ternario de Szekeres, escrito '
        'aquí C_3(N) de escala N^(log_3 2) ≈ N^0.63093. Nuestro script fuera de línea recomputa r_3(1..24) (con '
        'r_3(9) = 5 > |C_3(9)| = 4, r_3(14) = 8, r_3(20) = 9 y r_3(24) = 10) y evalúa los cascarones esféricos de '
        'Behrend (1946, DOI 10.1073/pnas.32.12.331; refinados por Elkin 2011, DOI 10.1007/s11856-011-0061-1, y '
        'Green & Wolf 2010, DOI 10.1007/978-0-387-68361-4_9) en base b = 2d − 1, donde 0 ≤ x_i + z_i ≤ 2d − 2 < b '
        'impide acarreos y toda cuerda recta entre dos puntos distintos cae en el interior estricto de la esfera '
        '(dando |B(5, 4)| = 30 en R*² = 18 dentro de N = 6,561; al mover los controles se actualizan las dos '
        'primeras tarjetas, las curvas, las barras y el estado superior, mientras la tercera tarjeta con pico 5.15 '
        'en N = 20, la cuarta tarjeta y ocho leyendas permanecen fijas). Mientras Roth (1953, DOI '
        '10.1112/jlms/s1-28.1.104) probó O(N / log log N) con el método continuo del círculo, este folio discretiza '
        'la ortogonalidad en el grupo cíclico impar Z_{2N+1} mediante T(A) = (1/M) ∑ Â(r)² conj(Â(2r mod M)); por '
        'su parte, Kelley y Meka (2023, DOI 10.1109/focs57990.2023.00059) obtuvieron exp(−c (log N)^(1/12)) N '
        'mediante cribado en espacio físico, expuesto en β = 1/12 por Bloom y Sisask (2023, DOI '
        '10.2140/ent.2023.2.15) y afinado a β = 1/9 en el preprint arXiv:2309.02353, dejando abierta β ∈ [1/9, 1/2].'
    ),
    'bridge_es': (
        'Extiende M.03, M.04 y M.15 a progresiones aritméticas de tres términos: recomputa r_3(1..24), cascarones '
        'esféricos de Behrend sin acarreos en base 2d − 1 e identidades cíclicas de Fourier en Z_{2N+1}, marcando '
        'abierta la brecha asintótica β ∈ [1/9, 1/2].'
    ),
}
