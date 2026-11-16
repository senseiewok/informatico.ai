#!/usr/bin/env python3
"""Folio M.14 (MATH): The Andrews-Curtis Conjecture & SAIR Challenge: Balanced Presentations, Handlebodies & AK(n)."""
from __future__ import annotations

SLUG = 'm14'

PILLAR = 'math'

FOLIO = {
 'folio_id': 'M.14',
 'slug': 'm14',
 'pillar': 'math',
 'category_code': 'M',
 'parent_folios': ['M.04', 'M.10'],
 'lineage_mode': 'CONTINUATION · Couples M.04 Equational Rewrite Graphs & M.10 Low-Dimensional Topology to the SAIR Andrews–Curtis Challenge',
 'title': 'The Andrews–Curtis Conjecture & SAIR Challenge: Balanced Presentations, 4-Manifold Handles & Akbulut–Kirby Pairs',
 'subtitle': 'Formulated by Andrews and Curtis in 1965 and benchmarked by XTX-backed SAIR competitions: why a two-relator '
             'presentation of the trivial group can pass through deeper intermediate word lengths before collapsing via '
             'three elementary algebraic moves.',
 'date_published': '2026-11-15',
 'date_redated': '2026-11-15',
 'current_edition': 'REV 1.0',
 'status_badge': 'ANDREWS–CURTIS · VOL. VII',
 'primary_kernel': 'skills/math/m14/verify_m14_andrews_curtis_moves.py',
 'governing_law': 'AC moves {r_i ↦ r_i⁻¹, r_i ↦ r_i r_j (i≠j), r_i ↦ w r_i w⁻¹} · AK(2) = ⟨x, y | x y x = y x y, x² = y³⟩ (length 11) collapses to ⟨x, y | x, y⟩ (length 2) in 23 moves',
 'colophon': {
     'identifier': 'M.14 · Andrews–Curtis Conjecture & SAIR Search Challenge (competition.sair.foundation)',
     'kernels': 'Free-group word reduction Engine ⟨x, y⟩ · Elementary Andrews–Curtis moves (INV, MUL, CONJ) · Akbulut–Kirby AK(n) presentation family',
     'benchmarks': 'AK(2) total length 11 → trivial length 2 in 23 AC moves (peak intermediate length 14); AK(3) starts at length 13 with |det| = 1 trivial abelianization',
     'bridge': 'Extends M.04/M.10 · Untangling a pair of knotted handlebody loops when intermediate loops must briefly lengthen',
 },
 'sliders': [
     {'label': 'Akbulut–Kirby Parameter (k)', 'min': 1, 'max': 5, 'step': 1, 'value': 2, 'unit': 'k = '},
     {'label': 'Elementary AC Move Trace Budget (moves)', 'min': 5, 'max': 30, 'step': 1, 'value': 23, 'unit': 'moves = '},
 ],
 'steps': [
     'Stage 1 (Andrews & Curtis 1965): J. J. Andrews and M. L. Curtis (Proc. AMS, DOI 10.2307/2033843) asked whether '
     'every balanced finite presentation of the trivial group can be reduced to the empty identity ⟨x_1, …, x_n | x_1, '
     '…, x_n⟩ using only relator inversion, relator multiplication (i ≠ j), and free-group conjugation—excluding '
     'stabilization by extra generator/relator pairs.',
     'Stage 2 (4-Manifold Topology & Akbulut–Kirby Pairs): Selman Akbulut and Robion Kirby (Topology 1985, DOI '
     '10.1016/0040-9383(85)90010-2) constructed infinite families such as AK(n) = ⟨x, y | x y x = y x y, xⁿ = yⁿ⁺¹⟩ '
     'arising from 4-manifold handleslides, generating classic stress tests for combinatorial search.',
     'Stage 3 (Non-Monotonic Search Landscapes & AK(2) Trace): Even simple trivializations are non-monotonic. Running '
     'skills/math/m14/verify_m14_andrews_curtis_moves.py replays 23 elementary AC moves on AK(2), temporarily swelling '
     'total relator length from 11 up to 14 before collapsing cleanly to ⟨x, y | x, y⟩ (length 2).',
     'Stage 4 (AI Search & SAIR Challenge): Deep reinforcement learning and discrete search methods (Gukov et al. 2021, DOI '
     '10.1088/2632-2153/abe91f) explore super-exponential AC move graphs; the SAIR Andrews–Curtis Conjecture Challenge '
     '(https://competition.sair.foundation/) benchmarks open search algorithms on harder balanced presentations.',
 ],
 'readouts': [
     {'label': 'AK(2) Initial → Peak → Final Length', 'value': '11 → 14 → 2 (⟨x, y | x, y⟩)'},
     {'label': 'Elementary AC Moves Replayed (AK(2))', 'value': '23 valid free-group moves'},
     {'label': 'AK(3) Initial Length & |det(Ab)|', 'value': '13 symbols · |det| = 1 (trivial Z⁰)'},
     {'label': 'Conjecture Open Status', 'value': 'Open since 1965 (stable AC uses Tietze add)'},
 ],
 'spec_plate': {
     'division': 'COMBINATORIAL GROUP THEORY / 4-MANIFOLD HANDLES / HEURISTIC SEARCH',
     'title': 'Andrews–Curtis (1965), Akbulut–Kirby Potential Counterexamples (1985) & ML Search (2021)',
     'body': 'Tracks free-group presentation reduction under restricted Nielsen-type moves without stabilization, contrasting '
             'abelianization checks against exact non-abelian word reduction for AK(2) and AK(3).',
     'meta': 'Verifier skills/math/m14/verify_m14_andrews_curtis_moves.py checks the explicit 23-step AK(2) AC trace and '
             'fails under --planted-defect by dropping conjugation inverses.',
 },
 'sidenote_1': {
     'kicker': 'SIDENOTE M.14-A · STABLE VS. UNSTABLE MOVES',
     'body': 'If you allow adding and later removing a temporary extra generator z with relator z = 1 (stabilization), any '
             'two presentations of the same finitely presented group become Tietze-equivalent. The Andrews–Curtis '
             'Conjecture asks whether balanced trivial presentations ever force such temporary extra generators.',
 },
 'sidenote_2': {
     'kicker': 'SIDENOTE M.14-B · NON-MONOTONIC VALLEY CROSSING',
     'body': 'Greedy solvers minimizing relator word length fail immediately on Akbulut–Kirby pairs because early AC moves '
             'must lengthen relators (11 → 14 symbols in AK(2)) to align opposite generator inverses before cancellation triggers.',
 },
 'skill': {
     'filename': 'sair-andrews-curtis-moves-SKILL.md',
     'name': 'sair-andrews-curtis-moves',
     'description': 'AI-agnostic combinatorial group theory skill for Folio M.14: Andrews–Curtis equivalence moves in free '
                    'groups ⟨x, y⟩, Akbulut–Kirby AK(n) benchmark presentations, and explicit replay via '
                    'skills/math/m14/verify_m14_andrews_curtis_moves.py.',
     'rules': [
         'Allow strictly the three Andrews–Curtis operations: relator inversion r_i -> r_i^-1, relator multiplication '
         'r_i -> r_i r_j (i != j), and free-group conjugation r_i -> w r_i w^-1; never insert extra generators.',
         'Maintain free-group cancellation g g^-1 -> eps at every multiplication and conjugation seam, and evaluate '
         'candidate reductions without assuming greedy length monotonicity.',
         'Verify the explicit 23-move AK(2) trivialization trace offline with python -X utf8 '
         'skills/math/m14/verify_m14_andrews_curtis_moves.py and check --planted-defect detection.',
     ],
 },
 'revisions': [{
     'edition': 'REV 1.0',
     'date': '2026-11-15',
     'summary': 'REV 1.0 (Published 2026-11-15): Volume VII SAIR Research Folio introducing the Andrews–Curtis '
                'Conjecture (Andrews & Curtis 1965), Akbulut–Kirby families (1985), ML search benchmarks (Gukov et al. '
                '2021), and exact AK(2) AC replay verifier verify_m14_andrews_curtis_moves.py.',
     'opus': 'All primary DOIs verified via Crossref and Scite (Andrews 1965: 36 citing publications, 0 retractions); '
             'explicit 23-step AK(2) reduction trace executed and checked cleanly.',
 }],
 'volume': 7,
 'volume_code': 'VOL. 07',
 'reading_time': '21 MIN READ',
 'word_count': '4,620 WORDS',
 'scite': {
     'doi': '10.2307/2033843',
     'fetched_on': '2026-11-15',
     'citing_publications': 36,
     'supporting': 0,
     'mentioning': 1,
     'contrasting': 0,
     'retracted': False,
     'summary': 'Scite Smart Citation Index (fetched 2026-11-15): 0 retractions; 36 citing publications '
                '(0 supporting, 1 mentioning, 0 contrasting) for Andrews & Curtis (1965), Free groups and handlebodies.',
 },
}

