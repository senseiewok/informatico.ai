# -*- coding: utf-8 -*-
"""Tech & Tools · The Toolbox — Folio X.04: Miura-Ori Deployable Solar Screens: From 3D Folding Kinematics (GLB) to Flat-Pattern DXF."""

FOLIO = {'slug': 'x04',
 'folio_id': 'X.04',
 'tool_id': 'TOOL-ARCH-2',
 'cat': 'architecture',
 'plate_slug': 'x04',
 'pillar_label_en': 'Small Architect & Maker Fabrication · Kinetic Facades & Laser/CNC DXF',
 'pillar_label_es': 'Fabricación para Arquitectos y Makers · Fachadas Cinéticas y DXF para '
                    'Láser/CNC',
 'badge_en': 'TOOLBOX X.04 · MIURA-ORI DEPLOYABLE SCREEN: 3D GLB/3MF + 2D LASER-CUTTER DXF',
 'badge_es': 'HERRAMIENTA X.04 · PANTALLA DESPLEGABLE MIURA-ORI: GLB/3MF 3D + DXF 2D PARA CORTE '
             'LÁSER',
 'title': 'Miura-Ori Deployable Solar Screens: From 3D Folding Kinematics (GLB) to Flat-Pattern '
          'DXF',
 'title_es': 'Pantallas Solares Desplegables Miura-Ori: De la Cinemática 3D (GLB) al Patrón Plano '
             'DXF',
 'subtitle': 'Bridging 3D deployable origami kinematics and 2D sheet fabrication: generate a '
             'watertight thickened Miura-ori facade shell (.glb, .3mf) and a laser-cutter/plotter '
             "crease pattern (.dxf) verified by Kawasaki–Justin and Maekawa's theorems.",
 'subtitle_es': 'Uniendo la cinemática origami 3D con la fabricación en lámina 2D: genera una '
                'envolvente Miura-ori hermética (.glb, .3mf) y su patrón de pliegue 2D (.dxf) para '
                'cortadora láser verificado por los teoremas de Kawasaki–Justin y Maekawa.',
 'why_en': 'Small architectural practices and independent makers frequently prototype adaptive '
           'shading screens, acoustic baffles, and folded-plate canopies using laser cutters, CNC '
           'drag-knives, or sheet-metal brakes. Folio X.04 pairs a 3D thickened Miura-ori shell '
           '(.glb, .3mf) with a production-structured 2D clean-room ASCII DXF (R2000 standard) '
           'flat pattern separated into CUT, MOUNTAIN, and VALLEY layers—while proving '
           'mathematically that every interior degree-4 vertex satisfies flat-foldability.',
 'why_es': 'Los estudios pequeños de arquitectura y talleres de fabricación digital suelen '
           'prototipar celosías solares adaptativas, paneles acústicos y cubiertas plegadas con '
           'cortadoras láser, routers CNC o dobladoras de lámina. El Folio X.04 combina una malla '
           '3D Miura-ori con espesor (.glb, .3mf) y un patrón plano 2D en formato DXF separado en '
           'capas CUT, MOUNTAIN y VALLEY—demostrando matemáticamente que cada vértice interior de '
           'grado 4 cumple la plegabilidad plana.',
 'governing_law': '∑_{i=1}^4 (−1)^i α_i = 78° − 102° + 102° − 78° = 0° · |M − V| = 2 · V = A_xy · '
                  'h = 144,000 mm³',
 'pass_pill_en': 'PASS · KAWASAKI Δα = 0° · |M−V| = 2 · GLB + 3MF + DXF',
 'pass_pill_es': 'APROBADO · KAWASAKI Δα = 0° · |M−V| = 2 · GLB + 3MF + DXF',
 'generator_script': 'skills/toolchain/x04/make_x04.py',
 'verifier_script': 'skills/toolchain/x04/verify_x04_toolchain_x04_miura_ori_dxf_fabricator.py',
 'skill_dir': 'skills/toolchain/x04',
 'skill_name': 'toolchain-x04-miura-ori-dxf-fabricator',
 'formats': ('glb', '3mf', 'dxf'),
 'primary_doi': '10.1073/pnas.1217998110',
 'scite_summary': 'Miura (1985) rigid origami kinematics, Schenk & Guest (2013) metamaterial '
                  'Poisson ratio, and Kawasaki–Justin flat-foldability verified offline.',
 'date_published': '2026-11-08',
 'date_redated': '2026-11-08',
 'current_edition': 'REV 1.0',
 'reading_time': '22 MIN READ',
 'small_studio_kit_en': 'Digital Fabrication & Laser-Cutter Kit (Inkscape / QCAD / LibreCAD / '
                        'LaserWeb + Blender): Open x04_artifact.dxf directly in any 2D CAD or '
                        'laser-cutter tool—layer CUT ( perimeter profile), layer MOUNTAIN (dashed '
                        'score lines), and layer VALLEY (dash-dot score lines)—and preview the '
                        'folded 3D state in x04_artifact.glb or print a snapped study tile from '
                        'x04_artifact.3mf.',
 'small_studio_kit_es': 'Kit de Fabricación Digital y Corte Láser (Inkscape / QCAD / LibreCAD / '
                        'LaserWeb + Blender): Abre x04_artifact.dxf directamente en cualquier '
                        'software CAD 2D o de corte láser—capa CUT (perímetro de corte), capa '
                        'MOUNTAIN (grabado de pliegue montaña) y capa VALLEY (grabado de pliegue '
                        'valle)—e inspecciona el estado plegado 3D en x04_artifact.glb o imprime '
                        'el módulo en 3D con x04_artifact.3mf.',
 'companion_folios': [('architecture',
                       'a10',
                       'Folio A.10',
                       'Miura-Ori Auxetic Kinetic Origami Facades'),
                      ('architecture',
                       'a04',
                       'Folio A.04',
                       'British High-Tech Gerberette Megastructures'),
                      ('architecture', 'a09', 'Folio A.09', 'Timoshenko Hygroscopic Timber Skins'),
                      ('math', 'm05', 'Folio M.05', 'AlphaGeometry 2 Euclidean Synthesis')],
 'external_links': [('LibreCAD / QCAD Open DXF Ecosystem', 'https://librecad.org/'),
                    ('Schenk & Guest (2013) Folded Metamaterials (PNAS)',
                     'https://doi.org/10.1073/pnas.1217998110'),
                    ('Origami Simulator / WebGL Crease Pattern Tools',
                     'https://origamisimulator.org/')],
 'act1_dropcap': 'In nineteen seventy, at the Institute of Space and Aeronautical Science in '
                 'Tokyo, astrophysicist Koryo Miura faced a severe aerospace dilemma: how to pack '
                 'hundreds of square meters of solar panel arrays into the cramped nosecone of a '
                 'rocket without mechanical jamming. Inspired by natural buckling patterns in thin '
                 'cylindrical shells, Miura devised a tessellation of interlocking parallelograms '
                 'that opened and closed along a single mechanical degree of freedom. By nineteen '
                 'eighty-five, Japan’s Space Flyer Unit carried his deployable solar canopy into '
                 'orbit, unfolding flawlessly in microgravity. Yet while aerospace engineers '
                 'celebrated its single-motion deployment, mathematicians like Toshikazu Kawasaki '
                 'and Jacques Justin recognized that Miura’s crease pattern obeyed profound local '
                 'geometric conservation laws. In twenty thirteen at Cambridge University, Mark '
                 'Schenk and Simon Guest proved that this pattern behaves as a mechanical '
                 'metamaterial, offering architecture a revolutionary pathway for rigid, auxetic '
                 'building envelopes.',
 'act1_body': 'The transition of Miura-ori from theoretical paper folding to physical '
              'architectural envelopes required solving rigorous kinematic and thickness '
              'constraints. In nineteen eighty-six and nineteen eighty-nine, Jacques Justin and '
              'Toshikazu Kawasaki proved the flat-foldability theorem, establishing that a '
              'four-crease vertex can fold flat if and only if the alternating sum of its '
              'consecutive sector angles equals zero. Simultaneously, Jun Maekawa proved the '
              'topological parity theorem, showing that the difference between mountain and valley '
              'creases meeting at any flat-foldable degree-four node is strictly two. In twenty '
              'thirteen, Mark Schenk and Simon D. Guest published their groundbreaking mechanical '
              'analysis in PNAS (DOI: 10.1073/pnas.1217998110), proving that folded origami sheets '
              'exhibit out-of-plane bending stiffness coupled to negative in-plane Poisson’s '
              'ratios. Soon after, Yan Chen, Rui Peng, and Zhong You resolved the physical panel '
              'thickness problem in Science (DOI: 10.1126/science.aab2870), establishing spatial '
              'kinematic offsets that prevent facet binding during folding, opening the door to '
              'full-scale architectural fabrication.',
 'pullquote': 'Every interior vertex of a flat-foldable crease pattern obeys two combinatorial '
              "laws—Kawasaki's alternating angle sum and Maekawa's mountain-valley parity—that a "
              '30-line Python verifier can check before the laser cutter ever fires.',
 'chronology': [('1970–1985',
                 'Koryo Miura invents the Miura-ori rigid origami fold at ISAS Tokyo for '
                 'deployable solar-panel arrays on space missions.'),
                ('1986–1989',
                 'Jacques Justin and Toshikazu Kawasaki independently prove that a single-vertex '
                 'crease pattern is flat-foldable if and only if its alternating sector angles sum '
                 'to zero.'),
                ('2013',
                 'Mark Schenk and Simon D. Guest prove in PNAS (DOI 10.1073/pnas.1217998110) that '
                 'Miura-ori sheets form negative-Poisson-ratio mechanical metamaterials.'),
                ('2026',
                 'Informatico.ai ships X.04: synchronized 3D watertight GLB/3MF shell and 2D '
                 'layered laser-cutter DXF generation with Kawasaki–Maekawa verification.')],
 'act2_intuition': 'Flat foldability across the Miura-ori screen is governed by the '
                   'Justin-Kawasaki theorem, which dictates that the alternating sum of sector '
                   'angles around every interior node must vanish: ∑_{i=1}^4 (−1)^i α_i = 78° − '
                   '102° + 102° − 78° = 0°. Because adjacent angles are supplementary, α_1 + α_2 = '
                   '180°, the pattern folds completely flat without panel buckling. Crease '
                   'assignments at each degree-four junction obey Maekawa’s parity theorem, |M − '
                   'V| = |3 − 1| = 2, requiring that exactly three mountain creases meet one '
                   'valley crease (or vice versa), guaranteeing topological non-intersection. When '
                   'panel thickness h = 6 mm is introduced to transform the zero-thickness mesh '
                   'into a physical CNC sheet, the material volume follows Cavalieri’s principle '
                   'and the divergence theorem: V = A_xy · h = 144,000.0 mm³, where A_xy '
                   'represents the projected planar area. The resulting solid maintains Euler '
                   'characteristic χ = 2, proving watertight topological closure across all '
                   'facets.',
 'sliders': [{'id': 'tp-tool-s0',
              'label': 'Parallelogram Sector Angle γ',
              'min': 55,
              'max': 85,
              'step': 1,
              'value': 78,
              'unit': '°'},
             {'id': 'tp-tool-s1',
              'label': 'Sheet Offset Thickness h',
              'min': 2,
              'max': 12,
              'step': 1,
              'value': 6,
              'unit': ' mm'}],
 'readouts': [{'label': 'Kawasaki Alternating Sum', 'value': '78° − 102° + 102° − 78° = 0°'},
              {'label': 'Maekawa Crease Parity |M−V|', 'value': '|3 − 1| = 2 (FLAT-FOLDABLE)'},
              {'label': 'Cavalieri / Divergence Volume', 'value': '144,000.0 mm³ (χ = 2 PASS)'},
              {'label': 'DXF Fabrication Layers', 'value': 'CUT · MOUNTAIN · VALLEY'}],
 'steps': ['Stage 1: Degree-4 Crease Kinematics & Kawasaki–Maekawa Synthesis — Assign '
           'parallelogram sector angles (γ = 78°, π − γ = 102°) and 3 Mountain + 1 Valley creases '
           'at each interior vertex so ∑(−1)^i α_i = 0° and |M − V| = 2.',
           'Stage 2: Cavalieri Z-Offset Thickened Shell Construction — Offset the 3×3 folded '
           'lattice by h = 6.0 mm and stitch the 8 perimeter segments into a closed 18-vertex, '
           '32-triangle watertight 2-manifold.',
           'Stage 3: Layered ASCII DXF Toolpath Serialization — Write x04_artifact.dxf with '
           'explicit AC1015 header units (mm) and separate CUT (continuous), MOUNTAIN (dashed), '
           'and VALLEY (dash-dot) LINE entities.',
           'Stage 4: Isometric Volume & Flat-Foldability Verification — Assert V_mesh = A_xy · h = '
           '144,000.0 mm³, verify DXF layer completeness, and confirm the planted-defect knockout '
           'rejects corrupted crease topology.'],
 'rules': ['Kawasaki–Justin Alternating Angle Invariant: At every interior degree-4 vertex with '
           'consecutive sector angles (α_1, α_2, α_3, α_4), flat-foldability requires α_1 − α_2 + '
           'α_3 − α_4 = 0° (α_1 + α_3 = α_2 + α_4 = 180°).',
           'Maekawa Mountain–Valley Parity Invariant: At every flat-foldable interior vertex, the '
           'difference between Mountain (M) and Valley (V) creases must satisfy |M − V| = 2.',
           'Cavalieri Thickened-Shell Volume Identity: The 3D divergence-theorem volume of the '
           'z-offset corrugated manifold must equal A_xy · h = 144,000.0 mm³ with Euler '
           'characteristic χ = 2.'],
 'sidenote_1': {'kicker': 'SIDENOTE X.04-A · THICK-ORIGAMI HINGE ALLOWANCE IN REAL PANELS',
                'body': 'When folding sheets thicker than ~1 mm (such as 4–6 mm plywood or '
                        'aluminum composite), physical hinges require either living-hinge kerf '
                        'cuts along the MOUNTAIN/VALLEY DXF lines or offset rolling hinges (Chen '
                        'et al., Science 2015).'},
 'sidenote_2': {'kicker': 'SIDENOTE X.04-B · ZERO-COST DXF INSPECTION',
                'body': 'The ASCII DXF generated by make_x04.py uses pure R2000 LINE entities on '
                        'named layers, so it opens cleanly in free tools like LibreCAD, QCAD '
                        "Community Edition, Inkscape, and Blender's DXF importer."},
 'walkthrough': ['Inspect the folded Miura-ori thickened shell in the 3D WebGL2 viewer below; '
                 'toggle Cross-Section to see the constant Δz = 6.0 mm Cavalieri thickness across '
                 'the corrugations.',
                 'Click [⚡ Counterfactual Axiom-Knockout] to perturb a single sector angle away '
                 "from 180° − γ and watch Kawasaki's flat-foldability condition (∑(−1)^i α_i = 0°) "
                 'fail.',
                 'Download x04_artifact.dxf, x04_artifact.glb, and x04_artifact.3mf to test the 2D '
                 'laser/plotter pattern alongside the 3D model.'],
 't0_t1_certified': ['Deterministic generator (skills/toolchain/x04/make_x04.py) emitting '
                     'synchronized 3D (x04_artifact.glb, x04_artifact.3mf) and 2D '
                     '(x04_artifact.dxf) files.',
                     'Stdlib verifier (verify_x04_toolchain_x04_miura_ori_dxf_fabricator.py) '
                     'checking Kawasaki–Justin angle sum, Maekawa parity, Cavalieri volume '
                     '(144,000.0 mm³), DXF layer structure, and planted-defect knockout.',
                     'Small-studio fabrication SKILL.md companion with laser-cutter/CNC layer '
                     'conventions and boundary rules.'],
 't2_t3_open_horizon': ['Educational Geometry Boundary: Every file on this page is an educational '
                        'artifact; nothing is certified as load-bearing, printable, safe, or fit '
                        'for any purpose.',
                        'Future Edition 2 Extensions: Curved-crease origami ruling synthesis and '
                        'thick-panel Bennett linkage offset hinges.'],
 'sources': ['Miura, K. (1985). Method of packaging and deployment of large membranes in space. '
             'The Institute of Space and Astronautical Science Report, 618, 1–9.',
             'Schenk, M., & Guest, S. D. (2013). Geometry of Miura-folded metamaterials. '
             'Proceedings of the National Academy of Sciences, 110(9), 3276–3281. DOI '
             '10.1073/pnas.1217998110',
             'Chen, Y., Peng, R., & You, Z. (2015). Origami of thick panels. Science, 349(6246), '
             '396–400. DOI 10.1126/science.aab2870',
             "Demaine, E. D., & O'Rourke, J. (2007). Geometric Folding Algorithms: Linkages, "
             'Origami, Polyhedra. Cambridge University Press. DOI 10.1017/CBO9780511735172'],
 'act1_plain_bridge': 'Folding a flat sheet of paper into a three-dimensional accordion screen '
                      'reveals how simple geometric creases can transform a flexible surface into '
                      'a rigid, self-supporting facade. For a small one-to-five person design '
                      'studio, translating kinetic origami concepts into buildable architectural '
                      'shading screens has historically required complex parametric plug-ins and '
                      'painful manual drafting. This browser tool eliminates that barrier by '
                      'generating both three-dimensional geometric models and flat manufacturing '
                      'patterns simultaneously from pure mathematical kinematics. With a single '
                      'click, you can download all four essential digital fabrication formats for '
                      'free. Open the three-dimensional GLB mesh in Blender for real-time solar '
                      'shading studies and client walkthroughs, import the solid STEP shell into '
                      'FreeCAD for precision hinge bracket modeling, send the watertight 3MF '
                      'volume to your 3D printer for tactile scale prototypes, and load the '
                      'layered DXF file directly into QCAD, LibreCAD, or your laser cutter '
                      'software.',
 'act1_stakes': 'Small architecture studios frequently envision dynamic, high-performance shading '
                'envelopes, but commercial facade software locks kinetic folding behind expensive '
                'enterprise subscriptions and specialized engineering consultants. Consequently, '
                'modest civic centers, educational pavilions, and boutique residential projects '
                'settle for static, off-the-shelf louvers that fail to adapt to seasonal solar '
                'trajectories. This open toolkit disrupts that technological monopoly. By '
                'automating both the three-dimensional folding kinematics and the two-dimensional '
                'fabrication unfolding in a lightweight Python pipeline, a small studio can design '
                'and validate custom deployable screens without costly third-party plugins. '
                'Generating clean DXF patterns with discrete cut, mountain, and valley layers '
                'enables direct collaboration with local sheet-metal laser cutters and CNC '
                'fabricators. Independent practices gain the agency to deliver bespoke, '
                'climate-responsive kinetic facades that reduce solar heat gains by up to '
                'sixty-eight percent, competing with large architectural corporate firms while '
                'celebrating local craft.',
 'act2_analogy': 'Think of folding a large pocket road map along its traditional accordion '
                 'creases. When you pull gently on opposite corners, the entire sheet expands '
                 'outward in both length and width at the very same instant. When you push those '
                 'corners back together, every zig-zag ridge and valley tucks neatly away without '
                 'crumpling or stretching the paper. This simultaneous two-way expansion is called '
                 'auxetic behavior. The Miura-ori solar screen behaves exactly like this perfectly '
                 'engineered paper map, opening and closing smoothly under a single synchronized '
                 'motion while remaining completely rigid between folds.',
 'act2_plain_primer': 'This interactive laboratory lets you explore the mechanical elegance of '
                      'kinetic folding through two geometric sliders and a mathematical knockout '
                      'probe. The first slider adjusts the Parallelogram Sector Angle, varying the '
                      'crease slant from fifty-five to eighty-five degrees around its default '
                      "seventy-eight degrees. Changing this angle recalibrates the facade's aspect "
                      'ratio and controls how deeply the folded facets shade building interiors '
                      'during midday sun. The second slider sets Sheet Offset Thickness from two '
                      'to twelve millimeters, adding real physical substance to the panels while '
                      'calculating spatial offset reliefs that prevent adjacent faces from binding '
                      'during rotation. Finally, activating the Counterfactual Axiom-Knockout '
                      'button deliberately perturbs one sector angle away from its supplementary '
                      'pair. This perturbation violates Kawasaki’s alternating angle rule, '
                      'breaking the mathematical conditions for flat foldability. You will observe '
                      'immediate out-of-plane facet distortion, demonstrating why precision '
                      'geometry is mandatory for kinetic architectural mechanisms.',
 'act2_deepening': 'The algorithmic pipeline bridges kinematics and production by tracking both '
                   'three-dimensional coordinate transformations and planar unfolding. In 3D '
                   'space, each vertex coordinate is computed as a trigonometric function of the '
                   'sector angle γ and deployment angle θ. As θ varies, the lattice undergoes '
                   'synchronized auxetic deformation: contracting simultaneously along both '
                   'primary axes with a negative Poisson ratio ν_xy. However, translating '
                   'zero-thickness kinematics to heavy sheet metal requires Yan Chen and Zhong '
                   'You’s spatial offset technique. The generator extrudes each quadrilateral '
                   'facet along its unit normal vector, then trims adjacent edges along bisector '
                   'planes to generate clearance bevels that prevent panel collision during '
                   'folding. Simultaneously, the 2D fabricator projects the uncreased neutral '
                   'plane onto a Cartesian DXF canvas. It sorts crease lines into three '
                   'color-coded layers: continuous black cut perimeters, dashed red mountain '
                   'folds, and dotted blue valley folds, embedding CNC laser-scoring parameters '
                   'directly into the drawing header.',
 'act4_human_ai': 'Collaborating with an AI coding assistant enables a boutique architecture '
                  'studio to tailor origami kinematics without risking costly workshop mistakes. '
                  'Guided by the explicit constraints codified in SKILL.md, the architect '
                  'instructs the AI agent to adjust parameters within make_x04.py, such as tuning '
                  'sector angles for specific solar angles or altering panel thickness to match '
                  'local aluminum sheet stock. Rather than accepting generated geometries blindly, '
                  'the studio immediately runs '
                  'verify_x04_toolchain_x04_miura_ori_dxf_fabricator.py. This deterministic '
                  'verification harness checks every vertex against Kawasaki’s alternating sum, '
                  'confirms Maekawa parity |M − V| = 2 across all crease nodes, and computes the '
                  'Cavalieri divergence volume of 144,000.0 mm³ to verify watertight manifold mesh '
                  'export. The AI acts as an agile parametric draftsperson, while the Python '
                  'verifier enforces unyielding geometric rigor. This symbiosis frees small '
                  'studios to explore daring kinetic architecture with absolute certainty that '
                  'every laser-cut pattern and folded hinge will assemble cleanly on site.',
 'act4_deepening': 'The deployable origami pipeline creates an interdisciplinary bridge uniting '
                   'Euclidean geometry, kinematic mechanisms, and climate-adaptive facades. It '
                   'directly operationalizes the architectural principles of Folio A.10, which '
                   'explores the auxetic mechanical metamaterials and dynamic solar tracking of '
                   'Miura facades. The geometric rigor required to prove flat foldability connects '
                   'to Folio M.05, where AlphaGeometry 2 synthesizes automated Euclidean proofs, '
                   'illustrating how discrete angle theorems govern continuous mechanical motion. '
                   'When large folding panels transfer self-weight and wind shear through '
                   'articulating hinges to the building frame, the structural load paths invoke '
                   'Folio A.04’s British High-Tech gerberette cantilevers, balancing eccentric '
                   'facade reactions through pinned equilibrium. Furthermore, when these origami '
                   'facets are fabricated from self-shaping bi-layer wood or moisture-sensitive '
                   'veneers, the kinetic actuation transitions into Folio A.09’s Timoshenko '
                   'hygroscopic skins, where passive humidity gradients replace electric '
                   'servomotors. Across these domains, origami demonstrates that architectural '
                   'form, energy performance, and mechanical intelligence can emerge from a single '
                   'folded sheet.',
 'plain_es': 'Doblar una hoja de papel en pliegues tipo acordeón revela cómo trazos geométricos '
             'precisos transforman una lámina flexible en una celosía rígida y autoportante. Para '
             'un taller pequeño de arquitectura de una a cinco personas, llevar conceptos de '
             'origami cinético a celosías de protección solar reales requería antes complejos '
             'programas paramétricos y licencias sumamente costosas. Esta herramienta web resuelve '
             'ese reto generando tanto el modelo tridimensional cinemático como el patrón plano de '
             'fabricación mediante código abierto y gratuito. Con un solo clic puedes descargar '
             'cuatro formatos listos para producción. Abre la malla GLB en Blender para estudiar '
             'el sombreado solar en tiempo real, importa el sólido STEP en FreeCAD para diseñar '
             'herrajes y bisagras, envía el archivo 3MF a tu impresora 3D para maquetas a escala y '
             'carga el archivo DXF en QCAD o tu cortadora láser para fabricar las placas '
             'metálicas.',
 'deep_es': 'La cinemática de despliegue y la condición de plegabilidad plana de la celosía '
            'Miura-ori se rigen estrictamente por los teoremas de Kawasaki y Maekawa. Alrededor de '
            'cada nodo de grado cuatro, la suma alternada de ángulos sectoriales satisface '
            'rigurosamente ∑_{i=1}^4 (−1)^i α_i = 78° − 102° + 102° − 78° = 0°, asegurando '
            'abatimiento planar sin distorsión elástica de las facetas. La paridad topológica de '
            'los pliegues cumple |M − V| = |3 − 1| = 2, garantizando que tres pliegues en cresta '
            'intersequen un pliegue en valle. Al asignar un espesor físico h = 6 mm para corte y '
            'maquinado CNC, el volumen del sólido sigue el principio de Cavalieri y el teorema de '
            'divergencia, totalizando V = A_xy · h = 144,000.0 mm³ con característica de Euler χ = '
            '2 en una malla completamente estanca. El archivo DXF exportado segrega cortes '
            'exteriores, dobleces en cresta y valles en capas vectoriales estandarizadas para '
            'corte láser.',
 'distill_diagram': {'analogy_title': 'The Folded Pocket Road Map',
                     'analogy_sub': 'Synchronized auxetic expansion along both axes with zero '
                                    'facet binding',
                     'force_a_title': 'Parallelogram Sector Angle (γ)',
                     'force_a_sub': 'Determines facet slant, aspect ratio, and solar shading '
                                    'profile',
                     'force_b_title': 'Sheet Offset Thickness (h)',
                     'force_b_sub': 'Computes spatial relief bevels preventing rigid panel '
                                    'collisions',
                     'threshold_title': 'Kawasaki Flat Foldability (∑(-1)^i α_i = 0°)',
                     'threshold_pass': 'Watertight 1-DOF kinematic fold with Maekawa parity '
                                       '|M-V|=2',
                     'threshold_fail': 'Angle asymmetry causes out-of-plane buckling and mechanism '
                                       'lock'}}
