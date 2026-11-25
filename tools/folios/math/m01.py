#!/usr/bin/env python3
"""Folio M.01 (MATH): Modularity Lifting, Spectral Zero-Density Barriers, and #3-SAT Sparsification."""
from __future__ import annotations

SLUG = 'm01'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.01',
 'slug': 'm01',
 'pillar': 'math',
 'category_code': 'M',
 'title': 'Modularity Lifting, Spectral Zero-Density Barriers, and #3-SAT Sparsification',
 'subtitle': "A reading of the Taylor-Wiles patching argument behind Fermat's Last Theorem, and of "
             'a public Lean 4 repository that states it formalises the proof, drawn as an energy '
             "landscape. The landscape and the ion-channel comparison are this folio's own analogy.",
 'date_published': '2026-10-18',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.5',
 'status_badge': 'REDATED REV 1.5',
 'primary_kernel': 'tools/discovery/formal_proof_thermodynamic_landscape.py',
 'colophon': {'identifier': 'M.01 · Modularity & Counting',
              'kernels': 'FLT · Taylor-Wiles R=T · #3-SAT sparsification',
              'benchmarks': 'Model values only: barrier 8.39 → 3.59 (illustrative units) · no proof was built or checked here',
              'bridge': 'Taylor-Wiles R=T ↔ dual-corrector rescue (analogy only)'},
 'sliders': [{'label': 'Exponent Axiom Mutation (p = 2 Pythagorean vs p ≥ 3)',
              'min': 2,
              'max': 11,
              'step': 1,
              'value': 5,
              'unit': 'p = '},
             {'label': 'ETH #3-SAT Clause Density (α = m / n)',
              'min': 2.5,
              'max': 6.0,
              'step': 0.02,
              'value': 4.26,
              'unit': 'α = '}],
 'steps': ['Stage 1 (Frey Curve & Semistability): Maps a^p + b^p = c^p to a semistable elliptic '
           'curve E/Q with minimal discriminant Δ_E = 2^(-8)(abc)^(2p).',
           'Stage 2 (Ribet Level-Lowering): Establishes that the mod-p Galois representation ρ_{E,p} is '
           'modular of level N = 2, creating a high-energy deductive bottleneck.',
           'Stage 3 (Taylor-Wiles R_Q = T_Q Patching): Auxiliary sets of primes Q_N make the '
           'comparison of R and T tractable. The folio draws this as a barrier falling from 8.39 '
           'to 3.59 in kcal/mol-style units; those two numbers are illustrative model values, '
           'not quantities found in the mathematics.',
           'Stage 4 (Cusp Form Contradiction): Forces ρ_{E,p} into weight-2 cusp forms '
           'S_2(Γ_0(2)), where dim S_2(Γ_0(2)) = 0 closes the proof.'],
 'readouts': [{'label': 'Effective Peak Barrier (model)', 'value': '3.59 vs 8.39 (illustrative units)'},
              {'label': 'Alluvial Hypothesis Flux (model)', 'value': '68.4% (illustrative)'},
              {'label': '#3-SAT Claim in formal-math/eth', 'value': '2^o(n) stated by its README (not checked here)'},
              {'label': 'Lean 4 Repository Statement', 'value': '29,511 theorems per README (not built here)'}],
 'sidenote_1': {'kicker': 'SIDENOTE M.01-A · COUNTERFACTUAL P = 2',
                'body': 'For exponent 2 the equation has solutions, such as 3² + 4² = 5², so the '
                        'argument must fail there, and it does: the Frey-curve contradiction is '
                        "only available for exponents of 3 and above. In the folio's model the "
                        'flux readout drops to 3.2% at p = 2, an illustrative value. Comparing '
                        'this with a truncated ion channel is a loose analogy and nothing more.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.01-B · A LOOSE ANALOGY WITH TWO-SITE CORRECTION',
                'body': 'Fiedorczuk & Chen (2022, DOI 10.1126/science.ade2216; PDB 8EIQ) report '
                        'that elexacaftor alone partially rectified interdomain assembly defects '
                        'in Δ508 CFTR and did so fully when combined with a type I corrector. The '
                        'folio borrows only the picture of two aids doing together what one '
                        'cannot. No mathematics passes between number theory and protein folding.'},
 'skill': {'filename': 'formal-math-modularity-SKILL.md',
           'name': 'formal-math-modularity',
           'description': 'AI-agnostic formal mathematics skill for Lean 4 FLT modularity lifting '
                          '(R=T), Ribet level-lowering, and #3-SAT sunflower sparsification.',
           'rules': ['Verify Frey curve semistability for prime exponent p >= 3 vs counterfactual '
                     'p = 2 Pythagorean collapse (3^2 + 4^2 = 5^2).',
                     'Enforce Taylor-Wiles auxiliary prime patching R_Q = T_Q and cusp-form '
                     'dimension dim S_2(Gamma_0(2)) = 0.',
                     'Bound #3-SAT worst-case time by Impagliazzo-Paturi-Zane sunflower '
                     'sparsification 2^(s_3 * n) near alpha_c = 4.26.']},
 'revisions': [{'edition': 'REV 1.5',
                'date': '2026-11-14',
                'summary': 'REV 1.5 (Redated 2026-11-14): Grounding revision. Earlier editions '
                           "said in the site's own voice that a 29,500-lemma Lean 4 proof was "
                           "'QED verified' with 'zero sorryAx', and that the Exponential Time "
                           'Hypothesis had been refuted. Nobody at this site built or checked '
                           'those repositories, so the page now reports only what their READMEs '
                           'state (29,511 theorems for anthropics/fermats-last-theorem; a 2^o(n) '
                           '#3-SAT algorithm for anthropics/formal-math/eth) and says so. The '
                           'barrier values 8.39 and 3.59 and the flux percentages are labelled as '
                           'illustrative model values and no longer cited to Wiles 1995. The '
                           "opening scene of Fermat by a hearth in Castres and the claims that "
                           'these results make encryption unbreakable are removed. The Cystic '
                           'Fibrosis comparison is marked as an analogy and sourced to Fiedorczuk '
                           '& Chen 2022.',
                'opus': 'Review: every DOI checked in Crossref and the Scite index on 2026-11-14; '
                        'both repository READMEs read on that date. Taylor & Wiles 1995 (DOI '
                        '10.2307/2118560), Impagliazzo, Paturi & Zane 2001 (DOI '
                        '10.1006/jcss.2001.1774) and Fiedorczuk & Chen 2022 (DOI '
                        '10.1126/science.ade2216) were added to the source list.'},
               {'edition': 'REV 1.4',
                'date': '2026-11-06',
                'summary': 'REV 1.4 (Redated 2026-11-06): Integrated late-October 2026 '
                           'anthropics/formal-math ETHIsFalse refutation (Challenge.lean, 2^o(n) '
                           '#3-SAT algorithm via Eight-Square Identity and SWAP = I - 2*singlet, '
                           's_3 = 0) and synchronized the 26-release Frontier AI & Formal Math '
                           'Catalog across 13 research organizations. (REV 1.5: withdrawn as stated. No file named ETHIsFalse was found in that repository on 2026-11-14, and the refutation is the repository\'s own unchecked claim.)',
                'opus': 'Cross-model check (Gemini 4 Argon + Gemma 4 31B + Ornith 1.5 '
                        '35B): Verified ETHIsFalse s_3 = 0 phase-transition update, Eight-Square '
                        'norm conservation, and zero sorryAx contamination. (REV 1.5: this '
                        "'verified' wording is withdrawn; the repository was not built or checked "
                        'by this site.)'},
               {'edition': 'REV 1.3',
                'date': '2026-11-02',
                'summary': 'REV 1.3 (Redated 2026-11-02): Earlier edition (superseded and withdrawn in REV 1.5) '
                           'that modeled the 5-stage FLT Boltzmann landscape alongside an '
                           'allosteric transmembrane channel dual-corrector analogy.',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Taylor-Wiles R=T patching activation barrier Delta G‡ = 3.59 kcal/mol and '
                        'Frey curve semistability discriminant. (REV 1.5: the barrier is an '
                        "illustrative model value; the 'zero sorryAx' and 'full isomorphism' "
                        'wording of this edition is withdrawn.)'},
               {'edition': 'REV 1.2',
                'date': '2026-11-01',
                'summary': 'REV 1.2 (Redated 2026-11-01): Coupled 5-stage FLT Boltzmann landscape '
                           'with ETH #3-SAT sparsification and exported canonical SHA-256 snapshot '
                           'to cf-research.',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'counterfactual p=2 Pythagorean collapse and dim S_2(Gamma_0(2)) = 0 '
                        'terminal obstruction.'},
               {'edition': 'REV 1.1',
                'date': '2026-10-25',
                'summary': 'REV 1.1 (Redated 2026-10-25): Added Noether-Kirchhoff alluvial '
                           'deductive flux conservation across proof tactics.',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified zero '
                        'sorryAx contamination across transitive dependency cones. (REV 1.5: '
                        'wording withdrawn; no such check was run by this site.)'},
               {'edition': 'REV 1.0',
                'date': '2026-10-18',
                'summary': 'REV 1.0 (Published 2026-10-18): Initial publication of the Lean 4 '
                           "Fermat's Last Theorem thermodynamic landscape.",
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'baseline Kramers escape rate across the Ribet level-lowering '
                        'bottleneck.'}],
 'governing_law': 'FLT · Taylor-Wiles R=T · #3-SAT sparsification',
 'governing_law_latex': r"a^p + b^p = c^p \;(p \ge 3) \;\Longrightarrow\; R_{\mathbb{Q}} \cong \mathbb{T}_{\mathbb{Q}}, \\ \dim\,S_2(\Gamma_0(2)) = 0",
 'volume': 1,
 'volume_code': 'VOL. 01',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.2307/2118559',
           'fetched_on': '2026-11-08',
           'citing_publications': 2170,
           'supporting': 8,
           'mentioning': 1292,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Wiles 1995 (DOI 10.2307/2118559), checked '
                      '2026-11-08: 2,170 citing publications (8 supporting, 1,292 mentioning, 0 '
                      'contrasting) and no retraction notice. These counts describe that one '
                      'paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'act1_dropcap': "Around 1637 (the date is traditional rather than documented) the French lawyer and mathematician Pierre de Fermat wrote a note in the margin of his copy of the Arithmetica of Diophantus, in Claude Bachet's Latin edition. Beside the eighth problem of the second book, which asks for a square to be divided into two squares, he remarked that a cube cannot be split into two cubes, nor a fourth power into two fourth powers, nor in general any power above the second into two like powers. He added that he had found a truly marvellous proof which the margin was too narrow to contain. The note became public only after his death in 1665, when his son Samuel printed an edition of the Arithmetica with his father's annotations in 1670. No general proof by Fermat has ever been found. The statement then resisted every attempt for more than three and a half centuries.",
 'act1_plain_bridge': "In plain words, Fermat asked whether simple building blocks can assemble into larger structures without leaving leftover fragments. When you tile a kitchen floor with square tiles, you can easily arrange two smaller squares to form a third, just like the classic three, four, five right triangle. But if you try to pack cubic blocks into a larger cube, solid geometry creates unavoidable corners and gaps. For centuries, this puzzle seemed like an isolated curiosity about whole numbers. Yet settling that playful question took some of the deepest mathematics of the twentieth century. One of its main objects, the elliptic curve, is also used in a widely deployed family of public-key cryptography. That is a shared object, not a consequence: the proof of Fermat's Last Theorem does not make any cipher secure, and the security of elliptic-curve cryptography rests on separate assumptions that remain unproved.",
 'act1_body': "The historical impasse broke only when modern mathematicians stopped treating integer equations as isolated puzzles and linked them to two profound geometric realms: elliptic curves and modular forms. In the mid-1980s Gerhard Frey observed that a hypothetical counterexample would give a semistable elliptic curve so unusual that it should not be modular. After Ken Ribet established the level-lowering statement known as the epsilon conjecture in 1986, Andrew Wiles worked for about seven years, largely in private, on the Taniyama–Shimura modularity conjecture for semistable elliptic curves. A gap was found in 1993; Wiles, working with Richard Taylor, repaired it in September 1994, and the two papers appeared in 1995 (Annals of Mathematics, DOI 10.2307/2118559 and DOI 10.2307/2118560). In 2026 a public repository, https://github.com/anthropics/fermats-last-theorem, published Lean 4 sources that its README describes as a complete, machine-checked proof of the theorem, with a page for each of 29,511 theorems, and with portions derived from the Imperial College London formalisation project led by Kevin Buzzard (https://github.com/ImperialCollegeLondon/FLT). Those are the repository's own statements. This site has not built or checked the proof.",
 'act1_stakes': "Turning a proof of more than a hundred pages into something a computer can check matters for a plain reason. Mathematical consensus has long depended on human refereeing, and subtle missteps can hide inside dense calculations. Wiles's first announced argument had such a gap, in its use of an Euler system, and closing it took about a year. A proof assistant such as Lean 4 replaces part of that trust with a mechanical check: every definition and lemma has to be accepted by a small kernel, and no step can be skipped. What a kernel cannot check is whether the formal statement means what a reader thinks it means, or whether an intermediate theorem deserves its name. The README of the Fermat repository says as much, and that reading is still a human job. For this page it also means one more thing: a claim that a proof is machine-checked is a claim about a build that someone has to run, and this site has not run it.",
 'pullquote': 'What took humanity 358 years to bridge by hand was not a lack of calculation, but a '
              'hidden phase transition between local deformations and global modular symmetry.',
 'pullquote_cite': "Editorial comment by this folio, in a thermodynamic metaphor · From Fermat's "
                   'margin note to the 1995 proof',
 'chronology': [('1637',
                 'Pierre de Fermat',
                 "Writes the marginal note in Diophantus's Arithmetica claiming a^n + b^n = c^n "
                 'has no positive integer solutions for n >= 3.'),
                ('1847',
                 'Ernst Kummer',
                 'Introduces ideal complex numbers and establishes FLT for regular primes, exposing the '
                 'class-group obstruction at irregular primes.'),
                ('1984–1986',
                 'Gerhard Frey & Ken Ribet',
                 'Frey links hypothetical solutions to a semistable elliptic curve; Ribet establishes '
                 'level-lowering onto weight-2 cusp forms of level N = 2.'),
                ('1994',
                 'Andrew Wiles & Richard Taylor',
                 'Resolve the deformation-ring bottleneck via the Taylor-Wiles auxiliary prime '
                 'patching bridge (R_Q = T_Q) and p = 3 <-> p = 5 switch.'),
                ('2024–2026',
                 'Lean 4 formalisation projects',
                 'The Imperial College London project led by Kevin Buzzard is public and '
                 'describes itself as ongoing. In 2026 the repository '
                 'anthropics/fermats-last-theorem states a complete machine-checked proof with '
                 '29,511 theorems. Not built or checked by this site.')],
 'act2_analogy': 'Everyday analogy: Imagine building a sweeping stone arch bridge across a turbulent mountain gorge. If you attempt to hoist a single massive stone beam across the gap, the material fractures under its own bending weight. However, by erecting temporary wooden scaffold towers in the riverbed, builders support intermediate blocks and relieve shear stress until the final keystone locks into place. Once the arch achieves self-supporting geometric equilibrium, the temporary scaffolding can be dismantled completely, leaving an enduring bridge.',
 'act2_plain_primer': 'Before looking at any equations, you can understand how this mathematical bridge operates through two intuitive control knobs. The first knob controls the geometric building block, shifting from flat squares to rigid three-dimensional cubes and higher dimensions. When this exponent knob rests at two, numbers fit together like flat square tiles on a bathroom floor, making balanced combinations easy to find. But as soon as you turn the knob to three or higher, the geometry stiffens, making it impossible for two integer blocks to combine into a third without leaving cracks. The second knob measures congestion, tracking how many overlapping rules or constraints crowd into the workspace. When rules are sparse, candidate shapes can flex and wiggle freely. But as congestion rises toward a critical tipping point, every local adjustment collides with neighboring constraints. To show that no illegal shape can survive, mathematicians use the temporary scaffolding from our bridge analogy to establish that every possible path collapses into a rigid dead end.',
 'distill_diagram': {'analogy_title': 'Scaffolded Stone Arch Bridge', 'analogy_sub': 'Temporary piers hold the span until keystones lock in balance', 'force_a_title': 'Exponent Axiom Mutation (p)', 'force_a_sub': 'Switches from Pythagorean squares to rigid higher-power geometry', 'force_b_title': 'Constraint Density (alpha)', 'force_b_sub': 'Tuning clause crowding toward the critical satisfiability cliff', 'threshold_title': 'Taylor-Wiles Modularity Barrier (R = T)', 'threshold_pass': 'Auxiliary primes patch the gap; cusp space collapses to zero', 'threshold_fail': 'Unpatched deformation ring stalls at the 8.39 model barrier (illustrative)'},
 'act2_intuition': 'Why do both formal mathematical deductions and complex computational searches suddenly freeze at an impassable wall? Picture an alpine expedition traversing a jagged ridge at midnight. A naive search examines every single boulder one by one—the brute-force equivalent of exploring exponential trees in the Exponential Time Hypothesis for #3-SAT at critical clause density alpha_c = 4.26. This folio pictures each deduction step as a mountain pass with a barrier height Delta G^‡. That picture is a metaphor of the folio, with made-up units; a proof has no temperature and no free energy. In the picture, the Taylor–Wiles patching method (R_Q = T_Q) plays the part of a catalyst. Instead of comparing the universal deformation ring R with the Hecke algebra T directly, which the folio draws as a barrier of 8.39, the method brings in an infinite sequence of auxiliary sets of primes Q_N that relax local ramification conditions, which the folio draws as a lower barrier of 3.59. Both numbers are illustrative model values chosen for the diagram; they appear in no paper. The mathematics itself is in Wiles (1995, DOI 10.2307/2118559) and Taylor & Wiles (1995, DOI 10.2307/2118560). Passing to the limit removes the auxiliary scaffolding, and the mod-p representation of the Frey curve would then have to come from a weight-2 cusp form in S_2(Gamma_0(2)), a space of dimension zero.',
 'act2_deepening': 'At a deeper structural level, the isomorphism R = T establishes a perfect dictionary between geometry and arithmetic. The deformation ring R classifies all continuous deformations of a Galois representation into matrix representations over complete local rings, while the Hecke algebra T captures the spectral eigenvalues of modular forms acting on differential forms. Before patching, the tangent space of R contains excessive obstruction classes, creating a gap between local symmetries and global modularity. By selecting auxiliary primes Q_N where the Frobenius trace matches specific eigenvalue congruences, Taylor and Wiles added controlled generators to both R_Q and T_Q. This turned both objects into free modules of finite rank over a formal power series ring. When the auxiliary primes are patched together across the projective limit, the excess variables cancel symmetrically to yield R = T. Simultaneously, coupling this deformation space to the clause density slider demonstrates how combinatorial constraints undergo a sharp phase transition from flexible satisfiability to rigid contradiction.',
 'walkthrough': ['Experiment 1 (Walk the 4-Stage Proof Stepper): Click Stages 1 -> 4 in the '
                 "interactive plate above. Watch how Frey's curve (Stage 1) and Ribet's "
                 'level-lowering (Stage 2) build tension up to the Taylor-Wiles R = T bridge '
                 '(Stage 3) before collapsing into dim S_2(Gamma_0(2)) = 0 (Stage 4).',
                 'Experiment 2 (Trigger the Counterfactual p = 2 Pythagorean Knockout): Drag the '
                 'Exponent slider all the way left to p = 2. Instantly, semistability fractures, '
                 'the Pythagorean solution 3^2 + 4^2 = 5^2 appears, and the model flux readout '
                 'drops from 68.4% to 3.2% (both illustrative values).',
                 'Experiment 3 (Probe the #3-SAT Clause Density): Scrub the Clause Density '
                 'slider across alpha = 4.26, close to the empirically observed satisfiability '
                 'threshold of random 3-SAT. The exponent 2^(0.385 n) shown in the lab is a '
                 'fixed illustrative value, not a proved bound.'],
 'act4_human_ai': 'Before formal proof assistants and frontier reasoning councils, a 100-page proof could only be checked by a handful of human specialists over months of line-by-line refereeing. With a proof assistant, a mathematician can lay out a dependency blueprint, people or AI agents can attempt the individual lemmas, and the Lean kernel rejects any step that does not follow. The README of anthropics/fermats-last-theorem states that its Lean sources were produced by AI agents building on human-written open-source Lean, and that its final check fails unless the proof rests on exactly the three standard axioms of Lean, with no sorry. The anthropics/formal-math repository carries an eth project whose README states a deterministic 2^o(n) algorithm for #3-SAT, which would refute the Exponential Time Hypothesis of Impagliazzo, Paturi & Zane (2001, DOI 10.1006/jcss.2001.1774). These are statements of the repositories. This site has not run either build and does not vouch for the mathematics; a claim of that size needs independent expert review.',
 'act4_deepening': 'Modern formalization projects demonstrate a new paradigm of collaborative research where human mathematicians and automated theorem provers divide labor according to cognitive strengths. Human architects design the blueprint graph, defining the high-level structural lemmas, strategic reductions, and topological definitions that give a proof its meaning. Automated tactic engines and machine-learning models then explore the granular combinatorial branches, discharging thousands of routine algebraic rearrangements and inductive obligations. Crucially, the interactive theorem prover acts as an incorruptible judge: no claim is accepted based on plausibility or stylistic elegance until its formal derivation passes kernel type verification. Looking toward the horizon, this hybrid methodology opens unprecedented avenues for exploring the Langlands program. Frontier questions concerning modularity lifting for higher-dimensional Calabi–Yau varieties, automorphic representations over general number fields, and the Birch and Swinnerton-Dyer conjecture are becoming amenable to distributed human-machine campaigns, transforming what once required centuries of solitary struggle into systematically verifiable collective milestones.',
 'cf_bridge': 'This bridge is an analogy and nothing more. In Cystic Fibrosis the most common '
              'mutation, the deletion of phenylalanine 508 in the CFTR protein, causes severe '
              'defects in how the protein is made and assembled. Fiedorczuk & Chen (2022, DOI '
              '10.1126/science.ade2216; PDB 8EIQ) solved cryo-electron microscopy structures of '
              'Δ508 CFTR and report that elexacaftor alone partially rectified interdomain '
              'assembly defects and, combined with a type I corrector, did so fully. The folio '
              'likes the resemblance to a proof step that needs two supports at once, but number '
              'theory tells us nothing about protein folding, and nothing here is medical '
              'advice. The p = 2 case is used in the same loose spirit: some CFTR variants, such '
              'as the nonsense variants G542X and W1282X, stop the protein from being made in '
              'full, and correctors of this kind are not expected to help when there is no '
              'full-length protein to correct.',
 'sources': ["Wiles, A. (1995). Modular elliptic curves and Fermat's Last Theorem. Annals of "
             'Mathematics, 141(3), 443–551. DOI: 10.2307/2118559.',
             'Taylor, R., & Wiles, A. (1995). Ring-theoretic properties of certain Hecke algebras. '
             'Annals of Mathematics, 141(3), 553–572. DOI: 10.2307/2118560.',
             'Impagliazzo, R., Paturi, R., & Zane, F. (2001). Which problems have strongly '
             'exponential complexity? Journal of Computer and System Sciences, 63(4), 512–530. '
             'DOI: 10.1006/jcss.2001.1774.',
             "Repository: anthropics/fermats-last-theorem, Fermat's Last Theorem in Lean 4 "
             '(https://github.com/anthropics/fermats-last-theorem). README read 2026-11-14: it '
             'states a complete machine-checked proof, 29,511 theorem pages, and portions '
             'derived from ImperialCollegeLondon/FLT (https://github.com/ImperialCollegeLondon/FLT), '
             'flt-regular and Mathlib. Not built or checked by this site.',
             'Repository: anthropics/formal-math (https://github.com/anthropics/formal-math), '
             'projects zeta23, 3sum-apsp and eth. README read 2026-11-14: the eth project '
             'states a 2^o(n) algorithm for #3-SAT. Not built or checked by this site. Earlier '
             'editions also listed a RISC-V proof repository; no public repository of that name '
             'was found on 2026-11-13 and the reference is withdrawn.',
             'The mathlib Community (2020). The Lean mathematical library. CPP 2020, 367–381. '
             'DOI: 10.1145/3372885.3373824.',
             'Fiedorczuk, K., & Chen, J. (2022). Molecular structures reveal synergistic rescue '
             'of Δ508 CFTR by Trikafta modulators. Science, 378(6617), 284–290. DOI: '
             '10.1126/science.ade2216.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Boltzmann proof '
        'barrier reduction and Taylor-Wiles patching">\n'
        '            <line x1="50" y1="185" x2="640" y2="185" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <polyline points="70,150 190,115 320,90 460,38 590,165" fill="none" '
        'stroke="currentColor" stroke-opacity="0.35" stroke-width="2" stroke-dasharray="5,4"/>\n'
        '            <polyline points="70,150 190,115 320,104 460,110 590,170" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="3"/>\n'
        '            <circle cx="70" cy="150" r="6" fill="var(--tp-prussian)"/><circle cx="190" '
        'cy="115" r="6" fill="var(--tp-prussian)"/>\n'
        '            <circle cx="320" cy="104" r="6" fill="var(--tp-verdigris)"/><circle cx="460" '
        'cy="110" r="7" fill="var(--tp-minium)"/>\n'
        '            <circle cx="590" cy="170" r="6" fill="var(--tp-verdigris)"/>\n'
        '            <text x="55" y="205" font-size="11" fill="currentColor">1. Frey Curve</text>\n'
        '            <text x="165" y="205" font-size="11" fill="currentColor">2. Ribet '
        'Level-2</text>\n'
        '            <text x="285" y="205" font-size="11" fill="currentColor">3. p=3 ↔ p=5</text>\n'
        '            <text x="415" y="205" font-size="11" fill="currentColor">4. R_Q = T_Q '
        'Bridge</text>\n'
        '            <text x="555" y="205" font-size="11" fill="currentColor">5. '
        'S_2(Γ_0(2))=0</text>\n'
        '            <text x="395" y="30" font-size="11" fill="var(--tp-minium)">Unbridged '
        'barrier: 8.39 (model value)</text>\n'
        '            <text x="390" y="136" font-size="11" fill="var(--tp-prussian)">Patched R=T '
        'barrier: 3.59 (model value)</text>\n'
        '          </svg>',
 'scite': {'doi': '10.2307/2118559',
           'fetched_on': '2026-11-08',
           'citing_publications': 2170,
           'supporting': 8,
           'mentioning': 1292,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Wiles 1995 (DOI 10.2307/2118559), checked '
                      '2026-11-08: 2,170 citing publications (8 supporting, 1,292 mentioning, 0 '
                      'contrasting) and no retraction notice. These counts describe that one '
                      'paper, not this folio.'}}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a modular elliptic curve torus bridging to a '
        'Galois representation lattice across a potential saddle would look like (artistic '
        'impression, not a formal diagram)',
 'caption': 'Conceptual Vision Plate M.01-V (Imagining What It Would Look Like) · Artistic '
            'geometric metaphor imagining the Taylor-Wiles R = T modularity bridge connecting an '
            'elliptic curve torus to a crystalline Galois lattice.'}

