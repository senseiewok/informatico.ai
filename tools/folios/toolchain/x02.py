# -*- coding: utf-8 -*-
"""Tech & Tools · The Toolbox — Folio X.02: Code-First Parametric Solids & Measured STEP AP242, 3MF, and GLB Round-Trip Fidelity."""

FOLIO = {
    'slug': 'x02',
    'folio_id': 'X.02',
    'tool_id': 'TOOL-ENG-1',
    'cat': 'engineering',
    'plate_slug': 'x02',
    'pillar_label_en': 'Engineering Toolbox · Code-First Parametric CAD & STEP AP242',
    'pillar_label_es': 'Herramientas de Ingeniería · CAD Paramétrico en Código y STEP AP242',
    'badge_en': 'TOOLBOX X.02 · BUILD123D / CADQUERY KERNEL → STEP AP242 · 3MF · GLB AUDIT',
    'badge_es': 'HERRAMIENTA X.02 · KERNEL BUILD123D / CADQUERY → AUDITORÍA STEP AP242 · 3MF · GLB',
    'title': 'Code-First Parametric Solids & Measured STEP AP242, 3MF, and GLB Round-Trip Fidelity',
    'title_es': 'Sólidos Paramétricos en Código y Fidelidad Medida entre STEP AP242, 3MF y GLB',
    'subtitle': (
        'Authoring version-controlled Python solids for independent mechanical and civil '
        'engineers while auditing planar volume parity and cylindrical chordal sagitta across '
        'STEP Part 21, 3MF, and GLB.'
    ),
    'subtitle_es': (
        'Modelado de sólidos paramétricos en Python bajo control de versiones para ingenieros '
        'mecánicos y civiles independientes, auditando volumen planar y sagita cordal entre '
        'STEP Parte 21, 3MF y GLB.'
    ),
    'why_en': (
        "Independent engineers and small hardware shops shouldn't need $5,000-per-seat "
        'commercial CAD licenses just to version-control a bracket, clevis, or structural node '
        'in Git. Code-first CAD in Python lets you parameterize dimensions as readable equations, '
        'review diffs in pull requests, and audit neutral exchange files offline for mesh '
        'topology and chordal tessellation error.'
    ),
    'why_es': (
        'Los ingenieros independientes y talleres pequeños no deberían pagar licencias '
        'comerciales de $5,000 USD anuales solo para versionar una ménsula o nodo estructural '
        'en Git. El CAD en código Python permite parametrizar cada cota, revisar cambios en '
        'pull requests y auditar archivos neutros fuera de línea en topología de malla y sagita '
        'cordal.'
    ),
    'governing_law': (
        'h_sagitta = R (1 − cos(π / N)) · V_step = V_flange + V_boss = 43,200 mm³ · ΔV / V < 10⁻⁶'
    ),
    'pass_pill_en': 'PASS · V = 43,200 mm³ · h_32 = 0.0722 mm · AP242 + 3MF + GLB',
    'pass_pill_es': 'APROBADO · V = 43,200 mm³ · h_32 = 0.0722 mm · AP242 + 3MF + GLB',
    'generator_script': 'skills/toolchain/x02/make_x02.py',
    'verifier_script': 'skills/toolchain/x02/verify_x02_toolchain_x02_parametric_step_3mf_roundtrip.py',
    'skill_dir': 'skills/toolchain/x02',
    'skill_name': 'toolchain-x02-parametric-step-3mf-roundtrip',
    'formats': ('glb', 'step', '3mf'),
    'primary_doi': '10.1115/1.4029050',
    'scite_summary': (
        'Grounded in Braid (1975), Requicha (1980), Cha Zhang & Tsuhan Chen (2001), and '
        'Feeney et al. (2015) ISO 10303-242 STEP AP242 exchange semantics.'
    ),
    'date_published': '2026-11-08',
    'date_redated': '2026-11-08',
    'current_edition': 'REV 1.0',
    'reading_time': '22 MIN READ',
    'small_studio_kit_en': (
        "Independent Engineer's Open Stack (build123d Apache-2.0 + FreeCAD 1.0 + OrcaSlicer): "
        'Use build123d or CadQuery on OpenCascade to export production ISO 10303-242 STEP AP242 '
        'EDGE_LOOP solids for CNC shops, open x02_artifact.3mf and x02_artifact.glb in slicers '
        'or Blender, and run verify_x02 to audit our illustrative Part-21 STEP sketch, 3MF, and '
        'GLB for 43,200.0 mm³ volume and chordal sagitta bounds.'
    ),
    'small_studio_kit_es': (
        'Stack Abierto para Ingenieros Independientes (build123d Apache-2.0 + FreeCAD 1.0 + '
        'OrcaSlicer): Usa build123d o CadQuery sobre OpenCascade para exportar sólidos STEP '
        'AP242 (ISO 10303-242) con EDGE_LOOP para talleres CNC, abre x02_artifact.3mf y '
        'x02_artifact.glb en laminadores o Blender, y ejecuta verify_x02 para auditar el esquema '
        'ilustrativo Parte 21, 3MF y GLB en volumen (43,200.0 mm³) y sagita cordal.'
    ),
    'companion_folios': [
        ('engineering', 'e10', 'Folio E.10', '3D Concrete Printing Thixotropy & Suiker Buckling'),
        ('engineering', 'e06', 'Folio E.06', 'ASCE 7-22 Lead-Rubber Seismic Base Isolation'),
        ('engineering', 'e11', 'Folio E.11', 'SIMP Topology Optimization & Inerter Dampers'),
        ('math', 'm05', 'Folio M.05', 'AlphaGeometry 2 Neuro-Symbolic Euclidean Synthesis'),
    ],
    'external_links': [
        ('gumyr/build123d (Apache-2.0 Python BREP CAD)', 'https://github.com/gumyr/build123d'),
        ('CadQuery/cadquery (Apache-2.0 Parametric CAD)', 'https://github.com/CadQuery/cadquery'),
        ('3MF Consortium Core Specification', 'https://github.com/3MFConsortium/spec_core'),
    ],
    'act1_dropcap': (
        'At the University of Cambridge Computer-Aided Design Group in 1975, Ian Braid published '
        'a solid-modeling program that built mechanical parts from six primitive shapes, '
        'including rectangular blocks, cylinders, wedges, and pierced plates. Earlier computer '
        'drawings stored only wireframe lines, which could not separate solid metal from empty '
        'air. Coarse polygon approximations created a second shop-floor hazard. Replacing a '
        'round locating bore with a handful of flat chords pulled the wall inward and pinched '
        'mating pins. Braid represented each body by its boundary instead, linking oriented '
        'faces, edges, and vertex loops around one closed interior volume. At the University of '
        'Rochester in 1980, Aristides Requicha formalized the topological closure rules that '
        'distinguish valid rigid solids from dangling faces. Auditing vertex pairing, enclosed '
        'volume, and chordal sagitta still guards open geometry files before any material is cut.'
    ),
    'act1_body': (
        'For decades, mechanical and structural engineering workflows relied on closed-source '
        'CAD programs whose binary files stripped parametric history or broke trimmed surfaces '
        'during translation. Building on the boundary-representation work of Braid (1975, DOI: '
        '10.1145/360715.360727) and the regularized solid-modeling theory of Requicha (1980, '
        'DOI: 10.1145/356827.356833), ISO 10303-242 STEP AP242 (Feeney et al., 2015, DOI: '
        '10.1115/1.4029050), serialized in ISO 10303-21 clear text, exchanges full B-rep solids '
        'through EDGE_LOOP, ADVANCED_FACE, and SHAPE_DEFINITION_REPRESENTATION entities when '
        'authored on OpenCascade via Apache-2.0 Python libraries such as build123d or CadQuery. '
        'In Folio X.02, our zero-dependency stdlib script make_x02.py emits a rectilinear '
        'stepped clevis pedestal (60 × 40 × 12 mm flange plus 40 × 20 × 18 mm boss) as 16 '
        'vertices and 28 triangles across binary glTF 2.0 (GLB), 3MF Core 1.2.3, and an '
        'illustrative Part-21 STEP entity sketch, while bounding cylindrical chordal sagitta.'
    ),
    'pullquote': (
        'Code-first CAD turns a mechanical part from an opaque binary file into an inspectable '
        'Python function: parameters go in, and open artifacts come out with checked 2-manifold '
        'topology, signed volume, and bounded chordal sagitta.'
    ),
    'chronology': [
        (
            '1975–1980',
            'Ian Braid at Cambridge (DOI 10.1145/360715.360727) and Aristides Requicha at '
            'Rochester (DOI 10.1145/356827.356833) formalize boundary-representation (B-rep) '
            'synthesis and regularized solid set operations.',
        ),
        (
            '1994–2015',
            'ISO 10303 pairs Part 21 ASCII clear-text encoding with ISO 10303-242 STEP AP242 '
            'Managed Model-Based 3D Engineering (Feeney et al., 2015, DOI 10.1115/1.4029050).',
        ),
        (
            '2001–2015',
            'Cha Zhang and Tsuhan Chen (DOI 10.1109/ICIP.2001.958278) formalize signed '
            'tetrahedral mesh volume integration; the 3MF Consortium releases unit-aware XML/ZIP '
            '3MF Core to replace unitless 1987 STL triangle soup.',
        ),
        (
            '2018–2026',
            'CadQuery 2 and build123d (Apache-2.0) bring Python scripting to OpenCascade so '
            'independent engineers can version-control parametric B-rep parts in Git.',
        ),
    ],
    'act2_intuition': (
        'Converting a smooth analytic cylinder into a triangle mesh for browser viewing or '
        'additive slicing introduces predictable polygon discretization error. For a circular '
        'locating bore of radius R approximated by an inscribed regular N-gon, the radial '
        'distance from the circular arc to the midpoint of each flat chord follows the sagitta '
        'relation h = R(1 − cos(π / N)), which behaves for large N as approximately R π² / '
        '(2 N²). On a reference bore of radius R = 15 mm, coarse tessellation at N = 12 facets '
        'pulls each chord inward by 0.5111 mm (and 1.1418 mm at N = 8), which could cause a '
        'precision dowel pin to bind. Raising N to 28 brings the sagitta down to 0.0943 mm '
        '(within a 0.10 mm clearance budget), and N = 32 reaches 0.0722 mm. By contrast, our '
        'exported stepped pedestal has purely planar orthogonal walls, so its 28 triangular '
        'facets enclose V = 43,200.0 mm³ without curved-surface discretization loss.'
    ),
    'sliders': [
        {
            'id': 'tp-tool-s0',
            'label': 'Circumferential Tessellation Facets N',
            'min': 8,
            'max': 64,
            'step': 4,
            'value': 32,
            'unit': 'N = ',
        },
        {
            'id': 'tp-tool-s1',
            'label': 'Upper Boss Height H_boss',
            'min': 10,
            'max': 30,
            'step': 2,
            'value': 18,
            'unit': ' mm',
        },
    ],
    'readouts': [
        {'label': 'Planar B-Rep / Mesh Volume', 'value': '43,200.0 mm³ (ΔV = 0.00%)'},
        {'label': 'Chordal Sagitta Error h(N)', 'value': '0.0722 mm (at R=15, N=32)'},
        {'label': 'STEP AP242 Schema Audit', 'value': 'CLOSED_SHELL · 28 FACES PASS'},
        {'label': '3MF & GLB Parity Verdict', 'value': 'PASS · SHA-256 VERIFIED'},
    ],
    'steps': [
        'Stage 1: Parametric Stepped-Pedestal Mesh — Construct the 4-ring rectilinear stepped '
        'pedestal (60 × 40 × 12 mm base flange plus 40 × 20 × 18 mm boss) as a single 16-vertex, '
        '28-triangle closed 2-manifold with analytical volume 28,800 + 14,400 = 43,200.0 mm³.',
        'Stage 2: Illustrative ISO 10303-21 Part-21 STEP Sketch — Serialize 16 VERTEX_POINT '
        'records and 28 triangular POLY_LOOP / PLANE face records in millimeter units (#7) for '
        'text inspection (use build123d / OpenCascade when EDGE_LOOP STEP AP242 import is needed).',
        'Stage 3: Deterministic 3MF Core 1.2.3 & GLB Packaging — Serialize the same 16 vertices '
        'and 28 triangles into fixed-timestamp 3MF ZIP XML and Khronos glTF 2.0 binary buffers '
        'with SHA-256 provenance recorded in manifest.json.',
        'Stage 4: Cross-Format Parity & Chordal Sagitta Audit — Parse STEP, 3MF, and GLB to '
        'check V = 16, F = 28, χ = 2, millimeter units, and signed volume 43,200.0 mm³ (Cha '
        'Zhang & Tsuhan Chen, 2001, DOI: 10.1109/ICIP.2001.958278), plus h(15, 32) = 0.072229 mm '
        '≤ 0.10 mm (N ≥ 28).',
    ],
    'rules': [
        'Cross-Format Topology, Unit & Volume Parity: Parsed DATA records in x02_artifact.step, '
        'millimeter XML in x02_artifact.3mf, and binary buffers in x02_artifact.glb must agree '
        'on V = 16, E = 42, F = 28, Euler χ = 2, and signed volume 43,200.0 mm³.',
        'Chordal Sagitta Clearance Bound: For a reference bore of radius R = 15 mm faceted into '
        'N chords, h = R(1 − cos(π/N)) equals 0.072229 mm at N = 32; keeping h ≤ 0.10 mm '
        'requires N ≥ 28 (whereas coarse N = 8 yields 1.1418 mm).',
        'Provenance & Planted-Defect Gate: Manifest SHA-256 hashes must match make_x02.py and '
        'all three artifacts, and verify_x02 must reject a flipped triangle normal, dropped STEP '
        'face, or unescaped ampersands in 3MF XML.',
    ],
    'sidenote_1': {
        'kicker': 'SIDENOTE X.02-A · WHY 3MF & STEP REPLACE UNITLESS 1987 STL',
        'body': (
            'Legacy 1987 STL files store disconnected triangle coordinates without units, '
            'shared vertex indices, or provenance metadata. Both 3MF Core 1.2.3 and STEP Part 21 '
            'declare explicit millimeter units and indexed vertex topology.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE X.02-B · ILLUSTRATIVE PART-21 SKETCH VS. OPENCASCADE STEP AP242',
        'body': (
            'Because make_x02.py uses only Python stdlib, x02_artifact.step is an illustrative '
            'Part-21 POLY_LOOP sketch rather than an OpenCascade-importable EDGE_LOOP + '
            'SHAPE_DEFINITION_REPRESENTATION solid; export production STEP AP242 via build123d '
            'or CadQuery.'
        ),
    },
    'walkthrough': [
        'Rotate the stepped clevis pedestal in the WebGL2 inspector below and toggle Wireframe '
        'to inspect the 16-vertex, 28-triangle shoulder terrace at z = 12 mm.',
        'Drag Circumferential Tessellation Facets N from 32 down below 28 (or click [⚡ '
        'Planted-Defect / Boundary Knockout], which sets N = 8) to watch h = R(1 − cos(π/N)) '
        'cross the 0.10 mm clearance threshold.',
        'Download x02_artifact.3mf, x02_artifact.glb, and x02_artifact.step, then run verify_x02 '
        'locally (and with --planted-defect) to inspect the JSON round-trip report.',
    ],
    't0_t1_certified': [
        'Stdlib generator (skills/toolchain/x02/make_x02.py) emitting watertight glTF 2.0 '
        '(.glb), 3MF Core 1.2.3 (.3mf), and an illustrative Part-21 STEP entity sketch (.step) '
        'for a stepped rectilinear pedestal.',
        'Stdlib verifier (verify_x02_toolchain_x02_parametric_step_3mf_roundtrip.py) parsing '
        'STEP DATA entities, 3MF XML, and GLB binary buffers for millimeter units, watertight '
        'χ = 2 topology, 43,200.0 mm³ signed volume, and h(15, 32) = 0.072229 mm ≤ 0.10 mm.',
        'Primary-source grounding in Braid (1975), Requicha (1980), Cha Zhang & Tsuhan Chen '
        '(2001), and Feeney et al. (2015) with offline DOI cache verification.',
    ],
    't2_t3_open_horizon': [
        'Educational Geometry Boundary: Every file on this page is an educational artifact; '
        'nothing is certified as load-bearing, printable, safe, or fit for any purpose.',
        'OpenCascade STEP AP242 Horizon: Full EDGE_LOOP, SHAPE_DEFINITION_REPRESENTATION, and '
        'CYLINDRICAL_SURFACE / NURBS STEP AP242 export requires build123d or CadQuery on '
        'OpenCascade rather than the stdlib Part-21 sketch shipped here.',
    ],
    'sources': [
        'Braid, I. C. (1975). The synthesis of solids bounded by many faces. Communications of '
        'the ACM, 18(4), 201–208. DOI 10.1145/360715.360727',
        'Requicha, A. A. G. (1980). Representations for rigid solids: Theory, methods, and '
        'systems. ACM Computing Surveys, 12(4), 437–464. DOI 10.1145/356827.356833',
        'Cha Zhang, & Tsuhan Chen. (2001). Efficient feature extraction for 2D/3D objects in '
        'mesh representation. Proceedings 2001 International Conference on Image Processing '
        '(ICIP), 3, 935–938. DOI 10.1109/ICIP.2001.958278',
        'Feeney, A. B., Frechette, S. P., & Srinivasan, V. (2015). A portrait of an ISO STEP '
        'tolerancing standard as an enabler of smart manufacturing systems. Journal of '
        'Computing and Information Science in Engineering, 15(2), 021001. DOI 10.1115/1.4029050',
        'Robinson, W. H. (1982). Lead-rubber hysteretic bearings suitable for protecting '
        'structures during earthquakes. Earthquake Engineering & Structural Dynamics, 10(4), '
        '593–604. DOI 10.1002/eqe.4290100408',
        'Sigmund, O. (2001). A 99 line topology optimization code written in Matlab. Structural '
        'and Multidisciplinary Optimization, 21(2), 120–127. DOI 10.1007/s001580050176',
        'Suiker, A. S. J. (2018). Mechanical performance of wall structures in 3D printing '
        'processes: Theory, design tools and experiments. International Journal of Mechanical '
        'Sciences, 137, 145–170. DOI 10.1016/j.ijmecsci.2018.01.010',
        'Trinh, T. H., Wu, Y., Le, Q. V., He, H., & Luong, T. (2024). Solving olympiad geometry '
        'without human demonstrations. Nature, 625, 476–482. DOI 10.1038/s41586-023-06747-5',
        'ISO 10303-242:2022 & ISO 10303-21:2016. Managed model-based 3D engineering (STEP '
        'AP242) and clear text encoding of the exchange structure.',
        '3MF Consortium. (2023). 3D Manufacturing Format Core Specification v1.2.3; and '
        'build123d Contributors (2023–2026), Apache-2.0 Python CAD library, '
        'https://github.com/gumyr/build123d',
    ],
    'act1_plain_bridge': (
        'Designing a metal bracket in code works much like writing a clear workshop recipe. '
        'Instead of dragging lines by hand, you state each measurement as a rule. Set a '
        'sixty-millimeter base flange and center a stepped mounting boss on top. Change one '
        'number, and the whole part updates together. Trouble often begins when you send that '
        'file to a machine shop or a printer. Milling software reads smooth analytic '
        'boundaries, whereas triangle-mesh printers chop curved holes into flat facets. Each '
        'flat facet pulls the wall slightly inward, so a locating pin may bind during assembly. '
        'On this page, you can turn a stepped pedestal in three dimensions and test how facet '
        'count changes bore clearance. Download the open files and run the companion Python '
        'script offline to check vertex, face, and volume counts yourself.'
    ),
    'act1_stakes': (
        'For an independent mechanical consultant or small hardware shop, silent geometry loss '
        'across file exports can stall fabrication. When a cylindrical bore of fifteen-millimeter '
        'radius is faceted into twelve chords instead of twenty-eight or thirty-two, inward '
        'chordal sagitta grows past half a millimeter, which may seize a hardened dowel pin '
        'during fit-up. At the same time, commercial CAD suites often cost several thousand '
        'dollars per seat annually and lock parametric feature trees inside proprietary binaries '
        'that Git cannot diff. Pairing Apache-2.0 Python kernels such as build123d or CadQuery '
        'with neutral STEP AP242 (Feeney et al., 2015, DOI: 10.1115/1.4029050), 3MF, and GLB '
        'workflows lets small teams keep dimensions in plain text, run automated byte-level '
        'topology checks in continuous integration, and share auditable artifacts with CNC '
        'machinists and additive fabricators.'
    ),
    'act2_analogy': (
        'A carpenter cutting a Japanese watari-ago notched timber joint planes each mortise and '
        'tenon cheek flat so opposing shoulders meet at clean right angles. Paring away a '
        'quarter-millimeter too much wood leaves the beam loose; leaving a proud ridge stops '
        'the joint from seating. Solid modeling requires similar geometric discipline so '
        'adjacent faces share edges cleanly without stray gaps. Where the analogy stops: timber '
        'swells with humidity and yields slightly along its grain, whereas digital boundary and '
        'mesh files fail through unpaired half-edges or polygon chordal shrinkage before any '
        'physical load is applied.'
    ),
    'act2_plain_primer': (
        'Two sliders and a knockout toggle control the interactive workbench below. The first '
        'slider sets Circumferential Tessellation Facets, modeling how many flat polygon sides '
        'approximate a fifteen-millimeter reference locating bore. At coarse settings such as '
        'eight or twelve facets, the flat chords pull inward across the opening and exceed a '
        'tenth-millimeter pin-clearance budget; at twenty-eight facets or higher, the chordal '
        'deviation stays within budget. The second slider adjusts Upper Boss Height on the '
        'stepped pedestal, updating the calculated block volume while keeping the base flange '
        'fixed. Clicking the Planted-Defect / Boundary Knockout button drops the facet slider to '
        'eight so the clearance alert fires in the browser, while running the Python verifier '
        'with its planted-defect flag flips a triangle normal in memory to test manifold '
        'rejection.'
    ),
    'act2_deepening': (
        'In Requicha’s (1980, DOI: 10.1145/356827.356833) solid-modeling framework, a valid '
        'rigid body is a regular closed point set (an r-set) whose boundary forms an orientable '
        '2-manifold without dangling faces or self-intersections. Full B-rep kernels such as '
        'OpenCascade construct stepped solids via regularized Boolean union, dissolving the '
        'shared interior patch at z = 12 mm and exporting EDGE_LOOP boundaries. Our stdlib '
        'generator make_x02.py builds the same stepped polyhedron directly by stitching four '
        'rectangular vertex rings—outer 60 × 40 mm rings at z = 0 and z = 12 mm, stepping inward '
        'across an eight-triangle shoulder terrace to inner 40 × 20 mm rings at z = 12 and z = '
        '30 mm—into 16 shared vertices, 42 undirected edges, and 28 outward counter-clockwise '
        'triangles (3F = 2E, Euler characteristic χ = V − E + F = 2). Evaluating the signed '
        'origin-tetrahedron sum V = (1/6) ∑ v₀ · (v₁ × v₂) (Cha Zhang & Tsuhan Chen, 2001, DOI: '
        '10.1109/ICIP.2001.958278) yields 43,200.0 mm³ across GLB, 3MF, and the Part-21 sketch.'
    ),
    'act4_human_ai': (
        'Language models asked to write parametric Python CAD scripts can draft flange and boss '
        'dimensions quickly, yet they may also hallucinate API calls, invert face winding, or '
        'confuse faceted meshes with OpenCascade EDGE_LOOP B-reps. Folio X.02 pairs human '
        'tolerance specification with a deterministic offline check in verify_x02 rather than '
        'trusting generated files by eye. The human engineer sets the interface dimensions and '
        'the 0.10 mm bore-sagitta ceiling; make_x02.py emits the reference .glb, .3mf, and '
        'illustrative .step files alongside manifest.json; and verify_x02 checks SHA-256 '
        'hashes, millimeter unit tags, watertight χ = 2 topology, and 43,200.0 mm³ signed '
        'volume across all three files, checks h(15, 32) = 0.072229 mm ≤ 0.10 mm (requiring '
        'N ≥ 28), and verifies that flipped normals, dropped STEP faces, and malformed 3MF XML '
        'are rejected.'
    ),
    'act4_deepening': (
        'Verified parametric geometry connects directly to four companion Folios on '
        'Informatico.ai. In seismic isolation (Folio E.06), lead-rubber elastomeric bearings '
        '(Robinson, 1982, DOI: 10.1002/eqe.4290100408) depend on concentric cylindrical core '
        'and shim tolerances under cyclic shear. In additive construction (Folio E.10), '
        'mechanistic wall-buckling and toolpath models for 3D concrete printing (Suiker, 2018, '
        'DOI: 10.1016/j.ijmecsci.2018.01.010) slice stepped solid geometry into layered '
        'extrusion paths. In structural optimization (Folio E.11), density fields from SIMP '
        'penalization (Sigmund, 2001, DOI: 10.1007/s001580050176) require boundary '
        'reconstruction into watertight solids before machining or printing. And in formal '
        'geometry (Folio M.05), neuro-symbolic Euclidean synthesis in AlphaGeometry (Trinh et '
        'al., 2024, DOI: 10.1038/s41586-023-06747-5) mirrors the pairing of symbolic rules with '
        'an independent geometric checker.'
    ),
    'plain_es': (
        'Diseñar un soporte metálico mediante código funciona como escribir una receta clara de '
        'taller. En vez de arrastrar líneas a mano en la computadora, ustedes definen cada '
        'medida como una regla. Fijan una brida base de sesenta milímetros y centran encima un '
        'bloque escalonado. Cambian un número y toda la pieza se actualiza junta. El problema '
        'suele aparecer al compartir el archivo con un taller de maquinado o impresión. El '
        'maquinado lee fronteras geométricas continuas, mientras las mallas de impresión cortan '
        'los barrenos redondos en caras planas. Cada cara plana reduce un poco el claro '
        'interior y un pasador de acero puede atorarse al ensamblar. Aquí pueden girar el '
        'pedestal en tres dimensiones y probar cómo el número de divisiones afecta esa holgura. '
        'También pueden descargar los archivos abiertos y correr la rutina en Python para '
        'revisar vértices, caras y volumen.'
    ),
    'deep_es': (
        'El intercambio de sólidos entre formatos abiertos distingue las fronteras B-rep '
        'analíticas de las mallas trianguladas (Braid, 1975; Requicha, 1980). En OpenCascade '
        '(build123d o CadQuery), el protocolo ISO 10303-242 (STEP AP242; Feeney et al., 2015) '
        'codificado en texto ISO 10303-21 emplea EDGE_LOOP y SHAPE_DEFINITION_REPRESENTATION; '
        'nuestro generador en biblioteca estándar make_x02.py emite un esquema ilustrativo '
        'Parte 21 con 16 puntos VERTEX_POINT y 28 bucles POLY_LOOP cuya malla cerrada en '
        'milímetros coincide en topología (χ = 2) y volumen con signo (43,200.0 mm³; Cha Zhang '
        'y Tsuhan Chen, 2001) con 3MF y GLB. Para un barreno de referencia R = 15 mm aproximado '
        'por N facetas, la sagita cordal h = R(1 − cos(π/N)) mide 0.5111 mm en N = 12, baja a '
        '0.0722 mm en N = 32 y exige N ≥ 28 para mantenerse dentro de 0.10 mm.'
    ),
    'distill_diagram': {
        'analogy_title': 'The Notched Timber & Sliding Fit',
        'analogy_sub': 'Planed flat cheeks and bounded clearances let mating joints seat cleanly.',
        'force_a_title': 'Analytic B-Rep Solid (STEP AP242)',
        'force_a_sub': 'Closed OpenCascade EDGE_LOOP shells in ISO 10303-242 (or planar Part-21 sketch).',
        'force_b_title': 'Chordal Tessellation Sagitta h(N)',
        'force_b_sub': 'Polygon discretization pulls cylindrical bore walls inward by h(N).',
        'threshold_title': 'Pin Clearance Tolerance (h ≤ 0.10 mm)',
        'threshold_pass': 'Fine Tessellation (N ≥ 28): h ≤ 0.10 mm, locating pins slide clear.',
        'threshold_fail': 'Coarse Facets (N < 28): Sagitta h > 0.10 mm, locating pins may bind.',
    },
}
