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
 'subtitle': "Completing Folios A.04, A.03, and M.05: a design study of how Koryo Miura's 1985 fold and "
             "Schenk & Guest's (2013) analysis of folded metamaterials could drive mashrabiya-inspired solar shading.",
 'date_published': '2026-11-03',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'KINETIC ORIGAMI · REV 1.1',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'tan(γ_2/2) = cos α · tan(γ_1/2) · ν_xy = −tan² φ < 0 · Kawasaki ∑ α_{2i} = π · '
                  'CSI 10 71 13',
 'colophon': {'identifier': 'A.10 · Kinetic Origami & Auxetic Mashrabiya Facades · CSI 10 71 13',
              'kernels': 'Miura-Ori Spherical Vertex Law · Schenk–Guest Auxetic ν_xy = −tan² φ',
              'benchmarks': 'Model values: α = 64° · θ = 36° ⇒ ν_xy ≈ −0.37 (folio parametrization) · '
                            'SHGC = 0.19 (assumed SHGC_glass = 0.60, η_shade = 0.845)',
              'bridge': 'Completes A.04/A.03/M.05'},
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
 'steps': ['Stage 1 (Kawasaki & Maekawa Flat-Foldable Vertex, Continuing M.05): Four rigid parallelogram '
           'facets meet at a degree-4 vertex satisfying Kawasaki alternating-angle sums (π) and Maekawa '
           'mountain-valley parity (|M − V| = 2; Hull 2020, DOI 10.1017/9781108778633), leaving one '
           'degree of freedom in the ideal rigid sheet (Miura 1985).',
           'Stage 2 (Spherical Trigonometry Dihedral Coupling): With primary fold angle γ_1 = θ = 36° and '
           'α = 64°, tan(γ_2/2) = cos α · tan(γ_1/2) yields secondary fold angle γ_2 ≈ 16.2° for zero-thickness '
           'facets (real thick panels require hinge-offset geometry; Tachi 2011, DOI 10.1201/b10971-24).',
           "Stage 3 (Auxetic Poisson Ratio, after Schenk & Guest 2013, DOI 10.1073/pnas.1217998110): Schenk "
           "and Guest showed that a Miura-ori sheet exhibits a negative in-plane Poisson ratio. In this "
           "folio's simplified parametrization, cos φ = sin α · cos(θ/2) gives φ ≈ 31.3° and "
           "ν_xy = −tan² φ ≈ −0.37 at default settings.",
           "Stage 4 (Mashrabiya-Inspired Solar Shading, Continuing A.03/A.04): With assumed bare-glazing "
           "SHGC_glass = 0.60 and shading effectiveness η_shade = 0.845, the folio's illustrative rule "
           "SHGC = SHGC_glass · (1 − η_shade · cos θ) gives 0.19 at θ = 36° (−68.4% solar heat gain in the "
           "model); published origami facade simulations (Meloni et al. 2023, DOI 10.1016/j.scs.2023.104740; "
           "Kahramanoğlu & Çakıcı Alp 2023, DOI 10.1016/j.jobe.2023.106241) motivate this study, though "
           "cooling loads and daylight are not computed here."],
 'readouts': [{'label': 'In-Plane Poisson Ratio (ν_xy)', 'value': '−0.37 (Model, −tan² φ)'},
              {'label': 'Effective Facade SHGC', 'value': '0.19 (Model, −68.4% vs Bare Glazing)'},
              {'label': 'Coupled Dihedral Angle (γ_2)', 'value': '16.2° (Model, γ_1 = θ)'},
              {'label': 'Kinematic Model Check', 'value': 'ONE DEGREE OF FREEDOM (IDEAL RIGID MODEL)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 10 71 13 / 08 44 13',
                'title': 'Kinetic Miura-Ori PTFE & Anodized Aluminum Mashrabiya Solar Shading Screen',
                'body': 'Design proposal: outboard exoskeleton-mounted (continuing A.04) kinetic origami '
                        'shading modules with stainless-steel vertex pins, PTFE membrane facets, and linear '
                        'actuators. Not a tested assembly.',
                'meta': 'Reference: Schenk & Guest (2013) DOI 10.1073/pnas.1217998110 · Al Bahar precedent: '
                        'Karanouh & Kerber (2015) DOI 10.3233/fde-150040; Attia (2017) DOI '
                        '10.5339/connect.2017.qgbc.6 · No wind or load testing was done for this folio'},
 'sidenote_1': {'kicker': 'SIDENOTE A.10-A · CONTINUING FOLIO A.04 MAXWELL–CALLADINE & M.05 RIGIDITY',
                'body': 'While Folio A.04 treats space frames with zero internal mechanisms (m = 0), ideal '
                        'rigid Miura-ori uses a single collective mechanism (m = 1) where facets fold in '
                        'lockstep (Miura 1985; Schenk & Guest 2013, DOI 10.1073/pnas.1217998110).'},
 'sidenote_2': {'kicker': 'SIDENOTE A.10-B · SPECIFICATION PLATE · CSI 10 71 13 (SOLAR MASHRABIYA)',
                'body': 'Traditional mashrabiya latticework tempers sun, glare, and privacy (El Semary et al. '
                        '2017, DOI 10.21625/archive.v1i1.113), and contemporary dynamic screens extend that '
                        'idea to responsive facades (Attia 2017, DOI 10.5339/connect.2017.qgbc.6). This folio '
                        'does not estimate building cooling-energy savings; those depend on climate, glazing, '
                        'and orientation, and any assembly remains untested.'},
 'skill': {'filename': 'kinetic-origami-miura-facade-SKILL.md',
           'name': 'kinetic-origami-miura-facade',
           'description': 'AI-agnostic architectural and mechanical-metamaterial skill for Miura-ori rigid '
                          'origami kinematics, Kawasaki flat-foldability, Schenk-Guest negative Poisson '
                          'ratio (nu_xy = -tan^2(phi)), and kinetic solar facades.',
           'rules': ["Enforce Kawasaki's flat-foldability theorem sum(alpha_even) = sum(alpha_odd) = pi and "
                     "Maekawa's mountain-valley rule |M - V| = 2 at every interior degree-4 vertex (Hull 2020, "
                     "DOI 10.1017/9781108778633).",
                     "Compute the semi-width angle phi from this folio's simplified parametrization "
                     "cos(phi) = sin(alpha) * cos(theta / 2) and evaluate nu_xy = -tan^2(phi) < 0 (about "
                     "-0.37 at alpha = 64, theta = 36); note that Schenk & Guest (2013, DOI "
                     "10.1073/pnas.1217998110) parametrize the fold differently.",
                     "Couple facade deployment angle theta to solar altitude; treat SHGC <= 0.22 at peak "
                     "insolation and >= 250 EML daylight as this folio's own design targets and report SHGC "
                     "as a model value, not a measurement."]},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The opening scene of Miura '
                           'folding paper at his desk was not sourced and is replaced by a plain account; '
                           'the JAXA attribution (JAXA was founded in 2003) and the 1980 date are corrected '
                           "to Miura's 1985 ISAS report. The Poisson ratio, secondary fold angle and SHGC "
                           "now follow from the folio's own formulas (−0.37, 16.2°, 0.19 with stated "
                           'assumptions); unsourced cooling-energy savings, wind testing and "zero jam" are '
                           'withdrawn, and an unrelated graphic-statics source is removed.',
                'opus': 'Review: references checked by DOI in Crossref; arithmetic recomputed from the '
                        'stated formulas.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-03',
                'summary': 'REV 1.0 (Published 2026-11-03): Volume V kinetic architecture monograph '
                           "completing Folios A.04, A.03 & M.05 via Schenk & Guest's folded metamaterial "
                           'kinematics (DOI 10.1073/pnas.1217998110) and Mashrabiya solar envelopes.',
                'opus': 'Initial model review (2026-11-03; Gemini 4 Argon + Qwen 3.8 27B). Its \'verified\' '
                        "wording is withdrawn in REV 1.1: the value nu_xy = -1.38 did not follow from the "
                        "folio's own formula, which gives about -0.37."}],
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
           'summary': 'Scite index entry for Schenk & Guest, Geometry of Miura-folded metamaterials '
                      '(DOI 10.1073/pnas.1217998110), checked 2026-11-08: 1,086 citing publications (10 '
                      "supporting, 770 mentioning, 0 contrasting) and no retraction notice. The counts "
                      "describe that paper, not this folio's model."}}

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
           'summary': 'Scite index entry for Schenk & Guest, Geometry of Miura-folded metamaterials '
                      '(DOI 10.1073/pnas.1217998110), checked 2026-11-08: 1,086 citing publications (10 '
                      "supporting, 770 mentioning, 0 contrasting) and no retraction notice. The counts "
                      "describe that paper, not this folio's model."},
 'act1_title': 'Act I — Continuing A.04 Exoskeletons, A.03 Daylighting & M.05 Rigidity: The '
               'Mathematics of Origami Building Envelopes',
 'act1_dropcap': 'Koryo Miura at the Institute of Space and Astronautical Science developed a herringbone '
                 'parallelogram fold to pack large spacecraft membranes for launch and deploy them in orbit '
                 '(Miura 1985). Pulling two opposite corners expands a Miura-ori sheet simultaneously in '
                 'length and width with a single kinematic degree of freedom (Miura 1985). In 2013, Mark '
                 'Schenk and Simon D. Guest analyzed Miura-ori as a mechanical metamaterial and showed that '
                 'its in-plane Poisson ratio is negative (PNAS, DOI 10.1073/pnas.1217998110). This folio '
                 'applies that geometry in a design study for adaptive solar shading.',
 'act1_plain_bridge': 'Stretching an ordinary rubber band makes it thinner in the middle, whereas pulling open '
                      'a Miura-ori folded sheet expands it in both length and width at once (Miura 1985; '
                      'Schenk & Guest 2013, DOI 10.1073/pnas.1217998110). Because every crease in the ideal '
                      'rigid pattern moves in lockstep, one edge displacement could unfold the whole array '
                      'instead of driving separate blinds (Miura 1985). Whether a built facade would save '
                      'cooling energy, and how much, is not estimated here.',
 'act1_body': 'Miura-ori originated for biaxial packaging and deployment of space membranes (Miura 1985). '
              'Mathematically, each degree-4 vertex satisfies Kawasaki\'s alternating-angle condition '
              '(∑ α_even = ∑ α_odd = π) and Maekawa\'s mountain-valley parity rule (|M − V| = 2; Hull 2020, '
              'DOI 10.1017/9781108778633). Schenk and Guest (2013, DOI 10.1073/pnas.1217998110) showed that '
              'this folding geometry yields a scale-independent negative in-plane Poisson ratio; this folio '
              'pairs tan(γ_2/2) = cos α · tan(γ_1/2) with ν_xy = −tan² φ using this folio\'s simplified '
              'parametrization cos φ = sin α · cos(θ/2). In built architecture, the Al Bahar Towers in Abu '
              'Dhabi employ automated PTFE-mesh shading screens inspired by origami and traditional '
              'mashrabiya lattices (Karanouh & Kerber 2015, DOI 10.3233/fde-150040; Attia 2017, DOI '
              '10.5339/connect.2017.qgbc.6). This folio explores a single-drive Miura-ori screen under CSI '
              'MasterFormat 10 71 13, with citation context for Schenk & Guest (2013) checked in Scite '
              '(Nicholson et al. 2021, DOI 10.1162/qss_a_00146).',
 'act1_stakes': 'Traditional Middle Eastern mashrabiya latticework moderates harsh daylight, solar heat gain, '
                'ventilation, and privacy (El Semary, Attalla & Gawad 2017, DOI '
                '10.21625/archive.v1i1.113). Contemporary adaptive facades convert those static screens into '
                'automated shading elements, though multi-unit mechanical drives require durability mockups, '
                'weather stripping, and commissioning (Attia 2017, DOI 10.5339/connect.2017.qgbc.6). '
                'Coupling facets through rigid origami kinematics aims to reduce actuator count, yet real '
                'architectural panels have finite thickness and hinge play that require offset hinge '
                'mechanisms (Tachi 2011, DOI 10.1201/b10971-24). This proposal remains untested.',
 'pullquote': '"In an ideal zero-thickness Miura-ori model, degree-4 vertex constraints couple every facet '
              'into one kinematic degree of freedom (Miura 1985; Schenk & Guest 2013); real panels require '
              'hinge offsets and tolerances (Tachi 2011)."',
 'chronology': [('1985',
                 'Koryo Miura describes biaxial packaging and deployment of large space membranes using a '
                 'herringbone parallelogram fold in ISAS Report No. 618 (Miura 1985).'),
                ('2011',
                 'Tomohiro Tachi formalizes geometric methods for rigid-foldable thick-panel origami beyond '
                 'zero-thickness sheets (DOI 10.1201/b10971-24).'),
                ('2013',
                 'Mark Schenk and Simon D. Guest analyze Miura-ori as a folded metamaterial with a negative '
                 'in-plane Poisson ratio in PNAS (DOI 10.1073/pnas.1217998110).'),
                ('2015–2023',
                 'Karanouh & Kerber (DOI 10.3233/fde-150040) and Attia (DOI 10.5339/connect.2017.qgbc.6) '
                 'document the Al Bahar Towers dynamic screens, while Meloni et al. (DOI '
                 '10.1016/j.scs.2023.104740) and Kahramanoğlu & Çakıcı Alp (DOI 10.1016/j.jobe.2023.106241) '
                 'model origami solar and visual-comfort facades.')],
 'act2_title': 'Act II — How It Actually Works: Spherical Degree-4 Vertex Kinematics + Auxetic '
               'Poisson Inversion',
 'act2_analogy': 'Unlike a carelessly folded road map that snags, a Miura-ori sheet aligns every crease at a '
                 'flat-foldable degree-4 vertex so opposite corners open and close smoothly together (Miura '
                 '1985; Schenk & Guest 2013, DOI 10.1073/pnas.1217998110).',
 'act2_plain_primer': 'The model below varies two geometric parameters of the Miura-ori pattern (Miura 1985): '
                      'deployment fold angle θ (10°–80°) and parallelogram sector angle α (52°–78°). At low θ '
                      'values, the facets unfold outward across the facade plane (small γ_1 and γ_2), '
                      'increasing shading coverage and lowering modeled SHGC (0.10 at 10°, 0.19 at 36°); '
                      'raising θ toward 80° folds the creases more sharply (γ_2 = 40.4° at α = 64°), '
                      'retracting the sheet and raising modeled SHGC toward 0.51. Adjusting α sets the aspect '
                      'ratio and auxetic expansion (Schenk & Guest 2013, DOI 10.1073/pnas.1217998110). '
                      'Responsive Miura-ori louver studies evaluate both solar reflection (Meloni et al. 2023, '
                      'DOI 10.1016/j.scs.2023.104740) and indoor visual comfort (Kahramanoğlu & Çakıcı Alp '
                      '2023, DOI 10.1016/j.jobe.2023.106241); values shown here are outputs of this folio\'s '
                      'simplified model.',
 'distill_diagram': {'analogy_title': 'The Synchronized Miura-Ori Lattice',
                     'analogy_sub': 'Pulls open in length and width simultaneously without facet strain',
                     'force_a_title': 'Deployment Fold Angle (θ)',
                     'force_a_sub': 'Modulates facade shading depth and modeled SHGC',
                     'force_b_title': 'Parallelogram Sector Angle (α)',
                     'force_b_sub': 'Sets geometric aspect ratio and auxetic Poisson response',
                     'threshold_title': 'Auxetic Kinematic State (ν_xy ≈ −0.37, Model)',
                     'threshold_pass': 'One-DOF deployment in ideal rigid model; SHGC 0.19 in model',
                     'threshold_fail': 'Facet bending or binding if vertices violate Kawasaki sum'},
 'act2_intuition': 'Continuing Folio A.04\'s mechanism count (m = 1 collective mode) and Folio M.05\'s '
                   'rigidity framing, consider four rigid parallelogram facets of acute sector angle α '
                   'meeting at a degree-4 vertex obeying Kawasaki\'s and Maekawa\'s conditions (Hull 2020, '
                   'DOI 10.1017/9781108778633). Under primary fold angle γ_1 = θ, this folio uses '
                   'cos φ = sin α · cos(θ/2) and tan(γ_2/2) = cos α · tan(γ_1/2), writing the in-plane '
                   'Poisson ratio as ν_xy = −tan² φ < 0 (Schenk & Guest 2013, DOI '
                   '10.1073/pnas.1217998110, use a distinct fold-angle parametrization). At α = 64° and '
                   'θ = 36°, under the stated assumptions, the model gives φ about 31.3°, ν_xy about −0.37, '
                   'and γ_2 about 16.2°. With assumed SHGC_glass = 0.60 and η_shade = 0.845, '
                   'SHGC = SHGC_glass · (1 − η_shade · cos θ) gives 0.19 (−68.4% in the model). In a '
                   'separate building simulation study, Meloni et al. (2023, DOI '
                   '10.1016/j.scs.2023.104740) reported Miura-fold facades cutting simulated pedestrian-level '
                   'reflected solar irradiance by 61% on average and up to 90%; daylight and cooling loads '
                   'are not computed here.',
 'act2_deepening': 'Because alternate sector angles sum to π and crease parities differ by two (Hull 2020, '
                   'DOI 10.1017/9781108778633), an ideal zero-thickness Miura-ori unit cell moves with one '
                   'degree of freedom (Miura 1985). In this folio\'s parametrization at θ = 36°, |ν_xy| '
                   'decreases as α rises, from about 0.78 at α = 52° to 0.16 at α = 78° (ν_xy rises from '
                   '−0.78 to −0.16). Real architectural panels have finite thickness and thermal expansion: '
                   'without thickness-accommodating hinge offsets (Tachi 2011, DOI 10.1201/b10971-24) and '
                   'perimeter tolerance checks during design-assist mockups and commissioning (Attia 2017, '
                   'DOI 10.5339/connect.2017.qgbc.6), panels bind or bend out of plane. This folio does not '
                   'design those bearings.',
 'walkthrough': ['Experiment 1 (Kinematic Deployment Angle θ): Vary θ from 10° (deployed shading) to 80° '
                 '(retracted creases) to track the modeled in-plane Poisson ratio ν_xy and coupled dihedral '
                 'angle γ_2 (the illustrative SHGC = 0.19 at θ = 36° is stated in Stage 4 and kept static '
                 'in the readout).',
                 'Experiment 2 (Parallelogram Sector Angle α): Vary α from 52° to 78° to track the '
                 'modeled in-plane Poisson ratio ν_xy = −tan² φ and coupled dihedral γ_2.',
                 'Experiment 3 (Stages 1–4): Step through Kawasaki flat-foldability, spherical vertex '
                 'coupling, auxetic expansion, and the illustrative solar-shading rule.'],
 'act4_title': 'Act IV — Deployable Facade Tectonics, Archive Continuity & Upstream Engineering Threads',
 'act4_human_ai': 'Combining Folio A.03\'s daylight framing and Folio A.04\'s exoskeleton maintenance access '
                  'with Miura-ori kinematics (Schenk & Guest 2013, DOI 10.1073/pnas.1217998110), facade '
                  'teams could evaluate adaptive screens using annual glare, solar-reflection, and daylight '
                  'simulations (Meloni et al. 2023, DOI 10.1016/j.scs.2023.104740; Kahramanoğlu & Çakıcı '
                  'Alp 2023, DOI 10.1016/j.jobe.2023.106241). This remains a design proposal; cooling-energy '
                  'savings and structural wind tests are not run here.',
 'act4_deepening': 'In a computational workflow, designers could map facade geometry to annual solar paths, '
                   'model thick-panel hinge offsets (Tachi 2011, DOI 10.1201/b10971-24), and validate '
                   'actuated modules through physical durability mockups and post-occupancy commissioning '
                   '(Attia 2017, DOI 10.5339/connect.2017.qgbc.6). Open engineering questions include '
                   'cyclic wind fatigue across compliant or pinned hinges, acoustic sealing, and '
                   'long-term maintenance costs relative to conventional motorized louvers.',
 'cf_bridge': 'Standalone kinetic-architecture folio (A.04 + A.03 + M.05 -> A.10), written for facade '
              'engineers and computational architects (CSI MasterFormat 10 71 13 covers exterior sun control '
              'devices).',
 'sources': ['Schenk, M., & Guest, S. D. (2013). Geometry of Miura-folded metamaterials. Proceedings of '
             'the National Academy of Sciences (PNAS), 110(9), 3276–3281. DOI: 10.1073/pnas.1217998110.',
             'Miura, K. (1985). Method of packaging and deployment of large membranes in space. Institute of '
             'Space and Astronautical Science Report, 618, 1–9.',
             'Hull, T. C. (2020). Origametry: Mathematical Methods in Paper Folding. Cambridge University '
             'Press. DOI: 10.1017/9781108778633.',
             'Tachi, T. (2011). Rigid-Foldable Thick Origami. In Origami 5 (pp. 253–263). A K Peters/CRC '
             'Press. DOI: 10.1201/b10971-24.',
             'Karanouh, A., & Kerber, E. (2015). Innovations in dynamic architecture. Journal of Facade '
             'Design and Engineering, 3(2), 185–221. DOI: 10.3233/fde-150040.',
             'Attia, S. (2017). Evaluation of adaptive facades: The case study of Al Bahr Towers in the UAE. '
             'QScience Connect, 2017(2). DOI: 10.5339/connect.2017.qgbc.6.',
             'El Semary, Y. M., Attalla, H., & Gawad, I. (2017). Modern Mashrabiyas with High-tech Daylight '
             'Responsive Systems. The Academic Research Community Publication, 1(1), 11. DOI: '
             '10.21625/archive.v1i1.113.',
             'Meloni, M., Zhang, Q., Cai, J., & Lee, D. S.-H. (2023). Origami-based adaptive facade for '
             'reducing reflected solar radiation in outdoor urban environments. Sustainable Cities and '
             'Society, 97, 104740. DOI: 10.1016/j.scs.2023.104740.',
             'Kahramanoğlu, B., & Çakıcı Alp, N. (2023). Enhancing visual comfort with Miura-ori-based '
             'responsive facade model. Journal of Building Engineering, 69, 106241. DOI: '
             '10.1016/j.jobe.2023.106241.',
             'CSI MasterFormat 10 71 13 Exterior Sun Control Devices & 08 44 13 Glazed Aluminum Curtain '
             "Walls. Named for context; neither sets this folio's targets.",
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of '
             'citations and classifies their intent using deep learning (https://scite.ai). Quantitative '
             'Science Studies, 2(3), 882–898. DOI: 10.1162/qss_a_00146.'],
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
 'headline': 'Miura-Ori Spherical Vertex Kinematics & Negative Poisson Ratios in a Design Model for '
             'Deployable Solar Mashrabiya Envelopes',
 'body': "Schenk & Guest showed that a Miura-folded sheet has a negative in-plane Poisson ratio (PNAS, DOI "
         "10.1073/pnas.1217998110). This design study, continuing Folios A.04, A.03 and M.05, uses that "
         "geometry for a proposed one-actuator solar screen: in the folio's simplified model ν_xy ≈ −0.37 "
         "and SHGC = 0.19 at default settings. Model values, not measurements."}