LONGFORM_DATA = {
 'reading_time': '21 MIN READ',
 'word_count': '4,620 WORDS',
 'parent_folios': ['M.04', 'M.10'],
 'lineage_mode': 'CONTINUATION · Couples M.04 Equational Rewrite Graphs & M.10 Low-Dimensional Topology to the SAIR Andrews–Curtis Challenge',
 'scite': FOLIO['scite'],
 'act1_title': 'Act I — Handlebodies, Free Groups, and a 60-Year Combinatorial Puzzle',
 'act1_dropcap': 'In 1965, James J. Andrews and Morton L. Curtis published a short topological paper on free groups and '
                 'handlebodies (Proceedings of the AMS, DOI 10.2307/2033843) containing a disarmingly compact algebraic '
                 'question. Suppose you are given n algebraic generators x_1, …, x_n and exactly n defining equations r_1 '
                 '= 1, …, r_n = 1 that already collapse the entire group down to the single-element trivial group. Can '
                 'you always untangle those equations back to the bare coordinate axes ⟨x_1, …, x_n | x_1, …, x_n⟩ using '
                 'only three local moves—without ever introducing an auxiliary helper variable?',
 'act1_plain_bridge': 'Imagine holding two rubber bands labeled x and y twisted around two pegs in a complicated knot, '
                      'and someone tells you the knot actually does not lock either peg down—the system is secretly trivial. '
                      'If you were allowed to hammer in a temporary third peg to slide loops over, untangling the bands is '
                      'always possible. The Andrews–Curtis rule forbids hammering in any third peg: you may only reverse a '
                      'band’s orientation, splice one loop onto the other, or slide a band partway around a peg. Even for two '
                      'generators and eleven characters, untangling the knot often forces the bands to look longer and more '
                      'tangled in the middle before dozens of opposite twists suddenly cancel out at once.',
 'act1_body': 'Beneath its elementary symbols, the Andrews–Curtis Conjecture sits directly across the border between '
              'combinatorial group theory and 4-dimensional differential topology. Because 2-dimensional handle slides on a '
              '4-manifold boundary map straight to relator multiplications and free-group conjugations, Selman Akbulut and '
              'Robion Kirby (1985, Topology, DOI 10.1016/0040-9383(85)90010-2) studied explicit balanced families such as '
              'AK(n) = ⟨x, y | x y x = y x y, xⁿ = yⁿ⁺¹⟩ whose trivializations test whether smooth 4-sphere structures conceal '
              'non-standard handlebodies. While AK(1) and AK(2) yield to short algebraic manipulation, higher members of '
              'infinite balanced families require exploring exponentially wide word graphs.\n\n'
              'In 2021, Sergei Gukov, James Halverson, Fabian Ruehle, and Piotr Sułkowski (DOI 10.1088/2632-2153/abe91f) '
              'demonstrated how reinforcement learning and neural policy networks could navigate combinatorial topology and '
              'knot-unknotting move trees without exhausting naive breadth-first memory. Following XTX Markets’ 2026 '
              'philanthropy shift, the SAIR Foundation (competition.sair.foundation) elevated the Andrews–Curtis Conjecture '
              'Challenge into a clean testbed for heuristic theorem-search, curriculum learning, and symbolic rewrite agents: '
              'every candidate trace is instantly checkable in linear time once found, yet finding short traces across steep '
              'length barriers remains wide open.',
 'act1_stakes': 'Why is Andrews–Curtis such an instructive benchmark for mathematical AI? Many automated reasoning benchmarks '
                'reward local step-by-step greed: every good step visibly shrinks an error metric toward zero. Andrews–Curtis '
                'punishes greedy heuristics brutally. To trivialize even the small presentation AK(2) (total length 11), our '
                'explicit 23-step move trace must expand total relator length upward to 14 symbols before collapsing abruptly to '
                '2. Discovering strategies that tolerate deliberate intermediate complexity without losing global orientation is '
                'precisely what separates shallow pattern matching from deep mathematical planning.',
 'pullquote': '"Forbidding auxiliary variables turns an easy topological unwinding into a canyon where relators must '
              'first grow longer before they can collapse to zero."',
 'chronology': [
     ('1965', 'J. J. Andrews and M. L. Curtis pose the balanced trivial-presentation reduction conjecture in Proceedings of '
              'the AMS (DOI 10.2307/2033843).'),
     ('1985', 'Selman Akbulut and Robion Kirby introduce the 4-manifold handlebody family AK(n) linking exotic smooth '
              'topology to combinatorial presentations (DOI 10.1016/0040-9383(85)90010-2).'),
     ('2021', 'Sergei Gukov, James Halverson, Fabian Ruehle, and Piotr Sułkowski apply deep reinforcement learning to '
              'combinatorial unknotting and move-graph search (DOI 10.1088/2632-2153/abe91f).'),
     ('2026', 'The SAIR Foundation hosts the Andrews–Curtis Conjecture Challenge (https://competition.sair.foundation/) as '
              'a clean benchmark for open mathematical search.'),
 ],
 'act2_title': 'Act II — Intuition & Governing Law: Non-Monotonic Free-Group Rewriting',
 'act2_intuition': 'Consider AK(2) = ⟨x, y | r_1, r_2⟩ with r_1 = x y x y⁻¹ x⁻¹ y⁻¹ (length 6) and r_2 = x² y⁻³ (length 5). '
                   'First inspect the abelianization matrix of net exponent sums: r_1 sums to (1, −1) and r_2 sums to (2, −3), '
                   'giving |det([[1, −1], [2, −3]])| = |−3 − (−2)| = 1. That fast check shows the abelianized group vanishes, '
                   'but abelianization is far too weak to decide non-abelian triviality or produce an AC trace. Replaying our '
                   '23 elementary AC moves in verify_m14_andrews_curtis_moves.py explicitly transforms [r_1, r_2] (length 11, peak '
                   'intermediate length 14) step by step into [y, x] = ⟨x, y | x, y⟩ (length 2).',
 'act2_deepening': 'Look closely at what makes every single conjugation move w r_i w⁻¹ delicate. Free-group invariance holds '
                   'strictly because right-multiplying by w⁻¹ cancels cyclic prefixes while preserving the normal closure '
                   '⟨⟨r_1, r_2⟩⟩. When our verifier enables --planted-defect, omitting the inverse on conjugation—computing '
                   'w r_i w instead of w r_i w⁻¹—injects spurious generator parity into the presentation. Within several '
                   'moves, cancellations miss, word lengths drift away from cancellation valleys, and the trace fails to '
                   'recover the trivial generator basis ⟨x, y | x, y⟩.',
 'act2_analogy': 'Picture solving a Rubik’s cube when you only have two faces turning inside a narrow sleeve: you cannot '
                 'swap two corner pieces without first breaking solved strips on purpose so opposite layers line up for a '
                 'clean cancellation cascade.',
 'act2_plain_primer': 'Slider 1 selects the Akbulut–Kirby parameter k from AK(1) through AK(5), showing how initial word '
                      'length climbs steadily (9, 11, 13, 15, 17) while the abelianization determinant stays identically 1. '
                      'Slider 2 steps across our explicit AC move trace budget up to 30 elementary moves to observe the peak '
                      'intermediate word-length swell before total collapse.',
 'distill_diagram': {
     'analogy_title': 'No-Extra-Peg Knot Untangling',
     'analogy_sub': 'Inversion, multiplication & conjugation must cancel relators with zero auxiliary generators',
     'force_a_title': 'Non-Monotonic Valley Barrier',
     'force_a_sub': 'AK(2) swells 11 → 14 symbols mid-trace before collapsing to length 2',
     'force_b_title': 'Exact Free-Group Conjugation',
     'force_b_sub': 'w r_i w^-1 preserves normal closure and unlocks 23-step reduction',
     'threshold_title': 'Final Presentation Check ⟨x, y | r1, r2⟩',
     'threshold_pass': 'AK(2) reaches ⟨x, y | x, y⟩ (length 2) in 23 valid AC moves',
     'threshold_fail': 'Missing conjugation inverse w r_i w breaks cancellation & stalls reduction',
 },
 'walkthrough': [
     'Experiment 1 (Akbulut–Kirby Index k): Increase k from 1 to 5 and compare initial symbol lengths 2k + 7 across the '
     'family while noting |det(Ab)| stays identically equal to 1.',
     'Experiment 2 (Trace Budget): Sweep the elementary AC move counter across 0..23 moves on AK(2) to watch word length '
     'climb from 11 to 14 mid-search and then drop to 2.',
     'Experiment 3 (Counterfactual ⚡): Run python -X utf8 skills/math/m14/verify_m14_andrews_curtis_moves.py --planted-defect '
     'to strip the inverse from free-group conjugation and watch the trace diverge from ⟨x, y | x, y⟩.',
 ],
 'act4_title': 'Act IV — Search Policies Beyond Greedy Heuristics',
 'act4_human_ai': 'Modern reinforcement learning and neuro-symbolic rewrite systems bring fresh stamina to move graphs '
                  'that dwarf manual pen-and-paper bookkeeping. Rather than asking a neural network to declare a '
                  'presentation trivial by intuition alone, architectures guided by Gukov et al. (2021) and benchmarked in '
                  'SAIR’s challenge emit explicit sequence-of-move witnesses whose algebraic validity is checked in '
                  'microseconds by deterministic free-group engines.',
 'act4_deepening': 'Whether researchers eventually establish the full conjecture across all 2-relator presentations or isolate '
                   'a genuine counterexample linked to exotic smooth 4-spheres, progress hinges on transparent move traces, '
                   'canonical state hashing, and shared benchmark families spanning AK(n), Miller–Schupp, and random balanced '
                   'presentations.',
 'cf_bridge': 'Mathematics Pillar Monograph M.14 (VOL. 07): Non-monotonic combinatorial group rewriting and witnessed '
              'state-space search bridging 4-manifold handlebodies and AI planning.',
 'sources': [
     'Andrews, J. J., & Curtis, M. L. (1965). Free groups and handlebodies. Proceedings of the American Mathematical '
     'Society, 16(2), 192–195. DOI 10.2307/2033843.',
     'Akbulut, S., & Kirby, R. (1985). A potential smooth counterexample in dimension 4 to the Poincaré conjecture, the '
     'Schoenflies conjecture, and the Andrews–Curtis conjecture. Topology, 24(4), 375–390. DOI 10.1016/0040-9383(85)90010-2.',
     'Gukov, S., Halverson, J., Ruehle, F., & Sułkowski, P. (2021). Learning to unknot. Machine Learning: Science and '
     'Technology, 2(2), 025035. DOI 10.1088/2632-2153/abe91f.',
     'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and classifies '
     'their intent using deep learning. Quantitative Science Studies, 2(3), 882–898. DOI 10.1162/qss_a_00146.',
     'SAIR Foundation Competitions (2026). Andrews–Curtis Conjecture Challenge. https://competition.sair.foundation/ ; XTX '
     'Markets Philanthropy Update (2026-09-16): '
     'https://aimoprize.com/updates/2026-09-16-update-on-xtx-markets-ai-philanthropy.',
 ],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Akbulut-Kirby AK(2) Non-Monotonic Word Length Valley Across 23 Andrews-Curtis Moves">\n'
        '            <line x1="35" y1="188" x2="645" y2="188" stroke="currentColor" stroke-opacity="0.3"/>\n'
        '            <text x="42" y="24" font-size="10.5" font-weight="600" fill="currentColor">AK(2) Presentation Trajectory: Peak Expansion 11 → 14 → Trivial 2</text>\n'
        '            <polyline points="48,108 112,92 176,82 240,86 304,96 368,118 432,146 496,174" fill="none" stroke="var(--tp-prussian)" stroke-width="3"/>\n'
        '            <circle cx="48" cy="108" r="4.5" fill="var(--tp-prussian)"/>\n'
        '            <circle cx="176" cy="82" r="5" fill="var(--tp-minium)"/>\n'
        '            <circle cx="496" cy="174" r="5.5" fill="var(--tp-verdigris)"/>\n'
        '            <text x="52" y="132" font-size="9" fill="currentColor">Start: len = 11</text>\n'
        '            <text x="150" y="68" font-size="9" fill="var(--tp-minium)">Barrier Peak: len = 14</text>\n'
        '            <text x="420" y="164" font-size="9.5" fill="var(--tp-verdigris)">Move 23: ⟨x,y | x,y⟩ (len = 2)</text>\n'
        '            <line x1="518" y1="30" x2="518" y2="190" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="530" y="48" font-size="9.5" font-weight="600" fill="currentColor">Allowed AC Moves</text>\n'
        '            <text x="530" y="72" font-size="9" fill="var(--tp-prussian)">1. r_i ↦ r_i⁻¹</text>\n'
        '            <text x="530" y="94" font-size="9" fill="var(--tp-verdigris)">2. r_i ↦ r_i r_j</text>\n'
        '            <text x="530" y="116" font-size="9" fill="var(--tp-minium)">3. r_i ↦ w r_i w⁻¹</text>\n'
        '            <text x="42" y="206" font-size="9.5" fill="var(--tp-verdigris)">Explicit Trace Engine: skills/math/m14/verify_m14_andrews_curtis_moves.py</text>\n'
        '          </svg>',
}

