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
 'subtitle': "Continuing Folio A.01's 2D catenary thrust lines and A.02's reciprocal frames: a design study of how James Clerk Maxwell's reciprocal figures and polyhedral graphic statics, with tools such as the open-source COMPAS framework, shape compression-only vaults; one published unreinforced funicular floor uses about a third of the material of a flat slab.",
 'date_published': '2026-11-07',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.5',
 'status_badge': '3D STATICS + SKY-COOLING · REV 1.5',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'σ_xx = Φ_yy · σ_yy = Φ_xx · det(H_Φ) > 0 · N_i ∝ A_i^* · q_net(8–13 μm) (folio design target ≥ 80 W/m²)',
 'colophon': {'identifier': 'A.11 · 3D Polyhedral Graphic Statics & Passive Sky-Cooling Vaults · REV 1.5',
              'kernels': 'Maxwell–Rankine Dual Polyhedra (Γ ↔ Γ^*) · Airy Concavity det(H_Φ) > 0 · '
                         '8–13 μm Sky-Cooling',
              'benchmarks': 'Model values: det(H_Φ) = +1.84 (illustrative) · q_net = 98.4 W/m² at air temperature · ΔT_eq = −7.08 °C for an assumed 13.9 W/(m²·K)',
              'bridge': 'Continues A.01/A.02 ↔ Toolbox X.03 STEP AP242 · Concave Stress Vaults & '
                        'P(VdF-HFP) Sky-Cooling'},
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
 'steps': ['Stage 1 (Airy Stress Function & Negative-Definite Hessian): In-plane membrane stresses are written through an Airy stress function Φ(x, y) as σ_xx = Φ_yy, σ_yy = Φ_xx, σ_xy = −Φ_xy. In his 1870 paper on reciprocal figures Maxwell read a polyhedron lifted over a frame as a discrete stress function of this kind.',
           'Stage 2 (Rankine–Minkowski Reciprocal Polyhedra Γ ↔ Γ^*): In 3D polyhedral graphic statics (Akbarzadeh, Van Mele & Block 2015, DOI 10.1016/j.cad.2015.01.006), each member of the form diagram is perpendicular to a face of a closed cell in the force diagram, and the face area is proportional to the member force; a closed cell means the forces at that node balance.',
           'Stage 3 (Concavity and Compression): If the Hessian of Φ is negative-definite (Φ_xx < 0, Φ_yy < 0, det(H_Φ) = Φ_xx Φ_yy − Φ_xy² > 0), the in-plane stress field of the model is compressive everywhere. That is a property of the model under the load case considered, not a structural check of a real shell; the 52 mm thickness is an illustrative value.',
           'Stage 4 (8–13 μm Radiative Sky-Cooling Extrados & Toolbox X.03 CAD Bridge): With a porous P(VdF-HFP)-type coating (Mandal et al. 2018, DOI 10.1126/science.aat9513) assumed at R_solar = 0.96 under 890 W/m² of sun, the extrados absorbs 35.6 W/m². The model assigns a net radiative exchange with the sky of 134.0 W/m² at air temperature (a fixed illustrative value), so q_net = 134.0 − 35.6 = 98.4 W/m²; divided by an assumed combined heat-exchange coefficient of 13.9 W/(m²·K), that gives ΔT_eq ≈ −7.08 °C. Toolbox X.03 provides the STEP AP242 voussoir geometry.'],
 'readouts': [{'label': 'Airy Hessian Determinant det(H_Φ)',
               'value': '+1.84 > 0 (Illustrative, Compressive in Model)'},
              {'label': 'Dual Polyhedron Closure Error', 'value': 'Closed by Construction (Model, No Solver Run)'},
              {'label': '8–13 μm Sky-Cooling Net Flux', 'value': '98.4 W/m² · ΔT_eq = −7.08 °C (Model)'},
              {'label': 'A.11 ↔ X.03 Model Status', 'value': 'COMPRESSION-ONLY IN MODEL · NOT A STRUCTURAL CHECK'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 04 20 00 / 07 56 00 / COMPAS-3GS / TOOLBOX X.03',
                'title': 'Unreinforced Funicular Ribbed Vaults with 8–13 μm Passive Sky-Cooling '
                         'Extrados & STEP AP242 Export',
                'body': 'Design proposal: compression-only tile and dry-cut stone funicular vaults shaped with reciprocal polyhedra (tools such as compas-dev/compas, geometry from Toolbox X.03), with a porous P(VdF-HFP)-type sky-cooling coating on the extrados at assumed R_solar = 0.96 and ε_8-13μm = 0.95. Not a tested or engineered assembly.',
                'meta': 'References: Akbarzadeh et al. 2015, DOI 10.1016/j.cad.2015.01.006 · Raman et al. 2014, DOI 10.1038/nature13883 · Mandal et al. 2018, DOI 10.1126/science.aat9513 · Model values, not measurements'},
 'sidenote_1': {'kicker': 'SIDENOTE A.11-A · CROSS-FIELD ANALOGY · SOAP FOAM & GUASTAVINO TILE VAULTS',
                'body': 'Rafael Guastavino and his son, who emigrated from Spain to the United States in 1881, built hundreds of thin timbrel tile vaults there (López et al. 2023, DOI 10.3390/buildings13082052). 3D polyhedral graphic statics came more than a century later, so it played no part in their designs. The soap-foam picture is this folio\'s analogy: in a polyhedral force diagram each cell closes, much as each bubble in a foam is closed, and each face area is proportional to the force in the matching member.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.11-B · DAYTIME SKY-COOLING VAULTS & TOOLBOX X.03 CAD',
                'body': 'Mandal et al. (2018, DOI 10.1126/science.aat9513) reported porous P(VdF-HFP) coatings that reached about 6 °C below ambient under 890 W/m² of sun and about 96 W/m² of cooling power under 750 W/m². In this folio\'s model the same kind of coating on a vault extrados gives 98.4 W/m² at air temperature, a model value. The companion 7-voussoir STEP AP242 and GLB kit is in Toolbox X.03 (/toolchain/x03/).'},
 'skill': {'filename': '3d-polyhedral-graphic-statics-SKILL.md',
           'name': '3d-polyhedral-graphic-statics',
           'description': 'AI-agnostic architectural and structural skill for 3D Polyhedral '
                          'Graphic Statics (Maxwell-Rankine dual polyhedra), strictly concave Airy '
                          'stress surfaces, 8-13 um daytime radiative sky-cooling vault envelopes, '
                          'and Toolbox X.03 STEP AP242 voussoir coupling.',
           'rules': ['Check 3D nodal equilibrium by requiring every polyhedral cell c_v^* in the '
                     'reciprocal force diagram Gamma^* to close within a numerical tolerance (for example ||sum F_i|| < 1e-12 kN).',
                     'Check that the model stress field is compressive by testing the Airy stress Hessian: Phi_xx < 0, Phi_yy < 0, and det(H_Phi) = Phi_xx*Phi_yy - Phi_xy^2 > 0. This is a model check for one load case, not a structural assessment of a real vault.',
                     "Evaluate daytime radiative sky-cooling net flux q_net = q_rad(T_s) - q_atm(T_a) - q_solar*(1 - R_solar) - h_c*(T_a - T_s); treat q_net >= 80 W/m^2 at T_a = 303.15 K and Delta T_eq <= -4.5 C as this folio's own design targets, and report results as model values, never as measurements."]},
 'revisions': [{'edition': 'REV 1.5',
                'date': '2026-11-14',
                'summary': "REV 1.5 (Redated 2026-11-14): Grounding revision. The opening scene of Maxwell at Glenlair and the claim that Rafael Guastavino built Grand Central's vaults in 1913 using Maxwell's principle were not sourced and are replaced by a plain account. The 70-72% concrete and carbon figures are replaced by a published one-third-of-the-material figure for an unreinforced funicular floor (Küpfer et al. 2025); 'PASS', 'certified' and 'guaranteed' wording for things nobody measured is withdrawn, and the sky-cooling numbers now state the assumptions they follow from. The 80 W/m² and −4.5 °C thresholds are labelled as this folio's own design targets.",
                'opus': 'Review: references checked by DOI in Crossref and Scite; central claims checked against the Scite index; arithmetic recomputed from the stated balance.'},
               {'edition': 'REV 1.4',
                'date': '2026-11-10',
                'summary': 'REV 1.4 (Redated 2026-11-10): Coupled 3D polyhedral graphic statics and '
                           'negative-definite Airy stress surfaces (DOI 10.1016/j.cad.2015.01.006) '
                           'with 8–13 μm atmospheric-window daytime radiative sky-cooling extrados '
                           'coatings (Raman et al. 2014, DOI 10.1038/nature13883; Mandal et al. 2018 '
                           'porous P(VdF-HFP), DOI 10.1126/science.aat9513), cross-linked directly to '
                           'Toolbox X.03 STEP AP242/3MF/DXF/GLB voussoir assemblies with reference '
                           'values stated in the essay.',
                'opus': "Council review (Gemini 4 Argon + Qwen 3.8 27B + Gemma 4 31B). Its 'verified' wording is withdrawn in REV 1.5: no Airy surface or force diagram was solved, and the cooling figures are model values that depend on stated assumptions."},
               {'edition': 'REV 1.0',
                'date': '2026-11-07',
                'summary': 'REV 1.0 (Published 2026-11-07): Volume VI Architecture monograph '
                           'continuing Folios A.01 & A.02 via Maxwell 3D polyhedral graphic '
                           'statics, Heyman limit analysis (DOI 10.1017/cbo9781107050310), and '
                           'compas-dev/compas.',
                'opus': "Council review (Gemini 4 Argon + Qwen 3.8 27B + Gemma 4 31B) of the area-force relation and Airy concavity. Its 'verified' wording is withdrawn in REV 1.5: the relation is proportionality, as published, and nothing was computed."}],
 'volume': 6,
 'volume_code': 'VOL. 06',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/j.cad.2015.01.006',
           'fetched_on': '2026-11-08',
           'citing_publications': 93,
           'supporting': 0,
           'mentioning': 55,
           'contrasting': 0,
           'retracted': False,
           'summary': "Scite index entry for Akbarzadeh, Van Mele & Block, On the equilibrium of funicular polyhedral frames and convex polyhedral force diagrams (DOI 10.1016/j.cad.2015.01.006), checked 2026-11-08: 93 citing publications (0 supporting, 55 mentioning, 0 contrasting) and no retraction notice. The counts describe that paper, not this folio's model."}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
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
           'summary': "Scite index entry for Akbarzadeh, Van Mele & Block, On the equilibrium of funicular polyhedral frames and convex polyhedral force diagrams (DOI 10.1016/j.cad.2015.01.006), checked 2026-11-08: 93 citing publications (0 supporting, 55 mentioning, 0 contrasting) and no retraction notice. The counts describe that paper, not this folio's model."},
 'act1_title': 'Act I — How Thin Masonry Vaults Stand in Compression',
 'act1_dropcap': "In 1864 James Clerk Maxwell published a short paper on reciprocal figures and diagrams of forces. He observed that when the drawing of a plane frame is the projection of a polyhedron with flat faces, the frame can carry a balanced set of internal forces, and in a longer paper of 1870 he read that polyhedron as a stress function. Masonry vaults depend on the same idea of balance: stone and tile resist squeezing far better than pulling, so a vault stands when its forces can flow through it in compression. In the United States, Rafael Guastavino and his son, who emigrated from Spain in 1881, built hundreds of thin timbrel tile vaults (López et al. 2023, DOI 10.3390/buildings13082052). This folio follows Maxwell's idea into three dimensions, where force diagrams become polyhedra.",
 'act1_plain_bridge': 'In plain words, think about how stone and concrete work. If you try to pull '
                      'a stone apart like a piece of taffy, it cracks and fails almost '
                      'immediately. But if you squeeze a stone tightly between your hands, it can '
                      'support immense weight without breaking. Standard modern floors are built '
                      'as flat concrete slabs. Because flat slabs bend and sag in the middle under '
                      'gravity, the bottom half gets stretched, forcing builders to bury thousands '
                      'of pounds of expensive, rust-prone steel rebar inside the concrete. Master '
                      'vault builders avoided this problem completely by arching the floor upward '
                      'into a shallow dome. When gravity presses down on an arch, the stone blocks '
                      'wedge tightly against one another, funneling all the weight downward into '
                      'pure compression. By using modern computers to shape these curved vaults in '
                      'three dimensions, architects can shape floors of tile, brick or plain concrete that need little or no steel in the vault itself. One published unreinforced funicular floor, the Hi-Lo floor, uses about one-third of the material of a conventional flat concrete slab (Küpfer et al. 2025, DOI 10.1088/1755-1315/1554/1/012083). The thrust still has to be taken by ties or supports.',
 'act1_body': "In Folio A.01 we traced Robert Hooke's 2D hanging chain and Jacques Heyman's "
              'plastic limit theorems (The Stone Skeleton, 1995, DOI 10.1017/cbo9781107050310). '
              'But real architectural spaces are three-dimensional, curved, and pierced by '
              "stairwells where simple two-dimensional slices fail. Maxwell's reciprocal figures (1864, 1870) linked plane frames in equilibrium to polyhedra and stress functions; C. R. Calladine (1978, DOI 10.1016/0020-7683(78)90052-5) revisited Maxwell's rule for counting the stiffness of frames; and Akbarzadeh, Van Mele, and Block (2015, DOI 10.1016/j.cad.2015.01.006) extended graphic statics to three dimensions with polyhedral force diagrams. Philippe Block's research group at ETH Zurich also develops the open-source COMPAS framework (https://github.com/compas-dev/compas), and built the dry-assembled cut-stone Armadillo Vault for the 2016 Venice Architecture Biennale. In this folio we pair such compression shells with a passive daytime radiative sky-cooling coating on the extrados (Raman et al. 2014, DOI 10.1038/nature13883; Mandal et al. 2018, porous P(VdF-HFP) polymer, DOI 10.1126/science.aat9513) and link them to neutral STEP AP242, 3MF, DXF, and GLB voussoir geometry in Toolbox X.03 (/toolchain/x03/). The pairing is a design study.",
 'act1_stakes': 'For centuries, master masons relied on lodge rules of thumb and geometric '
                'templates to size stone arches and buttresses. While these empirical rules '
                'produced magnificent structures, they required immense intuition and could not '
                'safely predict how irregular, freeform, or asymmetric vaults would behave under '
                'complex live loads. When twentieth-century builders transitioned to flat '
                'reinforced-concrete slabs, they substituted computational certainty for material '
                'efficiency: pouring massive, heavy flat slabs packed with tensile steel was '
                'simpler to calculate than complex masonry curves. Floor slabs use a large share of the concrete in a multi-storey building, and steel reinforcement can corrode where moisture and carbonation reach it. Unreinforced funicular floors aim to use less material and avoid reinforcement in the vault; one published system uses about one-third of the material of a flat slab (Küpfer et al. 2025, DOI 10.1088/1755-1315/1554/1/012083). How durable such floors are over a building\'s life is a question this folio does not answer.',
 'pullquote': '"In 3D graphic statics, a closed force polyhedron shows that the forces at a node balance, and a concave '
              'Airy surface shows that the model is in compression. These are first checks of form; a real vault still needs checks for '
              'stability, asymmetric loads and supports."',
 'chronology': [('1864–1870',
                 "James Clerk Maxwell's papers on reciprocal figures link plane frames in equilibrium to polyhedra and, in 1870, to stress functions."),
                ('1881 onward',
                 'Rafael Guastavino and his son, emigrating from Spain, build hundreds of thin timbrel tile vaults in the United States (López et al. 2023, DOI 10.3390/buildings13082052).'),
                ('1978–2015',
                 'Calladine (DOI 10.1016/0020-7683(78)90052-5), Heyman (DOI '
                 '10.1017/cbo9781107050310), and Akbarzadeh, Van Mele & Block (DOI '
                 '10.1016/j.cad.2015.01.006) contribute to masonry analysis, frame rigidity and 3D polyhedral graphic statics.'),
                ('2014–2018',
                 'Raman et al. (DOI 10.1038/nature13883) and Mandal et al. (DOI '
                 '10.1126/science.aat9513) report daytime radiative sky cooling below air temperature; this folio proposes pairing such coatings with vaults and Toolbox X.03 geometry.')],
 'act2_title': 'Act II — Cross-Field Intuition: Soap-Foam Dual Polyhedra & Concave Stress Bowls',
 'act2_analogy': 'Think of a cluster of soap bubbles resting in a wire frame: every paper-thin '
                 'soap film pulls in perfect physical balance because each bubble cell is '
                 'completely closed on all sides. Now imagine taking that cluster of soap bubbles '
                 'and flipping it upside down like an umbrella: every gentle tension pull in the '
                 'soap film converts into pure, rock-solid compression between stone blocks. If '
                 'the dual bubble cells close, the stone ceiling simply cannot fall down.',
 'act2_plain_primer': 'To design a compression-only stone vault using this soap-bubble duality, '
                      'you work with two primary structural knobs. The first knob controls the '
                      'scale of the reciprocal force crystal, which acts like an invisible '
                      'mathematical shadow of the building. As you enlarge this dual crystal, the '
                      'internal forces pushing through the stone ribs increase, showing you how '
                      "much horizontal thrust the building's perimeter walls and foundations must "
                      'push back against to keep the vault stable. The second knob adjusts the '
                      'crown rise of the vault relative to the distance it spans across the room. '
                      'If you dial this knob down toward a very shallow, almost flat arch, the '
                      'vault exerts enormous outward thrust against the support walls, requiring '
                      'heavy abutments. As you increase the crown rise and arch the vault higher, '
                      'the downward forces flow more steeply into the ground, reducing horizontal '
                      'thrust and allowing the floor to be built remarkably thin and light without '
                      'any steel reinforcement.',
 'distill_diagram': {'analogy_title': 'The Inverted Soap-Bubble Foam',
                     'analogy_sub': 'Closed polyhedral cells show three-dimensional balance of forces in the model',
                     'force_a_title': 'Dual Force Scale Knob (ζ_dual)',
                     'force_a_sub': 'Scales horizontal abutment thrust and reciprocal polyhedron '
                                    'volume',
                     'force_b_title': 'Vault Rise-to-Span Ratio (f/L)',
                     'force_b_sub': 'Directs internal thrust vectors into pure compression arches',
                     'threshold_title': 'Airy Stress Concavity det(H_Φ) > 0',
                     'threshold_pass': 'Compression throughout the model shell for the load case considered',
                     'threshold_fail': 'Convexity or unclosed dual cell causes tensile hinge '
                                       'cracking'},
 'act2_intuition': 'Imagine two linked three-dimensional geometric networks displayed side by side '
                   'in the open-source compas-dev/compas framework: the Form Diagram Gamma '
                   '(representing the physical geometry of the unreinforced stone or tile vault '
                   'ribs) and the Reciprocal Force Diagram Gamma_star (a cellular cluster of '
                   'convex polyhedral cells; Akbarzadeh et al. 2015, DOI 10.1016/j.cad.2015.01.006). '
                   'Every physical strut e_i in the vault is strictly perpendicular to a '
                   'corresponding polygonal face f_i_star in the dual force diagram, and the '
                   'area of that face A_i_star is proportional to the axial force N_i in the strut. '
                   'The outward area vectors of any closed polyhedron sum to zero, which is why a '
                   'closed cell expresses the balance of forces at a node. In-plane membrane stresses satisfy '
                   'sigma_xx = Phi_yy, sigma_yy = Phi_xx, and sigma_xy = -Phi_xy on the Airy stress '
                   'surface Phi(x, y): negative-definite curvature (Phi_xx < 0, Phi_yy < 0, '
                   'det(H_Phi) = Phi_xx*Phi_yy - Phi_xy^2 > 0) means the in-plane stresses of the model are compressive everywhere. The value det(H_Phi) = +1.84 shown on this page is illustrative; no Airy surface was solved for a real vault.',
 'act2_deepening': "This folio pairs compression-only geometry with passive radiative cooling and open CAD exchange. Structurally, a higher crown rise f/L steepens the thrust and lowers the horizontal force on the supports; the default f/L = 0.16 is an illustrative value, and no safety factor was computed. Thermally, a hierarchically porous P(VdF-HFP) coating (Mandal et al. 2018, DOI 10.1126/science.aat9513; building on Raman et al. 2014, DOI 10.1038/nature13883) is assumed at solar reflectance R_solar = 0.96 and 8–13 micrometer emissivity 0.95. At ambient T_a = 303.15 K (30.0 C) under 890 W/m^2 of sun, the extrados absorbs (1 - 0.96) * 890 = 35.6 W/m^2. The model assigns a net radiative exchange with the sky of 134.0 W/m^2 at air temperature, a fixed illustrative value, so q_net = 134.0 - 35.6 = 98.4 W/m^2. Dividing by an assumed combined heat-exchange coefficient of 13.9 W/(m^2 K) gives a surface about 7.08 C below the air; with stronger wind the drop would be smaller. For comparison, Mandal et al. measured about 6 C below ambient under 890 W/m^2. The 80 W/m^2 and -4.5 C thresholds are this folio's own design targets. How much this would cool the rooms under a massive vault is not modeled.",
 'walkthrough': ['Experiment 1 (Reciprocal Polyhedron Scale ζ_dual): Drag Dual Polyhedron Scale '
                 'ζ_dual from 0.50 to 2.00. Watch the reciprocal force crystal Γ^* expand or '
                 'contract as horizontal abutment thrust scales proportionally.',
                 'Experiment 2 (Vault Rise-to-Span Ratio f/L): Vary Crown Rise f/L from 0.08 to '
                 '0.30. Observe how the illustrative Airy Hessian determinant det(H_Φ) and the horizontal thrust respond in the model.',
                 'Experiment 3 (Counterfactual Knockout ⚡): Click [⚡ Counterfactual] to puncture a '
                 'face in the dual force polyhedron Γ^* and watch the model flag that the node no longer balances, a sign of where tension or hinging could start.'],
 'act4_title': "Act IV — Imagining Humanity's Future: Zero-Rebar Affordable Housing Built from "
               'Local Earth and Stone',
 'act4_human_ai': 'By pairing open-source compas-dev/compas (https://github.com/compas-dev/compas) '
                  'and Toolbox X.03 (/toolchain/x03/) neutral STEP AP242, 3MF, DXF, and GLB '
                  'generators with porous P(VdF-HFP) sky-cooling roof coatings (DOI '
                  '10.1126/science.aat9513), small studios in hot climates could explore vaulted housing of local compressed earth, tile, or cut stone with less steel and a passively cooled roof. This is a proposal; how much steel or air conditioning it would save is not estimated here.',
 'act4_deepening': 'Architects could couple 3D graphic statics directly to neutral CAD exchange and passive building physics. Using compas-dev/compas with Toolbox X.03 (/toolchain/x03/), a small studio could check that reciprocal force polyhedra close, test Airy stress concavity, and export STEP AP242, 3MF, DXF, and GLB voussoir geometry in Python without proprietary CAD seats; COMPAS is named here as a tool a reader could use, and this folio ran no COMPAS model. Pairing masonry thermal mass with 8–13 micrometer radiative sky-cooling coatings (Raman et al. 2014, DOI 10.1038/nature13883; Mandal et al. 2018, DOI 10.1126/science.aat9513) gives about 98 W/m^2 of cooling at air temperature in this folio\'s model. Open questions include robotic falsework-free placement, seismic '
                   'dry-joint rocking dissipation, and weather-durable mineral-polymer sky-cooling '
                   'glazes for century-scale zero-rebar housing.',
 'cf_bridge': 'Standalone Architectural Form-Finding & Passive Sky-Cooling Vault Flagship (A.01 + '
              'A.02 -> A.11 <-> Toolbox X.03): Engineered for architects and structural designers '
              'creating compression-only shells and passive radiative envelopes.',
 'sources': ['Akbarzadeh, M., Van Mele, T., & Block, P. (2015). On the equilibrium of funicular '
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
             'López López, D., et al. (2023). Multi-Level Numerical Modelling and Analysis of Tile Vaults. Buildings, 13(8), 2052. DOI: 10.3390/buildings13082052.',
             'Küpfer, C., Bertola, N., Jayasinghe, A., Orr, J., & Fivet, C. (2025). Concrete floors: multi-criteria analysis of conventional and novel solutions. IOP Conference Series: Earth and Environmental Science, 1554(1), 012083. DOI: 10.1088/1755-1315/1554/1/012083.',
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
        'fill="currentColor">Form Diagram Γ: Ribbed Funicular Floor Vault (Illustrative t = 52 mm)</text>\n'
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
        '            <text x="54" y="178" font-size="9.5" fill="var(--tp-verdigris)">Airy Stress '
        'Concavity det(H_Φ) = +1.84 &gt; 0 (Illustrative Model Value)</text>\n'
        '            <line x1="368" y1="24" x2="368" y2="192" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="386" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">Reciprocal Force Polyhedron Γ^* (N_i = A_i^*)</text>\n'
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
        'Minkowski Dual Cells ⇒ Forces Balance at Each Node</text>\n'
        '            <text x="44" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Design Study · Model Values · Not a Structural Check</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a dry-stacked limestone and Guastavino tile '
        'funicular vaulted hall with glowing 3D reciprocal Maxwell force polyhedra suspended in '
        'midair would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.11-V (Imagining What It Would Look Like) · Artistic '
            'architectural visualization (continuing Folios A.01 & A.02) imagining an unreinforced '
            'ribbed stone-and-tile vault designed via Maxwell 3D polyhedral graphic statics in '
            'COMPAS.'}

