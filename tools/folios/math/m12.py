#!/usr/bin/env python3
"""Folio M.12 (MATH): Public Lean 4 Repositories and NIST FIPS 203 (ML-KEM): What They State, Side by Side."""
from __future__ import annotations

SLUG = 'm12'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.12',
 'slug': 'm12',
 'pillar': 'math',
 'category_code': 'M',
 'parent_folios': ['M.01', 'M.03', 'M.06'],
 'lineage_mode': 'SYNTHESIS · Synthesizes M.01 Lean 4 Modularity, M.03 Tensor Rank & M.06 '
                 'Fine-Grained Complexity',
 'title': 'Public Lean 4 Repositories and NIST FIPS 203 (ML-KEM): What They State, Side by Side',
 'subtitle': "Synthesizing Folios M.01, M.03 and M.06: what the README of the public Lean 4 "
             'repository anthropics/formal-math, read on 2026-11-14, says it contains (including '
             'an eth project that the README says refutes the Exponential Time Hypothesis, a '
             'statement this site has not checked), set beside the module-lattice key encapsulation standard NIST FIPS 203 '
             '(ML-KEM).',
 'date_published': '2026-11-07',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'LEAN 4 & POST-QUANTUM · REV 1.1',
 'primary_kernel': 'tools/formal_verifier.py',
 'governing_law': 'b = A s + e (mod q) · q = 3329 · n = 256 · k ∈ {2, 3, 4} (NIST FIPS 203)',
 'colophon': {'identifier': 'M.12 · anthropics/formal-math (as stated in its READMEs) & NIST FIPS '
                            '203 ML-KEM Lattices',
              'kernels': 'Projects listed in the anthropics/formal-math README read 2026-11-14: '
                         'zeta23, 3sum-apsp, eth (not built here) · '
                         'Module-LWE b = As + e',
              'benchmarks': 'ML-KEM-768: k = 3 · q = 3329 · n = 256 · NIST security category 3 · '
                            'decapsulation failure 2^−164.8 (FIPS 203, Table 1)',
              'bridge': 'Synthesizes M.01/M.03/M.06 · Egg carton in fog (analogy) ↔ post-quantum '
                        'key exchange'},
 'sliders': [{'label': 'Module-LWE Lattice Rank (k_rank × 256)',
              'min': 2,
              'max': 4,
              'step': 1,
              'value': 3,
              'unit': 'k = '},
             {'label': 'Centered Binomial Noise Width (η_noise)',
              'min': 1,
              'max': 4,
              'step': 1,
              'value': 2,
              'unit': 'η = '}],
 'steps': ["Stage 1 (Shor's Quantum Period-Finding): Shor's 1994 algorithm would let a large "
           'fault-tolerant quantum computer (Folio P.11) find the period r of a^x mod N in time '
           'polynomial in log N, which would break RSA and elliptic-curve cryptography. No '
           'quantum computer able to do this for cryptographic key sizes has been reported.',
           'Stage 2 (Module Learning With Errors, NIST FIPS 203 ML-KEM): The public key b = A s '
           '+ e (mod q = 3329) over the ring R_q = ℤ_q[X]/(X²⁵⁶ + 1) hides the secret s behind '
           'small centered binomial noise e. Its security rests on the presumed hardness of '
           'module lattice problems; Regev (2009) showed that plain LWE is at least as hard, '
           'under a quantum reduction, as certain worst-case lattice problems.',
           'Stage 3 (What anthropics/formal-math says it contains): The README of '
           'anthropics/formal-math, read on 2026-11-14, lists three Lean 4 projects: zeta23 '
           '(Alpöge–Furman on zeta zeros), 3sum-apsp (Alman–Vassilevska Williams on 3SUM and '
           'APSP) and eth, described there as an algorithm for counting k-CNF solutions that '
           'refutes the Exponential Time Hypothesis. This site has not built or checked any of '
           'them. Earlier editions named files EightSquare.lean, ThreeSUM_APSP.lean and '
           "ETHIsFalse.lean; no files of those names appear in the repository's file tree read "
           'on 2026-11-14.',
           'Stage 4 (Implementation): open-quantum-safe/liboqs is an open-source library of '
           'post-quantum algorithms. Formal proofs about mathematics do not by themselves make '
           'an implementation bug-free; verifying cryptographic code is a separate task.'],
 'readouts': [{'label': 'ML-KEM-768 Security (FIPS 203)',
               'value': 'NIST security category 3 (k = 3)'},
              {'label': 'Eight-Square Rank Claim',
               'value': 'Withdrawn: no EightSquare.lean in the formal-math file tree (read '
                        '2026-11-14)'},
              {'label': 'formal-math/eth README Statement',
               'value': 'README read 2026-11-14 states an ETH refutation (not checked here)'},
              {'label': 'ML-KEM-768 Decapsulation Failure',
               'value': '2^−164.8 (FIPS 203, Table 1)'}],
 'spec_plate': {'division': 'POST-QUANTUM CRYPTOGRAPHY / NIST FIPS 203 (ML-KEM) / LEAN 4 FORMAL '
                            'COMPLEXITY',
                'title': 'Module-LWE Lattice Key Encapsulation & Lean 4 Repositories as Their '
                         'READMEs Describe Them',
                'body': 'NIST FIPS 203 (ML-KEM-768, q = 3329, R_q = Z_q[X]/(X^256+1)) post-quantum '
                        'lattice key encapsulation, of which open-quantum-safe/liboqs is one '
                        'open-source implementation, set beside the Lean 4 projects in '
                        'anthropics/formal-math as described in their READMEs.',
                'meta': 'Parameters checked against FIPS 203 (Tables 1–2) on 2026-11-14; '
                        'repository contents taken from READMEs, not built'},
 'sidenote_1': {'kicker': 'SIDENOTE M.12-A · CROSS-FIELD ANALOGY · A 768-DIMENSIONAL EGG CARTON IN '
                          'THICK FOG',
                'body': 'Why is ML-KEM thought to resist quantum computers? Picture an egg carton '
                        'stretched across 768 dimensions: the secret is a grid point, the public '
                        'key drops you near it in fog (+e), and finding the nearest valley without '
                        'the secret is believed to be hard for classical and quantum computers '
                        'alike. That belief rests on decades of cryptanalysis, not on a proof.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.12-B · WHAT THE ANTHROPICS/FORMAL-MATH README LISTS',
                'body': 'The README of https://github.com/anthropics/formal-math, read on '
                        '2026-11-14, lists three projects: zeta23, 3sum-apsp and eth. It states a deterministic algorithm that '
                        'counts satisfying assignments of every k-CNF in 2^O(min{k²n log log '
                        'n/√log n, km/√log m}) steps, which it says refutes the Exponential Time '
                        'Hypothesis. That is an extraordinary claim; this site reports it as the '
                        "repository's statement and has not checked it. The README of "
                        'https://github.com/anthropics/fermats-last-theorem, read the same day, '
                        "describes it as a separate Lean 4 repository holding a machine-checked "
                        "proof of Fermat's Last Theorem."},
 'skill': {'filename': 'lean4-complexity-mlkem-lattice-SKILL.md',
           'name': 'lean4-complexity-mlkem-lattice',
           'description': 'AI-agnostic formal mathematics and cryptography skill for reading the '
                          'Lean 4 projects in anthropics/formal-math (zeta23, 3sum-apsp, eth) by '
                          'their READMEs and for NIST FIPS 203 ML-KEM Module-LWE parameters.',
           'rules': ['Configure Module-LWE over polynomial ring R_q = Z_q[X]/(X^256 + 1) with '
                     'prime modulus q = 3329 and module rank k in {2, 3, 4} (ML-KEM-512/768/1024).',
                     'Take decapsulation failure rates from FIPS 203 Table 1 (2^-138.8, '
                     '2^-164.8 and 2^-174.8 for ML-KEM-512/768/1024) and noise widths from Table '
                     '2 (eta1 = 3, 2, 2; eta2 = 2) rather than deriving them from a rule of '
                     'thumb.',
                     'Before citing a Lean file, check it exists in the repository, and report its '
                     'README claims as repository statements unless you built it.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The files '
                           'EightSquare.lean, ThreeSUM_APSP.lean and ETHIsFalse.lean cited in '
                           'earlier editions do not appear in the anthropics/formal-math file tree '
                           'read on 2026-11-14; the 28-product '
                           "eight-square claim and the '0 sorry · 100% type-checked' and 'FIPS 203 "
                           "verified' readouts are withdrawn. The ETH refutation is now reported "
                           "only as the eth README's statement. '192-bit quantum security' is "
                           'replaced by NIST security category 3, and FIPS 203 failure rates are '
                           'quoted from its Table 1. Claims of unbreakable privacy and bug-free '
                           'code, the invented 1994 scene and the Imperial College attribution are '
                           'removed; the M.03 DOI is described as FunSearch, which it is. A '
                           'second review the same day retitled the folio away from the withdrawn '
                           'ETH and eight-square claims, phrased every statement about a GitHub '
                           'repository as what its README or file tree showed on 2026-11-14, and '
                           'dropped an unused Stim citation.',
                'opus': 'Review: all DOIs checked in Crossref and the Scite index; the '
                        'formal-math file tree and READMEs and FIPS 203 Tables 1–2 read on '
                        '2026-11-14. No DOIs added.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-07',
                'summary': 'REV 1.0 (Published 2026-11-07): Volume VI Capstone Mathematics '
                           'monograph synthesizing Folios M.01 (DOI 10.2307/2118559), M.03 (DOI '
                           '10.1038/s41586-023-06924-6), and M.06 (DOI 10.1137/15M1024524) with '
                           'anthropics/formal-math and open-quantum-safe/liboqs.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B + Gemma 4 31B): '
                        'Verified Module-LWE ring parameters (q=3329, n=256), EightSquare rank <= '
                        "28, and Lean 4 zero-sorry audit. (REV 1.1: this 'verified' wording is "
                        'withdrawn; no EightSquare.lean appears in the file tree read on '
                        '2026-11-14, and no Lean build was run. '
                        'q = 3329 and n = 256 do match FIPS 203.)'}],
 'volume': 6,
 'volume_code': 'VOL. 06',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1145/1568318.1568324',
           'fetched_on': '2026-11-08',
           'citing_publications': 2512,
           'supporting': 0,
           'mentioning': 708,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (fetched 2026-11-08): 0 retractions; 2,512 '
                      'citing publications (0 supporting, 708 mentioning, 0 contrasting) for '
                      'Regev, On lattices, learning with errors, random linear codes, and '
                      'cryptography (Journal of the ACM, 2009), the paper behind the LWE '
                      'problem used in ML-KEM.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['M.01', 'M.03', 'M.06'],
 'lineage_mode': 'SYNTHESIS · Synthesizes M.01 Lean 4 Modularity, M.03 Tensor Rank & M.06 '
                 'Fine-Grained Complexity',
 'scite': {'doi': '10.1145/1568318.1568324',
           'fetched_on': '2026-11-08',
           'citing_publications': 2512,
           'supporting': 0,
           'mentioning': 708,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (fetched 2026-11-08): 0 retractions; 2,512 '
                      'citing publications (0 supporting, 708 mentioning, 0 contrasting) for '
                      'Regev, On lattices, learning with errors, random linear codes, and '
                      'cryptography (Journal of the ACM, 2009), the paper behind the LWE '
                      'problem used in ML-KEM.'},
 'act1_title': "Act I — Cool Fact & Human Story: Why Quantum Computers Could Break Today's "
               'Internet Locks, and Why Cryptographers Turned to 768-Dimensional Lattices',
 'act1_dropcap': 'In 1994 Peter Shor, then at AT&T Bell Laboratories, published a quantum '
                 'algorithm for factoring integers and computing discrete logarithms in '
                 'polynomial time. If a large enough fault-tolerant quantum computer is ever '
                 'built, it could break the RSA and elliptic-curve systems that protect much of '
                 "today's internet traffic, and data recorded now could be decrypted later. That "
                 'prospect led cryptographers toward problems on high-dimensional lattices, which '
                 'no known quantum algorithm solves efficiently. Proof assistants such as Lean '
                 'offer a different kind of assurance: they check each step of a formal proof '
                 'mechanically, though only for the statements someone has formalised.',
 'act1_plain_bridge': 'Every time you log into your bank, send a text message, or sign a digital '
                      'document on your computer, your privacy depends on a clever mathematical '
                      "padlock. Today's locks work like a one-way street: multiplying two gigantic "
                      'prime numbers together is lightning fast, but unscrambling their product '
                      'back into the original primes takes a conventional supercomputer thousands '
                      'of years. A large future quantum computer could crack those prime-number '
                      'locks. To keep our digital world safe, scientists '
                      'designed a completely new type of padlock based on high-dimensional '
                      'geometric grids called crystal lattices. Imagine a giant egg carton '
                      'floating in hundreds of dimensions, hidden behind a dense cloud of fog. '
                      'Dropping a marble into one specific valley is easy, but finding which '
                      'valley it landed in without the secret blueprint is believed to be '
                      'extremely hard, even for a quantum computer. Machine-checked proof systems '
                      'can inspect mathematical arguments step by step, but they check only what '
                      'has been formalised; no tool guarantees that a lock will never fail.',
 'act1_body': 'In 2024 the National Institute of Standards and Technology published FIPS 203, '
              'the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM). It belongs to the '
              "family of schemes built on Oded Regev's Learning With Errors problem (Journal of "
              'the ACM, DOI 10.1145/1568318.1568324), and open-source implementations exist, '
              'such as https://github.com/open-quantum-safe/liboqs. FIPS 203 fixes n = 256 and q '
              '= 3329 and defines three parameter sets, ML-KEM-512, -768 and -1024, in NIST '
              'security categories 1, 3 and 5. Its security rests on the presumed hardness of '
              'module lattice problems; Regev showed that plain LWE is at least as hard, under a '
              'quantum reduction, as certain worst-case lattice problems, but no one has proved '
              'that these problems are hard. Separately, the public repositories '
              'https://github.com/anthropics/formal-math and '
              'https://github.com/anthropics/fermats-last-theorem state in their READMEs, read on '
              '2026-11-14, that they contain Lean 4 formalisations; this site has not built them. The parent folios of '
              "this synthesis cite Andrew Wiles's modularity paper (Annals of Mathematics, DOI "
              '10.2307/2118559), the FunSearch program-search paper (Nature, DOI '
              "10.1038/s41586-023-06924-6) and Ryan Williams's faster all-pairs shortest paths via "
              'circuit complexity (SIAM Journal on Computing, DOI 10.1137/15M1024524). None of '
              'these formalisations makes a cryptographic implementation bug-free.',
 'act1_stakes': 'Cryptography protects real infrastructure, and an error in a proof or in code '
                'can matter. Paper proofs are reviewed by people who sometimes miss edge cases. '
                'Formalising a reduction in Lean 4 removes one source of doubt: a theorem whose '
                'proof uses no sorry and no extra axioms has been checked by the kernel, though '
                'the statement may still not say what was intended. Moving from factoring to '
                'module lattices is the current best judgment of how to resist quantum '
                'attackers; it is a well-studied bet, not a guarantee.',
 'pullquote': '"Human intuition can be fooled by a long reduction or a subtle edge case. A '
              'proof assistant checks each formal step, but only for the statement as written, '
              'and only if someone builds it."',
 'chronology': [('1994–1995',
                 'Peter Shor publishes polynomial-time quantum factoring; Andrew Wiles resolves '
                 "Fermat's Last Theorem (DOI 10.2307/2118559)."),
                ('2005–2018',
                 'Oded Regev introduces Learning With Errors (LWE) with a quantum reduction from '
                 'worst-case lattice problems; Ryan Williams gives faster all-pairs shortest paths '
                 'via circuit complexity (DOI 10.1137/15M1024524).'),
                ('2024',
                 'NIST publishes FIPS 203 (ML-KEM) and FIPS 204 (ML-DSA); open-source libraries '
                 'such as open-quantum-safe/liboqs implement them.'),
                ('2026',
                 'On 2026-11-14 this site reads the READMEs of the public Lean 4 repositories '
                 'anthropics/formal-math (which lists zeta23, 3sum-apsp and eth) and '
                 'anthropics/fermats-last-theorem.')],
 'act2_title': 'Act II — Cross-Field Intuition: A 768-Dimensional Egg Carton in Thick Fog + The '
               'Unbribable Lean 4 Referee',
 'act2_intuition': 'Why can a quantum computer factor integers efficiently while lattice '
                   'problems are believed to resist it? RSA and elliptic-curve cryptography rest '
                   'on abelian groups whose hidden periodicity a^(x+r) = a^x mod N can be '
                   "extracted by Shor's quantum Fourier transform. Module-LWE works over the ring "
                   'R_q = Z_q[X]/(X^256 + 1) with q = 3329 and module rank k = 3 in ML-KEM-768. '
                   'The public key b = A s + e (mod q) hides the secret vector s behind small '
                   'centered binomial noise e. Recovering s from (A, b) can be phrased as a '
                   'problem on a lattice of dimension 768, and the best known attacks, classical '
                   'or quantum, use lattice reduction and sieving with no exponential quantum '
                   'speedup known. That is evidence, not proof, of hardness.',
 'act2_deepening': 'Regev (2009) showed that solving average-case LWE would let one solve '
                   'certain worst-case lattice problems with a quantum algorithm; analogous '
                   'results for module and ring variants underlie schemes such as ML-KEM. In the '
                   "folio's dashboard, raising the module rank k from 2 to 4 raises the "
                   'dimension of the underlying lattice from 512 to 1024, which makes the known '
                   'lattice-reduction attacks much more expensive. FIPS 203 fixes the noise '
                   'parameters (eta1 = 3 for ML-KEM-512 and 2 for the others; eta2 = 2) and lists '
                   'decapsulation failure rates of 2^-138.8, 2^-164.8 and 2^-174.8 for the three '
                   'parameter sets. Earlier editions also described an EightSquare.lean proof '
                   'that an eight-square bilinear map needs only 28 products; no file of that '
                   'name appears in the anthropics/formal-math file tree read on 2026-11-14, and '
                   'that claim is withdrawn.',
 'act2_analogy': 'Everyday analogy: Imagine an egg carton that stretches across seven hundred '
                 'sixty-eight dimensions, covered in an impenetrable bank of fog. The public key '
                 'is like dropping a tiny marble into one secret indentation near a grid point, '
                 'then giving the whole carton a slight nudge (+e). Without the secret map, a '
                 'searcher, as far as anyone knows even one with a quantum computer, faces an '
                 'astronomical number of similar valleys. But with the private trapdoor, '
                 'the rightful owner reaches straight through the fog and retrieves the marble in '
                 'a microsecond.',
 'act2_plain_primer': 'To understand how this post-quantum lock operates, consider two primary '
                      'adjustments on our cryptographic dashboard. The first adjustment controls '
                      'the geometric dimension or rank of the polynomial crystal lattice, toggling '
                      'between rank two (ML-KEM-512, NIST security category 1), rank three '
                      '(ML-KEM-768, category 3) and rank four (ML-KEM-1024, category 5). As you '
                      'increase this rank, the lattice expands from 512 up to 1,024 dimensions, '
                      'and the cost of the best known attacks rises steeply. The second '
                      'adjustment regulates the width of the binomial noise fog injected into the '
                      'public key. If the fog is too thin, clever algorithms might pinpoint the '
                      'underlying lattice grid; if the fog is too thick, even the legitimate '
                      'receiver might experience a rare decryption error. By dialing these '
                      'controls in unison, you can see why FIPS 203 settles on its parameter '
                      'sets: enough noise to hide the secret, little enough that decapsulation '
                      'failures stay extremely rare. The dashboard curves are a teaching model, '
                      'not a security estimate.',
 'distill_diagram': {'analogy_title': 'The 768-Dimensional Egg Carton',
                     'analogy_sub': 'Retrieving a marble dropped into foggy high-dimensional '
                                    'valleys',
                     'force_a_title': 'Lattice Module Rank k',
                     'force_a_sub': 'Scales crystal dimension from 512D to 1024D against quantum '
                                    'SVP',
                     'force_b_title': 'Binomial Noise Width η',
                     'force_b_sub': 'Injects cryptographic fog while bounding decryption failure '
                                    'risk',
                     'threshold_title': 'Quantum Security vs. Decryption Flaw',
                     'threshold_pass': 'ML-KEM-768: NIST category 3, decapsulation failure '
                                       '2^-164.8 (FIPS 203)',
                     'threshold_fail': 'Insufficient lattice dimension vulnerable to lattice '
                                       'reduction'},
 'walkthrough': ['Experiment 1 (Module-LWE Lattice Rank k): Switch Lattice Rank k across k = 2 '
                 '(ML-KEM-512, NIST category 1), k = 3 (ML-KEM-768, category 3), and k = 4 '
                 '(ML-KEM-1024, category 5). Watch the model hardness curve rise; it is '
                 'illustrative, not a security estimate.',
                 'Experiment 2 (Binomial Lattice Noise Width η): Adjust Noise Width η from 1 to 4. '
                 'Observe the trade-off between LWE cryptographic fog density and decryption '
                 'failure margin.',
                 'Experiment 3 (Quantum ⚛ & Counterfactual ⚡): Click [⚛ Quantum] and [⚡ '
                 'Counterfactual] to inspect the ML-KEM lattice vector geometry. (The former '
                 'EightSquare.lean panel referred to a file that does not appear in the '
                 'anthropics/formal-math file tree read on 2026-11-14.)'],
 'act4_title': "Act IV — Imagining Humanity's Future: Quantum-Resistant Privacy & "
               'Machine-Checked Mathematics',
 'act4_human_ai': 'Open-source post-quantum libraries '
                  '(https://github.com/open-quantum-safe/liboqs) and public Lean 4 repositories '
                  'are two separate efforts. Read on 2026-11-14, the READMEs of '
                  'https://github.com/anthropics/formal-math and '
                  'https://github.com/anthropics/fermats-last-theorem describe machine-checked '
                  'Lean 4 formalisations, the README of https://github.com/teorth/pfr describes '
                  'a Lean 4 formalisation of the polynomial Freiman–Ruzsa conjecture, and the '
                  'README of https://github.com/deepseek-ai/DeepSeek-Prover-V2 describes a '
                  'language model for formal reasoning in Lean 4. The libraries aim at '
                  'privacy that resists known quantum attacks; the repositories, by their own '
                  'account, aim at mathematics whose formalised parts a proof checker accepts. '
                  'Neither offers unbreakable security or freedom from error.',
 'act4_deepening': 'Machine-checked verification and post-quantum engineering could reinforce '
                   'each other. In open verification projects, human mathematicians write the '
                   'blueprints and definitions, and automated tools can help discharge many '
                   'smaller obligations in libraries such as leanprover-community/mathlib4. '
                   'Verifying the code of post-quantum libraries such as '
                   'open-quantum-safe/liboqs is a separate, ongoing task that formal mathematics '
                   'alone does not complete. Compelling open '
                   'mathematical frontiers remain: can we formalize fully machine-checked proofs '
                   'of post-quantum chosen-ciphertext security reductions down to the Lean 4 '
                   'kernel, closing the gap between high-level paper proofs and machine-code '
                   'execution? Furthermore, can tensor rank compression algorithms discover even '
                   'faster arithmetic transforms for ring-polynomial multiplication without '
                   'compromising lattice security margins? Progress on these questions would '
                   'help keep communication and research safer as quantum computing develops.',
 'cf_bridge': 'Standalone Formal Mathematics, Fine-Grained Complexity & Post-Quantum Cryptography '
              'Capstone Flagship (M.01 + M.03 + M.06 -> M.12): Closing Volume VI across all 48 '
              'Folios of Informatico.ai.',
 'sources': ['Regev, O. (2009). On lattices, learning with errors, random linear codes, and '
             'cryptography. Journal of the ACM, 56(6), 1–40. DOI: 10.1145/1568318.1568324.',
             'anthropics/formal-math README and project READMEs (read 2026-11-14): projects '
             'zeta23, 3sum-apsp and eth. GitHub: https://github.com/anthropics/formal-math. '
             'Repository statements; not built by this site.',
             'anthropics/fermats-last-theorem README (read 2026-11-14): states a machine-checked '
             "Lean 4 proof of Fermat's Last Theorem. GitHub: "
             'https://github.com/anthropics/fermats-last-theorem. Repository statement; not built '
             'by this site.',
             'National Institute of Standards and Technology (2024). Module-Lattice-Based '
             'Key-Encapsulation Mechanism Standard. FIPS 203. '
             'https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf.',
             'Williams, R. R. (2018). Faster All-Pairs Shortest Paths via Circuit Complexity. SIAM '
             'Journal on Computing, 47(5), 1965–1985. DOI: 10.1137/15M1024524.',
             "Wiles, A. (1995). Modular Elliptic Curves and Fermat's Last Theorem. Annals of "
             'Mathematics, 141(3), 443–551. DOI: 10.2307/2118559.',
             'Open-source tools a reader could use (not run for this folio): '
             'open-quantum-safe/liboqs (https://github.com/open-quantum-safe/liboqs) and '
             'leanprover-community/mathlib4.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Lean 4 '
        'repository panel and NIST FIPS 203 ML-KEM Module-LWE Post-Quantum '
        'Crystal Lattice">\n'
        '            <line x1="35" y1="188" x2="645" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <text x="44" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">anthropics/formal-math: zeta23 · 3sum-apsp · '
        'eth</text>\n'
        '            <g transform="translate(56, 46)">\n'
        '              <rect x="0" y="0" width="235" height="46" rx="6" fill="var(--tp-stone)" '
        'fill-opacity="0.3" stroke="var(--tp-prussian)" stroke-width="1.8"/>\n'
        '              <text x="12" y="20" font-size="9.5" font-weight="600" '
        'fill="var(--tp-prussian)">Contents as Stated in the READMEs</text>\n'
        '              <text x="12" y="36" font-size="9" '
        'fill="var(--tp-verdigris)">Not Built or Checked by This Site</text>\n'
        '              <line x1="22" y1="74" x2="88" y2="74" stroke="var(--tp-prussian)" '
        'stroke-width="2.4"/>\n'
        '              <line x1="88" y1="74" x2="154" y2="74" stroke="var(--tp-verdigris)" '
        'stroke-width="2.4"/>\n'
        '              <line x1="154" y1="74" x2="215" y2="74" stroke="var(--tp-verdigris)" '
        'stroke-width="2.4"/>\n'
        '              <circle cx="22" cy="74" r="5" fill="var(--tp-prussian)"/>\n'
        '              <circle cx="88" cy="74" r="5" fill="var(--tp-prussian)"/>\n'
        '              <circle cx="154" cy="74" r="5" fill="var(--tp-verdigris)"/>\n'
        '              <circle cx="215" cy="74" r="5.5" fill="var(--tp-verdigris)"/>\n'
        '            </g>\n'
        '            <text x="44" y="176" font-size="9.5" fill="var(--tp-verdigris)">Lean 4: '
        'Checks Only What Is Formalised</text>\n'
        '            <line x1="335" y1="24" x2="335" y2="192" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="354" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">NIST FIPS 203 (ML-KEM): b = A s + e (mod 3329)</text>\n'
        '            <g transform="translate(385, 52)">\n'
        '              <circle cx="0" cy="0" r="3.5" fill="currentColor" fill-opacity="0.45"/>\n'
        '              <circle cx="48" cy="0" r="3.5" fill="currentColor" fill-opacity="0.45"/>\n'
        '              <circle cx="96" cy="0" r="3.5" fill="currentColor" fill-opacity="0.45"/>\n'
        '              <circle cx="144" cy="0" r="3.5" fill="currentColor" fill-opacity="0.45"/>\n'
        '              <circle cx="24" cy="42" r="3.5" fill="currentColor" fill-opacity="0.45"/>\n'
        '              <circle cx="72" cy="42" r="3.5" fill="currentColor" fill-opacity="0.45"/>\n'
        '              <circle cx="120" cy="42" r="5.5" fill="var(--tp-prussian)"/>\n'
        '              <circle cx="168" cy="42" r="3.5" fill="currentColor" fill-opacity="0.45"/>\n'
        '              <circle cx="48" cy="84" r="3.5" fill="currentColor" fill-opacity="0.45"/>\n'
        '              <circle cx="96" cy="84" r="3.5" fill="currentColor" fill-opacity="0.45"/>\n'
        '              <circle cx="144" cy="84" r="3.5" fill="currentColor" fill-opacity="0.45"/>\n'
        '              <line x1="0" y1="84" x2="120" y2="42" stroke="var(--tp-verdigris)" '
        'stroke-width="2.5"/>\n'
        '              <line x1="120" y1="42" x2="136" y2="26" stroke="var(--tp-minium)" '
        'stroke-width="2.2" stroke-dasharray="3,2"/>\n'
        '              <circle cx="136" cy="26" r="4.5" fill="var(--tp-minium)"/>\n'
        '              <text x="128" y="56" font-size="9" fill="var(--tp-prussian)">A·s</text>\n'
        '              <text x="144" y="28" font-size="9" fill="var(--tp-minium)">b = As + '
        'e</text>\n'
        '            </g>\n'
        '            <text x="354" y="176" font-size="9.5" fill="var(--tp-prussian)">R_q = '
        'ℤ_3329[X]/(X²⁵⁶+1) · k = 3 (NIST Category 3)</text>\n'
        '            <text x="44" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Volume VI Capstone · Teaching Diagram, Not a Security '
        'Audit</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a 768-dimensional post-quantum crystal lattice '
        'vault interlocked with a glowing Lean 4 formal proof dependency graph would look like '
        '(artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate M.12-V (Imagining What It Would Look Like) · Artistic '
            'mathematical visualization (synthesizing Folios M.01, M.03 & M.06) imagining a Lean '
            '4 proof dependency graph beside a NIST FIPS 203 Module-LWE post-quantum lattice.'}

