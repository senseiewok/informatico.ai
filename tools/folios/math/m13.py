#!/usr/bin/env python3
"""Folio M.13 (MATH): The SAIR Lean Kernel Challenge: Trusted Type-Checking, Reflection & Proof-Term Reduction."""
from __future__ import annotations

SLUG = 'm13'

PILLAR = 'math'

FOLIO = {
 'folio_id': 'M.13',
 'slug': 'm13',
 'pillar': 'math',
 'category_code': 'M',
 'parent_folios': ['M.01', 'M.12'],
 'lineage_mode': 'CONTINUATION · Extends M.01 Formal Proof Checking & M.12 Lean 4 Context to the SAIR Lean Kernel Challenge',
 'title': 'The SAIR Lean Kernel Challenge: Trusted Type-Checking, Reflection & Proof-Term Reduction',
 'subtitle': 'Following XTX Markets’ 16 September 2026 reallocation of AI-for-math funding from AIMO to the SAIR Foundation, '
             'Mathlib, and Lean FRO: why separating untrusted tactic search from a small type-checking kernel makes proof '
             'checking tractable, and how reflection compresses unary Peano steps into logarithmic reduction.',
 'date_published': '2026-11-15',
 'date_redated': '2026-11-15',
 'current_edition': 'REV 1.0',
 'status_badge': 'SAIR LEAN KERNEL · VOL. VII',
 'primary_kernel': 'skills/math/m13/verify_m13_lean_kernel_reduction.py',
 'governing_law': 'Γ ⊢ t : T (de Bruijn kernel isolation) · Binary fast-doubling F_1024 mod (10⁹ + 7) = 754,854,590 in 33 modular muls vs. 1,024 unary steps',
 'colophon': {
     'identifier': 'M.13 · SAIR Lean Kernel Challenge & Reflection Reduction (competition.sair.foundation)',
     'kernels': 'Dependently typed CIC kernel checking · Proof by reflection (Boutin 1997; Grégoire–Leroy 2002) · Fast binary doubling vs. unary Peano reduction',
     'benchmarks': 'F_1024 mod 1,000,000,007 = 754,854,590 · recursion depth 12 · 33 modular multiplications vs. 1,024 unary steps (31.03x step ratio)',
     'bridge': 'Extends M.01/M.12 · Tiny airport passport checker (kernel) vs. sprawling logistics network (elaborator)',
 },
 'sliders': [
     {'label': 'Fibonacci Reduction Index (n)', 'min': 64, 'max': 2048, 'step': 64, 'value': 1024, 'unit': 'n = '},
     {'label': 'Binary Doubling Call Depth (d_rec)', 'min': 7, 'max': 12, 'step': 1, 'value': 11, 'unit': 'd_rec = '},
 ],
 'steps': [
     'Stage 1 (de Bruijn Criterion & Kernel Isolation): A proof assistant separates tactic heuristics and neural search in '
     'the elaborator from a compact, independent type-checker—the Lean 4 kernel (de Moura & Ullrich 2021, DOI '
     '10.1007/978-3-030-79876-5_37)—so a bug in search cannot sneak an unsound theorem past Γ ⊢ t : T.',
     'Stage 2 (The Definitional Reduction Bottleneck): Inside a formal kernel, evaluating arithmetic or algebraic normal '
     'forms step-by-step on unary Peano natural numbers forces O(n) or O(n²) term traversals, choking the type-checker '
     'even when the underlying mathematical argument is sound.',
     'Stage 3 (Proof by Reflection & Compiled Reduction): Proof by reflection (Boutin 1997, DOI 10.1007/bfb0014565) and '
     'compiled strong reduction (Grégoire & Leroy 2002, DOI 10.1145/581478.581501) replace long proof terms with a '
     'decision algorithm plus one soundness lemma; binary fast doubling reduces F_1024 mod (10⁹ + 7) = 754,854,590 in 33 '
     'multiplications instead of 1,024 sequential steps.',
     'Stage 4 (The SAIR Lean Kernel Challenge Landscape): On 16 September 2026, XTX Markets concluded the AIMO Prize and '
     'directed philanthropy toward Lean FRO ($10M to 2030), the Mathlib Initiative ($10M to 2030), and SAIR competitions '
     'including the Lean Kernel Challenge (https://competition.sair.foundation/), targeting high-throughput checking of '
     'complex proof terms.',
 ],
 'readouts': [
     {'label': 'Binary Reflection Output (F_1024 mod 1e9+7)', 'value': '754,854,590 (matches linear DP)'},
     {'label': 'Binary Doubling Work vs. Unary Steps', 'value': '33 modular muls vs. 1,024 steps (31.03x)'},
     {'label': 'Fast-Doubling Recursion Tree Depth', 'value': '12 frames (n = 1,024)'},
     {'label': 'Trusted Boundary', 'value': 'Kernel checks Γ ⊢ t : T independent of search'},
 ],
 'spec_plate': {
     'division': 'FORMAL TYPE THEORY / DEPENDENT KERNELS / ALGORITHMIC REDUCTION',
     'title': 'Lean 4 Kernel Architecture (de Moura & Ullrich 2021), Reflection & SAIR Research Track',
     'body': 'Contrasts O(n) unary term expansion inside a Calculus of Inductive Constructions kernel against O(log n) '
             'binary reflection (Boutin 1997; Grégoire & Leroy 2002), grounded in the SAIR Lean Kernel Challenge following '
             'XTX Markets’ 2026-09-16 announcement.',
     'meta': 'Verifier skills/math/m13/verify_m13_lean_kernel_reduction.py computes F_1024 mod 10^9+7 offline and rejects '
             'sign-corrupted doubling recurrences under --planted-defect.',
 },
 'sidenote_1': {
     'kicker': 'SIDENOTE M.13-A · THE DE BRUIJN CRITERION',
     'body': 'Named after Automath pioneer N. G. de Bruijn, the criterion states that trust rests exclusively in a small, '
             'independently re-implementable kernel that checks explicit proof objects Γ ⊢ t : T, regardless of how complex '
             'or opaque the tactics or AI models generating t may be.',
 },
 'sidenote_2': {
     'kicker': 'SIDENOTE M.13-B · XTX REALLOCATION (2026-09-16)',
     'body': 'XTX Markets’ 16 September 2026 philanthropy update ended the AIMO Prize (~$1.62M awarded across AIMO 1–3 and '
             'the Proof Pilot) and shifted resources to Lean FRO ($10M to 2030), Mathlib ($10M to 2030), and SAIR research '
             'challenges (competition.sair.foundation).',
 },
 'skill': {
     'filename': 'sair-lean-kernel-reduction-SKILL.md',
     'name': 'sair-lean-kernel-reduction',
     'description': 'AI-agnostic formal type-checking and kernel reduction skill for Folio M.13: de Bruijn isolation between '
                    'elaborator search and kernel Γ ⊢ t : T checking, proof by reflection (Boutin 1997; Grégoire–Leroy 2002), '
                    'and the binary fast-doubling verifier skills/math/m13/verify_m13_lean_kernel_reduction.py.',
     'rules': [
         'Keep search heuristics, LLM tactic synthesis, and elaborator macros outside the trusted computing base; trust only '
         'what passes an explicit, minimal Γ ⊢ t : T kernel checker.',
         'Avoid unary Peano O(n) reduction inside kernel conversion checks; replace linear step-by-step witness chains with '
         'binary reflection identities F_{2k} = F_k (2 F_{k+1} - F_k) and explicit soundness lemmas.',
         'Validate the binary vs. linear equivalence deterministically via python -X utf8 '
         'skills/math/m13/verify_m13_lean_kernel_reduction.py and test failure detection with --planted-defect.',
     ],
 },
 'revisions': [{
     'edition': 'REV 1.0',
     'date': '2026-11-15',
     'summary': 'REV 1.0 (Published 2026-11-15): Initial Volume VII SAIR Research Folio pairing the SAIR Lean Kernel '
                'Challenge (XTX 2026-09-16 shift) with de Moura & Ullrich (2021), Grégoire & Leroy (2002), Boutin (1997), '
                'and deterministic verifier verify_m13_lean_kernel_reduction.py.',
     'opus': 'All primary DOIs checked via Crossref and Scite (Moura 2021: 685 citing publications, 0 retractions); '
             'binary vs. linear Fibonacci reduction computed offline across 1,024 steps.',
 }],
 'volume': 7,
 'volume_code': 'VOL. 07',
 'reading_time': '20 MIN READ',
 'word_count': '4,550 WORDS',
 'scite': {
     'doi': '10.1007/978-3-030-79876-5_37',
     'fetched_on': '2026-11-15',
     'citing_publications': 685,
     'supporting': 0,
     'mentioning': 370,
     'contrasting': 0,
     'retracted': False,
     'summary': 'Scite Smart Citation Index (fetched 2026-11-15): 0 retractions; 685 citing publications '
                '(0 supporting, 370 mentioning, 0 contrasting) for de Moura & Ullrich (2021), The Lean 4 Theorem Prover '
                'and Programming Language.',
 },
}