META_3D = ('Miura-Ori Auxetic Saddle & Spherical Vertex Manifold',
 'X/Z: Tessellation Unit-Cell Plane · Y: Isometric Fold Height & Negative Poisson Ratio ν_xy')

ES_TRANSLATION = {'title_es': 'Origami Cinético y Fachadas Biomiméticas Desplegables Miura-Ori: Cinemática '
             'Isométrica de Pliegues, Inversión Auxética de Poisson y Envolventes Mashrabiya',
 'subtitle_es': 'Completando los Folios A.04, A.03 y M.05: estudio de diseño sobre cómo el pliegue de Koryo '
                'Miura (1985) y el análisis de metamateriales plegados de Schenk y Guest (2013) podrían '
                'mover celosías solares adaptativas inspiradas en la mashrabiya.',
 'why_es': 'A diferencia de una liga que se adelgaza al estirarla, una lámina plegada con el patrón '
           'Miura-ori se expande en largo y ancho a la vez con un solo grado de libertad en el modelo rígido '
           'ideal (Miura 1985; Schenk y Guest 2013, DOI 10.1073/pnas.1217998110).',
 'plain_es': 'Una liga común se adelgaza en el centro al estirarse, mientras que una lámina doblada con el '
             'patrón Miura-ori se abre a lo largo y a lo ancho al mismo tiempo con un solo movimiento '
             '(Miura 1985; Schenk y Guest 2013, DOI 10.1073/pnas.1217998110). En arquitectura, las celosías '
             'tradicionales mashrabiya regulan sol, deslumbramiento, ventilación y privacidad (El Semary et '
             'al. 2017, DOI 10.21625/archive.v1i1.113). Este folio explora una pantalla solar plegable '
             'movida por un solo actuador en lugar de decenas de motores; en paneles reales de espesor finito '
             'hacen falta bisagras desplazadas (Tachi 2011, DOI 10.1201/b10971-24). La propuesta no ha sido '
             'probada y aquí no se calculan el ahorro de energía de enfriamiento, la luz natural ni las '
             'cargas de viento.',
 'deep_es': 'Cada vértice de cuatro pliegues del Miura-ori cumple el teorema de Kawasaki (sumas alternas de '
            'ángulos iguales a π) y la regla de Maekawa (|M − V| = 2; Hull 2020, DOI '
            '10.1017/9781108778633), dando un grado de libertad en el modelo rígido de espesor nulo (Miura '
            '1985). Schenk y Guest (2013, DOI 10.1073/pnas.1217998110) mostraron la razón de Poisson negativa '
            'en el plano usando su propia definición angular. Con la parametrización simplificada de este '
            'folio, cos φ = sen α · cos(θ/2), tan(γ_2/2) = cos α · tan(γ_1/2) (con γ_1 = θ) y '
            'ν_xy = −tan² φ dan ν_xy ≈ −0.37 y γ_2 ≈ 16.2° con α = 64° y θ = 36°. Para la sombra solar, el '
            'modelo usa SHGC = SHGC_vidrio · (1 − η · cos θ) con valores supuestos SHGC_vidrio = 0.60 y '
            'η = 0.845, obteniendo 0.19 (−68.4 % en el modelo); son valores de modelo, no mediciones, y el '
            'ensamblaje sigue sin probarse. Precedentes construidos como las torres Al Bahar (Karanouh y '
            'Kerber 2015, DOI 10.3233/fde-150040; Attia 2017, DOI 10.5339/connect.2017.qgbc.6) y '
            'simulaciones recientes de fachadas Miura-ori (Meloni et al. 2023, DOI '
            '10.1016/j.scs.2023.104740; Kahramanoğlu y Çakıcı Alp 2023, DOI 10.1016/j.jobe.2023.106241) '
            'motivan este estudio.'}
