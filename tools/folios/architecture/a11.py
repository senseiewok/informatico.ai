#!/usr/bin/env python3
"""Folio A.11 (ARCHITECTURE): 3D Polyhedral Graphic Statics & Airy Stress Surfaces: Maxwell–Rankine Reciprocal Polyhedra, Guastavino Tile Vaulting & Zero-Rebar Floors."""
from __future__ import annotations

SLUG = 'a11'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.11',
 'slug': 'a11',
 'pillar': 'architecture',
 'category_code': 'A',
 'parent_folios': ['A.01', 'A.02'],
 'lineage_mode': 'CONTINUATION · Continues A.01 Funicular Masonry Vaults & A.02 Reciprocal '
                 'Gridshells',
 'title': '3D Polyhedral Graphic Statics & Airy Stress Surfaces: Maxwell–Rankine Reciprocal '
          'Polyhedra, Guastavino Tile Vaulting & Zero-Rebar Floors',
 'subtitle': 'An explanatory model linking 2D Airy stress surfaces, 3D reciprocal force polyhedra, '
             'and an untested exterior roof sky-cooling calculation; not a structural design method.',
 'date_published': '2026-11-07',
 'date_redated': '2026-11-21',
 'current_edition': 'REV 1.6',
 'status_badge': '3D STATICS + SKY-COOLING · REV 1.6',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'σ_xx = Φ_yy · σ_yy = Φ_xx · Φ_xx, Φ_yy < 0, det(H_Φ) > 0 (2D Airy) · N_i ∝ A_i^* (3D) · q_net(T_a)',
 'colophon': {'identifier': 'A.11 · 3D Polyhedral Graphic Statics & Sky-Cooling Vaults · REV 1.6',
              'kernels': '2D Airy Concavity (Φ_xx, Φ_yy < 0, det(H_Φ) > 0) · 3D Dual Polyhedra (Γ ↔ Γ^*) · 8–13 μm Cooling',
              'benchmarks': 'Fixed values: det(H_Φ) = +1.84 · q_net(T_a) = 98.4 W/m² · ΔT_eq ≈ −7.08 °C (assumed 134.0 W/m², 13.9 W/(m²·K))',
              'bridge': 'Continues A.01/A.02 · Separate 7-voussoir arch kit in Toolbox X.03'},
 'sliders': [{'label': 'Reciprocal Force Polyhedron Scale (ζ_dual)',
              'min': 0.5,
              'max': 2.0,
              'step': 0.05,
              'value': 1.15,
              'unit': 'ζ = '},
             {'label': 'Ribbed Vault Crown Rise-to-Span (f / L)',
              'min': 0.08,
              'max': 0.3,
              'step': 0.01,
              'value': 0.16,
              'unit': 'f/L = '}],
 'steps': ['Stage 1 (2D Airy Stress Surface): In 2D membrane models (tension-positive), σ_xx = Φ_yy, '
           'σ_yy = Φ_xx, σ_xy = −Φ_xy. Maxwell (1864, DOI 10.1080/14786446408643663; 1870) linked '
           'plane frames to polyhedra and stress functions; Thrust Network Analysis (Block & '
           'Ochsendorf 2007) projects 3D vault forces onto a 2D Airy surface.',
           'Stage 2 (3D Reciprocal Polyhedra Γ ↔ Γ^*): Separately, 3D polyhedral graphic statics '
           '(Akbarzadeh, Van Mele & Block 2015, DOI 10.1016/j.cad.2015.01.006) maps each bar '
           'perpendicular to a closed force-cell face, with axial force proportional to face area '
           '(N_i ∝ A_i^*); cell closure means nodal forces balance.',
           'Stage 3 (Concavity & Safety Boundary): Negative-definite Hessian (Φ_xx < 0, Φ_yy < 0, '
           'det(H_Φ) > 0) means the 2D model is compressive under one load case. This folio is an '
           'explanation, not a design method; none of its untested numbers (including t = 52 mm or '
           'det(H_Φ) = +1.84) may be used on a real structure.',
           'Stage 4 (Separate Exterior Sky-Cooling Pairing): For an exposed roof only (not a floor), '
           'assuming a P(VdF-HFP) coating (Mandal et al. 2018, DOI 10.1126/science.aat9513) with '
           'R_solar = 0.96 under 890 W/m² absorbs 35.6 W/m². With a lumped illustrative sky '
           'exchange of 134.0 W/m² at T_a = 303.15 K and assumed h_comb = 13.9 W/(m²·K), '
           'q_net(T_a) = 98.4 W/m² and ΔT_eq ≈ −7.08 °C. Toolbox X.03 (/toolchain/x03/) has a '
           'separate 7-voussoir arch STEP AP242 kit.'],
 'readouts': [{'label': 'Airy Hessian Determinant det(H_Φ)',
               'value': '+1.84 > 0 (Fixed Text, Φ_xx, Φ_yy < 0)'},
              {'label': 'Dual Polyhedron Closure Error',
               'value': 'Closed by Construction (Fixed Text, No Solver)'},
              {'label': '8–13 μm Sky-Cooling Net Flux',
               'value': '98.4 W/m² at T_a · ΔT_eq ≈ −7.08 °C (Fixed Text)'},
              {'label': 'A.11 Model Boundary',
               'value': 'EXPLANATORY MODEL · NOT A DESIGN METHOD'}],
 'spec_plate': {'division': 'EXPLANATORY PAIRING · CSI 04 20 00 / 07 56 00 (NOT A DESIGN SPEC)',
                'title': 'Illustrative Pairing: Funicular Compression Vaults & Exterior 8–13 μm '
                         'Sky-Cooling Coating',
                'body': 'Explanatory pairing only, not a design method or tested assembly: 3D '
                        'reciprocal force polyhedra (tools such as compas-dev/compas) paired on an '
                        'exposed roof with a porous P(VdF-HFP) coating at assumed R_solar = 0.96. '
                        'None of these untested numbers may be used on a real structure.',
                'meta': 'Akbarzadeh et al. 2015 (DOI 10.1016/j.cad.2015.01.006) · Raman et al. 2014 '
                        '(DOI 10.1038/nature13883) · Mandal et al. 2018 (DOI '
                        '10.1126/science.aat9513) · Fixed illustrative values'},
 'sidenote_1': {'kicker': 'SIDENOTE A.11-A · ANALOGY · SOAP FOAM & GUASTAVINO TILE VAULTS',
                'body': 'Rafael Guastavino and his son emigrated from Spain in 1881 and built '
                        'hundreds of thin timbrel tile vaults in the United States (López López et '
                        'al. 2023, DOI 10.3390/buildings13082052). 3D polyhedral graphic statics '
                        'came a century later and played no part in their work. The soap-foam '
                        'picture is an analogy for static force balance under one load case.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.11-B · DAYTIME SKY-COOLING & TOOLBOX X.03',
                'body': 'Mandal et al. (2018, DOI 10.1126/science.aat9513) reported porous '
                        'P(VdF-HFP) coatings about 6 °C below ambient under 890 W/m² of sun and '
                        'about 96 W/m² of cooling under 750 W/m². Under stated assumptions, this '
                        "folio's roof calculation gives 98.4 W/m² at air temperature. Toolbox X.03 "
                        '(/toolchain/x03/) offers a separate 7-voussoir arch STEP AP242/GLB kit.'},
 'skill': {'filename': '3d-polyhedral-graphic-statics-SKILL.md',
           'name': '3d-polyhedral-graphic-statics',
           'description': 'Explanatory companion for 3D Polyhedral Graphic Statics, 2D Airy '
                          'concavity, and exterior 8–13 μm sky-cooling arithmetic. Explanation '
                          'only, not a design method; no folio number may be used on a real '
                          'structure.',
           'rules': ['Explanation only, not a structural design method: no thickness, stress, or '
                     'cooling number from this folio may be used on a real structure.',
                     'In 3D reciprocal force diagrams Gamma^*, verify each polyhedral cell closes '
                     '(e.g. ||sum F_i|| < 1e-12 kN) with axial force proportional to face area '
                     '(N_i proportional to A_i^*).',
                     'In a 2D Airy model (tension-positive), check Phi_xx < 0, Phi_yy < 0, and '
                     'det(H_Phi) > 0 for one load case; this does not check buckling, sliding, '
                     'support movement, or asymmetric loads.',
                     'For an exposed roof only, distinguish cooling power at air temperature '
                     'q_net(T_a) = q_sky_net(T_a) - q_solar*(1 - R_solar) from steady-state '
                     'q_net(T_s) = 0, and estimate Delta T_eq = -q_net(T_a) / h_comb under stated '
                     'assumptions. Treat 80 W/m^2 and -4.5 C as untested illustrative benchmarks.']},
 'revisions': [{'edition': 'REV 1.6',
                'date': '2026-11-21',
                'summary': 'REV 1.6 (Redated 2026-11-21): Removed "design study" labels and the '
                           'unsafe "cannot fall down" claim; added an explicit non-design '
                           'structural boundary in Act I, Spanish, and SKILL.md. Aligned Act III '
                           'with solvers.mjs (sliders update labels only; readouts are fixed text, '
                           'no counterfactual solver), fixed SVG N_i ∝ A_i^* and dispatch edition, '
                           'separated 2D Airy from 3D polyhedra and floors from roofs, added '
                           'Maxwell (1864), corrected López López et al. (2023), cut uncited '
                           'history, and fixed US spellings.',
                'opus': 'Multi-family audit (Gemini 4 pro-tier + Ornith 1.5 35B); solver behavior '
                        'checked in solvers.mjs:1548-1554; citations verified offline.'},
               {'edition': 'REV 1.5',
                'date': '2026-11-14',
                'summary': "REV 1.5 (Redated 2026-11-14): Grounding revision. Replaced unsourced "
                           'Maxwell/Guastavino scenes and 70-72% claims with a plain account and '
                           'Küpfer et al. (2025). Withdrew unmeasured pass/certification wording; '
                           'labeled 80 W/m² and −4.5 °C as illustrative benchmarks.',
                'opus': 'Review: DOIs checked in Crossref and Scite; arithmetic recomputed from '
                        'the stated balance.'},
               {'edition': 'REV 1.4',
                'date': '2026-11-10',
                'summary': 'REV 1.4 (Redated 2026-11-10): Paired 3D polyhedral graphic statics '
                           '(DOI 10.1016/j.cad.2015.01.006) with 8–13 μm sky-cooling coatings '
                           '(Raman et al. 2014, DOI 10.1038/nature13883; Mandal et al. 2018, DOI '
                           '10.1126/science.aat9513) and linked Toolbox X.03.',
                'opus': "Council review (Gemini 4 Argon + Qwen 3.8 27B + Gemma 4 31B). 'Verified' "
                        'wording withdrawn in REV 1.5: no solver ran and cooling numbers depend on '
                        'stated assumptions.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-07',
                'summary': 'REV 1.0 (Published 2026-11-07): Initial Volume VI monograph continuing '
                           'A.01 & A.02 via Heyman (DOI 10.1017/cbo9781107050310) and '
                           'compas-dev/compas.',
                'opus': "Council review (Gemini 4 Argon + Qwen 3.8 27B + Gemma 4 31B). 'Verified' "
                        'wording withdrawn in REV 1.5: the relation is proportionality and nothing '
                        'was computed.'}],
 'volume': 6,
 'volume_code': 'VOL. 06',
 'reading_time': '19 MIN READ',
 'word_count': '4,100 WORDS',
 'scite': {'doi': '10.1016/j.cad.2015.01.006',
           'fetched_on': '2026-11-08',
           'citing_publications': 93,
           'supporting': 0,
           'mentioning': 55,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Akbarzadeh, Van Mele & Block, On the equilibrium of '
                      'funicular polyhedral frames and convex polyhedral force diagrams (DOI '
                      '10.1016/j.cad.2015.01.006), checked 2026-11-08: 93 citing publications (0 '
                      'supporting, 55 mentioning, 0 contrasting) and no retraction notice. The '
                      "counts describe that paper, not this folio's model."}}

