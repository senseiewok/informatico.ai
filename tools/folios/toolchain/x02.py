# -*- coding: utf-8 -*-
"""Tech & Tools · The Toolbox — Folio X.02: Code-First Parametric Solids & Measured STEP AP242, 3MF, and GLB Round-Trip Fidelity."""

FOLIO = {'slug': 'x02',
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
 'subtitle': 'Empowering solo mechanical and civil engineers to generate exact B-rep solids from '
             'version-controlled Python scripts and measure exactly what survives—and what is '
             'lost—across STEP AP242, 3MF, and GLB.',
 'subtitle_es': 'Empoderando a ingenieros mecánicos y civiles independientes para generar sólidos '
                'B-rep exactos desde scripts en Python bajo control de versiones y medir qué se '
                'conserva y qué se pierde entre STEP AP242, 3MF y GLB.',
 'why_en': "Independent engineers and small hardware shops shouldn't need $5,000-per-seat "
           'proprietary CAD licenses just to version-control a bracket, clevis, or structural node '
           'in Git. Code-first CAD in Python lets you parameterize every dimension as an equation, '
           'diff changes in pull requests, and export STEP AP242, 3MF, and GLB with a mathematical '
           'audit of chordal tessellation error.',
 'why_es': 'Los ingenieros independientes y talleres pequeños no deberían necesitar licencias '
           'propietarias de $5,000 USD anuales solo para controlar versiones de una pieza o nodo '
           'estructural en Git. El CAD basado en código Python permite parametrizar cada '
           'dimensión, revisar diffs en pull requests y exportar STEP AP242, 3MF y GLB auditando '
           'el error cordal de teselación.',
 'governing_law': 'h_sagitta = R (1 − cos(π / N)) · V_step = V_flange + V_boss = 43,200 mm³ · ΔV / '
                  'V < 10⁻⁶',
 'pass_pill_en': 'PASS · V = 43,200 mm³ · h_32 = 0.0722 mm · AP242 + 3MF + GLB',
 'pass_pill_es': 'APROBADO · V = 43,200 mm³ · h_32 = 0.0722 mm · AP242 + 3MF + GLB',
 'generator_script': 'skills/toolchain/x02/make_x02.py',
 'verifier_script': 'skills/toolchain/x02/verify_x02_toolchain_x02_parametric_step_3mf_roundtrip.py',
 'skill_dir': 'skills/toolchain/x02',
 'skill_name': 'toolchain-x02-parametric-step-3mf-roundtrip',
 'formats': ('glb', 'step', '3mf'),
 'primary_doi': '10.1115/1.4029050',
 'scite_summary': 'ISO 10303-242 (STEP AP242) boundary-representation exchange semantics (Feeney '
                  'et al., 2015) and chordal tessellation error bounds verified offline.',
 'date_published': '2026-11-08',
 'date_redated': '2026-11-08',
 'current_edition': 'REV 1.0',
 'reading_time': '22 MIN READ',
 'small_studio_kit_en': "Independent Engineer's Zero-Cost Stack (build123d Apache-2.0 + FreeCAD "
                        '1.0 + OrcaSlicer): Author parametric parts in Python, export ISO 10303-21 '
                        'STEP AP242 for CNC machine shops and 3MF for additive prototyping, and '
                        'run verify_x02 to confirm zero volume drift between B-rep and mesh.',
 'small_studio_kit_es': 'Stack sin Costo para Ingenieros Independientes (build123d Apache-2.0 + '
                        'FreeCAD 1.0 + OrcaSlicer): Modela piezas paramétricas en Python, exporta '
                        'STEP AP242 (ISO 10303-21) para maquinado CNC y 3MF para manufactura '
                        'aditiva, y ejecuta verify_x02 para certificar cero deriva volumétrica.',
 'companion_folios': [('engineering',
                       'e10',
                       'Folio E.10',
                       '3D Concrete Printing Thixotropy & Suiker Buckling'),
                      ('engineering',
                       'e06',
                       'Folio E.06',
                       'ASCE 7-22 Lead-Rubber Seismic Base Isolation'),
                      ('engineering',
                       'e11',
                       'Folio E.11',
                       'SIMP Topology Optimization & Inerter Dampers'),
                      ('math',
                       'm05',
                       'Folio M.05',
                       'AlphaGeometry 2 Neuro-Symbolic Euclidean Synthesis')],
 'external_links': [('gumyr/build123d (Apache-2.0 Python BREP CAD)',
                     'https://github.com/gumyr/build123d'),
                    ('CadQuery/cadquery (Apache-2.0 Parametric CAD)',
                     'https://github.com/CadQuery/cadquery'),
                    ('3MF Consortium Core Specification',
                     'https://github.com/3MFConsortium/spec_core')],
 'act1_dropcap': 'In the drafty computer laboratories of Cambridge University during the early '
                 '1970s, Ian Braid and Charles Lang wrestled with a quiet revolution on glowing '
                 'cathode-ray screens. For generations, machinists and patternmakers had shaped '
                 'turbine housings and gearbox casings using chalk markings, wooden templates, and '
                 'steel calipers. Translating those curved, interlocking metal solids into '
                 'computer memory seemed almost impossible. Wireframe sketches looked like ghostly '
                 'spiderwebs that could not tell solid metal from empty air, while faceted polygon '
                 'approximations stripped away the silky smooth curves of cylindrical bores. '
                 'Alongside Hungarian researcher Timothy Varady in Budapest, Braid helped pioneer '
                 'boundary representation, defining physical objects by their true geometric '
                 'boundaries: smooth analytical planes, cylinders, and topological loops. Decades '
                 'later, international standards teams codified that vision into the universal '
                 'STEP AP242 standard, ensuring that precise geometric forms could travel freely '
                 'between different software tools without losing their exact analytical curvature '
                 'or dimensional truth.',
 'act1_body': 'For decades, mechanical and structural engineering remained tethered to expensive, '
              'closed-source CAD ecosystems that stored geometry in proprietary binary formats. '
              'Sharing a model between different modeling programs frequently resulted in '
              'translated geometry losing its parametric history, trimming curves failing to '
              'evaluate, and cylindrical surfaces collapsing into crude triangle approximations. '
              'The ratification of ISO 10303-21 STEP AP242 (Feeney et al., 2015, DOI: '
              '10.1115/1.4029050) — established an open, model-based engineering foundation for '
              'boundary representations. Instead of approximating curved shapes as flat polygons, '
              'STEP '
              'AP242 defines solids through explicit topological hierarchies: CARTESIAN_POINT, '
              'VERTEX_POINT, POLY_LOOP, and ADVANCED_FACE entities bounded within a CLOSED_SHELL. '
              'In Folio X.02, we demonstrate how open Python libraries such as build123d and '
              'CadQuery liberate engineers from commercial lock-in. A single version-controlled '
              'Python script generates our stepped structural clevis pedestal, producing an exact '
              'ISO STEP AP242 boundary representation alongside modern 3MF and binary GLB mesh '
              'files. Our byte-level verifier inspects all three formats simultaneously, '
              'confirming that analytical volumes match exactly while measuring the chordal '
              'tessellation error introduced whenever smooth analytic surfaces are converted into '
              'faceted meshes.',
 'pullquote': 'Code-first CAD turns a mechanical drawing from an opaque binary blob into a pure '
              'function: parameters go in, and verified STEP AP242, 3MF, and GLB artifacts come '
              'out with known chordal error bounds.',
 'chronology': [('1973–1980',
                 'Ian Braid (Cambridge) and Charles Eastman pioneer boundary-representation '
                 '(B-rep) and constructive solid geometry (CSG) kernels.'),
                ('1994–2014',
                 'ISO 10303 (STEP) evolves from AP203/AP214 to AP242 Managed Model-Based 3D '
                 'Engineering, unifying product manufacturing information (PMI) and exact B-rep '
                 'topology.'),
                ('2015',
                 'The 3MF Consortium releases the open XML/ZIP 3MF specification to replace '
                 'unitless, non-manifold 1987 STL files.'),
                ('2018–2026',
                 'CadQuery 2 and build123d (Apache-2.0) bring algebraic Python scripting to '
                 'OpenCascade, liberating solo engineers from proprietary CAD lock-in.')],
 'act2_intuition': 'When an exact boundary representation is converted into a triangle mesh for '
                   'visualization or additive fabrication, curved geometries undergo inevitable '
                   'discretization error. Consider a circular cylindrical bore or boss of nominal '
                   'radius R approximated by an inscribed regular polygon with N flat facets. The '
                   'distance between the true circular arc and the center of each inscribed facet '
                   'chord is governed by the chordal sagitta formula: h = R(1 − cos(π / N)). Using '
                   'Taylor series expansion for large N, this geometric deviation scales inversely '
                   'with the square of facet count: h ≈ R π² / (2 N²). For a cylindrical locating '
                   'bore with radius R = 15 mm, setting N = 12 creates a chordal sagitta of 0.511 '
                   'mm—an error massive enough to prevent mating pins from fitting. Doubling N to '
                   '24 reduces the sagitta to 0.128 mm, while N = 32 reaches 0.0722 mm, fitting '
                   'within standard sliding tolerances. In contrast, planar stepped B-rep faces '
                   'retain their exact analytic volume V = 43,200.0 mm³ identically across STEP '
                   'AP242, 3MF, and GLB containers, illustrating the mathematical distinction '
                   'between exact boundary geometry and faceted representations.',
 'sliders': [{'id': 'tp-tool-s0',
              'label': 'Circumferential Tessellation Facets N',
              'min': 8,
              'max': 64,
              'step': 4,
              'value': 32,
              'unit': 'N = '},
             {'id': 'tp-tool-s1',
              'label': 'Upper Boss Height H_boss',
              'min': 10,
              'max': 30,
              'step': 2,
              'value': 18,
              'unit': ' mm'}],
 'readouts': [{'label': 'Exact B-Rep / Mesh Volume', 'value': '43,200.0 mm³ (ΔV = 0.00%)'},
              {'label': 'Chordal Sagitta Error h(N)', 'value': '0.0722 mm (at R=15, N=32)'},
              {'label': 'STEP AP242 Schema Audit', 'value': 'CLOSED_SHELL · 28 FACES PASS'},
              {'label': '3MF & GLB Parity Verdict', 'value': 'PASS · SHA-256 VERIFIED'}],
 'steps': ['Stage 1: Algebraic Python Solid Definition — Parameterize the stepped flange (60 × 40 '
           '× 12 mm) and boss (40 × 20 × 18 mm) as a single closed 2-manifold boundary with '
           'V_exact = 28,800 + 14,400 = 43,200.0 mm³.',
           'Stage 2: ISO 10303-21 STEP AP242 B-Rep Serialization — Emit explicit CARTESIAN_POINT, '
           'VERTEX_POINT, POLY_LOOP, ADVANCED_FACE, CLOSED_SHELL, and MANIFOLD_SOLID_BREP entities '
           'with millimeter length units (#7) and 10⁻⁵ mm uncertainty (#6).',
           'Stage 3: Deterministic 3MF ZIP & GLB Binary Packaging — Package the identical '
           '16-vertex, 28-triangle topology into 3MF Core 1.2.3 XML (fixed ZIP timestamp) and '
           'Khronos GLB binary buffers with embedded provenance metadata.',
           'Stage 4: Cross-Format Round-Trip & Chordal Deviation Audit — Verify that STEP, 3MF, '
           'and GLB agree on vertex/face counts and analytical volume, and bound circular bore '
           'discretization error via h = R(1 − cos(π/N)).'],
 'rules': ['Cross-Format Topological Identity: The vertex count (V = 16), face count (F = 28), and '
           'Euler characteristic (χ = 2) must match identically across x02_artifact.step, '
           'x02_artifact.3mf, and x02_artifact.glb.',
           'Chordal Sagitta Tolerance Bound: For any cylindrical feature of radius R discretized '
           'into N segments, the radial deviation is strictly h = R(1 − cos(π/N)); keeping h ≤ '
           '0.10 mm at R = 15 mm requires N ≥ 28.',
           'Provenance & Planted-Defect Gate: Every exported file must embed the generator script '
           'SHA-256 and boundary statement, and verify_x02 must reject any flipped-normal or '
           'corrupted-schema mutation.'],
 'sidenote_1': {'kicker': 'SIDENOTE X.02-A · WHY STL SHOULD RETIRE IN FAVOR OF 3MF & STEP',
                'body': 'The 1987 STL format stores raw triangle soup with no units, no vertex '
                        'sharing, no material metadata, and no license/provenance block. 3MF and '
                        'STEP AP242 preserve explicit units (mm) and shared vertex indices.'},
 'sidenote_2': {'kicker': 'SIDENOTE X.02-B · APACHE-2.0 BUILD123D FOR SOLO ENGINEERS',
                'body': 'Unlike GPL-licensed script CAD tools whose copyleft terms can complicate '
                        'client deliverables, build123d and CadQuery are licensed under '
                        'Apache-2.0, making them clean for independent consulting engineers.'},
 'walkthrough': ['Inspect the stepped clevis pedestal in the live WebGL2 viewer below; toggle '
                 'Wireframe to see the seamless 16-vertex, 28-triangle shoulder transition at z = '
                 '12 mm.',
                 'Scrub Circumferential Facets N down from 32 to 8 (or click [⚡ Counterfactual '
                 'Axiom-Knockout]) to watch the chordal sagitta error h = R(1 − cos(π/N)) breach '
                 'the 0.10 mm pin-clearance budget.',
                 'Download x02_artifact.step, x02_artifact.3mf, and x02_artifact.glb to test '
                 'import fidelity in FreeCAD, Blender, or your slicer.'],
 't0_t1_certified': ['Deterministic generator (skills/toolchain/x02/make_x02.py) emitting '
                     'byte-reproducible STEP AP242 (.step), 3MF Core 1.2.3 (.3mf), and glTF 2.0 '
                     '(.glb) solids.',
                     'Stdlib cross-format verifier '
                     '(verify_x02_toolchain_x02_parametric_step_3mf_roundtrip.py) checking '
                     'ISO-10303-21 AP242 B-rep entities, 3MF ZIP XML structure, GLB manifoldness, '
                     'and V = 43,200.0 mm³.',
                     'Explicit Round-Trip Survival Matrix documenting what survives across STEP '
                     'AP242, 3MF, and GLB (units, topology, colors, provenance).'],
 't2_t3_open_horizon': ['Educational Geometry Boundary: Every file on this page is an educational '
                        'artifact; nothing is certified as load-bearing, printable, safe, or fit '
                        'for any purpose.',
                        'Future Edition 2 Extensions: Analytic NURBS trimmed-surface STEP AP242 '
                        'export via build123d/OCCT C++ bindings and automated PMI semantic '
                        'tolerance extraction.'],
 'sources': ['ISO 10303-242:2022. Industrial automation systems and integration — Product data '
             'representation and exchange — Part 242: Application protocol: Managed model-based 3D '
             'engineering.',
             'Feeney, A. B., Frechette, S. P., & Srinivasan, V. (2015). A portrait of an ISO STEP '
             'tolerancing standard as an enabler of smart manufacturing systems. Journal of '
             'Computing and Information Science in Engineering, 15(2), 021001. DOI '
             '10.1115/1.4029050',
             '3MF Consortium. (2023). 3D Manufacturing Format Core Specification & Reference Guide '
             'v1.2.3. https://github.com/3MFConsortium/spec_core',
             'build123d Contributors. (2023–2026). build123d: A python CAD programming library '
             '(Apache-2.0). https://github.com/gumyr/build123d'],
 'act1_plain_bridge': 'Think of designing a precision metal bracket like writing a recipe. Instead '
                      'of drawing fixed lines, you write down clear rules. You specify that the '
                      'base is sixty millimeters long and the mounting boss sits centered on top. '
                      'If you change one measurement, the entire part updates automatically. That '
                      'is what parametric modeling means. But trouble starts when you share your '
                      'file. Different manufacturing tools speak completely different languages. '
                      'Some tools expect true curved surfaces, while others convert everything '
                      'into flat triangular facets. When a round hole turns into flat facets, the '
                      'opening shrinks slightly. Pins that should slide smoothly get stuck. Our '
                      'free interactive tool solves this headache. Right in your browser, you can '
                      'inspect an exact stepped pedestal in three dimensions. You can adjust the '
                      'facet count and watch how the roundness changes in real time. In seconds, '
                      'you can download verified files and Python scripts to audit your own parts.',
 'act1_stakes': 'For an independent mechanical consultant or a small hardware team, file exchange '
                'discrepancies between software tools create costly friction. When a client sends '
                'a model exported through an unchecked conversion pipeline, subtle geometric '
                'corruptions can slip through unnoticed. A circular cylindrical bore faceted into '
                'thirty-two chords shrinks by more than seventy microns along its radius. If an '
                'assembler tries to slide a hardened steel locating dowel into that faceted '
                'opening, the pin seizes tight, halting physical assembly. Worse still, '
                'proprietary CAD vendors charge upwards of five thousand dollars per seat each '
                'year, locking solo practitioners out of professional revision-control and '
                'file-checking workflows. Open, script-driven CAD coupled with offline '
                'verification democratizes this entire engineering cycle. By parameterizing parts '
                'in readable Python code and executing byte-level audits across STEP, 3MF, and GLB '
                'exports, solo practitioners can mathematically prove geometric integrity, verify '
                'clearance limits, and collaborate seamlessly with machining facilities without '
                'costly proprietary software.',
 'act2_analogy': 'Picture a master carpenter cutting a traditional Japanese watari-ago notched '
                 'timber joint with a razor-sharp hand chisel. When shaping the interlocking tenon '
                 'and mortise, every wooden face must be planed perfectly flat, meeting cleanly at '
                 'right angles. If the carpenter pares away just a quarter-millimeter too much '
                 'wood, the joint wobbles loosely and loses its grip. If the cut remains too '
                 'tight, the beams refuse to slide together. A true solid CAD model demands that '
                 'same exacting tactile fit: surfaces must meet with zero accidental gaps, '
                 'preserving exact boundaries and precise physical clearances.',
 'act2_plain_primer': 'Before diving into technical formulas, take a look at the two controls and '
                      'the counterfactual test in our interactive workbench. The first slider '
                      'adjusts the Circumferential Tessellation Facets, labeled N. When converting '
                      'a round hole or cylindrical boss into a 3D mesh, the computer approximates '
                      'the circle with a polygon of N sides. At low values like eight or twelve, '
                      'the circle looks noticeably chunky and shrinks inward, cutting into your '
                      'clearance tolerance. As you slide N up toward thirty-two or sixty-four, the '
                      'faceted shape hugs the true cylinder closely. The second slider changes the '
                      'Upper Boss Height, growing or shrinking the top stepped pedestal. Watch how '
                      'the exact mathematical volume recalculates instantly while keeping the base '
                      'flange unchanged. Finally, try the Planted-Defect Knockout button. Clicking '
                      'it intentionally drops the facet count or corrupts the schema, immediately '
                      'breaching the tolerance threshold and triggering an audit failure that '
                      'alerts the designer before any material is cut.',
 'act2_deepening': 'Inside a boundary representation kernel, solid bodies are not stored as loose '
                   'surface meshes, but as evaluated topological graphs anchored by precise '
                   'geometric definitions. A closed solid shell is constructed through the Boolean '
                   'union of oriented half-spaces, where each planar face is bounded by a directed '
                   'closed wire known in ISO 10303-21 syntax as a POLY_LOOP. In our stepped clevis '
                   'pedestal, the base flange (sixty by forty by twelve millimeters) merges with '
                   'the upper boss (forty by twenty by eighteen millimeters) along a shared planar '
                   'boundary at elevation z = 12 mm. Rather than retaining an internal dividing '
                   'wall, the kernel executes half-space regularization, dissolving redundant '
                   'internal faces and sewing outer faces into a single MANIFOLD_SOLID_BREP '
                   'bounded by a CLOSED_SHELL entity. Each ADVANCED_FACE explicitly references its '
                   'underlying surface equation, boundary orientation flag, and bounding vertex '
                   'loop. This topological rigor guarantees that every edge is shared by exactly '
                   'two adjacent faces with opposing parameter orientations, ensuring that '
                   'analytical mass properties and volume integrals evaluate without approximation '
                   'drift across neutral CAD exchange formats.',
 'act4_human_ai': 'In modern parametric CAD engineering, artificial intelligence tools can '
                  'generate complex solid modeling scripts in Python upon request. However, large '
                  'language models frequently invent nonexistent API methods, misplace Boolean '
                  'coordinate offsets, or hallucinate topological connections that produce invalid '
                  'non-manifold geometry or unstitched boundary shells. Folio X.02 introduces a '
                  'disciplined co-design workflow that prevents these failure modes. The human '
                  'engineer defines the mechanical interface requirements, dimensional tolerances, '
                  'and aesthetic proportions. The AI coding agent implements the parametric recipe '
                  'in Python using build123d or CadQuery syntax, adhering to portable rules '
                  'documented in our companion SKILL.md guide. Before any generated STEP AP242, '
                  '3MF, or GLB file is accepted into production, verify_x02 executes a fully '
                  'automated, offline verification pass. The verifier parses the STEP entity '
                  'graph, audits XML triangle indices in 3MF archives, validates binary GLB '
                  'buffers, and checks the chordal sagitta error against specified pin-clearance '
                  'tolerances. This mathematical gatekeeper ensures that the generative speed of '
                  'artificial intelligence is harnessed safely, leaving human engineers in '
                  'complete command of physical intent and functional geometry.',
 'act4_deepening': 'The boundary-representation and round-trip verification methodologies '
                   'developed in Folio X.02 form a vital connective bridge across Informatico.ai. '
                   'In Civil and Structural Engineering, modeling elastomeric bearings for seismic '
                   'base isolation (Folio E.06) demands precise parametric cylindrical boss '
                   'geometry to verify lead-core confinement clearances under cyclic lateral shear '
                   'displacement. In Advanced Manufacturing, toolpath synthesis for 3D concrete '
                   'printing (Folio E.10) requires exact STEP B-rep solids to compute thixotropic '
                   'bead slicing and avoid nozzle trajectory deviations. In Computational '
                   'Mechanics, SIMP topology optimization (Folio E.11) outputs organic density '
                   'distributions that must be reconstructed into smooth boundary-representation '
                   'solids for CNC milling operations. In Mathematics, neuro-symbolic geometry '
                   'synthesis (Folio M.05) bridges algebraic constraint systems with Euclidean '
                   'constructive geometry, matching the dual representation of parametric code and '
                   'evaluated B-rep entities. By mastering code-first CAD modeling in open Python, '
                   'solo engineers acquire a unified computational toolchain capable of expressing '
                   'complex physical concepts across civil, mechanical, and mathematical '
                   'disciplines without proprietary constraints or commercial software barriers.',
 'plain_es': 'Diseñar una pieza mecánica mediante código paramétrico es como escribir una receta '
             'clara en lugar de hacer un dibujo estático. En lugar de trazar líneas fijas, '
             'definimos dimensiones mediante fórmulas matemáticas. Por ejemplo, indicamos que la '
             'base mide sesenta milímetros de largo y que el soporte superior se ubica justo en el '
             'centro. Si más adelante cambiamos una medida, toda la pieza se actualiza de forma '
             'automática. El verdadero reto surge al compartir el archivo con talleres y '
             'colaboradores. Algunos sistemas requieren superficies analíticas perfectamente '
             'curvas, mientras que otros programas convierten todo en pequeños triángulos planos. '
             'Al transformar un orificio circular en caras planas, el diámetro efectivo se reduce '
             'y los pasadores metálicos pueden atascarse. Nuestra herramienta interactiva en el '
             'navegador les permite explorar un pedestal escalonado, ajustar el número de '
             'divisiones circulares y observar cómo cambia la redondez en tiempo real. En pocos '
             'segundos, pueden descargar modelos verificados y rutinas en Python para auditar sus '
             'propias piezas sin pagar licencias comerciales.',
 'deep_es': 'El intercambio de modelos geométricos entre formatos neutros ilustra la tensión '
            'matemática entre representaciones de frontera exactas y aproximaciones discretizadas '
            'por teselación. El estándar ISO 10303-21 STEP AP242 preserva definiciones topológicas '
            'analíticas mediante entidades MANIFOLD_SOLID_BREP compuestas por bucles cerrados y '
            'caras avanzadas, asegurando que el volumen teórico permanezca inalterado. En '
            'contraste, formatos como 3MF y GLB aproximan las superficies curvas mediante mallas '
            'de triángulos planos. Cuando se discretiza un cilindro circular de radio nominal en '
            'un polígono regular de N facetas, la desviación cordal máxima o sagita introduce una '
            'reducción radial calculada mediante la función trigonométrica correspondiente. A '
            'valores bajos de facetas, esta discrepancia dimensional puede impedir el ensamblaje '
            'adecuado de pasadores y bujes mecánicos. Al combinar scripts de modelado paramétrico '
            'en Python con verificadores deterministas que operan a nivel de bytes, los ingenieros '
            'independientes pueden certificar la equivalencia volumétrica entre representaciones '
            'continuas y discretas, garantizando tolerancias de holgura controladas sin depender '
            'de costosas plataformas comerciales.',
 'distill_diagram': {'analogy_title': 'The Notched Timber & Sliding Fit',
                     'analogy_sub': 'Exact planar faces and controlled tolerances ensure snug '
                                    'joint fit.',
                     'force_a_title': 'Analytic B-Rep Solid (STEP AP242)',
                     'force_a_sub': 'Exact mathematical cylinders, planes, and closed topological '
                                    'shells.',
                     'force_b_title': 'Chordal Tessellation Sagitta h(N)',
                     'force_b_sub': 'Polygon discretization pulls cylindrical walls inward by '
                                    'h(N).',
                     'threshold_title': 'Pin Clearance Tolerance (h ≤ 0.10 mm)',
                     'threshold_pass': 'Fine Tessellation (N ≥ 28): h ≤ 0.10 mm, mating pins slide '
                                       'free.',
                     'threshold_fail': 'Coarse Facets (N < 28): Sagitta h > 0.10 mm, mating pins '
                                       'seize.'}}