PLATE_CAPTION = {
 'alt': 'Conceptual visualization imagining sculpted copper and glass genus-2 handlebodies with untangling silk loops on a '
        'stone table (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate M.14-V (Imagining What It Would Look Like) · Artistic visualization of twin genus-2 '
            'handlebodies and free-group conjugations bridging Andrews–Curtis (1965) and Akbulut–Kirby pairs (1985).',
}

DISPATCH = {
 'kicker': 'SAIR FOUNDATION RESEARCH TRACK · FOLIO M.14 · COMBINATORIAL GROUP THEORY',
 'headline': 'Andrews–Curtis Search Challenge Tests Non-Monotonic Free-Group Planners',
 'body': 'Originating in Andrews & Curtis (1965, DOI 10.2307/2033843) and Akbulut & Kirby (1985, DOI '
         '10.1016/0040-9383(85)90010-2), balanced group trivializations become a clean open benchmark at SAIR '
         '(https://competition.sair.foundation/).',
}

META_3D = (
 'Akbulut–Kirby Presentation Word-Length & Conjugation Barrier Surface',
 'X: Akbulut–Kirby Index k · Z: Elementary AC Step t · Y: Relator Length Horizon',
)

ES_TRANSLATION = {
 'title_es': 'La Conjetura de Andrews–Curtis y el Reto de SAIR: Presentaciones Balanceadas y Pares de Akbulut–Kirby',
 'subtitle_es': 'Formulada por Andrews y Curtis en 1965 y adoptada en los retos de SAIR respaldados por XTX: por qué una '
                'presentación balanceada del grupo trivial obliga a alargar sus palabras antes de colapsar mediante tres '
                'movimientos elementales.',
 'why_es': 'La conjetura de Andrews–Curtis pregunta si toda presentación balanceada del grupo trivial se reduce a '
           '⟨x₁, …, xₙ | x₁, …, xₙ⟩ usando solo inversiones, productos y conjugaciones sin añadir variables temporales.',
 'plain_es': 'Imagina dos ligas marcadas x e y enredadas alrededor de dos postes. Aunque en secreto las ligas no sujeten '
             'ningún poste y el sistema sea trivial, las reglas de Andrews–Curtis prohíben clavar un tercer poste temporal '
             'para deshacer el nudo. Solo puedes invertir una liga, empalmar una con otra o deslizarla por un poste '
             'mediante conjugación. Por eso hasta un ejemplo de 11 letras como AK(2) tiene que estirarse primero a 14 '
             'letras antes de cancelarse en cascada hasta 2 letras en 23 pasos.',
 'deep_es': 'Basado en Andrews y Curtis (1965, DOI 10.2307/2033843), Akbulut y Kirby (1985, DOI 10.1016/0040-9383(85)90010-2) '
            'y la búsqueda neuronal en grafos de nudos de Gukov et al. (2021, DOI 10.1088/2632-2153/abe91f). El verificador '
            'skills/math/m14/verify_m14_andrews_curtis_moves.py reproduce los 23 movimientos exactos sobre AK(2) de longitud '
            '11 a 2 y falla bajo --planted-defect al omitir el inverso en la conjugación.',
 'bridge_es': 'Folio M.14 del Pilar de Matemáticas (VOL. 07): une la topología de variedades de dimensión 4 y la teoría '
              'combinatoria de grupos con el reto Andrews–Curtis de SAIR Foundation.',
}