DISPATCH = {'kicker': 'FRONTIER COMPUTATIONAL ARCHITECTURE DISPATCH · A.11 ↔ TOOLBOX X.03 · REV 1.4',
 'headline': 'A Design Study: 3D Polyhedral Graphic Statics & 8–13 μm Sky-Cooling Coatings on '
             'Compression-Only Vaults',
 'body': 'This folio pairs compression-only vault geometry from 3D graphic statics (Akbarzadeh et al., DOI 10.1016/j.cad.2015.01.006) and Toolbox X.03 STEP AP242 voussoir kits with a porous P(VdF-HFP) sky-cooling coating on the extrados (DOI 10.1038/nature13883, DOI 10.1126/science.aat9513). In its model the coating gives 98.4 W/m^2 of cooling at air temperature and a surface about 7.08 C below the air for an assumed heat-exchange coefficient. Model values, not measurements; one published unreinforced funicular floor uses about a third of the material of a flat slab (Küpfer et al. 2025).'}

META_3D = ('Maxwell–Airy 3D Concave Stress & Thrust Network Surface',
 'X: Span Coordinate x/L · Z: Transverse Coordinate y/L · Y: Airy Stress Potential Φ(x, y)')

ES_TRANSLATION = {'title_es': 'Estática Gráfica Poliédrica 3D y Superficies de Esfuerzo de Airy: Poliedros '
             'Recíprocos de Maxwell, Bóvedas de Guastavino y Pisos sin Acero',
 'subtitle_es': 'Continuando los Folios A.01 y A.02 hacia la Caja de Herramientas X.03: bóvedas '
                'poliédricas a compresión pura con recubrimientos de enfriamiento radiativo diurno '
                '(8–13 μm) y exportación STEP AP242.',
 'why_es': 'Igual que una espuma de burbujas de jabón se equilibra al cerrar sus celdas, una bóveda a compresión se equilibra cuando cierran las celdas de su diagrama de fuerzas; en el modelo de este folio, un recubrimiento de polímero poroso P(VdF-HFP) sobre la bóveda da 98.4 W/m² de enfriamiento a temperatura del aire bajo pleno sol.',
 'bridge_es': 'Estudio de diseño: la dualidad de poliedros recíprocos (con herramientas como COMPAS y la geometría de X.03) se combina con enfriamiento radiativo pasivo; en el modelo la superficie queda unos 7.08 °C por debajo del aire, con un coeficiente de intercambio de calor supuesto.',
 'plain_es': 'En palabras sencillas, imaginen cómo trabajan los materiales de construcción '
             'comunes. Si intentamos jalar o estirar una piedra o un ladrillo de barro, se agrieta '
             'y se rompe con facilidad. Pero si lo apretamos con fuerza, puede soportar el peso de '
             'un edificio entero sin sufrir ningún daño. Los pisos modernos de oficinas se '
             'construyen como losas planas de concreto; como se doblan hacia abajo en el centro '
             'por la gravedad, la parte inferior se estira, obligando a rellenarlas con toneladas '
             'de varillas de acero. Los constructores de bóvedas, como Rafael Guastavino y su hijo '
             'en Estados Unidos, curvaban los techos hacia arriba en forma de bóveda. Al recibir peso, los ladrillos se empujan unos contra '
             'otros a compresión hacia los apoyos. Con computadoras modernas para '
             'calcular estas curvas en tres dimensiones se pueden diseñar pisos de ladrillo, piedra o concreto '
             'con poco o nada de acero en la bóveda; un piso funicular sin refuerzo ya publicado usa cerca de '
             'un tercio del material de una losa plana (Küpfer et al. 2025). El empuje lo siguen tomando tirantes o apoyos.',
 'deep_es': 'Este folio es un estudio de diseño. Combina la estática gráfica poliédrica tridimensional (Akbarzadeh et '
            'al. 2015, DOI 10.1016/j.cad.2015.01.006) con recubrimientos pasivos de '
            'enfriamiento radiativo diurno en la ventana atmosférica de 8 a 13 micrómetros (Raman '
            'et al. 2014, DOI 10.1038/nature13883; Mandal et al. 2018, DOI 10.1126/science.aat9513) '
            'y con el kit de dovelas STEP AP242 de la Herramienta X.03 (/es-mx/toolchain/x03/). '
            'Cada celda cerrada del diagrama de fuerzas indica que las fuerzas de un nodo se equilibran, y un '
            'hessiano definido negativo de la superficie de Airy (Φ_xx < 0, Φ_yy < 0, det(H_Φ) > 0) indica que '
            'el modelo trabaja a compresión; el valor det(H_Φ) = +1.84 es ilustrativo y no sustituye una revisión estructural. '
            'En el extradós se supone un polímero poroso con reflectancia solar de 0.96 bajo 890 W/m² de sol: absorbe 35.6 W/m². '
            'El modelo le asigna un intercambio radiativo neto con el cielo de 134.0 W/m², un valor ilustrativo fijo, de modo que '
            'q_net = 98.4 W/m² a temperatura del aire (T_a = 303.15 K); con un coeficiente combinado de intercambio de calor supuesto '
            'de 13.9 W/(m²·K), la superficie queda unos 7.08 °C por debajo del aire. Las cifras de 80 W/m² y −4.5 °C son metas de diseño '
            'del propio folio. Como referencia, Mandal et al. midieron cerca de 6 °C bajo el ambiente. Son valores de modelo, no mediciones.'}
