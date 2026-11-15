#!/usr/bin/env python3
"""Folio A.10 (ARCHITECTURE): Kinetic Origami & Miura-Ori Deployable Biomimetic Facades: Isometric Crease Kinematics, Auxetic Poisson Ratio Inversion & Solar Mashrabiya Envelopes."""
from __future__ import annotations

SLUG = 'a10'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.10',
 'slug': 'a10',
 'pillar': 'architecture',
 'category_code': 'A',
 'parent_folios': ['A.04', 'A.03', 'M.05'],
 'lineage_mode': 'REFERENCE_COMPLETION · Completes A.04 High-Tech Exoskeletons, A.03 Daylighting & '
                 'M.05 Distance Rigidity',
 'title': 'Kinetic Origami & Miura-Ori Deployable Biomimetic Facades: Isometric Crease Kinematics, '
          'Auxetic Poisson Ratio Inversion & Solar Mashrabiya Envelopes',
 'subtitle': "Completing the deployable exoskeleton and daylighting threads of Folios A.04, A.03, and M.05: a design study of how Koryo Miura's fold and Schenk & Guest's analysis of folded metamaterials could drive adaptive, mashrabiya-inspired solar shading.",
 'date_published': '2026-11-03',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'KINETIC ORIGAMI · REV 1.1',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'tan(γ_2/2) = cos α · tan(γ_1/2) · ν_xy = −tan² φ < 0 · Kawasaki ∑ α_{2i} = π · '
                  'CSI 10 71 13',
 'colophon': {'identifier': 'A.10 · Kinetic Origami & Auxetic Mashrabiya Facades · CSI 10 71 13',
              'kernels': 'Miura-Ori Spherical Vertex Law · Schenk–Guest Auxetic ν_xy = −tan² φ',
              'benchmarks': 'Model values: α = 64° · θ = 36° ⇒ ν_xy ≈ −0.37 (folio parametrization) · SHGC = 0.19 (assumed SHGC_glass = 0.60, η_shade = 0.845)',
              'bridge': 'Completes A.04/A.03/M.05 · Loose analogy only: one-degree-of-freedom hinged motion ↔ protein domain motion (not a model of CFTR)'},
 'sliders': [{'label': 'Origami Deployment Fold Angle (θ)',
              'min': 10.0,
              'max': 80.0,
              'step': 2.0,
              'value': 36.0,
              'unit': '°'},
             {'label': 'Miura Parallelogram Sector Angle (α)',
              'min': 52.0,
              'max': 78.0,
              'step': 1.0,
              'value': 64.0,
              'unit': '°'}],
 'steps': ['Stage 1 (Kawasaki & Maekawa Flat-Foldable Vertex, Continuing M.05): Four rigid parallelogram facets meet at a degree-4 vertex whose alternate sector angles sum to π. In the ideal rigid model this leaves a single degree of freedom.',
           'Stage 2 (Spherical Trigonometry Dihedral Coupling): Taking the primary fold angle γ_1 = θ = 36° and α = 64°, the relation tan(γ_2/2) = cos α · tan(γ_1/2) gives a secondary fold angle γ_2 ≈ 16.2°. The facets are assumed rigid, so they do not stretch.',
           "Stage 3 (Auxetic Poisson Ratio, after Schenk & Guest 2013, DOI 10.1073/pnas.1217998110): Schenk and Guest showed that a Miura-ori sheet has a negative in-plane Poisson ratio. In this folio's simplified parametrization, cos φ = sin α · cos(θ/2) gives φ ≈ 31.3° and ν_xy = −tan² φ ≈ −0.37 at the default settings.",
           "Stage 4 (Mashrabiya-Inspired Solar Shading, Continuing A.03/A.04): With an assumed bare-glazing SHGC_glass = 0.60 and shading effectiveness η_shade = 0.845, the folio's rule SHGC = SHGC_glass · (1 − η_shade · cos θ) gives 0.19 at θ = 36°, a 68.4% cut in solar heat gain through the glazing in the model. Cooling-energy savings and daylight levels are not computed here."],
 'readouts': [{'label': 'In-Plane Poisson Ratio (ν_xy)', 'value': '−0.37 (Model, −tan² φ)'},
              {'label': 'Effective Facade SHGC', 'value': '0.19 (Model, −68.4% vs Bare Glazing)'},
              {'label': 'Coupled Dihedral Angle (γ_2)', 'value': '16.2° (Model, γ_1 = θ)'},
              {'label': 'Kinematic Model Check', 'value': 'ONE DEGREE OF FREEDOM (IDEAL RIGID MODEL)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 10 71 13 / 08 44 13',
                'title': 'Kinetic Miura-Ori PTFE & Anodized Aluminum Mashrabiya Solar Shading '
                         'Screen',
                'body': 'Design proposal: outboard exoskeleton-mounted (continuing A.04) kinetic origami shading modules with stainless-steel vertex pins, PTFE membrane facets and linear actuators. Not a tested assembly.',
                'meta': 'Reference: Schenk & Guest (2013) DOI 10.1073/pnas.1217998110 · Al Bahar precedent: Karanouh & Kerber (2015) DOI 10.3233/fde-150040 · No wind or load testing was done for this folio'},
 'sidenote_1': {'kicker': 'SIDENOTE A.10-A · CONTINUING FOLIO A.04 MAXWELL–CALLADINE & M.05 '
                          'RIGIDITY',
                'body': 'While Folio A.04 designed space frames with zero internal mechanisms (m = '
                        '0), rigid origami intentionally engineers a single cooperative mechanism '
                        '(m = 1) where all vertices move in lockstep.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.10-B · SPECIFICATION PLATE · CSI 10 71 13 (SOLAR MASHRABIYA)',
                'body': 'Historic mashrabiya screens are carved wooden lattices that temper sun and glare and give privacy. A kinetic origami screen is a modern design idea in the same spirit. This folio does not estimate how much cooling energy such a screen would save; that depends on climate, glazing and orientation.'},
 'skill': {'filename': 'kinetic-origami-miura-facade-SKILL.md',
           'name': 'kinetic-origami-miura-facade',
           'description': 'AI-agnostic architectural and mechanical-metamaterial skill for '
                          'Miura-ori rigid origami kinematics, Kawasaki flat-foldability, '
                          'Schenk-Guest negative Poisson ratio (nu_xy = -tan^2(phi)), and kinetic '
                          'solar facades.',
           'rules': ["Enforce Kawasaki's flat-foldability theorem sum(alpha_even) = sum(alpha_odd) "
                     "= pi and Maekawa's mountain-valley rule |M - V| = 2 at every interior "
                     'degree-4 vertex.',
                     "Compute the semi-width angle phi from this folio's simplified parametrization cos(phi) = sin(alpha) * cos(theta / 2) and "
                     'evaluate the in-plane Poisson ratio nu_xy = -tan^2(phi) < 0 (about -0.37 at alpha = 64, theta = 36); note that Schenk & Guest (2013) parametrize the fold differently.',
                     "Couple facade deployment angle theta to solar altitude; treat SHGC <= 0.22 at peak insolation and >= 250 EML daylight as this folio's own design targets and report SHGC as a model value, not a measurement."]},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The opening scene of Miura folding paper at his desk was not sourced and is replaced by a plain account; the JAXA attribution (JAXA was founded in 2003) and the 1980 date are corrected to Miura\'s 1985 ISAS report. The Poisson ratio, secondary fold angle and SHGC now follow from the folio\'s own formulas (−0.37, 16.2°, 0.19 with stated assumptions); unsourced cooling-energy savings, wind testing, "zero jam" and a CFTR structure claim are withdrawn, and an unrelated graphic-statics source is removed.',
                'opus': 'Review: references checked by DOI in Crossref; arithmetic recomputed from the stated formulas.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-03',
                'summary': 'REV 1.0 (Published 2026-11-03): Volume V kinetic architecture '
                           "monograph completing Folios A.04, A.03 & M.05 via Schenk & Guest's "
                           'folded metamaterial kinematics (DOI 10.1073/pnas.1217998110) and '
                           'Mashrabiya solar envelopes.',
                'opus': "Council review (Gemini 4 Argon + Qwen 3.8 27B). Its 'verified' wording is withdrawn in REV 1.1: the value nu_xy = -1.38 did not follow from the folio's own formula, which gives about -0.37."}],
 'volume': 5,
 'volume_code': 'VOL. 05',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1073/pnas.1217998110',
           'fetched_on': '2026-11-08',
           'citing_publications': 1086,
           'supporting': 10,
           'mentioning': 770,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Schenk & Guest, Geometry of Miura-folded metamaterials (DOI 10.1073/pnas.1217998110), checked 2026-11-08: 1,086 citing publications (10 supporting, 770 mentioning, 0 contrasting) and no retraction notice. The counts describe that paper, not this folio\'s model.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['A.04', 'A.03', 'M.05'],
 'lineage_mode': 'REFERENCE_COMPLETION · Completes A.04 High-Tech Exoskeletons, A.03 Daylighting & '
                 'M.05 Distance Rigidity',
 'scite': {'doi': '10.1073/pnas.1217998110',
           'fetched_on': '2026-11-08',
           'citing_publications': 1086,
           'supporting': 10,
           'mentioning': 770,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Schenk & Guest, Geometry of Miura-folded metamaterials (DOI 10.1073/pnas.1217998110), checked 2026-11-08: 1,086 citing publications (10 supporting, 770 mentioning, 0 contrasting) and no retraction notice. The counts describe that paper, not this folio\'s model.'},
 'act1_title': 'Act I — Continuing A.04 Exoskeletons, A.03 Daylighting & M.05 Rigidity: The '
               'Mathematics of Origami Building Envelopes',
 'act1_dropcap': "Koryo Miura, a Japanese engineer at the Institute of Space and Astronautical Science, worked on ways to pack large membranes, such as solar arrays, for launch and open them in space. His 1985 report describes a fold of identical parallelograms set in a herringbone pattern. A sheet folded this way opens and closes in a single motion: pull two opposite corners and it expands in length and width together. The pattern is now called Miura-ori. In 2013 Mark Schenk and Simon Guest at the University of Cambridge analysed the Miura fold as a mechanical metamaterial and showed, among other results, that its in-plane Poisson ratio is negative (PNAS, DOI 10.1073/pnas.1217998110). This folio is a design study of what that geometry could mean for sun-shading facades.",
 'act1_plain_bridge': 'In plain words, think about what happens when you stretch an everyday '
                      'rubber band. As you pull the ends apart to make it longer, the rubber band '
                      'becomes noticeably thinner in the middle. Almost every natural material '
                      'behaves this way. But kinetic origami does something completely unexpected '
                      'and counter-intuitive. When you pull open a folded paper map using the '
                      'Miura pattern, the sheet spreads wider in both directions at the exact same '
                      'time. Materials that expand sideways when pulled lengthwise are called '
                      'auxetic. For architects designing building facades, this strange expanding '
                      'behavior is an absolute superpower. Instead of installing hundreds of '
                      'separate motorized shades with thousands of tiny gears that can break or '
                      'freeze, an entire wall of interlocking shade panels can be linked into a '
                      'single continuous origami sheet. In the ideal model, tugging on one edge unfolds the whole sheet in unison. Whether a real facade would save cooling energy, and how much, is not worked out here.',
 'act1_body': "Miura-ori was developed by Koryo Miura for packaging and deploying large membranes in space (ISAS Report 618, 1985). In 2013 Mark Schenk and Simon D. Guest published an analysis in PNAS (DOI 10.1073/pnas.1217998110) that treats the Miura-ori sheet as a mechanical metamaterial and shows that its in-plane Poisson ratio is negative. Its degree-four vertices satisfy Kawasaki's flat-foldability condition, and spherical trigonometry links the fold angles of the creases at each vertex; this folio uses the relation tan(gamma_2 / 2) = cos(alpha) * tan(gamma_1 / 2) and writes the in-plane Poisson ratio as nu_xy = -tan^2(phi) with its own simplified expression for phi. In built architecture, the Al Bahar Towers in Abu Dhabi carry origami-like, umbrella-shaped shading units covered in PTFE-coated fiber mesh; their designers report that the screen cuts the facade's solar heat gain (g-value) by more than half compared with bare glazing (Karanouh & Kerber 2015, DOI 10.3233/fde-150040). Applying rigid Miura origami to a solar screen (specified under CSI 10 71 13, Exterior Sun Control Devices) is the design idea this folio explores.",
 'act1_stakes': "Builders in hot regions, from Cairo to Isfahan and Damascus, long used carved wooden lattice screens known as mashrabiya to temper sun and glare and to give privacy. In 1987 Jean Nouvel's Institut du Monde Arabe in Paris reinterpreted the mashrabiya as a wall of mechanical, light-sensitive apertures. Mechanical facades like that rely on many moving parts that need upkeep. The idea explored here is to put the motion into the geometry of the folds, so a whole screen could be moved by one actuator. That is a design hypothesis: real hinges have play and friction, and a real origami facade could still bind or wear.",
 'pullquote': '"A degree-4 Miura-ori vertex reduces a thousand-panel architectural solar screen to '
              'a single kinematic degree of freedom: pull one corner, and spherical trigonometry '
              'unfolds the entire facade."',
 'chronology': [('1985',
                 'Koryo Miura describes the packaging and deployment of large membranes in space with a parallelogram fold (ISAS Report 618), now known as Miura-ori.'),
                ('1987',
                 "Jean Nouvel's Institut du Monde Arabe opens in Paris with a facade of mechanical, light-sensitive apertures inspired by the mashrabiya."),
                ('2013',
                 'Mark Schenk & Simon D. Guest analyse Miura-ori as a folded metamaterial with a negative in-plane Poisson ratio in PNAS (DOI 10.1073/pnas.1217998110).'),
                ('2015',
                 'Karanouh & Kerber describe the design and delivery of the dynamic, origami-like PTFE shading screens of the Al Bahar Towers in Abu Dhabi (DOI 10.3233/fde-150040).')],
 'act2_title': 'Act II — How It Actually Works: Spherical Degree-4 Vertex Kinematics + Auxetic '
               'Poisson Inversion',
 'act2_analogy': 'Think of an old-fashioned paper road map that has been folded with accordion '
                 'creases: when you try to pull it open carelessly, the paper snags, binds, and '
                 'tears along the folds. Now imagine a fold pattern where every crease works in '
                 'harmony, like an expanding concertina or a pop-up paper umbrella: gently pulling '
                 'two opposite corners causes every folded facet to open simultaneously without '
                 'twisting or jamming. That synchronized unfolding is the core of rigid Miura '
                 'origami.',
 'act2_plain_primer': 'To control an origami facade on a skyscraper, you only need to adjust two '
                      'geometric knobs. The first knob controls the deployment fold angle, which '
                      'measures how far the folded panels have opened or closed. When this knob is '
                      'set to a low angle, the panels fold flat against each other, projecting '
                      'outward like an array of open umbrellas that block direct desert sun from '
                      'entering the building. As the afternoon cools and the sun sinks toward the '
                      'horizon, dialing this knob open flattens the panels back against the glass '
                      'wall, admitting panoramic city views and gentle evening light. The second '
                      'knob sets the sector angle of the individual parallelogram tiles that make '
                      'up the origami pattern. If you choose a steep, narrow diamond tile, the '
                      'facade opens with deep three-dimensional relief, creating dramatic '
                      'sculptural shadows. If you choose a wider angle, the panels move more '
                      'gently, acting like a lightweight, low-profile solar filter across the '
                      'glass curtain wall.',
 'distill_diagram': {'analogy_title': 'The Pop-Up Umbrella Lattice',
                     'analogy_sub': 'Pulls open in length and width simultaneously without panel '
                                    'strain',
                     'force_a_title': 'Deployment Fold Angle (θ)',
                     'force_a_sub': 'Modulates facade shading depth and overall solar heat '
                                    'transmission',
                     'force_b_title': 'Parallelogram Sector Angle (α)',
                     'force_b_sub': 'Sets geometric aspect ratio and auxetic negative Poisson '
                                    'response',
                     'threshold_title': 'Auxetic Kinematic State (ν_xy ≈ −0.37, Model)',
                     'threshold_pass': 'Smooth one-degree-of-freedom deployment in the ideal model; SHGC 0.19 in the model',
                     'threshold_fail': 'Facet bending or binding if vertices break Kawasaki '
                                       'symmetry'},
 'act2_intuition': 'Continuing the Maxwell–Calladine kinematic mechanism count of Folio A.04 (m = '
                   '1 single collective mechanism) and the distance geometry theorems of Folio '
                   'M.05, consider a Miura-ori unit cell composed of four rigid planar '
                   'parallelogram facets with acute sector angle alpha (typically 55° to 78°) '
                   'meeting at an interior degree-four vertex. When actuated by the primary fold '
                   "angle theta in the range from 10° to 80°, this folio uses a simplified parametrization of its own for the semi-width angle, cos(phi) = sin(alpha) * cos(theta / 2), and couples the secondary fold angle gamma_2 to the primary fold angle gamma_1 (taken equal to theta) via tan(gamma_2 / 2) = cos(alpha) * tan(gamma_1 / 2). It then writes the in-plane Poisson ratio as nu_xy = -tan^2(phi) < 0, the form Schenk & Guest give for their own fold-angle definition; with the folio's parametrization the default settings give phi ≈ 31.3° and nu_xy ≈ -0.37, and gamma_2 ≈ 16.2°. As an exterior shading screen (CSI 10 71 13), varying theta from 15° (projected canopy) to 78° (folded) changes the model's effective Solar Heat Gain Coefficient SHGC = SHGC_glass * (1 - eta_shade * cos(theta)); with the assumed SHGC_glass = 0.60 and eta_shade = 0.845 it is 0.19 at theta = 36°. These are model values; daylight and cooling loads are not computed.",
 'act2_deepening': "Rigid Miura-ori is tightly constrained by spherical trigonometry around each degree-four vertex. Because alternate sector angles sum to pi (Kawasaki) and mountain and valley creases differ by two (Maekawa), the ideal unit cell has a single degree of freedom. That coupling makes the Poisson ratio depend nonlinearly on the sector angle alpha. In this folio's parametrization, at theta = 36° the magnitude of nu_xy falls as alpha rises: about -0.78 at alpha = 52° and about -0.16 at alpha = 78°. Real hinges are not ideal. Thermal expansion or manufacturing misalignment can force panels to bend out of plane, so a built screen would need tolerance at its supports, for example sliding bearings at the perimeter; this folio does not design them.",
 'walkthrough': ['Experiment 1 (Kinematic Deployment Angle theta): Drag Origami Deployment Fold '
                 'Angle theta from 12° (deployed sun-blocking canopy) to 80° (compactly folded '
                 'open state). Watch the projected shading coverage and Effective SHGC respond in '
                 'real time.',
                 'Experiment 2 (Parallelogram Sector Angle alpha & Auxetic Ratio): Vary Miura '
                 'Sector Angle alpha from 52° to 78° and track the negative in-plane Poisson ratio '
                 'nu_xy = -tan^2(phi) alongside crease dihedral coupling.',
                 'Experiment 3 (From Space Array to Kinetic Mashrabiya): Step through Stages 1 to '
                 '4 to inspect Kawasaki flat-foldability, spherical vertex coupling, auxetic '
                 'expansion, and the solar-shading model.'],
 'act4_title': 'Act IV — Deployable Facade Tectonics, Archive Continuity & Upstream Biophysical '
               'Threads',
 'act4_human_ai': "Pairing Folio A.03's daylight targets and Folio A.04's exoskeleton maintenance rails with Schenk & Guest's rigid-origami kinematics, facade engineers could design PTFE and anodized-aluminum kinetic sunshades. This is a design proposal; the folio does not estimate cooling-energy savings or test for jamming.",
 'act4_deepening': 'Designers working with computational tools could generate site-specific origami envelopes: optimization could take annual solar maps, prevailing winds and interior daylight needs and vary the Miura crease pattern across a facade, and a sensor-driven controller could set the single drive. These are proposals, not a description of current practice. Significant frontier questions remain at the leading edge of '
                   'kinetic architecture: How can flexible compliant hinges fabricated from '
                   'shape-memory alloys or carbon-fiber composites withstand millions of fatigue '
                   'cycles under gusting wind turbulence without mechanical failure? Can kinetic '
                   'origami facades harvest wind and vibrational energy during storm events to '
                   'recharge their own emergency backup batteries? By answering these questions, '
                   'architects and computational tools transform static curtain walls into '
                   'responsive, lifelike skins.',
 'cf_bridge': 'Standalone kinetic-architecture folio (A.04 + A.03 + M.05 -> A.10), written for facade engineers, computational architects, and kinetic envelope designers (CSI 10 71 13 is the MasterFormat section for exterior sun control devices). It has no Cystic Fibrosis content. A loose analogy only: proteins such as CFTR also move as linked, nearly rigid domains, but origami kinematics is not a model of CFTR gating.',
 'sources': ['Schenk, M., & Guest, S. D. (2013). Geometry of Miura-folded metamaterials. Proceedings of '
             'the National Academy of Sciences (PNAS), 110(9), 3276–3281. DOI: '
             '10.1073/pnas.1217998110.',
             'Miura, K. (1985). Method of packaging and deployment of large membranes in space. '
             'Institute of Space and Astronautical Science Report, 618, 1–9.',
             'Karanouh, A., & Kerber, E. (2015). Innovations in dynamic architecture. Journal of Facade Design and '
             'Engineering, 3(2), 185–221. DOI: 10.3233/fde-150040.',
             'CSI MasterFormat 10 71 13 Exterior Sun Control Devices & 08 44 13 Glazed Aluminum '
             "Curtain Walls. Named for context; neither sets this folio's targets.",
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Miura-ori degree-4 '
        'rigid origami unit cell tessellation and auxetic negative Poisson ratio nu_xy = '
        '-tan^2(phi) curve">\n'
        '            <line x1="40" y1="188" x2="640" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <g id="tp-a10-miura-cell" transform="translate(190, 108)">\n'
        '              <polygon points="-95,-48 -15,-22 -5,32 -85,6" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '              <polygon points="-15,-22 75,-48 85,6 -5,32" fill="var(--tp-verdigris)" '
        'fill-opacity="0.28" stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '              <polygon points="-85,6 -5,32 10,68 -70,42" fill="var(--tp-verdigris)" '
        'fill-opacity="0.22" stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '              <polygon points="-5,32 85,6 100,42 10,68" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '              <line x1="-15" y1="-22" x2="-5" y2="32" stroke="var(--tp-minium)" '
        'stroke-width="2.5"/>\n'
        '              <circle cx="-5" cy="32" r="5" fill="var(--tp-minium)"/>\n'
        '            </g>\n'
        '            <text x="52" y="26" font-size="10.5" font-weight="600" '
        'fill="currentColor">Miura-Ori Degree-4 Spherical Vertex &amp; Mashrabiya Cell</text>\n'
        '            <text id="tp-a10-svg-cell-text" x="52" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">ν_xy = −tan² φ ≈ −0.37 (Model) · SHGC = 0.19 (Model)</text>\n'
        '            <line x1="355" y1="24" x2="355" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="372" y="26" font-size="10" font-weight="600" '
        'fill="currentColor">Poisson Ratio ν_xy(θ) &amp; Solar Shading Factor</text>\n'
        '            <path id="tp-a10-poisson-curve" d="M 380 62 Q 495 135 625 170" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="2.6"/>\n'
        '            <circle id="tp-a10-op-dot" cx="475" cy="112" r="6" fill="var(--tp-minium)"/>\n'
        '            <text x="382" y="55" font-size="9.5" fill="var(--tp-prussian)">Spherical Law: '
        'tan(γ₂/2) = cos α · tan(γ₁/2)</text>\n'
        '            <text id="tp-a10-shgc-text" x="382" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Model Solar Heat Gain vs Bare Glazing: −68.4%</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a kinetic Miura-ori origami Mashrabiya building '
        'facade deploying translucent geometric PTFE and anodized bronze facets across an '
        'exoskeleton curtain wall would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.10-V (Imagining What It Would Look Like) · Artistic '
            'architectural-kinematics visualization (completing Folios A.04, A.03 & M.05) '
            'imagining a rigid-foldable Miura-ori auxetic solar Mashrabiya envelope modulating '
            'desert sunlight with a single spherical-vertex degree of freedom.'}

