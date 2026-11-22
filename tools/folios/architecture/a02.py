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
             'a vertical step at each lap, converting global shell thrust into localized bending.',
 'date_published': '2026-10-25',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.3',
 'status_badge': 'REDATED REV 1.3',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'M_lap = V_lap a (1 − λ) · τ_d ≤ k_v f_{v,d}',
 'colophon': {'identifier': 'A.02 · Reciprocal Timber Gridshells',
              'kernels': '1:50 Nexorade Bay + 1:5 Notched Lap Joint',
              'benchmarks': 'Model values: M_lap = 5.15 kN·m (a = 0.373 m, λ = 0.25) · utilization 0.64 and SF 3.74 are illustrative',
              'bridge': 'Reciprocal Load Sharing'},
 'steps': ['Stage 1 (4-Valence Reciprocal Fan): Four GL28h larch members interlock in a pinwheel loop so '
           'no more than two members meet at any point.',
           'Stage 2 (Eccentricity-Induced Dome Rise): An assumed vertical offset e_z = 85 mm at each lap joint '
           'tilts each member; repeated around the fan, this gives the dome its rise.',
           'Stage 3 (Notch Shear & Bending Check, in the style of EN 1995-1-1): With V_lap = 18.4 kN, λ = 0.25 and an '
           'assumed member length L = 1.493 m (a = λL = 0.373 m), M_lap = 18.4 × 0.373 × 0.75 = 5.15 kN·m. The '
           'default notch utilization 0.64 is an illustrative baseline rescaled by the sliders below, not a full design check.',
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
 'sidenote_1': {'kicker': 'SIDENOTE A.02 · SHORT MEMBERS, NOTCHED LAPS',
                'body': 'Reciprocal frames let members shorter than the span cover it together (Popovic Larsen 2007, DOI '
                        '10.4324/9780080556000). The trade-off is bending and shear at every notch, which EN 1995-1-1 '
                        'and notch-fracture reviews ask designers to check (Jockwer, Steiger, and Frangi 2014, DOI '
                        '10.1061/(ASCE)ST.1943-541X.0000838).'},
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
                           'the utilization 0.64 and SF 3.74 are now labeled illustrative values. The bending moment '
                           'now states its assumed member length (L = 1.493 m), the invented Song and Leonardo scenes '
                           'are replaced by a plain account.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; Scite search found no '
                        'source for the 4x-6x span claim, so it was removed.'},
               {'edition': 'REV 1.2',
                'date': '2026-11-02',
                'summary': 'REV 1.2 (Redated 2026-11-02): Added a notched lap joint shear utilization and a gridshell '
                           'buckling factor SF = 3.74, with the portable reciprocal-timber-nexorade skill.',
                'opus': 'Cross-model check of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'wording is withdrawn in REV 1.3: nothing was built, tested or checked against EN 1995-1-1.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-01',
                'summary': 'REV 1.1 (Redated 2026-11-01): Added CSI 06 18 00 CNC glulam specification plate and '
                           'perpendicular-to-grain splitting reinforcement check.',
                'opus': 'Cross-model check of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'wording for k_v = 0.78 and utilization 0.64 is withdrawn in REV 1.3: these are illustrative values.'},
               {'edition': 'REV 1.0',
                'date': '2026-10-25',
                'summary': 'REV 1.0 (Published 2026-10-25): Initial publication of reciprocal nexorade kinematics and '
                           '1:5 CNC lap joinery.',
                'opus': 'Cross-model check of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
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
                 'of short logs without river piers. One such bridge appears in the twelfth-century scroll Along the '
                 'River During the Qingming Festival. Each log rests on its neighbors, so pieces shorter than the '
                 'crossing carry the span together. Leonardo da Vinci later sketched similar self-supporting loops '
                 'of short poles in sheets now bound in the Codex Atlanticus. Builders and engineers now call these '
                 'mutually supporting loops reciprocal frames (Popovic Larsen 2007, DOI 10.4324/9780080556000); the form-finding literature also calls them nexorades (Douthe and Baverel 2009, DOI 10.1016/j.compstruc.2009.06.011).',
 'history_body': "From Villard de Honnecourt's medieval floor grillages and Leonardo da Vinci's Codex Atlanticus sketches "
                 'to contemporary timber pavilions, reciprocal frames weave short bars into closed polygonal fans. '
                 'Olga Popovic Larsen (2007, Reciprocal Frame Architecture, DOI 10.4324/9780080556000) explains how '
                 'each member rests on the next so no node gathers many beams. Douthe and Baverel (2009, DOI '
                 '10.1016/j.compstruc.2009.06.011) formulate nexorade geometry through dynamic relaxation, while '
                 'Asefi and Bahremandi-Tolou (2019, DOI 10.1016/j.jobe.2019.100867) review architectural design '
                 'challenges. Designers could pair open tools such as compas-dev/compas '
                 '(https://github.com/compas-dev/compas; 3D graphic statics in DOI 10.1016/j.cad.2015.01.006) with '
                 'EN 1995-1-1 timber checks. This folio does not run those tools and makes no embodied-carbon claim; '
                 'its numbers come from the lap-moment formula shown.',
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
                ('2009–2011',
                 'Douthe & Baverel; Gelez, Aubry & Vaudeville',
                 'Apply dynamic relaxation to nexorade form-finding (DOI 10.1016/j.compstruc.2009.06.011) and study the bending resistance and stiffness of a simple nexorade (DOI 10.1260/0266-3511.26.4.331).'),
                ('2026',
                 'Informatico.ai Folio A.02',
                 'A teaching model of the reciprocal lap moment, with an illustrative buckling factor (SF = 3.74) and '
                 'an assumed joint stiffness.')],
 'intuition_lead': 'Under gravity, a reciprocal frame couples member bending, shear, and joint flexibility across '
                   'every bar in the loop (Gelez, Aubry, and Vaudeville 2011, DOI 10.1260/0266-3511.26.4.331). In '
                   'slender timber shells, local joint splitting and elastic buckling can govern before '
                   'compressive crushing. Here, an assumed vertical step e_z = 85 mm tilts each stacked bar to give '
                   'the fan its rise, while the in-plane engagement arm a = lambda_lap * L enters this folio\'s '
                   'simplified lap-moment formula M_lap = V_lap * a * (1 - lambda_lap) (for general reciprocal frame '
                   'behavior, see Popovic Larsen 2007, DOI 10.4324/9780080556000, and Asefi and Bahremandi-Tolou '
                   '2019, DOI 10.1016/j.jobe.2019.100867). With V_lap = 18.4 kN, lambda = 0.25, and assumed member '
                   'length L = 1.493 m, a = 0.373 m and M_lap = 5.15 kN·m. EN 1995-1-1 checks notched shear as '
                   'tau_d <= k_v * f_{v,d}; splitting at re-entrant notch corners is a documented failure mode '
                   '(Jockwer, Steiger, and Frangi 2014, DOI 10.1061/(ASCE)ST.1943-541X.0000838) often reinforced '
                   'with fully threaded self-tapping screws (Dietsch and Brandner 2015, DOI '
                   '10.1016/j.conbuildmat.2015.04.028). Utilization 0.64 and buckling factor 3.74 are illustrative '
                   'values, not a full design check by a qualified engineer.',
 'intuition_body': 'In an Euler buckling estimate, critical load N_cr = pi^2 E I_eff / (k L_trib)^2 depends on the '
                   'rotational stiffness K_phi of the lap joints. This folio assumes K_phi = 142 kN·m/rad for a screwed '
                   'lap joint; that value is an assumption, not taken from a test or EN 1995-1-1. With illustrative '
                   'N_cr = 1,280 kN against design force N_d = 342 kN, the ratio is 1,280 / 342 = 3.74. These are '
                   'teaching values; the folio makes no claim about embodied carbon.',
 'walkthrough': ['Experiment 1 (Sweep Engagement Ratio): Drag Slider 1 (λ = a / L) from 0.15 to 0.45 at V_lap = '
                 '18.4 kN. Watch M_lap climb from 3.50 to 6.80 kN·m as the lap moves inward toward mid-span.',
                 'Experiment 2 (Test the Surrogate Alert & Node): With λ = 0.25, raise Slider 2 (V_lap) to about 28.8 kN to see illustrative utilization pass 1.00, then inspect the 4-beam SVG weave below.',
                 'Experiment 3 (Read the Companion Skill): Download reciprocal-timber-nexorade SKILL.md below; it '
                 'summarizes the lap-moment formula, notch shear ratio, and screw-reinforcement rule as a study aid, '
                 'not a design code.'],
 'human_ai_shift': "Reciprocal frames are hard to adjust by hand because tilting one beam shifts every neighbor's "
                   'elevation (Douthe and Baverel 2009, DOI 10.1016/j.compstruc.2009.06.011). A designer could pair '
                   'compas-dev/compas (https://github.com/compas-dev/compas; graphic statics in DOI '
                   '10.1016/j.cad.2015.01.006) with FEniCS/dolfinx (DOI 10.1145/3524456) to explore geometry and '
                   'prepare cutting data. This folio names those tools as options; it did not run them.',
 'sources': ['Leonardo da Vinci (c. 1478–1519). Codex Atlanticus. Biblioteca Ambrosiana, Milan.',
             'Otto, F., & Hennicke, J. (1974). IL 10: Gitterschalen / Grid Shells. Institute for Lightweight '
             'Structures, Stuttgart.',
             'Popovic Larsen, O. (2007). Reciprocal Frame Architecture. Architectural Press / Routledge. DOI: '
             '10.4324/9780080556000.',
             'Douthe, C., & Baverel, O. (2009). Design of nexorades or reciprocal frame systems with the dynamic '
             'relaxation method. Computers & Structures, 87(21–22), 1296–1307. DOI: 10.1016/j.compstruc.2009.06.011.',
             'Gelez, S., Aubry, S., & Vaudeville, B. (2011). Behavior of a Simple Nexorade or Reciprocal Frame '
             'System. International Journal of Space Structures, 26(4), 331–342. DOI: 10.1260/0266-3511.26.4.331.',
             'Jockwer, R., Steiger, R., & Frangi, A. (2014). State-of-the-Art Review of Approaches for the Design of '
             'Timber Beams with Notches. Journal of Structural Engineering, 140(3). DOI: '
             '10.1061/(ASCE)ST.1943-541X.0000838.',
             'Dietsch, P., & Brandner, R. (2015). Self-tapping screws and threaded rods as reinforcement for '
             'structural timber elements – A state-of-the-art report. Construction and Building Materials, 97, '
             '78–89. DOI: 10.1016/j.conbuildmat.2015.04.028.',
             'Asefi, M., & Bahremandi-Tolou, M. (2019). Design challenges of reciprocal frame structures in '
             'architecture. Journal of Building Engineering, 26, 100867. DOI: 10.1016/j.jobe.2019.100867.',
             'CEN (2004). EN 1995-1-1, Eurocode 5: Design of timber structures — Part 1-1: General — Common rules and '
             'rules for buildings.',
             'CEN (2013). EN 14080, Timber structures — Glued laminated timber and glued solid timber — Requirements.',
             'Akbarzadeh, M., Van Mele, T., & Block, P. (2015). On the equilibrium of funicular polyhedral frames and '
             'convex polyhedral force diagrams. Computer-Aided Design, 63, 118–128. DOI: 10.1016/j.cad.2015.01.006. '
             '(Cited for graphic statics; compas-dev/compas, https://github.com/compas-dev/compas, is a separate '
             'open-source framework.)',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order '
             'Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (FEniCS/dolfinx, '
             'https://github.com/FEniCS/dolfinx). ACM Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: '
             '10.1145/3524456.'],
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
                 'of short logs without river piers. One such bridge appears in the twelfth-century scroll Along the '
                 'River During the Qingming Festival. Each log rests on its neighbors, so pieces shorter than the '
                 'crossing carry the span together. Leonardo da Vinci later sketched similar self-supporting loops '
                 'of short poles in sheets now bound in the Codex Atlanticus. Builders and engineers now call these '
                 'mutually supporting loops reciprocal frames (Popovic Larsen 2007, DOI 10.4324/9780080556000); the form-finding literature also calls them nexorades (Douthe and Baverel 2009, DOI 10.1016/j.compstruc.2009.06.011).',
 'act1_plain_bridge': 'Lay four wooden butter knives across an open coffee mug rim so each tip rests on the next '
                      'blade. Press down in the center. The pinwheel locks firm over the opening even though no '
                      'single knife reaches across on its own. Working together, short pieces bridge a wider gap. '
                      'Timber builders apply the same weave to roof halls with short boards instead of giant tree '
                      'trunks. Each beam leans on its neighbor at a simple notch, spreading weight without a '
                      'crowded central hub.',
 'act1_body': "From Villard de Honnecourt's medieval floor grillages and Leonardo da Vinci's Codex Atlanticus sketches "
              'to contemporary timber pavilions, reciprocal frames weave short bars into closed polygonal fans. '
              'Olga Popovic Larsen (2007, Reciprocal Frame Architecture, DOI 10.4324/9780080556000) explains how '
              'each member rests on the next so no node gathers many beams. Douthe and Baverel (2009, DOI '
              '10.1016/j.compstruc.2009.06.011) formulate nexorade geometry through dynamic relaxation, while '
              'Asefi and Bahremandi-Tolou (2019, DOI 10.1016/j.jobe.2019.100867) review architectural design '
              'challenges. Designers could pair open tools such as compas-dev/compas '
              '(https://github.com/compas-dev/compas; 3D graphic statics in DOI 10.1016/j.cad.2015.01.006) with '
              'EN 1995-1-1 timber checks. This folio does not run those tools and makes no embodied-carbon claim; '
              'its numbers come from the lap-moment formula shown.',
 'act1_stakes': 'Sizing reciprocal frames by eye risks joint rotation and splitting. In a reciprocal grid, member '
                'bending, shear, and joint flexibility are tightly coupled, and how the members connect affects the stiffness and robustness of the whole (Gelez, Aubry, and Vaudeville 2011, DOI 10.1260/0266-3511.26.4.331). Cutting a '
                'notch too deep severs tensile wood fibers and concentrates splitting stress perpendicular to the '
                'grain (Jockwer, Steiger, and Frangi 2014, DOI 10.1061/(ASCE)ST.1943-541X.0000838). Engineers '
                'therefore check both notch shear and overall frame stability.',
 'act2_analogy': 'Slide four interlocked butter knives across a mug rim farther inward from their tips, and each blade '
                 'bends harder over a longer lever arm. Short pieces still bridge the rim, yet every lap carries '
                 'sharper bending. Where the picture stops: kitchen knives are held only by friction and can slip apart, whereas notched '
                 'timber beams have cut grain fibers that can split under heavy shear.',
 'act2_plain_primer': 'Two sliders drive the teaching model below. The first slider sets the engagement ratio from '
                      '0.15 near the beam tip to 0.45 toward mid-span. Moving the lap inward lengthens the bending '
                      'lever and lifts the model moment from 3.50 to 6.80 kN·m at 18.4 kN. The second slider scales '
                      'downward notch shear from 8.0 to 32.0 kN. The interactive script scales illustrative '
                      'utilization proportionally with the lap moment from its 0.64 default, crossing 1.00 at about 28.8 kN when the engagement ratio is 0.25. It also scales the illustrative buckling factor inversely from 3.74. This '
                      'surrogate scaling is a teaching aid, not a Eurocode 5 notch-shear or buckling calculation.',
 'distill_diagram': {'analogy_title': 'Four Interlocked Knives Over Mug Rim',
                     'analogy_sub': 'Mutual lap support spans wide openings with short pieces',
                     'force_a_title': 'Engagement Ratio (λ = a/L)',
                     'force_a_sub': 'Moves lap inward toward mid-span, raising lever arm and lap moment',
                     'force_b_title': 'Lap Shear Force (V_lap)',
                     'force_b_sub': 'Downward roof gravity load transferred across each notch',
                     'threshold_title': 'Eurocode 5 Notch Shear Limit (τ_d <= k_v f_vd)',
                     'threshold_pass': 'Within the model limit; self-tapping screws help resist splitting',
                     'threshold_fail': 'Above model limit: notch shear rises; unreinforced wood can split along grain'},
 'act2_intuition': 'Under gravity, a reciprocal frame couples member bending, shear, and joint flexibility across '
                   'every bar in the loop (Gelez, Aubry, and Vaudeville 2011, DOI 10.1260/0266-3511.26.4.331). In '
                   'slender timber shells, local joint splitting and elastic buckling can govern before '
                   'compressive crushing. Here, an assumed vertical step e_z = 85 mm tilts each stacked bar to give '
                   'the fan its rise, while the in-plane engagement arm a = lambda_lap * L enters this folio\'s '
                   'simplified lap-moment formula M_lap = V_lap * a * (1 - lambda_lap) (for general reciprocal frame '
                   'behavior, see Popovic Larsen 2007, DOI 10.4324/9780080556000, and Asefi and Bahremandi-Tolou '
                   '2019, DOI 10.1016/j.jobe.2019.100867). With V_lap = 18.4 kN, lambda = 0.25, and assumed member '
                   'length L = 1.493 m, a = 0.373 m and M_lap = 5.15 kN·m. EN 1995-1-1 checks notched shear as '
                   'tau_d <= k_v * f_{v,d}; splitting at re-entrant notch corners is a documented failure mode '
                   '(Jockwer, Steiger, and Frangi 2014, DOI 10.1061/(ASCE)ST.1943-541X.0000838) often reinforced '
                   'with fully threaded self-tapping screws (Dietsch and Brandner 2015, DOI '
                   '10.1016/j.conbuildmat.2015.04.028). Utilization 0.64 and buckling factor 3.74 are illustrative '
                   'values, not a full design check by a qualified engineer.',
 'act2_deepening': 'Engagement ratio lambda and lap shear V_lap jointly drive M_lap = V_lap * a * (1 - lambda), '
                   'peaking as the lap approaches mid-span (lambda = 0.50). Because timber is orthotropic—stiff '
                   'along the grain but weak in perpendicular tension and shear—high notch loads demand careful '
                   'detailing and reinforcement. In addition, connection behavior affects the stiffness of the whole frame (Gelez, Aubry, and Vaudeville 2011, DOI 10.1260/0266-3511.26.4.331); in the Euler estimate used here, a lower rotational joint stiffness K_phi gives a lower critical load.',
 'act4_deepening': 'One proposal for practice, not current use: an architect could sketch the roof envelope while a '
                   'dynamic-relaxation solver computes closed-loop nexorade kinematics (Douthe and Baverel 2009, DOI '
                   '10.1016/j.compstruc.2009.06.011) and drafts five-axis toolpaths. Any output would still require '
                   'EN 1995-1-1 verification by a qualified engineer. An open research question is whether in-line '
                   'scanning during milling could detect knots and adjust notch positions to avoid weak grain.',
 'act4_human_ai': "Reciprocal frames are hard to adjust by hand because tilting one beam shifts every neighbor's "
                  'elevation (Douthe and Baverel 2009, DOI 10.1016/j.compstruc.2009.06.011). A designer could pair '
                  'compas-dev/compas (https://github.com/compas-dev/compas; graphic statics in DOI '
                  '10.1016/j.cad.2015.01.006) with FEniCS/dolfinx (DOI 10.1145/3524456) to explore geometry and '
                  'prepare cutting data. This folio names those tools as options; it did not run them.'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a 4-valence reciprocal timber gridshell (nexorade) with eccentric '
        'notched lap joints and beechwood shear keys would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.02-V (Imagining What It Would Look Like) · Artistic architectural cutaway '
            'imagining a 4-valence GL28h larch reciprocal timber gridshell (nexorade) where eccentric notched lap '
            'joints (M_lap = V_lap a (1 - lambda)) interlock without steel gusset plates.'}