LONGFORM_DATA = {
 'reading_time': '20 MIN READ',
 'word_count': '4,550 WORDS',
 'parent_folios': ['M.01', 'M.12'],
 'lineage_mode': 'CONTINUATION · Extends M.01 Formal Proof Checking & M.12 Lean 4 Context to the SAIR Lean Kernel Challenge',
 'scite': FOLIO['scite'],
 'act1_title': 'Act I — From Olympiad Contests to Trusted Kernel Infrastructure',
 'act1_dropcap': 'On 16 September 2026, XTX Markets announced the closure of the AI Mathematical Olympiad (AIMO) Prize '
                 'after awarding roughly $1.62 million across AIMO 1–3 and its Proof Pilot. Rather than stepping back from '
                 'automated mathematics, the announcement reallocated funding directly into foundational infrastructure: '
                 '$10 million toward the Lean Focused Research Organization through 2030, $10 million toward the Mathlib '
                 'Initiative through 2030, and targeted open research competitions through the Scientific AI Research '
                 '(SAIR) Foundation—starting with a challenge devoted directly to the Lean Kernel itself.',
 'act1_plain_bridge': 'Think of the difference between drafting an architectural skyscraper on napkins and checking its '
                      'structural steel tolerances at the city permit office. A proof assistant like Lean 4 has two completely '
                      'different jobs. The front end—tactics, autocomplete, neural proof search, and human hints—acts like a '
                      'creative studio sketching thousands of candidate ideas. The back end, called the kernel, is an austere, '
                      'tiny referee that sits behind locked doors and checks every single logical brick against the core rules '
                      'of type theory. You do not have to trust the creative studio, and you do not have to trust the AI that '
                      'wrote a proof draft, because nothing becomes a theorem until the kernel checks the final proof term '
                      'from first principles. The catch is speed: if the studio asks the kernel to unfold a slow step-by-step '
                      'calculation across thousands of tiny increments, the referee stalls even when the math is valid.',
 'act1_body': 'Modern dependent type theory gives mathematicians an unusually clean division of labor known as the de '
              'Bruijn criterion. In Lean 4 (de Moura & Ullrich, 2021, DOI 10.1007/978-3-030-79876-5_37), elaboration, '
              'metaprogramming, type-class resolution, and external tactic automation compile mathematical scripts down into '
              'explicit terms in the Calculus of Inductive Constructions. Those terms are then handed to a compact, C++-based '
              'type-checking kernel that validates typing judgments Γ ⊢ t : T and universe constraints without trusting any '
              'part of the frontend elaborator. Because every definition, lemma, and automation script in mathlib '
              '(DOI 10.1145/3372885.3373824) funnels through this narrow choke point, kernel performance and kernel auditability '
              'quietly govern the pace of large-scale formalization across the entire ecosystem.\n\n'
              'Whenever human or AI provers scale up to heavy algebraic, combinatorial, or number-theoretic arguments, '
              'definitional equality testing inside the kernel becomes a central bottleneck. Naive unary Peano arithmetic '
              'represents an integer n as n nested successor constructors S(S(...S(0)...)), so testing two intermediate '
              'values or unfolding recursive equations directly inside the kernel forces linear or quadratic term reductions. '
              'Work by Samuel Boutin (1997, DOI 10.1007/bfb0014565) on proof by reflection and by Benjamin Grégoire and '
              'Xavier Leroy (2002, DOI 10.1145/581478.581501) on compiled strong reduction demonstrated how type-checking '
              'kernels can evaluate computational subgoals orders of magnitude faster without sacrificing foundational '
              'soundness. The SAIR Lean Kernel Challenge (competition.sair.foundation) brings renewed focus to this exact '
              'interface between kernel simplicity, fast normalization, and adversarial proof-term resilience.',
 'act1_stakes': 'Why does kernel design matter well beyond academic proof assistants? Any organization that hopes to check '
                'machine-generated proofs—whether for cryptographic protocols, theorem libraries, or algebraic identities—faces '
                'an acute asymmetry: generating candidate proofs by search or neural sampling is messy and fallible, whereas '
                'checking a finished proof object should be fast, deterministic, and independent of the generator. If a proof '
                'kernel grows bloated with unverified shortcuts, a single reduction bug compromises every theorem checked by it. '
                'Conversely, if the kernel stays strictly minimal yet takes seconds or minutes to reduce computational subterms, '
                'automated proof synthesis hits a throughput wall. Balancing a minimal trusted computing base against logarithmic '
                'algorithmic reduction is one of the defining engineering challenges of formal mathematics in 2026.',
 'pullquote': '"A tiny type-checking kernel refuses to trust how smart your search was; it asks only whether every '
              'step in the finished term satisfies Γ ⊢ t : T."',
 'chronology': [
     ('1997', 'Samuel Boutin formalizes proof by reflection in Coq, replacing large symbolic proof trees with small '
              'verified decision procedures plus soundness lemmas (DOI 10.1007/bfb0014565).'),
     ('2002', 'Benjamin Grégoire and Xavier Leroy introduce compiled strong reduction in ICFP, bridging bytecode VM speed '
              'with dependent type-checker conversion rules (DOI 10.1145/581478.581501).'),
     ('2020–2021', 'The mathlib Community (DOI 10.1145/3372885.3373824) and Leonardo de Moura & Sebastian Ullrich (DOI '
                   '10.1007/978-3-030-79876-5_37) establish Lean 4’s extensible elaborator beside a compact kernel.'),
     ('2026-09-16', 'XTX Markets ends AIMO and commits $10M each to Lean FRO and Mathlib plus SAIR competitions including '
                    'the Lean Kernel Challenge (https://competition.sair.foundation/).'),
 ],
 'act2_title': 'Act II — Intuition & Governing Trade-Off: Trusted Surface vs. Reduction Throughput',
 'act2_intuition': 'Consider reducing a large arithmetic or recurrence identity inside Γ ⊢ t : T. If an automated tactic emits '
                   'an explicit unary trace over n = 1,024 successor steps, the kernel must inspect and reduce at least 1,024 '
                   'sequential transitions. By structuring the computation around binary reflection—the fast-doubling identity '
                   'F_{2k} = F_k (2 F_{k+1} − F_k) and F_{2k+1} = F_{k+1}² + F_k²—our offline verifier reaches F_1024 mod '
                   '(10⁹ + 7) = 754,854,590 across recursion depth 12 using just 33 modular multiplications, matching the '
                   '1,024-step linear reference exactly.',
 'act2_deepening': 'Crucially, logarithmic reduction only preserves trustworthiness if every algebraic rewrite used by the '
                   'reflected evaluator is backed by an equivalence check against the reference specification. In our deterministic '
                   'benchmark script (skills/math/m13/verify_m13_lean_kernel_reduction.py), flipping even a single sign inside the '
                   'fast-doubling recurrence—computing F_k (2 F_{k+1} + F_k) instead of F_k (2 F_{k+1} − F_k)—silently passes '
                   'recursion-depth and multiplication-budget checks while producing a wrong modular residue. Comparing both paths '
                   'catches the planted defect immediately. Notice the methodological parallel to type theory: fast evaluators are '
                   'only safe when tied cleanly to the kernel’s conversion relation.',
 'act2_analogy': 'Imagine verifying that a 1,024-step spiral staircase reaches floor 754 without counting every single tread '
                 'by hand. If an architect hands you a repeating geometric doubling rule plus a check on the base landing, '
                 'you can inspect 11 folded blueprints in moments—provided you check that the folding rule itself matches '
                 'ordinary step-by-step climbing at every seam.',
 'act2_plain_primer': 'The first slider sets the problem size n from 64 up to 2,048 steps, comparing how unary step-by-step '
                      'checking scales linearly against logarithmic binary doubling. The second slider sets the binary '
                      'recursion depth limit d_rec: if the kernel caps stack depth below the required bit-length plus one, '
                      'deep reflected terms stall before completing reduction.',
 'distill_diagram': {
     'analogy_title': 'Passport Referee vs. Doubling Blueprint',
     'analogy_sub': 'Tiny Γ ⊢ t : T checker stays small while reflected terms fold n steps into log2(n)',
     'force_a_title': 'Unary Reduction Cost O(n)',
     'force_a_sub': '1,024 sequential successor unfolds stress kernel time & memory',
     'force_b_title': 'Binary Reflection Speedup O(log n)',
     'force_b_sub': '33 modular multiplications across depth 12 preserve exact value match',
     'threshold_title': 'Equivalence Check (Γ ⊢ fast_fib(n) ≡ linear_fib(n))',
     'threshold_pass': 'Value 754,854,590 matches linear reference within 33 muls',
     'threshold_fail': 'Planted sign defect in doubling recurrence diverges from reference',
 },
 'walkthrough': [
     'Experiment 1 (Reduction Index n): Sweep n from 64 to 2,048 and compare O(n) unary step counts against 3 * ceil(log2(n)) '
     'binary fast-doubling multiplications.',
     'Experiment 2 (Recursion Depth Budget d_rec): Compare required tree depth 12 at n = 1,024 against constrained stack frames.',
     'Experiment 3 (Counterfactual ⚡): Run python -X utf8 skills/math/m13/verify_m13_lean_kernel_reduction.py --planted-defect '
     'to observe the corrupted doubling recurrence diverge immediately from the linear reference.',
 ],
 'act4_title': 'Act IV — Clean Interfaces for Machine-Assisted Proof Engineering',
 'act4_human_ai': 'Separating search from verification is what lets humans and AI systems collaborate safely on formal '
                  'mathematics. Under XTX Markets’ 2026 funding transition toward Lean FRO, Mathlib, and the SAIR competitions, '
                  'progress no longer depends on treating neural models as authorities: AI search proposes tactics or proof '
                  'scripts, while small kernels and reflection architectures act as incorruptible judges of valid derivation.',
 'act4_deepening': 'Improving a proof-checking kernel requires equal attention to correctness and performance: simplifying '
                   'definitional equality caches, sharpening compiled evaluation paths, and stress-testing pathological proof '
                   'terms generated by automated search. Each improvement lowers the barrier for checking massive collaborative '
                   'libraries cleanly and reproducibly.',
 'cf_bridge': 'Mathematics Pillar Monograph M.13 (VOL. 07): Formal verification kernels and reflection reduction principles '
              'applicable wherever trustworthy automated deduction meets computational scale.',
 'sources': [
     'de Moura, L., & Ullrich, S. (2021). The Lean 4 theorem prover and programming language. Automated Deduction – '
     'CADE 28, Lecture Notes in Computer Science, 12699, 625–635. DOI 10.1007/978-3-030-79876-5_37.',
     'Grégoire, B., & Leroy, X. (2002). A compiled implementation of strong reduction. Proceedings of the Seventh ACM '
     'SIGPLAN International Conference on Functional Programming (ICFP 2002), 235–246. DOI 10.1145/581478.581501.',
     'Boutin, S. (1997). Reflection-based decision procedures in Coq (Theoretical Aspects of Computer Software, TACS 1997). '
     'Lecture Notes in Computer Science, 1281, 515–529. DOI 10.1007/bfb0014565.',
     'The mathlib Community (2020). The Lean mathematical library. CPP 2020, 367–381. DOI 10.1145/3372885.3373824.',
     'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and classifies '
     'their intent using deep learning. Quantitative Science Studies, 2(3), 882–898. DOI 10.1162/qss_a_00146.',
     'XTX Markets (2026-09-16). Update on XTX Markets’ AI for Maths Philanthropy. '
     'https://aimoprize.com/updates/2026-09-16-update-on-xtx-markets-ai-philanthropy ; SAIR Foundation Competitions: '
     'https://competition.sair.foundation/.',
 ],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Lean 4 Untrusted Elaborator vs Trusted de Bruijn Kernel & Reflection Speedup">\n'
        '            <line x1="35" y1="188" x2="645" y2="188" stroke="currentColor" stroke-opacity="0.3"/>\n'
        '            <text x="42" y="24" font-size="10.5" font-weight="600" fill="currentColor">de Bruijn Isolation: Elaborator Search → Tiny Kernel (Γ ⊢ t : T)</text>\n'
        '            <rect x="44" y="44" width="124" height="58" rx="6" fill="var(--tp-minium)" fill-opacity="0.14" stroke="var(--tp-minium)" stroke-width="1.8"/>\n'
        '            <text x="106" y="69" font-size="9.5" text-anchor="middle" font-weight="600" fill="var(--tp-minium)">Elaborator &amp; Tactics</text>\n'
        '            <text x="106" y="86" font-size="8.5" text-anchor="middle" fill="currentColor">Untrusted Search</text>\n'
        '            <line x1="168" y1="73" x2="210" y2="73" stroke="var(--tp-prussian)" stroke-width="2.2"/>\n'
        '            <rect x="210" y="40" width="112" height="66" rx="6" fill="var(--tp-prussian)" fill-opacity="0.16" stroke="var(--tp-prussian)" stroke-width="2.2"/>\n'
        '            <text x="266" y="68" font-size="10" text-anchor="middle" font-weight="700" fill="var(--tp-prussian)">Lean 4 Kernel</text>\n'
        '            <text x="266" y="86" font-size="8.5" text-anchor="middle" fill="currentColor">Checks Γ ⊢ t : T</text>\n'
        '            <line x1="348" y1="22" x2="348" y2="192" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="368" y="24" font-size="10.5" font-weight="600" fill="currentColor">Unary O(n) vs. Binary Reflection O(log n)</text>\n'
        '            <path d="M 374 166 L 626 42" fill="none" stroke="var(--tp-minium)" stroke-width="2.2" stroke-dasharray="5,3"/>\n'
        '            <path d="M 374 166 Q 460 152 626 144" fill="none" stroke="var(--tp-verdigris)" stroke-width="3.2"/>\n'
        '            <circle cx="545" cy="147" r="5" fill="var(--tp-verdigris)"/>\n'
        '            <text x="378" y="56" font-size="9" fill="var(--tp-minium)">Unary Peano: 1,024 steps</text>\n'
        '            <text x="378" y="136" font-size="9.5" fill="var(--tp-verdigris)">Binary Doubling: 33 muls (depth 12)</text>\n'
        '            <text x="44" y="168" font-size="9.5" fill="var(--tp-prussian)">F_1024 mod 10^9+7 = 754,854,590</text>\n'
        '            <text x="44" y="206" font-size="9.5" fill="var(--tp-verdigris)">Deterministic check: skills/math/m13/verify_m13_lean_kernel_reduction.py</text>\n'
        '          </svg>',
}

