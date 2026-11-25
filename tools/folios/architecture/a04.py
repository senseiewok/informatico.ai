#!/usr/bin/env python3
"""Folio A.04 (ARCHITECTURE): From Archigram's Plug-In Megastructures to British High-Tech Exoskeletons: Gerberette Cantilevers, Maxwell Space Frames & Shearing-Layer Pods."""
from __future__ import annotations

SLUG = 'a04'

PILLAR = 'architecture'

_SCITE_RECORD = {
    'doi': '10.1016/0020-7683(86)90014-4',
    'fetched_on': '2026-11-08',
    'citing_publications': 833,
    'supporting': 1,
    'mentioning': 499,
    'contrasting': 0,
    'retracted': False,
    'summary': (
        'Scite index entry [observed: Scite ML citation classification, accessed 2026-11-08] for '
        'Pellegrino & Calladine, Matrix analysis of statically and kinematically indeterminate '
        'frameworks (DOI 10.1016/0020-7683(86)90014-4): 833 citing publications (distinct from '
        'statement tallies: 1 supporting, 499 mentioning, 0 contrasting) and no retraction notice. '
        "That paper analyzes pin-jointed framework matrices; it says nothing about gerberettes or this folio's assumed numbers."
    ),
}

FOLIO = {
    'folio_id': 'A.04',
    'slug': 'a04',
    'pillar': 'architecture',
    'category_code': 'A',
    'title': (
        "From Archigram's Plug-In Megastructures to British High-Tech Exoskeletons: Gerberette "
        'Cantilevers, Maxwell Space Frames & Shearing-Layer Pods'
    ),
    'subtitle': (
        'An architectural and statics explanation, not a structural design method: from '
        "Archigram's 1960s plug-in drawings to the Centre Pompidou cast-steel gerberette lever "
        'and replaceable service modules; no number here may be used on a real structure.'
    ),
    'date_published': '2026-11-01',
    'date_redated': '2026-11-14',
    'current_edition': 'REV 1.3',
    'status_badge': 'HIGH-TECH & ARCHIGRAM · REV 1.3',
    'primary_kernel': 'tools/folios/architecture/a04.py',
    'kernel_verdict': 'Not independently verified',
    'kernel_verdict_es': 'Sin verificación independiente',
    'governing_law': 'T_tie = V_p · (a / c) · b − 3j + 6 = s − m · τ_pod ≪ τ_frame',
    'colophon': {
        'identifier': 'A.04 · Archigram to High-Tech Exoskeletons · Teaching Model',
        'kernels': 'Gerberette Lever T_tie = V_p(a/c) · Maxwell-Calladine Count · Shearing Layers',
        'benchmarks': (
            'Assumed & illustrative values: T_tie = 4,800 × 1.60 / 6.00 = 1,280.0 kN '
            '(V_p assumed) · SF = 3.12 illustrative'
        ),
        'bridge': 'Durable Perimeter Frame + Replaceable Services (Untested Proposal)',
    },
    'sliders': [
        {
            'label': 'Gerberette Cantilever Arm (a)',
            'min': 0.8,
            'max': 2.6,
            'step': 0.05,
            'value': 1.6,
            'unit': ' m',
        },
        {
            'label': 'Exterior Tie-Rod Back-Span (c)',
            'min': 3.5,
            'max': 8.5,
            'step': 0.1,
            'value': 6.0,
            'unit': ' m',
        },
    ],
    'steps': [
        (
            "Stage 1 (Archigram Plug-In Matrix, 1961–1964): Cook's Plug-In City and Herron's "
            'Walking City depict a frame carrying replaceable capsules (Beslioglu 2014, DOI '
            '10.4995/vlc.2014.1829; the 100-year and 15-year lifetimes are fixed illustrative '
            'values).'
        ),
        (
            'Stage 2 (Pompidou Gerberette Lever, 1971–1977): Under the stated assumptions '
            '(V_p = 4,800 kN, a = 1.60 m, c = 6.00 m), T_tie = V_p·(a/c) = 1,280.0 kN and '
            'C_col = 6,080.0 kN (illustrative values, not real building loads).'
        ),
        (
            'Stage 3 (Foster & Rogers Perimeter Structure, 1978–1986): Norman Foster (HSBC Hong '
            "Kong) hangs floors from masts, and Richard Rogers (Lloyd's) places service towers "
            'outside main floor plates.'
        ),
        (
            "Stage 4 (Brand's Shearing Layers): Stewart Brand (1994) separates long-lived frames "
            'from faster-aging services; placing replaceable service pods outside the frame could '
            'remain an untested architectural proposal.'
        ),
    ],
    'readouts': [
        {'label': 'Exoskeleton Clear Span (Reported)', 'value': 'About 48 m (fixed reference text)'},
        {'label': 'Gerberette Tie-Rod Tension (Model)', 'value': '1,280.0 kN (SF = 3.12, illustrative)'},
        {'label': 'Shearing-Layer Ratio (Illustrative)', 'value': 'τ_pod = 15 yr / τ_frame = 100 yr (fixed text)'},
        {'label': 'Rigidity & Surrogate Tie Check', 'value': 'm = 0 assumed (fixed) · SF ≥ 1.50 (illustrative)'},
    ],
    'sidenote_1': {
        'kicker': 'SIDENOTE A.04-A · ARCHIGRAM, POMPIDOU & UNDOCUMENTED LINKS',
        'body': (
            "Archigram's 1960s issues explored plug-in frames (Cook et al. 1999; Beslioglu "
            '2014, DOI 10.4995/vlc.2014.1829). This folio documents no direct teaching link '
            "between Archigram and Team 4 (Foster and Rogers) or Jan Kaplický's Future Systems."
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE A.04-B · CONCEPT NOTE · CSI 05 12 13 (NOT A SPEC)',
        'body': (
            'Untested concept sketch, not a structural specification: cast-steel brackets '
            '(illustrative f_y = 355 MPa, Charpy 40 J at −20 °C), exterior tie rods, and '
            'detachable risers. No number here may be used on a real structure.'
        ),
    },
    'skill': {
        'filename': 'archigram-hightech-exoskeleton-SKILL.md',
        'name': 'archigram-hightech-exoskeleton',
        'description': (
            'Explanatory architectural and statics reference (not a structural design method) for '
            'cast-steel gerberette lever equilibrium, the Maxwell-Calladine counting rule, and '
            'Stewart Brand shearing layers; no number here may be used on a real structure.'
        ),
        'rules': [
            (
                'Explanatory, untested model only, not a structural design method (no number here '
                'may be used on a real structure): under assumed V_p = 4,800 kN, compute '
                'T_tie = V_p * (a / c) and C_col = V_p * (1 + a / c), with browser surrogate '
                'SF = 3.12 * (1,280 / max(100, T_tie)) flagging SF < 1.50 above 2,662.4 kN.'
            ),
            (
                'State the 3D Maxwell-Calladine count b - 3j + 6 = s - m (Pellegrino & Calladine '
                '1986, DOI 10.1016/0020-7683(86)90014-4); here m = 0, about 48 m clear span, and '
                '15 yr / 100 yr lifetimes remain fixed reference text, not verified matrix outputs.'
            ),
            (
                'Treat separating shorter-lived services (about 7-15 yr in Brand 1994) from '
                'long-lived structure (about 30-300 yr in Brand 1994; Habraken 2021, DOI '
                '10.4324/9781003014713) as an untested concept caveat, not a facility code.'
            ),
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.3',
            'date': '2026-11-14',
            'summary': (
                'REV 1.3 (Redated 2026-11-14): Grounding revision. Earlier PASS and COMPAS claims '
                'and unsourced mentorship claims are withdrawn; V_p = 4,800 kN and SF = 3.12 are '
                'labeled assumed and illustrative, fixed readouts and the 2,662.4 kN surrogate '
                'threshold are stated, and the non-design-method boundary is set across Act I, '
                'Spanish summary, and SKILL.md.'
            ),
            'opus': (
                'Review: references checked in Crossref and Scite; Hamzeian (2018, DOI '
                '10.1201/9780429506208-91) documents the Pompidou cast node, and lever estimates '
                'follow under the stated assumptions.'
            ),
        },
        {
            'edition': 'REV 1.2',
            'date': '2026-11-02',
            'summary': (
                'REV 1.2 (Redated 2026-11-02): Revised the cast-steel gerberette lever model and '
                'Stewart Brand shearing-layer discussion.'
            ),
            'opus': (
                "Cross-model check (Gemini 4 Argon + Qwen 3.8 27B); earlier 'verified' wording "
                'withdrawn in REV 1.3 because T_tie, SF = 3.12, and m = 0 were not verified.'
            ),
        },
        {
            'edition': 'REV 1.1',
            'date': '2026-11-01',
            'summary': (
                'REV 1.1 (Redated 2026-11-01): Initial 5-Act monograph from Archigram to British '
                'High-Tech with a gerberette lever model.'
            ),
            'opus': (
                "Cross-model check (Gemini 4 Argon + Qwen 3.8 27B); earlier 'verified' wording "
                'withdrawn in REV 1.3.'
            ),
        },
    ],
    'volume': 2,
    'volume_code': 'VOL. 02',
    'reading_time': '21 MIN READ',
    'word_count': '~4,530 WORDS',
    'scite': _SCITE_RECORD,
}

LONGFORM_DATA = {
    'reading_time': '21 MIN READ',
    'word_count': '~4,530 WORDS',
    'scite': _SCITE_RECORD,
    'history_lead': (
        'In London in 1961, Peter Cook, David Greene, and Michael Webb published the first '
        'broadsheet issue of Archigram, and Warren Chalk, Dennis Crompton, and Ron Herron joined '
        'the group by 1963. Brick walls stayed rigid while city life kept shifting. In 1964, Cook '
        'drew Plug-In City and Herron drew Walking City, picturing cranes lifting replaceable '
        'living capsules onto a durable steel frame. Seven years later in Paris, Renzo Piano, '
        'Richard Rogers, and engineer Peter Rice won the Centre Pompidou competition. Outside the '
        'recessed glass facade, cast-steel brackets pivoted on perimeter columns, supporting floor '
        'trusses on short inner arms while exterior tension rods anchored their outer tips. '
        'Stairs, water pipes, and air ducts moved onto the building perimeter. This folio is an '
        'explanation, not a structural design method, and none of its numbers may be used on a '
        'real structure.'
    ),
    'history_body': (
        "Archigram's 1961–1974 issues pictured durable frames carrying replaceable parts (Cook "
        'et al. 1999; Beslioglu 2014, DOI 10.4995/vlc.2014.1829); direct teaching links to Foster, '
        'Rogers, or Kaplický are not yet documented here. At the Centre Pompidou, Rice and Arup '
        'evolved a friction collar into the cast-steel gerberette, leaving floors of about 48 m '
        'column-free (Rice 1994; Hamzeian 2018, DOI 10.1201/9780429506208-91). Maxwell (1864, DOI '
        '10.1080/14786446408643663) gave bar-count rules for stiff frames, and Calladine (1978, '
        'DOI 10.1016/0020-7683(78)90052-5) with Pellegrino & Calladine (1986, DOI '
        '10.1016/0020-7683(86)90014-4) extended them to b − 3j + 6 = s − m. Readers could '
        'simulate frames in compas-dev/compas (https://github.com/compas-dev/compas; Akbarzadeh '
        'et al. 2015, DOI 10.1016/j.cad.2015.01.006); this folio is an untested explanation, not '
        'a design method, and no number here may be used on a real structure.'
    ),
    'pullquote': (
        'Archigram drew replaceable capsules in 1964 (Beslioglu 2014, DOI 10.4995/vlc.2014.1829); '
        'at the Centre Pompidou, Piano, Rogers, and Rice placed gerberettes and ducts outside so '
        'floors of about 48 m stayed open (Rice 1994; Hamzeian 2018, DOI 10.1201/9780429506208-91).'
    ),
    'pullquote_cite': 'Editorial Synthesis · Archigram (1964) to Centre Pompidou (1977) & Brand (1994)',
    'chronology': [
        (
            '1961–1964',
            'Archigram (Cook, Herron, Chalk, Crompton, Webb, Greene)',
            'Publish Archigram 1–4, Plug-In City, and Walking City, separating frame from '
            'capsules (Cook et al. 1999; Beslioglu 2014, DOI 10.4995/vlc.2014.1829).',
        ),
        (
            '1961–1972',
            'Cedric Price (Fun Palace) & N. J. Habraken (Supports)',
            'Propose reconfigurable matrices (Mathews 2006, DOI 10.1111/j.1531-314x.2006.00032.x) '
            'and shared supports with changeable infill (Habraken 2021, DOI 10.4324/9781003014713).',
        ),
        (
            '1971–1977',
            'Renzo Piano, Richard Rogers & Peter Rice (Centre Pompidou)',
            'Develop cast-steel gerberettes and exterior ducts around floors of about 48 m '
            '(Rice 1994; Hamzeian 2018, DOI 10.1201/9780429506208-91).',
        ),
        (
            '1978–1986',
            "Norman Foster (HSBC Hong Kong) & Richard Rogers (Lloyd's)",
            "Hang floors from masts (HSBC) and place service towers outside floor plates (Lloyd's).",
        ),
        (
            '1994',
            'Stewart Brand',
            "Publishes How Buildings Learn, adapting Duffy's shearing layers for structure "
            '(about 30–300 yr) and services (about 7–15 yr; Brand 1994).',
        ),
    ],
    'intuition_lead': (
        'Two static relations frame this explanation under the stated assumptions. First, the '
        'gerberette pivots on an exterior column as a lever (Rice 1994; Hamzeian 2018, DOI '
        '10.1201/9780429506208-91): assumed V_p = 4,800 kN at arm a and tie back-span c gives '
        'T_tie = V_p · (a / c) and C_col = V_p · (1 + a / c), or 1,280.0 kN and 6,080.0 kN at '
        'a = 1.60 m, c = 6.00 m. Over a in [0.80, 2.60] m and c in [3.50, 8.50] m, estimated '
        'T_tie spans 451.8 to 3,565.7 kN while surrogate SF = 3.12 × (1,280 / max(100, T_tie)) '
        'flags SF < 1.50 above 2,662.4 kN (a / c > 0.555). Second, b − 3j + 6 = s − m '
        '(Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4) is not verified by '
        'matrix calculation here: m = 0, about 48 m span, and 15 yr / 100 yr remain fixed '
        'reference text.'
    ),
    'intuition_body': (
        'In 3D pin-jointed frames, b − 3j + 6 = s − m relates bar count to self-stress and '
        'mechanisms (Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4). Perimeter '
        'columns leave interior floors open, as at the Centre Pompidou (Rice 1994), while '
        'anchoring back-span c shifts bending to exterior tie pull and could leave room for '
        'replaceable ducts (Brand 1994; Habraken 2021, DOI 10.4324/9781003014713).'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Step Through Four Stages): Select buttons 1 through 4 in the stage '
            "stepper above to move from Cook's 1964 Plug-In City to the Pompidou gerberette lever, "
            "exterior masts, and Brand's shearing layers."
        ),
        (
            'Experiment 2 (Sweep Lever Arms & Surrogate Alert): Drag Gerberette Cantilever Arm a '
            '(0.80–2.60 m) and Exterior Tie-Rod Back-Span c (3.50–8.50 m). Estimated T_tie spans '
            '451.8 kN (SF = 8.84) to 3,565.7 kN (SF = 1.12), crossing SF < 1.50 above 2,662.4 kN '
            '(at a = 1.95 m, c = 3.50 m, T_tie = 2,674.3 kN, SF = 1.49), while about 48 m, '
            '15 yr / 100 yr, and m = 0 stay fixed text.'
        ),
        (
            'Experiment 3 (Read the Companion Skill): Download archigram-hightech-exoskeleton '
            'SKILL.md below as an explanatory caveat sheet, not a structural design method.'
        ),
    ],
    'human_ai_shift': (
        "Speculative note: Cook's Plug-In City and Herron's Walking City imagined swappable "
        'capsules (Beslioglu 2014, DOI 10.4995/vlc.2014.1829). Future teams might pair sensors '
        'with maintenance logs to plan riser swaps; nothing here is simulated, tested, or '
        'approved for real buildings.'
    ),
    'sources': [
        'Maxwell, J. C. (1864). XLV. On reciprocal figures and diagrams of forces. The London, Edinburgh, and '
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
        '882–898. DOI: 10.1162/qss_a_00146.',
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Archigram Plug-In Megastructure to '
        'British High-Tech Exoskeleton Gerberette & Shearing Layers">\n'
        '            <rect id="tp-a04-bay" x="175" y="34" width="330" height="145" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="2.5"/>\n'
        '            <path id="tp-a04-truss-1" data-custom-curve="1" class="tp-svg-flow-line" d="M 175 82 Q 340 86 505 82" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="2.5" stroke-dasharray="6,4"/>\n'
        '            <path id="tp-a04-truss-2" data-custom-curve="1" class="tp-svg-flow-line" d="M 175 130 Q 340 134 505 130" fill="none" '
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
        '            <text x="205" y="110" font-size="10.5" fill="currentColor">Open Interior Space Plan '
        '(Brand τ = 3–30 yr)</text>\n'
        '            <text x="205" y="158" font-size="10.5" fill="currentColor">Perimeter Exoskeleton Mast &amp; Truss '
        '(Illustrative τ = 100 yr)</text>\n'
        '            <text x="22" y="110" font-size="10" fill="var(--tp-minium)">Gerberette + Tie</text>\n'
        '            <text x="546" y="34" font-size="10" font-weight="700" fill="var(--tp-verdigris)">Service '
        'Pods</text>\n'
        '            <text id="tp-a04-svg-label" x="135" y="206" font-size="11" fill="currentColor">Exoskeleton model '
        '· T_tie = 1,280 kN (assumed V_p = 4,800 kN)</text>\n'
        '          </svg>'
    ),
    'act1_dropcap': (
        'In London in 1961, Peter Cook, David Greene, and Michael Webb published the first '
        'broadsheet issue of Archigram, and Warren Chalk, Dennis Crompton, and Ron Herron joined '
        'the group by 1963. Brick walls stayed rigid while city life kept shifting. In 1964, Cook '
        'drew Plug-In City and Herron drew Walking City, picturing cranes lifting replaceable '
        'living capsules onto a durable steel frame. Seven years later in Paris, Renzo Piano, '
        'Richard Rogers, and engineer Peter Rice won the Centre Pompidou competition. Outside the '
        'recessed glass facade, cast-steel brackets pivoted on perimeter columns, supporting floor '
        'trusses on short inner arms while exterior tension rods anchored their outer tips. '
        'Stairs, water pipes, and air ducts moved onto the building perimeter. This folio is an '
        'explanation, not a structural design method, and none of its numbers may be used on a '
        'real structure.'
    ),
    'act1_plain_bridge': (
        'Conventional buildings may resemble a sealed desktop computer whose wires and water '
        'pipes hide inside load-bearing walls. Aged ducts force repair crews to open partitions. '
        'Moving columns, braces, and service shafts outside the glass wall turns that layout '
        'inside out. Heavy steel frames can stand for many decades while pipes and room layouts '
        'change far sooner. At each floor edge, a pivoted steel bracket balances interior floor '
        'weight against an outer vertical tension rod. Wide interior halls then stay clear of '
        'intermediate columns. Galleries, offices, and workrooms could shift layouts without '
        'cutting primary steel, though real retrofits still face local building constraints. '
        'Housing studies likewise separate shared supports from changeable interior rooms. Every '
        'figure here is an untested explanation, not a structural design method, and none may be '
        'used on a real structure.'
    ),
    'act1_body': (
        "Archigram's 1961–1974 issues pictured durable frames carrying replaceable parts (Cook "
        'et al. 1999; Beslioglu 2014, DOI 10.4995/vlc.2014.1829); direct teaching links to Foster, '
        'Rogers, or Kaplický are not yet documented here. At the Centre Pompidou, Rice and Arup '
        'evolved a friction collar into the cast-steel gerberette, leaving floors of about 48 m '
        'column-free (Rice 1994; Hamzeian 2018, DOI 10.1201/9780429506208-91). Maxwell (1864, DOI '
        '10.1080/14786446408643663) gave bar-count rules for stiff frames, and Calladine (1978, '
        'DOI 10.1016/0020-7683(78)90052-5) with Pellegrino & Calladine (1986, DOI '
        '10.1016/0020-7683(86)90014-4) extended them to b − 3j + 6 = s − m; Scite citation '
        'tallies here use Nicholson et al. (2021, DOI 10.1162/qss_a_00146). Readers could '
        'simulate frames in compas-dev/compas (https://github.com/compas-dev/compas; Akbarzadeh '
        'et al. 2015, DOI 10.1016/j.cad.2015.01.006); this folio is an untested explanation, not '
        'a design method, and no number here may be used on a real structure.'
    ),
    'act1_stakes': (
        "Embedding ducts, pipes, and wiring in masonry or concrete ties short-lived utilities to "
        "long-lived structure. Brand adapted Duffy's shearing layers: structure may endure about "
        '30 to 300 years, skin about 20 years, services about 7 to 15 years, and space plans '
        'about 3 to 30 years (Brand 1994), consistent with Habraken on supports and infill '
        '(Habraken 2021, DOI 10.4324/9781003014713). Without Maxwell–Calladine checks '
        '(Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4), cantilevers might '
        'allow unintended mechanisms.'
    ),
    'act2_analogy': (
        'On a playground seesaw, an adult sitting close to the pivot balances a child sitting '
        'farther out. A gerberette bracket uses that lever idea: the floor truss bears on a short '
        'inner arm while an exterior tie rod holds down the outer tip. Where the comparison '
        'stops: a wooden seesaw is one plank on a pin, whereas a cast bracket resists shear and '
        'torsion and a 3D frame could sway sideways without bracing.'
    ),
    'act2_plain_primer': (
        'Two sliders drive the lever estimate below under the stated assumptions. Gerberette '
        'Cantilever Arm sets the inner distance from column pivot to floor bearing, from about '
        '0.8 to 2.6 meters; lengthening it raises pull on the outer tie. Exterior Tie-Rod '
        'Back-Span sets the outer distance to the tie rod, from about 3.5 to 8.5 meters; '
        'widening it lowers tie pull, while clear span, lifetimes, and zero mechanisms remain '
        'fixed text.'
    ),
    'distill_diagram': {
        'analogy_title': 'Playground Seesaw Lever Equilibrium',
        'analogy_sub': 'Short floor lever balanced by long exterior tension tie',
        'force_a_title': 'Gerberette Cantilever Arm (a)',
        'force_a_sub': 'Lengthens floor-reaction lever arm across the column pivot',
        'force_b_title': 'Exterior Tie-Rod Back-Span (c)',
        'force_b_sub': 'Widens outer tie leverage to reduce downward balancing pull',
        'threshold_title': 'Surrogate Tie Ratio (SF >= 1.50, Illustrative)',
        'threshold_pass': 'Model tie tension at or below 2,662.4 kN (illustrative SF >= 1.50)',
        'threshold_fail': 'Surrogate SF < 1.50 above 2,662.4 kN (untested alert, not a code check)',
    },
    'act2_intuition': (
        'Two static relations frame this explanation under the stated assumptions. First, the '
        'gerberette pivots on an exterior column as a lever (Rice 1994; Hamzeian 2018, DOI '
        '10.1201/9780429506208-91): assumed V_p = 4,800 kN at arm a and tie back-span c gives '
        'T_tie = V_p · (a / c) and C_col = V_p · (1 + a / c), or 1,280.0 kN and 6,080.0 kN at '
        'a = 1.60 m, c = 6.00 m. Over a in [0.80, 2.60] m and c in [3.50, 8.50] m, estimated '
        'T_tie spans 451.8 to 3,565.7 kN while surrogate SF = 3.12 × (1,280 / max(100, T_tie)) '
        'flags SF < 1.50 above 2,662.4 kN (a / c > 0.555). Second, b − 3j + 6 = s − m '
        '(Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4) is not verified by '
        'matrix calculation here: m = 0, about 48 m span, and 15 yr / 100 yr remain fixed '
        'reference text.'
    ),
    'act2_deepening': (
        'Under the stated assumptions, the ratio a / c sets tie tension and column compression '
        'for fixed V_p. Raising a increases T_tie linearly, whereas widening c lowers tie pull '
        'and may open an exterior zone for detachable risers (Brand 1994). Pinning trusses at '
        'gerberette rockers limits column bending (Rice 1994), whereas a tight site restricting '
        'c raises tie pull and node shear (Hamzeian 2018, DOI 10.1201/9780429506208-91).'
    ),
    'act4_deepening': (
        'An untested proposal, not verified in practice: node sensors and crane-path simulations '
        'could monitor forces during riser swaps. Combining support-and-infill separation '
        '(Habraken 2021, DOI 10.4324/9781003014713), shearing layers (Brand 1994), and matrix '
        'checks (Pellegrino & Calladine 1986, DOI 10.1016/0020-7683(86)90014-4) might reduce '
        'retrofit disruption under stated assumptions, with caveats for unmodeled codes and joints.'
    ),
    'act4_human_ai': (
        "Speculative note: Cook's Plug-In City and Herron's Walking City imagined swappable "
        'capsules (Beslioglu 2014, DOI 10.4995/vlc.2014.1829). Future teams might pair sensors '
        'with maintenance logs to plan riser swaps; nothing here is simulated, tested, or '
        'approved for real buildings.'
    ),
}

