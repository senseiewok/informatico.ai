#!/usr/bin/env python3
"""Folio A.01 (ARCHITECTURE): Funicular Thrust Surfaces, Maxwell–Cremona Duals, and 1:5 Nodal Tectonics."""
from __future__ import annotations

SLUG = 'a01'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.01',
 'slug': 'a01',
 'pillar': 'architecture',
 'category_code': 'A',
 'title': 'Funicular Thrust Surfaces, Maxwell–Cremona Duals, and 1:5 Nodal Tectonics',
 'subtitle': "How a compression-only stone vault stands when its thrust line stays inside the masonry (Heyman's safe theorem), checked here against the stricter classical middle-third rule (|e| ≤ t/6), with an illustrative 1:5 springer node whose inside surface is modelled as staying above the dew point.",
 'date_published': '2026-10-20',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.4',
 'status_badge': 'REDATED REV 1.4',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'H = qL² / (8f) · |e| ≤ t/6',
 'colophon': {'identifier': 'A.01 · Vaults & Thermal Nodes',
              'kernels': '1:50 Section + 1:5 Nodal Loupe',
              'benchmarks': 'Model: middle-third rule |e| ≤ t/6 (geometric factor ≥ 3)',
              'bridge': 'Illustrative thermal-bridge node (ISO 10211 / ISO 13788 calculation methods)'},
 'steps': ['Stage 1 (Dead-Load Catenary): Under self-weight, the inverted catenary thrust line follows the centre line of the vault (e = 0 mm).',
           'Stage 2 (Asymmetric Haunch Load): Live load at the quarter-span shifts the funicular thrust line toward '
           'the extrados at the loaded haunch; at the default e = 32 mm the geometric factor is t/(2|e|) = 600/64 = 9.38.',
           'Stage 3 (Maxwell-Cremona Reciprocal Dual): With q = 24 kN/m, L = 18 m and f = 4.5 m, the horizontal ray H = qL²/(8f) = 216.0 kN and the vertical reaction V = qL/2 = 216.0 kN close the force polygon.',
           'Stage 4 (1:5 Springer Node A-04): A load-bearing thermal break with an assumed λ = 0.19 W/(m·K) is modelled as keeping the interior surface at T_si = 16.4 °C, above the dew point T_dew = 9.3 °C of air at 20 °C and 50% RH. T_si is a fixed illustrative value, not a calculated or measured one.'],
 'readouts': [{'label': 'Horizontal Thrust (H)', 'value': '216.0 kN'},
              {'label': 'Eccentricity vs Middle-Third', 'value': '32 / 100 mm'},
              {'label': 'Middle-Third Check (Model)', 'value': 'INSIDE MIDDLE THIRD (SF 9.38)'},
              {'label': 'Thermal Node (Illustrative)', 'value': 'T_si = 16.4 °C > T_dew = 9.3 °C'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 05 12 00 / 07 21 00',
                'title': 'Load-Bearing Structural Thermal Break Module (Node A-04)',
                'body': 'Illustrative specification for a load-bearing thermal-break pad under a masonry vault springer. The compressive design resistance σ_Rd = 45 MPa and thermal conductivity λ = 0.19 W/(m·K) are design assumptions, not data from a tested product; ordinary concrete conducts heat several times better than this.',
                'meta': 'Design sketch only · no BIM or CAD files are published · not tested or certified to any standard'},
 'sidenote_1': {'kicker': "SIDENOTE A.01 · HEYMAN'S SAFE THEOREM (1966)",
                'body': 'Jacques Heyman (1966, DOI 10.1016/0020-7683(66)90018-7) applied plastic theory to masonry: if any thrust line in equilibrium with the loads can be found that lies wholly within the masonry, the structure is safe. The middle-third rule |e| ≤ t/6 is an older and stricter condition that keeps the whole joint in compression; this folio uses it as its design target.'},
 'skill': {'filename': 'tectonic-funicular-envelope-SKILL.md',
           'name': 'tectonic-funicular-envelope',
           'description': 'AI-agnostic architectural and structural engineering skill for funicular vault graphic '
                          'statics (middle-third rule |e| <= t/6 as a design target) and a 1:5 thermal-break node check.',
           'rules': ['Horizontal Thrust: H = q * L^2 / (8 * f) under uniform line load q across span L and rise f.',
                     'Thrust-line check: compute the geometric factor SF = t / (2 * |e|). SF >= 3 means the thrust line is inside the middle third (|e| <= t / 6); SF = 1 means it has reached the edge, where a hinge can form. Report this as a model result, not as proof of safety.',
                     '1:5 Springer Thermal Node: check T_si > T_dew and the temperature factor f_Rsi = (T_si - T_e) / (T_i - T_e) defined in ISO 13788. The target f_Rsi >= 0.70 is this folio\'s own choice, not a requirement of the standard; state T_i, T_e and humidity with every result.']},
 'revisions': [{'edition': 'REV 1.4',
                'date': '2026-11-14',
                'summary': 'REV 1.4 (Redated 2026-11-14): Grounding revision. Earlier editions called the middle-third rule "Heyman\'s Safe Theorem"; Heyman\'s theorem only needs a thrust line inside the masonry, and the text now says so. No verification or certification of the thermal node was performed, and claims of preventing mould or infection in healthcare settings are withdrawn: nothing was measured. An unsourced scene about Hooke and Wren and an unsourced 70% concrete-saving figure are removed.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; model numbers recomputed from the stated formulas.'},
               {'edition': 'REV 1.3',
                'date': '2026-11-02',
                'summary': 'REV 1.3 (Redated 2026-11-02): Reported a +7.08 °C margin between the illustrative surface temperature and the dew point. No certification or fungal-reservoir prevention was measured; earlier wording is withdrawn in REV 1.4.',
                'opus': 'Council review of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B); the earlier word "verified" is withdrawn in REV 1.4 because nothing was measured. Arithmetic reviewed:horizontal thrust H = '
                        '216.0 kN, kern safety factor SF = 9.38, and f_Rsi >= 0.70 condensation protection.'},
               {'edition': 'REV 1.2',
                'date': '2026-11-01',
                'summary': 'REV 1.2 (Redated 2026-11-01): Added dynamic Maxwell-Cremona Reciprocal Force Dual SVG and '
                           'CSI 05 12 00 / 07 21 00 UHPC thermal-break plate.',
                'opus': 'Council review of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B); the earlier word "verified" is withdrawn in REV 1.4 because nothing was measured. Arithmetic reviewed:H = 216.0 kN, SF = 9.38, '
                        'and f_Rsi ≥ 0.70 condensation margin.'},
               {'edition': 'REV 1.1',
                'date': '2026-10-27',
                'summary': 'REV 1.1 (Redated 2026-10-27): Coupled 1:50 vault section to 1:5 EN ISO 13788 Glaser '
                           'dew-point loupe.',
                'opus': 'Council review of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B); the earlier word "verified" is withdrawn in REV 1.4 because nothing was measured. Arithmetic reviewed:T_si = 16.4 °C > T_dew = '
                        '9.3 °C at 20 °C / 50% RH.'},
               {'edition': 'REV 1.0',
                'date': '2026-10-20',
                'summary': 'REV 1.0 (Published 2026-10-20): Initial 1:50 funicular catenary vault form diagram.',
                'opus': 'Council review of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B); the earlier word "verified" is withdrawn in REV 1.4 because nothing was measured. Arithmetic reviewed:middle-third kern '
                        'boundary |e| ≤ 100 mm.'}],
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1017/CBO9781107050310',
           'fetched_on': '2026-11-08',
           'citing_publications': 484,
           'supporting': 7,
           'mentioning': 282,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Heyman, The Stone Skeleton (DOI 10.1017/CBO9781107050310), checked 2026-11-08: 484 citing publications (7 supporting, 282 mentioning, 0 contrasting) and no retraction notice. The book is about masonry structures; it says nothing about the thermal node.'},
 'volume': 1,
 'volume_code': 'VOL. 01',
 'sliders': [{'label': 'Vault Crown Rise Parameter (f)',
              'min': 2.5,
              'max': 6.5,
              'step': 0.05,
              'value': 4.5,
              'unit': ' m'},
             {'label': 'Thrust Eccentricity / Nodal Offset (e vs t/6 = 100 mm)',
              'min': 0.0,
              'max': 0.16,
              'step': 0.004,
              'value': 0.032,
              'unit': ' m'}]}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'history_lead': "In the 1670s London was rebuilding after the Great Fire, and work on the new St Paul's Cathedral began in 1675. Around the same time Robert Hooke, who worked alongside Christopher Wren on the rebuilding, printed a Latin anagram at the end of his book A Description of Helioscopes. Its solution was published only after his death, in 1705: as hangs the flexible line, so but inverted will stand the rigid arch. A hanging chain carries its own weight in pure tension. Turn the same curve upside down and build it in stone, and the stones carry their weight in pure compression.",
 'history_body': "Two centuries after Hooke, graphic statics took shape in the work of Karl Culmann, James Clerk Maxwell (1864, DOI 10.1080/14786446408643663) and Luigi Cremona: a drawing of a structure's form can be paired with a reciprocal drawing of its forces, so that forces can be read off with a ruler. Between 1898 and 1908 Antoni Gaudí used a hanging model of weighted cords to shape the church of the Colònia Güell. In 1966 Jacques Heyman brought these ideas into plastic limit analysis in his paper The Stone Skeleton (DOI 10.1016/0020-7683(66)90018-7), later expanded into a book (DOI 10.1017/CBO9781107050310). He assumed that masonry has no tensile strength, effectively unlimited compressive strength, and does not slide. Under those assumptions a vault is safe if a thrust line in equilibrium with the loads can be found that lies wholly within the masonry. More recently, three-dimensional graphic statics (Akbarzadeh, Van Mele and Block 2015, DOI 10.1016/j.cad.2015.01.006) and open tools such as compas-dev/compas (https://github.com/compas-dev/compas) have extended these methods to shells. This folio does not run those tools; its numbers come from the two formulas shown.",
 'pullquote': 'As hangs the flexible line, so but inverted will stand the rigid arch.',
 'pullquote_cite': 'Robert Hooke, anagram printed in A Description of Helioscopes (1670s); solution published 1705 (English translation of the Latin)',
 'chronology': [('1675',
                 'Robert Hooke',
                 'States, as an anagram, that a hanging chain turned upside down gives the shape of a standing arch; the solution is published in 1705.'),
                ('1864–1872',
                 'Maxwell, Culmann & Cremona',
                 'Develop reciprocal form-and-force diagrams, the basis of graphic statics.'),
                ('1898–1908',
                 'Antoni Gaudí',
                 'Builds a hanging model of weighted cords for the church of the Colònia Güell near Barcelona.'),
                ('1966',
                 'Jacques Heyman',
                 "Publishes 'The Stone Skeleton' (DOI 10.1016/0020-7683(66)90018-7), applying the safe theorem of plastic theory to masonry: a thrust line within the masonry is enough."),
                ('2026',
                 'Informatico.ai Folio A.01',
                 'Pairs an interactive thrust-line diagram with an illustrative thermal-bridge node. A teaching model, not a design check.')],
 'intuition_lead':'Why can an unreinforced stone vault stand for centuries, yet fail quickly if its abutments spread? Masonry is strong in compression, has almost no tensile strength, and resists sliding by friction. Jacques Heyman argued that the stability of such a structure is a matter of geometry rather than of crushing strength (The Stone Skeleton, DOI 10.1017/CBO9781107050310). While the thrust line stays inside the middle third of the section (|e| <= t/6, or within 100 millimeters of the centre of a 600-millimeter vault), the whole joint is in compression. Beyond t/6 the far edge of the joint begins to open, because dry joints cannot pull. A hinge forms only when the thrust line reaches the edge of the section (|e| = t/2), and an arch needs four such hinges to become a mechanism. The folio therefore reports a geometric factor SF = t/(2|e|): 3 at the middle-third limit, 1 at the edge. The thermal node is a separate, simpler model: it compares an assumed inside surface temperature with the dew point of the room air, using the quantities defined in ISO 13788. Nothing here was computed in compas-dev/compas (https://github.com/compas-dev/compas); it is named as a tool a reader could use for three-dimensional graphic statics (DOI 10.1016/j.cad.2015.01.006).',
 'intuition_body': 'As long as the resultant compressive force acts within the middle third of the cross-section '
                   '(eccentricity |e| <= t/6, or +/-100 mm inside a 600 mm vault), the entire thickness remains in '
                   'compression. When |e| exceeds t/6, the opposite face tries to go into tension; because dry '
                   'joints cannot pull, the joint starts to open there. A full hinge forms once the thrust line reaches the edge, and four hinges turn the arch into a collapse mechanism. Meanwhile, at the 1:5 abutment support where that 216 kN horizontal thrust '
                   'meets the foundation, the folio assumes a load-bearing thermal break that keeps the interior surface at 16.34 °C, which is 7.08 °C above the 9.26 °C dew point of room air at 20 °C and 50% relative humidity. The surface temperature is an illustrative value: the outdoor temperature and the node geometry that would produce it are not stated, and no ISO 10211 calculation was run.',
 'walkthrough': ['Experiment 1 (Scrub Crown Rise & Watch the Maxwell-Cremona Force Dual): Drag the Crown Rise slider '
                 '(f) between 2.5 m and 6.5 m. Watch both the 1:50 arch profile and the reciprocal pole O in the '
                 'Maxwell-Cremona force polygon shift live as horizontal thrust H = qL^2/(8f) changes.',
                 'Experiment 2 (Push Eccentricity Past the Middle-Third Kern): Drag the Asymmetric Live-Load '
                 'Eccentricity slider past 100 mm (t/6). Watch the readout change once the thrust line leaves the middle third; in the model this is where a joint would start to open.',
                 'Experiment 3 (Switch Between 1:50 Macro & 1:5 Nodal Scales): Click Stages 1 -> 4 in the stepper '
                 'above to inspect the Glaser vapor-pressure profile and CSI 07 27 00 thermal-break assembly.'],
 'human_ai_shift': 'Finite-element software often shows force flow only as colour maps. Graphic statics offers a more direct view: change the geometry and the force diagram changes with it. A designer, with or without an AI assistant, could pair form-and-force diagrams from a tool such as compas-dev/compas (https://github.com/compas-dev/compas; see DOI 10.1016/j.cad.2015.01.006 for the underlying three-dimensional graphic statics) with a heat-and-moisture model built on a finite-element library such as FEniCS/dolfinx (DOI 10.1145/3524456), and look for a stone shell that keeps its geometric factor at 3 or more while its inside surfaces stay above the dew point. This is a proposal for a workflow. The folio did not run these tools.',
 'cf_bridge': 'This bridge is modest. Surfaces that stay colder than the dew point of the room air collect condensation, and persistently damp building materials can support mould growth. Allergic bronchopulmonary aspergillosis is a recognised complication in people with Cystic Fibrosis (Stevens et al. 2003, DOI 10.1086/376525). This folio is a building-physics study. It measured no building, reports no health outcome, and is not medical or infection-control advice; people with CF should follow their care team.',
 'sources': ['Hooke, R. (1676). A Description of Helioscopes, and Some Other Instruments. London. (Contains the arch anagram; the solution was published in 1705.)',
             'Maxwell, J. C. (1864). On reciprocal figures and diagrams of forces. Philosophical Magazine, 27(182), '
             '250–261. DOI: 10.1080/14786446408643663.',
             'Heyman, J. (1966). The stone skeleton. International Journal of Solids and Structures, 2(2), 249–279. DOI: 10.1016/0020-7683(66)90018-7.',
             'Heyman, J. (1995). The Stone Skeleton: Structural Engineering of Masonry Architecture. Cambridge '
             'University Press. DOI: 10.1017/CBO9781107050310.',
             'ISO 13788 (2012). Hygrothermal performance of building components and building elements — Internal surface temperature to avoid critical surface humidity and interstitial condensation — Calculation methods.',
             'ISO 10211 (2017). Thermal bridges in building construction — Heat flows and surface temperatures — Detailed calculations.',
             'Stevens, D. A., et al. (2003). Allergic Bronchopulmonary Aspergillosis in Cystic Fibrosis—State of the Art: Cystic Fibrosis Foundation Consensus Conference. Clinical Infectious Diseases, 37(s3), S225–S264. DOI: 10.1086/376525.',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). ACM Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: 10.1145/3524456.',
             'Akbarzadeh, M., Van Mele, T., & Block, P. (2015). On the equilibrium of funicular polyhedral frames and '
             'convex polyhedral force diagrams (compas-dev/compas, https://github.com/compas-dev/compas). '
             'Computer-Aided Design, 63, 118–128. DOI: 10.1016/j.cad.2015.01.006.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations '
             'and classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
             '882–898. DOI: 10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="1:50 Funicular vault and '
        'Maxwell-Cremona force dual">\n'
        '            <path d="M 50 185 Q 250 15 450 185" fill="none" stroke="currentColor" stroke-opacity="0.35" '
        'stroke-width="16"/>\n'
        '            <path d="M 50 185 Q 250 35 450 185" fill="none" stroke="var(--tp-minium)" stroke-width="3"/>\n'
        '            <g transform="translate(500, 35)">\n'
        '              <line x1="90" y1="15" x2="90" y2="135" stroke="currentColor" stroke-width="2"/>\n'
        '              <line x1="15" y1="75" x2="90" y2="75" stroke="var(--tp-prussian)" stroke-width="2.5" '
        'stroke-dasharray="4,3"/>\n'
        '              <line x1="15" y1="75" x2="90" y2="15" stroke="var(--tp-minium)" stroke-width="2"/>\n'
        '              <line x1="15" y1="75" x2="90" y2="135" stroke="var(--tp-minium)" stroke-width="2"/>\n'
        '              <circle cx="15" cy="75" r="4.5" fill="var(--tp-prussian)"/>\n'
        '              <text x="5" y="95" font-size="10" fill="var(--tp-prussian)">Pole O (H=216 kN)</text>\n'
        '            </g>\n'
        '            <text x="155" y="205" font-size="11" fill="var(--tp-minium)">1:50 Funicular Thrust Line (|e| = 32 '
        'mm ≤ 100 mm Kern)</text>\n'
        '          </svg>',
 'scite': {'doi': '10.1017/CBO9781107050310',
           'fetched_on': '2026-11-08',
           'citing_publications': 484,
           'supporting': 7,
           'mentioning': 282,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Heyman, The Stone Skeleton (DOI 10.1017/CBO9781107050310), checked 2026-11-08: 484 citing publications (7 supporting, 282 mentioning, 0 contrasting) and no retraction notice. The book is about masonry structures; it says nothing about the thermal node.'},
 'word_count': '4,650 WORDS',
 'act1_dropcap': "In the 1670s London was rebuilding after the Great Fire, and work on the new St Paul's Cathedral began in 1675. Around the same time Robert Hooke, who worked alongside Christopher Wren on the rebuilding, printed a Latin anagram at the end of his book A Description of Helioscopes. Its solution was published only after his death, in 1705: as hangs the flexible line, so but inverted will stand the rigid arch. A hanging chain carries its own weight in pure tension. Turn the same curve upside down and build it in stone, and the stones carry their weight in pure compression.",
 'act1_plain_bridge': 'To picture how an arch stands, think of leaning two heavy hardback books together on a slippery '
                      'wooden table. If the books lean too steeply, their tops dig together tightly and they stay '
                      'upright. But if you spread their bottoms even an inch too far apart, the inward push slides '
                      'outward and both books crash flat. Stone and brick are wonderfully strong when you squeeze them '
                      'together, but they cannot handle being pulled apart. When stones rest on one another without '
                      'steel pins, the invisible line of squeezing force must stay safely buried deep inside the '
                      'middle of each block. If that line wanders too close to the outside edge, the opposite face '
                      'cracks open like an opening door hinge. Modern builders also face a quiet second threat at the '
                      'chilly base: keeping that heavy stone boundary warm and dry so winter frost does not rot the '
                      'foundation or breed mold in the air.',
 'act1_body': "Two centuries after Hooke, graphic statics took shape in the work of Karl Culmann, James Clerk Maxwell (1864, DOI 10.1080/14786446408643663) and Luigi Cremona: a drawing of a structure's form can be paired with a reciprocal drawing of its forces, so that forces can be read off with a ruler. Between 1898 and 1908 Antoni Gaudí used a hanging model of weighted cords to shape the church of the Colònia Güell. In 1966 Jacques Heyman brought these ideas into plastic limit analysis in his paper The Stone Skeleton (DOI 10.1016/0020-7683(66)90018-7), later expanded into a book (DOI 10.1017/CBO9781107050310). He assumed that masonry has no tensile strength, effectively unlimited compressive strength, and does not slide. Under those assumptions a vault is safe if a thrust line in equilibrium with the loads can be found that lies wholly within the masonry. More recently, three-dimensional graphic statics (Akbarzadeh, Van Mele and Block 2015, DOI 10.1016/j.cad.2015.01.006) and open tools such as compas-dev/compas (https://github.com/compas-dev/compas) have extended these methods to shells. This folio does not run those tools; its numbers come from the two formulas shown.",
 'act1_stakes': 'For centuries, medieval master masons relied on secret proportional geometric ratios guarded in lodge '
                'sketchbooks to size massive exterior flying buttresses. But geometric rules of thumb only work when '
                'construction materials, building proportions, and seasonal weather remain predictable. When '
                'unexpected soil settlement shifts a foundation footing outward by even a few inches, or when '
                'asymmetrical wind and snow push the thrust path outside the middle third of the stone thickness, '
                'structural stability rapidly deteriorates. The stones unclamp along dry mortar joints, transforming a '
                'rigid roof into a wobbling four-hinge linkage that buckles catastrophically under its own immense '
                'dead weight. Today, modern architects face an equally unforgiving thermal hazard: bridging that '
                'massive stone abutment into heated interior living spaces without a dedicated thermal barrier creates '
                'a severe cold spot. That chilly bridge draws indoor humidity into porous limestone pores, sparking '
                'winter condensation, hidden frost cracking, and aggressive mold spores.',
 'act2_analogy': 'Everyday analogy: Imagine carrying a heavy grocery sack pressed firmly against your chest versus '
                 "holding it at arm's length. Held tight against your ribs, gravity passes straight down through your "
                 'spine and legs in pure compression. But the moment you extend your arms outward, the weight levers '
                 'against your lower back, forcing back muscles to pull in sharp tension. An unreinforced masonry '
                 'vault behaves the same way: keeping thrust centered feels effortless, but pushing it off-center '
                 'demands tension that dry stones simply cannot supply.',
 'act2_plain_primer': 'In the interactive laboratory below, you control two physical knobs that determine whether a '
                      'stone shell stands proud or collapses in ruins. The first knob adjusts the crown rise of the '
                      'vault—how tall the arch arches overhead relative to its span across the room. When you flatten '
                      'the arch into a low, gentle curve, the stones push outward against the side walls with '
                      'ferocious horizontal force, like someone doing a vigorous split on slick ice. Making the arch '
                      'taller guides that downward weight more gently into the ground. The second knob introduces '
                      'live-load eccentricity, which represents an uneven weight like a heavy snow drift piled high on '
                      'only one flank of the roof. Dragging this second knob pushes the internal line of squeezing '
                      'force sideways away from the center of the masonry blocks. If you nudge that line beyond the '
                      'safe middle boundary, visible cracks appear.',
 'distill_diagram': {'analogy_title': 'Weight Pressed Against Spine vs Arms',
                     'analogy_sub': 'Centered loads compress; off-center loads create dangerous tension',
                     'force_a_title': 'Vault Crown Rise (f)',
                     'force_a_sub': 'Taller rise reduces outward horizontal thrust against abutments',
                     'force_b_title': 'Thrust Eccentricity (e)',
                     'force_b_sub': 'Asymmetric snow shifts the internal force path toward the face',
                     'threshold_title': 'Middle-Third Kern Boundary (|e| <= t/6)',
                     'threshold_pass': 'Model: whole joint in compression (geometric factor 3 or more)',
                     'threshold_fail': 'Model: joint starts to open; a hinge forms only if thrust reaches the edge'},
 'act2_intuition': 'Why can an unreinforced stone vault stand for centuries, yet fail quickly if its abutments spread? Masonry is strong in compression, has almost no tensile strength, and resists sliding by friction. Jacques Heyman argued that the stability of such a structure is a matter of geometry rather than of crushing strength (The Stone Skeleton, DOI 10.1017/CBO9781107050310). While the thrust line stays inside the middle third of the section (|e| <= t/6, or within 100 millimeters of the centre of a 600-millimeter vault), the whole joint is in compression. Beyond t/6 the far edge of the joint begins to open, because dry joints cannot pull. A hinge forms only when the thrust line reaches the edge of the section (|e| = t/2), and an arch needs four such hinges to become a mechanism. The folio therefore reports a geometric factor SF = t/(2|e|): 3 at the middle-third limit, 1 at the edge. The thermal node is a separate, simpler model: it compares an assumed inside surface temperature with the dew point of the room air, using the quantities defined in ISO 13788. Nothing here was computed in compas-dev/compas (https://github.com/compas-dev/compas); it is named as a tool a reader could use for three-dimensional graphic statics (DOI 10.1016/j.cad.2015.01.006).',
 'act2_deepening': 'The physical coupling between crown rise and thrust eccentricity reveals why shell design requires '
                   'dual-scale analysis. The horizontal thrust acting at the vault springers scales inversely with '
                   'crown rise: halving the arch height doubles the outward thrust force pushed against the abutments. '
                   'When an asymmetric live load shifts the funicular line toward the extrados at the quarter-span, '
                   'that heightened thrust magnifies the overturning moment on foundation piers. If the abutment '
                   'rotates outward by even a fraction of a degree, the span widens, dropping the crown and pushing '
                   'the thrust line even further toward the intrados. At the 1:5 scale abutment node, that '
                   'concentrated compressive force must pass through a specialized structural thermal break. Because '
                   'ordinary insulation crushes under high thrust, a load-bearing thermal-break element is needed, one that is both strong in compression and a poor conductor of heat. The folio assumes such an element; it is a design target meant to carry the thrust while keeping the interior surface above the dew point, not a tested product.',
 'act4_deepening': 'What follows is a proposal, not a description of current practice. A designer and an AI assistant could work in a loop: rather than using finite-element analysis only as a late check, a generative workflow could build the middle-third rule into the shape search. The designer would guide proportions, daylight and civic expression, while the assistant computes reciprocal Maxwell-Cremona diagrams for many candidate shapes and sets aside those that need very thick abutments. At the small scale, heat-and-moisture models could size thermal breaks for 1:5 nodes to reduce cold spots without giving up bearing stiffness. An open question centers '
                   'on autonomous robotic assembly: can cooperative climbing agents dynamically adjust mortar-free '
                   'stone placement during erection as real-time laser scanning detects sub-millimeter foundation '
                   'shifts, preserving funicular equilibrium and preventing premature hinge formation throughout every '
                   'intermediate stage of vault construction?',
 'act4_human_ai': 'Finite-element software often shows force flow only as colour maps. Graphic statics offers a more direct view: change the geometry and the force diagram changes with it. A designer, with or without an AI assistant, could pair form-and-force diagrams from a tool such as compas-dev/compas (https://github.com/compas-dev/compas; see DOI 10.1016/j.cad.2015.01.006 for the underlying three-dimensional graphic statics) with a heat-and-moisture model built on a finite-element library such as FEniCS/dolfinx (DOI 10.1145/3524456), and look for a stone shell that keeps its geometric factor at 3 or more while its inside surfaces stay above the dew point. This is a proposal for a workflow. The folio did not run these tools.'}

