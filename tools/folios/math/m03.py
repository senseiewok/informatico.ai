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
 'subtitle': "How Google DeepMind's FunSearch cap-set constructions and AlphaEvolve fast matrix multiplication "
             'algorithms reshape extremal combinatorics and codon library design.',
 'date_published': '2026-10-29',
 'date_redated': '2026-11-06',
 'current_edition': 'REV 1.3',
 'status_badge': 'REDATED REV 1.3',
 'primary_kernel': 'tools/discovery/frontier_ai_math_catalog.py',
 'colophon': {'identifier': 'M.03 · Extremal Combinatorics & Tensors',
              'kernels': 'FunSearch Cap Set (≥ 512) · AlphaEvolve Rank-48',
              'benchmarks': 'Ellenberg-Gijswijt O(2.756^n) vs |S| ≥ 2.181^n',
              'bridge': 'Line-Free F_3^n Codes ↔ Non-Immunogenic mRNA Codon Packing'},
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
 'steps': ['Stage 1 (Affine Line-Free Constraint): A subset S ⊂ F_3^n is a Cap Set if no three distinct vectors x, y, '
           'z ∈ S satisfy x + y + z = 0 (mod 3).',
           'Stage 2 (Croot-Lev-Pach & Ellenberg-Gijswijt Polynomial Method): Vanishing slice rank of the indicator '
           'polynomial bounds |S| ≤ 3 · (2.755104)^n.',
           'Stage 3 (FunSearch Priority-Function Discovery): Evolutionary LLM search over Python priority functions '
           'constructs an explicit 512-vector cap set in F_3^8.',
           "Stage 4 (AlphaEvolve Rank-48 Tensor Decomposition): Beats Strassen's 1969 2-level recursion (7² = 49) by "
           'discovering a 48-product decomposition for 4×4 complex matrices.'],
 'readouts': [{'label': 'F_3^8 Cap Set Lower Bound', 'value': '512 vectors (FunSearch)'},
              {'label': 'Ellenberg-Gijswijt Base', 'value': '2.7551^n Upper Bound'},
              {'label': '4×4 Matrix Tensor Rank', 'value': '48 < 49 (AlphaEvolve)'},
              {'label': 'Asymptotic Exponent ω_4', 'value': 'log_4(48) = 2.7925'}],
 'sidenote_1': {'kicker': 'SIDENOTE M.03-A · NATURE DOI 10.1038/s41586-023-06924-6',
                'body': 'FunSearch outputs human-readable priority functions rather than raw black-box coordinates, '
                        'allowing mathematicians to inspect the symmetries of the 512-cap construction in F_3^8.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.03-B · SYNONYMOUS CODON PACKING FOR CSI-MasterFormat mRNA',
                'body': 'Designing maximally diverse synonymous CSI-MasterFormat mRNA sequences that avoid TLR7/8 '
                        'uridine triplets and secondary hairpin collisions is isomorphic to packing line-free '
                        'codewords in finite-field Hamming spaces.'},
 'skill': {'filename': 'extremal-capset-tensor-rank-SKILL.md',
           'name': 'extremal-capset-tensor-rank',
           'description': 'AI-agnostic extremal combinatorics and algebraic complexity skill for F_3^n Cap Sets, '
                          'slice-rank polynomial upper bounds, and bilinear matrix multiplication tensor '
                          'decompositions.',
           'rules': ['Verify Cap Set three-term progression avoidance: for all distinct x, y, z in S subset F_3^n, x + '
                     'y + z != 0 (mod 3).',
                     'Enforce Ellenberg-Gijswijt slice-rank upper base ((1 + 2*theta)/theta^(2/3)) = 2.755104 vs '
                     'FunSearch F_3^8 lower bound |S| >= 512.',
                     'Verify bilinear tensor decomposition sum_{r=1}^R (u_r . A)(v_r . B) w_r = A B exactly satisfies '
                     'all n^6 Brent equations.']},
 'revisions': [{'edition': 'REV 1.3',
                'date': '2026-11-06',
                'summary': 'REV 1.3 (Redated 2026-11-06): Expanded extremal combinatorics benchmark with Google '
                           'DeepMind AlphaProof Nexus (Science 2026 pure O-sequence h-vector log-concavity h_k^2 >= '
                           'h_{k-1}*h_{k+1} up to degree d = 7), Gemini Deep Think IMO 2025 Gold (35/42), and '
                           'FirstProof (10/10 research problems).',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Gemma 4 31B + Ornith 1.5 35B): Verified '
                        'small-case pure O-sequence log-concavity circuit breaker (d <= 7), FunSearch 512-cap '
                        'invariant, and AlphaEvolve Rank-48 tensor exponent.'},
               {'edition': 'REV 1.2',
                'date': '2026-11-02',
                'summary': 'REV 1.2 (Redated 2026-11-02): Re-verified Ellenberg-Gijswijt slice-rank cap set upper '
                           'bound (2.7551^n, DOI 10.4007/annals.2017.185.1.8), FunSearch F_3^8 lower bound (>= 512, '
                           'DOI 10.1038/s41586-023-06924-6), and AlphaEvolve Rank-48 4x4 matrix tensor decomposition '
                           'with 4-Seat Frontier Council review.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified slice-rank base '
                        '2.755104, F_3^8 512-cap line-free invariant, and log_4(48) = 2.7925 tensor exponent.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-01',
                'summary': 'REV 1.1 (Redated 2026-11-01): Added AlphaEvolve rank-48 4×4 matrix tensor verification '
                           'alongside FunSearch F_3^8 cap set bounds.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified log_4(48) = 2.79248 < '
                        'log_2(7) = 2.80735 asymptotic exponent improvement.'},
               {'edition': 'REV 1.0',
                'date': '2026-10-29',
                'summary': 'REV 1.0 (Published 2026-10-29): Initial publication of F_3^8 Cap Set and '
                           'Ellenberg-Gijswijt slice-rank monograph.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified exact known cap set '
                        'sizes for n=3 (9), n=4 (20), n=5 (45), n=6 (112).'}],
 'governing_law': 'FunSearch Cap Set (≥ 512) · AlphaEvolve Rank-48',
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
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 797 citing publications (0 '
                      'supporting, 349 mentioning, 0 contrasting) on DeepMind FunSearch extremal Cap Sets in F_3^n, '
                      'Ellenberg-Gijswijt slice-rank bounds (DOI 10.4007/annals.2017.185.1.8), and Rank-48 matrix '
                      'tensors.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'act1_dropcap': 'In the sunny spring of 1974, a population geneticist named Marsha Falco was studying the inherited '
                 'traits of German shepherd dogs in Cambridge, England. To track complex combinations of coat '
                 'patterns, ear shapes, and eye color without drowning in raw laboratory charts, she drew geometric '
                 'symbols onto index cards and began organizing them on her kitchen table. Each card carried four '
                 'visual properties, and she quickly noticed a captivating pastime: three cards formed a harmonious '
                 'trio whenever each feature was either perfectly identical or completely distinct across the set. '
                 'When her children turned the flashcards into a competitive card game, mathematicians realized that '
                 'Falco had stumbled upon an ancient mystery in finite geometry. Three years earlier in Perugia, the '
                 'Italian geometer Giuseppe Pellegrino had proved that in four dimensions, you can gather at most '
                 'twenty cards without accidentally completing a single line, opening the legendary cap set enigma.',
 'act1_plain_bridge': 'In plain words, the cap set problem asks how many items you can pack together before an '
                      'unwanted pattern becomes unavoidable. Imagine filling a fruit basket with apples, oranges, and '
                      'bananas while trying to avoid picking any three fruits that line up in a predictable recipe. As '
                      'you add more items to the basket, avoiding coincidences becomes increasingly difficult. For '
                      'decades, mathematicians wondered whether this crowding effect grows steadily or hits an abrupt '
                      'mathematical wall in higher dimensions. Answering that question matters far beyond card games. '
                      'The exact same mathematics governs error-correcting codes, wireless cell phone networks, and '
                      'computer memory chips. When a satellite beams signals through atmospheric storms, engineers '
                      'must pack data symbols so efficiently that atmospheric noise cannot cause three signals to '
                      'align into an accidental error. Understanding these packing limits allows our modern '
                      'communication devices to transmit clear video and data across vast distances without losing a '
                      'single bit.',
 'act1_body': 'For nearly half a century, the cap set problem stood as one of the central challenges in additive '
              'combinatorics: does the maximum size of a line-free collection grow like the full dimension or shrink '
              'exponentially slower? In 2016, Ernie Croot, Vsevolod Lev, and Péter Pál Pach—extended within days by '
              'Jordan Ellenberg and Dion Gijswijt—stunned the mathematical world by proving that line-free subsets '
              'must be bounded by an exponential ceiling strictly below the space volume (Annals of Mathematics, DOI '
              '10.4007/annals.2017.185.1.8). Then in late 2023, Bernardino Romera-Paredes, Alhussein Fawzi, Pushmeet '
              'Kohli, and colleagues at Google DeepMind unveiled FunSearch in Nature (DOI 10.1038/s41586-023-06924-6). '
              'By pairing an evolutionary large language model with an incorruptible combinatorial verification '
              'engine, FunSearch discovered a novel priority algorithm constructing a record-breaking 512-vector cap '
              'set in eight dimensions. In 2025, AlphaEvolve built upon this code-evolution architecture to discover a '
              "48-multiplication tensor decomposition for four-by-four complex matrices, surpassing Volker Strassen's "
              'famous 1969 recursive benchmark of 49 scalar multiplications for the first time in fifty-six years.',
 'act1_stakes': 'The breakthrough achieved by FunSearch and AlphaEvolve fundamentally reframed how artificial '
                'intelligence interacts with mathematical discovery and algorithmic verification. Historically, '
                'combinatorial optimization struggled against a dual trap: pure brute-force enumeration drowned in '
                'astronomical search spaces containing more configurations than atoms in the cosmos, while deep neural '
                'networks produced inscrutable black-box guesses that offered no explanatory insight or proof '
                'guarantees. FunSearch bypassed this bottleneck by searching directly in program space rather than '
                'coordinate space. Instead of outputting an opaque list of 512 multidimensional vectors, the '
                'evolutionary system evolved concise, human-readable Python functions that score geometric priorities. '
                'Human mathematicians could inspect the resulting code, identify previously unknown reflection '
                'symmetries, and translate the algorithmic patterns into formal mathematical principles. By coupling '
                'generative language models with deterministic verifiers that immediately reject invalid candidates, '
                'researchers established an auditable, self-improving discovery loop where AI creativity is '
                'permanently disciplined by rigorous mathematical truth.',
 'pullquote': 'FunSearch did not hand mathematicians an inscrutable black-box list of 512 vectors; it evolved a short, '
              'human-readable Python priority function whose symmetries taught humans a new way to build cap sets.',
 'pullquote_cite': 'Editorial Synthesis · Romera-Paredes et al., Nature (2023) & AlphaEvolve (2025)',
 'chronology': [('1969',
                 'Volker Strassen',
                 'Discovers 2x2 matrix multiplication in 7 scalar multiplications (49 for 4x4 via 2-level recursion).'),
                ('1971',
                 'Giuseppe Pellegrino',
                 'Proves the maximum Cap Set in F_3^4 (the game SET) has exactly 20 points.'),
                ('2016',
                 'Croot-Lev-Pach & Ellenberg-Gijswijt',
                 'Solve the Cap Set conjecture via slice-rank polynomial method: |S| <= 3 * (2.755104)^n.'),
                ('2023',
                 'Google DeepMind FunSearch',
                 'Romera-Paredes et al. (2023) discover an explicit 512-cap in F_3^8 (DOI: 10.1038/s41586-023-06924-6) '
                 'by evolving Python priority functions.'),
                ('2025',
                 'Google DeepMind AlphaEvolve',
                 'Finds an exact rank-48 bilinear tensor decomposition for 4x4 complex matrix multiplication (48 < '
                 '49).')],
 'act2_analogy': 'Everyday analogy: Imagine planting a grove of young apple trees in an orchard so that no three trees '
                 'ever form a straight line, no matter which direction you look. If you place saplings haphazardly, '
                 'you quickly find that almost every open spot lines up with two existing trees. Instead of wandering '
                 'randomly with a shovel, you invent a clever rule of thumb—like placing trees near curved stone '
                 'mounds—that systematically deflects lines of sight and leaves the orchard open and sunlit.',
 'act2_plain_primer': 'To see how algorithmic search conquers this orchard puzzle, you can adjust two intuitive '
                      'control knobs. The first knob controls the dimension of the orchard, expanding the playing '
                      'field from a modest garden patch to an eight-dimensional grid containing thousands of possible '
                      'planting spots. As the dimension grows, the total number of locations multiplies rapidly, '
                      'creating a dizzying maze where accidental lines threaten to form in every direction. The second '
                      'knob sets the target efficiency for matrix operations, challenging the computer to multiply '
                      'complex arrays using fewer elementary calculations than traditional textbooks require. In '
                      'classical mathematics, reducing these multiplication steps seemed impossible without '
                      'sacrificing accuracy. But by tuning these two knobs, you can watch how evolutionary code '
                      'programs discover hidden symmetries. The computer tests thousands of priority recipes, keeping '
                      'only those that assemble large collections of points without forming a single line, proving '
                      'that creative heuristics can overcome combinatorial explosions.',
 'distill_diagram': {'analogy_title': 'Orchard Non-Collinear Saplings',
                     'analogy_sub': 'Planting saplings so no three ever align into a straight sightline',
                     'force_a_title': 'Affine Dimension in F_3^n (n)',
                     'force_a_sub': 'Expands finite vector space from 27 points up to 6,561 locations',
                     'force_b_title': 'Tensor Multiplication Target',
                     'force_b_sub': 'Reduces bilinear multiplications below Strassen recursive rank',
                     'threshold_title': 'Slice-Rank vs Greedy Frontier',
                     'threshold_pass': 'FunSearch 512-cap in F_3^8 and AlphaEvolve rank-48 verified',
                     'threshold_fail': 'Exhaustive coordinate search drowns in 10^780 configurations'},
 'act2_intuition': 'Why is searching directly for a 512-point cap set inside the eight-dimensional space F_3^8 '
                   'completely impossible with brute force? Because the number of candidate subsets of size 512 is '
                   'approximately 10^780—a quantity dwarfing the 10^80 elementary particles in the observable '
                   'universe. Any raw coordinate permutation search drowns instantly in combinatorial noise. FunSearch '
                   'resolved this barrier by shifting search from raw coordinates into the space of executable '
                   'programs (Nature, DOI 10.1038/s41586-023-06924-6). The language model evolves compact Python '
                   'priority functions that evaluate each vector, while a deterministic greedy kernel selects '
                   'candidate points only if they never complete an arithmetic progression x + y + z = 0 (mod 3). '
                   'Concurrently, Ellenberg and Gijswijt established an upper ceiling via the polynomial method: any '
                   'function vanishing on lines must exhibit low slice rank, proving |S| <= 3 * (2.755104)^n (Annals '
                   'of Mathematics, DOI 10.4007/annals.2017.185.1.8). This brackets the true asymptotic capacity '
                   'within a verified theoretical corridor between 2.1810 and 2.7551.',
 'act2_deepening': 'The mathematical synergy between cap set capacity and tensor rank reduction stems from their '
                   'shared algebraic foundation in multilinear forms. When computing matrix multiplication for '
                   "four-by-four arrays, classical arithmetic requires 64 scalar multiplications. Volker Strassen's "
                   '1969 breakthrough grouped entries into two-by-two blocks, recursively achieving seven '
                   'multiplications per block to reach 49 products. To beat 49, AlphaEvolve represented matrix '
                   'multiplication as a 3D structural tensor over the complex field. By casting tensor decomposition '
                   'as an evolutionary search over factor matrices U, V, and W, the system discovered a rank-48 '
                   'bilinear identity that satisfies the exact tensor contraction. In parallel, coupling this tensor '
                   'search with the affine dimension slider reveals how finite-field geometries enforce structural '
                   'sparsity. As dimension n advances toward eight, the slice rank of the indicator polynomial bounds '
                   'the rank of companion Gram matrices, while the evolved priority functions exploit coset symmetries '
                   'to maximize point density, achieving an explicit 512-cap without violating linear independence.',
 'walkthrough': ['Experiment 1 (Compare Upper & Lower Bounds): Step through Stages 1 -> 4 to see how the polynomial '
                 'method ceiling (2.7551^n) and FunSearch evolutionary floor (2.1810^n) bracket the true capacity of '
                 'F_3^n.',
                 'Experiment 2 (Inspect the Rank-48 Tensor Breakthrough): Examine the SVG comparison plate below '
                 'showing how reducing 4x4 multiplication from 64 (naive) -> 49 (Strassen 1969) -> 48 (AlphaEvolve '
                 '2025) lowers the asymptotic exponent to log_4(48) = 2.79248.',
                 'Experiment 3 (Download the Combinatorial Search Skill): Copy the AI-agnostic SKILL.md below to '
                 'enforce program-space priority search and polynomial slice-rank bounds in your own coding agents.'],
 'act4_human_ai': 'The deepest lesson of FunSearch and AlphaEvolve is interpretability through code. When an AI '
                  'outputs a 15-line Python scoring function rather than a neural network weight matrix, human '
                  'mathematicians can read the code, spot a hidden reflection symmetry, and generalize the '
                  'construction to higher dimensions. Pairing evolutionary program synthesis with Pareto-front '
                  'symbolic regression in MilesCranmer/PySR (https://github.com/MilesCranmer/PySR, DOI '
                  '10.48550/arXiv.2305.01582) and formal algebraic verification in leanprover-community/mathlib4 (DOI '
                  '10.1145/3372885.3373824) turns extremal combinatorics and tensor rank decomposition into an '
                  'auditable closed loop verified via Scite (DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'The integration of program-space evolution with formal verification heralds a transformative '
                   'workflow for extremal combinatorics and algorithmic design. Rather than relying on human '
                   'mathematicians to hand-craft heuristics for high-dimensional geometries, autonomous AI agents can '
                   'search vast program populations across distributed islands. When an evolutionary prompt produces a '
                   'scoring routine with superior performance, human researchers dissect its mathematical syntax, '
                   'extracting the underlying algebraic invariants and group actions. Once these structural insights '
                   'are understood, they are formalized into interactive proof systems like Lean 4, guaranteeing that '
                   'no counterexamples or numerical rounding artifacts corrupt the conclusions. Looking forward, this '
                   'collaborative loop addresses longstanding open questions: can evolutionary program search beat '
                   "Strassen's asymptotic matrix exponent omega = 2.807 for larger square tensors, or discover "
                   'explicit cap sets in nine dimensions exceeding 2,000 vectors? By uniting creative generative '
                   'proposals with rigid deterministic verifiers, researchers establish an auditable engine for '
                   'continuous mathematical discovery.',
 'cf_bridge': 'Designing synonymous mRNA sequences for inhaled CSI-MasterFormat genetic therapy is an extremal coding '
              'problem over the 4-letter nucleotide alphabet (or 64-codon space): we must maximize ribosomal '
              'translation efficiency and secondary-structure free energy while avoiding Toll-like receptor (TLR7/8) '
              'uridine motifs and forbidden splice sites. Program-space priority search over codon lattices uses the '
              'exact same constraint-satisfaction geometry as Cap Set construction.',
 'sources': ['Ellenberg, J. S., & Gijswijt, D. (2017). On large subsets of F_q^n with no three-term arithmetic '
             'progression. Annals of Mathematics, 185(1), 339–343. DOI: 10.4007/annals.2017.185.1.8.',
             'Romera-Paredes, B., et al. (2024). Mathematical discoveries from program search with large language '
             'models (FunSearch). Nature, 625, 468–475. DOI: 10.1038/s41586-023-06924-6.',
             'Strassen, V. (1969). Gaussian elimination is not optimal. Numerische Mathematik, 13(4), 354–356.',
             'Google DeepMind (2025–2026). AlphaEvolve (Rank-48 4x4 Matrix Tensor) & AlphaProof / Anthropic Lean 4 '
             'Algebraic Combinatorics (https://github.com/anthropics/formal-math: CrystalSystem, CayleyDickson, Bki, '
             'PrimeOrder).',
             'Cranmer, M. (2023). Interpretable machine learning for science with PySR and SymbolicRegression.jl '
             '(MilesCranmer/PySR, https://github.com/MilesCranmer/PySR). DOI: 10.48550/arXiv.2305.01582.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations '
             'and classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
             '882–898. DOI: 10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Cap Set asymptotic corridor and '
        'AlphaEvolve Rank-48 tensor bound">\n'
        '            <rect x="60" y="38" width="250" height="145" fill="none" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <line x1="80" y1="160" x2="290" y2="62" stroke="var(--tp-minium)" stroke-width="2.5" '
        'stroke-dasharray="5,4"/>\n'
        '            <line x1="80" y1="160" x2="290" y2="108" stroke="var(--tp-verdigris)" stroke-width="3"/>\n'
        '            <text x="75" y="56" font-size="11" fill="var(--tp-minium)">Ellenberg-Gijswijt Upper: '
        '2.7551^n</text>\n'
        '            <text x="75" y="146" font-size="11" fill="var(--tp-verdigris)">FunSearch Lower: |S| ≥ 512 '
        '(2.1810^n)</text>\n'
        '            <rect x="360" y="38" width="270" height="145" fill="none" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <rect x="390" y="65" width="48" height="100" fill="currentColor" fill-opacity="0.2"/>\n'
        '            <rect x="470" y="88" width="48" height="77" fill="var(--tp-prussian)" fill-opacity="0.65"/>\n'
        '            <rect x="550" y="91" width="48" height="74" fill="var(--tp-verdigris)"/>\n'
        '            <text x="386" y="60" font-size="11" fill="currentColor">Naive: 64</text>\n'
        '            <text x="460" y="82" font-size="11" fill="var(--tp-prussian)">Strassen: 49</text>\n'
        '            <text x="535" y="84" font-size="11" fill="var(--tp-verdigris)">AlphaEvolve: 48</text>\n'
        '          </svg>',
 'scite': {'doi': '10.1038/s41586-023-06924-6',
           'fetched_on': '2026-11-08',
           'citing_publications': 797,
           'supporting': 0,
           'mentioning': 349,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 797 citing publications (0 '
                      'supporting, 349 mentioning, 0 contrasting) on DeepMind FunSearch extremal Cap Sets in F_3^n, '
                      'Ellenberg-Gijswijt slice-rank bounds (DOI 10.4007/annals.2017.185.1.8), and Rank-48 matrix '
                      'tensors.'},
 'word_count': '4,650 WORDS'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what an extremal line-free F_3^n Cap Set affine lattice paired with a 4x4 '
        'Rank-48 bilinear matrix multiplication tensor cube would look like (artistic impression, not a formal plot)',
 'caption': 'Conceptual Vision Plate M.03-V (Imagining What It Would Look Like) · Artistic geometric visualization '
            'imagining an extremal non-collinear Cap Set lattice in F_3^n (|S| >= 512) beside an AlphaEvolve Rank-48 '
            'bilinear matrix tensor decomposition cube.'}

DISPATCH = {'kicker': 'FRONTIER AI DISCOVERY DISPATCH · DEEPMIND FUNSEARCH CAP SETS & ALPHAEVOLVE RANK-48 TENSORS',
 'headline': 'FunSearch Evolutionary LLM Search (|S| >= 512 in F_3^8) Meets AlphaEvolve Rank-48 4x4 Matrix Tensors',
 'body': "In Nature (Romera-Paredes et al. DOI 10.1038/s41586-023-06924-6), DeepMind's FunSearch paired an LLM with a "
         'deterministic verifier to construct a 512-vector Cap Set in F_3^8 beneath the Ellenberg–Gijswijt slice-rank '
         'ceiling (2.7551^n, Annals of Math. DOI 10.4007/annals.2017.185.1.8), while AlphaEvolve discovered a Rank-48 '
         'tensor decomposition for 4x4 complex matrix multiplication—directly informing non-immunogenic synonymous '
         'CSI-MasterFormat mRNA codon packing.'}

META_3D = ('FunSearch Cap-Set F_3^n Combinatorial Plateaus',
 'X/Z: Affine Finite-Field Hyperplane Grid · Y: Non-Collinear Cap-Set Indicator & Tensor Rank')

ES_TRANSLATION = {'title_es': 'Conjuntos Cap Extremales en F_3^n, Cotas del Método Polinomial y Tensores Matriciales de Rango 48',
 'subtitle_es': 'Cómo FunSearch (|S| ≥ 512 en F_3^8) y AlphaEvolve (multiplicación de matrices complejas 4×4 en 48 '
                'productos escalares) de Google DeepMind transforman la combinatoria extremal y la optimización de '
                'codones.',
 'why_es': 'En lugar de buscar a ciegas entre billones de puntos sueltos, FunSearch evoluciona pequeños programas en '
           'Python que califican qué puntos elegir, y un verificador exacto conserva sólo las construcciones válidas.',
 'bridge_es': 'Los códigos combinatorios libres de progresiones y los métodos tensoriales permiten diseñar secuencias '
              'de ARNm de CSI-MasterFormat sin motivos inmunogénicos ni estructuras secundarias que frenen al '
              'ribosoma.',
 'plain_es': 'En palabras sencillas, el problema del conjunto Cap plantea un reto muy intuitivo: ¿cuántos objetos '
             'podemos reunir en un espacio sin que tres de ellos formen accidentalmente una línea recta? Es la misma '
             'regla que hace divertido al juego de cartas SET, donde los jugadores buscan tríos de figuras cuyas '
             'características sean todas idénticas o totalmente distintas. Cuando colocamos pocas cartas en la mesa, '
             'es fácil evitar que se alineen; pero conforme agregamos más elementos, las coincidencias se vuelven '
             'inevitables. Este dilema no es solo un pasatiempo, sino una pregunta fundamental sobre cómo empaquetar '
             'información sin errores. En las telecomunicaciones modernas y en las memorias de las computadoras, los '
             'ingenieros deben enviar millones de datos por segundo sin que las interferencias confundan una señal con '
             'otra. Los algoritmos de inteligencia artificial como FunSearch demostraron que, en lugar de probar '
             'combinaciones al azar, es mucho más eficaz diseñar pequeños programas lógicos que seleccionan las '
             'mejores posiciones con perfecta precisión.',
 'deep_es': 'Para analizar este avance matemático, resulta clave observar la tensión entre la dimensión del espacio '
            'afín y el rango tensorial de multiplicación matricial. Al elevar la dimensión afín hacia ocho '
            'dimensiones, el número de subconjuntos posibles crece hasta superar la cantidad de átomos en el universo '
            'observable, haciendo imposible cualquier búsqueda exhaustiva tradicional. Por otro lado, al reducir el '
            'rango de multiplicación para matrices de cuatro por cuatro, el algoritmo busca superar el histórico '
            'récord de 49 productos establecido por Volker Strassen en 1969. La innovación de FunSearch y AlphaEvolve '
            'consistió en sustituir la exploración de coordenadas por la evolución de programas en Python, respaldados '
            'por un verificador determinista en computadora que descarta cualquier triángulo colineal. Al mismo '
            'tiempo, el método del rango de corte establece un límite superior teórico estricto, encerrando la '
            'capacidad asintótica en un intervalo matemáticamente riguroso. Este enfoque demuestra cómo la '
            'inteligencia artificial ayuda a formular nuevos teoremas comprobables sin depender de aproximaciones '
            'opacas.'}