DISPATCH = {'kicker': "FORMAL PROOF DISPATCH · LEAN 4 AND FERMAT'S LAST THEOREM · REPORTED, NOT CHECKED HERE",
 'headline': "A Public Lean 4 Repository States a Complete Formal Proof of Fermat's Last Theorem",
 'body': "Andrew Wiles's proof appeared in the Annals of Mathematics in 1995 (DOI "
         '10.2307/2118559), with the companion paper by Taylor and Wiles (DOI 10.2307/2118560). '
         'The repository https://github.com/anthropics/fermats-last-theorem states that it holds '
         'a complete machine-checked Lean 4 proof following Frey, Serre, Ribet, Wiles and '
         'Taylor-Wiles, with a page for each of 29,511 theorems, built in part on the Imperial '
         'College London project led by Kevin Buzzard. This site reports that statement. It has '
         'not built the repository or checked the proof.'}

META_3D = ('Lean 4 Fermat / Taylor–Wiles Modularity Bridge',
 'X: 5-Stage Proof Chain (Frey → QED) · Z: Deformation Ring Axis · Y: Formal Proof Barrier Height')

ES_TRANSLATION = {'title_es': 'Levantamiento de Modularidad, Barreras de Densidad de Ceros Espectrales y '
             'Esparsificación de #3-SAT',
 'subtitle_es': 'Una lectura del argumento de parchado de Taylor–Wiles detrás del Último Teorema '
                'de Fermat, y de un repositorio público en Lean 4 que afirma formalizar la '
                'demostración, dibujada como un paisaje de energía. El paisaje y la comparación '
                'con canales iónicos son una analogía de este folio.',
 'why_es': 'En la metáfora de este folio, el parchado de Taylor–Wiles (R_Q = T_Q) actúa como un '
           'catalizador: en vez de cruzar una barrera de un solo salto, construye escalones '
           'auxiliares. Los valores de barrera que muestra la página son ilustrativos.',
 'bridge_es': 'Es solo una analogía: Fiedorczuk y Chen (2022, DOI 10.1126/science.ade2216) '
              'reportan que elexacaftor por sí solo corrige parcialmente los defectos de '
              'ensamblaje entre dominios de la CFTR Δ508 y que, combinado con un corrector de '
              'tipo I, los corrige por completo. La teoría de números no dice nada sobre el '
              'plegamiento de proteínas y nada de esto es consejo médico.',
 'plain_es': 'En palabras sencillas, el Último Teorema de Fermat plantea una pregunta muy clara sobre cómo encajan las piezas en nuestro universo: ¿es posible combinar dos potencias perfectas para formar una tercera de la misma dimensión? Con cuadrados planos es sencillo, como cuando colocamos losetas en el piso de la cocina siguiendo el clásico triángulo de lados tres, cuatro y cinco. No obstante, al intentar apilar bloques tridimensionales para formar un cubo perfecto más grande, la geometría rígida deja huecos inevitables. Pierre de Fermat escribió en 1637 que esto era imposible para cualquier potencia mayor que dos, pero dejó al mundo sin su demostración. Lo fascinante es que este misterio no era una simple curiosidad aritmética. Para resolverlo, los matemáticos tuvieron que construir puentes entre universos que parecían no tener relación: las curvas elípticas y las formas modulares. Uno de esos objetos, la curva elíptica, también se usa en una familia muy extendida de criptografía de clave pública. Es un objeto compartido, no una consecuencia: la demostración del teorema de Fermat no vuelve seguro ningún cifrado, y la seguridad de la criptografía de curvas elípticas depende de supuestos distintos que siguen sin demostrarse.',
 'deep_es': 'El núcleo matemático de esta demostración se comprende al observar la interacción entre dos parámetros fundamentales: el exponente geométrico y la densidad de restricciones del sistema. En el deslizador del exponente, el valor dos permite que los enteros se acomoden en perfecta simetría pitagórica; pero en cuanto el exponente sube a tres o más, la deformación de la curva elíptica de Frey genera un discriminante imposible. Por su parte, la densidad de restricciones determina si las ramas lógicas encuentran una salida o chocan contra una contradicción total. El obstáculo histórico consistía en que comparar directamente el anillo de deformaciones con el álgebra de Hecke era demasiado difícil; este folio lo dibuja como una barrera alta. Andrew Wiles y Richard Taylor resolvieron el bloqueo introduciendo primos auxiliares que actúan como un andamio temporal; el folio lo dibuja como una barrera más baja. Los dos valores de barrera, 8.39 y 3.59, son valores ilustrativos del modelo y no aparecen en ningún artículo. Una vez que las piezas embonan en el límite, el andamio se retira y la forma cuspidal buscada tendría que vivir en un espacio de dimensión cero. El repositorio público anthropics/fermats-last-theorem afirma contener una demostración completa verificada en Lean 4, con 29,511 teoremas; este sitio reporta esa afirmación y no ha compilado ni revisado la demostración.'}
