#!/usr/bin/env python3
"""Folio M.05 (MATH): Neuro-Symbolic Deductive Search (AlphaGeometry 2): Auxiliary Constructions and Allosteric Pocket Triangulation."""
from __future__ import annotations

SLUG = 'm05'

PILLAR = 'math'

FOLIO = {'folio_id': 'M.05',
 'slug': 'm05',
 'pillar': 'math',
 'category_code': 'M',
 'title': 'Neuro-Symbolic Deductive Search (AlphaGeometry 2): Auxiliary Constructions and '
          'Allosteric Pocket Triangulation',
 'subtitle': 'How AlphaGeometry couples a symbolic Deductive Database + Algebraic Rules (DD+AR) '
             'engine with a neural model that proposes auxiliary points, as reported in Nature '
             'and in a follow-up report on AlphaGeometry2. The comparison with fixing a shape by '
             "adding a support point is this folio's own picture, and any link to protein "
             'structure is an analogy.',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.2',
 'status_badge': 'REDATED REV 1.2',
 'primary_kernel': 'tools/discovery/frontier_ai_math_catalog.py',
 'colophon': {'identifier': 'M.05 · Synthetic & Distance Geometry',
              'kernels': 'DD+AR Closure · Cayley-Menger det(B_5)=0',
              'benchmarks': 'AlphaGeometry 25 of 30 (Nature) · AlphaGeometry2 84% of IMO 2000-2024 geometry (arXiv)',
              'bridge': 'Auxiliary point ↔ added support point (analogy only)'},
 'sliders': [{'label': 'Auxiliary Construction Depth (k_aux Anchors)',
              'min': 1,
              'max': 8,
              'step': 1,
              'value': 3,
              'unit': 'k_aux = '},
             {'label': 'Constraint Graph Density (α = m / n)',
              'min': 2.5,
              'max': 6.0,
              'step': 0.02,
              'value': 4.26,
              'unit': 'α = '}],
 'steps': ['Stage 1 (Premise Graph Encoding): Translates geometric incidences (collinearity, '
           'concyclicity, distance ratios) into a symbolic hypergraph G_0.',
           'Stage 2 (Symbolic DD+AR Fixed-Point Closure): Runs deductive database rules and '
           'algebraic angle/ratio/area chasing until saturation.',
           'Stage 3 (Neural Auxiliary Construction X_aux): Proposes the missing auxiliary '
           'point/circle that bridges disconnected deductive components.',
           'Stage 4 (Cayley-Menger Check): Five points in three-dimensional space must satisfy '
           'det(B_5) = 0 for their squared distances. The page uses this only to illustrate a '
           'rigidity condition; it is not a protein calculation.'],
 'readouts': [{'label': 'Deductive Closure Gain', 'value': '14 → 47 Invariants (fixed illustrative values)'},
              {'label': 'IMO Geometry Solve Rate', 'value': '84% of IMO 2000-2024 geometry problems (AlphaGeometry2 report)'},
              {'label': 'Cayley-Menger Condition', 'value': 'det(B_5) = 0 for five points in R^3'},
              {'label': 'Symbolic Kernel Run', 'value': 'not run here (reported by the papers)'}],
 'sidenote_1': {'kicker': 'SIDENOTE M.05-A · NATURE DOI 10.1038/s41586-023-06747-5',
                'body': 'The Nature paper reports training on about 100 million synthetic '
                        'theorems and proofs, with no human demonstrations, and that '
                        'AlphaGeometry solved 25 of 30 olympiad-level test problems, against 10 '
                        'for the previous best method.'},
 'sidenote_2': {'kicker': 'SIDENOTE M.05-B · A LOOSE ANALOGY',
                'body': 'Adding one support point can fix the shape of a wobbly frame, which is '
                        'the picture behind an auxiliary construction. The folio draws this '
                        'picture beside protein structures only as an analogy and makes no claim '
                        'about how any drug works.'},
 'skill': {'filename': 'neuro-symbolic-geometry-SKILL.md',
           'name': 'neuro-symbolic-geometry',
           'description': 'AI-agnostic skill for neuro-symbolic DD+AR deductive closure, auxiliary '
                          'construction search, and Cayley-Menger 3D distance geometry.',
           'rules': ['Saturate forward symbolic deduction (DD) and linear algebraic ratio/angle '
                     'chasing (AR) before invoking neural auxiliary proposals.',
                     'Verify 3D Euclidean distance matrices via the Cayley-Menger determinant '
                     'det(B_{n+1}) = 0 and alternating sign minors.',
                     'Say plainly when a geometric picture is only an analogy for a biological '
                     'structure, and make no claim about how any drug works.']},
 'revisions': [{'edition': 'REV 1.2',
                'date': '2026-11-14',
                'summary': 'REV 1.2 (Redated 2026-11-14): Grounding revision. Earlier editions '
                           'said that AlphaGeometry reached IMO gold-medal level (the Nature '
                           'paper says 25 of 30 problems, approaching an average gold medallist; '
                           'the 84% figure is from the separate AlphaGeometry2 report, '
                           'arXiv:2502.03544), presented the numbers 14 to 47 and 0.42 Å as '
                           'results, and said that neuro-symbolic triangulation identifies how '
                           'elexacaftor and vanzacaftor hold the CFTR helices TM2, TM8 and TM11 '
                           'in place. None of those statements is supported by the sources; the '
                           'invented opening scene of Euclid in Alexandria, the claims about '
                           'robotic surgery and self-driving cars, and the "QED verified" labels '
                           'are removed. The numbers 14 and 47 are marked as fixed illustrative '
                           'values, the 0.42 Å figure is withdrawn, and the Cystic Fibrosis '
                           'section is shortened to a labeled analogy.',
                'opus': 'Review: DOIs checked in Crossref and the Scite index on 2026-11-14; the '
                        '25 of 30 result, the 100 million synthetic theorems and the 84% versus '
                        '54% figures were read in the Nature abstract and the arXiv abstract. '
                        'Chervonyi et al. 2025 (arXiv:2502.03544) was added to the source list.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-02',
                'summary': 'REV 1.1 (Redated 2026-11-02): AlphaGeometry 2 neuro-symbolic '
                           'DD+AR deductive closure and Cayley-Menger 3D distance geometry with '
                           '4-Seat Frontier Council review. (REV 1.2: "certified" wording '
                           'withdrawn.)',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Cayley-Menger determinant det(B_5) = 0 and auxiliary anchor triangulation '
                        'to transmembrane helices TM2-TM8-TM11. (REV 1.2: "verified" wording '
                        'withdrawn; the helix claim has no source.)'},
               {'edition': 'REV 1.0',
                'date': '2026-11-01',
                'summary': 'REV 1.0 (Published 2026-11-01): Initial 5-Act monograph on '
                           'neuro-symbolic DD+AR auxiliary construction and Cayley-Menger 3D '
                           'pocket rigidity.',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Cayley-Menger determinant rank conditions and DD+AR fixed-point '
                        'termination. (REV 1.2: "verified" wording withdrawn.)'}],
 'governing_law': 'DD+AR Closure · Cayley-Menger det(B_5) = 0',
 'governing_law_latex': r"\mathrm{DD}+\mathrm{AR}\;\text{Closure}, \\ \det(B_5) = 0 \;(\text{Cayley–Menger})",
 'volume': 3,
 'volume_code': 'VOL. 03',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1038/s41586-023-06747-5',
           'fetched_on': '2026-11-08',
           'citing_publications': 378,
           'supporting': 0,
           'mentioning': 90,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Trinh et al. 2024 (DOI 10.1038/s41586-023-06747-5), '
                      'checked 2026-11-08: 378 citing publications (0 supporting, 90 mentioning, 0 '
                      'contrasting). The entry also lists a correction notice (DOI '
                      '10.1038/s41586-024-07115-7). These counts describe that one paper, not '
                      'this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1038/s41586-023-06747-5',
           'fetched_on': '2026-11-08',
           'citing_publications': 378,
           'supporting': 0,
           'mentioning': 90,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Trinh et al. 2024 (DOI 10.1038/s41586-023-06747-5), '
                      'checked 2026-11-08: 378 citing publications (0 supporting, 90 mentioning, 0 '
                      'contrasting). The entry also lists a correction notice (DOI '
                      '10.1038/s41586-024-07115-7). These counts describe that one paper, not '
                      'this folio.'},
 'act1_title': "Act I — From Euclid's Hidden Auxiliary Lines to AlphaGeometry's Neuro-Symbolic "
               'Search',
 'act1_dropcap': "Euclid's Elements, written around 300 BCE, shows in Book I, Proposition 47 that in a right-angled triangle the square on the hypotenuse equals the sum of the squares on the other two sides. The standard proof adds auxiliary lines to the figure, joining vertices of the squares to opposite corners, which creates pairs of triangles of equal area. Knowing which extra line to draw is the creative step, and it is the step that automated geometry provers found hardest.",
 'act1_plain_bridge': 'In plain words, solving a challenging geometry problem can feel like finding your way through a dark house. You have a ring of familiar rules about angles, parallel lines and circles, but none of them seem to open the next door. Sometimes the way forward is to add a helper line or point to the drawing, after which the rules you already have apply again. A program that only applies rules to what is already drawn cannot do this. AlphaGeometry pairs such a rule-applying engine with a neural model that suggests helper points. This folio makes no claim that the method is used outside geometry problems.',
 'act1_body': "In January 2024, Trieu Trinh, Yuhuai Wu, Quoc Le, He He and Thang Luong reported AlphaGeometry in Nature (DOI 10.1038/s41586-023-06747-5). A neural language model, trained from scratch on about 100 million synthetic theorems and proofs, guides a symbolic deduction engine. The engine combines a Deductive Database with Algebraic Rules, working through the consequences of the premises; when it stalls, the neural model proposes an auxiliary construction and the engine resumes. On a test set of 30 olympiad-level problems the paper reports 25 solved, against 10 for the previous best method, which its authors describe as approaching an average International Mathematical Olympiad gold medallist. A follow-up report on AlphaGeometry2 (Chervonyi et al., arXiv:2502.03544) states that it raised the solving rate on IMO geometry problems from 2000 to 2024 from 54% to 84%.",
 'act1_stakes': 'Computer proofs in geometry have followed two main routes. Algebraic methods, such as the one developed by Wu Wen-Tsun and described in the book by Chou, Gao and Zhang (1994), translate a problem into polynomial equations. Synthetic methods apply deduction rules that resemble the steps of a human proof. AlphaGeometry combines a rule-based symbolic engine with a neural model that proposes auxiliary constructions. Because the symbolic engine carries out each deduction, a proof it outputs can be checked step by step, and the Nature paper reports that the proofs are human-readable. The folio does not claim that the method extends to other fields.',
 'pullquote': 'Symbolic deduction can only use objects that are already in the diagram; a neural '
              'model proposes an auxiliary point, and the symbolic engine then checks whether it '
              'helps.',
 'chronology': [('300 BCE',
                 "Euclid's Elements uses auxiliary constructions in proofs such as Book I, Prop. "
                 "47 ('Bride's Chair')."),
                ('1841 and 1928',
                 'Arthur Cayley (1841) and Karl Menger (1928) give determinant criteria for when '
                 'a set of distances can be realized by points in Euclidean space.'),
                ('Late 1970s',
                 'Wu Wen-Tsun develops algebraic methods for automated geometry deductions via '
                 'characteristic sets.'),
                ('2024',
                 'Trinh et al. publish AlphaGeometry in Nature (DOI 10.1038/s41586-023-06747-5), '
                 'reporting 25 of 30 olympiad-level problems solved.'),
                ('2025',
                 'Chervonyi et al. report AlphaGeometry2 solving 84% of IMO geometry problems from '
                 '2000 to 2024, against 54% for the first version (arXiv:2502.03544).')],
 'act2_title': 'Act II — How It Actually Works: DD+AR Closure + Cayley–Menger Distance Rigidity',
 'act2_analogy': 'Everyday analogy: Imagine assembling a wobbly four-bar picture frame from wooden slats pinned loosely at the four corners. If you nudge the top rail, the entire square distorts into a leaning rhombus because the corner joints can swivel freely. However, if you nail a single diagonal wooden slat across two opposite corners, the wobbly square instantly locks into two rigid triangles that cannot flex or sway no matter how hard you push.',
 'act2_plain_primer': 'To see how geometric locking works in practice, you can explore two intuitive control knobs. The first knob controls the auxiliary construction depth, determining how many helper pins or diagonal braces the computer is allowed to introduce into the diagram. With zero helper pins, a loose diagram wanders aimlessly with excess degrees of freedom. But as you dial in one or two auxiliary anchors, the system triangulates loose hinges, drastically shrinking ambiguity. The second knob sets constraint density, measuring how many geometric rules—such as parallel lines, equal angles, and circular tangents—crush into the workspace. When rules are sparse, shapes drift like loose scaffolding. But as constraint crowding approaches the critical threshold, adding a single diagonal cross-brace causes the entire system to snap into an unshakeable, rigid structure. Together, these two knobs are a picture of how a single well-placed point can turn a wobbly frame into a rigid one; they are not data from AlphaGeometry.',
 'distill_diagram': {'analogy_title': 'Diagonal Cross-Braced Truss', 'analogy_sub': 'Single diagonal slat locks wobbly frame into rigid triangles', 'force_a_title': 'Auxiliary Anchor Depth (k_aux)', 'force_a_sub': 'Number of neural helper points proposed to bridge stalled logic', 'force_b_title': 'Constraint Graph Density (alpha)', 'force_b_sub': 'Ratio of geometric incidences to vertices in deductive closure', 'threshold_title': 'Cayley-Menger Rigidity Barrier', 'threshold_pass': 'Deductive closure grows from 14 to 47 invariants (fixed illustrative values)', 'threshold_fail': 'Under-constrained linkages stay flexible without an added point'},
 'act2_intuition': 'In the symbolic part of AlphaGeometry, the engine (DD+AR) tracks collinearities, concyclic points and ratio relations using forward-chaining rules. When the premises do not give enough relations, the symbolic propagation stalls at an incomplete fixed point. This is where the neural model intervenes: it proposes an auxiliary construction X_aux, such as a new point or circle, after which the symbolic engine resumes. Adding one such point acts like inserting a diagonal member into a planar truss, which is the folio\'s picture. Separately, the Cayley–Menger determinant gives a condition on squared distances: five points in Euclidean three-space satisfy det(B_5) = 0. The numbers 14 and 47 on this page are fixed illustrative values for the size of a deductive closure before and after adding a point; they are not results from Trinh et al.',
 'act2_deepening': 'In the symbolic phase, the Deductive Database keeps relations among angles and ratios, while Algebraic Rules apply vector and area formulas such as the law of sines. When this closure saturates without proving the theorem, an auxiliary point can add new relations. The Cayley–Menger determinant is a classical condition on a matrix of squared distances: for five points in R^3 it must vanish. The two sliders on this page, auxiliary depth and constraint density, drive an illustration and are not AlphaGeometry parameters; the page does not claim a phase boundary or a rigidity proof.',
 'walkthrough': ['Experiment 1 (Auxiliary Anchor Injection): Inspect how adding 1 auxiliary '
                 'point X_aux changes an illustrative deductive closure from 14 base incidences to '
                 '47 invariants (fixed illustrative values).',
                 'Experiment 2 (Depth & Density Sliders): Adjust the interactive sliders to '
                 'see the illustration change; they are not measurements of AlphaGeometry.',
                 'Experiment 3 (Cayley–Menger Condition): Follow Steps 1 to 4 to see the '
                 'condition det(B_5) = 0 for five points in three-dimensional space.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification '
               'Bridge',
 'act4_human_ai': 'A proof assistant such as Lean can check geometric arguments step by step. The HepLean paper (DOI 10.1016/j.cpc.2024.109457; the project is now hosted as leanprover-community/physlib) and Mathlib (DOI 10.1145/3372885.3373824) are libraries a reader could look at. This folio ran no such checks, and it makes no claim about structural biology or engineering.',
 'act4_deepening': 'One can imagine feeding the symbolic traces of a geometry prover into a proof assistant such as Lean 4 so that each deduction is checked. That is a possibility, not something this folio did or has seen reported. Open questions in this area, such as extending auxiliary-construction search beyond Euclidean plane geometry, are not addressed here.',
 'cf_bridge': 'This bridge is an analogy the folio draws and nothing more. Fiedorczuk & Chen '
              '(2022, DOI 10.1126/science.ade2216; PDB 8EIQ) report cryo-electron microscopy '
              'structures of Δ508 CFTR with modulators. The folio borrows only the picture of an '
              'added point fixing a shape. It makes no claim about how any drug works, and nothing '
              'here is medical advice.',
 'sources': ['Trinh, T. H., Wu, Y., Le, Q. V., He, H., & Luong, T. (2024). Solving olympiad '
             'geometry without human demonstrations. Nature, 625, 476–482. DOI: '
             '10.1038/s41586-023-06747-5.',
             'Chervonyi, Y., Trinh, T. H., Olšák, M., et al. (2025). Gold-medalist performance in '
             'solving olympiad geometry with AlphaGeometry2. arXiv:2502.03544.',
             'Chou, S. C., Gao, X. S., & Zhang, J. Z. (1994). Machine Proofs in Geometry: '
             'Automated Production of Readable Proofs for Geometry Theorems. World Scientific.',
             'Fiedorczuk, K., & Chen, J. (2022). Molecular structures reveal synergistic rescue '
             'of Δ508 CFTR by Trikafta modulators (PDB 8EIQ). Science, 378(6617), 284–290. '
             'DOI: 10.1126/science.ade2216.',
             'Tooby-Smith, J. (2025). HepLean: Digitalising high energy physics. Computer Physics '
             'Communications, 308, 109457. DOI: 10.1016/j.cpc.2024.109457 (repository now '
             'leanprover-community/physlib, formerly HEPLean/PhysLean).',
             'The mathlib Community (2020). The Lean mathematical library (CPP 2020), '
             '367–381. DOI: 10.1145/3372885.3373824.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Neuro-symbolic '
        'auxiliary construction X_aux fixing a triangle (illustration)">\n'
        '            <circle cx="220" cy="112" r="78" fill="none" stroke="currentColor" '
        'stroke-opacity="0.35" stroke-width="1.5"/>\n'
        '            <polygon points="155,152 285,152 220,42" fill="var(--tp-prussian)" '
        'fill-opacity="0.12" stroke="var(--tp-prussian)" stroke-width="2.5"/>\n'
        '            <circle cx="220" cy="112" r="6" fill="var(--tp-minium)"/>\n'
        '            <line x1="155" y1="152" x2="220" y2="112" stroke="var(--tp-minium)" '
        'stroke-width="2" stroke-dasharray="4,3"/>\n'
        '            <line x1="285" y1="152" x2="220" y2="112" stroke="var(--tp-minium)" '
        'stroke-width="2" stroke-dasharray="4,3"/>\n'
        '            <line x1="220" y1="42" x2="220" y2="112" stroke="var(--tp-minium)" '
        'stroke-width="2" stroke-dasharray="4,3"/>\n'
        '            <text x="120" y="172" font-size="11" fill="currentColor">Point A</text>\n'
        '            <text x="255" y="172" font-size="11" fill="currentColor">Point B'
        '</text>\n'
        '            <text x="195" y="30" font-size="11" fill="currentColor">Point C</text>\n'
        '            <text x="232" y="114" font-size="11" fill="var(--tp-minium)">X_aux (auxiliary '
        'point)</text>\n'
        '            <rect x="375" y="45" width="265" height="130" fill="none" '
        'stroke="var(--tp-verdigris)" stroke-width="1.8"/>\n'
        '            <text x="390" y="72" font-size="11" fill="var(--tp-verdigris)">DD+AR + '
        'Cayley-Menger Closure</text>\n'
        '            <text x="390" y="98" font-size="11" fill="currentColor">Base Incidences: 14 → '
        'Closure: 47 (illustrative)</text>\n'
        '            <text x="390" y="122" font-size="11" fill="currentColor">det(B_5) = 0 for '
        '5 points in R^3</text>\n'
        '            <text x="390" y="146" font-size="11" fill="var(--tp-prussian)">Illustration '
        'only, not a measurement</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what Euclidean compass-and-straightedge constructions '
        'locking a 3D polyhedral truss via an auxiliary point would look like (artistic '
        'impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate M.05-V (Imagining What It Would Look Like) · Artistic '
            'geometric visualization imagining brass compass-and-straightedge circles and a '
            'crimson auxiliary point locking a 3D triangulated truss.'}

DISPATCH = {'kicker': 'REPORTED RESULTS · DEEPMIND ALPHAGEOMETRY AND ALPHAGEOMETRY2',
 'headline': 'AlphaGeometry Reports 25 of 30 Olympiad Problems; AlphaGeometry2 Reports 84% of IMO '
             'Geometry 2000–2024',
 'body': 'Published in Nature by Trinh, Wu, Le, He & Luong (DOI 10.1038/s41586-023-06747-5), '
         'AlphaGeometry pairs a symbolic deduction engine with a neural model, trained on about '
         '100 million synthetic theorems, that proposes auxiliary constructions, and reports 25 '
         'of 30 olympiad-level test problems solved. A follow-up report on AlphaGeometry2 '
         '(arXiv:2502.03544) states an 84% solving rate on IMO geometry problems from 2000 to '
         '2024. This site reports these results and did not reproduce them.'}

META_3D = ('AlphaGeometry 2 Polyhedral Tropical Roof',
 'X/Z: Tropical Valuation Plane · Y: Piecewise-Linear Tropical Polynomial & Auxiliary Cone')

ES_TRANSLATION = {'title_es': 'Búsqueda Deductiva Neuro-Simbólica (AlphaGeometry 2): Construcciones Auxiliares y '
             'Triangulación de Bolsillos Alostéricos',
 'subtitle_es': 'Cómo AlphaGeometry acopla un motor simbólico de Base de Datos Deductiva + Reglas '
                'Algebraicas (DD+AR) con un modelo neuronal que propone puntos auxiliares, según '
                'lo reportado en Nature y en un informe posterior sobre AlphaGeometry2. La '
                'comparación con fijar una forma añadiendo un punto de apoyo es una imagen de '
                'este folio, y cualquier vínculo con la estructura de proteínas es una analogía.',
 'why_es': 'Un marco cuadrado de cuatro barras se deforma fácilmente hasta que añades una sola '
           'barra diagonal (una construcción auxiliar), la cual bloquea toda la estructura en '
           'triángulos rígidos.',
 'bridge_es': 'Es solo una analogía de este folio: Fiedorczuk y Chen (2022, DOI '
              '10.1126/science.ade2216; PDB 8EIQ) reportan estructuras de crio-microscopía '
              'electrónica de la CFTR Δ508 con moduladores. El folio toma prestada únicamente la '
              'imagen de un punto añadido que fija una forma. No afirma nada sobre cómo actúa '
              'ningún medicamento, y nada de esto es consejo médico.',
 'plain_es': 'En palabras sencillas, resolver un problema difícil de geometría puede sentirse como andar por una casa a oscuras. Tenemos un manojo de reglas conocidas sobre ángulos, paralelas y círculos, pero ninguna parece abrir la siguiente puerta. A veces el camino es añadir una línea o un punto auxiliar al dibujo, y entonces las reglas que ya teníamos vuelven a servir. Un programa que solo aplica reglas a lo que ya está dibujado no puede hacer eso. AlphaGeometry combina un motor que aplica reglas con un modelo neuronal que sugiere puntos auxiliares. Este folio no afirma que el método se use fuera de los problemas de geometría.',
 'deep_es': 'Para entender este tema, conviene observar que, en la parte simbólica, el motor DD+AR sigue relaciones de colinealidad, puntos concíclicos y razones; cuando se queda sin relaciones nuevas, el modelo neuronal propone una construcción auxiliar y el motor continúa. Un solo punto añadido actúa como una diagonal en una armadura plana, que es la imagen de este folio. El determinante de Cayley–Menger es una condición clásica sobre las distancias al cuadrado: cinco puntos en el espacio euclidiano tridimensional cumplen det(B_5) = 0. Los números 14 y 47 de esta página son valores ilustrativos fijos, y los dos deslizadores impulsan una ilustración; no son mediciones de AlphaGeometry. El artículo de Nature reporta 25 de 30 problemas resueltos, y un informe posterior sobre AlphaGeometry2 reporta 84 % de los problemas de geometría de la IMO de 2000 a 2024; este sitio reporta esos resultados y no los reprodujo.'}