PLATE_CAPTION = {'alt': "Conceptual visualization imagining what Gaudi's hanging chain catenary model paired with Heyman's stone "
        'masonry funicular vault would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.01-V (Imagining What It Would Look Like) · Artistic architectural cutaway '
            "imagining Antoni Gaudi's inverted catenary hanging-chain model suspended beneath an unreinforced "
            'limestone ashlar funicular vault.'}

DISPATCH = {'kicker': 'FRONTIER TECTONIC DISPATCH · THRUST NETWORK ANALYSIS (TNA)',
 'headline': "3D Graphic Statics & Thrust Network Analysis Extend Heyman's Safe Theorem to Freeform Vaults",
 'body': "Jacques Heyman's safe theorem for masonry (DOI 10.1017/CBO9781107050310) says a vault stands if a thrust line can be found inside the stone. Three-dimensional graphic statics (Akbarzadeh, Van Mele and Block 2015, DOI 10.1016/j.cad.2015.01.006) extends the form-and-force diagrams of the nineteenth century to freeform shells. This folio shows the two-dimensional version as a teaching model."}

META_3D = ('Heyman Biaxial Catenary Masonry Groin Vault',
 'X: Vault Span L (18 m) · Z: Transverse Bay · Y: Inverted Funicular Thrust Line & Kern Envelope')