PLATE_CAPTION = {
 'alt': 'Conceptual visualization imagining an austere sapphire-and-vellum keystone observatory filtering dense threads of '
        'computational search into three crisp parallel beams (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate M.13-V (Imagining What It Would Look Like) · Artistic visualization contrasting sprawling '
            'proof-search threads with the compact de Bruijn Lean 4 type-checking kernel and reflected logarithmic beams.',
}

DISPATCH = {
 'kicker': 'SAIR FOUNDATION RESEARCH TRACK · FOLIO M.13 · XTX PHILANTHROPY SHIFT (2026-09-16)',
 'headline': 'XTX Reallocates AIMO Funding Toward Lean FRO, Mathlib & SAIR Lean Kernel Challenge',
 'body': 'Following XTX Markets’ 16 September 2026 update ending the AIMO Prize, open infrastructure grants prioritize Lean '
         'FRO, Mathlib, and SAIR’s Lean Kernel Challenge (https://competition.sair.foundation/), built atop de Moura & '
         'Ullrich (2021, DOI 10.1007/978-3-030-79876-5_37).',
}

META_3D = (
 'Lean 4 Kernel Isolation & Binary Reflection Reduction Surface',
 'X: Problem Scale n · Z: Binary Call Depth d_rec · Y: Reduction Step Cost Ratio',
)

