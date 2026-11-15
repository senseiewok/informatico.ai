#!/usr/bin/env python3
"""Folio A.02 (ARCHITECTURE): Reciprocal Timber Gridshells (Nexorades), Eccentric Lap Moments, and 1:5 Shear-Block Joinery."""
from __future__ import annotations

SLUG = 'a02'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.02',
 'slug': 'a02',
 'pillar': 'architecture',
 'category_code': 'A',
 'title': 'Reciprocal Timber Gridshells (Nexorades), Eccentric Lap Moments, and 1:5 Shear-Block Joinery',
 'subtitle': 'Structural kinematics of bolt-free reciprocal timber frames where each beam rests on its neighbor with '
             'engagement eccentricity e_z, converting global shell thrust into localized bending.',
 'date_published': '2026-10-25',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.3',
 'status_badge': 'REDATED REV 1.3',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'M_lap = V_lap a (1 − λ) · τ_d ≤ k_v f_{v,d}',
 'colophon': {'identifier': 'A.02 · Reciprocal Timber Gridshells',
              'kernels': '1:50 Nexorade Bay + 1:5 Notched Lap Joint',
              'benchmarks': 'Model values: M_lap = 5.15 kN·m (a = 0.373 m, λ = 0.25) · utilization 0.64 and SF 3.74 are illustrative',
              'bridge': 'Reciprocal Load Sharing ↔ CFTR NBD Dimer (a visual analogy only)'},
 'steps': ['Stage 1 (4-Valence Reciprocal Fan): Four GL28h larch members interlock in a pinwheel cyclic dependency so '
           'no more than two members meet at any single point.',
           'Stage 2 (Eccentricity-Induced Dome Rise): An assumed vertical offset e_z = 85 mm at each lap joint '
           'tilts each member, and repeated around the fan this gives the dome its rise.',
           'Stage 3 (Notch Shear & Bending Check, in the style of EN 1995-1-1): With V_lap = 18.4 kN, λ = 0.25 and an '
           'assumed member length L = 1.493 m (so a = λL = 0.373 m), M_lap = 18.4 × 0.373 × 0.75 = 5.15 kN·m. The '
           'notch utilization 0.64 is a fixed illustrative value, not a full design check.',
           'Stage 4 (1:5 CNC Dovetail Shear-Block Node): A proposed node in which hardwood beech dowels and EPDM gaskets '
           'carry shear without exposed steel plates (design proposal, not tested).'],
 'readouts': [{'label': 'Joint Shear Force (V_lap)', 'value': '18.4 kN'},
              {'label': 'Induced Bending Moment (Model)', 'value': '5.15 kN·m'},
              {'label': 'Notch Utilization (Illustrative)', 'value': '0.64 ≤ 1.00 (model)'},
              {'label': 'Buckling Factor (Illustrative)', 'value': 'SF = 3.74 (model value)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 06 18 00 / 06 13 23',
                'title': 'GL28h Larch Reciprocal Gridshell Member & Beech Shear-Key Kit (Node A-08)',
                'body': '5-axis CNC-milled glued laminated larch timber with pre-compressed beechwood shear keys and '
                        'concealed self-tapping full-thread reinforcement screws (f_{m,k} = 28 MPa, f_{v,k} = 3.5 '
                        'MPa).',
                'meta': 'Design proposal, not a product · EN 14080 is the glued-laminated timber product standard such members would need to meet'},
 'sidenote_1': {'kicker': 'SIDENOTE A.02 · VILLARD DE HONNECOURT TO KAGAWA',
                'body': 'Reciprocal frames let members shorter than the span cover it together (Popovic Larsen 2007, DOI '
                        '10.4324/9780080556000). The price is bending and shear at every notch, which EN 1995-1-1 asks '
                        'designers to check for notched members.'},
 'skill': {'filename': 'reciprocal-timber-nexorade-SKILL.md',
           'name': 'reciprocal-timber-nexorade',
           'description': 'AI-agnostic structural timber engineering skill for reciprocal gridshells (nexorades), '
                          'engagement ratio kinematics, and Eurocode 5 notched lap joint verification.',
           'rules': ['Compute reciprocal lap bending moment M_lap = V_lap * a * (1 - lambda_lap) for engagement ratio '
                     'lambda_lap = a / L.',
                     'Verify Eurocode 5 notched joint shear utilization tau_d / (k_v * f_{v,d}) <= 1.0 using effective '
                     'depth h_eff.',
                     'Provide full-thread self-tapping screw reinforcement perpendicular to grain where tension '
                     'splitting stress exceeds f_{t,90,d}.']},
 'revisions': [{'edition': 'REV 1.3',
                'date': '2026-11-14',
                'summary': 'REV 1.3 (Redated 2026-11-14): Grounding revision. The model does not prove gridshells safe; '
                           'earlier SAFE / PASS claims, buckling claims from COMPAS, '
                           'and an unsourced 60% embodied carbon reduction claim are withdrawn; '
                           'the utilization 0.64 and SF 3.74 are now labelled illustrative values. The bending moment '
                           'now states its assumed member length (L = 1.493 m), the invented Song and Leonardo scenes '
                           'are replaced by a plain account, and the CF section no longer makes health claims.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; Scite search found no '
                        'source for the 4x-6x span claim, so it was removed.'},
               {'edition': 'REV 1.2',
                'date': '2026-11-02',
                'summary': 'REV 1.2 (Redated 2026-11-02): Added a notched lap joint shear utilization and a gridshell '
                           'buckling factor SF = 3.74, with the portable reciprocal-timber-nexorade skill.',
                'opus': 'Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'wording is withdrawn in REV 1.3: nothing was built, tested or checked against EN 1995-1-1.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-01',
                'summary': 'REV 1.1 (Redated 2026-11-01): Added CSI 06 18 00 CNC glulam specification plate and '
                           'perpendicular-to-grain splitting reinforcement check.',
                'opus': 'Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'wording for k_v = 0.78 and utilization 0.64 is withdrawn in REV 1.3: these are illustrative values.'},
               {'edition': 'REV 1.0',
                'date': '2026-10-25',
                'summary': 'REV 1.0 (Published 2026-10-25): Initial publication of reciprocal nexorade kinematics and '
                           '1:5 CNC lap joinery.',
                'opus': 'Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'wording is withdrawn in REV 1.3.'}],
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/j.jobe.2019.100867',
           'fetched_on': '2026-11-08',
           'citing_publications': 19,
           'supporting': 0,
           'mentioning': 8,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Asefi & Bahremandi-Tolou, Design challenges of reciprocal frame structures in architecture (DOI 10.1016/j.jobe.2019.100867), checked 2026-11-08: 19 citing publications (0 supporting, 8 mentioning, 0 contrasting) and no retraction notice. The paper reviews reciprocal frame design; it does not check this folio\'s numbers.'},
 'volume': 1,
 'volume_code': 'VOL. 01',
 'sliders': [{'label': 'Reciprocal Engagement Ratio (λ = a / L)',
              'min': 0.15,
              'max': 0.45,
              'step': 0.01,
              'value': 0.25,
              'unit': 'λ = '},
             {'label': 'Notched Lap Shear Force (V_lap)',
              'min': 8.0,
              'max': 32.0,
              'step': 0.4,
              'value': 18.4,
              'unit': ' kN'}]}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'history_lead': 'In Northern Song China, timber "rainbow bridges" crossed the Bian River at Kaifeng as woven arches '
                 'of short logs, with no piers standing in the water; one appears in the twelfth-century scroll Along '
                 'the River During the Qingming Festival. Each log rests on its neighbors, so pieces shorter than the '
                 'span carry the span together. Leonardo da Vinci later drew similar self-supporting arrangements of '
                 'short poles in the sketches now collected in the Codex Atlanticus. Structures of this kind, in '
                 'which members support one another in a closed loop, are now called reciprocal frames (Popovic '
                 'Larsen 2007, DOI 10.4324/9780080556000).',
 'history_body': "From Leonardo da Vinci's sketches in the Codex Atlanticus to Villard de Honnecourt's medieval floor grillages and contemporary timber pavilions, reciprocal frames assemble short members into closed polygonal fans. In her book Reciprocal Frame Architecture (DOI 10.4324/9780080556000), Olga Popovic Larsen describes how in these systems each member rests on the next, so no single node gathers many members. Asefi and Bahremandi-Tolou review the design challenges of such frames in architecture (Journal of Building Engineering, DOI 10.1016/j.jobe.2019.100867). Designers today could pair form-finding tools such as compas-dev/compas (https://github.com/compas-dev/compas; see DOI 10.1016/j.cad.2015.01.006 for the underlying three-dimensional graphic statics) with timber connection rules from EN 1995-1-1. This folio does not run those tools, and it makes no embodied-carbon claim; its numbers come from the lap-moment formula shown.",
 'pullquote': 'A reciprocal timber frame replaces the congested multi-axis steel node with a woven rhythm of short, '
              'lap-jointed beams—where every member both supports its neighbor and is supported in return.',
 'pullquote_cite': "Editorial Synthesis · From the Song Dynasty Rainbow Bridges & Da Vinci's Codex Atlanticus to "
                   'Modern Timber Gridshells',
 'chronology': [('11th–12th c.',
                 'Northern Song Builders',
                 'Woven timber rainbow bridges (hongqiao) cross the Bian River at Kaifeng without piers in the water.'),
                ('c. 1480s–1510s',
                 'Leonardo da Vinci',
                 'Sketches self-supporting arrangements of short poles, later collected in the Codex Atlanticus.'),
                ('1975',
                 'Frei Otto & Ted Happold',
                 'Erect the Mannheim Multihalle timber gridshell by lifting a flat hemlock lath lattice into a '
                 'funicular shell.'),
                ('2010',
                 'Shigeru Ban & Hermann Blumer',
                 'Translate triaxial woven bamboo geometry into CNC-milled hexagonal/triangular glulam shell ribs at '
                 'Metz.'),
                ('2026',
                 'Informatico.ai Folio A.02',
                 'A teaching model of the reciprocal lap moment, with an illustrative buckling factor (SF = 3.74) and '
                 'an assumed joint stiffness.')],
 'intuition_lead': 'When gravity loads act on a curved reciprocal timber gridshell, the system transfers force through '
                   'membrane compression along its diagonal lattice ribs. However, what threatens slender timber '
                   'shells is not compressive crushing, but local joint splitting and global elastic buckling. The '
                   'vertical offset e_z at each lap joint inherently produces an eccentric bending moment M_lap = '
                   'V_lap * a * (1 - lambda_lap); this is the folio\'s simplified lever model of the lap (see Popovic Larsen, DOI '
                   '10.4324/9780080556000, and Asefi and Bahremandi-Tolou, DOI 10.1016/j.jobe.2019.100867, for '
                   'reciprocal frame behaviour in general). With V_lap = 18.4 kN, lambda = 0.25 and an assumed member '
                   'length of 1.493 m, the lap arm is a = 0.373 m and M_lap = 5.15 kN·m. EN 1995-1-1 includes a shear '
                   'check for notched members, tau_d <= k_v * f_{v,d}, and splitting at the re-entrant corner of a notch '
                   'is a known weakness that designers often address with fully threaded self-tapping screws. The '
                   'utilization of 0.64 and the elastic buckling factor of 3.74 shown here are illustrative values, not '
                   'the result of a full analysis; a real gridshell would need a complete design check by a qualified '
                   'engineer.',
 'intuition_body': 'In an Euler buckling estimate the critical load N_cr = pi^2 E I_eff / (k L_trib)^2 depends on the '
                   'rotational stiffness K_phi of the lap joints. This folio assumes K_phi = 142 kN·m/rad for a screwed '
                   'lap joint; that value is an assumption, not taken from a test or from EN 1995-1-1. With an '
                   'illustrative N_cr = 1,280 kN against a design force N_d = 342 kN, the ratio is 1,280 / 342 = 3.74. '
                   'These are teaching values; the folio makes no claim about embodied carbon.',
 'walkthrough': ['Experiment 1 (Step Through the 4 Stages): Click Stages 1 -> 4 above to follow the reciprocal fan, '
                 'the eccentricity e_z, the lap-moment and notch check, and the proposed CNC node.',
                 'Experiment 2 (Inspect the Reciprocal Nexorade Node): Examine the SVG diagram below showing how four '
                 'beams weave around the central opening with offset eccentricity e_z.',
                 'Experiment 3 (Read the Companion Skill): Download the reciprocal-timber-nexorade SKILL.md below; it '
                 'lists the lap-moment formula, the notch shear ratio and the screw-reinforcement rule used here. It is a '
                 'study aid, not a design code.'],
 'human_ai_shift': "Reciprocal frames are hard to design by hand because changing one beam's angle changes the "
                   'elevation of every neighboring beam. A designer, with or without an AI assistant, could pair '
                   'parametric geometry from a tool such as compas-dev/compas (https://github.com/compas-dev/compas; '
                   'see DOI 10.1016/j.cad.2015.01.006 for the underlying graphic statics) with a finite-element library '
                   'such as FEniCS/dolfinx (DOI 10.1145/3524456) to explore these weaves and prepare cutting data. This '
                   'folio names those tools as options a reader could use; it did not run them.',
 'cf_bridge': 'This bridge is an analogy, and a loose one. In a reciprocal frame each member holds up the next. In the '
              'CFTR protein, the two nucleotide-binding domains come together as a pair around ATP, and published '
              'structures show the F508del protein bound to the elexacaftor, tezacaftor and ivacaftor combination '
              '(for example PDB entry 8EIQ). The folio makes no claim about indoor air, materials or health in CF '
              'clinics, and it is not medical advice.',
 'sources': ['Leonardo da Vinci (c. 1478–1519). Codex Atlanticus. Biblioteca Ambrosiana, Milan.',
             'Otto, F., & Hennicke, J. (1974). IL 10: Gitterschalen / Grid Shells. Institute for Lightweight '
             'Structures, Stuttgart.',
             'Popovic Larsen, O. (2007). Reciprocal Frame Architecture. Architectural Press / Routledge. DOI: '
             '10.4324/9780080556000.',
             'Asefi, M., & Bahremandi-Tolou, M. (2019). Design challenges of reciprocal frame structures in '
             'architecture. Journal of Building Engineering, 26, 100867. DOI: 10.1016/j.jobe.2019.100867.',
             'CEN (2004). EN 1995-1-1, Eurocode 5: Design of timber structures — Part 1-1: General — Common rules and '
             'rules for buildings.',
             'Akbarzadeh, M., Van Mele, T., & Block, P. (2015). On the equilibrium of funicular polyhedral frames and '
             'convex polyhedral force diagrams. Computer-Aided Design, 63, 118–128. DOI: 10.1016/j.cad.2015.01.006. '
             '(Cited for graphic statics; compas-dev/compas, https://github.com/compas-dev/compas, is a separate '
             'open-source framework.)',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order '
             'Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (FEniCS/dolfinx, '
             'https://github.com/FEniCS/dolfinx). ACM Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: '
             '10.1145/3524456.',
             'RCSB Protein Data Bank entry 8EIQ: phosphorylated human delta F508 CFTR in complex with elexacaftor, '
             'tezacaftor, ivacaftor and ATP/Mg. https://www.rcsb.org/structure/8EIQ'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Reciprocal 4-beam nexorade weave and '
        'Euler buckling margin">\n'
        '            <g transform="translate(70, 20)">\n'
        '              <line x1="20" y1="50" x2="210" y2="50" stroke="var(--tp-prussian)" stroke-width="10"/>\n'
        '              <line x1="170" y1="15" x2="170" y2="175" stroke="var(--tp-minium)" stroke-width="10"/>\n'
        '              <line x1="230" y1="135" x2="40" y2="135" stroke="var(--tp-prussian)" stroke-width="10"/>\n'
        '              <line x1="80" y1="175" x2="80" y2="15" stroke="var(--tp-verdigris)" stroke-width="10"/>\n'
        '              <circle cx="170" cy="50" r="5" fill="var(--tp-vellum)"/><circle cx="170" cy="135" r="5" '
        'fill="var(--tp-vellum)"/>\n'
        '              <circle cx="80" cy="135" r="5" fill="var(--tp-vellum)"/><circle cx="80" cy="50" r="5" '
        'fill="var(--tp-vellum)"/>\n'
        '            </g>\n'
        '            <text x="65" y="208" font-size="11" fill="currentColor">1:5 Reciprocal 4-Beam Lap Weave (K_φ = '
        '142 kN·m/rad)</text>\n'
        '            <rect x="380" y="45" width="250" height="135" fill="none" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <rect x="415" y="135" width="65" height="32" fill="var(--tp-prussian)"/>\n'
        '            <rect x="525" y="65" width="65" height="102" fill="var(--tp-verdigris)"/>\n'
        '            <text x="405" y="128" font-size="11" fill="var(--tp-prussian)">Demand: 342 kN</text>\n'
        '            <text x="510" y="57" font-size="11" fill="var(--tp-verdigris)">N_cr: 1,280 kN (SF 3.74)</text>\n'
        '          </svg>',
 'scite': {'doi': '10.1016/j.jobe.2019.100867',
           'fetched_on': '2026-11-08',
           'citing_publications': 19,
           'supporting': 0,
           'mentioning': 8,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Asefi & Bahremandi-Tolou, Design challenges of reciprocal frame structures in architecture (DOI 10.1016/j.jobe.2019.100867), checked 2026-11-08: 19 citing publications (0 supporting, 8 mentioning, 0 contrasting) and no retraction notice. The paper reviews reciprocal frame design; it does not check this folio\'s numbers.'},
 'word_count': '4,650 WORDS',
 'act1_dropcap': 'In Northern Song China, timber "rainbow bridges" crossed the Bian River at Kaifeng as woven arches '
                 'of short logs, with no piers standing in the water; one appears in the twelfth-century scroll Along '
                 'the River During the Qingming Festival. Each log rests on its neighbors, so pieces shorter than the '
                 'span carry the span together. Leonardo da Vinci later drew similar self-supporting arrangements of '
                 'short poles in the sketches now collected in the Codex Atlanticus. Structures of this kind, in '
                 'which members support one another in a closed loop, are now called reciprocal frames (Popovic '
                 'Larsen 2007, DOI 10.4324/9780080556000).',
 'act1_plain_bridge': 'To see how a reciprocal timber frame works, take four wooden butter knives and place them over '
                      'the rim of an open coffee mug. If you weave them in a pinwheel pattern so that the tip of each '
                      'knife rests on the blade of the next one, the knives lock together firmly over the center. You '
                      'can press your thumb down on the middle of that weave and it will not fall into the cup. No '
                      'single knife is long enough to span the whole rim on its own, but working together, they form a '
                      'self-supporting bridge. In modern timber architecture, builders use this exact interlocking '
                      'trick to cover massive halls using short, sustainable boards instead of gigantic old-growth '
                      'tree trunks. Because the pieces lean on one another at simple notches, the roof carries heavy '
                      'snow loads while using light, locally harvested wood.',
 'act1_body': "From Leonardo da Vinci's sketches in the Codex Atlanticus to Villard de Honnecourt's medieval floor grillages and contemporary timber pavilions, reciprocal frames assemble short members into closed polygonal fans. In her book Reciprocal Frame Architecture (DOI 10.4324/9780080556000), Olga Popovic Larsen describes how in these systems each member rests on the next, so no single node gathers many members. Asefi and Bahremandi-Tolou review the design challenges of such frames in architecture (Journal of Building Engineering, DOI 10.1016/j.jobe.2019.100867). Designers today could pair form-finding tools such as compas-dev/compas (https://github.com/compas-dev/compas; see DOI 10.1016/j.cad.2015.01.006 for the underlying three-dimensional graphic statics) with timber connection rules from EN 1995-1-1. This folio does not run those tools, and it makes no embodied-carbon claim; its numbers come from the lap-moment formula shown.",
 'act1_stakes': 'Traditional carpentry depended on complex mortise-and-tenon joints secured with dry wooden pegs, but '
                'sizing reciprocal frames purely by eye carries dangerous structural vulnerabilities. Because each '
                'beam rests on its neighbor with an eccentric vertical offset, the axial compression that naturally '
                'stabilizes a dome gets converted into intense localized bending and shear at every notched joint. If '
                'carpenters cut a notch too deep, they sever the long wood fibers that carry tensile bending stress, '
                'concentrating splitting forces perpendicular to the grain. Under the weight of heavy winter snow or '
                'shifting wind gusts, an unreinforced notch can shear cleanly along the grain line. Because the system '
                'is mutually dependent, the failure of a single lap joint triggers an immediate domino effect, '
                'destabilizing adjacent members and causing the entire reciprocal shell to snap downward in '
                'catastrophic elastic buckling. Modern engineers must therefore verify both local notch shear stresses '
                'and global lattice stability simultaneously.',
 'act2_analogy': 'Everyday analogy: Interlock four index fingers in a closed pinwheel loop, where each fingertip '
                 'presses down on the knuckle of the next. Pressing downward in the center makes the circle tighten '
                 'against your palms with surprising rigidity. However, if one knuckle slips sideways or if you press '
                 'too hard near the delicate nail bed, the interlocking grip instantly unravels. Reciprocal timber '
                 'frames balance this exact trade-off: mutual geometric support creates strength, but localized joint '
                 'shearing must be rigorously reinforced.',
 'act2_plain_primer': 'In the digital workshop below, you explore how two architectural sliders govern the stability '
                      'of a reciprocal timber shell. The first slider adjusts the engagement ratio, which dictates how '
                      'far along the length of each beam the neighboring timber rests. When you slide this value '
                      'toward the outer tip, the central open eye of the pinwheel expands into a wide, airy skylight, '
                      'but the bending leverage on each beam increases dramatically. Bringing the joint closer to the '
                      'center stiffens the weave but crowds the wood members together. The second slider controls the '
                      'downward shear force acting at the notched joint, representing the weight of snow, roofing '
                      'tiles, and occupants pressing onto that connection. As this shear force climbs, it tests the '
                      'shear strength of the wooden notch. Balancing these two settings keeps the timber safely within '
                      'its natural structural capacity.',
 'distill_diagram': {'analogy_title': 'Four Interlocked Knives Over Mug Rim',
                     'analogy_sub': 'Mutual lap support spans wide openings with short pieces',
                     'force_a_title': 'Engagement Ratio (λ = a/L)',
                     'force_a_sub': 'Controls central eye radius, dome camber, and beam bending',
                     'force_b_title': 'Lap Shear Force (V_lap)',
                     'force_b_sub': 'Downline roof gravity loading transferred across each notch',
                     'threshold_title': 'Eurocode 5 Notch Shear Limit (τ_d <= k_v f_vd)',
                     'threshold_pass': 'Within the model limit; self-tapping screws help resist splitting',
                     'threshold_fail': 'Grain cleavage at notch re-entrant corner; shell snaps flat'},
 'act2_intuition': 'When gravity loads act on a curved reciprocal timber gridshell, the system transfers force through '
                   'membrane compression along its diagonal lattice ribs. However, what threatens slender timber '
                   'shells is not compressive crushing, but local joint splitting and global elastic buckling. The '
                   'vertical offset e_z at each lap joint inherently produces an eccentric bending moment M_lap = '
                   'V_lap * a * (1 - lambda_lap); this is the folio\'s simplified lever model of the lap (see Popovic Larsen, DOI '
                   '10.4324/9780080556000, and Asefi and Bahremandi-Tolou, DOI 10.1016/j.jobe.2019.100867, for '
                   'reciprocal frame behaviour in general). With V_lap = 18.4 kN, lambda = 0.25 and an assumed member '
                   'length of 1.493 m, the lap arm is a = 0.373 m and M_lap = 5.15 kN·m. EN 1995-1-1 includes a shear '
                   'check for notched members, tau_d <= k_v * f_{v,d}, and splitting at the re-entrant corner of a notch '
                   'is a known weakness that designers often address with fully threaded self-tapping screws. The '
                   'utilization of 0.64 and the elastic buckling factor of 3.74 shown here are illustrative values, not '
                   'the result of a full analysis; a real gridshell would need a complete design check by a qualified '
                   'engineer.',
 'act2_deepening': 'The nonlinear coupling between engagement ratio lambda and lap shear force V_lap dictates the '
                   'overall geometry and safety margin of the gridshell. Increasing the engagement ratio shifts the '
                   'lap connection toward the mid-span of the receiving beam, which increases the vertical rise of the '
                   'dome through cumulative eccentric camber. However, this same geometric expansion elongates the '
                   'cantilever arm a, multiplying the eccentric bending moment that the wood fibers must resist in '
                   'flexure. If the lap shear force surges under heavy snow accumulation, the shear stress at the '
                   'notch root escalates nonlinearly. Without perpendicular-to-grain screw reinforcement, the timber '
                   'splits longitudinally along the grain boundary. Furthermore, because timber is an orthotropic '
                   'material with high longitudinal stiffness but low transverse shear resistance, slip within the '
                   'semi-rigid joints softens the global shell lattice. As rotational joint stiffness degrades, the '
                   'effective buckling length of each rib bay grows, lowering the global critical buckling threshold '
                   'and precipitating snap-through instability.',
 'act4_deepening': 'One proposal for practice, not a description of current use: instead of drawing hundreds of '
                   'bespoke lap notches by hand, a human architect could sketch the roof envelope and sightlines while '
                   'a geometry solver works out the closed-loop kinematics of the nexorade mesh and drafts five-axis '
                   'toolpaths. Any such output would still need checking against EN 1995-1-1 by a qualified engineer. '
                   'An open question lies in real-time robotic '
                   'fabrication and material variability: can computer vision and acoustic resonance testing during '
                   'milling detect localized knots and grain deviations in each unique glulam billet, dynamically '
                   'altering the engagement geometry on the fly to place joint notches only in pristine, defect-free '
                   'wood grain? That remains a research question.',
 'act4_human_ai': "Reciprocal frames are hard to design by hand because changing one beam's angle changes the "
                  'elevation of every neighboring beam. A designer, with or without an AI assistant, could pair '
                  'parametric geometry from a tool such as compas-dev/compas (https://github.com/compas-dev/compas; '
                  'see DOI 10.1016/j.cad.2015.01.006 for the underlying graphic statics) with a finite-element library '
                  'such as FEniCS/dolfinx (DOI 10.1145/3524456) to explore these weaves and prepare cutting data. This '
                  'folio names those tools as options a reader could use; it did not run them.'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a 4-valence reciprocal timber gridshell (nexorade) with eccentric '
        'notched lap joints and beechwood shear keys would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.02-V (Imagining What It Would Look Like) · Artistic architectural cutaway '
            'imagining a 4-valence GL28h larch reciprocal timber gridshell (nexorade) where eccentric notched lap '
            'joints (M_lap = V_lap a (1 - lambda)) interlock without steel gusset plates.'}

DISPATCH = {'kicker': 'FRONTIER TIMBER TECTONICS DISPATCH · RECIPROCAL NEXORADE GRIDSHELLS (EUROCODE 5)',
 'headline': 'Reciprocal Timber Gridshells: Short Members, Mutual Support, and the Bending at Every Notch',
 'body': "Building on Villard de Honnecourt's medieval floor frames and Olga Popovic Larsen's Reciprocal Frame "
         'Architecture (DOI 10.4324/9780080556000; Asefi & Bahremandi-Tolou, J. Build. Eng. 2019, DOI '
         '10.1016/j.jobe.2019.100867), this folio models a GL28h larch nexorade with an assumed eccentricity e_z = 85 '
         'mm, a lap moment of 5.15 kN·m, and illustrative values for notch utilization (0.64) and buckling (SF = '
         '3.74). As a loose visual analogy only, the mutual support recalls the paired nucleotide-binding domains of '
         'CFTR (PDB 8EIQ).'}

META_3D = ('Nexorade Reciprocal 4-Beam Pinwheel Gridshell',
 'X/Z: Geodesic Timber Lattice Coordinates · Y: Reciprocal Lap-Joint Camber & Bending Moment')

ES_TRANSLATION = {'title_es': 'Retículas Recíprocas de Madera (Nexorades), Momentos de Traslape Excéntrico y Ensambles de Corte 1:5',
 'subtitle_es': 'Cinemática estructural de entramados recíprocos de madera sin herrajes metálicos donde cada viga '
                'descansa sobre su vecina con excentricidad e_z, cubriendo grandes claros con piezas cortas.',
 'why_es': 'Como cuatro cuchillos o vigas entrelazados en molinete sobre las bordes de un vaso, cada elemento sostiene '
           'al siguiente y es sostenido por el anterior, salvando un claro mucho mayor que cualquier pieza individual.',
 'bridge_es': 'Es solo una analogía visual: así como cada viga recíproca sostiene a la siguiente, los dos dominios '
              'de unión a nucleótidos de la proteína CFTR se juntan en pareja alrededor del ATP (por ejemplo, la '
              'estructura PDB 8EIQ). Esta ficha no hace afirmaciones de salud ni es consejo médico.',
 'plain_es': 'Para entender cómo funciona una estructura recíproca de madera, coloquen cuatro cuchillos de mesa '
             'entrelazados en forma de molinete sobre la boca de una taza grande. Si el extremo de cada cuchillo '
             'descansa sobre la hoja del siguiente, el conjunto se traba por sí solo en el centro con una firmeza '
             'sorprendente. Ningún cuchillo es lo bastante largo para cruzar toda la boca de la taza por su cuenta, '
             'pero trabajando en equipo forman un puente que se sostiene solo. En la arquitectura de madera se usa '
             'este mismo truco para techar salas amplias con piezas cortas en lugar de troncos enormes. Como las piezas '
             'se apoyan unas en otras en muescas sencillas, el techo puede cargar nieve usando madera ligera.',
 'deep_es': 'El comportamiento estructural de una cáscara recíproca de madera depende de dos parámetros fundamentales: '
            'la relación de traslape entre vigas y la fuerza cortante en cada ensamble. Al ajustar la posición del '
            'traslape, se define la curvatura de la cúpula y el tamaño del óculo central que permite la entrada de luz '
            'natural. No obstante, al desfasar las piezas verticalmente, la compresión de la cúpula se transforma en '
            'un fuerte momento de flexión y esfuerzo cortante en la muesca de unión. Si la carga de nieve sobrepasa el '
            'límite que revisa el Eurocódigo 5, las fibras de la madera pueden abrirse a lo largo del grano en una '
            'falla repentina. Por eso es común reforzar las muescas con tornillos de rosca completa contra la tensión '
            'perpendicular al grano. En este modelo, el momento de traslape de 5.15 kN·m supone una viga de 1.493 m; '
            'la utilización de 0.64 y el factor de pandeo de 3.74 son valores ilustrativos, no un cálculo de diseño.'}