LONGFORM_DATA = {'reading_time': '19 MIN READ',
 'word_count': '4,100 WORDS',
 'parent_folios': ['A.01', 'A.02'],
 'lineage_mode': 'CONTINUATION · Continues A.01 Funicular Masonry Vaults & A.02 Reciprocal '
                 'Gridshells',
 'scite': {'doi': '10.1016/j.cad.2015.01.006',
           'fetched_on': '2026-11-08',
           'citing_publications': 93,
           'supporting': 0,
           'mentioning': 55,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Akbarzadeh, Van Mele & Block, On the equilibrium of '
                      'funicular polyhedral frames and convex polyhedral force diagrams (DOI '
                      '10.1016/j.cad.2015.01.006), checked 2026-11-08: 93 citing publications (0 '
                      'supporting, 55 mentioning, 0 contrasting) and no retraction notice. The '
                      "counts describe that paper, not this folio's model."},
 'act1_title': 'Act I — How Thin Masonry Vaults Stand in Compression',
 'act1_dropcap': 'In 1864, James Clerk Maxwell published a paper on reciprocal figures and diagrams '
                 'of forces. He showed that when a drawing of a flat frame is the projection of a '
                 'closed polyhedron, the bars can carry balanced internal forces. Six years later, '
                 'Maxwell read that lifted polyhedron as an Airy stress surface for '
                 'two-dimensional frames. Masonry vaults rely on a similar principle of balance. '
                 'Stone and clay tile resist squeezing far better than pulling, so a curved vault '
                 'stands when gravity travels through it in compression. Rafael Guastavino and his '
                 'son emigrated from Spain in 1881 and built hundreds of thin timbrel tile vaults '
                 'across the United States. López López and colleagues documented those vaults in '
                 "2023. This folio explains how Maxwell's nineteenth-century geometry connects to "
                 'three-dimensional force polyhedra and a separate roof-cooling calculation. It is '
                 'an explanation, not a structural design method.',
 'act1_plain_bridge': 'In plain words, think about how stone and plain concrete respond to force. '
                      'If you pull a stone block apart, it cracks quickly. If you squeeze that '
                      'same block, it carries heavy weight. A flat concrete slab bends under '
                      'gravity, stretching its bottom face and requiring steel bars to resist that '
                      'tension. An arched vault redirects weight along curved paths so neighboring '
                      'blocks press together in compression. With modern geometry software, '
                      'researchers map those internal pushes as three-dimensional polyhedra. When '
                      'every cell of that force diagram closes, the modeled forces balance at each '
                      'joint for one assumed load. Even then, perimeter supports or ties must '
                      'resist the outward sideways thrust. A separate roof calculation also '
                      'illustrates daytime sky cooling on an exposed vault top. This folio is an '
                      'explanation of the geometry, not a design method, and none of its numbers '
                      'may be used on a real structure.',
 'act1_body': "In Folio A.01 we examined Hooke's hanging chain and Heyman's plastic limit theorems "
              '(The Stone Skeleton, 1995, DOI 10.1017/cbo9781107050310), while López López et al. '
              '(2023, DOI 10.3390/buildings13082052) document historic Guastavino tile vaults. Real '
              'vaults span three dimensions, where 2D slices are only approximations. Maxwell '
              '(1864, DOI 10.1080/14786446408643663; 1870) linked plane frames to polyhedra and 2D '
              'Airy stress surfaces, and Calladine (1978, DOI 10.1016/0020-7683(78)90052-5) '
              "revisited Maxwell's frame-stiffness count. Block and Ochsendorf (2007) used "
              'horizontal force projections in Thrust Network Analysis for 3D vaults, whereas '
              'Akbarzadeh, Van Mele, and Block (2015, DOI 10.1016/j.cad.2015.01.006) extended '
              "graphic statics to 3D polyhedral force diagrams; ETH Zurich's group also develops "
              'the open-source COMPAS framework (https://github.com/compas-dev/compas). Separately, '
              'this folio pairs that explanation with a roof-only radiative cooling calculation '
              'citing Raman et al. (2014, DOI 10.1038/nature13883) and Mandal et al. (2018, DOI '
              '10.1126/science.aat9513), and points to a separate 7-voussoir arch kit in Toolbox '
              'X.03 (/toolchain/x03/). This folio is an explanation, not a design method, and none '
              'of its untested numbers may be used on a real structure.',
 'act1_stakes': 'Flat reinforced-concrete slabs carry gravity by bending and rely on steel bars to '
                'resist tension, where moisture and carbonation may cause corrosion over time. '
                'Unreinforced funicular vaults aim to reduce material volume inside the vault '
                'itself: Küpfer et al. (2025, DOI 10.1088/1755-1315/1554/1/012083) report that one '
                'published unreinforced funicular floor uses about one-third of the material of a '
                'conventional flat slab. Outward thrust still requires ties or supports, and '
                'long-term durability is a caveat this folio does not answer.',
 'pullquote': '"In 3D graphic statics, a closed force polyhedron expresses nodal balance for one '
              'modeled load, and a concave 2D Airy surface marks compressive stresses in the model. '
              'Neither is a design check for a real vault."',
 'chronology': [('1864–1870',
                 'James Clerk Maxwell (1864, DOI 10.1080/14786446408643663; 1870) links plane '
                 'frames in equilibrium to polyhedra and stress functions.'),
                ('1881 onward',
                 'Rafael Guastavino and his son emigrate from Spain and build hundreds of timbrel '
                 'tile vaults in the United States (López López et al. 2023, DOI '
                 '10.3390/buildings13082052).'),
                ('1978–2015',
                 'Calladine (DOI 10.1016/0020-7683(78)90052-5), Heyman (DOI '
                 '10.1017/cbo9781107050310), Block & Ochsendorf (2007), and Akbarzadeh et al. '
                 '(DOI 10.1016/j.cad.2015.01.006) advance frame rigidity, limit analysis, Thrust '
                 'Network Analysis, and 3D polyhedral graphic statics.'),
                ('2014–2018',
                 'Raman et al. (DOI 10.1038/nature13883) and Mandal et al. (DOI '
                 '10.1126/science.aat9513) report daytime radiative sky cooling; this folio pairs '
                 'that exterior roof calculation with graphic statics as an explanatory model.')],
 'act2_title': 'Act II — Cross-Field Intuition: Soap-Foam Dual Polyhedra & Concave Stress Bowls',
 'act2_analogy': 'Picture a cluster of soap bubbles resting inside a wire frame. Each bubble cell '
                 'is closed on every side, so surface-tension pulls meet in balance at every seam. '
                 'Flip that geometric picture upside down: tension pulls map to compressive pushes '
                 'along stone ribs, and closed cells encode balanced forces at each joint. Where '
                 'the analogy stops: soap films carry uniform tension without buckling, sliding, '
                 'or support settlement. A real stone vault could still hinge, slide, crush, or '
                 'collapse under uneven live loads even when an idealized force cell closes.',
 'act2_plain_primer': 'Below, the laboratory lists two teaching parameters before any notation. '
                      'The Reciprocal Force Polyhedron Scale knob is an overall multiplier on the '
                      'dual force diagram: scaling it up corresponds conceptually to larger '
                      'internal forces and horizontal thrust. The Ribbed Vault Crown Rise-to-Span '
                      'knob represents arch steepness: shallower arches increase outward thrust, '
                      'while steeper rises direct loads more steeply downward. On this page, '
                      'dragging either slider updates only its label and visual preview; the four '
                      'readout cards stay fixed illustrative text and no solver runs.',
 'distill_diagram': {'analogy_title': 'Inverted Soap-Bubble Foam (Analogy)',
                     'analogy_sub': 'Closed cells represent static balance for one idealized load case',
                     'force_a_title': 'Reciprocal Force Polyhedron Scale (ζ_dual)',
                     'force_a_sub': 'Conceptual dual multiplier; slider updates label only',
                     'force_b_title': 'Ribbed Vault Crown Rise-to-Span (f / L)',
                     'force_b_sub': 'Conceptual arch steepness; slider updates label only',
                     'threshold_title': '2D Airy Concavity: Φ_xx, Φ_yy < 0, det(H_Φ) > 0',
                     'threshold_pass': 'Compressive 2D model stress field under one assumed load case',
                     'threshold_fail': 'Open dual cell or non-negative curvature violates pure-compression model'},
 'act2_intuition': '3D polyhedral graphic statics (Akbarzadeh et al. 2015, DOI '
                   '10.1016/j.cad.2015.01.006; tools such as compas-dev/compas) pairs a 3D Form '
                   'Diagram Γ of bars with a Reciprocal Force Diagram Γ^* of convex polyhedral '
                   'cells. Each strut e_i is perpendicular to a face f_i^* in Γ^*, with face area '
                   'A_i^* proportional to axial force N_i (N_i ∝ A_i^*). Because outward area '
                   'vectors of a closed polyhedron sum to zero, each closed cell encodes nodal '
                   'equilibrium. Separately, for 2D membrane states (or the horizontal force '
                   'projection in Thrust Network Analysis, Block & Ochsendorf 2007), an Airy '
                   'surface Φ(x, y) satisfies σ_xx = Φ_yy, σ_yy = Φ_xx, and σ_xy = −Φ_xy under the '
                   'tension-positive convention. Negative-definite curvature (Φ_xx < 0, Φ_yy < 0, '
                   'det(H_Φ) = Φ_xx Φ_yy − Φ_xy² > 0) means the 2D model stress field is '
                   'compressive everywhere for that load case. The readout det(H_Φ) = +1.84 is '
                   'fixed illustrative text; no simulation ran here.',
 'act2_deepening': 'This folio pairs two separate published methods—graphic statics for vaults and '
                   'daytime radiative cooling for an exposed roof extrados (not an interior '
                   'floor)—purely as an explanation. Structurally, a higher rise-to-span ratio f/L '
                   'could lower horizontal thrust; the default f/L = 0.16 is illustrative and '
                   'untested. Thermally, citing Raman et al. (2014, DOI 10.1038/nature13883) and '
                   'Mandal et al. (2018, DOI 10.1126/science.aat9513) for porous P(VdF-HFP) '
                   'coatings, the model assumes solar reflectance R_solar = 0.96 under 890 W/m² of '
                   'sunlight, absorbing (1 − 0.96) × 890 = 35.6 W/m². Assigning a lumped '
                   'illustrative sky exchange of 134.0 W/m² at air temperature T_a = 303.15 K '
                   '(30.0 °C)—not computed from a spectral emissivity model—gives q_net(T_a) = '
                   '134.0 − 35.6 = 98.4 W/m². Dividing by an assumed combined coefficient '
                   'h_comb = 13.9 W/(m²·K) estimates ΔT_eq ≈ −7.08 °C; stronger wind may shrink '
                   'that drop. For comparison, Mandal et al. measured about 6 °C below ambient '
                   'under 890 W/m². Interior room cooling is not yet modeled, and none of these '
                   'untested numbers may be used on a real building.',
 'walkthrough': ['Experiment 1 (Reciprocal Force Polyhedron Scale ζ_dual): Drag Reciprocal Force '
                 'Polyhedron Scale (ζ_dual) from 0.50 to 2.00. The slider updates only the '
                 'displayed ζ label and preview; all four readout cards hold fixed illustrative '
                 'text.',
                 'Experiment 2 (Ribbed Vault Crown Rise-to-Span f / L): Drag Ribbed Vault Crown '
                 'Rise-to-Span (f / L) from 0.08 to 0.30. Only the f/L label updates; '
                 'det(H_Φ) = +1.84 and the cooling figures stay fixed because no solver runs.',
                 'Experiment 3 (4-Stage Stepper & 3D Orbit): Click Stage buttons 1 through 4 above '
                 'the plate to inspect 2D Airy surfaces, 3D dual polyhedra, safety boundaries, and '
                 'the separate roof-cooling arithmetic, or drag the 3D preview to orbit it.'],
 'act4_title': 'Act IV — Open Research Directions: Open-Source Graphic Statics & Passive Roof '
               'Coatings',
 'act4_human_ai': 'Open-source tools such as compas-dev/compas '
                  '(https://github.com/compas-dev/compas) and neutral CAD exporters like the '
                  'separate 7-voussoir arch kit in Toolbox X.03 (/toolchain/x03/) let readers '
                  'study compression geometry without proprietary licenses. Pairing roof vaults '
                  'with porous P(VdF-HFP) sky-cooling coatings (Mandal et al. 2018, DOI '
                  '10.1126/science.aat9513) is an untested research concept; this folio estimates '
                  'no steel, cost, or air-conditioning savings.',
 'act4_deepening': 'This folio ran no COMPAS simulation; a reader could use COMPAS to test '
                   'polyhedral closure and export STEP AP242, 3MF, DXF, or GLB files. Open '
                   'caveats before any real use include seismic behavior, support settlement, '
                   'falsework-free assembly, and outdoor weathering of 8–13 μm radiative coatings '
                   '(Raman et al. 2014, DOI 10.1038/nature13883; Mandal et al. 2018, DOI '
                   '10.1126/science.aat9513).',
 'cf_bridge': 'Explanatory Architecture Monograph (A.01 + A.02 → A.11; separate arch kit in '
              'Toolbox X.03): Introduces 2D Airy concavity, 3D dual polyhedra, and exterior roof '
              'sky-cooling arithmetic; not a structural design method.',
 'sources': ['Maxwell, J. C. (1864). XLV. On reciprocal figures and diagrams of forces. The '
             'London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, '
             '27(182), 250–261. DOI: 10.1080/14786446408643663.',
             'Akbarzadeh, M., Van Mele, T., & Block, P. (2015). On the equilibrium of funicular '
             'polyhedral frames and convex polyhedral force diagrams. Computer-Aided Design, 63, '
             '118–128. DOI: 10.1016/j.cad.2015.01.006.',
             'Raman, A. P., Anoma, M. A., Zhu, L., Rephaeli, E., & Fan, S. (2014). Passive '
             'radiative cooling below ambient air temperature under direct sunlight. Nature, '
             '515(7528), 540–544. DOI: 10.1038/nature13883.',
             'Mandal, J., Fu, Y., Overvig, A. C., Jia, M., Sun, K., Shi, N. N., Zhou, H., Xiao, '
             'X., Yu, N., & Yang, Y. (2018). Hierarchically porous polymer coatings for highly '
             'efficient passive daytime radiative cooling. Science, 362(6412), 315–319. DOI: '
             '10.1126/science.aat9513.',
             'Heyman, J. (1995). The Stone Skeleton: Structural Engineering of Masonry '
             'Architecture. Cambridge University Press. DOI: 10.1017/cbo9781107050310.',
             "Calladine, C. R. (1978). Buckminster Fuller's 'Tensegrity' structures and Clerk "
             "Maxwell's rules for the construction of stiff frames. International Journal of "
             'Solids and Structures, 14(2), 161–172. DOI: 10.1016/0020-7683(78)90052-5.',
             'Block, P., & Ochsendorf, J. (2007). Thrust Network Analysis: A new methodology for '
             'three-dimensional equilibrium. Journal of the IASS, 48(3), 167–173.',
             'López López, D., et al. (2023). Multi-Level Numerical Modelling and Analysis of '
             'Tile Vaults. Buildings, 13(8), 2052. DOI: 10.3390/buildings13082052.',
             'Küpfer, C., Bertola, N., Jayasinghe, A., Orr, J., & Fivet, C. (2025). Concrete '
             'floors: multi-criteria analysis of conventional and novel solutions. IOP Conference '
             'Series: Earth and Environmental Science, 1554(1), 012083. DOI: '
             '10.1088/1755-1315/1554/1/012083.',
             'Open-Source Stack: COMPAS computational framework for architecture and structures '
             '(https://github.com/compas-dev/compas) & Informatico Toolbox X.03 (/toolchain/x03/).',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="3D Polyhedral '
        'Graphic Statics Form Diagram Vault and Reciprocal Minkowski Force Polyhedron">\n'
        '            <line x1="35" y1="188" x2="645" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <text x="44" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">Form Diagram Γ: Illustrative Vault (t = 52 mm, Not for Real Use)</text>\n'
        '            <path d="M 52 162 Q 195 44 338 162" fill="var(--tp-stone)" '
        'fill-opacity="0.28" stroke="var(--tp-prussian)" stroke-width="3.2"/>\n'
        '            <path d="M 86 142 Q 195 66 304 142" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="2.2"/>\n'
        '            <line x1="52" y1="72" x2="338" y2="72" stroke="currentColor" '
        'stroke-opacity="0.45" stroke-width="2"/>\n'
        '            <line x1="110" y1="72" x2="110" y2="112" stroke="var(--tp-prussian)" '
        'stroke-width="1.8"/>\n'
        '            <line x1="195" y1="72" x2="195" y2="96" stroke="var(--tp-prussian)" '
        'stroke-width="1.8"/>\n'
        '            <line x1="280" y1="72" x2="280" y2="112" stroke="var(--tp-prussian)" '
        'stroke-width="1.8"/>\n'
        '            <text x="54" y="178" font-size="9.5" fill="var(--tp-verdigris)">2D Airy '
        'Concavity: Φ_xx, Φ_yy &lt; 0, det(H_Φ) = +1.84 (Fixed Value)</text>\n'
        '            <line x1="368" y1="24" x2="368" y2="192" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="386" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">Reciprocal Force Polyhedron Γ^* (N_i ∝ A_i^*)</text>\n'
        '            <g transform="translate(508, 108)">\n'
        '              <polygon points="0,-54 58,-18 38,44 -38,44 -58,-18" '
        'fill="var(--tp-verdigris)" fill-opacity="0.18" stroke="var(--tp-prussian)" '
        'stroke-width="2.2"/>\n'
        '              <line x1="0" y1="-54" x2="0" y2="8" stroke="var(--tp-minium)" '
        'stroke-width="1.8"/>\n'
        '              <line x1="0" y1="8" x2="58" y2="-18" stroke="var(--tp-minium)" '
        'stroke-width="1.8"/>\n'
        '              <line x1="0" y1="8" x2="-58" y2="-18" stroke="var(--tp-minium)" '
        'stroke-width="1.8"/>\n'
        '              <line x1="0" y1="8" x2="38" y2="44" stroke="var(--tp-verdigris)" '
        'stroke-width="1.8"/>\n'
        '              <line x1="0" y1="8" x2="-38" y2="44" stroke="var(--tp-verdigris)" '
        'stroke-width="1.8"/>\n'
        '              <circle cx="0" cy="8" r="4.5" fill="var(--tp-minium)"/>\n'
        '            </g>\n'
        '            <text x="386" y="178" font-size="9.5" fill="var(--tp-prussian)">Closed '
        'Dual Cells ⇒ Nodal Balance for One Load Case</text>\n'
        '            <text x="44" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Explanatory Model · Fixed Values · Not a Design Method</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a dry-stacked limestone and Guastavino tile '
        'funicular vaulted hall with glowing 3D reciprocal force polyhedra suspended in midair '
        'would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.11-V (Imagining What It Would Look Like) · Artistic '
            'visualization (continuing A.01 & A.02) imagining an unreinforced ribbed vault '
            'alongside a 3D reciprocal force polyhedron.'}

DISPATCH = {'kicker': 'FRONTIER COMPUTATIONAL ARCHITECTURE DISPATCH · A.11 · REV 1.6',
 'headline': 'Explanatory Model: 3D Polyhedral Graphic Statics & Exterior 8–13 μm Sky-Cooling '
             'Coatings',
 'body': 'This folio explains 3D reciprocal force polyhedra (Akbarzadeh et al. 2015, DOI '
         '10.1016/j.cad.2015.01.006) alongside a separate roof-only radiative cooling calculation '
         'citing Raman et al. (2014, DOI 10.1038/nature13883) and porous P(VdF-HFP) coatings from '
         'Mandal et al. (2018, DOI 10.1126/science.aat9513). Under stated assumptions (134.0 W/m² '
         'sky exchange at air temperature, h_comb = 13.9 W/(m²·K)), the model estimates 98.4 W/m² '
         'and about −7.08 °C. Separately, Küpfer et al. (2025) report an unreinforced funicular '
         'floor using about one-third the material of a flat slab. Explanatory model only, not a '
         'design method.'}

META_3D = ('Maxwell–Airy 3D Concave Stress & Thrust Network Surface',
 'X: Span Coordinate x/L · Z: Transverse Coordinate y/L · Y: Airy Stress Potential Φ(x, y)')

ES_TRANSLATION = {'title_es': 'Estática Gráfica Poliédrica 3D y Superficies de Esfuerzo de Airy: Poliedros '
             'Recíprocos de Maxwell, Bóvedas de Guastavino y Pisos sin Acero',
 'subtitle_es': 'Modelo explicativo que conecta superficies de Airy en 2D, poliedros recíprocos '
                '3D y un cálculo hipotético de enfriamiento radiativo en azotea; no es un método '
                'de diseño estructural.',
 'why_es': 'Como una espuma de jabón con celdas cerradas en equilibrio, un diagrama poliédrico '
           'cerrado expresa equilibrio nodal para una carga idealizada. Dónde termina la analogía: '
           'una bóveda real aún puede pandearse, deslizarse o colapsar si cambian las cargas o '
           'ceden los apoyos. Este folio es una explicación, no un método de diseño, y ninguna de '
           'sus cifras puede usarse en una estructura real.',
 'bridge_es': 'Modelo explicativo (no un método de diseño): los controles del laboratorio solo '
              'actualizan sus etiquetas y las cuatro tarjetas muestran cifras ilustrativas fijas.',
 'plain_es': 'En palabras sencillas, piensen en cómo responden la piedra y el concreto simple ante '
             'una fuerza. Si jalan un bloque de piedra, se agrieta rápido. Si lo comprimen, '
             'soporta un peso enorme. Una losa plana de concreto se flexiona por gravedad, estira '
             'su cara inferior y necesita varillas de acero para resistir esa tensión. Una bóveda '
             'curva dirige el peso por trayectorias curvas para que los bloques se empujen en '
             'compresión. Con programas modernos de geometría, los investigadores representan esos '
             'empujes como poliedros tridimensionales. Cuando cada celda del diagrama de fuerzas '
             'cierra, las fuerzas del modelo se equilibran en cada nodo para una carga supuesta. '
             'Aun así, muros o tirantes deben resistir el empuje lateral. Un cálculo aparte '
             'ilustra el enfriamiento radiativo en una cubierta exterior. Este folio es una '
             'explicación, no un método de diseño, y ninguna de sus cifras puede usarse en una '
             'estructura real.',
 'deep_es': 'Este folio es una explicación, no un método de diseño, y ninguna de sus cifras puede '
            'usarse en una estructura real. Separa dos marcos: superficies de Airy en 2D (o '
            'proyecciones de Block y Ochsendorf 2007), donde Φ_xx, Φ_yy < 0 y det(H_Φ) > 0 '
            'indican compresión en el modelo para una carga, y estática gráfica poliédrica 3D '
            '(Akbarzadeh et al. 2015, DOI 10.1016/j.cad.2015.01.006), donde cada celda cerrada '
            'expresa equilibrio nodal con N_i ∝ A_i^*. En el navegador, los dos controles solo '
            'actualizan sus etiquetas; las cuatro lecturas son texto ilustrativo fijo y no corre '
            'ningún solucionador. Aparte, solo para una azotea expuesta (no un entrepiso), el '
            'modelo cita a Raman et al. (2014, DOI 10.1038/nature13883) y Mandal et al. (2018, '
            'DOI 10.1126/science.aat9513): con R_solar = 0.96 bajo 890 W/m² (absorbe 35.6 W/m²), '
            'intercambio neto ilustrativo de 134.0 W/m² a temperatura del aire y h_comb supuesto '
            'de 13.9 W/(m²·K), estima q_net(T_a) = 98.4 W/m² y ΔT_eq ≈ −7.08 °C. La Herramienta '
            'X.03 (/es-mx/toolchain/x03/) ofrece un kit aparte de arco de siete dovelas en STEP '
            'AP242.'}