ES_TRANSLATION = {
 'title_es': 'El Reto del Kernel de Lean de SAIR: Verificación Confiable, Reflexión y Reducción de Términos',
 'subtitle_es': 'Tras el anuncio de XTX Markets del 16 de septiembre de 2026 que cerró el premio AIMO y reorientó fondos '
                'hacia SAIR Foundation, Mathlib y Lean FRO: por qué separar la búsqueda no confiable de un núcleo mínimo de '
                'tipos acelera y protege la matemática formal.',
 'why_es': 'Separar un taller creativo de búsqueda (tácticas e IA) de un núcleo árbitro diminuto (Γ ⊢ t : T) permite '
           'comprobar pruebas complejas sin confiar en quien las generó, siempre que el núcleo reduzca cálculos en O(log n) '
           'y no en pasos unarios lentos.',
 'plain_es': 'Imagina la diferencia entre dibujar un rascacielos en servilletas y revisar sus tolerancias de acero en la '
             'oficina de permisos. Un asistente de pruebas como Lean 4 tiene dos piezas distintas: un entorno flexible que '
             'prueba tácticas y sugiere pasos, y un kernel mínimo y austero que solo comprueba la validez de la prueba '
             'terminada bajo las reglas de tipos. No hace falta confiar en la heurística que encontró el argumento, porque '
             'el kernel revisa cada ladrillo desde cero. El desafío está en el rendimiento: cuando una fórmula expande '
             'números en notación unaria paso a paso, el kernel se vuelve lento, mientras que la reflexión binaria comprime '
             '1,024 pasos en apenas 33 multiplicaciones modulares.',
 'deep_es': 'Basado en el diseño del kernel de Lean 4 (de Moura y Ullrich, 2021, DOI 10.1007/978-3-030-79876-5_37), la prueba '
            'por reflexión (Boutin, 1997, DOI 10.1007/bfb0014565) y la reducción fuerte compilada (Grégoire y Leroy, 2002, '
            'DOI 10.1145/581478.581501). El script determinista skills/math/m13/verify_m13_lean_kernel_reduction.py calcula '
            'F_1024 mod (10^9 + 7) = 754,854,590 con profundidad 12 y 33 multiplicaciones, y falla al activar '
            '--planted-defect cambiando el signo de la recurrencia.',
 'bridge_es': 'Folio M.13 del Pilar de Matemáticas (VOL. 07): conecta la transición filantrópica de XTX Markets hacia Lean '
              'FRO, Mathlib y SAIR con el núcleo de tipos de Lean 4 y la reducción reflejada.',
}
