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
           'studios and solo practitioners: using MIT-licensed Python tools (COMPAS, Bonsai BIM / IfcOpenShell, '
           'Blender, FreeCAD), a small studio can generate compression-only stone, brick, or '
           'cross-laminated timber (CLT) voussoir arches, verify their thrust-line equilibrium, '
           'and export 3D solids (.step, .3mf, .glb) plus 2D cutting templates (.dxf).',
 'why_es': 'En la arquitectura actual, la búsqueda de forma estructural suele quedar reservada '
           'para grandes corporativos con presupuestos de software inalcanzables. Diseñamos el '
           'Folio X.03 específicamente para empoderar a pequeños despachos de arquitectura y '
           'profesionales independientes: usando herramientas abiertas en Python con licencia MIT '
           '(COMPAS, Bonsai BIM / IfcOpenShell, Blender, FreeCAD), cualquier estudio puede generar arcos y bóvedas '
           'de piedra, ladrillo o madera (CLT) a compresión pura, verificar su línea de empuje y '
           'exportar sólidos 3D (.step, .3mf, .glb) y plantillas de corte 2D (.dxf).',
 'governing_law': 'H = q L² / (8 f) = 27.0 kN · |e(x)| ≤ t / 6 = 66.7 mm · ∑ F_i = 0 · χ = 2 N_v = '
                  '14',
 'pass_pill_en': 'PASS · 7 VOUSSOIRS · χ = 14 · H = 27.0 kN · STEP+3MF+DXF+GLB',
 'pass_pill_es': 'APROBADO · 7 DOVELAS · χ = 14 · H = 27.0 kN · STEP+3MF+DXF+GLB',
 'generator_script': 'skills/toolchain/x03/make_x03.py',
 'verifier_script': 'skills/toolchain/x03/verify_x03_toolchain_x03_small_architect_vault_kit.py',
 'skill_dir': 'skills/toolchain/x03',
 'skill_name': 'toolchain-x03-small-architect-vault-kit',
 'formats': ('glb', 'step', '3mf', 'dxf'),
 'primary_doi': '10.1016/j.CAD.2017.07.005',
 'scite_summary': 'Heyman (1966) safe theorem of masonry limit analysis and ETH Zurich Block '
                  'Research Group COMPAS graphic statics verified offline.',
 'date_published': '2026-11-08',
 'date_redated': '2026-11-08',
 'current_edition': 'REV 1.0',
 'reading_time': '22 MIN READ',
 'small_studio_kit_en': 'Boutique Architecture Studio Stack (COMPAS MIT + Blender 4.2 / Bonsai + '
                        'FreeCAD 1.0 + QCAD Community Edition / LibreCAD): Run make_x03.py to generate a 7-voussoir '
                        'funicular arch across 4 open formats—x03_artifact.glb for client WebGL '
                        'walkthroughs, x03_artifact.step for structural engineer coordination, '
                        'x03_artifact.3mf for 1:20 desktop study models, and x03_artifact.dxf for '
                        '2D stone/CLT CNC шаблоны (templates).',
 'small_studio_kit_es': 'Stack para Pequeños Estudios de Arquitectura (COMPAS MIT + Blender 4.2 / '
                        'Bonsai + FreeCAD 1.0 + QCAD Community Edition / LibreCAD): Ejecuta make_x03.py para generar un '
                        'arco funicular de 7 dovelas en 4 formatos abiertos: x03_artifact.glb para '
                        'presentaciones WebGL con clientes, x03_artifact.step para coordinación '
                        'estructural, x03_artifact.3mf para maquetas físicas 1:20 y '
                        'x03_artifact.dxf para plantillas de corte 2D en CNC.',
 'companion_folios': [('architecture',
                       'a11',
                       'Folio A.11',
                       '3D Polyhedral Graphic Statics & Stone Vaults'),
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
                    ('Bonsai BIM / IfcOpenShell (Native Open BIM)',
                     'https://bonsaibim.org/'),
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
              'through thrust network analysis and the open-source COMPAS framework (DOI: '
              '10.1016/j.CAD.2017.07.005). By translating reciprocal polyhedra into algebraic '
              'matrices, they showed that complex three-dimensional compression vaults can be '
              'calculated without non-linear finite element solvers, directly linking graphic '
              'statics to computerized architectural production.',
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
                ('2017–2026',
                 'Philippe Block and Tom Van Mele release the MIT-licensed COMPAS framework '
                 '(compas-dev/compas), bringing 2D/3D graphic statics to Python.')],
 'act2_intuition': 'The mathematical equilibrium of the seven-voussoir assembly rests on the '
                   'classical parabolic thrust relation H = q L² / (8 f). For a uniform load q '
                   'across span L with crown rise f = 2000 mm, the horizontal abutment thrust '
                   'resolves to exactly H = 27.00 kN. Static equilibrium demands that the vector '
                   'sum of all internal joint forces vanishes, ∑ F_i = 0. To guarantee that no '
                   'tensile stresses develop across any block interface of thickness t = 400 mm, '
                   'Heyman’s middle-third kern requires that the thrust eccentricity satisfies '
                   '|e(x)| ≤ t / 6 = 66.7 mm. Operating at |e| = 18.0 mm maintains full '
                   'cross-sectional compression. Topologically, each individual voussoir forms an '
                   'independent closed polyhedron with Euler characteristic χ = V − E + F = 2. '
                   'Across the entire seven-block assembly, the aggregate topological invariant '
                   'evaluates to χ = 2 N_v = 14, comprising V = 56 vertices, E = 126 edges, and F '
                   '= 84 faces, confirming boundary manifold closure.',
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
              {'label': 'Maxwell–Rankine Thrust H', 'value': '27.00 kN (at L=6m, f=2m)'},
              {'label': 'Heyman Middle-Third Kern', 'value': '|e| = 18.0 ≤ 66.7 mm (PASS)'},
              {'label': '4-Format Export Verdict', 'value': 'GLB · STEP · 3MF · DXF PASS'}],
 'steps': ['Stage 1: Funicular Thrust-Line & Joint-Normal Synthesis — Evaluate z(x_k) = f(1 − '
           '(2x_k/L)²) and unit normal n(x_k) across N_v + 1 = 8 radial stations to bound 7 '
           'compression-only voussoir blocks.',
           'Stage 2: Multi-Body Watertight Hexahedral Extrusion — Extrude each radial quad across '
           'bay width b = 600 mm into an 8-vertex, 12-triangle closed hexahedron (total V = 56, E '
           '= 126, F = 84, Euler characteristic χ = 2β_0 = 14).',
           'Stage 3: 4-Format Studio Exchange Generation — Emit x03_artifact.glb (WebGL/Blender), '
           'x03_artifact.step (AP242 B-rep), x03_artifact.3mf (1:20 physical model), and '
           'x03_artifact.dxf (2D CUT elevation + MOUNTAIN thrust line).',
           'Stage 4: Heyman Kern & Divergence-Volume Verification — Certify |e| ≤ t/6 = 66.7 mm, '
           'verify exact agreement between shoelace-extruded volume and 3D divergence volume '
           '(1.7724 × 10⁹ mm³), and test planted-defect rejection.'],
 'rules': ['Multi-Voussoir Topological Closure: Each of the N_v = 7 discrete voussoirs must be an '
           'independent closed 2-manifold (3F = 2E, χ = 2 per block, total χ = 14) with zero '
           'non-manifold edges.',
           'Heyman Middle-Third Safe Kern Bound: The thrust eccentricity |e| must satisfy |e| ≤ '
           't/6 (66.7 mm for t = 400 mm) at every bed joint so compressive stresses remain '
           'non-negative across the entire joint.',
           '4-Format Provenance & Volume Identity: The signed 3D mesh volume in GLB/3MF/STEP must '
           'match the 2D DXF elevation shoelace area multiplied by bay width b = 600 mm within '
           '10⁻⁴ relative error.'],
 'sidenote_1': {'kicker': 'SIDENOTE X.03-A · WHY SMALL ARCHITECTURE STUDIOS NEED OPEN EXCHANGE',
                'body': 'A small practice collaborating with a local stonemason, timber '
                        'fabricator, or structural engineer often needs 2D DXF templates and 3D '
                        'STEP/3MF solids simultaneously. Generating all four from one script '
                        'eliminates manual redrawing errors.'},
 'sidenote_2': {'kicker': 'SIDENOTE X.03-B · COMPAS & BONSAI BIM: SOVEREIGN OPEN ARCHITECTURE',
                'body': "Both ETH Zurich's COMPAS framework and the Bonsai BIM / IfcOpenShell + ezdxf open-source ecosystem "
                        'are MIT-licensed and run in standard Python 3, letting studios read and '
                        'write geometry without a commercial license seat.'},
 'walkthrough': ['Orbit the 7-voussoir funicular arch in the WebGL2 inspector below; notice how '
                 'vertex colors highlight the keystone compression crown versus the springer '
                 'haunches.',
                 'Drag Thrust Eccentricity |e| past 66.7 mm (or click [⚡ Counterfactual '
                 "Axiom-Knockout]) to see the thrust line exit Heyman's middle-third kern and open "
                 'a hinge.',
                 'Download x03_artifact.dxf (for 2D CAD/laser templates), x03_artifact.step, '
                 'x03_artifact.3mf, and x03_artifact.glb, plus the small-studio SKILL.md '
                 'companion.'],
 't0_t1_certified': ['Deterministic 4-format generator (skills/toolchain/x03/make_x03.py) emitting '
                     'x03_artifact.glb, x03_artifact.step, x03_artifact.3mf, and x03_artifact.dxf.',
                     'Byte-level stdlib verifier '
                     '(verify_x03_toolchain_x03_small_architect_vault_kit.py) certifying 7-block '
                     'watertightness (χ = 14), exact volume match, DXF layer structure, and '
                     'planted-defect knockout.',
                     'Portable SKILL.md companion tailored for small architecture studios using '
                     'Blender, FreeCAD, COMPAS, and QCAD Community Edition / LibreCAD.'],
 't2_t3_open_horizon': ['Educational Geometry Boundary: Every file on this page is an educational '
                        'artifact; nothing is certified as load-bearing, printable, safe, or fit '
                        'for any purpose.',
                        'Future Edition 2 Extensions: Polyhedral 3D graphic statics multi-rib '
                        'groin vaults and open-standard IFC 4.3 structural analysis view export.'],
 'sources': ['Heyman, J. (1966). The stone skeleton. International Journal of Solids and '
             'Structures, 2(2), 249–279. DOI 10.1016/0020-7683(66)90018-7',
             'Block, P., & Ochsendorf, J. (2007). Thrust network analysis: A new methodology for '
             'three-dimensional equilibrium. Journal of the International Association for Shell '
             'and Spatial Structures, 48(3), 167–173.',
             'Van Mele, T., et al. (2017–2026). COMPAS: A framework for computational research in '
             'architecture and structures (MIT License). https://github.com/compas-dev/compas',
             'Rippmann, M., & Block, P. (2013). Funicular shell design exploration. ACADIA 2013 '
             'Adaptive Architecture, 337–346.'],
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
                   'voussoirs, there exists an orthogonal dual polygon in Maxwell-Rankine force '
                   'space whose edge lengths correspond directly to internal compressive thrust '
                   'magnitudes. When you adjust crown rise f, the algorithmic pipeline dynamically '
                   'updates the nodal coordinates and rescales the dual force polyhedron without '
                   're-meshing the physical assembly. Each voussoir block is parameterized as a '
                   'solid prismatic hexahedron bounded by radial contact planes and curved '
                   'intrados and extrados surfaces. Contact stresses are evaluated across planar '
                   'quadrilaterals using trapezoidal compressive stress blocks. If the '
                   'eccentricity exceeds t / 6, the stress distribution triangularizes and contact '
                   'separates, introducing an unconstrained rotational hinge. By enforcing '
                   'equilibrium across the dual force network, the generator verifies that the '
                   'resultant thrust vector remains strictly within the middle third of every '
                   'radial bed joint before triggering multi-format export.',
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
                   'and modern material science, linking directly to our companion folios. It '
                   'deepens the funicular equilibrium foundations established in Folio A.01, which '
                   'maps Heyman masonry vaults against Glaser thermal diffusion nodes. The '
                   'polyhedral graphic statics implemented here directly extend Folio A.11’s '
                   'three-dimensional reciprocal polyhedra, proving how dual force diagrams '
                   'eliminate embodied carbon in floor plates by eliminating steel reinforcement. '
                   'When voussoir contact faces rotate to accommodate mutual bearing without '
                   'falsework, the mechanics bridge into Folio A.02’s reciprocal timber nexorades, '
                   'where interlocking timber members support spans far exceeding individual stick '
                   'lengths through mutual lap joints. Furthermore, when these voussoirs are cast '
                   'using modern low-carbon binders or 3D-printed earth mortars, their yield '
                   'stress and pumpability are governed by Folio E.02’s Herschel-Bulkley concrete '
                   'rheology. Together, these interdisciplinary links demonstrate that ancient '
                   'stereotomy and cutting-edge computational mechanics are twin expressions of '
                   'unyielding equilibrium physics.',
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
 'deep_es': 'El equilibrio estático de este ensamblaje de siete dovelas se fundamenta en la teoría '
            'plástica de Jacques Heyman y la estática gráfica recíproca de Maxwell y Rankine. La '
            'fuerza horizontal de empuje se determina mediante H = q L² / (8 f), resultando '
            'exactamente en 27.00 kN para un peralte de dos mil milímetros. Para erradicar '
            'cualquier esfuerzo de tracción en un material sin cohesión tensil, la línea de empuje '
            'debe confinarse estrictamente dentro del tercio medio de la sección de espesor t = '
            '400 mm, cumpliendo |e(x)| ≤ t / 6 = 66.7 mm. Con una excentricidad de operación de '
            '18.0 mm, las juntas radiales mantienen compresión total en sus caras de contacto. '
            'Topológicamente, cada bloque constituye un poliedro cerrado con característica de '
            'Euler χ = 2, totalizando χ = 14 en la macroestructura con 56 vértices, 126 aristas y '
            '84 caras conformando un colector cerrado estanco.',
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