DISPATCH = {'kicker': 'FRONTIER KINETIC FACADE DISPATCH · COMPLETING A.04, A.03 & M.05 · MIURA-ORI AUXETIC '
           'ORIGAMI',
 'headline': 'Miura-Ori Spherical Vertex Kinematics & Negative Poisson Ratios Drive Deployable '
             'Solar Mashrabiya Envelopes',
 'body': "Schenk & Guest showed that a Miura-folded sheet has a negative in-plane Poisson ratio (PNAS, DOI 10.1073/pnas.1217998110). This design study, continuing Folios A.04, A.03 and M.05, uses that geometry for a proposed one-actuator solar screen: in the folio's simplified model ν_xy ≈ −0.37 and SHGC = 0.19 at the default settings. Model values, not measurements."}

META_3D = ('Miura-Ori Auxetic Saddle & Spherical Vertex Manifold',
 'X/Z: Tessellation Unit-Cell Plane · Y: Isometric Fold Height & Negative Poisson Ratio ν_xy')

ES_TRANSLATION = {'title_es': 'Origami Cinético y Fachadas Biomiméticas Desplegables Miura-Ori: Cinemática '
             'Isométrica de Pliegues, Inversión Auxética de Poisson y Envolventes Mashrabiya',
 'subtitle_es': 'Completando los Folios A.04, A.03 y M.05: un estudio de diseño sobre cómo el pliegue de Koryo Miura y el análisis de metamateriales plegados de Schenk y Guest podrían mover celosías solares adaptativas inspiradas en la mashrabiya.',
 'why_es': 'A diferencia de una liga que se adelgaza al estirarla, un mapa plegado con el patrón '
           'Miura-ori se expande en ambas direcciones a la vez con un solo movimiento, permitiendo '
           'abrir o cerrar toda una fachada solar sin atascarse.',
 'bridge_es': 'Este folio es de arquitectura cinética y no tiene contenido sobre Fibrosis Quística. Solo como analogía: proteínas como CFTR también se mueven como dominios casi rígidos unidos entre sí, pero la cinemática del origami no es un modelo de cómo se abre CFTR.',
 'plain_es': 'En palabras sencillas, imaginen un mapa de papel doblado con un patrón especial de '
             'rombos: al jalar suavemente dos de sus esquinas, todo el mapa se abre a lo ancho y a '
             'lo largo al mismo tiempo con un solo movimiento fluido. El ingeniero japonés Koryo Miura '
             'describió este pliegue para empacar y desplegar grandes membranas en el espacio. Casi todas las cosas en el mundo '
             'se adelgazan cuando las estiramos, como una liga; en cambio, el patrón Miura-ori '
             'hace exactamente lo contrario, expandiéndose hacia los lados al estirarse. En la '
             'arquitectura, este folio explora una idea de diseño: en lugar de muchas persianas '
             'motorizadas por separado, una sola pantalla plegable inspirada en las celosías '
             'mashrabiya, movida por un solo cable o motor. En el modelo ideal toda la pantalla se '
             'abre a la vez; el folio no calcula cuánta energía de aire acondicionado se ahorraría.',
 'deep_es': 'Schenk y Guest (2013, DOI 10.1073/pnas.1217998110) mostraron que una lámina con pliegue Miura-ori tiene una razón de Poisson negativa en el plano. En el modelo ideal de caras rígidas, cada vértice de cuatro pliegues cumple el teorema de Kawasaki y la regla de Maekawa, y la lámina tiene un solo grado de libertad. Con la parametrización simplificada de este folio, cos φ = sen α · cos(θ/2) y ν_xy = −tan² φ dan ν_xy ≈ −0.37 con α = 64° y θ = 36°, y el segundo ángulo de pliegue resulta γ_2 ≈ 16.2°. Para la sombra solar, el folio usa SHGC = SHGC_vidrio · (1 − η · cos θ) con valores supuestos SHGC_vidrio = 0.60 y η = 0.845, lo que da 0.19, es decir 68.4 % menos ganancia solar que el vidrio sin protección en el modelo. Como precedente construido, los autores del diseño de las torres Al Bahar en Abu Dabi reportan que sus pantallas de malla de fibra con PTFE reducen a menos de la mitad la ganancia solar de la fachada frente al vidrio (Karanouh y Kerber 2015, DOI 10.3233/fde-150040). Son valores de modelo, no mediciones.'}
