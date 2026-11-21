#!/usr/bin/env python3
"""Folio M.14 (MATH): Sphere Packing, Cohn-Elkies Linear Programming Bounds & E8/Leech Lattices."""
from __future__ import annotations

SLUG = 'm14'

PILLAR = 'math'

_SCITE = {
    'doi': '10.4007/annals.2003.157.689',
    'fetched_on': '2026-11-21',
    'citing_publications': 377,
    'supporting': 3,
    'mentioning': 541,
    'contrasting': 0,
    'retracted': False,
    'summary': (
        'Scite Smart Citation Index entry for Cohn & Elkies 2003, "New upper bounds on sphere packings I" '
        '(Annals of Mathematics, DOI 10.4007/annals.2003.157.689), fetched 2026-11-21: 377 citing publications '
        '(3 supporting, 541 mentioning, 0 contrasting) and no retraction notice. '
        'These counts describe that foundational paper, not this folio.'
    ),
}

FOLIO = {
    'folio_id': 'M.14',
    'slug': 'm14',
    'pillar': 'math',
    'category_code': 'M',
    'parent_folios': ['M.09', 'M.12'],
    'lineage_mode': 'SYNTHESIS · Synthesizes M.09 Energy Transport & M.12 Lattice Geometry',
    'title': 'Sphere Packing in Dimensions 3, 4, 8 & 24: Cohn–Elkies Bounds, Modular Functions & Open Gaps',
    'subtitle': (
        'Synthesizing Folio M.09 energy transport and Folio M.12 lattice geometry: how Henry Cohn and Noam Elkies '
        'turned sphere packing into Fourier linear programming, how Maryna Viazovska and collaborators closed '
        'dimensions 8 and 24 via modular forms, and why dimension 4 and asymptotic space remain open.'
    ),
    'date_published': '2026-11-21',
    'date_redated': '2026-11-21',
    'current_edition': 'REV 1.0',
    'status_badge': 'SPHERE PACKING & LP BOUNDS · REV 1.0',
    'primary_kernel': 'skills/math/m14/verify_m14_sphere_packing.py',
    'governing_law': 'Δ_d ≤ Vol(B_d(r_cut/2)) · f(0)/f̂(0) · f(x) ≤ 0 (|x| ≥ r_cut) · f̂(t) ≥ 0 · Δ_8 = π⁴/384 · Δ_24 = π¹²/12!',
    'colophon': {
        'identifier': 'M.14 · Sphere Packing, Cohn–Elkies LP & Open Gaps · REV 1.0',
        'kernels': 'Laguerre–Gaussian Fourier Eigenbasis · Descartes Shift Check · Golay G_24 Leech Enumeration',
        'benchmarks': (
            'Offline model values: Δ_8(E_8) = 0.253670 (τ_8 = 240; deg-5 LP 0.303541) · '
            'Δ_24(Λ_24) = 0.001930 (τ_24 = 196,560; deg-5 LP 0.008955) · d=4 open gap (0.616850 vs 0.672477)'
        ),
        'bridge': 'Synthesizes M.09/M.12',
    },
    'sliders': [
        {
            'label': 'Euclidean Dimension (d)',
            'min': 2,
            'max': 24,
            'step': 1,
            'value': 8,
            'unit': 'd = ',
        },
        {
            'label': 'Laguerre Polynomial Degree (M)',
            'min': 3,
            'max': 5,
            'step': 2,
            'value': 5,
            'unit': 'M = ',
        },
    ],
    'steps': [
        (
            'Stage 1 (Lattice Geometry & Kissing Numbers from d = 2 to d = 24): Packing equal spheres in Euclidean space '
            'asks what fraction of volume non-overlapping balls can fill. In dimension 2 the hexagonal lattice A_2 fills '
            'π/√12 ≈ 0.906900 with 6 neighbors; in dimension 3, Hales et al. (2017, DOI 10.1017/fmp.2017.1) completed '
            'the formal Flyspeck check of the Kepler conjecture at π/(3√2) ≈ 0.740480 with 12 neighbors. In dimension 4, '
            'the checkerboard lattice D_4 has density π²/16 ≈ 0.616850 and Musin (2008, DOI 10.4007/annals.2008.168.1) '
            'settled the kissing number at τ_4 = 24, yet packing optimality in dimension 4 remains open.'
        ),
        (
            'Stage 2 (Cohn–Elkies Fourier Linear Programming Duality): Cohn and Elkies (2003, DOI 10.4007/annals.2003.157.689) '
            'showed that any radial Schwartz function f with f(0) = f̂(0) > 0, dual non-negativity f̂(t) ≥ 0 everywhere, '
            'and primal non-positivity f(x) ≤ 0 for |x| ≥ r_cut yields an upper bound Δ_d ≤ Vol(B_d(r_cut/2)) · f(0)/f̂(0) '
            'via the Poisson summation formula. Writing f in the Fourier eigenbasis ψ_k(x) = L_k^(d/2−1)(2π|x|²) exp(−π|x|²) '
            'with exact eigenvalue (−1)^k lets our offline verifier construct rational Laguerre–Gaussian test polynomials '
            'whose shifted polynomial P(u_cut + w) has every coefficient ≤ 0.'
        ),
        (
            'Stage 3 (Viazovska’s Modular Magic Functions in d = 8 and d = 24): In 2017, Viazovska (DOI 10.4007/annals.2017.185.3.7) '
            'constructed an infinite modular-form eigenfunction matching the E_8 root lattice (τ_8 = 240, Δ_8 = π⁴/384 ≈ 0.253670) '
            'with double roots at every non-minimal shell √(2k). Days later, Cohn, Kumar, Miller, Radchenko, and Viazovska '
            '(DOI 10.4007/annals.2017.185.3.8) extended the modular construction to the 24-dimensional Leech lattice Λ_24 '
            '(Δ_24 = π¹²/12! ≈ 0.001930, τ_24 = 196,560 minimal vectors built from the 759 octads of the extended binary '
            'Golay code G_24), and later established universal optimality across radial potentials (2022, DOI 10.4007/annals.2022.196.3.3).'
        ),
        (
            'Stage 4 (Open Hypothesis, Tier T0–T2, and Falsification Condition): Hypothesis (Tier T0–T2): finite-degree '
            'Laguerre–Gaussian test functions shrink the Cohn–Elkies upper bound monotonically from degree 3 to degree 5 '
            '(0.346486 → 0.303541 in d = 8; 0.087466 → 0.008955 in d = 24; 0.700415 → 0.672477 in d = 4), yet leave '
            'a roughly 9.0% gap above D_4 in dimension 4 while recent preprints push high-dimensional lower bounds upward '
            'via graph independence (arXiv:2312.10026) and stochastic ellipsoids (arXiv:2504.05042). This polynomial gap '
            'hypothesis would be falsified if an explicit non-lattice packing in dimension 4 exceeded π²/16 or if an '
            'admissible degree-5 Laguerre polynomial dropped below 0.616850; our deterministic checks inspect finite '
            'dimensions only and do not re-derive the asymptotic preprint bounds.'
        ),
    ],
    'readouts': [
        {'label': 'Lattice Packing Density (Δ_d)', 'value': '0.253670 (E_8, π^4/384, τ = 240)'},
        {'label': 'Laguerre Cohn–Elkies Bound (M = 5)', 'value': '0.303541 (r_cut = 1.6683, model)'},
        {'label': 'Polynomial-to-Lattice Ratio', 'value': '1.1966x (Viazovska modular limit: 1.0000x)'},
        {'label': 'Dimension Optimality Status', 'value': 'E_8 MATCHED BY VIAZOVSKA LP LIMIT (d = 8)'},
    ],
    'spec_plate': {
        'division': 'COMBINATORIAL & HARMONIC GEOMETRY / COHN–ELKIES LINEAR PROGRAMMING',
        'title': 'Exact Rational Laguerre–Gaussian Bounds, E_8 & Golay G_24 Leech Lattice Enumeration',
        'body': (
            'Offline verification specification: under the Fourier transform f̂(t) = ∫ f(x) exp(−2πi x·t) dx, radial '
            'eigenfunctions L_k^(d/2−1)(2π|x|²) exp(−π|x|²) carry eigenvalue (−1)^k. Setting P̂(u) = (u + α)∏(u − s_j)² '
            'in exact rational arithmetic guarantees f̂(t) ≥ 0, while checking that every coefficient of shifted '
            'P(u_cut + w) is ≤ 0 establishes f(x) ≤ 0 for |x| ≥ r_cut. Finite-degree bounds (M = 3, 5) strictly bound '
            'lattice densities from above without reaching the infinite modular-form optimum.'
        ),
        'meta': (
            'Primary anchors: Rogers 1958 (DOI 10.1112/plms/s3-8.4.609) · Cohn & Elkies 2003 '
            '(DOI 10.4007/annals.2003.157.689) · Musin 2008 (DOI 10.4007/annals.2008.168.1) · '
            'Viazovska 2017 (DOI 10.4007/annals.2017.185.3.7) · CKMRV 2017 (DOI 10.4007/annals.2017.185.3.8)'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE M.14-A · FOURIER EIGENVALUE PARITY & WHY ODD POLYNOMIAL DEGREE MATTERS',
        'body': (
            'In the Laguerre–Gaussian radial basis ψ_k(x) = L_k^(d/2−1)(2π|x|²) exp(−π|x|²), even-index modes have '
            'Fourier eigenvalue +1 while odd-index modes have eigenvalue −1. Choosing an odd-degree dual polynomial '
            'P̂(u) = (u + α)∏(u − s_j)² keeps P̂(u) ≥ 0 everywhere on [0, ∞) via positive leading term +u^(2m+1), '
            'while the (−1)^(2m+1) flip drives the primal polynomial P(u) → −∞ as u → ∞ so f(x) ≤ 0 holds past r_cut.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE M.14-B · FROM THE 24-BIT GOLAY CODE G_24 TO 196,560 LEECH SPHERES',
        'body': (
            'The Leech lattice Λ_24 achieves density π¹²/12! ≈ 0.001930 without a single root vector of squared norm 2. '
            'Its 196,560 minimal vectors of squared norm 4 (unscaled norm² = 32 in (1/√8) ℤ²⁴ coordinates) decompose '
            'cleanly via the 4,096 codewords of the extended binary Golay code G_24: 1,104 Type A vectors of shape '
            '((±4)², 0²²), 97,152 octad vectors from 759 weight-8 codewords (759 × 2⁷), and 98,304 parity vectors of '
            'shape ((±1)²³, ∓3) (24 × 2¹²), verified by direct codeword enumeration in verify_m14_sphere_packing.py.'
        ),
    },
    'skill': {
        'filename': 'sphere-packing-cohn-elkies-SKILL.md',
        'name': 'sphere-packing-cohn-elkies',
        'description': (
            'AI-agnostic harmonic analysis and lattice geometry skill for Cohn-Elkies Fourier linear programming '
            'bounds, Laguerre-Gaussian radial eigenfunctions, E8 and Leech lattice kissing counts, and open packing gaps.'
        ),
        'rules': [
            (
                'Fix the Fourier normalization f_hat(t) = integral f(x) exp(-2*pi*i x.t) dx so the radial eigenfunctions '
                'L_k^(d/2 - 1)(2*pi*|x|^2) exp(-pi*|x|^2) carry exact eigenvalue (-1)^k.'
            ),
            (
                'Check primal non-positivity f(x) <= 0 for |x| >= r_cut algebraically in exact rational arithmetic by '
                'checking that every coefficient of the shifted polynomial P(u_cut + w) is <= 0.'
            ),
            (
                'Distinguish settled kissing numbers from open packing densities: Musin (2008) settled tau_4 = 24 in '
                'dimension 4, while optimal sphere packing density Delta_4 >= pi^2/16 remains open.'
            ),
            (
                'Report asymptotic lower-bound preprints (Campos et al. arXiv:2312.10026; Klartag arXiv:2504.05042) as '
                'unrefereed high-dimensional scaling bounds separate from fixed-dimension finite checks.'
            ),
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.0',
            'date': '2026-11-21',
            'summary': (
                'REV 1.0 (Published 2026-11-21): Volume VII Mathematics monograph covering Rogers (1958), Cohn–Elkies '
                'Fourier linear programming (2003), Musin 4D kissing number (2008), Viazovska E_8 (2017), CKMRV Leech '
                'lattice & universal optimality (2017, 2022), Hales et al. Flyspeck (2017), and open dimension-4 and '
                'asymptotic packing gaps.'
            ),
            'opus': (
                'Verification note: all seven primary DOIs were checked against Crossref and Scite on 2026-11-21 with '
                'zero retraction notices; exact rational Laguerre–Gaussian bounds, Golay G_24 weight enumerator '
                'counts, and root-lattice kissing numbers are recomputed offline by '
                'skills/math/m14/verify_m14_sphere_packing.py.'
            ),
        }
    ],
    'volume': 7,
    'volume_code': 'VOL. 07',
    'reading_time': '22 MIN READ',
    'word_count': '4,600 WORDS',
    'scite': dict(_SCITE),
}

LONGFORM_DATA = {
    'reading_time': '22 MIN READ',
    'word_count': '4,600 WORDS',
    'parent_folios': ['M.09', 'M.12'],
    'lineage_mode': 'SYNTHESIS · Synthesizes M.09 Energy Transport & M.12 Lattice Geometry',
    'scite': dict(_SCITE),
    'act1_title': 'Act I — Cool Fact & Human Story: Why Cannonballs Stack Cleanly in Three Dimensions Yet Hide Secret Crystals in Eight and Twenty-Four',
    'act1_dropcap': (
        'Walk into any corner grocery store and watch how oranges sit in a wooden crate: staggered rows nestle into '
        'each other so neatly that a child can stack them without a ruler. Johannes Kepler conjectured in sixteen '
        'eleven that no arrangement of identical spheres in three dimensions can beat that pyramid stacking density of '
        'about seventy-four percent, yet four hundred years passed before mathematicians finished checking every tricky '
        'local cluster. Stranger still, as you add extra spatial dimensions, spheres shrink into narrow corners and '
        'nearly all space becomes empty gap. Out of that wilderness emerge two miraculous crystal lattices in eight and '
        'twenty-four dimensions where spheres lock together with uncanny symmetry. In twenty sixteen, Maryna Viazovska '
        'found a smooth radial test wave built from modular functions that locked eight dimensions shut, and days later '
        'a five-author team locked twenty-four dimensions too.'
    ),
    'act1_plain_bridge': (
        'In plain words, sphere packing asks how tightly you can cram identical marbles into a huge room without '
        'squashing any of them. On a flat tabletop, coins pack best in a honeycomb, leaving nine percent empty space. '
        'In our familiar three-dimensional room, stacked grocer pyramids fill seventy-four percent of the box. In '
        'four dimensions, where each marble can touch twenty-four neighbors at once, mathematicians still do not know '
        'whether a disordered arrangement might beat the neatest grid. Yet in eight and twenty-four dimensions, two '
        'exceptionally symmetric grids suddenly fit together so cleanly that a clever mathematical ruler rules out any '
        'denser arrangement. That ruler converts a geometric puzzle into a balance scale between real-space waves and '
        'their frequency spectra. Checking the ruler gives honest upper limits in any dimension, while leaving the '
        'four-dimensional race wide open.'
    ),
    'act1_body': (
        'The modern analytical turn began in 2003, when Henry Cohn and Noam Elkies published a Fourier linear programming '
        'bound in Annals of Mathematics (DOI 10.4007/annals.2003.157.689). Instead of tracking individual sphere positions, '
        'they asked for a single smooth radial function f whose Fourier transform f̂ stays non-negative everywhere while f '
        'turns non-positive beyond a cutoff radius r_cut. By Poisson summation over any periodic packing, that one '
        'function bounds density across all packings from above. Earlier, C. A. Rogers (1958, Proceedings of the London '
        'Mathematical Society, DOI 10.1112/plms/s3-8.4.609) bounded high-dimensional packing using simplex geometry, '
        'while Thomas Hales and the Flyspeck collaboration (2017, Forum of Mathematics, Pi, DOI 10.1017/fmp.2017.1) '
        'completed a formal machine-checked proof of the 3-dimensional Kepler conjecture. Meanwhile, Oleg Musin (2008, '
        'Annals of Mathematics, DOI 10.4007/annals.2008.168.1) settled the 4-dimensional kissing number at twenty-four.'
    ),
    'act1_stakes': (
        'In dimension 8, Viazovska (2017, Annals of Mathematics, DOI 10.4007/annals.2017.185.3.7) solved the Cohn–Elkies '
        'dual problem explicitly via weakly holomorphic modular forms, matching the E_8 lattice density π⁴/384 (around '
        '0.253670) and 240 touching neighbors. Within days, Cohn, Kumar, Miller, Radchenko, and Viazovska (2017, Annals of '
        'Mathematics, DOI 10.4007/annals.2017.185.3.8) matched the 24-dimensional Leech lattice Λ_24 at density '
        'π¹²/12! (around 0.001930) and 196,560 minimal vectors. Five years later, the same team (2022, Annals of '
        'Mathematics, DOI 10.4007/annals.2022.196.3.3) established universal optimality of E_8 and Λ_24 across all '
        'completely monotonic radial pair potentials—connecting optimal geometry directly back to energy-minimizing '
        'transport (Folio M.09) and error-correcting lattice codes (Folio M.12).'
    ),
    'pullquote': (
        '"Cohn and Elkies replaced an uncountable jungle of sphere configurations with one Fourier sign condition; '
        'Viazovska’s modular functions made that bound touch E_8 and Leech, leaving dimension 4 tantalizingly open."'
    ),
    'chronology': [
        (
            '1958',
            'C. A. Rogers establishes simplex upper bounds on equal-sphere packing density across general dimension d '
            '(Proceedings of the London Mathematical Society, DOI 10.1112/plms/s3-8.4.609).'
        ),
        (
            '2003',
            'Henry Cohn and Noam Elkies formulate the Fourier linear programming upper bound for sphere packings and '
            'show numerically that it comes within 10^−6 of E_8 and Λ_24 (Annals of Mathematics, DOI 10.4007/annals.2003.157.689).'
        ),
        (
            '2008',
            'Oleg R. Musin extends Delsarte’s linear programming polynomial method to settle the 4-dimensional kissing '
            'number at τ_4 = 24, matching the D_4 root lattice (Annals of Mathematics, DOI 10.4007/annals.2008.168.1).'
        ),
        (
            '2017',
            'Thomas Hales and the Flyspeck team publish a formal machine-checked proof of the 3-dimensional Kepler '
            'conjecture (Forum of Mathematics, Pi, DOI 10.1017/fmp.2017.1).'
        ),
        (
            '2017',
            'Maryna Viazovska settles 8-dimensional sphere packing (Δ_8 = π⁴/384, DOI 10.4007/annals.2017.185.3.7), and '
            'Cohn, Kumar, Miller, Radchenko, and Viazovska settle dimension 24 (Δ_24 = π¹²/12!, DOI 10.4007/annals.2017.185.3.8).'
        ),
        (
            '2022–2025',
            'CKMRV establish universal optimality of E_8 and Λ_24 (DOI 10.4007/annals.2022.196.3.3), while recent preprints '
            'improve high-dimensional lower bounds to (1 − o(1)) d log d / 2^(d+1) (arXiv:2312.10026) and lattice density '
            'c · d² · 2^−d (arXiv:2504.05042).'
        ),
    ],
    'act2_title': 'Act II — Cross-Field Intuition: Weighted Acoustic Chimes, Fourier Eigenvalues & The Dimension-4 Gap',
    'act2_analogy': (
        'Everyday analogy: Think of striking a bell in a stone courtyard and listening to both the ripples across the '
        'floor and the pure frequencies humming in the air. If you shape the bell’s rim so every overtone in the air '
        'stays non-negative while the floor wave sinks below zero past one yard, no repeating arrangement of pillars '
        'can crowd closer than the first zero crossing. In eight and twenty-four dimensions, Viazovska’s modular bells '
        'ring so cleanly that every overtone zero aligns with a crystal lattice shell; in four dimensions, polynomial '
        'bells still ring slightly off-key, leaving room between the four-dimensional checkerboard lattice and the lowest known roof.'
    ),
    'act2_plain_primer': (
        'Our interactive harmonic-geometry workbench exposes two parameters computed offline by our rational verifier. '
        'The first slider selects Euclidean Dimension d (from 2 to 24), comparing known lattice benchmarks (A_2, D_3, D_4, '
        'E_8, and Leech Λ_24) against Rogers-type high-dimensional trends and flagging dimension 4 where optimality is open. '
        'The second slider selects Laguerre Polynomial Degree M (degree 3 versus degree 5) in the exact Fourier eigenbasis '
        'L_k^(d/2−1)(2π|x|²) exp(−π|x|²). Raising M from 3 to 5 adds a second double zero to the spectrum f̂(t), pulling the '
        'upper bound down from 0.346486 to 0.303541 in d = 8 and from 0.087466 to 0.008955 in d = 24.'
    ),
    'distill_diagram': {
        'analogy_title': 'Primal Radial Cutoff vs. Dual Non-Negative Spectrum',
        'analogy_sub': 'Odd Laguerre modes flip sign under Fourier transform: ψ̂_k(t) = (−1)^k ψ_k(t)',
        'force_a_title': 'Euclidean Dimension (d = 2..24)',
        'force_a_sub': 'Exponential volume decay ~ 2^−d separates dense low-d lattices from open dimension 4 and asymptotic space',
        'force_b_title': 'Laguerre Polynomial Degree (M = 3, 5)',
        'force_b_sub': 'Adding squared dual zeros (u − s_j)² tightens the Cohn–Elkies ratio f(0)/f̂(0) toward the lattice limit',
        'threshold_title': 'Cohn–Elkies Admissibility Check',
        'threshold_pass': 'Dimension matched or admissible upper bound: f̂(t) ≥ 0 everywhere and P(u_cut + w) ≤ 0',
        'threshold_fail': 'Open density gap (d = 4 or non-magic d): polynomial LP roof sits strictly above lattice Δ_d',
    },
    'act2_intuition': (
        'Fix the Fourier transform convention f̂(t) = ∫ f(x) exp(−2πi x·t) dx on ℝ^d. With radial coordinate u = 2π|x|², '
        'the generalized Laguerre–Gaussian functions ψ_k(x) = L_k^(d/2−1)(u) exp(−u/2) are exact radial eigenfunctions '
        'of the d-dimensional Fourier transform with eigenvalue (−1)^k. Therefore, choosing a dual polynomial P̂(u) = '
        '(u + α)∏(u − s_j)² of odd degree M = 2m + 1 (with α > 0 and real double roots s_j > 0) automatically enforces '
        'f̂(t) ≥ 0 everywhere on ℝ^d. Expanding P̂(u) in the Laguerre basis and flipping the sign of every odd-index '
        'coefficient yields P(u), whose leading term −u^(2m+1) turns negative beyond a rational root bound u_cut.'
    ),
    'act2_deepening': (
        'Because u_cut = 2π r_cut² is rational, every π cancels in the ball volume factor for even dimensions d: '
        'Vol(B_d(r_cut/2)) = (u_cut/8)^(d/2) / (d/2)!. Our offline verifier checks P(0) > 0, checks P̂(u) ≥ 0, and '
        'expands the shifted polynomial P(u_cut + w) in exact Fraction arithmetic to verify that every coefficient is ≤ 0 '
        '(with leading coefficient < 0). That symbolic Descartes check establishes f(x) ≤ 0 for all |x| ≥ r_cut without '
        'floating-point sampling gaps. In d = 4, degree-5 Laguerre bounds tighten the upper roof from 0.700415 to '
        '0.672477, still 9.02% above D_4’s density π²/16 ≈ 0.616850—illustrating why finite polynomials alone do not '
        'close the gap without Viazovska’s infinite modular-form interpolation.'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Degree-3 vs. Degree-5 Tightening in Dimension 8): Start at d = 8 and toggle Laguerre Degree M '
            'between 3 and 5. Watch the Cohn–Elkies upper bound tighten from 0.346486 (1.3659× E_8) down to 0.303541 '
            '(1.1966× E_8), approaching Viazovska’s modular-form limit at π⁴/384 = 0.253670.'
        ),
        (
            'Experiment 2 (Inspecting the Open Dimension-4 Gap): Slide Euclidean Dimension d down to 4. Notice that Musin '
            '(2008) settled the kissing number τ_4 = 24, yet D_4 density π²/16 = 0.616850 remains 9.02% below our degree-5 '
            'polynomial bound 0.672477—and the status readout flags dimension 4 as open.'
        ),
        (
            'Experiment 3 (Golay G_24 & Dimension 24 Leech Jump): Slide Dimension d up to 24 and compare M = 3 (0.087466, '
            '45.3× Leech) against M = 5 with roots near the first two Leech shells (0.008955, 4.64× Leech), alongside '
            'the 4-Lens Observatory tabs (3D Surface, Phase Portraits, Kirchhoff Ribbon, Polar Radar).'
        ),
    ],
    'act4_title': 'Act IV — Imagining Humanity’s Future: Error-Correcting Codes, Post-Quantum Lattices & Open High-Dimensional Frontiers',
    'act4_human_ai': (
        'Sphere packing is far more than stacking marbles: every vector of a dense packing in d dimensions is a '
        'codeword separated from every neighbor by a fixed Euclidean distance. The 8-dimensional E_8 root system and the '
        '24-dimensional Leech lattice—built directly from the 4,096 codewords and 759 octads of the extended binary '
        'Golay code G_24—underpin classical modulation codes and benchmark modern lattice cryptography (Folio M.12). '
        'Making the Fourier linear programming bound inspectable in pure rational arithmetic lets students, '
        'mathematicians, and automated verifiers separate settled optimal dimensions from genuine open problems.'
    ),
    'act4_deepening': (
        'This folio frames an explicit Tier T0–T2 mathematical hypothesis: while finite-degree Laguerre–Gaussian '
        'polynomials tighten monotonically from M = 3 to M = 5 across dimensions 4, 8, and 24, closing the gap in '
        'dimensions outside {1, 2, 3, 8, 24} requires either new infinite modular/quasimodular ansätze or non-LP '
        'constructions—and recent breakthroughs by Campos, Jenssen, Michelen, and Sahasrabudhe (arXiv:2312.10026, '
        'asymptotic lower bound (1 − o(1)) d log d / 2^(d+1)) and Bo’az Klartag (arXiv:2504.05042, stochastic ellipsoid '
        'lattice lower bound c · d² · 2^−d) remain unrefereed preprints outside our finite-dimensional offline checks. '
        'Any admissible finite-degree Laguerre polynomial dropping below π²/16 in d = 4 would falsify D_4’s conjecture.'
    ),
    'cf_bridge': 'Synthesizes M.09/M.12',
    'sources': [
        (
            'Rogers, C. A. (1958). The Packing of Equal Spheres. Proceedings of the London Mathematical Society, s3-8(4), '
            '609–620. DOI: 10.1112/plms/s3-8.4.609.'
        ),
        (
            'Cohn, H., & Elkies, N. (2003). New upper bounds on sphere packings I. Annals of Mathematics, 157(2), '
            '689–714. DOI: 10.4007/annals.2003.157.689.'
        ),
        (
            'Musin, O. R. (2008). The kissing number in four dimensions. Annals of Mathematics, 168(1), 1–32. '
            'DOI: 10.4007/annals.2008.168.1.'
        ),
        (
            'Viazovska, M. S. (2017). The sphere packing problem in dimension 8. Annals of Mathematics, 185(3), '
            '991–1015. DOI: 10.4007/annals.2017.185.3.7.'
        ),
        (
            'Cohn, H., Kumar, A., Miller, S. D., Radchenko, D., & Viazovska, M. S. (2017). The sphere packing problem '
            'in dimension 24. Annals of Mathematics, 185(3), 1017–1033. DOI: 10.4007/annals.2017.185.3.8.'
        ),
        (
            'Hales, T., Adams, M., Bauer, G., Dang, T. D., Harrison, J., Le Truong, H., Kaliszyk, C., Magron, V., '
            'McLaughlin, S., Nguyen, T. T., Nguyen, Q. T., Nipkow, T., Obua, S., Pleso, J., Rute, J., Solovyev, A., '
            'Ta, T. H. A., Tran, N. T., Trieu, T. D., Urban, J., Vu, K., & Zumkeller, R. (2017). A Formal Proof of the '
            'Kepler Conjecture. Forum of Mathematics, Pi, 5, e2. DOI: 10.1017/fmp.2017.1.'
        ),
        (
            'Cohn, H., Kumar, A., Miller, S. D., Radchenko, D., & Viazovska, M. S. (2022). Universal optimality of the '
            'E_8 and Leech lattices and interpolation formulas. Annals of Mathematics, 196(3), 983–1082. '
            'DOI: 10.4007/annals.2022.196.3.3.'
        ),
        (
            'Campos, M., Jenssen, M., Michelen, M., & Sahasrabudhe, J. (2023). A new lower bound for sphere packing. '
            'Preprint arXiv:2312.10026.'
        ),
        (
            'Klartag, B. (2025). Lattice packing of spheres in high dimensions using a stochastically evolving ellipsoid. '
            'Preprint arXiv:2504.05042.'
        ),
        (
            'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and '
            'classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
            '882–898. DOI: 10.1162/qss_a_00146.'
        ),
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Cohn-Elkies radial Laguerre-Gaussian '
        'bounds versus lattice packing densities across dimensions 2, 3, 4, 8, and 24">\n'
        '            <line x1="48" y1="184" x2="352" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <line x1="48" y1="28" x2="48" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <text x="54" y="21" font-size="10.5" font-weight="600" fill="currentColor">Packing Density Δ_d &amp; Cohn–Elkies Dual Bound</text>\n'
        '            <path d="M 56 42 Q 112 72 162 114 T 342 178" fill="none" stroke="var(--tp-prussian)" stroke-width="2.2"/>\n'
        '            <path d="M 56 36 Q 116 64 168 102 T 342 168" fill="none" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="5,3"/>\n'
        '            <rect id="tp-m14-lat-bar" x="150" y="71" width="22" height="113" rx="3" fill="var(--tp-verdigris)" fill-opacity="0.45"/>\n'
        '            <rect id="tp-m14-ce-bar" x="176" y="68" width="22" height="116" rx="3" fill="var(--tp-minium)" fill-opacity="0.35"/>\n'
        '            <circle id="tp-m14-point" cx="134" cy="71" r="6" fill="var(--tp-verdigris)"/>\n'
        '            <text x="206" y="64" font-size="9" fill="var(--tp-minium)">Cohn–Elkies Degree-M LP Upper Bound</text>\n'
        '            <text x="206" y="80" font-size="9" fill="var(--tp-prussian)">Lattice Packing Density Δ_d</text>\n'
        '            <line x1="372" y1="24" x2="372" y2="192" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="388" y="21" font-size="10.5" font-weight="600" fill="currentColor">Exact Offline Bounds (d = 4, 8, 24)</text>\n'
        '            <rect x="388" y="38" width="256" height="62" rx="6" fill="var(--tp-stone)" fill-opacity="0.28" stroke="var(--tp-prussian)" stroke-width="1.6"/>\n'
        '            <text id="tp-m14-status-lbl" x="400" y="60" font-size="9" font-weight="600" fill="var(--tp-prussian)">d = 8 (E_8): Δ = 0.253670 · Deg-5 LP = 0.303541</text>\n'
        '            <text x="400" y="80" font-size="9" fill="var(--tp-verdigris)">d = 24 (Leech): Δ_24 = 0.001930 · Deg-5 LP = 0.008955</text>\n'
        '            <rect x="388" y="112" width="256" height="58" rx="6" fill="var(--tp-verdigris)" fill-opacity="0.12" stroke="var(--tp-verdigris)" stroke-width="1.4"/>\n'
        '            <text x="400" y="134" font-size="9.5" font-weight="600" fill="var(--tp-prussian)">d = 4 (D_4): τ_4 = 24 · Δ_4 = 0.616850 (OPEN GAP)</text>\n'
        '            <text x="400" y="154" font-size="9" fill="var(--tp-minium)">Deg-5 LP = 0.672477 · 196,560 Leech vectors via G_24</text>\n'
        '            <text x="48" y="206" font-size="10" fill="var(--tp-verdigris)">Exact rational Laguerre basis · Recomputed offline by verify_m14_sphere_packing.py</text>\n'
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining what a tactile mathematical tabletop apparatus for sphere packing and '
        'Voronoi cell geometry would look like: brushed brass and frosted quartz spheres nested inside a dark '
        'anodized-slate Voronoi cell tray beside a smooth matte-steel circular ring gauge on limestone vellum paper '
        '(artistic impression, not a measured physical specimen)'
    ),
    'caption': (
        'Conceptual Vision Plate M.14-V (Imagining What It Would Look Like) · Artistic studio view imagining dense '
        'sphere packing inside dark Voronoi facets beside a steel gauge ring. Exact rational Cohn–Elkies bounds and '
        'Golay G_24 Leech counts are kept intact in deterministic Plate M.14-A and the offline verifier below.'
    ),
}