ES_TRANSLATION = {'title_es': 'Superficies Foniculares de Empuje, Duales de Maxwell–Cremona y Tectónica Nodal 1:5',
 'subtitle_es': 'Cómo una bóveda de piedra a compresión pura se sostiene cuando su línea de empuje queda dentro de la mampostería (teorema de seguridad de Heyman), revisada aquí con la regla clásica, más estricta, del tercio medio (|e| ≤ t/6), junto con un nodo de arranque ilustrativo a escala 1:5 cuya superficie interior se modela por encima del punto de rocío.',
 'why_es': 'Una cadena colgante adopta por gravedad una forma de tracción pura; al invertirla como un arco de '
           'piedra (catenaria invertida de Hooke y Gaudí), toda la estructura trabaja en compresión pura sin doblarse.',
 'bridge_es': 'Este puente es modesto. Las superficies más frías que el punto de rocío del aire interior acumulan condensación, y los materiales que permanecen húmedos pueden favorecer el crecimiento de moho. La aspergilosis broncopulmonar alérgica es una complicación reconocida en personas con Fibrosis Quística (Stevens et al. 2003, DOI 10.1086/376525). Este folio es un estudio de física de edificios: no midió ningún edificio, no reporta resultados de salud y no es una recomendación médica ni de control de infecciones; las personas con FQ deben seguir las indicaciones de su equipo de atención.',
 'plain_es': 'Para comprender cómo se sostiene una bóveda de piedra, imaginen apoyar dos libros gruesos sobre una mesa '
             'de madera pulida. Si los libros se inclinan con suficiente altura, sus extremos superiores se presionan '
             'con firmeza y permanecen firmes. Pero si separamos las bases unos centímetros de más, el empuje hacia '
             'afuera los vence y ambos caen de golpe sobre la mesa. La piedra y el ladrillo son materiales '
             'extraordinarios cuando se comprimen, pero carecen de fuerza para resistir tensiones que intenten '
             'separarlos. Cuando los bloques descansan unos sobre otros sin varillas de acero, la línea invisible de '
             'fuerza debe viajar por el tercio central de cada pieza. Si esa fuerza se desvía hacia el borde '
             'exterior, la junta contraria se abre como una bisagra. En la arquitectura actual, los constructores '
             'también deben resolver un segundo dilema en la base: aislar térmicamente el apoyo para que el frío '
             'exterior no condense la humedad interior en moho.',
 'deep_es': 'El equilibrio de una bóveda depende de la interacción directa entre dos fuerzas físicas: la altura del '
            'arco en la clave y la excentricidad del empuje por cargas asimétricas. Una bóveda más tendida genera un '
            'colosal empuje horizontal en los estribos, mientras que elevar la flecha dirige la gravedad de manera '
            'vertical hacia los cimientos. El teorema de seguridad de Heyman dice que la bóveda es estable si existe una línea de empuje en equilibrio que quede dentro de la mampostería; la regla del tercio medio, más antigua y más estricta, mantiene toda la junta en compresión y es la meta de diseño de este folio. Cuando el '
            'viento o la nieve cargan un solo lado, la línea de fuerza se desplaza hacia el intradós o el extradós; al salir del tercio medio la junta empieza a abrirse, y solo si la línea llega al borde se forma una rótula. Se necesitan cuatro rótulas para que el arco se convierta en un mecanismo. El nodo térmico del apoyo es un modelo ilustrativo: supone un elemento portante de baja conductividad y una temperatura superficial interior por encima del punto de rocío. Nada de esto fue medido ni calculado con programas especializados.'}
