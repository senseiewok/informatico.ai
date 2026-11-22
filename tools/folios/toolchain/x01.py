# -*- coding: utf-8 -*-
"""Tech & Tools · The Toolbox — Folio X.01: Zero-Build WebGL2 GLB Inspector & Byte-Level 2-Manifold Geometry Verifier."""

FOLIO = {
    'slug': 'x01',
    'folio_id': 'X.01',
    'tool_id': 'TOOL-CORE-1',
    'cat': 'core',
    'plate_slug': 'x01',
    'pillar_label_en': 'Core 3D Instrument · WebGL2 & Byte-Level Verification',
    'pillar_label_es': 'Instrumento 3D Central · WebGL2 y Verificación a Nivel de Bytes',
    'badge_en': 'TOOLBOX X.01 · ZERO-BUILD WEBGL2 GLB INSPECTOR + STDLIB VALIDATOR',
    'badge_es': 'HERRAMIENTA X.01 · VISOR WEBGL2 GLB SIN DEPENDENCIAS + VALIDADOR STDLIB',
    'title': 'Zero-Build WebGL2 GLB Inspector & Byte-Level 2-Manifold Geometry Verifier',
    'title_es': 'Visor WebGL2 GLB sin Dependencias y Verificador Geométrico 2-Variedad a Nivel de Bytes',
    'subtitle': (
        'How a zero-dependency ES module parses binary glTF 2.0 (GLB) chunks into raw WebGL2 while '
        'a Python stdlib verifier checks half-edge watertightness, divergence-theorem volume, and '
        'malformed-binary rejection across GLB, STEP Part-21, and 3MF.'
    ),
    'subtitle_es': (
        'Cómo un módulo ES sin dependencias analiza bloques binarios glTF 2.0 (GLB) en WebGL2 puro '
        'mientras un verificador en Python stdlib comprueba hermeticidad de semi-aristas, volumen '
        'por divergencia y rechazo de binarios corruptos en GLB, STEP Parte 21 y 3MF.'
    ),
    'why_en': (
        'Most web 3D viewers load large third-party scripts and render whatever binary file arrives. '
        'For independent engineers, small architecture studios, and researchers, checking binary chunk '
        'bounds, half-edge pairing, Euler characteristic, and signed volume without external packages '
        'turns opaque CAD exports into inspectable geometric records.'
    ),
    'why_es': (
        'La mayoría de los visores 3D web cargan librerías pesadas y dibujan cualquier archivo binario '
        'sin revisarlo. Para ingenieros independientes, pequeños despachos de arquitectura e '
        'investigadores, auditar bloques binarios, semi-aristas, característica de Euler y volumen con '
        'signo sin dependencias convierte exportaciones CAD opacas en registros geométricos auditables.'
    ),
    'governing_law': 'V = (1/6) ∑_{f ∈ F} v_0 · (v_1 × v_2) · χ = V − E + F = 2 − 2g · 3F = 2E',
    'pass_pill_en': 'PASS · χ = 2 · V = 24,000 mm³ · 4/4 FUZZ REJECTED',
    'pass_pill_es': 'APROBADO · χ = 2 · V = 24,000 mm³ · 4/4 FUZZ RECHAZADOS',
    'generator_script': 'skills/toolchain/x01/make_x01.py',
    'verifier_script': 'skills/toolchain/x01/verify_x01_toolchain_x01_glb_inspector_validator.py',
    'skill_dir': 'skills/toolchain/x01',
    'skill_name': 'toolchain-x01-glb-inspector-validator',
    'formats': ('glb', 'step', '3mf'),
    'primary_doi': '10.1080/10867651.1996.10487458',
    'scite_summary': (
        'Khronos glTF 2.0 (ISO/IEC 12113:2022) binary chunk layout, Mirtich (1996) polyhedral '
        'divergence-volume integration, and Crane et al. (2013) discrete 2-manifold invariants '
        'checked offline.'
    ),
    'date_published': '2026-11-08',
    'date_redated': '2026-11-08',
    'current_edition': 'REV 1.0',
    'reading_time': '22 MIN READ',
    'small_studio_kit_en': (
        'Zero-Cost Studio Workflow (Blender 4.2 + FreeCAD 1.0 + Python 3 stdlib): Run make_x01.py to '
        'emit x01_artifact.glb (2,716 B), faceted Part-21 x01_artifact.step (10,356 B), and '
        'x01_artifact.3mf (1,672 B); run verify_x01 to check non-manifold seams, flipped normals, '
        'and chunk bounds in < 0.05s before opening a slicer or BIM model.'
    ),
    'small_studio_kit_es': (
        'Flujo de Estudio sin Costo (Blender 4.2 + FreeCAD 1.0 + Python 3 stdlib): Ejecuten '
        'make_x01.py para generar x01_artifact.glb (2,716 B), x01_artifact.step facetado Parte 21 '
        '(10,356 B) y x01_artifact.3mf (1,672 B); auditen cualquier malla .glb en busca de bordes '
        'no-variedad, normales invertidas o bloques corruptos en < 0.05s antes de enviarla a corte o BIM.'
    ),
    'companion_folios': [
        ('engineering', 'e10', 'Folio E.10', '3D Concrete Printing Thixotropy & Suiker Buckling'),
        ('math', 'm10', 'Folio M.10', 'Persistent Homology Barcodes & Topological Data Analysis'),
        ('engineering', 'e11', 'Folio E.11', 'SIMP Topology Optimization & Inerter Dampers'),
        ('architecture', 'a11', 'Folio A.11', '3D Polyhedral Graphic Statics & Stone Vaults'),
    ],
    'external_links': [
        (
            'Khronos glTF 2.0 Specification (ISO/IEC 12113:2022)',
            'https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html',
        ),
        ('elalish/manifold (Apache-2.0 CSG Kernel)', 'https://github.com/elalish/manifold'),
        ('mikedh/trimesh (MIT Mesh Inspector)', 'https://github.com/mikedh/trimesh'),
    ],
    'act1_dropcap': (
        'At the Prussian Academy in Berlin in 1750, Leonhard Euler studied hand-carved wooden blocks, '
        'crystal prisms, and faceted stone models by lamplight. Master masons and joiners had worked '
        'with these shapes for centuries, yet nobody had named the numerical balance tying a solid '
        'together. Euler noticed that however a closed block is beveled or subdivided, its corners, '
        'seams, and flat faces stay locked in a constant tally, a memoir printed by the Saint '
        'Petersburg Academy in 1758. Two and a half centuries later, graphics engineers met under the '
        'Khronos consortium to address a cognate workshop problem on the web. As three-dimensional '
        'models moved from desktop workstations to browsers, files arrived split at the seams, '
        'turned inside out, or truncated mid-transfer. Their open binary container meant every corner, '
        'edge, and triangular facet could travel intact across machines while honoring Euler’s '
        'eighteenth-century count.'
    ),
    'act1_plain_bridge': (
        'Think of a digital three-dimensional model like a hollow paper lantern built from flat '
        'triangles. To enclose space cleanly, each edge must join two neighboring triangles, because '
        'an open seam or a backward-facing patch breaks the shell. Engineers call such a closed '
        'surface a watertight mesh. When design programs export a model, subtle mismatches often '
        'appear quietly. Exporters round coordinates differently, drop shared seams, or flip a '
        'triangle inward, so a part might look fine on screen while a slicer or solver rejects it. '
        'Right on this page, a lightweight browser viewer opens binary mesh files directly without '
        'external libraries. You can rotate the calibration prism, slice across its interior, and '
        'inspect every facet. With one click, you can also download the neutral files and a Python '
        'script that checks your own exports in milliseconds.'
    ),
    'act1_body': (
        'Early exchange formats such as 1987 stereolithography files stored unindexed triangle '
        'coordinates—colloquially called polygon soup—without shared vertex indices, topological '
        'adjacency tables, or explicit linear units. On triangulated 2-manifolds, discrete '
        'differential-geometry operators depend on consistent edge sharing and outward face winding '
        '(Meyer, Desbrun, Schröder, & Barr, 2003, DOI 10.1007/978-3-662-05105-4_2). The Khronos glTF '
        '2.0 specification (ISO/IEC 12113:2022) and its binary GLB container address transport '
        'fragility through a twelve-byte little-endian header followed by four-byte-aligned JSON and '
        'BIN chunks. While glTF stores unitless linear coordinates, our committed 2,716-byte '
        'x01_artifact.glb records millimeter provenance in asset.extras alongside a 1,672-byte 3MF '
        'archive and a 10,356-byte ISO 10303-21 faceted POLY_LOOP B-rep sketch carrying an AP242 '
        'header (compare full analytic EDGE_LOOP STEP AP242 exchange in Feeney, Frechette, & '
        'Srinivasan, 2015, DOI 10.1115/1.4029050). In src/modules/glb-viewer.mjs, '
        'parseGlbBuffer checks chunk alignment, bufferView and accessor spans, finite floats, and '
        'vertex index bounds before uploading typed arrays directly into WebGL2.'
    ),
    'act1_stakes': (
        'For a solo engineer or a five-person architecture studio, silent mesh defects waste both '
        'bench time and workshop material. When an external contractor or script exports an asset '
        'with a flipped triangle normal or an unpaired boundary seam, smooth viewport shading can '
        'hide the flaw until a finite-element simulation diverges, a CAM toolpath halts, or a slicer '
        'bridges across an unintended void. Commercial mesh-repair seats charge steep annual fees to '
        'diagnose those boundary errors. Pairing neutral open standards with a readable Python '
        'standard-library verifier removes that license barrier. Running verify_x01 checks GLB chunk '
        'alignment, all four bufferViews, single-shell connectivity, signed volume, and cross-format '
        'parity across GLB, faceted Part-21 STEP, and 3MF in under fifty milliseconds, catching '
        'corrupt exports before a studio cuts a physical prototype.'
    ),
    'pullquote': (
        'A 3D binary should not be trusted merely because it renders; it earns trust when its chunk '
        'bounds, directed half-edge pairing, Euler characteristic, and signed divergence volume pass '
        'an independent check.'
    ),
    'chronology': [
        (
            '1750–1758',
            'Leonhard Euler writes his Berlin memoir on polyhedra and publishes the vertex-edge-face '
            'balance for closed genus-zero solids in the St. Petersburg Academy commentaries.',
        ),
        (
            '1813–1826',
            'Carl Friedrich Gauss and Mikhail Ostrogradsky formulate the divergence theorem, reducing '
            'three-dimensional volume integrals to boundary flux.',
        ),
        (
            '1996',
            'Brian Mirtich publishes fast polyhedral mass-property and signed-volume integration from '
            'boundary surface triangles (DOI 10.1080/10867651.1996.10487458).',
        ),
        (
            '2013–2022',
            'Keenan Crane et al. formalize discrete exterior calculus on meshes (DOI '
            '10.1145/2504435.2504442) and Khronos ratifies glTF 2.0 / GLB as ISO/IEC 12113:2022.',
        ),
        (
            '2026',
            'Informatico.ai ships X.01: a zero-dependency WebGL2 GLB inspector paired with a stdlib '
            'verifier across GLB, Part-21 STEP, and 3MF plus four malformed fuzz fixtures.',
        ),
    ],
    'act2_analogy': (
        'Picture stitching leather panels to make a classic soccer ball. Every seam joins two '
        'neighboring patches, with no open gap and no third flap crowded into the same stitch line, '
        'and every panel faces smooth grain outward. If one patch is sewn suede-side out, its seam '
        'directions clash with all three neighbors. The analogy stops at elasticity and self-contact: '
        'inflated leather stretches into curved domes and leaks air, whereas mesh facets stay rigid '
        'flat triangles with no internal pressure, and half-edge pairing checks combinatorial closure '
        'without ruling out geometric self-intersection.'
    ),
    'act2_plain_primer': (
        'In the Act III workbench below, two sliders and one mode switch let you test these invariants '
        'directly. Calibration Prism Length stretches or shortens the forty-millimeter prism along its '
        'first axis while keeping all twenty-four triangles sealed. Calibration Prism Height raises or '
        'lowers the twenty-millimeter roof elevation and scales the enclosed volume proportionally. '
        'Next, click the Planted-Defect / Boundary Knockout button. That mode flips Triangle 0 on the '
        'bottom face, creating three duplicate and three unpaired directed half-edges and dropping '
        'signed volume from 24,000.0 to 22,000.0 cubic millimeters while the undirected vertex-edge-face '
        'count stays at two.'
    ),
    'act2_intuition': (
        'Why can a boundary mesh reveal its enclosed volume without voxelizing the interior? Under '
        'the Gauss–Ostrogradsky divergence theorem, the position field F(x) = x has constant '
        'divergence ∇ · x = 3, so the interior integral equals one-third of the outward surface flux '
        '(Mirtich, 1996, DOI 10.1080/10867651.1996.10487458). Across planar triangles (v_0, v_1, v_2), '
        'that flux reduces to a sum of signed origin-anchored tetrahedra, V = (1/6) ∑ v_0 · (v_1 × '
        'v_2). Combinatorially, an orientable boundaryless 2-manifold requires every directed '
        'half-edge (u, v) to pair with one reverse twin (v, u), enforcing 3F = 2E and boundary-of-'
        'boundary cancellation ∂² = 0 (Crane, de Goes, Desbrun, & Schröder, 2013, DOI '
        '10.1145/2504435.2504442). On a single connected shell (β_0 = 1), V − E + F = 2 identifies '
        'genus zero.'
    ),
    'act2_deepening': (
        'Inside tools/toolchain_uga.py and tools/toolchain_x01_checks.py, byte-level verification '
        'proceeds without external CAD libraries. For x01_artifact.glb (2,716 bytes), the parser '
        'checks the twelve-byte header, four-byte alignment of the 1,896-byte JSON and 792-byte BIN '
        'chunks, all four contiguous bufferViews ([0:168] POSITION, [168:336] unit NORMAL, [336:504] '
        'COLOR_0, [504:792] uint32 indices), and finite IEEE-754 floats. It then builds the directed '
        'half-edge map across 14 vertices, 36 edges, and 24 faces, checks dual face-edge shell '
        'connectivity and single-umbrella vertex links (β_0 = 1), and cross-checks that '
        'x01_artifact.step (after stripping nested comments and string literals) and '
        'x01_artifact.3mf (with identity build transform) reconstruct the congruent 24,000.0 mm³ '
        'manifold. Flipping Triangle 0 reverses one 1,000.0 mm³ signed tetrahedron from +1,000.0 '
        'to −1,000.0 mm³, lowering total signed volume to 22,000.0 mm³.'
    ),
    'sliders': [
        {
            'id': 'tp-tool-s0',
            'label': 'Calibration Prism Length',
            'min': 20,
            'max': 80,
            'step': 2,
            'value': 40,
            'unit': ' mm',
        },
        {
            'id': 'tp-tool-s1',
            'label': 'Calibration Prism Height',
            'min': 10,
            'max': 40,
            'step': 2,
            'value': 20,
            'unit': ' mm',
        },
    ],
    'readouts': [
        {'label': 'GLB Binary Header & Chunks', 'value': 'glTF v2 · 2,716 B (PASS)'},
        {'label': '2-Manifold Topology (V, E, F)', 'value': 'V=14, E=36, F=24 · χ=2'},
        {'label': 'Divergence Signed Volume', 'value': '24,000.0 mm³ (err = 0.00%)'},
        {'label': 'Fuzz & Knockout Gate', 'value': '4/4 Fuzz + Defect REJECTED'},
    ],
    'steps': [
        'Stage 1: Khronos GLB Binary Header & Chunk Bounds Audit — Unpack the 12-byte header (<3I: '
        'magic 0x46546C67, version 2, total_len = 2,716 B) and check 4-byte-aligned JSON (1,896 B) '
        'and BIN (792 B) chunks plus all four bufferViews and finite float attributes.',
        'Stage 2: Directed Half-Edge Manifold Closure (3F = 2E, β_0 = 1) — Build the directed '
        'half-edge table {(u, v)} across all 24 triangles and check zero degenerate faces, zero '
        'duplicate half-edges, reverse twin pairing (v, u), and single-shell connectivity.',
        'Stage 3: Cross-Format Volume & Topology Parity — Compute χ = V − E + F = 2 and V_mesh = '
        '(1/6) ∑ v_0 · (v_1 × v_2) = 24,000.0 mm³ across x01_artifact.glb, comment-stripped Part-21 '
        'x01_artifact.step, and millimeter-unit x01_artifact.3mf.',
        'Stage 4: Malformed-Binary Fuzz Suite & Planted-Defect Knockout — Run the parser and '
        'manifold verifier against 4 malformed GLB fuzz files (truncated header, chunk OOB, vertex '
        'index OOB, flipped normal) and --planted-defect, checking that each defect fails.',
    ],
    'rules': [
        'Binary Chunk Containment Invariant: JSON and BIN chunks must be 4-byte aligned, every glTF '
        'bufferView and accessor span must lie within [0, BIN_byteLength], and every triangle index '
        'must be below POSITION.count.',
        'Watertight Single-Shell 2-Manifold Invariant: Across GLB, STEP, and 3MF, every directed '
        'half-edge (u, v) appears once with reverse twin (v, u) on one connected shell (β_0 = 1, '
        '3F = 2E, χ = 2).',
        'Planted-Defect Sensitivity Invariant: Flipping Triangle 0 ((0, 3, 8) → (0, 8, 3)) produces '
        '3 duplicate and 3 unpaired half-edges and drops signed volume from 24,000.0 to 22,000.0 mm³.',
    ],
    'sidenote_1': {
        'kicker': 'SIDENOTE X.01-A · WHY ZERO THIRD-PARTY WEBGL RUNTIME MATTERS',
        'body': (
            'Loading an external 3D runtime obscures how binary chunks map to GPU attributes. '
            'In src/modules/glb-viewer.mjs, parseGlbBuffer checks GLB headers, bufferViews, and '
            'accessor bounds before uploading buffers to WebGL2 and driving client-side CAD export.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE X.01-B · PLANTED-DEFECT FALSIFICATION',
        'body': (
            'A verifier that only prints PASS tells you little. Every verify_x*.py script checks '
            'the committed files first, then flips Triangle 0 and injects malformed 3MF XML in '
            'memory to check that failure paths stay live.'
        ),
    },
    'walkthrough': [
        'Orbit, zoom, and toggle Wireframe or Cross-Section Z-Slice on the live WebGL2 canvas below '
        'to inspect the 14-vertex, 24-triangle calibration manifold.',
        'Scrub Calibration Prism Length and Calibration Prism Height, or click [⚡ Planted-Defect / '
        'Boundary Knockout (Verifier FAIL)], to see how flipping Triangle 0 creates 3 duplicate and '
        '3 unpaired half-edges and lowers signed volume to 22,000.0 mm³.',
        'Download x01_artifact.glb, x01_artifact.step, or x01_artifact.3mf and run python '
        'skills/toolchain/x01/verify_x01_toolchain_x01_glb_inspector_validator.py locally.',
    ],
    't0_t1_certified': [
        'Zero-dependency WebGL2 GLB inspector and client-side GLB/STEP/DXF exporter in '
        'src/modules/glb-viewer.mjs (parseGlbBuffer + encodeCustomStepString).',
        'Deterministic Python stdlib generator (skills/toolchain/x01/make_x01.py) emitting '
        'x01_artifact.glb (2,716 B), faceted ISO 10303-21 POLY_LOOP x01_artifact.step (10,356 B), '
        'x01_artifact.3mf (1,672 B), manifest.json, and 4 malformed fuzz fixtures.',
        'Byte-level stdlib verifier (verify_x01_toolchain_x01_glb_inspector_validator.py) checking '
        'V = 14, E = 36, F = 24, β_0 = 1, χ = 2, and V = 24,000.0 mm³ across GLB, STEP, and 3MF '
        'plus 4/4 fuzz and planted-defect rejection.',
    ],
    't2_t3_open_horizon': [
        'Educational Geometry Boundary: Every file on this page is an educational artifact and is '
        'not certified as load-bearing, printable, safe, or fit for any purpose; combinatorial '
        '2-manifold checks do not test geometric self-intersection or structural strength.',
        'Future Edition 2 Extensions: Analytic NURBS EDGE_LOOP STEP AP242 surfaces, Draco/Meshopt '
        'buffer compression, and KTX2 GPU textures remain outside this v1 static-mesh subset.',
    ],
    'act4_human_ai': (
        'Language models can draft parametric mesh scripts in seconds, yet neural token predictors '
        'have no built-in spatial check; generated meshes routinely contain out-of-bounds indices, '
        'unpaired seams, or inverted face windings that look plausible under flat shading. Folio X.01 '
        'models a practical division of labor between human designer, coding agent, and deterministic '
        'verification code. The designer sets dimensions, clearances, and fabrication intent; an '
        'agent edits candidate geometry scripts guided by the companion SKILL.md; and the Python '
        'standard-library verifier decides whether each exported binary forms a closed single-shell '
        'manifold. By checking GLB chunk alignment, bufferView containment, comment-stripped STEP and '
        'millimeter 3MF face topology, and signed volume offline, the verifier rejects corrupt '
        'artifacts byte by byte before they enter a studio repository.'
    ),
    'act4_deepening': (
        'These byte-level and topological checks connect directly to the four companion monographs '
        'linked below. In Architecture, polyhedral graphic statics (Folio A.11) balances spatial '
        'frames through closed reciprocal force polyhedra where open facets break static equilibrium '
        '(Akbarzadeh, Van Mele, & Block, 2015, DOI 10.1016/j.cad.2015.01.006). In Engineering, '
        'extruded wall buckling and slicing models for 3D concrete printing (Folio E.10) rely on '
        'oriented shell geometry along the print path (Suiker, 2018, DOI '
        '10.1016/j.ijmecsci.2018.01.010). In Mathematics, persistent homology (Folio M.10) tracks '
        'Betti numbers and Euler characteristics across simplicial filtrations over binary boundary '
        'matrices (Edelsbrunner, Letscher, & Zomorodian, 2002, DOI 10.1007/s00454-002-2885-2). In '
        'structural optimization (Folio E.11), converting SIMP density fields (Sigmund, 2001, DOI '
        '10.1007/s001580050176) into printable struts likewise depends on watertight 2-manifold '
        'verification.'
    ),
    'sources': [
        'Khronos Group. (2022). glTF 2.0 Specification / ISO/IEC 12113:2022 Information technology — '
        'Runtime 3D asset delivery format. https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html',
        'Mirtich, B. (1996). Fast and accurate computation of polyhedral mass properties. Journal of '
        'Graphics Tools, 1(2), 31–50. DOI 10.1080/10867651.1996.10487458',
        'Meyer, M., Desbrun, M., Schröder, P., & Barr, A. H. (2003). Discrete differential-geometry '
        'operators for triangulated 2-manifolds. Visualization and Mathematics III, 35–57. DOI '
        '10.1007/978-3-662-05105-4_2',
        'Crane, K., de Goes, F., Desbrun, M., & Schröder, P. (2013). Digital geometry processing '
        'with discrete exterior calculus. ACM SIGGRAPH 2013 Courses. DOI 10.1145/2504435.2504442',
        'Feeney, A. B., Frechette, S. P., & Srinivasan, V. (2015). A portrait of an ISO STEP '
        'tolerancing standard as an enabler of smart manufacturing systems. Journal of Computing and '
        'Information Science in Engineering, 15(2), 021001. DOI 10.1115/1.4029050',
        'Akbarzadeh, M., Van Mele, T., & Block, P. (2015). On the equilibrium of funicular '
        'polyhedral frames and convex polyhedral force diagrams. Computer-Aided Design, 63, 118–128. '
        'DOI 10.1016/j.cad.2015.01.006',
        'Suiker, A. S. J. (2018). Mechanical performance of wall structures in 3D printing '
        'processes: Theory, design tools and experiments. International Journal of Mechanical '
        'Sciences, 137, 145–170. DOI 10.1016/j.ijmecsci.2018.01.010',
        'Edelsbrunner, H., Letscher, D., & Zomorodian, A. (2002). Topological persistence and '
        'simplification. Discrete & Computational Geometry, 28(4), 511–533. DOI '
        '10.1007/s00454-002-2885-2',
        'Sigmund, O. (2001). A 99 line topology optimization code written in Matlab. Structural and '
        'Multidisciplinary Optimization, 21(2), 120–127. DOI 10.1007/s001580050176',
        'Lalish, E. (2023–2026). Manifold: Geometry library for topological robustness (Apache-2.0). '
        'https://github.com/elalish/manifold',
    ],
    'plain_es': (
        'Imaginen una linterna hueca armada con pequeños triángulos planos de cartulina. Para cerrar '
        'el volumen sin huecos, cada costura debe unir dos triángulos vecinos con el lado exterior '
        'orientado hacia afuera. En geometría digital, esa cáscara continua se llama malla hermética. '
        'Al exportar archivos entre programas de diseño, suelen aparecer fallos silenciosos: bordes '
        'sin coser, coordenadas redondeadas o una cara volteada hacia adentro que pasa desapercibida '
        'en pantalla pero detiene el corte o la simulación. Este visor gratuito en el navegador web '
        'les permite abrir archivos binarios en tres dimensiones sin instalar programas adicionales. '
        'Pueden girar el prisma de calibración, revisar cortes transversales y observar cada '
        'triángulo. Con un clic, cualquier estudiante o despacho independiente puede descargar los '
        'modelos y el verificador en Python para auditar sus archivos sin licencias costosas.'
    ),
    'deep_es': (
        'La verificación de una malla poligonal combina topología combinatoria y cálculo vectorial. '
        'Por el teorema de la divergencia de Gauss-Ostrogradsky, el volumen encerrado se obtiene '
        'sumando tetraedros con signo sobre los triángulos frontera (Mirtich, 1996). Para que la '
        'frontera sea una 2-variedad orientable de una sola componente conexa, cada semi-arista '
        'dirigida debe emparejarse con una gemela inversa, cumpliendo tres caras por cada dos '
        'aristas y característica de Euler igual a dos en género cero. En x01_artifact.glb (2,716 '
        'bytes), el verificador revisa la cabecera de doce bytes, la alineación de cuatro bytes y '
        'los cuatro bufferViews antes de contrastar topología y volumen contra x01_artifact.step y '
        'x01_artifact.3mf. Si el Triángulo 0 invierte su orientación, aparecen tres semi-aristas '
        'duplicadas y tres sin pareja, y el volumen con signo baja de 24,000.0 a 22,000.0 mm³.'
    ),
    'distill_diagram': {
        'analogy_title': 'The Stitched Leather Ball & Seams',
        'analogy_sub': 'Each seam joins two outward-facing patches around a closed shell.',
        'force_a_title': 'Directed Half-Edge Pairing (3F = 2E)',
        'force_a_sub': 'Each directed half-edge pairs with one reverse twin on one shell.',
        'force_b_title': 'Signed Divergence Volume V(Ω)',
        'force_b_sub': 'Origin-anchored tetrahedra sum to 24,000.0 mm³ when normals face out.',
        'threshold_title': 'Euler–Poincaré & Half-Edge Gate (χ = 2)',
        'threshold_pass': 'Closed Genus-0 Shell: paired half-edges, β_0 = 1, χ = 2, 24,000.0 mm³.',
        'threshold_fail': 'Open Seam or Flipped Normal: half-edge pairing or signed volume fails.',
    },
}