DISPATCH = {
    'kicker': 'FRONTIER HARMONIC GEOMETRY DISPATCH · SPHERE PACKING & LP DUALITY',
    'headline': 'Cohn–Elkies Fourier Bounds, Viazovska Modular Forms & The Open Dimension-4 Gap',
    'body': (
        'Why do 8-dimensional E_8 and 24-dimensional Leech lattices lock into optimal sphere packings while dimension 4 '
        'remains open? Pairing exact Laguerre–Gaussian Fourier eigenfunctions (Cohn & Elkies 2003, '
        'DOI 10.4007/annals.2003.157.689) with Viazovska’s modular functions (DOI 10.4007/annals.2017.185.3.7) '
        'separates closed dimensions 8 and 24 from the open 9.02% degree-5 gap in dimension 4.'
    ),
}

META_3D = (
    'Sphere Packing Density & Cohn–Elkies Radial Dual Potential',
    'X: Spatial Radius r · Z: Dimension / Mode Index · Y: Radial Test Amplitude f(r)',
)

ES_TRANSLATION = {
    'title_es': 'Empaquetamiento de Esferas en Dimensiones 3, 4, 8 y 24: Cotas de Cohn–Elkies, Formas Modulares y Brechas Abiertas',
    'subtitle_es': (
        'Síntesis de los Folios M.09 y M.12: cómo Henry Cohn y Noam Elkies convirtieron el empaquetamiento de esferas '
        'en programación lineal de Fourier, cómo Maryna Viazovska y colaboradores cerraron las dimensiones 8 y 24, y '
        'por qué la dimensión 4 y el régimen asintótico siguen abiertos.'
    ),
    'why_es': (
        'Así como las naranjas se acomodan en pirámides dentro de una caja y las monedas en un panal sobre la mesa, '
        'en ocho y veinticuatro dimensiones aparecen redes cristalinas tan simétricas que una función dual cierra el '
        'techo, mientras la dimensión cuatro sigue abierta.'
    ),
    'plain_es': (
        'En palabras sencillas, el empaquetamiento de esferas pregunta qué fracción de una sala enorme puedes llenar '
        'con canicas idénticas sin aplastarlas. Sobre una mesa plana, el patrón hexagonal llena noventa y un por ciento '
        'con nueve por ciento de huecos; en tres dimensiones, las pirámides de frutería llenan setenta y cuatro por '
        'ciento de la caja. En cuatro dimensiones, aunque cada esfera toca a veinticuatro vecinas, todavía no se sabe '
        'si una configuración desordenada podría superar a la red D_4. En cambio, en ocho y veinticuatro dimensiones '
        'surgen cristales tan simétricos que una regla matemática descarta cualquier arreglo más denso. Esa regla '
        'convierte un problema geométrico en una balanza entre ondas espaciales y sus espectros de frecuencia, dando '
        'techos rigurosos en cada dimensión mientras deja abierta la carrera en cuatro dimensiones.'
    ),
    'deep_es': (
        'Con la convención de Fourier f̂(t) = ∫ f(x) exp(−2πi x·t) dx, las funciones radiales de Laguerre–Gauss '
        'ψ_k(x) = L_k^(d/2−1)(2π|x|²) exp(−π|x|²) tienen valor propio exacto (−1)^k. Al elegir P̂(u) = '
        '(u + α)∏(u − s_j)² de grado impar en aritmética racional exacta y comprobar que cada coeficiente de P(u_cut + w) '
        'es ≤ 0, nuestro verificador fuera de línea acota Δ_d desde arriba: en d = 8 (E_8, Δ_8 = π⁴/384 = 0.253670, '
        'τ_8 = 240; Viazovska 2017, DOI 10.4007/annals.2017.185.3.7) la cota de grado 5 baja de 0.346486 a 0.303541; '
        'en d = 24 (Leech Λ_24, Δ_24 = π¹²/12! = 0.001930, τ_24 = 196,560 mediante 759 octadas del código Golay G_24; '
        'CKMRV 2017, DOI 10.4007/annals.2017.185.3.8) baja de 0.087466 a 0.008955; en d = 4 (D_4, Δ_4 = π²/16 = '
        '0.616850, τ_4 = 24 por Musin 2008, DOI 10.4007/annals.2008.168.1) permanece una brecha de 9.02% frente a '
        '0.672477. Esta hipótesis T0–T2 quedaría falsada si algún empaquetamiento no reticular en d = 4 superara π²/16 '
        'o si un testigo polinomial admisible cayera debajo de 0.616850; los preprints arXiv:2312.10026 y '
        'arXiv:2504.05042 reportan cotas asintóticas inferiores fuera de nuestras pruebas finitas.'
    ),
    'bridge_es': (
        'Las cotas polinomiales de Cohn–Elkies acotan la densidad desde arriba en cualquier dimensión par, separando '
        'el cierre modular en d = 8 y d = 24 de la brecha abierta en d = 4.'
    ),
}
