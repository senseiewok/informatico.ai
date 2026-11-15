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
                           'and Rogers were unsourced and are withdrawn; V_p = 4,800 kN and SF = 3.12 are now labelled '
                           'as assumed and illustrative. The invented 1961 founding scene, a source entry that did not '
                           'exist as cited, and claims about gene-therapy pods and CF wards are replaced by a plain '
                           'account and a modest, labelled proposal.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; Scite found no paper on '
                        'the Pompidou gerberettes, so those details are kept to standard history only.'},
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
 'history_lead': 'Archigram began in London in 1961 as a small magazine. Its core group was Peter Cook, Warren Chalk, '
                 'Dennis Crompton, David Greene, Ron Herron and Michael Webb. Their drawings asked why a building should '
                 "stay fixed when the lives and technology inside it keep changing. In Cook's Plug-In City and Herron's "
                 'Walking City (both 1964), large structural frames carry capsules that cranes could lift in and out. In '
                 '1971 Renzo Piano and Richard Rogers, working with the engineers of Ove Arup & Partners including Peter '
                 'Rice, won the competition for the Centre Pompidou in Paris, a building often described as sharing '
                 "Archigram's spirit of exposed, adaptable structure.",
 'history_body': "Archigram's drawings are widely seen as an influence on British High-Tech architecture; this folio does not document direct teaching links to Team 4 (Norman Foster and Richard Rogers) or to Jan Kaplický's Future Systems. At the Centre Pompidou, the engineering team including Peter Rice used cast-steel brackets called gerberettes that carry the floor trusses on short arms outside the column line and are tied down by slender exterior ties, giving column-free floors of about 48 m. Norman Foster's Hongkong and Shanghai Bank headquarters hangs groups of floors from steel masts. Maxwell's rule for stiff frames, extended by Calladine (DOI 10.1016/0020-7683(78)90052-5) and by Pellegrino and Calladine (DOI 10.1016/0020-7683(86)90014-4), counts bars, joints, states of self-stress s and mechanisms m: b - 3j + 6 = s - m. Designers today could explore such frames with open tools such as compas-dev/compas (https://github.com/compas-dev/compas; see DOI 10.1016/j.cad.2015.01.006 for the underlying graphic statics). This folio does not run those tools.",
 'pullquote': 'What Archigram drew in 1964 as a utopian Plug-In megastructure, Piano, Rogers, Rice, and Foster '
              'engineered in cast steel: pull the structure and mechanical lungs to the outside so the interior floor '
              'plate can evolve forever.',
 'pullquote_cite': "Editorial Synthesis · From Peter Cook & Ron Herron's Archigram (1961–1974) to British High-Tech "
                   "(Pompidou, HSBC & Lloyd's)",
 'chronology': [('1961–1964',
                 'Archigram (Cook, Herron, Chalk, Crompton, Webb, Greene)',
                 'Publish Archigram 1–4, Plug-In City, and Walking City, separating the permanent structural frame '
                 'from clip-on modular capsules.'),
                ('1961–1972',
                 'Cedric Price (Fun Palace) & N. J. Habraken (Supports)',
                 "Formulate cybernetic reconfigurable space frames and Open Building 'Support vs. Infill' structural "
                 'theory.'),
                ('1971–1977',
                 'Renzo Piano, Richard Rogers & Peter Rice (Centre Pompidou)',
                 'Realize an exposed exoskeleton with cast-steel gerberettes, color-coded exterior services and '
                 'column-free floors of about 48 m.'),
                ('1978–1986',
                 "Norman Foster (HSBC Hong Kong) & Richard Rogers (Lloyd's)",
                 'Build mast-suspended floors (HSBC) and exterior service towers with prefabricated service pods '
                 "(Lloyd's)."),
                ('1994',
                 'Stewart Brand',
                 'Publishes How Buildings Learn, describing a building as layers that change at different rates, from '
                 'long-lived structure to short-lived services and space plan.')],
 'intuition_lead': 'The structural mechanics of a high-tech exoskeleton rest on two elegant static principles. First, '
                   'the cast-steel gerberette operates as a moment-free class-one lever pivoting on an exterior '
                   'tubular steel column. By applying the vertical floor reaction V_p at cantilever distance a and '
                   'restraining the outer tip with an exterior vertical tie rod at back-span c, the equilibrium '
                   'tension force resolves precisely to T_tie = V_p * (a / c). This configuration converts intense '
                   'mid-span bending into axial compression down the main column, C_col = V_p * (1 + a / c). With the '
                   'folio\'s assumed V_p = 4,800 kN, a = 1.60 m and c = 6.00 m, T_tie = 1,280 kN and C_col = 6,080 kN. '
                   'Second, the Maxwell-Calladine counting rule, b - 3j + 6 = s - m (Calladine, DOI '
                   '10.1016/0020-7683(78)90052-5; Pellegrino and Calladine, DOI 10.1016/0020-7683(86)90014-4), relates '
                   'bars and joints to states of self-stress s and mechanisms m; a frame with m = 0 has no internal '
                   'mechanism. This folio assumes m = 0 for its frame and does not compute it, and the tie-rod safety '
                   'factor of 3.12 is an illustrative value, not the result of a design check.',
 'intuition_body': 'This folio reads the High-Tech answer to the lifecycle mismatch through two structural ideas. '
                   'First, a perimeter frame can be checked for internal mechanisms with the Maxwell–Calladine counting '
                   'rule (b - 3j + 6 = s - m in 3D; for a simple 2D truss, b = 2j - 3), and carrying loads in a '
                   'perimeter frame or mast-and-gerberette exoskeleton is how the Pompidou keeps its floors free of '
                   'interior columns. Second, by cantilevering the vertical floor reaction V_p at a short gerberette fulcrum distance a '
                   '= 1.60 m outside the column line and anchoring the outer tip with a high-strength tension tie rod '
                   'at distance c = 6.00 m (T_tie = V_p * a / c), bending moment is pulled out of the interior truss '
                   'while leaving an exterior zone where service modules could be placed.',
 'walkthrough': ['Experiment 1 (Trace the Archigram-to-High-Tech Lineage): Click Stages 1 -> 4 in the stepper above to '
                 "follow the path from Peter Cook's 1964 Plug-In City to the Pompidou gerberette lever model, the "
                 "High-Tech masts and service towers, and Stewart Brand's shearing layers.",
                 'Experiment 2 (Move the Lever Arms): Drag the cantilever arm a and the tie back-span c below to see how '
                 'the model tie-rod tension T_tie = V_p · a / c changes for the assumed V_p = 4,800 kN.',
                 'Experiment 3 (Read the Companion Skill): Use the portable SKILL.md below to study the gerberette lever '
                 'formula, the Maxwell-Calladine counting rule and shearing-layer thinking. It is a study aid, not a '
                 'design code.'],
 'human_ai_shift': "A speculative coda, labelled as such: Ron Herron's Walking City and Peter Cook's Plug-In City "
                   'imagined buildings whose parts could be swapped. Future frames might use lightweight lattice '
                   'materials and robots for assembly and inspection, and digital models might help plan which modules '
                   'to replace. None of this is a description of current practice, the folio gives no figures for it, '
                   'and it is not an approved medical facility design.',
 'cf_bridge': 'A modest bridge, and a proposal. Infection prevention practice in Cystic Fibrosis care, including '
              'separating patients from one another, is set out in clinical guidance (Saiman et al. 2014, '
              '\'Infection Prevention and Control Guideline for Cystic Fibrosis: 2013 Update\', DOI 10.1086/676882). '
              'Clinical needs change over a building\'s life, so a frame that keeps services replaceable could make it '
              'easier to adapt rooms later. This folio designs no clinical room, reports no outcome, and is not '
              'medical or infection-control advice; people with CF should follow their care team.',
 'sources': ['Cook, P., Chalk, W., Crompton, D., Greene, D., Herron, R., & Webb, M. (1961–1974 / 1999). Archigram. '
             'Princeton Architectural Press.',
             'Rice, P. (1994). An Engineer Imagines. Artemis, London.',
             'Calladine, C. R. (1978). Buckminster Fuller\'s "Tensegrity" structures and Clerk Maxwell\'s rules for the '
             'construction of stiff frames. International Journal of Solids and Structures, 14(2), 161–172. DOI: '
             '10.1016/0020-7683(78)90052-5.',
             'Saiman, L., et al. (2014). Infection Prevention and Control Guideline for Cystic Fibrosis: 2013 Update. '
             'Infection Control & Hospital Epidemiology, 35(S1), S1–S67. DOI: 10.1086/676882.',
             'Pellegrino, S., & Calladine, C. R. (1986). Matrix analysis of statically and kinematically indeterminate '
             'frameworks. International Journal of Solids and Structures, 22(4), 409–428. DOI: '
             '10.1016/0020-7683(86)90014-4.',
             "Brand, S. (1994). How Buildings Learn: What Happens After They're Built. Viking Press.",
             'Akbarzadeh, M., Van Mele, T., & Block, P. (2015). On the equilibrium of funicular polyhedral frames and '
             'convex polyhedral force diagrams. Computer-Aided Design, 63, 118–128. DOI: 10.1016/j.cad.2015.01.006. '
             '(Cited for graphic statics; compas-dev/compas, https://github.com/compas-dev/compas, is a separate '
             'open-source framework.)'],
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
        '            <text x="215" y="62" font-size="11" font-weight="700" fill="var(--tp-prussian)">100% Column-Free '
        'Clear Span (48.0 m)</text>\n'
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
 'act1_dropcap': 'Archigram began in London in 1961 as a small magazine. Its core group was Peter Cook, Warren Chalk, '
                 'Dennis Crompton, David Greene, Ron Herron and Michael Webb. Their drawings asked why a building should '
                 "stay fixed when the lives and technology inside it keep changing. In Cook's Plug-In City and Herron's "
                 'Walking City (both 1964), large structural frames carry capsules that cranes could lift in and out. In '
                 '1971 Renzo Piano and Richard Rogers, working with the engineers of Ove Arup & Partners including Peter '
                 'Rice, won the competition for the Centre Pompidou in Paris, a building often described as sharing '
                 "Archigram's spirit of exposed, adaptable structure.",
 'act1_plain_bridge': 'Most conventional buildings resemble old desktop computers where all the delicate chips, pipes, '
                      'and wiring are glued permanently inside concrete walls. If a hospital needs to upgrade its '
                      'ventilation ducts or install modern medical technology twenty years later, workers have to tear '
                      'down walls or demolish the whole building. British high-tech architects inverted this logic by '
                      "pushing the building's skeleton and mechanical guts onto the outside of the facade. By perching "
                      'the structural columns outside and hanging elevators, water pipes, and air conditioning on the '
                      'exterior, the interior rooms become wide, completely open halls without a single column in the '
                      'way. Because the inside space is completely uncluttered, rooms can be reconfigured over a '
                      'weekend. When specialized clinic capsules or cleanrooms wear out, a service crane can simply '
                      'unbolt the old pod and plug in a brand-new module without disrupting the rest of the facility.',
 'act1_body': "Archigram's drawings are widely seen as an influence on British High-Tech architecture; this folio does not document direct teaching links to Team 4 (Norman Foster and Richard Rogers) or to Jan Kaplický's Future Systems. At the Centre Pompidou, the engineering team including Peter Rice used cast-steel brackets called gerberettes that carry the floor trusses on short arms outside the column line and are tied down by slender exterior ties, giving column-free floors of about 48 m. Norman Foster's Hongkong and Shanghai Bank headquarters hangs groups of floors from steel masts. Maxwell's rule for stiff frames, extended by Calladine (DOI 10.1016/0020-7683(78)90052-5) and by Pellegrino and Calladine (DOI 10.1016/0020-7683(86)90014-4), counts bars, joints, states of self-stress s and mechanisms m: b - 3j + 6 = s - m. Designers today could explore such frames with open tools such as compas-dev/compas (https://github.com/compas-dev/compas; see DOI 10.1016/j.cad.2015.01.006 for the underlying graphic statics). This folio does not run those tools.",
 'act1_stakes': 'Traditional institutional construction buries electrical conduits, drainage stacks, and heavy '
                'ventilation ducts deep inside reinforced concrete floor slabs and structural masonry partitions. '
                'While this traditional approach simplifies initial exterior waterproofing, it creates a fatal '
                "lifecycle trap that architect Stewart Brand identified as pace layering failure. A building's "
                'concrete structural frame easily lasts a century, but interior office layouts shift every three '
                'years, and high-intensity clinical heating, ventilation, and air conditioning systems require '
                'complete replacement after fifteen years. When mechanical ducts are entombed in structural concrete, '
                'updating a surgical suite or research laboratory requires jackhammers, building-wide asbestos '
                'abatement, and months of catastrophic downtime. Furthermore, attempting to push structures outward '
                'into long-span cantilevers without rigorous kinematic analysis risks sudden instability: if an '
                'exterior rocker arm or tension tie slips out of equilibrium, the unbraced perimeter frame can '
                'experience severe eccentric twisting, causing floor trusses to deflect excessively or snap connection '
                'bolts.',
 'act2_analogy': 'Everyday analogy: Think of a playground seesaw. A parent sits close to the center pivot on a short '
                 'lever arm, while a child sits far out on the opposite long arm. Because the child sits much further '
                 'from the fulcrum, the child easily balances the heavier adult. A high-tech gerberette acts as this '
                 'exact seesaw: the heavy floor beam presses on the short inner arm, while an exterior steel tension '
                 'cable anchored far away balances the colossal load effortlessly.',
 'act2_plain_primer': 'In the interactive laboratory below, you manipulate the mechanical balance of a high-tech '
                      'cast-steel gerberette cantilever. The first slider adjusts the length of the short cantilever '
                      'arm that reaches from the vertical column out to the floor truss fulcrum. Moving this arm '
                      'outward increases the leverage that the massive interior floor plate exerts against the '
                      "building's perimeter. The second slider changes the back-span distance to the exterior tension "
                      'tie-rod, which anchors the outer tip of the steel bracket to the ground. When you lengthen this '
                      'back-span, you increase the mechanical advantage of the tension cable, allowing a relatively '
                      'slender steel rod to restrain immense interior floor weights. By tuning these two levers in '
                      'harmony, you balance the seesaw perfectly. This balance neutralizes rotational bending on the '
                      'main column, keeps the interior completely column-free, and leaves clear exterior space where '
                      'cranes can plug in modular mechanical capsules.',
 'distill_diagram': {'analogy_title': 'Playground Seesaw Lever Equilibrium',
                     'analogy_sub': 'Short floor lever balanced by long exterior tension tie',
                     'force_a_title': 'Floor Cantilever Arm (a)',
                     'force_a_sub': 'Magnifies floor reaction leverage across the rocker pivot',
                     'force_b_title': 'Tie-Rod Back-Span (c)',
                     'force_b_sub': 'Lengthens cable leverage to balance colossal downward load',
                     'threshold_title': 'Maxwell Rigidity & Tie-Rod Yield Bound',
                     'threshold_pass': 'Lever in balance; tie within its assumed capacity (model)',
                     'threshold_fail': 'Tie-rod overload; column flexural hinge; frame collapse'},
 'act2_intuition': 'The structural mechanics of a high-tech exoskeleton rest on two elegant static principles. First, '
                   'the cast-steel gerberette operates as a moment-free class-one lever pivoting on an exterior '
                   'tubular steel column. By applying the vertical floor reaction V_p at cantilever distance a and '
                   'restraining the outer tip with an exterior vertical tie rod at back-span c, the equilibrium '
                   'tension force resolves precisely to T_tie = V_p * (a / c). This configuration converts intense '
                   'mid-span bending into axial compression down the main column, C_col = V_p * (1 + a / c). With the '
                   'folio\'s assumed V_p = 4,800 kN, a = 1.60 m and c = 6.00 m, T_tie = 1,280 kN and C_col = 6,080 kN. '
                   'Second, the Maxwell-Calladine counting rule, b - 3j + 6 = s - m (Calladine, DOI '
                   '10.1016/0020-7683(78)90052-5; Pellegrino and Calladine, DOI 10.1016/0020-7683(86)90014-4), relates '
                   'bars and joints to states of self-stress s and mechanisms m; a frame with m = 0 has no internal '
                   'mechanism. This folio assumes m = 0 for its frame and does not compute it, and the tie-rod safety '
                   'factor of 3.12 is an illustrative value, not the result of a design check.',
 'act2_deepening': 'The mathematical interaction between cantilever arm a and back-span c dictates the internal stress '
                   'state of the entire building skeleton. As the cantilever arm a is lengthened, the downward floor '
                   'load pivots further away from the column center, causing tie-rod tension T_tie to increase in '
                   'direct linear proportion. To avoid excessive tension steel or foundation uplift piles, the '
                   'back-span c must be widened, which pushes the exterior facade zone outward. This geometric '
                   "trade-off directly governs Stewart Brand's shearing layer decoupling: the outer structural bay "
                   'provides a dedicated structural zone for external elevators, color-coded ductwork, and modular '
                   'laboratory capsules. Because the floor trusses transmit negligible bending moment into the '
                   'columns, changes to floor stiffness do not alter global wind-drift resistance. However, if the '
                   'tie-rod back-span c is restricted by narrow site boundaries, the lever ratio a/c spikes, '
                   'escalating column compression and demanding heavy cast-steel pearlitic brackets capable of '
                   'resisting severe shear stresses without brittle winter fracture.',
 'act4_deepening': 'A proposal, not a description of current practice: a building model linked to strain gauges in '
                   'cast-steel nodes could track how loads shift when modules are swapped, and crane-path simulations '
                   'could help check that removing one module does not unbalance the exterior frame, with an engineer '
                   'signing off each step. An open research challenge involves autonomous robotic maintenance swarms: can magnetic climbing '
                   'robots and aerial drones continuously inspect tension tie-rods, detect microscopic fatigue cracks, '
                   'and apply corrosion-resistant coatings in situ? If so, adaptable frames might last longer '
                   'before major rebuilding; that remains a hope, not a result.',
 'act4_human_ai': "A speculative coda, labelled as such: Ron Herron's Walking City and Peter Cook's Plug-In City "
                  'imagined buildings whose parts could be swapped. Future frames might use lightweight lattice '
                  'materials and robots for assembly and inspection, and digital models might help plan which modules '
                  'to replace. None of this is a description of current practice, the folio gives no figures for it, '
                  'and it is not an approved medical facility design.'}

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
 'bridge_es': 'Las prácticas de prevención de infecciones en la atención de la Fibrosis Quística las fijan guías '
              'clínicas (Saiman et al. 2014, DOI 10.1086/676882). Esta ficha solo propone estructuras más fáciles de '
              'adaptar; no diseña salas clínicas ni es consejo médico.',
 'plain_es': 'La mayoría de los edificios convencionales se parecen a una vieja computadora de escritorio donde todos '
             'los cables, tuberías y circuitos están pegados con pegamento dentro de paredes de concreto. Cuando un '
             'hospital necesita renovar sus conductos de ventilación o instalar equipo médico moderno veinte años '
             'después, los trabajadores tienen que demoler muros y paralizar las actividades. Los arquitectos del '
             'movimiento High-Tech británico cambiaron esta lógica por completo al colocar el esqueleto estructural y '
             'las instalaciones mecánicas en el exterior de la fachada. Al situar las columnas afuera y colgar '
             'elevadores, tuberías y aire acondicionado en el perímetro, los pisos interiores se convierten en salones '
             'inmensos totalmente libres de columnas. Este espacio despejado permite reorganizar consultorios en un '
             'fin de semana. Además, cuando un quirófano o laboratorio se vuelve obsoleto, una grúa puede desconectar '
             'el módulo antiguo y enchufar una cápsula nueva sin afectar el resto del edificio, asegurando una '
             'adaptabilidad continua frente a las necesidades humanas.',
 'deep_es': 'El principio estático que hace posible estas plantas libres de cuarenta y ocho metros es la gerberette de '
            'acero fundido, que funciona como un balancín de palanca apoyado sobre las columnas exteriores. La pesada '
            'losa del piso presiona sobre un brazo corto, mientras que un tirante vertical exterior anclado a mayor '
            'distancia equilibra la carga mediante tensión pura. Esta disposición cancela los momentos de flexión en '
            'las columnas interiores y concentra las cargas de gravedad en un exoesqueleto perimetral gobernado por el '
            'conteo de rigidez de Maxwell-Calladine. En el modelo de esta ficha, con una reacción supuesta de 4,800 kN, '
            'un brazo de 1.60 m y un tirante a 6.00 m, la tensión del tirante es de 1,280 kN; el factor de seguridad de '
            '3.12 es ilustrativo y el índice de mecanismos m = 0 se supone, no se calcula. Separar la estructura '
            'permanente de las instalaciones de corta vida podría, como propuesta, facilitar la adaptación de '
            'laboratorios y salas clínicas.'}
