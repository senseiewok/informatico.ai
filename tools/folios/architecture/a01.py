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
 'subtitle': "How a compression-only stone vault stands when its thrust line stays inside the masonry (Heyman's safe theorem), checked here against the stricter classical middle-third rule (|e| ≤ t/6), with an illustrative 1:5 springer node whose inside surface is modeled as staying above the dew point.",
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
 'steps': ['Stage 1 (Dead-Load Catenary): Under self-weight, the inverted catenary thrust line follows the center line of the vault (e = 0 mm).',
           'Stage 2 (Asymmetric Haunch Load): Live load at the quarter-span shifts the funicular thrust line toward '
           'the extrados at the loaded haunch; at the default e = 32 mm the geometric factor is t/(2|e|) = 600/64 = 9.38.',
           'Stage 3 (Maxwell-Cremona Reciprocal Dual): With q = 24 kN/m, L = 18 m and f = 4.5 m, the horizontal ray H = qL²/(8f) = 216.0 kN and the vertical reaction V = qL/2 = 216.0 kN close the force polygon.',
           'Stage 4 (1:5 Springer Node A-04): A load-bearing thermal break with an assumed λ = 0.19 W/(m·K) is modeled as keeping the interior surface at T_si = 16.4 °C, above the dew point T_dew = 9.3 °C of air at 20 °C and 50% RH. T_si is a fixed illustrative value, not a calculated or measured one.'],
 'readouts': [{'label': 'Horizontal Thrust (H)', 'value': '216.0 kN'},
              {'label': 'Eccentricity vs Middle-Third', 'value': '32 / 100 mm'},
              {'label': 'Middle-Third Check (Model)', 'value': 'INSIDE MIDDLE THIRD (SF 9.38)'},
              {'label': 'Thermal Node (Illustrative)', 'value': 'T_si = 16.4 °C > T_dew = 9.3 °C'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 05 12 00 / 07 21 00',
                'title': 'Load-Bearing Structural Thermal Break Module (Node A-04)',
                'body': 'Illustrative specification for a load-bearing thermal-break pad under a masonry vault springer. The compressive design resistance σ_Rd = 45 MPa and thermal conductivity λ = 0.19 W/(m·K) are design assumptions, not data from a tested product; ordinary concrete conducts heat several times better than this.',
                'meta': 'Design sketch only · no BIM or CAD files are published · not tested or certified to any standard'},
 'sidenote_1': {'kicker': "SIDENOTE A.01 · HEYMAN'S SAFE THEOREM (1966)",
                'body': 'Jacques Heyman (1966, DOI 10.1016/0020-7683(66)90018-7) applied plastic theory to masonry: if any thrust line in equilibrium with the loads can be found that lies wholly within the masonry, the structure is safe. The middle-third rule |e| ≤ t/6 is an older and stricter condition that keeps the whole joint in compression; this folio uses it as its model target.'},
 'skill': {'filename': 'tectonic-funicular-envelope-SKILL.md',
           'name': 'tectonic-funicular-envelope',
           'description': 'AI-agnostic teaching skill for funicular vault graphic statics (middle-third rule '
                          '|e| <= t/6 as the model target) and an illustrative 1:5 thermal-break node. Not a design method.',
           'rules': ['Scope: this skill explains a teaching model. It is not a design method, and none of its numbers may be used on a real structure.',
                     'Horizontal Thrust: H = q * L^2 / (8 * f) under uniform line load q across span L and rise f.',
                     'Thrust-line check: compute the geometric factor SF = t / (2 * |e|). SF >= 3 means the thrust line is inside the middle third (|e| <= t / 6); SF = 1 means it has reached the edge, where a hinge can form. Report this as a model result, not as proof of safety.',
                     '1:5 Springer Thermal Node: check T_si > T_dew and the temperature factor f_Rsi = (T_si - T_e) / (T_i - T_e) defined in ISO 13788. The target f_Rsi >= 0.70 is this folio\'s own choice, not a requirement of the standard; state T_i, T_e and humidity with every result.']},
 'revisions': [{'edition': 'REV 1.4',
                'date': '2026-11-14',
                'summary': 'REV 1.4 (Redated 2026-11-14): Grounding revision. Earlier editions called the middle-third rule "Heyman\'s Safe Theorem"; Heyman\'s theorem only needs a thrust line inside the masonry, and the text now says so. No verification or certification of the thermal node was performed, and claims of preventing mold or infection in healthcare settings are withdrawn: nothing was measured. An unsourced scene about Hooke and Wren and an unsourced 70% concrete-saving figure are removed.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; model numbers recomputed from the stated formulas.'},
               {'edition': 'REV 1.3',
                'date': '2026-11-02',
                'summary': 'REV 1.3 (Redated 2026-11-02): Reported a +7.08 °C margin between the illustrative surface temperature and the dew point. No certification or fungal-reservoir prevention was measured; earlier wording is withdrawn in REV 1.4.',
                'opus': 'Cross-model check of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B); the earlier word "verified" is withdrawn in REV 1.4 because nothing was measured. Arithmetic reviewed: horizontal thrust H = '
                        '216.0 kN, kern safety factor SF = 9.38, and f_Rsi >= 0.70 condensation protection.'},
               {'edition': 'REV 1.2',
                'date': '2026-11-01',
                'summary': 'REV 1.2 (Redated 2026-11-01): Added dynamic Maxwell-Cremona Reciprocal Force Dual SVG and '
                           'CSI 05 12 00 / 07 21 00 UHPC thermal-break plate.',
                'opus': 'Cross-model check of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B); the earlier word "verified" is withdrawn in REV 1.4 because nothing was measured. Arithmetic reviewed: H = 216.0 kN, SF = 9.38, '
                        'and f_Rsi ≥ 0.70 condensation margin.'},
               {'edition': 'REV 1.1',
                'date': '2026-10-27',
                'summary': 'REV 1.1 (Redated 2026-10-27): Coupled 1:50 vault section to 1:5 EN ISO 13788 Glaser '
                           'dew-point loupe.',
                'opus': 'Cross-model check of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B); the earlier word "verified" is withdrawn in REV 1.4 because nothing was measured. Arithmetic reviewed: T_si = 16.4 °C > T_dew = '
                        '9.3 °C at 20 °C / 50% RH.'},
               {'edition': 'REV 1.0',
                'date': '2026-10-20',
                'summary': 'REV 1.0 (Published 2026-10-20): Initial 1:50 funicular catenary vault form diagram.',
                'opus': 'Cross-model check of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B); the earlier word "verified" is withdrawn in REV 1.4 because nothing was measured. Arithmetic reviewed: middle-third kern '
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
 'history_lead': "In the 1670s, Robert Hooke printed a Latin anagram at the end of A Description of Helioscopes. Its solution was published after his death in 1705: an inverted flexible hanging line gives the shape of a standing rigid arch. A hanging chain carries its weight in pure tension; invert that curve in stone, and the blocks carry weight in pure compression. This folio explains that idea with a teaching model. It is an explanation, not a design method, and none of its numbers may be used on a real structure.",
 'history_body': "Two centuries after Hooke, James Clerk Maxwell published On reciprocal figures and diagrams of forces (1864, DOI 10.1080/14786446408643663), pairing a drawing of a structure's form with a diagram of its forces. In 1966, Jacques Heyman applied plastic limit analysis in The Stone Skeleton (DOI 10.1016/0020-7683(66)90018-7). He later expanded the paper into a book (DOI 10.1017/CBO9781107050310). Assuming masonry has no tensile strength, effectively unlimited compressive strength, and does not slide, a vault is safe if an equilibrium thrust line lies wholly inside the stone. Three-dimensional graphic statics extends these methods to shells (Akbarzadeh, Van Mele, and Block 2015, DOI 10.1016/j.cad.2015.01.006). Open libraries such as compas-dev/compas (https://github.com/compas-dev/compas) build on this framework. This folio does not run those tools; its numbers come from the two formulas shown.",
 'pullquote': 'As hangs the flexible line, so but inverted will stand the rigid arch.',
 'pullquote_cite': 'Robert Hooke, anagram printed in A Description of Helioscopes (1670s); solution published 1705 (English translation of the Latin)',
 'chronology': [('1675',
                 'Robert Hooke',
                 'States, as an anagram, that a hanging chain turned upside down gives the shape of a standing arch; the solution is published in 1705.'),
                ('1864',
                 'James Clerk Maxwell',
                 "Publishes 'On reciprocal figures and diagrams of forces' (DOI 10.1080/14786446408643663)."),
                ('1966',
                 'Jacques Heyman',
                 "Publishes 'The Stone Skeleton' (DOI 10.1016/0020-7683(66)90018-7), applying the safe theorem of plastic theory to masonry: a thrust line within the masonry is enough."),
                ('2026',
                 'Informatico.ai Folio A.01',
                 'Pairs an interactive thrust-line diagram with an illustrative thermal-bridge node. A teaching model, not a design check.')],
 'intuition_lead': 'Why can an unreinforced stone vault stand for centuries, yet fail if its abutments spread? Masonry is strong in compression, has almost no tensile strength, and resists sliding by friction. Jacques Heyman argued that stability depends on geometry rather than crushing strength (The Stone Skeleton, DOI 10.1017/CBO9781107050310). While thrust stays inside the middle third (|e| <= t/6, within 100 millimeters of the center of a 600-millimeter vault), the whole joint stays compressed. Beyond t/6, the far edge begins to open because dry joints cannot pull. A hinge forms when the thrust line reaches the edge (|e| = t/2), and four hinges make a mechanism. The folio therefore reports a geometric factor SF = t/(2|e|): 3 at the middle-third limit, 1 at the edge. The thermal node is a separate, simpler model: it compares an assumed inside surface temperature with the room air dew point using ISO 13788 definitions. Nothing here was computed in compas-dev/compas (https://github.com/compas-dev/compas). It is named only as a tool a reader could use for three-dimensional graphic statics (DOI 10.1016/j.cad.2015.01.006).',
 'intuition_body': 'As long as the resultant compressive force acts within the middle third of the cross-section '
                   '(eccentricity |e| <= t/6, or +/-100 mm inside a 600 mm vault), the entire thickness remains in '
                   'compression. When |e| exceeds t/6, the opposite face tries to go into tension; because dry '
                   'joints cannot pull, the joint starts to open there. A full hinge forms once the thrust line reaches the edge, and four hinges turn the arch into a collapse mechanism. Meanwhile, at the 1:5 abutment support where that 216 kN horizontal thrust '
                   'meets the foundation, the folio assumes a load-bearing thermal break that keeps the interior surface at 16.4 °C, which is 7.1 °C above the 9.3 °C dew point of room air at 20 °C and 50% relative humidity. The surface temperature is an illustrative value: the outdoor temperature and the node geometry that would produce it are not stated, and no ISO 10211 calculation was run.',
 'walkthrough': ['Experiment 1 (Scrub Crown Rise & Watch the Maxwell-Cremona Force Dual): Drag the Crown Rise slider '
                 '(f) between 2.5 m and 6.5 m. Watch both the 1:50 arch profile and the reciprocal pole O in the '
                 'Maxwell-Cremona force polygon shift live as horizontal thrust H = qL^2/(8f) changes.',
                 'Experiment 2 (Push Eccentricity Past the Middle-Third Kern): Drag the Asymmetric Live-Load '
                 'Eccentricity slider past 100 mm (t/6). Watch the readout change once the thrust line leaves the middle third; in the model this is where a joint would start to open.',
                 'Experiment 3 (Switch Between 1:50 Macro & 1:5 Nodal Scales): Click Stages 1 -> 4 in the stepper '
                 'above to inspect the Glaser vapor-pressure profile and CSI 07 27 00 thermal-break assembly.'],
 'human_ai_shift': 'Finite-element software often shows force flow only as color maps. Graphic statics gives a direct link: change the geometry and the force diagram updates with it. A designer, with or without an AI assistant, could use tools such as compas-dev/compas (https://github.com/compas-dev/compas). That library draws on three-dimensional graphic statics (DOI 10.1016/j.cad.2015.01.006). Pairing geometry with a thermal model in FEniCS/dolfinx (DOI 10.1145/3524456) could compare shell shapes. The goal is keeping the geometric factor at 3 or more while inside surfaces stay above the dew point. This is a workflow proposal; the folio did not run these tools.',
 'sources': ['Hooke, R. (1676). A Description of Helioscopes, and Some Other Instruments. London. (Contains the arch anagram; the solution was published in 1705.)',
             'Maxwell, J. C. (1864). On reciprocal figures and diagrams of forces. Philosophical Magazine, 27(182), '
             '250–261. DOI: 10.1080/14786446408643663.',
             'Heyman, J. (1966). The stone skeleton. International Journal of Solids and Structures, 2(2), 249–279. DOI: 10.1016/0020-7683(66)90018-7.',
             'Heyman, J. (1995). The Stone Skeleton: Structural Engineering of Masonry Architecture. Cambridge '
             'University Press. DOI: 10.1017/CBO9781107050310.',
             'ISO 13788 (2012). Hygrothermal performance of building components and building elements — Internal surface temperature to avoid critical surface humidity and interstitial condensation — Calculation methods.',
             'ISO 10211 (2017). Thermal bridges in building construction — Heat flows and surface temperatures — Detailed calculations.',
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
 'act1_dropcap': "In the 1670s, Robert Hooke printed a Latin anagram at the end of A Description of Helioscopes. Its solution was published after his death in 1705: an inverted flexible hanging line gives the shape of a standing rigid arch. A hanging chain carries its weight in pure tension; invert that curve in stone, and the blocks carry weight in pure compression. This folio explains that idea with a teaching model. It is an explanation, not a design method, and none of its numbers may be used on a real structure.",
 'act1_plain_bridge': 'To picture how an arch stands, lean two heavy hardback books together on a smooth wooden '
                      'table. When they lean steeply, their tops press tightly together and hold. Spread their bottoms '
                      'too far apart, and the outward push slides both books flat. Stone and brick resist squeezing '
                      'well, yet they cannot handle being pulled apart. Without steel ties, the line of squeezing '
                      'force must stay inside the middle third of each block so the whole joint stays compressed. If '
                      'that line drifts past the middle third, the far face begins to open. A full hinge forms only '
                      'when thrust reaches the outer edge, and four hinges allow the arch to fold. The folio also '
                      'models one cold spot at the base of the wall: if an inside surface is colder than the room '
                      'dew point, moisture can condense on it.',
 'act1_body': "Two centuries after Hooke, James Clerk Maxwell published On reciprocal figures and diagrams of forces (1864, DOI 10.1080/14786446408643663), pairing a drawing of a structure's form with a diagram of its forces. In 1966, Jacques Heyman applied plastic limit analysis in The Stone Skeleton (DOI 10.1016/0020-7683(66)90018-7). He later expanded the paper into a book (DOI 10.1017/CBO9781107050310). Assuming masonry has no tensile strength, effectively unlimited compressive strength, and does not slide, a vault is safe if an equilibrium thrust line lies wholly inside the stone. Three-dimensional graphic statics extends these methods to shells (Akbarzadeh, Van Mele, and Block 2015, DOI 10.1016/j.cad.2015.01.006). Open libraries such as compas-dev/compas (https://github.com/compas-dev/compas) build on this framework. This folio does not run those tools; its numbers come from the two formulas shown.",
 'act1_stakes': 'Empirical rules of thumb assume fixed geometry and steady boundary conditions. If abutments '
                'spread or uneven loads push the thrust line outside the middle third, dry joints begin to open. A '
                'hinge forms only when thrust reaches the masonry edge (|e| = t/2), and four hinges make a collapse '
                'mechanism (Heyman, DOI 10.1017/CBO9781107050310). At the foundation node, an uninsulated abutment '
                'bridging warm indoor air to cold stone can cool the inside surface below the dew point (ISO 13788).',
 'act2_analogy': 'Carry a heavy grocery bag pressed tight against your chest, and gravity passes straight down your '
                 "spine in compression. Hold it at arm's length, and your lower back pulls in tension. Dry stone vaults "
                 'allow modest off-center loads while thrust stays inside the middle third. Push the load past that '
                 'boundary, and the far face tries to pull in tension that mortarless joints cannot supply.',
 'act2_plain_primer': 'In the interactive laboratory below, two sliders test how the vault model responds to '
                      'geometry and uneven load. The first slider sets the crown rise of the arch relative to its '
                      'span. Flattening the arch increases the outward horizontal thrust pushed against the side '
                      'abutments, while raising the crown directs the weight more steeply downward. The second slider '
                      'adds live-load eccentricity, representing an uneven load such as snow piled on one side of '
                      'the roof. Moving that slider shifts the thrust line away from the center of the blocks; past '
                      'the middle-third boundary, the model marks where a joint starts to open.',
 'distill_diagram': {'analogy_title': 'Weight Pressed Against Spine vs Arms',
                     'analogy_sub': 'Centered loads compress; off-center loads create dangerous tension',
                     'force_a_title': 'Vault Crown Rise (f)',
                     'force_a_sub': 'Taller rise reduces outward horizontal thrust against abutments',
                     'force_b_title': 'Thrust Eccentricity (e)',
                     'force_b_sub': 'Asymmetric snow shifts the internal force path toward the face',
                     'threshold_title': 'Middle-Third Kern Boundary (|e| <= t/6)',
                     'threshold_pass': 'Model: whole joint in compression (geometric factor 3 or more)',
                     'threshold_fail': 'Model: joint starts to open; a hinge forms only if thrust reaches the edge'},
 'act2_intuition': 'Why can an unreinforced stone vault stand for centuries, yet fail if its abutments spread? Masonry is strong in compression, has almost no tensile strength, and resists sliding by friction. Jacques Heyman argued that stability depends on geometry rather than crushing strength (The Stone Skeleton, DOI 10.1017/CBO9781107050310). While thrust stays inside the middle third (|e| <= t/6, within 100 millimeters of the center of a 600-millimeter vault), the whole joint stays compressed. Beyond t/6, the far edge begins to open because dry joints cannot pull. A hinge forms when the thrust line reaches the edge (|e| = t/2), and four hinges make a mechanism. The folio therefore reports a geometric factor SF = t/(2|e|): 3 at the middle-third limit, 1 at the edge. The thermal node is a separate, simpler model: it compares an assumed inside surface temperature with the room air dew point using ISO 13788 definitions. Nothing here was computed in compas-dev/compas (https://github.com/compas-dev/compas). It is named only as a tool a reader could use for three-dimensional graphic statics (DOI 10.1016/j.cad.2015.01.006).',
 'act2_deepening': 'Horizontal thrust at the vault springers scales inversely with crown rise: halving the arch '
                   'height doubles the outward thrust on the abutments. In this simplified model, however, horizontal '
                   'thrust H depends only on crown rise f. Eccentricity e sets SF independently, and the 1:5 thermal '
                   'node uses a fixed illustrative value. Physically, asymmetric live loads shift the funicular line '
                   'toward the extrados at the quarter-span. If an abutment spreads outward, the crown drops and pushes '
                   'the thrust line toward the intrados. At the 1:5 abutment node, compressive thrust must pass through '
                   'a load-bearing thermal break. Ordinary insulation crushes under high thrust. The folio assumes a '
                   'load-bearing pad as a model assumption, not a tested product. It is meant to carry thrust while '
                   'keeping the inside surface above the dew point.',
 'act4_deepening': 'What follows is a proposal, not a description of current practice. Rather than running '
                   'finite-element analysis only as a late check, a generative workflow could enforce the middle-third '
                   'rule directly during shape search. The designer would guide proportions, daylight, and civic '
                   'expression while software computes reciprocal Maxwell-Cremona diagrams across candidate shapes '
                   'and filters out forms requiring oversized abutments. At the small scale, ISO 10211 and ISO 13788 '
                   'methods could evaluate cold-spot temperatures for 1:5 nodes to reduce condensation risk. Separate '
                   'checks would address structural bearing stiffness.',
 'act4_human_ai': 'Finite-element software often shows force flow only as color maps. Graphic statics gives a direct link: change the geometry and the force diagram updates with it. A designer, with or without an AI assistant, could use tools such as compas-dev/compas (https://github.com/compas-dev/compas). That library draws on three-dimensional graphic statics (DOI 10.1016/j.cad.2015.01.006). Pairing geometry with a thermal model in FEniCS/dolfinx (DOI 10.1145/3524456) could compare shell shapes. The goal is keeping the geometric factor at 3 or more while inside surfaces stay above the dew point. This is a workflow proposal; the folio did not run these tools.'}

PLATE_CAPTION = {'alt': "Conceptual visualization imagining what a hanging chain catenary model paired with a stone "
        'masonry funicular vault would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.01-V (Imagining What It Would Look Like) · Artistic architectural cutaway '
            "imagining an inverted catenary hanging-chain model suspended beneath an unreinforced "
            'limestone ashlar funicular vault.'}

DISPATCH = {'kicker': 'FRONTIER TECTONIC DISPATCH · THRUST NETWORK ANALYSIS (TNA)',
 'headline': "3D Graphic Statics & Thrust Network Analysis Extend Heyman's Safe Theorem to Freeform Vaults",
 'body': "Jacques Heyman's safe theorem for masonry (DOI 10.1017/CBO9781107050310) says a vault stands if a thrust line can be found inside the stone. Three-dimensional graphic statics (Akbarzadeh, Van Mele and Block 2015, DOI 10.1016/j.cad.2015.01.006) extends the form-and-force diagrams of the nineteenth century to freeform shells. This folio shows the two-dimensional version as a teaching model."}

META_3D = ('Heyman Biaxial Catenary Masonry Groin Vault',
 'X: Vault Span L (18 m) · Z: Transverse Bay · Y: Inverted Funicular Thrust Line & Kern Envelope')

ES_TRANSLATION = {'title_es': 'Superficies Foniculares de Empuje, Duales de Maxwell–Cremona y Tectónica Nodal 1:5',
 'subtitle_es': 'Cómo una bóveda de piedra a compresión pura se sostiene cuando su línea de empuje queda dentro de la mampostería (teorema de seguridad de Heyman), revisada aquí con la regla clásica, más estricta, del tercio medio (|e| ≤ t/6), junto con un nodo de arranque ilustrativo a escala 1:5 cuya superficie interior se modela por encima del punto de rocío.',
 'why_es': 'Una cadena colgante adopta por gravedad una forma de tracción pura; al invertirla como un arco de '
           'piedra (catenaria invertida de Hooke), toda la estructura trabaja en compresión pura sin doblarse.',
 'plain_es': 'Para imaginar cómo se sostiene una bóveda de piedra, apoyen dos libros gruesos uno contra otro sobre '
             'una mesa lisa. Si se inclinan con suficiente altura, sus bordes superiores se presionan con firmeza y '
             'se mantienen en pie. Si separan las bases de más, el empuje hacia afuera los hace resbalar y caer. '
             'La piedra y el ladrillo resisten bien la compresión, pero no soportan que los estiren. Sin tirantes de '
             'acero, la línea de compresión debe quedar en el tercio central de cada bloque para mantener toda la '
             'junta comprimida. Si sale del tercio medio, la cara opuesta empieza a abrirse. Una rótula se forma '
             'solo al llegar al borde exterior, y cuatro rótulas permiten que el arco se pliegue. El folio también '
             'modela un punto frío en la base del muro: si una superficie interior está más fría que el punto de '
             'rocío del cuarto, la humedad puede condensarse sobre ella. Este folio es una explicación, no un método '
             'de diseño, y ninguno de sus números debe usarse en una estructura real.',
 'deep_es': 'El equilibrio de la bóveda acopla la altura del arco en la clave con la excentricidad de las cargas '
            'asimétricas. Un arco más tendido genera mayor empuje horizontal en los estribos. Elevar la flecha '
            'dirige el peso de forma más vertical hacia los cimientos. El teorema de seguridad de Heyman indica que la '
            'bóveda es estable si existe una línea de empuje en equilibrio dentro de la mampostería. La regla del '
            'tercio medio, más estricta, mantiene toda la junta en compresión y es la meta de diseño de este folio. '
            'Cuando una carga asimétrica desplaza la línea fuera del tercio medio, la junta empieza a abrirse. Si '
            'llega al borde se forma una rótula, y cuatro rótulas forman un mecanismo. El nodo térmico del apoyo es '
            'un modelo ilustrativo: supone un elemento portante de baja conductividad y una temperatura superficial '
            'interior por encima del punto de rocío. Nada de esto fue medido ni calculado con programas '
            'especializados.'}