PLATE_CAPTION = {
    'alt': (
        "Conceptual visualization imagining what Archigram's Walking City and Plug-In City "
        'combined with British High-Tech cast-steel gerberette exoskeletons and modular service '
        'pods might look like (artistic impression, not a measured structure)'
    ),
    'caption': (
        'Conceptual Vision Plate A.04-V (Imagining What It Would Look Like) · Artistic '
        "architectural visualization imagining Ron Herron's Walking City and Peter Cook's Plug-In "
        'City with cast-steel gerberette cantilevers, exterior tension tie rods, and crane-lifted '
        'service capsules (untested artistic impression, not an engineered structure).'
    ),
}

DISPATCH = {
    'kicker': 'HIGH-TECH & OPEN-BUILDING DISPATCH · ARCHIGRAM PLUG-IN FRAMES TO GERBERETTE STATICS',
    'headline': "From Archigram's 1964 Plug-In Capsules to High-Tech Exoskeletons: A Lever Model of the Gerberette",
    'body': (
        "Connecting Cook & Herron's Plug-In drawings (Beslioglu 2014, DOI 10.4995/vlc.2014.1829) "
        'with Centre Pompidou gerberettes (Hamzeian 2018, DOI 10.1201/9780429506208-91) and '
        'Pellegrino–Calladine counting (DOI 10.1016/0020-7683(86)90014-4), this untested '
        'explanation estimates T_tie = 1,280.0 kN under stated assumptions; no figure belongs on '
        'a real structure.'
    ),
}

