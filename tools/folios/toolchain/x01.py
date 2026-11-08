# -*- coding: utf-8 -*-
"""Tech & Tools · The Toolbox — Folio X.01: Zero-Build WebGL2 GLB Inspector & Byte-Level 2-Manifold Geometry Verifier."""

FOLIO = {'slug': 'x01',
 'folio_id': 'X.01',
 'tool_id': 'TOOL-CORE-1',
 'cat': 'core',
 'plate_slug': 'e10',
 'pillar_label_en': 'Core 3D Instrument · WebGL2 & Byte-Level Verification',
 'pillar_label_es': 'Instrumento 3D Central · WebGL2 y Verificación a Nivel de Bytes',
 'badge_en': 'TOOLBOX X.01 · ZERO-BUILD WEBGL2 GLB INSPECTOR + STDLIB VALIDATOR',
 'badge_es': 'HERRAMIENTA X.01 · VISOR WEBGL2 GLB SIN DEPENDENCIAS + VALIDADOR STDLIB',
 'title': 'Zero-Build WebGL2 GLB Inspector & Byte-Level 2-Manifold Geometry Verifier',
 'title_es': 'Visor WebGL2 GLB sin Dependencias y Verificador Geométrico 2-Variedad a Nivel de '
             'Bytes',
 'subtitle': 'How a 300-line zero-dependency ES module parses binary glTF 2.0 (GLB) buffers into '
             'raw WebGL2 while a Python stdlib verifier proves edge-manifold watertightness, '
             'divergence-theorem volume, and malformed-binary rejection.',
 'subtitle_es': 'Cómo un módulo ES sin dependencias analiza archivos binarios glTF 2.0 (GLB) en '
                'WebGL2 puro mientras un verificador en Python stdlib demuestra hermeticidad '
                '2-variedad, volumen por el teorema de la divergencia y rechazo de binarios '
                'corruptos.',
 'why_en': 'Most 3D viewers on the web pull in megabytes of third-party JavaScript and trust '
           'whatever binary file they are handed. For independent engineers, small architecture '
           'studios, and researchers, knowing why a 3D file is watertight—and inspecting its '
           'binary chunks, Euler characteristic, and signed volume without external '
           'dependencies—turns black-box CAD files into auditable mathematical objects.',
 'why_es': 'La mayoría de los visores 3D web descargan megabytes de librerías externas y confían '
           'ciegamente en cualquier archivo binario. Para ingenieros independientes, pequeños '
           'despachos de arquitectura e investigadores, verificar por qué una malla es hermética—e '
           'inspeccionar sus bloques binarios, característica de Euler y volumen con signo sin '
           'dependencias—convierte archivos CAD opacos en objetos matemáticos auditables.',
 'governing_law': 'V = (1/6) ∑_{f ∈ F} v_0 · (v_1 × v_2) · χ = V − E + F = 2 − 2g · 3F = 2E',
 'pass_pill_en': 'PASS · χ = 2 · V = 24,000 mm³ · 4/4 FUZZ REJECTED',
 'pass_pill_es': 'APROBADO · χ = 2 · V = 24,000 mm³ · 4/4 FUZZ RECHAZADOS',
 'generator_script': 'skills/toolchain/x01/make_x01.py',
 'verifier_script': 'skills/toolchain/x01/verify_x01_toolchain_x01_glb_inspector_validator.py',
 'skill_dir': 'skills/toolchain/x01',
 'skill_name': 'toolchain-x01-glb-inspector-validator',
 'formats': ('glb', 'step', '3mf'),
 'primary_doi': '10.1145/3596711.3596790',
 'scite_summary': 'Khronos glTF 2.0 binary transmission specification and discrete exterior '
                  'calculus / divergence-theorem polyhedral volume invariants verified offline.',
 'date_published': '2026-11-08',
 'date_redated': '2026-11-08',
 'current_edition': 'REV 1.0',
 'reading_time': '22 MIN READ',
 'small_studio_kit_en': 'Zero-Cost Studio Workflow (Blender 4.2 + FreeCAD 1.0 + Python 3 stdlib): '
                        'Run make_x01.py to emit x01_artifact.glb, x01_artifact.step, and '
                        'x01_artifact.3mf; audit any client or subcontractor .glb mesh for '
                        'non-manifold edges, inverted normals, or chunk corruption in < 0.05s '
                        'before opening a slicer or BIM model.',
 'small_studio_kit_es': 'Flujo de Estudio sin Costo (Blender 4.2 + FreeCAD 1.0 + Python 3 stdlib): '
                        'Ejecuta make_x01.py para generar x01_artifact.glb, x01_artifact.step y '
                        'x01_artifact.3mf; audita cualquier malla .glb en busca de bordes '
                        'no-variedad, normales invertidas o bloques corruptos en < 0.05s antes de '
                        'enviarla a corte o BIM.',
 'companion_folios': [('engineering',
                       'e10',
                       'Folio E.10',
                       '3D Concrete Printing Thixotropy & Suiker Buckling'),
                      ('math',
                       'm10',
                       'Folio M.10',
                       'Persistent Homology Barcodes & Topological Data Analysis'),
                      ('engineering',
                       'e11',
                       'Folio E.11',
                       'SIMP Topology Optimization & Inerter Dampers'),
                      ('architecture',
                       'a11',
                       'Folio A.11',
                       '3D Polyhedral Graphic Statics & Stone Vaults')],
 'external_links': [('Khronos glTF 2.0 Specification (ISO/IEC 12113)',
                     'https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html'),
                    ('elalish/manifold (Apache-2.0 CSG Kernel)',
                     'https://github.com/elalish/manifold'),
                    ('mikedh/trimesh (MIT Mesh Inspector)', 'https://github.com/mikedh/trimesh')],
 'act1_dropcap': 'In the quiet study of the Prussian Academy in Berlin during the winter of 1758, '
                 'Leonhard Euler spent long evenings examining hand-carved wooden blocks, crystal '
                 'prisms, and geometric solids. He was fascinated by a simple physical truth that '
                 'master masons, carpenters, and stonecutters had navigated for centuries: no '
                 'matter how you carve, bevel, or shape a closed solid, its corners, seams, and '
                 'outer surfaces remain bound together in an unbroken balance. Two and a half '
                 'centuries later, software engineers gathered under the Khronos Group to solve '
                 'that very same craft dilemma for our digital world. As three-dimensional models '
                 'moved from proprietary desktop workstations onto open web browsers, digital '
                 'objects kept arriving broken, inside out, or missing entire panels. By codifying '
                 'the binary glTF transmission standard, those modern architects established an '
                 'open digital container where every corner, seam, and triangular face could '
                 'travel across the internet intact, honoring the timeless geometric balance Euler '
                 'first uncovered by candlelight.',
 'act1_body': 'For decades, computer graphics suffered under loose, disconnected collections of '
              'triangles known colloquially as polygon soup. Early formats like the 1987 '
              'stereolithography standard stored lists of three-dimensional coordinates without '
              'indexing shared vertices, recording explicit units, or preserving topological '
              'relationships. When complex assemblies moved between competing modeling suites, '
              'files ballooned in size and frequently corrupted boundary edges. The release of the '
              'Khronos glTF 2.0 specification (DOI: 10.1145/3230744) — alongside its binary '
              'packaging format, GLB — fundamentally transformed this landscape. A binary GLB '
              'packages everything into a streamlined container beginning with a compact '
              'twelve-byte header defining the format magic number, version, and total file '
              'length. Immediately following this header, structured JSON metadata defines scene '
              'hierarchies and data types, while raw binary buffers store vertex positions, normal '
              'vectors, and indices in tightly packed byte arrays. In Folio X.01, our '
              'zero-dependency browser viewer maps these contiguous buffers directly into raw '
              'WebGL2 graphics memory. This architectural directness eliminates bloated '
              'intermediate runtimes and enables independent practitioners to audit file offsets, '
              'vertex arrays, and geometric closure with absolute byte-level transparency.',
 'pullquote': 'A 3D binary should never be trusted merely because it renders; it is trustworthy '
              'only when its chunk offsets, half-edge pairing, Euler characteristic, and signed '
              'divergence volume pass a deterministic check.',
 'chronology': [('1752',
                 'Leonhard Euler formulates the polyhedral invariant V − E + F = 2 for convex and '
                 'genus-0 closed polyhedra.'),
                ('1813–1826',
                 'Carl Friedrich Gauss and Mikhail Ostrogradsky establish the divergence theorem, '
                 'enabling exact polyhedral volume integration from boundary surface triangles.'),
                ('1991',
                 'Brian Mirtich and John Canny formalize fast, exact polyhedral mass-property and '
                 'signed-volume integration from surface triangulations.'),
                ('2017–2022',
                 'The Khronos Group ratifies glTF 2.0 and binary GLB (ISO/IEC 12113:2022) as the '
                 "royalty-free 'JPEG of 3D' transmission standard."),
                ('2026',
                 'Informatico.ai ships X.01: a zero-dependency WebGL2 GLB inspector paired with a '
                 'Python 3 stdlib byte-level manifold verifier and 4-case fuzz harness.')],
 'act2_intuition': 'How does a mathematical verifier prove that a faceted boundary surface '
                   'completely seals an enclosed volume? The governing insight rests on the '
                   'Gauss–Ostrogradsky divergence theorem, which connects the behavior of a vector '
                   'field across an interior volume to its flux through the boundary surface. When '
                   'we choose the simple vector field F(x) = x, its divergence equals the spatial '
                   'dimension: ∇ · x = 3. Consequently, the triple volume integral over the '
                   'interior domain Ω simplifies exactly to one-third of the surface flux integral '
                   'over the boundary ∂Ω. For a polyhedral surface composed of planar triangular '
                   'facets with vertices (v_0, v_1, v_2), this boundary integral breaks down into '
                   'a summation of signed tetrahedra anchored at the coordinate origin: V = (1/6) '
                   '∑ v_0 · (v_1 × v_2). In parallel, topological closure demands that every '
                   'directed half-edge (u, v) possesses a unique reverse twin (v, u), guaranteeing '
                   'the half-edge identity 3F = 2E. When all triangular faces circulate '
                   'consistently counterclockwise, the Euler–Poincaré characteristic yields χ = V '
                   '− E + F = 2, confirming a closed, genus-zero 2-manifold without relying on '
                   'external CAD kernels.',
 'sliders': [{'id': 'tp-tool-s0',
              'label': 'Calibration Prism Length L_x',
              'min': 20,
              'max': 80,
              'step': 2,
              'value': 40,
              'unit': ' mm'},
             {'id': 'tp-tool-s1',
              'label': 'Calibration Prism Height L_z',
              'min': 10,
              'max': 40,
              'step': 2,
              'value': 20,
              'unit': ' mm'}],
 'readouts': [{'label': 'GLB Binary Header & Chunks', 'value': 'glTF v2 · 1,708 B (PASS)'},
              {'label': '2-Manifold Topology (V, E, F)', 'value': 'V=14, E=36, F=24 · χ=2'},
              {'label': 'Divergence Signed Volume', 'value': '24,000.0 mm³ (err = 0.00%)'},
              {'label': 'Fuzz & Knockout Gate', 'value': '4/4 Fuzz + Defect REJECTED'}],
 'steps': ['Stage 1: Khronos GLB Binary Header & Chunk Bounds Audit — Unpack the 12-byte header '
           '(<3I: magic 0x46546C67, version 2, total_len) and verify that Chunk 0 (JSON) and Chunk '
           '1 (BIN) byte offsets and accessor bufferViews lie strictly within the file.',
           'Stage 2: Directed Half-Edge Manifold Closure (3F = 2E) — Build the directed half-edge '
           'table {(u, v)} across all triangles and assert zero degenerate triangles, zero '
           'duplicate half-edges, and 100% reverse half-edge pairing (v, u) ∈ E.',
           'Stage 3: Euler–Poincaré Characteristic & Divergence-Theorem Volume — Compute χ = V − E '
           '+ F = 2 − 2g and integrate V_mesh = (1/6) ∑ v_0 · (v_1 × v_2) to certify exact '
           'agreement with the analytical solid volume (24,000.0 mm³).',
           'Stage 4: Malformed-Binary Fuzz Suite & Planted-Defect Knockout — Run the parser and '
           'topological verifier against 4 malformed GLB fuzz files (truncated header, chunk OOB, '
           'vertex index OOB, flipped normal) and assert that every defect fails.'],
 'rules': ['Binary Chunk Containment Invariant: Every glTF bufferView byteOffset + byteLength must '
           'satisfy 0 ≤ start ≤ end ≤ BIN_byteLength, and every triangle index must be strictly '
           'less than POSITION.count.',
           'Watertight 2-Manifold Closure Invariant: Every directed half-edge (u, v) must appear '
           'exactly once and have a unique reverse half-edge (v, u), enforcing 3F = 2E and χ = V − '
           'E + F = 2.',
           'Planted-Defect Sensitivity Invariant: Flipping the winding of Triangle 0 ((i_0, i_1, '
           'i_2) → (i_0, i_2, i_1)) must immediately trigger duplicate/unpaired half-edge failure '
           'and alter the divergence volume.'],
 'sidenote_1': {'kicker': 'SIDENOTE X.01-A · WHY ZERO THIRD-PARTY WEBGL RUNTIME MATTERS',
                'body': 'Pulling a 600 KB external 3D library into a scientific monograph obscures '
                        'how buffers map to GPU attributes and expands the supply-chain surface. '
                        'Our glb-viewer.mjs parses the strict static-mesh GLB subset in ~280 lines '
                        'of native ES module code.'},
 'sidenote_2': {'kicker': 'SIDENOTE X.01-B · PLANTED-DEFECT FALSIFICATION',
                'body': 'A verifier that always prints PASS is useless. Every verify_x*.py script '
                        'in the Toolbox runs the valid artifact check first and then mutates a '
                        'face normal in memory to prove the failure path is live.'},
 'walkthrough': ['Orbit, zoom, and toggle Wireframe or Cross-Section on the live 3D WebGL2 canvas '
                 'below to inspect the 14-vertex, 24-triangle calibration manifold.',
                 'Scrub Calibration Prism Length L_x and Height L_z (or click [⚡ Counterfactual '
                 'Axiom-Knockout]) to see how a single flipped triangle normal breaks 3F = 2E '
                 'half-edge closure and corrupts the divergence-theorem volume.',
                 'Download x01_artifact.glb, x01_artifact.step, or x01_artifact.3mf and run python '
                 'skills/toolchain/x01/verify_x01_toolchain_x01_glb_inspector_validator.py '
                 'locally.'],
 't0_t1_certified': ['Zero-dependency WebGL2 GLB loader and interactive orbit/wireframe/clipping '
                     'inspector in src/research/modules/glb-viewer.mjs.',
                     'Deterministic Python stdlib generator (skills/toolchain/x01/make_x01.py) '
                     'emitting x01_artifact.glb, x01_artifact.step, x01_artifact.3mf, '
                     'manifest.json, and 4 malformed fuzz fixtures.',
                     'Byte-level stdlib verifier '
                     '(verify_x01_toolchain_x01_glb_inspector_validator.py) certifying χ = 2, V = '
                     '24,000.0 mm³, SHA-256 manifest match, 4/4 fuzz rejection, and planted-defect '
                     'knockout.'],
 't2_t3_open_horizon': ['Educational Geometry Boundary: Every file on this page is an educational '
                        'artifact; nothing is certified as load-bearing, printable, safe, or fit '
                        'for any purpose.',
                        'Future Edition 2 Extensions: Skeletal animation tracks, Draco/Meshopt '
                        'compressed buffer views, and KTX2 GPU texture transcoding remain outside '
                        'the v1 static-mesh subset.'],
 'sources': ['Khronos Group. (2022). glTF 2.0 Specification / ISO/IEC 12113:2022 Information '
             'technology — Runtime 3D asset delivery format. '
             'https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html',
             'Mirtich, B. (1996). Fast and accurate computation of polyhedral mass properties. '
             'Journal of Graphics Tools, 1(2), 31–50. DOI 10.1080/10867651.1996.10487458',
             'Crane, K., de Goes, F., Desbrun, M., & Schröder, P. (2013). Digital geometry '
             'processing with discrete exterior calculus. ACM SIGGRAPH 2013 Courses. DOI '
             '10.1145/2504435.2504442',
             'Lalish, E. (2023–2026). Manifold: Geometry library for topological robustness '
             '(Apache-2.0). https://github.com/elalish/manifold'],
 'act1_plain_bridge': 'Think of a digital 3D model like a hollow balloon made of '
                      'tiny flat triangles. To hold air, every single edge must be stitched neatly '
                      'between exactly two neighboring patches. If a single seam stays open, or if '
                      'one patch faces backward, the balloon leaks. In the computer world, we call '
                      'an unbroken shell a watertight mesh. When you export a 3D file from design '
                      'software, things often go wrong quietly. Programs write numbers slightly '
                      'differently, round off corners, or skip hidden seams. You might not see any '
                      'flaws on your screen, but downstream tools fail immediately. That is why we '
                      'built this free, open instrument. Right here in your web browser, our '
                      'lightweight tool opens binary 3D files directly with zero extra software. '
                      'You can spin the shape, inspect internal cross sections, and see every '
                      'triangle. With one click, you can download verified models and running '
                      'Python scripts to check your own files in seconds.',
 'act1_stakes': 'For an independent practitioner, a solo engineer, or a boutique five-person '
                'design studio, geometry errors carry serious economic consequences. When an '
                'automated geometry generator or an overseas modeling contractor exports an asset '
                'with a flipped normal or an unstitched seam, the error often stays completely '
                'invisible during casual viewport rendering. The defect reveals itself only when a '
                'downstream numerical simulation crashes, a toolpath generator halts midway '
                'through processing, or a physical mock-up fails during fitting. Commercial repair '
                'packages charge thousands of dollars in annual seat licenses just to diagnose '
                'these boundary defects. By putting mathematical verification directly into the '
                'hands of independent creators through open Python scripts and zero-cost web '
                'standards, we remove that expensive barrier. A fast, scriptable audit verifies '
                'edge manifoldness, calculates signed volume, and flags malformed chunks in '
                'milliseconds. This empowers small studios to catch geometric anomalies before '
                'physical prototypes are cut, operating with the same rigor as well-funded '
                'aerospace teams.',
 'act2_analogy': 'Picture stitching hexagonal and pentagonal leather patches to make a classic '
                 'leather soccer ball. For the ball to hold air, every single seam must join '
                 'exactly two neighboring leather panels—never leaving an unstitched gap, and '
                 'never allowing three patches to collide along a single seam. Furthermore, every '
                 'panel must be oriented smooth grain outward and suede facing in. If a '
                 'leatherworker accidentally stitches even one patch inside out, the smooth '
                 'spherical contour dimples backward, the seam balance breaks, and the ball '
                 'collapses as soon as air pumps in under pressure.',
 'act2_plain_primer': 'Before inspecting any geometric equations, look at the interactive controls '
                      'in our Act III workbench. The first slider adjusts the Calibration Prism '
                      'Length, stretching or shortening the rectangular body along its primary '
                      'axis. As you slide it, watch how the calculated internal volume updates '
                      'smoothly while the outer shell remains perfectly sealed. The second slider '
                      'controls the Calibration Prism Height, raising or lowering the roof '
                      'elevation of the prism. Adjusting both sliders demonstrates that whether '
                      'your geometry is wide, tall, or compact, every corner connects cleanly and '
                      'every surface normal points outward. Finally, test the Planted-Defect '
                      'Knockout button. Clicking this control intentionally flips the orientation '
                      'of a single triangle in the mesh, turning its normal vector backward. '
                      'Instantly, the edge-pairing audit turns red, the calculated signed volume '
                      'drops below the true physical space, and the verifier catches the breach. '
                      'It is a live demonstration that our audit genuinely fails when an error '
                      'occurs.',
 'act2_deepening': 'Under the hood of our Python standard library verifier, topological validation '
                   'operates without floating-point heuristics or complex external dependencies. '
                   'The algorithm begins by converting the triangular face index table into a '
                   'comprehensive dictionary of directed half-edges. Each triangle defined by '
                   'vertices (i, j, k) generates three ordered directed tuples: (i, j), (j, k), '
                   'and (k, i). For an orientable 2-manifold surface with zero boundary seams, '
                   'every directed half-edge (u, v) must have exactly one corresponding twin '
                   'half-edge (v, u) originating from an adjacent face. When traversing the entire '
                   'mesh, the presence of any unpaired directed half-edge immediately signals a '
                   'boundary puncture or open hole in the shell. Conversely, if a directed '
                   'half-edge appears more than once, non-manifold edge sharing or '
                   'self-intersecting t-junctions are present. Once mutual twin cancellation '
                   'certifies topological closure, the verifier computes the signed scalar triple '
                   'product for each triangle. If any individual face has its winding order '
                   'reversed, its local volume contribution flips from positive to negative, '
                   'immediately betraying the defect.',
 'act4_human_ai': 'As generative artificial intelligence transforms design engineering, language '
                  'models can write geometry generation scripts in seconds. However, deep neural '
                  'networks possess no innate spatial grounding; they frequently produce meshes '
                  'with pinched vertices, overlapping triangles, and flipped surface orientations '
                  'that appear plausible on screen but collapse during downstream computation. The '
                  'workflow embodied in Folio X.01 establishes a balanced human-agent partnership. '
                  'The human designer defines high-level design intent, functional clearances, and '
                  'material aesthetics. The artificial intelligence agent assists by rapidly '
                  'generating candidate scripts using make_x01.py guided by portable SKILL.md '
                  'conventions. Crucially, neither the human nor the AI is trusted on blind faith. '
                  'Before any generated file enters a project archive, our deterministic verifier '
                  'runs offline in Python standard library. It parses the binary GLB header, '
                  'validates every buffer boundary, proves half-edge manifold closure, and checks '
                  'signed volume against analytical ground truth. If the generative model '
                  'hallucinates an invalid facet or drops a coordinate, the verifier halts '
                  'execution and pinpoints the defect byte by byte, keeping the human firmly in '
                  'control.',
 'act4_deepening': 'The topological principles governing Folio X.01 ripple across all four '
                   'analytical disciplines on Informatico.ai. In the Architecture track, '
                   'polyhedral graphic statics (Folio A.11) relies on reciprocal thrust polyhedra '
                   'where every reciprocal cell must form a watertight closed polyhedron to '
                   'guarantee static equilibrium under self-weight. In the Engineering pillar, '
                   'material deposition path planning for additive concrete construction (Folio '
                   'E.10) requires continuous bounding manifolds to calculate layer slicing '
                   'without dry-run nozzle collisions. In the Mathematics pillar, persistent '
                   'homology and topological data analysis (Folio M.10) extract multi-scale '
                   'filtration barcodes from simplicial complexes, treating Euler characteristic '
                   'invariants as topological foundations. Across Physics and Continuum Mechanics, '
                   'finite-element formulations for structural topology optimization (Folio E.11) '
                   'discretize void-solid boundaries where divergence-theorem mass conservation '
                   'prevents numerical singularities during density filtering. By mastering the '
                   'fundamentals of half-edge connectivity and byte-level buffer validation in '
                   'this core instrument, practitioners acquire the essential mathematical '
                   'foundation needed to explore advanced computational monographs across '
                   'contemporary architecture, engineering mechanics, and theoretical physical '
                   'sciences.',
 'plain_es': 'Para entender una malla tridimensional de forma sencilla, imaginen un balón de '
             'fútbol armado con parches de cuero cosidos a mano. Para que el balón retenga el aire '
             'y no se desinfle, cada costura debe unir exactamente dos paneles adyacentes, sin '
             'dejar ningún orificio abierto y sin amontonar telas. Además, todos los parches deben '
             'mirar hacia afuera con el lado liso al exterior. En el diseño digital ocurre '
             'exactamente lo mismo: un modelo tridimensional está compuesto por pequeños '
             'triángulos planos que deben formar una cáscara perfectamente sellada. Con '
             'frecuencia, cuando exportamos archivos entre diferentes programas de diseño, algunas '
             'caras se voltean hacia adentro o quedan pequeñas grietas invisibles en la pantalla. '
             'Este visor gratuito en el navegador web les permite abrir y girar piezas en tres '
             'dimensiones directamente, inspeccionar cortes transversales y comprobar que cada '
             'triángulo esté bien colocado. Con un solo clic, cualquier estudiante, diseñador o '
             'taller independiente puede descargar modelos verificados y rutinas en Python para '
             'revisar sus geometrías sin gastar en licencias costosas.',
 'deep_es': 'La integridad matemática de una superficie poligonal descansa en la rigurosa '
            'equivalencia entre la topología discreta y el análisis vectorial clásico. Mediante el '
            'teorema de divergencia de Gauss-Ostrogradsky, el volumen encerrado por una variedad '
            'bidimensional cerrada se calcula exactamente a través de la suma de productos triples '
            'escalares sobre sus triángulos frontera. Para que esta formulación conserve validez, '
            'cada arista dirigida de la malla debe cancelarse con su semi-arista gemela orientada '
            'en sentido inverso, garantizando la condición de variedad bidimensional y preservando '
            'la característica de Euler igual a dos en sólidos de género cero. Cuando un modelo se '
            'transfiere en formato binario GLB, nuestro módulo analiza la cabecera de doce bytes y '
            'valida los límites de los bloques de memoria sin requerir dependencias externas de '
            'JavaScript. Si una sola cara invierte su orientación, el signo de su contribución '
            'volumétrica cambia inmediatamente y el emparejamiento de semi-aristas colapsa, '
            'permitiendo a ingenieros y despachos independientes certificar geometrías con '
            'absoluta precisión numérica.',
 'distill_diagram': {'analogy_title': 'The Stitched Leather Ball & Seams',
                     'analogy_sub': 'Every edge must pair exactly two faces to retain airtight '
                                    'volume.',
                     'force_a_title': 'Directed Half-Edge Pairing (3F = 2E)',
                     'force_a_sub': 'Every directed edge must find its exact reversed twin '
                                    'half-edge.',
                     'force_b_title': 'Signed Divergence Volume V(Ω)',
                     'force_b_sub': 'Sum of tetrahedra determinants proves watertight manifold '
                                    'closure.',
                     'threshold_title': 'Euler–Poincaré Characteristic (χ = 2)',
                     'threshold_pass': 'Watertight 2-Manifold: χ = 2, paired half-edges, exact '
                                       'volume.',
                     'threshold_fail': 'Unsealed Boundary / Inverted Normal: χ ≠ 2, volume '
                                       'corrupted.'}}
