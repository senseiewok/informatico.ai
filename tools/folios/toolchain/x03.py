# -*- coding: utf-8 -*-
"""Tech & Tools · The Toolbox — Folio X.03: The Small Architecture Studio's Vault, Timber & Reciprocal Frame Kit: Equilibrium to Open CAD."""

FOLIO = {'slug': 'x03',
 'folio_id': 'X.03',
 'tool_id': 'TOOL-ARCH-1',
 'cat': 'architecture',
 'plate_slug': 'x03',
 'pillar_label_en': "Small Architect's Studio Toolbox · Structural Form-Finding & Open BIM",
 'pillar_label_es': 'Caja de Herramientas para Pequeños Despachos de Arquitectura · Búsqueda de '
                    'Forma',
 'badge_en': "TOOLBOX X.03 · BOUTIQUE ARCHITECT'S ZERO-COST VAULT & TIMBER KIT (STEP · 3MF · DXF · "
             'GLB)',
 'badge_es': 'HERRAMIENTA X.03 · KIT SIN COSTO DE BÓVEDAS Y MADERA PARA ARQUITECTOS (STEP · 3MF · '
             'DXF · GLB)',
 'title': "The Small Architecture Studio's Vault, Timber & Reciprocal Frame Kit: Equilibrium to "
          'Open CAD',
 'title_es': 'El Kit de Bóvedas, Madera y Marcos Recíprocos para Pequeños Estudios de Arquitectura',
 'subtitle': "How 1-to-10-person architecture studios can run Jacques Heyman's middle-third kern "
             'analysis and Maxwell–Rankine polyhedral form-finding in Python—emitting '
             'ready-to-inspect STEP, 3MF, DXF, and GLB voussoir assemblies at zero software cost.',
 'subtitle_es': 'Cómo los pequeños despachos de arquitectura de 1 a 10 personas pueden ejecutar el '
                'análisis del núcleo central de Heyman y la estática gráfica de Maxwell–Rankine en '
                'Python—generando ensamblajes de dovelas en STEP, 3MF, DXF y GLB sin costo de '
                'software.',
 'why_en': 'In architecture, advanced structural form-finding and environmental simulation often '
           'get locked inside multinational engineering consultancies with six-figure software '
           'budgets. We built Folio X.03 specifically to empower small, independent architecture '
           'studios and solo practitioners: using MIT-licensed Python tools (COMPAS, Bonsai BIM / '
           'IfcOpenShell, Blender, FreeCAD), a small studio can generate compression-only stone, '
           'brick, or cross-laminated timber (CLT) voussoir arches, verify their thrust-line '
           'equilibrium, and export 3D solids (.step, .3mf, .glb) plus 2D cutting templates '
           '(.dxf).',
 'why_es': 'En la arquitectura actual, la búsqueda de forma estructural suele quedar reservada '
           'para grandes corporativos con presupuestos de software inalcanzables. Diseñamos el '
           'Folio X.03 específicamente para empoderar a pequeños despachos de arquitectura y '
           'profesionales independientes: usando herramientas abiertas en Python con licencia MIT '
           '(COMPAS, Bonsai BIM / IfcOpenShell, Blender, FreeCAD), cualquier estudio puede generar '
           'arcos y bóvedas de piedra, ladrillo o madera (CLT) a compresión pura, verificar su '
           'línea de empuje y exportar sólidos 3D (.step, .3mf, .glb) y plantillas de corte 2D '
           '(.dxf).',
 'governing_law': 'H = q L² / (8 f) = 27.0 kN · |e(x)| ≤ t / 6 = 66.7 mm · χ = 2 N_v = 14 · '
                  'q_net(8–13 μm) ≥ 80 W/m²',
 'pass_pill_en': 'PASS · 7 VOUSSOIRS · χ = 14 · H = 27.0 kN · q_net ≥ 80 W/m² · STEP+3MF+DXF+GLB',
 'pass_pill_es': 'APROBADO · 7 DOVELAS · χ = 14 · H = 27.0 kN · q_net ≥ 80 W/m² · STEP+3MF+DXF+GLB',
 'generator_script': 'skills/toolchain/x03/make_x03.py',
 'verifier_script': 'skills/toolchain/x03/verify_x03_toolchain_x03_small_architect_vault_kit.py',
 'skill_dir': 'skills/toolchain/x03',
 'skill_name': 'toolchain-x03-small-architect-vault-kit',
 'formats': ('glb', 'step', '3mf', 'dxf'),
 'primary_doi': '10.1016/0020-7683(66)90018-7',
 'scite_summary': 'Heyman (1966) masonry limit analysis, Akbarzadeh et al. (2015) polyhedral '
                  'graphic statics, and Raman (2014) / Mandal (2018) 8–13 μm radiative sky-cooling '
                  'verified offline.',
 'date_published': '2026-11-08',
 'date_redated': '2026-11-10',
 'current_edition': 'REV 1.4',
 'reading_time': '24 MIN READ',
 'small_studio_kit_en': 'Boutique Architecture Studio Stack (COMPAS MIT + Blender 4.2 / Bonsai + '
                        'FreeCAD 1.0 + QCAD Community Edition / LibreCAD): Run make_x03.py to '
                        'generate a 7-voussoir funicular arch coupled with an A.11 passive '
                        'radiative sky-cooling extrados envelope across 4 open '
                        'formats—x03_artifact.glb for client WebGL walkthroughs, x03_artifact.step '
                        'for structural engineer coordination, x03_artifact.3mf for 1:20 desktop '
                        'study models, and x03_artifact.dxf for 2D stone/CLT CNC cutting templates.',
 'small_studio_kit_es': 'Stack para Pequeños Estudios de Arquitectura (COMPAS MIT + Blender 4.2 / '
                        'Bonsai + FreeCAD 1.0 + QCAD Community Edition / LibreCAD): Ejecuta '
                        'make_x03.py para generar un arco funicular de 7 dovelas acoplado al '
                        'extradós de enfriamiento radiativo diurno A.11 en 4 formatos '
                        'abiertos: x03_artifact.glb para presentaciones WebGL con clientes, '
                        'x03_artifact.step para coordinación estructural, x03_artifact.3mf para '
                        'maquetas físicas 1:20 y x03_artifact.dxf para plantillas de corte 2D en '
                        'CNC.',
 'companion_folios': [('architecture',
                       'a11',
                       'Folio A.11',
                       '3D Polyhedral Graphic Statics & Sky-Cooling Vaults'),
                      ('architecture',
                       'a01',
                       'Folio A.01',
                       'Heyman Masonry Vaults & Glaser Thermal Nodes'),
                      ('architecture',
                       'a02',
                       'Folio A.02',
                       'Reciprocal Timber Nexorade Gridshells'),
                      ('engineering', 'e02', 'Folio E.02', 'Herschel–Bulkley Concrete Rheology')],
 'external_links': [('compas-dev/compas (MIT Computational Architecture Framework)',
                     'https://github.com/compas-dev/compas'),
                    ('Bonsai BIM / IfcOpenShell (Native Open BIM)', 'https://bonsaibim.org/'),
                    ('FreeCAD 1.0 BIM & Arch Workbench', 'https://www.freecad.org/')],
 'act1_dropcap': 'In sixteen seventy-five, Robert Hooke concealed his greatest discovery inside a '
                 'Latin anagram: as hangs the flexible chain, so, but inverted, stands the rigid '
                 'arch. For nearly three centuries, master masons carved cathedrals by intuition '
                 'and geometric proportion, trusting that pure compression could conquer gravity '
                 'without steel. Yet by the mid-twentieth century, modern structural engineering '
                 'had largely abandoned unreinforced stone, treating masonry with elastic beam '
                 'equations that falsely predicted catastrophic failure whenever tensile stress '
                 'appeared. Standing before the soaring stone vaults of King’s College Chapel in '
                 'Cambridge in nineteen sixty-six, structural historian Jacques Heyman recognized '
                 'the profound error of this modern dogma. He realized that historic masonry does '
                 'not fail by crushing or material yielding, but by geometric instability when the '
                 'line of thrust wanders outside the masonry blocks. Today, Philippe Block at ETH '
                 'Zurich transforms that insight into digital computation.',
 'act1_body': "Heyman formalized his breakthrough in his seminal nineteen sixty-six treatise 'The "
              "Stone Skeleton' (DOI: 10.1016/0020-7683(66)90018-7), establishing plastic limit "
              'analysis for masonry. He formulated three core axioms: stone possesses zero tensile '
              'capacity, stone has infinite compressive strength compared to ambient loads, and '
              'sliding between voussoirs cannot occur. Under these assumptions, the Safe Theorem '
              'guarantees that if any admissible thrust line can be drawn wholly within the arch '
              'boundaries in equilibrium with applied loads, the structure cannot collapse. James '
              'Clerk Maxwell’s eighteen sixty-four reciprocal force polygons and William Rankine’s '
              'graphic statics provided the geometric machinery to trace these equilibrium lines '
              'by hand. Decades later, Philippe Block and Tom Van Mele digitized this heritage '
              'through thrust network analysis, polyhedral graphic statics (Akbarzadeh, Van Mele, '
              '& Block, 2015, DOI: 10.1016/j.cad.2015.01.006), and the open-source COMPAS '
              'framework. In REV 1.4, we couple this compression-only vault geometry directly with '
              'Folio A.11’s passive daytime radiative sky-cooling extrados envelope: coating the '
              'outer vault shell with hierarchically porous P(VdF-HFP) polymer (Raman et al., 2014, '
              'DOI: 10.1038/nature13883; Mandal et al., 2018, DOI: 10.1126/science.aat9513) reflects '
              '96% of incident sunlight while radiating heat through the 8–13 μm atmospheric window.',
 'pullquote': 'When a two-person architecture studio can generate verified STEP, 3MF, DXF, and GLB '
              'vault geometry from a 100-line Python script, computational tectonics stops being a '
              'corporate monopoly and becomes a public craft.',
 'chronology': [('1675',
                 "Robert Hooke formulates the inverted hanging-chain law: 'As hangs the flexible "
                 "line, so but inverted will stand the rigid arch.'"),
                ('1864',
                 'James Clerk Maxwell establishes reciprocal force diagrams relating form polygons '
                 'to closed equilibrium force polygons.'),
                ('1966',
                 "Jacques Heyman publishes 'The Stone Skeleton' (DOI "
                 '10.1016/0020-7683(66)90018-7), proving the lower-bound safe theorem of masonry '
                 'arches.'),
                ('2014–2018',
                 'Raman et al. (DOI 10.1038/nature13883) and Mandal et al. (DOI '
                 '10.1126/science.aat9513) demonstrate daytime sub-ambient radiative sky cooling '
                 'across the 8–13 μm atmospheric window.'),
                ('2017–2026',
                 'Philippe Block and Tom Van Mele release the MIT-licensed COMPAS framework '
                 '(compas-dev/compas), bringing 2D/3D graphic statics to Python.')],
 'act2_intuition': 'The mathematical equilibrium of the seven-voussoir assembly (L = 6000 mm, f = '
                   '2000 mm, t = 400 mm, b = 600 mm) rests on the classical parabolic thrust '
                   'relation H = q L² / (8 f). For a uniform load q = 12 kN/m across span L = 6.0 m '
                   'with crown rise f = 2.0 m, horizontal abutment thrust resolves to exactly H = '
                   '27.00 kN, while ∑ F_i = 0 at every node. Heyman’s middle-third kern requires '
                   'that thrust eccentricity satisfies |e(x)| ≤ t / 6 = 66.7 mm; operating at |e| '
                   '= 18.0 mm maintains pure compression across every radial bed joint. '
                   'Topologically, each discrete hexahedral voussoir has Euler–Poincaré '
                   'characteristic χ = V − E + F = 2, giving aggregate χ = 2 N_v = 14 (V = 56, E = '
                   '126, F = 84) across STEP AP242, 3MF, DXF, and 2-manifold GLB. Simultaneously, '
                   'evaluating the A.11 porous P(VdF-HFP) extrados coating (R_solar = 0.96, '
                   'ε_{8–13 μm} = 0.95) at ambient T_a = 303.15 K under 890 W/m² solar irradiance '
                   'yields net radiative cooling flux q_net = 98.4 W/m² ≥ 80 W/m² and steady-state '
                   'sub-ambient cooling ΔT_eq = −7.08 °C ≤ −4.5 °C.',
 'sliders': [{'id': 'tp-tool-s0',
              'label': 'Vault Crown Rise f',
              'min': 1200,
              'max': 3000,
              'step': 100,
              'value': 2000,
              'unit': ' mm'},
             {'id': 'tp-tool-s1',
              'label': 'Thrust Eccentricity |e| (vs t/6 = 66.7 mm)',
              'min': 0,
              'max': 110,
              'step': 5,
              'value': 18,
              'unit': ' mm'}],
 'readouts': [{'label': '7-Voussoir Topology (V, E, F)', 'value': 'V=56, E=126, F=84 · χ=14'},
              {'label': 'Thrust H & Heyman Kern', 'value': 'H = 27.0 kN · |e| = 18.0 ≤ 66.7 mm'},
              {'label': 'A.11 Sky-Cooling Extrados', 'value': 'q_net = 98.4 W/m² · ΔT_eq = −7.08 °C'},
              {'label': '4-Format Export Verdict', 'value': 'STEP AP242 · 3MF · DXF · GLB PASS'}],
 'steps': ['Stage 1: Funicular Thrust-Line & Joint-Normal Synthesis — Evaluate z(x_k) = f(1 − '
           '(2x_k/L)²) and unit normal n(x_k) across N_v + 1 = 8 radial stations (L = 6000 mm, f = '
           '2000 mm, t = 400 mm) to bound 7 compression-only voussoir blocks at H = 27.0 kN.',
           'Stage 2: Multi-Body Watertight Hexahedral Extrusion — Extrude each radial quad across '
           'bay width b = 600 mm into an 8-vertex, 12-triangle closed hexahedron (total V = 56, E '
           '= 126, F = 84, Euler–Poincaré characteristic χ = 2 N_v = 14).',
           'Stage 3: 4-Format Studio Exchange & A.11 Extrados Coupling — Emit x03_artifact.glb, '
           'x03_artifact.step (AP242 B-rep), x03_artifact.3mf, and x03_artifact.dxf while '
           'evaluating 8–13 μm radiative sky-cooling flux across the 4.69 m² extrados shell.',
           'Stage 4: Heyman Kern, Sky-Cooling & Divergence-Volume Verification — Certify |e| ≤ t/6 '
           '= 66.7 mm, q_net = 98.4 W/m² ≥ 80 W/m² (ΔT_eq = −7.08 °C ≤ −4.5 °C), exact 3D volume '
           'match (1.7724 × 10⁹ mm³), and planted-defect rejection.'],
 'rules': ['Multi-Voussoir Topological Closure: Each of the N_v = 7 discrete voussoirs must be an '
           'independent closed 2-manifold (3F = 2E, χ = 2 per block, total χ = 2 N_v = 14) across '
           'GLB, 3MF, and STEP AP242 with zero non-manifold edges.',
           'Heyman Middle-Third Safe Kern Bound: At L = 6000 mm, f = 2000 mm, t = 400 mm, H = 27.0 '
           'kN, thrust eccentricity |e| must satisfy |e| ≤ t/6 = 66.7 mm so compressive stresses '
           'remain non-negative across every joint.',
           'A.11 Passive Sky-Cooling Extrados & 4-Format Volume Identity: The 8–13 μm coating '
           '(ε_{8–13 μm} = 0.95, R_solar = 0.96) must achieve q_net ≥ 80 W/m² and ΔT_eq ≤ −4.5 °C '
           'at T_a = 303.15 K, while 3D mesh volume matches 2D DXF shoelace area × b = 600 mm '
           'within 10⁻⁴ relative error.'],
 'sidenote_1': {'kicker': 'SIDENOTE X.03-A · WHY SMALL ARCHITECTURE STUDIOS NEED OPEN EXCHANGE',
                'body': 'A small practice collaborating with a local stonemason, timber '
                        'fabricator, or structural engineer often needs 2D DXF cutting templates '
                        'and 3D STEP/3MF solids simultaneously. Generating all four from one '
                        'script eliminates manual redrawing errors.'},
 'sidenote_2': {'kicker': 'SIDENOTE X.03-B · COMPAS & BONSAI BIM: SOVEREIGN OPEN ARCHITECTURE',
                'body': "Both ETH Zurich's COMPAS framework and the Bonsai BIM / IfcOpenShell + "
                        'ezdxf open-source ecosystem are MIT-licensed and run in standard Python '
                        '3, letting studios read and write geometry without a commercial license '
                        'seat.'},
 'walkthrough': ['Orbit the 7-voussoir funicular arch in the WebGL2 inspector below; notice how '
                 'vertex colors highlight the keystone compression crown versus the springer '
                 'haunches.',
                 'Drag Thrust Eccentricity |e| past 66.7 mm (or click [⚡ Counterfactual '
                 "Axiom-Knockout]) to see the thrust line exit Heyman's middle-third kern and open "
                 'a hinge.',
                 'Download x03_artifact.dxf (for 2D CAD/laser cutting templates), '
                 'x03_artifact.step, x03_artifact.3mf, and x03_artifact.glb, plus the small-studio '
                 'SKILL.md companion.'],
 't0_t1_certified': ['Deterministic 4-format generator (skills/toolchain/x03/make_x03.py) emitting '
                     'x03_artifact.glb, x03_artifact.step (AP242), x03_artifact.3mf, and '
                     'x03_artifact.dxf.',
                     'Byte-level stdlib verifier '
                     '(verify_x03_toolchain_x03_small_architect_vault_kit.py) certifying 7-block '
                     'watertightness (χ = 14), H = 27.0 kN, A.11 sky-cooling flux (q_net = 98.4 '
                     'W/m², ΔT_eq = −7.08 °C), exact volume match, and planted-defect knockout.',
                     'Portable SKILL.md companion tailored for small architecture studios using '
                     'Blender, FreeCAD, COMPAS, and QCAD Community Edition / LibreCAD.'],
 't2_t3_open_horizon': ['Educational Geometry Boundary: Every file on this page is an educational '
                        'artifact; nothing is certified as load-bearing, printable, safe, or fit '
                        'for any purpose.',
                        'Future Edition 2 Extensions: Polyhedral 3D graphic statics multi-rib '
                        'groin vaults, hygrometric dew-point coupling on radiative extrados shells, '
                        'and open-standard IFC 4.3 structural analysis view export.'],
 'sources': ['Heyman, J. (1966). The stone skeleton. International Journal of Solids and '
             'Structures, 2(2), 249–279. DOI 10.1016/0020-7683(66)90018-7',
             'Akbarzadeh, M., Van Mele, T., & Block, P. (2015). On the equilibrium of funicular '
             'polyhedral frames and convex polyhedral force diagrams. Computer-Aided Design, 63, '
             '118–128. DOI 10.1016/j.cad.2015.01.006',
             'Raman, A. P., Anoma, M. A., Zhu, L., Rephaeli, E., & Fan, S. (2014). Passive '
             'radiative cooling below ambient air temperature under direct sunlight. Nature, '
             '515(7528), 540–544. DOI 10.1038/nature13883',
             'Mandal, J., Fu, Y., Overvig, A. C., Jia, M., Sun, K., Shi, N. N., Zhou, H., Xiao, '
             'X., Yu, N., & Yang, Y. (2018). Hierarchically porous polymer coatings for highly '
             'efficient passive daytime radiative cooling. Science, 362(6412), 315–319. DOI '
             '10.1126/science.aat9513',
             'Block, P., & Ochsendorf, J. (2007). Thrust network analysis: A new methodology for '
             'three-dimensional equilibrium. Journal of the International Association for Shell '
             'and Spatial Structures, 48(3), 167–173.',
             'Van Mele, T., et al. (2017–2026). COMPAS: A framework for computational research in '
             'architecture and structures (MIT License). https://github.com/compas-dev/compas'],
 'act1_plain_bridge': 'Every historic masonry arch that has stood for centuries quietly proves '
                      'that stone works best when squeezed together rather than pulled apart. For '
                      'a small one-to-five person architectural studio, proving that a curved '
                      'vault or timber reciprocal roof will stand safely used to require expensive '
                      'proprietary software licenses that strained modest project budgets. This '
                      'interactive kit changes that equation by bringing classical thrust network '
                      'analysis directly to your browser and local workstation. With a single '
                      'click, you can generate and download four production-ready file formats at '
                      'zero cost. Open the three-dimensional GLB model in Blender for client '
                      'walkthroughs, import the solid STEP geometry into FreeCAD for precision CNC '
                      'milling, send the lightweight 3MF file to an Ultimaker or Prusa 3D printer '
                      'for physical scale mockups, and load the flat DXF shop drawings into QCAD '
                      'or LibreCAD for timber template fabrication.',
 'act1_stakes': 'Small architecture studios face a structural disadvantage when bidding on '
                'expressive, sustainable structural designs. Dominant commercial software suites '
                'charge thousands of dollars annually per seat, locking independent practices out '
                'of advanced vault form-finding, reciprocal timber detailing, and unreinforced '
                'masonry certification. As a result, small practices are pushed toward '
                'conventional post-and-beam steel or reinforced concrete schemes that carry '
                'massive embodied carbon penalties and demand heavy steel reinforcement. This '
                'toolkit dismantles that financial barrier. By packaging classical limit state '
                'analysis into a transparent, scriptable Python pipeline, a three-person studio '
                'can verify compression equilibrium on a laptop in seconds. Architects can rapidly '
                'design low-carbon limestone arches, recycled brick vaults, or reciprocal timber '
                'nexorades with complete structural authority. Generating open STEP and DXF files '
                'empowers designers to partner directly with local stone carvers and CNC '
                'carpenters, keeping fabrication budgets local while expanding creative '
                'architectural agency.',
 'act2_analogy': 'Hold a heavy brass chain loosely between your hands and watch it settle under '
                 'its own weight. Gravity pulls every link into a pure tension curve known as a '
                 'catenary. If you were to freeze those links solidly in place and flip the entire '
                 'assembly upside down, every tension force would invert into pure compression. '
                 'This inverted chain describes the invisible line of thrust running through a '
                 'stone arch. As long as that compressive thrust presses firmly through the middle '
                 'third of each dry-stone block, the stones press tightly together and the arch '
                 'stands effortlessly.',
 'act2_plain_primer': 'The interactive workbench gives you immediate physical control over vault '
                      'equilibrium through two calibrated sliders and an axiom knockout test. The '
                      'first slider adjusts Vault Crown Rise, allowing you to raise or lower the '
                      'arch apex from twelve hundred to three thousand millimeters. Increasing '
                      'crown height steepens the arch trajectory, dramatically reducing horizontal '
                      'outward thrust against the support abutments. The second slider controls '
                      'Thrust Eccentricity, shifting the internal thrust line away from the block '
                      'centerlines up to one hundred and ten millimeters. At the default eighteen '
                      'millimeters, the thrust stays safely within the sixty-six point seven '
                      'millimeter middle-third kern limit, keeping the contact faces entirely '
                      'under compression. When you trigger the Counterfactual Axiom-Knockout '
                      'button, the system forces eccentricity beyond this boundary. You will '
                      'immediately watch the joints open into a four-hinge kinematic collapse '
                      'mechanism, revealing exactly why classical stone arches fail geometrically.',
 'act2_deepening': 'Beneath the visual interface, Maxwell’s reciprocal force duality governs every '
                   'geometric transformation. For every primal polygon formed by the interlocking '
                   'voussoirs, there exists an orthogonal dual polygon in Maxwell–Rankine force '
                   'space whose edge lengths correspond directly to internal compressive thrust '
                   'magnitudes (Akbarzadeh et al., 2015, DOI: 10.1016/j.cad.2015.01.006). When you '
                   'adjust crown rise f, the algorithmic pipeline dynamically updates nodal '
                   'coordinates and rescales the dual force polyhedron without re-meshing the '
                   'physical assembly. Each voussoir block is parameterized as a closed prismatic '
                   'hexahedron (V = 8, E = 18, F = 12, χ = 2 per block; aggregate χ = 2 N_v = 14) '
                   'bounded by radial contact planes and intrados/extrados chords across L = 6000 '
                   'mm, f = 2000 mm, t = 400 mm, and b = 600 mm. Simultaneously, the outer extrados '
                   'facets (4.69 m² per bay) carry Folio A.11’s porous P(VdF-HFP) sky-cooling '
                   'envelope (R_solar = 0.96, ε_{8–13 μm} = 0.95), exporting q_net = 98.4 W/m² to '
                   'the cold sky (ΔT_eq = −7.08 °C at T_a = 303.15 K) before multi-format STEP '
                   'AP242, 3MF, DXF, and GLB serialization.',
 'act4_human_ai': 'In a small design studio, partnering with an AI coding assistant transforms '
                  'structural ideation from passive drafting into verifiable engineering. Rather '
                  'than treating artificial intelligence as a speculative image generator, the '
                  'architect deploys the AI model as an analytical copilot guided by make_x03.py, '
                  'verify_x03_toolchain_x03_small_architect_vault_kit.py, and the accompanying '
                  'SKILL.md specification. When client requirements dictate an irregular vault '
                  'span or altered clearance, the architect prompts the assistant to modify '
                  'boundary constraints in the generator script. Before committing to fabrication, '
                  'the studio executes the standalone verification script, which rigorously audits '
                  'the middle-third kern compliance, checks static equilibrium ∑ F_i = 0, and '
                  'validates Euler topological invariants across all exported CAD formats. The AI '
                  'agent cannot hallucinate non-functional geometry because the Python verifier '
                  'acts as a deterministic mathematical gatekeeper. This collaborative workflow '
                  'provides boutique studios with the rigorous engineering validation previously '
                  'restricted to multinational engineering firms, ensuring constructability at '
                  'zero overhead.',
 'act4_deepening': 'This toolkit forms a synthesis across structural physics, projective geometry, '
                   'and radiative envelope thermodynamics, linking directly to our companion '
                   'folios. It deepens the funicular equilibrium foundations established in Folio '
                   'A.01, which maps Heyman masonry vaults against Glaser thermal diffusion nodes. '
                   'In REV 1.4, Toolbox X.03 couples directly to Folio A.11’s concave Airy stress '
                   'surfaces (det(H_Φ) > 0), three-dimensional reciprocal polyhedra, and passive '
                   'daytime radiative sky-cooling extrados coatings (Raman et al., 2014, DOI: '
                   '10.1038/nature13883; Mandal et al., 2018, DOI: 10.1126/science.aat9513), '
                   'allowing unreinforced compression vaults to shed 98.4 W/m² through the 8–13 μm '
                   'atmospheric window while storing sub-ambient coolness in thermal stone mass. '
                   'When voussoir contact faces rotate to accommodate mutual bearing without '
                   'falsework, the mechanics bridge into Folio A.02’s reciprocal timber nexorades, '
                   'and when cast with low-carbon earth mortars, their pumpability follows Folio '
                   'E.02’s Herschel–Bulkley rheology.',
 'plain_es': 'Cualquier arco de piedra tradicional demuestra que la mampostería trabaja a la '
             'perfección cuando se comprime y sufre cuando se tensiona. Para un taller '
             'independiente de arquitectura de una a cinco personas, calcular una bóveda curva o '
             'una cubierta recíproca de madera solía requerir costosas licencias de software '
             'privativo fuera del alcance presupuestal. Esta herramienta interactiva democratiza '
             'ese cálculo al integrar el análisis estático clásico directamente en tu navegador y '
             'computadora local sin costo alguno. Con un solo clic puedes descargar cuatro '
             'formatos listos para taller. Puedes abrir el modelo tridimensional GLB en Blender '
             'para presentaciones con clientes, importar el sólido STEP en FreeCAD para mecanizado '
             'CNC de dovelas, mandar el archivo 3MF a tu impresora 3D para maquetas físicas y '
             'cargar los planos DXF en QCAD o LibreCAD para cortar plantillas de carpintería y '
             'cantería artesanal.',
 'deep_es': 'El equilibrio estático de este ensamblaje de siete dovelas (L = 6000 mm, f = 2000 '
            'mm, t = 400 mm, b = 600 mm) se fundamenta en la teoría plástica de Jacques Heyman y '
            'la estática gráfica recíproca de Maxwell y Rankine. El empuje horizontal H = q L² / '
            '(8 f) resulta exactamente en 27.00 kN, confinando la excentricidad |e| = 18.0 mm '
            'dentro del núcleo central |e(x)| ≤ t / 6 = 66.7 mm. Topológicamente, cada dovela '
            'hexaédrica cerrada posee característica de Euler–Poincaré χ = 2, sumando χ = 2 N_v = '
            '14 (56 vértices, 126 aristas y 84 caras) en STEP AP242, 3MF, DXF y GLB 2-variedad. '
            'En REV 1.4, el extradós acopla el recubrimiento poroso P(VdF-HFP) del Folio A.11 '
            '(R_solar = 0.96, ε_{8–13 μm} = 0.95), alcanzando un flujo neto de enfriamiento '
            'radiativo diurno q_net = 98.4 W/m² ≥ 80 W/m² y ΔT_eq = −7.08 °C ≤ −4.5 °C a T_a = '
            '303.15 K.',
 'distill_diagram': {'analogy_title': 'The Inverted Hanging Chain',
                     'analogy_sub': 'Gravity tension inverts into pure compressive vault '
                                    'equilibrium',
                     'force_a_title': 'Vault Crown Rise (f)',
                     'force_a_sub': 'Sets arch apex height and modulates horizontal abutment '
                                    'thrust H',
                     'force_b_title': 'Thrust Line Eccentricity (|e|)',
                     'force_b_sub': 'Tracks the internal compressive vector relative to block '
                                    'centers',
                     'threshold_title': 'Heyman Middle-Third Kern (|e| ≤ t/6 = 66.7 mm)',
                     'threshold_pass': 'Full cross-sectional compression across all seven '
                                       'voussoirs',
                     'threshold_fail': 'Tensile joint separation opens four-hinge kinematic '
                                       'collapse'}}