META_3D = (
    'High-Tech Cast-Steel Gerberette Cantilever Truss',
    'X: Column-Free Span & Rocker Fulcrum · Z: Structural Bay · Y: Bending Moment & Tension Tie',
)

ES_TRANSLATION = {
    'title_es': (
        'De las Megaestructuras Plug-In de Archigram a los Exoesqueletos High-Tech: Gerberettes, '
        'Marcos de Maxwell y Módulos de Servicios'
    ),
    'subtitle_es': (
        'Explicación arquitectónica y estática, no un método de diseño estructural: de los dibujos '
        'de Archigram a la palanca gerberette del Centro Pompidou y módulos reemplazables; ninguna '
        'cifra aquí puede usarse en una estructura real.'
    ),
    'why_es': (
        'En un sube y baja, un adulto cerca del pivote equilibra a un niño sentado más lejos. '
        'Una gerberette trabaja con esa palanca: la losa apoya en un brazo corto interior y un '
        'tirante exterior equilibra la punta. Donde termina la comparación: un sube y baja es '
        'una tabla sobre un pasador, mientras un nudo fundido resiste cortante y torsión y un '
        'marco 3D requiere arriostramiento.'
    ),
    'plain_es': (
        'Muchos edificios se parecen a una computadora sellada con tuberías dentro de muros '
        'portantes (Brand 1994). Al llevar columnas y ductos fuera de la fachada (Rice 1994), el '
        'esqueleto se separa del relleno cambiante (Habraken 2021, DOI 10.4324/9781003014713). '
        'Este folio es una explicación conceptual, no un método de diseño estructural, y ninguna '
        'cifra aquí debe usarse en una estructura real.'
    ),
    'deep_es': (
        'En el Centro Pompidou (claros de unos 48 m), el equipo de Rice evolucionó la gerberette '
        '(Hamzeian 2018, DOI 10.1201/9780429506208-91). Con V_p = 4,800 kN supuesto, a = 1.60 m y '
        'c = 6.00 m, T_tie = 1,280.0 kN y C_col = 6,080.0 kN; en a de 0.80 a 2.60 m y c de 3.50 a '
        '8.50 m, T_tie va de 451.8 a 3,565.7 kN y SF = 3.12 × (1,280 / max(100, T_tie)) alerta '
        'bajo 1.50 sobre 2,662.4 kN. El claro de ~48 m, 15/100 años y m = 0 (DOI '
        '10.1016/0020-7683(86)90014-4) son texto fijo, no un método de diseño estructural.'
    ),
}