DISPATCH = {'kicker': 'FRONTIER TIMBER TECTONICS DISPATCH · RECIPROCAL NEXORADE GRIDSHELLS (EUROCODE 5)',
 'headline': 'Reciprocal Timber Gridshells: Short Members, Mutual Support, and the Bending at Every Notch',
 'body': "Building on Villard de Honnecourt's medieval floor frames and Olga Popovic Larsen's Reciprocal Frame "
         'Architecture (DOI 10.4324/9780080556000; Douthe & Baverel 2009, DOI 10.1016/j.compstruc.2009.06.011; '
         'Asefi & Bahremandi-Tolou 2019, DOI 10.1016/j.jobe.2019.100867), this folio models a GL28h larch nexorade '
         'with assumed eccentricity e_z = 85 mm, lap moment 5.15 kN·m, and illustrative values for notch '
         'utilization (0.64) and buckling (SF = 3.74).'}

META_3D = ('Nexorade Reciprocal 4-Beam Pinwheel Gridshell',
 'X/Z: Geodesic Timber Lattice Coordinates · Y: Reciprocal Lap-Joint Camber & Bending Moment')

ES_TRANSLATION = {'title_es': 'Retículas Recíprocas de Madera (Nexorades), Momentos de Traslape Excéntrico y Ensambles de Corte 1:5',
 'subtitle_es': 'Cinemática estructural de entramados recíprocos de madera sin placas ni pernos metálicos donde cada '
                'viga descansa sobre su vecina con un desfase vertical en cada traslape, convirtiendo el empuje '
                'global en flexión local.',
 'why_es': 'Si cuatro cuchillos entrelazados sobre una taza se apoyan más hacia el centro de cada hoja, crecen el brazo de palanca y la flexión en cada apoyo. Donde termina la imagen: los cuchillos solo se sostienen por fricción y pueden resbalar, mientras que las vigas con muescas tienen fibras cortadas que pueden abrirse a lo largo del grano bajo cortante alto.',
 'plain_es': 'Coloquen cuatro cuchillos de madera para mantequilla sobre la boca de una taza de café, con cada punta apoyada sobre la '
             'hoja siguiente. Presionen el centro. El molinete se traba con firmeza aunque ningún cuchillo cruce la '
             'taza por sí solo. Juntos, varios tramos cortos salvan un claro mayor. En la arquitectura en madera se '
             'aplica el mismo tejido para cubrir salas amplias con tablas cortas en lugar de troncos enormes. Cada '
             'viga se apoya en su vecina con una muesca sencilla, sin reunir muchas piezas en un solo nudo.',
 'deep_es': 'Dos deslizadores controlan el modelo: la relación de traslape (de 0.15 cerca del extremo a 0.45 hacia '
            'el centro) y el cortante en la muesca (de 8.0 a 32.0 kN). Mover el traslape hacia el centro eleva '
            'M_lap de 3.50 a 6.80 kN·m con 18.4 kN (5.15 kN·m en el valor base λ = 0.25 y L = 1.493 m). La '
            'geometría entrante de la muesca concentra cortante y tensión perpendicular al grano; por ello el '
            'Eurocódigo 5 revisa estas zonas y suelen añadirse tornillos de rosca completa. Los deslizadores '
            'reescalan la utilización ilustrativa desde 0.64 proporcionalmente con M_lap (superando 1.00 cerca de 28.8 kN con λ = 0.25) y el factor de pandeo inversamente desde 3.74; es una guía didáctica, no un cálculo de diseño.'}