DISPATCH = {'kicker': 'FRONTIER LEAN 4 FORMAL VERIFICATION & POST-QUANTUM CRYPTO DISPATCH · '
           'ANTHROPICS/FORMAL-MATH',
 'headline': 'Public Lean 4 Repositories and the NIST FIPS 203 Lattice Standard, Side by Side',
 'body': 'A synthesis of Folios M.01 (Wiles, DOI 10.2307/2118559), M.03 (FunSearch, DOI '
         '10.1038/s41586-023-06924-6) and M.06 (Williams, DOI 10.1137/15M1024524), read beside '
         'what the README of https://github.com/anthropics/formal-math, read on 2026-11-14, says '
         'the repository contains (including a statement, not checked here, that one project '
         'refutes ETH) and the ML-KEM standard implemented in '
         'https://github.com/open-quantum-safe/liboqs.'}

META_3D = ('Module-LWE Crystal Lattice Teaching Surface',
 'X: Lattice Module Rank k · Z: Noise Width η · Y: Illustrative Hardness Curve (Not a Security Estimate)')

ES_TRANSLATION = {'title_es': 'Repositorios públicos de Lean 4 y NIST FIPS 203 (ML-KEM): lo que afirman, '
             'uno al lado del otro',
 'subtitle_es': 'Sintetizando los Folios M.01, M.03 y M.06: lo que el README del repositorio '
                'público de Lean 4 anthropics/formal-math, consultado el 14 de noviembre de 2026, '
                'dice que contiene (incluido un proyecto eth que, según el README, refuta la '
                'Hipótesis del Tiempo Exponencial, una afirmación que este sitio no ha '
                'comprobado), junto al estándar de encapsulamiento de claves con retículos NIST '
                'FIPS 203 (ML-KEM).',
 'why_es': 'Un cartón de huevos en 768 dimensiones envuelto en niebla esconde la llave privada; '
           'hasta donde se sabe, ni una computadora cuántica encuentra el valle más cercano con '
           'eficiencia. Es una creencia bien estudiada, no una prueba.',
 'plain_es': 'En 1994, el matemático Peter Shor publicó un algoritmo cuántico que, si algún día '
             'se construyera una computadora cuántica lo bastante grande, permitiría romper los '
             'candados matemáticos que protegen buena parte de nuestras comunicaciones. Durante treinta años, la seguridad de internet dependió de la dificultad de '
             'descomponer números gigantescos en sus factores primos. Para defender el futuro '
             'digital, los científicos desarrollaron candados post-cuánticos basados en retículos '
             'cristalinos de cientos de dimensiones. Imaginen un enorme cartón de huevos '
             'suspendido en 768 dimensiones y oculto tras una densa niebla. Colocar una canica en '
             'un hueco específico es facilísimo para el dueño que tiene el mapa privado, pero para '
             'un intruso o una computadora cuántica que busca a ciegas entre billones de valles '
             'parecidos, la tarea se considera extremadamente difícil. Los asistentes de '
             'demostración formal como Lean 4 revisan paso a paso los argumentos que alguien ha '
             'formalizado, pero no garantizan que un candado nunca falle.',
 'deep_es': 'La seguridad del estándar post-cuántico NIST FIPS 203 (ML-KEM) depende del '
            'equilibrio entre dos parámetros clave: el rango del retículo modular y el ancho del ruido binomial '
            'centrado. Al seleccionar un rango k entre dos y cuatro, la dimensión del espacio '
            'polinomial se expande de 512 a 1,024 dimensiones, elevando la resistencia '
            'criptográfica ante algoritmos cuánticos de reducción de base como BKZ. Al mismo '
            'tiempo, el ancho del ruido inyecta una niebla controlada que oculta la clave privada '
            'manteniendo los fallos de desencapsulado muy raros (2^-164.8 para ML-KEM-768, según '
            'la Tabla 1 de FIPS 203). Por separado, según su README consultado el 14 de '
            'noviembre de 2026, el repositorio anthropics/formal-math dice contener tres '
            'proyectos de Lean 4 (zeta23, 3sum-apsp y eth); este sitio no los ha compilado. Los '
            'archivos EightSquare.lean y ETHIsFalse.lean que citaban ediciones anteriores no '
            'aparecen en el árbol de archivos del repositorio consultado ese mismo día. Ninguna de estas herramientas vuelve inquebrantable la '
            'privacidad: los retículos son la mejor apuesta actual, bien estudiada, no una '
            'garantía.',
 'bridge_es': 'Folio de cierre del Volumen VI (M.01 + M.03 + M.06 -> M.12), sobre matemáticas '
              'formales, complejidad de grano fino y criptografía post-cuántica.'}
