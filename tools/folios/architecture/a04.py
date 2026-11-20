#!/usr/bin/env python3
"""Folio A.04 (ARCHITECTURE): From Archigram's Plug-In Megastructures to British High-Tech Exoskeletons: Gerberette Cantilevers, Maxwell Space Frames & Shearing-Layer Pods."""
from __future__ import annotations

SLUG = 'a04'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.04',
 'slug': 'a04',
 'pillar': 'architecture',
 'category_code': 'A',
 'title': "From Archigram's Plug-In Megastructures to British High-Tech Exoskeletons: Gerberette Cantilevers, Maxwell "
          'Space Frames & Shearing-Layer Pods',
 'subtitle': "How the plug-in ideas of Peter Cook and Ron Herron's 1960s Archigram drawings are widely seen as an "
             'influence on the British High-Tech work of Richard Rogers, Renzo Piano, Peter Rice and Norman '
             'Foster—and a lever model of the cast-steel gerberette, with replaceable service modules as a proposal.',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.3',
 'status_badge': 'HIGH-TECH & ARCHIGRAM · REV 1.3',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'T_tie = V_p · (a / c) · b − 3j + 6 = s − m · τ_pod ≪ τ_frame',
 'colophon': {'identifier': 'A.04 · Archigram to High-Tech Exoskeletons · CSI 05 12 13',
              'kernels': 'Gerberette T_tie = V_p(a/c) · Maxwell Rigidity · Shearing Layers',
              'benchmarks': 'Model values: T_tie = 4,800 × 1.60 / 6.00 = 1,280 kN (V_p assumed) · SF 3.12 illustrative',
              'bridge': 'Long-Life Frame + Replaceable Services ↔ Adaptable Clinical Buildings (a proposal)'},
 'sliders': [{'label': 'Gerberette Cantilever Arm (a)',
              'min': 0.8,
              'max': 2.6,
              'step': 0.05,
              'value': 1.6,
              'unit': ' m'},
             {'label': 'Exterior Tie-Rod Back-Span (c)',
              'min': 3.5,
              'max': 8.5,
              'step': 0.1,
              'value': 6.0,
              'unit': ' m'}],
 'steps': ["Stage 1 (Archigram Plug-In Matrix, 1961–1964): Peter Cook's Plug-In City and Ron Herron's Walking City "
           'imagine a long-lived structural frame carrying short-lived clip-on capsules (the 100-year and 15-year '
           'lifetimes used here are the folio\'s illustrative values).',
           'Stage 2 (Pompidou Cast-Steel Gerberette Equilibrium, 1971–1977): In the folio\'s lever model, an assumed '
           'floor reaction V_p = 4,800 kN acts at a = 1.60 m outside the column and is balanced by an exterior tie: '
           'T_tie = V_p·(a/c) = 4,800 × 1.60 / 6.00 = 1,280.0 kN at c = 6.00 m. These are teaching values, not the '
           'loads of the real building.',
           'Stage 3 (Foster & Rogers High-Tech Mast Suspension, 1978–1986): Norman Foster (HSBC Hong Kong) hangs floors '
           "from masts, and Richard Rogers (Lloyd's of London) places service towers and prefabricated service pods "
           'outside the main floor plates.',
           "Stage 4 (Brand's Shearing Layers & Replaceable Service Modules): Stewart Brand describes building layers "
           'that change at different rates. Keeping services outside the long-life frame could, as a proposal, make '
           'it easier to replace clinical or laboratory service modules.'],
 'readouts': [{'label': 'Exoskeleton Clear Span (Pompidou, as Reported)', 'value': 'About 48 m (column-free floors)'},
              {'label': 'Gerberette Tie-Rod Tension (Model)', 'value': '1,280.0 kN (SF = 3.12, illustrative)'},
              {'label': 'Shearing-Layer Ratio (Illustrative)', 'value': 'τ_pod = 15 yr / τ_frame = 100 yr'},
              {'label': 'Maxwell-Calladine Index (Assumed)', 'value': 'm = 0 assumed, not computed'}],
 'sidenote_1': {'kicker': 'SIDENOTE A.04-A · ARCHIGRAM TO FOSTER, ROGERS & FUTURE SYSTEMS',
                'body': "Archigram's members taught at architecture schools such as the Architectural Association, and "
                        'their drawings are widely seen as an influence on British High-Tech. This folio does not '
                        'document direct teaching links between Archigram and Team 4 (Norman Foster and Richard Rogers) '
                        "or Jan Kaplický's Future Systems."},
 'sidenote_2': {'kicker': 'SIDENOTE A.04-B · SPECIFICATION PLATE · CSI 05 12 13 (ARCHITECTURALLY EXPOSED STRUCTURAL '
                          'STEEL)',
                'body': 'Design proposal, not a tested product: cast-steel gerberette brackets with a specified f_y = 355 '
                        'MPa and Charpy V-notch ≥ 40 J at −20 °C, external stainless-steel tension tie rods, and '
                        'quick-disconnect service manifolds.'},
 'skill': {'filename': 'archigram-hightech-exoskeleton-SKILL.md',
           'name': 'archigram-hightech-exoskeleton',
           'description': 'AI-agnostic architectural and structural engineering skill for Archigram Plug-In '
                          'megastructures, British High-Tech exoskeletons (Foster, Rogers, Piano, Rice), gerberette '
                          'cantilever statics, Maxwell-Calladine space-frame rigidity, and Stewart Brand shearing '
                          'layers.',
           'rules': ['Evaluate cast-steel gerberette cantilever equilibrium: exterior tension tie force T_tie = '
                     'V_floor * (a / c) and column compression C_col = V_floor * (1 + a / c).',
                     'Verify 3D space-frame static and kinematic determinacy via the Maxwell-Calladine matrix index b '
                     '- 3j + 6 = s - m (ensuring m = 0 internal mechanisms).',
                     "Decouple Stewart Brand's 6 Shearing Layers by routing all Services (HVAC, medical gases, "
                     'cleanroom exhaust, tau = 7-15 yr) on the exterior exoskeleton outside the 48 m column-free '
                     'Structure (tau = 60-100 yr).']},
 'revisions': [{'edition': 'REV 1.3',
                'date': '2026-11-14',
                'summary': 'REV 1.3 (Redated 2026-11-14): Grounding revision. The PASS verdict, the claim that COMPAS '
                           'verified the tie-rod safety factor, and the claims that Archigram directly mentored Foster '
                           'and Rogers were unsourced and are withdrawn; V_p = 4,800 kN and SF = 3.12 are now labeled '
                           'as assumed and illustrative. The invented 1961 founding scene and a source entry that did not '
                           'exist as cited are replaced by a plain '
                           'account and a modest, labeled proposal.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; Hamzeian (2018, DOI '
                        '10.1201/9780429506208-91) documents the evolution of the Pompidou cast node, and the '
                        'lever-model numbers come from the stated formulas.'},
               {'edition': 'REV 1.2',
                'date': '2026-11-02',
                'summary': 'REV 1.2 (Redated 2026-11-02): Revised the cast-steel gerberette lever model and Stewart Brand '
                           'shearing-layer discussion.',
                'opus': 'Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'wording is withdrawn in REV 1.3: T_tie = 1,280 kN follows from assumed inputs, and SF = 3.12 '
                        'and m = 0 were not computed.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-01',
                'summary': 'REV 1.1 (Redated 2026-11-01): Dedicated 5-Act monograph tracing the lineage from Archigram '
                           '(Plug-In City, Walking City) to British High-Tech (Foster, Rogers, Piano, Rice) with a '
                           'gerberette lever model and shearing layers.',
                'opus': 'Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'wording is withdrawn in REV 1.3.'}],
 'volume': 2,
 'volume_code': 'VOL. 02',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/0020-7683(86)90014-4',
           'fetched_on': '2026-11-08',
           'citing_publications': 833,
           'supporting': 1,
           'mentioning': 499,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Pellegrino & Calladine, Matrix analysis of statically and kinematically indeterminate frameworks (DOI 10.1016/0020-7683(86)90014-4), checked 2026-11-08: 833 citing publications (1 supporting, 499 mentioning, 0 contrasting) and no retraction notice. The paper is about framework rigidity; it says nothing about gerberettes or this folio\'s numbers.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/0020-7683(86)90014-4',
           'fetched_on': '2026-11-08',
           'citing_publications': 833,
           'supporting': 1,
           'mentioning': 499,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Pellegrino & Calladine, Matrix analysis of statically and kinematically indeterminate frameworks (DOI 10.1016/0020-7683(86)90014-4), checked 2026-11-08: 833 citing publications (1 supporting, 499 mentioning, 0 contrasting) and no retraction notice. The paper is about framework rigidity; it says nothing about gerberettes or this folio\'s numbers.'},
 'history_lead': 'Archigram began in London in 1961 as a small magazine by Peter Cook, Warren Chalk, Dennis Crompton, '
                 'David Greene, Ron Herron, and Michael Webb (Cook et al. 1999). Their drawings asked why buildings '
                 'stay fixed when uses and technology keep changing. In Plug-In City and Walking City (1964), cranes '
                 'lift replaceable capsules onto a permanent frame (Beslioglu 2014, DOI 10.4995/vlc.2014.1829). In '
                 '1971 Renzo Piano, Richard Rogers, and Ove Arup & Partners engineers including Peter Rice won the '
                 'Centre Pompidou competition in Paris (Rice 1994; Hamzeian 2018, DOI 10.1201/9780429506208-91).',
 'history_body': "Archigram's drawings are widely seen as an influence on British High-Tech architecture; this folio "
                 'does not document direct teaching links to Norman Foster, Richard Rogers, or Jan Kaplický. At the '
                 'Centre Pompidou, Peter Rice and the Arup team evolved the cast-steel node from a friction collar into '
                 'the gerberette bracket (Hamzeian 2018, DOI 10.1201/9780429506208-91; Rice 1994). Floor trusses bear '
                 'on short gerberette arms outside the columns and are tied down at the outer tips. That layout '
                 'leaves floors of about 48 m free of interior columns, and Norman Foster later hung floors from masts '
                 'at HSBC Hong Kong. For rigid frames, James Clerk Maxwell introduced reciprocal force diagrams (1864, '
                 'DOI 10.1080/14786446408643663). Calladine (1978, DOI 10.1016/0020-7683(78)90052-5) and Pellegrino '
                 'and Calladine (1986, DOI 10.1016/0020-7683(86)90014-4) formalized the rule b − 3j + 6 = s − m for '
                 'self-stress states s and mechanisms m. Designers today could model polyhedral frames with '
                 'compas-dev/compas (https://github.com/compas-dev/compas; Akbarzadeh, Van Mele, and Block 2015, DOI '
                 '10.1016/j.cad.2015.01.006); this folio does not run those tools.',
 'pullquote': 'What Archigram drew in 1964 as a Plug-In frame (Beslioglu 2014, DOI 10.4995/vlc.2014.1829), Piano, '
              'Rogers, and Rice built in cast steel at the Pompidou (Rice 1994; Hamzeian 2018, DOI '
              '10.1201/9780429506208-91): push structure and services outward so the floor plate stays open.',
 'pullquote_cite': 'Editorial Synthesis · Archigram (1964) to Centre Pompidou (1977) & Brand (1994)',
 'chronology': [('1961–1964',
                 'Archigram (Cook, Herron, Chalk, Crompton, Webb, Greene)',
                 'Publish Archigram 1–4, Plug-In City, and Walking City, separating the structural frame from '
                 'clip-on capsules (Cook et al. 1999; Beslioglu 2014, DOI 10.4995/vlc.2014.1829).'),
                ('1961–1972',
                 'Cedric Price (Fun Palace) & N. J. Habraken (Supports)',
                 'Propose reconfigurable spatial matrices (Mathews 2006, DOI 10.1111/j.1531-314x.2006.00032.x) '
                 'and separate shared structural supports from changeable infill (Habraken 2021, orig. 1961/1972, '
                 'DOI 10.4324/9781003014713).'),
                ('1971–1977',
                 'Renzo Piano, Richard Rogers & Peter Rice (Centre Pompidou)',
                 'Develop cast-steel gerberette brackets and exterior services, leaving floor plates of about 48 m '
                 'column-free (Rice 1994; Hamzeian 2018, DOI 10.1201/9780429506208-91).'),
                ('1978–1986',
                 "Norman Foster (HSBC Hong Kong) & Richard Rogers (Lloyd's)",
                 'Hang floor trusses from exterior masts (HSBC) and place service towers outside main floor plates '
                 "(Lloyd's)."),
                ('1994',
                 'Stewart Brand',
                 'Publishes How Buildings Learn, adapting Frank Duffy\'s shearing layers to explain why structure '
                 '(30–300 yr) outlasts services (7–15 yr) and space plans (Brand 1994).')],
 'intuition_lead': 'This high-tech exoskeleton rests on two static ideas. First, the cast-steel gerberette acts as a '
                   'class-one lever pivoting on an exterior steel column (Rice 1994; Hamzeian 2018, DOI '
                   '10.1201/9780429506208-91). A floor reaction V_p acts at cantilever arm a outside the column, and '
                   'an exterior tie rod restrains the outer tip at back-span c, giving T_tie = V_p * (a / c). Column '
                   'compression then becomes C_col = V_p * (1 + a / c). With assumed inputs V_p = 4,800 kN, a = 1.60 m, '
                   'and c = 6.00 m, the model yields T_tie = 1,280 kN and C_col = 6,080 kN. Second, the '
                   'Maxwell–Calladine rule, b − 3j + 6 = s − m (Maxwell 1864, DOI 10.1080/14786446408643663; Calladine '
                   '1978, DOI 10.1016/0020-7683(78)90052-5; Pellegrino & Calladine 1986, DOI '
                   '10.1016/0020-7683(86)90014-4), relates bars and joints to states of self-stress s and mechanisms '
                   'm. This folio assumes m = 0 without computing a frame matrix, and treats SF = 3.12 as an '
                   'illustrative value.',
 'intuition_body': 'This folio reads the High-Tech response to lifecycle mismatch through two structural ideas. '
                   'First, a perimeter frame can be checked for internal mechanisms with the Maxwell–Calladine rule '
                   '(b − 3j + 6 = s − m in 3D, or b = 2j − 3 in 2D; Pellegrino & Calladine 1986, DOI '
                   '10.1016/0020-7683(86)90014-4). Carrying loads on a perimeter exoskeleton helps keep interior '
                   'floors free of columns, as at the Centre Pompidou (Rice 1994). Second, cantilevering V_p at '
                   'arm a = 1.60 m and anchoring the outer tip at back-span c = 6.00 m shifts bending demand to an '
                   'exterior tie rod (T_tie = V_p * a / c) while opening an outer zone for replaceable services '
                   '(Brand 1994; Habraken 2021, DOI 10.4324/9781003014713).',
 'walkthrough': ['Experiment 1 (Trace the Archigram-to-High-Tech Lineage): Click Stages 1 -> 4 in the stepper above to '
                 "follow the path from Peter Cook's 1964 Plug-In City to the Pompidou gerberette lever model, the "
                 "High-Tech masts and service towers, and Stewart Brand's shearing layers.",
                 'Experiment 2 (Move the Lever Arms): Drag the cantilever arm a and the tie back-span c below to see how '
                 'the model tie-rod tension T_tie = V_p · a / c changes for the assumed V_p = 4,800 kN.',
                 'Experiment 3 (Read the Companion Skill): Use the portable SKILL.md below to study the gerberette lever '
                 'formula, the Maxwell-Calladine counting rule and shearing-layer thinking. It is a study aid, not a '
                 'design code.'],
 'human_ai_shift': "A speculative coda, labeled as such: Ron Herron's Walking City and Peter Cook's Plug-In City "
                   'imagined buildings whose parts could be swapped (Beslioglu 2014, DOI 10.4995/vlc.2014.1829). '
                   'Future frames might use lightweight lattice materials and digital inspection logs to plan module '
                   'replacement. None of this describes current practice, no figures are computed here, and it is not '
                   'an approved medical facility design.',
 'sources': ['Maxwell, J. C. (1864). XLV. On reciprocal figures and diagrams of forces. The London, Edinburgh, and '
             'Dublin Philosophical Magazine and Journal of Science, 27(182), 250–261. DOI: '
             '10.1080/14786446408643663.',
             'Cook, P., Chalk, W., Crompton, D., Greene, D., Herron, R., & Webb, M. (1961–1974 / 1999). Archigram. '
             'Princeton Architectural Press.',
             'Beslioglu, B. (2014). The Critical Approach of "Plug" in Re-Conceptualisation of Architectural Program. '
             'VLC arquitectura. Research Journal, 1(1), 59–76. DOI: 10.4995/vlc.2014.1829.',
             'Mathews, S. (2006). The Fun Palace as Virtual Architecture: Cedric Price and the Practices of '
             'Indeterminacy. Journal of Architectural Education, 59(3), 39–48. DOI: '
             '10.1111/j.1531-314x.2006.00032.x.',
             'Habraken, N. J. (2021; orig. 1961 / 1972). Supports: An Alternative to Mass Housing. Routledge. DOI: '
             '10.4324/9781003014713.',
             'Rice, P. (1994). An Engineer Imagines. Artemis, London.',
             "Hamzeian, B. (2018). The evolution of the cast node of the Pompidou Centre: From the 'friction collar' "
             "to the 'gerberette'. Building Knowledge, Constructing Histories (6ICCH), Taylor & Francis. DOI: "
             '10.1201/9780429506208-91.',
             'Calladine, C. R. (1978). Buckminster Fuller\'s "Tensegrity" structures and Clerk Maxwell\'s rules for the '
             'construction of stiff frames. International Journal of Solids and Structures, 14(2), 161–172. DOI: '
             '10.1016/0020-7683(78)90052-5.',
             'Pellegrino, S., & Calladine, C. R. (1986). Matrix analysis of statically and kinematically indeterminate '
             'frameworks. International Journal of Solids and Structures, 22(4), 409–428. DOI: '
             '10.1016/0020-7683(86)90014-4.',
             "Brand, S. (1994). How Buildings Learn: What Happens After They're Built. Viking Press.",
             'Akbarzadeh, M., Van Mele, T., & Block, P. (2015). On the equilibrium of funicular polyhedral frames and '
             'convex polyhedral force diagrams. Computer-Aided Design, 63, 118–128. DOI: 10.1016/j.cad.2015.01.006. '
             '(Cited for graphic statics; compas-dev/compas, https://github.com/compas-dev/compas, is a separate '
             'open-source framework.)',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations '
             'and classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
             '882–898. DOI: 10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Archigram Plug-In Megastructure to '
        'British High-Tech Exoskeleton Gerberette & Shearing Layers">\n'
        '            <rect id="tp-a04-bay" x="175" y="34" width="330" height="145" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="2.5"/>\n'
        '            <path id="tp-a04-truss-1" class="tp-svg-flow-line" d="M 175 82 Q 340 88 505 82" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="2.5" stroke-dasharray="6,4"/>\n'
        '            <path id="tp-a04-truss-2" class="tp-svg-flow-line" d="M 175 130 Q 340 136 505 130" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="2.5" stroke-dasharray="6,4"/>\n'
        '            <line x1="145" y1="24" x2="145" y2="190" stroke="var(--tp-ink)" stroke-width="4.5"/>\n'
        '            <line x1="535" y1="24" x2="535" y2="190" stroke="var(--tp-ink)" stroke-width="4.5"/>\n'
        '            <line id="tp-a04-tie-l" class="tp-svg-flow-line" x1="95" y1="24" x2="95" y2="190" '
        'stroke="var(--tp-minium)" stroke-width="2.8" stroke-dasharray="5,3"/>\n'
        '            <line id="tp-a04-tie-r" class="tp-svg-flow-line" x1="585" y1="24" x2="585" y2="190" '
        'stroke="var(--tp-minium)" stroke-width="2.8" stroke-dasharray="5,3"/>\n'
        '            <polygon id="tp-a04-gerberette-1" points="95,82 145,73 175,82 145,91" fill="var(--tp-minium)"/>\n'
        '            <polygon id="tp-a04-gerberette-2" points="95,130 145,121 175,130 145,139" '
        'fill="var(--tp-minium)"/>\n'
        '            <rect id="tp-a04-pod-1" x="548" y="42" width="68" height="36" rx="3" fill="var(--tp-verdigris)" '
        'fill-opacity="0.26" stroke="var(--tp-verdigris)" stroke-width="2"/>\n'
        '            <rect id="tp-a04-pod-2" x="548" y="92" width="68" height="36" rx="3" fill="var(--tp-verdigris)" '
        'fill-opacity="0.26" stroke="var(--tp-verdigris)" stroke-width="2"/>\n'
        '            <rect id="tp-a04-pod-3" x="548" y="142" width="68" height="36" rx="3" fill="var(--tp-verdigris)" '
        'fill-opacity="0.26" stroke="var(--tp-verdigris)" stroke-width="2"/>\n'
        '            <text x="215" y="62" font-size="11" font-weight="700" fill="var(--tp-prussian)">Column-Free '
        'Clear Span (~48 m)</text>\n'
        '            <text x="210" y="110" font-size="10.5" fill="currentColor">Reconfigurable Lab / Clinical Floor '
        'Plate (τ = 3–15 yr)</text>\n'
        '            <text x="210" y="158" font-size="10.5" fill="currentColor">Permanent Exoskeleton Mast &amp; Truss '
        '(τ = 100 yr)</text>\n'
        '            <text x="22" y="110" font-size="10" fill="var(--tp-minium)">Gerberette + Tie</text>\n'
        '            <text x="546" y="34" font-size="10" font-weight="700" fill="var(--tp-verdigris)">Plug-In '
        'Pods</text>\n'
        '            <text id="tp-a04-svg-label" x="135" y="206" font-size="11" fill="currentColor">Archigram (1964) → '
        'Pompidou / Foster / Rogers High-Tech Exoskeleton (T_tie = 1,280 kN)</text>\n'
        '          </svg>',
 'act1_dropcap': 'Archigram began in London in 1961 as a small magazine by Peter Cook, Warren Chalk, Dennis Crompton, '
                 'David Greene, Ron Herron, and Michael Webb (Cook et al. 1999). Their drawings asked why buildings '
                 'stay fixed when uses and technology keep changing. In Plug-In City and Walking City (1964), cranes '
                 'lift replaceable capsules onto a permanent frame (Beslioglu 2014, DOI 10.4995/vlc.2014.1829). In '
                 '1971 Renzo Piano, Richard Rogers, and Ove Arup & Partners engineers including Peter Rice won the '
                 'Centre Pompidou competition in Paris (Rice 1994; Hamzeian 2018, DOI 10.1201/9780429506208-91).',
 'act1_plain_bridge': 'Most conventional buildings resemble a sealed desktop computer whose wires and pipes sit inside '
                      'structural walls. When ducts or lab utilities need replacement, workers may have to open walls '
                      'or partitions (Brand 1994). High-tech architects placed columns, ducts, and circulation outside '
                      'the facade instead (Rice 1994). Separating a durable frame from replaceable services builds on '
                      'Open Building support-and-infill thinking (Habraken 2021, DOI 10.4324/9781003014713), so '
                      'interior rooms could stay open for future layouts.',
 'act1_body': "Archigram's drawings are widely seen as an influence on British High-Tech architecture; this folio "
              'does not document direct teaching links to Norman Foster, Richard Rogers, or Jan Kaplický. At the '
              'Centre Pompidou, Peter Rice and the Arup team evolved the cast-steel node from a friction collar into '
              'the gerberette bracket (Hamzeian 2018, DOI 10.1201/9780429506208-91; Rice 1994). Floor trusses bear '
              'on short gerberette arms outside the columns and are tied down at the outer tips. That layout leaves '
              'floors of about 48 m free of interior columns, and Norman Foster later hung floors from masts at HSBC '
              'Hong Kong. For rigid frames, James Clerk Maxwell introduced reciprocal force diagrams (1864, DOI '
              '10.1080/14786446408643663). Calladine (1978, DOI 10.1016/0020-7683(78)90052-5) and Pellegrino and '
              'Calladine (1986, DOI 10.1016/0020-7683(86)90014-4) formalized b − 3j + 6 = s − m for self-stress '
              'states s and mechanisms m. Designers today could model polyhedral frames with compas-dev/compas '
              '(https://github.com/compas-dev/compas; Akbarzadeh, Van Mele, and Block 2015, DOI '
              '10.1016/j.cad.2015.01.006); this folio does not run those tools. Citation context was checked via Scite '
              '(Nicholson et al. 2021, DOI 10.1162/qss_a_00146).',
 'act1_stakes': 'Conventional construction often embeds ducts, pipes, and wiring inside permanent concrete or masonry '
                'elements. Stewart Brand adapted Frank Duffy\'s shearing layers to explain that mismatch: structure '
                'may endure about 30 to 300 years, skin about 20 years, services 7 to 15 years, and space plans 3 to '
                '30 years (Brand 1994). Habraken similarly proposed separating shared supports from changeable infill '
                '(Habraken 2021, DOI 10.4324/9781003014713). Exoskeleton cantilevers also require static and '
                'kinematic checks via Maxwell–Calladine counting (Pellegrino & Calladine 1986, DOI '
                '10.1016/0020-7683(86)90014-4). Without those checks, ties and brackets might slip out of '
                'equilibrium or allow unintended mechanisms.',
 'act2_analogy': 'Everyday analogy: Think of a playground seesaw. An adult sits close to the center pivot on a short '
                 'arm, while a child sits far out on the long arm to balance the load. A gerberette bracket acts as a '
                 'lever seesaw: the floor truss presses on a short inner arm, while an exterior steel tie rod at a '
                 'wider back-span balances that load.',
 'act2_plain_primer': 'The interactive model below controls two geometric lengths of a cast-steel gerberette cantilever '
                      '(Rice 1994; Hamzeian 2018, DOI 10.1201/9780429506208-91). The first slider sets the cantilever '
                      'arm a from the column center to the floor truss bearing. Lengthening a increases the lever arm '
                      'of the interior floor reaction. The second slider sets the back-span c from the column center to '
                      'the exterior tension tie rod. Lengthening c increases the tie rod\'s leverage, reducing the '
                      'model tension T_tie = V_p * (a / c) for a fixed floor reaction V_p and keeping bending out of '
                      'the interior truss.',
 'distill_diagram': {'analogy_title': 'Playground Seesaw Lever Equilibrium',
                     'analogy_sub': 'Short floor lever balanced by long exterior tension tie',
                     'force_a_title': 'Floor Cantilever Arm (a)',
                     'force_a_sub': 'Magnifies floor reaction leverage across the rocker pivot',
                     'force_b_title': 'Tie-Rod Back-Span (c)',
                     'force_b_sub': 'Lengthens cable leverage to balance downward floor load',
                     'threshold_title': 'Maxwell Rigidity & Tie-Rod Yield Bound',
                     'threshold_pass': 'Lever in balance; tie within its assumed capacity (model)',
                     'threshold_fail': 'Tie-rod overload; column flexural hinge; frame collapse'},
 'act2_intuition': 'This high-tech exoskeleton rests on two static ideas. First, the cast-steel gerberette acts as a '
                   'class-one lever pivoting on an exterior steel column (Rice 1994; Hamzeian 2018, DOI '
                   '10.1201/9780429506208-91). A floor reaction V_p acts at cantilever arm a outside the column, and '
                   'an exterior tie rod restrains the outer tip at back-span c, giving T_tie = V_p * (a / c). Column '
                   'compression then becomes C_col = V_p * (1 + a / c). With assumed inputs V_p = 4,800 kN, a = 1.60 m, '
                   'and c = 6.00 m, the model yields T_tie = 1,280 kN and C_col = 6,080 kN. Second, the '
                   'Maxwell–Calladine rule, b − 3j + 6 = s − m (Maxwell 1864, DOI 10.1080/14786446408643663; Calladine '
                   '1978, DOI 10.1016/0020-7683(78)90052-5; Pellegrino & Calladine 1986, DOI '
                   '10.1016/0020-7683(86)90014-4), relates bars and joints to states of self-stress s and mechanisms '
                   'm. This folio assumes m = 0 without computing a frame matrix, and treats SF = 3.12 as an '
                   'illustrative value.',
 'act2_deepening': 'The ratio a / c sets both tie-rod tension and column compression in the lever model. Lengthening '
                   'cantilever arm a increases T_tie linearly for a fixed V_p, so widening back-span c lowers tie '
                   'demand and opens the exterior bay where modular services can sit (Brand 1994). Pinning floor '
                   'trusses to gerberette pivots limits moment transfer into the perimeter columns (Rice 1994). '
                   'Conversely, a tight site that restricts back-span c raises a / c, increasing both tie tension and '
                   'bracket shear demand on cast-steel nodes (Hamzeian 2018, DOI 10.1201/9780429506208-91).',
 'act4_deepening': 'A proposal, not a description of current practice: strain gauges at cast-steel nodes could inform '
                   'a structural model during module swaps, while crane-path simulations could help engineers check '
                   'equilibrium at each step. Combining Habraken\'s support-and-infill split (Habraken 2021, DOI '
                   '10.4324/9781003014713), Brand\'s shearing layers (Brand 1994), and matrix frame checks '
                   '(Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4) might help future facilities '
                   'replace aging service pods without rebuilding the frame. Under the stated assumptions, whether '
                   'that lowers lifecycle cost or downtime remains untested and depends on site details not modeled '
                   'here.',
 'act4_human_ai': "A speculative coda, labeled as such: Ron Herron's Walking City and Peter Cook's Plug-In City "
                  'imagined buildings whose parts could be swapped (Beslioglu 2014, DOI 10.4995/vlc.2014.1829). '
                  'Future frames might use lightweight lattice materials and digital inspection logs to plan module '
                  'replacement. None of this describes current practice, no figures are computed here, and it is not '
                  'an approved medical facility design.'}

PLATE_CAPTION = {'alt': "Conceptual visualization imagining what Archigram's Walking City and Plug-In City combined with British "
        'High-Tech cast-steel gerberette exoskeletons and modular cleanroom pods would look like (artistic impression, '
        'not a measured structure)',
 'caption': 'Conceptual Vision Plate A.04-V (Imagining What It Would Look Like) · Artistic architectural visualization '
            "imagining Ron Herron's Walking City and Peter Cook's Plug-In City realized with cast-steel gerberette "
            'cantilevers, exterior tension tie rods, and crane-plugged modular bio-cleanroom capsules.'}

DISPATCH = {'kicker': 'FRONTIER HIGH-TECH & OPEN-BUILDING DISPATCH · ARCHIGRAM TO MODULAR CLEANROOMS',
 'headline': "From Archigram's 1964 Plug-In Capsules to High-Tech Exoskeletons: A Lever Model of the Gerberette",
 'body': "Connecting Peter Cook & Ron Herron's Archigram Plug-In drawings (1961–1974) with the Centre Pompidou's "
         "cast-steel gerberettes, Norman Foster's HSBC suspended floors, and the Pellegrino–Calladine counting rule "
         'for frameworks (Int. J. Solids Struct. DOI 10.1016/0020-7683(86)90014-4; Calladine DOI '
         '10.1016/0020-7683(78)90052-5), this folio models the gerberette as a lever (T_tie = V_p a/c = 1,280.0 kN for '
         'assumed inputs) and proposes, without claiming any built example, frames whose service modules could be '
         'replaced.'}

META_3D = ('High-Tech Cast-Steel Gerberette Cantilever Truss',
 'X: Column-Free Span & Rocker Fulcrum · Z: Structural Bay · Y: Bending Moment & Tension Tie')

ES_TRANSLATION = {'title_es': 'De las Megaestructuras Plug-In de Archigram a los Exoesqueletos High-Tech: Gerberettes, Marcos '
             'Espaciales de Maxwell y Cápsulas Clínicas',
 'subtitle_es': 'Cómo las ideas de cápsulas enchufables de Archigram suelen verse como una influencia en el High-Tech '
                'británico de Richard Rogers, Renzo Piano, Peter Rice y Norman Foster, y un modelo de palanca de la '
                'gerberette de acero fundido, con módulos de servicios reemplazables como propuesta.',
 'why_es': 'Separar un esqueleto estructural de larga vida de las instalaciones de vida corta podría facilitar, como '
           'propuesta, la actualización de laboratorios y salas clínicas sin demoler el edificio.',
 'plain_es': 'La mayoría de los edificios convencionales se parecen a una computadora sellada donde los cables y '
             'tuberías quedan dentro de muros estructurales. Cuando un edificio requiere renovar conductos o redes '
             'de servicios, las cuadrillas deben abrir muros y tabiques (Brand 1994). La arquitectura High-Tech '
             'invirtió esa lógica al llevar las columnas, ductos y circulaciones hacia el exterior de la fachada '
             '(Rice 1994). Separar la estructura duradera de las instalaciones reemplazables retoma el enfoque de '
             'soporte y relleno de Habraken (DOI 10.4324/9781003014713) para mantener plantas interiores abiertas.',
 'deep_es': 'El modelo de planta libre de unos 48 m en el Centro Pompidou emplea piezas de acero fundido llamadas '
            'gerberettes que evolucionaron de collarines de fricción a ménsulas articuladas (Rice 1994; Hamzeian '
            '2018, DOI 10.1201/9780429506208-91). La losa apoya sobre un brazo corto exterior y un tirante vertical '
            'más alejado equilibra la reacción mediante tensión pura, mientras la regla de Maxwell-Calladine '
            '(DOI 10.1016/0020-7683(86)90014-4) evalúa rigidez y mecanismos. En este modelo, con una reacción '
            'supuesta de 4,800 kN, un brazo de 1.60 m y un tirante a 6.00 m, la tensión del tirante es de 1,280 kN; '
            'el factor de seguridad de 3.12 es ilustrativo y m = 0 se supone, no se calcula. Separar la estructura '
            'de las instalaciones de corta vida es una propuesta apoyada en Brand (1994) y Habraken '
            '(DOI 10.4324/9781003014713).'}
